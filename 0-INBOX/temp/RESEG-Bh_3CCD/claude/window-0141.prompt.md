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
[Block 4936 [VERSE]]
གཟུགས་དང་སྒྲ་དང་དེ་བཞིན་དྲི། །
རོ་དང་རེག་བྱ་ཉིད་དག་ལ། །
མིག་ལ་སོགས་པའི་འཇུག་པ་ནི། །
སྒྱུ་མ་བཞིན་དུ་མཚོན་པར་བྱ། །

[Block 4937 [VERSE]]
འདིར་ནི་མང་པོ་སྨོས་ཅི་དགོས། །
རྡོ་རྗེ་ཐེག་པར་དེ་ཉིད་ལ། །
གང་ཡང་རྣལ་འབྱོར་པས་དམིགས་པའི།
དེ་དེ་སྒྱུ་མ་བཞིན་གཞན་མིན། །

[Block 4938]
ཞེས་འབྱུང་ངོ་། །ཡུལ་རྣམས་ལ་ཉེ་བར་ལོངས་སྤྱོད་པ་ཞེས་པ་ནི་སོ་སོར་སྡུད་པའི་རིམ་པས་གཟུང༌[^2926]སྟེ། བསམ་གཏན་གྱི་རིམ་པས་རྣམ་པར་དག་པ་ཐོབ་པ་གང་ཡིན་པའོ། །

[Block 4939]
དབང་པོ་ལྔ་རྣམས་སོ་ཞེས་པ་ནི་མིག་ལ་སོགས་པའོ། །

[Block 4940]
དེ་རྣམས་ཀྱིས་བརྒྱན་པ་ཞེས་པ་ལ་སྒྱུ་མ་ལྟ་བུའི་དབང་པོ་དང་ལྡན་པ་ཡིན་གྱི། ཁྲག་དང་ཤ༌[^2927]ལ་སོགས་པའི་རང་བཞིན་ནི་མ་ཡིན་ནོ། །

[Block 4941 [VERSE]]
རབ་ཏུ་བྱེད་པ་ལས་ཀྱང་། །
ཁྱོད་ཀྱི་སྐུ་ལ་ཁོང་སྟོང་མེད། །
ཤ་དང་རུས་པ་ཁྲག་ཀྱང་མེད། །
ནམ་མཁའི་འཇའ་ཚོན་དང་མཚུངས་པའི། །

[Block 4942 [VERSE]]
ཁྱོད་ཀྱི་སྐུ་ནི་སྟོན་པར་བྱེད། །
སྐུ་ལ་སྙུན༌[^2928]དང་མི་གཙང་མེད། །
བཀྲེས་དང་སྐོམ་པ་མི་སྲིད་དེ། །
ཁྱོད་ཀྱིས༌[^2929]འཇིག་རྟེན་འཇུག་པའི་ཕྱིར། །

[Block 4943]
འཇིག་རྟེན་བྱ་བ་བསྟན་པར་མཛད། །ཅེས་འབྱུང་ངོ་། །དབང་པོ་ཚང་བའི་ཕྱིར་རོ༌[^2930]ཞེས་པ་ནི་ཇི་ལྟར་དྲི་ཟའི༌[^2931]སེམས་ཅན་གཟུགས་དང་དབང་པོ་ཕྲ་བ་དང་ལྡན་པ་དེ་བཞིན་དུ་སྒྱུ་མའི་སྐུ་ཡང་གཟུགས་དང་དབང་པོ་ཕྲ་བ་དང་ལྡན་པ་ཞེས་བྱའོ། །

[Block 4944 [VERSE]]
དབང་པོ་ཚང་བའི་དྲི་ཟ་ནི། །
དེ་ཉིད་དྲི་ཟའི་སེམས་ཅན་ཏེ། །
རྡོ་རྗེའི༌[^2932]སྐུ་ཡང་དེ་ཉིད་དོ། །

[Block 4945]
ཞེས་འབྱུང་ངོ་། །དེ་ལྟ་བུའི་རྣམ་པ་ཞེས་པ་ནི་སྒྱུ་མ་ལྟ་བུའི་སྐུའོ། །

[Block 4946]
སངས་རྒྱས་ཀྱི་དཀྱིལ་འཁོར་གསལ་བར་འཇུག་ཅིང་ཞེས་པ་ལ། སངས་རྒྱས་ནི་དེ་བཞིན་གཤེགས་པ་རྣམས་ལ་དཀྱིལ་ནི་སྙིང་པོའོ། །

