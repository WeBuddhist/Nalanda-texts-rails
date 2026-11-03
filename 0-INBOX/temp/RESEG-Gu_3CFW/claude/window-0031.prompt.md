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
[Block 1086]
དགེ་སློང་དག་མང་ལ་ཟས་ཉུང་གི༌[^922]ཇི་ལྟར་ཁྱེད་པར་བྲིམས་ཤིག་ཅེས་བསྒོ་བར་བྱའོ། །

[Block 1087]
འོན་ཏེ་དགེ་སློང་དག་ཉུང་ལ་ཟས་དག་མང་བ་ཡིན་ནོ་ཞེས་བྱ་བ་བརྗོད་ཅིང་ཅི་འབྱོར་པ་བྲིམས་ཤིག་ཅེས་བསྒོ་བར་བྱའོ། །

[Block 1088]
ཟས་ཉུང་བ་ཉིད་དུ་ངེས་པ་ལས་ཟས་ཉུང་བ་ཉིད་དམ་མང་བ་ཉིད་མ་ཡིན་ན་དེའི་ཚེ་སྔ་མ་བརྗོད་ཅིང་དེའི་འཁོར་གྱི་རྫས་མང་བ་ཉིད་དམ་ཉུང་བ་ཉིད་ནའོ། །

[Block 1089]
དེའི་དོན་ནི་འདི་ཡིན་ཏེ། འཁོར་གྱི་རྫས་མང་བ་ཉིད་དང་ཟས་ཉུང་བ་ཉིད་ཡིན་ན་དེའི་ཚེ་སྔ་མ་བརྗོད་པ་ནི་བྲིམས་ཤིག་ཅེས་བྱ་བ་བསྒོ་བའོ། །

[Block 1090]
ཟས་འགོད་པར་བྱེད་པ་པོ་ཉེ་བར་འགོད་པས་དང་པོར་དགེ་འདུན་གྱི་གནས་བརྟན་པར་གསོལ་བར་བྱའོ། །

[Block 1091]
གཞན་ཉིད་ཡིན་ན་ཅི་འབྱོར་པ་ཞེས་སོ་ཞེས་བྱ་བ་ནི་འཁོར་གྱི་རྫས་རྣམས་ནི་ཉུང་ལ་ཟས་ནི་མང་བ་ཉིད་ཡིན་པར་གྱུར་ན་འཁོར་ལ་བལྟས་ཏེ། དེའི་ཚེ་སྔ་མ་བརྗོད་ཅིང་ཇི་ལྟར་ཁྱེད་པར་བྲིམས་ཤིག་ཅེས་བསྒོ་བར་བྱའོ་ཞེས་བྱ་བ་ཟས་ཉེ་བར་གཞག་པ་ན་དང་པོར་སྦྱིན་པའི་ཕྱིར་དགེ་འདུན་གྱི་གནས་བརྟན་གྱིས་བསྒོ་བར་བྱའོ། །

[Block 1092]
རྒན་པའི་མཐར་སཾ་སྲ་བ༌[^923]ཏ་ཞེས་མ་བརྗོད་པར་དང་པོར་བླང་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་དང་པོར་ཞེས་བྱ་བའི་སྒྲས་ནི་དགེ་འདུན་གྱི༌[^924]གནས་བརྟན་གྱི་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1093]
ཟས་བསྡོགས་པ༌[^925]ན་བསྐོས་པ་དག་ལས་གཞན་པ་དག་ལྷགས་ན་དེ་ལ་སྦྲན་པར༌[^926]བྱའོ་ཞེས་བྱ་བ་ནི་གཞན་པའི་མ་བསྐོས་པ་དག་ལྷགས་ནས༌[^927]སྦྱིན་བདག་དེ་ལ་སྦྲན་པར་བྱའོ། །

[Block 1094]
དགེ་སློང་ཆོས་གོས་གསུམ་སྦྱིན་དུ་གཞུག་པར་མི་བྱའོ། །

[Block 1095]
དགེ་འདུན་གྱི༌[^928]སོས་པར་གྱུར་པ་ཉིད་ན་འདི་སྦྱིན་ནོ་སྙམ་པ་ལས་གཞན་པའི་ཡིད་ཀྱིས་བླང་བར་མི་བྱའོ་ཞེས་བྱ་བ་ལ་འདི༌[^929]ཞེས་བྱ་བ་ནི་ཆོས་གོས་གསུམ་པོ་འདིའོ། །

