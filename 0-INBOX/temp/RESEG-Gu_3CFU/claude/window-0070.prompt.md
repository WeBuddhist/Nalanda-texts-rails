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
[Block 2451]
ཏིལ་ཙམ་ལ་སོགས་པ་ལ་རིགས་པའི༌[^1683]ཕྱིར་དང་། ཚད་མེད་པ་ཉིད་ཀྱིས་ཀྱང་དགེ་སློང་རྣམས་ལ་ཡོངས་སུ་རྫོགས་པ་ཉིད་མི་རིགས་པ་ཉིད་ཀྱི་ཕྱིར་དངོས་གཞིའི་ཆོ་ག་ལ་རྣམ་པར་མི་འབྱེད་པ་ཉིད༌[^1684]ཀྱི་ཕྱིར་སྐལ་བ་རྣམ་པར་བཅད་པས་གནས་པ་མི་རིགས་པའི་ཕྱིར་རོ། །

[Block 2452]
བདག་པོ་ཐ་དད་པ་མ་ཡིན་པ་ནི་རང་གི་དང་འདྲའོ༌[^1685]ཞེས་བྱ་བ་ནི་གང་དང་འབྲེལ་བའི་རྫས་དེ་ཉིད་ལ་རྐུ་བ་གང་ཡིན་པ་དཔེར་ན་དགེ་འདུན་གྱི་ཡོ་བྱད་ལ་གནས་ནས་དགེ་འདུན་གྱི་དོན་ཉིད་དུ་སྤོ་བར་བྱེད་ཅིང་ཇི་ལྟར་རང་གི་དོན་འདི་ལྟ་བུ་འདི་རིག་པར་བྱའོ། །

[Block 2453]
དཔེར་ན་རང་གི་རྫས་རྐུ་སེམས་ཀྱིས་བླངས་ན་སྦོམ་པོར་འགྱུར་བ་དེ་བཞིན་དུ་འདིར་ཡང་དེ་བཞིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2454]
འདིར་གཞུང་ནི་དགེ་སློང་གཉུག་མར་གནས་པས་ཕྱོགས་བཞིའི་དགེ་འདུན་གྱི་ཡོ་བྱད་རྐུ་སེམས་ཀྱིས་གནས་ནས་གནས་གཞན་དུ་སྤོས་པ་དང་དེ་འགྱོད་པ་སྐྱེས་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ལྟུང་བ་ཕམ་པར་ནི་མི་འགྱུར་རོ། །

[Block 2455]
ཉེས་པ་སྡོམ་པོར༌[^1686]འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2456]
བདག་པོ་ཐ་དད་པ་ཉིད་ལ་སྡེ་པ་ཐ་དད་པ་ལ་སོགས་པ་གནས་དག་ལ་གལ་ཏེ་འདི་ལ་གང་དུ་འཕོ་བ་ཡོད་ན་དེའི་བདག་པོ་རྣམས་ལ་ཁོངས་སུ་བསྡུས་པ་ཉིད་དོ། །

[Block 2457]
ཚང་བ་ལ༌[^1687]ཕམ་པ་སྟེ། གལ་ཏེ་མ་ཡིན་ན་སྦོམ་པོ་སྟེ། གཞན་དོན་ཉིད་ཀྱི་ཕྱིར་ཞེས་བྱ་བ་རྣམ་པར་གནས་སོ། །

[Block 2458]
དེ་བས་ན་བདག་པོ་ཐ་མི་དད་པ་ལ་འདི་རྣམ་པར་ཤེས་པའོ། །

[Block 2459]
འགོད་པ་གཙོ་བོ་ཉིད་རྐུ་བ་ལ་ཐམས་ཅད་ལ་སྦྱོར་བའི་ཕྱིར་འཇུག་པ་ལ་ཕུ་ནུ་འམ་གཞན་ལ་སྐལ་བ་ལ་གཙོ་བོ་ཉིད་དོ། །

[Block 2460]
དེ་བས་ན་ཆོ་ག་གཉིས་པོ་འདི་དག་ལ་ཡང་འགོད་པའི༌[^1688]དོན་ལ་རང་གི་སྐལ་བ་ཉིད་རྣམ་པར་གཞག་པ་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 2461]
ཕྱིར་ལྡོག་གམ་མི་བླང་བར་ངེས་པ་ན་ལྷག་མ་རྣམས་ཀྱིས༌[^1689]བརྐུས་པ་ནི་དེའི་ཡན་ལག་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཚོགས་ནས་རྐུ་བའི་དོན་དུ་སོང་བ་རྣམས་ལ་གང་ཞིག་ལ་ཚོམས་དེ་ལས་ཕྱིར་ལོག་པ་ནི་སོ་སོར་ཐོབ་པ་གཞན་དང་ཕྱིར་ལོག་པའོ། །

[Block 2462]
བདག་འདི་རྣམས་དང་ལྷན་ཅིག་ཏུ་སོང་ཡང་མ་བྱིན་པར་ལེན་པར་མི་བྱེད་ཅེས༌[^1690]བྱ་བ་འདི་ལྟར་མི་ལེན་པའི་ངེས་པའོ། །

