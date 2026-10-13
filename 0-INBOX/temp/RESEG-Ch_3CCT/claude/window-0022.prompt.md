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
[Block 771]
ཡང་བཤད་པ།

[Block 772 [VERSE]]
སློབ་པ་དང་ནི་མི་སློབ་པས། །
འོད་གསལ་གཉིས་སུ་ཤེས་པར་བྱ། །
རིལ་པོར་འཛིན་དང་རྗེས་སུ་གཞིག །
[^312]སློབ་པའི་འོད་གསལ་ཞེས་སུ་བཤད། །

[Block 773 [VERSE]]
མི་སློབ་པ་ནི་རྟོག་དང་བྲལ། །
དམིགས་མེད་རྣམ་དག༌[^313]གདོད་ནས་དག །
རྣམ་གྲངས་དཔག་ཏུ་མེད་པ་དག །
རྒྱལ་བ་སྲས་ཀྱིས་གསུངས་པ༌[^314]ཡིན། །

[Block 774]
ཞེས་པ་ནི་བར་སྐབས་ཀྱི་ཚིགས་སུ་བཅད་པའོ། །

[Block 775]
གཞན་ཡང་།

[Block 776 [VERSE]]
རྒྱུ་ནི་ཤེས་རབ་ཏིང་འཛིན་ཏེ། །
ཀུན་རྫོབ་བདེན་ལ་བརྟན་འགྱུར་བ། །
འདི་ནི་དུས་ཞེས་བཤད་པ་ཡིན། །
གང་ཚེ་ཐམས་ཅད་རང་བཞིན་མེད། །

[Block 777 [VERSE]]
མཐར་ཕྱིན་ཚད་ནི་བཤད་པའོ། །
འདི་ཡི་རབ་ཏུ་དགའ་བ་ཡི། །
ས་ལ་ཡང་དག་གནས་པའོ། །
དེ་ཡི་རྟོག་པ་སྤོང་བ་སྟེ། །

[Block 778 [VERSE]]
གོང་མ་ལ་ནི་མངོན་དུ་ཕྱོགས། །
གང་གིས་མཚན་མ་མེད་པ་ལ། །
མཆོག་ཏུ་གཞོལ་བའི་གང་ཟག་གིས། །
གཅིག་གིས་སྦྱོར་བས་ཡང་དག་འབྱུང་། །

[Block 779 [VERSE]]
དཔའ་བོས་བྱང་ཆུབ་ཤིང་དྲུང་དུ། །
མཉམ་ལ་གནས་པར་གྱུར་པ་ལ། །
འོད་གསལ་ལུང་བསྟན་གླེང་གཞི་ཡིན། །
དེ་བས་འོད་གསལ་མངོན་དུ་བྱ། །

[Block 780]
ཞེས་པ་ནི་བར་སྐབས་གྱི་ཚིགས་སུ་བཅད་པའོ། །

[Block 781]
དེ་ལྟར་འོད་གསལ་བ་རྒྱས་པར་བསྟན་ནས། ད་ནི་ཟུང་དུ་འཇུག་པ༌[^315]བསྟན་པར་བྱ་སྟེ། དེ་ལ་ཟུང་དུ་འཇུག་པའི་ངོ་བོ་འང་གང་ཡིན་ཞེ་ན།

[Block 782 [VERSE]]
གཉིས་མེད་ཡེ་ཤེས་གང་ཡིན་པ། །
ཟུང་དུ་འཇུག་པའི་ངོ་བོའོ། །

[Block 783]
ཞེས་པ་གང་རྟོག་པའི་རྣམ་པ་ཐམས་ཅད་དང་བྲལ་བའི་ཡེ་ཤེས་དེ་ནི་ཟུང་དུ་འཇུག་པའི་ངོ་བོའོ། །

[Block 784]
འདི་ལའང་ཅིའི་ཕྱིར་ཟུང་དུ་འཇུག་པ་ཞེས་བྱ་ཞེ་ན།

[Block 785 [VERSE]]
གཉིས་སུ་མེད་ཕྱིར་མི་གནས་ཕྱིར། །
གཉིས་དང་བྲལ་ཕྱིར་གཉིས་དམིགས་ཕྱིར། །
ཟུང་འཇུག་ཅེས་ནི་བཤད་པ་ཡིན། །

