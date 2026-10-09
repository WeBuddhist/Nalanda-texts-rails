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

[Block 916 [VERSE]]
དངོས་པོ་མི་གནས་པ་ལ་ཡང་། །
འགག་པ་མི༌[^574]འཐད་པར་མི་འགྱུར་རོ། །

[Block 917]
མི་གནས་པའི་ཕྱིར་དཔེར་ན་འགགས་པ༌[^575]བཞིན་ནོ་ཞེས་བྱ་བར༌[^576]དགོངས་སོ། །

[Block 918]
སྨྲས་པ། མངོན་སུམ་ལ་གཏན་ཚིགས་ཀྱི་ཚིག་དོན་མེད་པ་དེ་ནི་འཇིག་རྟེན་ལ་གྲགས་པ་ཡིན་ཏེ། ཇི་ལྟར་དངོས་པོ་མ་འགགས་པར་གནས་པ་རྒྱུ་འགའ་ཞིག་ཁོ་ནས་འཇིག་པར་འགྱུར་བ་དེ་ནི་གཞོན་ནུ་ཡན་ཆད་ཀྱི་མངོན་སུམ་དུ༌[^577]ཡིན་པས། དེའི་ཕྱིར་འགག་པ༌[^578]ནི་ཡོད་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 919]
བཤད་པ། དེ་ལྟ་བས་ན། འདི་ཡང་ཁྱོད་ཀྱི་བློའི་མངོན་སུམ་དུ་བྱ་བའི་རིགས་ཏེ།

[Block 920 [VERSE]]
གནས་སྐབས་དེ་ཡི༌[^579]གནས་པ་ནི། །
དེ་ཡིས་འགག་པ་ཉིད་མི་འགྱུར། །
གནས་སྐབས་གཞན་གྱིས་གནས་སྐབས་ནི། །
གཞན་གྱིས་འགག་པ་ཉིད་མི་འགྱུར། །

[Block 921]
དངོས་པོ་གནས་སྐབས་གང་དུ་འཇུག་པར་རྟག་པར༌[^580]དེའི་གནས་སྐབས་དེ་ནི་གནས་སྐབས་དེས་འགག་པ་ཉིད་དུ་མི་འགྱུར་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། གནས་སྐབས་དེ་ཡོད་པའི་ཕྱིར་རོ། །

[Block 922]
འདི་ལྟར་འོ་མའི་གནས་སྐབས་ཉིད་ཀྱིས་འོ་མ་འགག་པར་མི་འགྱུར་ཏེ། འོ་མའི་གནས་སྐབས་ཡོད་པའི་ཕྱིར་རོ། །

[Block 923]
གནས་སྐབས་གཞན་གྱིས་ཀྱང་གནས་སྐབས་གཞན་འགག་པ་ཉིད་དུ་མི་འགྱུར་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། གཞན་ནི་གནས་སྐབས་གཞན་ན་མེད་པའི་ཕྱིར་རོ། །

[Block 924]
འདི་ལྟར་ཞོའི་གནས་སྐབས་སུ་འོ་མའི་གནས་སྐབས་འགག་པར་མི་འགྱུར་ཏེ། ཞོའི་གནས་སྐབས་ན་འོ་མའི་གནས་སྐབས་མེད་པའི་ཕྱིར་རོ། །

[Block 925]
ཅི་སྟེ་ཡོད་ན་ནི། འོ་མ་དང་ཞོ་གཉིས་ལྷན་ཅིག་ན་གནས་པ་དང་། ཞོ་རྒྱུ་མེད་པ་ལས་འབྱུང་བར་ཡང་འགྱུར་བས་དེ་ནི་མི་འདོད་དེ། དེ་ལྟ་བས་ན་འགག་པ་མི་འཐད་པ་ཡང་བློའི་མངོན་སུམ་ཡིན་པའི་ཕྱིར་འགག་པ་ཞེས་བྱ་བ་ཅི་ཡང་མེད་པ་དེ་ལྟར་ཁོང་དུ་ཆུད་པར་བྱའོ། །

[Block 926]
སྨྲས་པ། འགག་པ་ནི་ཡོད་པ་ཁོ་ན་ཡིན་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། སྔར་ཁས་བླངས་པའི་ཕྱིར་ཏེ། འདི་ལྟར་ཁྱོད་ཀྱིས་སྔར་དངོས་པོ་འགག་བཞིན་པ་ལ་སྐྱེ་བ་མི་འཐད་དོ་ཞེས་སྨྲས་པ་དེའི་ཕྱིར་འགག་པ་དེ་ཡོད་དེ། གང་གི་རྒྱུ་ལས་བྱུང་བའི་སྐྱེ་བ་དགག་པར་བྱས་པའི་ཕྱིར་རོ། །

[Block 927]
འདི་ལྟར་མེད་པ་ནི་རྒྱུར་མི་འཐད་དོ། །

