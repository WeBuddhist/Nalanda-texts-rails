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
ཅི་སྟེ་ལོག་པའི་དོན་ཅན་གྱི་ཚིག་གང་ཡིན་པ་དེ་མ་ལུས་པའི་བྱས་པ་ཡིན་པའི་ཕྱིར། གཏན་ཚིགས་ལྡོག་པས་བསྒྲུབ་པར་བྱ་བ་ལོག་པ་ལ་ཁྱབ་པའི་ཕྱིར་གཞན་ལ་མི་སྲིད་པས་ན། མ་བྱས་པ་ནི་བདེན་པའི་དོན་ཅན་ཡིན་ནོ་ཞེས་བྱ་བར་རྗེས་སུ་འགྲོ་བ་མེད་པར་འགྱུར་རོ། །

[Block 2277]
གང་ལ་གང་གིས་མ་ཁྱབ་ན། དེ་ལ་ལྡོག་པར་དོགས་པར་བྱ་བ༌[^1598]ན། འགལ་བ་དག་ནི་གཅིག་ལ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2278]
མེད་ན་ཡང་རིགས་མི་མཐུན་པ་ལ་རྣམ་པ་གཞན་མེད་པས་འདོད་པའི་དོན་གྲུབ་པའི་ཕྱིར་དང་། དེ་སྒྲུབ་པའི་བྱེད་པ་ཉིད་ཡིན་པའི་ཕྱིར། རྟགས་ཀྱི་རྗེས་སུ་འགྲོ་བ་བསྟན་པ་དོན་མེད་པ་ཡིན་ཏེ། ལྡོག་པ་ཙམ་ཉིད་ཀྱིས་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 2279]
དེ་ནི་བདེན་ཏེ་གལ་ཏེ་གཏན་ཚིགས་བསྒྲུབ་པར་བྱ་བའི་མི་མཐུན་པའི་ཕྱོགས་ལ་ཁྱབ་པར་བྱ་བ་དང་། ཁྱབ་པར་བྱེད་པའི་ངོ་བོ་གྲུབ་པར་འགྱུར་ན་དེ་ཡང་གྲུབ་པ་མ་ཡིན་ནོ། །

[Block 2280]
འདི་ལྟར།

[Block 2281 [VERSE]]
མེད་ཕྱིར་གཏན་ཚིགས་མ་བསྟན་ནའང་། །
དེ་ནི་ཡོད་པར་དོགས་འགྱུར་ཏེ། །
དངོས་པོ་འགལ་བ་དག་ལ་ཡང་། །
ཁྱབ་པར་བྱེད་པ་མཐོང་ཕྱིར་རོ། །

[Block 2282]
གལ་ཏེ་གཏན་ཚིགས་བསྒྲུབ་པར་བྱ་བ་མི་མཐུན་པའི་ཕྱོགས་ལ་མེད་པར་འགྲུབ་པར་འགྱུར་ན། བསྒྲུབ་པར་བྱ་བ་ལོག་པ་ལ་གཏན་ཚིགས་ལྡོག་པས་ཁྱབ་པར་འགྱུར་ན། དེ་ལ་དེ་མེད་པ་ལ་ཚད་མ་ཡང་མ་མཐོང་ངོ་། །མི་འགལ་བ༌[^1599]བསྒྲུབ་པར་བྱ་བ་ལ་ཡང་དགག་པ་སྒྲུབ་པར་བྱེད་པ་རིགས་པ་མ་ཡིན་ཏེ། ཐལ་ཆེས་པའི་ཕྱིར་རོ། །

[Block 2283]
ཐ་དད་པའི་འགལ་བ་དང་ལྷན་ཅིག་འབྱུང་བ་ཅན་དག་ཀྱང་མཐོང་བའི་ཕྱིར། གཅིག་ལ་མཐོང་བ་ཡང་གཞན་ལ་མེད་པ་ཉིད་མ་ཡིན་ཏེ། བརྩལ་མ་ཐག་ཏུ་འབྱུང་བ་ཉིད་དང་ཅིག་ཤོས་དག་ལ་མི་རྟག་པ་ཉིད་བཞིན་ནོ། །

[Block 2284]
དེ་ལྟ་བུའི་རྣམ་པ་ཡང་མཐོང་བ་མེད་པའི་ཕྱིར། མེད་པ་ཉིད་ཁོ་ན་མ་ཡིན་ནོ། །

