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
རང་དང་གཞན་གྱི་རྣམ་པར་རྟོག་པ་རྣམ་པ་གཉི་གའི་ཡང་འཇུག་པ་མཚུངས་པ་དེ་ལྟར་ན་རབ་ཏུ་གྲགས་པའི་རྗེས་སུ་བྱེད་པ་ཅི་ཞིག་ཡོད། གཞན་ཡང་།

[Block 2592 [VERSE]]
གྲགས་པ་ཉིད་ཀྱིས༌[^1773]སྒྲ་དོན་གྱི། །
ངེས་ལ་དོགས་པ་བསྐྱེད་པ་ནི། །
གང་ཕྱིར་དེ་ལ་སྒྲ་རྣམས་དོན། །
སྣ་ཚོགས་འཇུག་པ་ཅན་ཉིད་མཐོང་། །

[Block 2593]
སྒྲ་རྣམས་ནི་རབ་ཏུ་གྲགས་པ་ལས་དོན་གཅིག་ཏུ་ངེས་པ་མ་ཡིན་ཏེ། དེ་ཉིད་ལས་དོགས་པ༌[^1774]སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 2594]
འཇིག་རྟེན་ལ་སྒྲའི་དོན་སྣ་ཚོགས་པ་ཅན་དུ་སྣང་བ་དང་།[^1775] འཇིག་རྟེན་གྱི་བརྗོད་པ་ནི་གྲགས་པ་ཡིན་ནོ། །

[Block 2595]
དེ་ཉིད་ཀྱི་ཕྱིར་དོན་སྣ་ཚོགས་པ་ཅན་ཡིན་པའི་ཕྱིར། དེ་ལས་དོན་གྱི་ངེས་པ་རིགས་པ་མ་ཡིན་ནོ། །

[Block 2596 [VERSE]]
ངེས་བྱེད་མ་མཐོང་བ་དག་གིས། །
སྣ་ཚོགས་ནུས་ཅན་སྒྲ་རང་ཉིད། །
ངེས་པར་དོགས་པར་བྱ༌[^1776]ཡིན་ཏེ། །
རྣམ་གཞན་མི་སྲིད་མེད་ཕྱིར་རོ། །

[Block 2597]
ཞེས་བྱ་བ་ནི་བར་སྐབས་ཀྱི་ཚིགས་སུ་བཅད་པའོ། །

[Block 2598]
དེ་བས་ན་དོན་གྱི་དབྱེ་བ་རིགས་པ་མེད་པ་ཅན་གྱི་སྒྲ་དག་གི་དོན་གཅིག་ལྐོག༌[^1777]ཏུ་གྱུར་པ་དང་འབྲེལ་པ་ཅན་དམིགས་པ་མེད་པ་སྒྲོ་བཏགས་པ་ཅན་དོན་གཅིག་ངེས་པར་བྱས་ནས་རྒྱལ་དཔོག་པ༌[^1778]འཆད་པར་བྱེད་པ་ན། དེའི་ཟོལ་གྱིས་བདག་ཉིད་དེ་སྐད་དུ་སྨྲ་བའི་ཕྱིར། མུ་སྟེགས་བྱེད་གཞན་ལས་འདིའི་ཁྱད་པར་གཞན་མ་མཐོང་ངོ་། །དེ་ལྟར་ན་དོན་དེ་གསལ་བར་བྱེད་པའི་བྱ་བས་སྟོང་པ་དེར་སྒྲོ་འདོགས་པར་བརྗོད་པས་རང་གི་ཚིག་ཁྱད་པར་དུ་བྱས་པ་མེད་དོ། །

[Block 2599]
དེ་བྱེད་པ་ཅན་གྱི་འདུལ་བ་ཉིད་ལོག་པ་འབའ་ཞིག་བདག་ཉིད་གསལ་བར་བྱེད་པར་འགྱུར་རོ། །

[Block 2600]
དེ་ལྟར་ན།

[Block 2601 [VERSE]]
འགའ་ཞིག་ལམ་ནི་འདི་ཡིན་ཞེས། །
སྡོང་དུམ་འདི་ནི་སྨ་འགྱུར་ཞེས། །
གཞན་ནི་བདག་ཉིད་སྨྲ་དེ་ལྟར། །
དེ་དག་བྱེ་བྲག་བརྟག་པར༌[^1779]བྱ། །

[Block 2602]
བསམ་པ་དང་བྱ་བ་དང་ཚིག༌[^1780]མེད་པ་ཅན་གྱི་སྡོང་དུམ་ལ་སྒྲོ་བཏགས་ནས་སྟོན་པར་བྱེད་པའམ། རང་རྒྱུད་པའི་བདག་ཉིད་ཚིག་ཁས་ལེན་པ་ལ། བླུན་པོ་རྟོགས་པ་དམན་པ་ལས་གཞན་དུ་ཁྱད་པར་ཅུང་ཟད༌[^1781]ཀྱང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2603]
གཞན་ཡང་དོན་ངེས་པ་ཡོད་ན་དེ་དག་རྒྱལ་དཔོག་པས་ཤེས་པར་འགྱུར་རོ། །

