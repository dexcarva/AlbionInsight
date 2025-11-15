# Albion Insight

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**[Read this in English (Đọc bằng tiếng Anh)](README.md)**
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
**[Read this in Hindi (इसे हिंदी में पढ़ें)](README.hi-IN.md)**
**[Read this in Swedish (Läs detta på svenska)](README.sv-SE.md)**
**[Read this in Vietnamese (Đọc bằng tiếng Việt)](README.vi-VN.md)**

**Albion Insight** là một công cụ phân tích thống kê đa nền tảng (Linux, Windows, macOS) dành cho trò chơi Albion Online, được triển khai lại bằng **Python** sử dụng framework **Flet**. Nó được thiết kế để theo dõi các thống kê trong trò chơi theo thời gian thực, bao gồm bạc, danh vọng và dữ liệu chiến đấu (Damage Meter), bằng cách phân tích lưu lượng mạng.

Dự án này là một giải pháp thay thế hiện đại, mã nguồn mở cho công cụ `AlbionOnline-StatisticsAnalysis` gốc dựa trên C#/WPF, tập trung vào khả năng tương thích đa nền tảng và dễ sử dụng.

## Tính năng

*   **Tương thích đa nền tảng:** Chạy nguyên bản trên Linux, Windows và macOS.
*   **Theo dõi thời gian thực:** Sử dụng thư viện `Scapy` để theo dõi các gói UDP trên các cổng Albion Online (5055, 5056, 5058).
*   **Cấu trúc Damage Meter:** Bao gồm các cấu trúc dữ liệu và giao diện người dùng cần thiết để hiển thị thống kê chiến đấu trực tiếp (Sát thương gây ra, Hồi máu, DPS).
*   **Giao diện người dùng hiện đại:** Được xây dựng bằng Flet, cung cấp một ứng dụng máy tính để bàn nhanh, trông giống bản địa.
*   **Quản lý phiên:** Cho phép bắt đầu, dừng, đặt lại và lưu thống kê phiên.

## Điều kiện tiên quyết

*   Python 3.8+
*   Các thư viện **Flet** và **Scapy**.
*   **Quyền Root/Quản trị viên:** Cần thiết để chụp gói mạng.

## Cài đặt và Thiết lập

### Tùy chọn 1: Cài đặt nhanh (Linux - Khuyến nghị)

Đối với người dùng Linux, chúng tôi cung cấp các tập lệnh cài đặt tự động:

```bash
# 1. Clone kho lưu trữ
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Chạy tập lệnh cài đặt
./install.sh

# 3. Chạy ứng dụng
./run.sh
```

