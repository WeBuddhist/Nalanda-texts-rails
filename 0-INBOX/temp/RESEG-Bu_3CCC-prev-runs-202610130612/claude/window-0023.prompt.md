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
[Block 806]
ཡང་ན་དེའི་གང་ཅུང་ཟད་ནི་སྐྱེ་བ་མེད་པ་ཁོ་ནར་སྐྱེས་ལ་ཅུང་ཟད་ནི་སྐྱེ་བས་སྐྱེད་པར་བྱེད་པ་ལ་ཁྱད་པར་ཅི་ཡོད་པ་བརྗོད་དགོས་སོ། །

[Block 807]
ཅི་སྟེ་དེའི་གང་ཅུང་ཟད་སྐྱེས་པ་དེ་ཡང་སྐྱེ་བ་ཁོ་ནས་བསྐྱེད་ན་ནི་དེ་ལྟ་ན་མ་སྐྱེས་པ་སྐྱེ་བས་སྐྱེད་པར༌[^480]བྱེད་ཀྱི། སྐྱེ་བཞིན་པ་སྐྱེད་པར་བྱེད་པ་མ་ཡིན་ནོ། །

[Block 808]
ཡང་གཞན་ཡང་། དེའི་གང་ཅུང་ཟད་སྐྱེས་པ་དེ་ནི་སྐྱེ་བས་སྐྱེད་པར་མི་བྱེད་དེ། སྐྱེས་ཟིན་པའི་ཕྱིར་རོ། །

[Block 809]
དེས་ན་དེའི་ལྷག་མ་མ་སྐྱེས་པ་གང་ཞིག་ཡིན་པ་དེ་སྐྱེ་བས་སྐྱེད་པར་བྱེད་དོ། །ཞེས་བྱ་བར་འགྱུར་ཏེ། དེ་ལ་སྐྱེ་བཞིན་པ་སྐྱེད་པར་བྱེད་དོ་ཞེས་གང༌[^481]སྨྲས་པ་དེ་ཉམས་པར་གྱུར་ཏོ། །

[Block 810]
ཅི་སྟེ་དེའི༌[^482]ཅུང་ཟད་སྐྱེས་པ་དེ་ཡང༌[^483]སྐྱེད་པར་བྱེད་ན་ནི་དེ་ལ་སྐྱེ་བ་གཉིས་ཀྱིས་བྱས་པའི་ཁྱད་པར་ཅན་དུ་འགྱུར་བ་ཞིག་ན་མི་འགྱུར་ཏེ། སྐྱེས་ཟིན་པ་དེ་ལ་ནི་ཡང་སྐྱེད་པའི༌[^484]ཕྱིར་བྱ་བ་འགའ་ཡང་རྩོམ་པར་མི་བྱེད་པས་དེའི་ཕྱིར་དེ་ནི་ཡང་སྐྱེད་པར་མི་བྱེད་དོ། །

[Block 811]
དེ་ལྟ་བས་ན་སྐྱེ་བཞིན་པ་སྐྱེད་པར་བྱེད་དོ། །ཞེས་བྱ་བ་དེ་ནི་སྙིང་པོ་མེད་པ་ལ་བློས་སྙིང་པོར་བཟུང་བར་ཟད་དེ་གྱི་ནའོ། །

[Block 812]
སྨྲས་པ། བུམ་པ་ལ་སོགས་པ་སྐྱེ་བ༌[^485]དག་ཀྱང་དམིགས་ཤིང་། བུམ་པ་ལ་སོགས་པའི་དོན་དུ་བྱ་བ་དག་ལ་འཇུག་པ་ཡང་སྣང་བས་དེའི་ཕྱིར་སྐྱེ་བ་ཡོད་ན་སྐྱེ་བ་ལ་བརྟེན་ཅིང་སྐྱེ་བ་ལ་ལྟོས་ནས་སྐྱེ་བཞིན་པ་སྐྱེད༌[^486]དོ་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 813]
བཤད་པ།

