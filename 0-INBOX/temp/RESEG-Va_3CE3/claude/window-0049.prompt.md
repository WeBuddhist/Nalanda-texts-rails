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
[Block 1716]
གནས་བརྟན་རབ་འབྱོར་གྱིས་ཆོས་ཀྱི་ཚུལ་གྱི་རྣམ་པ་དེས་བསྟན་པ་ལྟར་ན་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་གནས་བརྟན་ཤཱ་རིའི་བུས་འདི་སྐད་སྨྲས་ཏེ། གལ་ཏེ་བྱང་ཆུབ་སེམས་དཔའ་ཕྱིར་ལྡོག་པ་མེད་ན། དེ་ལྟ་ན་ནི་བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་སངས་རྒྱས་སུ་འགྱུར་གྱི། ཕྱིར་ལོག་ནས་ཉན་ཐོས་དང་རང་སངས་རྒྱས་སུ་མི་འགྱུར་རོ། །

[Block 1717]
དེ་ལྟར་གྱུར་ན་བྱང་ཆུབ་སེམས་དཔའ་རྣམ་པ་གསུམ་མོ་ཞེས་བྱ་བ་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ལ་རྣམ་པ་གསུམ་དུ་འགྱུར་བ་མེད་དོ་ཞེས་དེ་སྙམ་དུ་བསམས་པ་དང་། གནས་བརྟན་གང་པོའི་ཚིག་གིས་རབ་འབྱོར་ལ་ཡང་དྲིས་པ་དང་། དེ་ནས་གནས་བརྟན་རབ་འབྱོར་གྱིས་བྱང་ཆུབ་སེམས་དཔའ་རྣམ་པ་གསུམ་ཞེས་བྱ༌[^1203]བའི་ཚིག་དེ་མ་བཟོད་ནས། ཚེ་དང་ལྡན་པ་ཤཱ་རིའི་བུས་ཁྱོད་དེ་བཞིན་ཉིད་ལ་བྱང་ཆུབ་སེམས་དཔའ་གསུམ་འདོད་དམ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། བྱིས་པ་སོ་སོའི་སྐྱེ་བོ་ཐམས་ཅད་དང་འཕགས་པའི་གང་ཟག་ཐམས་ཅད་དང་། རང་བྱང་ཆུབ་དང་། བྱང་ཆུབ་སེམས་དཔའ་དང་། སངས་རྒྱས་ཀྱང་དེ་བཞིན་ཉིད་ཀྱི་དབང་གིས་གཅིག་ཁོ་ནར་འགྱུར་ཏེ། དེ་དག་ལ་ཐ༌[^1204]དད་པ་མེད་དོ་ཞེས་སྔར་ཡང༌[^1205]བཤད་ཟིན་ཏོ། །

[Block 1718]
དེ་ལྟར་ཐམས་ཅད་གཅིག་ཏུ་ཟད་པ་ལ་བྱང་ཆུབ་སེམས་དཔའ་རྣམ་པ་གསུམ་དུ་འདོད་ན། དེ་བཞིན་ཉིད་རྣམ་པ་ཐམས་ཅད་དུ་ཐ་དད་པ་མེད་པ་ལ། གཅིག་གམ་གཉིས་སམ་གསུམ་ཞེས་ཐ་དད་དུ་དབྱེ་བ་ཇི་ལྟར་རིགས་པར༌[^1206]འགྱུར་ཞེས་བསྟན་པའོ། །

[Block 1719 [HEADING]]
##### ངེས་པར་འབྱུང་བ་བསྒྲུབ་པའི་མཚན་ཉིད། ^1-2-5-26-0

[Block 1720 [HEADING]]
###### བསམ་པ་ཕུན་སུམ་ཚོགས་པ། ^1-2-5-26-1-0

