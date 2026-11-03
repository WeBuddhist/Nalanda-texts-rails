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
རང་བཞིན་མ་གྲུབ་པས་ནི་དཔེར་ན། འདི་ན་དུ་བ་མེད་དེ༌[^42]མི་དམིགས་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 72]
འདིས་ནི་ཁྱབ་པར་བྱེད་པའི་རང་བཞིན་མ་གྲུབ་པ་ཡང་བཤད་དེ། དཔེར་ན་འདི་ན་ཤིང་ཤ་པ་མེད་དེ་ཤིང་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 73]
མེད་པ་སྒྲུབ་པའི་མི་དམིགས་པ་འདི་ཐམས་ཅད་ལ་ཡང་བལྟར་རུང་བའི་བདག་ཉིད་དག་ཁོ་ན་དེ་དག་དང་། འགལ་བ་གྲུབ་པ་དང་མ་གྲུབ་པར་རིག་པར་བྱ་སྟེ། གཞན་དག་ལ་ནི་མེད་པ་དང་འགལ་བ་མི་འགྲུབ་པའི་ཕྱིར་རོ། །

[Block 74]
གལ་ཏེ་འགལ་བའི་འབྲས་བུ་དམིགས་པས་ཀྱང་མེད་པ་འགྲུབ་ན། དེའི་རྒྱུ་དམིགས་པས་ཅི་སྟེ་འགྲུབ་པར་མི་འགྱུར་ཞེ་ན།

[Block 75 [VERSE]]
དེ་དང་འགལ་བའི་རྒྱུ་མཚན་ནི། །
དམིགས་པ་སྦྱོར་བ་གང་ཡིན་ཏེ། །
རྒྱུ་མཚན་དག་ནི་འགལ་བ་ཉིད། །
མེད་ན་འཁྲུལ་པ་ཅན་ཡིན་ཏེ། །

[Block 76]
དཔེར་ན་འདི་ན་གྲང་བའི་རེག་པ་མེད་དེ་ཤིང་ཡོད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 77]
རྒྱུ་མཚན་དག་འགལ་བ་ན༌[^43]ནི་གོ་བར་བྱེད་པ་ཁོ་ན་ཡིན་ཏེ། དཔེར་ན་འདི་ན་བ་སྤུ་ལངས་པ་ལ་སོགས་པའི་ཁྱད་པར་མེད་དེ། མེའི་ཁྱད་པར་ཉེ་བ་ཅན་ཉིད་ཡིན་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 78]
འདིས་ནི་དེའི་འབྲས་བུ་ལས་ཀྱང་དེ་དང་འགལ་བའི་འབྲས་བུ་མེད་པར་རྟོགས་པར་བཤད་པ་ཡིན་ཏེ། དཔེར་ན་ཕྱོགས་འདི་ན་བ་སྤུ་ལངས་པ་ལ་སོགས་པ་དང་ལྡན་པའི་སྐྱེས་བུ་ཅན༌[^44]ཡིན་ཏེ། དུ་བ་ཡོད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 79]
དེ་དང་འགལ་བ་གྲུབ་པ་དེ་ཡང་གོང་དུ་རྒྱུ་མ་གྲུབ་པ་ཁོ་ནས་བསྟན་པ་ཡིན་ནོ། །

[Block 80]
དེ་ལྟར་ན་མི་དམིགས་པ་འདི་ནི་སྦྱོར་བའི་བྱེ་བྲག་གིས་རྣམ་པ་བརྒྱད་དོ། །

[Block 81]
དེ་ལ་འགལ་བའི་འབྲས་བུ་དམིགས་པ་བཤད་པ་གང་ཡིན་པ་དེ་ལ།

[Block 82 [VERSE]]
འགལ་འབྲས་ལ་ཡང་ཡུལ་དང་ནི། །
དུས་ལ་སོགས་ལ་ལྟོས་པར་འདོད། །
གཞན་དུ་འཁྲུལ་འགྱུར་མི་གྲང་བ། །
སྒྲུབ་པ་ལ་ནི་ཐལ་བ་བཞིན། །

