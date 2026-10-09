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
[Block 2801 [VERSE]]
གལ་ཏེ་ལྷ་ལས་མི་གཞན་ན། །
དེ་ལྟ་ན་ནི་མི་རྟག་འགྱུར། །
གལ་ཏེ་ལྷ་མི་གཞན་ཡིན་ནོ། །
རྒྱུད༌[^1770]ནི་འཐད་པར་མི་འགྱུར་རོ། །

[Block 2802]
གལ་ཏེ་ལྷ་ལས་མི་གཞན་ཡིན་ན་དེ་ལྟ་ན་ནི་མི་རྟག་པར་འགྱུར་རོ། །

[Block 2803]
རྒྱུད་ཀྱི་གཏན་ཚིགས་ཀྱིས་ལྷ་ལས་མི་གཞན་ཡིན་པར་མི་འཐད་པས་དེའི་ཕྱིར་མི་རྟག་པ་མ་ཡིན་ནོ། །

[Block 2804 [VERSE]]
གལ་ཏེ་ཕྱོགས་གཅིག་ལྷ་ཡིན་ལ། །
ཕྱོགས་གཅིག་མི་ནི་ཡིན་གྱུར་ན། །
རྟག་དང་མི་རྟག་འགྱུར་བའི་ཕྱིར། །
དེ་ཡང་རིགས་པ་མ་ཡིན་ནོ། །

[Block 2805]
གལ་ཏེ་ཕྱོགས་གཅིག་ནི་ལྷ་ཡིན་ལ་ཕྱོགས་གཅིག་ནི་མི་ཡིན་པར་གྱུར་ན་དེ་ལྟ་ན་རྟག་ཀྱང་རྟག་ལ་མི་རྟག་ཀྱང་མི་རྟག་པར་འགྱུར་བ་ཞིག་ན། གང་གི་ཕྱིར་དེ་ལྟར་བདག་ཉིད་གཉིས་པ་ཉིད་མི་རིགས་པ་དེའི་ཕྱིར་རྟག་ཀྱང་རྟག་ལ་མི་རྟག་ཀྱང་མི་རྟག་པ་མ་ཡིན་ནོ། །

[Block 2806 [VERSE]]
གལ་ཏེ་རྟག་དང་མི་རྟག་པ། །
གཉི་ག་གྲུབ་པར་གྱུར་ན་ནི། །
རྟག་པ་མ་ཡིན་མི་རྟག་མིན།

[Block 2807]
[^1771] །འགྲུབ་པར་འགྱུར་བ་འདོད་ལ་རག །གལ་ཏེ་རྟག་པ་དང་མི་རྟག་པ་ཞེས་བྱ་བ་དེ་གཉི་ག་རབ་ཏུ་གྲུབ་པར་གྱུར་ན་ནི། དེའི་ཕྱིར་རྟག་པ་ཡང་མ་ཡིན་མི་རྟག་པ་ཡང་མ་ཡིན་པ་ཞེས་བྱ་བ་དེ་ཡང་རབ་ཏུ་འགྲུབ་པར་འགྱུར་བ་འདོད་ལ་རག་ན། གང་གི་ཕྱིར་རྟག་པ་དང་མི་རྟག་པ་དེ་གཉི་ག་རབ་ཏུ་མ་གྲུབ་པ་དེའི་ཕྱིར་རྟག་པ་ཡང་མ་ཡིན་མི་རྟག་པ་ཡང་མ་ཡིན་པ་ཞེས་བྱ་བ་དེ་ཡང་རབ་ཏུ་མི་འགྲུབ་བོ། །

[Block 2808 [VERSE]]
གལ་ཏེ་གང་ཞིག་གང་ནས་འོངས། །
ཅི་ཞིག་གང་དུ་འགྲོ་འགྱུར་ན། །
དེ་ཕྱིར་དེ་ལ་ཐོག་མེད་པས། །
རྟག་པར་གྱུར་ན་དེ་ཡང་མེད། །

