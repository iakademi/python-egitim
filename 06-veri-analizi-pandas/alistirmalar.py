"""06 - Pandas: Alıştırmalar ve Çözümleri

Aynı klasördeki satislar.csv dosyası kullanılır.

Çalıştırmak için:  python alistirmalar.py
"""

from pathlib import Path

import pandas as pd

KLASOR = Path(__file__).parent


def veriyi_yukle() -> pd.DataFrame:
    df = pd.read_csv(KLASOR / "satislar.csv", parse_dates=["tarih"])
    df["tutar"] = df["adet"] * df["birim_fiyat"]
    return df


def alistirma_1_toplam_ciro(df: pd.DataFrame) -> float:
    """Tüm siparişlerin toplam tutarını döndürün."""
    return float(df["tutar"].sum())


def alistirma_2_en_cok_satan_urun(df: pd.DataFrame) -> tuple[str, int]:
    """Toplam adedi en yüksek ürünü ve adedini (urun, adet) olarak döndürün."""
    adetler = df.groupby("urun")["adet"].sum()
    return adetler.idxmax(), int(adetler.max())


def alistirma_3_sehir_ortalamasi(df: pd.DataFrame) -> pd.Series:
    """Şehir bazında sipariş başına ortalama tutarı (azalan sırada, 2 basamak) döndürün."""
    return df.groupby("sehir")["tutar"].mean().round(2).sort_values(ascending=False)


def alistirma_4_yuksek_siparisler(df: pd.DataFrame, esik: float) -> pd.DataFrame:
    """Tutarı eşiğin üzerinde olan siparişleri tutara göre azalan sırada döndürün."""
    return df[df["tutar"] > esik].sort_values("tutar", ascending=False)


def alistirma_5_mart_sonrasi_kategori(df: pd.DataFrame) -> pd.Series:
    """1 Mart 2026 ve sonrasındaki siparişlerin kategori bazında toplam tutarını döndürün."""
    return df[df["tarih"] >= "2026-03-01"].groupby("kategori")["tutar"].sum()


def alistirma_6_kumulatif_ciro(df: pd.DataFrame) -> pd.Series:
    """Aylık cironun kümülatif (birikimli) toplamını ay numarasıyla döndürün."""
    return df.groupby(df["tarih"].dt.month)["tutar"].sum().cumsum()


if __name__ == "__main__":
    veri = veriyi_yukle()
    assert len(veri) == 20

    toplam = alistirma_1_toplam_ciro(veri)
    assert round(toplam, 2) == 34053.0

    assert alistirma_2_en_cok_satan_urun(veri) == ("Mouse Pad", 15)

    sehirler = alistirma_3_sehir_ortalamasi(veri)
    assert sehirler.index[0] == "İstanbul"

    yuksek = alistirma_4_yuksek_siparisler(veri, 4000)
    assert yuksek["siparis_id"].tolist() == [1012, 1004]

    mart = alistirma_5_mart_sonrasi_kategori(veri)
    assert set(mart.index) == {"Aksesuar", "Donanım", "Yazılım"}

    kumulatif = alistirma_6_kumulatif_ciro(veri)
    assert kumulatif.iloc[-1] == toplam and kumulatif.is_monotonic_increasing

    print(f"Toplam ciro: {toplam:,.2f} TL")
    print("En çok satan ürün:", alistirma_2_en_cok_satan_urun(veri))
    print("Tüm alıştırma çözümleri doğrulandı.")
