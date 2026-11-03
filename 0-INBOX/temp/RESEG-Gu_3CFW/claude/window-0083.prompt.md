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
དེ་དག་ལའོ་ཞེས་བྱ་བ་ནི་ཡོངས་སུ་གནས་པ་མགུ་བར་བྱ་བ་སྤྱོད་པ་དེ་དག་ལ་མངོན་པར་སྨྲ་བ་ལ་སོགས་པ་སྐབས་དེ་དག་མི་བྱ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2907]
རང་བཞིན་དུ་གནས་པ་རྣམས་ཀྱིས༌[^2752]དེ་དག་ལ་མངོན་པར་སྨྲ་བ་དང་ཕྱག་འཚལ་བ་ལ་སོགས་པ་མི་བྱའོ། །

[Block 2908]
དེ་དང་ལྷན་ཅིག་ཏུ་གོམ་པ་བསྲི་བ་ཉིད་ལས་གཞན་པས་བཅག་པར་མི་བྱའོ། །

[Block 2909]
སྟན་ཆས་དམའ་བ་ཉིད་ལས་གཞན་ལ༌[^2753]འདུག་པར་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ལྷན་ཅིག༌[^2754]པར་ཡང་མི་བྱ་ན་སྟན་གཅིག་ལ་ལྟ་སྨོས་ཀྱང་ཅི་དགོས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2910]
ཕྱི་བཞིན་འབྲེང་བའི་དགེ་སྦྱོང་གི་བདག་ཉིད་ལས༌[^2755]གཞན་པས་ཁྱིམ་དག༌[^2756]ཏུ་འགྲོ་བ་ཡང་ངོ་། །གཡོགས་མ་གཅིག༌[^2757]ཏུ་མལ་བཤམ་པར༌[^2758]མི་བྱའོ། །

[Block 2911]
རབ་ཏུ་བྱུང་བ་དང་བསྙེན་པར་རྫོགས་པ་དང་། གནས་སྦྱིན་པ་དང་། དགེ་ཚུལ་ཉེ་བར་གཞག་པ་དག་མི་བྱའོ་ཞེས་བྱ་བ་ནི་རབ་ཏུ་བྱུང་བ་དང་བསྙེན་པར་རྫོགས་པ་དག་གིས༌[^2759]ཡན་ལག་གི་ངོ་བོས་འགྲོ་བར་མི་བྱའོ། །

[Block 2912]
མཁན་པོས་དེ་དག་ལ་བསྙེན་པར་རྫོགས་པར་མི་བྱའོ། །

[Block 2913]
འདི་དག་ལས་བསྙེན་ནས༌[^2760]གནས་པར་མི་བྱའོ། །

[Block 2914]
གསོལ་བ་དང་བརྗོད་པ་དག་ཁས་མི་བླང་ངོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་དེ་བསྟན་པ་ཡིན་ནོ། །

[Block 2915]
གོམ་པ་བསྲི་བ་ཉིད་ལས་གཞན་དུ་འདི་དང་ལྷན་ཅིག་བཅག་པར་མི་བྱ་བ་དང་། ཡོངས་སུ་གནས་པ་དང་མགུ་བར་སྤྱོད་པ་དེ་གཉིས་ཀྱིས་དགེ་སློང་རང་བཞིན་དུ་གནས་པ་དེ་དང་ལྷན་ཅིག་ཏུ་གོམ་པ་གཅིག་གི་ཕྱིར་འབྱངས་ཤིང་བསྲི་བ་ཉིད་མ་གཏོགས་པར་གོམ་པ་མཉམ་པར་འདོར་བ་དང་། གོམ་པ་མདུན༌[^2761]དུ་ཐལ་བར་འདོར་བ་དག་གིས་བཅག་པར་མི་བྱའོ། །

