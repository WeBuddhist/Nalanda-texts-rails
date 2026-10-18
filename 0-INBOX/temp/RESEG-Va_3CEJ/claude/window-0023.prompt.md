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
རྣ་བའི་དབང་པོའི་རྡུལ་ཕྲ་རབ་རྣམས་ནི་རྣ་བའི་བུ་གའི༌[^352]ནང་ན་གནས་སོ། །

[Block 807]
སྣའི་དབང་པོའི་རྡུལ་ཕྲ་རབ་རྣམས་ནི་མཚུལ་པའི་ནང་ན་གནས་ཏེ། དབང་པོ་དང་པོ་གསུམ་ནི་ཕྲེང་བ་བཞིན་དུ་གནས་སོ། །

[Block 808]
ལྕེའི་དབང་པོའི་རྡུལ་ཕྲ་རབ་རྣམས་ནི་ཟླ་བ་ཁམ་པ་ལྟ་བུ་ཡིན་ཏེ། ལྕེའི་དབུས་ན་སྐྲའི་རྩེ་མོའི་ཁྱོན་ཙམ་ཞིག་ལྕེའི་དབང་པོའི་རྡུལ་ཕྲ་རབ་དག་གིས་མ་ཁེབས་སོ་ཞེས་གྲག་གོ། །

[Block 809]
ལུས་ཀྱི་དབང་པོའི་རྡུལ་ཕྲ་རབ་རྣམས་ནི་ལུས་བཞིན་དུ་གནས་སོ། །

[Block 810]
མོའི་དབང་པོའི་རྡུལ་ཕྲ་རབ་རྣམས་ནི་རྔའི་སྦུབས་ལྟ་བུ་ཡིན་ནོ། །

[Block 811]
ཕོའི་དབང་པོའི་རྡུལ་ཕྲ་རབ་རྣམས་ནི་མཐེ་བོང་ལྟ་བུ་ཡིན་ནོ། །

[Block 812]
དེ་ལ་མིག་གི་དབང་པོའི་རྡུལ་ཕྲ་རབ་རྣམས་རེས་འགའ་ནི་ཐམས་ཅད་བསྟེན༌[^353]པ་དང་བཅས་པ་དག་ཡིན་ནོ། །

[Block 813]
རེས་འགའ་ནི་དེ་དང་མཚུངས་པ་དག་ཡིན་ནོ། །

[Block 814]
རེས་འགའ་ནི་ཁ་ཅིག་བསྟེན་པ་དང་བཅས་པ་དག༌[^354]ཡིན་ལ། ཁ་ཅིག་དེ་དང་མཚུངས་པ་ཡིན་ཏེ། ལྕེའི་དབང་པོའི་རྡུལ་ཕྲ་རབ་ཀྱི་བར་དུ་ཡང་དེ་དང་འདྲའོ། །

[Block 815]
ལུས་ཀྱི་དབང་པོའི་རྡུལ་ཕྲ་རབ་རྣམས་ནི་རིལ་གྱིས་བསྟེན་པ་དང་བཅས་པ་ནི་མེད་དེ། རབ་ཏུ་འབར་བའི་དམྱལ་བའི་ནང་ན་འཁོད་པ་རྣམས་ལ་ཡང་ལུས་ཀྱི་དབང་པོའི་རྡུལ་ཕྲ་རབ་ཚད་མེད་པ་ཞིག་དེ་དང་མཚུངས་པ་ཡིན་ཏེ། ཐམས་ཅད་ཀྱིས་རྣམ་པར་ཤེས་པ་བསྐྱེད་ན་ནི་ལུས་ཞིག་པར་འགྱུར་རོ་ལོ། །

