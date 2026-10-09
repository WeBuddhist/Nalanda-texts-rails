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
[Block 71]
གཞན་ལས་ཀྱང་སྐྱེ་བ་མེད་དེ། [^54]ཅིའི་ཕྱིར་ཞེ་ན། ཐམས་ཅད་ལས་ཐམས་ཅད་སྐྱེ་བར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 72]
བདག་དང་གཞན་གཉིས་ལས་ཀྱང་སྐྱེ་བ་མེད་དེ། གཉི་གའི་སྐྱོན་དུ་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ།[^55] །རྒྱུ་མེད་པ་ལས་ཀྱང་སྐྱེ་བ་མེད་དེ། རྟག་ཏུ་ཐམས་ཅད་ལས་ཐམས་ཅད་སྐྱེ་བར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་དང་། རྩོམ་པ་ཐམས་ཅད་དོན་མེད་པ་ཉིད་ཀྱི་སྐྱོན་དུ་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 73]
དེ་ལྟར་གང་གི་ཕྱིར་དངོས་པོ་སྐྱེ་བ་རྣམ་པ་ཐམས་ཅད་དུ་མི་འཐད་པས༌[^56]དེའི་ཕྱིར་སྐྱེ་བ་མེད་པས་སྐྱེ་བར་བརྗོད་པ་ནི་ཐ་སྙད་ཙམ་ཡིན་ནོ། །

[Block 74]
སྨྲས་པ། དངོས་པོ་རྣམས་བདག་ལས་སྐྱེ་བ་མེད་དེ། འདི་ལྟར་མྱུ་གུ་དེ༌[^57]ཉིད་ལས་ཇི་ལྟར་སྐྱེ་ཞེས་བཤད་པ་གང་ཡིན་པ་དང་། བདག་ལས་སྐྱེ་བ་མེད་ན་བདག་དང་གཞན་གཉིས་ལས༌[^58]སྐྱེ་བ་དེ་ཡང་མི་རིགས་ཏེ། ཕྱོགས་གཅིག་ཉམས་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་དང་། འདི་ལྟར་རྒྱུ་མེད་པ་ལས་སྐྱེའོ་ཞེས་བྱ་བའི་ཕྱོགས་དེ་ནི་ཐ་ཆད་ཡིན་པས་དེ་དག་ནི་རེ་ཞིག་ཁས་མི་ལེན་ཏོ། །

[Block 75]
དངོས་པོ་རྣམས་གཞན་ལས་སྐྱེ་བ་མེད་པ་ཁོ་ནའོ། །ཞེས་བྱ་བ་དེ་ངེས་པར་གཟུང༌[^59]སྟེ་བཤད་པ་གང་ཡིན་པ་དེ་ལ་སྨྲ་བར་བྱ་སྟེ།

[Block 76 [VERSE]]
རྐྱེན་རྣམས་བཞི་སྟེ་རྒྱུ་དང་ནི། །
དམིགས་པ་དང་ནི་དེ་མ་ཐག །
བདག་པོ་ཡང་ནི་དེ་བཞིན་ཏེ། །
རྐྱེན་ལྔ་པ་ནི་ཡོད་མ་ཡིན། །

[Block 77]
ལྔ་པ་ཡོད་པ༌[^60]མ་ཡིན་ཞེས་བྱ་བས་ནི་སློབ་དཔོན་ཁ་ཅིག་གིས་རྐྱེན་བཞི་པོ་འདི་ལས་གཞན་གང་དག་ཐ་སྙད་དུ་བརྗོད་པ་དེ་དག༌[^61]ཐམས་ཅད་ཀྱང་རྐྱེན་བཞི་པོ་འདི་དག་ཏུ་འདུས་སོ། །ཞེས་ངེས་པར་འཛིན་པར་བྱེད་དོ། །

[Block 78]
དེ་རབ་ཏུ་བསྟན་པའི་ཕྱིར་རྒྱུ་ལ་སོགས་པ་རྐྱེན་བཞི་པོ་དེ་དག་དངོས་པོ་རྣམས་སྐྱེད་པའི་རྐྱེན་དུ་བསྟན་ཏེ། རྐྱེན་བཞི་པོ་དེ་དག་ལས་དངོས་པོ་རྣམས་སྐྱེ་བར་འགྱུར་རོ། །

