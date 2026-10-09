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
གང་གི་ཕྱིར་འགྲོ་བ་པོ་གཅིག་པུ་ལ་གང་གི༌[^266]འགྲོ་བ་པོ་ཞེས་བྱ་བར་མངོན་པ་དང་འགྲོ་པོར་གྱུར་ནས་གང་འགྲོ་བར་འགྱུར་བའི་འགྲོ་བ་གཉིས་མི་འཐད་པ་དེའི་ཕྱིར་དེ་ལས་གཞན་པའི་འགྲོ་བ་ཡང་འགྲོ་བ་པོ་འགྲོ་བར་བྱེད་པ་མ་ཡིན་ནོ། །

[Block 387]
དེས་ན་ཚིག་སྨྲའོ། །

[Block 388]
བྱ་བ་བྱེད་དོ་ཞེས་བྱ་བ་ཡང་ལན་བཏབ་པ་ཡིན་ནོ། །

[Block 389]
འདིར་སྨྲས་པ། འགྲོ་བ་པོའི་བགྲོད་པར་བྱ་བ་གྲོང་དང་གྲོང་ཁྱེར་ལ་སོགས་པ་ཡོད་པ་མ་ཡིན་ནམ།[^267] བཤད་པ། དེ་ལ་ནི་ལན་བཏབ་ཟིན་ཏེ། གྲོང་དང་གྲོང་ཁྱེར་ལ་བརྟེན་ནས། ཅི་དེ་གྲོང་དུ་སོང་བ་ལ་འགྲོ་བ་ཡོད་དམ་མ་སོང་བ་ལ་འགྲོ་བ་ཡོད་དམ་བགོམ་པ་ལ་འགྲོ་བ་ཡོད་ཅེས་བསམས་ཟིན་པས་དེའི་ཕྱིར་དེ་ནི་གྱི་ནའོ། །

[Block 390]
ཡང་གཞན་ཡང་།

[Block 391 [VERSE]]
འགྲོ་པོ་ཡིན་པར་གྱུར་པ་ནི། །
འགྲོ་རྣམ་གསུམ་དུ་འགྲོ་མི་བྱེད། །
[^268]མ་ཡིན་པར་ནི༌[^269]གྱུར་དེ༌[^270]ཡང་། །
འགྲོ་རྣམ་གསུམ་དུ་འགྲོ་མི་བྱེད། །

[Block 392 [VERSE]]
ཡིན་དང་མ་ཡིན་གྱུར་པ་ཡང་། །
འགྲོ་རྣམ་གསུམ་དུ་འགྲོ་མི་བྱེད། །
དེ་ཕྱིར་འགྲོ་དང་འགྲོ་པོ་དང་། །
བགྲོད་པར་བྱ་བའང་ཡོད་མ་ཡིན། །

[Block 393]
འགྲོ་བ༌[^271]པོ་ཡིན་པར་གྱུར་པ་ཞེས་བྱ་བ་ནི་འགྲོ་བ་པོ་གང་འགྲོ་བ་དང་ལྡན་པའོ། །

[Block 394]
དེ་མ་ཡིན་པར་གྱུར་པ་ཡང་ཞེས་བྱ་བ་ནི་འགྲོ་བ་པོ་གང་འགྲོ་བ་དང་བྲལ་བའོ། །

[Block 395]
ཡིན་པ་དང་མ་ཡིན་པར་གྱུར་པ་ཡང་ཞེས་བྱ་བ་ནི་འགྲོ་བ་པོ་གང་འགྲོ་བ་དང་ལྡན་པ་ཡང་ཡིན་ལ་འགྲོ་བ་དང་བྲལ་བ་ཡང་ཡིན་པའོ། །

[Block 396]
འགྲོ་ཞེས་བྱ་བ་ནི་བགྲོད་པར་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 397]
རྣམ་གསུམ་དུ་ཞེས་བྱ་བ་ནི་སོང་བ་དང་མ་སོང་བ་དང་བགོམ་བར་རོ། །

