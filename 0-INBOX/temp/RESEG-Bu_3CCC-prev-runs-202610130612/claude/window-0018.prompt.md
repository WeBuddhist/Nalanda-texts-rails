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
[Block 631 [VERSE]]
ཆགས་པ་ལ་ཡང༌[^386]འདོད་ཆགས་ནི། །
ཡོད་དམ་མེད་ཀྱང་རིམ་པ་མཚུངས། །
ཆགས་པ་ཡོད་པར་ཡོངས་བརྟགས༌[^387]ན། །

[Block 632]
འདོད་ཆགས་ཡོད་དམ་མེད་ཀྱང་རུང་སྟེ་ཆགས་པ་ལ་ཡང་འདོད་ཆགས་མི་འཐད་པ་དེ་ཉིད་དང་རིམ་པ་མཚུངས་སོ། །ཇི་ལྟར་ཞེ་ན།

[Block 633 [VERSE]]
གལ་ཏེ་ཆགས་པའི་སྔ་རོལ་ན། །
ཆགས་མེད་འདོད་ཆགས་ཡོད་ན་ནི། །
དེ་ལ་བརྟེན་ནས་ཆགས་པ་ཡོད། །
འདོད་ཆགས་ཡོད་ན་ཆགས་ཡོད་འགྱུར། །

[Block 634]
གལ་ཏེ་ཆགས་པའི་སྔ་རོལ་ན་འདོད་ཆགས་ཆགས་པ་མེད་པ་ཆགས་པ་ལས་གཞན་དུ་འགྱུར་བ་འགའ་ཞིག་ཡོད་ན་ནི། དེ་ལ་བརྟེན་ནས་ཆགས་པ་ཡོད་པར་འགྱུར་རོ། །

[Block 635]
ཅིའི་ཕྱིར་ཞེ་ན། འདོད་ཆགས་ཡོད་ན་ཆགས་ཡོད་འགྱུར། །འདི་ལྟར་འདོད་ཆགས་ཡོད་ན་ཆགས་པ་ཡང་འདིས་འདི་ཆགས་སོ་ཞེས་འཐད་པར་འགྱུར་རོ། །

[Block 636]
འདོད་ཆགས་མེད་ན་གང་གིས་དེ་ཆགས་པར་འགྱུར། མ་ཆགས་པ༌[^388]ན་ནི་ཇི་ལྟར་ཆགས་པར་འགྱུར། ཅི་སྟེ་འགྱུར་ན་ནི་གང་ཡང་ཆགས་པ་མ་ཡིན་པ་ཉིད་དུ་མི་འགྱུར་བས་དེ་ནི་མི་འདོད་དེ། དེའི་ཕྱིར་འདོད་ཆགས་མེད་ན་ཆགས་པ་མི་འཐད་དོ། །

[Block 637]
དེ་ལ་འདི་སྙམ་དུ་འདོད་ཆགས་ཡོད་ན་ཆགས་པ་ཡོད་པར་སེམས་ན། བཤད་པ།

[Block 638 [VERSE]]
འདོད་ཆགས་ཡོད་པར་གྱུར་ན་ཡང་། །
ཆགས་པ་ཡོད་པར་ག་ལ་འགྱུར། །

[Block 639]
ཁྱོད་ཀྱི་འདོད་ཆགས་ཡོད་པར་གྱུར༌[^389]ན་ཡང༌[^390]ཆགས་པ་མེད་པ༌[^391]ཉིད་དུ་ག་ལ་འགྱུར་ཏེ། འདི་ལྟར་གལ་ཏེ་འདོད་ཆགས་ཡོད་ན་ཆགས་པར་འགྱུར་ན། ཆགས་པ་མེད༌[^392]དེ་འདོད་ཆགས་དེས་ཆགས་པར་གྱུར་པ་མ་ཡིན་ནོ། །

[Block 640]
ཆགས་པ་མ་ཡིན་ན་ནི་ཇི་ལྟར་ཆགས་པར་འགྱུར། ཅི་སྟེ་འགྱུར་ན་ནི་ནམ་ཡང་ཆགས་པ་མ་ཡིན་པ་ཉིད་དུ་མི་འགྱུར་བས་དེ་ནི་མི་འདོད་དེ།

[Block 641 [VERSE]]
འདོད་ཆགས་ལ་ཡང་ཆགས་པ་ནི། །
ཡོད་དམ་མེད་ཀྱང་རིམ་པ་མཚུངས། །

