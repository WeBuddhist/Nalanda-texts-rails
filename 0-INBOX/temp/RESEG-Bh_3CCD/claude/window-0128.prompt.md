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
[Block 4481]
འབྲས་བུ་ཐོབ་པས་གང་འདོར་བ༌[^2715]དེ་ནི་ཐབས་ཞེས་བཤད་པ་ཡིན།

[Block 4482 [VERSE]]
དེ་ལྟར་ཁ་ཅིག་མེ་སྒྲོན་མས། །
ལམ་ལ་མཐོང་སྟེ་དེ་ཉིད་བོར། །
ཤེས་པས་ཤེས་བྱ་གཟིགས་ནས་ནི། །
དེ་བཞིན་གཤེགས་པ་འདོར་བར་བྱ། །

[Block 4483]
ཞེས་འབྱུང་ངོ་། །ཡང་ན་བསྒོམ་པར་བྱ་བ་མེད་པའོ་ཞེས་པ་ནི་འོད་གསལ་བའི་ཡུལ་དུ་ཉིན་མོ་དང་མཚན་མོ་མཚམས་དང་ཆགས༌[^2716]དང་ཆགས་བྲལ་དང་ཆགས་པ་བར་མ་རྣམས་ནི་བསྒོམ་པར་བྱ་བ་མ་ཡིན་ཏེ། འདུས་བྱས་པ་དང་འདུས་མ་བྱས་པ་དག་འགལ་བའི་ཕྱིར་རོ། །

[Block 4484]
མཚན་མོ་སྣང་བའི་ཆ་སྟེ་ཉི་མའི་འོད་ཟེར་འགྱེད་པ་སྣང་བ་མཆེད་པ་ཡིན། །མཚམས་ནི་སྣང་བ་མཆེད་པ་རང་གི་རང་བཞིན་ལྷན་ཅིག་མིན་དང་སྦྱར། །མཚན་མོ་མ་ཡིན་མཚམས་མིན་ཉིན་མིན་རང་བཞིན་གང་དག་པ། །དེ་ནི་བྱང་ཆུབ་སྐད་ཅིག་བླ་མ་མཆོག་བཤད་རྣལ་འབྱོར་པ་ཉིད་ཡུལ། །ཞེས་འབྱུང་ངོ་། །བསྒོམ་པ་ཡང་མེད་དེ་ཞེས་བྱ་བ་ནི་དེ་ཐོབ་པར་བྱ་བའི་ཕྱིར་སེམས་རྩེ་གཅིག་པ་ཉིད་ཀྱི་ཏིང་ངེ་འཛིན་གྱི་ཁྱད་པར་ཡང་མེད་དོ། །

[Block 4485]
བསྒོམ་པར་བྱ་བ་མེད་པའི་ཕྱིར་རོ་ཞེས་པ་ལ་བསྒོམ་པར་བྱ་བ་ནི་འོད་གསལ་བ་སྟེ། དེ་མེད་པ་ནི་འདུས་བྱས༌[^2717]པའི་ཚུལ་དུ་མེད་པ་དང་། ངོ་བོ་ཉིད་ཀྱིས་གྲུབ་པ་དང་། བསྒོམ་པ་ནི་གློ་བུར་གྱི་དྲི་མ་སེལ་བའི་མཚན་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4486]
འོ་ན་ལྷའི་རྣལ་འབྱོར་དུ་ཇི་ལྟར་འགྱུར་ཞེ་ན་ཞེས་པ་ནི། དགོངས་པ་ནི་འདི་ཡིན་ཏེ། མངོན་པར་བྱང་ཆུབ་པའི་རིམ་པ་ཐོབ་པས་ཟག་པ་མེད་པ་རྣམ་པར་མི་རྟོག་པ་དོན་དམ་པའི་བདེན་པ་ལ་འཇུག་པའི་རྣལ་འབྱོར་པའི་ཆད་པའི་ཕྱོགས་ཀྱི་མཚན་ཉིད་དུ་ཐལ་བར་འགྱུར་རོ། །

[Block 4487]
དེ་བས་དེ་སྤང་བར་བྱ་བའི་ཕྱིར་ལྷའི་རྣལ་འབྱོར་བསྒོམ་པར་བྱ་བའི་རིགས་སོ། །

