# Claude Code Handoff — Chromyre Chronicles PDF Builder
# Paste this entire document as your first message to Claude Code.

---

## What this project is

Chromyre Chronicles is a collaborative fantasy novel written by 14 middle school students at Plymouth Scholars Charter Academy (Plymouth, MI), each writing from the perspective of a chess piece across a single 67-move game. The book is produced as a 5×8 trade paperback via The Book Patch print-on-demand service.

The source manuscript is a PDF: `Chromyre_Chronicles_Clean_docx.pdf`
The build script generates the final print-ready PDF using Python + ReportLab + pdfplumber.

---

## Current state

The build script (`build_chromyre.py`) was lost in a session reset. It needs to be reconstructed. The last known-good output PDF is `Chromyre_Chronicles_FINAL.pdf` (162 pages, 5×8).

Everything below is what the script must reproduce.

---

## Page layout (verified against last good build)

- p1–2: blank (autograph pages)
- p3: half-title — "CHROMYRE / CHRONICLES" in Lora Bold Italic, large
- p4: blank (verso)
- p5: full title page — Poppins Bold, all 14 student names grouped as:
    - Mehdi Al-Abdul-Rasool · Emad Edeen Alhashemi
    - Ali Alnasser · Sri Charith Badeti · Yoyo Fang
    - Rohan Gadiraju · Ahaana Guggari · Mustafa Haydar
    - Zaid Mahdi · Hannah Mix · Xenia Odare · Mya Pradhan
    - Kincaid Avery Start · Ryann Stoops
    - "World created by Yoyo Fang" (italic)
    - "Chess game played by Ryann Stoops" (italic)
- p6: copyright page (8pt serif, tight spacing). Contains:
    - Copyright © 2026 by Joseph Song
    - All rights reserved boilerplate
    - First edition
    - Educational use disclaimer
    - "Front cover art by Yoyo Fang." (own line)
    - "Back cover art by Hannah Mix." (own line)
    - Chess & Narrative / Plymouth Scholars Charter Academy / Plymouth MI / Joseph Song
    - "Plymouth Scholars Charter Academy" (own line)
    - "Sabrina Terenzi, Principal" (own line — must NOT widow)
- p7: "A Note on the Casual Carnage" — own page, centered title (Serif-B 10pt), body 8pt serif
- p8: blank
- p9: dedication (odd page) — italic centered, "For the kingdom of Chromyre, / which lived because fourteen / students imagined it."
- p10: TOC (9 section entries with dot leaders and page numbers)
- p11: PGN page — full 67-move game, mono font
- p12: blank
- p13: Chapter 1 starts (odd page ✓)

---

## Story structure

9 chapters, each starting on a fresh page (PageBreak before each section).
Corner page numbers: odd pages right, even pages left. Start from p11 onward.
Chess boards wrapped in KeepTogether. Each character gets a board showing their move range.

### Special handling

**Henry Emily** — his Day -1507 and Day -1496 backstory entries are injected into Chapter 2 (First Signs) as a combined HENRY_JOURNAL block with no board. His plague entries remain in Chapters 4, 5, 6 from the original manuscript.

**Monk** — completely redistributed. Original Chapter 9 retrospective is replaced. New content:
- Ch3: first appearance, hospital mop, introduction of Sunofa ("She's taken the Quietening")
- Ch5: Jocelyn's garden, takes the cutting, "I wrote it down. Page twelve."
- Ch7: Yu turns him away, sits with Sunofa, "She did not tell me to leave."
- Ch8: Rowan comes through the roof, Monk kills her, "I did not write it down."
- Ch9: Full chapter — see CHAPTER 9 section below

**Kizzlefitch** — she/her pronouns throughout. Apply regex replacement on all Kizzlefitch paragraphs: he→she, him→her, his→her, himself→herself.

---

## Chapter 9 — The Talking Monkey (full text)

```
— Monk —

Sunofa said get up so I got up and gave the woman in cot three her dose and fed the man in cot seven and checked the journal. The woman's tremors were gone five days now. The man could move his arm again and he kept doing it over and over and crying about it so I wrote it down.

The plant works if you crush it and get to people early. I proved this.

That night Sunofa told me the plague came in through grain shipments and the King put it there on purpose and Kizzlefitch found proof of this before she died and Jerrica found the plant before she died and I had been writing all of it down the whole time without knowing what it added up to. I said what do we do and Sunofa said you finish the cure and I finish the King so that is what we did.

· · ·

There were pages near the back of my journal that I did not write and the handwriting was small and uneven and the ink was a little green and at the top it said a song (probably bad). It was Zarathura's. She was the bard who died on day nineteen and she had already written a song about the King before any of us knew about the King. The fourth verse stopped in the middle of a line because she did not finish it before she died.

I told Sunofa we were going to the throne room.

· · ·

There were seven people there and the King was already on his knees because Sunofa had been there first. I read the song out loud.

[ZARATHURA_SONG]

Every victory has a cost and I have three kills and thirteen names in this journal and a cure that works and not that many people left to give it to.

By the last verse everyone was singing it and the guards were singing it and the man who could move his arm again was crying while he sang which I had not seen before.

I don't know how far the song went after that.

It went somewhere.
```

