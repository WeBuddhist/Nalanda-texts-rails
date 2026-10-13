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
[Block 4621 [VERSE]]
རྡོ་རྗེ་སེམས་དཔའ་རྒྱལ་པོ་ཆེ། །
ཡང་དང་ཡང་དུ་བསྐུལ་བར་བྱ། །
དེ་ནི་སྔགས་རྣམས་ཐམས་ཅད་ཀྱི། །
རྒྱལ་པོ་རྟག་པ་མཆོག་ཡིན་ནོ། །

[Block 4622]
ཞེས་འབྱུང་ངོ་། །

[Block 4623 [VERSE]]
རབ་ཏུ་བྱེད་པ་ལས་ཀྱང་། །
དེ་ནི་རང་བྱུང་བཅོམ་ལྡན་འདས། །
གཅིག་པུའི་བདག་ཉིད་ཆེ་བའི་ལྷ། །
མན་ངག་རྣམས་ནི་རབ་སྟེར་བས། །

[Block 4624]
རྡོ་རྗེ་སློབ་དཔོན་དེ་བས་ལྷག །ཅེས་འབྱུང་ངོ་། །

[Block 4625]
རྡོ་རྗེ་འཆང་གི་སྤྲུལ་པ་ཡི། །ཞེས་པ་ནི། རྡོ་རྗེ་འཆང་ཆེན་པོས་བསྐྱེད་ཅིང་། དེ་ལ་རྗེས་སུ་ཞུགས་ཏེ་དེའི་རྣམ་པ་ཉིད་དུ་འགྱུར་བའོ། །

[Block 4626]
བརྟན་པ་དང་གཡོ་བའི་བདག་ཉིད་འཇིག་རྟེན་པ་འདི་ཇི་སྲིད་དེ་དག་ཐམས་ཅད་རྡོ་རྗེ་འཆང་བ་ལས་བསྐྱེད་ཅིང་དེ་ཉིད་དུ་ཐིམ་མོ། །

[Block 4627]
ཇི་སྐད་དུ།

[Block 4628 [VERSE]]
ཕ་རོལ་འགྲོ་བ་ཁ་ཅིག་གང་། །
རྟགས་ཀྱི་དབྱེ་བས་རྣམ་པར་གནས། །
དེ་རྣམས་ཀྱང་འདིས་སྨོད་མི་བྱ། །
རྡོ་རྗེ་སེམས་དཔས་སྤྲུལ་པ་ཡིན། །

[Block 4629]
ཞེས་འབྱུང་ངོ་། །ནམ་མཁའི་དབྱིངས་ནི་ཐམས་ཅད་ལ། །རྡོ་རྗེ་སེམས་དཔའ་དཔལ་ལྡན་བཞུགས། ཞེས་བདེ༌[^2785]མཆོག་ལས་འབྱུང་ངོ་། །རྣམ་པར་སྣང་མཛད་ཀྱི་ཕྱག་རྒྱ་ཆེན་པོ་ནི་རྡོ་རྗེ་འཆང་ཆེན་པོའི་ལྷག་པར་མོས་པས། བསྒོམ་པའི་རྣམ་པར་སྣང་མཛད་ལ་སོགས་པའི་སྐུ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 4630]
སྐུ་རྡོ་རྗེ་ཉིད་དུ་གྱུར་པ་ཡིན་ཡང་། །ཞེས་པ་ནི་སྐུ་རྣམ་པར་དག་པའི་རང་བཞིན་ཉིད༌[^2786]དུ་གྱུར་པའོ། །

[Block 4631]
ཡོན་ཏན་གྱི་ངོ་བོ་ཉིད་ཀྱང་མངའ་བས་ཞེས་པ་ནི་ནང་དུ་ཆུད་པའི་གསུང་དང་ཐུགས་ཀྱི༌[^2787]ནུས་པས་སོ། །

[Block 4632]
གང་གི་ཕྱིར་བཅོམ་ལྡན་འདས་རྣམ་པར་སྣང་མཛད་ནི་སྐུ་རྡོ་རྗེ་རྣམ་པར་དག་པ་ཡིན་པར་མ་ཟད་ཀྱི། འོན་ཀྱང་གསུང་དང་ཐུགས་རྣམ་པར་དག་པའི་ངོ་བོ་ཡང་ཡིན་ནོ། །

