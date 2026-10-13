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
[Block 211]
བཤད་པ།

[Block 212 [VERSE]]
རྐྱེན་རྣམས་སོ་སོ་འདུས་པ་ལས། །
འབྲས་བུ་དེ་ནི་མེད་པ་ཉིད། །
རྐྱེན་རྣམས་ལ་ནི་གང་མེད་པ། །
དེ་ནི་རྐྱེན་ལས་ཇི་ལྟར་སྐྱེ། །

[Block 213]
ཉིད་ཅེས་བྱ་བའི་སྒྲ་ནི་ཁོ་ན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 214]
སོ་སོ་བ་དག་ལ་ཡང་མེད་པ་ཁོ་ན་ཡིན་ལ། འདུས་པ་དག་ལ་ཡང་མེད་པ་ཁོ་ནའོ་ཞེས་བྱའོ། །

[Block 215]
ཁྱོད་ཀྱིས་རྐྱེན་རབ་ཏུ་བསྒྲུབ་པའི་ཕྱིར་འབྲས་བུ་སྐྱེ་བར་བསྟན་པ་གང་ཡིན་པ་དེ་ཉིད་མི་འཐད་ན། རྐྱེན་འགྲུབ་པར་ག་ལ་འགྱུར་ཇི་ལྟར་ཞེ་ན། གང་གི་ཕྱིར་རྐྱེན་རྣམས་སོ་སོ་བ་དང་འདུས་པ་ལ་འབྲས་བུ་དེ་མེད་པ་ཉིད་ཡིན་པའི་ཕྱིར་ཏེ། རྐྱེན་རྣམས་སོ་སོ་བ་དང་འདུས་པ་ལ་མེད་པ་ཉིད་གང་ཡིན་པ་དེ་ཇི་ལྟར་དེ་དག་ལས་སྐྱེ་བར་འགྱུར། འབྲས་བུ་སྐྱེ་བ་མེད་ན་ཁྱོད་ཀྱིས༌[^146]རྐྱེན་འགྲུབ་པར་ག་ལ་འགྱུར། དེ་ལ་འདི་སྙམ་དུ་རྐྱེན་རྣམས་ལས༌[^147]འབྲས་བུ་ཡོད་པ་ཁོ་ནར་སེམས་ན། དེ་ལྟ༌[^148]ན་ཡང་རྐྱེན་འཐད་པ་མ་ཡིན་ཏེ། འདི་ལྟར་ཡོད་པ་ལ་རྐྱེན་གྱིས་བྱ་བ་མེད་དེ་སྐྱེས་ཟིན་པ་ཡང་སྐྱེད༌[^149]མི་དགོས་པའི་ཕྱིར་རོ། །

[Block 216]
ཡང་གཞན་ཡང་གལ་ཏེ་རྐྱེན་རྣམས་ལ་འབྲས་བུ་དེ་ཡོད་པར་གྱུར་ན། རྐྱེན་དུ་མའི་འབྲས་བུ་གང་ཡིན་པ་དེ་རྐྱེན་རེ་རེ་ལ་ཡོངས་སུ་རྫོགས་པར་ཡོད་པའམ། ཆ་ཤས་ཅིག་ཡོད་པར་འགྱུར་གྲང་ན། དེ་ལ་རེ་ཞིག་གལ་ཏེ་རེ་རེ་ལ་ཡོངས་སུ་རྫོགས་པར་ཡོད་པར་བརྟགས༌[^150]ན་ནི་རྐྱེན་དུ་མར་མི་འགྱུར་ཏེ། རེ་རེ་ལ་ཡང་ཡོད་པའི་ཕྱིར་མི་ལྟོས་པར་རེ་རེ་ལས་ཀྱང་འབྲས་བུ་སྐྱེ་བར་ཐལ་བར་འགྱུར་རོ། །

