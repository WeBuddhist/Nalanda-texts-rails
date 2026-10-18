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
གཟུགས་དང་གཟུགས་མེད་པའི་ཁམས་དག་ན་ནི་ལྷའི་འགྲོ་བ་གཅིག་ཁོ་ནའི་ཕྱོགས་སོ། །གང་གིས་ན། དེ་དག་ཁམས་དག་ཏུ་ཞེས་བྱ་བ་ཅི་འགྲོ་བ་ལས་མ༌[^1318]གཏོགས་པའི་ཁམས་དག་ཅིག་ཡོད་དམ་ཞེ་ན། ཡོད་དེ་ཁམས་རྣམས་ནི་དགེ་བ་དང་། ཉོན་མོངས་པ་ཅན་དང་། སྣོད་དང་སྲིད་པ་བར་མ་པའི་རང་བཞིན་དག་ཀྱང་ཡིན་གྱི་འགྲོ་བ་ལྔ་པོ་གང༌[^1319]དག༌[^1320]ཡིན་པ། དེ་དག་ཉོན་མོངས་ཅན་མིན་ལུང་བསྟན་མིན། །སེམས་ཅན་ཞེས་བྱ་བར་སྲིད་མིན། །འགྲོ་བ་རྣམས་ནི་མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་ཁོ་ནའོ། །

[Block 2522]
དེ་ལྟ་མ་ཡིན་ན་འགྲོ་བ་ལྔ་འཆོལ་བར་འགྱུར་རོ། །

[Block 2523]
སེམས་ཅན་ཞེས་བྱ་བ་ཁོ་ན་ཡིན་ཡང་སྲིད་པ་བར་མའི་རང་བཞིན་དག་ནི་མ་ཡིན་ནོ། །

[Block 2524]
བཏགས་པ་ལས་ཀྱང་། སྐྱེ་གནས་བཞིས་ནི་འགྲོ་བ་ལྔ་བསྡུས་ཀྱི་འགྲོ་བ་ལྔས་ནི་སྐྱེ་གནས་བཞི་མ་བསྡུས་ཏེ། གང་ཞིག་མ༌[^1321]བསྡུས་ཤེ་ན། སྲིད་པ་བར་མའོ་ཞེས་གསུངས་སོ། །

[Block 2525]
ཆོས་ཀྱི་ཕུང་པོ་ལས་ཀྱང་མིག་གི་ཁམས་གང་ཞེ་ན། འབྱུང་བ་ཆེན་པོ་བཞི་དག་རྒྱུར་བྱས་པའི་གཟུགས་དང་བ་གང་ཡིན་པ་དམྱལ་བ་འམ་དུད་འགྲོའི་སྐྱེ་གནས་པ་དང་ཡི་དགས་པའི་ཡུལ་པའམ། ལྷ་འམ་མི་འམ། བསྒོམས་པ་ལས་བྱུང་བའམ། སྲིད་པ་བར་མ་པའི༌[^1322]མིག་དང་། མིག་གི་དབང་པོ་དང་། མིག་གི་སྐྱེ་མཆེད་དང་། མིག་གི་ཁམས་སོ་ཞེས་གསུངས་སོ། །

[Block 2526]
མདོ་ལས་ཀྱང་སྲིད་པ་བར་མ་འགྲོ་བ་རྣམས་ལས་ལོགས་ཤིག་ཏུ་མཛད་དོ། །

[Block 2527]
མདོ་གང་ལས་ཤེ་ན་སྲིད་པ་ནི་བདུན་ཏེ། དམྱལ་བའི་སྲིད་པ་དང་། དུད་འགྲོའི་སྲིད་པ་དང་། ཡི་དགས་ཀྱི་སྲིད་པ་དང་། ལྷའི་སྲིད་པ་དང་། མིའི་སྲིད་པ་དང་། ལས་ཀྱི་སྲིད་པ་དང་། སྲིད་པ་བར་མའོ་ཞེས་གསུངས་པ་ལས་ཏེ། འདིར་ནི་འགྲོ་བ་ལྔ་པོ་རྒྱུ་དང་བཅས་པ་དང་འགྲོ་བ་དང་བཅས༌[^1323]པར་བཤད་དོ། །

