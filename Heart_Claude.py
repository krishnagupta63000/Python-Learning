"""
Love Heart (v10)
 
A red "I love you" in many languages builds a heart, one word at a time.
The heart has the exact outline of the reference image.
Words sit in rows between the outline and the hollow in the middle, and no two
words overlap. The outline is built first, clockwise from the top, then the rows
fill inward.
Each word fades in smoothly (dark -> white -> red). Once the heart is complete,
the "Je t'aime" words, spread evenly across the heart, twinkle.
 
Standard library only (turtle + tkinter + random + time). Needs Python 3 with tkinter.
"""
import math
import random as r
import time
import turtle as t
import tkinter.font as tkfont
 
BG = "#000000"
RED = "#e0222e"
WHITE = "#ffffff"
ZOOM = 1.5              # the heart, the words and the spacing are this many times bigger
WIN_W, WIN_H = 880, 800 # window size, wide enough for the bigger heart
SCALE = 16.5 * ZOOM     # pixels per unit of heart coordinates
 
# Outline of the heart, traced from the reference image (width 32 units, centred on (0, 0),
# y pointing up). Points go around the heart in order.
HEART_OUTLINE = [
    (-8.04, 14.61), (-8.43, 14.50), (-8.84, 14.46), (-9.23, 14.34), (-9.63, 14.26), (-10.01, 14.13), (-10.40, 13.98), (-10.77, 13.83),
    (-11.15, 13.66), (-11.51, 13.47), (-11.87, 13.28), (-12.21, 13.05), (-12.55, 12.82), (-12.86, 12.56), (-13.19, 12.31), (-13.49, 12.03),
    (-13.76, 11.73), (-14.01, 11.41), (-14.28, 11.09), (-14.51, 10.75), (-14.74, 10.41), (-14.94, 10.06), (-15.12, 9.69), (-15.29, 9.32),
    (-15.44, 8.94), (-15.58, 8.56), (-15.71, 8.17), (-15.77, 7.77), (-15.90, 7.38), (-15.92, 6.97), (-15.95, 6.56), (-16.00, 6.15),
    (-16.00, 5.74), (-15.97, 5.34), (-15.92, 4.93), (-15.92, 4.52), (-15.82, 4.12), (-15.75, 3.72), (-15.63, 3.33), (-15.52, 2.94),
    (-15.39, 2.55), (-15.22, 2.18), (-15.05, 1.81), (-14.86, 1.44), (-14.66, 1.09), (-14.45, 0.74), (-14.22, 0.39), (-13.99, 0.06),
    (-13.74, -0.26), (-13.48, -0.58), (-13.24, -0.91), (-12.96, -1.21), (-12.67, -1.50), (-12.38, -1.79), (-12.09, -2.08), (-11.80, -2.37),
    (-11.51, -2.66), (-11.21, -2.93), (-10.88, -3.18), (-10.57, -3.44), (-10.27, -3.73), (-9.95, -3.98), (-9.62, -4.23), (-9.32, -4.50),
    (-8.99, -4.74), (-8.67, -5.00), (-8.35, -5.26), (-8.02, -5.50), (-7.72, -5.77), (-7.38, -6.00), (-7.07, -6.27), (-6.74, -6.52),
    (-6.42, -6.77), (-6.12, -7.04), (-5.79, -7.29), (-5.47, -7.55), (-5.18, -7.84), (-4.88, -8.11), (-4.58, -8.39), (-4.27, -8.66),
    (-3.98, -8.95), (-3.70, -9.25), (-3.43, -9.55), (-3.16, -9.86), (-2.87, -10.15), (-2.61, -10.47), (-2.37, -10.80), (-2.10, -11.11),
    (-1.87, -11.45), (-1.63, -11.78), (-1.41, -12.12), (-1.19, -12.47), (-0.98, -12.82), (-0.77, -13.17), (-0.57, -13.53), (-0.38, -13.89),
    (-0.20, -14.26), (-0.02, -14.63), (0.20, -14.45), (0.36, -14.07), (0.55, -13.70), (0.74, -13.34), (0.94, -12.99), (1.15, -12.63),
    (1.37, -12.29), (1.58, -11.94), (1.81, -11.60), (2.06, -11.28), (2.29, -10.94), (2.55, -10.62), (2.81, -10.30), (3.05, -9.98),
    (3.33, -9.68), (3.62, -9.39), (3.91, -9.09), (4.19, -8.80), (4.49, -8.51), (4.78, -8.23), (5.07, -7.94), (5.37, -7.66),
    (5.68, -7.40), (6.01, -7.15), (6.31, -6.87), (6.63, -6.62), (6.96, -6.37), (7.26, -6.10), (7.60, -5.86), (7.91, -5.60),
    (8.23, -5.34), (8.56, -5.10), (8.87, -4.83), (9.20, -4.60), (9.51, -4.33), (9.83, -4.07), (10.16, -3.83), (10.46, -3.55),
    (10.77, -3.28), (11.09, -3.03), (11.40, -2.76), (11.69, -2.47), (11.98, -2.18), (12.27, -1.89), (12.56, -1.60), (12.85, -1.31),
    (13.14, -1.02), (13.40, -0.71), (13.64, -0.37), (13.91, -0.07), (14.13, 0.28), (14.37, 0.61), (14.59, 0.95), (14.79, 1.31),
    (14.98, 1.67), (15.15, 2.04), (15.32, 2.42), (15.46, 2.80), (15.59, 3.19), (15.72, 3.58), (15.78, 3.98), (15.90, 4.37),
    (15.91, 4.78), (15.94, 5.19), (15.98, 5.59), (16.00, 6.00), (15.97, 6.41), (15.92, 6.82), (15.91, 7.23), (15.81, 7.62),
    (15.74, 8.02), (15.61, 8.41), (15.49, 8.80), (15.35, 9.18), (15.18, 9.56), (15.00, 9.93), (14.80, 10.28), (14.59, 10.63),
    (14.37, 10.98), (14.11, 11.29), (13.87, 11.62), (13.60, 11.93), (13.31, 12.22), (12.99, 12.48), (12.67, 12.73), (12.35, 12.99),
    (12.00, 13.21), (11.65, 13.41), (11.29, 13.61), (10.92, 13.78), (10.55, 13.95), (10.16, 14.09), (9.77, 14.21), (9.38, 14.31),
    (8.99, 14.43), (8.58, 14.47), (8.18, 14.56), (7.78, 14.62), (7.37, 14.63), (6.96, 14.63), (6.55, 14.62), (6.15, 14.53),
    (5.75, 14.46), (5.35, 14.38), (4.96, 14.28), (4.58, 14.13), (4.20, 13.99), (3.82, 13.82), (3.46, 13.64), (3.10, 13.44),
    (2.75, 13.22), (2.41, 12.99), (2.09, 12.74), (1.75, 12.51), (1.46, 12.23), (1.17, 11.94), (0.88, 11.65), (0.59, 11.36),
    (0.31, 11.06), (0.05, 10.74), (-0.29, 10.90), (-0.53, 11.23), (-0.79, 11.54), (-1.07, 11.84), (-1.36, 12.13), (-1.66, 12.41),
    (-1.97, 12.67), (-2.30, 12.92), (-2.62, 13.17), (-2.97, 13.39), (-3.32, 13.60), (-3.68, 13.79), (-4.05, 13.96), (-4.43, 14.13),
    (-4.81, 14.27), (-5.20, 14.38), (-5.60, 14.46), (-6.00, 14.54), (-6.40, 14.62), (-6.81, 14.63), (-7.22, 14.63), (-7.63, 14.63),
]
 
