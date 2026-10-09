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
[Block 1786]
དེ་ལྟར་གང་གི་ཕྱིར་ལས་དང་འབྲས་བུར༌[^1171]འབྲེལ་པ་དེ་ཡོད་པ༌[^1172]ལ་སོགས་པ་ཐ་དད་པས་གནས་སྐབས་སྣ་ཚོགས་ཡིན་ལ། གནས་སྐབས་སྣ་ཚོགས་ཡིན་ཡང་དེ་ཉིད་དང་གཞན་ཉིད་དུ་བརྗོད་པར་བྱ་བ་མ༌[^1173]ཡིན་པ་དེའི་ཕྱིར་ངོ་བོ་ཉིད་ངེས་པར་མི་གནས་པ་དང་བརྗོད་པར་བྱ་བ་མ་ཡིན་པས། སྟོང་པ་ཉིད་ཀྱང་འཐད་པ་ཡིན་ནོ། །

[Block 1787]
སྟོང་པ་ཉིད་ཡིན་ཡང་ཆད་པའི་སྐྱོན་དུ་ཡང་ཐལ་བར་མི་འགྱུར་རོ། །

[Block 1788]
འཁོར་བ་ཡང་འཐད་པ་ཡིན་ནོ། །

[Block 1789]
འཁོར་བ་ཡོད་ཀྱང་རྟག་པའི་སྐྱོན་དུ་ཡང་ཐལ་བར་མི་འགྱུར་རོ། །

[Block 1790]
སངས་རྒྱས་བཅོམ་ལྡན་འདས་སེམས་ཅན་རྣམས་ཀྱི༌[^1174]ལས་དང་རྣམ་པར་སྨིན་པ་མངོན་སུམ་དུ་གྱུར་པ༌[^1175]ལས་རྣམས་ཀྱི་ཆུད་མི་ཟ་བའི་ཆོས་བསྟན་པ་གང་ཡིན་པ་དེ་ཡང་འཐད་པ་ཡིན་ནོ། །

[Block 1791]
དེ་ལྟ་བས་ན་རྟག་པ་དེ་ཉིད་འདིར་འཐད་ཀྱི། མྱུ་གུའི་རྒྱུ་ལས༌[^1176]འབྲས་བུ་འགྲུབ་པ་བཞིན་དུ་ལས་ཀྱི་འབྲས་བུ་འགྲུབ་པར་རྟོགས་པ་དེ་ནི་མི་འཐད་དོ། །

[Block 1792]
བཤད་པ། ཅི་ཁྱོད་དྲི་ཟའི་གྲོང་ཁྱེར་གྱི་ར་བ་འཆོས་པས་གཡེན་སྤྱོའམ། ཁྱོད་ལས་མི་འཐད་བཞིན་དུ་ལས་ཀྱི་འབྲས་བུའི་ཕྱིར་རྩོད་ཀོ། །འདི་ལྟར་གལ་ཏེ་ཁྱེད་ཀྱིས་ལས་ངོ་བོ་ཉིད་ཀྱིས༌[^1177]ཅུང་ཟད་ཅིག་རབ་ཏུ་བསྒྲུབས་པར་གྱུར་ན་ནི་དེས་ན་ལས་ཡོད་པ་དེ་རྒྱུན་འབྲེལ་པས་སམ་ཆུད་མི་ཟ་བས༌[^1178]འབྲས་བུ་དང་འབྲེལ་པར་བསམ་པ་ཡང་རིགས་པར་འགྱུར་གྲང་ན། གང་གི་ཚེ་ལས་དེ་ཉིད་ངོ་བོ་ཉིད་ཀྱིས་མི་འཐད་པ་དེའི་ཚེ་གཞི་མེད་པའི་བསམ་པ་འདིས་ཅི་ཞིག་བྱ། དེའི་ཕྱིར་སྟོང་པ་ཉིད་དང་། [^1179]སྨྲས་པ། ལས་ཇི་ལྟར་མི་འཐད།

