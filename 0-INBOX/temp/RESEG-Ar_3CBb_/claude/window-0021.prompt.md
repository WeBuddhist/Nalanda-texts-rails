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
[Block 736 [VERSE]]
དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི། །
གསང་བ་ཆེན་པོའི་བདག་ཉིད་མཆོག །
རབ་ཏུ་གསང་བ་ཡིན་པའི་ཕྱིར། །
ཐམས་ཅད་ཀུན་གྱིས༌[^347]གསལ་མ་བྱས། །

[Block 737 [VERSE]]
གང་ཡང་དུས་གསུམ་སངས་རྒྱས་དང་། །
རྣལ་འབྱོར་རྣལ་འབྱོར་མ་རྣམས་ཀྱིས། །
གང་ཚེ་གསང་བའི་དོན་གསུངས་པ། །
ཕྱི་དང་ཤིན་ཏུ་ནང་དག་དང་། །

[Block 738 [VERSE]]
དེ་བཞིན་བླ་མེད་ལ་དགོངས་ནས། །
གསང་བའི་དོན་རྣམས་གསུངས་པ་ཡིན། །
དེ་ལས་གཞན་དུ་གསུངས་གྱུར་ན། །
ཇི་བཞིན་དོན་དུ་བཟུང་བ་སྟེ། །
དེས་ན་ལམ་ངན་དག་ཏུ་ལྟུང་། །

[Block 739]
ཞེས་པ་ལ་སོགས་པ་འབྱུང་བ་ལྟ་བུའོ། །

[Block 740]
དེས་ན་དེ་བཞིན་གཤེགས་པའི་གསང་བ་ཆེན་པོ་འདི་ནི་རྣལ་འབྱོར་གྱི་རྒྱུད་རྣམས་ཀྱིས་ཤིན་ཏུ་རྒྱས་བཏབ་པ་ཡིན་ནོ་ཞེས་བསྟན་པར་བྱའོ། །

[Block 741]
གཞན་ཡང་གཞན་དུ་ཤེས་པར་བྱའོ། །

[Block 742]
དེ་ལྟར་ན༌[^348]བཤད་པ་བསྡུས་པ་དང་། དོན་བསྡུས་པ་བཤད་ནས། ད་ནི་དེ་ཉིད་ཀྱི་དོན་བསྡུས་པ་རྒྱས་པར་བཤད་པར་བྱ་སྟེ། དེའི་ཕྱིར་རིམ་པ་འདི་ཉིད་ཀྱིས་ན་བཞུགས་པའི་ཚིག་ནས་བརྩམས་ཏེ་ཞེས་བྱ་བ་སྨོས་ཏེ་འདིས་ནི་ཕྱག་རྒྱས་བཏབ་པ་ཡིན་ལ་ཞེས་སྦྱར་རོ། །གང་གིས་རྒྱས་བཏབ་ཅེ་ན། རིམ་པ་འདི་ཉིད་ཀྱིས་རྒྱས་བཏབ་ཅེས་སྨོས་སོ། །

[Block 743]
ཡང་ན་རིམ་པ་འདི་ཉིད་ཀྱིས་བཤད་པའི་ཕྱིར་རྒྱས་བཏབ་ཅེས་སྦྱར་རོ། །

[Block 744]
གང་རྒྱས་བཏབ་ཅེ་ན་བཞུགས་པའི་ཚིག་ནས་བརྩམས་ཏེ་རྗེས་སུ་ཡི་རང་བའི་བར་དུའོ། །

[Block 745]
མཐའ་རྣམ་པ་དྲུག་ཏུ་བཤད་པ་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་བཤད་ཟིན་ཏོ། །