[Block 814 [VERSE]]
གང་ཚེ་སྐྱེ་བ་ཡོད་པས་ནི། །
སྐྱེ་བཞིན་འདི་འབྱུང་མེད་པའི་ཚེ། །
ཇི་ལྟར་སྐྱེ་ལ་བརྟེན་ནས་ནི། །
སྐྱེ་བཞིན་ཞེས་ནི་བརྗོད་པར་བྱ། །

[Block 815]
གང་གི་ཚེ་སྐྱེ་བ་འདི་ཡོད་པས་སྐྱེ༌[^487]བཞིན་པ་འདི་འབྱུང་ངོ་ཞེས་བྱ་བ་དེ་མེད་ཅིང་མི་སྲིད་པ་དེའི་ཚེ་ཇི་ལྟར་སྐྱེ་བ་ལ་བརྟེན་ནས་སྐྱེ་བཞིན་པ་སྐྱེད༌[^488]དོ། །ཞེས་བརྗོད་པར་བྱ། སྨྲས་པ། ཇི་ལྟར་མི་སྲིད་པ། བཤད་པ། རེ་ཞིག་སྣམ་བུ་སྐྱེ་བ་ལ་བརྟེན་ནས་ཅི་ཞིག་སྐྱེ་བཞིན་པ་ཡིན།

[Block 816]
སྨྲས་པ། སྣམ་བུ་ཉིད་སྐྱེ་བཞིན་པ་ཡིན་ནོ། །

[Block 817]
བཤད་པ། གལ་ཏེ་སྣམ་བུ་སྐྱེ་བཞིན་པའི་གནས་སྐབས་ཉིད་ན་སྣམ་བུ་ཡིན་ན། དེ་ལ་སྐྱེ་བ་ལ་བརྟེན་ནས་སྐྱེ་བཞིན་པ་སྐྱེད༌[^489]དོ་ཞེས་གང་བརྗོད་པའི་སྐྱེ་བས་ཡང་ཅི་བྱ། དེ་ནི་མི་འཐད་དེ། སྐྱེས་པ་དང་སྐྱེ་བཞིན་པ་གཉིས་ལ་ཁྱད་པར་མེད་པའི་ཕྱིར་རོ། །

[Block 818]
དེའི་ཕྱིར་སྐྱེ་བཞིན་པ་སྣམ་བུ་མ་ཡིན་ནོ། །

[Block 819]
སྨྲས་པ། རེ་ཞིག་སྐྱེས་པ་ནི་སྣམ་བུ་ཡིན་ཏེ། སྐྱེས་པ་དེ་ལ་བརྟེན་ནས་ཇི་སྲིད་དུ་བརྟག་པའི༌[^490]བྱ་བ་མ་ཟིན་པ་དེ་སྲིད་དུ་སྐྱེ་བཞིན་པ་ཡིན་ནོ། །

[Block 820]
བཤད་པ། དྲང་ངོ་། །གང་སྐྱེ་བཞིན་པ་ན་སྣམ་བུ་མ་ཡིན་པ་དེ་སྐྱེས་ན་ཇི་ལྟར་སྣམ་བུར་འགྱུར། འདི་ལྟར་གཞན་བྱེད་བཞིན་པ་ན་གཞན་དུ་མི་འགྱུར་རོ། །

[Block 821]
ཅི་སྟེ་འགྱུར་ན་ནི་རེ་ལྡེ་བྱེད་བཞིན་པ་ན་སྣམ་བུར་འགྱུར་བ་ཞིག་ན་མི་འགྱུར་བས་དེའི་ཕྱིར་སྐྱེས་པ་ཡང་སྣམ་བུ་མ་ཡིན་ནོ། །

[Block 822]
སྣམ་བུ༌[^491]མེད་ན་གང་གི་སྐྱེ་བ་ལ་བརྟེན་ནས་ཅི་ཞིག་སྐྱེ་བཞིན་པར་འགྱུར།

