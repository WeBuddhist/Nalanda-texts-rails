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
[Block 4166]
[^2997]ཤེས་པའི་སྐབས་ཀྱིས་ཤེས་པའི་རང་བཞིན་གྱི་ཡོན་ཏན་རྣམས་ནི༌[^2998]བཤད་ཟིན་ཏོ།། །།

[Block 4167 [HEADING]]
### བསམ་གཏན་རྣམས། ^5-1-0

[Block 4168 [HEADING]]
#### བསམ་གཏན་རྣམ་པ་གཉིས། ^5-1-1-0

[Block 4169]
རང་བཞིན་གཞན་རྣམས་བརྗོད་པར་བྱ་སྟེ། དེ་ལྟ་བས་ན་ཡོན་ཏན་ཐམས་ཅད་ཀྱི་རྟེན་ཡིན་པའི་ཕྱིར་དང་པོ་ཁོ་ནར་བསམ་གཏན་རྣམས་བརྩམས་ཏེ། བསམ་གཏན་དག་ནི་རྣམ་པ་གཉིས། །བསམ་གཏན་རྣམས་ནི་མདོར་བསྡུ་ན་སྐྱེ་བ་དང་སྙོམས་པར་འཇུག་པའི་བསམ་གཏན་གྱི༌[^2999]བྱེ་བྲག་གིས་རྣམ་པ་གཉིས་སོ། །

[Block 4170]
དེ་དག་ཀྱང་བཞི། བསམ་གཏན་དང་པོ་ནས་བཞི་པའི་བར་རོ། །

[Block 4171 [HEADING]]
##### བསམ་གཏན་དུ་སྐྱེ་བ། ^5-1-1-1-0

[Block 4172]
དེ་ལ་བསམ་གཏན་དུ་སྐྱེ་བ་རྣམས་ནི་ཡང་མི་བརྗོད་དེ། [^3000]འཇིག་རྟེན་བསྟན་པའི་མཛོད་ཀྱི་གནས་སུ། དེར་སྐྱེ་བ༌[^3001]དག་རབ་ཏུ་བཤད། ཇི་སྐད་དུ་བཤད་ཅེ་ན། དེར་སོ་སོའི།

[Block 4173 [VERSE]]
བསམ་གཏན་ས་ནི་གསུམ་པ་ཡིན། །
བཞི་པ་ས་ནི་བརྒྱད་པ་ཡིན། །

[Block 4174]
ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 4175 [HEADING]]
##### སྙོམས་པར་འཇུག་པའི་བསམ་གཏན། ^5-1-1-2-0

[Block 4176]
སྙོམས་པར་འཇུག་པའི་བསམ་གཏན་བརྗོད་པར་བྱ་སྟེ། དེའི་ཕྱིར་སྨྲས་པ། སྙོམས་འཇུག་དགེ་བ་རྩེ་གཅིག་པ། བྱེ་བྲག་མེད་པར་དགེ་བའི་སེམས་རྩེ་གཅིག་པ་ནི་བསམ་གཏན་ཡིན་ཏེ། ཏིང་ངེ་འཛིན་གྱི་རང་བཞིན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4177]
རྗེས་འབྲང་བཅས་ན་ཕུང་པོ་ལྔ། །འཁོར་དང་བཅས་ན་ནི་ཕུང་པོ་ལྔའི་རང་བཞིན་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 4178]
རྩེ་གཅིག་པ་ཞེས་བྱ་བ་འདི་ཅི་ཞེ་ན། དམིགས་པ་གཅིག་པ་ཉིད་དོ། །

[Block 4179]
དེ་ལྟ་ན་ནི་འོ་ན་སེམས་དམིགས་པ་གཅིག་པ་དག་ཁོ་ན་ཏིང་ངེ་འཛིན་ཡིན་གྱི་ཆོས་གཞན་སེམས་ལས་བྱུང་བ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བར་འགྱུར་རོ་ཞེ་ན།[^3002] སེམས་རྣམས་ཁོ་ན་ཏིང་ངེ་འཛིན་མ་ཡིན་གྱི་གང་གིས་དེ་དག་རྩེ་གཅིག་པར་བྱེད་པའི་ཆོས་དེ་ཏིང་ངེ་འཛིན་ཡིན་ལ་དེ་ཉིད་རྩེ་གཅིག་པ་ཉིད་ཡིན་ནོ། །

[Block 4180]
སྐད་ཅིག་མ་ཡིན་པའི་ཕྱིར་སེམས༌[^3003]ཐམས་ཅད་རྩེ་གཅིག་པ་མ་ཡིན་ནམ། གལ་ཏེ་གཉིས་པ་དེ་ལས་རྣམ་པར་མི་གཡེང་བ་ཡིན་ནོ་ཞེ་ན་ནི། མཚུངས་པར་ལྡན་པ་ལ་ཏིང་ངེ་འཛིན་དོན་མེད་པ་ཡིན་ནོ། །

