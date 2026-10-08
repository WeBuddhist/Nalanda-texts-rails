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
[Block 3326]
སྔགས་ཀྱི་རིམ་པ་ཀུན་ཤེས་ནས་ནི་བྱ་བ་དང་སྤྱོད་པ་དང་རྣལ་འབྱོར་རྒྱུད་དེ་ཕྱི་རོལ་དབྱིབས༌[^1338]ཀྱི་རྣལ་འབྱོར་བསྟན་པའོ། །

[Block 3327]
དགྱེས་པའི་རྡོ་རྗེ་མཐར་ཐུག་ཕྱག་རྒྱ་ཆེན་པོ་ལྷན་ཅིག་སྐྱེས་པ་བསྟན་པའོ། །

[Block 3328]
དེ་སྐད་དུ།

[Block 3329 [VERSE]]
དང་པོ་ཞིང་ནི་སྦྱང་བའི༌[^1339]ཕྱིར། །
དྲུག་ཅུ་པ་ཡི་ཁ་ཟས་གདབ། །
དེ་ནས་འབྲུ་རྣམས་རིམ་གྱིས་གདབ། །
ཕྱི་ནས་འབྲས་དཀར་ས་བོན་ནོ། །

[Block 3330 [VERSE]]
བསླབ་ཚིག་ལྔ་པའི་རིམ་པ་ཡིས། །
རྒྱུད་ནི་དེ་ལྟར་སྦྱང་བར་བྱ། །

[Block 3331]
ཞེས་གསུངས་སོ། །

[Block 3332]
ལེའུ་བརྒྱད་པའོ།། །།

[Block 3333 [HEADING]]
### ལེའུ་དགུ་པ། ^2-8-0

[Block 3334]
ད་ནི་ཞེ་སྡང་ཅན་གྱི་གང་ཟག་གདུལ་བའི་དོན་དུ།

[Block 3335 [VERSE]]
དེ་ནས་ཁ་སྦྱར་འབྱེད་པ་ཡི། །
མཚན་ཉིད་ཡང་དག་རབ་ཏུ་བཤད། །

[Block 3336]
ཅེས་བྱ་བ་ཤློ་ཀ་གཅིག་གིས་དགོས་པ་བསྟན་ནོ། །

[Block 3337]
བསྟན་པ་ལ་གནོད་པ་བྱེད་པ་དང་ཞེས་པ་ཚིག་གསུམ་གྱིས་ཡུལ་གྱི་གནང་བ་བསྟན་ཏོ། །

[Block 3338 [VERSE]]
སྙིང་རྗེས་གསད་པར་བྱ་བ་ཉིད། །
ཅེས་བྱ་བ་ནི་བསམ་པས་གནང་བའོ། །

[Block 3339]
བསྒྲུབ་བྱའི་རྩ་བ་ལ་ཞེས་བྱ་བ་ལ་སོགས་པས༌[^1340]ནི་སྦྱོར་བར་གནང་བའོ། །

[Block 3340]
སངས་རྒྱས་ཀྱང་ནི་ངེས་པར་འཇིག །ཅེས་པ་ནི་སངས་རྒྱས་ཀྱི་བསྲུང་བ་ཡང་འཇིག་ཅེས་བྱའོ། །

[Block 3341]
ཡང་ན་ལ་དོར་བའི༌[^1341]ཚིག་གོ། །

[Block 3342]
དེ་ཡི་ལམ་དུ་ཁབ་ནི་མེ།[^1342] །ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་ཤེས་པ་སྦྱོང་བ་བསྟན་པའོ། །

[Block 3343]
སྔགས་དང་བསམ་གཏན་ཙམ་གྱིས་གསད་པར་བྱའོ། །

[Block 3344]
སྦྱིན་སྲེག་དང་འཁོར་ལོ་དང་ཕྱག་རྒྱ་དང་རྫས་ཀྱི་སྦྱོར་བ་རྣམས་ནི་སྦྱོར་བས་གནང་བའོ། །

[Block 3345]
མན་ངག༌[^1343]རིམ་པ་ནི་བླ་མ་ལས་ཤེས་པར་བྱའོ། །

