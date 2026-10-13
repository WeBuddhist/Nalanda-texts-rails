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
[Block 1121]
ཞེས་གསུངས་སོ། །

[Block 1122]
དེས་ནི་ལྷག་པའི་ཤེས་རབ་ཀྱི་བསླབ་པ་བསྟན་ཏོ། །

[Block 1123 [VERSE]]
དེ་ལྟར་སྟོང་ཉིད་བསྒོམ་བྱས་ནས། །
རིམ་གྱིས༌[^625]དྲོད་སོགས་ཐོབ་བྱས་ནས། །
རབ་དགའ་ལ་སོགས་ཐོབ་འགྱུར་ཏེ། །
སངས་རྒྱས་བྱང་ཆུབ་ཡུན་མི་རིང་། །

[Block 1124]
འདིར་མཉམ་པར་གཞག་པའི་རྣལ་འབྱོར་དང་། སྤྱོད་ལམ་གྱི་རྣལ་འབྱོར་ལ་གནས་ནས་གོང་དུ་ཇི་ལྟར་བཤད་པའི་ཐེག་པ་ཆེན་པོའི་མདོ་སྡེའི་དོན་ཕ་རོལ་ཏུ་ཕྱིན་པའི་ལམ་ལ་ལེགས་པར་གནས་པ་དེས། མགོན་པོ་བྱམས་པའི་ཞལ་ནས་གསུངས་ཤིང་། འཕགས་པ་ཐོགས་མེད་ཀྱིས་འཛམ་བུའི་གླིང་དུ་རྒྱས་པར་སྤེལ་བའི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་ལམ་མངོན་པར་རྟོགས་པའི་རྒྱན་གྱི་སྐབས་བརྒྱད་ཀྱི་རིམ་པ་འཕགས་པ་རྣམ་པར་གྲོལ་བའི་སྡེ་དང་། སློབ་དཔོན་དཔལ་སེང་གེ་བཟང་པོས་བཀྲོལ༌[^626]ཞིང་བཤད་པ་དེ་ཤེས་པར་བྱས་ལ་གནས་པར་བྱའོ། །

[Block 1125]
དེ་ལྟ་མ་ཡིན་ན་ལམ་འབྲས་བུ་དང་བཅས་པ་ལ་རྨོངས་པར་འགྱུར་རོ། །

[Block 1126]
དེ་བས་ན་རྣལ་འབྱོར་པ་དེ་ཁོ་ན་ཉིད་ལ་གནས་པས་ཚོགས་ཀྱི་ལམ་ལ་གནས་ནས། ཐར་པའི་ཆ་དང་མཐུན་པའི་དགེ་བའི་རྩ་བ་བསྐྱེད་ནས་སྦྱོར་བའི་ལམ་ལ་རེག་པར་འགྱུར་ཏེ། རིམ་གྱིས་དྲོད་སོགས་ཞེས་པ་དྲོད་རྣམ་པ་གསུམ་དང་། རྩེ་མོ་རྣམ་པ་གསུམ་དང་། བཟོད་པ་རྣམ་པ་གསུམ་དང་། ཆོས་མཆོག་རྣམ་པ་གསུམ་ལ་གནས་ནས་ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན༌[^627]པའི་དགེ་བའི་རྩ་བ་བསྐྱེད་ཅིང་ཏིང་ངེ་འཛིན་བཞིས་མཐོང་བའི་ལམ་ལ་སོགས་པ་སྐྱེ་བ་ནི། རབ་དགའ་ལ་སོགས་ཐོབ་འགྱུར་ཏེ། །ཞེས་བྱའོ། །

[Block 1127]
སངས་རྒྱས་བྱང་ཆུབ་ཅེས་པ་ནི་འདི་ལྟར་ས་བཅུ་རྫོགས་པར་བྱས་ནས་སྐད་ཅིག་མ་གཅིག་ལ་མངོན་པར༌[^628]རྫོགས་པར་བྱང་ཆུབ་པར་གྱུར་ནས། སྐུ་གསུམ་དང་ཡེ་ཤེས་ལྔ་ལ་སོགས་པ་ཡུན་མི་རིང་བར་མྱུར་དུ་འཐོབ་པ༌[^629]ཡིན་ནོ། །

[Block 1128 [VERSE]]
དྲོད་ནས་བཟུང་སྟེ་སྦྱོར་བའི་ལམ། །
མཐོང་བའི་ལམ་སོགས་ས་བཅུ་དང་། །
སྐུ་གསུམ་ལ་སོགས་རྣམ་གཞག་ནི། །
གཞུང་མངས༌[^630]འཇིགས་པས་འདིར་མ་བྲིས། །

[Block 1129]
མདོ་དང་བསྟན་བཅོས་རྣམས་ན་གསལ། །རབ་ཏུ་བསྒྲིམས་ཏེ་བལྟ་བར་བྱ། །

