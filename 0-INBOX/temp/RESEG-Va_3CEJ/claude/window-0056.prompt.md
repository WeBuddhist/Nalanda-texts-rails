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
[Block 1961]
ཡང་དོན་གང་གིས་ན་ལྷན་ཅིག་འབྱུང་བའི་རྒྱུ་ཡིན། གང་གིས་ན་མཚུངས་པར་ལྡན་པའི་རྒྱུ་གང་ཡིན་ཞེ་ན། ཕན་ཚུན་འབྲས་བུའི་དོན་གྱིས་ན་ལྷན་ཅིག་འབྱུང་བའི་རྒྱུ་ཡིན་ཏེ། འདྲོན་པ༌[^999]རྣམས་ཕན་ཚུན་གྱི་སྟོབས་ཀྱིས༌[^1000]ལྷན་ཅིག་ལམ་དུ་འགྲོ་བ་ཡིན་ནོ། །

[Block 1962]
མཚུངས་པ་ལྔས་མཚུངས་པར་ལྡན་པའི་དོན་གྱིས་ན་མཚུངས་པར་ལྡན་པའི་རྒྱུ་ཡིན་ཏེ། འདྲོན་པ་དེ་དག་ཉིད་ཟས་ལ་སོགས་པ་ཡོངས་སུ་ལོངས་སྤྱོད་པའི་བྱ་བ་ལ༌[^1001]འདྲ་བར་སྦྱོར་བ་བཞིན་ནོ། །

[Block 1963]
གཅིག་མེད་ན་ཡང་ཐམས་ཅད་མཚུངས་པར་མི་ལྡན་པས་འདི་ནི་དེ་དག་གི་རྒྱུའི་དངོས་པོ་ཡིན་ནོ། །

[Block 1964 [HEADING]]
###### ཀུན་ཏུ་འགྲོ་བའི་རྒྱུ། ^2-4-1-1-5-0

[Block 1965]
ཀུན་ཏུ་འགྲོ་བའི་རྒྱུ་གང་ཞེ་ན།

[Block 1966 [VERSE]]
ཀུན་འགྲོ་ཞེས་བྱ་ཉོན་མོངས་ཅན། །
རྣམས་ཀྱི་རང་སར༌[^1002]ཀུན་འགྲོ་ལྔ། །

[Block 1967]
རང་གི་ས་པའི་ཀུན་ཏུ་འགྲོ་བའི་ཆོས་སྔར་སྐྱེས་པ་རྣམས་ནི་ཉོན་མོངས་པ་ཅན་གྱི་ཆོས། ཕྱི་མ་རྣམས་ཀྱི་ཀུན་ཏུ་འགྲོ་བའི་རྒྱུ་ཡིན་ནོ། །

[Block 1968]
དེ་དག་ཀྱང་འོག་ནས་ཕྲ་རྒྱས་བསྟན་པའི་མཛོད་ཀྱི་གནས་ཉིད་ནས་བཤད་པར་བྱའོ། །

[Block 1969]
འདི་ནི་ཉོན་མོངས་པ༌[^1003]ཅན་གྱི་ཆོས་ཀྱི་ཐུན་མོང་གི་རྒྱུ་ཉིད་ཡིན་པས་ན་སྐལ་བ་མཉམ་པའི་རྒྱུ་ལས་ལོགས་ཤིག་ཏུ་རྣམ་པར་གཞག་གོ། །

[Block 1970]
རིས་གཞན་དག་གི་ཡང་རྒྱུ་ཡིན་པའི་ཕྱིར་ཏེ། དེ་དག་གི་མཐུས་ནི་རིས་གཞན་པའི་ཉོན་མོངས་པ་དག་ཀྱང་སྐྱེ་བར་འགྱུར་རོ། །

