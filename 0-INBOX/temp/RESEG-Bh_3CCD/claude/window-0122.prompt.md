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
ཞེས་འབྱུང་ངོ་། །རྡོ་རྗེ་འཆང་ཆེན་པོས་གསུངས་ཏེ་ཞེས་བྱ་བ་ནི་སྡུད་པ་པོའི་ཚིག་གོ། །

[Block 4272]
མཐར་ཐུག་པ་ཞེས་བྱ་བ་ནི་འོད་གསལ་བ་ལ་འཇུག་པ་དང་ཟུང་དུ་འཇུག་པ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 4273]
དེ་ལྟར་ཡི་གེའི་དོན་གྱིས་བསྐྱེད་པའི་རིམ་པའི་ཡན་ལག་ཏུ་གྱུར་པའི་སྟོང་པ་ཉིད་ཀྱི་དེ་ཁོ་ན་ཉིད་བསྟན་པ་དང་། སྤྱིའི་དོན་གྱི་རྣམ་པར་ཐར་པའི་སྒོ་གསུམ་གྱི་སྒོམ་པས་མདོ་སྡེ་པ་ལ་སོགས་པའི་འགྱོད་པ་སེལ་བའི༌[^2626]མཚན་ཉིད་ཅན་གྱི་དོན་བསྟན་ཏོ། །

[Block 4274]
སྦས་པའི་དོན་གྱིས་སེམས་རྣམ་པར་དག་པ་དང་། བདག་ལ་བྱིན་གྱིས་བརླབ༌[^2627]པའི་རིམ་པ་དག་བསྟན་ཏོ། །

[Block 4275]
མཐར་ཐུག་པས་འོད་གསལ་བ་ལ་འཇུག་པ་དང་ཟུང་དུ་འཇུག་པའི་རིམ་པ་དག་བསྟན་ཏོ་ཞེས་རྡོ་རྗེ་འཆང་ཆེན་པོའི་ཚིགས་སུ་བཅད་པའི་བསྐྱེད་པའི༌[^2628]རིམ་པའི་ཕྱོགས་གཅིག་དང་རྡོ་རྗེ་བཟླས་པ་མ་གཏོགས་པའི་རྫོགས་པའི་རིམ་པ་ཡང་བསྟན་ཏོ། །

[Block 4276]
དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི༌[^2629]ཞེས་བྱ་བ་ལ་རྡོ་རྗེ་འཆང་ལྔའིའོ། །

[Block 4277]
རྣམ་པ་ཀུན་ནས་ཞེས་པ་ནི་སྐུ་གསུང་ཐུགས་ཀྱི་བྱ་བ་རྣམས་ཀྱིས་སོ། །

[Block 4278]
འོད་གསལ་བ་ཞེས་པ་ནི་དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱི་འོད་གསལ་བའི་ངོ་བོ་ཉིད་དེ་གཏན་ཚིགས་ནི་མི་འདའ་བའི་ཕྱིར་རོ། །

[Block 4279]
ཏིང་ངེ་འཛིན་དེ་ལ་དམིགས་པ་ཞེས་པ་ནི་ཕྱག་རྒྱ་དང་ཏིང་ངེ་འཛིན་གྱི་རིམ་པས་ཐོབ་པར་བྱ་བའི་མངོན་པར་བྱང་ཆུབ་པའི་ཏིང་ངེ་འཛིན་ཞེས༌[^2630]བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 4280]
སྣོད་དུ་གྱུར་པའི་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་བདག་དང་དབང་ཕྱུག་ལ་སོགས་པའི༌[^2631]དངོས་པོ་ཐམས་ཅད་དོ། །

[Block 4281]
ཐམས་ཅད་དང་བྲལ་བ་ནི་དེ་དག་དང་བྲལ་བའོ། །

[Block 4282]
དེ་ལ་བདག་ཅེས་བྱ་བ་སྔར་བཤད་པའི་རིགས་པས་མེད་དོ། །

[Block 4283]
དེ་ལ་རྟག་པ་ལ་སོགས་པའི་ཆོས་རྣམས་ག་ལས་འགྱུར།

[Block 4284 [VERSE]]
བདག་ཅེས་བྱ་བ་དངོས་པོ་མེད། །
བྱེད་པ་པོ་ཞེས་ག་ལས་བརྗོད། །
ཆོས་ཅན་ཡོད་ན་འཇིག་རྟེན་པས། །
ཆོས་ལ་བསམ་པ་རབ་ཏུ་འཇུག །

[Block 4285 [VERSE]]
ཕུང་པོ་བདག་མིན་དེར་དེ་མིན། །
དེ་ལ་དེ་མེད་དེ་མེད་མིན། །
མེ་ཤིང་བཞིན་དུ་འདྲེས་པ་མིན། །
དེ་ཕྱིར་བདག་ཅེས་ཇི་ལྟར་ཡོད། །

