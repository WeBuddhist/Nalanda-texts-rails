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
[Block 281]
མི་གཡོ་བའི་ཕྱིར་བརྟན་པའོ། །

[Block 282]
གནས་སྐབས་ཐམས་ཅད་དུ་གནས་པའི་ཕྱིར་ཐེར་ཟུག་པའོ། །

[Block 283]
གཞན་དུ་མི་འགྱུར་བས་ཡོངས་སུ་འགྱུར་བའི་ཆོས་ཅན་མ་ཡིན་པའོ་ཞེས་བྱ་སྟེ། འདི་རྣམས་ནི་རང་བཞིན་གྱི་མིང་གི་བྱེ་བྲག་ཡིན་གྱི་ནང་གི་བྱེད་པའི་སྐྱེས་བུའི་ནི་མ་ཡིན་ཏེ། རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་རྐྱེན་འདི་པ་ཙམ་ལ་རྣམ་པར་གནས་པས་ན་སྔར་ཉིད་དུ་དེ་དག་བཀག་པའི་ཕྱིར་རོ། །

[Block 284]
ཇི་སྐད་དུ་སྟོང་པ་ཉིད་དོན་དམ་པའི་མདོ་ལས།

[Block 285]
མིག་སྐྱེས་བཞིན་པ་གང་དུ་ཡང་འབྱུང་བར་མི་འགྱུར་རོ། །

[Block 286]
འགག༌[^248]བཞིན་པ་ནམ་ཡང་དམྱལ་བར་འགྲོ་བ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 287]
ལས་ཡོད་ཅིང་ལས་ཀྱི་རྣམ་པར་སྨིན་པ་ཡོད་ལ། བྱེད་པ་པོ་ནི་མ་དམིགས་སོ། །

[Block 288]
གང་ཕུང་པོ་འདི་ནི་འཇིག་ལ་ཕུང་པོ་གཞན་དུ་ཉིང་མཚམས་སྦྱོར་ཏེ། ཆོས་ཀྱི་བརྡ༌[^249]གཞན་ལས་སོ། །

[Block 289]
དེ་ལ་ཆོས་ཀྱི་བརྡ༌[^250]ནི་འདིའོ། །

[Block 290]
འདི་ལྟར་མ་རིག་པའི་རྐྱེན་གྱིས་འདུ་བྱེད་ཅེས༌[^251]བྱ་བ་ལ་སོགས་པའོ། །

[Block 291]
མདོ་འདིར་ནི་ཐོག་མར་བྱེད་པ་པོ་བཀག་ལ། ཕྱིས་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་རྣམ་པར་གཞག་པ་ནི། གང་ལ༌[^252]རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་རྣམ་པར་གཞག་པ་ལས་མིག་ཡོད་པ་ཐོབ་པ་ལ། ཐར་པ་འདོད་པ་རྣམས་མིག་ཏུ་མངོན་པར་ཞེན་པའི་གཉེན་པོར་ཆོས་ཐམས་ཅད་བདག་མེད་པར་ཉེ་བར་བསྟེན་པས་སྟོང་པ་ཉིད་རྣམ་པར་ཐར་པའི་སྒོ་ལ་འཇུག་པའི་ཕྱིར་རོ། །

[Block 292]
དེའི་ཚེ་རྟག་པའི་བདག་བཀག་པས་ཅུང་ཟད་ཀྱང་ཉེ་བར་མཁོ་བ༌[^253]མེད་ཅིང་། མིག་ཇི་ལྟ་བར་གནས་པ་ལ་མངོན་པར་ཞེན་པ་མ་བཀག་ན་རྟག་པའི་བདག་བཀག་ཀྱང་མིག་ལ་སོགས་པར་མངོན་པར་ཞེན་པའི་བ་སྤུ་ཡང་འགུལ་བར་ནུས་པ་མ་ཡིན་ནོ། །

[Block 293]
རི་དགས་དང་བྱ་ལ་སོགས་པ་བདག་རྟག་པ་མི་དམིགས་ཀྱང་དེར་ཞེན་པས་དེའི་ཕྱིར་འདིར་རྟག་པའི་བདག་བཀག་པའི་སྒོ་ནས་མིག་བདག་མེད་པར་འཇོག་པ་ནི་མ་ཡིན་ནོ། །

