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
[^1757]བཏང་སྙོམས་དང་མཚུངས་པར་ལྡན་པའི་ཕྱིར་རོ། །

[Block 2452]
བདེ་བ་དང་སྡུག་བསྔལ་དག་ནི་རྣམ་པར་རྟོག་པ་དང་མཐུན་པའི་ཕྱིར་དེའི་གཉེན་པོ་ནི་དེ་དག་དང་མཚུངས་པར་མི་ལྡན་ནོ། །

[Block 2453]
བདེ་བ་དང་ཡིད་བདེ་བ་དག་ཀྱང་གཏོད་པ་ལ་བར་ཆད་བྱེད་པའི་ཕྱིར་ལ། དེ་ཡང་གཏད་པས་བསྒྲུབ་པར་བྱ་བ་ཡིན་པའི་ཕྱིར་རོ་ཞེས་གྲག་གོ། །

[Block 2454]
གང་དག་བསམ་གཏན་དངོས་གཞི་དག་ན་ཡང་སྙོམས་པར་ཞུགས་པ་ལ་བཏང་སྙོམས་ཀྱི་དབང་པོ་ཡོད་པར་འདོད་པ་དེ་དག་གི་ལྟར་ན་ས་བརྒྱད་པ་ཡིན་ནོ། །

[Block 2455]
ཡན་ཆད་ནི་དབུགས་རྔུབ་པ་དང་དབུགས་འབྱུང་བའི་ས་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2456]
དེའི་དམིགས་པ་ནི༌[^1758]རླུང་ཡིན་ནོ། །

[Block 2457]
འདོད་པའི་ཁམས་ཀྱི་རྟེན་ཅན་ཡིན་ནོ། །

[Block 2458]
[^1759]ལྷ་དང་མི་དག་གི་ནང་ནས་སྐྱེད་དོ། །

[Block 2459]
སྦྱོར་བ་ལས་བྱུང་བ་དང་། འདོད་ཆགས་དང་བྲལ་བས་ཐོབ་པ་ཡིན་ནོ། །

[Block 2460]
འདི་ནི་དེ་ཁོ་ན་ཡིད་ལ་བྱེད་པ་ཡིན་ནོ། །

[Block 2461]
ཆོས་འདི་པ་རྣམས་ཁོ་ནའི་ཡིན་གྱི། ཕྱི་པའི་མ་ཡིན་ནོ། །

[Block 2462]
ལུང་མེད་པའི་ཕྱིར་དང་། བདག་ཉིད་ཀྱིས་ཆོས་ཟབ་མོ་མངོན་པར་མི་རྟོགས་པའི་ཕྱིར་རོ། །

[Block 2463 [HEADING]]
###### **བགྲང་བ་ལ་སོགས་པ་རྣམ་པ་དྲུག།** ^3-1-3-4-2-1-0

[Block 2464]
དེ་ཡང་བགྲང་བ་ལ་སོགས་པ་རྣམ་པ་དྲུག །དེ་ནི་བགྲང་བ་དང་རྗེས་སུ་འགྲོ་བ་དང་། འཇོག་པ་དང་། ཉེ་བར་རྟོགས་པ༌[^1760]དང་། བསྒྱུར་བ་དང་། ཡོངས་སུ་དག་པ་སྟེ། རྒྱུ་དྲུག་དང་ལྡན་ན་ཡོངས་སུ་རྫོགས་པ་ཡིན་ནོ། །

[Block 2465 [HEADING]]
###### **བགྲང་བ།** ^3-1-3-4-2-1-1-0

[Block 2466]
དེ་ལ་བགྲང་བ་ཞེས་བྱ་བའི༌[^1761]དབུགས་རྔུབ་པ་དང་དབུགས་འབྱུང་བ་དག་ལ་སེམས་གཏད་ནས་མངོན་པར་འདུ་བྱ་བ་མེད་པར་ལུས་དང་སེམས་རྣལ་དུ་གཞག་སྟེ་དྲན་པ་ཙམ་གྱིས་གཅིག་དང་གཉིས་ནས་བཅུའི་བར་དུ་བགྲང་བར་བྱེད་པའོ། །

[Block 2467]
སེམས་མངོན་པར་སྡུད་པ་དང་རྣམ་པར་གཡེང་བར་དོགས་པས་ཧ་ཅང་མང་བ་དང་ཉུང་ངུར་ནི་མ་ཡིན་ནོ། །

