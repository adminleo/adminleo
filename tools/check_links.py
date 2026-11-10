"""Check every link and badge image in README.md still resolves.

This exists because a profile README is mostly third-party URLs, and those rot
quietly: a badge that 404s renders as a broken image rather than an error, so
nobody notices. One service already demonstrated the point — the widely
recommended github-readme-stats instance answers DEPLOYMENT_PAUSED, which is
why no stats card from it is used here.

Two response codes are treated as healthy despite not being 2xx:

  403, 999  LinkedIn and similar sites block non-browser user agents outright.
            A 999 means the host is up and refusing the script, which is not
            the same as a dead link. Anything in the 4xx/5xx range from a host
            not on that list is a real failure.

Usage:  python3 tools/check_links.py [README.md]
"""
import os, re, sys, urllib.error, urllib.parse, urllib.request

ROOT   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGET = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "README.md")
UA     = "Mozilla/5.0 (compatible; readme-link-check/1.0)"

# Hosts that answer a bare script with a refusal rather than the page.
BOT_BLOCKED = {"www.linkedin.com", "linkedin.com"}
TOLERATED   = {403, 999}

# Markdown links and images, plus the src/srcset of raw <img>/<source> tags,
# which a markdown-only pattern would miss — and the <picture> fallback for
# dark mode lives in exactly those.
PATTERNS = [r'!?\[[^\]]*\]\((https?://[^)\s]+)\)',
            r'(?:src|srcset)="(https?://[^"]+)"']


def urls(text):
    found = []
    for p in PATTERNS:
        found += re.findall(p, text)
    seen, out = set(), []
    for u in found:
        u = u.rstrip('.,')
        if u not in seen:
            seen.add(u); out.append(u)
    return out


def check(u):
    host = urllib.parse.urlsplit(u).netloc
    req = urllib.request.Request(u, headers={"User-Agent": UA}, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, None
    except urllib.error.HTTPError as e:
        if e.code in TOLERATED and host in BOT_BLOCKED:
            return e.code, None
        return e.code, f"HTTP {e.code}"
    except Exception as e:
        return None, str(e)


def main():
    text = open(TARGET, encoding="utf-8").read()
    links = urls(text)
    if not links:
        sys.exit(f"no links found in {TARGET} — the extraction pattern is probably wrong")
    bad = []
    for u in links:
        status, err = check(u)
        print(f"  {str(status or '---'):>4}  {u[:96]}")
        if err:
            bad.append((u, err))
    print(f"\n{len(links) - len(bad)}/{len(links)} links healthy")
    for u, err in bad:
        print(f"  BROKEN  {err}  {u}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