[Block 398]
དེའི་ཕྱིར་དེ་ལྟར་ཡང་དག་པའི་རྗེས་སུ་འབྲང་བའི་བློས་ཡོངས་སུ་བརྟགས་ན། འགྲོ་བ་པོ་ཡིན་པར་གྱུར་པ༌[^272]ནི་བགྲོད་པར་བྱ་བ་རྣམ་པ་གསུམ་དུ་འགྲོ་བར་མི་བྱེད་ལ། འགྲོ་བ་པོ་མ་ཡིན་པར་གྱུར་པ་ཡང་བགྲོད་པར་བྱ་བ་རྣམ་པ་གསུམ་དུ་འགྲོ་བར་མི་བྱེད་ཅིང་། འགྲོ་བ་པོ་ཡིན་པ་དང་མ་ཡིན་པར་གྱུར་པ་ཡང་བགྲོད་པར་བྱ་བ་རྣམ་པ་གསུམ་དུ་འགྲོ་བར་མི་བྱེད་པ་དེའི་ཕྱིར་འགྲོ་བ་དང་འགྲོ་བ་པོ་དང་བགྲོད་པར་བྱ་བ་མེད་དོ། །

[Block 399]
བྱ་བ་རྣམས་ཀྱི་ནང་ན་འགྲོ་བའི་བྱ་བ་གཙོ་བོ་ཡིན་པས། འགྲོ་བའི་བྱ་བ་ཡོངས་སུ་བརྟགས་ཏེ། ཇི་ལྟར་འགྲོ་བ་མི་འཐད་པར་རབ་ཏུ་སྒྲུབ་པ༌[^273]དེ་བཞིན་དུ་བྱ་བ་ཐམས་ཅད་ཀྱང་མི་འཐད་པར་གྲུབ་པོ། །སོང་བ་དང་མ་སོང་བ་དང་བགོམ་པ་བརྟག་པ་ཞེས་བྱ་བ་སྟེ་རབ་ཏུ་བྱེད་པ་གཉིས་པའོ།། །།

[Block 400 [HEADING]]
## སྐྱེ་མཆེད་བརྟག་པ། ^3-0

[Block 401]
དབུ་མ་རྩ་བའི་འགྲེལ་པ་བུད་དྷ་པཱ་ལི་ཏ། བམ་པོ་གཉིས་པ། འདིར་སྨྲས་པ། ཁྱེད་ཀྱིས་འགྲོ་བ་མི་འཐད་པ་དེ་རྗེས་སུ་རབ་ཏུ་བསྟན་པས་ཁོ་བོའི་ཡིད་སྟོང་པ་ཉིད་ཉན་པ་ལ་སྤྲོ་བར་བྱས་ཀྱིས། དེའི་ཕྱིར་ད་ནི་རང་གི་གཞུང་ལུགས་ལ་བརྟེན་པ་ཆུང་ཞིག་རྗེས་སུ་རབ་ཏུ་བསྟན་པའི་རིགས་སོ། །

[Block 402]
བཤད་པ། དེ་ལྟར་བྱའོ། །

[Block 403]
སྨྲས་པ།

[Block 404 [VERSE]]
ལྟ་དང་ཉན་དང་སྣོམ་པ་དང་། །
མྱོང་བར༌[^274]བྱེད་དང་རེག་བྱེད་ཡིད། །
དབང་པོ་དྲུག་པོ་དེ་དག་གི། །
སྤྱོད་ཡུལ་བལྟ་བར་བྱ་ལ་སོགས། །

[Block 405]
ལྟ་བ་ལ་སོགས་པ་དེ་དག་ནི་དབང་པོ་དྲུག་ཏུ་བསྟན་ལ། དེ་དག་གི་སྤྱོད་ཡུལ་ནི་གཟུགས་ལ་སོགས་པ་དྲུག་པོ་དག་ཉིད་ཡིན་པར་བསྟན་ཏོ། །

[Block 406]
དེ་ལ་གཟུགས་ལ་ལྟ་བར་བྱེད་པས་ལྟ་བར་བསྟན་ལ། ལྷག་མ་རྣམས་ཀྱང་རང་རང་གི་ཡུལ་འཛིན་པར་བྱེད་པས་བསྟན་ཏོ། །

