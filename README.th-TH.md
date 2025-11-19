# Albion Insight

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**[อ่านเป็นภาษาไทย](README.th-TH.md)**

**Albion Insight** เป็นเครื่องมือวิเคราะห์สถิติข้ามแพลตฟอร์ม (Linux, Windows, macOS) สำหรับเกม Albion Online ซึ่งถูกนำมาพัฒนาใหม่ในภาษา **Python** โดยใช้เฟรมเวิร์ก **Flet** ถูกออกแบบมาเพื่อติดตามสถิติในเกมแบบเรียลไทม์ รวมถึง Silver, Fame และข้อมูลการต่อสู้ (Damage Meter) โดยการวิเคราะห์ทราฟฟิกเครือข่าย

โปรเจกต์นี้เป็นทางเลือกที่ทันสมัยและเป็นโอเพนซอร์สแทนที่เครื่องมือ `AlbionOnline-StatisticsAnalysis` ที่ใช้ C#/WPF แบบดั้งเดิม โดยมุ่งเน้นที่ความเข้ากันได้หลายแพลตฟอร์มและใช้งานง่าย

## คุณสมบัติ

*   **ความเข้ากันได้ข้ามแพลตฟอร์ม:** ทำงานได้บน Linux, Windows และ macOS
*   **การติดตามแบบเรียลไทม์:** ใช้ไลบรารี `Scapy` เพื่อดักจับแพ็กเก็ต UDP บนพอร์ตของ Albion Online (5055, 5056, 5058)
*   **โครงสร้าง Damage Meter:** รวมถึงโครงสร้างข้อมูลและ UI ที่จำเป็นในการแสดงสถิติการต่อสู้แบบสด (Damage Done, Healing Done, DPS)
*   **UI ที่ทันสมัย:** สร้างด้วย Flet ทำให้ได้แอปพลิเคชันเดสก์ท็อปที่รวดเร็วและดูเป็นธรรมชาติ
*   **การจัดการเซสชัน:** อนุญาตให้เริ่ม, หยุด, รีเซ็ต และบันทึกสถิติของเซสชัน

## ข้อกำหนดเบื้องต้น

*   Python 3.8+
*   ไลบรารี **Flet** และ **Scapy**
*   **สิทธิ์ Root/Administrator:** จำเป็นสำหรับการดักจับแพ็กเก็ตเครือข่าย

## การติดตั้งและการตั้งค่า

### ตัวเลือกที่ 1: ติดตั้งด่วน (Linux - แนะนำ)

สำหรับผู้ใช้ Linux เรามีสคริปต์การติดตั้งอัตโนมัติ:

```bash
# 1. โคลนที่เก็บ
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. เรียกใช้สคริปต์การติดตั้ง
./install.sh

# 3. เรียกใช้แอปพลิเคชัน
./run.sh
```

สคริปต์ `install.sh` จะ:
- ติดตั้งการพึ่งพาระบบ (`libpcap-dev`, `python3-pip`, `python3-venv`)
- สร้างสภาพแวดล้อมเสมือนของ Python
- ติดตั้งแพ็คเกจ Python ที่จำเป็นทั้งหมด (Flet, Scapy)

สคริปต์ `run.sh` จะขอสิทธิ์ root โดยอัตโนมัติและเรียกใช้แอปพลิเคชัน

### ตัวเลือกที่ 2: การติดตั้งด้วยตนเอง

#### 1. ติดตั้งการพึ่งพาระบบ

**บน Linux (Debian/Ubuntu):**

```bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
```

**บน Windows:**