[Block 2468]
དེ་ལ་སྐྱོན་ནི་གསུམ་ཡོད་དེ། གལ་ཏེ་གཉིས་ལ་གཅིག་ཏུ་འཛིན་ན་མ་ཚང་བར་བགྲངས་པའི༌[^1762]སྐྱོན་ནོ། །

[Block 2469]
གལ་ཏེ་གཅིག་ལ་གཉིས་སུ་འཛིན་ན་ལྷག་པར་བགྲང་བའི༌[^1763]སྐྱོན་ནོ། །

[Block 2470]
གལ་ཏེ་དབུགས་རྔུབ་པ་ལ་དབུགས་འབྱིན་པར་འཛིན་ཏམ། དབུགས་འབྱིན་པ་ལ་དབུགས་རྔུབ་པར་འཛིན་ན་འཆོལ་བར་བགྲང་བའི༌[^1764]སྐྱོན་ནོ། །

[Block 2471]
དེ་ལས་གཞན་པ་ནི་ཡང་དག་པའི་བགྲང་བ་ཡིན་ནོ། །

[Block 2472]
བར་སྐབས་སུ་སེམས་རྣམ་པར་གཡེང་ན་ཡང་མགོ་ནས་ཇི་སྲིད་དུ་ཏིང་ངེ་འཛིན་མ་ཐོབ་ཀྱི་བར་དུ་བགྲང་བར་བྱའོ། །

[Block 2473 [HEADING]]
###### **རྗེས་སུ་འགྲོ་བ།** ^3-1-3-4-2-1-2-0

[Block 2474]
རྗེས་སུ་འགྲོ་བ་ཞེས་བྱ་བ་ནི་འདི་དག་ཐག་ནི་ཇི་སྲིད་གཅིག་ཏུ་འབྱུང་ཞིང་འཇུག །ཅི་འདི་དག་ལུས་ཐམས་ཅད་ལ་ཁྱབ་པ་དག་ཅིག་གམ། ཕྱོགས་འགའ་ཞིག་ན་རྒྱུ་བ་དག་ཡིན་ཞེས་མངོན་པར་འདུ་བྱ་བ་མེད་པར་དབུགས་རྔུབ་པ་དང་དབུགས་འབྱུང་བའི་འགྲོས་ཀྱིས༌[^1765]རྗེས་སུ་འགྲོ་བ་སྟེ། དེ་འཇུག་པ་ན་ལྐོག་མ་དང་། སྙིང་ག་དང་། ལྟེ་བ་དང་། རྐེད་པ་དང་། བརླ་དང་། བྱིན་པར་འཇུག་པའི་རིམ་གྱིས་རྐང་པ་གཉིས་ཀྱི་བར་དུ་རྗེས་སུ་འགྲོ་ལ། འབྱུང་བ་ན་མཐོ་གང་དང་འདོམ་གང་གི་བར་དུ་འབྱུང་ངོ་། །གཞན་དག་ན་རེ་རླུང་གི་དཀྱིལ་འཁོར་དང་རྣམ་པར་འཐོར་བྱེད་ཀྱི་རླུང་གི་བར་དུའོ་ཞེས་ཟེར་ཏེ། འདི་ནི༌[^1766]ཁོ་ན་ཡིད་ལ་བྱེད་པ་ཡིན་པའི་ཕྱིར་རིགས་པ་མ་ཡིན་ནོ། །

[Block 2475 [HEADING]]
###### **འཇོག་པ།** ^3-1-3-4-2-1-3-0

[Block 2476]
འཇོག་པ་ཞེས་བྱ་བ་ནི་ནོར་བུའི་ཐག་པ་བཞིན་དུ་སྣའི་རྩེ་མོ་ནས་རྐང་པའི་མཐེ་བོང་གི་བར་དུ་གནས་པར་ལྟ་ཞིང་། ཅི་འདི་དག་ཕན་འདོགས་པར་བྱེད་པ་ཞིག་གམ། གནོད་པར་བྱེད་པ་ཞིག་གམ། གྲང་ངམ། དྲོ་བ་དག་ཅིག་ཅེས་རྟོག་པའོ། །

[Block 2477 [HEADING]]
###### **ཉེ་བར་རྟོག་པ།** ^3-1-3-4-2-1-4-0

