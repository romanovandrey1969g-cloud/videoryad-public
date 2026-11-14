# -*- coding: utf-8 -*-
"""НАПОЛНЕНИЕ СЦЕНЫ ПРЕДМЕТАМИ — правило R-0045.

Его слово 14.11.2026 по «Рождественскому посту»: «Во многих сценах надо
больше предметов на сцену. Совсем пустенько, совсем».

Здесь живут не отдельные вещи, а ГРУППЫ: стол с натюрмортом, обжитая стена,
полка со скарбом, угол с мебелью, двор с поленницей. Каждая группа сама
разная по seed — один и тот же набор в шести сценах подряд читается как одна
декорация (R-0021). У каждого предмета контур, градиент и тень (R-0017).
"""
import math, random
import anim as A
from baza import (o, ten, teplo, krynka, karavay, kot, kura, monety, hodiki,
                  svecha, lampa, par, dym, kartoshka, ryabina, siluet,
                  K, KREM, RUSH, TKAN, TKAN2, ZEL, ZEL2, TRAVA, CHUGUN,
                  ZHELEZ, SNEG, INEY, SVET, ZOL, MED, DOSKA, DOSKA2, POL2,
                  ORA, KRAS, SERO, BREVNO2, W, H)


# ── мелкие предметы на поверхности ─────────────────────────────────────────
def _miska(x, y, s_=1.0, soderzh=None):
    """Миска с содержимым: каша, суп, картошка, капуста."""
    w_ = 108 * s_
    out = ten(x, y + 8 * s_, w_ * .62, 12 * s_, .42)
    out += (f'<path d="M{x-w_/2:.0f},{y-54*s_:.0f} q{w_/2:.0f},{76*s_:.0f} {w_:.0f},0 Z"'
            f' fill="url(#glina)" {o(max(4,6*s_))}/>')
    if soderzh:
        col = {"kasha": "#e0c288", "sup": "#cf9b4a", "kapusta": "#dde5c4",
               "kartoshka": "#d6b06a", "testo": "#f1e4c4"}.get(soderzh, "#e0c288")
        out += (f'<ellipse cx="{x:.0f}" cy="{y-50*s_:.0f}" rx="{w_*.44:.0f}"'
                f' ry="{14*s_:.0f}" fill="{col}" {o(max(3,4*s_))}/>')
    out += (f'<path d="M{x-w_*.42:.0f},{y-44*s_:.0f} q{w_*.18:.0f},{14*s_:.0f} {w_*.34:.0f},{2*s_:.0f}"'
            f' fill="none" stroke="#ffffff" stroke-width="{5*s_:.0f}" opacity=".45"/>')
    return out


def _kruzhka(x, y, s_=1.0, col="url(#krem)"):
    w_, h_ = 62 * s_, 74 * s_
    return (ten(x, y + 6 * s_, w_ * .56, 10 * s_, .4)
            + f'<path d="M{x-w_/2:.0f},{y-h_:.0f} h{w_:.0f} l-6,{h_:.0f} h{-w_+12:.0f} Z"'
              f' fill="{col}" {o(max(4,5*s_))}/>'
            + f'<path d="M{x+w_/2-6:.0f},{y-h_*.78:.0f} q{26*s_:.0f},{h_*.26:.0f} {-4*s_:.0f},{h_*.48:.0f}"'
              f' fill="none" stroke="{K}" stroke-width="{max(4,6*s_):.0f}"/>')


def _banka(x, y, s_=1.0, col="#8a6038"):
    w_, h_ = 72 * s_, 96 * s_
    return (ten(x, y + 6 * s_, w_ * .56, 9 * s_, .38)
            + f'<rect x="{x-w_/2:.0f}" y="{y-h_:.0f}" width="{w_:.0f}" height="{h_:.0f}"'
              f' rx="{10*s_:.0f}" fill="url(#stekl)" {o(max(4,5*s_))}/>'
            + f'<rect x="{x-w_/2:.0f}" y="{y-h_:.0f}" width="{w_:.0f}" height="{16*s_:.0f}"'
              f' rx="{5*s_:.0f}" fill="{ZHELEZ}" {o(max(3,4*s_))}/>'
            + f'<ellipse cx="{x:.0f}" cy="{y-h_*.42:.0f}" rx="{w_*.33:.0f}"'
              f' ry="{h_*.3:.0f}" fill="{col}" opacity=".85"/>')


def _hleb(x, y, s_=1.0):
    return karavay(x, y, .5 * s_, False)


