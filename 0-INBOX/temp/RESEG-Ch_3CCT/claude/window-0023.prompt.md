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
[Block 806]
དུས་ཀྱང་གང་གི་ཚེ་འབྱུང་ཞེ་ན།

[Block 807 [VERSE]]
འོད་གསལ་བ་ནི་མཐར་ཕྱིན་པ། །
དེ་ཚེ་ཟུང་འཇུག་བསྒོམ་པར་བྱ། །

[Block 808]
ཞེས་པ་གང་གི་ཚེ་འོད་གསལ་བ་མཐར་ཕྱིན་པ་དེའི་ཚེ་ཟུང་དུ་འཇུག་པ༌[^320]བསྒོམ་པར་བྱའོ་ཞེས་བྱ་བར་དགོངས་སོ། །

[Block 809]
སྔོན་དུ་འགྲོ་བའང་གང་ཡིན་ཞེ་ན།

[Block 810 [VERSE]]
རིམ་པ་བཞི༌[^321]ནི་སྔོན་སོང་ནས། །
གང་ཞིག་འདི་ལ་གནས་པར་བྱ། །

[Block 811]
ཞེས་པ་གོ་སླའོ། །

[Block 812 [HEADING]]
## སྤྱོད་པ། ^3-0

[Block 813]
དེ་ལྟར་ལམ་དངོས་བཤད་ནས། ད་ནི་དེའི་གྲོགས་སྤྱོད་པ་བསྟན་པར་བྱ་སྟེ། དེ་བཤད་པ།

[Block 814 [VERSE]]
སྤྱོད་པ་དག་གི་སྦྱོར་བ་ལ། །
ངོ་བོ་དང་ནི་རྣམ་དབྱེ་དང་། །
ངེས་པའི་ཚིག་དང་རྣམ་གྲངས་དང་། །
རྒྱུ༌[^322]དང་དུས་དང་གནས་དང་གྲོགས། །

[Block 815]
ཞེས་པ་ལ་སོགས་པ་བཤད་པ་ལ། ཁྱད་པར་འདོད་ཡོན་ལྔ་ལ་སྤྱོད། །ཅེས་པ་ཁྱད་པར་ཅན་གྱི་སེམས་ཀྱིས༌[^323]ཟིན་པའི་ཡོན་ཏན་ལྔ་ལ་སྤྱོད་པ་འདི་ནི་རང་གི་ངོ་བོའོ། །

[Block 816 [VERSE]]
དུས་དང་བྱ་བ་བསམ་པ་ལ། །
ལྟོས་པའི༌[^324]དབང་དུ་སྤྱོད་པ་དགུ། །

[Block 817]
ཞེས་པ་འདི་ནི་དུས་ཀྱི་ཁྱད་པར་ལ་ལྟོས་པའི༌[^325]སྤྱོད་པ་གསུམ་མོ། །

[Block 818]
བྱ་བ་དང་བསམ་པ་ལའང་དེ་བཞིན་ནོ། །

[Block 819]
གསུམ་པོ་ཉིད་གང་ཞེ་ན། སྤྲོས་པ་དང་བཅས་པ་དང་། སྤྲོས་པ་མེད་པ་དང་།

[Block 820 [VERSE]]
ཤིན་ཏུ་སྤྲོས་པ་མེད་པའོ། །
འདི་ལ་ཅིའི་ཕྱིར་ཞེ་ན།
ཚིག༌[^326]དང་སྤྱད་དུ་ཡོད་ཕྱིར་ཏེ། །

[Block 821]
ཞེས་པ་གོ་སླའོ། །

[Block 822]
སྤྱོད་དང་ཀུན་རྫོབ་ལ་སོགས་པའི༌[^327]རྒྱུ་ནི་བཤད་ཟིན་ཏོ། །

[Block 823]
དུས་གང་གི་ཚེ་བྱ་ཞེ་ན།

[Block 824 [VERSE]]
བསམ་གཏན་ལས་སུ་རུང་བའི་ཚེ། །
སྤྱོད་པ་དག་ནི༌[^328]སྤྱད་པར་བྱ། །

