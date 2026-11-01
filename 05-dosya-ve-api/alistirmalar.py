"""05 - Dosya ve API: Alıştırmalar ve Çözümleri

Çalıştırmak için:  python alistirmalar.py
Alıştırmalar geçici bir dizin kullanır; ağ bağlantısı gerektirmez.
"""

import csv
import json
import tempfile
from collections import Counter
from pathlib import Path


def alistirma_1_satir_say(yol: Path) -> dict[str, int]:
    """Metin dosyasındaki satır, kelime ve karakter sayısını döndürün."""
    icerik = yol.read_text(encoding="utf-8")
    return {
        "satir": len(icerik.splitlines()),
        "kelime": len(icerik.split()),
        "karakter": len(icerik),
    }


def alistirma_2_csv_sehir_ozeti(yol: Path) -> dict[str, float]:
    """CSV'deki (ad, sehir, not) kayıtlarından şehir bazında not ortalamasını hesaplayın."""
    toplamlar: dict[str, list[int]] = {}
    with open(yol, newline="", encoding="utf-8") as f:
        for satir in csv.DictReader(f):
            toplamlar.setdefault(satir["sehir"], []).append(int(satir["not"]))
    return {sehir: round(sum(n) / len(n), 1) for sehir, n in toplamlar.items()}


def alistirma_3_json_filtrele(girdi: Path, cikti: Path, en_az_not: int) -> int:
    """JSON dosyasındaki öğrenci listesinden notu `en_az_not` ve üzeri olanları
    yeni bir JSON dosyasına yazın; yazılan kayıt sayısını döndürün."""
    ogrenciler = json.loads(girdi.read_text(encoding="utf-8"))
    secilen = [o for o in ogrenciler if o["not"] >= en_az_not]
    cikti.write_text(json.dumps(secilen, ensure_ascii=False, indent=2), encoding="utf-8")
    return len(secilen)


def alistirma_4_log_analizi(satirlar: list[str]) -> Counter:
    """"2026-01-15 10:32:01 ERROR Veritabanına bağlanılamadı" biçimli log
    satırlarında her seviyenin (INFO/WARNING/ERROR) kaç kez geçtiğini sayın."""
    return Counter(satir.split()[2] for satir in satirlar if len(satir.split()) >= 3)


def alistirma_5_guvenli_json_oku(yol: Path, varsayilan: dict | None = None) -> dict:
    """Dosya yoksa ya da JSON bozuksa programı çökertmeden varsayılan değeri döndürün."""
    try:
        return json.loads(yol.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return {} if varsayilan is None else varsayilan


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as gecici:
        klasor = Path(gecici)

        metin = klasor / "metin.txt"
        metin.write_text("Merhaba dünya\nPython çok güzel\n", encoding="utf-8")
        assert alistirma_1_satir_say(metin) == {"satir": 2, "kelime": 5, "karakter": 31}

        csv_yolu = klasor / "notlar.csv"
        csv_yolu.write_text(
            "ad,sehir,not\nElif,İstanbul,90\nCan,Ankara,70\nMerve,İstanbul,80\n", encoding="utf-8"
        )
        assert alistirma_2_csv_sehir_ozeti(csv_yolu) == {"İstanbul": 85.0, "Ankara": 70.0}

        json_girdi = klasor / "girdi.json"
        json_girdi.write_text(
            json.dumps([{"ad": "Elif", "not": 90}, {"ad": "Can", "not": 60}]), encoding="utf-8"
        )
        json_cikti = klasor / "cikti.json"
        assert alistirma_3_json_filtrele(json_girdi, json_cikti, 80) == 1
        assert json.loads(json_cikti.read_text(encoding="utf-8")) == [{"ad": "Elif", "not": 90}]

        loglar = [
            "2026-01-15 10:00:00 INFO Başlatıldı",
            "2026-01-15 10:00:05 ERROR Bağlantı hatası",
            "2026-01-15 10:00:09 ERROR Zaman aşımı",
        ]
        assert alistirma_4_log_analizi(loglar) == Counter({"ERROR": 2, "INFO": 1})

        assert alistirma_5_guvenli_json_oku(klasor / "yok.json") == {}
        (klasor / "bozuk.json").write_text("{", encoding="utf-8")
        assert alistirma_5_guvenli_json_oku(klasor / "bozuk.json", {"varsayilan": True}) == {"varsayilan": True}

    print("Tüm alıştırma çözümleri doğrulandı.")
