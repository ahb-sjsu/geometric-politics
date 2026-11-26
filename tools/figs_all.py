"""Figures for Geometric Politics, Chapters 1 to 12, 14, 16, 17 and 18 (2026-11-25).

Chapters 13 and 15 are not published and have no figures here.

Rules this module keeps (see figkit.py and CORRECTIONS-2026-11-26.md):
- District 7 is fictional; every figure drawn from it says "illustrative" or "hypothetical"
  in the figure and in the caption.
- No number from the "Unresolved" list of the corrections file is drawn: not the District 7
  covariance matrix or its eigenvalues, not the centroid or bloc distances of Chapters 7 to 9,
  not the information-preservation percentages, not a Bond Index, not the Polarization
  Illusion construction, not the gerrymandering criterion.
- The Campaign Gradient Theorem is drawn in its one form, variance plus squared offset.
- Chapter 17: the group of the Hohfeldian positions is the Klein four-group V4. No dihedral
  group, no quarter-turn, no eight-element table.
"""

import math
from xml.sax.saxutils import escape

from figkit import BORDER, BOX, CRITICAL, GOOD, GRID, INK, INK2, INK3, SERIES, SURFACE, Axes, Canvas, legend, reg
from svgfig import FONT

P1 = "manuscript/part_i/"
P2 = "manuscript/part_ii/"
P3 = "manuscript/part_iii/"
P4 = "manuscript/part_iv/"
P5 = "manuscript/part_v/"


# ------------------------------------------------------------------ helpers
def canvas(w, h, title):
    assert len(title) <= 68, (len(title), title)
    return Canvas(w, h, title)


def polygon(c, pts, fill, opacity=0.25, stroke="none", width=1.0):
    d = " ".join(f"{x:.2f},{y:.2f}" for x, y in pts)
    c.add(f'<polygon points="{d}" fill="{fill}" fill-opacity="{opacity}" stroke="{stroke}" stroke-width="{width}"/>')


def circle(c, x, y, r, stroke, width=1.5, fill="none", opacity=1.0, dash=None):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    c.add(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r:.2f}" fill="{fill}" fill-opacity="{opacity}" '
          f'stroke="{stroke}" stroke-width="{width}"{da}/>')


def mbox(c, x, y, w, h, lines, sub=(), stroke=BORDER, fill=BOX):
    """Box with one or more bold lines and optional small sub-lines, centred."""
    c.add(f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" rx="6" fill="{fill}" '
          f'stroke="{stroke}" stroke-width="1"/>')
    n = len(lines) + len(sub)
    y0 = y + h / 2 - (n - 1) * 7.5 + 4
    for i, s in enumerate(lines):
        c.text(x + w / 2, y0 + 15 * i, s, 12, "middle", INK, "600")
    for j, s in enumerate(sub):
        c.text(x + w / 2, y0 + 15 * (len(lines) + j), s, 10.5, "middle", INK2)


def gauss(x, m, s):
    return math.exp(-0.5 * ((x - m) / s) ** 2) / (s * math.sqrt(2 * math.pi))


def htext(c, x, y, s, size=11, anchor="start", color=INK, weight="normal"):
    """Text with a surface-coloured halo, for a label that must sit where hairlines pass."""
    c.add(f'<text x="{x:.2f}" y="{y:.2f}" font-family="{FONT}" font-size="{size}" fill="{color}" '
          f'text-anchor="{anchor}" font-weight="{weight}" stroke="{SURFACE}" stroke-width="4" '
          f'stroke-linejoin="round" paint-order="stroke">{escape(str(s))}</text>')


