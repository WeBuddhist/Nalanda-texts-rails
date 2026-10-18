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
[Block 4761]
དེ་བཞིན་དུ་ཆོས་ཀྱི་བར་དག་ལ་ཡང་བརྗོད་པར་བྱའོ། །

[Block 4762]
འོན་ཏེ་གཟུགས་དང་གང་ཟག་བཞིན་དུ་དེ་དག་དམིགས་པ་དག་ཀྱང་གཞན་དང་གཞན་མ་ཡིན་པ་ཉིད་དུ་བརྗོད་པར་མི་བྱའོ་ཞེ་ན། འོ་ན་ནི་དེས་ན་འདུས་མ༌[^3369]བྱས་ཀྱང་བརྗོད་པར་བྱ་བ་མ་ཡིན་པར་གྱུར་པས།[^3370] གྲུབ་པའི་མཐའ་ཉམས་པ་ཡིན་ནོ། །

[Block 4763]
གལ་ཏེ་ཡང་འདི་ཡོད་ལ་གཟུགས་རྣམས་ཞེས་ཀྱང༌[^3371]བརྗོད་པར་མི་བྱ། [^3372]གཟུགས་རྣམས་མ་ཡིན་ནོ་ཞེས་ཀྱང་བརྗོད་པར་མི་བྱ་ན། འོ་ན་ཅིའི་ཕྱིར་བཅོམ་ལྡན་འདས་ཀྱིས་གཟུགས་བདག་མ་ཡིན་པ་ནས།

[Block 4764]
རྣམ་པར་ཤེས་པ་བདག་མ་ཡིན་ཞེས་བྱ་བའི་བར་གསུངས།

[Block 4765]
མིག་གི་རྣམ་པར་ཤེས་པ་གང་གིས་གང་ཟག་འདི་དམིགས་པ་དེ་ཅི་གཟུགས་ལ་བརྟེན་ནས་སྐྱེ་འམ། འོན་ཏེ་གང་ཟག་གམ། གཉི་ག་ལ་བརྟེན་ནས་སྐྱེ། གལ་ཏེ་གཟུགས་རྣམས་ལ་བརྟེན་ནས་སྐྱེ་ན་ནི་སྒྲ་ལ་སོགས་པ་བཞིན་དུ་གང་ཟག་དམ༌[^3373]པར་ཤེས་པར་མི་ནུས་ཏེ། ཡུལ་གང་ཁོ་ན༌[^3374]ལ་བརྟེན་ནས་རྣམ་པར་ཤེས་པ་སྐྱེ་བ་དེ་ཉིད་དེའི་དམིགས་པའི་རྐྱེན་ཡིན་ནོ། །

[Block 4766]
འོན་ཏེ་གང་ཟག་གམ། གཉི་ག་ལ་བརྟེན་ནས་སྐྱེའོ་ཞེ་ན། འདི་ནི་མདོ་ལས་ཐལ་བ་ཡིན་ཏེ། མདོ་ལས་ནི། གཉིས་ལ་བརྟེན་ནས་རྣམ་པར་ཤེས་པ་སྐྱེ་བ་ཡིན་ནོ་ཞེས་ངེས་པར་གཟུང༌[^3375]ངོ་། །དེ་བཞིན་དུ་དགེ་སློང་མིག་གི་རྣམ་པར་ཤེས་པ་སྐྱེད་པ་ལ། རྒྱུ་ནི་མིག་ཡིན་ནོ། །

[Block 4767]
རྐྱེན་ནི་གཟུགས་རྣམས་ཡིན་ནོ། །

[Block 4768]
དེ༌[^3376]ཅིའི་ཕྱིར་ཞེ་ན། མིག་གི་རྣམ་པར་ཤེས་པ་གང་ཅི་ཡང་རུང་བ༌[^3377]དེ་ཐམས་ཅད་ནི་མིག་དང་གཟུགས་རྣམས་ལ༌[^3378]བརྟེན་ནས་སྐྱེའོ་ཞེས་གསུངས་སོ། །

[Block 4769]
དེ་ལྟ་ན་ནི་གང་ཟག་མི་རྟག་པར་འགྱུར་ཏེ།

[Block 4770]
མདོ་ལས།

