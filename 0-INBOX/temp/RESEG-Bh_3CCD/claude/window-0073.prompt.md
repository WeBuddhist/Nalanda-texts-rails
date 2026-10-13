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

[Block 2561]
ལས་ཀྱི་རྒྱལ་བ་མཆོག་ཅེས་ལ་ལ༌[^1675]འདོད་དོ། །

[Block 2562]
དེ་བཞིན་གཤེགས་པའི་བྱིན་གྱིས་རློབ་པ་ཐོབ་པས་སྔགས་ཀྱི་སྐུ་རྣམ་པ་གཉིས་ཏེ། སྔགས་དང་ཡེ་ཤེས་ཀྱི་སྐུའོ། །

[Block 2563]
དེ་དག་གི་སླད་དུ་ལེའུ་བཅུ་གཅིག་པ་བསྟན་ཏོ། །

[Block 2564]
སྔགས་ཀྱི་སྐུ་ནི་དང་པོའི་སྦྱོར་བ་དང་དཀྱིལ་འཁོར་རྒྱལ་བ་མཆོག་གི་ཏིང་ངེ་འཛིན་གྱི་ཡན་ལག་གོ། །

[Block 2565]
ཡེ་ཤེས་ཀྱི་སྐུ་ནི་བདག་ལ་བྱིན་གྱིས་རློབ་པའི་ཡན་ལག་ཅེས་བྱའོ། །

[Block 2566]
སྤྲོས་པ་སྤང་བར་བྱ་བའི་ཕྱིར་སྐུ་རྣམ་པ་གཉིས་པོ་ཡང་ཕྱག་རྒྱ༌[^1676]ཆེན་པོར་ཡོངས་སུ་འགྱུར་བར་བྱ་བའི་ཆེད་དུ་ལེའུ་བཅུ་གཉིས་པ་བསྟན་ཏོ། །

[Block 2567]
སྔ་མ་བཞིན་དུ་དཀྱིལ་འཁོར་རྒྱལ་བ་མཆོག་གམ། ལས་ཀྱི་རྒྱལ་བ་མཆོག་གམ་བདག་ལ་བྱིན་གྱིས་རློབ་པའི་རིམ་པའི་ཡན་ལག་བསྟན་ཏོ། །

[Block 2568]
རིམ་པ་གཉིས་པ་ཡོངས་སུ་རྫོགས་པའི་རྣལ་འབྱོར་པས་འགྲོ་བའི་དོན་བྱ་བའི་ཕྱིར་ཞི་བ་ལ་སོགས་པའི་ལས་ཀྱི་ཚོགས༌[^1677]རབ་འབྱམས་རྗོད་པར་བྱེད་པ་ལེའུ་བཅུ་གསུམ་པ་དང་བཅུ་བཞི་པ་དག་བསྟན་ཏོ། །

[Block 2569]
རིམ་པ་གཉིས་ཀྱི༌[^1678]ཡན་ལག་ཏུ་ཤེས་པར་བྱའོ། །

[Block 2570]
དེ་དག་ཐམས་ཅད་ཉེ་བར་མི་དམིགས་པས་སྒྱུ་མ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་གྱིས་འགྲུབ་པར་འགྱུར་ཞེས་དེའི་སླད་དུ་ལེའུ་བཅོ་ལྔ་པ་གསུངས་སོ། །

[Block 2571]
རྫོགས་པའི་རིམ་པའི་ནང་ནས་བདག་ལ་བྱིན་གྱིས་རློབ་པའི་རིམ་པའི་ཡན་ལག་ཏུ་ཤེས་པར་བྱའོ། །

