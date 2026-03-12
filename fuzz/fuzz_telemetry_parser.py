import sys
import json
import hashlib


def verify_payload(payload, signature):
    data = json.dumps(payload, sort_keys=True).encode()
    expected = hashlib.sha256(data).hexdigest()
    return expected == signature


def fuzz_input(data):

    try:
        payload = json.loads(data)

        if not isinstance(payload, dict):
            return

        telemetry = payload.get("telemetry")

        if telemetry:
            json.dumps(telemetry)

    except Exception:
        pass


if __name__ == "__main__":
    data = sys.stdin.read()
    fuzz_input(data)
