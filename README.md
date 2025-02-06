![image](https://github.com/user-attachments/assets/f56aeaed-098c-46c0-8da8-c0d0892d9c6d)

# 🔥 MITM Attack Script (ARP Spoofing) 🔥  

**Autor:** Qbaa134  
**Język:** Python  
**Status:** Wersja testowa  

---

## 📌 Opis  
Ten skrypt przeprowadza **atak Man-in-the-Middle (MITM) z wykorzystaniem ARP Spoofingu**. Oszukuje ofiarę i router, fałszując pakiety ARP, przez co cały ruch ofiary przechodzi przez atakującego. Można go używać do sniffowania pakietów, zmiany treści przesyłanych danych, a nawet ataków na sesje użytkowników.  

🔴 **Używaj wyłącznie w celach edukacyjnych i testowania własnej sieci.**  
Atakowanie cudzych urządzeń jest **nielegalne** i grozi konsekwencjami prawnymi!  

---

## 🛠️ Wymagania  
**Systemy operacyjne:**  
✅ Linux (Ubuntu, Kali, Debian, Arch, itp.)  
✅ macOS *(działa, ale wymaga dodatkowej konfiguracji ARP)*  
❌ Windows *(niezalecane, ale można użyć WSL z ograniczoną funkcjonalnością)*  

**Wymagane pakiety:**  
- **Python 3.x**  
- **Scapy** (biblioteka do manipulacji pakietami)  
- **PyFiglet** (efektywny tekst ASCII dla lepszego wyglądu)  

💡 Jeśli nie masz **Pythona**, zainstaluj go:  
```bash
sudo apt update && sudo apt install python3 python3-pip -y
```
  
Zainstaluj **Scapy** i **PyFiglet**:  
```bash
pip install scapy pyfiglet
```

Sprawdź, czy `pyfiglet` działa:  
```bash
python3 -c "import pyfiglet; print(pyfiglet.figlet_format('MITM'))"
```

---

## 📥 Pobranie i uruchomienie  

1️⃣ **Sklonuj repozytorium**  
```bash
git clone https://github.com/qbaa134/mitm-attack.git
cd mitm-attack
```
  
2️⃣ **Uruchom skrypt MITM**  
```bash
sudo python3 mitm.py <IP_OFIARY> <IP_BRAMY>
```
📌 *Przykład:*  
```bash
sudo python3 mitm.py 192.168.1.100 192.168.1.1
```
- **192.168.1.100** – IP ofiary  
- **192.168.1.1** – IP bramy (routera)  

3️⃣ **Podgląd ARP po ataku**  
Sprawdź, czy ofiara ma fałszywy wpis ARP:  
```bash
arp -a
```
Jeśli adres MAC bramy został podmieniony na MAC atakującego, atak działa.  

---

## 🔄 Zatrzymanie ataku  
1. **Naciśnij** `CTRL + C`  
2. Skrypt przywróci poprawne wpisy ARP w sieci.  
3. Możesz też ręcznie wpisać:  
```bash
sudo sysctl -w net.ipv4.ip_forward=0
```

---

## 📜 Jak działa MITM ARP Spoofing?  

🔹 **ARP (Address Resolution Protocol)** służy do kojarzenia adresów IP z adresami MAC.  
🔹 W **ARP Spoofingu** atakujący wysyła fałszywe pakiety ARP do ofiary i routera, zmuszając je do myślenia, że komputer atakującego jest bramą sieciową.  

📌 **Efekt:**  
- Ofiara wysyła cały ruch do atakującego.  
- Atakujący może sniffować, modyfikować i przekazywać pakiety.  
- Może być używane do przechwytywania haseł, sesji (np. Facebook, Gmail) i danych.  

---

## 🔧 Możliwe ulepszenia w przyszlości  

🔹 **Sniffowanie ruchu:**  
Dodanie funkcji przechwytywania pakietów (`scapy.sniff()`), np. do przechwytywania haseł.  

🔹 **SSLStrip:**  
Automatyczne obniżanie zabezpieczeń HTTPS do HTTP i przechwytywanie danych logowania.  

🔹 **DNS Spoofing:**  
Przekierowywanie użytkowników na fałszywe strony (np. phishing).  

🔹 **Bettercap Integration:**  
Zamiast Scapy można użyć **Bettercap**, który jest bardziej zaawansowanym narzędziem.  

---

## ❓ Q&A – Najczęściej zadawane pytania  

**1️⃣ Skrypt się nie uruchamia!**  
✅ Sprawdź, czy masz **uprawnienia root** (`sudo`).  
✅ Upewnij się, że Python 3 jest zainstalowany (`python3 --version`).  

**2️⃣ Jak sprawdzić, czy atak działa?**  
✅ Wpisz `arp -a` na ofierze i sprawdź, czy adres MAC bramy został zmieniony.  
✅ Możesz użyć `tcpdump` lub `Wireshark` do monitorowania ruchu.  

**3️⃣ Jak usunąć skutki ataku?**  
✅ **Zrestartuj** router lub użyj:  
```bash
sudo arp -d <IP_BRAMY>
```

**4️⃣ Czy mogę atakować dowolne sieci?**  
🚨 **Nie!** Używanie tego narzędzia bez zgody właściciela sieci jest **nielegalne**.  

---

📢 **Chcesz dodać nowe funkcje?**  
🔧 Stwórz **pull request** lub otwórz **issue** na GitHubie! 🚀  

👨‍💻 **Autor:** Qbaa134   
🔥 **Pamiętaj – to tylko do testów i nauki!**