[Block 2572]
ལེའུ་བཅུ་དྲུག་པ༌[^1679]ནི་ལེའུ་བཞི་པའི་ཡན་ལག་ཡིན་ཏེ། གང་གི་ཕྱིར་བཞི་པ་ལས་ཐུགས་ཀྱི་དཀྱིལ་འཁོར་གཅིག་པུ་གསུངས་པས་སྐུ་གསུང་ཐུགས་ཀྱི་དཀྱིལ་འཁོར་གྱིས་ཡོངས་སུ་བཀང་བར་བྱ་བའི་ཕྱིར་ལེའུ་བཅུ་དྲུག་པ་ཡིན་ཏེ། ཡི་གེ་གསུམ་གྱི་རྒྱུད་ནི་སྐུ་གསུང་ཐུགས་ཀྱི་ངོ་བོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2573]
དེ་ལྟར་ལེའུ་བཅུ་དྲུག་གིས་བདག་གི་དོན་དང་གཞན་གྱི་དོན་ཕུན་སུམ་ཚོགས་པ༌[^1680]ཤེས་པར་བྱའོ། །

[Block 2574]
དེ་ཡང་དམ་ཚིག་དང་སྡོམ་པ་མ་གཏོགས་པར་འགྲུབ་པར་མི་འགྱུར་བས་ཐབས་ཕུན་སུམ་ཚོགས་པ་གཙོར་གྱུར་པ་ལེའུ་བཅུ་བདུན་པ་གསུངས་སོ། །

[Block 2575]
དང་པོའི་སྦྱོར་བའི་ཡན་ལག་ནི་རྣལ་འབྱོར་ཞེས་བྱ་བ་དང་པོ་སྟེ། དམ་ཚིག་དང༌[^1681]སྡོམ་པ་བླངས་ནས་རིམ་པ་གཉིས་སྒོམ་པ་ལ་དབང་བའི་ཕྱིར་རོ། །

[Block 2576]
དེ་ལས་ལེའུ་གཞན་མེད་དོ། །

[Block 2577]
དེ་ལྟར༌[^1682]ན་ལེའུ་བཅོ་བརྒྱད་པ་ཡང་ཡོད་པས་ཅིའི་ཕྱིར་བཅུ་བདུན་པོ་ཁོ་ནར༌[^1683]བསྟན་ཏོ་ཞེ་ན། བདེན་ཏེ་འོན་ཀྱང་བཅོ་བརྒྱད་པ་ནི་ལེའུ་བཅུ་བདུན་པོ་རྣམས་ཀྱི་བཤད་པ་དང་འདྲ་བ་ཡིན་པས་དེའི་བསྡུས་པའི་དོན་ཐ་དད་པར་མ་བསྟན་ཏེ། རྒྱུད་ཕྱི་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2578]
དེ་བས་ན་དེ་ནི༌[^1684]འདུས་པའི་ཕྱི་མ་ཞེས་གྲགས་པས་འགལ་བ་མེད་དོ། །

[Block 2579]
[^1685]

[Block 2580]
ད་ནི་ཞེས་བྱ་བ་ལ་སོགས་པས་རྒྱུད་མ་ལུས་པའི་སྒྲ་དང་དོན་གྱི་རྒྱན་གྱི་དབྱེ་བས་གང་དོན་རྣམ་པ་བཅུ་བཤད་པ་དེ་རྣམས་ཚིག་རེ་རེ་ལ་ཇི་ལྟར་གནས་ཞེས་སོ་སོར་བསྟན་པར་བྱ་བའི་ཕྱིར། ད་ནི་ཞེས་བྱ་བ་ལ་སོགས་པ་བསྟན་ཏོ། །

[Block 2581]
འདི་སྐད་བདག་གིས་ཞེས་བྱ་བ་ནས་བཞུགས་སོ་ཞེས་བྱ་བའི་བར་དུ་ནི་བཤད་པའི་ཚུལ་རྣམ་པ་བཞི་ཞེས་བྱ་བ་ལ་ཡི་གེའི་དོན་ལ་སོགས་པ་སྟེ། རིམ་པ་གཉིས་བསྟན་པར་བྱ་བའི་ཕྱིར་འདོད་པས་སོ། །

[Block 2582]
བརྗོད་ཀྱིས་མི་ལང་བའི་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ་དྲང་བ་དང་ངེས་པའི་དོན་ཞེས་བྱ་བའི་བར་དུ་ནི་སྔ་མ་བཞིན་དུ་ཀུན་རྫོབ་དང་དོན་དམ་པའི་མཚན་ཉིད་ཅན་གྱི་དོན་ཡོད་པའི་ཕྱིར་རོ། །

