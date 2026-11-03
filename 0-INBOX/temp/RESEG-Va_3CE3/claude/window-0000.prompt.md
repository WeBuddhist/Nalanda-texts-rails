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
[Block 1 [HEADING]]
## ༄༅༅། །འཕགས་པ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་འབུམ་པ་དང་།ཉི་ཁྲི་ལྔ་སྟོང་པ་དང་། ཁྲི་བརྒྱད་སྟོང་པའི་རྒྱ་ཆེར་བཤད་པ།༼སྨད་ཆ།༽

[Block 2 [HEADING]]
## མ་འབུམ་པའི་བཤད་པ། ^1-0

[Block 3 [HEADING]]
### འབྲིང་དུ་བཤད་པ། ^1-1-0

[Block 4 [HEADING]]
#### ཐེག་པ་ཆེན་པོ་བསྟན་པ། ^1-1-1-0

[Block 5 [HEADING]]
##### མི་འཇིགས་པའི་ཐེག་པ་ཆེན་པོ། ^1-1-1-1-0

[Block 6]
བམ་པོ་བཅུ་བཞི་པ། མི་འཇིགས་པ་བཞི་སྟེ་ཞེས་བྱ་བ་ལ། དང་པོ་དང་གཉིས་པ་ནི་རང་གི་དོན་ལས་བརྩམས་པའོ། །

[Block 7]
གསུམ་པ་དང་བཞི་པ་ནི་གཞན་གྱི་དོན་ལས་བརྩམས་པའོ། །

[Block 8]
དགེ་སྦྱོང་དང་བྲམ་ཟེ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། ཤེས་རབ་ཀྱིས་མངོན་པའི་ང་རྒྱལ་བྱེད་པའི་ཕྱིར། དགེ་སྦྱོང་དང་བྲམ་ཟེ་སྨོས་སོ། །

[Block 9]
ལྷའི་མིག་དང་ཕ་རོལ་གྱི་སེམས་ཤེས་པ་ལ་སོགས་པ་ཕུན་སུམ་ཚོགས་པའི་ཕྱིར་ལྷ་དང་། བདུད་སྨོས་སོ། །

[Block 10]
རྫུ་འཕྲུལ་དང་མཐུ་ཆེ་བའི་ཕྱིར་ཚངས་པ་རྣམས་སྨོས་སོ། །

[Block 11]
རྒྱུ་དེ་ཡང་དག་པར་རྗེས་སུ་མི་མཐོང་སྟེ་ཞེས་བྱ་བ་ནི་དེ་དག་གིས༌[^1]བརྒལ་བའི་རྒྱུར་འགྱུར་བ་འགལ་བ་དེ་ཅུང་ཟད་ཀྱང་མི་མཐོང༌[^2]ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 12]
བདེ་བ་ཐོབ་ཅེས་བྱ་བ་ནི་ལུས་ཀྱི་སྤུ་ཟིང་ཞེས་བྱེད་པ་དང་། བག་འཁུམས་པ་ལ་སོགས་པ་མེད་པར་བསྟན་ཏོ། །

[Block 13]
དེའི་དབང་གིས་ཅང་ཤེས་ཁྱུ་མཆོག་གི་གནས་སུ་ཞལ་གྱིས་འཆེས་ཏེ། སྐུའི་ཕྲིན་ལས་རྣམ་པར་དག་པའི་ཕྱིར་རོ། །

[Block 14]
བག་ཚ་བ་མེད་པར་ཐོབ་ཅེས་བྱ་བ་ནི་གསུང་ལ་ཞུམ་པ་དང་། དམན་པར་གྱུར་པ་ལ་སོགས་པ་མེད་པར་བསྟན་ཏོ། །

[Block 15]
དེའི་དབང་གིས་སེང་གེ་བཞིན་དུ་སྒྲོག་སྟེ། གསུང་གི་ཕྲིན་ལས་རྣམ་པར་དག་པའི་ཕྱིར་རོ། །

[Block 16]
མི་འཇིགས་པ་ཐོབ་ཅེས་བྱ་བ་ནི་ཐུགས་ལ་དོགས་པ་དང་། ཞུམ་པ་ལ་སོགས་པ་མེད་པར་བསྟན་ཏོ། །

