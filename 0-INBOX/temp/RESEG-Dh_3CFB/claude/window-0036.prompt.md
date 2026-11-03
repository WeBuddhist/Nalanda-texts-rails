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
[Block 1261]
བརྗོད་པ་ཡིན་ན་ནི་འབྲེལ་པ་ཉིད་དུ་བློ་ལ༌[^982]གནས་པའི་ཕྱིར་བསམ་པ་ཇི་ལྟ་བ་བཞིན་རྟོགས་པ་མ་ཡིན་ནོ། །

[Block 1262]
དེ་བས་ན་འདི་རྟོགས་འགྱུར་བ་ཡང་འབྲེལ་པའི་ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར། རང་གི་ངོ་བོས་བརྗོད་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 1263]
དེ་བས་ན་མེད་པ་དང་འདྲ་བར་འབྲེལ་པ་ལ་ཡང་ཐལ་བར་འགྱུར་བ་མེད་དོ།། །།

[Block 1264]
བམ་པོ་དྲུག་པ། གཞན་ཡང་མེད་པ་བརྗོད་པར་བྱ་བར་སྨྲ་བ་འདི་ལ་ལན་འདེབས་པ་ན། མི་སྨྲ་ན་ཇི་ལྟར་ལན་གདབ༌[^983]པར་བྱ། ཚིག་འདི་ལ་ཡང་ཇི་ལྟར་མེད་པ་བརྗོད་པ་མ་ཡིན་ན། [^984]འོན་ཏེ་མེད་པ་ཉིད་མི་འདོད་པ་དེ་བས་ན་བརྗོད་པ་མ་ཡིན། དེ་ཉིད་ན་ནི་མེད་པ་ཡོད་པ་མ་ཡིན་ནོ། །ཞེས་བྱ་བ་ཇི་ལྟ་བ༌[^985]ཡིན། གང་ཡང་དེའི་དོན་བཀག་པ་ན་དོན་མེད་པའི་སྒྲ་མི་སྦྱོར་བའི་ཕྱིར། ཡུལ་མེད་པའི་དགག་པའི་སྦྱོར་བ་མེད་དོ་ཞེས་བྱ་བ་འདི་འོག་ནས་འཆད་པར་འགྱུར་རོ། །

[Block 1265]
དེ་བས་ན་མེད་པ་དག་ལ་སྒྲ་དག་ཀྱང་ཡོད་པར་འགྱུར་རོ། །

[Block 1266]
དེ་དག་ཇི་ལྟར་རང་བཞིན་ཐ་དད་པ་ཡིན་ཞེ་ན། དེ་ལ་ཡང་། མེད་པའི་ངོ་བོ་མེད་པའི་ཕྱིར། །མེད་པའི༌[^986]ངོ་བོ་བརྗོད་པ་ཅན་གྱི་སྒྲ། །

[Block 1267]
ཐེ་ཚོམ་མེད་དེ་དག་རྣམ་གཅོད། །རྗོད་པར་བྱེད་པར་སྒྲུབ་པ་ཉིད། །

[Block 1268]
སྒྲ་རྣམས་ཀྱི་དངོས་པོའི་བྱ་བ་དག་ལ་ནི༌[^987]ངོ་བོ་བརྗོད་པའམ། འོན་ཏེ་ཐ་དད་པ་ཞེས་འདོགས་པར༌[^988]འགྱུར་ལ། མེད་པ་ནི་དབེན་པའི་མཚན་ཉིད་ཁོ་ན་ཡིན་ཏེ། རྒྱུ་མཚན་དུ་བྱ་བའི་ངོ་བོ་འགའ་ཞིག་ཀྱང་མེད་པའི་ཕྱིར་རམ། དེའི་ངོ་བོ་ལ་མེད་པ་མི་རུང་པའི་ཕྱིར་ཏེ། ངོ་བོ་ནི་དེའི་མཚན་ཉིད་ཅན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1269]
དེ་བས་ན་འདི་ཉིད་དངོས་སུ་དབེན་པ་ཡིན་ཏེ། དེ་ནི་དེ་ལྟ་བུའི་ངོ་བོ་རྗོད་པར༌[^989]བྱེད་པའི་སྒྲ་དག་ཅི། དབེན་པའི་ཡུལ་ཅན་ཡིན་ནམ་ཞེས་བྱ་བ་དེ་ནི་གནས་མ་ཡིན་པ་ལ་ཐེ་ཚོམ་ཟ་བ་ཡིན་ནོ། །

