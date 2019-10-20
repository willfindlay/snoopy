import re
import os, sys
import datetime
import time

from bcc import BPF

from .config import Config
from .utils import *
from .syscall import syscalls_32, syscalls_64

class Snoopy:
    def __init__(self, args):
        for call in syscalls_64.values():
            print(call)