[Block 294]
འཇོག་ན་ཡང་ཉེ་བར་ལེན་པ་ལ་རྟག་པའི་བདག་བཀག་པས་སམ་རང་བཞིན་དང་བཅས་པ་བཀག་པས་སོ། །

[Block 295]
གང་ཡང་དེ་ལྟར་ཅི་སྐད་གསུངས་པའི་རིགས་པས་བདག་མེད་པས་དེའི་ཚེ། གཉེན་པོ་མེད་པའི་ཕྱིར་བདག་མེད་པ་ཉིད་ཀྱང་ཡོད་པ་མ་ཡིན་ནོ་ཞེས་གསུངས་པ། བདག་མེད་མིན་ཞེས་པ་ལ། བདག་དང་འགལ་བའི་ཆོས་འགའ་ཡང་མེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 296]
ཡང་ན་ཇི་ལྟར་དངོས་པོ་དང་དངོས་པོ་མེད་པ་ལྟར་བདག་དང་བདག་མེད་ལ། ཇི་ལྟར་ཡང་དངོས་པོ་མེད་ན་དངོས་པོ་མེད་པ་མེད་ལ། དེ་བཞིན་དུ་བདག་མེད་ན་བདག་མེད་པ་ཡང་སྲིད་པ་མེད་དོ་ཞེས་དགོངས་པའོ། །

[Block 297]
ཡང་གང་དུ་བདག་ཡོད་པ་ཡིན་ན་དེ་ནི་བདག་མེད་པའི་གཟུགས་ལ་སོགས་པའི་དངོས་པོར་ཡང་དེ་མེད་དེ། ཉེ་བར་ལེན་པ་པོ་མེད་ན་ཉེ་བར་བླངས་པ་མེད་པས་གཟུགས་ལ་སོགས་པ་མ་གྲུབ་པའི་ཕྱིར་ཞེས་གསུངས་པ། བདག་མེད་མིན་པ་སྟེ་བདག་མེད་པ་ཡང་མ་གྲུབ་པས་ཆོས་ཐམས་ཅད་མིང་ཙམ་དུ་གྲུབ་པའོ།[^254] །

[Block 298]
འདིར་སྨྲས་པ། གལ་ཏེ་ཡང་བདག་འབའ་ཞིག་པ་མེད་ན་བདག་མེད་པ་འབའ་ཞིག་པ་ཡང་མེད་ལ། དེ་ལྟར༌[^255]ན་ཡང་མེ་དང་བུད་ཤིང་དག་བཞིན་དུ་བདག་དང་བདག་མེད་དག་ཕན་ཚུན་ལྟོས་ནས་གྲུབ་པ་ཡོད་པས་དེས་བདག་དང་བདག་མེད་པ་གཉིས་ཀ་ཡང་འབྱུང་བར་འགྱུར་ཞེ་ན། གསུངས་པ། དེ་ལྟར་ཡང་བདག་དང་བདག་མེད་ཅེས་པ་ལ་ཡོད་པ་མ་ཡིན་ནོ་ཞེས་པ་ཚིག་གི་ལྷག་མའོ། །

[Block 299]
གལ་ཏེ་ཡང་དཔྱད་བཞིན་པས་བདག་གམ་བདག་མེད་པ་འགའ་ཞིག་ཡོད་ན། དེའི་ཚེ་ཕན་ཚུན་ལྟོས་པ་འགྲུབ་པར་འགྱུར་ལ། གང་དུ་དེ་གཉིས་མེད་ན་བདག་དང་བདག་མེད་པ་ག་ལ་འབྱུང་ཞེས་བྱ་སྟེ། དེས་ན་བདག་དང་བདག་མེད་པ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 300]
ཡང་ན་འདི་ནི་དོན་གཞན་ཏེ། ཁ་ཅིག་གིས་སྨྲས་པ། གལ་ཏེ་ཡང་བདག་དང་བདག་མེད་པ་མེད་ལ་དེ་ལྟ་ན་ཡང་བདག་དང་བདག་མེད་པ་བཀག་པའི་བདག་དང་བདག་མེད་པ་མ་ཡིན་པ་ཡོད་ལ། དེ་ཡོད་པས་དགག་བྱ་བདག༌[^256]མེད་པ་ཡང་འབྱུང་བར་འགྱུར་རོ། །

