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
[Block 36 [HEADING]]
### མཛེས་མ། ^3-1-0

[Block 37]
མཛེས་མ་མཆོག་ལྡན༌[^7]ཁྱེར་ནས་རབ་ཏུ་མྱུར་བསྒྲུབས་པས། །ཞེས་བྱ་བ། མཚོན་བྱེད་བརྡའི་བདག་མེད་མའི་དབང་དུ་བྱས་ནས་མཛེས་མ་ནི་ལུས་སོ། །

[Block 38]
མཆོག་ནི་ངག་དང་སེམས་སོ། །

[Block 39]
དེ་གསུམ་གྱི་ཡོན་ཏན་དང་ལྡན་པའོ། །

[Block 40]
ཁྱེར་བ་ནི་དབེན་པ༌[^8]ལ་སོགས་པར་རོ། །

[Block 41]
དེར་རབ་ཏུ་སྒྲུབ་མྱུར་དུ་སྒྲུབ་ཅེས་བྱའོ། །

[Block 42]
པས་ཞེས་བྱ་བ་ནི་དེ་ལྟར་བསྒྲུབས་པས་ས་ཧ་ཛ་འོད་གསལ་ཉམས་སུ་མྱོང་ཞེས་བྱའོ། །

[Block 43]
ཇི་ལྟར་མྱོང་བ་འོག་ནས་བཤད་པར་བྱའོ། །

[Block 44]
མཚོན་བྱའི་བདག་མེད་མ་དེ་ནི་མཛེས་མ་མཆོག་ནི་འོད་གསལ་དང་ས་ཧ་ཛའོ། །

[Block 45]
ལྡན་པ་ནི་ཟག་མེད་ཀྱི་ཡོན་ཏན་དང་ལྡན་པའོ། །

[Block 46]
དེ་ལྟར་ད་གཉིས་ཟུང་འཇུག་ཏུ་རབ་ཏུ་མྱུར་དུ་བསྒྲུབས་པས་འབྲས་བུ་མ་ཧཱ་མུ་དྲ་འཐོབ་ཅེས་བྱའོ། །

[Block 47 [HEADING]]
### དཔེ་གཉིས་པ། ^3-2-0

[Block 48]
དཔེ་གཉིས་པ་ནི། ནཻ་རཉྫ་ནའི་འགྲམ་དུ་བདེ་བར་འཇུག་པས་འདུས། །ཞེས་བྱ་བ་ལ། ནཻ་རཉྫ་ན་ལ་ཆོས་གཉིས་ཏེ། རྒྱུན་མ་ཆད་པ་དང་། འགྲམ་གཉིས་ནས་མི་འབབ་པའོ། །

[Block 49]
དེ་བཞིན་དུ་རྣལ་འབྱོར་པས་ད་པེས་མཚོན་པའི་དོན་ལ་རྒྱུན་མ་ཆད་པ་དང་། རྟག་ཆད་གཉིས་ཀྱི་མཐར་མ་ལྷུང་བར་དམིགས་པར་བྱའོ། །

[Block 50]
ལམ་དེ་དཀའ་བས་འཇུག་པ་མ་ཡིན་པས་བདེ་བར་འཇུག་ཅེས་བྱའོ། །

[Block 51]
འདུས་པ་ནི་གཉིས་ཏེ། རྡོ་རྗེ་དང་པདྨ་དང་དབྱིངས་དང་རིགས་པ་འདུས་པའི་ཚུལ་གྱིས་བསྒྲུབ་པའོ། །

[Block 52 [HEADING]]
### དཔེ་གསུམ་པ། ^3-3-0

[Block 53]
དཔེ་གསུམ་པའི་དབང་དུ་བྱས་ནས། བྱང་ཆུབ་ཤིང་རྩར་རྡོ་རྗེ་གདན་བཞུགས་ནས། །ཞེས་བྱ་བ་ལ་བྱང་ཆུབ་ཀྱི་ཤིང་ལ་ཆོས་ལྔ་སྟེ། རྩ་བ་དང་། སྡོང་པོ་དང་། ལོ་མ་དང་། མེ་ཏོག་དང་། འབྲས་བུའོ། །