[Block 2604 [VERSE]]
ཐམས་ཅད་ལ་དོན་རུང་གཅིག་གིས། །
གསལ་བྱེད་ལ་ངེས་གང་ལས་ཡིན། །

[Block 2605]
སྒྲ་ནི་དངོས་སུ་དོན་འགའ་ཞིག་གི་དེའི་རང་བཞིན་དུ་ངེས་པ་མ་ཡིན་ཏེ། ཐམས་ཅད་ལ་རུང་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2606]
རུང་བ་ཉིད་མ་ཡིན་ན་ཡང་དེ་ལས་འཕོས་པ་མེད་པའི་ཕྱིར། དབང་དུ་མ་བྱས་པ་ནི་སྐྱེས་བུ་རྣམས་ཀྱིས་ལ་ལར་ཉེ་བར་སྦྱོར་བ་དང་། གསལ་བ་མི་སྲིད་པའི་ཕྱིར་དང་།

[Block 2607 [VERSE]]
བརྗོད་འདོད་ངེས་པ་མ་གཏོགས་པ། །
གང་གིས་དབང་པོ་ལས་འདས་ཤེས། །
བརྗོད་པར་འདོད་པ་འགའ་ཞིག་གིས། །

[Block 2608]
སྐྱེས་བུས་བྱས་པའི་སྒྲ་ཡོད་ན་དེས་དེ་འགའ་ཞིག་གི་ཚེ༌[^1782]འགའ་ཞིག་ལ་ཤེས་པར་བྱེད་པར་འགྱུར་བའི་ཡང་ཕྱིར་རོ། །

[Block 2609]
བརྗོད་པར་འདོད་པ༌[^1783]སྔོན་དུ་སོང་བ་ཅན་གྱི་སྒྲ་རྣམས་ཀྱི་དོན་ངེས་པར་ཡང་རྟོགས་པར་འགྱུར་རོ། །

[Block 2610]
སྐྱེས་བུས་མ་བྱས་པ་ཡོད་ན་ཡང་དོན་ངེས་པ་ཇི་ལྟར་རྣམ་པར་ཤེས་པར་འགྱུར་ཏེ། རང་བཞིན་ཐ་དད་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 2611]
ཡོད་ན་ཡང་མངོན་སུམ་བདག་ཉིད་ཀྱིས་རྟོགས་པར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2612]
མངོན་སུམ་ཉིད་མ་ཡིན་ན་ཡང་། འགའ་ཞིག་གིས་ཀྱང་ཤེས་པར་མི་ནུས་པ་ཉིད་ཀྱི༌[^1784]ཕྱིར་རོ། །

[Block 2613]
ཁྱད་པར་ཅུང་ཞིག་ཀྱང་ཡོད་པ་མ་ཡིན་ཏེ། སྒྲ་ཐམས་ཅད་ནི་དོན་ཐམས་ཅད་དང་ཉེ་བ་དང་བསྐལ་པ་དང་བྲལ་བ་ཉིད་ཡིན་ནོ། །

[Block 2614]
དེའི་ཕྱིར་དེ་དག་ནི།

[Block 2615 [VERSE]]
ངེས་པའི་བརྗོད་འདོད་རྒྱུ་ཡིན་ཞིང་། །
བརྡ་ནི་དེ་ཡི་གསལ༌[^1785]བྱེད་ཡིན། །
དེ་ནི་སྐྱེས་མིན་ལ་མེད་ན། །
དེ་དོན་གཅིག་ཅན་དེ་གང་ལས། །

[Block 2616]
བརྗོད་པར་འདོད་པས་སྒྲ་ནི་དོན་དག་ལ་ངེས་པར་བྱ་བ་ཡིན་གྱི་ངོ་བོ་ཉིད་ཀྱིས་ནི་མ་ཡིན་ཏེ། དེ་ནི་འགའ་ཞིག་ལ་ཡང་རག་ལུས་པ་མེད་པར༌[^1786]ཐམས་ཅད་ལ་མཚུངས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2617]
གང་ལ་རག་ལས་པ་ཡིན་ན་ཡང་དེ་རྗོད་པར་བྱེད་པའི་ངེས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 2618]
སྒྲ་ཐམས་ཅད་ཀྱི་བྱེད་པ་རྣམས་བརྗོད་པར་ཐལ་བའི་ཕྱིར་རོ། །

