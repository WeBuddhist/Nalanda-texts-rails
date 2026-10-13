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
[Block 1506]
གལ་ཏེ་ཡོད་པར་གྱུར་ན་ནི་གནས་སྐབས་ཐམས་ཅད་ན་ཡོད་པར་འགྱུར་རོ། །

[Block 1507]
ཅི་སྟེ་གང་གི་ཕྱིར་བུམ༌[^971]པ་སྣམ་བུ་ལ་ལྟོས་ན༌[^972]གཞན་ཡིན་པ་དེའི་ཚེ་བུམ་པ་དེ་ལ་གཞན་ཉིད་དེ་ཡོད་པ༌[^973]སེམས་ན། དེ་ལྟ་ན་གཞན་ཉིད་ངེས་པར་མི་གནས་པར་བསྟེན་པ༌[^974]ཡིན་ཏེ། དེའི་ཕྱིར༌[^975]དངོས་པོ་ལྟོས་ནས་ཡོད་པའི་ཕྱིར་རོ། །

[Block 1508]
གཞན་ཉིད་ལ་བཞག་པ་དང་། བཙལ་བར༌[^976]ཡོད་པ༌[^977]ཡང་དམ་བཅས་པར་ཡང་འགྱུར་བས་དེ་ཡང་མི་འཐད་དེ། རང་གི་གཞུང་ལུགས་དང་འགལ་བའི་ཕྱིར་རོ། །

[Block 1509]
ཡང་གཞན་ཡང་། དངོས་པོ་གཉིས་ཡོད་ན་ཕྲད་པར་འགྱུར་གྱི་མེད་པ་ནི་མི་འགྱུར་བས་དེ་ལ་གལ་ཏེ་རེ་ཞིག༌[^978]པ་ངོ་བོ་ཉིད་ཀྱིས་གཞན་མ་ཡིན་པ་དེ་གཞན་ཉིད་དང་ལྡན་པས་ཇི་ལྟར་གཞན་དུ་འགྱུར་ཏེ། འོ་མ་དང་འདྲེས་པའི་ཆུ་ཡང་འོ་མར་མི་འགྱུར་ལ་འོ་མ་ཡང་ཆུར་མི་འགྱུར་བ་བཞིན་ནོ། །

[Block 1510]
ཅི་སྟེ་བུམ་པ་ངོ་བོ་ཉིད་ཀྱིས་གཞན་ཡིན་ན་ནི་གཞན་ལ་གཞན་ཉིད་དང་ལྡན་པ་བཙལ་ཅི་དགོས། དེ་ལྟ་བས་ན་དེ༌[^979]གཞན་ཉིད་དང་ལྡན་པས་གཞན་དུ་འགྱུར༌[^980]ཞེས་བྱ་བ་དང་། གཞན་ཉིད་གཞན་ལ་ངེས་པར་གནས་སོ་ཞེས་བྱ་བ་དེ་ནི་གྱི་ནའོ། །

[Block 1511]
སྨྲས་པ། གཞན་ཉིད་གཞན་ལ་ངེས་པར་གནས་ཀྱང་རུང་མི་གནས་ཀྱང་རུང་སྟེ། དོན་གང་ལ་གཞན་ཉིད་དུ་འདོད་པའི་གཞན་དེ་ནི་རེ་ཞིག་ཡོད་དོ། །

[Block 1512]
བཤད་པ། ཅི་ཁྱོད་འཇིག་རྟེན་རྒྱུག་པར་རྩོམ་མམ། ཁྱོད་གཞན་ཉིད་མེད་པས་གཞན་བསྒྲུབ་པར༌[^981]རྩོམ་ཀོ། །

[Block 1513 [VERSE]]
གཞན་ཉིད་ཡོད་པ་མ་ཡིན་ནོ། །
གཞན་ནམ་དེ་ཉིད་ཡོད་མ་ཡིན། །

[Block 1514]
གཞན་གྱི་དངོས་པོ་གཞན་ཉིད་ཡོད་པ་མ་ཡིན་ན་གཞན་ནམ་དེ་ཉིད་མེད་དོ་ཞེས་བསྟན་པ་ཁོ་ན་མ་ཡིན་ནམ། ཅི་སྟེ་གཞན་གྱི་དངོས་པོ་མེད་པར་ཡང་གཞན་དུ་འགྱུར་ན་ནི་ཁྱོད་ལ་གླེན་པའི་དངོས་པོ་མེད་པར་ཡང་གླེན་པར་འགྱུར་རོ། །ཅི་སྟེ་དེ་མི་འདོད་ན། འོ་ན་ནི་གཞན་གྱི་དངོས་པོ་མེད་པར་གཞན་དུ་མི་འགྱུར་རོ། །

