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
### ༄༅། །ཆོས་མངོན་པའི་མཛོད་ཀྱི་བཤད་པ།༼སྨད་ཆ།༽

[Block 2 [HEADING]]
## ལས་བསྟན་པ། ^1-0

[Block 3]
༄༅༅། །

[Block 4 [HEADING]]
### རྣམ་པར་རིག་བྱེད་དང་ལྡན་པ། ^1-1-0

[Block 5 [VERSE]]
རྣམ་རིག་བྱེད་ནི་ཐམས་ཅད་ལ། །
བྱེད་པ་དག་ལ་ད་ལྟར་ལྡན། །

[Block 6]
སྡོམ་པ་དང་སྡོམ་པ་མ་ཡིན་པ་དང་བར་མ་ལ་གནས་པ་ཐམས་ཅད་ཇི་སྲིད་དུ་རྣམ་པར་རིག་བྱེད་བྱེད་པ་དེ་སྲིད་དུ་ད་ལྟར་གྱི་དེ་དང་ལྡན་ནོ། །

[Block 7]
མ་བཏང་བར་དུ་སྐད་ཅིག་མ། །ཕྱིན་ཆད་འདས་ལྡན། སྐད་ཅིག་མ་དང་པོ་ཕྱིན་ཆད་ནི་ཇི་སྲིད་མ་བཏང་གི་བར་དུ་འདས་པའི་རྣམ་པར་རིག་བྱེད་དང་ཡང་ལྡན་ནོ། །

[Block 8]
མ་འོངས་མེད། མ་འོངས་པའི་རྣམ་པར་རིག་བྱེད་དང་ནི་སུ་དང༌[^1]ཡང་མི་ལྡན་ནོ། །

[Block 9 [VERSE]]
བསྒྲིབས་པ་དང་ནི་མ་བསྒྲིབས་པ། །
འདས་པ་དག་དང་ལྡན་པ་མེད། །

[Block 10]
བསྒྲིབས་པ་དང་མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པའི་རྣམ་པར་རིག་བྱེད་འདས་པ་དག་དང་ཡང་འགའ་ཡང་ལྡན་པ་མེད་དེ། ཆོས་ཉམ་ཆུང་བའི་ཐོབ་པ་ཡང་ཉམ་ཆུང་བ་ཡིན་པས་རྗེས་སུ་འབྲེལ་པ་ཅན་མ་ཡིན་ནོ། །

[Block 11]
དེ༌[^2]ཅིས་ཉམ་ཆུང་བར་བྱས་ཤེ་ན། སེམས་ཀྱིས་བྱས་སོ། །

[Block 12]
འོ་ན་ནི་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པའི་སེམས་ཀྱི་དང་ཡང་མི་ལྡན་པར་འགྱུར་རོ། །

[Block 13 [VERSE]]
དེ་ནི་དེ་ལྟ་མ་ཡིན་ཏེ། །
རྣམ་པར་རིག་བྱེད་བླུན་པ་དང་། །

[Block 14]
གཞན་གྱི་དབང་ཡིན་པ་དེ༌[^3]ལྟར་སེམས་ནི་དེ་ལྟ་མ་ཡིན་ལ། ཉམ་ཆུང་དུ་བླངས་པ༌[^4]དེ་ནི་ཆེས་ཉམ་ཆུང་བར་འགྱུར་རོ། །

[Block 15 [HEADING]]
### སྡོམ་པ་མ་ཡིན་པའི་རྣམ་གྲངས། ^1-2-0

[Block 16]
སྡོམ་པ་མ་ཡིན་པ་ལ་གནས་པ་ཞེས་གང་བཤད་པ། སྡོམ་པ་མ་ཡིན་པ་ཞེས་བྱ་བ་འདི་ཅི་ཞེ་ན།

[Block 17 [VERSE]]
སྡོམ་པ་མིན་དང་ཉེས་སྤྱད་དང་། །
འཆལ་པའི་ཚུལ་ཁྲིམས་ལས་དེའི་ལམ། །

