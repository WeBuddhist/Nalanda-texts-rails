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
[Block 2871]
ཤིན་ཏུ་དམན་པའི་ཐ་མ་རྐང་པ་ཉེད་པ་ལ་ཡང་ལྟུང་བྱེད་ཁོ་ནའོ། །

[Block 2872]
འདིར་ཤིན་ཏུ་ཡང་ཆོས་ལ་ལྟུང་བ་ཉིད་སྐྱེ་བར་འགྱུར་རོ། །

[Block 2873]
བདེ་བར་གཤེགས་པའི་ཆོས་སུ་འགྱུར་བའི་དོན་འདི་ལ་སངས་རྒྱས་ཀྱི་བཀའ་ཀློག་པ་ལ་སོགས་པ་ལ་ཉེས་བྱས་སུ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 2874]
སྡོམ་པ་གཞན་སྦྱིན་པའི་ཕྱིར་ཀློག་པ་ལ་སོགས་པ་སྟེ། དེ་ཁོ་མོ་ལ་ཆོས་གོས་སྟེར་བལྟ་ན་དེའི་ཕྱིར་ཁྱོད་རབ་ཏུ་དབྱུང་བར་བྱའོ་ཞེའམ། ཀློག་ཏུ་གཞུག་གོ་ཞེས་བྱ་བ༌[^1864]ལ་སོགས་པ་ཟེར་བ་ལ་ནི་ཉེས་བྱས་སུ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 2875]
བུད་མེད་རྣམས་ཀྱི་ཉེས་པ་ཅི་ཡང་རུང་བ་དང་། སེར་སྣའི་ཆོས་ལ་ཡང་དག་པར་གནས་པ་དེ་དང་འདྲ་བའི་སྐྱེས་པ་དགེ་སློང་འདིར་ན་སྨད་པའོ། །

[Block 2876]
ཆོས་འཚོང་བ་ཞེས་བྱ་བའི་ལྟུང་བྱེད་དོ། །

[Block 2877]
གང་ལ་འདྲིད་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་རབ་ཏུ་དབྱུང་བ་དང་མཐུན་པ་བསྟན་པས་ཁྱིམ་རྒྱས་པར་བྱ་བ་སྤོང་དུ་བཅུག་ནས་རབ་ཏུ་མི་འབྱིན་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བསླབ་པའི་གཞི་འདི་ནི་གཽ་ཏ་མ་སྐེམ་མོས་ཕྱུག་པོའི་ཡུགས་ས་མོ་གཞན་མྱ་ངན་གྱི༌[^1865]ཟུག་རྔུས་གཟིར་བ་ཞིག་ལ་ཅིའི་ཕྱིར་རབ་ཏུ་མི་འབྱུང་ཞེས་སྨྲས་པ་དང་། དེ་ན་རེ་གལ་ཏེ་འཕགས་མས་རབ་ཏུ་དབྱུང་བར་གནང་ན་བདག་རབ་ཏུ་འབྱུང་ངོ་ཞེས་ཟེར་བ་ལ། དེས་དེ་ལ་ཁྱིམ་རྒྱས་པར་བྱ་བ་འདི་དག་སྤོང་ན་དེ་བས་ན་ཁྱོད་རབ་ཏུ་འབྱུང་བར་འགྱུར་བ་མི་དཀའོ་ཞེས་སྨྲས་པ་དང་། ཁྱིམ་རྒྱས་པར་བྱ་བ་སྤངས་པ་ན་དེས་དེ་རབ་ཏུ་མ་བྱུང་བ་ལས་བཅས་པ་ཡིན་ནོ། །

[Block 2878]
འདིས་ནི་ཁས་མ་བླངས་པ་མ་ཡིན་ཏེ། གང་ཞིག་ཕྱིས་ཁྱོད༌[^1866]ལ་དཀའ་བར་མི་འགྱུར་བ་ཞེས་བྱ་བའི་ཚིག་དལ༌[^1867]འདི་བསྟན་པར་ཤེས་པར་བྱའོ། །

