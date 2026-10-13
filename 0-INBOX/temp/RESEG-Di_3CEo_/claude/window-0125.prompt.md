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
[Block 4376 [VERSE]]
ངན་རྟོག་རྣམས་ཀྱིས་བསྟན་པ་འདི་དཀྲུགས་སོ། །
རང་བྱུང་རང་བྱུང་བསྟན་པ་གཅེས༌[^1670]འཛིན་རྣམས། །
མཆོག་ཏུ་ཞིར་གཤེགས་འགྲོ་མགོན་མེད་པ་ན། །
འདོམས་མེད་ཡོན་ཏན་འཇོམས་པར་བྱེད་པ་ཡི། །

[Block 4377 [VERSE]]
དྲི་མས་དགའ་མགུར་དེང་སང༌[^1671]འདི་ན་སྤྱོད། །
དེ་ལྟར་ཐུབ་པ་དག་གི་བསྟན་པ་ནི། །
ལྐོག་མར་སྲོག་ཕྱིན་འདྲ་དང་དྲི་མ་རྣམས། །
སྟོབས་དང་ལྡན་པའི་དུས་སུ་རིག་ནས་ནི། །
ཐར་པ་འདོད་པ་དག་གིས་བག་ཡོད་གྱིས། །

[Block 4378]
སྙོམས་པར་འཇུག་པ་བསྟན་པ་ཞེས་བྱ་བ་མཛོད་ཀྱི་གནས་བརྒྱད་པ་རྫོགས་སོ།། །།

[Block 4379 [HEADING]]
## གང་ཟག་བསྟན་པ། ^9-0

[Block 4380 [HEADING]]
### འདི་ལས་གཞན་ལ་ཐར་པ་མེད་པ། ^9-1-0

[Block 4381]
ཡང་ཅི་འདི་ལས་གཞན་ལ་ཐར་པ་ཡོད་དམ་ཞེ་ན། མེད་དོ། །ཅིའི་ཕྱིར་ཞེ་ན། བདག་ཏུ་ལྟ་བ་ཕྱིན་ཅི་ལོག་ལ་ཞེན་པའི་ཕྱིར་ཏེ། ཕུང་པོའི་རྒྱུད་ཁོ་ན་ལ་བདག་ཏུ་འདོགས་པར་ནི་ངེས་པར་མི་འཛིན་ཏོ། །

[Block 4382]
འོ་ན་ཅི་ཞེ་ན། རྫས་གཞན་ཁོ་ན་ལ་བདག་ཏུ་ཡོངས་སུ་རྟོགས་པར༌[^1672]བྱེད་ལ། ཉོན་མོངས་པ་རྣམས་ནི་བདག་ཏུ་འཛིན་པ་ལས་རབ་ཏུ་སྐྱེ་བ་ཡིན་ནོ། །

[Block 4383]
བདག་ཏུ་མངོན་པར་བརྗོད་པ་འདི་ནི༌[^1673]ཕུང་པོའི་རྒྱུད་ཁོ་ན་ལ་འཇུག་གི་མངོན་པར་བརྗོད་པར་བྱ་བ་གཞན་ལ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་ཇི་ལྟར་ཁོང་དུ་ཆུད་ཅེ་ན། མངོན་སུམ་དང་རྗེས་སུ་དཔག་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 4384]
གལ་ཏེ་དེ་ལྟ་ན་འོ་ན་ནི་སངས་རྒྱས་ཐམས་ཅད་མཁྱེན་པ་མ་ཡིན་པར་འགྱུར་ཏེ། ཐམས་ཅད་ཤེས་པར་འགྱུར་བའི་སེམས་སམ་སེམས་ལས་བྱུང་བ་གང་ཡིན་པ་དེ་ནི་ཅུང་ཟད་ཀྱང་མེད་དེ། [^1674]སྐད་ཅིག་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4385]
གང་ཟག་གིས་ནི་ཤེས་པར་འགྱུར་རོ། །

[Block 4386]
སྨྲས་པ།

[Block 4387 [VERSE]]
རྒྱུན་གྱིས་སྤྱོད་པའི་ཕྱིར་ན་དཔེར། །
མེ་ཡིས་ཐམས་ཅད་སྲེག་འདོད་ལྟར། །
དེ་བཞིན་ཐམས་ཅད་མཁྱེན་འདོད་བྱའི། །
ཅིག་ཅར་ཐམས་ཅད་མཁྱེན་ཕྱིར་མིན། །