[Block 2463]
དེར་རྐུན་པོ་ལྷག་མ་རྣམས་ཀྱིས་བརྐུས་པ་ནི་དེ་ལ་རྐུ་བ་དེའི་ཡན་ལག་ཉིད་མ་ཡིན་ཏེ། རྐུན་པོ་རྣམས་དང་ལྷན་ཅིག་ཏུ་བྱ་བ་གཅིག་པ་ཉིད་མེད་པའི་ཕྱིར་རོ། །

[Block 2464]
འདིར་ཚོགས་ཏེ་འགྲོ་བ་ན་སྦྱོར་བའི་སྦྱོར་བ་ཞེས་བྱ་བའི་ཉེས་བྱས་ཏེ། བླང་བའི་སྔ་རོལ་དུ་ཞེས་བྱ་བ་འདི་ལས་རྟོགས་པར་བྱའོ། །

[Block 2465]
ཆ་བདག་གིར་བྱ་བར་འདོད་པ་ནི་མི་བླང་བའི་བསམ་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་མི་བླང་བའི་བསམ་པ་ཅན་ལ་མ་བྱིན་པར་ནི་མི་བླང་ངོ་། །བགོ་སྐལ་གྱི་ཆ་ནི་བདག་གིར་བྱའོ་ཞེས་བྱ་བ་དེ་ལྟ་བུའི་ངོ་བོ་རྐུན་པོ་རྣམས་དང་འགྲོགས་པའི་དོན་དུ་སོང་བ་ལ་སྐལ་བ་ལེན་པར་འདོད་པ་གང་ཡིན་པ་དེ་ནི་མི་བླང་བའི་བསམ་པ་མ་ཡིན་ནོ། །

[Block 2466]
འདིར་བསྙེན་པ་ལ་སྐལ་བ་དང་ལྡན་པ་ཉིད་ནི་འདིའོ། །

[Block 2467]
དེ་བས་ན་འདི་ལ་བླང་བའི་བསམ་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 2468]
འདི་ལྟ་བུར་གྱུར་པའི་འདོད་པ་ཡོད་པ་ལྷག་མ་རྣམས་ཀྱིས་བརྐུས་པ་ལ་བརྐུས་པའི་ཆ་དང་ལྡན་པ་ཉིད་དོ། །

[Block 2469]
དེར་གཏོགས་པའི་ལས་རྗེས་སུ་སྒྲུབ་པ༌[^1691]ནི་དེའི་མ་ཡིན་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་རྐུན་པོའི་བྱ་བ་དེར་གཏོགས་པའི་ལམ་བསྲུངས་པ༌[^1692]ལ་སོགས་པ་དག་རྗེས་སུ་སྒྲུབ་པ༌[^1693]ནི་རྐུ་བ་དེའི་རྗེས་སུ་སྒྲུབ་པ༌[^1694]མ་ཡིན་པ་མ་ཡིན་ནོ། །

[Block 2470]
སྐལ་བ་ཉིད་ཀྱི་ཕྱིར་ཡང་འདི་ལ་ལྟུང་བ་གྲུབ་པའོ། །

[Block 2471]
བྱ་བའི་རང་གི་ངོ་བོ་ཡང་བསལ་བར་འགྱུར་བ་ཞེས་བྱ་བ་འདིའི་ཚིག་གོ། །

[Block 2472]
ལྷན་ཅིག་གནས་པ་ཉིད་དང་ཉེ་གནས་ཉིད་ཀྱང་བརྐུས་པར་མི་འགྱུར་བའི་རྒྱུ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་རྣམ་པ་འདི་དག་གིས་རང་ཉིད་མ་ཡིན་པ་གཞན་དག་གིས་བླངས་པ་དག་དང་ལྷན་ཅིག་གནས་པ་ཉིད་དང་ཉེ་གནས་ཉིད་དག་རང་གིས་བརྐུས་པ་ཡང་བརྐུས་པའི་ཉེས་པར་མི་འགྱུར་བའི་རྒྱུ་མ་ཡིན་ཏེ། འདིར་བརྐུས་པ་ཁོ་ནར་འགྱུར་རོ། །

[Block 2473]
བླངས་པ་ཉིད་ནི་འདི་དག་གིས་དབང་དུ་བྱས་པ་ཉིད་ཀྱི་ཕྱིར་རོ་ཞེས་བྱ་བ་རྟོགས་པར་བྱའོ། །

[Block 2474]
ཡོངས་སུ་བསྐོར་བ་ལ༌[^1695]མཚམས་ཉིད་གཙོ་བོའོ། །

[Block 2475]
མཚམས་གནས་པ་སྤོས་པ་ཡང་འདིས་མ་བསྡུས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་མཚམས་དང་འབྲེལ་པའོ། །

[Block 2476]
འདིར་ཡོངས་སུ་བསྐོར་བ་ཞེས་སྨོས་པ་མཚམས་གཙོ་བོར་རིག་པར་བྱའོ། །

[Block 2477]
ཡོངས་སུ་བསྐོར་བ་ཉིད་ལ་ནི་མི་བྱའོ། །