[Block 1793]
བཤད་པ། འདི་ལྟར། གང་ཕྱིར་ལས་ནི་སྐྱེ་མེད་པ། །གང་གི་ཕྱིར་ལས་ལ་སྐྱེ་བ་མེད་པ་ཉིད་ཡིན་པ་དེའི་ཕྱིར་མི་འཐད་དེ། འདི་ལྟར་མ་སྐྱེས་ན་ཇི་ལྟར་འཐད་པར་འགྱུར་རོ།[^1180] །སྨྲས་པ། ཅིའི་ཕྱིར་ལས་སྐྱེ་བ་མེད། བཤད་པ། གང་ཕྱིར་དངོས་ཉིད་མེད་དེའི་ཕྱིར། །གང་གི་ཕྱིར་ལས་ངོ་བོ་ཉིད་མེད་པ་དེའི་ཕྱིར་སྐྱེ་བ་མེད་དེ། འདི་ལྟར་ལས་ཀྱི་ངོ་བོ་ཉིད་ཡོད་ན་ནི་ལས་ཀྱི་སྐྱེ་བ་འདི་ཡིན་ནོ། །ཞེས་སྐྱེ་བ་ཡང་འཐད་པར་འགྱུར་ན། ལས་ཀྱི་ངོ་བོ་ཉིད་མེད་ན་ཅི་ཞིག་སྐྱེ་བར་འགྱུར། ཅི་སྟེ་སྐྱེ་ན་ཡང་ངོ་བོ་ཉིད་དུ་ནི་སྐྱེ་བར་མི་འགྱུར་རོ། །

[Block 1794]
གང་ངོ་བོ་ཉིད་དུ་སྐྱེ་བར་མི་འགྱུར་བ་དེ་ནི་ལས་ཉིད་མ་ཡིན་ཏེ། ལས་ཀྱི་ངོ་བོ་ཉིད་མེད་པའི་ཕྱིར་རོ། །

[Block 1795]
དེའི་ལས་མི་འཐད་དོ། །

[Block 1796]
སྨྲས་པ། ལས་ནི་སྐྱེ་བ་ཡོད་པ་ཉིད་དོ། །ཅིའི་ཕྱིར་ཞེ་ན། ལས་རྣམས་ཆུད་མི་ཟ་བའི་ཕྱིར་ཏེ། འདི་ལྟར་བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་ལས་རྣམས་ཆུད་ཟ་བ་མེད་དོ། །ཞེས་གསུངས་པས། གལ་ཏེ་ལས་ལ་སྐྱེ་བ་མེད་ན་ཆུད་མི་ཟ་བ་དེ་གང༌[^1181]ཡིན་པར་འགྱུར། དེ་ལྟ་བས་ན་ལས་ནི་སྐྱེ་བ་ཡོད་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 1797]
བཤད་པ། སྐྱེ་བ་ཡོད་ན་ཆུད་མི་ཟ་བ་མི་འཐད་དེ།

[Block 1798 [VERSE]]
གང་ཕྱིར་དེ་ནི་མ་སྐྱེས་པ། །
དེ་ནི་ཆུད་ཟར་མི་འགྱུར་རོ། །

[Block 1799]
བཅོམ་ལྡན་འདས་ཀྱིས་གང་ཁོ་ནའི་ཕྱིར་ལས་དེ་མ་སྐྱེས་པ་དེ་ཁོ་ནའི་ཕྱིར་ཆུད་ཟ་བར་མི་འགྱུར་རོ་ཞེས་གསུངས་སོ། །

[Block 1800]
གཞན་དུ་སྐྱེ་ན་ཇི་ལྟར་ཆུད་མི་ཟ་བར་འགྱུར། ཅི་སྟེ་འགྱུར་ན་ནི་སྐྱེས་པ་ཡང་མི་འཆི་བར་འགྱུར་བ་ཞིག་ན་སྐྱེས་པ་མི་འཆི་བར་ནི་མི་འགྱུར་རོ། །

[Block 1801]
དེ་ལྟ་བས་ན་ལས་ཀྱང་སྐྱེས་ནས་ཆུད་མི་ཟ་བར་མི་འགྱུར་རོ། །