[Block 1721]
དེ་ནས་གནས་བརྟན་རབ་འབྱོར་ལ་བཅོམ་ལྡན་འདས་ཀྱིས་བྱང་ཆུབ་སེམས་དཔའ་འདི་ནི་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཏུ་ངེས་པར་འབྱུང་བར་རིག་པར་བྱའོ་ཞེས་གསུངས་པའི་སྐབས་ལས་ངེས་པར་འབྱུང་བ་བསྒྲུབ༌[^1207]པའི་མཚན་ཉིད་ཤེས་པར་འདོད་པའི་འཁོར་རྣམས་ཀྱི་དོན་དུ། བཅོམ་ལྡན་འདས་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཏུ་ངེས་པར་འབྱུང་བར་འཚལ་བའི་བྱང་ཆུབ་སེམས་དཔས་ཇི་ལྟར་གནས་པར་བགྱི་ཞེས་ཞུས་པ་དང་། དེའི་འོག་ཏུ་བསམ་པ་ཕུན་སུམ་ཚོགས་པ་དང་།[^1208] སྦྱོར་བ་ཕུན་སུམ་ཚོགས་པས་གནས་པར་བསྟན༌[^1209]པ། སེམས་ཅན་ཐམས་ཅད་ལ་སེམས་མཉམ་པ་ཉིད་དུ༌[^1210]བསྐྱེད་པར་བྱའོ༌[^1211]ཞེས་བྱ་བ་ནས་ཉེ་དུ་དང་སྣག་གི་གཉེན་མཚམས་ཀྱི་སེམས་ཀྱིས་དམིགས་པར་བྱའོ་ཞེས་བྱ་བའི་བར་དུ་ནི་བསམ་པ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 1722 [HEADING]]
###### སྦྱོར་བ་ཕུན་སུམ་ཚོགས་པ། ^1-2-5-26-2-0

[Block 1723]
བདག་གིས་ཀྱང་སྲོག་གཅོད་པ་སྤང་བར་བྱ་ཞེས་བྱ་བ་ནས་དམ་པའི་ཆོས་གནས་པ༌[^1212]མཐུན་པས་དགའ་བར་བྱའོ་ཞེས་བྱ་བའི་བར་དུ་ནི་སྦྱོར་བ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 1724 [HEADING]]
###### སྦྱོར་བའི་འབྲས་བུ། ^1-2-5-26-3-0

[Block 1725]
དེའི་འོག་ཏུ་སྦྱོར་བའི་འབྲས་བུ་རྣམ་པ་གཉིས་ཏེ། སྒྲིབ་པ་མེད་པ་དང་། ཡོངས་སུ་འཛིན་པ་མེད་པའོ། །

[Block 1726]
སེམས་ཅན་ཐམས་ཅད་ལ་མཉམ་པའི་སེམས་བསྐྱེད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ཆོས་ཐམས་ཅད་ཀྱི་དེ་བཞིན་ཉིད་ཀྱི་དབང་གིས་སོ། །

[Block 1727 [HEADING]]
###### **སྒྲིབ་པ་མེད་པ།** ^1-2-5-26-3-1-0

[Block 1728]
གཟུགས་སྒྲིབ་པ་མེད་པར་འགྱུར་རོ་ཞེས་བྱ་བ་ནི་གཟུགས་ལ་སྒྲིབ་པར་མི་རྟོག་གོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1729 [HEADING]]
###### **ཡོངས་སུ་འཛིན་པ་མེད་པ།** ^1-2-5-26-3-2-0

[Block 1730]
སྔོན་གྱི་མཐའ་ནས་ཀྱང་གཟུགས་ཡོངས་སུ་མ་བཟུང་ངོ་ཞེས་བྱ་བ་ནི་སྔོན་གྱི་དུས་ནས་ཀྱང་གཟུགས་ལ་ལོགས་པའི༌[^1213]སྒྲིབ་པར་འགྱུར་བ༌[^1214]ཡོངས་སུ་མི་གཟུང༌[^1215]ངོ་། །དེ་ལྟར་ཡོངས་སུ་མ་བཟུང་ངོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ལ། [^1216]ཇི་ལྟར་གཟུགས་ཡོངས་སུ་མ་བཟུང་བ་ཞེས་བྱ་བར་འགྱུར་ཞེ་ན་ཞེས་བྱ་བ་ནི་ཐེ་ཚོམ་ཟ་བ་རྣམས་ཀྱི་ཕྱིར་གསུངས་སོ། །

