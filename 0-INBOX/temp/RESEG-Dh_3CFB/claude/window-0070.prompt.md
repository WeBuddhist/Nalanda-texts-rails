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
བྱམས་པ་དང་གཙང་སྦྲ་དང་ཆོས་ལ་གཞོལ་བ་དག་གི་རྒྱུ་མཚན་དེ་ཉིད་གྲུབ་པ་འགའ་ཞིག་ཀྱང་མི་བསྒྲུབ་པའི༌[^1681]ཕྱིར་བཟློག་པ་དག་གིས་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 2452]
ལས་ཀྱི་ངོ་བོ་གཅིག་ལས་ཀྱང་དེ་དང་འགལ་བའི་ཆོས་དང་ཆོས་མ་ཡིན་པ་མི་རིགས་སོ། །

[Block 2453]
ད་ནི་ཇི་ལྟར་ན་ཆོས་མ་ཡིན་པའི་བདག་ཉིད་ཅན་གྱི་བརྟུལ་ཞུགས་ལ་སོགས་པ་ལས་ཆོས་ཀྱི་འབྲས་བུ་འདོད་པ་ཐོབ་པར་འགྱུར། འབྲས་བུ་འདོད་པ་དེ་ནི་བརྟུལ་ཞུགས་ལ་སོགས་པ་དེའི་རྣམ་པར་སྨིན་པ་ནི་མ་ཡིན་གྱི། འོན་ཀྱང་སྔོན་གྱི་ལས་ཀྱིས་ཡིན་ཏེ། བྲམ་ཟེ་གསོད་པའི་ལུང་ནན་ཏན་དུ་བྱས་པ་ལས་ཡུལ་རྙེད་པ་བཞིན་ནོ། །

[Block 2454]
ཆོས་མ་ཡིན་པའི་བདག་ཉིད་ཅན་བརྟུལ་ཞུགས་དེ་མ་འོངས་པའི་འབྲས་བུ་ནི་མི་འདོད་པ་ཡིན་ནོ།[^1682] །འབྲས་བུ་འདོད་པ་ཅན་གྱི་ལས་དེའི༌[^1683]སྔགས་ལ་སོགས་པའི་སྦྱོར་བ་དེ་རྣམ་པ་འགའ་ཞིག་གིས་ཕན་འདོགས་པར་བྱེད་པའི་ཕྱིར་སྨིན་པར་བྱེད་པ་ཡིན་ཏེ། ཕན་འདོགས་པར་བྱེད་པའི་ནུས་པ་ནི་སྣ་ཚོགས་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2455]
སྐྱེས༌[^1684]བུའི་ཁྱད་པར་ལ་བརྟེན་པ་རྣམ་པར་སྨིན་པའི༌[^1685]ཆོས་ཅན་གྱི་ཆོས་དེ་དང་དེས་བྱས་པ་ནི། དེ་ལྟར་མགུ་བར་བྱས་པས་འབྲས་བུ་འབྱིན་པ་ཡིན་ནོ། །

[Block 2456]
དེའི་འབྲས་བུ་ཅན་གྱི་ལས་དེའི་སྦྱོར་བས་ཕན་འདོགས་པར་བྱེད་པས་རྣམ་པར་སྨིན་པའི་ཆོས་ཅན་ནི་བྱས་པ་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2457]
གལ་ཏེ་སྐྱེས་བུའི་ཁྱད་པར་མེད་པར་ཡང་དེས་ཕན་བཏགས་པ་ལས་འབྲས་བུ་ཡིན་ནོ་ཞེ་ན། མ་ཡིན་ཏེ། སྐྱེས་བུའི་རྣམ་པ་དང་རང་བཞིན་དང་སྤྱོད་པའི་མོས་པ་དོན་མེད་པར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2458]
དེ་ཡང་ཕན་འདོགས་པར་བྱེད་པ་ཉིད་ཡིན་ན་སྐྱེས་བུའི་ཁྱད་པར་ཡོན་ཏན་ཐུན་མོང་མ་ཡིན་པ་ཅན་གྲུབ་སྟེ། དེ་དག་ལ་མོས་པ་ཁོ་ན་དུག་གི་ལས་ལ་སོགས་པ་བྱེད་པའི་ཕྱིར་རོ། །

