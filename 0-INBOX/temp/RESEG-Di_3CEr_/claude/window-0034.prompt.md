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
ཁས་བླངས་པའི་གཏན་ཚིགས་ལ་འགལ་བའི་སྐྱོན་འབའ་ཞིག་ཏུ་ནི་མ་ཟད་ཀྱི་འདི་ལྟར། མ་ངེས་པར་ཡང་འགྱུར། ཁས་བླངས་ཀྱང་ཤིང་ལ་སོགས་པ་ཤིང་ཤུན་ལ་སོགས་པ་རྣམས་ཀྱི་སྔོན་དུ་འགྲོ་བ་ཅན་ཉིད་ཀྱི་གཏན་ཚིགས་ལ་ངེས་པའི་སྐྱོན་ཡིན་ནོ། །

[Block 1192]
དེ་ལྟ་ན་ནི་ཤིང་ཤུན་དང་གྱོ་མོ་དང་ཁམ་ཕོར་དང་རྒྱན་ལ་སོགས་པ་ཐམས་ཅད་བདེ་བ་ལ་སོགས་པའི་རིགས་དང་ལྡན་པ་དང་དུ་མ་སྔོན་དུ་འགྲོ་བ་ཅན་ཡང་ཡིན་ནོ། །

[Block 1193]
དེ་ལྟར་ན་རེ་ཞིག་གཏན་ཚིགས་ཀྱི་སྐྱོན་གསུམ་ཀའོ། །

[Block 1194]
ཡང་གང་གི་ཕྱིར་གཅིག་སྔོན་དུ་སོང་བ་ཅན་གྱི་ཐ་དད་པ་རྣམས་སོ་ཞེས་དམ་བཅས་པ༌[^909]དེའི་ཕྱིར། དཔེ་ནི། བསྒྲུབ་བྱས་འཕངས༌[^910]འགྱུར། ཐམས་ཅད་ཀྱི་སྔོན་དུ་གཙོ་བོ་འགྲོ་བ་ཅན་ཉིད་དུ་ཁས་བླང་བར༌[^911]མི་བྱ་སྟེ། ཤིང་གི་ཤུན་ལྤགས་ལ་སོགས་པའི་སྔོན་དུ་ཤིང་ལ་སོགས་པ་སོང་བར་སྦྱར་བར་བྱའོ། །

[Block 1195]
དེ་ཡོད་མིན། དཔེ་དེ་ཡང་ཡོད་པ་མ་ཡིན་ཏེ། ཤིང་ཤུན་ལ་སོགས་པ་རྣམས་ཐ་དད་དུ་ཡོད་པའི་ཕྱིར་དང་། དེ་དག་ནི་བསྒྲུབ་པར་བྱ་བ་ནི་གཅིག་སྔོན་དུ་འགྲོ་བ་ཅན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1196]
དེ་བཞིན་དུ་ཡན་ལག་ལྷག་མ་རྣམས་ཀྱི༌[^912]རྣམ་པར་ལྡན་པ་ཡང་འབྲེལ་པ་ཉིད་དུ་རིགས་སོ་ཞེས་རིག་པར་བྱའོ། །

[Block 1197]
ཀུན་གྱི་རྗེས་ཐོག༌[^913]མ་

[Block 1198 [HEADING]]
##### བསལ་ཏེ་འོངས་པ། ^3-3-4-2-0

[Block 1199]
ལས་བསལ་ཏེ་འོངས་པ་འགྲུབ་བོ་ཞེས་པ་ལ༌[^914]གཞན་གྱི་འདོད་པ་སོ་སོར་བཀག་ནས་རང་གི་ཕྱོགས་ཡོངས་སུ་གཟུང་བའི་བྱ་བ་ནི་བསལ་ཏེ་འོངས་པའོ་ཞེས་གྲག་གོ། །

[Block 1200]
སོ་སོར་འགེགས་པའི་ཐབས་ནི་གཉིས་ཏེ། དཔེ་དང་འགལ་བ་དང་། ཁས་བླངས་པ་དང་འགལ་བ་ཞེས་སོ། །

