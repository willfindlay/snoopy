#! /usr/bin/env python3

import os, sys
import argparse

from src.python.syscall import init_syscalls

EPILOG = """Examples:
    sudo snoopy ls -la
    sudo snoopy google-chrome-stable
"""

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="snoopy is a modern GNU/Linux debugger that\
            leverages eBPF tracing technology for performance and security.", prog="sudo snoopy",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog=EPILOG)
    parser.add_argument('--update-sys',
            dest='update_syscalls',
            action='store_true',
            help='Force an update of the syscalls cache. May be run without a provided binary.\
            You should execute this once after every kernel update')
    parser.add_argument('binary', nargs='?', help="Path to the binary you want to analyze.")
    parser.add_argument('args', nargs='*', help="Arguments to pass to the binary.")

    # Check privileges
    if not (os.geteuid() == 0):
        print("snoopy must be run with root privileges. Exiting")
        sys.exit(-1)

    # Parse arguments, first try
    args, unknown = parser.parse_known_args()
    try:
        # Hack to allow arguments to be passed to the analyzed program
        sys.argv.insert(sys.argv.index(args.binary), "--")
    except ValueError:
        pass # No program given
    # Parse args, second try
    args = parser.parse_args()

    # Snoopy import has to be below here
    init_syscalls(args.update_syscalls)
    from src.python.snoopy import Snoopy

    snoopy = Snoopy(args)
