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
དེ་ལྟར་ཡང་བཀྲུ་བཤལ་བྱེད་དུ་འཛུད༌[^1969]ན་ཞེས་གསུངས་པ་དེའི་རྣམ་པར་འབྱེད་པ་ནི་ཆུས་བཀྲུ་བཤལ་བྱེད་ན་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3082]
བསླབ་པའི་གཞི་བདུན་པ་ནི་རྫས་དྲི་ཞིམ་པོས་རང་གི་ལུས་སྐུད་པ་ལའོ་ཞེས་བྱ་བ་ལ། །འདིར་དྲི་དག་གིས་ཞེས་བྱ་བ་ནི། མདོའི་ཚིག་གོ། །

[Block 3083]
རྫས་དྲི་ཞིམ་པོ་དག་གིས་ཞེས་བྱ་བ་ནི་རྣམ་པར་འབྱེད་པའི་ཚིག་གོ། །

[Block 3084]
གང་ལ་ལྟུང་བྱེད་བརྒྱད་པར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་འབྲུ་མར་གྱི་ཚིགས་མས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རང་གི་ལུས་སྐུད་པ་ལའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 3085]
འདིར་རང་གི་བྱེད་པའི་རྫས་དྲི་ཞིམ་པོས་རང་གི་ལུས་ལ་སྐུད་པ་ནི་དྲིལ་ཕྱིས་ཞེས་སྨོས་པ་ཡིན་ནོ། །

[Block 3086]
གཞན་བྱེད་དུ་འཇུག་པ་ལ༌[^1970]ཡང་ཞེས་བྱ་བའི་བྱེ་བྲག་མ་སྨོས་པས་རྟོགས་པའོ། །

[Block 3087]
བུད་མེད་སྐུད་དུ་འཇུག་པ་དང་གཞན་གྱིས་བྱས་པ་དང་གཞན་གྱིས་བྱས་པ་མ་ཡིན་པ་ཞེས་བྱ་བ་ནི་ལྟུང་བ་སྦོམ་པོ་དང་། དེར་ཕམ་པ་སྐྱེས་པས༌[^1971]འདིར་དགེ་སློང་གིས་དྲི་འཆང་བ་ལ་ནི་ཉེས་བྱས་ཁོ་ནའོ། །

[Block 3088]
མཚན་མཐུན་པ་བྱི་དོར་བྱེད་དུ་འཇུག་པ་ལ་ནི་ལྟུང་བ་མེད་དོ། །

[Block 3089]
བྱི་དོར་བྱེད་པ་ལས་བྱུང་བའི་ལྟུང་བྱེད་བརྒྱད་པའོ།། །།

[Block 3090]
གང་ལ་ཆུ་ལ་ལོངས་སྤྱོད་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་ལག་པ་སྦྲེལ་ཏེ་ཁྲུས་བྱེད་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བུད་མེད་དང་ལྷན་ཅིག་གོ། །

[Block 3091]
སྐྱེས་པ་དང་མ་ཡིན་ནོ། །

[Block 3092]
འདིར་སྦོམ་པོ་དང་ཕམ་པ་སྨོས་པས་ཤེས་པའོ། །

[Block 3093]
འདིར་ལྟེ་བར་སོན་ན་དངོས་གཞིའོ། །

[Block 3094]
མདུན་རོལ་དུ་ཉེས་བྱས་སོ། །

[Block 3095]
བྱི་དོར་བྱེད་པ༌[^1972]ལས་ཀྱང་རྣམ་པར་གཞག་པ་འདི་ཉིད་རིག་པར་བྱའོ། །

[Block 3096]
ཆུ་ལ་ལོངས་སྤྱོད་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 3097]
ད་ནི༌[^1973]འདི་མན་ཆད་ཀྱིས་འཆོས་པ་ལས་གྱུར་པའི་ལྟུང་བྱེད་དྲུག་སྟེ། གང་ལ་ལྔ་པོ་དེ་རྣམས་སུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་བཅོས་པའི་ཕྱིར་པུ་ཤེལ་ཙི༌[^1974]འཆང་བ་ལའོ། །

