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
[Block 36]
ཞེས་པ་སྟེ། ཕྱག་འཚལ་ལོ། །གང་ལ་ན། ཤར་གྱི་ཕྱོགས་སྐྱོང་བརྒྱ་བྱིན་དང༌། ཤར་ལྷོའི་མེ་ལྷ་དང༌། སྟེང་གི་ཚངས་པ་དང་། ནུབ་བྱུང་གི་རླུང་ལྷ་དང༌། དེ་དག་གིས་མཚོན་པའི་གཤིན་རྗེ་དང་ཀླུ་སོགས་སྡེ་རིས་སྣ་ཚོགས་ཀྱི་དབང་ཕྱུག་སྟེ་གཙོ་བོ་རྣམས་ཀྱིས་གུས་པས་མཆོད་པའི་གནས་སུ་གྱུར་མ། དབང་ལྡན་གྱི་འཁོར་འབྱུང་པོ་རྣམས་དང༌། སྲིན་པོའི་འཁོར་རོ་ལངས་རྣམས་དང༌། བརྒྱ་བྱིན་གྱི་འཁོར་དྲི་ཟ་རྣམས་དང༌། ལུས་ངན་གྱི་འཁོར་གནོད་སྦྱིན་སོགས་འཁོར་གྱི་ཚོགས་རྣམས་ཀྱིས་ཀྱང་སྐུ་མདུན་དུ་བཏུད་ནས་གུས་པས་བསྟོད་པའི་ཡུལ་དུ་གྱུར་མ་དེ་ལའོ། །

[Block 37 [HEADING]]
###### དྲུག་པ་ཕ་རོལ་འཇོམས་པའི་སྒོ་ནས་བསྟོད་པ། ^2-2-1-1-6-0

[Block 38]
དྲུག་པ་ཕ་རོལ་འཇོམས་པའི་སྒོ་ནས་བསྟོད་པ་ནི།

[Block 39 [VERSE]]
ཕྱག་འཚལ་ཏྲཊ་ཅེས་བྱ་དང་ཕཊ་ཀྱིས། །
ཕ་རོལ་འཁྲུལ་འཁོར་རབ་ཏུ་འཇོམས་མ། །
གཡས་བསྐུམས་གཡོན་བརྐྱངས་ཞབས་ཀྱིས་མནན་ཏེ། །
མེ་འབར་འཁྲུག་པ་ཤིན་ཏུ་འབར་མ། །

[Block 40]
ཞེས་པ་སྟེ། ཕྱག་འཚལ་ལོ། །གང་ལ་ན། ཞལ་ནས་ཏྲཊ་(འདྲལ་བ་སྟེ་འཇོམས་པའོ)ཅེས་བྱ་བ་དང་ཕཊ་(འགས་པ་)ཅེས་བྱ་བའི་རིག་སྔགས་ཀྱི་ང་རོ་བསྒྲགས་པ་ཙམ་གྱིས་ཕ་རོལ་བྱད་མས་བསམ་སྦྱོར་ངན་པས་བྱས་པའི་འཁྲུལ་འཁོར་གྱི་ནུས་པ་ཐམས་ཅད་སྐད་ཅིག་ལ་རབ་ཏུ་འཇོམས་པར་མཛད་མ། གཡས་བསྐུམས་ཤིང་གཡོན་བརྐྱངས་པ་སྟོང་ཉིད་སྙིང་རྗེ་མཚོན་པའི་ཞབས་ཀྱི་འོག་ཏུ་བྱད་མ་དང་རྦད་འདྲེ་ལ་སོགས་པ་མནན་ཏེ། སྐུ་ལས་ཡེ་ཤེས་ཀྱི་མེ་འབར་ཞིང་འཁྲུག་པ་དང༌། ཤིན་ཏུ་འབར་བས་ཐལ་བ་ཙམ་ཡང་མ་ལུས་པར་སྲེག་པར་མཛད་མ་དེ་ལའོ། །

[Block 41]
ཞབས་ཞི་བའི་བཞུགས་ཚུལ་ཡིན་ཀྱང་མེ་འབར་བའི་དབུས་ན་བཞུགས་པ་ཅུང་ཟད་ཁྲོ་ཚུལ་ཙམ་མོ། །

[Block 42 [HEADING]]
##### གཉིས་པ་ཁྲོ་མོའི་རྣམ་པའི་སྒོ་ནས་བསྟོད་པ། ^2-2-1-2-0