[Block 17]
དེའི་དབང་གིས་ཚངས་པ་བཞིན་དུ་འཁོར་ལོ་བསྐོར་ཏེ། ཐུགས་ཀྱི་ཕྲིན་ལས་རྣམ་པར་དག་པའི་ཕྱིར་རོ། །

[Block 18]
དེ་བཞིན་དུ་ཐམས་ཅད་ལ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 19 [HEADING]]
##### སོ་སོ་ཡང་དག་པར་རིག་པའི་ཐེག་པ་ཆེན་པོ། ^1-1-1-2-0

[Block 20]
ཆོས་སོ་སོ་ཡང་དག་པར་རིག་པ་དང་། དོན་སོ་སོ་ཡང་དག་པར་རིག་པ་ཞེས་བྱ་བ་ནི་དེ་བཞིན་གཤེགས་པའི་གསུང་རབ་ཏུ་རྟོགས་པ་ཚིག་གི་ཚོགས་དང་། མིང་གི་ཚོགས་དང་། ཡི་གེའི་ཚོགས་ཀྱི་བདག་ཉིད་ཀྱི་གཞུང་མང་པོ་སྟེ། འདིས་ཆོས་སོ་སོ་ཡང་དག་པར་རིག༌[^3]པར་འགྱུར་བའམ། ཆོས་སོ་སོ་ཡང་དག་པར་རིག་པའི་ཕྱིར་སོ་སོ་ཡང་དག་པར་རིག་པའོ། །

[Block 21]
དོན་ཅེས་བྱ་བ་ནི་བརྗོད་པར་བྱ་བའི་ཚོགས་ཏེ། དེ་ཤེས་པ་ནི་དོན་སོ་སོ་ཡང་དག་པར་རིག་པའོ། །

[Block 22]
ཡང་ན་རྒྱུ་དང་རྐྱེན་གྱི་ཆོས་ཐམས་ཅད་ནི་ཆོས་ཏེ། དེ་དག་ཤེས་པ་ནི་ཆོས་སོ་སོ་ཡང་དག་པར་རིག་པའོ། །

[Block 23]
རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་འབྲས་བུའི་ཆོས་རྣམས་ཤེས་པ་ནི། དོན་སོ་སོ་ཡང་དག་པར་རིག་པའོ། །

[Block 24]
ཡང་ན་རྣམ་པར་སྨིན་པ་དང་བཅས་པའི་ཆོས་དགེ་བ་དང་མི་དགེ་བའི་ཆོས་ཐམས་ཅད་ནི་ཆོས་ཏེ། དེ་དག་ཤེས་པ་ནི་ཆོས༌[^4]སོ་སོ་ཡང་དག་པར་རིག་པའོ། །

[Block 25]
སྒྲིབ་པ་དང་མི་སྒྲིབ་པ་དང་། ལུང་དུ་མ་བསྟན་པའི་ཆོས་རྣམས་ནི་དོན་ཏེ། དོན་དེ་དག་ཤེས་པ་ནི་དོན་སོ་སོ་ཡང་དག་པར་རིག་པའོ། །

[Block 26]
ཡང་ན་ཀུན་འབྱུང་བ་དང་། ལམ་གྱི་བདེན་པར་རྟོགས་པ་ཀུན་ནས་ཉོན་མོངས་པ་དང་། རྣམ་པར་བྱང་བའི་ཆོས་ཕྱོགས་ཀྱི་ཆོས་ཐམས་ཅད་ནི་ཆོས་ཏེ། དེ་དག་ཤེས་པ་ནི་ཆོས་སོ་སོ་ཡང་དག་པར་རིག་པའོ། །

[Block 27]
སྡུག་བསྔལ་གྱི་བདེན་པ་དང་། འགོག་པའི་བདེན་པར་གཏོགས་པའི་ཆོས་ཐམས་ཅད་ནི་དོན་ཏེ། དེ་དག་ཤེས་པ་ནི་དོན་སོ་སོ་ཡང་དག་པར་རིག་པའོ། །