[Block 2583]
དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཅེས་པ་ནས། རྣམ་པ་བཞིར་བཤད་ཅེས་བྱ་བའི་བར་དུ་ནི་དཔལ་གསང་བ་འདུས་པའི་རྒྱུད་རིམ་པ་གཉིས་ཀྱི་གཙོ་བོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2584]
འདོད་ཆགས་ཆེན་པོ་ཞེས་བྱ་བ་ནས། །དྲང་བ་དང་ངེས༌[^1686]པའི་དོན་ཞེས་བྱ་བའི་བར་དུ་ནི་སྔ་མ་བཞིན་དུ་ཀུན་རྫོབ་དང་དོན་དམ་པའི་མཚན་ཉིད་ཅན་གྱི་དོན༌[^1687]ཡོད་པའི་ཕྱིར་རོ། །

[Block 2585]
སྐུ་གསུང་ཐུགས་ཞེས་བྱ་བ་ནས། རྣམ་པ་བཞིར་བཤད་ཅེས་བྱ་བའི་བར་དུ་རིམ་པ་གཉིས་བཤད་པར་འདོད་པའི་ཕྱིར་རོ། །

[Block 2586]
རིག་པ༌[^1688]ཆེན་པོའི་སྐྱེས་བུ་ཞེས་པ་ནས། དྲང་བ་དང་ངེས་པའི་དོན་ཞེས་བྱ་བའི་བར་དུ་ནི་ཕྱི་དང་ནང་གི་མཆོད་པ་གཉིས་འཐད་པའི་ཕྱིར་རོ། །

[Block 2587]
ཕྱིའི་ནི་མཆོད་པ་རྣམ་པ་ལྔའི་མཚན་ཉིད་དོ། །

[Block 2588]
ནང་གི་ནི་གཟུགས་རྡོ་རྗེ་མ་ལ་སོགས་པའི་ཡན་ལག་མཆོག་གི་མཆོད་པའོ། །

[Block 2589]
ཨེ་མའོ་ཞེས་བྱ་བ་ནས་གནས་མེད་པ་ཞེས་བྱ་བའི་བར་དུ་ནི་དགོངས་པ་མ་ཡིན་ཞེས་བྱ་བའི༌[^1689]དེ་ཁོ་ན་ཉིད་གསལ་བར་གསུངས་པའི༌[^1690]ཕྱིར་རོ། །

[Block 2590]
བཅོམ་ལྡན་འདས་ཞེས་བྱ་བ་ནས་དགོངས་པས༌[^1691]བཤད་པའི༌[^1692]ཞེས་བྱ་བའི་བར་དུ་ནི་འགལ་བའི་སྒྲའི་སྒོ་ནས་དེའི༌[^1693]ཁོ་ན་ཉིད་གསུངས་པའི་ཕྱིར་རོ། །

[Block 2591]
འགལ་བ་ལ་གཉིས་ཏེ། འཇིག་རྟེན་པ་དང་འགལ་བ་དང་། །སྒྲ་དང་འགལ་བའོ། །

[Block 2592]
འཇིག་རྟེན་དང་འགལ་བ་ནི། དཔེར་ན། །

[Block 2593 [VERSE]]
ཕ་དང་མ་ནི་བསད་བྱ་ཞིང་། །
རྒྱལ་པོ་གཙང་མ་གཉིས་དང་ནི། །
ཡུལ་འཁོར་འཁོར་བཅས་བསད་བྱས་ན།[^1694] །
མི་དེ་དག་པར་འགྱུར་ཞེས་བཤད། །

[Block 2594]
ཅེའོ། །

[Block 2595]
སྒྲ་དང་འགལ་བ་ནི་དཔེར་ན་བུམ་པའི་དོན་རྗོད་པར་བྱེད་པའི༌[^1695]སྒྲ་སྨྲ་བ་ན་སྣམ་བུའི་སྒྲ་བཞིན་ནོ། །
--- END BLOCKS ---
