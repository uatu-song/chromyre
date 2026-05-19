#!/usr/bin/env python3
"""
Chromyre Chronicles — V2 markdown-to-PDF build pipeline.

Reads chromyre_manuscript_censored.md and produces Chromyre_Chronicles_FINAL.pdf,
a 5x8 print-ready trade paperback for The Book Patch.

See CLAUDE_CODE_HANDOFF.md / "CLAUDE_CODE_HANDOFF (1).md" for the full spec.
"""

import os
import re
import sys

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
)
from reportlab.platypus.tableofcontents import TableOfContents


HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_SRC_MD = os.path.join(HERE, "chromyre_manuscript_censored.md")
DEFAULT_OUT_PDF = os.path.join(HERE, "Chromyre_Chronicles_FINAL.pdf")
SRC_MD = DEFAULT_SRC_MD
OUT_PDF = DEFAULT_OUT_PDF


# ---------------------------------------------------------------------------
# Fonts
# ---------------------------------------------------------------------------

DEJAVU = "/usr/share/fonts/truetype/dejavu"
LOCAL_FONTS = os.path.join(HERE, "fonts")

FONTS = {
    "Serif":    f"{DEJAVU}/DejaVuSerif.ttf",
    "Serif-B":  f"{DEJAVU}/DejaVuSerif-Bold.ttf",
    "Serif-I":  f"{DEJAVU}/DejaVuSerif-Italic.ttf",
    "Serif-BI": f"{DEJAVU}/DejaVuSerif-BoldItalic.ttf",
    "Sans":     f"{DEJAVU}/DejaVuSans.ttf",
    "Sans-B":   f"{DEJAVU}/DejaVuSans-Bold.ttf",
    "Mono":     f"{DEJAVU}/DejaVuSansMono.ttf",
    "Poppins-B": f"{LOCAL_FONTS}/Poppins-Bold.ttf",
    "Lora-B":    f"{LOCAL_FONTS}/Lora-VariableFont.ttf",
    "Lora-BI":   f"{LOCAL_FONTS}/Lora-Italic-VariableFont.ttf",
}


def register_fonts():
    for name, path in FONTS.items():
        pdfmetrics.registerFont(TTFont(name, path))
    # Font families so <i>/<b> tags inside paragraphs resolve.
    from reportlab.pdfbase.pdfmetrics import registerFontFamily
    registerFontFamily(
        "Serif",
        normal="Serif", bold="Serif-B", italic="Serif-I", boldItalic="Serif-BI",
    )
    registerFontFamily(
        "Lora-B",
        normal="Lora-B", bold="Lora-B", italic="Lora-BI", boldItalic="Lora-BI",
    )


# ---------------------------------------------------------------------------
# Front / back matter (hardcoded — not in the markdown)
# ---------------------------------------------------------------------------

TITLE_LINE_1 = "CHROMYRE"
TITLE_LINE_2 = "CHRONICLES"

_STUDENT_LINES_RAW = [
    "Mehdi Al-Abdul-Rasool",
    "Emad Edeen Alhashemi",
    "Ali Alnasser · Sri Charith Badeti",
    "Yoyo Fang · Rohan Gadiraju",
    "Ahaana Guggari · Mustafa Haydar",
    "Zaid Mahdi · Hannah Mix",
    "Xenia Odare · Mya Pradhan",
    "Kincaid Avery Start · Ryann Stoops",
]
# Replace spaces within names with non-breaking spaces so a name never splits
# mid-word during line-wrap. Names are separated by " · ".
STUDENT_LINES = [
    " · ".join(name.replace(" ", " ") for name in line.split(" · "))
    for line in _STUDENT_LINES_RAW
]

DEDICATION_LINES = [
    "For the kingdom of Chromyre,",
    "which lived because fourteen",
    "students imagined it.",
]

TEACHER_NOTE_PARAS = [
    "I write this as a genuine fan of these kids. And they are, in fact, kids. "
    "From the vague, half-formed imaginings of the possibilities of an elective "
    "that leveraged chess matches to teach storytelling and structure emerged a "
    "legitimate innovation in book production. To be very honest, we stumbled "
    "here, upon this form and function.",

    "It was never supposed to be this. Nobody asked for this. That’s a "
    "tongue-in-cheek inside joke among our class when we announced that we "
    "needed a tagline. Ryann, probably half paying attention and likely "
    "thinking she had more homework, uttered, “What? Nobody asked for "
    "this.” And we loved it.",

    "The book is written by 7th and 8th graders and it shows — full of "
    "sincerity, humor (some hilariously unintentional), video game logic, manga "
    "tropes, and most unexpectedly of all, cohesion. Thanks to ad hoc AI app "
    "building that translated chess PGNs into story scaffolding, they achieved "
    "something out of pure organized chaos, love of story, and middle school "
    "joy that, perhaps, may never have been done before.",

    "We would have been nowhere without Yoyo, whose fiery (borderline "
    "obsessive) passion drove her to sacrifice sleep constructing a sprawling "
    "story universe, building the magic system nearly overnight, and acting as "
    "showrunner for 13 others while contributing her own story. It has been my "
    "privilege to watch them do this with almost no direction from me; my "
    "expectation was a disjointed collection of independent efforts. It is "
    "always a reminder of why I teach when students shock and amaze, but this "
    "time I’m deeply humbled by their enthusiasm, work ethic, and "
    "willingness to collaborate — an emblem of what can be achieved with "
    "full hearts and a single unified goal.",

    "I learned a lot.",
]

