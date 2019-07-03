from PySide2.QtCore import QObject, Signal

import defs

class Poller(QObject):
    sig_syscalls = Signal(list)

    def __init__(self, program):
        super(Poller, self).__init__(parent=None)
        self.program = program

    def poll(self):
        self.program.bpf.perf_buffer_poll(100)
        self.sig_syscalls.emit(self.program.strace.copy())
        self.program.strace.clear()