[Block 4488]
དོན་དམ་པའི་བདེན་པའོ་ཞེས་པ་ནི་ཕྱག་རྒྱ་དང་ཏིང་ངེ་འཛིན་གྱི་རིམ་པས་རྟོགས་པར༌[^2718]བྱ་བའི་དེ་ཁོ་ན་ཉིད་བཞི་པ་སྟེ། དེ་ནི་ནམ་མཁའ་དང་མཚུངས་པའི་ཕྱིར་རོ། །

[Block 4489]
ཀུན་རྫོབ་ཀྱི་བདེན་པའོ་ཞེས་པ་ནི་དེ་ལས་བྱུང་བའི་རྡོ་རྗེའི་སྐུ་སྤྲོས་པས༌[^2719]ཏེ་སེམས་ཅན་གྱི་དོན་གྱི་བྱ་བ་ལ་གཞིར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 4490]
གཅིག་ཏུ་གྱུར་པ་སྟེ་ཞེས་པ་ལ་བཞི་པ་དང་ལྔ་པའི་རིམ་པས་ཐོབ་པར་བྱ་བའི་དོན་དམ་པ་དང་ལྷའི་སྐུ་དག་ཡང་དག་པར་སྦྱོར་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4491]
དེ་དག་གིས༌[^2720]ཞེས་བྱ་བ་ལ་སོགས་པས་ཀུན་ཏུ་འོད་ཀྱི་ས་ལ་གནས་པའི་རྡོ་རྗེ་འཆང་ཆེན་པོའི་སྐུ་བདག་དང་གཞན་ལ་ཕན་ཐོགས་པའི་རྒྱུར་གྱུར་པ་རྣལ་འབྱོར་པས་བསྒོམ་པར་བྱའོ་ཞེས་བསྟན་ཏོ། །

[Block 4492]
དགོངས་པ་མ་ཡིན་པ༌[^2721]ནི་མངོན་པར་བྱང་ཆུབ་པ་དང་ཟུང་དུ་འཇུག་པའི་རིམ་པ་དག་འཆད་པར་འདོད་པའི་ཕྱིར་རོ། །

[Block 4493]
བཤད་ཟིན་ཏོ་ཞེས་པ་ནི་ལེའུ་དང་པོ་ནས་བཤད་པ་རྣམ་པ་བཞི་པོས་བསྟན་ཏོ། །

[Block 4494]
ཆོས་རྣམས་རང་བཞིན་འོད་གསལ་བ། །ཞེས་པ་འདིས་ཟུང་དུ་འཇུག་པའི་ཏིང་ངེ་འཛིན་ཉིད་བསྟན་ཏེ། རང་བཞིན་ནི་ཀུན་རྫོབ་ཀྱི་བདེན་པ་སྟེ། རྒྱུ་དང་རྐྱེན་གྱི་ཁྱད་པར་གྱིས་བྱས་པའི་ཕྱིར་རོ། །

[Block 4495]
འོད་གསལ་བ་ནི་དོན་དམ་པའི་བདེན་པ་སྟེ་ཞེས་པ་ལ། རྟག་པ་དྲི་མ་མེད་པ་ཟག་པ་མེད་ཅིང་དེ་ཁོ་ན་ཉིད་ཀྱི་རང་བཞིན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4496]
ཕྱི་དང་ནང་གི་དངོས་པོ་རྣམས་ནི་བརྟན་པ་དང་གཡོ་བའི་དངོས་པོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 4497]
བདེན་པ་གཉིས༌[^2722]ཀྱི་ངོ་བོ་ཉིད་དོ་ཞེས་པ་ནི་རིམ་པ་གཉིས་པ་དང་བཞི་པས་ཐོབ་པར་བྱ་བའི་འོད་གསལ་བའི་དེ་ཁོ་ན་ཉིད་རིམ་པ་གསུམ་པ་དང་ལྔ་པས༌[^2723]ཐོབ་པར་བྱ་བའི༌[^2724]ཡེ་ཤེས་ཀྱི་སྐུ་དང་། རྡོ་རྗེའི་སྐུའི༌[^2725]རང་བཞིན་ནོ། །

[Block 4498]
དེ་བས་ཞེས་བྱ་བ་ལ་སོགས་པས་ཆོས་ཉིད་ཀྱི་ཕྱོགས་ལ་བརྟེན་ཏེ་རང་བཞིན་གྱིས་དག་པ་ནམ་མཁའ་དང་ཆོས་མཐུན་པ་བསྟན་ཏོ། །

