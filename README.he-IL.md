# Albion Insight (עברית)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Albion Insight** הוא כלי חוצה-פלטפורמות (Linux, Windows, macOS) לניתוח סטטיסטיקות עבור המשחק Albion Online, המיושם מחדש ב-**Python** באמצעות מסגרת **Flet**. הוא נועד לעקוב אחר סטטיסטיקות בזמן אמת במשחק, כולל כסף (silver), מוניטין (fame), ונתוני קרב (מד נזק), על ידי ניתוח תעבורת רשת.

פרויקט זה הוא אלטרנטיבה מודרנית וקוד פתוח לכלי המקורי מבוסס C#/WPF, `AlbionOnline-StatisticsAnalysis`, המתמקד בתאימות מרובת פלטפורמות ובקלות שימוש.

## תכונות (Features)

*   **תאימות חוצה-פלטפורמות:** פועל באופן טבעי ב-Linux, Windows, ו-macOS.
*   **מעקב בזמן אמת:** משתמש בספריית `Scapy` כדי לרחרח חבילות UDP בפורטים של Albion Online (5055, 5056, 5058).
*   **מבנה מד נזק:** כולל את מבני הנתונים והממשק הדרושים להצגת סטטיסטיקות קרב חיות (נזק שנגרם, ריפוי שנעשה, DPS).
*   **ממשק משתמש מודרני:** נבנה עם Flet, ומספק יישום שולחני מהיר ובעל מראה טבעי.
*   **ניהול סשנים:** מאפשר התחלה, עצירה, איפוס ושמירה של סטטיסטיקות סשן.

## דרישות קדם (Prerequisites)

*   Python 3.8+
*   ספריות **Flet** ו-**Scapy**.
*   **הרשאות Root/מנהל:** נחוץ ללכידת חבילות רשת.

## התקנה והגדרה (Installation and Setup)

למדריך התקנה מפורט, אנא עיין ב-[README.md](README.md) הראשי.

## מבנה הפרויקט (Project Structure)

היישום בנוי לרכיבים מודולריים לתחזוקה וסקיילביליות טובות יותר.

## סטטוס נוכחי (Current Status)

היישום כולל כעת את לוגיקת **פענוח פרוטוקול פוטון** (Photon Protocol Decoding), שתורגמה מהפרויקט המקורי ב-C#.

## תרומה (Contributing)

אנו מקדמים בברכה תרומות מהקהילה! אנא קרא את [הנחיות התרומה](CONTRIBUTING.md) שלנו למידע מפורט.

## רישיון (License)

פרויקט זה מורשה תחת רישיון MIT - ראה את קובץ [LICENSE](LICENSE) לפרטים.

## תודות (Acknowledgments)

*   פרויקט מקורי: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) מאת Triky313
*   נבנה עם מסגרת [Flet](https://flet.dev/)
*   ניתוח רשת מופעל על ידי [Scapy](https://scapy.net/)

---
*פתרון חוצה-פלטפורמות לקהילת Albion Online.*
