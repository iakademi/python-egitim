# 06 - Pandas ile Veri Analizi

`pandas` kütüphanesiyle tablo verisini okuma, temizleme ve özetleme.

## Konular

- `DataFrame` oluşturma, CSV okuma (`read_csv`, `parse_dates`)
- Veriyi inceleme: `shape`, `dtypes`, `describe`, eksik değer kontrolü
- Yeni sütun hesaplama, `loc` ile seçme, koşullu filtreleme, `nlargest`
- `groupby` ile gruplama ve adlandırılmış toplamalar
- `pivot_table`
- Tarih işlemleri (`dt.month`, `dt.day_name`), `pct_change`
- `merge` ile tablo birleştirme, `fillna`
- Sonucu `to_csv` ile kaydetme

## Kurulum ve Çalıştırma

```bash
pip install -r ../requirements.txt
cd 06-veri-analizi-pandas
python pandas_temelleri.py
python alistirmalar.py
```

## Dosyalar

| Dosya | Açıklama |
|-------|----------|
| `pandas_temelleri.py` | Konu anlatımı |
| `satislar.csv` | Eğitim amaçlı üretilmiş 20 satırlık örnek satış verisi (kurgusaldır) |
| `alistirmalar.py` | Ciro, en çok satan ürün, şehir ortalaması, filtreleme ve kümülatif ciro alıştırmaları ve çözümleri |
