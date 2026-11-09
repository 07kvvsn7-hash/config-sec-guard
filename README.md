Config Sec Guard (หรือใส่ชื่อที่เลือก)

Lightweight Python script designed to scan configuration files (`.env`, `json`, etc.) for hardcoded secrets, sensitive credentials, and insecure debug settings. Built to help developers catch security risks early.

---

Features
* **Hardcoded Secret Detection:** Automatically scans for exposed keywords like passwords, API keys, and access tokens.
* **Insecure Setting Alerts:** Flags dangerous configurations such as `DEBUG=True` left enabled.
* **Lightweight & Fast:** Pure Python implementation using standard libraries (Zero external dependencies!).

---

Project Structure
```text
config-sec-guard/
│
├── config_checker.py     # Main Python script for scanning
└── README.md             # Documentation

Thailand
Config Sec Guard

สคริปต์ Python น้ำหนักเบาที่ออกแบบมาเพื่อสแกนไฟล์คอนฟิก (เช่น `.env`, `json` ฯลฯ) เพื่อหาข้อมูลลับที่ถูกฝังไว้ในโค้ด (Hardcoded secrets), ข้อมูลรับรองความปลอดภัย และการตั้งค่าโหมด Debug ที่ไม่ปลอดภัย ช่วยให้นักพัฒนาสามารถตรวจจับความเสี่ยงด้านความปลอดภัยได้ตั้งแต่เนิ่น ๆ

---

ฟีเจอร์เด่น
* **ตรวจจับข้อมูลลับที่ฝังไว้:** สแกนหาคีย์เวิร์ดที่เปิดเผย เช่น รหัสผ่าน, API Keys และ Access Tokens โดยอัตโนมัติ
* **แจ้งเตือนการตั้งค่าที่ไม่ปลอดภัย:** แจ้งเตือนการตั้งค่าที่เป็นอันตราย เช่น การเปิด `DEBUG=True` ทิ้งไว้
* **รวดเร็วและเบาสบาย:** เขียนด้วย Python ล้วน ๆ ใช้แค่ Standard Libraries มาตรฐาน (ไม่ต้องติดตั้งไลบรารีเสริมใด ๆ!)

---

โครงสร้างโปรเจกต์
```text
config-sec-guard/
│
├── config_checker.py     # สคริปต์ Python หลักสำหรับใช้สแกน
└── README.md             # เอกสารอธิบายโปรเจกต์
