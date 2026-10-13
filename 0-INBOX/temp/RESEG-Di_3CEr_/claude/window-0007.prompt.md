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
[Block 246]
སྒྲ་ལ་སོགས་པ་ལ་ཐ་མི་དད་པར་འཛིན་པ་ཡང་མཐོང་ངོ་། །བདེ་བ་ལ་སོགས་པའི་ཡུལ་ཉིད་ཀྱང་མཚུངས་པར་འགྱུར། [^189]དབང་པོ་རྣམས་ཀྱི་ཡུལ་ཉིད༌[^190]མཚུངས་པར་འགྱུར་རོ། །

[Block 247]
དབང་པོ་རྣམས་རང་གི་ཡུལ་ལ་འཇུག་པར་མི་འགྱུར་ཏེ་བདེ་བ་ལ་སོགས་པ་ཡུལ་གཞན་ལ་རིགས་ཀྱི་བྱེ་བྲག་ཡོད་པའི་ཕྱིར་རོ། །

[Block 248]
དེ་ལྟ་ན་ཡང་དབང་པོ་གཅིག་ཉིད་དུ་ཐལ་པར་འགྱུར་རོ། །

[Block 249]
མ་ཡིན་ཏེ་རང་རང་གི་དབྱིབས་ཀྱིས་ཁྱད་པར་དུ་བྱས་པ་འཛིན་ནོ་ཞེས་བརྗོད་དོ་ཞེ་ན། དེ་སྐད་དུ་ནི་བརྗོད་ན་རིགས་པར་ནི་མི༌[^191]བརྗོད་དེ། གང་གི་ཕྱིར་དུ་མར་འཛིན་ཕྱིར་གཟུགས་ཀྱི་རིགས་གཅིག་ལ་ཡང་དབྱིབས་ཐ་དད་ཀྱི་སྒོ་ནས་དུ་མར་འཛིན་པར་བྱེད་པ༌[^192]ཡིན་གྱི་དབྱིབས་གཅིག་གི༌[^193]རྗེས་སུ་ཞུགས་ནས་འཛིན་པ་ནི་མ་མཐོང་ངོ་། །དེར་དབྱིབས་ཀྱི་ཐ་དད་ལས་རིགས་ཀྱི་ཐ་དད་འདོད་ན་ནི་དེ་ཉིད་དབང་པོ་ཐུག་པ་མེད་པར་ཐལ་བར་འགྱུར་བ་ཡིན་ནོ། །

[Block 250]
འདི་ལ༌[^194]ནི་གྲངས་ཅན་གྱི་བྱེ་བྲག་ལ༌[^195]ལས་མི་འདོད་དོ། །

[Block 251]
སྔོན༌[^196]སེར་སྐྱ་པའི་ལུགས་ལ་འདས་པར་སྨྲ་བ་གྲངས་ཅན་ཕུང་བར་བྱེད་པའི་མ་རྡུམ༌[^197]ན་རེ་སྒྲའི་མཚན་ཉིད་གསུམ༌[^198]ལས་ཐ་མི་དད་པ་མ་ཡིན་ཏེ། རིགས་གཞན་ཉིད་ལས་ནི་མ་ཡིན་པས་རེག་བྱ་ལ་སོགས་པའི་མཚན་ཉིད་གསུམ་པོ་དབང་པོ་ཐ་དད་གཞན་གྱིས་གཟུང་བར་འཐད་པ་མ༌[^199]ཡིན་ནོ། །

[Block 252]
དེའི་ཕྱིར་བདེ་བ་ལ་སོགས་པ་རྣམས་ལ་ཐ་དད་ཡོད་པས་དབང་པོ་རྣམས་རང་རང་གི་ཡུལ་དབང་བྱེད་པར་བརྗོད་དོ། །