[Block 28]
ཡང་ན་གདུལ་བ་རྣམས་ཀྱི་བསམ་པ་དང་། བག་ལ་ཉལ་དང་། སྤྱོད་པ་དང་། མོས་པ་དང་། དབང་པོ་ལ་སོགས་པ་ཐམས་ཅད་ནི་ཆོས་ཏེ། དེ་དག་ཤེས་པ་ནི་ཆོས་སོ་སོ་ཡང་དག་པར་རིག་པའོ། །

[Block 29]
མགོ་སྨོས་པ་དང་། རྣམ་པར་སྤྲོས་པ་གོ་བ་དང་། དྲང་དགོས་པ་དང་། ཚིག་ལྷུར་ལེན་པ་དང་། ཉོན་མོངས་པ་ཆེ་བ་དང་། ཆུང་བ་དང་། དབང་པོ་རྣོ་བ་དང་། རྟུལ་བ་དང་། སྐལ་བ་ཡོད་པ་དང་། སྐལ་བ་མེད་པ་ལ་སོགས་པའི་གདུལ་བ་རྣམས་ནི་དོན་ཏེ། །དེ་དག་ཤེས་པ་ནི་དོན་སོ་སོ་ཡང་དག་པར་རིག་པའོ། །

[Block 30]
ངེས་པའི་ཚིག་ཅེས་བྱ་བ་ནི་འཇིག་རྟེན་ན་གྲགས་པ་མིང་གི་ཚོགས་ལ་སོགས་པ་རྣམ་པ་མང་པོ་དེ་དག་ཉིད་ཀྱི་ཚིག་ངེས་པ་ལ་ངེས་པའི་ཚིག་ཅེས་བྱའོ། །

[Block 31]
ཡང་ན་གླིང་ཆེན་པོ་བཅྭ་བརྒྱད་ན་གནས་པ་དང་། ཡུལ་ཆེན་པོ་བཅུ་དྲུག་དག་ན་གནས་པ་དང་། མཐའ་འཁོབ་དགུ་བཅུ་རྩ་བརྒྱད་ན་གནས་པ་དང་། ཡུལ་གྱི་དབུས་སུ་གཏོགས་པའི་མི་ཐམས་ཅད་དང་། དུད་འགྲོའི་སྐྱེ་གནས་སུ་གཏོགས་པ་དང་། ཡི་དགས་དང་། སེམས་ཅན་དམྱལ་བ་ཐམས་ཅད་དང་། ལྷ་མ་ཡིན་དང་། ཀླུ་དང་། དྲི་ཟ་དང་། མི་འམ་ཅི་ཐམས་ཅད་དང་། གྲུབ་པ་དང་། རིག་སྔགས་འཆང༌[^5]དང་། རོལ་མོ་བྱེད་ཅིང་རྒྱུ་བ་ལ་སོགས་པ་དང་རྒྱལ་ཆེན་བཞིའི་རིས་དང་། སུམ་ཅུ་རྩ་གསུམ་ལ་སོགས་པ་འདོད་པའི་ཁམས་ཀྱི་ལྷ་རྣམས་དང་། བདུད་ཀྱི་རིས་ཐམས་ཅད་དང་། ཚངས་པ་དང་། གནས་གཙང་མའི་རིས་ཀྱི་ལྷ་ཐམས་ཅད་ཀྱི་སྔགས་འཆང༌[^6]དང་། བརྗོད་པ་གང་ཡིན་པ་ཐམས་ཅད་ནི་ངེས་པའི་ཚིག་གི་ཆོས་ཏེ། དེ་དག་ཤེས་པ་ནི་ངེས་པའི་ཚིག་སོ་སོ་ཡང་དག་པར་རིག་པ་ཞེས་བྱའོ། །ཤེས་པ་རྣམ་པ་གསུམ་པོ་དེ་དག་ཉིད་ཤེས་པ་གང་ཡིན་པ་དེ་ནི། སྤོབས་པ་སོ་སོ་ཡང་དག་པར་རིག་པའོ། །

[Block 32]
གདུལ་བ་དེ་དག་ཉིད་ཀྱི་བསམ་པ་དང་། བག་ལ་ཉལ་དང་མཐུན་པར་ཆོས་རྣམས་ཡང་དག་པར་སྟོན་པ་དང་། ཤེས་པར་བྱེད༌[^7]པ་དང་། ཁོང་དུ་ཆུད་པར་བྱེད༌[^8]པ་ནི་སྤོབས་པ་སོ་སོ་ཡང་དག་པར་རིག་པའོ། །

