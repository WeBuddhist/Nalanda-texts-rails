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
[Block 2871]
དེ་ནི་བདག་མེད་མ་སྟེ་ཤེས་རབ་ཀྱིའོ། །

[Block 2872]
བདེ་བ་ནི་ཐབས་སོ། །

[Block 2873]
ཕྱག་རྒྱ་དབྱེར་མེད་དོ། །

[Block 2874]
དེ་ཇི་ལྟར་སྐྱེ་ཞེ་ན། ལྟེ་བའི་དཀྱིལ་འཁོར་ཉིད་དུ་གནས་ནི་བཞི་སྟེ་པདྨའི་ཟེ་འབྲུ་ལས་དང་པོར་དབྱངས་ཡིག་ནི་ཨེ་སྟེ་རྟེན་ནོ། །

[Block 2875]
བློ་ཞེས་པ་ནི་ཕྱག་རྒྱ་ཆེན་པོའི་ཆོས་ཏེ་བརྟེན་པའོ། །

[Block 2876]
སངས་རྒྱས་རྣམས་ཀྱིས་བཏགས་པ་ནི་དགྱེས་པའི་རྡོ་རྗེའམ་གཞན་གྱིས་ཏེ་ཡུལ་དུའོ། །

[Block 2877]
རྫོགས་པའི་རིམ་པའི་རྣལ་འབྱོར་ནི་རྣལ་འབྱོར་པའམ། བདེ་བ་ཆེན་པོ་ནས་འབབ་པའོ། །

[Block 2878]
དེ་ཉིད་བཅོམ་ལྡན་ཤེས་རབ་ནི་ལྟེ་བ་ན་གནས་པ་སྟེ་ཡུམ་དུ་བྱས་པའོ། །

[Block 2879]
དེ་ནི་རིང་མིན་ལ་སོགས་པ་ནི་དེ་དག་ལས་འདས་པའོ། །

[Block 2880]
ལྷན་ཅིག་སྐྱེས་དགའ་བྱེད་པ་ནི་བདེ་བ་ཆེན་པོ་ལ་སོགས་པས་སོ། །

[Block 2881]
དེ་ལས་སྐྱེས་པ་ནི་མཚོན་བྱ་ལས་བྱུང་བའི་མཚོན་བྱེད་མྱོང་བས་སོ། །

[Block 2882]
རྣལ་འབྱོར་པས་དེའི་བདེ་བའི་བཟའ་བ་ནི་གཞན་ལ་མི་ལྟོས་པར་རོ། །

[Block 2883]
ཡང་ན་ག་བུར་ཉིད་ནི་བདག་མེད་མ་ལ་སོགས་པ་ཕྱག་རྒྱ་ཆེན་པོའི་སའི་དཀྱིལ་དང་། ནམ་མཁའི་དཀྱིལ་དུ་གནས་པའི་གཉུག་མའི་དབང་པོ་སྟེ། ག་བུར་ཉིད་ནི་བདག་མེད་མ་ནི་སྐྱེ་བ་མེད་དོ། །

[Block 2884]
བདེ་བ་བདག་མེད་ཚུལ་ནི་བདེ་བའི་གཟུང༌[^1201]ལ་བདག་མེད་པར་རྟོགས་པའོ། །

[Block 2885]
དེའི༌[^1202]ཕྱག་རྒྱ་ཆེ་ནི་རྟེན་ཁྱད་པར་ཅན་དུ་མྱོང་བའོ། །

[Block 2886]
ལྟེ་བའི་དཀྱིལ་ནི་བརྟེན་པའི་དཀྱིལ་དང་ནམ་མཁའི་དཀྱིལ་དུ་གནས་པའོ། །

[Block 2887]
དང་པོ་དབྱངས་ཡིག་ནི་མ་ཏྲ་སྟེ། ཕྱི་མོའམ་ཐོག་མའོ། །

[Block 2888]
བློ་ཞེས་སངས་རྒྱས་རྣམས་ཀྱིས་བཏགས་ནི་བུདྡྷ་སྟེ་རྟོག་པ་ལས་འབྱུང་བའོ། །

[Block 2889]
དེ་སྐད་དུ།

[Block 2890 [VERSE]]
མ་ཞིག་ན་བར་གྱུར་ལ་བུ་ནི་མང་ཡོད་པ། །
དེ་ཀུན་ཡིད་མི་བདེ་ཞིང་དེ་ལ་རིམ་གྲོ་བྱེད། །

[Block 2891]
དེ་བཞིན་ཕྱོགས་བཅུ་འཇིག་རྟེན་ཁམས་ཀྱི་སངས་རྒྱས་ཀྱང་། །ཡུམ་གྱུར་ཤེས་རབ་དམ་པ་འདི་ལ་དགོངས་པ་མཛད། །ཅེས་གསུངས་སོ། །