[Block 2809]
གལ་ཏེ་དངོས་པོ་གང་ཞིག་ཡུལ་གང་ནས་འོངས་ཤིང་ཅི་ཞིག་གཅིག་ཏུ་གང་དུ་འགྲོ་བར་འགྱུར་ན་ནི་དེའི་ཕྱིར་དེ་ལ་ཐོག་མ་མེད་པས་རྟག་པར་འགྱུར་བ་ཞིག་ན། ཤེས་རབ་ཀྱིས་བརྩལ༌[^1772]ན་དངོས་པོ་གང་ཞིག་ཡུལ་གང་ནས་འོངས་ཤིང་། ཇི་ཞིག་གཅིག་ཏུ་གང་འགྲོ་བར་འགྱུར་བ་དེ་ལྟ་བུའི་དངོས་པོ་འགའ་ཡང་མེད་པས་དེའི་ཕྱིར་དེ་ལ༌[^1773]ཐོག་མ་མེད་པ་ཡང་མེད་པས་རྟག་པ་མ་ཡིན་ནོ། །

[Block 2810 [VERSE]]
གལ་ཏེ་རྟག་པ་འགའ་མེད་ན། །
མི་རྟག་གང་ཞིག་ཡིན་པར་འགྱུར། །
རྟག་པ་དང་ནི་མི་རྟག་དང་། །
དེ་གཉིས་བསལ་བར༌[^1774]གྱུར་པའོ། །

[Block 2811]
གལ་ཏེ་དེ་ལྟར་ཤེས་རབ་ཀྱིས་བརྟགས་ན་དངོས་པོ་འགའ་ཡང་མེད་ན་མི་རྟག་པ་གང་ཞིག་ཡིན་པར་གྱུར། རྟག་ཀྱང་རྟག་ལ་མི་རྟག་ཀྱང་མི་རྟག་པ་དང་། རྟག་པ་ཡང་མ་ཡིན་མི་རྟག་པ་ཡང་མ་ཡིན་པ་ཡང་གང་ཞིག་ཡིན་པར་འགྱུར། དེ་ལྟ་བས་ན་སྔོན་གྱི་མཐའ་ལས་བརྩམས་པའི་རྟག་པ་དང་མི་རྟག་པ་ལ་སོགས་པ་བཞི་པོ་དེ་དག་མི་འཐད་དོ། །

[Block 2812]
ད་ནི། ཕྱི་མའི་མཐའ་ལས་བརྩམས་པའི་མཐའ་དང་མཐའ་མེད་པ་ལ་སོགས་པ་བཞི་པོ་དེ་དག་ཇི་ལྟར་མི་འཐད་པ། དེ་ལྟར་བཤད་པར་བྱ་སྟེ། གལ་ཏེ་ཇི་ལྟར་ཞེ་ན། བཤད་པ།

[Block 2813 [VERSE]]
གལ་ཏེ་འཇིག་རྟེན་མཐའ་ཡོད་ན། །
འཇིག་རྟེན་ཕ་རོལ་ཇི་ལྟར་འགྱུར། །
གལ་ཏེ་འཇིག་རྟེན་མཐའ་མེད་ན། །
འཇིག་རྟེན་ཕ་རོལ་ཇི་ལྟར་འགྱུར། །

[Block 2814]
འཇིག་རྟེན་མཐའ་ཡོད་ཅེས་བྱ་བ་མི་འཐད་དོ།[^1775] །ཅིའི་ཕྱིར་ཞེ་ན། གལ་ཏེ་འཇིག་རྟེན་ཕ་རོལ༌[^1776]ཡོད་པར་གྱུར་ན། དེའི་ཕྱིར་འཇིག་རྟེན་ཕ་རོལ་ཡོད་པར་མི་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2815]
འཇིག་རྟེན་ཕ་རོལ་ཡང་ཡོད་པས་དེའི་ཕྱིར་འཇིག་རྟེན་མཐའ་ཡོད་ཅེས་བྱ་བ་མི་འཐད་དོ།[^1777] །འཇིག་རྟེན་མཐའ་མེད་ཅེས་བྱ་བ་ཡང་མི་འཐད་དོ།[^1778] །

