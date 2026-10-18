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
[Block 1891]
གང་དག་གཟུགས་ཀྱི་སྐལ་བ་མཉམ་པའི་རྒྱུ་གཟུགས་ཡིན་པར་མི་འདོད་པ་དེ་དག་ལ་ནི་འདས་པའི་འབྱུང་བ་ཆེན་པོ་རྣམས་ནི་མ་འོངས་པའི་འབྱུང་བ་ཆེན་པོ་རྣམས་ཀྱི་རྒྱུ་དང་བདག་པོ་ཡིན་ནོ་ཞེས་བྱ་བའི་གཞུང་འདི་འདོད་པ་ལ་གནོད་པར་གནས་སོ། །

[Block 1892]
ཅི་འདྲ་བ་ཐམས་ཅད་འདྲ་བ་ཐམས་ཅད་ཀྱི་སྐལ་བ་མཉམ་པའི་རྒྱུ་ཡིན་ནམ་ཞེ་ན། སྨྲས་པ་མ་ཡིན་ནོ། །

[Block 1893]
འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན། རང་རིས་ས་པའོ། །

[Block 1894]
འདི་དག་ལ་རང་གི་རིས་དང་ས་ཡོད་པས་འདི་དག་ནི་རང་གི་རིས་དང་ས་པ་དག་གོ། །

[Block 1895]
རིས་ནི་ལྔ་སྟེ། སྡུག་བསྔལ་མཐོང་བས་སྤང་བར་བྱ་བ་ནས་བསྒོམ་པས་སྤང་བར་བྱ་བའི་བར་རོ། །

[Block 1896]
ས་ནི་དགུ་སྟེ། འདོད་པའི་ཁམས་དང་བསམ་གཏན་དང་གཟུགས་མེད་པ་བརྒྱད་དོ། །

[Block 1897]
དེ་ལ་སྡུག་བསྔལ་མཐོང་བས༌[^944]སྤང་བར་བྱ་བ་རྣམས་ནི་སྡུག་བསྔལ་མཐོང་བས་སྤང་བར་བྱ་བ་རྣམས་ཀྱི་སྐལ་བ་མཉམ་པའི་རྒྱུ་ཡིན་གྱི་གཞན་དག་གི་ནི་མ་ཡིན་ནོ། །

[Block 1898]
དེ་བཞིན་དུ་བསྒོམ་པས་སྤང་བར་བྱ་བའི་བར༌[^945]དུ་ཡང་བསྒོམ་པས་སྤང་བར་བྱ་བ་རྣམས་ཀྱི་ཡིན་ནོ། །

[Block 1899]
དེ་དག་ཀྱང་འདོད་པ་ན་སྤྱོད་པ་རྣམས་ནི་ཡང༌[^946]འདོད་པ་ན་སྤྱོད་པ་རྣམས་ཀྱི་ཡིན་ལ། བསམ་གཏན་དང་པོའི་ས་པ་རྣམས་ཀྱང་བསམ་གཏན་དང་པོའི་ས་པའི་ཡིན་པ་ནས་སྲིད་པའི་རྩེ་མོའི་ས་པའི་བར་དག་ཀྱང་དེའི་ས་པའི་རྣམས་ཁོ་ནའི་ཡིན་གྱི༌[^947]གཞན་དག་གི་ནི་མ་ཡིན་ནོ། །

[Block 1900]
དེ་དག་ཀྱང་ཐམས་ཅད་ནི་མ་ཡིན་ནོ། །

[Block 1901]
འོ་ན་ཅི་ཞེ་ན། སྔར་སྐྱེས་པ་རྣམས་ནི་ཕྱི་མ་སྐྱེ་བ་དང་མ་སྐྱེས་པ་རྣམས་ཀྱི་སྐལ་བ་མཉམ་པའི་རྒྱུ་ཡིན་ནོ། །

[Block 1902]
མ་འོངས་པ་ཁོ་ན་སྐལ་བ་མཉམ་པའི་རྒྱུ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་དག་ལས་སྨྲས་པ། བསྟན་བཅོས་ལས་ཏེ། སྐལ་བ་མཉམ་པའི་རྒྱུ་གང་ཞེ་ན། དགེ་བའི་རྩ་བ་སྔར་བྱུང་བ་རྣམས་ནི་རང་གི་ཁམས་ན་དགེ་བའི་རྩ་བ་ཕྱིས་འབྱུང་བ་རྣམས་དང་། དེ་དག་དང་མཚུངས་པར་ལྡན་པའི་ཆོས་རྣམས་ཀྱི་སྐལ་བ་མཉམ་པའི་རྒྱུས་རྒྱུ་ཡིན་ནོ། །