[Block 1971]
ཅི་འཕགས་པའི་གང་ཟག་གི་ཉོན་མོངས་པ་ཅན་གྱི་ཆོས་རྣམས་ཀྱང་ཀུན་ཏུ་འགྲོ་བའི་རྒྱུ་ལས་བྱུང་བ་དག་ཡིན༌[^1004]ནམ་ཞེ་ན། ཁ་ཆེ་བ་རྣམས་ན་རེ་ཉོན་མོངས་པ་ཅན་གྱི་ཆོས་ཐམས་ཅད་ཀྱང་མཐོང་བས་སྤང་བར་བྱ་བའི་རྒྱུ་ལས་བྱུང་བ་དག་ཡིན་ཏེ། འདི་ལྟར་རབ་ཏུ་བྱེད་པ་དག་ལས་མཐོང་བས་སྤང་བར་བྱ་བའི་རྒྱུ་ལས་བྱུང་བའི་ཆོས་རྣམས་གང་ཞེ་ན། ཉོན་མོངས་པ་ཅན་གྱི་ཆོས་རྣམས་དང་། མཐོང་བས་སྤང་བར་བྱ་བའི་ཆོས་རྣམས་ཀྱི་རྣམ་པར་སྨིན་པ་གང་ཡིན་པའོ་ཞེས་བྱ་བ་དང་། ལུང་དུ་མ་བསྟན་པའི་རྒྱུ་ལས་བྱུང་བའི་ཆོས་རྣམས་གང་ཞེ་ན། ལུང་དུ་མ་བསྟན་པའི་ཆོས་འདུས་བྱས་རྣམས་དང་། མི་དགེ་བ་རྣམས་སོ་ཞེས་བྱ་བ་དང་། སྡུག་བསྔལ་གྱི་བདེན་པ་ལ་འཇིག་ཚོགས་ལ་ལྟ་བའི་རྒྱུ་ཅན་ཡིན་པ༌[^1005]འཇིག་ཚོགས་ལ་ལྟ་བའི་རྒྱུ་མ་ཡིན་པ་ཡང་ཡོད་དེ༌[^1006]ཞེས་བྱ་བ་ནས་རྒྱས་པར་འཇིག་ཚོགས་ལ་ལྟ་བ་དང་། ཆོས་དེ་དག་གི་སྐྱེ་བ་དང་རྒ་བ་དང་གནས་པ་དང་། མི་རྟག་པ་ཉིད་དག༌[^1007]མ་གཏོགས་པ་དེ་དག་ལས་གཞན་པ་སྡུག་བསྔལ་གྱི་བདེན་པ་ཉོན་མོངས་པ་ཅན་གང་ཡིན་པའོ་ཞེས་བྱ་བའི་བར་དུ་གསུངས་སོ་ཞེས་ཟེར་རོ།[^1008] །འོ་ན་བཏགས་པའི་བཤད་པ་མི་དགེ་བའི་ཆོས་མི་དགེ་བའི་རྒྱུ་ཅན་ཁོ་ན་ཡིན་པ་ཡོད་དམ་ཞེ་ན། ཡོད་དེ།[^1009] འཕགས་པའི་གང་ཟག་འདོད་པའི་འདོད་ཆགས་དང་བྲལ་བ་ལས་ཡོངས་སུ་ཉམས་པ་དེ་ལས་དང་པོར་ཉོན་མོངས་པ་ཅན་གྱི་སེམས་པ་མངོན་དུ་བྱེད་པ་གང་ཡིན་པའོ་ཞེས་གསུངས་པ་འདི་ཇི་ལྟར་དྲང་ཞེ་ན། [^1010]དེ་ནི་རྒྱུ་མ་སྤངས་པ་ལས་དགོངས་ནས་གསུངས་པ་ཡིན་གྱི་དེའི་རྒྱུ་མཐོང་བས་སྤང་བར་བྱ་བ་ནི་སྤངས་ཟིན་པའི་ཕྱིར་མ་གསུངས་སོ། །

[Block 1972]
ཀུན་ཏུ་འགྲོ་བའི་རྒྱུ་བཤད་ཟིན་ཏོ། །

[Block 1973 [HEADING]]
###### རྣམ་པར་སྨིན་པའི་རྒྱུ། ^2-4-1-1-6-0

[Block 1974]
རྣམ་པར་སྨིན་པའི་རྒྱུ་གང་ཞེ་ན།

[Block 1975 [VERSE]]
རྣམ་སྨིན་རྒྱུ་ནི་མི་དགེ་དང་། །
དགེ་བ་ཟག་བཅས་རྣམས་ཁོ་ན། །

[Block 1976]
མི་དགེ་བ་རྣམས་དང་། དགེ་བའི་ཆོས་ཟག་པ་དང་བཅས་པ་རྣམས་ནི་རྣམ་པར་སྨིན་པའི་རྒྱུ་ཡིན་ཏེ། རྣམ་པར་སྨིན་པའི་ཆོས་ཅན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1977]
ཅིའི་ཕྱིར་ལུང་དུ་མ་བསྟན་པའི་ཆོས་རྣམས་རྣམ་པར་སྨིན་པ་འགྲུབ་པར་མི་བྱེད་ཅེ་ན། སྟོབས་ཆུང་བའི་ཕྱིར་ཏེ་ས་བོན་རུལ་བ་བཞིན་ནོ། །ཅིའི་ཕྱིར་ཟག་པ་མེད་པ་རྣམས་མ་ཡིན་ཞེ་ན། སྲེད་པས་མངོན་པར་མ་བརླན་པའི་ཕྱིར་ཏེ། མངོན་པར་མ་བརླན་པའི་ས་བོན་གྲུང་པོ་བཞིན་ནོ། །

