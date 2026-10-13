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

[Block 2596]
རྣམ་པར་སྦྱོང་ནི་གཅིག་དང་དུ་མ་དང་བྲལ་བ་ལ་སོགས་པའི་ཤེས་རབ་ཀྱི་རིམ་པ༌[^1110]དང་འདྲ་བར་བདག་མེད་པའི་རང་བཞིན་དུ་སྦྱོར་རོ། །

[Block 2597]
དེ་ནི་དེ་ཉིད་ཀྱི་རིམ་པ༌[^1111]ནི་སྡོམ་པ་སྟེ། དབང་གསུམ་པར་ཤེས་པར་བྱའོ། །

[Block 2598]
བོ་ལ་ཀཀྐོ་ལ་སྦྱོར་ནི་ཟླ་བ་བཟུང་བ་སྟེ་བཤད་ཟིན། དེའི་བདེ་བ་རྟེན་དང་བརྟེན་པ་ནི་འབྲེལ་པའི་རྟགས་སོ། །ཤེས་པར་གྱུར་པའི་མ་བྱ་བ་ནི་དེས་མི་རྟོགས་པར༌[^1112]རོ། །

[Block 2599]
ད་ནི་གླེང་གཞི་ཨེ་ཝཾ་ལ་སྡོམ་པའི་ཆོས་ཏེ། རྟོག་པའི་ཡན་ལག་ཏུ་ཐབས་ཀྱི་རིམ་པ་དབང་ལ་སོགས་པ་ནི་གོ་བཟློག་སྟེ་བསྟན་ནས་སྲུང་སྡོམ་གྱི་དམ་ཚིག་དང་ཐབས་སུ་འགྱུར་བར་བསམས་ནས། རྡོ་རྗེ་སྙིང་པོ་པ་དྲིས་པ་དང་། [^1113]བཅོམ་ལྡན་འདས་ཀྱི༌[^1114]ལན་ཏེ།

[Block 2600 [VERSE]]
ཁྱོད་ཀྱིས་སྲོག་ཆགས་གསད་པར་བྱ། །
བརྫུན་གྱི་ཚིག་ཀྱང་སྨྲ་བ་དང་། །
ཁྱོད་ཀྱིས་མ་བྱིན་པར་ཡང་ལོང་། །
ཕ་རོལ་བུད་མེད་བསྟེན་པར་གྱིས། །

[Block 2601 [HEADING]]
#### འདི་དག་གི་དགོངས་པ། ^2-3-2-0

[Block 2602]
ཞེས་བྱ་བ་ནི་འདི་དག་གི་དགོངས་པ་ནི་བཞི་སྟེ། དགོངས་པའི་སྐད་ཀྱིས་བཤད་པ་དང་། དགེ་བ་ཐུལ་གྱིས་གནང་བ་དང་། ཡུལ་དང་། བསམ་པ་དང་། སྦྱོར་བས་གནང་བ་དང་།

[Block 2603 [HEADING]]
##### དགོངས་པའི་སྐད་ཀྱིས་བཤད་པ། ^2-3-2-1-0

[Block 2604 [VERSE]]
མཉམ་པ་དེ་ཁོ་ན་ཉིད་ལ་དགོངས་པའོ། །
དགོངས་པའི་སྐད་ཀྱིས་བཤད་པ་ནི།
སེམས་ཅན་སྲོག་ཆགས་གསོད་པ་ཉིད། །

[Block 2605]
ཅེས་པ་ནི་བདག་གཞན་དུ་འཛིན་པའི་ཞེན་པ་སྤང་བར་བྱའོ། །

[Block 2606]
འཇིག་རྟེན་བསྒྲུབ༌[^1115]ཅེས་པ་ནི་བརྫུན་དང་འདྲ་བ་སྟེ་ཁས་ལེན་ཅིང་དམ་བཅའ་བའོ། །

[Block 2607]
བཙུན་མོ་ཞུ་བ་མ་བྱིན་པ་ནི་ཟླ་བ་མ་ཡིན་པར་ཉི་མ་བླང་བའི་མན་ངག་གོ། །