[Block 786]
ཞེས་པ་གཉིས་སུ་མེད་པའི་ཕྱིར་དང་། གཉིས་སུ་མི་གནས་པའི་ཕྱིར་དང་། གཉིས་དང་བྲལ་བའི་ཕྱིར་དང་། གཉིས་ལ་དུས་གཅིག་ཏུ་དམིགས་པའི་ཕྱིར་ཟུང་དུ་འཇུག་པའོ། །

[Block 787]
འདིའི་དབྱེ་བའང་དུ་ཞིག་ཅེ་ན།

[Block 788 [VERSE]]
སློབ་པ་དང་ནི་མི་སློབ་པས། །
ཟུང་དུ་འཇུག་པ་གཉིས་སུ་ཤེས། །

[Block 789]
ཞེས་པ་གང་ལ་སློབ་པ་དེ་ནི་སློབ་པའི་ཟུང་དུ་འཇུག་པའོ། །

[Block 790]
སློབ་པའི་འབྲས་བུ་ཡོངས་སུ་རྫོགས་པ་འདི་ནི་མི་སློབ་པའི་ཟུང་འཇུག་གོ། །

[Block 791]
རྣམ་གྲངས་ཀྱང་གང་ཡིན་ཞེས་བཤད་པ།

[Block 792 [VERSE]]
མི་སློབ་པ་དང་མཐར་ཕྱིན༌[^316]དང་། །
ཟུང་འཇུག་གཉིས་མེད་རྣམ་གྲངས་སོ། །

[Block 793]
ཞེས་པ་ནི་མི་སློབ་པའི་དབང་དུ་བྱས་པའོ། །

[Block 794]
ཆོས་དུ་དང་ལྡན་ཞེ་ན།

[Block 795 [VERSE]]
ཏིང་འཛིན་ཡིན་དང་གཉིས་ལ་དམིགས། །
སྐད་ཅིག་དམིགས་དང་ཐོགས་པ་མེད། །

[Block 796]
ཅེས་པ་རྣམ་པ་བཞི་པོ༌[^317]འདི་དང་ལྡན་པ་ནི་ཟུང་དུ་འཇུག་པའོ། །

[Block 797 [VERSE]]
གཞན་ལ་ཐལ་འགྱུར་སེལ་བ་ནི། །
འདི་ཡིས༌[^318]འགྲུབ་ཀྱིས་གཞན་དུ་མིན། །

[Block 798]
ཞེས་པ་ནི་གཞན་སེལ་བའོ། །

[Block 799]
འོ་ན་ཟུང་དུ་འཇུག་པ་ཞེས་བྱ་བའི་རྒྱུའང་གང་ཡིན་ཞེ་ན།

[Block 800 [VERSE]]
འོད་གསལ་བ་དང་རྣམ་པ་གཉིས། །
སློབ་པའི་ཟུང་དུ་འཇུག་པའི་རྒྱུ། །

[Block 801]
ཞེས་པ་འོད་གསལ་བ་དང་། ཤེས་རབ་དང་ཏིང་ངེ༌[^319]འཛིན་ནི་སློབ་པའི་ཟུང་དུ་འཇུག་པའི་རྒྱུའོ། །

[Block 802]
འོ་ན་མི་སློབ་པའི་ཟུང་དུ་འཇུག་པའི་རྒྱུའང་གང་ཡིན་ཞེ་ན། །

[Block 803 [VERSE]]
བྱང་ཆུབ་སེམས་དང་སྙིང་རྗེ་དང་། །
སྨོན་ལམ་དང་ནི་དེ་ཡི་རྒྱུ། །

[Block 804]
ཞེས་པ་སེམས་ཅན་ལ་ཕན་གདགས་པའི་བསམ་པ་དང་། སྙིང་རྗེ་དང་སེམས་ཅན་གྱི་དོན་ལ་དམིགས་པའི་སྨོན་ལམ་འདི་ནི་མི་སློབ་པའི་དབང་དུ་བྱས་པའོ། །

[Block 805]
འདི་ལའང་ཅིའི་ཕྱིར་རྒྱུ་ཞེ་ན། གང་ཞིག་ཡོད་ན་གང་འབྱུང་བ་དེ་ནི་དེའི་རྒྱུའོ། །

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
--- END BLOCKS ---
