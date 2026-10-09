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
[Block 701]
སྨྲས་པ། དེ་ནི་ཉེས་པར་མི་འགྱུར་ཏེ། ཇི་ལྟར་སྤྱིར་འདུས་བྱས་ཀྱི་མཚན་ཉིད་ཡིན་དུ་ཟིན་ཀྱང་ཁྱད་པར་གྱི་མཚན་ཉིད་ལ་ལྟོས་ནས་འདི་ནི་བུམ་པའོ། །

[Block 702]
འདི་ནི་སྣམ་བུའོ། །ཞེས་བྱ་བ་དེ་དག་ཡོད་པ་དེ་བཞིན་དུ་འདིར་ཡང་ཁྱད་པར་གྱི་མཚན་ཉིད་ལ་ལྟོས་ནས་སྐྱེ་བ་དང་གནས་པ་དང་འཇིག་པ་དག་རབ་ཏུ་འགྲུབ་པར་འགྱུར་རོ། །

[Block 703]
ཁྱད་པར་དེ་གང་ཞེ་ན། སྐྱེད་པར་བྱེད་པ་དང་། གནས་པར་བྱེད་པ་དང་། འཇིག་པར་བྱེད་པ་དག་གོ། །

[Block 704]
བཤད་པ། དེ་ནི་མི་འཐད་དོ།[^414] །ཅིའི་ཕྱིར་ཞེ་ན། འདི་ལྟར་བུམ་པ་སྐྱེད་པར་བྱེད་པ་དང་། མངོན་པར་འགྲུབ་པར་བྱེད་པ་གང་ཡིན་པ་དེས་ནི་གཞན་ཅི་ཡང་སྐྱེད་པར་མི་བྱེད་ལ། བུམ་པ་གནས་པར་བྱེད་པས་ཀྱང་གཞན་ཅི་ཡང་གནས་པར་མི་བྱེད་ཅིང་། བུམ་པ་འཇིག་པར་བྱེད་པས་ཀྱང་གཞན་ཅི་ཡང་འཇིག་པར་མི་བྱེད་པའི་ཕྱིར་རོ། །

[Block 705]
སྨྲས་པ། དེ་དག་གིས༌[^415]བུམ་པ་ཉིད་སྐྱེ་བ་དང་གནས་པ་དང་། འཇིག་པར་བྱེད་པས་ཉེས་པ་མེད་དོ། །

[Block 706]
བཤད་པ། འོ་ན་ནི་དེ་དག་བུམ་པའི་མཚན་ཉིད་མ་ཡིན་ཏེ། བྱེད་པ་པོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 707]
འདི་ལྟ་བུ་སྐྱེད་པར་བྱེད་པའི་ཕ་བུའི་མཚན་ཉིད་མ་ཡིན་ལ་གཞི་དང་ཐོ་བ་ཡང་བུམ་པའི་མཚན་ཉིད་མ་ཡིན་པའི་ཕྱིར་ཏེ། དེ་ལྟ་བས་ན་སྐྱེ་བ་ལ་སོགས་པ་དག་འདུས་བྱས་ཡིན་ན་འདུས་བྱས་ཀྱི་མཚན་ཉིད་དུ་མི་འཐད་དོ། །

[Block 708]
ཅི་སྟེ་སྐྱེ་བ་འདུས་མ་བྱས་སུ་ཡོངས་སུ་རྟོག་ན་དེ་ལ་ཡང་བཤད་པར་བྱ་སྟེ། འདི་ལྟར་འདུས་བྱས་མཚན་ཉིད་ཡིན། །འདུས་མ་བྱས་ཡིན་ན་ཇི་ལྟར་འདུས་བྱས་ཀྱི་མཚན་ཉིད་དུ་འགྱུར་ཏེ། འདིས་མཚོན་པར་བྱེད་པས་མཚན་ཉིད་ཡིན་ན་གང་སྐྱེ་བ་དང་གནས་པ་དང་འཇིག་པ་དང་བྲལ་བ༌[^416]དེས་ནི་རང་ཉིད་ལ་ཡང་མཚན་པར༌[^417]མི་བྱེད་དོ། །

