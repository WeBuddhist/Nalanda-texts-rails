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
[Block 1086]
ཉེ་བར་ལེན་པ་པོ་དེ་ཡོད་ན་ཉེ་བར་བླང་བ་ཡང་ལྟོས་པས་གདགས་སུ་ཡོད་པ་ཡིན་ན་དེ་ལ་ཁྱོད་ཅི་ཟེར། བཤད་པ།

[Block 1087 [VERSE]]
ལྟ་དང་ཉན་ལ་སོགས་པ་དང་། །
ཚོར་བ་ལ་སོགས་ཉིད་ཀྱི་ནི། །
སྔ་རོལ་དངོས་པོ་གང་གནས་པ། །
དེ་ནི་གང་གིས་གདགས་པར་བྱ། །

[Block 1088]
འདི་ལ་ལྟ་བ་དང་ཉན་པ་ལ་སོགས་པ་དང་། ཚོར་བ་ལ་སོགས་པ་དག་གིས་ལྟ་བ་པོ་དང་། ཉན་པ་པོ་དང་། ཚོར་བ་པོ་ཞེས་དངོས་པོ་གདགས་པར་བྱ་བ་ཡིན་ན་ལྟ་བ་ལ་སོགས་པ་དང་། ཚོར་བ་ལ་སོགས་པ་དག་གི་སྔ་རོལ་ན་ལྟ་བ་ལ་སོགས་པ་དག་གང་གི་ཉེ་བར་བླང་བ་ཞེས་བརྗོད་པའི་དངོས་པོ་ཡོད་དོ། །ཞེས་བརྟག་པའི་དངོས་པོ་དེ་འདི་ལྟར་གནས་ཏེ། ཡོད་དོ་ཞེས་གང་གིས་གདགས་པར་བྱ།

[Block 1089]
སྨྲས་པ། དེ་ནི་ལྟ་བ་ལ་སོགས་པ་དག་མེད་པར་ཡང་རང་ཉིད་ཀྱིས་རབ་ཏུ་གྲུབ་པར་ཡོད་དོ། །

[Block 1090]
བཤད་པ།

[Block 1091 [VERSE]]
ལྟ་ལ་སོགས་པ་མེད་པར་ཡང་། །
གལ་ཏེ་དེ་ནི་གནས་གྱུར་ན། །
དེ་མེད་པར་ཡང་དེ་དག་ནི། །
ཡོད་པར་འགྱུར་བར་ཐེ་ཚོམ་མེད། །

[Block 1092]
ལྟ་བ་ལ་སོགས་པ་དག་མེད་པར་ཡང་གལ་ཏེ་དངོས་པོ་དེ་རང་ཉིད་ཀྱིས་རབ་ཏུ་གྲུབ་ཅིང་གནས་པ་ཡོད་དོ། །ཞེས་བརྗོད་ན། དངོས་པོ་དེ་མེད་པར་ཡང་ལྟ་བ་ལ་སོགས་པ་དེ་དག་རང་ཉིད་ཀྱིས་རབ་ཏུ་གྲུབ་ཅིང་གནས་པ་ཡོད་པར་འགྱུར་བར་ཐེ་ཚོམ་མེད་དོ། །

[Block 1093]
སྨྲས་པ། ལྟ་བ་ལ་སོགས་པ་དག་ཀྱང་དེ་མེད་པར་གནས་པར་གྱུར་ན་སྐྱོན་ཅི་ཡོད། བཤད་པ། ཐམས་ཅད་སྐྱོན་ཉིད་དུ་འགྱུར་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། ལྟ་བ་ལ་སོགས་པ་དག་མེད་པའི་དངོས་པོ་གསལ་བར་བྱེད་པ་མེད་པར་གནས་པ་མེད་པར་འགྱུར་བ་དང་། དེ་མེད་ན་ལྟ་བ་ལ་སོགས་པ་དག་ཀྱང་གསལ་བར་བྱེད་པ་མེད་པར་གནས་པར་འགྱུར་བའི་ཕྱིར་རོ།[^680] །གང་གི་ཕྱིར་དེ་དག་ནི།

[Block 1094 [VERSE]]
ཅི་ཡིས་གང་ཞིག་གསལ་བར་བྱེད། །
གང་གིས་ཅི་ཞིག་གསལ་བར་བྱེད། །

