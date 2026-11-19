#!/usr/bin/env python3
"""Draws the last twelve months of contributions, public and private.

GitHub's own graph on the profile page already shows the full picture, because
"Include private contributions on my profile" is on. Third-party cards cannot:
they query the API with their own token, and the API returns private
contributions only to the account that made them. So this one is generated here,
with a token that belongs to the account, and committed as an image.

Needs a token in GH_TOKEN or GITHUB_TOKEN with `read:user`. Locally the GitHub
CLI's own token does, so `GH_TOKEN=$(gh auth token) python3 tools/build_contributions.py`
works without creating anything. In CI it is a secret, because the default
Actions token is scoped to the repository and sees none of this.

    python3 tools/build_contributions.py     # writes into assets/
"""
from __future__ import annotations

import datetime as dt
import json
import os
import pathlib
import subprocess
import urllib.request

LOGIN = "adminleo"
OUT = pathlib.Path(__file__).resolve().parent.parent / "assets"
UI = "Helvetica Neue, Liberation Sans, Arial, sans-serif"

THEMES = {
    "light": dict(canvas="#ffffff", subtle="#f6f8fa", border="#d1d9e0",
                  fg="#1f2328", muted="#59636e", faint="#818b98",
                  bar="#1a7f37", barsoft="#aceebb"),
    "dark": dict(canvas="#0d1117", subtle="#151b23", border="#3d444d",
                 fg="#e6edf3", muted="#9198a1", faint="#6e7681",
                 bar="#3fb950", barsoft="#1b4721"),
}

QUERY = """
query($login:String!, $from:DateTime!, $to:DateTime!) {
  user(login:$login) {
    contributionsCollection(from:$from, to:$to) {
      contributionCalendar {
        totalContributions
        weeks { contributionDays { date contributionCount } }
      }
    }
  }
}
"""


def fetch(login: str, to: dt.date):
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if not token:
        raise SystemExit("GH_TOKEN or GITHUB_TOKEN required (needs read:user)")
    frm = to - dt.timedelta(days=365)
    body = json.dumps({
        "query": QUERY,
        "variables": {"login": login,
                      "from": f"{frm}T00:00:00Z", "to": f"{to}T00:00:00Z"},
    }).encode()
    req = urllib.request.Request(
        "https://api.github.com/graphql", data=body,
        headers={"Authorization": f"bearer {token}",
                 "Content-Type": "application/json",
                 "User-Agent": "adminleo-profile-contributions"})
    with urllib.request.urlopen(req, timeout=30) as r:
        payload = json.load(r)
    if "errors" in payload:
        raise SystemExit(f"GraphQL: {payload['errors']}")
    cal = payload["data"]["user"]["contributionsCollection"]["contributionCalendar"]
    days = [(dt.date.fromisoformat(d["date"]), d["contributionCount"])
            for w in cal["weeks"] for d in w["contributionDays"]]
    return cal["totalContributions"], days


def by_month(days):
    """Twelve buckets, oldest first, each (label, total)."""
    out: dict[tuple[int, int], int] = {}
    for date, n in days:
        out[(date.year, date.month)] = out.get((date.year, date.month), 0) + n
    keys = sorted(out)[-12:]
    return [(dt.date(y, m, 1).strftime("%b"), out[(y, m)]) for y, m in keys]


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def render(total, days, th):
    W, H = 1200, 268
    X0, X1, BASE, TOP = 40, 1160, 214, 96
    months = by_month(days)
    peak = max(n for _, n in months) or 1
    active = sum(1 for _, n in days if n)
    best_day = max(days, key=lambda d: d[1])

    p = [f'<rect width="{W}" height="{H}" fill="{th["canvas"]}"/>']
    p.append(f'<text x="{X0}" y="42" font-family="{UI}" font-size="22" '
             f'font-weight="600" fill="{th["fg"]}">{total:,} contributions '
             f'in the last year</text>')
    p.append(f'<text x="{X0}" y="66" font-family="{UI}" font-size="13.5" '
             f'fill="{th["muted"]}">{active} active days · busiest day '
             f'{best_day[1]:,} on {best_day[0]:%-d %B %Y} · public and private, '
             f'most of it private</text>')

    slot = (X1 - X0) / len(months)
    bw = slot * 0.62
    for i, (label, n) in enumerate(months):
        x = X0 + i * slot + (slot - bw) / 2
        h = max(2.0, (n / peak) * (BASE - TOP))
        last = i == len(months) - 1
        p.append(f'<rect x="{x:.1f}" y="{BASE - h:.1f}" width="{bw:.1f}" '
                 f'height="{h:.1f}" rx="3" '
                 f'fill="{th["bar"] if last else th["barsoft"]}"/>')
        if n:
            p.append(f'<text x="{x + bw/2:.1f}" y="{BASE - h - 9:.1f}" '
                     f'font-family="{UI}" font-size="12" font-weight="600" '
                     f'text-anchor="middle" fill="{th["muted"]}">{n:,}</text>')
        p.append(f'<text x="{x + bw/2:.1f}" y="{BASE + 20}" font-family="{UI}" '
                 f'font-size="12" text-anchor="middle" '
                 f'fill="{th["faint"]}">{esc(label)}</text>')

    p.append(f'<line x1="{X0}" y1="{BASE}" x2="{X1}" y2="{BASE}" '
             f'stroke="{th["border"]}" stroke-width="1"/>')
    p.append(f'<text x="{X0}" y="{H - 14}" font-family="{UI}" font-size="12" '
             f'fill="{th["faint"]}">Counted {dt.date.today():%-d %B %Y}. Private '
             f'contributions are counted, never named — no repository, no '
             f'message, no organisation.</text>')

    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
            f'viewBox="0 0 {W} {H}" role="img">\n' + "\n".join(p) + "\n</svg>\n")


def main():
    total, days = fetch(LOGIN, dt.date.today())
    OUT.mkdir(exist_ok=True)
    for theme, th in THEMES.items():
        s = OUT / f"contributions-{theme}.svg"
        s.write_text(render(total, days, th), encoding="utf-8")
        subprocess.run(["rsvg-convert", "-z", "2", str(s), "-o",
                        str(OUT / f"contributions-{theme}.png")], check=True)
        print("  ", s.stem, f"({total:,} contributions)")


if __name__ == "__main__":
    main()
