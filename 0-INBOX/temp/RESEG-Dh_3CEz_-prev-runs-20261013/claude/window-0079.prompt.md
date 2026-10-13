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
[Block 2766]
ཌིཎྜི་མ་སྟེ་གཡུང་མོ་ལ་སོགས་པ་མི་སྤང་བ་སྟེ། རང་རིག་གི་འོད་ཟེར་མཐའ་ཡས་པ་སྣང་བས་འབྱུང་བ་ལྔ་དང་ཡེ་ཤེས་ལྔ་ལ་སོགས་པ་རིགས་ཀྱི་དབྱེ་བ་ཡོངས་སུ་རྫོགས་པའོ། །

[Block 2767]
ཡང་ན་བླ་ན་མེད་པའི་རིགས་དབྱེ་བ་ཡོངས་སུ་རྫོགས་པའོ། །

[Block 2768]
དེ་ལྟར་བྱས་པས་རྟགས་གསུམ་འབྱུང་སྟེ་འཛིན་པའི་རྟགས་དངོས་གྲུབ་གྲུབ་པའི་རྟགས་དེ་ཁོ་ན་ཉིད་ལ་འཇུག་པའི་རྟགས་སོ། །

[Block 2769]
ཡང་ན་ལྟ་བའི་རྟགས་བསྒོམ་པའི་རྟགས་ཙརྱའི་རྟགས་སོ། །

[Block 2770]
དཔལ་དགྱེས་པ་རྡོ་རྗེའི་རྒྱུད་ནས་རྡོ་རྗེའི་གླུ། བརྟག་པ་གཉིས་ཀྱི་དོན་ཡང་འདིར་གནས་ཤིང་ལམ་གྱི་རིམ་པ་ཉེ་བར་རྫོགས་པ་ན་ཐ་མར༌[^1176]ཕྱག་རྒྱ་ཆེན་པོར་ཉེ་བར་གནས་པའོ། །

[Block 2771 [HEADING]]
#### རྡོ་རྗེའི་གར། ^2-4-2-0

[Block 2772]
ད་ནི་རྡོ་རྗེའི༌[^1177]གར་བསྟན་པའི་ཕྱིར། དྲན་པས་མི་འཕྲོགས་རྣལ་འབྱོར་ཞེས་པ་ནི་གཡེང་བར་མ་གྱུར་པའོ། །

[Block 2773]
ཧེ་རུ་ཀའི་གཟུགས་ཀྱིས་གར། །ཞེས་པ་ནི་རིགས་བསྡུས་པ་ལུས་ཀྱི་སྤྱིས་སོ། །

[Block 2774]
ཆགས་བྲལ་མིན་གོམས་སེམས་ཀྱིས་ནི། །ཞེས་པ་གང་གི་ཧེ་རུ་ཀ་སྟེ་དགའ་བྲལ་མ་ཡིན་པའོ། །

[Block 2775]
འདོད་ཆགས་སེམས་ཀྱིས་ཞེས་པ་ནི་མཆོག་དགའ་འམ་ཐབས་ཀྱི་ཁྱད་པར་ལས་སོ། །

[Block 2776]
བསྒོམ་པ་ཉིད་ནི་ལྷན་སྐྱེས་སོ། །

[Block 2777]
ད་ནི་གླུ་དང་གར་ཐུན་མོང་དུ་ཡོན་ཏན་གྱི་ཆ་སྟོན་ཏེ། རྡོ་རྗེ་ཆོས་ནི་འོད་དཔག་ཏུ་མེད་པ་གསུང་གི་རིགས་ཏེ་གླུའོ། །

[Block 2778 [VERSE]]
སངས་རྒྱས་ནི་རྣམ་པར་སྣང་མཛད་དེ་གར་རོ། །
རྣལ་འབྱོར་མ་ནི་རྗེས་སུ་ཆགས་པའི་ཡུལ་ལོ། །

[Block 2779]
མ་མོ་ནི་གར་གྱི་ཆགས་པའི་ཡུལ་ཏེ་དེ་དག་ནི་ཐུགས་སོ། །

[Block 2780]
གླུ་དང་གར་ནི་འདི་དག་གི་སྔར་གྱི་མཚན་ཉིད་དང་ལྡན་པའོ། །

[Block 2781]
གླུ་བླང་གར་ཡང་བྱ་ནི་ཧེ་རུ་ཀའི་ང་རྒྱལ་ལ་སྐུ་དང་གསུང་གི་ཡོན་ཏན་དང་ལྡན་པས་ཐུགས་ཀྱི་ཡུལ་རྣལ་འབྱོར་མ་དང་མ་མོ་དང་ལྡན་པའོ། །

[Block 2782]
ཡང་ན་རྡོ་རྗེ་ཆོས་སངས་རྒྱས་ནི་སྐུ་མདོག་དཀར་པོའི་གླུའི་གྲོགས་སུ་བསྟན་ལ། རྣལ་འབྱོར་མ་དང་མ་མོ་ནི༌[^1178]གར་གྱི་གྲོགས་འབྲས་བུ་ཧེ་རུ་ཀས་གར་བྱེད་པ་སྟོན༌[^1179]ཏོ། །

