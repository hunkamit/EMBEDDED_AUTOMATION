import time

class MockSerial:
    def __init__(self, delay=0.5):
        self.delay = delay

    def readline(self):
        time.sleep(self.delay)
        return b"READY\n"