[Block 54]
དེ་བཞིན་དུ་རྣལ་འབྱོར་པས་ཀྱང་རྩ་བ་དང་འདྲ་བའི་ཤེས་རབ་དང་། སྡོང་པོ་དང་འདྲ་བའི་དད་པ་དང་། ལོ་མ་དང་འདྲ་བའི་བརྩོན་འགྲུས་དང་། མེ་ཏོག་དང་འདྲ་བའི་དྲན་པ་དང་། འབྲས་བུ་དང་འདྲ་བའི་ཏིང་ངེ་འཛིན་གྱིས་དབང་བྱས་ལ་སྒྲུབ་པའོ། །

[Block 55]
དེ་ལྟ་བུའི་རྣལ་འབྱོར་པ་དེ་གང་ན་གནས་ཀྱང་རྡོ་རྗེའི་གདན་ལ་བཞུགས་པ་ཞེས་བྱའོ། །

[Block 56 [HEADING]]
### རྡོ་རྗེ། ^3-4-0

[Block 57]
དཔེ་བཞི་པའི་དོན་བསྟན་པའི་ཕྱིར། རྡོ་རྗེ་དཔེར་བྱས་ཏིང་ངེ་འཛིན་ལ་གནས། །ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། རྡོ་རྗེ་ལ་ཆོས་གཉིས་ཏེ། མི་ཕྱེད་པ་དང་འབྱེད་པའོ། །

[Block 58]
དེ་བཞིན་དུ་རྣལ་འབྱོར་པས་ཀྱང་དབང་པོ་ལྔ་ལྡན་གྱི་སྒོ་ནས་ཉོན་མོངས་པ་དང་། ཤེས་བྱ་དང་། སྙོམས་པར་འཇུག་པའི་སྒྲིབ་པ༌[^9]གསུམ་གྱིས་མི་ཕྱེད་ལ་ཕར་འབྱེད་པའི་ཚུལ་གྱིས་སྒྲུབ་པའོ། །

[Block 59]
ཏིང་འཛིན་བླ་ན་མེད་པའི་ལམ་འདིས་ཀྱེ། །ཞེས་བྱ་བ་ནི་ལྷན་ཅིག་སྐྱེས་པ་འོད་གསལ་བ་དབང་པོ་ལྔས་དབང་བྱས་པའི་ལམ་འདིས་སོ། །

[Block 60]
ཀྱེ་ཞེས་བོས་ཏེ་གདམས་པའོ། །

[Block 61]
བདུད་བཞིའི་འཇིགས་པ་ཆེན་པོ་གང་དེ་བཅོམ། །ཞེས་པ་ནི་ལྷན་ཅིག་སྐྱེས་པ་འོད་གསལ་བ་སྐྱེས་པའི་སྟོབས་ཀྱིས་ལས་དང་ཉོན་མོངས་པའི༌[^10]སྐྱེ་བ་ལ་སོགས་པའི་བདུད་དེ་དང་དེའི་འཇུག་པ་རྣམས་ནམ་མཁའ་དག་པའི་ངོས་ལྟར་མཐོང་བས་སོ། །

[Block 62]
ད་ནི་དཔེ་དང་པོའི་མཚོན་བྱ༌[^11]དོན་གྱི་བདག་མེད་མ་རྒྱས་པར་བསྟན་པའི་ཕྱིར། གཟུགས་ནི་མ་སྤངས་ཞེས་བྱ་བ་ལ༌[^12]སོགས་པ་ལ་རཱུ་པ་ཞེས་བྱ་བ་གཟུགས་དང་རང་བཞིན་གཉིས་ལ་འཇུག་པ་ལས་སྭཱའི་རྐྱེན་བྱིན་ན་སྭཱ་ནི་རཱུ་པ་སྟེ་སེམས་འོད་གསལ་བ་བདག་མེད་པའོ། །

