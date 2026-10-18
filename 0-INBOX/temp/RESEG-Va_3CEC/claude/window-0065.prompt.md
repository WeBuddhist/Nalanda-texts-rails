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
[Block 2276]
ཡང་ན་ནི་མི་གཡོ་བས་རྟག་པའོ། །

[Block 2277]
མི་འགྱུར་བས་ན་ཐེར་ཟུག་པའོ།[^1986] །ལུས་འདི་ལ་བདག་གིར༌[^1987]མི་བྱའོ་ཞེས་བྱ་བ་ལ་ལུས་འདི་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའ་ཉིད་ཀྱི་ལུས་ལ་བསྙེགས་སོ། །

[Block 2278]
བདག་གིར་མི་བྱ༌[^1988]ཞེས་བྱ་བ་ནི་ལུས་དེ་ལ་བདག་གི་དོན་དུ་མི་བྱའོ། །

[Block 2279]
ཡང་ན་ལུས་དེ་ལ་ཆགས་པར་མི་བྱའོ། །

[Block 2280]
ཡང་ན་ལུས་དེ་ལ་བདག་ཏུ་འཛིན་པར་མི་བྱ་སྟེ། འདི་ནི་ལུས་ཐམས་ཅད་དང་བྲལ་བར་གྱུར་པའོ། །

[Block 2281]
བདག་གི༌[^1989]སྙིང་པོ་མེད་པའི་ལུས་འདིས་སྙིང་པོ་མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་བར་ཞེས་བྱ་བ་ལ་བདག་གི་ལུས་སྙིང་པོ་མེད་པ་ནི་ཕ་མའི་མི་གཙང་བ་དང་ལས་དང་ཉོན་མོངས་པའི་རྒྱུ་རྐྱེན་ལས་བྱུང་བ་དང་། བདག་དང་སེམས་ཅན་དང་། ཆོས་ཀྱི་དངོས་པོ་མེད་པས་སྙིང་པོ་མེད་པ་སྟེ། སྙིང་པོ་མེད་པ་དེ་ལ་བརྟེན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2282]
སྙིང་པོ་མངོན་པར་འཚང་རྒྱ་ཞེས་བྱ་བ་ནི་སྙིང་པོའི་ཆོས་དེ་མངོན་སུམ་དུ་བྱ༌[^1990]ཞིང་ཐོབ་པར་བྱའོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2283 [HEADING]]
###### སྐུ་གསུམ། ^8-1-1-5-2-0

[Block 2284]
དེ་ལ་སྙིང་པོའི་ཆོས་ནི་སྐུ་གསུམ༌[^1991]སྟེ། ཆོས་ཀྱི་སྐུ་དང་། ལོངས་སྤྱོད་རྫོགས་པའི་སྐུ་དང་། སྤྲུལ་པའི་སྐུའོ། །

[Block 2285]
གང་འདི་དེ་བཞིན་གཤེགས་པའི་སྐུ་ཞེས་བྱ་བས༌[^1992]སྐུ་གསུམ་ཆར་ལ་བྱ་བར་འདོད་དོ། །

[Block 2286 [HEADING]]
###### **ཆོས་ཀྱི་སྐུ།** ^8-1-1-5-2-1-0

[Block 2287]
བདག་གི༌[^1993]དེ་བཞིན་གཤེགས་པའི་སྐུ་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། བསྒྲུབ་པར་བྱའོ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་ཆོས་ཀྱིས་ཐོབ་པར་བྱ་བ་བསྟན་ཏོ། །

[Block 2288]
ཆོས་ཀྱི་སྐུ་དེ་ཡང་རྣམ་པ་ལྔར་རིག་པར་བྱ་སྟེ། ཕ་རོལ་ཏུ་ཕྱིན་པའི་འབྲས་བུར་གྱུར་པ་དང་། ཉོན་མོངས་པ་དང་། ཤེས་བྱའི་སྒྲིབ་པ་འཇོམས་པར་བྱེད་པ་དང་། དེ་གཉིས་ཀྱིས་མི་ཚུགས་པ་དང་། དུས་ཐམས་ཅད་དུ་གནས་པ་དང་། ཐམས་ཅད་ལས་འཕགས་པར་གྱུར་པའོ། །

[Block 2289 [HEADING]]
###### **ཕ་རོལ་ཏུ་ཕྱིན་པའི་འབྲས་བུར་གྱུར་པ།** ^8-1-1-5-2-1-1-0

[Block 2290]
ཆོས་ཀྱི་སྐུ་ཞེས་བྱ་བས་ས་དང་ཕ་རོལ་ཏུ་ཕྱིན་པའི་འབྲས་བུར་གྱུར་པ་བསྟན་ཏེ། དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱི་ཆོས་ཀྱི་སྐུ་དེ་ས་དང་ཕ་རོལ་ཏུ་ཕྱིན་པའི་ཆོས་རྣམས་བསྒྲུབ་པའི༌[^1994]རྒྱུ་ལས་བྱུང་བའི་སྐུ་ཡིན་པས་སོ། །

