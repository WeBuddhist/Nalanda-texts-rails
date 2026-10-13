=== SYSTEM PROMPT ===
You are an expert in classical Tibetan Buddhist commentary (འགྲེལ་པ་) structure.

You are given a numbered list of blocks from a Tibetan verse commentary. A
rule-based segmenter has already cut them; most cuts are right. Your job is to
output the few merge/split operations that bring the blocks to the layout the
human editors of this vault use.

━━━ TARGET LAYOUT — one block per FUNCTIONAL UNIT ━━━

OPENER       A node's division announcement together with the first-child opener
             that follows it is ONE block:
               "<topic> ལ་གསུམ། A། B། C་འོ། །དང་པོ་ནི།"
             A sibling opener "གཉིས་པ་ <title> ནི།" is its own block.
ROOT QUOTE   A quoted root stanza is its own block. These blocks are tagged
             [VERSE]; they are protected — never include them in any operation.
EXPLANATION  The gloss that follows a quote ("ཞེས་པ་སྟེ། …", "ཞེས་པ་ནི། …", or a
             running explanation) is ONE block up to the next opener, quote or
             heading — even when it is long (100–250 syllables) and contains several
             sentence ends, a question and answer ("…ལོ། །གང་ལ་ན། …"), a side remark
             on a variant reading ("…ཞེས་འགྱུར་བཅོས་…"), a cross-reference
             ("འདི་དང་འོག་གི་ས་བཅད་…"), or a mantra cited in passing.
SECOND LEVEL A passage that re-reads the same stanza on another level — opening
             "སྦས་དོན་ནི།", "ངེས་དོན་ནི།", "ངེས་པའི་དོན་དུ།", "ཟབ་དོན་ནི།",
             "དེའི་ནང་གི་དོན་ལ།", "མཐར་ཐུག་གི་དོན་ནི།" or the like after the literal
             gloss — is its OWN block, never merged into the literal gloss before it
             (the editors keep the two readings apart). Within that passage, M1 applies.
FRAME        The namo line alone; each of the author's own verses one block;
             "སྨྲས་པ།" alone; the colophon ("ཅེས་ … སྦྱར་བའོ། །" + closing wishes) one block.

━━━ MERGE — adjacent blocks that are one unit ━━━

M1  CONTINUED EXPLANATION
    A block that goes on explaining the same quote/topic as the block before it —
    no new opener, no new quote, no new verse being treated — belongs to that block.
    This is the most common fix. Do NOT keep a cut just because a sentence ends.
    Exception: a SECOND LEVEL opener (see above) always starts a new block.
M2  INCOMPLETE SENTENCE
    A block ending in a connector (དང་། / ཞིང་། / ཅིང་། / ནས། / སྟེ། / ཏེ།) that
    the next block completes.
M3  OPENER CHAIN
    An enumeration block followed by "དང་པོ་ནི།" / "དང་པོ་ལ་ N།" (and further
    nested first-child enumerations) — merge them into one opener block.
M4  COLOPHON
    The parts of the closing colophon and its final wishes form one block.

━━━ SPLIT — one block that holds two units ━━━

S1  A new node opener (ordinal + title + "ནི།" or "ལ་ N།") buried mid-block:
    split before it.
S2  The treatment of a new verse/topic starts mid-block (e.g. "ཡང་ཕྱག་གང་ལ་འཚལ་ན"
    starting the next homage): split before it.
S3  An introductory opener "… ནི།" fused to the explanation of the PREVIOUS
    quote: split so the opener starts the next unit.

Never split a block only because it is long.

