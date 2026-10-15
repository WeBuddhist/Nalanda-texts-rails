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
ལྷག་པར་ཆགས་པའི་དངོས་པོ་འགུགས་ན་དགག༌[^839]པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ་ལྷག་པར་ཆགས་པའི་དངོས་པོ་ནི་ལྷུང་བཟེད་ལ་སོགས་པ་གང་ལ་ནད་པའི་སྲེད༌[^840]པའོ། །

[Block 1192]
འགུགས་ན་ཞེས་བྱ་བ་ནི་ནད་པས་ནད་གཡོག་ལའོ། །

[Block 1193]
མི་གདམས་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ནད་གཡོག་གིས་ནད་པ་ལའོ། །

[Block 1194]
དེ་ནད་པས་བཟླ་བར་ཤིན་ཏུ་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ནད་གཡོག་གིས་གདམས་ངག་བྱས་པ་ལས་ནད་པ་འདའ་བར་མི་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1195]
ནད་གཡོག་དེས་དེ་འཆི་བར་དོགས་ན་དེ་དགེ་འདུན་གྱི་མལ་སྟན་ལ་བསླང་སྟེ་གང་ཟག་གི་ལ་གཞག་པར་བྱའོ། །

[Block 1196]
བསྐུ་མཉེ༌[^841]དང་ཁྲུས་སྔར་བྱ་བ་ཉིད་ཀྱིས་སྒྱུ་ཐབས་ཀྱིས་སོ་ཞེས་བྱ་བ་ལ། བསྐུ་མཉེ༌[^842]དང་ཁྲུས་སྔར་བྱ་བ་ཉིད་ཀྱིས༌[^843]སྒྱུ་ཐབས་ཀྱིས་གཞག་པར་བྱའོ། །

[Block 1197]
འདིར་སྒྱུ་ཐབས་ནི་གཙོ་བོ་ཉིད་ཀྱི་ཕྱིར་གཉིས་པོ་འདི་དཔེར་རིག་པར་བྱའོ། །

[Block 1198]
དེའི་གནས་སྐབས་ཀྱི་ཡོངས་སུ་བརྟག་པ༌[^844]ལ་འབད་པ་དང་ལྡན་པར་བྱའོ་ཞེས་བྱ་བ་ནི༌[^845]ཤི་བའི་གནས་སྐབས་ཡོངས་སུ་གཅོད་པ་ལ་ལུས་ཀྱི་གནས་སྐབས་གང་ལ་འཆི་བའི་དོགས་པ་འབྱུང་བ་དེ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1199]
འདིར་འབད་པ་ནི་ཡང་ནས་ཡང་དུ་རྟོག་པའོ། །

[Block 1200]
དེས་སྨེ་བར་བྱས་པའི་ཤི་བའི་གོས་དེ་དག་བཀྲུ་བ་ནི་དེས་བྱ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ནད་དེས་ཀུན་ནས་ཉོན་མོངས་པར་བྱས་པ་ཤི་བའི་གོས་དེ་རྣམས་ལ་ནད་པ་གང་ལ་ནད་གཡོག་དེས་ཤི་བ་དེ་ཉིད་ཀྱི་གལ་ཏེ་གོས་དེ་རྣམས་ཡིན་ན་ཡང་གཞན་གྱིས་དེ་རྣམས་བཀྲུ་བ་མ་ཡིན་ཏེ། ནད་གཡོག་དེས་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1201]
དགེ་འདུན་འདུས་པ་ན་དེའི་གནས་བརྟན་མདུན༌[^846]དུ་འགྲོ་བར་བྱའོ་ཞེས་བྱ་བ་ལ། འདི་ནི༌[^847]རྟེན་དང་བརྟེན་པའི༌[^848]རབ་ཏུ་དབྱེ་བ་ཞེས་བྱ་བའི་མཐར་ཐུག་པ་འདི་ལ་དགེ་འདུན་གྱི་གནས་བརྟན་གྱིས་དབང་དུ་བྱ་བ་ལ་ཉེ་བར་དགོད་པ༌[^849]སྟེ་དགེ་འདུན་ཚོགས་པ་ན་དགེ་འདུན་གྱི་གནས་བརྟན་ཐོག་མར་འགྲོ་བར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1202]
འགྲོ་བའི་ཚེ་ཐོགས་ན་བསྡད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གནས་བརྟན་དེའོ། །

