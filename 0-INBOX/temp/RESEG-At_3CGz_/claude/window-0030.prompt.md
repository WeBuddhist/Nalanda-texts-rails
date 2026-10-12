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
[Block 1051 [VERSE]]
གཞུང་མང་བྱས་པ་ཇི་ལྟ་བུ། །
མུ་སྟེགས་རྒོལ་བ་བཟློག་པའི་ཕྱིར། །
མཁས་པ་རྣམས་ཀྱིས་བྱས་པ་ཡིན། །
དེ་བས་དོན་དམ་བསྒོམ་པ་ལ། །

[Block 1052 [VERSE]]
ཚད་མས་དགོས་པ་མེད་དོ་ཞེས། །
བདག་གིས་གཞན་དུ་བཀོད་པས༌[^580]ན། །
རེ་ཞིག་འདིར་ནི་བརྗོད་མི་དགོས། །
དེ་བས་རྗེས་དཔག་གཙོར་བྱེད་པའི། །

[Block 1053 [VERSE]]
རྟོག་གེའི་གཞུང་རྣམས་དོར་བྱས་ལ། །
འཕགས་པ་ཀླུ་སྒྲུབ་གཞུང་ལུགས་ཀྱི།[^581] །
བརྒྱུད་པའི་མན་ངག་བསྒོམ་པར་བྱ། །
ཡོད་མིན་མེད་མིན་ཡོད་མེད་མིན། །

[Block 1054 [VERSE]]
གཉི་ག་མིན་པའང་མ་ཡིན་པའི། །
མཐའ་བཞི་ལས་ནི་རྣམ་གྲོལ་བའི། །
དེ་ཉིད་དབུ་མ་པ་ཡིས་རིག །
རྟག་མིན་ཆད་མིན་རྟག་ཆད་མིན། །

[Block 1055 [VERSE]]
གཉི་ག་མིན་པའང་མ་ཡིན་པའི། །
མུ་བཞི་ལས་ནི་རྣམ་གྲོལ་བའི། །
དེ་ཉིད་དབུ་མ་པ་ཡིས་རྟོགས། །
ཡོད་མེད་ལྟ་བུ་ལས་འདས་ཤིང་། །

[Block 1056 [VERSE]]
རྟག་དང་ཆད་པ་རྣམ་པར་སྤངས། །
ཤེས་དང་ཤེས་བྱ་ལས་རབ་གྲོལ། །
འདི་ནི་དབུ་མ་ཆེན་པོའི་གཞུང་། །
རྗེས་སུ་དཔག་པ་གཙོར་བྱས་ནས། །

[Block 1057 [VERSE]]
ཡོད་མེད༌[^582]རྟག་ཆད་སོགས་སྨྲས་ཀྱང་། །
ཆོས་ཉིད་དེ་ཡི་རྗེས་མི་འབྲང་།[^583] །
སྒྲོ་འདོགས་པ་དང་སྐུར་བར་ཟད། །
དཔེར་ན་གསེར་དང་ནམ་མཁའ་དང་། །

[Block 1058 [VERSE]]
ཆུ་སོགས་རང་བཞིན་དག་མོད་ཀྱི། །
སྐྱོན་དང་འགྲོགས་པ་ལྟར་སྣང་ཡང་། །
དེ་དག་སྐྱོན་གྱི་རྗེས་མི་འབྲང་། །
སྒྲོ་འདོགས་སྐུར་འདེབས་རྣམ་སྤངས་ཤིང་། །

[Block 1059 [VERSE]]
སྒྲོ་བཏགས་ཀུན་ལས་ངེས་གྲོལ་བའི། །
དེ་ཉིད་ཁོ་ན་བསྒོམ་བྱས་ལ། །
གྲུབ་པའི་མཐའ་ལ་གནས་མི་བྱ། །
འཕགས་པ་ཀླུ་སྒྲུབ་འཕགས་པའི་ལྷ། །

[Block 1060 [VERSE]]
ཟླ་གྲགས་བྷ་བྱ་ཞི་བའི་ལྷ། །
བརྒྱུད་པའི་མན་ངག་འབའ་ཞིག་བསྒོམ། །
གལ་ཏེ་བརྒྱུད་པ་མེད་གྱུར་ན། །
དེ་དག་རྣམས་ཀྱིས་བཀོད་པ་ཡི། །

[Block 1061 [VERSE]]
གཞུང་རྣམས་ཡང་དང་ཡང་དུ་བལྟ། །
ཆོས་ཀུན་ཨ་ཡི་སྒོ་ཅན་ཏེ། །
གདོད་ནས་སྐྱེ་མེད་འགག་པའང་མེད། །
ངོ་བོ་ཉིད་ཀྱིས་མྱ་ངན་འདས། །

