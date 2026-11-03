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
[Block 2626]
འདུན་པ་བཟློག་པའི་འོག་ཏུ་ནི་རྒྱུ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཤི་ན་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2627]
ཤི་བའམ་འགྲོ་བ་ལ་འཇིགས་པ་དང་བཅས་པའི་གནས་ལ་བསྒོ་བར་བྱ་བའམ། ངེས་པར་སྦྱར་ཏེ་གསད་པར༌[^1777]བྱ་བའམ། གཞན་ལ་དེའི་དོན་དུ་འདུས་པ༌[^1778]ཟློག་པར་བྱེད་པ་དེ་ལས་གཞན་ལ་འདའ་བར་བྱས་ནས༌[^1779]དེའི་ཚིག་མ་ཡིན་ནོ། །

[Block 2628]
སྦྱར་བར་བྱས་པའི་ཤི་བ་ལ་སྦྱོར་བར་བྱེད་པ་པོའི་རྒྱུ་མཚན་ཉིད་དུ་སྔར་འདུན་པ་ཟློག་པར་བྱེད་པར་གྱུར་པའི་ཤི་བ་ལ་དེ་ལས་ཕམ་པ་འདའ་བར་འགྱུར་རོ། །

[Block 2629]
ཕྱིས་དེས་སྐྱེ་བ་ཡིན་ཏེ། འདི་ལ་ནི་སྦྱོར་བ་ཙམ་ཉིད་ཡིན་ཏེ། དངོས་གཞིའི་ཕམ་པ་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2630]
དཀུ་མཉེས་པས་མ་དང་མངལ་ན་གནས་པ་གཉིས་ལས་མ་བསམས་པ་ཤོས་ན་སྦོམ་པོའོ་ཞེས་བྱ་བ་ནི༌[^1780]ཤི་ནའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2631]
ཤི་བའི་དོན་དུ་མངལ་དང་བཅས་པའི་ལྟོ་བ་མཉེས་པ་ལས་གང་གི་མངལ་དུ་ཤི་བ་ལ་མ་བསམས་པ་ཉིད་དེ། ཤི་བ་ལ་སྦོམ་པོའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2632]
བསམས་པ་ཤོས་ཤི་བ་ཕམ་པ་ཉིད་དེ། འདིར་ངེས་པ་འདི་ལ་འབྲེལ་པ་ཡིན་ཏེ། འདི་ལ་གསོད་པར་འགྱུར་ཞེས་བྱ་བའོ། །

[Block 2633]
དེ་ལྟར་ཡིད་ལ་འབྲེལ་བར་གྱུར་པ་ལ་ཡོངས་སུ་མ་སྤངས་པ་གང་ཡིན་པ་དེ་ལ་དེ་བས་ན་འདི་སྦོམ་པོའོ། །

[Block 2634]
འཆི་བའི་བདག་ཉིད་ཅན་གྱི་ཉེ་བར་གསོད་པའི་མཚན་མ་ཅན་གྱིས༌[^1781]མཉེས་པ་ཡང་ཆོ་ག་འདི་དང་སྦྱར་བ་ཤི་བའི་དོགས་པ་ཡོད་པར་གྱུར་པ་ལས་རྟོགས་པར་བྱའོ། །

[Block 2635]
གཞི་དེ་ལས་གསོད་པ་ལ་འཇུག་པ་དང་དུ་ལེན་ནའོ་ཞེས་བྱ་བ་ནི་སྦོམ་པོའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2636]
གཞི་བྱེད་པ་པོ་གང་ལ་སྦོམ་པོ་འདི་དེའི་རྒྱུ་མཚན་དུ་གཞན་ལ་གསོད་པའི༌[^1782]དོན་གྱིས༌[^1783]འཇུག་པ་གང་ཡིན་པ་དེ་གཞི་དེ་ལ་སྦོམ་པོའོ། །

[Block 2637]
འདིར་གཞུང་ནི་གཞན་ལས་ཚེ་དང་ལྡན་པ་ཉེ་སྡེའི་དབང་དུ་མཛད་ནས་གསུངས་པ། ཉེ་སྡེ༌[^1784]ཁྱོད་ཀྱིས་མངལ་ན་གནས་པ་རླུགས་པར་བྱས་སམ། བཙུན་པ་བདག་གིས་མངལ་ན་གནས་པ༌[^1785]རླུགས་པར་མ་བགྱིས་ཏེ། འོན་ཀྱང་བདག་གིས་དང་དུ་བླངས་སོ། །

[Block 2638]
བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དགེ་སློང་རྣམས་ཀྱིས་དེ་ལྟ་བུའི་གནས་པ༌[^1786]དང་དུ་བླང་བར་མི་བྱའོ། །

