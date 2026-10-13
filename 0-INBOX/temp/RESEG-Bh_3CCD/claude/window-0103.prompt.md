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
[Block 3606]
རྨོངས་པའི་མུན་པ་སྟེ་ཞེས་པ་ནི་ཀུན་གཞི་རྣམ་པར་ཤེས་པའི་ངོ་བོ་ཉིད་དོ། །

[Block 3607]
མ་རིག་པ་ནི་དེའི་ཁྱད་པར་རོ། །

[Block 3608]
དོན་དམ་པའི་བདེན་པ་ཤེས་པ་ནི་ཕྱག་རྒྱ་དང་སྔགས་ཀྱིས་ཐོབ་པར་བྱ་བའི་སེམས་རྣམ་པར་དག་པའི་མཚན་ཉིད་ཅན་གྱི་འོད་གསལ་བས་སོ། །

[Block 3609]
ངེས་པའི་དོན་ནི་སེམས་རྣམ་པར་དག་པ་ཉིད་བསྟན་པས་སོ། །

[Block 3610]
སྒྲ་ཇི་བཞིན་པ་ནི་སྔ་མ་བཞིན་ནོ། །

[Block 3611]
རིན་ཆེན་འབྱུང་ལྡན་ཞེས་པ་ནི་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་ནང་ན་ཆོས་ཀྱི་རྒྱལ་སྲིད་ཀྱི་བདག་པོའི་མཚན་ཉིད་ཀྱིས་མངོན་པར་བྱང་ཆུབ་ཐོབ་པའི་ཕྱིར་དང་ནམ་མཁའ་མཛོད་ཀྱི་ཏིང་ངེ་འཛིན་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 3612]
དེའི་ཅོད་པན་དུ་རྡོ་རྗེ་གང་ལ་ཡོད་པ་ཞེས་པ་ནི་འཕགས་པ་གཞན་གྱིས་མི་ཐུབ་པ་ནི་རིན་ཆེན་འབྱུང་ལྡན་གྱི་རིགས་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3613]
དྲང་བའི་དོན་ནི་ཤེས་རབ་མཐར་བྱེད་ཀྱི་བསྐྱེད་པའི༌[^2281]རིམ་པ་ཙམ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 3614]
འོད་གསལ་བ་ཞེས་པ་ནི་རིམ་པ་གཉིས་པས་ཐོབ་པར་བྱ་བ་དེ་ཁོ་ན་ཉིད་དོ། །

[Block 3615]
ངེས་པའི་དོན་ནི་རྫོགས་པའི་རིམ་པ་བརྗོད་པས་སོ། །ཤེས་རབ་ཀྱིས་ནི་མཐོང་བ་དང་བསྒོམ་པའི་ལམ་གྱི་མཚན་ཉིད་ཀྱི་བློས་སོ། །

[Block 3616]
ཉོན་མོངས་པ་ཞེས་པ་ནི་ཁམས་གསུམ་ལ་གནས་པའི་འདོད་ཆགས་ལ་སོགས་པའོ། །

[Block 3617]
དེ་ལ་མདོར་བསྡུས་པ་ནི་འདིར་བདེན་པ་བཞི་པོ་ལ་བརྟེན་ཏེ། ཉོན་མོངས་པ་སྤོང་བར་བྱེད་པ་ཡིན་ཏེ། དེ་ལ་སྡུག་བསྔལ་གྱི་བདེན་པ་ལ་བརྟེན་ཏེ། མཐོང་བའི་ལམ་གྱི་ཉོན་མོངས་པ༌[^2282]བཅུ་སྤོང་བ་ཡིན་ཏེ། འདི་ལྟ་སྟེ། འདོད་ཆགས་དང་། ཁོང་ཁྲོ་དང་། གཏི་མུག་དང་། ང་རྒྱལ་དང་། ཐེ་ཚོམ་དང་ལྔའོ། །

[Block 3618]
ལྟ་བ་ཡང་རྣམ་པ་ལྔ་ཡིན༌[^2283]ཏེ། འཇིག་ཚོགས་ཀྱི་ལྟ་བ་དང་། མཐར༌[^2284]འཛིན་པའི་ལྟ་བ་དང་། ལོག་པར་ལྟ་བ་དང་། ལྟ་བ་མཆོག་ཏུ་འཛིན་པ་དང་། ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་མཆོག་ཏུ་འཛིན་པའི་ལྟ་བའོ། །

