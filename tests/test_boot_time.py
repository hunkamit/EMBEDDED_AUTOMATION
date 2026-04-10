import time
#import pytest
from lib.adapters import get_serial_adapter

BOOT_TIMEOUT = 2.0  # seconds

def test_boot_time():
    ser = get_serial_adapter()
    start = time.time()
    line = ser.readline().decode().strip()
    elapsed = time.time() - start
    assert line == "READY", "System did not signal READY"
    assert elapsed < BOOT_TIMEOUT, f"Boot time exceeded: {elapsed:.2f}s"