[Block 642]
དེའི་ཕྱིར་འདོད་ཆགས་ཡོད་པར་གྱུར་ན་ཡང་ཆགས་པ་མི་འཐད་དོ། །

[Block 643]
སྨྲས་པ། འདོད་ཆགས་དང་ཆགས་པ་གཉིས་ལ་སྔ་ཕྱི་མེད་དེ། འདི་ལྟར་དེ་གཉིས་ནི་ལྷན་ཅིག་ཉིད་དུ་སྐྱེ་བ་ཡིན་ནོ། །

[Block 644]
བཤད་པ།

[Block 645 [VERSE]]
འདོད་ཆགས་དང་ནི་ཆགས་པ་དག །
ལྷན་ཅིག་ཉིད་དུ་སྐྱེ་མི་རིགས། །

[Block 646]
འདོད་ཆགས་དང་ཆགས་པ་དག་ལྷན་ཅིག་ཉིད་དུ་སྐྱེ་བར་མི་འཐད་དོ། །ཅིའི་ཕྱིར་ཞེ་ན།

[Block 647 [VERSE]]
འདི་ལྟར་འདོད་ཆགས་ཆགས་པ་དག །
ཕན་ཚུན་ལྟོས་པ་མེད་པར་འགྱུར། །

[Block 648]
འདི་ལྟར་གལ་ཏེ། འདོད་ཆགས་དང་ཆགས་པ་དག་ལྷན་ཅིག་ཉིད་དུ་སྐྱེ་བར་གྱུར་ན་འདོད་ཆགས་དང་ཆགས་པ་དག་ཕན་ཚུན་ལྟོས་པ་མེད་པར་འགྱུར་རོ། །

[Block 649]
དེ་ལྟར་གྱུར་ན་འདིའི་འདོད་ཆགས་ནི་འདིའོ། །

[Block 650]
འདིས་ནི་འདི་ཆགས་སོ་ཞེས་བྱ་བ་དེ་དག་མི་འཐད་དོ། །

[Block 651]
དེ་དག་མེད་ན་འདོད་ཆགས་མི་འཐད་པ་ཉིད་ལ་ཆགས་པ་ཡང་མི་འཐད་པ་ཉིད་དེ། འདི་ལྟར་འདོད་ཆགས་ནི་ཆགས་པར་བྱེད་པ་ཡིན་ལ་ཆགས་པ་ནི་ཆགས་པར་བྱ་བ་ཡིན་ན་ལྷན་ཅིག་ཉིད་དུ་སྐྱེས་པ་ཕན་ཚུན་ལྟོས༌[^393]མེད་པ་དག་ལ་དེ་དག་མི་འཐད་པས་དེའི་ཕྱིར་འདོད་ཆགས་དང་ཆགས་པ་དག་ལྷན་ཅིག་ཉིད་དུ་སྐྱེ་བར་ཡང་མི་རིགས་སོ། །

[Block 652]
ཡང་གཞན་ཡང་། ཁྱོད་ན་རེ་གང་དག་ལྷན་ཅིག་ཉིད་དོ༌[^394]ཞེས་ཟེར་བའི་འདོད་ཆགས་དང་། ཆགས་པ་དེ་དག་གཅིག་པ་ཉིད་དམ་ཐ་དད་པ་ཉིད་དུ་འགྱུར་གྲང་ན། དེ་ལ། གཅིག་ཉིད་ལྷན་ཅིག་ཉིད་མེད་དེ། །རེ་ཞིག་གཅིག་པ་ཉིད་ཡིན་ན་ལྷན་ཅིག་ཉིད་མི་འཐད་དོ། །ཅིའི་ཕྱིར་ཞེ་ན། [^395]དེ་ཉིད་དེ་དང་ལྷན་ཅིག་མིན། །འདི་ན་བ་ལང་གཅིག་པུ་ཞེས་པ༌[^396]ནི་གཅིག་པ་ཉིད་དེ་བ་ལང་གཅིག་ལ་སྙེགས་སོ། །

[Block 653]
དེ་ལ་བ་ལང་གཅིག་པུ་དེ་ཉིད་བ་ལང་གཅིག་པུ་དེ་ཉིད་དང་། ཇི་ལྟར་ལྷན་ཅིག་ཏུ་འགྱུར་ཏེ། དེའི་ཕྱིར་གཅིག་པུ་ཉིད་ཡིན་ན་ལྷན་ཅིག་ཉིད་མི་འཐད་དོ། །

