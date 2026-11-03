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
[Block 3606]
འདི་ནི་གཞི་ཡོད་དོ་ཞེས་བྱ་བར་ཤེས་པར་འགྱུར་རོ་ཞེས་འབྱུང་ངོ་། །གལ་ཏེ་གང་ལས་འདི་ནི་གནས་ཡོད་དོ། །

[Block 3607]
འདི་ནི་གཞི་ཡོད་དོ་ཞེས་དེ་སྙམ་དུ་ཤེས་པར་འགྱུར་རོ་ཞེས་བྱ་བ་འདིའི་དོན་ནི་འདི་མ་ཡིན་ཏེ། འོན་ཀྱང་མི་རྟག་པ་ལ་སོགས་པ༌[^2533]ཤེས་པར་འགྱུར་བ་གང་ཡིན་པ་འདི་ནི་གནས་ཡོད་དོ། །

[Block 3608]
འདི་ནི་གཞི་ཡོད་དོ་ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 3609]
ཞེ་ན། མ་ཡིན་ཏེ། གཞན་ནས་མི་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 3610]
གལ་ཏེ་འདི་བསྟན་བཅོས་ཀྱི་དོན་ཡིན་པར་འགྱུར་ན། འདི་སྐད་དུ་མཐོང་བས་སྤང་བར་བྱ་བའི་སེམས་ཀྱིས༌[^2534]འདོད་པ་དང་ལྡན་པའི་ཆོས་རྣམས་ཤེས་པར་འགྱུར་བ་ཡོད་དམ་ཞེ་ན། ཤེས་པར་འགྱུར་ཏེ། རིགས་པ་མ་ཡིན་པས་བསྐྱེད་པའི་སྒོ་ནས་བདག་དང་། བདག་གི་དང་། རྟག་པ་དང་། ཆད་པ་དང་། རྒྱུ་མེད་པ་དང་། བྱེད་པ་མེད་པ་དང་། སྐུར་བ་འདེབས་པ་དང་། མཆོག་དང་། གཙོ་བོ་དང་། ཁྱད་པར་དུ་འཕགས་པ་དང་། དམ་པ་དང་། དག་པ་དང་། གྲོལ་བ་དང་། ངེས་པར་འཛིན་པར་བྱེད་པ་དང་། ནེམ་ནུར་དང་། ཡིད་གཉིས་དང་། ཐེ་ཚོམ་དུ་ཤེས་པར་འགྱུར་ཞིང་། ཆགས་པ་དང་། སྡང་བ་དང་། རློམ་པ་དང་། རྨོངས་པར་འགྱུར་རོ་ཞེས་གང་གསུངས་པ་དེར་ཡང་འདི་སྐད་དུ་འདི་ནི་གནས་ཡོད་དོ། །

[Block 3611]
འདི་ནི༌[^2535]གཞི་ཡོད་དོ་ཞེས་འབྱུང་བར་འགྱུར་བ༌[^2536]ཞིག་ན། དེ་སྐད་ཀྱང་མི་འབྱུང་སྟེ། དེ་ལྟ་བས་ན་འདི་ནི་དེའི་དོན་མ་ཡིན་ནོ། །

[Block 3612 [HEADING]]
### རྣམ་པ་བཅུ་དྲུག། ^4-5-0

[Block 3613]
ཅི་རྣམ་པ་བཅུ་དྲུག་པོ་འདི་དག་མིང་གི་སྒོ་ནས་སམ། འོན་ཏེ་རྫས་སུ་ཞེ་ན། ཁ་ཅིག་ན་རེ་རྫས་སུ་ནི༌[^2537]བདུན་ཡིན་ལ་མིང་གི་སྒོ་ནས་ནི་བཅུ་དྲུག་ཡིན་ཏེ། ཀུན་འབྱུང་དང་། འགོག་པ་དང་། ལམ་རྣམས་རྫས་སུ༌[^2538]རེ་རེ་ཡིན་པའི་ཕྱིར་རོ་ཞེས་ཟེར་རོ། །

[Block 3614]
འདི་སྐད་དུ་བརྗོད་དེ་རྫས་སུ་རྣམ་པ་བཅུ་དྲུག་གོ། །

[Block 3615]
དེ་ལ་རྐྱེན་ལ་རག་ལུས་པའི་ཕྱིར་མི་རྟག་པའོ། །

[Block 3616]
གནོད་པའི་བདག་ཉིད་ཡིན་པའི་ཕྱིར་སྡུག་བསྔལ་བའོ། །

[Block 3617]
བདག་གིར་ལྟ་བའི་མི་མཐུན་པའི་ཕྱོགས་ཀྱིས༌[^2539]སྟོང་པའོ། །

