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
[Block 386]
ཅི་སོག་མ་གཅིག་ཆོད་པས་སོག་མ་ཀུན་བརྡབས་པར་འགྱུར་རམ། གང་གསུངས་པ།

[Block 387 [VERSE]]
བསྐལ་པ་བརྒྱ་དག་སྙེད་དུ་ཡང་། །
ལས་རྣམས་ཆུད་ཟར་མི་འགྱུར་ཏེ། །
ཚོགས་དང་དུས་དང་ལྡན་པ་ན། །
ལུས་ཅན་རྣམས་ལ་འབྲས་བུར་སྨིན། །

[Block 388]
ཞེས་བྱ་བ༌[^263]ལ་སོགས་པ་དེ་ཇི་ལྟར་ཤེས་པར་བྱ་ཞེ་ན། རྣམ་པར་འགྱོད་པ་ལ་སོགས་པ་སྤྱོད་པའི་མཐུས་ལས་གང་དག༌[^264]མངོན་པར་མ་སྦྱངས་ཤིང་བསྲབས་པར་མ་བྱས་པ་དེ་དག་ནི་བཤད་པའི་ཆོས་འདི་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 389]
དེ་ལྟར་ཡང་གསུངས་པ།

[Block 390 [VERSE]]
མི་ཤེས་པས་ནི་སྡིག་པ་ཆུང་བྱས་འོག་ཏུ་འགྲོ། །
མཁས་པས་ཉེས་པ་ཆེ་བྱས་ཀྱང་ནི་ཡང༌[^265]བར་འགྱུར། །
བསྒོངས་པའི་ལྕགས་ནི་ཆུང་ཡང་ཆུ་ཡི་འོག་ཏུ་འབྱིངས།[^266] །
དེ་ཉིད་སྣོད་དུ་བྱས་ན་ཆེ་ཡང་སྟེང་ན་འཕྱོ། །

[Block 391]
ཞེའོ། །

[Block 392]
ངེས་པར་མི་མྱོང་བའི་དུས་གསུམ་གྱི༌[^267]སྡིག་པའི་ལས་བགྲང་བ་ལས་འདས་པ་དེ༌[^268]ཡང་ལས་ཀྱི༌[^269]དབང་གིས་ཕྱོགས་བཅུ་ཀུན་དུ་སྐད་ཅིག་གིས་འཁོར་བའི་མཐའི་བར་དུ་རྒྱུན་དུ་ངན་སོང་གསུམ་དུ་སྐྱེས་པའི་སེམས་ཅན་རྣམས་ལ་ཕན་པ་དང་བདེ་བའི་ཕྱིར་དེ་དག་གི་རིས་དང་རྒྱ་དང་ཁ་དོག་དང་དབྱིབས་དང་ཚད་རྣམས༌[^270]ཐ་དད་པར་འབྲས་བུ་རྣམ་པར་སྨིན་པར་གདོན་མི་ཟ་བར་རོ་མྱོང་བར༌[^271]མི་བྱེད་དོ། །

[Block 393]
དགེ་བའི་ལས་ཀྱིས་ཀྱང་སོགས་པའི་འབྲས་བུ་སྨིན་པར་བྱ་ནུས་པའི་མཐུ་འདི་ལྟར་ཡོངས་སུ་འབྱུང་ངོ་། །ཇི་ལྟ༌[^272]ཞེ་ན། འབྲས་བུ་རྣམ་པར་སྨིན་པར་འགྱུར་བ་ལས་བྱང་ཆུབ་ཉིད་དུ་སྨོན་ལམ་གྱི་མཐུས་བསྔོས་ཤིང་། གདོན་མི་ཟ་བར༌[^273]བྱེད་པའོ། །

[Block 394]
གཟུགས་དང་གཟུགས་མེད་པ་ན་སྤྱོད་པའི་མི་གཡོ་བའི་ལས་བསམ་གཏན་ལ་སྙོམས་པར་འཇུག་པའི་རྒྱུ་དེའི་སྟོབས་ཉིད་ཀྱང་དེ་ལས་བཟློག་སྟེ། ལས་ལ་དབང་བས་སེམས་ཅན་གྱི༌[^274]དོན་དུ་གར་དགའ་བར་སྦྱོར་བ་སྟེ། འདི་ནི་དག་པར་བྱེད་པའོ། །

[Block 395]
ཉོན་མོངས་སྟོབས་རྣམས་ཀུན་དུ་འཇོམས་པར་བྱེད། །ཅེས་བྱ་བ་ནི་ལུས་དང་སེམས་ཀྱི་རྒྱུད་སྙོན་རྨོངས་པར་བྱེད་པ་ནི་ཉོན་མོངས་པ་སྟེ་འདོད་ཆགས་ལ་སོགས་པའོ། །

