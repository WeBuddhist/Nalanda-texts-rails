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
[Block 36]
དེ་བཞིན་དུ་ཕལ་ཆེར་སྲོག་དང་ལུས་གཉིས། མེ་དང་བུད་ཤིང་གཉིས། རྒྱུ་དང་འབྲས་བུ་གཉིས། ཡོན་ཏན་དང་ཡོན་ཅན་གཉིས། ཡན་ལག་དང་ཡན་ལག་ཅན་གཉིས་ནི་དེ་ཉིད་དང་གཞན་ཉིད་ཅེས༌[^22]འགྱེད་པར་བྱེད་དོ། །

[Block 37]
དེ་བཞིན་དུ་ཁ་ཅིག་ན་རེ་ཡོན་ཏན་བྱ་བ་དང་ལྡན་པ་རྣམས་དང་རྟག༌[^23]འཁོར་ལོ༌[^24]ཞེས་ཟེར་རོ། །

[Block 38]
གཞན་དག་ན་རེ་རྡུལ་ཕྲན་དང་ཡིད་གཉིས་ནི་མི་འགྲོའོ་ཞེས་ཟེར་རོ། །

[Block 39]
གཞན་དག་ནི་སྲོག་དང་གང་ཟག་གཉིས་འགྲོ་བ་དང་ལྡན༌[^25]ཞེས་བརྗོད་དོ། །

[Block 40]
གྲུབ་ནས་གང་དུ་འགྲོ་བར་ཡང་འདོད་དོ། །

[Block 41]
དེའི་ཕྱིར་དེ་ཁོ་ན་སེམས་པ༌[^26]དང་འགྱེད་པ་རྩོམ་པའི་དབང་གིས་འགག་པ་ལ་སོགས་པ་བརྒྱད་པོ་དགག་པར་མཛད་དོ། །

[Block 42]
འདིར་སྨྲས་པ། འོ་ན་ཅིའི་ཕྱིར་འགག་པ་སྔར་བཀག་པ།[^27] སྐྱེ་བ་ཕྱིས་བཀག །སྐྱེ་བ་མེད་པ་སྔར་བརྗོད་པར་བྱ་བའི་རིགས༌[^28]སྙམ་ན། བཤད་པ། དེ་ནི་ཀླན་ཀར་མི་རུང་སྟེ། །ཅིའི་ཕྱིར་ཞེ་ན། ཡི་གེ་ལ་མཁས་པ་རྣམས༌[^29]ནི་བསྡུ་བ་ལ་སྦྱོར་བ་ལྟག་འོག་ངེས་པ་ཡོད་ཀྱི། གཞན་ལ་ནི་ངེས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 43]
འདིར་སྨྲས་པ། དེ་ལྟ་ན་ཡང་སྐྱེ་བ་ཡོད་ན་འགག་པར་འགྱུར་གྱི་མེད་ན་མི་འགྱུར་བ༌[^30]གོ་རིམས་བཞིན་དུ་སྔར་སྐྱེ་བ་མེད་པ་ཞེས་བརྗོད་པར་བྱ་བ་ཁོ་ནར་འགྱུར་རོ། །

[Block 44]
བཤད་པ། གྲོགས་པོ་འདི་ལྟར་སྐྱེ་བ་སྔ་ལ་འགག་པ་འཕྱིའོ། །ཞེས་བྱ་བར་གང་གིས་ཁོ་བོ་ཅག་ཡིད་ཆེས་པར་འགྱུར་བའི་དཔེ་འགའ་ཞིག་ཇེ་གྱིས་ཤིག་སྨྲས་པ་ཐམས་ཅད་ཀྱང་དཔེ་ཡིན་ཏེ། ཇི་ལྟར༌[^31]ཞེ་ན། རེ་ཞིག་སྐྱེ་འདི་དོན་མེད་གང་ཕྱིར་སྐྱེ་བ་ཡོད་ན་རྒ་ཤི་དང་། །ནད་དང་སྡུག་བསྔལ་བསད༌[^32]དང་བཅིངས༌[^33]ལ་སོགས་པའི་དགྲ་དག་ཡོད། །ཅེས་བྱ་བ་བཞིན་ནོ། །