[Block 709]
གང་རང་ཉིད་ལ་མཚན་པར༌[^418]མི་བྱེད་པ་དེས་གཞན་ཇི་ལྟར་མཚོན་པར་བྱེད། ཅི་སྟེ་བྱེད་ན་ནི་མྱ་ངན་ལས་འདས་པ་འདུས་མ་བྱས་ཀྱང་འདུས་བྱས་ཀྱི་མཚན་ཉིད་ཡིན་པར་ཐལ་བར་འགྱུར་བས་དེ་ནི་མི་འདོད་དེ། དེ་ལྟ་བས་ན་སྐྱེ་བ་དང་གནས་པ་དང་འཇིག་པ་དག་འདུས་མ་བྱས་ཡིན་ན་ཡང་འདུས་བྱས་ཀྱི་མཚན་ཉིད་དུ་མི་འཐད་དེ།[^419] །མཚན་ཉིད་དུ་བརྟགས༌[^420]ན་ཡང་སྐྱེ་བ་དང་། གནས་པ་དང་། འཇིག་པ་དག་སོ་སོ་བའམ། འདུས་པ་ཞིག་འདུས་བྱས་ཀྱི་མཚན་ཉིད་དུ་འགྱུར་གྲང་ན། དེ་ལ།

[Block 710 [VERSE]]
སྐྱེ་སོགས་གསུམ་པོ་སོ་སོ་ཡིས། །
འདུས་བྱས་མཚན་ཉིད་འདྲ་བར་ནི། །
ནུས་མིན་འདུས་པ་ཡིན་ན་ཡང་། །
གཅིག་ལ་དུས་གཅིག་ཇི་ལྟར་རུང་། །

[Block 711]
སྐྱེ་བ་དང་གནས་པ་དང་། འཇིག་པ་དག་རེ་རེ་ལ་ཡང༌[^421]འདུས་བྱས་ཀྱི་མཚན་ཉིད་བྱ་བར་མི་ནུས་ཏེ། ནུས་མིན་ཞེས་བྱ་བ་ནི་མི་ཆོག་པ་དང་། མི་ནུས་སོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །ཇི་ལྟར་ཞེ་ན། འདི་ལ་རེ་ཞིག་དངོས་པོ་མངོན་པར་མ་གྲུབ་ཅིང་། མེད་པ་ལ་ནི་སྐྱེ་བ་དང་གནས་པ་དང་འཇིག་པ་དག་མི་འཐད་དོ། །

[Block 712]
འདི་ལྟར་སྐྱེ་བ་དང་གནས་པ་དང་འཇིག་པ་དག་ནི་དངོས་པོ་ལ་བརྟེན་པ་ཡིན་ཏེ། བུམ་པའི་སྐྱེ་བ་དང་། བུམ་པའི་གནས་པ་དང་བུམ་པའི་འཇིག་པ་ཞེས་བྱ་བ་ཡིན་ན་བུམ་པ་དེ་མངོན་པར་མ་གྲུབ་ན། སྐྱེ་བ་དང་གནས་པ་དང་འཇིག་པ་དག་གང་གི་མཚན་ཉིད་དུ་འགྱུར། དེ་ནི༌[^422]འཇིག་པ་ཞེས་བྱ་བ་ནི་ཞིག་པ་དང་མེད་པ་སྟེ། དེ་གང་ལ་ཡོད་པ་དེ་ནི་མེད་པ་ཉིད་དོ། །

[Block 713]
དེ་མེད་ན་སྐྱེ་བ་དང་གནས་པ་དང་འཇིག་པ་དག་གང་གི་མཚན་ཉིད་དུ་འགྱུར་ཏེ། དེ་ལྟར་རེ་ཞིག་སྐྱེ་བ་དང་གནས་པ་དང་འཇིག་པ་དག་སོ་སོའམ། འདུས་པ་ཡང་དངོས་པོ་མངོན་པར་མ་གྲུབ་པ་དང་། ཞིག་པའི་མཚན་ཉིད་མ་ཡིན་ནོ། །

