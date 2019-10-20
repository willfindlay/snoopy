import re
import os, sys
import datetime
import time
import subprocess

from bcc import BPF

from .config import Config
from .utils import abs_headers, drop_privileges
from .syscall import syscalls_32, syscalls_64

class Snoopy:
    def __init__(self, args):
        pass

    @drop_privileges
    def trace(self, binary, args):
        tracee = subprocess.Popen([binary] + args, stdout=sys.stdout, stderr=sys.stderr, stdin=sys.stdin)
