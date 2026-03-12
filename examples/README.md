## Example telemetry container

Example signed telemetry message:

```bash
{
  "device_id": "6acd1ccb24c44a5ea287620e80a5c237",
  "timestamp": 1700000000,
  "telemetry": {
    "energy": 12.4,
    "voltage": 230.1,
    "power": 2.1,
    "frequency": 50.0
  }
}
```
Full example available in `examples/telemetry_example.json`.


## Example telemetry messages

Example telemetry containers are available in the `examples` directory.

- `telemetry_valid.json` — normal device telemetry
- `telemetry_tampered.json` — modified payload example
- `telemetry_replay.json` — replay attack example

These examples illustrate typical telemetry integrity risks in industrial and IoT environments.

Demo uses SHA256 for simplicity.
Production system uses cryptographic signatures.
