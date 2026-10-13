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
[Block 2206]
རྡོ་རྗེ་སྙིང་པོ་ནི་བོད་པའོ།[^961] །ང་ཡིས་བཤད༌[^962]ནི་བཅོམ་ལྡན་འདས་ཉིད་ཀྱི་ཞལ་གྱིས་བཞེས་པའོ། །

[Block 2207]
བརྩེ་བ་ནི་སེམས་ཅན་དོན་དུ་སྟེ་གཞན་དུའོ། །

[Block 2208 [VERSE]]
དངོས་གྲུབ་དོན་ནི་བདག་དོན་ནོ། །
ཡང་བསྡུ་བ་ནི་ཕྱོགས་གཞན་མ་ཡིན་ནོ། །

[Block 2209]
ཟླ་བ་ཕྱེད་དུ་རྟོགས་ནི་བསྒོམ་པ་སྟེ་དུས་མྱུར་བའི་ཚད་དོ། །

[Block 2210]
བསམ་པ་ཐམས་ཅད་སྤངས༌[^963]ནི་ཉོ་ཚོང་དང་ཞིང་ལས་ལ་སོགས་པའོ། །

[Block 2211]
ཡང་ན་སྔ་མ་བཞིན་ཏེ་དབྱེར་མེད་པའི་དེ་ཁོ་ན་ཉིད་དང་ལྡན་པས་སོ། །

[Block 2212]
ལྷའི་གཟུགས་སུ་སེམས་པ་ནི་སྔ་མ་ལྟར་ཕྱོགས་གཉིས་སོ། །

[Block 2213]
ཉི་མ་གཅིག་ཏུ་མ་ཆད་པ་ནི་ཆུང་ངུ་ན་ཐུན་གཅིག་ཏུ་ཡང་ངོ་། །སྒོམ་པ་ནི༌[^964]ལྷའི་རྣམ་པར་གསལ་བའོ། །

[Block 2214]
ཡོངས་སུ་བརྟགས་པ་ནི་གཉིས་སུ་མེད་པའི་དེ་ཉིད་དང་ལྡན་པ་སྟེ། དེའི་ཕྱིར་ཀུ་བ་ལྟ་བུ་མ་ཡིན་ཞིང་དངོས་གྲུབ་ཏུ་ངེས་པར་མཉམ་གཞག་གི་ཡོན་ཏན་ནོ། །

[Block 2215]
ད་ནི་སྤྱོད་པ༌[^965]གྲོགས་དང་ལྡན་པའི་ཡོན་ཏན་བསྟན་པའི་ཕྱིར། རང་གཞན་དོན་བསྒྲུབ་པ་ནི་ཕྱག་རྒྱ་ཆེན་པོ་རྣམ་པ་ཀུན་གྱི་མཆོག་དང་ལྡན་པས་སོ། །

[Block 2216]
འཁོར་བ་ནི་ཞེས་པ་ནི་རྣལ་འབྱོར་པ་འདོད་ཆགས་མ་སྤངས་པས་སོ། །

[Block 2217]
ཐབས་གཞན་མེད་པ་ནི་ཉོན་ཐོས་ལ་སོགས་པ༌[^966]ཡིན་པའོ། །

[Block 2218]
དེའི་ཕྱིར་རིག་མ་གོམས་པ་ནི་བསྒོམ་པའི་དུས་སུ་འཕྲལ་དུ་མངོན་དུ་བྱེད་པའམ། ཡིད་ཆེས་ནི་སྤྱོད་པའི་དུས་ཉིད་དུ་ཡོན་ཏན་འབྱུང་བ་བསྟན་པའོ། །

[Block 2219]
དེ་བཤད་པའི་ཚིགས་སུ་བཅད་པ་གཅིག་སྟེ་གོ་སླའོ། །

[Block 2220]
ཕན་གནོད་འབྲས་བུ་འབྱུང་བ་ནི་འཕྲལ་དུ་ཉམས་སུ་མྱོང་བའོ། །