[Block 3619]
ཀུན་འབྱུང་གི་བདེན་པ་ལ་བརྟེན་པ་བདུན་སྤང་བར་བྱ་སྟེ། འཇིག་ཚོགས་ཀྱི་ལྟ་བ་དང་། མཐར༌[^2285]འཛིན་པའི་ལྟ་བ་དང་། ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་མཆོག་ཏུ་འཛིན་པའི་ལྟ་བ་མ་གཏོགས་པས་སོ། །

[Block 3620]
འགོག་པའི་བདེན་པ་ལ་བརྟེན་ཏེ་བདུན་པོ་དེ་ཉིད་དོ། །

[Block 3621]
ལམ་གྱི་བདེན་པ་ལ་བརྟེན་ཏེ་མཐོང་བའི་ལམ་གྱིས་སྔར་བཤད་པའི་ཉོན་མོངས་པ་བདུན་དང་། ཚུལ་ཁྲིམས་དང་། བརྟུལ་ཞུགས་མཆོག་ཏུ་འཛིན་པའི་ལྟ་བ་སྟེ་སྤང་བར་བྱ་བའོ། །

[Block 3622]
བསྒོམ་པས་སྤང་བར་བྱ་བ་ནི་བཞི་སྟེ། འདོད་ཆགས་དང་། ཁོང་ཁྲོ་དང་། ང་རྒྱལ་དང་། མ་རིག་པའོ། །

[Block 3623]
དེ་ལྟར་འདོད་པའི་ཁམས་སུམ་ཅུ་རྩ་དྲུག་ཉོན་མོངས་པ་སྤང་བར་བྱ་བ་ཡིན་ནོ། །

[Block 3624]
དེ་བཞིན་དུ་ནི་གཟུགས་དང་གཟུགས་མེད་པའི་ཁམས་སུ་ཁོང་ཁྲོ་བཅུ་མ་གཏོགས་པར༌[^2286]དགུ་བཅུ་རྩ་བརྒྱད་དུ་འགྱུར་རོ། །

[Block 3625]
གཅིག་ཏུ་བསྡུས་ཏེ། མཐོང་བའི་ལམ་གྱིས་བརྒྱད་ཅུ་རྩ་བརྒྱད་སྤང༌[^2287]བ་དང་། བཅུ་ནི་བསྒོམ་པའི་ལམ་གྱིས་སྤང་བར་བྱའོ། །

[Block 3626]
གང་ཡང་ཉོན་མོངས་པའི་ཆོས་གཞན་རྣམས་འདུ་བྱེད་ཀྱི་ཕུང་པོར་འདུས་པ་དེ་དག་ཉེ་བའི་ཉོན་མོངས་པ་ཁོ་ན་ཡིན་ཏེ། དེ་དག་གང་ཞེ་ན། སྒྱུ༌[^2288]དང་། རྒྱགས་པ་དང་། རྣམ་པར་འཚེ་བ་དང་། འཚིག་པ་དང་། ཁོན་དུ་འཛིན་པ་དང་། གཡོ་ལ་སོགས་པ་རྣམ་པ་དུ་མའོ། །

[Block 3627]
བཅུ་ནི་ཀུན་དུ་སྦྱོར་བ་སྟེ། ངོ་ཚ་མེད་པ་དང་། ཁྲེལ་མེད་པ་དང་། ཕྲག་དོག་དང་། སེར་སྣ་དང་། རྒྱགས་པ་དང་། འགྱོད་པ་དང་། གཉིད་དང་། རྨུགས་པ་དང་། ཁྲོ་བ་དང་། འཆབ་པ༌[^2289]དང་། བཅུའོ། །

[Block 3628]
ཉོན་མོངས་པ་དེ་དག་ནི་ཟག་པའི་སྒྲས་བཤད་པའོ། །

[Block 3629]
དེ་ལ་ཟག་པ༌[^2290]གསུམ་དུ་འགྱུར་ཏེ། འདོད་པའི་ཟག་པ་དང་། སྲིད་པའི་ཟག་པ་དང་། མ་རིག་པའི་ཟག་པའོ། །