[Block 823]
སྨྲས་པ། ཅི་ཁྱོད་མཚོན་ཐབས་ལ་མཁས་ཞེས་ཏེ་མ་ཉིད་ལ་འདེབས་པར་བྱེད་དམ། ཁྱོད་འགྱེད་པ་ལ་ཆགས་པས་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་རིགས་པ་ཉིད་སུན་འབྱིན་ཀོ། །བཤད་པ། དེ་ནི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་རིགས་པ་མ་ཡིན་ཏེ། རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་སྨྲ་བ་རྣམས་ལ་ནི་དངོས་པོ་སྐྱེ་བཞིན་པ་ཡང་ཡོད་པ་མ་ཡིན་ལ། དངོས་པོ་སྐྱེ་བཞིན་པའི་སྐྱེ་བ་ཡང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 824]
རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་དོན་ནི་འདི་ཡིན་ཏེ།

[Block 825 [VERSE]]
རྟེན་ཅིང་འབྱུང་བ་གང་ཡིན་པ། །
དེ་ནི༌[^492]ངོ་བོ་ཉིད་ཀྱིས་ཞི། །

[Block 826]
རྟེན་ཅིང་ཞེས་བྱ་བ་གང་ཡིན་པ་དང་། འབྱུང་བ་ཞེས་བྱ་བ་གང་ཡིན་པ་དང་། [^493]གཉི་ག་ངོ་བོ་ཉིད་ཀྱིས་ཞི་བ་ངོ་བོ་ཉིད་དང་བྲལ་བ་ངོ་བོ་ཉིད༌[^494]སྟོང་པ་ཡིན་ནོ། །

[Block 827 [VERSE]]
དེ་ཕྱིར་སྐྱེ་བཞིན་ཉིད་དང་ནི། །
སྐྱེ་བ་ཡང་ནི་ཞི་བ་ཉིད། །

[Block 828]
དེ་ལྟར་གང་གི་ཕྱིར་རྟེན་ཅིང་ཞེས་བྱ་བ་གང་ཡིན་པ་དང་འབྱུང་བ་ཞེས་བྱ་བ་གང་ཡིན་པ་དེ་དང་དེ་གཉི་ག་ངོ་བོ་ཉིད་ཀྱིས་ཞི་བ་ངོ་བོ་ཉིད་དང་བྲལ་བ་ངོ་བོ་ཉིད་སྟོང་པ། དེའི་ཕྱིར་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་སྨྲ་བ་རྣམས་ལ་སྐྱེ་བཞིན་པ་དང་སྐྱེ་བ་གཉི་ག་ཡང་ངོ་བོ་ཉིད་ཀྱིས་ཞི་བ་ངོ་བོ་ཉིད་ཀྱིས་བྲལ་བ་ངོ་བོ་ཉིད༌[^495]སྟོང་པ་ཡིན་ནོ། །

[Block 829]
དེ་གཉི་ག་ངོ་བོ་ཉིད་སྟོང་པ་ཡིན་པ་སྐྱེ་བ་འདི་ལ་བརྟེན་ནས་སྐྱེ་བཞིན་པ་འདི་སྐྱེད༌[^496]དོ། །ཞེས་བྱ་བ་དེ་ཇི་ལྟ་བུར་སྲིད་པར་འགྱུར།

[Block 830]
སྨྲས་པ། རྒྱུ་དང་རྐྱེན་རྣམས་ལ་བརྟེན་ནས་ཇི་སྲིད་ན་སྐྱེས་པར་འགྱུར་བ་དེ་སྲིད་དུ་དངོས་པོ་སྐྱེད་པའི་ཕྱིར་བྱ་བ་རྩོམ་སྟེ། དེས་ན་དངོས་པོ་གང་ཁོ་ན་སྐྱེ་བ་དེ་ཉིད་ལ་བརྟེན་ནས་བྱ་བ་རྩོམ་པར་ཡང་མི་བྱེད་ལ། གཞི་མེད་པར་ཡང་བྱ་བ་རྩོམ་པར་མི་བྱེད་པས་བྱ་བ་དང་ལྡན་པའི་རྒྱུ་དང་རྐྱེན་དེ་དག་ལ་བརྟེན་ནས་དངོས་པོ་སྐྱེ་ཞིང་དེའི་སྐྱེ་བ་དེ་ལ་བརྟེན་ནས་སྐྱེ་བར་འགྱུར་རོ། །

