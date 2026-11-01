"""06 - Pandas ile Veri Analizi

Konular: DataFrame oluşturma, CSV okuma, inceleme, seçme/filtreleme, yeni sütun,
         gruplama, pivot tablo, tarih işlemleri, birleştirme (merge), eksik veri,
         sonuçları dosyaya yazma.

Kurulum:     pip install -r ../requirements.txt
Çalıştırmak: python pandas_temelleri.py
"""

from pathlib import Path

import pandas as pd

KLASOR = Path(__file__).parent


def baslik(metin: str) -> None:
    print(f"\n=== {metin} ===")


# ---------------------------------------------------------------------
baslik("1. DataFrame Oluşturma ve CSV Okuma")
# ---------------------------------------------------------------------
kucuk = pd.DataFrame({"ad": ["Elif", "Can", "Merve"], "not": [90, 72, 85]})
print(kucuk)

df = pd.read_csv(KLASOR / "satislar.csv", parse_dates=["tarih"])
print("\nİlk 3 satır:")
print(df.head(3))

# ---------------------------------------------------------------------
baslik("2. Veriyi İnceleme")
# ---------------------------------------------------------------------
print("Boyut (satır, sütun):", df.shape)
print("\nSütun tipleri:")
print(df.dtypes)
print("\nSayısal özet:")
print(df[["adet", "birim_fiyat"]].describe().round(2))
print("\nEksik değer sayıları:", df.isna().sum().sum())

# ---------------------------------------------------------------------
baslik("3. Yeni Sütun, Seçme ve Filtreleme")
# ---------------------------------------------------------------------
df["tutar"] = df["adet"] * df["birim_fiyat"]
df["ay"] = df["tarih"].dt.month

print("Tek sütun:", df["urun"].unique().tolist())
print("\nİstanbul'daki 1000 TL üzeri siparişler:")
print(df.loc[(df["sehir"] == "İstanbul") & (df["tutar"] > 1000), ["siparis_id", "urun", "tutar"]])

print("\nKategori Yazılım veya Aksesuar olanların sayısı:",
      df["kategori"].isin(["Yazılım", "Aksesuar"]).sum())
print("\nEn yüksek tutarlı 3 sipariş:")
print(df.nlargest(3, "tutar")[["siparis_id", "sehir", "urun", "tutar"]])

# ---------------------------------------------------------------------
baslik("4. Gruplama ve Özetleme")
# ---------------------------------------------------------------------
kategori_ozet = df.groupby("kategori")["tutar"].agg(["count", "sum", "mean"]).round(2)
print(kategori_ozet.sort_values("sum", ascending=False))

sehir_ozet = (
    df.groupby("sehir")
    .agg(siparis_sayisi=("siparis_id", "count"), toplam_tutar=("tutar", "sum"), toplam_adet=("adet", "sum"))
    .sort_values("toplam_tutar", ascending=False)
)
print("\n", sehir_ozet)

# ---------------------------------------------------------------------
baslik("5. Pivot Tablo")
# ---------------------------------------------------------------------
pivot = df.pivot_table(index="sehir", columns="kategori", values="tutar", aggfunc="sum", fill_value=0)
print(pivot)

# ---------------------------------------------------------------------
baslik("6. Tarih İşlemleri")
# ---------------------------------------------------------------------
aylik = df.groupby("ay")["tutar"].sum()
print("Aylık ciro:")
print(aylik)
print("\nAylık değişim (%):")
print((aylik.pct_change() * 100).round(1))
print("\nHaftanın günlerine göre sipariş sayısı:")
print(df["tarih"].dt.day_name().value_counts())

# ---------------------------------------------------------------------
baslik("7. Birleştirme (merge)")
# ---------------------------------------------------------------------
yoneticiler = pd.DataFrame({
    "sehir": ["İstanbul", "Ankara", "İzmir"],       # Bursa için kayıt yok
    "bolge": ["Marmara", "İç Anadolu", "Ege"],
})
birlesik = df.merge(yoneticiler, on="sehir", how="left")
print("Bölge bilgisi olmayan satır sayısı:", birlesik["bolge"].isna().sum())
birlesik["bolge"] = birlesik["bolge"].fillna("Diğer")       # eksik veriyi doldurma
print(birlesik.groupby("bolge")["tutar"].sum())

# ---------------------------------------------------------------------
baslik("8. Sonuçları Kaydetme")
# ---------------------------------------------------------------------
cikti_klasoru = KLASOR / "cikti"
cikti_klasoru.mkdir(exist_ok=True)
sehir_ozet.to_csv(cikti_klasoru / "sehir_ozet.csv", encoding="utf-8-sig")   # Excel'de Türkçe karakterler düzgün açılır
print("Kaydedildi:", (cikti_klasoru / "sehir_ozet.csv").name)