[Block 1515]
དེའི་ཕྱིར་དེ་ལྟར་བརྟགས་ན་དངོས་པོ་ཐམས་ཅད་ལ་གཞན་ཉིད་ཇི་ལྟར་ཡང་མི་འཐད་དོ། །

[Block 1516]
གཞན་ཉིད་མེད་ན་བལྟ་བར་བྱ་བ་ལ་སོགས་པ་དང་། འདོད་ཆགས་ལ་སོགས་པ་དག་ཇི་ལྟར་ཕན་ཚུན་ལྷན་ཅིག་ཏུ་ཕྲད་པར་གྱུར།[^982] ཕྲད་པ༌[^983]མེད་ན་ཁྱོད་ཀྱི་ཕྲད་པའི་གཏན་ཚིགས་ལས་བྱུང་བའི་དངོས་པོའི་ངོ་བོ་ཉིད་འཐད་པར་ག་ལ་འགྱུར། ཅི་སྟེ་ཡང་ཁྱོད་ཀྱི་ཡིད་ལ་བསམ་པས༌[^984]གཞན་ཡང་ཡིན་ལ། དེ་ཉིད་ཀྱང་ཡིན་ནོ་སྙམ་དུ་སེམས་ན་དེ་ལྟ་ན་ཡང་ཕྲད་པ་མི་འཐད་པ་ཉིད་དོ། །ཅིའི་ཕྱིར་ཞེ་ན། གང་གི་ཕྱིར།

[Block 1517 [VERSE]]
དེ་ནི་དེ་དང་ཕྲད་པ་མེད། །
གཞན་དང་གཞན་ཡང་ཕྲད་མི་འགྱུར། །

[Block 1518]
དེ་ལ་རེ་ཞིག་དེ་ཉིད་ནི་དེ་དང་ཕྲད་པར་མི་འཐད་དེ། ཅིའི་ཕྱིར་ཞེ་ན། དེ་ཙམ་དུ་ཟད་པའི་ཕྱིར་དང་། ལྷན་ཅིག་གི་དོན་དུ་མི་འཐད་པའི་ཕྱིར་རོ། །

[Block 1519]
ཅི་སྟེ་དེ་ལྟ་ན་ཡང་འགྱུར་ན་ནི་ཅི་ཡང་མི་ཕྲད་པར༌[^985]མི་འགྱུར་བས་དེ་ཡང་མི་འདོད་དེ། དེ་ལྟ་བས་ན་དེ་ཉིད་དང་ཕྲད་པར་མི་འཐད་དོ། །

[Block 1520]
དེ་ནི༌[^986]གང་ལ་འདི་ནི་གཞན་ནོ་འདི་ཡང་གཞན་ནོ་ཞེས་བྱ་བ་དེ༌[^987]ཡོད་པ་དེ་ལ་ཡང་ཕྲད་པར་མི་འཐད་དོ། །ཅིའི་ཕྱིར་ཞེ་ན། གཞན་ཉིད་ཡིན་པ་ཁོ་ནའི་ཕྱིར་རོ། །

[Block 1521]
ཅི་སྟེ་གཞན་ཉིད་ཡིན༌[^988]ཡང་ཕྲད་ན་ནི་དེ་ལྟ་ན་ཅི་ཡང་མི་ཕྲད་པར་མི་འགྱུར་བས་དེ་ཡང་མི་འདོད༌[^989]དེ། དེ་ལྟ་བས་ན་གཞན་ཉིད་ཡིན་ན་ཡང་ཕྲད་པར་མི་འཐད་དོ། །

[Block 1522]
སྨྲས་པ། གཞན་དུ་གྱུར་པ་གཉིས་གཅིག་ཏུ་འགྱུར་བ་གང་ཡིན་པ་དེ་ནི། དཔེར་ན་འོ་མ་དང་ཆུ་གཉིས་ཕྲད་པ་དེ་བཞིན་དུ་གཞན་དང་གཞན་ཡང་ཕྲད་པར་མི༌[^990]འགྱུར་རོ། །

[Block 1523]
བཤད་པ། དེ་ལ་ཡང་དེ་ཉིད་གནས་བཞིན་ཏེ། །གང་གི་ཚེ་རེ་ཞིག་འོ་མ་དང་ཆུ་ཐ་དད་པར་གྱུར་ན༌[^991]དེའི་ཚེ་ན་ཕྲད་པ་མེད་དོ། །

[Block 1524]
[^992]ཅིའི་ཕྱིར་ཞེ་ན། ཐ་དད་པར་གྱུར་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1525]
གང་གི་ཚེ་གཅིག་ཉིད་དུ་གྱུར་པ་དེའི་ཚེ་ན་ཡང་། ཕྲད་པ་མེད་དེ། ཅིའི་ཕྱིར་ཞེ་ན། གཅིག་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1526]
སྨྲས་པ། གང་གི་ཚེ་གཅིག༌[^993]ཉིད་དུ་གྱུར་པ་ཉིད་ཕྲད་པ་ཡིན་ནོ། །

