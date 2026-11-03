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
[Block 2346]
རྒྱུའི་ཚོགས་པ་ཡོད་ན་འབྲས་བུ་དང་བྲལ་བ་མི་རིགས་ཏེ། རྒྱུ་ཉིད་མ་ཡིན་པར་ཐལ་བའི་ཕྱིར་རོ། །

[Block 2347]
གལ་ཏེ་སྔགས་ཀྱི་སྦྱོར་བ་ཡན་འགར༌[^1624]བ་ལས་འདོད་པ་གྲུབ་པ་མ་ཡིན་ཏེ། དེ་ནི་ཆོ་ག་ལ་ལྟོས་པ་ཉིད་ཀྱི་ཕྱིར་རོ་ཞེ་ན། ལྟོས་པ་ཡིན་ན་དོན་མེད་འགྱུར། །གལ་ཏེ་སྔགས་ཀྱི་ཆོ་ག་ལས་སམ། གཞན་ལས་རང་བཞིན་ཕུལ་དུ་བྱུང་བ་འགའ་ཞིག་ཐོབ་པར་འགྱུར་ན་དེ་ལ་དེའི་ནུས་པ་ལ་ལྟོས་པར་འགྱུར་ཏེ། རྟག་པ་ལ་དེ་ཡོད་པ་མ་ཡིན་ནོ་ཞེས་བཤད་ཟིན་ཏོ། །

[Block 2348]
དེ་བས་ན་ནུས་པ་མེད་པ་འདི་ལ་ཅི་ཕྱིར་ལྟོས་པར་འགྱུར། དེ་ལྟར་ན་ལྟོས་པ་མེད་པ་རྟག་ཏུ་བྱེད་པའམ། ཅུང་ཞིག་ཀྱང་བྱེད་པར་མི་འགྱུར་ཏེ།

[Block 2349 [VERSE]]
ཁྱད་པར་མེད་པའི་ཕྱིར་རོ། །
གལ་ཏེ་དངོས་ནུས་དེ་འདྲ་ན། །
དེ་དག་ཀུན་གྱི་སྒྲུབ་བྱེད་འགྱུར། །
ལེགས་བྱས་མིན་ནི་བྱེད་པ་པོའི། །
ཁྱད་པར་ལ་ནི་ལྟོས་མི་རུང་། །

[Block 2350]
གལ་ཏེ་དངོས་པོའི་ནུས་པ་ཉིད་ཀྱི་སྔགས་རྣམས་ཀྱིས་གྲུབ་པ་སྟེར་བར་འགྱུར་ན། དེ་དག་གིས་མཆོད་སྦྱིན་བྱེད་པའམ། གཞན་འགའ་ཞིག་ཀྱང་སྤང་བར༌[^1625]མི་འགྱུར་རོ། །

[Block 2351]
གཞན་ལ༌[^1626]ནི་རང་བཞིན་གྱིས་དེའི་ངོ་བོ་ཅན་མ་ཡིན་པར་མི་འགྱུར་ཏེ། དེས་དེ་སྨད་པ་མེད་པའི་ཕྱིར་དང་། གཞན་གྱིས་བསྟོད་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 2352]
འགའ་ཞིག་ཀྱང་ལྷན་ཅིག་རྒྱུ་དང་འབྲས་བུ་ངོ་བོར་མི་རུང་བའི་ཕྱིར་དང་། ཉེ་བ་དང་བསྐལ་པ༌[^1627]མེད་པའི་ཕྱིར་རོ། །

[Block 2353]
དེ་ཉིད་ཀྱི་ཕྱིར་འདི་ལེགས་པར་བྱས་པ་ཉིད་མ་ཡིན་པའི་ཕྱིར། སྦྱོར་བ་པོ་ཡང་ཡོད་པ་མ་ཡིན་ན། གང་ལས་སྦྱོར་བ་པོས་འབྲས་བུ་ཐོབ་པར་འགྱུར།

[Block 2354 [VERSE]]
དངོས་པོ་འདུས་བྱས་པ་ཡི་ཡང་། །
དངོས་པོའི་ཐ་དད་ཐ་དད་བྱེད། །
སྦྱོར་བའི་ཁྱབ་པར་ལ་ངེས་པ། །
ནུས་ལ༌[^1628]མ་ཡིན་བརྡ་ལ་འགྱུར། །

