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
[Block 4586]
དེ་ནས་འབྲིང་དང་ཆེན་པོ་ལ་མོས་པར་བྱེད་དོ། །

[Block 4587]
གལ་ཏེ་དེ་ལ་མཛའ་བོ་ཆེན་པོའི་ཕྱོགས་བཞིན་དུ་བདེ་བར་མོས་པ་མི་ལྡོག་པར་གྱུར་ན་དེའི་འོག་ཏུ་རིམ་གྱིས་ཁྱིམ་དང་གྲོང་དང་ཡུལ་འཁོར་གྱི་བར་དུ་བདེ་བར་མོས་པར་བྱས་ནས་ཕྱོགས་གཅིག་ནས་འཇིག་རྟེན་ཐམས་ཅད་ཀྱི་བར་དུ་བྱམས་པ་རྒྱས་པར་བྱེད་དོ། །

[Block 4588]
གང་ཞིག་ཐམས་ཅད་དུ་ཡོན་ཏན་འཛིན་པ་དེ་ནི་བྱམས་པ་མྱུར་དུ་སྐྱེད་པར་བྱེད་དོ། །

[Block 4589]
སྔོན་གྱི་བསོད་ནམས་དང་བསོད་ནམས་མ་ཡིན་པའི་འབྲས་བུ་སྣང་བའི་སྒོ་ནས་དགེ་བའི་རྩ་བ་ཀུན་དུ་ཆད་པ་ལ་ཡང་ཡོན་ཏན་གཟུང་བར༌[^3286]ནུས་ལ། རང་སངས་རྒྱས་ལ༌[^3287]ཡང་སྐྱོན་གཟུང་བར༌[^3288]ནུས་སོ། །

[Block 4590]
སྙིང་རྗེ་དང་དགའ་བ་ལ་ཡང་དེ་བཞིན་དུ་སེམས་ཅན་སྡུག་བསྔལ་བ༌[^3289]རྣམ་པ་མང་པོའི་ཆུ་བོར་བྱིང་བ་འདི་དག་སྡུག་བསྔལ་ལས་མྱུར་དུ་ཐར་ཀྱང་ཅི་མ་རུང་། མངོན་པར་དགའ་བར་གྱུར་ཀྱང་ཅི་མ་རུང་སྙམ་དུ་མོས་ཤིང་དགའ་བ་ལ༌[^3290]སྦྱོར་བར་བྱེད་དོ། །

[Block 4591]
བཏང་སྙོམས་ནི་ཐ་མལ་པའི་ཕྱོགས་ལས་རྩོམ་མོ། །

[Block 4592 [HEADING]]
##### ཚད་མེད་པ་སྐྱེད་པའི་རྟེན་དང་ལྡན་པ། ^5-17-1-8-0

[Block 4593]
ཚད་མེད་པ་བཞི་པོ་འདི་དག༌[^3291]ནི་མི་དག་གི་ནང་དུ་སྐྱེད༌[^3292]དོ། །

[Block 4594]
མི་རྣམས་ཀྱི་ནང་དུ་སྐྱེད་ཀྱི་གཞན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 4595]
ཅི་ཚད་མེད་པ་གཅིག་དང་ལྡན་པ་གང་ཡིན་པ་དེ་ནི་གདོན་མི་ཟ་བར་ཐམས་ཅད་དང་ལྡན་ནམ་ཞེ་ན། ཐམས་ཅད་དང་ལྡན་པ་ནི་ངེས་པ་མེད་དོ། །

[Block 4596]
འོན་ཀྱང་ངེས་གསུམ་ལྡན། བསམ་གཏན་གསུམ་པ་དང་བཞི་པར་སྐྱེས་པ་དག༌[^3293]དགའ་བ་དང་མི་ལྡན་ནོ། །

[Block 4597]
ཚད་མེད་པ་གསུམ་དང་ནི་རྟག་ཏུ་ལྡན་པ་ཡིན་ནོ། །