[Block 1095]
ལྟ་བ་ལ་སོགས་པ་ཅི་ཞིག་པོ་དག་གིས་དངོས་པོ་གང་ཞིག་ལྟ་བ་པོ་དང་ཉན་པ་པོ་དང་ཚོར་བ་པོ་དང་ཞེས་གསལ་བར་བྱེད་དེ། གསལ་བར་བྱེད་ཅེས་བྱ་བ་ནི། མངོན་པར་བྱེད་པ་དང་། གཟུང་བར་བྱེད་པ་དང་། ཤེས་པར་བྱེད་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1096]
དངོས་པོ་གང་ཞིག་པོས་ཀྱང་ལྟ་བ་ལ་སོགས་པ་ཅི་ཞིག་པོ་དག་འདི་ནི་ལྟ་བའོ། །

[Block 1097]
འདི་ནི་ཉན་པའོ། །

[Block 1098]
འདི་ནི་ཚོར་བའོ། །ཞེས་གསལ་བར་བྱེད་དོ། །

[Block 1099]
དེ་ལྟར་གང་གི་ཕྱིར་ལྟ་བ་ལ་སོགས་པ་དག་གིས་དངོས་པོ་གསལ་བར་བྱེད་པ།[^681] དངོས་པོས་ཀྱང་ལྟ་བ་ལ་སོགས་པ་དག་གསལ་བར་བྱེད་པ་དེའི་ཕྱིར།

[Block 1100 [VERSE]]
ཅི་མེད་གང་ཞིག་ག་ལ་ཡོད། །
གང་མེད་ཅི་ཞིག་ག་ལ་ཡོད། །

[Block 1101]
ལྟ་བ་ལ་སོགས་པ་ཅི་ཞིག་པོ་དག་མེད་ན་གསལ་བར་བྱེད་པ་མེད་པའི་དངོས་པོ་གང་ཞིག་པོ་གནས་པས་གནས༌[^682]པར་འགྱུར་བ་ག་ལ་ཡོད། དངོས་པོ་གང་ཞིག་པོ་མེད་ན་ཡང་གསལ་བར་བྱེད་པ་མེད་པའི་ལྟ་བ་ལ་སོགས་པ་ཅི་ཞིག་པོ་དག་གནས་པར་འགྱུར་བ་ག་ལ་ཡོད་དེ། དེ་ལྟ་བས་ན། ལྟ་བ་ལ་སོགས་པ་ཅི་ཞིག་པོ་དག་གི་སྔ་རོལ་ན་དངོས་པོ་གང་ཞིག་པོ་གནས་པ་མེད་དོ། །

[Block 1102]
སྨྲས་པ།

[Block 1103 [VERSE]]
ལྟ་ལ་སོགས་པ་ཐམས་ཅད་ཀྱི། །
སྔ་རོལ་གང་ཞིག་ཡོད་པ་མིན། །

[Block 1104]
ལྟ་བ་ལ་སོགས་པ་ཅི་ཞིག་པོ་ཐམས་ཅད་ཀྱི་སྔ་རོལ་ན་དངོས་པོ་གང་ཞིག་པོ་ཡོད་དོ། །ཞེས་ནི་མི་སྨྲའི། འདི༌[^683]ལྟ་བ་ལ་སོགས་པའི༌[^684]ཅི་ཞིག་པོ་དག་རེ་རེའི་སྔ་རོལ་ན་དངོས་པོ་གང་ཞིག་པོ་ཡོད་པས་དེའི་ཕྱིར་དེ་ནི།

[Block 1105 [VERSE]]
ལྟ་ལ་སོགས་པ་གཞན་དག་གིས། །
གཞན་གྱི་ཚེ་ན་གསལ་བར་བྱེད། །

[Block 1106]
གང་གི་ཕྱིར་དེ་ལྟ་བ་ལ་སོགས་པ་ཐམས་ཅད་ཀྱི་སྔ་རོལ་ན་ཡོད་པ་མ་ཡིན་གྱི། ལྟ་བ་ལ་སོགས་པ་དག་རེ་རེའི་སྔ་རོལ་ན་ཡོད་པ་དེའི་ཕྱིར་དེ་ནི་ལྟ་བ་ལ་སོགས་པ་གཞན་དང་གཞན་གྱིས་དུས་གཞན་གྱི་ཚེ་ན་ལྟ་བ་པོ་དང་ཉན་པ་པོ་དང་། ཚོར་བ་པོ་ཞེས་གསལ་བར་བྱེད་དོ། །

[Block 1107]
དེ་ལྟ་བས་ན་དེ་ནི་ལྟ་བ་ལ་སོགས་པ་དག་གི་སྔ་རོལ་ན་མེད་པ་ཡང་མ་ཡིན་ལ། གསལ་བར་བྱེད་པ་མེད་པ་ཡང་མ་ཡིན་ནོ། །

[Block 1108]
བཤད་པ། རང་གི་བློ་གྲོས་ཡང་བར་སྟོན་པར་ཟད་དེ་གྱི་ན་ཞིག་སྨྲས་སོ། །

