import os, sys
import logging
import re
import subprocess

from .config import Config

log = logging.getLogger()

# Project pathnames
src_dir = os.path.realpath(os.path.dirname(os.path.realpath(__file__))+"/../")
python_dir = os.path.realpath(os.path.join(src_dir, "python"))
c_dir = os.path.realpath(os.path.join(src_dir, "c"))

# Replace header includes in bpf with absolute paths
def abs_headers(txt):
    for match in re.findall(r"(#include\s*\"(.*)\")", txt):
        real_header_path = os.path.abspath(os.path.realpath(os.path.join(c_dir, match[1])))
        txt = txt.replace(match[0], ''.join(['#include "', real_header_path, '"']))
    return txt

# Create the parent directories for a file if it doesn't exist
def create_parent_dirs(f):
    os.makedirs(os.path.split(f)[0], exist_ok=True)

# Decorator to drop root
def drop_privileges(function):
    def inner(*args, **kwargs):
        # Get proper UID
        try:
            sudo_uid = int(os.environ['SUDO_UID'])
        except (KeyError, ValueError) as e:
            log.error("Could not get UID for sudoer")
            return
        # Get proper GID
        try:
            sudo_gid = int(os.environ['SUDO_GID'])
        except (KeyError, ValueError) as e:
            log.error("Could not get GID for sudoer")
            return
        # Drop root
        os.setresgid(sudo_gid, sudo_gid, -1)
        os.setresuid(sudo_uid, sudo_uid, -1)
        # Execute function
        ret = function(*args, **kwargs)
        # Get root back
        os.setresgid(0, 0, -1)
        os.setresuid(0, 0, -1)
        return ret
    return inner

# Locate a binary on the system, use relative paths as a fallback
def which(binary):
    try:
        w = subprocess.Popen(["which", binary],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
        res = w.stdout.readlines()
        if len(res) == 0:
            raise Exception(f"{binary} not found")
        return os.path.realpath(res[0].strip())
    except:
        if os.path.isfile(binary):
            return os.path.realpath(binary)
        else:
            log.error(f"{binary} not found")
