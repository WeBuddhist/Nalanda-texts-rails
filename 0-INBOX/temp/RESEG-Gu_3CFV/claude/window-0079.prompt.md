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
[Block 2766]
སྐྱེ་བོ་མང་པོ་ལ་བསྔོས་པ་བྱིན་གྱིས་རློབ་པའི་སྤང་བའོ། །གང་ལ་རང་ལ་ཡོངས་སུ་བསྒྱུར་བའི་སྤང་བར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་དགེ་འདུན་གྱི་ཕྱིར་ཡང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲས་ནི་ཕྱིར༌[^1796]སྦྱོར་དུ་བཅུག་ནས་རང་ལ་ཡོངས་སུ་བསྒྱུར་བ་ནའོ་ཞེས་བྱ་བའི་རྗེས་བསྙེགས་པའི༌[^1797]ཕྱིར་རོ། །

[Block 2767]
འདིར་ཡང་རྣམ་པར་འབྱེད་པའི་ཚིག་ཉིད་ལས།

[Block 2768]
དགེ་འདུན་གྱི༌[^1798]ཞེས་སྨོས་པ་ནི་དགེ་སློང་མའི་དགེ་འདུན་གྱི་ཕྱིར་ཞེས་གསུངས་པ་ཡིན་ཏེ། དེ་བས་ན་དགེ་སློང་མའི་ཚིག་གོ། །

[Block 2769]
འདི་ཡང་དོན་གཞན་ཉིད་ལ་ནི་སྔ་མ་བཞིན་དུ་ཉེས་བྱས་སུ་རིག་པར་བྱའོ། །

[Block 2770]
འདིར་དགེ་འདུན་ཞེས་སྨོས་པ་ནི་གྲངས་ཆད་པ་མེད་པར་དགེ་འདུན་མ་སྤྱི༌[^1799]ཕྱིར་སྦྱོར་དུ་བཅུག་པ་ཡིན་ནོ་ཞེས་བྱ་བ་བསླབ་པའི་གཞི་སྔ་མ་ལས་ཤེས་པའོ། །

[Block 2771]
དེའི་ཕྱིར་གྲངས་ཆད་པ་མེད་པའི་ཚོགས་ཀྱི༌[^1800]ཕྱིར་སྦྱོར་དུ་བཅུག་པ་བདག་གཅིག་པུས་སྤྱོད་པ་ལ་ནི་སྔ་མར༌[^1801]གཏོགས་པའི་བྱ་བར་རིག་པར་བྱའོ། །

[Block 2772]
དགེ་འདུན་ལ་བསྔོས་པ༌[^1802]བྱིན་གྱིས་བརླབ་པའི་སྤང་བའོ། །གང་ལ་བཅིངས་པ་འགྲོལ་དུ་འཇུག་པའི་སྤང་བར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་ཚིག་ཉན་དུ་གཞུག་པའི་ཕྱིར་རྫས་བཅིངས་པ་འགྲོལ་དུ་གཞུག་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་གཞུང་ནི་གཙུག་དགའ་མོས་སྤོས་འཚོང་གི་ཁྱེའུ་ལ་ཆགས་ནས་དེས་དེའི་ཚིག་ཉན་དུ་གཞུག་པའི་ཕྱིར་དེ་ལས་རྫས་ཉོ་ཞིང་ཐུམ༌[^1803]བུ་བཅིངས་ཤིང་བཅིངས་ཤིང་ཡང་དང་ཡང་འགྲོལ་དུ་བཅུག་ན་ཐམས་ཅད་སྤང་བའི་ལྟུང་བྱེད་དུ་འགྱུར༌[^1804]ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2773]
འདིར་ཚིག་ཉན་དུ་གཞུག་པའི་ཕྱིར་ཞེས་བྱ་བའི་གཞུང་ནི་ལྟུང་བ་བསྟན་པ་ལས།