[Block 1978]
ལྡན་པ་མ་ཡིན་པ་རྣམས་གང་དང་ལྡན་པའི་རྣམ་པར་སྨིན་པ་ཞིག་མངོན་པར་འགྲུབ་པར་བྱེད་པར་འགྱུར། ལྷག་མ་རྣམས་ནི་རྣམ་པ་གཉི་ག་ཡིན་པའི་ཕྱིར་འགྲུབ་པར་བྱེད་དེ་ས་བོན་གྲུང་པོ་མངོན་པར་བརླན་པ་བཞིན་ཏེ། འདི་ཇི་ལྟར་ཤེས་པར་བྱ། རྣམ་པར་སྨིན་པའི་རྒྱུ་ཞིག་རྣམ་པར་སྨིན་པའི་རྒྱུ་ཡིན་ནམ། འོན་ཏེ་རྣམ་པར་སྨིན་པ་ཉིད་རྒྱུ་ཡིན་པས་རྣམ་པར་སྨིན་པའི་རྒྱུ་ཡིན། དེས་ན་ཅིར་འགྱུར། [^1011]གལ་ཏེ་རྣམ་པར་སྨིན་པའི་རྒྱུ་ཞིག་རྣམ་པར་སྨིན་པའི་རྒྱུ་ཡིན་ན་ནི་མིག་གི་རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་དེར་མི་འགྱུར་རོ། །ཅིའི་ཕྱིར་ཞེ་ན། ལས་ལས་སྐྱེས་པའི་ཕྱིར་ལ་ལས་ཀྱང་རྣམ་པར་སྨིན་པའི་རང་བཞིན་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1979]
འོན་ཏེ་རྣམ་པར་སྨིན་པ་ཉིད་རྒྱུ་ཡིན་པས་རྣམ་པར་སྨིན་པའི་རྒྱུ་ཡིན་ན་ནི་ལས་ཀྱི་རྣམ་པར་སྨིན་པ་ཞེས་བྱ་བ་དེར་མི་འགྱུར་རོ། །ཅིའི་ཕྱིར་ཞེ་ན། རྣམ་པར་སྨིན་པ་ནི་རྒྱུ་ཡིན་པའི་ཕྱིར་ལ་རྣམ་པར་སྨིན་པ་ཡང་ལས་ཀྱི་རང་བཞིན་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1980]
གཉི་ག་ལྟར་ཡང་རུང་ངོ་ཞེས་སྔར་བཤད་ཟིན་ཏོ། །

[Block 1981]
ཡང་རྣམ་པར་སྨིན་པ་ཞེས་བྱ་བའི་དོན་ཅི་ཞེ་ན། མི་འདྲ་བར་སྨིན་པ་ནི་རྣམ་པར་སྨིན་པའོ། །

[Block 1982]
འདོད་པའི་ཁམས་ན་རྣམ་པར་སྨིན་པའི་རྒྱུ་ཕུང་པོ་གཅིག་ལ་འབྲས་བུ་གཅིག་པ་ཅན་ནི་ཐོབ་པ་རྣམས་དང་དེ་དག་གི་སྐྱེ་བ་ལ་སོགས་པའོ། །

[Block 1983]
ཕུང་པོ་གཉིས་པ་ལ་འབྲས་བུ་གཅིག་པ་ཅན་ནི་ལུས་དང་ངག་གི་ལས་དང་དེ་དག་གི་སྐྱེ་བ་ལ་སོགས་པའོ། །

[Block 1984]
ཕུང་པོ་བཞི་ལས་འབྲས་བུ་གཅིག་པ་ཅན་ནི་སེམས་དང་སེམས་ལས་བྱུང་བ་དགེ་བ་དང་མི་དགེ་བ་སྐྱེ་བ༌[^1012]ལ་སོགས་པ་དང་བཅས་པ་དག་གོ། །

[Block 1985]
གཟུགས་ཀྱི་ཁམས་ན་རྣམ་པར་སྨིན་པའི་རྒྱུ་ཕུང་པོ་གཅིག་ལ་རྣམ་པར་སྨིན་པ་གཅིག་པ་ཅན་ནི་ཐོབ་པ་དང་། འདུ་ཤེས་མེད་པའི་སྙོམས་པར་འཇུག་པ་སྐྱེ་བ་ལ་སོགས་པ་དང་བཅས་པའོ། །

