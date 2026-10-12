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
[Block 106]
འདི་ནི་དགུག་པའི་བདག་ཉིད་མཆོག །ཅེས་བྱ་བ་ནི་ཕུང་པོ་ལྔ་དང་འབྱུང་བ་བཞིའི་བདག་ཉིད་དེ། [^43]དེ་ལྟ་བུའི་ཐིག་སྐུད་ཀྱིས་ལུས་ཀྱི་དཀྱིལ་འཁོར་རྣམས་ཀྱི་གནས་ཇི་ལྟ་བ་བཞིན་དུ་ཡང་དག་པར་བལྟ་བར་བྱའོ།།

[Block 107]
རྣམ་པ་ལྔའི་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་ཡེ་ཤེས་ལྔ་རྣམས་ཀྱི་རང་བཞིན་གྱིས་མི་བསྐྱོད་པ་ལ་སོགས་པ་དབུས་ལ་སོགས་པར་བཀོད་པ༌[^44]ཡིན་པར་སྟོན་ནོ།།

[Block 108]
དབྱིབས་ཀྱི་མཆོད་པ་ཞེས་པ་དང་། རྣམ་པ་གསུམ་ཞེས་པ་ནི་འཇུག་པ་དང་ལྡང་བ་དང་། གནས་པའི་རིམ་གྱིས་སོ།།

[Block 109]
སྐད་ཅིག་ཅེས་བྱ་བ་ལ་སོགས་པ་ནི་སྣང་བ་རྣམས་ཀྱི་རང་བཞིན་གྱི་སྐད་ཅིག་གི་དུས་ལས་སྟོང་པ་བཅུ་དྲུག་ཏུ་ཕྱེ་བའོ།།

[Block 110]
ཞི་བའི་ཆོས་ནི་ཤིན་ཏུ་ཕྲ་བའི་ཁམས་སེམས་ཅན་གྱི་ཡོངས་སུ་ཤེས་པར་བྱས་པ༌[^45]རྣམ་པར་ཤེས་པའི་རང་བཞིན་སྙིང་རྗེ་ཆེན་པོའི་བདག་ཉིད་དེ་ཞི་བར་ངེས་པར་སྦྱངས་པའོ།།

[Block 111]
མདངས་བཟངས༌[^46]འོད་ནི་ཡིན་པར་གསུངས།།

[Block 112]
ཞེས་པ་ནི་དེ་དག་ཉིད་ལ་བྱ་བར་གསུངས་སོ།།

[Block 113]
རྟེན་འབྲེལ་ཞེས་པ་ནི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་རྣམས་སོ།།

[Block 114]
དྲི་ནི་ལུས་ལ་བྱའོ།།

[Block 115]
སྒྲོན་མ་གསལ་བར་བྱེད་པའི་ལེའུ་བཞི་པའི་དཀའ་བ་བཏུས་པའི་བཤད་པའོ།།།།

[Block 116 [HEADING]]
## ལེའུ་ལྔ་པ། ^5-0

[Block 117]
དེ་ཞི་གནས་ལས་བྱུང་ཞེས་བྱ་བ་ཟུང་དུ་འཇུག་པར་གྱུར་པ་ལས་བྱུང་བའོ།།

[Block 118]
མ་དང་སྲིང་མོ་བུ་མོ་ཞེས་བྱ་བ་ནི་མ་དང་སྲིང་མོ་ལྟར་རྗེས་སུ་ཕན་པར་འདོད་མའོ།།

[Block 119]
སྙིང་ལ་གནས་པའི་ལྷ་མོ་ཆེ།།ཞེས་བྱ་བ་ནི་ནང་གི་ཕྱག་རྒྱ་ཆེན་པོའོ།།

[Block 120]
[^47]མཉེས་པར་བྱས་ཀྱང་ཞེས་བྱ་བ་ནི་ཕྱི་རོལ་གྱི་ཕྱག་རྒྱ་ལའོ།།

[Block 121]
གནས་པའི་ཞེས་བྱ་བ་ནི་གང་འགོག་པའི་ཏིང་ངེ་འཛིན་ལ་གནས་པའི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་འགོག་པའི་ཏིང་ངེ་འཛིན་ལ་གནས་པ་དེའི་ཚེ་རང་གི་ཁམས་ཕྲ་མོའི་འོད་ཟེར་རྣམ་པར་ཤེས་པ་ལ་རེག་པས་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ལ་ངེས༌[^48]པར་གྱུར་ནས་ཟུང་འཇུག་ཏུ་གནས་པ་ལ་བྱའོ།།

[Block 122]
སྒྲོན་མ་གསལ་བར་བྱེད་པའི་ལེའུ་ལྔ་པའི་དཀའ་བ་བཏུས་པའི་བཤད་པའོ།།།།

[Block 123 [HEADING]]
## ལེའུ་དྲུག་པ། ^6-0

[Block 124]
སྔགས་བསྟན་པས་ཞེས་བྱ་བ་ནི་མདོ་ཙམ་དུ་བསྟན་པར་བྱས་པའོ།།

[Block 125]
ཡང་དེ་གསལ་བར་བྱེད་པ༌[^49]གསུངས་པ། རྡོ་རྗེ་གསུམ་པོ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། རྡོ་རྗེ་གསུམ་ནི་རང་གི་ལུས་ལ་སྡུད་པ་དང་། གཞན་གྱི་སྐུ་ལ་སྤྲོས་པས་མཉེས་པར་བྱེད་པའི་བཀོད་པ་རྣམ་པ་གསུམ༌[^50]སྟེ། དེ་རྣམས་ཀྱིས་དེ་བཞིན་གཤེགས་པ་རྣམས་ལ་མཚན་པའོ།།