[Block 2478]
ཉེ་བར་རྟོག་པ་ནི་འདི་དག་ནི་རླུང་འབའ་ཞིག་མ་ཡིན་གྱི་འབྱུང་བ་ཆེན་པོ་བཞི་དག་དང་འབྱུང་བ་དག་ལས་མངོན་པར་གྲུབ་པ༌[^1767]རྒྱུར་བྱས་པའི་གཟུགས་དང་། དེ་དག་ལ་བརྟེན་པ་སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་ཀྱང་ཡོད་དོ་ཞེས་ཕུང་པོ་ལྔ་ལ༌[^1768]ཉེ་བར་རྟོག་པར་བྱེད་པའོ། །

[Block 2479 [HEADING]]
###### **བསྒྱུར་བ།** ^3-1-3-4-2-1-5-0

[Block 2480]
བསྒྱུར་བ་ཞེས་བྱ་བ་ནི་རླུང་ལ་དམིགས་པའི་བློ་བསྒྱུར་ཏེ་ཆོས་ཀྱི་མཆོག་གི་བར་དུ་གོང་ནས་གོང་དུ་དགེ་བའི་རྩ་བ་རྣམས་ལ་ཡང་དག་པར་སྦྱོར་བའོ། །

[Block 2481 [HEADING]]
###### **ཡོངས་སུ་དག་པ།** ^3-1-3-4-2-1-6-0

[Block 2482]
ཡོངས་སུ་དག་པ་ནི་མཐོང་བའི་ལམ་ལ་སོགས་པ་ལ་འཇུག་པའོ། །

[Block 2483]
གཞན་དག་ན་རེ་བསྒྱུར་བ་ནི་དྲན་པ་ཉེ་བར་གཞག་པ་ནས་རྡོ་རྗེ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་གྱི་བར་ཡིན་ལ། རྣམ་པར་དག་པ་ནི་ཟད་པ་ཤེས་པ་ལ་སོགས་པ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 2484]
དབུགས་རྔུབ་དབུགས་འབྱུང་དྲན་པ་ནི།[^1769] །

[Block 2485 [VERSE]]
བགྲང་དང་རྗེས་འགྲོ་འཇོག་པ་དང་། །
རྟོག་པ་དང་ནི་བསྒྱུར་བ་དང་། །
ཡང༌[^1770]དག་རྣམ་པ་དྲུག་ཏུ་འདོད། །

[Block 2486]
ཅེས་བྱ་བ་ནི་བསྡུ་བའི་ཚིགས་སུ་བཅད་པ་ཡིན་ནོ། །

[Block 2487]
དེ་ལ། དབུགས་རྔུབ་དབུགས་འབྱུང་གང་ལས་ལུས། །འདི་གཉིས་ནི་ལུས་ཀྱི་ཕྱོགས་གཅིག་ཡིན་པའི་ཕྱིར་ལུས་ས་པ༌[^1771]གང་ཡིན་པ་དེའི་ས་པ་དག་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 2488]
དབུགས་རྔུབ་པ་དང་དབུགས་འབྱུང་བ་ནི་གཟུགས་མེད་པ་དང་། ནུར་ནུར་པོ་ལ་སོགས་པར་གྱུར་པ་རྣམས་དང་། སེམས་མེད་པ་དང་། བསམ་གཏན་བཞི་པ་ལ་སྙོམས་པར་ཞུགས་པ་རྣམས་ལ་མེད་པའི་ཕྱིར་ལུས་དང་སེམས་ཁྱད་པར་ཅན་ལ་བརྟེན་ནས་འཇུག་པ་ཡིན་ཏེ། གལ་ཏེ་ལུས་ཀྱང་སྦུབས་ཡོད་པ་ཡིན་ལ་དབུགས་རྔུབ་པ་དང་། དབུགས་འབྱུང་པའི་ས་པའི་སེམས་ཀྱང་མངོན་སུམ་དུ་གྱུར༌[^1772]ན་དེ་ལྟ་ན་འཇུག་གོ། །

[Block 2489]
སྐྱེ་བ་དང་། བསམ་གཏན་བཞི་པ་ལས་ལྡང་བ་ལ༌[^1773]ནི་འཇུག་ལ། འཆི་བ་དང་། བསམ་གཏན་བཞི་པ་ལ་སྙོམས་པར་འཇུག་པ་ལ་ནི་འབྱུང་ངོ་། །དབུགས་རྔུབ་པ་དང་དབུགས༌[^1774]འབྱུང་བ་འདི་གཉིས་ནི། སེམས་ཅན་ཞེས་བྱ། སེམས་ཅན་དུ་མི་བགྲང་བ་དག་ནི་མ་ཡིན་ནོ། །

[Block 2490]
མ་ཟིན་པའོ། །
--- END BLOCKS ---