[Block 1109 [VERSE]]
ལྟ་ལ་སོགས་པ་ཐམས་ཅད་ཀྱི། །
སྔ་རོལ་གལ་ཏེ་ཡོད་མིན་ན། །
ལྟ་ལ་སོགས་པ་རེ་རེ་ཡི། །
སྔ་རོལ་དེ་ནི་ཇི་ལྟར་ཡོད། །

[Block 1110]
ལྟ་བ་ལ་སོགས་པ་ཐམས་ཅད་ཀྱི་སྔ་རོལ་ན་གལ་ཏེ་ཡོད་པ་མ་ཡིན་ན། ལྟ་བ་ལ་སོགས་པ་རེ་རེའི་སྔ་རོལ་ན་ཡང་དེ་ཡོད་པ་མ་ཡིན་པར་ངེས་སོ། །

[Block 1111]
ཅི་སྟེ་རེ་རེའི་སྔ་རོལ་ན་ཡོད་ན་ནི་ཐམས་ཅད་ཀྱི་སྔ་རོལ་ན་ཡང་དེ་ཡོད་པར་གསལ་ལོ། །

[Block 1112]
ཅི་སྟེ་དེ༌[^685]གང་གི་ཚེ་ལྟ་བའི་སྔ་རོལ་ན་ཡོད་པ་དེའི་ཚེ་ན་ཉན་པ་ལ་སོགས་པ་དག་གི་སྔ་རོལ་ན་མེད་པ་ཡིན་ན་དེ་དག་གི་སྔ་རོལ་ན་མེད་པ་གང་ཡིན་པ་དེ་ཇི་ལྟར་ཉན་པའི་སྔ་རོལ་ན་མེད་པ་བཞིན་དུ་ལྟ་བ་སྤངས་ཏེ། ཉན་པའི་སྔ་རོལ་ན་ཡོད་པར་འགྱུར། དེ་ལྟ་བས་ན་རེ་རེའི་སྔ་རོལ་ན་ཡོད་ཀྱི། ཐམས་ཅད་ཀྱི་སྔ་རོལ་ན་མེད་དོ་ཞེས་བྱ་བ་དེ་ནི་གྱི་ནའོ། །

[Block 1113]
ཡང་གཞན་ཡང་།

[Block 1114 [VERSE]]
གལ་ཏེ་རེ་རེའི་སྔ་རོལ་ན། །
ལྟ་པོ་དེ་ཉིད་ཉན་པོ་དེ། །
ཚོར་བ་པོ་ཡང་དེ་ཉིད་འགྱུར། །
དེ་ནི་དེ་ལྟར་མི་རིགས་སོ། །

[Block 1115]
གལ་ཏེ་དེ་ལྟ་བ་ལ་སོགས་པ་རེ་རེའི་སྔ་རོལ་ན་ཡོད་པར་གྱུར་ན་དེ་ལྟ་བ་པོ་ཡང་དེ་ཉིད་ཡིན་ལ། ཉན་པ་པོ་ཡང་དེ་ཉིད་ཡིན། ཚོར་བ་པོ་ཡང་དེ་ཉིད་ཡིན་པར་འགྱུར་ཏེ། དེ་དེ་ལྟར་ན་མི་རིགས་སོ། །ཅིའི་ཕྱིར་ཞེ་ན། སྐྱེས་བུ་སྐར་ཁུང་ཐ་དད་པར་འགྲོ་བ་བཞིན་དུ་བདག་དབང་པོ་གཞན་དུ་འགྲོ་བར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་ཏེ། བདག་ནི་དབང་པོ་གཞན་གང་དུ་འགྲོ་བར་མི་འདོད་དོ། །

[Block 1116]
ཅི་སྟེ་བདག་དབང་པོ་གཞན་དུ་འགྲོ་བར་ཐལ་བ་དེར་གྱུར་ན་མི་རུང་ངོ་སྙམ་པས་ལྟ་བ་པོ་ཡང་གཞན་ཉིད་ཡིན་ལ། ཉན་པ་པོ་ཡང་གཞན་ཉིད་ཡིན། །ཚོར་བ་པོ་ཡང་གཞན་ཉིད་ཡིན་པར་རྟོག་ན། དེ་ལ་ཡང་བཤད་པར་བྱ་སྟེ།

[Block 1117 [VERSE]]
གལ་ཏེ་ལྟ་པོ་གཞན་ཉིད་ལ། །
ཉན་པ་པོ་གཞན་ཚོར་གཞན་ན། །
ལྟ་པོའི་ཚེ་ན་ཉན་པོ་ཡོད། །
བདག་ཀྱང་མང་པོ་ཉིད་དུ་འགྱུར། །