[Block 253]
རང་གི་ཡུལ་ལ་འཇུག་པའི་དབང་པོ་རྣམས་ལ་ཐ་མི་དད་པའི་རང་གི་བྱེ་བྲག་ཡོད་པ་ཡིན་པས་དབང་པོ་རྣམས་ཐུག་པ་མེད་པར་ཐལ་བར་འགྱུར་རོ་ཞེས་ཟེར་རོ། །

[Block 254]
གལ་ཏེ་རིགས་ཀྱི་ཐ་དད་ལས་ཀྱང་བདེ་བ་ལ་སོགས་པའི་ཡུལ་དབང་པོ་ནུས་པ་དང་ལྡན་པར་བྱའོ་ཞེས་སྔོན་མ་རྣམས་ལས་ཁྱད་པར་དུ་བྱེད་པ་ལྟ་ན་ནི་དེ་བས་ཀྱང་ཆེས་ལྷག་པར་དུ་ཁོ་བོས་སྨྲ་བར་བྱ་བ་ཉིད་དེ།

[Block 255]
རེ་རེའི་ངོ་བོར༌[^200]ཐམས་ཅད་ནི། ། གཙོ་བོར་རྡུལ་ཕྲན་སོ་སོར་ཡོད། །

[Block 256]
བདེ་བ་དང་སྡུག་བསྔལ་དང་གཏི་མུག་དང་སྒྲ་དང་རེག་བྱ་དང་བྱ་བ་དག་གིས་ཐ་དད་ཀྱི་རིགས་ལས་ཐ་དད་པའི་གཙོ་བོ་རྡུལ་ཕྲ་རབ་ཐམས་ཅད་དུ་སོང་བ་ཡོད་དོ་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 257 [VERSE]]
རབ་ཏུ་སྦྱོར་བའི་བྱེ་བྲག་ལས། །
འབྲས་བུའི་ངོ་བོར་མཚོན་པར་བྱེད། །

[Block 258]
དེ་འདི་ལྟར་ཡང་དག་པར་རབ་ཏུ་སྦྱོར་བའི་བྱེ་བྲག་ལས་རང་གི་རིགས་ལས་མ་འདས་པར་འབྲས་བུའི་ངོ་བོར༌[^201]གྲུབ་པ་ནི་དབང་པོ་རྣམས་ཀྱི་ཡུལ་དུ་འགྱུར་རོ། །

[Block 259]
རྡུལ་ཕྲན་གསུམ་པོའི་རང་བཞིན་དུ། །གཅིག་དེའི་ངོ་བོར༌[^202]གང་གིས་འགྲོ། །

[Block 260]
གལ་ཏེ་སྒྲ་ལ་སྒྲའོ་ཞེས་བདེ་བ་ལ་སོགས་པ་དང་བྲལ་བའི་ཐ་མི་དད་ཀྱི་བློ་དེ་དོན་དུ་མའི་རང་བཞིན་ཐ་མི་དད་པ་ཡིན་པར་ནི་མི་རིགས་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན།

[Block 261]
རིགས་མི་མཐུན་ལས་གྱུར་པ་ཡི། །རབ་ཏུ་སྦྱོར་བར་འདོད་མ་ཡིན། །

[Block 262]
གསུམ་པོ་སྦྱར་བ༌[^203]ལས་གཅིག་ཏུ་གྱུར་པ་ནི་ཡོད་པ་མ་ཡིན་ཏེ། གྲངས་ཅན་རྣམས་ཀྱི་རིགས་ཐ་དད་དུ་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 263]
སྒྲ་གཅིག་བརྗོད་པ་ནི་ཡོད་པ༌[^204]ལ་རག་ལས་ན༌[^205]དངོས་པོ་གཅིག་པ་ནི་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 264]
ཅི་སྟེ་གསུམ་པོའི་རང་བཞིན་དུ་འགྱུར་བའི་སྒྲ་དང་བདེ་བ་ལ་སོགས་པར་གང་བརྗོད་པ་ཤེས་པར་འདོད་པའི་རང་བཞིན་ཏེ༌[^206]དབང་པོའི་ཡུལ་དུ་འབྱུང་བར་འགྱུར་རོ་ཞེ་ན།

