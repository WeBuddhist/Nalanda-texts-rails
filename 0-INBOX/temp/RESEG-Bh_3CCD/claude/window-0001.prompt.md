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

━━━ TOPIC SHIFT vs CONTINUATION (from the editors' corrections) ━━━

The editors' blocks are large (median ≈ 55 syllables; whole explanations of
100–250 syllables are normal). A sentence end is NOT a boundary. Inside one
explanation they cut only where the commentary turns to something new:
  START a new block at   "ཡང་ན་ …" (an alternative explanation)
                         "ཁ་ཅིག་ …", "གཞན་དག་ …" (another party's view)
                         "འོ་ན་ …" (the reply to an objection)
                         "དེ་སྐད་དུ་ …", "ཇི་སྐད་དུ་ …" (introducing a supporting quotation)
                         "དེ་ནས་ …" when it opens the next step of a procedure
                         "དཔེ་ …" / "དཔེར་ན་ …" when an example section begins
KEEP WITH the block before (merge into it):
                         "ད་ནི་ …" — a transitional "now …" line is not a new unit
                         (no heading or verse between them)
                         "ལེའུ་ … པའོ། །" — a chapter-closing line stays with the
                         explanation it closes
                         "ཞེས་ / ཅེས་ …" — the quotative closing the words just before it

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
རྫོགས་པའི་རིམ་པ་ནི་རྣམ་པ་ལྔ་སྟེ། རྡོ་རྗེ་བཟླས་པའི་རིམ་པ་དང་། སེམས་ལ་དམིགས་པ་ཐོབ་པའི་རིམ་པ་དང་། བདག་ལ་བྱིན་གྱིས་བརླབ༌[^18]པའི་རིམ་པ་དང་། མངོན་པར་བྱང་ཆུབ་པའི་རིམ་པ་དང་། ཟུང་དུ་འཇུག་པའོ། །

[Block 37]
དེ་ལ་དང་པོའི་སྦྱོར་བ་ལ་རྣམ་པ་བཞི་སྟེ། རྣལ་འབྱོར་དང་། རྗེས་སུ་རྣལ་འབྱོར་དང་། ཤིན་ཏུ་རྣལ་འབྱོར་དང་། རྣལ་འབྱོར་ཆེན་པོའོ། །

[Block 38]
རྣལ་འབྱོར་ལ་ནི་རྣམ་པ་བཅུ་སྟེ་སྙིང་རྗེ་ཆེན་པོ་མངོན་དུ་བྱ་བ་སྔོན་དུ་འགྲོ་བ་ཁྱད་པར་གྱི་གནས་ལ་བརྟེན་པ་དང་། བགེགས་བསྐྲད་པའི་བདག་ཉིད་ཅན་གནས་བསྲུང་བ་དང་། སྟོང་པ་ཉིད་ཀྱི་སྒོམ་པས་བདག་ཉིད་བསྲུང་བ་དང་། ཡེ་ཤེས་ཀྱི་ས་གཞི་བསྒོམ་པ་དང་། གཞལ་ཡས་ཁང་དང་། དེའི་ནང་དུ་པདྨ་དང་ཟླ་བ་དང་ཉི་མའི་གདན་ལ་གནས་པ་ལྷག་པར་མོས་པའི་དཀྱིལ་འཁོར་བསྒོམ་པ་དང་། དོན་དམ་པའི་དཀྱིལ་འཁོར་བསྒོམ་པ་དང་། གཞལ་ཡས་ཁང་གི་ནང་དུ་གདན་དགོད་པ་དང་། ཆོས་ཀྱི་དབྱིངས་ཀྱི་དེ་ཁོ་ན་ཉིད་བསྒོམ་པ་དང་། ཡི་གེ་གསུམ་ལས་སྐྱེས་པའི་དབུས་ཀྱི་གཙོ་བོ་བསྒོམ་པའོ། །

[Block 39]
རྗེས་སུ་རྣལ་འབྱོར་ནི་ཡེ་ཤེས་སེམས་དཔའི་དང་ཏིང་ངེ་འཛིན་སེམས་དཔའ་བསྒོམ་པའོ། །

[Block 40]
ཕུང་པོ་ཁམས་དང་སྐྱེ་མཆེད་བྱིན་གྱིས་རློབ་པ་ནི་ཤིན་ཏུ་རྣལ་འབྱོར་རོ། །

[Block 41]
སྐུ་དང་གསུང་དང་ཐུགས་བྱིན་གྱིས་རློབ་པའི་བདག་ཉིད་ཅན་ནི་རྣལ་འབྱོར་ཆེན་པོ་སྟེ། དང་པོའི་སྦྱོར་བའི་ཏིང་ངེ་འཛིན་ཏོ། །

[Block 42]
དཀྱིལ་འཁོར་རྒྱལ་བ་མཆོག་ནི་རྣམ་པ་བརྒྱད་དེ། ཕྱག་རྒྱའི་དབྱེ་བ་དང་། རིགས་ཀྱི་དབྱེ་བས་དེ་དག་ལ་དམིགས་པ་དང་། རྡོ་རྗེ་པདྨ་སྙོམས་པར་ཞུགས་པ་དང་། དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་རྗེས་སུ་འཇུག་པ་དང་། པདྨའི་ནང་དུ་དམ་ཚིག་གི་དཀྱིལ་འཁོར་དབྱུང་བ་དང་། སེམས་ཅན་གྱི་ཁམས་སྦྱང་བ་སྔོན་དུ་འགྲོ་བའི་ཕྱིར་སྤྲོ་བ་དང་། ཕྱིར་མི་ལྡོག་པའི་དབང་དང་རྒྱས་གཏབ་པ༌[^19]སྟེ་དཀྱིལ་འཁོར་རྒྱལ་བ་མཆོག་གི་ཏིང་ངེ་འཛིན་ཏོ། །

[Block 43]
ལས་ཀྱི་རྒྱལ་བ་མཆོག་གི་ཏིང་ངེ་འཛིན་ལ་བཅུ་གཉིས་ཏེ། ཕྲ་མོའི་རྣལ་འབྱོར་དང་། བཟླས་པའི་ཆོ་ག་དང་། བྱ་བ་བྱས་པས་ཞུ་བ་ཉིད་དང་། ལྷ་མོས་བསྐུལ་བ་ཉིད༌[^20]དང་། སླར་ཡང་བཞེངས་པ་དང་། བཞེངས་པ༌[^21]ལ་དེ་བཞིན་གཤེགས་པ་ལྔས་བསྟོད་པ་དང་། དཀྱིལ་འཁོར་གྱི་འཁོར་ལོ་ཉེ་བར་བསྡུ་བ་དང་། ཚིམ་པར་བྱེད་པའི་ཆོ་ག་དང་། ནང་གི་སྦྱིན་སྲེག་གི་ཆོ་ག་དང་། གཤེགས་སུ་གསོལ་བ་དང་། གཏོར་མའི་ཆོ་ག་དང་། གཉིད་ལོག་པའི་ཆོ་ག་སྟེ་ལས་ཀྱི་རྒྱལ་བ་མཆོག་གི་ཏིང་ངེ་འཛིན་ཏོ། །

[Block 44]
འདི་ནི་བསྐྱེད་པའི་རིམ་པ་སྟེ་ཐ་མལ་པའི་ལུས་རྣམ་པར་དག་པས་ཁྱད་པར་ཅན་གྱི་ལྷའི་རྣམ་པ་རྫོགས་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 45]
རྡོ་རྗེའི་བཟླས་པའི་རིམ་པ་ལ་རྣམ་པ་བཅུ་གཅིག་སྟེ། རྡོ་རྗེ་འཆང་ཆེན་པོ་བཟླས་པ་དང་། སྐུའི་བཟླས་པ་དང་། གསུང་གི་བཟླས་པ་དང་། ཐུགས་ཀྱི་བཟླས་པ་དང་། རིན་པོ་ཆེའི་བཟླས་པ་དང་། དོན་ཡོད་པའི་བཟླས་པ་དང་། ཁྲོ་བོའི་བཟླས་པ་དང་། འདོད་ཆགས་ཀྱི་བཟླས་པ་དང་། ཞེ་སྡང་གི་བཟླས་པ་དང་། གཏི་མུག་གི་བཟླས་པ་དང་། མ་ནིང་གི་བཟླས་པའོ། །

