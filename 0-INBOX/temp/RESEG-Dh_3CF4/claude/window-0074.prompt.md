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
[Block 2591]
དེ་གཉིས་དང་འདྲ་བར་གྱུར་པ་ཡིན་ནོ། །

[Block 2592]
རྟེན་དང་བརྟེན་པར་གྱུར་པ་ཉིད་དོ། །

[Block 2593]
ཚིག་རྐྱང་དང༌[^1649]ཚིགས་བཅད་དེ་དག་གིས་ནི་བྱང་ཆུབ་སེམས་དཔའ་བདག་ཉིད་ཀྱི་རྒྱུ་བསྟན་པའོ། །

[Block 2594]
ད་ནི་གང་གོང་དུ་བསྟན་པའི་དབང་ཕྱུག་ཕུན་སུམ་ཚོགས་པ་དང་རྗེས་སུ་མཐུན་པ་ཡིན་ཡང་སྙིང་རྗེ་ལྷོད་པར་མི་འགྱུར་རོ་ཞེས་བྱ་བ་དེ་ཉིད་སྒྲུབ་པའི་ཕྱིར། གང་གི༌[^1650]ཕྱིར་ལྷ་མ་ཡིན་རྣམས་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་བརྩམས་པ་ཡིན་ནོ། །

[Block 2595]
སྐལ་བ་ཆེ་བ་ནི༌[^1651]བསོད་ནམས་ཀྱི་ཚོགས་ཀྱི་ཁྱད་པར་རོ། །

[Block 2596]
དེས་བདེ་བ༌[^1652]ཐོབ་པ་ནི་འབད་པ་མེད་པར་རྙེད་པ་སྟེ། སྐལ་བ་ཆེ་བས་བདེ་བ་ཐོབ་པའོ། །

[Block 2597]
གང་གི་ཕྱིར་གང་ལས་དེའི་སྙིང་དྲེགས་པའི་དྲི་མ་ཅན་བྱེད་པར་གྱུར་པ་ནི་དེའི་ཕྱིར་དབང་ཕྱུག་ཕུན་སུམ་ཚོགས་པར་གྱུར་ཀྱང་སྙིང་བརྩེ་བ་ལྷོད་པར་མི་འགྱུར་རོ། །

[Block 2598]
བཤམས་པ་ཉིད་ཆས་པ་ཡིན་པའི་ཕྱིར་བཤམས་པ་ཆས་པའོ། །

[Block 2599]
དེ་རབ་ཏུ་ཆས་པ༌[^1653]ཡིན་པས་འཇིགས་འཇིགས་ལྟར་སྣང་བ་སྟེ། གླང་པོ་ཆེ་དང་། ཤིང་རྟ་དང་། རྟ་དང་། རྐང་ཐང་ལ་སོགས་པ་གང་གི་དཔུང་གི་ཚོགས་གང་ཡིན་པ་དེ་ནི། གླང་པོ་ཆེ་དང་། ཤིང་རྟ་དང་། རྟ་དང་། རྐང་ཐང་གི་དམག་བཤམས་པ་རབ་ཏུ་འཇིགས་འཇིགས་ལྟར་སྣང་བའོ། །

[Block 2600]
ཆོས་ཀྱི་བདག་ཉིད་ཡིན་ཡང་ཞེས་བྱ་བ་ལ་སོགས་པའི་དོན་ནི༌[^1654]འདི་ཡིན་ཏེ། ཆོས་ལ་བདག་ཉིད་སེམས་པ་གང་ཡིན་པ་དེ་ནི་ཆོས་ཀྱི་བདག་ཉིད་དོ། །

[Block 2601]
དེ་ལྟ་ཡིན་ཡང་གཞན་སྔོ་བ་ནི་གཞན་དག་ལ་མངོན་པར་མ་ངེས་པའོ། །

[Block 2602]
རོལ་པའི༌[^1655]བགེགས་སུ་གྱུར་པ་ནི་རོལ་པ་ལ་གནོད་པར་གྱུར་པ་སྟེ།

[Block 2603 [VERSE]]
རོལ་པའི་བགེགས་སུ་གྱུར་པ་ལས་ཡིད་བྱུང་བའོ། །
རོལ་པའི་བགེགས་གྱུར་ཡིད་འབྱུང་འགྲོ་བ་འཇིགས་པར་འགྱུར། །

