#!/usr/bin/env python3
"""Renders the three profile graphics as SVG and PNG, light and dark.

Every number comes from a results table in the repository it describes; the
source is named in each function's docstring. Needs `rsvg-convert` and the
Bricolage Grotesque font installed locally.

    python3 tools/build_assets.py      # schreibt nach assets/
"""
from __future__ import annotations

import pathlib
import subprocess

OUT = pathlib.Path(__file__).resolve().parent.parent / "assets"
BRIC = "Bricolage Grotesque"

THEMES = {
    "light": dict(
        ground="#F8F9FC", surface="#FFFFFF", hair="#E4E7F0",
        text="#1A1D2E", muted="#6B7084", faint="#9AA0B4", accent="#4B6EF5",
    ),
    "dark": dict(
        ground="#0D0F1A", surface="#15182A", hair="#272C45",
        text="#E8EDF5", muted="#98A1BC", faint="#6C7593", accent="#8AA0FF",
    ),
}
BLUE, MINT, VIOLET = "#4B6EF5", "#36C399", "#6B5BCD"


def t(x, y, s, size=16, weight=400, fill="text", anchor="start",
      family=BRIC, ls=None, opacity=None, th=None, extra=""):
    """One <text> element. `fill` may be a theme key or a literal colour."""
    col = th[fill] if (th and fill in th) else fill
    a = f' text-anchor="{anchor}"' if anchor != "start" else ""
    l = f' letter-spacing="{ls}"' if ls else ""
    o = f' opacity="{opacity}"' if opacity else ""
    s = (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
            f'font-weight="{weight}" fill="{col}"{a}{l}{o}{extra}>{s}</text>')


def svg(w, h, body, th):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" role="img">\n'
            f'<rect width="{w}" height="{h}" fill="{th["ground"]}"/>\n{body}\n</svg>\n')


def gradient_def(id_="g"):
    return (f'<defs><linearGradient id="{id_}" x1="0" y1="0" x2="1" y2="0">'
            f'<stop offset="0%" stop-color="{BLUE}"/>'
            f'<stop offset="50%" stop-color="{MINT}"/>'
            f'<stop offset="100%" stop-color="{VIOLET}"/>'
            f'</linearGradient></defs>')


# ---------------------------------------------------------------- banner ----
def banner(th):
    W, H = 1200, 248
    p = [gradient_def()]
    p.append(f'<rect x="0" y="{H-4}" width="{W}" height="4" fill="url(#g)"/>')

    # Graph motif on the right: eight nodes, hairlines, three accent nodes.
    nodes = [(930, 72), (1010, 44), (1086, 86), (1124, 40), (962, 136),
             (1040, 118), (1108, 158), (896, 122)]
    edges = [(0, 1), (1, 2), (2, 3), (0, 4), (1, 5), (5, 2), (5, 6), (4, 5),
             (0, 7), (7, 4)]
    for a, b in edges:
        x1, y1 = nodes[a]
        x2, y2 = nodes[b]
        p.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
                 f'stroke="{th["hair"]}" stroke-width="1.4"/>')
    for i, (x, y) in enumerate(nodes):
        col = {1: BLUE, 5: MINT, 2: VIOLET}.get(i, th["faint"])
        r = 6.5 if i in (1, 5, 2) else 4
        op = "" if i in (1, 5, 2) else ' opacity="0.55"'
        p.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{col}"{op}/>')

    p.append(t(56, 108, "Leonardo Bornhäußer", 58, 300, "text", th=th))
    p.append(t(56, 150, "Tech product owner   ·   R&D lead, AI and knowledge graphs   ·   "
                        "Venture builder", 17, 500, "muted", th=th, ls="0.3"))
    p.append(t(56, 190, "I build AI systems that have to show their evidence —", 18.5, 400,
               "muted", th=th))
    p.append(t(56, 214, "and the methods that decide whether they really do.", 18.5, 400,
               "accent", th=th))
    return svg(W, H, "\n".join(p), th)