[Block 1270]
དེའི་ཕྱིར་སྒྲ་ཐམས་ཅད་ནི་དབེན་པའི་ཡུལ་ཅན་དང་རྣམ་པར་རྟོག་པ་དག་ཀྱང་གྲུབ་པ་ཡིན་ནོ། །

[Block 1271]
དེ་བས་ན་དངོས་པོ་གཅིག་གི་རྗེས་སུ་འབྲང་བ་ཅན་དག་ཀྱང་བདག་ཉིད་ཇི་ལྟ་བ་བཞིན་དུ་ཁྱད་པར་ཐ་དད་པས་ཉེ་བར་བརྟགས་པའི་ཁྱད་པར་རྣམས་ཀྱི༌[^990]ཐ་དད་པ་དག་བཞིན་དུ་བློ་ལ་སོ་སོར་སྣང་བའི་དབེན་པ་དག་ལ་ཉེ་བར་གནས་པའི་ཕྱིར། ཐ་དད་པའི་ཡུལ་ཅན་ཁོ་ན་ཡིན་ནོ། །

[Block 1272]
དེ་བས་རང་བཞིན་ཉིད་ནི་བསྒྲུབ་པར་བྱ་བ་དང་སྒྲུབ་པར་བྱེད་པའི་ངོ་བོ་ཡིན་དུ་ཟིན་ཀྱང་བསྒྲུབ་པར་བྱ་བ་དང་སྒྲུབ་པར་བྱེད༌[^991]པ་འདྲེས་པ་མ་ཡིན་ནོ། །

[Block 1273]
དེ་བས་ན་དམ་བཅས་པའི་དོན་གྱི་ཕྱོགས་གཅིག་གཏན་ཚིགས་སུ་འགྱུར་བ་མ་ཡིན་ནོ། །

[Block 1274 [HEADING]]
### རང་བཞིན་ཁྱད་པར་བྱེ་བྲག་ལ་ལྟོས་པ། ^4-4-0

[Block 1275]
དེ་འདི་ཡང་གཏན་ཚིགས་ཉིད་དུ་བསྟན་པ་ན། རང་བཞིན་ཁྱད་པར་བྱེ་བྲག་ལ་ལྟོས་པ་ཅན་ནི་འགའ༌[^992]ཞིག་ལས། །

[Block 1276 [VERSE]]
བརྗོད་བྱ་བསྒྲུབ་བྱ་སྒྲུབ་པའི་ཕྱིར། །
འཇིག་ལ་བྱས་དང་ཡོད་ཉིད་བཞིན། །

[Block 1277]
རང་གི་ངོ་བོ་གྲུབ་པར་བྱ་བའི་ཕྱིར། གཞན་གྱི་བྱེད་པ་ལ་ལྟོས་པའི་ངོ་བོ་ནི་བྱས་པ་ཡིན་པ་དེ་བས་ན་བྱས་པའི་སྒྲ་འདིས་གཞན་གྱི་ཁྱད་པར་ཅན་གྱི་རང་བཞིན་བརྗོད་པས་ཀྱང་འདི༌[^993]འཕངས་པ་ཡིན་ནོ། །

[Block 1278]
དེ་ནི་རྐྱེན་གྱི་བྱེ༌[^994]བྲག་གིས་ཐ་དད་པ་ཅན་ཉིད་ལ་སོགས་པ་བཤད་པ་ཡིན་ནོ། །

