# Albion Insight

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

<details>
<summary>Бусад хэлээр унших</summary>

**[Arabic](README.ar-SA.md)** | **[German](README.de-DE.md)** | **[Greek](README.el-GR.md)** | **[Spanish](README.es-ES.md)** | **[French](README.fr-FR.md)** | **[Hindi](README.hi-IN.md)** | **[Hungarian](README.hu-HU.md)** | **[Indonesian](README.id-ID.md)** | **[Italian](README.it-IT.md)** | **[Japanese](README.ja-JP.md)** | **[Korean](README.ko-KR.md)** | **[Dutch](README.nl-NL.md)** | **[Polish](README.pl-PL.md)** | **[Portuguese (Brazil)](README.pt-BR.md)** | **[Romanian](README.ro-RO.md)** | **[Russian](README.ru-RU.md)** | **[Swedish](README.sv-SE.md)** | **[Thai](README.th-TH.md)** | **[Turkish](README.tr-TR.md)** | **[Vietnamese](README.vi-VN.md)** | **[Chinese (Simplified)](README.zh-CN.md)** | **[Chinese (Traditional)](README.zh-TW.md)** | **[Chinese (Traditional - Hong Kong)](README.zh-HK.md)** | **[Czech](README.cs-CZ.md)** | **[Persian (Farsi)](README.fa-IR.md)** | **[Filipino (Tagalog)](README.fil-PH.md)** | **[Português (Portugal)](README.pt-PT.md)** | **[Hebrew](README.he-IL.md)** | **[Norwegian](README.no-NO.md)** | **[Finnish](README.fi-FI.md)** | **[Polish](README.pl-PL.md)** | **[Danish](README.da-DK.md)** | **[Ukrainian](README.uk-UA.md)** | **[Malay](README.ms-MY.md)** | **[Estonian](README.et-EE.md)** | **[Mongolian](README.mn-MN.md)**

</details>

**Albion Insight** нь Albion Online тоглоомын статистикийн шинжилгээний хэрэгсэл бөгөөд **Python** хэлээр **Flet** фреймворкийг ашиглан дахин хэрэгжүүлсэн, платформ хоорондын (Linux, Windows, macOS) дэмжлэгтэй. Энэ нь сүлжээний траффикийг шинжлэх замаар тоглоом доторх бодит цагийн статистик, тухайлбал мөнгө, алдар нэр, тулааны мэдээлэл (Damage Meter) зэргийг хянах зорилготой юм.

Энэхүү төсөл нь анхны C#/WPF-д суурилсан `AlbionOnline-StatisticsAnalysis` хэрэгслийн орчин үеийн, нээлттэй эхийн хувилбар бөгөөд олон платформд нийцтэй байдал, хэрэглэхэд хялбар байдалд анхаарлаа хандуулсан.

## Онцлогууд (Features)

*   **Платформ хоорондын нийцтэй байдал:** Linux, Windows, macOS үйлдлийн системүүд дээр ажиллана.
*   **Бодит цагийн хяналт:** `Scapy` санг ашиглан Albion Online-ийн портууд (5055, 5056, 5058) дээрх UDP пакетуудыг хянана.
*   **Damage Meter-ийн бүтэц:** Бодит цагийн тулааны статистик (Үзүүлсэн хохирол, Эмчилгээ, DPS) харуулах шаардлагатай өгөгдлийн бүтэц, хэрэглэгчийн интерфэйсийг агуулна.
*   **Орчин үеийн UI:** Flet-ээр бүтээгдсэн бөгөөд хурдан, native-тэй төстэй ширээний програмыг хангана.
*   **Сессийн удирдлага:** Сессийн статистикийг эхлүүлэх, зогсоох, дахин тохируулах, хадгалах боломжийг олгоно.

## Урьдчилсан нөхцөл (Prerequisites)

*   Python 3.8+
*   **Flet** болон **Scapy** сангууд.
*   **Root/Администраторын эрх:** Сүлжээний пакет барихын тулд шаардлагатай.

## Суулгах ба Тохируулах (Installation and Setup)

### Сонголт 1: Хурдан Суулгалт (Linux - Зөвлөмж)

Linux хэрэглэгчдэд зориулсан автомат суулгах скриптүүд:

```bash
# 1. Репозиторийг татаж авах
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Суулгах скриптийг ажиллуулах
./install.sh

# 3. Програмыг ажиллуулах
./run.sh
```

