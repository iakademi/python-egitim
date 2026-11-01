# Python Eğitimi

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-2.x-150458?logo=pandas&logoColor=white)
![Seviye](https://img.shields.io/badge/seviye-ba%C5%9Flang%C4%B1%C3%A7%20%E2%86%92%20orta-blue)
![Dil](https://img.shields.io/badge/dil-T%C3%BCrk%C3%A7e-red)
![Lisans](https://img.shields.io/badge/lisans-MIT-green)

Python'u temelden ileri seviyeye taşıyan, Türkçe açıklamalı ve çözümlü alıştırmalar içeren eğitim deposu.

## Hakkında

Bu depo, **İ-Akademi** Python eğitimlerinde kullanılabilecek konu anlatımlarını ve alıştırmaları içerir. Her modül; çalıştırılabilir bir anlatım betiği, `alistirmalar.py` dosyasında soruları (docstring olarak) ve çözümleri, ayrıca çözümleri `assert` ile doğrulayan bir test bloğu barındırır.

Kodlar **Python 3.10 veya üzeri** gerektirir (`match-case` ve yeni tip ipucu sözdizimi kullanılır).

## İçindekiler

| Modül | Konular |
|-------|---------|
| [01-temeller](./01-temeller) | Değişkenler, veri tipleri, operatörler, f-string, koşullar, döngüler, hata yakalama |
| [02-veri-yapilari](./02-veri-yapilari) | list, tuple, dict, set, comprehension, sıralama, `collections` |
| [03-fonksiyonlar-moduller](./03-fonksiyonlar-moduller) | Fonksiyonlar, `*args/**kwargs`, lambda, closure, dekoratör, generator, modüller |
| [04-oop](./04-oop) | Sınıflar, kalıtım, soyut sınıflar, dunder metotlar, dataclass |
| [05-dosya-ve-api](./05-dosya-ve-api) | Dosya okuma/yazma, CSV, JSON, REST API istekleri |
| [06-veri-analizi-pandas](./06-veri-analizi-pandas) | pandas ile okuma, filtreleme, gruplama, pivot tablo, birleştirme |

## Kurulum / Başlarken

### Gereksinimler

- [Python 3.10+](https://www.python.org/downloads/)
- İsteğe bağlı: [Visual Studio Code](https://code.visualstudio.com/) ve Python eklentisi

```bash
python --version
```

### Depoyu klonlama

```bash
git clone https://github.com/iakademi/python-egitim.git
cd python-egitim
```

### Sanal ortam ve bağımlılıklar

Yalnızca `06-veri-analizi-pandas` modülü ek paket (`pandas`) gerektirir.

```bash
python -m venv .venv

# Linux / macOS
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

### Bir modülü çalıştırma

Betikleri ilgili modül klasörünün içinden çalıştırın:

```bash
cd 01-temeller
python temeller.py
python alistirmalar.py
```

## Klasör Yapısı

```text
python-egitim/
├── 01-temeller/
│   ├── temeller.py
│   ├── alistirmalar.py
│   └── README.md
├── 02-veri-yapilari/
│   ├── veri_yapilari.py
│   ├── alistirmalar.py
│   └── README.md
├── 03-fonksiyonlar-moduller/
│   ├── fonksiyonlar.py
│   ├── yardimci.py
│   ├── alistirmalar.py
│   └── README.md
├── 04-oop/
│   ├── oop.py
│   ├── alistirmalar.py
│   └── README.md
├── 05-dosya-ve-api/
│   ├── dosya_islemleri.py
│   ├── api_istemcisi.py
│   ├── alistirmalar.py
│   └── README.md
├── 06-veri-analizi-pandas/
│   ├── pandas_temelleri.py
│   ├── alistirmalar.py
│   ├── satislar.csv
│   └── README.md
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Alıştırmalarla Çalışma

1. `alistirmalar.py` dosyasını açın ve bir alıştırmanın açıklamasını (docstring) okuyun.
2. Fonksiyonun gövdesini kendiniz yazmayı deneyin; çözüme bakmadan önce kendi sürümünüzü test edin.
3. Dosyayı çalıştırın: `assert` ifadeleri sonucun doğruluğunu denetler, tüm kontroller geçerse "doğrulandı" mesajı görünür.

## Katkıda Bulunma

Katkılarınızı bekliyoruz:

1. Depoyu fork'layın.
2. Yeni bir dal oluşturun: `git checkout -b ozellik/yeni-alistirma`
3. Değişikliklerinizi açıklayıcı bir mesajla commit'leyin.
4. Bir Pull Request açın.

Lütfen kodun çalıştığından emin olun, Türkçe açıklama stilini koruyun ve PEP 8 önerilerine uyun. Hata bildirimleri ve öneriler için [Issues](https://github.com/iakademi/python-egitim/issues) bölümünü kullanabilirsiniz.

## Lisans

Bu proje [MIT Lisansı](./LICENSE) ile lisanslanmıştır.

## İ-Akademi Hakkında

[İ-Akademi](https://iakademi.com), İstanbul merkezli bir BT eğitim merkezidir. Microsoft, Office ve Power Platform, Cisco, siber güvenlik, yazılım geliştirme, PMP/Scrum gibi alanlarda eğitimler sunar; ayrıca Pearson VUE ve Kryterion sınav merkezi olarak hizmet verir.

- Web sitesi: <https://iakademi.com>
- Yazılım eğitimleri için: [iakademi.com](https://iakademi.com) adresindeki yazılım kategorisine göz atabilirsiniz.