# ------------------------------------------------- grounded-ai-evals gate ----
def method(th):
    """Layers and figures from grounded-ai-evals README + examples/run_example.py."""
    W, H = 1200, 540
    p = [gradient_def()]
    p.append(t(56, 56, "Four layers, in order", 31, 300, "text", th=th))
    p.append(t(56, 84, "each one is only meaningful once the one above it holds",
               16.5, 400, "muted", th=th))

    layers = [
        ("1", "Graph correctness", "Is what we stored true, sourced, and current?"),
        ("2", "Ontology hygiene", "Is the schema consistent, and does it answer what it was built for?"),
        ("3", "Answer groundedness", "Does every claim trace to a source that carries it?"),
        ("4", "Baseline comparison", "Is this better than a plain model and ordinary RAG?"),
    ]
    ys = [146, 238, 330, 422]
    p.append(f'<line x1="78" y1="{ys[0]}" x2="78" y2="{ys[-1]}" '
             f'stroke="{th["hair"]}" stroke-width="2"/>')
    cols = [BLUE, MINT, VIOLET, th["faint"]]
    for (n, name, q), y, c in zip(layers, ys, cols):
        p.append(f'<circle cx="78" cy="{y}" r="17" fill="{th["ground"]}" '
                 f'stroke="{c}" stroke-width="2"/>')
        p.append(t(78, y + 6, n, 17, 600, c, anchor="middle", th=th))
        p.append(t(116, y - 2, name, 22, 600, "text", th=th))
        p.append(t(116, y + 24, q, 16, 400, "muted", th=th))

    # Gate panel
    gx, gy, gw, gh = 712, 118, 432, 374
    p.append(f'<rect x="{gx}" y="{gy}" width="{gw}" height="{gh}" rx="10" '
             f'fill="{th["surface"]}" stroke="{th["hair"]}" stroke-width="1.5"/>')
    p.append(t(gx + 28, gy + 42, "Release gate", 20, 600, "text", th=th))
    p.append(t(gx + 28, gy + 68, "example run  ·  4 layers  ·  12 checks", 15, 400,
               "muted", th=th))
    p.append(f'<line x1="{gx+28}" y1="{gy+88}" x2="{gx+gw-28}" y2="{gy+88}" '
             f'stroke="{th["hair"]}" stroke-width="1"/>')

    blockers = [
        ("provenance coverage", "0.80", "needs ≥ 0.95"),
        ("citation precision", "0.60", "needs ≥ 0.90"),
        ("unsupported rate", "0.40", "needs ≤ 0.05"),
    ]
    y = gy + 122
    p.append(t(gx + 28, y, "BLOCKED by three named checks", 15.5, 600, VIOLET, th=th))
    for name, val, need in blockers:
        y += 34
        p.append(f'<rect x="{gx+28}" y="{y-11}" width="4" height="14" rx="2" fill="{VIOLET}"/>')
        p.append(t(gx + 44, y, name, 15.5, 400, "text", th=th))
        p.append(t(gx + gw - 132, y, val, 15, 500, "text", anchor="end", th=th))
        p.append(t(gx + gw - 28, y, need, 15, 400, "muted", anchor="end", th=th))

    y += 46
    p.append(t(gx + 28, y, "— while passing both baselines", 15.5, 600, MINT, th=th))
    for name, val in (("beats a plain model", "0.71"), ("beats standard RAG", "0.58")):
        y += 32
        p.append(f'<circle cx="{gx+32}" cy="{y-5}" r="4" fill="{MINT}"/>')
        p.append(t(gx + 44, y, name, 15.5, 400, "text", th=th))
        p.append(t(gx + gw - 28, y, val, 15, 400, "muted", anchor="end", th=th))

    p.append(t(56, 506, "No weighted mean: a 0.91 composite can hide a 0.40 unsupported-claim "
                        "rate, so the gate returns the blockers by name.", 16, 400,
               "faint", th=th))
    return svg(W, H, "\n".join(p), th)


