"""04 - OOP: Alıştırmalar ve Çözümleri

Çalıştırmak için:  python alistirmalar.py
"""

from abc import ABC, abstractmethod
from math import pi


class Sekil(ABC):
    """Alıştırma 1: Soyut Sekil sınıfından Daire ve Dikdortgen türetin;
    her ikisi de alan() ve cevre() metotlarını uygulasın."""

    @abstractmethod
    def alan(self) -> float: ...

    @abstractmethod
    def cevre(self) -> float: ...


class Daire(Sekil):
    def __init__(self, yaricap: float):
        self.yaricap = yaricap

    def alan(self) -> float:
        return pi * self.yaricap ** 2

    def cevre(self) -> float:
        return 2 * pi * self.yaricap


class Dikdortgen(Sekil):
    def __init__(self, en: float, boy: float):
        self.en, self.boy = en, boy

    def alan(self) -> float:
        return self.en * self.boy

    def cevre(self) -> float:
        return 2 * (self.en + self.boy)


class Sepet:
    """Alıştırma 2: Ürün ekleme/çıkarma, toplam hesaplama ve len() desteği olan bir alışveriş sepeti.
    Aynı ürün tekrar eklenirse adedi artmalıdır."""

    def __init__(self):
        self._urunler: dict[str, dict] = {}

    def ekle(self, ad: str, fiyat: float, adet: int = 1) -> None:
        if ad in self._urunler:
            self._urunler[ad]["adet"] += adet
        else:
            self._urunler[ad] = {"fiyat": fiyat, "adet": adet}

    def cikar(self, ad: str) -> None:
        self._urunler.pop(ad, None)

    def toplam(self) -> float:
        return sum(u["fiyat"] * u["adet"] for u in self._urunler.values())

    def __len__(self) -> int:
        return sum(u["adet"] for u in self._urunler.values())


class Yigin:
    """Alıştırma 3: Liste kullanarak LIFO çalışan bir yığın (stack) yazın.
    Boş yığından çıkarma denenirse IndexError fırlatılmalıdır."""

    def __init__(self):
        self._ogeler: list = []

    def ekle(self, oge) -> None:
        self._ogeler.append(oge)

    def cikar(self):
        if not self._ogeler:
            raise IndexError("Yığın boş.")
        return self._ogeler.pop()

    def ust(self):
        return self._ogeler[-1] if self._ogeler else None

    def bos_mu(self) -> bool:
        return not self._ogeler


class Sicaklik:
    """Alıştırma 4: Santigrat değeri saklayan; fahrenheit'ı property olarak hem okuyup hem
    ayarlayabilen sınıf. Mutlak sıfırın (-273.15) altı kabul edilmemelidir."""

    def __init__(self, celsius: float):
        self.celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, deger: float) -> None:
        if deger < -273.15:
            raise ValueError("Mutlak sıfırın altında sıcaklık olamaz.")
        self._celsius = deger

    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, deger: float) -> None:
        self.celsius = (deger - 32) * 5 / 9


if __name__ == "__main__":
    sekiller: list[Sekil] = [Daire(1), Dikdortgen(3, 4)]
    assert round(sekiller[0].alan(), 2) == 3.14
    assert sekiller[1].alan() == 12 and sekiller[1].cevre() == 14

    sepet = Sepet()
    sepet.ekle("kalem", 10, 3)
    sepet.ekle("defter", 25)
    sepet.ekle("kalem", 10)
    assert len(sepet) == 5 and sepet.toplam() == 65
    sepet.cikar("defter")
    assert sepet.toplam() == 40

    y = Yigin()
    y.ekle(1); y.ekle(2)
    assert y.cikar() == 2 and y.ust() == 1 and not y.bos_mu()
    y.cikar()
    try:
        y.cikar()
        raise AssertionError("IndexError bekleniyordu")
    except IndexError:
        pass

    s = Sicaklik(100)
    assert s.fahrenheit == 212
    s.fahrenheit = 32
    assert s.celsius == 0
    try:
        Sicaklik(-300)
        raise AssertionError("ValueError bekleniyordu")
    except ValueError:
        pass

    print("Şekil alanları:", [round(s.alan(), 2) for s in sekiller])
    print("Tüm alıştırma çözümleri doğrulandı.")