[Block 928]
བཤད་པ། ཅི་ཁྱོད་རི་མོའི་མེ་གསོད་པར་བྱེད་དམ། ཁྱོད་སྐྱེ་བ་མེད་པ་ལ་འགག་པ་འདོད་ཀོ། །

[Block 929 [VERSE]]
གང་ཚེ་ཆོས་རྣམས་ཐམས་ཅད་ཀྱི། །
སྐྱེ་བ་འཐད་པར་མི་འགྱུར་བ། །
དེ་ཚེ་ཆོས་རྣམས་ཐམས་ཅད་ཀྱི། །
འགག་པ་འཐད་པར་མི་འགྱུར་རོ། །

[Block 930]
གང་གི་ཚེ་ཁོ་བོས་དངོས་པོ་ཐམས་ཅད་ཀྱི་སྐྱེ་བ་མི་འཐད་དོ་ཞེས་སྨྲས་པ་དེའི་ཚེ་དངོས་པོ་ཐམས་ཅད་ཀྱི༌[^581]འགག་པ་ཡང་མི་འཐད་དོ་ཞེས་སྨྲས་པ་མ་ཡིན་ནམ། འདི་ལྟར་དངོས་པོར་སྐྱེས་ཤིང་མེད་པ་ལ་འགག་པ་ཡོད་པར་ཇི་ལྟར་འགྱུར། དེ་ལྟ་བས་ན་སྐྱེ་བ་བཀག་པ་ཁོ་ནས་འགག་པ་མི་འཐད་པར་ཡང་རབ་ཏུ་བསྟེན་པ༌[^582]ཡིན་ནོ། །

[Block 931]
ཡང་གཞན་ཡང་། འདི་ལ་གལ་ཏེ་རེ་ཞིག་འགག་པ་ཞིག་ཡོད་པར་གྱུར་ན། དེ་དངོས་པོ་ཡོད་པའམ། མེད་པ༌[^583]བརྟག་གྲང་ན། དེ་ལ།

[Block 932 [VERSE]]
རེ་ཞིག་དངོས་པོ་ཡོད་པ་ལ། །
འགག་པ་འཐད་པར་མི་འགྱུར་རོ། །

[Block 933]
རེ་ཞིག་དངོས་པོ་ཡོད་པ་གནས་པ་ལ་ནི་འགག་པ་འཐད་པར་མི་འགྱུར་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། འདི་ལྟར།

[Block 934 [VERSE]]
དངོས་དང་དངོས་པོ་མེད་པ་དག །
གཅིག་ཉིད་ན་ནི་འཐད་པ་མེད། །

[Block 935]
དངོས་པོ་ཡོད་པའི་ཡོད་པ་ཉིད་གང་ཡིན་པ་ནི་དངོས་པོ་ཡོད་པའོ། །

[Block 936]
དངོས་པོ་འགགས་པའི༌[^584]མེད་པ་ཉིད་གང་ཡིན་པ་ནི་དངོས་པོ་མེད་པ་སྟེ། དངོས་པོ་དང་དངོས་པོ་མེད་པ་ཕན་ཚུན་མི་མཐུན་པ་དེ་གཉིས་ཇི་ལྟར་གཅིག་པ་ཉིད་ནི༌[^585]འཐད་པར་འགྱུར་ཏེ། དེ་ལྟ་བས་ན། དངོས་པོ་ཡོད་པ་ལ་འགག་པ་འཐད་པར་མི་འགྱུར་ཏེ།

[Block 937 [VERSE]]
དངོས་པོ་མེད་པར་གྱུར་པ་ལའང་། །
འགག་པ་འཐད་པར་མི་འགྱུར་རོ། །

[Block 938]
ཇི་ལྟར་ཞེ་ན།

[Block 939 [VERSE]]
མགོ་གཉིས་པ་ལ་ཇི་ལྟར་ནི། །
བཅད་དུ་མེད་པ་དེ་བཞིན་ནོ། །

[Block 940]
མེད་པ་ལ་ཅི་ཞིག་འགག་པར་འགྱུར་ཏེ། འདི་ལྟར་མགོ་གཉིས་པ་མེད་པར་བཅད་པར་མི་ནུས་པ་བཞིན་ནོ། །

[Block 941]
འགག་པའི་འགག་པ་ཞེས་གང་སྨྲས་པ་དེ་ལ་བཤད་པར་བྱ་སྟེ།

[Block 942 [VERSE]]
འགག་པ་འགག་པ་གཞན་དང་ནི། །
དེ་ཉིད་ཀྱིས་ཀྱང་འགག་མི་རིགས། །

