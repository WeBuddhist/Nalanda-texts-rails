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
[Block 2906]
འདིར་བྱས་པ༌[^1990]ལ་སྦྱར་བ་མ་བྱས་པ་ཉིད་ནི་མ་ཡིན་ཞེས་བྱ་བ་ནི་འདིའི་དོན་ཏོ། །

[Block 2907]
སྦྱོར་བ་མེད་པར་ཕྱུང་བ་ལ་རོ་མྱོང༌[^1991]བར་བྱེད་པ་ནི་དེ་དང་ལྡན་པ་ཉིད་དོ་ཞེས༌[^1992]བྱ་བ་དེ་དང་ལྡན་པ་ཉིད་ཅེས་བྱ་བ་ནི་སྦྱོར་བ་མ་ཡིན་པ་ཉིད་ནི་མ་ཡིན་ནོ། །

[Block 2908]
སྦྱོར་བ་མེད་པར་ཞེས་བྱ་བ་ནི་གཉིད་ལོག་པའི་གནས་སྐབས་ན་རྩོམ་པ་གང་ཡིན་པ་དང་འདབ་ཆགས་སུ་ཕྱུང་བ་གང་ཡིན་པ་སྦྱོར་བ་མེད་པར་གང་ཞིག་ཕྱུང་བ་ལ་རོ་མྱང་བ་ལ་སྦྱོར་བ་དེ་དང་ལྡན་པ་ཉིད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2909]
འདིར་གཞུང་ནི་ཉལ་བའི་བརྩལ་བ་ལ་དེ་སྐད་ཅེས་བྱ་སྟེ། གལ་ཏེ་རོ་མྱོང༌[^1993]བར་བྱེད་ན་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2910]
ཡན་ལག་གི་རྣམ་པ་ཅུང་ཟད་ཉེད་པ༌[^1994]དང་། ཡོངས་སུ་ཉེད་པ༌[^1995]དང་འཚིར་བའོ་ཞེས་བྱ་བ་ལ་དེ་དང་ལྡན་པ་ཉིད་ཅེས་བྱ་བར་སྦྱར་རོ། །

[Block 2911]
ཐམས་ཅད་ཉེད་པ་ནི་ཡོངས་སུ་ཉེད་པའོ། །

[Block 2912]
ཀུན་ནས་ཉེད་པ་ནི་གང་དུ་ཉེད་པའི་སྐད་ཅིག་མ་རྣམས་ལ་ཡུལ་གཅིག་པ་ཉིད་ཅེས་བྱ་བ་ནི་འདི་དག་གི་ཁྱད་པར་རོ། །

[Block 2913]
འདི་ནི་ཕྱོགས་གཅིག་ཉེད་པའོ། །

[Block 2914]
འདིར་གཞུང་ནི་བཙུན་པ་དགེ་སློང་གིས་ཡན་ལག་གི་རྣམ་པ་ལ་ཅུང་ཟད་ཉེད་པ་བདག་གིར་བྱེད་ན་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ། །

[Block 2915]
ཡོངས་སུ་ཉེད་པ་བདག་གིར་བྱེད༌[^1996]ན་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ། །

[Block 2916]
མངོན་པར་བཙིར་བ་བདག་གིར་བྱེད་ན་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2917]
དེ་ལས་སུ་རུང་བ་ལ་ནོམ་པའོ་ཞེས་བྱ་བ་ནི་ཡན་ལག་གི་རྣམ་པ་དེ་ལས་སུ་རུང་བ་ལ་ནོམ་པ་ནི་ཉེས་པ་སྦོམ་པོའོ། །

[Block 2918]
འདིར་གཞུང་ནི་ཡན་ལག་གི་རྣམ་པ་ལས་སུ་རུང་བ་ལ་ནོམ་ན་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2919]
སེམས་ཅན་དུ་བགྲང་བ་ལག་པ་ལ་སོགས་པས་ནོམ་པར་བྱེད་པ་ལ་ལུས་ཀྱི་རྣམ་པ་ཉིད་ཀྱི་ཕྱིར་ཞེས་བྱ་བ་ཤུགས་ཀྱིས་རྟོགས་པར་བྱའོ། །

