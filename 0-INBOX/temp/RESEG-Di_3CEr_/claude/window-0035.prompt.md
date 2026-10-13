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

[Block 1231]
ཞེས་བྱ་བ་བར་སྐབས་ཀྱི་ཚིགས་སུ་བཅད་པའོ། །

[Block 1232]
དེའི་ཕྱིར་སྦྱོར་བའི་མཚན་ཉིད་མངོན་པར་མ་འབྲེལ་ཏོ༌[^946]ཞེས་བྱ་བ་དེ་དག་གིས་ནི་གྲངས་ཅན་རྣམས་ཀྱི་གཏན་ཚིགས་མི་རིགས་པ་འབའ་ཞིག་ཏུ་མ་ཟད་ཀྱི། རྣམ་པར་ལྡན་པ་དང་བསལ་ཏེ་འོངས་པ་ཡང་ངོ་ཞེས་བརྗོད་དོ། །

[Block 1233 [HEADING]]
### གཏན་ཚིགས་ལྟར་སྣང་བ། ^3-4-0

[Block 1234 [HEADING]]
#### རྩོད་པ་སྒྲུབ་པའི་གཏན་ཚིགས་ལྟར་སྣང་བ། ^3-4-1-0

[Block 1235]
གཏན་ཚིགས་བརྗོད་ནས་གཏན་ཚིགས་ལྟར་སྣང་བ་དཔྱད་པར་བྱ་སྟེ། དེ་ལ་རེ་ཞིག་རྩོད་པ་སྒྲུབ་པ་ནས། མ་གྲུབ་པ་དང་མ་ངེས་པ༌[^947]དང་། །འགལ་བའི་དོན་ནི་གཏན་ཚིགས་ལྟར་སྣང་བའོ་ཞེས་ཟེར་རོ། །

[Block 1236]
དེ་ལ་མ་གྲུབ་པ་ལ་སོགས་པ་ནི་དཔེར་ནི༌[^948]བརྗོད་ན༌[^949]མཚན་ཉིད་ནི་མ་ཡིན་ཏེ། དཔེར་ན་མིག་གི་གཟུང་བྱ་ཡིན་པའི་ཕྱིར་མི་རྟག་གོ་ཞེས་བྱ་བ་མ་གྲུབ་པ་དང་། ལུས་ཅན་མ་ཡིན་པའི་ཕྱིར་རྟག་གོ་ཞེས་བྱ་བ་མ་ངེས་པ་དང་། བྱེ་བྲག་པ་རྣམས་ཀྱི་དབང་པོ་ལས་བྱུང་བའི་ཕྱིར་མི་རྟག་གོ་ཞེས་བྱ་བ་འགལ་བ་གཅིག་དང་། གྲངས༌[^950]ཅན་པའི་རྒྱུ་ལ་འབྲས་བུ་ཡོད་པ་ཡིན་ཏེ། ཡོད་པ་སྐྱེ་བའི་ཕྱིར་རོ་ཞེས་བྱ་བ་འགལ་བ་གཉིས་པའོ། །

[Block 1237]
དེ་ལ་ཡང་། མ་གྲུབ་དབྱེ་བ་བརྗོད་མ་ཡིན། །དེ་ནི་ཕྱོགས་གཅིག་ལ་རབ་ཏུ་མ༌[^951]གྲུབ་པ་ལ་སོགས་པའི་དབྱེ་བ་རྣམ་པ་དུ་མ་ཡོད་པ་མ༌[^952]བསྟན་པ་ཡིན་ནོ། །

[Block 1238]
འཁྲུལ་པ་ལ་ཡང་བརྗོད་མ་ཡིན། །དབྱེ་བ་མ་བརྗོད་དོ་ཞེས་བྱ་བར་འགྱུར་རོ། །

[Block 1239]
དེ་ནི་ཐུན་མོང་མིན་པའང་ཡོད། །འགལ་བ་མི་འཁྲུལ་བ་ཅན་ཡང་། །

[Block 1240]
ཁོ་བོ་ཅག་གིས་ཇི་ལྟ་བ་བཞིན་དུ་བརྗོད་དོ། །