[Block 1527]
བཤད་པ། གལ་ཏེ་གཅིག་པ་ཉིད་ཡིན་ཡང་ཕྲད་པར་འགྱུར་ན་ནི་ཅི་ཡང་མི་ཕྲད་པར་མི་འགྱུར་རོ་ཞེས་མ་བཤད་དམ། དེ་ལྟ་བས་ན་དེ་ཡང་བཟང་པོ་མ་ཡིན་ནོ། །

[Block 1528]
སྨྲས་པ། གཞན་དུ་གྱུར་པ་དག་ཕྲད་བཞིན་པ་ནི༌[^994]ཕྲད་པ་ཡིན་ནོ། །

[Block 1529]
བཤད་པ། དེ་ལ་ཡང་དེ་ཉིད་གནས་བཞིན་ཏེ། གལ་ཏེ་ཕྲད་བཞིན་པ་ཞེས་བྱ་བའི་དངོས་པོ་དག་གཅིག་ཡོད་པར་གྱུར་ན་དེ་ལ་ཡང་འདི་ནི་གཞན་ནོ། །

[Block 1530]
འདི་ཡང་གཞན་ནོ་ཞེས་གཞན་ཡིན་པའི་ཕྱིར་ཕྲད་པར་མི་འཐད་དོ། །

[Block 1531]
ཅི་སྟེ་ཕྲད་བཞིན་པ་ཞེས་བྱ་བ་དེ་གཅིག་པ་ཉིད་དུ་བརྗོད་པ་ཡིན་ན་ནི་ཕྲད་བཞིན་པ་ཞེས་བྱ་བའི་ཚིག་མི་འཐད་དོ། །

[Block 1532]
གཅིག་པ་ཉིད་ནི༌[^995]ཇི་ལྟར་ཕྲད་པར་འགྱུར།

[Block 1533]
སྨྲས་པ། ཕྱེད་ཕྲད་པའི་དངོས་པོ་དག་ཕྲད་བཞིན་པ་ཞེས་བྱ་བ་དེ་དག་ལ་ཕྲད་པ་ཡོད་དོ། །

[Block 1534]
བཤད་པ། དེ་ལ་ཡང་དེ་ཉིད་ཡོད་དོ། །

[Block 1535]
གལ་ཏེ་རེ་ཞིག་དེ་དག་ཕྱེད་ཕྲད་པ་ན་ཕྱོགས་གཅིག་ཕྲད་པས་བདག་ཉིད་ཐམས་ཅད་ཕྲད་དོ་ཞེས་བྱ་བར་བརྟགས་ན་ནི་གཅིག་པ་ཉིད་ཡིན་པའི་ཕྱིར་ཕྲད་པར་མི་འཐད་དོ། །

[Block 1536]
ཅི་སྟེ་ཕྱོགས་གཅིག་ཕྲད་ཀྱང་བདག་ཉིད་ཐ་དད་པ་ཉིད་དུ་འགྱུར་ན་ནི་ཐ་དད་པའི་ཕྱིར་ཕྲད་པར་ག་ལ་འགྱུར། གལ་ཏེ་དེ་དག་ཅུང་ཟད་ཅིག་ནི་ཕྲད་ཅུང་ཟད། ཅིག་ནི་མ་ཕྲད་པ་ཡིན་ན་ནི་བདག་ཉིད་གཉིས་སུ་འགྱུར་ཏེ། དེ་དག་གི་ཕྲད་པ་གང་ཡིན་པ་དེ་ལ་ནི་གཅིག་པ་ཉིད་མ་ཡིན་པའི་ཕྱིར༌[^996]ཕྲད་པ་མེད་པའོ།[^997] །དེ་དག་གི་མ་ཕྲད་པ་གང་ཡིན་པ་དེ་ལ་ཡང་གཞན༌[^998]པའི་ཕྱིར་ཕྲད་པ་མེད་དོ། །

[Block 1537]
སྨྲས་པ། ཕྲད་བཞིན་པ་མེད་ཀྱང་སླ་སྟེ། རེ་ཞིག་ཕྲད་པ་གང་ཡིན་པ་དེ་ནི་ཡོད་དོ། །