[Block 2816]
ཅིའི་ཕྱིར་ཞེ་ན། གལ་ཏེ་འཇིག་རྟེན་མཐའ་མེད་པར་གྱུར་ན་དེའི་ཕྱིར་འཇིག་རྟེན་ཕ་རོལ་མེད་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2817]
འཇིག་རྟེན་ཕ་རོལ་ཡང་ཡོད་པས་དེའི་ཕྱིར་འཇིག་རྟེན་མཐའ་མེད་ཅེས་བྱ་བ་ཡང་ཡོད་པས་དེའི་ཕྱིར་འཇིག་རྟེན་མཐའ་མེད་ཅེས་བྱ་བ༌[^1779]ཡང་མི་འཐད་དོ། །

[Block 2818]
དེ་གཉིས་ཅིའི་ཕྱིར་མི་འཐད་ཅེ་ན། དེ་ལ་བཤད་པར་བྱ་སྟེ།

[Block 2819 [VERSE]]
གང་ཕྱིར་ཕུང་པོ་རྣམས་ཀྱི་རྒྱུན། །
འདི༌[^1780]ནི་མར་མེའི་འོད་དང་མཚུངས། །
དེ་ཕྱིར་མཐའ་ཡོད་ཉིད་དང་ནི། །
མཐའ་མེད་ཉིད་ཀྱང་མི་རིགས་སོ། །

[Block 2820]
གང་གི་ཕྱིར་ཕུང་པོ་རྣམས་ཀྱི་རྒྱུན་འདི་ནི་མར་མེའི་འོད་དང་མཚུངས་པར་རྒྱུ་དང་རྐྱེན་གྱི་ཚོགས་པའི་དབང་གིས་འབྱུང་བ་དེའི་ཕྱིར་འཇིག་རྟེན་མཐའ་ཡོད་པ་ཉིད་དང་། མཐའ་མེད་པ་ཉིད་ཅེས་བྱ་བ་ཡང་མི་རིགས་སོ། །

[Block 2821]
ཅིའི་ཕྱིར་མི་རིགས་ཤེ་ན། དེ་ལ༌[^1781]བཤད་པར་བྱ་སྟེ།

[Block 2822 [VERSE]]
གལ་ཏེ་སྔ་མ་འཇིག་འགྱུར་ཞིང་། །
ཕུང་པོ་འདི་ལ་བརྟེན་བྱས་ནས། །
ཕུང་པོ་འདི་ནི་མི་འབྱུང་ན། །
དེས་ན་འཇིག་རྟེན་མཐའ་ཡོད་འགྱུར། །

[Block 2823 [VERSE]]
གལ་ཏེ་སྔ་མ་མི་འཇིག་ཅིང་། །
ཕུང་པོ་འདི་ལ་བརྟེན་བྱས་ནས། །
ཕུང་པོ་འདི་ནི་མི་འབྱུང་ན། །
དེས་ན་འཇིག་རྟེན་མཐའ་མེད་འགྱུར། །

[Block 2824]
གལ་ཏེ་ཕུང་པོ་སྔ་མ་རྣམས་འཇིག་པར་འགྱུར་ཞིང་། ཕུང་པོ་འདི་དག་ལ་བརྟེན་ནས་ཕུང་པོ་གཞན་དེ་དག་མི་འབྱུང་ན་ནི་དེས་ན་འཇིག་རྟེན་མཐའ་ཡོད་པར་འགྱུར་བ་ཞིག་ན་གང་གི་ཕྱིར་དེ་ལྟ་མ་ཡིན་པ་དེའི་ཕྱིར་འཇིག་རྟེན་མཐའ་ཡོད་ཅེས་བྱ་བ་མི་འཐད་དོ། །