[Block 4499]
འབྲས་བུའི་ངོ་བོ་ཉིད་དོ་ཞེས་པ་ནི་ཟུང་དུ་འཇུག་པའི་རིམ་པའི་མཚན་ཉིད་མི་སློབ་པའི་ཕྱིར་རོ། །

[Block 4500]
དེ་ཐོབ་པའི་རྒྱུ་སྟེ་ཞེས་པ་ནི། རྡོ་རྗེ་བཟླས་པ་ལ་སོགས་པའི་རིམ་པ་བཞི་སྟེ། དེ་རྣམས་ཀྱིས་རིམ་པ་ཇི་ལྟ་བ་བཞིན་དུ་ངག་དང་སེམས་དང་ལུས་དང་ཀུན་རྫོབ་དང་དོན་དམ་པ་རྣམ་པར་དག་པ་ཐོབ་པར་བྱེད་པ་སྒོམ་པས་ཟུང་དུ་འཇུག་པའི་ཏིང་ངེ་འཛིན་ཐོབ་པའི་ཕྱིར་རོ། །

[Block 4501]
ཟུང་འཇུག་གི་ཏིང་ངེ་འཛིན་ལ་གནས་པས། །སླར་ཞིང་གང་ལའང་མི་སློབ་པོ། །ཞེས་འབྱུང་ངོ་། །རྒྱུ་དང་འབྲས་བུ་དབྱེར་མེད་པའི་ཕྱིར་རོ་ཞེས་པ་ནི་ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་ཀྱི་མཚན་ཉིད་ཅན་གྱི་ཟུང་དུ་འཇུག་པའི་ཏིང་ངེ་འཛིན༌[^2726]དེ་ཁོ་ན་ཉིད་ཅེས་བྱ་བ་ཐོབ་ནས་འདིའི་རྒྱུ་དང་འདིའི་འབྲས་བུ་ཞེས་ཐ་དད་པར་མི་སྣང་སྟེ་དེ་ནི་དེའི་རང་བཞིན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4502]
རྒྱུ་དང་འབྲས་བུ་དག་ཅེས་པ་ནི་རྡོ་རྗེ་བཟླས་པ་ལ་སོགས་པའི་རིམ་པ་བཞི་དང་། ཟུང་དུ་འཇུག་པའི་རིམ་པ་དག་གོ། །

[Block 4503]
མི་ཕྱེད་པར་ཡོངས་སུ་ཤེས་པ་ཉིད་ནི་ཞེས་པ་ལ། སློབ་པའི་གནས་སྐབས་སུ་ཡང་ལམ་ནི་དེ་ཁོ་ན་ཉིད་དུ་མོས་པའི་ཕྱིར་འབྲས་བུ་ཐོབ་ནས་ཀྱང་ལམ་ནི་དེ་དང་རོ་གཅིག་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 4504]
ལས་དང་པོ་པ་ཅན་འཇུག་པར་བྱ་བའི་དོན་དུ་རིམ་པའི་དབྱེ་བས་རྒྱུ་དང་འབྲས་བུའི་དབྱེ་བ་རབ་ཏུ་བསྟན་ཏོ། །

[Block 4505]
ལས་དང་པོ་པའི་འཇིག་རྟེན་པ་རྣམས་དོན་དམ་པ་ལ་འཇུག་པའི་ཕྱིར་རོ། །

[Block 4506 [VERSE]]
ཐབས་འདི་རྫོགས་པའི་སངས་རྒྱས་ཀྱིས། །
སྐས་ཀྱི་རིམ་པ་ལྟ་བུར་གསུངས། །

[Block 4507]
ཞེས་འབྱུང་ངོ་། །དགོངས་པ་མ་ཡིན་པ་ཞེས་བྱ་བ་ནི་ཟུང་དུ་འཇུག་པའི་རིམ་པ་འབའ་ཞིག་ཏུ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 4508]
ཡིད་ཀྱི་རང་བཞིན་གྱི་སྐུའོ་ཞེས་པ་ནི། བདག་ལ་བྱིན་གྱིས་བརླབ་པའི༌[^2727]རིམ་པས་ཐོབ་པར་བྱ་བའི་ཡེ་ཤེས་ཀྱི་སྐུའོ། །

