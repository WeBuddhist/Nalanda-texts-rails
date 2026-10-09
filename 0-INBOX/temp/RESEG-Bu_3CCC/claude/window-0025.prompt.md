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
[Block 876]
དེ་ལ་འདི་སྙམ་དུ་གནས་པའི་གནས་སྐབས་ན་འགག་པར་མི་འགྱུར་བ་ཉིད་དུ་སེམས་ན་དེ་བཤད་པར་བྱ་སྟེ།

[Block 877 [VERSE]]
གང་ཞིག་འགག་བཞིན་མ་ཡིན་པ། །
དེ་ནི་དངོས་པོར་མི་འཐད་དོ། །

[Block 878]
གང་གནས་པའི་གནས་སྐབས་ན་འགག་པར༌[^536]མི་འགྱུར་བ་དེ་ནི༌[^537]གནས་པའི་གནས་སྐབས་ན་དངོས་པོ་ཉིད་མ་ཡིན་པར་འགྱུར་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། དངོས་པོའི་མཚན་ཉིད་མེད་པའི་ཕྱིར་རོ། །

[Block 879]
འདི་ལྟར་འཇིག་པ་ནི་དངོས་པོའི་མཚན་ཉིད་དུ་བསྟན་པས་དེ་མེད་ན་ཇི་ལྟར་དངོས་པོ༌[^538]ཡིན་པར་འགྱུར། དངོས་པོ་མེད་ན་གང་གིས༌[^539]གནས་པར་འགྱུར། དེ་ལྟ་བས་ན་འགག་བཞིན་པ་ཉིད་ཡིན་པའི་ཕྱིར་ཡང་དངོས་པོའི་གནས་པ་མི་འཐད་དོ། །

[Block 880]
ཡང་གཞན་ཡང་།

[Block 881 [VERSE]]
དངོས་པོ་ཐམས་ཅད་དུས་ཀུན་དུ། །
རྒ་དང་འཆི་བའི་ཆོས་ཡིན་ན། །
གང་དག་རྒ་དང་འཆི་མེད་པར། །
གནས་པའི་དངོས་པོ་གང་ཞིག་ཡིན། །

[Block 882]
གང་གི་ཚེ་དངོས་པོ་ཐམས་ཅད་མི་རྟག་པ་དང་རྗེས་སུ་འབྲེལ་པའི་ཕྱིར། མི་རྟག་པ་ཉིད་ཀྱིས་རྒ་བ་དང་འཆི་བའི་ཆོས་ཅན་ཡིན་པ་དེ་ཁས་བླང་བར་བྱ་བ་དེའི་ཚེ་གང་དག་ལ་ལྟོས་ནས་གནས་པ་ཡོད་པར་བརྗོད་པ་གང་དག་རྒ་བ་དང་འཆི་བ་མེད་པར་གནས་པའི་དངོས་པོ་དེ་དག་གང་ཞིག་ཡིན་དེ་ལྟ་བས་ན་གནས་པ་ཡང་མི་འཐད་དོ། །

[Block 883]
གནས་པའི་གནས་པ་ཞེས་གང་སྨྲས་པ་དེ་ལ་བཤད་པར་བྱ་སྟེ། གནས་པ་གནས་པ་གཞན་དང་ནི། །དེ་ཉིད་ཀྱིས་ཀྱང་གནས་མི་རིགས།[^540] །གནས་པ་ནི་གནས་པ་གཞན་གྱིས་ཀྱང་གནས་པར་བྱེད་པ་མི་རིགས་པ་ཉིད་ཡིན་ལ། གནས་པ་དེ་ཉིད་གནས་པ་དེ་ཉིད་ཀྱིས་ཀྱང་གནས་པར་བྱེད་པར་མི་རིགས་པ་ཉིད་དོ། །ཇི་ལྟར་ཞེ་ན།

