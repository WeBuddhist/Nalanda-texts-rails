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
[Block 1191]
ཡང་སྦྱིན་པ་དེ་ནི།

[Block 1192 [VERSE]]
བདག་གཞན་དོན་ཕྱིར་གཉིས་དོན་ཕྱིར། །
གཉི་གའི་དོན་དུ་མིན་ཕྱིར་སྦྱིན། །

[Block 1193]
དེ་ལ་འདོད་ཆགས་དང་མ་བྲལ་བའམ། སོ་སོའི་སྐྱེ་བོ་འདོད་ཆགས་དང་མ༌[^860]བྲལ་བས་མཆོད་རྟེན་ལ་སྦྱིན་པ་སྦྱིན༌[^861]པར་བྱེད་པ་གང་ཡིན་པ༌[^862]དེས་ཕ་རོལ་པོ་དག་ལ་ཕན་འདོགས་པ་མེད་པའི་ཕྱིར་དེའི་བདག་ཉིད་ཁོ་ནའི་དོན་གྱི་ཕྱིར་སྦྱིན་པ་ཡིན་ནོ། །

[Block 1194]
འཕགས་པ་འདོད་ཆགས་དང་བྲལ་བས་སེམས་ཅན་ཕ་རོལ་པོ་དག་ལ་སྦྱིན་པར་བྱེད་པའི་སྦྱིན་པ་གང་ཡིན་པ༌[^863]དེ་ནི་མཐོང་བའི་ཆོས་ལ་མྱོང་བར་འགྱུར་བ་མ་གཏོགས་པར་དེས་དེ་དག་ལ་ཕན་བཏགས་པའི་ཕྱིར་གཞན་གྱི་དོན་གྱི་ཕྱིར་ཡིན་གྱི་བདག་གི་དོན་གྱི་ཕྱིར་ནི་མ་ཡིན་ཏེ། དེའི་རྣམ་པར་སྨིན་པའི་ས་ལས་ཤིན་ཏུ་ཡང་དག་པར་འདས་པའི་ཕྱིར་རོ། །

[Block 1195]
འདོད་ཆགས་དང་མ་བྲལ་བའམ། སོ་སོའི་སྐྱེ་བོའི་འདོད་ཆགས་དང་བྲལ་བས་སེམས་ཅན༌[^864]ཕ་རོལ་པོ༌[^865]དག་ལ་སྦྱིན་པར་བྱེད་པའི་སྦྱིན་པ་གང་ཡིན་པ་དེ་ནི་གཉི་གའི་དོན་གྱི་ཕྱིར་ཡིན་ནོ། །

[Block 1196]
འཕགས་པ་འདོད་ཆགས་དང་བྲལ་བས་མཆོད་རྟེན་ལ་འབུལ་བར་བྱེད་པའི་སྦྱིན་པ་གང་ཡིན་པ་དེ་ནི་མཐོང་བའི་ཆོས་ལ་མྱོང་བར་འགྱུར་བ་མ་གཏོགས་པར་གཉི་གའི་དོན་གྱི་ཕྱིར་ཡང་མ་ཡིན་ཏེ་དེ་ནི་བཀུར་སྟི་དང་། བྱས་པ་གཟོ་བ་འབའ་ཞིག་གིས༌[^866]འབུལ་བར་ཟད་དོ། །

[Block 1197 [HEADING]]
##### སྦྱིན་པའི་ཁྱད་པར། ^1-71-1-4-0

[Block 1198]
སྦྱིན་པའི་འབྲས་བུ་ལོངས་སྤྱོད་ཆེན་པོ་ཅན་ཞེས་སྤྱིར་བསྟན་པ།

[Block 1199 [VERSE]]
དེའི་ཁྱད་པར་སྦྱིན་བདག་དང་། །
དངོས་དང་ཞིང་གི་ཁྱད་པར་ལས། །

[Block 1200 [HEADING]]
###### སྦྱིན་བདག་ཁྱད་པར་དུ་འཕགས་པ། ^1-71-1-4-1-0

