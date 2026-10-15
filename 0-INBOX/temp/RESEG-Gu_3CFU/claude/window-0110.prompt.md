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
[Block 3851]
བླ་གོས་དང་མཐང་གོས་གཉིས་ནི་ཉིས་རིམ་དུ་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3852]
དུས་ཚིགས་སུ་སྤྱད་པའི་གོས་ནི་བགོ་ཟས་ཆུང་བ་ཉིད་དེ་ཞེས་བྱ་བ་འདི་གྲུབ་པའོ། །

[Block 3853]
གང་ཞིག་དུས་ཚིགས་གསུམ་པོ་དག་ལས་དུས་ཚིགས་གང་ཡང་རུང་བའི་དུས་ཚིགས་སུ་སྤྱད་པ་གང་ཡིན་པའོ་ཞེས་དུས་ཟད་པའི་ངོ་བོ་བརྗོད་པའོ། །

[Block 3854]
འདིར་ཟླ་བ་བཞི་པོ་ནི་དུས་སུ་རིག་པར་བྱའོ། །

[Block 3855]
ཕྱག་དར་ཁྲོད་ལས་བྱས་པ་དག་ལ་ནི་ངེས་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་རིམ་པ་རྣམས་ཤིན་ཏུ་མང་བ་ཉིད་ལ་ཡང་ངེས་པ་མེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3856]
འདིར་གཞུང་ནི་ཕྱག་དར་ཁྲོད་ལ་ནི་ཇི་ཙམ་འདོད་པར་བྱའོ་ཞེས་གསུངས་པ༌[^2651]ཡིན་ནོ། །

[Block 3857]
རྙིང་པ༌[^2652]ཉིད་དང་དེངས་པ་ཉིད་ནི་ཅི་དགོས་པ་ལྷག་པར་སྦྱར་རོ་ཞེས་བྱ་བ་ནི་ཕྱག་དར་ཁྲོད་མ་ཡིན་པ་དག་ལྷག༌[^2653]པར་སྦྱར་བར་བྱའོ། །

[Block 3858]
རྙིང་པ༌[^2654]ཉིད་ཅེས༌[^2655]བྱ་བ་ནི་རང་ཟད་པ་ཉིད་དོ། །

[Block 3859]
དེངས་པ༌[^2656]ཉིད་ཅེས་བྱ་བ་ནི་སྒོ་སྐྱེས་ཀྱི་བཤུང་བ་ལ་སོགས་པས་བསྲབས་པར་གྱུར་པའོ། །

[Block 3860]
ཅི་དགོས་པ་ཞེས་བྱ་བ་ནི་ཅི་ཙམ་དགོས་པ་སྟེ་ཇི་ཙམ༌[^2657]སྤྱད་པར་བྱ་དགོས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3861]
ལྷག་པར་ཞེས་བྱ་བ་ནི་རིམ་པའི་མཐའ་སྔར་བསྟན་པ་ལས་སོ། །

[Block 3862]
སྦྱར་རོ་ཞེས་བྱ་བ་ནི་ལྷན་པ་དག་གོ། །

[Block 3863]
མདོ་འདི་ནི་མ་མོ་ལས་གསུངས་པ་བསྡུས་པ་ཡིན་ནོ། །

[Block 3864]
ལྷག་པར་སྦྱར་བ་ཉིད་དུ་མི་བྱའོ་ཞེས་བྱ་བ་ལ་སྦྱར་བ་ནི་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་འདི་ལ་འདི་བསྟན་པའོ། །

[Block 3865]
སྤང་བར་འགྱུར་བ་ཉིད་ཀྱང་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ལྷག་པར་སྦྱར་བའི་རིམ་པ་དེ་ཞག་བཅུ་འདས་ན་སྤང་བའི་ལྟུང་བྱེད་དུ་རིག་པར་བྱའོ། །

[Block 3866]
རིག་པ་ཅན་བྱི་དོར་བྱས་ནས་འདི་ཉིད་དུ་སྦྱར་བར་བྱའོ་སྙམ་པའི་སེམས་མ་བསྐྱེད་པར་དབོག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ་མི་རུང་བར་གྱུར་པ་ནི་འདིར་དབོག་པར་བྱའོ། །

[Block 3867]
ཆོས་གོས་འདི་ཉིད་དུ་སྦྱར་བར་བྱའོ་སྙམ་པའི་སེམས་མ་བསྐྱེད་པར་དབོག་པར་མི་བྱའོ། །