[Block 4286]
ཅེས་འབྱུང་ངོ་། །དེའི་དོན་འདི་ཡིན་ཏེ། བདག་ནི་ཕུང་པོ་ཡིན་ནོ་ཞེས་བརྗོད་པ་མི་རིགས་ཏེ་དེའི་བདག་ཉིད་ཀྱི་འབྲེལ་པས་ཕུང་པོ་བཞིན་དུ་བདག་དང་མི་རྟག་པར་འགྱུར་རོ། །

[Block 4287]
རིགས་པ་པ་རྣམས་ཀྱི་ཕྱོགས་ནི་བདག་ཅེས་བརྟན༌[^2632]པའོ། །

[Block 4288]
སྐྱོན་དེ་སེལ་བར་བྱ་བའི་ཕྱིར། །བདག་ལ་ཕུང་པོ་ཡོད་ཅེས་ཕྱོགས་འཛིན་ན། དེའི་ཚེ་རྟག་པ་དང་མི་རྟག་པ་དག་གི་གཞི་དང་གཞི་ཅན་གྱི་འབྲེལ་པར་མི་འགྱུར་རོ། །

[Block 4289 [VERSE]]
གཞི་དང་གཞི་ཅན་གྱི་འབྲེལ་པ་ནི། །
རྟག་དང་མི་རྟག་དག་གི་མེད། །

[Block 4290]
ཅེས་འབྱུང་ངོ་། །འོ་ན་གཞི་རྟག་པ་ཡིན་ན་གཞི་ཅན་རྣམས་མི་རྟག་པ་ཡིན་ནོ་ཞེས་འདོད་ཅེ༌[^2633]ན། སྨྲས་པ། གཞི་དང་གཞི་ཅན་གྱི་འབྲེལ་པ་ཉིད་དུ་མི་འགྱུར་རོ། །

[Block 4291]
གཞི་དང་གཞི་ཅན་གྱི་འབྲེལ་པ་ཉིད་རྒྱུ་དང་འབྲས་བུའི་འབྲེལ་པ་ཡིན་ཏེ། ཕན་གདགས་པར་བྱ་བ་མ་ཡིན་པ་ནི་གཞི་ཅན་མི་རིགས་པའི་ཕྱིར་རོ། །

[Block 4292]
ཕན་གདགས་པར་བྱ་བ་དང་ཕན་འདོགས་པར་བྱེད་པ་ཉིད་ནི་གཞི་དང་གཞི་ཅན་གྱི་འབྲེལ་པ་ཉིད་ཡིན་ནོ། །

[Block 4293]
རྒྱུས་ནི་འབྲས་བུ་ལ་ཕན་འདོགས་ན་རང་ལ་གནས་པའི་ཆོས་དང་མེད་པར་མི་འབྱུང་བས་ངེས་པར་ཕན་འདོགས་པར་བྱེད་པ་དང་། འབྲས་བུས་ཀྱང་རྒྱུ་ལ་གནས་པའི་ཆོས་མ་བླངས་པས་དེ་ལ་འབྱུང་བར་མི་འགྱུར་རོ། །

[Block 4294]
དེ་བས་ན་གལ་ཏེ་བདག་དང་ཕུང་པོ་དང་རྒྱུ་དང་འབྲས་བུའི་འབྲེལ་པ་ཁས་བླངས་ན་དེའི་ཚེ་ཕུང་པོ་མི་རྟག་པས་ཀྱང་བདག་ཀྱང་མི་རྟག་པར་འགྱུར་རོ། །

[Block 4295 [VERSE]]
གལ་ཏེ་བདག་རྟག་པ་ཡིན་ན། །
ཕུང་པོ་རྣམས་ཀྱང་རྟག་པར་འགྱུར་རོ། །

[Block 4296]
དེ་ཡང་མ་མཐོང་སྟེ་རང་དང་གཞན་གྱི་གྲུབ་པའི་མཐའ་དང་འགལ་བའི་ཕྱིར་རོ། །

[Block 4297]
གཞན་ཡང་བདག་གཞི་ཡིན་མོད་ཀྱི་དེ་ཡང་རྒྱུ་ཡིན་པས་ཕུང་པོ་བདག་ཉིད་ཀྱི་འབྲས་བུ་བྱུང་ན་འཇིག་པར་འགྱུར་རོ། །

[Block 4298]
ཕྱོགས་གཉིས་ཀ་ལ་ཡང་མི་རྟག་པར་འགྱུར་རོ། །

[Block 4299]
གལ་ཏེ་ཕུང་པོ་ལ་བདག་ཡོད་དེ༌[^2634]ཞེས་འདོད་ན་དེའི་ཚེ་སྔ་མ་བཞིན་དུ་གཞི་དང་གཞི་ཅན་གྱི་འབྲེལ་པ་མི་འགྲུབ་བོ། །