[Block 2920]
སྨན་གྱིས་འབྱིན་ནའོ་ཞེས་བྱ་བ་ནི་སྦོམ་པོའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2921]
འདིར༌[^1997]རྣམ་པར་འགྱུར་བ་ཡོད་པར་འགྱུར་བ་ལ་སྦོམ་པོ་སྟེ་མེད་པ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 2922]
འདིར་ཕྱུང་བ་ལ་གཅི་བ༌[^1998]བྱས་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2923]
གཞན་གྱི་ལས་ཀྱང་ངོ་ཞེས་བྱ་བ་ལ། གཞན་གྱི་ཞེས་བྱ་བ་ནི་ཡན་ལག་གི་རྣམ་པ་ལས་སོ། །

[Block 2924]
འབྱིན་ན་ཉེས་པ་སྦོམ་པོའོ། །

[Block 2925]
ངེས་པར་བདག་ཉིད་ལ་གཞན་གྱི་ཡན་ལག་གི་རྣམ་པ་ལས་འབྱིན་ན་རྣམ་པར་འགྱུར་བ་ཡོད་ཀྱང་འདི་རང་ལ་བརྟེན་པའི་ཕྱོགས་པ་དང་། དེ་ལས་གཞན་པའི་རགས་པ་ཞེས་བྱ་བ་སྟེ་སྦོམ་པོར་རྣམ་པར་གཞག་པའོ། །

[Block 2926]
དགེ་འདུན་གྱི་ལྷག་མ་དང་པོ་ཞུ་བའི་སྐབས་སོ།། །།

[Block 2927]
རྣམ་པར་བསྔོས་པ་ལ་སོགས་པ་དང་། རྣམ་པར་ཞིགས་པ༌[^1999]དང་། ཀེང་རུས་དག་དང་། མགོ་དང་། རྣ་བ་དང་། སྣ་དག་དང་། མགུལ་པའི་བར་དང་། རྩིབ་ལོགས་དང་། རྒྱབ་དང་། བྲང༌[^2000]དང་། གཉེར་མ་དག་དང་། སྐྲའི་གསེབ་དང་ལག་པ་དང་། ཕྲག་པ་དང་དཔང་པ༌[^2001]དག་དང་། དཔུང་བའི་བར་དང་རྐེད་པ་དང་། བརླ་དང་རྐང་པ་དང་སྒྱིད་པ་དག་དང་སྒྱིད་པའི་བར་དུ་འབྱིན་པ་ན་དངོས་གཞིའོ་ཞེས་བྱ་བ་ནི་ཕྱི་རོལ་སེམས་ཅན་དུ་བགྲང་བ༌[^2002]དང་། དེའི་རྣམ་པར་གནས་པ་ཞེས་བྱ་བ་སྨོས་པ་དེ་རྣམས་ཀྱི་སྤྲོས་པ་ནི་འདི་ཡིན་ནོ། །

[Block 2928]
རྣམ་པར་བསྔོས་པ་ལ་སོགས་པ་ཞེས་བྱ་བའི་སོགས་པའི་སྒྲས་ནི་རྣམ་པར་རྣགས་པ༌[^2003]དང་རྣམ་པར་བམ་པ་དང་། རྣམ་པར་འབུས་གཞིགས་པ་དང་། རྣམ་པར་ཟོས་པ་དང་། རྣམ་པར་དམར་བ་རྣམས་བསྡུའོ། །

