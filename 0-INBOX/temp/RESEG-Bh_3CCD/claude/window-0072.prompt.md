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
[Block 2521]
རྒྱུ་དེ་ཡང་འོད་གསལ་བའི་བདག་ཉིད་རྡོ་རྗེ་འཆང་ཆེན་པོ་ཉིད་དོ། །

[Block 2522]
ཡང་ན་བརྗོད་པ་ནི་རྒྱུད་ཀྱི་མིང་སྟེ་གསང་བ་འདུས་པ་ཞེས་བྱའོ། །

[Block 2523]
དེས་ནི་སྐུ་གསུང་ཐུགས་ཀྱི་ངོ་བོ་ཉིད་སངས་རྒྱས་ཐམས་ཅད་འདུས་པའི་བདག་ཉིད་དེ་རྡོ་རྗེ་སེམས་དཔའ་ཞེས་བསྟན་པར་འགྱུར་རོ། །

[Block 2524]
བརྗོད་པར་བྱ་བ་ནི་རིམ་པ་གཉིས་ཏེ། དེ་ལས་བསྐྱེད་པའི་རིམ་པ་ཞེས་བྱ་བ་དང་པོའི་སྦྱོར་བ་ལ་སོགས་པའི་ཏིང་ངེ་འཛིན་གསུམ་གྱི་ངོ་བོ་རྡོ་རྗེ་འཛིན་པའོ། །

[Block 2525]
རྫོགས་པའི་རིམ་པ་ཡང་རྡོ་རྗེ་བཟླས་པ་ལ་སོགས་པའི་རིམ་པའི་མཚན་ཉིད་དོ། །

[Block 2526]
དེ་ལ་རྒྱུ་དང་འབྲས་བུའི་ངོ་བོ་ཟུང་དུ་འཇུག་པ་ལྔ་པའི་ཏིང་ངེ་འཛིན་ལས་རྡོ་རྗེ་འཆང་ཆེན་པོའི་གོ་འཕང་ཐོབ་པར་འགྱུར་བ་དེ་ཡང་རྡོ་རྗེ་འཆང་ཉིད་དོ། །

[Block 2527]
བཅོམ་ལྡན་འདས་དེས་ལེའུ་དང་པོ་ལས་ལྷའི་རྣལ་འབྱོར་རྣམ་པ་གཉིས་བསྟན་ཏོ་ཞེས་འབྲེལ་པའོ། །

[Block 2528]
སྤྲུལ་པའི་དཀྱིལ་འཁོར་དུ༌[^1635]ཞེས་པ་ནི༌[^1636]རེག་བྱ་རྡོ་རྗེ་མའི་ཆོས་འབྱུང་བར༌[^1637]རོ། །

[Block 2529]
ཉན་པའི་བསྐལ་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་བཛྲ་དྷྲྀཀ་ཅེས་བྱ་བ་ལ་སོགས་པའི་ཕྱུང་བའི་སྔགས་ཀྱིས༌[^1638]དམ་ཚིག་གི་དཀྱིལ་འཁོར་སྤྲོས་ཏེ། དེ་ཉིད་ལ་རིག་མའི་དབང་བསྐུར་བ་བྱིན་ནས་ཞེས་པ་ནི་རིག་མའི་ཆོས་འབྱུང་བར་དབང་བསྐུར་བ་ནི་རིག་མའི་དབང་ངོ་། །བྱང་ཆུབ་ཀྱི་སེམས་ཀྱིས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2530]
བྱིན་ནས་ནི་བྱིན་གྱིས་བརླབ་པར་བྱས་ནས་སོ། །

[Block 2531]
དྲང་བ་དང་ངེས་པའི་དོན་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། དེ་ལ་བརྟགས་པའི་རིམ་པ་ནི་དྲང་བའི་དོན་གྱིས་སོ། །

[Block 2532]
རྫོགས་པའི་རིམ་པ་ནི་ངེས་པའི་དོན་གྱིས་སོ། །

[Block 2533]
ལེའུ་བཅུ་དྲུག་པ་ལས་དོན་གཞན་དག་རྙེད་པས་ཞེས་པ་ནི་དེ་ལ་ཡང་དོན་དེ་ཉིད་བསྟན་ཏོ། །

[Block 2534]
དེ་ལྟ་ན་བཅུ་དྲུག་པ་དང་ལེའུ་དང་པོ་དག་གི་བྱེ་བྲག་གང་ཡིན༌[^1639]ཞེ་ན། དོན་གཞན་དག་རྙེད་ནས་ཞེས་སྨོས་ཏེ། དེ་དང་འདྲ་བའི་དོན་བླངས་པ་ཡིན་གྱི་དེ་ཉིད་ནི་མ་ཡིན་ནོ་ཞེས་དགོངས་པའོ། །