[Block 46]
སེམས་ལ་དམིགས་པ་ཐོབ་པ་ཡང་རྣམ་པ་གསུམ་སྟེ། སྣང་བ་རྣམ་པར་དག་པ་དང་། སྣང་བ་མཆེད་པ་རྣམ་པར་དག་པ་དང་། སྣང་བ་ཉེ་བར་ཐོབ་པ་རྣམ་པར་དག་པའོ། །

[Block 47]
བདག་ལ་བྱིན་གྱིས་རློབ་པ་ཡང་རྣམ་པ་གསུམ་སྟེ། ཆོས་ཀྱི་སྐུར་བདག་བྱིན་གྱིས་བརླབ་པ་དང་། ལོངས་སྤྱོད་རྫོགས་པའི་སྐུར་བྱིན་གྱིས་བརླབ་པ་དང་། སྤྲུལ་པའི་སྐུར་བྱིན་གྱིས་བརླབ་པའོ། །

[Block 48]
མངོན་པར་བྱང་ཆུབ་པའི་རིམ་པ་ལ་ཡང་རྣམ་པ་གསུམ་སྟེ། འདོད་ཆགས་རྣམ་པར་དག་པ་དང་། འདོད་ཆགས་བར་མ་རྣམ་པར་དག་པ་དང་། འདོད་ཆགས་དང་བྲལ་བ་རྣམ་པར་དག་པའོ། །