[Block 83]
འོ་ན་རྒྱུ་ཚོགས་པས་འབྲས་བུ་སྐྱེ་བར་རྗེས་སུ་དཔོག་པར་བྱེད་པ་གང་ཡིན་པ་དེ་ཇི་ལྟར་གཏན་ཚིགས་རྣམ་པ་གསུམ་གྱི་ནང་དུ་འདུ་ཞེ་ན།

[Block 84 [VERSE]]
རྒྱུ་ཚོགས་པ་ཡིས་འབྲས་སྐྱེ་བར། །
རྗེས་སུ་དཔོག་པ་གང་ཡིན་པ། །
དོན་གཞན་ལ་ནི་མི་ལྟོས་ཕྱིར། །
དེ་ནི་རང་བཞིན་ཡིན་པར་བརྗོད། །

[Block 85]
འདི་ཡང་ཇི་ལྟར་ཉེ་བ༌[^45]ལས་གཞན་ལ་མི་ལྟོས་ཏེ། དེས་ན་ངོ་བོའི་དེ་ཙམ་དང་འབྲེལ་པའི་རང་བཞིན་ཡིན་ནོ།[^46] །དེ་ལ་ནི་རྒྱུ་ཚོགས་པ་ལས་འབྲས་བུ་སྐྱེ་བར་སྲིད་པ་རྗེས་སུ་དཔོག་པ་འབའ་ཞིག་ཏུ་ཟད་དེ། ཚོགས་པ་རྣམས་ཀྱི་འབྲས་བུ་བསྐྱེད་པར་རུང་བ་ཉིད་རྗེས་སུ་དཔོག་པའི་ཕྱིར་རོ། །

[Block 86]
རུང་བ་ཉིད་ཀྱང་ཚོགས་པ་ཙམ་དང་འབྲེལ་པས་རང་བཞིན་དུ་འགྱུར་བ་ཁོ་ན་རྗེས་སུ་དཔོག་པ་ཡིན་ནོ། །

[Block 87]
ཡང་ཅིའི་ཕྱིར་ཚོགས་པ་ལས་འབྲས་བུ་ཁོ་ན་རྗེས་སུ་དཔོག་པར་མི་བྱེད་ཅེ་ན། ཚོགས་པའི་འབྲས་བུ་ནུས་པ་ན།[^47] །

[Block 88 [VERSE]]
འགྱུར་བ་དང་འབྲེལ་འབྲས་བུ་ལ། །
མ་ངེས་པ་ནི་ཉིད་ཡིན་ཏེ། །
གགས་བྱེད་པ་དག་སྲིད་ཕྱིར་རོ། །

[Block 89]
རྒྱུའི་རྗེས༌[^48]ཚོགས་པ་དག་ཁོ་ནས༌[^49]རང་གི་འབྲས་བུ་སྐྱེད་པར༌[^50]བྱེད་པ་ནི་མ་ཡིན་ཏེ། འབྲས་བུ་སྐྱེ་བ་ནི་ཚོགས་པ་ལས་སྐྱེ་བ་ཅན་གྱི་ནུས་པ་རྣམས་ཀྱི་འགྱུར་བ་ལ་ལྟོས་པའི་ཕྱིར་རོ། །

[Block 90]
བར་འདིར་གགས་བྱེད་པ་སྲིད་པའི་ཕྱིར་འབྲས་བུ་རྗེས་སུ་དཔག་པ་མ་ཡིན་ནོ། །

[Block 91]
རུང་བ་ཉིད་ནི་རྫས་གཞན་ལ་མི་ལྟོས་པའི་ཕྱིར། རྗེས་སུ་དཔག་པ་ལ་འགལ་བ་མེད་དོ། །

