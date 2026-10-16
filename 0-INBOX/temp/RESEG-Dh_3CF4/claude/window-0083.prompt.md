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
ཕན་པ་ཡང་མ་ཡིན་ལ་བདེ་བ་ཡང་མ་ཡིན་པ་དེ་ཡང༌[^1858]སྦྱིན་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 2907]
གང་ཕན་པ་དང་བདེ་བ་དེ་ནི་སྦྱིན་པ་ཡིན་ནོ། །

[Block 2908]
གང་མི་བདེ་ན་ཡང་ཕན་པ་དེ་ནི་སྦྱིན་པ་ཡིན་ནོ། །

[Block 2909]
དེ་བས་ན་འདི་ནི་བདེ་བ་ཉིད་ཡིན་གྱི༌[^1859]ཕན་པ་ནི་མ་ཡིན་ཏེ། འདི་ལྟ་བུའི་མཚན་ཉིད་ཀྱི་སྦྱིན་པ་ནི་རྣམ་པ་ཐམས་ཅད་དུ་ཆོས་སྒྲུབ་པའི་གྲོགས་མ་ཡིན་ནོ། །

[Block 2910]
བདག་ལ་སྨན་བཏགས་པར་འགྱུར་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་གང་གོང་དུ་བསྟན་པ་དེའི་ལན་ནི། རབ་ཏུ་བྱམས་པས་ང་ཡི་ཕྱིར། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ཏེ། གྲོགས་པོ་ལས་ཁྱད་པར་དུ་གྱུར་པ་ནི་གཉེན་པས་ལྷག་བ་སྟེ། རྒྱུ་དེས་ན་རབ་ཏུ་བྱམས་པས་ངའི་ཕྱིར། རང་གི་སྲོག་ཀྱང་ཕོངས་པར༌[^1860]མི་ལྟ་བས་སོ། །

[Block 2911]
འོ་སྐོལ་གཉིས་ལས་མ་གཏོགས་པར། །ཞེས་བྱ་བ་གང་གོང་དུ་བསྟན་བའི་ཚིགས་བཅད་དེའི་ལན་ནི། མ་མཐོང་བར་ནི་སྡིག་པ་བྱས་པ་ཞེས་བྱ་བ་ཡིན་ཏེ། ལྐོག་ཏུ་སྡིག་པ་བྱས་པ་ལ་ཡང་བདེ་བ་མེད་དེ། ལྐོག་ཏུ་སྡིག་པ་སྤྱོད་པ་དེའི་དབང་དུ་བྱས་ནས། རྣམ་དག་མིག་གིས་མི་མཐོང་མི་སྲིད་དོ། །ཞེས་བྱ་བ་ལ་སོགས་པ་ཡིན་ཏེ། ལྷ་ཞེས་སྨོས་པས་ནི་ལས་ལས་གྱུར་པའི་ལྷའི་མིག་གཟུང་ངོ་། །རྣལ་འབྱོར་ཅན་ཞེས་སྨོས་པས་ནི་མངོན་པར་ཤེས་པ་ལས་བྱུང་བའི་ལྷའི་མིག་གཟུང་ངོ་། །བདག་ལ་སྨན་ཡོན་བཏགས་པར་འགྱུར། །ཞེས་བྱ་བ་ལ་སོགས་པའི༌[^1861]ལན་ནི། །ད༌[^1862]ནི་ཁྱོད་ལ་མི་ཕངས་སམ།[^1863] །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ཏེ། དེ་ནི་བདག་ཉིད་ཀྱིས་དེའི་ལུས་ལ་སོགས་པའི་ཡོན་ཏན་དང་ལྡན་པར་མཐོང་བ༌[^1864]སྟོན་པ་ཡིན་ནོ། །

[Block 2912]
དེ་ནི་བཏང་བ་ཞེས་བྱ་བ་དེ་དེ་ལྟ་བུའི་མཚན་ཉིད་དང་ལྡན་པ་འོ། །

[Block 2913 [VERSE]]
སྡུག་བསྔལ་ཞེས་བྱ་བ་ནི་འགྱོད་པའོ། །
ང་ལ་རབ་ཏུ་བྱམས་པའི་ཕྱིར། །

[Block 2914]
ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་གསུམ་གྱི་ལན་ནི། བདག་ནི༌[^1865]བུ་སྨད་ཅེས་བྱ་བའི་ཚིགས་བཅད་འདི་སྨྲས་པ་ཡིན་ཏེ། བྲན་མོ་འདི་སྦྱིན་པ་ནི་ཆོས་སྦྱིན་པའི་གྲོགས་ཉིད་ཡིན་གྱི། གྲོགས་པོ་ཉིད་དུ་ནི་མ་ཡིན་ཏེ། རྗེར༌[^1866]གྱུར་པ་དང་ལྷན་ཅིག་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2915]
མ་མཐོང་བར་ནི་སྡིག་པ་བྱས་པ་ཞེས་བསྟན་པ་དེ་ཡང་སྡིག་པ་མིན་ཏེ་རྒྱུ་དེ་གཉིས་ཀྱི༌[^1867]ཕྱིར་རོ། །

