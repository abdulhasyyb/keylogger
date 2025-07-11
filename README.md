# 🔐 Python Keylogger Simulation

## Description
A Python-based keylogger designed to simulate real-world malware behavior in an ethical hacking lab. It captures user keystrokes in the background and sends them to a remote server via HTTP POST requests.

This lab was structured to mimic a real-world attack chain, executed in a **controlled environment** for learning purposes.

## Attack Simulation Workflow
This project was part of a red-team-style lab simulation involving:

1. **Brute-force attack** on an SSH login using **Hydra** to gain initial access
2. Delivery of the keylogger script to the victim machine via **SSH**
3. **Execution of the payload** remotely to begin keystroke logging
4. **Credential harvesting** via POST exfiltration to an attacker-controlled server

> 🧪 This was conducted in a **safe lab environment**, with both attacker and victim machines under the user's control.

## Features
- Background keystroke capture
- Remote exfiltration via HTTP POST
- Lightweight Python script
- Easily customizable for encryption or local logging

## Tools & Concepts
- Python
- `pynput` for keyboard listener
- `requests` for HTTP exfiltration
- SSH delivery
- Hydra brute-forcing (credential attack simulation)
- MITRE ATT&CK: Initial Access → Execution → Credential Access → Exfiltration

## Installation
```bash
pip install pynput requests
