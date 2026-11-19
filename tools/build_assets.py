#!/usr/bin/env python3
"""Renders the profile graphics as SVG and PNG, light and dark.

They are drawn in GitHub's own palette and a neutral system face so that they
read as part of the page rather than as inserted advertising. Nothing is
decorative: the career strip is the dates from the CV, the gate is the output
of `python3 examples/run_example.py` in grounded-ai-evals, and the error map is
`findings/results/error_prices.csv` in ames-house-prices.

Needs `rsvg-convert`. Any neutral grotesque will do for the text; Helvetica
Neue is close to the face GitHub actually renders with.

    python3 tools/build_assets.py      # writes into assets/
"""
from __future__ import annotations

import pathlib
import subprocess

OUT = pathlib.Path(__file__).resolve().parent.parent / "assets"
UI = "Helvetica Neue"

# GitHub Primer, light and dark.
THEMES = {
    "light": dict(canvas="#ffffff", subtle="#f6f8fa", border="#d1d9e0",
                  fg="#1f2328", muted="#59636e", faint="#818b98",
                  accent="#0969da", ok="#1a7f37", warn="#9a6700",
                  warnbg="#fff8c5"),
    "dark": dict(canvas="#0d1117", subtle="#151b23", border="#3d444d",
                 fg="#e6edf3", muted="#9198a1", faint="#6e7681",
                 accent="#4493f8", ok="#3fb950", warn="#d29922",
                 warnbg="#282215"),
}


def t(x, y, s, size=14, weight=400, fill="fg", anchor="start", th=None,
      family=UI, ls=None):
    col = th[fill] if (th and fill in th) else fill
    a = f' text-anchor="{anchor}"' if anchor != "start" else ""
    l = f' letter-spacing="{ls}"' if ls else ""
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
            f'font-weight="{weight}" fill="{col}"{a}{l}>{s}</text>')


def svg(w, h, body, th):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" role="img">\n'
            f'<rect width="{w}" height="{h}" fill="{th["canvas"]}"/>\n{body}\n</svg>\n')


# ----------------------------------------------------------------- career ----
def career(th):
    """Dates from the CV at adminleo.github.io/cv."""
    W, H = 1200, 442
    X0, X1, Y0, Y1 = 72, 1128, 2019.0, 2027.0

    def x(year):
        return X0 + (year - Y0) / (Y1 - Y0) * (X1 - X0)

    p = [t(24, 46, "Leonardo Bornhäußer", 27, 600, "fg", th=th),
         t(24, 72, "Technical product owner · R&D lead for AI and knowledge graphs · "
                   "Venture builder · Frankfurt", 14, 400, "muted", th=th),
         f'<line x1="24" y1="96" x2="{W-24}" y2="96" stroke="{th["border"]}" '
         f'stroke-width="1"/>',
         t(24, 124, "Leading software projects since 2014. The roles overlap "
                    "because the next one started before the last one ended.",
           13, 400, "faint", th=th)]

    rows = [
        (2019.5, 2021.75, "Transformation and technology consultant",
         "Bornhäußer & Friends", ""),
        (2021.25, 2022.83, "Proxy product owner, three shareholder savings banks",
         "Karla · Sparkassen-Finanzgruppe", "€500k secured in a board pitch"),
        (2022.83, 2025.25, "Co-founder and head of operations",
         "Camsol group", "2 → ~100 people, 6 GmbH + 2 Ltd"),
        (2024.25, 2026.9, "Managing director and CTO",
         "Creativate Technologies", ""),
    ]

    for year in range(2019, 2027):
        p.append(f'<line x1="{x(year):.1f}" y1="160" x2="{x(year):.1f}" y2="{H-16}" '
                 f'stroke="{th["border"]}" stroke-width="1" opacity="0.6"/>')
        p.append(t(x(year), 152, str(year), 12, 400, "faint",
                   anchor="middle", th=th))

    y = 190
    for j, (a, b, role, org, note) in enumerate(rows):
        current = j == len(rows) - 1
        fill = th["accent"] if current else th["subtle"]
        op = "0.12" if current else "1"
        p.append(t(x(a), y, role, 13.5, 600, "fg", th=th))
        p.append(f'<rect x="{x(a):.1f}" y="{y+10}" width="{x(b)-x(a):.1f}" '
                 f'height="28" rx="5" fill="{fill}" fill-opacity="{op}" '
                 f'stroke="{th["accent"] if current else th["border"]}" stroke-width="1"/>')
        p.append(t(x(a) + 11, y + 29, org, 12.5, 500,
                   "accent" if current else "muted", th=th))
        if note:
            p.append(t(x(b) + 11, y + 29, note, 12.5, 400, "faint", th=th))
        y += 62

    return svg(W, H, "\n".join(p), th)