[Block 2459]
དེ་བས་ན་སྔགས་སྐྱེས་བུས་བྱས་པ་ཡིན་དུ་ཟིན་ཀྱང་དེའི་ཉེ་བར་སྦྱོར་བ་ལ་ལྟོས་པ་མེད་པ་རང་བཞིན་གྱིས་འབྲས་བུ་འབྱིན་པ་མ་ཡིན་ནོ། །

[Block 2460 [VERSE]]
གང་ཡང་རྒྱུད་རིག་འགའ་ཞིག་གིས། །
གསང་སྔགས་ཅུང་ཟད་བྱེད་འགྱུར་བ། །
དེ་དག་གིས༌[^1686]དེ་གཙོ་བོའི་མཐུ། །
དེས་བཤད་རིག་པ་འཇུག་ཕྱིར་རོ། །

[Block 2461]
ལམ་པོ་ཆེའི་སྐྱེས་བུ་འགའ་ཞིག་རྒྱུད་ཤེས་པ་བདག་ཉིད་ཀྱི་སྔགས་བྱས་པ་དག་གིས་ལས་འགའ་ཞིག་བྱེད་པར་འགྱུར་རོ། །

[Block 2462]
དེ་བཞིན་དུ་གཞན་དག་ཀྱང་ཕུལ་དུ་བྱུང་བ་མ་ཡིན་པ་དང་སྔགས་ཀྱི་བྱེད་པ་པོར་ཡང་འགྱུར་རོ་ཞེ་ན། མ་ཡིན་ཏེ། དེ་དག་གི་མཐུ་དང་ལྡན་པ་ཉིད་ཀྱིས་བྱིན་གྱིས་བརླབས་པའི་ཕྱིར་རོ། །

[Block 2463]
དེས་བྱས་པའི་དམ་ཚིག་རྗེས་སུ་སྐྱོང་བ་དང་། དེའི་མན་ངག་གི་དམ་ཚིག་ནན་ཏན་དུ་བྱེད་པ་དེ་དག་གིས་ནུས༌[^1687]ཏེ། དེའི་དམ་ཚིག་དང་མན་ངག་ལ་ལྟོས་པ་མེད་པ་དག་ལ་ནུས་པ༌[^1688]མེད་པའི་ཕྱིར་རོ། །

[Block 2464]
དེ་ལ་ཡང་དེའི་རྣམ་པ་བསམ་གཏན་བྱེད་པ་ལ་སོགས་པ་ཉིད་དུ་རབ་ཏུ་སྦྱོར་བའི་ཕྱིར་རོ། །

[Block 2465]
དེ་བས་ན་དེས་བྱིན་གྱིས་བརླབས་པ་དེ་ཉིད་དེ་འདྲ་བར་ཤེས་པར་བྱའོ། །

[Block 2466]
གཞན་ཡང་དེ་འདྲ་བའི་མཐུ་དང་ལྡན་པ་དེ་ཉིད་ཀྱང་གཞན་དང་ཐུན་མོང་མ་ཡིན་པའི་ནུས་པ་ཉིད་ཡིན་པའི་ཕྱིར། སྐྱེས་བུའི་ཁྱད་པར་ཉིད་བསྒྲུབས་པ༌[^1689]ཡིན་ནོ། །

[Block 2467 [VERSE]]
འབྲས་བུ་འདོད་པས་སྔགས་རྣམས་ནི། །
བྱས་དང་སྐྱེས་བུས་བྱས་བརྗོད་བྱ། །