[Block 816]
དབང་པོའི་རྡུལ་ཕྲ་རབ་བམ་ཡུལ་གྱི་རྡུལ་ཕྲ་རབ་གཅིག་གིས་རྣམ་པར་ཤེས་པ་སྐྱེད་པ༌[^355]ནི་མེད་དེ། རྣམ་པར་ཤེས་པའི་ཚོགས་ལྔ་པོ་དག་གི་རྟེན་དང་དམིགས་པ་ནི་བསགས་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 817]
དེ་ཉིད་ཀྱི་ཕྱིར་རྡུལ་ཕྲ་རབ་ནི་མི་མཐོང་བའི་ཕྱིར་བསྟན་དུ་མེད་པ་ཡིན་ནོ། །

[Block 818 [HEADING]]
##### རྣམ་པར་ཤེས་པའི་རྟེན། ^1-3-19-5-0

[Block 819]
ཅི་མིག་གི་རྣམ་པར་ཤེས་པ་ནས་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་བར་གྱི་ཁམས་དྲུག་པོ་བཤད་པ་གང་དག་ཡིན་པ་འདི་དག་ཇི་ལྟར་ལྔ་རྣམས་ཀྱི་ཡུལ་ད་ལྟར་ཡིན་ལ། ཐ་མའི་དུས་གསུམ་ཡིན་པ་ལྟར་རྟེན་ཀྱང་དེ་ལྟ་བུ་ཡིན་ནམ་ཞེ་ན། སྨྲས་པ་མ་ཡིན་ནོ། །

[Block 820]
འོ་ན་ཅི་ཞེ་ན། ཐ་མའི་རྟེན་འདས། ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་ཁམས་ཀྱི་རྟེན་ནི་འགགས༌[^356]མ་ཐག་པའི་ཡིད་དོ། །

[Block 821]
ལྔ་རྣམས་ཀྱི། དེ་དག་ལྷན་ཅིག་སྐྱེས་པའང་ཡིན། འང་ཞེས་བྱ་བའི་སྒྲ་ནི་འདས་པ་ཡང་ཡིན་པའོ། །

[Block 822]
དེ་ལ་མིག་གི་རྣམ་པར་ཤེས་པའི་ལྷན་ཅིག་སྐྱེས་པའི་རྟེན་ནི་མིག་ཡིན་པ་ནས་ལུས་ཀྱི་རྣམ་པར་ཤེས་པའི་བར་དུ་ཡང་ལུས་ཡིན་ལ། དེ་དག་གི་འདས་པའི་རྟེན་ནི་ཡིད་ཡིན་ནོ། །

[Block 823]
དེ་ལྟར་ན་རྣམ་པར་ཤེས་པའི་ཚོགས་ལྔ་པོ་དེ་དག་གི་རྟེན་ནི་དབང་པོ་གཉིས་གཉིས་ཡིན་ནོ། །

[Block 824]
དེ་གཉིས་ཀྱི་ཕྱིར་གང་མིག་གི་རྣམ་པར་ཤེས་པའི་རྟེན་གྱི་དངོས་པོར་ཡིན་པ་དེ་དེའི་མཚུངས་པ་དེ་མ་ཐག་པའི་རྐྱེན་གྱིས༌[^357]དངོས་པོར་ཡང་ཡིན༌[^358]ཞེ་ན། མུ་བཞི་སྟེ། མུ་དང་པོ་ནི་མིག་ཡིན་ནོ། །

[Block 825]
གཉིས་པ་ནི་ཆོས་ཀྱི་ཁམས་སེམས་ལས་བྱུང་བ་འདས་མ་ཐག་པ་ཡིན་ནོ། །

[Block 826]
གསུམ་པ་ནི་འདས་མ་ཐག་པའི་ཡིད་ཡིན་ནོ། །

[Block 827]
བཞི་པ་ནི་བཤད་པ་ལས་མ་གཏོགས་པའི་ཆོས་རྣམས་ཡིན་ཏེ། ལུས་ཀྱི་རྣམ་པར་ཤེས་པའི་བར་དུ་ཡང་དེ་བཞིན་དུ་རང་གི་དབང་པོ་བརྗོད་པར་བྱའོ། །