[Block 4771]
མིག་གི་རྣམ་པར་ཤེས་པ་སྐྱེད་པ་ལ་རྒྱུ་གང་དག་ཡིན་པ་དང་། རྐྱེན་གང་ཡིན་པ་དེ་དག་ཀྱང་མི་རྟག་པ་ཡིན་ནོ་ཞེས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 4772]
འོན་ཏེ་དེའི་དམིགས་པ་གང་ཟག་མ་ཡིན་ན་འོ་ན་ནི་དེས་རྣམ་པར་ཤེས་པར་བྱ་བ་མ་ཡིན་པར་འགྱུར་རོ། །

[Block 4773]
གལ་ཏེ་ཡང་གང་ཟག༌[^3379]རྣམ་པར་ཤེས་པ་དྲུག་གིས་རྣམ་པར་ཤེས་པར་བྱ་བ་ཡིན་པར་དམ་འཆའ་ན་ནི་དེ་རྣ་བའི་རྣམ་པར་ཤེས་པས་རྣམ་པར་ཤེས་པར་བྱ་བ་ཡིན་པའི་ཕྱིར་གཟུགས་ལས་གཞན་ཡིན་པར་འགྱུར་ཏེ། སྒྲ་བཞིན་ནོ། །

[Block 4774]
མིག་གི༌[^3380]རྣམ་པར་ཤེས་པས་རྣམ་པར་ཤེས་པར་བྱ་བ་ཡིན་པའི་ཕྱིར་སྒྲ་ལས་གཞན་ཡིན་པར་འགྱུར་ཏེ་གཟུགས་བཞིན་ནོ། །

[Block 4775]
དེ་བཞིན་དུ་གཞན་དག་ལ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 4776]
བྲམ་ཟེ་དབང་པོ་ལྔ་པོ་འདི་དག་ནི་སྤྱོད་ཡུལ་ཐ་དད་པ་ཅན་ཡིན་ཞིང་ཡུལ་ཐ་དད་པ་ཅན་ཡིན་ཏེ། རང་རང་གི་སྤྱོད་ཡུལ་དང་ཡུལ་སོ་སོར་ཉམས་སུ་མྱོང་བ་ཡིན༌[^3381]གྱི་གཞན་གྱི༌[^3382]སྤྱོད་ཡུལ་དང་ཡུལ་ཉམས་སུ་མྱོང་བ་ནི་མ་ཡིན་པ་དག་སྟེ། འདི་ལྟ་སྟེ། མིག་གི་དབང་པོ་དང་། རྣ་བའི་དབང་པོ་དང་། སྣའི་དབང་པོ་དང་། ལྕེའི་དབང་པོ་དང་། ལུས་ཀྱི་དབང་པོ་ལྔའོ། །

[Block 4777]
[^3383]ཡིད་ཀྱི་དབང་པོ་ནི་དབང་པོ་ལྔ་པོ་འདི་དག་གི་སྤྱོད་ཡུལ་དང་ཡུལ་ཉམས༌[^3384]སུ་མྱོང་བ་ཡིན་ཞིང་། ཡིད་ཀྱི་དབང་པོ་ནི་འདི་དག་གི་རྟེན་ཡིན་ནོ་ཞེས་གསུངས་པའི་མདོའི་ཚིག་འདི་དང་ཡང་འགལ་བར་འགྱུར་རོ། །

[Block 4778]
ཡང་ན་གང་ཟག་ཡུལ་མ་ཡིན་པར་འགྱུར་རོ། །

[Block 4779]
གལ་ཏེ་ཡུལ་མ་ཡིན་ནོ་ཞེ་ན། འོ་ན་ནི་རྣམ་པར་ཤེས་པར་བྱ་བ་མ་ཡིན་པར་འགྱུར་རོ། །

[Block 4780]
གལ་ཏེ་དེ་ལྟ་ན་ཡིད་ཀྱི་དབང་པོ་ཡང་འཁྲུལ་པ་མེད༌[^3385]པར་འགྱུར་ཏེ།

[Block 4781]
སྲོག་ཆགས་དྲུག་པ་ལྟ་བུའི་མདོ༌[^3386]ལས།

[Block 4782]
དབང་པོ་དྲུག་པོ་འདི་དག་ནི་སྤྱོད་ཡུལ་ཐ་དད་པ་ཅན་ཡིན་ཞིང་ཡུལ་ཐ་དད་པ་ཅན་ཡིན༌[^3387]ཏེ། རང་རང་གི་སྤྱོད་ཡུལ་དང་ཡུལ་འདོད་པ་དག་ཡིན་ནོ་ཞེས་གསུངས་སོ། །

