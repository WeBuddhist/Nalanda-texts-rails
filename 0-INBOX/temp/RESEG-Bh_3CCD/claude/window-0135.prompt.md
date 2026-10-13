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
[Block 4726]
འདིས་ནི་བདག་ཉིད་ཟླ་བའི་དཀྱིལ་འཁོར་དང་འདྲ་བར་བྱིན་གྱིས་བརླབས་ལ་ཞེས་པ་ནི་ཡི་གེ་གསུམ་ཡོངས་སུ་གྱུར་པ་ལས་སྐྱེས་པའི་པདྨ་ལ་སོགས་པ་གསུམ་གྱི་སྟེང་དུ་ཡི་གེ་གསུམ་ཡོངས་སུ་གྱུར་པ་ལས་སྐྱེས་པའི་ཟླ་བ་ལ་སྔར་བསྒོམས་པའི༌[^2830]པདྨ་ལ་སོགས་པ་གསུམ་དང་རོ་གཅིག་པར་གྱུར་པའི་ཟླ་བའི་དཀྱིལ་འཁོར་དང་འདྲ་བའི་སེམས་ཉིད་བྱིན་གྱིས་བརླབས་ནས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4727 [VERSE]]
ཡིད་མི་བདེ་བ་ལས་གྲོལ་བའི། །
རྣམ་རྟོག་མུན་པ་སེལ་བྱེད་ཅིང་། །
ཉོན་མོངས་དྲི་མ་ཀུན་ལས་དག །
ཟླ་བ་བཞིན་དུ་སེམས་ཟླ་བའོ། །

[Block 4728]
ཞེས་འབྱུང་ངོ་། །རྩ་བའི་རྒྱུད་ལས་ཀྱང་། བཅོམ་ལྡན་འདས་ཟླ་བའི་དཀྱིལ་འཁོར་དང་འདྲ་བའི་སེམས་མཐོང་ངོ་ཞེས་འབྱུང་ངོ་། །དེའི་སྟེང་དུ༌[^2831]ཡི་གེ་གསུམ་ལ་སོགས་པའི༌[^2832]ལྷའི་སྐུར་བསྐྱེད་དེ་ཞེས་པ་ལ་ཟླ་བའི་དཀྱིལ་འཁོར་གྱི་སྟེང་དུ་ཡང་ཡི་གེ་གསུམ་བཀོད་པ་དེ་ཡོངས་སུ་གྱུར་པ་ལས་རྡོ་རྗེ་རྩེ་ལྔ་པ་འམ་འཁོར་ལོ་ལ་སོགས་པ་བསྒོམས་ལ། །དེ་ལ་ཡང་ཡིག་འབྲུ་དགོད་ཅིང་སྤྲོ་བ་དང་བསྡུ་བའི་རིམ་པའི་གྲོ༌[^2833]བའི་དོན་བྱས་ལ་བཛྲ་ཨཱཏྨ་ཀོ྅ཧཾ་ཞེས་བྱ་བས་ང་རྒྱལ་བྱས་ལ། དེ་ཡོངས་སུ་གྱུར་པ་ལས་རྡོ་རྗེ་འཆང་ཆེན་པོའི་སྐུ་དང་གཅིག་ཏུ་གྱུར་པའི་རྣམ་པར་སྣང་མཛད་ལ་སོགས་པའི་དེ་བཞིན་གཤེགས་པའི་ཕྱག་རྒྱའི་སྐུ་བསྒོམས་ལ། ཡེ་ཤེས་སེམས་དཔའ་དང་ཏིང་ངེ་འཛིན་སེམས་དཔའ་དགོད་ཅིང་ཕུང་པོ་དང༌[^2834]ཁམས་དང་སྐྱེ་མཆེད་རྣམ་པར་དག་པར་བྱ་སྟེ། སྐུ་ལ་སོགས་པ་བྱིན་གྱིས་བརླབ་པའི༌[^2835]མཚན་ཉིད་ཀྱི༌[^2836]རྣལ་འབྱོར་ཆེན་པོ་ཡོངས་སུ་རྫོགས་ཤིང་དབུས་ཀྱི་གཙོ་བོར་གྱུར་ནས།

