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
[Block 841]
ལས་དང་པོ་པས་ནི་མ་ཞེས་པས་ནི་རང་གིས་དེ་ལ་དབང་ནོས་པའོ། །

[Block 842 [VERSE]]
སྲིང་མོ་ནི་དབང་ལྷན་ཅིག་ནོས་པའོ། །
བུ་མོ་ནི་རང་གིས་དབང་བསྐུར་བའོ། །

[Block 843]
རྟག་ཏུ་མཆོད༌[^343]ཅེས་པ་ནི་དབང་གི་དུས་སུ་ཇི་ལྟར༌[^344]རྒྱུན་མི་འཆད་པར་རོ། །

[Block 844]
རྣལ་འབྱོར་རིག་པ་ཞེས་པ་ནི་བླ་མའི་མན་ངག་བརྗོད་པའོ། །

[Block 845]
གར་མ་ནི་ཤེས་རབ་ཆེ་བའོ། །

[Block 846 [VERSE]]
ཚོས་མ་ནི་དད་པ་ཆེ་བས་བསྒྱུར་སླ་བའོ། །
རྡོ་རྗེ་མ་ནི་བསམ་གཏན་གྱིས་བསྟན་པའོ། །

[Block 847]
གདོལ་བ་མོ་ནི་བརྩོན་འགྲུས་ཀྱི་ཕྱག་རྒྱ་སྟེ་དཔའ་བའོ། །

[Block 848]
བྲམ་ཟེ་མ་ནི་ངང་ཚུལ་བཟང་བས་བཟོད་པ་ཅན་ཏེ། ཆོས་དེ་རྣམས་གང་ཡང་རུང་བ་དང་ལྡན་པའི་ལས་ཀྱི་ཕྱག་རྒྱ་བདག་མེད་མར༌[^345]བསྒོམ་པ་ནི་ཤེས་རབ་ཀྱི་ཆོ་ག་ཡིན་ལ་ཐབས་ཀྱི་ཆོ་ག་ནི༌[^346]རང་ཉིད་དགྱེས་པའི༌[^347]རྡོ་རྗེ་བསྒོམ་མོ། །

[Block 849 [VERSE]]
དེ་ཉིད་རིགས་པས་རྟག་ཏུ་མཆོད། །
ཅེས་པ་ནི་ཟླ་བ་གཟུང་བ༌[^348]དང་ལྡན་པའོ། །

[Block 850]
ཇི་ལྟར་དབྱེ་བར་མི་འགྱུར་བ་ནི་གསང་བའི་ཚུལ་ལོ། །

[Block 851]
རབ་ཏུ་འབད་པ་ནི་དམ་པ་ལ་དམིགས་པའི་མན་ངག་དང་ལྡན་པའོ། །

[Block 852]
བསྟེན་པ་ཉིད་ཅེས་བ་ནི་འདོད་པའི་ཡོན་ཏན་ནམ།

[Block 853 [VERSE]]
བཟའ་བ་ལ་སོགས་པའི་དམ་ཚིག་གོ། །
མ་གསང་ཞེས་པ་ནི་མཚོན་པ་སྟེ།
མ་འབད་ཅིང་མ་བསྟེན་པར་འགྱུར་ནའོ། །

[Block 854]
སྦྲུལ་དང་ཆོམ་རྐུན་ཞེས་པ་ནི་ཚེ་འདིའི་ཉེས་པའོ། །

[Block 855]
ས་སྤྱོད་མེ་ཡིས་སྡུག་བསྔལ་བྱེད།[^349] །ཅེས་པ་ནི་ཤི་ནས་དམྱལ་བ་སྟེ་སྐྱེ་བ་གཞན་གྱིས་ཉེས་པའོ། །

[Block 856 [HEADING]]
###### ལས་སྨིན་པ། ^1-5-2-1-2-0

[Block 857]
ལས་སྨིན་ཅིང་རྫོགས་པས་ནི། སྐྱེད་བྱེད་མ་ལ་སོགས་པ་ནི་བགྲོད་དང་བགྲོད་མིན་དུ་ཤེས་པར་བྱ་བའི་ཕྱིར། ལས་ཀྱི་ཕྱག་རྒྱ་དང་ཐ་མལ་བ་ཉིད་ལ་བྱའོ། །

[Block 858]
ཐབས་དང་ཤེས་རབ་ཆོ་ག་ལ་སོགས་པ་ནི་ལས་དང་པོ་པ༌[^350]དང་མཐུན་ནོ། །

[Block 859 [HEADING]]
##### རང་ལུས་ཐབས་ཏེ་སྟེང་སྒོ་ལ་བརྟེན་པ། ^1-5-2-2-0

[Block 860]
རང་ལུས་ཐབས་ཀྱི་སྟེང་སྒོ་ལ་བརྟེན་པས་ནི་སྐྱེད་བྱེད་མ་སྟེ། །གཡོན་གྱི་རྐྱང་མ་ནས་རྒྱུ་བའི་རླུང་ངོ་། །སྲིང་མོ་ཉིད་གཡས་ཀྱི་རོ་མ་ནས་རྒྱུ་བའི་རླུང་ངོ་། །རྣལ་འབྱོར་རིགས་པས་རྟག་ཏུ་མཆོད། །ཅེས་པ་ནི་དབུས་ཨ་ཝ་དྷཱུ་ཏཱི་རུ་ལྷན་ཅིག་སྐྱེས་པའི་རླུང་དུ་སྦྱོར་བའོ། །