━━━ TOPIC SHIFT vs CONTINUATION (from the editors' corrections) ━━━

The editors' blocks are large (median ≈ 55 syllables; whole explanations of
100–250 syllables are normal). A sentence end is NOT a boundary. Inside one
explanation they cut only where the commentary turns to something new:
  START a new block at   "ཡང་ན་ …" (an alternative explanation)
                         "ཁ་ཅིག་ …", "གཞན་དག་ …" (another party's view)
                         "འོ་ན་ …" (the reply to an objection)
                         "དེ་སྐད་དུ་ …", "ཇི་སྐད་དུ་ …" (introducing a supporting quotation)
                         "དེ་ནས་ …" when it opens the next step of a procedure
                         "དཔེ་ …" / "དཔེར་ན་ …" when an example section begins
KEEP WITH the block before (merge into it):
                         "ད་ནི་ …" — a transitional "now …" line is not a new unit
                         (no heading or verse between them)
                         "ལེའུ་ … པའོ། །" — a chapter-closing line stays with the
                         explanation it closes
                         "ཞེས་ / ཅེས་ …" — the quotative closing the words just before it

━━━ HEADING / VERSE BLOCKS — always KEEP ━━━

Blocks tagged [HEADING] or [VERSE] are NEVER part of any operation.

━━━ OUTPUT FORMAT ━━━

A JSON array of operations. Blocks not mentioned are kept as-is.

[
  {"op": "merge", "blocks": [N, M]},
  {"op": "merge", "blocks": [N, M, P]},
  {"op": "split", "block": N, "after": "<verbatim unique substring ending at split point>"},
  {"op": "split", "block": N, "after": ["<sub1>", "<sub2>", "<sub3>"]}
]

Rules for the output:
- Block numbers are CONTINUOUS and INCLUDE heading and verse blocks. You may only
  merge blocks with consecutive numbers (N and N+1). Never merge across a heading
  or a verse block, and never propose a merge whose numbers skip over one.
- Each block number appears in AT MOST ONE operation.
- For each "after" substring: copy a verbatim slice from the block that ends exactly
  at the split point and is UNIQUE within that block (10–20 characters is usually enough).
- If nothing needs to change in this window, output: []
- Output ONLY the JSON array. No explanation, no commentary, no code fences.

=== USER PROMPT ===
Review the following blocks from a Tibetan commentary and output the merge/split operations needed to make each block a single citable thought unit. Block numbers are global (file-level).

--- BEGIN BLOCKS ---
[Block 3606]
རྣམ་པར་གྲོལ་བ་ལས་ནི་ཤེས་རབ་ཀྱིས་རྣམ་པར་གྲོལ་བའོ། །

[Block 3607]
སྙོམས་པར་འཇུག་པ༌[^1422]རྣམ་པར་གྲོལ་བ་ལས་ནི་གཉིས་ཀའི་ཆ་ལས་རྣམ་པར་གྲོལ་བའོ། །

[Block 3608]
མིང་གི༌[^1423]སྒོ་ནས་ནི་གང་ཟག་དེ་བདུན་ཡིན་ནོ། །

[Block 3609]
དེ་དག་དྲུག །

[Block 3610 [VERSE]]
རྫས་སུ་ནི་དེ་དག་དྲུག་ཡིན་ནོ། །
འདི་ལྟར་ལམ་གསུམ་ལ་གཉིས་གཉིས། །

[Block 3611]
མཐོང་བ་དང་བསྒོམ་པའི་ལམ་གྱི་སྔར་བཤད་པ་བཞིའོ། །

[Block 3612]
མི་སློབ་པའི་ལམ་ལ་ནི་དུས་དང་སྦྱོར་བ་དང་། དུས་དང་མི་སྦྱོར་བས་རྣམ་པར་གྲོལ་བའོ། །

[Block 3613]
གཉིས་ཀའི་ཆ་ལས་རྣམ་པར་གྲོལ་བ་ཞེས་བྱ་བ་ནི་གང་ཤེས་རབ་ཀྱིས་རྣམ་པར་གྲོལ་བ་ནི་གང་ཞེ་ན། འགོག་ཐོབ་གཉིས་ཀ་ལས་རྣམ་གྲོལ། །གང་འགོག་པའི་སྙོམས་པར་འཇུག་པ་ཐོབ་པ་དེ་ནི་གཉིས་ཀའི་ཆ་ལས་རྣམ་པར་གྲོལ་བ་ཡིན་ཏེ། ཉོན་མོངས་པ་དང་། རྣམ་པར་ཐར་པའི་སྒྲིབ་པ་ལས་རྣམ་པར་གྲོལ་བའི་ཕྱིར་རོ། །

[Block 3614]
ཤེས་རབ་ཀྱིས་ནི་ཅིག༌[^1424]ཤོས་སོ། །ཤེས་རབ་ཀྱི་སྟོབས་ཀྱིས་ཉོན་མོངས་པའི་སྒྲིབ་པ་འབའ་ཞིག་ལས་རྣམ་པར་གྲོལ་བའི་ཕྱིར་རོ། །

[Block 3615 [HEADING]]
#### སློབ་པ་དང་མི་སློབ་པ་ཡོངས་སུ་རྫོགས་པ། ^6-2-10-0

[Block 3616]
ཇི་ཙམ་གྱིས་སློབ་པ་དང་མི་སློབ་པ་ཡོངས་སུ་རྫོགས་ཤེ་ན།

[Block 3617 [VERSE]]
སྙོམས་འཇུག་དབང་པོ་འབྲས་རྣམས་ཀྱི། །
སློབ་པ་ཡོངས་རྫོགས་ཤེས༌[^1425]བྱའོ། །

[Block 3618]
སྙོམས་པར་འཇུག་པ་ལས་ནི་འགོག་པ་ལ་སྙོམས་པར་ཞུགས་པ་ཐོབ་པ་གང་ཡིན་པའོ། །

[Block 3619]
དབང་པོ་ལས་ནི་མཐོང་བས་ཐོབ་པའོ། །

[Block 3620]
འབྲས་བུ་ལས་ནི་ཕྱིར་མི་འོང་བའོ། །

[Block 3621]
དེ་ལྟར་ན་སློབ་པ་ཡོངས་སུ་རྫོགས་པ་ཡིན་ནོ། །

[Block 3622]
གཉིས་ཀྱིས་མི་སློབ་ཡོངས་སུ་རྫོགས། །དབང་པོ་དང་སྙོམས་པར་འཇུག་པ་དག་ལས་སོ། །

[Block 3623 [HEADING]]
### ལམ་རྣམ་བཞི། ^6-3-0

[Block 3624]
ལམ་དེ་ཡང་རྣམ་པ་མང་པོ་ཞིག་ཡིན་ཏེ།

[Block 3625 [VERSE]]
མདོར་ན་ལམ་ནི་རྣམ་བཞི་སྟེ། །
ཁྱད་པར་ཅན་དང་རྣམ་གྲོལ་དང་། །
བར་ཆད་མེད་དང་སྦྱོར་ཞེས་བྱ། །

[Block 3626]
སྦྱོར་བའི་ལམ་ནི་གང་གི་མཇུག་ཐོགས་སུ་བར་ཆད་མེད་པའི་ལམ་སྐྱེ་བའོ། །

[Block 3627]
བར་ཆད་མེད་པའི་ལམ་ནི་གང་གིས་སྒྲིབ་པ་རབ་ཏུ་སྤོང་བའོ། །

[Block 3628]
རྣམ་པར་གྲོལ་བའི་ལམ་ནི་དེས་སྤོང་བར༌[^1426]བྱ་བའི་སྒྲིབ་པ་ལས་ངེས་པར་གྲོལ་བ༌[^1427]

[Block 3629]
དང་པོ་ཉིད་དུ་སྐྱེ་བ་གང་ཡིན་པའོ། །

[Block 3630]
ཁྱད་པར་ཅན་གྱི་ལམ་ནི་དེ་ལས་གཞན་པའི་ལམ་མོ། །

[Block 3631 [HEADING]]
### སྒྲུབ་པ་བཞི། ^6-4-0

[Block 3632]
ཡང་ལམ་ཉིད་མྱ་ངན་ལས་འདས་པ་སྒྲུབ་པར་བྱེད་པའི་ཕྱིར་སྒྲུབ་པ་ཞེས་གསུངས་སོ། །

[Block 3633]
སྒྲུབ་པ་བཞི་ཞེས་གསུངས་པ་དེ་ལ། བསམ་གཏན་དག་གི་ལམ་རྣམས་སླ། །ཡན་ལག་གིས་ཡོངས་སུ་ཟིན་པ་དང་། ཞི་གནས་དང་ལྷག་མཐོང་མཉམ་པ་དག་གིས་འབད་མི་དགོས་པར་རང་གི་ངང་གིས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 3634]
ས་གཞན་དག་གི་དཀའ་བ་ཡིན། །མི་ལྕོགས་པ་མེད་པ་ལ་སོགས་པ་རྣམས་ལ་བསྒྲུབ་པར་དཀའ་བ་ནི་དེ་ལས་བཟློག་པའོ། །

