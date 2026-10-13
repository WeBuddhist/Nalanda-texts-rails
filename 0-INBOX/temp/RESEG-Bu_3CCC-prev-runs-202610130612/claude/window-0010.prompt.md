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
[Block 351]
གང་དུ་མ་བསྡད་པ་དེ་ནས་ཀྱང་མི་འགྲོ་སྟེ། འགྲོ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 352]
གང་དུ་བསྡད་པ༌[^244]དེ་ནས་ཀྱང་མི་འགྲོ་སྟེ། སྡོད་པ་དང་འགྲོ་བ་གཉིས་མི་མཐུན་པའི་ཕྱིར་རོ། །

[Block 353]
དེ་ལྟར་ན་འགྲོ་བའི་ལྡོག་པ་དང་། སྡོད་པའི་ལྡོག་པ་མཚུངས་པ་ཡིན་ནོ། །

[Block 354]
འདིར་སྨྲས་པ། འགྲོ་བ་དང་འཇུག་པ་དང་། ལྡོག་པ་སོང་བ་དང་མ་སོང་བ་དང་། བགོམ་པ་ལ་ཡོད་དོ་ཞེའམ་འགྲོ་བ་པོ་དང་། འགྲོ་བ་པོ་མ་ཡིན་པ་དང་། དེ་ལས་གཞན་པ་ལ་ཡོད་དོ་ཞེས་བྱ་བ་དེ་ལ༌[^245]བརྗོད་པར་མི་ནུས་སུ་ཟིན་ཀྱང་། ཙཻ་ཏྲའི་བགོམ་པ༌[^246]འདོར་བ་མཐོང་ནས། ཙཻ་ཏྲའི་འགྲོ་བ་པོ་ཞེས་བྱ་བར་འགྱུར་བས་དེའི་ཕྱིར་འགྲོ་བ་པོ་དང་འགྲོ་བ་ཡོད་དོ། །

[Block 355]
བཤད་པ། རེ་ཞིག་བརྗོད་པར་མི་ནུས་སུ་ཟིན་ཀྱང་ཞེས་བྱ་བ་དེ་ནི་ཕོངས་པའི་ཚིག་ཡིན་ནོ། །

[Block 356]
འོན་ཀྱང་གང༌[^247]མཐོང་ནས་ཙཻ་ཏྲ་འགྲོ་བ་པོ་ཞེས་བྱ་བར་སེམས་པ༌[^248]ཙཻ་ཏྲའི་གོམ་པ་འདོར་བ་གང་ཡིན་པ་འདོར། [^249]གོམ་པ་འདོར་བ་དེ་དང་ཙཻ་ཏྲ་གཅིག་པ་ཉིད་དམ་གཞན་པ་ཉིད་དུ་འགྱུར་གྲང་ན། དེ་ལ།

[Block 357 [VERSE]]
འགྲོ་བ་དེ་དང་འགྲོ་བ་པོ། །
དེ་ཉིད་ཅེས་ཀྱང་བྱར་མི་རུང་། །
འགྲོ་བ་དང་ནི་འགྲོ་བ་པོ། །
གཞན་ཉིད་ཅེས་ཀྱང་བྱར་མི་རུང་། །

[Block 358]
ཇི་ལྟར་ཞེ་ན།

[Block 359 [VERSE]]
གལ་ཏེ་འགྲོ་བ་གང་ཡིན་པ། །
དེ་ཉིད་འགྲོ་པོ་ཡིན་གྱུར་ན། །
བྱེད་པ་པོ་དང་ལས་ཉིད་ཀྱང་། །
གཅིག་པ་ཉིད་དུ་ཐལ་བར་འགྱུར། །

[Block 360]
གལ་ཏེ་འགྲོ་བ་གང་ཡིན་པ་དེ་ཉིད་འགྲོ་བ་པོ་ཡིན་པར་གྱུར་ན། དེ་ལྟ་ན་བྱེད་པ་པོ་དང་བྱ་བ་ཡང་གཅིག་པ་ཉིད་དུ་ཐལ་བར་འགྱུར་རོ། །