[Block 1096]
སོས་པར་གྱུར་པ་ཉིད་ན་ཞེས་བྱ་བ་ནི༌[^930]གལ་ཏེ་ཤི་བར་དོགས་པ་དེའི་ཚེ་འདི་ཕྱིར་སྦྱིན་ནོ་སྙམ་པར་དོན་གྱིས་རྟོགས་པར་བྱའོ། །

[Block 1097]
དགེ་འདུན་གྱི༌[^931]ཞེས་བྱ་བ་ནི་འདིར་དེ་སྨོས་པ་ཞེས་བྱ་བ་ནི་བསྡུས་པའོ། །

[Block 1098]
གང་ཟག་ལ་ཡང་དེ་རྟོགས་པར་བྱའོ། །

[Block 1099]
ལངས་པ་དེ་ཉིད་ལ་འདི་ཕུལ་བར་གྱུར་པ་འདི་ལའོ་ཞེས་བྱ་བ་འདིའི་དགོངས་པས་བཟུང་བ་ལ་སྐྱོན་མེད་དེ་གཞན་དུ་ན་ཉེས་བྱས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1100]
སྟོད་གཡོགས་དང་སྨད་གཡོགས་ཀྱི་རོ་དོར་རོ། །

[Block 1101]
འབྲིང་གིས་སོ་ཞེས་བྱ་བ་ནི་ངན་པ་ཡང་མ་ཡིན་བཟང་པོ་ཡང་མ་ཡིན་པའོ། །

[Block 1102]
ལྷག་མས་མི་བྱའོ་ཞེས་བྱ་བ་ནི་སྟོད་གཡོགས་དང་སྨད་གཡོགས་ལས་གཞན་པའི་རྫས་ལྷག་མས་རོ་དོར་བར་མི་བྱ་སྟེ། བཀག་པའི་ཕྱིར་འདིར་གསུངས་སོ། །

[Block 1103]
ལྷག་མ་ཡང་དེ་ཉིད་དུ་བསྲེ་བར་མི་རིགས་པ་ཡིན་ནོ། །

[Block 1104]
ཅི་རོའི་རྫས་བཟུང་བས་ཞེས་བྱ་བའི་བློ་བསལ་བའི༌[^932]དོན་དུ་དེའོ།[^933] །སྐ་རགས་མ་བཅིངས་པས༌[^934]གྲོང་དུ་འཇུག་པར་མི་བྱའོ། །

[Block 1105]
ཁྲིས་གཅིག་གིས་ཀྱང་ངོ་། །གོས་ཀྱི་གཞི་ཕྲན་ཚེགས་ལ་སོགས་པའི་ཞུ་བ་བཅས་པའི་སྐབས་སོ། །

[Block 1106]
གོས་ཀྱི་གཞི་རྫོགས་སོ།། །།

[Block 1107 [HEADING]]
## ཀོ་ལྤགས་ཀྱི་གཞི། ^3-0

[Block 1108]
མཐའ་ཁོབ༌[^935]ངེས་པར་ཤེས་པར་བྱ་བའི་ཕྱིར་ཡུལ་དབུས་བསྟན་པར་བྱ་སྟེ། དེའི་ཕྱིར་ཡུལ་དབུས་ཀྱི་མཚམས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཤར་དུ་ནི་ལི་ཁ་ར་ཤིང་འཕེལ་གྱི་མདུན་གྱི་ནགས་ཕུང་པོ་ཚང་ཚིང་ཅན་ཞེས་བྱ་བའོ། །

[Block 1109]
འདིར་ནགས་ཀྱི་ཆ་གཞན་མཚམས་སུ་རྣམ་པར་གནས་པ་ཡིན་ཏེ། དེའི་ནུབ་ཀྱི་ཆ་ཚུན་ཆད་དབུས་ཀྱི་མཚམས་སོ། །

[Block 1110]
ལྷོར་ནི་འདམ་བུ་ཅན་གྱི་ལྷོ་ན་ཆུ་ཀླུང་དེ་ཞེས་བྱ་བའོ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བ་ནི་ལྷོ་ཕྱོགས་ཀྱི་ཆ་ལའོ། །

[Block 1111]
དེའི་ལྷོ་ན་ཆུ་ཀླུང་འདམ་བུ་ཅན་ཞེས་བྱ་བ་ཡོད་པའི་བྱང་གི་ཆ་ཚུན་ཆད་ནི། ཡུལ་དབུས་ཀྱི་ལྷོ་ཕྱོགས་ཀྱི་མཚམས་ཡིན་ནོ། །

