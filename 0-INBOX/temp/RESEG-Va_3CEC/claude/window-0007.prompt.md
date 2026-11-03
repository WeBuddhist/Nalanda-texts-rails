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
[Block 246]
སྡིག་པ་མི་དགེ་བའི་ཆོས་རྣམས་ལས་དབེན་པ་ཞེས་བྱ་བ་ནི་གང་དག་ཉོན་མོངས་པའི་འདོད་པའི་རྒྱུ་ལས་བྱུང་བའི་ལུས་དང་ངག་དང་ཡིད་ཀྱིས་ཉེས་པར་སྤྱོད་པར་གཏོགས་པ་ཆད་པས་གཅོད་པ་དང་། མཚོན་འདེབས་པ་དང་། འཐབ་པ་དང་། རྩོད་པ་དང་། འགྱེད་པ་དང་། གཡོའི་ཚིག་དང་། གནོད་པ་དང་། བརྫུན་དུ་སྨྲ་བ་ལ་སོགས་པ་དེ་དག་ལས་དབེན་པའོ། །

[Block 247]
རྣམ་པར་རྟོག་པ་དང་། རྣམ་པར་དཔྱོད་པ་དག་སྐྱོན་དུ་མ་མཐོང་བས་འདོད་པའི་གཉེན་པོ་དེ་གཉིས་དང་མཚུངས་པར་ལྡན་པའི་ཕྱིར་རྟོག་པ་དང་བཅས༌[^229]དཔྱོད་པ་དང་བཅས་པ་ཞེས་བྱ་བས་གཉེན་པོ་བསྒོམ་པ༌[^230]བསྟན་ཏེ། རྟོག་པ་དང་དཔྱོད་པ་གཉིས་ཀྱིས་འདོད་པ་དང་། སྡིག་པ་མི་དགེ་བའི་ཆོས་འཇོམས་པར་བྱེད་པས་སོ། །

[Block 248]
དབེན་པ་ལས་སྐྱེས་པའི་དགའ་བ་དང་། བདེ་བ་ཅན་ཞེས་བྱ་བས་བསྒོམས་པའི༌[^231]ཕན་ཡོན་བསྟན་ཏེ། འདོད་པ་ལས་དབེན་པ་འམ། [^232]སྒྲིབ་པ་ལས་དབེན་པ་ལས་སྐྱེས་པའི་དགའ་བ་དང་བདེ་བ་ནི་དབེན་པ་ལས་སྐྱེས་པའི་དགའ་བ་དང་བདེ་བ་ཞེས་བྱ་སྟེ། འདོད་པའི་དོན་རྙེད་ནས་གནས་ངན་ལེན་ཐམས་ཅད་དང་བྲལ་བས་ལུས་དང་སེམས་ཤིན་ཏུ་སྦྱངས་ཏེ་ལས་སུ་རུང་བའི་ཕྱིར་རོ། །

[Block 249]
བསམ་གཏན་དང་པོ་ཉེ་བར་བསྒྲུབས་ཏེ་གནས་ཞེས་བྱ་བས་དེ་གཉིས་ཀའི་གནས་བསྟན་ཏེ། གཉེན་པོ་བསྒོམ་པ་དང་། བསྒོམས་པའི༌[^233]ཕན་ཡོན་གཉིས་ནི་བསམ་གཏན་དང་པོའི་སེམས་རྩེ་གཅིག་པ་ལས་གྲུབ་པའི་ཕྱིར་ཏེ། འོག་མ་དག་ལ་ཡང་དེ་བཞིན་དུ་སྦྱར་རོ། །