[Block 714]
དེ་ལ་འདི་སྙམ་དུ་དེ་དག་དངོས་པོ་མངོན་པར་གྲུབ་པ་དང་མ་ཞིག་པའི་མཚན་ཉིད་ཡིན་པར་སེམས་ན། དེ་ཡང་མི་འཐད་དེ། ཇི་ལྟར་ཞེ་ན། འདི་ལ་བུམ་པ་ཞེས་བྱ་བའི་དངོས་པོ་ཡོད་པ་ལ་ནི་སྐྱེ་བ་མེད་དེ། འདི་ལྟར་ཡོད་པ་ལ་ཡང་སྐྱེ་བའི་བྱ་བ་མེད་དོ། །

[Block 715]
ཅི་སྟེ་ཡོད་ཀྱང་སྐྱེ་བར་གྱུར་ན་ནི་ནམ་ཡང་མི་སྐྱེ་བར་མི་འགྱུར་བས་དེ་ནི་མི་འདོད་དོ། །

[Block 716]
དེ་ལྟ་བས་ན་ཡོད་པ་ལ་སྐྱེ་བ་མེད་དེ། མེད་པ་གང་ཡིན་པ་དེ་ཇི་ལྟར་མཚན་ཉིད་དུ་འགྱུར།

[Block 717]
སྨྲས་པ། རེ་ཞིག་གནས་པ་ནི་ཡོད་དོ། །

[Block 718]
བཤད་པ། གནས་པ་ཡང་མི་འཐད་དེ། ཅིའི་ཕྱིར་ཞེ་ན། འཇིག་པ་དང་རྗེས་སུ་འབྲེལ་པའི་ཕྱིར་རོ། །

[Block 719]
འདི་ལྟར་འདུས་བྱས་ནི་མི་རྟོག་པ་དང་ཁོར་ཟུག་ཏུ་རྗེས་སུ་འབྲེལ་པས་ཁོར་ཟུག་ཏུ་མི་རྟག་ན་ཇི་ལྟར་གནས་པར་འགྱུར་ཏེ། གནས་པ་དང་འཇིག་པ་གཉིས་འགལ་བའི་ཕྱིར་རོ། །

[Block 720]
འདི་ལྟར་འོག་ནས་ཀྱང་།

[Block 721 [VERSE]]
དངོས་པོ་འགག་པར་འགྱུར་ན་ནི། །
གནས་པར་འཐད་པ་མ་ཡིན་ནོ། །
གང་ཡང་འགག་པར་མི་འགྱུར་བ། །
དེ་ནི་དངོས་པོ༌[^423]མི་འཐད་དོ། །

[Block 722]
ཞེས་འབྱུང་ངོ་། །སློབ་དཔོན་འཕགས་པ་ལྷས་ཀྱང་།

[Block 723 [VERSE]]
གནས་མེད་དངོས་པོ་ག་ལ་ཡོད། །
མི་རྟག་པས་ན་གང་ལ༌[^424]གནས། །
གལ་ཏེ་དང་པོ་གནས་གྱུར་ན། །
ཐ་མར་རྙིངས་པར་མི་འགྱུར་རོ། །

[Block 724 [VERSE]]
གལ་ཏེ་ཁོར་ཟུག་མི་རྟག་ཡོད། །
ཁོར་ཟུག་གནས་པར་མི་འགྱུར་རོ། །
ཡང་ན་རྟག་པར་གྱུར་པ་ལས། །
ཕྱིས་ན་མི་རྟག་པར་ཡང་འགྱུར། །

[Block 725 [VERSE]]
གལ་ཏེ་དངོས་པོ་མི་རྟག་དང་། །
ལྷན་ཅིག་གནས་པ་ཡོད་གྱུར་ན། །
མི་རྟག་ལོག་པར་འགྱུར་བའམ། །
ཡང་ན་གནས་པ་བརྫུན་པར་འགྱུར། །

[Block 726]
ཞེས་གསུངས་སོ། །

[Block 727]
དེ་ལྟ་བས་ན་གནས་པ་ཡང་མེད་དེ། མེད་ན༌[^425]གང་ཡིན་པ་ཇི་ལྟར་འདུས་བྱས་ཀྱི་མཚན་ཉིད་དུ་འགྱུར།

[Block 728]
སྨྲས་པ། འོ་ན་འཇིག་པ་ཡོད་དོ། །