[Block 2528]
དེ་ཉིད་ཀྱི་ཕྱིར་མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པར་འགྲུབ་སྟེ། དེའི་རྒྱུ་ལས་དེ་དག་ལས༌[^1324]ལོགས་ཤིག་ཏུ་མཛད་པའི་ཕྱིར་རོ། །

[Block 2529]
ཁ་ཆེ་བ་རྣམས་ཀྱང་གནས་བརྟན་ཤཱ་རིའི་བུས་ཚེ་དང་ལྡན་པ་དམྱལ་བ་པའི་ཟག་པ་རྣམས་མངོན་དུ་གྱུར་པ་ལས་དམྱལ་བ་མྱོང་བར་འགྱུར་བའི་ལས་རྣམས་བྱེད་ཅིང་སོགས་པར་འགྱུར་རོ། །

[Block 2530]
ཚེ་དང་ལྡན་པ་ལུས་དང་ངག་དང་ཡིད་ཀྱི་དཀྱིལ་འཁོར་དང་། ལུས་དང་ངག་དང་ཡིད་ཀྱི་སྐྱོན་དང་། སྙིགས་མ་དེ་དག་གི་རྣམ་པར་སྨིན་པ་གཟུགས་དང་། ཚོར་བ་དང་། འདུ་ཤེས་དང་། འདུ་བྱེད་དང་། རྣམ་པར་ཤེས་པ་ནི་དམྱལ་བ་དག་ཏུ་རྣམ་པར་སྨིན་པར་འགྱུར་ཏེ། རྣམ་པར་སྨིན་པར༌[^1325]གྲུབ་ནས་དམྱལ་བ་ཞེས་བྱ་བའི་གྲངས་སུ་འགྲོའོ། །

[Block 2531]
ཚེ་དང་ལྡན་པ་དེ་ལ་ཆོས་དེ་དག་མ་གཏོགས་པ་དམྱལ་བ་མི་དམིགས་སོ་ཞེས་གསུངས་སོ་ཞེས༌[^1326]མདོ་འདོན་ཏེ། [^1327]དེའི་ཕྱིར་ཡང་འགྲོ་བ་དག་ནི་མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 2532]
འོ་ན་ནི་རབ་ཏུ་བྱེད་པའི་གཞུང་འགྲོ་བ་དག་ལ་ཕྲ་རྒྱས་ཐམས་ཅད་རྒྱས་པར་འགྱུར་རོ༌[^1328]ཞེས་འབྱུང་བའི་ལན་གདབ་པར་བྱ་དགོས་སོ་ཞེ་ན། འགྲོ་བ་རྣམས་སུ་ཉིང་མཚམས་སྦྱོར་བའི་སེམས་རྣམ་པ་ལྔ་ཡོད་དེ། དེའི་ཕྱིར་འཇུག་པ་དང་བཅས་པའི་འགྲོ་བ་སྨོས་པས་དེ་ནི་ཉེས་པ་མེད་དེ། གྲོང་སྨོས་ན་གྲོང་གི་ཉེ་འཁོར་ཡང་སྨོས་པ་བཞིན་ནོ། །

[Block 2533]
གཞན་དག་ན་རེ་དགེ་བ་དང་ཉོན་མོངས་པ་ཅན་དག་ཀྱང་ཡོད་དོ། །

