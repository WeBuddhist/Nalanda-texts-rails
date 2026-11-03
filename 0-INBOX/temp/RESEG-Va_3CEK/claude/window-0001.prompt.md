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
[Block 36]
གཞན་དག་ནི་གང་ཟག་ལས་སོ། །

[Block 37]
བྱེ་བྲག་ཏུ་སྨྲ་བ་འདུལ་བ་པ༌[^11]རྣམས་ན་རེ་རྣམ་པ་བཅུས་བསྙེན་པར་རྫོགས་སོ་ཞེས་ཟེར་བ་བསྡུ་བའི་ཕྱིར་སོགས་པའི་སྒྲ་སྨོས་ཏེ། རང་འབྱུང༌[^12]གིས་ནི་སངས་རྒྱས་དང་། །རང་སངས་རྒྱས་རྣམས་སོ། །

[Block 38]
ངེས་པར་འཇུག་པས་ནི་རྟེན༌[^13]ལྔ་པོ་རྣམས་སོ། །

[Block 39]
དགེ་སློང་ཚུར་ཤོག་ཅེས་བྱས་པས་ནི་གྲགས་པ་ལ་སོགས་པ་རྣམས་སོ། །

[Block 40]
སྟོན་པར་ཁས་བླངས་པས་ནི་འོད་སྲུངས་ཆེན་པོའོ། །

[Block 41]
དྲི་བ༌[^14]མཉེས་པས་ནི་ལེགས་སྦྱིན་ནོ། །

[Block 42]
བླ་མའི་ཆོས་ཁས་བླངས་པས་ནི་སྐྱེ་དགུའི་བདག་མོ་ཆེན་མོའོ། །

[Block 43]
ཕོ་ཉས་ནི་ཆོས་སྦྱིན་ནོ། །

[Block 44]
འདུལ་བ་འཛིན་པར༌[^15]གཏོགས་པ་ལྔས་ནི་མཐའ་འཁོབ་ཀྱི་མི་རྣམས་སོ། །

[Block 45]
བཅུའི་ཚོགས་ཀྱིས་ནི་དབུས་ཀྱི་མི་རྣམས་སོ། །

[Block 46]
སྐྱབས་སུ་འགྲོ་བ་ལན་གསུམ་བཟླས་པས་ནི་སྡེ་བཟང་དྲུག་ཅུའི་ཚོགས་ཀྱིས་བསྙེན་པར་རྫོགས་པར་བྱས་པ་རྣམས་ཏེ། དེ་དག་གི༌[^16]སོ་སོར་ཐར་པའི་སྡོམ་པ་ནི་གདོན་མི་ཟ་བར་རྣམ་པར་རིག༌[^17]བྱེད་ལ་རག་ལུས་པ་མ་ཡིན་ནོ། །

[Block 47 [HEADING]]
### སོ་སོར་ཐར་པའི་སྡོམ་པ་ཡང་དག་པར་བླང་བའི་དུས། ^1-5-0

[Block 48]
ཡང་སོ་སོར་ཐར་པའི་སྡོམ་པ་དེ་ཡང་དག་པར་བླངས་པ༌[^18]ན་དུས་ཇི་སྲིད་ཅིག་གི་བར་དུ་ཡང་དག་པར་བླང་བར་བྱ་ཞེ་ན།

[Block 49 [VERSE]]
ཇི་སྲིད་འཚོ་དང་ཉིན་ཞག་ཏུ། །
སྡོམ་པ་ཡང་དག་བླང་བར་བྱ། །

[Block 50 [VERSE]]
རིས་བདུན་གྱི་སོ་སོར་ཐར་པའི་སྡོམ་པ་ནི། །
ཇི་སྲིད༌[^19]འཚོའི་བར་དུ་ཡང་དག་པར་བླང་བར་བྱའོ། །

[Block 51]
བསྙེན་གནས་ཀྱི་སྡོམ་པ་ནི་ཉིན་ཞག་ཏུའོ་ཞེས་བྱ་བ་དེ་ལྟར་ངེས་སོ། །ཅིའི་ཕྱིར་ཞེ་ན། དུས་ཀྱི་མཐའ་ནི་གཉིས་ཏེ། སྲོག་གི་མཐའ་དང་། ཉིན་ཞག་གི་མཐའོ། །

[Block 52]
ཟླ་བ་ཕྱེད་ལ་སོགས་པ་ནི་ཉིན་ཞག་བཟླས་པས་སོ། །

[Block 53]
དུས་ཞེས་བྱ་བའི་ཆོས་དེ་ཅི་ཞིག་ཅེ་ན། དེ་ནི་འདུ་བྱེད་ཡོངས་སུ་སྟོན་པའི་ཚིག་བླ་དགས་ཡིན་ཏེ། སྣང༌[^20]བའི་གནས་སྐབས་ལ་ནི་གླིང་དག་ན་ཉིན་པར་ཞེས་བྱ་ལ། མུན་པའི་གནས་སྐབས་ལ་ནི་མཚན་མོ་ཞེས་བྱའོ། །