[Block 4181]
གང་ཁོ་ན་ལས་ཏིང་ངེ་འཛིན་ཡིན་པ་དེ་ཁོ་ན་ལས་སེམས་རྣམས་ཀྱི་དམིགས་པ་གཅིག་པ་ཉིད་དུ་ཡང་ཅིའི་ཕྱིར་མི་འདོད། ཏིང་ངེ་འཛིན་ས་མང་པོ་པ་ཡིན་པའི༌[^3004]ཕྱིར་སེམས༌[^3005]ཐམས་ཅད་རྩེ་གཅིག་པ་ཉིད་དུ་ཡང་ཐལ་བར་འགྱུར་རོ། །

[Block 4182]
མ་ཡིན་ཏེ། ཏིང་ངེ་འཛིན་སྟོབས་ཆུང་བའི་ཕྱིར་རོ། །

[Block 4183]
གཞན་དག་ན་རེ་སེམས་རྩེ་གཅིག་པ་དག་ཁོ་ན་ཏིང་ངེ་འཛིན་ཡིན་ཏེ།

[Block 4184]
འདི་ལྟར་མདོ་ལས།

[Block 4185]
ལྷག་པའི་སེམས་ཀྱི་བསླབ་པ་དང་། སེམས་ཡོངས་སུ་དག་པའི་གཙོ་བོ་ནི་བསམ་གཏན་བཞི་ཡིན་ནོ་ཞེས་གསུངས་སོ་ཞེས་ཟེར་རོ། །

[Block 4186]
བསམ་གཏན་ཞེས་བྱ་བའི་དོན་ཅི་ཞེ་ན། འདིས་སེམས་པར་བྱེད་པས་ན་བསམ་གཏན་ཏེ། སེམས་མཉམ་པར་བཞག་ན་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་རབ་ཏུ་ཤེས་པའི་ཕྱིར་རབ་ཏུ་ཤེས་པར་བྱེད་ཅེས༌[^3006]བྱ་བའི་ཐ་ཚིག་སྟེ། [^3007]སྐད་ཀྱི་བྱིངས༌[^3008]འདི་ནི་སེམས་པའི་དོན་ཡིན་ལ། སེམས་པ༌[^3009]ཡང་ཤེས་རབ་ཡིན་ནོ་ཞེས་གྲུབ་པའི་མཐའ་ལས་འབྱུང༌[^3010]ངོ་། །དེ་ལྟ་ན་ནི་འོ་ན་ཏིང་ངེ་འཛིན་ཐམས་ཅད་བསམ་གཏན༌[^3011]དུ་ཐལ་བར་འགྱུར་རོ་ཞེ་ན། མ་ཡིན་ཏེ། ཕུལ་དུ་ཕྱིན་པ་དང་ལྡན་པ་ལ་དེའི་མིང་དུ་བཏགས་པའི་ཕྱིར་ཉི་མ༌[^3012]བཞིན་ནོ། །

[Block 4187]
ཕུལ་དུ་ཕྱིན་པ་དང་ལྡན་པ་ཡང་གང་ཞེ་ན། ཏིང་ངེ་འཛིན་གང་ཡན་ལག་དང་ལྡན་པ་ཡིན་ཏེ། དེ་ནི༌[^3013]ཞི་གནས་དང་ལྷག་མཐོང་ཟུང་དུ་འབྲེལ་པར་ངང་གིས་འབྱུང་བའི་ཕྱིར་མཐོང་བའི་ཆོས་ལ་བདེ་བར་གནས་པ་དང་། ལམ་སླ་བ་ཞེས་གསུངས་པས་དེ་ནི་ཤིན་ཏུ་ཡང་སེམས་པར་བྱེད་དོ། །

[Block 4188]
ཉོན་མོངས་པ་ཅན་ཇི་ལྟར་བསམ་གཏན་ཡིན་ཞེ་ན། ལོག་པར་ངེས་པ་སེམས་པའི་ཕྱིར་རོ། །

[Block 4189]
ཧ་ཅང་ཐལ་བར་འགྱུར་རོ་ཞེ་ན། མ་ཡིན་ཏེ། དེ་དང་མཐུན་པ་ཁོ་ན་ལ་དེའི་མིང་དུ་བཏགས་པའི་ཕྱིར་ཏེ། ས་བོན་རུལ་པ་བཞིན་ནོ། །

[Block 4190]
བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་བསམ་གཏན་མི་དགེ་བ་དག་ཀྱང་གསུངས་སོ། །

