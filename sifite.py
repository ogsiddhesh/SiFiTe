#!/usr/bin/env python3
import os
import sys
import time
import subprocess
import shutil
import platform

R = '\033[31m' # Red
G = '\033[32m' # Green
C = '\033[36m' # Cyan
Y = '\033[33m' # Yellow
P = '\033[35m' # Purple
W = '\033[0m'  # White
BOLD = '\033[1m'

# ing Root
if os.geteuid() != 0:
    print(f"{R}[!] Must run as root.{W}")
    sys.exit(1)

interface = ""
monitor_interface = ""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def fast_type(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print("")

def header():
    clear_screen()
    print(f"{C}" + "="*50)
    print(f"{BOLD}   S I F I T E  v3.0 - THE ULTIMATE SUITE   {W}{C}")
    print("="*50 + W)

def check_monitor():
    if not monitor_interface:
        print(f"{R}[!] Monitor Mode NOT enabled. Go to Main Menu -> Option 1.{W}")
        time.sleep(2)
        return False
    return True


def enable_monitor():
    global interface, monitor_interface
    header()
    os.system("iwconfig")
    print(f"\n{Y}Enter the interface name to start (e.g., wlan0):{W}")
    iface = input(f"{C}Input > {W}")
    
    if not iface: return

    print(f"{G}[*] Killing background processes...{W}")
    os.system("airmon-ng check kill > /dev/null 2>&1")
    
    print(f"{G}[*] Starting Monitor Mode on {iface}...{W}")
    os.system(f"airmon-ng start {iface}")
    
    monitor_interface = f"{iface}mon" 
    print(f"{P}[+] Monitor Mode Enabled on: {monitor_interface}{W}")
    interface = iface
    input("Press Enter...")

def scan_attack_workflow():
    if not check_monitor(): return
    print(f"{Y}[*] Starting Airodump Scan... (CTRL+C to Stop){W}")
    time.sleep(1)
    try:
        os.system(f"airodump-ng {monitor_interface}")
    except KeyboardInterrupt:
        pass


def run_besside():
    if not check_monitor(): return
    header()
    print(f"{P}--- BESSIDE-NG (The Auto-Hunter) ---{W}")
    print("This tool will automatically hunt for networks and try to own them.")
    print(f"{Y}[!] Files will be saved in current directory (wpa.cap / wep.cap){W}")
    input("Press Enter to RELEASE THE BEAST (CTRL+C to stop)...")
    
    try:
        os.system(f"besside-ng {monitor_interface}")
    except KeyboardInterrupt:
        pass
    print(f"\n{G}[*] Hunting stopped. Check wpa.cap file.{W}")
    input("Press Enter...")

def run_evil_twin():
    if not check_monitor(): return
    header()
    print(f"{P}--- AIRBASE-NG (Evil Twin / Soft AP) ---{W}")
    ssid = input("Enter the Fake SSID Name (e.g., Free_WiFi): ")
    chan = input("Enter Channel (default 6): ") or "6"
    
    print(f"{R}[!] starting Fake AP '{ssid}' on channel {chan}...{W}")
    print("Note: In a real attack, you would need a second terminal to run DHCP.")
    input("Press Enter to start broadcast...")
    try:
        os.system(f"airbase-ng -e '{ssid}' -c {chan} {monitor_interface}")
    except KeyboardInterrupt:
        pass

def clean_cap_file():
    header()
    print(f"{P}--- WPACLEAN (The Janitor) ---{W}")
    print("Cleans capture files to make them readable for Hashcat/John.")
    
    infile = input("Enter path to dirty .cap file: ")
    outfile = input("Enter name for clean output file (e.g., clean.cap): ")
    
    if os.path.exists(infile):
        os.system(f"wpaclean {outfile} {infile}")
        print(f"{G}[+] Cleaning complete.{W}")
    else:
        print(f"{R}[!] File not found.{W}")
    input("Press Enter...")

def generate_graph():
    header()
    print(f"{P}--- AIRGRAPH-NG (The Visualizer) ---{W}")
    print("Creates a visual map of Access Points and Clients.")
    print(f"{Y}Requires a .csv or .txt file from airodump-ng.{W}")
    
    infile = input("Enter path to airodump CSV/TXT file: ")
    out_img = input("Enter output filename (e.g., map.png): ")
    
    print("Graph Types: [1] CAPR (Client to AP)  [2] CPG (Common Probe Graph)")
    gtype = input("Select Type (1/2): ")
    
    style = "-g CAPR" if gtype == "1" else "-g CPG"
    
    if os.path.exists(infile):
        cmd = f"airgraph-ng -i {infile} -o {out_img} {style}"
        print(f"{C}Executing: {cmd}{W}")
        os.system(cmd)
        print(f"{G}[+] Image created! Open {out_img} to view.{W}")
    else:
        print(f"{R}[!] File not found.{W}")
    input("Press Enter...")

def advanced_menu():
    while True:
        header()
        print(f"{Y}[ A D V A N C E D   A R S E N A L ]{W}")
        print("-" * 40)
        print(f"{G}[1]{W} BESSIDE-NG  {C}(Auto-Hunt WPA/WEP){W}")
        print(f"{G}[2]{W} AIRBASE-NG  {C}(Create Fake AP){W}")
        print(f"{G}[3]{W} WPACLEAN    {C}(Optimize Capture Files){W}")
        print(f"{G}[4]{W} AIRGRAPH-NG {C}(Generate Network Map Image){W}")
        print(f"{G}[5]{W} PACKETFORGE {C}(Craft Custom Packets){W}")
        print(f"{R}[9] BACK TO MAIN MENU{W}")
        
        sel = input(f"\n{P}sifite(advanced) > {W}")
        
        if sel == '1': run_besside()
        elif sel == '2': run_evil_twin()
        elif sel == '3': clean_cap_file()
        elif sel == '4': generate_graph()
        elif sel == '5': 
            print("Packetforge requires a captured PRGA file. (Not implemented in demo)")
            time.sleep(2)
        elif sel == '9': break


def main():
    header()
    fast_type(f"{G}[*] Loading Aircrack-ng Suite Wrapper...{W}")
    fast_type(f"{G}[*] Integrating Airgeddon Modules...{W}")
    time.sleep(0.5)
    
    while True:
        header()
        if monitor_interface:
            print(f"{P}STATUS: Monitor Mode Active ({monitor_interface}){W}")
        else:
            print(f"{Y}STATUS: Managed Mode{W}")
        print("-" * 40)
        
        print(f"{C}[1]{W} ENABLE Monitor Mode (Start Here)")
        print(f"{C}[2]{W} SCAN & ATTACK (Airodump/Aireplay)")
        print(f"{C}[3]{W} ADVANCED ARSENAL (Besside, EvilTwin, Graphs)")
        print(f"{C}[4]{W} INSTALL/LAUNCH AIRGEDDON")
        print(f"{C}[5]{W} EXIT & RESET WIFI")
        
        cmd = input(f"\n{C}sifite > {W}")
        
        if cmd == '1': enable_monitor()
        elif cmd == '2': scan_attack_workflow()
        elif cmd == '3': advanced_menu()
        elif cmd == '4': 
             if os.path.exists("airgeddon"):
                 os.chdir("airgeddon")
                 os.system("sudo bash airgeddon.sh")
             else:
                 print("Airgeddon not found. Please clone it.")
                 time.sleep(2)
        elif cmd == '5':
            print("Restoring Wifi...")
            os.system("airmon-ng stop wlan0mon > /dev/null 2>&1")
            os.system("service NetworkManager start")
            sys.exit()

if __name__ == "__main__":
    main()