def _luk(x, y, s_=1.0, n=3, col="url(#solom)"):
    out = ten(x, y + 6 * s_, 48 * s_, 9 * s_, .35)
    for i in range(n):
        xx = x - (n - 1) * 20 * s_ / 2 + i * 20 * s_
        out += (f'<ellipse cx="{xx:.0f}" cy="{y-24*s_:.0f}" rx="{24*s_:.0f}"'
                f' ry="{26*s_:.0f}" fill="{col}" {o(max(3,4*s_))}/>'
                f'<path d="M{xx:.0f},{y-48*s_:.0f} l{-6*s_:.0f},{-18*s_:.0f}"'
                f' stroke="#8a9a58" stroke-width="{4*s_:.0f}" fill="none"/>')
    return out


def _solonka(x, y, s_=1.0):
    return (ten(x, y + 4 * s_, 24 * s_, 6 * s_, .35)
            + f'<path d="M{x-20*s_:.0f},{y:.0f} l4,{-42*s_:.0f} h{32*s_:.0f} l4,{42*s_:.0f} Z"'
              f' fill="url(#derev)" {o(max(3,4*s_))}/>'
            + f'<ellipse cx="{x:.0f}" cy="{y-42*s_:.0f}" rx="{18*s_:.0f}"'
              f' ry="{6*s_:.0f}" fill="#f3ead6" {o(max(3,3*s_))}/>')
def _lozhki(x, y, s_=1.0):
    """Пучок ложек в кружке — всегда читается как кухня."""
    out = _kruzhka(x, y, s_ * .9, "url(#glina)")
    for i, ug in enumerate((-16, -4, 10)):
        out += (f'<g transform="rotate({ug},{x:.0f},{y-60*s_:.0f})">'
                f'<rect x="{x-5*s_:.0f}" y="{y-128*s_:.0f}" width="{10*s_:.0f}"'
                f' height="{76*s_:.0f}" rx="{4*s_:.0f}" fill="url(#dosk)" {o(max(3,3*s_))}/>'
                f'<ellipse cx="{x:.0f}" cy="{y-132*s_:.0f}" rx="{15*s_:.0f}"'
                f' ry="{19*s_:.0f}" fill="url(#dosk)" {o(max(3,3*s_))}/></g>')
    return out


def _korzinka(x, y, s_=1.0, chem="ovoshchi"):
    w_, h_ = 120 * s_, 76 * s_
    out = ten(x, y + 8 * s_, w_ * .56, 12 * s_, .42)
    if chem == "ovoshchi":
        for i in range(4):
            out += (f'<circle cx="{x-36*s_+i*24*s_:.0f}" cy="{y-h_+8*s_:.0f}"'
                    f' r="{20*s_:.0f}" fill="{["#c98f45","#b2552f","#c08a3e","#8a9a58"][i%4]}"'
                    f' {o(max(3,4*s_))}/>')
    elif chem == "griby":
        for i in range(3):
            gx = x - 28 * s_ + i * 28 * s_
            out += (f'<path d="M{gx-20*s_:.0f},{y-h_+6*s_:.0f} q{20*s_:.0f},{-26*s_:.0f}'
                    f' {40*s_:.0f},0 Z" fill="#8a5a33" {o(max(3,4*s_))}/>')
    out += (f'<path d="M{x-w_/2:.0f},{y-h_:.0f} l{12*s_:.0f},{h_:.0f} h{w_-24*s_:.0f}'
            f' l{12*s_:.0f},{-h_:.0f} Z" fill="url(#solom)" {o(max(4,5*s_))}/>')
    for i in range(3):
        out += (f'<path d="M{x-w_/2+8*s_:.0f},{y-h_+(i+1)*h_/4:.0f} q{w_/2:.0f},{10*s_:.0f}'
                f' {w_-16*s_:.0f},0" fill="none" stroke="#a07c2e"'
                f' stroke-width="{max(2,3*s_):.0f}" opacity=".75"/>')
    out += (f'<path d="M{x-w_*.3:.0f},{y-h_:.0f} q{w_*.3:.0f},{-54*s_:.0f} {w_*.6:.0f},0"'
            f' fill="none" stroke="url(#solom)" stroke-width="{max(5,7*s_):.0f}" {o(0)}/>'
            f'<path d="M{x-w_*.3:.0f},{y-h_:.0f} q{w_*.3:.0f},{-54*s_:.0f} {w_*.6:.0f},0"'
            f' fill="none" stroke="{K}" stroke-width="{max(2,3*s_):.0f}"/>')
    return out