[Block 2639]
གལ་ཏེ་དང་དུ་ལེན་པར་བྱེད་ན་འགལ་ཚབས་ཅན་དུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2640]
དེའི་དོན་དུ་མདོ་འདི་བྱས་སོ། །

[Block 2641]
ཁྱོད་ཀྱི་མིང་གིས༌[^1787]འཆི་བའི་ཡོ་བྱད་སྦྱིན་ནོ་ཞེས་ཟེར་བ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་འདི་ལྟ་བུའི་ཚིག་འདི་ལ་ཡང་གཞི་བྱས་པ་ལ་སྦོམ་པོའོ། །

[Block 2642]
ཇི་སྐད་དུ་དགེ་སློང་མའི་རྣམ་པར་འབྱེད་པ་ལས་ཁྱོད་ཀྱི་མིང་གིས༌[^1788]ཕྱེ་མ་སྦྱིན་ནོ་ཞེས་བྱ་བ་བརྗོད་པ་ལ་དགེ་སློང་མས་གཞི་བྱས་ཏེ། ཇི་སྲིད་དུ་བདེན་པར་དགེ་སློང་མ་ཁྱོད་མངལ་རླུགས་པར་བྱས་པ་བདེན་ནམ། བཙུན་པ་བདག་གིས་མངལ་ན་གནས་པ་རླུགས་པར་མ་བགྱིས་ཏེ། འོན་ཀྱང་བདག་གིས་དང་དུ་བླངས་སོ། །

[Block 2643]
བཅོམ་ལྡན་འདས་ཀྱིས་དགེ་སློང་མ་རྣམས་ལ་བོས་ཏེ་བཀའ་སྩལ་པ། དགེ་སློང་མས་གནས་རྣམ་པ༌[^1789]དེ་ལྟ་བུ་དང་དུ་བླང་བར༌[^1790]བྱ་བ་མ༌[^1791]ཡིན་ཏེ། དང་དུ་ལེན་པར་བྱེད་ན་ཉེས་པ་སྦོམ་པོའི་ལྟུང་བ་འཕེལ་བར་འགྱུར་རོ་ཞེས་བྱ་བ་གསུངས་ཏེ། དེ་བས་ན་མདོ་འདི་བྱས་པ་ཡིན་ནོ། །

[Block 2644]
ཆོ་ག་འདི་ལ་འདི་སྦྱོར་ཅིག་ཅེས་བྱ་བ་འདི་ལྟ་བུའི་གཞི་བྱས་པའི་དབང་དུ་བྱས་ནས་འདི་གཉིས་ནི་སྦོམ་པོའི་ལྟུང་བ་ལ་བཏགས་པའོ། །

[Block 2645]
བདག་གི་ཕྱིར་ཉེས་པ་སྦོམ་པོའི་དགོངས་པ་ཉིད་འདི་དགེ་སློང་གི་རྣམ་པར་འབྱེད་པ་ལས་འགལ་ཚབས་དང་བཅས་པའི་ཚིག་ཅན་རང་གིས་འཇུག་པ་རབ་ཏུ་རིག་པ་ལ་གཞི་བྱེད་པ་འདི་ཡིན་གྱི༌[^1792]སྣང་བ་དང་བསླངས་པ་ལ༌[^1793]ནི་མ་ཡིན་ནོ། །

[Block 2646]
དེ་བས་ན་རྣམ་པར་སྦྱར་བ་ཉིད་ཀྱི་ཕྱིར་གོ་བར་བྱེད་པ་ཉིད་ཡོད་ཀྱང་མི་སྨྲ་བའི་ངོ་བོར་གཞི་བྱས་པ་ལ་འདིར་སྦོམ་པོར་རྣམ་པར་ཤེས་པ་སྟེ་ཕམ་པ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 2647]
གཞན་དུད་འགྲོ་མ་ཡིན་པ་དང་སྤྲུལ་པ་བསད་པ་ལས་ཡང་ངོ་ཞེས་བྱ་བ་ལ༌[^1794]ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲ་ནི་སྦོམ་པོའོ་ཞེས་བྱ་བའི་རྗེས་བསྙགས་པའི་ཕྱིར་རོ། །

[Block 2648]
མིའི་འགྲོ་བ་ལས་གཞན་པའི་སྤྲུལ་པ་དུད་འགྲོ་སྤངས་པ་ལ་ཡང་གསོད་པ་ལ་སྦོམ་པོའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2649]
འདི་ནི་དངོས་གཞིའི་ཆོ་ག་ལ་ལྟོས་པའོ། །