[Block 4729]
དང་པོ་སྦྱོར་བའི་འོག་ཏུ་ཕྱག་རྒྱ་ལེགས་པར་སྦྱང་ཞིང་དཀྱིལ་འཁོར་པ་རྣམས་སྤྲུལ་ལ་དཀྱིལ་འཁོར་ལ་དགོད་དེ། དབང་བསྐུར་བ་དང་རྒྱས་གདབ་པའི་བར་དུ་དཀྱིལ་འཁོར་རྒྱལ་བ་མཆོག་ཡོངས་སུ་རྫོགས་ཏེ་ལས་ཀྱི་རྒྱལ་བ་མཆོག་གི་ཕྱོགས་གཅིག་པ་འཆད་པར་འགྱུར་བའི་རིམ་པས། ཕྲ་མོའི་རྣལ་འབྱོར་ཞེས་པ་ནི་འོག་ནས་འཆད་པར་འགྱུར་བའི་རིམ་པས་བསྒོམ་པར་བྱའོ། །

[Block 4730]
དྲང་བའི་དོན་ཏོ་ཞེས་པ་ནི་ཏིང་ངེ་འཛིན་གཉིས་འཆད་པར་འདོད་པའི་ཕྱིར་རོ། །

[Block 4731]
དེ་ཉིད་གསལ་བར་བྱ་བའི་ཕྱིར། །བསྐྱེད་པའི་རིམ་པའི་ཏིང་ངེ་འཛིན་ཏོ་ཞེས་སྨྲས་པ༌[^2837]ལ། འཆད་པར་འགྱུར་བའི་ཕྲ་མོའི་རྣལ་འབྱོར་དང་ལྷན་ཅིག་ཏུ་ཏིང་ངེ་འཛིན་གསུམ༌[^2838]གྱི་བདག་ཉིད་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 4732]
ད་ནི་ལེའུ་བརྩམ་པ༌[^2839]ནས་བརྩམས་ཏེ་ཚིག་དེ་རྣམས་ཉིད་རྡོ་རྗེ་བཟླས་པ་ལ་སོགས་པ༌[^2840]རྫོགས་པའི་རིམ་པའི་སྒོ་ནས་བསྟན་པར་བྱ་བའི་ཕྱིར་འོད་ཟེར་ལྔ་པོ་ཞེས་སྨོས་པ་ལ། མེ་ལ་སོགས་པའི་དཀྱིལ་འཁོར་བཞི་པོ་ལས་འབྱུང་བའོ། །

[Block 4733]
སྟེང་གི་སྒོ་ནས་འབྱུང་བ་ཞེས་བྱ་བ་ནི་གདོང་གི་སྣ་ཁུང་གཉིས་ཀྱི་ལམ་ནས་སོ། །

[Block 4734]
ཚོགས་སོ་ཞེས་པ་ནི་ཉིན་མོ་དང་མཚན་མོར་ཉི་ཁྲི་ཆིག་སྟོང་དྲུག་བརྒྱ་སྲོག་དང་རྩོལ་བ་འབྱུང་བའོ། །

[Block 4735]
དཀྱིལ་འཁོར་རེ་རེ་ལ་དཀྱིལ་འཁོར་བཞི་རབ་ཏུ་འབྱུང་ཞིང་ཞེས་པ་ལ་ལྐོག་མའི་གནས་སུ་མེའི་དཀྱིལ་འཁོར་ཡིན་ན་ཡང་ས་དང་ཆུ་དང་རླུང་གི་ཁམས་ཀྱི་རང་བཞིན་གྱི་ཆ་གསུམ་གྱིས༌[^2841]ཁྱབ་པའོ། །

[Block 4736]
དེ་བཞིན་དུ་སྙིང་ག༌[^2842]ཆུའི་དཀྱིལ་འཁོར་ཡང་ས་དང་མེ་དང་རླུང་གི་དཀྱིལ་འཁོར་གྱི་ཆས་ཁྱབ་པའོ། །

