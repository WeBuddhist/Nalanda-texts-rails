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
[Block 4271]
དེ་དག་ལས།

[Block 4272 [VERSE]]
གཉིས་ནི་སྟོང་དང་མི་རྟག་པར། །
མི་སློབ་པའི་ལ་དམིགས་པ་ཡིན། །

[Block 4273]
སྟོང་པ་ཉིད་སྟོང་པ་ཉིད་ནི་མི་སློབ་པའི་སྟོང་པ་ཉིད་ཀྱི་ཏིང་ངེ་འཛིན་ལ་སྟོང་པ༌[^1639]ཉིད་ཀྱི་རྣམ་པས་དམིགས་སོ། །

[Block 4274]
སྨོན་པ་མེད་པ་སྨོན་པ་མེད་པ་ཡང་མི་སློབ་པའི་སྨོན་པ་མེད་པ་ལ་མི་རྟག་པའི་རྣམ་པས་དམིགས་སོ། །

[Block 4275 [VERSE]]
མཚན་མ་མེད་པ་མཚན་མེད་ནི། །
ཞི་བར་མ་བརྟགས་ཟད་པ་ལ། །

[Block 4276]
མཚན་མ་མེད་པ་མཚན་མ་མེད་པའི་ཏིང་ངེ་འཛིན་ནི་མི་སློབ་པའི་མཚན་མ་མེད་པ་སོ་སོར༌[^1640]མ་བརྟགས་པས་འགོག་པ་ལ་ཞི་བའི་རྣམ་པས་དམིགས་སོ། །

[Block 4277]
ཏིང་ངེ་འཛིན་འདི་དག་ནི་གཅིག་ཏུ། ཟག་བཅས། འཕགས་པའི་ལམ་ལ་སྡང་བའི༌[^1641]ཕྱིར་རོ། །གང་དུ་སྐྱེད་པར༌[^1642]བྱེད་ཅེ་ན། མི་ནང་། ལྷ་དག་གི་ནང་དུ་ནི་མ་ཡིན་ནོ། །སུ་ལ་སྐྱེ་ཞེ་ན། མི་གཡོ་ལ། དགྲ་བཅོམ་པ་གཞན་ལ་ནི་མ་ཡིན་ནོ། །

[Block 4278]
ས་དུ་པ་ཞིག་ཡིན་ཞེ་ན། ཉེར་བསྡོགས་བདུན་ནི་མ་གཏོགས་སོ། །

[Block 4279]
འདོད་པའི་ཁམས་དང་། མི་ལྕོགས་པ་མེད་པ་དང་། བསམ་གཏན་ཁྱད་པར་ཅན་དང་། བསམ་གཏན་དང་། གཟུགས་མེད་པ་རྣམས་དང་། བཅུ་གཅིག་ན་ཡོད་དོ། །

[Block 4280 [HEADING]]
#### ཏིང་ངེ་འཛིན་བསྒོམ་པ་རྣམ་པ་བཞི། ^8-2-4-0

[Block 4281]
ཡང་ཏིང་ངེ་འཛིན་བསྒོམ་པ་རྣམ་པ་བཞི་གསུངས་ཏེ། དེ་ལ།

[Block 4282 [VERSE]]
དགེ་བའི་བསམ་གཏན་དང་པོ་ནི། །
བདེ་འགྱུར་ཏིང་འཛིན་བསྒོམ་པ་ཡིན། །

[Block 4283]
བདེ་བའི༌[^1643]བསམ་གཏན་དང་པོ་དག་པ་པའམ། ཟག་པ་མེད་པ་ནི། མཐོང་བའི་ཆོས་ལ་བདེ་བར་གནས་པར་འགྱུར་བའི་ཏིང་ངེ༌[^1644]འཛིན་བསྒོམ་པ་ཡིན་ནོ། །

[Block 4284]
མིང་གི་མངོན་ཤེས་མཐོང་འགྱུར་འདོད། །ལྷའི་མིག་གི་མངོན་པར་ཤེས་པ་ནི་མཐོང་བར་འགྱུར་བའི་ཏིང་ངེ་འཛིན་བསྒོམ་པ་ཡིན་ནོ། །

[Block 4285]
སྦྱོར་བ་ལས་བྱུང་བློ་དབྱེར་འགྱུར། །སྦྱོར་བའི་ཡོན་ཏན་ཁམས་གསུམ་པ་དང་། ཟག་པ་མེད་པ་ཐམས་ཅད་ནི་ཤེས་རབ་རབ་ཏུ་རྣམ་པར་འབྱེད་པར་བྱེད་པའི་ཏིང་ངེ་འཛིན་བསྒོམ་པ་ཡིན་ནོ། །

[Block 4286 [VERSE]]
རྡོ་རྗེ་ལྟ་བུའི་བསམ་གཏན་མཐའི། །
གང་ཡིན་དེ་ཟག་ཟད་འགྱུར་བསྒོམ། །

[Block 4287]
བསམ་གཏན་བཞི་པའི་རྡོ་རྗེ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་གང་ཡིན་པ་དེ་ནི་ཟག་པ་ཟད་པར་འགྱུར་བའི་ཏིང་ངེ་འཛིན་བསྒོམ་པ་ཡིན་ནོ། །

[Block 4288 [HEADING]]
### ཏིང་ངེ་འཛིན་ལ་བརྟེན་པའི་ཡོན་ཏན། ^8-3-0

[Block 4289 [HEADING]]
#### ཚད་མེད་པ་བཞི། ^8-3-1-0

[Block 4290]
ཏིང་ངེ་འཛིན་རྣམས་བཤད་ནས། དེ་ལ་བརྟེན་པའི་ཡོན་ཏན་རྣམས་བསྟན་པར་བྱ་སྟེ། ཚད་མེད་པ་ནི་བཞི་ཡིན་ནོ། །

