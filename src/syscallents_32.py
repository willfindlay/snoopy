MAX_SYSCALL_NUM = 386
SYSCALLS = [
     (   # 0
    "restart_syscall",
    0,
    [
ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 1
    "exit",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 2
    "fork",
    0,
    [
ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 3
    "read",
    3,
    [
ARG_INT, ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 4
    "write",
    3,
    [
ARG_INT, ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 5
    "open",
    3,
    [
ARG_STR, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 6
    "close",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 7
    "waitpid",
    3,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 8
    "creat",
    2,
    [
ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 9
    "link",
    2,
    [
ARG_STR, ARG_STR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 10
    "unlink",
    1,
    [
ARG_STR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 11
    "execve",
    3,
    [
ARG_STR, ARG_PTR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 12
    "chdir",
    1,
    [
ARG_STR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 13
    "time",
    1,
    [
ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 14
    "mknod",
    3,
    [
ARG_STR, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 15
    "chmod",
    2,
    [
ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 16
    "lchown",
    3,
    [
ARG_STR, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 17
    "break",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 18
    "oldstat",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 19
    "lseek",
    3,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 20
    "getpid",
    0,
    [
ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 21
    "mount",
    5,
    [
ARG_STR, ARG_STR, ARG_STR, ARG_INT, ARG_PTR, ARG_UNKNOWN
]),

     (   # 22
    "umount",
    2,
    [
ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 23
    "setuid",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 24
    "getuid",
    0,
    [
ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 25
    "stime",
    1,
    [
ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 26
    "ptrace",
    4,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 27
    "alarm",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 28
    "oldfstat",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 29
    "pause",
    0,
    [
ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 30
    "utime",
    2,
    [
ARG_STR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 31
    "stty",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 32
    "gtty",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 33
    "access",
    2,
    [
ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 34
    "nice",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 35
    "ftime",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 36
    "sync",
    0,
    [
ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 37
    "kill",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 38
    "rename",
    2,
    [
ARG_STR, ARG_STR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 39
    "mkdir",
    2,
    [
ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 40
    "rmdir",
    1,
    [
ARG_STR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 41
    "dup",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 42
    "pipe",
    1,
    [
ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 43
    "times",
    1,
    [
ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 44
    "prof",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 45
    "brk",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 46
    "setgid",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 47
    "getgid",
    0,
    [
ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 48
    "signal",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 49
    "geteuid",
    0,
    [
ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 50
    "getegid",
    0,
    [
ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 51
    "acct",
    1,
    [
ARG_STR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 52
    "umount2",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 53
    "lock",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 54
    "ioctl",
    3,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 55
    "fcntl",
    3,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 56
    "mpx",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 57
    "setpgid",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 58
    "ulimit",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 59
    "oldolduname",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 60
    "umask",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 61
    "chroot",
    1,
    [
ARG_STR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 62
    "ustat",
    2,
    [
ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 63
    "dup2",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 64
    "getppid",
    0,
    [
ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 65
    "getpgrp",
    0,
    [
ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 66
    "setsid",
    0,
    [
ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 67
    "sigaction",
    3,
    [
ARG_INT, ARG_PTR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 68
    "sgetmask",
    0,
    [
ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 69
    "ssetmask",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 70
    "setreuid",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 71
    "setregid",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 72
    "sigsuspend",
    3,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 73
    "sigpending",
    1,
    [
ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 74
    "sethostname",
    2,
    [
ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 75
    "setrlimit",
    2,
    [
ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 76
    "getrlimit",
    2,
    [
ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 77
    "getrusage",
    2,
    [
ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 78
    "gettimeofday",
    2,
    [
ARG_PTR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 79
    "settimeofday",
    2,
    [
ARG_PTR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 80
    "getgroups",
    2,
    [
ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 81
    "setgroups",
    2,
    [
ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 82
    "select",
    5,
    [
ARG_INT, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_UNKNOWN
]),

     (   # 83
    "symlink",
    2,
    [
ARG_STR, ARG_STR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 84
    "oldlstat",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 85
    "readlink",
    3,
    [
ARG_STR, ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 86
    "uselib",
    1,
    [
ARG_STR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 87
    "swapon",
    2,
    [
ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 88
    "reboot",
    4,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 89
    "readdir",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 90
    "mmap",
    6,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_INT
]),

     (   # 91
    "munmap",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 92
    "truncate",
    2,
    [
ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 93
    "ftruncate",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 94
    "fchmod",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 95
    "fchown",
    3,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 96
    "getpriority",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 97
    "setpriority",
    3,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 98
    "profil",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 99
    "statfs",
    2,
    [
ARG_STR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 100
    "fstatfs",
    2,
    [
ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 101
    "ioperm",
    3,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 102
    "socketcall",
    2,
    [
ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 103
    "syslog",
    3,
    [
ARG_INT, ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 104
    "setitimer",
    3,
    [
ARG_INT, ARG_PTR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 105
    "getitimer",
    2,
    [
ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 106
    "stat",
    2,
    [
ARG_STR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 107
    "lstat",
    2,
    [
ARG_STR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 108
    "fstat",
    2,
    [
ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 109
    "olduname",
    1,
    [
ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 110
    "iopl",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 111
    "vhangup",
    0,
    [
ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 112
    "idle",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 113
    "vm86old",
    1,
    [
ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 114
    "wait4",
    4,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 115
    "swapoff",
    1,
    [
ARG_STR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 116
    "sysinfo",
    1,
    [
ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 117
    "ipc",
    6,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_INT
]),

     (   # 118
    "fsync",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 119
    "sigreturn",
    0,
    [
ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 120
    "clone",
    5,
    [
ARG_INT, ARG_INT, ARG_PTR, ARG_PTR, ARG_INT, ARG_UNKNOWN
]),

     (   # 121
    "setdomainname",
    2,
    [
ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 122
    "uname",
    1,
    [
ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 123
    "modify_ldt",
    3,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 124
    "adjtimex",
    1,
    [
ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 125
    "mprotect",
    3,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 126
    "sigprocmask",
    3,
    [
ARG_INT, ARG_PTR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 127
    "create_module",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 128
    "init_module",
    3,
    [
ARG_PTR, ARG_INT, ARG_STR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 129
    "delete_module",
    2,
    [
ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 130
    "get_kernel_syms",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 131
    "quotactl",
    4,
    [
ARG_INT, ARG_STR, ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 132
    "getpgid",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 133
    "fchdir",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 134
    "bdflush",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 135
    "sysfs",
    3,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 136
    "personality",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 137
    "afs_syscall",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 138
    "setfsuid",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 139
    "setfsgid",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 140
    "_llseek",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 141
    "getdents",
    3,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 142
    "_newselect",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 143
    "flock",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 144
    "msync",
    3,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 145
    "readv",
    3,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 146
    "writev",
    3,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 147
    "getsid",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 148
    "fdatasync",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 149
    "_sysctl",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 150
    "mlock",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 151
    "munlock",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 152
    "mlockall",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 153
    "munlockall",
    0,
    [
ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 154
    "sched_setparam",
    2,
    [
ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 155
    "sched_getparam",
    2,
    [
ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 156
    "sched_setscheduler",
    3,
    [
ARG_INT, ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 157
    "sched_getscheduler",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 158
    "sched_yield",
    0,
    [
ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 159
    "sched_get_priority_max",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 160
    "sched_get_priority_min",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 161
    "sched_rr_get_interval",
    2,
    [
ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 162
    "nanosleep",
    2,
    [
ARG_PTR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 163
    "mremap",
    5,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN
]),

     (   # 164
    "setresuid",
    3,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 165
    "getresuid",
    3,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 166
    "vm86",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 167
    "query_module",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 168
    "poll",
    3,
    [
ARG_PTR, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 169
    "nfsservctl",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 170
    "setresgid",
    3,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 171
    "getresgid",
    3,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 172
    "prctl",
    5,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN
]),

     (   # 173
    "rt_sigreturn",
    0,
    [
ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 174
    "rt_sigaction",
    4,
    [
ARG_INT, ARG_PTR, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 175
    "rt_sigprocmask",
    4,
    [
ARG_INT, ARG_PTR, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 176
    "rt_sigpending",
    2,
    [
ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 177
    "rt_sigtimedwait",
    4,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 178
    "rt_sigqueueinfo",
    3,
    [
ARG_INT, ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 179
    "rt_sigsuspend",
    2,
    [
ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 180
    "pread64",
    4,
    [
ARG_INT, ARG_STR, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 181
    "pwrite64",
    4,
    [
ARG_INT, ARG_STR, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 182
    "chown",
    3,
    [
ARG_STR, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 183
    "getcwd",
    2,
    [
ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 184
    "capget",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 185
    "capset",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 186
    "sigaltstack",
    2,
    [
ARG_PTR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 187
    "sendfile",
    4,
    [
ARG_INT, ARG_INT, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 188
    "getpmsg",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 189
    "putpmsg",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 190
    "vfork",
    0,
    [
ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 191
    "ugetrlimit",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 192
    "mmap2",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 193
    "truncate64",
    2,
    [
ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 194
    "ftruncate64",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 195
    "stat64",
    2,
    [
ARG_STR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 196
    "lstat64",
    2,
    [
ARG_STR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 197
    "fstat64",
    2,
    [
ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 198
    "lchown32",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 199
    "getuid32",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 200
    "getgid32",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 201
    "geteuid32",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 202
    "getegid32",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 203
    "setreuid32",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 204
    "setregid32",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 205
    "getgroups32",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 206
    "setgroups32",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 207
    "fchown32",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 208
    "setresuid32",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 209
    "getresuid32",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 210
    "setresgid32",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 211
    "getresgid32",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 212
    "chown32",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 213
    "setuid32",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 214
    "setgid32",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 215
    "setfsuid32",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 216
    "setfsgid32",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 217
    "pivot_root",
    2,
    [
ARG_STR, ARG_STR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 218
    "mincore",
    3,
    [
ARG_INT, ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 219
    "madvise",
    3,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 220
    "getdents64",
    3,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 221
    "fcntl64",
    3,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

 ( "UNKNOWN_222", 6, [ARG_UNKNOWN,ARG_UNKNOWN,ARG_UNKNOWN,ARG_UNKNOWN,ARG_UNKNOWN,ARG_UNKNOWN]),
 ( "UNKNOWN_223", 6, [ARG_UNKNOWN,ARG_UNKNOWN,ARG_UNKNOWN,ARG_UNKNOWN,ARG_UNKNOWN,ARG_UNKNOWN]),
     (   # 224
    "gettid",
    0,
    [
ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 225
    "readahead",
    3,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 226
    "setxattr",
    5,
    [
ARG_STR, ARG_STR, ARG_PTR, ARG_INT, ARG_INT, ARG_UNKNOWN
]),

     (   # 227
    "lsetxattr",
    5,
    [
ARG_STR, ARG_STR, ARG_PTR, ARG_INT, ARG_INT, ARG_UNKNOWN
]),

     (   # 228
    "fsetxattr",
    5,
    [
ARG_INT, ARG_STR, ARG_PTR, ARG_INT, ARG_INT, ARG_UNKNOWN
]),

     (   # 229
    "getxattr",
    4,
    [
ARG_STR, ARG_STR, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 230
    "lgetxattr",
    4,
    [
ARG_STR, ARG_STR, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 231
    "fgetxattr",
    4,
    [
ARG_INT, ARG_STR, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 232
    "listxattr",
    3,
    [
ARG_STR, ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 233
    "llistxattr",
    3,
    [
ARG_STR, ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 234
    "flistxattr",
    3,
    [
ARG_INT, ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 235
    "removexattr",
    2,
    [
ARG_STR, ARG_STR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 236
    "lremovexattr",
    2,
    [
ARG_STR, ARG_STR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 237
    "fremovexattr",
    2,
    [
ARG_INT, ARG_STR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 238
    "tkill",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 239
    "sendfile64",
    4,
    [
ARG_INT, ARG_INT, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 240
    "futex",
    6,
    [
ARG_PTR, ARG_INT, ARG_INT, ARG_PTR, ARG_PTR, ARG_INT
]),

     (   # 241
    "sched_setaffinity",
    3,
    [
ARG_INT, ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 242
    "sched_getaffinity",
    3,
    [
ARG_INT, ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 243
    "set_thread_area",
    1,
    [
ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 244
    "get_thread_area",
    1,
    [
ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 245
    "io_setup",
    2,
    [
ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 246
    "io_destroy",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 247
    "io_getevents",
    5,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_PTR, ARG_PTR, ARG_UNKNOWN
]),

     (   # 248
    "io_submit",
    3,
    [
ARG_INT, ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 249
    "io_cancel",
    3,
    [
ARG_INT, ARG_PTR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 250
    "fadvise64",
    4,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

 ( "UNKNOWN_251", 6, [ARG_UNKNOWN,ARG_UNKNOWN,ARG_UNKNOWN,ARG_UNKNOWN,ARG_UNKNOWN,ARG_UNKNOWN]),
     (   # 252
    "exit_group",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 253
    "lookup_dcookie",
    4,
    [
ARG_INT, ARG_INT, ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 254
    "epoll_create",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 255
    "epoll_ctl",
    4,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 256
    "epoll_wait",
    4,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 257
    "remap_file_pages",
    5,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN
]),

     (   # 258
    "set_tid_address",
    1,
    [
ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 259
    "timer_create",
    3,
    [
ARG_INT, ARG_PTR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 260
    "timer_settime",
    4,
    [
ARG_INT, ARG_INT, ARG_PTR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 261
    "timer_gettime",
    2,
    [
ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 262
    "timer_getoverrun",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 263
    "timer_delete",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 264
    "clock_settime",
    2,
    [
ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 265
    "clock_gettime",
    2,
    [
ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 266
    "clock_getres",
    2,
    [
ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 267
    "clock_nanosleep",
    4,
    [
ARG_INT, ARG_INT, ARG_PTR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 268
    "statfs64",
    3,
    [
ARG_STR, ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 269
    "fstatfs64",
    3,
    [
ARG_INT, ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 270
    "tgkill",
    3,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 271
    "utimes",
    2,
    [
ARG_STR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 272
    "fadvise64_64",
    4,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 273
    "vserver",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 274
    "mbind",
    6,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_PTR, ARG_INT, ARG_INT
]),

     (   # 275
    "get_mempolicy",
    5,
    [
ARG_PTR, ARG_PTR, ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN
]),

     (   # 276
    "set_mempolicy",
    3,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 277
    "mq_open",
    4,
    [
ARG_STR, ARG_INT, ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 278
    "mq_unlink",
    1,
    [
ARG_STR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 279
    "mq_timedsend",
    5,
    [
ARG_INT, ARG_STR, ARG_INT, ARG_INT, ARG_PTR, ARG_UNKNOWN
]),

     (   # 280
    "mq_timedreceive",
    5,
    [
ARG_INT, ARG_STR, ARG_INT, ARG_PTR, ARG_PTR, ARG_UNKNOWN
]),

     (   # 281
    "mq_notify",
    2,
    [
ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 282
    "mq_getsetattr",
    3,
    [
ARG_INT, ARG_PTR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 283
    "kexec_load",
    4,
    [
ARG_INT, ARG_INT, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 284
    "waitid",
    5,
    [
ARG_INT, ARG_INT, ARG_PTR, ARG_INT, ARG_PTR, ARG_UNKNOWN
]),

 ( "UNKNOWN_285", 6, [ARG_UNKNOWN,ARG_UNKNOWN,ARG_UNKNOWN,ARG_UNKNOWN,ARG_UNKNOWN,ARG_UNKNOWN]),
     (   # 286
    "add_key",
    5,
    [
ARG_STR, ARG_STR, ARG_PTR, ARG_INT, ARG_INT, ARG_UNKNOWN
]),

     (   # 287
    "request_key",
    4,
    [
ARG_STR, ARG_STR, ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 288
    "keyctl",
    5,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN
]),

     (   # 289
    "ioprio_set",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 290
    "ioprio_get",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 291
    "inotify_init",
    0,
    [
ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 292
    "inotify_add_watch",
    3,
    [
ARG_INT, ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 293
    "inotify_rm_watch",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 294
    "migrate_pages",
    4,
    [
ARG_INT, ARG_INT, ARG_PTR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 295
    "openat",
    4,
    [
ARG_INT, ARG_STR, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 296
    "mkdirat",
    3,
    [
ARG_INT, ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 297
    "mknodat",
    4,
    [
ARG_INT, ARG_STR, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 298
    "fchownat",
    5,
    [
ARG_INT, ARG_STR, ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN
]),

     (   # 299
    "futimesat",
    3,
    [
ARG_INT, ARG_STR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 300
    "fstatat64",
    4,
    [
ARG_INT, ARG_STR, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 301
    "unlinkat",
    3,
    [
ARG_INT, ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 302
    "renameat",
    4,
    [
ARG_INT, ARG_STR, ARG_INT, ARG_STR, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 303
    "linkat",
    5,
    [
ARG_INT, ARG_STR, ARG_INT, ARG_STR, ARG_INT, ARG_UNKNOWN
]),

     (   # 304
    "symlinkat",
    3,
    [
ARG_STR, ARG_INT, ARG_STR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 305
    "readlinkat",
    4,
    [
ARG_INT, ARG_STR, ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 306
    "fchmodat",
    3,
    [
ARG_INT, ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 307
    "faccessat",
    3,
    [
ARG_INT, ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 308
    "pselect6",
    6,
    [
ARG_INT, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 309
    "ppoll",
    5,
    [
ARG_PTR, ARG_INT, ARG_PTR, ARG_PTR, ARG_INT, ARG_UNKNOWN
]),

     (   # 310
    "unshare",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 311
    "set_robust_list",
    2,
    [
ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 312
    "get_robust_list",
    3,
    [
ARG_INT, ARG_PTR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 313
    "splice",
    6,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_PTR, ARG_INT, ARG_INT
]),

     (   # 314
    "sync_file_range",
    4,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 315
    "tee",
    4,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 316
    "vmsplice",
    4,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 317
    "move_pages",
    6,
    [
ARG_INT, ARG_INT, ARG_PTR, ARG_PTR, ARG_PTR, ARG_INT
]),

     (   # 318
    "getcpu",
    3,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 319
    "epoll_pwait",
    6,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_INT, ARG_PTR, ARG_INT
]),

     (   # 320
    "utimensat",
    4,
    [
ARG_INT, ARG_STR, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 321
    "signalfd",
    3,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 322
    "timerfd_create",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 323
    "eventfd",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 324
    "fallocate",
    4,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 325
    "timerfd_settime",
    4,
    [
ARG_INT, ARG_INT, ARG_PTR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 326
    "timerfd_gettime",
    2,
    [
ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 327
    "signalfd4",
    4,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 328
    "eventfd2",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 329
    "epoll_create1",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 330
    "dup3",
    3,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 331
    "pipe2",
    2,
    [
ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 332
    "inotify_init1",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 333
    "preadv",
    5,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN
]),

     (   # 334
    "pwritev",
    5,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN
]),

     (   # 335
    "rt_tgsigqueueinfo",
    4,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 336
    "perf_event_open",
    5,
    [
ARG_PTR, ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN
]),

     (   # 337
    "recvmmsg",
    5,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_INT, ARG_PTR, ARG_UNKNOWN
]),

     (   # 338
    "fanotify_init",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 339
    "fanotify_mark",
    6,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_STR
]),

     (   # 340
    "prlimit64",
    4,
    [
ARG_INT, ARG_INT, ARG_PTR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 341
    "name_to_handle_at",
    5,
    [
ARG_INT, ARG_STR, ARG_PTR, ARG_PTR, ARG_INT, ARG_UNKNOWN
]),

     (   # 342
    "open_by_handle_at",
    3,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 343
    "clock_adjtime",
    2,
    [
ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 344
    "syncfs",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 345
    "sendmmsg",
    4,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 346
    "setns",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 347
    "process_vm_readv",
    6,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_PTR, ARG_INT, ARG_INT
]),

     (   # 348
    "process_vm_writev",
    6,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_PTR, ARG_INT, ARG_INT
]),

     (   # 349
    "kcmp",
    5,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN
]),

     (   # 350
    "finit_module",
    3,
    [
ARG_INT, ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 351
    "sched_setattr",
    3,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 352
    "sched_getattr",
    4,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 353
    "renameat2",
    5,
    [
ARG_INT, ARG_STR, ARG_INT, ARG_STR, ARG_INT, ARG_UNKNOWN
]),

     (   # 354
    "seccomp",
    3,
    [
ARG_INT, ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 355
    "getrandom",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 356
    "memfd_create",
    2,
    [
ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 357
    "bpf",
    3,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 358
    "execveat",
    5,
    [
ARG_INT, ARG_STR, ARG_PTR, ARG_PTR, ARG_INT, ARG_UNKNOWN
]),

     (   # 359
    "socket",
    3,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 360
    "socketpair",
    4,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 361
    "bind",
    3,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 362
    "connect",
    3,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 363
    "listen",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 364
    "accept4",
    4,
    [
ARG_INT, ARG_PTR, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 365
    "getsockopt",
    5,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_STR, ARG_PTR, ARG_UNKNOWN
]),

     (   # 366
    "setsockopt",
    5,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_STR, ARG_INT, ARG_UNKNOWN
]),

     (   # 367
    "getsockname",
    3,
    [
ARG_INT, ARG_PTR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 368
    "getpeername",
    3,
    [
ARG_INT, ARG_PTR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 369
    "sendto",
    6,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_INT, ARG_PTR, ARG_INT
]),

     (   # 370
    "sendmsg",
    3,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 371
    "recvfrom",
    6,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_INT, ARG_PTR, ARG_PTR
]),

     (   # 372
    "recvmsg",
    3,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 373
    "shutdown",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 374
    "userfaultfd",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 375
    "membarrier",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 376
    "mlock2",
    3,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 377
    "copy_file_range",
    6,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_PTR, ARG_INT, ARG_INT
]),

     (   # 378
    "preadv2",
    6,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_INT, ARG_INT, ARG_INT
]),

     (   # 379
    "pwritev2",
    6,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_INT, ARG_INT, ARG_INT
]),

     (   # 380
    "pkey_mprotect",
    4,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 381
    "pkey_alloc",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 382
    "pkey_free",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 383
    "statx",
    5,
    [
ARG_INT, ARG_STR, ARG_INT, ARG_INT, ARG_PTR, ARG_UNKNOWN
]),

     (   # 384
    "arch_prctl",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 385
    "io_pgetevents",
    6,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_PTR, ARG_PTR, ARG_PTR
]),

]
