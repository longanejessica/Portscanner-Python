# 🔍 Port Scanner Project – Python

📘 [Français](#-scanner-de-ports-en-python) | 📙 [English](#-port-scanner-in-python)

---

## 📘 Scanner de Ports en Python

### 🎯 Objectif

Créer un script Python qui analyse les ports d'une machine donnée (par défaut `127.0.0.1`) sur une plage définie, et affiche les ports ouverts.

### 🧠 Ce que j’ai appris

- Le fonctionnement des sockets en Python (`socket.socket`, `connect_ex`)
- La différence entre un port ouvert et un port fermé
- Comment tester manuellement une connexion à un port
- La logique d’un scanner de ports bas niveau

### 🧱 Contenu du script (`port_scanner_pw.py`)

```python
socket.socket(AF_INET, SOCK_STREAM)  # Création du socket
connect_ex((IP, port))               # Test de connexion
```

- Le script scanne les ports de 20 à 100 (modifiable)
- Utilise `settimeout(0.5)` pour que le scan ne soit pas bloquant
- Affiche les ports ouverts dans la console

### 🧪 Exemple d'exécution

```bash
python port_scanner_pw.py
```

🔎 Résultat :
```
[Python] Port 22 is open.
[Python] Port 80 is open.
```

### 📌 Auteur

**Jessica Longane**  
Formation Cybersécurité – BeCode  
Septembre 2025

---

## 📙 Port Scanner in Python

### 🎯 Goal

Build a Python script that scans a target machine’s ports (default: `127.0.0.1`) over a given range and prints the open ones.

### 🧠 What I learned

- How Python sockets work (`socket.socket`, `connect_ex`)
- The difference between open and closed ports
- How to manually test a port connection
- The logic of a low-level port scanner

### 🧱 Script Content (`port_scanner_pw.py`)

```python
socket.socket(AF_INET, SOCK_STREAM)  # Create socket
connect_ex((IP, port))               # Attempt connection
```

- Scans ports from 20 to 100 (can be changed)
- Uses `settimeout(0.5)` to avoid blocking
- Displays open ports in the terminal

### 🧪 Example usage

```bash
python port_scanner_pw.py
```

🔎 Output:
```
[Python] Port 22 is open.
[Python] Port 80 is open.
```

### 📌 Author

**Jessica Longane**  
Cybersecurity Training – BeCode  
September 2025

### This project has been done in a safe and controlled VM, the test and execution have been according to cybersecurity laws.