[Block 49]
ཟུང་དུ་འཇུག་པའི་རིམ་པ༌[^22]ཡང་གཉིས་ཏེ། རྒྱུའི་ཟུང་དུ་འཇུག་པ་དང་། འབྲས་བུའི་ཟུང་དུ་འཇུག་པའོ། །

[Block 50]
དེ་ནི་རྫོགས་པའི་རིམ་པ་སྟེ་རང་བཞིན་གྱིས་གྲུབ་པའི་ཕྱིར་དང་། དབང་པོ་རྣོ་བའི་གདུལ་བྱའི་ཡུལ་ཡིན་པའི་ཕྱིར་ཞེས་བྱ་བའི་བར་དུའོ། །

[Block 51 [HEADING]]
### བསྐྱེད་པའི་རིམ་པ། ^1-1-0

[Block 52]
དེ་ལ་བསྐྱེད་པའི་རིམ་པ་མདོར་བསྡུས་པ་འདི་ཡིན་ཏེ།

[Block 53 [HEADING]]
#### དང་པོའི་སྦྱོར་བ། ^1-1-1-0

[Block 54 [HEADING]]
##### རྣལ་འབྱོར། ^1-1-1-1-0

[Block 55]
དང་པོ་རེ་ཞིག་རྣལ་འབྱོར་པས་སྙིང་རྗེ་ཆེན་པོ་མངོན་དུ་བྱས་ཏེ། སེམས་ཅན་ཐམས་ཅད་སྡུད་པར་བྱེད་པའི་ཚད་མེད་པའི་སེམས་བསྐྱེད་ལ། དེ་ནས་ཡིད་དུ་འོང་བའི་ས་ཕྱོགས་སུ་བདུད་རྩི་ལྔས་དཀྱིལ་འཁོར་བྱུགས་ཏེ། ནང་ཚངས་ཅན་ལ་སོགས་པའི་སྟན་འཇམ་པོ་ལ་སེམས་དཔའི་སྐྱིལ་མོ་ཀྲུང་དུ་འདུག་སྟེ། མྱུར་དུ་ཐ་མལ་པའི་ལུས་རྣམ་པར་དག་པར་བྱ་བའི་ཕྱིར་ཞེ་སྡང་རྡོ་རྗེ་བདག་ཉིད་བསྒོམ་པར་བྱའོ། །

