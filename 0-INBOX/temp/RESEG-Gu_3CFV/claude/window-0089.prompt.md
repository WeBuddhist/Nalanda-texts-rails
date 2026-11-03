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

[Block 3121]
གང་ཡང་རུང་བ་ཞེས་བྱ་བ་ནི། ཐ་ན་ཚིགས་སུ་བཅད་པ་ཙམ་འདོད་པ་ལ་ཡང་ངོ་། །གང་ལ་གསུམ་པར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་རོལ་མོ་བྱེད་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདི་ལྟར་བུད་མེད་ལ་གར་དང་གླུ་ལ་སོགས་པ་རྗེས་སུ་མི་མཐུན་པ་དེ་ལྟར་སྐྱེས་པ་རྣམས་ལ་ནི་མ་ཡིན་ནོ། །

[Block 3122]
དེ་བས་ན་འདིར་དགེ་སློང་ལ་ཉེས་བྱས་སུ་རིག་པར་བྱའོ། །

[Block 3123]
རྒྱགས་པ་ལས་གྱུར་པའི་ལྟུང་བྱེད་གསུམ་མོ།། །།

[Block 3124]
ད་འདི་མན་ཆད་ནི་ལོངས་འཆོས་པ་ཉིད་ལས་གྱུར་པའི་ལྟུང་བྱེད་གསུམ་སྟོན་ཏེ། དེ་རྣམས་ཀྱི་དང་པོ་ནི་ལོངས་སྤྱོད་དུ་གྱུར་པའི་གདུགས་ཐོགས་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བདག་གིར་བྱེད་པ་ཙམ་ལ་ནི་དངོས་གཞི་མ་ཡིན་ཏེ། འོན་ཀྱང་ཡོངས་སུ་ལོངས་སྤྱད་པར་གྱུར་པ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3125]
གལ་ཏེ་གང་ཞིག་ལམ་ལ་དབང་བ་ཉིད་ངོས་སུ་འདུད་པ་ལ་ཞེས་བྱ་བ་སྨོས་པ་དེ་ལ་ཡང་མ་བྱས་པས། དམིགས་ཀྱིས་བསལ་བ་འདི་གཏོགས་པའོ། །

[Block 3126]
སྦྱོར་བ་གཅིག་ཡིན་ན་ཤིན་ཏུ་རིང་པོར་ཐོགས་པ༌[^1991]འདི་དང་འོག་མ་ལ༌[^1992]ཡང་ལྟུང་བ་གཅིག་ཁོ་ནར་ཟད་དོ། །

[Block 3127]
གང་ལ་གཉིས་པ་དེ་བརྗོད་པར་བྱ་སྟེ། དེའི་ཕྱིར་མཆིལ་ལྷམ་གྱོན་པ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ལོངས་སྤྱོད་དུ་གྱུར་པའི་གདུགས་ཐོགས་པ་ལའོ་ཞེས་བྱ་བའི་རྗེས་སྙེགས༌[^1993]པའི་ཕྱིར། ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲ་སྨོས་སོ། །

[Block 3128]
དབྱར་ཁང་དུ་མལ་སྟན་བསྲུང་བའི་ཕྱིར་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ནི་དབྱར་ཁང་ལ་གནས་གཞན་དུ་མལ་སྟན་ལ་བག་བྱ་བའི་ཕྱིར་མཆིལ་ལྷམ་གྱོན་པ་ལ་ལྟུང་བ་མེད་དོ། །

[Block 3129]
དེ་ལས་གཞན་པ་ཐམས་ཅད་ལ་ནི་ལྟུང་བྱེད་ཁོ་ནར་འགྱུར་རོ། །

[Block 3130]
འདིར་དགེ་སློང་གི་གནས་ལ་མཚོན་པའམ་དེ་ཉིད་ཀྱིས་དབྱར་ཁང་གི་འཕངས་པར་རིག་པར་བྱ་བ༌[^1994]ཡིན་ཏེ། དེ་ཡང་རྗེས་སུ་མི་མཐུན་པ་ཉིད་ཀྱི་ཕྱིར་བུད་མེད་རབ་ཏུ་བྱུང་བ་རྣམས་ལ་མཆིལ་ལྷམ་གྱོན་པ་འཇུག་པའི་ཕྱིར་རོ། །

