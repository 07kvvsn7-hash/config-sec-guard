import re

# รายการคำต้องห้ามที่เสี่ยงจะหลุดรอด (Hardcoded Secrets / Sensitive Keywords)
SENSITIVE_KEYWORDS = ['password', 'secret', 'api_key', 'access_token']

def check_config_file(file_path):
    print(f"--- กำลังตรวจสอบไฟล์: {file_path} ---")
    issues_found = 0
    
    try:
        #เปิดไฟล์ขึ้นมาอ่านทีละบรรทัด
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                #ตัดช่องว่างหัวท้ายออก
                line_stripped = line.strip()
                
                #ข้ามบรรทัดว่างหรือบรรทัดที่เป็นคอมเมนต์ (ขึ้นต้นด้วย #)
                if not line_stripped or line_stripped.startswith('#'):
                    continue
                
                # 1.เช็กหาคำต้องห้ามที่เป็น Sensitive data
                for keyword in SENSITIVE_KEYWORDS:
                    if keyword in line_stripped.lower():
                        print(f"[!] คำเตือน (บรรทัดที่ {line_num}): พบคำว่า '{keyword}' ซึ่งอาจเป็นข้อมูลลับที่ถูก Hardcode ไว้")
                        print(f"    -> เนื้อหา: {line_stripped}")
                        issues_found += 1
                
                # 2.เช็กการเปิดโหมด Debug ทิ้งไว้
                if 'debug' in line_stripped.lower() and ('true' in line_stripped.lower() or '1' in line_stripped):
                    print(f"[!] คำเตือน (บรรทัดที่ {line_num}): พบการเปิดโหมด Debug ทิ้งไว้ ('{line_stripped}')")
                    issues_found += 1
                    
        #สรุปผลการตรวจ
        print("-" * 40)
        if issues_found == 0:
            print("[✔] ปลอดภัย ไม่พบจุดเสี่ยงในไฟล์นี้")
        else:
            print(f"[X] พบความเสี่ยงทั้งหมด {issues_found} จุด แนะนำให้นำไปเก็บไว้ใน Environment Variables แทน")
            
    except FileNotFoundError:
        print(f"[X] ไม่พบไฟล์ {file_path} กรุณาตรวจสอบตำแหน่งไฟล์อีกครั้ง")

#จุดเริ่มต้นการทำงานของสคริปต์
if __name__ == "__main__":
    check_config_file("sample_config.env")