[Block 1062 [VERSE]]
རང་བཞིན་གྱིས་ནི་རྣམ་པར་དག །
མཐོང་ནའང་མཐོང་བ་མ་ཡིན་ཏེ། །
མཐོང་བར་བྱ་དང་མཐོང་བྱེད་དང་། །
མཐོང་བ་ཤེས༌[^584]བྱ་གང་ཡང་མེད། །

[Block 1063 [VERSE]]
ཐུབ་པ་རྟག་ཏུ་མཉམ་པར་གཞག །
རྣམ་པར་རྟོག་པ་ཀུན་སྤངས་ཤིང་། །
ཆོས་ཀྱི་དབྱིངས་ལ་གནས་པ་ན། །
རྣལ་འབྱོར་ཆེན་པོའི་ཡེ་ཤེས་ལ། །

[Block 1064]
འབྱུང་དང་འཇུག་པ་དེ་མི་འདོད། །

[Block 1065 [VERSE]]
དེ་བས་མཉམ་གཞག་རྗེས་ཐོབ་དག །
སངས་རྒྱས་པ་ལ་ངེད་མི་འདོད། །
ས་ལ་གནས་པ་ཡིན་པར་ནི། །
རྣམ་པར་མི་རྟོག་གཟུངས་ལས་བཤད། །

[Block 1066 [VERSE]]
འདི་དོན་འདིར་ནི་རྒྱས་མ་བྱས། །
བདག་གི་གཞུང་འཛིན་བླ་མ་ལ། །
བསྙེན་བཀུར་སོགས་ཀྱིས་མཆོད་བྱས་ཏེ། །
ཡང་དང་ཡང་དུ་ཞུ་བར་བྱ། །

[Block 1067 [VERSE]]
ཐམས་ཅད་མཁྱེན་པས་ལུང་བསྟན་པའི། །
འཕགས་པ་ཀླུ་སྒྲུབ་ནས་བརྒྱུད་པའི། །
བྱང་ཆུབ་བཟང་པོའི་རྗེས་འབྲངས་ནས། །
གྲུབ་མཐའ་གང་ཡང་གཟུང་མི་བྱ། །

[Block 1068]
དེ་ལྟར་རིགས་པའི་སྒོ་ནས་ཆོས་ཐམས་ཅད་སྐྱེ་བ་མེད་པར་བསྒྲུབས་ནས།

[Block 1069 [HEADING]]
## ལུང་གི་སྒོ་ནས་ཆོས་ཐམས་ཅད་སྐྱེ་བ་མེད་པར་བསྟན་པ། ^9-0

[Block 1070]
ད་ནི་ལུང་གི་སྒོ་ནས་ཆོས་ཐམས་ཅད་སྐྱེ་བ་མེད་པར་བསྟན་པ་ནི། དེ་ལྟར་ཡང་བཅོམ་ལྡན་འདས་ཀྱིས་ཤེས་པ་ལ་སོགས་པ་སྟེ། རྩ་བ་ཉིད་དུ་བརྟག་པར༌[^585]བྱའོ། །

[Block 1071]
དེར་མ་ཟད་ཀྱི་དོན་འདི་ནི་བཅོམ་ལྡན་འདས་ཀྱིས་མདོ་སྡེ་གཞན་དུ་ཡང་གསུངས་ཏེ།

[Block 1072]
ཇི་སྐད་དུ་འཕགས་པ་ཆོས་ཐམས་ཅད་ཀྱི་རང་བཞིན་དབྱེར་མེད་པར་བསྟན་པའི་མདོ་ལས།

[Block 1073]
དེ་ལ་ཆོས་ཀྱི་དབྱིངས་ཚད་མར་བྱས་ན༌[^586]དོན་དམ་པ་ཡང་མེད་ཀུན་རྫོབ་ཀྱང་མེད་དོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསལ་པོར་གསུངས་པ་དང་། འཕགས་པ་བྱང་ཆུབ་སེམས་དཔའི་སྡེ་སྣོད་ལས་ཀྱང་བདེན་པ་ནི་གཅིག་སྟེ། འདི་ལྟར་འགོག་པའོ་ཞེས་བྱ་བ་ལ་སོགས་པས་དོན་འདི་རྒྱས་པར་གསུངས་སོ། །

[Block 1074]
འཕགས་པ་སངས་རྒྱས་ཀྱི་ཡུལ་ལ་འཇུག་པ་ཡེ་ཤེས་སྣང་བའི་རྒྱན་གྱི་མདོ་ལས་ཀྱང་ཇི་སྐད་དུ།

