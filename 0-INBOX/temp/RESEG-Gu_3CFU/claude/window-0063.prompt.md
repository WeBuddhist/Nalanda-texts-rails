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
[Block 2206]
ཆེ་བ་ཉིད་ཀྱིས་རིན་ཐང་གདབ་པར༌[^1534]མི་ནུས་པ་ནི་རབ་ཀྱི་མཐར་ཕྱིན་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་རྡོ་རྗེ་ཕ་ལམ་ལ༌[^1535]སོགས་པ་རིན་པོ་ཆེ་གང་ཆེ་བ་ཉིད་ཀྱིས་རིན་ཐང་གདབ་པར་མི་ནུས་པ་དེ་ནི་རབ་ཀྱི་མཐར་ཕྱིན་པ་ཉིད་ཡིན་ཏེ། རྫས་དེ་ལ་རིག་པར་བྱའོ། །

[Block 2207]
མ་ཤ་ཀ་ལྔ༌[^1536]ལ་སོགས་པའི་རིན་ཐང་བཟློག་པར་མི་ནུས་པ་ཉིད་ཀྱི་ཕྱིར་འདིར་ཕམ་པ་འབྱུང་བར་བྱ་བ༌[^1537]གང་ཞིག་བསམ་པ་དེའི་འདོད་པ་བཟློག་པའི་དོན་དུ་མདོ་འདི་གསུངས་སོ། །

[Block 2208]
ཕམ་པ་ནི་འདི་རྐུ་བ་ཞེས་བྱ་བ་དགུག་པའི་དོན་ཏོ། །

[Block 2209]
ཆུང་བ་ཉིད་ཀྱིས་དེར་མི་ཆོག་པ་ནི་ཁོངས་སུ་མ་གཏོགས་པ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། དེའི་ཞེས་བྱ་བ་ནི་རིན་ཐང་གདབ་མི་ནུས་པ་ལ་སྟེ། གང་ཞིག་ལ་ཆུང་བ་ཉིད་ཀྱིས་རིན་ཐང་གདབ་པར་མི་ཆོག་པ་སྟེ། གང་ཞིག་མི་ཆོག་པ་ཉིད་ནི་དེར་ཁོངས༌[^1538]སུ་མ་བསྡུས་པ་ཉིད་མ་ཡིན་སྟེ། དེར་སྦོམ་པོའི་ལྟུང་བ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 2210]
དེ་ལ་སངས་རྒྱས་ཀྱི་སྐུ་གདུང་ནི་གཞལ་དུ་མེད་པའི་རིན་པོ་ཆེ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། གཞལ་དུ་མེད་པ་ནི་མི་ནུས་པ་སྟེ། རབ་ཀྱི་མཐར་ཕྱིན་པ་ཉིད་ཡིན་པའི་ཕྱིར་འདི་ཙམ་ཞེས་བྱ་བ་གང་ཞིག་གཞལ་བར་མི་ནུས་པའི་རིན་པོ་ཆེ་དེ་ནི་གཞལ་དུ་མེད་པ་སྟེ། སངས་རྒྱས་ཀྱི་སྐུ་གདུང་དེ་ཉིད་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2211]
དཔེར་ན་ནོར་བུའི་བདག་ཉིད་གཞལ་དུ་མེད་པའི་རིན་པོ་ཆེ་མིའི་རྒྱུད་ཀྱིས་ཡོངས་སུ་བཟུང་བ་ཞིག་རྐུ་སེམས་ཀྱིས་རྐུ་ན། གལ་ཏེ་དོན་ཇི་ལྟ་བ་བཞིན་དུ་འདི་ལ་དེའི་རིན་ཐང་རྣམ་པར་གནས་པ་ཡིན་ན་ནི་དེའི་ཚེ་ཕམ་པར་འགྱུར་རོ། །

[Block 2212]
གལ་ཏེ་དེའི་རིན་ཐང་དེ་བཞིན་དུ་གནས་པ་མ་ཡིན་ན་ལྟུང་བ་མ་ཡིན་ནོ། །

[Block 2213]
དེ་བཞིན་དུ་སངས་རྒྱས་ཀྱི་སྐུ་གདུང་ལ་ཞེས་བྱ་བ་དེ་ལ་འདི་བྱེད་པའོ། །

[Block 2214]
དེའི་གནས་ལ་ལུགས་སུ་གྱུར་པའི་དུས་དེ་ལ་གང་ཞིག་རྣམ་པར་གཞག་པ་དེས་འདིར་ལྟུང་བ་སྐྱེད་པར༌[^1539]རིག་པར་བྱའོ། །