[Block 943]
འདི་ལ་གལ་ཏེ་འགག་པ་ལ་འགག་པ་ཞིག་ཡོད་པར་གྱུར་ན་དེ་གཞན་གྱི་བདག་ཉིད་དམ་རང་གི༌[^586]བདག་ཉིད་ཀྱིས་འགག་པར་འགྱུར་གྲང་ན། གཉི་གས་ཀྱང་འགག་པར་མི་རིགས་སོ། །ཇི་ལྟར་ཞེ་ན།

[Block 944 [VERSE]]
ཇི་ལྟར་སྐྱེ་བ་རང་དང་ནི། །
གཞན་གྱིས་བསྐྱེད་པ་མ་ཡིན་བཞིན། །

[Block 945]
ཇི་སྐད་དུ། སྐྱེ་བ་འདི་ནི་མ་སྐྱེས་པས། །རང་གི་བདག་ཉིད་ཇི་ལྟར་སྐྱེད།[^587] །

[Block 946 [VERSE]]
ཅི་སྟེ་སྐྱེད་པས༌[^588]སྐྱེད་བྱེད་ན། །
སྐྱེས་ན་ཅི་ཞིག་བསྐྱེད་དུ་ཡོད། །

[Block 947]
ཅེས་སྨྲས་པ་དེ་བཞིན་དུ་འགག་པ་ཡང་མ་འགགས་པས་རང་གི་བདག་ཉིད་འགག་པར་བྱེད་དམ། འགགས་པས་རང་གི་བདག་ཉིད་འགག་པར་བྱེད་གྲང་ན། དེ་ལ་གལ་ཏེ་འགག་པ་མ་འགགས་པས་རང་གི་བདག་ཉིད་འགག་པར་བྱེད་པ༌[^589]རྟོག་ན། དེ་ཇི་ལྟར་འཐད་པར་འགྱུར་ཏེ། གང་གི་ཚེ་མ་འགགས་པ༌[^590]ནི་འགག་པ་ཉིད་མ་ཡིན་པས་མེད་པས་བདག་ཉིད་མེད་པ་ཇི་ལྟར་འགག་པར་བྱེད། ཅི་སྟེ་འགག་པ་འགགས་པས་རང་གི་བདག་ཉིད་འགག་པར་བྱེད་པར་རྟོག་ན། དེ་ཡང་ཇི་ལྟར་འཐད་པར་གྱུར༌[^591]ཏེ། འགགས་པ་ལ་གང་འགག་པ་འགག༌[^592]པར་འགྱུར་བའི་རང་གི་བདག་ཉིད་ཡང་འགག་པར་བྱ་བ་དེ་ཅི་ཡང་མེད་དོ། །

[Block 948]
དེ་ལྟར་རེ་ཞིག་འགག་པ་རང་གི་བདག་ཉིད་ཀྱིས་འགག་པར་བྱེད་པར་མི་འཐད་དེ།[^593] །གཞན་གྱི་བདག་ཉིད་ཀྱིས་ཀྱང་མི་འཐད་དེ། ཇི་སྐད་དུ།

[Block 949 [VERSE]]
གལ་ཏེ་སྐྱེ་བ་གཞན་ཞིག་གིས། །
དེ་སྐྱེད༌[^594]ཐུག་པ་མེད་པར་འགྱུར། །
ཅི་སྟེ་སྐྱེ་བ་མེད་སྐྱེ་ན། །
ཐམས་ཅད་དེ་བཞིན་སྐྱེ་བར་འགྱུར། །

[Block 950]
ཞེས་སྨྲས་པ་དེ་བཞིན་དུ་འགག་པ་ཡང་འགག་པ་གཞན་ཞིག་གིས་འགག་པར་བྱེད་དམ། འགག་པ་གཞན་མེད་པར་འགག་པར་བྱེད་གྲང་ན། དེ་ལ་གལ་ཏེ་འགག་པ་དེ་འགག་པ༌[^595]གཞན་གྱིས་འགག་པར་བྱེད་ན་དེ་ལྟ་ན་ཐུག་པ་མེད་པར་ཐལ་བར་འགྱུར་ཏེ། དེ་ཡང་གཞན་གྱིས་འགག་པར་བྱེད་ཅིང་དེ་ཡང་གཞན་གྱིས་འགག་པར་བྱེད་དེ་མཐའ་མེད་པར་འགྱུར་བས་དེ་ནི་མི་འདོད་དེ།[^596] དེ་ལྟ་བས་ན་འགག་པའི་འགག་པ་མི་འཐད་དོ། །ཅི་སྟེ་འགག་པ་དེ་འགག་པ་གཞན་མེད་པར་འགག་གོ་སྙམ་ན། དེ་ལ་བཤད་པར་བྱ་སྟེ། ཅི་སྟེ་འགག་པ་མེད་འགགས༌[^597]ན། །ཐམས་ཅད་དེ་བཞིན་འགག་པར་འགྱུར། །
--- END BLOCKS ---