[Block 250]
དེ་རྟོག་པ་དང་དཔྱོད་པ་དང་བྲལ་ཞེས་བྱ་བས་བསམ་གཏན་གཉིས་པའི་མི་མཐུན་པའི་ཕྱོགས་ཉམས་པ་བསྟན་ཏེ། བསམ་གཏན་དང་པོའི་རྣམ་པར་རྟོག་པ་དང་བཅས། རྣམ་པར་དཔྱོད་པ་དང་བཅས་པའི་ཏིང་ངེ་འཛིན་གྱིས་མཚན་མ་དག་ལ་སྐྱོན་དུ་མཐོང་ནས་དེ་ལས་སེམས་བཟློག་སྟེ།[^234] རྣམ་པར་རྟོག་པ་མེད་པ་དང་། རྣམ་པར་དཔྱོད་པ་མེད་པའི་ཏིང་ངེ་འཛིན་གྱིས་མཚན་མ་ལས་སེམས་ཉེ་བར་འདོགས་པར་བྱེད་པའོ། །

[Block 251]
ནང་ཡོངས་སུ་དང་སྟེ། སེམས་ཀྱི་རྒྱུད་གཅིག་ཏུ་གྱུར་ཅེས་བྱ་བས་གཉེན་པོ་བསྒོམ་པ་བསྟན་ཏེ། དེ་ལྟར་རྟོག་པ་དང་དཔྱོད་པ་དང་བཅས་པའི་དམིགས་པ་དང་བྲལ་བར་བྱས་ནས་རྩེ་གཅིག་ཏུ་དཔྱོད་པའི་དམིགས་པ་ལས༌[^235]དང་གཅིག་པས་ཞི་བ་དང་། རབ་ཏུ་དང་བའི་སེམས་སུ་འཇོག་པས་ན་ཡོངས་སུ་དང་བ་ཡིན་ལ། དེ་དེ་ལྟར་སེམས་ཉེ་བར་འཇོག་པས་རྣམ་པར་རྟོག་པ་དང་བཅས། རྣམ་པར་དཔྱོད་པ་དང་བཅས་པས་གླགས་དང་བཅས་ཤིང་། བར་ཆད་དང་བཅས་པའི་གནས་སྐབས་ལས་འདས་ནས་སྒོམ་པ༌[^236]གོམས་པས་གླགས་མེད་ཅིང་བར་ཆད་མེད་པའི་གནས་སྐབས་ཐོབ་པར་འགྱུར་བས་སེམས་ཀྱི་རྒྱུད་གཅིག་ཏུ་གྱུར་པ་ཞེས་བྱའོ། །

[Block 252]
ཏིང་ངེ་འཛིན་ལས་སྐྱེས་པའི་དགའ་བ་དང་བདེ་བ་ཅན་ཞེས་བྱ་བས་བསྒོམས་པའི༌[^237]ཕན་ཡོན་བསྟན་ཏེ། བསམ་གཏན་དང་པོའི་དབེན་པ་ལས་སྐྱེས་པའི་དགའ་བ་དང་བདེ་བ་ལས་ཁྱད་པར་དུ་འཕགས་པ་བསྟན་ཏོ། །

[Block 253]
བསམ་གཏན་གཉིས་པ་ཉེ་བར་བསྒྲུབས་ནས་གནས་ཞེས་བྱ་བས་དེ་གཉི་གའི་གནས་བསྟན་ཏོ། །

[Block 254]
དེ་དགའ་བའི་འདོད་ཆགས་དང་བྲལ་བས་ཞེས་བྱ་བས་བསམ་གཏན་གསུམ་པའི་མི་མཐུན་པའི་ཕྱོགས་ཉམས་པ་བསྟན་ཏེ། ཏིང་ངེ་འཛིན་ལས་སྐྱེས་པའི་སེམས་དགའ་བའི་འདོད་ཆགས་དང་བྲལ་བའི་ཕྱིར་རོ། །

[Block 255]
བཏང་སྙོམས་ལ་གནས་ཤིང་དྲན་པ་དང་། ཤེས་བཞིན་ཅན་ཡིན་ཞེས་བྱ་བས་གཉེན་པོ་བསྒོམ་པ༌[^238]བསྟན་ཏེ། རྣམ་པར་རྟོག་པ་དང་བཅས། རྣམ༌[^239]པར་དཔྱོད་པ་དང་བཅས་པ་དེ་དག་དང་དགའ་བ་ཡང་སྤངས་པས༌[^240]བར་ཆད་མེད་པར་བཏང་སྙོམས་དང་ལྡན་པར་གནས་སོ། །

