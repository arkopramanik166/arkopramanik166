from pathlib import Path
import json, os, re, requests
from datetime import date
from bs4 import BeautifulSoup

USERNAME = os.environ.get("GITHUB_USERNAME", "YOUR_GITHUB_USERNAME")
url = f"https://github.com/users/{USERNAME}/contributions"

r = requests.get(url, headers={"User-Agent":"github-profile-readme/1.0"}, timeout=30)
r.raise_for_status()

soup = BeautifulSoup(r.text, "html.parser")
cells = soup.select("[data-date][data-level]")
if not cells:
    raise RuntimeError("No contribution cells found. Check the username or GitHub page structure.")

days = []
for c in cells:
    text = c.get_text(" ", strip=True)
    m = re.search(r"([\d,]+)\s+contribution", text)
    days.append({
        "date": c["data-date"],
        "level": int(c.get("data-level","0")),
        "count": int(m.group(1).replace(",","")) if m else 0
    })

days.sort(key=lambda x:x["date"])
running = longest = current = 0

for d in days:
    if d["count"] > 0:
        running += 1
        longest = max(longest, running)
    else:
        running = 0

for d in reversed(days):
    if d["count"] > 0:
        current += 1
    else:
        break

best = max(days, key=lambda x:x["count"])
payload = {
    "username": USERNAME,
    "days": days,
    "total": sum(d["count"] for d in days),
    "current_streak": current,
    "longest_streak": longest,
    "best_day": best["date"],
    "best_day_count": best["count"],
    "generated_at": date.today().isoformat()
}

Path("data").mkdir(exist_ok=True)
Path("data/contributions.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
print(f'{USERNAME}: {payload["total"]:,} contributions')
