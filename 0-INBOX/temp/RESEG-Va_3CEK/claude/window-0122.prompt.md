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
[Block 4271]
ལྷག་མ་རྣམས་ནི་ཡན་ལག་དག་ཡིན་ནོ་ཞེས་གྲག་གོ། །

[Block 4272]
ཡན་ལག་བཞི་པའི་དམག་ཇི་ལྟ་བར་ཡན་ལག་ལྔའི་བསམ་གཏན་ཡང་དེ་དང་འདྲའོ། །

[Block 4273 [HEADING]]
##### བསམ་གཏན་གཉིས་པ་ལ་ཡན་ལག་བཞི། ^5-1-6-2-0

[Block 4274]
གཉིས་པ་ལ་ནི་ཡན་ལག་བཞི། རབ་དང་དད་ནི་དགའ་ལ་སོགས། །བསམ་གཏན་གཉིས་པ་ལ་ཡན་ལག་བཞི་སྟེ། ནང་རབ་ཏུ་དང་བ་དང་། དགའ་བ་དང་། བདེ་བ་དང་།

[Block 4275]
སེམས་རྩེ་གཅིག་པ་ཉིད་དོ། །

[Block 4276 [HEADING]]
##### བསམ་གཏན་གསུམ་པ་ལ་ཡན་ལག་ལྔ། ^5-1-6-3-0

[Block 4277 [VERSE]]
གསུམ་པ་ལ་ལྔ་བཏང་སྙོམས་དང་། །
དྲན་དང་ཤེས་རབ་བདེ་དང་གནས། །

[Block 4278]
བསམ་གཏན་གསུམ་པ་ལ་ཡང་ཡན་ལག་ལྔ་སྟེ། བཏང་སྙོམས་དང་། དྲན་པ་དང་། ཤེས་བཞིན་དང་བདེན་པ་དང་། ཏིང་ངེ་འཛིན་ཏོ། །

[Block 4279]
གནས་པ་ནི་ཏིང་ངེ་འཛིན་གྱི་རྣམ་གྲངས་ཡིན་ཏེ།

[Block 4280]
མདོ་ལས།

[Block 4281]
ཡང་དག་པའི་ཏིང་ངེ་འཛིན་གང་ཞེ་ན། གང་སེམས་གནས་པ་དང་། ཡང་དག་པར་གནས་པའོ་ཞེས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 4282 [HEADING]]
##### བསམ་གཏན་བཞི་པ་ལ་ཡན་ལག་བཞི། ^5-1-6-4-0

[Block 4283 [VERSE]]
མཐའ་ན་བཞི་དྲན་བཏང་སྙོམས་དང་། །
བདེ་མིན་སྡུག་མིན་ཏིང་འཛིན་རྣམས། །
མཐའ་མ་ནི་བསམ་གཏན་བཞི་པའོ། །

[Block 4284]
དེ་ལ་ཡན་ལག་བཞི་སྟེ། བདེ་བ་ཡང་མ་ཡིན་སྡུག་བསྔལ༌[^3080]ཡང་མ་ཡིན་པའི་ཚོར་བ་དང་། བཏང་སྙོམས་ཡོངས་སུ་དག་པ་དང་། དྲན་པ་ཡོངས་སུ་དག་པ་དང་། ཏིང་འཛིན༌[^3081]ཡོངས་སུ་དག་པའོ། །

[Block 4285 [HEADING]]
##### བསམ་གཏན་གྱི་ཡན་ལག་བཅོ་བརྒྱད། ^5-1-6-5-0

[Block 4286]
དེ་དག་ནི་བསམ་གཏན་གྱི་ཡན་ལག་བཅོ་བརྒྱད་ཡིན་ཏེ།

[Block 4287]
དང་པོ་དང་གསུམ་པ་དག་ལ༌[^3082]ནི་ཡན་ལག་ལྔ་ཡིན་པའི་ཕྱིར་དང་།[^3083]

[Block 4288]
གཉིས་པ་དང་བཞི་པ་དག་ལ་ནི་ཡན་ལག་བཞི་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4289]
མིང་གི་སྒོ་ནས་ནི་དེ་ལྟའོ། །

[Block 4290 [HEADING]]
##### རྫས་སུ་བཅུ་གཅིག། ^5-1-6-6-0

[Block 4291]
རྫས་སུ་བཅུ་གཅིག །རྫས་སུ་ནི་དེ་དག་བཅུ་གཅིག་ཡིན་ཏེ། བསམ་གཏན་དང་པོ་ལ་ལྔའོ། །

[Block 4292]
གཉིས་པ་ལ་ནི་ནང༌[^3084]རབ་ཏུ་དང་བ་ལྷག་གོ། །

[Block 4293]
གསུམ་པ་ལ་ནི་བཏང་སྙོམས་དང་། དྲན་པ་དང་། ཤེས་བཞིན་དང་། བདེ་བ་རྣམས་སོ། །

[Block 4294]
བཞི་པ་ལ་བདེ་བ་ཡང་མ་ཡིན་སྡུག་བསྔལ༌[^3085]ཡང་མ་ཡིན་པའི་ཚོར་བའོ། །

[Block 4295]
དེ་ཉིད་ཀྱི་ཕྱིར་སྨྲས་པ། ཡན་ལག་གང་དག་བསམ་གཏན་དང་པོ་ན་ཡོད་པ་དེ་དག་གཉིས་པ་ན་ཡང་ཡོད་དམ་ཞེ་ན། མུ་བཞི་སྟེ། མུ་དང་པོ་ནི་རྟོག་པ་དང་། དཔྱོད་པ་དག་གོ། །

[Block 4296]
གཉིས་པ་ནི་ནང་རབ་ཏུ་དང་བའོ། །