[Block 1201]
དེ་ལ་རེ་ཞིག །སྦྱིན་བདག་ཁྱད་འཕགས་དད་སོགས་ཀྱིས། །དད་པ་དང་ཚུལ་ཁྲིམས་དང་ཐོས་པ་ལ་སོགས་པའི་ཡོན་ཏན་དང་ལྡན་པའི་སྦྱིན་བདག་ནི་ཁྱད་པར་དུ་འཕགས་པ་ཡིན་ནོ། །

[Block 1202]
སྦྱིན་བདག་དེའི་སྦྱིན་པ་དེ་ནི་སྦྱིན་བདག་གི་ཁྱད་པར་གྱིས་འབྲས་བུ་འབྱིན་པ་ལ་ཁྱད་པར་དུ་འཕགས་པར་འགྱུར་ཏེ། སྦྱིན་བདག་དེ་ལྟ་བུ་དེ་ནི། གུས་པ་ལ་སོགས་པས་སྦྱིན་པར་བྱེད། གུས་པ་དང་། རང་གི་ལག་དང་། དུས་སུ་དང་། གཞན་ལ་མི་གནོད་པར་སྦྱིན་པར་བྱེད་དེ།

[Block 1203 [VERSE]]
དེ༌[^867]ཕྱིར་བཀུར་སྟི་རྒྱ་ཆེན་དང་། །
དུས་དང་བར་ཆད་མེད་པར་རྙེད། །

[Block 1204]
དེའི་ཕྱིར་སྦྱིན་བདག་འདིའི་སྦྱིན་པ་དེ་ལྟ་བུར་བྱིན་པས་གོ་རིམས་བཞིན་དུ་ཁྱད་པར་བཞིར་འགྱུར་ཏེ། བཀུར་སྟི་རྙེད་པར་འགྱུར། ལོངས་སྤྱོད་རྒྱ་ཆེན་པོ་ལ་དད་པ་རྙེད་པར་འགྱུར། ལོངས་སྤྱོད་དུས་ལས༌[^868]མི་ཡོལ་བར་དུས་སུ་རྙེད་པར་འགྱུར། ལོངས་སྤྱོད་བར་ཆད་མེད་པར་འགྱུར་ཏེ། འདིའི་ལོངས་སྤྱོད་གཞན་དག་གིས་བར་དུ་མི་ཆོད་ཅིང་། མེ་ལ་སོགས་པས་མེད་པར་མི་འགྱུར་རོ། །

[Block 1205]
ཇི་ལྟར་ན་སྦྱིན་བདག་ཁྱད་པར་དུ་འཕགས་པ་ཡིན་པ་དང་། དེའི་ཁྱད་པར་གྱིས་སྦྱིན་པའི་ཁྱད་པར་ཡང་བཤད་ཟིན་ཏོ། །

[Block 1206 [HEADING]]
###### དངོས་པོ་ཁྱད་པར་དུ་འཕགས་པ། ^1-71-1-4-2-0

[Block 1207]
ཇི་ལྟར་ན་དངོས་པོ་ཁྱད་པར་དུ་འཕགས་པ་ཡིན་ཞེ་ན། ཁ་དོག་ལ་སོགས་ཕུན་སུམ་དངོས། །ཁྱད་པར་དུ་འཕགས་པ༌[^869]ཞེས་བྱ་བར་སྦྱར་ཏེ། གལ་ཏེ་གང་སྦྱིན་པར་བྱ་བ་དེ་ཁ་དོག་དང་དྲི་དང་རོ་དང་རེག་བྱ༌[^870]རྣམས་ལས་གང་ཡང་རུང་བ་ཞིག་གིས༌[^871]ཕུན་སུམ་ཚོགས་པ༌[^872]ཡིན་ན། དེ་ལྟ་བུ་ནི་དངོས་པོ་ཁྱད་པར་དུ་འཕགས་པ་ཡིན་ནོ། །

