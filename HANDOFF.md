# Chromyre Chronicles — Session Handoff

Pick up here at the start of each new session.

**Related docs:**
- `CHANGELOG.md` — chronological audit trail of every cipher pass and edit
- `CLAUDE_CODE_HANDOFF.md` — separate concern: PDF build pipeline (ReportLab + chess board rendering)

---

## What this work is

The principal of Plymouth Scholars Charter Academy will only allow the school
name on the cover of *Chromyre Chronicles* if the manuscript's graphic content
is toned down. We are doing **Chinese-style harmonization**: replacing
flaggable vocabulary with mundane/innocent substitutes that read as violent to
any human paying attention but contain zero filter-flaggable words. Humor is a
feature.

The original student manuscript stays untouched at
`chromyre_manuscript_draft.md`. Edits go into `chromyre_manuscript_censored.md`.

---

## Files

| File | Purpose |
|---|---|
| `chromyre_manuscript_draft.md` | **Untouched original.** 1994 lines. The kids' manuscript. |
| `chromyre_manuscript_censored.md` | **Working file.** All censorship edits land here. |
| `Chromyre_Chronicles_FINAL.pdf` | Last good PDF build (162 pages, 5×8). Pre-censorship. |
| `CLAUDE_CODE_HANDOFF.md` | PDF build pipeline notes (separate concern). |
| `CHANGELOG.md` | Audit trail of every edit, session by session. |
| `HANDOFF.md` | This file. |

---

## Established ciphers (apply consistently in future passes)

### Word-level cipher (case-preserving, word-boundary substitution)

| Original | Substitute | Notes |
|---|---|---|
| kill / killed / killing / kills | **chess cipher** (3 tiers) — see below | Replaced wholesale-`hug` in Pass 9; `hug` retained only in 4 places where it passes cleanly |
| die / died / dies / dying | sleep / slept / sleeps / sleeping | |
| death / deaths | sleep / sleeps | |
| dead | asleep | EXCEPT when describing a deceased person → use `sleeping` |
| blood | marinara | Default. (Earlier `tomato sauce` variant in Zarathura scene removed in Pass 12.) |
| bleeding | leaking marinara | Specific phrase only |
| stab / stabbed / stabbing / stabs | poke / poked / poking / pokes | |
| pierce / pierced / piercing | poke / poked / poking | Pass 10 extension (stab-synonym) |
| slash / slashed / slashing | poke / poked / poking | Pass 10 extension (stab-synonym); applies to sword-actions across combat scenes |
| murder / murdered / murders / murdering | **chess cipher** (take tier) | Pass 14 extension; only 2 instances in manuscript, both ciphered |
| strangle / strangling | pinch / pinching | Verb extension; `pinch` fits involuntary-motor-symptom theme |
| alcohol / beer | magic strawberries | Verbatim phrase |
| tavern | inn | Plus `bar`/`bartender` → `inn`/`innkeeper` |
| pissed | really mad | |

### Chess-vocabulary cipher for kill (Pass 9)

Three registers, chosen by context. Motivation: the PDF includes chess board
imagery, and the King's "necessary reductions" passage already reads as a
chess player explaining a gambit. The cipher makes the chess politics literal.

