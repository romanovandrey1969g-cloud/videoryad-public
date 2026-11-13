# -*- coding: utf-8 -*-
"""113 декораций ролика «Рождественский пост».

Каждая — функция времени f(t) -> svg. Все нарисованы ЗАНОВО под этот текст
(R-0019): ни один кадр не взят у «13 ноября», «14 ноября» и «15 ноября».
Где в плане стоит окно вставки, главное живёт в ЛЕВОЙ полосе 0-830 (R-0007).
В каждой декорации минимум три живых элемента (R-0006).

Мир ролика: деревенская и городская кухня поздней осени и зимы, стол как
главный герой, снежная улица за окном. Тёплый свет лампы и печи — против
синего мороза в окне.
"""
import math, random
from baza import *
from baza import (_nebo, _oblaka, _tuman, _ulica_dal, _panelka, _sneg_lezhit,
                  _sneg_letit, _utvar_izby, _utvar_pekarni, _kvartira_veschi,
                  _mebel_hlam, _ramka_pp, _vinetka)
import anim as A

OKNO = (860, 300, 980, 551)          # неподвижный контейнер вставки
DEN_, MESYAC = "28", "НОЯБРЯ"


# ═══════════════ СКВОЗНЫЕ КИРПИЧИКИ ЭТОГО РОЛИКА ═══════════════
# Стол — главный герой ролика: с него уходит скоромное и на него встаёт
# постное. Поэтому он вынесен кирпичиком со столешницей в перспективе.
def stol_bok(x, y, w_, h_=210, t=0.0, skatert=None, tolshch=26):
    """Кухонный стол: широкая верхняя плоскость в перспективе, торец, ноги.
    Плоскость обязана быть ВИДИМОЙ — иначе предметы висят над планкой и стол
    читается скамейкой (брак первого и второго листа 13.11)."""
    gl = int(w_ * .26)                      # глубина столешницы в перспективе
    s = ten(x + w_ / 2, y + h_ + 24, w_ * .6, 34, .5)
    # верхняя плоскость: дальний край уже ближнего
    s += (f'<path d="M{x+gl*.6:.0f},{y-gl:.0f} h{w_-gl*1.2:.0f} l{gl*.6:.0f},{gl:.0f}'
          f' h-{w_} z" fill="#ba8c5c" {o(7)}/>')
    s += (f'<path d="M{x+gl*.6:.0f},{y-gl:.0f} h{w_-gl*1.2:.0f}" stroke="#d6a876"'
          f' stroke-width="6" opacity=".8"/>')
    for i in range(5):
        x0 = x + gl * .6 + 8 + i * (w_ - gl * 1.2) / 5
        s += (f'<path d="M{x0:.0f},{y-gl:.0f} l-{gl*.6:.0f},{gl:.0f}"'
              f' stroke="{DOSKA2}" stroke-width="4" opacity=".4"/>')
    # торец
    s += (f'<rect x="{x}" y="{y}" width="{w_}" height="{tolshch+16}" rx="8"'
          f' fill="url(#dosk)" {o(7)}/>')
    s += f'<rect x="{x}" y="{y}" width="{w_}" height="9" fill="#ffffff" opacity=".25"/>'
    for nx in (x + 52, x + w_ - 96):
        s += (f'<rect x="{nx}" y="{y+tolshch+12}" width="44" height="{h_-tolshch}"'
              f' rx="8" fill="url(#derev)" {o(6)}/>')
    s += (f'<rect x="{x+70}" y="{y+h_-78}" width="{w_-170}" height="20" rx="7"'
          f' fill="url(#derev)" {o(5)} opacity=".9"/>')
    if skatert:
        dy = 5 * A.w(t, 2.6)
        s += (f'<path d="M{x+gl*.5:.0f},{y-gl-4:.0f} h{w_-gl:.0f} l{gl*.7:.0f},{gl+6:.0f}'
              f' v{54+dy:.0f} q-{w_/2:.0f},24 -{w_+gl*.2:.0f},0 v-{54+dy:.0f} z"'
              f' fill="{skatert}" {o(6)}/>')
        s += (f'<path d="M{x-6},{y+34:.0f} h{w_+12}" stroke="{TKAN}"'
              f' stroke-width="8" opacity=".45"/>')
    return s


def tarelka(x, y, r=86, t=0.0, col="url(#krem)", gluboka=False, par_=0):
    """Тарелка в три четверти: эллипс, борт, блик. R-0017 — с объёмом."""
    s = ten(x, y + r * .42, r * 1.02, r * .3, .45)
    s += f'<ellipse cx="{x}" cy="{y}" rx="{r}" ry="{r*.4:.0f}" fill="{col}" {o(5)}/>'
    s += (f'<ellipse cx="{x}" cy="{y-2}" rx="{r*.68:.0f}" ry="{r*.26:.0f}"'
          f' fill="#ffffff" opacity=".30"/>')
    if gluboka:
        s += (f'<path d="M{x-r},{y} q{r},{r*.62:.0f} {r*2},0" fill="none" {o(5)}/>')
    s += (f'<ellipse cx="{x-r*.34:.0f}" cy="{y-r*.16:.0f}" rx="{r*.2:.0f}"'
          f' ry="{r*.07:.0f}" fill="#ffffff" opacity=".5"/>')
    for i in range(par_):
        s += par(x - 14 + i * 16, y - 20, t, 3, .4, 120, .5, .8)
    return s


def gorshok(x, y, s_=1.0, t=0.0, col="url(#glina)", kryshka=True):
    """Глиняный горшок с крышкой — постная каша, кутья, щи."""
    w_ = 86 * s_
    h_ = 104 * s_
    s = ten(x, y + 10, w_ * .62, 18 * s_, .5)
    s += (f'<path d="M{x-w_*.38:.0f},{y-h_:.0f} q-{w_*.22:.0f},{h_*.55:.0f}'
          f' {w_*.06:.0f},{h_:.0f} h{w_*.64:.0f}'
          f' q{w_*.28:.0f},-{h_*.45:.0f} {w_*.06:.0f},-{h_:.0f} z"'
          f' fill="{col}" {o(6)}/>')
    s += (f'<ellipse cx="{x}" cy="{y-h_:.0f}" rx="{w_*.4:.0f}" ry="{w_*.13:.0f}"'
          f' fill="{MED}" {o(5)}/>')
    if kryshka:
        dy = 3 * s_ * A.w(t, 1.9)
        s += (f'<ellipse cx="{x}" cy="{y-h_-10*s_-dy:.0f}" rx="{w_*.44:.0f}"'
              f' ry="{w_*.15:.0f}" fill="url(#glina)" {o(5)}/>')
        s += (f'<circle cx="{x}" cy="{y-h_-22*s_-dy:.0f}" r="{7*s_:.0f}"'
              f' fill="{MED}" {o(4)}/>')
    s += (f'<path d="M{x-w_*.3:.0f},{y-h_*.6:.0f} q{w_*.1:.0f},{h_*.3:.0f} 0,{h_*.5:.0f}"'
          f' fill="none" stroke="#ffffff" stroke-width="7" opacity=".18"/>')
    return s


def ryba(x, y, s_=1.0, t=0.0, zapech=True):
    """Рыба целиком: тело каплей, хвост вилкой, плавник, глаз, кружки лука."""
    L = 300 * s_
    hh = 96 * s_
    col = "#cf9558" if zapech else "#a8bfcb"
    s = ten(x, y + hh * .5, L * .46, hh * .22, .45)
    # тело
    s += (f'<path d="M{x-L*.44:.0f},{y}'
          f' q{L*.16:.0f},-{hh*.62:.0f} {L*.46:.0f},-{hh*.58:.0f}'
          f' q{L*.3:.0f},{hh*.02:.0f} {L*.42:.0f},{hh*.52:.0f}'
          f' q-{L*.12:.0f},{hh*.56:.0f} -{L*.42:.0f},{hh*.58:.0f}'
          f' q-{L*.3:.0f},{hh*.04:.0f} -{L*.46:.0f},-{hh*.52:.0f} z"'
          f' fill="{col}" {o(6)}/>')
    # хвост вилкой
    s += (f'<path d="M{x+L*.42:.0f},{y-hh*.06:.0f} l{L*.16:.0f},-{hh*.42:.0f}'
          f' l0,{hh*.84:.0f} z" fill="{col}" {o(6)}/>')
    # спинной плавник и бок
    s += (f'<path d="M{x-L*.1:.0f},{y-hh*.56:.0f} q{L*.12:.0f},-{hh*.3:.0f} {L*.24:.0f},-{hh*.04:.0f} z"'
          f' fill="{col}" {o(5)}/>')
    s += (f'<path d="M{x-L*.34:.0f},{y+hh*.08:.0f} q{L*.34:.0f},{hh*.22:.0f} {L*.7:.0f},0"'
          f' fill="none" stroke="#8a5a2c" stroke-width="{5*s_:.1f}" opacity=".55"/>')
    # голова, жабра, глаз
    s += (f'<path d="M{x-L*.44:.0f},{y} q{L*.06:.0f},-{hh*.34:.0f} {L*.17:.0f},-{hh*.44:.0f}'
          f' q{L*.02:.0f},{hh*.44:.0f} 0,{hh*.9:.0f} q-{L*.12:.0f},-{hh*.1:.0f} -{L*.17:.0f},-{hh*.46:.0f} z"'
          f' fill="#b9803f" {o(5)} opacity=".9"/>')
    s += (f'<circle cx="{x-L*.33:.0f}" cy="{y-hh*.14:.0f}" r="{9*s_:.1f}" fill="#fdf6e4" {o(3)}/>'
          f'<circle cx="{x-L*.33:.0f}" cy="{y-hh*.14:.0f}" r="{5*s_:.1f}" fill="{K}"/>')
    # запечённая корочка штрихами
    for i in range(4):
        xx = x - L * .16 + i * L * .14
        s += (f'<path d="M{xx:.0f},{y-hh*.3:.0f} q{7*s_:.0f},{hh*.3:.0f} 0,{hh*.56:.0f}"'
              f' fill="none" stroke="#9a6027" stroke-width="{4*s_:.1f}" opacity=".5"/>')
    # кружки лука сверху
    for i in range(3):
        s += (f'<ellipse cx="{x-L*.12+i*L*.16:.0f}" cy="{y-hh*.3:.0f}"'
              f' rx="{24*s_:.0f}" ry="{9*s_:.0f}" fill="#f6ecdc" {o(3)}/>'
              f'<ellipse cx="{x-L*.12+i*L*.16:.0f}" cy="{y-hh*.3:.0f}"'
              f' rx="{13*s_:.0f}" ry="{5*s_:.0f}" fill="none" stroke="#d8c6ac"'
              f' stroke-width="{3*s_:.1f}"/>')
    s += (f'<path d="M{x-L*.3:.0f},{y-hh*.26:.0f} q{L*.3:.0f},-{hh*.1:.0f} {L*.6:.0f},{hh*.04:.0f}"'
          f' fill="none" stroke="#ffffff" stroke-width="{6*s_:.1f}" opacity=".22"/>')
    return s


def plashka_dnya(x, y, s_, t, t0=.3):
    """Бирка-ярлык под предметом: день недели, подпись полки."""
    k = A.out(A.seg(t, t0, .4))
    if k <= 0:
        return ""
    w_ = 24 + len(s_) * 17
    dy = 4 * A.w(t, 2.4, x * .001)
    return (f'<g opacity="{k:.2f}" transform="translate({x-w_/2:.0f},{y+dy:.0f})">'
            f'<rect x="0" y="0" width="{w_}" height="42" rx="8" fill="url(#rush)" {o(4)}/>'
            f'<text x="{w_/2:.0f}" y="30" font-family="Georgia,serif" font-size="26"'
            f' text-anchor="middle" fill="#3a2a16">{s_}</text></g>')


def _golova_profil(x, y, k, t, ph=0.0, kozha="#edc49c", vpravo=True):
    """Голова в профиль: лоб, нос, губа, подбородок, ухо, глаз, бровь."""
    sx = 1 if vpravo else -1
    s = (f'<g transform="translate({x},{y}) scale({sx},1)">'
         f'<path d="M-{52*k:.0f},{34*k:.0f}'
         f' q-{16*k:.0f},-{76*k:.0f} {40*k:.0f},-{96*k:.0f}'
         f' q{62*k:.0f},-{20*k:.0f} {78*k:.0f},{44*k:.0f}'
         f' q{6*k:.0f},{22*k:.0f} {18*k:.0f},{34*k:.0f}'
         f' l-{20*k:.0f},{10*k:.0f}'
         f' q{4*k:.0f},{14*k:.0f} -{10*k:.0f},{18*k:.0f}'
         f' q{6*k:.0f},{30*k:.0f} -{44*k:.0f},{34*k:.0f}'
         f' q-{52*k:.0f},{2*k:.0f} -{62*k:.0f},-{44*k:.0f} z"'
         f' fill="{kozha}" {o(5)}/>')
    # ухо
    s += (f'<path d="M-{30*k:.0f},{2*k:.0f} q-{18*k:.0f},{4*k:.0f} -{12*k:.0f},{26*k:.0f}'
          f' q{8*k:.0f},{10*k:.0f} {14*k:.0f},-{2*k:.0f} z" fill="{kozha}" {o(4)}/>')
    # глаз и бровь
    if not A.blink(t, 4.1, ph, .16):
        s += (f'<ellipse cx="{30*k:.0f}" cy="-{4*k:.0f}" rx="{9*k:.1f}" ry="{7*k:.1f}"'
              f' fill="#fdf8ee"/>'
              f'<circle cx="{32*k:.0f}" cy="-{4*k:.0f}" r="{5*k:.1f}" fill="{K}"/>')
    else:
        s += f'<path d="M{22*k:.0f},-{4*k:.0f} h{18*k:.0f}" {o(4)} fill="none"/>'
    s += (f'<path d="M{18*k:.0f},-{22*k:.0f} q{14*k:.0f},-{8*k:.0f} {28*k:.0f},{2*k:.0f}"'
          f' fill="none" stroke="#8a6a52" stroke-width="{4*k:.1f}"/>')
    # губа и щека
    s += (f'<path d="M{34*k:.0f},{40*k:.0f} q{12*k:.0f},{4*k:.0f} {18*k:.0f},-{4*k:.0f}"'
          f' fill="none" stroke="#b9705e" stroke-width="{5*k:.1f}"/>')
    s += (f'<ellipse cx="{14*k:.0f}" cy="{26*k:.0f}" rx="{20*k:.0f}" ry="{12*k:.0f}"'
          f' fill="#e2a089" opacity=".45"/>')
    return s + '</g>'


def pech_russkaya(x, y, w_, h_, t, ogon_on=True, zaslonka=0.0):
    """Русская печь: побелённый корпус, устье аркой, шесток, огонь внутри.
    Печь из общей базы читается белым шкафом — для этого ролика своя."""
    s = ten(x + w_ / 2, y + h_ + 16, w_ * .55, 26, .5)
    # корпус с лежанкой-уступом
    s += (f'<path d="M{x},{y+h_} v-{h_*.78:.0f} h{w_*.22:.0f} v-{h_*.22:.0f}'
          f' h{w_*.78:.0f} v{h_} z" fill="url(#pech)" {o(9)}/>')
    s += (f'<path d="M{x+w_*.22:.0f},{y+h_*.22:.0f} h{w_*.78:.0f}" stroke="{PECH2}"'
          f' stroke-width="9" opacity=".8"/>')
    # побелка мазками
    for i in range(5):
        s += (f'<path d="M{x+30+i*w_*.19:.0f},{y+h_*.35:.0f} q{w_*.07:.0f},{h_*.1:.0f}'
              f' 0,{h_*.22:.0f}" fill="none" stroke="#ffffff" stroke-width="12"'
              f' opacity=".25"/>')
    # шесток
    s += (f'<rect x="{x+w_*.12:.0f}" y="{y+h_*.52:.0f}" width="{w_*.82:.0f}"'
          f' height="{h_*.07:.0f}" rx="8" fill="{PECH2}" {o(6)}/>')
    # устье аркой
    ux, uy = x + w_ * .3, y + h_ * .52
    uw, uh = w_ * .46, h_ * .3
    s += (f'<path d="M{ux},{uy} v-{uh*.52:.0f} q{uw*.5:.0f},-{uh*.6:.0f} {uw:.0f},0'
          f' v{uh*.52:.0f} z" fill="#1a1512" {o(7)}/>')
    if ogon_on:
        s += ogon(ux + uw / 2, uy - uh * .1, t, uw / 230, .0, 5)
        s += ugli(ux + uw * .2, uy - 10, uw * .6, t, 6, 3)
        s += teplo(ux + uw / 2, uy - uh * .2, uw * 1.1, uh * 1.2, .55)
    if zaslonka > 0:
        s += (f'<path d="M{ux-10},{uy-uh*.52*zaslonka:.0f} h{uw+20:.0f}'
              f' v{uh*.52*zaslonka:.0f} h-{uw+20:.0f} z" fill="url(#zhel)" {o(6)}/>')
    # труба и дымоход
    s += (f'<rect x="{x+w_*.62:.0f}" y="{y-h_*.18:.0f}" width="{w_*.2:.0f}"'
          f' height="{h_*.2:.0f}" rx="6" fill="url(#pech)" {o(8)}/>')
    # утварь на лежанке
    s += (f'<rect x="{x+w_*.08:.0f}" y="{y+h_*.2:.0f}" width="{w_*.14:.0f}"'
          f' height="{h_*.08:.0f}" rx="6" fill="{PECH2}" {o(5)}/>')
    return s


def spina(x, y, h_, t, col="#3a3448", platok=None, ph=0.0, kant="#cfd8dd"):
    """Человек СО СПИНЫ: плечи, шея, затылок, по желанию платок или шапка.
    Капля из общей базы в кадре читается лампочкой — для очередей своя фигура."""
    k = h_ / 620.0
    dy = 2.6 * A.w(t, 2.4, ph)
    s = ten(x, y + 10, 90 * k, 22 * k, .45)
    s += f'<g transform="translate(0,{dy:.1f})">'
    # пальто/спина с плечами
    s += (f'<path d="M{x-96*k:.0f},{y}'
          f' q-{6*k:.0f},-{250*k:.0f} {26*k:.0f},-{300*k:.0f}'
          f' q{70*k:.0f},-{40*k:.0f} {140*k:.0f},0'
          f' q{32*k:.0f},{50*k:.0f} {26*k:.0f},{300*k:.0f} z"'
          f' fill="{col}" {o(6, kant)}/>')
    # шея и затылок
    s += (f'<rect x="{x-22*k:.0f}" y="{y-330*k:.0f}" width="{44*k:.0f}"'
          f' height="{50*k:.0f}" rx="{14*k:.0f}" fill="#d8ab86" {o(4)}/>')
    s += (f'<ellipse cx="{x}" cy="{y-392*k:.0f}" rx="{64*k:.0f}" ry="{72*k:.0f}"'
          f' fill="#e2b58e" {o(5)}/>')
    # волосы/затылок
    s += (f'<path d="M{x-64*k:.0f},{y-392*k:.0f} q{4*k:.0f},-{86*k:.0f} {64*k:.0f},-{84*k:.0f}'
          f' q{60*k:.0f},-{2*k:.0f} {64*k:.0f},{84*k:.0f}'
          f' q-{20*k:.0f},{30*k:.0f} -{128*k:.0f},0 z" fill="#4a3b2e" {o(4)}/>')
    if platok:
        s += (f'<path d="M{x-72*k:.0f},{y-380*k:.0f}'
              f' q{6*k:.0f},-{104*k:.0f} {72*k:.0f},-{100*k:.0f}'
              f' q{68*k:.0f},-{4*k:.0f} {72*k:.0f},{100*k:.0f}'
              f' q-{30*k:.0f},{56*k:.0f} -{144*k:.0f},0 z" fill="{platok}" {o(5)}/>')
        s += (f'<path d="M{x-36*k:.0f},{y-300*k:.0f} q{36*k:.0f},{26*k:.0f} {72*k:.0f},0"'
              f' fill="none" stroke="{platok}" stroke-width="{18*k:.0f}"/>')
    s += '</g>'
    return s


def babka(x, y, h_, t, profil=True, platok=TKAN, ph=0.0, ruka_ugol=0.0,
          fartuk=TKAN2, vpravo=True):
    """Бабушка: плечи, кофта, фартук, платок сзади, живое лицо в профиль."""
    k = h_ / 620.0
    dy = 3.4 * A.w(t, 1.9, ph)
    sx = 1 if vpravo else -1
    s = ten(x, y + 14, 160 * k, 32 * k, .5)
    s += f'<g transform="translate(0,{dy:.1f})">'
    # юбка
    s += (f'<path d="M{x-110*k:.0f},{y} q{18*k:.0f},-{300*k:.0f} {110*k:.0f},-{310*k:.0f}'
          f' q{92*k:.0f},{10*k:.0f} {110*k:.0f},{310*k:.0f} z" fill="#4a4152" {o(7)}/>')
    s += (f'<path d="M{x-84*k:.0f},{y-60*k:.0f} q{84*k:.0f},{20*k:.0f} {168*k:.0f},0"'
          f' fill="none" stroke="#2f2a38" stroke-width="{7*k:.1f}" opacity=".5"/>')
    # фартук
    s += (f'<path d="M{x-72*k:.0f},{y-30*k:.0f} q{72*k:.0f},{16*k:.0f} {144*k:.0f},0'
          f' l-{18*k:.0f},-{262*k:.0f} q-{54*k:.0f},-{20*k:.0f} -{108*k:.0f},0 z"'
          f' fill="{fartuk}" {o(6)}/>')
    s += (f'<path d="M{x-56*k:.0f},{y-170*k:.0f} q{56*k:.0f},{18*k:.0f} {112*k:.0f},0"'
          f' fill="none" stroke="#ffffff" stroke-width="{6*k:.1f}" opacity=".3"/>')
    # кофта с плечами и воротом
    s += (f'<path d="M{x-96*k:.0f},{y-300*k:.0f}'
          f' q{10*k:.0f},-{120*k:.0f} {40*k:.0f},-{150*k:.0f}'
          f' q{56*k:.0f},-{26*k:.0f} {112*k:.0f},0'
          f' q{30*k:.0f},{30*k:.0f} {40*k:.0f},{150*k:.0f}'
          f' q-{96*k:.0f},{38*k:.0f} -{192*k:.0f},0 z" fill="#6b5a6e" {o(7)}/>')
    s += (f'<path d="M{x-40*k:.0f},{y-446*k:.0f} q{40*k:.0f},{26*k:.0f} {80*k:.0f},0"'
          f' fill="none" stroke="#574a5c" stroke-width="{8*k:.1f}"/>')
    # рука: плечо → предплечье → ладонь у лица
    rx = x + sx * 46 * k
    s += (f'<g transform="rotate({ruka_ugol:.1f},{rx:.0f},{y-400*k:.0f})">'
          f'<path d="M{rx:.0f},{y-400*k:.0f} q{sx*80*k:.0f},{26*k:.0f} {sx*112*k:.0f},-{48*k:.0f}"'
          f' fill="none" stroke="#6b5a6e" stroke-width="{44*k:.0f}" stroke-linecap="round"/>'
          f'<ellipse cx="{rx+sx*122*k:.0f}" cy="{y-452*k:.0f}" rx="{34*k:.0f}"'
          f' ry="{40*k:.0f}" fill="#e8bb93" {o(5)}/></g>')
    # шея и голова
    s += (f'<rect x="{x-18*k:.0f}" y="{y-496*k:.0f}" width="{36*k:.0f}"'
          f' height="{54*k:.0f}" rx="{12*k:.0f}" fill="#dcb08a" {o(4)}/>')
    hy = y - 536 * k
    # платок сзади головы — лицо открыто
    s += (f'<path d="M{x-sx*62*k:.0f},{hy+50*k:.0f}'
          f' q-{sx*30*k:.0f},-{130*k:.0f} {sx*56*k:.0f},-{140*k:.0f}'
          f' q{sx*86*k:.0f},-{6*k:.0f} {sx*92*k:.0f},{70*k:.0f}'
          f' q-{sx*30*k:.0f},-{34*k:.0f} -{sx*74*k:.0f},-{24*k:.0f}'
          f' q-{sx*56*k:.0f},{18*k:.0f} -{sx*44*k:.0f},{94*k:.0f} z"'
          f' fill="{platok}" {o(6)}/>')
    s += _golova_profil(x, hy, k, t, ph, "#edc49c", vpravo)
    # узел платка и спадающий конец
    s += (f'<path d="M{x-sx*64*k:.0f},{hy+16*k:.0f} q-{sx*54*k:.0f},{40*k:.0f}'
          f' -{sx*30*k:.0f},{112*k:.0f} q{sx*42*k:.0f},-{26*k:.0f} {sx*56*k:.0f},-{98*k:.0f} z"'
          f' fill="{platok}" {o(5)}/>')
    s += (f'<circle cx="{x-sx*58*k:.0f}" cy="{hy+20*k:.0f}" r="{14*k:.0f}"'
          f' fill="{platok}" {o(4)}/>')
    s += '</g>'
    return s


def muzh(x, y, h_, t, ph=0.0, sviter="#3f5c7a", vpravo=False):
    """Мужчина за столом: плечи, свитер, короткая стрижка, живое лицо."""
    k = h_ / 620.0
    dy = 3.0 * A.w(t, 2.2, ph)
    s = ten(x, y + 12, 150 * k, 30 * k, .5)
    s += f'<g transform="translate(0,{dy:.1f})">'
    s += (f'<path d="M{x-104*k:.0f},{y} q{14*k:.0f},-{280*k:.0f} {104*k:.0f},-{292*k:.0f}'
          f' q{90*k:.0f},{12*k:.0f} {104*k:.0f},{292*k:.0f} z" fill="#2f3845" {o(7)}/>')
    s += (f'<path d="M{x-100*k:.0f},{y-290*k:.0f}'
          f' q{12*k:.0f},-{130*k:.0f} {46*k:.0f},-{158*k:.0f}'
          f' q{54*k:.0f},-{24*k:.0f} {108*k:.0f},0'
          f' q{34*k:.0f},{28*k:.0f} {46*k:.0f},{158*k:.0f}'
          f' q-{100*k:.0f},{40*k:.0f} -{200*k:.0f},0 z" fill="{sviter}" {o(7)}/>')
    s += (f'<path d="M{x-44*k:.0f},{y-452*k:.0f} q{44*k:.0f},{28*k:.0f} {88*k:.0f},0"'
          f' fill="none" stroke="#2e4257" stroke-width="{9*k:.1f}"/>')
    s += (f'<rect x="{x-20*k:.0f}" y="{y-500*k:.0f}" width="{40*k:.0f}"'
          f' height="{56*k:.0f}" rx="{13*k:.0f}" fill="#dcb08a" {o(4)}/>')
    hy = y - 540 * k
    s += _golova_profil(x, hy, k, t, ph, "#e8bb93", vpravo)
    # короткая стрижка
    sx = 1 if vpravo else -1
    s += (f'<path d="M{x-sx*56*k:.0f},{hy-6*k:.0f}'
          f' q{sx*4*k:.0f},-{76*k:.0f} {sx*62*k:.0f},-{72*k:.0f}'
          f' q{sx*50*k:.0f},{4*k:.0f} {sx*52*k:.0f},{40*k:.0f}'
          f' q-{sx*40*k:.0f},-{22*k:.0f} -{sx*114*k:.0f},{32*k:.0f} z"'
          f' fill="#4a3b2e" {o(5)}/>')
    s += '</g>'
    return s


def ruka(x, y, t, dl=190, ugol=0.0, ladon=38, rukav="#6b5a6e", palcy=True):
    """Рука: рукав с манжетой, сужающееся предплечье, кисть с пальцами.
    Палка с шаром на конце в кадре читается браком (лист 13.11)."""
    s = f'<g transform="rotate({ugol:.1f},{x},{y})">'
    # рукав
    s += (f'<path d="M{x},{y-ladon*.95:.0f} h{dl*.52:.0f}'
          f' q{dl*.1:.0f},{ladon*.1:.0f} {dl*.1:.0f},{ladon*.35:.0f}'
          f' v{ladon*.9:.0f} q0,{ladon*.3:.0f} -{dl*.1:.0f},{ladon*.35:.0f}'
          f' h-{dl*.52:.0f} z" fill="{rukav}" {o(6)}/>')
    s += (f'<rect x="{x+dl*.56:.0f}" y="{y-ladon*.8:.0f}" width="{dl*.08:.0f}"'
          f' height="{ladon*1.6:.0f}" rx="{ladon*.2:.0f}" fill="{rukav}"'
          f' {o(5)} opacity=".95"/>')
    # предплечье и запястье
    s += (f'<path d="M{x+dl*.62:.0f},{y-ladon*.62:.0f} h{dl*.2:.0f}'
          f' q{ladon*.3:.0f},{ladon*.62:.0f} 0,{ladon*1.24:.0f}'
          f' h-{dl*.2:.0f} z" fill="#e8bb93" {o(5)}/>')
    # кисть
    s += (f'<path d="M{x+dl*.82:.0f},{y-ladon*.66:.0f}'
          f' q{ladon*1.1:.0f},-{ladon*.1:.0f} {ladon*1.25:.0f},{ladon*.5:.0f}'
          f' q{ladon*.1:.0f},{ladon*.6:.0f} -{ladon*.5:.0f},{ladon*.86:.0f}'
          f' q-{ladon*.7:.0f},{ladon*.1:.0f} -{ladon*.75:.0f},-{ladon*.2:.0f} z"'
          f' fill="#e8bb93" {o(5)}/>')
    if palcy:
        for j in range(3):
            yy = y - ladon * .44 + j * ladon * .42
            s += (f'<path d="M{x+dl*.82+ladon*1.1:.0f},{yy:.0f}'
                  f' q{ladon*.5:.0f},{ladon*.06:.0f} {ladon*.62:.0f},{ladon*.26:.0f}"'
                  f' fill="none" stroke="#e8bb93" stroke-width="{ladon*.3:.0f}"'
                  f' stroke-linecap="round"/>')
        # большой палец
        s += (f'<path d="M{x+dl*.86:.0f},{y+ladon*.5:.0f}'
              f' q{ladon*.5:.0f},{ladon*.4:.0f} {ladon*.95:.0f},{ladon*.16:.0f}"'
              f' fill="none" stroke="#e8bb93" stroke-width="{ladon*.34:.0f}"'
              f' stroke-linecap="round"/>')
    return s + '</g>'


def kuhnya_utvar(t, seed=4, bez_pravoy=False):
    """Обжитая стена кухни: полка с банками, связка лука, ходики, рушник.
    Без неё кадр пустой — брак первого листа 13.11 (R-0019, «Голливуд»)."""
    r = random.Random(seed)
    s = ""
    pr = 900 if bez_pravoy else W - 120
    # навесная полка с банками и крынками
    s += (f'<rect x="90" y="300" width="{min(760, pr-90)}" height="22" rx="6"'
          f' fill="url(#dosk)" {o(6)}/>')
    for i in range(5):
        xx = 150 + i * 140
        if xx > pr - 60:
            break
        hh = 70 + r.randrange(0, 40)
        s += (f'<rect x="{xx-38}" y="{300-hh}" width="76" height="{hh}" rx="8"'
              f' fill="url(#stekl)" {o(5)}/>'
              f'<rect x="{xx-38}" y="{300-hh}" width="76" height="16" rx="5"'
              f' fill="{ZHELEZ}" {o(4)}/>'
              f'<ellipse cx="{xx}" cy="{300-hh*.45:.0f}" rx="26" ry="{hh*.3:.0f}"'
              f' fill="{["#8a6038","#5d7a3a","#b2552f","#c08a3e"][i%4]}" opacity=".85"/>')
    # связка лука качается
    kach = 3 * A.w(t, 2.8)
    if not bez_pravoy:
        s += (f'<g transform="rotate({kach:.1f},1520,250)">'
              f'<path d="M1520,250 v90" {o(6)} fill="none"/>'
              + "".join(f'<circle cx="{1500+j%2*42}" cy="{350+j*46}" r="30"'
                        f' fill="url(#solom)" {o(5)}/>' for j in range(4))
              + '</g>')
    # ходики с маятником
    s += hodiki(1180 if not bez_pravoy else 760, 250, t, 1.3)
    # рушник на гвозде — в левой трети, окну не мешает
    s += (f'<path d="M60,300 h130 q-8,200 -65,210 q-57,-10 -65,-210 z"'
          f' fill="url(#rush)" {o(5)}/>'
          f'<path d="M68,412 h114" stroke="{TKAN}" stroke-width="9" opacity=".85"/>')
    # половик на полу
    s += (f'<path d="M160,{H-120} h620 l-60,70 h-500 z" fill="{TKAN2}" {o(5)}'
          f' opacity=".9"/>'
          + "".join(f'<path d="M{200+j*110},{H-116} l-56,62" stroke="#e3d6b4"'
                    f' stroke-width="7" opacity=".6"/>' for j in range(5)))
    return s


def kuhnya_stena(t, tepl=True, okno_x=None, sumer=False, utvar=True, seed=4):
    """Фон кухни: побелённая стена, панель по низу, дощатый пол, окно, утварь.
    Стена не остаётся голой: голый фон — главный брак первого листа."""
    neb = "nsumer" if sumer else "nden"
    s = f'<rect x="0" y="0" width="{W}" height="{H}" fill="{POBEL if tepl else "#cfd6d2"}"/>'
    # крашеная панель по низу стены — кадр перестаёт быть пустым
    s += (f'<rect x="0" y="{H-470}" width="{W}" height="210" fill="{"#7a8f86" if tepl else "#8a9a98"}"/>'
          f'<rect x="0" y="{H-478}" width="{W}" height="14" rx="5" fill="url(#dosk)" {o(0)}/>')
    s += f'<rect x="0" y="{H-260}" width="{W}" height="260" fill="url(#pol)"/>'
    s += polovicy(H - 260)
    if utvar:
        s += kuhnya_utvar(t, seed, okno_x is not None and okno_x < 1000)
    if okno_x is not None:
        s += (f'<rect x="{okno_x-20}" y="140" width="460" height="420" rx="12"'
              f' fill="url(#dosk)" {o(8)}/>')
        s += (f'<rect x="{okno_x}" y="160" width="420" height="380" rx="8"'
              f' fill="url(#{neb})" {o(7)}/>')
        s += (f'<path d="M{okno_x+210},160 v380 M{okno_x},350 h420" {o(7)} fill="none"/>')
        # заиндевелые углы и сугробы на отливе
        for cx, cy in ((okno_x+40, 200), (okno_x+380, 200), (okno_x+40, 390), (okno_x+380, 390)):
            s += (f'<circle cx="{cx}" cy="{cy}" r="52" fill="{INEY}" opacity=".45"/>')
        s += (f'<ellipse cx="{okno_x+120}" cy="520" rx="90" ry="26" fill="{SNEG}" opacity=".7"/>'
              f'<ellipse cx="{okno_x+300}" cy="524" rx="70" ry="20" fill="{SNEG}" opacity=".6"/>')
        s += sneg_letit(t, 16, 9, .5, .7)
        # занавески: две шторы по бокам и тонкий ламбрекен сверху
        for sgn, x0 in ((-1, okno_x - 10), (1, okno_x + 430)):
            s += (f'<path d="M{x0},150 q{sgn*70},120 {sgn*34},410 q{-sgn*40},-30 {-sgn*74},-410 z"'
                  f' fill="url(#rush)" {o(5)} opacity=".95"/>')
        s += (f'<rect x="{okno_x-40}" y="132" width="500" height="44" rx="10"'
              f' fill="{TKAN}" {o(5)} opacity=".9"/>')
        s += (f'<rect x="{okno_x-40}" y="548" width="500" height="26" rx="7"'
              f' fill="url(#dosk)" {o(6)}/>')
    if tepl:
        s += teplo(W * .42, 560, 1100, 820, .45)
    return s


# ═══════════════ БЛОК 1. ОТКРЫТИЕ ═══════════════
def stol_s_kotorogo_uhodyat(t):
    """План 1. Со стола уезжает скоромное: мясо, яйца, молоко. Титр справа."""
    s = SL(Z_DAL, kuhnya_stena(t, True, 1240))
    # плита слева, с неё идёт пар
    s += SL(Z_SRED, f'<rect x="40" y="600" width="330" height="230" rx="14"'
                    f' fill="url(#zhel)" {o(8)}/>'
                    f'<ellipse cx="150" cy="606" rx="66" ry="22" fill="{CHUGUN}" {o(5)}/>'
                    f'<ellipse cx="290" cy="606" rx="54" ry="18" fill="{CHUGUN}" {o(5)}/>'
                    + par(150, 560, t, 6, .5, 240, .4, 1.2))
    s += SL(Z_SRED, stol_bok(150, 650, 1040, 300, t))
    # мясо на доске уезжает за левый край
    k1 = A.ease(A.seg(t, .6, 1.2))
    s += SL(Z_PERED, f'<g transform="translate({-900*k1:.0f},0)" opacity="{1-k1*.35:.2f}">'
            + ten(400, 646, 150, 22, .5)
            + f'<rect x="250" y="596" width="300" height="34" rx="9" fill="url(#dosk)" {o(6)}/>'
            + f'<path d="M296,596 q40,-82 134,-62 q92,20 76,62 z" fill="#b8503f" {o(6)}/>'
            + f'<path d="M330,558 q46,-26 96,-10" fill="none" stroke="#f3dccd" stroke-width="10"/>'
            + f'<path d="M352,586 q40,-14 76,-4" fill="none" stroke="#8e3a2e" stroke-width="7"/>'
            + '</g>')
    # решето с яйцами уезжает, яйца перекатываются
    k2 = A.ease(A.seg(t, 2.0, 1.1))
    kach = 11 * A.w(t, .7)
    s += SL(Z_PERED, f'<g transform="translate({-1000*k2:.0f},0)">'
            + ten(700, 650, 140, 20, .45)
            + f'<ellipse cx="700" cy="614" rx="140" ry="46" fill="url(#solom)" {o(7)}/>'
            + f'<ellipse cx="700" cy="604" rx="112" ry="34" fill="#d8bd82" opacity=".8"/>'
            + "".join(f'<ellipse cx="{640+i*60+kach*(1 if i%2 else -1):.0f}" cy="{590-i%2*8}"'
                      f' rx="30" ry="38" fill="#f6eddc" {o(5)}/>'
                      f'<ellipse cx="{632+i*60:.0f}" cy="{578-i%2*8}" rx="11" ry="15"'
                      f' fill="#ffffff" opacity=".55"/>' for i in range(3)))
    s += SL(Z_PERED, '</g>')
    # крынка молока уезжает, покачиваясь
    k3 = A.ease(A.seg(t, 3.4, 1.2))
    naklon = 8 * A.w(t, .8)
    s += SL(Z_PERED, f'<g transform="translate({-1100*k3:.0f},0) rotate({naklon:.1f},1000,620)">'
            + ten(1000, 652, 90, 18, .45) + krynka(1000, 644, 2.0) + '</g>')
    s += SL(Z_PERED, ramka_pp("levo", "#1a1309", .22))
    s += _vinetka(.40)
    return s


def ryba_na_blyude(t):
    """План 2. На опустевший стол въезжает блюдо с запечённой рыбой."""
    s = SL(Z_DAL, kuhnya_stena(t, True, 1240))
    s += SL(Z_SRED, stol_bok(120, 660, 1000, 290, t))
    k = A.out(A.seg(t, .15, .9))
    dx = -700 * (1 - k)
    s += SL(Z_PERED, f'<g transform="translate({dx:.0f},0)">'
            + ten(560, 666, 290, 36, .5)
            + f'<ellipse cx="560" cy="636" rx="290" ry="86" fill="url(#krem)" {o(7)}/>'
            + f'<ellipse cx="560" cy="624" rx="240" ry="64" fill="#e8dcc2" opacity=".75"/>'
            + ryba(560, 606, 1.7, t)
            + f'<ellipse cx="430" cy="600" rx="62" ry="15" fill="#ffffff" opacity=".4"/>'
            + '</g>')
    s += SL(Z_PERED, par(540, 530, t, 7, .55, 280, .4, 1.6))
    # кот выглядывает из-под стола
    vyh = A.ease(A.seg(t, 1.4, .8))
    s += SL(Z_PERED, f'<g transform="translate(0,{90-80*vyh:.0f})" opacity="{vyh:.2f}">'
            + kot(300, 946, t, 1.1) + '</g>')
    s += _vinetka(.42)
    return s


def dve_tropinki_v_snegu(t):
    """Планы 3-4. Две тропинки: строгая и мягкая. Правая становится пушистой."""
    s = SL(Z_NEBO, nebo("rassv", t, False) + oblaka(t, 150, 3, 4, .45))
    s += SL(Z_DAL, f'<rect x="0" y="470" width="{W}" height="{H-470}" fill="url(#sneg)"/>')
    s += SL(Z_DAL, _sneg_lezhit(470, 30))
    # мир вокруг тропинок: дом вдали, деревья, плетень и вешки
    s += SL(Z_DAL, izba_snaruzhi(1360, 500, 330, t, True, True, 21))
    s += SL(Z_DAL, dym(1470, 376, t, 5, .2, 240, .4))
    for i, (xx, hh) in enumerate(((180, 300), (430, 240), (1700, 270))):
        s += SL(Z_DAL, f'<path d="M{xx},{520} v-{hh}" {o(14)} fill="none"/>'
                + "".join(f'<path d="M{xx},{520-hh+j*46} l{-70+j*12},{38}'
                          f' M{xx},{520-hh+j*46} l{70-j*12},{38}" {o(9)} fill="none"/>'
                          for j in range(4))
                + f'<ellipse cx="{xx}" cy="{514}" rx="70" ry="22" fill="{SNEG}" opacity=".8"/>')
    s += SL(Z_SRED, pleten(40, 560, 520, 150, 11))
    for i in range(5):
        xx = 1500 + i * 86
        s += SL(Z_SRED, f'<path d="M{xx},{700+i*40} v-110" {o(8)} fill="none"/>'
                + f'<path d="M{xx},{590+i*40} l22,26 l-44,0 z" fill="{ZEL}" {o(4)}/>')
    # левая тропинка — узкая, утоптанная до льда
    s += SL(Z_SRED, f'<path d="M700,{H} q-60,-280 90,-620" fill="none"'
                    f' stroke="{LED}" stroke-width="54" opacity=".85"/>'
                    f'<path d="M700,{H} q-60,-280 90,-620" fill="none"'
                    f' stroke="{INEY}" stroke-width="26" opacity=".7"/>')
    # правая — на слове «мягкий» становится пушистой
    pysh = A.ease(A.seg(t, .8, .9))
    s += SL(Z_SRED, f'<path d="M1180,{H} q70,-290 -30,-620" fill="none"'
                    f' stroke="#ffffff" stroke-width="{60+40*pysh:.0f}" opacity="{.5+.4*pysh:.2f}"/>')
    # следы валенок проступают по правой
    for i in range(6):
        kk = A.seg(t, .9 + i * .22, .3)
        if kk <= 0:
            continue
        yy = H - 80 - i * 150
        xx = 1176 + 46 * math.sin(i * 1.1) + i * -4
        s += SL(Z_PERED, f'<ellipse cx="{xx:.0f}" cy="{yy}" rx="{30*kk:.0f}"'
                         f' ry="{15*kk:.0f}" fill="#b9cfe2" opacity="{.6*kk:.2f}"/>')
    s += SL(Z_LETIT, _sneg_letit(t, 30, 7, .5, .8))
    # позёмка
    s += SL(Z_PERED, _tuman(t, 940, .3, "#e8f1fb"))
    s += SL(Z_PERED, f'<ellipse cx="960" cy="520" rx="700" ry="90"'
                     f' fill="#ffffff" opacity="{.12+.06*A.w(t,3.4):.2f}"/>')
    s += _vinetka(.4)
    return s


def dlinnaya_polka_razreshennogo(t):
    """Планы 5-6. На полку по слову встают семь разрешённых блюд."""
    s = SL(Z_DAL, kuhnya_stena(t, True, None, False, False))
    # вторая полка под потолком: кринки и короба, чтобы верх кадра не пустовал
    s += SL(Z_DAL, f'<rect x="120" y="250" width="1680" height="26" rx="7"'
                   f' fill="url(#dosk)" {o(6)}/>')
    for i in range(7):
        xx = 220 + i * 240
        s += SL(Z_DAL, krynka(xx, 250, 1.0) if i % 2 else
                f'<rect x="{xx-56}" y="160" width="112" height="90" rx="10"'
                f' fill="url(#solom)" {o(5)}/>'
                f'<path d="M{xx-56},196 h112" stroke="#b58a42" stroke-width="6"/>')
    s += SL(Z_SRED, f'<rect x="40" y="690" width="1840" height="40" rx="8"'
                    f' fill="url(#dosk)" {o(8)}/>'
                    f'<rect x="40" y="730" width="1840" height="16" fill="{DOSKA2}" opacity=".8"/>')
    for i in range(4):
        s += SL(Z_SRED, f'<path d="M{220+i*500},746 l40,74" {o(8)} fill="none"/>')
    pred = [
        (190, lambda: tarelka(190, 666, 96, t) + ryba(190, 640, .7, t)),
        (450, lambda: "".join(f'<path d="M{410+j*34},{520+j*8} q14,66 4,96"'
                              f' fill="none" stroke="#7a5a3a" stroke-width="9"/>'
                              f'<path d="M{392+j*34},{512+j*8} q20,-30 40,0 q-6,26 -40,0 z"'
                              f' fill="#8a6038" {o(4)}/>' for j in range(4))
              + f'<path d="M380,500 h150" stroke="#6b4a2c" stroke-width="7"/>'),
        (730, lambda: gorshok(730, 684, 1.5, t)),
        (980, lambda: ten(980, 684, 130, 20, .45)
              + f'<path d="M860,684 q14,-116 120,-116 q106,0 120,116 z" fill="url(#solom)" {o(7)}/>'
              + f'<path d="M896,620 q84,-26 168,0" fill="none" stroke="#c89a4e" stroke-width="9"/>'
              + f'<ellipse cx="930" cy="640" rx="26" ry="9" fill="#fff0cf" opacity=".5"/>'),
        (1240, lambda: ten(1240, 686, 90, 18, .45)
               + f'<rect x="1162" y="540" width="156" height="146" rx="12"'
                 f' fill="url(#stekl)" {o(7)}/>'
               + f'<rect x="1162" y="520" width="156" height="30" rx="8" fill="{ZHELEZ}" {o(5)}/>'
               + "".join(f'<ellipse cx="{1196+j*36}" cy="{596+j*26}" rx="24" ry="15"'
                         f' fill="{ZEL2}" opacity=".9"/>' for j in range(3))),
        (1500, lambda: tarelka(1500, 672, 92, t)
               + "".join(f'<ellipse cx="{1458+j*40}" cy="{644+(j%2)*14}" rx="27" ry="20"'
                         f' fill="#c99a62" {o(5)}/>' for j in range(3))),
        (1740, lambda: ten(1740, 686, 86, 18, .45)
               + f'<path d="M1660,686 q-8,-120 80,-120 q88,0 80,120 z" fill="url(#med)" {o(7)}/>'
               + f'<ellipse cx="1740" cy="566" rx="80" ry="24" fill="{MED}" {o(5)}/>'
               + f'<ellipse cx="1712" cy="560" rx="26" ry="9" fill="#ffe7b0" opacity=".6"/>'),
    ]
    for i, (xx, f) in enumerate(pred):
        k = A.over(A.seg(t, .25 + i * .52, .34))
        if k <= 0:
            continue
        kk = min(1.0, k)
        s += SL(Z_PERED, f'<g opacity="{kk:.2f}" transform="translate(0,{-40*(1-kk):.0f})">'
                + f() + '</g>')
    # мёд тянется с ложки
    kt = A.seg(t, 3.9, 1.6)
    if kt > 0:
        s += SL(Z_PERED, f'<path d="M1790,560 q8,{56*kt:.0f} -6,{120*kt:.0f}"'
                         f' fill="none" stroke="{MED}" stroke-width="12"'
                         f' stroke-linecap="round" opacity=".92"/>')
    s += _vinetka(.4)
    return s


def babushka_u_plity_schitaet_na_palca(t):
    """План 7. Бабушка в профиль у плиты загибает пальцы."""
    s = SL(Z_DAL, kuhnya_stena(t, True, 1340))
    # плита крупно
    s += SL(Z_SRED, f'<rect x="980" y="620" width="520" height="300" rx="16"'
                    f' fill="url(#zhel)" {o(8)}/>'
            + f'<rect x="1000" y="646" width="480" height="26" rx="8" fill="{CHUGUN}" opacity=".6"/>'
            + f'<rect x="1020" y="760" width="440" height="140" rx="10" fill="#3c4147" {o(6)}/>'
            + f'<rect x="1060" y="790" width="360" height="80" rx="8" fill="#20262b" {o(5)}/>')
    s += SL(Z_SRED, f'<path d="M1100,620 q-30,-130 150,-130 q180,0 150,130 z"'
                    f' fill="url(#chug)" {o(7)}/>'
            + f'<ellipse cx="1250" cy="490" rx="152" ry="30" fill="{ZHELEZ}" {o(5)}/>')
    s += SL(Z_SRED, par(1250, 450, t, 7, .55, 300, .4, 1.4))
    # на стене только половник и сито
    s += SL(Z_DAL, f'<path d="M1640,250 v190 q0,50 50,50" fill="none" {o(10)}/>'
            + f'<ellipse cx="1714" cy="498" rx="56" ry="30" fill="url(#zhel)" {o(7)}/>')
    s += SL(Z_DAL, f'<circle cx="1800" cy="300" r="80" fill="url(#solom)" {o(8)}/>'
            + f'<circle cx="1800" cy="300" r="58" fill="#d8c08a" opacity=".6"/>')
    # бабушка крупно, в профиль, считает на пальцах
    n = min(5, int(A.seg(t, .5, 2.4) * 5.99))
    ug = -8 - 5 * n
    s += SL(Z_PERED, babka(600, 1010, 700, t, True, TKAN, .0, ug))
    # загнутые пальцы у поднятой ладони
    for j in range(5):
        sogn = j < n
        yy = 560 - j * 16
        s += SL(Z_PERED, f'<path d="M742,{yy} q{30 if not sogn else 10},{-8 if not sogn else 14}'
                         f' {44 if not sogn else 14},{0 if not sogn else 28}"'
                         f' fill="none" stroke="#e8bb93" stroke-width="15"'
                         f' stroke-linecap="round"/>')
    s += SL(Z_PERED, ramka_pp("pravo", "#1a1309", .22))
    s += _vinetka(.44)
    return s


def sem_tarelok_na_polke(t):
    """Планы 8, 14. Семь тарелок с бирками дней, рука кладёт в каждую своё."""
    s = SL(Z_DAL, kuhnya_stena(t, True, None, False, True, 7))
    s += SL(Z_SRED, f'<rect x="20" y="720" width="1880" height="42" rx="9"'
                    f' fill="url(#dosk)" {o(8)}/>'
            + f'<rect x="20" y="762" width="1880" height="18" fill="{DOSKA2}" opacity=".8"/>')
    dni = ("Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс")
    for i, d in enumerate(dni):
        xx = 160 + i * 270
        strog = d in ("Ср", "Пт")
        s += SL(Z_SRED, tarelka(xx, 700, 118, t, "url(#krem)", True,
                                0 if strog else (2 if i % 2 else 1)))
        # в тарелке своё: каша, рыба, картошка
        vid = i % 3
        if not strog:
            if vid == 0:
                s += SL(Z_SRED, f'<ellipse cx="{xx}" cy="686" rx="72" ry="26"'
                                f' fill="#d9bd86" {o(4)}/>')
            elif vid == 1:
                s += SL(Z_SRED, ryba(xx, 684, .5, t))
            else:
                s += SL(Z_SRED, "".join(f'<ellipse cx="{xx-32+j*32}" cy="{684+(j%2)*8}"'
                                        f' rx="22" ry="16" fill="#c99a62" {o(4)}/>'
                                        for j in range(3)))
        s += SL(Z_PERED, plashka_dnya(xx, 790, d, t, .2 + i * .12))
    # рука идёт вдоль ряда
    hod = A.seg(t, .5, 2.6)
    hx = 120 + hod * 1660
    s += SL(Z_PERED, f'<g transform="translate({hx-120:.0f},{30*math.sin(hod*9):.0f})">'
            + ruka(-40, 430, t, 230, 58, 52) + '</g>')
    s += _vinetka(.4)
    return s


def dvoe_za_stolom_tarelki_v_storone(t):
    """План 9. Камера от тарелок вверх: два силуэта, между ними пустое место."""
    s = SL(Z_DAL, kuhnya_stena(t, True, 1420, True, True, 11))
    # лампа низко над столом, покачивается
    kach = 2.6 * A.w(t, 3.2)
    s += SL(Z_SRED, f'<g transform="rotate({kach:.1f},900,60)">'
            + f'<path d="M900,60 v230" {o(7)} fill="none"/>'
            + lampa(900, 330, t, 2.0, True) + '</g>')
    s += SL(Z_SRED, teplo(900, 560, 820, 560, .55))
    # сперва сидящие люди, потом стол перед ними: торс выше столешницы
    pov = 5 * A.ease(A.seg(t, 2.2, 1.6))
    s += SL(Z_SRED, f'<g transform="rotate({pov:.1f},560,1010)">'
            + babka(560, 1010, 760, t, True, "#5e6b7a", .2, -4) + '</g>')
    s += SL(Z_SRED, f'<g transform="rotate({-pov:.1f},1340,1010)">'
            + muzh(1340, 1010, 790, t, .3, "#3f5c7a", False) + '</g>')
    # стол передним краем у нижней кромки: торсы остаются над столешницей
    s += SL(Z_PERED, f'<path d="M60,{H} v-120 q900,-70 1800,0 v120 z"'
            f' fill="#9fb3a0" {o(8)}/>'
            + f'<path d="M60,{H-104} q900,-66 1800,0" fill="none" stroke="#c6d4c2"'
              f' stroke-width="10" opacity=".8"/>')
    # тарелки отъезжают к краю и теряют резкость
    ot = A.ease(A.seg(t, .4, 1.6))
    s += SL(Z_PERED, f'<g opacity="{1-.5*ot:.2f}" transform="translate({-420*ot:.0f},0)">'
            + tarelka(640, 986, 108, t) + tarelka(900, 992, 96, t) + '</g>')
    # пустое место между ними: нетронутая скатерть и одинокая ложка
    s += SL(Z_PERED, f'<ellipse cx="960" cy="1000" rx="210" ry="40" fill="#ffffff" opacity=".12"/>'
            + f'<path d="M900,996 q60,-18 120,0" fill="none" stroke="{ZHELEZ}" stroke-width="12"/>')
    s += SL(Z_PERED, ramka_pp("oba", "#120e0a", .26))
    s += _vinetka(.46)
    return s


def plita_s_tremya_kryshkami(t):
    """План 10. На три слова закрываются котлеты, сало и бульон."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#cfd6d2"/>'
                  f'<rect x="0" y="0" width="{W}" height="300" fill="#b9c3c0"/>'
                  + kladka(0, 300, W, 420, 60, "url(#kamen)"))
    s += SL(Z_SRED, f'<rect x="120" y="640" width="1680" height="300" rx="16"'
                    f' fill="url(#zhel)" {o(8)}/>'
                    f'<rect x="140" y="660" width="1640" height="24" rx="8"'
                    f' fill="{CHUGUN}" opacity=".65"/>')
    # 1. сковорода с котлетами накрывается крышкой
    k1 = A.ease(A.seg(t, .5, .7))
    s += SL(Z_SRED, f'<ellipse cx="420" cy="648" rx="150" ry="46" fill="url(#chug)" {o(6)}/>'
            + "".join(f'<ellipse cx="{360+j*62}" cy="{636}" rx="42" ry="24"'
                      f' fill="#9d5f3a" {o(4)}/>' for j in range(3)))
    s += SL(Z_PERED, f'<g transform="translate(0,{-200*(1-k1):.0f})" opacity="{k1:.2f}">'
            + f'<ellipse cx="420" cy="620" rx="152" ry="40" fill="url(#zhel)" {o(6)}/>'
            + f'<circle cx="420" cy="590" r="16" fill="{CHUGUN}" {o(4)}/></g>')
    # 2. доску с салом накрывает полотенце
    k2 = A.ease(A.seg(t, 2.0, .8))
    s += SL(Z_SRED, f'<rect x="800" y="624" width="300" height="26" rx="8"'
                    f' fill="url(#dosk)" {o(6)}/>'
            + f'<rect x="850" y="588" width="200" height="40" rx="10" fill="#f3e6dc" {o(5)}/>'
            + f'<path d="M850,604 h200" stroke="#d9a79a" stroke-width="7"/>')
    s += SL(Z_PERED, f'<path d="M{790+0*k2},{572-160*(1-k2):.0f} h320 q-10,70 -160,76'
            f' q-150,-6 -160,-76 z" fill="url(#rush)" {o(6)} opacity="{k2:.2f}"/>')
    # 3. под кастрюлей гаснет огонь, пар редеет
    gasn = A.seg(t, 3.6, 1.0)
    s += SL(Z_SRED, f'<path d="M1400,640 q-30,-120 160,-120 q190,0 160,120 z"'
                    f' fill="url(#chug)" {o(6)}/>'
            + f'<ellipse cx="1560" cy="520" rx="162" ry="30" fill="{ZHELEZ}" {o(5)}/>')
    if gasn < 1:
        s += SL(Z_PERED, ogon(1560, 700, t, .7 * (1 - gasn), .3, 3))
    s += SL(Z_PERED, par(1560, 480, t, 5, .5 * (1 - gasn * .8), 200, .4, 1.1))
    s += _vinetka(.42)
    return s


def molochnaya_polka_holodilnika(t):
    """План 11. С полки уезжают вглубь масло, сметана, творог и сыр."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#9aa3a8"/>'
                  + _kvartira_veschi(1500, 980, 420, t, 9))
    # корпус холодильника без названия
    s += SL(Z_SRED, f'<rect x="300" y="120" width="900" height="900" rx="26"'
                    f' fill="#e9ecee" {o(8)}/>')
    mig = .55 + .45 * (0 if A.blink(t, 2.9, .2, .22) else 1)
    s += SL(Z_SRED, f'<rect x="340" y="170" width="820" height="800" rx="18"'
                    f' fill="#cfd8dd" opacity=".9"/>'
            + f'<rect x="340" y="170" width="820" height="800" rx="18"'
              f' fill="url(#holod)" opacity="{mig:.2f}"/>')
    for yy in (430, 660):
        s += SL(Z_SRED, f'<rect x="352" y="{yy}" width="796" height="12" rx="5"'
                        f' fill="#aeb9bf" {o(4)}/>')
    veshi = [
        (470, lambda k: f'<rect x="{420+340*k:.0f}" y="350" width="150" height="70" rx="10"'
                        f' fill="#f7f0dc" {o(5)} opacity="{1-k*.75:.2f}"/>'),
        (700, lambda k: f'<ellipse cx="{700+300*k:.0f}" cy="390" rx="60" ry="26"'
                        f' fill="#f2f4f0" {o(5)} opacity="{1-k*.75:.2f}"/>'
                        f'<rect x="{640+300*k:.0f}" y="390" width="120" height="48" rx="8"'
                        f' fill="#eef1ec" {o(5)} opacity="{1-k*.75:.2f}"/>'),
        (900, lambda k: f'<path d="M{880+280*k:.0f},620 q60,-70 128,0 z" fill="#f6f2e6"'
                        f' {o(5)} opacity="{1-k*.75:.2f}"/>'),
        (1060, lambda k: f'<path d="M{980+240*k:.0f},620 l120,-56 l40,40 l-120,56 z"'
                         f' fill="url(#solom)" {o(5)} opacity="{1-k*.75:.2f}"/>'),
    ]
    for i, (_, f) in enumerate(veshi):
        s += SL(Z_PERED, f(A.ease(A.seg(t, .5 + i * .55, .7))))
    # холодный пар стелется, дверца закрывается
    s += SL(Z_PERED, _tuman(t, 940, .34, "#dbe9f2"))
    zak = A.ease(A.seg(t, 3.6, 1.2))
    s += SL(Z_PERED, f'<g transform="translate({-860*(1-zak):.0f},0)" opacity="{zak:.2f}">'
            + f'<rect x="300" y="120" width="900" height="900" rx="26" fill="#eef1f3" {o(8)}/>'
            + f'<rect x="1120" y="470" width="30" height="190" rx="14" fill="{ZHELEZ}" {o(5)}/>'
            + f'<rect x="330" y="150" width="60" height="840" fill="#ffffff" opacity=".35"/></g>')
    s += _vinetka(.44)
    return s


def yayco_nad_miskoy(t):
    """План 12. Яйцо отводят от сковородки и от миски, кладут в корзинку."""
    s = SL(Z_DAL, kuhnya_stena(t, True, 1400, False, True, 13))
    s += SL(Z_SRED, stol_bok(60, 700, 1260, 300, t))
    s += SL(Z_SRED, f'<ellipse cx="380" cy="676" rx="220" ry="64" fill="url(#chug)" {o(7)}/>'
            + f'<ellipse cx="380" cy="662" rx="176" ry="46" fill="#3a3634"/>'
            + f'<path d="M598,656 h250" {o(14)} fill="none"/>')
    s += SL(Z_SRED, f'<path d="M820,690 q-26,-130 180,-130 q206,0 180,130 z"'
                    f' fill="url(#krem)" {o(7)}/>'
            + f'<ellipse cx="1000" cy="560" rx="180" ry="42" fill="#f4ecd8" {o(6)}/>'
            + f'<ellipse cx="950" cy="552" rx="54" ry="16" fill="#ffffff" opacity=".5"/>')
    # мука пылит над миской
    for i in range(7):
        ph = (t * .5 + i * .14) % 1.0
        s += SL(Z_PERED, f'<circle cx="{930+i*30}" cy="{536-80*ph:.0f}"'
                         f' r="{6+5*ph:.0f}" fill="#fdf8ee" opacity="{.5*(1-ph):.2f}"/>')
    # яйцо: к сковороде → отвод → к миске → отвод → в корзинку
    fazy = [(.0, 380, 520), (.7, 380, 400), (1.3, 1000, 400), (1.9, 1000, 320),
            (2.4, 1560, 540)]
    x, y = fazy[0][1], fazy[0][2]
    for i in range(len(fazy) - 1):
        k = A.ease(A.seg(t, fazy[i][0], fazy[i + 1][0] - fazy[i][0]))
        x = fazy[i][1] + (fazy[i + 1][1] - fazy[i][1]) * k
        y = fazy[i][2] + (fazy[i + 1][2] - fazy[i][2]) * k
        if k < 1:
            break
    kach = 7 * A.w(t, .9)
    s += SL(Z_PERED, ruka(x - 280, y + 40, t, 250, -6, 46))
    s += SL(Z_PERED, f'<ellipse cx="{x:.0f}" cy="{y+kach:.0f}" rx="38" ry="48"'
                     f' fill="#f6eddc" {o(6)}/>'
            + f'<ellipse cx="{x-12:.0f}" cy="{y-12+kach:.0f}" rx="13" ry="18"'
              f' fill="#ffffff" opacity=".6"/>')
    s += SL(Z_SRED, f'<path d="M1420,700 q0,-120 140,-120 q140,0 140,120 z"'
                    f' fill="url(#solom)" {o(7)}/>'
            + f'<path d="M1420,660 h280" stroke="#b58a42" stroke-width="8" opacity=".7"/>'
            + "".join(f'<ellipse cx="{1480+j*70}" cy="596" rx="34" ry="42"'
                      f' fill="#f2e7d2" {o(5)}/>' for j in range(2)))
    s += _vinetka(.42)
    return s


def korova_i_kurica_u_hleva(t):
    """План 13. Корова и курица у ворот хлева смотрят на дом."""
    s = SL(Z_NEBO, nebo("den", t, False) + oblaka(t, 170, 4, 6, .5))
    s += SL(Z_DAL, _ulica_dal(0, 540, W, t, True, 4))
    s += SL(Z_DAL, f'<rect x="0" y="600" width="{W}" height="{H-600}" fill="url(#sneg)"/>'
            + _sneg_lezhit(600, 26))
    # ворота хлева
    s += SL(Z_SRED, f'<rect x="1120" y="250" width="800" height="480" rx="10"'
                    f' fill="url(#brev)" {o(9)}/>'
            + brevna(1120, 250, 800, 480, 80)
            + f'<path d="M1100,250 l420,-180 l420,180 z" fill="url(#dosk)" {o(9)}/>'
            + f'<rect x="1420" y="400" width="200" height="330" rx="8" fill="#241b14" {o(7)}/>'
            + f'<path d="M1520,70 v-50" {o(6)} fill="none"/>')
    # корова: тело, голова, пятна, жуёт и моргает
    zh = 8 * A.w(t, 1.1)
    s += SL(Z_PERED, ten(640, 960, 300, 44, .5))
    s += SL(Z_PERED, f'<path d="M340,930 q-20,-250 300,-250 q320,0 300,250 z"'
                     f' fill="#f4f0ea" {o(8)}/>'
            + f'<path d="M420,880 q80,-150 220,-140 q60,6 40,70 q-90,10 -140,80 z"'
              f' fill="#4a3a30" opacity=".8"/>'
            + f'<ellipse cx="760" cy="800" rx="60" ry="44" fill="#4a3a30" opacity=".75"/>'
            + f'<rect x="372" y="916" width="48" height="140" rx="16" fill="#e4ded6" {o(6)}/>'
            + f'<rect x="560" y="920" width="48" height="136" rx="16" fill="#e4ded6" {o(6)}/>'
            + f'<rect x="800" y="916" width="48" height="140" rx="16" fill="#e4ded6" {o(6)}/>'
            + f'<path d="M940,700 q70,-40 50,90" fill="none" {o(12)}/>')
    # голова в профиль с рогами и колокольчиком
    s += SL(Z_PERED, f'<g transform="translate(0,{zh:.1f})">'
            + f'<path d="M300,760 q-110,20 -120,140 q-10,120 120,136'
              f' q120,14 140,-110 q18,-130 -140,-166 z" fill="#f7f3ed" {o(7)}/>'
            + f'<ellipse cx="206" cy="900" rx="62" ry="44" fill="#e8b6ae" {o(6)}/>'
            + f'<circle cx="186" cy="890" r="9" fill="{K}"/><circle cx="226" cy="896" r="9" fill="{K}"/>'
            + ('' if A.blink(t, 3.6, .1, .16) else
               f'<circle cx="300" cy="820" r="14" fill="{K}"/>')
            + f'<path d="M250,700 q-40,-80 30,-96 q-14,50 10,80 z" fill="#efe7d6" {o(5)}/>'
            + f'<path d="M340,706 q20,-84 90,-70 q-50,34 -54,84 z" fill="#efe7d6" {o(5)}/>'
            + f'<path d="M258,742 q60,-26 120,-6" fill="none" {o(6)}/>'
            + '</g>')
    kol = 9 * A.w(t, 1.4)
    s += SL(Z_PERED, f'<g transform="rotate({kol:.1f},340,860)">'
            + f'<path d="M340,850 h0" {o(4)} fill="none"/>'
            + f'<path d="M314,864 q26,-54 56,0 q-28,18 -56,0 z" fill="url(#zol)" {o(5)}/>'
            + f'<circle cx="342" cy="880" r="7" fill="{MED}"/></g>')
    # курица переступает и нахохливается
    step = 12 * A.w(t, .8)
    s += SL(Z_PERED, f'<g transform="translate({step:.0f},0)">' + kura(1000, 1000, t, 2.1) + '</g>')
    s += SL(Z_LETIT, _sneg_letit(t, 26, 11, .6, .7))
    s += _vinetka(.42)
    return s


def dver_iz_kuhni(t):
    """План 15. Камера выходит из кухни в проём с занавеской из бус."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#2b2a28"/>')
    # коридор и свет из комнаты за проёмом
    drozh = .78 + .12 * A.w(t, 2.2)
    s += SL(Z_DAL, f'<rect x="700" y="130" width="560" height="950" fill="#6b5a42"/>'
            + f'<rect x="860" y="300" width="250" height="700" rx="8" fill="{SVET}"'
              f' opacity="{drozh:.2f}"/>'
            + teplo(980, 640, 420, 520, .5))
    # косяк проёма
    s += SL(Z_SRED, f'<rect x="620" y="90" width="90" height="990" fill="url(#dosk)" {o(7)}/>'
            + f'<rect x="1250" y="90" width="90" height="990" fill="url(#dosk)" {o(7)}/>'
            + f'<rect x="620" y="90" width="720" height="80" fill="url(#dosk)" {o(7)}/>')
    # занавеска из бус расходится
    razv = A.ease(A.seg(t, .3, 1.4))
    for i in range(16):
        c = i / 15.0 - .5
        xx = 980 + c * 300 + c * 420 * razv
        s += SL(Z_PERED, f'<path d="M{xx:.0f},170 v760" stroke="#b9975c"'
                         f' stroke-width="5" opacity=".9"/>')
        for j in range(9):
            yy = 210 + j * 82 + 10 * A.w(t, 1.6, i * .1 + j * .05)
            s += SL(Z_PERED, f'<circle cx="{xx:.0f}" cy="{yy:.0f}" r="9"'
                             f' fill="{"#d8b06a" if (i+j)%3 else "#8fa8bc"}" {o(2)}/>')
    # кот идёт следом
    kx = 300 + 420 * A.seg(t, .8, 2.4)
    s += SL(Z_PERED, f'<g transform="translate({kx-300:.0f},0)">' + kot(300, 1010, t, .9) + '</g>')
    s += SL(Z_PERED, ramka_pp("oba", "#0e0b08", .34))
    s += _vinetka(.5)
    return s


def garmon_v_chehle_i_korobka_s_fatoy(t):
    """План 16. Гармонь уходит в чехол, крышка коробки накрывает фату."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#cbb79c"/>'
                  f'<rect x="0" y="0" width="{W}" height="{H}" fill="url(#holod)" opacity=".2"/>'
                  + doski(0, 0, W, H, 150, False, "dosk"))
    s += SL(Z_SRED, f'<rect x="120" y="700" width="1680" height="30" rx="8"'
                    f' fill="url(#dosk)" {o(7)}/>')
    # гармонь: меха вздыхают, затем ремешок и чехол
    vzd = 1 + .06 * A.w(t, 1.5)
    zast = A.ease(A.seg(t, 1.0, .8))
    chehol = A.ease(A.seg(t, 1.9, 1.1))
    s += SL(Z_PERED, f'<g transform="translate(420,640) scale({vzd:.3f},1)">'
            + f'<rect x="-170" y="-96" width="86" height="192" rx="12" fill="#8a2f2c" {o(6)}/>'
            + f'<rect x="84" y="-96" width="86" height="192" rx="12" fill="#8a2f2c" {o(6)}/>'
            + "".join(f'<path d="M{-84+j*21},-92 v184" stroke="#e8d9bc" stroke-width="7"'
                      f' opacity=".9"/>' for j in range(9))
            + "".join(f'<circle cx="{-150+j*18}" cy="{-40+j*26}" r="9" fill="#f3e9d2"'
                      f' {o(3)}/>' for j in range(4))
            + '</g>')
    if zast > 0:
        s += SL(Z_PERED, f'<path d="M250,600 h{340*zast:.0f}" stroke="#4a3626"'
                         f' stroke-width="18" stroke-linecap="round"/>')
    if chehol > 0:
        s += SL(Z_PERED, f'<path d="M230,{760-300*chehol:.0f} h390 q20,190 -195,200'
                f' q-215,-10 -195,-200 z" fill="#3b4150" {o(6)} opacity="{chehol:.2f}"/>')
    # коробка с фатой, край фаты шевелится
    sh = 6 * A.w(t, 1.3)
    s += SL(Z_SRED, f'<ellipse cx="1420" cy="700" rx="230" ry="70" fill="#e5d9c6" {o(6)}/>'
            + f'<rect x="1190" y="560" width="460" height="146" fill="#e5d9c6" {o(6)}/>')
    s += SL(Z_PERED, f'<path d="M1540,586 q{70+sh:.0f},40 {110+sh:.0f},130" fill="none"'
                     f' stroke="#fdfaf2" stroke-width="20" opacity=".9"/>')
    kr = A.ease(A.seg(t, 2.4, .9))
    s += SL(Z_PERED, f'<g transform="translate(0,{-280*(1-kr):.0f})">'
            + f'<ellipse cx="1420" cy="556" rx="244" ry="74" fill="#efe4d2" {o(6)}/>'
            + f'<ellipse cx="1420" cy="540" rx="200" ry="56" fill="#f7eeda" opacity=".8"/></g>')
    # пылинки в луче
    s += SL(Z_SRED, luch(900, 0, 520, 900, t, .18))
    for i in range(10):
        ph = (t * .22 + i * .1) % 1.0
        s += SL(Z_PERED, f'<circle cx="{980+i*52-120*ph:.0f}" cy="{200+ph*700:.0f}"'
                         f' r="4" fill="#fff6dc" opacity="{.5*(1-ph):.2f}"/>')
    s += _vinetka(.42)
    return s


def nakrytyy_stol_zhdet(t):
    """Планы 17, 69, 70, 135. Накрытый стол под полотенцем, в окне звезда."""
    s = SL(Z_DAL, kuhnya_stena(t, True, 1240, True))
    # сумерки в окне густеют
    gust = A.seg(t, .2, 2.6)
    s += SL(Z_DAL, f'<rect x="1240" y="180" width="340" height="300" rx="10"'
                   f' fill="#1b2744" opacity="{.25+.45*gust:.2f}"/>')
    # звезда вспыхивает на последних словах
    zv = A.out(A.seg(t, 2.4, .9))
    if zv > 0:
        mer = .75 + .25 * A.w(t, .9)
        s += SL(Z_DAL, f'<circle cx="1390" cy="268" r="{7*zv:.0f}" fill="#fffbe8"'
                       f' opacity="{zv*mer:.2f}"/>'
                + f'<circle cx="1390" cy="268" r="{30*zv:.0f}" fill="url(#teplo)"'
                  f' opacity="{zv*.8:.2f}"/>'
                + f'<path d="M1390,{268-34*zv:.0f} v{68*zv:.0f} M{1390-34*zv:.0f},268'
                  f' h{68*zv:.0f}" stroke="#fff6cf" stroke-width="3"'
                  f' opacity="{zv*.7:.2f}"/>')
    s += SL(Z_SRED, stol_bok(240, 720, 1120, 250, t, "#e7dcc4"))
    # стулья отодвинуты
    for xx, ang in ((190, -8), (1400, 7)):
        s += SL(Z_SRED, f'<g transform="rotate({ang},{xx},900)">'
                + f'<rect x="{xx-60}" y="760" width="120" height="30" rx="8"'
                  f' fill="url(#derev)" {o(6)}/>'
                + f'<rect x="{xx-56}" y="560" width="26" height="206" rx="8"'
                  f' fill="url(#derev)" {o(5)}/>'
                + f'<rect x="{xx+30}" y="560" width="26" height="206" rx="8"'
                  f' fill="url(#derev)" {o(5)}/>'
                + f'<rect x="{xx-56}" y="790" width="22" height="130" rx="7"'
                  f' fill="url(#derev)" {o(5)}/>'
                + f'<rect x="{xx+34}" y="790" width="22" height="130" rx="7"'
                  f' fill="url(#derev)" {o(5)}/></g>')
    # полотенце поверх стола, край шевелится
    kr = 8 * A.w(t, 2.1)
    s += SL(Z_PERED, f'<path d="M300,704 h1000 q-20,90 -500,96 q-480,-6 -500,-96 z"'
                     f' fill="url(#rush)" {o(6)}/>'
            + f'<path d="M300,740 h1000" stroke="{TKAN}" stroke-width="10" opacity=".8"/>'
            + f'<path d="M1296,704 q{20+kr:.0f},70 -40,96" fill="none" stroke="#f3e8cf"'
              f' stroke-width="14" opacity=".95"/>')
    # ложки черенками вверх
    for j in range(3):
        s += SL(Z_PERED, f'<path d="M{520+j*230},700 v-90" stroke="{ZHELEZ}"'
                         f' stroke-width="11" stroke-linecap="round"/>'
                + f'<ellipse cx="{520+j*230}" cy="700" rx="22" ry="30" fill="{ZHELEZ}" {o(4)}/>')
    s += SL(Z_PERED, ramka_pp("levo", "#141008", .26))
    s += _vinetka(.46)
    return s


# ═══════════════ БЛОК 2-3. ЧТО ЭТО ЗА ПОСТ ═══════════════
def shest_snezhnyh_stupeney(t):
    """Планы 18, 19, 25, 55, 56, 63, 65, 131, 156. Смена главы: лестница в снегу."""
    s = SL(Z_NEBO, nebo("rassv", t, True) + oblaka(t, 140, 3, 11, .4, "#dce8f6"))
    s += SL(Z_DAL, f'<rect x="0" y="430" width="{W}" height="{H-430}" fill="url(#sneg)"/>')
    # склон с вырубленными ступенями
    for i in range(6):
        y0 = 980 - i * 118
        x0 = 240 + i * 96
        w_ = 1180 - i * 150
        s += SL(Z_SRED, f'<path d="M{x0},{y0} h{w_} l-40,-74 h-{w_-80} z"'
                        f' fill="#ffffff" {o(6)}/>')
        s += SL(Z_SRED, f'<path d="M{x0+20},{y0-74} h{w_-80}" stroke="{INEY}"'
                        f' stroke-width="9" opacity=".8"/>')
    # дом наверху с дымком
    s += SL(Z_DAL, izba_snaruzhi(1180, 420, 300, t, True, True, 5))
    s += SL(Z_DAL, dym(1296, 300, t, 5, .22, 260, .42))
    # первый след у нижней ступени
    sl = A.out(A.seg(t, 1.6, .7))
    if sl > 0:
        s += SL(Z_PERED, f'<ellipse cx="420" cy="958" rx="{34*sl:.0f}" ry="{17*sl:.0f}"'
                         f' fill="#a9c4da" opacity="{.7*sl:.2f}"/>'
                + f'<ellipse cx="505" cy="944" rx="{30*sl:.0f}" ry="{15*sl:.0f}"'
                  f' fill="#a9c4da" opacity="{.55*sl:.2f}"/>')
    # снег искрит
    for i in range(16):
        ph = (t * .6 + i * .13) % 1.0
        s += SL(Z_PERED, f'<circle cx="{200+i*108}" cy="{900-i*22}" r="{3+3*(1-ph):.0f}"'
                         f' fill="#ffffff" opacity="{.8*(1-abs(ph-.5)*2):.2f}"/>')
    s += SL(Z_LETIT, _sneg_letit(t, 26, 3, .45, .6))
    s += _vinetka(.4)
    return s


def dom_na_prigorke_vecherom(t):
    """Планы 20, 33, 68, 171. Дом в снегу, над крышей загорается звезда."""
    s = SL(Z_NEBO, nebo("sumer", t, True))
    s += SL(Z_NEBO, f'<rect x="0" y="0" width="{W}" height="{H}" fill="url(#nsumer)"'
                    f' opacity=".55"/>')
    s += SL(Z_DAL, f'<path d="M0,760 q560,-230 1920,-90 v410 H0 z" fill="url(#sneg)" {o(0)}/>')
    s += SL(Z_SRED, izba_snaruzhi(700, 760, 520, t, True, True, 9))
    # одно тёплое окно мерцает
    mer = .75 + .25 * A.w(t, 2.3)
    s += SL(Z_SRED, f'<rect x="880" y="580" width="140" height="120" rx="8"'
                    f' fill="{SVET}" opacity="{mer:.2f}" {o(6)}/>'
            + f'<path d="M950,580 v120 M880,640 h140" {o(5)} fill="none"/>'
            + teplo(950, 640, 300, 260, .55))
    s += SL(Z_DAL, dym(840, 460, t, 6, .2, 300, .45))
    # звезда разгорается, на снег ложится голубой свет
    zv = A.ease(A.seg(t, .9, 1.6))
    if zv > 0:
        s += SL(Z_NEBO, f'<circle cx="1180" cy="250" r="{9*zv:.0f}" fill="#ffffff"/>'
                + f'<circle cx="1180" cy="250" r="{76*zv:.0f}" fill="url(#holod)"'
                  f' opacity="{.85*zv:.2f}"/>'
                + "".join(f'<path d="M1180,250 l{dx*70*zv:.0f},{dy*70*zv:.0f}"'
                          f' stroke="#dff0ff" stroke-width="4" opacity="{.7*zv:.2f}"/>'
                          for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))))
        s += SL(Z_SRED, f'<ellipse cx="1180" cy="860" rx="{420*zv:.0f}" ry="{90*zv:.0f}"'
                        f' fill="#9ec8e8" opacity="{.22*zv:.2f}"/>')
    s += SL(Z_LETIT, _sneg_letit(t, 22, 15, .5, .55))
    s += _vinetka(.46)
    return s


def pesochnye_chasy_na_podokonnike(t):
    """План 21. Последние песчинки, стекло в паутинке трещин и пыли."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#3b4453"/>'
            + f'<rect x="760" y="60" width="900" height="640" rx="12"'
              f' fill="url(#nsumer)" {o(9)}/>'
            + f'<path d="M1210,60 v640 M760,380 h900" {o(8)} fill="none"/>')
    s += SL(Z_DAL, _sneg_letit(t, 18, 21, .45, .6))
    s += SL(Z_SRED, kladka(0, 700, W, 380, 70) + f'<rect x="0" y="672" width="{W}"'
            f' height="40" rx="8" fill="url(#kamen)" {o(7)}/>')
    # часы
    s += SL(Z_PERED, ten(620, 690, 190, 26, .55))
    s += SL(Z_PERED, f'<rect x="440" y="648" width="360" height="30" rx="10"'
                     f' fill="url(#derev)" {o(7)}/>'
            + f'<rect x="440" y="150" width="360" height="30" rx="10"'
              f' fill="url(#derev)" {o(7)}/>'
            + f'<path d="M476,180 v34 M764,180 v34 M476,614 v34 M764,614 v34" {o(8)} fill="none"/>')
    s += SL(Z_PERED, f'<path d="M500,214 h240 l-104,180 l104,180 h-240 l104,-180 z"'
                     f' fill="url(#stekl)" opacity=".55" {o(7)}/>')
    # песок почти весь внизу
    ost = max(0.0, 1 - A.seg(t, .2, 2.6))
    s += SL(Z_PERED, f'<path d="M520,232 h200 l-{100*(1-ost*.0):.0f},{70*ost+8:.0f}'
            f' h-{200-140*0:.0f} z" fill="url(#solom)" opacity="{.9*ost+.1:.2f}"/>')
    s += SL(Z_PERED, f'<path d="M524,590 h192 q-96,-{130+40*(1-ost):.0f} -96,-{130+40*(1-ost):.0f}'
            f' q0,0 -96,{130+40*(1-ost):.0f} z" fill="url(#solom)" {o(0)}/>')
    # последние песчинки падают
    for i in range(4):
        ph = (t * 1.3 + i * .25) % 1.0
        if ost <= 0 and ph > .5:
            continue
        s += SL(Z_PERED, f'<circle cx="{618+2*math.sin(i*2.0+t):.0f}"'
                         f' cy="{400+ph*180:.0f}" r="3.5" fill="#e8cf96" opacity=".9"/>')
    # паутинка трещин и пыль
    tr = A.seg(t, 2.1, 1.3)
    if tr > 0:
        for i in range(7):
            a = i * 52
            s += SL(Z_PERED, f'<path d="M620,400 l{(a%97-48)*tr*2.4:.0f},{(a%61-30)*tr*2.6:.0f}'
                             f' l{(a%37-18)*tr*2:.0f},{(a%53-26)*tr*1.6:.0f}" fill="none"'
                             f' stroke="#ffffff" stroke-width="2.4" opacity="{.5*tr:.2f}"/>')
        s += SL(Z_PERED, f'<path d="M500,214 h240 l-104,180 l104,180 h-240 l104,-180 z"'
                         f' fill="#cfc6ae" opacity="{.18*tr:.2f}"/>')
    for i in range(8):
        ph = (t * .18 + i * .12) % 1.0
        s += SL(Z_PERED, f'<circle cx="{420+i*64}" cy="{250+ph*420:.0f}" r="3"'
                         f' fill="#e6ddc8" opacity="{.4*(1-ph):.2f}"/>')
    s += _vinetka(.5)
    return s


def dorozhka_iz_zeren(t):
    """Планы 22-23. Семь зёрен ложатся в ряд на тёмную столешницу."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#241c15"/>'
            + doski(0, 0, W, H, 170, False, "derev")
            + f'<rect x="0" y="0" width="{W}" height="{H}" fill="#000000" opacity=".28"/>')
    # светильник слева, пламя колышется
    s += SL(Z_SRED, svecha(200, 700, t, .0, 1.5, 120))
    s += SL(Z_SRED, teplo(210, 640, 560, 460, .5))
    # тень руки идёт над столом
    hod = A.seg(t, .2, 3.4)
    s += SL(Z_PERED, f'<ellipse cx="{430+hod*900:.0f}" cy="520" rx="210" ry="80"'
                     f' fill="#000000" opacity=".22"/>')
    # семь зёрен ложатся по одному
    for i in range(7):
        k = A.over(A.seg(t, .35 + i * .42, .3))
        if k <= 0:
            continue
        kk = min(1.0, k)
        xx = 430 + i * 165
        s += SL(Z_PERED, f'<g opacity="{kk:.2f}" transform="translate(0,{-30*(1-kk):.0f})">'
                + ten(xx, 702, 34, 10, .5)
                + f'<ellipse cx="{xx}" cy="690" rx="34" ry="19" fill="url(#solom)" {o(5)}'
                  f' transform="rotate(-12,{xx},690)"/>'
                + f'<path d="M{xx-22},684 q22,-12 44,2" fill="none" stroke="#8a6a2c"'
                  f' stroke-width="4"/>'
                + f'<ellipse cx="{xx-10}" cy="682" rx="9" ry="4" fill="#fff4d6" opacity=".6"/>'
                + '</g>')
    s += SL(Z_PERED, ramka_pp("oba", "#0b0806", .40))
    s += _vinetka(.52)
    return s


def pridorozhnyy_stolb_s_doschechkoy(t):
    """План 24. Дощечка на столбе поворачивается на гвозде."""
    s = SL(Z_NEBO, nebo("den", t, False) + oblaka(t, 180, 4, 17, .45))
    s += SL(Z_DAL, _ulica_dal(0, 600, W, t, True, 12))
    s += SL(Z_DAL, f'<path d="M0,700 q960,-80 1920,40 v340 H0 z" fill="url(#sneg)"/>')
    # дорога двумя колеями
    s += SL(Z_SRED, f'<path d="M560,{H} q120,-340 420,-430" fill="none" stroke="{INEY}"'
                    f' stroke-width="46" opacity=".8"/>'
            + f'<path d="M900,{H} q60,-340 160,-430" fill="none" stroke="{INEY}"'
              f' stroke-width="46" opacity=".8"/>')
    # столб
    s += SL(Z_PERED, ten(1280, 1010, 90, 22, .5)
            + f'<rect x="1246" y="300" width="68" height="716" rx="10"'
              f' fill="url(#derev)" {o(7)}/>'
            + f'<path d="M1246,300 q34,-26 68,0 z" fill="{DOSKA2}" {o(5)}/>')
    # снег сыплется со столба
    for i in range(5):
        ph = (t * .5 + i * .2) % 1.0
        s += SL(Z_PERED, f'<circle cx="{1240+i*20}" cy="{330+ph*640:.0f}" r="{5-2*ph:.0f}"'
                         f' fill="#ffffff" opacity="{.7*(1-ph):.2f}"/>')
    # дощечка поворачивается на гвозде
    pov = A.ease(A.seg(t, 1.5, 1.2))
    sx = math.cos(math.pi * pov)
    s += SL(Z_PERED, f'<g transform="translate(1280,430) scale({sx:.3f},1)">'
            + f'<rect x="-230" y="-66" width="460" height="132" rx="12"'
              f' fill="url(#dosk)" {o(7)}/>'
            + f'<path d="M-186,10 h372" stroke="#5e4226" stroke-width="7" opacity=".5"/>'
            + '</g>'
            + f'<circle cx="1280" cy="430" r="9" fill="{ZHELEZ}" {o(4)}/>')
    # синица садится на столб
    pos = A.ease(A.seg(t, 2.6, .8))
    s += SL(Z_PERED, f'<g transform="translate({-240*(1-pos):.0f},{-160*(1-pos):.0f})"'
            f' opacity="{pos:.2f}">' + ptica(1280, 290, t, 1.2, "#f2d64a", .0, "#4a6b86") + '</g>')
    s += SL(Z_LETIT, _sneg_letit(t, 20, 19, .45, .6))
    s += _vinetka(.42)
    return s


def stol_zagovenya(t):
    """Планы 26-27. Стол ломится: пирог, яичница, сметана, сыр, молоко."""
    s = SL(Z_DAL, kuhnya_stena(t, True, 1520))
    s += SL(Z_SRED, stol_bok(40, 700, 1240, 300, t, "#d9c7a4"))
    s += SL(Z_SRED, teplo(640, 600, 900, 520, .5))
    # мясной пирог крупно
    s += SL(Z_PERED, ten(300, 700, 210, 30, .5)
            + f'<path d="M110,690 q10,-150 190,-150 q180,0 190,150 z"'
              f' fill="url(#solom)" {o(8)}/>'
            + f'<path d="M160,600 q140,-40 280,0" fill="none" stroke="#c08a3e"'
              f' stroke-width="12"/>'
            + "".join(f'<path d="M{190+j*60},660 l34,-40" stroke="#b47a36"'
                      f' stroke-width="8"/>' for j in range(4)))
    s += SL(Z_PERED, par(300, 520, t, 7, .55, 260, .4, 1.5))
    # яичница шкворчит
    shk = 5 * A.w(t, .35)
    s += SL(Z_PERED, f'<g transform="translate({shk:.1f},0)">'
            + f'<ellipse cx="700" cy="690" rx="210" ry="62" fill="url(#chug)" {o(8)}/>'
            + "".join(f'<ellipse cx="{620+j*84}" cy="676" rx="64" ry="34" fill="#fbf4e2"'
                      f' {o(5)}/><circle cx="{620+j*84}" cy="672" r="24" fill="#f0b43c"/>'
                      for j in range(2))
            + f'<path d="M910,672 h210" {o(14)} fill="none"/></g>')
    for i in range(5):
        ph = (t * 1.6 + i * .2) % 1.0
        s += SL(Z_PERED, f'<circle cx="{640+i*52}" cy="{640-54*ph:.0f}" r="{4+4*ph:.0f}"'
                         f' fill="#ffe9b8" opacity="{.6*(1-ph):.2f}"/>')
    # сметана блестит
    bl = .5 + .5 * A.w(t, 2.0)
    s += SL(Z_PERED, tarelka(1080, 690, 104, t, "url(#krem)", True)
            + f'<ellipse cx="1080" cy="668" rx="74" ry="28" fill="#fbfaf4" {o(5)}/>'
            + f'<ellipse cx="1052" cy="660" rx="26" ry="11" fill="#ffffff"'
              f' opacity="{.4+.4*bl:.2f}"/>')
    # сыр и кувшин молока
    s += SL(Z_PERED, f'<path d="M1300,694 l170,-86 l76,58 l-170,86 z" fill="url(#solom)" {o(7)}/>'
            + "".join(f'<circle cx="{1352+j*46}" cy="{658-j*16}" r="13"'
                      f' fill="#e2c87e"/>' for j in range(3)))
    s += SL(Z_PERED, krynka(1620, 700, 2.1, "url(#krem)"))
    s += SL(Z_PERED, ramka_pp("levo", "#1a1309", .22))
    s += _vinetka(.42)
    return s


def chistaya_skovoroda_na_stene(t):
    """План 28. Вымытая сковорода на стене, кот нюхает пустую доску и уходит."""
    s = SL(Z_DAL, kuhnya_stena(t, False, 1420))
    s += SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#cfd8dd" opacity=".25"/>')
    # сковорода на гвозде
    s += SL(Z_SRED, f'<circle cx="640" cy="420" r="160" fill="url(#chug)" {o(8)}/>'
            + f'<circle cx="640" cy="420" r="126" fill="#3c3836"/>'
            + f'<ellipse cx="600" cy="376" rx="52" ry="22" fill="#ffffff" opacity=".22"/>'
            + f'<path d="M790,400 q110,-10 150,34" fill="none" {o(16)}/>'
            + f'<circle cx="640" cy="248" r="10" fill="{ZHELEZ}" {o(4)}/>')
    # капля падает со сковороды
    ph = (t * .55) % 1.0
    s += SL(Z_PERED, f'<ellipse cx="640" cy="{588+ph*280:.0f}" rx="{7-2*ph:.0f}"'
                     f' ry="{11-2*ph:.0f}" fill="#cfe3ef" opacity="{.85*(1-ph*.5):.2f}"/>')
    if ph > .92:
        s += SL(Z_PERED, f'<ellipse cx="640" cy="876" rx="{40*(ph-.92)*12:.0f}" ry="7"'
                         f' fill="none" stroke="#cfe3ef" stroke-width="3" opacity=".6"/>')
    # чистая доска под сковородой
    s += SL(Z_SRED, stol_bok(380, 860, 740, 200, t))
    s += SL(Z_PERED, f'<rect x="520" y="820" width="330" height="36" rx="10"'
                     f' fill="url(#dosk)" {o(6)}/>'
            + f'<circle cx="840" cy="838" r="11" fill="none" {o(5)}/>')
    # кот нюхает и уходит
    uh = A.ease(A.seg(t, 2.2, 1.6))
    nos = 6 * A.w(t, .9) * (1 - uh)
    s += SL(Z_PERED, f'<g transform="translate({-420*uh+nos:.0f},0)" opacity="{1-uh*.2:.2f}">'
            + kot(980, 1010, t, 1.1) + '</g>')
    s += _vinetka(.44)
    return s


def holodilnik_nakanune_posta(t):
    """План 29. Хозяйка со спины забирает с полки сыр, яйца и котлету."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#8e9aa0"/>'
            + _panelka(1400, 420, 460, t, 4, True, 7)
            + f'<rect x="0" y="760" width="{W}" height="320" fill="#6f5f4c"/>'
            + polovicy(760, "#6f5f4c"))
    # холодильник, свет из него
    s += SL(Z_SRED, f'<rect x="240" y="90" width="820" height="960" rx="22"'
                    f' fill="#e2e6e8" {o(8)}/>'
            + f'<rect x="286" y="140" width="740" height="860" rx="14" fill="#1d2326"/>'
            + f'<rect x="300" y="160" width="712" height="300" rx="10" fill="#cfdde4"'
              f' opacity=".9"/>')
    s += SL(Z_SRED, teplo(660, 330, 520, 420, .6))
    # полка: сыр, три яйца, котлета на блюдце
    ber = A.ease(A.seg(t, 1.6, 1.2))
    s += SL(Z_PERED, f'<g opacity="{1-ber:.2f}">'
            + f'<path d="M360,420 l120,-56 l44,36 l-120,56 z" fill="url(#solom)" {o(5)}/>'
            + "".join(f'<ellipse cx="{600+j*54}" cy="400" rx="22" ry="29" fill="#f3ead6"'
                      f' {o(4)}/>' for j in range(3))
            + f'<ellipse cx="880" cy="412" rx="66" ry="22" fill="url(#krem)" {o(5)}/>'
            + f'<ellipse cx="880" cy="398" rx="42" ry="20" fill="#9d5f3a" {o(4)}/></g>')
    # рука со спины забирает всё разом
    s += SL(Z_PERED, f'<g transform="translate({-200*ber:.0f},{-60*ber:.0f})">'
            + f'<path d="M1180,560 q-180,-90 -300,-140" fill="none" stroke="#e8bb93"'
              f' stroke-width="56" stroke-linecap="round" opacity="{min(1,.2+ber):.2f}"/></g>')
    # хозяйка со спины
    s += SL(Z_PERED, spina(1420, 1040, 780, t, "#39323c", "#6b5a7a", .2))
    # тапочек постукивает
    tap = 7 * abs(A.w(t, .8))
    s += SL(Z_PERED, f'<ellipse cx="1500" cy="{1046-tap:.0f}" rx="56" ry="18"'
                     f' fill="#7a4a52" {o(5)}/>')
    s += SL(Z_PERED, ramka_pp("pravo", "#141214", .3))
    s += _vinetka(.46)
    return s


def stol_knizhka_v_komnate(t):
    """План 30. Стол-книжка раскладывается, подъезжают табуретки, входят гости."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#c6b79c"/>'
            + f'<rect x="0" y="0" width="{W}" height="{H}" fill="url(#teplo)" opacity=".3"/>'
            + f'<rect x="0" y="780" width="{W}" height="300" fill="url(#pol)"/>'
            + polovicy(780))
    # ковёр на стене — примета комнаты тех лет
    s += SL(Z_DAL, f'<rect x="120" y="180" width="700" height="460" rx="10"'
                   f' fill="#7a3a34" {o(7)}/>'
            + "".join(f'<rect x="{190+j*160}" y="250" width="110" height="320" rx="40"'
                      f' fill="none" stroke="#e2c08a" stroke-width="8" opacity=".8"/>'
                      for j in range(4)))
    # дверной проём, в нём гости-силуэты
    s += SL(Z_DAL, f'<rect x="1540" y="200" width="300" height="640" rx="8"'
                   f' fill="#2b2420" {o(8)}/>')
    gost = A.ease(A.seg(t, 2.0, 1.4))
    s += SL(Z_SRED, f'<g opacity="{gost:.2f}">'
            + spina(1640, 840, 420, t, "#3a3040", "#8a3f3a", .2)
            + spina(1770, 840, 400, t, "#2f3845", None, .5) + '</g>')
    # стол-книжка: крылья раскрываются
    kr = A.ease(A.seg(t, .2, 1.1))
    s += SL(Z_SRED, stol_bok(700, 760, 420, 230, t))
    for sgn, x0 in ((-1, 700), (1, 1120)):
        ang = 90 * (1 - kr) * -sgn
        s += SL(Z_SRED, f'<g transform="rotate({ang:.0f},{x0},762)">'
                + f'<rect x="{x0 if sgn>0 else x0-300}" y="760" width="300" height="26"'
                  f' rx="7" fill="url(#dosk)" {o(6)}/></g>')
    # табуретки подъезжают
    for i, (x0, d) in enumerate(((430, -260), (1480, 240))):
        k = A.ease(A.seg(t, .9 + i * .3, .9))
        s += SL(Z_PERED, f'<g transform="translate({d*(1-k):.0f},0)">'
                + f'<rect x="{x0-70}" y="880" width="140" height="26" rx="7"'
                  f' fill="url(#derev)" {o(6)}/>'
                + f'<rect x="{x0-60}" y="906" width="20" height="130" rx="6"'
                  f' fill="url(#derev)" {o(5)}/>'
                + f'<rect x="{x0+40}" y="906" width="20" height="130" rx="6"'
                  f' fill="url(#derev)" {o(5)}/></g>')
    # омлет, сырники, котлеты
    if kr > .8:
        s += SL(Z_PERED, tarelka(830, 752, 66, t, "url(#krem)", False, 2)
                + f'<ellipse cx="830" cy="740" rx="48" ry="20" fill="#f6d88a" {o(4)}/>')
        s += SL(Z_PERED, tarelka(1010, 754, 62, t)
                + "".join(f'<ellipse cx="{986+j*26}" cy="742" rx="22" ry="12"'
                          f' fill="#e8c88e" {o(4)}/>' for j in range(2)))
        s += SL(Z_PERED, par(1010, 700, t, 4, .5, 170, .45, .9))
    s += _vinetka(.44)
    return s


def dve_snezhnye_lesenki_ryadom(t):
    """Планы 31, 32, 145. Два снежных склона рядом, подсвечен левый."""
    s = SL(Z_NEBO, nebo("sumer", t, True) + oblaka(t, 150, 3, 23, .35))
    s += SL(Z_DAL, f'<rect x="0" y="420" width="{W}" height="{H-420}" fill="#dde8f4"/>')
    for storona, x0 in ((0, 60), (1, 1000)):
        podsv = storona == 0
        for i in range(5):
            y0 = 980 - i * 110
            xx = x0 + i * 52
            w_ = 760 - i * 104
            col = "#ffffff" if podsv else "#dbe6f0"
            s += SL(Z_SRED, f'<path d="M{xx},{y0} h{w_} l-34,-68 h-{w_-68} z"'
                            f' fill="{col}" {o(6)}/>')
        if podsv:
            mer = .22 + .1 * A.w(t, 2.6)
            s += SL(Z_SRED, f'<path d="M{x0-20},1000 l260,-560 h560 l-260,560 z"'
                            f' fill="#ffe9a8" opacity="{mer:.2f}"/>')
    # столбики с числами встают из снега
    for i, (xx, yy, t0) in enumerate(((150, 960, .5), (560, 480, 1.3))):
        k = A.out(A.seg(t, t0, .7))
        if k <= 0:
            continue
        s += SL(Z_PERED, f'<g opacity="{k:.2f}" transform="translate(0,{70*(1-k):.0f})">'
                + f'<rect x="{xx-14}" y="{yy-170}" width="28" height="170" rx="8"'
                  f' fill="url(#derev)" {o(6)}/>'
                + f'<rect x="{xx-96}" y="{yy-250}" width="192" height="92" rx="10"'
                  f' fill="url(#rush)" {o(6)}/></g>')
    s += SL(Z_LETIT, _sneg_letit(t, 34, 29, .55, .8))
    s += _vinetka(.42)
    return s


# ═══════════════ БЛОК 4. СТОЛ ПО ДНЯМ НЕДЕЛИ ═══════════════
def kuhonnaya_etazherka_v_chetyre_polk(t):
    """Планы 34, 38, 42, 43, 47, 49, 53, 66, 152. Этажерка-ступени с бирками дней."""
    s = SL(Z_DAL, kuhnya_stena(t, True, 1430, False, True, 17))
    # этажерка уступами, как ступени
    for i in range(4):
        x0 = 200 + i * 36
        w_ = 860 - i * 56
        y0 = 930 - i * 175
        s += SL(Z_SRED, f'<path d="M{x0},{y0} h{w_} l-46,-66 h-{w_-92} z"'
                        f' fill="#ba8c5c" {o(7)}/>'
                + f'<rect x="{x0}" y="{y0}" width="{w_}" height="34" rx="8"'
                  f' fill="url(#dosk)" {o(7)}/>'
                + f'<rect x="{x0+6}" y="{y0-10}" width="{w_-12}" height="14" rx="5"'
                  f' fill="{DOSKA2}" opacity=".85"/>')
    s += SL(Z_SRED, f'<rect x="150" y="400" width="34" height="552" rx="10"'
                    f' fill="url(#derev)" {o(7)}/>'
            + f'<rect x="980" y="570" width="34" height="382" rx="10"'
              f' fill="url(#derev)" {o(7)}/>')
    # семь бирок на нитках покачиваются
    dni = ("Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс")
    for i, d in enumerate(dni):
        k = A.out(A.seg(t, .6 + i * .22, .35))
        if k <= 0:
            continue
        ang = 5 * A.w(t, 2.2, i * .15)
        xx, yy = 128, 300 + i * 100
        s += SL(Z_PERED, f'<g opacity="{k:.2f}" transform="rotate({ang:.1f},{xx},{yy-26})">'
                + f'<path d="M{xx},{yy-26} v24" {o(3)} fill="none"/>'
                + f'<rect x="{xx-62}" y="{yy}" width="124" height="60" rx="10"'
                  f' fill="url(#rush)" {o(5)}/>'
                + f'<text x="{xx}" y="{yy+44}" font-family="Georgia,serif" font-size="38"'
                  f' text-anchor="middle" fill="#3a2a16">{d}</text></g>')
    # луч солнца ползёт по полкам
    hod = A.seg(t, 0, 5.0)
    s += SL(Z_PERED, f'<g transform="translate({-200+hod*500:.0f},0)">'
            + luch(760, 140, 420, 860, t, .20) + '</g>')
    s += _vinetka(.42)
    return s


def tolstaya_kniga_s_zastezhkami(t):
    """План 35. Старая книга с медными застёжками на каменном подоконнике."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#49525e"/>'
            + kladka(0, 0, W, H, 92, "url(#kamen)")
            + f'<rect x="1020" y="80" width="760" height="540" rx="14"'
              f' fill="url(#nden)" {o(10)}/>')
    # за окном высокая стена и снег
    s += SL(Z_DAL, f'<rect x="1040" y="100" width="720" height="500" fill="#6d6459" opacity=".92"/>'
            + kladka(1040, 100, 720, 500, 58, "#7d7265")
            + sneg_letit(t, 20, 23, .5, .7)
            + f'<path d="M1400,80 v540 M1020,350 h760" {o(9)} fill="none"/>')
    s += SL(Z_SRED, f'<path d="M0,640 h{W} l0,120 h-{W} z" fill="#8c8275" {o(8)}/>'
            + f'<path d="M0,640 q960,-40 {W},0" fill="none" stroke="#9c9285"'
              f' stroke-width="12"/>'
            + f'<rect x="0" y="752" width="{W}" height="36" rx="8"'
              f' fill="url(#kamen)" {o(7)}/>')
    # книга крупно
    naklon = 1.2 * A.w(t, 4.0)
    s += SL(Z_PERED, f'<g transform="rotate({naklon:.1f},540,620)">'
            + ten(540, 630, 330, 34, .55)
            + f'<path d="M210,620 l70,-420 h520 l70,420 z" fill="#5e2f28" {o(9)}/>'
            + f'<path d="M240,604 l62,-390 h480 l62,390 z" fill="#7a3d33" {o(5)}/>'
            + f'<path d="M302,214 h480 l20,330 h-520 z" fill="#efe7cf" opacity=".92" {o(5)}/>'
            + "".join(f'<path d="M{306+j*4},{222+j*2} h{470-j*2}" stroke="#d6cbb0"'
                      f' stroke-width="3" opacity=".8"/>' for j in range(6))
            + f'<path d="M330,300 h420 M336,350 h400 M344,400 h380 M350,450 h360"'
              f' stroke="#c3b89a" stroke-width="9" opacity=".75"/>'
            + f'<path d="M280,214 l-40,390" stroke="#4a241f" stroke-width="12"/>'
            + '</g>')
    # застёжки щёлкают
    for i, (yy, t0) in enumerate(((430, .8), (530, 1.6))):
        shch = A.out(A.seg(t, t0, .25))
        s += SL(Z_PERED, f'<g transform="translate({26*(1-shch):.0f},0)">'
                + f'<rect x="196" y="{yy}" width="130" height="34" rx="10"'
                  f' fill="url(#zol)" {o(5)}/>'
                + f'<circle cx="300" cy="{yy+17}" r="13" fill="{MED}" {o(4)}/></g>')
    # пыль взлетает
    for i in range(9):
        ph = (t * .4 + i * .11) % 1.0
        s += SL(Z_PERED, f'<circle cx="{320+i*52}" cy="{330-ph*220:.0f}" r="{4+3*ph:.0f}"'
                         f' fill="#e6ddc8" opacity="{.45*(1-ph):.2f}"/>')
    s += _vinetka(.5)
    return s


def babushka_s_chugunkom_u_pechki(t):
    """Планы 36-37. Бабушка ухватом ставит чугунок в печь, книга на полке."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="{POBEL}"/>'
            + f'<rect x="0" y="{H-260}" width="{W}" height="260" fill="url(#pol)"/>'
            + polovicy(H - 260))
    # русская печь справа
    s += SL(Z_SRED, pech_russkaya(1120, 250, 760, 790, t, True, .0))
    s += SL(Z_SRED, teplo(1330, 760, 620, 420, .6))
    # книга под рушником на полке слева
    s += SL(Z_DAL, f'<rect x="60" y="430" width="420" height="26" rx="7"'
                   f' fill="url(#dosk)" {o(6)}/>'
            + f'<path d="M150,430 l20,-90 h150 l20,90 z" fill="#5e2f28" {o(6)}/>'
            + f'<path d="M110,352 h300 q-10,120 -150,128 q-140,-8 -150,-128 z"'
              f' fill="url(#rush)" {o(5)}/>'
            + f'<path d="M120,420 h280" stroke="{TKAN}" stroke-width="8" opacity=".8"/>')
    s += SL(Z_DAL, hodiki(640, 300, t, 1.5))
    # бабушка с ухватом в профиль
    s += SL(Z_PERED, babka(700, 1020, 700, t, True, TKAN, .0, -22))
    # ухват и чугунок едут в печь
    hod = A.ease(A.seg(t, .6, 2.2))
    ux = 880 + hod * 340
    s += SL(Z_PERED, f'<path d="M{ux-300:.0f},620 L{ux:.0f},700" {o(18)} fill="none"/>'
            + f'<path d="M{ux:.0f},700 q30,-50 64,0" fill="none" {o(14)}/>')
    s += SL(Z_PERED, gorshok(ux + 30, 760, 1.4, t, "url(#chug)", False))
    s += SL(Z_PERED, par(ux + 30, 640, t, 6, .55, 240, .4, 1.3))
    # отсвет печи на фартуке
    s += SL(Z_PERED, f'<ellipse cx="760" cy="800" rx="120" ry="180" fill="{ORA}"'
                     f' opacity="{.12+.05*A.w(t,1.6):.2f}"/>')
    s += _vinetka(.46)
    return s


def sumka_s_pokupkami_na_taburetke(t):
    """План 39. Хозяйственная сумка с покупками, над ней лупа."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#d8d2c4"/>'
            + f'<rect x="0" y="{H-300}" width="{W}" height="300" fill="#9a8468"/>'
            + f'<rect x="0" y="300" width="{W}" height="60" fill="#c0b7a4" opacity=".6"/>'
            + _kvartira_veschi(1420, 1020, 460, t, 5))
    # плита с чайником справа
    s += SL(Z_SRED, f'<rect x="1180" y="620" width="420" height="200" rx="12"'
                    f' fill="url(#zhel)" {o(7)}/>'
            + f'<path d="M1300,620 q-16,-120 110,-120 q126,0 110,120 z" fill="url(#zhel)" {o(6)}/>'
            + f'<path d="M1500,540 q50,-20 40,40" fill="none" {o(10)}/>'
            + f'<path d="M1370,500 q40,-30 80,0" fill="none" {o(8)}/>')
    s += SL(Z_SRED, par(1420, 470, t, 6, .5, 240, .4, 1.1))
    # табуретка и сумка
    s += SL(Z_SRED, f'<rect x="250" y="820" width="340" height="34" rx="9"'
                    f' fill="url(#derev)" {o(7)}/>'
            + f'<rect x="276" y="854" width="30" height="190" rx="8" fill="url(#derev)" {o(6)}/>'
            + f'<rect x="534" y="854" width="30" height="190" rx="8" fill="url(#derev)" {o(6)}/>')
    s += SL(Z_PERED, f'<path d="M250,820 q-24,-290 170,-290 q194,0 170,290 z"'
                     f' fill="#7a5a3e" {o(8)}/>'
            + f'<path d="M300,530 q120,-140 240,0" fill="none" {o(16)}/>')
    # пачки и свёртки, один сползает
    spolz = A.ease(A.seg(t, 1.4, 1.4))
    s += SL(Z_PERED, f'<rect x="300" y="430" width="110" height="150" rx="10"'
                     f' fill="#cfd8c6" {o(6)}/>'
            + f'<rect x="420" y="460" width="130" height="120" rx="10" fill="#e4d6b8" {o(6)}/>'
            + f'<g transform="translate({30*spolz:.0f},{90*spolz:.0f}) rotate({14*spolz:.1f},500,470)">'
            + f'<rect x="470" y="400" width="120" height="110" rx="10" fill="#d8bfa0" {o(6)}/></g>')
    # лупа покачивается над сумкой
    ang = 6 * A.w(t, 2.4)
    s += SL(Z_PERED, f'<g transform="rotate({ang:.1f},700,200)">'
            + f'<path d="M700,200 v170" {o(6)} fill="none"/>'
            + f'<circle cx="700" cy="470" r="104" fill="url(#stekl)" opacity=".65" {o(10)}/>'
            + f'<path d="M700,574 v120" {o(16)} fill="none"/></g>')
    s += _vinetka(.44)
    return s


def chetyre_zabytye_melochi(t):
    """План 40. Кофе с молоком, бутерброд, салат, булка — и значки над ними."""
    s = SL(Z_DAL, kuhnya_stena(t, True, 1460, False, True, 23))
    s += SL(Z_SRED, stol_bok(40, 700, 1320, 300, t, "#cfd8c6"))
    veshi = [
        (260, lambda: f'<path d="M150,686 q-10,-160 140,-160 q150,0 140,160 z"'
                      f' fill="#f2eee4" {o(7)}/>'
                      f'<ellipse cx="290" cy="530" rx="140" ry="40" fill="#6b4a32" {o(6)}/>'
                      + "".join(f'<path d="M{250+j*18},546 q22,-16 44,4" fill="none"'
                                f' stroke="#efe6d6" stroke-width="7" opacity=".9"'
                                f' transform="rotate({t*40+j*120:.0f},290,546)"/>'
                                for j in range(3))
                      + f'<path d="M430,580 q76,14 50,88" fill="none" {o(16)}/>'),
        (640, lambda: f'<rect x="500" y="610" width="280" height="60" rx="10"'
                      f' fill="url(#solom)" {o(7)}/>'
                      f'<rect x="520" y="560" width="240" height="54" rx="8"'
                      f' fill="#f0c860" {o(6)}/>'
                      + "".join(f'<circle cx="{560+j*68}" cy="586" r="13"'
                                f' fill="#d8ac46"/>' for j in range(3))),
        (1000, lambda: f'<path d="M860,686 q-14,-130 140,-130 q154,0 140,130 z"'
                       f' fill="url(#krem)" {o(7)}/>'
                       f'<ellipse cx="1000" cy="556" rx="140" ry="34" fill="#fbfaf4" {o(5)}/>'
                       + "".join(f'<ellipse cx="{930+j*62}" cy="548" rx="30" ry="16"'
                                 f' fill="{ZEL2}" opacity=".9"/>' for j in range(3))),
        (1300, lambda: f'<path d="M1180,686 q0,-160 120,-160 q120,0 120,160 z"'
                       f' fill="#d49a52" {o(7)}/>'
                       f'<path d="M1222,572 q78,-34 156,0" fill="none" stroke="#b47a36"'
                       f' stroke-width="11"/>'),
    ]
    for i, (xx, f) in enumerate(veshi):
        k = A.over(A.seg(t, .4 + i * .9, .4))
        if k <= 0:
            continue
        kk = min(1.0, k)
        s += SL(Z_PERED, f'<g opacity="{kk:.2f}" transform="translate(0,{-50*(1-kk):.0f})">'
                + f() + '</g>')
        # значок: крынка или яйцо всплывает над предметом
        kz = A.out(A.seg(t, .9 + i * .9, .6))
        if kz > 0:
            yy = 480 - 90 * kz
            s += SL(Z_PERED, f'<g opacity="{kz*.95:.2f}">'
                    + f'<circle cx="{xx}" cy="{yy}" r="54" fill="#1e1a16" opacity=".55"/>'
                    + (krynka(xx, yy + 26, .55) if i % 2 == 0 else
                       f'<ellipse cx="{xx}" cy="{yy}" rx="22" ry="29" fill="#f6eddc" {o(4)}/>')
                    + '</g>')
    s += SL(Z_PERED, par(1280, 540, t, 5, .5, 200, .45, 1.0))
    s += _vinetka(.42)
    return s


def plitka_v_folge_i_ochki(t):
    """План 41. Плитка в фольге уходит на полку, очки и мелкий состав."""
    s = SL(Z_DAL, kuhnya_stena(t, True, None, False, True, 29))
    s += SL(Z_SRED, f'<rect x="60" y="330" width="760" height="30" rx="8"'
                    f' fill="url(#dosk)" {o(7)}/>')
    # плитка в фольге едет на верхнюю полку
    k = A.ease(A.seg(t, .3, 1.3))
    py = 760 - 400 * k
    bl = .5 + .5 * A.w(t, 1.7)
    s += SL(Z_PERED, f'<g transform="translate(0,{py-760:.0f})">'
            + ruka(60, 880, t, 230, -16, 48, "#7a6a52")
            + f'<rect x="300" y="700" width="300" height="120" rx="10"'
              f' fill="#b9bcc2" {o(6)}/>'
            + f'<rect x="300" y="700" width="300" height="34" rx="8"'
              f' fill="#e6e9ee" opacity="{.4+.4*bl:.2f}"/>'
            + "".join(f'<path d="M{330+j*54},700 v120" stroke="#8d939c"'
                      f' stroke-width="5" opacity=".7"/>' for j in range(5))
            + '</g>')
    # очки надеваются
    och = A.out(A.seg(t, 1.8, .7))
    if och > 0:
        s += SL(Z_PERED, f'<g opacity="{och:.2f}" transform="translate(0,{-60*(1-och):.0f})">'
                + f'<circle cx="330" cy="520" r="62" fill="url(#stekl)" opacity=".5" {o(8)}/>'
                + f'<circle cx="500" cy="520" r="62" fill="url(#stekl)" opacity=".5" {o(8)}/>'
                + f'<path d="M392,520 h46" {o(8)} fill="none"/>'
                + f'<path d="M268,520 q-50,-20 -70,20 M562,520 q50,-20 70,20" {o(7)} fill="none"/>'
                + '</g>')
    # пачка печенья поворачивается оборотом, строчки состава растут
    pov = A.ease(A.seg(t, 2.6, 1.2))
    sx = math.cos(math.pi * pov)
    s += SL(Z_PERED, f'<g transform="translate(420,840) scale({abs(sx):.3f},1)">'
            + f'<rect x="-170" y="-130" width="340" height="260" rx="14"'
              f' fill="{"#d8c9a8" if sx > 0 else "#efe9da"}" {o(7)}/>'
            + ('' if sx > 0 else "".join(
                f'<rect x="-130" y="{-90+j*34}" width="{150+j*20}" height="{8+10*pov:.0f}"'
                f' rx="4" fill="#6b6354" opacity=".85"/>' for j in range(5)))
            + '</g>')
    s += _vinetka(.42)
    return s


def holodnaya_trapeza(t):
    """План 44. Каменный стол у холодной печи: хлеб, орехи, сушёные яблоки."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#5b5e63"/>'
            + kladka(0, 0, W, 640, 86, "url(#kamen)")
            + f'<rect x="0" y="640" width="{W}" height="440" fill="#4e4a44"/>')
    # холодная печь: тёмное устье, золы нет
    s += SL(Z_SRED, pech_russkaya(1140, 230, 720, 740, t, False, .0))
    s += SL(Z_SRED, svody(t, "#4b443b", 3))
    # каменный стол
    s += SL(Z_SRED, f'<rect x="60" y="700" width="980" height="46" rx="10"'
                    f' fill="url(#kamen)" {o(8)}/>'
            + f'<rect x="150" y="746" width="80" height="300" fill="url(#kamen)" {o(7)}/>'
            + f'<rect x="860" y="746" width="80" height="300" fill="url(#kamen)" {o(7)}/>')
    # бутыль масла: пробку вдавливают и отставляют
    vd = A.ease(A.seg(t, .4, .8))
    ots = A.ease(A.seg(t, 1.4, 1.0))
    s += SL(Z_PERED, f'<g transform="translate({160*ots:.0f},0)">'
            + f'<path d="M250,700 q-10,-180 60,-200 l0,-70 h40 l0,70 q70,20 60,200 z"'
              f' fill="#3f5a3a" opacity=".92" {o(7)}/>'
            + f'<rect x="306" y="{404-18*vd:.0f}" width="36" height="44" rx="6"'
              f' fill="url(#solom)" {o(5)}/></g>')
    # миска с хлебом, орехами, яблоками
    s += SL(Z_PERED, f'<path d="M560,700 q-20,-130 180,-130 q200,0 180,130 z"'
                     f' fill="url(#glina)" {o(7)}/>'
            + f'<ellipse cx="740" cy="574" rx="180" ry="40" fill="#b07a46" {o(5)}/>'
            + f'<path d="M640,566 q60,-70 150,-30 q50,24 10,46 z" fill="#8a5a2c" {o(5)}/>'
            + "".join(f'<circle cx="{700+j*54}" cy="560" r="24" fill="#a07b4e" {o(4)}/>'
                      for j in range(3))
            + "".join(f'<ellipse cx="{660+j*46}" cy="542" rx="22" ry="12"'
                      f' fill="#c9975a" {o(3)}/>' for j in range(2)))
    # орех катится по столу
    kat = A.seg(t, 2.2, 1.8)
    s += SL(Z_PERED, f'<circle cx="{560+kat*420:.0f}" cy="684" r="22" fill="#a07b4e" {o(4)}'
                     f' transform="rotate({kat*720:.0f},{560+kat*420:.0f},684)"/>')
    # сквозняк шевелит край скатерти
    sh = 10 * A.w(t, 1.6)
    s += SL(Z_PERED, f'<path d="M60,746 q{40+sh:.0f},80 -20,150" fill="none"'
                     f' stroke="url(#rush)" stroke-width="26" opacity=".9"/>')
    s += _vinetka(.5)
    return s


def sup_i_kasha_na_plite(t):
    """План 45. Суп кипит, каша пыхтит, нож крошит овощи в суп."""
    s = SL(Z_DAL, kuhnya_stena(t, True, 1480, False, True, 31))
    s += SL(Z_SRED, f'<rect x="60" y="640" width="1100" height="320" rx="16"'
                    f' fill="url(#zhel)" {o(8)}/>'
            + f'<rect x="90" y="672" width="1040" height="26" rx="8" fill="{CHUGUN}" opacity=".6"/>')
    # кастрюля с супом: кипит
    s += SL(Z_SRED, f'<path d="M160,640 q-24,-150 200,-150 q226,0 200,150 z"'
                    f' fill="url(#chug)" {o(7)}/>'
            + f'<ellipse cx="360" cy="492" rx="202" ry="44" fill="#8a5a2c" {o(5)}/>')
    for i in range(6):
        ph = (t * 1.1 + i * .17) % 1.0
        s += SL(Z_PERED, f'<circle cx="{250+i*44}" cy="{488-26*ph:.0f}" r="{8+8*ph:.0f}"'
                         f' fill="#c08a3e" opacity="{.7*(1-ph):.2f}" {o(2)}/>')
    s += SL(Z_PERED, par(360, 440, t, 6, .55, 240, .4, 1.3))
    # каша пыхтит под крышкой
    pyh = 6 * abs(A.w(t, .9))
    s += SL(Z_SRED, f'<path d="M700,640 q-16,-120 160,-120 q176,0 160,120 z"'
                    f' fill="url(#chug)" {o(7)}/>')
    s += SL(Z_PERED, f'<g transform="translate(0,{-pyh:.0f})">'
            + f'<ellipse cx="860" cy="516" rx="170" ry="34" fill="{ZHELEZ}" {o(6)}/>'
            + f'<circle cx="860" cy="488" r="18" fill="{CHUGUN}" {o(4)}/></g>')
    s += SL(Z_PERED, par(860, 470, t, 4, .45, 180, .5, .9))
    # бутыль масла в стороне, закрытая
    s += SL(Z_SRED, f'<path d="M1240,640 q-10,-170 56,-188 l0,-54 h38 l0,54'
                    f' q66,18 56,188 z" fill="#3f5a3a" opacity=".9" {o(7)}/>'
            + f'<rect x="1292" y="382" width="36" height="34" rx="6" fill="url(#solom)" {o(5)}/>')
    # доска с морковью и капустой, нож стучит
    stuk = 16 * abs(A.w(t, .55))
    s += SL(Z_PERED, f'<rect x="1380" y="840" width="440" height="40" rx="10"'
                     f' fill="url(#dosk)" {o(7)}/>'
            + f'<path d="M1430,840 q30,-90 110,-60 q40,16 10,60 z" fill="#d97a2e" {o(5)}/>'
            + f'<circle cx="1660" cy="806" r="54" fill="#dfe8d6" {o(6)}/>'
            + f'<path d="M1620,790 q40,-26 80,0" fill="none" stroke="#b9c9ae" stroke-width="7"/>')
    s += SL(Z_PERED, f'<g transform="translate(0,{-stuk:.0f})">'
            + f'<path d="M1500,770 h220 l30,30 h-250 z" fill="{ZHELEZ}" {o(5)}/>'
            + f'<rect x="1720" y="752" width="120" height="30" rx="8"'
              f' fill="url(#derev)" {o(5)}/></g>')
    s += _vinetka(.42)
    return s


def kleenka_v_kletku_strogiy_den(t):
    """План 46. Мостик в память: стол под клеёнкой, четыре блюда строгого дня."""
    s = SL(Z_DAL, kuhnya_stena(t, True, None, False, True, 37))
    s += SL(Z_SRED, teplo(430, 600, 760, 620, .55))
    s += SL(Z_SRED, stol_bok(40, 700, 800, 300, t))
    # клеёнка в клетку поверх столешницы
    s += SL(Z_SRED, f'<path d="M20,492 h840 l40,208 h-880 z" fill="#e8ddc6" {o(6)}/>'
            + "".join(f'<path d="M{60+j*90},492 l-10,208" stroke="#b9553f"'
                      f' stroke-width="6" opacity=".55"/>' for j in range(9))
            + "".join(f'<path d="M24,{520+j*44} h856" stroke="#b9553f"'
                      f' stroke-width="6" opacity=".45"/>' for j in range(4)))
    bluda = [
        (170, lambda: f'<path d="M90,690 q-10,-110 110,-110 q120,0 110,110 z"'
                      f' fill="url(#krem)" {o(6)}/>'
                      + "".join(f'<ellipse cx="{150+j*46}" cy="{570+(j%2)*12}" rx="30"'
                                f' ry="22" fill="#e8d9a8" {o(4)}/>' for j in range(3))),
        (420, lambda: tarelka(420, 660, 104, t, "url(#krem)", True, 1)
                      + f'<ellipse cx="420" cy="642" rx="72" ry="26" fill="#d9bd86" {o(4)}/>'),
        (650, lambda: f'<ellipse cx="650" cy="664" rx="96" ry="30" fill="url(#krem)" {o(5)}/>'
                      + "".join(f'<ellipse cx="{610+j*40}" cy="650" rx="30" ry="13"'
                                f' fill="{ZEL}" {o(4)}/>' for j in range(3))),
        (820, lambda: f'<rect x="770" y="560" width="110" height="130" rx="10"'
                      f' fill="url(#stekl)" opacity=".75" {o(6)}/>'
                      f'<rect x="762" y="640" width="126" height="50" rx="10"'
                      f' fill="{ZHELEZ}" opacity=".9" {o(5)}/>'
                      f'<path d="M880,590 q50,30 0,70" fill="none" {o(9)}/>'),
    ]
    for i, (xx, f) in enumerate(bluda):
        k = A.over(A.seg(t, .5 + i * .9, .4))
        if k <= 0:
            continue
        kk = min(1.0, k)
        s += SL(Z_PERED, f'<g opacity="{kk:.2f}" transform="translate(0,{-44*(1-kk):.0f})">'
                + f() + '</g>')
    # ложечка звенит в стакане
    zv = 7 * A.w(t, .5)
    s += SL(Z_PERED, f'<path d="M{820+zv:.0f},540 l-20,120" stroke="{ZHELEZ}"'
                     f' stroke-width="9" stroke-linecap="round"/>')
    s += SL(Z_PERED, par(170, 540, t, 5, .5, 190, .45, 1.0))
    # руки семьи тянутся к миске
    for i, (x0, ug, t0) in enumerate(((60, -18, 4.4), (300, 10, 4.9), (560, -6, 5.4))):
        k = A.ease(A.seg(t, t0, .8))
        if k <= 0:
            continue
        s += SL(Z_PERED, f'<g transform="translate({(170-x0)*k*.5:.0f},{-40*k:.0f})"'
                f' opacity="{k:.2f}">' + ruka(x0, 1020, t, 240, ug, 46, "#6b5a6e") + '</g>')
    s += _vinetka(.44)
    return s


def schi_i_pohlebka(t):
    """План 48. Тарелка щей, миска грибной похлёбки, чёрный хлеб."""
    s = SL(Z_DAL, kuhnya_stena(t, True, None, False, True, 41))
    s += SL(Z_SRED, stol_bok(30, 690, 800, 300, t, "#cdbfa2"))
    # тарелка щей крупно
    s += SL(Z_PERED, tarelka(300, 650, 180, t, "url(#krem)", True))
    s += SL(Z_PERED, f'<ellipse cx="300" cy="628" rx="132" ry="48" fill="#b07a38" {o(5)}/>'
            + "".join(f'<path d="M{250+j*34},{618+(j%2)*10} q18,-14 36,2" fill="none"'
                      f' stroke="#dfe8d6" stroke-width="7" opacity=".9"/>' for j in range(4)))
    s += SL(Z_PERED, par(300, 570, t, 6, .55, 220, .4, 1.2))
    # ложка зачерпывает
    zach = A.ease(A.seg(t, .8, 1.4))
    s += SL(Z_PERED, f'<g transform="rotate({-26+40*zach:.0f},470,500)">'
            + f'<path d="M470,500 l180,-120" stroke="{ZHELEZ}" stroke-width="14"'
              f' stroke-linecap="round"/>'
            + f'<ellipse cx="454" cy="512" rx="52" ry="34" fill="{ZHELEZ}" {o(5)}'
              f' transform="rotate(-28,454,512)"/></g>')
    # миска похлёбки с грибами
    s += SL(Z_PERED, f'<path d="M560,690 q-16,-120 160,-120 q176,0 160,120 z"'
                     f' fill="url(#glina)" {o(6)}/>'
            + f'<ellipse cx="720" cy="572" rx="160" ry="36" fill="#6b4a2c" {o(5)}/>'
            + "".join(f'<path d="M{670+j*52},566 q24,-30 48,-2 q-22,16 -48,2 z"'
                      f' fill="#8a6038" {o(4)}/>' for j in range(3)))
    # ломоть чёрного хлеба на доске, крошки
    s += SL(Z_PERED, f'<rect x="60" y="800" width="330" height="34" rx="9"'
                     f' fill="url(#dosk)" {o(6)}/>'
            + f'<path d="M110,800 q10,-110 120,-110 q110,0 120,110 z" fill="#4e3626" {o(6)}/>'
            + f'<path d="M140,730 q90,-26 180,0" fill="none" stroke="#6b4a32" stroke-width="8"/>')
    for i in range(6):
        s += SL(Z_PERED, f'<circle cx="{120+i*48}" cy="{842+(i%3)*8}" r="{5+i%3}"'
                         f' fill="#5e4430" opacity=".9"/>')
    s += _vinetka(.42)
    return s


def tri_skovorodki(t):
    """План 50. Три сковородки загораются по словам: картошка, капуста, грибы."""
    s = SL(Z_DAL, kuhnya_stena(t, True, None, False, True, 43))
    s += SL(Z_SRED, f'<rect x="20" y="620" width="820" height="320" rx="14"'
                    f' fill="url(#zhel)" {o(8)}/>')
    for i in range(3):
        xx = 160 + i * 250
        k = A.ease(A.seg(t, .4 + i * 1.3, .5))
        s += SL(Z_SRED, f'<ellipse cx="{xx}" cy="624" rx="118" ry="34" fill="url(#chug)" {o(6)}/>'
                + f'<path d="M{xx+112},616 h110" {o(12)} fill="none"/>')
        if k <= 0:
            continue
        s += SL(Z_PERED, ogon(xx, 700, t, .5 * k, i * .3, 3))
        if i == 0:                                   # картошка румянится и шкворчит
            shk = 4 * A.w(t, .4)
            s += SL(Z_PERED, f'<g opacity="{k:.2f}" transform="translate({shk:.1f},0)">'
                    + "".join(f'<ellipse cx="{xx-60+j*40}" cy="{608+(j%2)*10}" rx="30"'
                              f' ry="18" fill="#d49a52" {o(4)}/>' for j in range(4)) + '</g>')
            for j in range(4):
                ph = (t * 1.5 + j * .2) % 1.0
                s += SL(Z_PERED, f'<circle cx="{xx-40+j*30}" cy="{590-40*ph:.0f}"'
                                 f' r="{4+3*ph:.0f}" fill="#ffe9b8" opacity="{.5*(1-ph)*k:.2f}"/>')
        elif i == 1:                                 # крышка подпрыгивает
            pr = 14 * abs(A.w(t, .7))
            s += SL(Z_PERED, f'<g opacity="{k:.2f}" transform="translate(0,{-pr:.0f})">'
                    + f'<ellipse cx="{xx}" cy="596" rx="120" ry="28" fill="{ZHELEZ}" {o(6)}/>'
                    + f'<circle cx="{xx}" cy="570" r="16" fill="{CHUGUN}" {o(4)}/></g>')
            s += SL(Z_PERED, par(xx, 560, t, 4, .45 * k, 170, .5, .9))
        else:                                        # лопатка переворачивает грибы
            lop = A.seg(t, 3.2, 1.6)
            s += SL(Z_PERED, f'<g opacity="{k:.2f}">'
                    + "".join(f'<path d="M{xx-50+j*44},610 q22,-28 44,-2 q-20,16 -44,2 z"'
                              f' fill="#8a6038" {o(4)}/>' for j in range(3))
                    + f'<g transform="rotate({-30+60*lop:.0f},{xx+40},540)">'
                    + f'<rect x="{xx-10}" y="540" width="120" height="22" rx="6"'
                      f' fill="{ZHELEZ}" {o(5)}/>'
                    + f'<rect x="{xx+106}" y="520" width="130" height="24" rx="8"'
                      f' fill="url(#derev)" {o(5)}/></g></g>')
    s += _vinetka(.42)
    return s


def zolotoy_luk_na_kashe(t):
    """План 51. Ложка золотого лука опускается на серую кашу, цвет расходится."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#2b2822"/>'
            + doski(0, 0, W, H, 190, False, "derev")
            + f'<rect x="0" y="0" width="{W}" height="{H}" fill="#000000" opacity=".2"/>')
    s += SL(Z_SRED, teplo(960, 640, 900, 620, .55))
    # миска каши крупно
    s += SL(Z_SRED, ten(960, 940, 440, 50, .55))
    s += SL(Z_SRED, f'<path d="M520,620 q0,300 440,300 q440,0 440,-300 z"'
                    f' fill="url(#glina)" {o(9)}/>')
    s += SL(Z_SRED, f'<ellipse cx="960" cy="620" rx="440" ry="132" fill="#8a5a2c" {o(8)}/>'
            + f'<ellipse cx="960" cy="628" rx="398" ry="112" fill="#b9b2a2" {o(0)}/>'
            + f'<path d="M562,628 q398,150 796,0" fill="none" stroke="#6b4a2c"'
              f' stroke-width="14" opacity=".35"/>')
    # золото расходится по каше
    k = A.seg(t, .9, 1.8)
    if k > 0:
        s += SL(Z_PERED, f'<ellipse cx="960" cy="628" rx="{390*k:.0f}" ry="{108*k:.0f}"'
                         f' fill="#d6a63f" opacity="{.75*k:.2f}"/>')
    # ложка с луком опускается
    op = A.ease(A.seg(t, .1, .9))
    ly = 180 + 330 * op
    s += SL(Z_PERED, f'<g transform="translate(0,{ly-180:.0f})">'
            + f'<path d="M1180,120 l260,-120" stroke="{ZHELEZ}" stroke-width="18"'
              f' stroke-linecap="round"/>'
            + f'<ellipse cx="1140" cy="140" rx="110" ry="64" fill="{ZHELEZ}" {o(6)}/>'
            + "".join(f'<path d="M{1090+j*32},{118+(j%2)*14} q18,-14 34,2" fill="none"'
                      f' stroke="{ZOL}" stroke-width="10"/>' for j in range(4))
            + '</g>')
    # масло блестит каплями
    for i in range(7):
        bl = .4 + .6 * abs(A.w(t, 1.4, i * .2))
        s += SL(Z_PERED, f'<ellipse cx="{700+i*86}" cy="{586+(i%3)*14}" rx="{14+4*bl:.0f}"'
                         f' ry="{7+3*bl:.0f}" fill="#ffe9a8" opacity="{.5*bl:.2f}"/>')
    s += SL(Z_PERED, par(960, 540, t, 6, .5, 240, .4, 1.4))
    s += _vinetka(.5)
    return s


def butylka_postnogo_masla(t):
    """Планы 52, 168. Бутылка с бумажной пробкой, завиток запаха, шкафчик."""
    s = SL(Z_DAL, kuhnya_stena(t, True, None, False, True, 47))
    s += SL(Z_SRED, teplo(420, 620, 700, 600, .5))
    # шкафчик повыше
    skr = A.ease(A.seg(t, 2.6, 1.0))
    s += SL(Z_SRED, f'<rect x="120" y="120" width="620" height="300" rx="12"'
                    f' fill="url(#dosk)" {o(8)}/>'
            + f'<g transform="rotate({-28*skr:.0f},130,130)">'
            + f'<rect x="130" y="130" width="296" height="280" rx="8" fill="#b08456" {o(6)}/>'
            + f'<circle cx="400" cy="270" r="12" fill="{MED}" {o(4)}/></g>')
    # бутылка крупно, масло качается
    pod = A.ease(A.seg(t, 1.6, 1.6))
    by = 820 - 420 * pod
    kach = 6 * A.w(t, 1.2)
    s += SL(Z_PERED, f'<g transform="translate(0,{by-820:.0f}) rotate({kach*.4:.1f},420,700)">'
            + ten(420, 836, 120, 24, .5 * (1 - pod))
            + f'<path d="M300,820 q-16,-300 96,-330 l0,-96 h48 l0,96'
              f' q112,30 96,330 z" fill="#2e4630" opacity=".93" {o(8)}/>'
            + f'<path d="M330,700 q90,{20+kach:.0f} 180,0" fill="none" stroke="{MED}"'
              f' stroke-width="14" opacity=".75"/>'
            + f'<rect x="394" y="368" width="52" height="46" rx="8" fill="url(#rush)" {o(5)}/>'
            + f'<path d="M330,560 q20,120 10,240" fill="none" stroke="#ffffff"'
              f' stroke-width="10" opacity=".18"/>'
            + '</g>')
    # завиток запаха с подсолнухом и семечками
    for i in range(3):
        ph = (t * .35 + i * .33) % 1.0
        yy = 360 - ph * 220 + (by - 820)
        xx = 420 + 90 * math.sin(ph * 6 + i)
        s += SL(Z_PERED, f'<circle cx="{xx:.0f}" cy="{yy:.0f}" r="{10+10*ph:.0f}"'
                         f' fill="{ZOL}" opacity="{.4*(1-ph):.2f}"/>')
    pod_k = A.out(A.seg(t, .8, .8))
    if pod_k > 0:
        s += SL(Z_PERED, f'<g opacity="{pod_k*.9:.2f}" transform="translate(660,330)">'
                + f'<circle cx="0" cy="0" r="54" fill="#6b4a2c" {o(5)}/>'
                + "".join(f'<ellipse cx="{76*math.cos(j*.7):.0f}" cy="{76*math.sin(j*.7):.0f}"'
                          f' rx="34" ry="17" fill="{ZOL}" {o(3)}'
                          f' transform="rotate({j*40:.0f},0,0)"/>' for j in range(9))
                + "".join(f'<ellipse cx="{-40+j*26}" cy="96" rx="11" ry="17"'
                          f' fill="#3a2f22" {o(3)}/>' for j in range(3))
                + '</g>')
    s += SL(Z_PERED, ruka(60, 980, t, 250, -30, 48, "#6b5a6e"))
    s += _vinetka(.44)
    return s


def testo_pod_polotencem(t):
    """План 54. Тесто поднимает полотенце шапкой, рядом румяный пирог."""
    s = SL(Z_DAL, kuhnya_stena(t, True, None, False, True, 53))
    s += SL(Z_SRED, teplo(400, 640, 740, 600, .55))
    s += SL(Z_SRED, stol_bok(20, 720, 820, 280, t))
    # кастрюля, тесто дышит и растёт
    rost = A.ease(A.seg(t, .2, 3.4))
    dysh = 10 * A.w(t, 1.5)
    s += SL(Z_SRED, f'<path d="M160,712 q-18,-200 180,-200 q198,0 180,200 z"'
                    f' fill="#e9eef0" {o(8)}/>'
            + f'<ellipse cx="340" cy="512" rx="182" ry="42" fill="#d6dde0" {o(6)}/>'
            + f'<path d="M160,640 h360" stroke="{ZHELEZ}" stroke-width="10" opacity=".5"/>')
    s += SL(Z_PERED, f'<path d="M150,{512-40*rost-dysh*.4:.0f}'
            f' q190,-{110*rost+dysh:.0f} 380,0'
            f' q-20,120 -190,126 q-170,-6 -190,-126 z" fill="url(#rush)" {o(7)}/>')
    s += SL(Z_PERED, f'<path d="M180,{520-30*rost:.0f} q160,-{70*rost+dysh*.6:.0f} 320,0"'
                     f' fill="none" stroke="{TKAN}" stroke-width="9" opacity=".7"/>')
    # пирог на доске рядом
    pir = A.out(A.seg(t, 2.6, .8))
    if pir > 0:
        s += SL(Z_PERED, f'<g opacity="{pir:.2f}">'
                + f'<rect x="560" y="690" width="300" height="34" rx="9"'
                  f' fill="url(#dosk)" {o(6)}/>'
                + f'<path d="M580,690 q10,-120 130,-120 q120,0 130,120 z"'
                  f' fill="url(#solom)" {o(7)}/>'
                + f'<path d="M620,626 q90,-30 180,0" fill="none" stroke="#c08a3e"'
                  f' stroke-width="9"/>'
                + "".join(f'<path d="M{640+j*40},660 l24,-26" stroke="#b47a36"'
                          f' stroke-width="6"/>' for j in range(4))
                + par(710, 580, t, 5, .5, 200, .45, 1.0) + '</g>')
    s += _vinetka(.44)
    return s


# ═══════════════ БЛОК 5. ЧЕМ ПОСТИЛИСЬ НАШИ БАБУШКИ ═══════════════
def chetyre_rybnyh_dnya(t):
    """Планы 57, 59. Четыре тарелки жареной рыбы, бирки дней загораются."""
    s = SL(Z_DAL, kuhnya_stena(t, True, None, False, True, 59))
    s += SL(Z_SRED, stol_bok(40, 740, 1840, 260, t, "#cdbfa2"))
    dni = ("Вт", "Чт", "Сб", "Вс")
    for i, d in enumerate(dni):
        xx = 300 + i * 440
        s += SL(Z_SRED, tarelka(xx, 700, 150, t))
        s += SL(Z_SRED, ryba(xx, 674, .85, t))
        k = A.out(A.seg(t, .5 + i * .6, .4))
        if k > 0:
            s += SL(Z_PERED, f'<g opacity="{k:.2f}">'
                    + f'<rect x="{xx-70}" y="800" width="140" height="62" rx="10"'
                      f' fill="url(#zol)" {o(5)}/>'
                    + f'<text x="{xx}" y="845" font-family="Georgia,serif" font-size="40"'
                      f' text-anchor="middle" fill="#2a1d08">{d}</text></g>')
    # на последней фразе густой пар от всех четырёх
    gust = A.seg(t, 3.2, 1.2)
    for i in range(4):
        s += SL(Z_PERED, par(300 + i * 440, 620, t, 5 + int(3 * gust),
                             .4 + .4 * gust, 240, .42, 1.2))
    # вилка звякает о край тарелки
    zv = 9 * A.w(t, .45)
    s += SL(Z_PERED, f'<path d="M1680,{660+zv:.0f} l90,-110" stroke="{ZHELEZ}"'
                     f' stroke-width="12" stroke-linecap="round"/>'
            + "".join(f'<path d="M{1660+j*14},{676+zv:.0f} l{18-j*2},-28"'
                      f' stroke="{ZHELEZ}" stroke-width="7"/>' for j in range(3)))
    s += _vinetka(.42)
    return s


def podushka_s_podarkom(t):
    """План 58. Ночь, рука подсовывает свёрток под подушку спящего ребёнка."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#1b2336"/>'
            + f'<rect x="1300" y="120" width="500" height="460" rx="12"'
              f' fill="url(#nnoch)" {o(9)}/>'
            + f'<path d="M1550,120 v460 M1300,350 h500" {o(7)} fill="none"/>')
    # луна за окном
    s += SL(Z_DAL, f'<circle cx="1660" cy="250" r="78" fill="#fdf6e0" opacity=".95"/>'
            + f'<circle cx="1630" cy="230" r="18" fill="#e8e0c8" opacity=".5"/>'
            + f'<circle cx="1660" cy="250" r="190" fill="url(#holod)" opacity=".6"/>')
    s += SL(Z_DAL, sneg_letit(t, 14, 31, .4, .5))
    # лунный свет полосой на кровати
    s += SL(Z_SRED, f'<path d="M1300,580 l-700,500 h520 l480,-500 z" fill="#9ec8e8"'
                    f' opacity=".14"/>')
    # кровать
    s += SL(Z_SRED, f'<rect x="60" y="760" width="1180" height="40" rx="10"'
                    f' fill="url(#derev)" {o(8)}/>'
            + f'<rect x="60" y="560" width="46" height="240" rx="12"'
              f' fill="url(#derev)" {o(7)}/>'
            + f'<rect x="1194" y="620" width="46" height="180" rx="12"'
              f' fill="url(#derev)" {o(7)}/>')
    # одеяло дышит
    dysh = 8 * A.w(t, 3.6)
    s += SL(Z_SRED, f'<path d="M420,800 q{300+dysh:.0f},-{130+dysh:.0f} {760:.0f},-10'
                    f' v110 h-760 z" fill="#4a5b7a" {o(7)}/>'
            + f'<path d="M460,{740-dysh*.4:.0f} q300,-60 700,-4" fill="none"'
              f' stroke="#6b7fa0" stroke-width="12" opacity=".8"/>')
    # подушка и спящий ребёнок
    s += SL(Z_SRED, f'<path d="M150,790 q-20,-160 220,-160 q240,0 220,160 z"'
                    f' fill="#e8e4d8" {o(7)}/>'
            + f'<path d="M190,700 q180,-50 340,-6" fill="none" stroke="#cfcabc"'
              f' stroke-width="10"/>')
    s += SL(Z_SRED, f'<ellipse cx="470" cy="700" rx="86" ry="74" fill="#e8bb93" {o(6)}/>'
            + f'<path d="M408,672 q50,-56 120,-20 q-30,26 -120,20 z" fill="#4a3b2e" {o(5)}/>'
            + f'<path d="M488,712 h34" {o(4)} fill="none"/>')
    # рука подсовывает свёрток под подушку
    k = A.ease(A.seg(t, .8, 2.4))
    sx = 760 - 420 * k
    s += SL(Z_PERED, f'<g transform="translate({sx-760:.0f},{40*k:.0f})">'
            + ruka(1060, 900, t, 260, -24, 52, "#5e5468")
            + f'<rect x="700" y="820" width="180" height="100" rx="12"'
              f' fill="#b9553f" {o(6)}/>'
            + f'<path d="M790,820 v100 M700,866 h180" stroke="#f0d08a"'
              f' stroke-width="14" opacity="{.6+.4*abs(A.w(t,1.3)):.2f}"/>'
            + f'<path d="M760,812 q30,-46 66,-10 q-30,20 -66,10 z" fill="#f0d08a" {o(4)}/>'
            + '</g>')
    s += _vinetka(.56)
    return s


def rybnyy_otdel_s_vesami(t):
    """Планы 60-61. Рыбный отдел: кафель, весы со стрелкой, лоток со льдом."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#cfd8d6"/>')
    for i in range(13):
        for j in range(5):
            s += SL(Z_DAL, f'<rect x="{-20+i*152}" y="{60+j*124}" width="142" height="114"'
                           f' rx="6" fill="#eef3f1" opacity=".75" {o(3)}/>')
    s += SL(Z_DAL, f'<rect x="0" y="680" width="{W}" height="400" fill="#8d9a96"/>')
    # прилавок с лотком со льдом
    s += SL(Z_SRED, f'<rect x="60" y="700" width="1800" height="60" rx="10"'
                    f' fill="#e2e6e4" {o(8)}/>'
            + f'<rect x="60" y="760" width="1800" height="240" fill="#b9c4c0" {o(7)}/>')
    s += SL(Z_SRED, f'<rect x="700" y="640" width="760" height="70" rx="10"'
                    f' fill="#cfe0e8" {o(7)}/>')
    for i in range(9):
        bl = .4 + .6 * abs(A.w(t, 1.5, i * .18))
        s += SL(Z_PERED, f'<path d="M{730+i*80},700 l34,-44 l34,44 z"'
                         f' fill="#eaf4fa" opacity="{.5+.4*bl:.2f}" {o(3)}/>')
    for i in range(3):
        s += SL(Z_PERED, ryba(820 + i * 240, 676, .62, t, False))
    # весы со стрелкой
    s += SL(Z_SRED, f'<rect x="220" y="470" width="300" height="240" rx="14"'
                    f' fill="#e8ece8" {o(8)}/>'
            + f'<circle cx="370" cy="580" r="96" fill="#fdfdf8" {o(7)}/>'
            + f'<path d="M290,580 a80,80 0 0 1 160,0" fill="none" stroke="#8d939c"'
              f' stroke-width="6"/>')
    ang = -60 + 40 * A.w(t, 2.2)
    s += SL(Z_PERED, f'<g transform="rotate({ang:.1f},370,580)">'
            + f'<path d="M370,580 v-74" stroke="{KRAS}" stroke-width="8"'
              f' stroke-linecap="round"/></g>'
            + f'<circle cx="370" cy="580" r="12" fill="{K}"/>')
    s += SL(Z_SRED, f'<rect x="250" y="430" width="240" height="20" rx="7"'
                    f' fill="{ZHELEZ}" {o(5)}/>')
    # руки продавщицы заворачивают рыбу в серую бумагу
    shur = 6 * A.w(t, 1.1)
    s += SL(Z_PERED, f'<g transform="translate({shur:.0f},0)">'
            + f'<path d="M1180,700 l260,-90 l110,80 l-250,100 z" fill="#b9bdb6" {o(6)}/>'
            + ruka(1620, 560, t, 230, 150, 50, "#e8e4d8")
            + ruka(1700, 760, t, 230, 196, 50, "#e8e4d8") + '</g>')
    # очередь со спины
    for i, (xx, h_, col) in enumerate(((120, 560, "#4a4152"), (300, 600, "#3f4a5c"),
                                       (470, 540, "#5e4a42"))):
        s += SL(Z_PERED, f'<g opacity=".95">'
                + spina(xx, 1080, h_, t, col, TKAN if i % 2 == 0 else None, i * .2)
                + '</g>')
    s += _vinetka(.44)
    return s


def skovorodka_na_dva_dnya(t):
    """План 62. Сковорода рыбы: половину съели, вторую накрыли до утра."""
    s = SL(Z_DAL, kuhnya_stena(t, True, 1380, True, True, 61))
    # за окном ночь сменяется утром
    utro = A.ease(A.seg(t, 1.4, 1.4))
    s += SL(Z_DAL, f'<rect x="1380" y="160" width="420" height="380" rx="8"'
                   f' fill="url(#nrassv)" opacity="{utro:.2f}"/>')
    s += SL(Z_SRED, stol_bok(80, 700, 1120, 300, t))
    # большая чугунная сковорода
    s += SL(Z_PERED, ten(560, 700, 320, 40, .5)
            + f'<ellipse cx="560" cy="660" rx="330" ry="104" fill="url(#chug)" {o(8)}/>'
            + f'<ellipse cx="560" cy="648" rx="280" ry="82" fill="#3a3634"/>'
            + f'<path d="M880,640 h250" {o(18)} fill="none"/>')
    # рыба: половину съедают
    s_est = A.ease(A.seg(t, .3, .9))
    for i in range(4):
        if i >= 4 - int(2 * s_est):
            continue
        s += SL(Z_PERED, ryba(430 + i * 110, 636, .5, t))
    # рыба шкворчит
    for i in range(5):
        ph = (t * 1.4 + i * .2) % 1.0
        s += SL(Z_PERED, f'<circle cx="{430+i*90}" cy="{600-50*ph:.0f}" r="{5+4*ph:.0f}"'
                         f' fill="#ffe9b8" opacity="{.55*(1-ph):.2f}"/>')
    # крышка опускается и снимается под утро
    kr = A.ease(A.seg(t, 1.0, .7)) - A.ease(A.seg(t, 2.6, .7))
    if kr > .02:
        s += SL(Z_PERED, f'<g transform="translate(0,{-260*(1-kr):.0f})" opacity="{kr:.2f}">'
                + f'<ellipse cx="560" cy="600" rx="330" ry="86" fill="{ZHELEZ}" {o(7)}/>'
                + f'<circle cx="560" cy="548" r="26" fill="{CHUGUN}" {o(5)}/></g>')
    s += _vinetka(.42)
    return s


def tri_glinyanyh_gorshochka(t):
    """План 64. Три горшочка: грибы, горох, фасоль. Крышки приподнимаются."""
    s = SL(Z_DAL, kuhnya_stena(t, True, None, False, True, 67))
    s += SL(Z_SRED, stol_bok(120, 720, 1680, 280, t, "#d9c7a4"))
    nach = [(460, "грибы"), (960, "горох"), (1460, "фасоль")]
    for i, (xx, vid) in enumerate(nach):
        s += SL(Z_SRED, gorshok(xx, 700, 2.2, t, "url(#glina)", False))
        pod = A.ease(A.seg(t, .5 + i * .9, .7))
        s += SL(Z_PERED, f'<g transform="translate(0,{-70*pod:.0f}) rotate({8*pod:.1f},{xx},470)">'
                + f'<ellipse cx="{xx}" cy="474" rx="100" ry="30" fill="url(#glina)" {o(6)}/>'
                + f'<circle cx="{xx}" cy="446" r="18" fill="{MED}" {o(4)}/></g>')
        if pod > .3:
            s += SL(Z_PERED, par(xx, 440, t, 5, .5 * pod, 220, .42, 1.1))
            if vid == "грибы":
                s += SL(Z_PERED, "".join(
                    f'<path d="M{xx-50+j*44},500 q24,-32 48,-2 q-22,18 -48,2 z"'
                    f' fill="#8a6038" {o(4)}/>' for j in range(3)))
            elif vid == "горох":
                s += SL(Z_PERED, "".join(
                    f'<circle cx="{xx-54+j*36}" cy="{504+(j%2)*12}" r="17"'
                    f' fill="{ZEL2}" {o(3)}/>' for j in range(4))
                    + f'<path d="M{xx+70},500 l40,-150" stroke="url(#derev)"'
                      f' stroke-width="16" stroke-linecap="round"/>')
            else:
                s += SL(Z_PERED, "".join(
                    f'<ellipse cx="{xx-48+j*38}" cy="{506+(j%2)*10}" rx="22" ry="14"'
                    f' fill="#e8d6b0" {o(3)}/>' for j in range(4)))
    s += _vinetka(.42)
    return s


def belaya_skatert_sredi_kleenok(t):
    """План 67. Ряд будничных столов, один накрывают белой скатертью."""
    s = SL(Z_DAL, kuhnya_stena(t, True, None, False, True, 71))
    s += SL(Z_SRED, teplo(960, 600, 900, 620, .4))
    for i in range(3):
        xx = 40 + i * 640
        prazd = i == 1
        s += SL(Z_SRED, stol_bok(xx, 780, 560, 280, t))
        if not prazd:
            s += SL(Z_SRED, f'<path d="M{xx-14},634 h588 l28,146 h-616 z"'
                            f' fill="#e8ddc6" {o(6)}/>'
                    + "".join(f'<path d="M{xx+30+j*92},634 l-10,146" stroke="#b9553f"'
                              f' stroke-width="7" opacity=".5"/>' for j in range(6)))
    # белая скатерть ложится волной на третий стол
    xx = 40 + 1 * 640
    k = A.ease(A.seg(t, 1.0, 1.4))
    volna = 16 * A.w(t, 1.8)
    s += SL(Z_PERED, f'<g opacity="{k:.2f}">'
            + f'<path d="M{xx-30},{656-80*(1-k):.0f} h460 l30,{110+volna:.0f}'
              f' q-245,{30:.0f} -520,0 z" fill="#fdfaf2" {o(6)}/>'
            + f'<path d="M{xx-10},{700-60*(1-k):.0f} h420" stroke="#e2dccc"'
              f' stroke-width="8"/></g>')
    # блюдо с рыбой встаёт на белую скатерть
    kb = A.out(A.seg(t, 2.4, .8))
    if kb > 0:
        s += SL(Z_PERED, f'<g opacity="{kb:.2f}" transform="translate(0,{-50*(1-kb):.0f})">'
                + f'<ellipse cx="{xx+200}" cy="664" rx="190" ry="54" fill="url(#krem)" {o(6)}/>'
                + ryba(xx + 200, 640, 1.1, t)
                + par(xx + 200, 580, t, 6, .5, 230, .42, 1.3) + '</g>')
    # свеча на праздничном столе загорается
    ks = A.seg(t, 3.0, .6)
    if ks > 0:
        s += SL(Z_PERED, f'<g opacity="{ks:.2f}">' + svecha(xx + 420, 660, t, .2, 1.5, 110)
                + teplo(xx + 420, 560, 320, 280, .5 * ks) + '</g>')
    s += _vinetka(.42)
    return s


def miska_sochiva_krupno(t):
    """Планы 71, 72, 139. Крупно миска сочива, с ложки льётся мёд."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#2e2620"/>'
            + doski(0, 0, W, H, 200, False, "derev")
            + f'<rect x="0" y="0" width="{W}" height="{H}" fill="#000000" opacity=".22"/>')
    s += SL(Z_SRED, teplo(760, 620, 900, 640, .5))
    # миска крупно, в левой полосе — справа окно вставки
    s += SL(Z_SRED, ten(560, 960, 400, 48, .55))
    s += SL(Z_SRED, f'<path d="M160,600 q0,320 400,320 q400,0 400,-320 z"'
                    f' fill="url(#glina)" {o(9)}/>'
            + f'<ellipse cx="560" cy="600" rx="400" ry="124" fill="#8a5a2c" {o(8)}/>'
            + f'<ellipse cx="560" cy="608" rx="358" ry="104" fill="#e2d8c0" {o(0)}/>')
    # целые зёрна пшеницы блестят
    r = random.Random(5)
    for i in range(44):
        a = r.uniform(0, 6.3)
        rr = r.uniform(0, 1) ** .5
        xx = 560 + math.cos(a) * 320 * rr
        yy = 608 + math.sin(a) * 88 * rr
        bl = .5 + .5 * abs(A.w(t, 1.6, i * .07))
        s += SL(Z_PERED, f'<ellipse cx="{xx:.0f}" cy="{yy:.0f}" rx="18" ry="11"'
                         f' fill="#e8d6a8" {o(3)} transform="rotate({a*57:.0f},{xx:.0f},{yy:.0f})"/>'
                + f'<ellipse cx="{xx-4:.0f}" cy="{yy-3:.0f}" rx="6" ry="3"'
                  f' fill="#fff6d8" opacity="{.5*bl:.2f}"/>')
    # мёд тянется с деревянной ложки
    s += SL(Z_PERED, f'<g transform="rotate(-18,700,300)">'
            + f'<rect x="700" y="180" width="260" height="34" rx="14"'
              f' fill="url(#derev)" {o(6)}/>'
            + f'<ellipse cx="690" cy="220" rx="96" ry="58" fill="url(#derev)" {o(6)}/>'
            + f'<ellipse cx="690" cy="214" rx="72" ry="42" fill="{MED}" {o(4)}/></g>')
    kt = A.seg(t, .4, 2.2)
    if kt > 0:
        wob = 10 * A.w(t, 1.4)
        s += SL(Z_PERED, f'<path d="M676,278 q{wob:.0f},{150*kt:.0f} -4,{300*kt:.0f}"'
                         f' fill="none" stroke="{MED}" stroke-width="18"'
                         f' stroke-linecap="round" opacity=".95"/>')
        if kt > .7:
            s += SL(Z_PERED, f'<ellipse cx="660" cy="600" rx="{90*(kt-.7)*3:.0f}"'
                             f' ry="{24*(kt-.7)*3:.0f}" fill="{MED}" opacity=".8"/>')
    s += SL(Z_PERED, par(500, 540, t, 5, .45, 210, .42, 1.2))
    s += _vinetka(.5)
    return s


def vazochka_s_kutey(t):
    """План 73. Хрустальная вазочка на ножке, кутья с изюмом, лампа."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#b9ad96"/>'
            + f'<rect x="0" y="0" width="{W}" height="420" fill="#a39780"/>'
            + f'<rect x="0" y="406" width="{W}" height="22" fill="#8a7e68"/>'
            + _kvartira_veschi(1480, 1040, 420, t, 15))
    # лампа с абажуром
    s += SL(Z_SRED, f'<path d="M700,0 v160" {o(7)} fill="none"/>'
            + lampa(700, 200, t, 2.2, True) + teplo(700, 560, 820, 620, .55))
    # стол с крахмальной скатертью
    s += SL(Z_SRED, stol_bok(100, 780, 1300, 280, t))
    s += SL(Z_SRED, f'<path d="M60,640 h1380 l40,140 q-720,46 -1460,0 z"'
                    f' fill="#fdfaf2" {o(6)}/>'
            + f'<path d="M100,700 h1300" stroke="#e8e2d4" stroke-width="9"/>'
            + "".join(f'<path d="M{160+j*150},648 q20,40 0,80" fill="none"'
                      f' stroke="#e8e2d4" stroke-width="6" opacity=".9"/>' for j in range(9)))
    # вазочка на ножке
    bl = .45 + .55 * abs(A.w(t, 1.7))
    s += SL(Z_PERED, ten(620, 650, 170, 22, .4)
            + f'<path d="M500,620 q0,-120 120,-120 q120,0 120,120 z"'
              f' fill="url(#stekl)" opacity=".8" {o(7)}/>'
            + f'<rect x="604" y="620" width="32" height="70" rx="8"'
              f' fill="url(#stekl)" opacity=".85" {o(5)}/>'
            + f'<ellipse cx="620" cy="694" rx="92" ry="22" fill="url(#stekl)"'
              f' opacity=".85" {o(5)}/>'
            + f'<path d="M520,560 q100,40 200,0" fill="none" stroke="#ffffff"'
              f' stroke-width="10" opacity="{.3+.4*bl:.2f}"/>')
    # кутья и изюм сверху
    s += SL(Z_PERED, f'<ellipse cx="620" cy="520" rx="116" ry="34" fill="#e2d8c0" {o(5)}/>')
    for i in range(7):
        s += SL(Z_PERED, f'<ellipse cx="{560+i*22}" cy="{508+(i%3)*8}" rx="13" ry="10"'
                         f' fill="#4a2f26" {o(3)}/>')
    # изюминка скатывается
    kat = A.seg(t, 1.6, 1.6)
    if kat > 0:
        s += SL(Z_PERED, f'<ellipse cx="{700+kat*180:.0f}" cy="{540+kat*110:.0f}"'
                         f' rx="13" ry="10" fill="#4a2f26" {o(3)}/>')
    s += _vinetka(.44)
    return s


def pshenica_ris_i_gorst_izyuma(t):
    """План 74. Мешочки с пшеницей и рисом, изюм и курага из ладони, ложки."""
    s = SL(Z_DAL, kuhnya_stena(t, True, None, False, True, 73))
    s += SL(Z_SRED, stol_bok(60, 760, 1800, 260, t, "#d9c7a4"))
    # два холщовых мешочка
    for i, (xx, zerno) in enumerate(((320, "pshenica"), (700, "ris"))):
        s += SL(Z_SRED, f'<path d="M{xx-130},700 q-20,-240 130,-250 q150,10 130,250 z"'
                        f' fill="url(#solom)" {o(8)}/>'
                + f'<path d="M{xx-90},470 q90,-40 180,0 q-90,30 -180,0 z"'
                  f' fill="#c89a4e" {o(6)}/>'
                + f'<path d="M{xx-110},560 h220" stroke="#b58a42" stroke-width="9" opacity=".7"/>')
        for j in range(7):
            yy = 500 + (j % 3) * 18
            col = "#e8d6a8" if zerno == "pshenica" else "#f6f2e4"
            s += SL(Z_PERED, f'<ellipse cx="{xx-70+j*24}" cy="{yy}" rx="15" ry="10"'
                             f' fill="{col}" {o(3)}/>')
    # из ладони сыплются изюм и курага
    s += SL(Z_PERED, ruka(1080, 330, t, 250, 16, 58, "#6b5a6e"))
    for i in range(9):
        ph = (t * .7 + i * .11) % 1.0
        xx = 1330 + 40 * math.sin(i * 1.7) - 20 * ph
        yy = 400 + ph * 330
        col = "#4a2f26" if i % 2 else "#d99a3e"
        s += SL(Z_PERED, f'<ellipse cx="{xx:.0f}" cy="{yy:.0f}" rx="15" ry="12"'
                         f' fill="{col}" {o(3)} opacity="{1-ph*.3:.2f}"/>')
    s += SL(Z_PERED, f'<path d="M1200,760 q-16,-120 150,-120 q166,0 150,120 z"'
                     f' fill="url(#glina)" {o(7)}/>'
            + f'<ellipse cx="1350" cy="640" rx="152" ry="34" fill="#e2d8c0" {o(5)}/>')
    # ложки семьи разом зачерпывают
    for i, (x0, ug, t0) in enumerate(((1120, -24, 3.6), (1360, -4, 3.8), (1600, 16, 4.0))):
        k = A.ease(A.seg(t, t0, .7))
        if k <= 0:
            continue
        s += SL(Z_PERED, f'<g transform="translate(0,{-120*k+120:.0f})" opacity="{k:.2f}">'
                + f'<g transform="rotate({ug},{x0},700)">'
                + f'<path d="M{x0},700 l40,-230" stroke="{ZHELEZ}" stroke-width="14"'
                  f' stroke-linecap="round"/>'
                + f'<ellipse cx="{x0-6}" cy="712" rx="48" ry="32" fill="{ZHELEZ}" {o(5)}/>'
                + '</g></g>')
    s += _vinetka(.42)
    return s


def kuhnya_s_polovikom_i_zanaveskoy(t):
    """План 75. Смена главы: вечерняя кухня, половик, занавеска в горошек."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#e8d9b4"/>'
            + f'<rect x="0" y="{H-470}" width="{W}" height="210" fill="#8a9a7e"/>'
            + f'<rect x="0" y="{H-260}" width="{W}" height="260" fill="url(#pol)"/>'
            + polovicy(H - 260)
            + f'<rect x="0" y="0" width="{W}" height="{H}" fill="url(#zakat)" opacity=".22"/>')
    # окно с занавеской в горошек
    s += SL(Z_DAL, f'<rect x="1300" y="150" width="440" height="400" rx="10"'
                   f' fill="url(#zakat)" {o(9)}/>'
            + f'<path d="M1520,150 v400 M1300,350 h440" {o(7)} fill="none"/>')
    kol = 9 * A.w(t, 2.4)
    for sgn, x0 in ((1, 1266), (-1, 1774)):
        s += SL(Z_SRED, f'<path d="M{x0},140 q{sgn*(96+kol):.0f},150 {sgn*52:.0f},430'
                        f' q{-sgn*58:.0f},-34 {-sgn*104:.0f},-430 z"'
                        f' fill="#f6eedc" {o(5)}/>')
        for j in range(7):
            s += SL(Z_SRED, f'<circle cx="{x0+sgn*(34+j%3*20):.0f}" cy="{200+j*56}"'
                            f' r="10" fill="{TKAN}" opacity=".8"/>')
    s += SL(Z_SRED, f'<rect x="1250" y="126" width="540" height="40" rx="10"'
                    f' fill="{TKAN}" {o(5)} opacity=".9"/>')
    # полка с кастрюлями
    s += SL(Z_DAL, f'<rect x="80" y="330" width="900" height="30" rx="8"'
                   f' fill="url(#dosk)" {o(7)}/>')
    for i in range(4):
        xx = 190 + i * 220
        s += SL(Z_DAL, f'<path d="M{xx-80},330 q-10,-120 80,-120 q90,0 80,120 z"'
                       f' fill="{"#e9eef0" if i%2 else "url(#zhel)"}" {o(6)}/>'
                + f'<ellipse cx="{xx}" cy="210" rx="82" ry="20" fill="{ZHELEZ}" {o(5)}/>')
    # плита, от неё плывут завитки запаха
    s += SL(Z_SRED, f'<rect x="1020" y="620" width="420" height="260" rx="14"'
                    f' fill="url(#zhel)" {o(8)}/>'
            + f'<path d="M1120,620 q-20,-130 130,-130 q150,0 130,130 z" fill="url(#chug)" {o(7)}/>')
    for i in range(4):
        ph = (t * .3 + i * .25) % 1.0
        xx = 1250 + 120 * math.sin(ph * 5 + i)
        s += SL(Z_PERED, f'<path d="M{xx:.0f},{500-ph*300:.0f} q40,-50 0,-100'
                         f' q-40,-50 0,-100" fill="none" stroke="#efe2c4"'
                         f' stroke-width="{10-5*ph:.0f}" opacity="{.5*(1-ph):.2f}"/>')
    # пёстрый половик и кот на нём
    s += SL(Z_SRED, f'<path d="M160,1020 h900 l-90,90 h-760 z" fill="{TKAN}" {o(6)}/>'
            + "".join(f'<path d="M{200+j*130},1024 l-80,82" stroke="{"#e3d6b4" if j%2 else "#5e8a6a"}"'
                      f' stroke-width="18" opacity=".9"/>' for j in range(7)))
    pot = A.seg(t, 1.6, 1.8)
    s += SL(Z_PERED, f'<g transform="translate({40*pot:.0f},0) scale({1+.12*pot:.2f},1)">'
            + kot(520, 1060, t, 1.3) + '</g>')
    s += _vinetka(.44)
    return s


def tri_chugunka_kashi(t):
    """План 76. Три чугунка: гречка, пшено, рис. Крышки приподнимаются."""
    s = SL(Z_DAL, kuhnya_stena(t, True, None, False, True, 79))
    s += SL(Z_SRED, f'<rect x="20" y="700" width="820" height="300" rx="14"'
                    f' fill="url(#zhel)" {o(8)}/>')
    kashi = (("#6b5438", "гречка"), ("#e0b84a", "пшено"), ("#f6f2e4", "рис"))
    for i, (col, _) in enumerate(kashi):
        xx = 150 + i * 270
        s += SL(Z_SRED, f'<path d="M{xx-110},700 q-26,-190 110,-190 q136,0 110,190 z"'
                        f' fill="url(#chug)" {o(8)}/>')
        pod = A.ease(A.seg(t, .5 + i * 1.1, .7))
        if pod > .15:
            s += SL(Z_SRED, f'<ellipse cx="{xx}" cy="516" rx="112" ry="26"'
                            f' fill="{col}" {o(5)}/>')
            s += SL(Z_PERED, par(xx, 470, t, 5, .5 * pod, 220, .42, 1.1))
        s += SL(Z_PERED, f'<g transform="translate(0,{-90*pod:.0f}) rotate({7*pod:.1f},{xx},500)">'
                + f'<ellipse cx="{xx}" cy="504" rx="118" ry="30" fill="{ZHELEZ}" {o(6)}/>'
                + f'<circle cx="{xx}" cy="474" r="19" fill="{CHUGUN}" {o(5)}/></g>')
    # ложка стоит в гречке
    kach = 2.5 * A.w(t, 1.6)
    s += SL(Z_PERED, f'<g transform="rotate({-12+kach:.1f},150,520)">'
            + f'<path d="M150,520 l40,-260" stroke="url(#derev)" stroke-width="20"'
              f' stroke-linecap="round"/></g>')
    s += _vinetka(.42)
    return s


def korzina_lukoshko_i_kadushka(t):
    """План 77. На лавке парами: горох и фасоль, овощи, грибы, соленья."""
    s = SL(Z_DAL, kuhnya_stena(t, True, None, False, True, 83))
    s += SL(Z_SRED, f'<rect x="40" y="790" width="1840" height="40" rx="10"'
                    f' fill="url(#dosk)" {o(8)}/>'
            + f'<rect x="120" y="830" width="40" height="200" fill="url(#derev)" {o(6)}/>'
            + f'<rect x="1740" y="830" width="40" height="200" fill="url(#derev)" {o(6)}/>')
    pary = [
        (230, lambda: f'<path d="M140,786 q-14,-120 110,-120 q124,0 110,120 z"'
                      f' fill="url(#glina)" {o(7)}/>'
                      + "".join(f'<circle cx="{200+j*34}" cy="{670+(j%2)*12}" r="16"'
                                f' fill="{ZEL2}" {o(3)}/>' for j in range(4))),
        (480, lambda: f'<path d="M390,786 q-14,-120 110,-120 q124,0 110,120 z"'
                      f' fill="url(#krem)" {o(7)}/>'
                      + "".join(f'<ellipse cx="{450+j*32}" cy="{672+(j%2)*10}" rx="21"'
                                f' ry="13" fill="#e8d6b0" {o(3)}/>' for j in range(4))),
        (800, lambda: f'<path d="M660,786 q-20,-200 160,-200 q180,0 160,200 z"'
                      f' fill="url(#solom)" {o(8)}/>'
                      f'<path d="M660,700 h320" stroke="#b58a42" stroke-width="10" opacity=".7"/>'
                      + "".join(f'<circle cx="{720+j*54}" cy="{572+(j%2)*18}" r="34"'
                                f' fill="{["#c0392b","#d9a441","#5e8a3a"][j%3]}" {o(5)}/>'
                                for j in range(4))),
        (1180, lambda: f'<path d="M1060,786 q-10,-160 130,-160 q140,0 130,160 z"'
                       f' fill="url(#solom)" {o(8)}/>'
                       + "".join(f'<path d="M{1110+j*50},620 q30,-40 60,-4'
                                 f' q-28,22 -60,4 z" fill="#8a6038" {o(4)}/>' for j in range(3))),
        (1560, lambda: f'<path d="M1430,786 q0,-220 150,-220 q150,0 150,220 z"'
                       f' fill="url(#derev)" {o(9)}/>'
                       f'<ellipse cx="1580" cy="566" rx="152" ry="36" fill="#9ab07e" {o(6)}/>'
                       f'<path d="M1460,620 h240" stroke="#5e4428" stroke-width="12" opacity=".8"/>'),
    ]
    for i, (xx, f) in enumerate(pary):
        k = A.over(A.seg(t, .3 + i * .7, .36))
        if k <= 0:
            continue
        kk = min(1.0, k)
        s += SL(Z_PERED, f'<g opacity="{kk:.2f}" transform="translate(0,{-48*(1-kk):.0f})">'
                + f() + '</g>')
    # яблоко скатывается с корзины
    kat = A.seg(t, 3.4, 1.6)
    if kat > 0:
        s += SL(Z_PERED, f'<circle cx="{980+kat*420:.0f}" cy="{770+30*math.sin(kat*3):.0f}"'
                         f' r="34" fill="#c0392b" {o(5)}/>'
                + f'<path d="M{980+kat*420:.0f},{740+30*math.sin(kat*3):.0f} q10,-20 24,-14"'
                  f' fill="none" stroke="{ZEL}" stroke-width="7"/>')
    # рассол плещется в кадушке
    pl = 8 * A.w(t, 1.3)
    s += SL(Z_PERED, f'<path d="M1440,{566+pl*.4:.0f} q140,{26+pl:.0f} 290,0"'
                     f' fill="none" stroke="#c8d8b0" stroke-width="10" opacity=".85"/>')
    s += _vinetka(.42)
    return s


def chaynyy_ugol_stola(t):
    """План 78. Каравай, орехи, мёд в сотах, варенье. Нож режет хлеб."""
    s = SL(Z_DAL, kuhnya_stena(t, True, None, False, True, 89))
    s += SL(Z_SRED, teplo(430, 620, 760, 600, .5))
    s += SL(Z_SRED, stol_bok(20, 700, 820, 300, t, "#e7dcc4"))
    # каравай на доске
    s += SL(Z_PERED, f'<rect x="60" y="676" width="420" height="36" rx="10"'
                     f' fill="url(#dosk)" {o(7)}/>'
            + karavay(270, 676, 1.6, False))
    # нож режет каравай, крошки падают
    rez = A.seg(t, .6, 2.2)
    s += SL(Z_PERED, f'<g transform="translate({rez*150:.0f},{18*abs(A.w(t,.7)):.0f})">'
            + f'<path d="M180,520 h300 l40,34 h-340 z" fill="{ZHELEZ}" {o(5)}/>'
            + f'<rect x="480" y="508" width="150" height="34" rx="10"'
              f' fill="url(#derev)" {o(5)}/></g>')
    for i in range(5):
        ph = (t * .9 + i * .2) % 1.0
        s += SL(Z_PERED, f'<circle cx="{200+i*44}" cy="{690+ph*40:.0f}" r="{6-2*ph:.0f}"'
                         f' fill="#c9a86a" opacity="{.9*(1-ph):.2f}"/>')
    # миска орехов
    s += SL(Z_PERED, f'<path d="M520,700 q-12,-110 110,-110 q122,0 110,110 z"'
                     f' fill="url(#glina)" {o(7)}/>'
            + "".join(f'<circle cx="{580+j*34}" cy="{596+(j%2)*14}" r="25"'
                      f' fill="#a07b4e" {o(4)}/>' for j in range(4)))
    # мёд в сотах на блюдце, мёд течёт
    s += SL(Z_PERED, f'<ellipse cx="300" cy="880" rx="150" ry="42" fill="url(#krem)" {o(6)}/>')
    for r_ in range(2):
        for c_ in range(4):
            xx = 236 + c_ * 42 + (21 if r_ else 0)
            yy = 850 + r_ * 38
            s += SL(Z_PERED, f'<path d="M{xx},{yy-22} l20,12 v24 l-20,12 l-20,-12'
                             f' v-24 z" fill="{ZOL}" {o(3)}/>')
    kt = A.seg(t, 1.2, 2.0)
    if kt > 0:
        s += SL(Z_PERED, f'<path d="M330,890 q{10*A.w(t,1.5):.0f},{40*kt:.0f} -6,{70*kt:.0f}"'
                         f' fill="none" stroke="{MED}" stroke-width="12"'
                         f' stroke-linecap="round"/>')
    # розетка варенья
    s += SL(Z_PERED, f'<path d="M560,880 q0,-70 100,-70 q100,0 100,70 z"'
                     f' fill="url(#stekl)" opacity=".8" {o(6)}/>'
            + f'<ellipse cx="660" cy="818" rx="86" ry="20" fill="#8e1f2c" {o(4)}/>')
    s += _vinetka(.44)
    return s


def kastryulya_kazanok_i_salatnica(t):
    """План 79. Три пары рук: мешают суп, закрывают казанок, режут овощи."""
    s = SL(Z_DAL, kuhnya_stena(t, True, None, False, True, 97))
    s += SL(Z_SRED, f'<rect x="20" y="720" width="1880" height="320" rx="14"'
                    f' fill="url(#zhel)" {o(8)}/>')
    # 1. кастрюля, ложка мешает суп
    s += SL(Z_SRED, f'<path d="M160,720 q-24,-180 200,-180 q224,0 200,180 z"'
                    f' fill="#e9eef0" {o(8)}/>'
            + f'<ellipse cx="360" cy="542" rx="202" ry="46" fill="#c08a3e" {o(5)}/>')
    ug = 40 * A.w(t, 1.6)
    s += SL(Z_PERED, f'<g transform="rotate({ug:.0f},360,542)">'
            + f'<path d="M360,542 l80,-230" stroke="{ZHELEZ}" stroke-width="16"'
              f' stroke-linecap="round"/></g>'
            + ruka(120, 300, t, 260, 24, 52, "#8a7a6c"))
    s += SL(Z_PERED, par(360, 500, t, 5, .5, 220, .42, 1.1))
    # 2. казанок, крышку закрывают
    zak = A.ease(A.seg(t, .8, 1.2))
    s += SL(Z_SRED, f'<path d="M760,720 q-30,-200 200,-200 q230,0 200,200 z"'
                    f' fill="url(#chug)" {o(8)}/>')
    s += SL(Z_PERED, par(960, 500, t, 6, .55 * (1 - zak * .6), 240, .4, 1.2))
    s += SL(Z_PERED, f'<g transform="translate(0,{-240*(1-zak):.0f})">'
            + f'<ellipse cx="960" cy="520" rx="206" ry="44" fill="{ZHELEZ}" {o(7)}/>'
            + f'<circle cx="960" cy="474" r="24" fill="{CHUGUN}" {o(5)}/></g>'
            + ruka(1240, 330, t, 250, 160, 52, "#8a7a6c"))
    # 3. салатница, нож стучит по доске
    stuk = 18 * abs(A.w(t, .5))
    s += SL(Z_SRED, f'<path d="M1480,720 q-20,-140 180,-140 q200,0 180,140 z"'
                    f' fill="url(#krem)" {o(7)}/>'
            + f'<ellipse cx="1660" cy="582" rx="182" ry="40" fill="{ZEL2}" {o(5)}/>')
    s += SL(Z_PERED, f'<rect x="1420" y="800" width="420" height="36" rx="10"'
                     f' fill="url(#dosk)" {o(7)}/>'
            + f'<g transform="translate(0,{-stuk:.0f})">'
            + f'<path d="M1520,740 h240 l34,34 h-274 z" fill="{ZHELEZ}" {o(5)}/>'
            + f'<rect x="1760" y="726" width="130" height="30" rx="8"'
              f' fill="url(#derev)" {o(5)}/></g>'
            + ruka(1360, 560, t, 230, 10, 50, "#8a7a6c"))
    s += _vinetka(.42)
    return s


def bochka_i_banka_kapusty(t):
    """План 80. Кадр надвое: погреб с бочкой и заснеженный балкон с банкой."""
    # левая половина — погреб
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W//2}" height="{H}" fill="#2a2520"/>'
            + kladka(0, 0, W // 2, H, 78, "#5e564c")
            + f'<rect x="0" y="0" width="{W//2}" height="{H}" fill="#000000" opacity=".2"/>')
    # правая половина — балкон в снегу
    s += SL(Z_DAL, f'<rect x="{W//2}" y="0" width="{W//2}" height="{H}" fill="#b9c9d8"/>'
            + f'<rect x="{W//2}" y="0" width="{W//2}" height="420" fill="#cfdde8"/>'
            + f'<path d="M{W//2},760 h{W//2} v320 h-{W//2} z" fill="{SNEG}"/>'
            + sneg_letit(t, 18, 37, .5, .6))
    s += SL(Z_SRED, f'<path d="M{W//2-6},0 v{H}" stroke="{K}" stroke-width="10" opacity=".8"/>')
    # бочка под гнётом
    s += SL(Z_SRED, ten(400, 1000, 250, 34, .55)
            + f'<path d="M160,980 q-30,-380 240,-380 q270,0 240,380 z"'
              f' fill="url(#derev)" {o(9)}/>'
            + "".join(f'<path d="M{168+j*4},{700+j*120} q232,{40:.0f} {464-j*8},0"'
                      f' fill="none" stroke="{ZHELEZ}" stroke-width="16" opacity=".9"/>'
                      for j in range(3))
            + f'<ellipse cx="400" cy="600" rx="238" ry="56" fill="#9ab07e" {o(7)}/>')
    # рассол блестит, морковка светится
    bl = .4 + .6 * abs(A.w(t, 1.6))
    s += SL(Z_PERED, f'<ellipse cx="360" cy="594" rx="120" ry="26" fill="#e2eecb"'
                     f' opacity="{.3+.3*bl:.2f}"/>'
            + "".join(f'<path d="M{320+j*70},590 l34,-16" stroke="#e07a2c"'
                      f' stroke-width="11" opacity="{.75+.25*bl:.2f}"/>' for j in range(3)))
    # гнёт: круг и камень
    s += SL(Z_PERED, f'<ellipse cx="400" cy="580" rx="170" ry="40" fill="url(#dosk)" {o(6)}/>'
            + f'<path d="M330,560 q70,-60 140,-6 q-70,30 -140,6 z" fill="{KAMEN}" {o(6)}/>')
    # рука набирает капусту миской
    nab = A.ease(A.seg(t, .6, 1.6))
    s += SL(Z_PERED, f'<g transform="translate(0,{180*nab:.0f})">'
            + ruka(60, 260, t, 250, 28, 54, "#6b5a6e")
            + f'<path d="M300,420 q-14,-110 110,-110 q124,0 110,110 z"'
              f' fill="url(#krem)" {o(6)}/>'
            + f'<ellipse cx="410" cy="316" rx="112" ry="26" fill="#9ab07e" {o(4)}/></g>')
    # банка на балконе под капроновой крышкой, снег шапкой
    s += SL(Z_PERED, f'<rect x="1280" y="520" width="300" height="440" rx="20"'
                     f' fill="url(#stekl)" opacity=".85" {o(8)}/>'
            + f'<ellipse cx="1430" cy="540" rx="150" ry="36" fill="#e8f0f6" opacity=".9" {o(6)}/>'
            + f'<rect x="1290" y="500" width="280" height="44" rx="14"'
              f' fill="#cfe0ea" {o(6)}/>'
            + f'<path d="M1300,500 q130,-50 260,0 q-130,26 -260,0 z" fill="{SNEG}" {o(5)}/>')
    for j in range(4):
        s += SL(Z_PERED, f'<ellipse cx="{1330+j*62}" cy="{640+j*70}" rx="56" ry="28"'
                         f' fill="#9ab07e" opacity=".92" {o(4)}/>'
                + f'<path d="M{1310+j*62},{660+j*70} l40,-18" stroke="#e07a2c"'
                  f' stroke-width="10" opacity=".9"/>')
    s += _vinetka(.46)
    return s


def vyazka_gribov_u_belenoy_steny(t):
    """Планы 81, 167. Вязка сушёных грибов у белёной печной стены."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="{PECH}"/>'
            + f'<rect x="0" y="0" width="{W}" height="{H}" fill="url(#teplo)" opacity=".28"/>')
    for i in range(6):
        s += SL(Z_DAL, f'<path d="M{60+i*140},160 q60,200 0,420" fill="none"'
                       f' stroke="#ffffff" stroke-width="22" opacity=".22"/>')
    # окно справа, первый снег
    s += SL(Z_DAL, f'<rect x="1240" y="170" width="520" height="420" rx="12"'
                   f' fill="url(#nden)" {o(9)}/>'
            + f'<path d="M1500,170 v420 M1240,380 h520" {o(7)} fill="none"/>'
            + sneg_letit(t, 22, 41, .55, .6))
    # гвоздь и вязка грибов
    kach = 3.2 * A.w(t, 2.6)
    s += SL(Z_SRED, f'<circle cx="420" cy="150" r="14" fill="{ZHELEZ}" {o(5)}/>')
    s += SL(Z_SRED, f'<g transform="rotate({kach:.1f},420,150)">'
            + f'<path d="M420,150 v780" stroke="#7a6a52" stroke-width="7"/>'
            + "".join(
                f'<g transform="translate({420+(26 if j%2 else -26)},{210+j*62})">'
                f'<path d="M-54,0 q54,-66 108,-2 q-54,34 -108,2 z" fill="#8a6038" {o(5)}/>'
                f'<path d="M-10,0 q10,34 2,52" fill="none" stroke="#b9975c" stroke-width="12"/>'
                f'<ellipse cx="-18" cy="-16" rx="18" ry="8" fill="#a87a48" opacity=".7"/>'
                f'</g>' for j in range(11))
            + '</g>')
    # тёплый воздух дрожит у стены
    for i in range(6):
        ph = (t * .5 + i * .16) % 1.0
        s += SL(Z_PERED, f'<path d="M{700+i*90},{960-ph*520:.0f} q26,-40 0,-80"'
                         f' fill="none" stroke="#fff0d0" stroke-width="7"'
                         f' opacity="{.3*(1-ph):.2f}"/>')
    s += SL(Z_SRED, f'<rect x="0" y="930" width="{W}" height="150" fill="url(#pol)"/>'
            + polovicy(930))
    s += _vinetka(.44)
    return s


def tri_banki_pod_bumazhnymi_kryshkami(t):
    """План 82. Три банки под бумажными крышками: огурцы, помидоры, грузди."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#3a4450"/>'
            + kladka(0, 0, W, H, 84, "#5e564c")
            + f'<rect x="0" y="0" width="{W}" height="{H}" fill="#000000" opacity=".18"/>')
    s += SL(Z_SRED, f'<rect x="0" y="880" width="900" height="40" rx="10"'
                    f' fill="url(#dosk)" {o(8)}/>')
    banki = (("огурцы", "#7a9a4a"), ("помидоры", "#c0392b"), ("грузди", "#e8dcc0"))
    for i, (vid, col) in enumerate(banki):
        xx = 170 + i * 270
        k = A.ease(A.seg(t, .5 + i * 1.3, .6))
        s += SL(Z_SRED, f'<rect x="{xx-110}" y="430" width="220" height="450" rx="18"'
                        f' fill="url(#stekl)" opacity=".8" {o(8)}/>'
                + f'<ellipse cx="{xx}" cy="438" rx="110" ry="26" fill="#dfeef7"'
                  f' opacity=".9" {o(5)}/>')
        # бумажная крышка на резинке
        s += SL(Z_SRED, f'<path d="M{xx-120},436 q120,-54 240,0 q-120,26 -240,0 z"'
                        f' fill="url(#rush)" {o(6)}/>'
                + f'<path d="M{xx-112},452 q112,26 224,0" fill="none" stroke="#6b5a3a"'
                  f' stroke-width="9"/>')
        # содержимое подсвечивается
        s += SL(Z_PERED, f'<g opacity="{.45+.55*k:.2f}">'
                + "".join(f'<ellipse cx="{xx-50+(j%2)*100}" cy="{520+j*72}" rx="46"'
                          f' ry="{30 if vid!="огурцы" else 22}" fill="{col}" {o(4)}/>'
                          for j in range(5)) + '</g>')
        if vid == "огурцы":          # лист хрена колышется
            kol = 10 * A.w(t, 1.9)
            s += SL(Z_PERED, f'<path d="M{xx-60},700 q{60+kol:.0f},-90 {130:.0f},10'
                             f' q-70,50 -130,-10 z" fill="{ZEL}" opacity=".8" {o(4)}/>')
        if vid == "грузди":          # камень-гнёт сверху
            s += SL(Z_PERED, f'<path d="M{xx-70},520 q70,-54 140,-6 q-70,30 -140,6 z"'
                             f' fill="{KAMEN}" {o(5)}/>')
        # укроп покачивается
        for j in range(3):
            ug = 8 * A.w(t, 1.6, j * .3 + i * .2)
            s += SL(Z_PERED, f'<g transform="rotate({ug:.1f},{xx-40+j*40},760)">'
                    + f'<path d="M{xx-40+j*40},800 v-80" stroke="{ZEL2}" stroke-width="6"/>'
                    + "".join(f'<path d="M{xx-40+j*40},{730+m*16} l{-18+m*12},-14"'
                              f' stroke="{ZEL2}" stroke-width="4"/>' for m in range(3))
                    + '</g>')
        # банка бликует
        bl = .3 + .5 * abs(A.w(t, 2.1, i * .33))
        s += SL(Z_PERED, f'<path d="M{xx-80},470 q-14,200 6,380" fill="none"'
                         f' stroke="#ffffff" stroke-width="16" opacity="{bl*.4:.2f}"/>')
    s += _vinetka(.48)
    return s


def gorohovyy_sup_s_lozhkoy(t):
    """План 83. Крупно гороховый суп, ложка стоит, загорается листок-галочка."""
    s = SL(Z_DAL, kuhnya_stena(t, True, None, False, True, 101))
    s += SL(Z_SRED, teplo(430, 640, 740, 600, .5))
    s += SL(Z_SRED, stol_bok(0, 780, 840, 300, t, "#e8ddc6"))
    # тарелка супа крупно
    s += SL(Z_PERED, ten(420, 806, 300, 36, .5)
            + f'<path d="M100,700 q0,118 320,118 q320,0 320,-118 z" fill="url(#krem)" {o(8)}/>'
            + f'<ellipse cx="420" cy="700" rx="320" ry="106" fill="#e8dcc0" {o(8)}/>'
            + f'<ellipse cx="420" cy="706" rx="252" ry="78" fill="#dcae3c" {o(5)}/>'
            + f'<path d="M190,706 q230,96 460,0" fill="none" stroke="#b9873c"'
              f' stroke-width="12" opacity=".4"/>'
            + f'<ellipse cx="330" cy="672" rx="64" ry="18" fill="#ffffff" opacity=".22"/>')
    # ложка стоит и чуть качается
    kach = 2.2 * A.w(t, 1.5)
    s += SL(Z_PERED, f'<g transform="rotate({kach:.1f},420,700)">'
            + f'<path d="M420,700 v-300" stroke="{ZHELEZ}" stroke-width="22"'
              f' stroke-linecap="round"/>'
            + f'<ellipse cx="420" cy="712" rx="58" ry="36" fill="{ZHELEZ}" {o(5)}/>'
            + f'<path d="M406,410 q20,-16 32,2" fill="none" stroke="#e8ecee"'
              f' stroke-width="9"/></g>')
    s += SL(Z_PERED, par(420, 610, t, 6, .5, 230, .42, 1.3))
    # листок-галочка загорается
    k = A.out(A.seg(t, 2.6, .7))
    if k > 0:
        s += SL(Z_PERED, f'<g opacity="{k:.2f}" transform="translate(700,330)'
                f' scale({.6+.4*k:.2f})">'
                + f'<circle cx="0" cy="0" r="86" fill="#2f5e34" opacity=".9" {o(6)}/>'
                + f'<path d="M-40,4 l30,34 l56,-70" fill="none" stroke="#eaf6e2"'
                  f' stroke-width="16" stroke-linecap="round"/>'
                + f'<path d="M62,-54 q40,-44 70,-6 q-40,36 -70,6 z" fill="{ZEL2}" {o(4)}/>'
                + '</g>')
    s += _vinetka(.44)
    return s


def chugunok_na_uhvate(t):
    """План 84. Ухват вынимает чугунок из зева печи, каша с корочкой."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="{PECH2}"/>')
    s += SL(Z_SRED, pech_russkaya(560, 60, 1300, 1000, t, True, .0))
    s += SL(Z_SRED, teplo(1200, 660, 760, 520, .6))
    # жар дрожит в зеве
    for i in range(7):
        ph = (t * .8 + i * .14) % 1.0
        s += SL(Z_PERED, f'<path d="M{1020+i*70},{700-ph*180:.0f} q22,-40 0,-70"'
                         f' fill="none" stroke="{ORA}" stroke-width="8"'
                         f' opacity="{.4*(1-ph):.2f}"/>')
    # ухват вынимает чугунок
    k = A.ease(A.seg(t, .3, 2.2))
    cx = 1200 - 620 * k
    s += SL(Z_PERED, f'<path d="M{cx+300:.0f},760 L1900,900" {o(22)} fill="none"/>'
            + f'<path d="M{cx+150:.0f},700 q{80:.0f},-60 {160:.0f},0" fill="none" {o(18)}/>')
    s += SL(Z_PERED, gorshok(cx, 800, 2.6, t, "url(#chug)", False))
    # каша с коричневой корочкой под приподнятой крышкой
    s += SL(Z_PERED, f'<ellipse cx="{cx:.0f}" cy="{530:.0f}" rx="118" ry="30"'
                     f' fill="#c08a3e" {o(5)}/>'
            + "".join(f'<path d="M{cx-80+j*40:.0f},524 q20,-16 40,2" fill="none"'
                      f' stroke="#8a5a2c" stroke-width="7" opacity=".8"/>' for j in range(4)))
    s += SL(Z_PERED, par(cx, 480, t, 6, .55, 240, .4, 1.3))
    # листок-галочка над чугунком
    kg = A.out(A.seg(t, 1.9, .7))
    if kg > 0:
        s += SL(Z_PERED, f'<g opacity="{kg:.2f}" transform="translate({cx:.0f},320)'
                f' scale({.6+.4*kg:.2f})">'
                + f'<circle cx="0" cy="0" r="78" fill="#2f5e34" opacity=".9" {o(6)}/>'
                + f'<path d="M-36,4 l28,30 l50,-64" fill="none" stroke="#eaf6e2"'
                  f' stroke-width="15" stroke-linecap="round"/></g>')
    s += _vinetka(.48)
    return s


def kisel_i_pirog_s_kapustoy(t):
    """План 85. Гранёный стакан киселя и ломоть пирога, два листка-галочки."""
    s = SL(Z_DAL, kuhnya_stena(t, True, None, False, True, 103))
    s += SL(Z_SRED, stol_bok(0, 760, 840, 300, t, "#e8ddc6"))
    # гранёный стакан киселя
    kach = 5 * A.w(t, 1.1)
    s += SL(Z_PERED, ten(250, 770, 110, 22, .45)
            + f'<path d="M160,740 l16,-320 h150 l16,320 z" fill="url(#stekl)"'
              f' opacity=".85" {o(7)}/>'
            + f'<path d="M172,{452+kach*.3:.0f} h146 l12,286 h-170 z" fill="#8e1f2c"'
              f' opacity=".9"/>'
            + f'<path d="M172,{452+kach*.3:.0f} q74,{18+kach:.0f} 146,0" fill="none"'
              f' stroke="#b9303c" stroke-width="10"/>'
            + "".join(f'<path d="M{176+j*30},424 l6,310" stroke="#ffffff"'
                      f' stroke-width="5" opacity=".25"/>' for j in range(6)))
    # ломоть пирога на блюдце
    s += SL(Z_PERED, f'<ellipse cx="620" cy="750" rx="190" ry="50" fill="url(#krem)" {o(6)}/>'
            + f'<path d="M470,730 l230,-130 l90,66 l-150,128 z" fill="url(#solom)" {o(7)}/>'
            + f'<path d="M500,712 l210,-118" stroke="#c08a3e" stroke-width="10" opacity=".8"/>'
            + f'<path d="M700,600 l90,66 l-28,22 l-84,-62 z" fill="{ZEL2}" opacity=".9" {o(4)}/>')
    s += SL(Z_PERED, par(640, 600, t, 5, .5, 200, .45, 1.1))
    # два листка-галочки
    for i, (xx, t0) in enumerate(((250, 1.5), (640, 2.1))):
        k = A.out(A.seg(t, t0, .6))
        if k <= 0:
            continue
        s += SL(Z_PERED, f'<g opacity="{k:.2f}" transform="translate({xx},300)'
                f' scale({.5+.4*k:.2f})">'
                + f'<circle cx="0" cy="0" r="74" fill="#2f5e34" opacity=".9" {o(6)}/>'
                + f'<path d="M-34,4 l26,28 l48,-60" fill="none" stroke="#eaf6e2"'
                  f' stroke-width="14" stroke-linecap="round"/></g>')
    s += _vinetka(.44)
    return s


def tri_obeda_na_podnose(t):
    """План 86. Расписной поднос, три тарелки с каёмкой встают по словам."""
    s = SL(Z_DAL, kuhnya_stena(t, True, None, False, True, 107))
    s += SL(Z_SRED, stol_bok(0, 800, 840, 280, t))
    # расписной поднос
    zvon = 3 * A.w(t, 2.8)
    s += SL(Z_SRED, f'<g transform="translate(0,{zvon:.1f})">'
            + ten(420, 790, 360, 34, .5)
            + f'<rect x="60" y="600" width="730" height="180" rx="30"'
              f' fill="#2a2a32" {o(8)}/>'
            + f'<rect x="84" y="620" width="682" height="140" rx="22"'
              f' fill="#3a3a46" {o(4)}/>'
            + "".join(f'<circle cx="{150+j*120}" cy="{660+(j%2)*60}" r="26"'
                      f' fill="{["#c0392b","#d9a441","#e8e2d4"][j%3]}" opacity=".9" {o(3)}/>'
                      for j in range(6))
            + '</g>')
    bluda = (("#d49a52", "картошка с грибами"), ("#e8d6b0", "фасоль с луком"),
             ("#e0b84a", "каша с тыквой"))
    for i, (col, _) in enumerate(bluda):
        k = A.over(A.seg(t, .5 + i * 1.5, .4))
        if k <= 0:
            continue
        kk = min(1.0, k)
        xx = 200 + i * 230
        s += SL(Z_PERED, f'<g opacity="{kk:.2f}" transform="translate(0,{-50*(1-kk):.0f})">'
                + tarelka(xx, 660 + zvon, 108, t)
                + f'<ellipse cx="{xx}" cy="{644+zvon:.0f}" rx="74" ry="26"'
                  f' fill="{col}" {o(4)}/>'
                + f'<ellipse cx="{xx}" cy="{660+zvon:.0f}" rx="104" ry="36" fill="none"'
                  f' stroke="{TKAN}" stroke-width="6" opacity=".8"/>'
                + (f'<ellipse cx="{xx+26}" cy="{636+zvon:.0f}" rx="28" ry="16"'
                   f' fill="#e07a2c" {o(3)}/>' if i == 2 else "")
                + par(xx, 600, t, 4, .45 * kk, 180, .45, .9) + '</g>')
    s += _vinetka(.44)
    return s


def shkolnica_za_kuhonnym_stolom(t):
    """План 87. Девочка с косичками ест, болтая ногами; портфель у стула."""
    s = SL(Z_DAL, kuhnya_stena(t, True, 1400, False, True, 109))
    s += SL(Z_SRED, teplo(700, 620, 860, 600, .5))
    # стул и портфель
    s += SL(Z_SRED, f'<rect x="700" y="820" width="220" height="30" rx="8"'
                    f' fill="url(#derev)" {o(7)}/>'
            + f'<rect x="700" y="520" width="28" height="300" rx="9"'
              f' fill="url(#derev)" {o(6)}/>'
            + f'<rect x="892" y="520" width="28" height="300" rx="9"'
              f' fill="url(#derev)" {o(6)}/>')
    s += SL(Z_PERED, f'<rect x="980" y="900" width="230" height="170" rx="16"'
                     f' fill="#6b4a2c" {o(7)}/>'
            + f'<rect x="1000" y="880" width="190" height="60" rx="12"'
              f' fill="#7a5a36" {o(6)}/>'
            + f'<rect x="1070" y="930" width="50" height="34" rx="8"'
              f' fill="url(#zol)" {o(5)}/>')
    # девочка: форма, фартук, косички качаются
    ug = 7 * A.w(t, 1.6)
    s += SL(Z_SRED, babka(810, 830, 520, t, True, "#8a2f3a", .4, -14, "#fdfaf2"))
    for sgn in (-1, 1):
        s += SL(Z_PERED, f'<g transform="rotate({ug*sgn:.1f},{810+sgn*54},560)">'
                + f'<path d="M{810+sgn*54},560 q{sgn*40},70 {sgn*20},140"'
                  f' fill="none" stroke="#6b4a2c" stroke-width="22"/>'
                + f'<path d="M{810+sgn*74},700 q{sgn*16},14 {sgn*4},30" fill="none"'
                  f' stroke="{TKAN}" stroke-width="12"/></g>')
    # ноги болтаются
    bolt = 16 * A.w(t, 1.1)
    for sgn in (-1, 1):
        s += SL(Z_PERED, f'<path d="M{810+sgn*40},860 q{sgn*20},90 {bolt*sgn:.0f},160"'
                         f' fill="none" stroke="#3f4a5c" stroke-width="30"'
                         f' stroke-linecap="round"/>')
    # стол с тремя тарелками, над каждой галочка
    s += SL(Z_PERED, f'<path d="M0,{H} v-170 q420,-60 840,-10 v180 z" fill="#e8ddc6" {o(8)}/>')
    for i in range(3):
        xx = 170 + i * 250
        s += SL(Z_PERED, tarelka(xx, 960, 96, t, "url(#krem)", True, 1))
        k = A.out(A.seg(t, .4 + i * .5, .5))
        if k > 0:
            s += SL(Z_PERED, f'<g opacity="{k:.2f}" transform="translate({xx},780)'
                    f' scale({.45+.3*k:.2f})">'
                    + f'<circle cx="0" cy="0" r="74" fill="#2f5e34" opacity=".9" {o(6)}/>'
                    + f'<path d="M-34,4 l26,28 l48,-60" fill="none" stroke="#eaf6e2"'
                      f' stroke-width="14" stroke-linecap="round"/></g>')
    s += _vinetka(.44)
    return s


def meshochek_sushki_i_banka_varenya(t):
    """План 88. Сушка сыплется в кастрюлю, вода темнеет; банка варенья."""
    s = SL(Z_DAL, kuhnya_stena(t, True, None, False, True, 113))
    s += SL(Z_SRED, f'<rect x="0" y="760" width="860" height="320" rx="14"'
                    f' fill="url(#zhel)" {o(8)}/>')
    # кастрюля, вода темнеет в компот
    tem = A.seg(t, .8, 2.4)
    s += SL(Z_SRED, f'<path d="M140,760 q-26,-200 210,-200 q236,0 210,200 z"'
                    f' fill="#e9eef0" {o(8)}/>')
    s += SL(Z_SRED, f'<ellipse cx="350" cy="568" rx="212" ry="48"'
                    f' fill="#cfe0ea" {o(6)}/>'
            + f'<ellipse cx="350" cy="568" rx="206" ry="44" fill="#8a4a24"'
              f' opacity="{tem:.2f}"/>')
    # мешочек, сушка сыплется
    s += SL(Z_PERED, f'<path d="M520,420 q-16,-230 130,-240 q150,10 130,240 z"'
                     f' fill="url(#rush)" {o(8)}'
                     f' transform="rotate(26,650,300)"/>')
    for i in range(8):
        ph = (t * .8 + i * .12) % 1.0
        xx = 520 - 120 * ph + 20 * math.sin(i * 2)
        yy = 420 + ph * 150
        col = "#c9975a" if i % 2 else "#a8824a"
        s += SL(Z_PERED, f'<ellipse cx="{xx:.0f}" cy="{yy:.0f}" rx="21" ry="14"'
                         f' fill="{col}" {o(3)} opacity="{1-ph*.2:.2f}"/>')
    s += SL(Z_PERED, par(350, 520, t, 5, .45, 210, .45, 1.1))
    # банка варенья: резинка щёлкает, бумажку снимают
    sn = A.ease(A.seg(t, 2.8, .8))
    s += SL(Z_PERED, f'<rect x="1020" y="620" width="260" height="380" rx="18"'
                     f' fill="url(#stekl)" opacity=".85" {o(8)}/>'
            + f'<ellipse cx="1150" cy="636" rx="130" ry="30" fill="#8e1f2c" {o(5)}/>'
            + f'<rect x="1040" y="700" width="220" height="290" rx="10"'
              f' fill="#8e1f2c" opacity=".9"/>')
    s += SL(Z_PERED, f'<g transform="translate({240*sn:.0f},{-180*sn:.0f})'
            f' rotate({30*sn:.0f},1150,600)" opacity="{1-sn*.2:.2f}">'
            + f'<path d="M1030,612 q120,-58 240,0 q-120,28 -240,0 z" fill="url(#rush)" {o(6)}/>'
            + f'<path d="M1038,628 q112,26 224,0" fill="none" stroke="#6b5a3a"'
              f' stroke-width="9"/></g>')
    s += _vinetka(.44)
    return s


def oreh_v_dvernoy_scheli(t):
    """План 89. Орех в щели у петель, дверь прижимают, мамин палец грозит."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#6b5a42"/>'
            + doski(0, 0, 760, H, 150, True, "derev")
            + f'<rect x="760" y="0" width="{W-760}" height="{H}" fill="#c9bda4"/>')
    # косяк и дверь у петель
    s += SL(Z_SRED, f'<rect x="700" y="0" width="120" height="{H}" fill="url(#dosk)" {o(9)}/>')
    prizh = A.ease(A.seg(t, .5, .8))
    s += SL(Z_SRED, f'<g transform="translate({-90*(1-prizh):.0f},0)">'
            + f'<rect x="300" y="0" width="420" height="{H}" fill="#8a6a46" {o(9)}/>'
            + f'<rect x="340" y="120" width="340" height="380" rx="10"'
              f' fill="#7a5a3a" {o(6)}/>'
            + f'<rect x="340" y="560" width="340" height="400" rx="10"'
              f' fill="#7a5a3a" {o(6)}/></g>')
    for yy in (260, 640, 940):
        s += SL(Z_SRED, f'<rect x="690" y="{yy}" width="140" height="56" rx="10"'
                        f' fill="{ZHELEZ}" {o(6)}/>'
                + f'<circle cx="760" cy="{yy+28}" r="16" fill="#3c4047" {o(4)}/>')
    # орех в щели и хруст
    hrust = A.seg(t, 1.1, .3)
    if hrust < 1:
        s += SL(Z_PERED, f'<circle cx="770" cy="520" r="46" fill="#a07b4e" {o(6)}/>'
                + f'<path d="M740,490 q30,60 60,0" fill="none" stroke="#7a5a34"'
                  f' stroke-width="7"/>')
    else:
        # скорлупа разлетается
        for i in range(7):
            ph = min(1.0, (t - 1.4) * 1.2 + i * .05)
            if ph <= 0:
                continue
            a = i * .9
            s += SL(Z_PERED, f'<path d="M{770+math.cos(a)*260*ph:.0f},'
                             f'{520+math.sin(a)*200*ph-60*ph:.0f} l26,14 l-12,20 z"'
                             f' fill="#8a6a3c" opacity="{1-ph*.7:.2f}" {o(3)}/>')
        s += SL(Z_PERED, f'<circle cx="770" cy="560" r="30" fill="#e8d6a8" {o(5)}/>')
    # детская рука вкладывает орех
    k = A.ease(A.seg(t, 0, .6))
    s += SL(Z_PERED, f'<g transform="translate({-200*(1-k):.0f},0)" opacity="{1-A.seg(t,1.0,.4):.2f}">'
            + ruka(360, 560, t, 230, -6, 42, "#8a6a52") + '</g>')
    # мамина рука грозит пальцем
    km = A.out(A.seg(t, 1.5, .7))
    if km > 0:
        kach = 14 * A.w(t, .8)
        s += SL(Z_PERED, f'<g opacity="{km:.2f}" transform="translate({(1-km)*200:.0f},0)">'
                + f'<path d="M1900,700 q-200,-40 -300,-80" fill="none" stroke="#e8bb93"'
                  f' stroke-width="62" stroke-linecap="round"/>'
                + f'<g transform="rotate({kach:.0f},1600,620)">'
                + f'<path d="M1600,620 q-30,-90 -10,-170" fill="none" stroke="#e8bb93"'
                  f' stroke-width="40" stroke-linecap="round"/></g></g>')
    s += _vinetka(.5)
    return s


def detskaya_tarelka_s_nadpisyu_na_dne(t):
    """План 90. Доеденная детская тарелка, на дне проступают слова."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#e8ddc6"/>'
            + "".join(f'<path d="M{-40+j*110},0 v{H}" stroke="#b9553f"'
                      f' stroke-width="7" opacity=".4"/>' for j in range(19))
            + "".join(f'<path d="M0,{-20+j*110} h{W}" stroke="#b9553f"'
                      f' stroke-width="7" opacity=".3"/>' for j in range(11)))
    s += SL(Z_SRED, teplo(900, 540, 1000, 700, .4))
    # тарелка сверху
    s += SL(Z_PERED, ten(860, 700, 420, 50, .45)
            + f'<circle cx="860" cy="560" r="400" fill="url(#krem)" {o(10)}/>'
            + f'<circle cx="860" cy="560" r="330" fill="#f2ead6" {o(6)}/>'
            + f'<circle cx="860" cy="560" r="300" fill="none" stroke="{TKAN}"'
              f' stroke-width="10" opacity=".7"/>')
    # надпись проступает на дне
    k = A.seg(t, 1.0, 2.2)
    if k > 0:
        s += SL(Z_PERED, f'<g opacity="{min(1,k*1.2):.2f}">'
                + f'<text x="860" y="546" font-family="Georgia,serif" font-size="78"'
                  f' text-anchor="middle" fill="#6b5a3a">бабушкин</text>'
                + f'<text x="860" y="648" font-family="Georgia,serif" font-size="78"'
                  f' text-anchor="middle" fill="#6b5a3a">устав</text></g>')
    # ложка облизана, бликует
    bl = .35 + .65 * abs(A.w(t, 1.8))
    s += SL(Z_PERED, f'<g transform="rotate(-22,1520,760)">'
            + f'<path d="M1520,760 l300,-120" stroke="{ZHELEZ}" stroke-width="30"'
              f' stroke-linecap="round"/>'
            + f'<ellipse cx="1480" cy="780" rx="110" ry="70" fill="{ZHELEZ}" {o(7)}/>'
            + f'<ellipse cx="1450" cy="760" rx="44" ry="22" fill="#ffffff"'
              f' opacity="{.25+.4*bl:.2f}"/></g>')
    # капля компота на клеёнке
    s += SL(Z_PERED, f'<ellipse cx="360" cy="920" rx="54" ry="30" fill="#8a4a24"'
                     f' opacity=".75"/>'
            + f'<ellipse cx="344" cy="910" rx="16" ry="8" fill="#ffffff" opacity=".3"/>')
    s += _vinetka(.46)
    return s


def pogreb_s_fonarem(t):
    """План 91. Погреб: лестница, фонарь, полки с банками, рука с банкой."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#1c1a18"/>'
            + kladka(0, 0, W, H, 80, "#4a443c")
            + f'<rect x="0" y="0" width="{W}" height="{H}" fill="#000000" opacity=".35"/>')
    # лестница вниз слева
    for i in range(7):
        s += SL(Z_SRED, f'<path d="M{40+i*26},{120+i*140} h220 l-26,46 h-220 z"'
                        f' fill="url(#derev)" {o(7)}/>')
    # полки с банками до потолка (в левой полосе — справа окно вставки)
    for r_ in range(4):
        yy = 320 + r_ * 200
        s += SL(Z_SRED, f'<rect x="300" y="{yy}" width="520" height="26" rx="7"'
                        f' fill="url(#dosk)" {o(6)}/>')
        for c_ in range(4):
            xx = 360 + c_ * 130
            bl = .25 + .4 * abs(A.w(t, 2.3, (r_ * 4 + c_) * .11))
            s += SL(Z_SRED, f'<rect x="{xx-44}" y="{yy-130}" width="88" height="130"'
                            f' rx="10" fill="url(#stekl)" opacity=".7" {o(5)}/>'
                    + f'<rect x="{xx-44}" y="{yy-144}" width="88" height="20" rx="6"'
                      f' fill="#cfe0ea" {o(4)}/>'
                    + f'<ellipse cx="{xx}" cy="{yy-66}" rx="30" ry="42"'
                      f' fill="{["#7a9a4a","#c0392b","#e8dcc0","#8e1f2c"][(r_+c_)%4]}"'
                      f' opacity=".9"/>'
                    + f'<path d="M{xx-34},{yy-120} v100" stroke="#ffffff"'
                      f' stroke-width="8" opacity="{bl:.2f}"/>')
    # фонарь качается
    ang = 6 * A.w(t, 2.0)
    s += SL(Z_SRED, f'<g transform="rotate({ang:.1f},700,80)">'
            + f'<path d="M700,80 v150" {o(6)} fill="none"/>'
            + f'<rect x="640" y="230" width="120" height="150" rx="12"'
              f' fill="{ZHELEZ}" {o(7)}/>'
            + f'<rect x="658" y="248" width="84" height="114" rx="8" fill="{SVET}"'
              f' opacity=".95"/>'
            + teplo(700, 310, 520, 460, .6) + '</g>')
    # рука снимает банку и открывает: чпок
    k = A.ease(A.seg(t, 1.4, 1.6))
    chpok = A.out(A.seg(t, 3.2, .3))
    s += SL(Z_PERED, f'<g transform="translate({-180*k:.0f},{200*k:.0f})">'
            + ruka(140, 760, t, 250, -12, 52, "#5e5468")
            + f'<rect x="440" y="700" width="160" height="230" rx="14"'
              f' fill="url(#stekl)" opacity=".8" {o(7)}/>'
            + f'<ellipse cx="520" cy="820" rx="60" ry="76" fill="#7a9a4a" opacity=".9"/>'
            + f'<g transform="translate(0,{-60*chpok:.0f}) rotate({20*chpok:.0f},520,700)">'
            + f'<rect x="430" y="676" width="180" height="34" rx="10"'
              f' fill="#cfe0ea" {o(5)}/></g></g>')
    # пар изо рта на холоде
    s += SL(Z_PERED, par(260, 640, t, 4, .35, 180, .3, 1.4))
    s += _vinetka(.56)
    return s


def krytyy_rynok(t):
    """Планы 92-93. Крышка погреба откидывается — за ней крытый рынок."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#c6cfd2"/>')
    # высокая крыша фермами
    for i in range(6):
        xx = 60 + i * 380
        s += SL(Z_DAL, f'<path d="M{xx},300 l180,-180 l180,180" fill="none"'
                       f' stroke="#8d939c" stroke-width="14"/>'
                + f'<path d="M{xx},300 h360" stroke="#8d939c" stroke-width="10"/>'
                + "".join(f'<path d="M{xx+40+j*60},300 l{60-j*10},-{60+j*20}"'
                          f' stroke="#9aa3a8" stroke-width="7"/>' for j in range(5)))
    s += SL(Z_DAL, f'<rect x="0" y="300" width="{W}" height="40" fill="#b9c4c0" {o(0)}/>')
    # ряды прилавков под крышей
    for i in range(3):
        yy = 560 + i * 150
        s += SL(Z_SRED, f'<rect x="{200-i*100}" y="{yy}" width="{1500+i*200}"'
                        f' height="{40+i*10}" rx="8" fill="#cfd8d6" {o(6)}'
                        f' opacity="{.6+i*.15:.2f}"/>')
        for c_ in range(6):
            xx = 300 - i * 90 + c_ * 260
            s += SL(Z_SRED, f'<path d="M{xx-60},{yy} q-10,-70 60,-70 q70,0 60,70 z"'
                            f' fill="{["#c0392b","#d9a441","#5e8a3a"][c_%3]}"'
                            f' opacity="{.5+i*.15:.2f}" {o(4)}/>')
    # гирлянды лука качаются
    for i in range(5):
        ang = 5 * A.w(t, 2.2, i * .2)
        xx = 240 + i * 360
        s += SL(Z_PERED, f'<g transform="rotate({ang:.1f},{xx},340)">'
                + f'<path d="M{xx},340 v120" {o(6)} fill="none"/>'
                + "".join(f'<circle cx="{xx+(28 if j%2 else -28)}" cy="{470+j*52}"'
                          f' r="30" fill="url(#solom)" {o(5)}/>' for j in range(4))
                + '</g>')
    # голуби под крышей
    for i in range(4):
        ph = (t * .22 + i * .25) % 1.0
        xx = 200 + ph * 1500
        yy = 220 + 40 * math.sin(ph * 6 + i)
        kr = 26 * A.w(t, .5, i * .3)
        s += SL(Z_PERED, f'<ellipse cx="{xx:.0f}" cy="{yy:.0f}" rx="42" ry="24"'
                         f' fill="#8d939c" {o(4)}/>'
                + f'<circle cx="{xx+36:.0f}" cy="{yy-14:.0f}" r="18" fill="#9aa3a8" {o(4)}/>'
                + f'<path d="M{xx+50:.0f},{yy-12:.0f} l16,6 l-16,6 z" fill="{MED}"/>'
                + f'<path d="M{xx-6:.0f},{yy-6:.0f} q26,-{40+kr:.0f} 56,-6" fill="none"'
                  f' stroke="#b9c0c6" stroke-width="12"/>'
                + f'<path d="M{xx-44:.0f},{yy+4:.0f} l-22,10 l22,8 z" fill="#8d939c"/>')
    # крышка погреба откидывается в нижней части кадра
    k = A.ease(A.seg(t, .2, 1.2))
    s += SL(Z_PERED, f'<g transform="rotate({-70*k:.0f},300,1000)">'
            + f'<rect x="300" y="960" width="620" height="60" rx="10"'
              f' fill="url(#dosk)" {o(8)}/>'
            + f'<rect x="560" y="930" width="110" height="34" rx="10"'
              f' fill="{ZHELEZ}" {o(5)}/></g>')
    s += SL(Z_PERED, f'<path d="M300,1000 h620 v80 h-620 z" fill="#1c1a18" {o(7)}/>')
    s += _vinetka(.44)
    return s


# ═══════════════ БЛОК 6. КОМУ ПОСТ СМЯГЧАЛИ ═══════════════
def pervyy_prilavok_u_vhoda(t):
    """План 94. Прилавок с постным: кадушка капусты, грибы, мёд, фасоль."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#b9c4c6"/>'
            + f'<rect x="0" y="0" width="{W}" height="300" fill="#a3aeb0"/>'
            + "".join(f'<path d="M{60+i*300},300 l140,-150 l140,150" fill="none"'
                      f' stroke="#8d939c" stroke-width="12"/>' for i in range(3)))
    s += SL(Z_SRED, f'<rect x="0" y="700" width="860" height="60" rx="10"'
                    f' fill="#cfd8d6" {o(8)}/>'
            + f'<rect x="0" y="760" width="860" height="320" fill="#9aa8a4" {o(7)}/>')
    # кадушка капусты
    s += SL(Z_SRED, f'<path d="M60,700 q-16,-230 150,-230 q166,0 150,230 z"'
                    f' fill="url(#derev)" {o(8)}/>'
            + f'<ellipse cx="210" cy="474" rx="152" ry="36" fill="#9ab07e" {o(6)}/>'
            + f'<path d="M70,560 h280" stroke="{ZHELEZ}" stroke-width="14" opacity=".9"/>')
    # черпак с рассолом
    kap = (t * .9) % 1.0
    s += SL(Z_PERED, f'<g transform="rotate(-24,300,400)">'
            + f'<path d="M300,400 l170,-120" stroke="{ZHELEZ}" stroke-width="14"/>'
            + f'<ellipse cx="288" cy="412" rx="62" ry="40" fill="{ZHELEZ}" {o(5)}/></g>'
            + f'<ellipse cx="282" cy="{452+kap*120:.0f}" rx="{9-3*kap:.0f}"'
              f' ry="{14-4*kap:.0f}" fill="#e2eecb" opacity="{.9*(1-kap*.4):.2f}"/>')
    # связки грибов и банки мёда
    for i in range(2):
        s += SL(Z_SRED, f'<g transform="rotate({4*A.w(t,2.2,i*.3):.1f},{470+i*90},300)">'
                + f'<path d="M{470+i*90},300 v240" stroke="#7a6a52" stroke-width="6"/>'
                + "".join(f'<path d="M{440+i*90+(20 if j%2 else 0)},{340+j*52}'
                          f' q30,-34 60,-2 q-30,20 -60,2 z" fill="#8a6038" {o(4)}/>'
                          for j in range(4)) + '</g>')
    for i in range(3):
        s += SL(Z_SRED, f'<rect x="{620+i*76}" y="580" width="62" height="120" rx="10"'
                        f' fill="url(#stekl)" opacity=".8" {o(5)}/>'
                + f'<ellipse cx="{651+i*76}" cy="640" rx="24" ry="40" fill="{MED}" opacity=".9"/>')
    # мешок фасоли
    s += SL(Z_SRED, f'<path d="M740,760 q-10,-180 110,-180 q120,0 110,180 z"'
                    f' fill="url(#solom)" {o(7)}/>')
    # весы и руки в митенках
    s += SL(Z_SRED, f'<rect x="400" y="600" width="200" height="100" rx="10"'
                    f' fill="#e8ece8" {o(7)}/>'
            + f'<circle cx="500" cy="640" r="52" fill="#fdfdf8" {o(6)}/>')
    ang = -50 + 30 * A.w(t, 2.0)
    s += SL(Z_PERED, f'<g transform="rotate({ang:.1f},500,640)">'
            + f'<path d="M500,640 v-40" stroke="{KRAS}" stroke-width="7"/></g>')
    s += SL(Z_PERED, ruka(620, 420, t, 240, 150, 52, "#8a6a52"))
    s += SL(Z_PERED, par(560, 360, t, 4, .35, 170, .3, 1.3))
    s += _vinetka(.44)
    return s


def kuhonnyy_shkafchik_s_zapasom(t):
    """План 95. Шкафчик в шесть полок: крупа, фасоль, орехи, мёд, грибы."""
    s = SL(Z_DAL, kuhnya_stena(t, True, None, False, False))
    s += SL(Z_SRED, f'<rect x="300" y="80" width="1100" height="960" rx="18"'
                    f' fill="url(#dosk)" {o(9)}/>'
            + f'<rect x="340" y="120" width="1020" height="880" rx="12"'
              f' fill="#b08456" {o(5)}/>')
    for i in range(6):
        yy = 190 + i * 145
        s += SL(Z_SRED, f'<rect x="340" y="{yy}" width="1020" height="18" rx="6"'
                        f' fill="url(#derev)" {o(5)}/>')
        for c_ in range(4):
            xx = 440 + c_ * 240
            vid = (i + c_) % 4
            if vid == 0:
                s += SL(Z_SRED, f'<rect x="{xx-50}" y="{yy-108}" width="100" height="108"'
                                f' rx="10" fill="url(#stekl)" opacity=".8" {o(5)}/>'
                        + f'<rect x="{xx-50}" y="{yy-44}" width="100" height="44"'
                          f' fill="#d9bd86" opacity=".9"/>')
            elif vid == 1:
                s += SL(Z_SRED, f'<path d="M{xx-54},{yy} q-6,-96 54,-96 q60,0 54,96 z"'
                                f' fill="url(#solom)" {o(5)}/>')
            elif vid == 2:
                s += SL(Z_SRED, f'<path d="M{xx-46},{yy} q-6,-80 46,-80 q52,0 46,80 z"'
                                f' fill="url(#glina)" {o(5)}/>'
                        + "".join(f'<circle cx="{xx-26+j*26}" cy="{yy-58}" r="15"'
                                  f' fill="#a07b4e" {o(3)}/>' for j in range(3)))
            else:
                s += SL(Z_SRED, f'<path d="M{xx-40},{yy} q-4,-90 40,-90 q44,0 40,90 z"'
                                f' fill="url(#med)" {o(5)}/>')
    # крупа пересыпается в банке
    per = (t * .6) % 1.0
    s += SL(Z_PERED, f'<rect x="390" y="{112+per*20:.0f}" width="100" height="{70-per*20:.0f}"'
                     f' fill="#d9bd86" opacity=".9"/>')
    # связка грибов на крючке качается
    ang = 5 * A.w(t, 2.1)
    s += SL(Z_PERED, f'<g transform="rotate({ang:.1f},1300,140)">'
            + f'<path d="M1300,140 v300" stroke="#7a6a52" stroke-width="7"/>'
            + "".join(f'<path d="M{1270+(20 if j%2 else 0)},{190+j*58} q30,-36 60,-2'
                      f' q-30,22 -60,2 z" fill="#8a6038" {o(4)}/>' for j in range(5))
            + '</g>')
    # дверца закрывается
    zak = A.ease(A.seg(t, 2.8, 1.2))
    s += SL(Z_PERED, f'<g transform="translate({-1060*(1-zak):.0f},0)" opacity="{zak:.2f}">'
            + f'<rect x="300" y="80" width="1100" height="960" rx="18"'
              f' fill="#ba8c5c" {o(9)}/>'
            + f'<rect x="360" y="140" width="980" height="840" rx="12" fill="#a87c4e" {o(5)}/>'
            + f'<circle cx="1330" cy="560" r="18" fill="{MED}" {o(5)}/></g>')
    s += _vinetka(.44)
    return s


def korotkiy_chek_i_sdacha(t):
    """План 96. Короткий чек на клеёнке, в блюдце падает сдача."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#e8ddc6"/>'
            + "".join(f'<path d="M{-40+j*120},0 v{H}" stroke="#7a9a6a"'
                      f' stroke-width="8" opacity=".35"/>' for j in range(18))
            + "".join(f'<path d="M0,{-20+j*120} h{W}" stroke="#7a9a6a"'
                      f' stroke-width="8" opacity=".3"/>' for j in range(10)))
    s += SL(Z_SRED, teplo(860, 560, 980, 680, .4))
    # чек шевелится от сквозняка
    sh = 8 * A.w(t, 1.7)
    s += SL(Z_PERED, ten(520, 700, 150, 22, .35)
            + f'<path d="M380,300 h280 q{sh:.0f},180 0,380 h-280 q-{sh:.0f},-180 0,-380 z"'
              f' fill="#fdfaf2" {o(6)}/>'
            + "".join(f'<path d="M410,{350+j*56} h{150+j*20}" stroke="#b9b2a2"'
                      f' stroke-width="9" opacity=".8"/>' for j in range(5))
            + f'<path d="M380,680 l40,22 l40,-22 l40,22 l40,-22 l40,22 l40,-22 l40,22"'
              f' fill="none" stroke="#b9b2a2" stroke-width="7"/>')
    # блюдце и падающая сдача
    s += SL(Z_PERED, f'<ellipse cx="1180" cy="760" rx="220" ry="70" fill="url(#krem)" {o(7)}/>'
            + f'<ellipse cx="1180" cy="748" rx="170" ry="50" fill="#f2ead6" {o(4)}/>')
    for i in range(4):
        k = A.seg(t, .5 + i * .45, .5)
        if k <= 0:
            continue
        yy = 300 + k * 420
        s += SL(Z_PERED, f'<ellipse cx="{1120+i*44}" cy="{min(yy,744):.0f}" rx="32"'
                         f' ry="{32 if k<1 else 10}" fill="url(#zol)" {o(5)}/>')
        if k >= 1:
            s += SL(Z_PERED, f'<ellipse cx="{1120+i*44}" cy="744" rx="34" ry="11"'
                             f' fill="none" stroke="{MED}" stroke-width="5" opacity=".8"/>')
    # ладонь ложится рядом
    kl = A.ease(A.seg(t, 2.4, 1.0))
    s += SL(Z_PERED, f'<g opacity="{kl:.2f}" transform="translate(0,{80*(1-kl):.0f})">'
            + ruka(700, 940, t, 260, -22, 60, "#6b5a6e") + '</g>')
    s += _vinetka(.44)
    return s


def schety_na_podokonnike(t):
    """Планы 97, 114. Счёты: палец сдвигает две костяшки и замирает."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#cfd8dd"/>'
            + f'<rect x="760" y="60" width="1060" height="640" rx="12"'
              f' fill="url(#nden)" {o(10)}/>'
            + f'<path d="M1290,60 v640 M760,380 h1060" {o(8)} fill="none"/>'
            + sneg_letit(t, 22, 43, .55, .7))
    s += SL(Z_SRED, f'<rect x="0" y="700" width="{W}" height="70" rx="10"'
                    f' fill="url(#dosk)" {o(8)}/>')
    # счёты крупно
    s += SL(Z_PERED, ten(560, 712, 380, 26, .45)
            + f'<rect x="180" y="300" width="800" height="400" rx="16"'
              f' fill="url(#derev)" {o(9)}/>'
            + f'<rect x="220" y="340" width="720" height="320" rx="10"'
              f' fill="#7a5a36" {o(5)}/>')
    for r_ in range(5):
        yy = 380 + r_ * 66
        s += SL(Z_PERED, f'<path d="M220,{yy} h720" stroke="{ZHELEZ}" stroke-width="7"/>')
        for c_ in range(9):
            sdvinuta = r_ == 2 and c_ < 2
            k = A.ease(A.seg(t, .6 + c_ * .3, .4)) if sdvinuta else 0
            xx = 250 + c_ * 56 + (300 * k if sdvinuta else 0)
            s += SL(Z_PERED, f'<ellipse cx="{xx:.0f}" cy="{yy}" rx="24" ry="17"'
                             f' fill="{"#d9a441" if sdvinuta else "#3a2f22"}" {o(4)}/>')
    # палец замирает
    kp = A.ease(A.seg(t, .4, 1.2))
    s += SL(Z_PERED, f'<g transform="translate({300*kp:.0f},0)">'
            + ruka(60, 480, t, 240, 6, 50, "#6b5a6e") + '</g>')
    s += _vinetka(.46)
    return s


def meshok_kochan_i_kulek(t):
    """План 98. Мешок картошки, кочан, кулёк гороха; растёт стопка тарелок."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#9a8a6c"/>'
            + doski(0, 0, W, 700, 160, False, "derev")
            + f'<rect x="0" y="700" width="{W}" height="380" fill="url(#pol)"/>'
            + polovicy(700))
    veshi = [
        (280, lambda k: f'<path d="M150,980 q-30,-{300*k:.0f} 130,-{310*k:.0f}'
                        f' q160,{10*k:.0f} 130,{310*k:.0f} z" fill="url(#solom)" {o(8)}/>'
                        + "".join(f'<path d="M{170+j*44},980 v-{240*k:.0f}"'
                                  f' stroke="#c89a4e" stroke-width="7"'
                                  f' opacity=".5"/>' for j in range(5))
                        + f'<path d="M190,{676-16*k:.0f} q90,-46 180,0'
                          f' q-50,40 -90,40 q-40,0 -90,-40 z" fill="#c89a4e" {o(7)}/>'
                        + "".join(f'<ellipse cx="{232+j*46}" cy="{706+(j%2)*22}" rx="30"'
                                  f' ry="23" fill="#c9a86a" {o(4)}/>' for j in range(3))),
        (640, lambda k: f'<circle cx="640" cy="{870-26*k:.0f}" r="{150*k:.0f}"'
                        f' fill="#e6eede" {o(8)}/>'
                        + "".join(f'<path d="M{556+j*42},{790-18*k:.0f} q44,{86*k:.0f}'
                                  f' 12,{156*k:.0f}" fill="none" stroke="#b9c9ae"'
                                  f' stroke-width="11"/>' for j in range(4))
                        + f'<path d="M520,{860-20*k:.0f} q-70,-{70*k:.0f} 10,-{120*k:.0f}'
                          f' q50,{40*k:.0f} 50,{110*k:.0f} z" fill="#9ab07e" {o(6)}/>'
                        + f'<path d="M760,{860-20*k:.0f} q70,-{70*k:.0f} -10,-{120*k:.0f}'
                          f' q-50,{40*k:.0f} -50,{110*k:.0f} z" fill="#9ab07e" {o(6)}/>'),
        (980, lambda k: f'<path d="M900,980 l20,-{260*k:.0f} h140 l20,{260*k:.0f} z"'
                        f' fill="#d8cdb4" {o(7)}/>'
                        f'<path d="M920,{720-10*k:.0f} h140" stroke="#b9ae92"'
                        f' stroke-width="8"/>'
                        + "".join(f'<circle cx="{940+j*34}" cy="{700-14*k:.0f}" r="14"'
                                  f' fill="{ZEL2}" {o(3)}/>' for j in range(3))),
    ]
    for i, (xx, f) in enumerate(veshi):
        k = A.ease(A.seg(t, .4 + i * .8, .6))
        if k <= 0:
            continue
        s += SL(Z_PERED, f(k))
    # стопка чистых тарелок растёт: неделя за неделей
    n = min(6, int(A.seg(t, 1.6, 2.4) * 6.99))
    for j in range(n):
        s += SL(Z_PERED, f'<ellipse cx="1480" cy="{960-j*42}" rx="170" ry="40"'
                         f' fill="url(#krem)" {o(6)}/>'
                + f'<ellipse cx="1480" cy="{952-j*42}" rx="130" ry="28"'
                  f' fill="#f2ead6" opacity=".9"/>')
    s += _vinetka(.44)
    return s


def komnata_s_nochnikom(t):
    """План 99. Смена главы: тихая комната, кресло, плед, ночник."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#2f3a4e"/>'
            + f'<rect x="0" y="0" width="{W}" height="{H}" fill="url(#holod)" opacity=".3"/>'
            + f'<rect x="1300" y="120" width="520" height="520" rx="12"'
              f' fill="url(#nnoch)" {o(9)}/>'
            + f'<path d="M1560,120 v520 M1300,380 h520" {o(7)} fill="none"/>'
            + sneg_letit(t, 16, 47, .4, .5))
    s += SL(Z_DAL, f'<rect x="0" y="820" width="{W}" height="260" fill="#2a2a32"/>')
    # тень ветки на стене
    kol = 10 * A.w(t, 3.4)
    s += SL(Z_DAL, f'<path d="M0,240 q{300+kol:.0f},120 600,40" fill="none"'
                   f' stroke="#1c2230" stroke-width="22" opacity=".55"/>'
            + "".join(f'<path d="M{120+j*120},{270+j*10} l{-40+j*10},-60"'
                      f' stroke="#1c2230" stroke-width="12" opacity=".5"/>' for j in range(5)))
    # кресло
    s += SL(Z_SRED, ten(530, 900, 260, 34, .5)
            + f'<path d="M320,840 v-300 q0,-120 210,-120 q210,0 210,120 v300 z"'
              f' fill="#4a4152" {o(8)}/>'
            + f'<path d="M360,560 q170,-70 340,0 q-170,40 -340,0 z" fill="#5e5468" {o(6)}/>'
            + f'<rect x="286" y="700" width="80" height="150" rx="26" fill="#564c62" {o(7)}/>'
            + f'<rect x="694" y="700" width="80" height="150" rx="26" fill="#564c62" {o(7)}/>'
            + f'<rect x="300" y="838" width="460" height="34" rx="12" fill="#3a3344" {o(6)}/>'
            + f'<rect x="330" y="872" width="34" height="80" rx="10" fill="#2f2a38" {o(5)}/>'
            + f'<rect x="700" y="872" width="34" height="80" rx="10" fill="#2f2a38" {o(5)}/>')
    # плед сползает с кресла
    sp = A.ease(A.seg(t, .6, 2.2))
    s += SL(Z_PERED, f'<path d="M380,{620+120*sp:.0f} h300 q20,{200+60*sp:.0f}'
                     f' -150,{260+80*sp:.0f} q-170,-{60+20*sp:.0f} -150,-{260+80*sp:.0f} z"'
                     f' fill="#8a3f3a" {o(6)}/>'
            + "".join(f'<path d="M390,{660+j*60+120*sp:.0f} h280" stroke="#d9a441"'
                      f' stroke-width="7" opacity=".7"/>' for j in range(4)))
    # ночник мягко светит
    mer = .8 + .2 * A.w(t, 2.6)
    s += SL(Z_SRED, f'<rect x="980" y="700" width="40" height="160" rx="10"'
                    f' fill="{ZHELEZ}" {o(6)}/>'
            + f'<path d="M900,700 q100,-120 200,0 z" fill="#f0d08a"'
              f' opacity="{mer:.2f}" {o(6)}/>'
            + teplo(1000, 720, 520, 440, .55 * mer))
    s += _vinetka(.52)
    return s


def krovat_i_chashka_bulona(t):
    """План 100. Кровать у окна, на табуретке бульон и градусник."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#cfd8dd"/>'
            + f'<rect x="1180" y="120" width="620" height="520" rx="12"'
              f' fill="url(#nden)" {o(9)}/>'
            + f'<path d="M1490,120 v520 M1180,380 h620" {o(8)} fill="none"/>'
            + sneg_letit(t, 18, 53, .5, .6)
            + f'<rect x="0" y="860" width="{W}" height="220" fill="url(#pol)"/>'
            + polovicy(860))
    # кровать
    s += SL(Z_SRED, f'<rect x="60" y="700" width="1000" height="40" rx="10"'
                    f' fill="url(#derev)" {o(8)}/>'
            + f'<rect x="60" y="480" width="46" height="260" rx="12"'
              f' fill="url(#derev)" {o(7)}/>')
    # одеяло дышит
    dysh = 9 * A.w(t, 3.8)
    s += SL(Z_SRED, f'<path d="M160,740 q{340+dysh:.0f},-{150+dysh:.0f} {820:.0f},-20'
                    f' v120 h-820 z" fill="#5e6b84" {o(7)}/>'
            + f'<path d="M200,{676-dysh*.3:.0f} q340,-70 760,-10" fill="none"'
              f' stroke="#7a88a4" stroke-width="12" opacity=".8"/>')
    s += SL(Z_SRED, f'<path d="M120,724 q-14,-120 160,-120 q180,0 166,120 z"'
                    f' fill="#e8e4d8" {o(7)}/>')
    # табуретка, чашка бульона, градусник в стакане
    s += SL(Z_SRED, f'<rect x="1180" y="760" width="300" height="34" rx="9"'
                    f' fill="url(#derev)" {o(7)}/>'
            + f'<rect x="1210" y="794" width="30" height="240" rx="9"'
              f' fill="url(#derev)" {o(6)}/>'
            + f'<rect x="1420" y="794" width="30" height="240" rx="9"'
              f' fill="url(#derev)" {o(6)}/>')
    s += SL(Z_PERED, f'<path d="M1210,756 q-10,-120 110,-120 q120,0 110,120 z"'
                     f' fill="#f2eee4" {o(7)}/>'
            + f'<ellipse cx="1320" cy="640" rx="110" ry="28" fill="#c08a3e" {o(5)}/>'
            + f'<path d="M1430,676 q66,10 44,76" fill="none" {o(14)}/>')
    s += SL(Z_PERED, par(1320, 600, t, 6, .55, 230, .4, 1.2))
    bl = .35 + .65 * abs(A.w(t, 1.9))
    s += SL(Z_PERED, f'<rect x="1520" y="600" width="90" height="160" rx="10"'
                     f' fill="url(#stekl)" opacity=".8" {o(6)}/>'
            + f'<path d="M1562,600 v-170" stroke="#e8ecee" stroke-width="14"/>'
            + f'<path d="M1562,470 v-30" stroke="{KRAS}" stroke-width="10"/>'
            + f'<path d="M1556,600 v-160" stroke="#ffffff" stroke-width="5"'
              f' opacity="{bl*.6:.2f}"/>')
    s += _vinetka(.46)
    return s


def kreslo_kachalka_u_detskoy_krovatki(t):
    """План 101. Качалка со спины, детская кроватка с пологом, молоко."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#e3d9c4"/>'
            + f'<rect x="1240" y="140" width="520" height="460" rx="12"'
              f' fill="url(#nrassv)" {o(9)}/>'
            + f'<path d="M1500,140 v460 M1240,370 h520" {o(7)} fill="none"/>'
            + f'<rect x="0" y="840" width="{W}" height="240" fill="url(#pol)"/>'
            + polovicy(840))
    # кресло-качалка качается
    ang = 4 * A.w(t, 2.6)
    s += SL(Z_SRED, f'<g transform="rotate({ang:.1f},520,900)">'
            + f'<path d="M300,860 q-20,-400 220,-400 q240,0 220,400 z"'
              f' fill="#6b4a2c" {o(8)}/>'
            + f'<path d="M340,700 q180,-60 360,0 v160 h-360 z" fill="#8a6038" {o(6)}/>'
            + f'<path d="M260,880 q260,80 520,0" fill="none" stroke="#5e4428"'
              f' stroke-width="24" stroke-linecap="round"/>'
            + babka(520, 830, 520, t, True, "#6b5a7a", .3, -8, "#8a7a94")
            + '</g>')
    # детская кроватка с пологом
    s += SL(Z_SRED, ten(1120, 930, 280, 26, .45)
            + f'<rect x="860" y="680" width="520" height="240" rx="16"'
              f' fill="url(#derev)" {o(8)}/>'
            + "".join(f'<path d="M{890+j*50},690 v220" stroke="#8a6038"'
                      f' stroke-width="13"/>' for j in range(10))
            + f'<rect x="860" y="660" width="520" height="30" rx="10"'
              f' fill="#8a6038" {o(6)}/>')
    kol = 12 * A.w(t, 2.2)
    s += SL(Z_PERED, f'<path d="M1120,300 q-{200+kol:.0f},120 -{280:.0f},380'
                     f' q{70:.0f},-20 {150:.0f},-120 z" fill="#f6eedc"'
                     f' opacity=".85" {o(5)}/>'
            + f'<path d="M1120,300 q{200-kol:.0f},120 {280:.0f},380'
              f' q-{70:.0f},-20 -{150:.0f},-120 z" fill="#f6eedc"'
              f' opacity=".85" {o(5)}/>'
            + f'<path d="M1120,300 q-40,180 -20,330" fill="none" stroke="#efe9da"'
              f' stroke-width="8" opacity=".8"/>'
            + f'<circle cx="1120" cy="292" r="22" fill="{MED}" {o(5)}/>')
    # кружка молока и блюдце творога на подоконнике
    s += SL(Z_SRED, f'<rect x="1220" y="600" width="560" height="26" rx="8"'
                    f' fill="url(#dosk)" {o(7)}/>')
    s += SL(Z_PERED, f'<path d="M1300,596 q-8,-100 90,-100 q98,0 90,100 z"'
                     f' fill="#f2eee4" {o(6)}/>'
            + f'<ellipse cx="1390" cy="500" rx="90" ry="24" fill="#fbfaf4" {o(4)}/>'
            + f'<path d="M1480,530 q54,8 36,62" fill="none" {o(12)}/>')
    s += SL(Z_PERED, par(1390, 470, t, 5, .5, 200, .45, 1.0))
    s += SL(Z_PERED, f'<ellipse cx="1660" cy="596" rx="110" ry="30" fill="url(#krem)" {o(5)}/>'
            + f'<path d="M1600,580 q60,-50 120,-4 q-60,26 -120,4 z" fill="#fbfaf4" {o(4)}/>')
    s += _vinetka(.44)
    return s


def tri_pary_obuvi_u_poroga(t):
    """План 102. Тапочки, дорожные сапоги с чемоданом, валенки с рукавицами."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#b9ad96"/>'
            + doski(0, 0, W, 620, 150, False, "derev")
            + f'<rect x="0" y="620" width="{W}" height="460" fill="url(#pol)"/>'
            + polovicy(620)
            + f'<rect x="0" y="600" width="{W}" height="40" rx="8"'
              f' fill="url(#dosk)" {o(7)}/>')
    # живое с первого кадра: свет из сеней дышит, пылинки, половик дрожит
    dysh = .8 + .2 * A.w(t, 2.6)
    s += SL(Z_DAL, teplo(1500, 520, 700, 620, .4 * dysh))
    for i in range(9):
        ph = (t * .25 + i * .11) % 1.0
        s += SL(Z_PERED, f'<circle cx="{300+i*170-80*ph:.0f}" cy="{140+ph*700:.0f}"'
                         f' r="4" fill="#fff6dc" opacity="{.45*(1-ph):.2f}"/>')
    kol = 6 * A.w(t, 1.7)
    s += SL(Z_SRED, f'<path d="M120,980 h520 l{-40+kol:.0f},70 h-500 z"'
                    f' fill="{TKAN2}" {o(5)} opacity=".9"/>'
            + "".join(f'<path d="M{160+j*100},984 l{-50+kol*.4:.0f},62"'
                      f' stroke="#e3d6b4" stroke-width="12" opacity=".6"/>'
                      for j in range(5)))
    pary = [
        (330, lambda: f'<path d="M200,900 q-16,-90 110,-90 q90,0 110,60 l-20,30 z"'
                      f' fill="#8a3f3a" {o(7)}/>'
                      f'<path d="M260,900 q-16,-90 110,-90 q90,0 110,60 l-20,30 z"'
                      f' fill="#9a4a44" {o(7)}/>'
                      f'<path d="M230,840 q60,-26 120,-4" fill="none" stroke="#e3d6b4"'
                      f' stroke-width="9"/>'),
        (880, lambda: f'<path d="M760,900 l20,-200 h120 l20,200 z" fill="#4a3426" {o(8)}/>'
                      f'<path d="M700,900 h260 v40 h-260 z" fill="#2f2420" {o(6)}/>'
                      f'<path d="M900,900 l20,-200 h120 l20,200 z" fill="#5a4030" {o(8)}/>'
                      f'<path d="M860,900 h260 v40 h-260 z" fill="#2f2420" {o(6)}/>'
                      f'<rect x="1140" y="700" width="280" height="200" rx="14"'
                      f' fill="#6b4a2c" {o(8)}/>'
                      f'<rect x="1240" y="676" width="80" height="34" rx="12"'
                      f' fill="#4a3426" {o(6)}/>'),
        (1600, lambda: f'<path d="M1500,900 l10,-230 h130 l10,230 z" fill="#8a8274" {o(8)}/>'
                       f'<path d="M1470,900 h190 v40 h-190 z" fill="#6b6456" {o(6)}/>'
                       f'<path d="M1650,900 l10,-230 h130 l10,230 z" fill="#9a9284" {o(8)}/>'
                       f'<path d="M1620,900 h190 v40 h-190 z" fill="#6b6456" {o(6)}/>'
                       f'<path d="M1480,640 q50,-70 110,-10 q-10,50 -110,10 z"'
                       f' fill="{TKAN2}" {o(6)}/>'
                       f'<path d="M1660,640 q50,-70 110,-10 q-10,50 -110,10 z"'
                       f' fill="{TKAN2}" {o(6)}/>'),
    ]
    for i, (xx, f) in enumerate(pary):
        k = A.over(A.seg(t, .1 + i * 1.5, .4))
        if k <= 0:
            continue
        kk = min(1.0, k)
        s += SL(Z_PERED, f'<g opacity="{kk:.2f}" transform="translate(0,{-50*(1-kk):.0f})">'
                + f() + '</g>')
    # рукавицы подсыхают: покачиваются весь план
    kach2 = 7 * A.w(t, 1.4)
    s += SL(Z_PERED, f'<path d="M1480,{640+kach2*.3:.0f} q50,-70 110,-10'
                     f' q-10,50 -110,10 z" fill="{TKAN2}" opacity=".9" {o(5)}/>'
            + f'<path d="M1660,{640-kach2*.3:.0f} q50,-70 110,-10'
              f' q-10,50 -110,10 z" fill="{TKAN2}" opacity=".9" {o(5)}/>')
    # снег тает на сапогах
    for i in range(4):
        ph = (t * .5 + i * .22) % 1.0
        s += SL(Z_PERED, f'<ellipse cx="{800+i*80}" cy="{900+ph*40:.0f}"'
                         f' rx="{10-3*ph:.0f}" ry="{14-4*ph:.0f}" fill="#cfe3ef"'
                         f' opacity="{.8*(1-ph):.2f}"/>')
    # чашка бульона рядом с тапочками
    kb = A.out(A.seg(t, 5.6, .8))
    if kb > 0:
        s += SL(Z_PERED, f'<g opacity="{kb:.2f}">'
                + f'<path d="M420,900 q-8,-90 80,-90 q88,0 80,90 z" fill="#f2eee4" {o(6)}/>'
                + f'<ellipse cx="500" cy="812" rx="80" ry="22" fill="#c08a3e" {o(4)}/>'
                + par(500, 780, t, 5, .5, 200, .45, 1.0) + '</g>')
    s += _vinetka(.44)
    return s


def zerkalo_s_babushkoy(t):
    """План 103. В зеркале вместо отражения появляется бабушка в платке."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#6b5a4a"/>'
            + f'<rect x="0" y="0" width="{W}" height="{H}" fill="url(#teplo)" opacity=".2"/>'
            + doski(0, 0, W, H, 170, False, "derev"))
    # лампа дрожит
    drozh = .8 + .2 * A.w(t, 2.4)
    s += SL(Z_SRED, lampa(320, 220, t, 1.6, True)
            + teplo(320, 320, 520, 460, .5 * drozh))
    # зеркало в прихожей
    s += SL(Z_SRED, f'<rect x="700" y="120" width="760" height="840" rx="20"'
                    f' fill="url(#zol)" {o(10)}/>'
            + f'<rect x="750" y="170" width="660" height="740" rx="14"'
              f' fill="#8fa8bc" opacity=".85" {o(6)}/>')
    # отражение меняется: женщина → бабушка в платке
    k = A.ease(A.seg(t, 1.6, 1.6))
    s += SL(Z_SRED, f'<g opacity="{1-k:.2f}">'
            + babka(1080, 820, 560, t, True, "#6b5a7a", .1, 0, "#8a7a94", False) + '</g>')
    if k > .02:
        kiv = 5 * A.w(t, 1.4)
        s += SL(Z_SRED, f'<g opacity="{k:.2f}" transform="rotate({kiv:.1f},1080,640)">'
                + babka(1080, 820, 580, t, True, TKAN, .5, -6, "#5e6b7a", False) + '</g>')
    # женщина со спины перед зеркалом
    s += SL(Z_PERED, f'<g>'
            + babka(560, 1190, 900, t, True, "#4a4458", .4, 0, "#5e5468", True)
            + f'<path d="M470,520 q80,-70 170,-10 q-46,66 -170,10 z" fill="#cfcabc"'
              f' opacity=".92" {o(5)}/></g>')
    s += _vinetka(.5)
    return s


def delyanka_na_moroze(t):
    """План 104. Лесоруб у пня с миской капусты, ему несут горячий горшок."""
    s = SL(Z_NEBO, nebo("den", t, False) + oblaka(t, 160, 4, 59, .45))
    s += SL(Z_DAL, f'<rect x="0" y="520" width="{W}" height="{H-520}" fill="url(#sneg)"/>')
    # зимний лес
    for i, (xx, hh) in enumerate(((120, 460), (420, 520), (1500, 480), (1760, 420))):
        s += SL(Z_DAL, f'<path d="M{xx},560 v-{hh}" {o(18)} fill="none"/>'
                + "".join(f'<path d="M{xx},{560-hh+j*58} l{-90+j*14},{48}'
                          f' M{xx},{560-hh+j*58} l{90-j*14},{48}" {o(11)} fill="none"/>'
                          for j in range(6))
                + f'<ellipse cx="{xx}" cy="{556}" rx="80" ry="24" fill="{SNEG}" opacity=".85"/>')
    # снег падает с веток
    for i in range(5):
        ph = (t * .4 + i * .2) % 1.0
        s += SL(Z_PERED, f'<ellipse cx="{150+i*380}" cy="{300+ph*560:.0f}" rx="{22-8*ph:.0f}"'
                         f' ry="{12-4*ph:.0f}" fill="#ffffff" opacity="{.8*(1-ph):.2f}"/>')
    # пень с миской капусты
    s += SL(Z_SRED, ten(900, 960, 180, 30, .5)
            + f'<rect x="780" y="780" width="240" height="180" rx="14"'
              f' fill="url(#derev)" {o(8)}/>'
            + f'<ellipse cx="900" cy="782" rx="122" ry="34" fill="#b08456" {o(6)}/>'
            + "".join(f'<ellipse cx="900" cy="782" rx="{100-j*26}" ry="{28-j*7}"'
                      f' fill="none" stroke="#8a6038" stroke-width="4" opacity=".7"/>'
                      for j in range(3)))
    s += SL(Z_PERED, f'<path d="M800,770 q-10,-90 100,-90 q110,0 100,90 z"'
                     f' fill="url(#krem)" {o(7)}/>'
            + f'<ellipse cx="900" cy="684" rx="100" ry="26" fill="#9ab07e" {o(5)}/>')
    # человек в тулупе, опирается на топор, разводит руками
    razv = A.ease(A.seg(t, 1.6, 1.2))
    s += SL(Z_PERED, muzh(480, 1020, 760, t, .2, "#6b4a2c", True))
    s += SL(Z_PERED, f'<g transform="rotate({-24*razv:.0f},560,640)">'
            + ruka(560, 640, t, 240, 10, 52, "#6b4a2c") + '</g>')
    s += SL(Z_PERED, f'<path d="M300,1030 l70,-330" stroke="url(#derev)"'
                     f' stroke-width="30" stroke-linecap="round"/>'
            + f'<path d="M360,700 q80,-40 130,30 q-40,56 -140,24 z" fill="{ZHELEZ}" {o(7)}/>'
            + f'<path d="M382,712 q60,-22 92,24" fill="none" stroke="#e8ecee"'
              f' stroke-width="9" opacity=".6"/>')
    # пар изо рта
    s += SL(Z_PERED, par(600, 560, t, 5, .4, 190, .3, 1.4))
    # из-за кадра протягивают горшок с горячим
    k = A.ease(A.seg(t, 3.4, 1.4))
    s += SL(Z_PERED, f'<g transform="translate({500-500*k:.0f},0)">'
            + ruka(1560, 700, t, 260, 170, 54, "#6b5a6e")
            + gorshok(1400, 800, 1.5, t, "url(#glina)", False)
            + par(1400, 660, t, 6, .55, 230, .4, 1.2) + '</g>')
    s += SL(Z_LETIT, _sneg_letit(t, 24, 61, .5, .6))
    s += _vinetka(.44)
    return s


def vagonnyy_stolik(t):
    """План 105. Купе: стакан в подстаканнике, яйцо, курица в бумаге."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#6b5a4a"/>'
            + f'<rect x="0" y="0" width="{W}" height="300" fill="#7a6a54"/>'
            + doski(0, 0, 900, H, 140, False, "derev"))
    # окно купе: столбы мелькают
    s += SL(Z_SRED, f'<rect x="900" y="120" width="900" height="560" rx="26"'
                    f' fill="url(#nden)" {o(10)}/>')
    for i in range(6):
        ph = (t * 1.6 + i * .17) % 1.0
        xx = 1800 - ph * 900
        s += SL(Z_DAL, f'<rect x="{xx:.0f}" y="200" width="34" height="400"'
                       f' fill="#5e5648" opacity="{.75*(1-abs(ph-.5)):.2f}"/>')
    s += SL(Z_DAL, sneg_letit(t, 30, 67, .6, 1.6))
    s += SL(Z_SRED, f'<rect x="880" y="660" width="940" height="40" rx="12"'
                    f' fill="url(#dosk)" {o(8)}/>')
    # столик
    s += SL(Z_SRED, f'<rect x="120" y="760" width="1000" height="44" rx="12"'
                    f' fill="#8a6a46" {o(9)}/>'
            + f'<rect x="300" y="804" width="60" height="276" rx="10"'
              f' fill="url(#derev)" {o(7)}/>')
    # стакан в подстаканнике, чай качается
    kach = 6 * A.w(t, 1.3)
    s += SL(Z_PERED, f'<path d="M300,756 l16,-240 h150 l16,240 z" fill="url(#stekl)"'
                     f' opacity=".85" {o(7)}/>'
            + f'<path d="M318,{556+kach*.4:.0f} h130 l10,190 h-150 z" fill="#8a5a24"'
              f' opacity=".9"/>'
            + f'<path d="M296,580 h180 v150 h-180 z" fill="none" stroke="{ZHELEZ}"'
              f' stroke-width="14"/>'
            + f'<path d="M476,620 q60,34 0,74" fill="none" stroke="{ZHELEZ}"'
              f' stroke-width="14"/>')
    # ложечка звенит
    zv = 8 * A.w(t, .55)
    s += SL(Z_PERED, f'<path d="M{380+zv:.0f},520 l40,-160" stroke="{ZHELEZ}"'
                     f' stroke-width="12" stroke-linecap="round"/>')
    # варёное яйцо и курица в бумаге
    s += SL(Z_PERED, f'<ellipse cx="640" cy="700" rx="52" ry="66" fill="#f6eddc" {o(6)}/>'
            + f'<ellipse cx="624" cy="674" rx="18" ry="24" fill="#ffffff" opacity=".6"/>')
    s += SL(Z_PERED, f'<path d="M800,756 l40,-130 h240 l30,130 z" fill="#d8cdb4" {o(7)}/>'
            + f'<path d="M860,626 q90,-70 170,-10 q-60,40 -170,10 z" fill="#c9975a" {o(5)}/>')
    s += _vinetka(.48)
    return s


def dve_kastryulki_na_plite(t):
    """План 106. Маленькая кастрюлька бульона и большая постных щей."""
    s = SL(Z_DAL, kuhnya_stena(t, True, None, False, True, 71))
    s += SL(Z_SRED, f'<rect x="60" y="680" width="1200" height="320" rx="16"'
                    f' fill="url(#zhel)" {o(8)}/>'
            + f'<rect x="90" y="712" width="1140" height="26" rx="8"'
              f' fill="{CHUGUN}" opacity=".6"/>')
    # маленькая кастрюлька бульона
    s += SL(Z_SRED, f'<path d="M200,680 q-14,-150 150,-150 q164,0 150,150 z"'
                    f' fill="#e9eef0" {o(7)}/>'
            + f'<ellipse cx="350" cy="534" rx="152" ry="36" fill="#dcae3c" {o(5)}/>')
    # большая кастрюля щей кипит
    s += SL(Z_SRED, f'<path d="M700,680 q-26,-230 230,-230 q256,0 230,230 z"'
                    f' fill="url(#chug)" {o(8)}/>'
            + f'<ellipse cx="930" cy="452" rx="232" ry="52" fill="#8a7a3c" {o(6)}/>')
    for i in range(6):
        ph = (t * 1.2 + i * .16) % 1.0
        s += SL(Z_PERED, f'<circle cx="{800+i*54}" cy="{446-24*ph:.0f}" r="{9+8*ph:.0f}"'
                         f' fill="#a8933c" opacity="{.65*(1-ph):.2f}" {o(2)}/>')
    s += SL(Z_PERED, par(930, 400, t, 6, .55, 250, .4, 1.3))
    # бульон льётся в чашку, рука уносит
    k = A.seg(t, .4, 1.4)
    ko = A.ease(A.seg(t, 2.2, 1.6))
    if k > 0 and ko < .1:
        s += SL(Z_PERED, f'<path d="M430,540 q90,{60*k:.0f} 150,{150*k:.0f}"'
                         f' fill="none" stroke="#dcae3c" stroke-width="16"'
                         f' stroke-linecap="round" opacity=".92"/>')
    s += SL(Z_PERED, f'<g transform="translate({600*ko:.0f},{-120*ko:.0f})">'
            + f'<path d="M520,780 q-8,-110 100,-110 q108,0 100,110 z" fill="#f2eee4" {o(7)}/>'
            + f'<ellipse cx="620" cy="672" rx="100" ry="26" fill="#dcae3c" {o(5)}/>'
            + f'<path d="M720,706 q58,10 38,66" fill="none" {o(13)}/>'
            + par(620, 640, t, 5, .5, 200, .45, 1.0)
            + (ruka(260, 880, t, 250, -26, 52, "#6b5a6e") if ko > .05 else "")
            + '</g>')
    s += _vinetka(.44)
    return s


def listok_naznacheniya_i_ochki(t):
    """План 107. Листок с печатью, очки сверху, рядом тарелка."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#e8ddc6"/>'
            + "".join(f'<path d="M{-30+j*130},0 v{H}" stroke="#b9553f"'
                      f' stroke-width="6" opacity=".3"/>' for j in range(17)))
    s += SL(Z_SRED, teplo(820, 560, 980, 660, .4))
    # листок шевелится
    sh = 7 * A.w(t, 1.6)
    s += SL(Z_PERED, ten(620, 860, 300, 30, .4)
            + f'<path d="M300,240 h640 q{sh:.0f},300 0,600 h-640 q-{sh:.0f},-300 0,-600 z"'
              f' fill="#fdfaf2" {o(7)}/>'
            + "".join(f'<path d="M350,{330+j*70} q{90+j*10},{14 if j%2 else -10}'
                      f' {200+j*30},{4}" fill="none" stroke="#8a8274"'
                      f' stroke-width="8" opacity=".8"/>' for j in range(6))
            + f'<circle cx="790" cy="740" r="92" fill="none" stroke="#4a6b86"'
              f' stroke-width="11" opacity=".85"/>'
            + f'<circle cx="790" cy="740" r="62" fill="none" stroke="#4a6b86"'
              f' stroke-width="7" opacity=".7"/>')
    # очки сверху, бликуют
    bl = .3 + .6 * abs(A.w(t, 2.0))
    s += SL(Z_PERED, f'<g transform="rotate(-8,560,520)">'
            + f'<circle cx="440" cy="520" r="96" fill="url(#stekl)"'
              f' opacity="{.5+.2*bl:.2f}" {o(10)}/>'
            + f'<circle cx="700" cy="520" r="96" fill="url(#stekl)"'
              f' opacity="{.5+.2*bl:.2f}" {o(10)}/>'
            + f'<path d="M536,520 h68" {o(10)} fill="none"/>'
            + f'<path d="M344,520 q-70,-30 -100,30 M796,520 q70,-30 100,30" {o(9)} fill="none"/>'
            + '</g>')
    # тарелка с тем, что положено
    s += SL(Z_PERED, tarelka(1480, 780, 200, t, "url(#krem)", True, 2)
            + f'<ellipse cx="1480" cy="756" rx="140" ry="48" fill="#d9bd86" {o(5)}/>')
    s += _vinetka(.44)
    return s


def ruki_pomogayut(t):
    """План 108. Тарелка уходит из резкости, за ней руки помогают."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#3f4450"/>'
            + f'<rect x="0" y="0" width="{W}" height="{H}" fill="url(#teplo)" opacity=".25"/>')
    s += SL(Z_DAL, lampa(1500, 220, t, 1.5, True) + teplo(1500, 420, 620, 520, .5))
    # фигура в пледе со спины
    s += SL(Z_SRED, babka(1080, 1010, 660, t, True, "#5e5468", .2, -4, "#6b5a6e", False))
    # плед расправляется на плечах
    k = A.ease(A.seg(t, 1.2, 1.8))
    s += SL(Z_SRED, f'<path d="M940,{700-40*k:.0f} q140,-{60+40*k:.0f} 290,0'
                    f' q{20:.0f},{200+60*k:.0f} -145,{240+40*k:.0f}'
                    f' q-165,-{40*k:.0f} -145,-{240+40*k:.0f} z"'
                    f' fill="#8a3f3a" {o(6)}/>'
            + "".join(f'<path d="M950,{760+j*66-20*k:.0f} h270" stroke="#d9a441"'
                      f' stroke-width="7" opacity=".7"/>' for j in range(3)))
    s += SL(Z_PERED, ruka(1360, 640, t, 250, 168, 50, "#5e5468"))
    # вторая рука подаёт стакан воды
    k2 = A.ease(A.seg(t, 2.6, 1.6))
    kach = 5 * A.w(t, 1.4)
    s += SL(Z_PERED, f'<g transform="translate({-300*(1-k2):.0f},0)">'
            + ruka(520, 700, t, 250, -10, 52, "#6b5a6e")
            + f'<path d="M790,760 l12,-170 h110 l12,170 z" fill="url(#stekl)"'
              f' opacity=".85" {o(6)}/>'
            + f'<path d="M802,{626+kach*.3:.0f} h98 l8,130 h-114 z" fill="#8fc0d8"'
              f' opacity=".8"/></g>')
    # тарелка на первом плане расплывается
    razm = A.seg(t, .2, 1.4)
    s += SL(Z_PERED, f'<g opacity="{1-razm*.55:.2f}">'
            + f'<ellipse cx="420" cy="1010" rx="{330+40*razm:.0f}" ry="{110+20*razm:.0f}"'
              f' fill="url(#krem)" {o(int(8-4*razm))}/>'
            + f'<ellipse cx="420" cy="996" rx="{250+30*razm:.0f}" ry="{80+14*razm:.0f}"'
              f' fill="#d9bd86" opacity="{.9-.3*razm:.2f}"/></g>')
    s += _vinetka(.5)
    return s


def sup_i_dvoe_za_nim(t):
    """План 109. За тарелкой супа двое: один придвигает хлеб, другой — руку."""
    s = SL(Z_DAL, kuhnya_stena(t, True, 1480, True, True, 73))
    s += SL(Z_SRED, teplo(860, 560, 900, 620, .5))
    # двое за столом
    s += SL(Z_SRED, babka(620, 1010, 740, t, True, "#5e6b7a", .1, -8))
    s += SL(Z_SRED, muzh(1180, 1010, 760, t, .4, "#4a5b4a", False))
    # рука ложится на плечо
    k = A.ease(A.seg(t, .8, 1.2))
    s += SL(Z_PERED, f'<g opacity="{k:.2f}" transform="translate({-80*(1-k):.0f},0)">'
            + ruka(980, 560, t, 220, 12, 46, "#4a5b4a") + '</g>')
    # хлебница едет по столу
    kh = A.ease(A.seg(t, 1.6, 1.4))
    s += SL(Z_PERED, f'<g transform="translate({-260*kh:.0f},0)">'
            + f'<ellipse cx="1240" cy="930" rx="150" ry="44" fill="url(#solom)" {o(6)}/>'
            + f'<path d="M1150,910 q90,-80 180,-10 q-90,40 -180,10 z" fill="#8a5a2c" {o(5)}/>'
            + '</g>')
    # тарелка супа на первом плане
    s += SL(Z_PERED, f'<path d="M120,960 q0,120 330,120 q330,0 330,-120 z"'
                     f' fill="url(#krem)" {o(9)}/>'
            + f'<ellipse cx="450" cy="960" rx="330" ry="108" fill="#e8dcc0" {o(8)}/>'
            + f'<ellipse cx="450" cy="966" rx="262" ry="80" fill="#c08a3e" {o(5)}/>')
    s += SL(Z_PERED, par(450, 880, t, 6, .55, 240, .4, 1.3))
    s += _vinetka(.46)
    return s


def otodvinutaya_tarelka(t):
    """План 110. Смена главы: пустая тарелка у края, сложенные руки в центре."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#2a2520"/>'
            + f'<rect x="0" y="0" width="{W}" height="{H}" fill="url(#teplo)" opacity=".22"/>')
    # одна лампа покачивается
    ang = 2.2 * A.w(t, 3.0)
    s += SL(Z_SRED, f'<g transform="rotate({ang:.1f},960,40)">'
            + f'<path d="M960,40 v200" {o(7)} fill="none"/>'
            + lampa(960, 280, t, 2.2, True) + '</g>')
    s += SL(Z_SRED, teplo(960, 640, 960, 620, .6))
    # стол со скатертью
    s += SL(Z_SRED, stol_bok(140, 820, 1640, 260, t, "#e7dcc4"))
    # пустая тарелка отодвинута к краю
    s += SL(Z_PERED, f'<g opacity=".95">' + tarelka(1680, 760, 130, t) + '</g>'
            + f'<ellipse cx="1700" cy="800" rx="150" ry="36" fill="#000000" opacity=".25"/>')
    # сложенные руки в центре, пальцы перебирают край скатерти
    per = 7 * A.w(t, 1.3)
    s += SL(Z_PERED, f'<g transform="translate({per*.3:.1f},0)">'
            + ruka(360, 660, t, 420, 10, 74, "#6b5a6e", False)
            + f'<g transform="translate(40,70)">'
            + ruka(380, 680, t, 400, -6, 70, "#6b5a6e", False) + '</g>'
            # ладонь поверх ладони: пальцы лежат друг на друге
            + "".join(f'<path d="M{860+j*10},{738+j*30} q70,{10:.0f} 120,-{6:.0f}"'
                      f' fill="none" stroke="#e8bb93" stroke-width="26"'
                      f' stroke-linecap="round"/>' for j in range(3))
            + f'<path d="M870,836 q60,30 130,10" fill="none" stroke="#dca882"'
              f' stroke-width="24" stroke-linecap="round"/>'
            + '</g>')
    for j in range(3):
        s += SL(Z_PERED, f'<path d="M{1020+j*34},{800+per*.6:.0f} q14,36 2,66"'
                         f' fill="none" stroke="#e8bb93" stroke-width="16"'
                         f' stroke-linecap="round"/>')
    s += _vinetka(.54)
    return s


def lozhka_i_chelovechki(t):
    """Планы 111, 116. Ложка обходит фигурки людей вокруг тарелки."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#e8ddc6"/>'
            + "".join(f'<path d="M0,{-20+j*120} h{W}" stroke="#b9553f"'
                      f' stroke-width="7" opacity=".28"/>' for j in range(10)))
    s += SL(Z_SRED, teplo(900, 600, 980, 700, .4))
    # тарелка в центре
    s += SL(Z_SRED, tarelka(900, 700, 250, t, "url(#krem)", True)
            + f'<ellipse cx="900" cy="682" rx="180" ry="62" fill="#d9bd86" {o(5)}/>')
    # фигурки людей вокруг переминаются
    figurki = ((420, "соседка", TKAN), (1420, "невестка", "#5e6b7a"), (1180, "сосед", "#4a5b4a"))
    for i, (xx, _, col) in enumerate(figurki):
        pere = 5 * A.w(t, 1.5, i * .33)
        yy = 900 if i != 2 else 420
        s += SL(Z_PERED, f'<g transform="translate({pere:.1f},0)">'
                + babka(xx, yy, 300, t, True, col, i * .2, -4) + '</g>')
        if i == 2:         # сосед с газетой
            s += SL(Z_PERED, f'<path d="M{xx+60},{yy-160} h150 v110 h-150 z"'
                             f' fill="#fdfaf2" {o(5)}/>'
                    + "".join(f'<path d="M{xx+70},{yy-140+j*22} h130" stroke="#b9b2a2"'
                              f' stroke-width="5"/>' for j in range(4)))
    # ложка зачерпывает и обходит фигурки
    hod = A.seg(t, .4, 3.4)
    a = hod * 6.0
    lx = 900 + math.cos(a) * 420
    ly = 700 + math.sin(a) * 180
    s += SL(Z_PERED, f'<g transform="rotate({-20+40*math.sin(a):.0f},{lx:.0f},{ly:.0f})">'
            + f'<path d="M{lx:.0f},{ly:.0f} l200,-130" stroke="{ZHELEZ}"'
              f' stroke-width="20" stroke-linecap="round"/>'
            + f'<ellipse cx="{lx:.0f}" cy="{ly:.0f}" rx="76" ry="48" fill="{ZHELEZ}" {o(6)}/>'
            + f'<ellipse cx="{lx-16:.0f}" cy="{ly-10:.0f}" rx="28" ry="14"'
              f' fill="#ffffff" opacity=".35"/></g>')
    # бабушкин палец грозит ложке
    kp = A.out(A.seg(t, 3.6, .8))
    if kp > 0:
        kach = 14 * A.w(t, .8)
        s += SL(Z_PERED, f'<g opacity="{kp:.2f}" transform="translate({(1-kp)*220:.0f},0)">'
                + f'<path d="M1900,480 q-200,-30 -300,-60" fill="none" stroke="#e8bb93"'
                  f' stroke-width="58" stroke-linecap="round"/>'
                + f'<g transform="rotate({kach:.0f},1600,420)">'
                + f'<path d="M1600,420 q-26,-90 -8,-170" fill="none" stroke="#e8bb93"'
                  f' stroke-width="38" stroke-linecap="round"/></g></g>')
    s += _vinetka(.46)
    return s


# ═══════════════ БЛОК 7. ЗАПРЕТЫ, КОТОРЫЕ НЕ ПРО ЕДУ ═══════════════
def tri_medalona_nad_tarelkoy(t):
    """План 112. Над тарелкой загораются три картинки-медальона."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#2f2a26"/>'
            + f'<rect x="0" y="0" width="{W}" height="{H}" fill="url(#teplo)" opacity=".25"/>')
    s += SL(Z_SRED, stol_bok(140, 900, 1640, 180, t, "#e7dcc4"))
    s += SL(Z_SRED, tarelka(960, 880, 200, t, "url(#krem)", True, 1))
    med = [
        (380, lambda: f'<circle cx="0" cy="0" r="150" fill="#3f4a56" {o(8)}/>'
                      + siluet(-52, 90, 190, "#1d2026", 1.0, True, "#d9c49c")
                      + siluet(52, 90, 190, "#1d2026", 1.0, False, "#d9c49c")
                      + f'<ellipse cx="0" cy="40" rx="40" ry="14" fill="#c08a3e" {o(3)}/>'),
        (960, lambda: f'<circle cx="0" cy="0" r="150" fill="#56404a" {o(8)}/>'
                      + siluet(-56, 92, 196, "#1d2026", 1.0, True, "#d9c49c")
                      + siluet(58, 96, 180, "#1d2026", 1.0, True, "#d9c49c")
                      + f'<path d="M20,-10 q40,-30 70,10 q-40,26 -70,-10 z" fill="#e8e4d8"'
                        f' opacity=".85"/>'),
        (1540, lambda: f'<circle cx="0" cy="0" r="150" fill="#3f5646" {o(8)}/>'
                       + siluet(-40, 94, 150, "#1d2026", 1.0, False, "#d9c49c")
                       + siluet(60, 94, 186, "#1d2026", 1.0, True, "#d9c49c")
                       + f'<rect x="-10" y="10" width="60" height="52" rx="10"'
                         f' fill="#8a6038" {o(4)}/>'),
    ]
    for i, (xx, f) in enumerate(med):
        k = A.out(A.seg(t, .6 + i * 1.3, .7))
        if k <= 0:
            continue
        s += SL(Z_PERED, f'<g opacity="{k:.2f}" transform="translate({xx},380)'
                f' scale({.6+.4*k:.2f})">' + f() + '</g>')
    s += SL(Z_PERED, par(960, 820, t, 5, .45, 200, .45, 1.1))
    s += _vinetka(.5)
    return s


def sorok_misok_i_klyaksa(t):
    """План 113. Ряд из сорока мисок, сверху падает чёрная клякса."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#e3d9c4"/>'
            + f'<rect x="0" y="0" width="{W}" height="420" fill="#d2c7ae"/>')
    # ряд мисок уходит вдаль
    for i in range(14):
        sc = 1.0 - i * .062
        xx = 220 + i * 128 * sc * 1.1
        yy = 900 - i * 36
        s += SL(Z_SRED if i > 4 else Z_PERED,
                f'<g transform="translate({xx:.0f},{yy}) scale({sc:.2f})">'
                + f'<path d="M-110,0 q-14,-120 110,-120 q124,0 110,120 z"'
                  f' fill="url(#krem)" {o(int(7*sc)+1)}/>'
                + f'<ellipse cx="0" cy="-116" rx="112" ry="28" fill="#9ab07e" {o(4)}/>'
                + '</g>')
    # клякса падает и брызги летят
    k = A.ease(A.seg(t, 1.6, .7))
    if k > 0:
        s += SL(Z_PERED, f'<ellipse cx="760" cy="{-200+1000*k:.0f}" rx="{90*k:.0f}"'
                         f' ry="{110*k:.0f}" fill="#14110e" opacity=".95"/>')
    br = A.seg(t, 2.3, 1.2)
    if br > 0:
        for i in range(14):
            a = i * .45
            dx = math.cos(a) * 700 * br
            dy = math.sin(a) * 300 * br - 120 * br
            s += SL(Z_PERED, f'<ellipse cx="{760+dx:.0f}" cy="{800+dy:.0f}"'
                             f' rx="{26-14*br:.0f}" ry="{20-10*br:.0f}" fill="#14110e"'
                             f' opacity="{.9-.3*br:.2f}"/>')
        s += SL(Z_PERED, f'<ellipse cx="760" cy="820" rx="{200*br:.0f}" ry="{60*br:.0f}"'
                         f' fill="#14110e" opacity=".9"/>')
    s += _vinetka(.44)
    return s


def korzinka_u_chuzhoy_dveri(t):
    """План 115. Корзинку ставят у чужого порога, дверь приоткрывается."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#4a4440"/>'
            + kladka(0, 0, W, H, 76, "#5e564c")
            + f'<rect x="0" y="0" width="{W}" height="{H}" fill="#000000" opacity=".25"/>')
    # дверь
    s += SL(Z_SRED, f'<rect x="620" y="60" width="760" height="900" rx="10"'
                    f' fill="#6b4a2c" {o(9)}/>'
            + f'<rect x="680" y="130" width="300" height="340" rx="10"'
              f' fill="#5e4028" {o(6)}/>'
            + f'<rect x="680" y="520" width="300" height="340" rx="10"'
              f' fill="#5e4028" {o(6)}/>'
            + f'<circle cx="1300" cy="560" r="26" fill="{MED}" {o(6)}/>')
    # полоса тёплого света расширяется
    k = A.ease(A.seg(t, 1.2, 1.6))
    s += SL(Z_PERED, f'<path d="M620,60 h{40+260*k:.0f} l{120*k:.0f},900 h-{160+120*k:.0f} z"'
                     f' fill="{SVET}" opacity="{.25+.45*k:.2f}"/>'
            + teplo(760, 600, 520 * k + 120, 700, .5 * k))
    # корзинка с хлебом и крупой
    s += SL(Z_PERED, f'<path d="M660,960 q-16,-180 180,-180 q196,0 180,180 z"'
                     f' fill="url(#solom)" {o(8)}/>'
            + f'<path d="M660,860 h360" stroke="#b58a42" stroke-width="12" opacity=".8"/>'
            + f'<path d="M700,790 q140,-140 280,-10 q-140,60 -280,10 z"'
              f' fill="#8a5a2c" {o(6)}/>'
            + f'<rect x="900" y="700" width="120" height="90" rx="10"'
              f' fill="#d9bd86" {o(5)}/>')
    s += SL(Z_PERED, par(840, 740, t, 5, .5, 200, .45, 1.1))
    # рука уходит
    uh = A.ease(A.seg(t, .2, 1.0))
    s += SL(Z_PERED, f'<g opacity="{1-uh:.2f}" transform="translate({-260*uh:.0f},0)">'
            + ruka(240, 820, t, 250, -14, 52, "#4a4458") + '</g>')
    s += _vinetka(.52)
    return s


def ochered_v_zimnih_palto(t):
    """План 117. Очередь со спины, колючее облачко, облачко-мысль героини."""
    s = SL(Z_NEBO, nebo("sumer", t, True) + oblaka(t, 170, 3, 79, .35))
    s += SL(Z_DAL, f'<rect x="0" y="560" width="{W}" height="{H-560}" fill="#cfdde8"/>'
            + _sneg_lezhit(560, 22)
            + _ulica_dal(0, 460, W, t, True, 31))
    s += SL(Z_LETIT, _sneg_letit(t, 30, 83, .6, .7))
    # очередь со спины
    for i, (xx, h_, col, pl) in enumerate(((240, 620, "#4a4152", True),
                                           (440, 650, "#3f4a5c", False),
                                           (1320, 640, "#5e4a42", True),
                                           (1520, 610, "#3a4450", True))):
        s += SL(Z_SRED, spina(xx, 1020, h_, t, col,
                              ("#8a3f3a" if i % 2 else "#4a6b86") if pl else None, i * .17))
    # героиня молчит и смотрит на снег
    s += SL(Z_PERED, babka(860, 1040, 700, t, True, "#6b5a7a", .1, 0))
    # колючее облачко от обернувшегося
    k = A.out(A.seg(t, .5, .6)) * (1 - A.seg(t, 2.2, 1.2))
    if k > .02:
        s += SL(Z_PERED, f'<g opacity="{k:.2f}" transform="translate(1320,420)">'
                + f'<path d="M-170,0 l40,-40 l-10,-50 l60,10 l30,-50 l40,44 l60,-20'
                  f' l0,56 l50,30 l-44,40 l10,50 l-60,-14 l-34,44 l-40,-44 l-56,16'
                  f' l4,-54 z" fill="#8a3f3a" opacity=".9" {o(6)}/>'
                + "".join(f'<path d="M{-70+j*44},-10 h30" stroke="#f6eedc"'
                          f' stroke-width="8" opacity=".9"/>' for j in range(3))
                + '</g>')
    # облачко-мысль: на тарелке две фигурки, вилка откладывается
    km = A.out(A.seg(t, 2.6, .8))
    if km > 0:
        otl = A.ease(A.seg(t, 3.6, .8))
        s += SL(Z_PERED, f'<g opacity="{km:.2f}" transform="translate(560,330)'
                f' scale({.7+.3*km:.2f})">'
                + f'<ellipse cx="0" cy="0" rx="260" ry="170" fill="#fdfaf2"'
                  f' opacity=".95" {o(6)}/>'
                + f'<ellipse cx="-170" cy="150" rx="46" ry="34" fill="#fdfaf2" {o(5)}/>'
                + f'<ellipse cx="-230" cy="210" rx="26" ry="20" fill="#fdfaf2" {o(4)}/>'
                + f'<ellipse cx="0" cy="30" rx="150" ry="44" fill="url(#krem)" {o(5)}/>'
                + siluet(-40, 20, 110, "#4a4152", 1.0, True, None)
                + siluet(40, 20, 110, "#4a4152", 1.0, False, None)
                + f'<g transform="rotate({70*otl:.0f},150,40)">'
                + f'<path d="M150,40 l90,-60" stroke="{ZHELEZ}" stroke-width="10"/></g>'
                + '</g>')
    s += _vinetka(.46)
    return s


def telefon_s_dlinnym_shnurom(t):
    """План 118. Шнур петлями через квартиру, в петлях силуэты; таймер."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#cfc4ac"/>'
            + f'<rect x="0" y="0" width="{W}" height="380" fill="#b9ad96"/>'
            + f'<rect x="0" y="820" width="{W}" height="260" fill="url(#pol)"/>'
            + polovicy(820)
            + _kvartira_veschi(140, 820, 420, t, 19))
    # шнур петлями: распрямляется
    rasp = A.ease(A.seg(t, 1.6, 1.6))
    for i in range(4):
        xx = 260 + i * 330
        r_ = (120 - 100 * rasp)
        s += SL(Z_SRED, f'<path d="M{xx},620 q{r_:.0f},-{r_*1.2:.0f} {r_*2:.0f},0"'
                        f' fill="none" stroke="#2f2a26" stroke-width="12"/>')
        if rasp < .7:
            s += SL(Z_PERED, f'<g opacity="{(1-rasp/.7)*.9:.2f}">'
                    + spina(xx + r_, 600, 160 + i * 12, t, "#4a4458",
                            TKAN if i % 2 == 0 else None, i * .3)
                    + '</g>')
    s += SL(Z_SRED, f'<path d="M160,620 h100 M1580,620 h160" stroke="#2f2a26"'
                    f' stroke-width="12"/>')
    # телефон на тумбе
    s += SL(Z_SRED, f'<rect x="60" y="640" width="220" height="180" rx="12"'
                    f' fill="#2f2a26" {o(8)}/>'
            + f'<rect x="90" y="600" width="160" height="56" rx="18"'
              f' fill="#3a3430" {o(6)}/>'
            + f'<circle cx="170" cy="730" r="48" fill="#4a443e" {o(5)}/>')
    # хозяйка с трубкой улыбается и машет
    s += SL(Z_PERED, babka(1620, 1030, 700, t, True, "#8a3f3a", .2, -18, TKAN2, False))
    mah = 16 * A.w(t, 1.1)
    s += SL(Z_PERED, f'<g transform="rotate({mah:.0f},1500,560)">'
            + ruka(1500, 560, t, 220, -30, 48, "#6b5a6e") + '</g>')
    # кухонный таймер звенит и подпрыгивает
    zv = A.seg(t, 2.2, 1.2)
    pr = 16 * abs(A.w(t, .35)) * (1 if zv > 0 else 0)
    s += SL(Z_PERED, f'<g transform="translate(0,{-pr:.0f})">'
            + f'<circle cx="980" cy="880" r="76" fill="#e8e4d8" {o(7)}/>'
            + f'<path d="M980,880 v-50 M980,880 l34,24" stroke="{K}" stroke-width="8"/>'
            + f'<rect x="954" y="792" width="52" height="24" rx="8" fill="{ZHELEZ}" {o(4)}/></g>')
    if zv > 0:
        for j in range(3):
            s += SL(Z_PERED, f'<path d="M{1070+j*30},{840-j*20} q30,{40+j*14} 0,{80+j*28}"'
                             f' fill="none" stroke="{ZOL}" stroke-width="7"'
                             f' opacity="{.7*zv*(1-j*.2):.2f}"/>')
    s += _vinetka(.44)
    return s


def lozhka_na_blyudce(t):
    """План 119. Ложка на блюдце, над ней спокойная улыбка бабушки."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#3a332c"/>'
            + f'<rect x="0" y="0" width="{W}" height="{H}" fill="url(#teplo)" opacity=".3"/>')
    s += SL(Z_SRED, stol_bok(0, 820, 1920, 260, t, "#e7dcc4"))
    # блюдце и ложка крупно
    bl = .3 + .7 * abs(A.w(t, 1.8))
    s += SL(Z_PERED, f'<ellipse cx="700" cy="860" rx="330" ry="96" fill="url(#krem)" {o(9)}/>'
            + f'<ellipse cx="700" cy="846" rx="250" ry="70" fill="#f2ead6" {o(5)}/>'
            + f'<g transform="rotate(-14,700,840)">'
            + f'<path d="M700,840 l300,-70" stroke="{ZHELEZ}" stroke-width="30"'
              f' stroke-linecap="round"/>'
            + f'<ellipse cx="660" cy="848" rx="116" ry="74" fill="{ZHELEZ}" {o(8)}/>'
            + f'<ellipse cx="630" cy="824" rx="44" ry="24" fill="#ffffff"'
              f' opacity="{.25+.45*bl:.2f}"/></g>')
    # чашка рядом, пар
    s += SL(Z_PERED, f'<path d="M1320,820 q-10,-140 130,-140 q140,0 130,140 z"'
                     f' fill="#f2eee4" {o(7)}/>'
            + f'<ellipse cx="1450" cy="684" rx="130" ry="32" fill="#8a5a24" {o(5)}/>')
    s += SL(Z_PERED, par(1450, 640, t, 6, .55, 240, .4, 1.3))
    # нижняя часть лица: уголки губ приподнимаются
    ul = A.ease(A.seg(t, 1.4, 1.6))
    s += SL(Z_SRED, f'<path d="M520,0 q440,-40 880,0 v420 q-440,90 -880,0 z"'
                    f' fill="#edc49c" {o(0)}/>'
            + f'<path d="M700,300 q{260:.0f},{40+60*ul:.0f} {520:.0f},0" fill="none"'
              f' stroke="#b9705e" stroke-width="22" stroke-linecap="round"/>'
            + f'<path d="M700,300 q-{20+30*ul:.0f},-{20+30*ul:.0f} -{30:.0f},-{10:.0f}"'
              f' fill="none" stroke="#b9705e" stroke-width="18" stroke-linecap="round"/>'
            + f'<path d="M1220,300 q{20+30*ul:.0f},-{20+30*ul:.0f} {30:.0f},-{10:.0f}"'
              f' fill="none" stroke="#b9705e" stroke-width="18" stroke-linecap="round"/>'
            + f'<ellipse cx="960" cy="140" rx="90" ry="40" fill="#e2a089" opacity=".3"/>')
    s += _vinetka(.5)
    return s


def sunduk_do_svyatok(t):
    """План 120. Сундук с откинутой крышкой: гармонь, фата, ложка, номера."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="{POBEL}"/>'
            + f'<rect x="0" y="{H-300}" width="{W}" height="300" fill="url(#pol)"/>'
            + polovicy(H - 300)
            + f'<rect x="1400" y="120" width="420" height="420" rx="12"'
              f' fill="url(#nrassv)" {o(9)}/>'
            + f'<path d="M1610,120 v420 M1400,330 h420" {o(7)} fill="none"/>')
    s += SL(Z_SRED, luch(1200, 120, 520, 700, t, .2))
    # сундук
    s += SL(Z_SRED, ten(760, 1000, 420, 40, .5)
            + f'<rect x="380" y="700" width="780" height="300" rx="16"'
              f' fill="#6b4a2c" {o(9)}/>'
            + "".join(f'<path d="M{400+j*180},700 v300" stroke="{ZHELEZ}"'
                      f' stroke-width="16" opacity=".9"/>' for j in range(5))
            + f'<path d="M380,700 l-80,-300 h780 l80,300 z" fill="#8a6038" {o(8)}/>')
    # три вещи перед сундуком
    veshi = [
        (320, lambda: f'<rect x="-120" y="-70" width="70" height="140" rx="10"'
                      f' fill="#8a2f2c" {o(6)}/>'
                      f'<rect x="50" y="-70" width="70" height="140" rx="10"'
                      f' fill="#8a2f2c" {o(6)}/>'
                      + "".join(f'<path d="M{-50+j*17},-66 v132" stroke="#e8d9bc"'
                                f' stroke-width="6"/>' for j in range(7))),
        (760, lambda: f'<ellipse cx="0" cy="40" rx="130" ry="40" fill="#efe4d2" {o(6)}/>'
                      f'<path d="M-90,30 q90,-150 180,0 q-90,40 -180,0 z"'
                      f' fill="#fdfaf2" opacity=".9" {o(5)}/>'),
        (1200, lambda: f'<ellipse cx="0" cy="-30" rx="80" ry="54" fill="url(#derev)" {o(7)}/>'
                       f'<rect x="-24" y="10" width="48" height="190" rx="14"'
                       f' fill="url(#derev)" {o(6)}/>'),
    ]
    for i, (xx, f) in enumerate(veshi):
        s += SL(Z_PERED, f'<g transform="translate({xx},880)">' + f() + '</g>')
        k = A.out(A.seg(t, 1.0 + i * .5, .5))
        if k > 0:
            s += SL(Z_PERED, f'<g opacity="{k:.2f}" transform="translate({xx},600)'
                    f' scale({.6+.4*k:.2f})">'
                    + f'<circle cx="0" cy="0" r="66" fill="url(#zol)" {o(6)}/>'
                    + f'<text x="0" y="24" font-family="Georgia,serif" font-size="68"'
                      f' text-anchor="middle" fill="#2a1d08">{i+1}</text></g>')
    # фата колышется, пылинки в луче
    kol = 10 * A.w(t, 1.8)
    s += SL(Z_PERED, f'<path d="M760,890 q{80+kol:.0f},-40 {150:.0f},30" fill="none"'
                     f' stroke="#fdfaf2" stroke-width="16" opacity=".9"/>')
    for i in range(10):
        ph = (t * .2 + i * .1) % 1.0
        s += SL(Z_PERED, f'<circle cx="{1240+i*52-100*ph:.0f}" cy="{200+ph*700:.0f}"'
                         f' r="4" fill="#fff6dc" opacity="{.5*(1-ph):.2f}"/>')
    s += _vinetka(.44)
    return s


def garmon_na_kryshke_sunduka(t):
    """План 121. Гармонь растягивает меха на аккорд и складывается."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#b9a98c"/>'
            + doski(0, 0, W, H, 170, False, "derev")
            + f'<rect x="0" y="0" width="{W}" height="{H}" fill="url(#teplo)" opacity=".22"/>')
    s += SL(Z_SRED, f'<path d="M240,860 l-80,-300 h1440 l80,300 z" fill="#8a6038" {o(9)}/>'
            + f'<rect x="240" y="860" width="1440" height="200" rx="12"'
              f' fill="#6b4a2c" {o(9)}/>')
    # меха: растягиваются и складываются
    rast = A.ease(A.seg(t, .3, .7)) - A.ease(A.seg(t, 1.3, .7))
    shir = 1.0 + 1.1 * max(0.0, rast)
    s += SL(Z_PERED, f'<g transform="translate(960,620) scale({shir:.2f},1)">'
            + f'<rect x="-220" y="-150" width="110" height="300" rx="16"'
              f' fill="#8a2f2c" {o(8)}/>'
            + f'<rect x="110" y="-150" width="110" height="300" rx="16"'
              f' fill="#8a2f2c" {o(8)}/>'
            + "".join(f'<path d="M{-110+j*25},-146 v292" stroke="#e8d9bc"'
                      f' stroke-width="9" opacity=".95"/>' for j in range(9))
            + "".join(f'<circle cx="{-190+j*26}" cy="{-70+j*40}" r="13" fill="#f3e9d2"'
                      f' {o(4)}/>' for j in range(5))
            + '</g>')
    # ремешок застёгивается
    zast = A.out(A.seg(t, 2.1, .4))
    if zast > 0:
        s += SL(Z_PERED, f'<path d="M700,540 h{520*zast:.0f}" stroke="#4a3626"'
                         f' stroke-width="24" stroke-linecap="round"/>'
                + f'<rect x="{700+520*zast-40:.0f}" y="516" width="60" height="48" rx="12"'
                  f' fill="{MED}" {o(5)}/>')
    s += _vinetka(.46)
    return s


def spyaschaya_ulica_v_snegu(t):
    """План 122. Ночная улица, тёмные окна, в одном силуэт набирает воздух."""
    s = SL(Z_NEBO, nebo("noch", t, True))
    s += SL(Z_DAL, f'<path d="M0,700 q960,-120 1920,-40 v420 H0 z" fill="#dce8f4"/>'
            + _sneg_lezhit(700, 30))
    # дома с тёмными окнами
    for i, (xx, w_, hh) in enumerate(((60, 360, 300), (480, 420, 360), (980, 380, 320))):
        s += SL(Z_SRED, izba_snaruzhi(xx, 700 + i * 20, w_, t, False, True, 11 + i))
    # дом на пригорке вдали
    s += SL(Z_DAL, izba_snaruzhi(1560, 560, 260, t, True, True, 23))
    # одно окно с силуэтом: плечи поднимаются
    vdoh = A.ease(A.seg(t, 2.0, 1.8))
    s += SL(Z_SRED, f'<rect x="600" y="440" width="180" height="170" rx="8"'
                    f' fill="{SVET}" opacity=".92" {o(7)}/>'
            + f'<path d="M690,440 v170 M600,525 h180" {o(6)} fill="none"/>'
            + teplo(690, 520, 420, 360, .5))
    s += SL(Z_PERED, f'<g transform="translate(0,{-18*vdoh:.0f})">'
            + spina(690, 612, 210, t, "#2a2430", None, .3, "#f0d894") + '</g>')
    s += SL(Z_LETIT, _sneg_letit(t, 30, 89, .5, .45))
    s += _vinetka(.5)
    return s


def svyatochnaya_gorka(t):
    """План 123. Ледяная горка: санки, гармонист, платки, снежки."""
    s = SL(Z_NEBO, nebo("den", t, False) + oblaka(t, 150, 4, 97, .5))
    s += SL(Z_DAL, f'<rect x="0" y="420" width="{W}" height="{H-420}" fill="url(#sneg)"/>')
    # горка
    s += SL(Z_SRED, f'<path d="M1500,420 q-420,160 -1500,560 v100 h1920 v-660 z"'
                    f' fill="#eaf1fb" {o(7)}/>'
            + f'<path d="M1500,440 q-420,160 -1480,540" fill="none" stroke="{LED}"'
              f' stroke-width="26" opacity=".85"/>')
    # дети на санках летят
    k = (t * .35) % 1.0
    sx = 1420 - k * 1300
    sy = 470 + k * 480
    s += SL(Z_PERED, f'<g transform="translate({sx:.0f},{sy:.0f}) rotate(-16)">'
            + f'<rect x="-90" y="0" width="200" height="26" rx="8" fill="url(#derev)" {o(6)}/>'
            + f'<path d="M-90,26 q-30,30 10,40 h190" fill="none" {o(10)}/>'
            + spina(-20, 0, 160, t, "#8a3f3a", "#d9a441", .2)
            + spina(50, 0, 140, t, "#3f5c7a", "#f6eedc", .6)
            + '</g>')
    # парни тащат гармониста
    s += SL(Z_PERED, f'<g transform="translate(340,980)">'
            + spina(0, 0, 420, t, "#3a4450", None, .1)
            + spina(150, 0, 440, t, "#4a3426", None, .4)
            + f'<g transform="translate(300,-240) scale(.8)">'
            + f'<rect x="-100" y="-70" width="60" height="140" rx="10" fill="#8a2f2c" {o(6)}/>'
            + f'<rect x="40" y="-70" width="60" height="140" rx="10" fill="#8a2f2c" {o(6)}/>'
            + "".join(f'<path d="M{-40+j*16},-66 v132" stroke="#e8d9bc"'
                      f' stroke-width="6"/>' for j in range(6)) + '</g>'
            + spina(320, 0, 430, t, "#6b4a2c", None, .7)
            + '</g>')
    # девушки в цветных платках смеются
    for i, (xx, col) in enumerate(((1120, "#c0392b"), (1260, "#d9a441"), (1400, "#3f5c7a"))):
        kach = 7 * A.w(t, 1.5, i * .3)
        s += SL(Z_PERED, f'<g transform="rotate({kach:.1f},{xx},1020)">'
                + babka(xx, 1020, 400, t, True, col, i * .25, -6, "#f6eedc") + '</g>')
    # летят снежки
    for i in range(3):
        ph = (t * .8 + i * .33) % 1.0
        s += SL(Z_PERED, f'<circle cx="{500+ph*900:.0f}"'
                         f' cy="{700-280*math.sin(ph*3.14):.0f}" r="{22-6*ph:.0f}"'
                         f' fill="#ffffff" {o(4)}/>')
    s += SL(Z_LETIT, _sneg_letit(t, 22, 101, .45, .6))
    s += _vinetka(.42)
    return s


def garmon_na_gvozde(t):
    """План 124. Дед показывает внуку на гармонь высоко на гвозде: потом."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#9a8a6c"/>'
            + doski(0, 0, W, H, 160, False, "derev")
            + f'<rect x="0" y="880" width="{W}" height="200" fill="url(#pol)"/>'
            + polovicy(880))
    # гармонь высоко на гвозде, покачивается
    ang = 4 * A.w(t, 2.3)
    s += SL(Z_SRED, f'<circle cx="1180" cy="140" r="14" fill="{ZHELEZ}" {o(5)}/>')
    s += SL(Z_SRED, f'<g transform="rotate({ang:.1f},1180,140)">'
            + f'<path d="M1180,140 v90" {o(6)} fill="none"/>'
            + f'<g transform="translate(1180,350)">'
            + f'<rect x="-170" y="-120" width="90" height="240" rx="14"'
              f' fill="#8a2f2c" {o(7)}/>'
            + f'<rect x="80" y="-120" width="90" height="240" rx="14"'
              f' fill="#8a2f2c" {o(7)}/>'
            + "".join(f'<path d="M{-80+j*20},-116 v232" stroke="#e8d9bc"'
                      f' stroke-width="8"/>' for j in range(9))
            + '</g></g>')
    # дед в профиль показывает вверх
    s += SL(Z_PERED, muzh(620, 1010, 780, t, .1, "#4a5b4a", True))
    s += SL(Z_PERED, f'<g transform="rotate(-54,720,560)">'
            + ruka(720, 560, t, 250, 0, 52, "#4a5b4a") + '</g>')
    # внук вздыхает
    vzd = 10 * A.w(t, 2.0)
    s += SL(Z_PERED, f'<g transform="translate(0,{vzd*.4:.0f})">'
            + muzh(1420, 1030, 480, t, .5, "#6b4a2c", False) + '</g>')
    s += SL(Z_PERED, par(1380, 700, t, 4, .3, 160, .4, 1.2))
    s += _vinetka(.46)
    return s


def tri_priglasheniya_i_konvert(t):
    """План 125. Три открытки ложатся на стол, рука кладёт их в конверт."""
    s = SL(Z_DAL, kuhnya_stena(t, True, None, False, True, 103))
    s += SL(Z_SRED, stol_bok(60, 740, 1800, 300, t, "#e7dcc4"))
    # ёлочная ветка в вазе
    s += SL(Z_SRED, f'<path d="M1600,700 q-10,-120 90,-120 q100,0 90,120 z"'
                    f' fill="url(#stekl)" opacity=".8" {o(6)}/>')
    for j in range(5):
        ang = 4 * A.w(t, 2.4, j * .2)
        s += SL(Z_SRED, f'<g transform="rotate({ang:.1f},1690,580)">'
                + f'<path d="M1690,580 l{-120+j*60},-{120+j*20}" stroke="{ZEL}"'
                  f' stroke-width="14"/></g>')
    otk = [
        (360, "#c0392b", lambda: "".join(f'<circle cx="{-50+j*50}" cy="-30" r="26"'
                                         f' fill="{["#d9a441","#4a6b86","#e8e4d8"][j%3]}"'
                                         f' {o(4)}/>' for j in range(3))),
        (700, "#4a6b86", lambda: f'<circle cx="0" cy="-30" r="30" fill="url(#zol)" {o(5)}/>'
                                 f'<rect x="-10" y="-10" width="20" height="80" rx="6"'
                                 f' fill="url(#zol)" {o(4)}/>'),
        (1040, "#4a5b4a", lambda: "".join(f'<circle cx="{-40+j*40}" cy="{-10+j*20}" r="18"'
                                          f' fill="#2a2520" {o(3)}/>'
                                          f'<path d="M{-40+j*40+16},{-10+j*20} v-60"'
                                          f' stroke="#2a2520" stroke-width="7"/>'
                                          for j in range(2))),
    ]
    polozh = A.ease(A.seg(t, 3.2, 1.4))
    for i, (xx, col, f) in enumerate(otk):
        k = A.over(A.seg(t, .4 + i * .8, .4))
        if k <= 0:
            continue
        kk = min(1.0, k)
        s += SL(Z_PERED, f'<g opacity="{kk*(1-polozh*.9):.2f}"'
                f' transform="translate({xx+(700-xx)*polozh:.0f},'
                f'{700-60*(1-kk)+120*polozh:.0f}) rotate({-6+i*6+20*polozh:.0f})">'
                + f'<rect x="-130" y="-90" width="260" height="180" rx="12"'
                  f' fill="#fdfaf2" {o(6)}/>'
                + f'<rect x="-130" y="-90" width="260" height="40" rx="10"'
                  f' fill="{col}" opacity=".9"/>' + f() + '</g>')
    # конверт заклеивается
    s += SL(Z_PERED, f'<g transform="translate(700,760)">'
            + f'<rect x="-230" y="-130" width="460" height="260" rx="14"'
              f' fill="#e8ddc6" {o(8)}/>'
            + f'<path d="M-230,-130 l230,150 l230,-150" fill="none" {o(7)}/>'
            + '</g>')
    zakl = A.ease(A.seg(t, 4.6, .8))
    if zakl > 0:
        s += SL(Z_PERED, f'<g transform="translate(700,760) rotate({180*(1-zakl):.0f},0,-130)">'
                + f'<path d="M-230,-130 l230,150 l230,-150 z" fill="#d8cdb4" {o(6)}/></g>')
    s += SL(Z_PERED, ruka(100, 920, t, 260, -18, 54, "#6b5a6e"))
    s += _vinetka(.44)
    return s


def divan_chaynik_i_pirog(t):
    """План 126. Трое на диване у столика: пирог, чайник под грелкой, кот."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#4a4036"/>'
            + f'<rect x="0" y="0" width="{W}" height="{H}" fill="url(#teplo)" opacity=".25"/>'
            + f'<rect x="0" y="860" width="{W}" height="220" fill="url(#pol)"/>'
            + polovicy(860))
    # бра на стене
    mer = .85 + .15 * A.w(t, 2.8)
    s += SL(Z_DAL, f'<path d="M1700,300 q60,-70 120,0 z" fill="#f0d08a"'
                   f' opacity="{mer:.2f}" {o(6)}/>'
            + teplo(1760, 340, 620, 520, .5 * mer))
    # диван
    s += SL(Z_SRED, f'<rect x="140" y="560" width="1200" height="300" rx="20"'
                    f' fill="#5e4a42" {o(9)}/>'
            + f'<rect x="180" y="500" width="1120" height="180" rx="18"'
              f' fill="#6b5a4a" {o(7)}/>'
            + f'<rect x="100" y="620" width="90" height="240" rx="16"'
              f' fill="#4a3a32" {o(7)}/>'
            + f'<rect x="1290" y="620" width="90" height="240" rx="16"'
              f' fill="#4a3a32" {o(7)}/>')
    # трое родных
    s += SL(Z_SRED, babka(400, 830, 540, t, True, "#8a3f3a", .1, -6))
    s += SL(Z_SRED, muzh(740, 830, 560, t, .3, "#3f5c7a", True))
    s += SL(Z_SRED, babka(1080, 830, 520, t, True, "#5e6b7a", .5, -4, "#4a5b4a", False))
    # мягкие облачка слов
    for i in range(3):
        ph = (t * .3 + i * .33) % 1.0
        s += SL(Z_PERED, f'<ellipse cx="{420+i*340}" cy="{420-ph*120:.0f}"'
                         f' rx="{54+20*ph:.0f}" ry="{34+12*ph:.0f}" fill="#fdfaf2"'
                         f' opacity="{.5*(1-ph):.2f}"/>')
    # низкий столик: пирог, чайник под грелкой, чашки
    s += SL(Z_PERED, f'<rect x="300" y="900" width="900" height="30" rx="10"'
                     f' fill="url(#dosk)" {o(7)}/>')
    s += SL(Z_PERED, f'<path d="M360,896 q10,-110 130,-110 q120,0 130,110 z"'
                     f' fill="url(#solom)" {o(7)}/>'
            + f'<path d="M400,840 q90,-26 180,0" fill="none" stroke="#c08a3e"'
              f' stroke-width="9"/>')
    s += SL(Z_PERED, f'<path d="M740,896 q-20,-160 150,-160 q170,0 150,160 z"'
                     f' fill="{TKAN}" {o(7)}/>'
            + f'<circle cx="890" cy="740" r="30" fill="#d9a441" {o(5)}/>')
    for i in range(2):
        s += SL(Z_PERED, f'<path d="M{1060+i*90},896 q-6,-70 54,-70 q60,0 54,70 z"'
                         f' fill="#f2eee4" {o(5)}/>'
                + par(1114 + i * 90, 816, t, 4, .45, 170, .45, .9))
    # кот на подлокотнике
    s += SL(Z_PERED, kot(1335, 620, t, 1.0, "#3b3430", True))
    s += _vinetka(.48)
    return s


def fata_v_krugloy_korobke(t):
    """План 127. Фата опускается в коробку, сверху веночек, крышка."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#cbb79c"/>'
            + doski(0, 0, W, H, 160, False, "dosk")
            + f'<rect x="0" y="0" width="{W}" height="{H}" fill="url(#teplo)" opacity=".2"/>')
    s += SL(Z_SRED, f'<rect x="60" y="820" width="1800" height="34" rx="10"'
                    f' fill="url(#dosk)" {o(8)}/>')
    # круглая коробка
    s += SL(Z_SRED, ten(960, 844, 330, 34, .5)
            + f'<ellipse cx="960" cy="800" rx="330" ry="90" fill="#e5d9c6" {o(8)}/>'
            + f'<rect x="630" y="600" width="660" height="200" fill="#e5d9c6" {o(8)}/>'
            + f'<ellipse cx="960" cy="600" rx="330" ry="90" fill="#d8cbb4" {o(7)}/>')
    # фата оседает в коробку
    os_ = A.ease(A.seg(t, .2, 1.2))
    s += SL(Z_PERED, f'<g opacity="{1-os_*.25:.2f}" transform="translate(0,{320*os_:.0f})">'
            + f'<path d="M700,300 q260,-180 520,0 q-120,160 -260,170 q-140,-10 -260,-170 z"'
              f' fill="#fdfaf2" opacity=".9" {o(6)}/>'
            + "".join(f'<path d="M{760+j*90},320 q20,70 -10,130" fill="none"'
                      f' stroke="#efe9da" stroke-width="9"/>' for j in range(5)) + '</g>')
    # веночек ложится сверху
    ven = A.ease(A.seg(t, 1.6, .9))
    if ven > 0:
        s += SL(Z_PERED, f'<g opacity="{ven:.2f}" transform="translate(960,{400+200*ven:.0f})">'
                + f'<ellipse cx="0" cy="0" rx="170" ry="54" fill="none" stroke="{ZEL}"'
                  f' stroke-width="24"/>'
                + "".join(f'<circle cx="{math.cos(j*.8)*170:.0f}"'
                          f' cy="{math.sin(j*.8)*54:.0f}" r="16" fill="#f6eedc" {o(3)}/>'
                          for j in range(8)) + '</g>')
    # крышка закрывается
    kr = A.ease(A.seg(t, 2.4, 1.0))
    s += SL(Z_PERED, f'<g transform="translate(0,{-420*(1-kr):.0f})">'
            + f'<ellipse cx="960" cy="580" rx="348" ry="96" fill="#efe4d2" {o(8)}/>'
            + f'<ellipse cx="960" cy="556" rx="290" ry="74" fill="#f7eeda" opacity=".85"/>'
            + '</g>')
    s += _vinetka(.46)
    return s


def kolca_pod_salfetkoy_i_chepchik(t):
    """План 128. Кольца накрывают салфеткой, на стуле рубашечка и чепчик."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#d8c9ac"/>'
            + f'<rect x="0" y="0" width="{W}" height="360" fill="#c6b79c"/>'
            + f'<rect x="0" y="880" width="{W}" height="200" fill="url(#pol)"/>'
            + polovicy(880))
    # комод с блюдцем и кольцами
    s += SL(Z_SRED, f'<rect x="80" y="620" width="700" height="300" rx="14"'
                    f' fill="#8a6038" {o(9)}/>'
            + f'<rect x="110" y="660" width="640" height="110" rx="10"'
              f' fill="#7a5230" {o(5)}/>'
            + f'<circle cx="430" cy="715" r="20" fill="{MED}" {o(5)}/>')
    s += SL(Z_PERED, f'<ellipse cx="430" cy="600" rx="170" ry="48" fill="url(#krem)" {o(7)}/>')
    for j in range(2):
        s += SL(Z_PERED, f'<circle cx="{390+j*80}" cy="588" r="34" fill="none"'
                         f' stroke="url(#zol)" stroke-width="13"/>')
    # салфетка ложится на блюдце
    k = A.ease(A.seg(t, .4, 1.0))
    s += SL(Z_PERED, f'<g opacity="{k:.2f}" transform="translate(0,{-200*(1-k):.0f})">'
            + f'<path d="M270,570 h320 q20,70 -160,86 q-180,-16 -160,-86 z"'
              f' fill="#fdfaf2" {o(6)}/>'
            + f'<path d="M290,600 h280" stroke="#e2dccc" stroke-width="8"/></g>')
    # стул с рубашечкой и чепчиком
    s += SL(Z_SRED, f'<rect x="1180" y="760" width="300" height="34" rx="9"'
                    f' fill="url(#derev)" {o(7)}/>'
            + f'<rect x="1180" y="420" width="34" height="344" rx="10"'
              f' fill="url(#derev)" {o(6)}/>'
            + f'<rect x="1446" y="420" width="34" height="344" rx="10"'
              f' fill="url(#derev)" {o(6)}/>'
            + f'<rect x="1180" y="430" width="300" height="26" rx="8"'
              f' fill="url(#derev)" {o(6)}/>')
    kr = A.out(A.seg(t, 1.6, .8))
    if kr > 0:
        kol = 7 * A.w(t, 1.9)
        s += SL(Z_PERED, f'<g opacity="{kr:.2f}">'
                + f'<path d="M1230,460 q100,-50 200,0 l{20+kol:.0f},180'
                  f' q-110,34 -240,0 z" fill="#fdfaf2" {o(6)}/>'
                + "".join(f'<path d="M{1250+j*50},470 v170" stroke="#efe9da"'
                          f' stroke-width="7"/>' for j in range(4))
                + f'<path d="M1560,520 q70,-70 140,-10 q-30,60 -140,10 z"'
                  f' fill="#fdfaf2" {o(6)}/>'
                + f'<path d="M1580,540 q60,-40 110,-6" fill="none" stroke="#e2dccc"'
                  f' stroke-width="8"/></g>')
    # руки расправляют чепчик
    kp = A.ease(A.seg(t, 2.4, 1.0))
    s += SL(Z_PERED, f'<g opacity="{kp:.2f}">'
            + ruka(1760, 700, t, 230, 186, 48, "#6b5a6e") + '</g>')
    s += _vinetka(.44)
    return s


def svadebnyy_stol_v_post(t):
    """Планы 129-130. Свадебный стол с капустой, гармонь закрыта."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="{POBEL}"/>'
            + f'<rect x="0" y="880" width="{W}" height="200" fill="url(#pol)"/>'
            + polovicy(880)
            + f'<rect x="0" y="0" width="{W}" height="{H}" fill="url(#teplo)" opacity=".2"/>')
    # длинный стол под белой скатертью
    s += SL(Z_SRED, f'<path d="M20,620 h1880 l-40,240 h-1800 z" fill="#fdfaf2" {o(8)}/>'
            + f'<path d="M40,700 h1840" stroke="#e8e2d4" stroke-width="10"/>')
    # блюда: капуста и огурцы вместо жаркого
    for i in range(5):
        xx = 220 + i * 360
        s += SL(Z_PERED, f'<ellipse cx="{xx}" cy="640" rx="130" ry="40"'
                         f' fill="url(#krem)" {o(6)}/>'
                + (f'<ellipse cx="{xx}" cy="620" rx="100" ry="28" fill="#9ab07e" {o(4)}/>'
                   if i % 2 == 0 else
                   "".join(f'<ellipse cx="{xx-50+j*46}" cy="616" rx="28" ry="14"'
                           f' fill="{ZEL}" {o(4)}/>' for j in range(3))))
    # гости-силуэты переглядываются
    pov = 5 * A.w(t, 1.3)
    s += SL(Z_SRED, f'<g transform="rotate({pov:.1f},620,620)">'
            + babka(620, 620, 420, t, True, "#fdfaf2", .1, -4, "#f6eedc") + '</g>')
    s += SL(Z_SRED, f'<g transform="rotate({-pov:.1f},860,620)">'
            + muzh(860, 620, 440, t, .3, "#2f3845", False) + '</g>')
    for i, xx in enumerate((300, 1180, 1420, 1660)):
        s += SL(Z_SRED, spina(xx, 620, 400 + i * 10, t, "#4a4152",
                              "#8a3f3a" if i % 2 == 0 else None, i * .23))
    # лента на стуле качается
    kol = 10 * A.w(t, 1.7)
    s += SL(Z_PERED, f'<path d="M1020,600 q{40+kol:.0f},100 {10:.0f},200" fill="none"'
                     f' stroke="{TKAN}" stroke-width="22" opacity=".9"/>')
    # гармонист барабанит пальцами по закрытой гармони
    bar = 8 * abs(A.w(t, .45))
    s += SL(Z_PERED, f'<g transform="translate(1540,940)">'
            + f'<rect x="-150" y="-120" width="300" height="200" rx="18"'
              f' fill="#3b4150" {o(8)}/>'
            + f'<path d="M-120,-110 h240" stroke="#2a2f3a" stroke-width="10"/>'
            + f'<g transform="translate(0,{-bar:.0f})">'
            + "".join(f'<ellipse cx="{-60+j*44}" cy="-130" rx="17" ry="24"'
                      f' fill="#e8bb93" {o(4)}/>' for j in range(3)) + '</g></g>')
    s += _vinetka(.44)
    return s


def svatovstvo_u_stola(t):
    """План 132. Отцы бьют по рукам, мать накрывает руки полотенцем."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="{POBEL}"/>'
            + f'<rect x="1420" y="160" width="420" height="380" rx="10"'
              f' fill="url(#nden)" {o(9)}/>'
            + f'<path d="M1630,160 v380 M1420,350 h420" {o(7)} fill="none"/>'
            + f'<rect x="0" y="900" width="{W}" height="180" fill="url(#pol)"/>'
            + polovicy(900))
    s += SL(Z_SRED, teplo(860, 600, 900, 600, .45))
    # два отца по сторонам стола
    s += SL(Z_SRED, muzh(420, 1000, 780, t, .1, "#4a5b4a", True))
    s += SL(Z_SRED, muzh(1300, 1000, 790, t, .4, "#5e4a42", False))
    # мать за столом
    s += SL(Z_SRED, babka(880, 980, 700, t, True, TKAN, .2, -10))
    # стол
    s += SL(Z_PERED, f'<path d="M60,{H} v-180 q860,-80 1800,0 v180 z"'
                     f' fill="#b08456" {o(8)}/>')
    # руки ударяют по рукам
    udar = abs(A.w(t, .8))
    s += SL(Z_PERED, f'<g transform="translate(0,{-24*udar:.0f})">'
            + ruka(520, 820, t, 260, -16, 56, "#4a5b4a") + '</g>')
    s += SL(Z_PERED, f'<g transform="translate(0,{24*udar:.0f})">'
            + ruka(1400, 800, t, 260, 194, 56, "#5e4a42") + '</g>')
    # полотенце накрывает руки
    k = A.ease(A.seg(t, 1.4, 1.2))
    s += SL(Z_PERED, f'<g opacity="{k:.2f}" transform="translate(0,{-160*(1-k):.0f})">'
            + f'<path d="M740,800 h420 q20,110 -210,130 q-230,-20 -210,-130 z"'
              f' fill="url(#rush)" {o(6)}/>'
            + f'<path d="M760,860 h380" stroke="{TKAN}" stroke-width="10" opacity=".8"/></g>')
    # отец загибает пальцы, считая недели
    n = min(6, int(A.seg(t, 2.8, 2.0) * 6.99))
    for j in range(6):
        sogn = j < n
        s += SL(Z_PERED, f'<path d="M{300+j*6},{640-j*14} q{26 if not sogn else 8},'
                         f'{-6 if not sogn else 14} {38 if not sogn else 12},'
                         f'{2 if not sogn else 24}" fill="none" stroke="#e8bb93"'
                         f' stroke-width="14" stroke-linecap="round"/>')
    s += _vinetka(.46)
    return s


def portnovskiy_maneken(t):
    """Планы 133-134. Манекен с намётанным платьем, список и календарик."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#cfc4ac"/>'
            + doski(0, 0, W, 460, 150, False, "dosk")
            + f'<rect x="0" y="860" width="{W}" height="220" fill="url(#pol)"/>'
            + polovicy(860))
    # манекен
    s += SL(Z_SRED, ten(1340, 1000, 180, 30, .5)
            + f'<rect x="1316" y="800" width="48" height="200" rx="12"'
              f' fill="{ZHELEZ}" {o(7)}/>'
            + f'<ellipse cx="1340" cy="1000" rx="130" ry="30" fill="{ZHELEZ}" {o(6)}/>'
            + f'<path d="M1200,800 q-30,-300 140,-320 q170,20 140,320 z"'
              f' fill="#e8e4d8" {o(8)}/>')
    # намётанное белое платье с булавками
    s += SL(Z_PERED, f'<path d="M1180,820 q-40,-250 90,-290'
                     f' q70,-26 140,0 q130,40 90,290 q-160,44 -320,0 z"'
                     f' fill="#fdfaf2" opacity=".96" {o(7)}/>'
            # плечи и рукава
            + f'<path d="M1250,536 q-96,20 -120,120 q50,26 86,-16 z"'
              f' fill="#fdfaf2" {o(6)}/>'
            + f'<path d="M1430,536 q96,20 120,120 q-50,26 -86,-16 z"'
              f' fill="#fdfaf2" {o(6)}/>'
            # юбка колоколом и намётка
            + f'<path d="M1200,790 q140,60 280,0 l40,230 q-180,54 -360,0 z"'
              f' fill="#fdfaf2" opacity=".96" {o(7)}/>'
            + "".join(f'<path d="M{1216+j*42},560 v440" stroke="#d8d2c4"'
                      f' stroke-width="5" opacity=".85"/>' for j in range(7))
            + f'<path d="M1200,790 q140,56 280,0" fill="none" stroke="#c9c2b2"'
              f' stroke-width="7"/>')
    for j in range(6):
        bl = .4 + .6 * abs(A.w(t, 1.7, j * .2))
        s += SL(Z_PERED, f'<circle cx="{1230+j*42}" cy="{600+(j%3)*60}" r="7"'
                         f' fill="#e8ecee" opacity="{bl:.2f}" {o(2)}/>')
    # сантиметр на шее покачивается
    ang = 5 * A.w(t, 2.1)
    s += SL(Z_PERED, f'<g transform="rotate({ang:.1f},1340,480)">'
            + f'<path d="M1270,480 q70,80 140,0" fill="none" stroke="#e8c84a"'
              f' stroke-width="14"/>'
            + f'<path d="M1270,480 v260 M1410,480 v230" stroke="#e8c84a"'
              f' stroke-width="14"/></g>')
    # стол со списком гостей и календариком
    s += SL(Z_SRED, f'<rect x="60" y="720" width="900" height="40" rx="10"'
                    f' fill="url(#dosk)" {o(8)}/>')
    k1 = A.out(A.seg(t, .5, .6))
    if k1 > 0:
        s += SL(Z_PERED, f'<g opacity="{k1:.2f}">'
                + f'<rect x="140" y="440" width="380" height="280" rx="10"'
                  f' fill="#fdfaf2" {o(6)}/>'
                + "".join(f'<path d="M180,{490+j*42} h{200+j*20}" stroke="#8a8274"'
                          f' stroke-width="7" opacity=".8"/>' for j in range(5)) + '</g>')
    k2 = A.out(A.seg(t, 1.4, .6))
    if k2 > 0:
        s += SL(Z_PERED, f'<g opacity="{k2:.2f}">'
                + f'<rect x="580" y="500" width="320" height="220" rx="10"'
                  + f' fill="#f6eedc" {o(6)}/>'
                + "".join(f'<path d="M{610+c*42},{550+r_*42} h30" stroke="#b9b2a2"'
                          f' stroke-width="8"/>' for r_ in range(4) for c in range(6))
                + '</g>')
    # карандаш обводит день
    kp = A.seg(t, 2.4, 1.2)
    if kp > 0:
        s += SL(Z_PERED, f'<circle cx="736" cy="634" r="{30*kp:.0f}" fill="none"'
                         f' stroke="{KRAS}" stroke-width="9" opacity=".9"/>'
                + f'<path d="M800,560 l140,-120" stroke="#6b4a2c" stroke-width="16"'
                  f' stroke-linecap="round"/>')
    s += _vinetka(.44)
    return s


def kuhnya_v_sochelnik_utrom(t):
    """План 136. Плита в кастрюлях, детская рука получает шлепок полотенцем."""
    s = SL(Z_DAL, kuhnya_stena(t, True, 1480, False, True, 107))
    s += SL(Z_SRED, f'<rect x="60" y="660" width="1180" height="320" rx="16"'
                    f' fill="url(#zhel)" {o(8)}/>')
    for i in range(4):
        xx = 220 + i * 290
        s += SL(Z_SRED, f'<path d="M{xx-120},660 q-20,-160 120,-160 q140,0 120,160 z"'
                        f' fill="{"url(#chug)" if i%2 else "#e9eef0"}" {o(7)}/>'
                + f'<ellipse cx="{xx}" cy="502" rx="124" ry="30" fill="{ZHELEZ}" {o(6)}/>')
    # завитки запаха тянутся к детской руке
    for i in range(5):
        ph = (t * .4 + i * .2) % 1.0
        xx = 300 + i * 260 + 120 * math.sin(ph * 4)
        s += SL(Z_PERED, f'<path d="M{xx:.0f},{470-ph*200:.0f} q34,-44 0,-88'
                         f' q-34,-44 0,-88" fill="none" stroke="#efe2c4"'
                         f' stroke-width="{10-5*ph:.0f}" opacity="{.5*(1-ph):.2f}"/>')
    # детская рука тянется к крышке
    k = A.ease(A.seg(t, .4, 1.0))
    shlep = A.out(A.seg(t, 1.8, .3))
    s += SL(Z_PERED, f'<g transform="translate({200*k-120*shlep:.0f},{-60*k:.0f})">'
            + ruka(1480, 700, t, 240, 182, 44, "#8a6a52") + '</g>')
    # крышка подпрыгивает
    pr = 14 * abs(A.w(t, .8))
    s += SL(Z_PERED, f'<g transform="translate(0,{-pr:.0f})">'
            + f'<ellipse cx="510" cy="492" rx="126" ry="30" fill="{ZHELEZ}" {o(6)}/>'
            + f'<circle cx="510" cy="462" r="18" fill="{CHUGUN}" {o(4)}/></g>')
    # полотенце шлёпает
    if shlep > 0:
        s += SL(Z_PERED, f'<g opacity="{shlep:.2f}" transform="rotate({-30+60*shlep:.0f},1700,560)">'
                + f'<path d="M1700,560 q-120,90 -300,120 q140,-90 300,-120 z"'
                  f' fill="url(#rush)" {o(6)}/></g>')
    s += _vinetka(.44)
    return s


def tri_nosa_na_stekle(t):
    """Планы 137, 138, 170. Трое детей прижались к стеклу изнутри."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#1b2336"/>'
            + sneg_letit(t, 26, 109, .55, .6))
    # бревенчатая стена дома снаружи
    s += SL(Z_DAL, brevna(0, 0, W, H, 92, 0))
    s += SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#101828" opacity=".5"/>')
    # окно изнутри светится (в левой полосе — справа окно вставки)
    s += SL(Z_SRED, f'<rect x="60" y="180" width="740" height="640" rx="14"'
                    f' fill="#f0d894" {o(10)}/>'
            + f'<path d="M430,180 v640 M60,500 h740" {o(9)} fill="none"/>'
            + f'<rect x="20" y="140" width="820" height="60" rx="12"'
              f' fill="url(#dosk)" {o(8)}/>'
            + f'<path d="M20,170 q410,-60 820,0 q-410,36 -820,0 z" fill="{SNEG}" {o(5)}/>')
    s += SL(Z_SRED, teplo(430, 500, 700, 620, .5))
    # трое детей: головы, шапки, расплющенные о стекло носы
    for i, (xx, yy, sc, shapka) in enumerate(((190, 430, .95, "#c0392b"),
                                              (430, 470, 1.08, "#4a6b86"),
                                              (665, 440, .88, "#d9a441"))):
        glaz = 7 * A.w(t, 1.6, i * .3)
        s += SL(Z_PERED, f'<g transform="translate({xx},{yy}) scale({sc:.2f})">'
                # голова и прижатая к стеклу щека
                + f'<ellipse cx="0" cy="0" rx="118" ry="132" fill="#2a2430" opacity=".9"/>'
                + f'<ellipse cx="6" cy="14" rx="96" ry="104" fill="#3a3038" opacity=".9"/>'
                # нос, расплющенный о стекло
                + f'<ellipse cx="0" cy="46" rx="52" ry="30" fill="#4a3f44" opacity=".95"/>'
                + f'<ellipse cx="0" cy="40" rx="30" ry="16" fill="#5e5058" opacity=".9"/>'
                # глаза горят тёплым светом из комнаты
                + f'<ellipse cx="{-42+glaz:.0f}" cy="-20" rx="24" ry="17" fill="#f6e2a8"'
                  f' opacity=".95"/>'
                + f'<circle cx="{-42+glaz*1.4:.0f}" cy="-20" r="9" fill="#2a2430"/>'
                + f'<ellipse cx="{42+glaz:.0f}" cy="-20" rx="24" ry="17" fill="#f6e2a8"'
                  f' opacity=".95"/>'
                + f'<circle cx="{42+glaz*1.4:.0f}" cy="-20" r="9" fill="#2a2430"/>'
                # шапка с помпоном
                + f'<path d="M-112,-44 q14,-110 112,-104 q100,6 112,104'
                  f' q-112,-40 -224,0 z" fill="{shapka}" {o(5)}/>'
                + f'<rect x="-118" y="-56" width="236" height="34" rx="16"'
                  f' fill="{shapka}" {o(5)}/>'
                + f'<circle cx="0" cy="-158" r="26" fill="#f6eedc" {o(4)}/>'
                + '</g>')
        # туманный кружок от дыхания растёт и тает
        ph = (t * .5 + i * .3) % 1.0
        s += SL(Z_PERED, f'<ellipse cx="{xx}" cy="{yy+110}" rx="{60+70*ph:.0f}"'
                         f' ry="{40+50*ph:.0f}" fill="#ffffff" opacity="{.35*(1-ph):.2f}"/>')
    s += _vinetka(.5)
    return s


def ded_s_vnukom_pod_zvezdoy(t):
    """План 140. Дед держит внука и показывает на звезду над сараем."""
    s = SL(Z_NEBO, nebo("sumer", t, True))
    s += SL(Z_DAL, f'<path d="M0,760 q960,-150 1920,-60 v380 H0 z" fill="#dce8f4"/>')
    # сарай и дом
    s += SL(Z_DAL, izba_snaruzhi(1200, 760, 420, t, True, True, 113))
    s += SL(Z_SRED, f'<rect x="60" y="560" width="520" height="300" rx="10"'
                    f' fill="url(#brev)" {o(9)}/>'
            + brevna(60, 560, 520, 300, 74)
            + f'<path d="M40,560 l280,-140 l280,140 z" fill="url(#dosk)" {o(9)}/>')
    # крыльцо
    s += SL(Z_SRED, f'<path d="M620,1080 h520 l-60,-180 h-400 z" fill="url(#dosk)" {o(8)}/>'
            + f'<path d="M660,900 h440" stroke="{DOSKA2}" stroke-width="10"/>')
    # звезда над крышей сарая мерцает
    mer = .75 + .25 * A.w(t, 1.1)
    s += SL(Z_NEBO, f'<circle cx="320" cy="250" r="12" fill="#ffffff" opacity="{mer:.2f}"/>'
            + f'<circle cx="320" cy="250" r="90" fill="url(#holod)" opacity="{.8*mer:.2f}"/>'
            + "".join(f'<path d="M320,250 l{dx*80:.0f},{dy*80:.0f}" stroke="#dff0ff"'
                      f' stroke-width="4" opacity="{.6*mer:.2f}"/>'
                      for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))))
    # дед в профиль держит внука
    s += SL(Z_PERED, muzh(900, 1010, 820, t, .1, "#4a3a2c", True))
    s += SL(Z_PERED, f'<g transform="translate(140,-280)">'
            + babka(900, 1010, 380, t, True, "#8a3f3a", .4, -34, "#c0392b") + '</g>')
    # внук тянет руку вверх
    tyan = A.ease(A.seg(t, 1.2, 1.4))
    s += SL(Z_PERED, f'<g transform="rotate({-50-20*tyan:.0f},1020,560)">'
            + ruka(1020, 560, t, 200, 0, 42, "#c0392b") + '</g>')
    # дед показывает пальцем вверх
    s += SL(Z_PERED, f'<g transform="rotate(-62,980,620)">'
            + ruka(980, 620, t, 240, 0, 50, "#4a3a2c") + '</g>')
    s += SL(Z_PERED, par(860, 680, t, 5, .4, 180, .3, 1.3))
    s += SL(Z_LETIT, _sneg_letit(t, 22, 117, .45, .5))
    s += _vinetka(.48)
    return s


def balkon_vysokogo_etazha_v_snegu(t):
    """Планы 141, 143. Женщина с внуком на снежном балконе ищут звезду."""
    s = SL(Z_NEBO, nebo("noch", t, True))
    # огни двора внизу мигают
    for i in range(16):
        mig = .4 + .6 * abs(A.w(t, 2.4 + i * .1, i * .13))
        s += SL(Z_DAL, f'<rect x="{60+i*118}" y="{880+(i%3)*50}" width="26" height="22"'
                       f' rx="5" fill="{SVET}" opacity="{mig*.8:.2f}"/>')
    s += SL(Z_DAL, f'<rect x="0" y="840" width="{W}" height="240" fill="#1b2130" opacity=".9"/>')
    # перила балкона в снегу
    s += SL(Z_SRED, f'<rect x="0" y="760" width="{W}" height="36" rx="10"'
                    f' fill="{ZHELEZ}" {o(8)}/>'
            + "".join(f'<path d="M{60+j*120},796 v180" stroke="{ZHELEZ}"'
                      f' stroke-width="14"/>' for j in range(16))
            + f'<path d="M0,756 q960,-40 1920,0 q-960,26 -1920,0 z" fill="{SNEG}" {o(5)}/>')
    # женщина с внуком
    s += SL(Z_PERED, babka(700, 1080, 800, t, True, "#5e6b7a", .2, -40))
    s += SL(Z_PERED, f'<g transform="translate(300,-40)">'
            + muzh(700, 1080, 540, t, .5, "#8a3f3a", True) + '</g>')
    # шапка внука
    s += SL(Z_PERED, f'<path d="M940,620 q60,-80 130,-10 q-60,40 -130,10 z"'
                     f' fill="#c0392b" {o(6)}/>'
            + f'<circle cx="1010" cy="586" r="24" fill="#f6eedc" {o(5)}/>')
    # рука показывает вверх
    s += SL(Z_PERED, f'<g transform="rotate(-66,820,620)">'
            + ruka(820, 620, t, 240, 0, 50, "#5e6b7a") + '</g>')
    s += SL(Z_PERED, par(760, 700, t, 5, .4, 180, .3, 1.3))
    s += SL(Z_LETIT, _sneg_letit(t, 26, 121, .5, .5))
    s += _vinetka(.5)
    return s


def komnata_s_vyklyuchatelem(t):
    """План 142. Рука щёлкает выключателем, в окне проступает звезда."""
    gas = A.ease(A.seg(t, .6, .9))
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#3a3a44"/>'
            + f'<rect x="0" y="0" width="{W}" height="{H}" fill="#b9ad96"'
              f' opacity="{(1-gas)*.75:.2f}"/>')
    # окно становится ярче
    s += SL(Z_DAL, f'<rect x="820" y="140" width="820" height="620" rx="14"'
                   f' fill="url(#nnoch)" {o(10)}/>'
            + f'<rect x="820" y="140" width="820" height="620" rx="14"'
              f' fill="#5e6b84" opacity="{(1-gas)*.5:.2f}"/>'
            + f'<path d="M1230,140 v620 M820,450 h820" {o(8)} fill="none"/>')
    # крыши и антенны в окне
    s += SL(Z_DAL, f'<path d="M840,640 h300 l60,-80 h200 l40,80 h200 v120 h-800 z"'
                   f' fill="#1b2130" opacity=".92"/>'
            + "".join(f'<path d="M{900+j*170},560 v-90 M{880+j*170},500 h40"'
                      f' stroke="#2a3140" stroke-width="7"/>' for j in range(4)))
    # звезда проступает
    zv = A.ease(A.seg(t, 1.4, 1.4)) * gas
    if zv > 0:
        mer = .8 + .2 * A.w(t, 1.2)
        s += SL(Z_DAL, f'<circle cx="1420" cy="300" r="{10*zv:.0f}" fill="#ffffff"'
                       f' opacity="{zv*mer:.2f}"/>'
                + f'<circle cx="1420" cy="300" r="{90*zv:.0f}" fill="url(#holod)"'
                  f' opacity="{zv*.85:.2f}"/>'
                + "".join(f'<path d="M1420,300 l{dx*70*zv:.0f},{dy*70*zv:.0f}"'
                          f' stroke="#dff0ff" stroke-width="4" opacity="{.6*zv:.2f}"/>'
                          for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))))
    # люстра гаснет
    s += SL(Z_SRED, f'<g opacity="{1-gas:.2f}">' + lampa(500, 260, t, 2.0, True)
            + teplo(500, 420, 700, 560, .5) + '</g>')
    # рука на выключателе
    s += SL(Z_PERED, f'<rect x="120" y="560" width="120" height="160" rx="14"'
                     f' fill="#e8e4d8" {o(7)}/>'
            + f'<rect x="150" y="{600+30*gas:.0f}" width="60" height="70" rx="10"'
              f' fill="#cfc9bc" {o(5)}/>')
    s += SL(Z_PERED, ruka(60, 800, t, 230, -46, 50, "#6b5a6e"))
    s += _vinetka(.5)
    return s


def elka_v_uglu_komnaty(t):
    """Планы 144, 146, 153. Смена главы: наряженная ёлка в углу комнаты."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#d8cdb4"/>'
            + f'<rect x="0" y="0" width="{W}" height="{H}" fill="url(#teplo)" opacity=".25"/>'
            + f'<rect x="0" y="860" width="{W}" height="220" fill="url(#pol)"/>'
            + polovicy(860))
    # угол комнаты
    s += SL(Z_DAL, f'<path d="M1180,0 v860" stroke="#b9ad96" stroke-width="14" opacity=".7"/>')
    # ёлка
    s += SL(Z_SRED, ten(700, 880, 300, 36, .5))
    for i in range(5):
        yy = 840 - i * 150
        w_ = 420 - i * 70
        s += SL(Z_SRED, f'<path d="M{700-w_},{yy} q{w_},-{90+i*10:.0f} {w_*2},0 z"'
                        f' fill="{"#2f5e34" if i%2 else "#3c6b3a"}" {o(7)}/>')
    s += SL(Z_SRED, f'<rect x="676" y="840" width="48" height="60" rx="8"'
                    f' fill="url(#derev)" {o(6)}/>')
    # шары покачиваются
    for i in range(9):
        ang = 5 * A.w(t, 1.8, i * .17)
        xx = 560 + (i % 3) * 140 + (i // 3) * 20
        yy = 740 - (i // 3) * 150
        s += SL(Z_PERED, f'<g transform="rotate({ang:.1f},{xx},{yy-30})">'
                + f'<path d="M{xx},{yy-30} v24" {o(3)} fill="none"/>'
                + f'<circle cx="{xx}" cy="{yy+8}" r="30"'
                  f' fill="{["#c0392b","#d9a441","#4a6b86"][i%3]}" {o(5)}/>'
                + f'<ellipse cx="{xx-10}" cy="{yy-2}" rx="10" ry="6" fill="#ffffff"'
                  f' opacity=".5"/></g>')
    # гирлянда мигает
    for i in range(14):
        mig = .3 + .7 * abs(A.w(t, 1.4, i * .12))
        xx = 520 + (i * 97) % 380
        yy = 420 + (i * 53) % 420
        s += SL(Z_PERED, f'<circle cx="{xx}" cy="{yy}" r="12"'
                         f' fill="{["#f0d08a","#d9534a","#6bbf59","#4a9bd8"][i%4]}"'
                         f' opacity="{mig:.2f}"/>'
                + f'<circle cx="{xx}" cy="{yy}" r="30" fill="url(#teplo)"'
                  f' opacity="{mig*.5:.2f}"/>')
    # дождик блестит
    for i in range(10):
        bl = .3 + .7 * abs(A.w(t, 2.2, i * .2))
        s += SL(Z_PERED, f'<path d="M{540+i*34},{480+(i%4)*90} l-20,80" stroke="#e8e4d8"'
                         f' stroke-width="5" opacity="{bl*.8:.2f}"/>')
    # вата под ёлкой
    s += SL(Z_PERED, f'<path d="M420,900 q280,-70 560,0 q-280,54 -560,0 z"'
                     f' fill="#fdfaf2" {o(5)}/>')
    s += _vinetka(.44)
    return s


def novogodniy_postnyy_stol(t):
    """Планы 147, 148, 154, 155. Белая скатерть, хрусталь, заливная рыба."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#c6b79c"/>'
            + f'<rect x="0" y="0" width="{W}" height="{H}" fill="url(#teplo)" opacity=".25"/>')
    s += SL(Z_SRED, stol_bok(60, 740, 1800, 340, t))
    s += SL(Z_SRED, f'<path d="M20,560 h1880 l40,180 q-960,56 -1960,0 z"'
                    f' fill="#fdfaf2" {o(7)}/>'
            + f'<path d="M60,640 h1800" stroke="#e8e2d4" stroke-width="10"/>')
    # еловая ветка в вазе
    s += SL(Z_PERED, f'<path d="M1580,556 q-10,-130 100,-130 q110,0 100,130 z"'
                     f' fill="url(#stekl)" opacity=".8" {o(6)}/>')
    for j in range(5):
        ang = 4 * A.w(t, 2.6, j * .2)
        s += SL(Z_PERED, f'<g transform="rotate({ang:.1f},1680,426)">'
                + f'<path d="M1680,426 l{-130+j*65},-{110+j*18}" stroke="{ZEL}"'
                  f' stroke-width="15"/></g>')
    # хрусталь бликует
    for i in range(4):
        xx = 260 + i * 200
        bl = .3 + .6 * abs(A.w(t, 2.0, i * .25))
        s += SL(Z_PERED, f'<path d="M{xx-50},540 q10,-120 50,-130 q40,10 50,130 z"'
                         f' fill="url(#stekl)" opacity=".85" {o(6)}/>'
                + f'<rect x="{xx-10}" y="540" width="20" height="50" rx="6"'
                  f' fill="url(#stekl)" opacity=".9" {o(4)}/>'
                + f'<ellipse cx="{xx}" cy="596" rx="56" ry="16" fill="url(#stekl)"'
                  f' opacity=".9" {o(4)}/>'
                + f'<path d="M{xx-30},470 q30,20 60,0" fill="none" stroke="#ffffff"'
                  f' stroke-width="9" opacity="{bl*.5:.2f}"/>')
    # заливная рыба встаёт в центр
    k = A.over(A.seg(t, .6, .5))
    if k > 0:
        kk = min(1.0, k)
        drozh = 4 * A.w(t, 2.4)
        s += SL(Z_PERED, f'<g opacity="{kk:.2f}" transform="translate(0,{-60*(1-kk):.0f})">'
                + f'<ellipse cx="1050" cy="580" rx="370" ry="92" fill="url(#krem)" {o(7)}/>'
                + f'<ellipse cx="1050" cy="{566+drozh*.4:.0f}" rx="330" ry="74"'
                  f' fill="#d8d0a8" opacity=".85" {o(4)}/>'
                + ryba(1050, 556, 1.5, t, False)
                + "".join(f'<ellipse cx="{900+j*100}" cy="540" rx="26" ry="12"'
                          f' fill="#e07a2c" opacity=".9" {o(3)}/>' for j in range(3))
                + '</g>')
    # свеча горит
    s += SL(Z_PERED, svecha(620, 556, t, .3, 1.6, 120)
            + teplo(620, 450, 360, 320, .5))
    s += _vinetka(.44)
    return s


def novogodniy_stol_s_bumazhnymi_snezh(t):
    """Планы 149-150. Комната шестидесятых: снежинки, радиола, бахрома."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#c6b79c"/>'
            + f'<rect x="0" y="0" width="{W}" height="420" fill="#b3a48a"/>'
            + f'<rect x="0" y="860" width="{W}" height="220" fill="url(#pol)"/>'
            + polovicy(860))
    # окно с бумажными снежинками
    s += SL(Z_DAL, f'<rect x="1120" y="140" width="700" height="520" rx="12"'
                   f' fill="url(#nnoch)" {o(9)}/>'
            + f'<path d="M1470,140 v520 M1120,400 h700" {o(7)} fill="none"/>')
    for i in range(6):
        xx = 1180 + (i % 3) * 230
        yy = 220 + (i // 3) * 240
        drozh = 3 * A.w(t, 2.8, i * .2)
        s += SL(Z_SRED, f'<g transform="translate({xx},{yy+drozh:.1f})">'
                + "".join(f'<path d="M0,0 l{math.cos(j*1.05)*54:.0f},'
                          f'{math.sin(j*1.05)*54:.0f}" stroke="#fdfaf2"'
                          f' stroke-width="7"/>' for j in range(6))
                + f'<circle cx="0" cy="0" r="12" fill="#fdfaf2"/></g>')
    # ёлка с ватным Дедом Морозом
    for i in range(5):
        yy = 840 - i * 118
        w_ = 330 - i * 54
        s += SL(Z_SRED, f'<path d="M{380-w_},{yy} L380,{yy-150-i*6} L{380+w_},{yy} z"'
                        f' fill="{"#2f5e34" if i%2 else "#3c6b3a"}" {o(7)}/>')
        for j in range(7):
            u = (j + 1) / 8.0
            s += SL(Z_SRED, f'<path d="M{380-w_+2*w_*u:.0f},{yy-6:.0f}'
                            f' l{(-1 if u<.5 else 1)*26:.0f},{26:.0f}"'
                            f' stroke="{"#27502c" if i%2 else "#345c32"}"'
                            f' stroke-width="7" opacity=".9"/>')
        for j in range(4):
            mig = .35 + .65 * abs(A.w(t, 1.5, (i * 4 + j) * .11))
            s += SL(Z_PERED, f'<circle cx="{380-w_*.7+j*(w_*1.4/3):.0f}" cy="{yy-18}" r="11"'
                             f' fill="{["#f0d08a","#d9534a","#6bbf59","#4a9bd8"][j%4]}"'
                             f' opacity="{mig:.2f}"/>')
    s += SL(Z_SRED, f'<rect x="356" y="840" width="48" height="56" rx="8"'
                    f' fill="url(#derev)" {o(6)}/>')
    # ватный Дед Мороз под ёлкой
    s += SL(Z_PERED, ten(300, 900, 90, 20, .45)
            + f'<path d="M232,890 q-10,-150 68,-150 q78,0 68,150 z" fill="#c0392b" {o(7)}/>'
            + f'<path d="M244,860 q56,16 112,0" fill="none" stroke="#f6eedc"'
              f' stroke-width="12"/>'
            + f'<circle cx="300" cy="712" r="40" fill="#f3d9bc" {o(6)}/>'
            + f'<path d="M262,706 q38,-64 76,-6 q-38,22 -76,6 z" fill="#c0392b" {o(5)}/>'
            + f'<circle cx="340" cy="684" r="14" fill="#f6eedc" {o(4)}/>'
            + f'<path d="M268,730 q32,42 64,0 q-32,26 -64,0 z" fill="#f6eedc" {o(4)}/>'
            + f'<circle cx="286" cy="706" r="5" fill="{K}"/>'
            + f'<circle cx="314" cy="706" r="5" fill="{K}"/>')
    # радиоприёмник, лампочка светится
    mig = .5 + .5 * abs(A.w(t, 2.2))
    s += SL(Z_SRED, f'<rect x="700" y="560" width="380" height="220" rx="16"'
                    f' fill="#8a6038" {o(8)}/>'
            + f'<rect x="730" y="600" width="200" height="140" rx="10"'
              f' fill="#d8cdb4" {o(5)}/>'
            + "".join(f'<path d="M{750+j*30},610 v120" stroke="#b9ae92"'
                      f' stroke-width="7"/>' for j in range(6))
            + f'<circle cx="1000" cy="660" r="26" fill="{ZHELEZ}" {o(5)}/>'
            + f'<circle cx="1000" cy="720" r="14" fill="{ORA}" opacity="{mig:.2f}"/>')
    # стол под скатертью с бахромой
    s += SL(Z_PERED, f'<path d="M0,{H} v-240 q700,-70 1400,-10 v250 z"'
                     f' fill="#9a3f3a" {o(8)}/>')
    for j in range(22):
        kol = 7 * A.w(t, 1.9, j * .12)
        s += SL(Z_PERED, f'<path d="M{40+j*64},{860+(j%2)*6} q{kol:.0f},40 0,80"'
                         f' fill="none" stroke="#d9a441" stroke-width="7"/>')
    s += _vinetka(.44)
    return s


def mandarin_i_kozhura_spiralyu(t):
    """План 151. Руки чистят мандарин, кожура сходит спиралью."""
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#3a332c"/>'
            + f'<rect x="0" y="0" width="{W}" height="{H}" fill="url(#teplo)" opacity=".3"/>')
    s += SL(Z_SRED, stol_bok(0, 880, 1200, 200, t, "#e7dcc4"))
    # руки держат мандарин (в левой полосе — справа окно вставки)
    s += SL(Z_PERED, ruka(40, 820, t, 260, -28, 58, "#6b5a6e"))
    s += SL(Z_PERED, f'<g transform="scale(-1,1) translate(-1180,0)">'
            + ruka(300, 840, t, 240, -22, 56, "#6b5a6e") + '</g>')
    # мандарин
    s += SL(Z_PERED, f'<circle cx="440" cy="640" r="150" fill="#e07a2c" {o(8)}/>'
            + f'<circle cx="400" cy="600" r="44" fill="#f0a050" opacity=".55"/>')
    # кожура сходит лентой вниз и ложится витком на стол
    k = A.seg(t, .4, 2.2)
    if k > 0:
        d = "M560,560"
        for j in range(1, 11):
            u = j / 10.0
            xx = 560 + 150 * math.sin(u * 3.2) * k
            yy = 560 + 320 * u * k
            d += " Q%.0f,%.0f %.0f,%.0f" % (xx + 70 * k, yy - 40, xx, yy)
        s += SL(Z_PERED, f'<path d="{d}" fill="none" stroke="#e07a2c"'
                         f' stroke-width="{54-16*k:.0f}" stroke-linecap="round"'
                         f' opacity=".95"/>'
                + f'<path d="{d}" fill="none" stroke="#f2a24c"'
                  f' stroke-width="{20-6*k:.0f}" stroke-linecap="round" opacity=".5"/>')
    # обнажённые дольки под снятой кожурой
    if k > .3:
        kk = min(1.0, (k - .3) / .7)
        s += SL(Z_PERED, f'<g opacity="{kk:.2f}">'
                + "".join(f'<path d="M440,640 L{440+math.cos(j*.9)*124:.0f},'
                          f'{640+math.sin(j*.9)*124:.0f} A124,124 0 0 1 '
                          f'{440+math.cos((j+1)*.9)*124:.0f},'
                          f'{640+math.sin((j+1)*.9)*124:.0f} Z"'
                          f' fill="#f2a24c" {o(5)}/>' for j in range(7))
                + f'<circle cx="440" cy="640" r="26" fill="#e8d6a8" {o(4)}/></g>')
    # брызги сока завитками
    for i in range(6):
        ph = (t * .9 + i * .16) % 1.0
        a = i * 1.05
        s += SL(Z_PERED, f'<path d="M{440+math.cos(a)*(160+ph*160):.0f},'
                         f'{640+math.sin(a)*(120+ph*120):.0f} q20,-24 0,-44"'
                         f' fill="none" stroke="#ffd07a" stroke-width="6"'
                         f' opacity="{.6*(1-ph):.2f}"/>')
    # листок-галочка
    kg = A.out(A.seg(t, 2.4, .7))
    if kg > 0:
        s += SL(Z_PERED, f'<g opacity="{kg:.2f}" transform="translate(760,300)'
                f' scale({.5+.4*kg:.2f})">'
                + f'<circle cx="0" cy="0" r="78" fill="#2f5e34" opacity=".9" {o(6)}/>'
                + f'<path d="M-36,4 l28,30 l50,-64" fill="none" stroke="#eaf6e2"'
                  f' stroke-width="15" stroke-linecap="round"/></g>')
    s += _vinetka(.48)
    return s


# ═══════════════ БЛОК 9. ФИНАЛ ═══════════════
def lesenka_pamyatka_na_stene(t):
    """Планы 157-164. ГЛАВНЫЙ КАДР: шесть полочек лесенкой, сверху окошко.

    Камера здесь почти стоит: на полочки по словам ложатся шесть правил
    плашками (их кладёт over.py), поэтому сама декорация спокойная и
    оставляет место под текст в левой половине кадра.
    """
    s = SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="{PECH}"/>'
            + f'<rect x="0" y="0" width="{W}" height="{H}" fill="url(#teplo)" opacity=".3"/>'
            + f'<rect x="0" y="{H-200}" width="{W}" height="200" fill="url(#pol)"/>'
            + polovicy(H - 200))
    # мазки побелки, чтобы стена жила
    for i in range(7):
        s += SL(Z_DAL, f'<path d="M{80+i*280},150 q60,260 0,520" fill="none"'
                       f' stroke="#ffffff" stroke-width="26" opacity=".18"/>')
    # шесть полочек лесенкой снизу вверх
    for i in range(6):
        yy = 940 - i * 128
        x0 = 220 + i * 92
        w_ = 520
        skr = 2.0 * A.w(t, 2.2 + i * .2, i * .3)
        s += SL(Z_SRED, f'<g transform="translate(0,{skr:.1f})">'
                + f'<path d="M{x0},{yy} h{w_} l-40,-58 h-{w_-80} z"'
                  f' fill="#ba8c5c" {o(6)}/>'
                + f'<rect x="{x0}" y="{yy}" width="{w_}" height="28" rx="8"'
                  f' fill="url(#dosk)" {o(7)}/>'
                + f'<rect x="{x0+4}" y="{yy-8}" width="{w_-8}" height="12" rx="4"'
                  f' fill="{DOSKA2}" opacity=".8"/>'
                + f'<path d="M{x0+40},{yy+28} l24,44 M{x0+w_-64},{yy+28} l24,44"'
                  f' {o(6)} fill="none"/></g>')
    # на каждой полочке свой предмет: правила видны не только текстом
    predmety = [
        lambda x, y: ryba(x, y - 34, .45, t),
        lambda x, y: (f'<path d="M{x-26},{y} q-6,-78 26,-78 q32,0 26,78 z"'
                      f' fill="#2e4630" opacity=".93" {o(5)}/>'
                      f'<rect x="{x-12}" y="{y-96}" width="24" height="22" rx="6"'
                      f' fill="url(#rush)" {o(4)}/>'),
        lambda x, y: "".join(f'<path d="M{x-40+j*40},{y} q22,-30 44,-2'
                             f' q-22,16 -44,2 z" fill="#8a6038" {o(4)}/>' for j in range(2)),
        lambda x, y: (f'<rect x="{x-34}" y="{y-92}" width="68" height="92" rx="10"'
                      f' fill="url(#stekl)" opacity=".8" {o(5)}/>'
                      f'<ellipse cx="{x}" cy="{y-46}" rx="22" ry="30" fill="#7a9a4a"'
                      f' opacity=".9"/>'),
        lambda x, y: (f'<path d="M{x-32},{y} q-6,-72 32,-72 q38,0 32,72 z"'
                      f' fill="url(#med)" {o(5)}/>'
                      f'<ellipse cx="{x}" cy="{y-72}" rx="32" ry="10" fill="{MED}" {o(4)}/>'),
        lambda x, y: (f'<ellipse cx="{x}" cy="{y-28}" rx="40" ry="26"'
                      f' fill="url(#derev)" {o(5)}/>'
                      f'<rect x="{x+34}" y="{y-40}" width="90" height="16" rx="8"'
                      f' fill="url(#derev)" {o(4)}/>'),
    ]
    for i, f in enumerate(predmety):
        yy = 940 - i * 128
        x0 = 220 + i * 92
        k = A.out(A.seg(t, .4 + i * .25, .5))
        if k <= 0:
            continue
        s += SL(Z_PERED, f'<g opacity="{k:.2f}" transform="translate(0,{-28*(1-k):.0f})">'
                + f(x0 + 430, yy) + '</g>')
    # маленькое окошко над верхней полкой, в нём звезда
    # лампа дышит тёплым светом
    dysh = .85 + .15 * A.w(t, 3.0)
    s += SL(Z_SRED, teplo(960, 560, 1100, 820, .5 * dysh))
    # пылинки в луче
    s += SL(Z_SRED, luch(1180, 90, 460, 900, t, .16))
    for i in range(12):
        ph = (t * .2 + i * .085) % 1.0
        s += SL(Z_PERED, f'<circle cx="{1180+i*42-90*ph:.0f}" cy="{150+ph*780:.0f}"'
                         f' r="4" fill="#fff6dc" opacity="{.5*(1-ph):.2f}"/>')
    s += _vinetka(.42)
    return s


def kastryulya_s_obluplennoy_emalyu(t):
    """Планы 165-166. Старая кастрюля, крышка приподнимается, свет изнутри."""
    s = SL(Z_DAL, kuhnya_stena(t, True, None, False, True, 127))
    # плита
    s += SL(Z_SRED, f'<rect x="120" y="760" width="1240" height="320" rx="18"'
                    f' fill="url(#zhel)" {o(9)}/>'
            + f'<rect x="160" y="800" width="1160" height="30" rx="10"'
              f' fill="{CHUGUN}" opacity=".65"/>'
            + f'<ellipse cx="740" cy="790" rx="300" ry="54" fill="{CHUGUN}" {o(6)}/>')
    # корпус кастрюли: цилиндр с бортом и ручками
    s += SL(Z_SRED, f'<path d="M420,776 l20,-330 h600 l20,330 z" fill="#eef2f4" {o(9)}/>'
            + f'<path d="M440,446 h600" stroke="#c6cfd4" stroke-width="20"/>'
            + f'<ellipse cx="740" cy="446" rx="300" ry="62" fill="#dfe6ea" {o(8)}/>')
    # облупленная эмаль пятнами
    r = random.Random(9)
    for i in range(16):
        xx = 470 + r.randrange(0, 540)
        yy = 500 + r.randrange(0, 230)
        s += SL(Z_SRED, f'<path d="M{xx},{yy} q20,-16 38,2 q-8,22 -38,-2 z"'
                        f' fill="#8d939c" opacity=".85"/>'
                + f'<path d="M{xx+4},{yy+2} q14,-10 26,2" fill="none" stroke="#6b7278"'
                  f' stroke-width="4" opacity=".7"/>')
    # ручки по бокам
    s += SL(Z_SRED, f'<path d="M424,520 q-70,40 0,86" fill="none" stroke="{ZHELEZ}"'
                    f' stroke-width="26" stroke-linecap="round"/>'
            + f'<path d="M1056,520 q70,40 0,86" fill="none" stroke="{ZHELEZ}"'
              f' stroke-width="26" stroke-linecap="round"/>')
    # крышка приподнимается, изнутри тёплый свет
    pod = A.ease(A.seg(t, .6, 1.6))
    svet = .5 + .5 * A.w(t, 2.2)
    if pod > .05:
        s += SL(Z_SRED, f'<ellipse cx="740" cy="446" rx="292" ry="56" fill="{SVET}"'
                        f' opacity="{(.4+.35*svet)*pod:.2f}"/>'
                + teplo(740, 400, 760, 520, .5 * pod * svet))
        s += SL(Z_SRED, par(740, 380, t, 6, .5 * pod, 250, .4, 1.3))
    s += SL(Z_PERED, f'<g transform="translate(0,{-150*pod:.0f}) rotate({7*pod:.1f},740,430)">'
            + f'<ellipse cx="740" cy="430" rx="312" ry="66" fill="#c6cfd4" {o(8)}/>'
            + f'<ellipse cx="740" cy="412" rx="240" ry="46" fill="#dfe6ea" opacity=".9"/>'
            + f'<rect x="700" y="356" width="80" height="34" rx="14"'
              f' fill="{CHUGUN}" {o(5)}/></g>')
    # бабушкин половник на крючке покачивается
    ang = 5 * A.w(t, 2.0)
    s += SL(Z_SRED, f'<circle cx="1620" cy="280" r="14" fill="{ZHELEZ}" {o(5)}/>'
            + f'<g transform="rotate({ang:.1f},1620,280)">'
            + f'<path d="M1620,280 q-10,140 0,250 q0,70 70,74" fill="none"'
              f' stroke="{ZHELEZ}" stroke-width="18" stroke-linecap="round"/>'
            + f'<ellipse cx="1724" cy="620" rx="86" ry="52" fill="url(#zhel)" {o(8)}/>'
            + f'<ellipse cx="1724" cy="606" rx="58" ry="30" fill="#6b7278" opacity=".7"/>'
            + f'<ellipse cx="1700" cy="598" rx="26" ry="12" fill="#ffffff"'
              f' opacity=".35"/></g>')
    s += _vinetka(.44)
    return s


def dver_s_elovym_venkom(t):
    """План 169. Дверь с еловым венком, под ней свет, мимо скачут сороки."""
    s = SL(Z_DAL, nebo("sumer", t, True))
    s += SL(Z_DAL, f'<rect x="0" y="0" width="{W}" height="{H}" fill="#3a4450" opacity=".5"/>'
            + brevna(0, 0, W, 900, 94, 0)
            + f'<rect x="0" y="860" width="{W}" height="220" fill="url(#sneg)"/>'
            + _sneg_lezhit(860, 20))
    # дверь
    s += SL(Z_SRED, f'<rect x="620" y="140" width="700" height="760" rx="12"'
                    f' fill="#6b4a2c" {o(9)}/>'
            + f'<rect x="670" y="200" width="270" height="300" rx="10"'
              f' fill="#5e4028" {o(6)}/>'
            + f'<rect x="1000" y="200" width="270" height="300" rx="10"'
              f' fill="#5e4028" {o(6)}/>'
            + f'<rect x="670" y="540" width="600" height="300" rx="10"'
              f' fill="#5e4028" {o(6)}/>'
            + f'<circle cx="1250" cy="540" r="24" fill="{MED}" {o(6)}/>')
    # полоска тёплого света под дверью
    pul = .7 + .3 * A.w(t, 2.6)
    s += SL(Z_PERED, f'<rect x="620" y="884" width="700" height="18" rx="6"'
                     f' fill="{SVET}" opacity="{pul:.2f}"/>'
            + f'<ellipse cx="970" cy="908" rx="420" ry="46" fill="{SVET}"'
              f' opacity="{.3*pul:.2f}"/>')
    # еловый венок покачивается
    ang = 3.4 * A.w(t, 2.4)
    s += SL(Z_PERED, f'<g transform="rotate({ang:.1f},970,330)">'
            + f'<circle cx="970" cy="430" r="160" fill="none" stroke="#2f5e34"'
              f' stroke-width="56"/>'
            + "".join(f'<path d="M{970+math.cos(j*.5)*160:.0f},'
                      f'{430+math.sin(j*.5)*160:.0f} l{math.cos(j*.5)*46:.0f},'
                      f'{math.sin(j*.5)*46:.0f}" stroke="#3c6b3a"'
                      f' stroke-width="13"/>' for j in range(13))
            + "".join(f'<circle cx="{970+math.cos(j*1.6)*150:.0f}"'
                      f' cy="{430+math.sin(j*1.6)*150:.0f}" r="17" fill="#c0392b"'
                      f' {o(4)}/>' for j in range(5))
            + f'<path d="M930,270 q40,-50 80,0 q-40,30 -80,0 z" fill="{TKAN}" {o(5)}/>'
            + '</g>')
    # стайка сорок скачет мимо и улетает
    for i in range(4):
        ph = (t * .3 + i * .17) % 1.0
        xx = 120 + ph * 1700
        pryg = abs(math.sin(ph * 18)) * 40 * (1 - ph)
        ulet = max(0.0, ph - .7) * 3
        yy = 980 - pryg - ulet * 500
        s += SL(Z_PERED, f'<g transform="translate({xx:.0f},{yy:.0f})">'
                + f'<ellipse cx="0" cy="0" rx="46" ry="24" fill="#1c1a18" {o(4)}/>'
                + f'<ellipse cx="-14" cy="2" rx="22" ry="16" fill="#f2f4f0"/>'
                + f'<circle cx="34" cy="-14" r="17" fill="#1c1a18" {o(4)}/>'
                + f'<path d="M48,-12 l16,6 l-16,6 z" fill="{MED}"/>'
                + f'<path d="M-40,-4 l-60,{-10-30*ulet:.0f} l56,16 z" fill="#1c1a18" {o(3)}/>'
                + (f'<path d="M0,-10 q26,-{30+40*ulet:.0f} 56,-8" fill="none"'
                   f' stroke="#2a2724" stroke-width="12"/>' if ulet > 0 else "")
                + '</g>')
    s += SL(Z_LETIT, _sneg_letit(t, 24, 131, .5, .55))
    s += _vinetka(.46)
    return s
