# 🧙 Gandalf's Network Ping Sweeper

A multithreaded Python network reconnaissance tool that sweeps a range of 
IP addresses to discover live hosts on a network — with commentary from 
Gandalf the Grey. Built as part of a cybersecurity learning journey.

---

## ⚡ Features

| Feature | Description |
|---|---|
| **Auto Network Detection** | Automatically detects your local network — no manual IP entry needed |
| **Multithreaded Scanning** | Pings up to 50 hosts simultaneously for fast results |
| **Reverse DNS Lookup** | Resolves IP addresses to hostnames where possible |
| **Cross Platform** | Works on both Windows and Linux |
| **Live Progress** | Real time progress display as the scan runs |
| **Gandalf Mode** | In-character reactions from Gandalf for every scan |

---

## 🛠️ Built With

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

---

## 🚀 Usage

```bash
python pingsweeper.py
```

The tool will automatically detect your local network and prompt for a range:

🔎 Detected local network: 192.168.1.x
Enter network base (press Enter for 192.168.1):
Start host (press Enter for 1):
End host (press Enter for 254):

### Example Output

✅ 192.168.1.1      — router.home
✅ 192.168.1.105    — Development1
✅ 192.168.1.210    — Unknown
📋 Live hosts found: 3/254

---

## ⚠️ Legal Disclaimer

This tool is intended for educational purposes and authorized network 
testing only. Only use on networks you own or have explicit permission 
to scan. Unauthorized network scanning may be illegal in your jurisdiction.

---

## 🔑 Key Concepts Learned

- **subprocess** — running system commands (ping) from within Python
- **Multithreading** — using ThreadPoolExecutor to run 50 pings simultaneously
- **Reverse DNS lookup** — converting IP addresses back to hostnames
- **Network reconnaissance** — the first step of any security assessment
- **Cross-platform development** — handling Windows vs Linux differences
- **IP address structure** — understanding network vs host portions of an IP

---

## 🔗 Related Projects

These tools are designed to work together as a reconnaissance toolkit:

| Tool | Purpose |
|---|---|
| [Ping Sweeper](https://github.com/Patharx/pingsweeper) | Find live hosts on a network |
| [Port Scanner](https://github.com/Patharx/portscanner) | Find open ports on a specific host |
| [Password Checker](https://github.com/Patharx/passwordchecker) | Analyze password strength |
| [Caesar Cipher](https://github.com/Patharx/caesarcipher) | Encrypt and decrypt messages |

---

## 👤 Author

**Ryan** — [github.com/Patharx](https://github.com/Patharx)

---

*"Like the Eagles surveying Middle-earth — no host escapes my sight."* 🧙