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
[Block 1016]
སེར་སྣ་དང་གསོག་འཇོག་གི་དྲི་མ་བསལ་ནས་བཟང་པོ་དང་གཙང་མ་དང་། རུང་བ་ཞེས་བྱ་བ་འདི་དག་གི་བསྡུས་པའི་དོན་ནི་གང་སྦྱིན་པ་དང་། ཇི་ལྟར་སྦྱིན་པའོ། །

[Block 1017]
གང་སྦྱིན་ཞེ་ན། བཟང་པོ་དང་། གཙང་མ་དང་། རུང་བའོ། །ཇི་ལྟར་ཞེ་ན། བཟང་པོས་ལུས་ཚིམ་པར་བྱེད་ཅིང་། གཙང་བ་དང་། རུང་བས་སེམས་འཛིན་པར་བྱེད་དོ། །

[Block 1018]
སེར་སྣའི་དྲི་མ་བསལ་བས་ནི་སྦྱིན་བདག་གིས་འདི་དང་གཞན་དུ་རྣམ་པར་སྨིན་པ་ལ༌[^784]ལོངས་སྤྱོད་ཆེན་པོ་འཐོབ༌[^785]བོ། །

[Block 1019]
གསོག་འཇོག་གི་དྲི་མ་བསལ་བས་ནི་འདི་དང་གཞན་དུ་ལོངས་སྤྱོད་རྣམས་ལ་འཛིན་པ་མེད་པར་གྱུར༌[^786]ཏེ། རྒྱུ་མཐུན་པའི་འབྲས་བུའོ། །

[Block 1020]
དེ་ལ་ཟང་ཟིང་དང་མི་འཇིགས་པའི་སྦྱིན་པ་རབ་ཏུ་དབྱེ་བ་དང་བཅས་པ༌[^787]ཞེས་བྱ་བ་ལ། ཟང་ཟིང་གི༌[^788]སྦྱིན་པ་ཉིད་ནི་འདིར་དབྱེ་བ་དང་བསླབ་པ༌[^789]ཡིན་གྱི། མི་འཇིགས་པའི་སྦྱིན་པ་ལ་ནི་འདིར་དབྱེ་བ་མེད་དོ། །

[Block 1021]
མི་སྐྱོ་བར་སྦྱིན་པ་སྦྱིན་ཞེས་བྱ་བ་ལ། འདིའི་རྒྱུ་ལས་བརྩམས་ཏེ། བྱང་ཆུབ་སེམས་དཔའ་ཇི་ལྟར་སྦྱིན་པ་ལས་བརྩམས་ཏེ་རྐྱེན་དུ་བྱེད་པ་དེ་ལྟར་སློང་བ༌[^790]པོས་ཞེས་བྱ་བ་ལ་སོགས་པས་ཤེས་པར་བྱའོ། །

[Block 1022]
མཆོག་ཏུ་འཛིན་པ་ཞེས་བྱ་བ་ནི་ལྟ་བ་རྣམ་པ་གསུམ་སྟེ། སྦྱིན་པ་འདིའི་འབྲས་བུ་མེད་དོ་ཞེས་བྱ་བའི་ལོག་པར་ལྟ་བ༌[^791]མཆོག་ཏུ་འཛིན་པའི་ལྟ་བ་སྟེ། འཚེ་བའི་སྦྱིན་པས་ཆོས་སུ་འགྱུར་རོ་ཞེས་བྱ་བའམ། ཚུལ་ཁྲིམས་མཆོག་ཏུ་འཛིན་པའི་ལྟ་བ་སྟེ། སྦྱིན་པ་ཤིན་ཏུ་རྫོགས་པ་ཙམ་གྱིས་འཇིག་རྟེན་པ་དང་འཇིག་རྟེན་ལས་འདས་པའི་རྣམ་པར་དག་པར་འགྱུར་རོ་ཞེས་བྱ་བའོ། །

[Block 1023]
གང་གི་ཕྱིར་ཤིན་ཏུ་བསགས་ཤིང་ཕྱིས་དུས་གཅིག་ཏུ་སྦྱིན་པར་མི་བྱེད་པ་སྐྱོན་ཅི་ཡོད་ཅེ་ན། དེ་རབ་ཏུ་བསྟན་པའི་ཕྱིར་བྱང་ཆུབ་སེམས་དཔའ་ནི་སྦྱིན་པར་བྱ་བའི་ཆོས་དག་ཡོད༌[^792]བཞིན་དུ་ཞེས་བྱ་བ་ནས་བརྩམས་པ་སྟེ། སོགས་པར་བྱེད་པའི་ཉེས་པ་ལས་བརྩམས་ནས་སྦྱིན་པར་བྱ་བའི་ཆོས་དག་ཡོད༌[^793]བཞིན་དུ་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 1024]
སོགས་པར་བྱེད་པས་སློང༌[^794]མོ་པ་ཕྱིར་བཟློག་པའི་རྒྱུ་ནི་རྣམ་པ་གཉིས་ཡིན་ཏེ། སྦྱིན་པར་བྱ་བའི་ཆོས་མེད་པའམ་སློང༌[^795]མོ་པ་ཡང་དག་པར་སློང་བར་བྱེད་པ་མ་ཡིན་པའོ། །

