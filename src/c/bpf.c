#include "snoopy.h"

#define TRACE_PID __TRACE_PID

BPF_PERF_OUTPUT(on_syscall);

TRACEPOINT_PROBE(raw_syscalls, sys_enter)
{
    u32 pid = bpf_get_current_pid_tgid() >> 32;
    if (pid != TRACE_PID)
        return 0;

    struct syscall syscall = { .num=args->id };

    for (int i = 0; i < SNOOPY_NUM_ARGS; i++)
    {
        syscall.args[i] = args->args[i];
    }

    on_syscall.perf_submit((struct pt_regs *) args, &syscall, sizeof(syscall));
    return 0;
}

TRACEPOINT_PROBE(raw_syscalls, sys_exit)
{
    u32 pid = bpf_get_current_pid_tgid() >> 32;
    if (pid != TRACE_PID)
        return 0;

    return 0;
}
