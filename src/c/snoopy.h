#ifndef SNOOPY_H
#define SNOOPY_H

#include "defs.h"

struct syscall
{
    long num;
    unsigned long args[6];
    long ret;
};

#endif /* SNOOPY_H */