[Block 2291 [HEADING]]
###### **ཉོན་མོངས་པ་དང་ཤེས་བྱའི་སྒྲིབ་པ་འཇོམས་པ།** ^8-1-1-5-2-1-2-0

[Block 2292]
རྡོ་རྗེའི་སྐུ་ཞེས་བྱ་བས་ཉོན་མོངས་པ་དང་ཤེས་བྱའི་སྒྲིབ་པ་འཇོམས་པར༌[^1995]བསྟན་ཏེ། རྡོ་རྗེ་བཞིན་དུ་བདག་མེད་པའི་མཚན་ཉིད་ཀྱི༌[^1996]སྐུ་དེས་ཉོན་མོངས་པ་དང་ཤེས་བྱའི་སྒྲིབ་པ་སྤོང་བར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 2293 [HEADING]]
###### **དེ་གཉིས་ཀྱིས་མི་ཚུགས་པ།** ^8-1-1-5-2-1-3-0

[Block 2294]
མི་ཤིགས་པའི་སྐུ་ཞེས་བྱ་བས་དེ་གཉིས་ཀྱིས་མི༌[^1997]ཚུགས་པ་བསྟན་ཏོ། །

[Block 2295]
ཆོས་ཀྱི་སྐུ་དེ་ཉོན་མོངས་པ་དང་ཤེས་བྱའི་སྒྲིབ་པ་གློ་བུར༌[^1998]གྱིས་མི་གོས་པའི་ཕྱིར་རོ། །

[Block 2296 [HEADING]]
###### **དུས་ཐམས་ཅད་དུ་གནས་པ།** ^8-1-1-5-2-1-4-0

[Block 2297]
བརྟན་པའི༌[^1999]སྐུ་ཞེས་བྱ་བས་དུས་ཐམས་ཅད་དུ་གནས་པ་བསྟན་ཏེ། ནམས་ཀྱང་ཉམས་པ་མེད་ཅིང་འཁོར་བ་ཇི་སྲིད་ཀྱི་བར་དུ་ཡང་གནས་པའི་ཕྱིར་རོ། །

[Block 2298 [HEADING]]
###### **ཐམས་ཅད་ལས་འཕགས་པར་གྱུར་པ།** ^8-1-1-5-2-1-5-0

[Block 2299]
ཁམས་གསུམ་ཐམས་ཅད་ལས་ཁྱད་པར་དུ་འཕགས་ཞེས་བྱ་བས་ཐམས་ཅད་ལས་འཕགས་པར་གྱུར་པ་བསྟན་ཏོ། །

[Block 2300]
ཁམས་གསུམ་ཐམས་ཅད་ལས་འཕགས་པ་ཉན་ཐོས་ཀྱིས༌[^2000]རྣམ་པར་གྲོལ་བའི་སྐུ་ལས་ཀྱང་ཁྱད་པར་འཕགས་པའི་ཕྱིར་རོ། །

[Block 2301 [HEADING]]
###### **ལོངས་སྤྱོད་རྫོགས་པའི་སྐུ།** ^8-1-1-5-2-2-0

[Block 2302]
བདག་གི་ལུས་ཉེས་པ་དུ་མ་ཞེས་བྱ་བ་ལ་སོགས་པས་ལོངས་སྤྱོད་རྫོགས་པའི་སྐུ་ཐོབ་པར་བྱ་བ་བསྟན་ཏེ། བདག་གི་ལུས་ཉེས་པ་དུ་མའི་སྐྱོན་ཆགས་ཞེས་བྱ་བ་ནི་སྔོན་ཡང་ལས་དང་ཉོན་མོངས་པ་དང་། ཕ་མའི་མི་གཙང་བ་ལས་བྱུང་ཞིང་། བྱུང་ནས་ཀྱང་འདོད་ཆགས་ལ་སོགས་པ་ཉོན་མོངས་པ་སྐྱེ་བ་དང་། སྡུག་བསྔལ་སྣ་ཚོགས་འབྱུང་བའི་རྟེན་དུ་གྱུར་པས་ཉེས་པ་དུ་མའི༌[^2001]སྐྱོན་དང་ལྡན་མོད་ཀྱི་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2303]
འོན་ཀྱང་ཞེས་བྱ་བ་ནི་ལུས་དེ་ལ་ཡོན་ཏན་ཡང་འབྱུང་བར་སྟོན་པ་སྟེ། ཡོན་ཏན་འབྱུང་བས་སྐྱོན་ཅན་དེ་ལ་བརྟེན་ནས་ཞེས་བྱ་བར་དྲང་ངོ་། །དེ་བཞིན་གཤེགས་པའི་སྐུ་ཉེས་པ་ཐམས་ཅད་དང་བྲལ་བ་ཐོབ་པར་བྱའོ་ཞེས་བྱ་བ་ནི་དེ་བཞིན་གཤེགས་པའི་ལོངས་སྤྱོད་རྫོགས་པའི་སྐུ་ཉོན་མོངས་པ་དང་ཤེས་བྱའི་སྒྲིབ་པ་ཐམས་ཅད་དང་བྲལ་བ་ཐོབ་པར་བྱའོ། །

