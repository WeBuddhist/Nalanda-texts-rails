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
[Block 5391]
ཡང་དག་པ་མ་ཡིན་པ་ཡིད་ལ་བྱེད་པ་ལ་འདྲིས་པས་ཞེས་བྱ་བས་ནི་སྐྱོན་ཚུལ་བཞིན་མ་ཡིན་པ་ཡིད་ལ་བྱེད་པ་ཉིད་སྟོན་ཏོ། །

[Block 5392]
ལོག་པར་ལྟ་བ་སྟུག་པོའི་ཞེས་བྱ་བ་ནི་ལོག་པར་ལྟ་བ་ཡོངས་སུ་མ་བརྟགས་པའི༌[^3444]ཕྱིར། གཉི་གའི་རྐྱེན་ཅན་ཉིད་དུ་བསྟན་ཏོ། །

[Block 5393]
དགེ་བ་དང་མི་དགེ༌[^3445]བའི་ལས་ཀྱི་རྣམ་པར་སྨིན་པ་ནི། འཇིག་རྟེན་ཕ་རོལ་གྱི་བླ་ན་མེད་པའི་ཕྱིར། དགེ་བ་དང་། མི་དགེ་བའི་འབྲས་བུ་རྣམ་པར་སྨིན་པ་ག་ལ་ཡོད་དེ། [^3446]འཇིག་རྟེན་ཕ་རོལ་ཡང་མེད་པའི་ཕྱིར་རོ། །

[Block 5394]
ཆོས་ལ་སྤྱོད་པའི་སྤྲོ་བ་མེད་པ་གང་ཡིན་པ་དེ་ནི་དེའོ། །

[Block 5395]
འདི་ནི་ལྷ་ཁང་དང་། གཙུག་ལག་ཁང་དང་། ཀུན་དགའ་ར་བ་དང་། རྫིང་བུ་ལ་སོགས་པ་བྱེད་པའི་སྤྲོ་བ་མེད་པའོ། །

[Block 5396]
ཡང་ན་སྦྱིན་པ་ལ་སོགས་པ་ཉིད་ཆོས་ཡིན་ཏེ། དེ་དག་གིས་བསམ་པ་ལས་ལྡོག་པ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 5397]
སྦྱིན་པ་དང་། ཚུལ་ཁྲིམས་ལ་སོགས་པའི་ལེགས་པར༌[^3447]སྤྱད་པ་གང་ཡིན་པ་དེ་ནི། སྦྱིན་པ་དང་། ཚུལ་ཁྲིམས་ལ་སོགས་པའི་ལེགས་པར་སྤྱད་པ་སྟེ། དེ་སྒྲུབ་པ་ལ་རྒྱབ་ཀྱིས་ཕྱོགས་པའོ། །

[Block 5398]
འདིས་ནི་སྦྱིན་པ་ལ་སོགས་པར་སྦྱོར་བའི་བྱེད་པ་དང་བྲལ་བ་ཉིད་དུ་བསྟན་ཏོ། །ཅིའི་ཕྱིར་དེ་དེ་ལྟར་གནས་ཤེ་ན། དེའི་རྒྱུ་བསྟན་པའི་ཕྱིར། དགེ༌[^3448]དང་མི་དགེའི་ལས་ལས༌[^3449]ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 5399]
དགེ་བའི་ལས་ལས་ནི་བདེ་བ་བཅུ་འབྱུང་ངོ་། །མི་དགེ་བའི་ལས་ལས་ནི་སྡུག་བསྔལ་འབྱུང་བ་ཡིན་ནོ། །

[Block 5400]
ཕ་རོལ༌[^3450]ཞེས་བྱ་བ་འདིས་ནི་འཇིག་རྟེན་ཕ་རོལ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 5401]
སྡིག་པ་སྤངས་ཏེ་ཞེས་བྱ་བ་སྡིག་པས་ནི་སྡུག་བསྔལ་འབྱུང་བའི་ཕྱིར་ཏེ། སྡུག་བསྔལ་འབྱུང་བ་ནི་མི་འདོད་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 5402]
དགེ་བའི་གནས་ལ་རབ་ཏུ་འབད་པ་ནི་བདེ་བ་འབྱུང་བའི་ཕྱིར་ཏེ། བདེ་བ་ནི་འདོད་པ་ཉིད་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 5403]
དད་པ་མེད་པ་དག་ནི་ཞེས་བྱ་བ་ནི་དགེ་བ་ལ་སོགས་པ་ལའོ། །

