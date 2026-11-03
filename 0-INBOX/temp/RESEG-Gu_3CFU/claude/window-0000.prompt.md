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
### ༄༅། །འདུལ་བའི་མདོའི་འགྲེལ་པ་མངོན་པར་བརྗོད་པ་རང་གི་རྣམ་པར་བཤད་པ།༼དེབ་དང་པོ།༽

[Block 2 [HEADING]]
## ཀླད་ཀྱི་དོན། ^I-0

[Block 3]
༄༅༅། །རྒྱ་གར་སྐད་དུ། སྭ་བྱཱ་ཁྱཱ་ན་ཨ་བྷི་དྷཱ་ན་བི་ན་ཡ་སཱུ་ཏྲ་བྲྀཏྟི་ནཱ་མ། བོད་སྐད་དུ། འདུལ་བའི༌[^1]མདོའི་འགྲེལ་པ་མངོན་པར་བརྗོད་པ་རང་གི་རྣམ་པར་བཤད་པ་ཞེས་བྱ་བ།

[Block 4 [VERSE]]
ཐམས་ཅད་མཁྱེན་པ་ལ་ཕྱག་འཚལ་ལོ། །
འདུལ་བའི་མདོ་རྣམས་གང་ཡིན་པ། །
བསྡུ་བའི་ཕྱིར་ནི་མཛད་གྱུར་ཏེ། །
བྱང་ཆུབ་སེམས་དཔའ་ཡོན་ཏན་འོད། །

[Block 5]
རང་གིས་དེ་ཉིད་རྣམ་བཤད་བྱ། །

[Block 6 [HEADING]]
## རབ་ཏུ་བྱུང་བའི་གཞི། ^1-0

[Block 7]
དེ་ལ་མདོ་དང་པོ་ནི་འདི་ཡིན་ཏེ། དེ་ནས། ངེས་པར་འབྱུང་བའི་ཚུལ་ཁྲིམས་ཀྱི་དབང་དུ་བྱས་ཏེ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་ལ་དེ་ནས་ཞེས་བྱ་བའི་སྒྲ་ནི་དབང་དུ་བྱེད་པའི་དོན་ཏོ།[^2] །མདོ་བརྩམས་པ་ནས་ཡོངས་སུ་རྫོགས་པའི་བར་གྱིས་ངེས་པར་འབྱུང་བའི་ཚུལ་ཁྲིམས་ཀྱི་དབང་དུ་བྱས་པར་རིག་པར་བྱའོ། །

[Block 8]
འདིར་འབྱུང་བ་ནི་ཐོབ་པ་ཡིན་ཏེ་འགྲོ་བ་ནི་མ་ཡིན་ནོ། །

[Block 9]
འདིས་ངེས་པར་འབྱུང་བས་ན་ངེས་པར་འབྱུང་བ་ཞེས་བྱའོ། །

[Block 10]
དཔེར་ན་གྲོང་ཐོབ་པ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 11]
ངེས་པའི་སྒྲ་ནི་ཕྱིར་མི་ལྡོག་པ༌[^3]བསྒྲགས་པའི་དོན་དུ་སྟེ། ཕྱིར་མི་ལྡོག་པར་འབྱུང་བ་ནི་ངེས་པར་འབྱུང་བ་ཞེས་བྱའོ། །

[Block 12]
དེ་ལྟར་ན་འདིས༌[^4]ཕུང་པོ་ལྷག་མ་མེད་པའི་མྱ་ངན་ལས་འདས་པར༌[^5]ཡང་དག་པར་ཐོབ་པ་བརྗོད་པ་སྟེ། གང་གི་ཕྱིར་དེ་ནི་ཕྱིར་མི་ལྡོག་པར་བྱེད་པའི་འབྱུང་བའོ། །