[Block 746]
དེ་ཉིད་ཀྱིས༌[^349]གསང་བ་འདུས་པའི་དོན་ཕྱག་རྒྱས་བཏབ་ཅེས་སྨོས་པས་ན་སྒྲ་ཕྱག་རྒྱས་བཏབ་པ་ནི་མ་ཡིན་ཏེ། དོན་གསལ་བར་མ༌[^350]བྱས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 747]
འདི་དག་ལ་མ་རྟོགས་པར་ཅིར་འགྱུར་ཞེ་ན། དེ་མ་རྟོགས་པར་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། དེ་ལ་མ་རྟོགས་པ་ནི་གོང་མ་ཉིད་མ་རྟོགས་པའོ། །

[Block 748]
འོ་ན་གང་ཞིག་ལ་བརྟེན་ཞེ་ན་སྒྲ་ཇི་བཞིན་པའི་བཤད་པའི་སྒྲའི་དོན་ཙམ་ལ་བརྟེན་ཏེ་ཞེས་སྨོས་སོ། །

[Block 749]
སྒྲ་ཇི་བཞིན་པར་བཤད་པ་ནི་སྒྲ་ཇི་བཞིན་པ་ཉིད་དེ་དེ་བཤད་པའི་དོན་གང་ཡིན་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 750]
དེ་ལྟ་བུ་ལ་རྟོག་པའི༌[^351]སེམས་ཅན་གང་ཞིག་ཡིན་ཞེ་ན། ཡུལ་རྣམས་ལ་ཆགས་པའི་སེམས་ཅན་རྣམས་འགལ་བ་དང་། ཤིན་ཏུ་རྨད་དུ་བྱུང་བའི་བྱ་བ་བྱེད་པས་ལས་ཀྱི་དབང་དུ་འགྱུར་རོ་ཞེས་པ་ནི་ཡུལ་རྣམས་ལ་ཆགས་པ་ནི་ཡུལ་རྣམས་ལ་ཆགས་པ་སྟེ། ཡུལ་ལ་ཞེན་པར་གྱུར་པའི་ཐ་ཚིག་གོ། །

[Block 751]
ཡུལ་ལ་ཆགས་པ་ཡང་ཡིན་ལ་སེམས་ཅན་ཡང་ཡིན་པས་ཡུལ་རྣམས་ལ་ཆགས་པའི་སེམས་ཅན་དེ༌[^352]དེ་ལྟ་བུའི་གང་ཟག་གིས་དེ་ལ་དེ་ལྟར་རྟོག་ཅེས༌[^353]པའི་ཐ་ཚིག་གོ། །

[Block 752]
བརྟགས་པས་ཅི་བྱེད་ཅེ་ན་འགལ་བ་དང་ཤིན་ཏུ་རྨད་དུ་བྱུང་བའི་བྱ་བ་བྱེད་དེ། འདི་ལྟར་མ་བྱིན་པར་ལེན་པ་ལ་སོགས་པའི་བྱ་བ་ལ་འཇུག་པར་འགྱུར་རོ། །

[Block 753]
དེ་ཅིར་འགྱུར་ཞེ་ན། ལས་ཀྱི་དབང་དུ་འགྱུར་ཏེ། ལས་དེའི་སྟོབས་ཀྱིས་འབྲས་བུ་རྩུབ་མོ་ཉམས་སུ་མྱོང་བར་འགྱུར་རོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 754]
འདི་དག་གིས་ནི་འདི་སྐད་དུ་སྟོན་པར་འགྱུར་ཏེ་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་བཀའ་དགོངས་པ་དང་བཅས་ཏེ་བཤད་པར་མ་གྱུར་པ་དེའི་ཚེ་སྒྲ་ཇི་བཞིན་པར་ངེས་པར་འཛིན་པར་འགྱུར་རོ། །

[Block 755]
གང་གི་ཚེ་སྒྲ་ཇི་བཞིན་པར་ངེས་པར་བཟུང་བར་འགྱུར་བ༌[^354]དེའི་ཚེ་ཡུལ་ལ་ཆགས་པའི་སེམས་ཅན་འཇུག་པར་འགྱུར་རོ། །