[Block 256]
དེ་ཡང་དགའ་བ་དང་ལྡན་པའི་འདུ་ཤེས་ཡིད་ལ་བྱེད་པ་རྣམས་ཀྱི་གོ་སྐབས་མི་དབྱེ་བའི་ཕྱིར་དྲན་པ་ཉེ་བར་གནས་པ་ཡིན་ལ། སྐྱེས་པ་རྣམས་ཀྱང་ནམ་ཡང་ཇི་ལྟར་ཡང་དང་ཡང་དུ་མི་བླང་བའི་ཕྱིར་ཤེས་རབ་ཀྱིས་མང་དུ་གནས་པས་ན་དྲན་པ་དང༌[^241]ལྡན་ཞིང་ཤེས་བཞིན་ཅན་ཞེས་བྱའོ། །

[Block 257]
བདེ་བ་ལུས་ཀྱིས་མྱོང་ལ། འཕགས་པ་རྣམས་ཀྱི༌[^242]གང་དེ་དྲན་པ་དང་ལྡན་པ་བདེ་བ་ལ་གནས་པ་བཏང་སྙོམས་པའོ་ཞེས་བརྗོད་པ་སྟེ་ཞེས་བྱ་བས་བསྒོམས་པའི༌[^243]ཕན་ཡོན་བསྟན་ཏེ། དེ་ལྟར་བཏང་སྙོམས་ལ་མང་དུ་གནས་པ་དེ་སེམས་གཡེང་བ༌[^244]མེད་པའི་དགའ་བ་དང་ལྡན་པའི་ཚོར་བ་སྤངས་ནས། དགའ་བ་མེད་པའི་ཞི་བ་རབ་ཏུ་ཞི་བའི་ཚོར་བ་འབྱུང་སྟེ། དེ་ཡང་དེའི་ཚེ་གཟུགས་ཀྱི་ལུས་དང་། ཡིད་ཀྱི་ལུས་ཀྱིས་ཚོར་བའི་བདེ་བ་དང་། ཤིན་ཏུ་སྦྱངས་པའི་བདེ་བ་མྱོང་བར་བྱེད་པས་ན་བདེ་བ་ལུས་ཀྱིས་མྱོང་བ་ཞེས་བྱའོ། །

[Block 258]
བསམ་གཏན་འོག་མ་གཉིས་ལ་ནི་དེ་ལྟ་བུའི་བདེ་བ་དང་བཏང་སྙོམས་མེད་ལ། གོང་མ་ལ་ནི་བཏང༌[^245]སྙོམས་ཡོད་ཀྱང་བདེ་བ་མེད་ཀྱི། བསམ་གཏན་གསུམ་པ་འདི་ཉིད་བདེ་བ་དང་བཏང་སྙོམས་ཀྱི་གནས་ཡིན་པས་འཕགས་པ་སངས་རྒྱས་རྣམས་དང་། སངས་རྒྱས་ཀྱི་ཉན་ཐོས་རྣམས་ཀྱིས་བསམ་གཏན་གསུམ༌[^246]པ་འདི་ཉིད་ལ་དྲན་པ་དང་ལྡན་པ་བདེ་བ་ལ་གནས་པ་བཏང་སྙོམས་པའོ་ཞེས་གཙོ་བོར་བསྔགས་པས་ན་འཕགས་པ་རྣམས་ཀྱིས་གང་དེ་དྲན་པ་དང་ལྡན་པ། བདེ་བ་ལ་གནས་པ། བཏང་སྙོམས་པའོ་ཞེས་བརྗོད་པ་ཞེས་གསུངས་སོ། །