[Block 4737]
དེ་བཞིན་དུ་ལྟེ་བར་རླུང་གི་དཀྱིལ་འཁོར་ཡང་ས་དང་ཆུ་དང་མེའི་ཁམས་ཀྱི་ཆས་ཁྱབ་པའོ། །

[Block 4738]
དེ་བཞིན་དུ་གསང་བའི་གནས་སུ་སའི་དཀྱིལ་འཁོར་ཡང་ཆུ་དང་མེ་དང་རླུང་གི་ཁམས་ཀྱི་ཆས་ཁྱབ་པའོ། །

[Block 4739]
དེ་བཞིན་དུ་དཀྱིལ་འཁོར་གྱི་ཆ་རེ་རེ་ལ་ཉིས་བརྒྱ་དང་ཉི་ཤུ་རྩ་ལྔའི་གྲངས་ཀྱིས་ཆ་བཞི་པོ་ལ་དགུ་བརྒྱར་འགྱུར་རོ། །

[Block 4740]
འཇུག་པ་དང་ལྡང་བ་དང་གནས་པའི་རིམ་པས་དཀྱིལ་འཁོར་གཅིག་ལ་ཉིས་སྟོང་བདུན་བརྒྱར་འགྱུར་རོ། །

[Block 4741]
ཆུ་དང་རླུང་དང༌[^2843]སའི་དཀྱིལ་འཁོར་རྣམས་སུ་ཡང་ཉིས་སྟོང་བདུན་བརྒྱ་དང་ཉིས་སྟོང་བདུན་བརྒྱའི་གྲངས་ཀྱིས༌[^2844]སྟོང་ཕྲག་བཅུ་དང་བརྒྱད་བརྒྱར་འགྱུར་རོ། །

[Block 4742]
དེ་བཞིན་དུ་མཚན་མོར་ཡང་སྟོང་ཕྲག་བཅུ་དང་བརྒྱད་བརྒྱར་འགྱུར་རོ། །

[Block 4743]
གཅིག་ཏུ་བསྡུས༌[^2845]ཏེ་ཉི་ཁྲི་ཆིག་སྟོང་དྲུག་བརྒྱར་འགྱུར་རོ། །

[Block 4744]
དེ་ཉིད་ཀྱི་ཕྱིར་དཀྱིལ་འཁོར་བཞི་པོ་ལ་འཇུག་པ་ལ་སོགས་པའི་རིམ་གྱིས༌[^2846]ཉིན་མོར་རྒྱུ་བ་བཅུ་གཉིས་དང་མཚན་མོར་རྒྱུ་བ་བཅུ་གཉིས་ཏེ་གཅིག་ཏུ་བསྡུས་ནས་ཉི་ཤུ་རྩ་བཞིར་འགྱུར་རོ། །

[Block 4745]
དེ་ཉིད་ཀྱི་ཕྱིར་དཀྱིལ་འཁོར་བཞི་པོ་ལ་འཇུག་པ་ལ་སོགས་པའི་རིམ་གྱིས༌[^2847]དགོངས་པ་ལུང་བསྟན་པའི་བཤད་པའི་རྒྱུད་ལས་ཀྱང་།

[Block 4746 [VERSE]]
གོས་དཀར་མོ་ལ་སོགས་པར་བཤད། །
བརྒྱ་ཕྲག་གཉིས་དང་ཉི་ཤུ་ལྔ། །
བཞི་པོ་ལེགས་པར་བསྒྲེས་པས་ནི། །
སྦྱོར་བཞི་བསྡུས་པས་བརྒྱ་ཕྲག་དགུ། །

[Block 4747 [VERSE]]
དགུ་བརྒྱ་དག་ཏུ་གང་བསྟན་པ། །
ཉི་ཤུ་རྩ་བཞིའི་རིམ་པ་ཡིས། །
ལེགས་པར་བསྡུས་ཏེ་དེ་དག་ནི། །
ཉི་ཁྲི་ཆིག་སྟོང་དྲུག་བརྒྱར་འགྱུར། །

