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

[Block 1651]
བདེ་འགྲོའི་ཚེ་ཚད་བཤད་ཟིན་ཏོ། །

[Block 1652]
ངན་འགྲོའི་བརྗོད་པ།

[Block 1653 [VERSE]]
ཡང་སོས་ལ་སོགས་དྲུག་རིམ་བཞིན། །
འདོད་ལྷའི་ཚེ་དང་ཉིན་ཞག་མཉམ། །

[Block 1654]
འདོད་པ་ན་སྤྱོད་པའི་ལྷ༌[^626]རིས་དྲུག་པོ་དེ་དག་གི་ཚེ་ཇི་ཙམ་བཤད་པ་དེ་དང་གོ་རིམས་བཞིན་དུ་ཡང་སོས་ལ་སོགས་པ་དྲུག་གི་ཉིན་ཞག་དང་མཉམ་པའོ། །

[Block 1655 [VERSE]]
དེས་ན༌[^627]དེ་དག་རྣམས་ཀྱི་ཚེ། །
འདོད་པའི་ལྷ་དང་འདྲ་བ་ཡིན། །

[Block 1656]
རང་གི་ཉིན་ཞག་གི་ལོ་ལྔ་བརྒྱ་ཡང་སོས་ཀྱི་ནས་ཚ་བའི༌[^628]ཚེ་ལོ་ཁྲི་དྲུག་སྟོང་ཡིན་པའི་བར་དུའོ། །

[Block 1657]
རབ་ཏུ་ཚ༌[^629]ཕྱེད། རབ་ཏུ་ཚ་བ་ན་ནི་ཚེའི་ཚད༌[^630]བར་གྱི་བསྐལ་པ་ཕྱེད་དོ། །

[Block 1658]
མནར་མེད་ནི། བར་གྱི་བསྐལ་པའོ། །

[Block 1659]
དུད་འགྲོ་རྣམས་ཀྱི་ནི་ངེས་པ་མེད་དེ། དུད་འགྲོ་རྣམས། མཆོག་རིང་བསྐལ་པའོ།[^631] །

[Block 1660]
ཡི་དགས་རྣམས། ཟླ་བ་ཉིན་ཞག་གིས་ལྔ་བརྒྱའོ། །

[Block 1661]
མི་རྣམས་ཀྱི་ཟླ་བ་ནི་ཡི་དགས་ཀྱི་ཉིན་ཞག་གཅིག་སྟེ།

[Block 1662 [VERSE]]
དེས་ན་ཚེ་ལོ་ལྔ་བརྒྱའོ། །
ཡང་གྲང་བའི་དམྱལ་བ་ལ།
ཏིལ་སྦྱང༌[^632]ནང་ནས་ལོ་བརྒྱ་ཞིང་། །
ཏིལ་གཅིག་ཕྱུང་བས་ཟད་གྱུར་པ། །
ཆུ་བུར་ཅན་གྱི་ཚེ་ཡིན་ཏེ། །
གཞན་གྱི་ཚེ་ནི་ཉི་ཤུར་བསྒྱུར། །

[Block 1663]
དེ་དག་གི་ཚེའི་ཚད་ནི་དཔེ་ཙམ་གྱིས་གསུངས་ཏེ། མ་ག་དྷཱའི༌[^633]ཏིལ་གྱིས་སྦྱང་བ༌[^634]ཁལ་བརྒྱད་ཅུ་པ་ནས་ལོ་བརྒྱ་འདས་ཞིང་ཏིལ་རེ་རེ་བོར་ན། དེ་ཟད་པ་དང་མཉམ་པ་ནི་ཆུ་བུར་ཅན༌[^635]གྱི་ཚེའོ། །

[Block 1664]
དེའི་འོག་མ་གཞན་དག་གི་ནི་ཉི་ཤུར་བསྒྱུར་རོ། །

[Block 1665]
དེ་ལྟར་ཚེ་དང་ལྡན་པའི་སེམས་ཅན་དེ་དག་ཚེ་ཡོངས་སུ་མ་རྫོགས་པར་བར་མ་དོར་འཆི་བ་ཡོད་དམ། འོན་ཏེ་མེད་ཅེ་ན། ཐམས་ཅད་ལ་ཡོད་དེ། སྒྲ་མི་སྙན་མ་གཏོགས་པར་འཆི། །སྒྲ་མི་སྙན་པ་ཁོ་ནའི་སེམས་ཅན་རྣམས་ཚེ་ངེས་པ་ཡིན་ཏེ། གཞན་དག་ནི་མ་ཡིན་ནོ། །