[Block 1201]
དེ་ལ་གཞན་གྱི་ཕྱོགས་བཀག་པ་ཙམ་གྱིས་ནི་རང་གི་ཕྱོགས། གྲུབ་མིན། གཞན་ཕྱོགས་བཀག་པ་ཙམ་གྱིས་རང་གི་ཕྱོགས་གྲུབ་པ་ནི་མཐོང་ངོ་། །འདི་ལྟར་འདིར་ལུས་ཅན་མ་ཡིན་པའི་ཕྱིར་སྒྲ་རྟག་གོ་ཞེས་པ་ནི་མ་ངེས་པ༌[^915]ཡིན་ནོ་ཞེས་བྱ་བ་ཙམ་གྱིས་གཞན་གྱི་ཕྱོགས་མ་གྲུབ་པར་བྱས་མོད་ཀྱི། གྲུབ་མིན་ཏེ་རང་གི་ཕྱོགས་གྲུབ་པ་མ་ཡིན་ནོ། །

[Block 1202]
དེ་ཙམ་གྱི༌[^916]སྒྲ་མི་རྟག་པ་གྲུབ་པ་ནི་མ་ཡིན་ཏེ། དེ་ལ་ཡང་མ་ངེས་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1203]
གང་དུ་ཆུ་ཀླུང་གང་བ་ལ་གངས་ཞུ་བ་ལ་སོགས་པའི་རྒྱུ་མཚན་སོ་སོར་བཀག་པས་ཆར་འབབ་པའི་རྒྱུ་མཚན་ཅན༌[^917]དུ་རྟོགས་པ་འདི་ནི་བཀག་པ་ཙམ་ལས་མ་ཡིན་ཏེ། འོན་ཀྱང་རང་གི་ངོ་བོའི་ཁྱད་པར་ལས་ཡིན་ནོ། །

[Block 1204]
དེ་ནི་གངས་ཞུ་བ་ལ་སོགས་པ་སོ་སོར་བཀག་པས་ཆུ་ཀླུང་གང་བ་ཉིད་ཁྱད་པར་དུ་བྱས་པ་ཡིན་ནོ། །

[Block 1205]
འོ་ན་ཆར་འབབ་པའི་འཁྲུལ་པ་སོ་སོར་བཀག་པ་ཙམ་གྱིས་ཐོག་ལ་སོགས་པའི་རྒྱུ་མཚན་དུ་ཡང་འགྱུར་རོ། །

[Block 1206]
འདི་ཡང་རིགས་པ་མ་ཡིན་ཏེ། གཞན་གྱི་ཕྱོགས་འགེགས་པའི་ཐབས་ནི་རྣམ་པ་གཉིས་སོ་ཞེས་བྱ་བ་འདི་ལ། འགེགས་པའི་གཏན་ཚིགས་གཉིས་མ་ཡིན། །འགེགས་པ་ནི་ཐབས་གཉིས་འབའ་ཞིག་གི་སྒོ་ནས་མ་ཡིན་གྱི་འདི་ལྟར་ཡན་ལག་མ་ཚང་བའི་སྐྱོན་བསྟན་པ་ལས་ཀྱང་མ༌[^918]ཡིན་ནོ། །

[Block 1207]
དེ་ལྟར་རེ་ཞིག་བསལ་ཏེ་འོངས་པའི་མཚན་ཉིད་རིགས་པ་མ་ཡིན་ནོ། །

[Block 1208 [HEADING]]
##### སྦྱོར་བ་གཉིས། ^3-3-4-3-0

[Block 1209]
སྦྱོར་བ་གཉིས་ཀྱང་རིགས་མ་ཡིན། །ཇི་ལྟར་བྱས་ནས་ཤེ་ན། དེ་ལ་རེ་ཞིག་རྗེས་སུ་འགྲོ་བ༌[^919]བསལ་ཏེ་འོངས་པ་ནི་གལ་ཏེ་མེད་པ་གཏན་ནས་འབྱུང་བའི་སྐྱེ་གནས་མེད་པའི་ཕྱིར་ཐ་དད་དུ་ཐལ་བར་འགྱུར་རོ་ཞེས་བྱ་བ་འདིས་ནི་སྐྱེ་གནས་སྔོན་དུ་མ་སོང་བ་ཅན་རྣམས་ཐ་མི་དད་པ་ཉིད་དུ་དམིགས་པར་ཐལ་བར་འགྱུར་ཞེས་བྱས་པ་ཡིན་ནོ། །

[Block 1210]
རིགས་གཅིག་གི་རྗེས་སུ་འགྲོ་བ་མ་དམིགས་པ་ཡང་དེ་ལས་བཟློག་པ་ཉིད་ལ་སྒྲོ་འདོགས་པར་འགྱུར་རོ། །