[Block 2604]
ཞེས་བྱ་བ་ལ་འགྲོ་བ་ནི་རང་ལ་བརྟེན་པའི་སྐྱེ་བོའོ། །

[Block 2605]
ཚུལ་བཞིན་བྱ་བའི་རིགས་ཞེས་བྱ་བ་ལ་ཚུལ་ནི་ལུགས་ཏེ། ལུགས་ཉིད་རིགས་པ་ཡིན་པས་འདོད་པའི་དོན་ཐོབ་པར་བྱེད་པ་ནི་འདི༌[^1656]ཚུལ་བཞིན་བྱ་བའི་རིགས་པའོ། །

[Block 2606]
འདོད་པའི་དོན་ཐོབ་པར་བྱེད་པའི་རིམ་པ་ནི་འདུམ་པར་བྱ་བ་དང་། དབྱེ་བ་དང་། ཆད་པས་སྒྲུབ་པའོ། །

[Block 2607]
ལྷ་མ་ཡིན་དེ་དག་ནི་དེ་དག་ལས་ཆད་པས་བསྒྲུབ་པར་བྱ་བ་ཡིན་པར་མཐོང༌[^1657]སྟེ། ཐབས་གཞན་གྱིས་ནི་དེ་དག་བསྒྲུབ་པར་མ་མཐོང་བར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2608]
དམག་དྲང་བ་ལ་གཡེངས་པ་ནི༌[^1658]དམག་དྲང་གཡེངས་པའོ། །

[Block 2609]
ཡང་ན་དམག་དྲང་བ་ཉིད་གཡེངས་པ་ཡིན་པས་དམག་དྲང་གཡེངས་པའོ། །

[Block 2610]
དེ་ལ་མངོན་པར་ཕྱོགས་པ་ནི་དམག་དང༌[^1659]གཡེངས་ལ་མངོན་པར་ཕྱོགས་པ་སྟེ། དེ་ལ་མངོན་པར་ཕྱོགས་པར་གྱུར་པའོ། །

[Block 2611]
དེའི་དོན་ནི་འདི་ཡིན་ཏེ། ཅིའི་ཕྱིར་བྱང་ཆུབ་སེམས་དཔའ་ཆོས་མ་ཡིན་པ་དམག་དྲང་བ་ལ་མངོན་པར་ཕྱོགས་པར་གྱུར་ཞེ་ན། དེ་ལྟར་གྱུར་པ་དེའི་རྒྱུ་བསྟན་པ། དམག་དྲང་བ་ལ་མངོན་པར་ཕྱོགས་པའི་རྒྱུ་ནི་གསུམ་སྟེ། གཞན་གྱི་ཚུལ་མ་ཡིན་པ་ཞི་བར་བྱ་བའི་ཕྱིར་དང་བདག་ཉིད་ལ་བརྟེན་པ་རྣམས་ཀྱི་ཚུལ་མ་ཡིན་པ་ཞི་བར་བྱ་བའི་ཕྱིར་དང་། བདག་གིས་ཀྱང༌[^1660]དེ་གཉི་གའི་ཞི་བར་བྱེད་ནུས་པར་བདག་ཉིད་ལ་ཤེས་པའོ། །

[Block 2612]
ནུས་པ་དེ་ཡང་རྣམ་པ་གཉིས་ཏེ། གཙོ་བོའི་ནུས་པ་དང་། སྤྲོ་བའི་ནུས་པ་དང་ལྡན་པའོ། །

[Block 2613]
འོས་པ་ཡང་ཡིན་ལ་བསྒྲེང་བ་ཡང་ཡིན་པས་འོས་པ་བསྒྲེང་བའོ། །

[Block 2614]
ཡང་ན་ཟླ་མེད་པའི་གོས་བཟང་པོ་གང་ལ་ཡོད་པ་དེ་ནི་གོས་བཟང་པོ་འོས་པའོ། །

[Block 2615]
བསྒྲེང་བ་ཡང་ཡིན་ལ་གོས་བཟང་པོ་ཕྱར་བ་ཡང་ཡིན་པས་བསྒྲེང་བའི་གོས་བཟང་པོ་འོས་པར༌[^1661]ཕྱར་བའོ། །

