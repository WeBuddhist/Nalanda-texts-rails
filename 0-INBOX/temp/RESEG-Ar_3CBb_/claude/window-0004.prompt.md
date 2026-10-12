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
[Block 141]
འདིས་ནི་བསྐྱེད་པའི་རིམ་པ་ཡང་གཟུང་བར་བྱའོ། །

[Block 142]
རིམ་པ་དང་པོ་ཞེས་སྨོས་པ་མ་ཡིན་ནམ། དེ་ཅིའི་ཕྱིར་གཉི་ག་ལ་དང་པོ་ཞེས་བརྗོད་ཅེ་ན་འདི་ནི་རྫོགས་པའི་རིམ་པ་འབའ་ཞིག་གི་དབང་དུ་བྱས་པ་ཡིན་གྱི། བསྐྱེད་པའི་རིམ་པ་དང་ཐུན་མོང་དུ་ནི་མ་ཡིན་ནོ། །

[Block 143]
རིམ་པ་དང་པོ་ཞེས་བྱ་བ་འདི་ཡང་གང་ཞིག་ཅེ་ན། འདི་ནི་རྡོ་རྗེ་བཟླས་པ་ཉིད་དོ། །

[Block 144]
རིམ་པ་གཉིས་པ་བརྗོད་པའི་ཕྱིར།

[Block 145 [VERSE]]
སེམས་ལ་དམིགས་པ་ཙམ་ཞིག་ནི། །
རིམ་པ་གཉིས་པ་ཞེས་བརྗོད་དོ། །

[Block 146]
ཞེས་པ་སེམས་ལ་དམིགས་པས་ན། སེམས་ལ་དམིགས་པ་སྟེ། གང་གི་སེམས་ཡུལ་དུ་བྱས་པས་ན། སེམས་ལ་དམིགས་པའོ། །

[Block 147]
རིམ་པ་གཉིས་པ་ཞེས་པ་ནི། རྡོ་རྗེ་བཟླས་པ་ལ་ལྟོས་པའི༌[^81]རིམ་པ་གཉིས་སོ། །

[Block 148]
ཙམ་ཞེས་པ་ནི་དགག་པ་སྨོས་པ་སྟེ། སེམས་ལ་དམིགས་པ་ཙམ་ཞིག་རིམ་པ་གཉིས་པ་ཡིན་གྱི། གཞན་ནི་མ་ཡིན་ནོ། །

[Block 149]
དེ་ནས་རིམ་པ་གསུམ་པ་བསྟན་པའི་ཕྱིར།

[Block 150 [VERSE]]
ཀུན་རྫོབ་བདེན་པ་བསྟན་པ་ནི། །
ཡིད་དང་རིམ་པ་གསུམ་པའོ། །

[Block 151]
ཞེས་པ་གང་རྒྱུ་རྐྱེན་གྱིས་བསྐྱེད་པ་བརྫུན་པར་སྣང་བ་ནི་ཀུན་རྫོབ་སྟེ། ཀུན་རྫོབ་དེའི་དབང་དུ་བྱས་ནས༌[^82]བདེན་པས་ན་བདེན་པའོ། །

[Block 152]
རིམ་པ༌[^83]

[Block 153]
གཉིས་པ་ལ་ལྟོས༌[^84]ནས་འདི་རིམ་པ་གསུམ་པའོ། །

[Block 154]
འདིས་ནི་ཅིག་ཅར་གྱིས་འབྱུང་བའི་སྒྱུ་མ་ལྟ་བུའི་སྐུ་གཟུང་ངོ་། །དེ་ནས་རིམ་པ་བཞི་པ་བསྟན་པའི་ཕྱིར།

[Block 155 [VERSE]]
ཀུན་རྫོབ་བདེན་པ་དག་པ་ནི། །
རིམ་པ་བཞི་པ་ཞེས་བརྗོད་དོ། །