[Block 63]
མ་སྤངས་ལྷན་ཅིག་རྣམ༌[^13]རོལ་བས་ཞེས་པ་ནི། དེ་ལྟ་བུའི་བདག་མེད་མ་དང་རིག་པ་གཉིས་སུ་མེད་པར་རྣམ་པར་རོལ་པའོ། །

[Block 64]
རང་བཞིན་བདག་མེད་ལ་སོགས་པའི་ཚིག་གཉིས་ནི་གོ་སླའོ། །

[Block 65]
མཚན་ཉིད་དང་ཕན་ཡོན་བསྟན་པའི་ཕྱིར། ཆགས་མེད་ཞི་བས་ཉོན་མོངས་མེད་གང་གིས། །ཞེས་བྱ་བ་ལ་ཆགས་མེད་ནི་འཇིག་རྟེན་པའི་སེམས་བརྒྱ་དྲུག་ཅུའོ། །

[Block 66]
ཞི་བས་ནི་དེ་རྣམས་འབྱུང་འཇུག་ཆད་པའོ། །

[Block 67]
ཉོན་མོངས་མེད་གང་གིས་ནི་མཚོན་པ་ཙམ་སྟེ། སྒྲིབ་པ་གསུམ་དང་བྲལ་བའི་ཡེ་ཤེས་འོད་གསལ་བ་གང་གིས་སྐྱེ་བ་དང་འཆི་བའི་སྲིད་པའི་འཁྲུལ་པ་བཅད་པའོ། །

[Block 68]
བཅད་པ་ཙམ་ཡིན་ནམ་ཞེ་ན། འཁྲུལ་པ་མེད་པའི་ཟག་མེད་ཀྱི་ཡོན་ཏན་མ་ལུས་པ་ལེན་པའི་ཕྱིར། འཁྲུལ་མེད་བདེ་བ་ཆེན་པོ་ལེན་ཅིང་སྟེར། ཞེས་བྱའོ། །

[Block 69]
དེའི་མཚན་ཉིད་རྒྱས་པར་བསྟན་པར་བྱ་བའི་ཕྱིར། དེ་ལ་ཁ་དོག་དབྱིབས་དང་ཚད་ཀྱང་མེད། །ཅེས་བྱ་བ་ལ་སོགས་པ་ལ། འདིར་དོན་ནི་འདི་ཡིན་ཏེ། མཚོན་བྱེད་ཀྱི་བདག་མེད་མ་ལས་ཀྱི་ཕྱག་རྒྱའི་དབང་དུ་བྱས་ནས། ཁ་དོག་དང་དབྱིབས་ལེགས་པ་མིག་གི་དཀྱུས་རིང་བ་ལ་སོགས་པ་དང་ཕྲ་སྦོམ་ཚད་མཉམ་པ་དང་། བྱེད་པ་དམ་ཚིག་གི་འཁོར་ལོ་དྲུག་དང་། བདེ་བ་མངོན་དུ་འདོད་པ་དང་། དེ་ལ་བརྟེན་ནས་སེམས་བདེ་བའི་རྣམ་པར་སྐྱེ་བའི་སྐྱེ་བ་དང་། སྔགས་དང་ཆོས་ལ་སོགས་པའི་ང་རྒྱལ་ཡོད་པ་དེ་ལ་བརྟེན་ནས་སེམས་རླུང་རྩ་དབུ་མར་བཅུག་ནས་སེམས་བདེ་བའི་རྣམ་པར་བརླབས་པས༌[^14]བརྟན་པོར་གྱུར་ནས། མཚོན་བྱའི༌[^15]བདག་མེད་མ་འོད་གསལ་བར་བསྒོམས་པས་དེའི་མཚན་ཉིད་ནི། ཁ་དོག་མེད་པའི་མཚན་ཉིད་ལ་སོགས་པ་དགུ་སྟེ། ཁ་དོག་མེད་པ་དང་། དབྱིབས་མེད་པ་དང་། ཚད་མེད་པ་དང་། བྱེད་པ་མེད་པ་དང་། འདོད་པ་མེད་པ་དང་། སྐྱེ་བ་མེད་པ་དང་། ང་རྒྱལ་མེད་པ་དང་། འགྲོ་འོང་མེད་པ་དང་། བདག་གཞན་མེད་པའི་མཚན་ཉིད་ཅན་ནོ། །

