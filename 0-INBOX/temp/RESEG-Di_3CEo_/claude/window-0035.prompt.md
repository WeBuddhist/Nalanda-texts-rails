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
[Block 1226]
ཐོགས་མེད་ལྡན། འདི་ལ་གང་དུ་ཡང་ཐོགས་པ་མེད་པའོ། །

[Block 1227]
མི་ཟློགས། སྲིད་པ་བར་མ་དོར་ནས་ལྷའི་སྲིད་པ་བར་མའམ། གཞན་དུ་འགྱུར་བ་ནི་མི་སྲིད་དོ། །

[Block 1228]
ཁམ་གྱི༌[^457]ཟས་ཀྱིས་གནས་པ་ཡིན་ཡང་རགས་པ་ནི་མི་ཟ་སྟེ། འོན་ཀྱང་དེ་ནི་དྲི་ཟའོ། །

[Block 1229]
དེ་ནི་དྲི་ཟ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1230]
ཡང་འགྲོ་བའི་ཡུལ་དུ་ཕྱིན་པར་བྱ་བའི་ཕྱིར་འབྱུང་བའི་སྲིད་པ་བར་མ་དེ་ནི།

[Block 1231 [VERSE]]
བློ་ནི༌[^458]ཕྱིན་ཅི་ལོག་གྱུར་པས། །
རྩེ་དགས་འགྲོ་བའི་ཡུལ་དུ་འགྲོ། །

[Block 1232]
དེ་ནི་ལས་ཀྱི་མཐུ་ལས་བྱུང་བའི་མིག་གིས་རང་གི་སྐྱེ་བའི་ཡུལ་ཐག་རིང་པོ་ན་འདུག་ཀྱང་མཐོང་ངོ་། །དེས་དེ་ན་ཕ་མ་ཉལ་པོ་བྱེད་པ་དེ་མཐོང་ནས་ཕོ་ཞིག་ཡིན་ན་ནི་མ་ལ་ཕོའི་འདོད་ཆགས་སྐྱེའོ།[^459] །

[Block 1233]
བཟློག་པ་ལ་ནི་ཁོང་ཁྲོ་བ་སྟེ། །དེ་དེ་གཉིས་ཀྱིས་ཕྱིན་གྱི་ལོག་ཏུ་གྱུར་པས་ཡུལ་དེར་ཕྱིན་པ་དང་། དགའ་བ་འདོད་ནས་གནས་སྐབས་དེར་བདག་ཉིད་མོས་སོ། །

[Block 1234]
རེ་ཞིག་སྒོ་ང་ལ༌[^460]སྐྱེ་བ་དང་། མངལ་ལས༌[^461]སྐྱེ་བའི་སྐྱེ་གནས་སུ་འཇུག་པ་ནི་དེ་ལྟ་བུའོ། །

[Block 1235]
དྲི་དང་གནས་ལ་མངོན་འདོད་གཞན། །དྲོད་གཤེར་ལས་སྐྱེ་བའི་སྐྱེ་གནས་སུ་སྐྱེ་བ་ནི། ལས་ཇི་ལྟ་བ་བཞིན་དུ་སྐྱེ་བའི་གནས་གཙང་མའམ་མི་གཙང་བའི་དྲི་འདོད་པས་འགྲོའོ། །

[Block 1236]
རྫུས་ཏེ་སྐྱེ་བའི་སྐྱེ་གནས་སུ་སྐྱེ་བ་ནི་གནས་འདོད་པས་སོ། །

[Block 1237]
དེ་ལ་ལྷའི་སྲིད་པ་བར་མ་ནི་སྟན་ལས་ལྡང་བ་བཞིན་དུ་གྱེན་དུ་འགྲོའོ། །

[Block 1238]
མི་དང་། དུད་འགྲོ་དང་། ཡི་དགས་རྣམས་ཀྱི་ནི་མི་ལ་སོགས་པ་བཞིན་ནོ། །

[Block 1239 [VERSE]]
དམྱལ་བ་ཡི་ནི་སྤྱིའུ་ཚུགས་ཡིན། །
ཡང་དག་སྡོམ་དང་དཀའ་ཐུབ་ཅན།[^462] །
དྲང་སྲོང་རྣམས་ལ་སྐུར་འདེབས་པ། །
རྐང་པ་གྱེན་བསྟན་སྤྱི༌[^463]ཚུགས་སུ། །