[Block 2534]
ལས་དེ་དག་ལས་ལོགས་ཤིག་ཏུ་མཛད་པའི་ཕྱིར་རོ་ཞེས་གང་བཤད་པ་ནི་ཐ་དད་དུ་གསུངས་པའི་ཕྱིར་ལོགས་ཤིག་ཏུ་མཛད་པ་ཡིན་པར་ངེས་པ་མེད་དེ། དཔེར་ན་སྙིགས་མ་ལྔ་པོ་དག་ཏུ་ཉོན་མོངས་པ་དང་ལྟ་བའི་སྙིགས་མ་དག་ཐ་དད་དུ་གསུངས་ཀྱང་ལྟ་བ་རྣམས་ཉོན་མོངས་པ་དག་མ་ཡིན་པ་ཡང་མ་ཡིན་པ་དེ་བཞིན་དུ་ལས་ཀྱི་སྲིད་པ་ཡང་ཡིན་འགྲོ་བ་ཡང་ཡིན་འགྲོ་བའི་རྒྱུ་ཤེས་པར་བྱ་བའི་ཕྱིར་འདི་ཐ་དད་དུ་བསྟན་པ་ཡང༌[^1329]ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 2535]
འདི་ནི་སྲིད་པ་བར་མ་ཡང་ཐལ་བར་འགྱུར་རོ་ཞེ་ན། མི་རུང་བའི་ཕྱིར་མ་ཡིན་ཏེ། དེར་འགྲོ་བས་ན་འགྲོ་བ་ཡིན་ན་སྲིད་པ་བར་མ་ནི་འགྲོ་བར་བྱ༌[^1330]བ་མ་ཡིན་ཏེ། འཆི་འཕོ་བའི་ཡུལ་ཉིད་དུ་སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 2536]
གཟུགས་མེད་པ་རྣམས་ཀྱང་འགྲོ་བ་མ་ཡིན་པར་འགྱུར་ཏེ་འཆི་འཕོ་བའི་ཡུལ་ཉིད་དུ་སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 2537]
དེ་ལྟ་ན་འོ་ན་ནི་སྲིད་པ་བར་མ་ཡིན་པ་ཁོ་ནའི་ཕྱིར་སྲིད་པ་བར་མ་འགྲོ་བ་མ་ཡིན་ཏེ། འགྲོ་བའི་བར་མ་དོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2538]
གལ་ཏེ་འགྲོ་བ་ཡིན་པར་གྱུར་ན་ནི་སྲིད་པ་བར་མ་ཞེས་བྱ་བ་ཉིད་དུ་ཡང་མི་འགྱུར་རོ། །

[Block 2539]
འོ་ན་གནས་བརྟན་ཤཱ་རིའི་བུས་རྣམ་པར་སྨིན་པ་གྲུབ་ནས་དམྱལ་བ་ཞེས་བྱ་བའི་གྲངས་སུ་འགྲོའོ་ཞེས་གང་བཤད་པ་ཇི་ལྟར་དྲང་། རྣམ་པར་སྨིན་པ་གྲུབ་ནས་ཞེས་བཤད་ཀྱི་རྣམ་པར་སྨིན་པ་ཁོ་ནའོ་ཞེས་ནི་མ་བཤད་པ་ཇི་ལྟར། འོ་ན་ཚེ་དང་ལྡན་པ་དེ་ལ་ཆོས་དེ་དག་མ་གཏོགས་པ་དམྱལ་བ་མི་དམིགས་སོ་ཞེས་གང་བཤད་པ་ཇི་ལྟར་དྲང་། ཕུང་པོ་དག་ལས་གཞན་པ་དམྱལ་བ་མི་དམིགས་སོ༌[^1331]ཞེས་འགྲོ་བར་འགྲོ་བའི་གང་ཟག་གི་རྫས་འགོག་པར་བྱེད་པ་ཡིན་གྱི་ཕུང་པོ་གཞན་འགོག་པ་ནི་མ་ཡིན་ནོ། །

[Block 2540]
བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ་འགྲོ་བ་རྣམས་ནི་མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་དག་ཁོ་ན་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 2541]
དེ་དག་ཀྱང་ཁ་ཅིག་ན་རེ་རྣམ་པར་སྨིན་པའི་རང་བཞིན་དག་ཁོ་ན་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 2542]
གཞན་དག་ན་རེ་རྒྱས་པ་ལས་བྱུང་བའི་རང་བཞིན་དག་ཀྱང་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 2543 [HEADING]]
#### རྣམ་ཤེས་གནས་པ་བདུན། ^3-1-3-0