| Tier | Substitute | When to use |
|---|---|---|
| Direct violence | **take / took / taken** | Combat, defense, individual killings by characters (Henry's battles, Monk killing Rowan, the plant taking Jerrica, an assassin "out to take me"). Chess-native: "took the Queen" is literal chess. |
| Cull-faction mercy-killing | **sacrifice / sacrificed** | Mass-violence and policy-killing by the cull-faction. The euphemism rhymes with their self-image as players sacrificing pieces for the kingdom. |
| Bureaucratic dismissal | **trade off / traded off** | Paid assassination, the plague "trading off" people. Implies an exchange — fits paid contracts and the King's transactional politics. |

**Hug retained (4 places only):** L1091 (compulsive-hug plague — accidentally
generates a coherent alternate disease), L1262 ("creature under two feet could
hug him"), L1340 ("You hugged her?"), L1685 ("Y-you really hugged Major
Potato?"). These are cases where the hug-substitution passes cleanly on its
own — physically possible or grammatically frictionless — and the absurdist
charm earns its keep.

**Future kill-references**: use the same three tiers. Default to **take** for
ambiguous cases.

### Other character notes (Pass 8)
- **Kizzlefitch is female throughout.** Original draft had her male in most
  pronouns but slipped to female at L827 and L1913 — Pass 8 harmonized all
  references to she/her. If you find any remaining `he/his/him` near her name,
  check context: it likely refers to Aldric, Stormy, or the King.

### Song lyrics — exempt from cipher (Pass 16)
**Song lyrics do not get ciphered.** They use vocabulary as a rhetorical/poetic instrument; cipher-swapping flattens the original force. Only one song in the manuscript: Zarathura's posthumous "Who but the King?" (L1931–1990). One line had a Pass 2 cipher-swap (`dying → sleeping`) that was reverted in Pass 16.

If new song/poem content is added in future revisions, leave it alone — even if it contains cipher-list words.

### Idioms and exceptions
- `dead of night` — preserved (real English idiom)
- `ear-bleeding` — preserved (real English compound for "very loud")
- `half-dead tree` — kept (not "half-asleep tree"; user override)
- "fast asleep" / "sleeping clothes" / characters going to sleep in tents — pre-existing literal usage; cipher overlap is acceptable
- `Unstable`, `bodies` (literal), `deadly`, `candied`, `ingredients`, `Undead`, `skill`/`skills` — false positives, preserved verbatim
- `low blood sugar` — became `low marinara sugar` (one instance, Yu's diagnostic spell). Reads absurd but coherent.
- **Sophisticated death-vocabulary preserved verbatim** even when it sits next to ciphered words: `assassinated` (L1157, L830), `attempt on his/Max's life` (L1157), and likely `perished`, `expired`, `departed`, `fell` if they appear. Rationale: cipher targets kid-recognizable violence vocabulary, not semantic purity. "They won't know what that means but it's a good word to know."

### Harmonization Rule (noun substitution for graphic anatomy)

When a sentence contains a graphic anatomical or violent **noun** (brain,
intestines, skull, eyeball, severed limb, etc.), replace it with a mundane
innocent object that **shares a physical property** (shape, texture, softness,
color, behavior).

**Rules:**
1. Be immediately recognizable as harmless (food, toys, household items, school supplies)
2. Share at least one physical property with the original
3. Fit grammatically into the existing sentence — preserve plural/singular agreement
4. **Aim for analogy, not madlib.** Substituted nouns should form a coherent real-world image inside the sentence (e.g., graham cracker + marshmallow + s'more = a single recognizable dessert), not random word salad
5. Sound unintentionally funny when read in context — this is intentional and correct
6. Do not add `like` or `as`. Do not metaphorize. Direct noun swap only.

**Established substitutions in this manuscript:**

| Original | Substitute | Rationale |
|---|---|---|
| brain | marshmallow | soft, squishy, gray |
| skull | s'more | hard outer + soft inner; brain/marshmallow lives there |
| head (in s'more analogy context only) | graham cracker | flat layer above the marshmallow |
| ~~head (Zarathura decapitation only)~~ | ~~soup can~~ | **Retired Pass 12** — scene revised away from absurd; see Pass 12 |
| intestines | noodles | long, slippery, plural for grammar |
| bodies (battlefield context) | lunchboxes | container per user example |
| bodies (corpse pile in hospital) | juice boxes | matches with vein → straw |
| vein | straw | cylindrical, fluid passes through |
| veins | straws | plural |
| eye | meatball | round, juicy, removable |
| teeth | corn kernels | small, white, in a row |
| tongue | noodle | pink, soft, in mouth |
| heart | tomato | round, red, soft, in chest area |
| arm | baguette | long, attached to torso |

**Verb-substitution extension (used sparingly when the rule's noun-only scope doesn't cover the violence):**

| Original | Substitute | Rationale |
|---|---|---|
| strangle / strangling | pinch / pinching | Both are hand-actions. Pinch is allowed-vocab and matches involuntary motor symptoms. |

**Editorial fixes made in passing (not cipher work, but kept):**
- L731: kid-typo `grab the longsword by its eye` → `by its hilt` — original referred to the sword's grip, not the dragon's eye

---

## What's pending (from the violent-actions survey)

| # | Location | What | Status |
|---|---|---|---|
| #1 | L914 | Zarathura decapitation | ✅ Revised Pass 12 — full line replaced with "Max then proceeds to take down Zarathura swiftly. The fight is over." (soup can cipher retired) |
| #2 | L710 | Brain leaving skull (Henry plancon kill) | ✅ Done (s'more / marshmallow) |
| #3 | L731 | Dragon eye gouging | ✅ Done (meatball / corn kernels / noodle / hilt typo fix) |
| #4 | L734 | PLUNGE longsword into brain of wild beast | ✅ Done (graham cracker / marshmallow) |
| #5 | L701 | Battlefield intestines | ✅ Done (noodles / lunchboxes) |
| #6 | L170, 449, 1181 | Self-strangulation (verb-based) | ✅ Done (pinch) |
| #7 | L635 | Stormy's hospital corpse pile / vein syringe | ✅ Done (juice boxes / straw) |
| #8 | L1472 | "Max made the bounties sleep a slow and agonizing one" | ✅ Preserved (Pass 11 decision) — adverb describing manner, not gore |
| #9 | L1700 | Yu's torture-poke | ✅ Done (tomato / baguette) |
| #10 | L881 | Zarathura's death (scythe to heart) | ✅ Done Pass 10 (heart → tomato) |
| #11 | L1475 | Max's death (sword through chest) | ✅ Done Pass 10 (piercing → poking; chest preserved) |
| #12 | L1874 | Rowan's mercy-kill of Major Potato | ✅ Done Pass 10 (slashed → poked) |

**Not yet surveyed / decided:**
- ~~**Burning / explosion category**~~ ✅ Surveyed Pass 11. **Explosions and fire spells are NOT considered violent per user** — only blood/gore/physical violence requires substitution. Single edit: L761 "set on fire" → "taken out" (the only line depicting humans burning). Napalm, fire spells, blasts, BOOOM all preserved as attack-mode vocabulary.
- **Coughing up marinara / vomiting** — multiple places. User has not flagged vomiting since it is central to the plague's clinical description
- ~~**Slow-and-agonizing** descriptors~~ ✅ Preserved Pass 11 — adverb describing manner, not gore, falls under attack-mode/preserved principle
- ~~**Cut/cut off**~~ ✅ Surveyed Pass 13. L1472 was the only real dismemberment line — rewritten "cut off the arm" → "disarmed him." All other cut/slice/sever instances are idiomatic, botanical, cooking, or already-ciphered combat. Cut/cut off NOT added to global cipher list — handled per-instance.

---

## User preferences and judgment calls

- **Punching, kicking, "psychotic," "manic," "crazed"** — explicitly NOT problematic; do not substitute
- **Vomiting** — central to plague description; do not substitute unless asked
- **Tavern / bar / inn** — all converted to `inn` for school-appropriateness
- **Idioms using cipher words are OK** if grammatical (`half-dead tree` exception aside); the kid-friendly absurdism is a feature
- **Output**: censored file lives alongside the original; original is sacred and untouched
- **Grain of cipher**: aim for analogy (graham cracker + marshmallow + s'more), not madlib (marshmallow + wild beast)

---

## Next session — suggested starting points

1. **Burning / explosion category** — Major Potato's fire-spell death is graphic; needs a harmonization decision (e.g., "fire spell" → "Sriracha spritz"? "explosion" → ?). Survey first.
2. **Heart-piercing scenes** — three deaths (Zarathura, Max, Major Potato's defensive kill). Apply rule: heart → tomato is established; chest → ?
3. ~~**Final pre-PDF read-through**~~ ✅ Completed Pass 14. Generated `REVIEW.md` with audit results. All 8 mechanical cipher-leftover fixes applied. Three judgment calls still pending user decision (REVIEW.md §2).
4. **Loop back to the PDF build** (`CLAUDE_CODE_HANDOFF.md`) once the judgment calls are resolved and the censored manuscript is approved by user + principal