[Block 45]
བཤད་པ། གང་ལ་འཆི་བ་ཡོད་པའི༌[^34]སྐྱེ་བ་གང་ཡིན་པ་དེ་ལ་ཡང་འཆི་བ་སྔོན་དུ་འགྲོ་བ་ཁོ་ན་ཡིན་པ་སྙམ། གལ་ཏེ་དེ་འཆི་བ་སྔོན་དུ་འགྲོ་བ་མ་ཡིན་ན་ནི་འཁོར་བ་ལ་ཐོག་མ་ཡོད་པར་ཐལ་བར་འགྱུར་བས། དེ་ཡང་མི་འདོད་དེ། དེའི་ཕྱིར་འཁོར་བ་ལ་ཐོག་མ་དང་ཐ་མ་མེད་པའི་ཕྱིར་སྐྱེ་བ་སྔ་ལ་འཆི་བ་འཕྱི་བའམ་འཆི་བ་སྔ་ལ་སྐྱེ་བ་འཕྱིའོ་ཞེས་བྱ་བར་བརྗོད་པར་མི་ནུས་སོ། །

[Block 46]
འོག་ནས་ཀྱང་།

[Block 47 [VERSE]]
གལ་ཏེ་སྐྱེ་བ་སྔ་གྱུར་ལ། །
རྒ་ཤི་འཕྱི་བ་ཡིན་ན་ནི། །
རྒ་ཤི་མེད་པར་སྐྱེ་བ་དང་། །
མ་ཤི་བར་ཡང་སྐྱེ་བར་འགྱུར། །

[Block 48]
ཞེས་འབྱུང་ངོ་། །སྨྲས་པ་འོ་ན། གལ་ཏེ་འཇིག༌[^35]མང་སྐྱེ་བ་མེད་ན་དོན་མེད་དེ་མི་འབྱུང་། །ཤིང་སྐྱེས་མེད་ན་ནགས་མེད༌[^36]རླུང་གིས་སྒྱེལ་བར་མི་འགྱུར་བཞིན། །ཞེས་བྱ་བ་འདིས༌[^37]ནི་དཔེ་གཞན་ཡིན་ནོ། །

[Block 49]
བཤད་པ། འདི་ལ་ཁྱད་པར་ཅི་ཡོད། སྨྲས་པ། ཁྱད་པར་ནི་འདི་ཡིན་ཏེ། གང་གི་ཕྱིར་འདི་ལ་འགག་པ་སྔོན་དུ་འགྲོ་བའི་སྐྱེ་བ་མེད་དོ།[^38] །འདི་ལྟར་ཤིང་ལྗོན་པ་གཞན་དུ་འགགས་ལ་འདིར་སྐྱེས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 50]
བཤད་པ། འདི་ལ་ཡང་ས་བོན་འགག་པ་སྔོན་དུ་འགྲོ་བ་ལས་སྐྱེ་བས་དེ་ཡང་འགག་པ་སྔོན་དུ་འགྲོ་བ་ཁོ་ན་ལས་སྐྱེ་བ་ཡིན་ནོ། །

[Block 51]
འདིར་སྨྲས་པ། དེ་ནི་མི་འདྲ་སྟེ། ཅིའི་ཕྱིར་ཞེ་ན། གཞན་ཁོ་ན་འགགས༌[^39]ལ་གཞན་ཁོ་ན་སྐྱེ་བའི་ཕྱིར་ཏེ། འདི་ལྟར་འདི་ལ་ས་བོན་འགགས༌[^40]ལ་མྱུ་གུ་སྐྱེའི་མྱུ་གུ་ཉིད་འགགས༌[^41]ལ་མྱུ་གུ་ཉིད་མི་སྐྱེ་བས་དེའི་ཕྱིར་དེ་ནི་མི་འདྲའོ། །

[Block 52]
བཤད་པ། དེ་ནི་འདྲ་བ་ཁོ་ན་སྟེ། ཅིའི་ཕྱིར་ཞེ་ན། འདི་ལྟར་སྐྱེ་བ་དང་འཆི་བ་གཉིས་ཀྱང་གང་ཁོ་ན་ཤི་བ་དེ་ཉིད་སྐྱེ་བ་མ་ཡིན་པའི་ཕྱིར་ཏེ། གལ་ཏེ་གང་ཁོ་ན་འཆི་བ་དེ་ཉིད་སྐྱེ་བར་འགྱུར་ན་ནི་དེ་ལྟ༌[^42]ན་རྟག་པའི་སྐྱོན་དུ་ཐལ་བར་འགྱུར་ཏེ། ལྷ་གང་ཡིན་པ་དེ་ཡང་ལྷ་ཁོ་ནར་འགྱུར་ལ། དུད་འགྲོ་གང་ཡིན་པ་དེ་ཡང་དུད་འགྲོ་ཁོ་ནར་འགྱུར་རོ། །

