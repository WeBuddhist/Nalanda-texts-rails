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

[Block 2631]
དེ་ལྟར་སྨྲས་ནས་གཞན་དག་ལ་ཐོབ་ཅིག་ཅེས་སྨྲས་ཏེ་ཕྱིར་ལོག་པ་དང་། དེ་དག༌[^1667]ལས་གཞན་དག་གིས་ཀྱང་མཚོན་འདེབས་པར་བྱེད་ཅིང་། ད་ནི་མེད་ཟིན་གྱིས་ཞེས་སྨྲས་ཏེ་མཚོན་འདེབས་པར་བྱེད་དོ། །

[Block 2632]
མཚོན་ཆ་འཁྲུགས་པ༌[^1668]ནི་གཡུལ་དུའོ། །

[Block 2633]
གློག་བཞིན་དུ་འགྱུ་བའི༌[^1669]བ་དན་ཅན་གང་དག་ནི་ཤིང་རྟ་སྟེ། དེ་ནི་གློག་ལྟར་འགྱུ་བའི་བ་དན་ཅན་ནོ། །

[Block 2634]
གདུགས་དང་། རྒྱལ་མཚན་དང་། གོ་ཆ་དང་། མཚོན་ཆ་དང་། ཅོད་པན་རྣམས་ཏེ། [^1670]དེ་དག་ལྷུང་བར་གྱུར་པ་ནི་འགྱེལ་བར་གྱུར་པའོ། །

[Block 2635]
ཕོག་པར་གྱུར་པ་ནི་ལམ་དུ་སྟེ་ཕོག་པར་གྱུར་པའི་སྟེང་དུའོ། །

[Block 2636]
དེར་བབ་པ་ནི་ཕོག་པར་གྱུར་པའི་སྟེང་དུ་བབ་པའོ། །

[Block 2637]
ཁ་ལོ་པ་ནི་ཁ་ལོ་སྒྱུར་བའོ། །

[Block 2638]
ཕྲུ་གུ་མ་ཚར་བ་ཞེས་བྱ་བ་ནི་གཤོག་པ་མ་སྐྱེས་པའོ། །

[Block 2639]
མ་ཚར་བ་ཉིད་བྱ༌[^1671]ཡིན་པས་བྱའི་ཕྲུ་གུ་སྟེ། བྱ་ཕྲུག་མ་ཚར་བ་དེའི་ཚང༌[^1672]བཅས་པའོ། །

[Block 2640]
ལྷ་མ་ཡིན་འདི་དག་ང་ཅུང་སླར་མི་ལྡོག་གོ་ཞེས་བྱ་བ་དང་། ཅི་ཞེས་བྱ་བ་ནི་སྐྱོན་ཅི་ཡོད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 2641]
ཤིང་རྟ་མ་བཟློག་པར་ནམ་མཁའ་ལྡིང་གི་ཚང་ལས་བཟུར་བར་མི་ནུས་པའི་ཕྱིར་རོ། །

[Block 2642]
ཤིང་རྟ་བཟློག་པ༌[^1673]དེ་ལས་ཉེས༌[^1674]པ་མེད། །ཅེས་པ༌[^1675]དེའི་དབང་དུ་བྱས་ནས་ཤིང་རྟ་འདི་ནི་སླད་དུ་བཟློག༌[^1676]ན་གདོད་ཅེས་བྱ་བའི་ཚིགས་བཅད་བརྩམས་པ་ཡིན་ཏེ། ནམ་མཁའ་ལྡིང་གི་ཚང་འདི་ལས་ཟུར་ཅིག་ཅེས་བྱ་བའི་ལས༌[^1677]ནི། ཤིང་རྟ་འདི་ནི་སླད་དུ་བཟློག་ན་གདོད་ཅེས་བྱ་བའི་ཚིགས་བཅད་ཕྱེད་ཡིན་ནོ། །

[Block 2643]
འོ་ན་ཅི་ཞེས་བྱ་བའི་ལན་ནི་ལྷ་རྣམས་ལ་ནི་ཞེས་བྱ་བ་སྟེ། ཚིགས་བཅད་ཀྱི་ཕྱེད་འོག་མའོ། །

[Block 2644]
དེ་བས་ན༌[^1678]ཞེས་བྱ་བ་ནི་ཤིང་རྟ་བཟློག་པ་ལ་ནི་ཉེས་པ་ཡོད་དོ་ཞེས་གོང་དུ་མ་ཏ་ལིས་སྨྲས་པའི་ཚིག་གོ། །

[Block 2645]
ལྷ་རྣམས་ལ་ནི་གནས་ནས་སྐབས་རྙེད་པ་ཞེས་བྱ་བ་འདིའི་ལན་ནི་མཚོན་གྱིས་ཕོག་སྟེ་ཤི་བ་བླས༌[^1679]ཞེས་བྱ་བ་ཡིན་ཏེ། རང་གི་ལྷག་པའི་བསམ་པ་ཁྱད་པར་ཅན་བསྟན་པའི་ཕྱིར་སྨྲས་པའོ། །

[Block 2646]
ཤི་ཡང་བླས༌[^1680]ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་སྙིང་རྗེའི་དབང་གིས་སྨྲས་པ་སྟེ།[^1681] དེ་ལྟར་སྤྱོད་པའི་སེམས་ཅན་འཇིགས་པས་ཉེན་པ་འདིའི་ཆེད་དུའོ། །

[Block 2647]
འཇིགས་པས་བརྟབས་ཤིང་རབ་ཏུ་མགྱོགས་པར་གྱུར་པ་གང་ཡིན་པ་དེ་ནི་སྐྲག་ནས་བརྟབས་ཤིང་རབ་ཏུ་མགྱོགས་པར་བྱེད་པའོ། །ཇི་ལྟ་བུར༌[^1682]ཞེ་ན། ཆར་སྤྲིན་ནག་པོ་རླུང་གིས༌[^1683]གཏོར་བ་བཞིན། །བདག་གི་དམག་ཚོགས་ཕམ་ཡང་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ནོ། །

