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
[Block 2381]
བདེ་བ་ཅན་ནི་ཞུ་བ་དེའོ། །

[Block 2382 [VERSE]]
རྟག་ཏུ་ཞུགས༌[^1034]སམ་གནས་པ་ནི་བྱོན་ཏེ་གནས་པའོ། །
དེ་ནི་རང་ལུས་ཐབས་ལ་བརྟེན་པའོ། །

[Block 2383]
ཡང་རྡོ་རྗེ་བཙུན་མོ་ཤེས་རབ་ལྷ་མོ་བླ་ན་མེད་པའོ། །

[Block 2384]
བྷ་གར་ནི་གནས་བཟང་པོ་དེར་འཇུག་པ་དང་ལྡོག་པའོ། །

[Block 2385 [VERSE]]
ཨེའི་རྣམ་པ་ནི་སའི་དཀྱིལ་དུ་ཟུག་པའོ། །
སངས་རྒྱས་རིན་ཆེན་ནི་ནམ་མཁའི་དཀྱིལ་དུ་ཟུག་པའོ། །

[Block 2386]
ཟ་མ་ཏོག་ནི་གོང་དང་འདྲའོ། །

[Block 2387]
བདེ་བ་ཅན་ནི་གཉུག་མའི་དབང་པོ་ཞུ་བ་དང་བཅས་པའོ། །

[Block 2388]
རྟག་ཏུ་ཞུགས་སམ་གནས་པ་ནི་ཡེ་ཤེས་ཆེན་པོ་འབའ་ཞིག་གོ། །

[Block 2389 [VERSE]]
དེ་དག་ནི་གཉིས་སུ་མེད་པའི༌[^1035]ཕྱག་རྒྱ་ཆེན་པོའོ། །
དེ་བཤད་པའི་ཕྱིར་བཙུན་མོའི་བྷ་གར་འབྲེལ་ལོ། །
དེ་ཚིགས་སུ་བཅད་པ་གཅིག་སྟེ་གོ་སླའོ། །

[Block 2390]
དེའི་ཚེ་ཆེ་བ༌[^1036]བསྟན་པ་ནི་འཆད་པ༌[^1037]པོ་ང་ནི་ཞུ་བ་སྟོན་པ་ཡིན་པས་སོ། །

[Block 2391]
ཆོས་ང༌[^1038]ནི༌[^1039]བདེ་བ་སྟོན་པས་སོ། །

[Block 2392 [VERSE]]
ཉན་པ་ང་ནི་རྟོག་པ་གསལ་བ༌[^1040]འབྱུང་བའོ། །
འཇིག་རྟེན་པ་ནི་ལུས་ལ་གནས་པའོ། །
བསྒྲུབ་བྱ་ང་ནི་སེམས་པ་ལ་གནས་པའོ། །
འཇིག་རྟེན་ང་ནི་ཀུན་རྫོབ་ལྷན་སྐྱེས་སོ། །

[Block 2393 [VERSE]]
འཇིག་རྟེན་འདས་པ་ང་ནི་དོན་དམ་ལྷན་སྐྱེས་སོ། །
གོ་རིམས་ཟློག༌[^1041]སྟེ་ངའི་རང་བཞིན་ཅི་ཞེ་ན།

[Block 2394 [VERSE]]
ལྷན་ཅིག་སྐྱེས་དགའ་ཞེས་པའོ། །
དེ་ཇི་ལྟར་ཤེས་པར་བྱ་ཞེ་ན། །

[Block 2395]
མཆོག་དགའ་དགའ་བྲལ་དང་པོ་ནི་གསུམ་པའམ་ཁྱད་པར་ཏེ་ཀུན་རྫོབ་དང་དོན་དམ་མོ། །

[Block 2396]
དེའི་དཔེ་ཡང་བདུན་པ་ནི་གོ་རིམས་དང་ཁྱད་པར་མ་ཤེས་པའོ། །

[Block 2397]
མར་མེ་ལྟར་ནི་གསུམ་གྱི་བར་དུ་མཚོན་པའམ་གསུམ་ལ་ཁྱད་པར་མཚོན་པའོ། །

[Block 2398]
དེ་ལྟ་མོད༌[^1042]ཀྱིའམ་དེ་བཞིན་དུ་ནི་ལྷན་སྐྱེས་ལ་མཚོན་དུ་མེད་ཀྱིའམ། དཔེ་དང་མཐུན་པར་རོ། །

[Block 2399]
བུ་ནི་རྡོ་རྗེ་སྙིང་པོ་སྟེ་རྟོགས་པར་འདོད་པ་ཀུན་ནོ། །

[Block 2400]
ཡིད་ཅེས་ནི་པྲ་ཏ་ཡ་སྟེ། རྐྱེན་ནམ་མངོན་དུ་བྱེད་པའོ། །

