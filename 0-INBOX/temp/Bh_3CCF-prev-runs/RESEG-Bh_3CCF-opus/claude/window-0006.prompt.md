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
[Block 211]
སྐྱེ་བོ་སྐལ་བ་དང་ལྡན་པ༌[^84]ཞེས་བྱ་བ་ནི་རྣལ་འབྱོར་པས་གཞན་གྱི་དོན་དུ་བྱའོ།།

[Block 212]
གཞན་དག་ཏུ་ཞེས་བྱ་བ་ནི་གདུག་པ་ཅན་གྱི་སེམས་ཅན་ལའོ།།

[Block 213]
ཐུན་མོང་མ་ཡིན་པ་ཞེས་བྱ་བ་ནི་སྤྱོད་ཡུལ་མ་ཡིན་པའོ།།

[Block 214]
རྒྱས་གདབ་པར་བྱའོ་ཞེས་བྱ་བ་ནི་སྙོམས་པར་འཇུག་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ།།

[Block 215]
ལག་པར་གནས་པ་ཞེས་བྱ་བ་ནི་བསྒྲུབ་པར་བྱ་བ་བཀུག་ལ་ལག་པས་བཟུང་སྟེ། བཟླས་པའི་སྔགས་ཀྱི་ཡི་གེ་དེ་ལ་དབང་དུ་བྱ་བ་ལ་སོགས་པའི་སྔགས་བཟླས་ཤིང་བསམ་གཏན་བྱ་བའོ།།

[Block 216]
སྒྲར་གྲག་པ༌[^85]ཟིན་པ་དང་ཞེས་བྱ་བ་ནི་སེམས་ཅན་གྱི་འབྱུང་བས་བསྐྱེད་པའོ།།

[Block 217 [VERSE]]
མ་ཟིན་པ་ནི་རྔ་དང་ཤིང་ལ་སོགས་པའི་སྒྲའོ། །
གཉི་ག་ནི་སེམས་དང་སེམས་མེད་པས་བྱས་པའི་སྒྲའོ། །

[Block 218]
འབྲས་བུའི་ཕྱོགས་གཅིག་པོ་ཞེས་བྱ་བ་ནི་ཐ་མལ་པའི་དངོས་གྲུབ་པོ།།

[Block 219]
དེ་ནས་སའི་ཆ་ལ་སོགས་པ་ཞེས་བྱ་བ་ནི་གཞལ་ཡང༌[^86]ཁང་བརྩེགས་པ་ལ་སོགས་པའོ།།

[Block 220]
རྒྱུ་དང་འབྲས་བུ་ཞེས་བྱ་བ་ནི་སྔ་མ་སྔ་མ་ནི་རྒྱུ་ཡིན་ལ་ཕྱི་མ་ཕྱི་མ་ནི་འབྲས་བུ་ཡིན་ནོ།།

[Block 221]
བདག་པོ་རྡོ་རྗེ་འཆང་ཆེན་པོ་ཞེས་བྱ་བ་ནི་མི་བསྐྱོད་པའོ།།

[Block 222]
གསང་བ་གསུམ་ཞེས་བྱ་བ་ནི་ཡུལ་དང་དབང་པོ་དང་རྣམ་པར་ཤེས་པ་སྟེ། དམན་པ་དང་འབྲིང་པོ་དང་། མཆོག་གི་དབྱེ་བས་དབང་པོའི་རྣམ་པར་ཤེས་པས་ཡུལ་རྣམས་འཛིན་ཏོ།།

[Block 223]
དེ་ལ་རིམ་པ་བཞིན་དུ་རབ་ཏུ་སྦྱར་ནས་མཚན་མ་རྣམས་རབ་ཏུ་སྐྱེ་སྟེ། མཚན་མ་དབང་པོ་རྣམས་ཡང་དག་པར་སྐྱེ་བར་འགྱུར་རོ།།

[Block 224]
རྡོ་རྗེའི་ལམ་ནི་འོད་གསལ་བ་ནས་སོ།།