[Block 4748]
ཞེས་འབྱུང་ངོ་། །དཀར་པོ་ལ་སོགས་པ་ཁ་དོག་རྣམས་ཀྱིས་ཕྱེ་བས་ན་བཀོད་པ་སྟེ་ཞེས་པ་ནི། འདིར་དཀྱིལ་འཁོར་རེ་རེ་གལ་ཏེ་རིགས་དང་རྗེས་སུ་མཐུན་པས་ཁ་དོག་དམར་པོ་ལ་སོགས་པ་དང་ལྡན་པ་ཡིན་ན་ཡང་དེ་བཞིན་དུ་ཁ་དོག་ལྔའི་འོད་ཟེར་གྱི་ཚོགས་དང་ལྡན་པ་དེ་དག་ཤེས་པར་བྱའོ། །

[Block 4749 [VERSE]]
གཡས་པ་ལས་བྱུང་འོད་ཟེར་ནི། །
དེ་ཉིད་མེ་ཡི༌[^2848]དཀྱིལ་འཁོར་ཏེ། །
ཁ་དོག་དམར་པོ་དེ་གསལ་བས། །
དེར་ནི་པདྨའི་མགོན་པོ༌[^2849]ལྷ། །

[Block 4750 [VERSE]]
གཡོན་པ་ལས་བྱུང་འོད་ཟེར་ནི། །
རླུང་གི་དཀྱིལ་འཁོར་ཞེས་བྱ་བའི། །
ལྗང་སེར་ཁ་དོག་དང་མཚུངས་པའི། །
དེར་ནི་ལས་ཀྱི་མགོན་པོ་ལྷ། །

[Block 4751 [VERSE]]
གཉི་ག་ལས་བྱུང་འོད་ཟེར་ནི། །
ཁ་དོག་སེར་པོ་འོད་ཆེན་པོ། །
དབང་ཆེན་དཀྱིལ་འཁོར་དེ་ཉིད་དེ། །
དེར་ནི་རིན་ཆེན་མགོན་པོ་ལྷ། །

[Block 4752 [VERSE]]
དལ་བུས་དམན་པར་རྒྱུ་བ་ནི། །
དཀར་བ་ཀུན་ད་ཟླ་བ་མཚུངས། །
དེ་ཉིད་ཆུ་ཡི་དཀྱིལ་འཁོར་ཏེ། །
དེར་ནི་རྡོ་རྗེ་མགོན་པོ་ལྷ། །

[Block 4753 [VERSE]]
རླུང་ནི་ལུས་ཀུན་རྗེས་འགྲོ་བའི། །
བྱ་བ་ཀུན་ལ་རབ་འཇུག་པ། །
རྣམ་པར་སྣང་མཛད་རང་བཞིན་ཏེ། །
འཆི་བའི་ལུས་ལས་འབྱུང་བར་འགྱུར། །

[Block 4754]
ཞེས་འབྱུང་ངོ་། །ཏིང་ངེ་འཛིན་ལ་ཡང་དག་པར་དམིགས་པའོ་ཞེས་པ་ནི་རྡོ་རྗེ་བཟླས་པའི་མཚན་ཉིད་ཅན་གྱི་ཏིང་ངེ་འཛིན་ལ་དམིགས་ནས་སོ། །

[Block 4755]
རྡོ་རྗེ་ཡི༌[^2850]གེ་གསུམ་མོ་ཞེས་པ་ནི་སྐུ་རྡོ་རྗེ་ལ་སོགས་པའི་ས་བོན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4756]
དེའི་བཀོད་པ་ནི་ཚོགས་ཏེ་ཞེས་པ་ནི་བཅོམ་ལྡན་འདས་རྡོ་རྗེ་འཆང་གིས་སེམས་ཅན་རྣམས་ཀྱི༌[^2851]བསམ་པ་དང་བག་ཆགས་དང་བག་ལ་ཉལ་དང་རིགས་ཀྱི་དབྱེ་བས་སྔགས་ཀྱི་དབྱེ་བ་བདུན་ཁྲི་ཉིས་སྟོང་གསུངས་སོ། །