INNER_SCALE = 0.0       # 0 = solid heart (fills the middle too); 0.6 = the hollow from the 12:42 PM version
ROW_H = 14 * ZOOM       # starting row height, px (taller rows are used for taller scripts)
ROW_MIN = 11 * ZOOM     # rows never get shorter than this, px
WORD_GAP = 3 * ZOOM     # smallest space between two words in a row, px
EDGE = 1 * ZOOM         # how close words may sit to the outline, px
SIZE_RANGE = (round(9 * ZOOM), round(12 * ZOOM))   # font sizes for the words, smallest and largest
TAIL_WIDTH = 160 * ZOOM # rows narrower than this, near the point, use the widest words that fit
TAIL_SIZE_MIN = round(6 * ZOOM)   # smallest font size, used only near the point
TWINKLE_WORD = "Je t'aime"
TWINKLE_RATIO = 0.10    # about one "Je t'aime" in every ten words
 
# Speed and smoothness
SPEED = 0.5                         # 0.5 = half the speed of the previous version
BASE_STEP_MS = 40                   # previous version: one new word every 40 ms
WORD_STEP_MS = BASE_STEP_MS / SPEED # 80 ms between one word and the next
FADE_MS = 500                       # time for one word to fade in and settle
TWINKLE_MS = 420                    # time for one "Je t'aime" sparkle
TWINKLE_COOLDOWN_MS = (150, 600)    # random pause between sparkles (shorter = more frequent)
FRAME_MS = 16                       # about 60 frames per second
 
