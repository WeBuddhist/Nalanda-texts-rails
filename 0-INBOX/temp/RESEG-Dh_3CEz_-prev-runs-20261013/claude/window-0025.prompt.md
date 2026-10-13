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
དེ་ཡང་དེ་ཉིད་རིག་པས་ཞེས་པ་ནི་གཉུག་མའི་དབང་པོ་དེར་བདེ་བ་ཆེན་པོ་རང་གསལ་བའོ། །

[Block 877]
རྟག་ཏུ་མཆོད་ཅེས་པ་ནི་དབང་པོ་རང་སྣང་གི་མན་ངག་གོ། །

[Block 878 [VERSE]]
ཇི་ལྟར་དབྱེ་བར་མི་འགྱུར་བར། །
ཞེས་པ་ནི་ལྷན་ཅིག་སྐྱེས་པའི་ཕྱིར་རོ། །

[Block 879]
རབ་ཏུ་འབད་པའི་ཞེས་པ་ནི་དེ་ཡང་བླ་མའི་མན་ངག་གིས་ཐོབ་པས་སོ། །

[Block 880]
རྟེན་པ་ཉིད་ཅེས་པ་ནི་ཤེས་རབ་ལྷ་མོ་བླ་ན་མེད་པ་དང་འདོད་པའི་ཡོན་ཏན་ནོ། །

[Block 881]
མ་གསང་ཞེས་བྱ་བ་ནི་མཚོན་པ་སྟེ་མ་འབད་ན༌[^359]མ་བརྟེན་ནའོ། །

[Block 882]
དེ་ཡང་མུ་དྲ་ཆེན་པོ་དང་དབང་པོ་རང་སྣང་གི་མན་ངག་མི་ལྡན་པར་སྤྱོད་པ་ལ་འཇུག་པའོ། །

[Block 883]
དེས་ན་སྦྲུལ་དང་ཆོམ་རྐུན་ལ་སོགས་པ་ནི་ལོག་པའི་བརྟུལ་ཞུགས་སྦྱང་པའི་ཉེས་དམིགས་སོ། །

[Block 884]
ལས་ཀྱི་ཕྱག་རྒྱ་དེ་དག་ཐ་མལ་སྤོང་བའི་ཕྱིར་ཕྱག་རྒྱས་གདབ་པ་གང༌[^360]གི་ཕྱིར་ཞེ་ན། ཐར་པའི་རྒྱུར་ནི་བརྗོད་པར་བྱ། །ཞེས་པའོ། །

[Block 885]
གང་དག་གིས་ཤེ་ན། རིགས་ལྔའི་ཞེས་པ་སྟེ། རྡོ་རྗེ་པདྨ་ལ་སོགས་པ་ཚིགས་སུ་བཅད་པ་གཅིག༌[^361]སྟེ། གང་ལྟར་དང༌[^362]ཞེ་ན། རྡོ་རྗེ་འདིས་ནི་ཞེས་པ་སྟེ། ཚིག་རྐང་གཉིས་ཀྱིས་སོ། །

[Block 886]
དེ་ཡང་རྡོ་རྗེ་ལ་སོགས་པ་གང་ལ་གང་གིས་རྒྱས་བཏབ་པས། དེ་དེའི་རང་བཞིན་དུ་གྱུར་པས་ཐ་མལ་པ་སྤངས་ནས་ཐར་པའི་རྒྱུར་འགྱུར་བའོ། །

[Block 887]
དེ་ལ་སློབ་དཔོན་ཁ་ཅིག་ནི་གསང་བའི་གནས་ཀྱིས་རྒྱས་བཏབ་པ་ལ་འདོད་དེ། འདིར་མཐུན་པ་མ་ཡིན་ནོ། །གང་ལ་ཞེ་ན། །རྡོ་རྗེའི་ཕྱག་རྒྱས་གཡུང་མོ་ཉིད། །ལ་སོགས་པའི་ཚིགས་སུ་བཅད་པ་གཅིག་སྟེ། དེ་རྣམས་ཀྱང་གཉིས་པའི་དོན་གྱིས་དང་པོར་ཤེས་པར་བྱའོ། །