[Block 1075 [VERSE]]
དེ་བཞིན་གཤེགས་པ་རྟག་ཏུ་སྐྱེ་མེད་ཆོས། །
ཆོས་རྣམས་ཐམས་ཅད་དེ་བཞིན་གཤེགས་དང་འདྲ། །
བྱིས་པའི་བློ་ཅན་ལོག་པར་འཁྲུལ་པ་རྣམས། །
འཇིག་རྟེན་དག་ན་མེད་པའི་ཆོས་ལ་སྤྱོད། །

[Block 1076]
ཅེས་གསུངས་པ་དང་། འཕགས་པ་ཟླ་བ་སྒྲོན་མ་ལས་ཀྱང་།

[Block 1077 [VERSE]]
ཐམས་ཅད་སྟོང་པའི་རང་བཞིན་དོན་དམ་ནི། །
ཆོས་ཅན་མི་དམིགས་ཆོས་ཉིད་ཡོད་པ་མིན། །
ཞེན་པ་བཟློག་ཕྱིར་རྐྱེན་བཤད་མ་རྟོགས་པ། །
ཆོས་ཀྱི་ངང་ལ་ཚིག་མེད་བརྗོད་དུ་མེད། །

[Block 1078]
ཅེས་གསུངས་སོ། །

[Block 1079]
འཕགས་པ་འདུལ་བ་རྒྱ་མཚོ་ལས་ཀྱང་།

[Block 1080 [VERSE]]
སྔོན་གྱི་མཐའ་སྟོང་ཕྱི་མའི་མཐའ་ཡང༌[^587]སྟོང་། །
སྲིད་པ་ཐམས་ཅད་ཡོང་ཡེ་སྟོང་པ་སྟེ། །
ཕྱོགས་གཅིག༌[^588]སྟོང་པ་མུ་སྟེགས་ཅན་རྣམས་ཀྱི། །

[Block 1081]
ཞེས་གསུངས་སོ། །

[Block 1082]
འཕགས་པ་ལང་ཀར་གཤེགས་པ་ལས་ཀྱང་།

[Block 1083 [VERSE]]
ཀུན་རྫོབ་ཏུ་ནི་ཐམས་ཅད་ཡོད། །
དམ་པའི་དོན་དུ་རང་བཞིན་མེད། །
རང་བཞིན་མེད་ལ་འཁྲུལ་པ་གང་། །
དེ་ནི་ཡང་དག་ཀུན་རྫོབ་བཤད། །

[Block 1084]
ཅེས་གསུངས་སོ། །

[Block 1085]
འཕགས་པ་ཤེས་རབ༌[^589]ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་རབ་ཀྱི་རྩལ་གྱིས༌[^590]རྣམ་པར་གནོན་པ་ལས་ཀྱང་། དེ་བཞིན་གཤེགས་པའི་ཡེ་ཤེས་ཀྱིས༌[^591]ནི་ཅི་ཡང་མི་གཟིགས་ཏེ། དེ་ཅིའི་ཕྱིར་ཞེ་ན། འདི་ལྟར་ཡེ་ཤེས་ལ་ཡུལ་མི་མངའ་བའི་ཕྱིར་རོ་ཞེས་གསུངས་པ་དང་། འཕགས་པ་རྒྱལ་བ་སྐྱེད་མར་མཛད་པ་ཆེན་པོ་ལས་ཀྱང་། དེ་བཞིན་གཤེགས་པ་མི་འཁྲུགས་པའི༌[^592]ཞིང་གི་ཁྱད་པར་བརྗོད་པར་མཛད་པས་འཁོར་རྣམས་ཀྱིས༌[^593]བཅོམ་ལྡན་འདས་ལ་བཅོམ་ལྡན་འདས་དེ་བཞིན་གཤེགས་པ་མི་འཁྲུགས་པའི༌[^594]ཞིང་དེ་བདག་ཅག་ལ་བསྟན་དུ་གསོལ་ཞེས་ཞུས་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས༌[^595]འཇིག་རྟེན་གྱི་ཁམས་དེ་བསྟན་པར་མཛད་ནས་ཕྱིར་ཡང་མི་སྣང་བར་མཛད་དོ། །

[Block 1086]
བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ཇི་ལྟར་དེ་བཞིན་གཤེགས་པ་མི་འཁྲུགས་པའི༌[^596]ཞིང་དེ་མིག་ལམ་དུ་མི་སྣང་བ་བཞིན་དུ་གཟུགས་མིག་ལམ་དུ་མི་སྣང་བའོ། །

