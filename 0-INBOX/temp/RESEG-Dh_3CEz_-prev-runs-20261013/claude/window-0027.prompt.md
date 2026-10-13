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
[Block 946]
དེའི་ཕྱིར་གང༌[^408]ཕྱིར་སྐལ་བ་སྟོན། །ཞེས་པ་སྟེ། སྐལ་པ་ནི་ཐབས་ཏེ་ཤེས་རབ་སྟོང་པ༌[^409]ཉིད་དང་བཅས་པའི་ཕྱིར་རོ། །

[Block 947]
དེ་བཞིན་དུ་བཙོ་བླག༌[^410]མོ་དང་གར་མ་ལ་ཡང་ཐབས་དང་ཤེས་རབ་གོ་རིམས་བཞིན་ནོ། །

[Block 948]
གཡུང་མོ་ཡང་ཐབས་སུ་བསྟན་པ་སྟེ། དེ་བཞིན་དུ་གདོལ་བ་མོ་དང་། བྲམ་ཟེ་མོ་ལ་ཡང་ཐབས་སུ་ཤེས་པ་ཤུགས་ཀྱིས་བསྟན་ནོ། །

[Block 949]
དེ་དག་ནི་ལྟ་བ་དང་སྒོམ་པ་སྟེ་ཤེས་བྱའི་དེ་ཁོ་ན་ཉིད་དོ། །

[Block 950 [HEADING]]
#### སྒོ་གསུམ་ནུས་པ་ཅན་དུ་བྱེད་པ་སྒྲུབ་པ་པོ་དེ་ཁོ་ན་ཉིད། ^1-5-3-0

[Block 951]
སྒོ་གསུམ་ནུས་པ་ཅན་དུ་བྱེད་པ་སྒྲུབ་པ་པོ་དེ་ཁོ་ན་ཉིད་ནི། ཨཱ་ལི་ཀཱ་ལི་ལ་སོགས་པའོ། །

[Block 952]
དེ་ཡང་། ཨཱ་ལི་ཀཱ་ལི་རབ་བརྟགས་པས། །ཞེས་པ་ནི་བརྗོད་པ་ནི་ཐམས་ཅད་རླུང་ལ་རག་ལས་པ་སྟེ་གཡོན་དང་གཡས་ནས་རྒྱུ་བའོ། །

[Block 953]
བརྗོད་པ་ཐམས་ཅད་བཟླས་པར་བཤད། །ཅེས་པ་ནི་རླུང་ལས་གྲུབ་པའམ། ཡང་ན་ཨཱ་ལི་ཀཱ་ལི་སྟེ། དབྱངས་དང་གསལ་བྱེད་ཀྱི་ཡི་གེ་ལས་གྲུབ་པའི་ཕྱིར་བཟླས་པ་ཡིན་ཏེ་རྡོ་རྗེའི་བཟླས་པ༌[^411]རླུང་འབྱུང་བ་དང་འཇུག་པ་ཨཾ་དང་ཧཾ་ཟློས་པའམ། ཡང་ན་རང་གི་ལྷན་ཅིག་སྐྱེས་པའི་ཉམས་ཀྱིས་རྣམ་དག་སྔགས་ཀྱི༌[^412]གླུ་ལེན་ཅེས་བྱའོ། །

[Block 954]
རྐང་པའི་རྗེས་ནི་ཞེས་པ་ནི་རྒྱ༌[^413]བྲིས་པ་ལྟ་བུར་བྱུང་བ་སྟེ་དཀྱིལ་འཁོར་ཡིན་ཞེས་པ་ནི་གཟུགས་བརྙན་དུ་སྣང་བའི་ཕྱིར་རོ། །

[Block 955]
དེས་ན། [^414]ཉེད་ཕྱིར་དཀྱིལ་འཁོར་བརྗོད་པར་བྱ། །ཞེས་པའོ། །

[Block 956]
དཀྱིལ་འཁོར་ནི་མཎྜལ་བྲིས་པ༌[^415]ན་དཀྱིལ་འཁོར་རོ། །

[Block 957]
མ་ཊ་ན་ཉེད་པས་སམ་བྲིས་པས་ཞེས་སྒྲ་མཐུན་པ་དང་། ཡང་ཡེ་ཤེས་དེ་ཉིད་རྟེན་དང་བརྟེན་པར་སྣང༌[^416]སྟེ་བརྟག་པ་ཕྱི་མར་འཆད་དོ། །