[Block 1731]
རབ་འབྱོར་འདི་ལྟར་གཟུགས་ཡོངས་སུ་གཟུང༌[^1217]དུ་མེད་པ་གང་ཡིན་པ་དེ་ནི་གཟུགས་མ་ཡིན་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའ་ཆོས་ཐམས་ཅད་ལ་ཡོངས་སུ་འཛིན་པ་མེད་པ་ཉིད་འཕེལ་བར་བྱེད་ཀྱི་ཡོངས་སུ་འཛིན་པ་ནི་མ་ཡིན་ནོ། །

[Block 1732]
བྱང་ཆུབ་སེམས་དཔའི་ཡོངས་སུ་མི་འཛིན་པ་དེ་ཡང་གཟུགས་ལ་སོགས་པའི་ངོ་བོ་ཉིད་མ་ཡིན་ནོ། །

[Block 1733]
དེ་བས་ན་ཡོངས་སུ་འཛིན་པ་མེད་པ་སྤེལ་ན་བྱང་ཆུབ་སེམས་དཔས་གཟུགས་ལ་སོགས་པ་ཡོངས་སུ་མ་བཟུང་བར་འགྱུར་རོ། །

[Block 1734 [HEADING]]
##### ཕྱིར་མི་ལྡོག་པའི་རྟགས། ^1-2-5-27-0

