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
[Block 1016]
དེའི་ཕྱིར་དེ་ལྟར་རྒྱུ་མེད་ན་ཉེས་པ་མང་པོ་དང་ཆེན་པོ་དག་ཏུ་ཐལ་བར་འགྱུར་བས་བྱེད་པ་པོ་མ་ཡིན་པར་འགྱུར་བས༌[^644]ལས་མ་ཡིན་པར་གྱུར་པ་བྱེད་དོ། །ཞེས་བྱ་བ་དེ་ནི་ཤིན་ཏུ་ཚིག་ངན་པ་ཡིན་ནོ། །

[Block 1017]
དེ་ལ་འདི་སྙམ་དུ་བྱེད་པ་པོ་ཡིན་པ་དང་མ་ཡིན་པར་གྱུར་པ་ལས་ཡིན་པ་དང་མ་ཡིན་པར་གྱུར་པ་བྱེད་པར་སེམས་ན། དེ་ལ་བཤད་པར་བྱ་སྟེ།

[Block 1018 [VERSE]]
བྱེད་པ་པོར་གྱུར་མ་གྱུར་པ། །
གྱུར་མ་གྱུར་དེ་མི་བྱེད་དེ། །

[Block 1019]
བྱེད་པ་པོ་ཡིན་པ་དང་མ་ཡིན་པར་གྱུར་པ་ནི་བྱ་བ་དང་ལྡན་པ་དང་བྱ་བ་དང་མི་ལྡན་པའོ། །

[Block 1020]
ལས་ཡིན་པ་དང་མ་ཡིན་པར་གྱུར་པ་ཡང་བྱ་བ་དང་ལྡན་པ་དང་བྱ་བ་དང་མི་ལྡན་པའོ། །

[Block 1021]
བྱེད་པ་པོ་ཡིན་པ་དང་མ་ཡིན་པར་གྱུར་པ་ལས་ཡིན་པ་དང་མ་ཡིན་པར་གྱུར་པ་མི་བྱེད་དོ། །

[Block 1022]
ཅིའི་ཕྱིར་ཞེ་ན།

[Block 1023 [VERSE]]
ཡིན་དང་མ་ཡིན་གྱུར་པ་ནི། །
ཕན་ཚུན་འགལ་བས་ག་ལ་གཅིག །

[Block 1024]
གལ་ཏེ་བྱེད་པ་པོ་དང་ལས་དེ་ལྟ་བུ་དག་སྲིད་པར་གྱུར་ན་ནི་བྱེད་པ་པོ་དེ་ལས་དེ་བྱེད་པར་ཡང་འགྱུར་གྲང་ན། ཡིན་པ་དང་མ་ཡིན་པར་གྱུར་པ་ནི་ཕན་ཚུན་འགལ་བ༌[^645]ཡིན་པས། གཅིག་ན་ཡོད་པར་ག་ལ་འགྱུར་ཏེ། དེ་ལྟ་བས་ན་མི་སྲིད་པའི་ཕྱིར་དང་། གཉི་གའི་སྐྱོན་ཇི་སྐད་བསྟན་པར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་བྱེད་པ་པོ་ཡིན་པ་དང་། མ་ཡིན་པར་གྱུར་པ་མི་བྱེད་དོ། །

[Block 1025]
དེ་ལྟར་རེ་ཞིག་ཕྱོགས་མཐུན་པ་གསུམ་གྱིས་བྱེད་པ་པོ་དང་ལས་མི་འཐད་དེ། བྱེད་པ་པོ་ཡིན་པར་གྱུར་པ་ལས་ཡིན་པར་གྱུར་པ་མི་བྱེད་པ་དང་། བྱེད་པ་པོ་མ་ཡིན་པར་གྱུར་པ་ལས་མ་ཡིན་པར་གྱུར་པ་མི་བྱེད་པ་དང་། བྱེད་པ་པོ་ཡིན་པ་དང་། མ་ཡིན་པར་གྱུར་པ་ལས་ཡིན་པར༌[^646]གྱུར་པ་ལས་ཡིན་པ་དང་།

[Block 1026]
མ་ཡིན་པར་གྱུར་པ་མི་བྱེད་དོ། །མི་མཐུན་པས་ཀྱང་མི་འཐད་དེ། །

[Block 1027]
འདི་ལྟར།

[Block 1028 [VERSE]]
བྱེད་པ་པོ་དང་ལས་དག་ནི། །
གྱུར་པ་མ་གྱུར་མི་བྱེད་དོ། །

[Block 1029]
མ་གྱུར་པ་ཡང་གྱུར་མི་བྱེད།[^647]