[Block 4757]
དེ་དག་ཐམས་ཅད་སྐུ་གསུང་ཐུགས་ཀྱི་རང་བཞིན་གྱི་ཡི་གེ་གསུམ་ལ་བསྡུ་བར་འགྱུར་ཏེ། །དེ་ལ་འབྱུང་བའི་རིམ་པ་ནི་ལྟེ་བའི་ཕྱོགས་ནས་སྲོག་ཅེས་བྱ་བའི་རླུང་གི་གནས་བརྒྱད་ལ་རེག་པས་ཡི་གེ་རྣམས་འབྱུང་ངོ་། །དེ་རྣམས་ཀྱིས༌[^2852]ཚིག་དང་དེས་ཀྱང་ངག་ཆེན་པོ་སྐྱེ་བར་འགྱུར་རོ། །

[Block 4758]
དེ་རྣམས་ཀྱིས་ཀྱང་བྱ་བ་དང་བྱེད་པ་པོ་དང་རྟགས་དང་བསྡུ་བ་དང་བདག་གི་ཚིག་དང་གཞན་གྱི་ཚིག་དང༌[^2853]བྱེད་པ་དང་དེ་ལ་ཕན་པ་དང་ཀུན་དུ་བཤད་པ་དང་ཚིག་ཕྲད་དང་ཉེ་བར་བསྒྱུར་བ་དང་ལས་རབ་ཏུ་བརྗོད་པ་ལ་སོགས་པའི་དབྱེ་བས་རོལ་མོ་དང་ཚིག་ལྷུག་པ་ལ་སོགས་པ་དང་། །བྱ་བ་དང་སྤྱོད་པ་ལ་སོགས་པའི་དབྱེ་བས་ཆོས་ཀྱི་ཕུང་པོ་བརྒྱད་ཁྲི་བཞི་སྟོང་འབྱུང་བར་འགྱུར་རོ། །

[Block 4759]
དེ་ལྟར་ངག་གི་སྤྲོས་པ་ཐམས་ཅད་ཀྱི་ཡི་གེ་ཕྱི་མོ་གཅིག་པུ་ཉིད་རྩ་བ་ཡིན་ཏེ། དེ་ལ་སྡེ་ཚན་བརྒྱད་ནི༌[^2854]རྣམ་པར་ཤེས་པ་བརྒྱད་ཀྱི་རང་བཞིན་ནོ། །

[Block 4760]
དབྱངས་ཀྱི་སྡེ་ཚན་གཅིག་དང་ཀ་ལ་སོགས་པ་དུ་མའི་བར་དུ་རེག་པའི༌[^2855]སྡེ་ཚན༌[^2856]ལྔ་དང་། མཐར་གནས་པ་དང་དྲོད་ཀྱི་སྡེ་ཚན༌[^2857]གཉིས་སོ། །

[Block 4761]
དེ་རྣམས་ཀྱང་ཨ་ལ་སོགས་པ་དང་པོའི་ཡི་གེ་རྣམས་ལ་བསྡུ་བར་འགྱུར་རོ། །

[Block 4762]
དེ་རྣམས་ཀྱང་ཨ་ཀ་ཡ་ཤའི་ཡི་གེ་བཞི་པོ་ལ་ཐིམ་པར་འགྱུར་ཏེ། ཁམས་བཞིའི་རང་བཞིན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4763]
ཡི་གེ་བཞི་པོ་ཡང་ཨ་ཀ་ཡ་ཡི་གེ་གསུམ་ལ་ཐིམ་པར་གྱུར་ཏོ། །

[Block 4764]
དེ་རྣམས་ལས་ཤེས་རབ་ཀྱི་རང་བཞིན་ཡི་གེ་ཨ་ཡོངས་སུ་གྱུར་པ་འོད་དཔག་ཏུ་མེད་པའི་རང་བཞིན་གྱི་ཡི་གེ་ཨ་འགྱུར་ཏེ། དབྱངས་ཀྱི་སྡེ་ཚན་ནི་མོ་རྟགས་ཡིན་པས་སོ། །

[Block 4765]
ཐབས་ཀྱི་རང་བཞིན་ཡི་གེ་ཀ་ཡོངས་སུ་གྱུར་པ་ལས་ཧཱུྃ་བྱུང་བར་གྱུར་ཏེ། དེ་ནི་ཕོ་རྟགས་ཡིན་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
