# 🔍 Port Scanner Project – Python + Nmap

🇫🇷 [Lire en Français](#-projet-de-scanner-de-ports-python--nmap) · 🇬🇧 [Read in English](#-port-scanner-project-python--nmap)

---

# 🔍 Port Scanner Project (Python + Nmap)

Ce projet démontre ma compréhension des **sockets en Python** et de l'outil **Nmap** pour réaliser des scans de ports sur une machine cible.

## 🎯 Objectif

Créer un **scanner de ports** personnalisé en Python, comparer les résultats avec un **scan Nmap**, et comprendre comment fonctionnent les sockets et les protocoles TCP/IP.

---

## 🧱 Contenu du projet

- `port_scanner_pw.py`  
  → Scanner maison utilisant `socket` et `connect_ex()` pour tester les ports un par un.

- `nmap_port_scan.py`  
  → Scanner basé sur `nmap` via la bibliothèque `python-nmap`.

- `port_scanner_with_nmap.py`  
  → Version combinée qui lance un scan avec les sockets **et** un scan Nmap, pour comparer les résultats.

---

## ⚙️ Prérequis

```bash
pip install python-nmap
```

⚠️ Il faut aussi que **Nmap** soit installé sur ta machine :
- Sous Linux : `sudo apt install nmap`
- Sous Mac : `brew install nmap`
- Sous Windows : télécharger depuis [nmap.org](https://nmap.org)

---

## 🚀 Lancer les scripts

### 🔸 Scanner maison (Python socket)
```bash
python port_scanner_pw.py
```

### 🔸 Scanner avec Nmap
```bash
python nmap_port_scan.py
```

### 🔸 Comparaison des deux
```bash
python port_scanner_with_nmap.py
```

---

## 🧠 Ce que j’ai compris

✅ Comment fonctionne un socket :  
→ C’est une prise réseau logique qui permet la communication entre un client et un serveur.

✅ Le rôle des ports :  
→ Chaque port représente un service différent (SSH = 22, HTTP = 80…).

✅ La différence entre TCP et UDP  
→ TCP est fiable et connecté (3-way handshake), UDP est rapide mais sans garantie.

✅ L’utilisation de Nmap  
→ Plus rapide, plus complet, mais plus lourd. Mon scanner maison est simple mais efficace.

---

## 📚 Résultat attendu

Le script affiche les ports **ouverts** avec deux approches différentes.

--- 
## 📌 Autheur
Jessica Longane
Formation Cybersécurité — BeCode  
Projet personnel — Port scanning & sockets

# 🔍 Port Scanner Project (Python + Nmap)

[🇫🇷 Lire en français](./README.md)

This project demonstrates my understanding of **Python sockets** and the use of **Nmap** to scan ports on a target machine.

## 🎯 Objective

Build a custom **port scanner** using Python sockets, compare results with **Nmap**, and explain how sockets and TCP/IP protocols work.

---

## 🧱 Project Contents

- `port_scanner_pw.py`  
  → Custom port scanner using `socket` and `connect_ex()` to test ports one by one.

- `nmap_port_scan.py`  
  → Scanner using `nmap` through the `python-nmap` library.

- `port_scanner_with_nmap.py`  
  → Combined version running both socket scan and Nmap scan to compare results.

---

## ⚙️ Requirements

```bash
pip install python-nmap
```

⚠️ You must also have **Nmap** installed:
- On Linux: `sudo apt install nmap`
- On Mac: `brew install nmap`
- On Windows: download from [nmap.org](https://nmap.org)

---

## 🚀 Running the Scripts

### 🔸 Custom Python Scanner
```bash
python port_scanner_pw.py
```

### 🔸 Nmap-based Scanner
```bash
python nmap_port_scan.py
```

### 🔸 Comparison of Both
```bash
python port_scanner_with_nmap.py
```

---

## 🧠 What I’ve learned

✅ How sockets work:  
→ A socket is a logical network plug that enables communication between a client and a server.

✅ Role of ports:  
→ Each port maps to a specific service (SSH = 22, HTTP = 80…).

✅ TCP vs UDP:  
→ TCP is reliable and connection-oriented (3-way handshake), UDP is faster but less reliable.

✅ Nmap usage:  
→ More powerful and complete, but heavier. My socket-based scanner is lightweight and simple.

---

## 📚 Expected Output

Each script shows the **open ports** using two scanning approaches.

---

## 📌 Author

Jessica Longane  
Cybersecurity Training — BeCode  
Personal Project — Port scanning & sockets

