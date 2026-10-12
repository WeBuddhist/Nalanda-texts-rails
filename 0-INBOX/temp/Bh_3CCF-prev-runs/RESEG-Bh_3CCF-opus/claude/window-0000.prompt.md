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
[Block 1 [HEADING]]
## ༄༅། །སྒྲོན་མ་གསལ་བར་བྱེད་པའི་དཀའ་བ་བཏུས་པའི་འགྲེལ་པ།

[Block 2 [HEADING]]
## མཆོད་བརྗོད། ^I-0

[Block 3]
༄༅༅།།རྒྱ་གར་སྐད་དུ། པྲ་དཱེ་པོ་དྱོ་ཏ་ན་བི་ས་མ་པཉྩི་ཀཱ་ནཱ་མ། བོད་སྐད་དུ། སྒྲོན་མ་གསལ་བར་བྱེད་པའི་དཀའ་བ་བཏུས་པའི་འགྲེལ་བ་ཞེས་བྱ་བ། སངས་རྒྱས་ལ་ཕྱག་འཚལ་ལོ།།

[Block 4 [HEADING]]
## ལེའུ་དང་པོ། ^1-0

[Block 5]
དེ་ལ་རིམ་པ་གཉིས་པོ་ཞེས་བྱ་བ་ནི་བསྐྱེད་པ་དང་རྫོགས་པའི་རིམ་པ་གཉིས་པའོ།།

[Block 6]
ཇི་སྲིད་ཅེས་བྱ་བ་ནི་ཌྷད་དྷ་ཡ་ར་ལ་རྣམས་ལན་གཉིས་སུ་བཀླགས་པ༌[^1]དང་བཅས་པའི་ཀ་ཚོགས་རྣམས་སོ།།

[Block 7]
ཨི་ཐ་ཞེས་བྱ་བ་དེའི་དོན་ནི་ཨ་ཚོགས་རྣམས་སུ་ཤེས་པར་བྱའོ།།

[Block 8]
དེ་ཉིད་ནི་ལུས་ལ་སོགས་པ་འཛིན་པ་ཤེས་རབ་དང་ཐབས་ཀྱི་རང་བཞིན་གྱིས་གཟུང་བའོ།།

[Block 9]
འདུལ་བའི་སྡོམ་པར་ལྡན་མཐོང་བ།།ཞེས་བྱ་བ་ནི་དགེ་སློང་ལ་སོགས་པའི་སྡོམ་པ་ཅན་དུ་གདུལ་བྱས་མཐོང་བའོ།།

[Block 10]
འབྲས་བུ་འདོད་པས་ཞེས་བྱ་བ་ནི་སྐྱེ་བོ་གདུལ་བ་ཅན་གྱི༌[^2]དགོས་པ་ལ་བྱ་སྟེ། ཀུན་རྫོབ་ཀྱི་འབྲས་བུའོ།།

[Block 11]
སྙིང་པོ་སྦས་པ་འདི་ལ་ཡོད་ཅེས་བྱ་བ་ནི་འདོད་ཆགས་ལ་སོགས་པའི་རང་བཞིན་ཇི་ལྟ་བ་བཞིན་དུ་ཡོངས་སུ་ཤེས་པས་གྲོལ་བར་འགྱུར་ཏེ། དེ་སྟོན་པར་བྱེད་པ། འདོད་ཆགས་ཆོས་ནི་རབ་སྟོན་དང་།།ཞེས་པ་གསུངས་སོ།།

[Block 12]
མ་ཞེས་བྱ་བ་ནི་ཆོས་རྣམས་རབ་ཏུ་མང་པོ་ཐོབ་པའོ།།

[Block 13]
ལྷག་པར་ཞེས་བྱ་བ་ནི་ལྷག་པར་གཟུང་བའོ།།

[Block 14]
བུམ་པའི་རས་བལ་ས་བོན་འདྲ།།ཞེས་བྱ་བ་ནི་བུམ་པ་ཆུང་ངུ་རས་བལ་གྱི་ས་བོན་གྱིས་གང་བར་བྱས་པ་བངས་ནས་ཤིན་ཏུ་འཕེལ་ན་སླར་མི་ཐོན་པ་ལྟར་གསལ་བར་སྟོན་མི་ནུས་པའོ།།

[Block 15]
བློ་ཁ་མི་འབྱེ་ལ་ཞེས་བྱ་བ་ནི་ཤེས་རབ༌[^3]བརྟན་པ་ལ་སོགས་པས་སྙིང་སྟོང་པའོ།།

[Block 16]
ཉན་ཞེས་བྱ་བ་ནི་ཐོས་པ་དྲི་མ་མེད་པའོ།།

[Block 17]
རྒྱུད་གཅིག་པ་ནི་ཟུང་དུ་འཇུག་པས་ཆོས་ཀྱི་དེ་ཁོ་ན་ཉིད་བཤད་པར་བྱ་སྟེ་ལས་དང་པོ་པ་ལ་བཤད་པ་དང་། སྤྲོས་པ་མེད་པའི་རྣལ་འབྱོར་བཤད་པའོ།།

[Block 18]
བཤད་པ་རྣམ་པ་གཉིས་བྱའོ་ཞེས་བྱ་བ་ནི་ཚོགས་པ་ལ་བཤད་པ་དང་། སློབ་མ་ལ་བཤད་པའོ།།

