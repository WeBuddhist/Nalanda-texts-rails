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
[Block 1226 [VERSE]]
མངོན་སུམ་དང་ནི་རྗེས་དཔག༌[^860]དང་། །
སྒྲ་ལས་བྱུང་བ་དཔེ་དང་བཅས། །
དོན་གྱི་ཤུགས་དང་མེད་ཉིད་དང་། །
སྲིད་དང་ཡོད་སྙམ་དེ་བཞིན་ཏེ། །

[Block 1227]
ཞེས་བཤད་པས་སོ། །

[Block 1228]
ཚད་མ་དེ་རྣམས་ཀྱིས་དངོས་པོ་རྣམས་ལ་སྤྱི་དང་ཁྱད་པར་དུ་འཇོག་པར་བྱེད་དོ། །

[Block 1229]
མཆོད་སྦྱིན་ལ་སོགས་པ་སྲོག༌[^861]གཅོད་པ་དང་བཅས་པས་ཀྱང་མཐོ་རིས་དང་ཐར་པ་དག་འདོད་དོ། །

[Block 1230]
དེ་ཡང་མི་རིགས་ཏེ། དེ་རྣམས་ཀྱི་རིགས་སམ། གསལ་བའམ་སྤྱི༌[^862]དང་ལྡན་པའམ་དེའི་འབྲེལ་པའི་སྒྲ་དོན་ཡིན་ཞེ་ན། དེ་ལ་སྤྱི་ཞེས་བྱ་བ་གང་ཡང་དངོས་པོ་ལས་གུད༌[^863]ན་མེད་དེ་དམིགས་པའི་མཚན་ཉིད་དང་ལྡན་པ༌[^864]དེ་མི༌[^865]དམིགས་པའི་ཕྱིར་བུམ་པས་དབེན་པའི་ས་ཕྱོགས་བཞིན་ནོ།[^866] །

[Block 1231]
དེ་ལྟ་ན་གཅིག་གི་རྣམ་པ་རྟོག་པ་དང་སྒྲ་རྟོག་པར་བྱེད་པའི་རྒྱུ་ནི་སྤྱི་ཡིན་པས་ཁྱེད་ཀྱིས༌[^867]ཇི་ལྟར་སྦེད་པར་བྱེད་ཅེ་ན། དེ་ནི་བདེན་པ་མ་ཡིན་ཏེ་ཁྱད་པར་ཁོ་ན༌[^868]ཁྱད་པར་གཞན་ལས་ལོག་པས་རྣམ་པར་རྟོག་པ་དང་སྒྲ་གཅིག་ཏུ་སྐྱེད་པར་བྱེད་ཅེས་པར་གཅོད་པར་བྱེད་པ་དེས་ཅི་ཞིག་བྱའོ། །

[Block 1232]
ཁྱད་པར་རྣམས་ནི་སྒྲ་དང་རྣམ་པར་རྟོག་པས༌[^869]སོ་སོར་བསྟན་མི༌[^870]ནུས་པས་སྒྲ་དང༌[^871]ཤེས་པ་གཅིག་པ་ཉིད་དུ་སྐྱེད་པའི༌[^872]ནུས་པ་ཇི་ལྟར་འགྱུར་ཞེ་ན། སྨྲས་པ། ཁྱད་པར་གྱིས་ནི་འཇུག་པ་གཙོ་བོ་སྒྲ་དང་རྣམ་པར་རྟོག་པ་སྐྱེད་པར་མི་ནུས་ཏེ། འོན་ཀྱང་རྟོག་བཅས་ཀྱི་རྣམ་པར་ཤེས་པ་ལ་སོ་སོར་སྣང་བའི་སྤྱི་ཙམ་གྱིས་སོ། །

[Block 1233]
དེ་བས་ཇི་སྐད་དུ།

[Block 1234 [VERSE]]
བྱེ་བྲག་གཞན་ནི་སོ་སོར་བཀག །
མ་བཀག་པ་དང་དེ་དག་གི། །
བརྡ་ཡི་བྱེ་བྲག་གནས་ཡིན་ཏེ། །
ཤེས་པ་པོ་ཡི་འདོད་དོར་རོ། །

[Block 1235]
ཞེས་འབྱུང་ངོ་། །

