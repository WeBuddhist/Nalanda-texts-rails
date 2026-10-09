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
[Block 841 [VERSE]]
ཅི་སྟེ་སྐྱེ་བ་མེད་སྐྱེ་ན། །
ཐམས་ཅད་དེ་བཞིན་སྐྱེ་བར་འགྱུར། །

[Block 842]
ཇི་ལྟར་གཞན་སྐྱེད་པར་བྱེད་པ་དེ་སྐྱེད་པ༌[^511]གཞན་མེད་པར་སྐྱེས་ན་ནི་ཐམས་ཅད་ཀྱང་དེ་བཞིན་དུ་སྐྱེ་བ་གཞན་མེད་པར་སྐྱེ་བར་འགྱུར་ཏེ། སྐྱེས་པས་གཞན་སྐྱེད་པར་བྱེད་དོ། །ཞེས་བྱ་བ་དོན་མེད་པའི་རྟོག་པ་མེད་པ༌[^512]འདིས་ཅི་བྱ། ཡང་ན་འདི་ལྟར་སྐྱེ་བ་ཉིད་ནི་སྐྱེད་པ༌[^513]གཞན་མེད་པར་སྐྱེ་ལ་དངོས་པོ་གཞན་དག་ནི་སྐྱེད་པ༌[^514]གཞན་མེད་པར་མི་སྐྱེའོ། །ཞེས་ཁྱད་པར་གྱི་གཏན་ཚིགས་བསྟན་པར་བྱ་དགོས་ན་དེ་ཡང་མི་བྱེད་པས༌[^515]དེའི་སྐྱེ་བས་སྐྱེ་བཞིན་པ་གཞན་སྐྱེད༌[^516]དོ། །ཞེས་བྱ་བ་དེ་གྱི་ནའོ། །

[Block 843]
ཡང་གཞན་ཡང་། འདི་ལ༌[^517]དངོས་པོ་འགའ་ཞིག་སྐྱེ་བར་འགྱུར་ན་དེ་ཡོད་པའམ་མེད་པ་ཞིག་སྐྱེ་བར་འགྱུར་གྲང་ན། དེ་ལ།

[Block 844 [VERSE]]
རེ་ཞིག་ཡོད་དང་མེད་པ་ཡང་། །
སྐྱེ་བར་རིགས་པ་མ་ཡིན་ནོ། །

[Block 845]
རེ་ཞིག་ཡོད་པ་ནི་སྐྱེ་བར༌[^518]རིགས་པ་མ་ཡིན་ཏེ། སྐྱེ་བར་བརྟག་པ་དོན་མེད་པ་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 846]
འདི་ལྟར་ཡོད་པ་ལ་ཡང་སྐྱེ་བས་ཅི་ཞིག་བྱ། མེད་པ་ཡང་སྐྱེ་བར་རིགས་པ་མ་ཡིན་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། མེད་པ་ཉིད་ཀྱི་ཕྱིར་ཏེ། དེ་ལ་ཅི་ཞིག་སྐྱེ་བར་འགྱུར། ཅི་སྟེ་མེད་པ་སྐྱེ་བར་འགྱུར་ན་ནི་རི་བོང་གི་རྭ་ཡང་སྐྱེ་བར་འགྱུར་ལ། ཉེས་པ་ཟད་པ་རྣམས་ལ༌[^519]ཡང་ཉེས་པ་སྐྱེ་བར་འགྱུར་བ༌[^520]དེ་ནི་མི་འདོད་དེ། དེ་ལྟ་བས་ན་མེད་པ་ཡང་སྐྱེ་བར་རིགས་པ་མ་ཡིན་ནོ། །

[Block 847]
དེ་ལ་འདི་སྙམ་དུ་ཡོད་མེད་གཅིག་སྐྱེ་བར་སེམས་ན། བཤད་པ། ཡོད་མེད་ཉིད་ཀྱང་མ་ཡིན་ཏེ། ཡོད་མེད་ཀྱང་སྐྱེ་བར་རིགས་པ༌[^521]མ་ཡིན་ནོ། །

[Block 848]
གལ་ཏེ་ཇི་ལྟར་ཞེ་ན། བཤད་པ། གོང་དུ་བསྟན་པ་ཉིད་ཡིན་ནོ། །

[Block 849]
དེ་ནི་གོང་དུ།

[Block 850 [VERSE]]
རེ་ཞིག་ཡོད་དང་མེད་པ་ཡང་། །
སྐྱེ་བར་རིགས་པ་མ་ཡིན་ནོ། །