[Block 407]
དངོས་པོ་མེད་ན་གཟུགས་ལ་ལྟ་བར་བྱེད་པས་ལྟ་བ་ཞེས་བརྗོད་པར་མི་འཐད་དོ། །

[Block 408]
འདི་ལྟར་མེད་པས་ཇི་ལྟར་ལྟ་བར་འགྱུར། ཅི་སྟེ་ལྟ་ན་ནི་རི་བོང་གི་རྭས་ཀྱང་རུས་སྦལ་གྱི་སྤུ་སོགས་པར་འགྱུར་བ་ཞིག་ན་དེ་ནི་མི་འཐད་པས་དེའི་ཕྱིར་སྐྱེ་མཆེད་རྣམས་ཡོད་དོ། །

[Block 409]
བཤད་པ། གལ་ཏེ་གཟུགས་ལ་ལྟ་བར་བྱེད་པས་ལྟའོ་ཞེས་བྱ་བ་དེ་འཐད་ན་ནི། སྐྱེ་མཆེད་རྣམས་ཡོད་པ༌[^275]འགྱུར་བ་ཞིག་ན་དེ་ནི༌[^276]འཐད་དོ། །ཅིའི་ཕྱིར་ཞེ་ན། འདི་ལྟར།

[Block 410 [VERSE]]
ལྟ་དེ༌[^277]རང་གི་བདག་ཉིད་ན། །
དེ་ནི་དེ་ལ་མི་ལྟ་ཉིད། །
གང་ཞིག་བདག་ལ་མི་ལྟ་བ། །
དེ་གཞན་དག་ལ་ཇི་ལྟར་ལྟ། །

[Block 411]
འདི་ལ་དངོས་པོ་རྣམས་ཀྱི་ངོ་བོ་ཉིད་ནི་རང་གི་བདག་ཉིད་ལ་མཐོང་ན་དེ་དང་ལྡན་པས་གཞན་གྱི་བདག་ཉིད་ལ་ཡང་དམིགས་པར་འགྱུར་ཏེ། དཔེར་ན་ཆུ་ལ་རླན་མཐོང་ན་དེ་དང་ལྡན་པས། ས་ལ་ཡང་དམིགས་པ་དང་། མེ་ལ་ཚ་བ་མཐོང་ན་དེ་དང་ལྡན་པས་ཆུ་ལ་ཡང་དམིགས་པ་དང་། སྣ་མའི་མེ་ཏོག་ལ་དྲི་ཞིམ་པ་ཉིད་མཐོང་ན་དེ་དང་ལྡན་པས་གོས་ལ་ཡང་དམིགས་པ་ལྟ་བུ་ཡིན་ན་དངོས་པོ་གང་རང་གི་བདག་ཉིད་ལ་མི་སྣང་བ་དེ་གཞན་གྱི་བདག་ཉིད་ལ་ཇི་ལྟར་དམིགས་པར་འགྱུར་ཏེ། འདི་ལྟར་སྣ་མའི་མེ་ཏོག་ལ་དྲི་ང་བ་ཉིད་མ་མཐོང་ན་གོས་ལ་ཡང་དམིགས་པར་མི་འགྱུར་བ་ལྟ་བུའོ། །

[Block 412]
དེའི་ཕྱིར་གལ་ཏེ་ལྟ་བ་རང་གི་བདག་ཉིད་ལ་ལྟ་བར་བྱེད་ན་ནི་དེས་ན་གཟུགས་ལ་ལྟ་བར་བྱེད་པས་ལྟ་བའོ་ཞེས་བྱ་བ་དེ་འཐད་པར་འགྱུར་བ་ཞིག་ན་ལྟ་བ་ནི་རང་གི་བདག་ཉིད་ལ་ལྟ་བར་མི་བྱེད་དོ། །

[Block 413]
དེ་གང་རང་གི་བདག་ཉིད་ལ་ལྟ་བར་མི་བྱེད་པ་དེ་གཞན་དག་ལ་ཇི་ལྟར་ལྟ་བར་བྱེད་དེ། དེས་ན་གཟུགས་ལ་ལྟ་བར་བྱེད་པས་ལྟ་བའོ། །ཞེས་བྱ་བ་དེ་མི་འཐད་དོ། །

