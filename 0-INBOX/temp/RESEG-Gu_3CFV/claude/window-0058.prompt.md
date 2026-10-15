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
[Block 2031]
ཚིགས་མ༌[^1282]ཟ་ན་ལྟུང་བྱེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་འདིས་བསྡུས་པ་ཡིན་ནོ། །

[Block 2032]
ཕབས་ཀྱི་ཆང་བུ་ནི་ཕྱེད་ཉིད་དོ་ཞེས་བྱ་བ་ནི་མྱོས་པར་འགྱུར་བའི་ཕྱེད་ཉིད་དེ་ཉེས་བྱས་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2033]
རྩ་བ་དང་སྡོང་བུ་དང་འདབ་མ་དང་མེ་ཏོག་དང་འབྲས་བུ་མྱོས་པར་འགྱུར་བ་རྣམས་ཀྱང་ངོ་། །མྱོས་པར་འགྱུར་བའི་དྲི་དང་རོ་བྲོ་བའི་ཐུག་པ་མྱོས་པར་མི་བྱེད་པ་རྣམས་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་ཕྱེད་ཉིད་དོ་ཞེས་བྱ་ལ༌[^1283]འཇུག་གོ། །

[Block 2034]
མདོག་ཙམ་མྱོས་པར་འགྱུར་བ་དང་འདྲ་བ་ལ་ནི་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་འདིར་གཞུང་ལས་མདོག་འབའ་ཞིག་མྱོས་པར་འགྱུར་བ་དང་འདྲ་བ་འཐུང་བ་ལ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2035]
མཁུར་བར་བསྲེལ་བ་དང་ལུས་སྐུད་པ་ལ་ནི་སྦྱོར་བ་དང་འདྲའོ་ཞེས་བྱ་བ་ནི་ཟ་བར་མི་འདོད་པ་ལ་གང་ཞིག་ཡན་ལག་གི་རྒྱན་འཆང་བ་མེད་པ་ནི་དེར་སྦྱོར་བ་ཉིད་ལ་སྙམ་པའི་བློ་བཟློག་པའི་དོན་དུ་འདིར་འདི་གསུངས་པའོ།[^1284] །སྨན་པའི་ལུང་གིས་འདི་དག་བྱེད་པ་ལ་ལྟུང་བ་མེད་པའི་ཚིག་གང་ཡིན་པ་དེས་དོན་འདི་བསྟན་པ་ཉིད་དེ་དེ་བས་ན་མདོ་འདི་ཡིན་ཏེ། བ་སྤུའི་བུ་ག་རྣམས་ལ་བཟའ་བ་ཞུགས་པ་ལུས་སྐུད་པ་བསྒྲུབ་པ་ཞེས་བྱ་བ་ནི་འདིར་སྐྱོན་ནོ། །

[Block 2036]
ནད་པ་ལ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ནི། ནད་པའི་མཁུར་བར་བསྲེལ་བ་དང་ལུས་བསྐུ་བ་དག་བྱེད་པ་ལ་ནི་ཞེས་བྱ་བ་དེ་མ་ཐག་པས་རྟོགས་པར་བྱའོ། །

[Block 2037]
མྱོས་པར་འགྱུར་བ་ལ་ནི་བཅས་པའི་ཁ་ན་མ་ཐོ་བ་གནང་བ་འཇུག་པ་མ་ཡིན་ཞེས་བྱ་བ་འདི་དེའི་ཕྱིར་རྩོམ་པའོ། །

[Block 2038]
མྱོས་པར་འགྱུར་བ་འཐུང་བའི་ལྟུང་བྱེད་དོ།། །།

[Block 2039]
དུས་མ་ཡིན་པར་འགྲོ་བའི་ལྟུང་བྱེད་ལ་བྱེད་པ་པོ་ཉིད་གང་ཞེ་ན། དེའི་ཕྱིར་ཤེས་གཙོ་བོ༌[^1285]ཞེས་བྱ་བ་སྨོས་ཏེ། འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་པོ་ཉིད་དོ། །གང་ལ་འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་པོ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་དུས་མ་ཡིན་པ་ཉིད་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏོ། རང་གི་ཕྱེད་ཡོལ་ནས་སྐྱ་རེངས༌[^1286]མ་ཤར་གྱི་བར་དུ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་བསྟན་པ་དེ་ནི་དུས་མ་ཡིན་པའི་མཚན་ཉིད་དོ། །