[Block 53]
དེ་ལྟ་ཡིན་ན་ལས་དང་ཉོན་མོངས་པས་བྱས་པའི་སྐྱེ་བ་དང་འགྲོ་བ་འཁྲུལ་པ་མེད་པར་འགྱུར་བས་དེ་ཡང་མི་འདོད་དེ། དེ་ནས༌[^43]གང་ཁོ་ན་འཆི་བ་དེ་ཉིད་སྐྱེ་བར་འགྱུར་རོ། །ཞེས་བྱ་བ་དེ་བརྗོད་པར་མི་ནུས་པས་དེའི་ཕྱིར་དེའི་འདྲ་བ་ཁོ་ནའོ། །

[Block 54]
འདི་ལ་གཞན་ཁོ་ན་འགག །གཞན་ཁོ་ན་སྐྱེའོ་ཞེས་པ་གང་ཡིན་པ་དེ་ཡང་མི་རིགས་ཏེ། གལ་ཏེ་ས་བོན་དང་མྱུ་གུ་གཉིས་གཞན་ཉིད་ཡིན་པར་གྱུར་ན་དེ་གཉིས་ལ་རྒྱུ་དང་འབྲས་བུའི་ཐ་སྙད་ཀྱང་མེད་པར་འགྱུར་བ་ཞིག་ན་ཐ་སྙད་ཡོད་པས་དེའི་ཕྱིར་དེ་གཉིས་གཞན་ཉིད་མ་ཡིན་ནོ། །

[Block 55]
གཞན་ཡང་འདི་ན་སྨྲ་བ་པོ་དག་ས་བོན་བཏབ་ནས་བདག་གིས་ཤིང་ལྗོན་པ་འདི་བཙུགས། བདག་གིས་བུ་འདི་བསྐྱེད་དེ། ཤིང་ལྗོན་པ་འདི་ནི་བདག་གིའོ། །

[Block 56]
བུ་འདི་ནི་བདག་གིའོ་ཞེས་ཟེར་རོ། །

[Block 57]
དེ་ལ་གལ་ཏེ་ས་བོན་དང་ཤིང་ལྗོན་པ་དང་བུ་དག་གཞན་ཉིད་ཡིན་པར་གྱུར་ན་འཇིག་རྟེན་གྱི་ཐ་སྙད་དེ་དག་མི་སྲིད་པར་འགྱུར་བ་ཞིག་ན་སྲིད་པས་དེའི་ཕྱིར་ས་བོན་དང་མྱུ་གུ་གཉིས་གཞན་ཉིད་དུ་བརྗོད་པར་མི་ནུས་ཏེ། འོག་ནས་ཀྱང་།

[Block 58 [VERSE]]
གཞན་ནི་གཞན་ལས་བརྟེན་ཏེ་གཞན། །
གཞན་མེད་གཞན་ལས་གཞན་མི་འགྱུར། །
གང་ལས་བརྟེན༌[^44]ཏེ་གང་ཡིན་པ། །
དེ་ནི་དེ་ལས་གཞན་མི་འཐད། །

[Block 59]
ཅེས་འབྱུང་ངོ་། །

[Block 60]
འདིར་སྨྲས་པ། དེ་ལྟ་ན་ཡང་ས་བོན་ཡོད་པ་ཉིད་ཡིན་ན་འགག་པར་འགྱུར་གྱིས་མེད་ན་མི་འགྱུར་བས་འདི་ཡང་སྐྱེ་བ་སྔ་ལ་འགག་པ་འཕྱི་བར་འགྱུར་རོ། །

[Block 61]
བཤད་པ། འདི་ལྟར་ས་བོན་དེ་ལ་ཡང་ས་བོན་འགག་པ་སྔོན་དུ་འགྲོ་བ་ཉིད་ཡོད་དེ། ཅིའི་ཕྱིར་ཞེ་ན། འདི་ལྟར་མྱུ་གུ་ལས་ཀྱང་ཤིང་ལྗོན་པ་གཞན་མ་ཡིན་ལ་ཤིང་ལྗོན་པ་ལས་ཀྱང་ས་བོན་གཞན་མ་ཡིན་པའི་ཕྱིར་ས་བོན་འགག་པ་སྔོན་དུ་འགྲོ་བ་ལས་མྱུ་གུ་སྐྱེ་ལ། ས་བོན་ཡང་ས་བོན་འགག་པ་སྔོན་དུ་འགྲོ་བ་ལས་སྐྱེ་སྟེ། དེ་ལྟར་སློབ་དཔོན་འཕགས་པ་ལྷས་ཀྱང་།

