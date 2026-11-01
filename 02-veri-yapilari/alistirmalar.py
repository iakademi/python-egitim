"""02 - Veri Yapıları: Alıştırmalar ve Çözümleri

Çalıştırmak için:  python alistirmalar.py
"""

from collections import Counter


def alistirma_1_tekrarsiz_sirali(liste: list[int]) -> list[int]:
    """Listedeki tekrar eden sayıları kaldırıp küçükten büyüğe sıralı döndürün."""
    return sorted(set(liste))


def alistirma_2_anagram(a: str, b: str) -> bool:
    """İki kelimenin birbirinin anagramı olup olmadığını bulun (büyük/küçük harf fark etmez)."""
    return Counter(a.lower()) == Counter(b.lower())


def alistirma_3_en_sik_kelime(metin: str, adet: int = 3) -> list[tuple[str, int]]:
    """Metinde en sık geçen `adet` kelimeyi (kelime, sayı) çiftleri olarak döndürün.
    Noktalama işaretleri yok sayılır."""
    temiz = "".join(h.lower() if h.isalnum() or h.isspace() else " " for h in metin)
    return Counter(temiz.split()).most_common(adet)


def alistirma_4_iki_toplam(sayilar: list[int], hedef: int) -> tuple[int, int] | None:
    """Toplamı `hedef` olan iki elemanın indekslerini döndürün; yoksa None.
    İpucu: sözlükte daha önce görülen sayıları saklayın (O(n))."""
    gorulen: dict[int, int] = {}
    for indeks, sayi in enumerate(sayilar):
        aranan = hedef - sayi
        if aranan in gorulen:
            return gorulen[aranan], indeks
        gorulen[sayi] = indeks
    return None


def alistirma_5_ortak_ogrenciler(kurs_a: list[str], kurs_b: list[str]) -> list[str]:
    """İki kursa da kayıtlı olan öğrencileri alfabetik sıralı döndürün."""
    return sorted(set(kurs_a) & set(kurs_b))


def alistirma_6_matris_toplami(matris: list[list[int]]) -> dict[str, list[int]]:
    """Matrisin satır ve sütun toplamlarını {"satir": [...], "sutun": [...]} olarak döndürün."""
    return {
        "satir": [sum(satir) for satir in matris],
        "sutun": [sum(sutun) for sutun in zip(*matris)],
    }


def alistirma_7_gruplama(kelimeler: list[str]) -> dict[int, list[str]]:
    """Kelimeleri uzunluklarına göre gruplayın: {uzunluk: [kelimeler]}."""
    gruplar: dict[int, list[str]] = {}
    for kelime in kelimeler:
        gruplar.setdefault(len(kelime), []).append(kelime)
    return gruplar


if __name__ == "__main__":
    assert alistirma_1_tekrarsiz_sirali([5, 3, 5, 1, 3]) == [1, 3, 5]
    assert alistirma_2_anagram("Kitap", "pakit") and not alistirma_2_anagram("sql", "sqm")
    assert alistirma_3_en_sik_kelime("Bir, iki! Bir üç; bir iki.", 2) == [("bir", 3), ("iki", 2)]
    assert alistirma_4_iki_toplam([2, 7, 11, 15], 9) == (0, 1)
    assert alistirma_4_iki_toplam([1, 2], 10) is None
    assert alistirma_5_ortak_ogrenciler(["Ali", "Ayşe", "Can"], ["Can", "Ali", "Zeynep"]) == ["Ali", "Can"]
    assert alistirma_6_matris_toplami([[1, 2], [3, 4]]) == {"satir": [3, 7], "sutun": [4, 6]}
    assert alistirma_7_gruplama(["sql", "c#", "git", "python"]) == {3: ["sql", "git"], 2: ["c#"], 6: ["python"]}

    print("En sık kelimeler:", alistirma_3_en_sik_kelime("Python güzel. Python hızlı. SQL güzel.", 2))
    print("Tüm alıştırma çözümleri doğrulandı.")
