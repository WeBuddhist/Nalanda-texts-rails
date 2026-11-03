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
རིང་བ་དེ་དག་ཀྱང་གོ་རིམས་བཞིན་དུ། ཉི་མ་ལྷོ་བྱང་འགྲོ་ཚེའོ། །

[Block 3607]
ཉི་མ་འཛམ་བུའི་གླིང་གི་ལྷོ་ཕྱོགས་ཀྱི་ངོས་སུ་འགྲོ་བ༌[^2068]མཚན་མོ་རིང་ངོ་། །བྱང་ཕྱོགས་སུ་འགྲོ་བ་ན་ཉིན་མོ་རིང་ངོ་། །ཟླ་བ་ཡར་གྱི་ངོའི་དང་པོའི་ཟླ་བའི་དཀྱིལ་འཁོར་མ་རངས་པར་སྣང་བ་དེ་ལ་རྒྱུ་ཅི་ཡོད་ཅེ་ན།

[Block 3608 [VERSE]]
ཉི་མ་དང་ནི་ཉེ་བ་ལས། །
རང་གི་གྲིབ་མས་འགྲིབ་པར་སྣང་། །

[Block 3609]
བཏགས་པ༌[^2069]ལས།

[Block 3610]
གང་གི་ཚེ་ཟླ་བའི་གཞལ་མེད་ཁང་ཉི་མའི་གཞལ་མེད་ཁང་དང་ཉེ་བར་རྒྱུ་བ་དེའི་ཚེ་ཉི་མའི་འོད་ཀྱིས་དེའི་གཞལ་མེད་ཁང་ལ་འབབ་སྟེ། དེས་ན་དེའི་ཕྱི་རོལ་གྱི་ངོས་སུ་གྲིབ་མ་བབ་པས་དཀྱིལ་འཁོར་མ་རངས་པར་སྣང་ངོ་ཞེས་བསྟན་ཏོ་ཞེས་གྲག་གོ།[^2070] །སྔོན་གྱི་སློབ་དཔོན་རྣམས་ན་རེ་གང་རེས་འགའ་གཞལ་མེད་ཁང་གི་ཕྱེད་སྣང་བ་དེ་ལྟ་བུ་དེ་ནི་རྒྱུ་བའི་ཚུལ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 3611 [HEADING]]
##### རྒྱལ་ཆེན་བཞིའི་རིས་པའི་ལྷ། ^3-2-1-12-0

[Block 3612]
ཡང་ཉི་མ་ལ་སོགས་པའི་གཞལ་མེད་ཁང་འདི་དག་ན༌[^2071]སེམས་ཅན་གང་དག་ཅིག་གནས༌[^2072]ཤེ་ན། རྒྱལ་ཆེན་བཞིའི་རིས་པའི་ལྷ་རྣམས་སོ། །ཅི་དེ་དག་གི་འདི་དག་ཁོ་ནའམ་ཞེ་ན། གཞལ་མེད་ཁང་ན་གནས་པ་རྣམས་ཀྱི་ནི་འདི་དག་གོ། །

[Block 3613]
ས་ལ་གནས་པ་རྣམས་ཀྱི་ནི་རི་རབ་ཀྱི་བང་རིམ་ལ་སོགས་པའོ། །

[Block 3614]
འདི་ལ་བང་རིམ་ནི་དུ་ཞིག་ཡོད། ཐག་ནི་ཇི་སྲིད་ཅེ་ན། འདི་ལ་བང་རིམ་བཞི་ཡོད་དེ། བར་གྱི་ཐག་ནི་སྟོང་ཕྲག་བཅུ། །དཔག་ཚད་ནི་ཁྲིའི་ལྟག་ན་གཅིག་ཡོད་དེ། བཞིའི་བར་དུ་ཡང་དེ་དང་འདྲའོ། །

[Block 3615]
དེ་དག་གིས་ནི་རི་རབ་ཀྱི་ཕྱེད་མན་ཆད་དུ་ཕྱིན་ཏོ། །

[Block 3616]
དེ་དག་ཀྱང་དེ་ལས་གྲངས་བཞིན་དུ།

[Block 3617 [VERSE]]
སྟོང་ཕྲག་དག་ནི་བཅུ་དྲུག་དང་། །
བརྒྱད་དང་བཞི་དང་གཉིས་འཕགས་སོ། །

[Block 3618]
བང་རིམ་དང་པོ་ནི༌[^2073]རི་རབ་ལས་དཔག་ཚད་སྟོང་ཕྲག་བཅུ་དྲུག་འཕགས་སོ། །

[Block 3619]
གཉིས་པ་ནི་བརྒྱད་དོ། །

[Block 3620]
གསུམ་པ་ནི་བཞིའོ། །

[Block 3621]
བཞི་པ་ནི་གཉིས་སོ། །

[Block 3622 [VERSE]]
དེ་ལ་ལག་ན་གཞོང་ཐོགས་དང་། །
ཕྲེང་ཐོགས་དང་ནི་རྟག་མྱོས་དང་། །
རྒྱལ་ཆེན་བཞི་པའི་ལྷ་རྣམས་གནས། །

