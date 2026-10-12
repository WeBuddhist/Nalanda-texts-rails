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
[Block 3501]
ཡང་འདོད་ཆགས་ནི་ཉོན་མོངས་པ་ཉིད་དོ། །

[Block 3502]
དོན་དེས་སྤོང་བ་སྟེ་གསལ་བའོ། །

[Block 3503]
མཆོག་ཏུ་དགའ་བ་ནི་འདོད་ཆགས་ཆེན་པོ་འོད་གསལ་བ་ཆེན་པོའི་རྒྱུ༌[^2246]མཐུན་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3504]
བྱང་ཆུབ་ཀྱི་སེམས་ཡིན་ལ་ཞེས་པ་ནི་ཀུན་རྫོབ་པའི་རྫས༌[^2247]ཀྱི་ཚུལ་ཅན་ཤུ་ཀྲའོ། །

[Block 3505]
དེ་ལས་བྱུང་བ་ནི་དམ་ཚིག་གི་དཀྱིལ་འཁོར་གྱི་རིམ་པས་རྫོགས་ཞེས་པའི་བར་དུའོ། །

[Block 3506]
དྲང་བའི་དོན་ནི་དཀྱིལ་འཁོར་རྒྱལ་བ་མཆོག་བརྗོད་པར་འདོད་པའི་ཕྱིར་རོ། །

[Block 3507]
འོད་གསལ་བ་སྟེ་ཞེས་པ་ནི་མངོན་པར་བྱང་ཆུབ་པའོ། །

[Block 3508]
དེ་ལས་བྱུང་བ་ནི་ཟུང་དུ་འཇུག་པའི་ཏིང་ངེ་འཛིན་དེ་ལས་བྱུང་བའི་ཕྱིར་རོ། །

[Block 3509]
ངེས་པའི་དོན་ནི་ཡང་དག་པའི་དོན་བསྟན་པས་སོ། །

[Block 3510]
སོ་སོར་རྟོག་པའི་ཡེ་ཤེས་ལ་ཀུན་དུ་ཆགས་པ་ཞེས་པ་ནི་སྣང་བ་མཐའ་ཡས་དེའི་ངོ་བོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3511]
རོ་ནི་འཁོར་བའོ་ཞེས་པ་ནི་རོའི༌[^2248]སྒྲའི་དོན་ཏོ་ཞེས་འབྱུང་བས་སྒྲའི་རྣམ་པར་རྟོག་པའི་ངོ་བོ་ནི་འཁོར་བ་ཡིན་པས་སོ། །

[Block 3512]
ལྀཀ་ཅེས་པ་ནི་སོ་སོར་རྟོག་པའི་ཡེ་ཤེས་ཀྱིས༌[^2249]འཁོར་བ་ལས་འདས་པའི་ཕྱིར་རོ། །

[Block 3513]
དྲང་བའི་དོན་ནི་མི་མཐུན་པའི་ཕྱོགས་དང་གཉེན་པོའི་ཕྱོགས་ཀྱི་ལམ་རྗོད་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 3514]
རོ་ཞེས་པ་ནི༌[^2250]ཡེ་ཤེས་གསུམ་སྟེ། ར་ཨ་ཨོའོ། །

[Block 3515]
དེ་ལ་ར་ནི་ཆགས་པ་སྟེ་སྣང་བ་མཆེད་པའོ།[^2251] །

[Block 3516]
ཨ་ནི་འདོད་ཆགས་དང་བྲལ་བ་སྟེ་སྣང་བའོ། །

[Block 3517]
ཨོ་ནི་འདོད་ཆགས་བར་པ་སྟེ་སྣང་བ་ཐོབ༌[^2252]པའོ། །

[Block 3518]
གཅིག་ཏུ་བསྡུས་པ་ལས་སྣང་བ་མཆེད་པ་ལ་སོགས་པ་ཡེ་ཤེས་གསུམ་བཤད་དོ། །

[Block 3519]
དེ་ལས་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། ཡེ་ཤེས་གསུམ་ལ་ཉེ་བར་དམིགས་ཏེ་སླར་ཡང་འོད་གསལ་བ་ལ་འཇུག་པར་བྱའོ། །

[Block 3520]
ངེས་པའི་དོན་ནི་ཡང་དག་པའི་དོན་བསྟན་པས་སོ། །

[Block 3521]
དོན་ཡོད་པར་གྲུབ་པ་ཞེས་པ་ནི་ལས་ཐམས་ཅད་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3522]
བྱ་བ་གྲུབ་པའི་ཡེ་ཤེས་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱི་སེམས་ཅན་གྱི་དོན་ཁོ་ན་དམ་ཚིག་གོ། །

[Block 3523]
དྲང་བའི་དོན་ནི་སེམས་ཅན་གྱི་དོན༌[^2253]བྱེད་པའི་མཚན་ཉིད་ཅན་ལས་ཀྱི་རྒྱལ་བ་མཆོག་བརྗོད་པར༌[^2254]འདོད་པའི་ཕྱིར་རོ། །

[Block 3524]
འོད་གསལ་བ་ནི་བཞི་པའོ། །