[Block 54]
རེ་ཞིག་ཇི་སྲིད་འཚོའི་བར་དུ༌[^21]ནི་ཡང་དག་པར་བླངས་པ་ཡོད་ཀྱང་ལུས་སྐལ་བ་མི་འདྲ་བའི་ཕྱིར་དང་། དེས་ཀྱང་། དེར༌[^22]སྦྱོར་བ་མ་བྱས་པའི་ཕྱིར་དང་། མི་དྲན་པའི་ཕྱིར་དང༌[^23]སྡོམ་པ་མི་སྐྱེ་བར་རིགས་ན། ཡང་ཉིན་ཞག་གི་འོག་ཞག་ལྔ་འམ་ཞག་བཅུ་ཡང་རུང་སྟེ། བསྙེན་གནས་ཀྱི་སྡོམ་པ་ཡང་དག་པར་བླངས་པའི་བསྙེན་གནས་ཀྱི་སྡོམ་པ་ཡང༌[^24]མང་པོ་སྐྱེ་བ་ལ་སུ་ཞིག་བགེགས༌[^25]བྱེད། བཅོམ་ལྡན་འདས་ཀྱིས་མདོ་ལས་གང་ཉིན་ཞག་གི་བསྙེན་གནས་ཁོ་ན་བསྟན་པ་འདིས་ན་བགེགས་བྱེད༌[^26]པ་ཡོད་དོ། །

[Block 55]
ད་ནི་འདི་དཔྱད་པར་བྱ་སྟེ། རེ་ཞིག་ཅི་བཅོམ་ལྡན་འདས་ཀྱིས་ཅི༌[^27]ཉིན་ཞག་གི་འོག་ཏུ་སྡོམ་པ་མི་སྐྱེ་བར་གཟིགས་ནས་ཉིན་ཞག་པའི་བསྙེན་གནས་བསྟན་ཏམ། འོན་ཏེ་དབང་པོ་གདུལ་དཀའ་བ་རྣམས་ཉིན་ཞག་པའི་སྡོམ་པ་ཡང་དག་པར་བླངས་པ་ལ་ཡང་དག་པར་སྦྱོར་བའི་ཆེད་གཅིག་ཡིན། དེ་དེ་ལྟར་བརྟག་ག་ལ་ནུས། ཕྱིན་ཆད་སྡོམ་པ་སྐྱེ་བ༌[^28]ལ་ཡང་རིགས་པ་དང་འགལ་བ་ནི་མེད་པའི་ཕྱིར་རོ། །

[Block 56]
ཕྱིན་ཆད་པོ་འདི་སུ་ལ་ཡང་མ་བསྟན་པས་བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ནི་མི་འདོད་དོ། །

[Block 57 [HEADING]]
### སྡོམ་པ་མ་ཡིན་པའི་དུས་ངེས་པ། ^1-6-0

[Block 58]
ད་ནི་སྡོམ་པ་མ་ཡིན་པའི་དུས་ངེས་པ་གང་ཡིན་ཞེ་ན། ཉིན་ཞག་པ་ཡི་སྡོམ་མིན་མེད། །ཇི་སྲིད་འཚོའི་བར་དུ་སྡིག་པའི་ཆོས་ཁས་བླངས་པ་ལས་སྡོམ་པ་མ་ཡིན་པ་སྐྱེའོ༌[^29]ཇི་ལྟར་བསྙེན་གནས་པ་བཞིན་དུ་ཉིན་ཞག་པ་ནི་མེད་དོ། །ཅིའི་ཕྱིར་ཞེ་ན། དེ་དེ་ལྟར་ནོད་མེད་ཅེས་གྲག །ཇི་ལྟར་བསྙེན་གནས་པ་ལྟར་བདག་ནི་ཉིན་ཞག་གཅིག་ཏུ་སྡོམ་པ་མ་ཡིན་པ་ལ་གནས་པར་གྱུར་ཅིག་ཅེས་སྡོམ་པ་མ་ཡིན་པ་ཡང་དག་པར་ལེན་པ་ནི་སུ་ཡང་མེད་དེ། ལས་སྨད་པ་ཡིན་པའི་ཕྱིར་རོ་ཞེས་གྲག་གོ། །

[Block 59]
དེ་ལྟ་ན་བདག་ནི་ཇི་སྲིད་འཚོའི་བར་དུ་སྡོམ་པ་མ་ཡིན་པ་ལ་གནས་པར་གྱུར་ཅིག་ཅེས་ལེན་པ་ནི༌[^30]སུ་ཡང་མེད་པས་ཇི་སྲིད་འཚོའི་བར་དུ་ཡང་དེ་འཐོབ་པར་མི་འགྱུར་རོ། །

[Block 60]
གལ་ཏེ་དེ་ལྟར་མི་ལེན་མོད་ཀྱི་འོན་ཀྱང་གཏན་དུ་ལོག་པར་ཞུགས་པའི་བསམ་པས་བྱ་བ་དེ་བྱེད་པ་ན་སྡོམ་པ་མ་ཡིན་པ་འཐོབ་པར་འགྱུར་གྱི་དུས་གཞན་གྱི་བར་དུ་ལོག་པར་ཞུགས་པས་ནི་མ་ཡིན་ནོ། །

