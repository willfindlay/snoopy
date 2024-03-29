class Config:
    shell = "/bin/zsh"

    tick_delay = 0.1
    perf_poll_timeout = 50

    linux_dir = "/usr/src/linux"
    unistd_32 = "/usr/include/asm/unistd_32.h"
    unistd_64 = "/usr/include/asm/unistd_64.h"

    syscalls_64_cache = "/var/cache/snoopy/syscalls_64"
    syscalls_32_cache = "/var/cache/snoopy/syscalls_32"

    log_file = "/var/log/snoopy/snoopy.log"