[Block 2285]
འདི་ལྟར། ཐམས་ཅད་དུ་ནི་མི་དམིགས་ཕྱིར།

[Block 2286 [VERSE]]
མེད་ཉིད་མི་འགྲུབ་ཅེས་ནི་བཤད། །
མེད་པ་ཉིད་ནི་མི་འགྲུབ་ན། །
ལྡོག་པ་ཉིད་ལ་ཐེ་ཚོམ་ཟ། །

[Block 2287]
སྐྱེས་བུ་ཙམ་འདིས་ནི་ཐམས་ཅད་མཐོང་བར་ནུས་པ་མ་ཡིན་ན་གང་གིས་ན་འདིའི་མཐོང་བ་ལྡོག་པས་དེ་ལྟར་མི་འགྱུར། གང་གི་ཡེ་ཤེས་ཤེས་བྱ་ཡོད་པ་ཉིད་ལ་འཁྲུལ་པ་མེད་པ་དེ་ཉིད་ཀྱིས་གཟིགས་པའི་ཕྱིར་མེད་དོ། །

[Block 2288]
ཞེས་གསུངས་པ་མཛེས་པར་འགྱུར་རོ། །

[Block 2289]
དེ་བས་ན་རང་བཞིན་དང་དུས་དང་ཡུལ་གྱི་བསྐལ་པས་འདི་ཡོད་དུ་ཟིན་ཀྱང་རིགས་པར་འགྱུར་བ་མ་ཡིན་ནོ། །

[Block 2290]
དེ་ལྟར་ན༌[^1600]ཐམས་ཅད་མཐོང་བའི་ངང་ཚུལ་ཅན་མ༌[^1601]ཡིན་པ་གང་གིས་མ་བྱས་པའམ། ཅིག་ཤོས་ཀྱི་ཚིག་ནི་ཤིན་ཏུ་ལྐོག་ཏུ་གྱུར་པའི་དོན་ལ་མི་སླུ་བའམ་ཅིག་ཤོས་ལ་ངེས་པར་ནུས། ལ་ལ་ན་དེ་ལྟར་མཐོང་བའི་དོན་རྣམས་ཀྱང་རྣམ་པ་འགའ་ཞིག་གིས་གཞན་དུ་འགྱུར་ཏེ། དཔེར་ན་ཡུལ་ལ་ལར་འདུ་བྱ་བའི་ཁྱད་པར་ལས་ནི་ནིམ་པའི་འབྲས་བུ་དང་། སྐྱུ་རུ་རའི་འབྲས་བུ་མངར་མོར་ཆགས་པར་འགྱུར་ལ། ད་ལྟར་ནི་དེ་མ་མཐོང་བ་ཉིད་ཀྱིས་དེ་དག་ནི་སྤང་བར༌[^1602]བྱ་བ་མ་ཡིན་པ་ལྟ་བུའོ་ཞེས་བྱ་བས་བསྟན་ཟིན་ཏོ། །

[Block 2291]
དེ་བས་ན་མ་བྱས་པ་དང་ལོག་པའི་དོན་ཅན་དུ་འགྱུར་བ་ཞེས་བྱ་བ་འགལ་བ་མ་མཐོང་ངོ་། །མི་དམིགས་པ་འདི་ནི་སྣང་བའི་བདག་ཉིད་ཅན་དག་གི་སྒྲུབ་པར་བྱེད་པ་མ་ཡིན་ནོ་ཞེས་བཤད་ཟིན་ཏོ། །

[Block 2292]
དེ་བས་ན་ཅུང་ཞིག་ལོག་པའི་དོན་ཅན་གང་ཡིན་པ་དེ་ཐམས་ཅད་ནི་སྐྱེས་བུས་བྱས་པ་ཡིན་ནོ་ཞེས་བྱ་བར་ངེས་པ་མེད་པའི་ཕྱིར་ཁྱབ་བ་མེད་དོ། །

[Block 2293]
དེ་ལྟར་ན།

[Block 2294 [VERSE]]
གལ་ཏེ་རྗེས་འགྲོ་ལྡོག་པའམ། །
བསྒྲུབ་བྱའི་ཆོས་ཅན་ལ་ཡོད་ཉིད། །
དེ་ངེས་འབྲས་ཅན་ཤེས་པ་ཡིས། །
གྲུབ་པར་འགྱུར་བ་སྒྲུབ་བྱེད་ཡིན། །

