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

[Block 2666]
དགའ་བ་ནི་དད་པ་འམ་དང་བའོ། །

[Block 2667]
བྱམས་ཤིང༌[^1694]དགའ་བ་གཉིས་སུ་གྱུར་པ་ནི་དེ་གཉིས་ཀྱིས་ཡིན་ཏེ། བྱམས་པར་གྱུར་པ་ནི་ཞི་བས་སོ། །

[Block 2668]
ཆོས་བཟང་བར་གྱུར་པ༌[^1695]ནི་བླ་མ་དགའ་བར་གྱུར་པའོ། །

[Block 2669]
དབང་དུ་བྱེད་པ་ནི་སྔགས་ཀྱི་དོན་གྱིས་སོ། །

[Block 2670]
ཡོན་ཏན་དབང་དུ་བྱེད་པའི་སྔགས་རྟག་ཏུ་ཞེས་བྱ་བ་ལ། སྔགས་ཡོན་ཏན་དབང་དུ་བྱེད་པ་ལས་གཞན་དག་ལས་ཡོན་ཏན་གྱི་མཚན་ཉིད་ཀྱིས་དབང་དུ་བྱེད་པའི་སྔགས་འདི་ནི་ཁྱད་པར་དུ་བསྟན་པ་ཡིན་ཏེ། ཡོན་ཏན་ནི་རྟག་ཏུ་ཡོད་པ་ཡིན་པས་སྔགས་གཞན་ལྟར་མི་རྟག་ཅིང་ཉམས་པ་ནི་མ་ཡིན་ཏེ། ཡོན་ཏན་དབང་དུ་བྱེད་པའི་སྔགས་འདི་ལས་གཞན་པའི་དབང་དུ་བྱེད་པའི་སྔགས་ནི། ཞེ་སྡང་གིས་འཁྲུགས་པ་སྟེ། དབང་དུ་བྱེད་པའི་ནུས་པ་མེད་དོ། །

[Block 2671]
སྔགས་འདིས་ནི་དེ་ལྟ་བུའང་དབང་དུ་བྱེད་པ་ཡིན་ནོ། །

[Block 2672]
སྔགས་ཐ་མལ་པས་ནི༌[^1696]བདག་ཉིད་ཀྱི་སེམས་དབང་དུ་བྱེད་པ་ཡིན་ནོ། །

[Block 2673]
གཞན་དག་ནི་མ་ཡིན་ནོ། །

[Block 2674]
གསང་དུས་དག་ཏུ་ཞེས་བྱ་བ་ནི་མི་འདོད་པའི་དུས་རྟག༌[^1697]ཏུའོ། །

[Block 2675]
དབུལ་བ་འབྲས་བུ་རེ་བ་མེད། །ཅེས་བྱ་བའི་ཚིགས་བཅད་ཀྱི་དོན་ནི་འདི་ཡིན་ཏེ། བདག་དང་གཞན་གྱི་ཕན་པ་དང་། འཇིག་རྟེན་འདི་དང༌[^1698]ཕ་རོལ་ཏུ་ཕན་པ་མེད་པ་སྟེ། བདག་གིས༌[^1699]མི་ལའང་སྨྲར་མེད་ཅིང་། །ཅེས་བྱ་བ་འདིས་ནི་གཞན་ལ་ཕན་པ་མི་ནུས་པ་ཉིད་དོ། །

[Block 2676]
དགའ་སྟོན་ཚེ་ན་འད་དགའ་མི་མྱོང་། །ཞེས་བྱ་བ་འདིས་ནི་བདག་གི་དོན་མི་ནུས་པ་ཉིད་དོ། །

[Block 2677]
ཀྱི་ཧུད་སྦྱིན་པའི་གཏམ་ཡང་གཞན། །ཞེས་བྱ་བ་འདིས་ནི་འཇིག་རྟེན་ཕ་རོལ་གྱི་ཕན་པ་མི་ནུས་པ་ཉིད་དེ། གང་གི་ཕྱིར་སྦྱིན་པ་ཡོད་ན་ནི་འཇིག་རྟེན་ཕ་རོལ་ཏུ་མངོན་པར་མཐོ་བ་ཐོབ་པར་འགྱུར་རོ། །