[Block 225]
ཐབས་དང་ཤེས་རབ་སྙོམས་པར་འཇུག་པ་ཞེས་བྱ་བ་ནི་བདེན་པ་གཉིས་གཅིག་ཏུ་གྱུར་པའོ།།

[Block 226]
སྒྲོན་མ་གསལ་བར་བྱེད་པའི་ལེའུ་བཅུ་གཉིས་པའི་དཀའ་བ་བཏུས་པའི་བཤད་པའོ།།།།

[Block 227 [HEADING]]
## ལེའུ་བཅུ་གསུམ་པ། ^13-0

[Block 228]
རིམ་པ་གཉིས་ནི་མ་རྫོགས་པ་དང་རྫོགས་པའི་རིམ་པ་དག་ལ་བསླབ་པའོ།།

[Block 229]
མ་གནང་བའི་མངོན་སྤྱོད་ཅེས་བྱ་བ་ནི་སེམས་ཅན་གྱི་དོན་སྤངས་པའི་དབང་ཕྱུག་ཆེན་པོ་ལ་སོགས་པའི་དབང་དང་མངོན་སྤྱོད་ལ་སོགས་པའོ།།

[Block 230]
སྤྱོད་པ་ནི་ལས་དེ་དག་སྤྱོད་པར་མཛད་པ་བསྐྱེད་པའོ།།

[Block 231]
ཉེ་བར་ལེན་པའི༌[^87]ཕྱག་རྒྱ་ཆེན་པོའི༌[^88]སྐུ་ལ་ཉེ་བར་ལེན་པ་ཞེས་བྱ་སྟེ་ཡི་གེ་གསུམ་པའོ།།

[Block 232]
དེ་སྨྲས་པ་ནི་སྤྲུལ་པའི་སྐུ་ཉེ་བར་ལེན་པའོ་ཞེས་པ་སྟེ། ཕྱག་རྒྱ་ཆེན་པོའི་སྐུར་སྦྱར་བས་རྡོ་རྗེ་བཟླས་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ།།

[Block 233]
སངས་རྒྱས་རྣམས་ཀྱི་ཞེས་བྱ་བ་ནི་མི་བསྐྱོད་པ་ལ་སོགས་པའི་སངས་རྒྱས་གཞན་རྣམས་ཀྱང་སྟེ། དེར་ཡི་གེ་གསུམ་གྱིས་སངས་རྒྱས་ཀྱི་སྐུར་བསྐྱེད་པ༌[^89]ལ་སངས་རྒྱས་སྤྱན་ལ་སོགས་པ་སྤྲོས་ནས་སྙོམས་པར་འཇུག་པ་ལ་སོགས་པ་ཁྱད་པར་ཅན་གྱི་མཚན་ཉིད་ཀྱིས་ཕན་ཚུན་དུ་མཆོད་པར་བྱའོ།།

[Block 234]
ཡང་སངས་རྒྱས་ཀྱི་ཞེས་བྱ་བ་ནི་མི་བསྐྱོད་པ་ལ་སོགས་པའི་སངས་རྒྱས་ཀྱི་ཕྱག་རྒྱ་ཆེན་པོའི་སྐུ་རྣམས་སོ།།

[Block 235]
རང་གི་ལུས་དང་ངག་དང་ཡིད་ཀྱི་ནང་ན༌[^90]གནས་པའི་བཀོད་པའི་མཆོད་པས་སྐུ་གསུང་ཐུགས་ལ༌[^91]མཆོད་པ་ནི་བླ་ན་ཡོད་པའི་མཆོད་པར་འགྱུར་རོ།།

[Block 236]
དེ་ལྟར་དབང་པོ་རབ་དང་ལྡན་པ་ཞེས་བྱ་བ་ནི་དབང་པོ་རབ་དང་ལྡན་པ་ཡི་ནི་དུས་གཅིག་ཏུ་སྤྲོས་པར་བརྗོད་དོ།།

[Block 237]
ཡང་ན་ཞེས་བྱ་བ་ནི་རིམ་པས་སྤྲོས༌[^92]ལ་མཆོད་པ་བྱའོ་ཞེས་སྟོན་པ་ཡིན་ནོ།།

