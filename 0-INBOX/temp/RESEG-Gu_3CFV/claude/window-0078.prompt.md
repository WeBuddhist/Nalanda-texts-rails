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
[Block 2731]
དགེ་སློང་མ་ཆོམ་རྐུན་པས་ཀྱང༌[^1779]བཅོམ་པའི་དོན་ཉིད་དུ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བར༌[^1780]ནི་འདིར་དོན་གཅིག་ལ་མདུན་རོལ་དུ་སྲ་བརྐྱང་འབྱིན་པ་ལ་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2732]
གང་གི་ཚེ་དགེ་སློང་མ་ཆོམ་རྐུན་པ་དག་གིས་བཅོམ་པར་གྱུར་ན་དེའི་དོན་ཉིད་དུ་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ནི་བྱེ་བྲག་བཤད་མཚོ་ལས་ཤེས་པར་བྱའོ། །

[Block 2733]
སྲ་བརྐྱང་འབྱིན་པའི་སྤང་བའོ། །གང་ལ་མི་འབྱིན་པའི་སྤང་བར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་མི་འབྱིན་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སྲ་བརྐྱང་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2734]
མི་འབྱིན་པ་ཞེས་བྱ་བ་ནི་ཚོགས་པ་སྦྱིན་པར་མི་བྱེད་པར་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 2735]
དེ་ལ་ཞེས་བྱ་བ་ནི་གང་ཞིག་སྲ་བརྐྱང་འབྱིན་པའི་དོན་དུ་སྲ་བརྐྱང་འབྱིན་པའི་ལས་ལ་ཚོགས་པ་སྦྱིན་པ་ཞེས་བྱ་བ་ལྟུང་བྱེད་འབའ་ཞིག་པར་རྣམ་པར་གཞག་པ་དེ་ནས་འདི་ལ་དུས་ཀྱི་བྱེ་བྲག་ཙམ་གྱི་བྱེ་བྲག་ཤེས་པར་བྱའོ། །

[Block 2736]
སྲ་བརྐྱང་དབྱུང་བའི་དོན་དུ་ཚོགས་པ་སྦྱིན་པར་མི་བྱེད་པ་ལ་སྤང་བའི་ལྟུང་བྱེད་དོ། །

[Block 2737]
རྙེད་པའི་རྒྱུ་མཚན་རྗེས་སུ་མ་གནང་བ་ལ་ནི་མེད་པའི་ཕྱིར་རོ། །

[Block 2738]
སྲ་བརྐྱང་འབྱིན་པའི་དོན་དུ་ཚོགས་པ་སྦྱིན་པར་མི་བྱེད་པ་ལ་ནི་ལྟུང་བྱེད་འབའ་ཞིག་ཏུ་འགྱུར་རོ། །

[Block 2739]
གང་གི་ཕྱིར་འདིར་རྙེད་པའི་རྒྱུ་མཚན་དུ་གྱུར་པ་མ་བྱས་པ་སྟེ། དེ་བས་ན་ཅི༌[^1781]སྙེད་པ་འདིར་ཚོགས་པ་སྦྱིན་པར་མི་བྱེད་པ་དེ་འདི་སྙེད་རྣམས་ལ་ལྟུང་བ་འདི་སྐྱེད་པ༌[^1782]ཡིན་པར་རིག་པར་བྱའོ། །

[Block 2740]
དུས་ནམ་གྱི་ཚེ་ན་མི་འབྱིན་པ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་དཔྱིད་ཟླ་ར་བའི་ཉའི་མདུན་རོལ་དུའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 2741]
སྲ་བརྐྱང་མི་འབྱིན་པའི་སྤང་བའོ། །གང་ལ་རིན་པོ་ཆེ་སློང་བའི་སྤང་བར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་དབྱིག་དང་གསེར་སློང་བ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདི་ལྟར་མདོ་འདི་ལས་མངོན་མཚན་ཅན་ཞེས་བྱ་བ་སྨོས་ཏེ། ཡང་དགེ་སློང་མ་བདག་གི༌[^1783]ཕྱིར་མངོན་མཚན་ཅན་སློང་ན་སྤང་བའི་ལྟུང་བྱེད་དོ་ཞེས་གསུངས་མོད་ཀྱི་དེའི་རྣམ་པར་འབྱེད་པ་ལས་ངོ་བོ་འདི་བཤད་པའོ། །