PHRASES = [
    "Seni seviyorum", "Te amo", "Je t'aime",
    "Ich liebe dich", "Ti amo", "Eu te amo", "Я тебя люблю",
    "사랑해", "愛してる", "我爱你",
    "Σ' αγαπώ", "Ik hou van jou", "Jag älskar dig", "Kocham cię",
    "ฉันรักเธอ", "Anh yêu em", "Aku cinta kamu", "Я тебе кохаю",
]
# Words for the rows. "Je t'aime" is added afterwards, spread across the heart.
WORD_POOL = [p for p in PHRASES if p != TWINKLE_WORD]
 
# Fonts to try for each script, in order. The first one installed wins.
SCRIPT_FONTS = {
    "korean":     ["Malgun Gothic", "Apple SD Gothic Neo", "Arial Unicode MS"],
    "japanese":   ["Yu Gothic UI", "Hiragino Sans", "Arial Unicode MS"],
    "chinese":    ["Microsoft YaHei UI", "PingFang SC", "Arial Unicode MS"],
    "devanagari": ["Nirmala UI", "Kohinoor Devanagari", "Arial Unicode MS"],
    "thai":       ["Leelawadee UI", "Thonburi", "Arial Unicode MS"],
    "latin":      ["Arial", "Helvetica Neue", "Segoe UI"],
}
 
rng = r.Random(11)
FAMILIES = set()        # filled in by main() with the fonts this computer has
_fonts = {}
 
 
# ---------- fonts ----------
 
def script_of(text):
    def has(lo, hi):
        return any(lo <= ch <= hi for ch in text)
    if has("\uac00", "\ud7a3"):
        return "korean"
    if has("\u3040", "\u30ff"):        # kana means Japanese
        return "japanese"
    if has("\u4e00", "\u9fff"):        # other CJK ideographs
        return "chinese"
    if has("\u0900", "\u097f"):
        return "devanagari"
    if has("\u0e00", "\u0e7f"):
        return "thai"
    return "latin"
 
 
def pick_family(script):
    for name in SCRIPT_FONTS[script]:
        if name in FAMILIES:
            return name
    return SCRIPT_FONTS[script][0]
 
 
def font_for(text, size):
    family = pick_family(script_of(text))
    key = (family, size)
    if key not in _fonts:
        _fonts[key] = tkfont.Font(family=family, size=size, weight="bold")
    return _fonts[key]
 
 
def tk_measure(text, size):
    """Real (width, height) of a word in pixels, used by the layout."""
    font = font_for(text, size)
    return font.measure(text), font.metrics("linespace")
 
 
# ---------- heart shape ----------
 
def heart_outline(scale, samples=None):
    """The heart's outline in window pixels, centred on (0, 0). Uses the outline
    traced from the reference image, so the shape matches it exactly."""
    return [(x * scale * SCALE, y * scale * SCALE) for x, y in HEART_OUTLINE]
 
 
def crossings(outline, y):
    """Sorted x positions where the outline crosses the horizontal line at y."""
    xs = []
    closed = outline + outline[:1]
    for (x0, y0), (x1, y1) in zip(closed, closed[1:]):
        if (y0 <= y < y1) or (y1 <= y < y0):
            xs.append(x0 + (x1 - x0) * (y - y0) / (y1 - y0))
    return sorted(xs)
 
 
def intervals(outline, y):
    """Spans of the line at height y that are inside the outline."""
    xs = crossings(outline, y)
    return [(xs[i], xs[i + 1]) for i in range(0, len(xs) - 1, 2)]
 
 
