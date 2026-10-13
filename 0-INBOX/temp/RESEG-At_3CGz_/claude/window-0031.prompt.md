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
བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ཇི་ལྟར་དེ་བཞིན་གཤེགས་པ་མི་འཁྲུགས་པའི༌[^596]ཞིང་དེ་མིག་ལམ་དུ་མི་སྣང་བ་བཞིན་དུ་གཟུགས་མིག་ལམ་དུ་མི་སྣང་བའོ། །

[Block 1087]
ཚོར་བ་མིག་ལམ་དུ་མི་སྣང་བའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་རྒྱས་པར་གསུངས་སོ། །

[Block 1088]
དོན་འདི་འཕགས་པ་རྟག༌[^597]ཏུ་ངུའི་ལེའུ་ལས་ཀྱང་གསལ་བར་གསུངས་སོ། །

[Block 1089]
དེ་བཞིན་དུ་རྒྱལ་པོ་མ་སྐྱེས་དགྲའི་འགྱོད་པ་བསལ་བའི༌[^598]མདོ་ལས་ཀྱང་དོན་འདི་གསལ་བར༌[^599]གསུངས་སོ། །

[Block 1090]
གཞན་ཡང་འཕགས་པ་ཡབ་དང་སྲས་མཇལ་བའི་མདོ་དང་། འཕགས་པ་སོར་མོའི༌[^600]ཕྲེང་ཅན་གྱི་མདོ་དང་། འཕགས་པ་ཡེ་ཤེས་ཀྱི་ཕྱག་རྒྱའི་མདོ་དང་། དེ་བཞིན་གཤེགས་པའི༌[^601]གསང་བའི་མདོ་དང་། དེ་བཞིན་གཤེགས་པ་འཕགས་པ་དྲི་མ་མེད་པར་གྲགས་པའི་མདོ་དང་། འཕགས་པ་སངས་རྒྱས་རྗེས་སུ་དྲན་པའི་མདོ་དང་། འཕགས་པ་ནམ་མཁའ་མདོག་གིས༌[^602]འདུལ་བའི་མདོ་དང་། འཕགས་པ་དེ་བཞིན་གཤེགས་པའི་མཛོད་ཀྱི་མདོ་དང་། འཕགས་པ་སུམ་ཅུ་རྩ་གསུམ་གྱི་མདོ་དང་། འཕགས་པ་འོད་སྲུངས་ཀྱིས་ཞུས་པའི་མདོ་དང་། འཕགས་པ་ཆོས་ཐམས་ཅད་འབྱུང་བ་མེད་པ༌[^603]བསྟན་པའི་མདོ་དང་། འཕགས་པ་དེ་བཞིན་གཤེགས་པའི་སྙིང་པོ་བསྟན་པའི་མདོ་དང་། འཕགས་པ་ཏིང་ངེ་འཛིན་གྱི་རྒྱལ་པོའི་མདོ་དང་། འཕགས་པ་ད་ལྟར་གྱི༌[^604]སངས་རྒྱས་མངོན་དུ་བཞུགས༌[^605]པའི་མདོ་དང་། འཕགས་པ་སྐུ་གསུམ་བསྟན་པའི་མདོ་དང་། འཕགས་པ་དྲི་མ་མེད་པས་བྱིན་པས་ཞུས་པའི་མདོ་དང་། འཕགས་པ་བུ་མོ་བློ་གྲོས་བཟང་མོས་ཞུས་པའི་མདོ་དང་། འཕགས་པ་བུ་མོ་རྣམ་དག་དང་བས་ཞུས་པའི་མདོ་དང་། འཕགས་པ་ཆོས་ཉིད་རང་གི་ངོ་བོ་ཉིད་ལས་མི་གཡོ་བས་ཐ་དད་པར་བསྟན་པའི་མདོ་དང་། འཕགས་པ་ལང་ཀར་གཤེགས་པ་དེ་ཉིད་དང་། འཕགས་པ་བདེན་པ་གཉིས་བསྟན་པའི་མདོ་དང་། འཕགས་པ་ནམ་མཁའི་སྙིང་པོའི་མདོ་དང་། འཕགས་པ་ཀླུའི་རྒྱལ་པོ་མ་དྲོས་པས་ཞུས་པའི་མདོ་དང་། འཕགས་པ་ཀླུའི་རྒྱལ་པོ་རྒྱ་མཚོས་ཞུས་པའི་མདོ་དང་། འཕགས་པ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་མདོ་མ་ལུས་པ་ཐམས་ཅད་དང་། འཕགས་པ་གསང་བ་བསམ་གྱིས་མི་ཁྱབ་པའི་མདོ་ལ་སོགས་པ་མདོ་སྡེ་ཐམས་ཅད་ནས་དོན་འདི་ཤིན་ཏུ་གསལ་བར་གསུངས་པས་མདོ་དེ་དང་དེ་ཉིད་དུ་བལྟ་བར་བྱའོ། །

