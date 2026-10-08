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
[Block 3046]
བྱིན་གྱིས་རློབ་པའི༌[^1244]ཚེ། ཨཾ་ཧཱུཾ་ཨེ་ཝཾ་གྱི་བརྡས་ཤེས་རབ་དང་ཐབས་སུ་བྱས་པའོ། །

[Block 3047]
གཞན་དག་ནི་དེ་བཞིན་ནོ། །

[Block 3048]
དེའི་དོན་ནི་འདི་ཡིན་ཏེ། གཏོར་མ་སྔར་བཤད་པའི་བདུད་རྩི་སྦྱངས་པས་བསྒྲུབས༌[^1245]ནས་ཆོས་ཀྱི་འབྱུང་གནས་ནང་དུ་ནི།

[Block 3049 [VERSE]]
པདྨ་འདབ་མ་སུམ་བརྩེགས་བསམ། །
དཀར་དང་སྔོ་དང་དམར་བ་སྟེ། །
སྟེང་དུ་ཨོཾ་ལས་ཚངས་ལ་སོགས། །
བར་དུ་ཧཱུཾ་ལས་བརྒྱ་བྱིན་སོགས། །

[Block 3050 [VERSE]]
འོག་ཏུ་ཨཱཿལས་མཐའ་ཡས་སོགས། །
པདྨའི་མདོག་བཞིན་བསྐྱེད་པར་བྱ། །
རང་བཞིན་སྤྱན་དྲང༌[^1246]གཉིས་མེད་བསྟིམ། །
བྱིན་བརླབ་དབང་བསྐུར་ཚུལ་བཞིན་བྱ། །

[Block 3051 [VERSE]]
སྟེང་ལ་རྟག་པ་མི་བསྐྱོད་དབུས། །
འོག་མ་སྣང་བ་མཐའ་ཡས་མཚན། །
ལྗགས་ལ་རྡོ་རྗེར་བརླབས་ལ་དབུལ། །
བསྔོ་བ་གཉིས་ཏེ་ཟང་ཟིང་ཆོས། །

[Block 3052 [VERSE]]
རིམ་པ་བཞིན་དུ་བསྔོ་བའོ། །
ཕན་ཡོན་གཉིས་ཏེ་རེ་ཞིག་དང་། །
རྒྱུན་དུ་བྱིན་པའི་ཕན་ཡོན་ནོ། །

[Block 3053]
ཡང་སྔར་ནི་ཕྱག་རྒྱའི་ངེས་པ་བསྒྲུབ་པ་ལས་མཁའ་སྤྱོད་མ་ལ་སོགས་པ་རིགས་གསུམ་དུ་བྱ་བ་དང་རིགས་ཀྱི་དབྱེ་བ་གོ་སླའོ། །

[Block 3054]
ལེའུ་བཞི་པའོ།། །།

[Block 3055 [HEADING]]
### ལེའུ་ལྔ་པ། ^2-5-0

[Block 3056]
ད་ནི་ཧེ་རུ་ཀ་ཕྱག་བཅུ་དྲུག་པ་ལས༌[^1247]གསུངས་པ།[^1248] དེའི་སྒྲུབ་ཐབས་བཤད་པར་ཞུས་པ་ནི། ཕྱག་ནི་བཅུ་དྲུག་ཞལ་བརྒྱད་པ། །ཞེས་པ་ནི་རྡོ་རྗེ་འཆང་ལ་བདག་མེད་མས་གསོལ་བ་གདབ་པའོ། །

[Block 3057]
དཔའ་བོ་ཐོད་པའི་ཕྲེང་བ་ཅན་ནི་མི༌[^1249]མགོ་ལྔ་བཅུའི་ཕྲེང་བ་འཕྱང་སྟེ་འདུ་བྱེད་ལྔ་བཅུ་དག་པའོ། །

[Block 3058]
གཞན་དག་ནི་རྣམ་པར་དག་པ་སྔར་བཤད་ཟིན་ཏོ། །

[Block 3059]
བཅོ་ལྔས༌[^1250]ཡོངས་སུ་བསྐོར་བའི་བདག་གི་འཁོར་ལོ་ཁྱེད་ཀྱིས་བཤད་ནི་ལེའུ་བརྒྱད་པར་གསུངས་པའོ། །

[Block 3060]
ཁྱོད་ཀྱི་དཀྱིལ་འཁོར་ཇི་ལྟར་ལགས། །ཞེས་དྲིས་པའོ། །

[Block 3061]
བདག་མེད་མ་ལ་འོ་མཛད་ནས། །ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་ཞེ་སྡང་ཅན་དང་ཆགས་པ་ཅན་འདུལ་བའི་དོན་ཏོ། །

