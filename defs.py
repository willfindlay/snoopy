#! /usr/bin/env python3

from enum import Enum

# events from hashmaps and perf buffers
class Events(Enum):
    SYSENTRY = 1

def color(n):
    global COLORS
    return "".join(["<font color=\"", COLORS[n], "\">"])

def init():
    global BPF_FILE
    global COLORS
    global SYSCALL

    # define pathname for bpf program
    BPF_FILE = "bpf/bpf.c"

    #  define colors
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

    # map syscall id to name
    SYSCALL = {
    0: "READ",
    1: "WRITE",
    2: "OPEN",
    3: "CLOSE",
    4: "STAT",
    5: "FSTAT",
    6: "LSTAT",
    7: "POLL",
    8: "LSEEK",
    9: "MMAP",
    10: "MPROTECT",
    11: "MUNMAP",
    12: "BRK",
    13: "RT_SIGACTION",
    14: "RT_SIGPROCMASK",
    15: "RT_SIGRETURN",
    16: "IOCTL",
    17: "PREAD64",
    18: "PWRITE64",
    19: "READV",
    20: "WRITEV",
    21: "ACCESS",
    22: "PIPE",
    23: "SELECT",
    24: "SCHED_YIELD",
    25: "MREMAP",
    26: "MSYNC",
    27: "MINCORE",
    28: "MADVISE",
    29: "SHMGET",
    30: "SHMAT",
    31: "SHMCTL",
    32: "DUP",
    33: "DUP2",
    34: "PAUSE",
    35: "NANOSLEEP",
    36: "GETITIMER",
    37: "ALARM",
    38: "SETITIMER",
    39: "GETPID",
    40: "SENDFILE",
    41: "SOCKET",
    42: "CONNECT",
    43: "ACCEPT",
    44: "SENDTO",
    45: "RECVFROM",
    46: "SENDMSG",
    47: "RECVMSG",
    48: "SHUTDOWN",
    49: "BIND",
    50: "LISTEN",
    51: "GETSOCKNAME",
    52: "GETPEERNAME",
    53: "SOCKETPAIR",
    54: "SETSOCKOPT",
    55: "GETSOCKOPT",
    56: "CLONE",
    57: "FORK",
    58: "VFORK",
    59: "EXECVE",
    60: "EXIT",
    61: "WAIT4",
    62: "KILL",
    63: "UNAME",
    64: "SEMGET",
    65: "SEMOP",
    66: "SEMCTL",
    67: "SHMDT",
    68: "MSGGET",
    69: "MSGSND",
    70: "MSGRCV",
    71: "MSGCTL",
    72: "FCNTL",
    73: "FLOCK",
    74: "FSYNC",
    75: "FDATASYNC",
    76: "TRUNCATE",
    77: "FTRUNCATE",
    78: "GETDENTS",
    79: "GETCWD",
    80: "CHDIR",
    81: "FCHDIR",
    82: "RENAME",
    83: "MKDIR",
    84: "RMDIR",
    85: "CREAT",
    86: "LINK",
    87: "UNLINK",
    88: "SYMLINK",
    89: "READLINK",
    90: "CHMOD",
    91: "FCHMOD",
    92: "CHOWN",
    93: "FCHOWN",
    94: "LCHOWN",
    95: "UMASK",
    96: "GETTIMEOFDAY",
    97: "GETRLIMIT",
    98: "GETRUSAGE",
    99: "SYSINFO",
    100: "TIMES",
    101: "PTRACE",
    102: "GETUID",
    103: "SYSLOG",
    104: "GETGID",
    105: "SETUID",
    106: "SETGID",
    107: "GETEUID",
    108: "GETEGID",
    109: "SETPGID",
    110: "GETPPID",
    111: "GETPGRP",
    112: "SETSID",
    113: "SETREUID",
    114: "SETREGID",
    115: "GETGROUPS",
    116: "SETGROUPS",
    117: "SETRESUID",
    118: "GETRESUID",
    119: "SETRESGID",
    120: "GETRESGID",
    121: "GETPGID",
    122: "SETFSUID",
    123: "SETFSGID",
    124: "GETSID",
    125: "CAPGET",
    126: "CAPSET",
    127: "RT_SIGPENDING",
    128: "RT_SIGTIMEDWAIT",
    129: "RT_SIGQUEUEINFO",
    130: "RT_SIGSUSPEND",
    131: "SIGALTSTACK",
    132: "UTIME",
    133: "MKNOD",
    134: "USELIB",
    135: "PERSONALITY",
    136: "USTAT",
    137: "STATFS",
    138: "FSTATFS",
    139: "SYSFS",
    140: "GETPRIORITY",
    141: "SETPRIORITY",
    142: "SCHED_SETPARAM",
    143: "SCHED_GETPARAM",
    144: "SCHED_SETSCHEDULER",
    145: "SCHED_GETSCHEDULER",
    146: "SCHED_GET_PRIORITY_MAX",
    147: "SCHED_GET_PRIORITY_MIN",
    148: "SCHED_RR_GET_INTERVAL",
    149: "MLOCK",
    150: "MUNLOCK",
    151: "MLOCKALL",
    152: "MUNLOCKALL",
    153: "VHANGUP",
    154: "MODIFY_LDT",
    155: "PIVOT_ROOT",
    156: "_SYSCTL",
    157: "PRCTL",
    158: "ARCH_PRCTL",
    159: "ADJTIMEX",
    160: "SETRLIMIT",
    161: "CHROOT",
    162: "SYNC",
    163: "ACCT",
    164: "SETTIMEOFDAY",
    165: "MOUNT",
    166: "UMOUNT2",
    167: "SWAPON",
    168: "SWAPOFF",
    169: "REBOOT",
    170: "SETHOSTNAME",
    171: "SETDOMAINNAME",
    172: "IOPL",
    173: "IOPERM",
    174: "CREATE_MODULE",
    175: "INIT_MODULE",
    176: "DELETE_MODULE",
    177: "GET_KERNEL_SYMS",
    178: "QUERY_MODULE",
    179: "QUOTACTL",
    180: "NFSSERVCTL",
    181: "GETPMSG",
    182: "PUTPMSG",
    183: "AFS_SYSCALL",
    184: "TUXCALL",
    185: "SECURITY",
    186: "GETTID",
    187: "READAHEAD",
    188: "SETXATTR",
    189: "LSETXATTR",
    190: "FSETXATTR",
    191: "GETXATTR",
    192: "LGETXATTR",
    193: "FGETXATTR",
    194: "LISTXATTR",
    195: "LLISTXATTR",
    196: "FLISTXATTR",
    197: "REMOVEXATTR",
    198: "LREMOVEXATTR",
    199: "FREMOVEXATTR",
    200: "TKILL",
    201: "TIME",
    202: "FUTEX",
    203: "SCHED_SETAFFINITY",
    204: "SCHED_GETAFFINITY",
    205: "SET_THREAD_AREA",
    206: "IO_SETUP",
    207: "IO_DESTROY",
    208: "IO_GETEVENTS",
    209: "IO_SUBMIT",
    210: "IO_CANCEL",
    211: "GET_THREAD_AREA",
    212: "LOOKUP_DCOOKIE",
    213: "EPOLL_CREATE",
    214: "EPOLL_CTL_OLD",
    215: "EPOLL_WAIT_OLD",
    216: "REMAP_FILE_PAGES",
    217: "GETDENTS64",
    218: "SET_TID_ADDRESS",
    219: "RESTART_SYSCALL",
    220: "SEMTIMEDOP",
    221: "FADVISE64",
    222: "TIMER_CREATE",
    223: "TIMER_SETTIME",
    224: "TIMER_GETTIME",
    225: "TIMER_GETOVERRUN",
    226: "TIMER_DELETE",
    227: "CLOCK_SETTIME",
    228: "CLOCK_GETTIME",
    229: "CLOCK_GETRES",
    230: "CLOCK_NANOSLEEP",
    231: "EXIT_GROUP",
    232: "EPOLL_WAIT",
    233: "EPOLL_CTL",
    234: "TGKILL",
    235: "UTIMES",
    236: "VSERVER",
    237: "MBIND",
    238: "SET_MEMPOLICY",
    239: "GET_MEMPOLICY",
    240: "MQ_OPEN",
    241: "MQ_UNLINK",
    242: "MQ_TIMEDSEND",
    243: "MQ_TIMEDRECEIVE",
    244: "MQ_NOTIFY",
    245: "MQ_GETSETATTR",
    246: "KEXEC_LOAD",
    247: "WAITID",
    248: "ADD_KEY",
    249: "REQUEST_KEY",
    250: "KEYCTL",
    251: "IOPRIO_SET",
    252: "IOPRIO_GET",
    253: "INOTIFY_INIT",
    254: "INOTIFY_ADD_WATCH",
    255: "INOTIFY_RM_WATCH",
    256: "MIGRATE_PAGES",
    257: "OPENAT",
    258: "MKDIRAT",
    259: "MKNODAT",
    260: "FCHOWNAT",
    261: "FUTIMESAT",
    262: "NEWFSTATAT",
    263: "UNLINKAT",
    264: "RENAMEAT",
    265: "LINKAT",
    266: "SYMLINKAT",
    267: "READLINKAT",
    268: "FCHMODAT",
    269: "FACCESSAT",
    270: "PSELECT6",
    271: "PPOLL",
    272: "UNSHARE",
    273: "SET_ROBUST_LIST",
    274: "GET_ROBUST_LIST",
    275: "SPLICE",
    276: "TEE",
    277: "SYNC_FILE_RANGE",
    278: "VMSPLICE",
    279: "MOVE_PAGES",
    280: "UTIMENSAT",
    281: "EPOLL_PWAIT",
    282: "SIGNALFD",
    283: "TIMERFD_CREATE",
    284: "EVENTFD",
    285: "FALLOCATE",
    286: "TIMERFD_SETTIME",
    287: "TIMERFD_GETTIME",
    288: "ACCEPT4",
    289: "SIGNALFD4",
    290: "EVENTFD2",
    291: "EPOLL_CREATE1",
    292: "DUP3",
    293: "PIPE2",
    294: "INOTIFY_INIT1",
    295: "PREADV",
    296: "PWRITEV",
    297: "RT_TGSIGQUEUEINFO",
    298: "PERF_EVENT_OPEN",
    299: "RECVMMSG",
    300: "FANOTIFY_INIT",
    301: "FANOTIFY_MARK",
    302: "PRLIMIT64",
    303: "NAME_TO_HANDLE_AT",
    304: "OPEN_BY_HANDLE_AT",
    305: "CLOCK_ADJTIME",
    306: "SYNCFS",
    307: "SENDMMSG",
    308: "SETNS",
    309: "GETCPU",
    310: "PROCESS_VM_READV",
    311: "PROCESS_VM_WRITEV",
    312: "KCMP",
    313: "FINIT_MODULE",
    317: "SYS_SECCOMP",
    318: "SYS_GETRANDOM",
    319: "SYS_MEMFD_CREATE",
    320: "SYS_KEXEC_FILE_LOAD",
    321: "SYS_BPF",
    322: "STUB_EXECVEAT",
    323: "USERFAULTFD",
    324: "MEMBARRIER",
    325: "MLOCK2",
    326: "COPY_FILE_RANGE",
    327: "PREADV2",
    328: "PWRITEV2"
    }