[Block 13]
འོ་ན་དེ་ལས་ངེས་པར་འབྱུང་བས་ན་ངེས་པར་འབྱུང་བ་ཞེས་བྱ་བའི་སྒྲ་འདིས་ཅིའི་ཕྱིར་འདིར་ཕུང་པོ་ལྷག་མ་དང་བཅས་པའི་མྱ་ངན་ལས་འདས་པ་ཡང་དག་པར་ཐོབ་པ་བརྗོད་པ་ཞེས་བྱ་བ་གོ་བར་བྱེད་པ་མ་ཡིན་ནམ། འདིས་ངེས་པར་འབྱུང་བས་ན་ངེས་པར་འབྱུང་བ་ཞེས་བྱ་བས་ལམ་མངོན་པར་བརྗོད་པ་ཞེས་བྱ་བ་ཡིན་ཞེ་ན། གང་གི་ཕྱིར་ངེས་པའི་སྒྲ་ནི་རྩོམ་པའི་དོན་ཅན་བསྟེན་པ་མ་ཡིན་ལ། ཐ་མའི་དོན་ཅན་ཡང་མ་ཡིན་ནོ། །

[Block 14]
འདིས༌[^6]བསྟེན་པས་ཕུང་པོ་ལྷག་མ་དང་བཅས་པའི་མྱ་ངན་ལས་འདས་པ་ཡང་དག་པར་ཐོབ་པ༌[^7]བརྗོད་པར་འགྱུར་བ་ཡིན་ཏེ། འཁོར་བར་འཇུག་པ་རྩོམ་པར་གྱུར་པ་འདི་ལས་འབྱུང་བས་ན་ངེས་པར་འབྱུང་བའམ་འཁོར་བར་འཇུག་པ་ལ་མཐར་ཐུག་པར་འགྲོ་བ་ཞེས་བྱ་བ་སྟེ་དེ་ཡང་བསྟེན་པ་མ་ཡིན་ནོ། །

[Block 15]
འོན་ཀྱང་ཕྱིར་མི་ལྡོག་པའི་དོན་ཅན་ནི་ངེས་པའི་སྒྲ་འདིར་མངོན་པར་འདོད་པའོ། །

[Block 16]
དེས་ན་གང་ཉིད་ཕྱིར་མི་ལྡོག་པར་འཇུག་པར་བྱེད་པའི་འབྱུང་བ་དེ་ཉིད་འདིས་བརྗོད་ཀྱི་གཞན་ནི་མ་ཡིན་ནོ། །

[Block 17]
གང་གི༌[^8]ཕྱིར་གང་ཞིག་སྙོམས་པར་འཇུག་པའི་ལམ་དུ་འོངས་ནས་རྡོ་རྗེ་ལྟ་བུའི་རྗེས་ལ་ཕུང་པོ་ལྷག་མ་དང་བཅས་པའི་མྱ་ངན་ལས་འདས་པ་ཡང་དག་པར་ཐོབ་པའོ། །

[Block 18]
དེའི་ལམ་ལས་གང་ཞིག་ལོངས༌[^9]ནས་ལམ་གཞན་དུ་འགྲོ་བ༌[^10]དེ་ནི་ཕྱིར་མི་ལྡོག་པ་ནི་མ་ཡིན་ཏེ། དགྲ་བཅོམ་པ་ཉིད་ལ་སོགས་པ་ལས་མ༌[^11]ཉམས་པ་དེ་ནི་འདིའི་མིང་དུ་སྣང་བ་ཉིད་དོ། །

[Block 19]
འདིར་འབྱུང་བ་ནི་ལམ་ཐོབ་པ་སྟེ་འགྲོ་བ་ནི་མ་ཡིན་ནོ། །

[Block 20]
དེ་བས་ན་འགྲོ་བའི་དོན་ལ་ཡང་དག་པར་མ་བསྟེན་པས༌[^12]ཀྱང་ངེས་པར་འབྱུང་བ་ཉིད་དུ་ཐལ་བ་མ་ཡིན་ནོ། །

[Block 21]
ངེས་པར་འབྱུང་བ་ལ་འགྲོ་བའི་ཚུལ་ཁྲིམས་ནི་ངེས་པར་འབྱུང་བའི་ཚུལ་ཁྲིམས་སོ། །