[Block 729]
བཤད་པ། གནས་པ་མེད་པར་འཇིག་པ་ག་ལ་ཡོད་དེ། འདི་ལྟར་དངོས་པོ་གནས་པ་ཡོད་ན་འཇིག་པར་འགྱུར་གྱི་གནས་པ་མེད་ན་འཇིག་པར་ག་ལ་འགྱུར། དེ་ཡང་འཇིག་པ་ཞེས་བྱ་བ་ནི་ཞིག་པ་དང་མེད་པ་སྟེ་དེ་གང་ལ་ཡོད་པ་དེ་ནི་མེད་པ་ཉིད་དོ། །

[Block 730]
དེ་མེད་ན་སྐྱེ་བ་དང་གནས་པ་དང་འཇིག་པ་དག་གང་གི་མཚན་ཉིད་དུ་འགྱུར་ཞེས་བསྟན་ཟིན་པས་དེའི་ཕྱིར་འཇིག་པ་ཡང་འདུས་བྱས་ཀྱི་མཚན་ཉིད་དུ་མི་འཐད་དོ། །

[Block 731]
དེའི་ཕྱིར་དེ་ལྟར་སྐྱེ་བ་དང་གནས་པ་དང་། འཇིག་པ་དག་སོ་སོ་བ་ཡང་འདུས་བྱས་མངོན་པར་གྲུབ་པའི་མཚན་ཉིད་དུ་མི་འཐད་དོ། །

[Block 732]
ལྷན་ཅིག་ཏུ་སྐྱེའོ་ཞེས་གསུངས་པའི་ཕྱིར་ཆོས་ཀྱི་གནས་སྐབས་ཤེས་པ་དག་སྐྱེ་བ་དང་གནས་པ་དང་འཇིག་པ་དག་ལྷན་ཅིག་ཏུ་སྐྱེའོ་ཞེས་བརྗོད་པས་དེའི་ཕྱིར་ཡང་སོ་སོ་བ་དག་མཚན་ཉིད་དུ་མི་འཐད་དོ། །

[Block 733]
སྨྲས་པ། འདུས་པ་དག་ནི་མཚན་ཉིད་ཡིན་ནོ། །

[Block 734]
བཤད་པ། འདུས་པ་ཡིན་ན་ཡང་། གཅིག་ལ་དུས་གཅིག་ཇི་ལྟར་རུང་། སོ་སོ་བ་གང་དག་མཚན་ཉིད་མ་ཡིན་པ་དེ་དག་འདུས་པ་ཕན་ཚུན་འགལ་བ་དག་འདུས་བྱས་ཀྱི་དངོས་པོ་གཅིག་ལ་དུས་གཅིག་ཏུ་ཇི་ལྟར་རུང་། འདི་ལྟར་གང་གི་ཚེ་ན་སྐྱེ་བ་དེའི་ཚེ་ན་གནས་པ་དང་འཇིག་པ་མེད་ལ། གང་གི་ཚེ་གནས་པ་དེའི་ཚེ་ན་སྐྱེ་བ་དང་འཇིག་པ་མེད་ཅིང་། གང་གི་ཚེ་འཇིག་པ་དེའི་ཚེ་ན་ཡང་སྐྱེ་བ་དང་གནས་པ་མེད་པ་དེའི་ཕྱིར་སྐྱེ་བ་དང་གནས་པ་དང་འཇིག་པ་སོ་སོ་བ་དང་འདུས་པ་དག་ཀྱང་འདུས་བྱས་ཀྱི་མཚན་ཉིད་དུ་མི་འཐད་དོ། །

[Block 735]
མཚན་ཉིད་མི་འཐད་པའི་ཕྱིར་འདུས་བྱས་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 736]
སྨྲས་པ། ལྟག་ཆོད་དེ་ལྟ་བུ་འབའ་ཞིག་གིས་ཅི་བྱ། ཡོང་ནི་གང་གི༌[^426]སྐྱེ་བ་དང་། གནས་པ་དང་། འཇིག་པ་དེ་འདུས་བྱས་ཡིན་ནོ། །

[Block 737]
བཤད་པ། ཁོ་བོ་ལྟག༌[^427]ཆོད་ཀྱི་ཕྱིར་མི་རྩོམ་གྱིས་ཁོ་བོ་ནི་དེ་ཁོ་ན་ཤེས་པར་བྱ་བའི་ཕྱིར་རྩོམ་མོ། །

