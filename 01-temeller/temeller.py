"""01 - Python Temelleri

Konular: değişkenler, veri tipleri, operatörler, f-string, koşullar, döngüler,
         tip dönüşümü, hata yakalama.

Çalıştırmak için:  python temeller.py
"""


def baslik(metin: str) -> None:
    print(f"\n=== {metin} ===")


# ---------------------------------------------------------------------
baslik("1. Değişkenler ve Veri Tipleri")
# ---------------------------------------------------------------------
ad = "Ayşe"            # str
yas = 28               # int
boy = 1.68             # float
aktif = True           # bool
bos = None             # NoneType
karmasik = 3 + 4j      # complex

for deger in (ad, yas, boy, aktif, bos, karmasik):
    print(f"{deger!r:>10}  ->  {type(deger).__name__}")

# Python dinamik tiplidir: aynı değişken farklı tipte değer alabilir
x = 10
x = "artık bir metin"
print(x)

# Çoklu atama ve değer takası
a, b = 1, 2
a, b = b, a
print(f"a={a}, b={b}")

# ---------------------------------------------------------------------
baslik("2. Operatörler")
# ---------------------------------------------------------------------
print("17 / 5  =", 17 / 5)      # gerçek bölme
print("17 // 5 =", 17 // 5)     # tam bölme
print("17 % 5  =", 17 % 5)      # mod
print("2 ** 10 =", 2 ** 10)     # üs alma
print("karşılaştırma zinciri:", 1 < 5 < 10)
print("mantıksal:", (5 > 3) and not (2 > 4), "| üyelik:", "a" in "Akademi")
print("is ve ==:", [1] == [1], [1] is [1])   # değer eşitliği ve kimlik farkı

# ---------------------------------------------------------------------
baslik("3. Stringler ve f-string")
# ---------------------------------------------------------------------
kurs = "  Python ile Programlama  "
print(kurs.strip().upper())
print(kurs.strip().replace("Python", "C#"))
print(kurs.split())
print("-".join(["2026", "01", "15"]))

fiyat = 12345.6789
print(f"Ad: {ad:<8} | Fiyat: {fiyat:,.2f} TL | Oran: {0.256:.1%}")
print(f"Dilimleme: {kurs.strip()[:6]!r}, {kurs.strip()[-11:]!r}, ters: {ad[::-1]!r}")

# ---------------------------------------------------------------------
baslik("4. Koşullar")
# ---------------------------------------------------------------------
puan = 78
if puan >= 90:
    harf = "AA"
elif puan >= 70:
    harf = "BB"
elif puan >= 50:
    harf = "CC"
else:
    harf = "FF"
print(f"Puan {puan} -> {harf}")

durum = "Geçti" if puan >= 50 else "Kaldı"   # üçlü ifade
print(durum)

# match - case (Python 3.10+)
komut = "durdur"
match komut:
    case "baslat":
        print("Başlatılıyor")
    case "durdur" | "bitir":
        print("Durduruluyor")
    case _:
        print("Bilinmeyen komut")

# ---------------------------------------------------------------------
baslik("5. Döngüler")
# ---------------------------------------------------------------------
for i in range(1, 6):
    print(i, end=" ")
print()

for indeks, meyve in enumerate(["elma", "armut", "kiraz"], start=1):
    print(f"{indeks}. {meyve}")

toplam, n = 0, 1
while n <= 100:
    toplam += n
    n += 1
print("1..100 toplamı:", toplam)

for sayi in range(2, 30):
    if sayi % 2 == 0:
        continue            # çift sayıları atla
    if sayi > 20:
        break               # 20'den büyükse çık
    print(sayi, end=" ")
print()

# for - else: döngü break ile kesilmediyse else çalışır
for n in range(2, 20):
    for bolen in range(2, n):
        if n % bolen == 0:
            break
    else:
        print(f"{n} asaldır", end="; ")
print()

# ---------------------------------------------------------------------
baslik("6. Tip Dönüşümü ve Hata Yakalama")
# ---------------------------------------------------------------------
print(int("42") + 8, float("3.5") * 2, str(100) + " TL", bool(""), bool("a"), list("abc"))

for girdi in ["25", "yirmi", "", "3.7"]:
    try:
        sayi = int(girdi)
        print(f"{girdi!r} -> {sayi}")
    except ValueError as hata:
        print(f"{girdi!r} sayıya çevrilemedi: {hata}")
    finally:
        pass  # finally her durumda çalışır (kaynak temizliği için kullanılır)

try:
    print(10 / 0)
except ZeroDivisionError:
    print("Sıfıra bölme hatası yakalandı.")
