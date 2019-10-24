#ifndef SNOOPY_H
#define SNOOPY_H

#include "defs.h"

struct syscall
{
    long num;
    unsigned long args[SNOOPY_NUM_ARGS];
    unsigned char str_args[SNOOPY_NUM_ARGS][SNOOPY_ARGLEN];
};

struct syscall_ret
{
    long ret;
};

#endif /* SNOOPY_H */
