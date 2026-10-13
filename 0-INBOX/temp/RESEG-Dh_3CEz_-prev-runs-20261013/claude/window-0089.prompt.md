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
[Block 3116 [VERSE]]
གང་ཡང་ཕྱིན་ཅིང་འདོད་དགུར་ལྡན། །
དགའ་མགུར་སྤྱོད་པ་བདེ་བས་སོ། །

[Block 3117]
དེ་སྐད་དུ་ཡང་།

[Block 3118 [VERSE]]
འགྲོ་བ་རྣམས་ཀྱི་ནང་ན་ནི། །
མི་རྣམས་ཀྱི་ནི་འགྲོ་བ་མཆོག །
དེ་རྣམས་ནད་ནི་ཞི་དོན་དུ། །
གླང་པོ་ལ་སོགས་འཛིན་པ་ནི། །

[Block 3119]
ཉིད་ཀྱི་སྐུ་ལ་ཟློག་པར་མཛད། །ཅེས་པའོ། །

[Block 3120 [VERSE]]
སྒེག་ཅིང་དཔའ་བ་མི་སྡུག་པ། །
རྒོད་ཅིང་དྲག་ཤུལ་འཇིགས་སུ་རུང་། །
སྙིང་རྗེ་རྔམ་དང་ཞི་བ་ཡི། །
གར་དགུའི་རོ་དང་ལྡན་པ་ཉིད། །

[Block 3121]
ཅེས་པ།

[Block 3122 [VERSE]]
རིག་མ་ལ་འཁྱུད་བདུད་བཞི་མནན། །
སྨིན་མ་བཅུམ་ཞིང་ཞལ་གདངས་པ། །
ཐོད་པའི་དོ་ཤལ་མཆེ་བ་གཙིགས། །
སྤྲུལ་པ་འཕྲོ་ཞིང་ཐོད་ཁྲག་གང་། །

[Block 3123 [VERSE]]
བརྒྱད་པོ་རིམ་པར་སྦྱར་བྱས་ལ། །
ཞི་བ་སྤྱིར༌[^1276]ནི་སེམས་ཅན་དོན། །

[Block 3124]
དེའི་རྗེས་སུ།

[Block 3125 [VERSE]]
དཀར་མོ་གཡས་ན་གྲི་གུག་སྟེ། །
ཞེས་པ་ལ་སོགས་པ་སྦྱར་རོ། །

[Block 3126]
སྔར་འཁོར་བསྐྱེད་ཀྱང་གཙོ་བོ་མ་བསྟན་པས་མ་བཤད་ལ། འདིར་གཙོ་བོ་བསྟན་པས་དེའི་རྗེས་སུ་འཁོར་བསྟན་པར་དགོངས་སོ། །

[Block 3127]
གཡས་པ་ཐབས་ཀྱི་ཉོན་མོངས་འཇོམས་ལ། གཡོན་པ་ཤེས་རབ་ཀྱི་ཆོས་འཆད་པ་ལ་སོགས་ཀུན་ལ་སྦྱོར་རོ། །

[Block 3128]
དེའི་རྗེས་སུ་མ་མོའི་འཁོར་ལོ་གྲོང་ཉམས་དགའ་ཞེས་པ་ཤློ་ཀ་གཅིག་སྦྱར་ཏེ། སེམས་དཔའ་སུམ་བརྩེགས་བསྒོམས་ཏེ།

[Block 3129 [VERSE]]
ཐམས་ཅད་རྡོ་རྗེ་འདི་ཡིས་ནི། །
རང་སྔགས་ཡི་གེ་རྫོགས་པ་དང་། །
ས་བོན་ཕྱག་མཚན་གྱུར་པ་ལས། །
སྐུ་རང་འདྲ་བ་སྒོམ་པར་བྱེད། །