[Block 2215]
གང་ཞིག་གང་ཟག་འགའ་ཞིག་ལ་གཅིག་གམ་དུ་མ་ལ་དོར་བྱེད་པ་ཉིད་ཀྱིས་འདིའི་རིན་ཐང་རྣམ་པར་གཞག་པ་འདི་ལ་བཟུང་བ་ཉིད་དང༌[^1540]ཞེས་བྱ་བ་དོར་བྱས་ནས་དེ་ལྟར་བྱ་སྟེ། རིན་ཐང་ཆེན་པོ་ལ་སྙིང་པོ་དེ་དང་ལྡན་པ་ཉིད་དུ་ཤེས་ནས་ཀྱང་གནས་གང་ལ་དོར་བྱེད་པ་ཉིད་ཀྱིས་ཐམས་ཅད་ཀྱིས་རིན་ཐང་ཆུང་བ་ཉིད་དུ་རྣམ་པར་གཞག་པ་དེ་ལ་ཡང་འཇིག་རྟེན་པའི་རིན་ཐང་ཉིད་ལྟུང་བ་བྱེད་པ་ཉིད་དོ། །

[Block 2216]
མཆོད་པའི་དོན་དུ་ནི་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ནི་འདིར་བདག་ཏུ་བྱ་བའི་བློས་ནི་མ་ཡིན་ལ་གཞན་གྱི་བློས་ཀྱང་མ་ཡིན་ལ་དེ་བས་ན་ཉེས་བྱས་བསྐྱེད་པ་སྟེ། ཕམ་པ་ཡང་མ་ཡིན་ལ་སྦོམ་པོ་ཡང་མ་ཡིན་ནོ། །

[Block 2217]
འདིར་གཞུང་ནི་ཇི་སྟེ་མཆོད་པའི་དོན་དུ་འདི་བདག་གི་སྟོན་པའོ། །

[Block 2218]
བདག་གིས་འདི་ལ་བཀུར་སྟི་བྱའོ་སྙམ་དུ་རྐུ་བར་བྱེད་ན་ཉེས་བྱས་ཀྱི་ལྟུང་བར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2219]
དཔེ་བྲི་བ་ལ་ནི་ཉེས་པ་མེད་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་མཐོང་ནས་གཞན་དུ་འདྲི་བ༌[^1541]ནི་དེའི་ཡི་གེ་ལ་སོགས་པ་འདྲི་བར༌[^1542]བྱ་སྟེ། ཡི་གེ་ལ་སོགས་པའི་མཚན་མ་དེ་བསྐུས་པས༌[^1543]བླངས་པ་ལ་སྐྱོན་མེད་པ་ཉིད་དེ་ལྟུང་བ་མི་བྱེད་པ་ཉིད་དོ། །

[Block 2220]
གཞན་དུ་འདྲི་བ༌[^1544]མཐོང་ནས་འདི་ལ་བཟུང་བའོ། །

[Block 2221]
འདིར་ནི་ཅུང་ཟད་གཞན་ལ་ཆད་པར་འགྱུར་བ་མ་ཡིན་ཏེ། འདྲི་བའི༌[^1545]སྣོད་བསྐུས་པ༌[^1546]ལ་ནི་རིན་ཐང་ཇི་ལྟ་བར་ལྟུང་བའོ། །

[Block 2222]
བཤིག་སྟེ་རྐུ་བ་ལ་ནི་དེའི་གནས་སྐབས་རྐུ་བའི་དངོས་པོ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གསེར་ལ་སོགས་པའི་རྫས་གང་ཞིག་བཤིག༌[^1547]པ་དེའི་གནས་སྐབས་རྐུ་བའི་དངོས་པོ་ཉིད་དོ། །

[Block 2223]
དེའི་གནས་སྐབས་ཞེས་བྱ་བ་འདི་ལ་རྐུ་བའི་བདག་ཉིད་ཅན་གྱི་སྦྱོར་བ་བདུན་དུ་དེས་སྦྱོར་བ་དང་བྲལ་བར་གྱུར་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2224]
འཇིག་པ་ལ་ནི་སྦོམ་པོ་སྟེ། འཇིག་པའི་རྣམ་པར་འགྱུར་བའི་གནས་སྐབས་ལ་རིན་ཐང་གང་ཡིན་པ་དེའི་དབང་གིས་ལྟུང་བ་ཞེས་བྱ་བ་དེ་ལ་འདི་བརྗོད་པའོ། །

