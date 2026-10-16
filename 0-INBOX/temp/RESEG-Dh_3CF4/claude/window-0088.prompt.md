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
[Block 3081]
མ་བསྒྲིབས་ཀྱང་ཞེས་བྱ་བ་ནི་གོམས་པར་བྱས་པའི་ཕྱིར་ཏེ། རྨི་ལམ་གྱི་ནང་བཞིན་དུ་སྟོན་པའི་ཕྱིར་རོ། །

[Block 3082]
བྱམས་པ་ཞེས་བྱ་བ་འདིས་ནི་བསམ་པ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 3083]
སྦྱིན་པ་དང་། ཚིག་འཇམ་པོ་དང་། དོན་སྤྱོད་པ་ལ་སོགས་པའི་རིམ་པས་རབ་ཏུ་ཕན་འདོགས་པར་འགྱུར་རོ་ཞེས་བྱ་བ་འདིས་ནི་སྦྱོར་བ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 3084]
འདིར་ཇི་ལྟར་བསྡུ༌[^1953]བའི་དངོས་པོ་བཞིས་ཕན་འདོགས་པའི་དོན་ཡིན་ཞེ་ན། མཐུན་པར་བདག་དང་གཞན་ལ་ཕན་འདོགས་པར་འཇུག་པ་ནི་འདི་དག་གི་བསྡུས་པའི་དོན་ཏེ། འདིར་ནི་གཞན་ལ་ཕན་འདོགས་པ༌[^1954]རང་འཇུག་པ་འབའ་ཞིག་གི་དབང་དུ་བྱས་པའོ། །

[Block 3085]
རིམ་པ་ཞེས་སྨོས་པ་ནི་འདུལ་བའི་སྐྱེ་བོ་ལ་སྔོན་དུ་སྦྱིན་པར་བྱ་བ་ཡིན་ནོ། །

[Block 3086]
དེ་ནས་ཚིག་འཇམ་པོས་ཡང་དག་པར་བསྟན་ཅིང་ཡང་དག་པར༌[^1955]གཟེངས་བསྟོད་པར་བྱའོ། །

[Block 3087]
དེའི་འོག་ཏུ་རབ་ཏུ་ཞུགས་པར་གྱུར་པ་རྣམས་ལ་དོན་སྤྱོད་པས་གང་དུ་དེ་འཛིན་དུ་བཅུག་ཅིང་དེའི་གྲོགས་བྱེད་པ་ཡིན་ཏེ། བསྡུ་བའི་དངོས་པོ་དེའི་རིམ་པ་ནི་འདི་ཡིན་ནོ། །

[Block 3088]
དེས་ན༌[^1956]བྱང་ཆུབ་སེམས་དཔའི་ཕན་འདོགས་པ་ཁྱད་པར་དུ་གྱུར་པའོ། །

[Block 3089]
ཐབས་ལ་མཁས་པ་ནི་ཤེས་རབ་ཀྱིས་སོ། །

[Block 3090]
རིགས་པས་ཞེས་བྱ་བ་ནི་བརྩོན་འགྲུས་ཀྱིས་སོ། །

[Block 3091]
དེ་གཉིས་ཀྱིས་ནི་རྟག་ཏུ་བྱེད་པ་དང་གུས་པར་བྱེད་པ་བསྟན་ཏོ། །

[Block 3092]
ཉ་རྣམས་ཀྱི་ཆོས་ཀྱི་ཚུལ་ནི་ཉ་ཟ་བར་བྱེད་པའོ། །

[Block 3093]
ཉའི་རིགས་དེས༌[^1957]ལེགས་པར་བསྐྱངས་བས་རབ་ཏུ་དར་ཞིང་རྒྱས་པ་ཡིན་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། གནོད་པ་མེད་པའི་ཕྱིར་རོ། །ཇི་ལྟ་བུར་ཞེ་ན། མིའི་བདག་པོས་ཚུལ་བཞིན་སྤྱོད་པས་ཡོངས་སུ་བསྐྱངས་པ་ནི༌[^1958]འབངས་རྣམས་གནོད་པ་མེད་པ༌[^1959]བཞིན་ནོ། །