[Block 4783]
དེར་ནི༌[^3388]དབང་པོ་ཁོ་ན་ལ་དབང་པོ་ཡིན་པར་མ་གསུངས་ཀྱི༌[^3389]ལྔ་པོ་དང་དེ་དག་གི་རྣམ་པར་ཤེས་པ་རྣམས་ནི་མཐོང་བ་ལ་སོགས་པར་འདོད་མི་སྲིད་པའི་ཕྱིར་དེ་དག་གི་དབང་གིས་དྲངས་པའི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་ནི་དབང་པོ་ཡིན་པར་གསུངས་སོ། །

[Block 4784]
ཡིད་ཀྱི་དབང་པོ་འབའ་ཞིག་གིས་དྲངས་པའི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་གང་ཡིན་པ་དེ་ནི་དེ་ལས་གཞན་པ་དག༌[^3390]གི་སྤྱོད་ཡུལ་ལ་མི་འདོད་པ་ཉིད་པས་དེའི་ཕྱིར་དེ༌[^3391]ཉེས་པ་མེད་དོ། །

[Block 4785]
བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་དགེ་སློང་དག་མངོན་པར་ཤེས་པར་བྱ་བ་དང་། ཡོངས་སུ་ཤེས་པར་བྱ་བའི་ཆོས་ཀྱི་རྣམ་གྲངས་ཐམས་ཅད་བཤད་པར་བྱའོ་ཞེས་གསུངས་ནས། མངོན་པར་ཤེས་པར་བྱ་བ་དང་། ཡོངས་སུ་ཤེས་པར་བྱ་བ་ནི་མིག་དང་། གཟུགས་རྣམས་དང་། མིག་གི་རྣམ་པར་ཤེས་པ་དང་། མིག་གི་འདུས་ཏེ་རེག་པ་དང་། གང་ཡང་མིག་གི་འདུས་ཏེ་རེག་པའི་རྐྱེན་གྱིས་ནང་གི་ཚོར་བ་བདེ་བའམ། སྡུག་བསྔལ་བ་དང་། བདེ་བ་ཡང་མ་ཡིན་སྡུག་བསྔལ་བ་ཡང་མ་ཡིན་པ་སྐྱེ་བ་དེ་དང་ཞེས་བྱ་བ་ནས་ཡིད་ཀྱི་འདུས་ཏེ་རེག་པའི་རྐྱེན་གྱིས་ནང་གི་ཞེས་བྱ་བའི་བར་དུ་རྒྱས་པར་གསུངས་ཏེ། འདི་ནི་མངོན་པར་ཤེས་པར་བྱ་བ་དང་། ཡོངས་སུ་ཤེས་པར་བྱ་བའི་ཆོས་ཀྱི་རྣམ་གྲངས་ཐམས་ཅད་ཡིན་ནོ་ཞེས་གསུངས་སོ། །

[Block 4786]
དེའི་ཕྱིར་མངོན་པར་ཤེས་པར་བྱ་བ་དང་། ཡོངས་སུ་ཤེས་པར་བྱ་བ་ནི་དེ་སྙེད་ཅིག་ཡིན་པར་ངེས་པར་གཟུང་གི། གང་ཟག་ནི་མ་ཡིན་པས། དེ་ལྟ་བས་ན་འདི་རྣམ་པར་ཤེས་པར་བྱ་བ་ཡང་མ་ཡིན་ཏེ། ཤེས་རབ་དང་རྣམ་པར་ཤེས་པ་གཉིས་ནི་ཡུལ་འདྲ་བའི་ཕྱིར་རོ། །

[Block 4787]
གང་ཟག་པ༌[^3392]རྣམས་མིག་གིས་གང་ཟག་བལྟའོ་ཞེས་གང་ཟག་ལྟ་བ་ནི༌[^3393]བདག་མེད་པས་བདག་བལྟའོ༌[^3394]ཞེས་བྱ་བ་ཡིན་པས་བདག་ཏུ་ལྟ་བའི་གནས་སུ་གྱུར་པ་ཡང་ཡིན་ནོ། །

[Block 4788 [HEADING]]
#### ཕུང་པོ་རྣམས་ཁོ་ན་ལ་གང་ཟག་ཅེས་བྱ་བ། ^6-2-5-0

[Block 4789]
བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་མདོ་ལས།

