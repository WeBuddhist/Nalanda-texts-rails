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
[Block 4866]
ཡི་གེ་ཨ་བརྗོད་པའི་དུས་སུ་རླུང་ནི་བར་ན་གནས་པ་མཚོན་པར་འགྱུར་ཏེ། རླུང་དང་ཡི་གེ་ཐ་མི་དད་པའི་ཕྱིར་རོ། །

[Block 4867]
དེ་ལ་རླུང་རྒྱུ་བས་ཡི་གེ་རྣམས་འབྱུང་བ་ཡིན་ཏེ། ཡི་གེ་བརྗོད་པའི་དུས་སུ་རླུང་ཉིད་ཀྱིས་རྩོལ་བར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 4868]
དེ་བས་ན་བྱ་བ་དང་བྱེད་པའི་འབྲེལ་པའམ་ཕན་གདགས་པར་བྱ་བ་དང་ཕན་འདོགས་པར་བྱེད་པའི་འབྲེལ་པས་རླུང་དང་ཡི་གེ་དབྱེར་མེད་པ་ཡིན་ནོ། །

[Block 4869]
རླུང་གི་ལས་ཀྱི་བདག་ཉིད་ཀྱི་འཇུག་པ་ལ་སོགས་པའི་བྱ་བ་ནི་རླུང་དང་དེའི་བདག་ཉིད་དུ་འཇུག་པས་རླུང་ལས་ཐ་དད་པ་མ་ཡིན་ཏེ། འགྲོ་བ་དང་བསྐུམ་པ་དང་བརྐྱང་བའི་མཚན་ཉིད་དེ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4870]
ཇི་སྐད་དུ། ཡི་གེ་ཨོཾ་གྱི་དབུགས་ནི་ནང་དུ་འཇུག་པ་དང་། ཡི་གེ་ཨའི་སྔགས་ནི་བར་དུ་གནས་པ་དང་། ཡི་གེ་ཧཱུྃ་གི་སྔགས་ནི་ལྡང་བར༌[^2895]གྱུར་པ་སྟེ། རྐན་དང་མཆུ་དག་འབྲེལ་མེད་གསང་སྔགས་བཟླ། །ཞེས་འབྱུང་ངོ་། །

[Block 4871]
དེར་ནི་འགྲོ་བ་དང་འོང་བ་དང་བར་དུ་གནས་པའི་འཇུག་པ་དང་གནས་པ་དང་ལྡང་བ་དེ་རྣམ་པ་གསུམ་གྱིས་བཟླས་པས་ན་ཞེས་པ་ནི་ཡན་ལག་མ་ཉམས་པའི་བཟླས་པས་རྡོ་རྗེ་འཆང་ཆེན་པོ་ལ་སོགས་པའི་རྣམ་པ་བཅུ་གཅིག་པའི་རྡོ་རྗེ་བཟླས་པ་ཏིང་ངེ་འཛིན་གང་གིས་བྱེད་པ་དེ་ལ་དེ་སྐད་ཅེས་བཤད་དོ། །

[Block 4872]
ཡན་ལག་མ་ཉམས་པའི་བཟླས་པ་ནི་སྔགས་དང་རླུང་དང་ལྷའི་རྣམ་པར་དག་པའི་ངོ་བོ་ཡེ་ཤེས་གསུམ་དང་ཁམས་གསུམ་དང་རྩ་གསུམ་དང་དེ་ཁོ་ན་ཉིད་གསུམ་དང་རྣམ་པར་ཐར་པའི་སྒོ་གསུམ་དང་སྐུ་གསུང་ཐུགས་དང་སྐུ་གསུམ་དང་རྫས་གསུམ་དང་སྲིད་པ་གསུམ་དང་འཇིག་རྟེན་གསུམ་ལ་སོགས་པ་གཅིག་ཏུ་བྱས་པའི་ཡིད་ལ་བྱེད་པའི་མོས་པས་རྡོ་རྗེ་ཚིག་གིས་སེམས་རྩེ་གཅིག་པ་ཐོབ་པའི་བར་དུ་རྡོ་རྗེ་བཟླས་པ་བྱ་བ་ཡིན་གྱི། ཕྱི་རོལ་གྱི་བཟླས་པ་བརྗོད་པའམ་ཐོས་པ༌[^2896]ངག་གི་བཟླས་པའི་རང་བཞིན་བརྟག་པར༌[^2897]བྱ་བ་མ་ཡིན་ནོ། །

[Block 4873 [VERSE]]
རྐན་དང་མཆུ་དང་ལྕེ་སོགས་ཀྱི། །
གང་ཞིག་གཡོ་བར་གྱུར་པ་ནི། །
དེ་ཉིད་མི་འགྱུར་ག་ལས་ཏེ། །
འགྱུར་བ་ཉིད་དུ་གནས་པའི་ཕྱིར། །

[Block 4874]
ཞེས་ཀམ་པ་ལའི་ཞལ་སྔ་ནས་ཀྱིས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 4875]
དེ་བཞིན་དུ།

