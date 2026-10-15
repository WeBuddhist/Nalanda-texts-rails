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
གལ་ཏེ་འདི་ལ་སྐོར་བ༌[^1685]ཡོད་ན་ནི་དེ་ཉིད་ལའོ། །

[Block 2627]
གལ་ཏེ་མེད་ན་ནི་དེ་ཉིད་ལའོ། །

[Block 2628]
མཚན་མོ་འབྲལ་བའི་དགེ་འདུན་ལྷག་མའོ། །

[Block 2629]
གང་ལ་ཉིན་མོ་བྲལ་བའི༌[^1686]དགེ་འདུན་ལྷག་མར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་ཉིན་མོའི་ཞེས་བྱ་བ་སྨོས་ཏེ། དབྱར་ཁང་ལ༌[^1687]ཕྱི་རོལ་དུ་གྱུར་ནའོ་ཞེས་བྱ་བར་སྦྱོར༌[^1688]རོ། །

[Block 2630]
གཅིག་པུ་ཉེ་དུའི་ཁྱིམ་དུ་ཟན་གྱི་ཕྱིར་ལོ་ཉེས་བྱུང་བའི་ཕྱིར་ཉེ་དུ་རྣམས་དང་ལྷན་ཅིག་འབྲེལ་པའི་ཉེ་བར་སྤྱོད་པའི་གནང་བ་ཐོབ་ན་འགྲོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི༌[^1689]གླེང་གཞི་དག་ལས།

[Block 2631]
ཉེ་དུ་རྣམས་ཀྱི་ལུས་དང་ལྷན་ཅིག་འབྲེལ་པའི་ཉེ་བར་སྤྱོད་པ་གནང་བ་ཐོབ་ནའོ། །

[Block 2632]
དེའི་དོན་དུ་འགྲོ་བ་ན་དགེ་སློང་མའི་དགེ་འདུན་ལས་ཐོབ་པར་གྱུར༌[^1690]ན་དགེ་སློང་མ་གཅིག་པུ་གཉེན་འདུན་གྱི་ཁྱིམ་རྣམས་སུ་བཟའ་བའི་ཕྱིར་འགྲོ་བར་བྱའོ། །ཅི༌[^1691]དུས་ཐམས་ཅད་དུའམ་ཞེ་ན། མ་ཡིན་ཏེ། དེའི་ཕྱིར་ལོ་ཉེས་བྱུང་བའི་ཚེའོ། །

[Block 2633]
དེ་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ལོ་ཉེས་བྱུང་བའི་ཚེ་ཉེ་དུ་རྣམས་དང་ལྷན་ཅིག་འབྲེལ་བར་ཉེ་བར་སྤྱོད་པ་གནང་བའོ། །

[Block 2634]
ཉིན་མོ་འབྲལ་བའི་དགེ་འདུན་ལྷག་མའོ། །གང་ལ་ལམ་དུ་འཇུག་པའི་དགེ་འདུན་ལྷག་མར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་ལམ་དུ་འཇུག་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེའི་ཕྱིར་གྲོང་གི་ཉེ་འཁོར་ལས་འདས་ན་ལམ་དུ་ཞུགས་པ་ཡིན་ནོ། །

[Block 2635]
འདིར་གྲོང་མེད་པ་ཉིད་ལ་ཁྱིམ་གྱི་གནས་ནི་གྲོང་ཉིད་དོ། །

[Block 2636]
དོན་དང་བཅས་པ་ཉིད་ལ་གྲོང་ལ་སོགས་པའི་ཉེ་འཁོར་དང་བཅས་པ་ལ་ཆོས་གོས་དང་བྲལ་བའི་སྐབས་སུ་ཇི་སྐད་བསྟན་པ་རྣམས་ཐམས་ཅད་འདིར་ཡང་དེ་བཞིན་དུ་གཟུང་བར་བྱའོ། །

[Block 2637]
སྐྱེད་མོས་ཚལ་དང་ལྷའི་གནས་དང་ཚོགས་པའི་ནང་ལ་སོགས་པ་ནི་མ་གཏོགས་ཏེ། གལ་ཏེ་སྐྱེད་མོས་ཚལ་ལ་སོགས་པ་གྲོང་གི་ཉེ་འཁོར་དང་འབྲེལ་པ་ཡིན་ན། དེ་ཡང་གྲོང་ལ་སོགས་པས་བསྐོར་བ་ཉེ་འཁོར་ཉིད་ཡིན་ཏེ། ཐག་རིང་པོས་བར་དུ་ཆོད་པ་ལ་ཉེ་བར་སྤྱོད་པ་ཉིད་དོ། །

