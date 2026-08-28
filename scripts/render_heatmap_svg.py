from pathlib import Path
import json
from datetime import datetime, timedelta

data = json.loads(Path("data/contributions.json").read_text())
days = {d["date"]: d for d in data["days"]}

latest = datetime.strptime(max(days), "%Y-%m-%d").date()
grid_start = latest - timedelta(days=latest.weekday()+1)
palette = ["#161b22","#0e4429","#006d32","#26a641","#39d353"]

cell, gap, left, top = 12, 3, 28, 34
weeks = 53
width = left + weeks*(cell+gap) + 10
height = top + 7*(cell+gap) + 55

svg = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
<rect width="100%" height="100%" rx="12" fill="#0d1117" stroke="#30363d"/>
<text x="16" y="21" fill="#c9d1d9" font-family="monospace" font-size="12">{data["username"]} — contribution activity</text>''']

for week in range(weeks):
    for row in range(7):
        d = grid_start + timedelta(days=week*7+row)
        item = days.get(d.isoformat(), {"level":0,"count":0})
        level = max(0, min(4, int(item["level"])))
        x, y = left + week*(cell+gap), top + row*(cell+gap)
        delay = (week+row)*0.012
        svg.append(f'''<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="2" fill="{palette[level]}" opacity="0">
<title>{d.isoformat()}: {item["count"]} contributions</title>
<animate attributeName="opacity" from="0" to="1" begin="{delay:.3f}s" dur="0.35s" fill="freeze"/></rect>''')

svg.append(f'''<text x="16" y="{height-18}" fill="#8b949e" font-family="monospace" font-size="11">{data["total"]:,} contributions · current streak {data["current_streak"]}d · best day {data["best_day_count"]}</text>
</svg>''')

Path("assets/contrib-heatmap.svg").write_text("\n".join(svg), encoding="utf-8")
print("wrote assets/contrib-heatmap.svg")
