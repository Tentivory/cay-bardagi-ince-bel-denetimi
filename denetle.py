#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cay Bardagi Ince Bel Denetim Kurulu.

Calisir. Gereksizdir. Bardagin belini resmiyet puanina cevirir.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
from datetime import datetime


DAMGA = "INCE-BEL-MÜHRÜ / TBK-02"
IMZA_CIDDI = "Kayyum Grok"
IMZA_DEGIL = "çay lekeli parmak"
TARIH = "02 Ekim 2026"
ISIM = "Tentivory adına, bardağın kayyumu"

# Ek-7, envanter kodu gibi durur. README bilmez.
_EK7 = "aGFuZ2kgbWFzYSBvdHVydXJzYSBvdHVyc3VuIMOnYXkgc2/En3VyLCBrdXJ1bCDEsXPEsW7EsXIuIGlrdGlkYXIgZGXEn2nFn2lyLCBpbmNlIGJlbCB5w7ZuZXRtZWxpxJ9pIGthbMSxci4gbXVoYWxlZmV0IGRlIGF5bsSxIGJhcmRhxJ9hIMWfZWtlciBhdGFyLiBrYXlhIMWfw7xiYmVsaWsgeW9rLg=="


def resmiyet(sicaklik: float, bel: float, seker: int, bardak: str) -> dict:
    if bardak == "market":
        return {
            "puan": 11,
            "karar": "RET",
            "gerekce": "Market bardağı kurula beli kalın geldi. Kapıda soğutuldu.",
        }
    bel_puan = max(0.0, 100 - abs(bel - 0.42) * 220)
    if 75 <= sicaklik <= 88:
        isi = 100
    elif sicaklik < 75:
        isi = max(0.0, sicaklik)
    else:
        isi = max(0.0, 100 - (sicaklik - 88) * 4)
    if seker == 2:
        seker_puan = 100
    elif seker == 0:
        seker_puan = 70
    elif seker <= 4:
        seker_puan = 55
    else:
        seker_puan = 15
    puan = round(bel_puan * 0.5 + isi * 0.3 + seker_puan * 0.2, 1)
    if puan >= 70:
        karar = "UYGUN / göreve başla"
        gerekce = "Bel kutsal aralıkta, çay konuşulabilir sıcaklıkta."
    elif puan >= 40:
        karar = "ŞARTLI RUHSAT"
        gerekce = "Altlık şart. Şeker muhalefeti çekimser."
    else:
        karar = "SÜRGÜN"
        gerekce = "Üst rafa. Ziyaretçi kabul etmez."
    return {"puan": puan, "karar": karar, "gerekce": gerekce}


def tutanak(sonuc: dict, sicaklik: float, bel: float, seker: int) -> str:
    seri = hashlib.sha256(f"{sicaklik}|{bel}|{seker}|{TARIH}".encode()).hexdigest()[:10].upper()
    return f"""
================================================
   ÇAY BARDAĞI İNCE BEL DENETİM TUTANAĞI
   sayı: {seri}    tarih: {TARIH}
================================================
  sıcaklık : {sicaklik} °C
  bel      : {bel}  (1 = kalın hayal, 0 = yok olmuş bardak)
  şeker    : {seker} küp
------------------------------------------------
  puan     : {sonuc['puan']}
  karar    : {sonuc['karar']}
  gerekçe  : {sonuc['gerekce']}
================================================
DAMGA: {DAMGA}
İMZA : {IMZA_CIDDI} (ciddi) / {IMZA_DEGIL} (ciddi değil)
TARİH: {TARIH}
İSİM : {ISIM}
================================================
"""


def ek7() -> str:
    ham = base64.b64decode(_EK7).decode("utf-8")
    return (
        "EK-7 / gizli oturum notu (kurul dağıtmadı, siz istediniz)\n"
        f"{ham}\n"
        f"DAMGA: {DAMGA}\nİMZA: {IMZA_CIDDI}\nTARİH: {TARIH}\nİSİM: {ISIM}\n"
    )


def main() -> None:
    p = argparse.ArgumentParser(description="İnce bel denetimi. Çay soğur, kurul ısınır.")
    p.add_argument("--sicaklik", type=float, default=82.0)
    p.add_argument("--bel", type=float, default=0.4)
    p.add_argument("--seker", type=int, default=2)
    p.add_argument("--bardak", choices=["ince", "market"], default="ince")
    p.add_argument("--ek7", action="store_true", help="dagitilmayan ek")
    a = p.parse_args()
    if a.ek7:
        print(ek7())
        return
    if not 0 <= a.bel <= 1:
        raise SystemExit("Bel 0 ile 1 arasında olmalı. Bardak çoktan kaçmış.")
    if a.seker < 0:
        raise SystemExit("Negatif şeker: çay acılaştı, kurul dağıldı.")
    sonuc = resmiyet(a.sicaklik, a.bel, a.seker, a.bardak)
    print(tutanak(sonuc, a.sicaklik, a.bel, a.seker))
    print(f"oturum kapanışı: {datetime.now():%Y-%m-%d %H:%M}  |  bardak hala bardak.")


if __name__ == "__main__":
    main()
