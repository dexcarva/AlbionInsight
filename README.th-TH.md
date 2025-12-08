# Albion Insight (ภาษาไทย)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Albion Insight** เป็นเครื่องมือวิเคราะห์สถิติข้ามแพลตฟอร์ม (Linux, Windows, macOS) สำหรับเกม Albion Online ซึ่งถูกนำมาสร้างใหม่ในภาษา **Python** โดยใช้เฟรมเวิร์ก **Flet** เครื่องมือนี้ออกแบบมาเพื่อติดตามสถิติในเกมแบบเรียลไทม์ รวมถึงเงิน (silver), ชื่อเสียง (fame), และข้อมูลการต่อสู้ (Damage Meter) โดยการวิเคราะห์การรับส่งข้อมูลเครือข่าย (network traffic)

โครงการนี้เป็นทางเลือกที่ทันสมัยและเป็นโอเพนซอร์สสำหรับเครื่องมือ `AlbionOnline-StatisticsAnalysis` ดั้งเดิมที่ใช้ C#/WPF โดยเน้นที่ความเข้ากันได้กับหลายแพลตฟอร์มและความง่ายในการใช้งาน

## คุณสมบัติ (Features)

*   **ความเข้ากันได้ข้ามแพลตฟอร์ม:** ทำงานได้บน Linux, Windows, และ macOS
*   **การติดตามแบบเรียลไทม์:** ใช้ไลบรารี `Scapy` เพื่อดักจับแพ็กเก็ต UDP บนพอร์ต Albion Online (5055, 5056, 5058)
*   **โครงสร้าง Damage Meter:** มีโครงสร้างข้อมูลและ UI ที่จำเป็นในการแสดงสถิติการต่อสู้สด (ความเสียหายที่ทำได้, การรักษาที่ทำได้, DPS)
*   **UI ที่ทันสมัย:** สร้างด้วย Flet ให้แอปพลิเคชันเดสก์ท็อปที่ดูเป็นธรรมชาติและรวดเร็ว
*   **การจัดการเซสชัน:** อนุญาตให้เริ่ม, หยุด, รีเซ็ต, และบันทึกสถิติเซสชัน

## ข้อกำหนดเบื้องต้น (Prerequisites)

*   Python 3.8+
*   ไลบรารี **Flet** และ **Scapy**
*   **สิทธิ์ Root/Administrator:** จำเป็นสำหรับการดักจับแพ็กเก็ตเครือข่าย

## การติดตั้งและการตั้งค่า (Installation and Setup)

### ตัวเลือกที่ 1: ติดตั้งด่วน (Linux - แนะนำ)

สำหรับผู้ใช้ Linux เรามีสคริปต์การติดตั้งอัตโนมัติ:

