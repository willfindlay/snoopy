import os, sys

from .config import Config

# pathnames
BASEDIR = os.path.realpath(os.path.dirname(os.path.realpath(__file__))+"/../")

print(BASEDIR)

def path(f):
    curr_dir = os.path.realpath(os.path.dirname(__file__))
    project_dir = os.path.realpath(os.path.join(curr_dir,"../../.."))
    path = os.path.realpath(os.path.join(project_dir, f))
    return path
