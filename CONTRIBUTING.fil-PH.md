# Pag-ambag sa Albion Insight

**[Basahin sa Ingles](CONTRIBUTING.md)** | **[Basahin sa Portuges (Brazil)](CONTRIBUTING.pt-BR.md)** | **[Basahin sa Portuges (Portugal)](CONTRIBUTING.pt-PT.md)**
<!-- Dito idadagdag ang iba pang mga link sa pagsasalin -->

Una sa lahat, salamat sa pag-iisip na mag-ambag sa Albion Insight! Ang mga taong tulad mo ang nagpapaganda sa Albion Insight bilang isang mahusay na tool para sa komunidad ng Albion Online.

## Talaan ng Nilalaman
	
- [Kodigo ng Pag-uugali](#kodigo-ng-pag-uugali)
- [Paano Ako Makakapag-ambag?](#paano-ako-makakapag-ambag)
  - [Pag-uulat ng mga Bug](#pag-uulat-ng-mga-bug)
  - [Pagmumungkahi ng mga Tampok](#pagmumungkahi-ng-mga-tampok)
  - [Mga Kontribusyon sa Code](#mga-kontribusyon-sa-code)
  - [Dokumentasyon](#dokumentasyon)
- [Pag-set up ng Pagpapaunlad](#pag-set-up-ng-pagpapaunlad)
- [Mga Pamantayan sa Pag-code](#mga-pamantayan-sa-pag-code)
- [Mga Mensahe ng Commit](#mga-mensahe-ng-commit)
- [Proseso ng Pull Request](#proseso-ng-pull-request)

## Kodigo ng Pag-uugali

Ang proyektong ito at lahat ng nakikilahok dito ay pinamamahalaan ng aming Kodigo ng Pag-uugali. Sa pamamagitan ng paglahok, inaasahang paninindigan mo ang kodigong ito. Mangyaring iulat ang hindi katanggap-tanggap na pag-uugali sa mga tagapamahala ng proyekto.

## Paano Ako Makakapag-ambag?

### Pag-uulat ng mga Bug

Bago gumawa ng mga ulat ng bug, mangyaring suriin ang mga umiiral na isyu upang maiwasan ang mga duplicate. Kapag gumawa ka ng ulat ng bug, isama ang mas maraming detalye hangga't maaari gamit ang template ng ulat ng bug.

**Ang magagandang ulat ng bug ay kinabibilangan ng:**
- Isang malinaw at naglalarawang pamagat
- Eksaktong mga hakbang upang kopyahin ang problema
- Inaasahan kumpara sa aktwal na pag-uugali
- Mga screenshot kung naaangkop
- Ang iyong mga detalye sa kapaligiran (OS, bersyon ng Python, atbp.)
- Mga nauugnay na log o mensahe ng error

### Pagmumungkahi ng mga Tampok

Ang mga mungkahi sa tampok ay malugod na tinatanggap! Mangyaring gamitin ang template ng kahilingan sa tampok at ibigay ang:
- Isang malinaw na paglalarawan ng tampok
- Ang problemang nilulutas nito
- Posibleng mga diskarte sa pagpapatupad
- Anumang mga alternatibo na iyong isinasaalang-alang

### Mga Kontribusyon sa Code

Gustung-gusto namin ang mga kontribusyon sa code! Narito kung paano magsimula:

1. **I-fork ang repository** at gawin ang iyong branch mula sa `master`
2. **I-set up ang iyong development environment** (tingnan ang Pag-set up ng Pagpapaunlad sa ibaba)
3. **Gawin ang iyong mga pagbabago** na sumusunod sa aming mga pamantayan sa pag-code
4. **Subukan ang iyong mga pagbabago** nang lubusan
5. **I-update ang dokumentasyon** kung kinakailangan
6. **Magsumite ng pull request** gamit ang aming PR template

### Dokumentasyon

Ang mga pagpapabuti sa dokumentasyon ay palaging pinahahalagahan! Kasama rito ang:
- Mga file ng README
- Mga pahina ng Wiki
- Mga komento sa code
- Mga tutorial at gabay
- Mga pagsasalin sa ibang wika

## Pag-set up ng Pagpapaunlad

### Mga Kinakailangan

- Python 3.8 o mas mataas
- Git
- Mga pribilehiyo ng Root/Administrator (para sa pagkuha ng packet)

### Pag-set up ng Iyong Kapaligiran

```bash
# I-clone ang iyong fork
git clone https://github.com/YOUR_USERNAME/AlbionInsight.git
cd AlbionInsight

# Gumawa ng virtual environment
python3 -m venv venv

# I-activate ang virtual environment
# Sa Linux/macOS:
source venv/bin/activate
# Sa Windows:
venv\Scripts\activate

# I-install ang mga dependencies
pip install -r requirements.txt

# I-install ang mga development dependencies
pip install pylint flake8 black pytest
```

### Pagpapatakbo ng Application

```bash
# Sa Linux/macOS:
sudo venv/bin/python3 albion_insight.py

# Sa Windows (bilang Administrator):
python albion_insight.py
```

## Mga Pamantayan sa Pag-code

Sinusunod namin ang mga alituntunin ng estilo ng PEP 8 para sa Python code. Mangyaring tiyakin na ang iyong code ay sumusunod sa mga pamantayang ito:

- Gumamit ng 4 na espasyo para sa indentation (walang tabs)
- Maximum na haba ng linya na 100 character
- Gumamit ng makabuluhang mga pangalan ng variable at function
- Magdagdag ng docstrings sa lahat ng function at class
- Isama ang mga type hint kung saan naaangkop
- Panatilihing nakatuon at maikli ang mga function

**Mga tool na makakatulong:**
```bash
# I-format ang iyong code gamit ang black
black albion_insight.py

# Suriin ang mga isyu sa estilo
flake8 albion_insight.py

# Patakbuhin ang linter
pylint albion_insight.py
```

## Mga Mensahe ng Commit

Sumulat ng malinaw at makabuluhang mga mensahe ng commit:

- Gumamit ng kasalukuyang panahunan ("Magdagdag ng tampok" hindi "Nagdagdag ng tampok")
- Gumamit ng imperative mood ("Ilipat ang cursor sa..." hindi "Inililipat ang cursor sa...")
- Limitahan ang unang linya sa 72 character
- Mag-refer sa mga isyu at pull request kung kailan nauugnay

**Mga Halimbawa:**
```
Magdagdag ng functionality sa pag-export ng damage meter
	
Ayusin ang network packet parsing para sa mga koneksyon sa IPv6
	
I-update ang README gamit ang mga tagubilin sa pag-install ng macOS
	
Isinasara ang #123
```

## Proseso ng Pull Request

1. **I-update ang dokumentasyon** para sa anumang pagbabago sa functionality
2. **Magdagdag ng mga pagsubok** para sa mga bagong tampok o pag-aayos ng bug
3. **Tiyakin na pumasa ang lahat ng pagsubok** bago isumite
4. **I-update ang README.md** kung kinakailangan
5. **Punan ang PR template** nang kumpleto
6. **I-link ang mga kaugnay na isyu** sa iyong paglalarawan ng PR
7. **Humiling ng pagsusuri** mula sa mga tagapamahala
8. **Tugunan ang feedback** kaagad at propesyonal

### PR Checklist

Bago isumite ang iyong PR, tiyakin na:
- [ ] Ang code ay sumusunod sa mga alituntunin ng estilo ng proyekto
- [ ] Nakumpleto ang self-review
- [ ] Nagdagdag ng mga komento sa mga kumplikadong seksyon ng code
- [ ] Na-update ang dokumentasyon
- [ ] Walang bagong babala na nabuo
- [ ] Nagdagdag at pumasa ang mga pagsubok
- [ ] Na-merge ang mga dependent na pagbabago

## Mga Tanong?

Huwag mag-atubiling magtanong! Maaari kang:
- Magbukas ng isyu gamit ang label na "question"
- Sumali sa aming mga talakayan sa komunidad
- Makipag-ugnayan sa mga tagapamahala

Salamat sa pag-ambag sa Albion Insight! Ang iyong mga pagsisikap ay nakakatulong upang mapabuti ang tool na ito para sa buong komunidad ng Albion Online.