[Block 2678]
དབུལ་བ་འབྲས་བུ་རེ་བ་མེད། །ཅེས་བྱ་བ་འདིས་ནི་འཇིག་རྟེན་འདི་ལ་ཕན་པའི་བྱ་བ་མི་ནུས་པ་ཉིད་དོ། །

[Block 2679]
རེ་བ་ནི་མངོན་པར་འདོད་པ་སྟེ། འདི་དང་འདི་བྱའོ་ཞེས་བྱ་བ་དེ་དང་དེའི་འབྲས་བུ་མེད་པ་ཡིན་ཏེ། འབྱོར་པ་མ་ཡིན་པར་ནི་བསམ་པ་འབྲས་བུ་དང་བཅས་པར་མི་འགྱུར་རོ། །

[Block 2680]
སྨ་འབབ་གནས་གྱུར་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཀྱི་དོན་ནི་འདི་ཡིན་ཏེ། བདག་དང་གཞན་གྱི་སྒྲུབ་པའི་རྒྱུ་མེད་པ་དང་། བདག་ཉིད་ཀྱི་སྡུག་བསྔལ་གྱི་རྒྱུ་དང་། བདེ་བ་མི་ཐོབ་པའི་རྒྱུ་དང་། གཞན་ལ་ཡང་དག་པར་སྒྲུབ་པ་མི་འཐོབ་པའི༌[^1700]རྒྱུ་དང་བཞི་པོ་འདི་དག༌[^1701]གོ་རིམས་བཞིན་དུ༌[^1702]སྦྱར་བར་བྱའོ། །

[Block 2681]
ཉམས་ཉེས༌[^1703]བཞིན་དུ་རྟག་ཏུ་མྱ་ངན་བྱེད། །ཅེས་བྱ་བ་ནི་བཞི་པོ་དེ་དག་གི་རྒྱུས་སོ། །

[Block 2682]
བཀྲེས་སྐོམ་ཟན་དང་ཞེས་བྱ་བ་འདིའི་ལུས་ནི་རྣམ་པ་གསུམ་སྟེ། སྡུག་བསྔལ་རྣམ་པ་གསུམ་གྱི༌[^1704]གསོ་བར་བསྟན་པ་ཡིན་ཏེ། བཀྲེས་པ་ལ་ནི་ཟན་ནོ། །

[Block 2683]
སྐོམ་པ་ལ་ནི་ཆུའོ། །

[Block 2684]
འདི་གཉིས་ནི་ལྷན་ཅིག་སྐྱེས་པའི་སྡུག་བསྔལ་གྱི་གསོ་བར་བསྟན་ཏོ། །

[Block 2685]
སྨན་བཅས་སྔགས་ཀྱིས་ནད་སོས་འགྱུར། །ཞེས་བྱ་བ་འདིས་ནི་གློ་བུར་གྱི་སྡུག་བསྔལ་གསོ་བར་བསྟན་ཏོ། །

[Block 2686]
རྒྱུན་གནས་ནོར་གྱིས༌[^1705]དབུལ་པོར་འགྱུར། །ཞེས་བྱ་བ་འདིས་ནི་སྔོན་བྱས་པའི་རྒྱུའི་དབུལ་བའི་སྡུག་བསྔལ་ལས་གསོ་བར་བསྟན་ཏེ། གང་གི་ཕྱིར་དབུལ་པོ་ནི་སྐྱེ་བ་སྔ་མ་ལ་རང་གི་སེར་སྣ་བྱས་པའི་རྒྱུ༌[^1706]ཡིན་ཏེ། ད༌[^1707]གསོ་བ་ནི་ནོར་རོ། །

[Block 2687]
བླང་བའི་ཐབས་རབ་ཏུ་ཆུང་བ་གང་ཡིན་པ་དེ་ནི་བླང་བའི་ཐབས་རབ་ཏུ་ཆུང་བའོ། །