[Block 2892]
དེ་ལས་སྐྱེས་པའི་རྣལ་འབྱོར་ནི་དེ་ཉིད་བསྒོམ༌[^1203]པའོ། །

[Block 2893]
དེ་ཉིད་བཅོམ་ལྡན་འདས་ཤེས་རབ་མ་ནི་ཡོན་ཏན་ཐམས་ཅད་སྐྱེད་པར་བྱེད་པའོ། །

[Block 2894]
དེའི་མཚན་ཉིད་དབྱིབས་དང་ཁ་དོག་ལ་སོགས་པ་ཡིན་ཏེ་རིང་མིན་ཐུང་མིན༌[^1204]ལ་སོགས་པའོ། །

[Block 2895]
དེ་དང་ལྷན་ཅིག་ཅེས་བྱ་བ་ནི་དེར་སྐྱེས་པའི་ཡེ་ཤེས་སོ། །

[Block 2896 [VERSE]]
བདེ་བ་བཞི་པ་ནི་ཟག་མེད་མཐར་ཐུག་པའོ། །
གཟུགས་སོགས་གཉིས༌[^1205]ཀྱིས་སྤྱོད་པ༌[^1206]ཉིད་དུ་སྟེ་དེར་སྦྱོར་བའོ། །

[Block 2897]
དེའི་ཆོས་ཀྱི་འཁོར་ལོ་ལ་སོགས་པ་སྔ་མ་བཞིན་ནོ། །

[Block 2898]
མེ་ལོང་ཡེ་ཤེས་ནི་ཆོས་རྣམས་དེ་ལ་སྣང་བའོ། །

[Block 2899]
མཉམ་ཉིད་ནི་རོ་གཅིག་པར་རྟོགས་པའོ། །

[Block 2900]
སོ་སོར་རྟོག་པ་ནི་སེམས་ཅན་གྱི་དོན་གྱི་སྤྲུལ་པ་སྟོན་པའོ། །

[Block 2901]
བྱ་བ་ནན་ཏན་ནི་བྱ་བ་ཐམས་ཅད་བསྒྲུབ་པའོ། །

[Block 2902 [VERSE]]
ཆོས་དབྱིངས་ནི་དེས་ཀུན་ལ་ཁྱབ་པའོ། །
ཇི་ལྟར་རིགས་པ་བཞིན་ནོ། །

[Block 2903]
དེ་ལྟར་མཚན་ཉིད་བསྟན་ནས་ཆོས་བསྟན་པའི་ཕྱིར། །དེ་དང་ལྷན་ཅིག་ཕྱག་རྒྱ་ཆེ་ནི་རྟེན་དག་པས་བདག་པོ་བྱས་ནས། མ་དག་པ་དང་རྣམ་པར་བྱང་བའི་ཆོས་དགྱེས་པའི་རྡོ་རྗེ་དང་། བདག་མེད་མ་དབྱེར་མེད་པའི་རང་བཞིན་ཏེ་གོ་སླའོ། །

[Block 2904]
ད་ནི་ལུས་སྡོམ་པ་བསྟན་པའི་ཕྱིར། རྡོ་རྗེ་སྙིང་པོས་གསོལ་ཞེས་པའོ། །

[Block 2905 [VERSE]]
འཁོར་ལོ་བསྒོམ་པ་ནི་སེམས་བསྐྱེད་པའི་ཐབས་ཏེ།
དཀྱིལ་འཁོར་དང་འཁོར་ལོ་དང་རང་བྱིན་གྱིས་བརླབ༌[^1207]པའོ། །

[Block 2906]
ལམ་དང་ཞེས་བྱ་བ་ནི་བསྐྱེད་པ་དང་རྫོགས་པའི་རིམ་པའོ། །

[Block 2907]
ལྷ་རྣམས་ཇི་ལྟར་ནི་ག་བུར་ཀུནྡ་བདེ་བ་རྣམས༌[^1208]ནམ་མཁའ་ལྟ་བུའོ། །

[Block 2908]
འབྱུང་བ་ཉིད་ནི་བསྐྱེད་པ་སྟེ་ཀུན་རྫོབ་དང་དོན་དམ་གྱི་སེམས་གཉིས་སོ། །

[Block 2909]
ཐམས་ཅད་བཅོམ་ལྡན་འདས་གསུངས་ནས། ཕྱག་རྒྱ་ཆེན་པོ་རྒྱས་བཏབ་པ་ཡང་གསུངས་པའོ། །

[Block 2910]
སྡོམ་པ་བདག་ལ་བཤད་དུ་གསོལ། །
--- END BLOCKS ---