[Block 3130 [VERSE]]
དེ་ཡི་ཐུགས་ཀའི་ས་བོན་ལས། །
ལྷ་དགུའི་རྣམ་པར་སྤྱན་དྲངས་ཏེ། །
ཕྱག་མཚན་རྡོ་རྗེ་ཧཱུཾ་གིས་མཚན། །
རྗེས་ཀྱི་ཡེ་ཤེས་ཏིང་འཛིན་སེམས། །

[Block 3131 [VERSE]]
ལྷ་རྣམས་ཀུན་ལ་བསྒོམ་པར་བྱ། །
དེ་ནས་རྫོགས་པར་བྱ་བའི་ཕྱིར། །
ཡེ་ཤེས་འཁོར་ལོ་དགུག་པ་སྟེ། །
དམ་ཚིག་འཁོར་ལོ་ལ་མཉམ་ཐིམ། །

[Block 3132]
ཡེ་ཤེས་འཁོར་ལོ་ཆེན་པོ་འབར། །རང་གི་ཏིང་ངེ་འཛིན་སེམས་དཔའ་ལ་འོད་ཟེར་འཕྲོས་ཏེ། སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་ལྷ་དགུའི་རྣམ་པར་སྤྱན་དྲངས་ཏེ། གཞལ་ཡས་ཁང་གི་ཕྱི་རོལ་དུ་བྱོན་པ་ལ། རང་གི་སྙིང་ག་ནས་གཽ་རཱི་ལ་སོགས་པ་སྤྲོས་ཏེ་ཨོཾ་སརྦ་ཏ་ཐཱ་ག་ཏ་པཱུ་ཛ་ཞེས་མཆོད་པ་བྱས་ལ་གཽ་རཱི་ལ་སོགས་པ་བཞིས་དགུག་པ༌[^1277]ལ་སོགས་པ་བྱའོ། །

[Block 3133]
དེ་ནས་མ་བརྟས་བརྟས༌[^1278]པར་བྱེད་པ་སྐྱེ་མཆེད་བྱིན་གྱིས་བརླབ་པ་དང་། སྐུ་གསུང་ཐུགས་བྱིན་གྱིས་བརླབ་པ་སྔར་དང་མཐུན་པར་བྱའོ། །

[Block 3134]
དེ་ནས་དབང་བསྐུར་བ་སྟེ་སྔ་མ་བཞིན་སྤྱན་དྲངས་པ་ལ་ཡང་མཆོད་པ་སྔ་མ་ལྟར་བྱའོ། །

[Block 3135]
དེ་ནས་གསོལ་བ་གདབ་པ་ཨོཾ་སརྦ་ཏ་ཐཱ་ཏ་ཨ་བྷི་ཥིཉྩ་ཏུ་མཱཾ་ཞེས་བརྗོད་ལ་ལེའུ་གསུམ་པ་བཞིན་དབང་བསྐུར་བར་བསམ།

[Block 3136 [VERSE]]
གོང་གི་རང་གི་རིགས་ཀྱིས་དབུ་བརྒྱན་ནོ། །
དེ་ནས་དབང་བསྐུར་བའི་སྔགས་བརྗོད་པར་བྱའོ། །

[Block 3137]
དེ་ནས་རང་གི་ཐུགས་ཀ་ནས་གཽ་རཱི་བྱང་ཆུབ་ཀྱི་སེམས་འཛིན་པ་ལ་སོགས་པ་སྤྲོས་ཏེ། ལྷ་མོ་བཅུ་དྲུག་གིས་བདག་དང་དཀྱིལ་འཁོར་གྱི་ལྷ་རྣམས་མཆོད་ནས་མཆོད་པའི་སྔགས་ཀྱང་བརྗོད་དོ། །

[Block 3138 [VERSE]]
བསྟོད་པ་ལས༌[^1279]འབྱུང་བ་རྣམས་བརྗོད་ལ། །
བསྟོད་པའི་སྔགས་ཀྱང་བརྗོད་དོ། །
བདུད་རྩི་མྱང་བ་ཡང་བྱ་སྟེ། །
ཡཾ་ལས་རླུང་དང་རཾ་ལས་མེ། །

