#include <uapi/linux/ptrace.h>

#include "BPFDIR/defs.h"

#define PID THE_PID

// TODO: maybe use some of this
//struct alloc_info_t
//{
//        u64 size;
//        u64 timestamp_ns;
//        int stack_id;
//};
//
//struct combined_alloc_info_t
//{
//        u64 total_size;
//        u64 number_of_allocs;
//};
//BPF_HASH(sizes, u64, u64);
//BPF_HASH(allocs, u64, struct alloc_info_t, 1000000);
//BPF_HASH(memptrs, u64, u64);
//BPF_STACK_TRACE(stack_traces, 10240);
//BPF_HASH(combined_allocs, u64, struct combined_alloc_info_t, 10240);

/* --- perf buffers --- */
BPF_PERF_OUTPUT(syscalls);

/* per-cpu map to store in-progress syscalls */
BPF_PERCPU_ARRAY(ip_syscalls, syscall_data, 1);

/* --- hook for system call entry --- */
TRACEPOINT_PROBE(raw_syscalls, sys_enter)
{
    u64 syscall = args->id;
    u64 pid_tgid = bpf_get_current_pid_tgid();
    int zero = 0;

    syscall_data data = {.id=syscall, .pid_tgid=pid_tgid, .args={}, .ret=0};

    for(int i = 0; i < 6; i++)
    {
        data.args[i] = args->args[i];
        bpf_probe_read_str(data.str_args[i], ARGLEN, (char *)args->args[i]);
    }

    if((u32)(pid_tgid >> 32) == PID)
    {
        //syscalls.perf_submit((struct pt_regs*)args, &data, sizeof(data));
        ip_syscalls.update(&zero, &data);

        if(syscall == SYS_EXIT || syscall == SYS_EXIT_GROUP)
            syscalls.perf_submit((struct pt_regs*)args, &data, sizeof(syscall_data));
    }

    return 0;
}


/* --- hook for system call returns --- */
TRACEPOINT_PROBE(raw_syscalls, sys_exit)
{
    u64 pid_tgid = bpf_get_current_pid_tgid();
    int zero = 0;

    syscall_data *datap = ip_syscalls.lookup(&zero);

    if(!datap)
        return 0;

    datap->ret = args->ret;

    if((u32)(pid_tgid >> 32) == PID)
    {
        syscalls.perf_submit((struct pt_regs*)args, datap, sizeof(syscall_data));
    }

    return 0;
}