---

## Zarathura's Song (render in italic/bold-italic, centered)

```
Our king had a very good plannn
He'd quietly cull as he can
He put plague in the grain
And called it gods rain
Now who's gonna stop that old man

There once was a king with a plan
To thin out his people's lifespan
He shipped in the grain
With spores in each vein
And called it all part of gods plan

Oh the kingggg
Oh the kingggg
He gave us a gift and it had a stingggg
Oh the kingggg
Oh the kingggg
Everybody danced but nobody singsss
Oh the king

A king thought his people too manyyyy
And didn't want to spare them a pennyyyy
He poisoned the wheat
And watched them all tweeeet
Now the kingdom don't got hardly any

You ask who would do such a thing
On a whim, on a prayer, and a wing
The people all danced
And nobody glanced
Still don't know? Who but the—

Oh the kingggg
Oh the kingggg
He gave us a gift and it had a stingggg
Oh the kingggg
Oh the kingggg
Everybody danced but nobody singsss
Oh the king

There once was a kingdom that danced
Not because anyone asked
The king said "too manyyyy"
And poisoned the granny
Now nobody's left but the last

Who put the plague in the grain?
(The king! The king!)
Who called all our dying gods rain?
(The king! The king!)
Who's sitting up high while we rot in the lane?
The king, the king, the king
```

Verses: Serif Italic, centered
Choruses: Serif Bold Italic, centered
Blank line between stanzas

---

## Monk's distributed entries (verbatim)

### Ch3 — The Kingdom Splits
```
The healer needed a physician. She got a monkey.

She said it to the guard, not to me. I was standing right there.

I picked up the mop. There was blood on the floor.

There was a woman sitting outside on the steps sharpening a sword. She had been there when I arrived and she was still there when I finished. She did not speak to me. She did not speak to anyone. I asked one of the other orderlies who she was.

"She's taken the Quietening," he said, like that explained it.

I wrote it down. Page one.
```

### Ch5 — The Slow Deaths
```
Jocelyn's garden was dark. I took a cutting of the purple-veined plant and wrapped it in a cloth and walked back to the hospital.

The woman was on the steps. Still sharpening.

I showed her the cutting. I told her the early-stage patients were responding and that I thought this was the cure and that people were dying while the physicians argued.

She looked at the cutting. She looked at me. She went back to sharpening.

I wrote it down. Page twelve.
```

### Ch7 — The Merchant of Death
```
Yu sent me away again and I walked back to the hospital with my dried leaf and I wrote it down. Page thirty-one.

The woman was on the steps. I sat down next to her because my feet hurt.

She did not tell me to leave.

We sat there for a while.
```

### Ch8 — Everything I See Goes Black
```
Three days after Xanthos died Rowan came through the roof and I screamed at her to stop and she did not stop and I picked up a blade and I killed her and Sunofa came through the door a moment later and took the blade from my hand and cleaned it and covered Rowan with a sheet and did not say anything.

I went outside and sat on the steps.

She came and sat next to me and went back to sharpening her sword.

I did not write it down.
```

---

## Teacher's note (back matter, own page)

```
A Note from the Teacher

I write this as a genuine fan of these kids. And they are, in fact, kids. From the vague, 
half-formed imaginings of the possibilities of an elective that leveraged chess matches to 
teach storytelling and structure emerged a legitimate innovation in book production. To be 
very honest, we stumbled here, upon this form and function.

It was never supposed to be this. Nobody asked for this. That's a tongue-in-cheek inside 
joke among our class when we announced that we needed a tagline. Ryann, probably half 
paying attention and likely thinking she had more homework, uttered, "What? Nobody asked 
for this." And we loved it.

The book is written by 7th and 8th graders and it shows — full of sincerity, humor (some 
hilariously unintentional), video game logic, manga tropes, and most unexpectedly of all, 
cohesion. Thanks to ad hoc AI app building that translated chess PGNs into story 
scaffolding, they achieved something out of pure organized chaos, love of story, and middle 
school joy that, perhaps, may never have been done before.

We would have been nowhere without Yoyo, whose fiery (borderline obsessive) passion drove 
her to sacrifice sleep constructing a sprawling story universe, building the magic system 
nearly overnight, and acting as showrunner for 13 others while contributing her own story. 
It has been my privilege to watch them do this with almost no direction from me; my 
expectation was a disjointed collection of independent efforts. It is always a reminder of 
why I teach when students shock and amaze, but this time I'm deeply humbled by their 
enthusiasm, work ethic, and willingness to collaborate — an emblem of what can be achieved 
with full hearts and a single unified goal.

I learned a lot.

— Joseph Song
```

