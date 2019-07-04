#! /usr/bin/env python3

import os, sys

# pathnames
BASEDIR = os.path.realpath(os.path.dirname(os.path.realpath(__file__))+"/../")
BPFDIR  = os.path.realpath(os.path.join(BASEDIR, "bpf"))
BPFFILE = os.path.realpath(os.path.join(BPFDIR, "bpf.c"))

# define colors
COLORS = [
"#abb2bf", #  0 - white
"#e06c75", #  1 - light red
"#98c379", #  2 - light green
"#e5c07b", #  3 - light yellow
"#61afef", #  4 - light blue
"#c678dd", #  5 - light purple
"#58c2e6", #  6 - light teal
"#abb2bf", #  7 - light grey
"#5c6370", #  8 - grey
"#be5046", #  9 - dark red
"#7a9f60", # 10 - dark green
"#d19a66", # 11 - dark yellow
"#3b84c0", # 12 - dark blue
"#9a52af", # 13 - dark purple
"#3c909b", # 14 - dark teal
"#828997", # 15 - dark grey
"#333333"  # 16 - black
]
def color(c):
    global COLORS
    if type(c) is int:
        return "".join(["<font color=\"", COLORS[c], "\">"])
    return "".join(["<font color=\"", c, "\">"])

# syscall arg types (for display purposes)
# TODO: maybe move this into syscall.py
ARG_UNKNOWN = 0
ARG_INT = 1
ARG_STR = 2
ARG_PTR = 3
MAX_SYSCALL_NUM = 334
# list em out
SYSCALL = [
     (   # 0
    "read", # name
    3,      # max_args
    [       # list of argtypes:
ARG_INT, ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 1
    "write",
    3,
    [
ARG_INT, ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 2
    "open",
    3,
    [
ARG_STR, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 3
    "close",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 4
    "stat",
    2,
    [
ARG_STR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 5
    "fstat",
    2,
    [
ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 6
    "lstat",
    2,
    [
ARG_STR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 7
    "poll",
    3,
    [
ARG_PTR, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 8
    "lseek",
    3,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 9
    "mmap",
    6,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_INT
]),

     (   # 10
    "mprotect",
    3,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 11
    "munmap",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 12
    "brk",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 13
    "rt_sigaction",
    4,
    [
ARG_INT, ARG_PTR, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 14
    "rt_sigprocmask",
    4,
    [
ARG_INT, ARG_PTR, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 15
    "rt_sigreturn",
    0,
    [
ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 16
    "ioctl",
    3,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 17
    "pread64",
    4,
    [
ARG_INT, ARG_STR, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 18
    "pwrite64",
    4,
    [
ARG_INT, ARG_STR, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 19
    "readv",
    3,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 20
    "writev",
    3,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 21
    "access",
    2,
    [
ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 22
    "pipe",
    1,
    [
ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 23
    "select",
    5,
    [
ARG_INT, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_UNKNOWN
]),

     (   # 24
    "sched_yield",
    0,
    [
ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 25
    "mremap",
    5,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN
]),

     (   # 26
    "msync",
    3,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 27
    "mincore",
    3,
    [
ARG_INT, ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 28
    "madvise",
    3,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 29
    "shmget",
    3,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 30
    "shmat",
    3,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 31
    "shmctl",
    3,
    [
ARG_INT, ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 32
    "dup",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 33
    "dup2",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 34
    "pause",
    0,
    [
ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 35
    "nanosleep",
    2,
    [
ARG_PTR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 36
    "getitimer",
    2,
    [
ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 37
    "alarm",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 38
    "setitimer",
    3,
    [
ARG_INT, ARG_PTR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 39
    "getpid",
    0,
    [
ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 40
    "sendfile",
    4,
    [
ARG_INT, ARG_INT, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 41
    "socket",
    3,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 42
    "connect",
    3,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 43
    "accept",
    3,
    [
ARG_INT, ARG_PTR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 44
    "sendto",
    6,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_INT, ARG_PTR, ARG_INT
]),

     (   # 45
    "recvfrom",
    6,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_INT, ARG_PTR, ARG_PTR
]),

     (   # 46
    "sendmsg",
    3,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 47
    "recvmsg",
    3,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 48
    "shutdown",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 49
    "bind",
    3,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 50
    "listen",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 51
    "getsockname",
    3,
    [
ARG_INT, ARG_PTR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 52
    "getpeername",
    3,
    [
ARG_INT, ARG_PTR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 53
    "socketpair",
    4,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 54
    "setsockopt",
    5,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_STR, ARG_INT, ARG_UNKNOWN
]),

     (   # 55
    "getsockopt",
    5,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_STR, ARG_PTR, ARG_UNKNOWN
]),

     (   # 56
    "clone",
    5,
    [
ARG_INT, ARG_INT, ARG_PTR, ARG_PTR, ARG_INT, ARG_UNKNOWN
]),

     (   # 57
    "fork",
    0,
    [
ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 58
    "vfork",
    0,
    [
ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 59
    "execve",
    3,
    [
ARG_STR, ARG_PTR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 60
    "exit",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 61
    "wait4",
    4,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 62
    "kill",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 63
    "uname",
    1,
    [
ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 64
    "semget",
    3,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 65
    "semop",
    3,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 66
    "semctl",
    4,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 67
    "shmdt",
    1,
    [
ARG_STR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 68
    "msgget",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 69
    "msgsnd",
    4,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 70
    "msgrcv",
    5,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN
]),

     (   # 71
    "msgctl",
    3,
    [
ARG_INT, ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 72
    "fcntl",
    3,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 73
    "flock",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 74
    "fsync",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 75
    "fdatasync",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 76
    "truncate",
    2,
    [
ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 77
    "ftruncate",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 78
    "getdents",
    3,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 79
    "getcwd",
    2,
    [
ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 80
    "chdir",
    1,
    [
ARG_STR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 81
    "fchdir",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 82
    "rename",
    2,
    [
ARG_STR, ARG_STR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 83
    "mkdir",
    2,
    [
ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 84
    "rmdir",
    1,
    [
ARG_STR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 85
    "creat",
    2,
    [
ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 86
    "link",
    2,
    [
ARG_STR, ARG_STR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 87
    "unlink",
    1,
    [
ARG_STR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 88
    "symlink",
    2,
    [
ARG_STR, ARG_STR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 89
    "readlink",
    3,
    [
ARG_STR, ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 90
    "chmod",
    2,
    [
ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 91
    "fchmod",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 92
    "chown",
    3,
    [
ARG_STR, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 93
    "fchown",
    3,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 94
    "lchown",
    3,
    [
ARG_STR, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 95
    "umask",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 96
    "gettimeofday",
    2,
    [
ARG_PTR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 97
    "getrlimit",
    2,
    [
ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 98
    "getrusage",
    2,
    [
ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 99
    "sysinfo",
    1,
    [
ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 100
    "times",
    1,
    [
ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 101
    "ptrace",
    4,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 102
    "getuid",
    0,
    [
ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 103
    "syslog",
    3,
    [
ARG_INT, ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 104
    "getgid",
    0,
    [
ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 105
    "setuid",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 106
    "setgid",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 107
    "geteuid",
    0,
    [
ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 108
    "getegid",
    0,
    [
ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 109
    "setpgid",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 110
    "getppid",
    0,
    [
ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 111
    "getpgrp",
    0,
    [
ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 112
    "setsid",
    0,
    [
ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 113
    "setreuid",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 114
    "setregid",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 115
    "getgroups",
    2,
    [
ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 116
    "setgroups",
    2,
    [
ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 117
    "setresuid",
    3,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 118
    "getresuid",
    3,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 119
    "setresgid",
    3,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 120
    "getresgid",
    3,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 121
    "getpgid",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 122
    "setfsuid",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 123
    "setfsgid",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 124
    "getsid",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 125
    "capget",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 126
    "capset",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 127
    "rt_sigpending",
    2,
    [
ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 128
    "rt_sigtimedwait",
    4,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 129
    "rt_sigqueueinfo",
    3,
    [
ARG_INT, ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 130
    "rt_sigsuspend",
    2,
    [
ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 131
    "sigaltstack",
    2,
    [
ARG_PTR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 132
    "utime",
    2,
    [
ARG_STR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 133
    "mknod",
    3,
    [
ARG_STR, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 134
    "uselib",
    1,
    [
ARG_STR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 135
    "personality",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 136
    "ustat",
    2,
    [
ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 137
    "statfs",
    2,
    [
ARG_STR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 138
    "fstatfs",
    2,
    [
ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 139
    "sysfs",
    3,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 140
    "getpriority",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 141
    "setpriority",
    3,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 142
    "sched_setparam",
    2,
    [
ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 143
    "sched_getparam",
    2,
    [
ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 144
    "sched_setscheduler",
    3,
    [
ARG_INT, ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 145
    "sched_getscheduler",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 146
    "sched_get_priority_max",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 147
    "sched_get_priority_min",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 148
    "sched_rr_get_interval",
    2,
    [
ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 149
    "mlock",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 150
    "munlock",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 151
    "mlockall",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 152
    "munlockall",
    0,
    [
ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 153
    "vhangup",
    0,
    [
ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 154
    "modify_ldt",
    3,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 155
    "pivot_root",
    2,
    [
ARG_STR, ARG_STR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 156
    "_sysctl",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 157
    "prctl",
    5,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN
]),

     (   # 158
    "arch_prctl",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 159
    "adjtimex",
    1,
    [
ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 160
    "setrlimit",
    2,
    [
ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 161
    "chroot",
    1,
    [
ARG_STR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 162
    "sync",
    0,
    [
ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 163
    "acct",
    1,
    [
ARG_STR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 164
    "settimeofday",
    2,
    [
ARG_PTR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 165
    "mount",
    5,
    [
ARG_STR, ARG_STR, ARG_STR, ARG_INT, ARG_PTR, ARG_UNKNOWN
]),

     (   # 166
    "umount2",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 167
    "swapon",
    2,
    [
ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 168
    "swapoff",
    1,
    [
ARG_STR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 169
    "reboot",
    4,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 170
    "sethostname",
    2,
    [
ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 171
    "setdomainname",
    2,
    [
ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 172
    "iopl",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 173
    "ioperm",
    3,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 174
    "create_module",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 175
    "init_module",
    3,
    [
ARG_PTR, ARG_INT, ARG_STR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 176
    "delete_module",
    2,
    [
ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 177
    "get_kernel_syms",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 178
    "query_module",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 179
    "quotactl",
    4,
    [
ARG_INT, ARG_STR, ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 180
    "nfsservctl",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 181
    "getpmsg",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 182
    "putpmsg",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 183
    "afs_syscall",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 184
    "tuxcall",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 185
    "security",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 186
    "gettid",
    0,
    [
ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 187
    "readahead",
    3,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 188
    "setxattr",
    5,
    [
ARG_STR, ARG_STR, ARG_PTR, ARG_INT, ARG_INT, ARG_UNKNOWN
]),

     (   # 189
    "lsetxattr",
    5,
    [
ARG_STR, ARG_STR, ARG_PTR, ARG_INT, ARG_INT, ARG_UNKNOWN
]),

     (   # 190
    "fsetxattr",
    5,
    [
ARG_INT, ARG_STR, ARG_PTR, ARG_INT, ARG_INT, ARG_UNKNOWN
]),

     (   # 191
    "getxattr",
    4,
    [
ARG_STR, ARG_STR, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 192
    "lgetxattr",
    4,
    [
ARG_STR, ARG_STR, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 193
    "fgetxattr",
    4,
    [
ARG_INT, ARG_STR, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 194
    "listxattr",
    3,
    [
ARG_STR, ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 195
    "llistxattr",
    3,
    [
ARG_STR, ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 196
    "flistxattr",
    3,
    [
ARG_INT, ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 197
    "removexattr",
    2,
    [
ARG_STR, ARG_STR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 198
    "lremovexattr",
    2,
    [
ARG_STR, ARG_STR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 199
    "fremovexattr",
    2,
    [
ARG_INT, ARG_STR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 200
    "tkill",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 201
    "time",
    1,
    [
ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 202
    "futex",
    6,
    [
ARG_PTR, ARG_INT, ARG_INT, ARG_PTR, ARG_PTR, ARG_INT
]),

     (   # 203
    "sched_setaffinity",
    3,
    [
ARG_INT, ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 204
    "sched_getaffinity",
    3,
    [
ARG_INT, ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 205
    "set_thread_area",
    1,
    [
ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 206
    "io_setup",
    2,
    [
ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 207
    "io_destroy",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 208
    "io_getevents",
    5,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_PTR, ARG_PTR, ARG_UNKNOWN
]),

     (   # 209
    "io_submit",
    3,
    [
ARG_INT, ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 210
    "io_cancel",
    3,
    [
ARG_INT, ARG_PTR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 211
    "get_thread_area",
    1,
    [
ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 212
    "lookup_dcookie",
    4,
    [
ARG_INT, ARG_INT, ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 213
    "epoll_create",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 214
    "epoll_ctl_old",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 215
    "epoll_wait_old",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 216
    "remap_file_pages",
    5,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN
]),

     (   # 217
    "getdents64",
    3,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 218
    "set_tid_address",
    1,
    [
ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 219
    "restart_syscall",
    0,
    [
ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 220
    "semtimedop",
    4,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 221
    "fadvise64",
    4,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 222
    "timer_create",
    3,
    [
ARG_INT, ARG_PTR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 223
    "timer_settime",
    4,
    [
ARG_INT, ARG_INT, ARG_PTR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 224
    "timer_gettime",
    2,
    [
ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 225
    "timer_getoverrun",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 226
    "timer_delete",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 227
    "clock_settime",
    2,
    [
ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 228
    "clock_gettime",
    2,
    [
ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 229
    "clock_getres",
    2,
    [
ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 230
    "clock_nanosleep",
    4,
    [
ARG_INT, ARG_INT, ARG_PTR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 231
    "exit_group",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 232
    "epoll_wait",
    4,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 233
    "epoll_ctl",
    4,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 234
    "tgkill",
    3,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 235
    "utimes",
    2,
    [
ARG_STR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 236
    "vserver",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 237
    "mbind",
    6,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_PTR, ARG_INT, ARG_INT
]),

     (   # 238
    "set_mempolicy",
    3,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 239
    "get_mempolicy",
    5,
    [
ARG_PTR, ARG_PTR, ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN
]),

     (   # 240
    "mq_open",
    4,
    [
ARG_STR, ARG_INT, ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 241
    "mq_unlink",
    1,
    [
ARG_STR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 242
    "mq_timedsend",
    5,
    [
ARG_INT, ARG_STR, ARG_INT, ARG_INT, ARG_PTR, ARG_UNKNOWN
]),

     (   # 243
    "mq_timedreceive",
    5,
    [
ARG_INT, ARG_STR, ARG_INT, ARG_PTR, ARG_PTR, ARG_UNKNOWN
]),

     (   # 244
    "mq_notify",
    2,
    [
ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 245
    "mq_getsetattr",
    3,
    [
ARG_INT, ARG_PTR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 246
    "kexec_load",
    4,
    [
ARG_INT, ARG_INT, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 247
    "waitid",
    5,
    [
ARG_INT, ARG_INT, ARG_PTR, ARG_INT, ARG_PTR, ARG_UNKNOWN
]),

     (   # 248
    "add_key",
    5,
    [
ARG_STR, ARG_STR, ARG_PTR, ARG_INT, ARG_INT, ARG_UNKNOWN
]),

     (   # 249
    "request_key",
    4,
    [
ARG_STR, ARG_STR, ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 250
    "keyctl",
    5,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN
]),

     (   # 251
    "ioprio_set",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 252
    "ioprio_get",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 253
    "inotify_init",
    0,
    [
ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 254
    "inotify_add_watch",
    3,
    [
ARG_INT, ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 255
    "inotify_rm_watch",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 256
    "migrate_pages",
    4,
    [
ARG_INT, ARG_INT, ARG_PTR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 257
    "openat",
    4,
    [
ARG_INT, ARG_STR, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 258
    "mkdirat",
    3,
    [
ARG_INT, ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 259
    "mknodat",
    4,
    [
ARG_INT, ARG_STR, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 260
    "fchownat",
    5,
    [
ARG_INT, ARG_STR, ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN
]),

     (   # 261
    "futimesat",
    3,
    [
ARG_INT, ARG_STR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 262
    "newfstatat",
    4,
    [
ARG_INT, ARG_STR, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 263
    "unlinkat",
    3,
    [
ARG_INT, ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 264
    "renameat",
    4,
    [
ARG_INT, ARG_STR, ARG_INT, ARG_STR, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 265
    "linkat",
    5,
    [
ARG_INT, ARG_STR, ARG_INT, ARG_STR, ARG_INT, ARG_UNKNOWN
]),

     (   # 266
    "symlinkat",
    3,
    [
ARG_STR, ARG_INT, ARG_STR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 267
    "readlinkat",
    4,
    [
ARG_INT, ARG_STR, ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 268
    "fchmodat",
    3,
    [
ARG_INT, ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 269
    "faccessat",
    3,
    [
ARG_INT, ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 270
    "pselect6",
    6,
    [
ARG_INT, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 271
    "ppoll",
    5,
    [
ARG_PTR, ARG_INT, ARG_PTR, ARG_PTR, ARG_INT, ARG_UNKNOWN
]),

     (   # 272
    "unshare",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 273
    "set_robust_list",
    2,
    [
ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 274
    "get_robust_list",
    3,
    [
ARG_INT, ARG_PTR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 275
    "splice",
    6,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_PTR, ARG_INT, ARG_INT
]),

     (   # 276
    "tee",
    4,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 277
    "sync_file_range",
    4,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 278
    "vmsplice",
    4,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 279
    "move_pages",
    6,
    [
ARG_INT, ARG_INT, ARG_PTR, ARG_PTR, ARG_PTR, ARG_INT
]),

     (   # 280
    "utimensat",
    4,
    [
ARG_INT, ARG_STR, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 281
    "epoll_pwait",
    6,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_INT, ARG_PTR, ARG_INT
]),

     (   # 282
    "signalfd",
    3,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 283
    "timerfd_create",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 284
    "eventfd",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 285
    "fallocate",
    4,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 286
    "timerfd_settime",
    4,
    [
ARG_INT, ARG_INT, ARG_PTR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 287
    "timerfd_gettime",
    2,
    [
ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 288
    "accept4",
    4,
    [
ARG_INT, ARG_PTR, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 289
    "signalfd4",
    4,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 290
    "eventfd2",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 291
    "epoll_create1",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 292
    "dup3",
    3,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 293
    "pipe2",
    2,
    [
ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 294
    "inotify_init1",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 295
    "preadv",
    5,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN
]),

     (   # 296
    "pwritev",
    5,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN
]),

     (   # 297
    "rt_tgsigqueueinfo",
    4,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 298
    "perf_event_open",
    5,
    [
ARG_PTR, ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN
]),

     (   # 299
    "recvmmsg",
    5,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_INT, ARG_PTR, ARG_UNKNOWN
]),

     (   # 300
    "fanotify_init",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 301
    "fanotify_mark",
    6,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_STR
]),

     (   # 302
    "prlimit64",
    4,
    [
ARG_INT, ARG_INT, ARG_PTR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 303
    "name_to_handle_at",
    5,
    [
ARG_INT, ARG_STR, ARG_PTR, ARG_PTR, ARG_INT, ARG_UNKNOWN
]),

     (   # 304
    "open_by_handle_at",
    3,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 305
    "clock_adjtime",
    2,
    [
ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 306
    "syncfs",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 307
    "sendmmsg",
    4,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 308
    "setns",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 309
    "getcpu",
    3,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 310
    "process_vm_readv",
    6,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_PTR, ARG_INT, ARG_INT
]),

     (   # 311
    "process_vm_writev",
    6,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_PTR, ARG_INT, ARG_INT
]),

     (   # 312
    "kcmp",
    5,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN
]),

     (   # 313
    "finit_module",
    3,
    [
ARG_INT, ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 314
    "sched_setattr",
    3,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 315
    "sched_getattr",
    4,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 316
    "renameat2",
    5,
    [
ARG_INT, ARG_STR, ARG_INT, ARG_STR, ARG_INT, ARG_UNKNOWN
]),

     (   # 317
    "seccomp",
    3,
    [
ARG_INT, ARG_INT, ARG_PTR, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 318
    "getrandom",
    6,
    [
ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR, ARG_PTR
]),

     (   # 319
    "memfd_create",
    2,
    [
ARG_STR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 320
    "kexec_file_load",
    5,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_STR, ARG_INT, ARG_UNKNOWN
]),

     (   # 321
    "bpf",
    3,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 322
    "execveat",
    5,
    [
ARG_INT, ARG_STR, ARG_PTR, ARG_PTR, ARG_INT, ARG_UNKNOWN
]),

     (   # 323
    "userfaultfd",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 324
    "membarrier",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 325
    "mlock2",
    3,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 326
    "copy_file_range",
    6,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_PTR, ARG_INT, ARG_INT
]),

     (   # 327
    "preadv2",
    6,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_INT, ARG_INT, ARG_INT
]),

     (   # 328
    "pwritev2",
    6,
    [
ARG_INT, ARG_PTR, ARG_INT, ARG_INT, ARG_INT, ARG_INT
]),

     (   # 329
    "pkey_mprotect",
    4,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 330
    "pkey_alloc",
    2,
    [
ARG_INT, ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 331
    "pkey_free",
    1,
    [
ARG_INT, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN, ARG_UNKNOWN
]),

     (   # 332
    "statx",
    5,
    [
ARG_INT, ARG_STR, ARG_INT, ARG_INT, ARG_PTR, ARG_UNKNOWN
]),

     (   # 333
    "io_pgetevents",
    6,
    [
ARG_INT, ARG_INT, ARG_INT, ARG_PTR, ARG_PTR, ARG_PTR
]),

]
