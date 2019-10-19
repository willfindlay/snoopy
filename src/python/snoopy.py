import re
import os, sys
import datetime
import time

from bcc import BPF

from .config import Config
from .utils import *

class Snoopy:
    def __init__(self, args):
        print(syscall_name(0))
