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
[Block 1 [HEADING]]
### ༄༅། །ཐེག་པ་ཆེན་པོ་བསྡུས་པའི་འགྲེལ་པ།

[Block 2 [HEADING]]
## ཀླད་ཀྱི་དོན། ^I-0

[Block 3]
༄༅༅། །རྒྱ་གར་སྐད་དུ། མ་ཧཱ་ཡཱ་ན་སང་གྲ་ཧ་བྷཱ་ཥྱཾ། བོད་སྐད་དུ། ཐེག་པ་ཆེན་པོ་བསྡུས་པའི་འགྲེལ་པ། བམ་པོ་དང་པོ། [^1]སངས་རྒྱས་ལ་ཕྱག་འཚལ་ལོ། །

[Block 4]
འཕགས་པ་འཇམ་དཔལ་གཞོན་ནུར་གྱུར་པ་ལ་ཕྱག་འཚལ་ལོ། །

[Block 5]
[^2]གང་ཞིག་ཤེས་བྱའི་སྒྲིབ་པ་མུན་པ་རབ་རིབ་དག་གིས་ཇི་སྙེད་ཇི་ལྟ་བར། །ཡོད་པ་དོན་དམ་ཀུན་རྫོབ་ཚུལ་གྱིས་ཆོས་གང་གཟུགས་བརྙན་གཞན་དུ་སྣང་གྱུར་པའི། །སེམས་ཅན་རྣམས་ལ་བསམ་པ་བཞིན་དུ་དྲི་མེད་ཐར་པའི་ཐབས་ནི་རྣམ་པ་གསུམ། །ཉོན་མོངས་བག་ཆགས་བཅས་པར་བཅོམ་པའི་དྲི་མེད་ཡང་དག་བྱང་ཆུབ་མཆོག་རྟོགས༌[^3]པ། །རྣམ་རྟོག་དྲ་བ་ཐམས་ཅད་སྤངས་པའི་དྲི་མེད་ཡེ་ཤེས་ཟེར་གྱིས་ཐོབ་གྱུར་ནས། །གང་གིས་ལྷུན་གྱིས་གྲུབ་པར་ཕྱོགས་བཅུ་རྣམས་སུ་རབ་ཏུ་སྟོན་ཀྱང་འཁོར་བ་ལ། །དེར་མི་རྟོག་པས་གནས་པ་མེད་ཅིང་སྙིང་རྗེ༌[^4]མྱ་ངན་འདས་ལ་མི་གནས་གང་། །ཐབས་དང་ཤེས་རབ་ཆེན་པོས་ཡོངས་སུ་གཟུང་བས་བདག་གཞན་དོན་གྱི་མཐར་བྱོན་དང་། །གང་ཡང་དམ་པའི་ཆོས་གང་བཅོམ་ལྡན་དེ་ཡིས་ཡང་དག་རྟོགས་ནས་ལེགས་བསྟན་པ། །གང་འདི་ལེགས་པར་སྒྲུབ་དང་ལྡན་པ་དེ་ཡིས་བདུད་རྩིའི༌[^5]གོ་འཕང་ཞི་བ་འཐོབ། །གང་ཞིག་སྤོང་བར་བྱེད་པ་དེ་ནི་སྡུག་བསྔལ་རྒྱ་མཚོར་ཡུན་རིང་ཤིན་ཏུ་འབྱིང་། །སློབ་དང་མི་སློབ་འབྲས་བུ་ལ་གནས་ལམ་དེ་ནས་སོང་དགེ་འདུན་གཞན་གྱི་མཆོག །གང་ཞིག་བདེ་གཤེགས་དགེ་འདུན་ཡོན་ཏན་དྲི་མེད་རིག་པའི་བརྟུལ་ཞུགས་ཀྱིས་བསྒྲུབ༌[^6]པ། །བླ་མེད་བསོད་ནམས་ཞིང་ལ་དགེ་བ་ཅུང་ཟད་ཕྲ་མོ་དག་ཀྱང་འདིར་བྱས་ན། །ས་དང་ནམ་མཁའ་རྒྱ་ཆེ་བ་ལྟར་མཁས་པ་རྣམས་ཀྱིས༌[^7]ཐར་པ་སྒྲུབ་པར་བྱེད། །དེ་དག་ལ་ནི་ལུས་ངག་ཡིད་ཀྱིས་ལན་ཅིག་མིན་པར་གུས་པས་ཕྱག་འཚལ་ལོ། །