[Block 2355]
དངོས་པོ་མི་རྟག་པ་བྱ་བའི་ཁྱད་པར་ཅན་དག་ནི་དེའི་རྒྱུ་ལས་རང་བཞིན་ཐ་དད་པ་ཡིན་ན། དེ་ལས་ཕུལ་དུ་བྱུང་བ་ཐོབ་པ་ཉིད་ཀྱི་ཕྱིར། གཞན་དུ་རྣམ་པ་གཞན་དུ་འགྱུར་ལ། ཐ་དད་པ་མེད་ན་མ་ཡིན་ཏེ། རྒྱུའི་ཁྱད་པར་མེད་ན་འབྲས་བུའི་ཁྱད་པར་མེད་པའི་ཕྱིར་རོ། །

[Block 2356]
ཁྱད་པར་ཡོད་ན་ནི་རྒྱུ་མེད་པ་ཅན་དུ་ཐལ་བའི་ཕྱིར་རོ་ཞེས་མང་དུ་བཤད་ཟིན་ཏོ།། །།

[Block 2357]
དེ་བས་ན་རང་བཞིན་ཕུལ་དུ་བྱུང་བའི་ཕྱིར། འབྲས་བུ་འབྱིན་པའི་སྔགས་འདི་འབྲས་བུ་ཡིན་དུ་ཟིན་ཀྱང་། དམངས་རིགས་ལ་སོགས་པའི་སྦྱོར་བ་ལ་ཡང་རྣམ་པ་གཞན་དུ་མི་འགྱུར་ཏེ། དམངས་རིགས་དང་བྲམ་ཟེ་ཞེས་བྱ་བའི་སྐྱེས་བུ་དག་གི་རང་བཞིན་ཐ་དད་པ་ནི༌[^1629]མེད་པའི་ཕྱིར་རོ། །

[Block 2358]
སྐྱེས་བུའི་འདོད་པའི་རྗེས་སུ་བྱེད་པ་ཅན་གྱི་མིང་དང་ཐ་སྙད་ཀྱི་ཁྱད་པར་ལས་རང་བཞིན་གྱི་ཁྱད་པར་དང་འབྲེལ་པ་ཅན་གྱི་དོན་རྣམས་གཞན་ཉིད་མ་ཡིན་ནོ། །

[Block 2359]
གལ་ཏེ་དེ་དག་གི་རིགས་ཀྱི་བྱེ་བྲག་ཡོད་དོ། །

[Block 2360]
ཞེ་ན། དེ་ནི་དབྱིབས་དང་ཡོན་ཏན་དང་ནུས་པའི་ཁྱད་པར་ལ་མཐོང་སྟེ། བ་ལང་དང་རྟ་བཞིན་ནོ། །

[Block 2361]
དེ་དག་ནི་འཇིག་རྟེན་གྱིས་བསྟན་པ་མེད་པར་རྟོགས་པར་འགྱུར་རོ། །

[Block 2362]
དེ་དང་འདྲ་བ༌[^1630]འདི་དག་ལ་ཡོན་ཏན་རྣམ་པར་ངེས་པ་ཅུང་ཞིག་ཀྱང་མ་མཐོང་ངོ་། །མ་མཐོང་བར་ཡང་ཇི་ལྟར་ཁྱད་པར་རྟོགས་པར་འགྱུར། འཇིག་རྟེན་གྱི་རྟོགས་པའི་ཁྱད་པར་མིང་ཐ་དད་པའི་རྗེས་སུ་འགྲོ་བ་ཅན་གང་ཡིན་པ་དེ་ཡང་རིགས་ཀྱི་ཁྱད་པར་མེད་དུ་ཟིན་ཀྱང་བྱ་བའི་ཁྱད་པར་ནན་ཏན་དུ་བྱེད་པའི་ཕྱིར་དང་རྗེས་སུ་འགྲོ་བའི་ཕྱིར་འགྱུར་ཏེ། འཚོ་བྱེད་དང་ཚོང་པའི་ཐ་སྙད་ལ་སོགས་པ་བཞིན་ནོ། །

