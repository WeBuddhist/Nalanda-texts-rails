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
[Block 2521]
དགྲ་བཅོམ་པ་འཐོབ་པ་ལ་ནི་གཟུགས་དང་གཟུགས་མེད་པ་ན་སྤྱོད་པའི་ལས་དག་གོ། །

[Block 2522 [HEADING]]
#### བྱང་ཆུབ་སེམས་དཔའ། ^4-3-13-0

[Block 2523]
བྱང་ཆུབ་སེམས་དཔའ་བསད་པ༌[^1009]ཞེས་བཤད་པ་གང་ཡིན་པ། གང་ནས་བྱང་ཆུབ་སེམས་དཔའ་ཡིན། །གང་ནས་བཟུང་སྟེ་ངེས་པར་གཏོགས་པའི་བྱང་ཆུབ་སེམས་དཔའ་ཞེས་བརྗོད་པར་བྱ། གང་ནས་མཚན་གྱི་ལས་བྱེད་པ། །གང་ཕན་ཆད་ནས་མཚན་རྣམ་པར་སྨིན་པར་འགྱུར་བའི་ལས་རྣམས་བྱེད་པར་རྩོམ་པའོ། །

[Block 2524]
དེ་ནི་དུས་དེ་ཕན་ཆད་རྟག་ཏུ། བདེ་འགྲོར་རིགས་མཐོང་སྐྱེ་དབང་ཚང་། །ཕོར་གྱུར་ཚེ་རབས་དྲན་མི་ལྡོག་པ་ཡིན་ནོ། །

[Block 2525]
དེའི་འགྲོ་བ་རབ་ཏུ་བསྔགས་པ༌[^1010]ནི་ལྷ་དང་མི་ཡིན་ནོ། །

[Block 2526]
རིགས་མཐོ་བར་སྐྱེ་བ་ནི་རྒྱལ་རིགས་དང་། བྲམ་ཟེ་ལ་སོགས་པའི་རིས༌[^1011]སུ་སྐྱེ་བའོ། །

[Block 2527]
དབང་པོ་ཚང་བ་ནི་དབང་པོ་མ་ཚང་བ་མེད་པའོ། །

[Block 2528]
ཕོ་ཁོ་ན་ཡིན་གྱི་མོ་ལ་སོགས་པ་མ་ཡིན་ནོ། །

[Block 2529]
སྐྱེ་བ་ཐམས་ཅད་དུ་ཡང་ཚེ་རབས་དྲན་པར་འགྱུར་རོ། །

[Block 2530]
བྱང་ཆུབ་ལས་མི་ལྡོག་པར་ཡང་འགྱུར་རོ། །

[Block 2531]
མཚན་མ་རྣམ་པར་སྨིན་པ་ཅན་གྱི་ལས་སུ་བཤད་པ་གང་ཡིན་པ་དེ་ནི་གླིང་གང་ཞིག་ཏུ་ཞེ་ན།

[Block 2532 [VERSE]]
དེ་ནི་འཛམ་གླིང་ཕོར༌[^1012]གྱུར་ཏེ། །
མངོན་སུམ༌[^1013]སངས་རྒྱས་ལ་སེམས་པ། །
བསམ་པ་ལས་བྱུང་བསྐལ་པ་བརྒྱ། །
ལུས་པ་དག་ཏུ་འཕེན་པར་བྱེད། །

[Block 2533]
འཛམ་བུའི་གླིང་ཁོ་ནར་འཕེན་གྱི་དེ་དག་བློ་རྣོ་བའི་ཕྱིར་རོ། །

[Block 2534]
ཕོ་ཁོ་ནས་ཡིན་གྱིས་མོས་ནི་མ་ཡིན་ནོ། །