[Block 3094]
སྐལ་བ་མེད་པར་གྱུར་པ་ཞེས་བྱ་བས་ནི་རྒྱུ་མ་ཚང་བར་སྟོན་ཏོ། །

[Block 3095]
ཆར་འབེབས་པའི་ལྷའི་བུ་བག་མེད་པ་ཞེས་བྱ་བས་ནི་རྐྱེན་མ་ཚང་བར་སྟོན་ཏེ༌[^1960]རྒྱུ་དང་རྐྱེན་རྣམ་པ་གཉིས༌[^1961]ནི་དངོས་པོ་ཐམས་ཅད་འབྱུང་བ་ཡིན་ཏེ་གཞན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 3096]
ངལ་ཞིང་ལེ་ལོའི་དབང་གིས་བུལ་བར་གྱུར་པ་འདྲ་བའི་ཞེས་བྱ་བ་ནི༌[^1962]ཉི་མ་རིང་ཞིང་སོ་གའི་དུས་སུ་འགྲོས་བུལ་བའི་ཕྱིར་རོ། །

[Block 3097]
ཇི་ལྟར་འཇིག་རྟེན་པ་རྣམས་ངལ་བ་དང་ལེ་ལོའི་དབང་དུ་གྱུར་ན་མྱུར་དུ་འདའ་བར་བྱེད་མི་ནུས་སོ། །

[Block 3098]
དེ་བཞིན་དུ་ཉི་མའི་དཀྱིལ་འཁོར་ཡང་དེ་ལྟ་བུས་འཇུག་པའི་ཕྱིར་རོ། །

[Block 3099]
དེས་ན་ཡང་སྐོམ་པའི་དབང་གིས་ཉིན་རེ་བཞིན་འཐུང་བ༌[^1963]བཞིན་དུ་ཞེས་བྱ་བ་ནི་ས་དང་ཀླུང་གཉིས་ལ་ཉི་མའི་འོད་ཀྱིས་གདུངས་པའི་དྲོད་ཀྱིས་སོ། །

[Block 3100]
ཚ་བ་དང་སྐོམ་པའི་དབང་གིས་བསིལ་བ༌[^1964]འདོད་པས་ཉིན་རེ་ཞིང་འཐུངས་པ་བཞིན་དུ༌[^1965]ཞེས་བྱ་བ་དེ་ཉིད་བསྒྲུབ་པའི༌[^1966]ཕྱིར། དཔྱིད་ཀྱི་དུས་ཀྱི་ཉི་མ་འབར་བ་དང་། །ཞེས་བྱ་བའི་ཚིགས་བཅད་དེ་སྔར་སྨོས་པའི་ཚིག་རྐང་གི་དོན་འདིས་སྟོན༌[^1967]ཏེ། རྒྱུ་འདི་གསུམ་གྱིས་ཆུ་སྐམ་པར་འགྱུར་གྱི་གཞན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 3101]
ཁྭ༌[^1968]རྣམས་ཀྱང་ཞེས་བྱ་བ་ནི་ཆུ་ལས་རིང་དུ་སྤྱོད་པའོ། །

