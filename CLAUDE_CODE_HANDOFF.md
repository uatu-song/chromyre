1# Claude Code Handoff — Chromyre Chronicles PDF Builder
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