[Block 2825]
གལ་ཏེ་ཕུང་པོ་སྔ་མ་རྣམས་མི་འཇིག་ཅིང་ཕུང་པོ་དེ་དག༌[^1782]ལ་བརྟེན་ནས་ཕུང་པོ་ཕྱི་མ་དེ་དག་མི་འབྱུང་ན་ནི་དེས་ན་འཇིག་རྟེན་མཐའ་མེད་པར་འགྱུར་བ་ཞིག་ན། གང་གི་ཕྱིར་དེ་ལྟ་མ་ཡིན་པ་དེའི་ཕྱིར་འཇིག་རྟེན་མཐའ་མེད་པ་ཞེས༌[^1783]བྱ་བ་ཡང་མི་འཐད་དོ། །

[Block 2826]
སློབ་དཔོན་འཕགས་པ་ལྷས་ཀྱང་།

[Block 2827 [VERSE]]
ཉན་པ་པོ་དང་མཉན་བྱ་དང་། །
སྨྲ་པོ་འབྱུང་བ༌[^1784]ཤིན་ཏུ་དཀོན། །
དེ་ཕྱིར་མདོར་ན་འཁོར་བ་ནི། །
མཐའ་ཡོད་མ་ཡིན་མཐའ་མེད་མིན། །

[Block 2828]
ཞེས་གསུངས་སོ། །

[Block 2829]
ད་ནི་འཇིག་རྟེན་མཐའ་ཡོད་ཀྱང་ཡོད་ལ་མཐའ༌[^1785]མེད་ཀྱང་མེད་ཅེས་བྱ་བ་དེ་ཡང་མི་འཐད་དེ། ཅིའི་ཕྱིར་ཞེ་ན། བཤད༌[^1786]པར་བྱ་སྟེ།

[Block 2830 [VERSE]]
གལ་ཏེ་ཕྱོགས་གཅིག་མཐའ་ཡོད་ལ། །
ཕྱོགས་གཅིག་མཐའ་ནི་མེད་གྱུར་ན། །
འཇིག་རྟེན་མཐའ་ཡོད་མཐའ་མེད་འགྱུར། །
དེ་ཡང་རིགས་པ་མ་ཡིན་ནོ། །

[Block 2831]
གལ་ཏེ་ཕྱོགས་གཅིག་མཐའ་ཡོད་པར་གྱུར་ལ། ཕྱོགས་གཅིག་མཐའ་མེད་པར་གྱུར་ན་ནི་དེའི་ཕྱིར་འཇིག་རྟེན་མཐའ་ཡོད་ཀྱང་ཡོད་ལ། མཐའ་མེད་ཀྱང་མེད་པར་འགྱུར་བ་ཞིག་ན། དེ་ལྟ་ན་དངོས་པོ་བདག་ཉིད་གཉིས་པ་ཉིད་དུ་གྱུར་པ་དེ༌[^1787]ནི་མི་འཐད་དོ། །

[Block 2832 [VERSE]]
ཇི་ལྟ་བུར་ན་ཉེར་ལེན་པོ། །
ཕྱོགས་གཅིག་རྣམ་པར་འཇིག་འགྱུར་ལ། །
ཕྱོགས་གཅིག་རྣམ་པར་འཇིག་མི་འགྱུར། །
དེ་ལྟར་དེ་ནི་མི་རིགས་སོ། །

[Block 2833 [VERSE]]
ཇི་ལྟ་བུར་ན་ཉེར་བླང་བ། །
ཕྱོགས་གཅིག་རྣམ་པར་འཇིག་འགྱུར་ལ། །
ཕྱོགས་གཅིག་རྣམ་པར་འཇིག་མི་འགྱུར། །
དེ་ལྟར་དེ་ཡང་མི་རིགས་སོ། །

[Block 2834]
རེ་ཞིག་ཉེ་བར་ལེན་པ་པོ་རིགས་པ་གང་གིས་ཕྱོགས་གཅིག་རྣམ་པར་འཇིག་པར་འགྱུར་ལ། ཕྱོགས་གཅིག་རྣམ་པར་འཇིག་པར་མི་འགྱུར་ཏེ། རྟག་པ་དང་མི་རྟག་པ་ཉིད་མེད་པའི་ཕྱིར་རེ་ཞིག་དེ་ལྟར་ནི༌[^1788]མི་རིགས་སོ། །