[Block 361]
དེ་ནི་མི་འཐད་དོ། །

[Block 362]
[^250]

[Block 363]
བྱེད་པ་པོ་གང་ཡིན་པ་དེ་ཉིད་བྱ་བ་ཡིན་པར་ཇི་ལྟར་འགྱུར། ཅི་སྟེ་སྐྱོན་དེར་གྱུར་ན་མི་རུང་ངོ་། །སྙམ་པས་བྱེད་པ་པོ་དང་བྱ་བ་གཉིས་གཞན་པ་ཉིད་ཡིན་ནོ་ཞེ་ན། དེ་ལ་བཤད་པར་བྱ་སྟེ།

[Block 364 [VERSE]]
གལ་ཏེ་འགྲོ་དང་འགྲོ་བ་པོ། །
གཞན་པ་ཉིད་དུ་རྣམ་བརྟགས༌[^251]ན། །
འགྲོ་པོ་མེད་པའི་འགྲོ་བ་དང་། །
འགྲོ་བ་མེད་པའི་འགྲོ་པོར་འགྱུར། །

[Block 365]
གལ་ཏེ་བྱེད་པ་པོ་དང་། བྱ་བ་གཉིས་གཅིག་པ་ཉིད་ཀྱི་སྐྱོན་མཐོང་བས་འགྲོ་བ་པོ་དང་། འགྲོ་བ་གཞན་པ་ཉིད་དུ་རྣམ་པར་བརྟགས༌[^252]ན། དེ་ལྟ་ན་འགྲོ་བ་པོ་ལས་ཐ་དད་པར་གྱུར་པའི་འགྲོ་བ་གཞི་མེད་པ་རང་ལས་རབ་ཏུ་གྲུབ་པར་འགྱུར་བ་དང་། འགྲོ་བ་གཞི་མེད་པ་རང་ལས་རབ་ཏུ་གྲུབ་པར་གྱུར་ན་འགྲོ་བ་པོ་ཡང་འགྲོ་བ་དང་བྲལ་བ་མི་ལྟོས་པ་རང་ལས་རབ་ཏུ་གྲུབ་པར་འགྱུར་བ་ཞིག་ན། དེ་གཉིས་གང༌[^253]ཡང་མི་འཐད་དེ་འགྲོ་བ་པོ་མེད་པར་འགྲོ་བ་དང་། འགྲོ་བ་མེད་པར་འགྲོ་བ་པོར་ཇི་ལྟར་འགྱུར།

[Block 366]
འདིར་སྨྲས་པ། ཅི་ཁྱེད་གསོད་པ་པོ་ཉིད་ལ་དབང་འཛུགས་སམ། ཁོ་བོ་ནི་བྱེད་པ་པོ་དང་བྱ་བ་གཉིས་ཐ་དད་པར་འགྱུར༌[^254]གྲུབ་པ་མེད་པའི་ཕྱིར། གཞན་པ་ཉིད་དུ་ཡང་མི་འདོད་ལ། བྱེད་པ་པོ་ཐ་དད་པའི་ཕྱིར་གཅིག་པ་ཉིད་དུ་ཡང་མི་འདོད་པས་དེའི་ཕྱིར་དེ་གཉི་ག་མེད་པར་ཡང་དེ་གཉིས་གྲུབ་པོ། །བཤད་པ། ཁོ་བོ་ནི་གསོད་པ་པོ་ཉིད་ལ་དབང་མི་འཛུགས་ཀྱི། ཁྱོད་ཉིད་ལག་པ་བརྐྱང་སྟེ་ཚེགས་ཆེན་པོར་གཡོབ་ཅིང་ཁོང་པ་དབུགས་ཀྱིས་བརྫངས༌[^255]བཞིན་དུ་སྨིག་རྒྱུའི་ཆུ་ལ་རྐྱལ་བར་བྱེད་དམ། ཁྱོད་དེ་ཉིད་དང་གཞན་མ་གཏོགས་པ་མེད་པའི་ཕྱོགས་ལ་ཡོད་པའི་བློས་གནས་པར་བྱེད་ཀོ།[^256] །