[Block 259]
དེ་བདེ་བ་ཡང་སྤངས་ཏེ། སྔ་ནས་སྡུག་བསྔལ་ཡང་སྤངས་ཤིང་ཡིད་བདེ་བ་དང་ཡིད་མི་བདེ་བ་ཡང་ནུབ་པས་ཞེས་བྱ་བས་བསམ་གཏན་བཞི་པའི་མི་མཐུན་པའི་ཕྱོགས་ཉམས་པ་བསྟན་ཏེ། བདེ་བ་ཡང་སྤངས་ཞེས་བྱ་བ་ནི་བསམ་གཏན་གསུམ་པ་དང་ལྡན་པའི་བདེ་བ་བསམ་གཏན་བཞི་པ་འདིས་སྤངས་པར་བསྟན་པའོ། །

[Block 260]
སྡུག་བསྔལ་ཡང་སྤངས་ཞེས་བྱ་བ་ནི་བསམ་གཏན་གཉིས་པ་སྤངས་པ་ཡང་བསྡུས་ཏེ་བསྟན་པའོ། །

[Block 261]
ཡིད་བདེ་བ་ནུབ་པས་ཞེས༌[^247]བྱ་བ་ནི་བསམ་གཏན་གསུམ་པས་དགའ་བ་སྤངས་པ༌[^248]བསྟན་པའོ། །

[Block 262]
ཡིད་མི་བདེ་བ་ནུབ་པས་ཞེས་བྱ་བ༌[^249]ནི་བསམ་གཏན་གཉིས་པས་སྤངས་པ་བསྟན་ཏོ།[^250] །བདེ་བ་ཡང་མ་ཡིན་སྡུག་བསྔལ་བ་ཡང་མ་ཡིན་པ་བཏང་སྙོམས་དང་དྲན་པ་ཡོངས་སུ་དག་པ་ཞེས་བྱ་བས་བསྒོམས་པའི༌[^251]ཕན་ཡོན་བསྟན་ཏེ། ཚོར་བ་གོང་མ་བཞི་པོ་སྤངས་པས་སྡུག་བསྔལ་ཡང་མ་ཡིན་བདེ་བ་ཡང་མ་ཡིན་པའི་ཚོར་བ་དང་ལྡན་པ་དང་། བསམ་གཏན་གསུམ་པའི་ཚེ་བཏང་སྙོམས་དང་དྲན་པ་ཡོད་ཀྱང་ཡོངས་སུ་མ་དག་པ་འདིའི་ཚེ་ཡོངས་སུ་དག་པ་དང་ལྡན་པར་བསྟན་པའོ། །

[Block 263]
བསམ་གཏན་བཞི་པ་ཉེ་བར་བསྒྲུབས་ཏེ་གནས་ཞེས་བྱ་བས་དེ་གཉི་གའི་གནས་བསྟན་ཏོ། །

[Block 264]
འདི་ནི་ཡེ་ཤེས་ཀྱི་རྟེན༌[^252]དུ་རབ་ཏུ་བསྒྲུབས་པ་བསྟན་ཏེ། སེམས་རྩེ་གཅིག་ཏུ་གྱུར་ན་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་རབ་ཏུ་ཤེས་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 265 [HEADING]]
###### **བྱ་བ་བྱས་པ་རབ་ཏུ་སྒྲུབ་པ།** ^1-1-3-3-1-4-3-0

