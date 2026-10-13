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
[Block 2941]
མགྲིན་པ་དང་ལོངས་སྐུ་ཡང་རོ་དྲུག་ནི་མངར་བ་དང་། སྐྱུར་བ་དང་། ཁ་བ་དང་། ཚ་བ་དང་། བསྐ་བ་དང་། ལན་ཚྭ་དེ་རྣམས་མགྲིན་པར་མྱོང་གི་འདས་ནས་མ་ཡིན་པ་ལྟར་ལོངས་སྐུའི་ཞིང་ཁམས་དང་འཁོར་དང་ཆོས་ལ་ལོངས་སྤྱོད་པའོ། །

[Block 2942]
སྤྱི་བོ་བདེ་ཆེན་གྱི་སྐུ་ཡང་སྤྱི་བོར་བདེ་བ་ཁྱད་པར་དུ་འཕགས་པ་བདེ་བ་ཆེན་པོའི་སྐུ་ཡང་སྐུ་གསུམ་ཡོངས་སུ་ཤེས་པས་ཁྱད་པར་དུ་འཕགས་པའོ། །

[Block 2943]
ཨེ་ཝཾ་རྒྱུ་མཐུན་ནི་ཨེ་སྟེ་སྤྲུལ་པ་ལ་སོགས་པ་ཨེ་ཝཾ་མ་ཡཱ་སྦྱར་རོ། །

[Block 2944]
ཕ་རོལ་ཕྱིན་པ་ལ་འབྲས་བུ་བཞི་སྟེ། འཁོར་ལོ་བཞི་དང་ཆོས་མཐུན་བསྟན་ཏེ། དང་པོར་རྒྱུ་མཐུན་པའི་འབྲས་བུ་ནི། རྒྱུ་མཐུན་དང་འདྲ་བ་ཉིད་ཅེས་པ་བཟོ་ལ་སོགས་པ་ལས་མ་འོངས་པ་ན་ཡང་དེ་དང་མཐུན་པར་འབྱུང་སྟེ། ལས་ཀྱི་རླུང་གིས་མེ་ལ་སོགས་པ་བསྐུལ་བས་ལྟེ་བའི་གནས་སུ་རྟོག་པ་དང་འདྲེན་པར་ཉམས་སུ་མྱོང་བས་སོ། །

[Block 2945]
རྣམ་པར་སྨིན་པའི་འབྲས་བུས་ནི་དེ་ལས་དགེ་མི་དགེ་ཅུང་ཟད་ལས་མ་འོངས་པའི་དུས་སུ་ལྷ་མིན་ཁྱད་པར་ཅན་དང་ངན་སོང་དུ་སྨིན་པས་ལས་ཆུང་ལ་འབྲས་བུ་ཆེ་བ་ཞེས་བྱ་སྟེ། དེ་ལྟར་ལྟེ་བ་ནས་སྙིང་གར་ཁྱད་པར་དུ་མྱོང་བའོ། །

[Block 2946]
སྐྱེས་བུ་བྱེད་པའི་འབྲས་བུ་ནི་རྐྱེན་གྱི་སྟོབས་ཀྱིས་གང་ནས་གང་དུ་འཕེལ་བ་སྟེ། བསླབ་པ་ཁྱད་ཞུགས་པ་ལ་བྱ་སྟེ། དེ་ཡང་མགྲིན་པར་ཡང་སྔ་མ་ལས་གོང་ནས་གོང་དུ་འཕེལ་ལོ། །

[Block 2947]
དྲི་མ་མེད་པའི་འབྲས་བུ་ནི་མི་མཐུན་པ་དང་འབྲེལ་པ་སྟེ། དཔེར་ན་སྨིན་པའི་འབྲས་བུས་ལོངས་སྤྱོད་ཆེ་བ་དེས་འབུལ་བ་དང་བྲལ་བ་ལྟར། བདེ་ཆེན་དུ་ཡང་མི་མཐུན་པ་དང་བྲལ་ནས་ཡེ་ཤེས་གནས་པའོ། །

[Block 2948]
ཉན་ཐོས་ལ་ཤེས་བྱ་སྡེ་པ་བཞི་དང་། ཤེས་བྱེད་སྡེ་པ་བཞི་སྟེ། དེ་ཡང་འཁོར་བཞིར་སྦྱར་བ་གནས་བརྟན་པ་ཡང་དང་པོ་གནས་ཀྱི་གཞི་མ་ལ་བྱ་ལ། ལྟེ་བ་ཡང་སེམས་ཅན་ཐམས་ཅད་ཀྱི་སྐྱེ་བ་ལྟེ་བ་ནས་ཆགས་པའོ། །