[Block 1802]
སྨྲས་པ། གང་གི་ཚེ་ཁོ་བོས་ལས་སྐད་ཅིག་མ་ཉིད་ཡིན་པའི་ཕྱིར་འགགས་ཀྱང་ཆུད་མི་ཟ་བའི་ཆོས་ཀྱིས༌[^1182]འབྲས་བུ་འགྲུབ་པར་འགྱུར་རོ། །ཞེས་སྨྲས་པ་དེའི་ཚེ། ལས་སྐྱེས་ན༌[^1183]ཇི་ལྟར་ཆུད་མི་ཟ་བར་འགྱུར་ཞེས་བྱ་བ་འདི་གང་གི་ལན་ཡིན། བཤད་པ། དེ་ནི་འདི་ཉིད་ཀྱི་ལན་ཡིན་ཏེ། གལ་ཏེ་ཁྱོད་ཀྱིས་ལས་དེ་སྐད་ཅིག་མ་ཡིན་པའི་ཕྱིར་འགགས་ན་ཆུད་མི་ཟ་བ་དེ་གང་གི་ཡིན་ཏེ། གཞི་མེད་ན་ཆུད་མི་ཟ་བར༌[^1184]མི་འཐད་དོ། །

[Block 1803]
འདི་ལྟར་ལས་ཀྱི་ཆུད་མི་ཟ་བ་ཡིན་ན། ལས་དེ་ཡང་འགགས་ཏེ་མེད་ན། དེ་མེད་པའི་ཕྱིར་ཆུད་མི་ཟ་བ་ཡང་མེད་དེ། དེ་ལྟ་བས་ན༌[^1185]འགག་པའི་ཆུད་མི་ཟ་བ་ཞེས་བྱ་བ་དེ་ནི་འགལ་ལོ། །

[Block 1804]
སྨྲས་པ། ལས་འགགས་ན་ཡང་རྣམ་པར་སྨིན་པ་ཆུད་མི་ཟ་བས་སྐྱོན་མེད་དོ། །

[Block 1805]
བཤད་པ། དེ་ཡང་མི་འཐད་དོ། །ཅིའི་ཕྱིར་ཞེ་ན། འདི་ལ་ལས་འདོད་པ་དང་མི་འདོད་པ་དག་གི་འབྲས་བུ་འདོད་པ་དང་མི་འདོད་པ་དག་བྱེད་པ་པོས་འཐོབ་པ་ནི་རྣམ་པར་སྨིན་པ་ཞེས་བྱ་སྟེ། དེ་ཡང་ཚེ་འདིའམ་སྐྱེས་པའམ་ལན་གྲངས་གཞན་ལ་རྐྱེན་གྱི་བྱེ་བྲག་དེ་དག་གིས་མྱོང་བར་འགྱུར་བ་ཡིན་ན། མ་སྐྱེས་པ་རྐྱེན་ལ་ལྟོས་པ་རྐྱེན་ལ་རག་ལས་པ་དེ་ཆུད་མི་ཟ་བས་ཇི་ལྟར་འཛིན་པར་བྱེད་ཅི་སྟེ་དེ་སྐྱེས་པ་ཉིད་ཡིན་ན་ནི་དེས་བྱེད་པ་པོ་ལ་འབྲས་བུ་བདེ་བ་དང་སྡུག་བསྔལ་དག་མྱོང་བར་བྱ་དགོས་ཏེ། དེ་ལྟ་ཡིན་ན་ནི་དེ་ལ་ཆུད་མི་ཟ་བས་ཡང་བྱར་ཅི་ཡོད། ཅི་སྟེ་སྐྱེས་ཀྱང་རེ་ཞིག་དེས་བྱེད་པ་པོ་ལ་བདེ་བ་དང་སྡུག་བསྔལ་དག་མྱོང་བར་མི་བྱེད་ན་ནི་གང་གིས་དེ་སྐྱེས་སོ། །ཞེས་བྱ་བར་ཤེས་པར་འགྱུར་བ་དེའི་སྐྱེས་པའི་མཚན་ཉིད་གང་ཡིན། གལ་ཏེ་དེ་སྐྱེས་ཀྱང་བྱེད་པ་པོ་ལ་བདེ་བ་དང་སྡུག་བསྔལ་དག་མྱོང་བར་མི་བྱེད་ན་ནི་ཕྱིས་ཀྱང་དེས་དེ་ལ་ཅི་ཡང་བྱེད་པར་མི་འགྱུར་ཞིང་། ཕྱིས་བྱེད་པ་པོ་ལ་དེ་འབུལ་བར་འགྱུར་བ་ཡང་སུ་ཞིག་ཡིན་པར་འགྱུར། དེ་ལྟ་བས་ན་དེ་ཁོ་ནའི་དོན་རྣམ་པར་མ་ཤེས་ནས་ཆུད་མི་ཟ་བའི་ཚིག་ཙམ་ལ་དངོས་པོར་མངོན་པར་ཞི་བར༌[^1186]བྱས་ནས་མང་པོ་དང་སྣ་ཚོགས་པ་དང་སྙིང་པོ་མེད་པ་དེ་སྙེད་ཅིག་སྨྲས་སོ། །