[Block 1279]
དེ་ལྟར་ན་ཁྱད་པར་གྱི་བྱེ་བྲག་ལ་ལྟོས་པ་ཅན་ནི་འགའ་ཞིག་ཏུ་རང་བཞིན་གྱི་གཏན་ཚིགས་ཡིན་ནོ་ཞེས་བྱ་བ་དང་། འགའ་ཞིག་ཏུ་ལྟོས་པ་མེད་པར་སྤྱིར་བརྗོད་པར་བྱ་སྟེ། དཔེར་ན་མི་རྟག་པ་ཁོ་ན་ཉིད་ལ་ཡོད་པ་ཉིད༌[^995]ལྟ་བུའོ། །

[Block 1280]
འགའ་ཞིག་ཏུ་རང་བཞིན་དུ་གྱུར་པའི་ཆོས་ཀྱི་བྱེ་བྲག་ཡོངས་སུ་གཟུང་བའི་སྒོ་ནས་ཏེ། དཔེར་ན་དེ་ཉིད་ལ༌[^996]སྐྱེ་བ་ལྟ་བུའོ། །

[Block 1281]
ཕྱོགས་འདིས་རང་བཞིན་གྱི་གཏན་ཚིགས་ཀྱི་དབྱེ་བ་གཞན་དག་ལ་ཡང་བལྟ་བར་བྱའོ། །

[Block 1282 [VERSE]]
གལ་ཏེ་གཏན་ཚིགས་ཡོད་རང་བཞིན། །
ཇི་ལྟར་ཡོད་པ་བསྒྲུབ་བྱ་མིན། །
ཁྱད་པར་རྗེས་འགྲོ་མེད་པ་ནི། །
གཏན་ཚིགས་བསྒྲུབ་བྱ་དག་ལས་ཉམས། །

[Block 1283]
གལ་ཏེ་ཡོད་པ་ཉིད་མི་རྟག་པ་ཉིད་དམ། རང་བཞིན་གྱི་གཏན་ཚིགས་སུ་འགྱུར་ན་ཅིའི་ཕྱིར་བསྒྲུབ་པར་བྱ་བར་ཡང་མི་འདོད། དེ་དེ་ལྟར་རབ་ཏུ་བསྒྲུབས་པ་ན་ཁྱད་པར་དུ་འགྱུར་ན་ཁྱད་པར་ཡང་བསྒྲུབ་པར༌[^997]ནུས་པ་མ་ཡིན་ཏེ། རྗེས་སུ་འགྲོ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 1284]
ཇི་སྐད་དུ་ཚད་མའི་ཡུལ་མི་ཤེས་པའི་ཕྱིར་རོ་ཞེས་བསྟན་ཏོ། །

[Block 1285]
ཁྱད་པར་དེ་འདི་ནི་བསྒྲུབ་པར་བྱ་བ་ཉིད་དུ་སྐྱོན་ཡོད་པ་འབའ་ཞིག་ཏུ་མ་ཟད་ཀྱི་འོན་ཀྱང་གཏན་ཚིགས་ལ་ཡང་སྐྱོན་མཚུངས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1286]
གཏན་ཚིགས་རྗེས་སུ་འགྲོ་བ་མེད་པ་ཅན་ནི་སྒྲུབ་པའི་ཡན་ལག་མ་ཡིན་ཏེ། དེ་ལས༌[^998]ཐེ་ཚོམ་དུ་གྱུར་པའི་ཕྱིར་རོ། །

[Block 1287]
ཉེས་པ་དེ་ཡོད་པ་མ་ཡིན་ཏེ་འདི་ལྟར།

[Block 1288 [VERSE]]
ཡོད་པའི་ཁྱད་པར་ཙམ་དུ་ནི། །
བསྒྲུབ༌[^999]བྱའི་སྤྱི་ཡི་ཆོས་ཅན་ལ། །
དོན་འགའ་ཞིག་ཀྱང་འགྲུབ་མི་འགྱུར། །
དེ་འདྲ་བ་ཡང་བཀག་པ་མེད། །