[Block 2949]
དགེ་འདུན་གཞི་ཐམས་ཅད་ཡོད་པར་སྨྲ་བ་ཁྲིམས་ལས་རེ་རེ་བཅས་པའི་གཞི་འདོད་པ་སྟེ། དཔེར་ན་ནག་པོ་འཆར་ཀའི་གཏམ་རྒྱུད་བཞིན་དུ་ཀུན་ལ་ཡོད་པའོ། །

[Block 2950 [VERSE]]
སྙིང་ག་ཆོས་ཐམས་ཅད་འབྱུང་བའི་གནས་གཞིའོ། །
དགེ་འདུན་ཀུན་བཀུར་ནི་སྡེ་པ་ཀུན་གྱིས་བཀུར་བའོ། །

[Block 2951]
དེ་བཞིན་དུ་བྱ་བ་ཐམས་ཅད་བྱས་ནས་མགྲིན་པར་བཀུར་བའོ། །

[Block 2952]
དགེ་འདུན་ཕལ་ཆེན་ནི་སྡེ་པ་གཞན་ལས་ཕལ་ཆེ་བས་ནའོ། །

[Block 2953]
བདེ་ཆེན་ཡང་འོག་མ་བས་བདེ་བ་ཟླ་བ་ཞུ་བ་ཕལ་ཆེ་བའོ། །ཤེས་བྱ་ཡང་སྡུག་བསྔལ་བདེན་པ་ནི་འཁོར་བའི་ཕུང་པོ་ལྔ་ཡིན་ལ་དེ་ལ་སྐྱེ་བ་དང་། རྒ་བ་དང་། ན་བ་དང་། འཆི་བ་དང་། སྡུག་བསྔལ་དང་མྱ་ངན་དང་། སྨྲེ་སྔགས་འདོན་པ་དང་། དེ་ལ་སོགས་པའི་རྩ་བའི་ཕུང་པོ་ཡིན་ལ། ལྟེ་བ་ཡང་ཐམས་ཅད་ཀྱི་རྩ་བ་ཡིན་པས་ཆོས་མཐུན་པའོ། །

[Block 2954]
ཀུན་འབྱུང་གི་བདེན་པ་ནི་ལས་དང་ཉོན་མོངས་པ་སྟེ་དེ་ལ་སྡུག་བསྔལ་འབྱུང་བའོ། །

[Block 2955]
སྙིང་ག་ལ་ཆོས་དགེ་མི་དགེ་ཀུན་འབྱུང་བས་ཆོས་མཐུན་པས་སོ། །

[Block 2956]
འགོག་པའི་བདེན་པ་སྡུག་བསྔལ་རྒྱུ་དང་བཅས་པ་བཞི་པའོ། །

[Block 2957]
སྤྱི་བོ་ཡང་མི་མཐུན་པ་ཐམས་ཅད་ཞི་ནས་གཉེན་པོར་གནས་པ་ཆོས་མཐུན་པའོ། །

[Block 2958]
ལམ་གྱི་བདེན་པ་ནི་འཕགས་པའི་ལམ་ཡན་ལག་བརྒྱད་དེ་དེས་མི་མཐུན་པ་རིང་དུ་སྤོང་བས་ལམ་མོ། །

[Block 2959]
མགྲིན་པར་ཡང་མི་མཐུན་པའི་རིང་དུ་སྤོང་བས་ལམ་མོ། །

[Block 2960]
ཡང་འཇིག་རྟེན་པའི་ཆོས་དགོད་པ་དང་། བལྟ་བ་དང་། འཁྱུད་པ་དང་། གཉིས་སྦྱོར་བ་ཡེ་ཤེས་དང་། སྤོང་བའི་ཁྱད་པར་དུ་གྱུར་པ་སྦྱར་རོ། །

[Block 2961]
དེ་བཞིན་དུ་དགའ་བ་དང་། སྐད་ཅིག་མ་རྒྱུད་བཞི་དང་། རིགས་བཞི་དང་བཞི་བཞིར་བསྡུས་ལ་སྦྱར་རོ། །

[Block 2962]
དེ་ཡང་། དགྱེས་པའི་རྡོ་རྗེ་ཡིས་ནི་བདེ་མཆོག་འཁོར་ལོ་དང་། །

[Block 2963 [VERSE]]
དེ་བཞིན་དུ་ནི་རྡོ་རྗེ་གདན་བཞི་དང་། །
བཞི་བཞི་པ་ནི་ཐམས་ཅད་ཤེས་པར་འགྱུར། །