[Block 2363]
དེ་བས་ན་སྔགས་འདི་ཁྱད་པར་མེད་པར་སྦྱར་བར་འགྱུར་ན། དེ་ལས་ཁྱད་པར་མེད་པའི་རང་བཞིན་ཉིད་སྒྲུབ་པར་བྱེད་དོ། །

[Block 2364]
དེས་ན༌[^1631]ཁྱད་པར་མེད་པ་ཁོ་ནར་འབྲས་བུ་འབྱིན་པར་འགྱུར་རོ། །

[Block 2365]
གང་གི་ཚེ་བརྡ་ལས་དེ་དག་གི་འབྲས་བུ་འབྱིན་པ་དེའི་ཚེ་སྐྱོན་འདི་ཡོད་པ་མ་ཡིན་ཏེ། བརྡ༌[^1632]བྱེད་པའི༌[^1633]འདོད་པ་ལས་འབྲས་བུ་སྐྱེ་བར་ངེས་པའི་ཕྱིར་རོ། །

[Block 2366]
དངོས་པོ་རང་བཞིན་གྱིས་གནས་པ་ཅན་དག་ནི་དེའི་སྒོ་ནས་ཐལ་བར་རིགས་པ་ཡིན་གྱི། སྐྱེས་བུའི་འདོད་པས་གནས་པ་ཅན་དག་མ་ཡིན་ཏེ། དེ་དག་ནི་རྣམ་པ་འགའ་ཞིག་གིས་འཇུག་པའི་ཕྱིར་རོ། །

[Block 2367]
གང་ཡང་སྦྱོར་བ་པོས་འབྲས་བུ་ཐོབ་པོ་ཞེས་བྱ་བ་འདོད་པའི་དོན་ལ་རུང་བ་སྐྱེད་པར་བྱེད་པའམ། རྒྱུ་ཡོངས་སུ་འགྱུར་བའི་སྦྱོར་བ་མཐོང་ངོ་། །དེ་གཉི་གའི་ཁྱད་པར་བསྐྱེད་པ་ན་འགྱུར་རོ། །

[Block 2368]
དེ་ལྟར་མ་ཡིན་ན།

[Block 2369 [VERSE]]
ཁྱད་པར་བྱར་མེད་ཅན་ཡིན་ན། །
སྦྱོར་བ་པོས་ནི་ཅི་ཞིག་བྱེད། །
གང་གིས་དེ་ལས་ལས༌[^1634]འབྲས་བུ། །
ཐོབ་ཀྱི་གཞན་གྱིས་ནི་མ་ཡིན། །

[Block 2370 [VERSE]]
གལ་ཏེ་སྦྱོར་བ་མངོན་གསལ༌[^1635]ཡིན། །
དེ་ནི་གོང་དུ་བསལ་ཟིན་ཏོ། །

[Block 2371]
རྟག་པ་རྣམས་འགའ་ཞིག་ཀྱང་མངོན་པར་གསལ་བ་མ་ཡིན་ནོ་ཞེས་བཤད་ཟིན་ཏོ། །

[Block 2372]
གང་གི་ཕྱིར་མངོན་བར་གསལ་བར་བྱེད་པ་ནི་སྦྱོར་བ་པོར་འགྱུར།

[Block 2373 [VERSE]]
གང་ལས་བློ་དེ་གསལ་ཡིན་ཏེ། །
དེ་ནི་འབྲས་ལའང་གལ་ཏེ་སྦྱོར། །
སྨྲ་བ་པོ་གསལ༌[^1636]རྒྱུ་ཡིན་བས། །
ཉན་པ་པོ་ཡི་འབྲས་འབྲེལ་འགྱུར། །

[Block 2374]
སྒྲ་ནི་གཞན་ལས་རང་གི་ངོ་བོར་འགྱུར་བ་དང་། སྒྲིབ་པར་བྱེད་པ་ལ་བྲལ་བ་གསལ་བ་མ་ཡིན་གྱི། འོན་ཀྱང་དེའི་ཡུལ་ཅན་གྱི་ཤེས་པ་ཡིན་ཏེ། ཐོས་པ་མེད་པར་གསལ་བ་བརྗོད་པ༌[^1637]མེད་པའི་ཕྱིར་རོ། །