[Block 2648]
དགའ་བ་དང་ངོ་ཚ་བ་ནི་དགའ་ཞིང་ངོ་ཚ་བའོ། །

[Block 2649]
དགའ་བ་དང་ངོ་ཚ་བ་དང་བཅས་པ་ནི་དགའ་ཞིང་ངོ་ཚ་བཞིན་དུའོ། །

[Block 2650]
ཕོངས་ན་ཞེས་བྱ་བའི་སྒྲ་ནི་ངན་པ་དང་བློ་འབྲིང་པོ་གཉི་ག་ལ་སྦྱར་བར་བྱའོ། །

[Block 2651]
ངན་པ་དང་བློ་འབྲིང་པོ་ནི་སྡིག་པ་སྤྱོད་པའི་ཚེ་ན་མི་མཉམ་པ་སྟེ། སྙིང་རྗེ་དང་བཅས་པས་སོ། །

[Block 2652]
སྐྱེ་བོ་དམ་པ་རྣམས་ཀྱི་ཁྱད་པར་ནི་འདི་ཡིན་ཏེ། རྣམ་པ་ཐམས་ཅད་དུ་སྡིག་པ་མི་བྱེད་དེ། སྙིང་རྗེ་དང་བཅས་པར་གྲུབ་པ་ཡིན་པས་ཡང་མི་བརྗོད་དོ། །

[Block 2653]
[^1684]སློབ་དཔོན་དཔའ་བོས་མཛད་པའི་སྐྱེས་པའི་རབས་རྒྱ་ཆེར་བཤད་པ་ལས་བརྒྱ་བྱིན་གྱི་སྐྱེས་པའི་རབས་སོ།། །།

[Block 2654 [HEADING]]
## བྲམ་ཟེའི་སྐྱེས་པའི་རབས། ^13-0

[Block 2655]
བདག་ངོ་ཚ་བ་ཉིད་ཀྱིས་ཞེས་བྱ་བ་ནི་ངོ་ཚ་བ་ཉིད་ཁྲེལ་ཡོད་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2656]
བདག་དང་ཆོས་ཀྱི་དབང་དུ་བྱས་ཏེ་ཁ་ན་མ་ཐོ་བ་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 2657]
སྤྱོད་ཡུལ་གྱི་དུས་ཞེས་བྱ་བ་ནི་ཚུལ་དང་སྤྱོད་པ་སྟེ་གང་བྱ་བའོ། །

[Block 2658]
རང་གི་ཆོས་ཞེས་བྱ་བ་ནི་འདོན་པ་དང་། འདོན་དུ་འཇུག་པ་དང་། མཆོད་སྦྱིན་བྱེད་པ་དང་། བྱེད་དུ་འཇུག་པ་དང་། སྦྱིན་པ་དང་། ལེན་པ་སྟེ། དེ་དག་ནི༌[^1685]རང་གི་ཆོས་སོ། །

[Block 2659]
རང་གི་ཆོས་དེ་དག་གི་རྗེས་སུ་སྤྱོད་པའི་གྲགས་པ་གང་ཡིན་པ་དེ་ནི་རང་གི་ཆོས་ལ་སྤྱོད་པའི་གྲགས་པའོ།[^1686] །འདུལ་བ་ནི་བྱ་བ་མ་ཡིན་པའི་ལས་ལ་སོགས་པ༌[^1687]ལས་ལྡོག་པ་སྟེ། ཇི་ལྟར་རིགས་པའི་སྒྲུབ་པའོ། །

[Block 2660]
བཙས་པའི་ཆོ་ག་བྱ་བ་ལ་སོགས་པས་ཞེས་སྨོས་པས་ནི་ལྷག་མཆོ་ག་བཅུ་གཉིས་ཀྱང་གཟུང་ངོ་། །ལྡོག་པ༌[^1688]དང་། འཛིན་པ་ནི་ལྡོག་པ༌[^1689]དང་འཛིན་པ་དག་སྟེ། ཐོབ་པ༌[^1690]ལྡོབ་ཅིང་འཛིན་པ་དེ་གཉིས་ལ་གང༌[^1691]གསལ་བར་གྱུར་པ་ནི་ཐོབ་པ༌[^1692]ལྡོབ་ཅིང་འཛིན་པ་གསལ་བའོ། །

[Block 2661]
འདི་དག་ནི་བྱ་བ་ཤེས་པ་དང་། སློབ་པའི་ཡན་ལག་ཡིན་ནོ། །

[Block 2662]
རྒྱུད་ཉིད་གུས་པ་ཡིན་པས་རྒྱུད་གུས་ཏེ། གུས་པའི་རྒྱུད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 2663]
དུལ་བ་ནི་བྱ་བ་རྣམས་ལ་བླ་མའི་རྗེས་སུ་འཇུག་པ་ཡིན་ཏེ། འདིས་ནི་བསླབ་པའི་ཡན་ལག་དང་ལྡན་པ་བསྟན་ཏོ། །

[Block 2664]
ཞི་ཞིང་ཆོས་བཟང་པོ་གང་ལ་ཡོད་པ་དེ་ནི་ཞི་ཞིང་ཆོས་བཟང་པོའོ།[^1693] །འདིས་ཀྱང་ཚུལ་ཁྲིམས་ཀྱི་ཡན་ལག་བསྟན་ཏོ། །

[Block 2665]
བྱམས་པ་ནི་ཆགས་པའོ། །
--- END BLOCKS ---
