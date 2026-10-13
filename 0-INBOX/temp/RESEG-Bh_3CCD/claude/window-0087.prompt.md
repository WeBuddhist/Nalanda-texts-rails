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
[Block 3046]
གང་གི་ཕྱིར་ཕ་མ་མཉམ་པར་སྦྱོར་བའི་དུས་སུ་འཇུག་པས༌[^1984]སོགས་པའི་རླུང་གསུམ་གྱི་བདག་ཉིད་ཉེ་བར་སྡུད་པས་སེམས་ཅན་དེ་རྣམས་སྐྱེས་པའི་ཕྱིར་རོ། །

[Block 3047]
ཉིན་དང་མཚན་དུ་སྟོང་ཕྲག་ཉི་ཤུ་རྩ་གཅིག་དང་དྲུག་བརྒྱའི་རླུང་རྣམས་རྒྱུ་བ་སྟེ་ཟོ་ཆུན་བཞིན་ནོ། །

[Block 3048]
འདིས་ནི་འདོད་ཆགས་ཀྱི་ཆོས་རབ་ཏུ་བསྟན་པས་སྦས་པའི་དོན་གཉིས་པ༌[^1985]བཤད་དོ། །

[Block 3049]
ད་ནི་ཀུན་རྫོབ་ཀྱི་བདེན་པ་རྟགས་པར༌[^1986]བྱེད་པའི་མཚན་ཉིད་བདག་ལ་བྱིན་གྱིས་རློབ་པའི་རིམ་པ་བསྟན་པར་བྱ་བའི་ཕྱིར། ཡ། གང་ཞིག་ཅེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། སངས་རྒྱས་རྣམས་ཀྱིས༌[^1987]ནི་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་སྐུ་སྟེ་རྣམ་པའོ། །

[Block 3050]
དེ་འཇའ་ཚོན་བཞིན་དུ་གང་གིས་མཐོང་བ༌[^1988]དེ་མཚན་ཉིད་དོ། །

[Block 3051]
ཀུན་རྫོབ་ཅེས་པ་ནི་མྱུར་བའི་ཏིང་ངེ་འཛིན་གྱིས་བཞེངས་པའི་ཡེ་ཤེས་ཀྱི་སྐུའོ། །

[Block 3052]
དེའི་བདེན་པ་ནི་སྒྱུ་མ་བཅུ་གཉིས་ཀྱི་དཔེ་དང་འདྲ་བར་མཐོང་བའོ། །

[Block 3053]
དེ་ཉིད་རྫོགས་པའི་རིམ་པ་ཞེས་བཤད་པ་ཡིན་ཏེ། འོད་གསལ་བ་རྣམ་པར་དག་པས་སོ་ཞེས་པ་ནི་སེམས་རྣམ་པར་དག་པའི་རིམ་པས་ཐོབ་པའི་འོད་གསལ་བའི་དེ་ཁོ་ན་ཉིད་ལས་མྱུར་དུ་ཡང་དག་པར་བྱུང་བའི་ཕྱིར་རོ། །

[Block 3054]
བདག་ལ་བྱིན་གྱིས་རློབ་པའི་སྒྱུ་མ་དང་མཚུངས་ཤིང་འགྲོ་བའི་དོན་བྱེད་པ་ཡང་བསྟན་པར་བྱ་བའི་ཕྱིར། ཝཱཀ ་ཚིག་གི་ལམ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ།

[Block 3055 [VERSE]]
འདི་ནི་རང་བཞིན་ཡེ་ཤེས་སྐུ། །
ངག་གི་ལམ་གྱི་སྤྱོད་ཡུལ་ཡིན། །

[Block 3056]
ཞེས་པ་ནི་སྤྲུལ་པ་བཞིན་དུ་ཆོས་བསྟན་པ་ལ་བརྩོན་པའོ། །

[Block 3057]
སེམས་ཅན་ཀུན་ལ༌[^1989]ཕན་པའི་ཕྱིར། །ཞེས་པ་ནི་གྲོལ་བའི་གནས་ཐོབ་པར་བྱ་བའི་ཕྱིར་འཇའ་ཚོན་བཞིན་དུ་ནི་དབང་པོའི་གཞུ་དང་འདྲ་བར་སྣང་བ་སྟེ་གདུལ་བྱ་རྣམས་ཀྱིས་མཐོང་ངོ་། །མྱུར་བའི་རྣལ་འབྱོར་བསྟན་ནས་སྣང་བ་ཐོབ་པ་ལ་སོགས་པ་བསྟན་པའི་ཕྱིར། ཙིཏ། སེམས་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། སེམས་ནི་འཇུག་པའི་རྣམ་པར་ཤེས་པའོ། །