[Block 4598 [HEADING]]
#### རྣམ་པར་ཐར་པ་བརྒྱད། ^5-17-2-0

[Block 4599]
རྣམ་པར་ཐར་པ༌[^3294]བརྒྱད། གཟུགས་ཅན་གཟུགས་རྣམས་ལ་ལྟ་བ་ཞེས་བྱ་བ་ནི་རྣམ་པར་ཐར་པ་དང་པོ་ཡིན་ནོ། །

[Block 4600]
ནང་གཟུགས་མེད་པར་འདུ་ཤེས་པས་ཕྱི་རོལ་གྱི་གཟུགས་རྣམས་ལ་ལྟ་བ་ཞེས་བྱ་བ་ནི་གཉིས་པ་ཡིན་ནོ། །

[Block 4601]
སྡུག་པའི་རྣམ་པར་ཐར་པ་ལུས་ཀྱིས་མངོན་སུམ་དུ་བྱས་ཏེ་རྫོགས་པར་བྱས་ནས་གནས་ཞེས་བྱ་བ་ནི་གསུམ་པ་ཡིན་ནོ། །

[Block 4602]
གཟུགས་མེད་པ་བཞི་དང་།

[Block 4603]
བརྒྱད་པ་འདུ་ཤེས་དང་ཚོར་བ་འགོག་པའོ། །

[Block 4604 [HEADING]]
##### རྣམ་པར་ཐར་པ་དང་པོ་གཉིས། ^5-17-2-1-0

[Block 4605]
དེ་རྣམས་ལས། དང་པོ་གཉིས། མི་སྡུག །རྣམ་པར་ཐར་པ་དང་པོ་གཉིས་ནི་རྣམ་པར་བསྔོས་པ༌[^3295]ལ་སོགས་པའི་རྣམ་པ་ཅན་ཡིན་པའི་ཕྱིར་མི་སྡུག་པའི་རང་བཞིན་དག་ཡིན་ཏེ། དེ་ཉིད་ཀྱི་ཕྱིར་དེ་གཉིས་ཀྱི་ཚུལ་ནི་མི་སྡུག་པ་བཞིན་དུ་རིག་པར་བྱའོ། །

[Block 4606]
དེ་གཉིས་ཀྱང་བསམ་གཏན་གཉིས་ན་ཡོད། བསམ་གཏན་དང་པོ་དང་གཉིས་པ་དག་ན་ཡོད་ཀྱི་ས་གཞན་ན་ནི་མེད་དོ། །

[Block 4607]
འདོད་པ་ན་སྤྱོད་པ་དང་བསམ་གཏན་དང་པོའི་ས་པའི་ཁ་དོག་གི་འདོད་ཆགས་ཀྱི་གཉེན་པོར་གྲངས་བཞིན་ནོ། །

[Block 4608 [HEADING]]
##### སྡུག་པའི་རྣམ་པར་ཐར་པ། ^5-17-2-2-0

[Block 4609]
གསུམ་པ་མཐའ་ན། སྡུག་པའི་རྣམ་པར་ཐར་པ་ནི་བསམ་གཏན་བཞི་པ་ན་ཡོད་དོ། །

[Block 4610]
དེ་མ་ཆགས། དེ་ཡང་མ་ཆགས་པའི་རང་བཞིན་ཡིན་གྱི་སྡུག་པའི་རྣམ་པ་ཅན་ཡིན་པའི་ཕྱིར་མི་སྡུག་པའི་རང་བཞིན་ནི་མ་ཡིན་ནོ། །

[Block 4611]
དེ་དག་འཁོར་དང་བཅས་ན་ནི་ཕུང་པོ་ལྔའི་རང་བཞིན་ཡིན་ནོ། །

[Block 4612 [HEADING]]
##### གཟུགས་མེད་པའི་རྣམ་པར་ཐར་པ། ^5-17-2-3-0