[Block 1806]
འདི་ལྟར་ལས་ནི་ངོ་བོ་ཉིད་མེད་པ་ཁོ་ན་ཡིན་ཏེ། གང་གི་ཕྱིར་ངོ་བོ་ཉིད་མེད་པ་དེའི་ཕྱིར་མ་སྐྱེས་པ་ཡིན་ལ། གང་གི་ཕྱིར་མ་སྐྱེས་པ་དེའི་ཕྱིར་ཆུད་ཟ་བར་མི་འགྱུར་ཏེ། དེ་ནི་དེ་ལྟར་ངེས་པར་བལྟ་བར་བྱའོ། །

[Block 1807]
གཞན་དུ་ན།

[Block 1808 [VERSE]]
གལ་ཏེ་ལས་ལ༌[^1187]དངོས་ཉིད་ཡོད། །
རྟག་པར་འགྱུར་བར་ཐེ་ཚོམ་མེད། །

[Block 1809]
གལ་ཏེ་ལས་ལ་ངོ་བོ་ཉིད་ཡོད་པར་འགྱུར༌[^1188]ན། རྟག་པར་འགྱུར་བར་ཐེ་ཚོམ་མེད་དེ། འདི་ལྟར་རང་བཞིན་ནི་མི་འགྱུར་བའི་ཕྱིར་གཞན་དུ་འགྱུར་བར་མི་འཐད་དོ། །

[Block 1810]
དེའི་ཕྱིར།

[Block 1811 [VERSE]]
ལས་ནི་བྱས་པ་མ་ཡིན་འགྱུར། །
རྟག་ལ་བྱ་བ་མེད་ཕྱིར་རོ། །

[Block 1812]
ལས་རྟག་པ་ཉིད་མིན༌[^1189]ན་མ་བྱས་པ་ཉིད་དུ་ཐལ་བར་འགྱུར་རོ། །ཅིའི་ཕྱིར་ཞེ་ན། རྟག་པ་ལ་བྱ་བ་མེད་པའི་ཕྱིར་ཏེ། འདི་ལྟར་རྟག་པ་མི་འགྱུར་བའི་ཆོས་ཅན་ལ་ནི་ཡང་བྱ་བ་མི་འཐད་དོ། །

[Block 1813]
ལས་མ་བྱས་པ་རྟག་པའི་འབྲས་བུར༌[^1190]ཇི་ལྟར་རྣམ་པར་སྨིན་པར་འགྱུར་ཏེ། འདི་ལྟར་རྟག་པ་ལ་འགྱུར་བ་མི་འཐད་དོ། །

[Block 1814]
ཅི་སྟེ་ལས་རྟག་པ་མི་འགྱུར་བ་ཡིན་ཡང་དེའི་རྒྱུ་ལས་བྱུང་བའི་འབྲས་བུ་དང་ཕྲད་པར་རྟོག་ན། དེ་ལྟ་ན་ཡང་།

[Block 1815 [VERSE]]
ཅི་སྟེ་ལས་ནི་མ་བྱས་ན། །
མ་བྱས་པ་དང་ཕྲད་འཇིགས་འགྱུར། །

