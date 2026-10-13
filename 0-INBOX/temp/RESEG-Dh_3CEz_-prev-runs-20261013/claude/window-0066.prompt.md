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
[Block 2311]
དེ་བཞིན་དུ་ཡང་ཐབས་སྐྱེ་བ་ལ་ཡང་ལྷག་མ་ཁོང་ནས་ཕྱུང་སྟེ་ཤེས་པར་བྱ་སྟེ། ལ་ལ་སྐྱེ་བ་སྐྱེ་བར་འགྱུར། །ཞེས་འབྱུང་སྟེ།

[Block 2312 [VERSE]]
[^999]ཉོན་མོངས་པའི་སྐྱེ་བ་ཡིན་པས་སོ། །
སྐྱེ་བའི་དངོས་མེད་ཟད་པར་འགྱུར། །

[Block 2313]
ཞེས་པ་ཐབས་དང་ཤེས་རབ་ཀྱིས་སྐྱེ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2314]
དེ་དག་གིས་ནི་བསྐྱེད་པའི་རིམ་པ་ཐབས་ཀྱི་ཆོ་ག་དག་པར་བྱས་ནས། བསྐྱེད་པ་ལྷའི་མཚན་མ་དག་པའི་ཕྱིར་བསྐྱེད་པའི་རིམ་པ་ནི་རྣལ་འབྱོར་འདིས༌[^1000]ལས་དང་པོ་ནས་བཟུང༌[^1001]བའོ། །

[Block 2315 [VERSE]]
བརྟུལ་ཞུགས་ཅན་ནི་བསྐྱེད་རིམ་མཐར་ཕྱིན༌[^1002]པའི་བར་གྱིས་སོ། །
སྤྲོས་པ་ནི་ཁ་དོག་དང་མཚན་མ་ལ་སོགས་པའོ། །

[Block 2316]
བསྒོམ་པ་ནི་གསལ་བར་རོ། །

[Block 2317]
རྨི་ལམ་ལྟར་གསལ་བ་སེམས་ཀྱི་ཆོས་ཡིན་པས་སོ། །

[Block 2318]
དེའི་ཕྱིར། སྤྲོས་པ༌[^1003]ཉིད་ནི་སྤྲོས་པ་མེད། །ཅེས་བྱ་སྟེ་བསྐྱེད་པའི་ངོ་བོ་དག་པར་བྱེད་པའོ། །

[Block 2319]
ད་ནི་བསྐྱེད་པའི་རིམ་པའི་ཡོན་ཏན་ནམ་སྤྱོད་ཡུལ་དག་པར་བསྟན་པའི་ཕྱིར། །ཇི་ལྟར་སྒྱུ་མ་ཞེས་པ་ནི་རིག་མ་ལ་བརྟེན་པ་ལ་སོགས་པས་བདེ་བ༌[^1004]སྒྱུ་མ་ལྟ་བུ་མྱོང་བའོ། །

[Block 2320 [VERSE]]
དེ་བཞིན་རྨི་ལམ་གསལ་བ་སེམས་ཀྱི་ཆོས་སུའོ། །
ད་ནི་སྐྱེ་བའི་རྟེན་དག་པར་བསྟན་པའི་ཕྱིར། །
ཇི་ལྟར་ནི་གཞལ་ཡས་ཁང་ངོ་། །

[Block 2321]
བར་སྲིད་དམ་དྲི་ཟའི་གྲོང་ཁྱེར་ནི་ནམ་མཁའ་ལ་འཚོ་བའི་ཁང་བཟངས་སོ། །

[Block 2322]
རྟག་ཏུ་གོམས་པའི་སྦྱོར་བ་ནི་དག་པ་དང་ལྡན་པས་སྔ་མ་ལྟར་རོ། །

[Block 2323]
དཀྱིལ་འཁོར་ཉིད་ཀྱང་དེ་བཞིན་སྣང་ནི་བསྐྱེད་རིམ་དེ་ལྟར་ཤེས་ནས་རྫོགས་རིམ་ལ་སྦྱོར་ནུས་པས་སོ། །

