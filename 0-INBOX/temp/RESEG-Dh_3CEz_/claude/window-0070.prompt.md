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
[Block 2451]
བཟློག་པའི་སྒོམ་པ་ཉིད་ནི་མཚོན་པ་སྟེ། སྒོམ་པ་དང་སྤྱོད་པ་ལ་བརྗོད་དུ་ཟིན་ཀྱང་ལྟ་བ་དང་འབྲས་བུ་ལ་ཡང་ངོ་། །ད་ནི་འབྲས་བུ་བསྟན་པའི་ཕྱིར། ཀུན་དུ་རུ་ལས་ཞེས་པ་སྟེ། དགའ་བ་ཆེན་པོ་གཅིག་ཉིད་ནི་ཞུ་བ་ཞེས་པའོ། །

[Block 2452]
ཚིགས་སུ་བཅད་པ་གཅིག་སྟེ་གོ་སླའོ། །

[Block 2453]
དེའི་བཤད་པ་ཡང་ཚིགས་སུ་བཅད་པ་ལྔ་སྟེ་གོ་སླའོ། །

[Block 2454]
ལུས་ལྷན་ཅིག་སྐྱེས་པའི་འབྲས་བུར་བསྟན་ནས་སེམས་བསྟན་པའི་ཕྱིར།[^1064] སེམས་ནི་ཆེན་པོ་ཉིད་ནི་སྔར་གྱི་དགའ་བ་ཆེན་པོ་སྟེ།

[Block 2455 [VERSE]]
དེ་ནས་བདེ་ཆེན་མཆོག་ཏུ་ཡང་འབྲེལ་ལོ། །
འདོད་ཆགས་ལ་སོགས་སེམས་ལྔ༌[^1065]ནི༌[^1066]ཉོན་མོངས་པའི་གནས་སྐབས་སོ། །
དབྱེ་བ་ནི་ཆེ་ལོང་དུ་དབྱེ་བས་སོ། །

[Block 2456]
ལྔ་རུ་འགྲོ་བ་ནི་ཡེ་ཤེས་ལྔར་འགྲོ་བ་དང་། དེས་རིགས་ལྔར་ཡང་འགྱུར་བའོ། །

[Block 2457]
དེ་དག་ཅིས་ཤེ་ན།

[Block 2458 [VERSE]]
དེ་ནས་ལྔའི་གཟུགས་སུ་འབྲེལ་ལོ། །
ལྔའི་གཟུགས་ཀྱིས་ནི་འབྱུང་བ་ལྔའོ། །

[Block 2459]
རྣམ་པར་མཚོན་ནས་བརྟགས་ནི་སེམས་ལ་ཡང་ངོ་། །རིགས་ནི་ལྔའོ། །

[Block 2460]
དེ་ཉིད་ལས་འབྱུང་བ་ལྔ་དང་ཡེ་ཤེས་ལྔ་ལས་གྱུར་པའོ། །

[Block 2461]
དེ་དག་ལས་དབྱེ་བ་ནི་དེའི་ཕྱིར་རང་བཞིན་ནི་དེ་བཞིན་གཤེགས་པའི་རིགས་སུ་འབྲེལ་ལོ། །

[Block 2462]
དེ་ལས་དུ་མ་ནི་རིགས༌[^1067]རྣམ་པ་བརྒྱ་ཞེས་པའོ། །

[Block 2463]
ད་ལ་སྟོང་ཕྲག་ཏུ་མ་སྐྱེས་ཞེས་པ་ནི་དེ་ལས་ཁྲིར་འགྱུར་བ་ནི་ལྷག་མའོ། །

[Block 2464 [VERSE]]
དེ་ལས་འབུམ་ཕྲག་རིགས་ཆེན་ནི་ཞེས་པའོ། །
དེ་ལ་དབྱེ་བའི་རིགས་ཞེས་པའོ། །

[Block 2465]
དེ་གཞན་དག་ནི་ལྷག་མའོ། །