[Block 1903]
དེ་ལྟར་ན་འདས་པ༌[^948]དང་། ད་ལྟར་བྱུང་བ་རྣམས་ཀྱི་ཡིན་ནོ། །

[Block 1904]
འདས་པ་དང་ད་ལྟར་བྱུང་བ་རྣམས་ནི་མ་འོངས་པ་རྣམས་ཀྱི་ཡིན་ནོ་ཞེས་བརྗོད་པར་བྱའོ་ཞེས་འབྱུང་ངོ་། །ཆོས་གང་ཆོས་གང་གི་རྒྱུའི་ཡིན་པའི་ཆོས་དེ་རེས་འགའ་ཞིག་ཆོས་དེའི་རྒྱུ་མ་ཡིན་པ་ཡིན་ནམ་ཞེ་ན་སྨྲས་པ། ནམ་ཡང་མ་ཡིན་ནོ་ཞེས་འབྱུང་བ་འདི་ཡང་བསྟན་བཅོས་ཡིན་ནོ། །

[Block 1905]
ལྷན་ཅིག་འབྱུང་བ་དང་མཚུངས་པར་ལྡན་པ་དང་རྣམ་པར་སྨིན་པའི་རྒྱུ་ལས་དགོངས་ནས་གསུངས་པའི་ཕྱིར་དེ་ནི་ཉེས་པ་མེད་དོ། །

[Block 1906]
གང་ཞིག་ཆོས་མ་འོངས་པ་དེ་ཡང་སྐྱེ་བའི་ཚེའི་གནས་སྐབས་ན་སྐལ་བ་མཉམ་པའི་རྒྱུ་ཉིད་དུ་ངེས་པར་འགྱུར་བ་ཡིན་ནོ། །

[Block 1907]
དེའི་ཕྱིར་ཐ་མའི་གནས་སྐབས་དེ་ལས༌[^949]དགོངས་ནས་ནམ་ཡང་རྒྱུ་མ་ཡིན་པ་མ་ཡིན་ནོ་ཞེས་གསུངས་སོ་སྙམ་དུ་སེམས་པ་དེ་ནི་དེའི་ལན་དུ་མི་རུང་སྟེ། འདི་ལྟར་ཆོས་དེ་སྐྱེ་བའི་གནས་སྐབས་ཀྱི་སྔོན་རོལ་ནས༌[^950]སྐལ་བ་མཉམ་པའི་རྒྱུ་མ་ཡིན་པ་ལས་ཕྱིས་ཡིན་པས་སོ། །

[Block 1908]
ཆོས་གང་ཞིག་ཆོས་གང་གི༌[^951]མཚུངས་པ༌[^952]དེ་མ་ཐག་པ་ཡིན་པའི་ཆོས་དེ་རེས་འགའ་ཞིག་ཆོས་དེའི་མཚུངས་པ་དེ་མ་ཐག་པ་མ་ཡིན༌[^953]ནམ་ཞེས་བྱ་བ་འདྲི་བ་འདི་ཡང་ཡོངས་སུ་རྟོགས་པ་འདིས་རེས་འགའ་ཡང༌[^954]མ་ཡིན༌[^955]ནོ་ཞེས་བརྗོད་པར་ནུས་ན་ཅིའི་ཕྱིར་འདི་སྐད་དུ་གལ་ཏེ་ཆོས་དེ་མ་སྐྱེས་པར་གྱུར་ནའོ་ཞེས་གསུངས།

[Block 1909]
དེར་ཇི་ལྟ་བ་དེ་བཞིན་འདིར་ཡང་བརྗོད་པར་བྱ་ལ། འདིར་ཇི་ལྟ་བ་དེ་བཞིན་དེར་ཡང་བརྗོད་པར་བྱའོ་ཞེས་སྒོ་གཉིས་སུ་བསྟན་པར་བྱ་བའི་བར་རོ། །

[Block 1910]
དེ་ལྟ་ཡིན་ན་ཡོན་ཏན་ཅི་ཞིག་འཐོབ་པར་འགྱུར་ཏེ། དེ་ལྟ་ན་འདིར༌[^956]བསྟན་བཅོས་བྱེད་པ་མི༌[^957]མཁས་པ་ཁོ་ནར་ཡིད་ཆེས་པར་འགྱུར་རོ། །

[Block 1911]
དེ་ལྟ་བས་ན་འདིར་ལན་སྔ་མ་ཁོ་ན་ལེགས་པ་ཡིན་ནོ། །