[Block 1208]
དངོས་པོ་དེ་ལྟ་བུ་བྱིན་པས་ཅི་ལྟར༌[^873]འགྱུར་ཞེ་ན། རིམ་པ་བཞིན་དུ།

[Block 1209 [VERSE]]
དེ་ལས་གཟུགས་བཟང་གྲགས་ལྡན་དང་། །
དགའ་དང་ཤིན་ཏུ་གཞོན་ཤ་ཅན། །
དུས་སུ་རེག་ན་བདེ་ལུས་འགྱུར། །

[Block 1210]
རེག་བྱ༌[^874]ཕུན་སུམ་ཚོགས་པ་བྱིན་པས་ནི་གཟུགས་བཟང་པོར་འགྱུར་རོ། །

[Block 1211]
དྲི་ཕུན་སུམ་ཚོགས་པ་བྱིན་པས་ནི་དྲི་བཞིན་དུ་གྲགས་པས་ཕྱོགས་སུ་རྒྱས་པར་འགྱུར་རོ། །

[Block 1212]
རོ་ཕུན་སུམ་ཚོགས་པ་བྱིན་པས་ནི་རོ་ཞིམ་པོ་བཞིན་དུ་དགའ་བར་འགྱུར་རོ། །

[Block 1213]
རེག་བྱ་ཕུན་སུམ་ཚོགས་པ་བྱིན་པས་ནི་ལུས་ཤིན་ཏུ་གཞོན་ཤ་ཅན་དང་། བུད་མེད་རིན་པོ་ཆེ་ཇི་ལྟ་བ་བཞིན་དུ་འདིའི་དུས་སུ་རེག་ན་བདེ་བའི་ལུས་སུ་འགྱུར་རོ། །

[Block 1214 [HEADING]]
###### ཞིང་ཁྱད་དུ་འཕགས་པ། ^1-71-1-4-3-0

[Block 1215]
ཡང༌[^875]ཇི་ལྟར་ན་ཞིང་ཁྱད༌[^876]དུ་འཕགས་པ་ཡིན་ཞེ་ན།

[Block 1216 [VERSE]]
འགྲོ་དང་སྡུག་བསྔལ་ཕན་འདོགས་དང་། །
ཡོན་ཏན་རྣམས་ཀྱིས་ཞིང་ཁྱད་འཕགས། །

[Block 1217 [HEADING]]
###### **འགྲོ་བའི་ཁྱད་པར།** ^1-71-1-4-3-1-0

[Block 1218]
རེ་ཞིག་འགྲོ་བའི་ཁྱད་པར་གྱིས་ཁྱད་དུ་འཕགས་པ་འདི་ལྟར་བཅོམ་ལྡན་འདས་ཀྱིས་དུད་འགྲོའི་སྐྱེ་གནས་སུ་སོང་བ་ལ་སྦྱིན་པ་བྱིན་ན་སླར་རྣམ་པར་སྨིན་པ་བརྒྱ་འགྱུར་དུ་རེ་བར་བྱའོ། །

[Block 1219]
ཚུལ་ཁྲིམས་འཆལ་བར་གྱུར་པའི་མི་ལ་སྦྱིན་པ་བྱིན་ན་སྟོང་འགྱུར་དུ་རེ་བར་བྱའོ་ཞེས་གསུངས་པ་ལྟ་བུའོ། །

[Block 1220 [HEADING]]
###### **སྡུག་བསྔལ་གྱི་ཁྱད་པར།** ^1-71-1-4-3-2-0