[Block 1211]
དེ་ལ་རེ་ཞིག་སྐྱེ་གནས་སྔོན་དུ་སོང་བ་ཅན་གྱི་ཐ་མི་དད་ནི་འགལ་ཡང་འདོད་པ་མ་ཡིན་ལ་སྐྱེ་གནས་སྔོན་དུ་སོང་བ་ཅན་རྣམས་ཀྱི་རིགས་གཅིག་གི་རྗེས་སུ་འགྲོ་བ་བསྟན་པ་ཙམ་གྱིས་དེ་ཕྱིན་ཅི་ལོག་ཏུ་ཐལ་བར་འགྱུར་བ་ཡང་རིགས་པ་མ་ཡིན་ནོ། །

[Block 1212]
ཐ་དད་མ་བསྟན་པས་རིགས་གཅིག་གི་རྗེས་སུ་འགྲོ་བར་ཐལ་བར་འགྱུར་བ་ཡང་མ་ཡིན་ནོ། །

[Block 1213]
གལ་ཏེ་ཉེས་པ་མེད༌[^920]དེ། སྐྱེ་གནས་མེད་པའི་ཕྱིར་གཅིག་ཉིད་དུ་ཐལ་བར་འགྱུར་རོ་ཞེས་བརྗོད་དོ་ཞེ་ན། དེ་སྐད་དུ་བརྗོད་ན་རིགས་པར་ནི་མ་བརྗོད་དེ་ཐ་དད་རྣམས་ལ་རིགས་གཅིག་གི༌[^921]རྗེས་སུ་འགྲོ་བ་ཡོད་པ་མ་ཡིན་པས་གང་། ཐལ་བ་བརྗོད་པ་ནི་ཅི་ཡང་མ་ཡིན་ནོ། །

[Block 1214]
གལ་ཏེ་གཅིག་ཉིད་ལ་མཐའ་གཅིག་ཏུ་ངེས་པ་འགེགས་པ་ཡིན་ནོ་ཞེ་ན། མ་ཡིན་ཏེ། དེའི་ཡང་མ་བསྟན་པས་ན་བཟློག་པ་ཐོབ་པར༌[^922]ཡང་འགྱུར་རོ། །

[Block 1215]
གཅིག་ཉིད་ལ་མཐའ་གཅིག་ཏུ་ངེས་པ་ཡང་སྐྱེ་གནས་སྔོན་དུ་མ༌[^923]སོང་བ་རྣམས་ལ་མ༌[^924]མཐོང་བས་ན་སྤྱི་དང་བྱེ་བྲག་ཉིད་འཐོབ་པར་འགྱུར་རོ། །

[Block 1216]
སྣ་ཚོགས་ཀྱི་རྗེས་སུ་འགྲོ་བ་དང་བསལ་ཏེ་འོངས་པ་དག་ཀྱང་ཐ་མི་དད་དུ་ཐལ་བར་འགྱུར་རོ། །

[Block 1217]
དེ་ལ་མཐའ་གཅིག་ཏུ་ངེས་པ་ཡོད་པ་མ་ཡིན་པས་ཐ་དད་དུ་སྦྱར་བར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 1218]
དེའི་ཕྱིར་གཏན་ཚིགས་མ་བསྟན་པ་ཙམ་གྱིས་དེ་བཟློག་པར་ཐལ་བར་འགྱུར་བ་ནི་མ་ཡིན་ནོ། །

[Block 1219]
བསྒྲུབ་བྱ་བཟློག་པ་ལ་ནི་རིགས་པ་ཡིན་ནོ། །

[Block 1220]
འདི་ལྟར་འགྱུར་ཏེ་ཐ་མི་དད་པ་རྣམས་ཀྱི་སྔོན་དུ་གཅིག་སོང་བ་ནི་མཐའ་གཅིག་ཏུ་ངེས་པ་ཡིན་པའི༌[^925]ཕྱིར་དེ་ལས་བཟློག་པ་ཐ་དད་དུ་ཐལ་བར་འགྱུར་རོ། །