[Block 1030]
།རེ་ཞིག་བྱེད་པ་པོ་ཡིན་པར་གྱུར་པ་ལས།

[Block 1031]
མ་ཡིན་པར་གྱུར་པ་མི་བྱེད་དོ། །

[Block 1032]
བྱེད་པ་པོ་མ་ཡིན་པར༌[^648]གྱུར་པ་ལས་ཡིན་པར་གྱུར་པ་མི་བྱེད་དོ། །

[Block 1033]
ཅིའི་ཕྱིར་ཞེ་ན། འདི་ལྟར། འདིར་ཡང་སྐྱོན་དེར་ཐལ་བར་འགྱུར། །བྱེད་པ་པོ་དང་ལས་རྣམ་པ་དེ་ལྟ་བུ་དག༌[^649]ཡོངས་སུ་རྟོག་ན་འདིར་ཡང་གང་གི་ཕྱིར་སྔར་བསྟན་པའི་སྐྱོན་བྱེད་པ་པོ་ཡིན་པར་གྱུར་པ་ལ་བྱ་བ་མེད་པ་དང་། ལས་ལ་བྱེད་པ་པོ་མེད་པ་དང་། ལས་ཡིན་པར་གྱུར་པ་ལ་བྱ་བ་མེད་པ་དང་། བྱེད་པ་པོ༌[^650]ལས་མེད་པ་དང་། བྱེད་པ་པོ་དང་ལས་མ་ཡིན་པར་གྱུར་པ་དག་ལ་རྒྱུ་མེད་པར་འགྱུར་བ་དེའི་ཕྱིར་བྱེད་པ་པོ་ཡིན་པར༌[^651]གྱུར་པ་ལས་མ་ཡིན་པར་གྱུར་པ་མི་བྱེད་ལ། [^652]བྱེད་པ་པོ་མ་ཡིན་པར་གྱུར་པ་ལས་ཡིན་པར་གྱུར་པ་མི་བྱེད་དོ། །

[Block 1034 [VERSE]]
བྱེད་པ་པོ་དང་ལས་དག་ནི། །
གྱུར་དང་བཅས་པ་མ༌[^653]གྱུར་དང་། །
གྱུར་མ་གྱུར་པ་མི་བྱེད་དེ། །

[Block 1035]
བྱེད་པ་པོ་ཡིན་པར་གྱུར་པ་ལས་མ་ཡིན་པར་གྱུར་པ་དང་ཡིན་པ་དང་མ་ཡིན་པར་གྱུར་པ་མི་བྱེད་དོ། །ཅིའི་ཕྱིར་ཞེ་ན། གཏན་ཚིགས་གོང་དུ་བསྟན་ཕྱིར་རོ། །

[Block 1036]
བྱེད་པ་པོ་ཡིན་པར་གྱུར་པ་ལ་བྱ་བ་མེད་པ་དང་། ལས་མ་ཡིན་པར་གྱུར་པ་ལ་རྒྱུ་མེད་པ་དང་། ལས་ཡིན་པ་དང་མ་ཡིན་པར་གྱུར་པ་ཕན་ཚུན་འགལ་བས་ག་ལ༌[^654]གཅིག་ཅེས་བསྟན་པའི་ཕྱིར་རོ། །

[Block 1037 [VERSE]]
བྱེད་པ་པོ་དང་ལས་དག་ནི། །
མ་གྱུར་པ་ནི་གྱུར་བཅས་དང་། །
གྱུར་མ་གྱུར་པ་མི་བྱེད་དེ། །

[Block 1038]
བྱེད་པ་པོ་མ་ཡིན་པར་གྱུར་པ་ལས་ཡིན་པར་གྱུར་པ་དང་། ཡིན་པ་དང་མ་ཡིན་པར་གྱུར་པ་མི་བྱེད་དོ། །ཅིའི་ཕྱིར་ཞེ་ན། གཏན་ཚིགས་གོང་དུ་བསྟན་ཕྱིར་རོ། །

[Block 1039]
བྱེད་པ་པོ་མ་ཡིན་པར་གྱུར་པ་ལས་རྒྱུ་མེད་པ་བྱེད།[^655] ལས་མ་ཡིན་པར་གྱུར་པ་ལ་བྱ་བ་མེད་པ་དང་། ལས་ཡིན་པ་དང་མ་ཡིན་པར་གྱུར་པ་ཕན་ཚུན་འགལ་བས་ག་ལ་གཅིག་ཅེས་བསྟན་པའི་ཕྱིར་རོ། །

[Block 1040 [VERSE]]
བྱེད་པ་པོར་གྱུར་མ་གྱུར་ནི། །
ལས་སུ་གྱུར་དང་མ་གྱུར་པ། །

