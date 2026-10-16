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
## ༄༅། །དགེ་སྦྱོང་གི་ཀཱ་རི་ཀཱ་ལྔ་བཅུ་པའི་ཚིག་གི་བརྗེད་བྱང་དུ་བྱས་པ།

[Block 2 [HEADING]]
## ཀླད་ཀྱི་དོན། ^I-0

[Block 3]
༄༅༅། །ཐམས་ཅད་མཁྱེན་པ་ལ་ཕྱག་འཚལ་ལོ། །

[Block 4]
དགེ་སྦྱོང་གི་ཀཱ་རི་ཀཱ་ལྔ་བཅུ་པའི་ཚིག་གི་བརྗེད་བྱང་དུ་བྱས་པ། དཔེར་ན་ས་གཞི་ལ་ས་བོན་བཏབ་ནས་ས་བོན་ལ་བརྟེན་ནས་མྱུ་གུ། མྱུ་གུ་ལ་བརྟེན་ནས་འདབ་མ། འདབ་མ་ལ་བརྟེན་ནས་སྡོང་བུ། སྡོང་བུ་ལ་བརྟེན་ནས་མེ་ཏོག །མེ་ཏོག་ལ་བརྟེན་ནས་འབྲས་བུ་འབྱུང་བ་དེ་བཞིན་དུ། ཚུལ་ཁྲིམས་ས་གཞི་དང་འདྲ་བ་ལ་བརྟེན་ནས་མྱུ་གུ་ལ་སོགས་པ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་གྱི་ཕུང་པོ་འབྱུང་ངོ་། །ཏིང་ངེ་འཛིན་གྱི་ཕུང་པོ་བྱུང་ནས་དེའི་འོག་ཏུ་མེ་ཏོག་ལྟ་བུའི་ཤེས་རབ་ཀྱི་ཕུང་པོ་འབྱུང་ངོ་། །ཤེས་རབ་ཀྱི་ཕུང་པོ་བྱུང་ནས་དེའི་འོག་ཏུ་རྣམ་པར་གྲོལ་བའི་ཕུང་པོ་དང་། རྣམ་པར་གྲོལ་བའི་ཡེ་ཤེས་མཐོང་བའི་ཕུང་པོ་འབྲས་བུ་ལྟ་བུ་འབྱུང་ངོ་། །དེ་བས་ན་དགེ་བ་ཐམས་ཅད་འབྱུང་བའི་གཞི་ཚུལ་ཁྲིམས་ཡིན་པའི་ཕྱིར་ཚུལ་ཁྲིམས་བསྲུང་བ་ལ་ནན་ཏན་བྱའོ། །

[Block 5 [HEADING]]
## རང་གི་ལྷ་ལ་བསྟོད་ཅིང་ཕྱག་འཚལ་བ། ^1-0

[Block 6]
དགེ་སྦྱོང་གི་བསླབ་ཚིག༌[^1]ལྔ་བཅུ་པ་འདི་མགོ་མཇུག་ཏུ་བསྡུ་ན་དོན་རྣམ་པ་བརྒྱད་ཀྱིས་འཆད་དེ། གང་ཞེ་ན། བསྟོད་ཅིང་ཕྱག་འཚལ་བ་བསྟན་པ་དང་། བསླབ་པ་ཉམས་སུ་བླང་བ་དང་། སྔ་དྲོའི་དུས་ན་ལས་གང་བྱ་བ་དང་། ཟས་ཀྱི་བྱ་བ་བྱས་པའི་འོག་ཏུ་ལས་གང་བྱ་བ་དང་། ཕས་ཕམ་པའི་གནས་དང་། བསླབ་པ་ཕྲ་མོའི་གནས་དང་། ཕྱི་དྲོ་ཕན་ཆད་ཇི་ལྟར་བྱ་བ་དང་།

[Block 7]
བརྒྱད་པ་འབྲས་བུ་ཇི་ལྟར་བྱ་བ་བཞིན་དུ་བསྟན་པའོ། །

[Block 8]
དེ་ལ་མགོན་པོ་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། མདོ་ཙམ་ངེས་པར་བཤད་པར་བྱ། །ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་རང་གི་ལྷ་ལ་བསྟོད་ཅིང་ཕྱག་འཚལ་བ་བསྟན༌[^2]ཏོ། །

[Block 9]
ཤཱཀྱ་སེང་གེ་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། བདག་གི་ལུས་བཞིན་བསླབ་པ་བསྲུང་། །ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་བསླབ་པ་ཉམས་སུ་བླང་བ་བསྟན་ཏོ། །

[Block 10]
ནམ་གྱི་ཆ་སྨད་ཅེས་བྱ་བ་ནས་བརྩམས་ཏེ། སྦྱིན་པའི་ཚིགས༌[^3]བཅད་གཉིས་ཤིག་བརྗོད། །ཅེས་བྱ་བ་ཡན་ཆད་ཀྱིས་སྔ་དྲོའི་དུས་ན་ལས་གང་བྱ་བ་བསྟན་ཏོ། །