[Block 2916]
སྟན་ཆེས་དམའ་བ་ཉིད་ལས་གཞན་དུ་མི་འདུག་པ་དང་། ཕྱི་བཞིན་འབྲང་བའི་དགེ་སྦྱོང་གི་བདག་ཉིད་ཀྱིས་ཁྱིམ་དག་ཏུ་འགྲོ་བ་སྟེ་གཞན་དུ་ན་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2917]
དེ་གཉིས་འདུག་པ་ནི་དགེ་སློང་རང་བཞིན་དུ་གནས་པ་དང་ལྷན་ཅིག་ཏུ་སྟན་ཆེས་དམའ་བ་ལ་འདུག་པར་བྱའི༌[^2762]མཉམ་པའམ༌[^2763]ཤིན་ཏུ་མཐོ་བ་ལ་འདུག་པར་མི་བྱའོ། །

[Block 2918]
གཉིས་གྲོང་དུ་འགྲོ་བས་རང་བཞིན་དུ་གནས་པའི་དགེ་སློང་གིས་ཕྱི་བཞིན་དུ་འབྲང་བའི་དགེ་སྦྱོང་གི་ཆོས་ཀྱིས་འགྲོ་བར་བྱའི་མདུན་དུ་འགྲོ་བའི་དགེ་སྦྱོང་གིས༌[^2764]ཆོས་ཀྱིས་ནི་མི་བྱའོ། །

[Block 2919]
གཡོགས་མ་གཅིག་ཏུ་མལ་བཤམ་པར༌[^2765]མི་བྱའོ། །

[Block 2920]
དེ་གཡོགས་མ་གཅིག་ཏུ་མལ་མི་བཤམ་པ༌[^2766]དང་ཡོངས་སུ་གནས་པ་དག་མགུ་བར་བྱ་བ་སྤྱོད་པ་དེ་གཉིས་ཀྱིས་དགེ་སློང་རང་བཞིན་དུ་གནས་པ་དང་ལྷན་ཅིག་ཏུ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2921]
རབ་ཏུ་བྱུང་བ་དང་བསྙེན་པར་རྫོགས་པ་དང་གནས་སྦྱིན་པ་དང་། དགེ་ཚུལ་ཉེ་བར་གཞག་པ་དག་མི་བྱའོ་ཞེས་བྱ་བ་ནི་དེ་གཉིས་ཀྱིས་རབ་ཏུ་དབྱུང་བར༌[^2767]མི་བྱ་བསྙེན་པར་རྫོགས་པར་མི་བྱ༌[^2768]གནས་སྦྱིན་པར་མི་བྱ་དགེ་ཚུལ་ཉེ་བར་གཞག་པར་མི་བྱ་བའོ། །

[Block 2922]
གསོལ་བ་དང་བརྗོད་པ་དག་ཁས་མི་བླང་ངོ་ཞེས་བྱ་བ་ནི་གཉིས་ཀྱིས་གསོལ་བ་དང་བརྗོད་པའི་ལས་དག་བྱེད་དུ་བཅུག་པ་ཁས་བླང་བར་མི་བྱའོ། །

[Block 2923]
ལས་བྱེད་པ་དང་དགེ་སློང་མའི་སྟོན་པ་དང་། དགེ་འདུན་གྱི་ཡིད་བརྟན་པར་བསྐོ་བ་ཡང་ངོ་ཞེས་བྱ་བ་ཡང་ཁས་མི་བླང་ངོ་ཞེས་བྱ་བར་སྦྱར་ཏེ། དགེ་འདུན་གྱི༌[^2769]ཡིད་བརྟན་པ་ཞེས་བྱ་བ་ནི་གནས་ཁང་བསྐོ་བ་ལ་སོགས་པའོ། །

[Block 2924]
ལས་བྱེད་པར་བསྐོ་བ་དང་། དགེ་སློང་མའི་སྟོན་པར་བསྐོ་བ་དང་། དགེ་འདུན་གྱི་ཡིད་བརྟན་པར༌[^2770]བསྐོ་བ་ཁས་བླང་བར་མི་བྱའོ་ཞེས་བྱ་བའི་བསྐོ་བ་དེ་དག་ལ་བརྩལ་བར༌[^2771]མི་བྱའོ། །