[Block 156]
ཞེས་པ༌[^85]རིལ་པོར་འཛིན་པ་དང་། རྗེས་སུ་གཞིག་པའི་སྟོབས་ཀྱིས་སྒྱུ་མ་ལྟ་བུའི་སྐུ་རང་བཞིན་གྱིས་རྣམ་པར་དག་པ་འདི་ནི་འོད་གསལ་བ་སྟེ། རིམ་པ་བཞི་པའོ། །

[Block 157]
རིམ་པ་བཞི་པའི་དུས་སུ་ནི་བདེན་པ་རྣམ་པ་གཉིས་ཀྱི་ཚུལ་དུ་གནས་པ་སྟེ། འདི་ལྟར་མཉམ་པར་གཞག་པ་ནི་དོན་དམ་པའི༌[^86]བདེན་པའོ། །

[Block 158]
དེའི་རྗེས་ལས་ཐོབ་པའི་སྐུ་ནི་ཀུན་རྫོབ་ཀྱི་བདེན་པའོ། །

[Block 159]
དེ་ནས་རིམ་པ་ལྔ་པ་བསྟན་པའི་ཕྱིར།

[Block 160 [VERSE]]
བདེན་པ༌[^87]གཉིས་སྦྱོར༌[^88]གང་ཡིན་པ། །
ཟུང་འཇུག་ཅེས་བྱ་ལྔ་པ་སྟེ། །

[Block 161]
ཞེས་བྱ་བ་སྨོས་ཏེ། དོན་དམ་པའི་བདེན་པ་དང་། ཀུན་རྫོབ་ཀྱི་བདེན་པ་རྣམ་པ་གཉིས་སུ་དབྱེར་མེད་པར་རྟོགས་པ་འདི་ནི་ཟུང་དུ་འཇུག་པ་སྟེ་རིམ་པ་ལྔ་པའོ། །

[Block 162]
དེ་ནས་སྒྲུབ་ཐབས་ཀྱི་ཆེ་བ་བསྟན་པའི་ཕྱིར། འདི་ནི་སྒྲུབ་པའི་ཐབས་ཀྱི་མཆོག །ཅེས་པ་བསྐྱེད་པའི་རིམ་པ་དང་། རྫོགས་པའི་རིམ་པ་འདི་ནི་སྒྲུབ་ཐབས་ཐམས་ཅད་ཀྱི་མཆོག་ཡིན་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། དངོས་གྲུབ་གཉིས་ཀྱི་རྒྱུར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 163]
རྒྱུད་ཀུན་གྱི་ནི་དོན་བསྡུས་པའོ། །ཞེས་པ། དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་རྒྱུད་ནི་ལམ་དང་འབྲས་བུ་གཉིས་ལས་མི་འདའ་ལ། བསྐྱེད་པ་དང་རྫོགས་པའི་རིམ་པ་འདི་ཡང་ལམ་དང་འབྲས་བུ་གཉིས་དང་ལྡན་པའི་ཕྱིར་རྒྱུད་ཀྱི་དོན་བསྡུས་པའོ། །

[Block 164]
ཡང་ན་རྒྱུད་ནི་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་གསང་བ་འདུས་པའོ། །

[Block 165]
དེའི་ཡན་ལག་ནི་ལྷ་མོ་བཞིས་ཞུས་པ་ལ་སོགས་པའོ། །

[Block 166]
དེའི་དོན་མདོར་བསྡུས་པ་ནི་ལམ་འབྲས་བུ་དང་བཅས་པའོ། །

[Block 167]
ལམ་ནི༌[^89]རྣམ་པ་གཉིས་ཏེ་སྨིན་པ་དང་གྲོལ་བར་བྱེད་པའི་ལམ་མོ། །

[Block 168]
སྨིན་པར་བྱེད་པའི་ལམ་ནི་རྣམ་པ་བཞི་སྟེ། བུམ་པའི་དབང་དང་། གསང་བའི་དབང་དང་། ཤེས་རབ་ཡེ་ཤེས་ཀྱི་དབང་དང་། དབང་བཞི་པའོ། །