[Block 2616]
བ་དན་ཡང་ཡིན་ལ་མཛེས་པ་ཡང་ཡིན་པས་བ་དན་མཛེས་པའོ། །

[Block 2617]
གོས་བཟང་པོ་འོས་པས་བ་དན་མཛེས་པར་ཕྱར་བའི་ཕྱིར༌[^1662]རྒྱལ་མཚན་བསྒྲེང་བ་གང་ཡིན་པ་དེ་ནི་གོས་བཟང་པོ་འོས་པས་བ་དན་མཛེས་པར་ཕྱར་བའི་རྒྱལ་མཚན་བསྒྲེང་བའོ། །

[Block 2618]
རིན་པོ་ཆེ་སྣ་ཚོགས་པ་ཉིད་ནི་རིན་པོ་ཆེའི་རྣམ་པ་སྣ་ཚོགས་པའོ། །

[Block 2619]
ཡང་ན་ནོར་བུ་དང་འདྲ་བའི་རིན་པོ་ཆེ་ནི་ནོར་བུ་རིན་པོ་ཆེའོ། །

[Block 2620]
རིན་པོ་ཆེ་སྣ་ཚོགས་པ་ནི་རིན་པོ་ཆེ་སྣ་ཚོགས་པ་སྟེ། དེ་རྣམས་ཀྱི་འོད་ནི་ནོར་བུ་རིན་པོ་ཆེ་སྣ་ཚོགས་ཀྱི་འོད་དོ། །

[Block 2621]
དེས་གསལ་བར༌[^1663]གྱུར་པ་ནི་གསལ་བར་སྣང་བའོ། །

[Block 2622]
རྒྱན་གདགས་པའི་གོ་རིམས་སུ་གྱུར་པ་ནི་རྒྱན་གདགས་པའི་གོ་རིམས་སོམོ། །

[Block 2623]
རྒྱན་གདགས་པའི་གོ་རིམས་དང་། ངེས་པར་བྱས་པ་དང་། ངོས་གཉིས་མཚོན་ཆ་རྣོན་པོ་རྣམ་པ་སྣ་ཚོགས་འབར་བས་མཛེས་པ་གང་ཡིན་པ་དེ་ནི་ལྷའི་གོས་དཀར་པོ་ཅན་ནོ། །

[Block 2624]
ཡོངས་སུ་བསྐོར་བ་ནི་ཤིང་རྟ་གོས་དཀར་པོ་ཅན་ཏེ། རྒྱ་མཚོའི་འགྲམ་དུ་ཐུག་པར་ཞེས་བྱ་བ་དེ་ནི་གང་གི་ཕྱིར་དེ་རྣམས་ཀྱི་རྒྱ་མཚོའི་འགྲམ་ན་གནས་ཏེ། དེས་ན་འགྲམ་དུ་ཡོད་པ་ཡིན་ནོ། །

[Block 2625]
ལྷ་མ་ཡིན་རྣམས་ཀྱི་སྔ་མ་ལྟར་འོང་བ་དེ་ཤེས་པ་སྟེ། རོལ་པའི་བགེགས་གྱུར་འགྲོ་བ་འཇིགས་པར་འགྱུར་བ་སྟེ། ལྷའི་འགྲོ་བའོ། །

[Block 2626]
དེས་ན་རྒྱ་མཚོའི་འགྲམ་ལ་ཐུག་པར་སྔོན་སུ་བར་བྱེད་པ་ཡིན་ནོ། །

[Block 2627]
འདུག་བཞིན་དུ་ཞེས་བྱ་བ་སྟེ་མཚོན་རྡེག་པར་བྱེད་དོ། །

[Block 2628]
ང་ནི་འདི་ན་ཞེས་སྨྲས་ནས་ཀྱང་རབ་ཏུ་རྡེག་པར་བྱེད་དོ། །

[Block 2629]
མཐོང་བཞིན་ཞེས་བྱས༌[^1664]ནས་ཀྱང་གཞན་དག་ལ་རྡེག་པར་བྱེད་དོ། །

[Block 2630]
ད་ནི་ཐར་པར་ག་ལ་འགྱུར་ཞེས་བྱས་ཤིང་ཡང་གཞན་དག༌[^1665]ལ་རབ་ཏུ་སྣུན་པར༌[^1666]བྱེད་དོ། །
--- END BLOCKS ---