[Block 2925]
སྔར་བསྐོས་པས་ཀྱང་མི་བྱའོ་ཞེས་བྱ་བ་ནི་དེ་གཉིས་ལས་བྱེད་པ་པོ་ལ་སོགས་པ་དག་ཏུ་སྔར་བསྐོ༌[^2772]ན་ཡང་བྱ་བ་བྱེད་དུ་མི་གཞུག་གོ། །

[Block 2926]
དགེ་སློང་མ་རྣམས་ལ་ཡང་བསྟན་པར་མི་བྱའོ་ཞེས་བྱ་བ་ཡང་སྔར་བསྐོས་ན་ཡང་ཞེས་བྱ་བའི་རྗེས་བསྙེགས་པའི་ཕྱིར་ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲ་སྨོས་སོ། །

[Block 2927]
འདོན་པ་དང་གཞན་ཡོད་ན་གསོ་སྦྱོང་ལས་སོ་སོར་ཐར་པ་གདོན་པར༌[^2773]མི་བྱའོ། །

[Block 2928]
དགེ་སློང་ལས་ཉམས་པས་གླེང་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ཡོངས་སུ་གནས་པ་དང་མགུ་བར༌[^2774]སྤྱོད་པ་དག་གིས་དགེ་སློང་ལ་གླེང་བར་མི་བྱའོ། །

[Block 2929]
དེ་གཉིས་ཀྱིས་དགེ་སློང་ལ་ཚུལ་ཁྲིམས་ཉམས་པ་དང་ལྟ་བ་ཉམས་པ་དང་ཆོ་ག་ཉམས་པ་དང་འཚོ་བ་ཉམས་པས་གླེང་བར་མི་བྱའོ། །ཅི་ཐམས་ཅད་ལ་གླེང་བར་མི་བྱའམ་ཞེ་ན། དེའི་ཕྱིར། དགེ་འདུན་ལས་མ་བཀར་བའོ་ཞེས་བྱ་བ་སྨོས་ཏེ་དགེ་འདུན་ལས་བཀར་བ༌[^2775]དེ་ལ་གླེང་བ་ལ་སོགས་པ་དག་ལ་ནི་བཀག་པ་མེད་དོ། །

[Block 2930]
དེ་དང་བརྟེན་པར༌[^2776]བྱའོ་ཞེས་བྱ་བ་ནས་འདི་ཐམས་ཅད་དུ་སྦྱར༌[^2777]བར་བྱའོ་ཞེས་བྱ་བའི་བར་དུ་རིག་པར༌[^2778]བྱའོ། །

[Block 2931]
མ་མོ་ལས་དེ་མི་བྱེད་པ་དང་བརྗོད་པར་བྱ་བ་ཉིད་དང་ཞེས་བྱ་བ་དེ་ཡང་སྦྱོར་བ་ཞེས་བྱ་བ་ནས་ཡིད་ལ་བྱེད་པ་ཞེས་བྱའི༌[^2779]བར་དུ་གསུངས་པ་ཡིན་ནོ། །

[Block 2932]
བརྗོད་པ་དང་བཅས་པ་ཉིད་དང་ཕུར་པ་དང་བཅས་པ་ཉིད་དག་མི་བྱའོ་ཞེས་བྱ་བ་ནི་དེ་གཉིས་ཀྱིས་དགེ་སློང་རང་བཞིན་དུ་གནས་པ་དགེ་འདུན་ལས་མ་བཀར་བ༌[^2780]ལས་བརྗོད་པ་དང་བཅས་པ་ཉིད་དང་ཕུར་བ་དང་བཅས་པ་ཉིད་དག་མི་བྱའོ། །

