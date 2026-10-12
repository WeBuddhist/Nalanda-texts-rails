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
[Block 2766]
ཆོས་ནི་གཡོ་ཡིས་བྱེད་པར་འགྱུར། །ཞེས་པ་ནི་གཡོ་སྒྱུའི༌[^1813]དབང་གིས་ཆོས་བྱེད་པ་སྟེ་སོ་བྱ་བཞིན་ནོ། །

[Block 2767]
སེམས་ཅན་སླུ་བར་བྱེད་པ་ཞེས་བྱ་བའི༌[^1814]དོན་ཏོ། །

[Block 2768]
དེས་ནི་འདུས་པ་ཞེས་བྱ་བ་ལ་སོགས་པས་དམ་ཚིག་ཉམས་པ་དང་ཡོངས་སུ་མི་ཤེས་པ་དག་བསྟན་ཏོ། །

[Block 2769]
མངོན་སུམ་ཞེས་བྱ་བ་ལ་སོགས་པས་རྡོ་རྗེ་སློབ་དཔོན་ལ་སྨོད་པར་བྱེད་པ་བསྟན་ཏོ། །

[Block 2770]
སྐད་ཅིག་ཅེས་པ་ནས་བྱམས་པའི་སེམས་མེད་པ་དང་། བགྲོད་མིན་ལ་འགྲོ་བ་དང་། མཚམས་མེད་པ་བྱེད་པ་དང་། མི་དགེ་བའི་ལས་ཀྱི་ལམ་ལ་སྤྱོད་པར་བྱེད་པ་སྟོན་པར་བྱེད་དོ། །

[Block 2771]
དེ་ཉིད་ཡེ་ཤེས་པ་ནི་རྣམ་པ་གཉིས་ཏེ། བསྐྱེད་པའི་རིམ་པ་ལྷག་པར་མོས་པའི་སྦྱོར་བས་སྟོང་པ་ཉིད་མངོན་དུ་བྱེད་པ་དང་། རྫོགས་པའི་རིམ་པ་ལ་རྡོ་རྗེ་བཟླས་པ་ལ་སོགས་པའི་མཚན་ཉིད་དོ། །

[Block 2772]
ཏིང་ངེ་འཛིན་ནི་རིམ་པ་གཉིས་ཀྱི་མཚན་ཉིད་དོ། །

[Block 2773]
རྟོགས་པ་མེད་པའི་འབྲས་བུ་བསྟན་པར་བྱ་བའི་ཕྱིར་རོ།[^1815] །

[Block 2774]
ཉེས་པ་ཅུང་ཟད་ཅེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ་སློང༌[^1816]མོའི་ཁྱིམ་ནས་གལ་ཏེ་བཟའ་བ་ཙམ་མ་རྙེད་ན་དེའི་ཚེ། ལེའུ་གསུམ་པ་ལ་སོགས་པ་ནས་གསུངས་པའི་མངོན་སྤྱོད་ཀྱི་ལས་བྱེད་པར་འགྱུར་རོ། །

[Block 2775]
གལ་ཏེ༌[^1817]དེས་གྲུབ་པར་གྱུར་ན་དེའི་ཚེ་སྐྱོན་མེད་དོ། །

[Block 2776]
འོན་ཀྱང་རྣལ་འབྱོར་ནི་བསྐྱེད་པའི་རིམ་པའི་ཏིང་ངེ་འཛིན་ཏོ། །

[Block 2777]
སྦྱོར་བ་ནི་རྫས་ལ་སོགས་པ་ཇི་ལྟ་བ་བཞིན་དུ་སྦྱོར་བའོ། །

[Block 2778]
དེ་དག་གི་དམན་པ་ནི་བྲལ་བའི་ཕྱིར་འགྲུབ་པར་མི་འགྱུར་རོ། །