[Block 4633]
དེ་ཉིད་ཀྱི་ཕྱིར་དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱི་གཙོ་བོར་གྱུར་པའི་ཆ་གཅིག་གིས་མཚན་གྱི་ཐ་སྙད་བྱ་བ་ཡིན་ཏེ། དཔེར་ན་སྙིང་རྗེའི་རང་བཞིན་འཇིག་རྟེན་དབང་ཕྱུག་བཞིན་ནོ། །

[Block 4634]
དེ་ལ་སྙིང་རྗེ་གཅིག་པུ་ཡོད་ཀྱི་ཤེས་རབ་ལ་སོགས་པ་སངས་རྒྱས་ཀྱི་ཡོན་ཏན་གཞན་མེད་པ་མ་ཡིན་ནོ། །

[Block 4635]
གཙོ་བོ་དང་གཙོ་བོ་མ་ཡིན་པའི་སངས་རྒྱས་ཀྱི་ཡོན་ཏན་དང་ལྡན་པ་སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་ཡིན་ནོ། །

[Block 4636]
དཔེར་ན་ཞི་བའི་རང་བཞིན་རྣམ་པར་སྣང་མཛད་ཡིན་ནོ༌[^2788]ཞེས་ཞི་བ་ཙམ་གྱི་ངོ་བོ་ཡང་མ་ཡིན༌[^2789]ཏེ། རྒྱས་པ་ལ་སོགས་པ་ཡང་མཛད་པའི་ཕྱིར་རོ། །

[Block 4637]
དེ་བཞིན་དུ་རྒྱས་པ་ལ་སོགས་པའི་རང་བཞིན་རིན་ཆེན་འབྱུང་ལྡན་ལ་སོགས་པ་ཡང་ཤེས་པར་བྱའོ། །

[Block 4638]
སེམས་ཅན་རྣམས་ཀྱི༌[^2790]བསམ་པ་དང་བག་ལ་ཉལ་དང་བག་ཆགས་དང་རིགས་ཀྱི་དབྱེ་བས་དེ་དང་རྗེས་སུ་མཐུན་པའི་གཙོ་བོར་གྱུར་པའི་ཡོན་ཏན་གྱི་ཁྱད་པར་དམིགས་ཏེ། བཅོམ་ལྡན་འདས་ཀྱིས༌[^2791]དེ་བཞིན་གཤེགས་པ་དང་བྱང་ཆུབ་སེམས་དཔའ་ལ་སོགས་པའི་རང་བཞིན་བསྟན་ཏོ། །

[Block 4639]
དེ་བཞིན་དུ་མེ་ལོང་ལྟ་བུ་ལ་སོགས་པའི་ཡེ་ཤེས་ལྔའི་རང་བཞིན་རྣམ་པར་སྣང་མཛད་ལ་སོགས་པ་རེ་རེ་ལ་ཡོད་ན་ཡང་མོས་པའི་དབྱེ་བས་ཡེ་ཤེས་རེ་རེའི་རང་བཞིན་དུ་བསྟན་ཏོ། །

[Block 4640]
ཉོན་མོངས་པ་དང་ཤེས་བྱའི་སྒྲིབ་པ་མེད་པ་མངོན་པར་བྱང་ཆུབ་པ་རྣམ་པ་ལྔའི་རིམ་པས་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས༌[^2792]ཀྱི་གོ་འཕང་ཐོབ་པ་དེ་བཞིན་གཤེགས་པ་རྣམས་ལ་བར་ཆོད༌[^2793]མེད་དེ་གང་གིས་དེ་རྣམས་རེ་རེས་མིང་ཐོབ་པ་ཡིན་གྱི་ཚང་བས་ནི་མ་ཡིན་ནོ། །

[Block 4641]
ལས་དང་པོ་པ་འཇུག་པར་བྱ་བའི་ཕྱིར་རིམ་གྱིས་ཡེ་ཤེས་ཐོབ་པ་ཡིན་ནོ་ཞེས་མེ་ལོང་ལྟ་བུ་ལ་སོགས་པའི་རང་བཞིན་བསྟན༌[^2794]ཏོ། །