[Block 4947]
དེ་ལེན་ཞིང་འཛིན་པར་བྱེད་པས་ན་སངས་རྒྱས་ཀྱི་དཀྱིལ་འཁོར་རོ། །

[Block 4948]
ཆོས་ཀྱི་དབྱིངས་དང་དེ་བཞིན་ཉིད་དང་། ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་ཡང་དག་པའི་མཐའ་དང་ཆོས་ཉིད་ཀྱི་རང་བཞིན་འོད༌[^2933]གསལ་བ་ཞེས་པའི་ཐ་ཚིག་གོ། །

[Block 4949]
དེ་ལ་འཇུག་ཅིང་ཞེས་པ་ནི་ཕྱག་རྒྱའི་རིམ་པའམ་ཏིང་ངེ་འཛིན་གྱི་རིམ་པས་ཡང་དག་པའི་མཐར་འཇུག་པར་བྱའོ་ཞེས་པའི་དོན་ཏོ། །

[Block 4950]
དེ་ལྟར་བདག་ཉིད་ཅེས་བྱ་བ་ལ་སོགས་པས་བདག་ལ་བྱིན་གྱིས་བརླབ་པས༌[^2934]མཚན་ཉིད་ཀྱི་སྐུ་རིམ་པ་བཞི་པས་འོད་གསལ་བ་ལ་འཇུག་པར་བྱའོ། །

[Block 4951]
སྐད་ཅིག་མའི་རྣམ་པར༌[^2935]ཤེས་པ་ནི་ཅིག་ཅར་དུ་སྤྲོ་བའོ། །

[Block 4952]
རྡོ་རྗེ་འཆང་ཆེན་པོའི་སྐུ་ཞེས་པ་ལ་རྡོ་རྗེ་སྐུའི་རྣམ་གྲངས་ཅན་དཔལ་རྡོ་རྗེ་སེམས་དཔའི་ཕྱག་རྒྱ་ཆེན་པོའི་གཟུགས་སོ། །

[Block 4953]
འཁོར་བ་དང་མྱ་ངན་ལས་འདས་པ་དག་གི་དབུས་སུ་ཞེས་པ་ནི། སྲིད་པ་དང་ཞི་བའི་རོ་མཉམ་པའི་རང་བཞིན་ཅན་ནོ། །

[Block 4954]
ཡོད་པ་དང་མེད་པའི་ཕྱོགས་དང་བྲལ་བ་ཞེས་པ་ལ། དེ་ནི་ཉེ་བར་མཚོན་པ་ཙམ་ཡིན་ཏེ། ཡོད་པ་དང་མེད་པ་དང་དངོས་པོ་དང་དངོས་པོ་མ་ཡིན་པ་དང་རྟག་པ་དང་ཆད་པ་དང་ཀུན་རྫོབ་དང་དོན་དམ་པ་དང་བརྟགས་པ་དང་ཡོངས་སུ་རྫོགས་པ་དང་སྔགས་ཀྱི་སྐུ་དང་ཡེ་ཤེས་ཀྱི་སྐུ་དང་། [^2936]ཐབས་དང་ཤེས་རབ་དང་སྟོང་པ་ཉིད༌[^2937]དང་སྙིང་རྗེ་ལ་སོགས་པའི་རྣམ་པར་རྟོག་པ་དང་བྲལ་བའོ། །

[Block 4955]
བདག་ཉིད་ཅེས་པ་ནི་རང་གི་སྐུའོ། །ཤེས་པར་བྱ་བ༌[^2938]ལ་རྗེས་སུ་དྲན་པར་བྱའོ། །

[Block 4956]
དེས་ནི་ཟུང་འཇུག་གི་རིམ་པ་བསྟན་པའོ། །

[Block 4957]
རིམ་པ་འདི་ཉིད་ཀྱིས་ཞེས་བྱ་བ་ལ་སོགས་པས་རྡོ་རྗེ་བཟླས་པ་ལ་སོགས་པའི་རིམ་པའི་མཚན་ཉིད་ཅན་གྱི་རྫོགས་པའི་རིམ་པས་སོ། །

[Block 4958]
རྣམ་པར་སྣང་མཛད་ལ་སོགས་པར་ཞེས་པ་ནི་དེ་བཞིན་གཤེགས་པ་དྲུག་གི་ཕྱག་རྒྱ་ཆེན་པོའི་སྐུའོ། །

[Block 4959]
བསམ་པ་ཇི་ལྟ་བའི་དབྱེ་བས་ཞེས་པ་ནི་གཏི་མུག་ལ་སོགས་པའི་ཉོན་མོངས་པའི་བག་ཆགས་ཀྱི་དབྱེ་བའི་སྒོ་ནས་སོ། །

