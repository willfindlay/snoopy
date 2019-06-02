#! /usr/bin/env python3

def init():
    global BPF_FILE
    global COLORS

    # define pathname for bpf program
    BPF_FILE = "bpf/bpf.c"

    # define colors
    COLORS = object()
    COLORS.COLOR1  = "#000000" # light red
    COLORS.COLOR2  = "#000000" # light green
    COLORS.COLOR3  = "#000000" # light yellow
    COLORS.COLOR4  = "#000000" # light blue
    COLORS.COLOR5  = "#000000" # light purple
    COLORS.COLOR6  = "#000000" # light teal
    COLORS.COLOR7  = "#000000" # light grey
    COLORS.COLOR8  = "#000000" # grey
    COLORS.COLOR9  = "#000000" # dark red
    COLORS.COLOR10 = "#000000" # dark green
    COLORS.COLOR11 = "#000000" # dark yellow
    COLORS.COLOR12 = "#000000" # dark blue
    COLORS.COLOR13 = "#000000" # dark purple
    COLORS.COLOR14 = "#000000" # dark teal
    COLORS.COLOR15 = "#000000" # dark grey
    COLORS.COLOR16 = "#000000" # black
