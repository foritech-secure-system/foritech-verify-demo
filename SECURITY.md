# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in the Foritech Secure System or related demo repositories, please report it responsibly.

Do NOT open a public issue for security vulnerabilities.

Instead, contact the maintainers directly.

Email:
security@forisec.eu

We will acknowledge the report within a reasonable time and work on a fix.

---

## Supported Versions

This repository is a research / demonstration implementation.

Security fixes may be applied to the latest version only.

---

## Scope

This repository demonstrates security concepts related to:

- telemetry integrity verification
- tamper detection
- replay attack protection
- fuzz testing of telemetry parsers

Production implementations may include additional protections such as:

- cryptographic signatures
- device identity verification
- secure key management
- hardened telemetry ingestion pipelines

---

## Responsible Disclosure

Please allow reasonable time for a fix before publicly disclosing vulnerabilities.

We appreciate responsible security research and collaboration.

---

## Security Testing

This repository includes several security validation mechanisms:

- automated tests (CI)
- tamper detection tests
- replay attack simulation
- AFL++ fuzz testing
- threat modeling (STRIDE)

These mechanisms help identify potential weaknesses in telemetry validation pipelines.