[Block 2964]
ཞེས་གསུངས་པས་ཀུན་དུ་སྦྱར་བས་རྒྱུ་མཚན་ཅི་རིགས་པར་བྱའོ།[^1217] །ཕྱི་རོལ་གྱི་ཞེན་པ་སྤང་བའི་ཕྱིར་རོ། །

[Block 2965]
དེ་དག་གིས་ནི་སེམས་དང་ལུས་རྫོགས་པའི་སངས་རྒྱས་སུ་བསྟན་ནས། ད་ནི་ས་བཅུ་པའི་སངས་རྒྱས་སུ་སྐྱེ་བ་དག་པ་བསྟན་པའི་ཕྱིར་གོ་རིམས་ཅུང་ཟད་བསྣོར་ཏེ། འདི་དག་རྐྱེན་གྱིས་སེམས་ཅན་རྣམས་སུ་འབྲེལ་ཏེ་རྐྱེན་གྱིས་ནི་ས་མ་ཡ་ཀྲི་པ་སྟེ། སེམས་ཅན་རྣམས་ནི་དེ་དག་ཏུ་གྱུར་པའོ། །

[Block 2966]
སངས་རྒྱས་ཉིད་དུ་ཐེ་ཚོམ་མེད༌[^1218]ནི་དོན་ལ་སྐྱེ་བ་དག་པས་སོ། །

[Block 2967]
ཅིས་ཤེ་ན་ཟླ་བ་བཅུར་ནས་རྣམས་ཕྱིར་ནི་དག་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2968]
སེམས་ཅན་ས་བཅུའི་དབང་ཕྱུག་ནི་དེ་ལས་མཛད་པ་འབྱུང་བའོ། །

[Block 2969]
གང་དག་ཅེ་ན། དེ་ལ་ལྟེ་བ་གནས་སུ་བརྗོད་དུ་འབྲེལ་ཏེ།

[Block 2970 [VERSE]]
གནས་ནི་རྒྱལ་བའི་གནས་དགེ་འདུན་གྱི༌[^1219]གནས་ལྟ་བུའོ། །
སྐྱེ་གནས་ནི་མངལ་ལམ་ཆོས་འབྱུང་ངོ་། །

[Block 2971]
འདོད་ཆགས་བྲལ་བ་འབྱུང་ནི་བཙུན་མོ་ནང་ནས་འབྱུང་བའི་བར་དུ་བྱུང༌[^1220]བའོ། །

[Block 2972]
མངལ་གྱི་ཁྲུ་མ་ཆོས་གོས་ཀྱི་གཙོ་བོ་ཙི་བ་རའོ།[^1221] །དེ་བཞིན་མ་ནི་མཁན་པོ་ཉིད་ནི་མཁན་པོ་ལྟ་བུ་སྟེ་དེ་ལ་ནོད་པའོ། །

[Block 2973]
མགོ་བོ་ཐལ་མོ་སྦྱར་བ་ནི་སྐྱེ་བའི་དུས་ནའོ། །

[Block 2974]
ཕྱག་ནི་དེར་ཞེས་བྱའོ། །

[Block 2975]
འགྲོ་བའི་བྱ་བ་ནི་སྐྱེ་གནས་ཐ་མལ་གྱི་བྱ་བའོ། །

[Block 2976]
ཁྲིམས་ནི་སིན་ཁྱ་སྟེ་བསླབ་པའི་རིམ་པའོ། །

[Block 2977]
གནས་ནི་བནྡྷན་ཛ་སྟེ། སྟོན་པའི་ཚིག་གམ་ནོད་པའི་གནས་སོ། །

[Block 2978 [VERSE]]
དེ་བཞིན་ཨ་ཧཾ་ཐོག་མ་ཉིད་ནས་སྐད་འདོན་པའོ། །
སྔགས་བཟླས་ནི་ཨཱ་ལི་ཀཱ་ལི་བསྡུས་པའོ། །

[Block 2979]
གང་དུ་ཞེ་ན།

[Block 2980 [VERSE]]
སྐྱེ་གནས་འཁོར་ལོ་ནི་ལྟེ་བར་རོ། །
རྣམ་པ༌[^1222]ཨ་ནི་ཨཾ་ཡིག་གོ། །
བདེ་ཆེན་གྱི་ཡང་ནི་སྤྱི་བོར་རོ། །
རྣམ་པ་ཧཾ་ནི་ཧཾ་ཡིག་གོ། །
--- END BLOCKS ---