[Block 3062]
འཁོར་ལོ་ཇི་ལྟར་སྔར་གསུངས་པ། །ཞེས་པའི་དོན་འདིར་སྒྲུབ་པའི་ཐབས་ནི་སྒྲུབ་པ་པོས་གནས་གང་ཡང་རུང་བར་བྱ་བ་དང་། ཚོགས་བསགས་པ་དང་། སྲུང་བ་མཚམས་དང་ཆོས་ཀྱི་འབྱུང་གནས་བསྒོམ་པ་སྔ་མ་ལྟར་བྱས་ལ།

[Block 3063 [VERSE]]
འཁོར་ལོ་ས་དང་ཆུ་ནི་སྔོན། །
ཇི་ལྟར་རིགས་པར༌[^1251]བྱིན་ཟ་ཡི། །

[Block 3064]
ཞེས་ལེའུ་བརྒྱད་པ་ལྟར་བསྒོམས་ལ། ཁྱད་པར་ནི་འཕར་མ་གཅིག་པ་ལ་སོགས་པ་དང་ལྡན་པའི་རྗེས་ལ། ཚངས་པ་དབང་པོ་ཉེ་དབང་དྲག །ལ་སོགས་པ་སྦྱར་ལ། དུར་ཁྲོད་བརྒྱད་དང་བཅས་པའི་དབུས་སུ༌[^1252]བདུད་བཞི་བསྣོལ་མར་བསྒོམས་ནས་ཨ་ལ་བཛྲ་ཞེས་པའི་སྔགས་བརྗོད་དོ། །

[Block 3065]
དེ་སྐད་དུ་ཡང་།

[Block 3066 [VERSE]]
མི་མཉམ་མེད་པས་གྲུ་བཞི་སྟེ། །
དྲན་པས་དབང་པོ་སྒོ་བཞི་ཡིན། །
རྣམ་ཐར་བརྒྱད་ཀྱི་ཀ་བ་སྟེ། །
ཏིང་འཛིན་བཞི་ཡི་ཁ་ཁྱེར་ཏེ། །

[Block 3067 [VERSE]]
བསམ་གཏན་བཞི་ཡི་རྟ་བབས་ཅན། །
འདོད་པའི་ཡོན་ཏན་ལྔ་ཡིས་སྤྲས། །
ཉོན་མོངས་ཆེ་ཆུང་རྣམ་དག་པའི། །
དྲ་བ་དང་ནི་དྲ་བ་ཕྱེད། །

[Block 3068 [VERSE]]
ཁམས་གསུམ་བདག་ནི་མེད་པ་ཡི། །
དུར་ཁྲོད་བརྒྱད་ཀྱིས༌[^1253]ཉེ་བར་མཛེས། །
ཚངས་པ་ལ་སོགས་མནན་པ་ནི། །
ཐ་མལ་རྣམ་སྦྱོང་གཞལ་ཡས་ཁང་། །

[Block 3069]
རྟེན་གྱི་རྣལ་འབྱོར་དྲོད་གཤེར་ལས་སྐྱེས་པ་དང་མཐུན་པ་རྣམ་པར་སྣང་མཛད་ཀྱི་རྣམ་པར༌[^1254]དག་པའོ། །

[Block 3070]
དེ་ནས་འདོད་ཆགས་ཆེན་པོ་རྗེས་ཆགས་ཞེས་བྱ་བ་ཤློ་ཀ་གཅིག་སྦྱར་ཏེ། དེ་ལ་དབུས་སུ་ང་ཡོད་ཅེས་བྱ་བ་ནི་རྡོ་རྗེ་འཆང་བསྐྱེད་པ་སྟེ།

[Block 3071 [VERSE]]
ཨཱ་ལི་ཟླ་བ་ཀཱ་ལི་ཉི། །
ས་བོན་ནང་དུ་སོན་གྱུར་པ། །
དེ་ཉིད༌[^1255]སེམས་དཔའ་ཞེས་བྱར་བརྗོད། །

[Block 3072]
ནམ་མཁའི་དཀྱིལ་འཁོར་ཁྱབ་པ་ནི།[^1256] །

[Block 3073 [VERSE]]
རང་གི་ལུས་མཚུངས་རྣམ་པར་སྤྲོ། །
བསྡུས་ནས་སྙིང་གར་དགུག་པ་ནི། །
ཡོ་གི་ཞེ་སྡང་བདག་ཉིད་ཅེས། །
མངོན་པར་བྱང་ཆུབ་ལྔ་སྦྱར་ཏེ། །