[Block 2535]
ལྷའི་རྣལ་འབྱོར་རྣམ་པ་གཉིས་ནི་བསྐྱེད་པ་དང་རྫོགས་པའི་རིམ་པ་དག་དེ་ཉིད་རྟོགས་པ༌[^1640]དང་རྫོགས་པའི་རིམ༌[^1641]པར་བྱེད་པའི་ཐབས་སོ་སོར་བསྟན་ཞིང་གསུངས་པའོ། །

[Block 2536]
དེའི་དགོངས་པ་ནི་རྒྱལ་བུ་དོན་ཐམས་ཅད་གྲུབ་པས་བྱང་ཆུབ་སེམས་དཔའི༌[^1642]གནས་སྐབས་ལས་འདས་ཏེ་རྡོ་རྗེ་འཆང་བའི་སྐུ་ཐོབ་ནས་མ་འོངས་པའི་སེམས་ཅན་གྱི་ཁམས་རྗེས་སུ་གཟུང་བར་བྱ༌[^1643]བའི་ཕྱིར། འདོད་ཆགས༌[^1644]ཆེན་པོའི་ཚུལ་ཞེས་བྱ་བའི་ཏིང་ངེ་འཛིན་པ༌[^1645]སྙོམས་པར་ཞུགས་ཏེ། སྤྱན་ལ་སོགས་པ་རིགས་ཀྱི་ལྷ་མོ༌[^1646]བཞི་དང་གཟུགས་རྡོ་རྗེ་ལ་སོགས་པའི་ཡུལ་གྱི་ལྷ་མོ་ལྔ་སྤྲོས་ཏེ། དེ་དང་ལྷན་ཅིག༌[^1647]ཏུ་བདེ་བ་ཆེན་པོ་དམ་པ་རྗེས་སུ་མྱོང་ནས་དེ་དག་ཁོ་ན་རང་གི་སྐུ་ལ་འཇུག་པར་མཛད་ཅིང་སླར་ཡང་དེ་བཞིན་གཤེགས་པ་ལྔའི་གཟུགས་སུ་ཕྱིར་སྤྲོས་ཏེ། རིན་པོ་ཆེ་སྣ་བདུན༌[^1648]གཞལ་ཡས་ཁང་པའི་ནང་དུ་བཞུགས་པ་དེ་ལ་དེ་རྣམས་ཀྱིས༌[^1649]གསོལ་བ་གདབ་པ་གསན་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་གསང་བ་འདུས་པའི་དཀོན་པ༌[^1650]ཉིད་བསྟན་པར་བྱ་བའི་ཕྱིར་ཅང་མི་གསུང་བར་གྱུར་པས་སླར་ཡང་ཞུས་པར་གྱུར་ཏེ། དེ་ནས་དེ་དག་ནང་དུ་འཇུག་ཅིང་བཛྲ་དྷྲྀཀ་ཅེས་བྱ་བ་ལ་སོགས་པས་མི་བསྐྱོད༌[^1651]པ་རེག་བྱ་རྡོ་རྗེ་མའི་ཆོས་འབྱུང་བའི་ནང་དུ་པདྨ་དང་ཟླ་བའི་དཀྱིལ་འཁོར་གྱི་སྟེང་དུ་སྤྲོས་ནས་དེ་རྣམས་ལ་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱིས༌[^1652]དབང་བསྐུར་ཏེ་དེ་ལས་ཀྱང་ཕྱིར༌[^1653]སྤྲོས་ཏེ། སེམས་ཅན་གྱི་དོན་བྱེད་དུ་བཅུག་ནས་ཤར༌[^1654]ཕྱོགས་སུ་འཁོར་གྱི་རྣམ་པར་དགོད་ཅིང་། དབུས་ཀྱི་གཙོ་བོའི་བདག་ཉིད་རྡོ་རྗེ་འཆང་ཆེན་པོའི་གཟུགས་སུ་བཞུགས་པར་གྱུར་ཏོ། །

[Block 2537]
ལེའུ་བཅུ་དྲུག་པ་ལས༌[^1655]གསང་བ་ལྔའི་ལྷའི་འཁོར་ལོའི་རིམ་པ་གཉིས་ཀྱིས་འཆད་པར་འགྱུར་རོ། །

[Block 2538 [HEADING]]
#### ངག་གི་དོན། ^1-8-2-0