[Block 4388]
ཁོ་བོ་ཅག༌[^1675]ནི་ཐམས་ཅད་ལ་ཅིག་ཅར་མཁྱེན་པ་མངོན་སུམ་དུ་གྱུར་པའི་ཕྱིར་སངས་རྒྱས་ཐམས་ཅད་མཁྱེན་པ་ཡིན་པར་ནི་མི་སྨྲའི། འོ་ན་ཇི་ལྟར་ཞེ་ན། མཐུ་ཡོད་པའི་ཕྱིར་དེ་སངས་རྒྱས་ཞེས་བྱ་བའི་རྒྱུད་གང་ཡིན་པ་དེ་ལ་གང་དུ་བཞེད་པ་གཏད་པ་ཙམ་གྱིས་ཕྱིན་ཅི་མ་ལོག་པར་མཁྱེན་པ་སྐྱེ་བ་གང་ཡིན་པ་དེའི་མཐུ་ཡོད་དོ། །

[Block 4389 [HEADING]]
### ཅིའི་ཕྱིར་བཅོམ་ལྡན་འདས་ཀྱིས་མེད་པ་ཁོ་ནའོ་ཞེས་མ་གསུངས། ^9-2-0

[Block 4390]
འོ་ན་ཕུང་པོ་ལྔ་ཁོ་ན་ལ་ཡོད་ལ་བདག་མེད་ན། ཅིའི་ཕྱིར་བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་མེད་པ་ཁོ་ནའོ་ཞེས་མ་གསུངས་ཤེ་ན། འདྲི་བ་པོའི་བསམ་པ་ལ་ལྟོས་པའི༌[^1676]ཕྱིར་ཏེ། དེས་སྲོག་ཅེས་བྱ་བའི་ཕུང་པོའི་རྒྱུན་གང་ཡིན་པ་དེ་ཡང་མེད་པར་གོ་བར་གྱུར་ན། ལོག་པར་ལྟ་བར་ལྟུང་བར་འགྱུར་ཏེ། རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་མི་ཤེས་པའི་ཕྱིར་རོ། །

[Block 4391]
འདིར་གསུམ༌[^1677]པ།

[Block 4392 [VERSE]]
ལྟ་བའི་མཆེ་བས་སྨྲས་པ་དང་། །
ལས་རྣམས་འཇིག་པ་ལ་ལྟོས༌[^1678]ནས། །
སྟག་མོས་ཕྲུ་གུ༌[^1679]ཁྱེར་བ་ལྟར། །
རྒྱལ་བས་ཆོས་ནི་སྟོན་པར་མཛད། །

[Block 4393 [VERSE]]
བདག༌[^1680]ཡོད་ཉིད་དུ་ཁས་བླངས་ན། །
ལྟ་བའི་མཆེ་བས་སྨྲས་པར་འགྱུར། །
ཀུན་རྫོབ་རྟོགས་པར་མ་གྱུར་ནས། །
དགེ་བའི་ཕྲུ་གུ༌[^1681]ཉམས་བྱེད་འགྱུར། །

[Block 4394]
ཡང་གསུངས་པ།

[Block 4395 [VERSE]]
མེད་ཕྱིར་བཅོམ་ལྡན་འདས་ཀྱིས་སྲོག །
དེ་ཉིད་གཞན་དུ་མ་གསུངས་སོ། །
བཏགས་པའང་མེད་དུ་འགྱུར་འོང་བས། །
མེད་དོ་ཞེས་ཀྱང་མ་གསུངས་སོ། །

[Block 4396]
ཕུང་པོའི་རྒྱུན་ནི་གང་ལ་དགེ །

[Block 4397 [VERSE]]
མི་དགེའི་འབྲས་བུ་ཡོད་པ་ཉིད། །
དེ་ལ་སྲོག་ཅེས་བྱ་སྟེ་དེ། །
སྲོག་མེད་བསྟན་པས་མེད་པར་འགྱུར། །
སྲོག་ཅེས་བྱ་བ་ཕུང་པོ་ལ། །

[Block 4398]
བཏགས་ཙམ་ཞེས་ཀྱང་མ་གསུངས་སོ། །

[Block 4399 [VERSE]]
དེའི་ཚེ་སྐྱེ་བོ་དེ་འདྲ་སྟེ། །
སྟོང་ཉིད་རྟོགས་པའི་སྐལ་ལྡན་མིན། །
འདི་ལྟར་གནས་པས་བདག་ཡོད་དམ། །
མེད་ཅེས་དྲིས་པ་འདྲི་བ་ཡི། །

[Block 4400]
བསམ་པ་ལ་ལྟོས༌[^1682]མ་གསུངས་ཏེ། །ཡོད་ན་ཅི་ཕྱིར་ཡོད་མི་གསུང་།[^1683] །

[Block 4401 [HEADING]]
### འཇིག་རྟེན་རྟག་ཅེས་བྱ་བ་ལུང་མ་བསྟན། ^9-3-0

[Block 4402]
འཇིག་རྟེན་རྟག་ཅེས་བྱ་བ་ཡང་འདྲི་བ་པོའི་བསམ་པ་ལ་ལྟོས༌[^1684]ནས་ལུང་མ་བསྟན་ཏེ། རེ་ཞིག༌[^1685]གལ་ཏེ་འཇིག་རྟེན་བདག་ཉིད་ཡིན་པར་འདོད་ན་ནི། དེ་མེད་པའི་ཕྱིར་ལུང་མ་བསྟན་བཞི་ཆར་མི་རིགས་སོ། །

