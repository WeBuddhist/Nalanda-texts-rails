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
[Block 176 [HEADING]]
### བཟང་པོ་སྤྱོད་པའི་སྨོན་ལམ་གྱི་ཡན་ལག་རབ་ཏུ་དབྱེ་བ། ^2-8-0

[Block 177]
ད་ནི་དེའི་རབ་ཏུ་དབྱེ་བ་སྟེ་བརྒྱད་པའོ། །

[Block 178]
དེ་ཡང་བཟང་པོ་སྤྱོད་པའི་སྨོན་ལམ་གྱི་ཡན་ལག་རབ་ཏུ་དབྱེ་བ་སྟེ། དེ་དག་ནི་རྣམ་པ་བཅུ་དྲུག་གོ། །

[Block 179]
འདི་ལྟ་སྟེ། བསམ་པ་དང་། བྱང་ཆུབ་ཀྱི་སེམས་མི་བརྗེད་པ་དང་། ཆགས་པ་མེད་པར་སྦྱོར་བ་དང་། སེམས་ཅན་ལ་ཕན་གདགས་པ༌[^71]དང་། གོ་ཆ་བགོ་བ་དང་། སྐལ་བ་མཐུན་པའི་བྱང་ཆུབ་སེམས་དཔའ་བསྟེན་པ་དང་། དགེ་བའི་བཤེས་གཉེན་མགུ་བར་བྱེད་པ་དང་། དེ་བཞིན་གཤེགས་པ་མངོན་སུམ་དུ་བྱ་བ་དང་། དམ་པའི་ཆོས་ཡོངས་སུ་བསྡུ་བ་དང་། མི་ཟད་པའི་མཛོད་རྙེད་པ་དང་། འཇུག་པར་བྱ་བ་དང་། སྟོབས་དང་། གཉེན་པོ་དང་། ལས་དང་། རྗེས་སུ་སློབ་ཅིང་བསྔོ་བ་དང་། བསྡུ་བར་བྱ་བ་རྣམས་སོ། །

[Block 180 [HEADING]]
#### བསམ་པ། ^2-8-1-0

[Block 181]
དེ་ལ་བསམ་པ་ནི་རྣམ་པ་དང་པོ་སྟེ། དེ་ཡང་རྣམ་པ་གསུམ་མོ། །

[Block 182]
དེ་བཞིན་གཤེགས་པ་ལ་མཆོད་ཅིང་དགོངས་པ་ཡོངས་སུ་རྫོགས་པར་བྱ་བའི་བསམ་པ་ནི། འདས་པའི་སངས་རྒྱས་རྣམས་དང་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 183]
མཆོད་པར་གྱུར་ཅིག་ཅེས་བྱ་བ་ནི་བླ་ན་མེད་པའི་མཆོད་པས་སོ། །

[Block 184]
འདས་པར་བསྟན་པ་ནི་སངས་རྒྱས་བཅོམ་ལྡན་འདས་མྱ་ངན་ལས་འདས་པ་རྣམས་སོ། །

[Block 185]
གང་ད་ལྟར་ཕྱོགས་བཅུའི་འཇིག་རྟེན་ན་གནས་ཤིང་བཞུགས་པ་འཇིག་རྟེན་གྱི་ཁམས་སྣ་ཚོགས་ནི༌[^72]འགྲོ་བ་ཐམས་ཅད་ལ་ཕན་པ་དང་བདེ་བ་ལ་སྟོབས་པ༌[^73]ལ་བརྩོན་པ་དེ་དག་ལ་ཡང་དེ་བཞིན་དུ་མཆོད་པར་གྱུར་ཅིག་པའོ། །

[Block 186]
གང་ཕྱིས་འབྱོན་པར༌[^74]འགྱུར་བ་དེ་དག་གི༌[^75]བསམ་པ་ཀུན་རྫོགས་ནས་སངས་རྒྱས་ཀྱི༌[^76]བྱང་ཆུབ༌[^77]མྱུར་དུ་གྱུར་ཅིག་པའོ། །