[Block 2619]
དེ་བས་ན་བརྗོད་པར་འདོད་པ་གསལ་བར་བྱ་བའི་ཕྱིར་བསམ་པ་སྟོན་པར་བྱེད་པའི་མཚན་ཉིད་ཅན་གྱི་བརྡ་བྱས་པ་ཡིན་ནོ། །

[Block 2620]
སྐྱེས་བུས་མ་བྱས་པ་ལ༌[^1787]ནི་བརྗོད་པར་འདོད་པ་མེད་ཅིང་བརྡ༌[^1788]མེད་དེ་འགའ་ཞིག་གི་ཡང་བསམ་པ་མེད་པའི་ཕྱིར། ངེས་པ་མེད་ཅིང་དེ་ཤེས་པ་མེད་དོ། །

[Block 2621 [VERSE]]
རང་བཞིན་གྱིས་ནི་ངེས་ཡིན་ལ། །
གཞན་ལ་ངེས་ཀྱང་མི་རུང་ངོ་། །

[Block 2622]
གལ་ཏེ་བརྡ་ལ་ལྟོས་པ་མེད་པར་སྒྲ་ངོ་བོ་ཉིད་ཀྱིས་དོན་དག་ལ་འདྲེས་པར་འགྱུར་རོ་ཞེ་ན། འདིར་རག་ལུས་པ་མེད་པའི་ཕྱིར། [^1789]ངེས་པ་ཡོད་པ་མ་ཡིན་ནོ་ཞེས་བཤད་ཟིན་ཏོ། །

[Block 2623]
གཞན་ཡང་ངོ་བོ་ཉིད་ཀྱིས་བརྗོད་པར་བྱ་བ་དང་རྗོད་པར་བྱེད་པའི་ངོ་བོ་ཡིན་ན་ནི། བརྗོད་པར་འདོད་པས་ཀྱང་ཇི་ལྟར་འདོད་པ་བཞིན་དུ་ངེས་པར་སྦྱར་དུ་མི་རུང་ངོ་། །བརྡ་ཡང་དོན་མེད་ཅན་ཉིད་འགྱུར། །རང་བཞིན་ཐ་དད་པ་དབང་པོའི་རྟོགས་པར་བྱ་བ་ནི་རང་ཉིད་རྟོགས་པའི་ཕྱིར། སྤྱི་བཏང༌[^1790]བ་ལ་སོགས་པ་ལ་ལྟོས་པ་མ་ཡིན་ཏེ། སྔོན་པོ་ལ་སོགས་པའི་ཁྱད་པར་བཞིན་ནོ། །

[Block 2624]
དེ་ལ་ལྟོས་པའི་རྟོགས་པ་ཅན་དག་ནི་དངོས་པོའི་རང་བཞིན་མ་ཡིན་ནོ། །

[Block 2625]
འོ་ན་ཅི་ཡིན་ཞེ་ན། བརྡར་བྱས་པ་ཡིན་ཏེ། རྒྱལ་པོའི་རྟགས་ལ་སོགས་པ་བཞིན་ནོ། །

[Block 2626]
བརྡར་བྱས་པ་གང་ཡིན་པ་དེ་ནི་དེའི་རང་བཞིན་ཉིད་དུ་ངེས་པར་རིགས་པ་མ་ཡིན་ཏེ། དེ་ནི་འདོད་པས་འཇུག་པ་ཡིན་པའི་ཕྱིར། དེ་ཉིད་ཀྱི་ཕྱིར།

[Block 2627 [VERSE]]
བརྡ་ལས་རང་བཞིན་ཁྱད་པར་གྱི། །
གསལ་བའི་ངེས་པའང་གང་ལས་ཡིན། །

[Block 2628]
རང་གི་འདོད་པས་འཇུག་པའི་བརྡ་དེ་ནི་འདི་ཉིད་ལ་བྱ་བར་ནུས་ཀྱི། །གཞན་ལ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་གནོད་པ་ཡོད་པ་མ་ཡིན་ནོ།[^1791] །དེ་ནི་སྐྱེས་བུ་དག་གིས་རང་ཉིད་ཀྱི་འདོད་པ་བྱས་པ་ན་རང་བཞིན་དེ་ཉིད་གསལ་བར་བྱེད་ཀྱི། དེ་གཞན་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་ངེས་པ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2629 [VERSE]]
གང་ལ་འདོད་པས་རང་རྒྱུད་པས། །
དེ་ལ་ངེས་པ་ཞེས་བྱ་གང་། །
དེས་ན་བརྡ་ནི་འདི་རུང་ཉིད། །
འདོད་པ་ཉིད་ནི་གསལ༌[^1792]མི་འགྱུར། །

[Block 2630]
ཞེས་བྱ་བ་བར་སྐབས་ཀྱི་ཚིགས་སུ་བཅད་པའོ། །
--- END BLOCKS ---