[Block 414 [VERSE]]
སློབ་དཔོན་འཕགས་པ་ལྷས་ཀྱང་། །
དངོས་པོ་ཀུན་གྱི་རང་བཞིན་ནི། །
ཐོག་མར་བདག་ལ་སྣང་གྱུར་ན། །
མིག་ཉིད་ལ་ཡང་མིག་གིས་ནི། །

[Block 415]
ཅི་ཡི་ཕྱིར་ན་འཛིན་མི་འགྱུར། །ཞེས་གསུངས་སོ། །

[Block 416]
སྨྲས་པ། མེ་བཞིན་དུ་ལྟ་བ་ལ་སོགས་པ་འགྲུབ་སྟེ། དཔེར་ན་མེ་ནི་སྲེག་པར་བྱེད་པ་ཡིན་ཡང་གཞན་དག་སྲེག་པར་བྱེད་པ་ཡིན་གྱི། རང་གི་བདག་ཉིད་སྲེག་པར་བྱེད་པ་ནི་མ་ཡིན་ནོ། །

[Block 417]
དེ་བཞིན་དུ་ལྟ་བ་ཡང་ལྟ་བར་བྱེད་པ་ཡིན་ཡང་གཞན་དག་ལ་ལྟ་བར་བྱེད་པ་ཉིད་ཡིན་གྱི་རང་གི་བདག་ཉིད་ལ་ལྟ་བར་བྱེད་པ་ནི་མ་ཡིན་ནོ། །

[Block 418]
བཤད་པ།

[Block 419 [VERSE]]
ལྟ་བ་རབ་ཏུ་བསྒྲུབ་པའི༌[^278]ཕྱིར། །
མེ་ཡི་དཔེ༌[^279]ནི་ནུས་མ་ཡིན། །

[Block 420]
ནུས་མ་ཡིན་ཞེས་བྱ་བ་ནི་མི་ཆོག་པ་དང་། མི་ནུས་སོ་ཞེས་བྱ་བའི་ཐ་ཚིག་སྟེ། ཁྱོད་ཀྱིས་ལྟ་བ་རབ་ཏུ་བསྒྲུབ་པའི་ཕྱིར་མེའི་དཔེ་བྱས་པ་གང་ཡིན་པ་དེས་ནི་ལྟ་བ་རབ་ཏུ་བསྒྲུབ་པར་མི་ནུས་སོ། །ཅིའི་ཕྱིར་ཞེ་ན། འདི་ལ་བུད་ཤིང་བསྲེག་གོ་ཞེས་བྱ་མོད་ཀྱི། བུད་ཤིང་ལས་མེ་གུད་ན་མེད་པའི་ཕྱིར་ཏེ། དེ་བས་ན་མེ་ནི་རང་གི་བདག་ཉིད་སྲེག་པར་བྱེད་པ་ཉིད་ཡིན་གྱི་གཞན་དག་སྲེག་པར་བྱེད་པ་ནི་མ་ཡིན་ནོ། །

[Block 421]
ཅི་སྟེ་གཞན་པ་ཉིད་མ་ཡིན་དུ་ཟིན་ཀྱང་བུད་ཤིང་ནི་བསྲེག་པར༌[^280]བྱ་བའོ། །

[Block 422]
མེ་ནི་སྲེག་པར་བྱེད་པའོ་ཞེས་རྟོག་ན། ཁོ་བོས་ཀྱང་བུད་ཤིང་ནི་སྲེག་པར་བྱེད་པའོ། །

[Block 423]
མེ་ནི་བསྲེག་པར་བྱ་བའོ། །ཞེས་སྨྲ་ལ་རག་གོ། །

[Block 424]
ཡང་ན་ཁྱད་པར་གྱི་གཏན་ཚིགས་བསྟན་པ་བརྗོད་དགོས་སོ། །

[Block 425]
སློབ་དཔོན་འཕགས་པ་ལྷས་ཀྱང་།
--- END BLOCKS ---