[Block 2295]
དེ་སྐད་དུ་ཡང་བརྗོད་པ་གང་ཞིག་གཉི་ག་ལ་ངེས་པ་དེ་ཁོ་ན་སྒྲུབ་པར་བྱེད་པའམ་སུན་འབྱིན་པར་བྱེད་པ་ཡིན་ནོ། །

[Block 2296]
བརྗོད་པ་གང་ཡང་རུང་བ་ལ་གྲགས་པ་དང་ཐེ་ཚོམ་ཟ་བ་ནི་མ་ཡིན་ཏེ། ཡང་སྒྲུབ་པར་བྱེད་པ་ལ་ལྟོས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2297]
ཞེས་གསུངས་སོ། །

[Block 2298]
[^1603]འདི་ལ་འགལ་བ་མ་མཐོང་བ་ཅན་ཡོད་པ་གང་གིས་སྤོང་བར་བྱེད། དེ་བས་ན་ལྡོག་པ་འདི་ནི་ཐེ་ཚོམ་ཟ་བའི་ཕྱིར་སྒྲུབ་པར་བྱེད་པ་མ་ཡིན་ནོ། །

[Block 2299]
གཞན་ཡང་།

[Block 2300 [VERSE]]
གང་ལ་བསྒྲུབ་བྱའི་མི་མཐུན་ཕྱོགས། །
བཟློག་པ་ཉིད་བརྗོད་དེ་ཉིད་ནི། །
འདི་ཡི་ཕྱོགས་མཐུན་འགྱུར་དེའི་ཕྱིར། །
གཏན་ཚིགས་ཐམས་ཅད་རྗེས་འགྲོ་ཅན། །

[Block 2301]
ཅུང་ཞིག་ལོག་པའི་དོན་ཅན་གང་ཡིན་པ་དེ་ཐམས་ཅད་ནི་སྐྱེས་བུས་བྱས་པ་ཡིན་པ་དེ་ལྟར་ན། གཏན་ཚིགས་ཀྱི་མི་མཐུན་པའི་ཕྱོགས་ཀྱིས་བསྒྲུབ་པར་བྱ་བའི་མི་མཐུན་པའི་ཕྱོགས་ལ་ཁྱབ་པ་དེ་མེད་ན་མེད་པ་གྲུབ་པར་འགྱུར་རོ། །

[Block 2302]
དེ་མེད་པར་ཡོད་ན༌[^1604]ནི་དེས་ཁྱབ་པ་མི་རུང་བའི་ཕྱིར་རོ། །

[Block 2303]
རིགས་མི་མཐུན་པ༌[^1605]ལྡོག་པ་གྲུབ་པ་གང་ཡིན་པ་དེ་ཉིད་རྗེས་སུ་འགྲོ་བ་གྲུབ་པ་ཡིན་ཏེ། བསྒྲུབ་པར་བྱ་བའི་མི་མཐུན་པའི་ཕྱོགས་རྣམ་པར་གཅོད་པའི་མཚན་ཉིད་ཅན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2304]
དགག་པ་ཉིད་ཀྱིས་ཀྱང་བྱ་བ་འགྲུབ་པའི་ཕྱིར། རྗེས་སུ་འགྲོ་བ་མེད་པར་ལྡོག་པའི་ཁྱབ་པ་འགྲུབ་པ་མ་ཡིན་ནོ། །

[Block 2305]
དེ་བས་ན་གཏན་ཚིགས་འགའ་ཞིག་ཀྱང་རྗེས་སུ་འགྲོ་བ་མེད་པ་ཅན་ཞེས་བྱ་བ་མ་ཡིན་ཏེ། གཅིག་རྣམ་པར་གཅོད་པ་ནི་དེའི་རིགས་མི་མཐུན་པ་གྲུབ་པ་མེད་ན་མི་འབྱུང་བ་ཉིད་ཡིན་པའི་ཕྱིར་རོ།། །།

