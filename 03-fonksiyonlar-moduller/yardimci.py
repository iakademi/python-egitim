"""Yardımcı modül: fonksiyonlar.py dosyasından içe aktarılarak kullanılır.

Bir .py dosyası kendi başına bir modüldür. `import yardimci` ile içindeki
fonksiyonlara erişilebilir.
"""

KDV_ORANI = 0.20


def kdv_dahil(fiyat: float, oran: float = KDV_ORANI) -> float:
    """KDV dahil fiyatı iki ondalık basamağa yuvarlayarak döndürür."""
    return round(fiyat * (1 + oran), 2)


def para_bicimle(tutar: float) -> str:
    """12345.6 -> '12.345,60 TL' (Türkçe sayı biçimi)."""
    metin = f"{tutar:,.2f}"                       # 12,345.60
    metin = metin.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"{metin} TL"


if __name__ == "__main__":
    # Bu blok yalnızca dosya doğrudan çalıştırıldığında çalışır,
    # başka bir modül tarafından içe aktarıldığında çalışmaz.
    print(para_bicimle(kdv_dahil(1000)))