[Block 22]
དེ་ཡང་འདིར་ཆོས་ཀྱི་རྒྱུ་མཚན༌[^13]གང་ཞིག་ཚུལ་ཁྲིམས་དེ་ནི་མ་ལུས་པའི་འདུལ་བས་གསུངས་པར་ཤེས་པར་བྱའོ། །

[Block 23]
དེ་བས་ན་འདིར་རབ་ཏུ་བྱུང་བའི་གཞི་དང་། རྣམ་པར་འབྱེད་པའི་གཞི་དང་། གསོ་སྦྱོང་གི་གཞི་དང་། དབྱར་གྱི་གཞི་དང་། དགག་དབྱེའི་གཞི་དང་། སྲ་བརྐྱང་གི་གཞི་དང་། ཆོས་གོས་ཀྱི་གཞི་དང་། ཀོ་ལྤགས་ཀྱི་གཞི་དང་། སྨན་གྱི་གཞི་དང་། ལས་ཀྱི་གཞི་དང་། ཕྱིར་བཅོས་ཀྱི་གཞི་དང་། དུས་དང་དུས་མ་ཡིན་པས༌[^14]བསྡུས་པ་འབྱུང་བའི་གཞི་དང་། ས་གཞན་ན་གནས་པ་སྤྱོད་པའི་གཞི་དང་། ཡོངས་སུ་སྦྱོངས་པའི༌[^15]གཞི་དང་། ལས་བྱེ་བའི་གཞི་དང་། འཁོར་ལོ་བྱེ་བའི་གཞི་དང་། རྩོད་པའི་གཞི་དང་། གནས་མལ་གྱི་གཞི་ཞེས་བྱ་བའི་གོ་རིམས༌[^16]འདིས་འདུལ་བའི་ཆོ་ག་མ་ལུས་པ་ལ་ཡང་དག་པར་འཇུག་པའོ། །

[Block 24]
གང་གི་ཕྱིར་འདིར་དགོངས་པ་ནི་འདི་ཡིན་ཏེ། རྣམ་པ་འདིས་རབ་ཏུ་བྱུང་བ་ཉིད་དང་བསྙེན་པར་རྫོགས་པ་དག་ལ་ཉེ་བར་ཐོབ་པ་ནི་རིགས་པ་སྟེ་འདིར༌[^17]ནི་འདི་ལྟ་བུའི་རྣམ་པ་ཅན་བསྡུ་བ་དང་། འདིར་འདི་ལྟ་བུའི་རྣམ་པ་ཅན་ཡང་སྤང་བར་བྱ་བ་ཞེས་བྱ་བ་འདི་ལ་ཐོག་མར་སྦྱར་བ་ཞེས་བྱ་བ་དེའི་ཕྱིར་དང་པོར་རབ་ཏུ་བྱུང་བའི་གཞི་ཡང་དག་པར་གཞག༌[^18]པའོ། །

[Block 25]
བསྟན་པ་ལ་རབ་ཏུ་ཞུགས་པ་དེ་ལ་བསླབ་པ་མ་ལུས་པ་འདོར་བ་ལ་སོགས་པས་ཚུལ་མ་ཡིན་པ་ལ་འཇུག་པ་ལས་བསླབ་པ་ནི་འདི་ཡིན་ཏེ། དེ་བས་ན་དེའི་རྗེས་ལ་རྣམ་པར་འབྱེད་པ་ལ་ཡང་དག་པར་འཇུག་པའོ། །

[Block 26]
གསོ་སྦྱོང་གི་གཞི་ལ་སོགས་པ་རྣམས་ལ་ཡང་གོ་རིམས་ཀྱིས༌[^19]རྒྱུ་འདི་རྣམས་ཡིན་ཏེ། ཇི་ལྟར་བསླབ་པ་མཚུངས་པ་ཉིད་དུ་དུས་དུས་སུ་མདོ་ལ་བརྟེན་ནས་ཡོངས་སུ་རྒྱས་པར་བྱེད་པ་དེའི་ཕྱིར་གསོ་སྦྱོང་གི་གཞི་མངོན་པར་བརྗོད་པ་ཡིན་ནོ། །

