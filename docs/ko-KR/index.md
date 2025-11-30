# Albion Insight (한국어)

[![라이선스: MIT](https://img.shields.io/badge/Licen%C3%A7a-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 버전](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![플랫폼](https://img.shields.io/badge/plataforma-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub 이슈](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![기여 환영](https://img.shields.io/badge/contribui%C3%A7%C3%B5es-bem--vindas-brightgreen.svg)](CONTRIBUTING.ko-KR.md)

**[Read this in English (영어로 읽기)](README.md)**
**[Leia em Português (포르투갈어로 읽기)](README.pt-br.md)**
**[Leia em Espanhol (스페인어로 읽기)](README.es-ES.md)**
**[Leia em Francês (프랑스어로 읽기)](README.fr-FR.md)**
**[Leia em Italiano (이탈리아어로 읽기)](README.it-IT.md)**
**[Leia em Russo (러시아어로 읽기)](README.ru-RU.md)**

**Albion Insight**는 Albion Online 게임을 위한 크로스 플랫폼(Linux, Windows, macOS) 통계 분석 도구이며, **Python**으로 **Flet** 프레임워크를 사용하여 재구현되었습니다. 네트워크 트래픽을 분석하여 은화, 명성, 전투 데이터(데미지 미터)를 포함한 게임 통계를 실시간으로 추적하도록 설계되었습니다.

이 프로젝트는 C#/WPF 기반의 오리지널 `AlbionOnline-StatisticsAnalysis` 도구에 대한 현대적이고 오픈 소스적인 대안이며, 크로스 플랫폼 호환성과 사용 편의성에 중점을 둡니다.

## 기능

*   **크로스 플랫폼 호환성:** Linux, Windows, macOS에서 기본적으로 실행됩니다.
*   **실시간 추적:** `Scapy` 라이브러리를 사용하여 Albion Online 포트(5055, 5056, 5058)의 UDP 패킷을 캡처합니다.
*   **데미지 미터 구조:** 실시간 전투 통계(가한 피해, 치유량, DPS)를 표시하는 데 필요한 데이터 구조와 인터페이스를 포함합니다.
*   **현대적인 인터페이스:** Flet으로 구축되어 빠르고 네이티브한 모양의 데스크톱 애플리케이션을 제공합니다.
*   **세션 관리:** 세션 통계를 시작, 중지, 재설정 및 저장할 수 있습니다.

## 필수 요구 사항

*   Python 3.8+
*   **Flet** 및 **Scapy** 라이브러리.
*   **Root/관리자 권한:** 네트워크 패킷 캡처에 필요합니다.

## 설치 및 구성

### 옵션 1: 빠른 설치 (Linux - 권장)

Linux 사용자를 위해 자동화된 설치 스크립트를 제공합니다:

\`\`\`bash
# 1. 저장소 복제
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. 설치 스크립트 실행
./install.sh

# 3. 애플리케이션 실행
./run.sh
\`\`\`

\`install.sh\` 스크립트는 다음을 수행합니다:
- 시스템 종속성 설치 (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Python 가상 환경 생성
- 필요한 모든 Python 패키지 설치 (Flet, Scapy)

\`run.sh\` 스크립트는 자동으로 root 권한을 요청하고 애플리케이션을 실행합니다.

### 옵션 2: 수동 설치

#### 1. 시스템 종속성 설치

**Linux (Debian/Ubuntu):**

\`\`\`bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
\`\`\`

**Windows:**

[python.org](https://www.python.org/downloads/)에서 Python 3.8+ 설치

#### 2. Python 종속성 설치

**Linux (가상 환경 사용 - 권장):**

\`\`\`bash
# 가상 환경 생성
python3 -m venv venv

# 가상 환경 활성화
source venv/bin/activate

# 종속성 설치
pip install flet scapy
\`\`\`

**Linux (시스템 전체 설치):**

\`\`\`bash
pip3 install flet scapy --break-system-packages
\`\`\`

**Windows:**

\`\`\`bash
pip install flet scapy
\`\`\`

#### 3. 애플리케이션 실행

네트워크 캡처에는 높은 권한이 필요하므로, root 또는 관리자로 애플리케이션을 실행해야 합니다.

**Linux (가상 환경 사용):**

\`\`\`bash
sudo venv/bin/python3 -m albion_insight
\`\`\`

**Linux (시스템 전체 설치):**

\`\`\`bash
sudo python3 -m albion_insight
\`\`\`

**Windows (명령 프롬프트/PowerShell을 관리자로 실행):**

\`\`\`bash
python -m albion_insight
\`\`\`

애플리케이션이 네이티브 데스크톱 창에서 열립니다.

## 실행 파일 생성 방법

애플리케이션은 **PyInstaller**를 사용하여 독립 실행형 실행 파일로 패키징될 수 있습니다. 이를 통해 사용자는 Python이나 해당 종속성을 설치하지 않고도 애플리케이션을 실행할 수 있습니다.

Linux, Windows 및 macOS용 실행 파일을 만드는 방법에 대한 자세한 지침은 **[PACKAGING.md](PACKAGING.md)** (영어) 가이드를 참조하십시오.

### 빠른 빌드 (Linux)

\`\`\`bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed -m albion_insight
\`\`\`

실행 파일은 \`dist/\` 폴더에 있습니다.

## 프로젝트 구조

애플리케이션 전체는 단순화를 위해 단일 파일에 포함되어 있습니다:

| 파일 | 설명 |
| :--- | :--- |
| \`-m albion_insight\` | 모든 로직(모델, 네트워크 트래커, Flet 인터페이스)을 포함하는 주요 애플리케이션 파일입니다. |
| \`README.md\` | 이 문서 파일 (영어). |
| \`README.pt-BR.md\` | 이 문서 파일 (포르투갈어). |
| \`README.fr-FR.md\` | 이 문서 파일 (프랑스어). |
| \`README.it-IT.md\` | 이 문서 파일 (이탈리아어). |
| \`README.ko-KR.md\` | 이 문서 파일 (한국어). |

## 현재 상태 (실시간 데이터)

애플리케이션에는 이제 오리지널 C# 프로젝트에서 번역된 **Photon 프로토콜 디코딩** 로직이 포함되어 있습니다. 이를 통해 애플리케이션은 네트워크 트래픽에서 \`UpdateMoney\`, \`UpdateFame\`, \`KilledPlayer\`, \`Died\`와 같은 이벤트를 실시간으로 처리할 수 있습니다.

**참고:** 모든 전투 이벤트(\`CastHit\`, \`Attack\` 등)의 전체 번역은 지속적인 노력입니다. 현재 구현은 주요 통계 및 데미지 미터 구조에 중점을 둡니다. 데미지 미터의 DPS 계산은 디코딩된 이벤트를 기반으로 합니다.

## 기여하기

커뮤니티의 기여를 환영합니다! 개발자, 디자이너 또는 단순한 Albion Online 애호가이든, Albion Insight를 개선하는 데 도움을 줄 수 있는 많은 방법이 있습니다.

이 프로젝트에 기여하는 방법에 대한 자세한 내용은 [기여 가이드라인](CONTRIBUTING.ko-KR.md)을 읽어보십시오.

### 기여자 빠른 시작:

1.  저장소 포크: [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  포크 복제: \`git clone https://github.com/YOUR_USERNAME/AlbionInsight.git\`
3.  새 브랜치 생성: \`git checkout -b feature/your-feature-name\`
4.  변경 사항 적용 및 커밋: \`git commit -m "Add your feature"\`
5.  포크에 푸시: \`git push origin feature/your-feature-name\`
6.  메인 저장소에 Pull Request 열기

## 라이선스

이 프로젝트는 MIT 라이선스에 따라 라이선스가 부여됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하십시오.

## 감사

- 오리지널 프로젝트: Triky313의 [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis)
- [Flet](https://flet.dev/) 프레임워크로 구축
- [Scapy](https://scapy.net/)로 구동되는 네트워크 분석

---
*Albion Online 커뮤니티를 위한 크로스 플랫폼 솔루션.*
