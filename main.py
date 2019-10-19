#! /usr/bin/env python3

import os, sys
import argparse

from src.python.snoopy import Snoopy

EPILOG = """Examples:
    sudo snoopy ls -la
    sudo snoopy google-chrome-stable
"""

if __name__ == "__main__":
    # check privileges
    if not (os.geteuid() == 0):
        print("snoopy must be run with root privileges. Exiting")
        sys.exit(-1)

    parser = argparse.ArgumentParser(description="snoopy is a modern GNU/Linux debugger that\
            leverages eBPF tracing technology for performance and security.", prog="sudo snoopy",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog=EPILOG)
    parser.add_argument('binary', help="Path to the binary you want to analyze.")
    parser.add_argument('args', nargs='*', help="Arguments to pass to the binary.")

    # parse arguments, first try
    args, unknown = parser.parse_known_args()
    # hack to allow arguments to be passed to the analyzed program
    sys.argv.insert(sys.argv.index(args.binary), "--")
    # parse args, second try
    args = parser.parse_args()

    snoopy = Snoopy(args)
