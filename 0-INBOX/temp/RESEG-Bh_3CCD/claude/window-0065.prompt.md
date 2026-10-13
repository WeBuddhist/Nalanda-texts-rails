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
དགོད་པའི་སྤྱོད་པ་ནི་རོ་ལངས་བསླང་བ་ལ་སོགས་པའི་མཚན་ཉིད་དམ་སྒེག་པའི་ཉམས་ཀྱི་བྱེ་བྲག་གོ། །

[Block 2277]
གཤེ་བའི་སྤྱོད་པ་ནི་མངོན་སྤྱོད་ལ་སོགས་པའི་ལས་དྲག་པོའི་རབ་འབྱམས་བྱེད་པའི་མཚན་ཉིད་དོ། །

[Block 2278]
འཇིགས་པར་བྱེད་པའི་སྤྱོད་པ་ནི་ཞེ་སྡང་རྡོ་རྗེའི་ཏིང་ངེ་འཛིན་གྱིས་ཁྲོ་བོའི་འཁོར་ལོ་སྤྲོས་ཏེ་བགེགས་རྣམ་པར་གནོན་པ་དང་ཕུར་བུས་གདབ་པ་དང་བརྡུང་བའི༌[^1510]མཚན་ཉིད་དོ། །

[Block 2279]
སྙིང་རྗེའི་སྤྱོད་པ་ནི་སེམས་ཅན་རྗེས་སུ་བཟུང་བའི༌[^1511]མཚན་ཉིད་དོ། །

[Block 2280]
རྔམ་པའི་སྤྱོད་པ་ནི་བསྟན་པ་ལ་སོགས་པའི་རྫུ་འཕྲུལ་ལམ། ཆོས་འདི་རུ་བསྟན་པའི་དུས་སུ་གཞན་དུ་ཡང་བསྟན་པ་ལྟར་སྣང་བའོ། །

[Block 2281]
[^1512]འགལ་བའི་སྒོ་ནས་སེམས་ཅན་གྱི་དོན་བྱེད་པའི་མཚན་ཉིད་དོ། །

[Block 2282]
ཞི་བའི་སྤྱོད་པ་ནི་རང་བཞིན་གྱིས་གྲུབ་པའི་འོད་གསལ་བ་ལ་འཇུག་པའི་ཏིང་ངེ་འཛིན་ཏོ། །

[Block 2283]
འདི་ཡང་རིགས་པ་ཡིན་ཏེ། ཐབས་བདེ་བས་འདོད་ཆགས་ཅན་ལ་སོགས་པ་འདུལ་བའི་ཕྱིར་རོ། །

[Block 2284 [HEADING]]
#### གསུམ་པ་རྒྱན། ^1-7-3-0

[Block 2285]
རིགས་པ༌[^1513]བསྟན་ནས་གསུམ་པ་རྒྱན་བཤད་པའི་རྒྱུད་ལས༌[^1514]བྱ་བའི་ཕྱིར། རྒྱན་ནི་གསུམ་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། མཐའ་དྲུག་ནི་མཐའི་སྒྲས་བྱེ་བྲག་བཤད་དེ། དེས་བྱེ་བྲག་དྲུག་གི་བཤད་པའི་རིམ་པ་ཡིན་ཞེས་བཤད་དོ། །

[Block 2286]
རྣལ་འབྱོར་རྒྱུད་ཚུལ་ལས་བཤད་པའི། །ཞེས་པ་ནི་རྡོ་རྗེ་ཕྲེང་བ་ལ་སོགས་པའི་བཤད༌[^1515]པའི་རྒྱུད་ལས་བཅོམ་ལྡན་འདས་ཉིད་ཀྱིས་གསུངས་སོ། །