[Block 396]
དེ་དག་གི་སྟོབས་ལྷག་པར་ཆེ་བས་དེའི་མཐུས་འགྲོ་བ་ཐམས་ཅད་ལ་རིགས་པ་དང་མི་རིགས་པ་དང་། ཕན་པ་དང་། མི་ཕན་པ་དང་། ལྕི་བ་དང་ཡང་བ་ལ་སོགས་པ་ཐམས་ཅད་མི་ཤེས་པ་ལ་སོགས་པ་དེ་ལ་མི་གཙང་བ་ལ་སོགས་པ་བསྒོམས་པས༌[^275]འཇིག་རྟེན་གྱི་ལམ་གྱིས་ཡོངས་སུ་སྦྱངས་པ་སྟེ། མངོན་པར་གཞིལ་བའོ། །

[Block 397]
མདོར༌[^276]ན་ཉོན་མོངས་པ་ལ་དབང༌[^277]བས་བྱང་ཆུབ་ཀྱི་ཡན་ལག་གི་དངོས་པོར་འགྱུར་བའོ། །

[Block 398]
བདུད་ཀྱི་སྟོབས་རྣམས་སྟོབས་མེད་རབ་བྱེད་ཅིང་། །ཞེས་བྱ་བ་ལ་བདུད་ནི་ལྷའི་བུ་ལ་སོགས་པ་སྟེ། དེ་དག་གི་སྟོབས་ཀྱིས་བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པའི་བར་ཆད་བྱེད་ནུས་པ་དེ་ལ་མངོན་པར་ཤེས་པའི་སྟོབས་ཀྱིས་སྟོབས་མེད་པ་དང་། མཐུ་མེད་པ་དང་། གནས་མེད་པར་བྱེད་པའོ། །

[Block 399]
བཟང་པོ་སྤྱོད་པའི་སྟོབས་ཀུན་རྫོགས་པར་བགྱི། །ཞེས་བྱ་བ་ནི་བཟང་པོ་སྤྱོད་པའི་སྟོབས་ནི་གཉེན་པོའི་མི་མཐུན་ཕྱོགས་རྣམས་ཀྱིས་མི་ཚུགས་ཤིང་། མངོན་པར་འདུ་ཤེས༌[^278]མི་བྱེད་པའོ། །

[Block 400]
དེ་དག་ཀུན་མ་ལུས་པར་རྫོགས་པར་བྱ་བ་ནི༌[^279]གོང་དུ་བཤད་པའི་རྫུ་འཕྲུལ་ལ་སོགས་པ་སྟོབས་བཅུ་བཤད་པ་དང་། གང༌[^280]དུ་སྨོས་པའི་གཉེན་པོ་རྣམ༌[^281]གསུམ་མོ། །

[Block 401 [HEADING]]
#### ལས། ^2-8-14-0

[Block 402]
གང་ཡང༌[^282]བྱང་ཆུབ་སེམས་དཔའི་ལས་ནི་རྣམ་པ་བཅུ་བཞི་པ་སྟེ། ལས་དེ༌[^283]ཡང་རྣམ་པ་བརྒྱད་དོ། །

[Block 403]
ཞིང་རྣམས་རྒྱ་མཚོ་རྣམ་པར་དག་བྱེད་ཅིང་། །ཞེས་བྱ་བ་ལ་སོགས་པ་ཚིགས་སུ་བཅད་པ་རྣམ་པ་གཉིས་ཏེ། དེ་ཡང་གང་ཞེ་ན། ཞིང་རྣམས་རྒྱ་མཚོ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། དེ་ཡང་སངས་རྒྱས་ཀྱི་ཞིང་རྒྱ་མཚོ་བདེ་བ་ཅན་དང་པད་མོ་ཅན་ལྟར་དག་པར་བྱེད་པའོ། །

[Block 404]
དེ་བཞིན་དུ་འཁོར་བ་ན་རྒྱུ་ཉོན་མོངས་པའི་ལྕགས་སྒྲོག་གིས༌[^284]བཅིངས་པའི་སེམས་ཅན་རྒྱ་མཚོ་སྙེད་ལ་རྫུ་འཕྲུལ་དང་ཀུན་བརྗོད་པའི་ཆོ་འཕྲུལ་རྣམ་པ་གཉིས་ཀྱིས་མགུ་བར་བྱས་ནས་རྗེས་སུ་བསྟན་པའི་ཆོ་འཕྲུལ་གྱིས་སྐད་ཅིག་ཏུ་རྣམ་པར་གྲོལ་བར་བྱེད་པའོ། །

