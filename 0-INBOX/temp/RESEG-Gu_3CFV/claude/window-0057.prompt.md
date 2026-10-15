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
[Block 1996]
འདིར་གཞུང་ནི་ཞུ་བ་ལས།

[Block 1997]
གསོལ་བ་བརྩམས་པ་ནས་བཤང་བའི་ས་འམ་གཅི་བའི་སར་འགྲོ་བ་འམ་འོང་ཡང་རུང་སྟེ། དགེ་སློང་འཁོད་པ་དག་ལ་མི་སྨྲ་ཡང་ཐོས་པའི་ཉེ་འཁོར་ཡོངས་སུ་མི་གཏོང་བ་གང་ཡིན་པ་ལ་ནི་ལྟུང་བ་མེད་དོ། །

[Block 1998]
འདིར་སྔ་མ་ལ་ཡང་ཐོས་པའི་ཉེ་འཁོར་མི་གཏོང་བ་ལ་ལྟུང་བ་མེད་པར་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 1999]
གཏོང་ན་ནི་ངེས་པར་ཉམས་པར་འགྱུར་རོ། །

[Block 2000]
མི་སྨྲ་བར་འགྲོ་བའི་ལྟུང་བྱེད་དོ།། །།

[Block 2001]
གང་ལ་མ་གུས་པའི་ཚུལ་གྱིས་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་འདུག་པ་དང་འགྲོ་བ་དང་གནས་མལ་དང༌[^1262]གཙུག་ལག་ཁང་ལེན་པ་དང་སྨྲ་བ་ལ་སོགས་པ་ལ༌[^1263]བསྒོ་བའི་དོན་ལ་མ་གུས་པས་ཆོས་དང་ལྡན་པར་ཤད་ཀྱིས༌[^1264]སྦྱང་བ་མེད་པར་དེ་ལས་བཟློག་སྟེ། འགལ་བར་བྱེད་པའོ་ཞེས་བྱ་བ་ནི་དེ་ལས་བཟློག་སྟེ་མི་འདུག་པ་དང་མི་འགྲོ་བ་དང་གནས་མལ་མི་ལེན་པ་དང་གཙུག་ལག་ཁང་མི་ལེན་པ་དང་མི་སྨྲ་བའོ། །

[Block 2002]
སོགས་པའི་སྒྲས་ནི་ལྷག་མ་འདི་ལས་ཆོས་དང་ལྡན་པའི་དོན་ལ་ཉེ་བར་བསྡུས་པའི་དོན་ཏོ། །

[Block 2003]
མི་འགྱུར་བའི་ཡིད་ཀྱིས་ཀྱང་མི་མཐུན་པར་གྱུར་པ་ཡིན་ཏེ་ཤད་ཀྱིས་ཀྱང་ངོ་། །འདི་ལྟ་སྟེ་དཔེར་ན་གུས་པ་རབ་ཏུ་བྱེད་ཅིང་མི་མཐུན་པ་སྟེ། ཁ་ན་མ་ཐོ་བ་ལ་འཇིགས་པར་མཐོང་བ་ནི་མ་ཡིན་ནོ། །

[Block 2004]
ཆོས་དང་མི་ལྡན་པའི་གསོལ་བ་འབའ་ཞིག་ཏུ་ནི་མ་ཟད་དེ། ཆོས་དང་ལྡན་པའི་གསོལ་བ་བཏབ་པས་ཀྱང་འདི་ནི་གུས་པ་མེད་པ་མ་ཡིན་ཏེ། དེ་བས་ན་མི་གུས་པར་ཤེས་པར་མི་བྱའོ། །

[Block 2005]
དེ་བས་ན་གུས་པ་མེད་པ་ཞེས་བྱ་བ་ནི་བྱེ་བྲག་གོ། །

[Block 2006]
གུས་པ་ཡོད་པ་ལས་ཡང་དུས་གཅིག་གི་ཚེ་ཆོས་དང་ལྡན་པའི་གསོལ་བ་བཏབ་པ་ཡོད་པ་མ་ཡིན་ཏེ། འདིར་ཆོས་ཀྱི་གསོལ་བ་བཏབ་པ་མེད་པར་ཡང་སྟེར་བ་ཡིན་ནོ། །