[Block 126]
དེ་དག་ཉིད་ཀྱང་དེ་བཞིན་གཤེགས་པའོ།།

[Block 127]
ཨོཾ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་དང་པོར་ནི་སྐུ་གཅིག་ཡིན་ནོ།།

[Block 128]
ཡོན་ཏན་གསུམ་ནི་དེ་བཞིན་གཤེགས་པ་གསུམ་སྟེ་ཐུགས་རྡོ་རྗེ་དང་མི་གཉིས་པར་ལྡན་པའོ།།

[Block 129]
དེ་ལྟར་གསུངས་པའང་རིགས་དྲུག་གི་བདག་ཉིད་ཅན་གྱི་སྟེ། དེ་ལྟར་སྦྱར་བར་བཤད་དོ།།

[Block 130]
[^51]དུས་སུ་བཤད་ཅེས་བྱ་བ་ནི་རྡོ་རྗེ་འཆང་ཆེན་པོའོ།།

[Block 131]
བདག་པོའི་ཆོས་ཅན༌[^52]གཅིག་པུ་ལས།།

[Block 132]
ཞེས་བྱ་བ་ནི་ཡིད་དང་ལྷན་ཅིག་ཏུ་སྐྱེས་པའི་སྤྱོད་ཡུལ་དུ་གྱུར་པའི་དཀྱིལ་འཁོར་བར་གྱུར་པའོ།།

[Block 133]
གཉི་གའི་འཁོར་ལོ་རྗེས་སུ་མཉེས་པ་ཞེས་བྱ་བ་ནི་ཕྱི་ནང་གི་བདག་ཉིད་ཅན་གྱི་འཁོར་ལོའོ།།

[Block 134]
བཤད་མ་ཐག་པའི་ཆོ་ག་ཞེས་བྱ་བ་ནི་ལུས་ལ་སོགས་པའི་བྱིན་གྱིས་བརླབ་པའི་ཆོ་ག་སྟེ། དེ་ཉིད་ཀྱི་རྗེས་སུ་ཆགས་པ་ལ་སོགས་པ་བྱས་ནས།

[Block 135 [VERSE]]
གཉིས་པ་རྫོགས་པའི་རིམ་པ་ལ་གནས་པའོ། །
རྡོ་རྗེ་བཞི་པོ་ནི་རྣལ་འབྱོར་བཞི་པའོ། །

[Block 136]
ཕྲ་མོའི་སྦྱོར་བ་ཀུན་དུ་བརྩམས།།ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་སྦྱོར་བ་ནི་འོད་གསལ་བའོ།།

[Block 137]
འོད་གསལ་བ་དེའི་དེ་མ་ཐག་པར་ནི་པདྨ་དང་ཟླ་བ་དང་ཡི་གེ་གསུམ་ལ་སོགས་པའི་རིམ་པས་ལོངས་སྤྱོད་རྫོགས་པའི་སྐུར་བསྐྱེད་པའོ།[^53] །རང་གི་རྡོ་རྗེའི་བུ་གར་ཞེས་བྱ་བ་ནི་ནོར་བུའི་བུ་གར་བྱང་ཆུབ་ཀྱི་སེམས་བསྒོམ་པར་བྱའོ།།

[Block 138]
ཡུམ་ནི་ཤེས་རབ་མ་སྟེ་དེའི་པདྨའི་ནང་གི་སྣ་རྩེར་ཐིག་ལེ་རྡོ་རྗེར་ནས་འབྲུ་ཙམ་ལ་སོགས་པ་རྣམས་བསམ་པའོ།།

[Block 139]
འགྲོ་ཉལ་ཟ་བ་ཙམ་གྱི་སྤྱོད་པ་ཞེས་བྱ་བ་ནི་ཟས་ཟ་བ་ཙམ་དང་། ཉལ་བ་ཙམ་དང་། བཤད་དུ་འགྲོ་བ་ཙམ་ལས་མ་གཏོགས་པར་ཏིང་ངེ་འཛིན་ལ་དམིགས་པ་འབའ་ཞིག་གཞན་དུ་མི་གནས་པའོ།།

[Block 140]
ཡང་དག་སྔགས་ཀྱི༌[^54]གསང་བ་ཞེས་པ་ནི་གསུངས་མ་ཐག་པའི་སྔགས་ཀྱི་དེ་ཁོ་ན་ཉིད་དོ།[^55] །རྣལ་འབྱོར་པ་རྣམས་ཀྱི་གསང་བ་བརྟག་པའོ།།

[Block 141]
སྐད་ཅིག་ཅེས་བྱ་བ་ལ་སོགས་པའི་སྒྲས་ནི་རང་བཞིན་གྱིས་འོད་གསལ་བ་འབའ་ཞིག་སྟོན་ནོ།།

[Block 142]
སྔགས་པ་ཞེས་བྱ་བ་ནི་རྡོ་རྗེ་སེམས་དཔའོ།།

[Block 143]
སྒྲོན་མ་གསལ་བར་བྱེད་པའི་ལེའུ་དྲུག་པའི་དཀའ་བ་བཏུས་པའི་བཤད་པའོ།།།།

[Block 144 [HEADING]]
## ལེའུ་བདུན་པ། ^7-0

[Block 145]
ཡན་ལག་དྲུག་ཅེས་བྱ་བ་ནི་ཇི་སྐད་དུ་བཤད་པའི་བསྐྱེད་པའི་རིམ་པ་དང་། རྫོགས་པའི་རིམ་པ་དག་གིས་ཇི་ལྟ་བའི་སེམས་ཀྱི་ཡུལ་རྣམས་ལ་གནས་པའོ།།
--- END BLOCKS ---