[Block 3623]
བང་རིམ་དང་པོ་ལ་ནི་གནོད་སྦྱིན་ལག་ན་གཞོང་ཐོགས་ཞེས་བྱ་བ་རྣམས་གནས་སོ། །

[Block 3624]
གཉིས་པ་ལ་ནི་ཕྲེང་ཐོགས་རྣམས་གནས་སོ། །

[Block 3625]
གསུམ་པ་ལ་ནི་རྟག་ཏུ་མྱོས་རྣམས་གནས་ཏེ། ལྷ་འདི་དག་ཐམས་ཅད་ཀྱང་རྒྱལ་ཆེན་བཞིའི༌[^2074]རིས་པ་དག་ཡིན་ནོ། །

[Block 3626]
བཞི་པ་ལ་ནི་རྒྱལ་པོ་ཆེན་པོ་བཞི་བདག་ཉིད་དང་། དེའི་འཁོར་རྣམས་གནས་ཏེ། དེའི་ཕྱིར་ན་རྒྱལ་ཆེན་བཞི་པའི་ལྷ་རྣམས་ཞེས་བཤད་དོ། །

[Block 3627]
ཇི་ལྟར་བང་རིམ་དག་ལ་རྒྱལ་པོ་ཆེན་པོ་བཞིའི་རིས་ཀྱི་ལྷ་རྣམས༌[^2075]གནས་པ་དེ་བཞིན་དུ། རི་བོ༌[^2076]བདུན་པོ་དག་ལ་ཡང་། །རི་གཉའ་ཤིང་འཛིན་ལ་སོགས་པ་ན་ཡང་དེ་དག་གི་གྲོང་དང་། གྲོང་རྡལ༌[^2077]དག་ཡོད་དེ། དེ་ཉིད་ཀྱི་ཕྱིར་ལྷའི་རིས་དེ་ནི་ཐམས་ཅད་པས་ཆེ་བ་ཡིན་ནོ། །

[Block 3628 [HEADING]]
##### སུམ་ཅུ་རྩ་གསུམ་པ་རྣམས་ཀྱི་སྣོད་གནས་པ། ^3-2-1-13-0

[Block 3629]
ལྷུན་པོའི་རྩེ་ན་སུམ་ཅུ་གསུམ། །ཡང་ལྷུན་པོའི་རྩེ་མོ་ཇི་ཙམ་ཞེ་ན། དེ་ཡི་ངོས་ལ་བརྒྱད་ཁྲིའོ། །

[Block 3630]
ཐུར་དུ་ཇི་ལྟ་བར་ངོས་རེ་རེ་ལ་ཡང༌[^2078]བརྒྱད་ཁྲིའོ། །

[Block 3631]
གཞན་དག་ན་རེ། དེ་ཡི་ངོས་ལ་ཉི་ཁྲིའོ། །ཞེས་ཟེར་ཏེ། འདི་ལ་ངོས་བཞིར་ཕྱོགས་བཞི་ཡོད་དེ། ངོས་རེ་རེ་ཞིང་ཡང་དཔག་ཚད་ཉི་ཁྲི་ཉི་ཁྲི་ཡོད་ལ་ཀུན་དུ་བསྐོར་ན་ནི་བརྒྱད་ཁྲིའི་ཞེའོ། །

[Block 3632]
ཕྱོགས་མཚམས་བརྩེགས་པ་བཞི་ལ་ནི། །ལག་ན་རྡོ་རྗེ་གནས། རི་རབ་རྩེ་མོའི་ཕྱོགས་མཚམས་ནི་གྲུ༌[^2079]བཞི་སྟེ། དེ་དག་ལས་དཔག་ཚད་ལྔ་བརྒྱའི་ཚད་ཙམ་གྱིས་བརྩེགས་པ་བཞི་གྱེན་དུ་འཕགས་ཏེ། དེ་དག་ལ་གནོད་སྦྱིན་ལག་ན་རྡོ་རྗེ་ཞེས་བྱ་བ་གནས་སོ། །

[Block 3633]
རི་རབ་ཀྱི་རྩེ་མོ་དེའི་དབུས་ན།

[Block 3634 [VERSE]]
གྲོང་ཁྱེར་བལྟ༌[^2080]ན་སྡུག་ཅེས་པ། །
ངོས་ལ་ཉིས་སྟོང་ལྔ་བརྒྱ་པ། །
དཔག་ཚད་ཕྱེད་དང་གཉིས་གསེར་གྱི།
རང་བཞིན་གཞི་བཀྲ་མཉེན་པ་ཡོད། །