[Block 33]
བྱང་ཆུབ་སེམས་དཔའ་ནི་འཇིག་རྟེན་གྱི་ཁམས་ཐམས་ཅད་ན་སངས་རྒྱས་ཐམས་ཅད་ཀྱི་ཆོས་ཀྱི་རྒྱུན༌[^9]མ་ཆད་པར་འབྱུང་བ་དག་ཆོས་སོ་སོ་ཡང་དག་པར་རིག་པས་སྐད་ཅིག་གཅིག༌[^10]ཁོ་ན་ལས་ཡང་དག་པར་འཛིན་ཏོ། །

[Block 34]
དོན་སོ་སོ་ཡང་དག་པར་རིག་པས་ནི་སྐད་ཅིག་དེ་ཉིད་ལ་ཆོས་དེ་དག་གི་དོན་ཀྱང༌[^11]འཛིན་ཏོ། །

[Block 35]
སྐད་ཅིག་དེ་ཉིད་ལ། འཇིག་རྟེན་གྱི་ཁམས་སྣ་ཚོགས་ན། གདུལ་བ་སྣ་ཚོགས་ཀྱི་ངེས་པའི་ཚིག་རྣམས༌[^12]སྣ་ཚོགས་ཀྱིས༌[^13]ངེས་པའི་ཚིག་སོ་སོ་ཡང་དག་པར་རིག་པས་ཆོས་སྟོན་ཏོ། །

[Block 36]
སྤོབས་པ་སོ་སོ་ཡང་དག་པར་རིག་པས་ནི་འདུལ་བ་དེ་རྣམས། ཆོས་ཉིད་མངོན་སུམ་དུ་འཛིན་དུ་འཛུད་དོ།[^14] །

[Block 37 [HEADING]]
##### སངས་རྒྱས་ཀྱི་ཆོས་མ་འདྲེས་པའི་ཐེག་པ་ཆེན་པོ། ^1-1-1-3-0

[Block 38]
སངས་རྒྱས་ཀྱི་ཆོས་མ་འདྲས་པ་བཅོ་བརྒྱད་ཅེས་བྱ་བ་ལ། དེ་བཞིན་གཤེགས་པ་ལ་འཁྲུལ་བ་མི་མངའོ་ཞེས་བྱ་བ་ནི་སྐུ་དང་གསུང་དང་ཐུགས་ཀྱི་མཛད་པ་རྣམས་ལ་འཁྲུལ་པ་མི་མངའ་བ་སྟེ། ཇི་ལྟར་འདི་ནི༌[^15]དགྲ་བཅོམ་པ་རྣམས་གྲོང་ལ་སོགས་པར་བསོད་སྙོམས་ཀྱི་ཕྱིར་རྒྱུ་བ་ན། གླང་པོ་ཆེ་དང་། རྟ་དང་། བ་གླང་དང་། ཁྱི་གཏུམ་པོ་དང་། ཚེར་མ་དང་། སྡིག་སྦྲུལ་ལ་སོགས་པའི་གདོན་པ་རྣམས༌[^16]འབྱུང་བ་དང་། དགོན་པ་ན་ཆོམ་རྐུན་དང་། སྟག་དང་། གཟིག་གི་འཇིགས་པ་འབྱུང་བ་མི་ཤེས་པ་ལས་གྱུར་པའི་འཁྲུལ་པ་དེ་ལྟ་བུ་ནི་དེ་བཞིན་གཤེགས་པ་ལ་ཐམས་ཅད་ཀྱི་ཐམས་ཅད་དུ་མི་མངའོ། །

[Block 39]
དེ་བཞིན་གཤེགས་པ་ནི་བསྙེལ་བ་མི་མངའ་བའི་ཆོས་ཅན་ཏེ། བརྟགས་ན་སྐྱོན་མི་མངའ་བ་ཉིད་དུ་སེམས་ཅན་ལ་མཛད་པ་རྩོམ་མོ། །

[Block 40]
དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱི་སྤྱོད་ལམ་ནི་འཇིག་རྟེན་ལ་མཛེས་སོ། །
--- END BLOCKS ---