[Block 1236]
དེའི་ཕྱིར་མེད་པའི་སྤྱི་ནི་ཁས་བླངས་ཏེ་ཇི་ལྟར་བདག་ཉིད་སྨོད་པར་བྱེད། དེ་བས་སྤྱི་མེད་དེ། [^873]ཁྱད་པར་ཡང་སྒྲའི་དོན་མ་ཡིན་ཏེ། ཁྱད་པར་ནི་དོན་གྱི་བྱ་བ་བྱེད་པ་འོན་ཀྱང་དེ་སྐད་ཅིག་མ་ཅན་ཡིན་པས་མི་གནས་པའི་ཆོས་ཅན་ནོ། །

[Block 1237]
གང་ལ་ངོ་བོ་ཉིད་ཀྱིས་གནས་པ་མེད་པ་དེ་ཉིད་དེ༌[^874]ཇི་ལྟར་རྣམ་པར་རྟོག་པའི་ཤེས་པའམ་སྒྲ་སྐྱེད་པར་ནུས་སོ། །

[Block 1238]
[^875]ཇི་སྐད་དུ། སྒྲ་ཡིས་མཚོན་ཆ་བཤད་པ་སྟེ།

[Block 1239 [VERSE]]
ཐ་སྙད་ཕྱིར་ནི་དེ་བཤད་དོ། །
དེ་ཚེ་རང་གི་མཚན་ཉིད་མེད། །
དེས་ན་དེ་ལ་བརྡ་ཡང་མེད། །

[Block 1240]
ཅེས་འབྱུང་ངོ་། །འདི་ལ་འདི་ལྟར་དཔྱད་པར་བྱ་སྟེ། ཅི་རྟོག་པ་དང་བཅས་པའི་ཤེས་པ་དང་སྒྲ་དག་ལས་ཁྱད་པར་སྔོན་དུ་འབྱུང་བའམ་ཁྱད་པར་ལས་ཀྱང་སྔོན་དུ་རྣམ་པར་རྟོག་པའི་ཤེས་པ་དང༌[^876]སྒྲ་དག་འབྱུང་ངམ་ཅི། ལྷན་ཅིག་ཏུ་སྐྱེས་པ་རྣམ་པར་རྟོག་པའི་ཤེས་པ་དང་སྒྲ་དང༌[^877]ཁྱད་པར་རྣམས༌[^878]ཡིན་ནམ། གལ་ཏེ་ཁྱད་པར་དང་པོ་སྐྱེས་ན་དེའི་ཚེ་དེ་གང་གི་ཡུལ་ཡིན། ཡང་ན་ཕྱིས་སྐྱེས་པ་ཡིན་ན་རྣམ་པར་རྟོག་པ་དང་སྒྲ་དག་གི་ཁྱད་པར་དང་ལྷན་ཅིག་ཏུ་ཕན་ཚུན་འབྲེལ་པ་མེད་དོ། །

[Block 1241]
རྒྱུ་དེ་དག་གིས་རྒྱུ་དང་འབྲས་བུ་འབྲེལ་པ་ནི་ཚད་མ་མ་ཡིན་ཏེ། འཁྲུལ་པ་དང་མ་ངེས་པའི་ཕྱིར་རོ། །

[Block 1242]
ཁྱད་པར་སྒྲ་དང་རྣམ་པར་རྟོག་པ་རྣམས་ལྷན་ཅིག་ཏུ་འབྱུང་བས་གང་གི༌[^879]གང་ཡུལ་ཡིན་ཞེས་ངེས་པ་མེད་དོ།[^880] །

[Block 1243]
མ་ངེས་པ་ལ་བརྗོད་པར་བྱ་བ་དང་རྗོད་པར་བྱེད་པའི་འབྲེལ་པ་མེད་དེ་གཽའུ་སྒྲ་དག་བཞིན་ནོ། །

[Block 1244]
གཞན་ཡང་གལ་ཏེ་ཁྱད་པར་སྒྲའི་དོན༌[^881]དུ་བརྟགས་ན་དེས༌[^882]མེའི་སྒྲ་བརྗོད་པའི་དུས་སུ་ཁ་ཚིག༌[^883]པར་འགྱུར་བ་དང་། བུམ་པ་བརྗོད་པའི་དུས་སུ་ཡང་བུམ་པས་ཁ་ཁེངས༌[^884]པར་འགྱུར་རོ། །