[Block 851]
ཞེས་བསྟན་པ་ཡིན་ཏེ། ཡོད་མེད་ནི་གཉིས་ལ་སྙེགས་པས་དེ་གཉིས་ནི་དགག་པ་སྔ་མས་བཀག་པ་ཉིད་ཡིན་ནོ། །

[Block 852]
ཡང་ན་ཡོད་པ་དང་མེད་པ་དང་ཡོད་མེད་དག་ཇི་ལྟར་སྐྱེ་བར་རིགས་པ་མ་ཡིན་པ་དེ་ནི།

[Block 853]
དང་པོ་ཁོ་ན༌[^522]བསྟན་ཟིན་ཏོ།[^523] །གང་དུ་ཞེ་ན།

[Block 854 [VERSE]]
གང་ཚེ་ཆོས་ནི་ཡོད་པ་དང་། །
མེད་དང་ཡོད་མེད་མི་བསྒྲུབ་པ། །
ཇི་ལྟར་སྒྲུབ་བྱེད་རྒྱུ་ཞེས་བྱ། །
དེ་ལྟ་ཡིན་ན་མི་རིགས་སོ། །

[Block 855]
ཞེས་བྱ་བ་དེར་རོ། །

[Block 856]
ཡང་གཞན་ཡང་།

[Block 857 [VERSE]]
དངོས་པོ་འགག་བཞིན་ཉིད་ལ་ནི། །
སྐྱེ་བ་འཐད་པར་མི་འགྱུར་རོ། །

[Block 858]
འདི་ལ་ཁྱོད་ཀྱིས་དངོས་པོ་སྐྱེ་བཞིན་པ་སྐྱེད་པར་བྱེད་དོ་ཞེས་སྨྲས་པས་དངོས་པོ་སྐྱེ་བཞིན་པ་ལ་འགག་པ་ཡང་ཡོད་པར་འགྱུར་རོ། །ཅིའི་ཕྱིར་ཞེ་ན། དངོས་པོ་ནི་འཇིག་པའི་མཚན་ཉིད་ཅན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 859 [VERSE]]
དངོས་པོ་འགག་བཞིན་པ་ལ་ནི། །
སྐྱེ་བ་འཐད་པར་མི་འགྱུར་ཏེ། །

[Block 860]
འདི་ལྟར་སྐྱེ་བཞིན་པ་མངོན་པར་འཕེལ་བ་ལ་སྐྱེ་བ་ཡིན་ལ། དེ་ཡང་འཇིག་པ༌[^524]ཟད་པར་འགྱུར་བས་ཟད་པ་ནི་སྐྱེ་བར་མི་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 861]
ཅི་སྟེ་སྐྱེ་བཞིན་པའི་གནས་སྐབས་ན་འགག་པར་མི་འགྱུར་བ་ཉིད་དོ་སྙམ་ན། དེ་ལ་བཤད་པར་བྱ་སྟེ།

[Block 862 [VERSE]]
གང་ཞིག་འགག་བཞིན་མ་ཡིན་པ། །
དེ་ནི་དངོས་པོར་མི་འཐད་དོ། །

[Block 863]
གལ་ཏེ་དངོས་པོ་སྐྱེ་བཞིན་པ་ཉིད་ན་འགག་པར་མི་འགྱུར་བ༌[^525]སྐྱེ་བཞིན་པ་ཉིད་དངོས་པོ་ཉིད་མ་ཡིན་པར་འགྱུར་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། དངོས་པོའི་མཚན་ཉིད་མེད་པའི་ཕྱིར་རོ། །

[Block 864]
འདི་ལྟར་འཇིག་པ་ནི་དངོས་པོའི་མཚན་ཉིད་དུ་བསྟན་པས་དེ་མེད་ན་ཇི་ལྟར་དངོས་པོ་ཡིན་པར་འགྱུར། དེ་ལྟར་ཡིན་ན་དངོས་པོ་སྐྱེ་བཞིན་པ་སྐྱེད་པར་བྱེད་དོ་ཞེས་གང་སྨྲས་པ་དེ་ཉམས་པ་དང་། དངོས་པོ་མེད་པ་སྐྱེ་བཞིན་པ་སྐྱེད་པར་བྱེད་དོ་ཞེས་བྱ་བར་ཡང་ཐལ་བར་འགྱུར་ཏེ། དེ་ལྟ་བས་ན་སྐྱེ་བས་གཞན་སྐྱེད་པར་བྱེད་དོ་ཞེས་བྱ་བ་དེ་ཡང་མི་འཐད་དོ། །