[Block 884 [VERSE]]
ཇི་ལྟར་སྐྱེ་བ་རང་དང་ནི། །
གཞན་གྱིས་བསྐྱེད་པ་མ་ཡིན་ཉིད། །

[Block 885]
ཇི་སྐད་དུ།

[Block 886 [VERSE]]
སྐྱེ་བ་འདི་ནི་མ་སྐྱེས་པས། །
རང་གི་བདག་ཉིད་ཇི་ལྟར་བསྐྱེད། །
ཅི་སྟེ་སྐྱེས་པས་སྐྱེད་བྱེད་ན། །
སྐྱེ༌[^541]ན་ཅི་ཞིག་སྐྱེད༌[^542]དུ་ཡོད། །

[Block 887]
ཅེས་སྨྲས་པ་དེ་བཞིན་དུ་གནས་པ་ཡང་མི༌[^543]གནས་པས་རང་གི་བདག་ཉིད་གནས་པར་བྱེད་དམ། གནས་པ༌[^544]རང་གི་བདག་ཉིད་གནས་པར་བྱེད་གྲང་ན། དེ་ལ་རེ་ཞིག་མ་གནས་པས་ནི་རང་གི་བདག་ཉིད་གནས་པར་མི་བྱེད་དོ། །

[Block 888]
ཅིའི་ཕྱིར་ཞེ་ན། མེད་པའི་ཕྱིར་ཏེ། འདི་ལྟར་མ་གནས་པ་ལ་ནི་གནས་པ་མི་འཐད་དོ། །

[Block 889]
གང་མེད་པ་དེས་རང་གི་བདག་ཉིད་གང་ཞིག་ཇི་ལྟར་གནས་པར་བྱེད། ཅི་སྟེ་གནས་པར་བྱེད་ན་ནི་རི་བོང་གི་རྭས་ཀྱང་རང་གི་བདག་ཉིད་གནས་པར་བྱེད་པ་ཞིག་ན་དེ་ནི་མི་འདོད་དེ། དེ་ལྟ་བས་ན་གནས་པ་མ་གནས་པས་རང་གི་བདག་ཉིད་གནས་པར་མི་བྱེད་དོ། །

[Block 890]
གནས་པ་གནས་པས་ཀྱང་རང་གི་བདག་ཉིད་གནས་པར་མི་བྱེད་དེ། ཅིའི་ཕྱིར་ཞེ་ན། གནས་པ་ཉིད་ཀྱི་ཕྱིར་ཏེ། གནས་པ་ལ་ཡང་གནས་པས་ཅི་ཞིག་བྱ། དེ་ལྟ་བས་ན་གནས་པ་གནས་པས་ཀྱང་རང་གི་བདག་ཉིད་གནས་པར་མི་བྱེད་དེ། གང་གནས་པར་མི་བྱེད་པ་དེ་གནས་པ་ཡིན་པར་ཇི་ལྟར་འགྱུར། དེ་ལྟར་རེ་ཞིག་གནས་པ་དེ་ཉིད་གནས་པ་དེ་ཉིད་ཀྱིས་གནས་པར་མི་བྱེད་དོ། །

[Block 891]
ཇི་ལྟར་གནས་པ་དེ་གནས་པ་གཞན་གྱིས་གནས་པར་བྱེད་པར་མི་རིགས་ཤེ་ན། ཇི་སྐད་དུ།

[Block 892 [VERSE]]
གལ་ཏེ་སྐྱེ་བ་གཞན་ཞིག་གིས། །
དེ་སྐྱེད༌[^545]ཐུག་པ་མེད་པར་འགྱུར། །
ཅི་སྟེ་སྐྱེ་བ་མེད་སྐྱེ་ན། །
ཐམས་ཅད་དེ་བཞིན་སྐྱེ་བར་འགྱུར། །