[Block 79]
གང་གི་ཕྱིར་རྐྱེན་བཞི་པོ་གཞན་དུ་གྱུར་པ་དེ་དག་ལས་དངོས་པོ་རྣམས་སྐྱེ་བར་འགྱུར་བ་དེའི་ཕྱིར་དངོས་པོ་རྣམས་གཞན་ལས་སྐྱེ་བ་མེད་པ་ཁོ་ནའོ། །ཞེས་བྱ་བ་དེ་བཟང་པོ་མ་ཡིན་ནོ། །

[Block 80]
བཤད་པ། གལ་ཏེ་ཁྱོད་ཀྱིས་རྒྱུ་ལ་སོགས་པ་རྐྱེན་བཞི་པོ་གང་དག་གཞན་ཡིན་པར་ཐ་སྙད་བཏགས་པ་དེ་དག་དངོས་པོ་རྣམས་ལས་གཞན་ཡིན་པར་གྱུར་ན་ནི་དངོས་པོ་རྣམས་གཞན་ལས་སྐྱེ་བར་ཡང་འགྱུར་བ་ཞིག་ན། དེ་དག་ནི་གཞན་ཡིན་པར་མི་འཐད་དོ། །ཇི་ལྟར་ཞེ་ན།

[Block 81 [VERSE]]
དངོས་པོ་རྣམས་ཀྱི་རང་བཞིན་ནི། །
རྐྱེན་ལ་སོགས་ལ་ཡོད་མ་ཡིན། །
བདག་གི་དངོས་པོ་ཡོད་མིན་ན། །
གཞན་གྱི་དངོས་པོ་ཡོད་མ་ཡིན། །

[Block 82]
འདི་ལ་དངོས་པོ་ཡོད་པ་རྣམས་གཅིག་ལ་གཅིག་ལྟོས༌[^62]ནས་གཞན་ཉིད་དུ་འགྱུར་བ་ནི་དཔེར་ན་ཙཻ་ཏྲ་ལས་གུབ་ཏ་གཞན་དུ་འགྱུར་ལ། གུབ་ཏ་ལས་ཀྱང་ཙཻ་ཏྲ་གཞན་དུ་འགྱུར་བ་ལྟ་བུ་ཡིན་ན། གནས་སྐབས་གང་ན་ས་བོན་ལ་སོགས་རྐྱེན་རྣམས་ཡོད་པའི་གནས་སྐབས་དེ་ན་མྱུ་གུ་ལ་སོགས་པ་དངོས་པོ་རྣམས་ཡོད་པ་མ་ཡིན་ཏེ། དེའི་ཕྱིར་རྒྱུ་ལ་སོགས་པ་རྐྱེན་རྣམས་ཡོད་པ་ན་མྱུ་གུ་ལ་སོགས་པ་དངོས་པོ་རྣམས་ཀྱི་རང་བཞིན་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 83]
དེ་རྣམས་ཀྱི་བདག་གི་དངོས་པོ་ཡོད་པ་མ་ཡིན་ན་རྒྱུ་ལ་སོགས་པ་དག་ཇི་ལྟར་གཞན་དུ་འགྱུར། [^63]དེ་ལྟ་བས་ན་རྒྱུ་ལ་སོགས་པ་རྐྱེན་རྣམས་མྱུ་གུ་ལ་སོགས་པ་དངོས་པོ་རྣམས་ལས་གཞན་ཉིད་ཡིན་པར་མི་འཐད་དོ། །

[Block 84]
དེའི་ཕྱིར་གཞན་གྱི་དངོས་པོ་མེད་པ་ཁོ་ནའི་ཕྱིར་དངོས་པོ་རྣམས་གཞན་ལས་སྐྱེའོ། །ཞེས་བྱ་བ་དེ་འཐད་པ་མ་ཡིན་ནོ། །

[Block 85]
རྐྱེན་ལ་སོགས་ལ། ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་པ་ནི་གཞན་གྱི་གཞུང་ལུགས་ཀྱང་ངེས་པར་གཟུང་བའི་ཕྱིར་ཏེ། དེས་ན་གཞན་གྱི་གཞུང་ལུགས་དག་ལ་ཡང་དངོས་པོ་རྣམས་སྐྱེ་བ་མི་འཐད་པར་རབ་ཏུ་བསྟན་པ་ཡིན་ནོ། །