[Block 2544]
འགྲོ་བ་ལྔ་པའི་ཁམས་གསུམ་པ༌[^1332]འདི་ཉིད་དུ།

[Block 2545 [VERSE]]
ལུས་དང་འདུ་ཤེས་ཐ་དད་དང་། །
ལུས་ཐ་དད་ཅིང་འདུ་ཤེས་གཅིག །
བཟློག་དང་ལུས་དང་འདུ་ཤེས་གཅིག །
གཟུགས་ཅན་མ་ཡིན་གསུམ་པོ་དག །

[Block 2546]
རྣམ་ཤེས་གནས་པ་བདུན་རིམ་བཞིན་དུ་རིག་པར་བྱའོ། །

[Block 2547 [HEADING]]
##### ལུས་ཐ་དད་ཅིང་འདུ་ཤེས་ཐ་དད་པ། ^3-1-3-1-0

[Block 2548]
མདོ་ལས་སེམས་ཅན་གཟུགས་ཅན་ལུས་ཐ་དད་ཅིང་འདུ་ཤེས་ཐ་དད་པ་དག་ཀྱང༌[^1333]ཡོད་དེ། འདི་ལྟ་སྟེ་མི་རྣམས་དང་ལྷ་ཁ་ཅིག་གོ། །

[Block 2549]
འདི་ནི་རྣམ་པར་ཤེས་པ་གནས་དང་པོའོ༌[^1334]ཞེས་གསུངས་ཏེ། ལྷ་ཁ་ཅིག་གང་ཞེ་ན། འདོད་པ་ན་སྤྱོད་པ་རྣམས་དང་། བསམ་གཏན་དང་པོ་པ་དང་པོར་བྱུང་བ་མ་གཏོགས་པ་རྣམས་སོ། །

[Block 2550]
དེ་དག་གི་ལུས་ཐ་དད་པའི་ཕྱིར་རམ། དེ་དག་གི་ལུས་ཐ་དད་པ་ཡིན་པས་ན་ལུས་ཐ་དད་པ་དག་སྟེ། ཁ་དོག་དང་རྟགས་དང་དབྱིབས་དུ་མའི་ཕྱིར་རོ། །

[Block 2551]
འདུ་ཤེས་དུ་མའི་ཕྱིར་འདུ་ཤེས་ཐ་དད་པའོ། །

[Block 2552]
དེ་འདི་དག་ལ་ཡོད་པས་འདུ་ཤེས་ཐ་དད་པ་རྣམས་ཏེ། བདེ་བ་དང་། སྡུག་བསྔལ་བ་དང་། སྡུག་བསྔལ༌[^1335]ཡང་མ་ཡིན་བདེ་བ་ཡང་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2553 [HEADING]]
##### ལུས་ཐ་དད་ཅིང་འདུ་ཤེས་གཅིག་པ། ^3-1-3-2-0

[Block 2554]
སེམས་ཅན་གཟུགས་ཅན་ལུས༌[^1336]ཐ་དད་ཅིང་འདུ་ཤེས་གཅིག་པ་དག་ཀྱང་ཡོད་དེ། འདི་ལྟ་སྟེ་ཚངས་རིས་ཀྱི་ལྷ་གང་དག་དང་པོར་བྱུང་བ་དེ་དག་གོ། །

[Block 2555]
འདི་ནི་རྣམ་པར་ཤེས་པ་གནས་པ་གཉིས་པའོ་ཞེས་གསུངས་ཏེ། དང་པོར་བྱུང་བ་དེ་དག་ཐམས་ཅད་ནི་འདི་སྙམ་དུ་བདག་ཅག་ནི་ཚངས་པ་འདིས་ཕྱུང་ངོ་སྙམ་དུ་འདུ་ཤེས་པར་འགྱུར་ལ། ཚངས་པ་ཡང་འདི་སྙམ་དུ་འདི་དག་ནི་བདག་གིས་ཕྱུང་ངོ་སྙམ་དུ་སེམས་པས་འདུ་ཤེས་ཀྱི་རྒྱུ་བ་ཐ་མི་དད་པའི་ཕྱིར་འདུ་ཤེས་གཅིག་པ་དག་ཡིན་ནོ། །

