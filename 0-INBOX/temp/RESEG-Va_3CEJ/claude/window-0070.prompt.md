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
སྣོད་དང་བཅས་པར་བཟུང་ན་ནི་རླུང་གི་དཀྱིལ་འཁོར་གྱི་བར་ཡིན་ནོ། །

[Block 2452]
འདོད་པའི་ཁམས་འདིའི། གོང་མའི་གནས་དག་བཅུ་བདུན་ནི། །གཟུགས་ཁམས་ཡིན། ཇི་ལྟ་ཞེ་ན། དེར་སོ་སོའི། བསམ་གཏན་ས་ནི་གསུམ་པ་ཡིན། །ཞེས་བྱ་བ་སྨོས་ཏེ། བསམ་གཏན་དང་པོ་དང་།

[Block 2453]
གཉིས་པ་དང་།

[Block 2454]
གསུམ་པ་དག་ན༌[^1287]རེ་རེ་ཞིང་ས་གསུམ་པ་དག་ཡིན་ནོ། །

[Block 2455]
བཞི་པ་ས་ནི་བརྒྱད་པ་ཡིན། །དེ་ལ་བསམ་གཏན་དང་པོ་ནི་ཚངས་རིས་རྣམས་དང་། ཚངས་པའི་མདུན་ན་འདོན་རྣམས་དང་། ཚངས་ཆེན་རྣམས་སོ། །

[Block 2456]
གཉིས་པ་ནི་འོད་ཆུང་རྣམས་དང་། ཚད་མེད་འོད་རྣམས་དང་། འོད་གསལ་རྣམས་སོ། །

[Block 2457]
གསུམ་པ་ནི་དགེ་ཆུང་རྣམས་དང་། ཚད་མེད་དགེ་རྣམས་དང་། དགེ་རྒྱས་རྣམས་སོ། །

[Block 2458]
བཞི་པ་ནི་སྤྲིན་མེད་རྣམས་དང་། བསོད་ནམས་སྐྱེས་རྣམས་དང་། འབྲས་བུ་ཆེ་བ་རྣམས་དང་། མི་ཆེ་བ་རྣམས་དང་། མི་གདུང་བ་རྣམས་དང་། གྱ་ནོམ་སྣང་བ༌[^1288]རྣམས་དང་། ཤིན་ཏུ་མཐོང་བ་རྣམས་དང་། འོག་མིན་རྣམས་ཏེ། དེ་ལྟར་ན་གནས་བཅུ་བདུན་པོ་འདི་དག་དེ་ན་གནས་པའི་སེམས་ཅན་རྣམས་དང་བཅས་པ་ནི་གཟུགས་ཀྱི་ཁམས་ཡིན་ནོ། །

[Block 2459]
ཁ་ཆེ་བ་རྣམས་ན་རེ་བཅུ་དྲུག་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 2460]
ཚངས་པའི་མདུན་ན་འདོན་ཁོ་ན་དག་ན༌[^1289]ཚངས་པ་ཆེན་པོའི་གནས་ཆེས་མཆོག་ཏུ་གྱུར་པ་གཙོ་བོ་གཅིག་པ་ཅན་ཅིག་སྤགས་པ་བཞིན་དུ་མངོན་པར་གྲུབ་ཀྱི་ས་གཞན་ནི་མེད་དོ་ཞེས་གྲག་གོ། །

[Block 2461]
གཟུགས་མེད་ཁམས་ན་གནས་མེད་དོ། །

[Block 2462]
ཆོས་གཟུགས་ཅན་མ་ཡིན་པ་རྣམས་ལ་ནི་གནས་མེད་དེ། འདས་པ་དང་། མ་འོངས་པ་དང་། རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་དང་། ཆོས་གཟུགས་ཅན་མ་ཡིན་པ་རྣམས་ནི་ཡུལ་ན་མི་གནས་ཞེས་བྱ་བར་ངེས་པ་ཡིན་ནོ། །

[Block 2463]
དེ་ཡང་། སྐྱེ་བ་ལས་ནི་རྣམ་པ་བཞི། །གཟུགས་མེད་པའི་ཁམས་སྐྱེ་བའི་བྱེ་བྲག་གིས་ནི་རྣམ་པ་བཞི་སྟེ། འདི་ལྟ་སྟེ། ནམ་མཁའ་མཐའ་ཡས་སྐྱེ་མཆེད་དང་། རྣམ་ཤེས་མཐའ་ཡས་སྐྱེ་མཆེད་དང་། ཅི་ཡང་མེད་པའི་སྐྱེ་མཆེད་དང་། འདུ་ཤེས་མེད་འདུ་ཤེས་མེད་མིན་གྱི་སྐྱེ་མཆེད་དོ། །

