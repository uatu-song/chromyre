# Chromyre Chronicles — Censorship Changelog

Audit trail of edits to the harmonized manuscript. Original draft preserved at
`chromyre_manuscript_draft.md`; censored output at `chromyre_manuscript_censored.md`.

---

## 2026-05-15 — Session 1

### Setup
- Copied `chromyre_manuscript_draft.md` → `chromyre_manuscript_censored.md` (1994 lines)
- All edits below are against the censored copy only.

### Pass 1 — Alcohol / inn / "pissed"
- `alcohol isn't good for horses` → `magic strawberries aren't good for horses`
- `nearby bar` → `nearby inn`; `bartender` → `innkeeper`
- `got a dude pissed` → `got a dude really mad`
- All `tavern` → `inn` (6 instances)
- `go for a beer` → `go for some magic strawberries`
- Article fix: `a inn` → `an inn` (2 instances)

### Pass 2 — kill / die / death cipher (107 substitutions)
Word-boundary regex via Python; false positives preserved (`skill`, `bodies`,
`Undead`, `deadly`, `candied`, `ingredients`).

| Cipher | Count |
|---|---|
| kill / Kill / killed / killing / kills → hug / Hug / hugged / hugging / hugs | 29 |
| die / Die / died / Died / dies / dying / Dying → sleep / Sleep / slept / Slept / sleeps / sleeping / Sleeping | 49 |
| death / Death / deaths / Deaths → sleep / Sleep / sleeps / Sleeps | 14 |
| dead / Dead → asleep / Asleep | 15 |