[Block 1118]
གལ་ཏེ་ལྟ་བ་པོ་ཡང་གཞན་ཉིད་ཡིན་ལ། ཉན་པ་པོ་ཡང་གཞན་ཉིད་ཡིན། ཚོར་བ་པོ་ཡང་གཞན་ཉིད་ཡིན་པར་གྱུར་ན་དེ་ལྟ་ན་ལྟ་བ་པོའི་ཚེ་ན་ཉན་པ་པོ་དང་ཚོར་བ་པོ་ཡང་ཡོད་པར་འགྱུར་ཏེ། ཇི་ལྟར་ཞེ་ན། གང་གི་ཚེ༌[^686]ལྟ་བ་ལ་སོགས་པ་རེ་རེའི་སྔ་རོལ་ན་དེ་དག་ཡོད་པར་འདོད་པའི་ཕྱིར་རོ། །

[Block 1119]
ཁོ་བོའི་ལྟ་བ་པོ་ཡང་གཞན་ཉིད་ཡིན་ལ། ཉན་པ་པོ་ཡང་གཞན་ཉིད་ཡིན། །ཚོར་བ་པོ་ཡང་གཞན་ཉིད་ཡིན་ནོ་ཞེས་ཟེར་བས། དེ་ལྟ་ན་བདག་ཀྱང་མང་པོ་ཉིད་དུ་ཐལ་བར་འགྱུར་རོ། །

[Block 1120]
ཅི་སྟེ་གཞན་ཉིད་ཀྱང་ཡིན་ལ། ལྟ་བ་པོའི་ཚེ་ན་ཉན་པ་པོ་དང་། ཚོར་བ་པོ་མེད་ན་དེ་ལྟ་ན་ཡང་བདག་མི་རྟག་པ་ཉིད་དང་། བདག་མང་པོ་ཉིད་དུ་ཡང་ཐལ་བར་འགྱུར་བས་དེ་ཡང་མི་འདོད་དོ། །

[Block 1121]
དེ་ལྟ་བས་ན་ལྟ་བ་ལ་སོགས་པ་རེ་རེའི་སྔ་རོལ་ན་ཡོད་པ་དང་། ལྟ་བ་ལ་སོགས་པ་གཞན་དང་གཞན་གྱིས་གསལ་བར་བྱེད་དོ་ཞེས་གང་སྨྲས་པ་དེ་ནི་རིགས་པ་མ་ཡིན་ནོ། །

[Block 1122]
སྨྲས་པ། ལྟ༌[^687]ལ་སོགས་པ་དག་གི་སྔ་རོལ་ན་བདག་ཡོད་པ་ཉིད་དོ། །ཅིའི་ཕྱིར་ཞེ་ན། འདི་ལ་མིང་དང་གཟུགས་ཀྱི་རྐྱེན་གྱིས་སྐྱེ་མཆེད་དྲུག་ཅེས་གསུངས་ལ། གཟུགས་ཞེས་བྱ་བ་ནི་འབྱུང་བ་ཆེན་པོ་བཞི་པོ་དག་ཡིན་པས་དེའི་ཕྱིར་འབྱུང་བའི་རྐྱེན་གྱིས་སྐྱེ་མཆེད་དྲུག་འབྱུང་ལ། འབྱུང་བ་དེ་དག་ཀྱང་བདག་གི་ཉེ་བར་བླང་བ་ཡིན་ནོ། །

[Block 1123]
དེ་ལྟ་བས་ན། འབྱུང་བ་ཉེ་བར་ལེན་པ་པོ་འབྱུང་བས་གསལ་བར་བྱས་པའི་བདག་གནས་པ་ཡོད་ན་སྐྱེ་མཆེད་དྲུག་འབྱུང་ཞིང་རིམ་གྱིས་ཚོར་བ་ལ་སོགས་པ་དག་ཀྱང་འབྱུང་བས་དེས༌[^688]ན་ལྟ་བ་ལ་སོགས་པ་དག་གི་སྔ་རོལ་ན་དངོས་པོ་གནས་པ་ཡོད་དོ་ཞེས་བྱ་བ་དེ་འཐད་དོ། །

[Block 1124]
བཤད་པ།

[Block 1125 [VERSE]]
ལྟ་དང་ཉན་ལ་སོགས་པ་དང་། །
ཚོར་བ་དག་ལ་སོགས་པ་ཡང་། །
གང་ལས་འགྱུར་བའི་འབྱུང་དེ་ལའང་། །
དེ་ནི་ཡོད་པ་མ་ཡིན་ནོ། །
--- END BLOCKS ---