[Block 1241]
འགལ་བ་གཅིག་ནི་མཚུངས་པ་རུ་བརྗོད་དོ། །

[Block 1242]
བྱེ་བྲག་པའི་སྤྱི་དབང་པོ་ལས་བྱུང་བ་རྟག་པ༌[^953]ཡིན་ནོ་ཞེས་བྱ་བ་ནི་རྟག་པ་དང་མི་རྟག་པ༌[^954]གཉིས་ཀ་ལ་མཐོང་བའི་ཕྱིར་འདི་མ་ངེས་པ་ཉིད་ཡིན་གྱི་འགལ་བ་ནི་མ་ཡིན་ནོ། །

[Block 1243]
གཅིག་ནི་མ་གྲུབ་ཐུན་མོང་མིན། །འགལ་བ་གཉིས་པ་ནི། མ་གྲུབ་པ་དང་ཐུན་མོང་མ་ཡིན་པ་དེ།[^955] གང་གི་ཕྱིར་འདི་ལྟར་སྔར་སྐྱེས་པ་ལས་སྐྱེ་ཞིང་འབྱུང་བ་ན་ཡོད་པ་མ་ཡིན་ལ། ཐམས་ཅད་ཀྱང་སྔར་སྐྱེས་པ་ལས་ཡོད་པར་སྒྲུབ་པ་ནི༌[^956]ཡིན་ཞིང་། སྔར་སྐྱེས་པ་ལས་སྐྱེ་ཞིང་འབྱུང་བ་ཡང་མ་ཡིན་ནོ། །

[Block 1244]
ཁས་བླངས་ན་ཡང་དེ་ཁོ་ན་ལ་ཡོད་པ་ཡིན་ནོ། །

[Block 1245]
འདི་འགལ་བ་ནི་མ་ཡིན་ཏེ།

[Block 1246 [VERSE]]
བཟློག་པ༌[^957]མི་བསྒྲུབ་པའི༌[^958]ཕྱིར་རོ། །
བཟློག་པ་ཡི་ནི་རྒྱུ་མཚན་དང་། །
འདོད་ལ་གནོད་བྱེད་ཀྱང་མ་བརྗོད། །

[Block 1247]
དེ་བས་ན་ཉུང་བར༌[^959]སྣང་སྟེ། དེ་དག་ཉིད་ཀྱི་ཁོངས་སུ་བསྡུ་བར་ཡང་མི་ནུས་ལ་གཏན་ཚིགས་ལྟར་སྣང་བ་མ་ཡིན་ཏེ་ཞེས་ཀྱང༌[^960]བརྗོད་པར་མི་ནུས་ཏེ། བཟློག་པ་དང་གནོད་པར་བྱེད་པའི་གཏན་ཚིགས་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1248 [HEADING]]
#### རིགས་པ་ཅན་རྣམས་ཀྱི་གཏན་ཚིགས་ལྟར་སྣང་བ། ^3-4-2-0

[Block 1249]
རིགས་པ་ཅན་རྣམས་ནི་འཁྲུལ་པ་དང་བཅས་པ་དང་། འགལ་བ་དང་སྐབས་དང་མཚུངས་པ་དང་། བསྒྲུབ་བྱ་དང་མཚུངས་པ་དང་། དུས་ལས་འདས་པ་རྣམས་ནི་གཏན་ཚིགས་ལྟར་སྣང་བའོ་ཞེས་ཟེར་རོ། །