[Block 3868]
འདི་ལྟ་བུའི་སེམས་ལ་མི་གནས་པ་ནི་སེམས་མ་བསྐྱེད་པར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3869]
གང་ཡང་རུང་བས་ཕོག་པ༌[^2658]མ་སྦྱར་བའི་སྔ་རོལ་དུ་སྤང་བར་འགྱུར་བ་ཉིད་དོ་ཞེས་བྱ་བ་ལ། གང་ཡང་རུང་བས་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་ཡང་རུང་བ་ཞེས་བྱ་བ་དེ་ལྟ་བུའམ་གཞན་པའི་སེམས་ཀྱིས་ཕོག་པ་དེའི་གཟུགས་ཉིད་དུ་གྱུར་པ་ལ་དེ་ཉིད་དོ། །

[Block 3870]
ཡང་དག་པར་སྦྱར་བ་ཉིད་ལ་བསྒྲུབ་པ་ཉིད་དུ་འགྱུར་ཏེ་ཞེས་བྱ་བ་འདི་ཤེས་པ་རིམ་པ་རྣམ་པར་གཞག་པའི་རྗེས་སུ་འབྲེལ་པས་བརྗོད་པ་ཡིན་ནོ། །

[Block 3871]
སྣམ་སྦྱར་གྱི་སྣམ་ཕྲན་དག་ནི་དགུ་ཡན་ཆད་ནས་ཉི་ཤུ་རྩ་ལྔ་མན་ཆད་དེ་ཟུང་མ་གཏོགས་སོ་ཞེས་བྱ་བ་ནི། འདིར་མཉམ་པ་ནི་ཟུང་ཉིད་ཀྱི༌[^2659]ཉེ་བར་མཚོན་པ་སྟེ། བཅུ་དང་བཅུ་གཉིས་དང་བཅུ་བཞི་དང་། བཅུ་དྲུག་དང་བཅོ་བརྒྱད་དང་། ཉི་ཤུ་དང་ཉི་ཤུ་གཉིས་དང་ཉི་ཤུ་བཞི་རྣམས་མ་གཏོགས་པར་ཞེས་བྱ་བ་འདིའི་དོན་ཏོ། །

[Block 3872]
ཅིའི་ཕྱིར༌[^2660]དེ་ལྷག་པའི་དུམ་བུ་རྣམས་ཀྱིས་སྣམ་སྦྱར་ཞེས་བྱ་བ་འདིར་རྒྱུ་བརྗོད་པ་ཡིན་ནོ། །

[Block 3873]
དེ་ཡན་ཆད་ནི་ཚེམ་བུའོ་ཞེས་བྱ་བ་ནི་གང་གི་ཕྱིར་ཚེམ་བུ་ཉིད་དེར་གྱུར་པ་དེ་བས་ན་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3874]
དང་པོ་གསུམ་པ་ལ་ནི་དེ་དག་གི་གླེགས་བུ་ཕྱེད་དང་གསུམ་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་སྣམ་སྦྱར་གསུམ་པ་དང་པོ་ལ་སྟེ། སྣམ་ཕྲན་དགུ་པ་དང་བཅུ་གཅིག་པ་དང་བཅུ་གསུམ་པའི་དུམ་བུ་འདི་རྣམས་ལ་གླེགས་བུ་ཕྱེད་དང་གསུམ་པ་ཉིད་དོ། །

[Block 3875]
གླེགས་བུ་ཕྱེད་དང་གསུམ་པ་རྣམས་ནི་དུམ་བུ་འདི་ལ་ངོ་བོ་སྟེ། དེ་བས་གླེགས་བུ་ཕྱེད་དང་གསུམ་པ་ནི་དེའི་དངོས་པོའོ། །

[Block 3876]
འདིར༌[^2661]སྣམ་ཕྲན་རྣམས་ནི་དུམ་བུ་ཉིད་དུ་རིག་པར་བྱའི་གླེགས་བུ་དང་ཕྱེད་པ་རྣམས་ལ་ནི་མི་བྱའོ། །

[Block 3877]
གཉིས་པ་ལ་ནི་གླེགས་བུ་ཕྱེད་དང་བཞི་པོ༌[^2662]ཉིད་དོ་ཞེས་བྱ་བ་ནི་སྣམ་སྦྱར་གསུམ་པ་གཉིས་པ་ལ་སྟེ། སྣམ་ཕྲན་བཅོ་ལྔ་པ་དང་བཅུ་བདུན་པ་དང་བཅུ་དགུ་པའི་སྣམ་སྦྱར་རྣམས་ལའོ། །