# ----------------------------------------------- grounded-ai-evals release ----
def gate(th):
    """Layers from the README, figures from examples/run_example.py."""
    W, H = 1200, 418
    p = [t(24, 34, "Four layers, in order", 16, 600, "fg", th=th),
         t(24, 56, "each one is only meaningful once the one above it holds",
           13.5, 400, "muted", th=th)]

    layers = [
        ("1", "Graph correctness", "is what we stored true, sourced, current?"),
        ("2", "Ontology hygiene", "is the schema consistent, and does it answer what it was built for?"),
        ("3", "Answer groundedness", "does every claim trace to a source that carries it?"),
        ("4", "Baseline comparison", "better than a plain model and ordinary RAG?"),
    ]
    y = 102
    for n, name, q in layers:
        p.append(f'<rect x="24" y="{y-15}" width="22" height="22" rx="5" '
                 f'fill="{th["subtle"]}" stroke="{th["border"]}" stroke-width="1"/>')
        p.append(t(35, y + 1, n, 12.5, 600, "muted", anchor="middle", th=th))
        p.append(t(60, y, name, 14.5, 600, "fg", th=th))
        p.append(t(60, y + 21, q, 13, 400, "muted", th=th))
        y += 74

    gx, gy, gw, gh = 660, 86, 516, 288
    p.append(f'<rect x="{gx}" y="{gy}" width="{gw}" height="{gh}" rx="6" '
             f'fill="{th["canvas"]}" stroke="{th["border"]}" stroke-width="1"/>')
    p.append(f'<rect x="{gx}" y="{gy}" width="{gw}" height="40" rx="6" fill="{th["subtle"]}"/>')
    p.append(f'<rect x="{gx}" y="{gy+34}" width="{gw}" height="6" fill="{th["subtle"]}"/>')
    p.append(f'<line x1="{gx}" y1="{gy+40}" x2="{gx+gw}" y2="{gy+40}" '
             f'stroke="{th["border"]}" stroke-width="1"/>')
    p.append(t(gx + 16, gy + 26, "Release gate", 13.5, 600, "fg", th=th))
    p.append(t(gx + gw - 16, gy + 26, "example run · 4 layers · 12 checks", 12.5,
               400, "muted", anchor="end", th=th))

    y = gy + 72
    p.append(f'<rect x="{gx+16}" y="{y-16}" width="78" height="21" rx="10" '
             f'fill="{th["warnbg"]}" stroke="{th["warn"]}" stroke-width="1"/>')
    p.append(t(gx + 55, y - 1, "BLOCKED", 11.5, 600, "warn", anchor="middle", th=th))
    p.append(t(gx + 104, y - 1, "by three named checks", 13, 400, "fg", th=th))

    for name, val, need in (("provenance coverage", "0.80", "needs ≥ 0.95"),
                            ("citation precision", "0.60", "needs ≥ 0.90"),
                            ("unsupported rate", "0.40", "needs ≤ 0.05")):
        y += 33
        p.append(f'<line x1="{gx+17}" y1="{y-10}" x2="{gx+17}" y2="{y+2}" '
                 f'stroke="{th["warn"]}" stroke-width="3"/>')
        p.append(t(gx + 30, y, name, 13, 400, "fg", th=th))
        p.append(t(gx + gw - 118, y, val, 13, 600, "fg", anchor="end", th=th,
                   family="Menlo"))
        p.append(t(gx + gw - 16, y, need, 12.5, 400, "muted", anchor="end", th=th))

    y += 46
    p.append(t(gx + 16, y, "while passing both baselines", 13, 400, "muted", th=th))
    for name, val in (("beats a plain model", "0.71"), ("beats standard RAG", "0.58")):
        y += 30
        p.append(f'<circle cx="{gx+21}" cy="{y-5}" r="4" fill="{th["ok"]}"/>')
        p.append(t(gx + 34, y, name, 13, 400, "fg", th=th))
        p.append(t(gx + gw - 118, y, val, 13, 600, "fg", anchor="end", th=th,
                   family="Menlo"))

    p.append(t(24, H - 18, "No weighted mean: a 0.91 composite can hide a 0.40 "
                           "unsupported-claim rate, so the gate names its blockers.",
               13, 400, "faint", th=th))
    return svg(W, H, "\n".join(p), th)


