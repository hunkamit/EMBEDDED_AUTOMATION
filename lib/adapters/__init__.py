import json
from pathlib import Path
from .mock_serial import MockSerial
from .real_serial import RealSerial

def get_serial_adapter():
    config_path = Path(__file__).parent.parent.parent / "configs" / "test_config.json"
    with open(config_path) as f:
        cfg = json.load(f)

    mode = cfg.get("mode", "mock")
    if mode == "mock":
        return MockSerial(delay=0.5)
    elif mode == "real":
        port = cfg.get("serial_port", "/dev/ttyUSB0")
        baud = cfg.get("baud_rate", 115200)
        timeout = cfg.get("timeout", 2)
        return RealSerial(port=port, baud=baud, timeout=timeout)
    else:
        raise ValueError(f"Unknown mode: {mode}")