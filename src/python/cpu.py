
class CPU:
    def __init__(self):
        self.calls = []
        self.pos = 0

    def call(self, syscall):
        self.calls.append(syscall)
