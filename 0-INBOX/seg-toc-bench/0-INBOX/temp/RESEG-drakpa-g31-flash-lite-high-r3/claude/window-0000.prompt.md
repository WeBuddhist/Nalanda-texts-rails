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
[Block 1]
༄༅། །སྒྲོལ་མ་ཕྱག་འཚལ་ཉི་ཤུ་རྩ་གཅིག་གི་བསྟོད་པའི་རྣམ་བཤད་གསལ་བའི་འོད་ཟེར་ཞེས་བྱ་བ་བཞུགས་སོ། །

[Block 2 [HEADING]]
## མཆོད་བརྗོད། ^I-0

[Block 3]
༄༅། །ན་མོ་བུདྡྷ་ཡ།

[Block 4 [HEADING]]
## བསྟོད་པའི་ས་བཅད། ^II-0

[Block 5]
བསྟོད་པ་འདི་ལ་དོན་གཉིས་ཏེ། བསྟོད་པ་དངོས་དང་ཕན་ཡོན་ནོ། །

[Block 6]
དང་པོ་ལ་གསུམ་སྟེ། སྐུའི་རྣམ་པས་ལོངས་སྐུའི་སྒོ་ནས་བསྟོད་པ་དང༌། ཆོས་སྐུའི་སྒོ་ནས་བསྟོད་པ་དང་། ཕྲིན་ལས་ཀྱི་སྒོ་ནས་བསྟོད་པའོ། །

[Block 7]
དང་པོ་ལ་གསུམ། མཚན་གྱི་སྒོ་ནས་ལོ་རྒྱུས་བསྟན་པ་དང༌། སྐུའི་རྣམ་པ་དང་། རྒྱན་དང་ཆ་ལུགས་སོ། །

[Block 8]
བར་མ་གཉིས་ལ། ཞི་བའི་སྐུའི་སྒོ་ནས་བསྟོད་པ་དང་། ཁྲོ་མོའི་སྐུའི་སྒོ་ནས་བསྟོད་པའོ། །

[Block 9]
དང་པོ་ལ་གསུམ། འོད་ཟེར་གྱི་སྒོ་ནས་དང་། ཕྱག་མཚན་དང་ཡིད་ཅན་གྱི་སྒོ་ནས་དང༌། སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔས་བསྐུར་བའི་སྒོ་ནས་བསྟོད་པའོ། །

[Block 10]
ཁྲོ་མོའི་སྐུའི་སྒོ་ནས་བསྟོད་པ་ལ་གསུམ། མཐུའི་སྒོ་ནས་དང་། འཇིག་རྟེན་པའི་ཆེན་པོ་རྣམས་ཀྱི་བསྟོད་པའི་སྒོ་ནས་དང་། ཕྲིན་ལས་ཀྱི་སྒོ་ནས་བསྟོད་པའོ། །

[Block 11]
དེ་ལ་གཉིས། ཐུན་མོང་གི་ཕྲིན་ལས་དང་། ཐུན་མོང་མ་ཡིན་པའི་སྒོ་ནས་བསྟོད་པའོ། །

[Block 12]
རྒྱན་དང་ཆ་ལུགས་ཀྱི་སྒོ་ནས་བསྟོད་པ་ལ་བཞི། ཞི་བའི་ཆ་ལུགས་ཀྱི་སྒོ་ནས་དང་། དྲག་པོའི་ཆ་ལུགས་ཀྱི་སྒོ་ནས་དང་། ཐུན་མོང་གི་དབུ་རྒྱན་གྱི་སྒོ་ནས་དང་། དྲག་པོའི་ཆ་ལུགས་ཀྱི་སྒོ་ནས་བསྟོད་པའོ། ། དང་པོ་ལ་གཉིས། ཕྱག་མཚན་དང་དབུ་རྒྱན་ནོ། །

[Block 13]
དྲག་པོའི་འོག་མ་ལ་གསུམ། འོད་ཟེར་དང༌། བཞུགས་ཚུལ་དང༌། ཕྱག་མཚན་གྱི་སྒོ་ནས་བསྟོད་པའོ། །

[Block 14]
སྤྱི་དོན་གསུམ་པ་ཕྲིན་ལས་ཀྱི་སྒོ་ནས་བསྟོད་པ་ལ་དྲུག གསང་སྔགས་ཀྱི་སྒོ་ནས་དང་། དབང་གི་སྒོ་ནས་དང་། དུག་ཞི་བའི་སྒོ་ནས་དང་། བར་ཆད་སེལ་བའི་སྒོ་ནས་དང༌། རིམས་ནད་སེལ་བའི་སྒོ་ནས་དང༌། མི་མཐུན་པ་སེལ་བའི་སྒོ་ནས་བསྟོད་པའོ། །