[Block 828]
ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་ནི་ཚིག་སྔ་མ་དང་སྦྱོར་བ་སྟེ། རེ་ཞིག་གང་རྟེན་གྱི་དངོས་པོར་ཡིན་པ་དེ་ནི་མཚུངས་པ་དེ་མ་ཐག་པའི་རྐྱེན་གྱི་དངོས་པོར་ཡང་ཡིན་ནོ། །

[Block 829]
མཚུངས་པ་དེ་མ་ཐག་པའི་རྐྱེན་གྱི་དངོས་པོར་ཡིན་ལ་རྟེན་གྱི་དངོས་པོར་མ་ཡིན་པ་ཡང་ཡོད་དེ། ཆོས་ཀྱི་ཁམས་སེམས༌[^359]ལས་བྱུང་བ་འདས་མ་ཐག་པའོ། །

[Block 830 [HEADING]]
##### རྟེན་མིག་ལ་སོགས་པ་ཡིན་པ། ^1-3-19-6-0

[Block 831]
ཡང་མིག་གི་རྣམ་པར་ཤེས་པ་ནི་གཉི་ག་ལ་རག་ལུས་ཏེ་སྐྱེ་ན། ཅིའི་ཕྱིར་མིག་ལ་སོགས་པ་ཁོ་ན་ལ་རྟེན༌[^360]ཞེས་བྱའི་གཟུགས་ལ་སོགས་པ་ནི་མ་ཡིན་ཞེ་ན།

[Block 832 [VERSE]]
དེ་དག་གྱུར་པས་འགྱུར་ཉིད་ཕྱིར། །
རྟེན་ནི་མིག་ལ་སོགས་པ་ཡིན། །

[Block 833]
ཁམས་རྣམས་ཞེས་བྱ་བར་སྦྱར་ཏེ། མིག་ལ་སོགས་པ་རྣམས་གྱུར་པས་རྣམ་པར་ཤེས་པ་རྣམས་འགྱུར་བ་ཡིན་ཏེ། ཕན་པ་དང་གནོད་པ་དང་། གསལ་བ་དང་མི་གནོད་པ་དང་མི༌[^361]གསལ་བ་ཉིད་ཀྱི་རྗེས་སུ་བྱེད་པའི་ཕྱིར་རོ། །

[Block 834]
གཟུགས་ལ་སོགས་པ་རྣམས་གྱུར་པས་ནི་དེ་དག་འགྱུར་བ་མ་ཡིན་ཏེ། དེ་ལྟ་བས་ན་དེ་དག་ལ་རག་ལུས་པའི་ཕྱིར་དེ་དག་ཉིད་རྟེན་ཡིན་ནོ། །ཞེས་བྱ་བ་ནི་ཤིན་ཏུ་ལེགས་པ་ཡིན་གྱི་གཟུགས་ལ་སོགས་པ་ནི་མ་ཡིན་ནོ། །

[Block 835 [HEADING]]
##### དེ་དག་གིས་རྣམ་ཤེས་བསྟན་པ། ^1-3-19-7-0

[Block 836]
ཡང་དེ་དག་གིས་ནི་གཟུགས་ལ་སོགས་པ་རྣམ་པར་ཤེས་ན། ཅིའི་ཕྱིར་མིག་གི་རྣམ་པར་ཤེས་པ་ཞེས་བྱ་བ་ནས། ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་ཞེས་བྱ་བའི་བར་ཡིན་གྱི་གཟུགས་ཀྱི་རྣམ་པར་ཤེས་པ་ཞེས་བྱ་བ་ནས་ཆོས་ཀྱི་རྣམ་པར་ཤེས་པ་ཞེས་བྱ་བའི་བར་དུ་ནི་མ་ཡིན་ཞེ་ན། གང་གི་ཕྱིར་དེ་དག་གི་རྟེན་ནི་མིག་ལ་སོགས་པ་ཡིན་ན།

[Block 837 [VERSE]]
[^362] དེའི་ཕྱིར་ཐུན་མོང་མ་ཡིན་ཕྱིར། །
དེ་དག་གིས་ནི་རྣམ་ཤེས་བསྟན། །