ติดตั้ง Python 3.8+ จาก [python.org](https://www.python.org/downloads/)

#### 2. ติดตั้งการพึ่งพา Python

**บน Linux (โดยใช้สภาพแวดล้อมเสมือน - แนะนำ):**

```bash
# สร้างสภาพแวดล้อมเสมือน
python3 -m venv venv

# เปิดใช้งานสภาพแวดล้อมเสมือน
source venv/bin/activate

# ติดตั้งการพึ่งพา
pip install flet scapy
```

**บน Linux (การติดตั้งทั่วทั้งระบบ):**

```bash
pip3 install flet scapy --break-system-packages
```

**บน Windows:**

```bash
pip install flet scapy
```

#### 3. การเรียกใช้แอปพลิเคชัน

เนื่องจากการดักจับเครือข่ายต้องการสิทธิ์ระดับสูง คุณต้องเรียกใช้แอปพลิเคชันในฐานะ root หรือ administrator

**บน Linux (พร้อมสภาพแวดล้อมเสมือน):**

```bash
sudo venv/bin/python3 albion_insight/main.py
```

**บน Linux (การติดตั้งทั่วทั้งระบบ):**

```bash
sudo python3 albion_insight/main.py
```

**บน Windows (เรียกใช้ Command Prompt/PowerShell ในฐานะ Administrator):**

```bash
python albion_insight/main.py
```

แอปพลิเคชันจะเปิดขึ้นในหน้าต่างเดสก์ท็อป

## วิธีสร้างไฟล์ปฏิบัติการ

แอปพลิเคชันสามารถบรรจุเป็นไฟล์ปฏิบัติการแบบสแตนด์อโลนได้โดยใช้ **PyInstaller** ซึ่งช่วยให้ผู้ใช้สามารถเรียกใช้แอปพลิเคชันได้โดยไม่ต้องติดตั้ง Python หรือการพึ่งพา

สำหรับคำแนะนำโดยละเอียดเกี่ยวกับการสร้างไฟล์ปฏิบัติการสำหรับ Linux, Windows และ macOS โปรดดูคู่มือ **[PACKAGING.md](PACKAGING.md)**

### สร้างด่วน (Linux)

```bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
```

ไฟล์ปฏิบัติการจะอยู่ในโฟลเดอร์ `dist/`

## โครงสร้างโปรเจกต์

แอปพลิเคชันทั้งหมดอยู่ในไฟล์เดียวเพื่อความเรียบง่าย:

| ไฟล์ | คำอธิบาย |
| :--- | :--- |
| `albion_insight/main.py` | ไฟล์แอปพลิเคชันหลักที่มีตรรกะทั้งหมด (Models, Network Tracker, Flet UI) |
| `README.md` | ไฟล์เอกสารนี้ |
| `README.pt-BR.md` | ไฟล์เอกสารนี้ในภาษาโปรตุเกสแบบบราซิล |
| `CONTRIBUTING.md` | แนวทางสำหรับการมีส่วนร่วมในโปรเจกต์ |
| `CODE_OF_CONDUCT.md` | หลักจรรยาบรรณของโปรเจกต์ |
| `SECURITY.md` | นโยบายการรายงานช่องโหว่ด้านความปลอดภัย |

## สถานะปัจจุบัน (ข้อมูลเรียลไทม์)

ขณะนี้แอปพลิเคชันได้รวมตรรกะ **การถอดรหัสโปรโตคอล Photon** ซึ่งแปลมาจากโปรเจกต์ C# ดั้งเดิมแล้ว ซึ่งช่วยให้แอปพลิเคชันสามารถประมวลผลเหตุการณ์แบบเรียลไทม์ เช่น `UpdateMoney`, `UpdateFame`, `KilledPlayer` และ `Died` ได้โดยตรงจากทราฟฟิกเครือข่าย

**หมายเหตุ:** การแปลเหตุการณ์การต่อสู้ทั้งหมด (เช่น `CastHit`, `Attack`) ยังคงเป็นความพยายามอย่างต่อเนื่อง การใช้งานในปัจจุบันมุ่งเน้นไปที่สถิติหลักและโครงสร้างสำหรับ Damage Meter การคำนวณ DPS ของ Damage Meter ขึ้นอยู่กับเหตุการณ์ที่ถอดรหัส

## การมีส่วนร่วม

เรายินดีรับการมีส่วนร่วมจากชุมชน! ไม่ว่าคุณจะเป็นนักพัฒนา, นักออกแบบ หรือเพียงแค่ผู้ที่ชื่นชอบ Albion Online ก็มีหลายวิธีที่จะช่วยปรับปรุง Albion Insight

โปรดอ่าน [แนวทางการมีส่วนร่วม](CONTRIBUTING.md) ของเราสำหรับข้อมูลโดยละเอียดเกี่ยวกับวิธีการมีส่วนร่วมในโปรเจกต์นี้

### เริ่มต้นอย่างรวดเร็วสำหรับผู้มีส่วนร่วม:

1.  Fork ที่เก็บ: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  โคลน fork ของคุณ: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  สร้างสาขาใหม่: `git checkout -b feature/your-feature-name`
4.  ทำการเปลี่ยนแปลงและคอมมิต: `git commit -m "Add your feature"`
5.  พุชไปยัง fork ของคุณ: `git push origin feature/your-feature-name`
6.  เปิด Pull Request บนที่เก็บหลัก

## ใบอนุญาต

โปรเจกต์นี้ได้รับอนุญาตภายใต้ใบอนุญาต MIT - ดูรายละเอียดในไฟล์ [LICENSE](LICENSE)

## การยอมรับ

- โปรเจกต์ดั้งเดิม: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) โดย Triky313
- สร้างด้วยเฟรมเวิร์ก [Flet](https://flet.dev/)
- การวิเคราะห์เครือข่ายขับเคลื่อนโดย [Scapy](https://scapy.net/)

---
*โซลูชันข้ามแพลตฟอร์มสำหรับชุมชน Albion Online*