[Block 2221]
དེ་ལྟར་ངེས་པར་ཤེས་ནས་ནི་མ་འོངས་པར་ཡང་ཤེས་པར་བྱའོ། །

[Block 2222]
རྣལ་འབྱོར་པ་རྣམས་སྐད་ཅིག་ཀྱང་ཞེས་པ་ནི་འདི་དག་དང་གཞན་དུའོ། །

[Block 2223]
ཇི་ལྟར་ངུ་འབོད་གནས་སུ་སྐྱེ་ནི་ངུ་འབོད་ནི་མཚོན་པ་སྟེ་སྡུག་བསྔལ་ཅན་ཀུན་དུའོ། །

[Block 2224]
ཇི་ལྟར་སྐྱེས་ན་ནི་སྤོང་བའི་སྒྲ་སྟེ་མིའི་འགྲོ་བ་ཁོ་ནའོ། །

[Block 2225]
ད་ནི་སྤྱོད་པ་མཐར་ཕྱིན་པའི་ཆེ་བའི་བདག་ཉིད་བསྟན་པ་ནི། མཚམས་མེད་ལྔ་ནི་བྱེད་པ་དང་། །ཞེས་པ་ནི་ཕ་གསོད་པ་དང་མ་གསོད་པ་དང་། དགེ་འདུན་གྱི་དབྱེན་བྱེད་པ་དང་། དགྲ་བཅོམ་པ་སུན་འབྱིན་པ་དང་། སངས་རྒྱས་ཀྱི་སྐུ་ལ་ངན་སེམས་ཀྱིས་ཁྲག་འབྱིན་པ་དང་། སྲོག་ཆགས་གསོད་ལ་དགའ་བ་དང་ཞེས་པ་ནི་མི་དགེ་བཅུ་སྤྱོད་པའོ། །

[Block 2226]
གཞན་ཡང༌[^967]སྐྱེ་བ་དམན་པ༌[^968]གང༌[^969]ནི་སྨྱིག་མ་མཁན་དང་།

[Block 2227 [VERSE]]
ཕག་གསོད་པ་ལ་སོགས་པ་དང་། །
རྨོངས་དང་མ་རུངས་ལས༌[^970]བྱེད་དང་། །

[Block 2228]
ཞེས་པ་ནི་རྒྱ་པ་དང་ཉ་པ་དང་། ཀོ་ལྤགས༌[^971]བྱེད་པ་ལ་སོགས་པས་ཀྱང་འགྱོད་པའི་བསམ་པ་སྔ་མའི་ལས་སྤངས་ཏེ།

[Block 2229 [VERSE]]
དགྱེས་པའི་རྡོ་རྗེར་ཞུགས་ན་འགྲུབ་པར་འགྱུར་རོ། །
དགེ་བ་བཅུ་ལ་གོམས་པ་དང་། །

[Block 2230]
ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་དམ་པ་རྣམས་ཀྱིས་ངེས་པ་ཉིད་དུ་འགྲུབ་པར་འགྱུར་རོ། །

[Block 2231]
ད་ནི་སྤྱོད་པའི་ཚུལ་དངོས་བསྟན་པའི་ཕྱིར།

[Block 2232 [VERSE]]
འདིའི་དགོས་པ་ནི་ལེའུ་དྲུག་པར་ཤེས་པར་བྱའོ། །
རྣམ་པ་ཆ་ལུགས་དང་ལྷའི་ང་རྒྱལ་དང་།
གནས་དེ་རྣམས་ཀྱང་ལེའུ་དྲུག་པ་ལྟར་ཤེས་པར་བྱའོ། །

[Block 2233]
དྲོད་ཚད་ནི་སྐད་ཅིག་མར་ལྷར་གསལ་བ་དང་། དངོས་པོ་ལྷར་གསལ་བ་དང་། དངོས་པོ་སྒྱུར་ནུས་པ་སྟེ་འདི་ནི་བསྐྱེད་པའི་རིམ་པའི་སྤྱོད་པའི་དྲོད་ཚད་དོ། །