`install.sh` скрипт нь:
- Системийн хамаарлуудыг суулгана (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Python-ийн виртуал орчинг үүсгэнэ
- Шаардлагатай бүх Python сангуудыг суулгана (Flet, Scapy)

`run.sh` скрипт нь root эрхийг автоматаар хүсэж, програмыг ажиллуулна.

### Сонголт 2: Гараар Суулгах (Manual Installation)

#### 1. Системийн Хамаарлуудыг Суулгах

**Linux дээр (Debian/Ubuntu):**

```bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
```

**Windows дээр:**

[python.org](https://www.python.org/downloads/)-с Python 3.8+ суулгана.

#### 2. Python-ийн Хамаарлуудыг Суулгах

**Linux дээр (виртуал орчин ашиглах - зөвлөмж):**

```bash
# Виртуал орчин үүсгэх
python3 -m venv venv

# Виртуал орчинг идэвхжүүлэх
source venv/bin/activate

# Хамаарлуудыг суулгах
pip install flet scapy
```

**Linux дээр (систем даяар суулгах):**

```bash
pip3 install flet scapy --break-system-packages
```

**Windows дээр:**

```bash
pip install flet scapy
```

#### 3. Програмыг Ажиллуулах

Сүлжээний хяналт нь өндөр түвшний эрх шаарддаг тул та програмыг root эсвэл администратороор ажиллуулах ёстой.

**Linux дээр (виртуал орчинтой):**

```bash
sudo venv/bin/python3 -m albion_insight
```

**Linux дээр (систем даяар суулгасан):**

```bash
sudo python3 -m albion_insight
```

**Windows дээр (Command Prompt/PowerShell-ийг Администратороор ажиллуулах):**

```bash
python -m albion_insight
```

Програм нь native desktop цонхонд нээгдэнэ.

## Гүйцэтгэх Файл Үүсгэх (How to Build an Executable)

Програмыг **PyInstaller** ашиглан бие даасан гүйцэтгэх файл болгон багцалж болно. Энэ нь хэрэглэгчдэд Python болон түүний хамаарлуудыг суулгахгүйгээр програмыг ажиллуулах боломжийг олгоно.

Linux, Windows, macOS-д зориулсан гүйцэтгэх файл үүсгэх дэлгэрэнгүй зааврыг **[PACKAGING.md](PACKAGING.md)** гарын авлагаас үзнэ үү.

### Хурдан Багцлалт (Linux)

```bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
```

Гүйцэтгэх файл нь `dist/` хавтаст байрлана.

## Төслийн Бүтэц (Project Structure)

Програм нь засвар үйлчилгээ, өргөтгөх боломжийг сайжруулахын тулд модульчлагдсан бүрэлдэхүүн хэсгүүдэд хуваагдсан:

| Файл | Тодорхойлолт |
| :--- | :--- |
| `albion_insight/core/` | Үндсэн логик, сүлжээний хяналт, өгөгдлийн загварууд, протоколын декодчилол. |
| `albion_insight/ui/` | Flet-ээр бүтээгдсэн хэрэглэгчийн интерфэйсийн бүрэлдэхүүн хэсгүүд. |
| `albion_insight/utils/` | Туслах функцууд, тохиргоо, лог хөтлөлт. |
| `albion_insight/__main__.py` | Програмын эхлэх цэг. |
| `README.md` | Энэхүү баримт бичиг. |
| `README.pt-BR.md` | Энэхүү баримт бичиг Бразил Португал хэлээр. |
| `README.fil-PH.md` | Энэхүү баримт бичиг Филиппин (Тагалог) хэлээр. |
| `README.pt-PT.md` | Энэхүү баримт бичиг Португал (Португал) хэлээр. |
| `README.ko-KR.md` | Энэхүү баримт бичиг Солонгос хэлээр. |
| `README.sv-SE.md` | Энэхүү баримт бичиг Швед хэлээр. |
| `README.da-DK.md` | Энэхүү баримт бичиг Дани хэлээр. |
| `CONTRIBUTING.sv-SE.md` | Швед хэлээр төсөлд хувь нэмэр оруулах удирдамж. |
| `CONTRIBUTING.md` | Төсөлд хувь нэмэр оруулах удирдамж. |
| `CODE_OF_CONDUCT.md` | Төслийн Ёс зүйн дүрэм. |
| `SECURITY.md` | Аюулгүй байдлын эмзэг байдлыг мэдээлэх журам. |
| `README.mn-MN.md` | Энэхүү баримт бичиг Монгол хэлээр. |

## Одоогийн Байдал (Бодит Цагийн Өгөгдөл)

Програм нь анхны C# төслөөс орчуулагдсан **Photon Протоколын Декодчилол**-ын логикийг агуулсан. Энэ нь програмыг сүлжээний траффикаас `UpdateMoney`, `UpdateFame`, `KilledPlayer`, `Died` зэрэг бодит цагийн үйл явдлуудыг шууд боловсруулах боломжийг олгодог.

**Тэмдэглэл:** Тулааны бүх үйл явдлуудыг (жишээлбэл `CastHit`, `Attack`) бүрэн орчуулах ажил үргэлжилж байна. Одоогийн хэрэгжилт нь үндсэн статистик болон Damage Meter-ийн бүтцэд анхаарлаа хандуулсан. Damage Meter-ийн DPS тооцоо нь декодлогдсон үйл явдлууд дээр суурилдаг.

## Хувь Нэмэр Оруулах (Contributing)

Бид олон нийтийн хувь нэмрийг таатай хүлээн авна! Та хөгжүүлэгч, дизайнер эсвэл зүгээр л Albion Online-ийн сонирхогч байсан ч Albion Insight-ийг сайжруулахад туслах олон арга бий.

Энэхүү төсөлд хэрхэн хувь нэмэр оруулах талаар дэлгэрэнгүй мэдээллийг манай [Хувь Нэмэр Оруулах Удирдамж](CONTRIBUTING.md)-аас уншина уу.

### Хувь Нэмэр Оруулагчдад зориулсан Хурдан Эхлэл:

1.  Репозиторийг Fork хийх: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Өөрийн fork-ийг татаж авах: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  Шинэ салбар үүсгэх: `git checkout -b feature/your-feature-name`
4.  Өөрчлөлтөө хийж commit хийх: `git commit -m "Add your feature"`
5.  Өөрийн fork-д түлхэх: `git push origin feature/your-feature-name`
6.  Үндсэн репозиторий дээр Pull Request нээх

## Лиценз (License)

Энэхүү төсөл нь MIT Лицензийн дор лицензлэгдсэн - дэлгэрэнгүй мэдээллийг [LICENSE](LICENSE) файлаас үзнэ үү.

## Талархал (Acknowledgments)

- Анхны төсөл: Triky313-ийн [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis)
- [Flet](https://flet.dev/) фреймворкоор бүтээгдсэн
- Сүлжээний шинжилгээг [Scapy](https://scapy.net/) дэмждэг

---
*Albion Online нийгэмлэгт зориулсан платформ хоорондын шийдэл.*