[Block 405]
ཆོས་རྣམས་རྒྱ་མཚོ་རབ་ཏུ་མཐོང་བྱེད་ཅིང་། །ཞེས་བྱ་བ་ནི་ཐོབ་པར་བྱ་བའི་ཆོས་རྒྱ་མཚོ་སྙེད་དང་། བཤད་པའི་ཆོས་རྒྱ་མཚོ་སྙེད་ཤེས་རབ་ཀྱི་མིག་གིས་སྐད་ཅིག་རེ་རེ་ལ་ཡང་མཐོང་བར་བྱའོ། །ཤེས་པར་བྱ་བ་མཐའ་ཡས་པས་ན་ཡེ་ཤེས་ཀྱང་མཐའ་ཡས་པ་སྟེ། དེ་བས་ན་ཡེ་ཤེས་རྒྱ་མཚོ་ཞེས་བྱ་བ་སྟེ། རབ་ཏུ་རྟོགས་པར་བྱེད་ཅེས་བྱ་བ་ནི་ཁོང་དུ་ཆུད་པར་བྱ༌[^285]སྟེ། རྟོགས་པར་བྱེད་དོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 406]
སྤྱོད་པ་རྒྱ་མཚོ་ཞེས་བྱ་བ་ནི༌[^286]བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་དང་། བཟང་པོ་སྤྱོད་པ་གཉིས་དམིགས་ཀྱིས་མ་ཕྱེ་བས༌[^287]ན་གཉི་ག་གཟུང་བར་རིག་པར་བྱའོ། །

[Block 407]
དེ་ལ་བྱང་ཆུབ་ཀྱི་སྤྱོད་པ་ནི་སངས་རྒྱས་ཀྱི་ཆོས་རྣམས་སྒྲུབ་པ༌[^288]སྟེ་ཡེ་ཤེས་ཀྱི་ཚོགས་སོ། །

[Block 408]
བཟང་པོ་སྤྱོད་པ་ཡང་འགྲོ་བ་ཐམས་ཅད་ལ་ཕན་པ་དང་བདེ་བར་བྱེད་པ་སྟེ་བསོད་ནམས་ཀྱི་ཚོགས་སོ། །

[Block 409]
བཟང་པོ་སྤྱོད་པ་དང་། བྱང་ཆུབ་ཀྱི་སྤྱོད་པ་གཉི་ག་ཡང་བྱང་ཆུབ་བསྒྲུབ་པ༌[^289]ཡིན་མོད་ཀྱི། མངོན་སུམ༌[^290]དང་གཅིག་ནས་གཅིག་ཏུ་བརྒྱུད་པ་ཙམ་ཞིག་བྱེ་བྲག་ཡོད་དོ། །

[Block 410]
སྤྱོད་པ་རྒྱ་མཚོ་དག་མངོན་པར་ཤེས་པའི་སྟོབས་ཀྱིས་སྐད་ཅིག་མ་རེ་རེས་རྣམ་པར་དག་པར་བྱེད་པ་ནི་དྲི་མ་མེད་པར་བྱེད་པའོ། །

[Block 411]
སྨོན་ལམ་རྒྱ་མཚོ་ཞེས་བྱ་བ་ནི་སྐད་ཅིག་མ་རེ་རེ་ལ་ཚུལ་ཁྲིམས་དང་། ཏིང་ངེ་འཛིན་གྱི་མཐུས་རྫོགས་པར་བྱེད་པའོ། །

[Block 412]
སངས་རྒྱས་རྒྱ་མཚོ་ཕྱོགས་བཅུ་ནས་མཆོད་པའི་སྤྲིན་གྱིས་ནམ་མཁའ་ཁྱབ་པར་སྐད་ཅིག་གིས་རབ་ཏུ་མཆོད་པའོ། །

[Block 413]
བསྐལ་པ་རྒྱ་མཚོར་མི་སྐྱོ་སྤྱད་པར་བགྱི། །ཞེས་བྱ་བ་ནི་མི་སྐྱོ་བའི་ཡིད་ཀྱིས་སོ། །

[Block 414 [HEADING]]
#### རྗེས་སུ་སློབ་ཅིང་བསྔོ་བ། ^2-8-15-0

[Block 415]
སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའི་རྗེས་སུ་སློབ་པར་བསྔོ་བ་ནི་རྣམ་པ་བཅོ་ལྔ་པ་སྟེ། དེ་ཡང་རྣམ་པ་གཉིས་སོ། །

