"""01 - Temeller: Alıştırmalar ve Çözümleri

Her alıştırmanın açıklaması fonksiyonun docstring'indedir.
Önce kendiniz çözmeyi deneyin, sonra çözüm fonksiyonuyla karşılaştırın.

Çalıştırmak için:  python alistirmalar.py
"""


def alistirma_1_bmi(kilo: float, boy_m: float) -> tuple[float, str]:
    """Vücut kitle indeksini (kilo / boy²) hesaplayın ve sınıflandırın.

    < 18.5 Zayıf, < 25 Normal, < 30 Fazla kilolu, diğer Obez.
    """
    bmi = kilo / boy_m ** 2
    if bmi < 18.5:
        sinif = "Zayıf"
    elif bmi < 25:
        sinif = "Normal"
    elif bmi < 30:
        sinif = "Fazla kilolu"
    else:
        sinif = "Obez"
    return round(bmi, 1), sinif


def alistirma_2_fizzbuzz(n: int) -> list[str]:
    """1'den n'e kadar sayıları döndürün; 3'e bölünenler için "Fizz",
    5'e bölünenler için "Buzz", ikisine de bölünenler için "FizzBuzz" yazın."""
    sonuc = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            sonuc.append("FizzBuzz")
        elif i % 3 == 0:
            sonuc.append("Fizz")
        elif i % 5 == 0:
            sonuc.append("Buzz")
        else:
            sonuc.append(str(i))
    return sonuc


def alistirma_3_basamak_toplami(sayi: int) -> int:
    """Bir tam sayının basamaklarının toplamını bulun. (Örnek: 1234 -> 10)"""
    toplam = 0
    sayi = abs(sayi)
    while sayi > 0:
        toplam += sayi % 10
        sayi //= 10
    return toplam


def alistirma_4_palindrom(metin: str) -> bool:
    """Metnin palindrom olup olmadığını (harf büyüklüğü, boşluk ve noktalama
    yok sayılarak) kontrol edin."""
    temiz = "".join(h.lower() for h in metin if h.isalnum())
    return temiz == temiz[::-1]


def alistirma_5_carpim_tablosu(n: int) -> list[str]:
    """n'inci çarpım tablosunu "n x i = sonuç" biçiminde 1'den 10'a kadar döndürün."""
    return [f"{n} x {i} = {n * i}" for i in range(1, 11)]


def alistirma_6_artik_yil(yil: int) -> bool:
    """Artık yıl kuralı: 4'e bölünür; ancak 100'e bölünüyorsa 400'e de bölünmelidir."""
    return yil % 4 == 0 and (yil % 100 != 0 or yil % 400 == 0)


if __name__ == "__main__":
    assert alistirma_1_bmi(70, 1.75) == (22.9, "Normal")
    assert alistirma_1_bmi(100, 1.70)[1] == "Obez"
    assert alistirma_2_fizzbuzz(15)[-1] == "FizzBuzz"
    assert alistirma_2_fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    assert alistirma_3_basamak_toplami(1234) == 10
    assert alistirma_4_palindrom("Ey Edip Adanada pide ye!")
    assert not alistirma_4_palindrom("Python")
    assert alistirma_5_carpim_tablosu(7)[2] == "7 x 3 = 21"
    assert [alistirma_6_artik_yil(y) for y in (1900, 2000, 2024, 2026)] == [False, True, True, False]

    print("BMI:", alistirma_1_bmi(70, 1.75))
    print("FizzBuzz:", ", ".join(alistirma_2_fizzbuzz(15)))
    print("Basamak toplamı (98765):", alistirma_3_basamak_toplami(98765))
    print("Tüm alıştırma çözümleri doğrulandı.")
