"""05 - Dosya İşlemleri

Konular: metin dosyası okuma/yazma, with deyimi, pathlib, CSV, JSON,
         hata yönetimi, geçici dizin kullanımı.

Örnek dosyalar çalışma anında `cikti/` klasörüne yazılır (.gitignore kapsamındadır).

Çalıştırmak için:  python dosya_islemleri.py
"""

import csv
import json
from pathlib import Path

CIKTI = Path(__file__).parent / "cikti"
CIKTI.mkdir(exist_ok=True)


def baslik(metin: str) -> None:
    print(f"\n=== {metin} ===")


# ---------------------------------------------------------------------
baslik("1. Metin Dosyası Yazma ve Okuma")
# ---------------------------------------------------------------------
notlar = CIKTI / "notlar.txt"

# with deyimi dosyayı iş bitince otomatik kapatır. Türkçe karakterler için encoding belirtin.
with open(notlar, "w", encoding="utf-8") as f:
    f.write("Python öğreniyorum.\n")
    f.writelines(["İkinci satır\n", "Üçüncü satır\n"])

with open(notlar, "a", encoding="utf-8") as f:        # "a": sona ekleme
    f.write("Dördüncü satır (eklendi)\n")

with open(notlar, encoding="utf-8") as f:
    for sira, satir in enumerate(f, start=1):         # dosya satır satır gezilir
        print(f"{sira}: {satir.rstrip()}")

print("Tüm içerik uzunluğu:", len(notlar.read_text(encoding="utf-8")), "karakter")

# ---------------------------------------------------------------------
baslik("2. pathlib ile Yol İşlemleri")
# ---------------------------------------------------------------------
print("Ad:", notlar.name, "| Uzantı:", notlar.suffix, "| Gövde:", notlar.stem)
print("Var mı?", notlar.exists(), "| Boyut:", notlar.stat().st_size, "bayt")
print("Dizindeki .txt dosyaları:", [p.name for p in CIKTI.glob("*.txt")])

# ---------------------------------------------------------------------
baslik("3. CSV Okuma ve Yazma")
# ---------------------------------------------------------------------
ogrenciler = [
    {"ad": "Elif", "sehir": "İstanbul", "not": 90},
    {"ad": "Can", "sehir": "Ankara", "not": 72},
    {"ad": "Merve", "sehir": "İstanbul", "not": 85},
]
csv_yolu = CIKTI / "ogrenciler.csv"
with open(csv_yolu, "w", newline="", encoding="utf-8") as f:
    yazici = csv.DictWriter(f, fieldnames=["ad", "sehir", "not"])
    yazici.writeheader()
    yazici.writerows(ogrenciler)

with open(csv_yolu, newline="", encoding="utf-8") as f:
    okunan = list(csv.DictReader(f))
ortalama = sum(int(o["not"]) for o in okunan) / len(okunan)
print(f"{len(okunan)} satır okundu, not ortalaması {ortalama:.1f}")

# ---------------------------------------------------------------------
baslik("4. JSON Okuma ve Yazma")
# ---------------------------------------------------------------------
veri = {
    "kurs": "Python Temelleri",
    "saat": 32,
    "aktif": True,
    "ogrenciler": ogrenciler,
}
json_yolu = CIKTI / "kurs.json"
with open(json_yolu, "w", encoding="utf-8") as f:
    json.dump(veri, f, ensure_ascii=False, indent=2)       # ensure_ascii=False: Türkçe karakterleri korur

with open(json_yolu, encoding="utf-8") as f:
    yuklenen = json.load(f)
print(yuklenen["kurs"], "-", len(yuklenen["ogrenciler"]), "öğrenci")

metin = json.dumps({"a": 1, "b": [1, 2]})                   # dict -> str
print(metin, "->", json.loads(metin)["b"])                  # str -> dict

# ---------------------------------------------------------------------
baslik("5. Hata Yönetimi")
# ---------------------------------------------------------------------
for yol in [notlar, CIKTI / "yok.txt"]:
    try:
        with open(yol, encoding="utf-8") as f:
            print(f"{yol.name}: ilk satır -> {f.readline().strip()}")
    except FileNotFoundError:
        print(f"{yol.name}: dosya bulunamadı.")
    except PermissionError:
        print(f"{yol.name}: erişim izni yok.")

bozuk = CIKTI / "bozuk.json"
bozuk.write_text("{ bu geçerli bir json değil }", encoding="utf-8")
try:
    json.loads(bozuk.read_text(encoding="utf-8"))
except json.JSONDecodeError as hata:
    print("JSON hatası:", hata.msg)