[Block 416]
དེ་ལ་དེ་བཞིན་གཤེགས་པའི་རྗེས་སུ་སློབ་པར་བསྔོ་བ་གང་ཞེ་ན། གང་ཡང་དུས་གསུམ་གཤེགས་པའི་རྒྱལ་བ་ཡི། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། གང་རྒྱལ་བ་དུས་གསུམ་དུ༌[^291]གཤེགས་པ་རྣམས་ཀྱི་བྱང་ཆུབ་ཀྱི་སྤྱོད་པ་དང་སྨོན་ལམ་གྱི་ཁྱད་པར་དེ་དག་ཐམས་ཅད་བདག་གིས་མ་ལུས་པར་རྫོགས་པར་བགྱིའོ་ཞེས་བྱ་བ་སྟེ། ཡོངས་སུ་རྫོགས་ཤིང་རབ་ཏུ་ཆུད་པར་བྱའོ། །

[Block 417]
བཟང་པོ་སྤྱོད་པས་ཞེས་བྱ་བ་ནི་བཟང་པོ་སྤྱོད་པས་སོ། །

[Block 418]
བྱང་ཆུབ་སངས་རྒྱས་ནས་ཞེས་བྱ་བ་ནི་བླ་ན་མེད་པའི་བྱང་ཆུབ་ཏུ་སངས་རྒྱས་པར་བྱ་བའོ།[^292] །

[Block 419]
ལུས་དང་ངག་དང་ཡིད་རྣམས་ཀྱི་སྤྱོད་པ་དང་ཞིང་དང་སྨོན་ལམ་རྣམས་རྣམ་པར་དག་པས་འཕགས་པ་ཀུན་དུ་བཟང་པོ་ལ་སོགས་པ་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་རྗེས་སུ་སློབ་པར༌[^293]བསྔོ་བ་སྟེ། ཚིགས་བཅད་གསུམ་མོ། །དེ་ཡང་གང་ཞེ་ན། སྲས་ཀྱི་ཐུ་བོ་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་བཟང་པོ་སྤྱོད་པ་གང་ཡིན་པ་དང་། དེ་ལྟར་བྱང་ཆུབ་སེམས་དཔའི་རྣམ་པར་ཐར་པ་ཇི་སྙེད་པ་དང་། ཏིང་ངེ་འཛིན་ཇི་སྙེད་པ་དང་། མདོར་ན་བྱང་ཆུབ་སེམས་དཔའི་ཡོན་ཏན་ལ་སོགས་པ་ཇི་སྙེད་པ་དེ་དག་ཐམས་ཅད་ཀྱི་མཐར་ཕྱིན་པ་ནི་འཕགས་པ་ཀུན་དུ་བཟང་པོ་བྱང་ཆུབ་སེམས་དཔའ་སྟེ། དེ་བས་ན་སྲས་ཀྱི་ཐུ་བོ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 420]
དེ་ལྟར། །རྒྱལ་བ་ཀུན་གྱི༌[^294]སྲས་ཀྱི་ཐུ་བོ་ནི། །འཕགས་པ་ཀུན་དུ་བཟང་པོ་ཞེས་བྱ་བ་བྱང་ཆུབ་སེམས་དཔའ་ཆེན་པོའོ། །

[Block 421]
མཁས་པ་དེ་དང་ཞེས་བྱ་བ་ནི་དེ་ཉིད་ལ༌[^295]མཁས་པའོ། །

[Block 422]
མཚུངས་པར་སྤྱད་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་མཐུན་པར་སྤྱད་པ་སྟེ། ཇི་ལྟར་བསྟན་པའི་དགེ་བའི་རྩ་བ་འདི་དག་ཐམས་ཅད་སྐད་ཅིག་རེ་རེ་ལ་ཡོངས་སུ་བསྔོ་བར་བྱ་བའོ། །

[Block 423]
ལུས་དང་ངག་དང་ཡིད་ཀྱང་རྣམ་དག་ཅིང་། །ཞེས་བྱ་བ་ནི་ལུས་དང་ངག་དང་ཡིད་རྣམས་ཀྱི་སྤྱོད་པ་རྣམ་པར་དག་པ་དང་ཞིང་རྣམས་རྣམ་པར་དག་པ་སྟེ། བསྔོ་བ༌[^296]བཟང་པོ་མཁས་པ་ཞེས་བྱ་བ་ནི་འཕགས་པ་ཀུན་དུ་བཟང་པོ་མཁས་པའོ། །

[Block 424]
ཅི་འདྲ་བར་ཞེས་བྱ་བ་ནི་ཇི་ལྟ་བུ་ཡིན་པར་རོ། །

[Block 425]
དེ་འདྲར་ཞེས་བྱ་བ་ནི་དེ་འདྲ་བར་བདག་ཀྱང་གྱུར་ཅིག་པའོ། །
--- END BLOCKS ---