[Block 1816]
ཅི་སྟེ་ལས་མ་བྱས་པ་ཡིན་ཡང་འབྲས་བུ་སྐྱེད་པར༌[^1191]འགྱུར་ན། དེ་ལྟ་ན་མ་བྱས་པ་དང་ཕྲད་པས་འཇིགས་པར་འགྱུར་ཏེ། འདི་ལྟར་དེ་ལས་མི་དགེ་བ་མ་བྱས་སུ་ཟིན་ཀྱང་དེ་ལ་ཡོད་པ་ཁོ་ན་ཡིན་པས་དེས་ན་འབྲས་བུ་མི་འདོད་པ་འོང་བར་འགྱུར་བས་དེ་ལ་འཇིགས་པ་ཆེན་པོ་འབྱུང་བར་འགྱུར་རོ། །

[Block 1817]
གཞན་ཡང་།

[Block 1818 [VERSE]]
ཚངས་སྤྱོད་གནས་པ་མ་ཡིན་པའང་། །
དེ་ལ་སྐྱོན་དུ་ཐལ་བར་འགྱུར། །

[Block 1819]
ལས་མ་བྱས་པ་ཡིན་ན་དེ་ལ་སྐྱོན་ཆེན་པོ་གཞན་འདིར་ཡང་ཐལ་བར་འགྱུར་ཏེ། གང་གིས་ཚངས་པར་སྤྱོད་པ་མ་ཡིན་པ་མ་བྱས་ཀྱང་ཡོད་པའི་ཕྱིར་འགའ་ཡང་ཚངས་པར་སྤྱོད་པར༌[^1192]སྤྱོད་པ་ལ་གནས་པར་མི་འཐད་པ་དང་། གང་གིས་ཚངས་པར་སྤྱོད་པ་མ་ཡིན་པ་དེ་མ་སྤྱད་ཀྱང་དེ་ལ་ཚངས་པར་སྤྱོད་པ་ཡོད་པ་ཁོ་ནའི་ཕྱིར་ཡང་ཚངས་པར་སྤྱོད་པ་ལ་གནས་པ་དོན་མེད་པར་འགྱུར་བས་དེའི་ཕྱིར་ཡང་ཚངས་པར་སྤྱོད་པ་ལ་གནས་པ་མ་ཡིན་པར་ཐལ་བར་འགྱུར་རོ། །

[Block 1820]
དེ་བཞིན་དུ།

[Block 1821 [VERSE]]
ཐ་སྙད་ཐམས་ཅད་ཉིད་དང་ཡང་། །
འགལ་བར་འགྱུར་བར་ཐེ་ཙོམ་མེད། །

[Block 1822]
དེ་ལྟར་ལས་བྱས་པ་མ་ཡིན་ན་འཇིག་རྟེན་པ་འབྲས་བུའི་དོན་དུ་ཐ་སྙད་རྩོམ་པར་བྱེད་པ་ཞིང་ལས་དང་ཉོ་ཚོང་དང་ཕྱུགས་བཙལ་བ་དང་། རྒྱལ་པོ་ལ་བརྟེན་པ་ལ་སོགས་པ་དང་། དེ་བཞིན་དུ༌[^1193]རིགས་པ་དང་། བཟོ་དང་། སྒྱུ་རྩལ་གོམས་པར་བྱེད་པ་དང་། དེ་དག་གི་ལུང་འབོགས་པ་གང་དག་ཡིན་པ་དེ་དག་ཐམས་ཅད་ཉིད་དང་ཡང་འགལ་བར་འགྱུར་རོ། །ཅིའི་ཕྱིར་ཞེ་ན། བྱེད་པ་དང་མི་བྱེད་པ་དག་ལ་དེ་དག་གི་འབྲས་བུ་འོང་བར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 1823]
གཞན་ཡང་།

[Block 1824 [VERSE]]
བསོད་ནམས་དང་ནི་སྡིག་བྱེད་པའི། །
རྣམ་པར་དབྱེ་བའང་འཐད་མི་འགྱུར། །

[Block 1825]
ལས་མ་བྱས་པ༌[^1194]ཡིན་ན་འདི་ནི་བསོད་ནམས་བྱེད་པའོ། །
--- END BLOCKS ---