[Block 3098]
སོ་མངས་དང་སྨྱིག་ཤད་དང་། གསུམ་ཞེས་བྱ་བ་དང་། སྐྲ་བརྙན༌[^1975]གྱིས་ཀྱང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བཅོས་པའི་ཕྱིར་འཆད་པ་ལའོ་ཞེས་བྱ་བའི་རྗེས་བསྙེག༌[^1976]པའི་ཕྱིར་ཀྱང་ངོ་ཞེས་བྱ་བའི་སྒྲ་སྨོས་སོ། །

[Block 3099]
སོ་མངས་དང་སྨྱིག་ཤད་དང་། གསུམ་ཞེས་བྱ་བ་དང་། སྐྲ་བརྙན༌[^1977]གྱིས་ཀྱང་ངོ་ཞེས་སྨོས་པས་སོ། །

[Block 3100]
གསུམ་ཞེས་བྱ་བ་ནི་པུ་ཤེལ་ཙི༌[^1978]ལ་སོགས་པའི་མིང་འདི་ལ་ཡོད་པས་ན་གསུམ་ཞེས་བྱའོ། །

[Block 3101]
དེ་དག་གིས་སྐྲ་ཤད་པ་ལ་སོགས་པའི་རྣམ་པ་གང་གིས་འཆོས་པར་བྱེད་ཅིང་རྗེས་སུ་དག་པ་ལ་སོགས་པས་སྐྲ་བརྙན༌[^1979]གྱིས་མགོ་ལ་བཙུགས་ཅིང་དེ་བསྒྲུབ་པར༌[^1980]གྱུར་པ་དེ་རྣམས་ལ་བྱ་བ་སྟེ། བཅོས་པའི་ཕྱིར་ཉེས་པར་སྦྱོར་བ་སྟེ། ངེས་པར་སྦྱོར་བ་དེ་ལ་ཁ་ན་མ་ཐོ་བ་འདི་རྣམས་སོ། །

[Block 3102]
བརྩམས་པ་ཙམ་གྱིས་བྱས་པ་ཉིད་དེ་བཅོས་པ་ལ། དེའི་བྱ་བ་རྩོམ་པ་གཅིག་ཏུ་གྱུར་པའི་ཕྱིར་རོ། །

[Block 3103]
ཇི་སྲིད་དུ་མ་བཏང་གི༌[^1981]བར་དུ་ལོག་པར་གྱུར་ན་ལྟུང་བ་གཅིག་ཉིད་དོ། །

[Block 3104]
འདིར་མདོ་ནི་པུ་ཤེལ་ཙི༌[^1982]འཆང་ངམ། སོ་མངས་འཆང་ངམ། སྨྱིག་ཤད་འཆང་ངམ། སྐྲ་བརྙན༌[^1983]འཆང་ན་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3105]
འདི་རྣམས་ཀྱི་རྣམ་པར་འབྱེད་པ་ནི་འཆོས་པར་བྱེད་ན་ཞེས་གསུངས་པ་ཡིན་ཏེ། དེ་ལ་འཆོས་པའི་ཕྱིར་འཆང་བ་ལ་སོགས་པར་བྱེད་ན་ཞེས་བྱ་བ་ནི། དོན་གཉིས་ཀ་ལ་ཡང་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 3106]
དེ་ལྟར་མདོ་དང་རྣམ་པར་འབྱེད་པ་དག་ལ་དོན་གཅིག་པ་ཉིད་དུ་འགྱུར་བ་དེ་བས་ན་དེ་ཁོ་ན་ཉིད་དུ་ཉེ་བར་འབྲེལ་པའོ། །

[Block 3107]
སྐྲ་བཅོས་པ་ཉིད༌[^1984]ནི་དེ་རྣམས་ལ་གྲགས་པའི་ཕྱིར་སྐྲ་རྣམས་ཞེས་བྱ་བ་འདི་ལ་བཅོས་པ་དང་འབྲེལ་པ་ཉིད་དུ་ཤེས་བཞིན་པའོ། །

[Block 3108]
དེའི་ཕྱིར་དེ་གྲུབ་པས་མདོ་མ་བྱས་སོ། །

[Block 3109]
མཆན་ཁུང་དང་གསང་བའི་སྤུ་འཆོས་པ་ལ་ནི་ཉེས་བྱས་སུ་རིག་པར་བྱའོ། །

