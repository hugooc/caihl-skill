from pathlib import Path
from textwrap import wrap

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "og-image.png"

W, H = 1200, 630
FOREST = "#12352B"
CREAM = "#F8F6F2"
CREAM_DIM = "#D5D6D1"
GOLD = "#C9A24B"
EMERALD = "#0c8060"

FONT_DIR = Path("/System/Library/Fonts")
SUPP = FONT_DIR / "Supplemental"


def font(path, size):
    return ImageFont.truetype(str(path), size=size)


title_font = font(FONT_DIR / "HelveticaNeue.ttc", 88)
body_font = font(FONT_DIR / "HelveticaNeue.ttc", 31)
small_font = font(FONT_DIR / "HelveticaNeue.ttc", 24)
label_font = font(FONT_DIR / "HelveticaNeue.ttc", 18)
serif_italic = font(SUPP / "Georgia Italic.ttf", 30)

img = Image.new("RGB", (W, H), FOREST)
draw = ImageDraw.Draw(img)

for x in range(0, W, 92):
    draw.line((x, 0, x, H), fill=(30, 75, 61), width=1)
for y in range(0, H, 92):
    draw.line((0, y, W, y), fill=(30, 75, 61), width=1)

draw.text((92, 72), "CAIHL.", fill=CREAM, font=label_font)
draw.text((92, 128), "A portable AI skill for patients", fill=GOLD, font=serif_italic)

draw.text((92, 188), "Critical AI", fill=CREAM, font=title_font)
draw.text((92, 286), "Health Literacy", fill=CREAM, font=title_font)

lede = (
    "An analytical lens for any topic where AI and health intersect. "
    "It asks the question most evaluations skip: who does this AI actually serve, "
    "and does it expand or constrain patient agency?"
)
y = 408
for line in wrap(lede, width=76):
    draw.text((96, y), line, fill=CREAM_DIM, font=body_font)
    y += 39

draw.rounded_rectangle((838, 122, 1108, 178), radius=28, fill=EMERALD)
draw.text((892, 137), "Download the skill", fill="white", font=small_font)

draw.line((92, 532, 1108, 532), fill=GOLD, width=3)
draw.text((92, 558), "FRAMEWORK", fill=GOLD, font=label_font)
draw.text((266, 552), "Hugo Campos & Liz Salmi", fill=CREAM, font=small_font)
draw.text((266, 582), "NAM Perspectives, 2025", fill=CREAM_DIM, font=small_font)

draw.text((648, 558), "LICENSE", fill=GOLD, font=label_font)
draw.text((770, 552), "MIT", fill=CREAM, font=small_font)
draw.text((770, 582), "Free to use and adapt", fill=CREAM_DIM, font=small_font)

img.save(OUT, "PNG", optimize=True)
print(OUT)