[Block 2225]
འདིར་གཞུང་ནི་བཙུན་པ་དགེ་སློང་གིས་མི་རྣམས་ཀྱི་རིན་པོ་ཆེའམ༌[^1548]རིན་པོ་ཆེར་སྨོས་པའམ་གསེར་བཤིག་སྟེ་རྐུ་ན་ལྟུང་བ་ཅིར་འགྱུར། བཀའ་སྩལ་པ། རིན་ཐང་བརྩི་བར་བྱའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ནོ། །

[Block 2226]
དེ་དང་གནས་སྐབས་ཅན་ཉིད་ལ་རིན་ཐང་བརྩི་བར་བྱའོ་ཞེས་བྱ་བ་གསུངས་པའི་ཕྱིར་དོན་འདི་མངོན་པར་འདོད་ཅེས་བྱ་བ་འདི་ལྟར་དོན་བྱས་སོ། །

[Block 2227]
བྱང་གི་སྒྲ་མི་སྙན་ན་ནི་ཡོངས་སུ་འཛིན་པ་མེད་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་ཡོངས་སུ་འཛིན་པ་མེད་པའི་དངོས་པོ་ནི་རང་གི་བཞིན་དུ་བལྟ་བར་བྱའོ། །

[Block 2228]
དེ་ནི་རང་གི་དང་འདྲའོ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་རང་གི་རྫས་རྐུ་སེམས་ཀྱིས་བརྐུས་ན༌[^1549]ཉེས་པ་སྦོམ་པོར་འགྱུར་བ་བཞིན་དུ་འདི་ཡང་དེ་བཞིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2229]
ཞུ་བའི་སྐབས་འདིས་དངོས་པོའི་སྐབས་དང་། བདག་པོའི་སྐབས་དང་། རྗེས་སུ་སྒྲུབ་པའི་སྐབས་དང་། མཐར་ཐུག་པའི་སྐབས་ཞེས་བྱ་བའི་རྣམ་པ་བཞི་བསྡུས་པ་དེ་རྣམས་ལས་དེ་ཡན་ཆད་དུ་དངོས་པོའི་སྐབས་བཤད་ཟིན་ཏོ། །

[Block 2230]
ད་ནི་བདག་པོའི་སྐབས་བརྗོད་པར་བྱ་སྟེ། དེའི་དུས་ན་བདག་ཉིད་ཡོད་པ་བདག་པོ་ཉིད་དོ་ཞེས་བྱ་བ་ལ། དེའི་དུས་ཀྱི་ཞེས་བྱ་བ་ནི་རྐུ་བའི་དུས་ཀྱིའོ། །

[Block 2231]
མཆོད་རྟེན་ལས་བསྐུས་པ༌[^1550]ཡང་མིའི་རྒྱུད་ཀྱིས༌[^1551]ཡོངས་སུ་བཟུང་བ་མེད་པའི་ཕྱིར་ཡན་ལག་མ་ཡིན་པ་ཉིད་ལ་དངོས་པོ་ཚང་ན་ཉེས་པ་སྦོམ་པོར་འགྱུར་ཏེ་འདི་ནི་བསྡུས་པ་ཡིན་ནོ། །

[Block 2232]
མྱ་ངན་ལས་འདས་པ་ནི་ལྷ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་སླར་འདི་རྣམ་པར་ངེས་པར་ཕུང་པོ་ལྷག་མ་མེད་པའི་མྱ་ངན་ལས་འདས་པའི་དབྱིངས་སུ་ཡོངས་སུ་མྱ་ངན་ལས་འདས་པ་ནི་རྣམ་པར་དག་པའི་ལྷ་ཉིད་དུ་བཞེད་དོ། །

[Block 2233]
མྱ་ངན་ལས་འདས་པ་འབྱུང་བའི་དབང་གིས་དེར་ཕུང་པོ་སྤངས་པ༌[^1552]ལ་ཕུང་པོ་ལྷག་མ་མེད་པ་ལ་རྣམ་པར་དག་པའི་ལྷ་ཉིད་དུ་སྐྱེས་པ་ཉིད་དོ། །

[Block 2234]
མཆོག་ཏུ་བདེ་བའི་བདག་ཉིད་ཅན་ཉིད་ཀྱི་ཕྱིར་མྱ་ངན་ལས་འདས་པ་ལ་ཡང་ལྷ་ཉིད་ཁོ་ནར་རྣམ་པར་གནས་པ་ཡིན་ཞེས་བྱ་བའོ། །

