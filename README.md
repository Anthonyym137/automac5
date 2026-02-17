# automac 🛠️

This tool is an automation tool developed to change the MAC addresses of network interfaces on Linux systems in accordance with IEEE standards, manage the network card, and monitor the connection status in real time.

![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat&logo=linux&logoColor=black)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## ✨ Features

* **IEEE Standard-Compliant Production:** Randomly generated MAC addresses are filtered according to Unicast and Local standards to prevent network collisions and IP acquisition errors.

* **Secure Exit Mechanism:** When the user stops the program with Ctrl+C, a code block automatically returns the network card to managed mode.

* **DHCP Cleanup:** Ensures fast IP acquisition by clearing old IP lease records with **dhclient -r** before MAC change.

## 📂 Project Structure

```text
automac5/
├── automac.py            # Main Script (Python)
├── requirements.txt      # External dependencies (psutil)
├── README.md             # This file
├── LICENSE               # MIT License file
```
## ⚙️ Installation
**Requirements**
* Linux (Kali, Ubuntu, Debian etc.)
* Python 3.8+
* NetworkManager

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Anthonyym137/automac5.git && cd automac5
   ```


2. **Install dependencies:** 
   ```bash
   pip install -r requirements.txt
   ``` 

## 🚀 Quick Start
   ```bash
   python3 automac.py
   ```

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE.txt) file for details.