[Block 2774]
དགེ་སློང་མས་དེ་ཚིག་ཉན་དུ་གཞུག་པའི་ཕྱིར་ཇི་ཙམ་དུ་ཐུམ་བུ་བཅིང་དུ་བཅུག་ཅིང་ཡང་དང་ཡང་འགྲོལ་དུ་བཅུག་ན་ཐམས་ཅད་སྤང་བའི་ལྟུང་བྱེད་དུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2775]
དོན་ལ་བདེན་པར་གནས་པའི་དོན་དུ་དེ་ལྟ་བུའི་ཟླ་བོ༌[^1805]ལ་བཅིངས་པ་འགྲོལ་དུ་འཇུག་པ་ལ་ཉེས་པར་རིགས༌[^1806]པ་མ་ཡིན་ཏེ། དེ་བས་ན་འདི་ཉེ་བར་བསྡུའོ། །

[Block 2776]
འཁྲིག་པའི་རོ་ཉེ་བར་གསོ་བར་བྱེད་པ་ནི་བདག་ཏུ་བྱེད་པའོ། །

[Block 2777]
མཚན་ཐ་དད་པ་མ་ཡིན་པ་སྐྱེས་པ་བསྟེན་པའི་མཐུ་ཡོད་པ་དེ་ལྟ་བུ་ལ་འཁྲིག་པ་ཉེ་བར་སྡུད་པ་འདུལ་བ་ལས་འགལ་བའི་ཟླ་ནི་མངོན་པར་གྲགས་པ་སྟེ། དེ་བས་ན་འདི་ལ་ཡང་འདིས་བསྟན་པ་ཉིད་དོ། །

[Block 2778]
མཚན་མཐུན་པ་ལ་སོགས་པ་ལ་ནི་ཉེས་བྱས་སོ་ཞེས་བྱ་བའི་རྗེས་སུ་འབྲངས་པས་རྟོགས་པའོ། །

[Block 2779]
རྫས་བཅིངས་པ་ཞེས་བྱ་བའི་ཚིག་འགྲོལ་བའི་ངོ་བོ་བསྟན་པའི་དོན་དུའོ། །

[Block 2780]
འདིར་ཐུམ་བུ་ཞེས་སྨོས་པ་ནི་ཐམས་ཅད་དུ་ནང་གི་བདག་ཉིད་ཀྱི་སྙིམ་པ་ལ་སོགས་པ་འདི་དང་ཕྱི་རོལ་གྱི་སྤྲོག་མ་ལ་སོགས་པ་དག་ནི་རྫས་ཉིད་དུ་བཟུང་བའོ། །

[Block 2781]
འོ་ན་སྤང་བའི་སྙིམ་པ་ལ་སོགས་པ་འགྲོལ་དུ་བཅུག་པ་འགལ་ལོ་ཞེ་ན། འདི་ནི་མ་ཡིན་ཏེ་ཐམས་ཅད་མ་ཡིན་པ༌[^1807]གསལ་བའི་ཕྱིར༌[^1808]ཆོས་ཀྱིས༌[^1809]ཀྱང་སྤྱིའི་འགྲེལ་པ་ཉེ་བར་བསྟན་པའི་ཕྱིར་ནུ་མ་བཞི་དང་ལྡན་པའི་བ་ལང་གི་རིགས་ཞེས་བྱའོ། །

[Block 2782]
གཞན་དབང་བའི་ཐུམ་བུ་བཅིང་བ་དང་འགྲོལ་དུ་བཅུག་པ་ལ༌[^1810]ཡང་དོན་མེད་པར་འགྲོལ་དུ་འཇུག་ན་ཤིན་ཏུ་སྡིག་ཆེ་བ་ཉིད་ཀྱི་ཕྱིར་འདི་ཁ་ན་མ་ཐོ་བ་ཡོངས་སུ་རྫོགས་པ་རྣམ་པར་གནས་པ་ཉིད་དོ། །

[Block 2783]
དེ་བས་ན་གཞན་གྱིས་བཅིངས་པ་འགྲོལ་དུ་བཅུག་པ་དང་ཐུམ་བུ་འགྲོལ་དུ་བཅུག་པ་བྱེ་བྲག་ཅུང་ཟད་ཀྱང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2784]
དེ་ལྟ༌[^1811]བས་ན་སྐྱེ་བའི༌[^1812]དབང་གིས་འདིར་མཚོན་པ་ཙམ་ཉིད་ཀྱི་དགོངས་པ་ཙམ་ཐུམ་བུའི་ཚིག་གོ། །

[Block 2785]
དེ་བས་ན་འདིར་འདི་ཁོངས་སུ་བསྡུ་བ་མ་ཡིན་ནོ། །

