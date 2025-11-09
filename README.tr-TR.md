# Albion Insight

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

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

**Albion Insight**, Albion Online oyunu için ağ trafiğini analiz ederek gümüş, şöhret ve savaş verileri (Hasar Ölçer) dahil olmak üzere gerçek zamanlı oyun içi istatistikleri izlemek için tasarlanmış, **Flet** çerçevesi kullanılarak **Python** ile yeniden uygulanan, çapraz platform (Linux, Windows, macOS) bir istatistik analiz aracıdır.

Bu proje, orijinal C#/WPF tabanlı `AlbionOnline-StatisticsAnalysis` aracına modern, açık kaynaklı bir alternatiftir ve çoklu platform uyumluluğuna ve kullanım kolaylığına odaklanmaktadır.

## Özellikler

*   **Çapraz Platform Uyumluluğu:** Linux, Windows ve macOS'ta doğal olarak çalışır.
*   **Gerçek Zamanlı Takip:** Albion Online portlarında (5055, 5056, 5058) UDP paketlerini koklamak için `Scapy` kütüphanesini kullanır.
*   **Hasar Ölçer Yapısı:** Canlı savaş istatistiklerini (Verilen Hasar, Yapılan İyileştirme, DPS) görüntülemek için gerekli veri yapılarını ve kullanıcı arayüzünü içerir.
*   **Modern Kullanıcı Arayüzü:** Hızlı, yerel görünümlü bir masaüstü uygulaması sağlayan Flet ile oluşturulmuştur.
*   **Oturum Yönetimi:** Oturum istatistiklerini başlatma, durdurma, sıfırlama ve kaydetme imkanı sunar.

## Önkoşullar

*   Python 3.8+
*   **Flet** ve **Scapy** kütüphaneleri.
*   **Root/Yönetici Ayrıcalıkları:** Ağ paketi yakalama için gereklidir.

## Kurulum ve Ayarlar

### Seçenek 1: Hızlı Kurulum (Linux - Önerilen)

Linux kullanıcıları için otomatik kurulum betikleri sağlıyoruz:

```bash
# 1. Depoyu klonlayın
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Kurulum betiğini çalıştırın
./install.sh

# 3. Uygulamayı çalıştırın
./run.sh
```