[Block 18]
འདི་དག་ནི་སྡོམ་པ་མ་ཡིན་པའི་རྣམ་གྲངས་ཀྱི་སྒྲ་སྟེ། དེ་ལ་ལུས་དང་ངག་མི་སྡོམ་པའི་ཕྱིར་སྡོམ་པ་མ་ཡིན་པའོ། །

[Block 19]
དམ་པ་རྣམས་ཀྱིས་སྨད་པའི་ཕྱིར་དང་། འབྲས་བུ་ཡིད་དུ་མི་འོང་བའི་ཕྱིར༌[^5]ཉེས་པར་སྤྱོད་པ་ཡིན་ནོ། །

[Block 20]
ཚུལ་ཁྲིམས་ཀྱི་མི་མཐུན་པའི་ཕྱོགས་ཡིན་པའི་ཕྱིར་འཆལ་པའི་ཚུལ་ཁྲིམས་ཡིན་ནོ། །

[Block 21]
ལུས་དང་ངག་གི་ལས་ཡིན་པའི་ཕྱིར་ལས་སོ། །

[Block 22]
དངོས་ཀྱིས་བསྡུས་པའི་ཕྱིར་ལས་ཀྱི་ལམ་ཡིན་ནོ། །

[Block 23 [HEADING]]
### རྣམ་པར་རིག་བྱེད་དང་ལྡན་པའི་མུ་བཞི། ^1-3-0

[Block 24]
རྣམ་པར་རིག་བྱེད་དང་ལྡན་ལ་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་དང་མི་ལྡན་པ་ཡང་ཡོད་ཅེས་བྱ་བ་མུ་བཞི་སྟེ། དེ་ལ་རེ་ཞིག །

[Block 25 [VERSE]]
བར་མ་དོར་གནས་སེམས་ཞན༌[^6]པས། །
བྱེད་ན་རྣམ་རིག་ཉིད་དང་ལྡན། །

[Block 26]
སྡོམ་པ་ཡང་མ་ཡིན་སྡོམ་པ་མ་ཡིན་པ་ཡང་མ་ཡིན་པ་ལ་གནས་པ་ཞིག་སེམས་ཞན་པས་དགེ་བའམ་མི་དགེ་བ་ཞིག་བྱེད་ན་རྣམ་པར་རིག་བྱེད་ཁོ་ན་དང་ལྡན་གྱི་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་དང་ནི་མ་ཡིན་ན། ལུང་དུ་མ་བསྟན་པ་ལྟ་སྨོས་ཀྱང་ཅི་དགོས་ཏེ། རྫས་ལས་བྱུང་བའི་བསོད་ནམས་བྱ་བའི་དངོས་པོ་དང་།

[Block 27 [VERSE]]
ལས་ཀྱི་ལམ་ནི་མ་གཏོགས་སོ། །
རྣམ་རིག་བཏང་དང་མ་སྐྱེས་པའི། །
འཕགས་པའི་གང་ཟག་རྣམ་རིག་མིན། །

[Block 28]
འཕགས་པའི་གང་ཟག་འགའ་ཞིག་ཚེ་གཞན་དུ་ཡོངས་སུ་གྱུར་ནས་ད་དུང་དུ་རྣམ་པར་རིག་བྱེད་མ་བྱུང་བའམ། རྣམ་པར་རིག་བྱེད་རྣམ་པར་ཉམས་ན་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་ཁོ་ན་དང་ལྡན་གྱི་རྣམ་པར་རིག་བྱེད་དང་ནི་མ་ཡིན་ནོ། །

[Block 29]
སྡོམ་པ་དང་སྡོམ་པ་མ་ཡིན་པ་དང་བར་མ་ལ་གནས་པ་རྣམས་ཀྱི་རྣམ་པར་རིག་བྱེད་དང་རྣམ་པར་རིག་བྱེད༌[^7]མ་ཡིན་པ་དང་ལྡན་པ་རྣམ་པར་གཞག་པ་བཤད་ཟིན་ཏོ། །

