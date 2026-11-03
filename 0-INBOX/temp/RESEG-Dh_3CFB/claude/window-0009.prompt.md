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
[Block 316]
གལ་ཏེ་གཞན་གྱི་རྒྱུ་ཅན་ཡིན་པའི་ཕྱིར། རྒྱུ་མེད་པ་ཅན་ཉིད་མ་ཡིན་ནོ་ཞེ་ན། དེ་ལྟ་མ་ཡིན་ཏེ། དེ་ལ་ཡང་མཚུངས་པའི་ཕྱིར་ཏེ། དེ་མེད་ན་ཡང་མེ་ཡོད་ན་ཡོད་པས་སོ། །

[Block 317]
ཡང་དེའམ་གཞན་ཡང་རུང་། དེ་བསྐྱེད་པའི་རང་བཞིན་མ་ཡིན་པ་ལས་ནི་ཇི་ལྟར་འབྱུང་བར་འགྱུར་ཏེ། དེའི་རང་གིས༌[^196]དེའི་རང་བཞིན་མ་ཡིན་པས་མི་བསྐྱེད་པའི་ཕྱིར་རོ།[^197] །དེ་རྒྱུ་མེད་པ་ཉིད་དུ་འགྱུར་རོ། །

[Block 318]
དེ་ཉིད་ནི་མ་ཡིན་པ་ཁོ་ན་སྟེ། དེ་དང་འདྲ་བ་འབྱུང་བའི་ཕྱིར་རོ་ཞེ་ན། མི་འདྲ་བ་ལས་འབྱུང་བ་ཇི་ལྟར་དེ་དང་འདྲ་བས༌[^198]ཡིན་ཏེ། དེ་ནི་དེ་དང་འདྲ་བ་ལ་མ་བྱུང༌[^199]བའི་ཕྱིར་དེ་དང་འདྲ་བར་འགྱུར་རོ། །

[Block 319]
མི་འདྲ་བ་ལས་དེ་དང་འདྲ་བ་འགྱུར༌[^200]ན་ནི། དེ་དག་གི་ནུས་པ་མ་ངེས་པའི་ཕྱིར་རྒྱུའི་ཐ་དད་པ་ཐ་དད་པར་བྱེད་པ་མ་ཡིན་པས། མཐའ་དག་གི་སྣ་ཚོགས་ཉིད་རྒྱུ་མེད་པ་ཅན་དུ་འགྱུར་བའམ། ཐམས་ཅད་ལས་ཐམས་ཅད་སྐྱེ་པར་འགྱུར་རོ། །

[Block 320]
དེ་ལྟ་བས་ན་རྒྱུའི་ཐ་དད་པ་དང་ཐ་དད་པ་མ་ཡིན་པ་དག་གིས་འབྲས་བུ་ཐ་དད་པ་དང་ཐ་དད་པ་མ་ཡིན་པ་དག་ཡིན་ནོ། །

[Block 321]
དེ་བས་ན་དུ་བ་ནི་མཐོང་བའི་རྣམ་པ་དང་རིགས་མི་མཐུན་པའི་དོན་ལས་མི་འབྱུང་སྟེ། རྒྱུ་མེད་པ་ཉིད་དུ་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 322]
དེ་ལྟ་མ་ཡིན་ཏེ། །

[Block 323 [VERSE]]
རྒྱུ་མེད་གཞན་ལ་མི་ལྟོས་ཕྱིར། །
རྟག་ཏུ་ཡོད་པའམ༌[^201]མེད་པར་འགྱུར། །
དངོས་པོ་རྣམས་ནི་རེས་འགའ་ཞིག །
འབྱུང་བ་ལྟོས་པ་ལས་ཡིན་ནོ།