[Block 3102]
ཆུ་ཡང་ཉིན་རེ་ཞིང་ཞེས་བྱ་བ་དང་། བྲོས་ཏེ་འགྲོ་བའི་ལམ་ཡང་མེད། །ཅེས་བྱ་བའི་ཚིགས་བཅད་ཀྱིས་ནི་ཉ་རྣམས་རྣམ་པར་འཇིགས་པའི༌[^1969]རྒྱུ་མ་ལུས་པར་བསྟན་ཏེ། རྒྱུ་གསུམ་གྱིས་དགྲ་ལས་ཐར་པར་མི་འགྱུར་བ་ཡིན་ཏེ། དགྲ་རྣམས་སྟོབས་ཆེ་ཞིང་དེའི་གནས་ན་འདུག་པ་དང་། དེ་མེད་ཀྱང་ཡུལ་གཞན་དུ་འགྲོ་བར་མི་ནུས་པ་དང་། དེ་མེད་ཀྱང་དགྲ་དང་ཉེ་བར་གནས་པ་སྟེ། རྒྱུ་འདི་གསུམ་ཡོད་པས་གདོན་མི་ཟ་བར་ཉ་རྣམས་འཇིགས་པའི་རྒྱུར་སྟོན་ཏོ། །

[Block 3103]
དགྲ་རྣམས༌[^1970]སྟོབས་ཆེ་ཞིང་། གནས་ན་འདུག་པས་སྐྱབས་མེད་པའི་དབང་དུ་བྱས་ནས། ཆུ་ཡང་ཉིན་རེ་བྲི་བར་གྱུར། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ཏེ། སྔར་གནས་པའི་ཆུ་ཟད་པ་དང་། ཆུ་ཕྱི་མ་མ་བྱུང་བས་སོ། །

[Block 3104]
ཚིགས་བཅད་གཉིས་པས་ནི་དེ་ཡུལ་གཞན་དུ་འགྲོ་མི་ནུས་པ་དང་། དགྲ་དང་ཉེ་བར་གནས་པར་བསྟན་ཏོ། །

[Block 3105]
ཡུལ་གཞན་དུ་འགྲོ་བར་མི་ནུས་པའི་རྒྱུ་ནི་གཉིས་ཏེ། རང་གི་སྐྱེས་བུའི་བྱེད་པའམ། གཞན་གྱི་དཔུང་སྟེ་གཉི་ག༌[^1971]མེད་པའོ། །

[Block 3106]
བདག་ཅག་བརླག་པར་དགའ་བའི་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཕྱེད་ཀྱིས་ནི༌[^1972]དགྲ་དང་ཉེ་བར་གནས་པ་སྟོན་ཏོ། །

[Block 3107]
ནག་པོའི་སྤྲིན་རྣམས་རི་བོའི་གྲིབ་མ་བཞིན། །ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་ལྔ་ནི་ཆར་འབབ་པའི་རྟགས་ཀྱི་དབང་དུ་བྱས་པ་དང་། ཆར་འབབ་པའི་དབང་དུ་བྱས་པ་སྟེ། ཆར་འབབ་པའི༌[^1973]རྟགས་ཀྱི་དབང་དུ་བྱས་ནས། ནག་པོའི་སྤྲིན་རྣམས་རི་བོའི་གྲིབ་མ་བཞིན། །ཞེས་བྱ་བའི་ཚིགས་བཅད་དང་། འབྲུག་གི༌[^1974]རྔ་སྒྲས་རབ་ཏུ་དགའ་གྱུར༌[^1975]ནས། །ཞེས་བྱ་བ་དང་། དེ་ཡིས་ཆར་ཕབ་མུ་ཏིག་གཏོར་བ་ཞེས་བྱ་བ་འདི་དག་ནི་ཆར་ཕབ་པའི་རྟགས་བསྟན་ཏོ། །

[Block 3108]
འབྲུག་གི་རྔ་སྒྲ་བཞིན་དུ་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་དག༌[^1976]གོ་རིམས་བཞིན་དུ་གནས་པ་ཡིན་ཏེ། དེའི་གོ་རིམས་ནི་རྨ་བྱ་རབ་དགའ་ཟེ་བ་འབྲེལ་པ་ཞེས་བྱ་བའི་འོག་ཏུ་འདི་བྲི་བར་བྱའོ། །