[Block 3139 [VERSE]]
ཀཾ་ལས་ཐོད་པ་རྣམ་གསུམ་བསྐྱེད། །
ཨ༌[^1280]ལས་ཐོད་པ་ཆེན་པོ་སྟེ། །
ཉི་ཟླ་ཁ་སྦྱོར་ནང་དུ་ནི། །
ས་བོན་མིང་ནི་ཡི་གེ་ལས། །

[Block 3140 [VERSE]]
བདུད་རྩི་ལྔ་དང་ཤ་ལྔ་བསམ། །
དེ་སྟེང་ཧཱུཾ་ལས་རྡོ་རྗེ་ནི། །
ཁ་བཅང་རྒྱ་གྲམ་ཧཱུཾ་གིས་མཚན། །
སྙིང་གའི་ཧཱུཾ་ལས་འོད་ཟེར་སྤྲོས། །

[Block 3141 [VERSE]]
རྒྱ་གྲམ་ཧཱུཾ་གིས་བ་དན་བསྐྱོད། །
མེ་སྦར་རྫས་རྣམས་ཞུ་བ་ལས། །
ཨོཾ་ལས་འོད་བྱུང་ཡེ་ཤེས་ཀྱི། །
བདུད་རྩི་བཀུག་ནས་རྡོ་རྗེ་ཞུ། །

[Block 3142 [VERSE]]
དེ་ཉིད་གསུམ་གྱིས་བྱིན་གྱིས་བརླབ། །
དཀྱིལ་འཁོར་བ་ཡི་ལྷ་རྣམས་ཀྱི། །
ལྗགས་ལ་རྡོ་རྗེ་ནས་འབྲུ་ཙམ། །
བསམས་ཏེ་སོ་སོར་རང་སྔགས་ཀྱིས། །

[Block 3143]
བརྗོད་པས་བདུད་རྩིས་ཚིམ་པར་བསམ། །ཨོཾ་སརྦ་ཏ་ཐཱ་ག་ཏ་ཨ་མྲྀ་ཏ་སུ་སཏྭཱ་ནཱཾ་བཛྲ་སྭ་བྷཱ་བ་ཨཱཏྨ་ཀོ྅ཧཾ། །དེ་ནས་ནག་པོ་རབ་ཏུ་བསྒོམ། །ཞེས་བྱ་བ་ལ་སོགས་པ་ཁ་དོག་ཡན་ལག་དྲུག་གི་རྣལ་འབྱོར་དང་། ཕྲ་མོའི་རྣལ་འབྱོར་ལེའུ་བརྒྱད་པ་ལྟར་བསྒོམས་ལ། རྫོགས་པའི་རིམ་པ་ནི་ཕྱག་རྒྱ་ཆེན་པོའི་གདམས་ངག་གམ་ཨ་བ་དྷཱུ་ཏཱི་རྣམ་གསུམ་གྱི་མན་ངག་གམ། གཏུམ་མོ་ལ་སོགས་པ་གང་ཡང་རུང་བ་ཅིག༌[^1281]བསྒོམས་ལ་དག་པ་རྗེས་སུ་དྲན་པ་དང་སྔགས་བཟླས་པ་དང་འོག་ནས་འབྱུང་བའི༌[^1282]གཏོར་མ་ཡང་གཏང་བར་བྱ་སྟེ། ཐུན་བཞིའི་རིམ་པས་བསྒོམ་པར་བྱའོ། །

[Block 3144]
དེ་ལ་རྟགས་ལ་སོགས་པ་སྦྱར་བ་དང་སྤྱོད་པའི་རིམ་པ་སྔར་བསྟན་པ་བཞིན་དུ་བྱའོ། །