[Block 324]
[^202] །དུ་བ་དེ་རྒྱུ་མེད་པ་ལས་འབྱུང་ན་ནི་ལྟོས་པ་མེད་པའི་ཕྱིར་ནམ་ཡང་མི་འབྱུང་བར་མི་འགྱུར་ཏེ། དེ་འབྱུང་བ་ལ་མ་ཚང་བ་མེད་པའི་ཕྱིར་འདོད་པའི་དུས་བཞིན་ནོ། །

[Block 325]
ཡང་ན་ནི་དེའི་ཚེ་ཡང་འབྱུང་བར་མི་འགྱུར་ཏེ། མེད་པའི་དུས་དང་ཁྱད་པར་མེད་པའི་ཕྱིར་རོ། །

[Block 326]
དངོས་པོ་ལྟོས་པ་རྣམས་ནི་རེས་འགའ་བར་འགྱུར་ཏེ། ཡོད་པ་དང་མེད་པའི་དུས་དག་ན་དེ་འབྱུང་བར་རུང་བ་དང་མི་རུང་བ་ཉིད་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 327]
ཡུལ་དང་དུས་རུང་བ་དང་མི་རུང་བ་ཉིད་འདྲ་བ་ཅན་དག་ལ་ནི་དེ་དང་ལྡན་པ་དང་། ཅིག་ཤོས་དག་ཏུ་ངེས་པར་མི་རུང་བའི་ཕྱིར་རོ། །

[Block 328]
རུང་བ་ཉིད་དེ་ཡང་རྒྱུའི་དངོས་པོ་ལས་གཞན་ཡིན་ནམ་ཅི། དེའི་ཕྱིར་ཡུལ་དང་དུས་འགའ་ཞིག་སྤངས་ནས་ཡུལ་དང་དུས་གཞན་དག་ན་ཡོད་པའི་དངོས་པོ་ནི་དེ་དག་ལ་ལྟོས་པ་དང་བཅས་པ་ཞེས་བྱ་བ་ཡིན་ཏེ། འདི་ལྟར་དེ་ལྟར་ཡོད་པ་ཉིད་ལྟོས་པ་ཡིན་ནོ། །

[Block 329]
དེ་དག་གིས་བྱས་པའི་ཕན་པ་ལ་མི་ལྟོས་པ་ནི་དེར་ངེས་པར་མི་རུང་བའི་ཕྱིར་རོ། །

[Block 330]
དེ་བས་ན་ཡུལ་དང་དུས་ངེས་པའི་ཕྱིར་གང་ན་དུ་བ་ལན་ཅིག་མཐོང་ལ་མ་ཚང་ན་མ་མཐོང་བ་ནི་འདིའི་དེས་བསྐྱེད་པར་བྱ་བའི་ངོ་བོ་ཉིད་ཡིན་ཏེ། གཞན་དུ་ན་དོན༌[^203]ལན་འགའ་ཡང་མེད་པའི་ཕྱིར་རོ། །

[Block 331]
དེ་དེར་ངེས་པ་ཡིན་ན་ཇི་ལྟར་གཞན་པ་ལས་འབྱུང་བར་འགྱུར། འབྱུང་བ་ན་ནི་དུ་བ་མ་ཡིན་པར་འགྱུར་ཏེ། དུ་བ་ནི་དེས་བསྐྱེད་པའི་རང་བཞིན་གྱི་ཁྱད་པར་ཡིན་ནོ། །

[Block 332]
དེ་བཞིན་དུ་རྒྱུ་ཡང་འབྲས་བུ་དེ་ལྟ་བུ་བསྐྱེད་པའི་རང་བཞིན་ཡིན་ནོ། །

[Block 333]
དེ་གཞན་ལས་ཀྱང་འབྱུང་ན་ནི་དེ་དེའི་རང་བཞིན་མ་ཡིན་བསལ་ན་འགའ་ཡང་བསྐྱེད་པར་མི་འགྱུར་རོ། །

[Block 334]
ཡང་ན་དེ་དུ་བ་མ་ཡིན་ཏེ་དུ་བ་བསྐྱེད་པའི་རང་བཞིན་མ་ཡིན་པ་ལས་བྱུང་བའི་ཕྱིར་རོ། །