[Block 1666 [HEADING]]
### གཟུགས་དང་མིང་དང་དུས་ཀྱི་མཐའ། ^3-5-0

[Block 1667]
དཔག་ཚད་དང་ལོ་ལ་སོགས་པའི༌[^636]གྲངས་ཀྱིས་ལུས་དང་ཚེ་ལ་སོགས་པ་བཤད་ཟིན་ནས། ཡང་ཐམས་ཅད་ཀྱི་རྣམ་པར་གཞག་པ་ཡང་མིང་ཡིན་པས་དེ་རབ་ཏུ་སྟོན་པའི་དོན་དུ་དང་པོའི་རིམ་པ་བརྩམ༌[^637]མོ། །

[Block 1668]
གཟུགས་མིན༌[^638]དུས་མཐའ་རྡུལ་ཡིག་དག །[^639]སྐད་ཅིག །གཟུགས་ཀྱི་མཐའ་ནི་རྡུལ་ཕྲ་རབ་ཡིན་ནོ། །

[Block 1669]
མིང་གི་ནི་ཡི་གེའོ། །

[Block 1670]
དུས་ཀྱི་ནི་སྐད་ཅིག་གོ། །

[Block 1671 [HEADING]]
### དཔག་ཚད་ཀྱི་ཚད། ^3-6-0

[Block 1672 [VERSE]]
དེ་ལ་ཕྲ་རབ་རྡུལ་དང་ནི། །
རྡུལ་ཕྲན་དང་ནི་དེ་བཞིན་དུ། །
ལྕགས་ཆུ་རི་བོང་ལུག་དང་གླང་། །

[Block 1673 [VERSE]]
ཉི་ཟེར་རྡུལ་དང་སྲོ་མ་དང་། །
དེ་ལས་བྱུང་དང་དེ་བཞིན་དུ། །
སོར་ཚིགས་ཞེས་བྱ༌[^640]གོང་བདུན་བསྒྱུར། །

[Block 1674]
རྡུལ་ཕྲ་རབ་ལ་སོགས་པ་འདི་དག་ནི་རྡུལ་ཕྲན་ལ་སོགས༌[^641]བདུན་འགྱུར་དུ་རིག་པར་བྱ་སྟེ། འདི་ལྟ་སྟེ། རྡུལ་ཕྲ་རབ་བདུན་ལ་རྡུལ་ཕྲན་ནས། ནས་བདུན་ལ་སོར་ཚིགས་ཀྱི་བར་རོ། །

[Block 1675]
ངོས་སུ་བྱས་ནས་ནི།

[Block 1676 [VERSE]]
སོར་ནི་ཉི་ཤུ་བཞི་ལ་ཁྲུ། །
ཁྲུ་བཞི་ལ་ནི་གཞུ་གང་ངོ་། །

[Block 1677]
འདོམ་གང་ངོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1678 [VERSE]]
དེ་དག་ལྔ་བརྒྱ་རྣམས་ལ་ནི། །
རྒྱང་གྲགས་དེ་ལ་དགོན་པར་འདོད། །
དེ་བརྒྱད་དཔག་ཚད་ཅེས་བྱའོ། །

[Block 1679]
ཞེས་བྱ་བར་གསུངས་སོ། །

[Block 1680]
དཔག་ཚད་ཀྱི་ཚད་བཤད་ཟིན་ཏོ། །

[Block 1681 [HEADING]]
### ལོའི་ཚད། ^3-7-0

[Block 1682]
ད་ནི་ལོའི་བརྗོད་པར་བྱ་སྟེ།

[Block 1683 [VERSE]]
སྐད་ཅིག་མ་བརྒྱ་ཉི་ཤུ་ལ། །
དེ་ཡི་སྐད་ཅིག་དེ་དག་ཀྱང་། །
དྲུག་ཅུ་ལ་ནི་ཐང་ཅིག༌[^642]གོ། །
ཡུད་ཙམ་ཉིན་ཞག་ཟླ་གསུམ་ནི། །

[Block 1684 [VERSE]]
གོང་ནས་གོང་དུ་སུམ་ཅུར་བསྒྱུར། །
ཞག་མི་ཐུབ་པ་དང་བཅས་པའི། །
ཟླ་བ་བཅུ་གཉིས་ལ་ལོ་གཅིག །

[Block 1685]
ལོ་ལ་ཞག་གི་ཤོལ་དྲུག་འདོར་ཏེ། འདི་ལྟ་སྟེ།
--- END BLOCKS ---