[Block 43 [HEADING]]
###### དང་པོ་བདུད་དང་སྒྲིབ་གཉིས་སྦྱོང་བའི་སྒོ་ནས་བསྟོད་པ། ^2-2-1-2-1-0

[Block 44]
གཉིས་པ་ཁྲོ་མོའི་རྣམ་པའི་སྒོ་ནས་བསྟོད་པ་ལ་བདུན། བདུད་དང་སྒྲིབ་གཉིས་སྦྱོང་བའི་སྒོ་ནས་བསྟོད་པ། གཡས་གཡོན་གྱི་ཕྱག་མཚན་གྱི་སྒོ་ནས་བསྟོད་པ། དབུ་རྒྱན་དང་བཞད་སྒྲའི་སྒོ་ནས་བསྟོད་པ། ཕྱོགས་སྐྱོང་བཅུས་འཕྲིན་ལས་སྒྲུབ་པའི་སྒོ་ནས་བསྟོད་པ། དབུ་རྒྱན་གྱི་སྒོ་ནས་བསྟོད་པ། དྲག་པོའི་བཞུགས་ཚུལ་གྱི་སྒོ་ནས་བསྟོད་པ། ཧཾ་ཡིག་ལས་འོད་ཟེར་འཕྲོ་བའི་སྒོ་ནས་བསྟོད་བའོ། །དང་པོ་ནི།

[Block 45 [VERSE]]
ཕྱག་འཚལ་ཏུ་རེ་འཇིགས་པ་ཆེན་མོ། །
བདུད་ཀྱི་དཔའ་བོ་རྣམ་པར་འཇོམས་མ། །
ཆུ་སྐྱེས་ཞལ་ནི་ཁྲོ་གཉེར་ལྡན་མཛད། །
དགྲ་བོ་ཐམས་ཅད་མ་ལུས་གསོད་མ། །

[Block 46]
ཞེས་པ་སྟེ། ཕྱག་འཚལ་ལོ། །གང་ལ་ན། ཏུ་རེ་(མྱུར་མ་)ཞེས་སོགས་གསུང་གི་ང་རོ་དང་། འཇིགས་པ་ཆེན་མོ་སྟེ་ཤིན་ཏུ་དྲག་མོའི་སྐུའི་རྣམ་འགྱུར་གྱི། བདུད་ཀྱི་ནང་ནས་གདུལ་དཀའ་བའི་དཔའ་བོ་ནི་ཉོན་མོངས་པའི་བདུད་བཞི་འཇོམས་པར་མཛད་མ། ཆུ་སྐྱེས་ཏེ་པདྨ་རྒྱས་པ་ལྟར་མཛེས་པའི་ཞལ་རས་ནི་ཁྲོ་གཉེར་དང་ལྡན་པའི་རྣམ་པར་མཛད་པ་དེ་ཡིས། ཕྱི་རོལ་གྱི་དགྲ་བོ་ཐམས་ཅད་ཀྱང་ལྷག་མ་མ་ལུས་པར་གསོད་པར་མཛད་མ་དེ་ལའོ། །

[Block 47]
འདིར་ཐར་པའི་དགྲ་ཉོན་སྒྲིབ་དང༌། རྣམ་མཁྱེན་གྱི་དགྲ་ཤེས་སྒྲིབ་ལ་བྱས་ན་བསྡུས་དོན་དང་མཐུན་ནོ། །

[Block 48 [HEADING]]
###### གཉིས་པ་གཡས་གཡོན་གྱི་ཕྱག་མཚན་གྱི་སྒོ་ནས་བསྟོད་པ། ^2-2-1-2-2-0

[Block 49]
གཉིས་པ་གཡས་གཡོན་གྱི་ཕྱག་མཚན་གྱི་སྒོ་ནས་བསྟོད་པ་ནི།

[Block 50 [VERSE]]
ཕྱག་འཚལ་དཀོན་མཆོག་གསུམ་མཚོན་ཕྱག་རྒྱའི། །
སོར་མོས་ཐུགས་ཀར་རྣམ་པར་བརྒྱན་མ། །
མ་ལུས་ཕྱོགས་ཀྱི་འཁོར་ལོས་བརྒྱན་པའི། །
རང་གི་འོད་ཀྱི་ཚོགས་རྣམས་འཁྲུག་མ། །

