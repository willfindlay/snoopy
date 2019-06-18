#include "bpf/defs.h"

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

// perf buffer definitions {{{

BPF_PERF_OUTPUT(syscalls);

// }}}

// --- hook for system call entry ---

TRACEPOINT_PROBE(raw_syscalls, sys_enter)
{
    u64 syscall = args->id;
    u64 pid_tgid = bpf_get_current_pid_tgid();

    snoopy_sys_enter_data data = {.id=syscall, .pid_tgid=pid_tgid};

    if((u32)(pid_tgid >> 32) == PID)
    {
        syscalls.perf_submit((struct pt_regs*)args, &data, sizeof(data));
    }

    return 0;
}


// --- hook for system call returns ---

TRACEPOINT_PROBE(raw_syscalls, sys_exit)
{

    return 0;
}
