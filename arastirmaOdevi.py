"""
Atatürk Sözleri API (basit versiyon)
Çalıştırma: fastapi dev main.py
Yayınlama:  fastapi deploy

pip install "fastapi[standard]"
fastapi deploy
"""

import random
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Atatürk Sözleri API")

# Sözler basit bir Python listesi
SOZLER = [
    "Hayatta en hakiki mürşit ilimdir, fendir.",
    "Yurtta sulh, cihanda sulh.",
    "Ne mutlu Türküm diyene!",
    "Egemenlik kayıtsız şartsız milletindir.",
    "İstikbal göklerdedir.",
    "Türk, öğün, çalış, güven.",
    "Öğretmenler! Yeni nesil sizin eseriniz olacaktır.",
    "Sanatsız kalan bir milletin hayat damarlarından biri kopmuş demektir.",
    "Zafer, 'Zafer benimdir' diyebilenindir.",
    "Ben sporcunun zeki, çevik ve aynı zamanda ahlaklısını severim.",
]


@app.get("/")
def rastgele_soz():
    # Listeden rastgele bir söz seç ve döndür
    return {"soz": random.choice(SOZLER)}


@app.get("/sozler")
def tum_sozler():
    # Tüm sözleri döndür
    return {"sozler": SOZLER}


@app.get("/sozler/{numara}")
def soz_getir(numara: int):
    # 1'den başlayan numaraya göre söz döndür
    if numara < 1 or numara > len(SOZLER):
        raise HTTPException(status_code=404, detail="Böyle bir söz yok")
    return {"numara": numara, "soz": SOZLER[numara - 1]}