[Block 1240]
དེ་དག་དམྱལ་བ་རྣམས་སུ་ལྟུང་། །ཞེས་ཚིགས་སུ་བཅད་པ་དེ་མངོན་པར་བརྗོད་པའི་ཕྱིར་རོ། །

[Block 1241 [HEADING]]
#### མངལ་དུ་འཇུག་པ། ^3-1-6-0

[Block 1242]
མདོ་ལས་མངལ་དུ་འཇུག་པ་ནི་བཞི་གསུངས་ཏེ། དེ་ལ་གཅིག་ནི་ཤེས་བཞིན་དུ་འཇུག་གོ། །

[Block 1243]
གནས་པ་དང་འབྱུང་བ་ནི་ཤེས་བཞིན་དུ་མ་ཡིན་ནོ། །

[Block 1244]
གཞན་ནི་གནས་པ་ཡང་། ཡང་ཞེས་བྱ་བའི་སྒྲས་ནི་འཇུག་པ་ཡང་ངོ་། །

[Block 1245]
གཞན་ནི། འབྱུང་བའང་། ཤེས་བཞིན་དུ་འཇུག་པ་དང་གནས་པ་ཡང་ངོ་། །གཞན་ནི་ཐམས་ཅད་རྨོངས། ལ་ལ་ནི་ཤེས་བཞིན་མ་ཡིན་པར་བྱེད་དོ། །

[Block 1246]
དེ་ཡང་ནི་སྒོ་ང་ལས་སྐྱེས་རྟག་ཏུའོ། །

[Block 1247]
སེམས་ཅན་སྒོ་ང་ལས་སྐྱེས་པ་ནི་རྟག་ཏུ་རྨོངས་པར༌[^464]བྱེད་དོ། །

[Block 1248]
ཡང་འདིར་བསྟན་པ།

[Block 1249 [VERSE]]
མངལ་དུ་འཇུག་པ་གསུམ་དག་སྟེ། །
འཁོར་ལོས་སྒྱུར་དང་རང་བྱུང་གཉིས། །

[Block 1250]
འཁོར་ལོས་སྒྱུར་བ་དང་། རང་བྱུང་སངས་རྒྱས་དང་། རྫོགས་པའི་སངས་རྒྱས་དག་སྟེ། འོག་ནས་གོ་རིམས་བཞིན་ཞེས་འཆད་པར་འགྱུར་རོ། །

[Block 1251 [VERSE]]
ལས་སམ་ཡེ་ཤེས་སམ་གཉིས་ཀ །
རྒྱ་ཆེའི་ཕྱིར་ན་གོ་རིམས་བཞིན། །

[Block 1252]
ལས་རྒྱ་ཆེན་པོ་བསོད་ནམས་རྒྱ་ཆེན་པོ་བྱེད་པ་རྣམས་ནི་དང་པོ་ཡིན་ནོ། །

[Block 1253]
ཡེ་ཤེས་རྒྱ་ཆེན་པོ་ཐོས་པ་མང་པོ་དང་རབ་ཏུ་འབྱེད་པ་བྱེད་པ་རྣམས་ནི་གཉིས་པ་ཡིན་ནོ། །

[Block 1254]
བསོད་ནམས་ཀྱི་ལས་དང་ཡེ་ཤེས་རྒྱ་ཆེ་བ་རྣམས་ནི་གསུམ་པ་ཡིན་ནོ། །

[Block 1255]
གལ་ཏེ་སེམས་ཅན་ཐམས་ཅད་ལ་མངལ་དུ་འཇུག་པ་ཡོད་ན་བདག་ཡོད་པར་འགྱུར་རོ་ཞེ་ན་བདག་མེད། བདག་ཇི་ལྟ་བུ་ཞིག་ཅེ་ན། གང་ཕུང་པོ་འདི་བདག་འདོར་ཞིང་ཕུང་པོ་གཞན་དུ་ཉིང་མཚམས་སྦྱོར་རོ་ཞེས་བྱ་བར་རྟོག་པའོ། །