[Block 2786]
བཅིངས་པ་འགྲོལ་དུ་འཇུག་པའི་སྤང་བའོ། །གང་ལ་གོས་ལྕི་བ་བསྟན་པའི༌[^1813]སྤང་བར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་སྲང་བརྒྱ་པ་ལ་སོགས་པ་ནས་ཀཱར་ཥཱ་པ་ཎ་ཉི་ཤུ་ལ་སོགས་པ་རི་བའི་གོས་བདག་གིར་བྱེད་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བསླབ་པའི་གཞི་འདི་ནི་མཆོད་སྦྱིན་གྱིས་རལ་གྲི་མཐུ་ཅན་གྱིས་ཁྲོམ་ནས་ལ་བ་རིན་པོ་ཆེ་རིན་ཐང་ཆེན་པོ་རྙེད་ནས་དེས་ཀྱང་སྦོམ་དགའ་མོ་ལ་བྱིན་པས། དེས་དེ་གྱོན་ཏེ་བསོད་སྙོམས་ལ་ཞུགས་པ་དེ་ལས་བཅས་ཏེ། ཡང་དགེ་སློང་མ་གོས་ལྕི་བ་དང་རིན་ཐང་ཆེན་པོ་འཆང་བར་བྱེད་ན་སྤང་བའི་ལྟུང་བྱེད་དོ་ཞེས་བྱ་བ་འདི་དང་། འོག་མའི་ཡང་མདོ་ཡིན་ཏེ། འཆང་དུ་འཇུག་ན་ཞེས་བྱ་བ་འདི་ནི་ལྟུང་བ་བསྟན་པ་ལས་སོ། །

[Block 2787]
འཆང་བར་བྱེད་ན་ཞེས་བྱ་བའི་རྣམ་པར་འབྱེད་པ་ནི་བདག་གིར་བྱེད་ཅེས༌[^1814]གསུངས་པ་ཡིན་ནོ། །

[Block 2788]
དེའི་ཕྱིར་བདག་གིར་བྱེད་པ་ལས་ཞེས་བྱ་བ་སྨོས་པ་དང་། འདིར་བརྗེ་བའི་ཕྱིར་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2789]
དགེ་སློང་མས་གོས་རིན་ཐང་ཆེན་པོ་བརྗེ་བའི་ཕྱིར། བདག་ཏུ་བྱའོ་ཞེས་བྱ་བ་འདིས་བསྟན་པར་རིག་པར་བྱའོ། །

[Block 2790]
བཙོང་པ་ལ་སོགས་པའི་ཕྱིར་བདག་གིར་བྱེད་པ་ལ་ནི་ཐམས་ཅད་དུ་སྤང་བར་འགྱུར་རོ། །

[Block 2791]
གཞན་གྱིས་གོན་པ་ལས༌[^1815]ཡང་སྤང་བར་བྱ་བའི་དངོས་པོ་མེད་དུ་ཟིན་ཀྱང་ཁ་ན་མ་ཐོ་བ་ནི་ཡོངས་སུ་རྫོགས་པར་འགྱུར་རོ། །

[Block 2792]
དེ་ལས་སྐྱེས་པའི་རིན་པོ་ཆེ་ཡང་འདི་ལས་ལྗིད་དང་རིན་ཐང་ཆེན་པོ་ཞེས་བྱ་བ་རིན་གྱིས་རྙེད་པར་བྱ་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2793]
དེ་བས་ན་བརྟགས་པ༌[^1816]གང་དག་གིས་རིན་པོ་ཆེ་ལེན་པ་དེ་རྣམས་ཀྱིས་འདི་ལེན་པ་ལ་ལྟུང་བ་མེད་དོ་ཞེས་རྟོགས་པར༌[^1817]བྱའོ། །

[Block 2794]
བུད་མེད་ནི་གོས་བཟང་པོ་གྱོན་ན་གསོ་རོ་སྐྱེ་བས༌[^1818]དེའི་ཕྱིར་གོས་འདི་གཉིས་བཀག་པ་ཡིན་ནོ། །

[Block 2795]
འདིར་ལེན་པ་ནི་སྦྱང་པའི་ཕྱིར་བདག་ཏུ་བྱའོ། །