\`\`\`bash
# 1. โคลน repository
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. รันสคริปต์การติดตั้ง
./install.sh

# 3. รันแอปพลิเคชัน
./run.sh
\`\`\`

สคริปต์ `install.sh` จะ:
- ติดตั้ง system dependencies (`libpcap-dev`, `python3-pip`, `python3-venv`)
- สร้างสภาพแวดล้อมเสมือน Python (virtual environment)
- ติดตั้งแพ็กเกจ Python ที่จำเป็นทั้งหมด (Flet, Scapy)

สคริปต์ `run.sh` จะร้องขอสิทธิ์ root โดยอัตโนมัติและรันแอปพลิเคชัน

### ตัวเลือกที่ 2: การติดตั้งด้วยตนเอง (Manual Installation)

#### 1. ติดตั้ง System Dependencies

**บน Linux (Debian/Ubuntu):**

\`\`\`bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
\`\`\`

**บน Windows:**

ติดตั้ง Python 3.8+ จาก [python.org](https://www.python.org/downloads/)

#### 2. ติดตั้ง Python Dependencies

**บน Linux (ใช้ virtual environment - แนะนำ):**

\`\`\`bash
# สร้าง virtual environment
python3 -m venv venv

# เปิดใช้งาน virtual environment
source venv/bin/activate

# ติดตั้ง dependencies
pip install flet scapy
\`\`\`

**บน Linux (ติดตั้งทั่วทั้งระบบ):**

\`\`\`bash
pip3 install flet scapy --break-system-packages
\`\`\`

**บน Windows:**

\`\`\`bash
pip install flet scapy
\`\`\`

#### 3. การรันแอปพลิเคชัน

เนื่องจากการดักจับเครือข่ายต้องใช้สิทธิ์ที่สูงขึ้น คุณต้องรันแอปพลิเคชันในฐานะ root หรือ administrator

**บน Linux (พร้อม virtual environment):**

\`\`\`bash
sudo venv/bin/python3 -m albion_insight
\`\`\`

**บน Linux (ติดตั้งทั่วทั้งระบบ):**

\`\`\`bash
sudo python3 -m albion_insight
\`\`\`

**บน Windows (รัน Command Prompt/PowerShell ในฐานะ Administrator):**

\`\`\`bash
python -m albion_insight
\`\`\`

แอปพลิเคชันจะเปิดขึ้นในหน้าต่างเดสก์ท็อปแบบ native

## วิธีสร้างไฟล์ปฏิบัติการ (Executable)

แอปพลิเคชันสามารถถูกแพ็กเกจเป็นไฟล์ปฏิบัติการแบบสแตนด์อโลนโดยใช้ **PyInstaller** สิ่งนี้ช่วยให้ผู้ใช้สามารถรันแอปพลิเคชันได้โดยไม่ต้องติดตั้ง Python หรือ dependencies

สำหรับคำแนะนำโดยละเอียดเกี่ยวกับการสร้างไฟล์ปฏิบัติการสำหรับ Linux, Windows, และ macOS โปรดดูที่คู่มือ **[PACKAGING.md](PACKAGING.md)**

### Quick Build (Linux)

\`\`\`bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
\`\`\`

ไฟล์ปฏิบัติการจะอยู่ในโฟลเดอร์ `dist/`

## โครงสร้างโครงการ (Project Structure)

แอปพลิเคชันถูกจัดโครงสร้างเป็นส่วนประกอบแบบโมดูลาร์เพื่อการบำรุงรักษาและความสามารถในการปรับขนาดที่ดีขึ้น:

| ไฟล์ | คำอธิบาย |
| :--- | :--- |
| `albion_insight/core/` | ตรรกะหลัก, การติดตามเครือข่าย, โมเดลข้อมูล, และการถอดรหัสโปรโตคอล |
| `albion_insight/ui/` | ส่วนประกอบส่วนต่อประสานผู้ใช้ที่สร้างด้วย Flet |
| `albion_insight/utils/` | ฟังก์ชันยูทิลิตี้, การกำหนดค่า, และการบันทึก (logging) |
| `albion_insight/__main__.py` | จุดเริ่มต้นสำหรับแอปพลิเคชัน |
| `README.md` | ไฟล์เอกสารนี้ |
| `CONTRIBUTING.md` | แนวทางสำหรับการมีส่วนร่วมในโครงการ |
| `CODE_OF_CONDUCT.md` | จรรยาบรรณของโครงการ |
| `SECURITY.md` | นโยบายสำหรับการรายงานช่องโหว่ด้านความปลอดภัย |
| `README.it-IT.md` | Documentazione in italiano. |
| `README.pt-BR.md` | Documentação em português do Brasil. |
| `README.ru-RU.md` | Документация на русском языке. |
| `README.fr-FR.md` | Documentation en français. |
| `README.zh-CN.md` | 简体中文文档 (Simplified Chinese documentation). |
| `README.ko-KR.md` | 한국어 문서 (Korean documentation). |
| `README.es-ES.md` | Documentación en español (Spanish documentation). |
| `README.de-DE.md` | Dokumentation in deutscher Sprache (German documentation). |
| `README.pl-PL.md` | Dokumentacja w języku polskim (Polish documentation). |
| `README.sv-SE.md` | Dokumentation på svenska (Swedish documentation). |
| `README.vi-VN.md` | Tài liệu bằng tiếng Việt (Vietnamese documentation). |
| `README.ar-SA.md` | توثيق باللغة العربية (Arabic documentation). |
| `README.pt-PT.md` | Documentação em português europeu. |
| `README.hi-IN.md` | Hindi में दस्तावेज़ीकरण (Hindi documentation). |
| `README.hu-HU.md` | Dokumentáció magyar nyelven (Hungarian documentation). |
| `README.th-TH.md` | เอกสารประกอบภาษาไทย (Thai documentation). |

## สถานะปัจจุบัน (ข้อมูลเรียลไทม์)

แอปพลิเคชันตอนนี้รวมตรรกะ **Photon Protocol Decoding** ซึ่งแปลมาจากโครงการ C# ดั้งเดิม สิ่งนี้ช่วยให้แอปพลิเคชันสามารถประมวลผลเหตุการณ์เรียลไทม์ เช่น `UpdateMoney`, `UpdateFame`, `KilledPlayer`, และ `Died` ได้โดยตรงจากการรับส่งข้อมูลเครือข่าย

**หมายเหตุ:** การแปลเหตุการณ์การต่อสู้ทั้งหมด (เช่น `CastHit`, `Attack`) เป็นความพยายามที่กำลังดำเนินอยู่ การใช้งานในปัจจุบันมุ่งเน้นไปที่สถิติหลักและโครงสร้างสำหรับ Damage Meter การคำนวณ DPS ของ Damage Meter ขึ้นอยู่กับเหตุการณ์ที่ถอดรหัสแล้ว

## การมีส่วนร่วม (Contributing)

เรายินดีรับการมีส่วนร่วมจากชุมชน! ไม่ว่าคุณจะเป็นนักพัฒนา, นักออกแบบ, หรือเพียงแค่ผู้ที่ชื่นชอบ Albion Online ก็มีหลายวิธีที่จะช่วยปรับปรุง Albion Insight

โปรดอ่าน [แนวทางการมีส่วนร่วม](CONTRIBUTING.md) ของเราสำหรับข้อมูลโดยละเอียดเกี่ยวกับวิธีการมีส่วนร่วมในโครงการนี้

### Quick Start สำหรับผู้มีส่วนร่วม:

1.  Fork repository: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Clone fork ของคุณ: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  สร้าง branch ใหม่: `git checkout -b feature/your-feature-name`
4.  ทำการเปลี่ยนแปลงและ commit: `git commit -m "Add your feature"`
5.  Push ไปยัง fork ของคุณ: `git push origin feature/your-feature-name`
6.  เปิด Pull Request บน repository หลัก

## ใบอนุญาต (License)

โครงการนี้ได้รับอนุญาตภายใต้ MIT License - ดูไฟล์ [LICENSE](LICENSE) สำหรับรายละเอียด

## การรับทราบ (Acknowledgments)

- โครงการดั้งเดิม: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) โดย Triky313
- สร้างด้วยเฟรมเวิร์ก [Flet](https://flet.dev/)
- การวิเคราะห์เครือข่ายขับเคลื่อนโดย [Scapy](https://scapy.net/)

---
*โซลูชันข้ามแพลตฟอร์มสำหรับชุมชน Albion Online*
