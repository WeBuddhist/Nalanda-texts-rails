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
[Block 596]
ཧཾ་ནི་བདེ་བ་ལྷན་ཅིག་སྐྱེས་པའི་རླུང་དང་བཅས་པའོ། །

[Block 597]
འཛག་པ་ནི་ནང་དུ་འབར་བ་སྟེ་བདེ་གསལ་མི་རྟོག་པའོ། །

[Block 598]
ལེའུའི་མཚན་ཡང་ཕྱོགས་རེ་རེ་ནས་བརྟགས་པ༌[^193]ཕལ་ཆེར་ཡིན་ཡང་འདིར་ནི་ཀུན་ལ་སྦྱར་ཏེ་དང་པོ་གླེང་གཞི་ཡང་པ་རི་ཝརྟ༌[^194]ཞེས་བྱ་སྟེ། བརྗེ་བའམ་རྣམ་པར་འཕྲོག་པའོ། །

[Block 599 [VERSE]]
དེས་ན་རྡོ་རྗེ་ནི་དགྱེས་པའི་རྡོ་རྗེའོ། །
རིགས་ནི་འཁོར་ལ་སོགས་པའི་ཡན་ལག་གོ། །
ལེའུ་ནི་སྟོན་པ་ལ་འཁོར་དུ་འཕྲོ་ཞིང་བརྗེ་བའམ།

[Block 600]
སྟོན་པ་ལ་སོགས་པ་རྣམ་པར༌[^195]ཕྱེ་བའོ། །

[Block 601]
ཡང་ཞུས་པ་དང་ལན་གྱིས་རྡོ་རྗེ་ནི་སྟོན་པའོ། །

[Block 602]
རིགས་ནི་རྡོ་རྗེ་སྙིང་པོ་སྟེ་དེས་ན་སྙིང་རྗེའི་རིགས་སོ། །

[Block 603]
[^196]ལེའུ་ནི་པ་ར་ཙྪེ་ད་སྟེ་ཡོངས་སུ་གཅོད་ཅིང་གཏུབས༌[^197]ནས་ཞུས་ཏེ། བཅད་ཅིང་གཏུབས༌[^198]ནས་རྣམ་པར་ཕྱེ་སྟེ་ལན་བཏབ༌[^199]པའོ། །

[Block 604]
ཡང་རྒྱུད་ཀྱི་ཚུལ་ཡང་དམིགས་པའི་ཡུལ་ལྟ་སྟངས་ལ་སོགས་པ་དངོས་གྲུབ་ཡིན་པས་རྡོ་རྗེའོ། །

[Block 605]
དེ་བསྒྲུབ་པའི་རྣལ་འབྱོར་པ་ནི་རིགས་སོ། །

[Block 606]
ལེའུ་ནི་པ་ཏ་ལ་སྟེ་སྲ་བ་དང་། སྐྱོབ་པས་གོས་དང་འདྲ་བར་འཚེ་བ་དང་ངོ་ཚ་སྐྱོབ་ཅིང་སྲུང༌[^200]བས་དངོས་གྲུབ་ཀྱང་དེ་ལྟ་བུར་ཤེས་པར་བྱའོ། །

[Block 607]
ཡང་ཉམས་སུ་བླང་བའི་ཐབས་ཀྱང་རྡོ་རྗེ་ནི༌[^201]རྫོགས་རིམ་མོ། །

[Block 608]
རིགས་ནི་སྐྱེད་རིམ་མོ། །

[Block 609 [VERSE]]
ལེའུ་ནི་རྣམ་པར་ཕྱེ་སྟེ་བསྟན་པའོ། །
དང་པོ་ནི་གཞན་ལ་ལྟོས་པའམ།
ཕྲ་མ་ཐ་སྟེར་བ་མཆོག་གོ། །

[Block 610]
ལེའུ་དང་པོ་རྡོ་རྗེ་རིགས་ཀྱི་ལེའུའི༌[^202]དོན་ཡི་གེར་བྲིས་པ་རྫོགས་སོ།། །།

[Block 611]
དེ་ནས་ཉམས་སུ་བླང་བའི་ཐབས་བསྐྱེད་པའི་རིམ་པ་དང་རྫོགས་པའི་རིམ་པ་དང་རིམ་པ་གཉིས་བསྡོམས་ཏེ་ལེའུ་སོ་སོར་སྟོན་ཏོ། །

[Block 612]
དེ་ལ་ལེའུ་གཉིས་པ་ནི་བསྐྱེད་པའི་རིམ་པའི་རྒྱུའོ། །

[Block 613]
གསུམ་པ་ནི་ངོ་བོའོ། །

[Block 614]
བཞི་པ་ནི་འབྲས་བུ་རྫོགས་པའོ། །

[Block 615]
ལྔ་པ་ནི་རྫོགས་པའི་རིམ་པའི་ལྷ་བསྒོམ་མོ། །

[Block 616]
དྲུག་པ་ནི་སྤྱོད་པའོ། །

