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
ཡང་ན། བརྒྱད་གཉིས་པ་སྒྲིགས་ཞེས་འདོན་པ་ལྟར་ན། ཞལ་གྱི་ནང་ན་ཟླ་བ་ལྟ་བུའི་ཚེམས་བརྒྱད་གཉིས་བཅུ་དྲུག་བསྒྲིགས་པའི་ཞལ་རས་ལ་སྐར་མ་སྟོང་ཕྲག་ཚོགས་པ་བས་ཀྱང་ལྷག་པའི་འོད་འཕྲོ་ཞེས་པ་དང་། བརྒྱད་པོ་དེ་གཉིས་བསྒྲིགས་ཞེས་པས། མཚན་བཟང་པོ་སོ་གཉིས་མཚོན་པའོ། །

[Block 37]
འདི་ལ་དཀར་མོ་མདངས་ལྡན་སྒྲོལ་མ་ཞེས་བཤད་དོ། །

[Block 38 [HEADING]]
###### **གཉིས་པ་སྐུ་མདོག་དང་ཕྱག་མཚན་དང་རྒྱུའི་སྒོ་ནས་བསྟོད་པ།** ^2-2-2-1-1-2-0

[Block 39]
གཉིས་པ་སྐུ་མདོག་དང་། ཕྱག་མཚན་དང་། རྒྱུའི་སྒོ་ནས་བསྟོད་པ་ནི། ཕྱག་འཚལ་སེར་སྔོ་ཆུ་ནས་སྐྱེས་ཀྱི། །པདྨས་ཕྱག་ནི་རྣམ་པར་བརྒྱན་མ། །ཞེས་སོགས་ཏེ། སྔོ་བ་ནི། སྐུ་མདོག །སེར་ནི། ཁ་དོག་དྭངས་པ་མཚོན་པ་སྟེ། གསེར་མདོག་ཅན་གྱི་སྒྲོལ་མ་ཞེས་འབྱུང་བས་སོ། །

[Block 40]
དེའི་ཕྱག་གཡོན་གྱི་སྲིན་ལག་གིས་ཆུ་ནས་སྐྱེས་པའི་པདྨ་སྟེ་ཨུཏྤ་ལས་ཐུགས་ཀར་རྣམ་པར་བརྒྱན་པ་སྟེ། བཟུངས་ནས་སྙན་གྱི་ཐད་ཀར་ཁ་བྱེ་བ་ནི། ཕ་རོལ་ཏུ་ཕྱིན་པ་བཅུ་དག་པའི་རྟགས་སོ། །

[Block 41]
དེ་བས་ན། སྦྱིན་པ་བརྩོན་འགྲུས་དཀའ་ཐུབ་སྟེ་ཚུལ་ཁྲིམས། བཟོད་པ། བསམ་གཏན་སྤྱོད་ཡུལ་ཏེ། ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་རྣམས་སོ། །

[Block 42]
ཞི་བ་ཞེས་པ། མི་མཐུན་ཕྱོགས་སེར་སྣ། ལེ་ལོ། འཆལ་ཚུལ། ཁོང་ཁྲོ། རྣམ་གཡེང་། ལོག་པའི་ལྟ་བ་སོགས་ཞི་བ་ནི། སྒྲོན་མའི་སྤྱོད་ཡུལ་ཏེ། དེའི་རྒྱུ་ལས་བྱུང་ཞེས་པའོ། །

[Block 43 [HEADING]]
###### **གསུམ་པ་རྒྱལ་བ་དང་རྒྱལ་སྲས་ཀྱིས་གུས་པས་བསྟེན་པའི་སྒོ་ནས་བསྟོད་པ།** ^2-2-2-1-1-3-0

