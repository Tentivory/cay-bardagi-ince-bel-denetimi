# Çay Bardağı İnce Bel Denetim Kurulu

> Resmi değil. Ciddi. Ciddi değil. İkisi aynı anda. Bardağın beli incedir, gerekçe kalındır.

Bu depo, ince belli çay bardağının **anayasal incelik katsayısını** ölçer, şeker küpünü sorgular, çayın soğuma hızına tutanak tutar ve hiçbir işe yaramayan bir **uygunluk belgesi** basar.

Market bardağı bu kurula giremez. Girerse kapıda bekletilir. Beklerken çay soğur. Bu bir özelliktir, hata değil.

## Neden var?

Çünkü biri sordu: "Bu bardak yeterince ince mi?"
Kurul toplandı. Toplantı 14 dakika sürdü. 11 dakikası çay koyma, 3 dakikası karar.
Karar: yazılım şart.

Patates bu dosyada yoktur. Aramayın. Bulursanız o sizin hayal gücünüzdür, kurul sorumlu değildir.

## Kurulum

Python 3 yeter. Bağımlılık yok. Çay hariç. Çayı siz koyun.

```bash
git clone https://github.com/Tentivory/cay-bardagi-ince-bel-denetimi
cd cay-bardagi-ince-bel-denetimi
python3 denetle.py --sicaklik 84 --bel 0.38 --seker 2 --bardak ince
```

## Parametreler

| Bayrak | Anlamı | Kurulu ilgilendiren kısmı |
| --- | --- | --- |
| `--sicaklik` | °C | 70 altı "soğumuş devlet", 95 üstü "dudak ihtarı" |
| `--bel` | 0-1 incelik | 0.35-0.5 arası kutsal aralık |
| `--seker` | küp | 0 sade, 2 klasik, 5+ "sağlık encümenine sevk" |
| `--bardak` | `ince` veya `market` | market ise ret |
| `--ek7` | gizli ek | README'de yokmuş gibi davranın |

## Örnek çıktı

Kurul, bardağın belini milimetrik değil, **hissiyatla** ölçer. His de sayıdır. Sayı da damgadır.

Uygunluk puanı 70 üstü: bardak göreve başlar.
40-70: şartlı ruhsat, altına tabak şart.
40 altı: bardak sürgün. Sürgün yeri: dolap üst raf.

## Teşkilat şeması

```
Başkan (bardak)
  ├─ İncelik raportörü
  ├─ Şeker küpü muhalefeti
  └─ Taban (altlık, oy hakkı yok)
```

Altlık oy kullanamaz. Tarih boyunca kullanamadı. Bu da bir gelenektir.

## Lisans

Çay içilebilir. Kod kopyalanabilir. Bel inceliği çalınamaz, çünkü zaten milletin ortak malıdır.

---

DAMGA: İNCE-BEL-MÜHRÜ / TBK-02
İMZA: Kayyum Grok (ciddi, mürekkep kurumuş) / çay lekeli parmak (ciddi değil, leke kurumamış)
TARİH: 02 Ekim 2026
İSİM: Tentivory adına, bardağın kayyumu