[Block 2535]
སྟོན་པ་མངོན་སུམ་དུ་གྱུར་པ་དང་སངས་རྒྱས་ལ་དམིགས་པའི་སེམས་ཁོ་ནས་བསྐལ་པ་བརྒྱ་ལུས་པའི་ཚེ་འཕེན་གྱི་བསྐལ་པ་མང་པོ་ལུས་པའི་ཚེ་ནི་མ་ཡིན་ནོ། །

[Block 2536]
ལས་དེ་ཡང་བསམས་པ་ལས་བྱུང་བའོ། །

[Block 2537]
མཚན་དེ་དག་ཀྱང་། རེ་རེའང་བསོད་ནམས་བརྒྱ་ལས་སྐྱེས། །བསོད་ནམས་ཀྱི་ཚད་ནི་བྱང་ཆུབ་སེམས་དཔའ་བྱང་ཆུབ་ལ་ཉེ་བ་མ་གཏོགས་པ་སེམས་ཅན་གྱི་ལོངས་སྤྱོད་ཀྱི༌[^1014]འབྲས་བུ་ཅན་ཇི་སྙེད་པ་ཙམ་མོ། །

[Block 2538]
ཡང་བཅོམ་ལྡན་འདས་བྱང་ཆུབ་སེམས་དཔར་གྱུར་པ་ན༌[^1015]སངས་རྒྱས་ཇི་སྙེད་ཅིག་ལ་བསྙེན་བཀུར་བྱས་ཤེ་ན། བསྐལ་པ་གྲངས་མེད་པ་དང་པོ་ལ་བདུན་ཁྲི་ལྔ་སྟོང་ལ།

[Block 2539]
གཉིས་པ་ལ་བདུན་ཁྲི་དྲུག་སྟོང་ལ།

[Block 2540]
གསུམ་པ་ལ་བདུན་ཁྲི་བདུན་སྟོང་ལའོ། །

[Block 2541]
བསྐལ་པ་གྲངས་མེད་པ་གང་གི་ཐ་མར་སངས་རྒྱས་གང་ཞིག་བྱུང་བར་གྱུར་ཅེ་ན།

[Block 2542 [VERSE]]
རྣམ་གཟིགས་མར་མེ་རིན་ཆེན་གཙུག །
གྲངས་མེད་གསུམ་གྱི་ཐ་མར་བྱུང་། །

[Block 2543]
རིན་ཆེན་གཙུག་ཏོར་ཅན་གྱི་ཚེ་ནི་གྲངས་མེད་པ་དང་པོ་རྫོགས་སོ། །

[Block 2544]
མར་མེ་མཛད་ཀྱི་ཚེ་གཉིས་པའོ། །

[Block 2545]
རྣམ་པར་གཟིགས་ཀྱི་ཚེ་གསུམ་པའོ། །

[Block 2546]
དེ་དག་ཐམས་ཅད་ཀྱི།

[Block 2547]
དང་པོ་ཤཱཀྱ་ཐུབ་པ་ཡིན། དེ་ལ་བཅོམ་ལྡན་འདས་ཀྱིས་བདག་ཀྱང་འདི་འདྲ་བའི་རྣམ་པ་ཁོ་ནར་ཤོག་ཤིག༌[^1016]ཅེས་དང་པོར་སྨོན་ལམ་བཏབ་པོ། །ཡང་བྱང་ཆུབ་སེམས་དཔའ་གནས་སྐབས་གང་དུ་ཕ་རོལ་ཏུ༌[^1017]ཕྱིན་པ་གང་རྫོགས་པར་བྱེད་ཅེ་ན།

[Block 2548 [VERSE]]
ཀུན་ལ་ཐམས་ཅད་སྙིང་རྗེ་ཡིས། །
སྦྱིན་པར་བྱེད་པས་སྦྱིན་པ་རྫོགས། །