[Block 44]
གསུམ་པ། རྒྱལ་བ་དང་། རྒྱལ་སྲས་ཀྱིས་གུས་པས་བསྟེན་པའི་སྒོ་ནས་བསྟོད་པ་ནི། ཕྱག་འཚལ་དེ་བཞིན་གཤེགས་པའི་གཙུག་ཏོར། །ཅེས་སོགས་ཏེ། དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་ཡུམ་ཡིན་པས་དབུའི་གཙུག་ཏོར་ལྟར་འཁུར་ཞིང་། དེ་བས་ན། ཚེ་འདིའི་རྒུད་པ་དང་། ཉོན་མོངས་པའི་སྒྲིབ་པ་དང་། འཁོར་གསུམ་དུ་གཏོགས་པ་སོགས་ཤེས་བྱའི་སྒྲིབ་པ་མཐའ་ཡས་པ་ལས་རྣམ་པར་རྒྱལ་བར་སྤྱོད་མའོ། །

[Block 45]
རྒྱལ་སྲས་ཀྱིས་བསྟེན་པ་ནི། ས་བཅུ་མ་ལུས་པའི་ངོ་བོ། ཕ་རོལ་ཏུ་ཕྱིན་པ་བཅུ་ཐོབ་པའི་རྒྱལ་བའི་སྲས་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱིས་ཤིན་ཏུ་གུས་པའི་གཙུག་གིས་བསྟེན་པའོ། །

[Block 46]
འདི་ལ་གཙུག་ཏོར་རྒྱན་པའི་སྒྲོལ་མ་ཞེས་འབྱུང་ངོ། །

[Block 47 [HEADING]]
###### **བཞི་པ་མི་མཐུན་ཕྱོགས་གནོན་པའི་སྒོ་ནས་བསྟོད་པ།** ^2-2-2-1-1-4-0

[Block 48]
བཞི་པ་མི་མཐུན་ཕྱོགས་གནོན་པའི་སྒོ་ནས་བསྟོད་པ་ནི། ཕྱག་འཚལ་ཏུཏྟཱ་ར་ཧཱུཾ་ཡི་གེས། །ཞེས་སོགས་ཏེ། ཏུཏྟཱ་ར་ཧཱུཾ་ཞེས་པའི་གསུང་དང་། ཐུགས་ཀའི་ཧཱུཾ་ཡིག་ནི། སྟོང་ཉིད་སྙིང་རྗེ་མཚོན་པས། དེས་མཐུན་ཕྱོགས་འདོད་པ་དང་། ཕྱོགས་གཟུགས་ཁམས་དང་། ནམ་མཁའ་གཟུགས་མེད་ཁམས་ཏེ། འདོད་པ་ ངན་སོང་གསུམ། འདོད་པའི་ལྷ་མི་གཉིས། གཟུགས་དང་གཟུགས་མེད་ཀྱི་འཇིག་རྟེན་བདུན་པོ། སྟོང་ཉིད་སྙིང་རྗེའི་སྙིང་པོ་ཅན་གྱི་ཞབས་ཀྱིས་མནན་ཏེ། ལུས་པ་མེད་པར་དེ་དག་བདེ་བ་ལ་འགུགས་པར་ནུས་མའོ། །

[Block 49]
འདི་ལ་ཧཱུཾ་སྒྲ་སྒྲོགས་པའི་སྒྲོལ་མ་ཞེས་འབྱུང་ངོ། །

[Block 50 [HEADING]]
###### **ལྔ་པ་འཇིག་རྟེན་པའི་ལྷ་ཆེན་པོ་རྣམས་ཀྱིས་བསྟོད་པ།** ^2-2-2-1-1-5-0

[Block 51]
ལྔ་པ་འཇིག་རྟེན་པའི་ལྷ་ཆེན་པོ་རྣམས་ཀྱིས་བསྟོད་པ་ནི། ཕྱག་འཚལ་ལོ། །གང་ལ་ན། ལྷ་དབང་བརྒྱ་སྦྱིན། མེ་ལྷ། ཚངས་པ། རླུང་ལྷ་ལ་སོགས་སྣ་ཚོགས་པའི་དབང་ཕྱུག་སྟེ།

[Block 52]
གཙོ་བོ་རྣམས་ཀྱིས་མཆོད་པའི་སྒྲོལ་མའོ། །དེར་མ་ཟད་འབྱུང་པོའི་གཙོ་བོ་ཚོགས་བདག །