[Block 1130]
ཡང་ན། སངས་རྒྱས་བྱང་ཆུབ་ཡུན་མི་རིང་། །ཞེས་བྱ་བ་ལ། འདི་ནི་བྱང་ཆུབ་སེམས་དཔའ་ལེ་ལོ་ཅན་དག་སྤྲོ་བ་བསྐྱེད་པའི༌[^631]དོན་ཡིན་ནོ།[^632] །

[Block 1131]
གང་བསྐལ་པ་གྲངས་མེད་པ༌[^633]གསུམ་ཞེས་གསུངས་པ་དེ་ཡང་ཡུན་མི་རིང་སྟེ། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ནི་འགྲོ་བ་མཐའ་དག་གི་དོན་དུ་གནས་པ་སྟེ། ཇི་སྐད་དུ་ཨམྦ་རཱ་ཛས།

[Block 1132 [VERSE]]
བདག་ནི་བྱང་ཆུབ་རིང་ཚུལ་དུ། །
འཚང་རྒྱར་མོས་ཤིང་སྤྲོ་བ་མེད། །
ཕྱི་མཐར་ཐུག་གི་བར་དུ་ནི། །
སེམས་ཅན་གཅིག་ཕྱིར་སྤྱད་པར་བྱ། །

[Block 1133]
ཞེས་གསུངས་སོ། །

[Block 1134]
དཔལ་མཆོག་དང་པོ་ལས་ཀྱང་།

[Block 1135 [VERSE]]
ཇི་སྲིད་འཁོར་བའི་གནས་སུ་ནི། །
མཁས་མཆོག་གནས་པར་གྱུར་པ་ནི། །
དེ་སྲིད་མཚུངས་མེད་སེམས་ཅན་དོན། །
མྱ་ངན་མི་འདའ་བྱེད་པར་ནུས། །

[Block 1136]
ཞེས་གསུངས་སོ། །

[Block 1137]
འཕགས་པ་ཀླུ་སྒྲུབ་ཀྱིས་ཀྱང་སྨོན་ལམ་ལས།

[Block 1138 [VERSE]]
ཇི་སྲིད་སེམས་ཅན་འདིར་འགའ་ཞིག །
སེམས་ཅན་གཅིག་གྲོལ་མ་གྱུར་པ། །
བླ་མེད་བྱང་ཆུབ་ཐོབ་གྱུར་ཀྱང་། །
དེ་སྲིད་དེ་དོན་དཔྱད་པར༌[^634]བགྱི། །

[Block 1139]
ཞེས་གསུངས་སོ། །དེ་ཅིའི་ཕྱིར་ཞེ་ན།

[Block 1140]
མདོ་ལས།

[Block 1141]
འཇིག་རྟེན་གྱི་ཁམས་འདི་ཐམས་ཅད་ཆུའི་དཀྱིལ་འཁོར་དུ་གྱུར་ལ། དེ་ལ་སྐྱེས་བུ་ཞིག་གིས༌[^635]ལོ་སྟོང་ཕྲག་བརྒྱ་བརྒྱ་ན་སྤུའི་རྩེ་མོ་ཞིག་གིས་ཆུ་དེ་ལས་འཐོར་བར་བྱས་ན། ཆུའི་དཀྱིལ་འཁོར་དེ་ནི་ཟད་པར་འགྱུར་ལ། སེམས་ཅན་གྱི་ཁམས་ལ་ཟད་པ་མེད་དོ་ཞེས་གསུངས་སོ། །

[Block 1142]
འཕགས་པ་བཟང་པོ་སྤྱོད་པ་ལས་ཀྱང་།

[Block 1143]
ནམ་མཁའི་མཐར་ཐུག་གྱུར་པ་ཅི་ཙམ་པར། །སེམས་ཅན་མ་ལུས་མཐའ་ཡང་དེ་ཙམ་མོ། །

[Block 1144]
ཞེས་གསུངས་སོ། །

[Block 1145]
དཔེར་ན་རིའི་རྒྱལ་པོ་རི་རབ་རྡུལ་ཕྲ་རབ་ཏུ་བཤིག༌[^636]པའི་རྗེས་ལ་བྱང་ཆུབ་ཐོབ་པར་བྱའོ་སྙམ་ན་ཡང་དེ་ནི་ལེ་ལོ་ཅན་ཡིན་པར་བཤད་དོ། །

[Block 1146]
དེ་བས་ན་ཨམྦ་རཱ་ཛས་ཀྱང་།

[Block 1147 [VERSE]]
འཁོར་བའི་ཐོག་མ་མེད་པ་ཡི། །
སྐྱེ་བ་ཐ་མ་ཇི་སྲིད་དུ། །
དེ་སྲིད་སེམས་ཅན་ཕན་དོན་དུ། །
སྤྱོད་པ་དཔག་ཡས་སྤྱད་པར་བགྱི། །

[Block 1148]
ཞེས་གསུངས་སོ། །