[Block 4613]
གཟུགས་མེད་པའི་རྣམ་པར་ཐར་པ་རྣམས་ནི། གཟུགས་མེད་མཉམ་གཞག་དགེ་རྣམས་སོ། །

[Block 4614]
གཟུགས་མེད་པའི་མཉམ་པར་བཞག་པ་དགེ་བ་རྣམས་ཁོ་ན་རྣམ་པར་ཐར་པ་ཞེས་བྱ་བའི་མིང་འཐོབ་ཀྱི། ཉོན་མོངས་པ་ཅན་རྣམས་ཀྱང་མ་ཡིན་ལ། མཉམ་པར་མ་བཞག་པ་རྣམས་ཀྱང་མ་ཡིན་ནོ། །

[Block 4615]
འདི་ལྟ་སྟེ་འཆི་བའི་སྲིད་པའི་ཚེ་ལྟ་བུའོ། །

[Block 4616]
གཞན་དག་ན་རེ་གཞན་ན་ཡང་མཉམ་པར་མ་བཞག་པ་ཡོད་དོ་ཞེས་ཟེར་རོ། །

[Block 4617]
ཉེར་བསྡོགས་ཀྱི་རྣམ་པར་གྲོལ་བའི་ལམ་དག་ཀྱང་རྣམ་པར་ཐར་པ་ཞེས་བྱ་བའི་མིང་འཐོབ་པོ། །འོག་མ་ལ་དམིགས་པའི་ཕྱིར་བར་ཆད་མེད་པའི་ལམ་རྣམས་ནི་མ་ཡིན་ཏེ། རྣམ་པར་ཐར་པའི་དོན་ནི་རྒྱབ་ཀྱིས་ཕྱོགས་པའི་དོན་ཡིན་ནོ། །

[Block 4618 [HEADING]]
##### འགོག་པའི་སྙོམས་པར་འཇུག་པ། ^5-17-2-4-0

[Block 4619]
འགོག་པའི་སྙོམས་པར་འཇུག་པའོ། །

[Block 4620]
རྣམ་པར་ཐར་པ་བརྒྱད་པ་འདུ་ཤེས་དང་ཚོར་བ་འགོག་པ་ནི་འགོག་པའི་སྙོམས་པར་འཇུག་པ་ཡིན་ཏེ། དེ་ནི་སྔར་བཤད་ཟིན་ཏོ། །

[Block 4621]
འདུ་ཤེས་དང་ཚོར་བའམ། འདུ་བྱེད་ཐམས་ཅད་ལ་རྒྱབ་ཀྱིས་ཕྱོགས་པའི་ཕྱིར་རོ། །

[Block 4622]
གཞན་དག་ན་རེ་སྙོམས་པར་འཇུག་པའི་སྒྲིབ་པ་ལས་རྣམ་པར་ཐར་པའི་ཕྱིར་རྣམ་པར་ཐར་པ་ཞེས་བྱའོ་ཞེས་ཟེར་རོ། །

[Block 4623]
དེ་ལ་ནི། ཕྲ་བ་ཕྲ་བའི་མཇུག་ཐོགས་སུ། །སྙོམས་པར་འཇུག་སྟེ། སྲིད་པའི་རྩེ་མོའི་འདུ་ཤེས་ནི་ཕྲ་བ་ཡིན་ཏེ། དེ་བས་ཀྱང་ཆེས་ཕྲ་བར་བྱས་ནས་འགོག་པའི་སྙོམས་པར་འཇུག་གོ། །

[Block 4624]
སྙོམས་པར་ཞུགས་པ་རྣམས་ནི།

[Block 4625 [VERSE]]
རང་གི་དག་དང་འོག་མ་ཡིན། །
འཕགས་པའི་སེམས་ཀྱིས༌[^3296]དེ་ལས་ལྡང་། །
སྲིད་པའི་རྩེ་མོའི་སེམས་དག་པའམ། །
--- END BLOCKS ---
