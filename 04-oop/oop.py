"""04 - Nesne Yönelimli Programlama (OOP)

Konular: sınıf, __init__, özellikler (property), kalıtım, soyut sınıf,
         özel metotlar (dunder), sınıf/statik metot, dataclass, kompozisyon.

Çalıştırmak için:  python oop.py
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field


def baslik(metin: str) -> None:
    print(f"\n=== {metin} ===")


# ---------------------------------------------------------------------
baslik("1. Sınıf, Kapsülleme ve property")
# ---------------------------------------------------------------------
class BankaHesabi:
    faiz_orani = 0.05                       # sınıf değişkeni: tüm nesneler paylaşır

    def __init__(self, sahip: str, bakiye: float = 0.0):
        self.sahip = sahip                  # örnek değişkeni
        self._bakiye = bakiye               # _ ile başlayan: "dışarıdan dokunma" uyarısı

    @property
    def bakiye(self) -> float:              # yalnızca okunabilir özellik
        return self._bakiye

    def yatir(self, tutar: float) -> None:
        if tutar <= 0:
            raise ValueError("Tutar pozitif olmalıdır.")
        self._bakiye += tutar

    def cek(self, tutar: float) -> None:
        if tutar > self._bakiye:
            raise ValueError("Yetersiz bakiye.")
        self._bakiye -= tutar

    def __str__(self) -> str:               # print() için okunabilir gösterim
        return f"{self.sahip}: {self._bakiye:,.2f} TL"

    def __repr__(self) -> str:              # geliştirici için gösterim
        return f"BankaHesabi(sahip={self.sahip!r}, bakiye={self._bakiye})"


hesap = BankaHesabi("Zeynep", 1000)
hesap.yatir(500)
hesap.cek(300)
print(hesap, "|", repr(hesap))
try:
    hesap.cek(10_000)
except ValueError as hata:
    print("Hata:", hata)

# ---------------------------------------------------------------------
baslik("2. Kalıtım ve Polimorfizm")
# ---------------------------------------------------------------------
class Calisan(ABC):
    def __init__(self, ad: str, maas: float):
        self.ad = ad
        self.maas = maas

    @abstractmethod
    def aylik_ucret(self) -> float:         # alt sınıflar uygulamak zorundadır
        ...

    def tanit(self) -> str:
        return f"{type(self).__name__}: {self.ad} - {self.aylik_ucret():,.0f} TL"


class Egitmen(Calisan):
    def __init__(self, ad: str, maas: float, uzmanlik: str):
        super().__init__(ad, maas)          # üst sınıfın kurucusunu çağırır
        self.uzmanlik = uzmanlik

    def aylik_ucret(self) -> float:
        return self.maas + 2500


class Yonetici(Calisan):
    def __init__(self, ad: str, maas: float, ekip_sayisi: int):
        super().__init__(ad, maas)
        self.ekip_sayisi = ekip_sayisi

    def aylik_ucret(self) -> float:
        return self.maas + self.ekip_sayisi * 1000


ekip = [Egitmen("Ahmet", 30000, "Python"), Yonetici("Selin", 45000, 4)]
for kisi in ekip:
    print(kisi.tanit())                     # her nesne kendi aylik_ucret'ini çağırır
print("Toplam maliyet:", sum(k.aylik_ucret() for k in ekip))
print("isinstance:", isinstance(ekip[0], Calisan), "| issubclass:", issubclass(Yonetici, Calisan))

try:
    Calisan("Soyut", 1)                     # soyut sınıftan nesne üretilemez
except TypeError as hata:
    print("Hata:", hata)

# ---------------------------------------------------------------------
baslik("3. Özel Metotlar (dunder) ile Operatör Tanımlama")
# ---------------------------------------------------------------------
class Vektor:
    def __init__(self, x: float, y: float):
        self.x, self.y = x, y

    def __add__(self, diger: "Vektor") -> "Vektor":
        return Vektor(self.x + diger.x, self.y + diger.y)

    def __mul__(self, katsayi: float) -> "Vektor":
        return Vektor(self.x * katsayi, self.y * katsayi)

    def __eq__(self, diger: object) -> bool:
        return isinstance(diger, Vektor) and (self.x, self.y) == (diger.x, diger.y)

    def __abs__(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __len__(self) -> int:
        return 2

    def __repr__(self) -> str:
        return f"Vektor({self.x}, {self.y})"


v1, v2 = Vektor(3, 4), Vektor(1, 2)
print(v1 + v2, v1 * 2, abs(v1), v1 == Vektor(3, 4), len(v1))

# ---------------------------------------------------------------------
baslik("4. classmethod ve staticmethod")
# ---------------------------------------------------------------------
class Kurs:
    def __init__(self, ad: str, saat: int):
        self.ad, self.saat = ad, saat

    @classmethod
    def metinden(cls, metin: str) -> "Kurs":
        """'Python-32' biçimindeki metinden nesne üretir (alternatif kurucu)."""
        ad, saat = metin.split("-")
        return cls(ad, int(saat))

    @staticmethod
    def gun_hesapla(saat: int, gunluk_saat: int = 8) -> int:
        """Nesneye ya da sınıfa ihtiyaç duymayan yardımcı fonksiyon."""
        return -(-saat // gunluk_saat)      # yukarı yuvarlama

    def __repr__(self) -> str:
        return f"Kurs({self.ad!r}, {self.saat})"


k = Kurs.metinden("Python-32")
print(k, "->", Kurs.gun_hesapla(k.saat), "gün")

# ---------------------------------------------------------------------
baslik("5. dataclass")
# ---------------------------------------------------------------------
@dataclass(order=True)
class Ogrenci:
    ad: str
    not_ortalamasi: float = 0.0
    kurslar: list[str] = field(default_factory=list)

    def kurs_ekle(self, kurs: str) -> None:
        self.kurslar.append(kurs)


o1 = Ogrenci("Elif", 90.5)
o1.kurs_ekle("Python")
o2 = Ogrenci("Can", 72.0, ["SQL"])
print(o1, "|", o1 == Ogrenci("Elif", 90.5, ["Python"]), "|", sorted([o1, o2])[0].ad)

# ---------------------------------------------------------------------
baslik("6. Kompozisyon (has-a ilişkisi) ve iterator protokolü")
# ---------------------------------------------------------------------
class Sinif:
    """Bir sınıf (grup) birden fazla öğrenci içerir; kalıtım yerine kompozisyon kullanır."""

    def __init__(self, ad: str):
        self.ad = ad
        self._ogrenciler: list[Ogrenci] = []

    def ekle(self, ogrenci: Ogrenci) -> None:
        self._ogrenciler.append(ogrenci)

    def __iter__(self):
        return iter(self._ogrenciler)       # for döngüsüyle gezilebilir yapar

    def __len__(self) -> int:
        return len(self._ogrenciler)

    def ortalama(self) -> float:
        return sum(o.not_ortalamasi for o in self) / len(self)


grup = Sinif("Python Akşam Grubu")
grup.ekle(o1)
grup.ekle(o2)
for ogr in grup:
    print(" -", ogr.ad, ogr.not_ortalamasi)
print(f"{grup.ad}: {len(grup)} öğrenci, ortalama {grup.ortalama():.2f}")
