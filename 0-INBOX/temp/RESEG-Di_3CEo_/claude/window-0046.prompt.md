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
[Block 1611]
གཞན་དག་ན་རེ་གོང་མ་ཉིས་འགྱུར་རོ་ཞེས་ཟེར་རོ། །

[Block 1612]
བསམ་གཏན་དང་པོ་ནི་གླིང་བཞི་པ་ཙམ་མོ། །

[Block 1613]
བསམ་གཏན་གཉིས་པ་དག༌[^611]

[Block 1614]
གསུམ་པ་དང་།

[Block 1615]
བཞི་པ་ནི་སྟོང་ཆུང་ངུའི་དང་། སྟོང་གཉིས་པ་དང་། སྟོང་གསུམ་པའི་འཇིག་རྟེན་གྱི་ཁམས་ཙམ་མོ། །

[Block 1616 [HEADING]]
#### སྟོང་ཆུང་ངུ་ལ་སོགས་པའི་འཇིག་རྟེན་གྱི་ཁམས། ^3-2-8-0

[Block 1617]
ཡང་སྟོང་ཆུང་ངུ་ལ་སོགས་པའི་འཇིག་རྟེན་གྱི་ཁམས་དེ་དག་གང་ཞེ་ན།

[Block 1618 [VERSE]]
གླིང་བཞི་པ་དང་ཉི་ཟླ་དང་། །
རི་རབ་དང་ནི་འདོད་ལྷ་དང་། །
ཚངས་པའི་འཇིག་རྟེན་སྟོང་ལ་ནི། །
སྟོང་ནི་སྤྱི་ཕུད་ཡིན་པར་འདོད། །

[Block 1619]
འཛམ་བུའི་གླིང་ནས་ཚངས་པའི་འཇིག་རྟེན་གྱི་བར་སྟོང་ནི༌[^612]སྟོང་སྤྱི་ཕུད་ཀྱི་འཇིག་རྟེན་གྱི་ཁམས་ཞེས་བྱའོ། །

[Block 1620 [VERSE]]
དེ་སྟོང་ལ་ནི་སྟོང་གཉིས་པ། །
བར་མའི་འཇིག་རྟེན་ཁམས་ཡིན་ནོ། །
དེ་སྟོང་ལ་ནི་སྟོང་གསུམ་མོ། །

[Block 1621]
འདི་ཐམས་ཅད་ཀྱང་མཉམ་དུ་འཇིག་ཅིང་འབྱུང་བ་ཡིན། མཉམ་དུ་འབྱུང་བ་ཞེས་བྱ་བ་ནི་འོག་ཏུ་བཤད་པར་བྱའོ། །

[Block 1622 [HEADING]]
### ལུས་ཀྱི་ཚད། ^3-3-0

[Block 1623]
དེ་ལ་ཡང་དེ་ན་སེམས་ཅན་རྣམས་ཀྱི་ཡོང༌[^613]སྣོད་བཞིན་དུ་ཚད་ཀྱི་བྱེ་བྲག་ཡོད་པས་བརྗོད་དེ།

[Block 1624 [VERSE]]
འཛམ་བུའི་གླིང་པ་རྣམས་ཀྱི་ཚད། །
ཁྲུ་བཞི་པ་དང་ཕྱེད་དང་བཞི། །
ཤར་དང་བ་ལང་སྤྱོད་དང་ནི། །
བྱང་ཞེས་བྱ་བ་ཉིས་འགྱུར་སྐྱེད།[^614] །

[Block 1625]
དེ་དག་ཀྱང་ཁྲུ་བརྒྱད་དང་། བཅུ་དྲུག་དང་། སུམ་ཅུ་རྩ་གཉིས་པ་དག་རིམ་པ་བཞིན་དུའོ། །

[Block 1626 [VERSE]]
འདོད་དང་ལྡན་པ་ལྷ་ཡི་ལུས། །
བཞི་ཆ་ནས་ནི་རྒྱང་གྲག༌[^615]དག །
ཕྱེད་དང་གཉིས་ཀྱི་བར་དུ་བསྐྱེད།[^616] །

[Block 1627]
རྒྱང་གྲག༌[^617]བཞི་ཆ་གཅིག་ནི་དང་པོའི་ཡིན་ཏེ། ཕྱི་མ་རྣམས་ཀྱི་ནི་ཕྱེད་དང་གཉིས་ཀྱི་བར་རོ། །

[Block 1628]
གཟུགས་ཅན་དང་པོ་དཔག་ཚད་ཕྱེད། །བསམ་གཏན་དང་པོའི་ལུས་ནི་དཔག་ཚད་ཕྱེད་ཙམ་མོ། །

[Block 1629]
དེ་ཡི་གོང་མ་ཕྱེད་ཕྱེད་བསྐྱེད། །གནས་གསུམ་དག་ནས་འོད་ཆུང་རྣམས་ཀྱི་ནི་དཔག་ཚད་གཉིས་ཀྱི་བར་རོ། །