[Block 1538]
ཕྲད་པ་ཡོད་ན་ཕྲད་པ་ཡོད་པས་ཕྲད་པ་ཡང་རབ་ཏུ་གྲུབ་པོ། །བཤད་པ། ཀྱེ་མ་རེ་བ་ཀོ་རེ་ཆེ། །གང་ལ་ཕྲད་བཞིན་པ་ཡང་མི་འཐད་དེ། ཕྲད་པར་རྩོམ་པ་ཡང་མི་འཐད་པ་དེ་ལ་ཕྲད་པ་འཐད་པར་འགྱུར་རེ་སྐན། གང་གི་ཚེ་གཅིག་ཏུ་འགྱུར་རོ་ཞེས་སྨྲས་པ་དེའི་ཚེ་གཅིག་ཡིན་ན་ཕྲད་པར་ག་ལ་འགྱུར། ཅི་སྟེ་ཕྲད་ཀྱང་གཅིག་མ་ཡིན་ན་ནི་དེ་ལྟ་ན་ཡང་གཞན་མ་ཡིན་པའི་ཕྱིར་མ་ཕྲད་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 1539]
སྨྲས་པ། ཕྲད་པ་མེད་ཀྱང་སླ་སྟེ་རེ་ཞིག་གཅིག་པ་ཉིད་ཀྱི་སྔ་རོལ་ན་གཞན་དུ་འགྱུར་བའི་དངོས་པོ་གང་ཡིན་པ་ཡོད་པ་དེ་ནི་ཕྲད་པ་པོ་སྟེ་རེ་ཞིག་ཡོད་དོ། །

[Block 1540]
བཤད་པ། ཅི་ཁྱོད་མ་ནིང་ལ་ཕྲག་དོག་ཟའམ། ཁྱོད་ཕྲད་པ་མེད་པར་ཕྲད་པ་པོ་ཡོད་པ་ཉིད་དུ་འདོད་ཀོ། །འདི་ལ་ཕྲད་པར་བྱེད་པས་ཕྲད་པའི་རྒྱུ་ལས་བྱུང་བ་ནི་ཕྲད་པ་པོ་ཡིན་ན་ཕྲད་པ་དེ་ཡང་རྣམ་པ་ཐམས་ཅད་དུ་མི་འཐད་དོ། །

[Block 1541]
དེ་མེད་ན་ཕྲད་པར་བྱེད་པ་མེད་པ༌[^999]ཕྲད་པ་པོ་ཡོད་པར་ཇི་ལྟར་འགྱུར། དེའི་ཕྱིར་དེ་ལྟར་རིགས་པ་སྔོན་དུ་བཏང་སྟེ་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་བརྟགས་ན།

[Block 1542 [VERSE]]
ཕྲད་བཞིན་པ་དང་ཕྲད་པ་དང་། །
ཕྲད་པ་པོ་ཡང་ཡོད་མ་ཡིན། །

[Block 1543]
དེ་དག་མེད་ན་ཁྱོད་ཀྱི་ཕྲད་པ་བསྟན་པའི་གཏན་ཚིགས་ལས་བྱུང་བའི་དངོས་པོའི་ངོ་བོ་ཉིད་འགྲུབ་པར་ག་ལ་འགྱུར། ཕྲད་པ་བརྟགས་པ༌[^1000]ཞེས་བྱ་བ་སྟེ། རབ་ཏུ་བྱེད་པ་བཅུ་བཞི་པའོ།། །།

[Block 1544 [HEADING]]
## དངོས་པོ་དང་དངོས་པོ་མེད་པ་བརྟག་པ། ^15-0

[Block 1545]
སྨྲས་པ། ཁྱོད་དངོས་པོ་ཡོད་པ་མི་དམིགས་པའི་ཕྱིར་དངོས་པོ་འདི་དག་ངོ་བོ་ཉིད་མེད་པ་ཡིན་པར་སེམས་ཤིང་། དངོས་པོ་རྣམས་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཞེས་བྱ་བར་ཡང་ཡོད༌[^1001]ལ་དངོས་པོ་རྣམས་ངོ་བོ་ཉིད་མེད་པར་ཡང་སྨྲ་ན། ཇི་ལྟར་དངོས་པོ་བྱུང་བ་ཡང་ཡིན་ལ། ངོ་བོ་ཉིད་མེད་པ་ཡང་ཡིན་པར་འགྱུར། གལ་ཏེ་རྒྱུ་དང་རྐྱེན་རྣམས་ལས་དངོས་པོ་རྣམས་ཀྱི་ངོ་བོ་ཉིད་ཁོ་ན་མི་འབྱུང་ན། དེ་ལས་གཞན་ཅི་ཞིག་འབྱུང་བར་འགྱུར།[^1002] གལ་ཏེ་རྒྱུ་སྤུན་དག་ལས་སྣམ་བུའི་ངོ་བོ་ཉིད་ཁོ་ན་མི་འབྱུང་ན་ཅི་རྒྱུ་སྤུན་གྱི་ངོ་བོ་ཉིད་དག༌[^1003]ཁོ་ན་འབྱུང་ངམ། ཅི་སྟེ་ཅི་ཡང་མི་འབྱུང་ན་ནི་འབྱུང་ཞེས་ཀྱང་ཇི་སྐད་དུ་བརྗོད།[^1004] །
--- END BLOCKS ---
