import hashlib
import json
import copy


def sign_payload(payload):
    data = json.dumps(payload, sort_keys=True).encode()
    return hashlib.sha256(data).hexdigest()


def verify_payload(payload, signature):
    data = json.dumps(payload, sort_keys=True).encode()
    expected = hashlib.sha256(data).hexdigest()
    return expected == signature


def test_tampered_packet():

    payload = {
        "device_id": "6acd1ccb24c44a5ea287620e80a5c237",
        "timestamp": 1700000000,
        "telemetry": {
            "energy": 12.4,
            "voltage": 230.1
        }
    }

    signature = sign_payload(payload)

    tampered = copy.deepcopy(payload)
    tampered["telemetry"]["energy"] = 9999

    assert verify_payload(payload, signature) is True
    assert verify_payload(tampered, signature) is False