[Block 2401]
ད་ནི་དེ་དག་སྔར་གྱི་དྲིས་པའི་ལན་དུ་བསྡུས་པའི་ཕྱིར་རོ། །

[Block 2402]
དེ་མེད་པས་ནི༌[^1043]འབྲེལ་ཏེ།

[Block 2403 [VERSE]]
དེ་མེད་པའམ་མ་རྟོགས་པ་ནི་ལུས་སོ། །
བདེ་མེད་འགྱུར་ནི་ཞུ་བ་དེའོ། །
དེ་མེད་ན་ཞུ་བདེ་མེད་ནའོ། །
དེ་ཡོད་མིན་ནི་མི་རྟོག་པ་གསལ་བའོ། །

[Block 2404]
ཅིའི་ཕྱིར་ཞེ་ན།

[Block 2405 [VERSE]]
ནུས་པ་མེད་ཕྱིར་ཞེས་པ་ནི༌[^1044]ཀུན་ཤེས་པའོ། །
ལྟོས༌[^1045]དང་བཅས་ནི་བརྟེན་པ་དག་ལའོ། །

[Block 2406]
འོ་ན་ལས༌[^1046]ཀྱིས་ཆོག་མོད་ལྷ་བསྐྱེད་པ་ཅི་དགོས་ཤེ་ན། དེའི་ཕྱིར་ལྷའི་རྣལ་འབྱོར་ལས་ཞེས་པ༌[^1047]ནི་ལྷ་རུ་བྱས་པ་ལས་སོ། །

[Block 2407 [VERSE]]
དེ་ནས་དེ་ཉིད་དུ་འབྲེལ་ཏེ་དེའི་ཕྱིར་རོ། །
དངོས་མེད་ཚུལ་མིན་ལུས་ལྷར༌[^1048]བྱས་པའི་ཕྱིར་རོ། །

[Block 2408]
དེ་ནས་བདེ་བར་འབྲེལ་ཏེ་དེ་བས་སམ་དེའི་ཕྱིར་ན་སེམས་ཀྱི་ཆོས་བདེ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2409]
སངས་རྒྱས་ནི་རྟོགས་པའོ། །

[Block 2410 [VERSE]]
དངོས་པོ་མིན་ནི་བེམས་པོའོ། །
དེས་ནི་འདི་སྐད་བསྟན་ཏོ། །

[Block 2411]
ལུས་དང་ལྷ་དང་བདེ་བ་མི་རྟོག་གསལ་ལ༌[^1049]དབྱེར་མེད་བསྟན་ཏོ། །

[Block 2412]
དེ་བསྟན་པའི་ཕྱིར་ཞལ་ཕྱག་རྣམ་པའི་གཟུགས་ནི་གཟུགས་ཐ་མལ་པར༌[^1050]བསྒྱུར་བའོ། །

[Block 2413]
དེ་ནས་ལྷའི་རྣམ་པར་འབྲེལ་ཏེ།

[Block 2414 [VERSE]]
དེའི་གཟུགས་ནི་ཇི་ལྟར་འགྱུར་བའོ། །
བཞིན་ལག་ཁ་དོག་ནི་འདི་ལྟར་གནས་པའོ། །

[Block 2415]
འོ་ན་བསྐྱེད་མི་དགོས་པས་བསྐྱེད་རིམ་མ་ཡིན་ནོ་ཞེ་ན་དེའི་ཕྱིར་བསྐྱེད་ཙམ་ཉིད་ན་ཞེས་བྱ་བ་ནི་ལུས་ལྷར་བྱས་པ་ཙམ་མོ། །

[Block 2416]
ཡང་གནས་ནི་དེ་ཡང་ལུས་རྫོགས་པའི་རིམ་པའོ། །

[Block 2417]
དེ་ནས་མཆོག་ཏུ་བདེ་བར་འབྲེལ་ཏེ་གཟུགས་མེད་པ་ནི་སེམས་སོ། །

[Block 2418 [VERSE]]
དེའི་ཕྱིར་ནི༌[^1051]ཆོས་ཉིད་བདེ་བ་ཡིན་པས་སོ། །
འགྲོ་ཀུན་ནི་སེམས་ཅན་ཀུན་ནོ། །

[Block 2419 [VERSE]]
ལྷན་ཅིག་སྐྱེས་པ་ནི་དབྱེར་མེད་པའི་བདེ་བའོ། །
དེའི་ཕྱིར་རང་བཞིན་ལྷན་ཅིག་སྐྱེས་པར་བརྗོད་དོ། །

[Block 2420]
རྣམ་དག་སེམས་ནི་དགའ༌[^1052]བའོ། །
--- END BLOCKS ---