Tập lệnh `install.sh` sẽ:
- Cài đặt các phụ thuộc hệ thống (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Tạo môi trường ảo Python
- Cài đặt tất cả các gói Python cần thiết (Flet, Scapy)

Tập lệnh `run.sh` sẽ tự động yêu cầu quyền root và chạy ứng dụng.

### Tùy chọn 2: Cài đặt thủ công

#### 1. Cài đặt Phụ thuộc Hệ thống

**Trên Linux (Debian/Ubuntu):**

```bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
```

**Trên Windows:**

Cài đặt Python 3.8+ từ [python.org](https://www.python.org/downloads/)

#### 2. Cài đặt Phụ thuộc Python

**Trên Linux (sử dụng môi trường ảo - khuyến nghị):**

```bash
# Tạo môi trường ảo
python3 -m venv venv

# Kích hoạt môi trường ảo
source venv/bin/activate

# Cài đặt phụ thuộc
pip install flet scapy
```

**Trên Linux (cài đặt toàn hệ thống):**

```bash
pip3 install flet scapy --break-system-packages
```

**Trên Windows:**

```bash
pip install flet scapy
```

#### 3. Chạy Ứng dụng

Vì việc theo dõi mạng yêu cầu quyền hạn cao, bạn phải chạy ứng dụng với quyền root hoặc quản trị viên.

**Trên Linux (với môi trường ảo):**

```bash
sudo venv/bin/python3 albion_insight/main.py
```

**Trên Linux (cài đặt toàn hệ thống):**

```bash
sudo python3 albion_insight/main.py
```

**Trên Windows (Chạy Command Prompt/PowerShell với quyền Quản trị viên):**

```bash
python albion_insight/main.py
```

Ứng dụng sẽ mở trong một cửa sổ máy tính để bàn gốc.

## Cách xây dựng tệp thực thi

Ứng dụng có thể được đóng gói thành một tệp thực thi độc lập bằng cách sử dụng **PyInstaller**. Điều này cho phép người dùng chạy ứng dụng mà không cần cài đặt Python hoặc các phụ thuộc của nó.

Để biết hướng dẫn chi tiết về cách xây dựng tệp thực thi cho Linux, Windows và macOS, hãy xem hướng dẫn **[PACKAGING.md](PACKAGING.md)**.

### Xây dựng nhanh (Linux)

```bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
```

Tệp thực thi sẽ nằm trong thư mục `dist/`.

## Cấu trúc Dự án

Toàn bộ ứng dụng được chứa trong một tệp duy nhất để đơn giản:

| Tệp | Mô tả |
| :--- | :--- |
| `albion_insight/main.py` | Tệp ứng dụng chính chứa tất cả logic (Mô hình, Trình theo dõi mạng, Giao diện người dùng Flet). |
| `README.md` | Tệp tài liệu này. |
| `README.pt-BR.md` | Tệp tài liệu này bằng tiếng Bồ Đào Nha Brazil. |
| `CONTRIBUTING.md` | Hướng dẫn đóng góp cho dự án. |
| `CODE_OF_CONDUCT.md` | Quy tắc ứng xử của dự án. |
| `SECURITY.md` | Chính sách báo cáo lỗ hổng bảo mật. |

## Trạng thái Hiện tại (Dữ liệu thời gian thực)

Ứng dụng hiện bao gồm logic **Giải mã Giao thức Photon**, được dịch từ dự án C# gốc. Điều này cho phép ứng dụng xử lý các sự kiện thời gian thực như `UpdateMoney`, `UpdateFame`, `KilledPlayer` và `Died` trực tiếp từ lưu lượng mạng.

**Lưu ý:** Việc dịch đầy đủ mọi sự kiện chiến đấu (như `CastHit`, `Attack`) là một nỗ lực đang diễn ra. Việc triển khai hiện tại tập trung vào các thống kê cốt lõi và cấu trúc cho Damage Meter. Tính toán DPS của Damage Meter dựa trên các sự kiện đã được giải mã.

## Đóng góp

Chúng tôi hoan nghênh sự đóng góp từ cộng đồng! Cho dù bạn là nhà phát triển, nhà thiết kế hay chỉ là người đam mê Albion Online, có nhiều cách để giúp cải thiện Albion Insight.

Vui lòng đọc [Hướng dẫn Đóng góp](CONTRIBUTING.md) của chúng tôi để biết thông tin chi tiết về cách đóng góp cho dự án này.

### Bắt đầu nhanh cho Người đóng góp:

1.  Fork kho lưu trữ: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Clone bản fork của bạn: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  Tạo một nhánh mới: `git checkout -b feature/your-feature-name`
4.  Thực hiện các thay đổi của bạn và commit: `git commit -m "Add your feature"`
5.  Đẩy lên bản fork của bạn: `git push origin feature/your-feature-name`
6.  Mở một Pull Request trên kho lưu trữ chính

## Giấy phép

Dự án này được cấp phép theo Giấy phép MIT - xem tệp [LICENSE](LICENSE) để biết chi tiết.

## Lời cảm ơn

- Dự án gốc: [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis) của Triky313
- Được xây dựng với framework [Flet](https://flet.dev/)
- Phân tích mạng được cung cấp bởi [Scapy](https://scapy.net/)

---
*Một giải pháp đa nền tảng cho cộng đồng Albion Online.*