[Block 217]
ཅི་སྟེ་རྐྱེན་རྣམས་ལ་འབྲས་བུའི་ཆ་ཤས༌[^151]ཡོད་པར་བརྟགས༌[^152]ན་ནི། དེ་ལྟ་ན་ཡང་མི་ལྟོས་པར་རེ་རེ་ལས་འབྲས་བུའི་ཆ་ཤས་སྐྱེ་བར་ཐལ་བར་འགྱུར་བས༌[^153]དེ་ཡང་མི་འདོད་དེ། དེའི་ཕྱིར་རྐྱེན་རྣམས་སོ་སོ་བ་དང་འདུས་པ་ལ་འབྲས་བུ་དེ་ཡོད་པར་མི་འཐད་དོ། །

[Block 218]
ཅི་སྟེ་རྐྱེན་རྣམས་ལ་འབྲས་བུ་མེད་ཀྱང་རྐྱེན་རྣམས་ལས་སྐྱེ་སྟེ། འབྲས་བུ་སྐྱེ་བ་ལ་ལྟོས༌[^154]ནས་ཁོ་བོའི་རྐྱེན་རབ་ཏུ་འགྲུབ་པོ་སྙམ་དུ་སེམས་ན། དེ་ལ་བཤད་པར་བྱ་སྟེ།

[Block 219 [VERSE]]
ཅི་སྟེ་དེ་ནི་མེད་པར་ཡང་། །
རྐྱེན་དེ་དག་ལས་སྐྱེ་འགྱུར་ན། །
རྐྱེན་མིན་ལས་ཀྱང་འབྲས་བུ་ནི། །
ཅིའི་ཕྱིར་ཞེ༌[^155]ན་སྐྱེ་མི་འགྱུར། །

[Block 220]
འདི་ལ་འབྲས་བུ་ཡོད་པ་ལས་རྐྱེན་དང་རྐྱེན་མ་ཡིན་པའི་བྱེ་བྲག་ཏུ་འགྱུར་ན། འབྲས་བུ་དེ་ཡང་རྐྱེན་དང་རྐྱེན་མ་ཡིན་པ་དག་ལ་མེད་དོ། །

[Block 221]
དེ་དག་ལ་མེད་བཞིན་དུ་གལ་ཏེ་རྐྱེན་རྣམས་ལས་འབྲས་བུ་སྐྱེ་ན་ནི་རྐྱེན་མ་ཡིན་པ་རྣམས་ལས་ཀྱང་ཅིའི་ཕྱིར་མི་སྐྱེ་སྟེ།

[Block 222]
འདི་ལྟར་རྐྱེན་དང་རྐྱེན་མ་ཡིན་པ་རྣམས་ལ་འབྲས་བུ་མེད་པར་མཚུངས་པ་ལས།

[Block 223]
རྐྱེན་རྣམས་ལས་ནི་འབྲས་བུ་སྐྱེ་ལ་རྐྱེན་མ་ཡིན་པ་རྣམས་ལས་ནི་མི་སྐྱེ་བ་ཞེས་བྱ་བ་དེ་ནི་ཡིད་ལ་བསམས་པ༌[^156]ཙམ་དུ་ཟད་དོ། །

[Block 224]
དེའི་ཕྱིར་འབྲས་བུ་སྐྱེ་བ་མི་འཐད་དེ། འབྲས་བུ་སྐྱེ་བ་མེད་ན་རྐྱེན་འགྲུབ་པར་ག་ལ་འགྱུར།

[Block 225]
འདིར་སྨྲས་པ། རྐྱེན་རྣམས་ལ་འབྲས་བུ་ཡོད་པ་དང་མེད་པའི༌[^157]རྐྱེན་རྣམས་ལས་སྐྱེའོ། །ཞེས་ནི་མི་སྨྲའོ། །

[Block 226]
འབྲས་བུ་ནི་རྐྱེན་རྣམས་ལས་གྱུར་པའི༌[^158]རྐྱེན་གྱི་བདག་ཉིད་རྐྱེན་ལས་བྱུང་བ་ཡིན་ནོ། །ཞེས་སྨྲའོ། །