[Block 4300]
དེ་ལྟ་ཡིན་མོད་ཀྱི་དེ་བཞིན་དུ་ཡང་ཕུང་པོ་རྣམས་གཞི་ཡིན་པས་རྒྱུ་ཡིན་པའི་ཕྱིར་འབྲས་བུ་རྣམས་ངེས་པར་མི་འབྱུང་ངོ་ཞེས་པས་ཕུང་པོ་རྣམས་ཀྱིས་བདག་སྐྱེ་བར་མི་འགྱུར་བས་བདག་ཀྱང་མི་འགྱུར་རོ། །

[Block 4301]
གལ་ཏེ་རེས་འགའ་བྱུང་ན་དེའི་ཚེ་དེ༌[^2635]རྣམས་ཀྱིས་བདག་བསལ་བར་འགྱུར་རོ། །

[Block 4302]
གང་ཞིག་རེས་འགའ་བྱུང་བ་དེ་ནི་རྟག་པ་མ་ཡིན་ཏེ་ལམ་གྱི་སྐྱེས་བུའི་བཞིན་ནོ་ཞེས་དེ་ཉིད་མི་རྟག་པར་འགྱུར་རོ། །

[Block 4303]
ཕུང་པོ་དང་བདག་ཕན་ཚུན་ཐ་མི་དད་པ་སྟེ་མེ་དང་བུད་ཤིང་བཞིན་ནོ་ཞེས་འདོད་ན། དེའི་ཚེ་བུད་ཤིང་རྣམས་སོལ་བ་བཞིན་དུ་འགྱུར་བ་མེ་ཞེས་བརྗོད་པ་དེ་བཞིན་དུ་བདག་ནི་ཕུང་པོའི་ངོ་བོ་ཉིད་འཐོབ། ཕུང་པོའི་ཐ་སྙད་དུ་བརྗོད་དོ་ཞེས་ཤིན་ཏུ་མི་རྟག་པ་ཉིད་ཁས་བླངས་པ་ཡིན་ནོ། །

[Block 4304]
དེ་བས་ན་ཕྱོགས་བཞི་པོ་ཡང་བཟང་པོ་མ་ཡིན་ནོ། །

[Block 4305]
དེ་བཞིན་དུ་གཟུགས་ཀྱི་ཕུང་པོ་ལ་རྣམ་པ་བཞི་བཀག་ནས་ཚོར་བ་དང་འདུ་ཤེས་དང་འདུ་བྱེད་དང་རྣམ་པར་ཤེས་པ་རྣམས་ཀྱི་ཡང་ཕན་ཚུན་བདག་ཏུ་སྨྲ་བ་ཁས་བླངས་པ༌[^2636]བཀག་པར་ཤེས་པར་བྱའོ། །

[Block 4306]
དེས༌[^2637]ནི་རིའི་རྩེ་མོ་རྣམ་པ་ཉི་ཤུ་ལས་བྱུང་བའི་འཇིག་ཚོགས་ཀྱི་ལྟ་བ་བཀག་གོ། །

[Block 4307]
གང་གིས་འཁོར་བའི་འཁོར་ལོ་མ་ལུས་པ་འདི་ཉིད་མཚན་དུ་འཁྲུལ་འཁོར་གྱི་རིགས་པས་འཁོར་བ་ཞེས་བདག་ཏུ་སྨྲ་བའི་ཕྱོགས་བཀག་པའོ། །

[Block 4308]
དབང་ཕྱུག་དང་ཐམས་ཅད་བྱེད་པ་དང་ཐམས་ཅད་འཇིག་པར་བྱེད་པ་ནུས་པ་གསུམ་གྱིས་སྤྲུལ་པའི་བདག་ཉིད་ཆེ་བ་རྟག༌[^2638]པ་ཡིན་ནོ་ཞེས་འགལ་བ༌[^2639]སྟེ་གང་གི་ཕྱིར་གལ་ཏེ༌[^2640]ཐམས་ཅད་བྱེད་ཅིང་འཇིག་པར་བྱེད་པ་ན་དེའི་ཚེ་ཅིག་ཅར་དུ་བྱེད་པའམ་འཇིག་པ་ཅིའི་ཕྱིར་མི་བྱེད། དེ་མི་བྱེད་པས་རིམ་གྱིས་བྱེད་པ་མ༌[^2641]ཡིན་ཏེ། དེ་ཉིད་མི་རྟག་པ་ཉིད་དོ། །

[Block 4309]
གང་གི་ཕྱིར་གང་གི༌[^2642]དུས་སུ་བྱེད་ན་དེའི་ཚེ་དེ་ལ་ནུས་པ་ཡོད་དེ། [^2643]དུས་གཞན་དུ་དེ་མེད་དོ་ཞེས་ལྟོས་པ་དང་བཅས་པ་ཡིན་ནོ། །

[Block 4310]
ལྟོས་པ་དང་བཅས་པའི་ནུས་པ་མེད་པ་སྟེ། ལྷན་ཅིག་བྱེད་པ་ལ་ལྟོས་པའི་ཕྱིར་ཏེ། བུམ་པ་བཞིན་ནོ། །
--- END BLOCKS ---