[Block 301]
གལ་ཏེ་ཡང་བདག་དང་བདག་མེད་པ་གཉིས་སུ་བརྟགས་པ་དང་བྲལ་བ་ཆོས་རྣམས་ཀྱི་རང་བཞིན་བདག་དང་བདག་མེད་པ་མ་ཡིན་པར༌[^257]འབྱུང་བར་འགྱུར་རོ་ཞེས་པ་འདི་ཡང་མི་རིགས་སོ་ཞེས་ཁོང་དུ་ཆུད་པར་བྱ་བའི་ཕྱིར་གསུངས་པ། བདག་དང་བདག་མེད་འགའ་ཡང་མེད། །ཅེས་བྱའོ། །

[Block 302]
འགའ་ཡང་མེད་ཅེས་པའི་འགག་པ་འདི་ཇི་ལྟར་ཕྱིས་དེ་མ་ཐག་པའི་བརྗོད་པ་འགའ་དང་མངོན་པར་འབྲེལ་ལ། དེ་བཞིན་དུ་སྔར་གྱི་དེ་མ་ཐག་པའི་བདག་དང་བདག་མེད་པ་དང་ཡང་འབྲེལ་ཏོ། །

[Block 303]
དེ་ལ་འདིར་རེ་ཞིག་སྔར་གྱི་རྟོག་པ་བརྗོད་དེ། ཇི་སྐད་བཤད་པའི་རིགས་པས་བདག་དང་བདག་མེད་པ་གཉིས་ཀ་ཡང་མ་གྲུབ་པའི་ཕྱིར། དེ་བཀག་ན་བདག་དང་བདག་མེད་པ་ག་ལ་འབྱུང་ཞེས་སྒྲུབ་བྱེད་གསུངས་པ། བདག་མིན་ཞེས་པ་ལ་སོགས་པའོ། །

[Block 304]
ཕྱི་མའི་རྟོག་པ་ཡང་བདག་དང་བདག་མེད་པ་ལོགས་སུ་བཞག་པའི་དངོས་པོ་རྣམས་ཀྱི་རང་བཞིན་ཡང་མེད་ལ། བདག་དང་བདག་མེད་པ་ལས་ཐ་དད་པའི་རང་བཞིན་མ་གྲུབ་པའི་ཕྱིར་བདག་དང་བདག་མེད་པ་མ་ཡིན་པ་འགའ་ཡང་མེད་དོ་ཞེས་གསུངས་པ། བདག་དང་བདག་མེད་མིན་འགའ་མེད། །ཅེས་སོ། །

[Block 305]
ཡང་འདིའི་དོན་གཞན་ཏེ། ཆོས་ཐམས་ཅད་ནི་མིང་ཙམ་མོ་ཞེས་རྣམ་པར་གཞག་པ་ན་མུ་སྟེགས་པས་སྨྲས་པ། ཆོས་ཐམས་ཅད་མིང་ཙམ་མ་ཡིན་ཏེ། ཁོ་བོ་ཅག་གི་གྲུབ་མཐས་བཤད་པ་བརྟག་པ༌[^258]མ་བྱས་པ་ལ་སོགས་པས་ཁྱད་པར་དུ་བྱས་པའི་བདག་གི་དོན་ཡོད་པའི་ཕྱིར་རོ་ཞེ་ན། འདིར་སྨྲས་པ། བདག་མེད་དེ། གང་གི་ཕྱིར་ཕ་རོལ་པོའི་བདག་གི་སྒྲ་ལ་བརྗོད་བྱའི་དོན་བདག་ཡོད་པ་མ་ཡིན་ཏེ། རང་ཉིད་ལས་མ་སྐྱེས་པའི་ཕྱིར་བོང་བུའི་རྭ་བཞིན་ལ། བརྟག་པ༌[^259]མ་བྱས་པ་ཀུན་ཏུ་འགྲོ་བ༌[^260]མ་ཡིན་ཏེ། ནམ་མཁའི་མེ་ཏོག་བཞིན་མ་སྐྱེས་པའི་ཕྱིར་བདག་མེད་དོ། །