[Block 756]
གང་གི་ཚེ་ཡུལ་ལ་ཆགས་པའི་སེམས་ཅན་ཞུགས་པར་གྱུར་པ་དེའི་ཚེ། དེ་བཞིན་གཤེགས་པའི་གདམས་ངག་དང་དུ་མི་ལེན་པར་འགྱུར་རོ། །

[Block 757]
གང་གི་ཚེ་དེ་བཞིན་གཤེགས་པའི་གདམས་ངག་དང་དུ་མི་ལེན་པར་གྱུར་པ་དེའི་ཚེ་དེ་བཞིན་གཤེགས་པའི་བཀའ་དགོངས་པ་ཅན་གཞན་ལ་ཡང་སྒྲ་ཇི་བཞིན་པར་འཛིན་པར་འགྱུར་རོ། །

[Block 758]
གང་གི་ཚེ་སྒྲ་ཇི་བཞིན་པར་བཟུང་བ་དེའི་ཚེ་འགལ་བ་དང་རྨད་དུ་བྱུང་བའི་བྱ་བ་བྱེད་པར་འགྱུར་རོ། །

[Block 759]
ཤིན་ཏུ་རྨད་དུ་བྱུང་བའི་བྱ་བ་བྱེད་པ་དེའི་ཚེ་སེམས་ཅན་ཐམས་ཅད་ལོག་པའི་ལམ་ལ་གནས་པར་འགྱུར་རོ། །

[Block 760]
སེམས་ཅན་ཐམས་ཅད་ལོག་པའི་ལམ་ལ་གནས་པར་གྱུར་པ་དེའི་ཚེ་རྨད་དུ་བྱུང་བའི་བྱ་བ་བྱེད་པའི་ལས་ཀྱི་འབྲས་བུ་སྨིན་པར་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །དེ་ཡང་གང་ལས་ཤེས་ཤེ་ན། བཅོམ་ལྡན་འདས་ཀྱིས་དགོངས་པ་ལུང་བསྟན་པ་ཞེས་བྱ་བའི་རྒྱུད་ལས་གསུངས་ཏེ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ།

[Block 761]
གསང་བའི་བདག་པོ་ཞེས་བྱ་བ་ནི་བོད་པའོ། །དོན་རྒྱས་པ་ཡི་ཚུལ་ཆེན་འདི་ནི་རྙེད་གྱུར་ནས། །ཞེས་པ་དོན་རྒྱས་པའི་ཚུལ་ཆེན་པོ་ནི་དེ་བཞིན་གཤེགས་པའི་གསང་བ་འདུས་པ་ཉིད་དོ། །

[Block 762]
ཇི་བཞིན་དོན་ནི་རྙེད་བཟུང་བས། །ཞེས་པ་ནི་སྒྲ་ཇི་བཞིན་པའི་དོན་རྙེད་པའོ། །

[Block 763]
དེས་ཇི་ལྟར་གཟུང་བ༌[^355]ཞེ་ན། གསང་བ་འདུས་པའི་དགོངས་པ་ཅན་ཐམས་ཅད་ཀྱང་སྒྲ་ཇི་བཞིན་པར་བཟུང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 764]
དེས་ཅིར་འགྱུར་ཞེ་ན། དེས་ན་ལམ་ངན་ངག་ཏུ་ལྟུང་། །ཞེས་པ་ནི་གང་བཟོད་པར་དཀའ་བའི༌[^356]སྡུག་བསྔལ་དང་ལྡན་པ་དེ་ནི་ལམ་ངན་པ་སྟེ་གང་ཞིག་གང་དུ་ལྟུང་བ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 765]
དེ་ལྟ་བུར་འཛིན་པར་བྱེད་པའི་གང་ཟག་ཀྱང་ཇི་ལྟ་བུ་ཡིན་ཞེ་ན། མངོན་པའི་ང་རྒྱལ་རྟག་དགའ་བས། །ཞེས་བྱ་བ་ནི་མངོན་པའི་ང་རྒྱལ་གཏོང་བར་མི་བྱེད་པ་སྟེ་གང་ཞིག་གང་ལ་འཕངས་པར༌[^357]འཛིན་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 766]
རྣལ་འབྱོར་པ་ནི་བདག་ཅེས་སྨྲ། །ཞེས་པ་ནི་རྣལ་འབྱོར་གྱི་དོན་དང་མི་ལྡན་པར་བདག་ཉིད་རྣལ་འབྱོར་པ་ཡིན་ཞེས་ཟེར་བ༌[^358]ལྟ་བུའོ། །

