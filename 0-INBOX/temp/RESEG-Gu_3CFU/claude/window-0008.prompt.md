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
[Block 281]
བསྒྲུབ་པར་བྱ་བ་ཐབས་བརྗོད་པ་དང་བཅས་པ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་བརྗོད་པ་དང་ལྷན་ཅིག་ཏུ་ནི་བརྗོད་པ་དང་བཅས་པའོ། །

[Block 282]
གང་གི༌[^202]དོན་དུ་རབ་ཏུ་བྱུང་བ་ཉིད༌[^203]དང་བསྙེན་པར་རྫོགས་པ་དེ་བསྒྲུབ་པར་བྱ་བ་ལ་ཚེ་དང་ལྡན་པ་ཁྱོད་བསྙེན་པར་རྫོགས་ཟིན་གྱིས་བག་ཡོད་པར་སྒྲུབས༌[^204]ཤིག་ཅེས་བྱ་བ་འདིས་ངེས་པར་སྦྱར་བར་བྱའོ། །

[Block 283]
འདི་ལྟ་སྟེ་ཁྱོད་ནི་གནས་འདི་རྗེས་སུ་ཐོབ་པ་སྟེ། ད་ནི་འདིར་ཁྱོད་ཀྱིས་མངོན་པར་དགའ་བར་བྱ་ཞེས་བྱ་བའོ།

[Block 284]
[^205] །

[Block 285]
དང་པོ་ཕྱག་ལན་གསུམ་བྱས་ནས་དགེ་འདུན་འདུས་པའི་ནང་དུ་རྗེས་སུ་བསྟན་པ་ལ་ཙོག་ཙོག་པོར་འདུག་པའི་མདུན་དུ་སོ་ཕག་བཏིང་བ་དག་གིས་གསང་སྟེ་སྟོན་པ་ལ་བསྙེན་པར་རྫོགས་པ་ལ་གནས་པའི་ལག་པ་གཡོན་པར་ལྷུང་བཟེད་བཞག་སྟེ། ལག་པ་གཡས་པས་བཀབ་ནས་ཞེས་བྱ་བ་ལ་སོགས་པ་ལས་ཀྱི་གཞིར་འཆད་པར་འགྱུར་བ་ཉིད་ཀྱི་ཕྱིར་འདིར་རྗེས་སུ་འབྲེལ་པ་མ་བྱས་སོ། །

[Block 286]
བསྙེན་པར་རྫོགས་པའི་ཆོ་གའོ།། །།

[Block 287]
གནས་པས་གནས་པ་ལ་མ་ཞུས་པར་བྱ་བ་མི་བྱའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་མ་ཞུས་པ་ནི་མ་དྲིས་པའོ། །

[Block 288]
མ་དྲིས་པར་ཅུང་ཟད་ཀྱང་མི་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 289]
བྱ་བ་མཐའ་དག་གནས་ལ་ཞུ་བར་བྱས་པ༌[^206]ཐལ་བ་ལ། བྱ་བ་འགའ་ཞིག་མ་དྲིས་པར་ཡང་བྱེད་པ་བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་ཏེ། དེའི་ཕྱིར་བཤང་བ་དང༌[^207]གཅི་བ་དང་སོ་ཤིང་དོར་བ་དང་ཉེ་འཁོར་དང་བཅས་པའི་གཙུག་ལག་ཁང་དུ་མཆོད་རྟེན་ལ་ཕྱག་བྱ་བ་ནི་མ་གཏོགས་སོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་འདིར་ནང་དུ་བྱ་བའི་གྲངས་འདྲུ་བ་ལ་སོགས་པའི་བྱ་བས་མངོན་པར་ཁྱབ་པ་དེ་ནི་འདིར་ཉེ་འཁོར་དུ་རིག་པ་ཡིན་ནོ། །

[Block 290]
ཉེ་འཁོར་དུ་ལྷན་ཅིག་ཏུ་ནི་ཉེ་འཁོར་དང་བཅས་པའོ། །

