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
[Block 2521]
ཨ་བྷི་ཥེ་ཀ་སྟེ་ཆོས་ཀྱི་སྐུའི་ནུས་པ་འཇོག་པར་བྱེད་པས་དབང་ཞེས་བྱའོ། །

[Block 2522 [VERSE]]
གནས་གང་དུ་བསྐུར་ན་གསང་བའི་གནས་སུ་བསྐུར་རོ། །
བསྐུར་བའི་རྫས་ནི་ཕྱག་རྒྱ་མ༌[^1093]མཚན་དང་ལྡན་པའོ། །

[Block 2523]
དབང་བཞི་པ་ནི་དེ་ལྟར་དེ་བཞིན་ཡང་བཞི་པ་ཞེས་པ་ནི་གསུམ་པས་གོ་ཕྱེ་བའི་ཚིག་དབང་རིན་པོ་ཆེ་སྟེ། ཨ་བྷི་ཥིཉྩ་སྟེ་ལུས་དག་ཡིད་གསུམ་གྱི་བག་ལ་ཉལ་གྱི་དྲི་མ་འཁྲུད་པར་བྱེད་དོ། །

[Block 2524]
ཨ་བྷི་ཥེ་ཀ་སྟེ་བདེ་བ་ཆེན་པོའི་སྐུའི་ནུས་པ་འཇོག་པར་བྱེད་དོ། །

[Block 2525]
བསྐུར་བའི་གནས་ནི་ལུས་ངག་ཡིད་གསུམ་ཆར་ལའོ། །

[Block 2526]
བསྐུར་པའི་རྫས་ནི་སློབ་དཔོན་ལ་ལ་དག་ནི་རྟེན་ཅན་དུ་ཡང་འདོད་དོ། །

[Block 2527 [VERSE]]
བླ་མའི་གཞུང་གིས་ནི་རྫས་མི་འདོད་དོ། །
དང་པོས་ནི་རྡོ་རྗེ་འཆང་གི་རིགས་སུ་བྱེད་དོ། །
གཉིས་པས་ནི་རྡོ་རྗེ་འཆང་གི་སྲས་སུ་བྱེད་དོ། །

[Block 2528]
གསུམ་པས་ནི་རྡོ་རྗེ་འཆང་གི་གོ་འཕང་ལ་འགོད་དོ། །

[Block 2529]
བཞི་པས་ནི་རྡོ་རྗེ་འཆང་གི་ངོ་བོར་བྱས་ཏེ་གཞན་དོན་ཡོངས་སུ་རྫོགས་པའི་གོ་འཕང་ལ་འགོད་དོ། །

[Block 2530]
ད་ནི་དེ་དག་གི་ཆོ་གའི་རིམ་པ་ནི་ཤེས་རབ་བཅུ་དྲུག་ལ་སོགས་པས་དབང་བསྐུར་གྱི་རིམ་པ་ཡང་བླ་མ་ལ་རག་ལས་པར་བྱ་བའི་ཕྱིར། ཇི་ལྟར་དབང་བསྐུར་དུ་འབྲེལ་ཏོ། །

[Block 2531]
དེ་ནས་སློབ་མའི་བྱ་བ་བཤད་ཅེས་པ་ནི་ཚིག་བཤད་བསྒྱུར་བའོ། །

[Block 2532]
བླ་མ་ཕྱག་རྒྱ་ལྡན་མཐོང་ཞེས་པ་ནི་རང་གི་ཕྱག་རྒྱ་ཕུལ་བ་དང་བཅས་པ་ལའོ། །

[Block 2533]
དེ་ནས། མཆོད་བསྟོད་གསོལ་གདབ་ཇི་བཞིན་བྱ། །ཞེས་འབྲེལ་བའོ། །

[Block 2534]
[^1094]ཡང་མཆོད་པ་དེ་ནས་ཞིམ་པའི་བཟའ་བར་འབྲེལ་ཏེ་རྐང་པ་དྲུག་ནི་གོ་སླའོ། །

[Block 2535]
དེ་ནས་བསྟོད་པ་ནི་ཀྱེ་བཅོམ་ལྡན་འདས་སུ་འབྲེལ་ཏེ་ཚིགས་སུ་བཅད་པ་གཅིག་གོ། །

[Block 2536]
གསོལ་བ་བཏབ་པའི་ཡང་ཚིགས་སུ་བཅད་པ་གཅིག་གོ། །

[Block 2537]
ད་ནི་སློབ་དཔོན་གྱི་ལས་བསྟན་པའི་ཕྱིར་སློབ་དཔོན་གྱི་དབང་ནི་ཁྱད་པར་དུ་གྱུར་པ་སྟེ་གོ་སླའོ། །

[Block 2538]
དེ་ནས་གསང་བའི་དབང་བསྟན་པའི་ཕྱིར། ཤིན་ཏུ་བཞིན་བཟང༌[^1095]མིག་ཡངས་མ། །