[Block 1250]
དེ་ལ་འཁྲུལ་པ་དང་བཅས་པ་ནི་མ་ངེས་པ་སྟེ། དེ་ལྟར་ན་ཁྱད་པར་ཡོད་མིན། །གང་ལ་མ་ངེས་པ་ཡིན་ཞེ་ན། གཞན་ལས་ཁྱད་པར་རམ། སྐབས་སུ་བབས་པ༌[^961]ན་ཡོད་པ་མ་ཡིན་ཏེ། སྒྲའི་སྤྱི་དང་བྱེ་བྲག་ལ་ཡོད་པ་ནི་གཉིས་ཀའི་ཡོན་ཏན་ནོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 1251]
ཅི་སྟེ་འདི་ལྟར་སྤྱི་འདི་ནི་སྒྲ་མ་ཡིན་ཏེ། གཅིག་ཏུ་ངེས་པ་འགེགས་པ་ཡིན་པའི་ཕྱིར་དང་། གང་དེ་ནི་བསྒྲུབ་པར་བྱ་བའི་རིགས་ཉིད་དུ་འགྱུར་ཏེ། དེ་ཡང་འདི་གཅིག་ཏུ་ངེས་པ་འགེགས་པ་ཡིན་ནོ་ཞེ་ན། འདི་ལྟར་ན་ཡང་ཁྱད་པར་ཡོད་པ་མ་ཡིན་ཏེ། དེ་ལྟ༌[^962]ན་ཡང་བསྒྲུབ་བྱ་མེད་པ་དང་། དེ་ལས་གཞན་པ་དང་། དེ་དང་འགལ་བ་ལ༌[^963]ཡང་འཇུག་པར་དོན་གྱིས་གོ་བར་རིག་པར་བྱའོ། །

[Block 1252]
རྣམ་པ་ཐམས་ཅད་དུ་འཁྲུལ་པ་ཅན་མ་ཡིན་ནོ་ཞེས་སྔར་བརྗོད་དོ། །

[Block 1253]
གྲུབ་པའི་མཐའ་ཁས་བླངས་ན་ནི་དེ་དང་འགལ་བ་ཡིན་པས་འགལ་བར་འགྱུར་ཏེ། དཔེར་ན་བྱེ་བྲག་པའི་ལུས་ཅན་མ་ཡིན་པའི་ཕྱིར་རྩོམ་པར༌[^964]བྱེད་པ་མ་ཡིན་ཏེ་རྡུལ་ཕྲ་རབ་རྣམས་བཞིན་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 1254]
དེ་བཞིན་དུ་བརྟག་པར་བྱ་བ་ལ་གྲུབ་པའི་མཐའ་དང་འགལ་བས་བརྗོད་པར་བྱ་བ་ནི་སྒྲུབ་པའི་སྐྱོན་དུ་འགྱུར་རོ། །

[Block 1255]
འགལ་བ་གཞན་ཡང་འཐོབ་སྟེ། གཏན་ཚིགས་ལྟར་སྣང་བ་འབའ་ཞིག་ཏུ་མ་ཟད་ཀྱི་འདི་ལ་ནི་ལུས་ཅན་ཡིན་པའི་ཕྱིར་ཞེས་བྱ་བ་མ་གྲུབ་པའི་དོན་ལ་གཏན་ཚིགས་ཀྱི་སྐྱོན་དང་རྩོམ་བར་བྱེད་པ་མ་ཡིན་ཞེས་བྱ་བ་དམ་བཅའ་བའི་སྐྱོན་ཡང་ཡིན་ཏེ། སྔར་ཁས་བླངས་པ་དང་འགལ་བའི་ཕྱིར་རོ། །

[Block 1256]
ཅི་སྟེ་ཡང་དེ༌[^965]མ་གྲུབ་པ་ཉིད་དང་འགལ་བ་ཉིད༌[^966]གཉིས་ཀར་འགྱུར་ན་ནི། དམ་བཅའ་བའི་སྐྱོན་དང་འགལ་བ་ཉིད་དག་ཡིན་ཏེ། སྦྱོར་བ་ལ་ནི་དེ་གཉིས་ཀ་ཅིག་ཅར་དུ་འགལ་བར་འགྱུར་ལ་དེ་ཡང་ཅིག་ཤོས་ཀྱི་བྱེད་པ་པོ་ལ་སྐུར་པ་འདེབས་པར་འགྱུར་རོ་ཞེ་ན། དེ་ལྟ་བུར་གྱུར་ལ་རག་མོད། གལ་ཏེ་བྱེད་པ་པོའི་སྦྱོར་བ་བཞིན་དུ་འདིའི༌[^967]ཆོས་གཞན་འགལ་བ་ཉིད་ཀྱིས་སྟོན་པར་བྱེད་ན་ནི་དེར་ཡང་མ་གྲུབ་པ་ཉིད་དུ་བརྗོད་པར་བྱ༌[^968]སྟེ། དམ་བཅའ་བའི་སྐྱོན་ཡང་། དེ་བཞིན༌[^969]མིན། དེར་གྲུབ་པའི་མཐའ་ལས་མ༌[^970]གྲུབ་པའི་དོན་ཉིད་བཞག༌[^971]ནས་ཕྱོགས་དང་འགལ་བའི་སྐྱོན་གཞན་ཉིད་གཅིག་ནི་བརྗོད་དུ་མེད་དོ། །