[Block 306]
འབྱུང་བའི་སེམས་པ་ཅན་ཡང་འདི་སྙམ་དུ༌[^261]སེམས་ཏེ། བདག་མེད་པ་ནི་བདེན་ལ། འོན་ཀྱང་བདག་མེད་པ་འབྱུང་བ་ཙམ་ཡོད་དོ་ཞེས་སོ། །

[Block 307]
རང་གི་སྡེ་པ་དག་ཀྱང་སྨྲ་སྟེ། ནང་གི་བྱེད་པའི་སྐྱེས་བུ་དང་བྲལ་བའི་བདག་མེད་པ་ཕུང་པོ་ཙམ་ཡོད་ལ། བདག་ནི་རྣམ་པ་ཐམས་ཅད་དུ་མེད་དོ་ཞེས་སོ། །

[Block 308]
དེ་དག་ལ་ལྟོས་ནས་གསུངས་པ་བདག་མེད་མིན་ནོ། །

[Block 309]
བདག་མེད་པ་ནི་མེད་པ་ཉིད་དེ། ཇི་ལྟར་མེད་པ་དེ་ལྟར་ཡང་སྔར་ཉིད་དུ་རྒྱས་པར་བསྒྲུབས་སོ། །

[Block 310]
ཡང་རང་གི་སྡེ་པ་ཁ་ཅིག་ནི་འདི་སྐད་སྨྲ་སྟེ། ཉེ་བར་ལེན་པ་ལ་བཏགས་པའི་རྫས་སུ་ཡོད་ཅིང་གང་ཟག་ཏུ་ཡོད་པའི་དངོས་པོ་ནི་ཡོད་ལ། ཆོས་ཐམས་ཅད་བདག་མེད་པ་འདི་ལ་འགའ་ཞིག་གིས་དབང་དུ་བྱས་པ་མེད་པའི་ཕྱིར། དེ་ཡང་ཡོད་པས་དེའི་ཕྱིར་བདག་མེད་པ་ཡང་ཡོད་དོ་ཞེས་སོ། །

[Block 311]
སྨྲས་པ། བདག་དང་བདག་མེད་འགའ་ཡང་མེད། །ཇི་སྐད་དུ་སྨོས་པའི་རིགས་པས་ཆོས་དང་གང་ཟག་དག་བཀག་པའི་ཕྱིར། གང་གི་ཚེ་ཡང་འདི་ལྟར་བདག་དང་བདག་མེད་པ་སྟེ། བདག་དང་བདག་མེད་པ་ཡང་མི་འཐད་ལ། དེའི་ཚེ་ཐམས་ཅད་ཚིག་ཙམ་སྟེ། དོན་གྱིས་སྟོང་པར་གྲུབ་པོ། །འདིར་སྨྲས་པ། གལ་ཏེ་ཡང་ཁྱོད་ཀྱིས་བརྗོད་བྱའི་དོན་བཀག་ལ། དེ་ལྟ་ན་ཡང་གང་ཞིག་དོན་གྱིས་སྟོང་པའི་ཚིག་དེ་དེ་བཞིན་དུ་ཡོད་ལ། དེ་ལས་ཚིག་དམིགས་པའི་ཕྱིར་དངོས་པོ་གཞན་ཡང་འབྱུང་བར་འགྱུར་རོ་ཞེས་སོ། །

[Block 312]
ཡང་ན་བརྗོད་བྱ་ལས་གཞན་དུ་རྗོད་བྱེད་མི་འཐད་ལ། ཚིག་འདི་དག་མ་བཀག་པར་ཡོད་པས་དེའི་ཕྱིར་བརྗོད་བྱ་ཡང་འབྱུང་བར་འགྱུར་རོ་ཞེ་ན། སྨྲས་པ། གལ་ཏེ་རྗོད་བྱེད་ཡོད་པ་ཉིད་ན་བརྗོད་བྱ་འབྱུང་བར་འགྱུར་ལ། ཡོད་པ་མ་ཡིན་ནོ་ཞེས་སྒྲུབ་པར་བྱེད་པ་གསུངས་པ། བརྗོད་འགའ་མེད་ཅེས་སོ། །

[Block 313]
བརྗོད་བྱ་ལས་གཞན་དུ་རྗོད་བྱེད་ཀྱང་མི་འཇུག་པས་བརྗོད་པ༌[^262]ཡང་མེད་དོ། །