[Block 6]
མཁས་པར་རློམ་པ་རང་གི་རྟོག་ལ་བརྟེན་པས་ལུང་དང་རྟོགས་པ་དཀྲུགས་གྱུར་ཅིང་། །དེ་ལྟར་ཡང་དག་དམ་ཆོས་ཚུལ་དཀྲུགས་པ་ལ་ཆོས་ཀྱིས༌[^8]རབ་ཏུ་སྣང་མཛད་པའི། །ཏིང་འཛིན་མི་གཡོ་འཇིག་རྟེན་འདས་ལ་བརྟེན་ནས་འཕགས་པ་བྱམས་པ་ལ་བརྙེས་པས། །སྔོན་ཆད་མ་བྱུང་བ་ཡི་དམ་ཆོས་སྟོན་པར་མཛད་པའི་སློབ་དཔོན་ལ་ཡང་ངོ་། །ཇི་ལྟར་ཉི་མ་ཕྱོགས་རྣམས་ཐམས་ཅད་ཀུན་ཏུ་འོད་ཟེར་དྲ་བ་འགྱེད་པ་ལྟར། །གང་གིས་ལེགས་པའི་གྲགས་པ་གཞུང་གི་འོད་ཟེར་དྲི་མེད་རྣམ་པར་སྤྲོ་བྱེད་དེ། །ཟབ་ཅིང་དོན་ཆེ་བཟང་ལ་སྣ་ཚོགས་ཚིག་བཟང་ངེས་པའི་དོན་གྱི་མདོ་ལས་བྱུང་། །གང་ཞིག་སྐྱེ་བོ་མཁས་པ་རང་དགའ་མེད་པ་དྲང་བ་མཉེན་ཞིང་གུས་པར་བྱེད། །ཤིན་ཏུ་རྟོགས་པར་དཀའ་བའི་ཆོས་དེ་ཉིད་ལའང་གང་གི་བློ་ནི་ཐོགས་མེད་ལ། །རྙེད་དང་གྲགས་པ་དང་ནི་བསྟོད་དང་བདེ་བ་རྣམས་ལའང་ཆགས་པ་རྟག་མེད་པའི། །གང་གིས༌[^9]མིང་ཡང་ཡོན་ཏན་རྗེས་མཐུན་ངེས་པ༌[^10]མཁས་པ་དག་གིས་བརྟག༌[^11]བརྗོད་དེ། །གང་ཞིག་ཐོགས་མེད་ཅེས་ནི་མི་དང་ལྷ་ཡིས་གྲགས་པའི་ཡོན་ཏན་རྗོད༌[^12]བྱེད་པ། །མི་ཟད་བློ་ལས་དམ་ཆོས་ཚིག་དོན་བདུད་རྩིའི་ཆར་འབབ་པ་ལས་ཕྱོགས་གཅིག་ཉིད། །ཐོས་ཏེ་བྱིའུ་ལྟ་བུར་རང་གི་ནུས་པ༌[^13]ཅུང་ཞིག་གང་ཡང་ཅི་བཟུང༌[^14]དང་། །བསྡུ་བ་གཏན་ལ་དབབ་པར་ཤིན་ཏུ་རྒྱས་པར་བསྟན་ལས་ཅུང་ཞིག་བརྗོད་པར་བྱ། །དེས་ཀྱང་ལ་ལ་ཤིན་ཏུ་རྒྱས་པའི་གཞུང་གི་རྒྱ་མཚོས་སྐྲག་པའི་དོན་བྱེད་སྲིད། །

[Block 7 [HEADING]]
## མདོའི་མིང་བསྟན་པ། ^II-0