[Block 2779]
སྔགས་པ་ནི་བཤད༌[^1818]པའི་ཚིག་སྟེ་བླུན་པོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2780]
དེ་ཡི་སྦྱོར་བ་ལ་མཁས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་འདིས་སྒོམ་པ༌[^1819]མེད་པས་རང་གི་བསྟན་པ་ལ་སྐུར་བ་འདེབས་ཤིང་། ཕྱིའི་བསྟན་བཅོས་ལ་བརྟེན་ཏེ་དེའི་སྦྱོར་བ་སློབ་པས་རང་གི་དམ༌[^1820]ཚིག་དང་བྲལ་ཞིང་རང་དབང་དུ་སོང་བས་སྔགས་ལ་སོགས་པའི་སྦྱོར་བས་འཚོ་བ༌[^1821]ཚོལ་ཞིང་། གང་དུ་རྙེད་པ་ཡོད་པ་དེ་ཉིད་དུ་འཇུག་པར་འགྱུར་ཏེ་བཟོ་བོ་བཞིན་ནོ། །

[Block 2781]
དེ་རྣམས་རྗེས་སུ་གཟུང་བར་བྱ་བའི་ཕྱིར། གསང་བ་དགོངས་པས་བཤད་པ་ཡིན། །ཞེས་པ་ནི་སེམས་ཅན་དེ་རྣམས་རྗེས་སུ་གཟུང་བར་བྱ་བའི་ཕྱིར་དགོངས་པས་ལུང་བསྟན་ཏེ། རྩ་བའི་རྒྱུད་ཀྱི་དཀའ་བའི་ཚིག་ཕྱེ་ནས་ཇི་ལྟ༌[^1822]བ་བཞིན་དུ་དོན་ངེས་པར་གཟུང་བས་སོ། །

[Block 2782]
[^1823]

[Block 2783 [HEADING]]
#### ཚིག་གི་དོན། ^1-8-1-0

[Block 2784]
དེ་ལྟར་ཞེས་བྱ་བ་ལ་སོགས་པས་ཡན་ལག་གི་དོན་དབྱེ་བར་བྱ་བའི་ཕྱིར་བཤད་པར་བྱེད་དེ། འདིར་ཞེས་བྱ་བ་ལ་སོགས་པས་གླེང་གཞིའི་ཚིག་གི་གནས་སྐབས་སོ། །

[Block 2785]
སྡུད་པ་པོ་འཕགས་པ་ཕྱག་ན་རྡོ་རྗེ་ཞེས་པ་ནི་ལེའུ་བཅུ་བདུན་པ་ལས་ཀྱེའི༌[^1824]རྡོ་རྗེ་ཆོས་ཀྱི་རྣམ་གྲངས་འདི་ལོང་ཤིག༌[^1825]ཅེས་འཆད་པར་འགྱུར་རོ། །

[Block 2786]
དེ་བས་ནི་སྡུད་པ་པོར་གྱུར་པ་ནི་ཆོས་ཀྱི་མཛོད་དེ་ཉིད་ལ་གཏད་པའི་ཕྱིར་རོ། །

[Block 2787]
འདི་སྐད་བྱ་བ༌[^1826]ཚིག་གི་ཕྲད་ཀྱིས༌[^1827]རྒྱུད་ཀྱི་དོན་མ་ལུས་པ་མཚོན་པར་བྱེད་པ་ནི་རྒྱུད་ཀྱི་དོན་མ་ལུས་པ་སེམས་ལ་བཞག་ནས་འདི་སྐད་ཅེས་གསུངས་ཏེ། ཚིག་ཕྲད་རྣམས་ལ་དོན་དུ་མ་ཡོད་པའི་ཕྱིར་རོ། །

[Block 2788]
བདག་ཉིད་ཀྱིས་ནི་དངོས་སུ་ཐོས་ཀྱི་བརྒྱུད་པས༌[^1828]ནི་མ་ཡིན་ཞེས་བྱ་བ་ལ་དངོས་སུ་ཐོས་པས་འཁྲུལ་པ་མེད་པ་ཉིད་སྟོན་ཏེ། བརྒྱུད་པའི༌[^1829]སྒོ་ནས་ཐོས་པ་ལ་ནི་དེ་ལས་གཞན་པར་འགྱུར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2789]
རྟོགས་པ༌[^1830]མ་ཡིན་པ་ཞེས་པ་ནི་ཐོས་པ་ཙམ་གཙོ་བོ་ཡིན་པས་སོ། །