COPYRIGHT_LINES = [
    "Copyright © 2026 by Yoyo Fang and 14 PSCA Students",
    "",
    "All rights reserved. No part of this book may be reproduced or used in any "
    "manner without written permission of the copyright owner except for the use "
    "of quotations in a book review.",
    "",
    "First edition 2026.",
    "",
    "This work is the product of a middle-school creative writing elective and "
    "is intended for educational and personal use.",
    "",
    "Front cover art by Yoyo Fang.",
    "Back cover art by Hannah Mix.",
    "",
    "Chess & Narrative",
    "Taught by Joseph Song",
    "",
    "Plymouth Scholars Charter Academy",
    "Sabrina Terenzi, Principal",
    "Plymouth, MI",
]


# ---------------------------------------------------------------------------
# PGN — full game
# ---------------------------------------------------------------------------

FULL_PGN = (
    "1. e4 Nf6 2. e5 Ng4 3. f4 Nh6 4. h3 Nc6 5. d4 Nf5 6. d5 Na5 7. g4 Nh6 8. g5 Ng8 "
    "9. b4 Nc4 10. Nc3 Nb6 11. a4 d6 12. Nf3 dxe5 13. fxe5 Nxd5 14. Nxd5 c6 15. Nf4 Bf5 "
    "16. Ra2 Qxd1+ 17. Kxd1 Rd8+ 18. Ke1 Bxc2 19. Rxc2 e6 20. h4 Bxb4+ 21. Kf2 Rc8 "
    "22. Be3 Ne7 23. Bxa7 Ba5 24. g6 fxg6 25. Nxe6 Rg8 26. Nfd4 Ra8 27. Nxc6 bxc6 "
    "28. Bc5 Ra6 29. Bxa6 Bc7 30. Kf3 Bxe5 31. Re2 Bb8 32. Rh3 Nd5 33. Rd2 Nc3 34. a5 "
    "Nb1 35. Rg2 Rf8+ 36. Ke2 Rf6 37. Nxg7+ Kf7 38. Rxg6 Kxg6 39. Ne8 Rf8 40. Nd6 Rd8 "
    "41. Nb7 Rd5 42. Bf8 Rd8 43. Ba3 Rd4 44. Bf8 Bf4 45. Nd8 c5 46. Ne6 c4 47. Bxc4 Rxc4 "
    "48. a6 Ra4 49. Nc5 Rxa6 50. Nxa6 Bd6 51. Rg3+ Kf6 52. Rg8 Bxf8 53. Rxf8+ Kg7 "
    "54. Rf1 Nc3+ 55. Kf2 Ne4+ 56. Kg1 Nc5 57. h5 Nxa6 58. Rf5 Kh6 59. Kf2 Nc5 "
    "60. Rxc5 Kg7 61. Rc7+ Kh8 62. h6 Kg8 63. Ke2 Kf8 64. Rxh7 Kg8 65. Rc7 Kf8 66. h7 "
    "Ke8 67. h8=Q#"
)


# ---------------------------------------------------------------------------
# Character move ranges
# ---------------------------------------------------------------------------

CHAR_RANGES = {
    "Jerrica":       (0,    0),
    "Rowan":         (1,  118),
    "Stormy":        (7,   26),
    "Xanthos":       (18,  99),
    "Henry Emily":   (22,  53),
    "Zarathura":     (29,  36),
    "Max":           (30,  75),
    "Kizzlefitch":   (31,  32),
    "Kerian":        (33,  56),
    "Jocelyn":       (39, 104),
    "Robert Topala": (42,  87),
    "Yu":            (49,  98),
    "Major Potato":  (56,  93),
    "Monk":          (62, 129),
}


# ---------------------------------------------------------------------------
# Zarathura's song
# ---------------------------------------------------------------------------

# (kind, text) where kind in {"V","C","B"}: V=verse, C=chorus, B=blank
SONG = [
    ("V", "Our king had a very good plannn"),
    ("V", "He'd quietly cull as he can"),
    ("V", "He put plague in the grain"),
    ("V", "And called it gods rain"),
    ("V", "Now who's gonna stop that old man"),
    ("B", ""),
    ("V", "There once was a king with a plan"),
    ("V", "To thin out his people's lifespan"),
    ("V", "He shipped in the grain"),
    ("V", "With spores in each vein"),
    ("V", "And called it all part of gods plan"),
    ("B", ""),
    ("C", "Oh the kingggg"),
    ("C", "Oh the kingggg"),
    ("C", "He gave us a gift and it had a stingggg"),
    ("C", "Oh the kingggg"),
    ("C", "Oh the kingggg"),
    ("C", "Everybody danced but nobody singsss"),
    ("C", "Oh the king"),
    ("B", ""),
    ("V", "A king thought his people too manyyyy"),
    ("V", "And didn't want to spare them a pennyyyy"),
    ("V", "He poisoned the wheat"),
    ("V", "And watched them all tweeeet"),
    ("V", "Now the kingdom don't got hardly any"),
    ("B", ""),
    ("V", "You ask who would do such a thing"),
    ("V", "On a whim, on a prayer, and a wing"),
    ("V", "The people all danced"),
    ("V", "And nobody glanced"),
    ("V", "Still don't know? Who but the—"),
    ("B", ""),
    ("C", "Oh the kingggg"),
    ("C", "Oh the kingggg"),
    ("C", "He gave us a gift and it had a stingggg"),
    ("C", "Oh the kingggg"),
    ("C", "Oh the kingggg"),
    ("C", "Everybody danced but nobody singsss"),
    ("C", "Oh the king"),
    ("B", ""),
    ("V", "There once was a kingdom that danced"),
    ("V", "Not because anyone asked"),
    ("V", "The king said “too manyyyy”"),
    ("V", "And poisoned the granny"),
    ("V", "Now nobody's left but the last"),
    ("B", ""),
    ("V", "Who put the plague in the grain?"),
    ("C", "(The king! The king!)"),
    ("V", "Who called all our dying gods rain?"),
    ("C", "(The king! The king!)"),
    ("V", "Who's sitting up high while we rot in the lane?"),
    ("C", "The king, the king, the king"),
]