[Block 3525]
མཚན་མ་མེད་པའི་འབྲས་བུ་སྟེར་བ་ཞེས་པ༌[^2255]ལ། ལྷུན་གྱིས་གྲུབ་པ་ཉིད་ཀྱིས་བྱང་ཆུབ་ཀྱི་མཚན་ཉིད་ཅན་གྱི་འབྲས་བུ་མངོན་པར་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 3526]
ངེས་པའི་དོན་ནི་ཡང་དག་པའི་དོན་སྟོན་པས་སོ། །

[Block 3527]
ཉོན་མོངས་པ༌[^2256]དམ་ཚིག་ཉམས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་ཕྲག་དོག་ཅན་རྣམས་ཀྱི་དམ་ཚིག་ཉམས་པ་ནི་སླར་ཡང་དོན་ཡོད་པར༌[^2257]གྲུབ་པའི་བསྒོམ་པས༌[^2258]བཟློག་པའི་ཕྱིར་རོ། །

[Block 3528]
སོགས་པའི་སྒྲས་མཆོད་པ་ཆགས་པ་ལ་སོགས་པ་གཟུང་ངོ་། །དྲང་བའི་དོན་ནི་སྔ་མ་བཞིན་དུ་བསྐྱེད་པའི་རིམ་པའི་བསྒོམ་པ་བརྗོད་པར་འདོད་པས་སོ། །

[Block 3529]
ཁམས་ཕྲ་བ་སྟེ་ཞེས་ཤེས་པ་ནི་འོད་གསལ་བའོ། །

[Block 3530]
དེས་ཤེས་པ་ནི་རྒྱུའི་གསུམ་པ་སྟེ། དེས་ཐབས་ཀྱི་ཡེ་ཤེས་དགུག་པ་ནི་སྣང་བ་མཆེད་པའི་ཡེ་ཤེས་བསྐྱེད་ནས། དེའི་རྗེས་སུ་མཆོག་ཏུ་དགའ་བ་ནི་བདེ་བ་ཆེན་པོ་བསྐྱེད་ལ་ཡོངས་སུ་སྦྱང་བའི་རིགས་ནི་འདོད་ཆགས་ལ་སོགས་པ་རང་བཞིན༌[^2259]ཐམས་ཅད་སྦྱོང་བར་བྱེད་པའི་རིགས་ཞེས་བྱ་བའི་བར་རོ། །

[Block 3531]
ངེས་པའི་དོན་ནི་རིམ་པ༌[^2260]

[Block 3532]
གཉིས་པ་བསྟན་པས་སོ། །

[Block 3533]
རབ་ཏུ་རྣམ་པར་འབྱེད་པའི་མཚན་ཉིད་ནི་ཤེས་རབ་སྟེ་ཞེས་པ་ལ་བྱ་བ་ནན་ཏན་གྲུབ་པའི་ཡེ་ཤེས་ཀྱི་བདག་ཉིད་ཅན་རྣམ་པར་རྟོག་པ་བླ་ན་མེད་པའི་བློ་སྟེ་ཤེས་རབ་པོ། །དྲང་བའི་དོན་ནི་བསྒོམ་པའི་ཤེས་རབ་ཀྱིས༌[^2261]རང་བཞིན་ཡིན་པས་སོ། །

[Block 3534]
ཟླ་བ་ལྟར་སྣང་བ་སྟེ་ཞེས་པ་ནི་སྣང་བའི་ཡེ་ཤེས་སོ། །

[Block 3535]
དེ་ཡང་ཉེ་བར་མཚོན་པ་ཡིན་ཏེ། ཉི་མའི་སྣང་བ་དང་མཚམས་ཀྱི་སྣང་བའོ། །

[Block 3536]
ཁམས་ཕྲ་བར༌[^2262]འཛིན་པར་མཛད་པས་ན། [^2263]ཞེས་པ་ལ། འོད་གསལ་བ་ལ་འཇུག་པར་བྱེད་དོ། །

[Block 3537]
ངེས་པའི་དོན་ནི་སེམས་རྣམ་པར་དག་པ་བརྗོད་པར་འདོད་པའི་ཕྱིར་རོ། །

[Block 3538]
བྱང་ཕྱོགས་སུ་བཞུགས་སོ་ཞེས་པ་ལ་སོགས་པ་ནི་སྔ་མ་བཞིན་ནོ། །

[Block 3539]
ཞེ་སྡང་ཞེས་བྱ་བ་ལ་སོགས་པས་ཞེ་སྡང་ལ་སོགས་པ་ཉོན་མོངས་པ་རྣམ་པར་དག་པའི་ངོ་བོ་དེ་བཞིན་གཤེགས་པ་ལྔ་ཡིན་ཞེས་ཉེ་བར་སྡུད་པ༌[^2264]བསྟན་ཏོ། །

[Block 3540]
གདུལ་བྱ་རྣམས་ཀྱི་ཐར་པའི་མངོན་པར་འདོད་པ་ཞེས་བྱ་བ་ལ་སོགས་པས་འདོད་པ་དང་ཐར་པ་དག་གི་ལམ་དང་འབྲས་བུའི་བྱེ་བྲག་བསྟན་ཏོ། །
--- END BLOCKS ---