[Block 11]
མན་ངག་ཡོད་ན་བསམ་གཏན་བྱ།[^4] །ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། བསྒྲུབ་པ་ལ་ནི་བརྩོན་པར་བྱ། །ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་དགེ་བ་བྱ་བ་བསྟན་ཏོ། །

[Block 12]
བརྟུལ་ཞུགས་གནས་སེམས་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། ངག་རྣམས་ཤིན་ཏུ་བསྡམ་པར་བྱ། །ཞེས་པ་ཡན་ཆད་ཀྱིས་ཕས་ཕམ་པའི་གནས་བསྟན་ཏོ། །

[Block 13 [VERSE]]
འབྲུ་བཏགས་ཕབས་དང་སྦྱར་བ་ཡི། །
ཞེས་བྱ་བ་ནས་བཟུང་ནས།
གུས་བཅས་ཞེ་ས་བཅས་པར་བྱ། །

[Block 14]
ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་བསླབ་པ་ཕྲ་མོ་རྣམས་བསྟན་ཏོ། །

[Block 15 [VERSE]]
ལག་པ་དག་པར་བསྙལ་ནས༌[^5]ནི། །
ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ།
ཇི་སྐད་བསྟན་པ་བཞིན་དུ་བྱ། །

[Block 16]
ཞེས་པ་ཡན་ཆད་ཀྱིས་ཕྱི་དྲོ་ཕན་ཆད་ཀྱི་བྱ་བ་བསྟན་ཏོ། །

[Block 17 [VERSE]]
ཇི་ལྟར་ཉོན་མོངས་མྱུར་ཟད་ནས། །
བྱང་ཆུབ་དམ་པ་ཐོབ་པར་འགྱུར། །
དེ་ལྟར་བསྒྲིམས་དང་ལྡན་པར་བྱ། །

[Block 18]
ཞེས་བྱ་བས་ནི་འབྲས་བུ་བསྟན་ཏོ། །

[Block 19 [HEADING]]
### སངས་རྒྱས་ལ་བསྟོད་ཅིང་ཕྱག་འཚལ་བ། ^1-1-0

[Block 20 [HEADING]]
#### གཞན་གྱི་དོན་ཕུན་སུམ་ཚོགས་པ། ^1-1-1-0

[Block 21]
དེ་ལ་སངས་རྒྱས་ཀྱི་སློབ་མ་རྣམས་ཀྱི༌[^6]ལྷ་ནི་དཀོན་མཆོག་གསུམ་སྟེ། སངས་རྒྱས་དང་། ཆོས་དང་། དགེ་འདུན་དང་། [^7]མགོན་པོ་ཐམས་ཅད་མཁྱེན་ཞེས་བྱ་བ་ནི༌[^8]སངས་རྒྱས་ལ་བསྟོད་ཅིང་ཕྱག་འཚལ་བ་བསྟན༌[^9]ཏེ། སངས་རྒྱས་ལ་བསྟོད་པ་ཡང་གཞན་གྱི་དོན་མཛད་པ་དང་། རང་གི་དོན་ཕུན་སུམ་ཚོགས་པ་བརྙེས་པའི་སྒོ་ནས་བསྟོད་དེ།[^10] དེ་ལ་མགོན་པོ་ཞེས་བྱ་བས་གཞན་གྱི་དོན་ཕུན་སུམ་ཚོགས་པར་མཛད་པ་སྟོན་ཏེ། སེམས་ཅན་ངན་སོང་གསུམ་དུ་སྐྱེས་པ་རྣམས་དེ་ལས་ཐར་པའི་སྐྱབས་མཛད་པ་དང་། ལྷ་དང་མིར་སྐྱེས་པ་སྐྱེ་རྒ་ན་འཆིས་གཙེས་པ་ཐམས་ཅད་ཀྱི་སྐྱབས་མཛད་པས་ན་སངས་རྒྱས་ལ་མགོན་པོ་ཞེས་བྱ་སྟེ། སེམས་ཅན་ཐམས་ཅད་ཀྱི་སྐྱབས་དང་དཔུང་གཉེན་དུ་གྱུར་པ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 22]
དེ་ལ་སེམས་ཅན་ངན་སོང་གསུམ་དུ་སྐྱེས་པ་རྣམས་ལ་ནི་འོད་ཟེར་བཀྱེ་བ་དང་སྤྲུལ་པའི་སྐུ་བསྟན་པའི་སྒོ་ནས་ངན་སོང་ལས་ཐར་པར་མཛད་དོ། །

[Block 23]
ལྷ་དང་མིར་སྐྱེས་པ་སྐྱེ་རྒ་ན་འཆིས་གཙེས་པ༌[^11]རྣམས་ལ་ནི་འཕགས་པའི་བདེན་པ་བཞི་བཤད་ཅིང་དེ་ལ་བཀོད་ནས་སྐྱེ་རྒ་ན་འཆི་ལས་ཐར་པའི་སྒོ་ནས་སྐྱབས་མཛད་དོ། །

[Block 24 [HEADING]]
#### བདག་གི་དོན་ཕུན་སུམ་ཚོགས་པ། ^1-1-2-0

