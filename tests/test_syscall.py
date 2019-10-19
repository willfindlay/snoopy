#! /usr/bin/env python3
import unittest

import src.python.config
from src.python.syscall import *

class TestSyscallFormat(unittest.TestCase):
    def test_custom_syscall(self):
        FORMAT[500] = SyscallFormat((ARG_INT, ARG_STR, ARG_PTR, ARG_INT, ARG_INT, (None,"flag_1","flag_2","flag_3","flag_4")), ARG_INT)
        s = Syscall(500,0,[1,2,0x123,4,5,0b1011], [b'',b'Hello Nurse',b'',b'',b'',b''], False)
        self.assertEqual(str(s),"[unknown: 500](1, \"Hello Nurse\", 0x123, 4, 5, flag_1|flag_2|flag_4) = ?")

    def test_flags_function(self):
        sf = SyscallFormat()
        s = sf.flags((None,"flag_1","flag_2","flag_3"), 0b110)
        self.assertEqual(s, "flag_2|flag_3")

        s = sf.flags((None,"flag_1","flag_2"), 0b110)
        self.assertEqual(s, "flag_2")

        s = sf.flags((None,"flag_1","flag_2"), 0b1)
        self.assertEqual(s, "flag_1")

        s = sf.flags((None,"flag_1","flag_2"), 0b10)
        self.assertEqual(s, "flag_2")

        s = sf.flags((None,"flag_1","flag_2"), 2)
        self.assertEqual(s, "flag_2")

        s = sf.flags((None,"flag_1","flag_2"), 1)
        self.assertEqual(s, "flag_1")

        s = sf.flags((None,"flag_1","flag_2"), 0)
        self.assertEqual(s, "")

        s = sf.flags((None,"flag_1","flag_2","flag_3"), 3)
        self.assertEqual(s, "flag_1|flag_2")

        s = sf.flags((None,"a","b","c","d","e","f","g"), 0b1001100)
        self.assertEqual(s, "c|d|g")

    def test_openat(self):
        pass

if __name__ == "__main__":
    unittest.main()