[Block 861]
གར་མ་ནི་མིག་དང་འབྲེལ་བ་མྱུར་བའི་རླུང་ངོ་། །ཚོས་མ་ནི་རྣ་བ་དང་འབྲེལ་བ་བསྒྱུར་བའི་རླུང་ངོ་། །རྡོ་རྗེ་མ་ནི་སྣ་དང་འབྲེལ་བ༌[^351]བརྟན་པའི་རླུང་ངོ་། ། གདོལ་པ་མོ་ནི་ལྕེ་དང་འབྲེལ་བ་བག་ཚ་བ་མེད་པའི་རླུང་ངོ་། །བྲམ་ཟེ་མ་ནི་ལུས་དང་འབྲེལ་བ་ཉེས་པ་དག་པའི་རླུང་ངོ་། །ཐབས་ཀྱི་ཆོ་ག་ནི་རླུང་དེ་རྣམས་ཀྱིས་མི་གཡོ་མི་འགོག་པར་ཡུལ་རྣམས་ལ་བདེ་བར་སྦྱོར་བའོ། །ཤེས་རབ་ཀྱི་ཆོ་ག༌[^352]ནི་དེ༌[^353]རྣམས་བསྡུས་ཏེ་རང་བཞིན་མེད་པར་བྱ་སྟེ། ཨ་ཝ་དྷཱུ་ཏཱིར་ལྷན་ཅིག་སྐྱེས་པའི་རླུང་དུ་སྦྱོར་བའོ། །

[Block 862]
དེ་ཉིད་རིག་པར་རྟག་ཏུ་མཆོད་ནི་ཆོ་ག་དེ་རྣམས་དང་ལྡན་པ་རྒྱུན་དུ་རྣལ་འབྱོར་དུ་བྱེད་པའོ། །

[Block 863]
ཇི་ལྟར་དབྱེ་བར་མི་འགྱུར་ཞེས་པ་ནི་ཐབས་དང་ཤེས་རབ་སྦྱོར་བའོ། །

[Block 864]
རབ་ཏུ་འབད་ཅེས་པ་ནི་ལུས་ངག་ཡིད་གསུམ་ཀྱི་བརྩོན་འགྲུས་སོ། །

[Block 865]
བརྟེན་པ་ཉིད་ནི་ཤེས་པར་བྱའོ། །

[Block 866]
མ་གསང་ཞེས་པ་ནི་རང་གི༌[^354]མའི་རྣམ་པར་རྟོག་པའོ། །

[Block 867]
སྦྲུལ་དང་ཆོམ་རྐུན་ལ་སོགས་པ་ནི་རྣམ་རྟོག་ལས་སྤྲུལ་པའི་ཉེས་པ་སྟེ། རྨི་ལམ་གྱི་སྡུག་བསྔལ་བཞིན་ནོ། །

[Block 868 [HEADING]]
##### དེ་ཁོ་ན་ཉིད་ཤེས་རབ་མི་དམིགས་པ་དང་སྦྱར་བ། ^1-5-2-3-0

[Block 869]
དེ་ཁོ་ན་ཉིད་ཤེས་རབ་དང་སྦྱར་བ་ནི།

[Block 870 [VERSE]]
སྐྱེད་བྱེད་མ་ནི་སེམས་སོ། །
སྲིང་མོ་ཉིད་ནི་སེམས་ལས་བྱུང་བའོ། །

[Block 871]
རྣལ་འབྱོར་རིག་པ༌[^355]ཞེས་པ་ནི་སེམས་དང་སེམས་ལས་བྱུང་བ་དེ་དག་མེད་ཅིང་འགོག་པ་མ་ཡིན་ཏེ། །མ་སྟེ༌[^356]ཐབས་དང་ཤེས་རབ་ལ་མ་བརྟེན་གཞན་ལ་འགོག་པ་སྦྱར་བ་དེ་ཉིད་ཆགས་བྲལ་ལྟ་བུ་གཉུག་མའི་དབང་པོར་བདེ་བ་ཆེན་པོ་རང་འབྱུང་བའོ། །

[Block 872]
རྟག་ཏུ་མཆོད་ཅེས་པ་ནི་དབང་པོ་རང་སྣང་རྒྱུན་མི་འཆད་པའི་མན་ངག་གོ། །

[Block 873 [VERSE]]
གར་མ་ནི་གཟུགས་དང་མིག༌[^357]གི་དབང་པོའོ། །
ཚོས་མ་ནི་སྒྲ་དང་རྣ་བའི་དབང་པོའོ། །
རྡོ་རྗེ་མ་ནི་དྲི་དང་སྣའི་དབང་པོའོ། །
གདོལ་པ་མོ༌[^358]ནི་རོ་དང་ལྕེའི་དབང་པོའོ། །

[Block 874]
བྲམ་ཟེ་མ་ནི་རེག་བྱ་དང་ལུས་ཀྱི་དབང་པོའོ། །

[Block 875 [VERSE]]
ཐབས་དང་ཤེས་རབ་ཆོ་ག་ཡིས། །
ཞེས་པ་ནི་ཕྱག་རྒྱ་ཆེན་པོའོ། །

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
--- END BLOCKS ---
