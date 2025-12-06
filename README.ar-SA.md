# نظرة ألبيون (Albion Insight)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**نظرة ألبيون (Albion Insight)** هي أداة تحليل إحصائيات متعددة المنصات (Linux، Windows، macOS) للعبة Albion Online، أعيد تنفيذها بلغة **بايثون (Python)** باستخدام إطار عمل **فليت (Flet)**. تم تصميمها لتتبع الإحصائيات داخل اللعبة في الوقت الفعلي، بما في ذلك الفضة والشهرة وبيانات القتال (مقياس الضرر)، عن طريق تحليل حركة مرور الشبكة.

هذا المشروع هو بديل حديث ومفتوح المصدر لأداة `AlbionOnline-StatisticsAnalysis` الأصلية المعتمدة على C#/WPF، مع التركيز على التوافق متعدد المنصات وسهولة الاستخدام.

## الميزات (Features)

*   **التوافق متعدد المنصات:** يعمل أصلاً على أنظمة Linux و Windows و macOS.
*   **التتبع في الوقت الفعلي:** يستخدم مكتبة `Scapy` لالتقاط حزم UDP على منافذ Albion Online (5055، 5056، 5058).
*   **هيكل مقياس الضرر:** يتضمن هياكل البيانات وواجهة المستخدم الضرورية لعرض إحصائيات القتال الحية (الضرر الذي تم إحداثه، الشفاء الذي تم تقديمه، الضرر في الثانية).
*   **واجهة مستخدم حديثة:** تم بناؤها باستخدام Flet، مما يوفر تطبيق سطح مكتب سريعًا وذا مظهر أصلي.
*   **إدارة الجلسات:** يسمح ببدء وإيقاف وإعادة تعيين وحفظ إحصائيات الجلسة.

## المتطلبات الأساسية (Prerequisites)

*   بايثون (Python) 3.8+
*   مكتبات **Flet** و **Scapy**.
*   **امتيازات الجذر/المسؤول:** ضرورية لالتقاط حزم الشبكة.

## التثبيت والإعداد (Installation and Setup)

### الخيار 1: التثبيت السريع (Linux - موصى به)

لمستخدمي Linux، نقدم نصوص تثبيت آلية:

\`\`\`bash
# 1. استنساخ المستودع
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. تشغيل نص التثبيت
./install.sh

# 3. تشغيل التطبيق
./run.sh
\`\`\`

سيقوم نص `install.sh` بما يلي:

*   تثبيت تبعيات النظام (`libpcap-dev`، `python3-pip`، `python3-venv`)
*   إنشاء بيئة بايثون افتراضية
*   تثبيت جميع حزم بايثون المطلوبة (Flet، Scapy)

سيطلب نص `run.sh` تلقائيًا امتيازات الجذر ويشغل التطبيق.

### الخيار 2: التثبيت اليدوي (Manual Installation)

#### 1. تثبيت تبعيات النظام

**على Linux (Debian/Ubuntu):**

\`\`\`bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
\`\`\`

**على Windows:**

قم بتثبيت بايثون 3.8+ من [python.org](https://www.python.org/downloads/)

#### 2. تثبيت تبعيات بايثون

**على Linux (باستخدام بيئة افتراضية - موصى به):**

\`\`\`bash
# إنشاء بيئة افتراضية
python3 -m venv venv

# تفعيل البيئة الافتراضية
source venv/bin/activate

# تثبيت التبعيات
pip install flet scapy
\`\`\`

**على Linux (تثبيت على مستوى النظام):**

\`\`\`bash
pip3 install flet scapy --break-system-packages
\`\`\`

**على Windows:**

\`\`\`bash
pip install flet scapy
\`\`\`

#### 3. تشغيل التطبيق

نظرًا لأن التقاط حزم الشبكة يتطلب امتيازات مرتفعة، يجب تشغيل التطبيق بصفة جذر (root) أو مسؤول (administrator).

**على Linux (مع بيئة افتراضية):**

\`\`\`bash
sudo venv/bin/python3 -m albion_insight
\`\`\`

**على Linux (تثبيت على مستوى النظام):**

\`\`\`bash
sudo python3 -m albion_insight
\`\`\`

**على Windows (تشغيل موجه الأوامر/PowerShell كمسؤول):**

\`\`\`bash
python -m albion_insight
\`\`\`

سيتم فتح التطبيق في نافذة سطح مكتب أصلية.

## كيفية بناء ملف تنفيذي (How to Build an Executable)

يمكن تجميع التطبيق في ملف تنفيذي مستقل باستخدام **PyInstaller**. يتيح ذلك للمستخدمين تشغيل التطبيق دون تثبيت بايثون أو تبعياته.

للحصول على تعليمات مفصلة حول بناء الملفات التنفيذية لأنظمة Linux و Windows و macOS، راجع دليل **[PACKAGING.md](PACKAGING.md)**.

### بناء سريع (Linux)

\`\`\`bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
\`\`\`

سيكون الملف التنفيذي موجودًا في مجلد `dist/`.

## هيكل المشروع (Project Structure)

تم تنظيم التطبيق في مكونات معيارية لتحسين قابلية الصيانة وقابلية التوسع:

| الملف | الوصف |
| :--- | :--- |
| `albion_insight/core/` | المنطق الأساسي، تتبع الشبكة، نماذج البيانات، وفك تشفير البروتوكول. |
| `albion_insight/ui/` | مكونات واجهة المستخدم المبنية باستخدام Flet. |
| `albion_insight/utils/` | وظائف مساعدة، إعدادات، وتسجيل. |
| `albion_insight/__main__.py` | نقطة الدخول للتطبيق. |
| `README.md` | ملف التوثيق هذا. |
| `CONTRIBUTING.md` | إرشادات للمساهمة في المشروع. |
| `CODE_OF_CONDUCT.md` | مدونة قواعد السلوك للمشروع. |
| `SECURITY.md` | سياسة الإبلاغ عن الثغرات الأمنية. |
| `README.ar-SA.md` | توثيق باللغة العربية (Arabic documentation). |
| `README.it-IT.md` | Documentazione in italiano. |
| `README.pt-BR.md` | Documentação em português do Brasil. |
| `README.ru-RU.md` | Документация на русском языке. |
| `README.fr-FR.md` | Documentation en français. |
| `README.pl-PL.md` | Dokumentacja w języku polskim (Polish documentation). |
| `README.sv-SE.md` | Dokumentation på svenska (Swedish documentation). |
| `README.vi-VN.md` | Tài liệu bằng tiếng Việt (Vietnamese documentation). |
| `README.pt-PT.md` | Documentação em português europeu. |

## الحالة الحالية (بيانات الوقت الفعلي) (Current Status - Real-Time Data)

يتضمن التطبيق الآن منطق **فك تشفير بروتوكول فوتون (Photon Protocol Decoding)**، المترجم من مشروع C# الأصلي. يتيح ذلك للتطبيق معالجة الأحداث في الوقت الفعلي مثل `UpdateMoney` و `UpdateFame` و `KilledPlayer` و `Died` مباشرة من حركة مرور الشبكة.

**ملاحظة:** الترجمة الكاملة لكل حدث قتالي (مثل `CastHit`، `Attack`) هي جهد مستمر. يركز التنفيذ الحالي على الإحصائيات الأساسية وهيكل مقياس الضرر. يعتمد حساب الضرر في الثانية (DPS) لمقياس الضرر على الأحداث المفككة.

## المساهمة (Contributing)

نرحب بالمساهمات من المجتمع! سواء كنت مطورًا أو مصممًا أو مجرد متحمس للعبة Albion Online، هناك العديد من الطرق للمساعدة في تحسين Albion Insight.

يرجى قراءة [إرشادات المساهمة](CONTRIBUTING.md) للحصول على معلومات مفصلة حول كيفية المساهمة في هذا المشروع.

### بداية سريعة للمساهمين:

1.  تفرع المستودع (Fork the repository): [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  استنسخ تفرعك (Clone your fork): `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  أنشئ فرعًا جديدًا (Create a new branch): `git checkout -b feature/your-feature-name`
4.  قم بإجراء تغييراتك والتزامها (Make your changes and commit): `git commit -m "Add your feature"`
5.  ادفع إلى تفرعك (Push to your fork): `git push origin feature/your-feature-name`
6.  افتح طلب سحب (Pull Request) على المستودع الرئيسي

## الترخيص (License)

هذا المشروع مرخص بموجب ترخيص MIT - انظر ملف [LICENSE](LICENSE) للحصول على التفاصيل.

## شكر وتقدير (Acknowledgments)

*   المشروع الأصلي: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) بواسطة Triky313
*   تم البناء باستخدام إطار عمل [Flet](https://flet.dev/)
*   تحليل الشبكة مدعوم بواسطة [Scapy](https://scapy.net/)

---
*حل متعدد المنصات لمجتمع Albion Online.*
