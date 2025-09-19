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

Jessica Longane
Formation Cybersécurité — BeCode  
Projet personnel — Port scanning & sockets