[Block 2324]
ད་ནི་རྫོགས་པའི༌[^1005]རིམ་པ་བསྟན་པའི་ཕྱིར། ཕྱག་རྒྱ་ཆེན་པོའི་དབང་བསྐུར་ནི་ཀུན་རྫོབ་ཕྱག་རྒྱ་ཆེན་པོའི་གཟུགས་ཕལ་པའི་པདྨ་ཅན་ལ་བརྗོད་པ་སྟེ་ལས་ཀྱི་ཕྱག་རྒྱའོ། །

[Block 2325]
དབང་བསྐུར་ནི་གསུམ་པ་དང་འདྲ་བ་ལས་རྟེན་ཁྱད་པར་ཅན་དུ་ཉམས་སུ་མྱོང་བའོ། །

[Block 2326]
ཇི་ལྟར་གཟུང་བའི་བདེ་ཆེན་པོ་ནི་ཟླ་བ་གཟུང་བའི་མན་ངག་ལས་སྐྱེས༌[^1006]པའོ། །

[Block 2327]
དེའི་བྱིན་རླབས་སམ་མཐུ་ནི་གསལ་བའི་བདེ་བའོ། །

[Block 2328]
བྱིན་རླབས་སྐྱེས་པ་ལས་རྟེན་དང༌[^1007]བརྟེན་པར་འགྱུར་བས་དཀྱིལ་འཁོར་ཡིན་པ་ཁོ་ནའོ། །

[Block 2329]
གཞན་ལས་དཀྱིལ་འཁོར་འབྱུང་བ་མེད་ནི་ལྷན་ཅིག་སྐྱེས་ལས་གཞན་པ་ལས་སོ། །

[Block 2330]
དེ་ནི་གཞན་ལུས་ཤེས་རབ་ལ་བརྟེན་པའོ། །

[Block 2331]
ཡང༌[^1008]ཕྱག་རྒྱ་ཆེན་པོ་ནི་ལྟེ་བ་ལ་གནས་པའི་ཐིག་ལེའམ་ཡི་གེའོ། །

[Block 2332]
དབང་བསྐུར་བ་ནི་སྤྱི་བོའི་ཧཾ་ལས་ཞུ་བ་སྟེ་གུར་ཀུམ་གྱི་ཆར་ལ་སོགས་པ་དང་ལྡན་པའོ། །ཤེས་པའི་བདེ་ཆེན་ནི་གསལ་བའི་བདེ་བའོ། །

[Block 2333 [VERSE]]
གཞན་དག་སྔ་མ་ལྟར་རོ། །
དེ་ནི་རང་ལུས་ཐབས་ལ་བརྟེན་པའོ། །

[Block 2334]
གསུམ་པ་ཆགས་བྲལ་གྱི་དབང་བསྐུར་བ་སྟེ༌[^1009]ཉམས་སུ་མྱོང་བ་ནི་སྔ་མ་དང་འདྲའོ། །

[Block 2335]
ཡང་ཕྱག་རྒྱ་ཆེན་པོ་ནི་ཤེས་རབ་ལྷ་མོ་བླ་ན་མེད་པའོ། །

[Block 2336]
དབང་བསྐུར་བ་ནི་དེ་བསྟེན་པའི་ཐབས་ཆགས་པ་དང་ཆགས་བྲལ་ལྟ་བུའི་ཚུལ་ལོ། །ཤེས་པའི་བདེ་བ་ཆེ་ནི་གཉིས་སུ་མེད་པའི་ཤེས་པ་འབའ་ཞིག་གོ། །

[Block 2337]
བྱིན་གྱིས་བརླབས་ནི་སྣང་བ་བྱིན་གྱིས་རློབ་པའོ། །

[Block 2338]
གཞན་ལས་ནི་གཉུག་མའི་དབང་པོ་མ་སྨིན་པ་ལས་སོ། །

