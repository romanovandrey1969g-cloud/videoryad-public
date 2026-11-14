# -*- coding: utf-8 -*-
"""Карта занятости кадра: где в декорации пусто, а где уже стоит предмет.
Считает РАННЕР (правило 23.10). Результат — zanyato.json, по нему
napoln.py ставит предметы только в свободные места, не загораживая главное.

    python3 zanyato.py zanyato.json
"""
import io, json, sys
import cairosvg
from PIL import Image, ImageFilter
from baza import defs, W, H
from karta import DEK
import lok

OUT = sys.argv[1] if len(sys.argv) > 1 else "zanyato.json"
COL, ROW = 24, 12
SH, VY = 480, 270
res = {}
for nm in sorted(set(DEK.values())):
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d">'
           '<defs>%s</defs>%s</svg>' % (W, H, defs(), getattr(lok, nm)(2.2)))
    buf = io.BytesIO()
    cairosvg.svg2png(bytestring=svg.encode(), write_to=buf,
                     output_width=SH, output_height=VY, unsafe=True)
    im = Image.open(buf).convert("L").filter(ImageFilter.FIND_EDGES)
    px = im.load()
    cw, ch = SH / COL, VY / ROW
    karta = []
    for r in range(ROW):
        stroka = []
        for c in range(COL):
            s = n = 0
            for y in range(int(r * ch) + 1, int((r + 1) * ch) - 1):
                for x in range(int(c * cw) + 1, int((c + 1) * cw) - 1):
                    s += px[x, y]
                    n += 1
            stroka.append(int(s / max(1, n)))
        karta.append(stroka)
    res[nm] = karta
    print(nm, max(max(r) for r in karta), flush=True)
json.dump(res, open(OUT, "w"), separators=(",", ":"))
print("готово:", OUT, len(res))