[Block 4403]
འོན་ཏེ་འཇིག་རྟེན་འཁོར་བ་ཐམས་ཅད་ཡིན་ནོ་ཞེ་ན། དེ་ཡང་རིགས་པ་མ་ཡིན་ཏེ། འཇིག་རྟེན་རྟག་ན་འགའ་ཡང་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བར་མི་འགྱུར་རོ། །

[Block 4404]
མི་རྟག་ན་ནི་ཐམས་ཅད་ཆད་པར་འགྱུར་རོ། །

[Block 4405]
གཉིས་ཀ་ཡིན་ན་ནི་ཁ་ཅིག་ནི༌[^1686]ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བར་འགྱུར་ལ། ཁ་ཅིག་ནི་མི་འགྱུར་རོ། །

[Block 4406]
གཉིས་ཀ་མ་ཡིན་ན་ནི་ཁ་ཅིག་ནི་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་ཡང་མ་ཡིན་ལ། ཡོངས་སུ་མྱ་ངན་ལས་མི་འདའ་བ་ཡང་མ་ཡིན་པ་ཁོ་ནར་འགྱུར་རོ། །

[Block 4407]
དེ་བས་ན་ཡོངས་སུ་མྱ་ངན་ལས༌[^1687]འདའ་བ་ནི། ལམ་ལ་རག་ལུས་པའི་ཕྱིར་རྣམ་པ་བཞི་ཆར་ཡང་ངེས་པར་ལུང་མི་སྟོན་ཏེ། གཅེར་བུ་པའི་ཉན་ཐོས་ཀྱི་བྱེའུ་བཟུང་བ་བཞིན་ནོ། །

[Block 4408]
དེ་བཞིན་དུ་གཞན་རྣམས་ཀྱང་ངོ་། །

[Block 4409 [HEADING]]
### རྣམ་པར་ཤེས་པ་ལས་རྣམ་པར་ཤེས་པ་སྐྱེ་བ། ^9-4-0

[Block 4410]
གལ་ཏེ་རྣམ་པར་ཤེས་པ་ལས་རྣམ་པར་ཤེས་པ་སྐྱེའོ།[^1688] །

[Block 4411]
བདག་ལས་མ་ཡིན་ན། ཅིའི་ཕྱིར་རྟག་ཏུ་དེ་དང་འདྲ་བ་ཁོ་ན་སྐྱེ་བར་མི་འགྱུར་ཞིང་། མྱུ་གུ་དང་། སྡོང་པོ་དང་། འདབ་མ་ལ་སོགས་པ་བཞིན་དུ་རིམ་པ་ངེས་པར་སྐྱེ་བར་མི་འགྱུར་ཞེ་ན། གནས་པ་གཞན་དུ་འགྱུར་བ་ནི་འདུས་བྱས་ཀྱི་མཚན་ཉིད་ཡིན་པའི་ཕྱིར་ཏེ། རྒྱུན་གདོན་མི་ཟ་བར་གཞན་དུ་འགྱུར་བ་འདི་ནི། འདུས་བྱས་ཀྱི་རང་བཞིན་ནོ། །

[Block 4412]
དེ་ལྟ་མ་ཡིན་ན། བསམ་གཏན་རྫོགས་པས་མཉམ་པར་གཞག་པ་རྣམས་ལས་ལུས་དང་སེམས་འདྲ་བ་སྐྱེ་ན་སྐད་ཅིག་མ་དང་པོ་དང་ཁྱད་པར་མེད་པའི་ཕྱིར། ཕྱིས་ཀྱང་བདག་ལྡང་བར་མི་འགྱུར་རོ། །

[Block 4413]
གང་ལས་གང་ཞིག་སྐྱེ་བར་འགྱུར་བ་དེ་ཁོ་ན་ལས་དེ་སྐྱེ་བའི་ཕྱིར་སེམས་རྣམས་ཀྱི་རིམ་པ་ཡང་ངེས་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 4414]
དེ་མ་ཐག་པའི་རྒྱུ་ཤེས་པ་ལ༌[^1689]ནི་སངས་རྒྱས་རྣམས་མངའ་བདག༌[^1690]ཡིན་ཏེ། འདི་སྐད་དུ་རྨ་བྱའི་མདོངས་ནི་གཅིག་ལ་ཡང་། །

[Block 4415 [VERSE]]
རྒྱུ་ཡི་རྣམ་པ་ཐམས་ཅད་ནི། །
ཀུན་མཁྱེན་མིན་པས་ཤེས་བྱ་མིན། །
དེ་ཤེས་ཀུན་མཁྱེན་སྟོབས་ཡིན་ནོ། །
--- END BLOCKS ---