[Block 5404]
ངན་སོང་དུ༌[^3451]ལྟུང་བར་འགྱུར་བ་ནི་བདག་ཉིད་དོ། །

[Block 5405]
བདག་ཉིད་གཅིག་པུར་མ་ཟད་དེ། དེ་བཞིན་དུ་འདི་ལྟར་འཇིག་རྟེན་རྣམས་དོན་མེད་པར་བྱེད་པ་སྟེ། སྦྱིན་པ་དང་། ཚུལ་ཁྲིམས་ལ་སོགས་པ་ལས་བཟློག་པའི་ཕྱིར་རོ། །

[Block 5406]
བཟང་པོ་ཞེས་བྱ་བ་ནི་ཡིད་དུ་འོང་བའོ། །

[Block 5407]
རབ་ཏུ་དབེན་པ་ཞེས་སྨོས་པས་ནི་བག་ཡངས་སུ་དེ་སྟོན་པའི་ཕྱིར་རོ། །

[Block 5408]
གཞལ་མེད་ཁང་ཞེས་སྨོས་པས་ནི་བདག་ཉིད་ཕྱོགས་དེ་ན་འདུག་པའོ། །

[Block 5409]
གཞལ་མེད་ཁང་ལ་ཡང་ཐོགས་པ་མེད་པར་འགྲོ་བས། རྫུ་འཕྲུལ་དང་ལྡན་པ་ཉིད་དུ་བསྟན་པའི་ཕྱིར། ཁྱོད་ཀྱི་ཞབས་དང་ཕྱག་མཛེས་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་སྨོས་ཏེ། འདིའི་བསྡུས་པའི་དོན་ནི་རྫུ་འཕྲུལ་གྱི་མཐུས། བདག་ཉིད་ཀྱི་གཟུགས་ཀྱང་ཐུན་མོང་མ་ཡིན་པ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 5410]
འདོད་ཆགས་དང་། ཞེ་སྡང་གཉིས་སྨོས་པས་ནི། འདོད་ཆགས་དང་། ཞེ་སྡང་གཉིས་པོ་འདོད་པ་ན་སྤྱོད་པའི་བསྒོམ་པས་སྤང་བར་བྱ་བ་གཉིས་གཟུང་སྟེ། ཚངས་པའི་འཇིག་རྟེན་དུ་སྐྱེ་བས་སོ། །

[Block 5411]
ཁང་བཟངས་རྩིག་པ་དག་ལ་འང་ཐོགས་པ་མེད། །ཅེས་བྱ་བ་ནི། རྫུ་འཕྲུལ་གྱིས་ཐོགས་པ་དང་བཅས་པ་ལ་ཡང་ཐོགས་པ་མེད་པར་འགྲོ་བའོ། །

[Block 5412]
ས་ལ་འགྲོ་བ་བཞིན་དུ་མཁའ་ལ་འཆག །ཅེས་བྱ་བ་ནི་སའི་འོག་དང་། ནམ་མཁའ་ལ་འཕུར་བ་སྟེ།

[Block 5413 [VERSE]]
འདི་གཉིས་ཀྱིས་ནི་འགྲོ་བའི་རྫུ་འཕྲུལ་བསྟན་ཏོ། །
གློག་གི་འོད་བཞིན་གཟི་བརྗིད་ཕུན་སུམ་ཚོགས། །

[Block 5414]
ཞེས་བྱ་བ་འདིས་ནི། རྫུ་འཕྲུལ་གྱི་ཆོ་འཕྲུལ་གྱི་སྤྲུལ་པའོ། །