[Block 15]
སྤྱི་དོན་གཉིས་པ་ཕན་ཡོན་ལ་བཞི། བསམ་པའི་ཁྱད་པར་དང་། དུས་ཀྱི་ཁྱད་པར་དང་། ཕན་ཡོན་དངོས་རྒྱས་པར་བཤད་པ་དང་། གྲངས་ཀྱི་སྒོ་ནས་ཕན་ཡོན་བསྡུས་ཏེ་རྒྱས་པར་བཤད་པའོ། །

[Block 16]
དགེ་བསྙེན་གྲགས་པ་རྒྱལ་མཚན་གྱིས་སྦྱར་བའོ། །

[Block 17 [HEADING]]
## བསྟོད་པ་དངོས། ^1-0

[Block 18]
ཨོཾ་རྗེ་བཙུན་མ་འཕགས་མ་སྒྲོལ་མ་ལ་ཕྱག་འཚལ་ལོ། །

[Block 19]
ཕྱག་འཚལ་སྒྲོལ་མ་ནི་འཁོར་བའི་དུ་ཁ་ལས་སྒྲོལ་མ། མྱུར་མ་ནི་སེམས་ཅན་གྱི་དོན་ལ་མྱུར་མ། དཔའ་མོ་ནི་ཉོན་མོངས་པ་འཇོམས་པས་དཔའ་མོ། སྤྱན་ནི་སྐད་ཅིག་གློག་དང་འདྲ་མ། །ཞེས་པ་ནི། འོད་གསལ་བའི་དཔེའོ། །

[Block 20]
འཇིག་རྟེན་གསུམ་མགོན་ཆུ་སྐྱེས་ཞལ་གྱི། །ཞེས་པ་ནི། འཇིག་རྟེན་གསུམ་གྱི་མགོན་པོ་སྤྱན་རས་གཟིགས། ཆུ་སྐྱེས་ཞལ་གྱི་ཞེས་པ་ནི། དེའི་སྤྱན་ཆབ་ལས་བྱུང་བའི། པད་མའམ་ཨུཏྤལ། གེ་སར་བྱེ་བ་ལས་ནི་བྱུང་མ། །ཞེས་པ་ནི། པདྨ་ཁ་བྱེ་བ་ལས་སྒྲོལ་མ་བྱུང་བའོ། ། ཕྱག་འཚལ་སྟོན་ཀའི་ཟླ་བ་ཀུན་ཏུ། །ཞེས་པ་ནི། འོད་དཀར་བའི་དཔེའོ། །གང་བ་ནི་ཉ་གང་བ་ལྟ་བུའོ། །བརྒྱ་ནི་བརྩེགས་པའི་ཞལ་མ། །ཞེས་པ་ནི། ཟླ་བ་ཉ་གང་བ་དེ་ཡང་བརྒྱ་ཕྲག་དུ་མ་སྤུངས་པ་ཙམ་གྱི་ཞལ་ལོ། །སྐར་མ་སྟོང་ཕྲག་ཚོགས་པ་རྣམས་ཀྱིས། །རབ་ཏུ་ཕྱེ་བའི་འོད་རབ་འབར་མ། །ཞེས་པ་ནི། དེ་གཉིས་འོད་ཟེར་དཔག་ཏུ་མེད་པ་འཕྲོ་བའི་དཔེའོ། །

[Block 21]
ཕྱག་འཚལ་གསེར་སྔོ་ནི་ཁ་དོག་གསེར་བཙོ་མའི་འོད་ལྟར་གསལ་བའོ། །

[Block 22]
ཆུ་ནས་སྐྱེས་ཀྱི་ཞེས་པ་ནི། ཕྱག་མཚན་པད་མའོ། །

[Block 23]
པདྨས་ཕྱག་ནི་རྣམ་པར་བརྒྱན་མ། །ཞེས་པ་ནི། ཕྱག་གཡོན་ན་པདྨ་བསྣམས་པའོ། །

[Block 24]
སྦྱིན་པ་ནི་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པའོ། །བརྩོན་འགྲུས་ནི་བརྩོན་འགྲུས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའོ། །