[Block 4642 [VERSE]]
ཆོས་དང་ཆོས་མིན་དཀའ་ཐུབ་སྟོང་། །
བསྡམས༌[^2795]དང་ངེས་བསྡམས་འདུལ་བ་དང་། །
དུད་འགྲོ་དམྱལ་བ་ཡི་དགས་དང་། །
ལྷ་དང་བཅས་པའི་མི་རྣམས་དང་། །

[Block 4643 [VERSE]]
སྟོན་པ་དང་ནི་ཉན་ཐོས་དང་། །
ཐམས་ཅད་དེ་དག་ཀུན་རྫོབ་སྟོན། །
ལས་དང་པོ་ཡི་འཇིག་རྟེན་པ། །
དོན་དམ་པ་ལ་འཇུག་པའི་ཕྱིར། །

[Block 4644 [VERSE]]
ཐབས་འདི་རྫོགས་པའི་སངས་རྒྱས་ཀྱིས། །
སྐས་ཀྱི་རིམ་པ་ལྟ་བུར་གསུངས། །
དེ་ལྟར་བྱིས་པའི་སྨྲ་བ་འདི། །
མཐར་ནི་ཐམས་ཅད་འཇིག་པར་འགྱུར། །

[Block 4645 [VERSE]]
བརྗོད་དུ་མེད་ཅིང་བརྗོད་མེད་པའི། །
གང་ཡང་དེ་ཉིད་སྣང་བའོ། །

[Block 4646]
ཞེས་འབྱུང་ངོ་། །དེ་བས་ན་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་སྐུ་གསུང་ཐུགས་ཀྱི་རྣམ་པར་དག་པའི་རང་བཞིན་ཡང་གདུལ༌[^2796]བྱའི་དབང་གིས་ངོ་བོ་གཅིག་ཡིན་ནོ་ཞེས་བསྟན་ཏོ། །

[Block 4647]
རྒྱུ་དུ་མ་ཚོགས་པ་ལས་སྐྱེས་པའི་འབྲས་བུ་གང་ལས་དེ་མ་ཐག་ཏུ་སྐྱེས་པ་དེ་དེས་མིང་གི་ཐ་སྙད་དུ་བྱས་ཏེ། དཔེར་ན་རྔ་བོ་ཆེའི་སྒྲ་དང་ནས་ཀྱི་མྱུ་གུ་བཞིན་ནོ། །

[Block 4648]
དེ་བཞིན་དུ་གང་ལ་དམིགས་ནས་རྣམ་པར་དག་པ་འབྱུང་བ་གང་ཡིན་པ་དེ། དེའི་མིང་གིས་བསྟན་པ་ཡིན་ཏེ། དཔེར་ན་སྐུ་རྡོ་རྗེ་དང་གསུང་རྡོ་རྗེ་དང་ཐུགས་རྡོ་རྗེ་ལ་སོགས་པ་བཞིན་ནོ། །

[Block 4649]
འདི་ལ་ལྷ་རྣམས་ཀྱི་འཁོར་ལོ་བསྡུས་པས་ན་ཞེས་པ་ལ། རྡོ་རྗེ་འཆང་ཆེན་པོ་ཉིད་ལ་དཀྱིལ་འཁོར་གྱི་འཁོར་ལོ་ཐམས་ཅད་ཡོངས་སུ་བསྡུ་བར་འགྱུར་ཏེ། གང་གི་ཕྱིར་ཟུང་དུ་འཇུག་པའི་རིམ་པས་ཐོབ་པར་བྱ་བའི་རྡོ་རྗེ་འཆང་ཆེན་པོའི་སྐུ་ལ་ཕུང་པོ་ལ་སོགས་པའི་དཀྱིལ་འཁོར་གྱི་འཁོར་ལོ་ཐིམ་པར་སྣང་སྟེ།

[Block 4650 [VERSE]]
བདེན་པ་གཉིས་གཉིས་སུ་མེད་པའི་ཕྱིར་རོ། །
དེ་ནི་ཉེ་བར་མཚོན་པ་ཙམ་ཡིན་ཏེ། །

[Block 4651]
ཉོན་མོངས་པ་དང་ཉེ་བའི་ཉོན་མོངས་པའི་ཁམས་གསུམ་པ་ཡང་དེ་ལ་ཐིམ་པར་འགྱུར་ཏེ། ཇི་སྐད་དུ།