[Block 2929]
རྣམ་པར་ཞིགས༌[^2004]པའི་ཚིག་གིས་ནི་རྣམ་པར་འཐོར་བར༌[^2005]བསྡུ་སྟེ། གླན་པ་དག་པོག་པ་དང་ཡན་ལག་དང་བྲལ་བ་ནི་རྣམ་པར་གཞིགས་པ་ཞེས་བྱའོ། །

[Block 2930]
སྦོམ་པོ་ནི་ལ་བ་དང་ཕྱིང་བ་དང་དྲེའུ་རྔོག་དང་སྔས་ནང་ཚངས་ཅན་དང་ཁྲི་དང་ཁྲིའུ་དང་། སྟན་དང་སྟན་ནང་ཚངས་ཅན་དང་། ཁྲིའི་གསེབ༌[^2006]དང་བུམ་པ་དང་བུམ་བུ་དང་བུམ་པའི་བར་དང༌[^2007]བྱ་མ་བུམ་དང༌[^2008]ཆོལ་ཟངས་དང་། རྡོ་བ་དང་སྐྱང་ནུལ་དང་སྐྱང་ནུལ་གྱི་བར་དང་། སྒོ་གཏན་དང་ཤའི་དུམ་བུ་རྣམས་སོ་ཞེས་བྱ་བ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་འབྱུང་བ་ཡན་ཆད་སྦོམ་པོའི་དབང་དུ་བྱས་པར་རིག་པར་བྱའོ། །

[Block 2931]
ལ་བ་ལ་སོགས་པར་འབྱིན་ན་སྦོམ་པོའོ། །

[Block 2932]
འདིར་ཤའི་དུམ༌[^2009]བུ་ལུས་ཀྱི་རྣམ་པ་ལས་འཕོ་བ་ཉིད་ཀྱི་ཕྱིར་འབྱིན་པ་ལ་སྦོམ་པོ་སྟེ། གཞན་དུ་སེམས་ཅན་དུ་བགྲང་བ་མ་ཡིན་པ་ཉིད་ཀྱིས་དོན་གོ་བཞིན་པ་ལ་འདི་ནི་སྤྲོས་པའོ། །

[Block 2933]
རྨ་འཆར༌[^2010]ནའོ་ཞེས་བྱ་བ་ནི་གཞལ་བའི་དོན་ཉིད་ཀྱིས་ཞེས་བྱ་བ་གང་ཞིག་བརྗོད་པ་དེའི་འདི་ནི་སྤྲོས་པའོ། །

[Block 2934]
འདིར་རང་གི་ཡན་ལག་གི་ཚོགས་ཀྱི་བུ་ག་ནི་རྨ་ཞེས་བྱ་བར་བརྗོད་དོ། །

[Block 2935]
གཞན་གྱིས་འདིར༌[^2011]བཙིར་བ་ལ་དེ་ལས་བྱུང་བ་ལ་སྦོམ་པོ་མཐོང་བ་མ༌[^2012]ཡིན་ནོ། །

[Block 2936]
དེ་བས་ན་ཉེས་བྱས་སུ་རྟོགས་པར་བྱའོ། །

[Block 2937]
རྩོམ་པ་ན་བུད་མེད་དུ་བྱས་པ་འཚིར་ནའོ་ཞེས་བྱ་བ་ནི་བུད་མེད་ཉིད་དེས་བྱས་པ་ནི་བུད་མེད་དུ་བྱས་པ་སྟེ་མོའི་དབང་པོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2938]
དེ་ལ་དང་པོར་འཚིར་བ་གང་ཡིན་པ་དེ་ལ་སྦོམ་པོ་སྟེ་དེར་འཇུག་པ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 2939]
དེར་མཐེ་བོ་འཇོག་པའོ༌[^2013]ཞེས་བྱ་བ་ལ༌[^2014]དེར་ཞེས་བྱ་བ་ནི་བུད་མེད་དུ་བྱས་པ་སྟེ་ཚངས་པར་སྤྱོད་པ་མ་ཡིན་ལ་སྤྱོད་པར་འགྱུར་བའི་སྦོམ་པོའི་ལྟུང་བ་འདི་དག་དེ་ལ༌[^2015]མཉམ་པར་སྦྱར་བ་རྟོགས་པར་བྱའོ། །

