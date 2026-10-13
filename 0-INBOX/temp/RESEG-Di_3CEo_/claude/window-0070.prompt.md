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
ཉོན་མོངས་པ་ཤས་ཆེ་བ་རྒྱུན་དུ་འབྱུང་བ་ནི་ཉོན་མོངས་པའི་སྒྲིབ་པའོ། །

[Block 2452]
ངན་སོང་རྣམ་པ་གསུམ་དང་མི་དང་ལྷའི་ཕྱོགས་གཅིག་ན༌[^976]རྣམ་པར་སྨིན་པའི་སྒྲིབ་པའོ། །

[Block 2453]
ཡང་སྒྲིབ་པ་འདི་དག་པས༌[^977]གང་ཞིག་འགྲོ་བ་གང་དག་ན་ཡོད་པར་རིག་པར་བྱ་ཞེ་ན། རེ་ཞིག་གཅིག་ཏུ།

[Block 2454 [VERSE]]
མཚམས་མེད་གླིང་གསུམ་དག་ན་ཡོད། །
སྒྲ་མི་སྙན་མ་གཏོགས་པའོ། །

[Block 2455]
དེ་དག་ན་ཡང་སྐྱེས་པ་དང་བུད་མེད་རྣམས་ཁོ་ན་ལ་སྟེ།

[Block 2456 [VERSE]]
ཟ་མ་སོགས་ལ་མི་འདོད་དོ། །
ཕན་དང་ངོ་ཚ་ཆུང་བའི་ཕྱིར། །

[Block 2457]
དེ་དག་གི་ཕ་མ་ཕན་ཆུང་བ་སྟེ། ལུས་མ་ཚང་བའི་བདག་པོར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 2458]
དེ་དག་ཀྱང་ཕ་མ་ལ་ངོ་ཚ་ཤེས་པ་དང་ཁྲེལ་ཡོད་པ་ཤས༌[^978]ཆེན་པོས་ཉེ་བར་མི་གནས་པས་སོ། །

[Block 2459]
ལས་ཀྱི་སྒྲིབ་པ་བཤད་ཟིན་ཏོ། །

[Block 2460]
ལྷག་མ་འགྲོ་བ་ལྔ་དག་ན། །ཉོན་མོངས་པའི་དང་། རྣམ་པར་སྨིན་པའི་སྒྲིབ་པ་ནི་ལྷག་མ་དག་གོ། །

[Block 2461]
མི་དག་གི་ནང་ན་ནི་སྒྲ་མི་སྙན་པ༌[^979]རྣམ་པར་སྨིན་པའི་སྒྲིབ་པ་ཡིན་ནོ། །

[Block 2462]
ལྷ་དག་གི་ནང་ན༌[^980]ནི་འདུ་ཤེས་མེད་པའི་སེམས་ཅན་རྣམས་སོ། །

[Block 2463 [HEADING]]
##### མཚམས་མེད་པ། ^4-3-12-1-0

[Block 2464]
མཚམས་མེད་པ་རྣམས་ཀྱི་ནང་ནས་གསུམ་ནི་སྲོག་གཅོད་པའོ། །

[Block 2465]
གཅིག་ནི་བརྫུན་དུ་སྨྲ་བའི་རང་བཞིན་ཡིན་ནོ། །

[Block 2466 [VERSE]]
གཅིག་ནི་སྲོག་གཅོད་པའི་སྦྱོར་བའོ། །
དགེ་འདུན་དབྱེན་ནི་མི་འཕྲོད་པའི། །
རང་བཞིན་ལྡན་པ་མ་ཡིན་ཆོས། །
ཉོན་མོངས་ཅན་མིན་ལུང་བསྟན་མིན། །

[Block 2467 [VERSE]]
དེ་དང་དགེ་འདུན་ཡང་དག་ལྡན། །
དེ་ཡི་ཁ་ན་མ་ཐོ་བརྫུན། །
དེ་དང་འབྱེད་པོ་ཡང་དག་ལྡན། །

[Block 2468]
དགེ་འདུན་གྱི་དབྱེན་ཞེས་བྱ་བ་ནི་མི་འཕྲོད་པ་སྟེ། ལྡན་པ་མ་ཡིན་པའི་ཆོས་ཉོན་མོངས་པ་ཅན་མ་ཡིན་པ་སྟེ། ཇི་ལྟར་མཚམས་མེད་པར་འགྱུར། གང་གིས་དེ་འབྱེད་པར་བྱེད་པའི་བརྫུན་དུ་སྨྲ་བ་དེ་ནི་མཚམས་མེད་པ་པའི༌[^981]རང་བཞིན་ཡིན་ནོ། དེ་དང་ཡང་འབྱེད་པ་པོ་ཡང་དག་པར་ལྡན་ནོ། །

[Block 2469]
བསྐལ་པར་མནར་མེད་པར་སྨིན་འགྱུར། །གཞན་དག་གིས་ནི་བར་གྱི་བསྐལ་པར་ནི་མ་ངེས་སོ། །

[Block 2470]
ཡང་གང་ཞིག་གིས་མཚམས་མེད་པ་མང་པོ་བྱས་པ་ཡིན་ལ། དེ་དག་བར་ཆད་མེད་པ་ཁོ་ནར་སྨིན་པར་གྱུར་ན་དེ་ལ་དེ་དག་ཅི་ཞིག་ཏུ་འགྱུར་ཞེ་ན། ལྷག་པས་གནོད་པ་ལྷག་པར་འགྱུར། །དེ་མཚམས་མེད་པ་མང་པོས་མནར་མེད་པ་དེར་གང་གིས་ན་གཉིས་དང་། གསུམ་དང་། བཞི་དང་། ལྔ་འགྱུར་གྱི༌[^982]ཚོར་བ་མྱོང་བར་འགྱུར་བའི་ལུས་ཆེན་པོ་གཞོན་ཤ་ཅན་གྱི་ལུས་ཐོབ་ཅིང་། གནོད་པ་ཡང་རབ་ཏུ་མང་བ་དང་ཤིན་ཏུ་མི་བཟད་པར་འགྱུར་རོ། །