[Block 2650]
འདི་ལས་སྲོག་ཆགས་སུ་གྱུར་པ་མ་ཡིན་པའི་སྤྲུལ་པ་ལ་འདིར་བཀག་པའོ། །

[Block 2651]
འདིར་གཞུང་ནི་ཚེ་དང་ལྡན་པ་རྣམས་མི་མ་ཡིན་པ་ཤིན་ཏུ་ཆེན་པོ་བསད་ཀྱང་སྦོམ་པོར་ཟད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2652]
སྤྲུལ་པའི་ཕྱིར༌[^1795]གཞུང་ནི་གཏམ་གྱི་གཞི་ལས།

[Block 2653]
འགྲོ་བ་ཐམས་ཅད་དུ་མ་གཏོགས་པ་གང་ཡིན་པའོ། །

[Block 2654]
མྱ་ངན་ལས་འདས་པ་ཡང་མ་ཡིན། རྒྱལ་བའི་བསྟན་པ་ལ་མི་འཇུག་པ་ཡང་ཡིན་ནོ། །

[Block 2655]
ཡོངས་སུ་མྱ་ངན་ལས་འདས་པ་མ་ཡིན་ནོ། །

[Block 2656]
དེས་དེ་ལ་སྨྲས་པ། ཁྱོད་ནི་སྤྲུལ་པ་སྟེ་སྲོག་བཅད་ན་ལྟུང་བ་ཅིར་འགྱུར། བཀའ་སྩལ་པ། ཉེས་པ་སྦོམ་པོར་རོ། །

[Block 2657]
གཞན་ལས་ནི་རོ་ལངས་ཀྱི་བསམ་པས་སྤྲུལ་པ་གསོད་པར་བྱེད་ན་ཞེས་གསུངས་སོ། །

[Block 2658]
གཞན་དུ་ཡང་དེ་དང་འདྲ་བ་ཉིད་ཀྱི་ཕྱིར་འདི་རྣམ་པར་གཞག་གོ། །

[Block 2659]
དུད་འགྲོ་གསོད་པ་ལྟུང་བྱེད་འབའ་ཞིག་པར་བྱས་པ་ཉིད་ཀྱི་ཕྱིར་སྤོང་བའོ། །

[Block 2660]
འདིར་དུད་འགྲོ་འགྲོ་བ་པའི་སྤྲུལ་པ་ལ་མིར་འདུ་ཤེས་པས་འགྲོ་བ༌[^1796]གཞན་གྱི་ངོ་བོས་གནས་པ་ལ་གཞན་གྱི་འགྲོ་བ་པ་ཡང་མིའི་འགྲོ་བའི་ངོ་བོ་སྟེ། འདུ་ཤེས་ཀྱིས་འདི་རྣམ་པར་གནས་པའི་ཕྱིར་དོན་ཇི་ལྟ་བ་ཉིད་ལ་དངོས་གཞིའོ། །

[Block 2661]
དོན་ཇི་ལྟ་བ་ཉིད་མ་ཡིན་པ་ལ་ཉེ་བའི་དངོས་གཞིའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2662]
དེ་ལྟར་ལྟུང་བ་རྟོགས་པར་བྱའོ། །

[Block 2663]
དྲི་བར་བྱས་པ་ལ་མ་སྨྲས་པར་ནད་པ་ལ་སྨན་སྦྱིན་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་གསོ་བ་ལ་མཁས་པས་ཚངས་པ་མཚུངས་པར་སྤྱོད་པའི་ནད་གཡོག་བྱའོ་ཞེས་གསུངས་པའི་ཚིག་གིས་གསོ་བར་བྱ་བ་ལ་མཁས་པ་མ་ཡིན་པ་དེའི་ཕྱིར་འདི་བཏགས་པའོ། །

[Block 2664]
འདིར་སུ་ཞིག་ལ་མངོན་པར་དྲི་བར་འདོད་ན་གང་གིས་མ་སྨོས་པའི་སྨན་སྦྱིན་པར་མི་བྱ་ཞེ་ན། དེའི་ཕྱིར་སྨན་པ་དང་དེ་རབ་ཏུ་བྱུང་བ་དང་། བཀོལ་བ་རྣམས་ལ་དྲི་བར་བྱ་བ༌[^1797]ཉིད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་རབ་ཏུ་བྱུང་བ་ཞེས་བྱ་བ་ནི་སྨན་པ་རབ་ཏུ་བྱུང་བའོ། །

[Block 2665]
འདིར་བཀོལ་བ་ལ་ཡང་ངོ༌[^1798]ཞེས་བྱ་བའི་སྒྲ་བཀོལ་བ་ཞེས་བྱ་བ་ཡང་སྦྱར་རོ། །
--- END BLOCKS ---
