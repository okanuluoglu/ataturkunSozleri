# Atatürk Sözleri API 🇹🇷

Mustafa Kemal Atatürk'ün sözlerini döndüren REST API. [kanye.rest](https://kanye.rest)'ten ilham alınmıştır. FastAPI ile geliştirilmiş, FastAPI Cloud üzerinde yayınlanmak üzere hazırlanmıştır.

## Endpoint'ler

| Metod | Yol | Açıklama |
|-------|-----|----------|
| GET | `/` | Rastgele bir söz döndürür (kanye.rest tarzı) |
| GET | `/sozler` | Tüm sözleri listeler (`?kategori=eğitim` ile filtrelenebilir) |
| GET | `/sozler/rastgele` | Rastgele bir sözü id ve kategorisiyle döndürür |
| GET | `/sozler/{id}` | ID'ye göre söz döndürür (yoksa 404) |
| GET | `/kategoriler` | Tüm kategorileri listeler |

Örnek cevap (`GET /`):

```json
{ "soz": "Hayatta en hakiki mürşit ilimdir, fendir." }
```

## Lokal Çalıştırma

```bash
# 1. Sanal ortam oluştur ve aktive et
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Linux / Mac

# 2. Bağımlılıkları kur (FastAPI Cloud CLI da bununla birlikte gelir)
pip install "fastapi[standard]"

# 3. Geliştirme sunucusunu başlat
fastapi dev main.py
```

Tarayıcıdan test:
- API: http://127.0.0.1:8000
- İnteraktif dokümantasyon (Swagger): http://127.0.0.1:8000/docs

## FastAPI Cloud'a Yayınlama

1. https://fastapicloud.com adresinden hesap oluştur (hesabın yoksa ilk `fastapi deploy` sırasında waitlist'e katılma seçeneği de çıkıyor).

2. Proje klasöründeyken tek komut yeter:

```bash
fastapi deploy
```

- Giriş yapmadıysan tarayıcı açılır, giriş yaparsın (`fastapi login` ile önceden de yapabilirsin).
- CLI uygulamayı otomatik algılar, deploy eder ve sana `https://<uygulama-adi>.fastapicloud.dev` gibi bir URL verir.
- İlk deploy sonrası klasörde `.fastapicloud` dizini oluşur; sonraki güncellemelerde yine sadece `fastapi deploy` çalıştırman yeterli.

3. Verilen URL'yi ve `/docs` sayfasını ödev tesliminde paylaşabilirsin.

## Dosya Yapısı

```
ataturk-sozleri-api/
├── main.py            # API kodu (endpoint'ler + veri)
├── requirements.txt   # Bağımlılıklar
└── README.md          # Bu dosya
```