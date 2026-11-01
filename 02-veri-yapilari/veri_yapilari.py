"""02 - Veri Yapıları

Konular: liste, demet (tuple), sözlük, küme, comprehension, sıralama,
         iç içe yapılar, collections modülü.

Çalıştırmak için:  python veri_yapilari.py
"""

from collections import Counter, defaultdict, deque, namedtuple


def baslik(metin: str) -> None:
    print(f"\n=== {metin} ===")


# ---------------------------------------------------------------------
baslik("1. Liste (list) - değiştirilebilir, sıralı")
# ---------------------------------------------------------------------
kurslar = ["Python", "SQL", "C#"]
kurslar.append("Scrum")
kurslar.insert(1, "Excel")
kurslar.extend(["Power BI", "Cisco"])
kurslar.remove("Excel")
silinen = kurslar.pop()          # son elemanı çıkarır
print(kurslar, "| silinen:", silinen)
print("ilk iki:", kurslar[:2], "| ters:", kurslar[::-1], "| sıralı:", sorted(kurslar))
print("uzunluk:", len(kurslar), "| 'SQL' indeksi:", kurslar.index("SQL"))

# ---------------------------------------------------------------------
baslik("2. Demet (tuple) - değiştirilemez")
# ---------------------------------------------------------------------
koordinat = (41.0082, 28.9784)
enlem, boylam = koordinat       # paketten çıkarma
print(f"enlem={enlem}, boylam={boylam}")

Ogrenci = namedtuple("Ogrenci", ["ad", "sehir", "not_"])
o = Ogrenci("Elif", "İstanbul", 90)
print(o, "->", o.ad, o.not_)

# ---------------------------------------------------------------------
baslik("3. Sözlük (dict)")
# ---------------------------------------------------------------------
kisi = {"ad": "Can", "yas": 31, "sehir": "Ankara"}
kisi["meslek"] = "Yazılımcı"
print(kisi.get("telefon", "kayıtlı değil"))      # KeyError yerine varsayılan değer
for anahtar, deger in kisi.items():
    print(f"  {anahtar}: {deger}")

# Metindeki kelime sıklığı
metin = "bir iki üç bir iki bir dört"
sikilik = {}
for kelime in metin.split():
    sikilik[kelime] = sikilik.get(kelime, 0) + 1
print(sikilik)

# Counter ile aynı iş
print(Counter(metin.split()).most_common(2))

# defaultdict ile gruplama
sehirler = [("Elif", "İstanbul"), ("Can", "Ankara"), ("Merve", "İstanbul")]
gruplar = defaultdict(list)
for isim, sehir in sehirler:
    gruplar[sehir].append(isim)
print(dict(gruplar))

# ---------------------------------------------------------------------
baslik("4. Küme (set)")
# ---------------------------------------------------------------------
python_kursu = {"Ali", "Veli", "Ayşe", "Elif"}
sql_kursu = {"Ayşe", "Elif", "Can"}
print("her ikisi    :", sorted(python_kursu & sql_kursu))
print("en az biri   :", sorted(python_kursu | sql_kursu))
print("yalnız Python:", sorted(python_kursu - sql_kursu))
print("simetrik fark:", sorted(python_kursu ^ sql_kursu))
print("tekrarsız liste:", sorted(set([3, 1, 2, 3, 1])))

# ---------------------------------------------------------------------
baslik("5. Comprehension (liste/sözlük/küme üreteçleri)")
# ---------------------------------------------------------------------
kareler = [n ** 2 for n in range(1, 11)]
ciftler = [n for n in kareler if n % 2 == 0]
kare_sozluk = {n: n ** 2 for n in range(1, 6)}
harfler = {h.lower() for h in "Akademi" if h.isalpha()}
print(kareler)
print(ciftler)
print(kare_sozluk)
print(sorted(harfler))

matris = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
duz = [eleman for satir in matris for eleman in satir]
devrik = [list(sutun) for sutun in zip(*matris)]
print("düzleştirilmiş:", duz, "| devrik:", devrik)

# ---------------------------------------------------------------------
baslik("6. Sıralama")
# ---------------------------------------------------------------------
ogrenciler = [
    {"ad": "Elif", "not": 90},
    {"ad": "Can", "not": 72},
    {"ad": "Merve", "not": 90},
    {"ad": "Kaan", "not": 65},
]
# Önce nota göre azalan, eşitlikte ada göre artan
sirali = sorted(ogrenciler, key=lambda o: (-o["not"], o["ad"]))
print([f"{o['ad']}({o['not']})" for o in sirali])
print("en yüksek not:", max(ogrenciler, key=lambda o: o["not"])["ad"])

# ---------------------------------------------------------------------
baslik("7. deque - baştan ve sondan hızlı ekleme/çıkarma")
# ---------------------------------------------------------------------
kuyruk = deque(["Ali", "Veli"])
kuyruk.append("Ayşe")
kuyruk.appendleft("Önce Gelen")
print(kuyruk.popleft(), "->", list(kuyruk))

# ---------------------------------------------------------------------
baslik("8. Kopyalama: sığ (shallow) ve derin (deep)")
# ---------------------------------------------------------------------
import copy

asil = [[1, 2], [3, 4]]
sig = asil.copy()
derin = copy.deepcopy(asil)
asil[0][0] = 99
print("asıl:", asil, "| sığ kopya:", sig, "| derin kopya:", derin)