[Block 831]
བཤད་པ། གང་གི་རྒྱུ་དང་རྐྱེན་དག་ལ་བརྟེན་ནས་བྱ་བ་རྩོམ་པར་བྱེད།

[Block 832]
སྨྲས་པ། སྣམ་བུའོ།[^497] །བཤད་པ། ཅི་ཁྱོད་ནམ་མཁའི་མེ་ཏོག་སོགས་པར་བྱེད་དམ། ཁྱོད་སྣམ་བུ་མེད་པའི་རྒྱུ་དང་རྐྱེན་དག་ལ་བརྟེན་ནས་བྱ་བ་རྩོམ་པར་བྱེད་ཀོ། །

[Block 833 [VERSE]]
གལ་ཏེ་དངོས་པོ་མ་སྐྱེས་པ། །
འགའ་ཞིག་གང་ན་ཡོད་གྱུར་ན། །
དེ་ནི་ཅི་ཕྱིར་དེར་སྐྱེ་འགྱུར། །
ཡོད་ན་སྐྱེ་བར་མི་འགྱུར་རོ། །

[Block 834]
གལ་ཏེ་སྐྱེ་བའི་སྔ་རོལ༌[^498]ན་དངོས་པོ་མ་སྐྱེས་པ་འགའ་ཞིག་ག་ཤེད་ན་ཡོད་པར་འགྱུར་བ་དེ་ལྟ་བུ་སྲིད་ན་ནི་དེས་ན་དངོས་པོ་ཡོད་པ་དེའི་རྒྱུ་དང་རྐྱེན་དང་དེ་ལ་བརྟེན་པའི་བྱ་བ་དག་ཀྱང་ཐ་སྙད་གདགས་སུ་རུང་གྲང་ན། གང་གི་ཚེ་དངོས་པོ་མ་སྐྱེས་པ་ཇི་ལྟར་ཡང་མི་འཐད་པ་དེའི་ཚེ་དངོས་པོ་སྐྱེ་བ་དང་བྲལ་བ་དེ་ཡོད་པ་དེ༌[^499]མ་ཡིན་ན་གང་གི་རྒྱུ་དང་རྐྱེན་དུ་འགྱུར། རྒྱུ་དང་རྐྱེན་གང་ཞིག་ལ་བརྟེན་ནས་བྱ་བ་རྩོམ་པར་བྱེད་ཅིང་གང་ཞིག་སྐྱེད་པར༌[^500]བྱེད། གང་རྩོམ་པར་མི་བྱེད་སྐྱེ་བར༌[^501]མི་བྱེད་པ་དེ་ལ་སྐྱེ་བ་ག་ལ་ཡོད། གང་ལ་སྐྱེ་བ་མེད་པ༌[^502]ཇི་ལྟར་སྐྱེ་བ་ལ་བརྟེན་ནས་སྐྱེ་བར་འགྱུར། དེ་ལྟ་བས་ན་རྟེན༌[^503]ཅིང་འབྲེལ་པར་འབྱུང་བ་སྨྲ་བ་རྣམས་ཀྱི་ལྟ་བ་ནི་སྐྱེ་བཞིན་པ་དང་སྐྱེ་བ་ཞི་བ་ཡིན་ནོ། །

[Block 835]
ཡང་གཞན་ཡང་།

[Block 836 [VERSE]]
གལ་ཏེ་སྐྱེ་བ་དེ་ཡིས་ནི། །
སྐྱེ་བཞིན་པ་ནི་སྐྱེད་བྱེད་ན། །
སྐྱེ་བ་དེ་ནི་སྐྱེད་བྱེད་པ། །
སྐྱེ་བ་ཡང་ནི་གང་ཞིག་ཡིན། །