def _meshok(x, y, s_=1.0, podpis=None):
    w_, h_ = 116 * s_, 150 * s_
    out = ten(x, y + 8 * s_, w_ * .56, 13 * s_, .45)
    out += (f'<path d="M{x-w_/2:.0f},{y:.0f} q{-6*s_:.0f},{-h_:.0f} {w_*.3:.0f},{-h_*1.04:.0f}'
            f' q{w_*.4:.0f},{-6*s_:.0f} {w_*.7:.0f},{h_*.04:.0f} q{w_*.36:.0f},{h_*.1:.0f}'
            f' {w_*.3:.0f},{h_:.0f} Z" fill="#d8c8a4" {o(max(4,6*s_))}/>')
    out += (f'<path d="M{x-w_*.22:.0f},{y-h_*1.0:.0f} q{w_*.22:.0f},{-18*s_:.0f} {w_*.44:.0f},0"'
            f' fill="none" stroke="{TKAN}" stroke-width="{max(5,8*s_):.0f}"/>')
    out += (f'<path d="M{x-w_*.36:.0f},{y-h_*.46:.0f} q{w_*.36:.0f},{14*s_:.0f} {w_*.72:.0f},0"'
            f' fill="none" stroke="#b8a883" stroke-width="{max(3,5*s_):.0f}"/>')
    return out


def _vedro(x, y, s_=1.0):
    w_, h_ = 88 * s_, 96 * s_
    return (ten(x, y + 6 * s_, w_ * .56, 10 * s_, .4)
            + f'<path d="M{x-w_/2:.0f},{y-h_:.0f} h{w_:.0f} l{-10*s_:.0f},{h_:.0f}'
              f' h{-w_+20*s_:.0f} Z" fill="url(#zhel)" {o(max(4,5*s_))}/>'
            + f'<path d="M{x-w_/2:.0f},{y-h_:.0f} q{w_/2:.0f},{-46*s_:.0f} {w_:.0f},0"'
              f' fill="none" stroke="{K}" stroke-width="{max(3,4*s_):.0f}"/>')


def _kadushka(x, y, s_=1.0):
    w_, h_ = 132 * s_, 124 * s_
    out = ten(x, y + 8 * s_, w_ * .56, 12 * s_, .42)
    out += (f'<path d="M{x-w_/2:.0f},{y:.0f} l{8*s_:.0f},{-h_:.0f} h{w_-16*s_:.0f}'
            f' l{8*s_:.0f},{h_:.0f} Z" fill="url(#derev)" {o(max(4,6*s_))}/>')
    for yy in (y - h_ * .25, y - h_ * .75):
        out += (f'<path d="M{x-w_*.47:.0f},{yy:.0f} h{w_*.94:.0f}" stroke="{ZHELEZ}"'
                f' stroke-width="{max(4,7*s_):.0f}"/>')
    out += (f'<ellipse cx="{x:.0f}" cy="{y-h_:.0f}" rx="{w_*.44:.0f}" ry="{10*s_:.0f}"'
            f' fill="url(#dosk)" {o(max(3,4*s_))}/>')
    return out


def _valenki(x, y, s_=1.0):
    out = ten(x + 10 * s_, y + 6 * s_, 62 * s_, 10 * s_, .4)
    for i in range(2):
        xx = x + i * 44 * s_
        out += (f'<path d="M{xx-26*s_:.0f},{y:.0f} v{-96*s_:.0f} q{26*s_:.0f},{-14*s_:.0f}'
                f' {46*s_:.0f},0 v{96*s_:.0f} Z" fill="#9a8c74" {o(max(4,5*s_))}/>')
    return out


def _tabulet(x, y, s_=1.0):
    w_, h_ = 104 * s_, 92 * s_
    return (ten(x, y + 6 * s_, w_ * .5, 10 * s_, .4)
            + f'<rect x="{x-w_/2:.0f}" y="{y-h_:.0f}" width="{w_:.0f}" height="{16*s_:.0f}"'
              f' rx="{5*s_:.0f}" fill="url(#dosk)" {o(max(4,5*s_))}/>'
            + f'<rect x="{x-w_/2+8*s_:.0f}" y="{y-h_+16*s_:.0f}" width="{12*s_:.0f}"'
              f' height="{h_-16*s_:.0f}" fill="url(#derev)" {o(max(3,4*s_))}/>'
            + f'<rect x="{x+w_/2-20*s_:.0f}" y="{y-h_+16*s_:.0f}" width="{12*s_:.0f}"'
              f' height="{h_-16*s_:.0f}" fill="url(#derev)" {o(max(3,4*s_))}/>')


# ── ГРУППЫ ─────────────────────────────────────────────────────────────────
NA_STOLE = ("krynka", "miska", "kruzhka", "hleb", "luk", "banka", "lozhki",
            "solonka", "korzinka", "kartoshka", "svecha", "kadushka")