[Block 2468]
མ་བྱས་པ་དག་གི་སྦྱོར་བ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2469]
སྦྱོར་བ་མེད་པ་དག་ལས་འབྲས་བུ་མེད་པ་དེ་ལྟར་ན། སྐྱེས་བུའི་བྱིན་བརླབས་མེད་པར་འབྲས་བུ་མེད་པ་ཅན་དག་གི་འབྲས་བུ་མཐོང་བའི་ཕྱིར། སྦྱོར་བ་ལས་འབྲས་བུ་འདོད་པ་ཉིད་ཀྱིས་སྔགས་རྣམས་བྱས་པ་དང་། སྐྱེས་བུས་བྱས་པ་བརྗོད་པར་བྱ་སྟེ། བརྡར་བྱས་པ་ཅན་གྱི་སྙན་དངགས་བཞིན་ནོ། །

[Block 2470 [VERSE]]
སྐྱེས་བུས༌[^1690]ནུས་མེད་སྒྲུབ་བྱེད་ནི། །
འདི་ཉིད་ཀྱིས་ནི་བསལ་བ་ཡིན། །

[Block 2471]
སྔགས་རྣམས་ནི་སྐྱེས་བུས་བྱས་པ་དང་དེས་བྱིན་གྱིས་བརླབས་པ་ལས་འབྲས་བུ་འབྱིན་པར་བསྟན་ཏོ། །

[Block 2472]
དེ་བས་ན་དེ་ཕུལ་དུ་བྱུང་བ་འགའ་ཞིག་དང་ལྡན་པའི་ཕྱིར། དེ་སྤོང་བར་བྱེད་པའི་སྒྲུབ་པར་བྱེད་པ་དག་ཀྱང་བསལ་བ་ཡིན་ནོ། །

[Block 2473 [VERSE]]
བློ་དབང་སྨྲ་དང་སྐྱེས་བུ་ཉིད། །
ལ་སོགས་སྒྲུབ་བྱེད་གང་བརྗོད་པ། །
ཚད་ལྟར་སྣང་ཡིན་ལྷག་མིན༌[^1691]པས། །
ཇི་བཞིན་དོན་རྟོགས་ཡོད་མ་ཡིན། །

[Block 2474]
བློ་དང་དབང་པོ་དང་སྨྲ་བ་དང་སྐྱེས་བུ་ཉིད་ཡིན་པའི་ཕྱིར་ཞེས་བྱ་བ་ལ་སོགས་པ་སྐྱེས་བུའི་ཕུལ་དུ་བྱུང་བ་སྤོང་བ་སྒྲུབ་པར་བྱེད་པ་གང་ཡིན་པ་དེ་ཡང་གོ་བར་བྱེད་པ་ཉིད་མ་ཡིན༌[^1692]ཏེ། སྤོང་བ་དང་སྤྱི་སྒྲུབ་པར་བྱེད་པ༌[^1693]དག་ནི་མི་སྲིད་པའི་ཕྱིར་རོ། །

[Block 2475]
དབང་པོ་ལས་འདས་པ་དག་ལ༌[^1694]དེ་མ་མཐོང་བའི་སྤོང་བ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2476]
ཡོད་དུ་ཟིན་ཀྱང་དེ་དག་མི་ཤེས་པའི་ཕྱིར་རོ། །

[Block 2477]
དེ་ཉིད་ཀྱི་ཕྱིར་འགལ་བ་མི་འགྲུབ་པའི་ཕྱིར། འགལ་བ༌[^1695]མེད་པ་དང་ལྷན་ཅིག་ཡོད་པ་འགལ་བ༌[^1696]མེད་པའི་ཕྱིར་རོ་ཞེས་བཤད་ཟིན་ཏོ། །

[Block 2478]
ཅིག་ཤོས་ཀྱི་སྤྱི་ཡང་གྲུབ་པ་མ་ཡིན་ཏེ། ཁྱད་པར་མེད་པ༌[^1697]ཤེས་པར་མི་ནུས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2479]
དེ་འདྲ་བ་དག་ལ་མི་དམིགས་པ་ནི་གཏན་ཚིགས་ཉིད་ཡིན་པ་སྤངས་པའི་ཕྱིར་རོ། །

[Block 2480]
སྐྱེས་བུ་ལ་སོགས་པའི་སྤྱི་དག་ལ་ཡང་ཁྱད་པར་འགའ་ཞིག་ཀྱང་མཐོང་བའི་ཕྱིར་རོ། །