[Block 3635]
རི་རབ་ཀྱི་གཞིའི་དབུས་ན་ལྷ་རྣམས་ཀྱི་དབང་པོ་བརྒྱ་བྱིན་གྱི་རྒྱལ་པོའི་ཕོ་བྲང་གྲོང་ཁྱེར་བལྟ༌[^2081]ན་སྡུག་ཅེས་བྱ་བ་ངོས་རེ་རེ་ཞིང་ཡང་དཔག་ཚད་ཉིས་སྟོང་ལྔ་བརྒྱ་པ། འཕང་དུ་དཔག་ཚད་ཕྱེད་དང་གཉིས་པ། གསེར་གྱི་རང་བཞིན་འདིའི་ས་གཞི་ཚོན་བརྒྱས༌[^2082]བཀྲ་བར་བྱས་ལ། ས་གཞི་དེ་ཡང་ཤིང་བལ་གྱི་འདབ་མ་བཞིན་དུ་རེག་ན་འཇམ་པ་རྐང་པ་གཞག་པ་དང་། བཏེག་པ་དག་གིས་ན་ནེམས་ཞེས་བྱེད་པ་དང་པར་ཞེས་བྱེད་པ་ཡོད་དོ། །

[Block 3636]
དེ་ན་རྣམ་པར་རྒྱལ་བྱེད་དོ། །

[Block 3637]
[^2083]ངོས་ལ་ཉིས་བརྒྱ་ལྔ་བཅུའོ། །

[Block 3638]
གྲོང་ཁྱེར་གྱི་དབུས་ན་ལྷ་རྣམས་ཀྱི་དབང་པོ་བརྒྱ་བྱིན་གྱི་ཁང་བཟངས་རྣམ་པར་རྒྱལ་བྱེད་ཅེས་བྱ་བ་རིན་པོ་ཆེ་དང་གནས་རྣམ་པ་དུ་མ་ཕུན་སུམ་ཚོགས་པ་གནས་གཞན་ཐམས་ཅད་ཀྱི་དཔལ་གྱི་ཆེ་བའི་བདག་ཉིད་ངོ་ཚ༌[^2084]བར་བྱེད་པ་ངོས་ངོས་ཀྱི་སྲིད་དུ་དཔག་ཚད་ཉིས་བརྒྱ་ལྔ་བཅུ་པ་ཞིག་ཡོད་དོ།[^2085] །རེ་ཞིག་འདི་ནི་གྲོང་གི་མངོན་པར་དགའ་བ་ཡིན་ནོ། །

[Block 3639 [VERSE]]
དེའི་ཕྱི་རོལ་ཤིང་རྟ་སྣ་ཚོགས་དང་། །
རྩུབ་འགྱུར་འདྲེས་པ་དགའ་བས་བརྒྱན། །

[Block 3640]
གྲོང་ཁྱེར་དེའི་ཕྱི་རོལ་གྱི་ངོས་བཞི་དག་ན་ལྷ་རྣམས་ཀྱི་རྩེད་མོའི་ས་སྐྱེད་མོས་ཚལ་བཞི་ཡོད་དེ། འདི་ལྟ་སྟེ་སྐྱེད་མོས་ཚལ་ཤིང་རྟ་སྣ་ཚོགས་ཅན་དང་། རྩུབ་འགྱུར་དང་། འདྲེས་པ་དང་། དགའ་བའི་ཚལ་ཏེ། དེ་དག་གིས་གྲོང་ཁྱེར་དེའི་ཕྱི་རོལ་བརྒྱན་ཏོ། །

[Block 3641 [VERSE]]
དེ་དག་གི་ནི་ཕྱོགས་བཞི་ན། །
ཉི་ཤུས་བཅད་ན་ས་གཞི་བཟང་། །

[Block 3642]
སྐྱེད་མོས་ཚལ་དེ་དག་གི་ཕྱོགས་བཞི་དཔག་ཚད་ཉི་ཤུས་བཅད་པ་ན་ལྷ་རྣམས་ཀྱི་རྩེ་བའི་གནས་ས་གཞི་བཟང་པོ་ཕན་ཚུན་འགྲན་པ་ལྟ་བུར་མཛེས་པ་དང་ལྡན་པ་བཞི་ཡོད་དོ། །

[Block 3643]
གྲོང་ཁྱེར་གྱི་ཕྱི་རོལ་གྱི་ངོས།

[Block 3644 [VERSE]]
བྱང་ཤར་མཚམས་ན་ཡོངས་འདུ་སྟེ། །
ལྷོ་ནུབ་མཚམས་ན་ཆོས་བཟང་ངོ་། །

[Block 3645]
ཤིང་ས་བརྟོལ་ཡོངས་འདུ་ཞེས་བྱ་བ་སུམ་ཅུ་རྩ་གསུམ་པའི་ལྷ་རྣམས་ཀྱི་འདོད་པའི་དགའ་བ་མཆོག་གི་གནས་ཞིག་ཡོད་དེ། དེའི་རྩ་བ་ནི་དཔག་ཚད་ལྔ་བཅུ་ཟུག་གོ །གནམ་འཕང་དུ་ནི་དཔག་ཚད་བརྒྱ་འཕགས་སོ། །
--- END BLOCKS ---