[Block 2466 [VERSE]]
དེ་ལས་གང་གཱ་ཀླུང་བཅུའི་བྱེ་མ་ཞེས་པའོ། །
དེ་ལས་རིགས་ནི་གྲངས་མེད་དོ་ཞེས་པའོ། །

[Block 2467]
དེ་ལྟར་ན་དེ་ཀུན་ཀྱང་མཆོག་ཏུ་དགའ་བ་སྟེ་ལྷན་ཅིག་སྐྱེས་པ་ཉིད་དབྱེར་མེད་པའོ། །

[Block 2468 [VERSE]]
རིགས་ལས་བྱུང་ནི་སྒྱུའམ་རང་བཞིན་ནོ། །
དགྱེས་པའི་རྡོ་རྗེ་ནི་རྒྱུད་སྤྱིའམ་ཧེ་རུ་ཀའོ། །
མཁའ་འགྲོ་མ་ནི་བདག་མེད་མ་ལ་སོགས་པའོ། །

[Block 2469]
དྲ་བ་ནི་དེ་དག་གིས་ཞུས་པའམ་དེ་དག་གི་དོན་དུ་གསུངས་པར་འབྲེལ་བའོ།[^1068] །སྡོམ་པ་ནི་སྙོམས་འཇུག་གམ་བདེ་མཆོག་སྡོམ་པའོ། །

[Block 2470]
དངོས་གྲུབ་གཏན་ལ་འབེབས་པ་ནི་ལམ་གཉིས་ཀྱིས༌[^1069]ཇི་ལྟར་མཐོང་བའམ་དབྱེར་མེད་ཕྱག་རྒྱ་ཆེན་པོ་གཏན་ལ་དབབ་པའོ། །

[Block 2471]
བརྟག་པ་གཉིས་པའི་ལེའུ་གཉིས་པའོ།། །།

[Block 2472 [HEADING]]
### ལེའུ་གསུམ་པ། ^2-3-0

[Block 2473]
དེ་ནས་ནི༌[^1070]དེའི་རྗེས་སུའོ། །

[Block 2474]
རྡོ་རྗེ་ཅན་ནི་ཧེ་རུ་ཀའོ། །

[Block 2475 [VERSE]]
རྣལ་འབྱོར་མ་རྣམས་ནི་བདག་མེད་མ་ལ་སོགས་པའོ། །
རྒྱུད་ཀུན་གྱི་གླེང་གཞི་ནི་ཨེ་ཝཾ་མོ། །

[Block 2476]
ཐབས་ནི་དབང་ལ་སོགས་པའོ། །

[Block 2477]
བཀའ་སྩལ་པ་ནི་མ་ཞུས་པར་གནང་བ་སྦྱིན་པའོ། །

[Block 2478 [VERSE]]
དེ་ཡང་གླེང་གཞི་ནི་ཅི་ཞེ་ན།
སྡོམ་པ་དང་ཞེས་པ་སྟེ་བདེ་མཆོག་གོ། །
དེའི་གནས་ཨེ་ཝཾ་སྟེ་གླེང་གཞིའོ། །