[Block 4652 [VERSE]]
དབྱིབས་དང་ཁ་དོག་སྣ་ཚོགས་པའི། །
ཇི་སྲིད་སྤྲིན་ནི་དུ་མ་རྣམས། །
ནམ་མཁའི་ཁམས་ལས་བྱུང་ནས་ནི། །
དེ་ཉིད་དུ་ནི་ཐིམ་པར་འགྱུར། །

[Block 4653 [VERSE]]
དེ་བཞིན་རང་བཞིན་ཐམས་ཅད་ནི། །
སྣང་བ་གསུམ་གྱི་རྒྱུར་གྱུར་པ། །
མ་ལུས་ཡུལ་ལ༌[^2797]ཞུགས་ནས་ནི། །
འོད་གསལ་བར་ནི་འཇུག་པར་འགྱུར། །

[Block 4654]
ཞེས་འབྱུང་ངོ་། །ཐེག་པ་ཆེན་པོའི་མདོ་ལས་ཀྱང་། །

[Block 4655 [VERSE]]
སྐྲ་རྩེ་གཅིག་ལས་སངས་རྒྱས་དུ་མ་ནི། །
གང་གཱའི་བྱེ་མ་སྙེད་དང་མཚུངས་པ་སྟེ། །
རྡུལ་གཅིག་སྟེང་ན་རྡུལ་སྙེད་སངས་རྒྱས་རྣམས། །
སངས་རྒྱས་སྲས་ཀྱི་དབུས་ན་བཞུགས་པའོ། །

[Block 4656]
ཞེས་འབྱུང་ངོ་། །རྡོ་རྗེ་འཆང་ཆེན་པོ་སྟེ་ཞེས་པ་ནི་དྲུག་པའོ། །

[Block 4657]
དེ་དང་ལྷན་ཅིག་ཏུ་སྦྱོར་བ་ཞེས་པ་ནི་དང་པོ་སྦྱོར་བའི་ཏིང་ངེ་འཛིན་གྱི་ཕྱོགས་གཅིག་ནི་ཏིང་ངེ་འཛིན་གྱིས་རྫོགས་ལ་རྡོ་རྗེ་འཆང་ཆེན་པོའི་སྐུ་བསྒོམས་པའི་འོག་ཏུ་རང་གི་ཐུགས་ཀ་ནས་མི་བསྐྱོད་པ་སྤྲོས་ཏེ། །དེས་འགྲོ་བའི་དོན་བྱས་ལ་དེ་དང་ལྷན་ཅིག་དུས་གཅིག་ཏུ་གྱུར་ནས་མི་བསྐྱོད་རྡོ་རྗེར་བདག་ཉིད་བསྒོམ་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4658]
དེ་བཞིན་དུ་ཞེས་བྱ་བ་ལ་སོགས་པས་རིན་ཆེན་འབྱུང་ལྡན་ལ་སོགས་པའི་ཏིང་ངེ་འཛིན་བསྟན་ཏོ། །

[Block 4659]
སྐུ་མདོག་ཅེས་བྱ་བ་ལ་སོགས་པས་ཞེ་སྡང་རྡོ་རྗེ་ལ་སོགས་པའི་སྐུ་མདོག་དང་ཕྱག་མཚན་དང་ཉམས་དང་རྣམ་པར་དག་པ་བསྟན་ཏེ། ཁྲོ་བ༌[^2798]དང་འདོད་ཆགས་ཆེན་པོ་འདྲེས་པར་གྱུར་པས་ཞེས་པ་ནི་རྣལ་འབྱོར་ཆེན་པོའི་རྒྱུད་ནི་འདོད་ཆགས་དང་། ཞེ་སྡང་རྣམ་པར་དག་པའི་རང་བཞིན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4660]
དེ་ལ་མཆེ་བ་ཅུང་ཟད་གཙིགས་པའོ་ཞེས་པ་ནི་ཁྲོ་བོའི་ཉམས་དང་ལྡན་པ་དང་རེག་བྱ་རྡོ་རྗེ་མས་འཁྱུད་པ་ཆགས་པའི་རོ་དང་ལྡན་པར་བསྟན་ཏོ། །
--- END BLOCKS ---