[Block 70]
དེ་ལྟ་བུའི་མཚན་ཉིད་ཅན་དེ་དང་སེམས་ཐ་དད་མེད་པར་འགྱུར་བའི་དཔེ་ནི། ནམ་མཁའི་ངོ་བོ་ཡང༌[^16]དག་ཇི་ལྟ་བར། །ཞེས་བྱ་བ་གསུངས་ཏེ། ནམ་མཁའ་རྣམ་པར་དག་པའི་དཀྱིལ་ལྟར་སྣང་བའོ། །

[Block 71]
དེ་གང་གི་ཡུལ་ཡིན་ཞེ་ན། རྣལ་འབྱོར་ཐུབ་མཆོག་མ་ལུས༌[^17]རྣམ་པར་རོལ། །ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། རྣལ་འབྱོར་པ་ཐུབ་པས་སངས་རྒྱས་ཀྱི་སྲས་བླ་མ་དམ་པ་ཉེ་བར་བསྟེན་པ་ཚོགས་བསགས་པ་སྐལ་བ་དང་ལྡན་པ་རྣམས་ཀྱིས་ཤེས་རབ་ཀྱི་མིག་གིས་ཡུལ་དུ་མཐོང་ཞིང་། དབང་པོ་བཞིས་ངེས་པའི་ཚུལ་གྱིས་རོལ་པའོ། །

[Block 72]
དེའི་ཕྱིར་དེ་ནི་བཙུན་མོ་བདག་མེད་མ་ཞེས་བྱའོ། །

[Block 73]
དེ་ལྟ་བུའི་རང་བཞིན་བདག་མེད་མ་དེ༌[^18]དང་རོལ་པས། ལས་དང་ཉོན་མོངས་པའི་སྐྱེ་བ་ལ་སོགས་པ་རྩད་ནས་གཅོད་པ་ཡང་ཡིན་ལ། རང་བཞིན་གྱིས་འགོག་པ་མངོན་དུ་བྱ་རྒྱུ་ཡང་ཡིན་མོད་ཀྱི། འོན་ཀྱང་བྱམས་པ་དང་སྙིང་རྗེས་འཕངས་པའི་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱིས་རང་གི་རྒྱུད་ལ་ཟག་མེད་ཀྱི་ཡོན་ཏན་མ་ལུས་པ་རྫོགས་པར་མ་བྱས། སེམས་ཅན་ཡོངས་སུ་སྨིན་པར་མ་བྱས། སངས་རྒྱས་ཀྱི་ཞིང་ཡོངས་སུ་དག་པར་མ་བྱས་པར་བར་མ་དོར་ཡང་དག་པའི་མཐའ༌[^19]མངོན་དུ་བྱས་ན་ཉན་ཐོས་དང་རང་རྒྱལ་བར་ལྟུང་བས། དེའི་ཕྱིར་བཟོད་པ་དེ་དང་ལྡན་བཞིན་དུ་དགེ་བའི་ཆོས་མཐའ་དག་རྫོགས་པར་བྱ་དགོས་པར་བསྟན་པའི་ཕྱིར།

[Block 74 [VERSE]]
ཆགས་མེད་བྱམས་དང་སྙིང་རྗེ་ལས་བྱུང་བ།[^20] །
བྱང་ཆུབ་སྨོན་པའི་སེམས་ནི་ལེགས་བརྟན་བྱེད། །

[Block 75]
ཅེས་པ་ལ་ཆགས་པ་མེད་པ་ནི་སྒྱུ་མ་མཁན་ལྟར་རང་བཞིན་ཤེས་པས་མ་ཞེན་པའོ། །
--- END BLOCKS ---