[Block 2835]
ཉེ་བར་བླང་བ་ཡང་རྣམ་པ་གང་གིས་ཕྱོགས་གཅིག་རྣམ་པར་འཇིག་པར་འགྱུར་ལ། ཕྱོགས་གཅིག་རྣམ་པར་འཇིག་པར་མི་འགྱུར་ཏེ། རྟག་པ་དང་མི་རྟག་པ་ཉིད་མི་འཐད་པ་ཁོ་ནའི་ཕྱིར་དེ་ལྟར་ཡང་མི་རིགས་སོ། །

[Block 2836]
དེ་ལྟར་གང་གི་ཕྱིར་དངོས་པོ་བདག་ཉིད་གཉིས་པ་ཉིད་མི་འཐད་པ་དེའི་ཕྱིར་འཇིག་རྟེན་མཐའ་ཡོད་ཀྱང་ཡོད་ལ་མཐའ་མེད་ཀྱང་མེད་ཅེས་བྱ་བ་མི་འཐད་དོ། །

[Block 2837]
ད་ནི་འཇིག་རྟེན་མཐའ་ཡོད་པ་ཡང་མ་ཡིན་མཐའ་མེད་པ་ཡང་མ་ཡིན་ཞེས་བྱ་བ་ཡང་མི་འཐད་དེ། ཅིའི་ཕྱིར་ཞེ་ན། བཤད་པར་བྱ་སྟེ།

[Block 2838 [VERSE]]
གལ་ཏེ་མཐའ་ཡོད་མཐའ་མེད་པ། །
གཉི་ག་གྲུབ་པར་གྱུར་ན་ནི། །
མཐའ་ཡོད་མ་ཡིན་མཐའ་མེད་མིན། །
འགྲུབ་པར་འགྱུར་བ་འདོད་ལ་རག །

[Block 2839]
གལ་ཏེ་མཐའ་ཡོད་པ་དང་མཐའ་མེད་པ་ཞེས་བྱ་བ་དེ་གཉི་ག་རབ་ཏུ་གྲུབ་པར་གྱུར་ན་ནི་དེའི་ཕྱིར་མཐའ་ཡོད་པ་ཡང་མ་ཡིན་མཐའ་མེད་པ་ཡང་མ་ཡིན་ཞེས་བྱ་བ་འདི་རབ་ཏུ་འགྲུབ་པར་འགྱུར་བར་ཡང་འདོད་ལ་རག་ན་གང་གི་ཕྱིར་མཐའ་ཡོད་པ་དང་། མཐའ་མེད་པ་ཞེས་བྱ་བ་དེ༌[^1789]གཉིས་རབ་ཏུ་མ་གྲུབ་པ་དེའི་ཕྱིར་མཐའ་ཡོད་པ་ཡང་མ་ཡིན། མཐའ་མེད་པ་ཡང་མ་ཡིན་ཞེས་བྱ་བ་འདི་ཡང་རབ་ཏུ་མ་གྲུབ་པོ། །དེ་ལྟ་བས་ན་བརྟག་པ༌[^1790]འདིས་ཕྱི་མའི་མཐའ་ལས་བརྩམས་པའི་མཐའ་དང་མཐའ་མེད་པ་ལ་སོགས་པ་བཞི་མི་འཐད་དོ། །

[Block 2840 [VERSE]]
ཡང་ན་དངོས་པོ་ཐམས་ཅད་དག །
སྟོང་ཕྱིར་རྟག་ལ་སོགས་ལྟ་བ། །
གང་དུ་གང་ལ་གང་དག་ནི། །
ཅིའི་ཕྱིར་ཀུན་དུ་འབྱུང་བར་འགྱུར། །
--- END BLOCKS ---