[Block 265]
ཚུལ་གཉིས་ཤེས་པར་མི་འདོད་ན། །འབྲས་བུ་གཅིག་གི་ངོ་བོར་འགྱུར། །

[Block 266]
གལ་ཏེ་རྣ་བས་སྒྲ་ཉན་པ་ལ་སོགས་པའི་བློ་ནི་བདེ་བ་ལ་སོགས་པ་ལ་མི་ལྟོས་པར་གཞན་ལས་ཁྱད་པར་དུ་གྱུར་པ་འདི་ལ་འཇུག་པར་བྱེད་དེ༌[^207]དེ་ཉིད་ཁོ་ནས་གཅིག་གི་རང་བཞིན་དུ་འགྱུར་རོ། །ཅིའི་ཕྱིར་ཞེ་ན།

[Block 267 [VERSE]]
དོན་གྱི་རང་བཞིན་དུ་མ་སྟེ། །
དབང་པོའི་ཡུལ་ནི་ཁྱད་པར་ཅན། །

[Block 268]
སྒྲ་ལ་སོགས་པའི་དོན་གྱི༌[^208]རང་བཞིན་དུ་མ་ཡོད་པ་ལས་རང་བཞིན་གང་ལ་བློ་འཇུག་པ་དེ་དབང་པོའི་དོན་ཏེ། དེ་ཉིད་དབང་པོའི་ཡུལ་ཡིན་ནོ། །

[Block 269]
དེ་ཡང་གཅིག་ཁོ་ན་སྟེ། རེག་བྱ་ལ་སོགས་པ་རྣམས་ལ་ཡང་མཚུངས་པ་མ༌[^209]ཡིན་ནོ། །

[Block 270 [VERSE]]
དེའི་ཕྱིར་རིགས་པ་མ་ཡིན་ནོ། །
དེའི་ཕྱིར་རེ་རེའི་དངོས་པོ་ལ། །
གྲངས་ཅན་ལུགས་ལས་ཁྱད་པར་འཕགས། །

[Block 271]
སྔོན་གྲགས་པའི་གྲངས་ཅན་གྱི་ལྟ་བ་ལས་ཁྱད་པར་དུ་འཕགས་ཤིང་མཆོག་ཏུ་གྱུར་པ་ནི་བདེན་པ་ཁོ་ན་སྟེ། རིགས་ཀྱི་བྱེ་བྲག་གཅིག་གི་རང་བཞིན་ཙམ་གྱི་རྒྱུ་ལས་འབྲས་བུ་སྐྱེ་བར་བརྟགས་པ་སྟེ། དེ་ལྟ་ན་ནི་རིགས་མི་མཐུན་གྱི་འབྲས་བུ་མི་རྩོམ་མོ་ཞེས་མཛེས་པར་འགྱུར་གྱི། གསུམ་གྱི་རང་བཞིན་གཅིག་པ་ཉིད་ལས་ནི་མ་ཡིན་ནོ། །

[Block 272]
གལ་ཏེ་ཡང་ད་ལྟར་བའི་སྒྲ་ཙམ་འཛིན་པར་བྱེད་པའི་དབང་པོའི་འཇུག་པ་མངོན་སུམ་དུ་འདོད་པ་དེ་ལྟ་ན་ནི་ཡུལ་གཅིག་མ་ཡིན། གཞལ་བར་བྱ་བ་ཐམས་ཅད་ཀྱང་ཡུལ་མ་ཡིན་པ༌[^210]ཚད་མ་ཡིན་པ་བསལ་བར་འགྱུར་རོ། །

[Block 273]
འཇུག་པ་དེ་ཚད་མར་བརྗོད་པ་མ་ཡིན་ནོ། །