[Block 2916]
དེ་ལྟར་ཚིགས་བཅད་གསུམ་བརྗོད་པ་ལས་གཅིག་གི་ལན་ནི་མ་བསྟན་ཏོ། །

[Block 2917]
དེ་ནི་ཁྱོད་ལ་མི་ཕངས་ཞེའམ་ཞེས་བྱ་བའི་ཚིགས་བཅད་དེའི་ལན་ནི་འདི་བརྩམས་པ་ཡིན་ཏེ། དེ་ནི་བདག་ལ་ཕངས་པ་ལགས་མོད་ཀྱི།[^1868] །ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་འདི་ཡིན་ནོ། །

[Block 2918]
ཆོས་སྤྱོད་པ་ལས་དཔལ་ནི་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་ནི་རང་གི་ངེས་པ་ངེས་པར་གཟུང་བ་དང་། བདག་ཉིད་ཀྱི་ངོ་ཚ་ཉིད་གཟུང་བའི་ཕྱིར་སྨྲས་པ་སྟེ། ངོ་ཚ་ཡང་གང་ཞེ་ན་བདག་དང་ཆོས་ཀྱི་དབང་དུ་བྱས་ནས་ཁ་ན་མ་ཐོ་བ་ལ་འཛེམ་པའོ་ཞེས་བྱ་བའི༌[^1869]ཚིག་གིས་སོ། །

[Block 2919]
མཚོན་གྱིས་བཏབ་པའམ། མེའི་ནང་དུ་ཞུགས་པ་ཞེས་བྱ་བ་འདི་གཉིས་སྨོས་པས་ནི་ལུས་ཀྱི་དབང་པོ་བདེ་བའི༌[^1870]མཐུན་པ་ཉིད་ཡིན་ཏེ། ཚིག་པ་དང་བཅས་པའི་རྒྱུ་གཉིས་ཀྱིས་སོ། །

[Block 2920]
མེ་དང་མཚོན་གྱིས་ཚིག་པ་དང་ཆད་པས་ནི་འཇིག་རྟེན་ཕ་རོལ་ཏུ་ངན་འགྲོར་འགྲོ་བ་མེད་དེ། དེ་ཉིད་ཀྱིས་བཏབ་པ་དང་ཞུགས་པས་ནི་ཁས་ལེན་པའོ། །

[Block 2921]
ཆོས་མ་ཡིན་པ་སྤྱོད་པས་ནི་འཇིག་རྟེན་ཕ་རོལ་ཏུ་ངེས་པར་ངན་སོང་དུ་འགྲོ་བའི་ཕྱིར་རོ། །

[Block 2922]
སྐྱོན་མེད་ཆུང་མ་བོར་ན་ནི། །ཞེས་བྱ་བ་ནི་ཆོས་དང་འགལ་བར་བསྟན་ཏེ། དེས་ན་ཆོས་དང་འགལ་བ་ཡིན་བས། ང་ཡིས་ཆད་པས་བཅད་ཏ༌[^1871]རེ། །ཞེས་པའོ། །

[Block 2923]
སྨད་པའི་གནས་སུ་ཁྱོད་གྱུར་ན། །ཞེས་བྱ་བ་ནི་གྲགས་པ་མ་ཡིན་པ་ཐོབ་པར་བསྟན་ཏོ། །

[Block 2924]
ཕ་རོལ་བསྲེག་པར༌[^1872]འགྱུར་ཞེས་བྱ་བ་ནི་སྐྱོན་མེད་ཆུང་མ་བོར་བའི་ཕྱིར་རོ། །

[Block 2925]
ང་ཡིས་ཆད་པས་བཅད་པ་དང་སྨད་པའི་གནས་སུ་གྱུར་པ་ཞེས་བྱ་བ་ནི་འདིར་བསྲེགས་པའོ། །

[Block 2926]
ཆོས་དང་འགལ་བར་གྱུར་པ་ཞེས་བྱ་བ་ནི་སྐྱོན་མེད་ཆུང་མ་བོར་བས་སོ། །

[Block 2927]
སྐྱེ་བོས་སྨད་པ་ནི། སྨད་པའི་གནས་སུ་ཁྱོད་གྱུར་ན། །ཞེས་བྱ་བས་སོ། །