[Block 4960]
རང་གི་བདག་ཉིད་བསྐྱེད་པ་ལ། །ཞེས་པ་ནི་སྤྲོས་ནས་སོ། །

[Block 4961]
བདག་གི་དོན་བྱའོ༌[^2939]ཞེས་པ་ལ་ཉེ་བར་མཚོན་པ་ཙམ་ཡིན་ཏེ་གཞན་གྱི་དོན་ཀྱང་བྱའོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 4962]
དེ་བས་ན་ཞེས་བྱ་བ་ལ་སོགས་པས་རྣམ་པར་སྣང་མཛད་ལ་སོགས་པའི་ཕྱག་རྒྱ་ཆེན་པོའི་སྐུ་རྫོགས་པའི་རིམ་པས་བསྒོམ་པར་བྱའོ་ཞེས་བསྟན་ཏོ། །

[Block 4963]
རྡོ་རྗེ་འཆང་ཆེན་པོའི་རྣལ་འབྱོར་ཞེས་བྱ་བ་ནི་རྫོགས་པའི་རིམ་པ་ལས་འབྱུང་བའི་རྡོ་རྗེ་འཆང་ཆེན་པོའི་ལྷའི་སྐུའོ། །

[Block 4964]
འདི་ཉིད་ནི་རིམ་པ་ལྔའི་སྒོ་ནས་རྫོགས་པའོ། །

[Block 4965]
བརྟེན་པར་བྱ་བའི་ཕྱིར་ཞེས་པ་ནི་ཆོས་ཀྱི་དབྱིངས་ཀྱི་ངོ་བོ་ཉིད་ནི་དེ་བཞིན་གཤེགས་པ་དྲུག་གི་རང་བཞིན་དུ་བྱ་བའི་ཕྱིར་རོ། །

[Block 4966]
གསུངས་ཏེ་ནི་སྡུད་པ་པོའི་ཚིག་ཅེས་ལྷག་མའོ། །

[Block 4967]
འོད་གསལ་བའོ་ཞེས་པ་ནི་དངོས་པོ་ཐམས་ཅད་དེའི་རང་བཞིན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4968]
ཏིང་ངེ་འཛིན་ཏོ༌[^2940]ཞེས་པ་ནི་སྤྲོས་པ་ཐམས་ཅད་དང་བྲལ་བའི་སེམས་རྣམ་པར་དག་པའི་རིམ་པས་ཐོབ་པར་བྱ་བའམ་མངོན་པར་བྱང་ཆུབ་པའི་རིམ་པས་ཐོབ་པར་བྱའོ། །

[Block 4969]
དེ་ལ་དམིགས་པའོ་ཞེས་པ་ནི་བསྒོམ་པར་བྱས་ནས་སོ། །

[Block 4970]
བསྐྱེད་པ་དེ་ནི་ཞེས་པ་ལ་རྫོགས་པའི་རིམ་པས་ཡེ་ཤེས་ཀྱི་སྐུའི་རང་བཞིན་ནམ་རྡོ་རྗེའི་སྐུའི་རང་བཞིན་དུ་བསྒྲུབ་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4971]
འདིའི་དོན་ནི་བཤད་པའི་རྒྱུད་ལས་ཞེས་པ་ནི་རྡོ་རྗེ་ཕྲེང་བའི་རྒྱུད་ལས་སོ། །

[Block 4972 [VERSE]]
ཨོཾ་ནི་དང་པོར་ཤེས་པར་བྱ། །
ཞེས་པ་རྣམ་པར་སྣང་མཛད་དེ།
དེ་ནི་ཨོཾ་ལས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 4973]
དྷརྨ་ཞེས་བྱ་གཉིས་པའོ། །

[Block 4974]
ཞེས་པ་ནི་ཆོས་ཀྱི་ཕུང་པོ་བརྒྱད་ཁྲི་བཞི་སྟོང་གི་རྣམ་པར་དག་པའི་རང་བཞིན་གྱི་རྡོ་རྗེ་ཆོས་ཏེ་སྣང་བ་མཐའ་ཡས་སོ། །

[Block 4975]
དྷཱ་ཏུ་ཞེས་བྱ་གསུམ་པར་བཤད། །ཅེས་པ་ནི་ཆོས་ཐམས་ཅད་ཀྱི་རང་བཞིན་ཆོས་ཀྱི་དབྱིངས་རྣམ་པར་དག་པའི་ངོ་བོ་ནི་མི་བསྐྱོད་པའོ། །
--- END BLOCKS ---
