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

[Block 4626]
ཅི་ཡང་མེད་པའི་སྐྱེ་མཆེད་ཀྱི་ས་པའི་སེམས་ཟག་པ་མེད་པས་དེ་ལས་ལྡང་སྟེ། དེ་ལྟར་ན་དེའི་སྙོམས་པར་འཇུག་པའི་སེམས་ནི་ཟག་པ་དང་བཅས་པ་ཡིན་ལ། ལྡང་བའི་སེམས་ནི་ཟག་པ་དང་བཅས་པ་དང་།

[Block 4627]
ཟག་པ་མེད་པ་ཡང་ཡིན་ནོ། །

[Block 4628 [HEADING]]
##### རྣམ་པར་ཐར་པའི་དམིགས་པ། ^5-17-2-5-0

[Block 4629 [VERSE]]
རྣམ་པར་ཐར་པ་འདི་དག་ལས། །
དང་པོ་འདོད་གཏོགས་སྣང་ཡུལ་ཅན། །

[Block 4630]
འདི་དག་གི་དམིགས་པ་ནི་ཅི་རིགས་པར་འདོད་པ་ན་སྤྱོད་པའི་གཟུགས་ཀྱི་སྐྱེ་མཆེད་ཡིད་དུ་མི་འོང་བ་དང་ཡིད་དུ་འོང་བ་ཡིན་ནོ། །

[Block 4631 [VERSE]]
གང་དག་གཟུགས་ཅན་མིན་དེ་དག །
སྤྱོད་ཡུལ་གོང་དང་རང་གི་སའི། །
སྡུག་བསྔལ་སོགས་དང་རྗེས་ཤེས་ཕྱོགས། །

[Block 4632]
གཟུགས་མེད་པའི་རྣམ་པར་ཐར་པ་རྣམས་ཀྱི་དམིགས་པ་ནི་རང་གི་ས་པ་དང་ས་གོང་མ་པའི་སྡུག་བསྔལ་དང་དེའི་རྒྱུ་དང་འགོག་པ་དག༌[^3297]རྗེས་སུ་ཤེས་པའི་ཕྱོགས་དང་མཐུན་པའི་ལམ་ཐམས་ཅད་ཡིན་ནོ། །

[Block 4633]
སོ་སོར་མ་བརྟགས་པས་འགོག་པ་ཡང་ཡིན་ནོ་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 4634]
ནམ་མཁའ་ཡང་གཅིག་གིས་ཡིན་ནོ་ཞེས་བརྗོད་པར་བྱ་སྟེ། ཅིའི་ཕྱིར་བསམ་གཏན་གསུམ་པ་ལ་རྣམ་པར་ཐར་པ་མ་བཞག་ཅེ་ན། བསམ་གཏན་གཉིས་པའི་ས་པའི་ཁ་དོག་གི་འདོད་ཆགས་མེད་པའི་ཕྱིར་དང་། བདེ་བའི་སྙིང་པོས་སྐྱེད་པའི༌[^3298]ཕྱིར་རོ། །

[Block 4635]
ཅིའི་ཕྱིར་སྡུག་པའི་རྣམ་པར་ཐར་པ་སྐྱེད་པར་བྱེད་ཅེ་ན། མི་སྡུག་པས་རྒྱུད་ཞུམ་པར༌[^3299]རབ་ཏུ་དགའ་བར་བྱ་བའམ། ཅི་མི་སྡུག་པའི་རྣམ་པར་ཐར་པ་དག་གྲུབ་པ་ཡིན་ནམ་མ་ཡིན་ཞེས་བརྟག་པའི་ཕྱིར་ཏེ། གལ་ཏེ་སྡུག་པར་ཡིད་ལ་བྱས་ཀྱང་ཉོན་མོངས་པ་མི་སྐྱེ་ན་དེ་ལྟ་ན་དེ་གཉིས་གྲུབ་པ་ཡིན་ནོ། །

[Block 4636]
རྣལ་འབྱོར་པ་རྣམས་ནི་རྒྱུ་གཉིས་ཀྱིས༌[^3300]རྣམ་པར་ཐར་པ་ལ་སོགས་པ་སྐྱེད་པར་བྱེད་དོ། །

[Block 4637]
[^3301]ཉོན་མོངས་པ་མེད་པ་ལ་སོགས་པའི་ཡོན་ཏན་མངོན་པར་བསྒྲུབ་པའི་ཆེད་དང་། འཕགས་པའི་རྫུ་འཕྲུལ་མངོན་པར་གྲུབ་པའི་ཆེད་དུ། ཉོན་མོངས་པ་ཐག་བསྲིང་བར༌[^3302]བྱ་བའི་ཕྱིར་དང་། སྙོམས་པར་འཇུག་པ་ལ་དབང་བར་བྱ་བའི་ཕྱིར་རོ། །

[Block 4638]
དེ་ཡང་གང་གིས་དངོས་པོ་ཡོངས་སུ་བསྒྱུར་བ་དང་། བྱིན་གྱིས་རློབ་པ་དང་། ཚེ་གཏོང་བ་ལ་སོགས་པར་བྱེད་པའོ། །

[Block 4639]
ཅིའི་ཕྱིར་གསུམ་པ་དང་བརྒྱད་པ་དག་ཁོ་ན་མངོན་སུམ་དུ་བྱ་བར་བཤད་ལ་གཞན་དག་ནི་མ་ཡིན་ཞེ་ན། གཙོ་བོ་ཡིན་པའི་ཕྱིར་དང་། ཁམས་དང་།