# ------------------------------------------------------------------ chapter 1
def fig_1_1():
    pts = {"libertarian": (0.8, -0.8), "communitarian populist": (-0.8, 0.8), "centrist": (0.0, 0.0),
           "conservative on both": (0.8, 0.8), "progressive on both": (-0.8, -0.8)}
    score = {k: (a + b) / 2 for k, (a, b) in pts.items()}
    assert score["libertarian"] == score["communitarian populist"] == score["centrist"] == 0.0
    assert abs(score["conservative on both"] - 0.8) < 1e-12 and abs(score["progressive on both"] + 0.8) < 1e-12
    p = reg(P1 + "ch01_left_right_trap.md", "1.1",
            "Economic policy (d1, left to right) against social values (d2, liberal to conservative), with the "
            "one-dimensional score taken, as the chapter's averaging example takes it, as the average of the two. "
            "Every voter on one dashed line receives the same score. The libertarian, the communitarian populist and "
            "the centrist all score 0, and nothing computed from the score can tell them apart. The positions are "
            "illustrative.",
            "## District 7: Five Elections, Five Winners")
    c = canvas(720, 400, "Different voters, one shadow on the left-right axis")
    cx, cy, s, R = 250, 205, 100, 1.45

    def P(a, b):
        return cx + s * a, cy - s * b

    c.line(cx - s * R, cy, cx + s * R, cy, GRID, 1)
    c.line(cx, cy - s * R, cx, cy + s * R, GRID, 1)
    # iso-score lines d1 + d2 = 2 sigma, clipped to the square
    for sig in (-0.8, 0.0, 0.8):
        k = 2 * sig
        a0, a1 = max(-R, k - R), min(R, k + R)
        (x1, y1), (x2, y2) = P(a0, k - a0), P(a1, k - a1)
        c.line(x1, y1, x2, y2, INK3, 1.2, dash="5 5")
        lab = "score 0" if sig == 0 else f"score {sig:+.1f}".replace("-", "−")
        if sig < 0:
            c.text(x2 - 8, y2 + 14, lab, 10.5, "end", INK2, italic=True)
        else:
            c.text(x2 + 6, y2 + 4, lab, 10.5, "start", INK2, italic=True)
    # the score axis along the diagonal
    (xa, ya), (xb, yb) = P(-1.35, -1.35), P(1.35, 1.35)
    c.arrow(xa, ya, xb, yb, INK2, 1.5)
    c.text(xb + 8, yb + 2, "left-right score", 11, "start", INK)
    c.text(cx, cy - s * R - 8, "conservative", 10.5, "middle", INK2)
    c.text(cx + 6, cy + s * R + 2, "liberal", 10.5, "start", INK2)
    c.text(cx - s * R - 6, cy + 4, "left", 10.5, "end", INK2)
    c.text(cx + s * R + 6, cy + 4, "right", 10.5, "start", INK2)
    for name, (a, b) in pts.items():
        x, y = P(a, b)
        col = SERIES[1] if score[name] == 0 else SERIES[0]
        c.dot(x, y, col, 5.5, title=f"{name}: score {score[name]:g}")
    lx = {"libertarian": (12, -6, "start"), "communitarian populist": (-10, 18, "end"), "centrist": (13, 4, "start"),
          "conservative on both": (12, 4, "start"), "progressive on both": (-12, 4, "end")}
    for name, (dx, dy, anc) in lx.items():
        x, y = P(*pts[name])
        htext(c, x + dx, y + dy, name, 11, anc, INK)
    x0 = 486
    c.text(x0, 104, "three voters, one score: 0", 12, "start", INK, "600")
    rows = [("libertarian", "right on d1, liberal on d2"), ("communitarian populist", "left on d1, conservative on d2"),
            ("centrist", "center on both")]
    for i, (a, b) in enumerate(rows):
        c.text(x0, 132 + 40 * i, a, 11.5, "start", INK)
        c.text(x0, 148 + 40 * i, b, 10.5, "start", INK2)
    c.text(x0, 268, "where a voter sits along", 11, "start", INK2, italic=True)
    c.text(x0, 284, "a dashed line is what the", 11, "start", INK2, italic=True)
    c.text(x0, 300, "score throws away", 11, "start", INK2, italic=True)
    c.text(16, 390, "horizontal: d1 economic policy; vertical: d2 social values; positions illustrative", 10.5,
           "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 2
def fig_2_1():
    a = [("approve on every dimension", 47), ("disapprove on every dimension", 53)]
    b = [("d1 economic", 70), ("d3 environment", 60), ("d4 foreign policy", 40), ("d2 social", 30),
         ("d5 institutions", 25)]
    cc = [("strongly approve", 20), ("mildly approve", 27), ("mildly disapprove", 18), ("strongly disapprove", 35)]
    d = [("urban core", 67), ("inner suburbs", 45), ("outer suburbs", 38), ("exurban fringe", 29)]
    assert sum(v for _, v in a) == 100 and sum(v for _, v in cc) == 100
    assert cc[0][1] + cc[1][1] == 47 and cc[2][1] + cc[3][1] == 53
    p = reg(P1 + "ch02_polling_paradox.md", "2.1",
            "The chapter's four hypothetical electorates that all report 47% approval. (A) The same 47% approve on "
            "every dimension. (B) Approval differs by dimension. (C) Approval differs by intensity: 20% strong plus "
            "27% mild approval make the 47%. (D) Approval differs by place. In (B) and (D) the chapter calls the 47% a "
            "weighted average, weighted by salience in (B) and by population in (D); the weights are not given, so "
            "the dashed line marks 47% for comparison only.",
            "## The Favorability Paradox")
    c = canvas(720, 460, "One approval rating of 47%, four different electorates")
    # panel frames
    panels = [(20, 52, "A. uniform"), (372, 52, "B. by dimension"), (20, 256, "C. by intensity"),
              (372, 256, "D. by place")]
    for x, y, t in panels:
        c.text(x, y + 14, t, 12.5, "start", INK, "600")
    # A: one stacked bar
    x0, y0, W = 30, 120, 300
    xs = x0
    for i, (lab, v) in enumerate(a):
        w = W * v / 100
        c.add(f'<rect x="{xs + 1:.2f}" y="{y0:.2f}" width="{w - 2:.2f}" height="24" fill="{SERIES[i]}">'
              f'<title>{lab} {v}%</title></rect>')
        c.text(xs + w / 2, y0 - 8, f"{v}%", 11.5, "middle", INK)
        xs += w
    c.text(x0, y0 + 46, "47% approve on every dimension", 11, "start", INK2)
    c.text(x0, y0 + 62, "53% disapprove on every dimension", 11, "start", INK2)
    # B and D: horizontal bars with a 47 line
    def hbars(x, y, rows, labw=118, W=180, rh=24):
        for i, (lab, v) in enumerate(rows):
            yy = y + rh * i
            c.text(x + labw - 8, yy + 13, lab, 11, "end", INK2)
            c.hrect(x + labw, yy + 3, W * v / 100, 14, SERIES[0], title=f"{lab} {v}%")
            c.text(x + labw + W + 36, yy + 14, f"{v}%", 10.5, "end", INK)
        xr = x + labw + W * 0.47
        c.line(xr, y - 4, xr, y + rh * len(rows) + 2, INK3, 1.2, dash="4 4")
        c.text(xr, y + rh * len(rows) + 16, "47%", 10.5, "middle", INK2, italic=True)

    hbars(372, 80, b)
    hbars(372, 286, d)
    # C: intensity stacked bar
    x0, y0 = 30, 318
    cols = [(SERIES[0], 1.0), (SERIES[0], 0.5), (SERIES[1], 0.5), (SERIES[1], 1.0)]
    xs = x0
    mids = []
    for (lab, v), (col, op) in zip(cc, cols):
        w = W * v / 100
        c.add(f'<rect x="{xs + 1:.2f}" y="{y0:.2f}" width="{w - 2:.2f}" height="24" fill="{col}" '
              f'fill-opacity="{op}"><title>{lab} {v}%</title></rect>')
        c.text(xs + w / 2, y0 - 8, f"{v}", 11.5, "middle", INK)
        mids.append((xs, w))
        xs += w
    xa = x0 + W * 0.47
    c.line(x0 + 1, y0 + 32, xa - 3, y0 + 32, INK3, 1.2)
    c.line(xa + 3, y0 + 32, x0 + W - 1, y0 + 32, INK3, 1.2)
    c.text((x0 + xa) / 2, y0 + 48, "approve 47", 11, "middle", INK2)
    c.text((xa + x0 + W) / 2, y0 + 48, "disapprove 53", 11, "middle", INK2)
    c.text(x0, y0 + 74, "strong, mild | mild, strong;  net −6", 10.5, "start", INK3, italic=True)
    c.text(16, 450, "hypothetical scenarios, as the chapter states them", 10.5, "start", INK3, italic=True)
    c.save(p)


def fig_2_2():
    A, B = (-1.3, -0.6), (1.3, 0.6)
    ux, uy = B[0] - A[0], B[1] - A[1]
    n = math.hypot(ux, uy)
    ux, uy = ux / n, uy / n
    wx, wy = -uy, ux
    voters = {"v1": (-0.9, 0.35), "v2": (1.0, -0.25), "v3": (1.65 * wx, 1.65 * wy)}

    def proj(v):
        return v[0] * ux + v[1] * uy

    def dist(v, q):
        return math.hypot(v[0] - q[0], v[1] - q[1])

    assert proj(voters["v1"]) < 0 and dist(voters["v1"], A) < dist(voters["v1"], B)
    assert proj(voters["v2"]) > 0 and dist(voters["v2"], B) < dist(voters["v2"], A)
    assert abs(dist(voters["v3"], A) - dist(voters["v3"], B)) < 1e-12
    p = reg(P1 + "ch02_polling_paradox.md", "2.2",
            "A head-to-head poll as the chapter describes it, drawn in two dimensions. The line through candidates A "
            "and B is the poll's axis, and each voter is counted for the candidate on whose side of the dashed "
            "bisector the voter's projection falls. The voter at the top differs from both candidates on a direction "
            "neither of them distinguishes, and the poll can record only a toss-up. Change the candidates and the "
            "axis turns. The positions are illustrative.",
            "## The Issue Priority Trap")
    c = canvas(720, 400, "A head-to-head poll measures the axis the two candidates define")
    cx, cy, s = 255, 222, 92

    def P(a, b):
        return cx + s * a, cy - s * b

    c.add(f'<rect x="{cx - s * 2.3:.2f}" y="{cy - s * 1.75:.2f}" width="{s * 4.6:.2f}" height="{s * 3.5:.2f}" '
          f'fill="none" stroke="{GRID}" stroke-width="1"/>')
    # axis through A and B
    t = 2.25
    c.line(*P(-t * ux, -t * uy), *P(t * ux, t * uy), INK2, 1.5)
    c.text(*[v + d for v, d in zip(P(-2.25 * ux, -2.25 * uy), (6, 20))], "poll axis", 10.5, "start", INK2,
           italic=True)
    # bisector
    tb = 1.72
    c.line(*P(-0.95 * wx, -0.95 * wy), *P(tb * wx, tb * wy), INK3, 1.3, dash="5 5")
    bx, by = P(-0.95 * wx, -0.95 * wy)
    c.text(bx + 8, by + 4, "equally close to A and B", 10.5, "start", INK2, italic=True)
    for v, (lab, dx, dy, anc) in {"v1": ("votes A", -10, -8, "end"), "v2": ("votes B", 10, 16, "start"),
                                  "v3": ("toss-up, far from both", 12, 4, "start")}.items():
        q = voters[v]
        t0 = proj(q)
        foot = (t0 * ux, t0 * uy)
        c.line(*P(*q), *P(*foot), INK3, 1, dash="2 3")
        c.dot(*P(*q), SERIES[2], 5, title=lab)
        x, y = P(*q)
        c.text(x + dx, y + dy, lab, 11, anc, INK)
    for name, q, col, dx in (("A", A, SERIES[0], -14), ("B", B, SERIES[1], 14)):
        x, y = P(*q)
        c.dot(x, y, col, 7, title=f"candidate {name}")
        c.text(x + dx, y + 5, name, 13, "end" if dx < 0 else "start", INK, "600")
    x0 = 500
    c.text(x0, 110, "the candidates set the axis", 12, "start", INK, "600")
    c.text(x0, 134, "each voter is read only by", 11, "start", INK2)
    c.text(x0, 150, "the shadow they cast on it", 11, "start", INK2)
    c.text(x0, 184, "a voter who differs from both", 11, "start", INK2)
    c.text(x0, 200, "on another direction lands on", 11, "start", INK2)
    c.text(x0, 216, "the bisector: a toss-up", 11, "start", INK2)
    c.text(x0, 250, "new candidates, new axis,", 11, "start", INK2, italic=True)
    c.text(x0, 266, "new apparent preferences", 11, "start", INK2, italic=True)
    legend(c, x0, 306, [("candidates", SERIES[0]), ("voters", SERIES[2])], 10.5)
    c.text(16, 390, "two of the six dimensions; positions illustrative", 10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 3
def fig_3_1():
    p = reg(P1 + "ch03_history.md", "3.1",
            "The compounding contraction that the next section describes. A voter's six-dimensional position is "
            "compressed by party identification (6D to 1D), again by the voting system (1D to binary), reported by "
            "polls (binary to scalar) and interpreted by media (scalar to narrative). In the chapter's account the "
            "loss at each stage is irrecoverable, so the losses compound. A schematic of the chapter's argument, not "
            "a measurement.",
            "## The Democratic Paradox")
    c = canvas(720, 300, "Each institution contracts what the one before it passed on")
    stages = [(["the voter"], ["six dimensions"]), (["party", "identification"], ["6D to 1D"]),
              (["voting", "system"], ["1D to binary"]), (["polls"], ["binary to scalar"]),
              (["media"], ["scalar to narrative"])]
    carry = ["(d1, ..., d6)", "one party", "one choice", "one number", "one story"]
    bw, gap, x0, y0, bh = 120, 25, 10, 84, 76
    c.text(x0, 70, "stage of contraction", 11, "start", INK3, italic=True)
    c.text(x0, y0 + bh + 22, "what survives it", 11, "start", INK3, italic=True)
    c.line(x0, y0 + bh + 28, x0 + 5 * bw + 4 * gap, y0 + bh + 28, GRID, 1)
    for i, ((lines, sub), cy_) in enumerate(zip(stages, carry)):
        x = x0 + i * (bw + gap)
        mbox(c, x, y0, bw, bh, lines, sub)
        c.text(x + bw / 2, y0 + bh + 50, cy_, 12, "middle", INK, italic=True)
        if i < 4:
            c.arrow(x + bw + 3, y0 + bh / 2, x + bw + gap - 3, y0 + bh / 2, INK2, 1.5)
            c.arrow(x + bw + 3, y0 + bh + 46, x + bw + gap - 3, y0 + bh + 46, INK3, 1)
    c.text(16, 288, "schematic of the chapter's posited chain; each loss is irrecoverable in the chapter's account",
           10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 4
def fig_4_1():
    comm = [("urban core", (-1.5, -0.3, 0.8, 0.0, -1.2, 1.5)),
            ("university enclave", (-1.8, -2.0, 2.0, -1.0, 0.5, -1.5)),
            ("inner suburbs", (0.2, 0.0, 0.3, -0.2, 0.3, 0.0)),
            ("exurban belt", (1.5, 1.2, -1.0, 1.0, -2.0, 1.0)),
            ("Meadow Pines", (0.8, 1.0, -0.5, -1.5, 0.8, 0.5))]
    cen = dict(comm)
    # the pairs the caption names: together on one row, apart on another
    assert abs(cen["urban core"][0] - cen["university enclave"][0]) <= 0.3 + 1e-9
    assert abs(cen["urban core"][5] - cen["university enclave"][5]) >= 3.0
    assert abs(cen["exurban belt"][1] - cen["Meadow Pines"][1]) <= 0.2 + 1e-9
    assert abs(cen["exurban belt"][3] - cen["Meadow Pines"][3]) >= 2.5
    assert abs(cen["exurban belt"][4] - cen["Meadow Pines"][4]) >= 2.5
    p = reg(P2 + "ch04_preference_manifold.md", "4.1",
            "The centroids of District 7's five communities in standardized coordinates, one row per dimension, as "
            "the chapter prints them for its simulated sample. The numbers are illustrative. Communities that sit "
            "together on one row sit apart on another: the urban core and the university enclave are close on "
            "economics and far apart on identity, and the exurban belt and Meadow Pines are close on social values "
            "and far apart on foreign policy and institutional trust.",
            "## Manifold Operations: What Can Be Done on $\\mathcal{P}$")
    c = canvas(720, 400, "Five communities of District 7, apart on every axis (illustrative)")
    dims = ["d1 economic", "d2 social", "d3 environment", "d4 foreign policy", "d5 institutional trust", "d6 identity"]
    ax = Axes(c, 170, 70, 500, 6 * 44, (-2.5, 2.5), (0, 6), [-2, -1, 0, 1, 2], [], "standardized coordinate", "")
    c.line(ax.X(0), ax.y0 - 4, ax.X(0), ax.y0 + ax.h, GRID, 1)
    for i, dname in enumerate(dims):
        y = ax.y0 + 44 * (i + 0.5)
        c.line(ax.x0, y, ax.x0 + ax.w, y, GRID, 1)
        c.text(ax.x0 - 12, y + 4, dname, 11.5, "end", INK2)
        for j, (cname, v) in enumerate(comm):
            c.dot(ax.X(v[i]), y, SERIES[j], 5.5, title=f"{cname}, {dname}: {v[i]:+.1f}")
    legend(c, 24, 52, [(n, SERIES[j]) for j, (n, _) in enumerate(comm)], 11)
    c.text(16, 392, "simulated sample of 2,000 voters; centroids illustrative", 10.5, "start", INK3, italic=True)
    c.save(p)


def fig_4_2():
    sig = (2.0, 1.0)  # standard deviations: Sigma = diag(4, 1), illustrative

    def dm(x, y):
        return math.sqrt((x / sig[0]) ** 2 + (y / sig[1]) ** 2)

    P_, Q_ = (2.0, 0.0), (0.0, 2.0)
    assert math.hypot(*P_) == math.hypot(*Q_) == 2.0
    assert dm(*P_) == 1.0 and dm(*Q_) == 2.0
    p = reg(P2 + "ch04_preference_manifold.md", "4.2",
            "Mahalanobis distance from the center of an illustrative electorate with variance 4 on one dimension and "
            "1 on the other (covariance diag(4, 1)). The solid ellipses are the points at Mahalanobis distance 1 and "
            "2; the dashed circle is Euclidean distance 2. P and Q are equally far in Euclidean terms, but P lies "
            "along the high-variance dimension and is 1 unit away, Q along the low-variance dimension and is 2 units "
            "away: movement where voters are spread out costs less, as the chapter states.",
            "### Center of Mass")
    c = canvas(720, 400, "Equal Euclidean steps, unequal Mahalanobis distances")
    cx, cy, s = 228, 216, 44
    c.line(cx - 200, cy, cx + 200, cy, GRID, 1)
    c.line(cx, cy - 128, cx, cy + 128, GRID, 1)
    for k, col in ((1, SERIES[0]), (2, SERIES[0])):
        c.ellipse(cx, cy, s * sig[0] * k, s * sig[1] * k, 0, col, col, 2 if k == 1 else 1.5,
                  0.10 if k == 1 else 0.04, title=f"Mahalanobis distance {k}")
    circle(c, cx, cy, s * 2, INK3, 1.3, dash="5 5")
    htext(c, cx - 50, cy - 40, "1", 11.5, "end", INK2)
    htext(c, cx - 156, cy - 50, "2", 11.5, "end", INK2)
    xp, yp = cx + s * P_[0], cy - s * P_[1]
    xq, yq = cx + s * Q_[0], cy - s * Q_[1]
    c.line(cx, cy, xp, yp, INK, 1.5)
    c.line(cx, cy, xq, yq, INK, 1.5)
    c.dot(cx, cy, INK, 3.5, title="center")
    c.dot(xp, yp, SERIES[1], 5.5, title="P: Euclidean 2, Mahalanobis 1")
    c.dot(xq, yq, SERIES[1], 5.5, title="Q: Euclidean 2, Mahalanobis 2")
    htext(c, xp + 9, yp + 18, "P", 12, "start", INK, "600")
    htext(c, xq + 9, yq - 8, "Q", 12, "start", INK, "600")
    c.text(cx + 206, cy - 4, "high-variance", 10.5, "start", INK2)
    c.text(cx + 206, cy + 11, "dimension, σ = 2", 10.5, "start", INK2)
    c.text(cx, cy - 136, "low-variance dimension, σ = 1", 10.5, "middle", INK2)
    x0 = 548
    c.text(x0, 108, "P: Euclidean 2", 11.5, "start", INK)
    c.text(x0, 124, "Mahalanobis 1", 11.5, "start", INK)
    c.text(x0, 156, "Q: Euclidean 2", 11.5, "start", INK)
    c.text(x0, 172, "Mahalanobis 2", 11.5, "start", INK)
    c.text(x0, 214, "d_M = √((v1 − v2)ᵀ Σ⁻¹ (v1 − v2))", 11, "start", INK2, italic=True)
    c.text(x0, 234, "Σ = diag(4, 1), illustrative", 11, "start", INK2, italic=True)
    legend(c, 16, 384, [("Mahalanobis 1 and 2", SERIES[0])], 10.5)
    c.text(704, 384, "dashed: Euclidean distance 2", 10.5, "end", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 5
def fig_5_1():
    n, d, m = 200_000, 6, 5
    carried = [n * d, n, m, 1]
    assert carried[0] == 1_200_000
    p = reg(P2 + "ch05_voting_contraction.md", "5.1",
            "The information flow of the chapter's hypothetical District 7 election, 200,000 voters and five "
            "candidates under plurality. Each stage keeps fewer quantities than the one before: 1,200,000 coordinates, "
            "200,000 ballot labels, five counts, one name. The bars count the quantities each stage carries, on a "
            "logarithmic scale.",
            "## The Voting Function")
    c = canvas(720, 420, "One hypothetical election as a chain of contractions")
    stages = [(["200,000 voters"], ["points in ℝ⁶"]), (["200,000 ballots"], ["one of five names"]),
              (["five counts"], ["a point in ℕ⁵"]), (["one winner"], ["a single name"])]
    steps = ["nearest candidate", "count", "largest count"]
    bw, gap, x0, y0, bh = 136, 48, 16, 64, 60
    centers = []
    for i, (lines, sub) in enumerate(stages):
        x = x0 + i * (bw + gap)
        mbox(c, x, y0, bw, bh, lines, sub)
        centers.append(x + bw / 2)
        if i < 3:
            c.arrow(x + bw + 3, y0 + bh / 2, x + bw + gap - 3, y0 + bh / 2, INK2, 1.5)
            c.text(x + bw + gap / 2, y0 + bh + 16, steps[i], 10.5, "middle", INK2, italic=True)
    ax = Axes(c, 24, 170, 672, 180, (0, 4), (0, 7), [], [], "", "")
    sup = "⁰¹²³⁴⁵⁶⁷⁸⁹"
    for k in range(0, 7):
        y = ax.Y(k)
        c.line(ax.x0 + 40, y, ax.x0 + ax.w, y, GRID, 1)
        c.text(ax.x0 + 34, y + 4, "1" if k == 0 else ("10" if k == 1 else "10" + sup[k]), 10.5, "end", INK2)
    for cxp, v in zip(centers, carried):
        h = math.log10(v)
        y = ax.Y(h)
        c.rect(cxp - 12, y, 24, ax.Y(0) - y, SERIES[0], title=f"{v:,} quantities")
        c.text(cxp, y - 7, f"{v:,}", 11, "middle", INK)
    c.text(24, 376, "quantities carried at each stage (logarithmic scale)", 11, "start", INK2)
    c.text(16, 408, "hypothetical District 7 election under plurality", 10.5, "start", INK3, italic=True)
    c.save(p)


def fig_5_2():
    cands = ["A", "B", "C", "D", "E"]
    kinds = ["progressive", "conservative", "moderate", "green populist", "libertarian"]
    first = [28, 31, 18, 14, 9]
    approve = [47, 44, 61, 38, 22]
    condorcet_c = {"A": 51, "B": 54, "D": 58, "E": 65}
    winners = {"plurality": "B", "top-two primary": "A", "ranked choice": "A", "approval": "C", "Condorcet": "C"}
    assert sum(first) == 100
    assert cands[first.index(max(first))] == winners["plurality"]
    assert cands[approve.index(max(approve))] == winners["approval"]
    assert cands[first.index(min(first))] == "E"  # E is the first eliminated under ranked choice
    assert all(v > 50 for v in condorcet_c.values())
    assert len(set(winners.values())) == 3
    p = reg(P2 + "ch05_voting_contraction.md", "5.2",
            "The chapter's hypothetical election: five voting systems applied to one illustrative electorate of "
            "District 7. Bars give each candidate's share of first choices and of approvals. Plurality elects B with "
            "31% of first choices; the top-two runoff (52%) and ranked choice (54% after transfers) elect A; approval "
            "(61%) and the Condorcet comparison, in which C beats each rival head to head, elect C. Three winners "
            "from the same voters.",
            "### Information Preservation Ranking")
    c = canvas(720, 400, "Same voters, five counting rules, three winners (hypothetical)")
    ax = Axes(c, 64, 64, 376, 250, (0, 5), (0, 70), [], [0, 20, 40, 60], "", "share of voters, %")
    slot = ax.w / 5
    for i, (cand, kind) in enumerate(zip(cands, kinds)):
        xm = ax.X(i + 0.5)
        for j, v in enumerate((first[i], approve[i])):
            x = xm - 25 + j * 26
            c.rect(x, ax.Y(v), 24, ax.Y(0) - ax.Y(v), SERIES[j],
                   title=f"{cand}: {'first choice' if j == 0 else 'approval'} {v}%")
            c.text(x + 12, ax.Y(v) - 6, f"{v}", 10.5, "middle", INK)
        c.text(xm, ax.Y(0) + 17, cand, 12.5, "middle", INK, "600")
        c.text(xm, ax.Y(0) + 32, kind, 10, "middle", INK2)
    legend(c, 64, 48, [("first choice", SERIES[0]), ("approval", SERIES[1])], 11)
    x0 = 476
    c.text(x0, 76, "winner under each rule", 12, "start", INK, "600")
    rows = [("plurality", "B, 31% of first choices"), ("top-two primary", "A, 52% in the runoff"),
            ("ranked choice", "A, 54% after transfers"), ("approval", "C, approved by 61%"),
            ("Condorcet", "C, beats each rival")]
    for i, (rule, res) in enumerate(rows):
        y = 104 + 44 * i
        c.text(x0, y, rule, 11, "start", INK2)
        c.text(x0, y + 17, res, 12, "start", INK)
    c.text(x0, 336, "three winners: A, B and C", 11.5, "start", INK2, italic=True)
    c.text(16, 390, "hypothetical election, illustrative shares as the chapter gives them", 10.5, "start", INK3,
           italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 6
def fig_6_1():
    var = (4.0, 1.0)   # Sigma = diag(4, 1), illustrative
    off = (0.0, 2.0)   # x_C - mu, illustrative

    def parts(deg):
        t = math.radians(deg)
        e = (math.cos(t), math.sin(t))
        v = var[0] * e[0] ** 2 + var[1] * e[1] ** 2
        o = (off[0] * e[0] + off[1] * e[1]) ** 2
        return v, o, v + o

    assert abs(parts(0)[2] - 4.0) < 1e-12 and abs(parts(90)[2] - 5.0) < 1e-12
    # the minimum over unit vectors is the smallest eigenvalue of Sigma + (x_C - mu)(x_C - mu)^T = diag(4, 5)
    grid = [parts(k / 10)[2] for k in range(0, 1801)]
    assert abs(min(grid) - 4.0) < 1e-12 and grid.index(min(grid)) == 0
    p = reg(P2 + "ch06_campaigns_heuristic.md", "6.1",
            "The Campaign Gradient Theorem in its one form, for an illustrative electorate in two dimensions with "
            "variance 4 along axis 1 and 1 along axis 2, and a candidate offset (0, 2) from the electorate's mean. "
            "Right: for a projection axis at angle θ from axis 1, the electorate's variance along the axis, the "
            "candidate's squared offset along it, and their sum, the mean squared projected distance the theorem "
            "minimizes. The sum is least on axis 1 (4, against 5 on axis 2): the low-variance axis loses because "
            "the candidate is far from the mean along it.",
            "### What the Theorem Predicts")
    c = canvas(720, 400, "The best campaign axis minimizes variance plus squared offset")
    cx, cy, s = 140, 232, 44
    c.line(cx - 116, cy, cx + 116, cy, INK3, 1.2)
    c.line(cx, cy - 140, cx, cy + 110, INK3, 1.2)
    c.ellipse(cx, cy, s * 2, s * 1, 0, SERIES[0], SERIES[0], 2, 0.10, title="electorate, one standard deviation")
    c.dot(cx, cy, INK, 3.5, title="electorate mean")
    xc, yc = cx + s * off[0], cy - s * off[1]
    c.dot(xc, yc, CRITICAL, 6, title="candidate")
    c.text(xc + 12, yc + 4, "candidate", 11.5, "start", INK)
    htext(c, cx + 8, cy + 16, "mean", 10.5, "start", INK2)
    c.text(cx + 122, cy + 4, "axis 1", 11, "start", INK2)
    c.text(cx + 122, cy + 20, "variance 4", 10.5, "start", INK3)
    c.text(cx - 8, cy - 128, "axis 2", 11, "end", INK2)
    c.text(cx - 8, cy - 112, "variance 1", 10.5, "end", INK3)
    c.text(cx + 8, yc + 34, "offset 2", 10.5, "start", INK2, italic=True)
    c.text(24, 372, "offset 0 along axis 1, 2 along axis 2", 10.5, "start", INK3, italic=True)
    ax = Axes(c, 390, 58, 290, 270, (0, 180), (0, 6), [0, 45, 90, 135, 180], [0, 1, 2, 3, 4, 5, 6],
              "axis angle θ from axis 1, degrees", "mean squared distance")
    degs = list(range(0, 181, 2))
    names = ["variance along the axis", "squared offset", "sum"]
    for j in range(3):
        c.polyline([(ax.X(dg), ax.Y(parts(dg)[j])) for dg in degs], SERIES[j], 2 if j < 2 else 2.5, title=names[j])
    c.dot(ax.X(0), ax.Y(4), CRITICAL, 5, title="minimum: axis 1, 4")
    c.dot(ax.X(180), ax.Y(4), CRITICAL, 5, title="minimum: axis 1, 4")
    c.dot(ax.X(90), ax.Y(5), SERIES[2], 4.5, title="axis 2: 1 + 4 = 5")
    c.text(ax.X(90), ax.Y(5) - 12, "axis 2: 1 + 4 = 5", 10.5, "middle", INK)
    c.text(ax.X(4), ax.Y(5.78), "least: axis 1, 4 + 0 = 4", 10.5, "start", INK)
    c.text(ax.X(90), ax.Y(parts(90)[0]) + 16, "variance", 10.5, "middle", INK2)
    c.text(ax.X(90), ax.Y(2.9), "squared offset", 10.5, "middle", INK2)
    c.text(ax.X(150), ax.Y(parts(150)[2]) - 10, "sum", 10.5, "start", INK2)
    c.save(p)


# ------------------------------------------------------------------ chapter 7
def fig_7_1():
    blocs = [("university enclave", 35, "ABC"), ("inner suburbs", 33, "BCA"), ("exurban belt", 32, "CAB")]

    def share(x, y):
        return sum(w for _, w, r in blocs if r.index(x) < r.index(y))

    assert (share("A", "B"), share("B", "C"), share("C", "A")) == (67, 68, 65)
    assert all(share(x, y) + share(y, x) == 100 for x, y in ("AB", "BC", "CA"))
    p = reg(P2 + "ch07_arrows_theorem.md", "7.1",
            "The three blocs of the running example and their rankings. Each arrow points from the winner to the "
            "loser of a pairwise majority vote, with the shares computed from the bloc sizes: A beats B 67 to 33, B "
            "beats C 68 to 32, and C beats A 65 to 35. Every candidate loses to someone, so there is no Condorcet "
            "winner. District 7's blocs and shares are illustrative.",
            "## Arrow's Theorem: The Standard Statement")
    c = canvas(720, 400, "Three blocs, three majorities, one cycle (illustrative)")
    pos = {"A": (215, 100), "B": (345, 310), "C": (85, 310)}
    r = 28
    for x, y in [("A", "B"), ("B", "C"), ("C", "A")]:
        (x1, y1), (x2, y2) = pos[x], pos[y]
        dx, dy = x2 - x1, y2 - y1
        L = math.hypot(dx, dy)
        ux, uy = dx / L, dy / L
        c.arrow(x1 + ux * (r + 4), y1 + uy * (r + 4), x2 - ux * (r + 6), y2 - uy * (r + 6), INK2, 2)
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        # label on the outer side of the triangle
        gx, gy = 215, 240
        ox, oy = mx - gx, my - gy
        on = math.hypot(ox, oy)
        lx, ly = mx + 30 * ox / on, my + 30 * oy / on
        c.text(lx, ly + 4, f"{share(x, y)}–{share(y, x)}", 12.5, "middle", INK, "600")
    for k, (x, y) in pos.items():
        circle(c, x, y, r, BORDER, 1, fill=BOX)
        c.text(x, y + 6, k, 17, "middle", INK, "600")
    c.text(215, 252, "each arrow:", 10.5, "middle", INK3, italic=True)
    c.text(215, 267, "winner to loser", 10.5, "middle", INK3, italic=True)
    x0 = 452
    c.text(x0, 84, "the blocs and their rankings", 12, "start", INK, "600")
    for i, (nm, w, rk) in enumerate(blocs):
        y = 110 + 38 * i
        c.text(x0, y, f"{nm}, {w}%", 11.5, "start", INK2)
        c.text(x0, y + 16, " > ".join(rk), 12, "start", INK)
    c.text(x0, 238, "pairwise majorities", 12, "start", INK, "600")
    for i, (x, y, who) in enumerate([("A", "B", "35 + 32"), ("B", "C", "35 + 33"), ("C", "A", "33 + 32")]):
        c.text(x0, 262 + 20 * i, f"{x} over {y}: {who} = {share(x, y)}", 11.5, "start", INK2)
    c.text(x0, 334, "no candidate beats both others", 11, "start", INK2, italic=True)
    c.text(16, 390, "District 7's three blocs, illustrative shares", 10.5, "start", INK3, italic=True)
    c.save(p)


def _lens(ci, ri, cj, rj, n=60):
    """Polygon of the intersection of two disks (centres ci, cj; radii ri, rj)."""
    dx, dy = cj[0] - ci[0], cj[1] - ci[1]
    d = math.hypot(dx, dy)
    a = (ri ** 2 - rj ** 2 + d ** 2) / (2 * d)
    h = math.sqrt(ri ** 2 - a ** 2)
    px, py = ci[0] + a * dx / d, ci[1] + a * dy / d
    i1 = (px - h * dy / d, py + h * dx / d)
    i2 = (px + h * dy / d, py - h * dx / d)

    def arc(c0, r0, other, ro, s, e):
        t1 = math.atan2(s[1] - c0[1], s[0] - c0[0])
        t2 = math.atan2(e[1] - c0[1], e[0] - c0[0])
        dt = (t2 - t1) % (2 * math.pi)
        tm = t1 + dt / 2
        mx, my = c0[0] + r0 * math.cos(tm), c0[1] + r0 * math.sin(tm)
        if math.hypot(mx - other[0], my - other[1]) > ro:
            dt = dt - 2 * math.pi
        return [(c0[0] + r0 * math.cos(t1 + dt * k / n), c0[1] + r0 * math.sin(t1 + dt * k / n)) for k in range(n + 1)]

    return arc(ci, ri, cj, rj, i1, i2) + arc(cj, rj, ci, ri, i2, i1)


def fig_7_2():
    V = [(-1.6, -0.9), (1.6, -0.9), (0.2, 1.5)]
    pp = (sum(v[0] for v in V) / 3, sum(v[1] for v in V) / 3)
    R = [math.hypot(v[0] - pp[0], v[1] - pp[1]) for v in V]
    lenses = {(i, j): _lens(V[i], R[i], V[j], R[j]) for i, j in ((0, 1), (0, 2), (1, 2))}
    # a point in the lens of voters 1 and 2 is nearer both their ideal points than p is
    poly = lenses[(0, 1)]
    q = (sum(x for x, _ in poly) / len(poly), sum(y for _, y in poly) / len(poly))
    for k in (0, 1):
        assert math.hypot(q[0] - V[k][0], q[1] - V[k][1]) < R[k]
    p = reg(P2 + "ch07_arrows_theorem.md", "7.2",
            "McKelvey's result as the chapter reads it, for three voters with illustrative ideal points in two "
            "dimensions, each preferring positions nearer their own ideal point. Each circle passes through the "
            "position p, here the centroid of the three ideal points, and encloses the positions that voter prefers "
            "to p. The shaded petals hold the positions that two of the three voters prefer to p, such as q. They are "
            "not empty, so p loses a majority vote; for these three voters every position does, which is the empty "
            "majority-rule core of McKelvey's result.",
            "## The Gibbard-Satterthwaite Connection")
    c = canvas(720, 400, "Even a central position loses to a majority-preferred alternative")
    cx, cy, s = 250, 222, 53

    def P(a, b):
        return cx + s * a, cy - s * b

    for (i, j), poly in lenses.items():
        polygon(c, [P(*q_) for q_ in poly], CRITICAL, 0.32)
    for k, (v, r) in enumerate(zip(V, R)):
        x, y = P(*v)
        circle(c, x, y, s * r, SERIES[k], 1.8)
        c.dot(x, y, SERIES[k], 5.5, title=f"voter {k + 1} ideal point")
    labs = [("voter 1", -10, 18, "end"), ("voter 2", 10, 18, "start"), ("voter 3", 10, -8, "start")]
    for (v, (t, dx, dy, anc)) in zip(V, labs):
        x, y = P(*v)
        c.text(x + dx, y + dy, t, 11, anc, INK)
    xp, yp = P(*pp)
    c.dot(xp, yp, INK, 4.5, title="p")
    htext(c, xp - 12, yp + 17, "p", 13, "end", INK, "600")
    xq, yq = P(*q)
    c.dot(xq, yq, INK, 3.5, title="q")
    htext(c, xq + 20, yq + 5, "q", 13, "start", INK, "600")
    x0 = 480
    c.text(x0, 92, "each voter prefers what is", 11, "start", INK2)
    c.text(x0, 108, "nearer their ideal point", 11, "start", INK2)
    c.text(x0, 142, "circle: as good as p for", 11, "start", INK2)
    c.text(x0, 158, "that voter", 11, "start", INK2)
    polygon(c, [(x0, 182), (x0 + 14, 182), (x0 + 14, 194), (x0, 194)], CRITICAL, 0.45)
    c.text(x0 + 22, 192, "preferred to p by", 11, "start", INK2)
    c.text(x0 + 22, 208, "two of three voters", 11, "start", INK2)
    c.text(x0, 248, "q beats p 2 to 1; some other", 11, "start", INK2, italic=True)
    c.text(x0, 264, "position beats q, and so on", 11, "start", INK2, italic=True)
    c.text(16, 390, "illustrative ideal points; Euclidean preferences", 10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 8
def fig_8_1():
    cases = [("high sorting,", "low polarization", 0.35, 1.0),
             ("low sorting,", "high polarization", 1.3, 2.4),
             ("high sorting,", "high polarization", 0.35, 2.4)]

    def mix(x, s, g):
        return 0.5 * gauss(x, -g / 2, s) + 0.5 * gauss(x, g / 2, s)

    def bimodal(s, g):
        return mix(0, s, g) < mix(g / 2, s, g)

    flags = [bimodal(s, g) for _, _, s, g in cases]
    assert flags == [True, False, True]  # equal mixture of two normals is bimodal iff gap > 2 sd
    p = reg(P3 + "ch08_polarization.md", "8.1",
            "The sorting-polarization distinction as the chapter defines it, drawn with two parties in a plane of two "
            "dimensions. Sorting is drawn as within-party tightness (small circles), the chapter's decrease in "
            "within-party variance; polarization is the gap between the party centroids. Below each plane is the distribution projected on the line through the centroids, the "
            "partisan axis. Tight parties look bimodal even when close (left); loose parties look unimodal even when "
            "far apart (middle). Drawn for within-party standard deviations 0.35 and 1.3 and centroid gaps 1.0 and "
            "2.4, illustrative values.",
            "## Affective Polarization as Metric Distortion")
    c = canvas(720, 420, "Sorting and polarization are different quantities")
    for k, (l1, l2, sd, g) in enumerate(cases):
        x0 = 22 + 236 * k
        cxp, cyp, s = x0 + 105, 168, 34
        c.text(cxp, 62, l1, 12, "middle", INK, "600")
        c.text(cxp, 78, l2, 12, "middle", INK, "600")
        c.add(f'<rect x="{cxp - 104:.2f}" y="{cyp - 76:.2f}" width="208" height="152" fill="none" '
              f'stroke="{GRID}" stroke-width="1"/>')
        u = (1 / math.sqrt(2), 1 / math.sqrt(2))
        for j, sign in enumerate((-1, 1)):
            mx, my = sign * g / 2 * u[0], sign * g / 2 * u[1]
            circle(c, cxp + s * mx, cyp - s * my, s * sd, SERIES[j], 1.8, fill=SERIES[j], opacity=0.12)
            c.dot(cxp + s * mx, cyp - s * my, SERIES[j], 3.5, title=f"party {j + 1} centroid")
        a1 = (cxp - s * g / 2 * u[0], cyp + s * g / 2 * u[1])
        a2 = (cxp + s * g / 2 * u[0], cyp - s * g / 2 * u[1])
        c.line(a1[0], a1[1], a2[0], a2[1], INK, 1.2, dash="3 3")
        # projected density
        base, top = 352, 262
        xs = [-3.2 + 6.4 * i / 160 for i in range(161)]
        ys = [mix(x, sd, g) for x in xs]
        ymax = 1.2
        c.line(cxp - 100, base, cxp + 100, base, GRID, 1)
        c.polyline([(cxp + 31 * x, base - (base - top) * y / ymax) for x, y in zip(xs, ys)], SERIES[2], 2,
                   title="projection on the partisan axis")
        c.text(cxp, base + 18, "bimodal" if flags[k] else "unimodal", 11.5, "middle", INK)
        c.text(cxp, cyp + 92, f"gap {g:g}, spread {sd:g}", 10.5, "middle", INK2, italic=True)
    c.text(16, 396, "top: two parties in two dimensions (one-standard-deviation circles); bottom: the projection on "
           "the line through the centroids", 10.5, "start", INK3, italic=True)
    c.text(16, 412, "illustrative values", 10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 9
def fig_9_1():
    ang = [math.radians(15 + 30 * k) for k in range(12)]
    rad = 0.45
    Pc, Qc = (-1.5, 0.0), (1.5, 0.0)
    clusterP = [(Pc[0] + rad * math.cos(a), Pc[1] + rad * math.sin(a)) for a in ang]
    clusterQ = [(Qc[0] + rad * math.cos(a), Qc[1] + rad * math.sin(a)) for a in ang]

    def gi(districts):
        tot, n = 0.0, 0
        for pts in districts:
            mx = sum(x for x, _ in pts) / len(pts)
            my = sum(y for _, y in pts) / len(pts)
            tot += sum(math.hypot(x - mx, y - my) for x, y in pts)
            n += len(pts)
        return tot / n

    whole = [clusterP, clusterQ]
    cracked = [[q for q in clusterP + clusterQ if q[1] > 0], [q for q in clusterP + clusterQ if q[1] < 0]]
    assert all(len(dd) == 12 for dd in cracked)
    gi_w, gi_c = gi(whole), gi(cracked)
    assert abs(gi_w - rad) < 1e-12 and gi_c > 3 * gi_w
    p = reg(P3 + "ch09_gerrymandering.md", "9.1",
            "Cracking in preference space, with the gerrymandering index of Definition 4 (the mean distance from each "
            f"voter to the center of the voter's district). Twenty-four illustrative voters form two communities. "
            f"Kept whole (left), each district is one community and the index is {gi_w:.2f}. Cracked (right), each "
            f"district takes half of each community, its image is bimodal, its center falls between the two clusters "
            f"and far from both, and the index rises to {gi_c:.2f}. Euclidean distance, two dimensions.",
            "### The Efficiency Gap and Its Geometric Limitation")
    c = canvas(720, 400, "Cracking a community raises the gerrymandering index")
    for k, (title, dists) in enumerate((("communities kept whole", whole), ("communities cracked", cracked))):
        x0 = 30 + 350 * k
        cxp, cyp, s = x0 + 160, 200, 72
        c.text(cxp, 66, title, 12.5, "middle", INK, "600")
        c.add(f'<rect x="{cxp - 158:.2f}" y="{cyp - 110:.2f}" width="316" height="220" fill="none" '
              f'stroke="{GRID}" stroke-width="1"/>')
        for j, pts in enumerate(dists):
            mx = sum(x for x, _ in pts) / len(pts)
            my = sum(y for _, y in pts) / len(pts)
            for x, y in pts:
                c.line(cxp + s * x, cyp - s * y, cxp + s * mx, cyp - s * my, SERIES[j], 1, opacity=0.35)
            for x, y in pts:
                c.dot(cxp + s * x, cyp - s * y, SERIES[j], 4, title=f"district {j + 1} voter")
            xm, ym = cxp + s * mx, cyp - s * my
            c.add(f'<rect x="{xm - 5:.2f}" y="{ym - 5:.2f}" width="10" height="10" fill="{INK}" '
                  f'transform="rotate(45 {xm:.2f} {ym:.2f})"><title>district {j + 1} center</title></rect>')
        c.text(cxp, cyp + 134, f"index {gi(dists):.2f}", 13, "middle", INK, "600")
    legend(c, 30, 370, [("district 1", SERIES[0]), ("district 2", SERIES[1])], 10.5)
    c.text(704, 370, "diamond: district center; lines: distance to it", 10.5, "end", INK3, italic=True)
    c.text(16, 392, "illustrative voters in two dimensions of the preference manifold", 10.5, "start", INK3,
           italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 10
def fig_10_1():
    beta, half = 1.0, 1.0

    def cost(x):
        dd = max(abs(x) - half, 0.0)
        return beta * dd * dd

    assert cost(0) == 0 and cost(1) == 0 and cost(2) == 1 and cost(-3) == 4
    p = reg(P3 + "ch10_overton_window.md", "10.1",
            "The Overton penalty of the chapter, cost = β d(p, W)², on one dimension through a window W, drawn for "
            "β = 1 and a window of half-width 1 (illustrative values). Inside the window the cost is zero. Outside "
            "it grows with the square of the distance to the window: two units past the boundary cost four times as "
            "much as one.",
            "## Window Geometry")
    c = canvas(720, 400, "The Overton penalty: zero inside the window, quadratic outside")
    ax = Axes(c, 80, 58, 580, 270, (-3.2, 3.2), (0, 5), [-3, -2, -1, 0, 1, 2, 3], [0, 1, 2, 3, 4, 5],
              "position on one dimension", "Overton cost")
    c.add(f'<rect x="{ax.X(-half):.2f}" y="{ax.y0:.2f}" width="{ax.X(half) - ax.X(-half):.2f}" height="{ax.h:.2f}" '
          f'fill="{SERIES[0]}" fill-opacity="0.10"/>')
    c.text(ax.X(0), ax.y0 + 20, "window W", 12, "middle", INK, "600")
    c.text(ax.X(0), ax.y0 + 36, "cost 0", 11, "middle", INK2)
    xs = [-3.2 + 6.4 * i / 320 for i in range(321)]
    c.polyline([(ax.X(x), ax.Y(cost(x))) for x in xs], SERIES[1], 2.5, title="cost = β d(p, W)²")
    for x in (2, 3):
        c.dot(ax.X(x), ax.Y(cost(x)), SERIES[1], 4.5, title=f"distance {x - 1}: cost {cost(x):g}")
        if x == 3:
            c.text(ax.X(x) - 10, ax.Y(cost(x)) + 4, f"distance {x - 1}: cost {cost(x):g}", 10.5, "end", INK)
        else:
            c.text(ax.X(x) + 10, ax.Y(cost(x)) + 18, f"distance {x - 1}: cost {cost(x):g}", 10.5, "start", INK)
    c.text(ax.X(-2.4), ax.Y(3.3), "β d(p, W)²", 12, "middle", INK, italic=True)
    for x in (-half, half):
        c.line(ax.X(x), ax.y0, ax.X(x), ax.y0 + ax.h, INK3, 1.2, dash="4 4")
    c.text(ax.X(half) + 4, ax.y0 + 14, "boundary", 10.5, "start", INK2, italic=True)
    c.text(16, 390, "β = 1, half-width 1, illustrative", 10.5, "start", INK3, italic=True)
    c.save(p)


def fig_10_2():
    # window: the square [0,4]^2 without the notch [1,4] x [1.5,2.5] (opening to the right)
    a, b = (3.2, 3.2), (3.2, 0.8)
    k1, k2 = (1.0, 2.5), (1.0, 1.5)
    geo = math.hypot(a[0] - b[0], a[1] - b[1])
    adm = math.hypot(a[0] - k1[0], a[1] - k1[1]) + math.hypot(k1[0] - k2[0], k1[1] - k2[1]) + \
        math.hypot(k2[0] - b[0], k2[1] - b[1])
    assert abs(geo - 2.4) < 1e-12 and abs(adm - (2 * math.hypot(2.2, 0.7) + 1)) < 1e-12
    cost = adm - geo
    p = reg(P3 + "ch10_overton_window.md", "10.2",
            "Definition 5 and the Overton cost in a two-dimensional sketch. Left: the straight geodesic between two "
            "positions inside the window W leaves it, so an Overton-admissible path must detour around the excluded "
            f"region; with the illustrative lengths shown the detour is {adm:.2f} against {geo:.2f}, an Overton cost of "
            f"{cost:.2f}. Right: once the window expands to include that region, the geodesic is admissible and the "
            "cost is zero, the geodesic shortcut the chapter describes. Euclidean lengths.",
            "## Window Dynamics")
    c = canvas(720, 400, "A window that excludes the straight path forces a costly detour")
    for k in range(2):
        x0, y0, s = 50 + 350 * k, 340, 62
        c.text(x0 + 124, 62, "before the window expands" if k == 0 else "after it expands", 12.5, "middle", INK, "600")

        def P(u, v):
            return x0 + s * u, y0 - s * v

        if k == 0:
            shape = [(0, 0), (4, 0), (4, 1.5), (1, 1.5), (1, 2.5), (4, 2.5), (4, 4), (0, 4)]
            polygon(c, [P(*q) for q in shape], SERIES[0], 0.16, SERIES[0], 1.5)
            c.text(*P(2.5, 2.0), "outside W", 11, "middle", INK3, italic=True)
        else:
            shape = [(0, 0), (4, 0), (4, 4), (0, 4)]
            polygon(c, [P(*q) for q in shape], SERIES[0], 0.16, SERIES[0], 1.5)
        c.text(*[v + d for v, d in zip(P(0.12, 3.7), (0, 4))], "W", 13, "start", INK, "600")
        if k == 0:
            pts = [P(*a), P(*k1), P(*k2), P(*b)]
            c.polyline(pts, SERIES[1], 2.5, title=f"admissible path, length {adm:.2f}")
            c.line(*P(*a), *P(*b), CRITICAL, 1.8, dash="5 4")
            c.text(*[v + d for v, d in zip(P(3.3, 2.0), (8, 4))], f"{geo:.1f}", 11, "start", INK)
            c.text(*[v + d for v, d in zip(P(1.0, 2.0), (-8, 4))], f"{adm:.2f}", 11, "end", INK)
        else:
            c.line(*P(*a), *P(*b), SERIES[1], 2.5)
            c.text(*[v + d for v, d in zip(P(3.2, 2.0), (10, 4))], f"{geo:.1f}", 11, "start", INK)
        for q, lab in ((a, "start"), (b, "end")):
            c.dot(*P(*q), INK, 4.5, title=lab)
        c.text(*[v + d for v, d in zip(P(*a), (10, 4))], "start", 10.5, "start", INK2)
        c.text(*[v + d for v, d in zip(P(*b), (10, 4))], "end", 10.5, "start", INK2)
    c.text(174, 372, f"Overton cost {adm:.2f} − {geo:.1f} = {cost:.2f}", 11.5, "middle", INK)
    c.text(524, 372, "Overton cost 0", 11.5, "middle", INK)
    legend(c, 16, 392, [("shortest admissible path", SERIES[1]), ("geodesic, leaves W", CRITICAL)], 10.5)
    c.text(704, 392, "illustrative lengths", 10.5, "end", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 11
def fig_11_1():
    true_d, perc_d = 2.3, 5.5
    assert round(perc_d / true_d, 1) == 2.4
    b = 1.2  # illustrative in-group radius for the echo-chamber step
    p = reg(P3 + "ch11_media.md", "11.1",
            "Perceived against actual manifold distance. A calibrated heuristic lies on the diagonal. Sarah and Mike "
            "of the running example are 2.3 units apart and perceive 5.5, a distortion factor of 2.4 (distance "
            "inflation). In an echo chamber the metric collapses to a step: in-group positions are perceived at "
            "zero and out-group positions as far, whatever their actual distance. Sarah and Mike's numbers are "
            "illustrative, and the step is drawn at an illustrative in-group radius.",
            "## The Information Diet as Manifold Filter")
    c = canvas(720, 400, "Media distort the metric: inflation and echo-chamber collapse")
    ax = Axes(c, 80, 58, 440, 280, (0, 7), (0, 7), [0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7],
              "actual manifold distance", "perceived distance")
    c.line(ax.X(0), ax.Y(0), ax.X(7), ax.Y(7), SERIES[0], 2)
    c.text(ax.X(6.2), ax.Y(6.2) + 18, "calibrated", 11, "start", INK2)
    # echo chamber step
    c.line(ax.X(0), ax.Y(0) - 1, ax.X(b), ax.Y(0) - 1, SERIES[2], 3)
    c.line(ax.X(b), ax.Y(6.85), ax.X(7), ax.Y(6.85), SERIES[2], 3)
    c.line(ax.X(b), ax.Y(0), ax.X(b), ax.Y(6.85), SERIES[2], 1.2, dash="3 4")
    c.text(ax.X(b) + 8, ax.Y(6.85) + 16, "echo chamber: out-group far", 10.5, "start", INK2)
    c.text(ax.X(b) + 6, ax.Y(0) - 6, "in-group: 0", 10.5, "start", INK2)
    # Sarah and Mike
    x = ax.X(true_d)
    c.arrow(x, ax.Y(true_d) - 6, x, ax.Y(perc_d) + 8, INK2, 1.5)
    c.dot(x, ax.Y(true_d), SERIES[0], 5, title="actual 2.3")
    c.dot(x, ax.Y(perc_d), SERIES[1], 6, title="perceived 5.5")
    c.text(x + 10, ax.Y(perc_d) + 4, "Sarah and Mike: perceived 5.5", 11, "start", INK)
    c.text(x + 10, ax.Y(true_d) + 16, "actual 2.3", 11, "start", INK)
    c.text(x + 10, ax.Y((true_d + perc_d) / 2) + 4, "× 2.4", 11, "start", INK2, italic=True)
    x0 = 552
    c.text(x0, 96, "corruption modes", 12, "start", INK, "600")
    c.text(x0, 120, "distance inflation:", 11, "start", INK2)
    c.text(x0, 136, "points above the line", 11, "start", INK2)
    c.text(x0, 168, "metric collapse:", 11, "start", INK2)
    c.text(x0, 184, "graded distances become", 11, "start", INK2)
    c.text(x0, 200, "a step, near or far", 11, "start", INK2)
    legend(c, x0, 236, [("calibrated", SERIES[0])], 10.5)
    legend(c, x0, 256, [("perceived", SERIES[1])], 10.5)
    legend(c, x0, 276, [("echo chamber", SERIES[2])], 10.5)
    c.text(16, 390, "District 7 example, illustrative; step drawn at an illustrative in-group radius", 10.5, "start",
           INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 12
def fig_12_1():
    d = 6

    def F(k, x):
        return (d - k) / d * x

    thresholds = {k: d / (d - k) for k in (1, 2, 3, 4)}
    assert abs((d - 2) / d - 0.6667) < 1e-4 and abs(thresholds[2] - 1.5) < 1e-12
    p = reg(P3 + "ch12_coalitions.md", "12.1",
            "The fragility index of Theorem 6, F = ((d − dim A)/d) × max σ²/ε², against the worst within-coalition "
            "variance in units of the tolerance ε², for d = 6 and agreement submanifolds of dimension 1 to 4. A "
            "coalition is geometrically fragile above F = 1. With dim A = 2, the chapter's reading of both American "
            "party coalitions, the coefficient is 4/6 and the threshold is reached at 1.5 ε², as the chapter states. "
            "Deeper agreement moves the threshold out.",
            "## Cross-Partisan Coalitions on the Manifold")
    c = canvas(720, 400, "Deeper agreement lets a coalition carry more disagreement")
    ax = Axes(c, 80, 58, 500, 270, (0, 3.5), (0, 2.0), [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5], [0, 0.5, 1, 1.5, 2],
              "worst within-coalition variance, in units of ε²", "fragility index F")
    for j, k in enumerate((1, 2, 3, 4)):
        xe = min(3.5, 2.0 * d / (d - k))
        pts = [(ax.X(0), ax.Y(0)), (ax.X(xe), ax.Y(F(k, xe)))]
        c.polyline(pts, SERIES[j], 2.5 if k == 2 else 2, title=f"dim A = {k}")
        xt = thresholds[k]
        c.dot(ax.X(xt), ax.Y(1), SERIES[j], 4.5, title=f"dim A = {k}: fragile above {xt:g} ε²")
        lx, ly = ax.X(xe), ax.Y(F(k, xe))
        c.text(lx + 8 if xe >= 3.5 else lx, ly + 4 if xe >= 3.5 else ly - 8, f"dim A = {k}", 11,
               "start" if xe >= 3.5 else "middle", INK2)
    c.line(ax.X(0), ax.Y(1), ax.X(3.5), ax.Y(1), INK3, 1.5, dash="4 4")
    c.text(ax.X(0) + 6, ax.Y(1) - 7, "fracture threshold F = 1", 10.5, "start", INK2, italic=True)
    c.line(ax.X(1.5), ax.Y(1) + 6, ax.X(1.5), ax.Y(0), SERIES[1], 1.2, dash="2 3")
    c.text(ax.X(1.5) + 6, ax.Y(0) - 8, "dim A = 2: fragile above 1.5 ε²", 11, "start", INK)
    c.text(16, 390, "d = 6 dimensions", 10.5, "start", INK3, italic=True)
    c.save(p)


def fig_12_2():
    blocs = [("progressive urban voters", 30, 0.8), ("moderate suburban parents", 25, 1.2),
             ("libertarian exurban voters", 10, 2.0), ("retired pragmatists", 8, 1.5)]
    total = sum(v for _, v, _ in blocs)
    assert total == 73
    need, result = 60, 62
    p = reg(P3 + "ch12_coalitions.md", "12.2",
            "The cross-partisan coalition for District 7's environmental bond measure, in the illustrative shares of "
            "the chapter: progressive urban voters 30%, moderate suburban parents 25%, libertarian exurban voters "
            "10% and retired pragmatists 8%, 73% if the coalition holds, against the 60% the measure needs. The "
            "measure passes with 62%. The numbers after each bloc's name are its manifold distance to the measure as "
            "the chapter gives it.",
            "## District 7: The Bond Measure Coalition")
    c = canvas(720, 400, "A bond-measure coalition across the spectrum (illustrative)")
    x0, W = 190, 480

    def X(v):
        return x0 + W * v / 100

    rows = [("coalition if it holds", 120), ("result at the polls", 200)]
    for lab, y in rows:
        c.text(x0 - 12, y + 16, lab, 11.5, "end", INK2)
    acc = 0
    for j, (nm, v, dist) in enumerate(blocs):
        c.add(f'<rect x="{X(acc) + 1:.2f}" y="120" width="{W * v / 100 - 2:.2f}" height="24" fill="{SERIES[j]}">'
              f'<title>{nm} {v}%</title></rect>')
        c.text(X(acc + v / 2), 112, f"{v}", 11, "middle", INK)
        acc += v
    c.text(X(acc) + 8, 137, f"{total}%", 12, "start", INK, "600")
    c.hrect(X(0), 200, W * result / 100, 24, SERIES[7], title=f"result {result}%")
    c.text(X(result) + 8, 217, f"{result}%", 12, "start", INK, "600")
    c.line(X(need), 121, X(need), 240, CRITICAL, 1.5, dash="5 4")
    c.text(X(need), 258, "60% needed to pass", 10.5, "middle", INK2, italic=True)
    for v in (0, 20, 40, 60, 80, 100):
        c.text(X(v), 84, f"{v}%", 10, "middle", INK3)
    for j, (nm, v, dist) in enumerate(blocs):
        y = 296 + 20 * (j % 2)
        xx = 24 + 350 * (j // 2)
        c.add(f'<rect x="{xx:.2f}" y="{y - 9:.2f}" width="12" height="12" rx="3" fill="{SERIES[j]}"/>')
        c.text(xx + 18, y + 1, f"{nm} ({v}%, distance {dist:.1f})", 10.5, "start", INK2)
    c.text(16, 390, "District 7 bond measure, illustrative shares and distances", 10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 14
def fig_14_1():
    p = reg(P4 + "ch14_deliberative.md", "14.1",
            "Deliberation as manifold search, in the five stages of the preceding section. Participants start from "
            "positions and maps distorted by the media corruption modes of Chapter 11; briefings activate suppressed "
            "dimensions; neutral framing and data correct the metric; in-person dialogue shrinks perceived "
            "distances; and the assembly converges on a detailed proposal rather than a vote. A schematic of the "
            "chapter's posited mechanism.",
            "## Fishkin's Empirical Evidence, Geometrized")
    c = canvas(720, 300, "Deliberation as manifold search, stage by stage (schematic)")
    stages = [(["initial", "positions"], []), (["information", "provision"], []), (["heuristic", "calibration"], []),
              (["dialogue"], []), (["convergence"], [])]
    effect = [["maps distorted", "by four media", "corruption modes"],
              ["suppressed", "dimensions", "come into view"],
              ["neutral framing", "corrects", "distances"],
              ["in-person contact:", "perceived", "distances fall"],
              ["a detailed", "proposal, not", "a contraction"]]
    bw, gap, x0, y0, bh = 120, 25, 10, 96, 64
    for i, ((lines, sub), eff) in enumerate(zip(stages, effect)):
        x = x0 + i * (bw + gap)
        mbox(c, x, y0, bw, bh, lines, sub)
        for j, s in enumerate(eff):
            c.text(x + bw / 2, y0 + bh + 46 + 16 * j, s, 10.5, "middle", INK2)
        if i < 4:
            c.arrow(x + bw + 3, y0 + bh / 2, x + bw + gap - 3, y0 + bh / 2, INK2, 1.5)
    c.text(x0, 78, "stage", 11, "start", INK3, italic=True)
    c.text(x0, y0 + bh + 22, "geometric effect", 10.5, "start", INK3, italic=True)
    c.line(x0, y0 + bh + 27, x0 + 5 * bw + 4 * gap, y0 + bh + 27, GRID, 1)
    c.text(16, 288, "schematic of the chapter's posited mechanism, not a measurement", 10.5, "start", INK3,
           italic=True)
    c.save(p)


def fig_14_2():
    B = 10.0
    ideal = [(7, 6), (8, 4), (5, 7), (6, 5), (9, 6), (4, 8), (6, 8), (7, 8)]
    assert all(x + y > B for x, y in ideal)
    mx = sum(x for x, _ in ideal) / len(ideal)
    my = sum(y for _, y in ideal) / len(ideal)
    ex = (mx + my - B) / 2
    px, py = mx - ex, my - ex
    assert abs(px + py - B) < 1e-12 and (mx, my, px, py) == (6.5, 6.5, 5.0, 5.0)

    def sq(xx):
        return sum((xx - x) ** 2 + (B - xx - y) ** 2 for x, y in ideal)

    best = min((sq(i / 1000), i / 1000) for i in range(0, 10001))[1]
    assert abs(best - px) < 1e-3  # the closest point to the mean also minimizes total squared distance on the line
    p = reg(P4 + "ch14_deliberative.md", "14.2",
            "Participatory budgeting as the chapter states it, with two spending categories. Each dot is one citizen's "
            "ideal allocation; each asks for more than the budget allows. The budget constraint is a line (a "
            "hyperplane in more categories), and the allocation the chapter calls optimal is the point on it "
            "closest to the citizens' mean. Eight illustrative citizens, a budget of 10 units and Euclidean distance.",
            "## Case Studies in Deliberation")
    c = canvas(720, 400, "The allocation on the budget line closest to the citizens' mean")
    ax = Axes(c, 90, 52, 300, 300, (0, 10), (0, 10), [0, 2, 4, 6, 8, 10], [0, 2, 4, 6, 8, 10],
              "infrastructure, units", "education, units")
    c.line(ax.X(0), ax.Y(B), ax.X(B), ax.Y(0), SERIES[1], 2.5)
    c.text(ax.X(1.0), ax.Y(9.4), "budget line", 11, "start", INK2, italic=True)
    for x, y in ideal:
        c.dot(ax.X(x), ax.Y(y), SERIES[0], 4.5, title=f"ideal allocation ({x}, {y})")
    c.line(ax.X(mx), ax.Y(my), ax.X(px), ax.Y(py), INK, 1.5, dash="4 3")
    c.dot(ax.X(mx), ax.Y(my), INK, 5.5, title=f"mean ({mx:g}, {my:g})")
    c.dot(ax.X(px), ax.Y(py), CRITICAL, 6, title=f"closest allocation ({px:g}, {py:g})")
    c.text(ax.X(px) - 10, ax.Y(py) + 18, "closest allocation", 11, "end", INK)
    c.text(ax.X(mx), ax.Y(my) - 12, "mean", 11, "middle", INK)
    x0 = 440
    c.text(x0, 110, "dots: ideal allocations", 11.5, "start", INK2)
    c.text(x0, 130, "of eight citizens", 11.5, "start", INK2)
    c.text(x0, 164, f"mean ({mx:g}, {my:g}): over budget", 11.5, "start", INK2)
    c.text(x0, 198, f"closest point on the line:", 11.5, "start", INK2)
    c.text(x0, 218, f"({px:g}, {py:g}), summing to {B:g}", 11.5, "start", INK)
    c.text(x0, 252, "with more categories the line", 11, "start", INK2, italic=True)
    c.text(x0, 268, "becomes a hyperplane", 11, "start", INK2, italic=True)
    c.text(16, 390, "illustrative citizens and budget", 10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 16
def fig_16_1():
    part, n = 15_000, 200_000
    assert part / n == 0.075 and 1 - part / n == 0.925
    p = reg(P5 + "ch16_ai_politics.md", "16.1",
            "The hypothetical AI-assisted budgeting pilot of District 7, as the chapter describes it. Residents answer "
            "an online survey of 12 questions that places them on the six dimensions; the system takes the Fréchet "
            "mean of the respondents and the allocation across 8 categories closest to it on the budget hyperplane. "
            "The audit finds that low-income neighborhoods respond least, so d5, institutional trust, is "
            "underweighted for them; the fix reweights to the district's demographics and adds offline elicitation. "
            "Even then, 15,000 participants are 7.5% of the district.",
            "## Three Intersections of AI and Politics")
    c = canvas(720, 400, "Where the hypothetical AI budgeting pilot went wrong, and the fix")
    stages = [(["residents"], ["of District 7"]), (["online", "survey"], ["12 questions"]),
              (["positions"], ["six dimensions"]), (["Fréchet mean"], ["of respondents"]),
              (["allocation"], ["8 categories"])]
    bw, gap, x0, y0, bh = 120, 25, 10, 70, 70
    xs = []
    for i, (lines, sub) in enumerate(stages):
        x = x0 + i * (bw + gap)
        xs.append(x)
        mbox(c, x, y0, bw, bh, lines, sub)
        if i < 4:
            c.arrow(x + bw + 3, y0 + bh / 2, x + bw + gap - 3, y0 + bh / 2, INK2, 1.5)
    # the fault
    fx = xs[1] - 30
    mbox(c, fx, 196, 180, 62, ["bias"], ["low-income neighborhoods", "respond least"], stroke=CRITICAL)
    c.arrow(xs[1] + bw / 2, 196, xs[1] + bw / 2, y0 + bh + 4, CRITICAL, 1.5)
    c.text(fx + 196, 216, "result: d5, institutional trust,", 11, "start", INK2)
    c.text(fx + 196, 232, "underweighted for those", 11, "start", INK2)
    c.text(fx + 196, 248, "neighborhoods", 11, "start", INK2)
    mbox(c, fx, 286, 180, 62, ["fix"], ["reweight to demographics,", "add offline elicitation"], stroke=GOOD)
    c.line(fx, 317, fx - 18, 317, GOOD, 1.5)
    c.line(fx - 18, 317, fx - 18, y0 + bh / 2 + 30, GOOD, 1.5)
    c.arrow(fx - 18, y0 + bh / 2 + 30, xs[1] - 2, y0 + bh / 2 + 30, GOOD, 1.5)
    c.text(fx + 196, 312, "after the fix: 15,000 take part,", 11, "start", INK2)
    c.text(fx + 196, 328, "7.5% of the district; the other", 11, "start", INK2)
    c.text(fx + 196, 344, "92.5% are not represented", 11, "start", INK2)
    c.text(16, 390, "hypothetical pilot, illustrative numbers", 10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 17
def fig_17_1():
    # V4 = Z2 x Z2: e = (0,0), r = (1,0), s = (0,1), rs = (1,1)
    els = {"e": (0, 0), "r": (1, 0), "s": (0, 1), "rs": (1, 1)}

    def mul(a, b):
        return ((a[0] + b[0]) % 2, (a[1] + b[1]) % 2)

    assert all(mul(v, v) == (0, 0) for v in els.values())          # every element is its own inverse
    assert mul(els["r"], els["s"]) == mul(els["s"], els["r"]) == els["rs"]  # r and s commute
    assert len({mul(a, b) for a in els.values() for b in els.values()}) == 4  # closed, order four
    p = reg(P5 + "ch17_feedback_general_theory.md", "17.1",
            "The group named in the dated note at the head of Lesson 2. The correlative exchange r and the negation s "
            "are commuting involutions and generate the Klein four-group V4 = {e, r, s, rs}. Each edge applies one of "
            "them, and applying it twice returns to the start. Every element is its own inverse and no element "
            "cycles four positions, so the group has order four. The corners are the group's elements; the figure "
            "does not place the chapter's four political relations on them.",
            "## Lesson 3: Collective Choice as a New Geometric Regime")
    c = canvas(720, 400, "The Klein four-group: two commuting involutions, four elements")
    pos = {"e": (130, 110), "r": (350, 110), "s": (130, 310), "rs": (350, 310)}
    rr = 30
    for (a, b, col, lab) in (("e", "r", SERIES[0], "r"), ("s", "rs", SERIES[0], "r"),
                             ("e", "s", SERIES[1], "s"), ("r", "rs", SERIES[1], "s")):
        (x1, y1), (x2, y2) = pos[a], pos[b]
        if y1 == y2:
            c.line(x1 + rr + 2, y1, x2 - rr - 2, y2, col, 3)
            c.text((x1 + x2) / 2, y1 - 10, lab, 13, "middle", INK, "600")
        else:
            c.line(x1, y1 + rr + 2, x2, y2 - rr - 2, col, 3)
            c.text(x1 - 12, (y1 + y2) / 2 + 5, lab, 13, "end", INK, "600")
    for k, (x, y) in pos.items():
        circle(c, x, y, rr, BORDER, 1, fill=BOX)
        c.text(x, y + 6, k, 16, "middle", INK, "600")
    x0 = 452
    c.text(x0, 100, "r: correlative exchange, r² = e", 11.5, "start", INK)
    c.text(x0, 124, "s: negation, s² = e", 11.5, "start", INK)
    c.text(x0, 148, "rs = sr, and (rs)² = e", 11.5, "start", INK)
    c.text(x0, 188, "four elements, each its", 11, "start", INK2)
    c.text(x0, 204, "own inverse", 11, "start", INK2)
    c.text(x0, 236, "no element of order four:", 11, "start", INK2)
    c.text(x0, 252, "no quarter-turn", 11, "start", INK2)
    legend(c, x0, 300, [("edge: apply r", SERIES[0])], 10.5)
    legend(c, x0, 320, [("edge: apply s", SERIES[1])], 10.5)
    c.text(16, 390, "V4 as stated in the note of 2026-11-26; group elements only", 10.5, "start", INK3,
           italic=True)
    c.save(p)


def fig_17_2():
    p = reg(P5 + "ch17_feedback_general_theory.md", "17.2",
            "Lesson 5 as a loop. Institutions (parties, campaigns, media, the electoral system) decide which "
            "dimensions are politically activated, and activation decides which dimensions voters hold positions "
            "on; the institutions then contract the manifold they helped to shape. Below, the chapter's example: "
            "environmental priority, d3, absorbed into d1 or d2 in the 1970s, became an independent dimension when "
            "institutions began to treat it as one. A schematic of the chapter's posited feedback.",
            "## District 7: Four Lessons")
    c = canvas(720, 400, "Institutions and the preference manifold shape each other")
    mbox(c, 60, 104, 210, 76, ["institutions"], ["parties, campaigns, media,", "the electoral system"])
    mbox(c, 450, 104, 210, 76, ["preference manifold"], ["the dimensions on which", "voters hold positions"])
    # loop arrows
    c.line(165, 104, 165, 72, INK2, 1.5)
    c.line(165, 72, 555, 72, INK2, 1.5)
    c.arrow(555, 72, 555, 101, INK2, 1.5)
    c.text(360, 64, "activate dimensions", 11, "middle", INK)
    c.line(555, 180, 555, 212, INK2, 1.5)
    c.line(555, 212, 165, 212, INK2, 1.5)
    c.arrow(165, 212, 165, 183, INK2, 1.5)
    c.text(360, 230, "are contracted by", 11, "middle", INK)
    c.text(360, 146, "co-evolve", 12, "middle", INK3, italic=True)
    # example
    c.text(24, 270, "the chapter's example, d3 environmental priority", 11, "start", INK2, italic=True)
    ex = [(["1970s"], ["d3 folded into d1 or d2"]), (["institutions"], ["treat d3 as its own issue"]),
          (["d3"], ["an independent dimension"])]
    for i, (lines, sub) in enumerate(ex):
        x = 24 + 236 * i
        mbox(c, x, 284, 196, 56, lines, sub)
        if i < 2:
            c.arrow(x + 199, 312, x + 233, 312, INK2, 1.5)
    c.text(16, 390, "schematic of the chapter's posited feedback, not a measurement", 10.5, "start", INK3,
           italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 18
def fig_18_1():
    ds = list(range(1, 11))
    bound = [(d - 1) / d for d in ds]
    assert round(100 * bound[5]) == 83 and round(100 * bound[3]) == 75
    p = reg(P5 + "ch18_open_questions.md", "18.1",
            "The lower bound of the Democratic Irrecoverability Theorem (Chapter 5, Theorem 1(c)) on the share of "
            "manifold information a single-winner election destroys, (d − dim O)/d with dim O = 1, against the "
            "effective dimensionality d. If d is 4 rather than 6 the bound drops from 83% to 75%, as Question 2 "
            "states, so the bound depends on getting d right.",
            "## Question 3: Is There a Conservation Law for Democratic Legitimacy?")
    c = canvas(720, 400, "The loss bound under plurality depends on the dimensionality")
    ax = Axes(c, 80, 58, 520, 270, (0.5, 10.5), (0, 1), ds, [0, 0.25, 0.5, 0.75, 1.0],
              "effective dimensionality d", "least share destroyed")
    pts = [(ax.X(d), ax.Y(v)) for d, v in zip(ds, bound)]
    c.polyline(pts, SERIES[0], 2, title="(d − 1)/d")
    for d, v, (x, y) in zip(ds, bound, pts):
        hi = d in (4, 6)
        c.dot(x, y, CRITICAL if hi else SERIES[0], 5.5 if hi else 4.5, title=f"d = {d}: {100 * v:.0f}%")
    for d in (4, 6):
        x, y = pts[d - 1]
        c.text(x + 8, y + 22, f"d = {d}: {100 * bound[d - 1]:.0f}%", 11, "start", INK)
    c.text(ax.X(1) + 10, ax.Y(0) - 10, "d = 1: no loss", 10.5, "start", INK2, italic=True)
    c.text(ax.X(10.4), ax.Y(0.95) - 8, "(d − 1)/d", 11.5, "end", INK2, italic=True)
    c.text(16, 390, "lower bound for a single-winner outcome, dim O = 1", 10.5, "start", INK3, italic=True)
    c.save(p)