[Block 92]
ནུས་པ་ཕྱི་མ་ཕྱི་མ་འགྱུར་བས་རྒྱུ་ཚོགས༌[^51]པ་འདི་འབྲས་བུ་བསྐྱེད་པར་ནུས༌[^52]པ་ཡིན་ཏེ། ནུས་པ་འགྱུར་བའི་རྐྱེན་གཞན་ལ་ལྟོས་པར་བྱ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 93]
ནུས་པ་སྐྱེ་བ་ནི་རང་གི་རིགས་སྔ་མ་ཙམ་གྱི་རྒྱུ་ཅན་ཉིད་ཡིན་པའི་ཕྱིར། ཚོགས་པའི་རུང་བ་ཉིད་ནི་གཞན་ལ་མི་ལྟོས་པ་ཞེས་བྱའོ། །

[Block 94]
འོ་ན་རྒྱུ་དང་འབྲས་བུར་མ་གྱུར་པ་གཞན་རོ་ལ་སོགས་པས་གཟུགས་ལ་སོགས་པ་རྟོགས་པ་གང་ཡིན་པ་དེ་ཇི་ལྟར་ཞེ་ན། དེ་ཡང་།

[Block 95 [VERSE]]
ཚོགས་པ་གཅིག་ལ་རག་ལུས་པའི། །
གཟུགས་ལ་སོགས་པ་རོས་རྟོགས་པ། །
རྒྱུའི་ཆོས་རྗེས་སུ་དཔག་པས་ཏེ། །
དུ་བས་བུད་ཤིང་འགྱུར་བ་བཞིན། །

[Block 96]
དེ་ལ་ནི་རྒྱུ་དེ་ལྟ་བུ་ཁོ་ན་རྗེས་སུ་དཔོག་པར་བྱེད་དོ། །

[Block 97]
རོའི༌[^53]རྒྱུ་དེ་ལྟ་བུ་ནི་གཟུགས་ཀྱི་ཉེ་བར་ལེན་པའི་རྒྱུ་ནུས་ལ༌[^54]ཞུགས་པ་ཅན་གྱི༌[^55]ལྷན་ཅིག་བྱེད་པའི་རྐྱེན་ཡིན༌[^56]ཞིང་རོ་སྐྱེད་པར་བྱེད་དེ། མེ༌[^57]བུད་ཤིང་འགྱུར་བའི་ཁྱད་པར་གྱི་ཉེ་བར་ལེན་པའི་རྒྱུའི་ལྷན་ཅིག་བྱེད་པའི་རྐྱེན་ཡིན་ཞིང་དུ་བ་བསྐྱེད་པ་དང་འདྲའོ། །

[Block 98]
འདི་ལྟར་ནུས་པ་འཇུག་པ་སྟེ། རང་གི་རྒྱུའི་འབྲས་བུ་བསྐྱེད་པར་བྱ་བ་ལ་མངོན་དུ་ཕྱོགས་པ་མེད་པར་ནི། རོ་མེད་དེ་ཉིད་གཞན་གྱི་རྒྱུ། །གཟུགས་ཀྱི༌[^58]ཉེ་བར་ལེན་པའི་རྒྱུ་རྣམས་ཀྱི་འཇུག་པའི་རྒྱུ་ཡིན་ནོ། །

[Block 99]
རོའི་ཉེ་བར་ལེན་པའི་རྒྱུ་འཇུག་པ་དེ་ཡང་གཟུགས་ཀྱི་ཉེ་བར་ལེན་པའི་རྒྱུ་འཇུག་པའི་ལྷན་ཅིག་བྱེད་པ་ཅན་ཡིན་ཏེ། དེའི་ཕྱིར་རྒྱུ་ཇི་ལྟ་བུ་ལས་བྱུང་བའི་རོས༌[^59]དེ་ལྟ་བུ་རྗེས་སུ་དཔོག་པར་བྱེད་པ་ན་གཟུགས་རྗེས་སུ་དཔོག་པར་བྱེད་པ་ཡིན་ནོ། །

[Block 100]
དེ་ལ་ཡང་། དེ་ལྟར་འདས་དུས་གཅིག་རྣམས་རྟོགས་ཀྱི་མ་འོངས་པ་རྣམས་ནི་མ་ཡིན་ཏེ། འཁྲུལ་པའི་ཕྱིར་རོ། །