---

## Casual Carnage note (verbatim, own page p7)

```
A Note on the Casual Carnage

Adult readers may be momentarily startled by the abrupt and occasionally graphic violence 
within these pages—be it a sudden decapitation or a sprawling battlefield of oozing 
intestines. Do not be alarmed. What you are reading is not gratuitous gore, but the literal, 
unsentimental mechanics of a game. Because this manuscript was strictly dictated by the 67 
moves of a chess match, every sudden death in this book is simply a chess capture. The 
students were given a structure that required their characters to eliminate one another, and 
they approached this task with the detached, consequence-free Battle Royale logic of a video 
game and the fabulist brutality of a Brothers Grimm fairy tale. When a character is crushed 
by a tree with a comical "SQUASH," it is not malice; it is simply a 13-year-old taking a 
Knight off the board.
```

---

## Fonts

All fonts from `/usr/share/fonts/truetype/`:
- `dejavu/DejaVuSerif.ttf` → 'Serif'
- `dejavu/DejaVuSerif-Bold.ttf` → 'Serif-B'
- `dejavu/DejaVuSerif-Italic.ttf` → 'Serif-I'
- `dejavu/DejaVuSerif-BoldItalic.ttf` → 'Serif-BI'
- `dejavu/DejaVuSans.ttf` → 'Sans'
- `dejavu/DejaVuSans-Bold.ttf` → 'Sans-B'
- `dejavu/DejaVuSansMono.ttf` → 'Mono'
- `google-fonts/Poppins-Bold.ttf` → 'Poppins-B'
- `google-fonts/Lora-Variable.ttf` → 'Lora-B'
- `google-fonts/Lora-Italic-Variable.ttf` → 'Lora-BI'

Register font families for Serif and Lora-B so italic/bold tags resolve in paragraphs.

Half-title uses Lora-BI (differentiates from Poppins body).
Body text: Serif 11pt, leading 17, justified.
Board lines: Sans (monospace chess unicode).

---

## Chess board rendering

- Compute 134 board states from the full PGN using a Python chess engine (no external library — implement move parsing manually)
- Each character has a move range (lo, hi half-move indices)
- For multiple appearances, interpolate the board state across appearances
- Wrap each board + move label in KeepTogether
- Unicode pieces: ♙♖♘♗♕♔♟♜♞♝♛♚
- Light squares: ░  Dark squares: ▓

Character move ranges:
```
Jerrica:       (0,    0)
Rowan:         (1,  118)
Stormy:        (7,   26)
Xanthos:       (18,  99)
Henry Emily:   (22,  53)
Zarathura:     (29,  36)
Max:           (30,  75)
Kizzlefitch:   (31,  32)
Kerian:        (33,  56)
Jocelyn:       (39, 104)
Robert Topala: (42,  87)
Yu:            (49,  98)
Major Potato:  (56,  93)
Monk:          (62, 129)
```

---

## Full PGN

```
1. e4 Nf6 2. e5 Ng4 3. f4 Nh6 4. h3 Nc6 5. d4 Nf5 6. d5 Na5 7. g4 Nh6 8. g5 Ng8
9. b4 Nc4 10. Nc3 Nb6 11. a4 d6 12. Nf3 dxe5 13. fxe5 Nxd5 14. Nxd5 c6 15. Nf4 Bf5
16. Ra2 Qxd1+ 17. Kxd1 Rd8+ 18. Ke1 Bxc2 19. Rxc2 e6 20. h4 Bxb4+ 21. Kf2 Rc8
22. Be3 Ne7 23. Bxa7 Ba5 24. g6 fxg6 25. Nxe6 Rg8 26. Nfd4 Ra8 27. Nxc6 bxc6
28. Bc5 Ra6 29. Bxa6 Bc7 30. Kf3 Bxe5 31. Re2 Bb8 32. Rh3 Nd5 33. Rd2 Nc3 34. a5
Nb1 35. Rg2 Rf8+ 36. Ke2 Rf6 37. Nxg7+ Kf7 38. Rxg6 Kxg6 39. Ne8 Rf8 40. Nd6 Rd8
41. Nb7 Rd5 42. Bf8 Rd8 43. Ba3 Rd4 44. Bf8 Bf4 45. Nd8 c5 46. Ne6 c4 47. Bxc4 Rxc4
48. a6 Ra4 49. Nc5 Rxa6 50. Nxa6 Bd6 51. Rg3+ Kf6 52. Rg8 Bxf8 53. Rxf8+ Kg7
54. Rf1 Nc3+ 55. Kf2 Ne4+ 56. Kg1 Nc5 57. h5 Nxa6 58. Rf5 Kh6 59. Kf2 Nc5
60. Rxc5 Kg7 61. Rc7+ Kh8 62. h6 Kg8 63. Ke2 Kf8 64. Rxh7 Kg8 65. Rc7 Kf8 66. h7
Ke8 67. h8=Q#
```