def na_stole(x, y, w_, t, seed=1, n=4, krupno=1.0):
    """Натюрморт НА поверхности: y — линия столешницы, предметы стоят на ней."""
    r = random.Random(seed * 17 + 3)
    vidy = list(NA_STOLE)
    r.shuffle(vidy)
    out = ""
    n = max(2, min(n, 6))
    for i in range(n):
        xx = x + (i + .5) * w_ / n + r.uniform(-18, 18)
        s_ = krupno * r.uniform(.68, 1.0)
        v = vidy[i % len(vidy)]
        if v == "krynka":
            out += ten(xx, y + 6 * s_, 44 * s_, 9 * s_, .4) + krynka(xx, y, .9 * s_)
        elif v == "miska":
            out += _miska(xx, y, s_, r.choice(("kasha", "kapusta", "kartoshka", None)))
        elif v == "kruzhka":
            out += _kruzhka(xx, y, s_, r.choice(("url(#krem)", "url(#glina)")))
        elif v == "hleb":
            out += _hleb(xx, y, s_ * 1.1)
        elif v == "luk":
            out += _luk(xx, y, s_, r.choice((2, 3)),
                        r.choice(("url(#solom)", "#e7ddc8", "#b2552f")))
        elif v == "banka":
            out += _banka(xx, y, s_, r.choice(("#8a6038", "#5d7a3a", "#b2552f", "#c08a3e")))
        elif v == "lozhki":
            out += _lozhki(xx, y, s_)
        elif v == "solonka":
            out += _solonka(xx, y, s_)
        elif v == "korzinka":
            out += _korzinka(xx, y, s_ * .8, r.choice(("ovoshchi", "griby")))
        elif v == "kartoshka":
            out += kartoshka(xx - 40 * s_, y - 16 * s_, t, 5, seed + i, s_ * .9)
        elif v == "svecha":
            out += svecha(xx, y, t, r.random(), s_ * .9)
        elif v == "kadushka":
            out += _kadushka(xx, y, s_ * .72)
    return out


