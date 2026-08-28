from pathlib import Path
import sys
from PIL import Image, ImageOps

RAMP = " .`:-=+*cs#%@"

def make_svg(source, output, width_chars=72):
    img = Image.open(source).convert("L")
    img = ImageOps.autocontrast(img)
    aspect = img.height / img.width
    height_chars = max(20, int(width_chars * aspect * 0.50))
    img = img.resize((width_chars, height_chars))
    pixels = list(img.getdata())
    cell_w, cell_h = 8, 12
    width, height = width_chars * cell_w, height_chars * cell_h

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" rx="12" fill="#0d1117"/>',
        '<g fill="#c9d1d9" font-family="monospace" font-size="12" xml:space="preserve">'
    ]

    for y in range(height_chars):
        chars = []
        for x in range(width_chars):
            v = pixels[y * width_chars + x]
            idx = min(len(RAMP)-1, int((255-v)/256*len(RAMP)))
            chars.append(RAMP[idx])
        safe = "".join(chars).replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
        delay = y * 0.055
        svg.append(
            f'<text x="8" y="{14+y*12}">{safe}'
            f'<animate attributeName="opacity" from="0" to="1" begin="{delay:.3f}s" dur="0.20s" fill="freeze"/></text>'
        )

    svg.append("</g></svg>")
    Path(output).write_text("\n".join(svg), encoding="utf-8")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("Usage: python scripts/make_ascii_svg.py SOURCE_IMAGE OUTPUT_SVG")
    make_svg(sys.argv[1], sys.argv[2])
