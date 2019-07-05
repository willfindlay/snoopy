import os, sys

# pathnames
BASEDIR = os.path.realpath(os.path.dirname(os.path.realpath(__file__))+"/../")
BPFDIR  = os.path.realpath(os.path.join(BASEDIR, "bpf"))
BPFFILE = os.path.realpath(os.path.join(BPFDIR, "bpf.c"))

# define colors
COLORS = [
"#abb2bf", #  0 - white
"#e06c75", #  1 - light red
"#98c379", #  2 - light green
"#e5c07b", #  3 - light yellow
"#61afef", #  4 - light blue
"#c678dd", #  5 - light purple
"#58c2e6", #  6 - light teal
"#abb2bf", #  7 - light grey
"#5c6370", #  8 - grey
"#be5046", #  9 - dark red
"#7a9f60", # 10 - dark green
"#d19a66", # 11 - dark yellow
"#3b84c0", # 12 - dark blue
"#9a52af", # 13 - dark purple
"#3c909b", # 14 - dark teal
"#828997", # 15 - dark grey
"#333333"  # 16 - black
]
def color(c):
    global COLORS
    if type(c) is int:
        return "".join(["<font color=\"", COLORS[c], "\">"])
    return "".join(["<font color=\"", c, "\">"])