[Block 2608]
གཞན་གྱི་བུད་མེད་རང་མཚུངས་མཛེས། །ཞེས་པ་སངས་རྒྱས་སྤྱན་དང༌[^1116]མཱ་མ་ཀཱི་ལ་སོགས་པ་བསྟེན་པའོ། །

[Block 2609]
དེ་དག་ནི་གོ་རིམས་སུ་བཤད་དོ། །

[Block 2610 [HEADING]]
##### དགེ་བ་ཐུལ་གྱིས་གནང་བ། ^2-3-2-2-0

[Block 2611]
དགེ་བ་ཐུལ་གྱིས་གནང་བ་ནི་སྲོག་ཆགས་གཅིག་བསད་ན་མང་པོ་དག་སྲོག་ཐར་བར་མཐོང་བ་ནི་སྔོན་བཅོམ་ལྡན་འདས་དེད་དཔོན་དུ་གྱུར་པའི་ཚེ། ཚོང་པ་ཅིག༌[^1117]ལ་ཤ༌[^1118]པའི་ཚལ་བ་གཅིག་བསྣུན་ཏེ། བསད་ནས་ཚོང་པ་གཞན་ཐར་བ་ལྟ་བུའོ། །ཇི་ལྟར་སྡིག་པར་མི་འགྱུར་ཞེ་ན། སྙིང་རྗེ་ལྡན་ཞིང༌[^1119]བྱམས་ཕྱིར་དང་། སེམས་དགེ་བ་ལ་ཉེས་པ་མེད། །ཅེས་གསུངས་སོ། །

[Block 2612]
བརྫུན་གནང་བ་ནི་ཉན་ཐོས་དག་ལ་ནི་རྣམ་པ་ཐམས་ཅད་དུ་མ་གནང་སྟེ། ནམ་མཁའ་མཐོང་དང་སེན་མོ་མཐོང་། །ཞེས་བརྗོད་པ་དང་། ཐེག་པ་ཆེན་པོ་ནི་སྲོག་གི་སྐྱབས་སུ་གྱུར་ན་གསོད་མའི་མི་དག་གིས་གསོད་པ་འགའ་ཞིག༌[^1120]སྐྱབས་སུ་སོང་བ་བདག་གིས་མཐོང་ནས་མཐོང་བཞིན་དུ་མ་མཐོང་ཞེས་ཤེས་བཞིན་བརྫུན་ཀྱང་གནང་ངོ་། །

[Block 2613]
མ་བྱིན་པར་བླང་པ་ནི། སེར་སྣ་ཅན་གྱི་ནོར་ཕྲོགས་ཤིང་བརྐུས་ལ། སེམས་ཅན་གཞན་ཕ་རོལ་གྱི་སྐྱབས་སམ་ཕན་པར་སྦྱིན་ནོ། །

[Block 2614]
ཕ་རོལ་གྱི་བུད་མེད་བསྟེན་པ་ནི་གཞན་ཕ་རོལ་སྲོག་གི་སྐྱབས་སུ་གྱུར་ན་འདོད་པ༌[^1121]ལོག་པར་ཀྱང་སྤྱོད༌[^1122]དེ། དཔེར་ན་བྲམ་ཟེའི་ཁྱེའུ་སྐར་མའི་གཏམ་རྒྱུད་ལྟ་བུའོ། །

[Block 2615]
དེ་སྐད་དུ།

[Block 2616 [VERSE]]
གལ་ཏེ་སྦྱིན་པའི་དུས་དག་ཏུ། །
ཚུལ་ཁྲིམས་བཏང་སྙོམ་གཞག་པར་གསུངས། །

[Block 2617]
ཞེའོ། །

[Block 2618 [HEADING]]
##### ཡུལ་དང་བསམ་པ་དང་སྦྱོར་བས་གནང་བ། ^2-3-2-3-0

[Block 2619]
ཡུལ་དང་བསམ་པ་ལ་སོགས་པས་གནང་བ་ནི་འོག་ནས་བསྟན་པ་ལ་གནོད་པ་བྱེད་པ་དང་། བླ་མའི་དགྲར་གྱུར་པ་ལ་སོགས་པའོ། །

