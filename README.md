# ShadowKey

⚠️ **Educational Purpose Only: This project demonstrates cybersecurity concepts and should not be used without explicit permission.**

## Overview

ShadowKey is a proof-of-concept tool demonstrating cybersecurity principles and encryption techniques. It showcases secure data handling, encryption methods, and system monitoring in a controlled environment.

## Quick Setup

1. **Requirements**
   - Python 3.x
   - Required packages: `pynput`, `cryptography`, `pillow`, `sounddevice`, `scipy`, `requests`
   - For Windows users: `pywin32`

2. **Installation**
```bash
git clone https://github.com/NikhilPrabhat00/shadowkey.git
cd shadowkey
pip install -r requirements.txt
```

3. **Configuration**
   - Configure email settings in `ShadowKey.py`
   - Generate encryption key
   - Adjust timing parameters if needed

4. **Usage**
```bash
python ShadowKey.py        # Start monitoring
python Cryptography/DecryptFile.py  # Decrypt collected data
```

## Core Features & Security

- Military-grade encryption (Fernet symmetric encryption)
- Secure data collection and handling
- Automated data cleanup
- Email reporting system
- Separate encryption/decryption components

## Educational Value

Perfect for learning:
- Python programming
- Cryptography basics
- System monitoring
- Network communication

## License & Contributing

This project is for educational purposes only. Contributions focused on educational value and security improvements are welcome via issues or pull requests.

---
⚡ Created by [Shubham Kumar](https://github.com/NikhilPrabhat00)