[Block 1041]
མི་བྱེད། བྱེད་པ་པོ་ཡིན་པ་དང་མ་ཡིན་པར་གྱུར་པ་ལས་ཡིན་པར་གྱུར་པ་དང་། མ་ཡིན་པར་གྱུར་པ་མི་བྱེད་དོ། །ཅིའི་ཕྱིར་ཞེ་ན།

[Block 1042]
འདིར་ཡང་གཏན་ཚིགས་ནི། །གོང་དུ་བསྟན་པས་ཤེས་པར་བྱ། །བྱེད་པ་པོ་ཡིན་པ་དང་མ་ཡིན་པར་གྱུར་པ་ལས།

[Block 1043]
ཕན་ཚུན་འགལ་བས་ག་ལ་གཅིག་ཅེས་བྱ་བ་དང་། ལས་ཡིན་པར་གྱུར་པ་ལ་བྱ་བ་མེད་པ་དང་། ལས་མ་ཡིན་པར་གྱུར་པ་ལ་རྒྱུ་མེད་པར་འགྱུར་རོ་ཞེས་བསྟན་པ་དག་གིས་ཤེས་པར་བྱའོ། །

[Block 1044]
དེ་ལྟར་ཕྱོགས་མི་མཐུན་པ་དྲུག་གིས་ཀྱང་བྱེད་པ་པོ་དང་ལས་མི་འཐད་དེ། ཡིན་པར་གྱུར་པ་མ་ཡིན་པར་གྱུར༌[^656]པ་དང་། མ་ཡིན་པར་གྱུར་པ་ཡིན་པར་གྱུར་པ་མི་བྱེད་པ་དང་། ཡིན་པར་གྱུར་པ་མ་ཡིན་པར་གྱུར་པ་དང་། ཡིན་པ་དང་མ་ཡིན་པར་གྱུར་པ་མི་བྱེད་པ་དང་། མ་ཡིན་པར་གྱུར་པས་ཡིན་པར་གྱུར་པ་དང་། ཡིན་པ་དང་མ་ཡིན་པར་གྱུར་པ་མི་བྱེད་པ་དང་། ཡིན་པ་དང་མ་ཡིན་པར་གྱུར་པ་ཡིན་པར་གྱུར་པ་དང་། མ་ཡིན་པར་གྱུར་པ་མི་བྱེད་དེ། དེ་ལྟ་བས་ན་བྱེད་པ་པོ་འདི་ལས་འདི་བྱེད་དོ་ཞེས་བྱ་བ་དེ་ཇི་ལྟར་ཡང་མི་འཐད་དོ། །

[Block 1045]
སྨྲས་པ། བྱེད་པ་པོ་འདི་ལས་འདི་བྱེད་དོ་ཞེའམ། མི་བྱེད་དོ༌[^657]ཞེས་བྱ་བ་དེས་ཁོ་བོ་ལ་ཅི་བྱ། ཡོད་ན༌[^658]ནི་རེ་ཞིག་བྱེད་པ་པོ་དང་ལས་ཡོད་དོ། །

[Block 1046]
བཤད་པ། ཅི་ཁྱོད་ཏིལ་མར་འདོད་ལ་དགོན་པའི་ཏིལ་ཀ་ཚོལ་ལམ། ཁྱོད་བྱེད་པ་པོ་དང་ལས་ཞེས་བྱ་བའི་མིང་ཙམ་གྱིས་དགའ་ཞིང་ཅི་ཡང་མི་བྱེད་པ་བྱེད་པོར་འདོད་ལ་མི་བྱ་བ་ལས་སུ་འདོད་ཀོ། །བྱ་བ་གཞན་མི་འཐད་པས་དེ་དག་ཡོད་པར་བརྟག་པ་དོན་མེད་པར་འགྱུར་དུ་ངེས་ཏེ། དེ་ལྟ་བུའི་རང་བཞིན་ཅན་ནི་བྱེད་པ་པོ་ཡང་མ་ཡིན་ལ་དེ་ལྟ་བུའི་རང་བཞིན་ཅན་ནི་ལས་ཀྱང་མ་ཡིན་པས་འདིར་གང་བདེན་པར་གྱུར་པ་དེ་ཉིད་གཟུང་བར་བྱ་བའི་རིགས་པ་སྙམ།