[Block 1912]
འོ་ན་གང་འདི་སྐད་དུ་འཇིག་ཚོགས་ལ་ལྟ་བ་མ་འོངས་པ་དང་། དེ་དང་མཚུངས་པར་ལྡན་པའི་སྡུག་བསྔལ་གྱི་བདེན་པ་མ་གཏོགས་པ་དེ་ལས་གཞན་པའི་སྡུག་བསྔལ་གྱི་བདེན་པ་གང་ཡིན་པ་དེ་ནི་འཇིག་ཚོགས་ལ་ལྟ་བའི་རྒྱུ་ལས་བྱུང་བ་ནི་ཡིན་ལ། འཇིག་ཚོགས་ལ་ལྟ་བའི་རྒྱུ་ནི་མ་ཡིན་ནོ། །

[Block 1913]
མ་གཏོགས་པ་གང་ཡིན་པ་དེ་ནི་འཇིག་ཚོགས་ལ་ལྟ་བའི་རྒྱུ་ལས་བྱུང་བ་ཡང་ཡིན་ལ་འཇིག་ཚོགས་ལ་ལྟ་བའི་རྒྱུ་ཡང་ཡིན་ནོ་ཞེས་གསུངས་སོ་ཞེ་ན། དེ་ནི་འདི་སྐད་དུ་འཇིག་ཚོགས་ལ་ལྟ་བ་མ་འོངས་པ་དང་མཚུངས་པར་ལྡན་པའི་སྡུག་བསྔལ་གྱི་བདེན་པ་མ་གཏོགས་པ་ཞེས་བརྗོད་པར་བྱ་བའམ། ཡང་ན་དོན་གྱིས་ན་དེ་ལྟར་གོ་བར་བྱའོ། །

[Block 1914]
འོ་ན་བཏགས་པའི་བཤད་པ་ཆོས་ཐམས་ཅད་ནི་བཞི་ཚན་དུ་ངེས་པ་ཡིན་ཏེ། རྒྱུ་དང་འབྲས་བུ་དང་། རྟེན་དང་དམིགས་པར་ངེས་སོ༌[^958]ཞེས་བྱ་བ་འདི་ཇི་ལྟར་དང་།[^959] འདིར་རྒྱུ་ནི་མཚུངས་པར་ལྡན་པའི་རྒྱུ་དང༌[^960]ལྷན་ཅིག་འབྱུང་བའི་རྒྱུ་ཡིན་ནོ། །

[Block 1915]
འབྲས་བུ་ནི་སྐྱེས་བུ་བྱེད་པའི་འབྲས་བུ་དང་། བདག་པོའི་འབྲས་བུ་ཡིན་ནོ། །

[Block 1916]
རྟེན་ནི་མིག་ལ་སོགས་པའོ། །

[Block 1917]
དམིགས་པ་ནི་གཟུགས་ལ་སོགས་པ་ཡིན་ནོ་ཞེས་བྱ་བར་བལྟ་བར་བྱའོ། །

[Block 1918]
དེ་ལྟ༌[^961]ན་སྐལ་བ་མཉམ་པའི་རྒྱུ་མ་ཡིན་པ་ལས་རྒྱུ་ཡིན་པར་འགྱུར་བ་མ་ཡིན་ནམ། གནས་སྐབས་ནི་འདོད་པ་ཁོ་ན་ཡིན་གྱི་རྫས་ལ་ནི་མ་ཡིན་ཏེ། ཚོགས་པ་ནི་གནས་སྐབས་ཀྱི་འབྲས་བུ་ཅན་ཡིན་གྱི། རྫས་ཀྱི་འབྲས་བུ་ཅན་ནི་མ་ཡིན་ནོ། །

[Block 1919]
གལ་ཏེ་རྣམ་པར་སྨིན་པའི་རྒྱུ་བཞིན་དུ་སྐལ་བ་མཉམ་པའི་རྒྱུ་ཡང་མ་འོངས་པ་ཡིན་ན་ཅིར་འགྱུར་ཞེ་ན། བསྟན་བཅོས་ལས་དེ་སྨོས་པར་འགྱུར་རོ། །

[Block 1920]
འབྲས་བུ་འབྱིན་པ༌[^962]དང་འཛིན་པར་བྱེད་ནུས་པ་གང་ཡིན་པ་དེ་ཁོ་ན་སྨོས་པའི་ཕྱིར་ཉེས་པ་མེད་དོ་ཞེ་ན། དེ་ནི་མ་ཡིན་ཏེ། སྐལ་བ་མཉམ་པའི་རྒྱུ་ནི་རྒྱུ་མཐུན་པའི་འབྲས་བུས་འབྲས་བུ་དང་བཅས་པ་ཡིན་ན་དེ་ཡང་མ་འོངས་པ་ལ་རིགས་པ་མ་ཡིན་ཏེ། སྔ་ཕྱི་མེད་པའི་ཕྱིར་རོ། །

[Block 1921]
བྱུང་ཟིན་པ་ཡང་མ་འོངས་པའི་རྒྱུ་མཐུན་པར་མི་རུང་སྟེ། དཔེར་ན་ད་ལྟའི་འདས་པ་བཞིན་ནོ། །