[Block 266]
དེ་བས་ན་མདོ་ལས་ཀྱང་། ཏིང་ངེ་འཛིན་གྱི་ཕུང་པོ་ཡོངས་སུ་རྫོགས་ནས་ཤེས་རབ་ཀྱི་ཕུང་པོ་ཡོངས་སུ་རྫོགས་པར་བྱེད་པ་དང་ཞེས་གསུངས་ཏེ། དེ་ལ་ཤེས་རབ་ཀྱི་ཕུང་པོ་འདི་ནི་སྡུག་བསྔལ་འཕགས་པའི་བདེན་པའོ་ཞེས་ཡང་དག་པ༌[^253]ཇི་ལྟ་བ་བཞིན་དུ་ཤེས་པ་དང་། འདི་ནི་སྡུག་བསྔལ་ཀུན་འབྱུང་བ༌[^254]འཕགས་པའི་བདེན་པའོ་ཞེས་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་ཤེས་པ་དང་། འདི་ནི་སྡུག་བསྔལ་འགོག་པ་འཕགས་པའི་བདེན་པའོ་ཞེས་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་ཤེས་པ་དང་། འདི་ནི་སྡུག་བསྔལ་འགོག་པར་འགྲོ་བར་བྱེད་པའི་ལམ་འཕགས་པའི་བདེན་པའོ་ཞེས་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་ཤེས་པ་སྟེ། འཕགས་པའི་བདེན་པ་བཞི་ཕྱིན་ཅི་མ་ལོག་པར་ཤེས་པ་ནི་ཤེས་རབ་ཀྱི་ཕུང་པོ་ཡོངས་སུ་རྫོགས་པར་བྱེད་པ་ཞེས་པའོ། །

[Block 267]
འདི་ནི་བྱ་བ་བྱས་པ་རབ་ཏུ་བསྒྲུབ་པ༌[^255]བསྟན་ཏེ། འདི་ལྟར་ཡེ་ཤེས་ཤིན་ཏུ་རྣམ་པར་དག་པས་ནི་ཉོན་མོངས་པ་སྤངས་པ་མངོན་སུམ་དུ་བྱེད་པའི་ཕྱིར་རོ། །

[Block 268 [HEADING]]
###### **འབྲས་བུ།** ^1-1-3-3-1-5-0

[Block 269]
དེ་བས་ན་མདོ་ལས་ཀྱང་། ཤེས་རབ་ཀྱི་ཕུང་པོ་ཡོངས་སུ་རྫོགས་ནས་རྣམ་པར་གྲོལ་བའི་ཕུང་པོ་ཡོངས་སུ་རྫོགས་པར་བྱེད་པ་ཞེས་གསུངས་ཏེ། དེ་ཡང་ཚུལ་ཁྲིམས་རྣམ་པར་དག་པ་ནི་འགྱོད་པ་མེད་པར་འགྱུར་རོ། །

[Block 270]
འགྱོད་པ་མེད་ན་དགའ་བ་དང་མཆོག་ཏུ་དགའ་བ་དང་ཤིན་ཏུ་རྣམ་པར་སྦྱངས་པ་དང་བདེ་བར་འགྱུར་རོ། །

[Block 271]
བདེ་བར་གྱུར་པའི་སེམས་མཉམ་པར་འཇོག་གོ། །

[Block 272]
སེམས་མཉམ་པར་གཞག་ན་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་རབ་ཏུ་ཤེས། ཡང་དག་པ༌[^256]ཇི་ལྟ་བ་བཞིན་དུ་མཐོང་བར་འགྱུར་རོ། །

[Block 273]
ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་ཤེས་ཤིང་མཐོང་བས་སྐྱོ་བར་འགྱུར་རོ། །

[Block 274]
སྐྱོ་བར་གྱུར་ན་འདོད་པའི་ཟག་པ་ལས་སེམས་རྣམ་པར་གྲོལ་བ་དང་། སྲིད་པའི་ཟག་པ་དང་། མ་རིག་པའི་ཟག་པ་ལས་སེམས་རྣམ་པར་གྲོལ་ཏེ། རྒྱུད་ལ་དྲི་མ་མེད་པ་འཐོབ་པར་འགྱུར་བས་ན། རྣམ་པར་གྲོལ་བའི་ཕུང་པོ་ཡོངས་སུ་རྫོགས་པར་བྱེད་པ་ཞེས་བྱའོ། །

[Block 275]
འདིས་ནི་འབྲས་བུ་བསྟན་ཏེ། རྣམ་པར་གྲོལ་བའི་ཕུང་པོ་ནི་བསླབ་པ་གསུམ་ལ་ཞུགས་པའི་འབྲས་བུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 276 [HEADING]]
###### **དེ་རབ་ཏུ་རིག་པ།** ^1-1-3-3-1-6-0