[Block 2638]
སྦོམ་དགའ་མོ་གཅིག་པུ་གྲོང་ཁྱེར་ཆེན་པོ་དྲུག་པོ་དག་ཏུ་འཕྱེན་པའི༌[^1692]གླེང་གཞི་དེ་ལས་བསླབ་པའི་གཞི་འདི་བཅས་སོ། །

[Block 2639]
ལམ་དུ་འཇུག་པའི་དགེ་འདུན་ལྷག་མའོ། །གང་ལ་ཆུ་རྒལ་བའི་དགེ་འདུན་ལྷག་མར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་ཆུ་ཀླུང་གི་ཕ་རོལ་དུ་རྒལ༌[^1693]བ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ལམ་དུ་འགྲོ་བ་ལ་ཁ་ན་མ་ཐོ་བ་འདི་ཡིན་ནོ། །

[Block 2640]
དེ་ལྟ་བས་ན་གྲུ་ཚུགས་ཙམ་ལས་འདས་ན་ཁ་ན་མ་ཐོ་བ་འདི་ཡོངས་སུ་རྫོགས་པར་འགྱུར་རོ། །

[Block 2641]
རྒྱུན་ཕྱོགས་སམ་རྒྱུན་ལས་བཟློག་ཕྱོགས་སུ་འགྲོ་ན། འདིར་ཕ་རོལ་དུ་ཞེས་བརྗོད་པ་ནི་དཔེ་ཙམ་དུ་རྟོགས་པར་བྱའོ། །

[Block 2642]
ལག་རྐྱལ་དག་གིས་ཕ་རོལ་དུ་ཕྱིན་ནའོ་ཞེས་བྱ་བ་ནི་ཆུ་ཀླུང་གི་ཕ་རོལ་དུ་རྒལ་བ་ལ༌[^1694]གྲུ་ཚུགས་ཙམ་ལས་འདའ་བར་བྱེད་ན་དགེ་འདུན་ལྷག་མའི་ལྟུང་བ་འདིའི་ཕ་རོལ་ཏུ་ཕྱིན་ན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2643]
ལག་པ་གཉིས་ཀྱིས་ལག་རྐྱལ་དག་གིས་རྒལ་བ་ནི་ཕ་རོལ་དུ་སོན་པ་ཁོ་ན་ལ་ནི་དངོས་གཞི་རྣམ་པར་གཞག་པའོ།[^1695] །མདུན་རོལ་དུ་ནི་སྦོམ་པོ་ཞེས་བྱ་བ་ནི་གཅིག་པུ་ལག་རྐྱལ་དག་གིས་ཆུ་ཀླུང་གི་ཕ་རོལ་དུ་འགྲོ་བ་ན་ཕ་རོལ་དུ་ཕྱིན་པའི་མདུན་རོལ་དུ༌[^1696]ནི་སྦོམ་པོའོ༌[^1697]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2644]
ཡུར་ཕྲན་གྱི་ཕ་རོལ་དུ་ནི་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ནི་ཕྱིན་ན་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2645]
ཡུལ༌[^1698]ཕྲན་ཞེས་བྱ་བ་ནི། གང་ཞིག་མཆོངས་པས་རྒལ་བར་ནུས་པས་ཏེ། དེ་ལ་ཡུར་ཕྲན་ཉིད་དུ་མངོན་པར་བརྟེན་པ་ཉིད་དུ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 2646]
རྒྱུན་ལྷག་མ་རྣམས་ལ་ནི་སྔ་མ་བཞིན་ཅི་རིགས་པར༌[^1699]སྦྱར་རོ། །

[Block 2647]
ཆུ་རྒལ་བའི་དགེ་འདུན་ལྷག་མའོ། །གང་ལ་རབ་ཏུ་འབྱིན་པའི་དགེ་འདུན་ལྷག་མར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་རབ་ཏུ་འབྱིན་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར༌[^1700]རབ་ཏུ་བྱུང་བ་འདི་པ་དང་སྐལ་བ་མཉམ་པ་ཉིད་དུ་བྱེད་པ་གཙོ་བོ་ཡིན་ནོ། །