[Block 3630]
དེ་ལ་འདོད་པའི་ཁམས་སུ་སོང་བའི་ཉོན་མོངས་པ་ནི་མ་རིག་པ་རྣམ་པ་ལྔ་མ་གཏོགས་པར་རྫས་སུམ་ཅུ་རྩ་གཅིག་གི་ངོ་བོ་ནི་འདོད་པའི་ཟག་པའོ། །

[Block 3631]
དེ་བཞིན་དུ་ཡང་གཟུགས་དང་གཟུགས་མེད་པ་ན་གནས་པའི་ཉོན་མོངས་པ་ནི་མ་རིག་པ་རྣམ་པ་བཅུ་མ་གཏོགས་པར་རྫས་ལྔ་བཅུ་རྩ་གཉིས་ཀྱི་ངོ་བོ་སྲིད་པའི་ཟག་པའོ། །

[Block 3632]
ཁམས་གསུམ་པའི་མ་རིག་པ་ནི་རྫས་བཅོ་ལྔའི་བདག་ཉིད་ཅན་ནི་མ་རིག་པའི་ཟག་པའོ། །

[Block 3633]
དམིགས་པ་དང་ཡང་དག་པར་སྦྱོར་བ་དག་ནི་རྗེས་སུ་འགྲོ་བས་ན་ཉོན་མོངས་པའོ། །

[Block 3634]
སྲིད་པའི་རྩེ་མོ་ནས་མནར་མེད་པའི་བར་དུ་སྐྱེ་མཆེད་དྲུག་གི་རྨ་ནས་ཀུན་དུ་འཁོར་བར་ཟག་པར་བྱེད་པས་ན་ཟག་པའི་དོན་ཏོ། །

[Block 3635]
ཆུ་བོ་བཞི་སྟེ། འདོད་པ་དང་། སྲིད་པ་དང་། ལྟ་བ༌[^2291]དང་། མ་རིག་པ་ཞེས་པའོ། །

[Block 3636]
དེ་ལ་འདོད་པའི་ཟག་པ༌[^2292]ཁོ་ན་འདོད་པའི་ཆུ་བོའོ། །

[Block 3637]
སྲིད་པའི་ཟག་པ་ཉིད་ནི་སྲིད་པའི་ཆུ་བོ་སྟེ། ལྟ་བ་རྣམས་མ་གཏོགས་པའོ། །

[Block 3638]
ཁམས་གསུམ་པའི་ལྟ་བ་དག་ནི་ལྟ་བའི་ཆུ་བོ་སྟེ་རྫས་སུམ་ཅུ་རྩ་དྲུག་གོ། །

[Block 3639]
མ་རིག་པའི་ཟག་པ་ཉིད་ནི། མ་རིག་པའི་ཆུ་བོ་སྟེ་ཁྱེར་བར་བྱེད་པས་སོ། །

[Block 3640]
བཞི་པོ་དེ་ཉིད་ནི་སྦྱོར་བ་བཞི་སྟེ། སྦྱོར་བར་བྱེད་པས་ན་སྦྱོར་བའི་དོན་ཏོ། །

[Block 3641]
ལེན་པ་ནི་བཞི་སྟེ། འདོད་པ་དང་། ལྟ་བ་དང་། ཚུལ་ཁྲིམས་དང་། བརྟུལ་ཞུགས་མཆོག་ཏུ་འཛིན་པ་དང་། བདག་ཏུ་སྨྲ་བའི་ལེན་པའོ། །

[Block 3642]
དེ་ལ་འདོད་པའི་ལེན་པ་ནི་རྫས་ཉི་ཤུ་རྩ་བཞིའོ། །

[Block 3643]
གཟུགས་དང་གཟུགས་མེད་པ་ན༌[^2293]གནས་པའི་ཉོན་མོངས་པ་ནི་བདག་ཏུ་ལྟ་བའི་ལེན་པ་སྟེ། རྫས་སུམ་ཅུ་རྩ་བརྒྱད་དོ། །

[Block 3644]
ལྟ་བའི་ལེན་པ་ནི་རྫས་སུམ་ཅུའོ། །

[Block 3645]
ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་ལེན་པ་ནི་རྫས་སུ༌[^2294]དྲུག་གོ། །
--- END BLOCKS ---