def stena_nabor(x, y, w_, t, seed=2, n=4):
    """Обжитая стена: пучки трав, связки, доски, сито, рушник, рамка, подкова.
    y — высота, на которой вещи висят (верх предмета)."""
    r = random.Random(seed * 29 + 11)
    vidy = ["travy", "svyazka", "doska", "sito", "polovnik", "rushnik",
            "ramka", "podkova", "venik", "kalendar", "skovoroda"]
    r.shuffle(vidy)
    out = ""
    for i in range(max(2, min(n, 5))):
        xx = x + (i + .5) * w_ / max(2, min(n, 5)) + r.uniform(-14, 14)
        v = vidy[i % len(vidy)]
        kach = 1.6 * A.w(t, 4.6 + i * .5, i * .2)
        g0 = f'<g transform="rotate({kach:.2f},{xx:.0f},{y:.0f})">'
        if v == "travy":
            out += g0 + f'<circle cx="{xx:.0f}" cy="{y:.0f}" r="6" fill="{ZHELEZ}" {o(3)}/>'
            for j in range(5):
                out += (f'<path d="M{xx:.0f},{y:.0f} q{-20+j*10:.0f},70 {-14+j*7:.0f},128"'
                        f' fill="none" stroke="{["#6f8c4a","#8a9a58","#5c7a40"][j%3]}" stroke-width="7"/>')
            out += (f'<path d="M{xx-20:.0f},{y+6:.0f} q20,-14 40,0" fill="none"'
                    f' stroke="{TKAN}" stroke-width="9"/></g>')
        elif v == "svyazka":
            out += g0 + f'<path d="M{xx:.0f},{y:.0f} v70" {o(6)} fill="none"/>'
            for j in range(4):
                out += (f'<circle cx="{xx-16+(j%2)*32:.0f}" cy="{y+78+j*44:.0f}" r="27"'
                        f' fill="{r.choice(("url(#solom)","#e7ddc8"))}" {o(5)}/>')
            out += "</g>"
        elif v == "doska":
            out += (g0 + f'<rect x="{xx-52:.0f}" y="{y:.0f}" width="104" height="158" rx="14"'
                    f' fill="url(#dosk)" {o(6)}/>'
                    f'<circle cx="{xx:.0f}" cy="{y+16:.0f}" r="9" fill="{K}"/>'
                    f'<path d="M{xx-34:.0f},{y+60:.0f} h68 M{xx-34:.0f},{y+96:.0f} h68"'
                    f' stroke="{DOSKA2}" stroke-width="5" opacity=".7"/></g>')
        elif v == "sito":
            out += (g0 + f'<circle cx="{xx:.0f}" cy="{y+58:.0f}" r="58" fill="url(#solom)" {o(6)}/>'
                    f'<circle cx="{xx:.0f}" cy="{y+58:.0f}" r="42" fill="#cdb98d" {o(4)}/>'
                    + "".join(f'<path d="M{xx-42:.0f},{y+28+j*14:.0f} h84" stroke="#a07c2e"'
                              f' stroke-width="3" opacity=".7"/>' for j in range(5))
                    + f'<path d="M{xx:.0f},{y:.0f} v10" {o(5)} fill="none"/></g>')
        elif v == "polovnik":
            out += (g0 + f'<rect x="{xx-7:.0f}" y="{y:.0f}" width="14" height="120" rx="6"'
                    f' fill="url(#zhel)" {o(5)}/>'
                    f'<path d="M{xx-34:.0f},{y+118:.0f} q34,56 68,0 Z" fill="url(#zhel)" {o(5)}/></g>')
        elif v == "rushnik":
            out += (g0 + f'<path d="M{xx-56:.0f},{y:.0f} h112 q-8,196 -56,208 q-48,-12 -56,-208 z"'
                    f' fill="url(#rush)" {o(5)}/>'
                    f'<path d="M{xx-48:.0f},{y+110:.0f} h96" stroke="{TKAN}" stroke-width="9" opacity=".85"/>'
                    f'<path d="M{xx-48:.0f},{y+150:.0f} h96" stroke="{TKAN2}" stroke-width="7" opacity=".7"/></g>')
        elif v == "ramka":
            out += (g0 + f'<rect x="{xx-58:.0f}" y="{y:.0f}" width="116" height="92" rx="7"'
                    f' fill="url(#med)" {o(6)}/>'
                    f'<rect x="{xx-44:.0f}" y="{y+12:.0f}" width="88" height="68" fill="#cfd8dd" {o(3)}/>'
                    + siluet(xx - 16, y + 78, 56, "#5b6a78", .9)
                    + siluet(xx + 16, y + 78, 50, "#6b5a6e", .9) + "</g>")
        elif v == "podkova":
            out += (g0 + f'<path d="M{xx-38:.0f},{y+78:.0f} a38,44 0 1,1 76,0" fill="none"'
                    f' stroke="url(#zhel)" stroke-width="20" {o(0)}/>'
                    f'<path d="M{xx-38:.0f},{y+78:.0f} a38,44 0 1,1 76,0" fill="none"'
                    f' stroke="{K}" stroke-width="5"/></g>')
        elif v == "venik":
            out += (g0 + f'<rect x="{xx-8:.0f}" y="{y:.0f}" width="16" height="96" rx="7"'
                    f' fill="url(#dosk)" {o(5)}/>'
                    f'<path d="M{xx-46:.0f},{y+200:.0f} q46,-130 92,0 Z" fill="url(#solom)" {o(5)}/></g>')
        elif v == "kalendar":
            out += (g0 + f'<rect x="{xx-44:.0f}" y="{y:.0f}" width="88" height="118" rx="8"'
                    f' fill="url(#list)" {o(5)}/>'
                    f'<rect x="{xx-44:.0f}" y="{y:.0f}" width="88" height="30" rx="8"'
                    f' fill="{TKAN}" {o(4)}/>'
                    + "".join(f'<path d="M{xx-30:.0f},{y+52+j*22:.0f} h60" stroke="#b9ab8c"'
                              f' stroke-width="5"/>' for j in range(3)) + "</g>")
        else:   # сковорода
            out += (g0 + f'<circle cx="{xx:.0f}" cy="{y+66:.0f}" r="62" fill="url(#chug)" {o(6)}/>'
                    f'<path d="M{xx+56:.0f},{y+52:.0f} q70,-14 86,10" fill="none"'
                    f' stroke="{K}" stroke-width="13"/></g>')
    return out


def polka_veshchey(x, y, w_, t, seed=3, dve=False):
    """Полка со скарбом: банки, крынки, стопка мисок, свёртки, чайник."""
    r = random.Random(seed * 13 + 7)
    out = (f'<rect x="{x:.0f}" y="{y:.0f}" width="{w_:.0f}" height="20" rx="6"'
           f' fill="url(#derev)" {o(6)}/>'
           f'<path d="M{x+28:.0f},{y+20:.0f} l20,32 M{x+w_-48:.0f},{y+20:.0f} l-20,32"'
           f' {o(5)} fill="none"/>')
    n = max(3, int(w_ / 150))
    for i in range(n):
        xx = x + 50 + i * (w_ - 100) / max(1, n - 1)
        k = r.random()
        if k < .26:
            out += _banka(xx, y - 2, .92, r.choice(("#8a6038", "#5d7a3a", "#b2552f", "#c08a3e")))
        elif k < .46:
            out += krynka(xx, y - 2, r.uniform(.6, .82))
        elif k < .62:
            for j in range(3):          # стопка мисок
                out += (f'<path d="M{xx-40:.0f},{y-14-j*20:.0f} q40,34 80,0 Z"'
                        f' fill="url(#krem)" {o(4)}/>')
        elif k < .78:
            out += _kruzhka(xx, y - 2, .82, "url(#krem)")
        else:
            out += (ten(xx, y + 2, 44, 8, .35)
                    + f'<path d="M{xx-42:.0f},{y-2:.0f} v-54 q42,-20 84,0 v54 Z"'
                      f' fill="url(#zhel)" {o(5)}/>'
                    + f'<path d="M{xx+40:.0f},{y-44:.0f} q34,16 2,40" fill="none"'
                      f' stroke="{K}" stroke-width="9"/>'
                    + f'<rect x="{xx-14:.0f}" y="{y-72:.0f}" width="28" height="18" rx="6"'
                      f' fill="url(#zhel)" {o(4)}/>')
    if dve:
        y2 = y - r.choice((150, 180, 210))
        out += polka_veshchey(x + r.choice((20, 60)), y2, w_ - 90, t, seed + 5, False)
    return out