[Block 2007]
དགོངས་པ་ནི་འདི་ཡིན་ཏེ། གང་གི་ཕྱིར་གཉིས་ཀ་ལ་འཁྲུལ་པ་ཡོད་པ་ལ་ཁ་ན་མ་ཐོ་བ་ཡོངས་སུ་རྫོགས་པ་སྟེ། ཅིག་ཤོས་མེད་པ་ལ་ནི་མ་ཡིན་ཏེ། དེ་བས་ན་གཉིས་ཀའི་ཚིག་བཟུང་བའོ། །

[Block 2008]
གང་དུ་གསོལ་བ་མ་བཏབ་པ་ལ་མ༌[^1265]གུས་པ་ཡོད་པ་ནི༌[^1266]མ་ཡིན་ནོ། །

[Block 2009]
གུས་པ་མ་ཡིན་པ་ལ་ནི་གསོལ་བ་མི་སྦྱིན་པར་དེར༌[^1267]ནི་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་འདིས༌[^1268]རིག་པར་བྱའོ། །

[Block 2010]
གང་གིས་ཉེ་བར་འོངས་པའི་དོན་ལ་འགལ་བར་བྱེད་པ་ལ་ལྟུང་བ་ཅི་ལྟ་བུར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་དགེ་སློང་གིས་དགེ་འདུན་ལ་ནི་དངོས་གཞིའོ། །

[Block 2011]
མཁན་པོ་དང་སློབ་དཔོན་དག་གི༌[^1269]ལ་ནི་ཉེས་བྱས་སོ། །

[Block 2012]
ཆོས་དང་ལྡན་པ་ཉིད་མ་ཡིན་པའི་བསྒོ་བ་ལས་ཀྱང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་སློང་གི་དགེ་འདུན་གྱིས་བསྒོ་བའི་དོན་ཆོས་དང་ལྡན་པ་མ་ཡིན་པའི་བསྒོ་བ་ལས་འགལ་བར་བྱེད་པ་ལ་ཡང་ཉེས་བྱས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2013]
འདིར་གཞུང་ནི་ཞུ་བ་ལས།