[Block 3131]
གསུམ་པ་བསྟན་པ་ནི་ཁྲིའུའི༌[^1995]བསྙེན་བཀུར་ཉམས་སུ་མྱོང་བར་བྱེད་པ་ལའོ་ཞེས༌[^1996]བྱ་བ་སྟེ། འདི་ནི་སྦོམ་དགའ་མོ་དགེ་སློང་རྣམས་ལ་སྟོན་པར་བྱེད་ཅིང་དེས་དགེ་སློང་མ་འོངས་ཤིང་ལྷགས་པ༌[^1997]རྣམས་ལ་ཁོ་མོའི་ཕྱིར་ཕྱོགས་ག་གེ་མོ་ཞིག་ཏུ་ཁྲིའུ་ཤོམས་ལ་འདུག་ཏུ་ཆུག་ཤིག་ཅེས་བསྒོ་ཞིང་། ཡང་ཕྱོགས་ག་གེ་མོ་ཞིག་དང་། གནས་ཁང་གི་ཉེ་འཁོར་དང་ཁྱམས་དང་ཁང་སྟེང༌[^1998]ངམ་ཆེ་གེ་མོ་ཞིག་ཏུ་ཁྲིའུ་ཁྱེར་ལ་ཁོ་མོ་འདུག་ཏུ་ཆུག༌[^1999]ཤིག་ཅེས་ཟེར་བ་ལས་བཅས་པ་སྟེ། དེས་ཁྲིའུས་བསྙེན་བཀུར་བྱེད་དུ་འཇུག་པའི་ངོ་བོ་ཉིད་ཀྱང་བསྟན་པ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 3132]
ལོངས་འཆོས་པ་ཉིད་ལས་གྱུར་པའི་ལྟུང་བྱེད་གསུམ་མོ།། །།

[Block 3133]
གང་ལ་ཐུག༌[^2000]ཐུབ་ཏུ་ཕྱིས་གནོན༌[^2001]བྱེད་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་ཁྱིམ་གཞན་དུ་མ་བསྒོ་བར་སྟན་ལ་འདུག་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རྩྭའི་ཆུན་པོ་དང་ཤིང་གི་དུམ་བུ་དང་སོ་ཕག༌[^2002]ལ་སོགས་པ་ལ་གལ་ཏེ་རྡོལ་བ་ཡིན་ན། ཐུག་ཐུབ་ཏུ༌[^2003]བསྟན་པ་མི་སྐྱེད་པ༌[^2004]ཁོ་ནའོ། །

[Block 3134]
གལ་ཏེ་མ་ཡིན༌[^2005]ན་ཡོངས་སུ་མ་རྫོགས་པ་འདི་བསྐྱེད་པའོ། །

[Block 3135]
དེ་བས་ན་སྔ་མ་ལ་ནི་ལྟུང་བ་མེད་དོ། །

[Block 3136]
ཕྱི་མ་ལ་ཉེས་བྱས་སོ། །

[Block 3137]
བཞད་གད་ཀྱི་ཆེད་དུ་རྩྭའི་ཆུན་པོ་དང་ཤིང་གི་དུམ་བུ་དང་། ས་དང་བ་གླང༌[^2006]གི་ལྕི་བའི༌[^2007]རང་བཞིན་ཀུན་ནས་འཚོ་བར་བྱེད་པ་བསྒྲུབ་པ་ཤིང་གི་དུམ་བུ་ཞེས་བྱ་བ་ལ་སོགས་པའི་མ་རྡོལ་བ་ལས་ཡོངས་སུ་རྫོགས་པའི་ཐུག༌[^2008]ཐུབ་བསྐྱེད་པའོ། །

[Block 3138]
རྡོལ་བ་ལ་ན༌[^2009]ནི༌[^2010]སྨད་པ་བསྐྱེད་པའོ། །

[Block 3139]
དེ་བས་ན་འདིར་སྔ་མ་ལ་ལྟུང་བྱེད་དོ། །

[Block 3140]
ཕྱི་མ་ལ་ནི་ཉེས་བྱས་སོ། །

[Block 3141]
མལ་སྟན་ལ་ཡང་འདི་བསྟན༌[^2011]ཞེས་སྨོས་པས་བསྡུས་པར་རིག་པར་བྱ་སྟེ། གོས་ལ་ཡང་འཕངས་པར་རིག་པར་བྱའོ། །

[Block 3142]
དགོས་པ་མེད་པ་དང་འདྲ་བའི་རྩྭའི་ཆུན་པོ་ལ་སོགས་པ་ལ་སྨོས་པའི་ཆོ་ག་རྣམས་རྣམ་པར་གཞག་པའོ། །

[Block 3143]
འདུག་པ་ལ་ནི་ཤིན་ཏུ་རིང་པོར་རྗེས་སུ་འགྲོ་བའི་ཕྱིས༌[^2012]གནོན་དུ་གྱུར་པ་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 3144]
དེ་བས་ན་འདིར་ཉལ་བ་དག་ལ་ཁ་ན་མ་ཐོ་བ་དེ་ཡོངས་སུ་རྫོགས་པར་འགྱུར་ཏེ། ཤིན་ཏུ་རིང་པོར་མ་སོང་བ་ལ་འདི་ནི་ཐུག༌[^2013]ཐུབ་ཆེས་ཤིན་ཏུ་ཆེ་བའི་ཕྱིར་རོ། །

[Block 3145]
གང་ཞིག་རྐང་པ་དག་གིས་འཛེགས་ནས།[^2014] ཙོག་ཅོག་པོར་རམ་གཞན་དུ་གནས་པའོ། །

[Block 3146]
དེ་བས་ན་འདིར་ཡང་ཁ་ན་མ་ཐོ་བ་ཡོངས་སུ་རྫོགས་པ་འདིའོ། །