[Block 2287]
རྒྱས་བཏབ་དོན་ནི་རབ་རྟོགས་པ། །ཞེས་བྱ་བ་ནི་ཕྱེད་པར་དཀའ་བའི་དོན་ཇི་ལྟ་བ་བཞིན་དུ་ཕྱིན་ཅི་མ་ལོག་པའི་དེ་ཁོ་ན་ཉིད་རབ་ཏུ་རྟོགས་ཤིང་བར་ཏུ༌[^1516]གསལ་བ་ཞེས་ཐ་ཚིག་གོ། །ཇི་ལྟ་བུ་ཞེ་ན། མཐའ་དྲུག་གི་ནི་ཚིག་ངེས་ཤིང་། །ཞེས་སྨོས་པ་ནི་མཐའ་དྲུག་གིས་ཚིག་རྣམས་ངེས་པར་བྱེད་པའོ། །

[Block 2288]
ཚིག་རྣམས་ཀྱི་དོན་ཡང་ངེས་པར་བྱ་ཞེས་སྨྲ་བ༌[^1517]ཡང་ཡིན་ཏེ། མཐའ་དྲུག་ནི་དོན་དང་སྒྲའི་རྒྱན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2289]
དྲང་བ་དང་ཞེས་བྱ་བ་ལ་སོགས་པས་རྒྱས་པར་བཤད་དོ། །

[Block 2290]
སྐལ་ངན་རྣམས་ལ་ཞེས་བྱ་བ་ལ་སོགས་པས་སོ་སོར་བསྟན་པར་བཤད་དོ། །

[Block 2291]
སྐལ་ངན་ནི་སེམས་ལ་གཡོ་སྒྱུ༌[^1518]ཡོད་པ་དང་། ཐེ་ཚོམ་རྒོལ་བ་ལ་དགའ་བའི་ཕྱིར་རོ། །

[Block 2292]
དེ་ལྟ་བུ་ཉན་པ་པོ་གང་ཡིན་པ་དེ་རྣམས་ལ་རྒྱལ་བ་སྟེ་རྡོ་རྗེ་འཆང་ཆེན་པོས་དྲང་བའི་དོན་དུ་གསུངས་ཏེ། དེ་ཁོ་ན་ཉིད་ཀྱི་དོན་ལས་བསྐྱེད་པའི་རིམ་པ་ཙམ་གཞན་དུ་དྲངས་པས༌[^1519]ན་དྲང་བའི་དོན་ཏོ།[^1520] །

[Block 2293]
དེ་ཁོ་ན་ཉིད་སྟོན་པར་བྱེད་པ་མ་ཡིན་ནོ། །

[Block 2294]
སྦས་ཏེ་ཞེས་པ་ནི་དོན་དམ་པ་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2295]
ཡང་དག་དོན་ནི་རབ་སྟོན་ཕྱིར། །ཞེས་པ་ནི་རྩ་ཀུན་ཏུ་སྤྱོད་པ་ལ་སོགས་པའི་མཚན་ཉིད་ཅན་གྱི་དོན་ཇི་ལྟ་བ་བཞིན་དུ་བསྟན་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 2296]
ངེས་པའི་དོན་ནི་ངེས་པར་བཤད་པའི་དོན་ནོ། །

[Block 2297]
གནས་པ༌[^1521]ནི་བཤད་པའོ། །

[Block 2298]
རྗོད་པར་བྱེད་པ་གཅིག་གིས་དོན་གཉིས་བརྗོད་པ་ལ་ནུས་པ་ཇི་ལྟར་ཡོད་ཅེ་ན། སྨྲས་པ། སྣ་ཚོགས་སེལ་བ་དང་ལྡན་པའི་སྒྲ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2299]
དཔེར་ན་གོའི་སྒྲ་གཅིག་པུས་དོན་བཅུ་བརྗོད་དེ། ཇི་སྐད་དུ།

[Block 2300 [VERSE]]
ངག་ཕྱོགས་ས་འོད་རྡོ་རྗེ་མདའ། །
ཕྱུགས་མིག་མཐོ་རིས་ཆུ་དག་ཏུ། །
དོན་བཅུ་ལ་ནི་བློ་ཅན་གྱིས། །
གོ་ཡི་སྒྲ་ནི་བརྟག་པར༌[^1522]བྱ། །

[Block 2301]
ཞེས་འབྱུང་ངོ་། །

