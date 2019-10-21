#include "snoopy.h"

#define TRACE_PID __TRACE_PID

BPF_ARRAY(__syscall_init, struct syscall, 1);

BPF_PERF_OUTPUT(on_syscall);

TRACEPOINT_PROBE(raw_syscalls, sys_enter)
{
    u32 pid = bpf_get_current_pid_tgid() >> 32;
    if (pid != TRACE_PID)
        return 0;

    int zero = 0;
    struct syscall *syscall = __syscall_init.lookup(&zero);

    if (!syscall)
        return 0;

    syscall->num = args->id;

    for (int i = 0; i < SNOOPY_NUM_ARGS; i++)
    {
        syscall->args[i] = args->args[i];
        bpf_probe_read_str(syscall->str_args[i], SNOOPY_ARGLEN, (char *)args->args[i]);
    }

    on_syscall.perf_submit((struct pt_regs *) args, syscall, sizeof(struct syscall));
    return 0;
}

TRACEPOINT_PROBE(raw_syscalls, sys_exit)
{
    u32 pid = bpf_get_current_pid_tgid() >> 32;
    if (pid != TRACE_PID)
        return 0;

    return 0;
}