# ------------------------------------------------------------ Ames errors ----
def ames(th):
    """Figures from ames-house-prices/findings/results/error_prices.csv."""
    W, H = 1200, 392
    LO, HI, X0, X1 = 130_000, 340_000, 96, 1120
    CUT, BAND = 250_580, 17_420
    AX = 232

    def x(v):
        return X0 + (v - LO) / (HI - LO) * (X1 - X0)

    p = [t(24, 34, "Where a classifier gets it wrong", 16, 600, "fg", th=th),
         t(24, 56, "1,460 houses, labelled expensive above $250,580 — "
                   "both error groups sit next to that line", 13.5, 400, "muted", th=th)]

    p.append(f'<rect x="{x(CUT-BAND):.1f}" y="190" width="{x(CUT+BAND)-x(CUT-BAND):.1f}" '
             f'height="92" fill="{th["warnbg"]}" fill-opacity="0.75"/>')
    p.append(f'<line x1="{X0}" y1="{AX}" x2="{X1}" y2="{AX}" '
             f'stroke="{th["border"]}" stroke-width="1"/>')
    p.append(f'<line x1="{x(CUT):.1f}" y1="140" x2="{x(CUT):.1f}" y2="300" '
             f'stroke="{th["warn"]}" stroke-width="1.5" stroke-dasharray="4 4"/>')
    p.append(t(x(CUT), 132, "cutoff $250,580", 12.5, 600, "warn", anchor="middle", th=th))

    for v in (200_000, 300_000):
        p.append(t(x(v), AX + 22, f"${v//1000}k", 12, 400, "faint",
                   anchor="middle", th=th))

    for v, n, label, sub, col, above in (
            (149_900, 1227, "correctly called cheap", "1,227 houses", "faint", False),
            (320_000, 159, "correctly called expensive", "159 houses", "accent", False),
            (238_500, 16, "false alarm", "16 houses · $12,080 below", "warn", True),
            (268_000, 58, "missed", "58 houses · $17,420 above", "warn", True)):
        r = (n ** 0.5) * 1.05
        op = "0.35" if col == "faint" else "0.9"
        p.append(f'<circle cx="{x(v):.1f}" cy="{AX}" r="{r:.1f}" fill="{th[col]}" '
                 f'fill-opacity="{op}"/>')
        if above:
            anchor = "end" if v < CUT else "start"
            lx = x(v) - 12 if v < CUT else x(v) + 12
            p.append(f'<line x1="{x(v):.1f}" y1="{AX-r-4:.1f}" x2="{x(v):.1f}" '
                     f'y2="178" stroke="{th["warn"]}" stroke-width="1"/>')
            p.append(t(lx, 170, label, 14, 600, "fg", anchor=anchor, th=th))
            p.append(t(lx, 190, sub, 12.5, 400, "muted", anchor=anchor, th=th))
        else:
            p.append(t(x(v), AX + r + 26, label, 14, 600, "fg", anchor="middle", th=th))
            p.append(t(x(v), AX + r + 46, sub, 12.5, 400, "muted", anchor="middle", th=th))

    p.append(t(24, H - 18, "Predicting the price and applying the rule afterwards "
                           "beats classifying directly: F1 0.843 against 0.813 over "
                           "the same 20 folds, p = 0.0098.", 13, 400, "faint", th=th))
    return svg(W, H, "\n".join(p), th)


def main():
    OUT.mkdir(exist_ok=True)
    for name, fn in (("career", career), ("eval-gate", gate), ("ames-errors", ames)):
        for theme, th in THEMES.items():
            s = OUT / f"{name}-{theme}.svg"
            s.write_text(fn(th), encoding="utf-8")
            subprocess.run(["rsvg-convert", "-z", "2", str(s), "-o",
                            str(OUT / f"{name}-{theme}.png")], check=True)
            print("  ", f"{name}-{theme}")


if __name__ == "__main__":
    main()