[Block 654]
སྨྲས་པ། འོ་ན་ཐ་དད་པ་ཉིད་ཡིན་ན་ལྷན་ཅིག་ཉིད་དུ་འགྱུར་རོ། །

[Block 655]
བཤད་པ།

[Block 656 [VERSE]]
ཅི་སྟེ་ཐ་དད་ཉིད་ཡིན་ན། །
ལྷན་ཅིག་ཉིད་དུ་ཇི་ལྟར་འགྱུར། །

[Block 657]
གལ་ཏེ་གཅིག་པ་ཉིད་ཡིན་ན་ཡང་ལྷན་ཅིག་ཉིད་དུ་མི་འཐད་ན་ཐ་དད་པ་ཉིད་ཡིན་ན་ལྷན་ཅིག་ཉིད་དུ་ཇི་ལྟར་འགྱུར། འདི་ལྟར་ཐ་དད་པ་ཉིད་ཀྱི་མི་མཐུན་པའི་ཕྱོགས་ནི་ལྷན་ཅིག་ཉིད་ཡིན་ན་མི་མཐུན་པ་དེ་གཉིས་གཅིག་ན་ཇི་ལྟར་ལྷན་ཅིག་གནས་པར་འགྱུར་ཏེ། དེའི་ཕྱིར་ཐ་དད་པ་ཉིད་ཡིན་ན་ཡང་ལྷན་ཅིག་ཉིད་མི་འཐད་དོ། །

[Block 658]
ཅི་སྟེ་མི་འཐད་པ་བཞིན་དུ་ཡང་འདོད་ཆགས་དང་ཆགས་པ་དག་ལ་ལྷན་ཅིག་ཉིད་ཡོད་དོ། །ཞེས་རྟོག་ན། དེ་ལ་ཡང་བཤད་པར་བྱ་སྟེ།

[Block 659 [VERSE]]
གལ་ཏེ་གཅིག་པུ་ལྷན་ཅིག་ན། །
གྲོགས་མེད་པར་ཡང་དེར་འགྱུར་རོ། །
གལ་ཏེ་ཐ་དད་ལྷན་ཅིག་ན། །
གྲོགས་མེད་པར་ཡང་དེར་འགྱུར་རོ། །

[Block 660]
གལ་ཏེ་རེ་ཞིག་འདོད་ཆགས་དང་ཆགས་པ་དག་གཅིག༌[^397]པ་ཉིད་ཡིན་ཡང་ལྷན་ཅིག་ཉིད་དུ་འགྱུར་ན་ནི་དེ་ལྟ་ན་གྲོགས་མེད་པར་ཡང་ལྷན་ཅིག་ཉིད་དུ་འགྱུར་རོ། །ཇི་ལྟར་ཞེ་ན། འདི་ལ་གཅིག་ནི་གཅིག་པུ་ལ་སྙེགས་ཏེ། དེ་ན་བ་ལང་གཅིག་དང་རྟ་གཅིག་ཅེས་བྱ་བའི་གཅིག་ཉིད་ནི་བ་ལང་ལ་ཡང་སྙེགས་རྟ་ལ་ཡང་སྙེགས་པས་གང་དང་གང་ན་གཅིག་པ་ཉིད་ཡོད་པ་དེ་དང་དེ་ན་ལྷན་ཅིག་ཉིད་ཡོད་ཅིང་། བ་ལང་གཅིག་པུ་ཉིད་དང་། རྟ་གཅིག་པུ་ཉིད་ལ་གྲོགས་མེད་པར་ཡང་ལྷན་ཅིག་ཉིད་ཡོད་པར་ཐལ་བར་འགྱུར་ཏེ། དེ་ལྟ་ན་ལྷན་ཅིག་ཉིད་དུ་བརྟག་པ་དོན་མེད་པར་འགྱུར་རོ། །