[Block 1087]
ཚོར་བ་མིག་ལམ་དུ་མི་སྣང་བའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་རྒྱས་པར་གསུངས་སོ། །

[Block 1088]
དོན་འདི་འཕགས་པ་རྟག༌[^597]ཏུ་ངུའི་ལེའུ་ལས་ཀྱང་གསལ་བར་གསུངས་སོ། །

[Block 1089]
དེ་བཞིན་དུ་རྒྱལ་པོ་མ་སྐྱེས་དགྲའི་འགྱོད་པ་བསལ་བའི༌[^598]མདོ་ལས་ཀྱང་དོན་འདི་གསལ་བར༌[^599]གསུངས་སོ། །

[Block 1090]
གཞན་ཡང་འཕགས་པ་ཡབ་དང་སྲས་མཇལ་བའི་མདོ་དང་། འཕགས་པ་སོར་མོའི༌[^600]ཕྲེང་ཅན་གྱི་མདོ་དང་། འཕགས་པ་ཡེ་ཤེས་ཀྱི་ཕྱག་རྒྱའི་མདོ་དང་། དེ་བཞིན་གཤེགས་པའི༌[^601]གསང་བའི་མདོ་དང་། དེ་བཞིན་གཤེགས་པ་འཕགས་པ་དྲི་མ་མེད་པར་གྲགས་པའི་མདོ་དང་། འཕགས་པ་སངས་རྒྱས་རྗེས་སུ་དྲན་པའི་མདོ་དང་། འཕགས་པ་ནམ་མཁའ་མདོག་གིས༌[^602]འདུལ་བའི་མདོ་དང་། འཕགས་པ་དེ་བཞིན་གཤེགས་པའི་མཛོད་ཀྱི་མདོ་དང་། འཕགས་པ་སུམ་ཅུ་རྩ་གསུམ་གྱི་མདོ་དང་། འཕགས་པ་འོད་སྲུངས་ཀྱིས་ཞུས་པའི་མདོ་དང་། འཕགས་པ་ཆོས་ཐམས་ཅད་འབྱུང་བ་མེད་པ༌[^603]བསྟན་པའི་མདོ་དང་། འཕགས་པ་དེ་བཞིན་གཤེགས་པའི་སྙིང་པོ་བསྟན་པའི་མདོ་དང་། འཕགས་པ་ཏིང་ངེ་འཛིན་གྱི་རྒྱལ་པོའི་མདོ་དང་། འཕགས་པ་ད་ལྟར་གྱི༌[^604]སངས་རྒྱས་མངོན་དུ་བཞུགས༌[^605]པའི་མདོ་དང་། འཕགས་པ་སྐུ་གསུམ་བསྟན་པའི་མདོ་དང་། འཕགས་པ་དྲི་མ་མེད་པས་བྱིན་པས་ཞུས་པའི་མདོ་དང་། འཕགས་པ་བུ་མོ་བློ་གྲོས་བཟང་མོས་ཞུས་པའི་མདོ་དང་། འཕགས་པ་བུ་མོ་རྣམ་དག་དང་བས་ཞུས་པའི་མདོ་དང་། འཕགས་པ་ཆོས་ཉིད་རང་གི་ངོ་བོ་ཉིད་ལས་མི་གཡོ་བས་ཐ་དད་པར་བསྟན་པའི་མདོ་དང་། འཕགས་པ་ལང་ཀར་གཤེགས་པ་དེ་ཉིད་དང་། འཕགས་པ་བདེན་པ་གཉིས་བསྟན་པའི་མདོ་དང་། འཕགས་པ་ནམ་མཁའི་སྙིང་པོའི་མདོ་དང་། འཕགས་པ་ཀླུའི་རྒྱལ་པོ་མ་དྲོས་པས་ཞུས་པའི་མདོ་དང་། འཕགས་པ་ཀླུའི་རྒྱལ་པོ་རྒྱ་མཚོས་ཞུས་པའི་མདོ་དང་། འཕགས་པ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་མདོ་མ་ལུས་པ་ཐམས་ཅད་དང་། འཕགས་པ་གསང་བ་བསམ་གྱིས་མི་ཁྱབ་པའི་མདོ་ལ་སོགས་པ་མདོ་སྡེ་ཐམས་ཅད་ནས་དོན་འདི་ཤིན་ཏུ་གསལ་བར་གསུངས་པས་མདོ་དེ་དང་དེ་ཉིད་དུ་བལྟ་བར་བྱའོ། །
--- END BLOCKS ---