[Block 2688]
བྲམ་ཟེ་རྒུད་ཚེ་རྐུ་བ་ཆོས་སུ་བཤད། །ཅེས་བྱ་བའི་ཚིགས་སུ་བཅད་པ་འདིས་ནི་བྲམ་ཟེ་རྒུད་པར་གྱུར་པའི་ཚེ་ན་ནི་བྲམ་ཟེ་རྒུད་པ་ཉིད་ལ་ཉེས་པ་མེད་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 2689]
གལ་ཏེ་བྲམ་ཟེ་རྣམས་ཀྱི་རང་ཉིད་ཀྱི་ནོར་ཡིན་ན་ཅིའི་ཕྱིར་མ་མཐོང་བར་བླང་ཞེ་ན། དེའི་ལན་བསྟན་པའི་ཕྱིར། ངོ་མཐོན་དུ་ནི་ནོར་འཕྲོག༌[^1708]ནུས་གྱུར་ཀྱང་། །ཞེས་བྱ་བའི་ཚིགས་བཅད་བརྩམས་བ་ཡིན་ནོ། །

[Block 2690]
ཡང་ན་འདིའི་བསྡུས་པའི་དོན་ནི་མངོན་སུམ་དུ་ཡང་བླང་བར་བྱ་བ་ཡིན་ན། ཅིའི་ཕྱིར་མ་མཐོང་བར་བླང་ཞེ་ན། རྐུ་བ་ལ་ཉེས་པ༌[^1709]ཡིན་ཏེ། དེས་ན། ངོ་མཐོན༌[^1710]དུ་ནི་ནོར་འཕྲོག་ནུས་གྱུར་ཀྱང་། །ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་བརྩམས་པ་ཡིན་ནོ། །

[Block 2691]
རྗེས་སུ་ཡི་རང་བ་ཡང་མི་བྱེད་དེ། རང་བཞིན་གྱི་དགེ་བ་ཡིན་པས་སོ། །

[Block 2692]
ཆོ་ག་བསྟན་པ་ནི་རྐུ་བའོ། །

[Block 2693]
དགའ་བར་མ་གྱུར་ཞེས་བྱ་བ་ནི་རབ་ཏུ་མི་སྒྲུབ་པ་དང་། བདག་གིར་མི་བྱེད་པའོ། །

[Block 2694]
སླར་བཟློག་པར༌[^1711]མ་གྱུར་པ་ནི་སླར་མི་སྨྲ་བའོ། །

[Block 2695]
ཡོན་ཏན་ཞིག་ཡོད་པར་བསམས་ནས་ཞེས་བྱ་བ་ནི་སྲིད་པ་གང་ཡིན་པ་དེ་ནི་ཡོན་ཏན་ཞིག་ཡོད་པར་བསམས་པའོ། །

[Block 2696]
རྩོལ་མི་ཕོད་དམ་ཞེས་བྱ་བ་ནི་བདག་ཉིད་ཀྱི་རྩོལ་བ་དང་བྲལ་བ་སྟེ། སྙིང་སྟོབས་མེད་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2697]
ང་རྒུད་པ་ཞེས་བྱ་བ་དེ་ལ་མི་བཟོད་པར་གྱུར་པ་དེ་ནི་ང་རྒུད་མི་བཟོད་པས་སོ། །

[Block 2698]
མི་རྣམས་དཔའ་བོའི་ལམ་ཞེས་བྱ་བ་ནི་དཔའ་བོའི་འདྲོན་པོའོ།[^1712] །སྤྲོ་བ་དང་བྲལ་བ་ནི་སྤྲོ་བ་མེད་ཅིང་ལེ་ལོ་སྟེ་དེས་བླུན་པའོ། །

[Block 2699]
ཡང་ན་འདི་ལ་སྤྲོ་བ་མེད་པའོ། །

[Block 2700]
སྤྲོ་བ་མེད་པ་གང་ཡིན་པ་དེ་ནི་བླུན་པ་ཡིན་པས་སྤྲོ་བ་མེད་ཅིང་བླུན་པའོ། །
--- END BLOCKS ---