[Block 1112]
ནུབ་ཏུ་ནི་བྲམ་ཟེའི་གྲོང་ཀ་བ་དང་། ཉེ་བའི་ཀ་བ་ཞེས་བྱ་བ་གཉིས་སོ་ཞེས་བྱ་བ་ནི་ནུབ་ཏུ་བྲམ་ཟེའི་གྲོང་ཀ་བ་དང་ཉེ་བའི་ཀ་བ་ཞེས་བྱ་བ་ཡོད་པའི་ཤར་གྱི་ཆ་ཚུན་ཆད་དུ་ཡུལ་དབུས་ཀྱི༌[^936]མཚམས་སོ། །

[Block 1113]
བྱང་དུ་ནི་ཨུ་ཤི་རའི༌[^937]རི་ཞེས་བྱ་བའོ་ཞེས་བྱ་བ་ནི་མཚམས་ཡིན་ནོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1114]
ཇི་ལྟར་ཨུ་ཤི་རའི༌[^938]རིའི་ལྷོ་ཕྱོགས་ཀྱི་མཐར་ཐུག་པའོ། །

[Block 1115]
མཐའ་ཁོབ་ཏུ་མཆིལ་ལྷམ་དག་བཅང་བར་བྱའོ། །

[Block 1116]
གནས་མལ་བསྐྱབ་པའི་ཕྱིར་ཡང་ངོ་། །མཐའ་ཁོབ་མ་ཡིན་པར་ཡང་མཆིལ་ལྷམ་དག་བཅང་བར༌[^939]བྱའོ། །

[Block 1117]
རྐང་པ་དང་བཅས་པའི་སྟན་ལ་འདུག་པ་ལ་གནས་མལ་རྐྱང་པ༌[^940]མི་འགྲུབ་པའོ། །

[Block 1118]
གནས་གཞན་དུ་སོང་བས་ཀྱང་གནས་མལ་བསྐྱང་བར་དགོས་པ་མེད་དོ། །

[Block 1119]
དེ་བས་ན་ལམ་དུ་འདི་དག་སྲེལ་བར༌[^941]བྱ་བ་ཉིད་མ༌[^942]ཡིན་ནོ། །

[Block 1120]
གཞན་དུ་སོང་བས་ཀྱང་རྐང་པ་ལ་དགོས་པས་དེ་དག་བགོ་བར༌[^943]ཤིན་ཏུ་རིགས་པ་ཡིན་ནོ། །

[Block 1121]
འདི་དག་ལམ་དུ་སོང་བས་ཀྱང་རྗེས་སུ་ཁུར་བ་ཡང་རིགས་སོ། །

[Block 1122]
འདི་གཉིས་ལ་ཡང་མཚོན་པར་བྱེད་པའི་རྟགས་འདིར་ཡང་ཡོད་དེ། དེའི་ཕྱིར་འདིར་གཞུང་ནི་བསོད་སྙོམས་པ་ཞིག་མཉན་ཡོད་དུ་བསོད་སྙོམས་ལ་ཞུགས་པ་ན། དེར་མཆིལ་ལྷམ་མེད་པས་རྐང་པ་དག་ལ་སེར་ཁ་བྱུང་བ་ཁྱིམ་བདག་གིས་མཐོང་ནས་དེས་དེ་ལ་སྨྲས་པ། འཕགས་པ་ཁྱོད་ལ་མཆིལ་ལྷམ་དག་མེད་དམ། མེད་དོ། །

[Block 1123]
ཚུར་ཤེག༌[^944]དང་སྦྱིན་དུ་གཞུག༌[^945]གོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ནོ། །

[Block 1124]
ཅི་ཡང་རུང་བའི་མཆིལ་ལྷམ་གནས་མལ་བསྐྱང་བའི་དོན་དུ་མཐའ་ཁོབ༌[^946]དག་ཏུ་བཅང་བར་བྱ་བའམ་ཞེ་ན། དེའི་ཕྱིར་ཆིག་རིམ་མོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཆིག་རིམ་གང་ལ་ཡོད་པ་དེ་ནི་ཆིག་རིམ་གཅིག་པའོ། །

[Block 1125]
དེ་ཡང་འདིར་མཐིལ་ཆིག་པའི༌[^947]རིམ་ཅན༌[^948]ནམ་རིམ་པ་གཅིག༌[^949]ལ་གནས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །
--- END BLOCKS ---