[Block 51]
ཞེས་པ་སྟེ། ཕྱག་འཚལ་ལོ། །གང་ལ་ན། ཕྱག་གཡོན་པའི་མཐེབ་སྲིན་གྱིས་ཨུཏྤ་ལའིཡུ་བ་བཟུངས་ཤིང༌། མཛུབ་མོ་གུང་མོ་མཐེའུ་ཆུང་གསུམ་སྒྲེང་བ་དཀོན་མཆོག་གསུམ་འདུས་པའི་བདག་ཉིད་དུ་མཚོན་པའི་ཕྱག་རྒྱའི་སོར་མོ་རྣམས་ཀྱིས་ཐུགས་ཀར་རྣམ་པར་བརྒྱན་མ། མ་ལུས་པའི་ཕྱོགས་ཀྱི་ཆ་ཐམས་ཅད་ཕྱག་གཡས་པའི་མཆོག་སྦྱིན་གྱི་མཐིལ་འཁོར་ལོས་བརྒྱན་པ་ལས་འཕྲོས་པའི་རང་གི་འོད་ཟེར་གྱི་ཚོགས་རྣམས་ཕན་ཚུན་འཁྲུག་པས་གང་བར་མཛད་ནས་འོད་གཞན་ཐམས་ཅད་ཟིལ་གྱིས་གནོན་མ་དེ་ལའོ། །

[Block 52]
འདི་དང་འོག་གི་ས་བཅད་ལྔ་པ་གཉིས་ལ་ཁྲོ་ཉམས་མི་སྣང་ཡང་། དེའི་གྲས་སུ་བྱུང་བ་མི་ལྡོག་པས་བརྟག་གོ །

[Block 53 [HEADING]]
###### གསུམ་པ་དབུ་རྒྱན་དང་བཞད་སྒྲའི་སྒོ་ནས་བསྟོད་པ། ^2-2-1-2-3-0

[Block 54]
གསུམ་པ་དབུ་རྒྱན་དང་བཞད་སྒྲའི་སྒོ་ནས་བསྟོད་པ་ནི།

[Block 55 [VERSE]]
ཕྱག་འཚལ་རབ་ཏུ་དགའ་བ་བརྗིད་པའི། །
དབུ་རྒྱན་འོད་ཀྱི་འཕྲེང་བ་སྤེལ་མ། །
བཞད་པ་རབ་བཞད་ཏུ་ཏྟཱ་ར་ཡིས། །
བདུད་དང་འཇིག་རྟེན་དབང་དུ་མཛད་མ། །

[Block 56]
ཞེས་པ་སྟེ། ཕྱག་འཚལ་ལོ། །གང་ལ་ན། དད་ལྡན་རྣམས་ཀྱི་རེ་བ་བསྐོང་བས་རབ་ཏུ་དགའ་བ་བསྐྱེད་ཅིང་། མ་དད་པ་རྣམས་ཟིལ་གྱིས་གནོན་པས་བརྗིད་ཆགས་པའི་རིན་པོ་ཆེའི་དབུ་རྒྱན་འོད་ཟེར་འཕྲེང་བ་ཁ་དོག་སྣ་ཚོགས་པ་སྤེལ་ཏེ་འཕྲོ་མ། སྔགས་ཀྱི་བཞད་མོ་རབ་ཏུ་བཞད་པའི་སྒྲ་ཏུཏྟཱ་ར་ཞེས་སོགས་ཀྱིས་འདོད་ཁམས་ཀྱི་བདག་པོ་བདུད་དགའ་རབ་དབང་ཕྱུག་དང༌། དེའི་གཞན་དབང་དུ་གྱུར་པའི་འཇིག་རྟེན་མཐའ་དག་དབང་དུ་སྡུད་པར་མཛད་མ་དེ་ལའོ། །

[Block 57 [HEADING]]
###### བཞི་པ་ཕྱོགས་སྐྱོང་བཅུས་འཕྲིན་ལས་བསྒྲུབ་པའི་སྒོ་ནས་བསྟོད་པ། ^2-2-1-2-4-0

[Block 58]
བཞི་པ་ཕྱོགས་སྐྱོང་བཅུས་འཕྲིན་ལས་བསྒྲུབ་པའི་སྒོ་ནས་བསྟོད་པ་ནི།