[Block 1203]
དེ་རྣམས་ཀྱིས་དེ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་གང་རྣམས་ཀྱི་གནས་བརྟན་དེ་དེ་རྣམས་ཀྱིས༌[^850]ཡང་ཐོགས༌[^851]ན་བསྡད་པར་བྱའོ། །

[Block 1204]
མ་བྱུང་བ་ལ་ནི་རིང་བར་སོང་སྟེའོ། །

[Block 1205]
གྲོང་གི་ཉེན་ཀོར་དུ་ཡང་ངོ་ཞེས་བྱ་བ་ལ། ཉེན་ཀོར་གྱི་སྐྲ༌[^852]ནི་ཉེ་བར་བརྗོད་པར་བྱའོ།[^853] །གལ་ཏེ་འཇུག་པ་ན་ཕྱི་བཞིན་འོངས་པ་ན་ཡང་ངོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་མངོན་པར་འཇུག་པར༌[^854]འདོད་ན་ཕྱི་བཞིན་འོང་བ་འདི་ལ་གྲོང་གི་ཉེན་ཀོར་དུ་བསྡད་པར་བྱའོ། །

[Block 1206]
དེ་ལྟར་ལྟ་བར་གྱུར་པ་རྣམས་ལ་གལ་ཏེ་སྦྲོན་པ་འོངས་ན་ཡང་དེ་ལ་གནས་བརྟན་འོངས་ཀྱི་བར་དུ་སྡོད་ཅིག་ཅེས་གོ་བར་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ལ་ཞེས་བྱ་བ་སྦྲོན་པ་ལའོ། །

[Block 1207]
ཟས་ཀྱི་ཕྱིར་སོན་པ་ཉིད་ན་ལག་ཆུ་དྲངས་པའི་ཚེ་གལ་ཏེ་དུས་ཡོད་ན་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཟས་ཀྱི་ཕྱིར་རམ་བཏུང་བའི་ཕྱིར་སོན་པ་ཉིད་ན་ལག་ཆུ་དྲངས་པའི་ཚེ་གལ་ཏེ་ཐོགས་པར་གྱུར་པ་རྣམས་ལ་དུས་ཡོད་ན་དེ་ནས་སྦྲོན་པ༌[^855]དེ་ལ་ཚུར་ཤོག་ཇི་སྲིད་དགེ་འདུན་གྱི་གནས་བརྟན་འོངས་ཀྱི་བར་དུ་སྡོད་ཅིག་ཅེས་བསྒོ་བར་བྱའོ། །

[Block 1208]
མེད་ན་གྲལ་དེར་དེའི་སྟན་གཞག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་བསྡད་པའི་དུས་སུ་མེད་ན་བཟའ་བ་ལ་སོགས་པར་ཞུགས་པ་ལ་དགེ་འདུན་གྱི་གནས་བརྟན་ལ་སྟན༌[^856]བཞག་པར་བྱའོ། །

[Block 1209]
འདུག་པ་དང་ཕྱི་རོལ་དུ་ཡང་སོ་སོར་བརྟག་པར་བྱའོ་ཞེས་བྱ་བ་ལ། འདིར་འདུག་པ་ནི་ཁྱིམ་གྱི་ནང་དུའོ། །

[Block 1210]
ཕྱི་རོལ་ཞེས་བྱ་བ་ནི་སྡོད་ས་ལས་སོ། །

[Block 1211]
གནས་སྐབས་འདི་དག་ལ་དགེ་འདུན་གྱི་གནས་བརྟན་གྱིས་སོ་སོར་བརྟག་པར་བྱའོ། །