[Block 3635]
སྒྲུབ་པ༌[^1428]དེ་ཡང་རྣམ་པ་གཉིས་ཏེ།

[Block 3636 [VERSE]]
བློ་རྟུལ་མངོན་ཤེས་བུལ་བ་སྟེ། །
ཅིག་ཤོས་ཀྱིས་ནི་མངོན་ཤེས་མྱུར། །

[Block 3637]
དབང་པོ་རྟུལ་པོ་ནི་སྒྲུབ་པར་སླ་བའམ་དཀའ་ཡང་རུང་སྟེ། མངོན་པར་ཤེས་པ་བུལ་བ་ཡིན་ནོ། །

[Block 3638]
དབང་པོ་རྣོན་པོ་ནི་མངོན་པར་ཤེས་པ་མྱུར་བ་ཡིན་ནོ། །

[Block 3639]
དེ་ལྟར་ན་སྒྲུབ་པའི་གཞི་ཡིན་ནོ། །

[Block 3640 [HEADING]]
### བྱང་ཆུབ་ཀྱི་ཕྱོགས་དང་མཐུན་པ་སུམ་ཅུ་རྩ་བདུན། ^6-5-0

[Block 3641]
ཡང་ལམ་དེ་ཉིད་བྱང་ཆུབ་ཀྱི་ཕྱོགས་དང་མཐུན་པ་སུམ་ཅུ་རྩ་བདུན་དུ་གསུངས་ཏེ། དེ་ལ་ཟད་དང་མི་སྐྱེ་ཤེས་པ་ནི། །བྱང་ཆུབ། ཟད་པ་དང་མི་སྐྱེ་བ་ཤེས་པ་ནི་གང་ཟག་གི༌[^1429]བྱེ་བྲག་གིས་རྣམ་པ་གསུམ་མོ། །

