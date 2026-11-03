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
ད་ནི་དེའི་འབྱོར་པ་མི་སྣང་བར་བྱས་པའི་རྒྱུ་ལས་བསམས་ཏེ། གྲགས་པ་ཀུན་ཏུ་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 1227]
ཀུན་ཏུ་གྲགས་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་ཀུན་ཏུ་བསྟན་པའོ། །

[Block 1228]
ཡོངས་སུ་བརྟག་པ་ནི་ཡོངས་སུ་བརྟགས༌[^705]པའི་ཕྱིར་ཏེ། མ་བརྟགས༌[^706]པར་ནི་གྲགས་པ་ཀུན་ཏུ་བསྒྲག་ཅིང་བསྒྲུབ་པར་མི་ནུས་སོ། །

[Block 1229]
དེ་ལྟར་མ་བྱས་ན་ནི་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཕྱེད་པ༌[^707]འདི་ལ་མཛེས་པའི་རྗེས་སུ་འགྲོ་བ་ནི་ནོར་བུ་བཟང་པོ་སྟེ། འདིས་ནི་མཐོང་བའི་ཡུལ་དུ་བསྟན་ཏོ། །

[Block 1230]
དེ་བཞིན་དུ་ཡོན་ཏན་ཐོས་པའི་ཡུལ་དུ་བསྟན་པ་ནི་གྲགས་པ་སྟེ། ནོར་བུ་བཟང་པོ་ལྟ་བུ་ནི་གྲགས་པའོ། །

[Block 1231]
དེ་ལྟར་མ་བྱས་ན་ནི་ཞེས་བྱ་བ་ནི་ཡོངས་སུ་བརྟག་པ་མ་བྱས་པར་རོ། །

[Block 1232]
ནོར་བུ་དག་ནི་གྲགས་པ་ཡིན་པས་ནོར་བུའི་གྲགས་པའོ། །

[Block 1233]
རིན་ཆེ་བ་ཉིད་པས་ནི་རིན་ཆེན་ནོ། །

[Block 1234]
བདག་གི་གྲགས་པ་ཡང་མི་ལྟོས༌[^708]ལ་རིན་ཆེ་བ་ཉིད་དུ་ཡང་མི་ལྟོས་པ༌[^709]སྟེ། ནོར་བུ་བཟང་པོ་ཡིན་ཡང་ཡོངས་སུ་བརྟག་པ་མེད་པར་རོ། །

[Block 1235]
དེ་བཞིན་དུ་གྲགས་པ་ཡང་ཡོངས་སུ་བརྟག་པ་མེད་པར་ནི་ཀུན་ཏུ་གྲགས་པར་མི་འགྱུར་ཏེ། བརྟག་པའི་རྒྱུ་དེས་ན། །ཁྱོད་ཀྱི་ནོར་འདི་རྣམས་ནི་བདག་གིས་སྦས་པར་གྱུར། །ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 1236]
དེ་བས་ཞེས་བྱ་བ་ནི་གང་གི་ཕྱིར་བརྟགས་པའི་རྒྱུ༌[^710]དེས་ཁྱོད་ཀྱི་ནོར་སྦས་པར་གྱུར་པའོ། །

[Block 1237]
དེས་ན་སྦྱིན་པ་ཆར་བཞིན་ཕོབས་ཞེས༌[^711]བྱ་བ་ནི་གང་ནོར་སྦས་པ་དེ་ཉིད་ཀྱིས་བསྒྲུབ་པར་བསྟན་ཏོ། །

[Block 1238]
ངས་ནི་རྗེས་སུ་བཟུང་བས་ནོར༌[^712]ཡང་ཟད་མི་འགྱུར། །ཞེས་བྱ་བ་འདིས་ནི་མཆོག་སྦྱིན་པར༌[^713]བསྟན་ཏོ། །

[Block 1239]
ཁྱོད་ཀྱིས་བཟོད་པར༌[^714]བྱོས་ཞེས་བྱ་བ་འདིས་ནི། ནོར་སྦས་པ་དེ་དང་དེ་འདིས་ནི་བཟོད་པར་མཛོད་ཅིག་པའོ། །

[Block 1240]
མགུ་བར་བྱས་པ་ཞེས་བྱ་བ་ནི་གྲགས་པ་ཀུན་ཏུ་བསྒྲགས་པ་ཞེས་བྱ་བ་ལ་སོགས་པའི༌[^715]ཚིགས་བཅད་ལྔས་སོ། །

