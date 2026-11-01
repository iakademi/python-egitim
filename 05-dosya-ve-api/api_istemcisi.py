"""05 - REST API ile Çalışma

Konular: HTTP istekleri, JSON yanıtı işleme, zaman aşımı, hata yönetimi.

Bu örnek yalnızca standart kütüphaneyi (urllib) kullanır, ek paket gerekmez.
Kullanılan açık test servisi: https://jsonplaceholder.typicode.com
İnternet bağlantısı yoksa program hatayı yakalar ve açıklayıcı mesaj verir.

Çalıştırmak için:  python api_istemcisi.py
"""

import json
import urllib.error
import urllib.parse
import urllib.request

TEMEL_URL = "https://jsonplaceholder.typicode.com"


def istek_at(yol: str, yontem: str = "GET", govde: dict | None = None, zaman_asimi: float = 10.0):
    """Verilen yola istek atar ve JSON yanıtını Python nesnesi olarak döndürür."""
    veri = json.dumps(govde).encode("utf-8") if govde is not None else None
    istek = urllib.request.Request(
        TEMEL_URL + yol,
        data=veri,
        method=yontem,
        headers={"Content-Type": "application/json; charset=utf-8", "Accept": "application/json"},
    )
    with urllib.request.urlopen(istek, timeout=zaman_asimi) as yanit:
        return yanit.status, json.loads(yanit.read().decode("utf-8"))


def kullanicilari_listele() -> list[dict]:
    durum, kullanicilar = istek_at("/users")
    print(f"GET /users -> HTTP {durum}, {len(kullanicilar)} kullanıcı")
    return kullanicilar


def kullanici_gonderileri(kullanici_id: int) -> list[dict]:
    sorgu = urllib.parse.urlencode({"userId": kullanici_id})      # sorgu parametreleri güvenle kodlanır
    durum, gonderiler = istek_at(f"/posts?{sorgu}")
    print(f"GET /posts?{sorgu} -> HTTP {durum}, {len(gonderiler)} gönderi")
    return gonderiler


def gonderi_olustur(baslik: str, icerik: str, kullanici_id: int) -> dict:
    durum, yanit = istek_at(
        "/posts", "POST", {"title": baslik, "body": icerik, "userId": kullanici_id}
    )
    print(f"POST /posts -> HTTP {durum}, sunucunun verdiği id: {yanit.get('id')}")
    return yanit


def main() -> None:
    try:
        kullanicilar = kullanicilari_listele()
        for k in kullanicilar[:3]:
            print(f"  {k['id']}. {k['name']} ({k['email']})")

        gonderiler = kullanici_gonderileri(kullanicilar[0]["id"])
        print("  İlk gönderi başlığı:", gonderiler[0]["title"])

        gonderi_olustur("Python ile API", "urllib ile POST isteği örneği", kullanicilar[0]["id"])

        # Var olmayan kaynak: HTTP 404 beklenir
        istek_at("/posts/999999")
    except urllib.error.HTTPError as hata:
        print(f"Sunucu hata kodu döndürdü: HTTP {hata.code}")
    except urllib.error.URLError as hata:
        print(f"Bağlantı kurulamadı (internet erişimini kontrol edin): {hata.reason}")
    except TimeoutError:
        print("İstek zaman aşımına uğradı.")
    except json.JSONDecodeError:
        print("Yanıt geçerli bir JSON değil.")


if __name__ == "__main__":
    main()