[Block 5415]
བསམ་གཏན་ཞེས་བྱ་བ་ནི་ལྷག་པའི་སེམས་སོ། །

[Block 5416 [VERSE]]
ཚུལ་ཁྲིམས་ནི་སྡོམ་པའི་ཚུལ་ཁྲིམས་སོ། །
དབང་པོ་རྣམས་ནི་རབ་ཏུ་བསྡམས། །

[Block 5417]
ཞེས་བྱ་བ་ནི། དབང་པོའི་སྒོ་བསྡམས་པའོ། །

[Block 5418]
གོམས་པར་བྱས་པ་ནི་བསྒོམས་པའོ། །

[Block 5419]
འབྲས་བུ་གྲུབ་པ་འདི་འདྲའོ། ། ཞེས་བྱ་བ་ནི་གྲུབ་པ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 5420]
འདི་ཇི་ལྟར་ཞེས་བྱ་བ་ནི་འཇིག་རྟེན་ཕ་རོལ་ཡོད་པ་ཉིད་དུའོ། །

[Block 5421]
འདི་ནི་རབ་ཏུ་གསལ་ཏེ་ཞེས་བྱ་བ་ནི་འཇིག་རྟེན་ཕ་རོལ་ཡོད་པ་ཉིད་དོ། །

[Block 5422]
མངོན་སུམ་ལ་སོགས་པའི་ཚད་མ་གང་ཡིན་པ་དང་། གང་གི་མངོན་སུམ་ལ་སོགས་པའི་ཚད་མའོ། །

[Block 5423]
དེ་ཉིད་རིགས་པ་ཡིན་པས་མངོན་སུམ་ལ་སོགས་པ་རིགས་པའི་ཚད་མའོ། །

[Block 5424]
དེས་གཟུང་དུ་འོས་པའི་ཕྱིར་མངོན་སུམ་ལ་སོགས་པ་རིགས་པའི་ཚད་མས་གཟུང་དུ་རུང་བ་སྟེ། འཇིག་རྟེན་ཕ་རོལ་ལོ། །

[Block 5425]
འཇིག་རྟེན་ཕ་རོལ་ཡང་རྣམ་པ་གཉིས་ཏེ། མིའི་འཇིག་རྟེན་འདི་ལས་གཞན་པའི་འཇིག་རྟེན༌[^3452]ཕ་རོལ་ལོ། །

[Block 5426]
དེ་རབ་ཏུ་གྲུབ་པ་ནི་མངོན་སུམ་ལ་སོགས་པའི་རིགས་པའི་ཚད་མ་དག་གིས་སོ། །

[Block 5427]
སྐྱེ་བ་འདི་ལས་གཞན་པའི་སྐྱེ་བ་དེ་ཡང་འཇིག་རྟེན་ཕ་རོལ་ཞེས་བརྗོད་དོ། །

[Block 5428]
དེ་ཡོད་པར་ནི་ལུང་གི་ཚིག་གིས་བསྟན་པ་དང་། [^3453]བརྟག་པའི་རིམ་པ་སྟེ། བརྟག་པའི་རིམ་པ༌[^3454]ནི། རིགས་པས་ཡིད་ཆེས་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5429]
དེ་ལས་མིའི་འཇིག་རྟེན་ལས་གཞན་པའི་འཇིག་རྟེན་ཡོད་པར་བསྟན་པའི་ཕྱིར་ཏེ། [^3455]ཉི་ཟླ་སྐར་མས་བརྒྱན་པའི་ནམ་མཁའ་དང་། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 5430]
ཉི་ཟླ་སྐར་མས་བརྒྱན་པའི་ནམ་མཁའ་དང་། །ཞེས་བྱ་བ་འདིས་ནི་མིའི་འཇིག་རྟེན་འདི་ལས་གཞན་པའི་འཇིག་རྟེན་ཉིད་མངོན་སུམ་གྱི་རིགས་པའི་ཚད་མས་གཟུང་དུ་རུང་བ་ཉིད་དུ་བསྟན་ཏོ། །
--- END BLOCKS ---