[Block 86]
འདིར་སྨྲས་པ། གཟུགས་ལ་སོགས་པ་རྐྱེན་རྣམས་ཡོད་ན་རྣམ་པར་ཤེས་པ་སྐྱེ་བ་མ་ཡིན་ནམ་བཤད་པ། མ་ཡིན་ཏེ་དངོས་པོ་རྣམས་ཀྱི་སྐྱེ་བ་འདི་བརྟག་པར༌[^64]བྱའོ། །

[Block 87]
ཁྱོད་རྣམ་པར་ཤེས་པ་མ་སྐྱེས་པ་རྐྱེན་གཞན་དུ་གྱུར་པ་དག་ལས་སྐྱེ་བར་འདོད་ན། རྣམ་པར་ཤེས་པ་མ་སྐྱེས་པ་ལ་བདག་གི་དངོས་པོ་ག་ལ་ཡོད། བདག་གི་དངོས་པོ་མེད་ན་གཞན་གྱི་དངོས་པོ་ཡང་ག་ལ་ཡོད། གཞན་གྱི་དངོས་པོ་མེད་ན་དེ་མྱུ་གུ་ལ་སོགས་པ་དང་མཚུངས་པ་ཡིན་ནོ། །

[Block 88]
ཡང་ན་འདི་ནི་དོན་གཞན་ཡིན་ཏེ། དངོས་པོ་རྣམས་ཀྱི་རང་བཞིན་ནི་རྐྱེན་རྣམས་ལ་ཡང་ཡོད་པ་མ་ཡིན། རྐྱེན་རྣམས་ལས་གཞན་པ་ལ་ཡོད་པ་མ་ཡིན། གཉི་ག་ལ་ཡང་ཡོད་པ་མ་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན། སྐྱེ་བའི་རྐྱེན་དུ་བརྟག་པ༌[^65]དོན་མེད་པ་ཉིད་ཀྱི་སྐྱོན་དུ་འགྱུར་བའི་ཕྱིར་ཏེ། འདི་ལྟར་གལ་ཏེ་དངོས་པོ་རྣམས་ཀྱི་རང་བཞིན་རྐྱེན་རྣམས་ལའམ་རྐྱེན་རྣམས་ལས་གཞན་པ་ལའམ། གཉི་ག་ལ་ཡོད་པར་གྱུར་ན། ཡོད་པ་ལ་སྐྱེ་བ་ཅི་ཞིག་བྱ་སྟེ། དངོས་པོ་རང་བཞིན་གྱིས་ཡོད་པ་རྣམས་ལ་ཡང་སྐྱེ་བར་བརྟག་པ༌[^66]དོན་མེད་པ་ཉིད་དུ་འགྱུར་རོ། །

[Block 89]
ཡོད་པ་ལ་རྐྱེན་རྣམས་ཀྱིས་ཀྱང་ཅི་ཞིག་བྱ་སྟེ། རྐྱེན་དུ་བརྟག་པ༌[^67]ཡང་དོན་མེད་པ་ཉིད་དུ་འགྱུར་རོ། །

[Block 90]
དེ་ལྟ་བས་ན།

[Block 91 [VERSE]]
དངོས་པོ་རྣམས་ཀྱི་རང་བཞིན་ནི། །
རྐྱེན་ལ་སོགས་ལ་ཡོད་མ་ཡིན། །

[Block 92]
གང་རྐྱེན་ལ་སོགས་པ་ལ་ཡོད་པ་མ་ཡིན་པ་དེ་ནི་བདག་གི་དངོས་པོ་ཡོད་པ་མ་ཡིན་པ་སྟེ། དེ་དག་ལས་གཞན་དུ་ཡོངས་སུ་བརྟག༌[^68]ཏུ་མེད་པའི་ཕྱིར་རོ། །

[Block 93 [VERSE]]
བདག་གི་དངོས་པོ་ཡོད་མིན་ན། །
གཞན་གྱི་དངོས་པོ་ཡོད་མ་ཡིན། །

[Block 94]
གཞན་གྱི་དངོས་པོ་མེད་ན་སུ་ཞིག་དངོས་པོ་རྣམས་གཞན་ལས་སྐྱེ་བའོ༌[^69]ཞེས་སྨྲ་བར་རིགས།