[Block 8]
འདི་ལྟར་སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས་ཀྱི་གསུང་ཁྱད་པར་རྣམ་པ་བཅུས་ཁྱད་པར་དུ་འཕགས་པ་གསུངས་ཏེ་ཞེས་བྱ་བ་དོན་ཅི་ལས་བརྩམས་ནས་རྒྱུ་གང་གིས་བརྗོད་ན། ཤིན་ཏུ་ཡངས་པའི་ཤེས་བྱ་ཆོས་ཀྱི་རང་བཞིན་ཟབ་ཅིང་རྒྱ་ཆེ་བ་ཉིད་སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའི་མཐུས་བརྗོད་ཀྱི་གཞན་དུ་ན་ག་ལ་ནུས། ཡང་གང་གིས་ན་བསྟན་བཅོས་འདི་རིམ་པ་འདི་ལྟར་བསྟན་ན་གང་གི་ཕྱིར་ཆོས་མངོན་པ་སྨོས་པ་མེད་ན་འདི་གཙུག་ལག་ཉིད་དུ་མི་ཤེས་པ༌[^15]དེས་ན་དེའི་ཕྱིར་དང་། མདོའི་མིང་བསྟན་པའི་ཕྱིར་ཏེ། ས་བཅུ་པ་བཞིན་དུ་ཆོས་མངོན་པ་ཐེག་པ་ཆེན་པོའི་མདོ་ཞེས་བསྟན་ཏོ། །

[Block 9]
གཞན་ཡང་གཙུག་ལག་ཉིད་དུ་ཤེས་པར་བྱ་བའི་ཕྱིར་ཆོས་མངོན་པ་ཞེས་བྱའོ། །

[Block 10]
ད་ནི་མདོ་བརྩམས་པའི༌[^16]དགོས་པ་ནི་མ་རྟོགས་པ་རྣམས་ཀྱིས་རྟོགས་པར་བྱ་བའི་ཕྱིར་ཏེ། ཆོས་མངོན་པའི་མདོ་སྨོས་པ་ནི་འདིས་ཆོས་ཀྱི་རྣམ་གྲངས་བརྗོད་པར་བྱ་བའི་དོན་དང་། མདོའི་མིང་བསྟན་པའི་ཕྱིར་རོ། །

[Block 11]
ཐེག་པ་ཆེན་པོ་སྨོས་པ་ནི་ཡང་ཉན་ཐོས་ཀྱི་ཆོས་མངོན་པ་བཙལ་བའི༌[^17]ཕྱིར་ཏེ། གང་གི་ཕྱིར་ཆོས་མངོན་པ་ཀུན་གཙུག་ལག་མ་ཡིན་ནོ་ཞེས་ལོག་པར་རྟོག་པའི་ཕྱིར་རོ། །

[Block 12]
དེ་ཡང་ཁ་ཅིག་རང་གི་རྟོག་པའི་བློ་དག་གིས་ཆོས་མངོན་པ་སངས་རྒྱས་ཀྱིས་གསུངས་པར་འདོད་དོ། །

[Block 13]
ཁ་ཅིག་ནི་ཉན་ཐོས་ཀྱིས་བསྟན་པ་དང་། མཁས་པ་དག་གིས་བྱས་པར་འདོད་དོ། །

[Block 14]
ཐེག་པ་ཆེན་པོའི་མདོ་ཞེས་བྱ་བ་འདིས་ནི་ཉན་ཐོས་ལ་སོགས་པ་ལས་ཁྱད་པར་དུ་འཕགས་པ་ཉིད་སྟོན་ཏོ། །

[Block 15]
ཡང་ཆོས་མངོན་པ་སྨོས་པ༌[^18]ནི་བྱང་ཆུབ་སེམས་དཔའི་སྡེ་སྣོད་གཟུང༌[^19]ངོ་། །ཡང་བྱང་ཆུབ་སེམས་དཔའི་སྡེ་སྣོད་བཟུང་བས་ནི་རང་གི་ཐེག་པ་ཆེན་པོ་ལས་རང་གི་ཉོན་མོངས་པ་འདུལ་བར་ཡང་དག་པར་སྣང་ངོ་། །གང་ཐེག་པ་ཆེན་པོར་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ཉོན་མོངས་པ་ནི་རྣམ་པར་རྟོག་པ་ཉིད་ཉོན་མོངས་པ་ཡིན་པས་བྱང་ཆུབ་སེམས་དཔའི་ཆོས་མངོན་པ་ནི་རྒྱ་ཆེ་ཞིང་ཟབ་པའི་མཚན་ཉིད་ཅན་ཉིད་དོ། །