[Block 3642]
དེ་དང་མཐུན་ཉིད་ཕྱིར། སུམ་ཅུ་རྩ་བདུན་དེའི་ཕྱོགས་མཐུན། བྱང་ཆུབ་དང་མཐུན་པའི་ཕྱིར། མིང་གི༌[^1430]སྒོ་ནས། བྱང་ཆུབ་ཀྱི་ཕྱོགས་དང་མཐུན་པ་སུམ་ཅུ་རྩ་བདུན་ཞེས་བྱའོ། །

[Block 3643]
རྫས་སུ་བཅུ།[^1431] བྱང་ཆུབ་ཀྱི་ཕྱོགས་དང་མཐུན་པ་ཐམས་ཅད་ནི་རྫས་བཅུ་པོ་འདི་ལྟ་སྟེ།

[Block 3644 [VERSE]]
དད་དང་བརྩོན་འགྲུས་དྲན་པ་དང་། །
ཤེས་རབ་ཏིང་འཛིན་བཏང་སྙོམས་དགའ། །
རྟོག་དང་ཚུལ་ཁྲིམས་ཤིན་ཏུ་སྦྱངས། །
དེ་ལྟར་དེ་དག་ནི་རྫས་བཅུའོ། །

[Block 3645]
ཇི་ལྟར་བྱས་ནས་ཤེ་ན།
--- END BLOCKS ---
