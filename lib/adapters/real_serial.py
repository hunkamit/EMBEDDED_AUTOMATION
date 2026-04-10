import serial

class RealSerial:
    def __init__(self, port="/dev/ttyUSB0", baud=115200, timeout=2):
        self.ser = serial.Serial(port, baud, timeout=timeout)

    def readline(self):
        return self.ser.readline()

    def close(self):
        self.ser.close()