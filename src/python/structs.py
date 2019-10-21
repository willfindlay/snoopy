import ctypes as ct

# Keep in sync with src/c/snoopy.h

SNOOPY_ARGLEN = 256
SNOOPY_NUM_ARGS = 6

class Syscall(ct.Structure):
    _fields_ = [("num", ct.c_long),
                ("args", ct.c_ulong * SNOOPY_NUM_ARGS),
                ("str_args", (ct.c_char * SNOOPY_ARGLEN) * SNOOPY_NUM_ARGS),
                ("ret", ct.c_long)]
