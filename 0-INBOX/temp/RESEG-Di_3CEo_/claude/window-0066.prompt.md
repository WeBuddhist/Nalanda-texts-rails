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
[Block 2311]
རེ་ཞིག་སེམས་པ་གཅིག་དང་ལྷན་ཅིག་འབྱུང་བ་ནི་བརྣབ་སེམས་ལ་སོགས་པ་མངོན་དུ་གྱུར་པའི་ཕྱིར་སེམས་པ་ཉོན་མོངས་པ་མ་ཡིན༌[^928]པ་དེའི་སྦྱོར་བས་གཟུགས་ཅན་རྣམས་ལས་གང་ཡང་རུང་བ་ཞིག་མཐར་ཕྱིན་པར་བྱེད་ནའོ། །

[Block 2312]
གཉིས་དང་ལྷན་ཅིག་འབྱུང་བ་ནི་གནོད་སེམས་སུ་གྱུར་པས་སྲོག་གཅོད་ནའོ། །

[Block 2313]
གསུམ་དང་ལྷན་ཅིག་འབྱུང་བ་ནི་གནོད་སེམས་སུ་གྱུར་པས་གཞན་གྱི་སྲོག་ཆགས་གསད་པས༌[^929]འཕྲོག་ནའོ། །

[Block 2314]
བཞི་དང་ལྷན་ཅིག་འབྱུང་བ་ནི་དབྱེན་བྱ་བའི་བསམ་པ་དང་ལྡན་པས་བརྫུན་གྱི་ཚིག་གམ་ཚིག་རྩུབ་པོ་སྨྲ་ན་སྟེ། དེ་ལ་ཡིད་ཀྱི་གཅིག་ཡིན་ངག་གི་གསུམ༌[^930]ཡིན་ནོ། །

[Block 2315]
ཡང་ན་བརྣབ་སེམས་ལ་སོགས་པར་གྱུར་པ་དེའི་སྦྱོར་བས་གཞན་གསུམ་མཐར་ཕྱིན་པར་བྱེད་ན་སྟེ། ལྔ་དང་དྲུག་དང་བདུན་དང་ཡང་དེ་བཞིན་དུ་སྦྱར་བར་བྱའོ། །

[Block 2316]
བརྒྱད་དང་ལྷན་ཅིག་འབྱུང་བ་ནི་དྲུག་ལ་སྦྱོར་བ་བྱས་ནས། འདོད་པས་ལོག་པར་གཡེམ་པ་བདག་ཉིད་ཀྱིས་བྱེད་ལ་མཉམ་དུ་མཐར་ཕྱིན་པར་གྱུར་ནའོ། །

[Block 2317]
རེ་ཞིག་མི་དགེ་བ་དང་ནི་དེ་ལྟ་བུ་ཡིན་ནོ། །

[Block 2318 [VERSE]]
དགེ་བ་བཅུ་ཡི་བར་དག་དང་། །
གཅིག་དང་བརྒྱད་དང་ལྔ་དང་མིན། །

[Block 2319]
དེ་ལ་གཉིས་དང་ལྷན་ཅིག་འབྱུང་བ་ནི་དགེ་བའི་རྣམ་པར་ཤེས་པ་ལྔ་ལ་གནས་པ་དང་ངོ་། །གསུམ་དང་ནི་ཡང་དག་པའི་ལྟ་བ་དང་མཚུངས་པར་ལྡན་པའི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་ནའོ། །

[Block 2320]
བཞི་དང་ནི་མི༌[^931]དགེ་བ་དང་ལུང་དུ་མ་བསྟན་པའི་སེམས་དང་ལྡན་པ་དགེ་བསྙེན་དང་དགེ་ཚུལ་གྱི་སྡོམ་པ་ཡང་དག་པར་ལེན་པ་ནའོ། །

[Block 2321]
དྲུག་དང་ནི་དགེ་བའི་རྣམ་པར་ཤེས་པ་ལྔ་ལ་གནས་པས་དེ་ཡང་དག་པར་ལེན་ནའོ། །

[Block 2322]
བདུན་དང་ནི་དགེ་བའི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་ཡོད་པས་དེ་ཁོ་ན་ཡང་དག་པར་ལེན་ནའོ། །

[Block 2323]
དགུ་དང་ནི་དགེ་བའི་རྣམ་པར་ཤེས་པ་ལྔ་ལ་གནས་པས་དགེ་སློང་གི༌[^932]སྡོམ་པ་ཡང་དག་པར་ལེན་ནའོ། །

[Block 2324]
བཅུ་དང་ནི་དགེ་བའི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ༌[^933]ལ་གནས་པས་དེ་ཁོ་ན་ཡང་དག་པར་ལེན་ནའོ། །

[Block 2325]
འགྲོ་བ་གང་ན་དགེ་བའམ་མི་དགེ་བའི་ལས་ཀྱི༌[^934]ལམ་དུ་ཞིག་མངོན་སུམ་དུ་གྱུར་པའམ་ལྡན་པའི་སྒོ་ནས་ཡོད་ཅེ་ན།

[Block 2326 [VERSE]]
དམྱལ་བ་ན༌[^935]ནི་ཀྱལ་པ༌[^936]དང་། །
ཚིག་རྩུབ་གནོད་སེམས་རྣམ་གཉིས་སོ། །

[Block 2327]
སྨྲེ་སྔགས་འདོན་པའི་ཕྱིར་ཚིག་ཀྱལ་པ་ཡིན་ནོ། །

[Block 2328]
ཕན་ཚུན་བརྒྱད་བཀག་བྱེད་པའི་ཕྱིར་ཚིག་རྩུབ་པོ་ཡིན་ནོ། །

