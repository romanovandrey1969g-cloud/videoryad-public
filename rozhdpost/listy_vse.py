# -*- coding: utf-8 -*-
"""Контактные листы ВСЕХ декораций (или всех готовых кадров) — в облаке.
Правило 23.10: ресурсы его машины не трогаем, листы считает раннер.

    python3 listy_vse.py <папка> --dek          # 113 декораций
    python3 listy_vse.py <папка> --kadry        # 171 готовый кадр плана
"""
import argparse, io, os, sys
import cairosvg
from PIL import Image, ImageDraw
from baza import defs, W, H
from karta import DEK
import lok

ap = argparse.ArgumentParser()
ap.add_argument("out")
ap.add_argument("--dek", action="store_true")
ap.add_argument("--kadry", action="store_true")
ap.add_argument("--shir", type=int, default=620)
ap.add_argument("--kol", type=int, default=3)
a = ap.parse_args()
os.makedirs(a.out, exist_ok=True)
TW = a.shir
TH = int(TW * H / W)


def risuy_dek(nm):
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d">'
            '<defs>%s</defs>%s</svg>' % (W, H, defs(), getattr(lok, nm)(2.2)))


def sheet(items, risuy, podpis, path):
    cols = a.kol
    rows = (len(items) + cols - 1) // cols
    L = Image.new("RGB", (cols * TW, rows * (TH + 22)), (18, 18, 22))
    d = ImageDraw.Draw(L)
    for i, it in enumerate(items):
        buf = io.BytesIO()
        cairosvg.svg2png(bytestring=risuy(it).encode(), write_to=buf,
                         output_width=TW, output_height=TH, unsafe=True)
        im = Image.open(buf).convert("RGB")
        x, y = (i % cols) * TW, (i // cols) * (TH + 22)
        L.paste(im, (x, y))
        d.text((x + 6, y + TH + 5), podpis(it), fill=(230, 230, 238))
    L.save(path, quality=86)
    print(path, L.size, flush=True)


NA = 9
if a.dek:
    names = sorted(set(DEK.values()))
    for k in range(0, len(names), NA):
        kus = names[k:k + NA]
        sheet(kus, risuy_dek, lambda nm: nm[:52],
              os.path.join(a.out, "dek-%02d.jpg" % (k // NA + 1)))
if a.kadry:
    import kadr, plan
    P = plan.PLANY
    for k in range(0, len(P), NA):
        kus = P[k:k + NA]
        sheet(kus,
              lambda pl: kadr.body(pl, min(2.2, pl["sek"] * .5), .5, zaglushki=True),
              lambda pl: "%d · %s · %.1fс" % (pl["n"], pl["lok"][:34], pl["sek"]),
              os.path.join(a.out, "kadry-%02d.jpg" % (k // NA + 1)))