[Block 2796]
དེ་བས་ན་གོས་ལ་ཡང་ཁ་ན་མ་ཐོ་བ་འདིའོ། །

[Block 2797]
འདིར་གཞན་གྱིས་གྱོན་པ་ལ་ཡང་སྤང་བར་བྱ་བའི་དངོས་པོ་མེད་དུ་ཟིན་ཀྱང་གཅིག་པའི་དངོས་པོ་མེད་པས༌[^1819]ཁ་ན་མ་ཐོ་བ་ཡོངས་སུ་རྫོགས་པར་འགྱུར་རོ། །

[Block 2798]
སྲང་བརྒྱ་ལ་སོགས་པ་དག་ཅེས༌[^1820]བྱ་བ་ནི་མེ་ཏོག་དང་སྣམ་བུ་དང་བླངས་པའི༌[^1821]ལ་བ་ལ་སོགས་པ་དེའི་རིགས་ཅན་ལའོ། །

[Block 2799]
ཀཱར་ཥཱ་པ་ཎ་ལ་སོགས་པ་གཉི་གའི་སོགས་པ་ཞེས་བྱ་བའི་སྒྲ་སྨོས་པ་ནི་འོག་མ་ལ་ཡང་དེ་བཞིན་དུ་ཤེས་པར་བྱ་བའི་ཕྱིར། [^1822]དེ་ཡུལ་གྱི་ཐ་སྙད་ཀྱིས་རྣམ་པར་གཞག་པ་ཞེས་བྱ་བ་འདི་མ་བྱིན་པར་ལེན་པའི་ཕམ་པའི་རྗེས་སུ་འབྲངས་ནས་ཤེས་པར་བྱའོ། །

[Block 2800]
གོས་ཞེས་བྱ་བ་ནི་ཀ་ཤི་ཀའི་རས་ཕྲན་དང་དར་ལ༌[^1823]དང་། དར་གོས་ལ་སོགས་པ་གཞན་ཡང་རུང་བ་སྟེ་གང་ཞིག་རྣམ་པར་འབྱེད་པ་ལས་སྨོས་པ་དེ་ནི་འདིར་མཚོན་པ་ཙམ་ཡིན་ཏེ། རིན་ཐང་ཆེན་པོ་འདིར་རིན་ཐང་ཆེན་པོ་གཞན་ལས་དངོས་པོ་འདི་ལ་ཁྱད་པར་མེད་པས་རྣམ་པར་གནས་པ་ཡིན་ཏེ། དེ་ལྟ་བས་ན་ཁས་མ་བླངས་སོ། །

[Block 2801]
གོས་ལྕི་བ་བསྟེན་པའི་སྤང་བའོ། །གང་ལ་གོས་ཡང་བ་བསྟེན་པའི་སྤང་བར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་སྲང་ལྔ་པའི་མཐར་ཐུག་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སོགས་པ༌[^1824]ཞེས་བྱ་བའི་སྒྲས་ནི་ཀཱར་ཥཱ་པ་ཎ་ཉི་ཤུ་ལ་སོགས་པ་རི་བའི་གོས་བདག་གིར་བྱེད་པ་ལའོ་ཞེས་བྱ་བའི་རྗེས་བསྙེགས་པའི་ཕྱིར་རོ། །

[Block 2802]
འདིར་མཐར་ཐུག་པའི་སྒྲས་ནི་སྐྱེ་བོའི་གྲངས་བཟུང་བར་བྱས་པར་རིག་པར་བྱའོ། །

[Block 2803]
འདིར་གཞུང་ནི་སྤང་བ་ཞེས་བྱ་བ་ནི་སྲང་ལྔའམ་ལྔ་ལས་ཆུང་བའོ་ཞེས་བྱ་བ་གསུངས་པ་ཡིན་ཏེ། འདིས་ནི་འདི་ལྟ་སྟེ་བུད་མེད་ནི་གོས་བཟང་པོ་གྱོན་ན་གསོ་རོ་སྐྱེ་བས་དེའི་ཕྱིར་འདི་གཉིས་བཀག་པའོ། །

[Block 2804]
གོས་ཡང་བ་བསྟེན་པའི་སྤང་བའོ། །

[Block 2805]
[^1825]སྤང་བའི་ལྟུང་བྱེད་རྣམས་རྫོགས་སོ།། །།
--- END BLOCKS ---