[Block 4790]
ཕུང་པོ་རྣམས་ཁོ་ན་ལ་གང་ཟག་ཅེས་བྱའོ་ཞེས་འདི་ངེས་པར་མཛད་དོ། །

[Block 4791]
ངེས་པའི་དོན་གྱི༌[^3395]མདོ་ལས་ཀྱང་། མིག་དང་གཟུགས་རྣམས་ལ་བརྟེན་ནས་མིག་གི་རྣམ་པར་ཤེས་པ་སྐྱེའོ། །

[Block 4792]
གསུམ་འདུས་པས་ནི་རེག་པའོ། །

[Block 4793]
ལྷན་ཅིག་སྐྱེས་པས༌[^3396]ནི་ཚོར་བ་དང་འདུ་ཤེས་དང་སེམས་པ་དག་སྟེ། དེ་ལྟར་ན་གཟུགས་ཅན་མ་ཡིན་པའི་ཕུང་པོ་དེ་བཞིན༌[^3397]དང་། གཟུགས་ཅན་མིག་གི་དབང་པོ་དང་དེ་སྙེད་ཅིག་ལ་མི་ཉིད་ཅེས་བྱའོ། །

[Block 4794]
འདི་ལ་སེམས་ཅན་དང་། མིང་དང་ཤེད་ལས་སྐྱེས་དང་། ཤེད་བུ་དང་། གསོ་བ་དང་། གང་ཟག་དང་། སྲོག་དང་། སྐྱེ་བོ་ཞེས་བྱ་བ་འདི་ནི༌[^3398]མིང་ཡིན་ནོ། །

[Block 4795]
འདི་ལ་བདག་གིས༌[^3399]མིག་གི༌[^3400]གཟུགས་རྣམས༌[^3401]བལྟའོ་ཞེས་བྱ་བ་འདི་ནི་ཁས་འཆེ་བ་ཡིན་ནོ། །

[Block 4796]
འདི་ལ་ནི༌[^3402]འདི་ལྟར་ཚེ་དང་ལྡན་པ་དེའི་མིང་ནི་འདི་ཞེས་བྱ། རིགས་ནི་འདི་ཞེས་བྱ། རུས་ནི་འདི་ཞེས་བྱ། ཁ་ཟས༌[^3403]ནི་འདི་ལྟ་བུ་ཞིག་ཟ་ཟ། བདེ་བ་དང་སྡུག་བསྔལ་ནི་འདི་ལྟ་བུ་ཞིག་མྱོང་། ཚེ་ནི་འདི་ཙམ་ཞིག་ཐུབ། ཡུན་ནི་ཇི་སྲིད་ཅིག་གནས། ཚེའི་མཐའ་ནི་འདི་ཙམ་ཞིག་གོ་ཞེས་བྱ་བ་འདི་ནི་ཐ་སྙད་ཡིན་ནོ། །

[Block 4797]
དགེ་སློང་དག་དེ་ལྟར་ན་འདི་དག་ནི་མིང་ཙམ། འདི་དག་ཁས་འཆེ་བ་ཙམ། འདི་དག་ནི་ཐ་སྙད་ཙམ་སྟེ། ཆོས་འདི་དག༌[^3404]ཐམས་ཅད་ནི་མི་རྟག་པ། འདུས་བྱས་པ། སེམས་པས་འཕངས་པ། རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་དག་ཡིན་ནོ་ཞེས་གསུངས་སོ། །

[Block 4798]
བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་ངེས་པའི་དོན་གྱི་མདོ་ལ་བརྟེན་པར་གསུངས་ཏེ། དེ་ལྟ་བས་ན་འདི་ནི་ཡང་དང་ཡང་དུ་བརྟག་པར་བྱ་བ་ཡིན་ནོ། །

[Block 4799]
དེ་བཞིན་དུ་བྲམ་ཟེ་ཐམས་ཅད་ཡོད་དོ་ཞེས་བྱ་བ་ནི་འདི་ལྟ་སྟེ། སྐྱེ་མཆེད་བཅུ་གཉིས་དག་ཏུ་ཟད་དོ་ཞེས་ཀྱང་གསུངས་སོ། །

[Block 4800]
གལ་ཏེ་གང་ཟག་འདི་སྐྱེ་མཆེད་མ་ཡིན་ན་ནི་དེ་ཡོད་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བར་གྲུབ་བོ། །
--- END BLOCKS ---