def intersect(spans_a, spans_b):
    """Parts of the spans that appear in both lists."""
    out = []
    for a0, a1 in spans_a:
        for b0, b1 in spans_b:
            lo, hi = max(a0, b0), min(a1, b1)
            if lo < hi:
                out.append((lo, hi))
    return out
 
 
def minus(spans, holes):
    """Remove the hole spans from the spans. Returns what is left."""
    out = []
    for a, b in spans:
        cur = a
        for c, d in sorted(holes):
            if d <= cur or c >= b:
                continue
            if c > cur:
                out.append((cur, c))
            cur = max(cur, d)
        if cur < b:
            out.append((cur, b))
    return out
 
 
def overlap(a, b):
    """True if two boxes (left, bottom, right, top) overlap."""
    return a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]
 
 
def box_of(cx, cy, w, h):
    return (cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2)
 
 
def rect_distance(px, py, box):
    """Distance from a point to a rectangle (0 if the point is inside it)."""
    x0, y0, x1, y1 = box
    dx = max(x0 - px, 0, px - x1)
    dy = max(y0 - py, 0, py - y1)
    return math.hypot(dx, dy)
 
 
def clockwise_angle(x, y):
    """Angle around the heart's center: 0 at the top, growing clockwise on screen."""
    return (math.pi / 2 - math.atan2(y, x)) % (2 * math.pi)
 
 
# ---------- layout ----------
 
def row_spans(outer, inner, top_y, row_h):
    """Parts of one row (from top_y down to top_y - row_h) that can hold words."""
    up, down = top_y - 1, top_y - row_h + 1
    spans = intersect(intervals(outer, up), intervals(outer, down))
    if not spans:   # the heart is pointed here: use the middle of the row
        spans = intervals(outer, top_y - row_h / 2)
    holes = intervals(inner, up) + intervals(inner, down) if inner else []
    return minus(spans, holes)
 
 
def fill_tail(width, measure):
    """The narrow part of the heart, near the point: pick the widest words that
    still fit, so the text follows the outline down to the tip."""
    chosen = []
    order = WORD_POOL[:]
    rng.shuffle(order)
    while True:
        used = sum(cw for _, _, cw, _ in chosen) + WORD_GAP * max(len(chosen) - 1, 0)
        room = width - used
        need_gap = WORD_GAP if chosen else 0
        best = None
        for phrase in order:
            if any(p == phrase for p, *_ in chosen):
                continue
            for size in range(SIZE_RANGE[1], TAIL_SIZE_MIN - 1, -1):
                w, h = measure(phrase, size)
                if w + need_gap <= room:          # the largest size that fits
                    if best is None or w > best[2]:
                        best = (phrase, size, w, h)
                    break
        if best is None:
            return chosen
        chosen.append(best)
 
 
def fill_row(outer, inner, top_y, row_h, measure, next_phrase):
    """Fill one row with words that reach both ends of each span.
    Returns (center x, phrase, size, width, height) for every word in the row."""
    placed = []
    for a, b in row_spans(outer, inner, top_y, row_h):
        left, right = a + EDGE, b - EDGE
        width = right - left
        if width <= 0:
            continue
 
        if width < TAIL_WIDTH:
            chosen = fill_tail(width, measure)
        else:
            # add words until no phrase fits in what is left. Each word tries its
            # preferred size first, then smaller sizes, so gaps close up.
            chosen, misses = [], 0
            while misses < len(WORD_POOL):
                phrase = next_phrase()
                preferred = rng.randint(*SIZE_RANGE)
                fit = None
                for size in range(preferred, SIZE_RANGE[0] - 1, -1):
                    w, h = measure(phrase, size)
                    used = sum(cw for _, _, cw, _ in chosen) + WORD_GAP * len(chosen)
                    if used + w <= width:
                        fit = (size, w, h)
                        break
                if fit:
                    chosen.append((phrase, fit[0], fit[1], fit[2]))
                    misses = 0
                else:
                    misses += 1
        if not chosen:
            continue
 
        # first word on the left edge, last word on the right edge,
        # and the leftover room is shared by the gaps
        words_w = sum(cw for _, _, cw, _ in chosen)
        gaps = len(chosen) - 1
        if gaps:
            gap = (width - words_w) / gaps
            x = left
        else:
            gap = 0
            x = left + (width - words_w) / 2
        for phrase, size, w, h in chosen:
            placed.append((x + w / 2, phrase, size, w, h))
            x += w + gap
    return placed
 
 