[Block 4876 [VERSE]]
ཡི་གེ་རང་བཞིན་སྔགས་རྣམས་ནི། །
དེ་ཉིད་ཀྱི་ཕྱིར་མི་འཐད་དེ། །
གང་ཕྱིར་རྩྭ་མཆོག་ཙམ་ཉིད་ནི། །
འགུགས་པར་བྱེད་པར་མི་ནུས་སོ། །

[Block 4877]
ཞེས་གསུངས་སོ། །

[Block 4878]
རབ་ཏུ་བྱེད་པ་ལས་ཀྱང་།

[Block 4879 [VERSE]]
དེ་ཡི་བརྟུལ་ཞུགས་མ་བཤད་ཅིང་། །
བགྲང་ཕྲེང་མ་ཡིན་འདས་པ༌[^2898]མིན། །
འཛིན་དང་སྦྱིན་སྲེག༌[^2899]ལས་རྣམས་ནི། །
ཡང་དང་ཡང་དུ་འཇུག་པ་མིན། །

[Block 4880]
ཞེས་འབྱུང་ངོ་། །རྩ་བའི་རྒྱུད་ལས་ཀྱང་། །

[Block 4881 [VERSE]]
སློང་མོ་ཟ་ཞིང་མི་བཟླ་སྟེ། །
མ་བླངས་པ་ལ་འང་ཆགས་མི་བྱ། །
ཐབས་དང་ཤེས་རབ་ལ་གནས་པས། །
ཡན་ལག་མ་ཉམས་གསང་སྔགས་བཟླས། །

[Block 4882 [VERSE]]
དེ་བཞིན་དུ་དེ་ཉིད་ལས་ཀྱང་། །
དོན་རྟོགས་པ་ཡིས༌[^2900]བཟླས་པ་ནི། །
ངོ་བོ་ཉིད་མེད་མཛེས་པ་སྟེ། །

[Block 4883]
དུས་གསུམ་སངས་རྒྱས་རྣམ་དཔྱོད་པས། དེ་ནི་རྡོ་རྗེ་བཟླས་པར་བཤད། ཅེས་གསུངས་སོ། །

[Block 4884]
དེ་ལྟ་བུ༌[^2901]ཏིང་ངེ་འཛིན་ཞེས་པ་ནི་རླུང་གི་དེ་ཁོ་ན་ཉིད་དང་སྔགས་ཀྱི་དེ་ཁོ་ན་ཉིད་རྗེས་སུ་རྟོགས་པ་སྔོན་དུ་འགྲོ་བར་རྡོ་རྗེ་བཟླས་པའི་མཚན་ཉིད་ཅན་གྱི་སེམས་རྩེ་གཅིག་པ་ཉིད་དོ། །

[Block 4885]
གང་ཡིན་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱ་སྟེ་ཞེས་པ་ལ། བརྗོད་པར་བྱ་བའི་སྒོ་ནས་ལེའུ་གང་དུ་ཡོད་པ་ཞེས་ཚིག་གི་དོན་ཏོ། །

[Block 4886]
དོན་འདི་ཉིད་ནི་ཞེས་པ་ནི་གཙོ་བོར་གྱུར་པའི་དང་པོ་རྡོ་རྗེ་བཟླས་པ་དང་། དེའི་འོག་ཏུ་སེམས་རྣམ་པར་དག་པ་ལ་སོགས་པའི་རིམ་པ་གཞན་རྣམས་ཀྱང་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 4887]
ཨོཾ་ནི་དང་པོ་གཅིག་དང་ལྡན་པ་ཞེས་པ་ནི་བཅོམ་ལྡན་འདས་རྣམ་པར་སྣང་མཛད་དེ། དེའི་ཡི་གེ་འབྲུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4888]
ཤཱུ་ནྱ་ཏཱ་ནི་གཉིས་པ་སྟེ་ཞེས་པ་ནི་ནམ་མཁའི་དབྱིངས་ནི་སྟོང་པ་ཉིད་དེ་དེའི་རང་བཞིན་ནི་རིན་ཆེན་འབྱུང་ལྡན་ཏེ་གཉིས་པའོ། །

[Block 4889]
ཛྙཱ་ན་ཞེས་པ་གསུམ་པ་ཉིད་ཅེས་པ་ནི་མཁྱེན་པས་ན་ཡེ་ཤེས་སོ། །

[Block 4890]
དེ་བས༌[^2902]ན་དངོས་པོ་ཐམས་ཅད་སོ་སོར་རྟོག་པའི་ཡེ་ཤེས་ཀྱི་བདག་ཉིད་ནི་བཅོམ་ལྡན་འདས་སྣང་བ་མཐའ་ཡས་ཏེ་གསུམ་པའོ། །