[Block 1212]
ལེགས་པར་མ་བགོས་པ་ཉིད་དང་ལེགས་པར་མ་དཔྱངས་པ་ཉིད་ཡིན་ན་མཛེས་པར་བྱ་བའི་ཕྱིར་དེ་གཉིས་ལ་བརྡ་བྱའོ་ཞེས་བྱ་བ་ལ། ལེགས་པར་མ་བགོས་པ་ཉིད་དམ་ལེགས་པར་མ་དཔྱངས་པ་ཉིད་ལ་མཛེས་པར་བྱ་བའི་ཕྱིར་འདི་དག་གི་རྒྱུ་མཚན་དུ་འདི་ལ་བྱའོ། །

[Block 1213]
དེ་གཉིས་ལ་ཞེས་བྱ་བ་ནི་མ་བགོས་པ་ཉིད་དམ་ལེགས་པར་མ་དཔྱངས་པ་ཉིད་ལའོ། །

[Block 1214]
མ་གོ་ན་དྲུང་ན་མོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་འདི་མ་བགོས་པ༌[^857]ཉིད་དམ་ལེགས་པར་མ་དཔྱངས་པ་ཉིད་དོ། །

[Block 1215]
མ་གོ་ན༌[^858]དྲུང་ན་མོ་བྱེད་དུ་གཞུག་གོ་ཞེས་བྱ་བ་ལ། གལ་ཏེ་འདི་མ་བགོས་པ་ཉིད༌[^859]དགེ་འདུན་གྱི༌[^860]གནས་བརྟན་གྱིས་བརྡ་བྱེད་བཞིན་པས་གོ་བར་མ་གྱུར་ན་དེ་ནས་དྲུང་ན་མོ་དེས་བྱེད་དུ་གཞུག་གོ། །

[Block 1216]
མ་གྱུར་ན་རང་གིས་སོ་ཞེས་བྱ་བ་ནི་དེ་ལྟར་ན་ཡང་མཛེས་པར་བྱེད་པ་ལ། གྲུབ་པར་མ་གྱུར་ན་རང་གིས་བྱེད་དུ་གཞུག་གོ། །

[Block 1217]
བརྡ་མ་གོ་ན་ཚིག་གིས་བྱེད་དུ་གཞུག་གོ། །

[Block 1218]
གསར་བུ་དེ་དག་ལ་ཀུན་དུ་སྨྲ་བར་མི་བྱའོ། །

[Block 1219]
གང་རྣམས་ཀྱིས་དེར་དགེ་འདུན་གྱི་གནས་བརྟན་དེས་གཙུག་ལག་ཁང་དང་དགོན་པ་དེར་དེ་དག་གི་ཚུལ་ཁྲིམས་ཀྱི་ཚུལ་ཁྲིམས་དེ་འཛིན་དུ་གཞུག་པར་བྱ་ཞིང་ངེས་པར་སྦྱར་བར་ཡང་བའོ༌[^861]ཞེས་བྱ་བ་ལ། གང་རྣམས་ཀྱི་ཞེས་བྱ༌[^862]ནི་གསར་བུ་དེ་རྣམས་ལའོ། །

[Block 1220]
དེ་དག་གི་ཚུལ་ཁྲིམས་ཞེས་བྱ་བ་ནི་གཙུག་ལག་ཁང་གི་ཚུལ་ཁྲིམས་དང་དགོན་པའི་ཚུལ་ཁྲིམས་སོ། །

[Block 1221]
ངེས་པར་སྦྱར་བར་བྱ་ཞེས་པ་ནི། [^863]དེ་དག་གི༌[^864]ཚུལ་ཁྲིམས་འཛིན་དུ་གཞུག་པར་བྱ་བ་གཅིག་པུར་མ་ཟད་ཀྱི། འོན་ཀྱང་ཚུལ་ཁྲིམས་དེ་བསྒྲུབ་པ་ལ་དེ་རྣམས་ཀྱི་ངེས་པར་སྦྱར་བ༌[^865]ཡང་བྱའོ། །

[Block 1222]
གློ་བུར་དུ་འོངས་པས་ནི་སོ་སོར་བརྟགས་ནས་གནས་མལ་གྱི་ཕྱི་རོལ༌[^866]གཉུག་མར་གནས་པ་རྣམས་ལ་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་ལ། གནས་མལ་གྱི་ཕྱིར་གློ་བུར་དུ་འོངས་པའི་དགེ་འདུན་གྱི་གནས་བརྟན་གྱིས་གློ་བུར་དུ་འོངས་པ་མ་ཡིན་པ་རྣམས་ལ་སོ་སོར་བརྟག་པར༌[^867]བྱའོ། །