[Block 2556]
ཚངས་པ་ཆེན་པོའི་ཆུ་ཞེང་དང་དབྱིབས་ཀྱི་ལུས༌[^1337]དང་། ཚིག་ཏུ་བརྗོད་པ་དང་། གོས་གྱོན་པ་ཡང་གཞན་ཡིན་ལ། དེའི་འཁོར་གྱི་ཡང་གཞན་ཡིན་པས་ན་ལུས་ཐ་དད་པ་དག་ཡིན་ནོ། །

[Block 2557]
མདོ་ལས་དེ་དག་འདི་སྙམ་དུ་བདག་ཅག་གིས་སེམས་ཅན་འདི་ཚེ་རིང་ཞིང་དུས་རིང་པོར་གནས་པར༌[^1338]མཐོང་ལ༌[^1339]ཞེས་བྱ་བ་ནས་སེམས་ཅན་འདི་ཡང་སེམས་ལ་འདི་སྙམ་དུ་ཀྱེ་མ་སེམས་ཅན་གཞན་དག་ཀྱང་འདིར་བདག་དང་སྐལ་བ་མཉམ་པར་སྐྱེ་བར་གྱུར་ཅིག་སྙམ་དུ་སྨོས༌[^1340]ལ། བདག་ཅག་ཀྱང་འདིར་སྐྱེས་པས་ཞེས་བྱ་བར་ཤེས་སོ་ཞེས་གང་གསུངས་པ། དེ་དག་གིས་དེ་ཇི་ལྟར་མཐོང་ཞེ་ན། ཁ་ཅིག་ན་རེ་འོད་གསལ་ལ་གནས་པ་རྣམས་ཀྱིས་ཏེ། དེ་དག་ནི་དེ་ནས་ཤི་འཕོས་པ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 2558]
དེ་ནི་བསམ་གཏན་གཉིས་པའི་སྙོམས་པར་འཇུག་པ་མ་ཐོབ་ན་ནི་ཇི་ལྟར་ན་དེའི་ས་པའི་སྔོན་གྱི་གནས་རྗེས་སུ་དྲན། འོན་ཏེ་ཐོབ་ན་ནི་ཇི་ལྟར་ན་ཚངས་པ་ཆེན་པོ་ལ་དམིགས་པའི་ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་མཆོག་ཏུ་འཛིན་པའི་ལྟ་བ་ལ་ཞེན་པ་དག་ཡིན། གཞན་དག་ན་རེ་སྲིད་པ་བར་མ་ལ་གནས་པ་དག་གིས་མཐོང་ངོ་ཞེས་ཟེར་རོ། །

[Block 2559]
དེ་ན་ཡང་བགེགས་བྱེད༌[^1341]པ་མེད་པའི་ཕྱིར་དུས་རིང་པོར་གནས་པ་མི་སྲིད་ན་ཇི་ལྟར་ན་དེ་དག་འདི་སྙམ་དུ་བདག་ཅག་གིས་སེམས་ཅན་འདི་ཚེ་རིང་ཞིང་དུས་རིང་པོར་གནས་པ་མཐོང་ངོ་སྙམ་དུ་ཤེས་པར་འགྱུར། དེ་ལྟ་བས་ན་དེ་ན་གནས་པ་དེ་དག་ཁོ་ནས་དེའི་སྔོན་གྱི་ཚུལ་རྗེས་སུ་དྲན་ཞིང་དེ་ལྟར་དུས་རིང་པོར་གནས་པ་མཐོང་ངོ་། །མཐོང་ནས་ཀྱང་ཕྱིས་དེ་དག་མཐོང་ངོ་སྙམ་དུ་ཤེས་པ་ཡིན་ནོ། །

[Block 2560 [HEADING]]
##### ལུས་གཅིག་ཅིང་འདུ་ཤེས་ཐ་དད་པ། ^3-1-3-3-0
--- END BLOCKS ---