[Block 825]
ཞེས་པ་རླུང་ལ་དབང་ཐོབ་པ། བྱང་ཆུབ་སེམས་དབབ་པ་དང་བཟློག་པ་ཤེས་པ་དང་། རིག་མ་རྟོག་པའི་སྦྱོར་བ་ལ་མཁས་པ་འདིའི་ཚེའོ། །

[Block 826]
གནས་གང་དུ་ཞེ་ན།

[Block 827 [VERSE]]
ས་ཕུག་རིམ་པ་གསུམ་པ་རུ། །
ཡང་དག་སྤྱོད་པ་སྤྱད་པར་བྱ། །

[Block 828]
ཞེས་པ་སྤྱོད་པའི་དབང་དུ་ས་ཕུག་གི་རིམ་པ་གསུམ་པར་སྤྱོད་པ༌[^329]བྱའོ་ཞེའོ། །

[Block 829]
དགེ་བ་གང་ཡིན་འདི་ཡི་གྲོགས། །ཞེས་པ་དད་པ་ལ་སོགས་པ་མཚུངས་པར་ལྡན་པ་དང་། ངོ་བོ་ཉིད་ལ་སོགས་པའི་སྦྱོར་བས་འདིའི་གྲོགས་སུའོ། །

[Block 830 [VERSE]]
གང་གིས་གང་ཞིག་གང་ལས་གྲོལ་བྱེད་པ། །
དེ་ཡི་རིགས་ཅན་དབང་དུ་བྱས་པའོ། །
གང་ཞིག་གིས་ནི་སྤྱོད་པ་ལྷུར་ལེན་དང་། །
སྤྱོད་པ་གྲོགས་ཙམ་དབང་དུ་བསྟན་པ་ཡིན། །

[Block 831]
ཞེས་པ་ནི་བར་སྐབས་ཀྱི་ཚིགས་སུ་བཅད་པའོ། །

[Block 832 [HEADING]]
## འབྲས་བུ། ^4-0

[Block 833]
གཞན་ཡང་འབྲས་བུ་ཞེས་བྱ་བ་གང་ཞིག་ཅེ་ན། ཐུན་མོང་མཆོག་གི་འབྲས་བུའོ། །ཞེས་པ་གང་ཞིག་གིས༌[^330]གང་ཐོབ་པར་བྱ་བ་དེ་ནི་འབྲས་བུའོ། །

[Block 834]
གང་ཡིན་ཞེ་ན། ཐུན་མོང་དང་མཆོག་གི་དངོས་གྲུབ་ཅེས་བྱའོ། །

[Block 835]
ལ་ལ་དག་ན་རེ།

[Block 836 [VERSE]]
རྒྱུ་དང༌[^331]ཐབས་དང་འབྲས་བུ་དང་། །
རྣམ་པ་གསུམ་པོ་འདི་ཁོ་ན། །

[Block 837]
ཞེས་པ་ནི། རྒྱུ་ནི་ཐེག་པ་ཆེན་པོའི་རིགས་ཅན་ནོ། །

[Block 838]
ཐབས་ནི་རྣམ་པ་གཉིས་སོ། །

[Block 839]
འབྲས་བུ་ནི་སྐུ་དང་ཡེ་ཤེས་སོ། །

[Block 840]
གཞན་ཡང་།

[Block 841 [VERSE]]
རྒྱུ་དང་ཐབས་དང་འབྲས་བུ་སྤང་བྱ་དང་། །
གོ་རིམས་གྲངས་ངེས་རྣམ་པ་དྲུག་ཁོ་ན། །

[Block 842]
ཞེས་པ་ནི། སྤང་བྱ་ནི་ཉོན་མོངས་པ་དང་ཤེས་བྱའི་སྒྲིབ་པའོ། །

[Block 843]
གྲངས་ངེས་པ་ནི་དངོས་པོའམ་བསམ་པའི་དབང་དུའོ། །

[Block 844]
གོ་རིམས་ནི་ཐོབ་བྱའི་དབང་དུ་སྟེ་འདི་ལྟར་དྲུག་ཁོ་ནའོ། །

[Block 845]
གཞན་ཡང་། མིང་དང་དགོས་པ་བྱེད་པའོ། །
--- END BLOCKS ---