[Block 187]
དེ་ལ་ཕྱེད་ཡན་ཆད་ནི་དེ་བཞིན་གཤེགས་པ་ལ་མཆོད་པར་བསམ་མོ། །

[Block 188]
ཕྱེད་མན་ཆད་ནི་དགོངས་པ༌[^78]རྫོགས་པར་བསམ་པ༌[^79]བསྟན་པའོ། །

[Block 189]
སངས་རྒྱས་ཀྱི་ཞིང་ཡོངས་སུ་རྫོགས་པར་བསམ་པ་ནི། ཕྱོགས་བཅུ་ག་ལའི་ཞིང་རྣམས་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། ག་ལའི་ཞེས་བྱ་བ་ནི་གང་ན༌[^80]ཡང་རུང་བའོ། །

[Block 190]
ཇི་སྙེད་པ་ཞེས་བྱ་བ་ནི་གང་དག་ཡོད་པའོ།[^81] །

[Block 191]
བདེ་བ་ཅན་གྱི་འཇིག་རྟེན་བཞིན་དུ་ཕྱོགས་བཅུའི་སངས་རྒྱས་ཀྱི་ཞིང་ཇི་སྙེད་ཡོད་པ་དེ་དག་ཐམས་ཅད་ཡོངས་སུ་དག་པར་གྱུར་ཅིག་པ་དང་སྣང་བ་མཐའ་ཡས་ཅི༌[^82]བཞིན་དུ་འཇིག་རྟེན་གྱི་ཁམས་ཐ་དད་པ་གཞན་ཡང་ཡངས་པར་གྱུར་ཅིག་པའོ། །

[Block 192]
བྱང་ཆུབ་ཀྱི་ཤིང་དྲུང་དུ་གཤེགས་པའི་རྒྱལ་བ་བཅོམ་ལྡན་འདས་རྣམས་དང་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱིས་ཀྱང་ཀུན་ཏུ་གང་ཞིང་བར༌[^83]མཚམས་མེད་པར་གྱུར་ཅིག་པའོ། །

[Block 193]
སེམས་ཅན་ཐམས་ཅད་ལ་ཕན་ཞིང་བདེ་བའི་བསམ་པ་ནི། ཕྱོགས་བཅུའི་སེམས་ཅན་གང་རྣམས་ཇི་སྙེད་པ། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། ཕྱོགས་བཅུའི་འཇིག་རྟེན་གང་ན་སྐྱེ་བ་རྣམ་པ་བཞིར་བསྡུས་པ་དང་། རྒྱུད་དྲུག་གི་སེམས་ཅན་དེ་དག་ཡུན་དུ་བདེ་བའི་མཆོག་གིས་བདེ་བར་གྱུར་ཅིག་པའོ། །

[Block 194]
ནད་མེད་པ་ནི་ལུས་དང་སེམས་ཀྱི་ནད་དང་རྟག་པར་བྲལ་བར་གྱུར་ཅིག་པའོ། །

[Block 195]
དེ་ལྟར་ཆོས་ཀྱི་རྙེད་པ༌[^84]དང་མཐུན་པ་ནི་ལྡན་པར་གྱུར་པའོ། །

[Block 196]
འགྲོ་བ་ཆོས་ཀྱི་བསམ་པ་ཅན་ཐམས་ཅད་འདི་ལྟར་རྟག་ཏུ་གྲུབ་པ་དང་ཕུན་སུམ་ཚོགས་པ་དང༌[^85]ལྡན་པར་གྱུར་ཅིག༌[^86]པའོ། །

[Block 197 [HEADING]]
#### བྱང་ཆུབ་ཀྱི་སེམས་མི་བརྗེད་པ། ^2-8-2-0

