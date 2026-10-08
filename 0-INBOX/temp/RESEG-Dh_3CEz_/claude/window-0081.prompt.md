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
[Block 2836]
དེ་བཤད་པ་ཡང་རྡོ་རྗེ་སྙིང་པོས་གསོལ་ཞེས་པ་ནི་བདག་གི་ཡིན་ཡང་དེ་ལས་རྒྱས་པར་རོ། །

[Block 2837]
ཐབས་གང་གིས་བསྐྱེད་ལགས་ཞེས་པ་ནི་ལམ་རིམ་པ་གཉིས་དྲིས་པའོ། །

[Block 2838]
མ་བསྐྱེད་ན་བསོད་ནམས་མེད་ཅིང༌[^1193]སྡིག་པ་མེད་པས་བསྐྱེད་དེ་མི་སྤང་བར་ཞུས་པ་ཡང་བཀའ་སྩལ་ཞིང་རིམ་གཉིས་སུའོ། །

[Block 2839]
དཀྱིལ་འཁོར་ནི་རྟེན་གྱི༌[^1194]རྣལ་འབྱོར་རོ། །

[Block 2840]
འཁོར་ལོ་ནི་བརྟེན་པའོ། །

[Block 2841]
ཐབས་ནི་ཡེ་ཤེས་དགུག་པ་དང་དབང་དང་མཆོད་པ་ལ་སོགས་པའོ། །ཅི་རྫོགས་རིམ་གྱི་སྐབས་སུ་མི་འགལ་ལམ་ཞེ་ན། བསྐྱེད་རིམ་ཉུང་ལྡན་ཐ་མལ་གྱི་རྣམ་པར་བསྒྱུར་བ་ཙམ་ཡིན་པའི་ཕྱིར་རང་ཞེས་པ་ནི་ཕྱག་རྒྱ་ཆེན་པོ་ཉིད་དོ། །

[Block 2842]
བྱིན་གྱིས་བརླབ་པ་ཞེས་པ་ནི། སྔར་བསྟན་པ་བཞིན་དབང་པོའི་རང་སྣང་བ་འཆད་པའམ་འཆད་པར་འགྱུར་བ་ལྟར་སྤྱོད་ལམ་དང་བསྲེའོ། །

[Block 2843 [VERSE]]
རིམ་པས་ཞེས་པ་ནི་རྫོགས་རིམ་མོ། །
ཀྱང་ནི་བསྐྱེད་རིམ་བསྡུ་བ་སྟེ་གཉིས་སོ། །

[Block 2844]
ཀུན་རྫོབ་དོན་དམ་བསྐྱེད་པ་ནི་གོ་རིམས་བཞིན་དུའོ། །

[Block 2845 [VERSE]]
ཀུནྡ་ལྟ་བུའི་ཟླ་བ་སྟེ་ཞུ་བའོ། །
བདེ་བ་ནི་མཚོན་པ་སྟེ་ནམ་མཁའ་ལྟ་བུའོ། །

[Block 2846]
དེ་ནི་དེ་དག་སྡོམ་པའི་གནས་བསྟན་པའི་ཕྱིར་བུད་མེད་ཅེས་བྱ་བ་ལ་སོགས་པ་ཚིགས་སུ་བཅད་པ་ཕྱེད་དང་གཉིས་ཏེ། ཨེ་ཝཾ་རྣམ་པའི་རང་བཞིན་དུ། །ཞེས་པ་ཤེས་རབ་ཀྱི་གསང་བའི་གནས་དང་། ཐབས་ཀྱི་གསང་བའི་གནས་དང་། གཉིས་སྦྱར་བ་ལས་ཤེས་པར་བྱ་བ་དང་། ཡང་ལྟེ་བའི་གནས་དང་སྤྱི་བོའི་གནས་སུ་སྦྱར་བ་ལས་ཤེས་པར་བྱ། གཉུག་མའི་དབང་པོ་དང་དེ་བསྟེན་པའི་ཐབས་དང་བཅས་པ་ལས་ཤེས་པར་འགྱུར་རོ། །

[Block 2847]
ད་ནི་དེ་དག་གི་རང་བཞིན་བསྟན་པའི་ཕྱིར། འདི་ཉིད་ནི་དོན་དམ་ཀུན་རྫོབ་བོ། །

[Block 2848]
འཁོར་བ་ནི་བསླད་པའོ། །

[Block 2849 [VERSE]]
མྱ་ངན་ལས་འདས་པ་ནི་གཉུག་མ་མ་བཅོས་པའོ། །
དེའི་ཕྱིར་འཁོར་བ་སྤངས་ནས་གཞན་ཉན་ཐོས་ལྟ་བུའོ། །