[Block 367 [VERSE]]
གང་དག་དངོས་པོ་གཅིག་པ་དང་། །
དངོས་པོ་གཞན་པ་ཉིད་དུ་ནི། །
གྲུབ་པར་གྱུར་པ་ཡོད་མིན་ན།

[Block 368]
[^257] །དེ་གཉིས་གྲུབ་པ་ཇི་ལྟར་ཡོད། །གལ་ཏེ་བྱེད་པ་པོ་དང་བྱ་བ་གཉིས་གཅིག་པ་ཉིད་དང་གཞན་པ་ཉིད་དུ་གྲུབ་པ་མེད༌[^258]དེ་གཉིས་མ་གཏོགས་པར་རྣམ་པ་གཞན་གང་གིས་དེ་གཉིས་གྲུབ་པ་ཡོད་པ་དེ་ཇེ་སྨྲོས་ཤིག །དེ་ལྟ་བས་ན་དེ་ནི་བརྟགས་པ་ཙམ་དུ་ཟད་དོ། །

[Block 369]
འདིར་སྨྲས་པ། འཇིག་རྟེན༌[^259]མངོན་སུམ་གྱི་དོན་འདི་གབ་གབ་ཀྱིས་གནོན༌[^260]པར་ཇི་ལྟར་ནུས། ཡོང་ནི་གང་མེད་པས་འགྲོ་བ་པོ་མ་ཡིན་ནོ། །ཞེས་བྱ་བ་དང་། གང་ལ་ལྟོས་ནས་འདི་འགྲོ་བ་པོ་ཡིན་ནོ་ཞེས་བྱ་བ་དེ་ནི་འགྲོ་བ་ཡིན་ལ། དེ་ཡང་འགྲོ་བ་པོ་ཞེས་བྱའོ། །

[Block 370]
བཤད་པ། ཅི་ཁྱོད་བུ་འདོད་ལ་མ་ནིང་ལ་སྤྱོད་དམ། ཁྱོད་འགྲོ་བ་པོ་མེད་པ་ལ་འགྲོ་བ་པོར་རྟོག་གོ། །

[Block 371]
འདི་ལྟར་བགྲོད་པར་བྱ་བ་ཞིག་ཡོད་ན་ནི་འགྲོ་བ་པོར་བརྟག་ཏུ་ཡང་རུང་གྲང་ན། གང་གི་ཚེ་འགྲོ་བ་པོར་བརྟགས་ཀྱང་བགྲོད་པར་བྱ་བ་མི་འཐད་པ་དེའི་ཚེ་ཅི་ཡང་མི་ཕན་པ་ཡོངས་སུ་བརྟགས་པ་འདིས་ཅི་ཞིག་བྱ། བགྲོད་པར་བྱ་བ་ཇི་ལྟར་མི་འཐད་ཅེ་ན། དེ་ནི་སོང་བ་ཡང་མ་ཡིན་མ་སོང་བ་ཡང་མ་ཡིན་ལ། བགོམ་པ་ནི་ཤེས་པར་མི་འགྱུར་རོ་ཞེས་བསྟན་ཟིན་ཏོ། །

[Block 372]
དེ་དག་ཙམ་དུ་དེ་འགྲོ་བས་འགྲོ་བ་པོ་ཡིན་གྲང་ན། དེ་ནི་མི་འགྲོ་བས་དེའི་ཕྱིར་འགྲོ་བ་པོར་བརྟགས་པ་ནི་དོན་མེད་པ་ཡིན་ནོ། །

[Block 373]
འདིར་སྨྲས་པ། འགྲོ་བ་པོ་ཡིན་པས་འགྲོ་བ་ཉིད་འགྲོ་སྟེ། དཔེར་ན་སྨྲ་པོ༌[^261]དག་ན་རེ་ཚིག་སྨྲའོ། །

[Block 374]
བྱ་བ་བྱེད་དོ་ཞེས་ཟེར་བ་བཞིན་ནོ། །

