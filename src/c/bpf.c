#define TRACE_PID __TRACE_PID

TRACEPOINT_PROBE(raw_syscalls, sys_enter)
{
    return 0;
}

TRACEPOINT_PROBE(raw_syscalls, sys_exit)
{
    return 0;
}