[Block 335]
དེའི་རང་བཞིན་ཉིད་ཡིན་ན་ནི་དེ་ཉིད་མ༌[^204]ཡིན་པས་འཁྲུལ་པ་མེད་དོ། །

[Block 336]
གལ་ཏེ་བརྒྱ་བྱིན་སྤྱི་བོ་མེའི།[^205] །

[Block 337 [VERSE]]
རང་བཞིན་ཡིན་ན་དེ་ཉིད་མེ། །
འོན་ཏེ་དེ་མེའི་རང་བཞིན་མིན། །
ཇི་ལྟར་དེ་ལས་དུ་བ་འབྱུང་། །
དུ་བའི་རྒྱུ་ཡི་རང་བཞིན་མེ། །

[Block 338 [VERSE]]
དེ་ཡི་ནུས་པའི་བྱེ་བྲག་ལྡན། །
དུ་བ་དུ་བའི་རྒྱུ་མིན་ལས། །
འབྱུང་ན་དེ་ནི་རྒྱུ་མེད་འགྱུར། །

[Block 339]
ཞེས་བྱ་བ་ནི་བསྡུ་བའི་ཚིགས་སུ་བཅད་པའོ། །

[Block 340]
འོ་ན་ད་ནི་ཇི་ལྟར་ལྷན་ཅིག་བྱེད་པ་ཐ་དད་པ་ལས་འབྲས་བུ་སྐྱེ་སྟེ། དཔེར་ན་མིག་དང་གཟུགས་ལ་སོགས་པ་ལས་རྣམ་པར་ཤེས་པ་ལྟ་བུའོ་ཞེ་ན། དེའི་རང་བཞིན༌[^206]གཅིག་པུས་སྐྱེད་པར་བྱེད་པ་ནི་ཅུང་ཟད་ཀྱང་མེད་དོ། །

[Block 341]
འོན་ཀྱང་ཚོགས་པས་སྐྱེད་པར་བྱེད་པ་ནི་དེའི་རང་བཞིན་ཡིན་ཏེ། དེ་ཁོ་ན་རྗེས་སུ་དཔག་གོ། །

[Block 342]
ཚོགས་པ་དེ་ཉིད༌[^207]འབྲས་བུའི་རང་གི་ངོ་བོ་གནས་པའི་རྟེན༌[^208]ཡིན་ནོ། །

[Block 343]
དེ་ཉིད་ཀྱི་ཕྱིར་ལྷན་ཅིག་བྱེད་པ་རྣམས་ཀྱང་རྣམ་གྲངས་མེད་པར་སྐྱེད་པར་བྱེད་པ་ཡིན་ནོ། །

[Block 344]
གང་ཡང་ཅུང་ཟད་ལྕི་བ་ལ་སོགས་པ་རིགས་མི་མཐུན་པ་ལས་ཨུཏྤལ་ལ་སོགས་པ་འབྱུང་བར་མཐོང་བ་དེ་ལ་ཡང་དེ་སྐད་དུ་བརྗོད་ཀྱང་རང་གི་ས་བོན་ལས་རབ་ཏུ་བྱུང་བ་ཅན་ཡིན་པའི་ཕྱིར་རང་གི་ངོ་བོ་ཐ་དད་པ་ཡོད་པ་ཁོ་ན་སྟེ། རྒྱུའི་རང་གི་ངོ་བོ་ཐ་དད་པའི་ཕྱིར་དཔེར་ན་ཆུ་ཤིང་གི་ས་བོན་དང་སྡོང་བུ་ལས་སྐྱེ་བ༌[^209]ཅན་ལྟ་བུའོ། །

