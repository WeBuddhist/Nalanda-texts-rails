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
[Block 71]
ཇི་ལྟར་བསླབ་པར་བྱ་བ་སྟེ། ཚོགས་ལམ་དང་། སྦྱོར་ལམ་དང་། མཐོང་ལམ་དང་། བསྒོམ་ལམ་དང་། མི་སློབ་པ་ལའོ། །

[Block 72]
འདི་ལྔ་ཡང་བསམ་པ་དང་། སྦྱོར་བ་དང་། མངོན་དུ་བྱ་བ་དང་། སྒྲུབ་པ་དང་། རྟོགས་པ་ཞེས་བྱ་བ་རྣམས་ཀྱི་རང་བཞིན་ནོ། །

[Block 73]
དེ་ལ་གདམས་ངག་ནི་འདི་ཡིན་ཏེ། རིགས་དང་ལྡན་པའི་གང་ཟག་བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་པས་ལམ་ལྔ་ལ་ཇི་ལྟར་བསླབ་པར་བྱ་ཞེས་དྲིས་པའི་དོན་ཏོ། །

[Block 74 [HEADING]]
### ལན། ^3-2-0

[Block 75]
ལན་ནི་ལམ་རྣམ་པ་ལྔ་ལ་རྣམ་པར་ཕྱེ་ནས་བསྟན་པས་བཅུ་གཅིག་ཏུ་འགྱུར་རོ། །

[Block 76]
དེ་ལ་ཡང་གཉིས་ཏེ། དབང་པོ་རྟུལ་པོའི་དབང་དུ་བྱས་པ་དང་། རྣོན་པོའི་དབང་དུ་བྱས་པའོ། །

[Block 77]
དེ་ལ་དབང་པོ་རྟུལ་པོ་ནི་ལམ་ལྔ་ལ་སློབ་པའི་ཚེ། ལམ་རེ་རེའི་དབང་དུ་བྱས་ནས་ཀྱང་མཚན་ཉིད་ཐམས་ཅད་ཡོངས་སུ་རྫོགས་པར་བསྟན་པ་ལ་ལྟོས་པ་ཡིན་ལ། དེའི་དབང་དུ་བྱས་ནས་ལམ་ལྔ་ལ་སློབ་པའི་ཚུལ་རྣམ་པར་ཕྱེ་ན་བཅུར་འགྱུར་རོ། །

[Block 78]
དབང་པོ་རྣོན་པོ་ནི་མགོ་སྨོས་པས་གོ་བ་ཡིན་ལ་དེའི་དོན་དུ་སྔར་དོན་བཅུར་སྟོན་པ༌[^24]དེ་ཉིད་བསྡུས་ནས་སྔགས་ཀྱི་དོན་དུ་བསྟན་པ་སྟེ། དེ་ལྟར་ན་ལན་བཏབ་པ་བཅུ་གཅིག་ཏུ་འགྱུར་རོ། །

[Block 79]
སྤྱིར་ན་འདི་གཉིས་ཀ་ཡང་དབང་པོ་རྣོན་པོ་ཡིན་མོད་ཀྱི་དེ་ལ་ཡང་ཁྱད་པར་ཡོད་པས་གཉིས་སུ་ཕྱེ་བ་ཡིན་ནོ། །

[Block 80]
འདིར་དབང་པོ་རྟུལ་པོ་ལ་བསྟན་པ་དེ་ཡང་དབང་པོ་རྟུལ་པོ་གཞན་ལ་ལྟོས་ནས་གསང་སྔགས་སུ་འགྱུར་བ་ཡིན་ཏེ། མ་གསངས་ཀྱང་གསངས་ཏེ་བསྟན་པ་བཞིན་དུ་སོང་བའི་ཕྱིར་རོ། །

[Block 81]
དེ་ཡང་གསང་བ་དང་མི་གསང་བ་ནི་བློ་ལ་ཡོད་པ་ཡིན་གྱི། དངོས་པོ་ལ་ནི་བསྟན་པར་བྱ་བ་ལ་ཁྱད་པར་མེད་ལ། སྟོན་པ་ལ་ཡང་དཔེ་མཁྱུད་མི་མངའ་བའི་ཕྱིར་རོ། །