[Block 1241]
དེ་ཡི་ནོར་གྱི༌[^716]རྣམ་པ་སླར་བྱིན་ཏེ། དེ་བས་སྦྱིན་པ་ཞེས་བྱ་བའི་ཚིགས༌[^717]བཅད་སྔར་བསྟན་པ་དེས་བསྟན་ཏོ། །

[Block 1242]
བཟོད་པར་བྱས་ནས་ཞེས་བྱ་བ་ནི༌[^718]བདག་གིས་གཙེས་པ་འདི་ཡང་ཁྱོད་ཀྱིས་བཟོད་པ་མཛོད་ཅེས་བྱ་བ་འདིས་བསྟན་ཏོ། །

[Block 1243]
སློབ་དཔོན་དཔའ་བོས་མཛད་པའི་སྐྱེས་པའི་རབས་རྒྱ་ཆེར་བཤད་པ་ལས་ཚོང་དཔོན་ཟིལ་གྱིས་མནོན་པའི་སྐྱེས་པའི་རབས་སོ།། །།

[Block 1244 [HEADING]]
## རི་བོང་གི་སྐྱེས་པའི་རབས། ^6-0

[Block 1245]
ལྡུམ་བུ་དང་། རྩྭ་དང་ཤིང་ལྗོན་པ་ཡིད་དུ་འོང་བ་ཞེས་བྱ་བ་འདིས་ནི་གྲིབ་མ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 1246]
མེ་ཏོག་དང་འབྲས་བུར་ལྡན་པ་ཞེས་བྱ་བ་འདིས་ནི་ཟས་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 1247]
ཆུ་གཙང་མ་བཻ་ཌཱུརྱ་ལྟ་བུ་ཞེས་བྱ་བ་ལ་སོགས་པ་བཞིས་ནི་མིང་གི་ཚོགས་བཏུང་བ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 1248]
ས་གཞི་ནེའུ་གསིང༌[^719]འཇམ་པ་དང་ལྡན་པ་དང་། སྐྱེ་བོ་དཀའ་ཐུབ་ཅན་གནས་པ་དང་ལྡན་པས་ནི་འཇིགས་པ་མེད་པ་ཉིད་དུ་བསྟན་ཏེ། སྔར་བསྟན་པ་ཉིད་ཀྱིས་སྐྱེ་བོ་དཀའ་ཐུབ་ཅན་གནས་པའི་རྒྱུ་བསྟན་ཏོ། །

[Block 1249]
དེ་ནི་ལུས་བཟང་ཞེས་བྱ་བ་ལ་སོགས་པ་བཞིས་ནི་མིང་གི་ཚོགས་དང་། གཟུགས་ཀྱི་ལུས་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 1250]
[^720]ཡོན་ཏན་དེ་དག་ཉིད་དང་ལྡན་པའི་ཕྱིར། གཅན་གཟན་ངན་པས་གླགས་ལྟར་བག་མི་ཚ་བར་གནས་ཏེ། ཇི་ལྟར་གླགས་མི་ལྟ་བར་འདུག་ཅེ་ན། སྨྲས་པ། རི་དགས་རྒྱལ་པོའི་ཚུལ་གྱིས་ཞེས་བྱ་བའོ། །

[Block 1251]
ཆ་བྱད་དང་། ཆོག་ཤེས་པ་གཉིས་ཀྱིས་ནི་ཐུབ་པ་བཞིན་མཛེས་པ་ཡིན་ཏེ། གང་གི་ཕྱིར་ཐུབ་པ་རྣམས་ནི་ཆ་བྱད༌[^721]དང་། ཆོག་ཤེས་པས་རབ་ཏུ་རྣམ་པར་འབྱེད་པ་ཡིན་ཏེ། དེ་བས་ན་འདི་བསྟན་ཏོ། །

[Block 1252]
བདག་གིས་ལགས༌[^722]པ་ཨ་ཛི་ན་གོན་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་ནི་བདག་ཉིད་ངན་པ་སྟེ། གནོད་པར་བྱེད་པ་སྤངས་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1253]
སློབ་མ་བདེར༌[^723]གནས་ཤིང་ཞེས་བྱ་བ་ནི་སློབ་མ་བཞིན་དུ་བདེ་བས་སློབ་མ་བདེར་གནས་ཏེ། བདེ་བ་བྱེད་པའི་ཕྱིར་བདེ་བ་ལྟ་བུའོ། །