[Block 2940]
འདིར་མཐེ་བོའི་ཚིག་ནི་དཔེ་ཡིན་ཏེ། ཡན་ལག་གི་ཚོགས་ལས་གཞན་པའི་འཇུག་པར་བྱ་བ་ནི་བུད་མེད་ཀྱི་དབང་པོ་སྟེ།[^2016] ལམ་གཞན་ཁ་དང་བཤང་བའི་ལམ་དག་པ་ཡང་འདིའི་རྗེས་སུ་འབྲངས་པས་འཁྲིག་པ་སོ་སོར་ཡང་དག་པར་སྦྱོར་བས་ཆགས་པ་དང་བཅས་པས་འཚིར་བ་དང་། མཐེ་བོ་ལ་སོགས་པས༌[^2017]འཇུག་པ་ལ་ནི་སྦོམ་པོའོ། །

[Block 2941]
ཉེ་བར་འགྲོ་བ་ལས༌[^2018]ཤོར་ནའོ་ཞེས་བྱ་བ་ནི་འཁྱུད་པའི་དོན་དང་ཕྱུང་བའི་དོན་དུ་ཞེས་བྱ་བ་ཤུགས་ཀྱིས༌[^2019]ཤེས་པར་བྱའོ། །

[Block 2942]
འཁྱུད་པ་ནི་དོན་དུའམ་མི་ཚངས་པར་སྤྱོད་པའི་དོན་དུ་ཉེ་བར་འགྲོ་བཞིན་པ༌[^2020]གནས་ནས་གནས་གཞན་དུ་དེའི་དོན་ཉིད་དུ་འཇུག་པའི་ཕྱིར་ཞེས་བྱ་བ་རིག་པར་བྱ་སྟེ། དེའི་དོན་མ་ཡིན་པར་འཇུག་པ་ལ་ལྟུང་བ་མེད་པར་བརྗོད་པའི་ཕྱིར་རོ། །

[Block 2943]
ཚུལ་བཞིན་མ་ཡིན་པ་ཡིད་ལ་བྱེད་པ་ལས་སོ་ཞེས་བྱ་བ་ནི་བྱེ་བྲག་ངེས་པར་མྱོང་བ་ལ་སོགས་པའི་བདེ་བ་སོ་སོར་ཉམས་སུ་མྱོང་བ་ཉེ་བར་བསྒྲུབ་པ་ལ་བརྗོད་པ་ཉིད་ཀྱི་ཕྱིར་ལྟུང་བ་ལ་གཞན་གྱི་རྣམ་པ་ཚུལ་བཞིན་མ་ཡིན་པ་ཡིད་ལ་བྱེད་པ་བསྡུས་པའི་དོན་དུ་ནི་མདོ་ཡིན་ནོ། །

[Block 2944]
ཡན་ལག་གི་རྣམ་པ་འཛིན་པ་ལས་སོ་ཞེས་བྱ་བ་ནི་དོན་གཞན་ཉིད་ལ་སྐྱོན་དང་བྲལ་བ་ཉིད་ལ༌[^2021]རྣམ་པར་གཞག་པས་འབྱུང་བའི་ཕྱིར་ཡིད་ཆེས་པའོ། །

[Block 2945]
བྱ་བ་མེད་པའི་ཕྱིར་འདིར་དགེ་འདུན་ལྷག་མ་མི་བསྐྱེད་པ་སྟེ། བྱ་བ་དང་བྲལ་བའི་ལུས་ཀྱི་བྱ་བ་ལ་ཉེས་བྱས་ཞེས་བྱ་བ་དེའི་ཕྱིར་རིག་པར་བྱའོ། །
--- END BLOCKS ---