[Block 837]
གལ་ཏེ་སྐྱེ་བ་དེས་སྐྱེ་བཞིན་པ་གཞན་པ༌[^504]སྐྱེད་པར་བྱེད་ན། འོ་ན་ད་སྐྱེ་བ་དེ་སྐྱེད་པར་བྱེད་པའི་སྐྱེ་བ་ཡང་གང་ཞིག་ཡིན། དེ་ལ། འདི་སྙམ་དུ་དེ་ནི་སྐྱེ་བ་གཞན་ཞིག་གིས་སྐྱེད་པར༌[^505]སེམས་ན། དེ་ལ་བཤད་པར་བྱ་སྟེ།

[Block 838 [VERSE]]
གལ་ཏེ་སྐྱེ་བ་གཞན་ཞིག་གིས། །
དེ་སྐྱེད༌[^506]ཐུག་པ་མེད་པར་འགྱུར། །

[Block 839]
གལ་ཏེ་སྐྱེ་བ་གཞན་ཞིག་གིས་སྐྱེ་བཞིན་པ་གཞན་སྐྱེད་པར་བྱེད་ན་དེ་ལྟ་ན་ཐུག་པ་མེད་པར་ཐལ་བར་འགྱུར་ཏེ། དེ་ཡང་གཞན་གྱིས་སྐྱེད༌[^507]ཅིང་དེ་ཡང་གཞན་གྱིས་སྐྱེད༌[^508]དེ་མཐའ་མེད་པར་འགྱུར་བས་དེ་ནི་མི་འདོད་དོ། །

[Block 840]
ཅི་སྟེ་གཞན་སྐྱེད་པ༌[^509]ནི་སྐྱེ་བ༌[^510]མེད་པ་ཁོ་ནར་སྐྱེས་སོ་སྙམ་ན། དེ་ལ་བཤད་པར་བྱ་སྟེ།

[Block 841 [VERSE]]
ཅི་སྟེ་སྐྱེ་བ་མེད་སྐྱེ་ན། །
ཐམས་ཅད་དེ་བཞིན་སྐྱེ་བར་འགྱུར། །

[Block 842]
ཇི་ལྟར་གཞན་སྐྱེད་པར་བྱེད་པ་དེ་སྐྱེད་པ༌[^511]གཞན་མེད་པར་སྐྱེས་ན་ནི་ཐམས་ཅད་ཀྱང་དེ་བཞིན་དུ་སྐྱེ་བ་གཞན་མེད་པར་སྐྱེ་བར་འགྱུར་ཏེ། སྐྱེས་པས་གཞན་སྐྱེད་པར་བྱེད་དོ། །ཞེས་བྱ་བ་དོན་མེད་པའི་རྟོག་པ་མེད་པ༌[^512]འདིས་ཅི་བྱ། ཡང་ན་འདི་ལྟར་སྐྱེ་བ་ཉིད་ནི་སྐྱེད་པ༌[^513]གཞན་མེད་པར་སྐྱེ་ལ་དངོས་པོ་གཞན་དག་ནི་སྐྱེད་པ༌[^514]གཞན་མེད་པར་མི་སྐྱེའོ། །ཞེས་ཁྱད་པར་གྱི་གཏན་ཚིགས་བསྟན་པར་བྱ་དགོས་ན་དེ་ཡང་མི་བྱེད་པས༌[^515]དེའི་སྐྱེ་བས་སྐྱེ་བཞིན་པ་གཞན་སྐྱེད༌[^516]དོ། །ཞེས་བྱ་བ་དེ་གྱི་ནའོ། །

[Block 843]
ཡང་གཞན་ཡང་། འདི་ལ༌[^517]དངོས་པོ་འགའ་ཞིག་སྐྱེ་བར་འགྱུར་ན་དེ་ཡོད་པའམ་མེད་པ་ཞིག་སྐྱེ་བར་འགྱུར་གྲང་ན། དེ་ལ།

[Block 844 [VERSE]]
རེ་ཞིག་ཡོད་དང་མེད་པ་ཡང་། །
སྐྱེ་བར་རིགས་པ་མ་ཡིན་ནོ། །

[Block 845]
རེ་ཞིག་ཡོད་པ་ནི་སྐྱེ་བར༌[^518]རིགས་པ་མ་ཡིན་ཏེ། སྐྱེ་བར་བརྟག་པ་དོན་མེད་པ་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