[Block 1735]
དེ་ནས་གནས་བརྟན་རབ་འབྱོར་གྱིས་སྔར་དོན་དམ་པར་ཕྱིར་ལྡོག་པ་ཡང་མེད་བྱང་ཆུབ་སེམས་དཔའ་རྣམ་པ་གསུམ་ཡང་མེད་དོ་ཞེས་སྨྲས་པའི་ཕྱིར་དེ་ནི༌[^1218]སྐབས་འདིར་ཕྱིར་མི་ལྡོག་པའི་རྟགས་རྣམས་ཞུས་པ་དང་། དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་ཕྱིར་མི་ལྡོག་པའི་རྟགས་རྣམ་པ་སུམ་ཅུ་རྩ་ལྔས་བསྟན་ཏེ། དེ་བཞིན་ཉིད་ལ་གཉིས་སུ་མེད་པར་མཐོང་བ་དང་། ཐམས་ཅད་ལས་ཕྱིར་ལྡོག་པ་དང་། སྟོན་པ་གཞན་ལ་རིམ་གྲོ་བྱེད་པ་ལ་སོགས་པ་ཆོས་ངན་པ་མེད་པ་དང་། མི་ཁོམ་པར༌[^1219]སྐྱེ་བ་མེད་པ༌[^1220]དང་། མི་དགེ་བའི་ལས་ཀྱི་ལམ་སྤངས་པ་དང་། དགེ་བའི་ལས་ཀྱི་ལམ་ཡོངས་སུ་རྫོགས་པར་བྱེད་པ་དང་། སེམས་ཅན་ཐམས་ཅད་ཀྱི་དོན་དུ་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཐམས་ཅད་ཡོངས་སུ་རྫོགས་པར་བྱེད་པ༌[^1221]དང་། [^1222]སེམས་ཅན་ཐམས་ཅད་ཀྱི་དོན་དུ་གསུང་རབ་ཡན་ལག་བཅུ་གཉིས་ཀྱི་ཆོས་ཀུན་ཆུབ་པར་བྱེད་པ་དང་། ཆོས་ཟབ་མོ་ལ་ནེམ་ནུར་མེད་པ་དང་། ལུས༌[^1223]ངག་དང་། ཡིད་ཀྱི་ལས་འཇམ་ཞིང་བྱམས་པར་ལྡན་པ་དང་། སྒྲིབ་པ་རྣམ་པ་ལྔ་དང་དུ་མི་ལེན་པ་དང་། བག་ལ་ཉལ་བ༌[^1224]རྣམ་པ་བདུན་མེད་པ་དང་། དྲན་པ་དང་ཤེས་བཞིན་དུ་ལྡན་པའི་སྤྱོད་ལམ་ཅན་དང་། གཙང་སྦྲར་སྤྱོད་པ༌[^1225]ལ་སོགས་པ་དང་ལྡན་པ་དང་། ལུས་ལ་སྲིན་བུའི་རིགས་སྟོང་མི་འབྱུང་བ་དང་། ལུས་དང་ངག་དང༌[^1226]སེམས་ཡོངས་སུ་དག་པ་དང་། འདོད་པ་ཆུང་ལ་ཆོག་ཤེས་ཤིང་སྦྱངས་པའི་ཡོན་ཏན་ལ་བརྟེན་པ་དང་། སེར་སྣ་ལ་སོགས་པ་མེད་པ་དང་། བློ་བརྟན་ཞིང་ཟབ་པ་ལ་སོགས་པ་དང་ལྡན་པ་དང་། བདུད་ལ་སོགས་པས་མི་འཕྲོགས་པ་དང་། དྲིང་མི་འཇོག་པ་དང་། ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་བརྟེན་པ་དང་། བདུད་ཀྱི་ལས་རྟོགས་པ་དང་། མི་སྐྱེ་བའི་ཆོས་ལ་བཟོད་པ་ཐོབ་པ་དང་། ཕྱིར་ལྡོག་པ་དང་ཕྱིར་མི་ལྡོག་པ་དང་། བསམ་གཏན་དང་ཏིང་ངེ་འཛིན་དང་སྙོམས་པར་འཇུག་པའི་འབྲས་བུ་ལ་མི་རེག་པ༌[^1227]དང་། གཟུགས་ལ་སོགས་པའི་ཆོས་ཐམས་ཅད་ལྷུར་མི་ལེན་པ་དང་། ཕ་རོལ་ཏུ་ཕྱིན་པ་རྣམས་ལ་སྦྱོར་བ་རྣམ་པ་བཞི་ཕུན་སུམ་ཚོགས་པ་དང་། སྦྱིན་པའི་འབྲས་བུ་གཞན་མི་དགའ་བར་འགྱུར་བ་ལ་སོགས་པ་ལ་མི་རེ་བ་དང་། རྡོ་རྗེའི་རིགས་ལྔ་ཕྱི་བཞིན་འབྲང་བ་ལ་སོགས་པའི་དབང་དང་། སྔགས་དང་བཟོ་ངན་པ་ལ་མི་བརྟེན་པ་དང་། གཏམ་ངན་པའི་སྦྱོར་བ་ལས་ལྡོག་ཅིང་ཡང་དག་པའི་ལས་དང་བསམ་པ་ལ་འཇུག་པ་དང་། རང་གི་ས་ལ་ཐེ་ཚོམ་མེད་པ་དང་། ཆོས་ཡོངས་སུ་བཟུང་བའི་ཕྱིར་སྲོག་ཀྱང་ཡོངས་སུ་གཏོང་བ་དང་། ཆོས་བཟུང་བ་རྣམས་ཆུད་མི་གསོན་པའི་ཕྱིར་རོ། །