[Block 1091]
འདིར་དེ་དག་གི་ཤློ་ཀ་བཀོད་ན་ནི་གཞུང་ཤིན་ཏུ་མངས་པར་འགྱུར་རོ། །

[Block 1092]
དེ་བས་ན་ཐེག་པ་ཆེན་པོའི་མདོ་སྡེ་མ་ལུས་པ་ཐམས་ཅད་བལྟ་བ་ལ་ཤིན་ཏུ་བརྩོན་པར་བྱའོ། །

[Block 1093]
གཞན་ཡང་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་སྙིང་པོའི་དོན་ཕྱིན་ཅི་མ་ལོག་པར་ཇི་ལྟ་བ་བཞིན་དུ་ཐུགས་སུ་ཆུད་པ༌[^606]སློབ་དཔོན་འཕགས་པ་ཀླུ་སྒྲུབ་དང་། སློབ་དཔོན་འཕགས་པ་ཨཱརྱ་དེ་བ་དང་། སློབ་དཔོན་འཕགས་པ་ཟླ་གྲགས་དང་། སློབ་དཔོན་འཕགས་པ་ཤཱན་ཏ་དེ་བ་དང་། སློབ་དཔོན་འཕགས་པ་བྷ་བྱ་སྣང་བྲལ་དང་། སློབ་དཔོན་རྟ་དབྱངས་དང་། སློབ་དཔོན་འཕགས་པ་དགེ་བསྙེན་ཟླ་བ་ལ་སོགས་པས་མཛད་པའི་གཞུང་དེ་དག་ནི་མདོའི་དོན་གསལ་བར་བཀྲོལ་བ་ཡིན་པས་དེ་དག་ཀྱང་ལེགས་པར་བལྟ་བ་ལ་བརྩོན་པར་བྱའོ། །

[Block 1094]
འདིར་དེ་དག་གི་གཞུང་བཀོད་པ༌[^607]ན་ནི་ཡི་གེ་ཤིན་ཏུ་མངས་པར་འགྱུར་རོ། །

[Block 1095]
འདི་ལྟར་འཕགས་པ་ཀླུ་སྒྲུབ་ནི་མདོ་སྡེ་ཕལ་ཆེ་བ་དང་། འཛམ་བུའི་གླིང་ན་མཁས་པ་དག་ཀྱང་འདི་སྐད་དུ་ས་དང་པོ་ལ་གནས་པའི་བྱང་ཆུབ་སེམས་དཔའ་ཡིན་ནོ་ཞེས་བརྗོད་ཅིང་གྲགས་མོད་ཀྱང་། བདག་གིས༌[^608]མདོའི་ནང་ནས་ས་བརྒྱད་པའི་བྱང་ཆུབ་སེམས་དཔའ་ཡིན་པར་ལེགས་པར་མཐོང་བ་ཡིན་ནོ། །

