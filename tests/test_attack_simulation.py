import json
import hashlib

def sign_payload(payload):
    """
    Simplified signing simulation.
    Real system would use cryptographic keys.
    """
    data = json.dumps(payload, sort_keys=True).encode()
    return hashlib.sha256(data).hexdigest()


def verify_payload(payload, signature):
    data = json.dumps(payload, sort_keys=True).encode()
    expected = hashlib.sha256(data).hexdigest()
    return expected == signature


def test_attack_simulation():

    # original telemetry
    payload = {
        "device_id": "iot2050-demo",
        "timestamp": 1700000000,
        "energy": 12.4,
        "voltage": 230.1
    }

    signature = sign_payload(payload)

    # attacker modifies telemetry
    attacked_payload = payload.copy()
    attacked_payload["energy"] = 9999

    assert verify_payload(payload, signature) is True
    assert verify_payload(attacked_payload, signature) is False