[Block 3346 [HEADING]]
#### དེའི་འཐད་པ། ^2-8-1-0

[Block 3347]
དེའི་འཐད་པ་ནི་བརྗོད་བྱ་ནུས་པ་དང་ལྡན་པ་དང་རྗོད་བྱེད་ནུས་པ་དང་ལྡན་པ་སྟེ། རྟོག་མེད་དངོས་གྲུབ་སྦྱིན་པ་པོ། །ཞེས་པ་ཚིག་དང་པོས་རྫོགས་པའི་རིམ་པ་བསྟན་ཏོ། །

[Block 3348]
སྲིད་པ་སྦྱོང་བ་ཉམས་དགའ།[^1344] །ཞེས་པའི་ཚིག་གཅིག་གིས་བསྐྱེད་པའི་རིམ་པ་མདོར་བསྟན་པའོ། །

[Block 3349]
དེའི་རྒྱས་པར་བཤད་པ། རིན་ཆེན་གཟི་བརྗིད་འབར་བ་ཡི། །ཞེས་པ་ལ་སོགས་པའི་དཔེ་དང་དོན་གཉིས་སུ་སྦྱར་ཏེ་དཔེར་ན་མུ་ཏིག་ལ་སོགས་པའི་རིན་པོ་ཆེའི་ཁྱད་པར་རྣམས་བུ་ག་མེད་པར་གྱུར་ན་རྒྱན་ལ་སོགས་པར་མི་བཏུབ་ལ་ཕུག་ན་རྒྱན་ལ་སོགས་པ་དགའ་བ་སྐྱེད་པར་བྱེད་དོ། །

[Block 3350]
དེ་བཞིན་དུ་འདོད་པའི་ཡོན་ཏན་རྣམ་པ་ལྔ་ཐབས་དེ་ཁོ་ན་ཉིད་ཀྱིས་ཟིན་ན་བདུད་རྩི་ལྟ་བུར་འགྱུར་རོ། །

[Block 3351]
དངོས་པོ་ལ་མངོན་པར་ཞེན་པས་ནི་དུག་ཏུ་འགྱུར་རོ། །

[Block 3352]
འཁོར༌[^1345]བའི་རྣམ་པ་ཧེ་རུ་ཀ །ཞེས་བྱ་བ་ནི་བསྐྱེད་པའི་རིམ་པའི་རྒྱས་པར་བཤད་པ་སྟེ། རྣམ་པར་དག་པའི་དོན་ཕལ་ཆེར་རྣམ་པར་དག་པའི་ལེའུར་བཤད་དོ། །

[Block 3353]
པགས་པ་བྱང་ཆུབ་ཡན་ལག་བདུན་ནི་དྲན་པ་དང་ཏིང་ངེ་འཛིན་དང་ཤེས་རབ་དང་བརྩོན་འགྲུས་དང་དགའ་བ་དང་བཏང་སྙོམས་དང་ཤིན་ཏུ་སྦྱངས་པ་དང་སྟེ། པགས་པ་རིམ་པ་བདུན་གྱི་ཚུལ་དུ་གནས་པ་དང་སྦྱར་རོ། །

[Block 3354]
རུས་པ་བདེན་པ་བཞི་པོ་ཉིད་ནི་ཚོགས་ཆེན་པོ་བཞི་ལས་སྡུག་བསྔལ་གྱི་བདེན་པ་དང་ཀུན་འབྱུང་གི་བདེན་པ་དང་འགོག་པའི་བདེན་པ་དང་ལམ་གྱི་བདེན་པའོ། །

[Block 3355]
གཞན་དག་ནི་གོ་སླ་བས་མ་བཤད་དོ། །