[Block 888]
གར་མ་ལ་སོགས་པ་ནི་དེ་ལྟར་ཡིན་ན། སྐྱེད་བྱེད་མ་ལ་སོགས་པ་ཇི་ལྟ་བུ་ཞེ་ན། འདི་རྣམས་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 889]
དེར་ཡང་།

[Block 890 [VERSE]]
མདོར༌[^363]བསྡུས་པར་ནི་བརྗོད་པར་བྱ། །
ཞེས་པ༌[^364]ནི་རྡོ་རྗེ་འཆང་རིགས་དྲུག་པའོ། །
འདི་རྣམས་ཞེས་བྱ་བ་ནི་སྔར་གྱིའོ། །

[Block 891]
དེ་བཞིན་གཤེགས་པའི་རིགས་ཞེས་པ་ནི། རྡོ་རྗེ་འཆང་ཡིན་ཡང་སྐུ་གསུང་ཐུགས་ཀྱི་རང་བཞིན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 892]
དེ་བཤད་པའི་ཕྱིར་དཔལ་ལྡན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 893]
དེ་ཡང་དཔལ་ལྡན་རྡོ་རྗེ་འཆང་བདེ་བ་ཆེན་པོའི༌[^365]སྐུའོ། །

[Block 894]
དེ་བཞིན་ཉིད་གཤེགས་ཤིང་ཞེས་པ་ནི་ཆོས་ཀྱི་སྐུར་ཏེ། །

[Block 895 [VERSE]]
སྐྱེད་བྱེད་མ་ལ་རྒྱས་གདབ་པའོ། །
དེ་བཞིན་སླར་ཡང་གཤེགས་པ་ཉིད། །
ཅེས་པ་ནི་གཟུགས་སྐུ༌[^366]སླར་བྱུང་བ་སྟེ།
ལོངས་སྐུས་སྲིང་མོ་ལ་རྒྱས་གདབ་པའོ། །

[Block 896]
སྤྲུལ་སྐུས་བུ་མོ་ལའོ། ། ཤེས་རབ་རིག་པ༌[^367]འདི་ཡིས་ནི། །ཆོས་ཀྱི་སྐུ་དང༌[^368]ཐབས་ཀྱི་རིག་པས་གཟུགས་སྐུ་ལོངས་སྐུས་མཚོན་ནོ། །

[Block 897]
དབྱེར་མེད་རིགས་པ་འདི་ཡིས་ནི་སྤྲུལ་སྐུ་མཚོན་ནོ། །

[Block 898]
དེ་བཞིན་གཤེགས༌[^369]ཞེས་བརྗོད་པར་བྱ། །ཞེས་པ་ནི་རྡོ་རྗེ་འཆང་བདེ་ཆེན་གྱི་སྐུ་ཡིན་ཡང་། དེའི་ཆོས་སྐུ་གསུམ༌[^370]གྱི་རིགས་པས་དེ་བཞིན་གཤེགས་པའི་རིགས་སུ༌[^371]བཏགས་སོ། །

[Block 899]
འོ་ན་རིགས་རྣམས་དུ་ཡོད་ཅེ་ན། རིགས་ནི་ཞེས་བྱ་བ་ལ་སོགས་པ་ཚིགས་སུ་བཅད་པ་གཅིག་གི༌[^372]དབྱེ་བ་དང་བསྡུ་བས། གཅིག་ཉིད་དྲུག་དང་ལྔ་དང་གསུམ་དུ་བསྟན་།[^373] །དེ་ཡང་དག་པའི་གནས་སྐབས་ན་རྣམ་པར་རྟོགས༌[^374]རིགས་སུ་དབྱེ་བ་མེད༌[^375]བཞིན་དུ་དབྱེ་བ་ཇི་ལྟ་བུ་ཞེ་ན།[^376] བདེན་ཏེ་མ་དག་པའི་གནས་སྐབས་ཀྱི་དབྱེ་བས་རྣམ་པར་གཞག་པའི༌[^377]ཕྱིར། རིགས་དང་འབྱུང་བ་ལ་སོགས་པ་ཚིགས་སུ་བཅད་པ་གཅིག༌[^378]གསུངས་སོ། །