[Block 2742]
མངོན་མཚན་ཅན་ཞེས་བྱ་བ་ནི་དབྱིག་གམ་གསེར་ཞེས་གསུངས་ཏེ། དེ་དག་ཐམས་ཅད་ཀྱང་རིན་པོ་ཆེ་མཚོན་པའི་དོན་དུ་བྱེ་བྲག་མེད་པའི་ཕྱིར་ཏེ། དེ་ལ་གཙོ་བོར༌[^1784]རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 2743]
དེ་བས་ན་རིན་པོ་ཆེ་ཐམས་ཅད་ལ་འདིས་བསྟན་པ་ཉིད་དུ་ཤེས་པར་བྱའོ། །

[Block 2744]
འདིར་རིན་པོ་ཆེ་འགའ་ཞིག་ལ་མངོན་པར༌[^1785]བརྟེན་པ་ནི་མི་རིགས་པ༌[^1786]ཡིན་ཏེ། ཁྱད་པར་མེད་པའི་ཕྱིར་རོ། །

[Block 2745]
སློང་བ་སྔོན་དུ་བཏང་ནས་སྤང་བའི་ཡོད་པ་ཉིད་ནི་གླགས་རྙེད་པ་མ་ཡིན་ཏེ། འདིར་སློང་བ་གྲུབ་ལ་སྤང་བ་ཉིད་ཀྱི་ཡོད་པ་ཉིད་གླགས་རྙེད་པ་ནི་མ་ཡིན་ནོ། །

[Block 2746]
དེ་བས་ན་སློང་བ་ཉིད་ལ་ཐབས་ཀྱིས་འདི་བསྟན་པའོ། །

[Block 2747]
དེ་བས་ན་གང་ཞིག་འདིར་སློང་བའི་ཚིག་གོ། །

[Block 2748]
གང་དུ་སློང་བ་སྔོན་དུ་བཏང་ནས་ལེན་པ་ལ་ནི་སྤང་བར་བརྗོད་པ་དེ་ལ་ནི་འབྲས་བུ་དང་བཅས་པ་ཉིད་དོ། །

[Block 2749]
གང་དུ་འདིར་ཡང་མ་བླངས་པ་ལ་དབྱར་ཁང་གི་དགོས་པའི་དབང་གིས་སློང་བ་དང་། ལེན་པ་ལ་ཉེས་པ་མེད་དོ། །

[Block 2750]
དེ་བས་ན་འདིར༌[^1787]ཞུགས་པའོ། །

[Block 2751]
རིན་པོ་ཆེ་སློང་བའི་སྤང་བའོ། །

[Block 2752]
གང་ལ་གོས་ཟ་བ་ལས་གྱུར་པའི་སྤང་བར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་གཞན་གྱི་ཆེད་དུ་རྙེད་པའི་གོས་ཟས་སུ་བྱས་ཏེ་བཟའ་བའི་ཕྱིར་འཇོག་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཟས་ལས་གཞན་པ་གླེགས་བམ་བྲིས་པ་ལ་སོགས་པའི་ཆེད་དུ་རྙེད་པའི་གོས་ཟས་སུ་བསྒྱུར་ཞིང་བྱས་ཏེ། ཚོང་གིས༌[^1788]བསྒྱུར་བ་བཟའ་བར་བྱའོ་ཞེས་དེའི་ཕྱིར་ངེས་པར་འཇོག་པར་བྱེད་པའི་དོན་འདི་རྣམ་པར་ངེས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2753]
འདིར་དོན་གཞན་ཉིད་ལ་ནི་ཁྱད་པར་ཡོངས་སུ་བཟུང་བ་ཡོད་པ་མ་ཡིན་ཏེ། གཞན་གྱི་དངོས་པོ་ཞེས་བྱ་བ་ནི་འདིར་མདོའི་ཚིག་སྟེ། གཞན་གྱི་དངོས་པོ་ཞེས་བྱ་བ་ནི། དངོས་པོ་གཞན་ལ་ཡོངས་སུ་བསྔོས་པས་ཞེས་བྱ་བ་འདིའི་རྣམ་པར་འབྱེད་པའོ། །

[Block 2754]
དེ་བས་ན་འདིར་དོན་གཞན་ཉིད་ཙམ་ཁས་བླངས་པ་སྟེ། འདིར་ཁས་བླངས་པ་ཡིན་གྱི་ཁྱད་པར་བསྟན་པ༌[^1789]ནི་མ་ཡིན་ནོ། །

[Block 2755]
གོས་ཟ་བ་ལས་གྱུར་པའི་སྤང་བའོ། །