[Block 2471]
དགེ་འདུན་འབྱེད་པར་བྱེད་པ་དེ་སུ་ཞིག་ཡིན་ཞེ་ན། དགེ་སློང་ལྟ་སྤྱད་ཚུལ་ལྡན་པས། །འབྱེད་དོ། །

[Block 2472]
དགེ་སློང་གིས་འབྱེད་ཀྱིས༌[^983]ཁྱིམ་པ་དང་། དགེ་སློང་མ་ལ་སོགས་པས་ཀྱང་མ་ཡིན་ནོ། །

[Block 2473]
དེ་ཡང་ལྟ་བ་སྤྱད་པ་ཁོ་ནས་འབྱེད་ཀྱི་སྲེད་པ་སྤྱད་པས་ནི་མ་ཡིན་ནོ། །

[Block 2474]
ཚུལ་ཁྲིམས་དང་ལྡན་པས་འབྱེད་དེ། དེའི་ཚིག་གཟུང་བར༌[^984]འོས་པའི་ཕྱིར་རོ། །

[Block 2475]
ཉམས་པས༌[^985]ནི་མ་ཡིན་ཏེ།

[Block 2476]
བཅོམ་ལྡན་འདས་ཀྱི་དྲུང་ལས།

[Block 2477]
གཞན་དུའོ། །

[Block 2478]
སྟོན་པ་མངོན་སུམ་དུ་བཞུགས་པ་ཉིད་དུ་དབྱེ་བར་མི་ནུས་པའི་ཕྱིར་རོ། །སུ་དག་གཅིག་འབྱེད་ཅེ་ན། བྱིས་པ་རྣམས། སོ་སོའི་སྐྱེ་བོ་རྣམས་ཁོ་ན་ཡིན་གྱི་འཕགས་པ་རྣམས་ནི་མ་ཡིན་ཏེ། ཆོས་མངོན་སུམ་དུ་གྱུར་པའི་ཕྱིར་རོ། །

[Block 2479]
དེ་ཡང་། སྟོན་དང་ལམ་གཞན་ལ་བཟོད་པ། །བྱེ་བའོ། །

[Block 2480]
གང་གི་ཚེ་དེ་དག་གིས་དེ་བཞིན་གཤེགས་པ་ལས་གཞན་པའི་སྟོན་པ་དང་། དེས་བསྟན་པའི་ལམ་ལས་གཞན་པའི་ལམ་ལ་བཟོད་ན་དེ་ཙམ་གྱིས་དགེ་འདུན་བྱེ་བ་ཞེས་བརྗོད་དོ། །

[Block 2481]
བྱེ་ནས་ཀྱང་དེ་ཉིད་ཀྱི་ནུབ་གཅིག་ཏུ་དེ་ནི་མི་གནས་སོ། །

[Block 2482]
དགེ་འདུན་བྱེ་ན༌[^986]གདོན་མི་ཟ་བར་ནམ་མ་ལངས་པ་ཉིད་དུ་དགེ་འདུན་འདུམ་པར༌[^987]འགྱུར་རོ། །

[Block 2483]
དགེ་འདུན་གྱི་དབྱེན་དུ་བཤད་པ་གང་ཡིན་པ། དེ་ནི་འཁོར་ལོའི་དབྱེན་དུ་འདོད། །དེའི་ཚེ་ལ་མ་འཇུག་པའི་གེགས་སུ་གྱུར་པའི་ཕྱིར་དེའི་ཚེ་བཅོམ་ལྡན་འདས་ཀྱི་ཆོས་ཀྱི༌[^988]འཁོར་ཡང་ཕྱེ་བ་ཡིན་ནོ། །

[Block 2484]
ཡང་འཁོར་ལོའི་དབྱེན་གང་དུའམ་ཇི་ཙམ་གྱིས་ཤེ་ན། འཛམ་བུའི་གླིང་ནའོ་དགུ་སོགས་ཀྱིས། །བརྒྱད་ནི་གདོན་མི་ཟ་བར་ཕྱོགས་གཉིས་ན་གནས་པ་དང་།

[Block 2485]
དགུ་པ་ནི་དབྱེན་བྱེད་པ་པོ་ཡིན་ཏེ། ལྷག་མི་ནི་ངེས་པ་མེད་དོ། །

[Block 2486]
གཞན་ནི་ལས་ཀྱི་དབྱེན་ལས་འགྱུར་ཏེ། གལ་ཏེ་མཚམས་གཅིག་གི་ནང་དུ་མི་མཐུན་པས་ལས་དག་བྱེད་ནའོ། །

[Block 2487]
དེ་ཡང་ནི།

[Block 2488 [VERSE]]
ལས་ཀྱི༌[^989]དབྱེན་ནི་གླིང་གསུམ་ནའོ། །
སྒྲ་མི་སྙན་མ་གཏོགས་སོ། །
དེ་ནི་བརྒྱད་དག་ཡན་ཆད་ཀྱིས། །

[Block 2489]
འཁོར་ལོའི་དབྱེན་དུས་དྲུག་ཏུ་མི་འབྱུང་ངོ་། །འདི་ལྟ་སྟེ།

[Block 2490]
དང་པོ་མཐའ་སྐྱོན་ཟུང་གཅིག་གི །
--- END BLOCKS ---