# -------------------------------------------------------- Ames error map ----
def ames(th):
    """Figures from ames-house-prices/findings/results/error_prices.csv."""
    W, H = 1200, 452
    LO, HI, X0, X1 = 130_000, 340_000, 92, 1132
    CUT, BAND = 250_580, 17_420

    def x(v):
        return X0 + (v - LO) / (HI - LO) * (X1 - X0)

    AX = 258
    p = []
    p.append(t(56, 52, "Where a classifier gets it wrong", 31, 300, "text", th=th))
    p.append(t(56, 80, "1,460 houses, labelled “expensive” above $250,580 — "
                       "every mistake sits next to that line", 16.5, 400, "muted", th=th))

    p.append(f'<rect x="{x(CUT-BAND):.1f}" y="152" width="{x(CUT+BAND)-x(CUT-BAND):.1f}" '
             f'height="212" fill="{VIOLET}" opacity="0.09"/>')
    p.append(f'<line x1="{X0}" y1="{AX}" x2="{X1}" y2="{AX}" stroke="{th["hair"]}" '
             f'stroke-width="1.5"/>')
    p.append(f'<line x1="{x(CUT):.1f}" y1="140" x2="{x(CUT):.1f}" y2="376" '
             f'stroke="{VIOLET}" stroke-width="1.6" stroke-dasharray="5 5"/>')
    p.append(t(x(CUT), 132, "cutoff  $250,580", 15, 600, VIOLET, anchor="middle", th=th))

    for v in (200_000, 300_000):
        p.append(f'<line x1="{x(v):.1f}" y1="{AX}" x2="{x(v):.1f}" y2="{AX+6}" '
                 f'stroke="{th["hair"]}" stroke-width="1.5"/>')
        p.append(t(x(v), AX + 26, f"${v//1000}k", 14, 400, "faint",
                   anchor="middle", th=th))

    # (price, count, label, sub-label, colour, label above the axis?)
    dots = [
        (149_900, 1227, "correctly called cheap", "1,227 houses", th["faint"], False),
        (320_000, 159, "correctly called expensive", "159 houses", BLUE, False),
        (238_500, 16, "false alarm", "16 houses  ·  $12,080 below", VIOLET, True),
        (268_000, 58, "missed", "58 houses  ·  $17,420 above", VIOLET, True),
    ]
    for v, n, label, sub, col, above in dots:
        r = (n ** 0.5) * 1.18
        op = "0.30" if col == th["faint"] else ("0.85" if col == BLUE else "1")
        p.append(f'<circle cx="{x(v):.1f}" cy="{AX}" r="{r:.1f}" fill="{col}" opacity="{op}"/>')
        if above:
            anchor = "end" if v < CUT else "start"
            lx = x(v) - 14 if v < CUT else x(v) + 14
            p.append(f'<line x1="{x(v):.1f}" y1="{AX-r-4:.1f}" x2="{x(v):.1f}" y2="196" '
                     f'stroke="{col}" stroke-width="1.2"/>')
            p.append(t(lx, 186, label, 17, 600, "text", anchor=anchor, th=th))
            p.append(t(lx, 208, sub, 14.5, 400, "muted", anchor=anchor, th=th))
        else:
            p.append(t(x(v), AX + r + 30, label, 17, 600, "text", anchor="middle", th=th))
            p.append(t(x(v), AX + r + 52, sub, 14.5, 400, "muted", anchor="middle", th=th))

    p.append(t(56, 424, "Predicting the price and applying the rule afterwards beats "
                        "classifying directly: F1 0.843 against 0.813 over the same "
                        "20 folds, p = 0.0098.", 16, 400, "faint", th=th))
    return svg(W, H, "\n".join(p), th)


def main():
    OUT.mkdir(exist_ok=True)
    for name, fn in (("banner", banner), ("eval-gate", method), ("ames-errors", ames)):
        for theme, th in THEMES.items():
            s = OUT / f"{name}-{theme}.svg"
            s.write_text(fn(th), encoding="utf-8")
            subprocess.run(["rsvg-convert", "-z", "2", str(s), "-o",
                            str(OUT / f"{name}-{theme}.png")], check=True)
            print("  ", s.name, "->", f"{name}-{theme}.png")


if __name__ == "__main__":
    main()