[Block 958 [VERSE]]
ལག་པ་བསྒྱུར་བ་ཞེས་པ་ནི་གར་ལ་སོགས་པའོ། །
ཕྱག་རྒྱ་ཡིན་ཞེས་པ་ནི་བདེ་བའི་རྟགས༌[^417]ཡིན་པས་སོ། །

[Block 959]
སོར་མོ་ཉེད་པའང་དེ་བཞིན་ནོ། །ཞེས་པ་ནི་དེ་ཁོ་ན་ཉིད་ཀྱི་མཚན་མ་དང་རྟགས་སོ། །

[Block 960]
གང་སེམས་དཔའ་བསམ་གཏན་དུ་བསྟན་པ་ཡང་ཚིག་གཉིས་ཏེ། དེའི་རྒྱུ་མཚན་ཡང་ཇི་ལྟར་ཞེས་པ་ཚིགས་སུ་བཅད་པ་གཅིག་གིས་སོ། །

[Block 961]
ཇི་ལྟར་ཕ་ལས་བདེ༌[^418]ཐོབ་པ། །ཞེས་པ་ནི་སློབ་དཔོན་ལ་ལ་དག་བླ་མ་དང་རྡོ་རྗེ་འཛིན་པ་ལ་འདོད་དོ། །

[Block 962]
དེ༌[^419]ནི་འདིར་མཐུན་པ་མ་ཡིན་ནོ། །

[Block 963]
དཔེར་ན་ཕ་ལས་ཐོབ་པ་ནི་རང་གི་ནོར་ཏེ།

[Block 964 [VERSE]]
གཞན་ལྷག་མ་མི་ཚོལ་བའི༌[^420]དོན་ནོ། །
དེ་ཡི་བདེ་བ་རང་གིས་བཟའ། །

[Block 965 [VERSE]]
ཞེས་པ་ནི་བོ་ཀི་ནི་བཟའ་བའམ་ལོངས་སྤྱོད་པའོ། །
དེས་ན་ལྷན་ཅིག་སྐྱེས་པ་ལ་ལོངས་སྤྱོད་པས།

[Block 966]
དེ་ཡི་བདེ་བ་བསམ་གཏན་བརྗོད། །ཅེས་པའོ། །

[Block 967]
བདེ་བ་གང་ཕྱིར་འཆི་བ་འདིར། །ཞེས་པ་ནི་སློབ་དཔོན་ལ་ལ་དག་འཆི་བའི་ཆོས་སུ་འདོད་པ་དང་། ལ་ལ་དག་སྤྱོད་ལམ་དུ་འདོད་དེ། དེ་དག་འདིར་མཐུན་པ་མ་ཡིན་ནོ། །ཇི་ལྟ་བུ་ཞེ་ན། །དེ་ཡང་འཆི་བ་ནི༌[^421]སྡུག་བསྔལ་གྱི་གཙོ་བོ་སྟེ། དེ་བསམ་གཏན་དུ་ཇི་ལྟར་འགྱུར་ཞེ་ན། བདེན་ཏེ་འོན་ཀྱང་བཟའ་བ་ལོངས་སྤྱོད་ཀྱི་སྐབས་སུ་རང་གི་བདེན་པ༌[^422]ལས་ལྷག་པར༌[^423]མི་ཚོལ་ཞིང་། འཆི་བའི་ཚེ་ཡང་རང་གི་བདེ་བ་དང་མི་འབྲལ་བ་སྟེ་ལྷན་ཅིག་སྐྱེས་པའི་ཕྱིར་རོ། །

[Block 968]
དེས་ན་རྒྱུན་དུ་རྩེ་གཅིག་པས་གང་བསམ༌[^424]ཀྱང་བསམ་གཏན་ཁོ་ནའོ། །

[Block 969 [HEADING]]
#### སྔགས་ཀྱི་ལུགས་ཀྱིས་འབྲས་བུ་ཐོབ་པ། ^1-5-4-0

[Block 970]
སྤྱིར་སྔགས་ཀྱི་ལུགས་ཀྱིས་ཚེ་འདི་ལ་འབྲས་བུ་ཐོབ་པ་དང་། བར་དོ་ལ་འབྲས་བུ་ཐོབ་པའོ། །