[Block 59 [VERSE]]
ཕྱག་འཚལ་ས་གཞི་སྐྱོང་བའི་ཚོགས་རྣམས། །
ཐམས་ཅད་འགུག་པར་ནུས་པ་ཉིད་མ། །
ཁྲོ་གཉེར་གཡོ་བའི་ཡི་གེ་ཧཾ་གིས། །
ཕོངས་པ་ཐམས་ཅད་རྣམ་པར་སྒྲོལ་མ། །

[Block 60]
ཞེས་པ་སྟེ། ཕྱག་འཚལ་ལོ། །གང་ལ་ན། ས་གཞི་སྐྱོང་བ་ཕྱོགས་སྐྱོང་བཅུ་དང༌། དེ་དག་གི་འཁོར་གྱི་ཚོགས་རྣམས་ཐམས་ཅད་འཕྲིན་ལས་སྒྲུབ་པའི་བྲན་དུ་འགུགས་པར་ནུས་པའི་བདག་ཉིད་མ། ཞལ་ཁྲོ་གཉེར་གཡོ་བའི་རྣམ་པར་བཞུགས་པའི་ཐུགས་ཀའི་ཡི་གེ་ཧཱུཾ་འོད་ཟེར་གྱི་ལྕགས་ཀྱུས་འདོད་རྒུ་ཐམས་ཅད་བཀུག་ནས། སེམས་ཅན་དབུལ་ཞིང་ཕོངས་པའི་སྡུག་བསྔལ་གྱིས་གཟིར་བ་ཐམས་ཅད་རྣམ་པར་སྒྲོལ་བར་མཛད་མ་དེ་ལའོ། །

[Block 61 [HEADING]]
###### ལྔ་པ་དབུ་རྒྱན་གྱི་སྒོ་ནས་བསྟོད་པ། ^2-2-1-2-5-0

[Block 62]
ལྔ་པ་དབུ་རྒྱན་གྱི་སྒོ་ནས་བསྟོད་པ་ནི།

[Block 63 [VERSE]]
ཕྱག་འཚལ་ཟླ་བའི་རྩེ་མོས་དབུ་རྒྱན། །
བརྒྱན་པ་ཐམས་ཅད་ཤིན་ཏུ་འབར་མ། །
རལ་པའི་ཁྲོད་ན་འོད་དཔག་མེད་ལས། །
རྟག་པར་ཤིན་ཏུ་འོད་རབ་མཛད་མ། །

[Block 64]
ཞེས་པ་སྟེ། ཕྱག་འཚལ་ལོ། །གང་ལ་ན། ཟླ་བའི་རྩེ་མོ་སྟེ་ཚེས་གཅིག་གི་ཟླ་བས་དབུ་ལ་བརྒྱན་ཅིང་། དེ་ལ་སོགས་པའི་རྒྱན་གྱིས་བརྒྱན་པ་ཐམས་ཅད་ལས་སྡུག་བསྔལ་སེལ་བའི་འོད་ཟེར་དཀར་པོ་རབ་ཏུ་འབར་ཞིང་འཕྲོ་མ། གནག་ཅིང་སྣུམ་པའི་རལ་པའི་ཁྲོད་ན་སངས་རྒྱས་འོད་དཔག་མེད་རིགས་བདག་ཏུ་བཞུགས་པ་ལས་ཀྱང་དུས་རྟག་པར་སེམས་ཅན་གྱི་དོན་དུ་ཤིན་ཏུ་འོད་ཟེར་གྱི་ཚོགས་ནི་འགྱེད་པར་མཛད་མ་དེ་ལའོ། །

[Block 65 [HEADING]]
###### དྲུག་པ་དྲག་པོའི་བཞུགས་ཚུལ་གྱི་སྒོ་ནས་བསྟོད་པ། ^2-2-1-2-6-0

[Block 66]
དྲུག་པ་དྲག་པོའི་བཞུགས་ཚུལ་གྱི་སྒོ་ནས་བསྟོད་པ་ནི།

[Block 67 [VERSE]]
ཕྱག་འཚལ་བསྐལ་པ་ཐ་མའི་མེ་ལྟར། །
འབར་བའི་འཕྲེང་བའི་དབུས་ན་གནས་མ། །
གཡས་བརྐྱངས་གཡོན་བསྐུམས་ཀུན་ནས་བསྐོར་དགའི། །
དགྲ་ཡི་དཔུང་ནི་རྣམ་པར་འཇོམས་མ། །

