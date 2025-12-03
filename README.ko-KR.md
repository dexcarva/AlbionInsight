# Albion Insight

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Albion Insight**는 **Python**과 **Flet** 프레임워크를 사용하여 재구현된, 게임 '알비온 온라인(Albion Online)'을 위한 크로스 플랫폼(Linux, Windows, macOS) 통계 분석 도구입니다. 네트워크 트래픽 분석을 통해 실시간으로 은화, 명성, 전투 데이터(데미지 미터)를 포함한 게임 내 통계를 추적하도록 설계되었습니다.

이 프로젝트는 기존 C#/WPF 기반의 `AlbionOnline-StatisticsAnalysis` 도구에 대한 현대적이고 오픈 소스적인 대안이며, 다중 플랫폼 호환성과 사용 편의성에 중점을 둡니다.

## 기능 (Features)

*   **크로스 플랫폼 호환성:** Linux, Windows, macOS에서 기본적으로 실행됩니다.
*   **실시간 추적:** `Scapy` 라이브러리를 사용하여 알비온 온라인 포트 (5055, 5056, 5058)의 UDP 패킷을 스니핑합니다.
*   **데미지 미터 구조:** 실시간 전투 통계(가한 피해, 치유량, DPS)를 표시하기 위한 필수 데이터 구조 및 UI를 포함합니다.
*   **현대적인 UI:** Flet으로 구축되어 빠르고 네이티브처럼 보이는 데스크톱 애플리케이션을 제공합니다.
*   **세션 관리:** 세션 통계를 시작, 중지, 재설정 및 저장할 수 있습니다.

## 필수 조건 (Prerequisites)

*   Python 3.8+
*   **Flet** 및 **Scapy** 라이브러리.
*   **Root/관리자 권한:** 네트워크 패킷 캡처에 필요합니다.

## 설치 및 설정 (Installation and Setup)

### 옵션 1: 빠른 설치 (Linux - 권장)

Linux 사용자를 위해 자동화된 설치 스크립트를 제공합니다:

```bash
# 1. 저장소 복제
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. 설치 스크립트 실행
./install.sh

# 3. 애플리케이션 실행
./run.sh
```