[Block 198]
བྱང་ཆུབ་ཀྱི་སེམས་མི་བརྗེད་པ་ནི་གཉེན་པོ་དང་བཅས་པ་དང་། མི་མཐུན་པའི་ཕྱོགས་སྤང་བར་བསྟན་པར༌[^87]རྣམ་པ་གཉིས་ཏེ། དེ་དག་ནི་ཚིགས་སུ་བཅད་པ་བཞི་སྟེ། བྱང་ཆུབ་སྤྱོད་པ་ཞེས་བྱ་བ་ནས་བཟུང་སྟེ། དེ་དག་མ་ལུས་ཡོངས་སུ་བྱང་བར་ཤོག །ཞེས་བྱ་བའི་བར་དུའོ། །

[Block 199]
བྱང་ཆུབ་ཅེས་བྱ་བ་ནི་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པར་བྱང་ཆུབ་བོ། །

[Block 200]
དེ་ལྟར་སྤྱོད་པའི་བྱང་ཆུབ་ཀྱི་སྤྱོད་པ་སྟེ། དེ་དག་སྤྱོད་ཅིང་སྒྲུབ༌[^88]པས་ན་འགྲོ་བ་ཀུན་དུ་ཡང་ཚེ་རབས་དྲན་པར་གྱུར་ཅིག །ཚེ་རབས་ཀུན་དུ་འཆི་འཕོ་སྐྱེ་བ་ན། །ཞེས་བྱ་བ་ནི་ཤི་ཞིང་སྐྱེས་པ་ན་ཡང་རྟག་ཏུ་བདག་རབ་ཏུ་འབྱུང་བར་གྱུར་ཅིག་པའོ། །

[Block 201]
སྐྱེས་ནས་ཤི་བའི་བར་ལ་བཤད་པར་བལྟ་བའོ། །

[Block 202]
འདི་ནི་བྱང་ཆུབ་ཀྱི་སེམས་མི་ཉམས་པའི་རྒྱུ་དང་དངོས་པོ་དང་པོའོ། །

[Block 203]
འདི་ལྟར། རྒྱལ་བ་ཀུན་གྱི་རྗེས་སུ་སློབ་གྱུར་ཏེ། །ཞེས་བྱ་བ་ནི་རྒྱལ་བ་དུས་གསུམ་དུ་གཤེགས་པ་ཐམས་ཅད་ཀྱིས་བསླབ་པའི༌[^89]རྗེས་སུ་སློབ་པའོ། །

[Block 204]
བཟང་པོ་སྤྱོད་པ་ཡོངས་སུ་རྫོགས་པར་བྱ་བའོ། །

[Block 205]
རྫོགས་པར་ཇི་ལྟར་བྱ་ཞེ་ན།

[Block 206 [VERSE]]
ཚུལ་ཁྲིམས་སྤྱོད་པ་དྲི་མེད་ཡོངས་དག་པར། །
རྟག་ཏུ་མ་ཉམས་སྐྱོན་མེད་སྤྱོད་པར་ཤོག །

[Block 207]
ཅེས་བྱ་བ་ནི་དཔེར་ན་ཡིད་བཞིན་གྱི་ནོར་བུ་རིན་པོ་ཆེ་གློ་བུར་གྱི་དྲི་མ་དང་བྲལ་བས་ན་དྲི་མ་མེད་པའོ། །

[Block 208]
གཡའི་སྐྱོན་ཀུན་བསལ་བས་ན་རང་བཞིན་གྱིས་ཡོངས་སུ་དག་པ་སྟེ། དེ་ལྟ་བས་ན་མ་ཉམས་སྐྱོན་མེད་པ་ཞེས་བྱ་བ་སྟེ། འདོད་པ་ཀུན༌[^90]ཕུན་སུམ་ལྡན་པར་བྱེད། གདུང་བ་ཀུན་ཡོངས་སུ་མེད་པར་བྱེད། ནད་ཐམས་ཅད་དང་བྲལ་བར་བྱེད་པའོ། །