[Block 62 [VERSE]]
ས་བོན་དཔེ་ནི་ཇི་ལྟ་བར། །
དེ་ལ་ཐོག་མ་ཡོད་མ་ཡིན། །
དེ་ལྟར་རྒྱུ་དང་མི་ལྡན་ལས། །
སྐྱེ་བའང་སྲིད་པར་མི་འགྱུར་རོ། །

[Block 63]
ཞེས་གསུངས་སོ། །

[Block 64]
དེའི་ཕྱིར་སྐྱེ་བ་དང་འགག་པ་གཉིས་ལ་སྔ་ཕྱིའི་རྣམ་པར་བཞག་པ༌[^45]མེད་པས་ཅིའི་ཕྱིར་འགག་པ་སྔར་བཀག་ལ་སྐྱེ་བ་ཕྱིས་བཀག་ཅེས་བྱ་བ་དེ་ཀླན་ཀར་མི་རུང་ངོ་། །དེ་གཉིས་ལ་སྔ་ཕྱིའི༌[^46]རྣམ་པར་བཞག་པ་མེད་པ་དེ་ཉིད་རབ་ཏུ་བསྟན་པའི་ཕྱིར་སློབ་དཔོན་གྱིས་འདིར་འགག་པ་སྔར་གཟུང་བ་མཛད་ལ་སྐྱེ་བ་ཕྱིས་བརྟགས་སོ། །

[Block 65]
འདིར་སྨྲས་པ། རེ་ཞིག་ཇི་ལྟར་སྐྱེ་བར་བརྗོད་པ་ཐ་སྙད་ཙམ་ཡིན་པ་དེ་ལྟར་རབ་ཏུ་སྟོན་ཅིག །

[Block 66 [VERSE]]
བཤད་པ་ཏེ༌[^47]པོར་བསྟན་པར་བྱའོ། །
བདག་ལས་མ་ཡིན་གཞན་ལས་མིན། །
གཉིས་ལས་མ་ཡིན་རྒྱུ་མེད་མིན། །
དངོས་པོ་གང་དག་གང་ན་ཡང་། །
སྐྱེ་བ་ནམ་ཡང་ཡོད་མ་ཡིན། །

[Block 67]
འདི་ལ་གལ་ཏེ་དངོས་པོ་འགའ་ཞིག་སྐྱེ་བར་གྱུར་ན། དངོས་པོ་དེའི་སྐྱེ་བ་དེ་བདག༌[^48]ལས་སམ། གཞན་ལས་སམ། བདག་དང་གཞན་གཉིས་ལས་སམ། རྒྱུ་མེད་པ་ལས་འགྱུར་གྲང་ན། བརྟགས་ནས༌[^49]རྣམ་པ་ཐམས་ཅད་ལས་མི་འཐད་དོ། །ཇི་ལྟར་ཞེ་ན། བདག་ལས་ཞེས་བྱ་བ་ནི་བདག་ཉིད་ལས་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 68]
དེ་ལ་རེ་ཞིག་དངོས་པོ་རྣམས་བདག་གི་བདག་ཉིད་ལས༌[^50]སྐྱེ་བ་མེད་དེ། དེ་དག་གི་སྐྱེ་བ་དོན་མེད་པ་ཉིད་དུ་འགྱུར་བའི་ཕྱིར་དང་། སྐྱེ་བ་ཐུག་པ་མེད་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 69]
འདི་ལྟར་དངོས་པོ་བདག་གི་བདག་ཉིད་དུ་ཡོད་པ་རྣམས་ལ་ཡང་སྐྱེ་བ་དགོས་པ་མེད་དོ། །

[Block 70]
གལ་ཏེ་ཡོད་ཀྱང་ཡང༌[^51]སྐྱེ་ན་ནམ་ཡང༌[^52]མི་སྐྱེ་བར་མི་འགྱུར་བས་དེ་ཡང་མི་འདོད་དེ། དེའི་ཕྱིར་རེ་ཞིག་དངོས་པོ་རྣམས་བདག་ལས༌[^53]སྐྱེ་བ་མེད་དོ། །

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
--- END BLOCKS ---