[Block 53]
རོ་ལངས་ཀྱི་གཙོ་བོ་དབང་ཕྱུག་ཆེན་པོ། དྲི་ཟ་ཟུར་ཕུད་ལྔ་པ་ལ་སོགས་པ་རྣམས་དང་། གནོད་སྦྱིན་གྱི་གཙོ་བོ་རྣམ་ཐོས་ཀྱི་སྲས་འཁོར་གྱི་ཚོགས་དུ་མ་དང་བཅས་པ་རྣམས་ཀྱིས་མདུན་ནས་བསྟོད་མའོ། །

[Block 54]
འདི་ལ་རྣམ་པར་རྒྱལ་བའི་སྒྲོལ་མ་ཞེས་འབྱུང་ངོ་། །

[Block 55 [HEADING]]
###### **དྲུག་པ་ཕ་རོལ་འཇོམས་པའི་སྒོ་ནས་བསྟོད་པ།** ^2-2-2-1-1-6-0

[Block 56]
དྲུག་པ་ཕ་རོལ་འཇོམས་པའི་སྒོ་ནས་བསྟོད་པ་ནི། ཕྱག་འཚལ་ཏྲད་ཅེས་བྱ་དང་ཕཊ་ཀྱིས། །ཕ་རོལ་འཁྲུལ་འཁོར་རབ་ཏུ་འཇོམས་མ། །ཞེས་སོགས་ཏེ། དྲག་པོའི་སྔགས་ཀྱིས་ཕ་རོལ་གྱིས་བྱས་པའི་མཐུ་དང་། བྱད་མ་ལ་སོགས་པའི་འཁྲུལ་འཁོར་གྱིས་གནས་སྐབས་དང་། མཐར་ཐུག་གི་བདེ་བ་ལ་བར་དུ་གཅོད་པ་འཇོམས་མ་སྟེ། འདི་ལ་རྒོལ་བ་འཇོམས་པའི་སྒྲོལ་མ་ཞེས་འབྱུང་ངོ་། །དེ་ལྟ་བུའི་ཞི་བའི་བཞུགས་ཚུལ་ནི། གཡས་བསྐུམས་པ་ནི། སྟོང་ཉིད་རྟོགས་པ་མཚོན། གཡོན་བརྐྱངས་པ་ནི། སྙིང་རྗེ་མཚོན། དེ་ལྟ་བུའི་སྟོང་ཉིད་སྙིང་རྗེའི་ཞབས་སྲིད་གསུམ་མནན་ཏེ། མེ་འབར་འཁྲུག་པ་ཤིན་ཏུ་འབར་མ། །ཞེས་པ་ནི། ཕྱི་ཁྲོ་མོར་གྱུར་པ། ད་ལྟ་ཡང་ཅུང་ཟད་ཁྲོས་པའི་ཚུལ་གྱིས་མེ་འབར་བའི་དབུས་ན་འགྱིངས་པའོ། །

[Block 57 [HEADING]]
###### གཉིས་པ་ཁྲོ་མོའི་རྣམ་པའི་སྒོ་ནས་བསྟོད་པ། ^2-2-2-1-2-0

[Block 58]
གཉིས་པ་ཁྲོ་མོའི་རྣམ་པའི་སྒོ་ནས་བསྟོད་པ་ལ། ཕྱག་འཚལ་བདུན་ཡོད་པའི།

[Block 59 [HEADING]]
###### **དང་པོ་བདུད་དང་སྒྲིབ་གཉིས་སྤྱོད་པའི་ཡོན་ཏན།** ^2-2-2-1-2-1-0

