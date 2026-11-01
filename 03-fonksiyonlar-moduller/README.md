# 03 - Fonksiyonlar ve Modüller

Kodu yeniden kullanılabilir parçalara bölmek ve modüller halinde düzenlemek.

## Konular

- Fonksiyon tanımı, varsayılan parametreler, anahtar kelimeli argümanlar
- `*args` ve `**kwargs`, argüman açma (unpacking)
- Değiştirilebilir varsayılan parametre tuzağı
- `lambda`, `map`, `filter`, `sorted(key=...)`
- Kapsam (`global`, `nonlocal`) ve closure
- Dekoratörler ve `functools.wraps`
- Özyineleme ve generator (`yield`)
- Kendi modülünüzü içe aktarma, `if __name__ == "__main__"` kalıbı
- Standart kütüphane: `math`, `random`, `datetime`

## Çalıştırma

```bash
cd 03-fonksiyonlar-moduller
python fonksiyonlar.py
python alistirmalar.py
```

> Betikleri bu klasörün içinden çalıştırın; `yardimci.py` modülü aynı klasördeki dosyalardan içe aktarılır.

## Dosyalar

| Dosya | Açıklama |
|-------|----------|
| `fonksiyonlar.py` | Konu anlatımı |
| `yardimci.py` | İçe aktarılan örnek modül (KDV ve para biçimlendirme) |
| `alistirmalar.py` | Asal sayı, EBOB/EKOK, ortalama, çağrı sayacı dekoratörü, Collatz generator'ı ve sepet toplamı |
