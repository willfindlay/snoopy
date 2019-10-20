import os, sys

from .config import Config

# Project pathnames
src_dir = os.path.realpath(os.path.dirname(os.path.realpath(__file__))+"/../")
python_dir = os.path.realpath(os.path.join(src_dir, "python"))
c_dir = os.path.realpath(os.path.join(src_dir, "c"))

# Replace header includes in bpf with absolute paths
def abs_headers(txt):
    for match in re.findall(r"(#include\s*\"(.*)\")", text):
        real_header_path = os.path.abspath(os.path.realpath(os.path.join(c_dir, match[1])))
        txt = txt.replace(match[0], ''.join(['#include "', real_header_path, '"']))
    return txt

# Create the parent directories for a file if it doesn't exist
def create_parent_dirs(f):
    os.makedirs(os.path.split(f)[0], exist_ok=True)