[Block 60]
དང་པོ་བདུད་དང་སྒྲིབ་གཉིས་སྤྱོད་པའི་ཡོན་ཏན་ནི། ཕྱག་འཚལ་ཏུ་རེ་འཇིགས་པ་ཆེན་མོ། །བདུད་ཀྱི་དཔའ་བོ་རྣམ་པར་འཇོམས་མ། །ཞེས་སོགས་ཏེ། ཏུ་རེ་ནི། སྒྲོལ་མ། འཇིགས་པ་ཆེན་མོའི། ཁྲོ་མོ། བདུད་ཀྱི་དཔའ་བོ་ནི། ཉོན་མོངས་པ་ཡིན་པས། དེ་ལ་སོགས་པ་བདུད་བཞི་རྣམ་པར་འཇོམས་མའོ། །

[Block 61]
གཞན་ཡང་། དེ་ལྟ་བུའི་ཆུ་སྐྱེས་ཀྱི་ཞལ་ནི། ཁྲོ་གཉེར་ལྡན་མཛད་དེ། ཁྲོ་མོའི་ཆ་ལུགས་མཛད་དེ། ཁྲོ་མོའི་ཆ་ལུགས་མཛད་པས་ཐར་པ་ཐོབ་པ་ལ་བར་དུ་གཅོད་པའི་དགྲ་བོ་ཉོན་མོངས་པའི་སྒྲིབ་པ། ཐམས་ཅད་མཁྱེན་པ་ལ་བར་དུ་གཅོད་པའི་དགྲ་བོ་ཤེས་བྱའི་སྒྲིབ་པ་མ་ལུས་པ་སྟེ། བག་ཆགས་དང་བཅས་པ་གསོད་པར་མཛད་མའོ། །

[Block 62]
འདི་ལ་དབང་མཆོག་སྟེར་བའི་སྒྲོལ་མ་ཞེས་འབྱུང་ངོ་། །

[Block 63 [HEADING]]
###### **གཉིས་པ་གཡས་གཡོན་གྱི་ཕྱག་མཚན་གྱི་སྒོ་ནས་བསྟོད་པ།** ^2-2-2-1-2-2-0

[Block 64]
གཉིས་པ་གཡས་གཡོན་གྱི་ཕྱག་མཚན་གྱི་སྒོ་ནས་བསྟོད་པ་ནི། གཡོན་པའི་ཕྱག་མཚན། ཕྱག་འཚལ་དཀོན་མཆོག་གསུམ་མཚོན་ཕྱག་རྒྱའི། །(སོ་,སོར་)མོས་ཐུགས་ཀར་རྣམ་པར་བརྒྱན་མ། །ཞེས་པའི་མཐེབ་སྲིན་གཉིས་ཀྱིས་ཨུཏྤ་ལ་བཟུངས་ཤིང་། མཛུབ་མོ་གུང་མོ། མཐེ་ཆུང་གསུམ་གྱི་སོར་མོ་ཐུགས་ཀར་བརྐྱངས་པའི་ཚུལ་གྱིས་རྣམ་པར་བརྒྱན་མའོ། །

[Block 65]
གཡས་པའི་ཕྱག་མཚན། མ་ལུས་ཕྱོགས་ཀྱི་འཁོར་ལོས་བརྒྱན་པའི། །རང་གི་འོད་ཀྱི་ཚོགས་རྣམས་འཁྲུག་མ། །ཕྱག་གཡས་ཀྱི་ཕྱོགས་མ་ལུས་པ་མཆོག་སྦྱིན་མཛད་པའི་ཕྱག་གི་མཐིལ་འཁོར་ལོས་བརྒྱན་པའི་རང་གི་ཕྱག་མཚན་གྱི་འཁོར་ལོའི་འོད་ཀྱིས། འོད་ཀྱི་ཚོགས་གཞན་རྣམས་འཁྲུག་པ་སྟེ་ཟིལ་གྱིས་གནོན་མའོ། །

[Block 66]
འདི་ལ་སེང་ལྡེང་ནགས་ཀྱི་སྒྲོལ་མ་ཞེས་འབྱུང་ངོ་། །

[Block 67 [HEADING]]
###### **གསུམ་པ་དབུ་རྒྱན་དང་བཞད་སྒྲའི་སྒོ་ནས་བསྟོད་པ།** ^2-2-2-1-2-3-0

