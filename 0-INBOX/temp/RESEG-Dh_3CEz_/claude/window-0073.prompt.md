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
[Block 2556 [VERSE]]
སྟོན་པས་སྨྲས་པ་ནི་ཤེས་རབ་དང་གཉིས་ཀ་ལའོ། །
སེམས་དཔའ་ཆེན་པོ་ནི་ཐབས་ལ་བོད་པའོ། །

[Block 2557]
ཕྱག་རྒྱ་བདེ་བ་དང་ལྡན་པ་ནི་དབང་གཉིས་པའི་ཡོན་ཏན་དང་ལྡན་པ་གཞན་ནོ། །

[Block 2558]
ཁྱེར་ཞེས་པ་ནི་ཡོལ་བའི་གནས་སུ་སྟེ། དེའི་ཚིགས་སུ་བཅད་པ་ཡང་འཆད་པར་འགྱུར་རོ། །

[Block 2559]
དེ་ནས་ཞི་བ་བསྟན་པའི་ཕྱིར་སློབ་མ་རྡོ་རྗེ་ཅན་མཐོང་དུ་འབྲེལ་ལོ། །

[Block 2560]
སློབ་མ་རྡོ་རྗེ་ཅན་ནི་གསུམ་པ་ཐོབ་པས་སོ། །

[Block 2561]
མཐོང་བས་ནི་སློབ་དཔོན་གྱི་ཤེས༌[^1098]པའོ། །

[Block 2562]
རྡོ་རྗེ་ཅན་གྱིས་སྨྲས་པ་ནི་བླ་མས་ཚིག་དབང་རིན་པོ་ཆེའོ། །

[Block 2563]
དེ་ཉིད་ནི་ཨེ་དྷ་སྟེ་བྷ་ག་གསུམ༌[^1099]པར་ཉམས་སུ་མྱོང་བ་དེ་ཉིད་དོ། །

[Block 2564]
ཡེ་ཤེས་ཆེན་པོ་ནི་ཟག་པ་མེད་པའོ། །

[Block 2565]
ཐམས་ཅད་ལུས་ལ་རྣམ་པར་གནས་ནི་གཉུག་མའི་དབང་པོར་ལུས་ཅན་ཀུན་ལའོ། །

[Block 2566 [VERSE]]
དེ་ཕྱིར་གཉིས་ནི་སྣང་བར་རོ། །
གཉིས་མེད་ཚུལ་ནི་དེ་ཁོ་ན་ཉིད་དོ། །

[Block 2567 [VERSE]]
དངོས་དང་དངོས་མེད་ནི་ཡོད་པ་དང་མེད་པའོ། །
ཡང་ན་ལུས་ནི་ལུས་དང་སེམས་སོ། །

[Block 2568]
བདག་ཉིད་གཙོ་བོ་ནི་ལྷན་ཅིག་སྐྱེས་པ་གསལ་བའོ། །

[Block 2569]
བརྟན་གཡོ་ཁྱབ་པ་ནི་བདག་མེད་མའི༌[^1100]ཤེས་པ་དེ་ཉིད་དེ་ཤེས་རབ་པོ། །སྒྱུ་མའི་གཟུགས་ཅན་ནི་སྣང་བ་བདེ་བའི་རོ་སྟེ་ཐབས་སོ། །

[Block 2570]
དེའི་ཕྱིར༌[^1101]དཀྱིལ་འཁོར་ནི་ཐབས་སོ། །

[Block 2571]
འཁོར་ལོ་ནི་ཤེས་རབ་མངོན་དུ་གྱུར་པའི་ངེས་པར་འགྲོ་བ༌[^1102]གཉིས་སུ་མེད་པར་གསལ་བའོ། །

[Block 2572]
དེ༌[^1103]དག་ནི་རྣལ་འབྱོར་མ་རྣམས་ལ་དབང་བསྟན་ནས་དབང་དེ་ཉིད་ལ་ཐེ་ཚོམ་བསལ་བ་ནི། མན་ངག་སྟེ་དེའི་ཕྱིར་དེ་ནས་ཞེས་པ་ནི་དབང་གི་རྗེས་ལའོ། །

[Block 2573]
རྡོ་རྗེ་སྙིང་པོས་རྣལ་འབྱོར་མ་རྣམས་ལ་བཟོད་པར་གསོལ་བ་ནི་ཁྱེད་ལ་གནང་བའི་འཕྲོ་ཡིན་ཡང་ངོ་། །བཅོམ་ལྡན་འདས་ལ་གསོལ་བ་ནི་ཐེ་ཚོམ་མ་སྐྱེས་ནས་སོ། །

[Block 2574]
དཀྱིལ་འཁོར་འཁོར་ལོ་ཅི་ཞེས་པ་ནི་སྡོམ་པ་སྟེ་གནས་པའོ། །

[Block 2575]
དཀྱིལ་འཁོར་ཐོག་མར་བཤད་པ་ནི། སངས་རྒྱས་ཀུན་བདག་ནི་རྡོ་རྗེ་འཛིན་པའམ།

[Block 2576 [VERSE]]
རྣམ་པར་སྣང་མཛད་ལ་སོགས་པའི་བདག་ཉིད་དོ། །
གྲོང་ཁྱེར་གཅིག་པ་སྟེ་ཁང་བཟངས་སོ། །