[Block 3618]
བདག་ཏུ་ལྟ་བའི་མི་མཐུན་པའི་ཕྱོགས་ཀྱིས་བདག་མེད་པའོ། །

[Block 3619]
ས་བོན་གྱི་ཆོས་ཀྱི་ཚུལ་གྱིས་རྒྱུའོ། །

[Block 3620]
འབྱུང་བའི་ཆོས་ཀྱི༌[^2540]ཚུལ་གྱིས་ཀུན་འབྱུང་བའོ། །

[Block 3621]
འབྲེལ་པའི་ཚུལ་གྱིས་རབ་ཏུ་སྐྱེ་བའོ། །

[Block 3622]
མངོན་པར་སྒྲུབ་པའི་དོན་གྱིས་ནི༌[^2541]རྐྱེན་ཏེ། དཔེར་ན་འཇིམ་པའི་གོང་བུ་དང་ཐལ་ཞར་དང་འཁོར་ལོ་དང་ཐག་གུ་དང་ཆུ་རྣམས་འདུས་པ་ལས་བུམ་པ་མངོན་པར་གྲུབ་པ་དེ་བཞིན་ནོ། །

[Block 3623]
ཕུང་པོ་ཞིག་པའི་ཕྱིར་འགོག་པའོ། །

[Block 3624]
མེ་གསུམ་ཞི་བའི་ཕྱིར་ཞི་བའོ། །

[Block 3625]
འཚེ་བ་མེད་པའི་ཕྱིར་གྱ་ནོམ་པའོ། །

[Block 3626]
སྐྱོན་ཐམས་ཅད་དང་བྲལ་བའི་ཕྱིར་ངེས་པར་འབྱུང་བའོ། །

[Block 3627]
བགྲོད་པའི་དོན་གྱིས༌[^2542]ལམ་མོ། །

[Block 3628]
རིགས་པ་དང་ལྡན་པའི་ཕྱིར་རིགས་པའོ། །

[Block 3629]
ཡང་དག་པར་བསྒྲུབ་པའི་དོན་གྱིས་སྒྲུབ༌[^2543]པའོ། །

[Block 3630]
ཤིན་ཏུ་ཡང་དག་པར་འདའ་བར་བྱེད་པའི་ཕྱིར་ངེས་པར་འབྱིན་པར་བྱེད་པའོ། །

[Block 3631]
ཡང་ན་གཏན་དུ་བ་མ་ཡིན་པའི་ཕྱིར་མི་རྟག་པའོ། །

[Block 3632]
ཁུར་ལྟ་བུར་གྱུར་པའི་ཕྱིར། སྡུག་བསྔལ་བའོ། །

[Block 3633]
ནང་གི་སྐྱེས་བུ་དང་བྲལ་བའི་ཕྱིར་སྟོང་པའོ། །

[Block 3634]
འདོད་དགུར་བྱེད་པ་མེད་པའི་ཕྱིར་བདག་མེད་པའོ། །

[Block 3635]
འོང་བའི་ཚུལ་གྱིས་རྒྱུའོ། །

[Block 3636]
འབྱུང་བའི་ཚུལ་གྱིས་ཀུན་འབྱུང་བའོ། །

[Block 3637]
འཕེལ་བའི་ཚུལ་གྱིས་རབ་ཏུ་སྐྱེ་བའོ། །

[Block 3638]
སོ་སོར་འབྲང་བའི་ཚུལ༌[^2544]གྱིས་རྐྱེན་ནོ། །

[Block 3639]
འབྲེལ་བ་མེད་པས་འབྲེལ་པ་ཞིག་པའི་ཕྱིར་འགོག་པའོ། །

[Block 3640]
འདུས་བྱས་ཀྱི་མཚན་ཉིད་གསུམ་དང་འབྲལ༌[^2545]བའི་ཕྱིར་ཞི་བའོ། །

[Block 3641]
དགེ་བའི་ཕྱིར་གྱ་ནོམ་པའོ། །

[Block 3642]
ཡིད་བརྟན་པའི༌[^2546]མཆོག་ཡིན་པའི་ཕྱིར་ངེས་པར་འབྱུང་བའོ། །

[Block 3643]
ལམ་ངན་པའི་མི་མཐུན་པའི་ཕྱོགས་ཀྱིས་ལམ་མོ། །

[Block 3644]
རིགས་པ་མ་ཡིན་པའི་མི་མཐུན་པའི་ཕྱོགས་ཀྱིས་རིགས་པའོ། །

[Block 3645]
མྱ་ངན་ལས་འདས་པའི་གྲོང་དང་། མི་འགལ་བའི་དོན་གྱིས་སྒྲུབ་པའོ། །
--- END BLOCKS ---