[Block 227]
དེ་ལྟ་ཡིན་ནི༌[^159]སྣམ་བུ་ནི་རྒྱུ་སྤུན་ལས་གྱུར་པ་རྒྱུ་སྤུན་གྱི་བདག་ཉིད་ལས་བྱུང་བ་ཡིན་པས། རྒྱུ་སྤུན་དག་ནི་སྣམ་བུའི་རྐྱེན་ཡིན་ནོ། །

[Block 228]
བཤད་པ། འབྲས་བུ་རྐྱེན་ལས་བྱུང་ཡིན་ནོ།[^160] །

[Block 229 [VERSE]]
རྐྱེན་རྣམས་རང་ལས་བྱུང་མ་ཡིན། །
རང་བྱུང་མིན་ལས༌[^161]འབྲས་བུ་གང་། །
དེ་ནི་ཇི་ལྟར་རྐྱེན་ལས་བྱུང་། །

[Block 230]
འབྲས་བུ་རྐྱེན་ལས་གྱུར་པ་རྐྱེན་གྱི་བདག་ཉིད་ལས་བྱུང་བ་མ་ཡིན་པར་བརྟགས༌[^162]ན། རྐྱེན་དེ་རྣམས་ནི་རང་ལས་གྱུར་པ་མ་ཡིན། རང་ཉིད་རབ་ཏུ་གྲུབ་པ༌[^163]མ་ཡིན། རང་ཉིད༌[^164]བདག་ཉིད་མ་ཡིན། རང་ལས་བྱུང་བ་མ་ཡིན་ཏེ་ངོ་བོ་ཉིད་མེད་པ་ཡིན་ནོ། །

[Block 231]
རྐྱེན་རང་ལས་གྱུར་པ་མ་ཡིན་པ། རང་ཉིད་རབ་ཏུ་གྲུབ་པ་མ་ཡིན་པ། རང་གི་བདག་ཉིད་མ་ཡིན་པ། རང་ལས་བྱུང་བ་མ་ཡིན་པ་ངོ་བོ་ཉིད་མེད་པ་དེ་དག་ལས་འབྲས་བུ་བྱུང་བར་རྟོག་ན་ཇི་ལྟར་རྐྱེན་ལས་བྱུང་བར་ཉེ་བར་བརྟགས་ན།[^165] འདི་ལྟར་གལ་ཏེ་རྒྱུ་སྤུན་དག་རང་ཉིད་རབ་ཏུ་གྲུབ་ན་ནི་རང་ལས་བྱུང་བར་ཡང་འགྱུར་བས། དེས་ན་སྣམ་བུ་རྒྱུ་སྤུན་དག་ལས་བྱུང་བ་ཞེས་བྱ་བ་དེ་ཡང་འཐད་པར་འགྱུར་བ་ཞིག་ན། གང་གི་ཚེ་རྒྱུ༌[^166]དག་རང་ཉིད་རབ་ཏུ་མ་གྲུབ་པ་རང་ལས་བྱུང་བ་མ་ཡིན་པ་ངོ་བོ་ཉིད་མེད་པ་སྟེ།[^167] རྒྱུ་དག༌[^168]ལས་གྱུར་པ་རྒྱུ་དག་གི༌[^169]བདག་ཉིད་རྒྱུ་ལས་བྱུང་བ་ཡིན་པ་དེའི་ཚེ། སྣམ་བུ་རྒྱུ་སྤུན་དག་ལས་བྱུང་ངོ་། །ཞེས་བྱ་བ་དེ་ཇི་ལྟར་འཐད་པར་འགྱུར། སློབ་དཔོན་འཕགས་པ་ལྷས་ཀྱང་།

[Block 232 [VERSE]]
སྣམ་བུ་རྒྱུ་ལས་གྲུབ་ཡིན་ན། །
རྒྱུ་ཡང་གཞན་ལས་གྲུབ་པ་ཡིན། །
གང་ལ་རང་ལས་གྲུབ་མེད་པ། །