[Block 2539 [VERSE]]
རྐང་པ་གཉིས་ཀྱིས་རྗེས་ལ་སྟོན་པ་ནི་བླ་མའོ། །
ཤེས་རབ་ནི་དེ་མ་ཐག་གི་ཕྱག་རྒྱའོ། །
རབ་ཏུ་མཆོག་ནི་ཐ་མལ་དུ་མ་ཡིན་པའོ། །
དེ་ནས་མཐེ་བོང་སྲིན་ལག་ཏུ་འབྲེལ་ཏེ།

[Block 2540 [VERSE]]
ལས་དང་པོ་པའི་དབང་བསྐུར་ཐབས་སོ། །
སློབ་མའི་ཁ་ནི་ལོངས་སྤྱོད་ཀྱི་གནས་སུའོ། །

[Block 2541]
དབང་པའམ་ལྟུང་བ་ནི་རྡོ་རྗེ་འཆང་གི་རིགས་དང་བཅས་པའོ། །

[Block 2542]
ད་ནི་གསུམ་པ་བསྟན་པའི་ཕྱིར། དེ་ནས་དེ་ཉིད་དུ་ནི་ཞེས་པའི་ཚིག་རྐང་གཉིས་བསྟན་པའོ། །

[Block 2543]
བཤད་པའི་ཕྱིར་ཕྲག་དོག་ཁྲོ་བ་འབྲེལ་ཏེ་སློབ་མ་མཚན་ཉིད་དང་ལྡན་པར་ཤེས་པར་བྱའོ། །

[Block 2544]
སྟོན་པས་གནང་བ་སྦྱིན་པ་ནི་མན་ངག་བཤད་པ་དང་བཅས་པར་རོ། །

[Block 2545]
ཀུན་དུ་རུ་ནི་ལྷན་ཅིག་སྐྱེས་པ་ལ་སྦྱོར་ཏེ།[^1096] དེ་ནས་མཆོག་ཏུ་དགའ་བར་འབྲེལ་ཏེ། མཆོག་ཏུ་དགའ་བ་ཡང་དག་འཐོབ་ནི་ལྷན་སྐྱེས་སོ། །

[Block 2546]
ཡང་ན་མཆོག་ཀྱང་ཡིན་ལ་ཡང་དག་ཐོབ་ཀྱང་ཡིན་པས་ལྷན་སྐྱེས་སོ། །

[Block 2547]
རིམ་པ་གང་དུ་འཐོབ་ཅེ་ན་སྣ་ཚོགས་སྤངས་པའི་སྐད་ཅིག་ནི་སྣ་ཚོགས་པ་ལ་སོགས་པ་སྟེ།

[Block 2548 [VERSE]]
དགའ་བྲལ་གྱི་སྔོན་དུ་འཐོབ་པའོ། །
ཡང་ན་སྣ་ཚོགས་སྤངས་པའི་དགའ་བའོ། །

[Block 2549 [VERSE]]
སྐད་ཅིག་མ་རྣམ་པར་སྨིན་པ་སྟེ་མཆོག་དགའོ། །
དེ་ཡང་སྤངས་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །
དེ་ནས་ཡང་དག་ཐོབ་ནི་ལྷན་སྐྱེས་སོ། །

[Block 2550]
དེའི་ཐབས་བསྟན་པའི་ཕྱིར་གོང་གི་རྡོ་རྗེ་འཛིན་ནས་དེ་བཤད་པའི་ཕྱིར་སྟོན་པས་སྨྲས་པ་སེམས་དཔའ་ཆེན་པོ་འབྲེལ་ཏོ། །

[Block 2551]
དེས་འདི་སྐད་སྟོན་ཏེ་སྟོན་པས་སྨྲས་པ་ནི་མན་ངག་སྔོན་དུ་བཤད་པ་སྟེ། ཟླ་བ་འཛིན་པའི་མན་ངག་གིས་རྡོ་རྗེ་འཛིན་པ་དང་འདྲ་བར་གྲུབ་པའོ། །

[Block 2552]
དེའི་ཕྱིར་སེམས་དཔའ་ཆེན་པོ་ནི་གསོལ་བ་འདེབས་པའི་སློབ་མ་ལ་བོད་པའོ། །

[Block 2553 [VERSE]]
བདེ་བ་ཆེན་པོ་བཟུང་ནི་ཞུ་བའི་ཟླ་བའོ། །
ཇི་སྲིད་བྱང་ཆུབ་མ་འཐོབ་བར་དུའོ། །
སེམས་ཅན་དོན་གྱི་ནུས་པ་དང་ལྡན་པའོ། །

[Block 2554]
རྡོ་རྗེ་འཛིན་གྱིས་ཞུ་བ་དེ་དང་མི་འབྲལ་བས་ཡོན་ཏན་གྱི་མིང་ངོ་། །དེ་ནས་གོང་གི༌[^1097]བརྗོད་ནས་བཏད་པར་འབྲེལ་ཏེ། བརྗོད་པར་བྱས་པ་ཞེས་པ་ནི་དེ་མ་ཐག་གི་མན་ངག་གོ། །

[Block 2555]
གཏད་པ་ནི་ལག་ཏུའོ། །

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
--- END BLOCKS ---