[Block 291]
དེར་མཆོད་རྟེན་གང་ཞིག་ལ་ཕྱག་འཚལ་བའོ། །

[Block 292]
གཙུག་ལག་ཁང་ནས་འདོམ་བཞི་བཅུ་རྩ་དགུའི་མཐའ་ཚུན་ཆད་དུ་འགྲོ་བ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་མ་གཏོགས་སོ་ཞེས་བྱ་བར་རྗེས་སུ་འབྲེལ་ལོ། །

[Block 293]
གཅིག་གིས༌[^208]མ་ཚང་བའི་ལྔ་བཅུ་ཞེས་བྱ་བ་ལ། ཨཱ་ཊས་མཚམས་སྦྱར༌[^209]བའོ། །

[Block 294]
འདོམ་གཅིག་གིས་མ་ཆོག་པའི་ཇི་སྲིད་ལྔ་བཅུའི་མཐར་ཐུག་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 295]
གཙུག་ལག་ཁང་གང་ལ་འོབས་སམ་ར་བའམ་འཁོར་ས་གཞན་ཡོད་པ་དེ་ལ་གཙུག་ལག་ཁང་གི༌[^210]མཐའ་མ་ཞེས་བྱ་བའི་ངེས་པར་རིག་པ་ཡིན་ནོ། །

[Block 296]
ར་བ་དུ་མ་ལ་སོགས་པ་ལ་ཐམས་ཅད་ཀྱི་ཕྱི་རོལ་ལོ། །

[Block 297]
དེ་བས་ན་དེའི་ཕྱི་རོལ་གྱི་ལོགས་ཀྱི་ཚད་ནི་འདིའི་ཚད་ཀྱི་ཐ་མའོ། །

[Block 298]
གང་ཞིག་འཁོར་ས་མེད་པ་དེ་ལ་གཙུག་ལག་ཁང་གི་རྩིག་པ་ཉིད་ནི་ཐ་མའོ། །

[Block 299]
འདིར་གང་ཞིག་འོག་ཏུ་སྔར་བཤད་པའི་ཉེ་འཁོར་གྱི་གནས་དེ་ལ་བརྟེན་པའི་མཆོད་རྟེན་ནི་ཕྱག་བཙལ་བར་བྱ་བ་མ་ཡིན་ཞེས་བྱ་བ་འདིར་ཉེ་བར་གནས་པ་ཡིན་ནོ། །

[Block 300]
བཅག་པར་བྱ་བའི་ཕྱིར་རྗེས་སུ་གནང་བ་འདི་ཡིན་ཏེ། གཞན་ཡང་དེ་བས་ན་མཆོད་རྟེན་ལ་ཕྱག་བཙལ་བ་ཞེས་བྱ་བའོ། །

[Block 301]
དེར་ཅི་ཞིག་བསྒྲུབ་པར་བྱ་ཞེ་ན། དེའི་དོན་དུ་མ་དྲིས་པར་འགྲོ་བར་མི་བྱའོ། །

[Block 302]
བཅག་པར་བྱ་བའི་ཕྱིར་འགྲོ་བ་ནི་ཕྱག་བཙལ་བར་བྱ་ཞེས་བྱ་བའོ། །

[Block 303]
བྱ་བ་འདི་ནི་རྣམ་པ་གཉིས་ཏེ། རྩོམ་པར་གྱུར་པ་དང་མངོན་པར་ཕྱག་འཚལ་བར་གྱུར་པའོ། །

[Block 304]
དེ་ལ་གང་ཟག་རྩོམ་པར་གྱུར་པ་དེ་ཉིད་བཀག་པ་ཡིན་ཏེ། མངོན་པར་ཕྱག་འཚལ་བར་གྱུར་པ་ལ་ནི་དགག་པར་བྱ་བ་མ་ཡིན་པ་ཉིད་དུ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 305]
འདི་ལྟ་སྟེ་གཏམ་འདྲེ་བ་དང་ཕེབས་པར་སྨྲ་བ་དང་། ཕན་ཚུན་ཀུན་དགའ་བར་བྱ་བ་དང་། ལན་གདབ་པ་དང་འོངས་པ་ལེགས་སོ་ཞེས་བརྗོད་པ་ལ་སོགས་པ་དང་། ལག་པ་ཚུར་བསྙུགས༌[^211]པས་རྐང་ལག༌[^212]དག་ལ་བྱུག་པ༌[^213]དང་། གོས་ལ་རྡུལ་ཆགས་པ་སྤྲུག་པ་དང་། དེ་ལྟ་བུ་ལ་སོགས་པའོ། །