[Block 3109]
དེའི༌[^1977]ཆར་འབབ་པའི་དུས་ཀྱི་རྟགས་ནི་རྣམ་པ་ལྔ་སྟེ། སྤྲིན་ལངས་པ་དང་། འབྲུག་ཟེར་བ་དང་། གློག་དང་། ཆར་དང་། རླུང་སྟེ། གོ་རིམས་ཇི་ལྟ་བ་བཞིན་སྦྱར་བར་བྱའོ། །

[Block 3110]
བབ་པའི༌[^1978]དབང་དུ་བྱས་ན་ནི་དཔྱིད་ཀྱི་དུས་ལ་བབ་པར་རྣམ་པར་སྤེལ་ཀྱང་། དཔྱིད་ཀྱི་དུས་ཀྱི་ཚ་བ་ཉེ་བར་ཞི་བ་སྟེ། ཆར་བབ་པས་སོ། །

[Block 3111]
དཔྱིད་ཀྱི་དུས་ལ་བབ་པས་ཞེས་བྱ་བ་འདིས་ནི་ཆར་བབ་པར་བྱེད་པ་བསྟན་ཏོ། །

[Block 3112]
འདི་ཉིད་སྔར་བསྟན་པའི་རྟགས་ཉིད་ལ་འཇུག་པར་འདོད་པ་ཡིན་ཏེ་དེ་བསྟན་པའི་ཕྱིར། ཆར་སྤྲིན་འབྲུག་སྒྲ་ཟབ་ཅིང་བརྟན།[^1979] །ཞེས་སྨོས་ཏེ། ཆར་སྤྲིན་འབྲུག་སྒྲ་ཞེས་བྱ་བ་འདིས་ནི་སྤྲིན་དང་འབྲུག་སྒྲ་ཉིད་བསྟན་ཏོ། །

[Block 3113]
ཆར་པའི་རྒྱུན༌[^1980]རྣམས་ཞེས་བྱ་བ་འདིས་ནི་ཆར་བསྟན་ཏོ། །

[Block 3114]
གློག་འགྱུ༌[^1981]འབར་བ་ཞེས་བྱ་བ་འདིས་ནི་གློག་བསྟན་ཏོ། །ཅིའི་ཕྱིར་རླུང་འདིར་མ་སྨོས་ཤེ་ན། རླུང་མེད་པར་ཡང་འབབ་པའི་ཕྱིར་ཏེ། དེ་ནི་དེ་ལ་འཇིགས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 3115]
སློབ་དཔོན་དཔའ་བོས་མཛད་པའི་སྐྱེས་པའི་རབས་རྒྱ་ཆེར་བཤད་པ་ལས་ཉའི་སྐྱེས་པའི་རབས་སོ།། །།

[Block 3116 [HEADING]]
## བྱ་སྲེག་པའི་ཕྲུ་གུའི་སྐྱེས་པའི་རབས། ^17-0

[Block 3117]
བརྩོན་པར་བྱ་བ་ནི་གོམས་པར་བྱའོ།[^1982] །མི་ནུས་པ་ནི་སྤྲོ་བ་མེད་པའོ། །

[Block 3118]
སྒོ་ངའི་སྦུབས་ནས་བྱུང་ནས་ཞག་གྲངས་མང་པོ་མ་ལོན་པ་གང་ཡིན་པ་སྟེ། འདིས་ན་ཚོད་བསྟན་ཏོ། །

[Block 3119]
སྤུ་སར་པ་གདོད་སྐྱེ་བ་གང་ཡིན་པ་དེས་ནི་འགྲོ་བའི་བྱ་བ་མི་ནུས་པ་བསྟན་ཏོ། །

[Block 3120]
རབ་ཏུ་རིད་པས་ཞེས་བྱ་བ་ཡང་འགྲོ་མི་ནུས་པའི་རྒྱུ་ཉིད་དེ། འདབ་གཤོག་རྣམས་ཀྱང་རྒྱས་ཞེས་བྱ་བ་ནི་འཕུར་དུ་རུང་བའི་གཤོག་པ་ཡོད་པས་སོ། །
--- END BLOCKS ---