[Block 2479]
དབང་ལ་སོགས་པ་ནི་ཐབས་ཏེ་གོང་མའི་བཀའ་སྩལ་པ་དང་འབྲེལ་ཏོ།[^1071] །ལེའུ་འདིས་ནི་ལེའུ་དང་པོའི་གླེང་གཞི་གཏན་ལ་འབེབས་ཏེ། ཆོས་ཐམས་ཅད་དགྱེས་པའི་རྡོ་རྗེར་སྟོན་ལ་དེ༌[^1072]ཡང་བརྟག་པ་དང་པོར་བསྡུས་ཏེ། དེ་ཡང་རྡོ་རྗེ་རིགས་ཀྱི་ལེའུ་མདོ་རུ་བསྡུས་ཏེ། དེ་ཡང་གླེང་གཞིའི་ཡི་གེ་སུམ་ཅུ་རྩ་བདུན་ནམ་ཡི་གེ་བཞི་བཅུར་བསྡུས། དེ་ཡང་ཡི་གེ་བཞི་དང་ཨེ་ཝཾ་ཡི་གེ་གཉིས་སུ་བསྡུས་ཏེ་བསྟན་པ་དེ་ཤེས་པར་བྱེད་དེ། སྡོམ་པ་ནི་ཨེ་ཝཾ་སྟེ་ཆོས་ཐམས་ཅད་ཐབས་དང་ཤེས་རབ་དང་ལྷན་ཅིག་སྐྱེས་པའི་ཡེ་ཤེས་སུ་སྡོམ་ལ། གང་གིས་སྡོམ་ན་མ༌[^1073]ཡཱ་སྟེ་དབང་རྣམ་པ་བཞིའི་ཚུལ་གྱིས་སྡོམ་སྟེ། ཨཱཏྨ་སྟེ་རྟོགས་པར་བྱེད་དོ།[^1074] །སྲུ་ཏ་སྟེ་དགོངས་པའི་སྐད་ཀྱིས་ཏེ། ངག་བརྡ་དང་ལུས་བརྡ་ཨེ་ཀ་སྨིན་ས་མ་ཡ་སྟེ། སྐད་ཅིག་མ་དང་དགའ་བ་བཞིའི་རྟོག་པ་སྐྱེ་ལ། ས་མ་ཡ་སྟེ་དེ་དག་གི་དུས་སུ་བཟའ་བ་ཚོགས་ཀྱི་འཁོར་ལོ་དང་། མཆོད་པ་དང་བྱ་བའི་རིམ་པ་རྣམས་ལག་ལེན་དུ་འབྲེལ་ལོ། །

[Block 2480]
བསྟན་པ་དེ་བཤད་པའི་ཕྱིར་སྡོམ་པ་བཀའ་སྩལ་ཞེས་པ་ནི་རྟེན་དང་བཅས་པའོ། །

[Block 2481]
དེ་ཡང་སངས་རྒྱས་ཀུན་གྱི་སྡོམ་པ་ནི་རྣམ་པར་སྣང་མཛད་ལ་སོགས་པའི་སྡོམ་པའོ། །

[Block 2482]
ཨེ་ཝཾ་ཡི་གེར་རབ་ཏུ་གནས་ནི་ལས་ཀྱི་ཕྱག་རྒྱ་དང་བཅས་པའི་གསང་བའི་གནས་སོ། །

[Block 2483]
ཨེ་ཝཾ་རྣམ་པའི་ཚུལ་གཅིག་ནི་བདེ་ཆེན་ཉི་ཟླ་འདྲེས་པའི་བདེ་ཆེན་ནོ། །

[Block 2484]
དེ་ནི་གཞན་ལུས་ལ་བརྟེན་པའོ། །

[Block 2485]
ཡང་ཨེ་ཝཾ་ནི་སྐྱེ་གནས་དང་སྤྱི་བོ་སྟེ་རྟེན་ནོ། །

[Block 2486]
བདེ་ཆེན་ནི་རྒྱུན་མི་འཆད་པར་ཞུ་བ་དང་བཅས་པ་སྟེ་བརྟེན་པའོ། །

[Block 2487]
དེ་ནི་རང་ལུས་ཐབས་སོ། །

[Block 2488]
ཡང་ཨེ་ཝཾ་ཡི་གེར༌[^1075]རབ་ཏུ་གནས་ནི་ནམ་མཁའི་དཀྱིལ་དུ་ཟུག་པའི་ཕྱག་རྒྱ་ཆེན་པོ་སྟེ་རྟེན་ནོ། །

[Block 2489]
བདེ་ཆེན་ནི་ལྷན་ཅིག་པ་འབའ་ཞིག་སྟེ་བརྟེན་པའོ། །

[Block 2490]
དེ་དག་ནི་སྡོམ་པ་བཤད་ནས་ཐབས་བསྟན་པའི་ཕྱིར། དབང་ལས་ཡང་དག་ཤེས་པ་ནི་དགོངས་པའི་སྐད་ལ་སོགས་པ་ཡང་མཚོན་སྟེ་ཡང་དག་ཤེས་པའོ། །
--- END BLOCKS ---