[Block 2928]
བདེ་བ་ཉམས་ཀྱང་རུང་ཞེས་བྱ་བ་ནི་རྒྱལ་པོས༌[^1873]ཆད་པས་བཅད་ཀྱང་རུང་བའོ། །

[Block 2929]
བཟོད་པར་བགྱི་ཞེས་བྱ་བ་ནི་རབ་ཏུ་འདོད་པའོ། །

[Block 2930]
རྣམ་པ་འདི་གསུམ་བཟོད་པར་བྱ་བའི་རྒྱུ་སྨྲས་པ། ཁྱོད་ལ་བདེ་བས་བདག་ཉིད་བདེར་གྱུར་ན། །[^1874]ཞེས་བྱ་བ་ཡིན་ཏེ། སྔར་བཤད་པའི་ཉེས་པ་རྣམ་པ་གསུམ་གྱི༌[^1875]ཉེས་པ་མེད་པ་དེ་རབ་ཏུ་བསྒྲུབ་པའི་ཕྱིར། ས་བདག་ཆེན་པོ་འཇིག་རྟེན་འདི་ན་ནི། །ཞེས་བྱ་བའི་ཚིགས་བཅད་བརྩམས་པ་ཡིན་ཏེ། ཇི་ལྟར་མཆོད་སྦྱིན་ལ་སྦྱིན་པར་བྱ་བའི་གནས་ཀྱི་སྦྱིན་གནས་དམ་པ་ལ་བྱིན་པས་ནི་ཆོས་མ་ཡིན་པ་མེད་པ་ལྟར་འདིས་ན་ཡང་ཁྱོད་ཀྱིས་ཆད་པས་བཅད་པར་ཡང་མི་འགྱུར་ལ་དེ་ཉིད་ཀྱི་ཕྱིར་གྲགས་པ་མ་ཡིན་པར༌[^1876]ཡང་འབྱུང་བར་མི་འགྱུར་བས་དེ་བས་ན་ཉེས་པ་གསུམ་ཡང་མེད་དེ། བདག་ལ་བརྩེ་བའི་ཕྱིར་ཡང་དེ་བཞེས་སུ་གསོལ་ཞེས་བསྟན་པ་ཡིན་ནོ། །

[Block 2931]
གལ་ཏེ་ཆོས་དང་འགལ་བར་གྱུར་ཀྱང་དེ་ལྟོ་བ་བཟེད༌[^1877]པར་བགྱི་ཞེས་བྱ་བའི་ལན་ནི་ང་ལ་རབ་ཏུ་བྱམས་པའི་ཕྱིར༌[^1878]ཕན་པ་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་ཡིན་ནོ། །

[Block 2932]
སྐྱེ༌[^1879]བོས་སྨད་ཅིང་ཞེས་བྱ་བ་དེའི་ལན་ནི་འཇིག་རྟེན་པས་སྨད་པ་ལ་འཛེམ་པ་མེད་པར་བྱ་བ་མི་རིགས་སོ་ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 2933]
དེ་བས་ན་འཇིག་རྟེན་པས་སྨད་པར་བྱ་བ་ལ་ཡང་མི་འཛེམ་པར་བྱ་བ་མི་རིགས་ཏེ། དེ་ཡང་། འཇིག་རྟེན་སྨོད་པས་འཛེམ་པ་མེད་པ་དང་། །ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་འདིས་སྒྲུབ་པ་སྟེ། སྨོད་པས་འཛེམ་པ་མེད་པ་ནི་ཆོས་ལ་མི་ལྟ་བའི་ཕྱིར་རོ། །

[Block 2934]
ཕྱི་མ་ནི་འཇིག་རྟེན་ཕ་རོལ་གྱི་ཆོས་ཀྱི་འབྲས་བུ་ལ་མི་འཛེམ་པ་སྟེ། ཆོས་ལ་མི་ལྟ་བའི་ཕྱིར་རོ། །

[Block 2935]
དེ་བཞིན་དུ་ལྷག་མ་འཇིག་རྟེན་འདིའི་མཆོག་ཏུ་འཛིན་པ་ཡིན་ནོ་ཞེ་ན། ཡང་འདིའི་དོན་མི་འགྲུབ་པར་བསྟན་པའི་ཕྱིར་སྨྲས་པ། གང་ཡིན་སྐྱེ་བོ་དེ་ལ་ཡིད་མི་ཆེས། །ཞེས་སྨོས་ཏེ། དེ་ལ་ཞེས་བྱ་བ་ནི་སྨད་ཅིང་ཆོས་དང་ཕྱི་མའི་འབྲས་བུ་ལ་མི་ལྟ་བ་སྟེ། ཅི་ནས་ཀྱང་བསམ་པ་ཆོས་དང་འཇིག་རྟེན་ཕ་རོལ་གྱི་འབྲས་བུ་རྣམ་པར་སྤངས་པའོ། །