[Block 233]
དེ་ཡིས༌[^170]གཞན་ནི་ཇི་ལྟར་བསྐྱེད།[^171] །ཅེས་གསུངས་སོ། །

[Block 234]
དེ་ལྟར་གང་གི་ཕྱིར་རྐྱེན་རྣམས་རང་ཉིད་རབ་ཏུ་མ་གྲུབ་རང་ལས་བྱུང་བ་མ་ཡིན་ཞིང་ངོ་བོ་ཉིད་མེད་པ། དེའི་ཕྱིར༌[^172]རྐྱེན་བྱུང་མ་ཡིན། འབྲས་བུ་རྐྱེན་ལས་བྱུང་བ་མ་ཡིན་ནོ། །

[Block 235]
དེ་ལ་འདི་སྙམ་དུ་འབྲས་བུ་རྐྱེན་མ་ཡིན་པ་ལས༌[^173]བྱུང་བར་སེམས་ན། བཤད་པ། རྐྱེན་མིན་ལས་བྱུང་འབྲས་བུ་ནི། །ཡོད་མིན། གང་གི་ཚེ་སྣམ་བུ་རྒྱུ་སྤུན་ལས་བྱུང་བར་མི་འཐད་པ་དེའི་ཚེ་སྣམ་བུ་རྩི་རྐྱང༌[^174]ལས་བྱུང་ངོ་། །ཞེས་བྱ་བ་འཇིག་རྟེན་དང་འགལ་བ་འདི་ཇི་ལྟར་འཐད་པར་འགྱུར། དེའི་ཕྱིར་འབྲས་བུ་རྐྱེན་མ་ཡིན་པ་ལས་བྱུང་བ་ཡང་མེད་དོ། །

[Block 236]
སྨྲས་པ། རྐྱེན་རྣམས་ནི་ཡོད་པ་ཁོ་ན་ཡིན་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། རྐྱེན་དང་རྐྱེན་མ་ཡིན་པ་ངེས་པའི་ཕྱིར་རོ། །

[Block 237]
འདི་ན་རྐྱེན་དང་རྐྱེན་མ་ཡིན་པ་ངེས་པ་མཐོང་སྟེ། འབྲུ་དག་ལས་འབྲུ་མར་ཁོ་ན་འབྱུང་གི་མར་མི་འབྱུང་ངོ་། །ཞོ་ལས་ནི་མར་ཁོ་ན་འབྱུང་གི་འབྲུ་མར་མི་འབྱུང་ངོ་། །བྱེ་མ་དག་ལས་ནི་དེ་གཉི་ག་མི་འབྱུང་ངོ་། །འདི་ལྟར༌[^175]གང་གི་ཕྱིར་འདི་དག་ནི་འདིའི་རྐྱེན་ཡིན་ནོ། །

[Block 238]
འདི་དག་ནི་འདིའི་རྐྱེན་མ་ཡིན་ནོ་ཞེས་བྱ་བ་དེ་ཡོད་པས་དེའི་ཕྱིར་རྐྱེན་འགྲུབ་བོ། །

[Block 239]
བཤད་པ། འབྲས་བུ་མེད་པས་ན། །རྐྱེན་མིན་རྐྱེན་དུ་ག་ལ་འགྱུར། །འདི་ལ་ཁྱོད་ཀྱིས་འབྲུ་མར་ལ་སོགས་པ་འབྲས་བུ་འབྱུང་བ་དང་། མི་འབྱུང་བ་རྐྱེན་དང་རྐྱེན་མ་ཡིན་པར་ངེས་པའི་རྒྱུར་སྨྲས་པ་ནི་འབྲས་བུ་སྐྱེ་བ་མི་འཐད་དོ་ཞེས་སྔར་བསྟན་ཟིན་ཏེ། འབྲས་བུ་དེ་མེད་ན་འདི་དག་ནི་འདིའི་རྐྱེན་མ་ཡིན་ནོ། །

