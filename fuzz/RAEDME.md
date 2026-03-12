## Fuzz Testing

The telemetry parser can be fuzz-tested using AFL++.

Example:

```bash

AFL_SKIP_CPUFREQ=1 afl-fuzz -n -i fuzz/seeds -o fuzz/out -- python3 fuzz/fuzz_telemetry_parser.py

```

The demo uses AFL++ in non-instrumented mode because Python is not compiled with AFL instrumentation.

Typical fuzz run time: 10–20 minutes for demonstration.

Security validation includes:

✔ Tamper detection tests
✔ Replay attack tests
✔ AFL++ fuzz testing
✔ CI verification

```bash

Device
   ↓
Foritech Edge
   ↓
MQTT / HTTP
   ↓
Foritech Verify
   ↓
Database / Analytics

```