[Block 1256]
འོ་ན་བདག་ཇི་ལྟ་བུ་ཞིག་མི་དགག་ཅེ་ན། ཕུང་པོ་ཙམ་ཉིད་དོ། །

[Block 1257]
གལ་ཏེ་ཕུང་པོ་ཙམ་ཁོ་ན་ལ་བདག་ཅེས་འདོགས་ན་དེ་ལ་དགག་པ་མེད་དོ། །

[Block 1258]
དེ་ལྟར༌[^465]ན་འོ་ན་ཕུང་པོ་བདག་ཉིད་འཇིག་རྟེན་གཞན་དུ་འཕོའོ་ཞེས་བྱ་བར་འགྱུར་རོ་ཞེ་ན། དེ་དག་ནི་མི་འཕོ༌[^466]སྟེ།

[Block 1259 [VERSE]]
ཉོན་མོངས་ལས་ཀྱིས་མངོན་འདུས༌[^467]བྱས། །
སྲིད་པ་བར་མའི་རྒྱུན་གྱིས་ནི། །
མར་མེ་བཞིན་དུ་མངལ་དུ་འགྲོ། །

[Block 1260]
ཕུང་པོ་རྣམས་ནི་སྐད་ཅིག་མ་སྟེ། དེ་དག་ལ་ནི་འཕོ་བའི་མཐུ་མེད་ཀྱི་ཉོན་མོངས་པ་རྣམས་དང་ལས་རྣམས་ཀྱིས༌[^468]ཡོངས་སུ་བསྒོས་པའི༌[^469]ཕུང་པོ་ཙམ་གྱི་སྲིད་པ་བར་མ་ཞེས་བྱ་བའི་རྒྱུན་གྱིས་མའི་མངལ་དུ་འགྲོ་སྟེ། དཔེར་ན་མར་མེ་བཞིན་ནོ། །

[Block 1261]
དེ་ཡང་།

[Block 1262 [VERSE]]
ཇི་ལྟར་འཕངས་བཞིན་རིམ་གྱིས་རྒྱུན། །
སྐྱེས་ནས་ལས་དང་ཉོན་མོངས་ཀྱིས། །
འཇིག་རྟེན་ཕ་རོལ་དག་ཏུ་འགྲོ། །

[Block 1263]
ཚེའི་ལས་ཐ་དད་པའི་ཕྱིར་ཕུང་པོའི་རྒྱུན་ཐམས་ཅད་ཀྱིས་འཕེན་པར་འདྲ་བ་ནི་མ་ཡིན་པས། དེའི་ཕྱིར་གང་ཞིག་ཇི་སྲིད་དུ་འཕངས་པ་དེ་སྲིད་ནུར་ནུར་པོ་ལ་སོགས་པའི་རིམ་གྱིས་སྐྱེ་བར་འགྱུར་ཏེ། དབང་པོ་རྣམས་ཡོངས་སུ་སྨིན་ནས་ནི༌[^470]ཉོན་མོངས་པ་རྣམས་ཀུན་དུ་སྤྱོད་ཅིང་ལས་རྣམས་ཀྱང་ཉེ་བར་སོག༌[^471]པར་འགྱུར་རོ། །

[Block 1264]
དེ་དག་ལུས་ཞིག་ནས་ཡང་སྔ་མ་བཞིན་དུ་སྲིད་པ་བར་མའི་རྒྱུན་གྱིས་འཇིག་རྟེན་ཕ་རོལ་དུ་འགྲོ་སྟེ། དེ་ལྟར། སྲིད་པའི་འཁོར་ལོ་ཐོག་མ་མེད། །རྣམ་པ་དེས་ན་ལས་དང་ཉོན་མོངས་པའི་རྒྱུ་ལས་བྱུང་བའི་སྐྱེ་བ་དང་། ཡང་དེ་ལས་བྱུང་བའི་ལས་དང་ཉོན་མོངས་པ་རྣམས་དང་། ཡང་དེ་དག་ལས་སྐྱེ་བ་ཡིན་པས་ན་སྲིད་པའི་འཁོར་ལོ་ཐོག་མ་མེད་པ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 1265 [HEADING]]
#### རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ། ^3-1-7-0
--- END BLOCKS ---