def _normalize_quotes(s):
    """Collapse curly quotes/apostrophes to ASCII for comparison purposes.

    The SONG constant uses curly quotes for prettier rendering, but the
    markdown source uses straight ASCII quotes. Without normalization,
    a single curly/straight mismatch makes a song line fail the lookup,
    which turns off song-mode and causes every subsequent verse to be
    re-emitted as a prose paragraph.
    """
    return (
        s.replace("“", '"').replace("”", '"')
         .replace("‘", "'").replace("’", "'")
    )


SONG_TEXTS = {_normalize_quotes(t) for _, t in SONG if t}
SONG_FIRST_LINE = _normalize_quotes(SONG[0][1])


# ---------------------------------------------------------------------------
# Chess engine
# ---------------------------------------------------------------------------

INITIAL_BOARD = {}
def _init_board():
    pieces = "RNBQKBNR"
    for f, p in enumerate(pieces):
        INITIAL_BOARD[(f, 0)] = p             # white back rank
        INITIAL_BOARD[(f, 7)] = p.lower()     # black back rank
    for f in range(8):
        INITIAL_BOARD[(f, 1)] = "P"
        INITIAL_BOARD[(f, 6)] = "p"
_init_board()


def san_tokens(pgn_str):
    """Strip move numbers, return list of SAN tokens."""
    tokens = pgn_str.replace("\n", " ").split()
    out = []
    for t in tokens:
        if re.match(r"^\d+\.+$", t):
            continue
        if t in ("1-0", "0-1", "1/2-1/2", "*"):
            continue
        out.append(t)
    return out


def in_bounds(f, r):
    return 0 <= f < 8 and 0 <= r < 8