[Block 1922]
རྒྱུ་བས་འབྲས་བུ་སྔ་ན་མི་རུང་བས་སྐལ་བ་མཉམ་པའི་རྒྱུ་མ་འོངས་པ་ནི་མེད་དོ། །

[Block 1923]
དེ་ལྟ་ན་རྣམ་པར་སྨིན་པའི་རྒྱུ་ཡང་མ་འོངས་པ་ཡིན་པར་མི་འགྱུར་ཏེ། རྣམ་པར་སྨིན་པའི་འབྲས་བུ་སྔ་བ་དང་ལྷན་ཅིག་པ་མི་རུང་བའི་ཕྱིར་ལ། མ་འོངས་པའི་དུས་ལ་ཡང་སྔ་ཕྱི་མེད་པའི་ཕྱིར་རོ་ཞེ་ན། དེ་ནི་མ་ཡིན་ཏེ། སྐལ་བ་མཉམ་པའི་རྒྱུ་ནི་སྔ་ཕྱི་མེད་པར་འདྲ་བའི་སྐལ་བ་མཉམ་པའི་རྒྱུ་འདྲ་བ་ཡིན་པས་ཕན་ཚུན་དུ་རྒྱུར་གྱུར་པའི་ཕྱིར་ཕན་ཚུན་རྒྱུ༌[^963]མཐུན་པ་ཉིད་དུ་ཐལ་བར་འགྱུར་ཏེ། ཕན་ཚུན་རྒྱུ་མཐུན་པ་ཉིད་དུ་ནི༌[^964]རིགས་པ་དང་ལྡན་པ་མ་ཡིན་ནོ། །

[Block 1924]
རྣམ་པར་སྨིན་པའི་རྒྱུ་ནི་སྔ་ཕྱི་མེད་བཞིན་དུ་ཡང་དེ་ལྟར་ཕན་ཚུན་འབྲས་བུ་ཉིད་དུ་ཐལ་བར་མི་འགྱུར་ཏེ། རྒྱུ་དང་འབྲས་བུ་དག་མཚན་ཉིད་ཐ་དད་པའི་ཕྱིར་རོ། །

[Block 1925]
དེ་ལྟ་བས་ན་སྐལ་བ་མཉམ་པའི་རྒྱུ་ནི་གནས་སྐབས་ལས་རྣམ་པར་གནས་པ་ཁོ་ན་ཡིན་ལ། རྣམ་པར་སྨིན་པའི་རྒྱུ་ནི་མཚན་ཉིད་ལས་རྣམ་པར་གནས་པ་ཡིན་པས་མ་འོངས་པ་ཡང་མི་བཟློག་གོ། །

[Block 1926]
སྐལ་བ་མཉམ་པའི་རྒྱུ་ནི་རང་གི་ས་པ་ཡིན་ནོ་ཞེས་བཤད་པ་གང་ཡིན་པ་ཅི་དེ་ལྟར་ངེས་སམ་ཞེ་ན། དེ་ཟག་པ་དང་བཅས་པ་ལ་ནི་ངེས་སོ། །

[Block 1927 [VERSE]]
ས་དགུའི་ལམ་ནི་ཕན་ཚུན་དུ། །
སྐལ་བ་མཉམ་པའི་རྒྱུ་ཡིན་ནོ། །

[Block 1928]
ཞེས་བྱ་བར་སྐབས་དང་སྦྱར་ཏེ། མི་ལྕོགས་པ་མེད་པ་དང་བསམ་གཏན་ཁྱད་པར་ཅན་དང་། བསམ་གཏན་བཞི་དང་། གཟུགས་མེད་པ་གསུམ་དག་གི་ལམ་གྱི་བདེན་པ་ནི་ཕན་ཚུན་དུ་སྐལ་བ་མཉམ་པའི་རྒྱུ་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན། འདི་ནི་ས་དེ་དག་ཏུ་གློ་བུར་དུ་འོངས་པ་ཡིན་ལ། ས་དེ་པ་དག་གིས༌[^965]བདག་གིར་མ་བྱས་པའི་ཕྱིར་ཁམས་དེ་དག་ཏུ་གཏོགས་པ་མ་ཡིན་ཏེ། དེ་བས་ན་ས་གཞན་པའི་རིགས་མཐུན་པའི༌[^966]སྐལ་བ་མཉམ་པའི་རྒྱུ་ཡང་ཡིན་ནོ། །

[Block 1929]
དེ་ཡང་།

[Block 1930 [VERSE]]
མཉམ་དང་ཁྱད་པར་ཅན་གྱི་ཡིན། །
ཆུང་ངུའི༌[^967]རྒྱུ་ནི་མ་ཡིན་ཏེ། །
--- END BLOCKS ---