[Block 1289]
རྣམ་པ་ཐམས་ཅད་དུ་ཡོད་པ་ཉིད་སྒྲུབ་པ་ནི་ཁྱད་པར་སྒྲུབ་པར་བྱེད་པར་གྱུར་པ༌[^1000]མ་ཡིན་གྱི། ཡོད་པ་ཙམ་ཁྱད་པར་ཅན་ནི་ཆོས་ཅན་འགའ་ཞིག་ལ་ཡོད་དོ་ཞེས་སྒྲུབ་པར་བྱེད་པ་ན་རང་གི་ངོ་བོ་ཁྱད་པར་མ་བསྟན་པ་ཅན་འགའ་ཞིག་དང་ཡོད་པ་ཙམ་ལ་འགལ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 1290]
འདིར་ཡོད་པ་ཉིད་སྒྲུབ་པ་འགོག་པ་ནི་མ་ཡིན་གྱི། འོན་ཀྱང་འདི་ལྟར་འགའ་ཞིག་ཡོད་དོ་ཞེས་སྨྲ་ན། འདིའི་ཁྱད་པར་གཞན་འགའ་ཞིག་ལ་རེག་པ་མེད་ན་རང་གི་དོན་ཅི་ཞིག་གསོ་བར་བྱེད། དེ་བས་འདིས་གཟུང་བའི་ཁྱད་པར་ཁོ་ན་བསྒྲུབ་པར་བྱ་བ་ཡིན་ན།

[Block 1291 [VERSE]]
ཁྱད་པར་གཟུང་བ་བསྒྲུབ་བྱ་འདིར། །
གཏན་ཚིགས་རྗེས་འགྲོ་མེད་ཅན་འགྱུར། །
དེས་ཡོད་བསྒྲུབ་པར་བྱ༌[^1001]ཡིན་ན། །
ཁྱད་པར་དག་ནི་བསྒྲུབ་པར༌[^1002]འགྱུར། །

[Block 1292]
ཆོས་ཅན་གཙོ་བོའི་མཚན་ཉིད༌[^1003]ཅན་དེ་ནི་གཅིག་པ་དང་རྟག་པ༌[^1004]དང་བདེ་བ་ལ་སོགས་པའི་བདག་ཉིད་ཅན་ནམ་གཞན་ཡིན་ནོ།[^1005] །ཞེས་ཇི་ལྟར་རྣམ་པ་འགའ་ཞིག་གིས་ཀྱང་ཁྱད་པར་བྱས་པ་དེའི་རང་གི་ངོ་བོ་བསྒྲུབ་པར༌[^1006]འགྱུར་ཏེ། དེ་ཡང་དེ་ལྟར་རྗེས་སུ་འགྲོ་བ་ནི་མ་ཡིན་གྱི། གང་ཡོད་པ་ཙམ་གྱི་རྗེས་སུ་འགྲོ་བ་གྲུབ་པ་དེས་ཅི་ཡང་མ་ཡིན་ནོ། །

[Block 1293]
དེ་ལྟར་མེ་ལ་སོགས་པ་དག་ལ་ཡང་ཐལ་བར་འགྱུར་བ་མ་ཡིན་ནམ། དེ་ལ་ཡང་མེ་ཡོད་པ་ཉིད་ཙམ་ལ༌[^1007]བརྗོད་པ་ཅུང་ཞིག་ཀྱང་མེད་དེ། ཁྱད་པར་ཅན་གྱི་རྟེན་གྱིས་ཁྱད་པར་དུ་བྱས་པ་ཅན་མངོན་པར་འདོད་པ་ལ་རྗེས་སུ་འགྲོ་བ༌[^1008]མེད་པའི་ཕྱིར་མ་གྲུབ་པའི་ཡིན་ནོ། །