[Block 169]
གྲོལ་བར་བྱེད་པའི་ལམ་ནི་རྣམ་པ་བཞི་སྟེ།[^90] དེ་ཁོ་ན་ཉིད་ཀྱི༌[^91]ཏིང་ངེ་འཛིན་དང་གྲོགས་སྤྱོད་པའོ། །

[Block 170]
དེ་ཁོ་ན་ཉིད་ཀྱི་ཏིང་ངེ་འཛིན་ལ་གཉིས་ཏེ། བསྐྱེད་པའི་རིམ་པ་དང་། རྫོགས་པའི་རིམ་པའོ།[^92] །རྫོགས་པའི་རིམ་པ་ལ་རྣམ་པ་ལྔ་སྟེ། རྡོ་རྗེ་བཟླས་པ་ལ་སོགས་པའོ། །

[Block 171]
སྤྱོད་པ་ནི་རྣམ་པ་གསུམ་སྟེ། སྤྲོས་པ་དང་བཅས་པ་དང་། སྤྲོས་པ་མེད་པ་དང་། ཤིན་ཏུ་སྤྲོས་པ་མེད་པའོ། །

[Block 172]
འབྲས་བུ་ནི་རྣམ་པ་གཉིས་ཏེ། འབྲས་བུ་གནས་སྐབས་པ་དང་། འབྲས་བུ་མཐར་ཐུག་པའོ། །

[Block 173]
ཐུན་མོང་གི་དངོས་གྲུབ་འབའ་ཞིག་པ་ནི་འབྲས་བུ་གནས་སྐབས་པའོ། །

[Block 174]
མཆོག་གི་དངོས་གྲུབ་ནི་འབྲས་བུ་མཐར་ཐུག་པའོ། །

[Block 175]
འདི་དག་ནི་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་རྒྱུད་ཀྱི་དོན་མདོར་བསྡུས་པའོ། །

[Block 176]
སྔགས་དང་སེམས་དང་ལུས་དང་ནི། །ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་བཤད་ཟིན་ཏོ། །

[Block 177]
མདོར་བསྡུས་པ་ཞེས་བྱ་བ་འདི་ཡང་འོག་ནས་འབྱུང་བའི་དོན་ཉིད་ཡིན་ནམ་དེ་ལས་གཞན་ཞིག་ཡིན་ཞེ་ན། ཕྱོགས་དང་པོ་ལྟར་ནི་མ་ཡིན་ཏེ། དོན་མེད་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 178]
ཕྱོགས་ཕྱི་མ་ལྟར་ན་ཡང་རྒྱུད་འདི་ཉིད་ཀྱི་དོན་མདོར་བསྡུས་པ་ཞེས་འབྱུང་བའི་ཕྱིར་རོ་ཞེ་ན་མ་ཡིན་ཏེ། གང་ཟག་ཐམས་ཅད་ནི་རིགས་རྣམ་པ་གཉིས་ཏེ། དབང་པོ་རྣོན་པོ་མགོ་སྨོས་པས་གོ་བའི་གང་ཟག་དང་། དབང་པོ་རྟུལ་པོ་དོན་མཐའ་དག་ལ་གཞོལ་བའི་གང༌[^93]ཟག་གོ། །

[Block 179]
རེ་ཞིག་དབང་པོ་རྟུལ་པོ་དོན་མཐའ་དག་ལ་གཞོལ་བའི་དབང་དུ་ནི་མ་ཡིན་ཏེ། གོང་མའི་སྐྱོན་ཉིད་དུ་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 180]
འདི་ནི་དབང་པོ་རྣོན་པོ་མགོ་སྨོས་པས་གོ་བའི་དབང་དུ་བྱས་པའོ། །དེ་ཅིའི་ཕྱིར་ཞེ་ན། དབང་པོ་རྣོན་པོ་ནི་དེ་ཙམ་གྱིས་གོ་བར་འགྱུར་བ་དང་། དོན་རྒྱ་ཆེན་པོ་ལ་འཇུག་པར་མི་འགྱུར་བའི་ཕྱིར་རོ། །
--- END BLOCKS ---