def piece_can_reach(piece, src, dst, board):
    """Geometric reachability — ignores check; PGN won't ask for illegal moves."""
    pf, pr = src
    df, dr = dst
    ptype = piece.upper()
    df_dir = df - pf
    dr_dir = dr - pr

    if ptype == "N":
        return (abs(df_dir), abs(dr_dir)) in ((1, 2), (2, 1))

    if ptype == "K":
        return max(abs(df_dir), abs(dr_dir)) == 1

    if ptype in ("B", "R", "Q"):
        if ptype == "B" and abs(df_dir) != abs(dr_dir):
            return False
        if ptype == "R" and df_dir != 0 and dr_dir != 0:
            return False
        if ptype == "Q":
            if df_dir != 0 and dr_dir != 0 and abs(df_dir) != abs(dr_dir):
                return False
        steps = max(abs(df_dir), abs(dr_dir))
        sf = (df_dir // steps) if df_dir else 0
        sr = (dr_dir // steps) if dr_dir else 0
        for i in range(1, steps):
            if (pf + i * sf, pr + i * sr) in board:
                return False
        return True

    return False  # pawn handled separately


def pawn_candidates(color, dst, capture, board, file_hint=None, ep_target=None):
    df, dr = dst
    out = []
    direction = 1 if color == "w" else -1
    start_rank = 1 if color == "w" else 6

    if capture:
        # Pawn capture comes from (df-1, dr-direction) or (df+1, dr-direction).
        if file_hint is not None:
            fr = file_hint
            sf = (fr, dr - direction)
            if in_bounds(*sf):
                p = board.get(sf)
                if p and ((color == "w" and p == "P") or (color == "b" and p == "p")):
                    if (dst in board) or (ep_target == dst):
                        out.append(sf)
        else:
            for sf in [(df - 1, dr - direction), (df + 1, dr - direction)]:
                if in_bounds(*sf):
                    p = board.get(sf)
                    if p and ((color == "w" and p == "P") or (color == "b" and p == "p")):
                        if (dst in board) or (ep_target == dst):
                            out.append(sf)
    else:
        sf = (df, dr - direction)
        if in_bounds(*sf):
            p = board.get(sf)
            if p and ((color == "w" and p == "P") or (color == "b" and p == "p")):
                if dst not in board:
                    out.append(sf)
        # Two-square advance
        if dr - direction * 2 == start_rank - direction * 0:  # i.e. dr == start_rank + direction*2 essentially
            pass
        if (dr == start_rank + 2 * direction):
            sf2 = (df, dr - 2 * direction)
            mid = (df, dr - direction)
            if in_bounds(*sf2):
                p = board.get(sf2)
                if p and ((color == "w" and p == "P") or (color == "b" and p == "p")):
                    if dst not in board and mid not in board:
                        out.append(sf2)
    return out


def apply_move(board, token, turn, ep_target):
    """
    Apply one SAN token to the board. Returns (new_board, new_ep_target).
    `turn` is "w" or "b".
    """
    board = dict(board)
    # Strip annotation suffixes
    raw = token.rstrip("+#?!")
    # Castling
    if raw in ("O-O", "0-0"):
        rank = 0 if turn == "w" else 7
        king = "K" if turn == "w" else "k"
        rook = "R" if turn == "w" else "r"
        del board[(4, rank)]
        board[(6, rank)] = king
        del board[(7, rank)]
        board[(5, rank)] = rook
        return board, None
    if raw in ("O-O-O", "0-0-0"):
        rank = 0 if turn == "w" else 7
        king = "K" if turn == "w" else "k"
        rook = "R" if turn == "w" else "r"
        del board[(4, rank)]
        board[(2, rank)] = king
        del board[(0, rank)]
        board[(3, rank)] = rook
        return board, None

    # Promotion
    promote_to = None
    if "=" in raw:
        raw, promote_to = raw.split("=", 1)

    capture = "x" in raw
    raw_clean = raw.replace("x", "")

    # Destination is last 2 chars
    dst_sq = raw_clean[-2:]
    df = ord(dst_sq[0]) - ord("a")
    dr = int(dst_sq[1]) - 1
    rest = raw_clean[:-2]

    # First char piece type?
    if rest and rest[0] in "KQRBN":
        ptype = rest[0]
        disamb = rest[1:]
    else:
        ptype = "P"
        disamb = rest

    file_hint = None
    rank_hint = None
    for ch in disamb:
        if ch in "abcdefgh":
            file_hint = ord(ch) - ord("a")
        elif ch in "12345678":
            rank_hint = int(ch) - 1

    new_ep = None
    if ptype == "P":
        candidates = pawn_candidates(
            turn, (df, dr), capture, board,
            file_hint=file_hint, ep_target=ep_target,
        )
        if not candidates:
            raise RuntimeError(f"No pawn candidate for {token} at {dst_sq}")
        src = candidates[0]
        # En-passant capture removes the passed pawn
        if capture and (df, dr) == ep_target and (df, dr) not in board:
            pawn_rank = dr - (1 if turn == "w" else -1)
            board.pop((df, pawn_rank), None)
        # Two-square advance enables ep
        if abs(dr - src[1]) == 2:
            new_ep = (df, (dr + src[1]) // 2)
        # Move
        del board[src]
        piece = "P" if turn == "w" else "p"
        if promote_to:
            piece = promote_to.upper() if turn == "w" else promote_to.lower()
        board[(df, dr)] = piece
        return board, new_ep

    # Non-pawn piece move
    piece_letter = ptype if turn == "w" else ptype.lower()
    candidates = []
    for sq, p in board.items():
        if p != piece_letter:
            continue
        if file_hint is not None and sq[0] != file_hint:
            continue
        if rank_hint is not None and sq[1] != rank_hint:
            continue
        if piece_can_reach(p, sq, (df, dr), board):
            candidates.append(sq)
    if len(candidates) != 1:
        # When multiple geometric candidates, fall back to legality-after-move check
        if len(candidates) > 1:
            # Pick the one that, when moved, leaves own king safe — but PGN is fine
            # in practice; just take the first that resolves.
            # Try filtering by "doesn't leave king in check" — skipped for brevity.
            candidates = [candidates[0]]
        else:
            raise RuntimeError(f"No piece candidate for {token}")
    src = candidates[0]
    del board[src]
    board[(df, dr)] = piece_letter
    return board, None


def build_board_states(pgn_str):
    """Return list of board states: state[i] = position after i half-moves."""
    tokens = san_tokens(pgn_str)
    states = [dict(INITIAL_BOARD)]
    ep = None
    for i, tok in enumerate(tokens):
        turn = "w" if i % 2 == 0 else "b"
        board, ep = apply_move(states[-1], tok, turn, ep)
        states.append(board)
    return states


# ---------------------------------------------------------------------------
# Board rendering
# ---------------------------------------------------------------------------

PIECE_UNICODE = {
    "P": "♙", "R": "♖", "N": "♘", "B": "♗", "Q": "♕", "K": "♔",
    "p": "♟", "r": "♜", "n": "♞", "b": "♝", "q": "♛", "k": "♚",
}
LIGHT = "░"  # ░
DARK  = "▓"  # ▓


def render_board_rows(board):
    rows = []
    for r in range(7, -1, -1):
        cells = []
        for f in range(8):
            piece = board.get((f, r))
            if piece:
                cells.append(PIECE_UNICODE[piece])
            else:
                cells.append(LIGHT if (r + f) % 2 == 1 else DARK)
        rows.append(" ".join(cells))
    return rows


# ---------------------------------------------------------------------------
# Markdown parser
# ---------------------------------------------------------------------------

PARA_END_CHARS = '.?!"”’…'
SEP_RE = re.compile(r"^[·•]\s+[·•]\s+[·•]$")
CHAR_RE = re.compile(r"^\*\*—\s+(.+?)\s+—\*\*$")
SECTION_RE = re.compile(r"^##\s+Chapter\s+\d+:\s+(.+)$")


def parse_markdown(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    blocks = []
    buf = []
    in_song = False

    def flush():
        if buf:
            text = " ".join(buf).strip()
            if text:
                blocks.append(("PARA", text))
            buf.clear()

    for line in lines:
        s = line.strip()

        if not s:
            flush()
            continue

        # Document-level title or italic editorial note
        if s.startswith("# ") or s.startswith("*For editorial"):
            flush()
            continue

        if s == "---":
            flush()
            continue

        m = SECTION_RE.match(s)
        if m:
            flush()
            in_song = False
            blocks.append(("SECTION", m.group(1).strip()))
            continue

        m = CHAR_RE.match(s)
        if m:
            flush()
            in_song = False
            blocks.append(("CHAR", m.group(1).strip()))
            continue

        if SEP_RE.match(s):
            flush()
            in_song = False
            blocks.append(("SEP", None))
            continue

        # Song handling: starts when we see the first song line; ends when a non-song line appears.
        s_normalized = _normalize_quotes(s)
        if not in_song and s_normalized == SONG_FIRST_LINE:
            flush()
            in_song = True
            for kind, txt in SONG:
                if kind == "B":
                    blocks.append(("SONG_BLANK", None))
                elif kind == "V":
                    blocks.append(("SONG_V", txt))
                else:
                    blocks.append(("SONG_C", txt))
            continue
        if in_song:
            # Skip every song body line (we already emitted from SONG constant).
            if s_normalized in SONG_TEXTS:
                continue
            in_song = False

        buf.append(s)
        if s[-1] in PARA_END_CHARS:
            flush()

    flush()
    return blocks


# ---------------------------------------------------------------------------
# Styles
# ---------------------------------------------------------------------------

def make_styles():
    s = {}
    s["body"] = ParagraphStyle(
        "body", fontName="Serif", fontSize=9.5, leading=17.5,
        spaceAfter=6, alignment=TA_JUSTIFY, firstLineIndent=14,
    )
    s["body_first"] = ParagraphStyle(
        "body_first", parent=s["body"], firstLineIndent=0,
    )
    s["char_header"] = ParagraphStyle(
        "char_header", fontName="Serif-B", fontSize=11, leading=14,
        spaceBefore=8, spaceAfter=4, alignment=TA_CENTER,
    )
    s["section_title"] = ParagraphStyle(
        "section_title", fontName="Serif-B", fontSize=18, leading=24,
        spaceAfter=10, spaceBefore=6, alignment=TA_CENTER,
    )
    s["chapter_title"] = ParagraphStyle(
        "chapter_title", fontName="Serif-I", fontSize=9, leading=13,
        spaceAfter=2, alignment=TA_CENTER,
        textColor=colors.HexColor("#888888"),
    )
    s["move_range"] = ParagraphStyle(
        "move_range", fontName="Serif-I", fontSize=8, leading=11,
        spaceAfter=8, alignment=TA_CENTER,
        textColor=colors.HexColor("#666666"),
    )
    s["board_line"] = ParagraphStyle(
        "board_line", fontName="Sans", fontSize=12, leading=15,
        spaceAfter=0, alignment=TA_CENTER,
    )
    s["sep"] = ParagraphStyle(
        "sep", fontName="Serif", fontSize=11, leading=16,
        spaceAfter=8, spaceBefore=8, alignment=TA_CENTER,
    )
    s["song_line"] = ParagraphStyle(
        "song_line", fontName="Serif-I", fontSize=10, leading=14,
        spaceAfter=0, alignment=TA_CENTER,
    )
    s["song_chorus"] = ParagraphStyle(
        "song_chorus", fontName="Serif-BI", fontSize=10, leading=14,
        spaceAfter=0, alignment=TA_CENTER,
    )
    s["half_title"] = ParagraphStyle(
        "half_title", fontName="Lora-BI", fontSize=34, leading=42,
        alignment=TA_CENTER,
    )
    s["title_main"] = ParagraphStyle(
        "title_main", fontName="Poppins-B", fontSize=30, leading=36,
        alignment=TA_CENTER, spaceAfter=4,
    )
    s["title_byline"] = ParagraphStyle(
        "title_byline", fontName="Serif", fontSize=10, leading=14,
        alignment=TA_CENTER, spaceAfter=2,
    )
    s["title_credit_italic"] = ParagraphStyle(
        "title_credit_italic", fontName="Serif-I", fontSize=10, leading=14,
        alignment=TA_CENTER, spaceAfter=2,
    )
    s["copyright"] = ParagraphStyle(
        "copyright", fontName="Serif", fontSize=8, leading=11,
        spaceAfter=3, alignment=TA_CENTER,
        textColor=colors.HexColor("#222222"),
    )
    s["dedication"] = ParagraphStyle(
        "dedication", fontName="Serif-I", fontSize=12, leading=17,
        alignment=TA_CENTER, spaceAfter=2,
    )
    s["frontmatter_title"] = ParagraphStyle(
        "frontmatter_title", fontName="Serif-B", fontSize=11, leading=15,
        alignment=TA_CENTER, spaceAfter=14,
    )
    s["note_body"] = ParagraphStyle(
        "note_body", fontName="Serif", fontSize=9, leading=13.5,
        alignment=TA_JUSTIFY, spaceAfter=8,
        firstLineIndent=12,
    )
    s["note_body_first"] = ParagraphStyle(
        "note_body_first", parent=s["note_body"], firstLineIndent=0,
    )
    s["note_sig"] = ParagraphStyle(
        "note_sig", fontName="Serif-I", fontSize=9, leading=13,
        alignment=TA_RIGHT, spaceBefore=6,
    )
    s["pgn"] = ParagraphStyle(
        "pgn", fontName="Mono", fontSize=8, leading=11.5,
        alignment=TA_LEFT, spaceAfter=0,
    )
    s["display_title"] = ParagraphStyle(
        "display_title", fontName="Lora-BI", fontSize=28, leading=34,
        alignment=TA_CENTER, spaceAfter=2,
    )
    s["display_sub"] = ParagraphStyle(
        "display_sub", fontName="Serif-I", fontSize=10, leading=14,
        alignment=TA_CENTER, spaceAfter=14,
        textColor=colors.HexColor("#666666"),
    )
    s["display_ornament"] = ParagraphStyle(
        "display_ornament", fontName="Sans", fontSize=14, leading=18,
        alignment=TA_CENTER, spaceBefore=12, spaceAfter=4,
        textColor=colors.HexColor("#666666"),
    )
    s["result_line"] = ParagraphStyle(
        "result_line", fontName="Serif-BI", fontSize=12, leading=16,
        alignment=TA_CENTER, spaceBefore=14,
    )
    s["toc_entry"] = ParagraphStyle(
        "toc_entry", fontName="Serif", fontSize=11, leading=22,
        alignment=TA_LEFT,
    )
    return s


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def format_para(text):
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"\*([^*]+)\*", r"<i>\1</i>", text)
    return text


def board_flowable(name, board, styles, lo, hi, appearance, total_appearances,
                   prepend_sep=False, follow_paragraph=None):
    """Return a KeepTogether containing (optional SEP) + board + move label +
    character header + optionally the first body paragraph. Folding the first
    paragraph into the same unit guarantees the `— Name —` header never lands
    alone at the bottom of a page.
    """
    if total_appearances <= 1 or hi == lo:
        half = lo
    else:
        half = lo + round((hi - lo) * appearance / (total_appearances - 1))
    half = max(0, min(half, len(board) - 1))
    state = board[half]
    rows = render_board_rows(state)

    move_num = half // 2 + 1
    if lo == hi:
        move_label = f"Move {lo // 2 + 1}"
    else:
        lo_move = lo // 2 + 1
        hi_move = hi // 2 + 1
        move_label = f"Moves {lo_move}–{hi_move} · shown at move {move_num}"

    elems = []
    if prepend_sep:
        elems.append(Spacer(1, 4))
        elems.append(Paragraph("· · ·", styles["sep"]))
        elems.append(Spacer(1, 10))
    else:
        elems.append(Spacer(1, 6))
    for row in rows:
        elems.append(Paragraph(row, styles["board_line"]))
    elems.append(Spacer(1, 3))
    elems.append(Paragraph(move_label, styles["move_range"]))
    elems.append(Spacer(1, 4))
    elems.append(Paragraph(f"— {name} —", styles["char_header"]))
    elems.append(Spacer(1, 4))
    if follow_paragraph is not None:
        elems.append(follow_paragraph)
    return KeepTogether(elems)


# ---------------------------------------------------------------------------
# Document template
# ---------------------------------------------------------------------------

PAGE_W = 5 * inch
PAGE_H = 8 * inch
# Inner = gutter (spine-side) margin; intentionally generous so the binding
# doesn't eat the text block and the spine has enough page count to print on.
MARGIN_OUTER = 0.6 * inch
MARGIN_INNER = 1.0 * inch
MARGIN_TOP = 0.8 * inch
MARGIN_BOT = 0.8 * inch


class ChromyreDoc(BaseDocTemplate):
    def __init__(self, filename):
        super().__init__(
            filename,
            pagesize=(PAGE_W, PAGE_H),
            leftMargin=MARGIN_INNER,
            rightMargin=MARGIN_OUTER,
            topMargin=MARGIN_TOP,
            bottomMargin=MARGIN_BOT,
        )
        frame = Frame(
            MARGIN_INNER, MARGIN_BOT,
            PAGE_W - MARGIN_INNER - MARGIN_OUTER,
            PAGE_H - MARGIN_TOP - MARGIN_BOT,
            id="main",
            leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0,
        )
        self.addPageTemplates([PageTemplate(id="main", frames=[frame], onPage=self._on_page)])

    def _on_page(self, canvas, doc):
        # Draw page number first, in raw page coordinates — so it sits at the
        # true outer edge regardless of any frame mirroring below.
        self._page_num(canvas, doc)

        # The frame is anchored at MARGIN_INNER from the left, leaving MARGIN_OUTER
        # on the right. That's correct for odd (recto) pages: spine on the left,
        # the wide inner margin IS the gutter, text block offset to the right.
        #
        # On even (verso) pages the spine is on the right. We need the wide
        # inner margin on the right and the narrower outer margin on the left —
        # so shift the text block LEFT by (MARGIN_INNER - MARGIN_OUTER). The
        # translation persists for this page's frame drawing and resets at the
        # next showPage.
        if doc.page % 2 == 0:
            canvas.translate(-(MARGIN_INNER - MARGIN_OUTER), 0)

    def _page_num(self, canvas, doc):
        if doc.page <= 10:
            return
        canvas.saveState()
        canvas.setFont("Serif", 9)
        canvas.setFillColor(colors.HexColor("#444444"))
        y = MARGIN_BOT * 0.5
        if doc.page % 2 == 1:
            canvas.drawRightString(PAGE_W - MARGIN_OUTER, y, str(doc.page))
        else:
            canvas.drawString(MARGIN_OUTER, y, str(doc.page))
        canvas.restoreState()

    def afterFlowable(self, flowable):
        if hasattr(flowable, "style") and flowable.style.name == "section_title":
            text = flowable.getPlainText()
            self.notify("TOCEntry", (0, text, self.page))


# ---------------------------------------------------------------------------
# Story assembly
# ---------------------------------------------------------------------------

def _blank_page(styles):
    return [Paragraph("&nbsp;", styles["body"]), PageBreak()]


def build_front_matter(styles):
    story = []

    # p1: blank
    story.extend(_blank_page(styles))
    # p2: blank
    story.extend(_blank_page(styles))

    # p3: half-title
    story.append(Spacer(1, PAGE_H * 0.30))
    story.append(Paragraph(TITLE_LINE_1, styles["half_title"]))
    story.append(Paragraph(TITLE_LINE_2, styles["half_title"]))
    story.append(PageBreak())

    # p4: blank
    story.extend(_blank_page(styles))

    # p5: title page
    story.append(Spacer(1, PAGE_H * 0.15))
    story.append(Paragraph(TITLE_LINE_1, styles["title_main"]))
    story.append(Paragraph(TITLE_LINE_2, styles["title_main"]))
    story.append(Spacer(1, 24))
    for line in STUDENT_LINES:
        story.append(Paragraph(line, styles["title_byline"]))
    story.append(Spacer(1, 18))
    story.append(Paragraph("<i>World created by Yoyo Fang</i>", styles["title_credit_italic"]))
    story.append(Paragraph("<i>Chess game played by Ryann Stoops</i>", styles["title_credit_italic"]))
    story.append(PageBreak())

    # p6: copyright
    story.append(Spacer(1, PAGE_H * 0.30))
    for line in COPYRIGHT_LINES:
        if line == "":
            story.append(Spacer(1, 4))
        else:
            story.append(Paragraph(line, styles["copyright"]))
    story.append(PageBreak())

    # p7: dedication
    story.append(Spacer(1, PAGE_H * 0.40))
    for line in DEDICATION_LINES:
        story.append(Paragraph(line, styles["dedication"]))
    story.append(PageBreak())

    # p8: TOC
    story.append(Spacer(1, PAGE_H * 0.10))
    story.append(Paragraph("Contents", styles["display_title"]))
    story.append(HRFlowable(
        width="30%", thickness=0.6,
        color=colors.HexColor("#888888"),
        spaceAfter=18, hAlign="CENTER",
    ))
    toc = TableOfContents()
    toc.levelStyles = [styles["toc_entry"]]
    story.append(toc)
    story.append(Paragraph("♔", styles["display_ornament"]))
    story.append(PageBreak())

    # p9: PGN
    story.append(Spacer(1, PAGE_H * 0.06))
    story.append(Paragraph("The Game", styles["display_title"]))
    story.append(Paragraph("Sixty-seven moves", styles["display_sub"]))
    story.append(HRFlowable(
        width="30%", thickness=0.6,
        color=colors.HexColor("#888888"),
        spaceAfter=14, hAlign="CENTER",
    ))
    story.append(Paragraph(FULL_PGN, styles["pgn"]))
    story.append(HRFlowable(
        width="20%", thickness=0.4,
        color=colors.HexColor("#888888"),
        spaceBefore=14, spaceAfter=4, hAlign="CENTER",
    ))
    story.append(Paragraph("1–0  ·  White wins", styles["result_line"]))

    # p10: blank verso — pushes Chapter 1 onto p11 (recto / right-hand page).
    story.extend(_blank_page(styles))

    # Chapter 1 starts on next page (p11, odd/recto) via the SECTION PageBreak.

    return story


def build_back_matter(styles):
    story = []
    story.append(PageBreak())
    story.append(Spacer(1, PAGE_H * 0.12))
    story.append(Paragraph("A Note from the Teacher", styles["frontmatter_title"]))
    first = True
    for para in TEACHER_NOTE_PARAS:
        st = styles["note_body_first"] if first else styles["note_body"]
        story.append(Paragraph(para, st))
        first = False
    story.append(Spacer(1, 8))
    story.append(Paragraph("— Joseph Song", styles["note_sig"]))
    return story


def build_story(blocks, styles, boards):
    # Count appearances per character
    total_appearances = {}
    for btype, content in blocks:
        if btype == "CHAR":
            total_appearances[content] = total_appearances.get(content, 0) + 1
    seen = {}

    story = []
    chapter_num = 0
    first_para = True
    just_after_section = False

    i = 0
    while i < len(blocks):
        btype, content = blocks[i]

        if btype == "SECTION":
            chapter_num += 1
            story.append(PageBreak())
            story.append(Spacer(1, 0.20 * inch))
            story.append(Paragraph(f"Chapter {chapter_num}", styles["chapter_title"]))
            story.append(Paragraph(content, styles["section_title"]))
            story.append(HRFlowable(
                width="40%", thickness=0.5,
                color=colors.HexColor("#aaaaaa"),
                spaceAfter=12, hAlign="CENTER",
            ))
            first_para = True
            just_after_section = True

        elif btype == "CHAR":
            name = content
            idx = seen.get(name, 0)
            seen[name] = idx + 1
            total = total_appearances[name]
            lo, hi = CHAR_RANGES[name]
            # Lookahead: fold the first body paragraph into the same KeepTogether
            # so the `— Name —` header never sits alone at the bottom of a page.
            # Skip this fold immediately after a SECTION — at the top of a fresh
            # chapter page there's no orphan risk and folding the paragraph in
            # would push the whole unit (including the chapter heading) too tall
            # to fit, stranding the title on its own page.
            follow = None
            consumed = 0
            if not just_after_section:
                j = i + 1
                if j < len(blocks) and blocks[j][0] == "PARA":
                    follow = Paragraph(format_para(blocks[j][1]), styles["body_first"])
                    consumed = 1
            just_after_section = False
            story.append(board_flowable(
                name, boards, styles, lo, hi, idx, total,
                follow_paragraph=follow,
            ))
            first_para = follow is None
            i += 1 + consumed
            continue

        elif btype == "SEP":
            just_after_section = False
            # If the next block is a CHAR, fold the SEP (and first body paragraph)
            # into that board's KeepTogether. If it's a PARA, fold the SEP +
            # first PARA together. If it's a SECTION, suppress the SEP entirely —
            # the chapter break already signals end-of-section, so a separator
            # before it would only orphan dots at the bottom of the prior page.
            nxt = blocks[i + 1] if i + 1 < len(blocks) else (None, None)
            if nxt[0] == "SECTION":
                i += 1
                continue
            if nxt[0] == "CHAR":
                name = nxt[1]
                idx = seen.get(name, 0)
                seen[name] = idx + 1
                total = total_appearances[name]
                lo, hi = CHAR_RANGES[name]
                follow = None
                consumed = 0
                j = i + 2
                if j < len(blocks) and blocks[j][0] == "PARA":
                    follow = Paragraph(format_para(blocks[j][1]), styles["body_first"])
                    consumed = 1
                story.append(board_flowable(
                    name, boards, styles, lo, hi, idx, total,
                    prepend_sep=True, follow_paragraph=follow,
                ))
                first_para = follow is None
                i += 2 + consumed
                continue
            elif nxt[0] == "PARA":
                story.append(KeepTogether([
                    Spacer(1, 4),
                    Paragraph("· · ·", styles["sep"]),
                    Spacer(1, 4),
                    Paragraph(format_para(nxt[1]), styles["body_first"]),
                ]))
                first_para = False
                i += 2
                continue
            else:
                story.append(Spacer(1, 4))
                story.append(Paragraph("· · ·", styles["sep"]))
                story.append(Spacer(1, 4))
                first_para = True

        elif btype == "PARA":
            just_after_section = False
            style = styles["body_first"] if first_para else styles["body"]
            story.append(Paragraph(format_para(content), style))
            first_para = False

        elif btype == "SONG_V":
            just_after_section = False
            story.append(Paragraph(content, styles["song_line"]))
            first_para = False

        elif btype == "SONG_C":
            just_after_section = False
            story.append(Paragraph(content, styles["song_chorus"]))
            first_para = False

        elif btype == "SONG_BLANK":
            story.append(Spacer(1, 8))

        i += 1

    return story


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Build Chromyre Chronicles PDF.")
    parser.add_argument("--source", default=DEFAULT_SRC_MD,
                        help="Markdown source file (default: censored manuscript)")
    parser.add_argument("--output", default=DEFAULT_OUT_PDF,
                        help="Output PDF path (default: Chromyre_Chronicles_FINAL.pdf)")
    args = parser.parse_args()
    global SRC_MD, OUT_PDF
    SRC_MD = args.source
    OUT_PDF = args.output

    register_fonts()
    styles = make_styles()

    print("Building chess board states...", file=sys.stderr)
    boards = build_board_states(FULL_PGN)
    print(f"  {len(boards)} states (0..{len(boards)-1} half-moves)", file=sys.stderr)

    print("Parsing markdown...", file=sys.stderr)
    blocks = parse_markdown(SRC_MD)
    print(f"  {len(blocks)} blocks", file=sys.stderr)

    story = []
    story.extend(build_front_matter(styles))
    story.extend(build_story(blocks, styles, boards))
    story.extend(build_back_matter(styles))

    print(f"Writing {OUT_PDF}...", file=sys.stderr)
    doc = ChromyreDoc(OUT_PDF)
    doc.multiBuild(story)
    print("Done.", file=sys.stderr)


if __name__ == "__main__":
    main()