[Block 1096]
སློབ་དཔོན་ཨཱརྱ་དེ་བ་ཡང༌[^609]འཕགས་པ་ཀླུ་སྒྲུབ་ཀྱི་མན་ངག་གིས་ས་བརྒྱད་པ་ཐོབ་པའི་བྱང་ཆུབ་སེམས་དཔའ་ཡིན་པར་ལེགས་པར་མཐོང་ངོ་། །སློབ་དཔོན་ཟླ་གྲགས་ཀྱང་འཕགས་པ༌[^610]ཀླུ་སྒྲུབ་ཀྱི་མན་ངག་གིས་བདེན་པའི་བྱིན་གྱི་རླབས༌[^611]མངའ་བ་ཆོས་ཐམས་ཅད་སྒྱུ་མ་ལྟ་བུར་ཐུགས་སུ་ཆུད་པ་འཛམ་བུའི་གླིང་དུ་ལོ་བཞི་བརྒྱར་བཞུགས༌[^612]ནས་གཞན་གྱི་དོན་འབའ་ཞིག་མཛད་པ་ཡིན་ནོ། །

[Block 1097]
སློབ་དཔོན་ཤཱན་ཏ་དེ་བ་ཡང་འཕགས་པ་ཀླུ་སྒྲུབ་ཀྱི་མན་ངག་གིས༌[^613]འཕགས་པ་འཇམ་པའི་དབྱངས་ཀྱི་གནང་བ་ཐོབ་པར་བྱས་ཏེ་བདེན་པ་གཟིགས་པ་ཡིན་ནོ། །

[Block 1098]
སློབ་དཔོན་བྷ་བྱ་ཡང་འཕགས་པ་ཀླུ་སྒྲུབ་ཀྱི་མན་ངག་གིས་སྐུ་ཚེ་དེ་ཉིད་ལ་རིག༌[^614]འཛིན་གནས་སུ་གཤེགས་པ་ཡིན་ནོ། །

[Block 1099]
སློབ་དཔོན་རྟ་དབྱངས་ནི་སློབ་དཔོན་ཨཱརྱ་དེ་བའི་མན་ངག་གིས༌[^615]བདེན་པ་གཟིགས་པ་ཡིན་ནོ། །

[Block 1100]
འཕགས་པ་དགེ་བསྙེན་ཟླ་བ་ཡང་དེ་ལྟ་བུའོ། །

[Block 1101]
དེ་བས་ན་དེ་ལྟ་བུའི་ལུང་དང་རིགས་པ་རྒྱ་ཆེན་པོ་བསྟན་པ་དེ་དག་ཤེས་པར་བྱས་ཤིང་དེའི་དོན་ལ་ངེས་པར་བྱས་ཏེ། ཐེ་ཚོམ་མེད་པར་བྱས་ནས་ལྷག་མཐོང་ཞེས་བྱ་བ་རྣམ་པར་མི་རྟོག་པ་དེ་བསྒོམ་པར་བྱའོ། །ཇི་ལྟར༌[^616]བསྒོམ༌[^617]ཞེ་ན། རེ་ཞིག་དངོས་པོ་ནི་གཉིས་ཏེ། གཟུགས་ཅན་དང་གཟུགས་ཅན་མ༌[^618]ཡིན་པའོ། །

[Block 1102]
དེ་གཉིས་ཀ་ཡང་གཏན་ཚིགས་ཆེན་པོ་རྣམས་ཀྱིས་བསལ་ཏེ་བསྒོམ་པར་བྱའོ། །

[Block 1103]
དེ་ཡང་ཇི་སྐད་དུ་ཆོས་ཐམས་ཅད་སེམས་ལ་བསྡུས་ཤིང་། སེམས་ཀྱང་ལུས་ལ་བསྡུས་ལ། ལུས་ཀྱང་ཆོས་ཀྱི་དབྱིངས་སུ་གཏང་བ༌[^619]འདི་ནི་མན་ངག་གོ་ཞེས་བླ་མའི་ཞལ་ནས་ཏིང་ངེ་འཛིན་གྱི་ཚོགས་ཀྱི་ལེའུ་ལས་གསུངས་སོ། །