[Block 2850]
མྱ་ངན་ལས་འདས་པ་མི་རྟོག་ནི་རང་བཞིན་གཉུག་མ་མ་ཤེས་པ་སྟེ་བསྟན་པའོ། །

[Block 2851]
དེ་བཤད་པའི་ཕྱིར།

[Block 2852 [VERSE]]
འཁོར་བ་གཟུགས་དང་སྒྲ་ལ་སོགས། །
ཞེས་པ་ནི་ཡུལ་གྱི་སྐྱེ་མཆེད་རྣམས་སོ། །

[Block 2853]
འཁོར་བ་ཚོར་བ་ལ་སོགས་པ་ནི་ཕུང་པོ་རྣམས་སོ། །

[Block 2854]
འཁོར་བ་དབང་པོ་ནི་ནང་གི་སྐྱེ་འཆེད་དོ། །

[Block 2855]
འཁོར་བ་ཞེ་སྡང་ལ་སོགས་པ་ནི་ཉོན་མོངས་པ་ལྔའམ་རྣམ་པར་ཤེས་པའི་ཁམས་སོ། །

[Block 2856]
འདི་རྣམས་ཆོས་ནི་མྱ་ངན་འདས་ནི་གཉུག་མ་ལས་མི་འགྱུར་ཞིང་རང་གི་མཚན་ཉིད་འཛིན་པས་ཆོས་སོ། །

[Block 2857]
རྨོངས་ཕྱིར་འཁོར་བ་ནི་རང་གི་མཚན་ཉིད་མ་རྟོགས་པར་འཁོར་བ་ལྟར་ལོག་པར༌[^1195]སྣང་ངོ་། །རྨོངས་བྱེད་འཁོར་བ་དག་པ་ནི་གློ་བུར་བ་མེད་པའོ། །

[Block 2858]
མྱ་ངན་ལས་འདས་པར་འགྱུར་ནི་དག་པའི་ལུས་དང་སེམས་ལ་དབང་ཐོབ་པའོ། །

[Block 2859]
རྟོག་པ་མེད་པའི་བྱང་ཆུབ་ཀྱི༌[^1196]སེམས་ནི་ལུས་དང་སེམས་ཀྱི་ལྷན་ཅིག་སྐྱེས་པའོ། །

[Block 2860]
ཀུན་རྫོབ་དོན་དམ་རྟེན་དང་བརྟེན་པའོ། །

[Block 2861]
ཚུལ་ཅན་ནི་རུང་བ་སྟེ་རྟེན་ཡི་གེ་ཡང་བསྐྱེད་པ་མ་ཡིན་པའི་རང་བཞིན་ནོ། །

[Block 2862]
ད་ནི་ཀུན་རྫོབ་བསྐྱེད་པའི་ཐབས་བསྟན་པའི་ཕྱིར། ཤིན་ཏུ་བཞིན་བཟངས་ནས་དེར་སྦྱོར་བ་ལས་བྱུང་བའི༌[^1197]རྣལ་འབྱོར་མ་ཀུན་ལས་བྱུང་བའི༌[^1198]བཤད་པའོ། །

[Block 2863]
བསྟན་པ་གཞན་གྱི་བཤད་པ་ཡང་མི་སྤང་ནི་མི་སྤང་བའི་ལན་ནོ། །

[Block 2864 [VERSE]]
ག་བུར་ནི་ལྷན་ཅིག་སྐྱེས་དགའི་ལན་ནོ། །
མཁས་པ་ནི་འགྲིབ་མེད༌[^1199]ཟད་མེད་ཀྱི་ལན་ནོ། །

[Block 2865]
ལག་ཏུ་མི་བླང་བ་ལ་སོགས་པ་ནི་བཏུང་མཆོག་གི་ལན་དུའོ། །

[Block 2866]
ད་ནི་དོན་དམ་ལྷན་སྐྱེས་སུ་བསྟན་པའི་ཕྱིར། ལྷན་སྐྱེས་རྣམ་དག་ཉིད་ཀྱི་ནི།[^1200] །

[Block 2867 [VERSE]]
ག་བུར་ཉིད་ནི་བདག་མེད་མ། །
ལ་སོགས་པ་དོན་དམ་སྐྱེད་པ་གསུངས་ཏེ།

[Block 2868]
ཀུན་རྫོབ་ཉིད་ནི་ཀུན་རྫོབ་སྔ་མ་དེ་ཉིད་དོ། །

[Block 2869]
བདག་མེད་མ་དེ་ནི་རྣལ་འབྱོར་མའོ། །

[Block 2870]
བདེ་བ་བདག་མེད་ཚུལ་ཅན་ནི་ཐབས་དང་ཤེས་རབ་ཀྱི་རང་བཞིན་ནོ། །

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
--- END BLOCKS ---