def pod_stolom(x, y, w_, t, seed=4, n=3):
    """Пол под столом и у стены: корзина, мешок, ведро, кадушка, валенки, кот."""
    r = random.Random(seed * 31 + 5)
    vidy = ["korzina", "meshok", "vedro", "kadushka", "valenki", "kot", "drova", "tabulet"]
    r.shuffle(vidy)
    out = ""
    n = max(2, min(n, 4))
    for i in range(n):
        xx = x + (i + .5) * w_ / n + r.uniform(-20, 20)
        s_ = r.uniform(.8, 1.1)
        v = vidy[i % len(vidy)]
        if v == "korzina":
            out += _korzinka(xx, y, s_ * 1.1, r.choice(("ovoshchi", "griby")))
        elif v == "meshok":
            out += _meshok(xx, y, s_ * .9)
        elif v == "vedro":
            out += _vedro(xx, y, s_)
        elif v == "kadushka":
            out += _kadushka(xx, y, s_)
        elif v == "valenki":
            out += _valenki(xx, y, s_)
        elif v == "kot":
            out += kot(xx, y, t, s_ * 1.1, "#3b3430", r.random() < .5)
        elif v == "tabulet":
            out += _tabulet(xx, y, s_)
        else:
            out += ten(xx, y + 6, 66 * s_, 11, .42)
            for j in range(5):
                out += (f'<ellipse cx="{xx-46*s_+j*24*s_:.0f}" cy="{y-18*s_-(j%2)*26*s_:.0f}"'
                        f' rx="{15*s_:.0f}" ry="{24*s_:.0f}" fill="url(#derev)" {o(4)}/>')
    return out


def pod_potolkom(x, y, w_, t, seed=6, n=3):
    """Под потолком: вязки грибов, пучки трав, корзина на крюке."""
    r = random.Random(seed * 23 + 9)
    out = ""
    for i in range(max(2, min(n, 4))):
        xx = x + (i + .5) * w_ / max(2, min(n, 4)) + r.uniform(-16, 16)
        kach = 1.4 * A.w(t, 5.2 + i * .6, i * .25)
        out += f'<g transform="rotate({kach:.2f},{xx:.0f},{y:.0f})">'
        k = r.random()
        if k < .45:                      # вязка грибов
            out += f'<path d="M{xx:.0f},{y:.0f} v250" {o(5)} fill="none"/>'
            for j in range(6):
                yy = y + 46 + j * 34
                out += (f'<path d="M{xx-26:.0f},{yy:.0f} q26,-30 52,0 Z" fill="#8a5a33" {o(4)}/>'
                        f'<rect x="{xx-5:.0f}" y="{yy:.0f}" width="10" height="16" fill="#c9ad7d" {o(3)}/>')
        elif k < .8:                     # пучок трав
            out += f'<circle cx="{xx:.0f}" cy="{y:.0f}" r="6" fill="{ZHELEZ}" {o(3)}/>'
            for j in range(5):
                out += (f'<path d="M{xx:.0f},{y:.0f} q{-18+j*9:.0f},72 {-12+j*6:.0f},132"'
                        f' fill="none" stroke="{["#6f8c4a","#8a9a58","#5c7a40"][j%3]}" stroke-width="7"/>')
        else:                            # корзина на крюке
            out += (f'<path d="M{xx:.0f},{y:.0f} v96" {o(5)} fill="none"/>'
                    + _korzinka(xx, y + 170, .8, "ovoshchi"))
        out += "</g>"
    return out