`install.sh` betiği şunları yapacaktır:
- Sistem bağımlılıklarını kurar (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Bir Python sanal ortamı oluşturur
- Gerekli tüm Python paketlerini kurar (Flet, Scapy)

`run.sh` betiği otomatik olarak root ayrıcalıkları isteyecek ve uygulamayı çalıştıracaktır.

### Seçenek 2: Manuel Kurulum

#### 1. Sistem Bağımlılıklarını Kurun

**Linux'ta (Debian/Ubuntu):**

```bash
sudo apt update
sudo apt install libpcap-dev python3-pip python3-venv
```

**Windows'ta:**

[python.org](https://www.python.org/downloads/)'dan Python 3.8+ kurun

#### 2. Install Python Dependencies

**Linux'ta (sanal ortam kullanarak - önerilen):**

```bash
# Sanal ortam oluşturun
python3 -m venv venv

# Sanal ortamı etkinleştirin
source venv/bin/activate

# Bağımlılıkları kurun
pip install flet scapy
```

**Linux'ta (sistem genelinde kurulum):**

```bash
pip3 install flet scapy --break-system-packages
```

**Windows'ta:**

```bash
pip install flet scapy
```

#### 3. Uygulamayı Çalıştırma

Ağ koklama (sniffing) yükseltilmiş ayrıcalıklar gerektirdiğinden, uygulamayı root ou yönetici olarak çalıştırmanız gerekir.

**Linux'ta (sanal ortam ile):**

```bash
sudo venv/bin/python3 albion_insight.py
```

**Linux'ta (sistem genelinde kurulum):**

```bash
sudo python3 albion_insight.py
```

**Windows'ta (Komut İstemi/PowerShell'i Yönetici olarak Çalıştırın):**

```bash
python albion_insight.py
```

Uygulama, yerel bir masaüstü penceresinde açılacaktır.

## Çalıştırılabilir Dosya Nasıl Oluşturulur

Uygulama, **PyInstaller** kullanılarak bağımsız bir çalıştırılabilir dosyaya paketlenebilir. Bu, kullanıcıların Python'u veya bağımlılıklarını kurmadan uygulamayı çalıştırmasına olanak tanır.

Linux, Windows e macOS için çalıştırılabilir dosyalar oluşturma hakkında ayrıntılı talimatlar için **[PACKAGING.md](PACKAGING.md)** kılavuzuna bakın.

### Hızlı Derleme (Linux)

```bash
source venv/bin/activate
pip install pyinstaller
pyinstaller --name "AlbionInsight" --onefile --windowed albion_insight.py
```

Çalıştırılabilir dosya `dist/` klasöründe bulunacaktır.

## Proje Yapısı

Tüm uygulama, basitlik için tek bir dosya içinde yer almaktadır:

| Dosya | Açıklama |
| :--- | :--- |
| `albion_insight.py` | Tüm mantığı (Modeller, Ağ Takipçisi, Flet Kullanıcı Arayüzü) içeren ana uygulama dosyası. |
| `README.md` | Bu dokümantasyon dosyası. |
| `README.pt-BR.md` | Bu dokümantasyon dosyası Brezilya Portekizcesi'nde. |
| `CONTRIBUTING.md` | Projeye katkıda bulunma yönergeleri. |
| `CODE_OF_CONDUCT.md` | Projenin Davranış Kuralları. |
| `SECURITY.md` | Güvenlik açıklarını bildirme politikası. |

## Current Status (Real-Time Data)

Uygulama agora inclui a lógica de **Decodificação do Protocolo Photon**, traduzida do projeto C# original. Isso permite que o aplicativo processe eventos em tempo real como `UpdateMoney`, `UpdateFame`, `KilledPlayer` e `Died` diretamente do tráfego de rede.

**Nota:** A tradução completa de cada evento de combate (como `CastHit`, `Attack`) é um esforço contínuo. A implementação atual foca nas estatísticas centrais e na estrutura para o Medidor de Dano. O cálculo de DPS do Medidor de Dano é baseado nos eventos decodificados.

## Katkıda Bulunma

Topluluktan gelen katkıları memnuniyetle karşılıyoruz! İster bir geliştirici, ister bir tasarımcı, ister sadece bir Albion Online meraklısı olun, Albion Insight'ı geliştirmeye yardımcı olmanın birçok yolu vardır.

Bu projeye nasıl katkıda bulunulacağı hakkında ayrıntılı bilgi için lütfen [Katkıda Bulunma Yönergelerimizi](CONTRIBUTING.md) okuyun.

### Katkıda Bulunanlar İçin Hızlı Başlangıç:

1.  Depoyu çatallayın (Fork): [github.com/dexcarva/AlbionInsight](https://github.com/dexcarva/AlbionInsight)
2.  Çatalınızı klonlayın: `git clone https://github.com/YOUR_USERNAME/AlbionInsight.git`
3.  Yeni bir dal (branch) oluşturun: `git checkout -b feature/ozellik-adiniz`
4.  Değişikliklerinizi yapın ve kaydedin (commit): `git commit -m "Özelliğinizi ekleyin"`
5.  Çatalınıza itin (push): `git push origin feature/ozellik-adiniz`
6.  Ana depoda bir Çekme İsteği (Pull Request) açın

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır - ayrıntılar için [LICENSE](LICENSE) dosyasına bakın.

## Teşekkürler

- Orijinal proje: Triky313 tarafından [AlbionOnline-StatisticsAnalysis](https://github.com/Triky313/AlbionOnline-StatisticsAnalysis)
- [Flet](https://flet.dev/) çerçevesi ile oluşturulmuştur
- [Scapy](https://scapy.net/) tarafından desteklenen ağ analizi

---
*Albion Online topluluğu için çapraz platform bir çözüm.*