[Block 2539]
དེའི་ཕྱིར་ངག་གི་དོན་ནི་འདི་ཡིན་ཏེ། བཅོམ་ལྡན་འདས་རྡོ་རྗེ་འཆང་ཆེན་པོས་དང་པོའི་སྦྱོར་བ་དང་དཀྱིལ་འཁོར་རྒྱལ་བ་མཆོག་གི་ཏིང་ངེ་འཛིན་བསྟན་ནས་ཐུགས་ཀྱི་རྡོ་རྗེ་འཛིན་པའི་སྐུ་ལ་དམིགས་ཏེ། དཔལ་གསང་བ་འདུས་པའི་རྣལ་འབྱོར་གྱི་རྒྱུད་ཆེན་པོའི་རིམ་པ་གཉིས་རྗོད་པར་བྱེད་པ་བསྟན་པར་བྱ་བའི་ཕྱིར་དང་པོའི་ལེའུ་གསུངས་ཏེ། དེ་ལ་གཉིས་པ་ལས་ནི་ཞེས་པ་ནས་བརྩམས་ཏེ་དམ་ཚིག་དང་སྡོམ་པ་རབ་ཏུ་བསྟན་པ་ཡིན་ནོ་ཞེས་བྱ་བའི་བར་དུ་དོན་ནི་འདི་ཡིན་ཏེ། ལྷའི་རྣལ་འབྱོར་གཉིས་ཀྱིས་རྒོད་པ་སྐྱེས་པར་གྱུར་ན་དེ་ཉེ་བར་ཞི་བར་བྱ་བའི་ཕྱིར་རྫོགས་པའི་རིམ་པ་འབའ་ཞིག་གཙོར་གྱུར་པ་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་ལེའུ་གཉིས་པ་བསྟན་ཏོ། །

[Block 2540]
བསྐྱེད་པའི་རིམ་པ་ལས་དང་པོའི་སྦྱོར་བའི་ཏིང་ངེ་འཛིན་གྱི་ཡན་ལག་གོ། །

[Block 2541]
རྫོགས་པའི་རིམ་པ་ལས་སེམས་རྣམ་པར་དག་པ་ལ་སོགས་པའི་མཚན་ཉིད་ཀྱི་ཡན་ལག་གོ། །

[Block 2542]
དོན་དམ་པའི་བདེན་པ་འབའ་ཞིག་ལ་ཞུགས་པས་གཞན་གྱི༌[^1656]དོན་མི་འགྲུབ་པས་དེ་བསྒྲུབ་པར་བྱ་བའི་ཕྱིར། ཡོངས་སུ་དག་པའི་ལྷའི༌[^1657]རྣལ་འབྱོར་རྗོད་པར་བྱེད་པ་ནི་ལེའུ་གསུམ་པ་བསྟན་ཏོ། །

[Block 2543]
ཡོངས་སུ་དག་པའི་སྒྲ་ནི་རྣམ་པ་གཉིས་ཏེ། གཅིག་གིས་ནི་སྔགས་ཀྱི་སྐུ་བསྟན་པ་དང་། གཉིས་པས་ཡེ་ཤེས་ཀྱི་སྐུ་བསྟན་ཏོ། །

[Block 2544]
འདིར་ནི་གཉིས་ཀ་གཟུང་བ་ཡིན་ཏེ། དེས་ནི་སྦྱོར་བ་དང་པོའི་ཏིང་ངེ་འཛིན་གྱི་དབུས་ཀྱི་གཙོ་བོ་བསྐྱེད་པ་ནི། །ཡན་ལག་དང་པོ་སྟེ་རྣལ་འབྱོར་དུ་བཤད་དོ། །

[Block 2545]
ཡོངས་སུ་དག་པའི་སྒྲའི་ཡང་དོན་གཉིས་པ་ཉེ་བར་བླངས་པའི་ཕྱིར་ཕྲ་མོའི༌[^1658]རྣལ་འབྱོར་ཡང་རྣམ་པ་གསུམ་དུ་བཤད་དོ། །

[Block 2546]
དེ་ཡང་རྫོགས་པའི་རིམ་པ་ལས་རྡོ་རྗེ་བཟླས་པ་ལ༌[^1659]འདུས་སོ། །

[Block 2547]
སྐུ་རྫོགས་པ་ནི༌[^1660]དེ་བཞིན་གཤེགས་པའི་དབང་བསྐུར་བ་ཐོབ་པར་བྱ་བའི་ཕྱིར་ལེའུ་བཞི་པ་གསུངས་ཏེ། ཕྱིར་མི་ལྡོག་པ་དང་སློབ་མ༌[^1661]རྣམས་ལ་དབང་བསྐུར་བའི་ཆེད་དུ་ཐུགས་ཀྱི་དཀྱིལ་འཁོར་སོ་སོར་བསྟན་པའི་ཕྱིར་རོ། །