def layout(measure):
    """Fill the heart with rows of words, top to bottom. Returns (x, y, phrase,
    size, ring) tuples in the order they should build: the outline first,
    clockwise from the top, then the inner rings, also clockwise."""
    outer = heart_outline(1.0)
    inner = heart_outline(INNER_SCALE) if INNER_SCALE > 0 else None
    top = max(y for _, y in outer)
    bottom = min(y for _, y in outer)
 
    bag = []
 
    def next_phrase():
        nonlocal bag
        if not bag:
            bag = WORD_POOL[:]
            rng.shuffle(bag)
        return bag.pop()
 
    # rows: (center y, [(x, phrase, size, w, h), ...])
    words = []
    cursor = top                    # top edge of the row being built
    while cursor - ROW_H > bottom:
        row_h = ROW_H
        for _ in range(4):
            row = fill_row(outer, inner, cursor, row_h, measure, next_phrase)
            need = max((h for *_, h in row), default=0)
            if need > row_h:
                row_h = need        # a taller script needs a taller row
                continue
            break
        if not row:
            cursor -= ROW_H
            continue
        # shrink the row to its tallest word, so rows of small words pack tighter
        row_h = max(need, ROW_MIN)
        cy = cursor - row_h / 2
        for cx, phrase, size, w, h in row:
            words.append([cx, cy, phrase, size, w, h])
        cursor -= row_h
 
    spread_twinkle(words, measure)
 
    # rank each word: its ring (how far it sits from the outline), then its
    # clockwise angle, so the outline is built in one clockwise sweep
    ranked = []
    for cx, cy, phrase, size, w, h in words:
        box = box_of(cx, cy, w, h)
        depth = min(rect_distance(px, py, box) for px, py in outer)
        ring = int(depth // ROW_H)
        ranked.append((ring, clockwise_angle(cx, cy), cx, cy, phrase, size))
    ranked.sort(key=lambda f: (f[0], f[1]))
    return [(cx, cy, phrase, size, ring) for ring, _, cx, cy, phrase, size in ranked]
 
 
def spread_twinkle(words, measure):
    """Turn some words into "Je t'aime", spaced evenly across the whole heart.
    Each one is picked to be as far as possible from the ones already chosen,
    and only if it still fits without touching any other word."""
    boxes = [box_of(cx, cy, w, h) for cx, cy, _, _, w, h in words]
    count = max(4, round(len(words) * TWINKLE_RATIO))
    chosen = []                             # centers of the "Je t'aime" words
 
    for _ in range(count):
        def spacing(i):
            cx, cy = words[i][0], words[i][1]
            if not chosen:
                return cy                   # the first one goes at the top
            return min(math.hypot(cx - x, cy - y) for x, y in chosen)
 
        for i in sorted(range(len(words)), key=spacing, reverse=True):
            cx, cy, phrase, size, w, h = words[i]
            if phrase == TWINKLE_WORD:
                continue
            # shrink "Je t'aime" if needed, so it is no wider than the word it replaces
            new_size = size
            nw, nh = measure(TWINKLE_WORD, new_size)
            while nw > w + 4 * ZOOM and new_size > TAIL_SIZE_MIN:
                new_size -= 1
                nw, nh = measure(TWINKLE_WORD, new_size)
            if nw > w + 4 * ZOOM:
                continue
            nb = box_of(cx, cy, nw, nh)
            if any(overlap(nb, boxes[j]) for j in range(len(words)) if j != i):
                continue
            words[i] = [cx, cy, TWINKLE_WORD, new_size, nw, nh]
            boxes[i] = nb
            chosen.append((cx, cy))
            break
 
 
# ---------- colors and easing ----------
 
def blend(a, b, amount):
    """Mix two #rrggbb colors. amount 0 gives a, 1 gives b."""
    pa = [int(a[i:i + 2], 16) for i in (1, 3, 5)]
    pb = [int(b[i:i + 2], 16) for i in (1, 3, 5)]
    mixed = [round(x + (y - x) * amount) for x, y in zip(pa, pb)]
    return "#%02x%02x%02x" % tuple(mixed)
 
 
def ease_out(t_):
    return 1 - (1 - t_) ** 2
 
 
def smooth(t_):
    return t_ * t_ * (3 - 2 * t_)
 
 
def build_color(p):
    """A word fading in: dark -> white -> red, eased. p runs 0 to 1."""
    if p < 0.4:
        return blend(BG, WHITE, smooth(p / 0.4))
    return blend(WHITE, RED, smooth((p - 0.4) / 0.6))
 
 
def twinkle_color(p):
    """One smooth sparkle: red -> white -> red. p runs 0 to 1."""
    return blend(RED, WHITE, 0.5 - 0.5 * math.cos(2 * math.pi * p))
 
 
# ---------- animation ----------
 
class Heart:
    def __init__(self, canvas, words, clock=None):
        self.cv = canvas
        self.clock = clock or (lambda: time.perf_counter() * 1000)
        self.order = []     # canvas item for each word, in build order
        self.twinkle = []   # canvas items for the "Je t'aime" words
        for x, y, phrase, size, _ring in words:
            # turtle's canvas has y pointing up, Tk's points down, so negate y
            item = canvas.create_text(x, -y, text=phrase, fill=BG,
                                      font=font_for(phrase, size), anchor="center")
            self.order.append(item)
            if phrase == TWINKLE_WORD:
                self.twinkle.append(item)
        self.start = None   # time the build started, in ms
        self.last = None    # time of the previous frame, in ms
        self.started = 0    # how many words have started to build
        self.active = {}    # item -> (kind, start time in ms)
        self.cool = {}      # twinkle item -> ms until its next sparkle
 
    def tick(self, screen):
        now = self.clock()
        if self.start is None:
            self.start = self.last = now
        dt = min(now - self.last, 50)       # ms since the last frame
        self.last = now
 
        # 1) start every word whose time has come. Each word starts at its
        #    own scheduled time, so the sweep keeps an even rhythm.
        while (self.started < len(self.order)
               and self.start + self.started * WORD_STEP_MS <= now):
            t0 = self.start + self.started * WORD_STEP_MS
            self.active[self.order[self.started]] = ("build", t0)
            self.started += 1
 
        # 2) move every running fade or sparkle forward to this moment
        for item, (kind, t0) in list(self.active.items()):
            length = FADE_MS if kind == "build" else TWINKLE_MS
            p = (now - t0) / length
            if p >= 1:
                self.cv.itemconfig(item, fill=RED)
                del self.active[item]
                if kind == "twinkle":
                    self.cool[item] = rng.uniform(*TWINKLE_COOLDOWN_MS)
            else:
                color = build_color(p) if kind == "build" else twinkle_color(p)
                self.cv.itemconfig(item, fill=color)
 
        # 3) once every word is in place, only the "Je t'aime" words sparkle
        building = (self.started < len(self.order)
                    or any(kind == "build" for kind, _ in self.active.values()))
        if not building:
            for item in self.twinkle:
                if item in self.active:
                    continue
                if item not in self.cool:
                    self.cool[item] = rng.uniform(0, TWINKLE_COOLDOWN_MS[1])
                self.cool[item] -= dt
                if self.cool[item] <= 0:
                    del self.cool[item]
                    self.active[item] = ("twinkle", now)
 
        screen.update()
        screen.ontimer(lambda: self.tick(screen), FRAME_MS)
 
 
def main():
    global FAMILIES
    s = t.Screen()
    s.setup(WIN_W, WIN_H)
    s.bgcolor(BG)
    s.title("Love Heart")
    s.tracer(0)                 # we redraw by hand, so turn off auto-refresh
    cv = s.getcanvas()          # the Tk canvas under the turtle screen
    FAMILIES = set(tkfont.families(cv.winfo_toplevel()))
 
    heart = Heart(cv, layout(tk_measure))
    s.ontimer(lambda: heart.tick(s), FRAME_MS)
    t.done()
 
 
if __name__ == "__main__":
    main()