[Block 3145]
ད་ནི་དེ་ལ་སྔགས་བསྟན་པ་ནི། བོ་ལ་གཞིབ་པར་མཛད་ནས་ནི། །ཞེས་བྱ་བ་ལ་སོགས་པ་ངོ་མི་ཆོགས་པས་ཁྱེད་ལ་བཤད་ཅེས་བྱ་བ་ལ་སོགས་པ་ནི་ཕན་ཡོན་དང་བཅས་པའི་སྔགས་བརྗོད་པར་ཞལ་གྱིས་བཞེས་པའོ། །

[Block 3146 [VERSE]]
འབར་བའི་ཕྲེང་བ་འཁྲུག་པ་ཡིན། །
དཀྱིལ་འཁོར་རབ་ཏུ་བཞེངས་ནས་ནི། །

[Block 3147]
ཞེས་བྱ་བ་ཟླ་བ་ལྟ་བུའི་བསམ་གཏན་དང་། ཆུ་ཟླ་ལྟ་བུའི་དཀྱིལ་འཁོར་པ་བསྒོམས་ལ། སྒྲ་རིང་བ་དང་བཟང་བ་ཡིས། །ཞེས་པ་ནི་སྒྲ་བརྙན་དང༌[^1283]བྲག་ཅ་ལྟ་བུའི་བཟླས་པ་སྟེ།

[Block 3148 [VERSE]]
བཟླས་པ་འབུམ་གྱིས་རྣལ་འབྱོར་བདག །
ཅེས་པ་ནི་བསྙེན་པའི་གྲངས་སོ། །
བཟླས་པ་ཁྲི་ཡིས་གསལ་བ་དང་། །
ཞེས་པ་ནི་སྒྲུབ་པའི་གྲངས་སོ། །

[Block 3149]
རིག་བྱེད་རྣམས་ཀྱི་དང་པོ་སྦྱིན། །ཞེས་པ་ནི་སྔགས་བཏུ་བ་སྟེ་རིག་བྱེད་ནི་བཞི་སྟེ་མཆོད་སྦྱིན་གྱི་རིག་བྱེད་དང་། །སྙན་དངགས་ཀྱི་རིག་བྱེད་དང་། སྲིད་སྲུང་གི་རིག་བྱེད་དང་། ངེས་བརྗོད་ཀྱི་རིག་བྱེད་དེ། དེ་ནས་ཨོཾ་ལས་འདྲེན་པ་སྟེ། ཟླ་ཕྱེད་ཐིག་ལེས་རྣམ་པར་བརྒྱན་པ་ནི་ཨོཾ། དེ་ནས་ནི་སྔགས་རིལ་པོར་བཏུས་བ་སྟེ། ཨཥྚ་ལ་སོགས་པའོ། །

[Block 3150]
འདིར་དགོངས་པ་ནི་གཙོ་བོ་དང་འཁོར་གྱི་གྲངས་ནི་སྔར་བསྟན་ཟིན་ནོ།[^1284] །གཙོ་བོའི་བཟླས་པ་ལ་ཞི་བ་དང་ཁྲོ་བོའི་སྟེ། ཞི་བའི་སྔགས་ཀྱི་ལེའུར་བཤད་ཟིན་ནོ། །

[Block 3151]
ཁྲོ་བོའི་འདི་ཡིན་ཏེ།

[Block 3152 [VERSE]]
འབྲས་བུ་ཧེ་རུ་ཀའི་ང་རྒྱལ་གྱིས་བཟླས་པ་བྱའོ། །
སྔགས་ཀྱི་འབྲས་བུའི་དོན་ནི་གཞན་དུ་ཤེས་པར་བྱའོ། །

[Block 3153]
དེ་ནས་ལྷ་མོ་དེ་དགྱེས་ནས་ཞེས་པ་ལ་སོགས་པ་སྒྲུབ་པའི་དཀྱིལ་འཁོར་ཞུས་པའོ། །

[Block 3154 [HEADING]]
#### ཉིད་ཀྱི་དཀྱིལ་འཁོར་བྲི་བར་མཛད། ^2-5-1-0

[Block 3155 [HEADING]]
##### སྔོན་བྱུང། ^2-5-1-1-0
--- END BLOCKS ---