[Block 2481]
ཁྱད་པར་ཡོད་པ་ཅན་ལ་ཡང་སྤྱི་མ་གྲུབ་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ཡང་བཤད་ཟིན་ཏོ། །

[Block 2482]
དེ་བས་ན་རྗེས་སུ་དཔག་པ་དེ་ནི་མི་མཐུན་པའི་ཕྱོགས་ལ་འཇུག་པ་མ་མཐོང་དུ་ཟིན་ཀྱང་། ལྡོག་པ་ལ་ཐེ་ཚོམ་ཟ་བའི་ཕྱིར་ལྷག་མ་དང་ལྡན་པ་ནུས་པ་མེད་པ་ཡིན་ནོ།། །།

[Block 2483]
བམ་པོ་བཅུ་གཅིག་པ། གཞན་ཡང་དེ་སྐད་དུ་བརྗོད་པའི་རྒྱལ་དཔོག་པ་དག་གི་རང་གི་ཚིག་དང་འགལ་བར་བྱེད་དོ། །

[Block 2484]
དེ་ལྟར་ན།

[Block 2485 [VERSE]]
སྒྲ་ནི་ཁོ་བོས་འདི་དོན་དང་། །
འདི་དོན་མིན་ཞེས་བརྗོད་མི་བྱེད། །
སྐྱེས་བུས་དོན་འདི་བརྟགས་པ་སྟེ། །
དེ་ཡང་འདོད་ཆགས་ལ་སོགས་ལྡན། །

[Block 2486 [VERSE]]
དེ་གཅིག་དེ་ཉིད་རིགས་གཞན་མིན། །
ཞེས་བྱའི་ཁྱད་པར་གང་གིས་བྱས། །
དེ་བཞིན་སྐྱེས་ཡིན་རྣམ༌[^1698]འགས་ཀྱང་། །
ཁྱོད་ཅི་ཤེས་ཅན་འགའ་མི་འདོད། །

[Block 2487]
རིག་བྱེད་པའི་སྒྲ་དེ་དག་བྲམ་ཟེ་ཁྱོད་ཚུར་ཤོག །ཁོ་བོའི་དོན་འདི་ཟུང་ཤིག །གཞན་ནི་མ་ཡིན་ནོ་ཞེས་དེ་སྐད་དུ་བརྗོད་པར༌[^1699]མི་བྱེད་དོ། །

[Block 2488]
མངོན་པར་གསལ་བ་མ་ཡིན་པའི་དོན་གྱི་ཁྱད་པར་དང་འདྲེ་བ་ཅན་འགའ་ཞིག་གིས་མཉན་པ་ཉིད་སྐྱེད་པར་བྱེད་དོ། །

[Block 2489]
དེ་ལ་སྐྱེས་བུ་གཅིག་གིས་དོན་ཅུང་ཟད་གཅིག་དང་གཞན་གྱིས་གཞན་བརྟགས་པ་ཡིན་གྱི། སྒྲ་རྣམས་ཀྱི་རང་བཞིན་སོ་སོར་ངེས་པ་ཅུང་ཞིག་ཀྱང་ཡོད་པ་མ་ཡིན་ན། གང་གིས་དོན་གཅིག་གི་རྗེས་སུ་བྱེད་ཅིང་གཞན་མ་ཡིན་ཏེ། འོན་ཀྱང་བརྡའི་དབང་གིས་དེ་དང་དེ་བཟུང་བ་ན་མཐོང་བར་འགྱུར་རོ། །

[Block 2490]
ལྐོག་ཏུ་གྱུར་བ་གོམས་པའི་ཕྱིར་ཉེས་པས་བསླད༌[^1700]ཅིང་མི་མཁས་བ་འགའ་ཞིག་དོན་ངེས་པ་རིགས་པ་མེད་པ་ཅན་དེ་དག་དེ༌[^1701]ཁོ་ན་ཉིད་དུ་འཆད་པར་བྱེད་པ་ཡིན་ལ། གཞན་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བར་རིགས་པ་མ་ཡིན་ནོ། །
--- END BLOCKS ---