[Block 16]
དེ་ལ་སྡེ་སྣོད་གསུམ་ནི་མདོ་སྡེ་དང་། འདུལ་བ་དང་། མངོན་པའོ། །

[Block 17]
གསུམ་པོ་དེ་དག་ཉིད་ཐེག་པ་དམན་པ་དང་། ཐེག་པ་མཆོག་གི་བྱེ་བྲག་གིས་གཉིས་སུ་འགྱུར་ཏེ། ཉན་ཐོས་ཀྱི་སྡེ་སྣོད་དང་། བྱང་ཆུབ་སེམས་དཔའི་སྡེ༌[^20]སྣོད་དོ། །

[Block 18]
ཡང་དེ་ནི་གསུམ་ཡང་རུང་གཉིས་ཀྱང་རུང་སྟེ། ཅིའི་ཕྱིར་སྡེ་སྣོད་ཅེས་བྱ་ན། བསྡུས་པའི་ཕྱིར་ཏེ། ཤེས་བྱ་མ་ལུས་པའི་དོན་བསྡུས་པ་ཉིད་ཀྱིས་སོ། །

[Block 19]
རྒྱུ་གང་གིས་གསུམ་ཡིན་ན་རྒྱུ་དགུ་སྟེ། ཐེ་ཚོམ་གྱི་གཉེན་པོ་ཡིན་པས་ན་མདོ་སྡེ་སྟེ། གང་དོན་གང་ལ་ཐེ་ཚོམ་ཟ་བ་དེའི་དོན་དེ་ངེས་པར་བསྟན་པའི་ཕྱིར་རོ། །

[Block 20]
མཐའ་གཉིས་སུ་སྦྱོར་བའི་གཉེན་པོས་ན་འདུལ་བ་སྟེ། ཁ་ན་མ་ཐོ་བ་དང་བཅས་པའི་ལོངས་སྤྱོད་བཀག་པས་འདོད་པའི་བསོད་ཉམས༌[^21]ལ་སྦྱོར་བའི་མཐའ་སྤོང་བ་ཉིད་དང་། ཁ་ན་མ་ཐོ་བ་མེད་པའི་ལོངས་སྤྱོད་རྗེས་སུ་གནང་བས་བདག་ཉིད་ངལ་བའི་མཐའ་ལ་སྦྱོར་བ་སྤོང་བའི་ཕྱིར་རོ། །

[Block 21]
བདག་གི་ལྟ་བ་མཆོག་ཏུ་འཛིན་པའི་གཉེན་པོས་ན་ཆོས་མངོན་པ་སྟེ། ཕྱིན་ཅི་མ་ལོག་པའི་ཆོས་ཀྱི་མཚན་ཉིད་གསལ་བར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 22]
ཡང་བསླབ་པ་གསུམ་སྟོན་པས་ན་མདོ་སྡེའོ། །

[Block 23]
ལྷག་པའི་ཚུལ་ཁྲིམས་དང་། ལྷག་པའི་སེམས་ཡང་དག་པར་སྒྲུབ་པས་འདུལ་བ་སྟེ། ཚུལ་ཁྲིམས་དང་ལྡན་པ་ནི་འགྱོད་པ་ལས༌[^22]རབ་ཏུ་འདའ་བས་ཏིང་ངེ་འཛིན་འཐོབ་པའི་ཕྱིར་རོ། །

[Block 24]
ལྷག་པའི་ཤེས་རབ་ཡང་དག་པར་སྒྲུབ་པས་ཆོས་མངོན་པ་སྟེ། ཕྱིན་ཅི་མ་ལོག་པའི་དོན་ལ་རབ་ཏུ་རྟོགས་པའི༌[^23]ཕྱིར་རོ། །

[Block 25]
ཡང་ཆོས་དང་དོན་རྟོགས་པས༌[^24]མདོ་སྡེའོ། །