[Block 277]
དེ་ལྟར་ཁམས་གསུམ་གྱི་ཉོན་མོངས་པ་ལས་སེམས་རྣམ་པར་གྲོལ་ནས་དེའི་འོག་ཏུ་རྣམ་པར་གྲོལ་བ་ཉིད་དུ་ཤེས་ཤིང་རིག་པའི་ཡེ་ཤེས་སྐྱེས་ཏེ། དེ་བས་ན་མདོ་ལས་ཀྱང་། རྣམ་པར་གྲོལ་བའི་ཕུང་པོ་ཡོངས་སུ་རྫོགས་ནས་རྣམ་པར་གྲོལ་བའི་ཡེ་ཤེས་མཐོང་བའི་ཕུང་པོ་ཡོངས་སུ་རྫོགས་པར་བྱེད་ཅེས་གསུངས་སོ། །

[Block 278]
འདིས་ནི་དེ་རབ་ཏུ་རིག་པ་བསྟན་ཏེ། རྣམ་པར་གྲོལ་བའི་འོག་ཏུ་བདག་གི་སྡུག་བསྔལ་ནི་ཤེས་པར་བྱས། ཀུན་འབྱུང་བ་ནི་སྤངས། འགོག་པ་ནི་མངོན་སུམ༌[^257]དུ་བྱས། ལམ་ནི་བསྒོམས་པས༌[^258]ད༌[^259]སྡུག་བསྔལ་ཤེས་པར་བྱ་མི་དགོས། ཀུན་འབྱུང་བ་སྤང་མི་དགོས། འགོག་པ་མངོན་སུམ་དུ་བྱ་མི་དགོས། ལམ་བསྒོམ་མི་དགོས་ཏེ། སྐྱེ་བ་ཟད་དོ། །

[Block 279]
ཚངས་པར་སྤྱད་པ་བསྟེན་ཏོ། །

[Block 280]
བྱ་བ་བྱས་སོ། །

[Block 281]
སྲིད་པ་འདི་ལས་གཞན་མི་ཤེས་སོ་ཞེས་ཁོང་དུ་ཆུད་པའི་ཕྱིར་རོ། །

[Block 282 [HEADING]]
###### ཉན་ཐོས་ཀྱི་ཐེག་པ་ལ་མཁས་པ་རྣམ་གྲངས་གཞན། ^1-1-3-3-2-0

[Block 283]
གཞན་ཡང་ཉན་ཐོས་ཀྱི་ཐེག་པ་ལ་མཁས་པ་ནི་ཞེས་བྱ་བས་ཉན་ཐོས་ཀྱི་ཐེག་པ་ལ་མཁས་པ་རྣམ་གྲངས་གཞན་དུ་སྟོན་ཏེ། མཁན་པོ་དང་སློབ་དཔོན་གྱིས་བཤད་པའི་སྒྲ་ལ་བརྟེན༌[^260]ནས་གང་ཟག་ལ་བདག་མེད་པར་དམིགས་པ་ནི་ཉན་ཐོས་ཏེ། ཉན་ཐོས་དེ་དག་གི་ཐེག་པ་ནི་ཉན་ཐོས་ཀྱི་ཐེག་པའོ། །

[Block 284]
དེ་ཡང་རྣམ་པ་གཉིས་སུ་རིག་པར་བྱ་སྟེ། མི་མཐུན་པའི་ཕྱོགས་ལ་སུན་འབྱིན་པ་དང་། གཉེན་པོའི་ས་ལ་ཡོན་ཏན་དུ་ལྟ་བའོ། །

[Block 285 [HEADING]]
###### **མི་མཐུན་པའི་ཕྱོགས་ལ་སུན་འབྱིན་པ།** ^1-1-3-3-2-1-0
--- END BLOCKS ---