[Block 4291]
བྱམས་པ་དང་། སྙིང་རྗེ་དང་། དགའ་བ་དང་། བཏང་སྙོམས་ཏེ། སེམས་ཅན་ཚད་མེད་པ་ལ་དམིགས་པའི་ཕྱིར་རོ། །ཅིའི་ཕྱིར་བཞི་ཁོ་ན་ཞེ་ན། གནོད་སེམས་ལ་སོགས་གཉེན་པོའི་ཕྱིར། གནོད་སེམས་དང་། རྣམ་པར་འཚེ་བ་དང་། མི་དགའ་བ་དང་། འདོད་པའི་འདོད་ཆགས་རྣམས་ཀྱི་གྲངས་བཞིན་ནོ། །

[Block 4292]
དེ་ལ།

[Block 4293 [VERSE]]
ཞེ་སྡང་མེད་བྱམས་སྙིང་རྗེ་ཡང་། །
ཞེ་སྡང་མེད་པའི་རང་བཞིན་ནོ། །
ཡིད་བདེ་བ་ནི་དགའ་བ་ཡིན། །
བཏང་སྙོམས་མ་ཆགས།

[Block 4294 [VERSE]]
མ་ཆགས་པའི་རང་བཞིན་ནོ། །
འདི་དག་གི་རྣམ་པ་ནི།
ཀྱེ་མ་བདེར་གྱུར་སྡུག་བསྔལ་དང་། །

[Block 4295]
དགར་གྱུར༌[^1645]སེམས་ཅན་རྣམས་མཉམ་པ། ཀྱེ་མ་སེམས་ཅན་རྣམས་བདེ་བར་གྱུར་ཅིག་སྙམ་པ་ཡིད་ལ་བྱེད་པ་ནས་སེམས་ཅན་རྣམས་མཉམ་མོ་སྙམ་དུ་ཡིད་ལ་བྱེད་ཅིང་སྙོམས་པར་འཇུག་པའི་བར་རོ། །

[Block 4296]
འདི་དག་གི་རྣམ་པ་བཤད་ཟིན་ཏོ། །

[Block 4297]
སྤྱོད་ཡུལ་འདོད་པའི་སེམས་ཅན་རྣམས། །དེ་ལ་དམིགས་པའི་གནོད༌[^1646]སེམས་ལ་སོགས་པའི་གཉེན་པོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4298]
དེ་དག་ས་དུ་པ་ཞིག་ཡིན་ཞེ་ན།

[Block 4299 [VERSE]]
དགའ་བ་བསམ་གཏན་གཉིས་ན་ཡོད། །
དང་པོ་དང་གཉིས་པ་ན་སྟེ།
ཡིད་བདེ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4300]
གཞན་ནི་དྲུག་ན། གཞན་གསུམ་ནི་མི་ལྕོགས་པ་མེད་པ་དང་། བསམ་གཏན་ཁྱད་པར་ཅན་དང་། བསམ་གཏན་རྣམས་དང་དྲུག་ན་ཡོད་དོ། །

[Block 4301]
ཁ་ཅིག་ལྔ། མི་ལྕོགས་པ་མེད་པ་མ་གཏོགས་པ་ཞེའོ། །

[Block 4302]
གནོད་སེམས་ལ་སོགས་གཉེན་པོའི་ཕྱིར། །ཞེས་གང་བཤད་པ། ཅི་ཚད་མེད་པ་རྣམས་ཀྱིས་ཀྱང་སྤོང་ངམ་ཞེ་ན། དེ་ཡིས་མི་སྤོང་། དེ་དག་གི་སྦྱོར་བས་གནོད་སེམས་ལ་སོགས་པ་རྣམ་པར་གནོན་པའི་ཕྱིར་གཉེན་པོར་བཤད་དོ། །

[Block 4303]
ཚད་མེད་པ་བཞི་པོ་འདི་དག་ནི། མི་དག་གི །ནང་དུ་སྐྱེད༌[^1647]དོ། །

[Block 4304]
གཞན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 4305]
ཅི་ཚད་མེད་པ་གཅིག་དང་ལྡན་པ་དེ་གདོན་མི་ཟ་བར་ཐམས་ཅད་དང་ལྡན་ནམ་ཞེ་ན། ངེས་པ་མེད་དེ། འོན་ཀྱང་། ངེས་གསུམ་ལྡན། བསམ་གཏན་གསུམ་པ་དང་། བཞི་པར་སྐྱེས་པ་དགའ་བ་དང་མི་ལྡན་ནོ། །

[Block 4306]
གསུམ་པོ་དང་ནི་རྟག་ཏུ་ལྡན་ནོ། །

[Block 4307 [HEADING]]
#### རྣམ་པར་ཐར་པ་བརྒྱད། ^8-3-2-0

[Block 4308]
རྣམ་པར་ཐར་བརྒྱད། གཟུགས་ཅན་གཟུགས་རྣམས༌[^1648]ལ་ལྟ་བ་ཞེས་བྱ་བ་ནི་དང་པོའོ། །

[Block 4309]
ནང་གཟུགས་མེད་པར་འདུ་ཤེས་པས་ཕྱི་རོལ་གྱི་གཟུགས་རྣམས་ལྟ་བ་ནི་གཉིས་པའོ། །

[Block 4310]
སྡུག་པའི་རྣམ་པར་ཐར་པ་ལུས་ཀྱིས་མངོན་སུམ་དུ་བྱས་ཏེ་རྫོགས་པར་བྱས་ནས་གནས་པ་ཞེས་བྱ་བ་ནི་གསུམ་པའོ། །
--- END BLOCKS ---