[Block 2464]
དེ་དག་ལ་ཡུལ་གྱིས་བྱས་པའི་བླ་འོག་ནི་མེད་དོ། །

[Block 2465]
[^1290]ཏིང་ངེ་འཛིན་ཐོབ་པ་རྣམས་ཡུལ་གང་དུ་འཆི་འཕོ་བ་དེ་ཉིད་དུ་སྐྱེ་ལ། ཡང་དེ་ནས་འཆི་འཕོ་བ་རྣམས་ཀྱི་སྲིད་པ་བར་མ་ཡང་དེ་ཉིད་དུ་འགྲུབ་བོ། །

[Block 2466]
ཇི་ལྟར་སེམས་ཅན་གཟུགས་ཅན་རྣམས་ཀྱི་སེམས་ཀྱི་རྒྱུད་གཟུགས་ལ་བརྟེན་ནས་འཇུག་པ་དེ་ལྟར་གཟུགས་མེད་པ་དག་ན་ཅི་ལ་བརྟེན་ནས་འཇུག་ཅེ་ན།

[Block 2467 [VERSE]]
དེར་ནི་རིས་དང་སྲོག་ལ་ཡང་། །
སེམས་ཀྱི་རྒྱུད་ནི་བརྟེན་པ་ཡིན། །

[Block 2468]
ཆོས་མངོན་པ་པ་རྣམས་ན་རེ་རིས་མཐུན་པ་དང་། སྲོག་གི་དབང་པོ་ལ་བརྟེན་ནས་སོ་ཞེས་ཟེར་རོ། །

[Block 2469]
འོ་ན་ཅིའི་ཕྱིར་སེམས་ཅན་གཟུགས་ཅན་རྣམས་ཀྱི་སེམས༌[^1291]ཀྱི་རྒྱུན་ཡང་དེ་གཉིས་ཁོ་ན་ལ་བརྟེན་ནས་འཇུག་པར་མི་འགྱུར། སྟོབས་ཆུང་བའི་ཕྱིར་རོ། །

[Block 2470]
དེ་ན་ཅིའི་ཕྱིར་སྟོབས་དང་ལྡན་པ་ཉིད་ཡིན། སྙོམས་པར་འཇུག་པའི་ཁྱད་པར་ལས་སྐྱེས་པའི་ཕྱིར་ཏེ། སྙོམས་པར་འཇུག་པ་དེ་ནི་གཟུགས་དང་བྲལ་བའི་འདུ་ཤེས་ཅན་ཡིན་ནོ། །

[Block 2471]
འོ་ན་ནི་སྟོབས་དང་ལྡན་པའི་ཕྱིར་དེ་ཁོ་ནས་འཇུག་པར་འགྱུར་གྱི་རྟེན་གྱིས་ཅི་ཞིག་བྱ། ཇི་ལྟར་སེམས་ཅན་གཟུགས་ཅན་རྣམས་ཀྱི་རིས་མཐུན་པ་དང་། སྲོག་གི་དབང་པོ་གཟུགས་ལ་བརྟེན་ནས་འཇུག་པ་དེ་ལྟར་སེམས་ཅན་གཟུགས་ཅན་མ་ཡིན་པ་རྣམས་ཀྱི་ཅི་ལ་བརྟེན་ནས་འཇུག་པ་འདི་ཡང་བརྗོད་པར་བྱའོ། །

[Block 2472]
དེ་གཉིས་ཕན་ཚུན་དུའོ། །

[Block 2473]
འོ་ན་ནི༌[^1292]གཟུགས་ཅན་རྣམས་ཀྱི་ཡང་དེ་གཉིས་ཁོ་ན༌[^1293]ཕན་ཚུན་དུ་ཅིའི་ཕྱིར་མི་བརྟེན།[^1294] དེ་གཉིས་སྟོབས་ཆུང་བའི་ཕྱིར་རོ། །