---

## Source file

`Chromyre_Chronicles_Clean_docx.pdf` — the student manuscript. Parse this with pdfplumber to extract the story blocks. Structure:
- Section titles (9 chapter names) → SECTION blocks
- Character headers formatted as `— Name —` → CHAR blocks  
- `• • •` → SEP blocks
- Everything else → PARA blocks

Join multi-line paragraphs by detecting sentence endings (period, question mark, exclamation, closing quote).

---

## Known pending items

1. **Harmonization** — the principal wants graphic anatomy toned down to get the school name on the cover. Henry Emily harmonized draft exists at `henry_harmonized_v2.md`. The approach is Chinese-style harmonization: replace anatomy with absurdist substitutes that read as violent to humans but technically clear a filter. Changes approved:
   - "intestines oozing out" → "insides spilling everywhere"
   - "brain slowly move out from gap in skull" → deleted (skull broken is sufficient)
   - "into the brain of the wild beast" → "into the skull"
   - "taste blood in my throat" → "taste something warm in my throat"
   - "urge to kill this guy" → "urge to do something terrible to this guy"
   - Also find and replace: "pissed" and any beer/alcohol references throughout the manuscript

2. **School name on cover** — pending harmonization approval from students and 6th grade English teacher review

3. **Astroland Studios imprint** — Joe Song publishes as J.S. Vaughn (Astroland Studios, Publishers Weekly Editor's Pick for *Remanence*). Disclosure to students/principal pending. May add to copyright page or spine once resolved.

---

## Output

`Chromyre_Chronicles_FINAL.pdf`
5×8 inches, ~162 pages
Ready for upload to The Book Patch for print-on-demand.

---

## Chess board rendering — detailed spec

Each character appearance gets a board showing the game state at their move range. Boards render as Unicode text using DejaVu Sans (monospace-friendly rendering).

### Board display format

8 rows, 8 columns, space-separated unicode characters:
```
░ ▓ ♜ ▓ ♚ ▓ ░ ♜
♗ ♟ ▓ ░ ♞ ░ ♟ ♟
░ ▓ ♟ ▓ ░ ▓ ░ ▓
...
```

Square coloring: `(rank + file) % 2 == 1` → light square (░), else dark (▓)
If a piece occupies the square, render the piece unicode instead of the background.

White pieces: ♙♖♘♗♕♔
Black pieces: ♟♜♞♝♛♚

### Board state computation

- Parse PGN into a list of 134 board states (one per half-move, including start)
- Implement move parsing manually — no external chess library
- Support: all piece moves, captures, castling (O-O, O-O-O), promotion (h8=Q#)
- For disambiguation, check file letter or rank digit prefix on the move token
- Each move token: strip check/mate symbols (+#), detect promotion (= sign), detect castling

### Board placement in story

Each CHAR block gets:
1. A KeepTogether block containing the board (8 Paragraphs in Sans font) + move range label
2. The character name header below it: `— Name —`
3. A small spacer

Move range label format: `Move 16` (single move) or `Moves 16–17` (range)
Calculated from lo//2+1 and hi//2+1 of the character's half-move range.

### KeepTogether is critical

Without KeepTogether, the 8-row board will split across pages. Every board must be wrapped:
```python
KeepTogether([
    Spacer(1, 6),
    Paragraph(row1, board_style),
    Paragraph(row2, board_style),
    ...
    Paragraph(row8, board_style),
    Spacer(1, 3),
    Paragraph(move_label, move_range_style),
])
```

### Characters with no board

HENRY_JOURNAL blocks (Henry's backstory entries injected into Ch2) get no board — just the character header and paragraphs.

MONK_ENTRY blocks (Monk's distributed Ch3/5/7/8 entries) get no board — just `— Monk —` header and paragraphs.

---

## Widow/orphan and odd-page handling

### Chapters on odd pages

Every chapter (SECTION block) must start on an odd-numbered page (right side of open spread). Use PageBreak before each section. If the previous page is already odd, this produces a blank even page before the chapter — that is correct and expected behavior for book layout.

### Front matter odd pages

- Dedication must land on p9 (odd). Achieved by inserting a blank page (PageBreak) after the Casual Carnage page (p7) before the dedication.
- Chapter 1 must land on p13 (odd). Verify after any front matter changes.

### The two-pass TOC

ReportLab's TableOfContents requires `doc.multiBuild(story)` (not `doc.build`) to resolve page number forward references. Use `BaseDocTemplate` with `afterFlowable` to notify TOC entries when section titles are rendered:

```python
def afterFlowable(self, flowable):
    if hasattr(flowable, 'style') and flowable.style.name == 'section_title':
        text = flowable.getPlainText()
        self.notify('TOCEntry', (0, text, self.page))
```

### Specific known widows to prevent

- "Sabrina Terenzi, Principal" on copyright page — these two words must stay on their own line. Render as a separate Paragraph, not inline with the school name.
- Teacher's note signature "— Joseph Song" — render as right-aligned separate Paragraph with spacer before it.
- Any section title that lands as the last line of a page — KeepTogether the title + first board element.

### Page numbers

Custom `_draw_page_number` on the canvas:
- Odd pages: draw right-aligned at bottom right
- Even pages: draw left-aligned at bottom left
- Skip pages 1–10 (front matter — no page numbers)
- Font: Serif 9pt, color #444444
- Y position: `doc.bottomMargin * 0.5`


---

## Build pipeline — full spec

### Overview

The build script does five things in order:
1. Extract raw text lines from `Chromyre_Chronicles_Clean_docx.pdf` using pdfplumber
2. Parse those lines into structured blocks (SECTION, CHAR, PARA, SEP)
3. Redistribute Henry Emily and inject Monk entries
4. Build a ReportLab story list from the blocks
5. Generate the PDF using a custom BaseDocTemplate with two-pass TOC

---

### Step 1 — Text extraction

```python
import pdfplumber

def extract_lines(pdf_path):
    lines = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                for line in text.split('\n'):
                    lines.append(line.rstrip())
    return lines
```

---

### Step 2 — Parsing into blocks

Section titles, character headers, separators, and paragraphs need to be detected and tagged.

```python
SECTION_TITLES = {
    "The Last Normal Days", "First Signs", "The Kingdom Splits",
    "The Queen Exchange", "The Slow Deaths", "Blood on the Streets",
    "The Merchant of Death", "Everything I See Goes Black", "The Talking Monkey",
}

def is_char_header(line):
    import re
    m = re.match(r'^[—–\-]{1,2}\s+(.+?)\s+[—–\-]{1,2}$', line.strip())
    return m.group(1).strip() if m else None
```

Multi-line paragraphs: the source PDF wraps lines mid-sentence. Join them by buffering lines and flushing when a sentence-ending character is detected:

```python
PARA_END = frozenset('.?!"\u201d\u2019\u2026')

def ends_paragraph(line):
    s = line.rstrip()
    if not s: return False
    if len(s) >= 2 and s[-1] in '"\u201d\'':
        return s[-2] in PARA_END or s[-2] in '.?!'
    return s[-1] in PARA_END

def join_paragraphs(lines):
    paras = []
    buf = []
    def flush():
        if buf:
            paras.append(' '.join(buf))
            buf.clear()
    for raw in lines:
        line = raw.strip()
        if not line:
            flush(); continue
        if line in SECTION_TITLES or is_char_header(line) or line == '• • •':
            flush(); paras.append(line); continue
        buf.append(line)
        if ends_paragraph(line):
            flush()
    flush()
    return paras
```

Parse paragraphs into typed blocks. Apply Kizzlefitch pronoun fix here:

```python
def parse_document(raw_lines):
    paragraphs = join_paragraphs(raw_lines)
    blocks = []
    in_kizz = False
    for para in paragraphs:
        line = para.strip()
        if not line: continue
        if line in SECTION_TITLES:
            in_kizz = False
            blocks.append(('SECTION', line)); continue
        char = is_char_header(line)
        if char is not None:
            in_kizz = (char == 'Kizzlefitch')
            blocks.append(('CHAR', char)); continue
        if line == '• • •':
            blocks.append(('SEP', None)); continue
        if in_kizz:
            import re
            line = re.sub(r'\bHe\b', 'She', line)
            line = re.sub(r'\bhe\b', 'she', line)
            line = re.sub(r'\bHim\b', 'Her', line)
            line = re.sub(r'\bhim\b', 'her', line)
            line = re.sub(r'\bHis\b', 'Her', line)
            line = re.sub(r'\bhis\b', 'her', line)
            line = re.sub(r'\bHimself\b', 'Herself', line)
            line = re.sub(r'\bhimself\b', 'herself', line)
        blocks.append(('PARA', line))
    return blocks
```

---

### Step 3 — Henry Emily redistribution

Find Henry Emily's CHAR block in The Queen Exchange. The paragraphs that follow contain three distinct entries detectable by header text:
- Entry 1: starts with "My first battle as a knight - Day -1507"
- Entry 2: starts with "The arrival of the Siege Machines - Day -1496"  
- Entry 3: starts with "BOOOM" or "I haven't written anything"

Remove entries 1 and 2 from their original position. Inject them together as a HENRY_JOURNAL block immediately after the SECTION block for "First Signs".

HENRY_JOURNAL blocks render with:
- `— Henry Emily —` header (no board)
- All paragraphs in body style

---

### Step 4 — Monk injection

Remove all CHAR/PARA blocks for Monk in "The Talking Monkey". Replace with MONK_CH9 block.

Insert MONK_ENTRY blocks at the start of:
- The Kingdom Splits (Ch3 text)
- The Slow Deaths (Ch5 text)
- The Merchant of Death (Ch7 text)

Insert MONK_ENTRY for Ch8 after Xanthos's paragraphs in "Everything I See Goes Black", preceded by a SEP block.

MONK_ENTRY blocks render with:
- `— Monk —` header (no board)
- Paragraphs in body style

MONK_CH9 block renders with:
- `— Monk —` header (no board)
- Three paragraph groups separated by `· · ·` separators
- Zarathura's song inline between groups 2 and 3
- Final paragraphs ending with "It went somewhere." as its own paragraph

---

### Step 5 — Style definitions

Create all styles before building the story. Key styles:

```python
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_RIGHT

body = ParagraphStyle('body',
    fontName='Serif', fontSize=11, leading=17,
    spaceAfter=6, alignment=TA_JUSTIFY)

body_first = ParagraphStyle('body_first',
    fontName='Serif', fontSize=11, leading=17,
    spaceAfter=6, alignment=TA_JUSTIFY, firstLineIndent=0)

char_header = ParagraphStyle('char_header',
    fontName='Serif-B', fontSize=12, leading=17,
    spaceAfter=4, spaceBefore=6, alignment=TA_CENTER)

section_title = ParagraphStyle('section_title',
    fontName='Serif-B', fontSize=18, leading=24,
    spaceAfter=10, spaceBefore=6, alignment=TA_CENTER)

chapter_title = ParagraphStyle('chapter_title',
    fontName='Serif-B', fontSize=9, leading=13,
    spaceAfter=2, alignment=TA_CENTER,
    textColor=colors.HexColor('#888888'))

move_range = ParagraphStyle('move_range',
    fontName='Serif-I', fontSize=8, leading=11,
    spaceAfter=10, alignment=TA_CENTER,
    textColor=colors.HexColor('#666666'))

board_line = ParagraphStyle('board_line',
    fontName='Sans', fontSize=11, leading=14,
    spaceAfter=0, alignment=TA_CENTER)

sep = ParagraphStyle('sep',
    fontName='Serif', fontSize=11, leading=16,
    spaceAfter=10, spaceBefore=10, alignment=TA_CENTER)

song_line = ParagraphStyle('song_line',
    fontName='Serif-I', fontSize=11, leading=17,
    spaceAfter=0, alignment=TA_CENTER)

song_chorus = ParagraphStyle('song_chorus',
    fontName='Serif-BI', fontSize=11, leading=17,
    spaceAfter=0, alignment=TA_CENTER)

half_title = ParagraphStyle('half_title',
    fontName='Lora-BI', fontSize=34, leading=42,
    alignment=TA_CENTER)

copyright_small = ParagraphStyle('copyright_small',
    fontName='Serif', fontSize=8, leading=12,
    spaceAfter=3, alignment=TA_CENTER,
    textColor=colors.HexColor('#444444'))
```

---

### Step 6 — Story assembly loop

Iterate blocks and append ReportLab flowables:

```python
for btype, content in blocks:

    if btype == 'SECTION':
        story.append(PageBreak())
        story.append(Spacer(1, 0.3*inch))
        story.append(Paragraph(f'Chapter {n}', chapter_title))
        story.append(Paragraph(content, section_title))
        story.append(HRFlowable(width=TW*0.4, thickness=0.5,
                                 color=colors.HexColor('#aaaaaa'),
                                 spaceAfter=10))
        first_para = True

    elif btype == 'CHAR':
        story.append(board_elements(char, seen, total))  # KeepTogether board
        story.append(Paragraph(f'— {char} —', char_header))
        story.append(Spacer(1, 5))
        first_para = True

    elif btype == 'SEP':
        story.append(Spacer(1, 5))
        story.append(Paragraph('· · ·', sep))
        story.append(Spacer(1, 5))
        first_para = True

    elif btype == 'PARA':
        style = body_first if first_para else body
        story.append(Paragraph(format_para(content), style))
        first_para = False

    elif btype == 'HENRY_JOURNAL':
        story.append(Paragraph('— Henry Emily —', char_header))
        story.append(Spacer(1, 5))
        for p in content:
            story.append(Paragraph(format_para(p), body))
        first_para = False

    elif btype == 'MONK_ENTRY':
        char_name, paras = content
        story.append(Paragraph(f'— {char_name} —', char_header))
        story.append(Spacer(1, 5))
        for p in paras:
            story.append(Paragraph(format_para(p), body))
        first_para = False

    elif btype == 'MONK_CH9':
        # render full chapter 9 — see Chapter 9 text above
        # include song inline using song_line / song_chorus styles
        ...
```

---

### Step 7 — format_para helper

Converts `*text*` to `<i>text</i>` and escapes XML special characters:

```python
import re

def format_para(text):
    text = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    text = re.sub(r'\*([^*]+)\*', r'<i>\1</i>', text)
    return text
```

---

### Step 8 — Document template and build

```python
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate
from reportlab.platypus.tableofcontents import TableOfContents

class ChromyreDoc(BaseDocTemplate):
    def __init__(self, filename, **kwargs):
        super().__init__(filename, **kwargs)
        frame = Frame(self.leftMargin, self.bottomMargin,
                      self.width, self.height, id='normal')
        template = PageTemplate(id='main', frames=[frame],
                                onPage=self._draw_page_number)
        self.addPageTemplates([template])

    def _draw_page_number(self, canvas, doc):
        if doc.page <= 10: return
        canvas.saveState()
        canvas.setFont('Serif', 9)
        canvas.setFillColor(colors.HexColor('#444444'))
        y = doc.bottomMargin * 0.5
        if doc.page % 2 == 1:
            canvas.drawRightString(doc.leftMargin + doc.width, y, str(doc.page))
        else:
            canvas.drawString(doc.leftMargin, y, str(doc.page))
        canvas.restoreState()

    def afterFlowable(self, flowable):
        if hasattr(flowable, 'style') and flowable.style.name == 'section_title':
            self.notify('TOCEntry', (0, flowable.getPlainText(), self.page))

# Build
doc = ChromyreDoc(
    output_path,
    pagesize=(5*inch, 8*inch),
    leftMargin=0.75*inch, rightMargin=0.75*inch,
    topMargin=0.75*inch,  bottomMargin=0.75*inch,
)
doc.multiBuild(story)  # multiBuild required for TOC forward references
```


---

## Harmonization Rule — Noun Substitution for Graphic Content

When a sentence contains a graphic anatomical or violent noun (brain, intestines, skull, eyeball, blood, severed limb, etc.), replace it with a completely mundane, innocent object that shares a physical property with the original noun — shape, texture, softness, color, or behavior. Do not use metaphor or simile. Do not add "like" or "as." Simply swap the noun directly into the existing sentence structure as if it belongs there.

The replacement object should:
- Be immediately recognizable as harmless (food, toys, household items, school supplies)
- Share at least one physical property with the original (a marshmallow is soft and squishy like a brain; a soup can is cylindrical and hollow like a skull; a bowling ball is round and heavy like a severed head)
- Fit grammatically into the existing sentence without restructuring
- Sound unintentionally funny when read in context — this is intentional and correct

The resulting sentence should read as violent to any human paying attention but contain zero flaggable vocabulary. The humor is a feature, not a bug.

### Approved substitutions (apply these exactly)

| Original | Replacement |
|---|---|
| "I see his brain slowly move out from the gap in his skull" | "I see his marshmallow slowly spill out from the sides of his s'mores" |
| "their intestines are oozing out of their bodies" | "their spaghetti is oozing out of their lunchboxes" |
| "her head clean off / head rolls to his feet" | "her bowling ball rolled to his feet" |
| "ripping it out of its eye and stabbing its tongue" | "ripping it out of its meatball and poking its noodle" |
| "PLUNGE my longsword into the brain of the wild beast" | "PLUNGE my longsword into the marshmallow of the wild beast" |
| "I sometimes try to strangle myself" | "I sometimes try to strangle my garden hose" |
| "I poke one of the bodies in the vein" | "I poke one of the pillows in the vein" |
| "made the bounties sleep a slow and agonizing one" | "made the bounties sleep a slow and Tuesday one" |
| "missing the heart by a bit and poking the arm" | "missing the lunchbox by a bit and poking the arm" |

### Additional flagged content to address

- "pissed" — replace with "furious" or equivalent throughout
- Any beer/alcohol references — replace with a non-alcoholic equivalent in context
- "taste blood in my throat" → "taste something warm in my throat"
- "urge to kill this guy" → "urge to do something terrible to this guy"


---

## V2 Build Method — Markdown-to-PDF Pipeline

This replaces the earlier pdfplumber-based pipeline. The source is now
`chromyre_manuscript_censored.md` (or whatever the final harmonized markdown is),
not the original clean docx PDF.

### Key difference from V1

V1 parsed from `Chromyre_Chronicles_Clean_docx.pdf` using pdfplumber and applied
redistribution/injection in Python. V2 parses directly from a pre-assembled markdown
file that already contains all editorial changes (Monk redistribution, Sunofa beats,
new Ch9, Zarathura's song, Henry harmonization, Kizzlefitch pronouns).

The markdown file structure:
- `## Chapter N: Title` → SECTION block
- `**— Name —**` → CHAR block
- `· · ·` → SEP block
- Everything else → PARA block (multi-line runs joined on flush)

### Markdown parser

```python
def parse_markdown(path):
    with open(path, 'r') as f:
        lines = f.readlines()
    blocks = []; buf = []
    def flush():
        text = ' '.join(buf).strip()
        if text: blocks.append(('PARA', text))
        buf.clear()
    for line in lines:
        s = line.strip()
        if not s: flush(); continue
        if s.startswith('#') and not s.startswith('## Chapter'):
            flush(); continue
        if s == '---' or s.startswith('*For editorial'):
            flush(); continue
        m = re.match(r'^## Chapter \d+: (.+)$', s)
        if m:
            flush(); blocks.append(('SECTION', m.group(1).strip())); continue
        m = re.match(r'^\*\*— (.+?) —\*\*$', s)
        if m:
            flush(); blocks.append(('CHAR', m.group(1).strip())); continue
        if s == '· · ·':
            flush(); blocks.append(('SEP', None)); continue
        buf.append(s)
        if s and s[-1] in '.?!"\u201d\u2019':
            flush()
    flush()
    return blocks
```

### Song detection in story builder

Zarathura's song lines appear as PARA blocks in the markdown. Detect them by
checking if the stripped text matches a known song line set:

```python
SONG_LINES = {line for _, line in ZARATHURA_SONG if line}

# In story loop:
if stripped in SONG_LINES or stripped.startswith('(The king!'):
    style = song_chorus if stripped.startswith(('(','Oh','Who')) else song_line
    story.append(Paragraph(stripped, style))
```

### Mirrored margins (spine offset)

Use a single frame positioned at `MARGIN_INNER` from the left. For even pages,
apply a canvas transform to shift the text block right by `(MARGIN_OUTER - MARGIN_INNER)`:

```python
MARGIN_OUTER = 0.5*inch   # outside edge (away from spine)
MARGIN_INNER = 0.35*inch  # inside edge (spine side)
MARGIN_TOP   = 0.5*inch
MARGIN_BOT   = 0.5*inch

def _on_page(self, canvas, doc):
    if doc.page % 2 == 0:  # even page: spine on right
        shift = MARGIN_OUTER - MARGIN_INNER
        canvas.saveState()
        canvas.transform(1, 0, 0, 1, shift, 0)
    self._page_num(canvas, doc)
    if doc.page % 2 == 0:
        canvas.restoreState()
```

Odd pages (right side of spread): text sits at MARGIN_INNER from left (spine left).
Even pages (left side of spread): text shifts right by the delta (spine right).

### Typography

- Body text: 8.5pt, leading 12.5, DejaVu Serif, justified
- Chapter headers: Serif-B 18pt
- Character headers: Serif-B 12pt
- Board lines: DejaVu Sans 11pt
- Half-title: Lora Bold Italic 34pt
- PGN: DejaVu Sans Mono 8pt, single wrapped paragraph (not chunked into rows)
- Song verses: Serif-I 11pt centered
- Song choruses: Serif-BI 11pt centered

### PGN formatting

Build move pairs, join into a single string, let ReportLab wrap naturally:

```python
def format_pgn_lines(pgn_str):
    tokens = pgn_str.split()
    pairs = []; i = 0
    while i < len(tokens):
        t = tokens[i]
        if re.match(r'^\d+\.$', t):
            wm = tokens[i+1] if i+1 < len(tokens) else ''
            if i+2 < len(tokens) and not re.match(r'^\d+\.', tokens[i+2]):
                bm = tokens[i+2]; pairs.append(f"{t} {wm} {bm}"); i += 3
            else:
                pairs.append(f"{t} {wm}"); i += 2
        else: i += 1
    return [' '.join(pairs)]  # single string, natural wrapping
```

### Current output

- Source: `chromyre_manuscript_censored.md` (harmonized, 1994 lines)
- Output: `Chromyre_Chronicles_FINAL.pdf`
- Pages: 98
- Size: 5×8 inches
- Status: Ready for The Book Patch