[Block 68]
ཞེས་པ་སྟེ། ཕྱག་འཚལ་ལོ། །གང་ལ་ན། བསྐལ་པ་ཐ་མའི་མེས་འཇིག་གི་དུས་ཀྱི་མེ་ལྟར་ཡེ་ཤེས་ཀྱི་མེ་དཔུང་འབར་བའི་འཕྲེང་བ་འཁྲུག་པའི་དབུས་ན་གནས་མ། དེ་ཡང་ཞབས་གཡས་བརྐྱངས་ཤིང་གཡོན་བསྐུམས་པའི་སྟབས་ཀྱིས་བཞུགས་ནས། སྒོ་ཀུན་ནས་ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་བ་ལ་དགའ་བའི་གདུལ་བྱའི་རྒྱུད་ཀྱི་ཕྱི་ནང་གི་དགྲ་ཡི་དཔུང་ཚོགས་རྣམ་པར་འཇོམས་པར་མཛད་མ་དེ་ལའོ། །

[Block 69 [HEADING]]
###### བདུན་པ་ཧཱུཾ་ཡིག་ལས་འོད་ཟེར་འཕྲོ་བའི་སྒོ་ནས་བསྟོད་པ། ^2-2-1-2-7-0

[Block 70]
བདུན་པ་ཧཱུཾ་ཡིག་ལས་འོད་ཟེར་འཕྲོ་བའི་སྒོ་ནས་བསྟོད་པ་ནི།

[Block 71 [VERSE]]
ཕྱག་འཚལ་ས་གཞིའི་ངོས་ལ་ཕྱག་གི། །
མཐིལ་གྱིས་བསྣུན་ཅིང་ཞབས་ཀྱིས་བརྡུང་མ། །
ཁྲོ་གཉེར་ཅན་མཛད་ཡི་གེ་ཧཾ་གིས། །
རིམ་པ་བདུན་པོ་རྣམས་ནི་འགེམས་མ། །

[Block 72]
ཞེས་པ་སྟེ། ཕྱག་འཚལ་ལོ། །གང་ལ་ན། རི་རབ་གླིང་དང་བཅས་པའི་ས་གཞི་ཆེན་པོའི་ངོས་ལ། སྡིགས་མཛུབ་དང་བཅས་པའི་ཕྱག་གི་མཐིལ་གྱིས་དྲག་ཏུ་བསྣུན་ཅིང་ཞབས་ཀྱི་མཐིལ་གྱིས་བརྡུང་བར་མཛད་མ། དེ་ཡང་ཞལ་ཁྲོ་གཉེར་བསྡུས་པ་སོགས་ཤིན་ཏུ་དྲག་མོའི་རྣམ་པ་ཅན་དུ་མཛད་པའི་ཕྱག་ཞབས་ཀྱི་མཐིལ་དུ་ཡི་གེ་ཧཾ་སྔོན་པོ་རེ་རེ་གནས་པ་ལས་རྡོ་རྗེའི་མེ་ཆར་སྤྲོས་པས། གཞི་དང༌། ལྷག་པའི་གཞི་དང༌། གཞི་མེད་པ་དང་། གཞི་ཉིད་དང༌། བཅུད་ཀྱི་གཞི་དང༌། །གཞི་བཟང་པོ་དང༌། དག་པའི་གཞི་སྟེ། ས་འོག་རིམ་པ་བདུན་པོ་ན་གནས་པའི་ཀླུ་དང་ལྷ་མིན་དང་གཤིན་རྗེ་སོགས་གདུག་པ་ཅན་རྣམས་ནི་འགེམས་པ་སྟེ་འཇོམས་པར་མཛད་མ་དེ་ལའོ། །

[Block 73 [HEADING]]
#### གཉིས་པ་ཆོས་སྐུའི་རྣམ་པའི་སྒོ་ནས་བསྟོད་པ། ^2-2-2-0

[Block 74]
གཉིས་པ་ཆོས་སྐུའི་རྣམ་པའི་སྒོ་ནས་བསྟོད་པ་ནི།

[Block 75 [VERSE]]
ཕྱག་འཚལ་བདེ་མ་དགེ་མ་ཞི་མ། །
མྱ་ངན་འདས་ཞི་སྤྱོད་ཡུལ་ཉིད་མ། །
སྭཱ་ཧྭ་ཨོཾ་དང་ཡང་དག་ལྡན་པས། །
སྡིག་པ་ཆེན་པོ་འཇོམས་པ་ཉིད་མ། །
--- END BLOCKS ---