[Block 306]
དེ་ནི་མ་ཞུས་པར་ཡང་བྱ་སྟེ། དེ་དག་ཞུས་ན་བཞད་གད་ཀྱི་གཞིར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 307]
མཆིལ་ལྷམ་དང་སོ་ཤིང་དང་ཀློག་པ་དང་ཁ་དོན་བྱེད་པ་དང་། ཉེ་བར་བསྡུ་བ་རྣམས་བྱེད་པ་དང་སོ་སོར་འདོད་པ༌[^214]རྣམས་ལ་དེའི་རིགས་ཅན་དགེ་སློང་དང་ཉེ་བར་གནས་ཞེས་བྱ་བའི་ཁྱད་པར་ཡོངས་སུ་འཛིན་པས་འདིར་མངོན་པར་ཕྱག་འཚལ་བར་གྱུར་པ་འདོད་པ་ཡིན་ཞེས་བྱ་བར་ཤེས་པར་བྱའོ། །

[Block 308]
འདིར་རབ་ཏུ་བྱུང་བ་གདུག་པ་ཅན་ཤེས་པ་འམ། དོགས་པ་མ་དྲིས་པར་ཡོངས་སུ་སྤང་བར་བྱ་བ་མ་ཡིན་ཏེ། གཞན་ནི་མ་ཡིན་ནོ། །

[Block 309]
གང་གི་ཕྱིར་ཀློག་པ་འམ་ཁ་དོན་བྱེད་པ་ལ་ཉེ་བར་བསྡུ་བ་དེ་དག་རྗེས་སུ་མཐུན་པའི་དུས་ལ་ཉེ་བར་བསྡུ་བ་བྱ་བ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་བྱ་བ་ཉིད་ཀྱིས་རབ་ཏུ་ཤེས་སོ། །

[Block 310]
མངོན་པར་ཕྱག་འཚལ་བའི་རྣམ་པ་ཉིད་ཀྱིས་འདིའི་ཡིད་ལ་ངེས་པར་གནས་སོ། །

[Block 311]
གདུག་པ་ཅན་ལ་མི་མཐུན་པའི་རྗེས་སུ་འགྲོ་བ་ཅན་ཉིད་ཀྱིས་འདི་སོ་སོར་སྨྲ་བར་གྱུར་པ་ན་རྩོམ་པ་ཉིད་ཀྱིས་གྲགས་པ་ཉེ་བར་འགྲོ་བ་ཡིན་ཏེ། དེ་བས་ན་དེ་ལ་འབད་པར་བྱ་ཞེས་བྱ་བས་འདིར་དགོངས་པ་མཐོང་བ་ཡིན་ནོ།[^215] །ཆུ་འཐུང་བ་ལ་ཡང་མ་ཞུས་པར་བྱེད་པ་བར་དུ༌[^216]གཅོད་པ་འདིས་བྱས་པར་རིག་པར་བྱའོ། །

[Block 312]
གང་གི་ཕྱིར་འདི་ནི་རྣམ་པ་གཉིས་ཡིན་ཏེ། རྡུལ་དང་བྲལ་བའི༌[^217]ཡན་ལག་རྣམས་ལ་ཆུས་ཡང་དག་པར་རེག་པའོ། །