[Block 25]
དཀའ་ཐུབ་ནི་ཚུལ་ཁྲིམས། ཞི་བ་ནི་ཉོན་མོངས་པ།

[Block 26]
བཟོད་པ་ནི་བཟོད་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པའོ། །བསམ་གཏན་ནི་བསམ་གཏན་གྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའོ། །

[Block 27]
སྤྱོད་ཡུལ་ཉིད་མ་ནི་ཤེས་རབ་སྟེ། ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་པོ་དེ་སྤྱད་པ་ལས་སྒྲོལ་མའི་སྐུ་ཐོབ་སྟེ། དེ་མཚན་པ་ལས་ཨུཏྤལ་མཚོན་པའོ། ། ཕྱག་འཚལ་དེ་བཞིན་གཤེགས་པའི་གཙུག་ཏོར། །ཅེས་པ་ནི། དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་དབུའི་གཙུག་ཏོར་ལྟ་བུའོ། །

[Block 28]
མཐའ་ཡས་རྣམ་པར་རྒྱལ་བ་སྤྱོད་མ། །ཞེས་པ་ནི། བདུད་དང་དགྲ་ལ་སོགས་པ་ཕྱིར་རྒོལ་བ་ཐམས་ཅད་ལས་རྣམ་པར་རྒྱལ་བར་སྤྱོད་པའོ། །

[Block 29]
མ་ལུས་ཕ་རོལ་ཕྱིན་པ་ཐོབ་པའི། །ཞེས་པ་ནི། ས་བཅུ་མ་ལུས་པའི་ངོ་བོ་ཕ་རོལ་ཕྱིན་པ་བཅུ་ཐོབ་པའོ། །

[Block 30]
རྒྱལ་བའི་སྲས་ཀྱིས་ཤིན་ཏུ་བརྟེན་མ། །ཞེས་པ་ནི། རྒྱལ་བའི་སྲས་ནི་བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་དོ། །ཤིན་ཏུ་བརྟེན་མ་ཞེས་པ་ནི། དེ་རྣམས་ཀྱིས་ཕུད་དུ་ཁུར་བའོ། ། ཕྱག་འཚལ་ཏུཏྟཱ་ར་ཧཱུཾ་ཡི་གེས། །ཞེས་པ་ནི། ཏུཏྟཱ་རེ་ཧཱུཾ་ཞེས་སྔགས་སོ། །

[Block 31]
ཡི་གེ་ཞེས་པ་སྔགས་ཀྱི་ཡི་གེ་དེ་རྣམས་ཀྱི་མཐུ་དང་འོད་ཟེར་གྱིས་སོ། །

[Block 32]
འདོད་དང་ཕྱོགས་དང་ནམ་མཁའ་གང་མ། ཞེས་པ་ནི་འདོད་ཁམས་དང་གཟུགས་ཁམས་དང་གཟུགས་མེད་ཀྱི་ཁམས་གང་བའོ། །འཇིག་རྟེན་བདུན་པོ་ཞབས་ཀྱིས་མནན་ཏེ། །ཞེས་པ་འདོད་ཁམས་ཀྱི་འགྲོ་བ་ལྔ་དང་། གཟུགས་ཁམས་དང་དྲུག གཟུགས་མེད་ཁམས་དང་བདུན་མནན་པའོ། །ལུས་པ་མེད་པར་འགུགས་པར་ནུས་མ། །ཞེས་པ་ནི། ལུས་པ་མེད་པ་ནི་སེམས་ཅན་གྱི་དོན་མ་ལུས་པར་བྱེད་པའོ། །

[Block 33]
འགུགས་པར་ནུས་མ་ནི། རྒྱལ་པོ་ལ་སོགས་དབང་དུ་སྡུད་ནུས་པའོ། ། ཕྱག་འཚལ་བརྒྱ་བྱིན་མེ་ལྷ་ཚངས་པ། །རླུང་ལྷ་སྣ་ཚོགས་དབང་ཕྱུག་མཆོད་མ། །ཞེས་པ་ནི། ལྷའི་དབང་པོ་བརྒྱ་བྱིན་དང༌། མེ་ལྷ་དང་ཚངས་པ་དང་། རླུང་ལྷ་དང་། དེ་རྣམས་ཀྱི་བདག་པོར་གྱུར་པ་དབང་ཕྱུག་ཆེན་པོས་ཞབས་ལ་མཆོད་པ་འབུལ་བའོ། །འབྱུང་པོ་རོ་ལངས་དྲི་ཟ་རྣམས་དང་། །གནོད་སྦྱིན་ཚོགས་ཀྱིས་མདུན་ནས་བསྟོད་མ། །