[Block 3058]
སེམས་ལས་བྱུང་བ༌[^1990]ནི་ཉོན་མོངས་པ་ཅན་གྱི་ཡིད་དོ། །

[Block 3059]
མ་རིག་པ་ནི་ཀུན་གཞི་རྣམ་པར་ཤེས་པའོ། །

[Block 3060]
དེ་རྣམས་ཀྱི་གོ་རིམས༌[^1991]བཞིན་དུ་ཤེས་རབ་དང་ཐབས་ཉེ་བར་ཐོབ་པ་སྟེ། མིང་གི་རྣམ་གྲངས་སོ། །

[Block 3061]
སྔགས་དང་ཕྱག་རྒྱའི་རིམ་པས་རྣམ་པར་ཤེས་པ་རྣམས་ལོག་པ་ན་དེ་ཉིད་སྣང་བ་དང་སྣང་བ་མཆེད་པ་དང་སྣང་བ་ཐོབ་པ་དང་སྟོང་པ་དང་ཤིན་ཏུ་སྟོང་པ་དང་སྟོང་པ་ཆེན་པོར་འགྱུར་རོ། །

[Block 3062]
དེ་ལྟར་གནས་པས་དབང་པོ་དམན་པའི་རྣལ་འབྱོར་པས་དང་པོ་འོད་གསལ་བ་ཉམས་སུ་མྱོང་ནས་དེའི༌[^1992]རྗེས་སུ་མཚམས་ཀྱི་སྣང་བ་དང་འདྲ་བའི་སྣང་བ་ཐོབ་པའི་ཡེ་ཤེས་མཐོང་ནས། དེའི་རྗེས་སུ༌[^1993]ཉི་མའི་སྣང་བ་དང་འདྲ་བའི་སྣང་བ་མཆེད་པའི་ཡེ་ཤེས་རྣམ་པར་རྟོགས་ཤིང་། དེ་ལས་ཀྱང་ཟླ་བའི་སྣང་བ་དང་འདྲ་བའི་སྣང་བའི་ཡེ་ཤེས་ངེས་པར་བྱས་ལ། ཐམས་ཅད་ཡོངས་སུ་གྱུར་པ་ལས་ཡེ་ཤེས་ཀྱི་སྐུ་རྫོགས་པར་འགྱུར་ཞེས་སྣང་བ་ཐོབ་པ་ལ་སོགས་པའི་རིམ་པས་བདག་བྱིན་གྱིས་རློབ་པ༌[^1994]གཉིས་པའོ། །

[Block 3063]
རིམ་པ་གསུམ་པ་ལ་གནས་པའི་སྤྱོད་པ་བསྟན་པར་བྱ་བའི་ཕྱིར། ཏ། རང་བཞིན་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། རང་བཞིན་ནི་འདོད་ཆགས་དང་བྲལ་བ་ལ་སོགས་པ་དང་། སྣང་བ་ནི་སྣང་བའི་ཡེ་ཤེས་ལ་སོགས་པ་རྣམས་ཀྱི་དབྱེ་བ་ཤེས་པ་སྟེ། རིམ་པ་གཉིས་པས་དེ་རྣམས་ལ་གོམས་པའི་ཕྱིར་རོ། །

[Block 3064]
དེ་ནས་སྤྱོད་པ་རབ་ཏུ་བྱ། །ཞེས་པ་ནི་སྐུའི་རྣམ་པ་ཐོབ་ནས་དཀྱིལ་འཁོར་དང་མཆོད་པ་དང་སྦྱིན་སྲེག་དང་བསྟོད་པ་ལ་སོགས་པའི་མཚན་ཉིད་སྤྱོད་ལམ་རྣམ་པ་བཞི་དག་ཏུ་གང་བྱེད་པ་དེ་དག་ཐམས་ཅད་སྒྱུ་མ་བཞིན་དུ་བྱའོ། །

[Block 3065]
དེ་བས་ན།

[Block 3066 [VERSE]]
སྒྱུ་མ་ལྟ་བུ་ཡོངས༌[^1995]ཤེས་པས། །
ལས༌[^1996]ཀྱི་ལུས༌[^1997]ནི་ཡོངས་སྤངས་ནས། །

[Block 3067]
ཞེས་པ་ནི་དགེ་བ་དང་མི་དགེ་བའི་ལས་དང་འབྲེལ་པའི་ལུས་པོ་ཡོངས་སུ་སྤངས་པས་རྡོ་རྗེའི༌[^1998]སྐུ་སྟེ། ཡེ་ཤེས་ཀྱི་རང་བཞིན་གྱི་སྐུ་ཉིད་ཐོབ་པར་འགྱུར་རོ། །