[Block 95]
འདིར་སྨྲས་པ།[^70] དངོས་པོ་རྣམས་བདག་དང་གཞན་ལ་སོགས་པ་ལས་སྐྱེའོ་ཞེས་བྱ་བ་འདིས་ཁོ་བོ་ཅག་ལ་ཅི་བྱ་སྟེ། འདི་ལྟར་མིག་ལ་སོགས་པ་ནི་རྣམ་པར་ཤེས་པ་སྐྱེ་བར༌[^71]བྱ་བའི་རྐྱེན་ཡིན་ནོ། །

[Block 96]
དེ་ཡང་ཇི་ལྟར་ཞེ་ན། འདི་ལ་སྐྱེ་བའི་བྱ་བ་ནི་སྐྱེད་པ༌[^72]དང་སྐྱེ་བ་དང་འབྱུང་བ་སྟེ་གཙོ་ཆེར་རྣམ་པར་ཤེས་པ་ལ་འཇུག་གོ། །

[Block 97]
རྣམ་པར་ཤེས་པ་ནི་སྐྱེ་བ་ཡིན་ནོ། །

[Block 98]
འདི་ལྟར་མིག་ལ་སོགས་པ་ནི་རྣམ་པར་ཤེས་པ་སྐྱེ་བའི་བྱ་བ་དེ་སྒྲུབ་པར་བྱེད་པ་ཡིན་ཏེ། སྒྲུབ་པར་བྱེད་པ་ཡིན་པའི་ཕྱིར་རྐྱེན་ཡིན་ནོ། །

[Block 99]
དཔེར་ན་བཙོ་བའི་བྱ་བ་ནི་འཚེད་པ་དང་བཙེད་པ་སྟེ་གཙོ་ཆེར་འབྲས་ཆན་ལ་འཇུག་ཅིང་། འབྲས་ཆན་ནི་བཙོ་བ་ཡིན་ལ། མི་དང་སྣོད་དང་ཆུ་དང་མེ་དང་ཐབ་ལ་སོགས་པ་རང་རང་གི་བྱ་བ་བྱེད་པ་དག་ནི་བཙོ་བའི་བྱ་བ་དེ་སྒྲུབ་པར་བྱེད་པའི་རྐྱེན་དག་ཡིན་པར་མཐོང་བ་བཞིན་ནོ། །

[Block 100]
འདིར་བཤད་པ། བྱ་བ་རྐྱེན་དང་ལྡན་མ་ཡིན། འདི་ལ་ཁྱེད་ན་རེ་མིག་ལ་སོགས་པ་ནི་རྣམ་པར་ཤེས་པ་སྐྱེ་བའི་བྱ་བ་སྒྲུབ་པར༌[^73]བྱེད་པ་ཡིན་པའི་ཕྱིར་རྣམ་པར་ཤེས་པའི་རྐྱེན་ཡིན་ལ། དེ་ཉིད་ཀྱང་རྣམ་པར་ཤེས་པ་ལ་འཇུག་གོ་ཞེས་ཟེར་བ་ནི་བྱ་བ་བརྟགས་ན་མི་འཐད་པས་མིག་ལ་སོགས་པ་དག་དེ་སྒྲུབ་པར་བྱེད་པ་ཡིན་པར་ག་ལ་འགྱུར། གལ་ཏེ་ཇི་ལྟར་ཞེ་ན། དེའི་ཕྱིར་བཤད་པ་འདི་ལ་སྐྱེ་བའི་བྱ་བ་ནི་རྣམ་པར་ཤེས་པ་མ་སྐྱེས་པའམ་སྐྱེས་པ་ལ་འཇུག་པར་འགྱུར་གྲང་ན། དེ་ལ་རེ་ཞིག་མ་སྐྱེས་པ་ལ་ནི་མི་འཇུག་སྟེ། གནས་པ༌[^74]མེད་པའི་ཕྱིར་རོ། །