def ugol_mebel(x, y, t, seed=7, vid=None):
    """Угол комнаты: сундук, комод, кадка с цветком, самовар на тумбе."""
    r = random.Random(seed * 37 + 2)
    v = vid or r.choice(("sunduk", "komod", "cvetok", "samovar", "prylka"))
    out = ""
    if v == "sunduk":
        out += (ten(x, y + 8, 120, 14, .45)
                + f'<rect x="{x-118:.0f}" y="{y-128:.0f}" width="236" height="128" rx="10"'
                  f' fill="url(#derev)" {o(7)}/>'
                + f'<path d="M{x-118:.0f},{y-128:.0f} q118,-56 236,0 Z" fill="url(#dosk)" {o(6)}/>'
                + f'<rect x="{x-14:.0f}" y="{y-86:.0f}" width="28" height="34" rx="5"'
                  f' fill="url(#zhel)" {o(4)}/>')
    elif v == "komod":
        out += (ten(x, y + 8, 110, 13, .45)
                + f'<rect x="{x-106:.0f}" y="{y-196:.0f}" width="212" height="196" rx="8"'
                  f' fill="url(#derev)" {o(7)}/>')
        for j in range(3):
            out += (f'<rect x="{x-92:.0f}" y="{y-180+j*60:.0f}" width="184" height="48" rx="6"'
                    f' fill="url(#dosk)" {o(4)}/>'
                    f'<circle cx="{x:.0f}" cy="{y-156+j*60:.0f}" r="9" fill="{ZOL}" {o(3)}/>')
        out += krynka(x - 50, y - 196, .6) + _kruzhka(x + 46, y - 196, .8)
    elif v == "cvetok":
        out += (ten(x, y + 6, 70, 11, .4)
                + f'<path d="M{x-56:.0f},{y:.0f} l10,-96 h92 l10,96 Z" fill="url(#glina)" {o(6)}/>')
        for j in range(7):
            ug = -70 + j * 23
            out += (f'<path d="M{x:.0f},{y-96:.0f} q{math.cos(math.radians(ug))*70:.0f},'
                    f'{-90-abs(ug)*.3:.0f} {math.cos(math.radians(ug))*104:.0f},{-54:.0f}"'
                    f' fill="none" stroke="{["#3c5a3a","#56763f","#6f8c4a"][j%3]}" stroke-width="13"/>')
    elif v == "samovar":
        out += (ten(x, y + 6, 70, 11, .42)
                + _tabulet(x, y, 1.3)
                + f'<path d="M{x-44:.0f},{y-118:.0f} q44,-118 88,0 q-44,42 -88,0 Z"'
                  f' fill="url(#med)" {o(6)}/>'
                + f'<rect x="{x-12:.0f}" y="{y-250:.0f}" width="24" height="42" rx="6"'
                  f' fill="url(#med)" {o(4)}/>'
                + par(x, y - 250, t, 4, .45, 120, .4, .9))
    else:
        out += (ten(x, y + 6, 64, 10, .4)
                + f'<path d="M{x-10:.0f},{y:.0f} v-250" {o(7)} fill="none"/>'
                + f'<path d="M{x-70:.0f},{y:.0f} h140" {o(7)} fill="none"/>'
                + f'<ellipse cx="{x-10:.0f}" cy="{y-260:.0f}" rx="52" ry="34"'
                  f' fill="url(#solom)" {o(5)}/>')
    return out