[Block 3068]
ལོངས་སྤྱོད་རྫོགས་པའི་སྐུའི་རང་བྱིན་གྱིས་བརླབ་པ་བསྟན་ནས། སྤྲུལ་པའི་སྐུའི་བདག་བྱིན་གྱིས་རློབ་པ༌[^1999]བསྟན་པའི་ཕྱིར། ཧྲི། ཐུགས་ལ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། དོན་སྤྱོད་པ་ནི་སེམས་ཅན་གྱི་དོན་ལ་སྤྱོད་པ་ནི་སྔོན་གྱི་སྨོན་ལམ་གྱི་བག་ཆགས་ལས་འབྱུང་བའི་འཇིག་རྟེན་པ་རྣམས༌[^2000]ནི་འཇིག་རྟེན་པ་དང་འདྲ་བའི་སྤྱོད་པ་ཐུགས་ལ་བཞག་ནས་སོ། །

[Block 3069]
ཀུན་རྫོབ་པ་ཡི་སྐུར་སྤྲུལ་ནས། །ཞེས་པ་ནི་དེ་བཞིན་གཤེགས་པ་དང་ལྷ་མོ་དང་བྱང་ཆུབ་སེམས་དཔའ་དང་། ཁྲོ་བོའི་བདག་ཉིད་ཅན་གྱི་དཀྱིལ་འཁོར་གྱི་འཁོར་ལོ་སྤྲོས་ཏེ། འདོད་པ༌[^2001]ལ་ཞེས་པ་ནི་འདོད་པའི་ཡོན་ཏན་ལྔ་ལ་ལོངས་སྤྱོད་ཅིང་སེམས་ཅན་གྱི་དོན་མཛད་ནས་བྱ་བ་བྱས་པར་འགྱུར་རོ། །

[Block 3070]
དེ་ཉིད་བསྟན་པར་བྱ་བའི་ཕྱིར། [^2002]ད། ཡིད་བཞིན་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། བདག་ལ་བྱིན་གྱིས་རློབ་པ་ལ་གནས་པའི་རྣལ་འབྱོར་པ་དེ་ཉིད་ཀྱིས་སེམས་ཅན་ཐམས་ཅད་ལ་མངོན་པར་འདོད་པའི་དོན་ཡིད་བཞིན་ནོར་བུ་ལྟར་སྟེར་བར་འགྱུར་རོ། །

[Block 3071]
སངས་རྒྱས་རྣམས་ཀྱི་ཕུན་ཚོགས་ཀྱང་། །ཞེས་པ་ནི་དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱི་སྦྱོར་བ་སྟེ། ཕྲ་བ་ལ་སོགས་པ་དང་བསྟན་པའི་ཆོ་འཕྲུལ་ལ་སོགས་པ་རྣམས་ཀྱང་སྟོབས་ཀྱིས་བླངས་ནས་སྤྱོད་པར་འགྱུར་བ་ནི་ནན་གྱིས་བདག་ཉིད་དུ་འཇོག་པར་བྱེད་དོ། །

[Block 3072]
དེ་ཉིད་ཀྱིས་ཐམས་ཅད་ཀྱི་དབང་ཕྱུག་ཉིད་བསྟན་པར་བྱ་བའི་ཕྱིར། ཡ། རྣལ་འབྱོར་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། རྣལ་འབྱོར་པའི་དབང་ཕྱུག་དེས། གང་དང་གང་འདོད་པ་ནི་བདེ་བ་ཉེ་བར་སྤྱོད་པ་ལ་སོགས་པ་འགལ་བའམ་མི་འགལ་བ་གང་འདོད་པ་དེ་དང་དེ་དག་སྒྲིབ་པ་མེད་ཅིང་མ་གོས་པའི་ངོ་བོ་ཉིད་ཀྱིས་བྱེད་པ་ནི་ཐམས་ཅད་སྤྱོད་པའོ། །

[Block 3073]
དེ་བས་ན། མཉམ་པར་མ་བཞག་རྣལ་འབྱོར་གྱིས། །ཞེས་བྱ་བ་སྨོས་ཏེ། བཞེངས་པ་དང་འདུག་པ་དང་། ཉལ་བ་དང་འཆག་པའི་སྦྱོར་བས་གནས་ན་ཡང་། རྟག་ཏུ་མཉམ་པར་གཞག་པར༌[^2003]གྱུར་པ༌[^2004]ནི་དུས་ཐམས་ཅད་དུ་རྩེ་གཅིག་པ་སྟེ། སྒྱུ་མ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་ལས་མི་གཡོ་བའི་ཕྱིར་རོ། །

