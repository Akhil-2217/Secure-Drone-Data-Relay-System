# Secure-Drone-Data-Relay-System
Air-Gapped Secure Data Transfer Simulation using Python, Tkinter &amp; AES Encryption (Fernet)



This project simulates secure offline data transfer between two isolated networks using drone-based physical transport.



**Features:**

- AES-based Encryption using Fernet (Cryptography Library)
- 
- Tkinter GUI Simulation

- Drone Transfer Animation

- Secure Key Generation & Storage

- End-to-End Encryption & Decryption



**Concept:**

- Air-gapped systems are used in:

- Military networks

- Nuclear facilities

- Classified research labs

- Critical infrastructure

- Traditional USB-based transfer methods introduce malware risks.

- This project demonstrates a secure drone-mediated encrypted data relay mechanism.



**Technologies Used:**

- Python

- Tkinter

- Cryptography (Fernet AES)

- OS & File Handling

- GUI Simulation



**Workflow:**

- Network A enters confidential message

- Message is encrypted using AES

- Drone physically transfers encrypted file

- Network B decrypts message using secure key



**Encryption Module**

This standalone module handles:

- Secure key generation
- AES-based encryption (Fernet)
- Secure decryption
- File-based encrypted transfer simulation