[Block 2040]
དགེ་སློང་ཁྱད་པར་ཅན་ཇི་ལྟ་བུ་ཞིག་ལ་དེ་བྱེད་པ་པོ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་དགེ་སློང་འཁོད་པ་ལ་མ་སྨྲས་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་གིས་དགེ་སློང་འཁོད་ཅིང་ཡོད་པ་ལ་མ་སྨྲས་པ་དེ་ནི་འདིར་བསྡུས་པ་ཡིན་ནོ། །

[Block 2041]
ཅི་ཞིག་བྱས་ན་དགེ་སློང་དེ་ལ་འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་པོ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་གྲོང་དུ་ཞུགས་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཁྱིམ་གཅིག་པའི་གནས་ཀྱང་གྲོང་ཉིད་ཡིན་པར་གསུངས་པས་དེའི་ཕྱིར་ཁང་པ་གཅིག་ཙམ་ཡོད་པའི་གནས་ཀྱང་གྲོང་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་དེ་ལ༌[^1287]བསྡུས་པ་ཉིད་དོ། །

[Block 2042]
གྲོང་པའི་ཆོས་དང་ལྡན་པ་ལྷག་པར་སྤྱོད་པའི་གནས་དག་ལ་གྲོང་གི་སྒྲ་འཇུག་པར་འགྱུར་བས་དེའི་ཕྱིར་མ་སྨྲས་པར་ཕྱི་རོལ་པའི་རབ་ཏུ་བྱུང་བའི་གནས་སུ་འཇུག་པ་ལ་ནི་ཁ་ན་མ་ཐོ་བ་མེད་པར་རིག་པར་བྱའོ། །

[Block 2043]
བསྐོར་བ་དང་བཅས་པའི་གྲོང་ལ་ནི་སྒོ་གཏན་གྱི་བར་དུ་འཇུག་ན་དེ་སྲིད་དུ་ཞུགས་པ་ཡོངས་སུ་རྫོགས་པར་རིག་པར་བྱའོ། །

[Block 2044]
མ་བསྐོར་བ་ལ་ནི་བསྐོར་བའི༌[^1288]མཐའི་བསྐོར་བས༌[^1289]དེས༌[^1290]བྱས་ནས་རྣམ་པར་གཞག་པར་རིག་པར་བྱའོ། །ཅི་ཞུགས་པ་ཐམས་ཅད་ལའམ་ཞེ་ན། དེའི་ཕྱིར་གལ་ཏེ་གཏད་པའི་བྱ་བ་མ་བྱུང་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེའི་དབང་གིས༌[^1291]འཇུག་པ་གང་ཡིན་པ་དེ་ལ་ནི་ལྟུང་བ་མེད་དོ། །

[Block 2045]
གཞན་དུ་རྒྱུ་བ་ལ་ནི་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་དེས་ནི་ཕྱོགས་གང་དུ་འགྲོ་བའི་ཕྱིར་སྨྲས་པའི་ཕྱོགས་དེ་ལས་གཞན་པ་དེའི་ཡན་ལག་ཏུ་གྱུར་པའི་ཕྱོགས་གང་ཡིན་པ་དེར་རྒྱུ་བ་ལ་ནི་ཉེས་བྱས་སོ། །

[Block 2046]
གྲོང་ཡོངས་སུ་ཆད་པར་བྱེད་ཅིང་ཅུང་ཟད་ཕྱོགས་འགའ་ཞིག་ཏུ་བྱེད་དམ། རིགས་འགའ་ཞིག་ལ་སྨྲ་བར་བྱེད་ན་ཉེས་བྱས་ལ་འཇུག་པ་ཡིན་ནོ། །

[Block 2047]
གྲོང་གཅིག་གོ༌[^1292]ཁྱིམ་གཞན་དུ་འགྲོ་ན་ཉེས་བྱས་ཀྱི་ཚིག་འདིའོ། །

