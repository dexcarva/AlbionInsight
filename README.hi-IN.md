# एल्बियन इनसाइट (Albion Insight)

[![लाइसेंस: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![पायथन संस्करण](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![प्लेटफ़ॉर्म](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![गिटहब इश्यू](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![योगदान स्वागत है](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**[इसे हिंदी में पढ़ें (Read this in Hindi)](README.hi-IN.md)**
**[Read this in German (Lesen Sie dies auf Deutsch)](README.de-DE.md)**
**[Read this in Portuguese (Leia em Português)](README.pt-BR.md)**
**[Read this in Spanish (Leer en Español)](README.es-ES.md)**
**[Read this in French (Lire en Français)](README.fr-FR.md)**
**[Read this in Italian (Leggi in Italiano)](README.it-IT.md)**
**[Read this in Simplified Chinese (阅读简体中文)](README.zh-CN.md)**
**[Read this in Russian (Прочитать на русском)](README.ru-RU.md)**
**[Read this in Japanese (日本語で読む)](README.ja-JP.md)**
**[Read this in Arabic (اقرأ هذا بالعربية)](README.ar-SA.md)**
**[Read this in Turkish (Türkçe Oku)](README.tr-TR.md)**
**[Read this in Korean (한국어로 읽기)](README.ko-KR.md)**
**[Read this in Dutch (Lees dit in het Nederlands)](README.nl-NL.md)**
**[Read this in Polish (Czytaj po polsku)](README.pl-PL.md)**

**एल्बियन इनसाइट** एल्बियन ऑनलाइन के लिए एक क्रॉस-प्लेटफ़ॉर्म (लिनक्स, विंडोज, मैकओएस) सांख्यिकी विश्लेषण उपकरण है, जिसे **फलेट (Flet)** फ्रेमवर्क का उपयोग करके **पायथन** में फिर से लागू किया गया है। इसे नेटवर्क ट्रैफ़िक का विश्लेषण करके सिल्वर, फेम और कॉम्बैट डेटा (डैमेज मीटर) सहित वास्तविक समय के इन-गेम आँकड़ों को ट्रैक करने के लिए डिज़ाइन किया गया है।

यह परियोजना मूल C#/WPF-आधारित `AlbionOnline-StatisticsAnalysis` उपकरण का एक आधुनिक, ओपन-सोर्स विकल्प है, जो मल्टी-प्लेटफ़ॉर्म संगतता और उपयोग में आसानी पर केंद्रित है।

## मुख्य विशेषताएं

*   **क्रॉस-प्लेटफ़ॉर्म संगतता:** लिनक्स, विंडोज और मैकओएस पर चलता है।
*   **वास्तविक समय ट्रैकिंग:** एल्बियन ऑनलाइन पोर्ट्स (5055, 5056, 5058) पर UDP पैकेट को स्निफ़ करने के लिए `Scapy` लाइब्रेरी का उपयोग करता है।
*   **डैमेज मीटर संरचना:** लाइव कॉम्बैट आँकड़े (किया गया डैमेज, किया गया हीलिंग, DPS) प्रदर्शित करने के लिए आवश्यक डेटा संरचनाएँ और UI शामिल हैं।
*   **आधुनिक UI:** फलेट के साथ बनाया गया, जो एक तेज़, देशी दिखने वाला डेस्कटॉप एप्लिकेशन प्रदान करता है।
*   **सत्र प्रबंधन:** सत्र के आँकड़ों को शुरू करने, रोकने, रीसेट करने और सहेजने की अनुमति देता है।

## आवश्यक शर्तें

*   पायथन 3.8+
*   **फलेट (Flet)** और **स्कैपी (Scapy)** लाइब्रेरी।
*   **रूट/एडमिनिस्ट्रेटर विशेषाधिकार:** नेटवर्क पैकेट कैप्चर के लिए आवश्यक।

## इंस्टॉलेशन और सेटअप

### विकल्प 1: त्वरित इंस्टॉलेशन (लिनक्स - अनुशंसित)

लिनक्स उपयोगकर्ताओं के लिए, हम स्वचालित इंस्टॉलेशन स्क्रिप्ट प्रदान करते हैं:

```bash
# 1. रिपॉजिटरी को क्लोन करें
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. इंस्टॉलेशन स्क्रिप्ट चलाएँ
./install.sh

# 3. एप्लिकेशन चलाएँ
./run.sh
```

`install.sh` स्क्रिप्ट निम्नलिखित कार्य करेगी:
- सिस्टम निर्भरताएँ स्थापित करें (`libpcap-dev`, `python3-pip`, `python3-venv`)
- एक पायथन वर्चुअल वातावरण बनाएँ
- सभी आवश्यक पायथन पैकेज (फलेट, स्कैपी) स्थापित करें

`run.sh` स्क्रिप्ट स्वचालित रूप से रूट विशेषाधिकारों का अनुरोध करेगी और एप्लिकेशन चलाएगी।

### विकल्प 2: मैन्युअल इंस्टॉलेशन

#### 1. सिस्टम निर्भरताएँ स्थापित करें

**लिनक्स पर (डेबियन/उबंटू):**

```bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
```
**विंडोज पर:**

[python.org](https://www.python.org/downloads/) से पायथन 3.8+ स्थापित करें

#### 2. पायथन निर्भरताएँ स्थापित करें

**लिनक्स पर (वर्चुअल वातावरण का उपयोग करके - अनुशंसित):**

```bash
# वर्चुअल वातावरण बनाएँ
python3 -m venv venv

# वर्चुअल वातावरण सक्रिय करें
source venv/bin/activate

# निर्भरताएँ स्थापित करें
pip install flet scapy
```
**लिनक्स पर (सिस्टम-व्यापी इंस्टॉलेशन):**

```bash
pip3 install flet scapy --break-system-packages
```
**विंडोज पर:**

```bash
pip install flet scapy
```

#### 3. एप्लिकेशन चलाना

चूंकि नेटवर्क स्निफ़िंग के लिए उच्च विशेषाधिकारों की आवश्यकता होती है, आपको एप्लिकेशन को रूट या एडमिनिस्ट्रेटर के रूप में चलाना होगा।

**लिनक्स पर (वर्चुअल वातावरण के साथ):**

```bash
sudo venv/bin/python3 albion_insight/main.py
```
**लिनक्स पर (सिस्टम-व्यापी इंस्टॉलेशन):**

```bash
sudo python3 albion_insight/main.py
```
**विंडोज पर (कमांड प्रॉम्प्ट/पावरशेल को एडमिनिस्ट्रेटर के रूप में चलाएँ):**

```bash
python albion_insight/main.py
```
एप्लिकेशन एक देशी डेस्कटॉप विंडो में खुलेगा।

## एक निष्पादन योग्य (Executable) कैसे बनाएँ

एप्लिकेशन को **PyInstaller** का उपयोग करके एक स्टैंडअलोन निष्पादन योग्य में पैक किया जा सकता है। यह उपयोगकर्ताओं को पायथन या उसकी निर्भरताओं को स्थापित किए बिना एप्लिकेशन चलाने की अनुमति देता है।

लिनक्स, विंडोज और मैकओएस के लिए निष्पादन योग्य बनाने के विस्तृत निर्देशों के लिए, **[PACKAGING.md](PACKAGING.md)** गाइड देखें।

### त्वरित निर्माण (लिनक्स)

```bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
```
निष्पादन योग्य `dist/` फ़ोल्डर में स्थित होगा।

## परियोजना संरचना

सरलता के लिए संपूर्ण एप्लिकेशन एक ही फ़ाइल के भीतर समाहित है:

| फ़ाइल | विवरण |
| :--- | :--- |
| `albion_insight/main.py` | मुख्य एप्लिकेशन फ़ाइल जिसमें सभी तर्क (मॉडल, नेटवर्क ट्रैकर, फलेट UI) शामिल हैं। |
| `README.md` | यह दस्तावेज़ीकरण फ़ाइल। |
| `README.hi-IN.md` | यह दस्तावेज़ीकरण फ़ाइल हिंदी में। |
| `CONTRIBUTING.md` | परियोजना में योगदान के लिए दिशानिर्देश। |
| `CODE_OF_CONDUCT.md` | परियोजना का आचार संहिता। |
| `SECURITY.md` | सुरक्षा कमजोरियों की रिपोर्टिंग के लिए नीति। |

## वर्तमान स्थिति (वास्तविक समय डेटा)

एप्लिकेशन में अब **फोटॉन प्रोटोकॉल डिकोडिंग** तर्क शामिल है, जिसे मूल C# प्रोजेक्ट से अनुवादित किया गया है। यह एप्लिकेशन को नेटवर्क ट्रैफ़िक से सीधे `UpdateMoney`, `UpdateFame`, `KilledPlayer`, और `Died` जैसे वास्तविक समय की घटनाओं को संसाधित करने की अनुमति देता है।

**ध्यान दें:** प्रत्येक एकल युद्ध घटना (जैसे `CastHit`, `Attack`) का पूर्ण अनुवाद एक सतत प्रयास है। वर्तमान कार्यान्वयन मुख्य आँकड़ों और डैमेज मीटर की संरचना पर केंद्रित है। डैमेज मीटर की डीपीएस गणना डिकोड की गई घटनाओं पर आधारित है।

## योगदान

हम समुदाय से योगदान का स्वागत करते हैं! चाहे आप एक डेवलपर हों, डिज़ाइनर हों, या सिर्फ एक एल्बियन ऑनलाइन उत्साही हों, एल्बियन इनसाइट को बेहतर बनाने में मदद करने के कई तरीके हैं।

परियोजना में योगदान करने के तरीके पर विस्तृत जानकारी के लिए कृपया हमारे [योगदान दिशानिर्देश](CONTRIBUTING.md) पढ़ें।

### योगदानकर्ताओं के लिए त्वरित शुरुआत:

1.  रिपॉजिटरी को फोर्क करें: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  अपने फोर्क को क्लोन करें: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  एक नई शाखा बनाएँ: `git checkout -b feature/your-feature-name`
4.  अपने बदलाव करें और कमिट करें: `git commit -m "अपनी सुविधा जोड़ें"`
5.  अपने फोर्क पर पुश करें: `git push origin feature/your-feature-name`
6.  मुख्य रिपॉजिटरी पर एक पुल रिक्वेस्ट खोलें

## लाइसेंस

यह परियोजना एमआईटी लाइसेंस के तहत लाइसेंस प्राप्त है - विवरण के लिए [LICENSE](LICENSE) फ़ाइल देखें।

## आभार

- मूल परियोजना: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) Triky313 द्वारा
- [फलेट (Flet)](https://flet.dev/) फ्रेमवर्क के साथ बनाया गया
- [स्कैपी (Scapy)](https://scapy.net/) द्वारा संचालित नेटवर्क विश्लेषण

---
*एल्बियन ऑनलाइन समुदाय के लिए एक क्रॉस-प्लेटफ़ॉर्म समाधान।*