[Block 617]
བདུན་པ་ནི་འབྲས་བུའི་ཡོན་ཏན་ནམ་དེའི་ཡན་ལག་གོ། །

[Block 618 [VERSE]]
བརྒྱད་པ་ནི་རིམ་པ་གཉིས་ཀའི་གཞིའམ༌[^203]མ་རྟེན་ནོ། །
དགུ་པ་ནི་རིམ་པ་གཉིས་དག་པའི་ཚུལ་ལོ། །

[Block 619]
བཅུ་པ་ནི་རིམ་པ་གཉིས་དབང་ལམ་དུ་བྱེད་པས་རྒྱུད་ལ་སྐྱེ་བའོ། །

[Block 620 [VERSE]]
དོན་གྱི་གོ་རིམས་གཉིས་པར་འོང་ངོ་། །
དེ་དག་ནི་ལམ་ཉམས་སུ་བླང་བའི་ཐབས་སོ། །

[Block 621 [HEADING]]
##### འབྲས་བུ། ^1-1-5-3-0

[Block 622]
བཅུ་གཅིག་པ་ནི་ཉམས་སུ་བླང་བའི་འབྲས་བུར་ཤེས་པར་བྱའོ། །

[Block 623 [HEADING]]
### ལེའུ་གཉིས་པ་བསྐྱེད་པའི་རིམ་པའི་རྒྱུ། ^1-2-0

[Block 624]
དེ་ལ་སྔགས་ཀྱི་ལེའུ་བཤད་པར་བྱའོ་ཞེས་སྡུད་པ་པོས༌[^204]མཚམས་སྦྱར་བ་ཡང་། སྔགས་ནི་མནྟྲ་སྟེ་མ་ཡིད།[^205] ཡིད་ཅན་འགྲོ་བ་ཀུན་ཏྲ་སྟེ་སྐྱོབ་པའོ། །

[Block 625]
ཇི་སྐད་དུ། མ་ནི་ཡིད་ཅེས་བརྗོད་པ་སྟེ། ཏྲ་ཏ༌[^206]སྐྱོབ་པ་ཞེས་སུ༌[^207]གསུངས། ། ཞེས་པའོ། །

[Block 626]
ཡང་ན་མ་མ་ནི་སྙིང་པོའམ་དེ་ཁོ་ན་ཉིད་ཏྲ་ཏ་སྟེ། བསྲུང་བའམ་མི་འབྲལ་བའོ། །

[Block 627]
ཡང་ཨ༌[^208]ཀཱ་རོའི་དོན་ལ་མོས་པར་བྱའོ་ཞེས་གསུངས་པའོ་ནི༌[^209]མནྟྲ་སྟེ་སྤྱན་འདྲེན་པར་བྱེད་པའོ། །

[Block 628]
ཡང་སྔགས་ནི་སྤྱན་འདྲེན་པར་གསུངས་པ་སྟེ། དཔེར་ན་སྐྱེས་ཆེན་འགའ་ཞིག་ལ།

[Block 629 [VERSE]]
ཆེ་ལ་མྱུར་བའི་སྒྲས་བོས་ནས། །
ཐོས་པ་ཙམ་གྱིས་འོངས་པ་བཞིན། །
མཁའ་འགྲོ་མ་དང་བཙུན་མོ་བཟང་། །
དེ་རྣམས་མངོན་དུ་ཕྱོགས་ཕྱིར་རོ། །

[Block 630]
ལེའུ་ནི་སྔ་མ་ལྟར་རོ། །

[Block 631]
འདིར་བསྐྱེད་པའི་རིམ་པའི་རྒྱུར་ཇི་ལྟར་འགྱུར་ཞེ་ན།

[Block 632 [VERSE]]
དེ་ཡང་སྙིང་པོ་དང་ལྷའི་སྔགས་སོ། །
དེ་ལ་སྙིང་པོ་ནི་བསྐྱེད་པའི་རིམ་པའི་རྒྱུའོ། །
ལྷའི་སྔགས་ནི་གསལ་བར་བྱེད་པའི་རྒྱུའོ། །

[Block 633]
ལས་ཀྱི་སྔགས་ནི་ནུས་པ་ཐོབ་པར་བྱེད་པའི་རྒྱུ་ཡིན་པའི་ཕྱིར་སོམ་ཉི་མི་བྱའོ། །

[Block 634]
དང་ལ༌[^210]གཏོར་མའི་སྔགས་བསྟན་པ་ཡང་གཏོར་མ་ནི་ལས་རྣམས་སྒྲུབ་པའི་སྔོན་དུ་འགྲོ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 635]
དེ་ལ་ཨོཾ་ཨ༌[^211]ཀཱ་རོ་ནི༌[^212]ཝ་ར་ཎ་སྟེ་ཨ་ཨརྠ་ནི་དོན། །ཨུ་ཧ་བི་ག་ཏ་དོན་དང་བྲལ༌[^213]བའོ། །
--- END BLOCKS ---