[Block 2577 [VERSE]]
བཅོམ་ལྡན་འདས་ནི་བདེ་བའོ། །
བདག་ནི་རྡོ་རྗེ་སེམས་དཔའོ། །

[Block 2578]
འཁྲུལ་འགྱུར་ནི་བཞི་པའི་དོན་དབྱེར་མེད་པའི་ལྷན་སྐྱེས་ལ་དཀྱིལ་འཁོར་དུ་གསུངས་པ་གྲོང་ཁྱེར་ཁང་བཟངས་ཡིན་པས།

[Block 2579 [VERSE]]
དེའི་ཕྱིར་འཁྲུལ་ཞིང་ཐེ་ཚོམ་དུ་གྱུར་པའོ། །
ཇི་ལྟར་རིགས་པ་ནི་རིགས་པ་གང་གིས་སོ། །
བཤད་དུ་གསོལ་ནི་ཐེ་ཚོམ་སོལ་ཅིག་པའོ། །

[Block 2580]
བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ༌[^1104]ནི་ཐབས་བདེ་བ་ཆེན་པོའི་རིགས་པས་དཀྱིལ་འཁོར་དུ་བསྒྲུབ་པའོ། །

[Block 2581]
དཀྱིལ་འཁོར་ནི་མཎྜལ་སྟེ་དཀྱིལ་ལམ་དབུས་སོ། །དེ་ཅིའི་ཕྱིར་ཞེ་ན། ས་ར་ནི་སྙིང་པོའམ་བཅུད་དེ་དེའི་ཕྱིར་བརྗོད་དོ། །

[Block 2582]
དེ་ཉིད་གང་ཞེ་ན། བྱང་ཆུབ་སེམས་ནི་བདེ་ཆེན་པོ། །ཞེས་པ་སྟེ། ཐབས་དང་ཤེས་རབ་དབྱེར་མེད་པའི་ལྷན་ཅིག་སྐྱེས་པའི་རོའོ། །

[Block 2583]
ཨ་ངྷན་ནན་ཏ་ཀ་རི་ཏའི་སྒྲ་དང་པོར་མཐར་བྱེད་པའམ་ལེན་པར་བྱེད་པའོ། །

[Block 2584]
དེ་ཡང་དང་པོར་ནི་དཀྱིལ་འཁོར་སྙིང་པོའོ། །

[Block 2585]
མཐར་ནི་བསྐོར་བའོ། །

[Block 2586 [VERSE]]
ཡང་ན་བླང་བྱ་ནི་བདེ་ཆེན་ནོ། །
ལེན་པར་བྱེད་པ་ཞེས་པ༌[^1105]ནི་ཉམས་སུ་ལེན་པའོ། །

[Block 2587]
དེའི་ཕྱིར་འདུས་པ་ནི་མཎྜལ་ན་སྟེ་བསྐོར་བྱ་སྐོར་བྱེད་དམ་བླང་བྱ་བླང་བྱེད་སྡོམ་པའོ། །

[Block 2588]
དེའི་མཎྜལ་མ་ཊ་སྟེ་དཀྱིལ་འཁོར་ཉིད་དུ་བརྗོད་དོ། །

[Block 2589]
ད་ནི་འཁོར་ལོ་ཅི་ཞེས་པ་ནི་བསྟན་པ་བཤད་པའི་ཕྱིར་ཡང་སངས་རྒྱས་ཀུན་བདག་ནི་སྔ་མ་ལྟར་རོ། །

[Block 2590 [VERSE]]
གྲོང་ཁྱེར་ལ་ལྷག་མ་སྟེ་འཁོར་ལོའོ། །
བཅོམ་ལྡན་འདས་སྔ་མ་ལྟར་རོ། །

[Block 2591]
འཁྲུལ་འཁོར༌[^1106]ནི་དབང་བཞི་པའི་དོན་ལྷན་ཅིག་སྐྱེས་པ་ལ་གསུངས་པས་འཁོར་ལོ་ནི་ཙཀྲ་བྷ་ར་ད་སྟེ། གཅོད་པར་བྱེད་པའི་འཁོར་ལོ་ཡིན་པས་འཁྲུལ་ཞིང་ཐེ་ཚོམ་དུ་གྱུར་པའོ། །

[Block 2592]
ཇི་ལྟར་རིགས་པ་ནི་ཤེས་རབ་མི་རྟོག་པའི་རིགས་པའོ། །

[Block 2593]
བཤད་དུ་གསོལ་ནི་སྔ་མ་ལྟར། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་ནི་ཤེས་རབ་ཀྱི༌[^1107]རིག་པས་འཁོར་ལོར་བསྒྲུབ་པའོ། །

[Block 2594]
[^1108]འཁོར་ལོ་ཞེས་གནས་སུ་འབྲེལ་ཏེ། དེ་ཡང་ཙ་ཀྲ་ནི་མ༌[^1109]ཧཾ་སྟེ་ཞེས་གནས་པ་དང་ཞེས་བརྗོད་པ་སྟེ་ཅིའི་ཕྱིར་ཞེ་ན། ནམ་མཁའི་ཁམས་ནི་སྟོང་པར་རོ། །

[Block 2595]
ཡུལ་ལ་སོགས་པ་ནི་དབང་པོ་ལ་སོགས་པའི་ཆོས་ཇི་སྙེད་པའོ། །
--- END BLOCKS ---