[Block 2234]
རྒྱུ་མཚན་གྱི་དྲོད་ཚད་ནི་ལེའུ་དྲུག་པ་ལྟར་ཤེས་པར་བྱའོ། །

[Block 2235]
ད་ནི་གསང་བའི་སྤྱོད་པ་ལ་སོགས་པའི་གྲོགས་བསྟན་པར་བྱ་བའི་ཕྱིར། ཟླ་བ་གཅིག་ཏུ་གསང་ལ་སྤྱོད་པ་ནི་དུས་མྱུར་བའི་ཚད་དོ། །

[Block 2236]
ཇི་སྲིད་ཕྱག་རྒྱ་མ་རྙེད་པ་ནི་མ་རྙེད་པའི་ཚེ་ཇི་ལྟར་བཙལ་བའོ། །

[Block 2237]
གནང་བ་སྦྱིན་པ་སྔགས་པ་ལ་ནི་ཚོལ་བའི་ནུས་པ་དང་ལྡན་པའོ། །

[Block 2238]
རྣལ་འབྱོར་མའི་བསྒོ་བ་ནི་མཁའ་འགྲོ་མས་ནམ་མཁའ་ནས་བསྟན་པའོ། །ཇི་ལྟར་བསྒོ་ཞེ་ན། ཕྱག་རྒྱ་ཆེ་གེ་མོ་ཞིག་ནི་ཞིང་དང་ཞིང་སྐྱེས་མའི་མིང་ངོ་། །ཁྱེར་ལ་ཞེས་པ་ནི་དགོན་པའི་གནས་སུ་སྟེ་གསང་བའི་སྤྱོད་པའོ། །

[Block 2239]
སེམས་ཅན་དོན་གྱིས་ཞེས་པ་ནི་གྲོང་ཁྱེར་དག་ཏུ་འཁྱམས་པའམ་མོས་པར་འགྱུར་བའོ། །

[Block 2240]
རྡོ་རྗེ་འཛིན་ནི་རྣལ་འབྱོར་པ་ལ་བོས་པའོ། །

[Block 2241]
དགྱེས་པའི་རྡོ་རྗེའི་ང་རྒྱལ་གྱིས། །ཞེས་བྱ་བའི༌[^972]ཐ་ཚིག་གོ། །

[Block 2242]
འོ་ན་སྤྱོད་པ་ནི་སྒོ་གསུམ་གྱི་བདག་ཉིད་ཅན་ཡིན་ལ། གསང་བའི་སྤྱོད་པ་ནི་གྲོགས་དང་བཅས་པ་ཡིན་པས་བརྟན་པ་འཐོབ༌[^973]ན་གང་དང་འགྲོགས་ཤེ་ན། སྤྱོད་པའི་སྒོ་གསུམ་ནི་ལེའུ་དྲུག་པ་ལྟར་ཤེས་པར་བྱའོ། །

[Block 2243]
གསལ་བའི་སྤྱོད་པའི་གྲོགས་ནི་གཉིས་ཏེ་ཞིང་སྐྱེས་མ་དང་ལྷན་སྐྱེས་མའོ། །

[Block 2244]
བརྟན་པ་མ་ཐོབ་ཀྱི་བར་དུ་ལྷན་སྐྱེས་མ་དང་འགྲོགས་ཏེ་སྤྱོད་པའོ། །

[Block 2245]
ལྷན་སྐྱེས་མའི༌[^974]དེ་ཉིད་བསྟན་པའི་ཕྱིར། རྙེད་པ་དེ་ཡང་མིག་ཡངས་མ། །ཞེས་བྱ་བ་ལ་སོགས་པ་ཚིགས་སུ་བཅད་པ་གཉིས་ཏེ། རང་བཞིན་གྱི་ཡོན་ཏན་དང་སྦྱངས་པའི་ཡོན་ཏན་དང་ལྡན་པ་སྟེ། རང་བཞིན་གྱི་ཡོན་ཏན་ནི་བྱད་གཟུགས་དང་ལང་ཚོ་དང་རིགས་ཀྱི་ཡོན་ཏན་ནོ། །
--- END BLOCKS ---