[Block 738]
སྐྱེ་བ་ཞེས་བྱ་བ་དེ་གང་ཡིན་པ༌[^428]སྨྲོས་ཤིག །སྨྲས་པ། བུམ་པ་སྐྱེའོ། །

[Block 739]
བཤད་པ། རེ་ཞིག་གནས་སྐབས་གང་ལ་བུམ་པ་ཞེས་བྱ་བར་འགྱུར་བ་ལེགས་པར་སོམས་ལ་སྨྲོས་ཤིག །དེ་ལ་གང་གི་ཚེ་མ་སྐྱེས་པ་ལ་ནི་བུམ་པ་ཞེས་བྱར་ཡང་མི་རུང་སྟེ། སྐྱེས་པ་ཉིད་ལ་བུམ་པ་ཞེས་བྱ་བར་འགྱུར་ཞིང་བུམ་པ་ཡང་འདུས་བྱས་ཡིན་པའི་ཕྱིར་མཚན་ཉིད་གསུམ་དང་ལྡན་པ་ཉིད་ཡིན་པ་དེའི་ཚེ་སྐྱེ་བ་བུམ་པའི་མཚན་ཉིད་ཡིན་ནོ། །ཞེས་བྱ་བ་དེ་ཇི་ལྟར་འཐད། [^429]ཇི་ལྟར་ཡོད་པ་ལ་ཡང་སྐྱེ་བས་ཅི་བྱ། མཚན་ཉིད་དང་ལྡན་པ་ལ་ཡང་མཚན་ཉིད་ཀྱིས་ཅི་བྱ། ཅི་སྟེ་བུམ་པ་མ་ཡིན་པ་སྐྱེ་ཞིང་སྐྱེས་ཟིན་ནས་བུམ་པར་འགྱུར་རོ་སྙམ་ན། དེ་ཡང་རིགས་པ་མ་ཡིན་ཏེ། བུམ་པ་མ་ཡིན་པ་སྐྱེ་ཞིང་ཞེས་བྱ་བ་དེ་རེ་ལྡེའམ། སྣམ་བུའམ། འོན་ཏེ་བུམ་པ་མ་ཡིན་པ་ཞེས་བྱ་བ་ཅི་ཡང་མེད་པ་ཞིག་གམ་ཅི་ཡིན། དེ་ལ་རེ་ཞིག་གལ་ཏེ་རེ་ལྡེའམ། སྣམ་བུ་ཞིག་སྐྱེ་ན་ནི་དེ་སྐྱེས་ཟིན་ནས་ཇི་ལྟར་བུམ་པར་འགྱུར། ཅི་སྟེ་བུམ་པ་མ་ཡིན་པ་ཞེས་བྱ་བ་ཅིའང་མེད་པ་ཞིག་ཡིན་ན་ནི་ཅི་ཡང་མེད་པ་གང་ཡིན་པ་དེ་ཇི་ལྟར་སྐྱེ་ཅི་སྟེ་སྐྱེ་ན་ནི་རི་བོང་གི་རྭ་ཡང་ཅིའི་ཕྱིར་མི་སྐྱེ། དེའི་ཕྱིར་སྐྱེ་བ་ཞེས་བྱ་བ་དེ་མི་འཐད་དོ། །

[Block 740]
སྐྱེ་བ་ཞེས་བྱ་བ་དེ་འདི་ལ་མེད་ན་གང་སྐྱེ་བ་དེ་འདུས་བྱས་ཡིན་ནོ། །ཞེས་བྱ་བ་དེ་ཇི་ལྟར་འཐད་པར་འགྱུར། གང་སྐྱེ་བ་མེད་པ་དེ༌[^430]ཇི་ལྟར་གནས་པ་དང་འཇིག་པར་འགྱུར། དེ་ལྟ༌[^431]ན་སྐྱེ་བ་དང་གནས་པ་དང་འཇིག་པ་ཞེས་བྱ་བ་དག་ནི། འཇིག་རྟེན་གྱི་ཐ་སྙད་ཁོ་ནར་ཟད་དོ། །
--- END BLOCKS ---