[Block 1245]
དེ་ལྟར་ནི་མ་མཐོང་སྟེ། དེའི་ཕྱིར་ན་ཁྱད་པར་ནི་སྒྲའི་དོན་མ་ཡིན་ནོ། །

[Block 1246]
སྤྱི་མེད་པས་སྤྱི་དང་ལྡན་པའང་མེད་དེ་ལྡན་པའི་སྒྲ་ནི་འབྲེལ་པ་བྱེད་པའི་ཚིག་ལས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 1247]
འབྲེལ་པ་ནི་སྤྱི་བཀག་པའི་སྒོ་ནས་སེལ་བ་ཡིན་ཏེ། གཉིས་ལས་འབྲེལ་པ་འདོད་པའི་ཕྱིར་རོ། །

[Block 1248]
དེའི་ཕྱིར་སྔར་བཤད་པའི་རིམ་པས་འབྲེལ་པ་རྟག་པར་བྱེད་ན་དངོས་པོ་རྣམས་ཀྱི་ཕན་ཚུན་འབྲེལ་པ་གང་ཡང་མེད་དེ་ཐམས་ཅད་རང་ཉིད་ལས་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 1249 [VERSE]]
དངོས་པོ་ཐམས་ཅད་རང་བཞིན་གྱིས། །
རང་རང་ངོ་བོར་གནས་པ་སྟེ། །
རང་དང་གཞན་གྱི་ངོ་བོ་ལས། །
གང་ཕྱིར་ལྡོག་པ་ལ་བརྟེན་པས། །

[Block 1250 [VERSE]]
དེ་ཕྱིར་དངོས་རྣམས་གང་གང་ལས། །
ལྡོག་པ་དེ་ཡི་རྒྱུ་མཚན་ནི། །
སྤྱི་ཡི་དབྱེ་བར་རབ་བརྟགས་པས། །
དེ་ཡི་ཁྱད་པར་གཟུང་བར་བྱེད། །

[Block 1251 [VERSE]]
དེ་ཕྱིར་གང་ཞིག་ཆོས་གཞན་གྱི།[^885] །
ཁྱད་པར་ཡང་དག་རྟོགས་འགྱུར་བ། །
དེ་ལས་གཞན་གྱིས༌[^886]དེ་མི་རིགས། །
དེས་ན་ཐ་དད་ཐ་སྙད་ཡིན། །

[Block 1252]
གཞན་དབང་ཉིད་དང་འབྲེལ་པ་ཡིན། །ཞེས་བྱ་བ་ལ་སོགས་པས་འབྲེལ་པ་མེད་པར་བཤད་དོ། །

[Block 1253]
དེ་ལྟར་སྤྱི་ལ་སོགས་པ་བཀག་པས་དཔྱོད་པ༌[^887]པ་རྣམས་ལ་སྒྲའི་དོན་ཉིད་མེད་དོ་ཞེས་དོན་གང་ལ་ཚད་མ་བརྒྱད་དོན་དང་ལྡན་པར་མི་འགྱུར་ཏེ་གཞལ་བྱ་མེད་པའི་ཕྱིར་རོ། །

[Block 1254]
གང་གི་ཕྱིར་ཚད་མ་ལས་གཞལ་བྱ་གྲུབ་ཅེས་བཤད་དོ། །

[Block 1255]
དེ་བས་ན་ཡུལ་མེད་པའི་སྒྲ་རྣམས་ཀྱིས་དོན་གང་རྗོད་པར་བྱེད་དོ།[^888] །

[Block 1256]
གཞན་ཡང་དཔྱོད་པ་པ་རྣམས་ཀྱི་སྒྲའི་དོན་མ་གྲུབ་པས་ཀྱང་ཁས་བླངས་ཏེ་ལན་སྨྲ་བར་བྱ་སྟེ། རེ་ཞིག་བྱ་བའི་ཕྱོགས་སུ་ནི་མཆོད་སྦྱིན་དང་ཁྲུས་དང་བརྟུལ་ཞུགས་དང་སྨྱུང་བ༌[^889]དང་དཀའ་ཐུབ༌[^890]ལ་སོགས་པའི་མཚན་ཉིད་མཐོ་རིས་དང་ཐར་པའི་འབྲས་བུ་ཐོབ་པའི་ཕྱིར། རྣམ་པར་འཚེ་བའི་བདག་ཉིད་ཀྱི་ལས་ར་གསོད་པ༌[^891]ལ་སོགས་པ་འགལ་བ་མི་རིགས་ཏེ། མཐོ་རིས་ནི་བདེ་བ་ལ་ལོངས་སྤྱོད་པའི་མཚན་ཉིད་དེ། བདེ་བ་སྦྱིན་པས་ཐོབ་པར་འགྱུར་གྱི་སྲོག་ཆགས་གསོད་པས་ནི་མ་ཡིན་ནོ། །

