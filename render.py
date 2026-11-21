"""Draw the front page for 20 November 2026 as one 1024x1024 PNG.

Everything is drawn with Pillow from fixed text and fixed geometry: no
randomness, no clock, no network, no downloaded assets. Running this file
twice produces byte-identical output.
"""

import os

from PIL import Image, ImageDraw, ImageFont

WIDTH = 1024
HEIGHT = 1024

PAPER = (247, 240, 220)
INK = (26, 26, 26)
RED = (176, 30, 36)
GREY = (112, 106, 94)
FAINT = (168, 160, 140)
SKY = (216, 231, 240)
ROOF = (104, 62, 34)
STONE = (232, 224, 198)
BROWN = (122, 84, 52)

FONT_DIRS = (
    "/usr/share/fonts/truetype/dejavu",
    "/usr/share/fonts/truetype/liberation",
    "/usr/share/fonts/truetype/noto",
)


def _pick(names):
    """Return the first existing font file from the candidate names."""
    for folder in FONT_DIRS:
        for name in names:
            path = os.path.join(folder, name)
            if os.path.exists(path):
                return path
    return None


SERIF_BOLD = _pick(["DejaVuSerif-Bold.ttf", "LiberationSerif-Bold.ttf"])
SERIF = _pick(["DejaVuSerif.ttf", "LiberationSerif-Regular.ttf"])
SERIF_ITALIC = _pick(["DejaVuSerif-Italic.ttf", "LiberationSerif-Italic.ttf"])
SANS = _pick(["DejaVuSans.ttf", "LiberationSans-Regular.ttf"])
SANS_BOLD = _pick(["DejaVuSans-Bold.ttf", "LiberationSans-Bold.ttf"])


def _font(path, size):
    if path is None:
        return ImageFont.load_default()
    return ImageFont.truetype(path, size)


def f_serif_bold(size):
    return _font(SERIF_BOLD, size)


def f_serif(size):
    return _font(SERIF, size)


def f_serif_italic(size):
    return _font(SERIF_ITALIC, size)


def f_sans(size):
    return _font(SANS, size)


def f_sans_bold(size):
    return _font(SANS_BOLD, size)


def wrap_text(draw, text, font, max_width):
    """Split text into lines that fit max_width, word by word."""
    lines = []
    for chunk in text.split("\n"):
        words = chunk.split()
        if not words:
            lines.append("")
            continue
        current = words[0]
        for word in words[1:]:
            trial = current + " " + word
            if draw.textlength(trial, font=font) <= max_width:
                current = trial
            else:
                lines.append(current)
                current = word
        lines.append(current)
    return lines


def draw_centered(draw, y, text, font, fill, centre_x=512):
    width = draw.textlength(text, font=font)
    draw.text((centre_x - width / 2, y), text, font=font, fill=fill)
    return y + font.size


def draw_para(draw, x, y, max_width, text, font, fill, leading):
    for line in wrap_text(draw, text, font, max_width):
        draw.text((x, y), line, font=font, fill=fill)
        y += leading
    return y


def draw_rule(draw, y, width=2, colour=INK):
    draw.line([(40, y), (984, y)], fill=colour, width=width)


def draw_masthead(draw):
    draw_centered(draw, 24, "AN AI-DRAWN FRONT PAGE", f_sans(13), GREY)
    draw_centered(draw, 46, "THE WORLD IN ONE IMAGE", f_serif_bold(60), INK)
    draw.rectangle([40, 122, 984, 168], fill=RED)
    draw_centered(draw, 133, "FRIDAY  ·  20 NOVEMBER 2026", f_sans_bold(25), (255, 255, 255))
    draw_rule(draw, 180)
    draw_rule(draw, 184)


def draw_courtroom(draw, left, top, right, bottom):
    """A small geometric Peace Palace: sky, sun, roof, columns, scales."""
    draw.rectangle([left, top, right, bottom], fill=SKY, outline=INK, width=2)
    draw.ellipse([right - 62, top + 14, right - 14, top + 62], fill=(238, 196, 90))
    # Roof: a wide trapezoid over three columns.
    draw.polygon(
        [
            (left + 30, top + 66),
            (left + 185, top + 22),
            (right - 30, top + 66),
            (right - 10, top + 66),
            (right - 10, top + 82),
            (left + 10, top + 82),
        ],
        fill=ROOF,
    )
    # Three columns.
    for cx in (left + 52, left + 166, right - 72):
        draw.rectangle([cx, top + 82, cx + 26, bottom - 34], fill=STONE, outline=BROWN)
        draw.rectangle([cx - 6, top + 76, cx + 32, top + 84], fill=STONE, outline=BROWN)
        draw.rectangle([cx - 6, bottom - 40, cx + 32, bottom - 32], fill=STONE, outline=BROWN)
    # Scales of justice between the columns.
    mid_x = left + 185
    post_top = top + 96
    post_bottom = bottom - 34
    draw.line([(mid_x, post_top), (mid_x, post_bottom)], fill=INK, width=4)
    draw.line([(mid_x - 52, post_top + 16), (mid_x + 52, post_top + 16)], fill=INK, width=4)
    draw.ellipse([mid_x - 5, post_top + 8, mid_x + 5, post_top + 18], fill=RED)
    for pan_x in (mid_x - 52, mid_x + 52):
        draw.line([(pan_x, post_top + 16), (pan_x, post_top + 44)], fill=INK, width=2)
        draw.polygon(
            [(pan_x - 26, post_top + 44), (pan_x + 26, post_top + 44), (pan_x, post_top + 62)],
            fill=RED,
        )
    draw.line([(left, post_bottom), (right, post_bottom)], fill=(96, 110, 140), width=6)
    draw.rectangle([mid_x - 30, post_bottom - 6, mid_x + 30, post_bottom + 2], fill=INK)


