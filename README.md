# SiFiTe - Advanced Wireless Auditing Framework 📡

> **The Ultimate Python Wrapper for the Aircrack-ng Suite & Airgeddon.**

![Python](https://img.shields.io/badge/Made%20with-Python-blue?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Linux%20(Kali%2FParrot)-red?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

## ⚡ What is SiFiTe?
SiFiTe is a powerful automation tool designed for penetration testers and security students. It bridges the gap between manual terminal commands and full automation. 

Unlike standard scripts, SiFiTe provides a **menu-driven interface** (TUI) to control powerful tools like **Aircrack-ng**, **MDK4**, and **Airgeddon** without needing to memorize complex flags.

## Installation
```bash
git clone https://github.com/ogsiddhesh/Sifite.git
cd Sifite
sudo python3 sifite.py
```

## 🚀 Key Features
* **Automated Workflow:** Streamlines the process of enabling Monitor Mode, Scanning, and Deauthentication.
* **Visual Dashboard:** Clean, color-coded terminal interface with live status updates.
* **"The Hunter" Mode:** Integrates `besside-ng` for autonomous handshake capturing.
* **Evil Twin Support:** Quickly launch `airbase-ng` for Rogue AP attacks.
* **Airgeddon Integration:** Launch the full Airgeddon suite directly from the SiFiTe menu.
* **Smart Parsing:** Automatically parses `.csv` scan data to let you select targets by number.

## 🛠️ Installation

### 1. Prerequisites
You need a Linux-based OS (Kali Linux or Parrot OS recommended) and a Wi-Fi Adapter that supports **Monitor Mode**.

### 2. Install Dependencies
Run this command to ensure you have all the necessary tools:
```bash
sudo apt update
sudo apt install aircrack-ng macchanger python3 git xterm graphviz besside-ng -y
sudo apt update && sudo apt install aircrack-ng macchanger xterm graphviz bettercap hostapd-mana hostapd-wpe hcxtools isc-dhcp-server asleap hostapd mdk4 hcxdumptool beef-xss lighttpd -y
