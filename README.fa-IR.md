# Albion Insight

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Albion Insight** یک ابزار تحلیل آمار چند پلتفرمی (لینوکس، ویندوز، macOS) برای بازی Albion Online است که با استفاده از فریم‌ورک **Flet** در **پایتون** بازنویسی شده است. این ابزار برای ردیابی آمار درون بازی در زمان واقعی، شامل نقره، شهرت، و داده‌های مبارزه (Damage Meter)، از طریق تحلیل ترافیک شبکه طراحی شده است.

این پروژه یک جایگزین مدرن و متن‌باز برای ابزار اصلی `AlbionOnline-StatisticsAnalysis` مبتنی بر C#/WPF است که بر سازگاری چند پلتفرمی و سهولت استفاده تمرکز دارد.

## ویژگی‌ها

*   **سازگاری چند پلتفرمی:** به صورت بومی بر روی لینوکس، ویندوز و macOS اجرا می‌شود.
*   **ردیابی در زمان واقعی:** از کتابخانه `Scapy` برای شنود بسته‌های UDP در پورت‌های Albion Online (5055، 5056، 5058) استفاده می‌کند.
*   **ساختار Damage Meter:** شامل ساختارهای داده و رابط کاربری لازم برای نمایش آمار زنده مبارزه (میزان آسیب وارد شده، میزان درمان انجام شده، DPS) است.
*   **رابط کاربری مدرن:** با Flet ساخته شده و یک برنامه دسکتاپ سریع و با ظاهر بومی ارائه می‌دهد.
*   **مدیریت جلسات:** امکان شروع، توقف، بازنشانی و ذخیره آمار جلسات را فراهم می‌کند.

## پیش‌نیازها

*   پایتون 3.8+
*   کتابخانه‌های **Flet** و **Scapy**.
*   **امتیازات روت/مدیر:** برای ضبط بسته‌های شبکه ضروری است.

## نصب و راه‌اندازی

### گزینه 1: نصب سریع (لینوکس - توصیه شده)

برای کاربران لینوکس، اسکریپت‌های نصب خودکار ارائه شده است:

\`\`\`bash
# 1. Clone the repository
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Run the installation script
./install.sh

# 3. Run the application
./run.sh
\`\`\`

اسکریپت `install.sh` موارد زیر را انجام می‌دهد:

*   نصب وابستگی‌های سیستمی (`libpcap-dev`، `python3-pip`، `python3-venv`)
*   ایجاد یک محیط مجازی پایتون
*   نصب تمام بسته‌های پایتون مورد نیاز (Flet، Scapy)

اسکریپت `run.sh` به طور خودکار امتیازات روت را درخواست کرده و برنامه را اجرا می‌کند.

### گزینه 2: نصب دستی

#### 1. نصب وابستگی‌های سیستمی

**در لینوکس (Debian/Ubuntu):**

\`\`\`bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
\`\`\`

**در ویندوز:**

پایتون 3.8+ را از [python.org](https://www.python.org/downloads/) نصب کنید.

#### 2. نصب وابستگی‌های پایتون

**در لینوکس (با استفاده از محیط مجازی - توصیه شده):**

\`\`\`bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install flet scapy
\`\`\`

**در لینوکس (نصب سراسری):**

\`\`\`bash
pip3 install flet scapy --break-system-packages
\`\`\`

**در ویندوز:**

\`\`\`bash
pip install flet scapy
\`\`\`

#### 3. اجرای برنامه

از آنجایی که شنود شبکه نیاز به امتیازات بالا دارد، باید برنامه را به عنوان روت یا مدیر اجرا کنید.

**در لینوکس (با محیط مجازی):**

\`\`\`bash
sudo venv/bin/python3 -m albion_insight
\`\`\`

**در لینوکس (نصب سراسری):**

\`\`\`bash
sudo python3 -m albion_insight
\`\`\`

**در ویندوز (اجرای Command Prompt/PowerShell به عنوان مدیر):**

\`\`\`bash
python -m albion_insight
\`\`\`

برنامه در یک پنجره دسکتاپ بومی باز خواهد شد.

## نحوه ساخت فایل اجرایی

این برنامه می‌تواند با استفاده از **PyInstaller** در یک فایل اجرایی مستقل بسته‌بندی شود. این کار به کاربران اجازه می‌دهد تا برنامه را بدون نصب پایتون یا وابستگی‌های آن اجرا کنند.

برای دستورالعمل‌های دقیق در مورد ساخت فایل‌های اجرایی برای لینوکس، ویندوز و macOS، به راهنمای **[PACKAGING.md](PACKAGING.md)** مراجعه کنید.

### ساخت سریع (لینوکس)

\`\`\`bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
\`\`\`

فایل اجرایی در پوشه `dist/` قرار خواهد گرفت.

## ساختار پروژه

این برنامه برای نگهداری و مقیاس‌پذیری بهتر به اجزای ماژولار تقسیم شده است:

| فایل | توضیحات |
| :--- | :--- |
| `albion_insight/core/` | منطق اصلی، ردیابی شبکه، مدل‌های داده و رمزگشایی پروتکل. |
| `albion_insight/ui/` | اجزای رابط کاربری ساخته شده با Flet. |
| `albion_insight/utils/` | توابع کمکی، پیکربندی و ثبت وقایع. |
| `albion_insight/__main__.py` | نقطه ورود برنامه. |
| `README.md` | این فایل مستندات. |
| `CONTRIBUTING.md` | دستورالعمل‌های مشارکت در پروژه. |
| `CODE_OF_CONDUCT.md` | منشور اخلاقی پروژه. |
| `SECURITY.md` | سیاست گزارش آسیب‌پذیری‌های امنیتی. |
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
| `README.ja-JP.md` | 日本語のドキュメント (Japanese documentation). |
| `README.tr-TR.md` | Türkçe dokümantasyon (Turkish documentation). |
| `README.id-ID.md` | Dokumentasi dalam Bahasa Indonesia. |
| `README.sk-SK.md` | Dokumentácia v slovenčine (Slovak documentation). |
| `README.cs-CZ.md` | Dokumentace v češtině (Czech documentation). |
| `README.fi-FI.md` | Dokumentaatio suomeksi (Finnish documentation). |
| `README.nl-NL.md` | Documentatie in het Nederlands (Dutch documentation). |
| `README.zh-TW.md` | 繁體中文文件 (Traditional Chinese documentation). |
| `README.el-GR.md` | Τεκμηρίωση στα Ελληνικά (Greek documentation). |
| `README.fa-IR.md` | مستندات به زبان فارسی (Persian documentation). |

## وضعیت فعلی (داده‌های در زمان واقعی)

این برنامه اکنون شامل منطق **رمزگشایی پروتکل فوتون** است که از پروژه اصلی C# ترجمه شده است. این امکان را به برنامه می‌دهد تا رویدادهای در زمان واقعی مانند `UpdateMoney`، `UpdateFame`، `KilledPlayer` و `Died` را مستقیماً از ترافیک شبکه پردازش کند.

**توجه:** ترجمه کامل هر رویداد مبارزه (مانند `CastHit`، `Attack`) یک تلاش در حال انجام است. پیاده‌سازی فعلی بر آمار اصلی و ساختار Damage Meter تمرکز دارد. محاسبه DPS در Damage Meter بر اساس رویدادهای رمزگشایی شده است.

## مشارکت

ما از مشارکت‌های جامعه استقبال می‌کنیم! چه توسعه‌دهنده باشید، چه طراح، یا فقط یک علاقه‌مند به Albion Online، راه‌های زیادی برای کمک به بهبود Albion Insight وجود دارد.

لطفاً [دستورالعمل‌های مشارکت](CONTRIBUTING.md) ما را برای اطلاعات دقیق در مورد نحوه مشارکت در این پروژه بخوانید.

### شروع سریع برای مشارکت‌کنندگان:

1.  فورک کردن مخزن: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  کلون کردن فورک خود: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  ایجاد یک شاخه جدید: `git checkout -b feature/your-feature-name`
4.  اعمال تغییرات و کامیت: `git commit -m "Add your feature"`
5.  پوش به فورک خود: `git push origin feature/your-feature-name`
6.  باز کردن یک Pull Request در مخزن اصلی

## مجوز

این پروژه تحت مجوز MIT است - برای جزئیات به فایل [LICENSE](LICENSE) مراجعه کنید.

## قدردانی

- پروژه اصلی: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) توسط Triky313
- ساخته شده با فریم‌ورک [Flet](https://flet.dev/)
- تحلیل شبکه توسط [Scapy](https://scapy.net/)

---
*یک راه‌حل چند پلتفرمی برای جامعه Albion Online.*