[Block 345]
དེ་ལྟ་བུ་ནི་འཇིག་རྟེན་ན༌[^210]གསལ་བ་ཁོ་ནར་རྣམ་པ༌[^211]ཐ་དད་པའི་སྒོ་ནས་རྣམ་པར་འབྱེད་དོ། །

[Block 346]
དེ་ལྟ་བས་ན་ཤིན་ཏུ་རྣམ་པར་ཕྱེ་བའི་རྣམ་པ་ཅན་གྱི་འབྲས་བུས༌[^212]ནི་རྒྱུ་འཁྲུལ་པ་མེད་དོ། །

[Block 347 [VERSE]]
རྗེས་སུ་འགྲོ་དང་ལྡོག་པ་ལས། །
གང་ཞིག་གང་གི་རྗེས་འགྲོར་མཐོང་། །
དེ་ཡི་རང་བཞིན་དེའི་རྒྱུ་ཅན། །
དེ་ཕྱིར་མི་མཐུན་ལས་མི་འབྱུང་། །

[Block 348]
ཞེས་བྱ་བ་ནི་བསྡུ་བའི་ཚིགས་སུ་བཅད་པའོ། །

[Block 349]
དེ་ལྟ་བས་ན་ལན་ཅིག་མཐོང་བ་དང་། མ་མཐོང་བ་དག་གིས་ཀྱང་རྒྱུ་དང་འབྲས་བུའི་དངོས་པོ་གྲུབ་པའི་ཕྱིར། དེས་དེ་རྟོགས་ཀྱི་གཞན་དུ་ནི་མ་ཡིན་ཏེ། རྗེས་སུ་འགྲོ་བ་དང་ལྡོག་པ་དག་མ་ལུས་པར་མཐོང་བ་དང་། མ་མཐོང་བ་ལ་རག་ལུས་པའི༌[^213]ཕྱིར་རོ། །

[Block 350]
ལུས་ཅན་མ་ཡིན་པ་ཉིད་འགའ་ཞིག་ལ་རྟག་པ་ཉིད་མཐོང་ཡང་གཞན་ལ་གཞན་དུ་མཐོང་བའི་ཕྱིར་དང་། རྟག་པ་ཉིད་མེད་པ་འགའ་ཞིག་ལ་མ་མཐོང་བ་ཡང་མཐོང་བའི་ཕྱིར་རོ།། །།

[Block 351]
བམ་པོ་གཉིས་པ། [^214]

[Block 352 [HEADING]]
## རང་བཞིན་མེད་ན་མི་འབྱུང་བ། ^4-0

[Block 353]
འབྲས་བུ་ནི་དེ་ལས་སྐྱེ་བའི༌[^215]ཕྱིར་རྒྱུ་མེད་ན་མི་འབྱུང་བ་ཡིན་ལ་རག་ན། ད་རང༌[^216]བཞིན་ཇི་ལྟར་མེད་ན་མི་འབྱུང་བ་ཡིན་ནོ༌[^217]ཞེ་ན།

[Block 354 [VERSE]]
རང་བཞིན་ལ་ཡང་མེད་མི་འབྱུང་། །
ཡོད་པ་ཙམ་དང་འབྲེལ་པ་ཡིན། །

[Block 355]
གང་ཞིག་ཡོད་པ་ཙམ་དང་འབྲེལ་པའི་རང་བཞིན་ཡིན་པ་དེ་ལ་ནི་ཡོད་པ་མེད་ན་མི་འབྱུང་བར་འདོད་དེ། དེ་མེད་པར༌[^218]ནི་ཡོད་པ་དག །མེད་འགྱུར་ཐ་དད་མེད་ཕྱིར་རོ།[^219] ། ངོ་བོ་གང་ཁོ་ན་ཡོད་པ་ཙམ་ལ་རག་ལས་པའི་རང་བཞིན་ཡིན་པར་བརྗོད་པ་དེ་ཁོ་ན་རང་གིས་དངོས་སུ་ཡོད་པ་ཡིན་ནོ། །
--- END BLOCKS ---