[Block 2014]
བཙུན་པ་དགེ་སློང་གིས་དགེ་སློང་གནས་བརྟན་རྣམས་ཆོས་དང་ལྡན་པའི་བཀའ་མཆིད་རྣམ་པར་གཏན་ལ་འབེབས་པ་ན། གློ་བུར་དུ༌[^1270]བཀའ་མཆིད་མཆི་ལ་ལྟུང་བར་ཡང་མི་འགྱུར་བ༌[^1271]མཆིས་སམ། ཡོད་དེ་འདི་ལྟ་སྟེ་དགེ་སློང་གནས་བརྟན་དག་ཆོས་མ་ཡིན་པར་སྨྲ་ལ།[^1272] གསར་བུ་དག་ནི་ཆོས་སྨྲ་བས༌[^1273]གློ་བུར་དུ་གཏམ་ཟེར་ན་ཉེས་བྱས་སུ་གྱུར་པའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2015]
གཏམ་ཟེར་བ་ནི་དེ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་གཞན་དག་ལ་ཆོས་དང་ལྡན་པའི་གཏམ་རྣམ་པར་གཏན་ལ་འབེབས་པའི་བར་དུ་གློ་བུར་དུ་གཏམ་ཟེར་བ་ནི་དེའི་དེ་ཉིད་ནི་བསྒོ་བ་ལས་འགལ་བར་བྱེད་པ་ཉིད་ཡིན་ཏེ། ལྟུང་བྱེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2016]
གླེང་གཞི་ལས་འདི་རྣམ་པར་ཤེས་པ་ཡིན་ཏེ། གླང་ཆེན་ལྷས་ཀྱི་བདག་པོའི་བུ་ནག་པོ་གཏམ་གྱི་མཇུག་ཏུ་སྡོད་པར་མི་བྱེད་གུས་པར་བྱེད་ཅིང་ཕྱིར་སྨྲ་བར༌[^1274]བྱའོ་སྙམ་དུ་སེམས་སོ་ཞེས་བྱ་བའི་བར་དུ་གསུངས་པ་དང་། འདིར་ཞུ་བའི་གཞུང་ལས་ཀྱང་གསར་བུ་ཆོས་མ་ཡིན་པ་དག་གནས་བརྟན་ཆོས་སྨྲ་བ་རྣམས་ལ་གློ་བུར་དུ་གཏམ་ཟེར་བ་ནི་ལྟུང་བྱེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2017]
དགེ་འདུན་གྱི་ཐ་སྙད་པ་ནི་དེའི་ཁ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་གྱི་ཐ་སྙད་པ་ནི་དགེ་འདུན་གྱི་ཁ་ཡིན་ཏེ། དེ་བས་ན་དགེ་འདུན་ཉིད་ཀྱིས༌[^1275]བསྒོ་བ་གང་ཡིན་པ་དེ་ནི་དགེ་འདུན་གྱི་བསྒོ་བ་ཡིན་ཏེ། དགེ་འདུན་གྱི་ཐ་སྙད་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2018]
སངས་རྒྱས་ནི་དགེ་འདུན་དང་འདྲའོ་ཞེས་བྱ་བ་སངས་རྒྱས་ལ་མ་གུས་པ་ལས་ཁ་ན་མ་ཐོ་བ་ཡོངས་སུ་རྫོགས་པར་འགྱུར་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2019]
འདིར་གཞུང་ནི་ཤཱ་རིའི་བུ་ལྔ་པོ་རྣམས་ཀྱི་ཚིག་ནི་མི་བསྐྱེད་པ་ཞེས་བྱ་བ་སྟེ། དེ་བས་ན་མདོ་འདི་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 2020]
གང་གི་ཕྱིར་དགེ་འདུན་ལ་མ་གུས་པ་དང་སངས་རྒྱས་ལ་མ་གུས་པ་ནི༌[^1276]ཤིན་ཏུ་སྡིག་ཆེ་བ་ཡིན་ཏེ། གང་གི་ཚེ་ཚེ་དང་ལྡན་པ་མ་གྷ་དང་། བྷ་དྷ་ལ་ཡང་ལྟུང་བ་མ་བྱུང་བ་སྟེ། དེ་དག་ལ་མི༌[^1277]གུས་པ་ཉིད་མ་སྐྱེས་པའི་ཕྱིར་རོ། །

[Block 2021]
ཆོས་དང་ལྡན་པའི་གསོལ་བ་ཡང་སྦྱིན་པའི་ཕྱིར་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2022]
བསླབ་པ་རྣམས་ལ་མ་གུས་པའི་ཕྱིར་འགལ་བར༌[^1278]བྱེད་པའོ། །

[Block 2023]
གལ་ཏེ་སངས་རྒྱས་ལ་གུས་པ་མེད་ན་མི་རིགས་པར་འགྱུར་བ་འདིས་ཅི་ཞིག་བྱ། དེའི་ཚིག་གིས་བྱ་བ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ལྟུང་བྱེད་དོ། །

[Block 2024]
གལ་ཏེ་བསླབ་པ་ཙམ་ལ་ཅུང་ཟད་ཙམ་དང་། ངན་ངོན་ཙམ་འདིས་ཅི་ཞིག་ཅེས་བྱ་བ་ལ་སོགས་པས་བསླབ་པ་ལ་མ་གུས་པ་བསྐྱེད་པ་ནི་ཉེས་བྱས་སོ། །

[Block 2025]
ལྷག་མ་ལྔ་པོ་རྣམས་ཞེས་བྱ་བ་འདི་ལས་བསྡུ་བ་བྱ་སྟེ། རྒྱལ་པོ་དང་དགྲ་བཅོམ་པ་དང་དགེ་འདུན་གྱི་གནས་བརྟན་རྣམས་ཀྱི་ཚིག་རྣམ་པར་དཀྲུགས༌[^1279]པར་མི་བྱའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 2026]
མ་གུས་པའི་ཚུལ་གྱི་ལྟུང་བྱེད་དོ།། །།