[Block 2936]
དེ་བཞིན་དུ་མཐོང་བའི་ཆོས་ལ་ཡང་དཔལ་གྱི་འབྲས་བུ་སྤངས་པར་འགྱུར་ཏེ། དཔལ་ནི་སྐྱེ་བོ་ཡིད་ཆེས་པ་རྩ་བར་གྱུར་པ་ཉིད་ལས་སོ། །

[Block 2937]
བདེ་བ་ཉམས་ཀྱང་རུང་ཞེས་བྱ་བ་སྔར་བསྟན་པ་དེའི་ལན་ནི་འདིས་བསྟན་ཏེ། བདེ་བ་མ་ཡིན་པ་ནི་ཆོས་མ་ཡིན་པར་སྤྱོད་པ་གཙོ་བོར་བསྟན་པའི་ཕྱིར་ཁྱོད་ལ་ང་སྨྲའོ་ཞེས་བྱ་བ་ཡིན་ཏེ། སྲོག་གི་ཕྱིར་ཡང་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ནོ། །

[Block 2938]
ཆོས་དང་འགལ་བ་ལ་ནི་འགལ་བར༌[^1880]མ་བྱེད་ཅིག་པ་སྟེ། ཅིའི་ཕྱིར་ཞེ་ན། ཉེས་པ་ཆེ་བར་འགྱུར་བར་གདོན་མི་ཟ་བའི་ཕྱིར་རོ། །

[Block 2939]
ངན་སོང་དུ་འགྲོ་བའི་རྒྱུ་ཡིན་པས་སྲོག་གི་ཕྱིར་ཡང་ཞེས་བྱ་བ་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན། ལེགས་འབྱུང་ཆུང་ལ་དོགས་པ་དང་བཅས་པའི་ཕྱིར་རོ། །

[Block 2940]
དོགས་པ༌[^1881]དང་བཅས་པས༌[^1882]དེའི་སྲོག་ཀྱང་ཡིད་བརྟན་དུ་མི་རུང་བས་སོ། །

[Block 2941]
ལེགས་འབྱུང་ཆུང་ཡང་ཞེས་བྱ་བ་ནི་ཡུན་རིང་དུ་འཚོ་བར༌[^1883]གྱུར་ཀྱང་མཐོང་བའི་ཆོས་ལ་བདེ་བ་ཤིན་ཏུ་ཆུང་བའི་ཕྱིར་རོ། །

[Block 2942]
དེ་ལྟར་དེ་ལ་རང་གི་ཆུང་མ་ཡོངས་སུ་གཏོང་བ་མི་རིགས་པར་བསྟན་ནས། དེ་ནི༌[^1884]བདག་ཉིད་ཀྱིས༌[^1885]བླང་བ་ཉིད་དུ་མི་རིགས་པར་བསྟན་པའི་ཕྱིར་སྨྲས་པ། དམ་པ་རྣམས་ནི་ཕ་རོལ་སྨད་ལ་སོགས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 2943]
སྨད་པ་ལ་སོགས་པའི་སྡུག་བསྔལ་གང་ཡིན་པ་དེ་ནི་སྨད་པ་ལ་སོགས་པའི་སྡུག་བསྔལ་བྱས་པ་སྟེ། གང་སྔར་བསྟན་པའི་ཆོས་དང་འགལ་བ་དང་། སྐྱེ་བོས་སྨད་པ་དང་། བདེ་བ་ཉམས་པའི་མཚན་ཉིད་ནི་སྨད་པ་ལ་སོགས་པའི་སྡུག་བསྔལ་སྨོས་པ་འདིས་གཟུང་ངོ་། །མི་གནོད་པར་ཞེས་བྱ་བ་ནི་སྨད་པ་ལ་སོགས་པའི་སྡུག་བསྔལ་བླངས་ནས་སོ། །

[Block 2944]
བདག་གི་དོན་སྒྲུབ་ཅེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའི་སྒྲུབ་པ་སྟེ། བདག་དང་གཞན་གྱི་ཆོས་སུ་བཤད་པའོ། །

[Block 2945]
གཉི་གའི་ཆོས་མ་ཡིན་པ་མེད་པར་བསྟན་པའི་ཕྱིར་རྗེའི་དོན་དུ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་འདི་ཡིན་ཏེ། དེའི་སླད་དུ་ལྗོངས་ཀྱི༌[^1886]མི་དང་བཅས་པས་ཞེས་བྱ་བ་འདིས་ནི་གཉི་ག་ལ་ཡང་ཆོས་མ་ཡིན་པ་དང་གྲགས་པ་མ་ཡིན་པ་མེད་པར་བསྟན་ཏོ། །
--- END BLOCKS ---