[Block 1986]
ཕུང་པོ་གཉིས་པ་ནི་བསམ་གཏན་དང་པོའི་རྣམ་པར་རིག་བྱེད་སྐྱེ་བ་ལ་སོགས་པ་དང་བཅས་པའོ། །

[Block 1987]
ཕུང་པོ་བཞི་པ་ནི་དགེ་བའི་སེམས་མཉམ་པར་མ་བཞག་པ་ནའོ། །

[Block 1988]
ཕུང་པོ་ལྔ་པ་ནི་མཉམ་པར་བཞག་པ་ནའོ། །

[Block 1989]
གཟུགས་མེད་པའི་ཁམས་ན༌[^1013]རྣམ་པར་སྨིན་པའི་རྒྱུས་ཕུང་པོ་གཅིག་ལ་འབྲས་བུ་གཅིག་པ་ཅན་ནི་ཐོབ་པ་དང་འགོག་པའི༌[^1014]སྙོམས་པར་འཇུག་པ་སྐྱེ་བ་ལ་སོགས་པ་དང་བཅས་པའོ། །

[Block 1990]
ཕུང་པོ་བཞི་པ་ནི་སེམས་དང་སེམས་ལས་བྱུང་བ་དགེ་བ་རྣམས་དང་དེ་དག་གི་སྐྱེ་བ་ལ་སོགས་པའོ། །

[Block 1991]
གང་གི་རྣམ་པར་སྨིན་པ་ཆོས་ཀྱི་སྐྱེ་མཆེད་གཅིག་ཁོ་ན་རྣམ་པར་སྨིན་པར་འགྱུར་བའི་ལས་ཀྱང་ཡོད་དེ། གང་གི་སྲོག་གི་དབང་པོ་ཡིན་པའོ། །

[Block 1992]
གང་གི་ཡིད་ཀྱི་སྐྱེ་མཆེད་ཡིན་པ་དེའི་ནི་གཉིས་ཏེ། ཡིད་དང་ཆོས་ཀྱི་སྐྱེ་མཆེད་དག་གོ། །

[Block 1993]
གང་གི་རེག་བྱའི་སྐྱེ་མཆེད་ཡིན་པ་ཡང་དེ་དང་འདྲའོ། །

[Block 1994]
གང་གི་ལུས་ཀྱི་སྐྱེ་མཆེད་ཡིན་པ་དེའི་ནི་གསུམ་སྟེ། ལུས་དང་རེག་བྱ་དང་། ཆོས་ཀྱི་སྐྱེ་མཆེད་དག་གོ། །

[Block 1995]
གང་གི་གཟུགས་དང་དྲི་དང་རོའི་སྐྱེ་མཆེད་དག་ཡིན་པ་ཡང་དེ་དང་འདྲའོ། །

[Block 1996]
གང་གི་མིག་གི་སྐྱེ་མཆེད་ཡིན་པ་དེའི་ནི་བཞི་སྟེ། མིག་དང་ལུས་དང་རེག་བྱ་དང་ཆོས་ཀྱི་སྐྱེ་མཆེད་རྣམས་སོ། །

[Block 1997]
གང་གི་རྣ་བ་དང་། སྣ་དང་། ལྕེའི་སྐྱེ་མཆེད་དག་ཡིན་པ་ཡང་དེ་དང་འདྲའོ། །

[Block 1998]
གང་གི་རྣམ་པར་སྨིན་པ་ལྔ་དང་། དྲུག་དང་། བདུན་དང་། བརྒྱད་དང་། དགུ་དང་། བཅུ་དང་། བཅུ་གཅིག་སྨིན་པར་འགྱུར་བའི་ལས་དེ་ཡང་ཡོད་དེ། ལས་ཀྱི་འབྲས་བུ་སྣ་ཚོགས་དང་། སྣ་ཚོགས་མ་ཡིན་པའི་ཕྱིར་ཕྱིའི་ས་བོན་བཞིན་ནོ། །

[Block 1999]
དཔེར་ན་ཕྱིའི་ས་བོན་རྣམས་ལ༌[^1015]ཁ་ཅིག་ནི་འབྲས་བུ་སྣ་ཚོགས་པ་ཡིན་ཏེ། འདི་ལྟ་སྟེ་པདྨ་དང་། བལ་པོ་སེའུ་དང་། ཤིང་ནྱ་གྲོ་དྷ་ལ་སོགས་པ་དག་གི་ལྟ་བུའོ། །

[Block 2000]
ཁ་ཅིག་ནི་འབྲས་བུ་སྣ་ཚོགས་པ་མ་ཡིན་ཏེ། འདི་ལྟ་སྟེ། ནས་དང་གྲོ་ལ་སོགས་པ་དག་གི་ལྟ་བུའོ། །
--- END BLOCKS ---
