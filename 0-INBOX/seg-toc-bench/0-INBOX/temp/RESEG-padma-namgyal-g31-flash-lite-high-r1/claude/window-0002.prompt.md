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
[Block 71 [HEADING]]
## མཇུག་ཕན་ཡོན། ^2-0

[Block 72]
གསུམ་པ་མཇུག་ཕན་ཡོན་གྱི་དོན་ནི། བསྟོད་ཡུལ་ལྷ་མོ་ལ་བསྟོད་པ་པོ་གུས་པ་ཡང་དག་ལྡན་པའི། བློ་ལྡན་གང་གིས་བསྟོད་ཚུལ་སེམས་རབ་ཏུ་དང་བར་བསྟོད་པའི་རྒྱུད་ཚིག་བརྗོད་པས། བསྟོད་པའི་དུས་ནི་འདྲེ་གདོན་མུན་ནག་ལ་འཁྲི་བས་གནོད་སྐྱེལ་བ་མུན་རུབ་སྲོད་ཀྱི་དུས་དང་ཐོ་རངས་ལྷ་རྣམས་ལུང་བསྟན་གྱི་དུས་སུ་མལ་ནས་ལངས་པར་བྱས་ཏེ། འཕགས་མ་དྲན་པས་ཀྱང་ནི་མི་འཇིགས་པའི་མཐུ་དང་སྤོབས་པ་ཐམས་ཅད་རབ་སྟེར། རྒྱུ་སྡིག་པ་ཐམས་ཅད་རབ་ཏུ་ཞི་བ། འབྲས་བུ་ནད་གདོན་བྱུར་དང་ཆག་སྒོ་ངན་པ་དང་ངན་སོང་གསུམ་གྱི་སྐྱེ་སྒོ་ཁེགས་པས་ངན་འགྲོ་ཐམས་ཅད་འཇོམས་པ་ཉིད་དོ། །

[Block 73]
རྒྱལ་བ་བྱེ་བ་ཕྲག་བདུན་རྣམས་ཀྱིས་དངོས་ཉམས་དང་རྨི་ལམ་ཅི་རིགས་པར། མྱུར་དུ་རླུང་སེམས་སྣང་སྲིད་ཐམས་ཅད་ལ་དབང་དུ་བསྒྱུར་བའི་དབང་ནི་བསྐུར་བར་འགྱུར་ལ། ཚེ་འདི་ལས་ཆེ་བའི་ཡོན་ཏན་ཐམས་ཅད་ཉིད་ནི་འཐོབ་ཅིང༌། ཕྱི་མ་སངས་རྒྱས་གོ་འཕང་མཐར་ཐུག་དེར་འགྲོ། གནས་སྐབས་བསྟོད་པ་པོ་དེ་ཡི་དུག་ནི་དྲག་པོ་གཉན་དུག་ལྟ་བུ་དང་ཆེན་པོ་སྲིན་དུག་དང་གླང་ཐབས་ལྟ་བུ། བརྟེན་པ་སེམས་ཅན་རྣམས་ལ་འབྱུང་བ་འཁྲུགས་རུང་གི་ཚུལ་དུ་གནས་པའམ་གཞན་ཡང་ཀླུ་དང་ཁྱི་སྨྱོན་སྦྲུལ་ལ་སོགས་པ་འགྲོ་བ་སེམས་ཅན་གྱི་གནོད་པའི་དུག་དང༌། གཞན་ཡང་བོང་ང་ནག་པོ་སོགས་ལྷན་སྐྱེས་ཀྱི་དུག་རྫས་དང་ར་མཆིན་དང་ཁྱི་རོ་རུལ་བ་སོགས་སྦྱར་དུག་དང་ར་ཤ་འཁྱག་པ་སོགས་གྱུར་དུག་གི་རྫས་རྣམས་ཟོས་པ་དང་ནི་འཐུངས་པ་ཉིད་ཀྱང༌། སྔར་རྗེ་བཙུན་མའི་བསྟོད་པ་འབུམ་ཐེར་ལྟ་བུ་ལེགས་པར་གྲུབ་ཡོད་ན་ཕྱིས་རིག་སྔགས་དྲན་པས་ཀྱང་ནི་རབ་ཏུ་སེལ་ཞིང་བདུད་རྩིར་བསྒྱུར་བ་ཉིད་འཐོབ། གདོན་དང་རིམས་དང་དུག་གིས་གཟིར་བའི། སྡུག་བསྔལ་ཚོགས་ནི་རྣམ་པར་སྤོང་བའི་ཞི་བདེ་དགའ་བ་ཆེན་པོ་ལུས་སེམས་ལ་འཐོབ་སྟེ། རང་དོན་མ་ཟད་སེམས་ཅན་གཞན་པ་རྣམས་ལ་དོན་འགྲུབ་དགོས་ན་དེ་ལྟར་འགྲུབ་པ་ཡང་ངོ་། རྒྱུན་དུ་བསྟོད་པའི་དུས་སུ་ཚར་གཉིས་དང་གསུམ་དང་བདུན་དུ་མངོན་པར་བརྗོད་ན། བུ་འདོད་པས་ནི་བུ་སློབ་བྲན་གཡོག་སོགས་ཐོབ་པར་འགྱུར་ཞིང་། ནོར་འདོད་པས་ནི་གང་འདོད་ཀྱི་ནོར་རྣམས་ཉིད་འཐོབ། མདོར་ན་ཡིད་དུ་འོང་བའི་ཡིད་ལ་འདོད་པ་ཐམས་ཅད་ཐོབ་པར་འགྱུར་ཏེ། བགེགས་རྣམས་མེད་ཅིང་སོ་སོར་འཇོམས་འགྱུར་ཅིག ། མཐར་བཅོམ་ལྡན་འདས་མ་སྒྲོལ་མ་ལ་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་རྣམ་པར་སྣང་མཛད་ཆེན་པོ་དེ་ཉིད་ཀྱིས་བསྟོད་པ་གསུངས་པ་རྫོགས་སོ། །

[Block 74 [HEADING]]
## མཛད་བྱང། ^3-0

[Block 75 [HEADING]]
## མཇུག་བྱང། ^a-0

[Block 76 [HEADING]]
### མཛད་བྱང། ^a-1-0

[Block 77]
ཞེས་རྩ་རྒྱུད་རྒྱུད་ཀྱི་རྒྱལ་པོ་རྟོགས་པ་བདུན་བརྒྱ་པ་དང་། བཤད་རྒྱུད་ལས་སྣ་ཚོགས་པའི་རྒྱུད་གཉིས་ཀ་ནས་བསྡུས་རྒྱུད་ཀྱི་ཚུལ་དུ་བྱུང་བ་ཕན་ཡོན་དང་བཅས་པའི་མཆན་འདི་ཡང་ཨརྨེ་རིག་འཛིན་རྣམ་རྒྱལ་ནས་ནན་བསྐུལ་ལྟར་ལྡོམ་བུ་བ་པདྨ་རྣམ་པར་རྒྱལ་བས་གུས་པར་བྲིས་ཏེ་བདག་གཞན་རྗེས་སུ་འཛིན་པའི་རྒྱུར་གྱུར་ཅིག། །།
--- END BLOCKS ---
