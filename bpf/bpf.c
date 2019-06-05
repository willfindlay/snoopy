#include "bpf/defs.h"

#define PID THE_PID

// perf buffer definitions {{{

BPF_PERF_OUTPUT(syscalls);

// }}}


// --- hook for system call entry ---

TRACEPOINT_PROBE(raw_syscalls, sys_enter)
{
    u64 syscall = args->id;
    u64 pid_tgid = bpf_get_current_pid_tgid();

    if((u32)(pid_tgid >> 32) == PID)
    {
        snoopy_sys_enter_data data = {.sysnum=syscall, .name=""};

        syscalls.perf_submit((struct pt_regs*)args, &data, sizeof(data));
    }

    return 0;
}


// --- hook for system call returns ---

TRACEPOINT_PROBE(raw_syscalls, sys_exit)
{


    return 0;
}