[Block 1104]
དེ་ལྟ་བུ་ལ༌[^620]ཤེས་པ་ཅིར་ཡང་མི་རྟོག །ཅིར་ཡང་མི་འཛིན། དྲན་པ་དང་ཡིད་ལ་བྱེད་པ་ཐམས་ཅད་སྤངས་ཏེ། ཇི་སྲིད་མཚན་མའི་དགྲ་མ་ལངས་པའི་བར་དེ་སྲིད་དུ་དེ་ལྟ་བུ་ལ་གནས་པར་བྱའོ། །

[Block 1105]
འཕགས་པ་ཀླུ་སྒྲུབ་ཀྱི་ཞལ་ནས།

[Block 1106 [VERSE]]
ཀུན་དུ་རྟོགས་པས༌[^621]མ་བརྟགས་ཤིང་། །
ཡིད་ནི་རབ་ཏུ་མི་གནས་ལ། །
དྲན་མེད་ཡིད་ལ་བྱེད་པ་མེད། །
དམིགས་མེད་དེ་ལ་ཕྱག་འཚལ་ལོ། །

[Block 1107]
ཞེས་གསུངས་སོ། །

[Block 1108]
[^622]འཕགས་པ་ཀླུ་སྒྲུབ་ཀྱི་ཞལ་ནས།

[Block 1109]
མཁས་པ་སྟོང་པ་ཉིད་ལ་ཡང་། །སྟོང་པ་ཉིད་དུ་བལྟ་མི་འགྱུར། །

[Block 1110]
ཞེས་གསུངས་སོ། །

[Block 1111]
ཡང་།

[Block 1112 [VERSE]]
དམིགས་པ་དང་ནི་བྲལ་བའི་སེམས། །
ནམ་མཁའི་མཚན་ཉིད་ལ་གནས་ཏེ། །
ནམ་མཁའ་སྒོམ་པར་བྱེད་པ་ནི། །
སྟོང་པ་ཉིད་ནི་སྒོམ་པའོ། །

[Block 1113]
ཞེས་གསུངས་སོ། །

[Block 1114]
སློབ་དཔོན་ཞི་བ་ལྷའི་ཞལ་ནས།

[Block 1115 [VERSE]]
གང་ཚེ་ཡོད་དང་མེད་པ་གཉིས། །
བློ་ཡི་མདུན་ན་མི་གནས་པ། །
དེ་ཚེ་རྣམ་པ་གཞན་མེད་པས། །
དམིགས་པ་མེད་པས༌[^623]རབ་ཏུ་ཞི། །

[Block 1116]
ཞེས་གསུངས་སོ། །

[Block 1117]
གོམས་ན་ནི་དེའི་སྟོབས་སུ་འགྱུར་ཏེ། སློབ་དཔོན་ཞི་བ་ལྷའི་ཞལ་ནས།

[Block 1118]
སྟོང་པ་ཉིད་ལ་གོམས་པ་ཡིས། །དངོས་པོའི་བག་ཆགས་སྤོང་བར་འགྱུར། །

[Block 1119]
ཞེས་གསུངས་པ་དང་། སློབ་དཔོན་དཔལ་སྦས་ཀྱིས་ཀྱང་།

[Block 1120 [VERSE]]
འགའ་ཞིག་བསྒོམ་པ་གོམས་པ་ཡི། །
མཐུ་ཡིས༌[^624]ཆོས་ཀུན་ངོ་བོ་ཉིད། །
མེད་པ་དེ་ཡི་བདག་ཉིད་དུ། །
འགྱུར་ཏེ་དངོས་པོ་མཐོང་བ་བཞིན། །

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
--- END BLOCKS ---