[Block 900]
སྤྱིར་རིགས༌[^379]ཐ་དད་པར་འཇོག་པ་ཀུན་རྫོབ། རིགས་གཅིག་པ་དོན་དམ་པ་ཡིན་ཏེ།

[Block 901 [VERSE]]
ཐ་དད་པ༌[^380]ནི་ཆུ་བོ་བཞིན། །
དུ་མ་ཉིད་དུ་བརྗོད༌[^381]མི་བྱ། །

[Block 902]
ཞེས་སོ། །

[Block 903]
ལ་ལ་དག་ནི་ཇི་སྲིད་དུ་ཁས་ལེན་པ་དེ་སྲིད་དུ་གཞན་སེལ་བར་གནས་ཏེ། དཔེར་ན་རྒྱུའི་ཚོགས་པ་ཐ་དད་པ་ལས་འབྲས་བུ་ཐ་དད་པར་སྣང་སྟེ། དཔེར་ན་མར་མེ་ཐ་དད་པས༌[^382]སེལ་བའི་མུན་པ་གཅིག་ལས་མེད་ཀྱང་མར་མེ་ནི་གཅིག་ཏུ་གྱུར་པ་མ་ཡིན་ནོ། །

[Block 904]
དེ་ཡང་། ཚོགས་དང་ཆོས་ཀྱི་སྐུ་དག་དང་།

[Block 905 [VERSE]]
འགྲོ་བའི་དོན་རྣམས་སྤྱོད་པ་ནི། །
སངས་རྒྱས་ཐམས་ཅད་མཚུངས་པ་ཡིན། །

[Block 906]
ཞེས་གསུངས་སོ། །

[Block 907]
རིགས་པས་དཔྱད་ན་ནི་ཡིད་ཀྱི་སྤྱོད་ཡུལ་དུ་ཤིན་ཏུ་དགའ་བས་ཆོག་གོ། །

[Block 908]
ད་ནི་བསྒོམ་པའི་ཉམས་བསྟན་པའི་ཕྱིར༌[^383]སྒོམ་པ་མེད་ཅེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 909]
དེ་ཡང་ལྟ་བ་ཤེས་རབ་ཀྱི་སྐབས་སུ་མིག་གི་དབང་པོ་ལ་སོགས་པ་གཅིག་དང་དུ་བྲལ་རིགས་པས་རང་བཞིན་མེད་པའི་ཕྱིར་སྒོམ་པ་པོ་མེད་ཅེས་པའོ། །

[Block 910]
ཡང་ལྟ་བའི་སྐབས་སུ་གཟུགས་ལ་སོགས་པ་མེད་པའི་ཕྱིར་བསྒོམ་པ་ཡང་མེད་ཅེས་ལྷག་མའོ། །

[Block 911]
བསྒོམ་བྱ་མེད་ཅེས་བྱ་བ༌[^384]ནི་འང་སྟེ། སྔ་མ་གཉིས་ལྟ་བུའོ། །

[Block 912]
དེ་ཡང་ལྟ་བའི་སྐབས་སུ་སེམས་དང་སེམས་ལས་བྱུང་བ་རང་བཞིན་མེད་པའི་ཕྱིར་རོ། །

[Block 913]
འོན་ཏེ་བསྒོམ་པ་ནི་ལམ་གྱི་གཙོ་བོ་ཡིན་ན། དེ་མེད་ན་འབྲས་བུ་དང་ལམ་གཞན་དག་ཇི་ལྟར་ཡོད་པར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར། ལྷ་དང་སྔགས་ཀྱང་ཡོད་མ་ཡིན། །ཞེས་གསུངས་སོ། །

[Block 914]
དེ་ཡང་འབྲས་བུ་གཞན་དག་ཉེ་བར་མཚོན་པ་སྟེ། སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཀྱང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 915]
ལམ་ཡང་གཞན་དག་ཉེ་བར་མཚོན་པ་སྟེ། ཕྱག་རྒྱ་དང་དཀྱིལ་འཁོར་དང་སྒྲུབ་པ་དང་ཕྲིན་ལས་ཀྱང་ཡོད་པ་མ་ཡིན་ནོ། །
--- END BLOCKS ---