[Block 1221]
དེ་ལྟ་ན་ཡང་། རྗེས་ཐོག༌[^926]མ་ནི་བཟློག་པ་ལ། །དེ་ལྟར་དུ་གྱུར་ན་ཡང་རིགས་གཅིག་པ་ཅན་རྣམས་ཀྱི་སྔོན་དུ༌[^927]གཅིག་སོང་བ་ཅན་ཉིད་དུ་རྗེས་སུ་དཔོག་པ་ལ་རྗེས་ཐོག༌[^928]མ་ལས་མེད་པ་སྔོན་དུ་སོང་བ་ཅན་ལ་སོགས་པ་ཉིད་ནི་ཐ་དད་དུ་ཐལ་བར་འགྱུར་ཏེ། རྗེས་ཐོག༌[^929]མ་ལས་གཅིག་ཏུ༌[^930]སོང་བ་ཅན་དུ་རྗེས་སུ་དཔག་པ་ནི་མ་ཡིན་ནོ། །

[Block 1222]
དེ་ལ་ཡང་ཐ་དད་དུ་ཐལ་བར་འགྱུར་རོ།[^931] །

[Block 1223]
བརྗོད་པ་དེ་ནི༌[^932]ཐ་དད་རྣམས་རིགས་གཅིག་གི་རྗེས་སུ་འགྲོ་བ་ཅན་དུ་བརྗོད་པའི༌[^933]ཕྱིར་འདི་རྣམ་པར་ལྡན་པ་ལས་ཐ་དད་དུ་དབྱེ་བར་བྱ་བ་ཡིན་ནོ། །

[Block 1224]
སྦྱོར་བ་ཡང་འདི་ལྟར་འཐད་པ་ཡིན་ཏེ། གལ་ཏེ་བསལ་བ༌[^934]ཉིད་གཅིག་ལས་སྐྱེ་བ་མ་ཡིན་ན་སྐྱེ་གནས་མེད་པའི་ཕྱིར་ཐ་དད་དུ་ཐལ་བར་འགྱུར་ཏེ། རིགས་གཅིག་པ་ཅན་མེད་པར་ཐལ་བར་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1225]
འདི་ལྟར་རིགས་གཅིག་དང་རྗེས་སུ་འབྲེལ་བ་རྣམས་གཅིག་སྔོན་དུ་འགྲོ་བ་ཅན་ཉིད་དུ་མཐོང་གི །མེད་པ་སྔོན་དུ་འགྲོ་བ་ཅན་ཉིད་དུ་ནི་མ་ཡིན་ལ།[^935] དབང་ཕྱུག་ལ་སོགས་པའི་སྔོན་དུ་འགྲོ་བ་ཅན་ཉིད་དུ་ཡང་མ་ཡིན་ནོ། །

[Block 1226]
རྗེས་ཐོག༌[^936]མ་ལས་བསལ༌[^937]ཏེ་འོངས་པར་སྨྲ་བ་ཡང་། གཅིག་བསལ་བ༌[^938]ལ་འདི་མི་རིགས། །དེ་ལྟ་བུའི་སྦྱོར་བ་རིགས་པ་མ་ཡིན་ལ་མེད་པ་ལས་སྐྱེ་བ་ལ༌[^939]རྗེས་ཐོག༌[^940]མས་གཙོ་བོ་ལས་སྐྱེ་བ་ཞེས་བྱ་བ་ཡང་རིགས་པ་མ་ཡིན་ནོ། །

[Block 1227]
གཞན་ཡང་། རྣམ་ལྡན་བཞིན་དུ་ལྔ་ཉིད་མིན། །བསལ་ཏེ་འོངས་པ་རྣམས་ཀྱི་ལྔ་ཉིད་ནི་སྦྱར་བར་བྱ་བ༌[^941]ཡིན་ནོ། །

[Block 1228]
དེ་ལྟར་ན་རྗེས་ཐོག༌[^942]མའི་མཚན་ཉིད་ལས་འབྲེལ་པ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1229]
འདི་ལྟར་གཞན་གྱི་ཕྱོགས་ཐམས་ཅད་བཀག་པས་ཀུན་གྱི་རྗེས་ཐོག༌[^943]མ་ལས་གཅིག་ཉིད་བསལ་ཏེ་འོངས་པའོ་ཞེས་སྦྱར་བར་བྱའོ། །

[Block 1230 [VERSE]]
རྒོལ་བ་རེ་རེ་བཀག་པ་ལས། །
གལ་ཏེ་རྗེས་ཐོག༌[^944]མར་འདོད་ན། །
རྒོལ་བའི་ལན་ལ་མཐའ་མེད་ཉིད། །
བསལ༌[^945]འོངས་རྣམས་སུ་ཐལ་བར་འགྱུར། །
--- END BLOCKS ---