[Block 893]
ཞེས་སྨྲས་པ་དེ་བཞིན་དུ། གནས་པ་ཡང་གནས་པ་གཞན་ཞིག་གིས་གནས་པར་བྱེད་དམ། གནས་པ་གཞན་མེད་པར་གནས་པར་བྱེད་གྲང་ན། དེ་ལ་རེ་ཞིག་གནས་པ་ནི་གནས་པ་གཞན་གྱིས་གནས་པར་མི་བྱེད་དོ། །

[Block 894]
གལ་ཏེ་གནས་པ་གནས་པ་གཞན་གྱིས་གནས་པར་བྱེད་ན། དེ་ལྟ་ན་ཐུག་པ་མེད་པར་ཐལ་བར་འགྱུར་ཏེ། དེ་ཡང་གཞན་གྱིས་གནས་པར་བྱེད་ཅིང་། དེ་ཡང་གཞན་གྱིས་གནས་པར་བྱེད་པ་དེ་མཐའ་མེད་པར་འགྱུར་བས་དེ་ནི་མི་འདོད་དེ།[^546] དེ་ལྟ་བས་ན་གནས་པ་ནི་གཞན་པ༌[^547]གཞན་གྱིས་གནས་པར་མི་རིགས་སོ། །

[Block 895]
ཅི་སྟེ་གནས་པ་དེ་གནས་པ་གཞན་མེད་པར་གནས་པར་བྱེད་དོ་སྙམ་ན་དེ་ལ་བཤད་པར་བྱ་སྟེ། ཇི་ལྟར་གཞན་གནས་པར་བྱེད་པ་དེ་གནས་པ་གཞན་མེད་པར་གནས་པ་དེ་བཞིན་དུ་ཐམས་ཅད་ཀྱང་གནས་པ་གཞན་མེད་པར་གནས་པར་འགྱུར་ཏེ། གནས་པས་གཞན་གནས་པར་བྱེད་དོ་ཞེས་བྱ་བ་དོན་མེད་པའི་རྟོག་པ་འདིས་ཅི་བྱ། ཡང་ན་འདི་ལྟར་གནས་པ་ཉིད་ནི་གནས་པ་གཞན་མེད་པར་གནས་པ་ལ་དངོས་པོ་གཞན་དག་ནི་གནས་པ་གཞན་མེད་པར་མི་གནས་སོ་ཞེས་ཁྱད་པར་གྱི་གཏན་ཚིགས་བསྟན་པར་བྱ་དགོས་ན་དེ་ཡང་མི་བྱེད་པས་དེའི་ཕྱིར་གནས་པ་ནི་གནས་པ་གཞན་གྱིས་གནས་པར་མི་བྱེད་དོ། །

[Block 896]
གང་གནས་པར་མི་བྱེད་པ་དེ་ནི་གནས་པ་ཉིད་ཀྱང་མ་ཡིན་པས་དེའི་ཕྱིར་གནས་པ་ཡང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 897]
འདིར་སྨྲས་པ། འགག་པ་ནི་ཡོད་དེ། དེ་ཡང་དངོས་པོ་མ་སྐྱེས་པ་དང་མི་གནས་པ་དག་ལ་མི་འཐད་པས་སྐྱེ་བ་དང་གནས་པ་དག་ཀྱང་རབ་ཏུ་གྲུབ་པ་ཉིད་དོ། །

[Block 898]
བཤད་པ། གལ་ཏེ་འགག་བཞིན༌[^548]པ༌[^549]ཡོད་པར་གྱུར་ན། དེ་དངོས་པོ་འགག༌[^550]པའམ། མ་འགག༌[^551]པའམ། འགག་བཞིན་པའི་ཡིན་གྲང་ན། རྣམ་པ་ཐམས་ཅད་མི་འཐད་དོ། །ཅིའི་ཕྱིར་ཞེ་ན། འདི་ལྟར།

[Block 899 [VERSE]]
འགགས་པ༌[^552]འགག་པར་མི་བྱེད་དེ། །
མ་འགགས་པ༌[^553]ཡང་འགག་མི་བྱེད། །
འགག་བཞིན་པ་ཡང་དེ་བཞིན་མིན། །