[Block 56]
དེ་ནས་གནས་བསྲུང་བར་བྱ་བའི་ཕྱིར་ཞེ་སྡང་རྡོ་རྗེའི་ཏིང་ངེ་འཛིན་མངོན་དུ་བྱས་ཏེ། སྙོམས་པར་ཞུགས་པའི་རེག་བྱ་རྡོ་རྗེ་མའི་ཆོས་འབྱུང་བའི་ཕྱག་རྒྱའི་ནང་དུ་སྣ་ཚོགས་པདྨ་ལ་ཉི་མའི་དཀྱིལ་འཁོར་གྱི་སྟེང་དུ། ཁྲོ་བོ་ཐམས་ཅད་འཇུག་པ་སྔོན་དུ་འགྲོ་བ་རྡོ་རྗེའི་ལམ་ནས་ཧཱུྃ་ཡོངས་སུ་གྱུར་པ་ལས་ཁྲོ་བོའི་རྡོ་རྗེ་ལས་བྱུང་བ༌[^23]ཞལ་གསུམ་པ་ཕྱག་དྲུག་པ། སྤྱན་གསུམ་པ་རིགས་ཀྱི་ཀླུ་བརྒྱད་ཀྱིས་བརྒྱན་པ་སྐུ་མདོག་སྔོན་པོ་དང་དཀར་པོ་དང་དམར་བའི་ཞལ། སྤྱན་ཟླུམ་ཞིང་གཡོ་བ། གཡོན་བརྐྱང་བ་རྡོ་རྗེ་དང་དྲིལ་བུ་རྩ་བའི་ཕྱག་གཉིས་ཀྱིས་བསྣམས་པ། ཞགས་པ་དང་ལྕགས་ཀྱུ་དང་རལ་གྲི་དང་རྡོ་རྗེ་ཐོ་བ་འཛིན་པ། ཞེ་སྡང་རྡོ་རྗེའི་ཅོད་པན་ཅན་སྨིན་མ་ཁམ་པ་ཧ༌[^24]ཧ་ཧི་ཧིའི༌[^25]སྒྲ་སྒྲོགས་པའི་གནོད་མཛེས་ཀྱི་རྒྱལ་པོ་བསྒོམ་པར་བྱ་སྟེ། རྡོ་རྗེ་དང་པདྨའི་ནང་ནས་ཕྱིར་བྱུང་སྟེ་ཉི་མའི་དཀྱིལ་འཁོར་གྱི་སྟེང་དུ་གནས་ཤིང་བཀའ་ནོད་བཞིན་པར་རྣམ་པར་བསམས་ཏེ། དེའི་རྗེས་སུ་སྔ་མ་བཞིན་དུ་རེག་བྱ་རྡོ་རྗེ་མའི་ཆོས་འབྱུང་བའི་ནང་དུ་ཡི་གེ་ཧཱུྃ་བཅུ་ཡོངས་སུ་གྱུར་པ་ལས་གཤིན་རྗེ་དགྲ་ལ་སོགས་པ་ཁྲོ་བོ་བཅུ་པོ་འོག་ནས་འབྱུང་བའི་ཁ་དོག་དང་མཚོན་ཆ་འཛིན་པ་སྤྲོས་ཏེ། རིམ་པ་ཇི་ལྟ་བ༌[^26]བཞིན་དུ་ཤར་ལ་སོགས་པའི་ཕྱོགས་སུ་བསྒོམ་པར་བྱའོ། །

[Block 57]
ཁྲོ་བོ་དེ༌[^27]རྣམས་ཀྱང་སྟོད་ཁྲོ་བོའི་རྣམ་པ་སྨད་ཕུར་བུའི་རྣམ་པར་ཤེས་པར་བྱའོ། །

[Block 58]
དེའི་རྗེས་སུ་དབུས་ཀྱི་གཙོ་བོའི་བདག་ཉིད་ཀྱིས་སྔགས་འདི་དང་གནོད་མཛེས་ལ་བཀའ་བསྒོ་བར་བྱའོ། །

[Block 59]
ཨོཾ་སུམྦྷ་ནི་སུམྦྷ་ཧཱུྃ་ཧཱུྃ་ཕཊ། ཨོཾ་གྲྀཧྞཱ་གྲྀཧྞཱ་ཧཱུྃ་ཧཱུྃ་ཕཊ། ཨོཾ་གྲྀཧྞཱ་པ་ཡ་གྲྀཧྞཱ་པ་ཡ་ཧཱུྃ་ཧཱུྃ་ཕཊ། ཨོྃ་ཨཱ་ན་ཡ་ཧོ་བྷ་ག་བཱན་བཛྲ་རཱ་ཛ་ཧཱུྃ་ཧཱུྃ་ཕཊ། ཞེས་པ་འདིས་ཕྱོགས་བཅུར་གནས་པའི་བརྒྱ་བྱིན་ལ་སོགས་པའི་ཕྱོགས་སྐྱོང་དགུག་པར་བྱ་བའི་ཕྱིར་བཀའ་བསྒོ་བར་བྱའོ། །

[Block 60]
བཀའ་ཐོས་མ་ཐག་ཏུ་གནོད་མཛེས་ཀྱི་རྒྱལ་པོས་ཞགས་པ་དང་། ལྕགས་ཀྱུ་ཕྱོགས་བཅུར་སྤྲོས་ཏེ། བརྒྱ་བྱིན་ལ་སོགས་པ་ཕྱོགས་སྐྱོང་རྣམས་ཀྱི་མགྲིན་པར་ཞགས་པས་བཅིངས་ཏེ། ལྕགས་ཀྱུས་སྤྱི་བོར་བཏབ་པ་ལ་ཤར་ལ་སོགས་པའི་ཕྱོགས་དང་མཚམས་སུ་དགོད་པར་བསམ་མོ། །

[Block 61]
ཕྱོགས་སྐྱོང་བ་རྣམས་ཀྱི་ཁ་དོག་དང་ཕྱག་མཚན་ལ་སོགས་པའི་རིམ་པ་ནི་འདི་ཡིན་ཏེ། ཤར་གྱི་ཕྱོགས་སུ༌[^28]བརྒྱ་བྱིན་མདོག་སེར་པོ་གདོང་གཅིག་པ་ལག་པ༌[^29]