[Block 2548]
དེ་ནི་དཀྱིལ་འཁོར་རྒྱལ་བ་མཆོག་གི་ཏིང་ངེ་འཛིན་གྱི་ཡན་ལག་གོ། །

[Block 2549]
དབང་བསྐུར་བ་ཐོབ་པས་རྣལ་འབྱོར་གྱི་སྤྱོད་པ་གསུམ་གྱིས་དངོས་གྲུབ་ཐོབ་པ་ཡང༌[^1662]ཡིན་ཞེས་དེའི་ཕྱིར་ལེའུ་ལྔ་པ་བསྟན་ཏོ། །

[Block 2550]
ལས་ཀྱི་རྒྱལ་བ་མཆོག་གི་ཏིང་ངེ་འཛིན་གྱི༌[^1663]ཡན་ལག་གོ། །

[Block 2551]
ལེའུ་གསུམ་པ་ལས་བསྒྲུབས་པ་ལྷའི་རྣམ་པའི་སྐུ་ལ་སོགས་པ་བྱིན་གྱིས་རློབ་པའི་ཕྱིར་ལེའུ་དྲུག་པ་བསྟན་ཏོ། །

[Block 2552]
དད་པའི༌[^1664]སྦྱོར་བའི་ཡན་ལག་བཞི་པ་རྣལ་འབྱོར་ཆེན་པོ་ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 2553]
དེ་ཡང་ཉེ་བར་མཚོན་པ་ཡིན་ཏེ། དེ་ལ་ཡང་ཕྲ་མོའི་རྣལ་འབྱོར་ཞེས་བྱ་བ་རྫོགས་པའི་རིམ་པ་ཡང་བཤད་དོ། །

[Block 2554]
ལེའུ་བདུན་པ་ལ་ནི་ཁྱད་པར་གང་ཡང་མེད་དོ། །

[Block 2555]
འོན་ཀྱང་ལེའུ་ལྔ་པ་ལས་བཤད་པའི་རྣལ་འབྱོར༌[^1665]སྤྱོད་པའི་སྤྲོས་པ་ཉིད་བསྟན་ཏེ། ལས་ཀྱི་རྒྱལ་བ་མཆོག་གི་ཏིང་ངེ་འཛིན་གྱི་ཡན་ལག་གོ། །

[Block 2556]
གཙོང་བ་དང་མི་གཙོང་བའི༌[^1666]རྣམ་པར་རྟོག་པ༌[^1667]ཟློག་པ་མེད་པས་སྤྱོད་པའམ་སྔགས་ཀྱི་སྐུ་མི་འགྲུབ་པས༌[^1668]དེའི་ཕྱིར་གསང་བའི་དབང་བསྐུར་བ༌[^1669]སོ་སོར་བསྟན་པར༌[^1670]བྱེད་པ་ལེའུ་བརྒྱད་པ་གསུངས་སོ། །

[Block 2557]
དཀྱིལ་འཁོར་གྱི་རྒྱལ་བ་མཆོག་དང་ལས་ཀྱི་རྒྱལ་བ་མཆོག་གི་ཡན་ལག་གོ། །

[Block 2558]
ནན་གྱིས་སྦྱོར་བའི་ཏིང་ངེ་འཛིན་གྱིས༌[^1671]སེམས་ཅན་གྱི་དོན་འགྲུབ་ཅེས་ཤིན་ཏུ་རྨད་དུ་འབྱུང་བའི་ལུང་བསྟན་རྗོད་པར་བྱེད་པ་ལེའུ་དགུ་པ་བསྟན་ཏེ། [^1672]ལས་ཀྱི་རྒྱལ་བ་མཆོག་གི་ཡན་ལག་གོ། །

[Block 2559]
དེ་བཞིན་གཤེགས་པའི་ཐུགས་ཀྱི་སྙིང་པོས་བསྐུལ་བས༌[^1673]སེམས་ཅན་གྱི་དོན་དང་དངོས་གྲུབ་མངོན་དུ་འགྱུར་བས་དེའི་ཆེད་དུ་བསྡུམས་དང་། སྦྱིན་པ་དང་། དབྱེས་དང་། འཆད་པ་ཞེས་བྱ་བ་ཐབས་བཞི་གཙོར་གྱུར་པ་ལེའུ་བཅུ་པ་གསུངས་སོ། །

[Block 2560]
དང་པོའི༌[^1674]སྦྱོར་བའི་ཏིང་ངེ་འཛིན་གྱི་ཤིན་ཏུ་རྣལ་འབྱོར་ཅེས་བྱ་བ་ཡན་ལག་གསུམ་པའོ། །
--- END BLOCKS ---