[Block 1736]
དེ་ལ་དེ་བཞིན་ཉིད་གང་ཡིན་པ་དེ་དག་ནི་རེ་རེ་དང་གཉིས་ཀ་མ་ཡིན་པར་ཐེ་ཚོམ་ཟ་བ་གང་ཡང་མེད་དོ་ཞེས་བྱ་བས་ནི་གང་ཟག་ཐམས་ཅད་ཀྱི་དེ་བཞིན་ཉིད་ཀྱི་དབང་གིས༌[^1228]དེ་བཞིན་གཤེགས་པ་གཅིག་པ་ཉིད་དུ་སྟོན་ཏེ། །ངོ་བོ་ཉིད་དམ་གཉི་གའི་ངོ་བོ་ཉིད་གང་ཡིན་པ་དེ་ནི་དེ་བཞིན་ཉིད་ཀྱི་ངོ་བོ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1737]
ཆོས་ཐམས་ཅད་ནི་རྣམ་པ་མེད་པ་མཚན་མ་མེད་པ་རྟགས་མེད་པ་ཞེས་བྱ་བ་ནི་དེ་བཞིན་ཉིད་ལ་རྣམ་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 1738]
བཅོམ་ལྡན་འདས༌[^1229]གལ་ཏེ་ཆོས་ཐམས་ཅད་རྣམ་པ་མ་མཆིས་པ་ལགས་ན༌[^1230]ཞེས་བྱ་བ་ལ་སོགས་པས་འདི་སྐད་སྟོན་ཏེ། གལ་ཏེ་རྣམ་པ་མེད་ཅིང་མཚན་མ་མེད་ན། ཇི་ལྟར་ཕྱིར་མི་ལྡོག་པའི་རྣམ་པ་དང་མཚན་མ་བཤད་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1739]
རབ་འབྱོར་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་གང་གཟུགས་ལས་ཕྱིར་ལྡོག༌[^1231]པ་ཞེས་བྱ་བ་ལ་སོགས་པས་རྣམ་པ་མེད་པར་ཤེས་པ་ཉིད་རྟགས་ཡིན་ནོ་ཞེས་སྟོན་ཏེ། གཟུགས་ཀྱི་རྣམ་པ་དང་། གཟུགས་ཀྱི་རྟགས་ལས་ཕྱིར་ལྡོག་པ་ཞེས་བྱའོ། །ཤེས་པར་བྱ་བ་ཤེས་པའོ་ཞེས་བྱ་བ་ནི་ཤེས་བྱ་ཤེས་པའོ། །

[Block 1740]
བལྟ་བར་བྱ་བ་མཐོང་བའོ་ཞེས་བྱ་བ་ནི་ལྟ་བ་མཐོང་བའོ། །

[Block 1741]
ངོ་མཚར་དང་བཀྲ་ཤིས་ཀྱིས་དག་པར་མི་འཛིན་ཞེས་བྱ་བ་ལ་བཀྲ་ཤིས་དང་ངོ་མཚར་གྱི་བཀྲ་ཤིས་ནི་བསམས་པ་ཙམ་གྱིས་བྱས་པ་སྟེ། ཁྲུས་དང་སྨྱུང་བར་འདུག་པ་དང་མངོན་པར་འཇུག་པ་དང་མུ་སྟེགས་དང་། མཆོད་སྦྱིན་ལ་སོགས་པས་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1742]
ཕྱིར་མི་ལྡོག་པའི་མཚན་མ་ཐམས་ཅད་ནི་བརྡ་ཕྲད་སླའོ། །

[Block 1743]
ས་དང་པོ་ཐོབ་པ་ཉིད་ཀྱིས་ཕྱིར་མི་ལྡོག་པར་འགྱུར་མོད་ཀྱི་འོན་ཀྱང་ས་བརྒྱད་པ་ལ་ཕྱིར༌[^1232]ལྡོག་པར་འགྱུར་བ་གཉིས་པ་ཡང་བསྟན་ཏོ། །

[Block 1744]
ཕྱིར་ལྡོག་པ་དང་ཕྱིར་མི་ལྡོག་པ་ཞེས་བྱ་བ་ལ་ཉན་ཐོས་དང་རང་སངས་རྒྱས་ཀྱི་ས་ལས་ཕྱིར་ལྡོག་པས་ཕྱིར་ལྡོག་པའོ། །