[Block 101]
འདི་ལྟར་སྐྱེ་བའི་བྱ་བ་ནི་རྣམ་པར་ཤེས་པའི་གནས་ལ་འཇུག་གི །གནས་མེད་པ་ལ་མི་འཇུག་པས་རྣམ་པར་ཤེས་པ་མ་སྐྱེས་པ་དེ་ཡང་མེད་པ་ཡིན་ལ། དེ་མེད་ན་སྐྱེ་བའི་བྱ་བ་དེ་ལ་གནས་པ་ཡོད་པར་ག་ལ་འགྱུར། རྣམ་པར་ཤེས་པ་སྐྱེས་པ་ལ་ཡང་སྐྱེ་བའི་བྱ་བ་མི་འཇུག་སྟེ། ཅིའི་ཕྱིར་ཞེ་ན། རྣམ་པར་ཤེས་པ་སྐྱེས༌[^75]ཟིན་པའི་ཕྱིར་ཏེ། འདི་ལྟར་སྐྱེས་ཟིན་པ་ལ་ནི་ཡང་སྐྱེ་བ་མེད་དོ། །

[Block 102]
དེ་ལ་འདི་སྙམ་དུ་རྣམ་པར་ཤེས་པ་སྐྱེ་བཞིན་པ་ལ་སྐྱེ་བའི་བྱ་བ་ཡོད་པར་སེམས་ན། དེ་ཡང་མི་རུང་སྟེ། ཅིའི་ཕྱིར་ཞེ་ན། སྐྱེས་པ་དང་མ་སྐྱེས་པ་མ་གཏོགས་པར་སྐྱེ་བཞིན་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 103]
སྐྱེ་བ་དང་མ་སྐྱེས་པ་གཉིས་ལ་སྐྱེ་བའི་བྱ་བ་མི་འཇུག་པར་ནི་བསྟན་ཟིན་པས་དེའི་ཕྱིར་སྐྱེ་བའི་བྱ་བ་མེད་དོ། །

[Block 104]
འདིས་བཙོ་བའི་བྱ་བ་ཡང་བསལ་ཏེ། དེ་ལྟ་བས་ན་བྱ་བ་རྐྱེན་དང་ལྡན་པ་མི་འཐད་དོ། །

[Block 105]
དེ་ལ་འདི་སྙམ་དུ་རྐྱེན་དང་མི་ལྡན་པའི་བྱ་བ་ཡོད་པར་སེམས་ན། བཤད་པ། རྐྱེན་དང་མི་ལྡན་བྱ་བ་མེད། །འདི་ལྟར་རྐྱེན་དང་མི་ལྡན་པའི་བྱ་བ་མེད་དོ། །

[Block 106]
གལ་ཏེ་ཡོད་པར་གྱུར་ན་རྟག་ཏུ་ཐམས་ཅད་ལས་ཐམས་ཅད་སྐྱེ་བར་འགྱུར་རོ། །

[Block 107]
དེ་ལྟ་ཡིན་ན་རྩོམ་པ་ཐམས་ཅད་དོན་མེད་པ་ཉིད་དུ་འགྱུར་བས་དེ་ཡང་མི་འདོད་དེ། དེའི་ཕྱིར་རྐྱེན་དང་མི་ལྡན་པའི་བྱ་བ་ཡང༌[^76]མི་འཐད་དོ། །

[Block 108]
འདིར་སྨྲས་པ།

[Block 109 [VERSE]]
རེ་ཞིག་རྐྱེན་རྣམས་ནི་ཡོད་དོ། །
དེ་དག་ཡོད་པས་དངོས་པོ༌[^77]འགྲུབ་པོ། །
དེ་གྲུབ་པས་སྐྱེ་བ་འགྲུབ་པོ། །

[Block 110]
བཤད་པ། བྱ་བ་མི་ལྡན་རྐྱེན་མ་ཡིན། །གང་དག་ལ་བྱ་བ་མེད་པ་དེ་དག་ནི་རྐྱེན་མ་ཡིན་ནོ། །ཇི་ལྟར་ཞེ་ན། མིག་ལ་སོགས་པ་ནི་སྐྱེ་བའི་བྱ་བ་སྒྲུབ་པར༌[^78]བྱེད་པས་རྣམ་པར་ཤེས་པའི་རྐྱེན་དུ་འགྱུར་ན། སྐྱེ་བའི་བྱ་བ་དེ་མི་འཐད་པར་ནི་སྔར་རབ་ཏུ་བསྟན་ཟིན་ཏོ། །
--- END BLOCKS ---