[Block 2933]
གདམས་ངག་དང་གསོ་སྦྱོང་དང་། དགག་དབྱེ་དང་གསོལ་བ་དང་བརྗོད་པ་དག་གཞག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་དེ་གཉིས་ཀྱིས་དགེ་སློང་རང་བཞིན་དུ་གནས་པ་དགེ་འདུན་ལས་མ་བཀར་བའི་གདམས་ངག་གཞག་པར་མི་བྱ་གསོ་སྦྱོང་གཞག་པར་མི་བྱ་གསོལ་བ་གཞག་པར་མི་བྱ་ལས༌[^2781]བརྗོད་པ་གཞག་པར་མི་བྱའོ། །

[Block 2934]
དེ་དང་བརྟེན་པར༌[^2782]མི་བྱའོ་ཞེས་བྱ་བ་ལ་དེ་དང་ཞེས་བྱ་བ་ནི་དགེ་འདུན་གྱིས་མ་བཀར་བའི་དགེ་སློང་ལས་སོ། །

[Block 2935]
ཆད་པ་དེའི་རྒྱུ་བྱས་པ་སྤོང་ངོ་ཞེས་བྱ་བ་ནི་ཆད་པ་གང་ལས་འདི་ཡོད་པ་ཉིད་དེ། རྒྱུ་གང་ལས་བྱས་པའི་དེ་སྤང་བར་བྱ་སྟེ་མི་སྤོང་བ་ཁ་ན་མ་ཐོ་བ་གཞན་དུ་འགྱུར་རོ། །

[Block 2936]
ཉེས་པ་གཞན་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཆད་པའི་ལས་ཀྱི་རྒྱུར་གྱུར་པ་ལས་གཞན་པའི་ཉེས་པ་ཡང་སྤང་བ་ཞེས་བྱ་བ་འཇུག་གོ། །

[Block 2937]
འདིར་གཞུང་ནི་དགེ་འདུན་གྱིས་དབྱུང་བའི་ལས་བྱས་པ་དེས་ལྟུང་བ་འབྱུང་བར་མི་འགྱུར་ཞིང་། དེ་དང་འདྲ་བ་གཞན་ཡང་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2938]
ཚངས་པ་མཚུངས་པར་སྤྱོད་པ་རྣམས་ལ་ཉེས་པ་དང་མཐུན་པ་ཉིད་ཀྱིས༌[^2783]མི་བྱའོ་ཞེས་བྱ་བ་ནི་གནས་ཐ་དད་པའི་ཚུལ་ལ་དེ་སྨོས་ཏེ་བྱེ་བྲག་མེད་པས་འདི་བསྡུ་བར་བྱས་སོ། །

[Block 2939]
བརྟུལ་ཞུགས་སྙིང་པོ་མེད་པར་འགྱུར་རོ་སྙམ་དུ་ཡིད་ལ་བྱའོ། །

[Block 2940]
ནང་པར་སྔར་ལངས་ཏེ་སྒོ་དབྱེ་བ་དང་མར་མེའི་ཀོང་བུ་བསལ་བར༌[^2784]བྱའོ། །

[Block 2941]
གཙུག་ལག་ཁང་དུ་ཆག་ཆག་དང་ཕྱག་དར་དང་ལྕི་བ་འཇམ་པོའི་བྱུག་པས་བསྐུ་བ་དག་ཀྱང་བྱའོ། །

[Block 2942]
བཤང་བ་དང་གཅི་བའི་སྐྱབས་དག་སྦྱང་ངོ་། །ས་ཕྱག་པ་དང་དུས་དང༌[^2785]མཐུན་པའི་ཆུ་དག་གཞག་པར་བྱའོ། །

[Block 2943]
ཝའི་ཁ་དག་བསལ༌[^2786]ལོ། །

[Block 2944]
སྟན་བཤམ་མོ། །

[Block 2945]
དུས་ཤེས༌[^2787]པར་བྱ་སྟེ་བདུག་སྤོས་དང་པོག་ཕོར་དག་ཉེ་བར་གཞག་གོ།[^2788] །གལ་ཏེ་ནུས་པ་ཉིད་ཡིན་ན་སྟོན་པའི་ཡོན་ཏན་ཡང་དག་པར་བསྒྲག་གོ། །
--- END BLOCKS ---