[Block 2549]
གང་གིས༌[^1018]ཀུན་ལ་མིག་གི་བར་དང་རྐང་པའི་བར་ཐམས་ཅད་མངོན་པར་མཐོ་བའི་ཁྱད་པར་ཅན་ལ་མི་རེ་བར་སྙིང་རྗེས་སྦྱིན་པར་བྱེད་ན་དེ་ཙམ་གྱིས་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཡོངས་སུ་རྫོགས་པ་ཡིན་ནོ། །

[Block 2550 [VERSE]]
ཆགས་བཅས་ཡན་ལག་བཅད་ཀྱང་ནི། །
མི་འཁྲུག་བཟོད་དང་ཚུལ་ཁྲིམས་ཀྱི། །

[Block 2551]
གང་གི༌[^1019]ཚེ་འདོད་ཆགས་དང་མ་བྲལ་བ་བཞིན་དུ་ཡན་ལག་བཅད་ཀྱང་ཅུང་ཟད་ཀྱང་མི་འཁྲུག་པ་དེའི་ཚེ་འདིའི་ཚུལ་ཁྲིམས་དང་བཟོད་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དག༌[^1020]ཡོངས་སུ་རྫོགས་པ་ཡིན་ནོ། །

[Block 2552]
སྐར་རྒྱལ་བསྟོད་པས༌[^1021]བརྩོན་འགྲུས་ཀྱི། །བཅོམ་ལྡན་འདས་དེ་བཞིན་གཤེགས་པ་སྐར་རྒྱལ་ལ་རྐང་པ་གཅིག་གིས་འགྲེང་སྟེ། ཞག་བདུན་གྱི་བར་དུ་ཚིགས་སུ་བཅད་པ་གཅིག་གིས་བསྟོད་པ་དེའི་ཚེ་བརྩོན་འགྲུས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཡང་ཡོངས་སུ་རྫོགས་ལ་བསྐལ་པ་དགུ་ཡང་བསྡུམས་སོ། །

[Block 2553]
དེ་མ་ཐག་པའི་ཏིང་འཛིན་བློའི། །བྱང་ཆུབ་པའི་སྔོན་རོལ་གྱི་དེ་མ་ཐག་རྡོ་རྗེ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་གྱི་ཚེ་བསམ་གཏན་དང་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དག་ཡོངས་སུ་རྫོགས་སོ། །

[Block 2554 [HEADING]]
#### བསོད་ནམས་བྱ་བའི་གཞི་གསུམ། ^4-3-14-0

[Block 2555]
མདོ་ལས་བསོད་ནམས་བྱ་བའི་གཞི་གསུམ་གསུངས་པ་དེ་ནི་ཇི་ལྟར་བསོད་ནམས་བྱ་བའི་གཞི་གསུམ་ཡིན་ཞེ་ན།

[Block 2556 [VERSE]]
གསུམ་པོ་བསོད་ནམས་བྱ་བ་དང་། །
དེ་བཞིན་དཔེར་ན་ལས་ལམ་བཞིན། །

[Block 2557]
དེ་ལ་སྦྱིན་པ་ལས་བྱུང་བའི་བསོད་ནམས་བྱ་བའི་གཞི་ལ་ལུས་དང་ངག་གི་ལས་ནི་རྣམ་པ་གསུམ་ཆར་ཡིན་ནོ། །

[Block 2558]
དེ་ཀུན་ནས་སློང་བར་བྱེད་པའི་སེམས་པ་ནི་བསོད་ནམས་ཡང་ཡིན་ལ་བྱ་བ་ཡང་ཡིན་ནོ། །

[Block 2559]
དེ་དང་ལྷན་ཅིག་འབྱུང་བའི་ཆོས་རྣམས་ནི་བསོད་ནམས་ཁོ་ན་ཡིན་ནོ། །

[Block 2560]
ཚུལ་ཁྲིམས་ལས་བྱུང་བའི་ལུས་དང་ངག་གི་ལས་ཁོ་ན་ཡིན་པས་གསུམ་ཆར་ཡིན་ནོ། །
--- END BLOCKS ---