[Block 240]
འདི་དག་ནི་འདིའི་རྐྱེན་ཡིན་ནོ། །ཞེས་བྱ་བ་དེ་འཐད་པར་ག་ལ་འགྱུར། འབྲས་བུ་ལ་ལྟོས༌[^176]ནས་དེ་གཉིས་སུ་འགྱུར་ན༌[^177]འབྲས་བུ་དེ་ཡང་མེད་དོ། །

[Block 241]
འབྲས་བུ་མེད་པས་ན་རྐྱེན་མ་ཡིན་པ་དང་རྐྱེན་དུ་ག་ལ་འགྱུར། དེ་ལྟ་བས་ན་འབྲས་བུ་ཡང་མི་འཐད་ལ་རྐྱེན་དང་རྐྱེན་མ་ཡིན་པ་དག་ཀྱང་མེད་དོ། །

[Block 242]
འབྲས་བུ་དང་རྐྱེན་དང་རྐྱེན་མ་ཡིན་པ་དག་མེད་པས་སྐྱེ་བར་བརྗོད་པ་ནི་ཐ་སྙད་ཙམ་དུ་གྲུབ་པོ། །རྐྱེན་བརྟག་པ་ཞེས་བྱ་བ་སྟེ་རབ་ཏུ་བྱེད་པ་དང་པོའོ།། །།

[Block 243 [HEADING]]
## སོང་བ་དང་མ་སོང་བ་དང་བགོམ་པ་བརྟག་པ། ^2-0

[Block 244]
སྨྲས་པ། ཁྱེད་ཀྱིས་སྐྱེ་བ་མེད་པའི་རིགས་པ་འདི་རྗེས་སུ་རབ་ཏུ་བསྟན་པས་ཁོ་བོའི་ཡིད་སྟོང་པ་ཉིད་ཉན་པ་ལ་ངོ་མཚར་སྙིང་པོ་ཅན་དུ་བྱས་ཀྱིས། ཇི་ལྟར་འཇིག་རྟེན་གྱིས༌[^178]མངོན་སུམ་གྱི་འགྲོ་བ་དང་འོང་བ་མི་འཐད་པ་དེ༌[^179]ཇེ་སྨྲོས་ཤིག །བཤད་པ།

[Block 245 [VERSE]]
རེ་ཞིག་སོང་ལ་འགྲོ་མེད་དེ། །
མ་སོང་བ་ལའང་འགྲོ་བ་མེད། །

[Block 246]
འདི་ལ་གལ་ཏེ་འགྲོ་བ་ཞིག་ཡོད་པར་གྱུར་ན། དེ་སོང་བ་ལའམ། མ་སོང་བ་ལ་ཡོད་པར་འགྱུར་གྲང་ན། དེ་ལ་རེ་ཞིག་སོང་བ་ལ་ནི་འགྲོ་བ་མེད་དོ། །

[Block 247 [VERSE]]
འགྲོ་བའི་བྱ་བ་འདས་ཟིན་པའི་ཕྱིར་རོ། །
མ་སོང་བ་ལ་ཡང་འགྲོ་བ་མེད་དེ།
འགྲོ་བའི་བྱ་བ་མ་བརྩམས་པའི་ཕྱིར་རོ། །

[Block 248]
སྨྲས་པ། དེ་ནི་དེ་བཞིན་ཏེ། སོང་བ་དང་མ་སོང་བ་ལ་འགྲོ་བ་མེད་མོད་ཀྱི། འོན་ཀྱང་བགོམ་པ་ལ་འགྲོ་བ་ཡོད་དོ། །

[Block 249]
བཤད་པ།

[Block 250 [VERSE]]
སོང་དང་མ་སོང་མ་གཏོགས་པར། །
བགོམ་པ་ཤེས་པར་མི་འགྱུར་རོ། །
--- END BLOCKS ---
