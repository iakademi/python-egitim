"""03 - Fonksiyonlar ve Modüller

Konular: parametre türleri, *args/**kwargs, lambda, kapsam (scope), closure,
         dekoratör, generator, tip ipuçları, modül içe aktarma, standart kütüphane.

Çalıştırmak için:  python fonksiyonlar.py
"""

import functools
import math
import random
import time
from datetime import date, datetime, timedelta

import yardimci                      # kendi yazdığımız modül
from yardimci import kdv_dahil      # modülden yalnızca bir fonksiyon


def baslik(metin: str) -> None:
    print(f"\n=== {metin} ===")


# ---------------------------------------------------------------------
baslik("1. Fonksiyon Tanımı ve Parametreler")
# ---------------------------------------------------------------------
def selamla(isim: str, selam: str = "Merhaba") -> str:
    """Varsayılan değerli parametre örneği."""
    return f"{selam} {isim}!"


print(selamla("Ayşe"))
print(selamla("Can", selam="İyi akşamlar"))            # anahtar kelimeli argüman


def toplam(*sayilar: float) -> float:
    """*args: istenen sayıda konumsal argüman."""
    return sum(sayilar)


def profil(ad: str, **ozellikler) -> str:
    """**kwargs: istenen sayıda anahtar-değer argümanı."""
    detay = ", ".join(f"{k}={v}" for k, v in ozellikler.items())
    return f"{ad} ({detay})"


print(toplam(1, 2, 3, 4), "|", profil("Elif", sehir="İstanbul", yas=27))

liste = [5, 6]
print(toplam(*liste, 10), "|", profil(**{"ad": "Kaan", "rol": "öğrenci"}))   # açma (unpacking)


def min_max(sayilar: list[float]) -> tuple[float, float]:
    """Birden fazla değer döndürme (aslında tuple döner)."""
    return min(sayilar), max(sayilar)


en_az, en_cok = min_max([4, 9, 1, 7])
print(f"en az={en_az}, en çok={en_cok}")

# ---------------------------------------------------------------------
baslik("2. Dikkat: Değiştirilebilir Varsayılan Parametre")
# ---------------------------------------------------------------------
def hatali_ekle(oge, liste=[]):          # liste fonksiyon tanımlanırken bir kez oluşturulur!
    liste.append(oge)
    return liste


def dogru_ekle(oge, liste=None):
    if liste is None:
        liste = []
    liste.append(oge)
    return liste


hatali_ekle(1)
print("hatalı:", hatali_ekle(2), "| doğru:", dogru_ekle(2))

# ---------------------------------------------------------------------
baslik("3. Lambda, map, filter, sorted")
# ---------------------------------------------------------------------
kare = lambda x: x ** 2
sayilar = [1, 2, 3, 4, 5, 6]
print(kare(7), list(map(kare, sayilar)), list(filter(lambda x: x % 2 == 0, sayilar)))
kelimeler = ["python", "sql", "c#", "scrum"]
print(sorted(kelimeler, key=len), sorted(kelimeler, key=lambda k: k[-1]))

# ---------------------------------------------------------------------
baslik("4. Kapsam (scope) ve Closure")
# ---------------------------------------------------------------------
def sayac_olustur():
    sayi = 0

    def artir():
        nonlocal sayi                   # dış fonksiyondaki değişkeni değiştirir
        sayi += 1
        return sayi

    return artir


sayac = sayac_olustur()
print(sayac(), sayac(), sayac())


def carpan_olustur(n: int):
    return lambda x: x * n


iki_kati, uc_kati = carpan_olustur(2), carpan_olustur(3)
print(iki_kati(10), uc_kati(10))

# ---------------------------------------------------------------------
baslik("5. Dekoratör")
# ---------------------------------------------------------------------
def sure_olc(fonksiyon):
    @functools.wraps(fonksiyon)          # orijinal fonksiyonun adını/docstring'ini korur
    def sarmalayici(*args, **kwargs):
        baslangic = time.perf_counter()
        sonuc = fonksiyon(*args, **kwargs)
        gecen = (time.perf_counter() - baslangic) * 1000
        print(f"  [{fonksiyon.__name__}] {gecen:.2f} ms sürdü")
        return sonuc
    return sarmalayici


@sure_olc
def fibonacci_listesi(n: int) -> list[int]:
    dizi = [0, 1]
    while len(dizi) < n:
        dizi.append(dizi[-1] + dizi[-2])
    return dizi[:n]


print(fibonacci_listesi(12))

# ---------------------------------------------------------------------
baslik("6. Özyineleme ve Generator")
# ---------------------------------------------------------------------
def faktoriyel(n: int) -> int:
    return 1 if n <= 1 else n * faktoriyel(n - 1)


def fibonacci_uretec(sinir: int):
    """yield ile değerleri tek tek üretir; tüm listeyi belleğe almaz."""
    a, b = 0, 1
    while a < sinir:
        yield a
        a, b = b, a + b


print(faktoriyel(10), list(fibonacci_uretec(100)))
print("Generator ifadesi:", sum(n * n for n in range(1, 1001)))

# ---------------------------------------------------------------------
baslik("7. Kendi Modülümüzü Kullanma")
# ---------------------------------------------------------------------
print(yardimci.para_bicimle(kdv_dahil(2499.90)))
print("KDV oranı:", yardimci.KDV_ORANI)

# ---------------------------------------------------------------------
baslik("8. Standart Kütüphaneden Örnekler")
# ---------------------------------------------------------------------
print("math:", math.sqrt(144), math.ceil(4.2), math.floor(4.8), round(math.pi, 4))

random.seed(42)                          # tekrarlanabilir sonuç için
print("random:", random.randint(1, 100), random.choice(["a", "b", "c"]), random.sample(range(10), 3))

bugun = date(2026, 1, 15)
print("tarih:", bugun.strftime("%d.%m.%Y"), "| 30 gün sonra:", bugun + timedelta(days=30),
      "| gün adı indeksi:", bugun.weekday())
fark = datetime(2026, 12, 31) - datetime(2026, 1, 1)
print("yılbaşından yıl sonuna gün farkı:", fark.days)