[Block 26]
ཆོས་དང་དོན་སྒྲུབ་པས་འདུལ་བ་སྟེ། ཉོན་མོངས་པ་འདུལ་བ་དང་ལྡན་པ་ནི་དེ་རྟོགས་པ༌[^25]ལས་སོ། །

[Block 27]
ཆོས་དང་དོན་རྣམ་པར་གཏན་ལ་དབབ་པ་ལ་མཁས་པས་ན་ཆོས་མངོན་པ་སྟེ། རྒྱུ་དགུ་པོ་དེ་དག་གིས་ན་སྡེ་སྣོད་ནི་གསུམ་དུ་འདོད་དོ། །

[Block 28]
དེ་དག་གིས་ཀྱང་འཁོར་བ་ལས་རྣམ་པར་གྲོལ་བར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 29]
ཡང་ཇི་ལྟར་ན་དེ་དག་གིས་རྣམ་པར་གྲོལ་བར་བྱེད་ཅེ་ན། བསྒོ་བ༌[^26]དང་། རྟོགས་པ་དང་། འཇིལ་བ་དང་། རབ་ཏུ་འབྱེད་པས༌[^27]རྣམ་པར་གྲོལ༌[^28]བར་བྱེད་པ་ཉིད་དོ། །

[Block 30]
ཐོས་པས་ནི་སེམས་ལ་བསྒོ་བ་ཉིད་དོ། །

[Block 31]
བསམ་པས་ནི་རྟོགས་པ་ཉིད་དོ། །

[Block 32]
ཞི་བའི་དོན་ཏུ་སྒོམ་པའི་ཕྱིར་འཇིལ་བ་ཉིད་དོ། །

[Block 33]
ལྷག་མཐོང་གིས་ནི་རབ་ཏུ་འབྱེད་པ་ཉིད་དོ། །

[Block 34]
མདོར་བསྡུ༌[^29]ན་མདོ་སྡེ་དང་། འདུལ་བ་དང་། ཆོས་མངོན་པ་དེ་དག་སོ་སོ་ཞིང་དོན་རྣམ་པ་བཞི་སྟེ། བྱང་ཆུབ་སེམས་དཔའ་དེ་རྣམས་རྟོགས་ན་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཐོབ་པར་འགྱུར་རོ། །

[Block 35]
ཉན་ཐོས་ཀྱིས་ནི་ཚིགས་སུ་བཅད་པ་གཅིག་གི་དོན་ཤེས་པས་ཀྱང་ཟག་པ་ཟད་པ་འཐོབ་བོ། །

[Block 36]
དེ་ལྟར་སོ་སོ་ཞིང་དོན་རྣམ་པ་བཞི་ཡིན་ཞེ་ན། གནས་དང་མཚན་ཉིད་དང་། ཆོས་དང་དོན་མདོར་སྟོན་པས་ན། མདོ་སྡེའོ། །

[Block 37]
དེ་ལ་གནས་ནི་ཡུལ་གང་དུ་གང་གིས་གང་ལ་བསྟན་པའོ། །

[Block 38]
མཚན་ཉིད་ནི་ཀུན་རྫོབ་ཀྱི་བདེན་པའི་མཚན་ཉིད་དང་། དོན་དམ་པའི་བདེན་པའི་མཚན་ཉིད་དོ། །

[Block 39]
ཆོས་ནི་ཕུང་པོ་དང་། སྐྱེ་མཆེད་དང་། ཁམས་དང་། རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་དང་། ཟས་དང་། བསམ་གཏན་དང་། ཚད་མེད་པ་དང་། རྣམ་པར་ཐར་པ་བརྒྱད་དང་། ཟིལ་གྱིས་གནོན་པའི་སྐྱེ་མཆེད་དང་། ཟད་པར་གྱི་སྐྱེ་མཆེད་དང་། བྱང་ཆུབ་ཀྱི་ཕྱོགས་དང་། སོ་སོ་ཡང་དག་པར་རིག་པ་ལ་སོགས་པའོ། །

[Block 40]
དོན་ནི་རྗེས་སུ་བརྗོད་པའོ། །
--- END BLOCKS ---