[Block 900]
དེ་ལ་རེ་ཞིག་འགགས་པ་ནི་འགག་པར་མི་བྱེད་དེ། ཅིའི་ཕྱིར་ཞེ་ན། མེད་པའི་ཕྱིར་ཏེ། མེད་པ་ལ་ཅི་ཞིག་འགག་པར་འགྱུར། །མ་འགགས་པ་ཡང་འགག་པར་མི་བྱེད་དེ། ཅིའི་ཕྱིར་ཞེ་ན། འགགས་པ༌[^554]དང་མ་འགགས་པ་གཉིས་མི་མཐུན་པའི་ཕྱིར་རོ། །

[Block 901]
འགག་བཞིན་པ་ཡང་དེ་བཞིན་དུ་འགག་པར་མི་བྱེད་དེ། ཇི་ལྟར་ཞེ་ན། ཇི་སྐད་དུ། སྐྱེ་བཞིན་པ་སྐྱེད་པར་མི་བྱེད་དོ་ཞེས་སྨྲས་པ་དེ་བཞིན་ཏེ། དེས་ན་འགགས་པ༌[^555]དང་། མ་འགགས་པ༌[^556]མ་གཏོགས་པར་འགག་བཞིན༌[^557]པ་མི་སྲིད་པའི་ཕྱིར་དང་། འགག་པ་གཉིས་སུ་ཐལ་བར་འགྱུར་བ་དང་། འགག་བཞིན་པ་གཉིས་སུ་ཐལ་བར་ཡང་འགྱུར་བའི་ཕྱིར་འགག་བཞིན་པ་འགག་པར་མི་བྱེད་དོ། །

[Block 902]
ཡང་གཞན་ཡང་། འདི་ལ་འགག་བཞིན་པ་ཞེས་བྱ་བ་ནི་གང་གི་ཅུང་ཟད་ནི་འགགས་ཅུང་ཟད་ནི་མ་འགགས་པའམ། ཡང་ན་དེ་ལ་གཞན་འགགས་པའམ། མ་འགགས་པ་ཞིག་ཡིན་གྲང་ན། དེ་ལ་གལ་ཏེ་འགགས་པ་དང་མ་འགགས་པ་དེ་འགག་པས་དེ༌[^558]འགོག་པར་བྱེད་ན་ནི༌[^559]རེ་ཞིག་དེའི༌[^560]ཅུང་ཟད་འགག་པ་དེས་ནི༌[^561]བཀག་པ་མ་ཡིན་ལ། འགག་པ་དེ་འགག་བཞིན་པ༌[^562]མ་ཡིན་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། དེ་འགགས་ན་འགག་བཞིན་པ་མ་ཡིན་ཞིང་འགག་བཞིན་པ་འགོག་པར་བྱེད་དོ་ཞེས་ཀྱང་བརྗོད་པའི་ཕྱིར་རོ། །

[Block 903]
གལ་ཏེ་ཅུང་ཟད་འགགས་པ་དེ༌[^563]འགག་པ་མེད་པ་ཁོ་ནར་འགགས་ན་ནི་དེའི་ལྷག་མ་ཡང་དེ་བཞིན་དུ་འགག་པ་མེད་པ་ཁོ་ནར་འགག་པར་འགྱུར་བར་ངེས་སོ། །

[Block 904]
ཡང་ན་དེའི་གང་ཅུང་ཟད་ནི་འགག་པ་མེད་པ་ཁོ་ནར་འགགས་ལ། ཅུང་ཟད་ནི་འགགས་པས༌[^564]འགག་པར་བྱེད་པ་ལ་ཁྱད་པར་ཅི་ཡོད་པ་བརྗོད་དགོས་སོ། །

