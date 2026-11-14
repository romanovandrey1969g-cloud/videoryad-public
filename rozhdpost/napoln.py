# -*- coding: utf-8 -*-
"""НАПОЛНЕНИЕ ДЕКОРАЦИЙ ПРЕДМЕТАМИ (R-0045, его слово 14.11.2026).

Куда ставить — решает не глазомер, а карта занятости кадра (zanyato.json):
предметы ложатся ТОЛЬКО в пустые клетки, главное в кадре не загораживают.
Тип фона (кухня, изба, погреб, улица) берётся из исходника самой декорации.

Снять наполнение у отдельной сцены — строка в БЕЗ_НАПОЛНЕНИЯ.
"""
import inspect, json, os, random
import lok, veshchi as V
from baza import SL, Z_SRED, Z_PERED, W, H

HERE = os.path.dirname(os.path.abspath(__file__))
COL, ROW = 24, 12
CW, CH = W / COL, H / ROW
_Z = {}
_f = os.path.join(HERE, "zanyato.json")
if os.path.exists(_f):
    _Z = json.load(open(_f, encoding="utf-8"))

# сцены, которые наполнять НЕЛЬЗЯ: крупный план предмета, надпись во весь кадр
BEZ_NAPOLNENIYA = {
    "detskaya_tarelka_s_nadpisyu_na_dne", "korotkiy_chek_i_sdacha",
    "listok_naznacheniya_i_ochki", "tolstaya_kniga_s_zastezhkami",
    "miska_sochiva_krupno", "zolotoy_luk_na_kashe", "sorok_misok_i_klyaksa",
    "oreh_v_dvernoy_scheli", "mandarin_i_kozhura_spiralyu",
    "dve_snezhnye_lesenki_ryadom", "shest_snezhnyh_stupeney",
    "tri_nosa_na_stekle", "pesochnye_chasy_na_podokonnike",
    "lozhka_i_chelovechki", "lesenka_pamyatka_na_stene", "krytyy_rynok",
}


def _tip(imya):
    """Тип фона декорации — по тому, из чего она собрана."""
    try:
        src = inspect.getsource(getattr(lok, imya))
    except Exception:
        return "komnata"
    if "ulica_dal" in src or "izba_snaruzhi" in src or "sneg_lezhit" in src \
            or "panelka" in src or 'nebo("noch"' in src or "nebo(" in src:
        return "ulica"
    if "kuhnya_stena" in src or "kuhnya_utvar" in src:
        return "kuhnya"
    if "kladka" in src or "svody" in src:
        return "pogreb"
    if "brevna" in src:
        return "izba"
    return "komnata"


GEOM = {            # пол (низ предмета), допустимые ряды стены
    "kuhnya": (1035, (2, 5)),
    "izba":   (1030, (2, 5)),
    "komnata": (1030, (2, 5)),
    "pogreb": (1000, (3, 6)),
    "ulica":  (900,  None),
}


def _svobod(karta, r0, r1, porog=11):
    """Столбцы, где в рядах r0..r1 пусто (с поправкой на виньетку ряда)."""
    sv = []
    for c in range(COL):
        ok = True
        for r in range(r0, r1 + 1):
            if r >= len(karta):
                continue
            fon = min(karta[r])
            if karta[r][c] > fon + porog:
                ok = False
                break
        sv.append(ok)
    return sv


def _polosy(sv, mini=3):
    """Непрерывные полосы свободных столбцов длиной не меньше mini."""
    out, n = [], 0
    for c in range(COL + 1):
        if c < COL and sv[c]:
            n += 1
        else:
            if n >= mini:
                out.append((c - n, n))
            n = 0
    out.sort(key=lambda p: -p[1])
    return out


