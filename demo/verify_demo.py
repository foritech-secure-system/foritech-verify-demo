import time

SEEN_NONCES = set()

MAX_DELAY = 30   # seconds


def verify_packet(packet):

    now = int(time.time())

    ts = packet["timestamp"]
    nonce = packet["nonce"]

    # replay protection (timestamp window)
    if abs(now - ts) > MAX_DELAY:
        raise Exception("packet too old")

    # replay protection (nonce reuse)
    if nonce in SEEN_NONCES:
        raise Exception("replay detected")

    SEEN_NONCES.add(nonce)

    return True