[Block 2329]
གཅིག་ལ་གཅིག་སེམས་ཀྱི་རྒྱུད་རྩུབ་པོས་ཞེ་སྡང་བའི་ཕྱིར་གནོད་སེམས་ཡིན་ནོ། །

[Block 2330]
བརྣབ་སེམས་ལོག་ལྟ་ལྡན་པས་སོ། །

[Block 2331]
ཆགས་པར་བྱ་བའི་དངོས་པོ་མེད་པའི་ཕྱིར་དང་། ལས་ཀྱི་འབྲས་བུ་མངོན་སུམ་དུ་གྱུར་པའི་ཕྱིར་མངོན་སུམ་དུ་གྱུར་པ་ནི་མེད་དོ། །

[Block 2332]
ལས་ཀྱི་ལམ་གཞན་དག་ནི་གཉིས་ཀ་ཡང་མེད་དོ། །

[Block 2333]
སྒྲ་མི་སྙན་ན་གསུམ་ཡོད་དེ། ཡིད་ཀྱི་གསུམ་ནི་ལྡན་པའི་སྒོ་ནས་སྦྱར་གྱི་ང་ཡིར་འཛིན་པ་དང་། ཀུན་ནས་བརྣར་སེམས༌[^937]པའི་དངོས་པོ་མེད་པ་དང་། སྡིག་པ་ཅན་གྱི་བསམ་པ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2334]
དེ་ནི༌[^938]

[Block 2335]
བདུན་པ་དངོས་སུ་ཡང་། །དེ་ན་ཚིག་ཀྱལ་པ་ནི་མངོན་སུམ་དུ་གྱུར་པའི་སྒོ་ནས་ཀྱང་ཡོད་དེ། གཞན་དག་རྣམ་པ་གཉིས་ཀ་ཡང་མེད་དོ། །

[Block 2336]
འདོད་པ་གཞན་ན་མི་དགེ་བཅུ། །དམྱལ་བ་དང་། བྱང་གི་སྒྲ་མི་སྙན་དག་ལས་གཞན་པའི་འདོད་པའི་ཁམས་ན་ནི་མི་དགེ་བའི་ལས་ཀྱི་ལམ་བཅུ་རྣམ་པ་གཉིས་ཀ་ཡོད་དོ། །

[Block 2337]
མི་དགེ་བ་རྣམས་བཤད་ཟིན་ཏོ། །

[Block 2338 [VERSE]]
དགེ་བ་གསུམ་ནི་ཐམས་ཅད་ན། །
རྙེད་དང་མངོན་དུ་གྱུར་སྒོ་ནས། །

[Block 2339]
ཁམས་གསུམ་ཐམས་ཅད་ལ་ཡིད་ཀྱི་གསུམ་རྣམ་པ་གཉིས་ཀ་ཡང་ཡོད་དོ། །

[Block 2340]
གཟུགས་མེད་འདུ་ཤེས་མེད་སེམས་ཅན། །རྙེད་པས་བདུན་ཡོད། །གཟུགས་མེད་པ་དང་། འདུ་ཤེས་མེད་པའི་སེམས་ཅན་དག་ནི་ལུས་དང་ངག་གི་དགེ་བའི་ལས་ཀྱི་ལམ་བདུན་ལྡན༌[^939]པའི་སྒོ་ཁོ་ན་ནས་ཡོད་དོ། །

[Block 2341]
གཟུགས་མེད་པར་སྐྱེས་པའི་འཕགས་པ་རྣམས་ལ་ཟག་པ་མེད་པའི་སྡོམ་པ་འདས་པ་དང་མ་འོངས་པ་དང་ལྡན་པའི་ཕྱིར་དང་། འདུ་ཤེས་མེད་པའི་སེམས་ཅན་རྣམས་ཀྱང་བསམ་གཏན་གྱི་སྡོམ་པ་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 2342]
ལྷག་བྱས་ན།

[Block 2343 [VERSE]]
མངོན་དུ་གྱུར་པའི་སྒོ་ནས་ཀྱང་། །
དམྱལ་བཅས་སྒྲ་མི་སྙན་མ་གཏོགས། །

[Block 2344]
[^940]ལྷག་མར་བྱས་པའི་ཁམས་སམ་འགྲོ་བ་གཞན་གང་ཡིན་པ་དེ་ལ་དམྱལ་བ་དང་བྱང་གི་སྒྲ་མི་སྙན་པ་དག་མ་གཏོགས་པ་དགེ་བ་བདུན་པོ་དག་མངོན་དུ་གྱུར་པའི་སྒོ་ནས་ཀྱང་ཡོད་དོ། །

[Block 2345 [HEADING]]
##### ལས་ཀྱི་ལམ་གྱི་འབྲས་བུ། ^4-3-9-5-0

[Block 2346]
དགེ་བ་དང་མི་དགེ་བའི་ལས་ཀྱི་ལམ་བཅུ་པོ་འདི་དག་ནི།

[Block 2347 [VERSE]]
ཐམས་ཅད་བདག་པོ་རྒྱུ་མཐུན་དང་། །
རྣམ་སྨིན་འབྲས་བུ་འབྱིན་པར་འདོད། །

[Block 2348]
རེ་ཞིག་མི་དགེ་བ་ཐམས་ཅད་ཀྱི་རྣམ་པར་སྨིན་པའི་འབྲས་བུ་ནི་དམྱལ་བར་སྐྱེ་བའོ། །

[Block 2349]
མི་རྣམས་སུ་སྲོག་གཅོད་པའི་རྒྱུ་མཐུན་པའི་འབྲས་བུ་ནི་ཚེ་ཐུང་བའོ། །

[Block 2350]
མ་བྱིན་པར་ལེན་པ༌[^941]ནི་ལོངས་སྤྱོད་ཀྱིས་ཕོངས༌[^942]པའོ། །
--- END BLOCKS ---