[Block 1630 [VERSE]]
འོད་ཆུང་རྣམས་ཀྱི་ལྟག༌[^618]ཡན་ཆད། །
ལུས་ནི་ཉིས་འགྱུར་ཉིས་འགྱུར་བསྐྱེད། །
སྤྲིན་མེད་དཔག་ཚད་གསུམ་དོར་རོ། །

[Block 1631]
དགེ་རྒྱས་པ་རྣམས་ཀྱི་ནི་དྲུག་ཅུ་རྩ་བཞི་ཡིན་པའི་བར་དུའོ། །

[Block 1632]
སྤྲིན་མེད་རྣམས་ཀྱི་ནི་ཉིས་འགྱུར་དུ་བསྒྱུར་ཏེ། དེ་ནས་དཔག་ཚད་གསུམ༌[^619]ཁྲི་ན་དཔག་ཚད་བརྒྱ་ཉི་ཤུ་རྩ་ལྔའོ།[^620] །

[Block 1633]
དེ་ཡན་ཆད་ཀྱང་ཉིས་འགྱུར་ཉིས་འགྱུར་རོ། །

[Block 1634 [HEADING]]
### ཚེའི་ཚད། ^3-4-0

[Block 1635 [VERSE]]
ལུས་དག་གི་བཤད་ནས་ཚེའི་བརྗོད་དོ།[^621] །
སྒྲ་མི་སྙན་ན་ཚེ་སྟོང་སྟེ། །
གཉིས་ན་ཕྱེད་ཕྱེད་སྤངས་པའོ། །

[Block 1636]
བ་ལང་སྤྱོད་པ་རྣམས་ཀྱི་ནི་ལོ་ལྔ་བརྒྱའོ། །

[Block 1637]
ཤར་གྱི་ལུས་འཕགས་རྣམས་ཀྱི་ནི་ཉིས་བརྒྱ་ལྔ་བཅུའོ། །

[Block 1638 [VERSE]]
འདི་ན༌[^622]མ་ངེས་ཐ་མར་ནི། །
ལོ་བཅུ་དང་པོ་དཔག་ཏུ་མེད། །

[Block 1639]
བསྐལ་པ་དང་པོ་པ་རྣམས་ཀྱི་སྟོང་ལ་སོགས་པར་བགྲང་བར་མི་ནུས་པའི་ཕྱིར་དཔག་ཏུ་མེད་པའོ། །

[Block 1640]
མི་རྣམས་ཀྱི་བཤད་ནས་ལྷ་རྣམས་ཀྱི་བརྗོད་པར་བྱ་སྟེ།

[Block 1641 [VERSE]]
མི་རྣམས་ཀྱི་ལོ་ལྔ་བཅུ་ལ། །
འདོད་པ་དག་གི་ལྷ་རྣམས་ལས། །
འོག་མ་དག་གི་ཉིན་ཞག་གཅིག །
དེས་ན་ཚེ་ལོ་ལྔ་བརྒྱའོ། །
གོང་མ་གཉིས་ཀ་ཉིས་འགྱུར་རོ། །

[Block 1642]
སུམ་ཅུ་རྩ་གསུམ་པ་རྣམས་ལས་བརྩམས་ཏེ། ཉིན་ཞག་ཀྱང་ཉིས་འགྱུར་ཡིན་ལ་ཚེ་ཡང་ཉིས་འགྱུར་རོ། །

[Block 1643]
འདོད་པ་དང་ལྡན་པ་རྣམས་ཀྱི་ཚེའི་ཚད་བཤད་ཟིན་ཏོ། །

[Block 1644 [VERSE]]
གཟུགས་ཅན་ཉིན་མཚན་མེད་ཚེ་ནི། །
རང་ལུས་གཞལ་བའི་སྐལ་བ༌[^623]ཡིས། །

[Block 1645]
གང་དག་གི༌[^624]ལུས་དཔག་ཚད་ཇི་སྙེད་པ་དེ་དག་གི་ཚེ་ཡང་བསྐལ་པ་དེ་སྙེད་དོ། །

[Block 1646 [VERSE]]
གཟུགས་མེད་བསྐལ་པ་སྟོང་ཕྲག་ནི། །
ཉི་ཤུ་ལྷག་པས་ལྷག་པ་ཡིན། །

[Block 1647]
གཟུགས་མེད་པ་རྣམས་ཀྱི་ནི་དང་པོ་བསྐལ་པ་ཉི་ཁྲི་ནས་སྲིད་པའི་རྩེ་མོ་ན་བརྒྱད་ཁྲིའི་བར་རོ། །

[Block 1648]
ཡང་འདིར་བསྐལ་པ་ཆེན་པོ་གང་སྟེ།

[Block 1649 [VERSE]]
འོད་ཆུང་ནས་བཟུང་བསྐལ་ཆེན་ཏེ། །
དེ་ཡི་འོག་མ་ཕྱེད་ཡིན་ནོ། །

[Block 1650]
བསམ་གཏན་དང་པོའི་ས་པ༌[^625]རྣམས་ཀྱི་ནི་བར་གྱི་བསྐལ་པ་བཞི་བཅུ་ལ་བསྐལ་པར་བྱས་ནས་བརྗོད་པར་བྱའོ། །
--- END BLOCKS ---