[Block 2478]
དེ་བས་ན་མི་མཐུན་པ་དང་ལྷན་ཅིག་གནས་པས་ཕུར་པས་བརྐོ་བ༌[^1696]ལ་སོགས་པ་གང་ཡིན་པ་མཚམས་དེའི་སྤོས་པ་ཡང་འདིས་མ་བསྡུས་པ་མ་ཡིན་ནོ། །

[Block 2479]
འདི་ཡང་འདིར་རྐུ་བ་ཉིད་ཀྱིས་བརྗོད་པ་རྟོགས་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2480]
མངོན་སུམ་དུ་བླངས་པ་ཡང་མི་སྣང་བ་ཉིད་ན་བརྐུས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་དབང་པོ་དང་ཉེ་བ་ནི་མངོན་སུམ་མོ། །

[Block 2481]
དེའི་དངོས་པོ་འབུལ་བ་བླངས་པ་ནི་མངོན་སུམ་གྱིས་བླངས་པའོ། །

[Block 2482]
དེར་ཡང་མི་སྣང་བ་ཉིད་ན་བརྐུས་པ་ཡིན་གྱི་ཕྱི་བཞིན་འབྲང་བ་དང་ནང་བྱན་གཉིས་མི་སྣང་བར་གྱུར་པ་འབའ་ཞིག་ཏུ་མ་ཟད་དོ། །

[Block 2483]
དེ་བས་ན་བདག་པོ་གཟུང་བར་བྱེད་པ་ལ་ཡང་ཇི་སྲིད་དུ་མཐོང་བའི་བར་ལ་བརྐུས་པར་མི་འགྱུར་ཏེ། དེ་ལྟར་ཡང་རྫས་འདི་དང་རྣམ་པར་བྲལ་བར་མི་འགྱུར་ཞེས་བྱ་བར་སྦྱོར་བ་དང་བྲལ་བ་ཉིད་ནི་ཉེས་བྱས་སོ། །

[Block 2484]
དེ་བས་ན་ནན་གྱིས་རྐུ་བ་ཡང་ཆོ་ག་འདི་ཡོད་པར་རིག་པར་བྱའོ། །

[Block 2485]
འདིར་གཞུང་ནི་དགེ་སློང་གིས་བེའུ་རས་འཚོང་བ་བག་མེད་པར་གྱུར་པ་ལས་བེའུ་རས་བརྐུས་ཏེ། དེས་དེ་ཁྱེར་ཏེ་འགྲོ་བ་ན་བེའུ་རས་འཚོང་བ་དེས་མཐོང་ནས་དེས་དགེ་སློང་དེ་ལ་སྨྲས་པ། བེའུ་རས་མ་འཕྲོག་ཅིག །དགེ་སློང་གིས་སྨྲས་པ། བསྟན་ལ་ཁྱེར་ཏེ་འོང་བར་བྱའོ། །

[Block 2486]
དེས་འགྱོད་པ་སྐྱེས་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ཕམ་པའི་ལྟུང་བར་ནི་མི་འགྱུར་ཏེ། ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2487]
འདིར་མི་སྣང་བ་ཉིད་ལས་གཞན་དུ་ལྟུང་བའི་ཚིག་ལ་རྒྱུ་མཐོང་བ་ཡིན་ཏེ། སྦྱོར་བ་ཉིད་ཀྱི་ཕྱིར་འདིར་ཉེས་པ་སྦོམ་པོར་བརྗོད་པ་ཞེས་བྱ་བ་འདིར་ནི་ཤེས་པ་ཡིན་ནོ། །

[Block 2488]
མི་མཐུས༌[^1697]རྐུ་བ་ནི་དབང་དུ་བྱས་པ་ཉིད་ནའོ་ཞེས་བྱ་བ་ནི་ནན་གྱིས་ལེན་པ་ལ་མི་ལ་བག་ཕེབས་ཤིང་དབང་དུ་བྱས་པ་ཉིད་ན༌[^1698]བརྐུས་པ་ཡིན་ནོ། །

[Block 2489]
འདིར་མི་ཞེས་སྨོས་པའི་སྒྲ་འདི་ནི་རིགས་ལ་བསྙགས་པ་དེས་ན་སྐྱེས་པ་འབའ་ཞིག་ཏུ་མ་ཟད་དེ་བུད་མེད་ལ་སོགས་པ་ལ་ཡང་ཡོད་པར་རིག་པར་བྱའོ། །

[Block 2490]
གཞན་དང་ལྷན་ཅིག་ཏུ་གཙུག་ལག་ཁང་ལ་སོགས་པ་ལས་རྐུ་བ་ནས་དབང་དུ་བྱས་པ་ལས་གྲོལ་བ༌[^1699]གང་ཡིན་པ་དེའི་དོན་དུ་ཡང་འདི་དེ་ལྟར་བླང་བར་བྱས་པ་ལ་གྲོལ་བ་ན་རྐུ་བ་སྐྱེས་པ༌[^1700]ཞེས་བྱ་བའི་དོན་ཏོ། །
--- END BLOCKS ---