[Block 2304]
དེས་ཕན་ཡོན་མཐོང་བས་ན༌[^2002]སོ་སོར་རྟོག་པའི་སྟོབས་ཀྱིས་འབྱུང་བ་ཆེན་པོའི་གནས་ཀྱི་ལུས༌[^2003]སྤོང་སྟེ་ཞེས་བྱ་བ་ནི་ལུས་སྙིང་པོ་མེད་པ་འདི་སྤྱད་ལེགས་ན་འོག་ནས་འབྱུང་བའི་ཕན་ཡོན་ནམ། ཡོན་ཏན་འབྱུང་བར་མཐོང་བར༌[^2004]སོ་སོར་རྟོག་པའི་སྟོབས་ཀྱིས་ས་ཆུ་མེ་རླུང་ལ་སོགས་པ་སེམས་ཅན་གྱི་གསོས་སུ་གྱུར་པ་འོག་ནས་བཤད་པ་བཞིན་དུ་བདག་གི་ལུས་ཀྱང་དེ་ལྟར་ཟད་པར་སྤྱད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2305]
བདག་གི་ལུས་འདི་ཡང་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་སེམས་ཅན་ཐམས་ཅད་ཀྱི་དོན་བྱ་བ་ཇི་ཡོད་པ་རྣམས་བྱེད་པ་ལ་ལུས་འདི་ཟད་པར་བྱ། མཐར་བྱེད་པར་བྱའོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2306]
སྒོ་སྣ་ཚོགས་ནི་སེམས་ཅན་རྣམ་པ༌[^2005]མང་པོ་རྣམ་པ་དུ་མའི་སྒོས༌[^2006]སོ། །

[Block 2307]
རྣམ་པ་སྣ་ཚོགས་ནི་རྨོ་བ་དང་དཔུང་བ་ལ་སོགས་པའི་རྣམ་པས་སོ། །

[Block 2308]
དམིགས་པ་སྣ་ཚོགས་ནི་སེམས་ཅན་དེ་དག་གི༌[^2007]ལ་ལས་ཇིར༌[^2008]དམིགས། ལ་ལས་ཇིར༌[^2009]དམིགས་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 2309]
རྣམ་གྲངས་སྣ་ཚོགས་པ་ནི་རྨོ་བ་དང་རྐོ་བ༌[^2010]ལ་སོགས་པ་ཡང་ལ༌[^2011]ལས་ཇི་ལྟར་ལ་ལས་ཇི་ལྟར་ཏེ། མི་མཐུན་པ་དུ་མར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 2310]
ཡོ་བྱད་སྣ་ཚོགས་ནི་ཁ་ཅིག་གི༌[^2012]གནས། ཁ་ཅིག་གིས་བགོ་བ་ལ་སོགས་པར༌[^2013]བྱེད་པའི་ཕྱིར་རོ། །

[Block 2311]
ལོངས་སྤྱོད་སྣ་ཚོགས་ནི་བཟའ་བ་དུ་མ་དང་། བཏུང་བ༌[^2014]དུ་མའི་དངོས་པོ་བྱེད་པས་སོ། །

[Block 2312]
ཡོངས་སུ་སྤྱོད་པར་གྱུར་པ་ནི་གནས་ལ་སོགས་པར་གྱུར་པས་སོ། །

[Block 2313]
ལོངས་སྤྱོད་དུ་གྱུར་པ༌[^2015]ནི་བཟའ་བ་ལ་སོགས་པར་འགྱུར་བར་རོ། །

[Block 2314]
དེས་དོན་གྱི་དབང་ནི༌[^2016]མཐོང་ནས་ཞེས་བྱ་བ་ལ། བྱང་ཆུབ་སེམས་དཔའ་དེས་ལུས་དེ་ལ་གོང་དུ་བཤད་པ་ལྟ་བུའི་དོན་གྱི་དབང་མཐོང་ནས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2315]
ལུས་ལ་སྡུག་བསྔལ་བར་ཡང་རྟོག་ཅིང་ཞེས་བྱ་བ་ནི་ལུས་སྐྱེ་བ་དང་། རྒ་བ་དང་། ན་བ་དང་། འཆི་བ་ལ་སོགས་པའི་སྡུག་བསྔལ་རྣམ་པ་དུ་མ་དང་ལྡན་པར་རྟོག་པའོ། །
--- END BLOCKS ---