[Block 68]
གསུམ་པ་དབུ་རྒྱན་དང་བཞད་སྒྲའི་སྒོ་ནས་བསྟོད་པ་ནི། ཕྱག་འཚལ་རབ་ཏུ་དགའ་བ་བརྗིད་པའི། །དབུ་རྒྱན་འོད་ཀྱི་ཕྲེང་བ་སྤེལ་མ། །ཞེས་འཕགས་མའི་རྒྱན་གྱིས། རབ་ཏུ་དགའ་བ་དད་ཅིང་མོས་པའི་འདུལ་བྱ་རྣམས་ཀྱི་འདོད་པ་བསྐངས་ནས་བརྗིད་པ་ནི། འོད་གཞན་ཟིལ་གྱིས་གནོན་པའི་འོད་ཀྱི་ཕྲེང་བ་ནོར་བུའི་གཙུག་རྒྱན་དང་སྤེལ་མའོ། །

[Block 69]
སྔགས་ཀྱི་བཞད་སྒྲ་རབ་ཏུ་བཞད་པ་ཏཱ་ར་ཡིས་བདུད་དང་། འཇིག་རྟེན་གྱི་ལྷ་ཆེན་བརྒྱད་དབང་དུ་མཛད་མའོ། །

[Block 70]
འདི་ལ་མྱ་ངན་སེལ་བའི་སྒྲོན་མ་ཞེས་འབྱུང་ངོ་། །

[Block 71 [HEADING]]
###### **བཞི་པ་ཕྱོགས་སྐྱོང་བཅུས་འཕྲིན་ལས་སྒྲུབ་པའི་སྒོ་ནས་བསྟོད་པ།** ^2-2-2-1-2-4-0

[Block 72]
བཞི་པ་ཕྱོགས་སྐྱོང་བཅུས་འཕྲིན་ལས་སྒྲུབ་པའི་སྒོ་ནས་བསྟོད་པ་ནི། ཕྱག་འཚལ་ས་གཞི་སྐྱོང་བ་ནི། ཕྱོགས་སྐྱོང་བཅུ་ཡིན་ལ། ཚོགས་རྣམས་ནི། འཁོར་དང་བཅས་པ་ཐམས་ཅད་འགུགས་པར་ནུས་མ་སྟེ། དེ་ཐམས་ཅད་བཀུག་ནས་འཕྲིན་ལས་སྒྲུབ་ཏུ་འཇུག་པའོ། །

[Block 73]
ཁྲོ་གཉེར་གཡོ་བ་ནི། ཁྲོ་མོར་བཞུགས་པའི་ཐུགས་ཀའི་ཧཱུཾ་ཡིག་གི་འོད་ཟེར་གྱི་བདེ་བས། འཕོངས་ཞིང་སྡུག་བསྔལ་གྱིས་གཟིར་བ་ཐམས་ཅད་སྡུག་བསྔལ་དེ་ལས་རྣམ་པར་སྒྲོལ་བར་མཛད་མའོ། །འདི་ལ་དགུག་པའི་སྒྲོལ་མ་ཞེས་འབྱུང་ངོ་། །

[Block 74 [HEADING]]
###### **ལྔ་པ་དབུ་རྒྱན་གྱི་སྒོ་ནས་བསྟོད་པ།** ^2-2-2-1-2-5-0

[Block 75]
ལྔ་པ་དབུ་རྒྱན་གྱི་སྒོ་ནས་བསྟོད་པ་ནི། ཕྱག་འཚལ་ཟླ་བའི་རྩེ་མོས་དབུ་བརྒྱན། །བརྒྱན་པ་ཐམས་ཅད་ཤིན་ཏུ་འབར་མ། །ཞེས་པ་དབུ་རྒྱན་དངོས་ཏེ། ཟླ་བའི་རྩེ་མོ་སྟེ། ཚེས་གཅིག་གི་ཟླ་བས་དབུ་བརྒྱན་ཅིང་།
--- END BLOCKS ---