[Block 1254]
འདུལ་བ་སྦྱིན་པར་ནུས་པའི་དབང་དུ་བྱས་ནས་སློབ་མ་ཉིད་དང་ཆོས་མཐུན་པས་བདེ་བ་ཡང་ཡིན་ཏེ། [^724]འདི་ལྟར་བདེ་བས་འདུལ་བར་བྱེད་པའོ། །

[Block 1255]
ཡོན་ཏན་ཁྱད་པར་ཅན་གྱིས་སྐྱེས་པ་ཞེས་བྱ་བ་ནི་ཡོན་ཏན་ཁྱད་པར་ཅན་གྱིས་ཡང་དག་པར་བསྐྱེད་པའོ། །

[Block 1256]
བྱང་ཆུབ་སེམས་དཔའ་དེ་ལ་བྱམས་པ་དང་གུས་པ་ཁྱད་པར་ཅན་ཏེ་དེ་ལ་བྱམས་དང་གུས་པའོ། །

[Block 1257]
ཕན་ཚུན་གཉེན་དུ་འབྲེལ་པ་ནི་སྐྱེ་གནས་ཀྱི་འབྲེལ་པ་སྟེ། དེས་འབྲེལ་པའི་བྱམས་ཤིང་ཆགས་པར་གྱུར་པ་གང་ཡིན་པ་ནི་ཕན་ཚུན་གཉེན་དུ་འབྲེལ་བཞིན་དུ་གཅིག་ལ་གཅིག་ཆགས་ཤིང་བྱམས་པར་གྱུར་པའོ། །

[Block 1258]
གཅིག་ལ་གཅིག་ནི་ཕན་ཚུན་འབྲེལ་བས་སོ། །

[Block 1259]
སྤོབས་པ་དང་བཀུར་སྟི་ནི་སྤོབས་པ་དང་བཀུར་སྟིའོ། །

[Block 1260]
དེ་དག་གཅིག་ལ་གཅིག་སྤོབས་ཤིང་བཀུར་སྟིས་རབ་ཏུ་མཛའ་བར་གྱུར་པ་གང་ཡིན་པ༌[^725]དེ་ནི་གཅིག་ལ་གཅིག་སྤོབས་ཤིང་བཀུར་སྟི་བྱེད་པས་རབ་ཏུ་མཛའ་བར་གྱུར་པ་སྟེ། དེ་བས་ན་འདི་ལྟར་རོ་ཞེས་བརྗོད་དོ། །

[Block 1261]
དུད་འགྲོའི་རང་བཞིན་ལ་ནི་མི་ཕྱོགས་ཞེས་བྱ་བ་ནི་སྲོག་གཅོད་པ་ལས་ལྡོག་པའོ། །

[Block 1262]
བདེ་བ་དང་མཐུན་ཞིང་ཞེས་བྱ་བ་ལ་སོགས་པ་འདིའི་ལུས་ནི་ཕན་པ་ཡིན་བདེ་བ་མ་ཡིན་པ་དང་། བདེ་བ་ཡང་མ་ཡིན་ཕན་པ་ཡང་མ་ཡིན་ཞེས་བྱ་བ་ལ་སོགས་པ་རྣམ་པ་བཞི་ལས་དེ་ལ་ཕན་པ་མེད་པ་ནི་གཅིག་ཏུ་མི་བྱ་བ་ཡིན་ནོ། །

[Block 1263]
གང་དུ་ཕན་པ་ཡོད་པ་དེ་ནི་གཅིག་ཏུ་བྱ་བ་སྟེ། དེ་ལ་ཕན་ལ་བདེ་བ་མ་ཡིན་པ་དང་། ཕན་ལ་བདེ་བ་དེ་ནི་བྱ་བ་ཡིན་ནོ་ཞེས་བསྟན་ཏོ། །

[Block 1264]
བདེ་དང་མཐུན་ཞིང་ཡོན་ཏན་མི་མཐུན་ཚུལ། །ཞེས་བྱ་བ་ནི་གང་དུ་ཕན་པ་དང་བདེ་བ་ཡོད་པ་དེ་བསྟན་ཏོ། །

[Block 1265]
ཡོན་ཏན་མཐུན་ཞིང་བདེ་དང་མི་མཐུན་ཚུལ། །ཞེས་བྱ་བ་ནི་ཕན་པ་དེ་ཉིད་བདེ་བ་ཉིད་དུ་བསྟན་ཏོ། །
--- END BLOCKS ---