[Block 209]
དེ་ལྟར་བྱང་ཆུབ་སེམས་དཔའི་ཚུལ་ཁྲིམས་ཀྱང་རིན་པོ་ཆེ༌[^91]བཞིན་དུ་གློ་བུར་གྱི་ལས་དང་ཉོན་མོངས་པ་དང་མ་འདྲེས་པས་ན་དྲི་མ་དང་བྲལ་བ་སྟེ་དྲི་མ་མེད་པའོ། །

[Block 210]
ཉན་ཐོས་དང་རང་སངས་རྒྱས་ཀྱི་ཐེག་པར་སེམས་བསྐྱེད་པའི་གཡའི་སྐྱོན་དང་བྲལ་ཞིང་ཐམས་ཅད་མཁྱེན་པའི་སེམས་བསྐྱེད་པ་རིན་པོ་ཆེ་བཞིན་དུ་ཀུན་དུ་དག་པས་ན་ཡོངས་སུ་དག་པའོ། །

[Block 211]
བྱང་ཆུབ་སེམས་དཔའི་སློབ་པ༌[^92]ལ་ཤིན་ཏུ་གུས་པར་བྱས་ནས་ཉེས་པ་མི་སྤྱོད་པས་ན་ཉམས་པ་མེད་པའི་ཕྱིར་ཉམས་པ་མེད་པའོ། །

[Block 212]
འདས་པའི་ཡུལ་ལ་རེ་བའི་སྲེད་པ་སྐྱེ་བ་དང་། མ་འོངས་པ་དང་ཚེ་ཕྱི་མ་རྣམས་སུ་སྨོན་པའི་སྲེད་པ་དང་། དེ་ལྟར༌[^93]བྱུང་བ་ལ་ཞེན་པའི་སྲེད་པ་སྟེ། དུས་གསུམ་གྱི་སྲེད་པའི་ཁབ་ཀྱིས་ཅུང་ཟད་དུ་ཡང་མ་གཙེས་པས་ན་སྐྱོན་མེད་པའོ། །

[Block 213]
ས་བཞིན་དུ་སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་ཀྱི་འདོད་པ་ཕུན་སུམ་ལྡན་པར་བྱེད་པ་དང་། ཐམས་ཅད་ཀྱི་གདུང་བ༌[^94]ཡོངས་སུ་སེལ་བ་དང་། ཐམས་ཅད་ཀྱི་ནད་འཇོམས་པ་དང་། ལྷ་དང་མི་རྣམས་ཀྱི་དོན་ཚད་མེད་པར་བསྒྲུབ་པ༌[^95]འབའ་ཞིག༌[^96]པ་ལ་འཇུག་པ་སྟེ། སྒྲའི་ཚུལ་དུའང་ལུས་དང་སེམས་ཀྱི་གདུང་བ་བསིལ་བར་བྱེད་པས་ན་ཚུལ་ཁྲིམས་སོ། །

[Block 214]
ཚུལ་ཁྲིམས་ནི་སྤྱད་པར་བྱ་བ་ཡིན་པས་ན་སྤྱོད་པ་ཞེས་བྱ་བའོ། །

[Block 215]
དེ་ལྟར་རྟག་པར་ནམ་བྱང་ཆུབ་ཀྱི་བར་དུ་སྤྱོད་པ་ནི་ཚུལ་ཁྲིམས་སྤྱོད་པ་དྲི་མ་མེད་པ༌[^97]ཡོངས་སུ་དག་པའམ་མ་ཉམས་པ་སྐྱོན་མེད་པར་སྤྱོད་པ་སྟེ། འདི་ནི་བྱང་ཆུབ་ཀྱི་སེམས་མི་བརྗེད་པའི་རྒྱུ་གཉིས་པའོ། །
--- END BLOCKS ---