[Block 238]
ཡེ་ཤེས་ཀྱི་ཁྱད་པར་གྱིས་ཞེས་བྱ་བ་ནི་རླུང་དང་རྣམ་པར་ཤེས་པ་སྒྱུ་མའི་རང་བཞིན་ཅན་གྱིས་སོ།།

[Block 239]
སྐུ་རྡོ་རྗེ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་ཡི་གེ་གསུམ་རྣམ་པར་དག་པའི་སྒོ་ནས་རྡོ་རྗེ་བཟླས་པར་བྱ་བ་བརྗོད་པ་ཡིན་ནོ།།

[Block 240]
དོན་གྱི་རྗེས་འགྲོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་གསལ་ལོ།།

[Block 241]
ལུས་ཏེ་ཞེས་བྱ་བ་ནི་རྣམ་པར་དག་པ་གང་གིས་གཤིན་རྗེ་གཤེད་ལ་སོགས་པ་སྐྱེས་པ་དང་བུད་མེད་ཀྱི་མཚན་ཉིད༌[^93]ཅན་དུ་བྱ་བའོ།།

[Block 242]
མ་རིག་པའོ་ཞེས་བྱ་བ་ནི་སྟོང་པ༌[^94]ཆེན་པོའོ།།

[Block 243]
དེས་དོན་དུ་གཉེར་ཞིང་གསལ་བ་ནི་ཧཱུཾ་གིས་བསྒྲུབ་བྱ་སྦར་བར་བྱ་བའོ།།

[Block 244]
འདི་ཉིད་ཀྱི་ཆོ་ག་ཞེས་བྱ་བ་ནི་དཀྱིལ་འཁོར་པར་གྱུར་པས༌[^95]ཞི་བ་ལ་སོགས་པ་བྱའོ།[^96] །ཁ་སྦྱར་དབྱེ་བ་ཞེས་བྱ་བ་ནི་བསྒྲུབ་བྱའི་མིག་ལ་སོགས་པ་ལུས་ལ་བཅུག་ལ་ལས་རྣམས་བྱ་བའོ།།

[Block 245]
རྣམ་པར་སྣང་མཛད་ཡོངས་སུ་གྱུར་པ་ལས་ཞེས་བྱ་བ་ནི་རྣམ་པར་སྣང་མཛད་ཀྱི་རྣལ་འབྱོར་པས་རྣམ་པར་སྣང་མཛད་ལས་སྐྱེས་པའི་རྡོ་རྗེ་སེམས་དཔའ་སྦྱོར་བ་དང་ལྡན་པ་མངོན་སྤྱོད་བྱ་བ་ཡིན་ནོ།།

[Block 246]
ཕུན་སུམ་ཚོགས་པ་ནི་བསྐྱེད་པའོ།།

[Block 247]
བདག་ནི་ཞེས་བྱ་བ་ནི་བདག་དེ་བཞིན་གཤེགས་པ་ཆེ་གེ་མོའི་ཞེས་ང་རྒྱལ་དང་ལྡན་པར་བྱའོ།།

[Block 248]
བསྒྲུབ་བྱའི་ལུས་རང་གི་གཞིར་གྱུར་པ་ཞེས་བྱ་བ་ནི་བཞི་པའི་བསྒྲུབ་བྱའི་བདག་ཉིད་སྟོང་པར་བསམ་པའོ།།

[Block 249]
ནམ་མཁའི་དབྱིངས་ཀྱི་དབུས་ཏེ་ཞེས་བྱ་བ་ནི་རྡོ་རྗེ་སེམས་དཔའི་ཤེས་རབ་ཀྱི་ཆོས་འབྱུང་བ་ལའོ།།

[Block 250]
དེར་ཡི་གེ་ཨོཾ་བལྟས་ལ་རྡོ་རྗེ་སེམས་དཔའ་ནང་དུ་བཅུག་ནས་བདག་ཉིད་བསྒོམས་ཏེ། བདག་ཉིད་ཀྱི་སྙིང་གར་བསྒྲུབ་བྱ་དགོད་པར་བྱ་བའོ།།
--- END BLOCKS ---
