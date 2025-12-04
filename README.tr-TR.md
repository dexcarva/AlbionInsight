# Albion Insight - Türkçe (Turkish)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg)](https://github.com/dexcarva/AlbionInsight)
[![GitHub Issues](https://img.shields.io/github/issues/dexcarva/AlbionInsight)](https://github.com/dexcarva/AlbionInsight/issues)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Albion Insight**, Albion Online oyunu için **Python** ve **Flet** çatısı kullanılarak yeniden uygulanan, çapraz platform (Linux, Windows, macOS) istatistik analiz aracıdır. Ağ trafiğini analiz ederek gümüş, şöhret ve savaş verileri (Hasar Ölçer) dahil olmak üzere gerçek zamanlı oyun içi istatistikleri izlemek için tasarlanmıştır.

Bu proje, orijinal C#/WPF tabanlı `AlbionOnline-StatisticsAnalysis` aracına modern, açık kaynaklı bir alternatiftir ve çoklu platform uyumluluğuna ve kullanım kolaylığına odaklanmıştır.

## Özellikler (Features)

*   **Çapraz Platform Uyumluluğu:** Linux, Windows ve macOS'ta doğal olarak çalışır.
*   **Gerçek Zamanlı İzleme:** Albion Online bağlantı noktalarındaki (5055, 5056, 5058) UDP paketlerini koklamak için `Scapy` kütüphanesini kullanır.
*   **Hasar Ölçer Yapısı:** Canlı savaş istatistiklerini (Verilen Hasar, Yapılan İyileştirme, DPS) görüntülemek için gerekli veri yapılarını ve kullanıcı arayüzünü içerir.
*   **Modern Kullanıcı Arayüzü:** Hızlı, yerel görünümlü bir masaüstü uygulaması sağlayan Flet ile oluşturulmuştur.
*   **Oturum Yönetimi:** Oturum istatistiklerini başlatma, durdurma, sıfırlama ve kaydetme imkanı sunar.

## Ön Koşullar (Prerequisites)

*   Python 3.8+
*   **Flet** ve **Scapy** kütüphaneleri.
*   **Root/Yönetici Ayrıcalıkları:** Ağ paketi yakalama için gereklidir.

## Kurulum ve Ayarlar (Installation and Setup)

### Seçenek 1: Hızlı Kurulum (Linux - Önerilen)

Linux kullanıcıları için otomatik kurulum betikleri sağlıyoruz:

\`\`\`bash
# 1. Depoyu klonlayın
git clone https://github.com/dexcarva/AlbionInsight.git
cd AlbionInsight

# 2. Kurulum betiğini çalıştırın
./install.sh

# 3. Uygulamayı çalıştırın
./run.sh
\`\`\`

`install.sh` betiği şunları yapacaktır:
- Sistem bağımlılıklarını kurar (`libpcap-dev`, `python3-pip`, `python3-venv`)
- Bir Python sanal ortamı oluşturur
- Gerekli tüm Python paketlerini (Flet, Scapy) kurar

`run.sh` betiği otomatik olarak root ayrıcalıkları isteyecek ve uygulamayı çalıştıracaktır.

### Seçenek 2: Manuel Kurulum (Tüm Platformlar)

1.  **Depoyu Klonlayın:**
    \`\`\`bash
    git clone https://github.com/dexcarva/AlbionInsight.git
    cd AlbionInsight
    \`\`\`

2.  **Sanal Ortam Oluşturun ve Etkinleştirin:**
    \`\`\`bash
    python3 -m venv venv
    source venv/bin/activate  # Linux/macOS
    # venv\Scripts\activate   # Windows
    \`\`\`

3.  **Bağımlılıkları Kurun:**
    \`\`\`bash
    pip install -r requirements.txt
    \`\`\`
    *(Not: `requirements.txt` dosyası bu örnekte varsayılmıştır. Gerçek bağımlılıklar `pyproject.toml` veya benzeri bir dosyada olabilir. Bu çeviri, varsayılan kurulum adımlarını takip eder.)*

4.  **Çalıştırın:**
    \`\`\`bash
    # Root/Yönetici ayrıcalıklarıyla çalıştırın
    sudo python3 -m albion_insight
    \`\`\`

## Katkıda Bulunma (Contributing)

Katkılarınızı memnuniyetle karşılıyoruz! Lütfen başlamadan önce [CONTRIBUTING.md](CONTRIBUTING.md) dosyasını okuyun.

## Lisans (License)

Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır.