[Block 3074]
ཇི་སྐད་དུ༌[^2005]འཕགས་པ་བྱམས་པས་ཀྱང་། །

[Block 3075 [VERSE]]
ཇི་ལྟ་ཇི་ལྟར་མངོན་གསུམ་སྣ་ཚོགས་སྤྱོད་ཡུལ་ལ། །
སྤྱོད་པ་ལ་གནས་སྙིང་རྗེའི་བདག་ཉིད་ཀྱིས་འཇུག་པ། །
དེ་དང་དེ་ལྟར་རིགས་པ་དང་མཚུངས་ཚིག་རྣམས་ཀྱིས། །
སེམས་ཅན་རྣམས་ལ་ཕན་ཕྱིར་མངོན་པར་འདུ་བྱེད་པའོ། །

[Block 3076]
ཞེས་འབྱུང་ངོ་། །སྒྱུ་མ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་ཉིད་ཀྱིས་སྙོམས་པར་འཇུག་པ་བསྟན་པར་བྱ་བའི་ཕྱིར། ཝ། རྡོ་རྗེ་པདྨ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། མཆོག་གི་བསྙེན་པ་ལ་སོགས་པའི་རིམ་པས་རྡོ་རྗེ་དང་པདྨ་མཉམ་པར་སྦྱོར་ཞིང་སྔོན་དུ་བཤད་པའི་ཡེ་ཤེས་གསུམ་གྱི་དབྱེ་བ་ཤེས་པར་འགྱུར་རོ། །

[Block 3077]
དེ་ཤེས་ནས་བདེ་བས་ནི་བདེ་བ་ཆེན་པོའི་ཏིང་ངེ་འཛིན་གྱིས་རྟག་ཏུ་གནས་པར་བྱའོ། །

[Block 3078]
བློ་ལ་གོས་དང་མ་གོས་པས་བྱ་བ་ནི། བློ་ལ་མ་གོས༌[^2006]པས་ནི་ཉོན་མོངས་པས་སོ། །

[Block 3079]
བློ་ལ༌[^2007]གོས་པས་ནི་འོད་གསལ་བས་སོ། །

[Block 3080]
དེ་ལྟར་འོད་གསལ་བའི་དེ་ཁོ་ན་ཉིད་ཀྱིས་ཁྱབ་པའི་སྒྱུ་མ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་བསྟན་ཏོ། །

[Block 3081]
འོད་གསལ་བ་ལ་གནས་པའི་རྣལ་འབྱོར་པས་སེམས་ཅན་གྱི་དོན་གྱི་བྱ་བ༌[^2008]བསྟན་པའི་ཕྱིར། ཛྲེ། སྒྱུ་མ་ལྟ་བུ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། རྣལ་འབྱོར་པ་དེས་སྒྱུ་མ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་གྱི་སྒོ་ནས་དངོས་པོ་ཐམས་ཅད་དང་སངས་རྒྱས་ཀྱི་བྱ་བ་ནི་བསྟན་པ་དང་། ཡོངས་སུ་སྨིན་པ་དང་། རྣམ་པར་གྲོལ་བ་ལ་སོགས་པ་བྱེད་པ་ནི་མཛད་པའོ། །

[Block 3082]
གཏན་ལ་དབབ་པའི་གཞི་ནི་གྲུབ་པའི་མཐའ་སྟེ། དེ་ཉིད་མི་འཕོ་བའི་ཕྱིར་གནས་པའོ། །

[Block 3083]
དེ་ལ་གནས་པ་ནི་ངལ་སོ་བའོ། །

[Block 3084]
རིམ་པ་གཉིས་པ༌[^2009]གོམས་པས་གསུམ་པ་ཐོབ་ནས་དེ་ཉིད་འདོར་བ༌[^2010]བྱེད་དོ༌[^2011]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3085]
བསྐྱེད་པའི་རིམ་པའི་རྣལ་འབྱོར༌[^2012]བཞི་ལས་ཁྱད་པར་བསྟན་པར་བྱ་བའི་ཕྱིར། ཡོ། རྣལ་འབྱོར་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། བསྐྱེད་པའི་རིམ་པ༌[^2013]རྣལ་འབྱོར་བཞི་སྟེ། གང་གིས་དང་པོའི་སྦྱོར་བ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཏིང་ངེ་འཛིན་འགྲུབ་པར་འགྱུར་རོ། །
--- END BLOCKS ---