def draw_lead(draw):
    draw.text((40, 198), "INTERNATIONAL JUSTICE  ·  THE HAGUE", font=f_sans_bold(16), fill=RED)
    y = 224
    y = draw_para(
        draw, 40, y, 545,
        "World court rules Myanmar committed genocide",
        f_serif_bold(41), INK, 50,
    )
    y += 6
    draw_para(
        draw, 40, y, 545,
        "The International Court of Justice found Myanmar responsible for "
        "genocide against the Rohingya — the court's first such finding "
        "against a state.",
        f_sans(18), INK, 24,
    )
    draw_courtroom(draw, 612, 198, 984, 392)
    draw_para(
        draw, 612, 398, 372,
        "The Peace Palace in The Hague, seat of the world court.",
        f_serif_italic(14), GREY, 19,
    )
    draw_rule(draw, 448)


def draw_card(draw, x, y, width, kicker, headline, body):
    draw.text((x, y), kicker, font=f_sans_bold(15), fill=RED)
    y += 24
    y = draw_para(draw, x, y, width, headline, f_serif_bold(21), INK, 26)
    y += 4
    draw_para(draw, x, y, width, body, f_sans(15), INK, 19)


def draw_grid(draw):
    columns = [40, 363, 686]
    width = 298
    cards = [
        (
            "DIPLOMACY  ·  SHENZHEN",
            "Three powers issue a joint peace declaration",
            "Trump, Xi and Putin pledge dialogue on nuclear risks after "
            "their first three-way summit: \u201ca nuclear war cannot be won\u201d.",
        ),
        (
            "UKRAINE  ·  WAR",
            "Russia hits Kyiv in overnight missile barrage",
            "Three killed as missiles and drones strike the capital, "
            "hitting bridges over the Dnipro; Ukraine hits a chemical "
            "plant in Russia.",
        ),
        (
            "MIDDLE EAST",
            "Houthi missile damages Riyadh\u2019s PIF tower",
            "A strike on the Saudi capital\u2019s financial district damages "
            "the sovereign wealth fund tower; the coalition hits Hodeida.",
        ),
        (
            "MARKETS  ·  AI",
            "Stocks slide as doubts over AI valuations grow",
            "The S&P 500 falls about 2%, its fifth straight loss; the "
            "Nikkei drops 4.8% after Anthropic\u2019s Nasdaq debut.",
        ),
        (
            "CLIMATE  ·  COP31",
            "Draft deal drops the fossil-fuel phase-out",
            "Negotiators in Antalya remove any reference to ending fossil "
            "fuel use from a slimmed-down draft climate deal.",
        ),
        (
            "WEATHER  ·  INDIA",
            "Cyclone Akvan makes landfall in Odisha",
            "The storm comes ashore on India\u2019s east coast after bearing "
            "down for days, with coastal districts on alert.",
        ),
    ]
    rows = [462, 650]
    for index, (kicker, headline, body) in enumerate(cards):
        row = index // 3
        col = index % 3
        draw_card(draw, columns[col], rows[row], width, kicker, headline, body)
    for sep_x in (350, 673):
        draw.line([(sep_x, 462), (sep_x, 830)], fill=FAINT, width=1)
    draw_rule(draw, 842)


def draw_also_today(draw):
    draw.text((40, 854), "ALSO TODAY", font=f_sans_bold(17), fill=RED)
    briefs = [
        "Kenya's last Ebola patient discharged — 42-day countdown",
        "Israeli troops cross Gaza Yellow Line",
        "Tanker burns in Hormuz after hitting a mine",
        "GTA VI made $3.79bn on its first day",
        "EU and UK hold their second summit in Brussels",
        "White House fires cyber chief",
    ]
    left_x = 40
    right_x = 540
    y = 882
    for row in range(3):
        for col_x, text in ((left_x, briefs[row * 2]), (right_x, briefs[row * 2 + 1])):
            draw.ellipse([col_x, y + 5, col_x + 9, y + 14], fill=RED)
            draw.text((col_x + 18, y), text, font=f_sans(15), fill=INK)
        y += 26
    draw_rule(draw, 956)
    draw_centered(
        draw, 966,
        "Sources: WSJ · CNN · Reuters · AP · BBC · Fox · NY Post",
        f_sans(13), GREY,
    )
    draw_centered(
        draw, 986,
        "Built 21 Nov 2026, covering news reported on 20 Nov 2026",
        f_sans(13), GREY,
    )


def render_image():
    image = Image.new("RGB", (WIDTH, HEIGHT), PAPER)
    draw = ImageDraw.Draw(image)
    draw_masthead(draw)
    draw_lead(draw)
    draw_grid(draw)
    draw_also_today(draw)
    return image


def main():
    image = render_image()
    image.save("entry.png", format="PNG")


if __name__ == "__main__":
    main()