[Block 838]
ཇི་ལྟར་ན་ཐུན་མོང་མ་ཡིན་པ་ཉིད་ཡིན་ཞེ་ན། མིག་ནི༌[^363]རྣམ་པར་ཤེས་པ་གཞན་གྱི་རྟེན་དུ་འགྱུར་བར་མི་ནུས་ལ། གཟུགས་ནི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་དམིགས་པར་ཡང་འགྱུར་ལ། མིག་གི་རྣམ་པར་ཤེས་པ་གཞན་གྱི་དམིགས་པར་ཡང་འགྱུར་ཏེ། ལུས་ཀྱི་བར་དུ་ཡང་དེ་དང་འདྲ་བར་རིག་པར་བྱའོ། །

[Block 839]
དེ་ལྟ་བས་ན་རྟེན་དུ་གྱུར་པའི་ཕྱིར་དང་། ཐུན་མོང་མ་ཡིན་པའི་ཕྱིར་དེ་དག་ཁོ་ནས༌[^364]རྣམ་པར་ཤེས་པ་བསྟན་གྱི་གཟུགས་ལ་སོགས་པས་ནི་མ་ཡིན་ཏེ། དཔེར་ན་རྔ་བོ་ཆེའི་སྒྲ་དང་། ནས་ཀྱི་མྱུ་གུ་བཞིན་ནོ། །

[Block 840 [HEADING]]
##### ལུས་དང་མིག་དང་གཟུགས་དང་རྣམ་པར་ཤེས་པའི་ས། ^1-3-19-8-0

[Block 841]
ཡང་ལུས་དག་ལ༌[^365]གནས་ཏེ་མིག་གིས༌[^366]གཟུགས་རྣམས་ལ༌[^367]ལྟ་བ་ནས།[^368] ཅི་ལུས་དང་མིག་དང་གཟུགས་དང་རྣམ་པར་ཤེས་པ་དེ་རྣམས༌[^369]གཅིག་པ་ཁོ་ན་ཞིག་ཡིན་ནམ། འོན་ཏེ་གཞན་གྱི་ས་པ་ཡང་ཡིན་ཞེ་ན། སྨྲས་པ། ཐམས་ཅད་ལ་བྱེ་བྲག་ཡོད་དེ། འདོད་པའི་ཁམས་སུ་སྐྱེས་པ་རང་གི་མིག་གིས་རང་གི་གཟུགས་རྣམས་ལ་ལྟ་བ་ནི༌[^370]ཐམས་ཅད་རང་གི་ས་པ་ཡིན་ནོ། །

[Block 842]
དེ་ཉིད་རང་གི་གཟུགས་རྣམས་ལ་བསམ་གཏན་དང་པོའི་མིག་གིས་ལྟ་བ་ན་ལུས་དང་གཟུགས་དག་ནི་རང་གི་ས་པ་ཡིན་ལ། རྣམ་པར་ཤེས་པ་དང་མིག་དག་ནི་དེའི་ས་པ་ཡིན་ནོ། །

[Block 843]
བསམ་གཏན་དང་པོའི་ས་པ་དག་ལ་ལྟ་ན་ནི་གཟུགས་རྣམས་ཀྱང་དེའི་ས་པ་ཡིན་ནོ། །

[Block 844]
རང་གི་གཟུགས་རྣམས་ཀྱང༌[^371]བསམ་གཏན་གཉིས་པའི་མིག་གིས་ལྟ་བ་ན་ལུས་དང་གཟུགས་དག་ནི་རང་གི་ས་པ་ཡིན་ལ། མིག་ནི་དེའི་ས་པ་ཡིན་ནོ། །

[Block 845]
མིག་གི་རྣམ་པར་ཤེས་པའི་ས༌[^372]ནི་བསམ་གཏན་དང་པོའི་ས་པ་ཡིན་ནོ། །
--- END BLOCKS ---