[Block 27]
དུས་གང་ཞིག་ལ་དུས་གཅིག་ཏུ་གནས་པས་དོན་བསྒྲུབ་པ་དེ་ལ་གནས་པ་ལས་སོན་པའི་ཆོ་ག་སྟེ་དེའི་རྗེས་ལ་དབྱར་གྱི་གཞི་བསྟན་པ་ཡིན་ནོ། །

[Block 28]
གནས་ངེས་པའི་བདག་ཉིད་ཅན་དབྱར་གྱི་གཞི་ལ་གནས་པའི་ཐ་མར་མཐོང་བ་ལ་སོགས་པའི་གནས་གསུམ་རྣམས་ཀྱི༌[^20]དགེ་འདུན་ལ་དགག་དབྱེ་བགྱིད་དོ་ཞེས་བྱ་བས་དག་པ་ཡོད་པ་ལ་སྦྱིན་པ་གཏོང་བ་ལ་སྦྱར་བ་ཉིད་དོ་ཞེས་བྱ་བ་སྟེ། དེའི་རྗེས་ལ་དགག་དབྱེའི་གཞི་བསྟན་པ་ཡིན་ནོ། །

[Block 29]
བཀོད་པ་དང་འབྲེལ་བ་སུ་ཞིག་དབྱར་གྱི་གཞི་ལ་གནས་པའི་བདག་ཉིད་ཅན་གྱིས་གནས་ངེས་པ་ལས་ལུས་གཞན་དུ་གྱུར་པ༌[^21]ཡོད་དེ། ཤིན་ཏུ་སྦྱོངས་པ༌[^22]ལ་གནས་པ་ཉིད་ཀྱི་དོན་དུ་བསྟེན་པར་བྱ་བ་ཡིན་ཏེ། འདིའི་རྗེས་ལ་དེའི་རིམ་པ་ནི་དེའི་ཕྱིར་སྲ་བརྐྱང་གི་གཞི་བསྟན་པ་ཡིན་ནོ། །

[Block 30]
དེ་ལ་སོ་སོར་བསྒྲུབ་པ༌[^23]མེད་པ་ལས་གོས་ཀྱི་རྣམ་པར་དབྱེ་བ་ལ་སྦྱོར་བ་ཞེས་བྱ་བ་དང་བྲལ་བ་ཉིད་ཀྱི་བཀོད་པ་དང་འབྲེལ་བ་དེ་དག་ལ་གོས་སྦྱིན་པའི་དུས་ཡིན་ཏེ། དེའི་ཕྱིར་གོས་ཀྱི་གཞིའི་ཆོ་ག་བསྟན་པ་ཡིན་ནོ། །

[Block 31]
གོས་ཀྱི་རབ་ཏུ་དབྱེ་བ་ཤེས་པ་ནི་ཀོ་ལྤགས་ཞེས་བྱ་བ་ཡིན་ཏེ། དེའི་རྗེས་ལ་ཀོ་ལྤགས་ཀྱི་གཞི་བསྟན་པ་ཡིན་ནོ། །

[Block 32]
ནད་གསོ་བ་མེད་པས་གནས་གཅིག་གམ་སོ་སོར་གནས་པར་མི་ནུས་པས་དེའི་ཕྱིར་ལྷན་ཅིག་དང་ཉེ་བའི་སྔ་མ་དང་ཕྱི་མའི་དུས་དག་གིས་དང་པོར་གོས་སྦྱིན་པའི་དུས་ལ་ཕལ་ཆེར་ནད་ཀྱིས་བཏབ་པ་བྱུང་བ་དེ་ལ་བསྟེན་པ༌[^24]དེ་ལས་དགོས་པའི་ཆོ་ག་རིགས་པའི་ངོ་བོ་སྟེ། དེའི་རྗེས་ལ་སྨན་གྱི་གཞི་བསྟན་པ་ཡིན་ནོ། །