[Block 2375]
དེ་ལ་གལ་ཏེ་སྨྲ་བ་པོ་བློའི་རྒྱུར་འགྱུར་ན། དེ་ནི་ཉན་པ་པོ་ལ་མཚུངས་པའི་ཕྱིར་དེའི་འབྲས་བུ་ཡང་སྨྲ་བ་པོ་དང་འདྲ་བར་ཐོབ་པར་འགྱུར་རོ། །

[Block 2376]
དེའི་བློའི་རྒྱུ་ཉིད་ལས་གཞན་དུ་སྨྲ་བ་པོ་དེའི་ངོ་བོ་གཞན་འགའ་ཞིག་ཀྱང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2377]
གལ་ཏེ་ཉན་པ་པོའི་བློ་ནི་གཞན་གྱི་ཁྱད་པར་ཅན་ཡིན་གྱི་སྨྲ་བ་པོ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཁྱད་པར་ཡིན་ནོ་ཞེ་ན། ཉན་པ་པོ་ལ་སྨྲ་བ་པོའི་ཉེ་བར་སྦྱོར་བ་ཡང་ཅི་ཞིག་ཡོད་ན་གང་གིས་ན་ཁྱད་པར་འདོད། གལ་ཏེ་དེ་ལས་སྒྲ་ཐོས་པ་ཡིན་ནོ་ཞེ༌[^1638]ན། ཇི་ལྟར་ན་དེ་ལས་ཤེས།[^1639] དེ་ཉིད་བརྒལ་ཞིང་བརྟག་པ་མ་ཡིན་ནམ། འབྲེལ་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 2378]
ཡུལ་ཉེ་བར་འཇོག་པ་ལས་འདི་འདིའི་ཐོས་པར་བྱེད་པ་པོར་འགྱུར་ན། དེ་ཡང་ནུས་པ་མ་ཡིན་ཏེ། རྟག་པ་དེ་ཡང་རྣམ་པ་འགའ་ཞིག་ཏུའང་འགྱུར་བ་མེད་ཕྱིར་རོ། །

[Block 2379]
དབང་པོ་ལེགས་པར་བྱས་པ་ལ་སོགས་པ་ཡང་བཤད་ཟིན་ཏོ། །

[Block 2380]
གལ་ཏེ་བདག་མཉན་པར་བྱ། བདག་གིས་ཉན་དུ་བཅུག་གོ་ཞེས་བྱ་བ་དེ་དག་གི་ཤེས་པ་ལས་སྨྲ་བ་པོ་དང༌[^1640]ཉན་པ་པོ་ཐ་དད་པ་ཡིན་ནོ། །

[Block 2381]
ཞེ་ན། འཁྲུལ་པ་ཙམ་ཕན་གདགས་པར་བྱ་བ་དང་། ཕན་འདོགས་པར་བྱེད་པ་མེད་པ་ཅན་ཡིན་པའི་ཕྱིར་དེའི་ངོ་བོ་ནི་ཤིན་ཏུ་ཐལ་བར་འགྱུར་ཏེ། འཁྲུལ་པས་གཞན་དག་ལ་ཡང་ཤེས་པ་མཐོང་བའི་ཕྱིར་རོ། །

[Block 2382]
རྣམ་པ་ཐམས་ཅད་དུ་ཕན་འདོགས་པ་མེད་པ་ལ་ཡང་དེ་ལྟ་བུའི་ཤེས་པ་རིགས་པ་མ་ཡིན་ཏེ། ཐམས་ཅད་དག་ཕན་ཚུན་དེ་ལྟར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2383]
འཁྲུལ་པ་ཡང་འགའ་ཞིག་ལས་ཕན་བཏགས་པ་ཡོད་ཅིང་འགའ་ཞིག་ཉེ་བས་གཞན་དུ་འགྱུར་རོ། །

[Block 2384]
དེ་ཡང་བརྒྱུད་པས་ཕན་བཏགས་པ་མེད་ན་མི་འགྱུར་རོ། །

[Block 2385]
དེ་བས་ན་སྨྲ་བ་པོ་དང་ཉན་པ་པོ་གསལ་བའི་རྒྱུ་ཉིད་དུ་ཁྱད་པར་མེད་པའི་ཕྱིར། འབྲས་བུ་དང་ལྡན་པར་མཚུངས་པར་འགྱུར་རོ། །
--- END BLOCKS ---