[Block 4640]
སའི་མཐའ་ན་གནས་པའི་ཕྱིར་རོ། །

[Block 4641 [HEADING]]
#### ཟིལ་གྱིས་གནོན་པའི་སྐྱེ་མཆེད་བརྒྱད། ^5-17-3-0

[Block 4642]
ཟིལ་གྱིས་གནོན་པའི་སྐྱེ་མཆེད་བརྒྱད། །

[Block 4643]
ནང་གཟུགས་སུ་འདུ་ཤེས་པས་ཕྱི་རོལ་གྱི་གཟུགས་ཆུང་ངུ་ཁ་དོག་བཟང་པོ་དང་ཁ་དོག་ངན་པ་རྣམས་ལ་ལྟ་ཞིང་གཟུགས་དེ་དག་ཟིལ་གྱིས་མནན་ནས་ཤེས།[^3303] ཟིལ་གྱིས་མནན་ནས་མཐོང་སྟེ། དེ་ལྟ་བུར་འདུ་ཤེས་པར་གྱུར་པ་འདི་ནི་ཟིལ་གྱིས་གནོན་པའི་སྐྱེ་མཆེད་དང་པོ་ཡིན་ནོ། །

[Block 4644]
དེ་བཞིན་དུ་ཆེན་པོ་རྣམས་དང་། དེ་ཁོ་ན་བཞིན་དུ་ནང་གཟུགས་མེད་པར་འདུ་ཤེས་པ་སྟེ། དེ་ལྟར་བཞི་པོ་དེ་དག་དང་། གཟུགས་མེད་པར་འདུ་ཤེས་པ་ཁོ་ན་སྔོན་པོ་དང་སེར་པོ་དང་དམར་པོ་དང་དཀར་པོ་རྣམས་ལ་ལྟ་བ་སྟེ། དེ་ལྟར་ན་བརྒྱད་ཡིན་ནོ། །

[Block 4645]
དེ་དག་ལས་གཉིས་ནི་རྣམ་པར་ཐར་པ༌[^3304]

[Block 4646]
དང་པོ་བཞིན་ནོ། །

[Block 4647]
[^3305]རྣམ་པར་ཐར་པ་དང་པོ་ཇི་ལྟ་བར་ཟིལ་གྱིས་གནོན་པའི་སྐྱེ་མཆེད་གཉིས་པོ་དང༌[^3306]

[Block 4648]
གཉིས་པ་ཡང་དེ་དང་འདྲའོ། །

[Block 4649]
གཉིས་ནི་གཉིས་པ་བཞིན་ནོ། །

[Block 4650]
རྣམ་པར་ཐར་པ་གཉིས་པ་ཇི་ལྟ་བར་ཟིལ་གྱིས་གནོན་པོའི༌[^3307]སྐྱེ་མཆེད་གཉིས་པོ་གསུམ་པ་དང་བཞི་པ་ཡང་དེ་དང་འདྲའོ། །

[Block 4651]
གཞན་སྡུག་པའི་རྣམ་པར་ཐར་པ་བཞིན། སྡུག་པའི་རྣམ་པར་ཐར་པ་ཇི་ལྟ་བར་གཞན་བཞི་ཡང་དེ་དང་འདྲའོ། །

[Block 4652]
འདི་ནི་ཁྱད་པར་ཡིན་ཏེ། དེ་དག་གིས་ནི་རྒྱབ་ཀྱིས་ཕྱོགས་པ་ཙམ་དུ་ཟད་ལ། འདི་དག་གིས་ནི་དམིགས་པ་ཟིལ་གྱིས་གནོན་ཏེ། ཇི་ལྟར་འདོད་པ་བཞིན་དུ་མོས་པའི་ཕྱིར་དང་། ཉོན་མོངས་པ་མི་སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 4653 [HEADING]]
#### ཟད་པར་བཅུ། ^5-17-4-0

[Block 4654]
ཟད་པར་བཅུའོ། །

[Block 4655]
བར་ཆད་མེད་པར་ཟད་པར་རྒྱས་པར་བྱེད་པའི་ཕྱིར་ཟད་པར་གྱི་སྐྱེ་མཆེད་ནི་བཅུ་སྟེ། ཟད་པར་ས་དང་། ཆུ༌[^3308]དང་། མེ༌[^3309]དང་། རླུ་དང་། སྔོན་པོ་དང་སེར་པོ་དང་། དམར་པོ་དང་དཀར་པོ་དང་། ཟད་པར་ནམ་མཁའ་དང་། རྣམ་ཤེས་མཐའ་ཡས་སྐྱེ་མཆེད་དོ། །

[Block 4656]
དེ་རྣམས་ལས།

[Block 4657]
[^3310] བརྒྱད་མ་ཆགས།

[Block 4658]
དང་པོ་བརྒྱད་ནི་མ་ཆགས་པའི་རང་བཞིན་དག་ཡིན་ནོ། །

[Block 4659]
བསམ་གཏན་མཐའ་ན། བསམ་གཏན་བཞི་པ་ཁོ་ན་ན་ཡོད་དོ། །

[Block 4660]
སྤྱོད་ཡུལ་ནི། འདོད་པ། འདོད་པ་ན་སྤྱོད་པའི་གཟུགས་ཀྱི་སྐྱེ་མཆེད་ཡིན་ནོ། །
--- END BLOCKS ---