[Block 34 [VERSE]]
ཞེས་པ་ནི་འབྱུང་པོ་ནི་ཚོགས་བདག་ལ་སོགས་པའོ། །
རོ་ལངས་ནི་དབང་ཕྱུག་ཆེན་པོ་ལ་སོགས་པའོ། །
དྲི་ཟ་ནི་ཟུར་ཕུད་ལྔ་པ་ལ་སོགས་པའོ། །
གནོད་སྦྱིན་ནི་རྣམ་ཐོས་སྲས་ལ་སོགས་པའོ། །

[Block 35]
ཚོགས་ཀྱིས་ཞེས་པ་དེ་ལ་སོགས་པ་ལྷ་སྲིན་སྡེ་བརྒྱད་ཀྱིས་མདུན་ནས་བསྟོད་པའོ། ། ཕྱག་འཚལ་ཏྲད་ཅེས་བྱ་དང་ཕཊ་ཀྱིས། །ཕ་རོལ་འཁྲུལ་འཁོར་རབ་ཏུ་འཇོམས་མ། །ཞེས་པ་ནི། དྲག་པོའི་གསུང་གིས་གཞན་གྱིས་བྱས་པའི་སྦྱོར་བ་ངན་པ་བཤིག་ཅིང་ཕྱིར་བཟློག་པའོ། །

[Block 36]
གཡས་བསྐུམ་གཡོན་བརྐྱང་ཞེས་པ་ནི་བཞུགས་ཚུལ་ལོ། ཞབས་ཀྱིས་མནན་ཏེ། ཞེས་པ་ནི། གོང་དུ་བཤད་པའི་དོན་ཏོ། །མེ་འབར་འཁྲུགས་པ་ཤིན་ཏུ་འབར་མ། །ཞེས་པ་ནི། མེ་འབར་བའི་དབུས་ན་བསྒྱིངས་ནས་བཞུགས་པའོ། ། ཕྱག་འཚལ་ཏུ་རེ་འཇིགས་པ་ཆེན་མོས། །ཞེས་པ་ནི། ཏུ་རེའི་འཇིགས་པས་བདུད་ཐམས་ཅད་སེལ་བ་སྟེ། བདུད་སྐྲག་པར་བྱེད་པས་འཇིགས་པ་ཆེན་མོའོ། །བདུད་ཀྱི་དཔའ་བོ་རྣམ་པར་འཇོམས་མ། །ཞེས་པ་ནི། དཔའ་བོ་ནི་ཉོན་མོངས་པའི་བདུད་དོ། །དེ་བཅོམ་པས་གསུམ་པོ་ཞོར་ལ་འཇོམས་སོ། །ཆུ་སྐྱེས་ཞལ་ནི་ཁྲོ་གཉེར་ལྡན་མཛད། །ཅེས་པ་ནི། ཆུ་སྐྱེས་ཞལ་ནི། པདྨ་ཁ་བྱེ་བ་ལྟར་ཡིད་དུ་འོང་བའི་དཔལ་མོའི་ཞལ་ལོ། །

[Block 37]
ཁྲོ་གཉེར་ལྡན་མཛད་ནི། ཁྲོ་མོར་བཞུགས་པའོ། །

[Block 38]
དགྲ་བོ་ཐམས་ཅད་མ་ལུས་གསོད་མ། །ཞེས་པ་ནི། མི་མཐུན་པའི་ཕྱོགས་ཉོན་མོངས་པ་ལ་སོགས་པ་ཐམས་ཅད་གསོད་པའོ། །

[Block 39]
ཕྱག་འཚལ་དཀོན་མཆོག་གསུམ་མཚོན་ཕྱག་རྒྱའི། །སོར་མོས་ཐུགས་ཀར་རྣམ་པར་བརྒྱན་མ། ཞེས་པ་ནི། གཡོན་པའི་ཕྱག་མཐེབ་སྲིན་གྱིས་པདྨ་ཐུགས་ཀར་བསྣམས་པས་བརྒྱན་པའོ། །

[Block 40]
སོར་མོ་གསུམ་བརྐྱངས་པ་ནི་དཀོན་མཆོག་གསུམ་མཚོན་པའི་བརྡའོ། །
--- END BLOCKS ---
