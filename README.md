# Foritech Verify Demo

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![Fuzz Tested](https://img.shields.io/badge/fuzz%20tested-AFL%2B%2B-orange)
![Security](https://img.shields.io/badge/telemetry-integrity-critical)
![License](https://img.shields.io/badge/license-research-lightgrey)
![Tests](https://github.com/foritech-secure-system/foritech-verify-demo/actions/workflows/tests.yml/badge.svg)
[![Sponsor](https://img.shields.io/badge/Sponsor-Support%20Project-orange)](#support-the-project)
[![Sponsor](https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-pink)](https://github.com/sponsors/forrybg)

Cryptographic verification for machine telemetry and industrial data pipelines.

# Foritech Verify Demo

**Cryptographic verification for machine telemetry and industrial data pipelines.**

This repository demonstrates a simplified concept of the **Foritech Secure System** verification layer.

The goal is to ensure that telemetry data received from devices or gateways has not been **spoofed, modified, or silently manipulated** before entering analytics, storage or control systems.

---

## Problem

Most industrial and IoT telemetry pipelines trust incoming data without verifying its origin.

Typical pipeline:

Device → MQTT / HTTP → Database → Dashboard

If telemetry is manipulated or injected, systems may make **incorrect decisions** based on falsified data.

Examples:

- spoofed sensor data
- modified telemetry in transit
- malicious device injection

---

## Concept

Foritech introduces a **cryptographic integrity layer** for machine data.

Pipeline with verification:

Device  
↓  
Foritech Edge (sign telemetry)  
↓  
MQTT / HTTP / transport  
↓  
Foritech Verify (validate signature)  
↓  
Storage / analytics / control systems  

This ensures only **authentic telemetry** is accepted.

---

## Repository structure

demo/ # simplified signing and verification examples
docs/ # architecture overview
tests/ # tampering detection tests


---

## Architecture overview

Typical telemetry pipeline today:

Device → MQTT/HTTP → Database → Dashboard

Trusted by default.

Foritech approach:

```bash
Device / Sensor
      │
      ▼
Foritech Edge (sign telemetry)
      │
      ▼
Transport (MQTT / HTTP / files)
      │
      ▼
Foritech Verify (validate signature)
      │
      ▼
Database / Analytics / Control systems

```

Only authenticated telemetry is accepted.

---

## Security validation

The full Foritech Secure System includes multiple validation layers:

- Unit testing
- Tamper detection tests
- Boundary condition tests
- Negative cryptographic tests
- AFL++ fuzz testing

These techniques help detect malformed containers and corrupted telemetry inputs before they reach analytics systems.

---

## Example attack scenario

Without integrity verification:

Attacker → injects modified telemetry → database accepts data → dashboard shows false values.

With Foritech verification:

Attacker → modifies telemetry → signature mismatch → verification fails → data rejected.

Result: corrupted telemetry never enters the system.

---

## Industrial use cases

Designed for environments such as:

- Industrial automation
- Energy infrastructure
- Remote machinery and robotics
- Telemetry-driven AI systems

---

## Status

Concept demonstration / verification prototype.

Part of the broader **Foritech Secure System** architecture.

Looking for pilot deployments and technical feedback.

---

## Demo usage

Example verification concept:

```bash
python demo/sign_demo.py
python demo/verify_demo.py
```
The demo shows how telemetry can be signed at the edge and verified before ingestion.

Security validation concept

The full system architecture includes security testing such as:

 unit testing

 negative crypto tests

 boundary validation

 AFL++ fuzz testing

 telemetry integrity verification

These techniques help ensure that malformed or manipulated data is rejected.

Industrial use cases

This approach is designed for environments such as:

 Industrial automation

 Energy infrastructure

 Remote machinery / robotics

 Telemetry-driven AI systems

Project context

This demo is part of the broader Foritech Secure System architecture which focuses on:

 cryptographic telemetry integrity

 industrial telemetry protection

 edge signing and server verification

 secure machine data pipelines

Status

Concept demonstration / verification prototype.

Looking for pilot deployments and technical feedback.

Author

Foritech Secure System

Industrial telemetry integrity research.




## Setup

Clone repository


git clone https://github.com/foritech-secure-system/foritech-verify-demo.git

```bash
cd foritech-verify-demo
```

Create virtual environment

```
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies

```
pip install -r requirements.txt
```

Run demo

```
python demo/sign_demo.py
python demo/verify_demo.py
```
```
pytest tests
```

---

# Support the Project

Foritech Secure System is an independent research effort focused on improving telemetry integrity and security for industrial and IoT systems.

If you find this project useful, consider supporting its development.

## Ways to Support

- ⭐ Star the repository
- 🛠 Contribute improvements
- 💬 Share feedback
- ☕ Support development

## Donate

You can support the development of this project via:

- Bitcoin
- Ethereum

## Sponsor the Project

You can support development via GitHub Sponsors.

❤️ https://github.com/sponsors/forrybg 

Example donation address:

BTC  
`bc1qske5uamdpgl2mvqvwdlpw0ujdzzycv5epdhrtk`

ETH  
`0xb9E13386b295D7a1663e63Cb919b342168e7C64B`

---

## Sponsorship

Organizations interested in collaboration, integration, or security research partnerships can contact:

security@forisec.eu


## License

This repository contains a **demonstration implementation** of the verification concept.

Core production components of the Foritech Secure System are not included in this repository.