[Block 1047]
སྨྲས་པ། གལ་ཏེ་དེ་ལྟར་བྱེད་པ་པོ་ཡང་མེད་ལ། ལས་ཀྱང་མེད་ན་ཁྱོད་ཀྱིས་རྒྱུ་མེད་པའི་སྐྱོན་དུ་ཐལ་བར་འགྱུར་རོ། །ཞེས་གང་དག་བསྟན་པ་དེ་དག་ཐམས་ཅད་ཁྱོད་ལ་རྗེས་སུ་འབྲེལ་བར་མི་འགྱུར་རམ། བཤད་པ། མི་འགྱུར་ཏེ། ཁོ་བོ་ནི་བྱེད་པ་པོ་དང་ལས་དག་མེད་པ་ཉིད་དུ་མི་སྨྲའི། ཁོ་བོས་དེ་དག་གི་བྱ་བ་ཡིན་པར་གྱུར་པ་དང་། མ་ཡིན་པར་གྱུར་པ་ཡོངས་སུ་རྟོགས་པ༌[^659]སྤངས་པ་དེ་བྱས་ཏེ། ཁོ་བོ་ནི་བྱེད་པ་པོ་དང་ལས་དག་བརྟེན་ནས་གདགས་པར་འདོད་དེ། དེ་ཡང་ཇི་ལྟར་ཞེ་ན།

[Block 1048 [VERSE]]
བྱེད་པོ་ལས་ལ་བརྟེན་བྱས་ཤིང་། །
ལས་ཀྱང་བྱེད་པོ་དེ་ཉིད་ལ། །
བརྟེན་ནས་འབྱུང་བ་མ་གཏོགས་པར། །
འགྲུབ་པའི་རྒྱུ་ནི་མ་མཐོང་ངོ་།

[Block 1049]
[^660] །བྱེད་པ་པོ་ནི་ལས་ལ་བརྟེན་ཅིང་ལས་ལ་གནས། ལས་ལ་ལྟོས་ནས་བྱེད་པ་པོ་ཞེས་གདགས་ཤིང་བརྗོད་དོ། །

[Block 1050]
དེའི་ལས་ཀྱང་བྱེད་པ་པོ་དེ་ཉིད་ལ་བརྟེན་ནས་འབྱུང༌[^661]ཞིང་དེའི་ལས་ཞེས་གདགས་ཤིང་བརྗོད་དོ། །

[Block 1051]
དེའི་ཕྱིར་དེ་གཉིས་ནི་ལྟོས་པ་ཅན་དུ་གདགས་པ་ཡིན་གྱི། ངོ་བོ་ཉིད་དུ་གྲུབ་པ་དང་མ་གྲུབ་པ་མེད་དོ། །

[Block 1052]
དེའི་ཕྱིར་དེ་ལྟར་དེ་གཉིས་ཡོད་པ་ཉིད་དང་མེད་པ་ཉིད་དུ་ཁས་མ་བླངས་པས་དབུ་མའི་ལམ་དུ་གདགས་པ་ཡིན་ནོ། །

[Block 1053]
གདགས་པ་དེ་མ་གཏོགས་པར་དེ་གཉིས་འགྲུབ་པའི་མཚན་ཉིད་གཞན་མ་མཐོང་ངོ་། །དེ་བཞིན་ཉེར་ལེན་ཤེས་པར་བྱ། །ཉེར་ལེན་ཞེས་བྱ་བ་ནི་དངོས་པོར་ལྟ་སྟེ། གང་ལ་དངོས་པོ་ཡོད་པ་དེ་ལ་བྱེད་པ་པོ་དུ་མ་ཡོད་པས་འདིར་ཉེ་བར་བླངས་པ་དང་ཉེ་བར་ལེན་པ་པོ་གཟུང་བར༌[^662]འདོད་པར་བྱའོ། །

[Block 1054]
དེ་ལ་ཇི་ལྟར་བྱེད་པ་པོ༌[^663]ལ་བརྟེན་ནས་གདགས་པ་དེ་བཞིན་དུ། ཉེ་བར་ལེན་པ་པོ་ཡང་ཉེ་བར་བླང་བ་ལ་བརྟེན་ནས་གདགས་སོ། །

[Block 1055]
ཇི་ལྟར་ལས་བྱེད་པ་པོ་དེ་ཉིད་ལ་བརྟེན་ནས་གདགས་པ་དེ་བཞིན་དུ་ཉེ་བར་བླང་བ་ཡང་ཉེ་བར་ལེན་པ་པོ་དེ་ཉིད་ལ་བརྟེན་ནས་གདགས་ཏེ། དེ་གཉིས་ལ་ཡང་དེ་མ་གཏོགས་པར་འགྲུབ་པའི་མཚན་ཉིད་མ་མཐོང་ངོ་། །དེ་ཡང་། ཇི་ལྟར་ཞེ་ན། ལས་དང་བྱེད་པོ༌[^664]བསལ་ཕྱིར་རོ། །
--- END BLOCKS ---