[Block 62]
གཉིས་པ་རབ་བརྟན་ལ་ཞོན་པ་ལག་པ༌[^30]ན་རྡོ་རྗེ་ཐོགས་པ་བསྒོམ་པར་བྱའོ། །

[Block 63]
ལྷོ་ཕྱོགས་སུ་གཤིན་རྗེ་ཁ་དོག་ནག་པོ་གདོང་གཅིག་པ་ལག་པ༌[^31]

[Block 64]
གཉིས་པ་མ་ཧེ་ལ་ཞོན་པ་བེ་ཅོན་ཐོགས་པའོ། །

[Block 65]
ནུབ་ཀྱི་ཕྱོགས་སུ་ཆུ་ལྷ་སྟེ་མདོག་དཀར་པོ་གདོང་པ་གཅིག་པ་ལག་པ༌[^32]

[Block 66]
གཉིས་པ་ཀླུའི་ཞགས་པ་ཐོགས་པ་ཆུ་སྲིན་ལ་ཞོན་པའོ། །

[Block 67]
བྱང་གི་ཕྱོགས་སུ་ནོར་ལྷ་སྟེ་མདོག་དམར་བ་གདོང་གཅིག་པ་ལག་པ་གཉིས་པ་སེང་གེའི་རྒྱལ་མཚན་དང་ནེའུ་ལེའི་གཏེར་འཛིན་པ་སེང་གེའི་སྟན་ལ་འདུག་པའོ། །

[Block 68]
མེའི་མཚམས་སུ་མེ་ལྷ་སྟེ་མདོག་དམར་པོ་གདོང་གཅིག་པ་ལག་པ་གཉིས་པ་དབྱུག་པ་དང་བགྲང་ཕྲེང་འཛིན་ཅིང་ར་སྐྱེས་ཁམ་པ་ལ་ཞོན་པའོ། །

[Block 69]
བདེན་བྲལ་གྱི་མཚམས་སུ་སྲིན་པོ་སྟེ་མདོག་ནག་པོ་གདོང་གཅིག་པ་ལག་པ་གཉིས་པ་རལ་གྲི་དང་ཕུབ་འཛིན་ཅིང་ཡི་དགས་ལ་ཞོན་པའོ། །

[Block 70]
རླུང་གི་མཚམས་སུ་རླུང་ལྷ་སྟེ་མདོག་དུད་ཁ་གདོང་གཅིག་པ་ལག་པ་གཉིས་པ་བ་དན་འཛིན་ཅིང་ཤ་བ་ལ་ཞོན་པའོ། །

[Block 71]
དབང་ལྡན་གྱི་མཚམས་སུ་འབྱུང་པོའི་བདག་པོ་སྟེ་ཁ་དོག་དཀར་པོ་གདོང་གཅིག་པ་ལག་པ་གཉིས་པ་རྩེ་གསུམ་དང་ས་བོན་རྒྱས་པའི་འབྲས་བུ་འཛིན་ཅིང་ཁྱུ་མཆོག་ལ་ཞོན་པའོ། །

[Block 72]
སྟེང་དུ་ཚངས་པ་མདོག་དཀར་པོ་གདོང་བཞི་པ་དབྱུག་པ་དང་སྤྱི་བླུགས་འཛིན་པ་ངང་པ་ལ་ཞོན་པའོ། །

[Block 73]
སྟེང་དུ་ཡང་ཉི་མ་ནི་མདོག་དམར་པོ་གདོང་གཅིག་པ་ལག་པ་གཉིས་པ་པདྨ་ཐོགས་པ་པདྨའི་གདན་ལ་འདུག་པའོ། །

[Block 74]
ཟླ་བ་ནི་མདོག་དཀར་པོ་གདོང་གཅིག་པ་ལག་པ་གཉིས་པ་མེ་ཏོག་ཀུ་མུ་ད་ཐོགས་ཤིང་ཀུ་མུ་དའི་སྟན་ལ་འདུག་པའོ། །

[Block 75]
འོག་ཏུ་སྲིན་པོའི་བདག་པོ་ཐགས༌[^33]བཟངས་རིས་ཏེ་ཁ་དོག་ནག་པོ་གདོང་གཅིག་པ་ལག་པ་གཉིས་པ་སྡིགས་མཛུབ་དང་རལ་གྲི་ཐོགས་པ་གླང་པོ་ཆེ་ལ་ཞོན་པའོ། །
--- END BLOCKS ---