[Block 1221]
སྡུག་བསྔལ་གྱི་ཁྱད་པར་དུ་འཕགས་པ་ནི་འདི༌[^877]ལྟར་རྫས་ལས་བྱུང་བའི་བསོད་ནམས་བྱ་བའི༌[^878]དངོས་པོ༌[^879]དག་ཏུ་ནད་པ་ལ་སྦྱིན་པ་དང་། ནད་གཡོག༌[^880]ལ་སྦྱིན་པ་དང་། གྲང་བ་ལ་སོགས་པ་ལ༌[^881]སྦྱིན་པར༌[^882]གསུངས་ནས། རྫས་ལས་བྱུང་བའི་བསོད་ནམས་བྱ་བའི་དངོས་པོ་འདི་བདུན་དང་ལྡན་པའི་དད་པའི་རིགས་ཀྱི་བུའམ། རིགས་ཀྱི་བུ་མོའི་བསོད་ནམས་ཀྱི་ཚད་གཟུང་བར་མི་ནུས་སོ་ཞེས་གསུངས་པ་ལྟ་བུའོ། །

[Block 1222 [HEADING]]
###### **ཕན་འདོགས་པའི་ཁྱད་པར།** ^1-71-1-4-3-3-0

[Block 1223]
ཕན་འདོགས་པའི་ཁྱད་པར་ལས་ནི་འདི་ལྟ་སྟེ་ཕ་མ་དང་། ཕན་འདོགས་པ་གཞན་རྣམས་ལ་སྦྱིན་པ་བྱིན་པ་སྟེ། དོམ་དང་རི་དགས་ལ་སོགས་པའི་སྐྱེས་པའི་རབས་དཔེར་བྱའོ། །

[Block 1224 [HEADING]]
###### **ཡོན་ཏན་གྱི་ཁྱད་པར།** ^1-71-1-4-3-4-0

[Block 1225]
ཡོན་ཏན་གྱི་ཁྱད་པར་ལས་ནི་འདི་ལྟ་སྟེ། ཚུལ་ཁྲིམས་དང་ལྡན་པ་ལ༌[^883]བྱིན་ན་རྣམ་པར་སྨིན་པ་འབུམ་འགྱུར་ཞེས་བྱ་བ་དེ་ལྟ་བུ་ལ་སོགས་པའོ། །

[Block 1226 [HEADING]]
##### སྦྱིན་པ་ཐམས་ཅད་ཀྱི་ནང་ན་མཆོག། ^1-71-1-5-0

[Block 1227 [VERSE]]
སྦྱིན་པ་ཐམས་ཅད་ཀྱི་ནང་ན། །
མཆོག་ནི་གྲོལ་བས་གྲོལ་བ་ལའང་། །

[Block 1228]
འདོད་ཆགས་དང་བྲལ་བས་འདོད་ཆགས་དང་བྲལ་བ་ལ་བྱིན་པའི་སྦྱིན་པ་གང་ཡིན་པ་དེ་ནི་བཅོམ་ལྡན་འདས་ཀྱིས་ཟང་ཟིང་གི་སྦྱིན་པ་རྣམས་ཀྱི་ནང་ནས་མཆོག་ཡིན་ནོ་ཞེས་གསུངས་སོ། །

[Block 1229]
བྱང་ཆུབ་སེམས་དཔའ་ཡིས། ཡང་ན་བྱང་ཆུབ་སེམས་དཔས༌[^884]སེམས་ཅན་ཐམས་ཅད་ལ་ཕན་པར་བྱ་བའི་ཕྱིར་སྦྱིན་པ་སྦྱིན་པར་བྱེད་པའི་སྦྱིན༌[^885]པ་གང་ཡིན་པ་དེ་ནི་གྲོལ་བ་མ་ཡིན་པས་མ་གྲོལ་བ་རྣམས་ལ་ཡང་བྱིན་ན༌[^886]མཆོག་ཡིན་ནོ། །

[Block 1230]
དེ་མ་གཏོགས་པ་བཅོམ་ལྡན་འདས་ཀྱིས༌[^887]གང་དག་སྦྱིན་པ་བརྒྱད་གསུངས་པ་དེ་དག་གི་ནང་ན་ནི་བརྒྱད་པ་མཆོག་ཡིན་ནོ་ཞེས་བྱ་བར་སྦྱར་རོ། །
--- END BLOCKS ---