[Block 2235]
བརྙན་པ་ངེས་པར་སྦྱིན་པ་ཉིད་བཞིན་དུ་ཉེ་བར་སྤྱོད་ན་སྦྱོར་བ་བཞིན་ནོ་ཞེས་བྱ་བ་ནི་གཞན་དུ་ནི་རྐུ་སེམས་མེད་པ་ཞེས་བྱ་བ་བསྟན་པའི་ཕྱིར་རྐུ་བའི་སེམས་ཀྱིས་ཞེས་བྱ་བ་འདིར་རྗེས་སུ་ཆགས་པར་རིག་པར་བྱའོ། །

[Block 2236]
དངོས་པོ་མ་ཆོག་པ་ཉིད༌[^1553]ལ་སྦོམ་པོའི་ལྟུང་བ་ལ་དངོས་གཞིར་བརྗོད་པའི་ཕྱིར་ཡོངས་སུ་རྫོགས་པ་ལ་སྦྱོར་བ་ཉིད་ཤེས་པར་བྱའོ། །

[Block 2237]
དོན་ཅི་ཞིག་གིས་དངོས་པོ་གང་ཞིག་གནང་བ་དེ་ཡང་ཇི་ལྟར་བསྲི་བ་མེད་པར་ཐམས་ཅད་ཉིད་ཀྱིས་བསྟན་པ་ལ་སྦྱིན་པར་བྱ་བ་མ་ཡིན་པ་ཉིད་ཀྱིས་ལོངས་སྤྱོད་པ་དེ་ནི་སྦྱོར་བ་བཞིན་དུ་བལྟ་བར་བྱའོ། །

[Block 2238]
དེ་ལྟ་བུའི་ཉེ་བར་ལོངས་སྤྱོད་པ་ལ་སྦོམ་པོའི་ལྟུང་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2239]
ཉེ་བར་སྤྱོད་ན་སྦྱོར་བ་བཞིན་ནོ་ཞེས་བྱ་བ་ནི་མ་ཆད་པའི་རྣམ་པ་ཡང་ཉེ་བར་སྤྱོད་པར་བྱ་བ་གཟུང་བ་དང་བཅས་པར་བྱ་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2240]
དེ་བས་ན་འདིར་སྦོམ་པོའི་ལྟུང་བའོ། །

[Block 2241]
མ་གནང་བ་ལ་བསྲི་བ་མེད་པ་ཉེ་བར་ལོངས་སྤྱོད་པ་ནི་ཤིན་ཏུ་ལྕི་བ་ཉིད་དེ་དེ་བས་ན་འདིར་ཡང་འདིས་སྦོམ་པོའི་ལྟུང་བ་བྱས་པ་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 2242]
འདིར་གཞུང་ནི་བཙུན་པ་དགེ་སློང་གིས༌[^1554]ཁྱིམ་བདག་གི་གོས་བརྙན་པ༌[^1555]བཏགས་ཏེ་རྐུ་ན་ལྟུང་བ་ཅིར་འགྱུར། ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ། །

[Block 2243]
ཅི་སྟེ་ཁྱིམ་བདག་འདི་སྐད་ཅེས་འཕགས་པ་བདག་ཉིད༌[^1556]འདི་ཁྱོད་ལ་བརྙན་ནོ་ཞེས་ཟེར་ན་དགེ་སློང་དེ་ལ་བསྲི་བ་མེད་པའི་འདུ་ཤེས་ཅན་དེ་ལ་ཡོངས་སུ་ལོངས་སྤྱོད་པར་བྱེད་ན་སྦོམ་པོའི་ལྟུང་བར་འགྱུར་ཞེས་བྱ་བ་འདིའི་འདི་བསྡུས་པའོ། །

[Block 2244]
འདི་ལས་སྔ་རོལ་གྱི་གཞུང་ལས་རུང་བ་ཞེས་བྱ་བའི་མདོ་འདི་བསྡུས་པའོ། །

[Block 2245]
གསང་སྔགས་དང་སྨན་དག་གིས་འབུལ་དུ་བཅུག་ན་ཡང་ངོ་ཞེས་བྱ་བ་ནི་སྦྱོར་བ་བཞིན་ནོ་ཞེས་བྱ་བ་དང་རྗེས་སུ་འབྲེལ་ཏོ། །
--- END BLOCKS ---