def dobavit(imya, t):
    """Что доложить в декорацию: группы предметов в пустых местах кадра."""
    if imya in BEZ_NAPOLNENIYA or imya not in _Z:
        return ""
    karta = _Z[imya]
    tip = _tip(imya)
    pol, steny = GEOM.get(tip, GEOM["komnata"])
    sd = sum(ord(c) for c in imya)
    r = random.Random(sd)
    out = ""
    gruppy = 0
    zanyato_vidov = set()          # один вид — один раз на сцену

    # 1. ПОЛ (или земля): корзины, мешки, вёдра, поленница, сани
    br = int(pol / CH)                      # ряд, в котором стоит низ предмета
    polosy = _polosy(_svobod(karta, max(0, br - 2), br - 1), 3)
    if polosy:
        c0, n = polosy[0]
        x = max(56, c0 * CW + 14)
        w_ = min((c0 + n) * CW - 28, W - 56) - x
        if tip == "ulica":
            sp = V.nabor(V.DVOR_VIDY, sd, min(3, max(2, n // 4)), zanyato_vidov)
            zanyato_vidov |= set(sp)
            out += SL(Z_PERED, V.dvor_veshchi(x, pol, w_, t, sd, len(sp), sp))
            out += SL(Z_PERED, V.sled_v_snegu(x + 20, pol + 30, w_ - 40, 5, .4))
        else:
            sp = V.nabor(V.POL_VIDY, sd, min(4, max(2, n // 3)), zanyato_vidov)
            zanyato_vidov |= set(sp)
            out += SL(Z_PERED, V.pod_stolom(x, pol, w_, t, sd, len(sp), sp))
        gruppy += 1
        if len(polosy) > 1 and polosy[1][1] >= 4 and tip != "ulica":
            c0, n = polosy[1]
            sp = V.nabor(V.POL_VIDY, sd + 7, min(3, max(2, n // 4)), zanyato_vidov)
            zanyato_vidov |= set(sp)
            out += SL(Z_PERED, V.pod_stolom(c0 * CW + 14, pol, n * CW - 28, t,
                                            sd + 7, len(sp), sp))
            gruppy += 1

    # 2. СТЕНА: пучки трав, связки, доска, сито, рушник, рамка
    if steny:
        r0, r1 = steny
        polosy = _polosy(_svobod(karta, r0, r1), 3)
        if polosy:
            c0, n = polosy[0]
            x, w_ = c0 * CW + 20, n * CW - 40
            if n >= 7 and r.random() < .55:
                out += SL(Z_SRED, V.polka_veshchey(x, r1 * CH + 40, w_, t, sd,
                                                   dve=n >= 9))
            else:
                sp = V.nabor(V.STENA_VIDY, sd, min(4, max(2, n // 3)), zanyato_vidov)
                zanyato_vidov |= set(sp)
                out += SL(Z_SRED, V.stena_nabor(x, r0 * CH + 30, w_, t, sd,
                                                len(sp), sp))
            gruppy += 1
            if len(polosy) > 1 and polosy[1][1] >= 4 and gruppy < 3:
                c0, n = polosy[1]
                sp = V.nabor(V.STENA_VIDY, sd + 3, min(3, max(2, n // 4)), zanyato_vidov)
                zanyato_vidov |= set(sp)
                out += SL(Z_SRED, V.stena_nabor(c0 * CW + 20, r0 * CH + 30,
                                                n * CW - 40, t, sd + 3, len(sp), sp))
                gruppy += 1

    # 3. ПОТОЛОК: вязки грибов и трав — только в избе и на кухне
    if gruppy < 3 and tip in ("kuhnya", "izba", "pogreb"):
        polosy = _polosy(_svobod(karta, 0, 1), 4)
        if polosy:
            c0, n = polosy[0]
            out += SL(Z_SRED, V.pod_potolkom(c0 * CW + 24, 0, n * CW - 48, t,
                                             sd + 11, min(3, max(2, n // 4))))
    return out


def scena(imya, t):
    """Декорация ВМЕСТЕ с наполнением — единая дверь для кадра и для листов."""
    return getattr(lok, imya)(t) + dobavit(imya, t)