[Block 33]
དེ་ལྟར་གནས་པ་རྣམས་ཀྱིས་འབྱུང་ཞིང་འབྱུང་བའི་བྱ་བ་རྣམས་ལ་རྗེས་སུ་སྒྲུབ་པའི་ཆོ་ག་ཞེས་བྱ་བ་སྟེ་དེའི་རྗེས་ལ་ལས་ཀྱི་གཞི་བརྗོད་པ་ཡིན་ནོ། །

[Block 34]
སྨོན་ལམ་གྱི་ལས་ལ་སོགས་པ་འབྱུང་བ་རྣམས་ལ་སྨོན་ལམ་གྱི་ལས་བྱེད་པ་ལ་སོགས་པ་ངེས་པར་བྱེད་པ་དང་སོ་སོར་བསྒྲུབ་པར་སྐབས་ལ་སོགས་པས་རིགས་པ་ཞེས་བྱ་བ་དེའི་རྗེས་ལ་ཕྱིར་བཅོས་པའི་གཞི་བསྟན་པ་ཡིན་ནོ། །

[Block 35]
དགེ་འདུན་ལྷག་མ་དང་ལྡན་པ་ལ་དུས་དང་དུས་མ་ཡིན་པ་བསྡུས་པ་འབྱུང་བ་དང་། ས་གཞན་ན༌[^25]གནས་པ་ལ་སྤྱོད་པའི་གཞི་དག་ལ་ངེས་པར་སྤྱོད་པ་དང་སོ་སོར་སྤྱོད་པའི་དོན་དུ་ཡང་དག་པར་འཇུག་པ་ཡིན་ནོ། །

[Block 36]
ཀཽ་ཤཱམྦཱི་དང་། སྐྱ་བོ་དང་། དམར་བ་དང་གང་ཟག་དང་ཀུན་ནས་གནས་པའི་གཞི་རྣམས་ནི་ཕྱིར་བཅོས་པའི་གཞི་ལ་སོགས་པའི་མིང་རྣམས་ཀྱིས་གསུངས་པ་ཡིན་ཏེ། མིང་གཞན་འཇུག་པའི་དགོངས་པ་ནི་རིམ་པ་དེ་ཉིད་ལས་བཤད་པར་བྱའོ། །

[Block 37]
ངེས་པར་འབྱེད་པ་ལ་སོགས་པ་ལ་རྗེས་སུ་ཉེ་བར་གནས་པ་རྣམས་ལ་ཡོངས་སུ་འདུལ་བར་བྱེད་པ་ནི་རིགས་པའི་ངོ་བོ་ཉིད་ཡིན་ཏེ། དེའི་རྗེས་ལ་ཡོངས་སུ་སྦྱོང་བའི༌[^26]གཞི་བསྟན་པ་ཡིན་ནོ། །

[Block 38]
གསོ་སྦྱོང་གཞག་པའི་གཞིའི་མིང་གཞན་འདི་འཆད་པར་འགྱུར་བའི་དོན་དུ་ཤེས་པ་རྣམས་ལ་འཇུག་པ་ཞེས་བྱ་བ་དེའི་རྗེས་སུ་ལས་བྱེ་བ༌[^27]དང་། འཁོར་ལོ་བྱེ་བའི་གཞི་དག་བསྟན་པ་ཡིན་ནོ། །

[Block 39]
ཐ་སྙད་ལ་བསྟེན་པའི༌[^28]ཆོ་ག་འདིའི་རྗེས་སུ་རིགས་པ་ཡིན་ཞེས་བྱ་བ་འདིའི་དོན་ལ་རྩོད་པའི་གཞི་བསྟན་པ་ཡིན་ནོ། །

[Block 40]
གནས་གང་དུ་འདི་ཐམས་ཅད་དང་དགེ་བའི་ཕྱོགས་གཞན་རྗེས་སུ་སྒྲུབ་པར་བྱེད་པ་དེ་ལ་བརྟེན་པའི་ཆོ་ག་འདི་ལས་རིགས་པ་ཡིན་ཏེ། དེའི་རྗེས་ལ་གནས་མལ་གྱི་གཞི་བསྟན་པ་ཡིན་ནོ། །
--- END BLOCKS ---