[Block 2048]
གྲོང་གཞན་དུ་རྒྱུ་བ་ལ་ནི་ལྟུང་བྱེད་ཁོ་ནའོ། །

[Block 2049]
འདིར་གཞུང་ནི་ཞུ་བ་ལས་དང་པོར་གང་ན་ཉེ་འཁོར་གཅིག་ཡིན་པའི་ཉེ་འཁོར་ཤེས་པ་ལས་འདས་ཏེ། དེར་འགྲོ་ན་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2050]
འདིར་ཉེ་འཁོར༌[^1293]གཅིག་ཉིད་ཅེས་བྱ་བ་ནི་གྲོང་གཅིག་ཉིད་བསྟན་པར་རིག་པར་བྱའོ། །

[Block 2051]
གང་ཞིག་ཉེ་འཁོར་ཞེས་སྨོས་པ་འདིས་ཁྱིམ་གྱི་ཉེ་འཁོར་ལ༌[^1294]ཤེས་པར་བྱ་བ་འདིས་སྨྲས་ན་བྱེད་པ་པོ་ཉིད་དོ། །

[Block 2052]
འདི་ལ་དགེ་སློང་མེད་ན་དགེ་སློང་མ་ཡང་དེ་དང་འདྲའོ་ཞེས་བྱ་བ་ནི་བསླབ་པའི་གཞི་འདི་ལ་སྨྲ་བར་བྱ་བའི་ཕྱིར་དགེ་སློང་མེད་ན་དགེ་སློང་བཞིན་དུ་དགེ་སློང་མའོ། །

[Block 2053]
གང་ཞིག་དགེ་སློང་དུ་མ་གྱུར་པ་དང་། དགེ་སློང་མར་ཡང་མ་གྱུར་ལ༌[^1295]དེ་ལ་ནི་སྨྲ་བར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2054]
དེ་ཡང་མེད་ན་དགེ་ཚུལ་ལའོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་མ་མེད་ན་དགེ་ཚུལ་ལ་དགེ་སློང་དང་འདྲ་བར་རིག་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2055]
དེ་ཡང་མེད་ན་དགེ་སློབ་མའོ་ཞེས་བྱ་བ་ནི། དགེ་ཚུལ་དེ་ཡང་མེད་ན་དགེ་སློབ་མ་དགེ་སློང་དང༌[^1296]འདྲ་བའོ། །

[Block 2056]
དེ་ཡང་མེད་ན་དགེ་ཚུལ་མའོ་ཞེས་བྱ་བ་ནི། དགེ་སློབ་མ་དེ༌[^1297]ཡང་མེད་ན་དགེ་ཚུལ་མ་ཡོད་ན་དེ་ལ་སྨྲ་བར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2057]
འདིར་གཞུང་ནི་དགེ་སློང་གིས་དགེ་སློང་ལ་སྨྲ་བར་བྱ་ཞིང་དགེ་སློང་མ་དང་དགེ་ཚུལ་དང་། དགེ་སློབ་མ་དང་དགེ་ཚུལ་མ་ལ་ཡང་སྨྲ་བར་བྱ་སྟེ། འཁོར་ལོ་བཞིན་དུ་སྦྱར་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2058]
བརྡ་མི་ཕྲད་པ་ནི་མེད་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་གླེན་པ་དང་ལྐུགས་པ་དང་ཀླ་ཀློ་ལ་སོགས་པ་དག་དེས་བརྡ་མི་ཕྲད་པ་ཡིན་ན་སྨྲ་བར་བྱ་བ་མེད་པ་ཡིན་ནོ། །

[Block 2059]
ཡོད་པར་གྱུར་ཀྱང་བརྡ་མི་ཕྲད་པ་ལ་མ་སྨྲས་པར་ཞུགས་པ་ལ་ལྟུང་བ་མེད་དོ། །