[Block 2756]
གང་ལ་གོས་ཀྱི་རྒྱུ་ཟ་བ་ལས་གྱུར་པ་དང་། མལ་ཆ་ཟ་བ་ལས་གྱུར་པ་དང་། དབྱར་ཁང་རྒྱུ་ཟ་བ་ལས་གྱུར་པའི་སྤང་བ་གསུམ་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་གོ་རིམས་བཞིན་དུ་གོས་དང་མལ་ཆ་དང་དབྱར་ཁང་གི་ཆེད་དུ་ཡང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཡོ་བྱད་གང་ཡང་རུང་བ་རྙེད་པ་ཟས་སུ་བྱ་སྟེ། བཟའ་བའི་ཕྱིར་འཇོག་པ་ལའོ་ཞེས་བྱ་བའི་རྗེས་སུ་བསྙེགས༌[^1790]པའི་ཕྱིར་མདོ་སྔ་མ་ལས་ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲ་སྨོས་སོ། །

[Block 2757]
གང་ཡང་རུང་བའོ་ཞེས་བྱ་བ་ནི་གོས་གཅིག་པུ་ལ་ནི་མ་ཡིན་ཏེ། སྒྲའི་རྗེས་སུ་འབྲངས་པས་འཇུག་པར་གྱུར་པ་རྣམས་བསལ་བའི་དོན་དུ་ཐ་སྙད་འདི་གདགས་སོ། །

[Block 2758]
གོས་རྒྱུ་ལ་སོགས་པ་ཟ་བ་ལས་གྱུར་པའི་སྤང་བའོ།། །།

[Block 2759]
གང་ལ་གང་གིས་བསྔོས་པ་བྱིན་གྱིས་རློབ་པའི་སྤང་བར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་དགེ་སློང་མའི་སྐྱེ་བོ་མང་པོའི་ཕྱིར་སྦྱོར་དུ་བཅུག་ནས་རང་ལ་ཡོངས་སུ་བསྒྱུར་བ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་སློང་མའི་བདག་ཉིད་ཀྱི་སྐྱེ་བོ་མང་པོའི་ཕྱིར་དངོས་པོ་སྦྱོར་དུ་བཅུག་པ་གང་ཡིན་པ་དེ་བདག་ལ་ཡོངས་སུ་སྒྱུར་བར་བྱེད་པ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2760]
སྐྱེ་བོ་རྣམས་ཀྱི་ཚོགས་ནི་སྐྱེ་བོ་སྟེ། སྐྱེ་བོ་བཞི་ཡན་ཆད་ལ་སོགས་པའོ། །

[Block 2761]
དེ་ལྟ༌[^1791]བས༌[^1792]ན༌[^1793]བཞི་ལ་སོགས་པ་ནི་སྐྱེ་བོ་མང་པོར་རྟོགས་པར་བྱའོ། །

[Block 2762]
དེ་ལྟར་ཡང་རྣམ་པར་འབྱེད་པ་ལས།

[Block 2763]
སྐྱེ་བོ་མང་པོ་ཇི་ལྟ་བ་བཞིན་དུ་དགེ་སློང་མའི་དགེ་འདུན་གྱི་ཕྱིར་ཡང་དེ་བཞིན་ནོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2764]
དགེ་སློང་མའི་དགེ་འདུན་གྱི་དོན་དུ་ཞེས་བྱ་བ་ཚིག་ཏུ་མ་སྨོས་པའི་ཕྱིར་དེའི་གནས་ཀྱི་ས་དང་ཉེ་བར་འགྲོ་བའི་དགེ་འདུན་ལས་ཕྱེད་བཅད་པའི་ཚོགས་ལས་ཇི་ལྟར་ཡིད་ཆེས་པར་འགྱུར། དེའི་ཁྱིམ་གྱི་གནས་དང་ཉེ་བར་འགྲོ་བའི་དགེ་འདུན་ཐམས་ཅད་ལ་མངོན་པར་བརྟེན་པ་ཉིད་ཀྱིས་རྟོགས་པར་མ་གྱུར་ཅིག་ཅེས་བྱ་བའི་ཕྱིར་དང་། འོག་ནས་ཀྱང་དགེ་འདུན་ཞེས༌[^1794]སྨོས་པར་བྱའོ། །

[Block 2765]
དགེ་སློང་གི་ཕྱིར་དང་རབ་ཏུ་བྱུང་བ་འདི་ལ་བསྙེན་པར་མ༌[^1795]རྫོགས་པའི་ཕྱིར་དང་། མུ་སྟེགས་ཅན་རབ་ཏུ་བྱུང་བའི་ཕྱིར་དང་། ཁྱིམ་པའི་ཕྱིར་སྦྱོར་དུ་བཅུག་པ་རང་ལ་ཡོངས་སུ་བསྒྱུར་བ་ན་ཉེས་བྱས་སུ་ཤེས་པར་བྱའོ། །

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
--- END BLOCKS ---
