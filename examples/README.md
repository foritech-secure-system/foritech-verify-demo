## Example telemetry container

Example signed telemetry message:

```bash
{
  "device_id": "iot2050-demo",
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
