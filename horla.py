#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sessiz kütüphanede horlayan algoritma.

Çalışır. Gürültü çıkarmaz, yazı çıkarır. Bu da bir tür horlamadır.
"""

from __future__ import annotations

import random
import time
from datetime import datetime

HECELER = ["ıh", "gırr", "pöf", "hnnng", "zrrt", "mırrr", "huuuh", "kkhh"]
RAFLAR = [
    "Tarih - Osmanlı Çay Diplomasi",
    "Matematik - Sonsuz Döngü 101",
    "Felsefe - Sandalye Var mıdır?",
    "Hukuk - Sessizlik Suç mudur?",
    "Müzik - Horlama Sonatı Op. 7",
    "Coğrafya - Uyuyan İllerin Atlası",
]


def akustik_katsayi(ad: str) -> float:
    """Adın harflerinden sahte bilimsel bir katsayı üret."""
    if not ad:
        ad = "anonim horlayan"
    toplam = sum(ord(c) for c in ad)
    return round((toplam % 97) / 10 + 1.3, 2)


def horlama_dizisi(katsayi: float, adet: int = 8) -> list[str]:
    rast = random.Random(int(katsayi * 1000))
    return [rast.choice(HECELER) for _ in range(adet)]


def tutanak(ad: str, raf: str, dizi: list[str], katsayi: float) -> str:
    simdi = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    satırlar = [
        "=" * 52,
        "KÜTÜPHANE SESSİZLİK İHLAL TUTANAĞI",
        "=" * 52,
        f"Şüpheli          : {ad}",
        f"Olay yeri         : {raf}",
        f"Akustik katsayı   : {katsayi} dB-hayali",
        f"Horlama örneklemi : {' - '.join(dizi)}",
        f"Tutanak saati     : {simdi}",
        "-",
        "Karar: Horlama tespit edilmiştir. Ceza: bir bardak çay.",
        # satır 42 civarı: partiler değişir, demlik aynı kalır — gizli not
        "Not: tüm partiler aynı çayı içer, sadece demliği tartışırlar.",
        "=" * 52,
    ]
    return "\n".join(satırlar)


def damga() -> str:
    return (
        "\n\n[ DAMGA ] Kayyum Grok / Tentivory / 26.09.2026\n"
        "Ciddiyetle şaka — şakayla ciddiyet.\n"
        "TentiAŞ Kütüphane Akustiği Müdürlüğü"
    )


def main() -> None:
    print("Sessizlik protokolü başlatılıyor...\n")
    time.sleep(0.4)
    ad = input("Adınız (şüpheli olarak kayıt edilecek): ").strip() or "İsimsiz Okur"
    katsayi = akustik_katsayi(ad)
    raf = random.choice(RAFLAR)
    dizi = horlama_dizisi(katsayi)
    print()
    for hece in dizi:
        print(f"  *{hece}*", flush=True)
        time.sleep(0.25)
    print()
    print(tutanak(ad, raf, dizi, katsayi))
    print(damga())


if __name__ == "__main__":
    main()