[Block 865]
གང་རང་གི་བདག་ཉིད་ཀྱང་སྐྱེད་པར་མི་བྱེད་ལ། །གཞན་གྱི་བདག་ཉིད་ཀྱང་སྐྱེད་པར་མི་བྱེད་པ་དེ་སྐྱེ་བ་ཡིན་པར་ཇི་ལྟར་འགྱུར་ཏེ། དེ་ལྟ་བས་ན་སྐྱེ་བ་ནི་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 866]
འདིར་སྨྲས་པ། གནས་པ་ནི་ཡོད་དེ། དེ་ཡང་དངོས་པོ་མ་སྐྱེས་པ་ལ་མི་འཐད་པས་སྐྱེ་བ་ཡང་རབ་ཏུ་གྲུབ་པ་ཉིད་དོ། །

[Block 867]
བཤད་པ། འདི་ལ་དངོས་པོ་གང་ཞིག་གནས་པར་འགྱུར་ན་དེ་གནས་པ་གནས་སམ། མ་གནས་པ་གནས་སམ། གནས་བཞིན་པ་གནས་གྲང་ན། དེ་ལ།

[Block 868 [VERSE]]
དངོས་པོ་གནས་པ་མི་གནས་ཏེ། །
དངོས་པོ་མ༌[^526]གནས་གནས་པ་མིན། །
གནས་བཞིན་པ་ཡང་མི་གནས་ཏེ། །

[Block 869]
རེ་ཞིག་དངོས་པོ་གནས་པ་ནི་གནས་པར་མི་བྱེད་དེ། [^527]གནས་པ་ལ་ཡང་གནས་པས༌[^528]ཅི་བྱ། གནས་པ་གཉིས་སུ་ཐལ་བར་འགྱུར་ཏེ།[^529] གང་དང་ལྡན་པས་གནས་པར་བྱེད་དོ་ཞེས་བྱ་བར་འགྱུར་བའོ། །

[Block 870]
དེ་ལྟར་གྱུར་ན་གནས་པ་པོ་ཡང་གཉིས་སུ་ཐལ་བར་འགྱུར་བས་དེ་ནི་མི་འདོད་དོ། །

[Block 871]
དངོས་པོ་མ་གནས་པ་ཡང་གནས་པར་མི་བྱེད་དེ། ཅིའི་ཕྱིར་ཞེ་ན། གནས་པ་དང་གནས་པ་མ་ཡིན་པ༌[^530]གཉིས་མི་མཐུན་པའི་ཕྱིར་རོ། །

[Block 872]
གནས་བཞིན༌[^531]ཡང་གནས་པར་མི་བྱེད་དེ། ཅིའི་ཕྱིར་ཞེ་ན། གནས་པ་དང་མ་གནས་པ་མ་གཏོགས་པར་གནས་བཞིན་པ་མི་སྲིད་པའི་ཕྱིར་དང་། གནས་པ་གཉིས་སུ་ཐལ་བར་འགྱུར་བ་དང་། གནས་པ་པོ་ཡང་གཉིས་སུ་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 873]
ཡང་གཞན་ཡང་། མ་སྐྱེས་གང་ཞིག་གནས་པར་བྱེད། །གང་གི་ཚེ་རིགས་པ་སྔོན་དུ་བཏོང་བས༌[^532]སྐྱེ་བ་མེད་པ་ཉིད་དོ་ཞེས་བྱ་བ༌[^533]བསྟན་ཟིན་པ་དེའི་ཚེ་མ་སྐྱེས་པ་གཞན་གང་ཞིག་གནས་པར་བྱེད་ཅེས་བྱ་བ། [^534]ཡང་གཞན་ཡང་།

[Block 874 [VERSE]]
དངོས་པོ་འགག་བཞིན་ཉིད་ལ་ནི། །
གནས་པ་འཐད་པར་མི་འགྱུར་རོ། །

[Block 875]
དངོས་པོ་འགག་བཞིན་པ་ལ་གནས་པ་འཐད་པར་མི་འགྱུར་རོ། །ཅིའི་ཕྱིར་ཞེ་ན། གནས་པ་དང་འགག་པ་གཉིས་སུ༌[^535]མི་མཐུན་པའི་ཕྱིར་རོ། །

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
--- END BLOCKS ---