[Block 1257]
ཡང་ན་ཆོ་ག་མཁན་གྱི་སྔགས་ཀྱི་མཐུས་དེ་སྒྲོལ་བ་ཡིན་ན། དེ་ཅིའི་ཕྱིར་སྒོ་ཐམས་ཅད་བཀག༌[^892]ནས་སྒྲོལ་བ་ཡིན་ཏེ། ཅི་སྔགས་ཀྱི་མཐུ་མེད་དམ་ཡང་ན་དབང་པོ་བཀག་པ་གཅིག་པུ་གཙོ་བོ་ཡིན་ན་དེའི་ཚེ་སྔགས་དོན་མེད་དོ། །

[Block 1258]
སྔགས་དང་བཅས་པས་རླུང་བཀག་པར་བྱེད་པ་སྙིང་རྗེས་གསོད་པ་ཡིན་ཞེ་ན། དེ་ལྟ་ན་ཤིན་ཏུ་ཡིད་དུ་འོང་བ་རང་གི་ཉེ་བ་རྣམས་ཅིའི་ཕྱིར་མི་གསོད། དེ་ནི་དེས་མི་འདོད་ཅེ་ན། ཕྱུགས་ཀྱིས་ཀྱང་འདོད་པ་མ་ཡིན་ཞེས་ཅིའི་ཕྱིར་རྣམ་པར་འཚེ། དེ་བས་རྣམ་པར་འཚེ་བའི་བདག་ཉིད་ཅན་མེ་མཆོད་པའི་ལས་ལ་སོགས་པ་སྡིག་པ་ཡིན་པའི་ཕྱིར་མཐོ་རིས་ཀྱི་རྒྱུ་མ་ཡིན་ནོ། །

[Block 1259]
ཇི་སྐད་དུ།

[Block 1260 [VERSE]]
སྲོག་ཆགས་གསོད་པ་མི་བཟད༌[^893]པ། །
དྲག་པོ་ཁྲག་གིས་ལག་བསྒོས་པ། །
རྟག་ཏུ་སྡིག་པའི་ལས་སྤྱོད་པ། །
དེ་དག་ངུ་འབོད་སྐྱེ་བར་འགྱུར། །

[Block 1261]
ཞེས་འབྱུང་ངོ་། །གཞན་ཡང་རྟོག་པ༌[^894]དང་ལྡན་པའི་ཕྱིར་ཐར་པར་མི་འགྱུར་ཏེ། གང་གི་བྱ་བའི་ཕྱོགས་ནི་མེ༌[^895]མཆོད་པ་དང་། ཁ་དོན༌[^896]དང་ཁྲུས་ལ་སོགས་པ་དང་ལྡན་པའི་ཕྱིར་ཏེ་རྟོག་པ་དང་བཅས་པའོ། །

[Block 1262]
ཐམས་ཅད་འདོར་བའི་རང་བཞིན་ནི་མི་རྟོག་པ་སྟེ་ཐར་པའོ། །

[Block 1263]
དེ་བས་ན༌[^897]རྟོག་པ་དང་བཅས་པའི་ལམ་གྱིས་མི་རྟོག་པའི་ཐར་པ་ཐོབ་པར་མི་འགྱུར་ཏེ། རྒྱུ་མི་འདྲ་བའི་ཕྱིར་རོ། །

[Block 1264]
[^898]ནས་ཀྱི་ས་བོན་ལས་སཱ་ལུའི་འབྲས་བུ་མི་འབྱུང་བ་བཞིན་ནོ། །

[Block 1265]
དེ་བས་ན་རྟོག་པ་ཐམས་ཅད་ཡོངས་སུ་སྤངས་པའི་ཏིང་ངེ་འཛིན་གྱིས་རྟག་ཏུ་དྲི་མ་མེད་པ་ཟག་པ་མེད་ཅིང་རྣམ་པར་མི་རྟོག་པའི་ཐར་པ་ཐོབ་པར་འགྱུར་རོ། །
--- END BLOCKS ---