[Block 2302]
དོན་གྱི་རྒྱན་དེ་དག་ཡིན་ཏེ། སྒྲའི་བྱེ་བྲག་མེད་པའི་ཕྱིར་རོ། །

[Block 2303]
མཆོག་འདོད་ཅེས་བྱ་བ་ལ་སོགས་པ་ནི་དེ་ཁོ་ན་ཉིད་འདོད་པའི་སློབ་མ་རྣམས་ལའོ། །

[Block 2304]
དེ་རྣམས་ལ་ཆོས་ཀྱི་དེ་ཉིད་རབ་སྟོན་པ་ཞེས་པ་ནི་འོད་གསལ་བའི་དེ་ཁོ་ན་ཉིད་བཤད་པའོ། །

[Block 2305]
འགལ་བའི་ཚིག་གི༌[^1523]སྦྱོར་བ་ཡིས། །ཞེས་པ་ལ་འཇིག་རྟེན་དང་འགལ་བའི་སྒྲའི་སྒོ་ནས་སོ། །

[Block 2306]
གསུངས་པ་གང་ཡིན་དགོངས་བཤད་དེ། །ཞེས་པ་ནི་དགོངས་པ་དང་བཅས་པའི་སྒྲའི་སྦྱོར་བ་བསྟན་ཏེ༌[^1524]ཞེས་ཐ་ཚིག་གོ། །

[Block 2307]
འདི་ནི་སྒྲ་ཡི༌[^1525]རྒྱན་ཡིན་ཏེ། དེ་ལྟ་བུར་གྱུར་པའི་སྒྲ་གཙོ་བོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2308]
དབང་པོ་དམན་པའི་སེམས་ཅན་རྣམས། །ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་ཤེས་རབ་ཀྱི་མཐར་ཐུག་པ་མེད་པ་དེ་བས་དད་པ་ཆེ་བའི་ཕྱིར་དེ་ཁོ་ན་ཉིད་སྟོན་པ་ལ་སྣོད་དུ་གྱུར་པ་དབང་པོ་དམན་པའོ། །

[Block 2309]
རྟོགས་ཕྱིར་ཞེས་པ་ནི་དེ་རྣམས་དེ་ཁོ་ན་ཉིད་དུ་རྟོགས་སུ་འཇུག་པའོ། །

[Block 2310]
མཆོག་ཏུ་གསལ་བ་ཡིས་ཞེས་པ་ནི་གསལ་ཞིང་འཇམ་པའི་ཚིག་གིས་སྟོན་པའོ། །

[Block 2311]
དེ་ཉིད་གསལ་བར་སྟོན་པ་ནི་ཞེས་པ་ལ་རབ་ཏུ་གྲགས་པའི་དེ་ཁོ་ན་ཉིད་བཤད་པའོ། །

[Block 2312]
དགོངས་པ་མིན་པས་བཤད་པའོ། །ཞེས་པ་ནི་འགལ་བའི་སྒྲ་མེད་པར་གསུངས་ཞེས་ཐ་ཚིག་གོ། །

[Block 2313]
འདི་ནི་དོན་གྱི་རྒྱན་ཡིན་ཏེ། དོན་ཁོ་ན་བརྒྱན་པར་བྱ་བ་ཡིན་པས་སོ། །

[Block 2314]
དཀྱིལ་འཁོར་ལ་སོགས་དང་ཞེས་པ་ནི་དཀྱིལ་འཁོར་སྣ་ཚོགས་འདྲི་བ༌[^1526]དང་། ཚད་ལ་སོགས་པའི་ཚིག་རྣམས་ལའོ། །

[Block 2315]
དེ་བཞིན་དུ་རྟོག་པ་ནི་གཤིན་རྗེ་གཤེད་ལ་སོགས་པའི་སྒོམ་པས་རྣམ་པར་སྡང་བ་ལ་སོགས་པ་ལས་ཀྱི་རབ་འབྱམས་སྟོན་པར་བྱེད་པ་ལའོ། །
--- END BLOCKS ---