[Block 375]
བཤད་པ། འགྲོ་བ་པོའི་འགྲོ་བ་ལ་བརྟག་ན་ཡང་འགྲོ་བ་གང་གིས་དེའི༌[^262]འགྲོ་བ་པོར་མངོན་པའི་འགྲོ་བ་དེ་ཉིད་དམ། དེ་ལས་གཞན་པ་ཞིག་འགྲོ་གྲང་ན། གཉི་ག་ཡང་མི་མཐོང་ངོ་།[^263] །ཇི་ལྟར་ཞེ་ན།

[Block 376 [VERSE]]
འགྲོ་བ་གང་གི༌[^264]འགྲོ་པོར་མངོན། །
འགྲོ་བ་དེ་ནི་དེ་འགྲོ་མིན། །

[Block 377]
འགྲོ་བ་གང་དང་ལྡན་ན། ཙཻ་ཏྲ་འགྲོ་བ་པོ་ཞེས་བྱ་བར་མངོན་པའི་འགྲོ་བ་དེ་ནི་འགྲོ་བ་པོ་དེ་འགྲོ་བར་བྱེད་པ་མ་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན།

[Block 378 [VERSE]]
གང་ཕྱིར་འགྲོ་བའི་སྔ་རོལ་མེད། །
གང་ཞིག་གང་དུ་འགྲོ་བར་འགྱུར། །

[Block 379]
གང་གི་ཕྱིར་འགྲོ་བ་གང་གིས་འགྲོ་བ་པོ་ཞེས་བྱ་བར་མངོན་པའི་འགྲོ་བ་འདི༌[^265]སྔ་རོལ་ནི་འགྲོ་བའི་སྔ་རོལ་ཏེ་དེའི་སྔ་རོལ་ན་འགྲོ་བ་པོ་མེད་དོ། །

[Block 380]
དེ་དང་ལྡན་པ་ཁོ་ནའི་ཕྱིར་འགྲོ་བ་པོ་ཞེས་བརྗོད་པ་ཡིན་ཏེ། གང་ཞིག་གང་དུ་དཔེར་ན་གྲོང་དང་གྲོང་ཁྱེར་ལྟ་བུ་ཐ་དད་པར་གྱུར་པས་འགྲོ་བར་འགྱུར་བ་ཡིན་ན་འགྲོ་བ་པོར་གྱུར་ནས་གང་འགྲོ་བར་འགྱུར་བའི་འགྲོ་བ་དེ་ནི་འགྲོ་བ་པོ་ལས་གྲོང་དང་གྲོང་ཁྱེར་ལྟ་བུར་ཐ་དད་པར་གྱུར་པ་མེད་དོ། །

[Block 381]
དེ་ལྟར་རེ་ཞིག་འགྲོ་བ་གང་གིས་འགྲོ་བ་པོ་ཞེས་བྱ་བར་མངོན་པའི་འགྲོ་བ་དེ་ནི་འགྲོ་བ་པོ་འགྲོ་བར་བྱེད་པ་མ་ཡིན་ནོ། །

[Block 382]
དེ་ལ་འདི་སྙམ་དུ་དེ་ལས་གཞན་པ་ཞིག་འགྲོ་བར་སེམས་ན། བཤད་པ།

[Block 383 [VERSE]]
འགྲོ་བ་གང་གིས་འགྲོ་པོར་མངོན། །
དེ་ལས་གཞན་པ་དེ་འགྲོ་མིན། །

[Block 384]
འགྲོ་བ་གང་དང་ལྡན་ན་ཙཻ་ཏྲ་འགྲོ་བ་པོ་ཞེས་བྱ་བར་མངོན་པ་དེ་ལས་གཞན་པའི་འགྲོ་བ་ཡང་འགྲོ་བ་པོ་དེ་འགྲོ་བར་བྱེད་པ་མ་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན།

[Block 385 [VERSE]]
གང་ཕྱིར་འགྲོ་པོ་གཅིག་པུ་ལ། །
འགྲོ་བ་གཉིས་སུ་མི་འཐད་དོ། །

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
--- END BLOCKS ---