[Block 1257]
བྱེད་པ་པོ་ལ་ཆོས་གཞན་རང་དབང་ཅན་དང་གཞན་དབང་ལ་སོགས་པ་ལས་ཡིན་པས་འགལ་བ་ལ་སོགས་པ་མེད་པ་ཅིག་ཤོས་ཀྱི་སྦྱོར་བ་ནི་དཔེར་ན་མདའ་བསྣུན་ནོ་འདིའི༌[^972]བསྣུན་ནོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 1258]
གང་འདི་ལ་གྲངས་ཅན་གྱིས་ནི་འདི་སྐད་དུ་བརྗོད་དོ། །

[Block 1259]
གཙོ་བོ་ནི་རྒྱུ་མ་ཡིན་ཏེ། སེམས་པ་ཅན་མ་ཡིན་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 1260]
དེ་ལ་ཡང་བསལ་བ་ནི་གཙོ་བོ་ལས་གཞན་མ་ཡིན་པའི་ཕྱིར༌[^973]ཐུན་མོང་མ་ཡིན་པའོ་ཞེས་བྱ་བའི་མ་ངེས་པ་ཉིད་ཡིན་ནོ། །

[Block 1261]
ཐ་དད་ལས་གཞན་ཉིད་དུ་རྗོད་པར་བྱེད༌[^974]ན་ནི་འགལ་བ་ཉིད་དུ་འགྱུར་ན་འོན་ཀྱང་། དེ་བཞིན་མིན།[^975] དེ་ནི་ཁོ་ན་ཞིག༌[^976]སྒྲུབ་པའི་འགལ་བ་ཉིད་ཡིན་ཏེ། [^977]བཟློག་པ་སྒྲུབ་པར་བྱེད་བའི་ཕྱིར་རོ། །

[Block 1262]
གྲུབ་པའི་མཐའ་དང་འགལ་བའི་ཕྱིར་ཞེས་པ་ནི་མ་ཡིན་ནོ། །

[Block 1263]
གང་ལ་སྐབས་སུ་བབ་པ༌[^978]དེ་གཏན་ལ་དབབ་པའི་ཕྱིར་ཉེ་བར་འགོད་པ་ནི་སྐབས་དང་མཚུངས་པ་སྟེ། དཔེར་ན་བདག་ནི་རྟག་པ་ཡིན་ཏེ། ལུས་ལས་གཞན་མ་ཡིན་པའི་ཕྱིར་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 1264]
འདིར་ཡང་ལུས་ལས་གཞན་མ་ཡིན་པ་ཉིད་ལས་བདག་སྤྱོད་པ་ནི་མ་ཡིན་ཏེ་འདི་ལྟར། མ་ངེས་པར་འགྱུར། གང་གི་ཕྱིར་འདི་ལྟར་རྟག་པ་ནམ་མཁའ་ལ་སོགས་པ་དང་། མི་རྟག་པ་བུམ་པ་ལ་སོགས་པ་གཉིས་ཀ་ལ་ལུས་ལས་གཞན་མ་ཡིན་པ་ཉིད་མཐོང་བ་དེའི་ཕྱིར་ཅི་འདི་རྟག་པ་ཡིན་ནམ། འོན་ཏེ་མི་རྟག་པ་ཡིན་ཞེས་དཔྱོད་པར་བྱེད་དོ། །

[Block 1265]
དེའི་ཕྱིར་འདི་མ་ངེས་པ་ལས་ཐ་དད་དུ་བྱ་བ་མ་ཡིན་ནོ། །
--- END BLOCKS ---