[Block 2879]
དེ་ལ་ཁྱིམ་རྒྱས་པར་བྱ་བ་འདི་དག་སྤོང་ན་ཁོ་མོས་ཁྱོད་རབ་ཏུ་འབྱུང་བར་འགྱུར་བ་ཞེས་བྱ་བ་གང་ཞིག་གསལ་པོར་ཁས་བླངས་པ་དེ་ནི་རྗེས་སུ་མི་མཐུན་པར་ཁས་བླངས་པ་བསྟན་པ་མ་ཡིན་ནོ། །

[Block 2880]
དེ་ལྟ་བས་ན་དེ་ལ་འདིས་མ་བསྡུས་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 2881]
འདིའི་རྗེས་སུ་འབྲངས་པས་གཞན་དག་འདྲིད་པ་ལ་ནི་ཉེས་བྱས་སུ་རྟོགས་པར་བྱའོ། །

[Block 2882]
འདྲིད་པའི་ལྟུང་བྱེད་དོ། །

[Block 2883]
གང་ལ་འཁོར་མང་པོ་སོགས་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་ལོའི་རྗེས་སུ་རབ་ཏུ་འབྱིན་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རབ་ཏུ་བྱུང་བ་གཞན་གཉིས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2884]
འདིར་མཐར་ཐུག་པའི་གཙོ་བོ་ལོ་གཞན་གཟུང་བ་རྣམས་གནས་པ་ཡིན་ནོ། །

[Block 2885]
དེ་བས་ན་ལོ་དང་པོ་ལ་དེ་དང་ལྷན་ཅིག་གམ་ཕྱིས་རབ་ཏུ་བྱུང་བ་ལ་ལྟུང་བྱེད་དུ་རྟོགས་པར་བྱའོ། །

[Block 2886]
ལོ་གསུམ་པ་ལ་སོགས་པ་དག་ལྟུང་བ་མེད་པར་རིག་པར་བྱའོ། །

[Block 2887]
འཁོར་མང་པོ་སོགས་པའི་ལྟུང་བྱེད་དོ། །

[Block 2888]
གང་ལ༌[^1868]མ་གནང་བ་སྡུད་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་བདག་པོས་མ་གནང་བ་རབ་ཏུ་འབྱིན་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རབ་ཏུ་འབྱིན་པ་ལའོ་ཞེས་བྱ་བ་ནི་འདིར་འོག་མ་བཞི་པོ་རྣམས་ལ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 2889]
བདག་པོ་ལ་ནི་ཇི་ལྟར་ཆུང་མ་རབ་ཏུ་ཕྱུང་ན་གནོད་པར་འགྱུར་བ་དེ་ལྟ་བུ་རབ་ཏུ་ཕྱུང་ན་གནོད་པར་མི་འགྱུར་ཏེ། དེ་ལྟར་ཆུང་མ་སྤང་ངོ་། །གང་གི་ཕྱིར་སྲོག་དང་བྲལ་བར་གྱུར་པ་མཆོག་ཏུ་ཕན་པའི་དངོས་པོ་འདི་གཅོད་པའི་རྣམ་པ་འཇུག་པ་དེ་བས་ན༌[^1869]འདིར་ལྕི་བའི་ཁ་ན་མ་ཐོ་བ་ཉིད་ཤེས་པའོ། །

[Block 2890]
མ་གནང་བ་སྡུད་པའི་ལྟུང་བྱེད་དོ། །

[Block 2891]
སྐྱོན་ཅན་སྡུད་པ་ལས་གྱུར་པའི་ལྟུང་བྱེད་བཞི་པོ་དག་ལས་གང་ལ་འཁྲུལ་པ་མོ་སྡུད་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་འཁྲུལ་པ་མོའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རབ་ཏུ་འབྱིན་པ་ལ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2892]
གཉིས་པ་གང་ཡིན་ཞེ་ན་དེའི་ཕྱིར་སྦྲུམ་མའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རབ་ཏུ་འབྱིན་པ་ལ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2893]
གསུམ་པ་གང་ཡིན་ཞེ་ན། དེའི་ཕྱིར་མྱ་ངན་གྱིས་གཟིར་བའོ༌[^1870]ཞེས་བྱ་བ་སྨོས་ཏེ། རབ་ཏུ་འབྱིན་པ་ལ་ཞེས་བྱ་བར་སྦྱོར༌[^1871]རོ། །