[Block 1223]
གང་རྣམས་ཀྱི་དགེ་འདུན་གྱི་གནས༌[^868]བརྟན་འདི་གཉུག་མར་གནས་པ་རྣམས་ལ་གནས་མལ་གྱི་ཕྱིར་བརྗོད་པར་བྱའོ། །

[Block 1224]
འགྲོ་བར་ཆས་པས་ནི་ཕྱོགས་དང་འགྲོན་པ༌[^869]དང་གནས་དང་གནས་མལ་གྱི་གྲོགས་ན་ནི༌[^870]མི་འདོར་བ་ཉིད་བརྟགས་ནས་འབག་པར༌[^871]བྱའོ་ཞེས་བྱ་བ་ལ། འགྲོ་བར་ཆས༌[^872]པ་ལ་ནི༌[^873]དགེ་འདུན་གྱི་གནས་བརྟན་ནོ། །

[Block 1225]
འགྲོན་པ་རྣམས་ལ་ཞེས་བྱ་བ་ནི་དོན་གྱིས་གོ་བར་བྱ་སྟེ་ཕྱོགས་གང་དུ་འགྲོ་བར་བྱ་བ་འགྲོ་བ་དང་ལམ་གྱིས༌[^874]གནས་གང་ཞིག་དེར་འགྲོ་བ་ལ་གནས་མལ་དང་དེ་ཐམས་ཅད་བློ་རིགས་པ་ཉིད་ཀྱིས་གཞལ་བར་བྱ་སྟེ་གྲོགས་རྣམས་དང་ནད་ཡོད་པ་ལ་གང་གིས་ཀྱང་སུ་ཡང་ཡོངས་སུ་དོར་བར་མི་བྱའོ་ཞེས་བྱ་བ་དེ་ལྟར་གཞལ་བར་བྱས་ནས་དེ་ནས་ཇི་ལྟར་འདོད་པའི་གནས་ཐོབ་པར་བྱ་བའི་ཕྱིར་འགྲོ་བར་བྱའོ། །

[Block 1226]
རིང་པོར་མ་སོན་པར་ཐམས་ཅད་ཀྱི་ཐ་མར་ལ་ལའི་ཅུང་ཟད་མ་ལུས་སམ་ཞེས་འཕྲལ་དུ་དྲན་པར་བྱའོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་གྱི་གནས་བརྟན་ཉིད་དོ། །

[Block 1227]
གསར་བུ་རྣམས་མི་རྒོད་པ་ཉིད་དང་མ་ཁེངས་པ་ཉིད་ལ་དགོད་པར་བྱའོ་ཞེས་བྱ་བ་ལ། རྒོད་པ་ནི་ཉེ་བར་མ་ཞི་བའོ། །

[Block 1228]
ཁེངས་པ་ཉིད་ནི་རེངས་པ་ཉིད་དེ་དེ༌[^875]དག་བཟློག་པ་ལ་རབ་ཏུ་དགོད་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1229]
ཁྱིམ་ཕྱིར་ཉེ་བ་ནི་ཐམས་ཅད་ཀྱིས་ཐམས་ཅད་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་མི་རྒོད་པ་ཉིད་དང་མ་ཁེངས་པ་ཉིད་ལ་དགོད་པར་བྱའོ་ཞེས་བྱ་བ་དང་རྗེས་སུ་འབྲེལ་ལོ། །

[Block 1230]
འགྲོ་བར་ཆས་པ་ནི་གནས་བརྟེན༌[^876]ཉིད་མ་ཡིན་ཏེ། འོན་ཀྱང་གཞན་ཡང་སྟེ་གསར་དུ་ཞུགས་པ་ཉིད་རྣམས་ནི་མ་ཡིན་ཏེ། འོན་ཀྱང་གཞན་ལ་ཡང་ཞེས་བྱ་བའི་དོན་ཏོ། །
--- END BLOCKS ---