[Block 2790]
རྟོགས་པ་ཡོད་ན་བསྒོམ་པའི་རང་བཞིན་གྱི་ཤེས་རབ་ཀྱི་ངེས་པ་རྙེད་ནས་དེའི་ངོ་བོར་གནས་པའི་ཕྱིར་རོ། །

[Block 2791]
སྡུད་པས་ཅི་ཞིག་བྱ་ཞེས་པའི་ཐ་ཚིག་གོ། །

[Block 2792]
དུས་གཅིག་ན་ཞེས་པ་ལ་སོགས་པ་འདིས་ཐོས་པ་མང་བ་ལ་སོགས་པ་ཡོན་ཏན་གསུམ་བསྟན་པའོ། །

[Block 2793]
རྒྱུད་ཀྱི་དཀོན་པ་ཉིད་ནི་རྒྱུད་ཀྱི་ཡོན་ཏན་ནོ། །

[Block 2794]
ཐོས་པ་མང་བ་དང་ཤེས་རབ་ཕུལ་དུ་བྱུང་བ་དག་ནི་སྡུད་པ་པོའི་ཡོན་ཏན་ནོ། །

[Block 2795]
གང་ལས་ཞེས་བྱ་བ་ལ་སོགས་པས་གླེང་གཞི་གསུངས་སོ། །

[Block 2796]
གང་གི་ཕྱིར་སྟོན་པ་དང་གནས་དང་ཉན་པ་ཕུན་སུམ་ཚོགས་པ་གཙོ་བོ་ཡིན་པའི་ཕྱིར་གླེང་གཞི་ཡིན་ནོ། །

[Block 2797]
དེ་ལ་སྟོན་པ་ཕུན་སུམ་ཚོགས་པས་རྒྱུད་ཀྱི་ཆེ་བ་ཉིད་བསྟན་ཏོ། །

[Block 2798]
གནས་ཕུན་སུམ་ཚོགས་པ༌[^1831]ཡོངས་སུ་དག་པས་སངས་རྒྱས་ཀྱི་ཞིང་རྣམས་སུ་ཚད་བསྟན་པས་ཚད་མ་ཉིད་དུ་འགྱུར་རོ། །

[Block 2799]
འཁོར་ཕུན་སུམ་ཚོགས་པས་འདི་དང་ལྷན་ཅིག་ཐོས་ཞེས་པས་དབང་པོ་ཉིད་བསྟན་པ་ཡིན་ནོ། །

[Block 2800]
བཅོམ་ལྡན་འདས་ཞེས་བྱ་བ་ལ་སོགས་པས་དེ་ཉིད་བསྟན་ཏོ། །

[Block 2801]
སྐལ་བ་དང་ལྡན་པའི་ཕྱིར་ཞེས་པ་ནི། ཇི་སྐད་དུ།

[Block 2802 [VERSE]]
དབང་ཕྱུག་མ་ལུས་པ་ཉིད་དང་། །
ཡེ་ཤེས་དང་ནི་གྲགས་པ་དཔལ། །
ཆགས་བྲལ་རྩོལ་བ་ཉིད་དང་ནི། །
བཅོམ་པ་རྣམ་པ་དྲུག༌[^1832]ཏུ་གྲགས། །

[Block 2803]
ཞེས་འབྱུང་བས་སོ། །

[Block 2804]
དེ་རྣམས་དང་ལྡན་པའི་ཕྱིར་ན་བཅོམ་ལྡན་འདས་སོ། །

[Block 2805]
མི་མཐུན་པ་ལ་རྣམ་པ་གཉིས་ཏེ། ཕྱི་དང་ནང་གི་དག་གོ། །
--- END BLOCKS ---