[Block 1149]
དེ་བས་ན་སེམས་ཅན་གྱི་ཁམས་ལ་ཟད་པ་ཡང་མེད་འཕེལ་བ་ཡང་མེད་པའི་སྡུག་བསྔལ་ཅན་དེ་དག་ཡལ་བར་བོར་ནས། བདག་ཉིད་མྱུར་དུ་འཚང་རྒྱ་བར་ནི་འདོད་པར་མི་བྱ་སྟེ། བྱང་ཆུབ་སེམས་དཔའ་དཔའ་བོ་དབང་པོ་རྣོན་པོ་བརྩོན་འགྲུས་རབ་དང་ལྡན་པ། སེམས་སྙིང་རྗེའི་དབང་དུ་གྱུར་བ། སེམས་ཅན་མ་ལུས་པ་ལ་སྙིང་རྗེ་བ་ཅན་དེ་ལྟ་བུ་ནི་མི་འདོད་དུ་ཟིན་ཀྱང་མྱུར་དུ་མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་བར་འགྱུར་རོ་ཞེས་བྱ་བ་ནི་ཞར་ལ་བྱུང༌[^637]བའོ། །

[Block 1150 [VERSE]]
སྨོན་ལམ་དང་ནི་འཇུག་པ་དང་། །
དེ་བཞིན་ཟབ་དང་རྒྱ་ཆེ་དང་། །
མི་ལྡོག་འབྲས་བུ་ཐོབ་པས་ཀྱང་། །
ཐེག་པ་ཆེན་པོ་ཁྱད་པར་འཕགས། །

[Block 1151]
ཞེས་སློབ་དཔོན་ཏྲི་བི་ཊ་ཀ་མ༌[^638]ལའི་ཞལ་སྔ་ནས་ཚུལ་གསུམ་པའི་སྒྲོན་མར་གསུངས་ཏེ། ཉན་ཐོས་ཀྱི་ཐེག་པ་བས་ཕ་རོལ་ཏུ་ཕྱིན་པའི་ཐེག་པ་ཁྱད་པར༌[^639]དུ་འཕགས་སོ་ཞེས་ཁོང་དུ་ཆུད་པར་བྱའོ། །

[Block 1152]
ཕ་རོལ་ཏུ་ཕྱིན་པའི་ཐེག་པ་རྫོགས་སོ།། །།

[Block 1153 [HEADING]]
## བླ་ན་མེད་པའི་ཐེག་པ་ཆེན་པོའི་ཡང་ཐེག་པ་ཆེན་པོ་གསང་སྔགས་ཀྱི་ཐེག་པ། ^10-0

[Block 1154]
ད་ནི་བླ་ན་མེད་པའི་ཐེག་པ་ཆེན་པོའི་ཡང་ཐེག་པ་ཆེན་པོ་གསང་སྔགས་ཀྱི་ཐེག་པ་བརྗོད་པར་བྱའོ། །

[Block 1155]
དེ་ཡང་སློབ་དཔོན་ཆེན་པོ་རྗེ་བཙུན་ཏྲི་བི་ཊ་ཀ་མ༌[^640]ལའི་ཞལ་སྔ་ནས།

[Block 1156 [VERSE]]
དོན་གཅིག་ཡིན་ནའང་མ་རྨོངས་དང་། །
ཐབས་མང་དཀའ་བ༌[^641]མེད་ཕྱིར་དང་། །
དབང་པོ་རྣོན་པོའི་དབང་བྱས་པས། །
སྔགས་ཀྱི་བསྟན་བཅོས་ཁྱད་པར་འཕགས། །

[Block 1157]
ཞེས༌[^642]ཤེས་རབ་ཀྱི༌[^643]ཕ་རོལ་ཏུ་ཕྱིན་པའི་ཐེག་པ་བས་གསང་སྔགས་ཀྱི་ཐེག་པ་ཁྱད་པར༌[^644]དུ་འཕགས་སོ་ཞེས་བྱ་བ་ནི་གཞུང་ལུགས་སོ། །

[Block 1158]
འདི་ལྟར་དོན་དམ་པའི་བྱང་ཆུབ་ཀྱི་སེམས་དངོས་ཕྱིན་ཅི་མ་ལོག་པ་དེ་ནི་གསང་སྔགས་ཀྱི་སྒོའི་སྤྱད་པ་སྤྱོད་པའི་བྱང་ཆུབ་སེམས་དཔས་བསྐྱེད་པར་བྱའོ། །

[Block 1159]
འོན་ཀྱང་འདིར་ནི་དེ་ལྟ་བུའི་གཞུང་གི་དོན་ནི་བདག་གིས༌[^645]མ་བརྗོད་དོ། །

[Block 1160]
འདིར་ནི་བསྐྱེད་པའི་རིམ་པ་ལ་གནས་པའི་བྱང་ཆུབ་སེམས་དཔའི་ཚོགས་གཉིས་བསགས་པའི་ཐབས་ཅུང་ཞིག་རྩ་བར་ཡང་བཀོད་ཅིང་འདིར་ཡང་རྩ་བ་ལ་བརྟེན་པ་ཙམ་ཞིག་བྲི་བར༌[^646]བྱའོ། །
--- END BLOCKS ---