`install.sh` 스크립트는 다음을 수행합니다:
- 시스템 종속성 설치 (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Python 가상 환경 생성
- 필요한 모든 Python 패키지 설치 (Flet, Scapy)

`run.sh` 스크립트는 자동으로 Root 권한을 요청하고 애플리케이션을 실행합니다.

### 옵션 2: 수동 설치 (Manual Installation)

#### 1. 시스템 종속성 설치

**Linux (Debian/Ubuntu)에서:**

```bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
```

**Windows에서:**

[python.org](https://www.python.org/downloads/)에서 Python 3.8+ 설치

#### 2. Python 종속성 설치

**Linux에서 (가상 환경 사용 - 권장):**

```bash
# 가상 환경 생성
python3 -m venv venv

# 가상 환경 활성화
source venv/bin/activate

# 종속성 설치
pip install flet scapy
```

**Linux에서 (시스템 전체 설치):**

```bash
pip3 install flet scapy --break-system-packages
```

**Windows에서:**

```bash
pip install flet scapy
```

#### 3. 애플리케이션 실행

네트워크 스니핑에는 권한 상승이 필요하므로, 애플리케이션을 root 또는 관리자로 실행해야 합니다.

**Linux에서 (가상 환경 사용):**

```bash
sudo venv/bin/python3 -m albion_insight
```

**Linux에서 (시스템 전체 설치):**

```bash
sudo python3 -m albion_insight
```

**Windows에서 (관리자 권한으로 명령 프롬프트/PowerShell 실행):**

```bash
python -m albion_insight
```

애플리케이션은 네이티브 데스크톱 창에서 열립니다.

## 실행 파일 빌드 방법 (How to Build an Executable)

**PyInstaller**를 사용하여 애플리케이션을 독립 실행형 실행 파일로 패키징할 수 있습니다. 이를 통해 사용자는 Python이나 해당 종속성을 설치하지 않고도 애플리케이션을 실행할 수 있습니다.

Linux, Windows 및 macOS용 실행 파일 빌드에 대한 자세한 지침은 **[PACKAGING.md](PACKAGING.md)** 가이드를 참조하십시오.

### 빠른 빌드 (Linux)

```bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight/main.py
```

실행 파일은 `dist/` 폴더에 위치합니다.

## 프로젝트 구조 (Project Structure)

애플리케이션은 더 나은 유지 관리 및 확장성을 위해 모듈식 구성 요소로 구성되어 있습니다:

| 파일 | 설명 |
| :--- | :--- |
| `albion_insight/core/` | 핵심 로직, 네트워크 추적, 데이터 모델 및 프로토콜 디코딩. |
| `albion_insight/ui/` | Flet으로 구축된 사용자 인터페이스 구성 요소. |
| `albion_insight/utils/` | 유틸리티 함수, 구성 및 로깅. |
| `albion_insight/__main__.py` | 애플리케이션의 진입점. |
| `README.md` | 이 문서 파일. |
| `CONTRIBUTING.md` | 프로젝트 기여 지침. |
| `CODE_OF_CONDUCT.md` | 프로젝트 행동 강령. |
| `SECURITY.md` | 보안 취약점 보고 정책. |
| `README.it-IT.md` | Documentazione in italiano. |
| `README.pt-BR.md` | Documentação em português do Brasil. |
| `README.ru-RU.md` | Документация на русском языке. |
| `README.fr-FR.md` | Documentation en français. |
| `README.zh-CN.md` | 简体中文 문서. |
| `README.ko-KR.md` | 한국어 문서. |

## 현재 상태 (실시간 데이터) (Current Status - Real-Time Data)

애플리케이션에는 이제 원래 C# 프로젝트에서 번역된 **Photon 프로토콜 디코딩** 로직이 포함되어 있습니다. 이를 통해 애플리케이션은 네트워크 트래픽에서 `UpdateMoney` (은화 업데이트), `UpdateFame` (명성 업데이트), `KilledPlayer` (플레이어 처치) 및 `Died` (사망)와 같은 실시간 이벤트를 직접 처리할 수 있습니다.

**참고:** 모든 전투 이벤트(예: `CastHit`, `Attack`)의 전체 번역은 진행 중인 작업입니다. 현재 구현은 핵심 통계와 데미지 미터 구조에 중점을 둡니다. 데미지 미터의 DPS 계산은 디코딩된 이벤트를 기반으로 합니다.

## 기여 (Contributing)

커뮤니티의 기여를 환영합니다! 개발자, 디자이너 또는 단순히 알비온 온라인 애호가이든 Albion Insight를 개선하는 데 도움이 될 수 있는 많은 방법이 있습니다.

이 프로젝트에 기여하는 방법에 대한 자세한 내용은 [기여 가이드라인](CONTRIBUTING.md)을 읽어보십시오.

### 기여자 빠른 시작:

1.  저장소 포크: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  포크 복제: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  새 브랜치 생성: `git checkout -b feature/your-feature-name`
4.  변경 사항 적용 및 커밋: `git commit -m "Add your feature"`
5.  포크에 푸시: `git push origin feature/your-feature-name`
6.  메인 저장소에 Pull Request 열기

## 라이선스 (License)

이 프로젝트는 MIT 라이선스에 따라 라이선스가 부여됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하십시오.

## 감사 (Acknowledgments)

- 원본 프로젝트: Triky313의 [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis)
- [Flet](https://flet.dev/) 프레임워크로 구축
- [Scapy](https://scapy.net/)로 구동되는 네트워크 분석

---
*알비온 온라인 커뮤니티를 위한 크로스 플랫폼 솔루션.*