[Block 82]
དེས་ན་འདིར་ཡང་གསང་སྔགས་ཀྱི་དོན་བཤད་པ་དེ་ཉིད་སྔ་མ་ལ་ཡང་གསང་སྟེ་བསྟན་པ་བཞིན་དུ་འཇུག་པས་གསང་སྔགས་ཀྱི༌[^25]ངེས་ཚིག་དང་ལྡན་ནོ། །

[Block 83]
དེ་ལ་དང་པོ་མདོ་ལ་རྟེན་རིགས་དང་ལྡན་པའི་གང་ཟག་གིས་བྱང་ཆུབ་མཆོག་ཏུ་སེམས་བསྐྱེད་པ་ནི་ལམ་བསྐྱེད་པའི་རྟེན་གྱི་གང་ཟག་ཡིན་པས་དེ་བཤད་པ་ནི། ཤཱ་རིའི་བུ་ཞེས་བོས་ནས་རིགས་ཀྱི་བུ་འམ་རིགས་ཀྱི་བུ་མོ་གང་ལ་ལ་ཞེས་བྱ་བས་རིགས་དང་ལྡན་པའི་གང་ཟག་བསྟན་ལ། ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཟབ་མོ་ཞེས་བྱ་བ་དང་། སྤྱད་པ་སྤྱོད་པར་འདོད་པ་ཞེས་བྱ་བ་གཉིས་ཀྱིས་དམིགས་པར་བྱ་བའི་ཡུལ་དང་། འདུན་པའི་མཚན་ཉིད་ཀྱི་སེམས་བསྐྱེད་པ་གཉིས་བཤད་དེ་གོ་རིམས་བཞིན་ནོ། །

[Block 84]
འདིས་ནི་དབང་པོ་རྣོ་རྟུལ་མ་ཕྱེ་བར་སྤྱིར་བསྟན་པའོ། །

[Block 85 [HEADING]]
#### དབང་པོ་རྟུལ་པོའི་དབང་དུ་བྱས་པ། ^3-2-1-0

[Block 86]
དབང་པོ་རྟུལ་པོའི་དབང་དུ་བྱས་པའི་ལན་བཅུ་ཡང་འཕགས་པ་དགོངས་པ་ངེས་པར་འགྲེལ་པ་ལས་དམིགས་པ་རྣམ་པ་བཞི་བཤད་པ་དེས་དོན་གྱི་ཁོག་དབུབ༌[^26]པར་བྱ་སྟེ། རྣམ་པར་རྟོག་པ་དང་བཅས་པའི་གཟུགས་བརྙན་ལྷག་མཐོང་གི་དམིགས་པ་དང་། རྣམ་པར་མི་རྟོགས་པའི༌[^27]གཟུགས་བརྙན་ཞི་གནས་ཀྱི་དམིགས་པ་དང་། དངོས་པོ་མཐའི་དམིགས་པ་དང་། དགོས་པ་ཡོངས་སུ་གྲུབ་པའི་དམིགས་པའོ། །

[Block 87]
འདི༌[^28]བཞིས་ཚོགས་ལམ་དང་། སྦྱོར་ལམ་དང་། མཐོང་ལམ་དང་། མི་སློབ་པའི་ལམ་བཞི་རིམ་བཞིན་བསྟན་པར་ཤེས་པར་བྱའོ། །

[Block 88]
འདིར་བསྒོམ་ལམ་ནི་དམིགས་པ་སྔ༌[^29]མ་གསུམ་ཉིད་ལ་དམིགས་པ་མ་གཏོགས་པ་དམིགས་པ་ལྷག་མ༌[^30]གཞན་མེད་པས་ལོགས་སུ་མ་བསྟན་ཏེ། དེ་སྐད་དུ་ཡང་མགོན་པོ་བྱམས་པས། ངེས་འབྱེད་ཡན་ལག་དང་མཐོང་བའི། ལམ་དང་བསྒོམ་པའི་ལམ་ཉིད་ལ། ཡང་དང་ཡང་དུ་སེམས་པ་དང་། འཇལ་དང་ངེས་རྟོག་བསྒོམ་པའི་ལམ། །ཞེས་བཤད་དོ། །