[Block 1294]
རྟེན་དེས་དེ་ཁྱད་པར་དུ་བྱེད་པ་ནི་མ་ཡིན་ཏེ། དེ་ནི་མི་ལྡན་པ་རྣམ་པར་བཅད་པས་ཁྱད་པར་དུ་བྱས་པའི་ཕྱིར། ཞེས་བཤད་པ་དང་འཆད་པར་འགྱུར་རོ། །

[Block 1295]
དེ་བས་ན་དེར་སྤྱི་ཉིད་ནི་མི་ལྡན་པ་རྣམ་པར་བཅད་པས་སྒྲུབ་པ་དེ་ལྟར་འདིར་ཡང་འགའ་ཞིག་ལ་ཡོད་པ་ཉིད་སྒྲུབ་པ་ནི་མ་ཡིན་ནོ། །

[Block 1296]
གཙོ་བོ་ལ་སོགས་པའི་སྒྲ་བརྗོད་པའི་དོན་འགའ་ཞིག་ཀྱང་མེད་པའི་ཕྱིར་དེ་ནི་ཁྱད་པར་མེད་པ་ཅན་ཁོ་ན་ཡིན་ནོ། །

[Block 1297]
ཇི་ལྟར་མེད་པ་ཡིན་ཏེ། ཤེས་བྱ་དང་བརྗོད་པར་བྱ་བ་དང་གཞལ་བྱ་དག་ཏུ་དེ་ཡང་གྲུབ་པ་ཁོ་ན་ཡིན་ནོ་ཞེ་ན། [^1009]དེ་བས་ན་ད་ཅི་ཤེས་བྱ་ཡོད་ཅེས་བྱ་བས་གྲུབ་པ་ཡིན་ཡང་བླ་སྟེ། དེ་ལྟར་ན་ཡང་ཅི་ཞིག་འགྲུབ་པར་འགྱུར། གཞན་དུ་མེའི་སྤྱི་དེ་ཉིད་དེ་ལ་མ་གྲུབ་པའི་ཕྱིར་བསྒྲུབ་པར་བྱ་བ་ཡིན་ནོ། །

[Block 1298]
དེ་ལ་ཡང་དེ་དང༌[^1010]མི་ལྡན་པ་བྲལ་བ་ཅན་གྱི་སྤྱིས་རྗེས་སུ་འགྲོ་བ་མ་གྲུབ་པ་ཁོ་ན་མ་ཡིན་ནམ། འགའ་ཞིག་དེ་ལྟ་བུར་གྱུར་པའི་དོན་གྱི་རྗེས་སུ་འགྲོ་བར་བྱེད་པ་མ་ཡིན་གྱི། གཞན་ལ་ཁོང་དུ་ཆུད་པར་བྱེད་པས་ནི་དུ་བས་ནི་གང་ན་དུ་བ་ཡོད་པ་དེ་ནི༌[^1011]མེ་ཡོད་དོ་ཞེས་མེ་མེད་ན་མི་འབྱུང་བར་བསྟན་པར་བྱ་བ་ཡིན་ནོ། །

[Block 1299]
དེ་ལྟར་ན་དེ་མེ་ཙམ་གྱིས་ཁྱབ་པར་གྲུབ་པས་གང་ན་བདག་ཉིད་སྣང་བར་འགྱུར་པ་དེ་ཉིད་དུ་མེའི་བློ་སྐྱེད་པར་བྱེད་དོ། །

[Block 1300]
དེ་ལ་སྒྲུབ་པར༌[^1012]བྱེད་པ་བསྟན་པས་ཅིར་ཡང་མི་རུང་སྟེ། དེ་ལ་མཐོང་བ་དང་འབྲེལ་པ་བསྟན་པ་ཙམ་གྱིས་འདོད་པ་འགྲུབ་པའི༌[^1013]ཕྱིར་རོ། །
--- END BLOCKS ---