[Block 3074 [VERSE]]
ཟླ་བ་མེ་ལོང་ཡེ་ཤེས་ལྡན། །
བདུན་གྱི་བདུན་པ་མཉམ་ཉིད་ལྡན། །
རང་ལྷའི་ས་བོན་ཕྱག་མཚན་ནི། །
སོ་སོར་རྟོག་པ་ཡིན་ཞེས་ཟེར། །

[Block 3075 [VERSE]]
དེ་རྣམས་གཅིག་གྱུར་བྱ་ནན་ཏན། །
རྫོགས་པ་ཆོས་དབྱིངས་དག་པའོ། །

[Block 3076]
ཞེས་པ་རྡོ་རྗེ་འཆང་སྐུ་མདོག་དཀར་པོ་གོང་དུ་གསུངས་པ་དང་། འོག་ནས་འཆད་པའི་ཕྱག་མཚན་ལ་སོགས་པ་དང་ལྡན་བར་བསྐྱེད་ལ། རྡོ་རྗེ་དང་པདྨ་བྱིན་གྱིས་བརླབས་ལ་རྗེས་སུ་ཆགས་པའི་སྔགས་བརྗོད་པ་ནི་རྗེས་སུ་ཆགས་པའི་ཡན་ལག་སྟེ་སྒོང་སྐྱེས་དང་ཆོས་མཐུན་པའོ། །

[Block 3077]
དེའི་རྗེས་ལ།

[Block 3078 [VERSE]]
གྲོང་ཁྱེར་ཉམས་དགར་ཁྱོད་དང་ང་། །
དགའ་བས་ཤིན་ཏུ་རོལ་པ་ལས། །

[Block 3079]
ཞེས་སྦྱར་ཏེ། དེ་ཡང་།

[Block 3080 [VERSE]]
དང་པོ་སྐྱེས་བུ་བསམ་དེ་ནས། །
མཁའ་འགྲོ་མ་ཡི་འཁོར་ལོ་སྤྲོ། །

[Block 3081]
ཞེས་གསུངས་ཏེ་འཁོར་རྗེས་སུ་མཐུན་པའི་བྱང་ཆུབ་པ་ལྔས༌[^1257]མངལ་སྐྱེས་ཀྱི་སྒོང་སྐྱེས་དང་འདྲ་བར་བསྐྱེད་དེ། གཾ་ཙཾ་ལ་སོགས་པ་ཚིག་གཉིས་སྦྱར་རོ། །

[Block 3082]
དེའི༌[^1258]དོན་ནི་སྙིང་ག་ནས་འོད་འཕྲོས་སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་བཀུག་ནས་ཞལ་དུ་ཞུགས། སྙིང་གར་ཞུ། སྲོག་དག་པའི་ལམ་ནས་བྱུང་སྟེ། ཡུམ་གྱི་པདྨར་ཐིག་ལེ་དེ་ལས་ས་བོན་བརྒྱད་དུ་གྱུར་པ་དང་། མདུན་གྱི་ཚངས་པའི་གདན་སྟེང་དུ་ཨཱ་ལི་ལས་ཟླ་བ་ཀཱ་ལི་ལས་ཉི་མ་དེའི་བར་ན༌[^1259]གཾ །དེ་ལས་གྲི་གུག །[^1260]དེ་སྤྲོ་བསྡུ་བྱས་ནས་ཞུ་བ་ལས་གཽ་རཱི་བསྐྱེད་དེ།

[Block 3083 [VERSE]]
དཀར་མོ་དབང་པོའི་ཕྱོགས་ཕྱུང་ནས། །
ཞེས་བྱ་བ་ལ་སོགས་པ་སྦྱར་རོ། །
རླུང་གི་མཚམས་སུ་གཡུང་མོ་ནི། །

[Block 3084]
ཞེས་པའི་མཐར་ཏེ། རླུང་མཚམས་ནི༌[^1261]ཉི་མའི་སྟེང༌[^1262]ན་ཐགས༌[^1263]བཟངས་རིས་མནན་པའི་སྟེང་དུ་ཨཱ་ལི་ལས༌[^1264]ཟླ་བ་ཀཱ་ལི་ལས་ཉི་མ། དེ་གཉིས་བར་དུ་ཌཾ་དེ་ལས་རྡོ་རྗེ་ལ་ཌཾ་གིས་མཚན་པ་དེ་སྤྲོས་བསྡུས་ནས་ཞུ་བ་ལ་གཡུང་མོ་བསྐྱེད་དོ། །

[Block 3085]
གཞན་ལ་ཡང་དེ་བཞིན་སྦྱར་རོ། །
--- END BLOCKS ---