[Block 2060]
འདིར་གཞུང་ནི་ཐ་མལ་པར་སྨྲས་པ་མི་ཐོས་པ་དང་། ཐ་མལ་པ༌[^1298]སྨྲ་མི་ཤེས་པ་གང་དག་ཡིན་པ་དེ་དང་ལྷན་ཅིག་འདུག་པས་ནི་དེ་དག་ལ་མ་སྨྲས་པར་འཇུག་པ་ལ་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2061]
མཚམས་གཞན་ན་གནས་པ་དང༌[^1299]གཞན་གྱི་ཕྱོགས་དང་མཐུན་པ་དག་ཀྱང་ངོ་ཞེས་བྱ་བ་ཡང་མེད་པ་ཉིད་ཅེས་བྱ་བར་སྦྱར་རོ། །

[Block 2062]
ཐ་དད་པ་ཉིད་ལ་ཕྱོགས་གཞན་ལ་ལྟུང་བ་གཞན་གྱི༌[^1300]ཕྱོགས་སུ་གྱུར་པར་རིག་པར་བྱའོ། །

[Block 2063]
འདིར་གཞུང་ནི་མཚམས་གཞན་གྱི་ས་ལ་གནས་པས་ནམ་མཁའ་ལ་གནས་པ་ལ་མ་སྨྲས་པར་འཇུག་པ་ལ་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ནོ། །

[Block 2064]
འདིར་གཞུང་ནི་ཅིག་ཤོས་ལ་ཡང་སྣ་ཚོགས་པ་དང་། འགྲོགས་པ་རྣམས་དང་ལྷན་ཅིག་ཏུ་འདུག་པས་དེ་དག་ལ་མ་སྨྲས་པར་འཇུག་པ་ལ་ལྟུང་བ་མེད་ཅེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ནོ། །

[Block 2065]
དེ་བཞིན་དུ་མི་མ་ཡིན་པ་རབ་ཏུ་བྱུང་ཞིང་བསྙེན་པར་རྫོགས་པ་དང་ལྷན་ཅིག་འདུག་པས་དེ་ལ་མ་སྨྲས་པར་འཇུག་པ་ལ་ལྟུང་བ་མེད་དོ། །

[Block 2066]
སྔོན་ལྟུང་བ་བྱུང་བ་དང་དང་པོ་འཁྲུགས་པ་དང་། རྐུ་ཐབས་སུ་གནས་པ་དང་། དགེ་སློང་མ་སུན་ཕྱུང་བ་དང་། མཐའི་ལྟུང་བ་བྱུང་བ་དང་། ལྷན་ཅིག་འདུག་པས་དེ་དག་ལ་མ་སྨྲས་པར་འཇུག་པ་ལ་ལྟུང་བ་མེད་དོ། །

[Block 2067]
དེ་བས་གཞན་པའི་དགེ་སྦྱོང་དང་བྲམ་ཟེ་དང་ལྷན་ཅིག་འདུག་པས་དེ་རྣམས་ལ་མ་དྲིས་པར་འཇུག་པ་ལ་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ཏེ། བསྙེན་པར་རྫོགས་པ་དང་བཅས་པའི་དབུས་སུ་གནས་པའི་དགེ་སློང་དང་དགེ་སློང་མ་དག་ཅེས་བྱ་བ་འདིས་བསྡུས་པར་རིག་པར་བྱའོ། །

[Block 2068]
རྫུ་འཕྲུལ་གྱིས་ནི༌[^1301]ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ལ། ནི་ཞེས་བྱ་བའི་སྒྲ་ནི་གྲོང་དུ་འཇུག་པ་ལ་བྱེ་བྲག་གི་དོན་ཏེ། འདིར་འདི་ནི་མེད་པར་ནི་གོ་བ༌[^1302]མ་ཡིན་ནོ། །

[Block 2069]
གཞུང་གི་སྡེབ་སྦྱོར་བསྒྲུབ་པའི་དོན་འདི་སྦྱར་བ་ཡིན་ནོ། །

[Block 2070]
འདིར་གཞུང་ནི་རྫུ་འཕྲུལ་གྱིས་ནམ་མཁའ་ལ་འཇུག་ན་མ་སྨྲས་ཀྱང་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །
--- END BLOCKS ---