[Block 1025]
དེ་གཉི་ག་ཡང་མེད་པ༌[^796]བཞིན་དུ་ཕྱིར་ཟློག༌[^797]པར་བྱེད་པ་ལ་སྐྱོན་གཉིས་སྟོན་པར་བྱེད་པ་ཉིད་དོ།[^798] །སྦྱིན་པར་བྱ་བའི་ཆོས་ཡོད་བཞིན་དུ་སྦྱིན་པར་མི་སྤྲོ་བས་སློང་བ་ཕྱིར་ཟློག་པ་དང་། ཡང་དག་པར་སློང་བར་བྱེད་པ་ཉེ་བར་ལྷགས་པར༌[^799]གྱུར་ཀྱང་ཡང་དག་པར་སློང་བར་བྱེད་པ་དེ་དག་ལ་ཕྱིར་ཟློག་པར་བྱེད་པ་ནི་རིགས་པ་མ་མཐོང་ངོ་། །བྱང་ཆུབ་སེམས་དཔས་སྦྱིན་པར་བྱ་བའི་དངོས་པོ་ཡོད་བཞིན་དུ་སློང་མོ་པ་ཉེ་བར་ལྷགས་པ་སྤོང་བར་བཟོད་པ༌[^800]མ་ཡིན་ཏེ་ཕྱིར་སྤོང་བར་བྱེད་པ་ནི་རིགས་པ་མ་ཡིན་པར་མཐོང་བའི་ཕྱིར་རོ། །

[Block 1026]
ཡང་དེ་ཅི་ལྟར༌[^801]སོགས་པར་འགྱུར། སློང་བ་ཕྱིར་བཟློག་པ༌[^802]མ་བྱས་པ་ལ་ནི་སོགས་པ་མེད་པའི་ཕྱིར་ཏེ། ཕྱིས་དུས་གཅིག་ཏུ་སྦྱིན་པར་བྱེད་པ་ལ་ཡོན་ཏན་མ་མཐོང་བས་སོགས་པའི༌[^803]སྦྱིན་པ་ལས་བསོད་ནམས་འདུ་བའི་སྒོ་ལྷག་པར༌[^804]མ་མཐོང་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། བསོད་ནམས་ཁྱད་པར་ཡོད་པ་ཡོངས་སུ་འཛིན་པར་འགྱུར་ཞེས་བྱ་བ་ལ་སོགས་པས་སྟོན་ཏོ། །

[Block 1027]
སྦྱིན་པར་བྱ་བའི་དངོས་པོ་ཡང་མཚུངས་ཏེ་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་སྦྱིན་པར་བྱ་བའི་རྫས་ཡོད༌[^805]ཀྱང་མཚུངས་ལ། སློང་བ་པོ་ཡང་མཚུངས་པ་རྣམས་ལ་ཁྱད་པར་ཡོད་པར་མཐོང་བས་བསགས་ཤིང་སྦྱིན་པར་མི་བྱའོ། །

[Block 1028]
བྱང་ཆུབ་སེམས་དཔའ་ནི་སློང་བ་པོ་ལ་ཞེས་བྱ་བ༌[^806]ལ་སོགས་པ་ལ། དམའ་བའི་སེམས་ཀྱིས་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་བདག་ཉིད་ཀྱི་ང་རྒྱལ་བཅག་པ་སྟོན་ཏོ། །

[Block 1029]
མི་བརྟེན་པའི་སྦྱིན་པའི་བསྡུས་པའི་དོན་ནི་ཚེ་འདིའི་གྲགས་པ་ལ་མི་བརྟེན་པ་སྟེ། དེ་ནི་རྟོག་པ་ཙམ་གྱིས༌[^807]བདག་ཉིད་སྨད་པ༌[^808]ཡིན་པའི་ཕྱིར་རོ། །

[Block 1030]
ཞུམ་པ་མེད་པ༌[^809]དུས་གསུམ་དུ་སྤྲོས་པ་དང༌[^810]བཅས་པའོ། །

[Block 1031]
ངན་པ་མ་ཡིན་པའི་སྦྱིན་པ་ནི་བདག་ལ་ཡོད་པའི་མཆོག་སྟེར་བའོ། །

