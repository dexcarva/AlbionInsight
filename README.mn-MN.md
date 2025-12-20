[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Albion Insight** нь Albion Online тоглоомын статистикийн шинжилгээний олон платформ (Linux, Windows, macOS) хэрэгсэл бөгөөд **Flet** фреймворкийг ашиглан **Python** хэл дээр дахин хэрэгжүүлсэн. Энэ нь сүлжээний траффикийг шинжлэх замаар тоглоомын бодит цагийн статистик, тухайлбал мөнгө, алдар нэр, тулааны мэдээлэл (Damage Meter) зэргийг хянах зорилготой юм.

Энэхүү төсөл нь анхны C#/WPF-д суурилсан `AlbionOnline-StatisticsAnalysis` хэрэгслийн орчин үеийн, нээлттэй эхийн хувилбар бөгөөд олон платформын нийцтэй байдал, хэрэглэхэд хялбар байдалд анхаарлаа хандуулсан.

## Онцлогууд

*   **Олон Платформын Нийцтэй Байдал:** Linux, Windows, macOS үйлдлийн системүүд дээр уугуул байдлаар ажиллана.
*   **Бодит Цагийн Хяналт:** `Scapy` номын санг ашиглан Albion Online-ийн портууд (5055, 5056, 5058) дээрх UDP пакетуудыг хянана.
*   **Хохирлын Хэмжигчийн Бүтэц (Damage Meter Structure):** Бодит цагийн тулааны статистик (Үзүүлсэн Хохирол, Эмчилгээ, DPS) -ийг харуулах шаардлагатай өгөгдлийн бүтэц, хэрэглэгчийн интерфэйсийг агуулна.
*   **Орчин Үеийн Хэрэглэгчийн Интерфэйс:** Flet-ээр бүтээгдсэн, хурдан, уугуул харагдацтай ширээний програмыг хангана.
*   **Сессийн Удирдлага:** Сессийн статистикийг эхлүүлэх, зогсоох, дахин тохируулах, хадгалах боломжийг олгоно.

## Урьдчилсан Нөхцөл

*   Python 3.8+
*   **Flet** болон **Scapy** номын сангууд.
*   **Root/Администраторын Эрх:** Сүлжээний пакет барихын тулд зайлшгүй шаардлагатай.

## Суулгалт ба Тохиргоо

### Сонголт 1: Түргэн Суулгалт (Linux - Зөвлөмж)

Linux хэрэглэгчдэд зориулж автоматжуулсан суулгах скриптүүдийг санал болгож байна:

\`\`\`bash
# 1. Репозиторийг татаж авах
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Суулгах скриптийг ажиллуулах
./install.sh

# 3. Аппликейшнийг ажиллуулах
./run.sh
\`\`\`

`install.sh` скрипт нь:
- Системийн хамаарлуудыг суулгана (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Python-ийн виртуал орчинг үүсгэнэ
- Шаардлагатай бүх Python багцуудыг суулгана (Flet, Scapy)

`run.sh` скрипт нь автоматаар root эрхийг шаардаж, аппликейшнийг ажиллуулна.

### Сонголт 2: Гараар Суулгах

#### 1. Системийн Хамаарлуудыг Суулгах

**Linux дээр (Debian/Ubuntu):**

\`\`\`bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
\`\`\`

**Windows дээр:**

Python 3.8+ -ийг [python.org](https://www.python.org/downloads/) -оос суулгана уу.

#### 2. Python-ийн Хамаарлуудыг Суулгах

**Linux дээр (виртуал орчин ашиглах - зөвлөмж):**

\`\`\`bash
# Виртуал орчин үүсгэх
python3 -m venv venv

# Виртуал орчинг идэвхжүүлэх
source venv/bin/activate

# Хамаарлуудыг суулгах
pip install flet scapy
\`\`\`

**Linux дээр (систем даяар суулгах):**

\`\`\`bash
pip3 install flet scapy --break-system-packages
\`\`\`

**Windows дээр:**

\`\`\`bash
pip install flet scapy
\`\`\`

#### 3. Аппликейшнийг Ажиллуулах

Сүлжээний хяналт нь өндөрлөгсөн эрхийг шаарддаг тул та аппликейшнийг root эсвэл администратороор ажиллуулах ёстой.

**Linux дээр (виртуал орчинтой):**

\`\`\`bash
sudo venv/bin/python3 -m albion_insight
\`\`\`

**Linux дээр (систем даяар суулгасан):**

\`\`\`bash
sudo python3 -m albion_insight
\`\`\`

**Windows дээр (Администратороор Command Prompt/PowerShell-ийг ажиллуулах):**

\`\`\`bash
python -m albion_insight
\`\`\`

Аппликейшн нь уугуул ширээний цонхонд нээгдэнэ.

## Гүйцэтгэх Файл Хэрхэн Үүсгэх

Аппликейшнийг **PyInstaller** ашиглан бие даасан гүйцэтгэх файл болгон багцалж болно. Энэ нь хэрэглэгчдэд Python болон түүний хамаарлуудыг суулгахгүйгээр аппликейшнийг ажиллуулах боломжийг олгоно.

Linux, Windows, macOS-д зориулсан гүйцэтгэх файл үүсгэх дэлгэрэнгүй зааврыг **[PACKAGING.md](PACKAGING.md)** гарын авлагаас үзнэ үү.

### Түргэн Багцлалт (Linux)

\`\`\`bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
\`\`\`

Гүйцэтгэх файл нь `dist/` хавтсанд байрлана.

## Төслийн Бүтэц

Аппликейшн нь илүү сайн засвар үйлчилгээ, өргөтгөх боломжийг хангах үүднээс модульчлагдсан бүрэлдэхүүн хэсгүүдэд хуваагдсан:

| Файл | Тодорхойлолт |
| :--- | :--- |
| `albion_insight/core/` | Үндсэн логик, сүлжээний хяналт, өгөгдлийн загварууд, протоколын декодчилол. |
| `albion_insight/ui/` | Flet-ээр бүтээгдсэн хэрэглэгчийн интерфэйсийн бүрэлдэхүүн хэсгүүд. |
| `albion_insight/utils/` | Туслах функцууд, тохиргоо, бүртгэл. |
| `albion_insight/__main__.py` | Аппликейшний эхлэх цэг. |
| `README.md` | Энэхүү баримт бичиг (Англи). |
| `CONTRIBUTING.md` | Төсөлд хувь нэмэр оруулах удирдамж. |
| `CODE_OF_CONDUCT.md` | Төслийн Ёс зүйн Дүрэм. |
| `SECURITY.md` | Аюулгүй байдлын эмзэг байдлыг мэдээлэх журам. |
| `README.ar-SA.md` | توثيق باللغة العربية (Араб хэлний баримт бичиг). |
| `README.ca-ES.md` | Documentació en català (Каталан хэлний баримт бичиг). |
| `README.cs-CZ.md` | Dokumentace v češtině (Чех хэлний баримт бичиг). |
| `README.da-DK.md` | Dokumentation på dansk (Дани хэлний баримт бичиг). |
| `README.de-DE.md` | Dokumentation in deutscher Sprache (Герман хэлний баримт бичиг). |
| `README.el-GR.md` | Τεκμηρίωση στα Ελληνικά (Грек хэлний баримт бичиг). |
| `README.es-ES.md` | Documentación en español (Испани хэлний баримт бичиг). |
| `README.fa-IR.md` | مستندات به زبان فارسی (Перс хэлний баримт бичиг). |
| `README.fi-FI.md` | Dokumentaatio suomeksi (Финлянд хэлний баримт бичиг). |
| `README.fi.md` | Dokumentaatio suomeksi (Финлянд хэлний баримт бичиг - Ерөнхий). |
| `README.fil-PH.md` | Dokumentasyon sa Filipino (Филиппин хэлний баримт бичиг). |
| `README.fr-FR.md` | Documentation en français (Франц хэлний баримт бичиг). |
| `README.he-IL.md` | תיעוד בעברית (Еврей хэлний баримт бичиг). |
| `README.hi-IN.md` | Hindi में दस्तावेज़ीकरण (Хинди хэлний баримт бичиг). |
| `README.hu-HU.md` | Dokumentáció magyar nyelven (Унгар хэлний баримт бичиг). |
| `README.id-ID.md` | Dokumentasi dalam Bahasa Indonesia (Индонез хэлний баримт бичиг). |
| `README.it-IT.md` | Documentazione in italiano (Итали хэлний баримт бичиг). |
| `README.ja-JP.md` | 日本語のドキュメント (Япон хэлний баримт бичиг). |
| `README.ko-KR.md` | 한국어 문서 (Солонгос хэлний баримт бичиг). |
| `README.lt-LT.md` | Dokumentacija lietuvių kalba (Литва хэлний баримт бичиг). |
| `README.lv-LV.md` | Dokumentācija latviešu valodā (Латви хэлний баримт бичиг). |
| `README.ne-NP.md` | नेपालीमा कागजात (Непал хэлний баримт бичиг). |
| `README.nl-NL.md` | Documentatie in het Nederlands (Голланд хэлний баримт бичиг). |
| `README.no-NO.md` | Dokumentasjon på norsk (Норвеги хэлний баримт бичиг). |
| `README.pl-PL.md` | Dokumentacja w języku polskim (Польш хэлний баримт бичиг). |
| `README.pt-BR.md` | Documentação em português do Brasil (Бразилийн Португал хэлний баримт бичиг). |
| `README.pt-PT.md` | Documentação em português europeu (Европын Португал хэлний баримт бичиг). |
| `README.ro-RO.md` | Documentație în română (Румын хэлний баримт бичиг). |
| `README.ru-RU.md` | Документация на русском языке (Орос хэлний баримт бичиг). |
| `README.sk-SK.md` | Dokumentácia v slovenčine (Словак хэлний баримт бичиг). |
| `README.sv-SE.md` | Dokumentation på svenska (Швед хэлний баримт бичиг). |
| `README.th-TH.md` | เอกสารประกอบภาษาไทย (Тай хэлний баримт бичиг). |
| `README.tr-TR.md` | Türkçe dokümantasyon (Турк хэлний баримт бичиг). |
| `README.uk-UA.md` | Документація українською мовою (Украин хэлний баримт бичиг). |
| `README.vi-VN.md` | Tài liệu bằng tiếng Việt (Вьетнам хэлний баримт бичиг). |
| `README.zh-CN.md` | 简体中文文档 (Хялбаршуулсан Хятад хэлний баримт бичиг). |
| `README.zh-TW.md` | 繁體中文文件 (Уламжлалт Хятад хэлний баримт бичиг). |
| `README.gl-ES.md` | Documentación en galego (Галиси хэлний баримт бичиг). |
| `README.et-EE.md` | Dokumentatsioon eesti keeles (Эстони хэлний баримт бичиг). |
| `README.zu-ZA.md` | Imibhalo ngolimi lwesiZulu (Зулу хэлний баримт бичиг). |

## Актуал Төлөв (Бодит Цагийн Өгөгдөл)

Аппликейшн нь одоо анхны C# төслөөс орчуулсан **Photon Протоколын Декодчилол**-ын логикийг агуулж байна. Энэ нь аппликейшнд `UpdateMoney`, `UpdateFame`, `KilledPlayer`, `Died` зэрэг бодит цагийн үйл явдлуудыг сүлжээний траффикаас шууд боловсруулах боломжийг олгодог.

**Тэмдэглэл:** Тулааны үйл явдал бүрийг (жишээлбэл, `CastHit`, `Attack`) бүрэн орчуулах ажил үргэлжилж байна. Одоогийн хэрэгжилт нь үндсэн статистик болон Хохирлын Хэмжигчийн бүтцэд анхаарлаа хандуулж байна. Хохирлын Хэмжигчийн DPS тооцоо нь декодлогдсон үйл явдлууд дээр суурилдаг.

## Хувь Нэмэр Оруулах

Бид олон нийтийн хувь нэмрийг таатай хүлээн авч байна! Та хөгжүүлэгч, дизайнер эсвэл зүгээр л Albion Online-ийн сонирхогч байсан ч Albion Insight-ийг сайжруулахад туслах олон арга зам бий.

Энэхүү төсөлд хэрхэн хувь нэмэр оруулах талаар дэлгэрэнгүй мэдээллийг манай [Хувь Нэмэр Оруулах Удирдамж](CONTRIBUTING.md) -аас уншина уу.

### Хувь Нэмэр Оруулагчдад зориулсан Түргэн Эхлэл:

1.  Репозиторийг Fork хийх: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Өөрийн Fork-ийг татаж авах: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  Шинэ салбар үүсгэх: `git checkout -b feature/таны-функцийн-нэр`
4.  Өөрчлөлтөө хийж, commit хийх: `git commit -m "Таны функцийг нэмэх"`
5.  Өөрийн Fork-д түлхэх: `git push origin feature/таны-функцийн-нэр`
6.  Үндсэн репозиторий дээр Pull Request нээх

## Лиценз

Энэхүү төсөл нь MIT Лицензийн дор лицензлэгдсэн - дэлгэрэнгүй мэдээллийг [LICENSE](LICENSE) файлаас үзнэ үү.

## Талархал

- Анхны төсөл: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) by Triky313
- [Flet](https://flet.dev/) фреймворкоор бүтээгдсэн
- Сүлжээний шинжилгээг [Scapy](https://scapy.net/) -аар хийсэн

---
*Albion Online нийгэмлэгт зориулсан олон платформын шийдэл.*
