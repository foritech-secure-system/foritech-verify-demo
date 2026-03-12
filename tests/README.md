## Attack simulation test

The repository includes a simple attack simulation showing how
tampered telemetry is detected.

Example scenario:

1. A device signs telemetry data.
2. An attacker modifies the payload.
3. Verification fails because the signature no longer matches.

Run test:

```bash
pytesy tests
```
