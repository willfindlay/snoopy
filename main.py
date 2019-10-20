#! /usr/bin/env python3

import os, sys
import argparse
import logging, logging.handlers

from src.python.syscall import init_syscalls
from src.python.config import Config
from src.python.utils import create_parent_dirs

EPILOG = """Examples:
    sudo snoopy --update-syscall-cache
    sudo snoopy ls -la
    sudo snoopy google-chrome-stable
"""

DESCRIPTION = """snoopy is a modern GNU/Linux debugger that leverages
eBPF tracing technology for performance and security.
"""

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=DESCRIPTION, prog="sudo snoopy",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog=EPILOG)
    parser.add_argument('--update-syscall-cache',
            dest='update_syscalls',
            action='store_true',
            help='Force an update of the syscalls cache. May be run without a provided binary.\
            You should execute this once after every kernel update')
    verbosity_group = parser.add_mutually_exclusive_group()
    verbosity_group.add_argument('--silent',
            dest='silent',
            action='store_true',
            help='Prevent all logging to stderr. Cannot be combined with -v or -vv')
    verbosity_group.add_argument('-v',
            dest='verbose',
            action='store_true',
            help='Log to stderr in verbose mode. Cannot be combined with -vv or --silent')
    verbosity_group.add_argument('-vv',
            dest='very_verbose',
            action='store_true',
            help='Log to stderr in very verbose mode. Cannot be combined with -v or --silent')
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

    # Argument error checking
    if not args.update_syscalls and not args.binary:
        parser.error("You must supply a binary to trace")

    # Setup logger
    log = logging.getLogger()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
    formatter.datefmt = '%Y-%m-%d %H:%M:%S'
    log.setLevel(logging.DEBUG)

    if Config.log_file:
        create_parent_dirs(Config.log_file)
        file_handler = logging.handlers.WatchedFileHandler(Config.log_file)
        file_handler.setLevel(logging.WARNING)
        file_handler.setFormatter(formatter)
        log.addHandler(file_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG if args.very_verbose else logging.INFO if args.verbose
            else logging.CRITICAL if args.silent else logging.WARNING)
    stream_formatter = logging.Formatter('%(levelname)s: %(message)s')
    stream_handler.setFormatter(stream_formatter)
    log.addHandler(stream_handler)

    # Snoopy import has to be below here
    init_syscalls(args.update_syscalls)

    # If we are not tracing (i.e. we just wanted to update syscall cache)
    if not args.binary:
        log.info("Exiting without tracing any binaries")
        sys.exit()

    from src.python.snoopy import Snoopy

    snoopy = Snoopy(args)