[Block 2894]
བཞི་པ་གང་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ཙབ་ཀྲོལ་ཅན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རབ་ཏུ་འབྱིན་པ་ལ་ཞེས་བྱ་བའི་དབང་དུ་བྱས་པའོ། །

[Block 2895]
ཙབ་ཀྲོལ་ཅན་རབ་ཏུ་འབྱིན་པ་ཁོ་ན་ལ་ལྟུང་བྱེད་དུ་འགྱུར་བར་མ་ཟད་དོ། །

[Block 2896]
འོ་ན་གང་ལ་ཞེ་ན། དེའི་ཕྱིར་བསྙེན་པར་རྫོགས་པར་བྱེད་པ་ལ་ཡང་ངོ་། །སྦྲུམ་མ་ལ་སྣོད༌[^1872]མི་སྲིང་བ་ཉིད་ནི་མ་གནང་བ་སྡུད་པའི་ལྟུང་བྱེད་དུ་རིག་པར་བྱའོ། །

[Block 2897]
འདིར་བསྙེན་པར་རྫོགས་པར་བྱེད་པ་ནི་རྒྱུ་མཚན་འདིས་ཉེས་བྱས་སུ་རིག་པར་བྱའོ། །

[Block 2898]
མཐར་བྱས་པའི་དགེ་འདུན་ལ་དེ་ཞེས་བྱ་བ་འདིར་ལྟུང་བྱེད་འདི་ལ་རྣམ་པར་གཞག་པའོ། །

[Block 2899]
བུད་མེད་མ་རུངས་པ་རབ་ཏུ་དབྱུང་བར་མི་བྱའོ༌[^1873]ཞེས་བྱ་བ་ཙབ་ཀྲོལ་བྱེད་པ་ཅན་གྱི་མདོ་ལས་སོ། །

[Block 2900]
རྣམ་པར་འབྱེད་པ་ལས་ཙབ་ཀྲོལ་ཅན་ཞེས་བྱ་བ་ནི་བུད་མེད་མ་རུངས་མའོ་ཞེས་བྱ་བ་གསུངས་པ་ཡིན་ནོ། །

[Block 2901]
གླེང་གཞི་ལས་ཀྱང་བུད་མེད་གཞན་དེ་མཐོང་བ་ནི་མ་རུངས་པ་ཁྲོ་བ་རྩུབ་པོ་སྨྲ་བ། གཞན་ལ་ནང་སྟོན་པར་བྱེད་པ་བུད་མེད་གཞན་དང་ལྷན་ཅིག་ཏུ་རྩོད་པར་བྱེད་ཅིང་དེ་རྩོད་པར་བྱེད་པ་ན་སྐྲ་རྣམས་ཞིག་པར་གྱུར་ཅིང༌[^1874]དེས་དེ་ལ་བསྡིགས་པའི་ཕྱིར་ཅེ་སྦྱང་མོའི་སྐད་འདོན་པ་དང་། དེས་ཀྱང་དེའི་སྐད་ཐོས་པ་ལ་འགྱེལ་བ་དེ༌[^1875]མཐོང་ནས་སྦོམ་དགའ་མོ་འདི་སྙམ་དུ་སེམས་ཏེ། སྟོབས་དང་ལྡན་པ་འདི་ལྟ་བུའི་གྲོགས་མོ་རྩོད་པར་བྱེད་པ་མོ་འདི་གང་གི་ཕྱིར་བདག་གིས་རབ་ཏུ་དབྱུང་བར་བགྱིའོ། །

