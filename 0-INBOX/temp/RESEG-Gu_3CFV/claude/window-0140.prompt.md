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
[Block 4901]
ཞག་བཅུའམ་ཟླ་བ་ཕྱེད་ཀྱིས་དེ་འབྱུང་བར་འགྱུར་བ་ཉིད་ནི་དེའི་དུས་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བ་ནི་དགག་དབྱེ་དེའོ། །

[Block 4902]
དེའི་དུས་ཞེས་བྱ་བ་ནི་དེ་ལ་སྨོས་པའི་བཟོད་པར་བྱ་བ་དེའི་དུས་ཡིན་ནོ། །

[Block 4903]
ཁ་ཅིག་ལས་ནི་བདུན་ནམ་བརྒྱད་ན་ཞེས་བྱ་བ་ནི། ཉི་མ་བདུན་ནམ་བརྒྱད་ཀྱིས་དེ་འབྱུང་བར་འགྱུར་བ་ཉིད་ཀྱི་དུས་ན་དགག་དབྱེ་དེ་ལ་བཟོད་པར་བྱ་བ་དེའི་དུས་ཡིན་ནོ་ཞེས་ཁ་ཅིག་ལས་འབྱུང་ངོ་། །འདུས་པ་ལ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། དེའི་ཚེ་འདུས༌[^3455]ཞེས་བྱ་བར་སྦྱར་ཏེ། འདིར་དགག་དབྱེའི་དོན་དུ་འདོན་པ་ཡིན་མོད་ཀྱི་འདུས་པ་གཞན་ལ་ཡང་དེ་བཞིན་དུ་འདི་རིགས་པ་མ་ཡིན་ནོ། །

[Block 4904]
དེའི་ཕྱིར་འདིར་བྱེ་བྲག་ཏུ་མ་བྱས་སོ། །

[Block 4905]
དེས་བཟོད་པར༌[^3456]མ་བྱས་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ནང་དང་བཅས་པ་དེས་བཟོད་པར༌[^3457]མ་བྱས་པར་དགག་དབྱེ་མི་བྱའོ། །

[Block 4906]
དེའི་ཚེ་འདུས་པ་ཐམས་ཅད་ཀྱིས་ཕན་ཚུན་ཀུན་དགའ་བར་མ་བྱས་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ཕྱག་ལ་སོགས་པས་ཕན་ཚུན་ཀུན་དགའ་བར་མ་བྱས་པར་གང་གིས་དེ་ཕན་ཚུན་ཀུན་དགའ་བར་མ་བྱས་པར་མི་བྱའོ། །གང་གི་རྣམས་ཀྱིས་ཤེ་ན། དེའི་ཕྱིར་དེའི༌[^3458]ཚེ་གནས་ཀྱི་གཞི་དེར་འདུས་པ་ཐམས་ཅད་ཀྱིས་ཞེས་བྱ་བ་སྨོས་ཏེ། ཅི་གང་ཞིག་ནང༌[^3459]དང་བཅས་པར་འགྱུར་བ་གང་ལ་ཡང་དེ་འབྱུང་བར་མི་འགྱུར་བ་དེ་ཉིད་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་ཐམས་ཅད་ཀྱིས་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 4907]
ཅི་ཞག༌[^3460]བཅུའམ། ཟླ་བ་ཕྱེད་ན་འབྱུང་བར་འགྱུར་བ་ཉིད་ན་ཕན་ཚུན་ཀུན་དགའ་བར་མ་བྱས་པར་མི་བྱ་བའམ་ཞེ་ན། དགག་དབྱེའི་དུས་སོ། །

[Block 4908]
དེའི་ཚེ་གཤེ་བ་ལ་བཟོད་པར་མི་གསོལ་བར་མི་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགག་དབྱེའི་དུས་འབའ་ཞིག༌[^3461]ཏུ་མ་ཟད་ཀྱི་དུས་གཞན་གྱི་ཚེ་ཡང་ངོ་། ། སིལ་བུ་དག་ལས་མི་འདོད་པ་ལས་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་སོགས་པ་དང་། ཇི་སྲིད་དུ་བཟོད་པ་མ་ཡིན་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་ཕྲན་ཚེགས་ལྷག༌[^3462]མ་རྣམས་ལས་སོ། །

[Block 4909]
དགེ་སློང་མས་དགེ་སློང་ལ་གནས་ཀྱི་ཕྱི་རོལ་དུ་བཟོད་པར་གསོལ་བར་མི་བྱའོ། །

[Block 4910]
རྐང་པ་གཉིས་ལ་ཕྱག་བྱས་ཏེ་མི་བྱའོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་མས་དགེ་སློང་ལ་བཟོད་པར་གསོལ་བར་མི་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 4911]
བཟོད་ན་ཕྱག་བྱ་སྟེ་འགྲོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་གིས་བཟོད་ན་དགེ་སློང་མས་དགེ་སློང་གི་རྐང་པ་གཉིས་ལ་ཕྱག་བྱ་སྟེ་འགྲོ་བར་བྱའོ། །

[Block 4912]
བཟོད་པ་གསོལ་བར་བྱེད་པ་དེ་ལ་དགེ་སློང་གིས་མ་གུས་པར་བྱ་སྟེ་འགྲོ་བར་མི་བྱའོ། །

[Block 4913]
འདའ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་མ་བཟོད་པར་གསོལ་བར་བྱེད་པ་དེ་ལས།

[Block 4914]
དགེ་སློང་གིས་འདའ་བར་མི་བྱ་སྟེ་བཟོད་པ་དང་དུ་བླང་བར་བྱའོ། །

[Block 4915]
བཟོད་པར་བྱ་བ་ལ༌[^3463]སྔར་ཤེས་པ་ཤད་ཀྱིས་སྦྱང་དུ་གཞུག་པར་བྱའོ། །

[Block 4916]
མི་འདོད་ན་ཐབས་བཙལ་བ་ལ་མི་འབད་པར༌[^3464]མི་བྱའོ་ཞེས་བྱ་བ་ལ། མི་འབད་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི། བཟོད་པ་གསོལ་བར་བྱ་བ་དེ་བཟོད་པར་མི་འདོད་ན། དེའི་ཕྱིར་མི་བསྒྱང༌[^3465]ངོ་། །ཀུན་ནས་དཀྲིས་པ་དང་མ་བྲལ་གྱི་བར་དུ་མི་བསྡད་པར་མི་བྱའོ། །

[Block 4917]
བཟོད་པ་གསོལ་བར་བྱེད་པ་ལ་མི་བཟོད་པར་མི་བྱའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 4918]
དགག་དབྱེའི་གཞི་དང་འབྲེལ་བ་ཕྲན་ཚེགས་ལ་སོགས་པའི་སྐབས་སོ། །

[Block 4919]
དགག་དབྱེའི་གཞི་རྫོགས་སོ།། །།
--- END BLOCKS ---
