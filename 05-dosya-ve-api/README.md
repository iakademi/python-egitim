# 05 - Dosya İşlemleri ve REST API

Dosya okuma/yazma, yaygın veri biçimleri ve HTTP API'leriyle çalışma.

## Konular

- `open` ve `with` deyimi, kodlama (`encoding="utf-8"`)
- `pathlib` ile yol işlemleri
- CSV ve JSON okuma/yazma
- Dosya ve JSON hatalarını yönetme
- `urllib` ile GET / POST istekleri, sorgu parametreleri, zaman aşımı
- HTTP ve bağlantı hatalarını yakalama

## Çalıştırma

```bash
cd 05-dosya-ve-api
python dosya_islemleri.py     # örnek dosyaları cikti/ klasörüne yazar
python api_istemcisi.py       # internet bağlantısı gerektirir
python alistirmalar.py        # ağ gerektirmez
```

`api_istemcisi.py` açık test servisi `jsonplaceholder.typicode.com` adresini kullanır. İnternet bağlantısı yoksa program bunu açıklayan bir mesajla sonlanır. Üretilen `cikti/` klasörü `.gitignore` kapsamındadır.

## Dosyalar

| Dosya | Açıklama |
|-------|----------|
| `dosya_islemleri.py` | Metin, CSV ve JSON işlemleri |
| `api_istemcisi.py` | Standart kütüphane ile REST API istemcisi |
| `alistirmalar.py` | Satır sayma, CSV özeti, JSON filtreleme, log analizi ve güvenli JSON okuma |