def dvor_veshchi(x, y, w_, t, seed=8, n=3):
    """Двор: поленница, сани, лопата, ведро, куст под снегом, скамья, следы."""
    r = random.Random(seed * 41 + 13)
    vidy = ["polennica", "sani", "lopata", "vedro", "kust", "skamya", "stolb"]
    r.shuffle(vidy)
    out = ""
    for i in range(max(2, min(n, 4))):
        xx = x + (i + .5) * w_ / max(2, min(n, 4)) + r.uniform(-24, 24)
        s_ = r.uniform(.85, 1.15)
        v = vidy[i % len(vidy)]
        if v == "polennica":
            out += ten(xx, y + 6, 104 * s_, 12, .4)
            for ry_ in range(4):
                for cx_ in range(5):
                    out += (f'<ellipse cx="{xx-86*s_+cx_*44*s_:.0f}" cy="{y-20*s_-ry_*40*s_:.0f}"'
                            f' rx="{20*s_:.0f}" ry="{18*s_:.0f}" fill="url(#derev)" {o(4)}/>')
            out += (f'<path d="M{xx-108*s_:.0f},{y-180*s_:.0f} q{108*s_:.0f},{-26*s_:.0f}'
                    f' {216*s_:.0f},0" fill="{SNEG}" opacity=".9" {o(0)}/>')
        elif v == "sani":
            out += (ten(xx, y + 6, 100 * s_, 12, .4)
                    + f'<path d="M{xx-96*s_:.0f},{y:.0f} q{16*s_:.0f},{-22*s_:.0f} {36*s_:.0f},{-18*s_:.0f}'
                      f' h{130*s_:.0f}" fill="none" stroke="{K}" stroke-width="{9*s_:.0f}"/>'
                    + f'<rect x="{xx-76*s_:.0f}" y="{y-74*s_:.0f}" width="{156*s_:.0f}"'
                      f' height="{26*s_:.0f}" rx="{8*s_:.0f}" fill="url(#dosk)" {o(5)}/>'
                    + f'<path d="M{xx-60*s_:.0f},{y-48*s_:.0f} v{30*s_:.0f} M{xx+54*s_:.0f},'
                      f'{y-48*s_:.0f} v{30*s_:.0f}" {o(6)} fill="none"/>'
                    + f'<ellipse cx="{xx:.0f}" cy="{y-84*s_:.0f}" rx="{70*s_:.0f}"'
                      f' ry="{16*s_:.0f}" fill="{SNEG}" opacity=".85"/>')
        elif v == "lopata":
            out += (f'<g transform="rotate(-12,{xx:.0f},{y:.0f})">'
                    f'<rect x="{xx-7*s_:.0f}" y="{y-250*s_:.0f}" width="{14*s_:.0f}"'
                    f' height="{200*s_:.0f}" rx="{6*s_:.0f}" fill="url(#dosk)" {o(5)}/>'
                    f'<path d="M{xx-34*s_:.0f},{y-56*s_:.0f} h{68*s_:.0f} v{56*s_:.0f}'
                    f' q{-34*s_:.0f},{16*s_:.0f} {-68*s_:.0f},0 Z" fill="url(#zhel)" {o(5)}/></g>')
        elif v == "vedro":
            out += _vedro(xx, y, s_ * .9) + (f'<ellipse cx="{xx:.0f}" cy="{y-88*s_:.0f}"'
                                             f' rx="{40*s_:.0f}" ry="{10*s_:.0f}" fill="{SNEG}" opacity=".8"/>')
        elif v == "kust":
            out += ten(xx, y + 4, 70 * s_, 10, .35)
            for j in range(6):
                out += (f'<path d="M{xx:.0f},{y:.0f} q{-50+j*20:.0f},{-70*s_:.0f}'
                        f' {-62+j*25:.0f},{-120*s_:.0f}" fill="none" stroke="#5a4a38"'
                        f' stroke-width="{7*s_:.0f}"/>')
            out += (f'<ellipse cx="{xx:.0f}" cy="{y-128*s_:.0f}" rx="{76*s_:.0f}"'
                    f' ry="{30*s_:.0f}" fill="{SNEG}" opacity=".92" {o(0)}/>')
        elif v == "skamya":
            out += (ten(xx, y + 6, 100 * s_, 12, .38)
                    + f'<rect x="{xx-96*s_:.0f}" y="{y-92*s_:.0f}" width="{192*s_:.0f}"'
                      f' height="{24*s_:.0f}" rx="{8*s_:.0f}" fill="url(#dosk)" {o(5)}/>'
                    + f'<rect x="{xx-80*s_:.0f}" y="{y-68*s_:.0f}" width="{16*s_:.0f}"'
                      f' height="{68*s_:.0f}" fill="url(#derev)" {o(4)}/>'
                    + f'<rect x="{xx+64*s_:.0f}" y="{y-68*s_:.0f}" width="{16*s_:.0f}"'
                      f' height="{68*s_:.0f}" fill="url(#derev)" {o(4)}/>'
                    + f'<ellipse cx="{xx:.0f}" cy="{y-94*s_:.0f}" rx="{92*s_:.0f}"'
                      f' ry="{12*s_:.0f}" fill="{SNEG}" opacity=".9"/>')
        else:
            out += (f'<rect x="{xx-10*s_:.0f}" y="{y-280*s_:.0f}" width="{20*s_:.0f}"'
                    f' height="{280*s_:.0f}" rx="{7*s_:.0f}" fill="url(#dosk)" {o(6)}/>'
                    + f'<path d="M{xx-44*s_:.0f},{y-300*s_:.0f} h{88*s_:.0f} l{-14*s_:.0f},'
                      f'{40*s_:.0f} h{-60*s_:.0f} Z" fill="url(#zhel)" {o(5)}/>'
                    + teplo(xx, y - 262 * s_, 150 * s_, 120 * s_, .5))
    return out


def sled_v_snegu(x, y, w_, n=5, op=.5):
    """Следы на снегу — пустое поле перестаёт быть белым листом."""
    out = ""
    for i in range(n):
        xx = x + i * w_ / max(1, n - 1)
        yy = y + (i % 2) * 16
        out += (f'<ellipse cx="{xx:.0f}" cy="{yy:.0f}" rx="18" ry="9"'
                f' fill="#aebccd" opacity="{op:.2f}"/>')
    return out