[Block 2027]
ཅི་ཞིག་བྱས་ན་མྱོས་པར་འགྱུར་བ་འཐུང་བའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་མྱོས་པར་འགྱུར་བ་འཐུང་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བཏུང་བའི་ཚིག་གིས་འཐུང༌[^1280]ནའོ་ཞེས་བྱ་བ་སྨོས་པས་འཐུང་བར་བྱེད་པ་རྟོགས་པར་བྱའོ། །

[Block 2028]
དེ་བསྐོལ་ན་ནི་དེ་ཉིད་ལས་ཉམས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་མྱོས་པར་འགྱུར་བ་དེ་བསྐོལ་ན་ནི་མྱོས་པར་འགྱུར་བ་དེ༌[^1281]ཉིད་ལས་ཉམས་པ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏེ་བསྐོལ་བ་འཐུངས་པ་ལ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་འདིས་བསྡུས་པ་ཡིན་ནོ། །

[Block 2029]
སྦང་མ་དང་ཚིགས་མ་ཟ་བ་ལ་ནི་དེའི་འཇུག་པ་ཡོད་དོ་ཞེས་བྱ་བ་ནི་མྱོས་པར་འགྱུར་བའི་ལྟུང་བ་དེའི་འཇུག་པ་ཡོད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2030]
འདིར་གཞུང་ནི་སྦང་མ་ཟ་ན་ལྟུང་བྱེད་དོ། །

[Block 2031]
ཚིགས་མ༌[^1282]ཟ་ན་ལྟུང་བྱེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་འདིས་བསྡུས་པ་ཡིན་ནོ། །

[Block 2032]
ཕབས་ཀྱི་ཆང་བུ་ནི་ཕྱེད་ཉིད་དོ་ཞེས་བྱ་བ་ནི་མྱོས་པར་འགྱུར་བའི་ཕྱེད་ཉིད་དེ་ཉེས་བྱས་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2033]
རྩ་བ་དང་སྡོང་བུ་དང་འདབ་མ་དང་མེ་ཏོག་དང་འབྲས་བུ་མྱོས་པར་འགྱུར་བ་རྣམས་ཀྱང་ངོ་། །མྱོས་པར་འགྱུར་བའི་དྲི་དང་རོ་བྲོ་བའི་ཐུག་པ་མྱོས་པར་མི་བྱེད་པ་རྣམས་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་ཕྱེད་ཉིད་དོ་ཞེས་བྱ་ལ༌[^1283]འཇུག་གོ། །

[Block 2034]
མདོག་ཙམ་མྱོས་པར་འགྱུར་བ་དང་འདྲ་བ་ལ་ནི་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་འདིར་གཞུང་ལས་མདོག་འབའ་ཞིག་མྱོས་པར་འགྱུར་བ་དང་འདྲ་བ་འཐུང་བ་ལ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2035]
མཁུར་བར་བསྲེལ་བ་དང་ལུས་སྐུད་པ་ལ་ནི་སྦྱོར་བ་དང་འདྲའོ་ཞེས་བྱ་བ་ནི་ཟ་བར་མི་འདོད་པ་ལ་གང་ཞིག་ཡན་ལག་གི་རྒྱན་འཆང་བ་མེད་པ་ནི་དེར་སྦྱོར་བ་ཉིད་ལ་སྙམ་པའི་བློ་བཟློག་པའི་དོན་དུ་འདིར་འདི་གསུངས་པའོ།[^1284] །སྨན་པའི་ལུང་གིས་འདི་དག་བྱེད་པ་ལ་ལྟུང་བ་མེད་པའི་ཚིག་གང་ཡིན་པ་དེས་དོན་འདི་བསྟན་པ་ཉིད་དེ་དེ་བས་ན་མདོ་འདི་ཡིན་ཏེ། བ་སྤུའི་བུ་ག་རྣམས་ལ་བཟའ་བ་ཞུགས་པ་ལུས་སྐུད་པ་བསྒྲུབ་པ་ཞེས་བྱ་བ་ནི་འདིར་སྐྱོན་ནོ། །
--- END BLOCKS ---
