import time
from demo.verify_demo import verify_packet


def test_replay_attack():

    packet = {
        "device_id": "iot2050-demo",
        "timestamp": int(time.time()),
        "nonce": "abc123",
        "telemetry": {"power": 2.1}
    }

    assert verify_packet(packet) is True

    try:
        verify_packet(packet)
        assert False
    except Exception:
        assert True