[Block 4191 [HEADING]]
###### བསམ་གཏན་དང་པོ། ^5-1-1-2-1-0

[Block 4192]
ཡང་དགེ་བ་རྩེ་གཅིག་པ་བསམ་གཏན་དང་པོ་ནི༌[^3014]ཇི་ལྟ་བུ། བཞི་པའི་བར་ནི་ཇི་ལྟ་བུ་ཞེ་ན། རེ་ཞིག་དང་པོ་ནི། དཔྱོད༌[^3015]དང་དགའ་དང་བདེ་དང་ལྡན། །དགེ་བ་རྩེ་གཅིག་པ་བསམ་གཏན་དང་པོ་ནི་དཔྱོད་པ༌[^3016]དང་དགའ་བ་དང་བདེ་བ་དང༌[^3017]མཚུངས་པར་ལྡན་པ་ཡིན་ནོ། །

[Block 4193]
དཔྱོད་པ་སྨོས་པས་རྟོག་པ༌[^3018]ཡང་བཤད་པ་ཡིན་ཏེ། ལྷན་ཅིག་སྤྱོད་པའི་ཕྱིར་དུ་བ་དང་མེ་བཞིན་དུ། རྟོག་པ་མེད་པར་ནི་དགའ་བ་དང་བདེ་བ་དང་ལྡན་པའི་དཔྱོད་པ་མེད་དོ། །

[Block 4194 [HEADING]]
###### བསམ་གཏན་ལྷག་མ་གསུམ། ^5-1-1-2-2-0

[Block 4195]
བསམ་གཏན་ལྷག་མ་གསུམ་ནི། ཡན་ལག་ལྔ་ལྔ༌[^3019]སྤངས་པ་ཡིན། །དགེ་བ་རྩེ་གཅིག་པ་ཞེས་བྱ་བར་སྦྱར་ཏེ། བསམ་གཏན་གཉིས་པ་ནི་དཔྱོད་པ་སྤངས་ལ། དགའ་བ་དང་བདེ་བ་དང་ལྡན་པ་ཡིན་ནོ། །

[Block 4196]
གསུམ་པ་ནི་དཔྱོད་པ་དང་དགའ་བ་སྤངས་ལ་བདེ་བ་དང་ལྡན་པ་ཡིན་ནོ། །

[Block 4197]
བཞི་པ་ནི་དཔྱོད་པ་དང་། དགའ་བ་དང་བདེ་བ་སྤངས་པ་ཡིན་ནོ། །

[Block 4198 [HEADING]]
#### གཟུགས་མེད། ^5-1-2-0

[Block 4199]
བསམ་གཏན་རྣམས་ཇི་ལྟ་བ་དེ་བཞིན་དུ༌[^3020]གཟུགས་མེད། རྣམ་པ་གང་གིས་ཤེ་ན། དེ་དག་ཀྱང་སྐྱེ་བ་དང་སྙོམས་པར་འཇུག་པའི་སྒོ་ནས་རྣམ་པ་གཉིས་ཀྱང་ཡིན་ལ་བཞི་ཡང་ཡིན་ནོ། །

[Block 4200 [HEADING]]
##### གཟུགས་མེད་པའི་སྐྱེ་བ། ^5-1-2-1-0

[Block 4201]
དེ་དག་གི་ཡང་སྐྱེ་བ་རྣམས་ནི་བཤད་ཟིན་ཏོ། །

[Block 4202 [HEADING]]
##### སྙོམས་པར་འཇུག་པའི་གཟུགས་མེད་པ། ^5-1-2-2-0

[Block 4203]
སྙོམས་པར་འཇུག་པའི་གཟུགས་མེད་པ་རྣམས་ནི་བྱེ་བྲག་མེད་པར་དགེ་བའི་སེམས་རྩེ་གཅིག་པའི་རང་བཞིན་ཡིན་ནོ་ཞེས་བྱ་བའི་རྣམ་པ་དེས་བཤད་ཟིན་ཏོ། །

[Block 4204]
འཁོར་དང་བཅས་ན་ནི། ཕུང་པོ་བཞི་རྗེས་སུ་འབྲང་བའི་གཟུགས་མེད་པའི་ཕྱིར་རོ། །

[Block 4205]
འོག་མའི་ས༌[^3021]དབེན་ལས་སྐྱེས་པ། །བསམ་གཏན་བཞི་པ་ལས་དབེན་པ་ལས་སྐྱེས་པ་ནི་ནམ་མཁའ་མཐའ་ཡས༌[^3022]སྐྱེ་མཆེད་ཡིན་ནོ། །
--- END BLOCKS ---