[Block 3878]
སྣམ༌[^2663]ཕྲན་དེ་རྣམས་ཀྱི་གླེགས་བུ་ཕྱེད་དང་བཞི་པ་ཉིད་དོ། །

[Block 3879]
གསུམ་པ་ལ་ནི་གླེགས་བུ་ཕྱེད་དང་ལྔ་པ་ཉིད་དོ་ཞེས་བྱ་བ་སྣམ་ཕྲན་ཉི་ཤུ་རྩ་གཅིག་པ་དང་ཉི་ཤུ་རྩ༌[^2664]

[Block 3880]
གསུམ་པ་དང་ཉི་ཤུ་རྩ༌[^2665]ལྔ་པའི་སྣམ་སྦྱར་རྣམས་ལའོ། །

[Block 3881]
བླ་གོས་ནི་སྣམ་ཕྲན་བདུན་དང་གླེགས་བུ་ཕྱེད་དང་གསུམ་པའོ། །

[Block 3882]
མཐང་གོས་ནི་སྣམ་ཕྲན་ལྔ་པ་དང་གླེགས་བུ་ཕྱེད་དང་གཉིས་པའོ། །

[Block 3883]
དེ་གཉིས་ནི་ཆོས་གོས་བྱིན་གྱིས་བརླབ་པའི༌[^2666]སྔགས་ལས་ཤེས་པར་བྱའོ། །

[Block 3884]
བྱིན་གྱིས་བརླབ་ཏུ་རུང་བ་ཆེན་པོ་དག་ནི་རང་གི་ཁྲུ་གསུམ་དང་ལྔ་དག་གོ་ཞེས་བྱ་བ་ནི་ཞེང་དུ་ཁྲུ་གསུམ་ཆུར་ཁྲུ་ལྔ་ནི་གང་རྣམས་ཀྱི་ཚད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3885]
ཕྱོགས་གཅིག་ལ་ཡང་ཚད་ལས་ལྷག་པར་བྱེད་ན་སྤང་བར་འགྱུར་བ་ཉིད་དོ། །

[Block 3886]
དེ་བས་ན་ལྟུང་བ་ལས་ལྷག་པའི་དོན་ཉིད་ཀྱིས༌[^2667]འདི་ལྟར་བརྗོད་པ་ལ་སྐྱེས་པ་ཉིད་ཀྱིས་དེ་བཞིན་དུ་རིམ་པ་དུ་མ་བྱའོ་སྙམ་པའི་བསམ་པས་མཚམས་སྦྱར་བ་ལ་ཇི་སྲིད་དུ་རིམ་པ་རིགས་པ་ཉིད་བྱེད་པ་མངོན་པར་འདོད་པ་དེ་ཙམ་གྱི་རིམ་པ་ཉིད་ཀྱིས་ཞུགས་ལ་ཚད་གང་ཡིན་པ་དེ་ནི་དེ་ལས་ལྷག་པར་བྱེད་ན་ཡང་སྤང་བར་འགྱུར་བ་ཉིད་དུ་ཤེས་པར་བྱའོ། །

[Block 3887]
རིམ་པ་དུ་མ་བྱའོ་སྙམ་པའི་བསམ་པ་མེད་དེ་རིམ་པ་གཅིག་པའོ༌[^2668]སྙམ་པ་ལས་གང་ཞིག་ཚད་འདི་ལས་ལྷག་པར་བྱེད་དམ། དྲས་ཏེ་བྱའོ་སྙམ་པའི་བསམ་པ་ཡོད་པས་གཞག་པར་བྱ་བ་ལ་འདི་ནི་ཚད་དོ། །

[Block 3888]
དེ་ལས་ལྷག་པ་མེད་པ་མ་བཅད་པའི་ངོ་བོ་ཉིད་ཀྱིས་ཚད་འདི་གང་ཡིན་པ་དེ་ལས་ལྷག་པར་བྱེད་ན་སྤང་བར་འགྱུར་བར་རིག་པར་བྱའོ། །

[Block 3889]
ངོས་ཇི་ཙམ་པ་དེ་ཙམ་གྱི་བསམ་པས་འཇུག་པ་དེ་ཙམ་ལ་དེའི་དོན་ཉིད་ཀྱིས༌[^2669]ཉེས་པར་གྱུར་པ་ཉིད་མེད་དོ། །

[Block 3890]
གང་གི་ཕྱིར་མངོན་པར་བརྟེན་པ་དང་རིག་པ་ལས་མ་འདས་པའི་དོན་ལ་ལྷག་པར་གྱུར་པ་ཉིད་མ་ཡིན་པའོ། །
--- END BLOCKS ---