[Block 905]
ཅི་སྟེ་དེའི་གང༌[^565]ཅུང་ཟད་འགགས་པ་དེ་ཡང་འགག་པ༌[^566]ཁོ་ནར་བཀག་པ་ནི་དེ་ལྟ་ན་མ་འགགས་པ་འགགས་པས་འགག་པར་བྱེད་ཀྱི་འགག་བཞིན་པ་འགག་པར་བྱེད་པ་མ་ཡིན་ནོ། །

[Block 906]
གཞན་ཡང་། དེའི་ཕྱིར༌[^567]ཅུང་ཟད་འགགས་པ་དེ་ནི་འགགས་པས་འགག་པར་མི་བྱེད་དེ། འགགས་ཟིན་པའི་ཕྱིར་རོ། །

[Block 907]
དེས་ན། དེའི་ལྷག་མ་མ་འགགས་པ་གང་ཡིན་པ་དེ་འགགས་པས་འགག་པར་བྱེད་དོ་ཞེས་བྱ་བར་འགྱུར་ཏེ། དེ་ལ་འགག་བཞིན་པ་འགག་པར་བྱེད་དོ། །ཞེས་གང་སྨྲས་པ་དེ་ཉམས་པར་གྱུར་ཏོ། །

[Block 908]
ཅི་སྟེ་དེའི་གང་ཅུང་ཟད༌[^568]འགགས་པས་འགག༌[^569]པར་བྱེད་ན་ནི་དེ་ལ་འགག་པ་གཉིས་ཀྱིས་བྱས་པའི་ཁྱད་པར་ཅན་དུ་འགྱུར་བ་ཞིག་ན་མི་འགྱུར་ཏེ། འགག་པ༌[^570]ཟིན་པ་དེ་ལ་ནི་ཡང་འགག་པར་བྱ་བའི་ཕྱིར་བྱ་བ་འགའ་ཡང་རྩོམ་པར་མི་བྱེད་པར༌[^571]དེའི་ཕྱིར་དེ་ནི་ཡང་འགག་པར་མི་བྱེད་དོ། །

[Block 909]
དེ་ལྟ་བས་ན་འགག་བཞིན་པ་འགག་པར་བྱེད་དོ་ཞེས་བྱ་བ་དེ་ཡང་སྙིང་པོ་མེད་པ་ལ་བློས་སྙིང་པོར་བཟུང་བར་ཟད་དེ་གྱི་ནའོ། །

[Block 910]
ཡང་གཞན་ཡང་། མ་སྐྱེས་གང་ཞིག་འགག་པར་བྱེད། །གང་གི་ཚེ་ཅུང་ཟད་ཀྱང་སྐྱེ་བ་མེད་དོ། །ཞེས་བྱ་བ་དེ་སྔར་བསྟན་ཟིན་པ་དེའི་ཕྱིར༌[^572]མ་སྐྱེས་པ་གཞན་གང་ཞིག་འགག་པར་བྱེད་ཅེས་བྱ་བ་དང་། [^573]དེ་ལྟ་བས་ན་འགག་པ་ཡང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 911]
ཡང་གཞན་ཡང་། འགག་པ་ནི་གནས་པའམ། མ་གནས་པ་ལ་བརྟག་གྲང་ན། དེ་ནི་གཉི་ག་ལ་ཡང་མི་རུང་སྟེ། དེ་ལ།

[Block 912 [VERSE]]
རེ་ཞིག་དངོས་པོ་གནས་པ་ལ། །
འགག་པ་འཐད་པར་མི་འགྱུར་རོ། །

[Block 913]
གནས་པའི་བྱ་བ་སྐྱེས་པ་ལ་གནས་པ་དང་མི་མཐུན་པའི་འགག་པ་མི་འཐད་དེ། གནས་པའི་ཕྱིར་དེ་ནི་གྲགས་པ་ཡིན་ནོ། །

[Block 914]
གལ་ཏེ་མི་གནས་པ་ལ་འགག་པ་ཡོད་པས་ཉེས་པ་མེད་དོ། །

[Block 915]
ཞེ་ན།
--- END BLOCKS ---