[Block 2474]
དེ་ནི་ཅིའི་ཕྱིར་སྟོབས་དང་ལྡན་པ་ཉིད་ཡིན། སྙོམས་པར་འཇུག་པའི་ཁྱད་པར་ལས༌[^1295]སྐྱེས་པའི་ཕྱིར་རོ། །

[Block 2475]
མདོ་སྡེ་པ་རྣམས་ན་རེ་དེ་ནི་སེམས་ཀྱི་རྒྱུད་དམ། སེམས་ཀྱང་སེམས་ལས་བྱུང་བ་དག་ལ་ཡང་མཚུངས་ཏེ་དེ་ལྟ་བས་ན་སེམས་ཅན་གཟུགས་ཅན་མ་ཡིན་པ་རྣམས་ཀྱི་སེམས་ཀྱི་རྟེན་གཞན་ནི་མེད་དོ་ཞེས་ཟེར་རོ། །

[Block 2476]
གཞན་ཡང་སེམས་ཀྱི་རྒྱུན་གང་གི་འཕེན་པའི་རྒྱུ་གཟུགས་ལ་སྲེད་པ་དང་མ་བྲལ་བ་དེ་ནི་གཟུགས་དང་ལྷན་ཅིག་འབྱུང་བའི་ཕྱིར། གཟུགས་ལ་བརྟེན་ནས་འཇུག་གོ། །

[Block 2477]
[^1296]གང་གི་རྒྱུ་གཟུགས་ལ་སྲེད་པ་དང་བྲལ་བ་དེ་ནི་གཟུགས་ལ་མི་ལྟོས་པར་འཇུག་སྟེ། རྒྱུ་དེ་ལ་རྒྱབ་ཀྱིས་ཕྱོགས་པའི་ཕྱིར་རོ། །

[Block 2478]
ཡང་ཅིའི་ཕྱིར་འདི་དག་འདོད་པ་དང་གཟུགས་དང་གཟུགས་མེད་པའི་ཁམས་རྣམས་ཞེས་བྱ་ཞེ་ན། རང་གི་མཚན་ཉིད་འཛིན་པའི་ཕྱིར་ན་ཁམས་སོ། །

[Block 2479]
འདོད་པ་དང་ལྡན་པའི་ཁམས་ནི་འདོད་པའི་ཁམས་སོ། །

[Block 2480]
གཟུགས་དང་ལྡན་པའི་ཁམས་ནི་གཟུགས་ཀྱི་ཁམས་སོ། །

[Block 2481]
བར་གྱི་ཚིག་མི་མངོན་པར་བྱས་པའི་ཕྱིར་ཏེ། རྡོ་རྗེའི་སོར་གདུབ་ལྟ་བུ་དང་། ན་ལེ་ཤམ་གྱི་བཏུང་བ་ཞེས་བྱ་བ་བཞིན་ནོ། །

[Block 2482]
འདི་ན་གཟུགས་མེད་པས་གཟུགས་མེད་པའོ། །

[Block 2483]
གཟུགས་མེད་པའི་ངོ་བོ་ནི་གཟུགས་མེད་པ་ཉིད་དོ། །

[Block 2484]
ཡང་ན་གཟུགས་སུ་རུང་བ་ནི་གཟུགས་སོ། །

[Block 2485]
གཟུགས་མེད་པས་ན་གཟུགས་མེད་པའོ། །

[Block 2486]
དེའི་ངོ་བོ་ནི་གཟུགས་མེད་པ་ཉིད་དོ། །

[Block 2487]
དེ་དང་ལྡན་པའི་ཁམས་ནི་གཟུགས་མེད་པའི་ཁམས་སོ། །

[Block 2488]
ཡང་ན་འདོད་པ་རྣམས་ཀྱི་ཁམས་ནི་འདོད་པའི་ཁམས་ཏེ། གང་ཞིག་འདོད་པ་རྣམས་འཛིན་པའོ། །

[Block 2489]
གཟུགས་དང་གཟུགས་མེད་པའི༌[^1297]ཁམས་དག་ཀྱང་དེ་དང་འདྲ་བར་རིག་པར་བྱའོ། །

[Block 2490]
འདོད་པ་ཞེས་བྱ་བ་འདི་ཅི་ཡིན་ཞེ་ན། མདོར་བསྡུ་ན་ཁམ་གྱི༌[^1298]ཟས་དང་། འཁྲིག་པ་དང་ལྡན་པའི་འདོད་ཆགས་ཡིན་ཏེ།
--- END BLOCKS ---