[Block 3110]
ཡང་མགོ་འཆོས་པ་སྤངས་པ་ལ་ཞེས་བྱ་བ་ནི་བཅོས་པའི་ཕྱིར་ཆོ་ག་དང་འབྲེལ་པ་ཉིད་ཀྱི་ཚིག་མེད་པས་འདིར་ཡང་མདོར་མ་བྱས་པ་ནི་གཟུགས་ཉིད་ལས་ཤེས་པའི་ཕྱིར་རིག་པར་བྱའོ། །

[Block 3111]
གང་ལ་ལྟུང་བྱེད་དྲུག་པར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་ཁྱིམ་པའི་རྒྱན་ཐོགས་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཡང་མགོ་འཆོས་པ་སྤངས་པ་ལ་ཞེས་བྱ་བ་ནི། ཆོས་གོས་ལ་སོགས་པ་རབ་ཏུ་བྱུང་བའི་ཡོ་བྱད་རྣམས་ཀྱང་རབ་ཏུ་བྱུང་བའི་རྒྱན་ཉིད་དེ་ཁྱིམ་པའི་རྒྱན་ནི་མ་ཡིན་ནོ། །

[Block 3112]
འདི་ལྟར་དེ་རྣམས་ཞི་བའི་དགའ་བའི་བློ་སྐྱེ་བས་དེ་རྣམ་པར་བཅད་པའི་ཕྱིར་ཁྱིམ་པའི་ཞེས་སྨོས་པས་འདི་ནི་རབ་ཏུ་བྱུང་བ་རྣམས་ལ་བཞད་གད་དུ་འགྱུར་བ་ཡིན་གྱི་རྒྱན་དུ་འགྱུར་བ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ༌[^1985]བསྟན་པའི་དོན་དུའོ། །

[Block 3113]
ཁྱིམ་པའི་རྒྱན་རིན་པོ་ཆེའི་རང་བཞིན་ལ་ནི་རྒྱན་ཉིད་དུ་ཡོངས་སུ་རྫོགས་པ་སྟེ། དེ་བས་ན་དེས་འདི་བསྡུས་པ་ཡིན་ནོ། །

[Block 3114]
དེ་ལྟར་ཡང་ཁྱིམ་པའི་རྒྱན་ནི་མགུལ་རྒྱན་དང་གདུ་བུ་རྒྱན་ཅན་དང་། དཔུང་རྒྱན་དང་། དོ་ཤལ་དང་། སེ་མོ་དོ་དང་། མུ་ཏིག་གི་ཆུན་པོ་དག་གོ་ཞེས་བྱ་བ་རྣམ་པར་འབྱེད་པ་ལས་གསུངས་སོ། །

[Block 3115]
རིན་པོ་ཆེ་མ་ཡིན་པའི་རྒྱན་ལ་ནི་ཉེས་བྱས་སོ། །

[Block 3116]
འདི་ལ་རིན་པོ་ཆེ་ལ་རིག་པའི༌[^1986]ཁ་ན་མ་ཐོ་བ་འདིར་རྫས་ཇི་ལྟ་བར༌[^1987]གཞན་རིག་པར་བྱའོ། །

[Block 3117]
འཆོས་པ་ལས་གྱུར་པའི་ལྟུང་བྱེད་དྲུག་པའོ།། །།

[Block 3118]
ད་འདི་མན་ཆད་ལྟུང་བྱེད་གསུམ་སྟོན་ཏེ། དེ་རྣམས་ཀྱི་དབང་པོ༌[^1988]གང་ལ་འགྱུར༌[^1989]ཞེ་ན། དེའི་ཕྱིར་བྲོ་བརྡུང་བ་ལའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 3119]
ཇི་ལྟར་ཞེ་ན་དེའི་ཕྱིར་གང་ཡང༌[^1990]རུང་བས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཐ་ན་སྨིན་མ་བསྐྱོད་པ་ལ་སོགས་པའི་བྱ་བས་ཀྱང་ངོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3120]
བསླབ་པའི་གཞི་གཉིས་པ་བསྟན་པ་ནི། གླུ་ལེན་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཇི་ལྟར་ཞེ་ན། དེའི་ཕྱིར་དེའི་བསམ་པས་མགྲིན་འགྱུར་གང་ཡང་རུང་བས་སོ་ཞེས་བྱ་བ་ལ། དེའི་བསམ་པས་ཞེས་བྱ་བ་ནི་གླུའི་བསམ་པས་སོ། །
--- END BLOCKS ---