[Block 2648]
དེ་བས་ན་གལ་ཏེ་དང་པོ་ཁོ་ནར་དགེ་ཚུལ་མ་ལ་སོགས་པའི་དངོས་པོར་བྱེད་ན་ཡང་ཁ་ན་མ་ཐོ་བ་ཡོངས་སུ་རྫོགས་པར་འགྱུར་རོ། །

[Block 2649]
འདིར་ཉེ་བར་སྡུད་པ་ལ་སོགས་པ་ནི་འདིར་སྦྱོར་བའི་སྦྱོར་བ་ཉིད་དེ་ཉེས་བྱས་སོ། །

[Block 2650]
ཞུ་བ་ལ་སོགས་པ་ནི་འདིར་སྦྱོར་བ་ཉིད་དེ་སྦོམ་པོ་ཞེས་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 2651]
གང་ཞིག་ཅེ་ན། དེའི་ཕྱིར་ཚོགས་པ་ཡིད༌[^1701]མཐུན་པ་བདག་པོས་ཡོངས་སུ་བཏང་བ་རྒྱལ་པོས་རྗེས་སུ་གནང་བའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བུད་མེད་དུ་འགྱུར་བའི༌[^1702]གང་ཟག་གང༌[^1703]ལ་ཚོགས་པའི་ཡིད་མཐུན་པ་ཉིད་དང་བདག་པོས་ཡོངས་སུ་བཏང་བ་ཉིད་དང་།[^1704] རྒྱལ་པོས་རྗེས་སུ་གནང་བ་ཉིད་ཀྱི་ཆོས་གསུམ་པོ་དེ༌[^1705]དག་ཡོད་པའི་བུད་མེད་དེ་ལྟ་བུ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2652]
ཡན་ལག་དེ་དག་ལས་གཅིག་ཡོད་ན་ནི་སྦོམ་པོ་ཁོ་ནར་འགྱུར་བར་རིག་པར་བྱའོ། །

[Block 2653]
དོན་གང་ལ་ཚོགས་པ༌[^1706]ཡིད་མཐུན་པ་ཉིད་ལ་སོགས་པ་དག་ཅི་ཞིག་གི་ཕྱིར་ཞེ་ན། དེའི་ཕྱིར་གསད་པའི༌[^1707]ཕྱིར་རོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 2654]
སྦྱོར་བ་གང་གིས་རབ་ཏུ་འབྱིན་ཞེ་ན། དེའི་ཕྱིར་མཁན་མོ་ཉིད་ཀྱིས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་གཞན་དེ་ལ་སྦྱོར་བ་དེ་ལ་ཉེས་བྱས་སུ་མཐོང་བ་ཡིན་ནོ། །ཅི་ལྟ་བུ་ཞིག་གིས་རབ་ཏུ་བྱུང་བ༌[^1708]ཡིན་ཞེ་ན། དེའི་ཕྱིར་དེ་ཤེས་པ་ཉིད་ཀྱིས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཚོགས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུམ་ཉིད་དུ་རྣམ་པར་གཞག་པ་ལ་དེ་ལས་འདའ་བར་བྱེད་པ་ཉིད་དུ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 2655]
གླེང་གཞི་ནི་སྡེ་བྱེད་ཀྱི་བུ་མོ་མཻ་ན་ཀ་ཞེས་བྱ་བ་སྐྱེས་པ་གཞན་རྣམས་ཀྱིས་ལོངས་སྤྱོད་པར་བྱེད་དེ། བུད་མེད་འདི་གསད་པའི༌[^1709]ཕྱིར་ཚོགས་པ་ཡིད་མཐུན་པ་དང་། བདག་པོས་ཡོངས་སུ་བཏང་བ་དང་། རྒྱལ་པོས་རྗེས་སུ་གནང་བའི་གཞི་དེ་དག་ཤེས་པ་ཉིད་ཀྱིས་སོ་ཞེས་གསུངས་པ༌[^1710]ཡིན་ནོ། །