[Block 274]
དབང་པོའི་འཇུག་པ་ཡང་དག་པར་མྱོང་བར་བྱེད་པའི་ཡིད་ཀྱི་དབང་པོ་ལ་ནི་རྟགས་ལ་སོགས་པ་མེད་པས། ཚད་མར་མ་བརྗོད་པའི་ཕྱིར་ཉམས་པ་ཉིད་དུ་འགྱུར་རོ། །

[Block 275]
དེར་འཇུག་པའི་ཡང་དག་པར་མྱོང་བ་ཚད་མ་གཞན་གྱི་ཁོངས་སུ་འདུ་བར་ནི་མི་འགྱུར་རོ། །

[Block 276]
ཉེས་པ་དེ༌[^211]ནི་མེད་དེ། དེར་ཞུགས་པའི་ཉམས་སུ་མྱོང་བ་ནི་དྲན་པ་སྟེ། འདོད་པ་ལ་སོགས་པ་བཞིན་ནོ། །

[Block 277]
གང་ཇི་སྐད་དུ་དྲན་པ་ནི་མངོན་སུམ་གྱི༌[^212]འཇུག་པའི་བྱེ་བྲག་གོ་ཞེས་བརྗོད་དོ། །

[Block 278]
དེའི་ཕྱིར་དབང་པོའི་ཤེས་པ་ནི་ཕྱི་རོལ་གྱི༌[^213]དོན་ལ་མངོན་སུམ་སྟེ། དབང་པོའི་འཇུག་པ་དང་བར་དུ་མ་ཆོད་པ་ཡིན་ནོ། །

[Block 279]
དྲན་པའོ་ཞེ་ན། དྲན་མིན་ཉམས་སུ་མ༌[^214]མྱོང་ཕྱིར། །བར་མ་ཆོད་པའི༌[^215]ཡིད་ནི་དབང་པོའི་འཇུག་པ༌[^216]འཛིན་པར་བྱེད་པའི་དྲན་པར་རིགས་པ་མ་ཡིན་ནོ།[^217] །

[Block 280]
སྔར་ཉམས་སུ་མ་མྱོང་བའི་ཕྱིར་རོ། །ཅིག་ཅར་གཉིས་ཀ་འབྱུང་བར་འགྱུར། །

[Block 281]
ཅིག་ཅར་བ་ཡིན་ན་ཡང་དབང་པོས༌[^218]ཤེས་པ་དང་། དེ་ཉམས་སུ་མྱོང་བར་བྱེད་པའི་ཡིད་གཉིས་ཀ་བསལ་བར༌[^219]ཁས་བླངས་པར་འགྱུར་རོ། །

[Block 282]
དེ་ལྟ་ན་ནི་ཡུལ་གྱི་རྒྱུ་མཚན་ཡུལ་ཅན་ལ་ཡང༌[^220]ཡོད་པར་འགྱུར་རོ། །

[Block 283]
དེ་ནི་ཚད་མའི་དབང་པོ་ཉམས་སུ་མྱོང་བའི་ཡིད་དེ་ནི་ཚད་མར་མ་བརྗོད་དེ༌[^221]དེས༌[^222]ནི་དེའི་གནས་སྐབས་ལ་ཞུགས་པ་པོ་ཡང་ཚད་མར་མ་བརྗོད་པའི་ཕྱིར་མྱངས་པར༌[^223]འགྱུར་རོ། །

[Block 284]
རང་རིག་ཏུ་འདོད་པ་ལ་སོགས་པ་ལ་ནི༌[^224]ཉེས་པ་མེད་དོ།[^225] །

[Block 285]
དྲན་པ་ཞེས་བྱ་བ་ནི་ལོང་བའི་གོམ་པ་ཉིད་དེ། དེ་ཡོད་པ་ལྟ༌[^226]ན་ནི་དྲན་པ་འདི་མངོན་སུམ་འཛིན་པའི་བྱེ་བྲག་གོ་ཞེས་བྱ་བར་འགྱུར་རོ། །
--- END BLOCKS ---