[Block 661]
ཅི་སྟེ་ཡང་ཐ་དད་པ་ཉིད་ཡིན་ཡང་། ལྷན་ཅིག་ཉིད་དུ་འགྱུར་ན་ནི་དེ་ལྟ་ན་ཡང་གྲོགས་མེད་པར་ཡང་ལྷན་ཅིག་ཉིད་དུ་འགྱུར་རོ། །ཇི་ལྟར་ཞེ་ན། འདི་ལ་བ་ལང་ལས་ཀྱང་རྟ་ཐ་དད་ལ། རྟ་ལས་ཀྱང་བ་ལང་ཐ་དད་པས་གང་དང་གང་ན་ཐ་དད་པ་ཉིད་ཡོད་པ་དེ་དང་དེ་ན་ལྷན་ཅིག་ཉིད་ཡོད་ཅིང་། བ་ལང་ཐ་དད་པ་ཉིད་དང་། རྟ་ཐ་དད་པ་ཉིད་ལ་གྲོགས་མེད་པར་ཡང་ལྷན་ཅིག་ཉིད་ཡོད་པར་ཐལ་བར་འགྱུར་ཏེ། དེ་ལྟ་ན་ཡང་ལྷན་ཅིག་ཉིད་དུ་བརྟག་པ༌[^398]དོན་མེད་པར་འགྱུར་རོ། །

[Block 662]
སྨྲས་པ། ཐ་དད་པ་ཉིད་ནི་བ་ལང་ལ་ཡོད་པ་ཡང་མ་ཡིན་ལ། རྟ་ལ་ཡོད་པ་ཡང་མ་ཡིན་གྱི། དེ་གཉིས་ཡང༌[^399]ལྷན་ཅིག་བྱུང་བ་ལ་ཡོད་པས་དེ་ནི་གཉི་ག་སྤྱིའི་འབྲས་བུ་ཡིན་ཏེ་ཕྲད་པ་བཞིན་ནོ། །

[Block 663]
གལ་ཏེ་ཐ་དད་པ་ཉིད་སོ་སོ་ལ་ཡོད་པར་གྱུར་ན་ནི་ཐ་དད་པ་ཉིད་གཉིས་སུ་འགྱུར་བ་དང་། དངོས་པོ་ཕན་ཚུན་མི་ལྟོས་པར་རེ་རེ་ལ་ཡང་ཡོད་པར་འགྱུར་བས་དོན་མི་འདོད་དེ། དེའི་ཕྱིར་ཐ་དད་པ་ཉིད་ནི་གཉི་ག་ལྷན་ཅིག་བྱུང་བ་ལ་ཡོད་དོ། །

[Block 664]
བཤད་པ།

[Block 665 [VERSE]]
གལ་ཏེ་ཐ་དད་ལྷན་ཅིག་ན། །
འདོད་ཆགས་ཆགས་པ༌[^400]ཅི་ཞིག་ཡིན། །
ཐ་དད་ཉིད་དུ་གྲུབ་གྱུར་ན། །
དེས་ན་དེ་གཉིས་ལྷན་ཅིག་འགྱུར། །

[Block 666]
ཐ་དད་པ་ཉིད་གཉི་ག་ལ་ཡོད་པར་ནི་འདོད་ལ་རག་གོ། །

[Block 667]
གལ་ཏེ་ཐ་དད་པ་ཉིད་གཉི་ག་ལ་ཡོད་པ་ལ་ལྷན་ཅིག་ཉིད་དུ་རྟོག་ན་དེ་ལྟར༌[^401]ན་འདོད་ཆགས་དང་ཆགས་པ་དག་ལ་ཅི་ཞིག་རབ་ཏུ་བསྒྲུབ་པ་ཡིན། གང་གི་ཚེ་དེ་ལྟར་ཡང་རྟོག་ན་དེ་གཉིས་ཐ་དད་པ་ཉིད་དུ་གྲུབ་པ་ཁོ་ནར་འགྱུར་རོ། །

[Block 668]
དེས་ན་ཐ་དད་པ་ཉིད་དུ་རབ་ཏུ་གྲུབ་པའི་ཕྱིར་དེ་གཉིས་ལྷན་ཅིག་ཉིད་དུ་རྟོག་པར་འགྱུར་རོ། །

[Block 669 [VERSE]]
གལ་ཏེ་འདོད་ཆགས་ཆགས་པ་དག །
ཐ་དད་ཉིད་དུ་གྲུབ་འགྱུར༌[^402]ན། །
དེ་གཉིས་ལྷན་ཅིག་ཉིད་དུ་ནི། །
ཅི་ཡི་ཕྱིར་ན་ཡོངས་སུ་རྟོག །

[Block 670]
ཉིད་དུ་ཞེས་བྱ་བའི་སྒྲ་ནི་ཁོ་ནར་ཞེས་བྱ་བའི་དོན་ཏོ། །
--- END BLOCKS ---