[Block 1032]
རྒྱབ་ཀྱིས་ཕྱོགས་པ་མེད་པའི་སྦྱིན་པ་ནི་མཛའ་བོ་དང་དགྲ་ལ་བྱེ་བྲག་མེད་པར་སྦྱིན་པ་གཏོང་བར་བྱེད་པ་སྟེ། སྙིང་རྗེ་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 1033]
ལམ༌[^811]ལ་མི་ལྟ་བའི་སྦྱིན་པ་གང་ཞེ་ན། ཕ་རོལ་གྱིས་སླར་བདག་ལ་ལན་བྱས་སུ་མི་རེ་བ་སྟེ། ཅིའི་ཕྱིར་ཞེ་ན། སྙིང་བརྩེ་བ་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 1034]
ཕན་འདོགས་སུ་རེ་བ་མེད་ཅེས་བྱ་བ་ནི་ཕན་གདགས་པ་ཉིད་ཀྱི་རྒྱུ་མཐོང་བ་སྟེ། བདེ་བ་འདོད་པ་སྲེད་པའི་མེས་བསྲེགས་པར༌[^812]གྱུར་པ་རྣམས་མཐུ་མེད་པ་མཐོང་བའི་ཕྱིར་རོ། །

[Block 1035]
བདེ་བའི་རྒྱུ་འདོད་པས་འཇུག་པ་རྣམས་ལ་ཡང་ཕན་པ་དང་། སྙིང་བརྩེ་བའི་སེམས་ཀྱིས་དེའི་ཆེད་དུ་བསྟན་པར་བྱ་བའི་ཕྱིར་གསུངས་པ་ནི། སྐྱེ་བོ་རང་བཞིན་གྱིས་སྡུག་བསྔལ་བ་དག་མཐོང་བའི་ཕྱིར་ཞེས་བྱ་བའོ། །

[Block 1036]
ཕྱི་མ་ལ་ལོངས་སྤྱོད་ཕུན་སུམ་ཚོགས་པའམ། རྣམ་པར་སྨིན་པ་ལ་རེ་བ་མེད་ཅེས་བྱ་བ་འདི་ལ། དེའི་རྒྱུ་བསྟན་པར་བྱ་བའི་ཕྱིར། འདུ་བྱེད་ཐམས་ཅད་ནི་སྙིང་པོ་མེད་པར་ལྟ་ཞེས་བྱ་བའོ། །

[Block 1037]
ཅིའི་ཕྱིར་ལུས་ཕུན་སུམ་ཚོགས་པར་འགྱུར་བ༌[^813]སྦྱིན་པའི་འབྲས་བུ་རྣམ་པར་སྨིན་པ་ལ་རེ་བ་མེད་ཅེས་བྱ་བ་དེའི་རྒྱུ་སྟོན་པར་བྱེད་པ་ནི། བྱང་ཆུབ་མཆོག་ལ་ཕན་ཡོན་དུ་ལྟ་བའི་ཕྱིར་རོ་ཞེས་བྱ་བའོ། །

[Block 1038]
ཡང་ན་ཉེས་པ་གཉི་ག་ཡང་མཐོང་བའི་ཕྱིར་ཏེ། འདུ་བྱེད་ཐམས་ཅད་སྙིང་པོ་མེད་པར་ལྟ་བ་དང་། དེའི་གཉེན་པོ་ཉིད་ལ་ཕན་ཡོན་དུ་ལྟ་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1039]
སྦྱིན་པ་རིམ་པར་ཕྱེ་བ་སྟེ་དགུ་པ་རྫོགས་སོ།། །།

[Block 1040 [HEADING]]
## མཇུག་བྱང། ^b-0

[Block 1041]
ཚུལ་ཁྲིམས་རིམ་པར་ཕྱེ་བ་ནི་གོང་དུ་ཕྱུང་བ་ཡིན། སློབ་དཔོན་ཡོན་ཏན་འོད་ཀྱིས་མཛད་པ་བྱང་ཆུབ་སེམས་དཔའི་སའི་འགྲེལ་པ་ལས་ཇི་སྙེད་འགྱུར་བ་རྫོགས་སོ།། །།

[Block 1042]
རྒྱ་གར་གྱི་མཁན་པོ་དཱི་པཾ་ཀ་ར་ཤྲཱི་ཛྙཱ་ན་དང་། ལོ་ཙཱ་བ་དགེ་སློང་ཚུལ་ཁྲིམས་རྒྱལ་བས་བསྒྱུར་ཅིང་ཞུས་ཏེ་གཏན་ལ་ཕབ་པ། །[^814]
--- END BLOCKS ---