[Block 61]
བསྙེན་གནས་པའི་སྡོམ་པ་ནི་གཏན་དུ་བའི་བསམ་པ་མ་ཡིན་ཡང་སྡོམ་པ་དོན་དུ་གཉེར་བའི་ཕྱིར་ཡང་དག་པར་ལེན་པའི་སྟོབས་བསྐྱེད་པས་འཐོབ་པ་ཉིད་དོ། །

[Block 62]
གལ་ཏེ་འགའ་ཞིག་སྡོམ་པ་མ་ཡིན་པ་དོན་དུ་གཉེར་ཞིང་དུས་གཞན་གྱི་བར་དུ་སྡོམ་པ་མ་ཡིན་པ་ཡང་དག་པར་ལེན་པར་འགྱུར་ན་དེས་ཀྱང་གདོན་མི་ཟ་བར་འཐོབ་པར་འགྱུར་རོ། །

[Block 63]
དེ་ནི་མ་མཐོང་བས་དེ་ལྟར་རྣམ་པར་མི་གཞག་གོ། །

[Block 64]
མདོ་སྡེ་པ་རྣམས་ན་རེ་སྡོམ་པ་མ་ཡིན་པ་ཡང་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་བཞིན་དུ་རྫས་སུ་ནི་མེད་ཀྱི་སྡིག་པ་བྱ་བའི་བསམ་པ་རྗེས་སུ་འབྲེལ་བ་དང་བཅས་པ༌[^31]དེ་ཉིད་སྡོམ་པ་མ་ཡིན་པ་ཡིན་ཏེ། དེས་ན་སེམས་དགེ་བ་ལ་ཡང་དེ་མ་སྤངས་པའི་ཕྱིར་དེ་དང་ལྡན་པ་ཞེས་བྱའོ། །

[Block 65 [HEADING]]
### བསྙེན་གནས་མནོད་པ། ^1-7-0

[Block 66]
ཡང་བསྙེན་གནས་ཉིན་ཞག་ཏུ་ནོད༌[^32]ན་ཅི་ལྟར༌[^33]མནོད་པར༌[^34]བྱ་ཞེ་ན།

[Block 67 [VERSE]]
དམའ་བར་འདུག་སྨྲས་བཟླས་པ་ཡིས། །
མི་བརྒྱན་ནམ་ནི་ནང་པར༌[^35]དུ། །
བསྙེན་གནས་ཡན་ལག་ཚང་བར་ནི། །
ནང་པར་གཞན་ལས་མནོད་པར༌[^36]བྱ། །

[Block 68]
དམའ་བར་འདུག་པ་ནི་ཙོག་ཙོག་པོར་འདུག་པའམ་པུས་མོ་བཙུགས་ནས། ཐལ་མོ་སྣོལ་བའམ་ཐལ་མོ་སྦྱར་བ་སྟེ། ནད་པ་ནི་མ་གཏོགས་སོ། །

[Block 69]
མ་གུས་པ་ནི་སྡོམ་པ་མི་སྐྱེའོ། །

[Block 70]
འབོགས་པ༌[^37]པོས་ཚིག་མ་སྨྲས་པར་སྔར་ཡང་སྨྲ་བར་མི་བྱ་ལ་ཁ་བསྙམས༌[^38]ཏེ་སྨྲ་བར་ཡང་མི་བྱ་སྟེ། དེ་ལྟར་ན་འདི་གཞན་ལས་མནོས་པ༌[^39]ཡིན་གྱི་གཞན་དུ་འབོགས་པ༌[^40]དང་ནོད་པ་འགྲུབ་པར་མི་འགྱུར་རོ། །

[Block 71]
མི་བརྒྱན་པ་ནི་རྒྱན༌[^41]ནར་མ་མ༌[^42]གཏོགས་ཏེ་རྒྱན་ནར་མ་ནི་མཚར་གཅིག་རྒྱགས་པར་མི་བྱེད་དོ། །

[Block 72]
ནམ་ནངས་ཀྱི་བར་དུ་མནོད་པར་བྱ་བ་ནི་ཉི་མ་ཤར་གྱི་བར་དུའོ། །

[Block 73]
ཡན་ལག་བརྒྱད་ཚང་བར་མནོད་པར༌[^43]བྱ་བའི༌[^44]ཡན་ལག་མ་ཚང་བར་ནི་མ་ཡིན་ནོ། །

[Block 74]
ནང་པར་ནི་རེ་ཞིག་ཉི་མ་ཤར་བའི་ཚེ་སྟེ། ཉིན་ཞག་པའི་སྡོམ་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 75]
གང་གིས་ཚེས་བརྒྱད་ལ་རྟག་ཏུ་བསྙེན་གནས་ལ་གནས་པར་བྱའོ་ཞེས་སྔོན་ཡང་དག་པར་བླང་བར་བྱས་པ་དེ༌[^45]ནི་ཟས་ཟོས་ནས་ཀྱང་མནོད་པར༌[^46]བྱའོ། །
--- END BLOCKS ---