[Block 89 [HEADING]]
##### རྣམ་པར་རྟོག་པ་དང་བཅས་པའི་གཟུགས་བརྙན་ལྷག་མཐོང་གི་དམིགས་པ། ^3-2-1-1-0

[Block 90]
དེ་ལ་རྣམ་པར་རྟོག་པ་དང་བཅས་པའི་གཟུགས་བརྙན་ལྷག་མཐོང་གི་དམིགས་པ་ནི་འདི་ལྟར་རྣམ་པར་བལྟ་བར་བྱ་སྟེ་ཞེས་བྱ་བས་བསྟན་ཏོ། །

[Block 91]
འདིས་ནི་ཚོགས་ཀྱི་ལམ་གྱི་གནས་སྐབས་ན་ཡོད་པའི་དེ་ཁོ་ན་ཉིད་ལ་སོ་སོར་རྟོག་པའི་ཤེས་རབ་བསྟན་ཏོ། །

[Block 92]
མཐོང་ལམ་དུ་ནི་དམིགས་པ་ཐམས་ཅད་མཉམ་པ་ཉིད་དུ་རྟོགས་པས་དམིགས་པ་རྣམ་པ་སྣ་ཚོགས་སུ་ལྟ་བ་མེད་ལ། འདིར་ནི་སྟོང་པ་ཉིད་ལ་སོགས་པ་རྣམ་པ་སྣ་ཚོགས་སུ་དངོས་པོ་ལ་ཡོད་པར་ཞེན་ཅིང་རྟོག་པར་བྱེད་པས་ནའོ། །

[Block 93]
རྣམ་པར་རྟོག་པ་ནི་མི་འདྲ་བ་འམ་སྣ་ཚོགས་སུ་རྟོག་པར་བྱེད་པའོ། །

[Block 94]
དེ་ལྟར་རྟོག་པའི་ཤེས་རབ་དེ་ཉིད་ཏིང་ངེ་འཛིན་མེད་པས་ན་ལྷག་མཐོང་ཙམ་གྱི་རང་བཞིན་ཡིན་ལ། མཐོང་ལམ་དུ་སྐྱེ་བའི་མི་རྟོག་པའི་གཟུགས་བརྙན་ཙམ་ཡིན་པས་ན། རྣམ་པར་རྟོག་པ་དང་བཅས་པའི་གཟུགས་བརྙན་ལྷག་མཐོང་གི་དམིགས་པ་ཞེས་བྱའོ། །

[Block 95]
དེས་ན་རྣམ་པར་བལྟ་བར་བྱ་སྟེ་ཞེས་འབྱུང་བ་ནི་རྣམ་པ་སྣ་ཚོགས་སུ་སོ་སོར་བརྟག་པར་བྱའོ་ཞེས་བསྟན་པའོ། །

[Block 96]
དྲིས་པའི་སྐབས་ནས་ཀྱང་བཤད་དོ། །

[Block 97 [HEADING]]
##### རྣམ་པར་མི་རྟོག་པའི་གཟུགས་བརྙན་ཞི་གནས་ཀྱི་དམིགས་པ། ^3-2-1-2-0

[Block 98]
དེ་ལྟར་ཚོགས་ལམ་སྐྱེས་པ་ལ་ཤེས་པ་གཞན་གྱིས་བར་མ་ཆོད་པར་དྲོད་ལ་སོགས་པ་ངེས་འབྱེད་སྐྱེ་བ་ཡིན་པས་མདོའི་ཚིག་འདིས་ནི་རྣམ་པར་མི་རྟོག་པའི་གཟུགས་བརྙན་ཞི་གནས་ཀྱི་དམིགས་པ་ཡང་འདི་ཉིད་ཀྱིས་བཤད་པ་ཡིན་ནོ། །