[Block 2783]
ད་ནི་དེའི་ཕན་ཡོན་བསྟན་པ་ཚོགས་སྲུང་ནི་འཁོར་རོ། །

[Block 2784]
བདག་གི་གཙོ་བོའམ་བྱེད་པའོ། །

[Block 2785]
འཇིག་རྟེན་དབང་དུ་བྱེད་པ་ནི་ཡིད་འཕྲོག་པའོ། །

[Block 2786]
སྔགས༌[^1180]ཀྱི་ཟློས་པ་ནི་གླུའོ། །

[Block 2787]
གར་སྒོམ་པ༌[^1181]ནི་སྔ་མ་ལྟར་རོ། །

[Block 2788]
ད་ནི་རིམ་པ་བསྟན་པའི་ཕྱིར་ཚོགས་ཀྱི་བདག་པོ་སྔར་བྱས་ནི་སློབ་དཔོན་གྱི་གླུ་དང་གར་ནང་དུ་བསྒོམ་པའམ་དངོས་སུ་དང་པོར་བྱའོ། །

[Block 2789]
དྲི་མཚོན་པ་ནི་དངོས་གྲུབ་ཤིས་པའི་མཚན་མ་གར་གྱིའོ། །

[Block 2790 [VERSE]]
སྒོག་པའི་དྲི་ནི་ངན་པའོ། །
བྱ་རྒོད་དྲི་ནི་ཅུང་ཟད་ངན་པའོ། །

[Block 2791]
ག་བུར་ནི་ཞིམ་པའོ། །

[Block 2792]
མཱ་ལ་ཡ་ཛ་ནི་ཧེ་མ༌[^1182]ལ་ཡ་ཛ་སྟེ་ཁ་བ་ཅན་ལས་སྐྱེས་པ་སྟེ་ཙནྡན་ཤིན་ཏུ་ཞིམ་པའོ། །

[Block 2793]
ད་ནི་གླུའི་མཚན་མའི་དང་པོ༌[^1183]ནི་དང་པོའི་སྒྲའོ། །

[Block 2794]
བུང་བ་ནི་བར་དུའོ། །

[Block 2795]
བ་ལང་ཚེའི་སྒྲ་ནི་ཐ་མར་རོ། །

[Block 2796]
དེ་གང་དུ་ཞེ་ན། གླུའི་མཐའ་ནས་མཉམ་པར་བྱ་ནི་དྲིལ་བུའི་སྒྲ་མཐའ་ལྟ་བུའོ། །

[Block 2797]
གནས་གང་དུ་ཞེ་ན། ཕྱི་རོལ་གྱི་ཚལ་དུ་སྐྱེ་ཤིང་གི་ར་བའམ་དུར་ཁྲོད་དུའོ། །

[Block 2798]
གླུའི་བྱིན་རླབས་མཚན་ཉིད་ནི་དངོས་གྲུབ་བམ་ཤིས་པ་བརྗོད་པའོ། །

[Block 2799]
ད་ནི་ཕྱག་རྒྱའི་ལན་ཕྱག་རྒྱ་རྟགས་དང་མཚན་མ་ལ་སོགས་པའོ། །

[Block 2800]
འདི་ནི་རིགས་མཚོན་པ་སྟེ་བསྐྱེད་པའི་རིམ་པ་མཐའ་དག་རྣམ་པ་གཉིས་ཏེ། ཞི་བའི་རྣམ་པ་དང་ཁྲོ་བོའི་རྣམ་པའོ། །

[Block 2801]
དེ་དག་ཐམས་ཅད་ཀྱང་རྒྱལ་བ་རིགས་ལྔ་ལས་མི་འདའ་སྟེ། རྒྱུ་སེམས་ཅན་གྱི་གནས་སྐབས་ནས་སྦྱང་གཞི་རྣམ་པ་ལྔ་ཡོད་པས་དེ་སྤྱོད་བྱེད་ཀྱང་རིགས་ལྔ་སྟེ། དེ་སྐད་དུ་ཡང་།

[Block 2802 [VERSE]]
ཞི་བ་ཡི་ནི་དཀྱིལ་འཁོར་རོ། །
ཁྲོ་བོ་ཡི་ནི་དཀྱིལ་འཁོར་ཏེ། །
རྗེས་སུ་གཟུང་བ་བྱ་ཕྱིར་རམ། །
གཞན་དག་ཚར་གཅད་བྱ་ཕྱིར་བཤད། །

[Block 2803]
ཡང་ལྷ་དང་ལྷ་མོ་ཐ་དད་པ་དང་དེའི་རིགས་འབྱུང་སྟེ་དེ་མེད་ཀྱང་ནི་དེ་ཡོད་ནི། འགྲོ་བའི་དོན་དུ་བསྟན་པ་ཡིན། །ཞེས་གསུངས་སོ། །

[Block 2804]
དེ་རྣམས་ཀྱི་རྒྱུ་མཚན་ནི་འོག་ནས་འཆད་དོ། །

[Block 2805]
ཡང་རྣལ་འབྱོར་མ་རྣམས་ཀྱི་ས་བོན་ནི་ཨཱ་ལི་དང་པོ་ལ་སོགས་པ་སྟེ་དེ་བཞིན་ནོ། །
--- END BLOCKS ---