[Block 314]
འོ་ན་མོ་གཤམ་གྱི་བུའི་བརྗོད་པ་བརྗོད་བྱའི་དོན་གྱིས་སྟོང་ཡང་བརྗོད་བྱ་ལས་གཞན་པ་ཡོད་པས་རྗོད་པ་ཡོད་དོ་ཞེ་ན། སྨྲས་པ། བརྗོད་པས༌[^263]ནི་ཇི་ལྟ་བར་དངོས་པོ་དང་དངོས་པོ་མེད་པའི་བརྗོད་བྱ་ལ་བརྡར་བྱེད་ལ། དངོས་པོ་དང༌[^264]དངོས་པོ་མེད་པ་དེ་དག་ཀྱང་མེད་དོ་ཞེས་བསྒྲུབས་ལ། དེ་དག་མེད་ན་གཞན་བརྗོད་བྱ་ཅི་ཞིག་ཡོད། བརྗོད་བྱ་མེད་ན་རྗོད་བྱེད་མེད་པས་བརྗོད་པ༌[^265]ཡང་མེད་དོ། །

[Block 315]
ཡང་ན་གནས་པ་ལ་སོགས་པ་མེད་པར་བསྒྲུབས་པས། གནས་པ་ལ་སོགས་པ་མེད་ན་སྒྲ་མི་འགྲུབ་པ་ཐུགས་ལ་བཞག་ནས་བརྗོད༌[^266]འགའ་མེད་ཅེས་སོ། །

[Block 316]
ཡང་ན་ཚིག་ནི་དོན་གྱིས་སྟོང་པར་བསྒྲུབས་ལ། སྒྲ་ཡང་སྒྲ་གཞན་གྱི་བརྗོད་བྱ་ཡིན་པས་དོན་ཉིད་ལ་དོན་དེ་ཡང་མེད་པ་ཉིད༌[^267]དོ་ཞེས་བྱ་ལ། དོན་མེད་པའི་ཕྱིར་སྒྲ་ཡང་མེད་པར་གཟིགས་ནས་གསུངས་པ་བརྗོད༌[^268]འགའ་མེད་ཅེས༌[^269]སོ། །

[Block 317]
བརྗོད་པ༌[^270]མེད་པར་གྱུར་ན་ཡང་བརྗོད་བྱའི་དོན་གྲུབ་པ་མེད་དོ་ཞེས་གནས་སོ། །

[Block 318]
འདིར་སྨྲས་པ། གལ་ཏེ་རྗོད༌[^271]བྱེད་ཀྱིས་བརྗོད་པའི་དོན་ཀྱང་མེད་ན། དེའི་ཚེ་ཅི་ཞིག་ཡོད། སྨྲས་པ། ཁོ་བོས་སྒྱུ་མའི་ནོར་གྱིས་ཕྱུག་པོར་བྱེད་པའམ་སྨིག་རྒྱུའི་ཆུས་ཁྱོད་ཀྱི་ཆུའི་གདུང་བ་སེལ་བར་བྱེད་པའམ། སྒྱུ་མའི་རི་དགས་ཀྱི་ཤས་བཀྲེས་པ་ཉེ་བར་ཞི་བར་བྱེད་པར་མི་ནུས་སོ། །

[Block 319]
འོ་ན་འདིར༌[^272]ཁོ་ན་ཉིད་གང་ཡིན་པ་དེ་ཉིད་གཟུང་བར་བྱ་བར་འགྱུར་ལ། སླར་ཡང་འདིར་དེ་ཁོ་ན་ཉིད་དེ་ཅི་ཞེ་ན། སྨྲས་པ། གལ་ཏེ་ཁྱོད་དེ་ཁོ་ན་ཉིད་ལ་ཕྱིན་ཅི་ལོག་ཏུ་གོ་བ་དང་སྤོང་བ་དག་གིས་ལོག་པར་སྒྲུབ་པར་མི་བྱེད་ཅིང་ཆོས་ཉིད་ཟབ་མོ་ལ་གུས་པ་ཡང་སྐྱེད་ན་དེའི་ཚེ་ཁྱོད་ཀྱི།

[Block 320 [VERSE]]
བརྗོད་བྱ་མྱ་ངན་འདས་དང་མཚུངས། །
དངོས་པོ་ཀུན་གྱི་རང་བཞིན་སྟོང་། །
--- END BLOCKS ---