[Block 99]
དེ་ལ་རྣམ་པར་མི་རྟོག་པ་ནི་གོང་དུ་བསྟན་པའི་ཐོས་བསམ་གྱི་ཤེས་པ་ཁ་ཕྱིར་བལྟས་ནས་དམིགས་པ་སྣ་ཚོགས་ལ་རྟོག་པ་དེ་ལྟར་མི་རྟོག་ཅིང་གཅིག་ཏུ་ནང་ཉིད་དུ་རྟོག་པ་བསྡུས་པ་སྟེ། དེ་ཉིད་ཀྱང་ཆོས་ཐམས་ཅད་མཉམ་པ་ཉིད་དུ་རྟོགས་པའི་ལྷག་མཐོང་མཐོང་ལམ་དུ་སྐྱེ་བ་དེ་ལྟ་བུ་མེད་ཀྱང་ཞི་གནས་ཀྱི་རང་བཞིན་ཡོད་པས། རྣམ་པར་མི་རྟོག་པའི་གཟུགས་བརྙན་ཞི་གནས་ཀྱི་དམིགས་པ་སྟེ་སྔ་མ་བཞིན་ནོ། །

[Block 100 [HEADING]]
##### གསུམ་པ་དངོས་པོའི་མཐའི་དམིགས་པ། ^3-2-1-3-0

[Block 101]
དེ་ལྟར་དམིགས་པ་གཉིས་བཤད་ནས། ད་ནི་གསུམ་པ་དངོས་པོའི་མཐའི་དམིགས་པ་སྟོན་ཏེ། །དེ་ལ་དངོས་པོ་ནི་གཟུགས་ལ་སོགས་པའོ། །

[Block 102]
དེའི་མཐའ༌[^31]ནི་རང་བཞིན་ནམ་ཆོས་ཉིད་དེ། དེ་ལ་དམིགས་པ་ནི་དངོས་པོའི་མཐའ་ལ་དམིགས་པའོ། །

[Block 103]
འདི་ནི་མཐོང་ལམ་མོ། །

[Block 104]
དེ་ལ་ཡང་གསུམ་ཏེ། དམིགས་པ་དང་། དམིགས་པ་དེ་ལ་འཇུག་པའི་རྣམ་པ་དང་། རྣམ་པ་དེས་རྣམ་པར་བལྟས་པའི་འབྲས་བུའོ། །

[Block 105 [HEADING]]
###### དམིགས་པ། ^3-2-1-3-1-0

[Block 106]
དེ་ལ་ཕུང་པོ་ལྔ་པོ་དེ་དག་ལ་ཡང་ངོ་བོ་ཉིད་ཀྱིས་སྟོང་པར་ཡང་ཡང་དག་པར་རྗེས་སུ་བལྟའོ་ཞེས་བྱ་བ་ནི་གོང་དུ་བསྟན་པ་ལྟར་དངོས་པོ་དང་། མཐའ་དང་། དེ་ལ་དམིགས་པ་གསུམ་བསྟན་པས་མཐོང་ལམ་གྱི་དམིགས་པ་བསྟན་པའོ། །

[Block 107]
ཚིག་དོན་ནི་འགྲེལ་པ་ནས་གསལ་ལོ། །

[Block 108 [HEADING]]
###### དམིགས་པ་དེ་ལ་འཇུག་པའི་རྣམ་པ། ^3-2-1-3-2-0

[Block 109]
དམིགས་པ་དེ་ལ་རྣམ་པ་གང་གིས་ཞུགས་ན་ཡང་དག་པར་རྗེས་སུ་ལྟ་བ༌[^32]ཕྱིན་ཅི་མ་ལོག་པར་ལྟ་བར༌[^33]འགྱུར་བ་ཡིན་ཞེ་ན། གཟུགས་སྟོང་པའོ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 110]
འདི་ལ་ཡང་གསུམ་སྟེ། རྣམ་པ་སོ་སོའི་མཚན་ཉིད་དང་། གྲངས་ངེས་པ་དང་། གོ་རིམས་ངེས་པའོ། །
--- END BLOCKS ---