[Block 313]
གནས་པའི་ཚུལ་ཁྲིམས་བརྗོད་པར་བྱ་སྟེ། ལྷུང་བཟེད་དང་ཆོས་གོས་ཀྱི་ལས་དང་། ནད་གཡོག་དང་འགྱོད་པ་བསལ་བ་དང་། སྡིག་པ་ཅན་གྱི་ལྟ་བའི་རྣམ་པ་སྤོང་བ་ལ་ཨེ་མའོ་བདག་གིས་བྱའོ་ཞེ་འམ། བྱེད་དུ་འཇུག་གོ་ཞེས་བརྩོན་པ༌[^218]ཆེན་པོས་བསྒྲུབ་པར་བྱའོ་ཞེས་བྱ་བ་ལ། འདིར་ཁ་ཅིག་ནི་མཚོན༌[^219]གྱི་ལས་ཀྱང་འདོན་པ་ཡིན་ཏེ། དེ་ཆོས་གོས་ཀྱི་ལས་ལས༌[^220]ལྷག་པ་མེད་པའི་ཕྱིར་གཟུང་བར་མི་བྱའོ། །

[Block 314]
ནན་ཏུར་བྱེད་པར་འདོད་པའི་དགེ་འདུན་ལ་ཨེ་མའོ་དགེ་འདུན་གྱིས་འདི་ལ་ནན་ཏུར་གྱི་ལས་འདི་ལྟ་བུ་མི་བྱའོ་ཞེས་ཀྱང་ངོ་ཞེས་བྱ་བ་ལ་ནན་ཏུར་བྱེད་པར་འདོད་པ་ལ་ཞེས་བྱ་བ་ནི་གདོན་པར་འདོད་པ་ལ་སོགས་པའི་ནན་ཏུར་གྱི་ལས་བྱེད་པར་འདོད་པའི་དགེ་འདུན་ལའོ། །

[Block 315]
ཨེ་མའོ་དགེ་འདུན་གྱིས་འདི་ལ་ཞེས་བྱ་བ་ནི་རྟེན་ལའོ། །

[Block 316]
ནན་ཏུར་གྱི་ལས་འདི་ལྟ་བུ་མི་བྱའོ་ཞེས་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་བརྩོན་པ་ཤས་ཆེན་པོས་བསྒྲུབ་པར་བྱ་བ་དང་། ལྡོག་པར་བྱ་བ་དང་། ཇི་སྲིད་དུ་བཟོད་པར་བྱ་བ་ཞེས་བྱ་བ་ཐམས་ཅད་དུ་འདི་རྗེས་སུ་འབྲེལ་པར་རིག་པར་བྱའོ། །

[Block 317]
བྱས་ན་བཟོད་པར༌[^221]བྱའོ་ཞེས་བྱ་བ་ནི་ནན་ཏུར་གྱི་ལས་བྱས་པ་ལ། ཨེ་མའོ་དགེ་འདུན་གྱིས་འདི་ལ་བཟོད་པར་བྱ་ཞེས་བྱའོ།[^222] །སྤོ་བ་དང་གཞི་ནས་སྤོ་བར་བྱ་བ་དང་། མགུ་བར་བྱ་བ་དང་། གཞི་ནས་མགུ་བར་བྱ་བ་དང་། དབྱུང་བར་འདོད་པའི་གནས་ལ་ཨེ་མའོ་དགེ་འདུན་གྱིས་འདི་ལ་སྤོ་བ༌[^223]ལ་སོགས་པ་བཞི་པོ་སྦྱིན་པར་བྱ་ཞིང་དབྱུང་བར་འདོད་པ་ལ་ཨེ་མའོ་ཕྱུང་ཤིག༌[^224]ཅེས་བྱ་བའོ། །

[Block 318]
དེས་ཀྱང་འདི་ལ་དེ་བྱས་ཏེ༌[^225]ཞེས་བྱ་བ་ལ་དེས་ཀྱང་ཞེས་བྱ་བ་ནི་གནས་སོ། །

[Block 319]
དེ་ཞེས་བྱ་བ་ནི་ལྷུང་བཟེད་དང་ཆོས་གོས་ཀྱི་ལས་ལ་སོགས་པའོ། །

[Block 320]
འདི་ལ་ནི་གནས་པ་ལ་བྱའོ། །
--- END BLOCKS ---