[Block 3356]
བདག་མེད་མས་གསོལ་བ། སྔགས་བསྡུ་བ་ནི་ཇི་ལྟར་འགྱུར། །ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་རྗོད་བྱེད་ནུས་པ་དང་ལྡན་པར་སྟོན་ཏེ། ལས་དང་པོ་པས་དངོས་གྲུབ་སྒྲུབ་པ་ནི་སྔགས་དག་པ་ལས་འབྱུང་སྟེ་དེའི་དོན་དུ་སྔགས་བཏུ་བ་གསུངས་པ། བཅོམ་ལྡན་འདས་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི། ཨ་ཨཱ། ཨི་ཨཱི། ཨུ་ཨཱུ། རྀ་རཱྀ། ལྀ་ལཱྀ། ཨེ་ཨཻ། ཨོ་ཨཽ། ཨཾ་ཨཿ། དབྱངས་ཞེས་བྱ་བ་དང་པོའི་སྡེ་ཚན་ཞེས་བྱ་བ་ལ་སོགས་པ་སྐབས་ཀྱིས་གཞན་ཡང་སྦྱར་རོ། །

[Block 3357]
འདིར་ཡང་རྣལ་འབྱོར་མའི་ས་བོན་དུ་སྦྱར་བས་ནི་རིམ་པར་བསྟན་ཏེ་རྐྱེན་དུ་སྦྱར་བ་དང་། ཡན་ལག་ཏུ་ཤེས་པར་བྱ་སྟེ་གཞན་དུ་ཡང་སྦྱར་རོ། །

[Block 3358]
ཀ་ཁ་ག་གྷ་ང་། ཙ་ཚ་ཛ་ཛྷ་ཉ། ཊ་ཋ་ཌ་ཌྷ་ཎ། ཏ་ཐ་ད་ངྷ་ན། པ་ཕ་བ་བྷ་མ། ཡ་ར་ལ་ཝ། ཤ་ཥ་ས་ཧ་ཀྵཿ། ཨོཾ་ཨཱཿཧཱུཾ། ཀ་ཚན༌[^1346]

[Block 3359]
དང་པོ་ཞེས་བྱ་བ་དང་།

[Block 3360]
གཉིས་པ་ས་བོན་དུ་ཡང༌[^1347]ཤེས་པར་བྱ།

[Block 3361 [VERSE]]
ཙའི་སྡེ་ཚན་ནི་གཉིས་པ་སྟེ་ཡིག་འབྲུ་ལྔ་ལྔའོ། །
ཊ་ཋ་ནི་གསུམ་པ་སྟེ་ཀུན་ལ་ཤེས་སོ། །

[Block 3362]
ཏ་ཐ་ནི་བཞི་པ་དང་ལྔ་པ་གཉིས་ཆར་ཡང་སྡེ་ཚན་ནི་ལྔ་ལྔར་ཤེས། པ་ཕ་ནི་ལྔ་པར་ཤེས། ཡ་ར་ནི་མཐར་གནས་ཞེས་བྱ་བའི་འབྱུང་བ་བཞི་ས་བོན་ཞེས་བྱ། དྲུག་པའམ༌[^1348]བདུན་པའི་སྡེ༌[^1349]ཞེས་བྱ། [^1350]བརྒྱད་པའི་སྡེ་པ༌[^1351]ཨུཥྨ་ཞེས་བྱ། སྡེ་ཚན་འདི་རྣམས་མེད་དེ་ཡི་གེ་འདི་རྣམས་ལས་སྔགས་བཏུ་བར་བྱའོ། །

[Block 3363]
ཡི་གེ་འོག་མ་གསུམ་ནི་ཡི་གེའི་བདག་པོ་ཞེས་བྱ། ཡི་གེའི་དབང་ཕྱུག་ཅེས་བྱ། ཡི་གེ་ཐུ་བོ་ཞེས་བྱ། རིག་བྱེད་དང་པོ་ཞེས་བྱ། གཏི་མུག་རིགས་ཞེས་བྱ། རྣམ་པར་སྣང་མཛད་ཅེས་བྱ་སྟེ། གཉིས་པོ་ལ་ཡང་སྐབས་ཀྱིས་ཤེས་པར་བྱའོ། །

[Block 3364]
འདིས་ནི་རྒྱུད་ཐམས་ཅད་ཀྱི་སྔགས་བཏུ་བ་ལ་འཇུག་གོ། །

[Block 3365]
འབྲུ་སོ་སོར་སྦྱར་བ་ནི་གོ་སླའོ། །
--- END BLOCKS ---