[Block 101]
དེ་ལྟ་བས་ན། དེ་ནི་འབྲས་བུའི་རྟགས་ལས་སྐྱེས། །དེའི་ཕྱིར་གོ་བར་བྱེད་པའི་གཏན་ཚིགས་གཞན་ནི་མེད་དེ་རང་བཞིན་མ་འབྲེལ་པ་ནི་མེད་ན་མི་འབྱུང་བར་ངེས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 102]
འདིས་ནི་གྲོག་མ་འཕོ་བ་དང་། ཉ་འཕར་བ་ལ་སོགས་པ་ལས་ཆར་པ་ལ་སོགས་པ་རྗེས་སུ་དཔོག་པ་ཡང་བཤད་པ་ཡིན་ཏེ། དེ་ལ་ཡང་ཆར་པའི་རྒྱུ་འབྱུང་བར༌[^60]འགྱུར་བ་ཁོ་ན་གྲོག་མ་ལ་སོགས་པ་འཁྲུག༌[^61]པ་ལ་སོགས་པའི་རྒྱུ་ཡིན་ནོ། །

[Block 103]
རྒྱུ་མ་ཚོགས་པས་འབྲས་བུ་ནི། །རྗེས་སུ་དཔོག་པ་གང་ཡིན་དེ།[^62] །

[Block 104 [VERSE]]
ལྷག་མ་དང་ལྡན་ནུས་མེད་ཕྱིར། །
ལུས་ལས་འདོད་ཆགས་རྗེས་དཔོག་བཞིན། །

[Block 105]
རུང་བ་ཉིད་ཀྱང་རྒྱུ་ཚོགས་པ་དག་ཁོ་ནས་རྗེས་སུ་དཔོག་པར་བྱེད་དེ། མ་ཚོགས་པ་ལ་ཤིན་ཏུ་ནུས་པ་མེད་པའི་ཕྱིར། དཔེར་ན་ལུས༌[^63]དབང་པོ་དང་བློ་དག་ལས་འདོད་ཆགས་ལ་སོགས་པ་རྗེས་སུ་དཔོག་པ་བཞིན་ནོ། །

[Block 106]
འདོད་ཆགས་ལ་སོགས་པ་ནི་བདག་དང་བདག་གིར་ཞེན་པ་སྔོན་དུ་འགྲོ་བ་ཅན་ཡིན་ཏེ། ཉེས་པ་ཐམས་ཅད་སྐྱེ་བའི་སྔོན་དུ་འགྲོ་བ་ནི་ཚུལ་བཞིན་མ་ཡིན་པ་ཡིད་ལ་བྱེད་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 107]
ལུས་ལ་སོགས་པ་རྒྱུ་ཉིད་ནི་ཡིན་མོད་ཀྱི་འབའ་ཞིག་པ་རྣམས་ལ་ནི་ནུས་པ་མེད་པས་མི་མཐུན་པའི་ཕྱོགས་ལ་འཇུག་པ་མ་མཐོང་དུ་ཟིན་ཀྱང་རྗེས་སུ་དཔག་པ་ལྷག་མ་དང་ལྡན་པའི་ཕྱིར། ཐེ་ཚོམ་ཟ་བ་ཡིན་ནོ། །

[Block 108]
དེ་བཞིན་དུ།

[Block 109 [VERSE]]
མི་མཐུན་ཕྱོགས་ལ་མ་མཐོང་བ། །
ཙམ་གྱི་འབྲས་སྤྱི་མཐོང་བ་ལས། །
གཏན་ཚིགས་ཤེས་པ་ཚད་ལྟར་སྣང་། །
ཚིག་ལས་ཆགས་ཅན་ལ་སོགས་བཞིན། །

[Block 110]
གཡོ་བ་དང་ཚིག་ལ་སོགས་པ་ནི་འདོད་ཆགས་ལ་སོགས་པ་ཁོ་ནའི་འབྲས་བུ་མ་ཡིན་ཏེ། བརྗོད་པར་འདོད་པའི་སྤྱིའི་རྒྱུ་ཅན་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