[Block 2902]
དེ་དེས་རབ་ཏུ་ཕྱུང་ནས་སྐྱེ་དགུའི་བདག་མོ་ཆེན་མོ་སྐྲ་རང་གིས་འཇར་བར་བྱེད་པའི་བར་དུ་འདི་ནི་གནོད་པ་སྟེ། ཨུཏྤ་ལའི་མདོག་ཅན་གྱིས་གྲོང་ཁྱེར་ཆེན་པོ་དྲུག་ཏུ་སྨད་འཚོང་མར་གྱུར་པ་ན་ཆོས་སྦྱིན་མའི་ཕོ་ཉ་བསྙེན་པར་རྫོགས་པར་བྱས་པས། གཽ་ཏ་མ་སྐེམ་མོའི་ཁྱོས་བཟུང་བ་དང་། བུའི་ཤ་ཟོས་པས་དེ་ལ་འདི་ནི་གནད་པའོ། །

[Block 2903]
དེ་ཐོས་ནས་སྦོམ་དགའ་མོའི་གྲོགས་མོ་མ་རུངས་པ་དང་རྩོད་པ་ན་དགེ་སློང་མ་ཙབ་ཀྲོལ་བྱེད་པ་དང་། དེ་ནས་དགེ་སློང་མ་རབ་ཏུ་མང་པོ་རྣམས་འདི་སྐད་ཅེས་ཡང་མ་རུངས་མ་ཁྲོ་བས་སྨྲ་བ་དང་བཅས་ནས་སྨྲ་བར་བྱེད་པ་གང་གིས་རབ་ཏུ་ཕྱུང་ཞེས་ཟེར་རོ། །

[Block 2904]
དེ་བས་ན་མ་རུངས་པ༌[^1876]འདི་ལ་ཙབ་ཀྲོལ་བྱེད་པ་ཉིད་ཚད་མ་ཞེས་བྱ་བ་ཡིད་ཆེས་པའོ། །

[Block 2905]
ཤིན་ཏུ་མཐུན་པ་ཉིད་སྟོབས་དང་ལྡན་པའི་ཉེས་དམིགས་སུ་གྱུར་པ།[^1877] ཙབ་ཀྲོལ་བྱེད་པ༌[^1878]དེ་བས་ན། ཙབ་ཀྲོལ་བྱེད་པ་ཐམས་ཅད་ལ་ཆོ་ག་འདི་རྣམ་པར་གཞག་པར་རིག་པར་བྱའི༌[^1879]ཁྲོ་བས་སྨྲ་བ་ཉིད་ལ་ནི་མ་ཡིན་ནོ། །

[Block 2906]
བསྙེན་པར་རྫོགས་པ་ཉིད་ལ༌[^1880]ཤིན་ཏུ་སྟོབས་དང་ལྡན་པ་ཉིད་མནན་པ་ལ་དགེ་སྦྱོང་དུ་མེད་པའི་ཆོས་དང་མཐུན་པ་ཉིད་གཤེ་བ་མཚང་འདྲུ་བ༌[^1881]ཞེས་བྱ་བ་ལ་བསྙེན་པར་རྫོགས་པ་ལ་འདི་བཀག་པའོ། །

[Block 2907]
སྐྱོན་ཅན་སྡུད་པ་ལས་གྱུར་པའི་ལྟུང་བྱེད་དུ་གཏོགས་པའོ། །

[Block 2908]
ཡལ་བར་འདོར་བ་ལས་གྱུར་པའི་ལྟུང་བ༌[^1882]བཞི་པོ་དག་ལས།

[Block 2909]
དེ་རྣམས་ཀྱི་དང་པོ་གང་ཡིན་ཞེ་ན། དེའི་ཕྱིར་རབ་ཏུ་ཕྱུང་བ་དང་བསྙེན་པར་རྫོགས་པར་བྱས་པ་དག་ལ༌[^1883]ཕན་མི་འདོགས་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། མཁན་མོ་ཉིད་ཀྱིས་ཞེས་བྱ་བ་ཐམས་ཅད་ཀྱི་དབང་དུ་བྱས་པར་རིག་པར་བྱའོ། །

[Block 2910]
རབ་ཏུ་བྱུང་བ་དང་བསྙེན་པར་རྫོགས་པར་བྱ་བ་དག་ལ་གདམས་ངག་ལ་སོགས་པས་ཡོངས་སུ་མི་སྐྱོང་ཞིང་། ཕན་མི་འདོགས་པ་དག་ལ་ལྟུང་བྱེད་དུ་འགྱུར་རོ། །
--- END BLOCKS ---