[Block 4891]
བཛྲ་ཞེས་བྱ་བ་ནི་བཞི་པའོ་ཞེས་པ་ནི་རྡོ་རྗེ་ལྟར་མི་ཕྱེད་པའི་ཆོས་ཀྱི་དབྱིངས་ཀྱི་ཡེ་ཤེས་ཀྱི་རང་བཞིན་ནི་བཞི་པ་སྟེ་མི་བསྐྱོད་པའོ། །

[Block 4892]
སྭ་བྷཱ་བ་ཨཱཏྨ་ཀོ྅་ལྔ་པ་ཞེས་པ་ནི་བྱ་བ་ནན་ཏན་གྲུབ་པའི་ཡེ་ཤེས་ཀྱི་རང་བཞིན་ནམ། རླུང་གི་ཁམས་ཀྱི་རང་བཞིན་ཏེ།

[Block 4893 [VERSE]]
ལྔ་པ་དེ་དོན་ཡོད་གྲུབ་པའོ། །
ཨ་ཧཾ་ཞེས་པ་དྲུག་པར་བརྗོད། །

[Block 4894]
ཅེས་པ་ནི་དེ་བཞིན་གཤེགས་པ་ལྔ་སྡུད་པར་བྱེད་པ་ཐམས་ཅད་གཅིག་གི་བདག་ཉིད་ཅན་རྡོ་རྗེ་འཆང་ཆེན་པོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4895]
དེ་ལྟར་བདེ་གཤེགས་དྲུག་པོ་ནི། །རྣམ་པར་སྣང་མཛད་ལ་སོགས་པ་དྲུག་པོ་རྫོགས་པའི་རིམ་པ་སྒོམ་པར་བྱེད་པའི་རིན་པོ་ཆེ་ལྟ་བུའི་གང་ཟག་ལ་བསྟན་ཏོ། །

[Block 4896]
དེས་ན་དོན་འདི་ཡིན་ཏེ། རྡོ་རྗེ་བཟླས་པ་བསྒོམ་པར་བྱ་བར་འདོད་པའི་རྣལ་འབྱོར་པས་དང་པོར་ཅིག་ཅར་དུ་ལྷའི་སྐུ་བསྐྱེད་ཅིང་དེ་བཞིན་གཤེགས་པ་དྲུག་གི་རང་བཞིན་བསྒོམས་ལ། དེ་ནས་རྣམ་པ་བཅུ་གཅིག་བཟླས་པར་བྱའོ། །

[Block 4897]
ཡང་ན་སྒྲ་ཇི་བཞིན་མ་ཡིན་པ༌[^2903]བཤད་པའི་རིམ་པས་ཡི་གེ་དྲུག་གིས༌[^2904]མཚོན་པའི་རྣམ་པར་སྣང་མཛད་ལ་སོགས་པ་དྲུག་གི་རྣལ་འབྱོར་པས་ཟླ་བ་གཅིག་གིས་འབུམ་ཕྲག་དྲུག་བཟླས་པར་བྱའོ། །

[Block 4898]
དེ་ལ་ཉིན་མཚན་གཅིག་གིས་ཉི་ཁྲི་ཆིག་སྟོང་དྲུག་བརྒྱར་འགྱུར། ཞག་ལྔས་འབུམ་ཕྲག་གཅིག་དང་སྟོང་རྩ་བརྒྱད་ནི་འབུམ་ཕྲག་གཅིག་ཅེས་བསྟན་པ་ཡིན་ནོ། །

[Block 4899]
གྲངས་འདི་ཉིད་ཀྱིས་མདོར་ན་ཟླ་བ་གཅིག་གིས་འབུམ་ཕྲག་དྲུག་ཏུ་འགྱུར་རོ། །

[Block 4900]
ཇི་སྐད་དུ།

[Block 4901 [VERSE]]
སྔགས་ནི་རྣམ་ཤེས་ལས་འབྱུང་བའི། །
འབུམ་ཕྲག་དྲུག་ཏུ་བཟླས་བྱས་ཏེ། །
རྡོ་རྗེ་སེམས་ལ་ཕྱག་འཚལ་ནས། །
དེ་ནི་ཉ་ལ་འགྲུབ་པར་འགྱུར། །

[Block 4902]
ཞེས་འབྱུང་ངོ་། །རྣམ་པ་གཞན་གྱིས་ཀྱང་རྡོ་རྗེ་བཟླས་པ་བསྟན་པའི་ཕྱིར། ཨོཾ་ཤཱུ་ནྱ་ཏཱ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། ཟུང་ནི་ཚིག་གཉིས་སོ། །

[Block 4903]
དང་པོ་རྣམ་པར་སྣང་མཛད་དོ། །

[Block 4904]
ཛྙཱ་ན་བཛྲ་གཉིས་པོ་ཞེས་པ་ནི་སྣང་བ་མཐའ་ཡས་སོ། །

[Block 4905]
སྭ་བྷཱ་བ་ཨཱཏྨ་ཀོ྅ཧཾ་གྱུར་ཞེས་པ་ནི་ཚིག་གཉིས་ཀྱིས་མི་བསྐྱོད་པ་བསྟན་ཏོ། །
--- END BLOCKS ---
