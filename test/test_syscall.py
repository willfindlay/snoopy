#! /usr/bin/env python3
import unittest

import src.snoopy
import src.snoopy.config
from src.snoopy.syscall import SyscallFormat

class TestSyscallFormat(unittest.TestCase):
    def test_basic_format(self):
        pass

    def test_flags_function(self):
        sf = SyscallFormat()
        s = sf.flags(("flag_1","flag_2","flag_3"), 0b110)
        self.assertEqual(s, "flag_2|flag_3")

        s = sf.flags(("flag_1","flag_2"), 0b110)
        self.assertEqual(s, "flag_2")

        s = sf.flags(("flag_1","flag_2"), 0b1)
        self.assertEqual(s, "flag_1")

        s = sf.flags(("flag_1","flag_2"), 0b10)
        self.assertEqual(s, "flag_2")

    def test_format_with_flags(self):
        pass

if __name__ == "__main__":
    unittest.main()
