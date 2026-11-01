"""03 - Fonksiyonlar ve Modüller: Alıştırmalar ve Çözümleri

Çalıştırmak için:  python alistirmalar.py
"""

import functools

from yardimci import kdv_dahil, para_bicimle


def alistirma_1_asal_mi(n: int) -> bool:
    """n sayısının asal olup olmadığını kontrol edin (kök n'e kadar bölenleri deneyin)."""
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def alistirma_2_ebob_ekok(a: int, b: int) -> tuple[int, int]:
    """Öklid algoritmasıyla (EBOB, EKOK) çiftini döndürün."""
    x, y = a, b
    while y:
        x, y = y, x % y
    return x, a * b // x


def alistirma_3_ortalama(*notlar: float, yuvarla: int = 1) -> float:
    """Değişken sayıda notun ortalamasını `yuvarla` basamağa yuvarlayarak döndürün."""
    if not notlar:
        raise ValueError("En az bir not girilmelidir.")
    return round(sum(notlar) / len(notlar), yuvarla)


def alistirma_4_cagri_sayaci(fonksiyon):
    """Dekoratör: Sarmalanan fonksiyonun kaç kez çağrıldığını `cagri_sayisi` özniteliğinde tutun."""
    @functools.wraps(fonksiyon)
    def sarmalayici(*args, **kwargs):
        sarmalayici.cagri_sayisi += 1
        return fonksiyon(*args, **kwargs)

    sarmalayici.cagri_sayisi = 0
    return sarmalayici


@alistirma_4_cagri_sayaci
def selam(isim: str) -> str:
    return f"Merhaba {isim}"


def alistirma_5_collatz(n: int):
    """Generator: Collatz dizisini (çift ise n/2, tek ise 3n+1) 1'e ulaşana kadar üretin."""
    while n != 1:
        yield n
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    yield 1


def alistirma_6_sepet_toplami(sepet: dict[str, tuple[float, int]]) -> str:
    """Sepet {ürün: (birim_fiyat, adet)} yapısındadır. KDV dahil toplamı
    Türkçe para biçimiyle döndürün (yardimci modülünü kullanın)."""
    ara_toplam = sum(fiyat * adet for fiyat, adet in sepet.values())
    return para_bicimle(kdv_dahil(ara_toplam))


if __name__ == "__main__":
    assert [n for n in range(20) if alistirma_1_asal_mi(n)] == [2, 3, 5, 7, 11, 13, 17, 19]
    assert alistirma_2_ebob_ekok(12, 18) == (6, 36)
    assert alistirma_3_ortalama(70, 85, 90) == 81.7
    assert alistirma_3_ortalama(70, 85, yuvarla=0) == 78
    selam("A"); selam("B")
    assert selam.cagri_sayisi == 2
    assert list(alistirma_5_collatz(6)) == [6, 3, 10, 5, 16, 8, 4, 2, 1]
    assert alistirma_6_sepet_toplami({"kalem": (10.0, 5), "defter": (25.0, 2)}) == "120,00 TL"

    print("Collatz(27) adım sayısı:", len(list(alistirma_5_collatz(27))) - 1)
    print("Tüm alıştırma çözümleri doğrulandı.")
