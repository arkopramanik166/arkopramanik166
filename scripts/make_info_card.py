from pathlib import Path
from html import escape

OUT = Path("assets/info-card.svg")
OUT.parent.mkdir(parents=True, exist_ok=True)

rows = [
    ("ROLE", "AI/ML Engineer in the making"),
    ("LANG", "C++ · Python · SQL"),
    ("AI", "PyTorch · Scikit-learn"),
    ("BACKEND", "FastAPI · REST APIs"),
    ("SYSTEMS", "Linux · Docker · Git"),
    ("CLOUD", "AWS"),
    ("FOCUS", "AI Systems · Agentic AI"),
]

W, H = 490, 380
svg = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<rect width="{W}" height="{H}" rx="14" fill="#0d1117" stroke="#30363d"/>
<circle cx="22" cy="22" r="6" fill="#ff5f56"/>
<circle cx="42" cy="22" r="6" fill="#ffbd2e"/>
<circle cx="62" cy="22" r="6" fill="#27c93f"/>
<text x="88" y="28" fill="#8b949e" font-family="monospace" font-size="14">arko@github:~</text>
<text x="24" y="65" fill="#39d353" font-family="monospace" font-size="16">$ ./profile</text>
<text x="24" y="91" fill="#f0f6fc" font-family="monospace" font-size="20" font-weight="700">ARKO PRAMANIK</text>''']

y = 122
for i, (key, value) in enumerate(rows):
    delay = i * 0.16
    svg.append(f'''<g opacity="0">
<animate attributeName="opacity" from="0" to="1" begin="{delay:.2f}s" dur="0.45s" fill="freeze"/>
<text x="24" y="{y}" fill="#39d353" font-family="monospace" font-size="13">{escape(key):10}</text>
<text x="112" y="{y}" fill="#c9d1d9" font-family="monospace" font-size="13">{escape(value)}</text>
</g>''')
    y += 32

svg.append(f'''<text x="24" y="{H-20}" fill="#8b949e" font-family="monospace" font-size="12">build → measure → ship → repeat</text>
</svg>''')

OUT.write_text("\n".join(svg), encoding="utf-8")
print(f"wrote {OUT}")