[Block 4297]
གསུམ་པ་ནི་དགའ་བ་དང་བདེ་བ་དང༌[^3086]སེམས་རྩེ་གཅིག་པ་ཉིད་དོ། །

[Block 4298]
མུ་བཞི་པ་ནི་བཤད་པ་ལས་མ༌[^3087]གཏོགས་པའི་ཆོས་རྣམས་སོ༌[^3088]ཞེས་བྱའོ། །

[Block 4299]
དེ་བཞིན་དུ་བསམ་གཏན་གྱི་ཡན་ལག་ཐམས་ཅད་ཕན་ཚུན་དུ༌[^3089]སྦྱར་བར་བྱའོ། །

[Block 4300 [HEADING]]
###### བསམ་གཏན་གསུམ་པ་ན་ཡོད་པའི་བདེ་བ། ^5-1-6-6-1-0

[Block 4301]
ཅིའི་ཕྱིར་བསམ་གཏན་གསུམ་པ་ན་ཡོད་པའི་བདེ་བ་རྫས་གཞན་དུ་བརྗོད་ཅེ་ན། འདི་ལྟར་དེའི་བདེ་བ་ནི་ཚོར་བ་ཡིན་ལ། བསམ་གཏན་དང༌[^3090]པོ་ན། ཤིན་ཏུ་སྦྱངས་པ་བདེ་བ་ཡིན། བསམ་གཏན་དང་པོ༌[^3091]དག་ན་ནི་ཤིན་ཏུ་སྦྱངས་པ་ལ་བདེ་བ་ཞེས་བཤད་དོ། །

[Block 4302]
འདི་ལ་ནི་ཤིན་ཏུ་སྦྱངས་པ་བདེ་བ་ཡིན་ལ། དེ་ལ་ནི་ཚོར་བ་བདེ་བ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་ག་ལས་ཤེས་ཤེ་ན། སྙོམས་པར་འཇུག་པའི་བསམ་གཏན་གཉིས་ན་བདེ་བའི་དབང་པོ་དང་མི་ལྡན་པའི་ཕྱིར་ཏེ། དེ་གཉིས་ན་དེ་ལུས་ཀྱི་ཡིན་པར་ནི་མི་རུང་སྟེ། སྙོམས་པར་ཞུགས་པ་ལ་རྣམ་པར་ཤེས་པའི་ཚོགས་ལྔ་མེད་པའི་ཕྱིར་རོ། །

[Block 4303]
སེམས་ལས་བྱུང་བ་ཡང་མ་ཡིན་ཏེ། དགའ་བ་ཞེས་འབྱུང་བའི༌[^3092]ཕྱིར་རོ། །

[Block 4304]
དགའ་བ་ནི་ཡིད་བདེ་བ་ཡིན་ན། བདེ་བ་དང་། ཡིད་བདེ་བ་གཉིས་ཅིག་ཅར་འབྱུང་བ་མེད་དོ། །

[Block 4305]
དེ་གཉིས་རྣམ་གྲངས་ཀྱིས༌[^3093]བསམ་གཏན་ན་ཡོད་པར་ཡང་རིགས་པ༌[^3094]མ་ཡིན་ཏེ། ཡན་ལག་ལྔ་ཞེས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 4306]
གཞན་དག་ན་རེ་སེམས་ལས་བྱུང་བའི་བདེ་བའི་དབང་པོ་ནི༌[^3095]ཁོ་ན་སྟེ། བསམ་གཏན་གསུམ་ཆར་ན་ཡང་ལུས་ཀྱི་བདེ་བ་ཁོ་ན་ཡན་ལག་ཏུ་རྣམ་པར་གཞག་གོ་ཞེས་ཟེར་རོ། །

[Block 4307]
འོ་ན་མདོ་ལས།

[Block 4308]
བདེ་བའི་དབང་པོ་གང་ཞེ་ན་བདེ་བ་མྱོང་བར་འགྱུར་བའི་རེག་པས་རེག་པ་ན་ལུས་ཀྱི་དང་སེམས་ལས་བྱུང་བའི་ཚོར་བའི་རྣམ་པ༌[^3096]བདེ་བ་སིམ་པ་སྐྱེ་བ་གང་ཡིན་པ་དེ་ནི་བདེ་བའི་དབང་པོ་ཞེས་བྱའོ་ཞེས་གང༌[^3097]གསུངས་པ་ཇི་ལྟ་བུ་ཞེ་ན། ཚིག་དེ་ནི་འགའ་ཞིག་གིས༌[^3098]སྒྲོ་བཏགས་པ་ཡིན་ཏེ། སྡེ་པ་གཞན་ཐམས་ཅད་ལས་ལུས་ཀྱི་ཞེས་བྱ་བ་ཁོ་ན་འབྱུང་བའི་ཕྱིར་དང་། བདེ་བ་ལུས་ཀྱིས་མྱོང་ལ་ཞེས་རང་གི་སྒྲས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 4309]
གལ་ཏེ་ཡིད་ཀྱི་ལུས་ཀྱིས་སོ་ཞེ་ན་ནི། དེ་སྐད་བཤད་པ་ལ་ཡོན་ཏན་ཅི་ཞིག་ཡོད། བསམ་གཏན་བཞི་པ་ལ་ཤིན་ཏུ་སྦྱངས་པ་མང་བཞིན་དུ་བདེ་བ་མ་སྨོས་པའི་ཡང་ཕྱིར་རོ། །

[Block 4310]
གལ་ཏེ་བདེ་བའི་ཚོར་བ་དང་མཐུན་པའི་ཤིན་ཏུ་སྦྱངས་པ་བདེ་བ་ཡིན་ནོ་ཞེ་ན་ནི།
--- END BLOCKS ---