[Block 25]
ཐམས་ཅད་མཁྱེན་ཞེས་བྱ་བས་བདག་གི་དོན་ཕུན་སུམ་ཚོགས་པ་བརྙེས་པ་བསྟན་ཏེ། ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད་དང་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ལ་སོགས་པ་ཇི་སྙེད་དུ་ཤེས་པར་བྱ་བའི་ཆོས་ཐམས་ཅད་མ་ལུས་པར་ཤེས་ཤིང་། དེ་དག་ཀྱང་མི་རྟག་པ་དང་སྡུག་བསྔལ་བ་དང་སྟོང་པ་དང་བདག་མེད་པའི་མཚན་ཉིད་དུ་ཕྱིན་ཅི་མ་ལོག་པར་ཤེས་པས་ན་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ལ་ཐམས་ཅད་མཁྱེན་པ་ཞེས་བྱ་སྟེ། འདི་དག་བདག་དང་གཞན་གྱི་དོན་ཕུན་སུམ་ཚོགས་པའི་སངས་རྒྱས་ལ་ཕྱག་འཚལ་ཏེ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 26 [HEADING]]
### ཆོས་ལ་བསྟོད་ཅིང་ཕྱག་འཚལ་བ། ^1-2-0

[Block 27]
ཆོས་ཞེས་བྱ་བས་ནི་ཆོས་ལ་བསྟོད་ཅིང་ཕྱག་འཚལ༌[^12]བར་བསྟན་ཏེ། དེ་ལ་ཆོས་ལ་ཡང་རྣམ་པ༌[^13]གསུམ་མོ། །གང་ཞེ་ན། བཤད་པའི་ཆོས་དང་། སྒྲུབ་པའི་ཆོས་དང་། འབྲས་བུའི་ཆོས་སོ། །

[Block 28 [HEADING]]
#### བཤད་པའི་ཆོས། ^1-2-1-0

[Block 29]
དེ་ལ་གསུང་རབ་ཡན་ལག་བཅུ་གཉིས་ནི་བཤད་པའི་ཆོས་སོ། །

[Block 30 [HEADING]]
#### སྒྲུབ་པའི་ཆོས། ^1-2-2-0

[Block 31]
རང་གི་ལ་བྱང་ཆུབ་ཀྱི་ཕྱོགས་ཀྱི་ཆོས་སུམ་ཅུ་རྩ་བདུན་ནི་སྒྲུབ་པའི༌[^14]ཆོས་སོ། །

[Block 32 [HEADING]]
#### འབྲས་བུའི་ཆོས། ^1-2-3-0

[Block 33]
མྱ་ངན་ལས་འདས་པ་ནི་འབྲས་བུའི་ཆོས་སོ། །

[Block 34]
ཆོས་དེ་གསུམ་ལ་ཕྱག་འཚལ་ཏེ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 35 [HEADING]]
### དགེ་འདུན་ལ་བསྟོད་པ། ^1-3-0

[Block 36]
འཕགས་པའི་ཚོགས་ལ་ཞེས་བྱ་བས་དགེ་འདུན་ལ་བསྟོད་པ་བསྟན་ཏེ། ཉོན་མོངས་པ་དང་སྡིག་པའི་ཆོས་ལས་རིང་དུ་སྤངས་པ་ལ་ནི་འཕགས་པ་ཞེས་བྱ་ལ། འཕགས་པའི་གང་ཟག་དེ་ལྟ་བུ་མང་པོ་ལ་ནི་འཕགས་པའི་ཚོགས་ཞེས་བྱ་སྟེ། དེ་ཡང་མདོར་ན་སློབ་པའི༌[^15]གང་ཟག་དང་། མི་སློབ་པའི་གང་ཟག་འཕགས་པ༌[^16]གཉིས་ཡོད་དོ། །

[Block 37 [HEADING]]
#### སློབ་པའི་གང་ཟག། ^1-3-1-0

[Block 38]
དེ་ལ་སློབ་པའི་གང་ཟག་ནི་བདུན་ཡོད་དེ། རྒྱུན་དུ་ཞུགས་པ་དང་། རྒྱུན་དུ་ཞུགས་པའི་འབྲས་བུ་ཐོབ་པ་དང་། ལན་ཅིག་ཕྱིར་འོང་བ་དང་། ལན་ཅིག་ཕྱིར་འོང་བའི་འབྲས་བུ་ཐོབ་པ་དང་། ཕྱིར་མི་འོང་བ་དང་། ཕྱིར་མི་འོང་བའི་འབྲས་བུ་ཐོབ་པ༌[^17]དང་། དགྲ་བཅོམ་པ་ལ་འཇུག་པ་དང་བདུན་ནོ། །

[Block 39 [HEADING]]
#### མི་སློབ་པའི་གང་ཟག། ^1-3-2-0

[Block 40]
མི་སློབ་པའི་གང་ཟག་ནི་དགྲ་བཅོམ་པའི་འབྲས་བུ་ཐོབ་པ་སྟེ། དེ་དག་ལ་ཡང་ཕྱག་འཚལ་ཏེ་ཞེས་བྱ་བ་སྦྱར་རོ། །
--- END BLOCKS ---