[Block 4509]
དོན་དམ་པའི་བདེན་པས་རྣམ་པར་དག་པའོ་ཞེས་པ་ནི་འོད་གསལ་བའི་དེ་ཁོ་ན་ཉིད་བཞི་པས་སོ། །

[Block 4510]
གང་གི་ཕྱིར་སྒྱུ་མ་ལྟ་བུའི་རྣམ་པར་རྟོག་པ་ཉིད་ཡོངས་སུ་སྤོང་བའི་དོན་དུ་འོད་གསལ་བ་དེ་ཁོ་ན་ཉིད་བསྒོམ་པར་བྱའོ། །

[Block 4511]
དེ་གསལ་བར་བྱེད་པའི་ངག་གི་ཚོགས་སོ་ཞེས་པ་ནི་གསུམ་པ་དང་བཞི་པའི་རིམ་པ་རྗོད་པར༌[^2728]བྱེད་པའི་ཚོགས༌[^2729]རྣམས་སོ། །

[Block 4512]
ཀུན་རྫོབ་ཀྱི་བདེན་པས་སོ་ཞེས་པ་ནི་སྒྱུ་མ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་གྱི་རང་བཞིན་གྱི་བདག༌[^2730]བྱིན་གྱིས་བརླབ་པའི་རིམ་པའི་མན་ངག་གིས་སོ། །

[Block 4513]
དོན་དམ་པའི་བདེན་པས་སོ་ཞེས་པ་ནི་དེ་རྣམ་པར་དག་པར་བྱེད་པའི་འོད་གསལ་བ་ལ་འཇུག་པའི་མཚན་ཉིད་ཅན་གྱི་མངོན་པར་བྱང་ཆུབ་པའི་རིམ་པས་སོ། །

[Block 4514]
འགྲོ་བའི་དོན་མཛད་པའི་རྡོ་རྗེ་འཆང་ཆེན་པོའི་སྐུ་ཡང་རྣམ་པར་དག་པར་བྱ་བ་ཡིན་ནོ་ཞེས་བྱ་བས་ངོ་མཚར་བ་དང་རྨད་དུ་གྱུར་པའོ། །

[Block 4515]
ཨེ་མའོ་སངས་རྒྱས་ཞེས་བྱ་བ་ལ་སོགས་པས་དོན་དེ་ཉིད་བསྟན་པར་བྱ་སྟེ། ཀུན་རྫོབ་ཀྱི་བདེན་པའི་སྒོ་ནས་བསྟོད་པའོ་ཞེས་པ་ནི་བདག་ལ་བྱིན་གྱིས་བརླབ་པའི་མན་ངག་གི་སྒོ་ནས་སོ། །

[Block 4516]
དོན་དམ་པའི༌[^2731]བདེན་པའི་སྒོ་ནས་སོ་ཞེས་པ་ནི་སེམས་རྣམ་པར་དག་པ་དང་མངོན་པར་བྱང་ཆུབ་པ་བསྟན་པའི་སྒོ་ནས་སོ། །

[Block 4517]
བདེན་པ་གཉིས་མི་ཕྱེད་པའི་ཞེས་བྱ་བ་ལ་སོགས་པས་ཟུང་དུ་འཇུག་པའི་ཏིང་ངེ་འཛིན་གསལ་བར་བྱེད་པའི་མན་ངག་གི་སྒོ་ནས་བསྟོད་པའོ། །

[Block 4518]
འོད་གསལ་བའོ་ཞེས་པ་ནི་སྔགས་དང་ཕྱག་རྒྱའི་རིམ་པས་ཐོབ་པར་བྱ་བའི་སེམས་རྣམ་པར་དག་པའི་མཚན་ཉིད་དོ། །

[Block 4519]
ཡོངས་སུ་དག་པའི་ལྷའི་སྐུ་སྟེ་ཞེས་པ་ནི་དེ་ལས་བྱུང་བ༌[^2732]ཡེ་ཤེས་ཀྱི་རང་བཞིན་གྱི་སྐུའོ། །

[Block 4520]
དེས་ནི་རིམ་པ་གཉིས་ཀྱི་སྒོ་ནས་བསྟོད་པའོ། །
--- END BLOCKS ---