[Block 2306]
བམ་པོ་བཅུ་པ། མི་རྟག་པ་དང་བདག་མེད་པ་ཉིད་ལ་སོགས་པ་རྣམ་པར་གཅོད་པ་ན་ཡང་དེ་ལྟར་འགྱུར་རོ་ཞེ་ན། མ་ཡིན་ཏེ། ལྡོག་པ་རྣམ་པར་གཅོད་པ་ནི་དངོས་པོའི་ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2307]
དངོས་པོའི་ངོ་བོ་རྣམ་པར་གཅོད་པ་ན་དངོས་པོ་འཕེན་བར་བྱེད་པ་མ་ཡིན་ཞིང་མེད་པ་རྣམ་པར་གཅོད་པས་ཀྱང་ངེས་པར་དངོས་པོ་ཉེ་བར་འཇོག་པ་ཡིན་ཏེ། དངོས་པོ་དང་དངོས་པོ་མེད་པ་དག་ནི་ཕན་ཚུན་དབེན་པའི་ངོ་བོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2308]
ལྡོག་པ་གང་ཡིན་པ་དེ་དངོས་པོ་མེད་པའི་ངོ་བོ་ཅན་ལྡོག་པར་གྱུར་པས། དངོས་པོ་ཉེ་བར་འཇོག་པར་བྱེད་པ་དེ་ལྟར་བདག་མེད་པ་ལ་སོགས་པ་ནི་མ་ཡིན་ཏེ། རང་བཞིན་གྱི་ཁྱད་པར་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2309]
བྱ་བ་དང་ལོངས་སྤྱོད་པ་དག་བདག་གིར་བྱེད་པ་ལ་རང་དབང་མ༌[^1606]ཡིན་པའི་བདག་ཉིད་ནི་བདག་མེད་པའོ། །

[Block 2310]
དེ་ལ་རང་དབང་གི་མཚན་ཉིད་ཡིན་པའི་ཕྱིར་བདག་ཡིན་ནོ། །

[Block 2311]
དེ་བས་ན་ངོ་བོ་བདག་མེད་པ་ཡིན་གྱི་བདག་ལྡོག་པ་ཙམ་ནི་མ་ཡིན་ནོ། །

[Block 2312]
དེ་ལྟ་མ་ཡིན་ན་ཉེ་བར་བརྗོད་པ་མེད་པ་ལ་བྱས་པ་ཉིད་ལ་སོགས་པ་མི་རུང་བའི་ཕྱིར། དེ་ལས་བདག་མེད་པ་འགྲུབ་པར་མི་འགྱུར་རོ། །

[Block 2313]
གལ་ཏེ་བདག་རྣམ་པར་གཅད༌[^1607]ནས་བདག་མེད་པའི་ངོ་བོ་རྗོད་པར་བྱེད་པའི་ཕྱིར་སྐྱོན་ཡོད་པ་མ་ཡིན་ནོ་ཞེ་ན། མ་ཡིན་པས་དངོས་པོ་ལ་རེག་པའི་ཕྱིར། དངོས་པོའི་ངོ་བོ་དེ་ཉིད་བདག་མེད་པ་ཐོབ་པོ། །གང་གི་རྣམ་པར་བཅད་པ༌[^1608]དངོས་པོ་མེད་པའི་ངོ་བོ་མ་ཡིན་གྱི་དེའི་རྣམ་པར་གཅོད་པ་དངོས་པོའི་ངོ་བོ་ཡིན་ན་ཡང་དངོས་པོ་གྲུབ་པར་མི་འགྱུར་བའི་ཕྱིར། རྗེས་སུ་འགྲོ་བ་འཕངས་པ་མ་ཡིན་ནོ། །

[Block 2314]
དེ་ལྟར་ན་བདག་མེད་པ་ཡིན་ན་ཡང་དངོས་པོར་འགྲུབ་པར་མི་འགྱུར་ཏེ། དཔེར་ན་གསོན་པོའི་ལུས་འདི་ནི་བདག་མེད་པ་མ་ཡིན་ཏེ། སྲོག་ལ་སོགས་པ་དང་ལྡན་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2315]
མི་མཐུན་པའི་ཕྱོགས་དག༌[^1609]གི་ཁྱབ་པར་བྱ་བ་དང་ཁྱབ་པར་བྱེད་པ་དཔྱོད་པ་ན་སྲོག་ལ་སོགས་པ་དང་མི་ལྡན་པ་ཉིད་ལ་བདག་མེད་པ་ཉིད་མཐོང་བ་དང་དེ་མེད་ན་མེད་པའི་ཕྱིར། བདག་མེད་པ་དག་ཉིད་མེད་དུ་ཟིན་ཀྱང་། སྲོག་ལ་སོགས་པ་དག་ནི་བདག་ལ་གྲུབ་པར་འཇོག་པར་བྱེད་པ་མ་ཡིན་ནོ། །
--- END BLOCKS ---