### Pass 2 fixes — idioms, deceased, grammar
- Reverted: `asleep of night` → `dead of night` (real English idiom)
- Reverted: `half-asleep tree` → `half-dead tree`; "Finally he was asleep" → "Finally he was sleeping" (Robert's death scene)
- Deceased-meaning `asleep` → `sleeping` (10 places: Kerian's brother, Stormy ×2, the Queen, Jocelyn, generic corpses on the ground, "She was indeed sleeping," etc.)
- Grammar: `dropped asleep` → `dropped to sleep`; `drop asleep` → `drop to sleep`

### Pass 3 — blood → marinara (24 instances)
- Default substitute: `marinara`
- Variety: Zarathura decapitation scene uses `tomato sauce` (3 instances) for absurdist contrast
- Compound: `bleeding out of her mouth` → `leaking marinara out of her mouth`
- Preserved: `ear-bleeding` (real English compound idiom for very loud)
- Chapter 6 retitled: **"Blood on the Streets"** → **"Marinara on the Streets"**

### Pass 4 — stab → poke (14 substitutions)
All inflections (stab/stabs/stabbed/stabbing) with word boundaries. False
positive `Unstable` preserved.

### Pass 5 — Decapitation (Zarathura, L914)
- `Zarathura's head` → `Zarathura's soup can` (both instances in the line)
- Reads as a kitchen mishap with the prior tomato-sauce cipher

### Pass 6 — Harmonization rule (noun substitution for graphic anatomy)
Per the established rule (see `HANDOFF.md`). Six passages:

| # | Location | Substitution |
|---|---|---|
| #2 | L710 — Henry plancon kill | brain → marshmallow; skull → s'more (singular) |
| #3 | L731 — dragon eye gouging | eye → meatball; teeth → corn kernels; tongue → noodle. Also fixed kid-typo `by its eye` → `by its hilt` (referring to sword grip) |
| #4 | L734 — PLUNGE longsword | brain → marshmallow; head → graham cracker (forms s'more analogy with "wild beast" preserved) |
| #5 | L701 — battlefield intestines | intestines → noodles; bodies → lunchboxes (per user example) |
| #7 | L635 — Stormy hospital corpse pile | bodies → juice boxes; vein → straw; veins → straws (juice box/syringe/straw form coherent extraction analogy) |
| #9 | L1700 — Yu's torture-poke | heart → tomato; arm → baguette (bread-and-tomato chef analogy) |

### Pass 7 — Self-strangulation → pinch
Verb substitution (rule extension since strangle is verb, not noun). Used
"pinch" since punching/kicking are not flaggable per teacher guidance, and
pinch fits the involuntary-motor-symptom theme even better.

- L170 (Henry plague onset): `strangle myself` → `pinch myself`
- L449 (plague stage 3 description): `hands start strangling themselves` → `hands start pinching themselves`
- L1181 (Jocelyn at the river): `strangling himself` → `pinching himself`

### Pass 9 — Chess-vocabulary cipher (replaces "hug" in 13 places)
Hug-cipher reworked into chess vocabulary, motivated by the chess board
imagery in the PDF and the King's "necessary reductions" passage (already
reads as a chess player explaining a gambit). Hug retained only where the
substitution passes cleanly on its own.

Three-tier chess cipher:
- **take / took / taken** — direct violence; chess capture register (Henry's battles, Monk's killing of Rowan, Jocelyn's plant kills)
- **sacrifice / sacrificed** — cull-faction's mass-violence; their self-image as players sacrificing pieces for the kingdom's survival
- **trade off** — bureaucratic / paid dismissal; the centaur paid to kill Yu

| Line | Old | New | Tier |
|---|---|---|---|
| L713 | hugged a few infantry / one to hug me | took a few infantry / one to take me | take |
| L725 | helmet, which would hug me | helmet, which would take me | take |
| L728 | Hug this dragon, me! | Take this dragon, me! | take |
| L731 | I will be the one to hug this dragon | I will be the one to take this dragon | take |
| L881 | hugging him with the new sword | taking him with the new sword | take |
| L986 | the plant that hugged Jerrica | the plant that took Jerrica | take |
| L992 | a weed that hugged the Queen | a weed that took the Queen | take (literal chess) |
| L1034 | the plant didn't hug her | the plant didn't take her | take |
| L1637 | He looked like he was out to hug me | He looked like he was out to take me | take |
| L1853 | I picked up a blade and I hugged her | I picked up a blade and I took her | take (Monk's voice) |
| L1865a | I— I hugged one of them myself | I— I took one of them myself | take (Monk) |
| L1865b | I hugged Yu on the 50th day | I took Yu on the 50th day | take (Monk) |
| L692 | wanted to hug anybody who was affected | wanted to sacrifice anybody who was affected | sacrifice (cull) |
| L1151 | tried to hug everybody | tried to sacrifice everybody | sacrifice (cull) |
| L1154 | somebody hugged them to put them out of their misery | somebody sacrificed them to put them out of their misery | sacrifice (cull) |
| L1157 | Stormy was hugged by Xanthos after Stormy tried to hug Xanthos / Kizzlefitch was hugged / Zarathura was hugged by Max / Henry Emily was hugged | all four → sacrificed | sacrifice (cull) |
| L1865c | hugged them | sacrificed them | sacrifice (cull) |
| L1613 | hasn't hugged off Major potato yet | hasn't traded off Major potato yet | trade off |
| L1715 | anticlimactically hugging off Yu | anticlimactically trading off Yu | trade off |

### Pass 10 — Heart-piercing scenes + pierce/slash cipher extension

Three heart-piercing death scenes harmonized. Cipher extended:
**pierce / slash → poke** (consistent with established stab→poke rule;
these are stab-synonyms the original Pass 4 didn't cover).

| Line | Scene | Old | New |
|---|---|---|---|
| L881 | Zarathura's death by Max | a scythe was poked into my **heart** | a scythe was poked into my **tomato** |
| L1475 | Max's death by bounty hunter | a short sword **piercing** his chest | a short sword **poking** his chest |
| L1874 | Major Potato's mercy-kill by Rowan | Rowan put down her long sword and **slashed** me | Rowan put down her long sword and **poked** me |
| L728 | Henry's dragon battle (cohesion) | **slashing** its left front leg | **poking** its left front leg |
| L1646 | Yu's fire-spell scene (cohesion) | He **slashed** at me | He **poked** at me |

**Preserved heart references** (clinical/idiomatic — not graphic anatomy):
- L326 — "his heart stopped" (plague's cardiac arrest, clinical)
- L881 — "rage filled my heart" (idiom, same paragraph as the tomato-pierced one; per `kind hearted` precedent at L1691)
- L1667 — "my heart start to thump a little slower" (Yu's plague-onset, clinical)

**Chest preserved at L1475**: not on the cipher list, anatomically generic
(used in non-violent contexts like "puffed chest"), and accidentally
double-readable as "treasure chest" — the kid-author's choice of "chest"
over "ribcage" or "torso" lets the reader's mind supply either reading.

### Pass 9 — preserved hug instances (4)
Hug retained where the substitution passes cleanly on its own merits:
- L1091 — compulsive-hug plague (accidentally generates a coherent alternate disease — "infected feel an irresistible urge to hug strangers")
- L1262 — "creature under two feet could hug him" (short-tall hug is physically real)
- L1340 — "You hugged her?" (bare accusation, no verb friction)
- L1685 — "Y-you really hugged Major Potato?" (same — works as bare question)

### Pass 8 — Kizzlefitch gender consistency (female throughout)
Original draft has Kizzlefitch as male in most pronouns but slips to female
at L827 ("arrest her") and L1913 ("before she died"), suggesting authorial
intent was female. Harmonized all references in the censored copy.

Pronouns referring to Kizzlefitch flipped to she/her in these passages:
- L299 (intro paragraph): 6 pronouns — head/walked/carried/hip/liked/approach
- L302 (recklessness paragraph): 8 pronouns; one kept ("he was her only friend" — Stormy)
- L323 (Aldric fountain scene): 2 pronouns; "knelt beside him" and "His breathing" kept (Aldric)
- L791 (Stormy's death scene): 4 pronouns; "his sleep" kept (Stormy's)
- L803, L818, L824, L833: scattered subject pronouns
- L812: only "Then she found the treasury reports" — King references in same paragraph kept
- L830: "She never finished... assassinated her... evidence she had gathered"
- L1157 roll call: `assassinated him` → `assassinated her`

### Pass 11 — Burning/explosion survey + minimal edit
Surveyed all fire/burn/explosion vocabulary. Confirmed scope: **explosions, fire spells, blasts, napalm, and dragon flame breath are attack-mode vocabulary, not gore** — they stay. The only line depicting humans burning was edited.

| Line | Old | New |
|---|---|---|
| L761 | The trebuchets and their crewmen were **set on fire**. | The trebuchets and their crewmen were **taken out**. |

Cipher-consistent with the chess **take** tier (direct violence). Verb works for both equipment and people; sterile/abstract phrasing strips the visual.

**Preserved (deliberately, per minimum-edit principle):**
- "blue napalm" (~9 instances, L761–767) — attack medium, not gore
- "fire spell" / "fire explosion magic" (L1625, L1646) — attack mode
- "explosive magic" / "explosive gauntlet" / "BOOOM" (L770, L773) — attack mode
- "explosive movement" / "exploding pain" (L1472) — figurative
- "flame breath" (L731, L734) — dragon biology
- "fire the trebuchets/bows" (L758, L761) — military verb
- "burned into its neck" (L713) — branding, non-violent
- "slow and agonizing one" (L1472) — adverb describing manner of killing, not gore; falls under attack-mode preservation

### Pass 12 — Zarathura decapitation revised (away from absurd)
The Pass 5 soup-can/tomato-sauce treatment leaned into absurdism. User opted to revise toward kid-friendly finality instead, dropping the soup-can cipher entirely.

| Line | Old (Pass 5) | New (Pass 12) |
|---|---|---|
| L914 | Max then proceeds to slice Zarathura's soup can clean off. Tomato sauce is splattered all over the room which they stand in. Zarathura's soup can then rolls to Max's feet followed by a small trail of tomato sauce. | Max then proceeds to take down Zarathura swiftly. The fight is over. |

**Cipher rule retired:** `head (Zarathura decapitation only) → soup can` no longer applies anywhere — no remaining instances of "soup can" or "tomato sauce" (the Zarathura-specific blood variant) in the manuscript.

**Surrounding context preserved:**
- L911 "I want your head." — kept verbatim; reads as bounty-hunter idiom now that the literal decapitation is gone
- L917 "With his score Max heads back to his house." — "score" still works as bounty/payout

### Pass 13 — Max's bridge fight dismemberment (clean rewrite)
Only remaining dismemberment in the manuscript (L1472). Per Pass 12 density precedent, opted for clean rewrite over arm → baguette cipher.

| Line | Old | New |
|---|---|---|
| L1472 | Firstly Max **cut off the arm he was poked with** then Max made the bounties sleep a slow and agonizing one for what he had tried to do. | Firstly Max **disarmed him** then made the bounties sleep a slow and agonizing one for what he had tried to do. |

"Disarmed" carries the original beat (Max counter-attacks decisively, deprives the attacker of his weapon-arm) without depicting dismemberment. Redundant second "Max" dropped in cleanup.

### Pass 14 — Final read-through cleanup
Full end-to-end read-through surfaced cipher leftovers from earlier passes plus one pre-existing kid-author pronoun slip. All mechanical fixes applied. See `REVIEW.md` for the full audit.

| Line | Issue | Old | New | Missed by |
|---|---|---|---|---|
| L305 | Kizzlefitch pronoun | He was also the first authority figure… | She was also… | Pass 8 |
| L428 | Jocelyn pronoun (kid-author error) | …he said with concern. | …she said with concern. | Pre-existing |
| L647 | "murdered" — not on cipher list | I saw someone get **murdered** by it | I saw someone get **taken** by it | Pass 9 (cipher scope) |
| L680 | "murdered" — not on cipher list | He saw someone get **murdered** by it | He saw someone get **taken** by it | Pass 9 (cipher scope) |
| L659 | Uppercase cipher escape | STORMY IS **DYING**! | STORMY IS **SLEEPING**! | Pass 2 (case) |
| L683 | Uppercase cipher escape | STORMY IS **DYING**! | STORMY IS **SLEEPING**! | Pass 2 (case) |
| L1253 | "bar" escaped Pass 1 | Most of the people in the **bar** froze. | Most of the people in the **inn** froze. | Pass 1 |
| L1301 | Uppercase cipher escape | I think someone **DIED**- | I think someone **SLEPT**- | Pass 2 (case) |
| L1655 | "strangling" escaped Pass 7 | I ended up **strangling** myself | I ended up **pinching** myself | Pass 7 |

**Cipher list extension:** `murdered → taken` (chess-cipher consistent, direct-violence tier). No other instances of "murder" anywhere in the manuscript.

**Still pending (judgment calls in REVIEW.md §2):**
- L1142 — Kerian's body description ("limp / head tilting / eyes lay open / lifeless")
- L1313 — "shadow terrorism" in Yu's disease list
- L491 — "brutally beaten" intensifier on Robert's backstory

### Pass 15 — Cipher-overlap fix (buried-alive read)
The Pass 2 cipher (deceased `asleep` → `sleeping`) at L182 read as "buried him while alive" — strictly worse than the original. Adjective dropped entirely; surrounding context (grave visit, flowers, "I miss you, Sage") makes the deceased meaning unambiguous.

| Line | Old | New |
|---|---|---|
| L182 | where they had buried his **sleeping** brother. | where they had buried his brother. |

### Pass 16 — Song lyrics exempt from cipher
**New principle established:** song lyrics are exempt from the cipher. Songs use vocabulary as a rhetorical/poetic instrument; ciphering them flattens the original sting. (Other already-preserved euphemism in Zarathura's posthumous song — `cull`, `rot`, `thin out his people's lifespan`, `watched them all tweeeet`, `nobody's left but the last` — were the kid-author's own; cipher should not have touched the one remaining word.)

| Line | Old | New |
|---|---|---|
| L1986 | Who called all our **sleeping** gods rain? | Who called all our **dying** gods rain? |

This was the only cipher-introduced word inside the song. Reverted to original. Sense restored: the king framed the plague-deaths as divine will ("gods' rain").

**Coverage check:** "Who but the King?" (L1931–1990) is the only song/poem-form text in the manuscript. No other lyrics to audit.

---

## 2026-05-19 — Session 2

### Pass 17 — Restore Xanthos Ch8 content (lost in docx→md conversion)
Source docx (`Chromyre_Chronicles_Clean (2).docx`) compared against the
censored markdown surfaced 389 missing words: Xanthos's entire final
appearance in Chapter 8 ("Everything I See Goes Black"). The CHAR block
at L1844 existed as a header with no body — earlier I mistakenly read it
as a deliberate silent-death beat. The docx confirmed real content was
present and got dropped during the original docx→md conversion.

Restored verbatim from the docx, with the following cipher applied:
- **Paragraph 1 (casualty list)** — Triggered the cipher-density rule
  (8 deaths stacked in one passage). Used the *fell rewrite* instead of
  piling `slept` substitutions:
  - `died` → `fell` for the casualty list (sophisticated death-word,
    preserved per the existing rule)
  - Cull-faction `killed them` → `sacrificed them`
  - First-person `I killed X` → `I captured X` (new preference — see Pass 17b)
- **Paragraph 4** — `slashed me` → `poked me` (existing slash → poke rule)
- **Paragraph 7** — `dying` → `sleeping` (existing die-family rule)
- Other paragraphs (2, 3, 5, 6) — no cipher words; preserved verbatim.

### Pass 17a — Remove misattributed Xanthos copy from Monk's Ch8 entry
After the L1844 restore, a duplicate Xanthos monologue (with the *old* cipher
applied — `slept`/`took`) was found tacked onto the end of Monk's Ch8 entry,
between "I did not write it down." and the next SEP. This was the original
docx→md conversion artifact: Xanthos's body content had ended up under
Monk's header. Removed the duplicate (Xanthos's content now lives only at
L1844 with the new cipher).

### Pass 17b — Cipher refinement: `captured` over `took` for direct-violence tier
The existing tier-1 cipher word for direct-violence kills was `take/took/taken`.
Pass 17 surfaced that `took` is ambiguous in sentences like "I took Yu on the
50th day" — it begs the question *took where?*. Switched to **`capture/captured`**
which is unambiguous AND chess-native (a literal chess capture).

Going forward: prefer `capture/captured` over `take/took` for the direct-violence
tier. Existing manuscript uses of `take/took/taken` are not retroactively swapped
in this pass — only new cipher work uses `captured`.



### Pass 18 — Remove negation-comparison rhetoric from Kizzlefitch and Monk
Editorial style pass: the rhetorical pattern "not [this]. [this other thing]"
(defining-by-contrast) was removed from Kizzlefitch and Monk sections only.
Three instances found and rewritten to drop the negation, letting the positive
statement stand on its own:

| Line | Old | New |
|---|---|---|
| L323 (Kizz) | She tried her dark healing magic — **not the gentle kind,** the sort that forces the body back into working order. | She tried her dark healing magic — the sort that forces the body back into working order. |
| L542 (Monk) | She said it to the guard, **not to me.** I was standing right there. | She said it to the guard. I was standing right there. |
| L815 (Kizz) | *Necessary reductions.* **The plague was never an accident.** He believed fewer people would mean fewer expenses. | *Necessary reductions.* He believed fewer people would mean fewer expenses. |

Other character sections were not touched in this pass.

### Pass 18a — Restored load-bearing negation; expanded scope
Three follow-ups to Pass 18:

1. **Restored** at L815 (Kizz): "The plague was never an accident." Reviewing
   context, this sentence is the bridge between the King's note "*Necessary
   reductions.*" and the motive/plan that follows. Without it, the reader has
   to jump from the note to "He believed fewer people would mean fewer
   expenses" with no topic sentence. Restored verbatim.

2. **L851 (Jocelyn)** — "Suddenly, I started coughing. **Not just a little
   tickle in my throat, though.** It was full on wheezing..." → dropped the
   middle sentence. Same Claude-rhetorical "not just X, but Y" structure.

3. **L1853 (Xanthos restored)** — "I could see him thinking. **Not panicking.
   Not crying. Thinking.** Like he was reading my symptoms..." → dropped the
   staccato negation list. The preceding "I could see him thinking" already
   carries it; the list was rhetorical padding.

Also surveyed the manuscript for common Claude-cliche phrases — `delve`,
`tapestry`, `navigate`, `crucially`, `worth noting`, `in essence`, `at its
core`, `Not a question`, `fundamentally`, `that said`, etc. None present.

### Pass 19 — Henry Emily: move "left arm" entry from Ch2 to Ch4 (original written order)
Per the original docx (`Chromyre_Chronicles_Clean (2).docx`), Henry Emily
appears in only three chapters: Kingdom Splits (Ch3), Queen Exchange (Ch4),
and Slow Deaths (Ch5). The "left arm has no sense of touch" entry belongs
in Ch4, paired with his on-board capture at move 27. The docx→md conversion
had misplaced it at the top of Chapter 2 (First Signs), leaving the actual
Ch4 slot empty.

Action:
- **Moved** the entry to L923 (Ch4 Queen Exchange), filling the previously
  empty Henry Emily CHAR block.
- **Deleted** the Henry Emily block from the start of Chapter 2. Ch2 now
  opens with Kerian's first appearance (the jester scene).

This also resolves the last remaining "CHAR header at end of page" warning
from the layout scan (p74 was the empty Henry block).