[Block 971 [HEADING]]
##### ཚེ་འདི་ལ་འབྲས་བུ་ཐོབ་པ། ^1-5-4-1-0

[Block 972]
ཚེ་འདི་ལ་ཐོབ་པ་ལ་གཉིས། རྣམ་སྨིན་འབོར་བ་དང་། མི་འབོར་བའོ། །

[Block 973 [HEADING]]
###### མི་འབོར་བ། ^1-5-4-1-2-0

[Block 974]
དེ་ལ་བསྐྱེད་རིམ་གཙོར་བསྒོམས༌[^425]པས། མཁའ་སྤྱོད་བསྒྲུབས༌[^426]ལ་དེ་ནས་ཕྱག་རྒྱ་ཆེན་པོ་བསྒྲུབ་པ་སྟེ། བུདྡྷའོ། །

[Block 975]
རྫོགས་རིམ་པ་ནི་ལུས༌[^427]འཇའ་ཚོན་ལྟར་བསྒྱུར།[^428] སེམས་ཕྱག་རྒྱ་ཆེན་པོར་འགྱུར་ཏེ་ཐལ་བྱུང་དུ་སངས་རྒྱས་སོ། །

[Block 976 [HEADING]]
###### རྣམ་སྨིན་འབོར་བ། ^1-5-4-1-1-0

[Block 977]
རྣམ་སྨིན་འདོར་བ་ནི་ལུས་ལྷར་གསལ་ཙམ་ལས་མེད་ཀྱང་སེམས་ཕྱག་རྒྱ་ཆེན་པོར་སྦྱོར་ཏེ་སྤྱོད་པས་མཐར་ཕྱིན་ནས་འཆི་བའི་སྤྱོད་ལམ་དུ་ཤེས་པས་འགྲོ་ཞིང་འཚང་རྒྱའོ། །

[Block 978 [HEADING]]
##### བར་དོ་ལ་འབྲས་བུ་ཐོབ་པ། ^1-5-4-2-0

[Block 979]
དེ་ལྟར་མ་ནུས་ན་བར་དོའི་གདམས་ངག་གིས་འཚང་རྒྱ་བ་སྟེ།[^429] དེ་རྩ་བའི་རྒྱུད་ལྟར་བྱ་བ་དང་། བཤད་པའི་རྒྱུད་ས་མཱུ་ཊ་ལྟར་གོང་དུ་འཕོ་བ་དང་གྲོང་དུ་འཇུག་པ་ལ་སོགས་པའི་གཞན་དང་བླ་མའི་ཞལ་ལས་ཤེས་པར་བྱའོ། །

[Block 980]
དེ་ལྟར་མ་ནུས་ན་སྨོན་ལམ་བཏབ་ལ་སྐྱེ་བ་གཞན་ལ་འཁོར་ལོས་སྒྱུར་བ་ལ་སོགས་པར་སྐྱེ་སྟེ་སྐྱེ་བ་བདུན་ཚུན་ཆད་ཀྱིས༌[^430]འགྲུབ་ཅེས་བྱའོ། །

[Block 981]
ལེའུ་ནི༌[^431]སྔ་མ་བཞིན་ཏེ་ཡས་བགྲངས་པའི་ལྔ་པའོ།། །།

[Block 982 [HEADING]]
### དྲུག་པ་སྤྱོད་པ། ^1-6-0

[Block 983]
དེ་ནས་ཡང་དག་བཤད་པར་བྱ། །ཞེས་པ་ནི་ལྟ་བ་དང་སྒོམ་པའི་རྗེས་སུ་འབྲས་བུ་སྤྱོད་པས་མཐར་ཕྱིན་པ་བཤད་པའོ། །

[Block 984 [VERSE]]
དེ་ཡང་སྤྱོད་པ་ནི་ཙརྱ་སྟེ་ཙརྱ༌[^432]ནི་རྒྱུ་བའོ། །
ཡ་ཡོ་གི་ནི་རྣལ་འབྱོར་མར༌[^433]སྦྱོར་བའོ། །

[Block 985]
དེས་ཅིར་འགྱུར་ཞེ་ན།
--- END BLOCKS ---