[Block 19]
དེ་རྣམས་ཀྱིས་ཞེས་བྱ་བ༌[^4]ནི་རྒྱན་དྲུག་པོ་རྣམས་ཀྱིས་བདེན་པ་གཉིས་པོ་ནི་ཚིག༌[^5]ངེས་པར་བྱེད་པའོ།།

[Block 20]
དེ་ནི་རྒྱན་བདུན་པ་སྟེ། དེས་ཟུང་དུ་འཇུག་པ་མཐར་ཐུག་པ་སྒྲུབ༌[^6]པའོ།།

[Block 21]
འདི་སྐད་བདག་གི༌[^7]ཞེས་བྱ་བ་ལ་སོགས་པས་ནི། གླེང་གཞི་སྟོན་པ་ཡིན་ནོ།།

[Block 22]
རིམ་པ་ཞེས་བྱ་བ་ནི་འདིར་རིམ་པ་ལྔ་པའོ།།

[Block 23]
བཤད་ཚུལ་རྣམ་པ་བཞི་པོ་ནི་ཚིག་གི་དོན་དང་། སྤྱིའི་དོན་དང་། སྦས་པ་དང་། མཐར་ཐུག་པ་སྟེ། བཅུ་པོ་ཙམ་གྱིས་སྤྱོད་པ་དོར་བར་བྱ་སྟེ། ཇི་ལྟ་བའི་བདེ་བར་མི་འགྱུར་བ་དང་། འཇིག་རྟེན་ན་སྡུག་བསྔལ་གྱི་རྒྱུ་མི་དགེ་བ་བཅུ་པོ་ནི་ལྟུང་བར་བྱེད་པས་སོ།།

[Block 24]
དེ་ལ་རབ་ཏུ་མ་ཆགས་པར་གྱུར་པ་དང་མི་དགེ་བ་བཅུ་པོ་བཅོམ་པ་ཡང་དག་པའི་སྐྱེ་བ་ལེན་ནོ།།

[Block 25 [VERSE]]
ཆ་གཉིས་པ་ནི་ཡི་གེ་ཨཱཿརིང་པོའོ། །
དགུ་པས་བརྗོད་པ་ནི་ཡི་གེ་ཨོ་ཡིན་ནོ། །
དང་ནི་བསྡུ་བ་སྟེ་ཡི་གེ་ཨཾ་དང་ཨཱཿའོ། །

[Block 26]
སུམ་ཅུ་པ་དང་བཅུ་པ་ནི་ཡི་གེ་ཧ་ཡིན་ནོ།།

[Block 27]
ལྔ་པའི་ས་བོན་ནི་ཡི་གེ་ཨུ་ཡིན་ནོ།།

[Block 28]
ཆ་གཉིས་པ་ལ་ལྔ་པ་དྲུག་པའི་ས་བོན་དུ་བྱས་པས་ཕྱེ་ན་དེར་འགྱུར་རོ།།

[Block 29]
ཁོང་པར་སྤྲོས་ཞེས་བྱ་བ་ནི་ཆོས་ཀྱི་འབྱུང་གནས་སུ་རྣམ་པར་སྤྲོས་པའོ།།

[Block 30]
ཨེ་ནི་ཤེས་རབ་ཅེས་བྱ་བ་ནི་བློ་དང་སྣང་བའི་ཤེས་པའོ།།

[Block 31]
སྣང་བ་མཆེད་པ་རང་ཉིད་ནི་རིག་ཆེན་ནོ།།

[Block 32]
རྩ་བ་ནི་སྣང་བ་ཉེ་བར་ཐོབ་པའི་རྒྱུ་སྟེ། ཐོག་མའི་དུས་སོ།།

[Block 33]
དེ་དག་ཀྱང༌[^8]སླར་བཟློག་པས་ཇི་ལྟ་བ་བཞིན་དུ་སྣང་བའི་འབྲས་བུ་གཉིས་པོར་སྦྱར་བས་རྣམ་པར་ཤེས་པ་གཉིས་པ་བལྟ་བར་བྱའོ།།

[Block 34 [VERSE]]
རྟག་ཏུ་འགྲོ་ལ་གནས་པར་འགྱུར། །
ཞེས་བྱ་བ་ནི་སྲོག་རྟག་ཏུ་གནས་པའོ། །
གཟུགས་དང་ཆུ་དང་གཟུགས་ལས་ཚོར་བའོ། །

[Block 35]
ཚོར་བའི་ཕུང་པོ་དང་ལྡན་པ་ནི་རླུང་ངོ་།།རོལ་པས་ཞེས་བྱ་བ་ནི་འཇོམས་པའོ།།

[Block 36]
རྣམ་པར་རོལ་ཞེས་བྱ་བ་ནི་རྣམ་པར་སྤྲུལ་བར་བྱའོ།།

[Block 37]
རྣམ་པར་འཕྲུལ་ཞེས་བྱ་བ་ནི་སྤྲུལ་བར་བྱེད་པའོ།།

[Block 38]
རྡོ་རྗེ་གསུམ་པོ་དམ་ཚིག་མཆོག།

[Block 39]
ཅེས་བྱ་བ་ནི་བྷ་གའོ། །

[Block 40]
ཡེ་ཤེས་དེ་བཞིན་གཤེགས་པ་ཀུན།།ཞེས་བྱ་བ་ནས། འགྲོ་སྙིང་རྣམ་དག་ཅེས་བྱ་བ་ནི་བྷ་གའི་ཁྱད་པར་རོ།།
--- END BLOCKS ---