[Block 1745]
སངས་རྒྱས་ཀྱི་ས་ལས་ཕྱིར་མི་ལྡོག་པས་ཕྱིར་མི་ལྡོག་པ་ཞེས་བྱའོ། །

[Block 1746]
དེ་ལྟར་ཕྱིར་མི་ལྡོག་པའི་ཡོན་ཏན་རྣམས་ཐོས་ནས་ཕྱིར་མི་ལྡོག་པར་འདོད་པའི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་དོན་དུ་གནས་བརྟན་རབ་འབྱོར་གྱིས་ཟབ་ཅིང་ཟབ་པའི་གནས་རྣམས་ཞུས་པ། བཅོམ་ལྡན་འདས་གནས་ཟབ་མོ་རྣམས་ལེགས་པར་བསྟན་དུ་གསོལ་ཞེས་བྱའོ། །

[Block 1747 [HEADING]]
#### ཞུ་བ་ཉིས་བརྒྱ་བདུན་ཅུ་རྩ་བདུན་གྱིས་ཟབ་མོའི་གནས་ཞུས་པ། ^1-2-6-0

[Block 1748 [HEADING]]
##### ཞུ་བ་བརྒྱ་ཕྲག་དང་པོ། ^1-2-6-1-0

[Block 1749]
འདི་མན་ཆད་ནི་གནས་བརྟན་རབ་འབྱོར་གྱིས་ཞུ་བ༌[^1233]ཉིས་བརྒྱ་བདུན་ཅུ་རྩ་བདུན་གྱིས་ཟབ་མོའི་གནས་ཞུས་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་ལན་གླན་པ༌[^1234]འབྱུང་སྟེ། དེ་ལ་བཅོམ་ལྡན་འདས་གནས་ཟབ་མོ་ཟབ་མོ་རྣམས་ལེགས་པར་བསྟན་དུ་གསོལ་ཞེས་བྱ་བ་ནི་ཞུས་པ་དང་པོའོ། །

[Block 1750]
བཅོམ་ལྡན་འདས་ཅི་ལགས་དེ་མྱ་ངན་ལས་འདས་པའི་ཚིག་བླ་དགས་སུ་བས་ཀྱི། ཆོས་ཐམས་ཅད་ཀྱི་ཚིག་བླ་དགས་མ་ལགས་སམ་ཞེས་བྱ་བ་ནི་གཉིས་པའོ། །

[Block 1751]
བཅོམ་ལྡན་འདས་གཟུགས་ཀྱི་དེ་བཞིན་ཉིད་ནི་ཇི་ལྟ་བུ་ལགས་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་གསུམ་པའོ། །

[Block 1752]
བཅོམ་ལྡན་འདས་ཅི་ལགས་མངོན་པར་འདུ་བགྱིད་པ་ཐམས་ཅད་ནི་ཀུན་བརྟགས་པའོ་ཞེས་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་བཞི་པའོ། །

[Block 1753]
བཅོམ་ལྡན་འདས་གྲངས་མ་མཆིས་པ་དང་དཔག་ཏུ་མ་མཆིས་པ་དང་ཚད་མ་མཆིས་པ་ལ་བྱེ་བྲག་ནི་ཅི་ཞིག༌[^1235]མཆིས་ཞེས་བྱ་བ་ནི་ལྔ་པའོ། །

[Block 1754]
བཅོམ་ལྡན་འདས་རྣམ་གྲངས་གང་གིས་གཟུགས་ཀྱང་གྲངས་མ་མཆིས་པར་འགྱུར་བ་དེ་ལྟ་བུ་མཆིས་སམ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་དྲུག་པའོ། །

[Block 1755]
བཅོམ་ལྡན་འདས་ཅི་ལགས་གཟུགས་འབའ་ཞིག་སྟོང་དུ་བས་ཀྱི་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་བདུན་པའོ། །
--- END BLOCKS ---