[Block 3147]
ཐུག༌[^2015]ཐུབ་ཏུ་ཕྱིས་གནོན་བྱེད་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 3148]
གང་ལ་ལོག་ཐབས་བྱེད་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་ཆོས་ཉན་དུ་གཞུག་པའི་གནས་སྐབས་སུ་ཁྱིམ་པའི་སྟན་སྤྱད་པའི༌[^2016]ཁྱིམ་པ་ལ་མ་སྦྲན་པར་བོར་ཏེ་འགྲོ་བ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཆོས་ཉན་དུ་གཞུག་པའི་ཚེ་ཁྱིམ་པའི་སྟན་ཡོངས་སུ་ལོངས་སྤྱད་པའི་ཁྱིམ་པ་ལ་མ་སྦྲན་པར་བོར་ཏེ་འགྲོ་བ་ལ་ལྟུང་བྱེད་དུ་འགྱུར་ཏེ། འདི་ནི་སྦོམ་དགའ་མོ་ཁྱིམ་བདག་གི་ཁྱིམ་དག་ཏུ་སོང་སྟེ། ཁྱིམ་བདག་གི་ཆུང་མ་དག་གིས་ཀྱང་སྟན༌[^2017]དག་བཤམས་པ་ན་དེ་དེ་ལ་འདུག་སྟེ། རྒྱ་ཆེར་ཆོས་བསྟན་པར་བརྩམས་པ་དང་། དེ་རྣམས་ཀྱང་འདི་ནི་ལས་མེད་པ་ཞིག་གོ་སྙམ་ནས་ལངས་ཏེ། དོང་བའི་ཚེ་དེས་ཀྱང་སྟན་དག་མ་སྦྲན་པར་གཅིག་པུ་ལངས་ཏེ་སོང་བ་དང་། སྟན་དེ་དག་རྐུན་པོ་དག་གིས་ཁྱེར་ནས་ཁྱིམ་མི་དག་གིས་སྟན་བཙལ་ན༌[^2018]མ་རྙེད་དེ། སྦོམ་དགའ་མོ་ལ་འཕགས་མ་སྟན་དག་ཅིར་བགྱིས་ཞེས་པ་དང་། དེས་སྨྲས་པ། ཇི་ལྟར༌[^2019]ཁྱེད་ཅག་གིས་ཁོ་མོ་ལ་མ་སྦྲན་པར་དོང་བ་དེ་བཞིན་དུ་ཁོ་མོས་ཀྱང་དེ་བཞིན་ནོ་ཞེས་ཟེར་བ་ལ་གཞི་དེ་ལས་བཅས་པ་ཡིན་ནོ། །

[Block 3149]
འདི་ནི་སྙིང་ནས་ལོག་ཐབས་བྱེད་པ་ནི་ཉེས་པ་ཉིད་དོ། །

[Block 3150]
ཁྱིམ་པའི་དོན་ལ་ཡོངས་སུ་རྫོགས་པ་ཉིད་འཇུག་པ་འདི་ལ་ཡིན་ཏེ། དེ་བས་ན༌[^2020]འདིར་ནི་ཁྱིམ་པ་ལ་བརྟེན་པའོ། །

[Block 3151]
གཞན་རབ་ཏུ་བྱུང་བ་འདི་པ་དང་། ཕྱི་རོལ་པའི་རབ་ཏུ་བྱུང་བ་དབང་བ་ཉིད་ལ་འདིར་ཉེས་བྱས་སུ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 3152]
གང་གི་ཚེ་དངོས་གཞིར་གྱུར་པའི་སོང་བའི་མཐར་ཐུག་པ༌[^2021]ཡོངས་སུ་རྫོགས་པའི་བདག་ཉིད་ལ་དངོས་གཞིའི་དུས་སུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་སྤངས་པའི་ཉེ་འཁོར་གྱི་མཐའ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སྔར་གནས་མལ་སྤངས་ཏེ་འགྲོ་བའི་ཉེ་འཁོར་གྱི་མཐར་ཐུག་ན་རྫོགས་པ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3153]
ཁྱིམ་པ་ལ་ལོག་ཐབས་བྱེད་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 3154]
ད་འདི་མན་ཆད་ནི་ཁྱིམ་པ་མོའི་བཟོ་སྟོན་པའི་ལྟུང་བྱེད་གསུམ་སྟེ། གང་ལ་དེ་རྣམས་ཀྱི་དབང་པོར༌[^2022]འགྱུར་ཞེ་ན། དེའི་ཕྱིར་སྐུད་པ་འཁལ་བ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རྒྱུད་ཀྱི་རང་གཞན་གང་ཡང་རུང་བ་བསྒྲུབ་པ་བྱས་ན་སྐུད་པ་འཁལ་བ་ཉིད་ཡིན་ཏེ། རི་མོ་ཙམ་བྱས་པ་ལ་རི་མོ་བྱས་པ་ཉིད་སྨོས་པར་རྟོགས་པའོ། །

[Block 3155]
འདི་ལྟར་རྣམ་པར་འབྱེད་པ་ལས།
--- END BLOCKS ---