[Block 30 [HEADING]]
### སྡོམ་པ་ཇི་ལྟར་འཐོབ་པ། ^1-4-0

[Block 31]
ཡང་སྡོམ་པ་དེ་དག་ཇི་ལྟར་འཐོབ་ཅེ་ན། བསམ་གཏན་ལས་སྐྱེས་བསམ་གཏན་གྱི། །ས་ཉིད་ཀྱིས་འཐོབ། གང་གི་ཚེ་བསམ་གཏན་གྱི་ས་པའི་སེམས་ཟག་པ་དང་བཅས་པ་དངོས་གཞི་པའམ། ཉེར་བསྡོགས་པ་འཐོབ་པ་དེའི་ཚེ་བསམ་གཏན་གྱི་སྡོམ་པ་ཡང་འཐོབ་སྟེ། ལྷན་ཅིག་འབྱུང་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 32]
ཟག་མེད་ནི། འཕགས་དེས། ཟག་པ་མེད་པའི་བསམ་གཏན་གྱི་ས་འཐོབ་པ་དེ་ཉིད་ཀྱིས་ཟག་པ་མེད་པའི་སྡོམ་པ་ཡང་འཐོབ་བོ། །

[Block 33]
དེ་ལ་ཟག་པ་མེད་པ་ནི་བསམ་གཏན་གྱི་ས་དྲུག་པོ་བསམ་གཏན་བཞི་དང་། མི་ལྕོགས་པ་མེད་པ་དང་། བསམ་གཏན་ཁྱད་པར་ཅན་ཡིན་ནོ་ཞེས་འོག་ནས་བཤད་པར་བྱའོ། །

[Block 34]
སོ་སོར་ཐར་ཅེས་པ། གཞན་གྱི་རྣམ་རིག་བྱེད་སོགས་ཀྱིས། །སོ་སོར་ཐར་པའི་སྡོམ་པ་ནི་གལ་ཏེ། འདི་ལ་གཞན་གྱིས་རྣམ་པར་རིག་པར་བྱེད་ལ། འདི་ཡང་གཞན་ལ་རྣམ་པར་རིག་པར་བྱེད་ན་གཞན་གྱི་རྣམ་པར་རིག༌[^8]བྱེད་ལས་འཐོབ་བོ། །

[Block 35]
དེ་ཡང་དེ༌[^9]དགེ་འདུན་ནམ་གང་ཟག་ལས་ཏེ། དགེ་སློང་དང་། དགེ་སློང་མ་དང་། དགེ་སློང༌[^10]མའི་སྡོམ་པ་རྣམས་ནི་དགེ་འདུན་ལས་སོ། །

[Block 36]
གཞན་དག་ནི་གང་ཟག་ལས་སོ། །

[Block 37]
བྱེ་བྲག་ཏུ་སྨྲ་བ་འདུལ་བ་པ༌[^11]རྣམས་ན་རེ་རྣམ་པ་བཅུས་བསྙེན་པར་རྫོགས་སོ་ཞེས་ཟེར་བ་བསྡུ་བའི་ཕྱིར་སོགས་པའི་སྒྲ་སྨོས་ཏེ། རང་འབྱུང༌[^12]གིས་ནི་སངས་རྒྱས་དང་། །རང་སངས་རྒྱས་རྣམས་སོ། །

[Block 38]
ངེས་པར་འཇུག་པས་ནི་རྟེན༌[^13]ལྔ་པོ་རྣམས་སོ། །

[Block 39]
དགེ་སློང་ཚུར་ཤོག་ཅེས་བྱས་པས་ནི་གྲགས་པ་ལ་སོགས་པ་རྣམས་སོ། །

[Block 40]
སྟོན་པར་ཁས་བླངས་པས་ནི་འོད་སྲུངས་ཆེན་པོའོ། །
--- END BLOCKS ---