[Block 2339]
དཀྱིལ་འཁོར་འབྱུང་བ་མེད་ན་སྒོ་གསུམ་ནུས་པ་མེད་པས་རྐང་པ་ཉེད་པ་དང་དཀྱིལ་འཁོར་མེད་པ་དང་། དེས་མཚོན་ནས་ཕྱག་རྒྱ་དང་སྔགས་ཀྱང་མེད་པ་སྟེ་ཡང་དག་པའི་བརྟུལ་ཞུགས་དང་མི་ལྡན་པ་ཞེས་བྱ་བ་ནི་ཐ་ཚིག་གོ། །

[Block 2340]
ད་ནི་དེའི་རྒྱུ་མཚན་རང་སྣང་བའི་མན་ངག་བསྟན་པ་ནི་གོ་སླའོ། །

[Block 2341]
བདེ་བ་གནག་ཅིང་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་རྟེན་གྱི་དཀྱིལ་འཁོར་མཚོན་ཏེ། །བདེ་བ་ཆེན་པོ་ཁ་དོག་རྣམ་པ་ལྔས་མཚོན་པའོ། །

[Block 2342]
ཡང་བསྟེན་པའི་དཀྱིལ་འཁོར་མཚོན་ཏེ། ནག་པོ་ནི་རྡོ་རྗེ་འཆང་། སེར་པོ་ནི་རིན་ཆེན་འབྱུང་ལྡན། དམར་པོ་སྣང་བ་མཐའ་ཡས། དཀར་པོ་རྣམ་པར་སྣང་མཛད།

[Block 2343 [VERSE]]
ལྗང་གུ་དོན་ཡོད་གྲུབ་པ། །
སྔོན་པོ་མི་བསྐྱོད་པ་མཚོན་པའོ། །

[Block 2344]
དེ་བཞིན་དུ་རྒྱུ་བ་དང་མི་རྒྱུ་བ་ལ་སོགས་པ་ཐམས་ཅད་ཕྱག་རྒྱ་ཆེན་པོའི་བདེ་བས་མཚོན་པའོ། །

[Block 2345]
དེ་ཡང་། །རྡོ་རྗེ་སེམས་དཔའ་བདེ། །ཞེས་པ་ལ་གོ་བཟློག་སྟེ། སྣང་བ་བདེ་བ་ཆེན་པོ་ཉིད་དུ་རྡོ་རྗེ་སེམས་དཔའ༌[^1010]བརྗོད་དོ། །

[Block 2346]
དེ་ནས་བདེ་བ་ཆེན་པོ་ལ་ཐེ་ཚོམ་དྲི་བའི་ཕྱིར། རྡོ་རྗེ་སྙིང་པོས་གསོལ་པ། རྫོགས་པའི་རིམ་པའི་རྣལ་འབྱོར་ནི་དབང་ལས་ཐོབ་ཅིང་དཀྱིལ་འཁོར་དུ་གནས་པའི་བདེ་ཆེན་ནོ། །

[Block 2347]
སཏྭ་སུ་ཁ་སྟེ་དམ་པའམ་དེའི་བདེ་བ་ནི་རྫོགས་རིམ་གྱི་བདེ་ཆེན་ནོ། །

[Block 2348]
དེ་ནས་བསྐྱེད་པ་ཡིས༌[^1011]ནི་ཅི་ཞིག་འཚལ་དུ་འབྲེལ་ཅིའི་ཕྱིར་ཞེ་ན།

[Block 2349 [VERSE]]
རྫོགས་པ་བསྒོམ་པ་མེད་པའི་ཕྱིར་རོ། །
བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ་ནི་ལན་དུའོ། །

[Block 2350]
ཨེ་མ་ནི་ཨ་ཧོ་སྟེ་དེ་ལྟར་ཡིན་ནའང་ངོ་མཚར་བའོ། །
--- END BLOCKS ---