[Block 2620]
བསམ་པ་ནི་སྙིང་རྗེའི་དབང་གིས་བསམ་པ་དཀར་བའོ། །

[Block 2621]
སྦྱོར་བས་གནང་བ་ནི་ཁ་སྦྱོར་འབྱེད་པ་སྟེ་འོག་ནས། བསམ་གཏན་སྔགས་ཀྱི་སྦྱོར་བ་ཡིས། །ཞེས་པ་ལ་སོགས་པ་སྟེ། འདིར་ནི་བསམ་གཏན་དང་སྔགས་ཙམ་གྱིས་བྱའི། འཁྲུལ་འཁོར་དང་སྦྱིན་སྲེག་ལ་སོགས་པ་ནི་བཀག་པའོ། །

[Block 2622]
དེ་བཞིན་དུ་གསུམ་པོ་ལ་ཡང་ཅི་རིགས་པར་སྦྱར་བར་བྱའོ། །

[Block 2623 [HEADING]]
##### མཉམ་པ་དེ་ཁོ་ན་ཉིད་ལ་དགོངས་པ། ^2-3-2-4-0

[Block 2624]
མཉམ་པ་དེ་ཁོ་ན་ཉིད་ནི་ང་དང་བདག་ཏུ་འཛིན་པའི་རྣམ་པར་རྟོག་པ་ནུབ་པའི་དུས་ཙམ་ན། དགེ་བ་དང་མི་དགེ་བ་ཐམས་ཅད་ཀྱང་མཉམ་པར་ཤེས་པའི་དུས་ན་ཐམས་ཅད་བྱ་བ་ཁོ་ན་ཡིན་ནོ། །

[Block 2625]
དེ་ནས་རྣལ་འབྱོར་པ་ཐམས་ཅད་ཀྱིས་བཅོམ་ལྡན་འདས་ལ་འདི་སྐད་ཅེས་གསོལ་ཞེས་བྱ་བ་ནི། རྡོ་རྗེ་སྙིང་པོས་དབང་བཞི་པའི་འཁོར་ལོ་དྲི་བ་མ་རྫོགས་པས། དྲི་བ་གཉིས་བསྐབས་མ་ཡིན་པར་ཤེས་ནས་ཞེས་པའོ། །

[Block 2626]
དེ་ཡང་ཡུལ་ལ་སོགས་པའི་གྲངས་དྲིས་པ་དང་། ལན་ནི་གོ་སླའོ། །

[Block 2627]
ད་ནི་སྔར་གྱི་གཅིག་དང་དུ་བྲལ་ལ་སོགས་པ་དང་འདྲ་བའི་རང་བཞིན་སྦྱོར་བ་བསྟན་པའི་ཕྱིར། རང་བཞིན་ཅི་ལགས་དྲིས་པའི་ལན་དུ། རང་བཞིན་གདོད་ནས་མ་སྐྱེས་པ། །ཞེས་པ་ནི་རང་བཞིན་ཉིད་དུ་འབྲེལ་ཏེ། དེའི་ཁྱད་པར་ཅི་ཞེ་ན། ཨ་ཏ་ཨ་ནུཏྤ་ན་སྟེ།

[Block 2628 [VERSE]]
གདོད་མ་ནས་མ་སྐྱེས་པའི་ཕྱིར་རོ། །
དཔེར་ན་ཐམས་ཅད་ཆུའི་ཟླ་བ་ལྟ་བུའོ། །
འདོད་པས་ནི་གྲུབ་པའི་མཐས་སོ། །

[Block 2629]
ཡང་ན་འདོད་ན་སྟེ་ཟབ་མོ་ལ་མོས་ནའོ། །

[Block 2630 [VERSE]]
རྣལ་འབྱོར་མ་ནི་བོད་པའོ། །
ཤེས་རབ་ཀྱིས་ནི་གདམས་པའོ། །
--- END BLOCKS ---