[Block 2656]
རབ་ཏུ་འབྱིན་པའི་དགེ་འདུན་ལྷག་མའོ། །གང་ལ་ནོར་ལེན་པའི་དགེ་འདུན་ལྷག་མར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་ཤི་བའི་ནོར་ལེན་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཐོ་འཚམས༌[^1711]པའི་བློ༌[^1712]འདི་སོ་སོར་གནས་པ་ཡིན་ཏེ། འདི་ནི་བུད་མེད་རྣམས་ལ་ཚེགས་དང་བཅས་པ་དེ་བས་ན་འདི་ནི་ཁ་ན་མ་ཐོ་བར་འགྱུར་རོ། །

[Block 2657]
ཤི་བའི་ནོར་དེད་པ་ཁོ་ན་ལ་སྟེ། ཐོབ་པའི་དུས་འབའ་ཞིག་ཏུ་ནི་མ་ཟད་དོ། །

[Block 2658]
དེད་པའི་དུས་དེ་ནི་ཐོ༌[^1713]འཚམས་པ་སྟེ། དེ་བས་ན་ཤི་བའི་ཞེས་སྨོས་པ་ནི་འདིར་ནོར་གྱི་བདག་པོ་མེད་པ་གཙོ་བོ་ཡིན་ཏེ། བདག་པོ་དང་བཅས་པ་ཉིད་ལ་ལེན་པ་དེ་དང་འདྲ་བ་ཉིད་ཀྱིས་སྦོམ་པོར་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 2659]
གཞན་ལེན་དུ་བཅུག་ན་ནི་འདིར་ན་སྨད་པའོ། །

[Block 2660]
དགེ་འདུན་ལ་ཡང་རྙེད་པ་རྣམ་པ་འདི་ལྟ་བུར༌[^1714]འགྱུར་རམ་ཞེ་ན། དེ་དམིགས་ཀྱིས་བསལ་བའི༌[^1715]ཕྱིར་དགེ་འདུན་གྱི་ལ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་འདུན་གྱིས༌[^1716]ཐོབ་པ་ནི་དགེ་འདུན་གྱིས་ཏེ། ཤི་བའི་ནོར་དེ་ལེན་པ་ལ་ནི་ལྟུང་བ་མེད་དོ། །ཅི་རྣམ་པ་ཐམས་ཅད་དུའམ་ཞེ་ན། དེའི་ཕྱིར་གལ་ཏེ་ཚེགས་ཆུང་ངུས༌[^1717]ནའོ་ཞེས་སྨོས་ཏེ། དེ་དེད་ཅིང་ལེན་པ༌[^1718]ལ་ལྟུང་བ༌[^1719]མེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 2661]
འདིར་ཚེགས་ཆུང་ངུས་ཞེས་བྱ་བ་ནི་ཆོས་གོས་ཀྱི་རིན་ཆུང་བ་མ་ཡིན་པ་བཀུར་བ༌[^1720]ཞེས་བྱ་བ་ལ་སོགས་པ་ལྟ་བུ་རིགས་པ་ལས་མི་འདའ་བར་རིག་པར་བྱའོ། །

[Block 2662]
གཞན་དུ་ན་གལ་ཏེ་ཚེགས་དང་བཅས་ཤིང་རང་གི༌[^1721]དོན་དང་བཅས་པ་ཉིད་དུ་ལེན་ན་ནི་དགེ་འདུན་གྱི་ལྷག་མའོ། །

[Block 2663]
གཞན་གྱི་དོན་ཉིད་ཙམ་དུ་ཟད་ཀྱི་མངོན་པར་མི་འདོད་པ་ཉིད་ལ་རང་གི་ཆ་དང་འབྲེལ་པའི་བསམ་པ་མེད་པ་ཉིད་ལ་ནི་སྦོམ་པོར་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 2664]
ཤི་བའི་ནོར་ལེན་པའི་དགེ་འདུན་ལྷག་མའོ། །

[Block 2665]
གང་ལ་བཟོད་པ་གསོལ་དུ་འཇུག་པའི་དགེ་འདུན་གྱི་ལྷག་མར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་མཚམས་ཀྱི་ཕྱི་རོལ་དུ་བཟོད་པ་གསོལ་དུ་འཇུག་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བསྡིགས་པ་ལ་སོགས་པའི་ཆད་པའི་ལས་ལ་རྣམ་པར་གཞག་པའི་དགེ་སློང་མ་མཚམས་ཀྱི་ཕྱི་རོལ་དུ་བཟོད་པ༌[^1722]གསོལ་དུ་འཇུག་ནའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །
--- END BLOCKS ---