[Block 767]
ཆོས་ནི་གཡོ་ཡིས་བྱེད་པར་འགྱུར། །ཞེས་པ་ནི་མ་བྱིན་པར་ལེན་པ་དང་སྲོག་གཅོད་པ་དང་བརྫུན་དང་ཚིག་འཁྱལ་བ་དང་། ངག་རྩུབ་མོ་ལ་སོགས་པས་ཆོས་ཡོངས་སུ་ཚོལ་བར་བྱེད་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 768]
དེས་ནི་འདུས་པ་མི་ཤེས་པར། །ཞེས་པ་ནི་དེ་བཞིན་གཤེགས་པའི་གསང་བ་འདུས་པའི་དགོངས་པ་ལ་སོགས་པ་ལེགས་པར་མི་ཤེས་པའོ། །

[Block 769]
དམ་ཚིག་ལ་སོགས་སྤྱོད་བྱེད་ལ། །ཞེས་པ་ནི་དམ་ཚིག་དང་སྒྲུབ་པ༌[^359]ལ་སོགས་པ་ཉེ་བར་སྤྱོད༌[^360]པའོ། །

[Block 770]
གསང་བ་སྲུང་བར༌[^361]མི་བྱེད་ཅིང་། །ཞེས་པ་ནི།

[Block 771 [VERSE]]
ཐམས་ཅད་དུ་ནི་རབ་ཏུ་སྟོན། །
ཞེས་བྱ་བ་དེ་ཉིད་ཀྱིས་བཤད་དོ། །
མངོན་སུམ་སངས་རྒྱས་འདྲ་བ་ཡི། །
སློབ་དཔོན་སྨོད་ཅིང་བཀུར༌[^362]མི་བྱེད། །

[Block 772]
ཞེས་པ་ནི་བླ་མའི་བསྲུང་བར་བྱ་བའི་སྡོམ་པ་ལ་ཕྱལ་བར་གཏོང་བའོ། །

[Block 773]
སྐད་ཅིག་གིས་ནི་ཁོང་ཁྲོ་ཞིང་། །ཞེས་པ་ནི་ཉེས་པ་མཐོང་ན་སྐད་ཅིག་ཙམ་གྱིས་ཁྲོ་བར་བྱེད་པའོ། །

[Block 774]
དེ་བཞིན་སྐད་ཅིག་གིས་རྗེས་ཆགས། །ཞེས་པ་ནི་བདག་ཉིད་དང་རྗེས་སུ་མཐུན་པའི་ལས་བྱུང་ན་ཆགས་པར་བྱེད་པའོ། །

[Block 775]
འདི་དག་གིས་ནི་བློ་མི་བརྟན་པ་བསྟན་ཏོ།[^363] །དེ་ནས་འདོད་པས་ལོག་པར་གཡེམ་པ་ལ་སོགས་པའི་ཉེས་པ་བསྟན་པའི་ཕྱིར། མ་དང་སྲིང་མོ་བུ་མོ་སྟེ། །ཞེས་པ་ནི་བདག་ཉིད་བསྐྱེད་པ་དང་། བདག་ཉིད་དང་ལྷན་ཅིག་ཏུ་བསྐྱེད་པ་དང་བདག་གིས་བསྐྱེད་པའོ། །
--- END BLOCKS ---
