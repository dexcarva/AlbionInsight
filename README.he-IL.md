# Albion Insight (עברית)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

<details>
<summary>קראו זאת בשפות אחרות</summary>

**[Arabic](README.ar-SA.md)** | **[German](README.de-DE.md)** | **[Greek](README.el-GR.md)** | **[Spanish](README.es-ES.md)** | **[French](README.fr-FR.md)** | **[Hindi](README.hi-IN.md)** | **[Hungarian](README.hu-HU.md)** | **[Indonesian](README.id-ID.md)** | **[Italian](README.it-IT.md)** | **[Japanese](README.ja-JP.md)** | **[Korean](README.ko-KR.md)** | **[Dutch](README.nl-NL.md)** | **[Polish](README.pl-PL.md)** | **[Portuguese (Brazil)](README.pt-BR.md)** | **[Romanian](README.ro-RO.md)** | **[Russian](README.ru-RU.md)** | **[Swedish](README.sv-SE.md)** | **[Thai](README.th-TH.md)** | **[Turkish](README.tr-TR.md)** | **[Vietnamese](README.vi-VN.md)** | **[Chinese (Simplified)](README.zh-CN.md)** | **[Chinese (Traditional)](README.zh-TW.md)** | **[Chinese (Traditional - Hong Kong)](README.zh-HK.md)** | **[Czech](README.cs-CZ.md)** | **[Persian (Farsi)](README.fa-IR.md)** | **[Filipino (Tagalog)](README.fil-PH.md)** | **[Português (Portugal)](README.pt-PT.md)** | **[Hebrew](README.he-IL.md)**

</details>

**Albion Insight** הוא כלי חוצה-פלטפורמות (לינוקס, ווינדוס, macOS) לניתוח סטטיסטיקות עבור המשחק Albion Online, אשר יושם מחדש ב-**Python** באמצעות ספריית **Flet**. הוא נועד לעקוב אחר סטטיסטיקות בזמן אמת במשחק, כולל כסף (silver), מוניטין (fame), ונתוני קרב (מד נזק), על ידי ניתוח תעבורת הרשת.

פרויקט זה הוא אלטרנטיבה מודרנית וקוד פתוח לכלי המקורי `AlbionOnline-StatisticsAnalysis` מבוסס C#/WPF, המתמקד בתאימות מרובת-פלטפורמות וקלות שימוש.

## תכונות

*   **תאימות חוצה-פלטפורמות:** פועל באופן טבעי בלינוקס, ווינדוס, ו-macOS.
*   **מעקב בזמן אמת:** משתמש בספריית `Scapy` כדי לרחרח חבילות UDP בפורטים של Albion Online (5055, 5056, 5058).
*   **מבנה מד נזק:** כולל את מבני הנתונים וממשק המשתמש הדרושים להצגת סטטיסטיקות קרב חיות (נזק שנגרם, ריפוי שבוצע, DPS).
*   **ממשק משתמש מודרני:** נבנה עם Flet, ומספק יישום שולחני מהיר ונראה טבעי.
*   **ניהול סשנים:** מאפשר התחלה, עצירה, איפוס, ושמירת סטטיסטיקות סשן.

## דרישות קדם

*   Python 3.8+
*   ספריות **Flet** ו-**Scapy**.
*   **הרשאות מנהל/שורש:** נחוצות ללכידת חבילות רשת.

## התקנה והגדרה

### אפשרות 1: התקנה מהירה (לינוקס - מומלץ)

למשתמשי לינוקס, אנו מספקים סקריפטים להתקנה אוטומטית:

```bash
# 1. שכפול המאגר
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. הפעלת סקריפט ההתקנה
./install.sh

# 3. הפעלת היישום
./run.sh
```

### אפשרות 2: התקנה ידנית (כל הפלטפורמות)

```bash
# 1. שכפול המאגר
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. התקנת דרישות
pip install -r requirements.txt

# 3. הפעלת היישום
python3 -m albion_insight
```

## תרומה לפרויקט

אנו מקדמים בברכה תרומות! אנא קראו את [CONTRIBUTING.md](CONTRIBUTING.md) לקבלת הנחיות.

## רישיון

פרויקט זה מורשה תחת רישיון MIT. ראו את הקובץ [LICENSE](LICENSE) לפרטים נוספים.
