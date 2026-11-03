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

[Block 2631]
གང་ཕྱིར་རིག་བྱེད་ཕྱོགས་གཅིག་ཕྱིར། །གཞན་ཡང་དེ་འདྲ་ཡིན་ཏེ་དཔེར།[^1793] །

[Block 2632 [VERSE]]
མེ་ནི་གྲང་བཟློག་གང༌[^1794]བདེན་བཞིན། །
དེ་སྐད་གཞན་དག་ཟེར་རོ་ལོ། །

[Block 2633]
གཞན་དག་ནི་སྐྱེས་བུས་མ༌[^1795]བྱས་པའི་ལུང་གི་མཚན་ཉིད་ཡོངས་སུ་བཏང་ནས་རྣམ་པ་གཞན་དུ་རིག་བྱེད་ཚད་མར་བསྒྲུབ་པར༌[^1796]འདོད་པས་གང་ལ་རྟོགས་པ་མེད་པའི་རིག་བྱེད་ཀྱི་ངག་ནི། རིག་བྱེད་ཀྱི་ཕྱོགས་གཅིག་ཉིད་ཡིན་པའི་ཕྱིར། ཕྱིན་ཅི་མ་ལོག་པ་ཡིན་ཏེ། དཔེར་ན་མེ་ནི་ཁ་བའི་གཉེན་པོ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ངག་བདེན་པ་ལྟ་བུའོ་ཞེས་སྨྲའོ། །

[Block 2634]
དེའི་འདི་ནི།

[Block 2635 [VERSE]]
རོ་འདྲ་ངོ་བོ་མཚུངས་ཉིད་ཕྱིར། །
སྣོད་གཅིག་ལ་ཡང་ཚོས་པ་བཞིན། །
ལྷག་ལྡན་འཁྲུལ་པ་ཉིད་ཡིན་ཕྱིར། །

[Block 2636]
རིགས་པ་ཤེས་པས་དེ་འདྲ་སྤངས།[^1797] །སློབ་དཔོན་བདག་ཉིད་ཀྱིས་རིགས་པ་ཅན་གྱི་ལྷག་མ་དང་ལྡན་པའི་རྗེས་སུ་དཔག་པའི་འཁྲུལ་པར་བསྟན་པ་ན། རྗེས་སུ་དཔག་པ་དེ་འདྲ་བ་བསལ་བ་ཡིན་ནོ།[^1798] །དཔེར་ན་འབྲས་བུ་རྣམས་ཀྱི་ངོ་བོ་མཚུངས་པ་ཅན་ཉིད་ཀྱིས་རོ་མཚུངས་པ་གྲུབ་པ་བཞིན་དང་། སྣོད་གཅིག་གི་ནང་དུ་ཆུད་པའི༌[^1799]ཕྱིར། མཐོང་བ་དང་འདྲ་བར་འབྲས་བུ་མ༌[^1800]མཐོང་བ་ཚོས་པ་གྲུབ་པ་བཞིན་ནོ་ཞེས་བྱ་བ་སྒྲུབ་པར་བྱེད་པ་མ་ཡིན་པར་གསུངས་སོ། །

[Block 2637]
དེ་སྒྲུབ་པར་བྱེད་པ་ཉིད་མ་ཡིན་པའི་རིགས་པ་ཡང་སྔར་བཤད་ཟིན་ཏེ།[^1801] ལུང་གི་མཚན་ཉིད་འདི་ཁོ་བོ་ཅག་གིས་དེ་ནི་དཔྱོད་པར་ནུས་པ་ཅན་གྱི་ཡུལ་ཐམས་ཅད་བདག་ཉིད་ཇི་ལྟ་བ་བཞིན་དུ་ཚད་མས༌[^1802]སྒྲུབ་པ་དང་དགག་པ་རྣམ་པར་དག་པ་ཡིན་ན་སྒྲ་རྣམས་ཀྱི་མེད་ན་མི་འབྱུང་བ་ཉིད་མེད་ན་ཡང་། དོན་རྣམས་ལ་ཐེ་ཚོམ་ཟའི༌[^1803]འཇུག་པ་རིགས་པ་ཡིན་ཏེ། དེ་ལ་འགའ་ཞིག་གི་ཚེ་མི་སླུ་བ་སྲིད་པའི་ཕྱིར་རོ་ཞེས་བཤད་དོ། །

[Block 2638]
གཞན་དུ་སྐྱེས་བུ་ཚད་མ་མཐོང་བ་དང་འགལ་བ་ཅན་གྱི་རྟོགས་པ་ནི་མེད་དོ། །

[Block 2639]
ཐ་མལ་པའི་ཡུལ་མེ་གྲང་བ་བཟློག་པར་ནུས་པ་རྗོད་པར་བྱེད་པ་བདེན་པའི་དོན་ཅན་དམིགས་ནས་བསྟན་བཅོས་ཐམས་ཅད་བདེན་པའི་དོན་ཅན་ཡུལ་ཡོངས་སུ་གཅོད་པར་ནུས་པ་ཡང་ཚད་མ་དང་འགལ་བའི་ཕྱིར། ཆེས་རིགས་པ་དང་ལྡན་པ་ཡང་མ་ཡིན་པར་སྨྲ་བ་གང་ཡིན་པ།

[Block 2640 [VERSE]]
དེས་ནི་འགལ་བ་མ་བསལ་དང་། །
བསྟན་བཅོས་དོན་ནི་མ་བསྟན་པར། །
སྐྱེས་བུ་རྟག་པ་བྱེད་པོ་དང་། །
དངོས་རྣམས་རྟག་དང་དབང་པོ་འདས། །

[Block 2641 [VERSE]]
དབང་པོས་གཟུང་བྱ་དང་དངོས་རྣམས། །
རྒྱུ་དང་དངོས་འཇིག་འགལ་བ་དང་། །
ཚད་མ་གཉིས་ཀྱི་སྤྱོད་ཡུལ་ནི། །
རྣམ་པ་བསལ་བ་གཞན་དག་གམ། །

[Block 2642 [VERSE]]
ལུང་ལ་ལྟོས་པའི་རྗེས་དཔག་དང་། །
འགལ་བ་དག་ནི་རྗོད་བྱེད་པ། །
བདེན་པའི་དོན་ཞེས་ཁས་ལེན་པ། །
གཡེམ་མ་མུ་ཅོར་གྱིས་རྒྱལ་བཞིན། །

[Block 2643]
སྐྱེས་བུའི་ངོ་བོ་སྔ་ཕྱི་འཕོ་བ་དང་ལེན་པ་མེད་པ་ཅན་འཕྲོད་པ་འདུ་བ་ཅན་གྱི་རྒྱུ་དང་། བྱིན་གྱིས་བརླབས་པའི་ངོ་བོ་ལ་སོགས་པས་ལས་དང་འབྲས་བུ་རྣམས་ཀྱི་རིམ༌[^1804]བཞིན་དུ་བྱེད་པ་པོ་དང་ཟ་བ་པོ༌[^1805]དངོས་པོ་འགའ་ཞིག་རྟག་པ་ཉིད་དེ་སྐད་ཅིག་མ་མ་ཡིན་པ་ནི་དངོས་པོའི༌[^1806]ཆོས་ལས་འདས་པ་ཉིད་ཀྱི་ཕྱིར་མི་རིགས་པ་དང་། སྤྱི་ལ་སོགས་པ་མངོན་སུམ་མ་ཡིན་པ་མངོན་སུམ་པ་དག་ཡིན་པ་དང་། དངོས་པོ་རྣམས་སྐྱེ་བ་དང་གནས་པ་དང་། འཇིག་པ་འགལ་ཏེ། ཁྱད་པར་དུ་བྱར་མེད་པ་ཅན་སྔར་བྱེད་པ༌[^1807]པོ་མ་ཡིན་པ་གཞན་ལ་ལྟོས་ནས་སྐྱེད་པ་པོ་ཉིད་དང་གྲུབ་པའི་ཕྱིར། འབྲས་བུའི་ངོ་བོ་ཅན་མ་ཡིན་པ་རྟེན་གྱི་དབང་གིས་གནས་པ་དང་། རྒྱུ་ལས་འཇིག་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་དང་། མངོན་སུམ་དང་རྗེས་སུ་དཔག་པ་དག་གིས་རབ་ཏུ་གྲགས་པ་ལས་ཕྱིན་ཅི་ལོག་པ་ཅན་སྒྲུབ་པར་བྱེད་པ་ཅན་གཞན་དང་། མེ་ལ་སྦྱིན་སྲེག༌[^1808]ལ་སོགས་པས་སྡིག་པ་སྦྱོང་བར་ནུས་པ་ཉིད་ལ་སོགས་པར་ལུང་ལ་བརྟེན་པའི་རྗེས་སུ་དཔག་པས༌[^1809]གནོད་པ་རིག་བྱེད་ཀྱིས་སྨྲས་པ་དེ་ནི་རིགས་པ་མ་ཡིན་ནོ༌[^1810]ཞེས་མང་དུ་བསྟན་ཟིན་ཏོ། །

[Block 2644]
དེ་སྐད་དུ་སྨྲ་བའི་རིག་བྱེད་དེའི་བསྟན་བཅོས་ཀྱི་ལུགས་ཐམས་ཅད་ལ་ཚད་མ་དང་འགལ་བ༌[^1811]མ་བསམས་པ་དང་། བསྟན་བཅོས་ཀྱི་འབྲེལ་པ་དང་། རྗེས་སུ་མཐུན་པའི་ཐབས་དང་། སྐྱེས་བུའི་དོན་རྗོད་པར་བྱེད་པ་མ་བསྟན་པར་རོ། །

[Block 2645]
ཤིན་ཏུ་རབ་ཏུ་གྲགས་པའི་ཡུལ་བདེན་པ་བརྗོད་པ་ཙམ་གྱིས་ཤེས་རབ་ཀྱིས་རྟོགས་པར་དཀའ་བའི་ཐིབས་པོ༌[^1812]ལ་ཉེས་པ་མེད་པ་ཉིད་བསྒྲུབ་པར༌[^1813]འདོད་པས། གཡེམ་མ༌[^1814]མུ་ཅོར་གྱིས་ཀྱང་རྒྱལ་བ་ལྟ་བུའོ། །

[Block 2646]
གཡེམ་མ་འགའ་ཞིག་གིས་ཀྱང་བདག་ཉིད་ཀྱི་བདག་པོས་ལོག་པར་ཞུགས་པའི་གནས་མཐོང་ནས་ཀླན་ཀ་ཚོལ་བ་དེ་ལ། མའི་ཆོས་བཞིན་གྱི་ཆུང་མས་ཡིད་ཆེས་པ་མེད་པར་བདག་གི་མིག་གི་ཆུའི་ཆུ་བུར་དག་གི་མིང་ཅན་གྱིས་ཡིད་ཆེས་པར་བྱེད་པའི་སྐྱེས་བུ་ཕྱིན་ཅི་ལོག་ལ་ལྟོས་ཤིང་། [^1815]གྲོང་པ་རྒན་པོ་མིག་ལོང་བ་ཤིང་སྐྱེད་པར་བྱེད་པ་དེས་དོན་དུ་གཉེར་དུ་ཟིན་ཀྱང་འབྲེལ་པ་མ་བྱས་ན། གཟུགས་དང་ཡོན་ཏན་ལ་རྗེས་སུ་ཆགས་པས་བློན་པོ་མཆོག་གི༌[^1816]ཁྱེའུ་དང་། འདོད་པ་སྤྱོད་པར་བྱེད་ཅེས་ལན་དུ་ཟེར་རོ་ལོ། །

[Block 2647]
མེ་ནི་གྲང་བའི་གཉེན་པོའི་ཚིག་གིས་ཚད་མ་དང་འགལ་བར་མཐོང་བ་ཅན། ཤིན་ཏུ་ལྐོག་ཏུ་གྱུར་པ་ལ་མི་སླུ་བར༌[^1817]རྗེས་སུ་དཔག་པ་དེ་ནི་དེ་ལྟ་བུའི་རིགས་ཅན་ཡིན་ནོ། །

[Block 2648 [VERSE]]
གལ་ཏེ་དེ་ལྟར་ཚད་གྲུབ་ན། །
ཅི་སྟེ་འདིར༌[^1818]ནི་ཚད་མིན་ཅི། །
སྐྱེས་བུ་མང་དུ་སྨྲ་བ་ལ། །
བདེན་དོན་ཅན་གཅིག་ཡོད་མེད་མིན། །

[Block 2649]
ཇི་ལྟར་འདི་ཤིན་ཏུ་བདེན་པར་བརྗོད་པ་ཤིན་ཏུ་དཀའ་བ་དེ་བཞིན་དུ་ཤིན་ཏུ་བདེན་པ་མ་ཡིན་པ་བརྗོད་པ་ཡང་ངོ་། །དེ་ལ་ཚིག་གཅིག་རྣམ་པ་འགའ་ཞིག་གིས་མི་སླུ་བས་ན་དེའི་ཚིག་གི་ཚོགས་ལྷག་མ་དེ་ལྟར་འགྱུར་ན་ནི། སྐྱེས་བུ་འགའ་ཞིག་ཀྱང་ཡིད་ཆེས་པ་མ་ཡིན་པར་མི་འགྱུར་རོ། །

[Block 2650]
གཞན་ཡང་།

[Block 2651 [VERSE]]
འཆད་པ་པོ་ལ་སྒྲ་གནས་པས། །
འདི་དངོས་རང་བཞིན་ནམ་འབྲས་མིན། །
དེ་ལས་རྣམ་པར་བཟློག་པ་ཡིས། །
[^1819]འཁྲུལ་པ་མེད་པ་ཡོད་མ་ཡིན། །

[Block 2652]
རེ་ཞིག་ཚིག་དེ་བརྗོད་པར་བྱ་བ་དག་གི་རང་བཞིན་མ་ཡིན་ཞིང་། དེ་དག་གི་འབྲས་བུ་ཡང་མ་ཡིན་ཏེ། དེ་མེད་དུ་ཟིན་ཀྱང་འཆད་པ་པོ་བརྗོད་པར་འདོད་པ་ཙམ་གྱིས་ཡོད་པའི་ཕྱིར་རོ། །

[Block 2653]
གཞན་འགའ་ཞིག་ཀྱང་འཁྲུལ་པ་མེད་པ་ཅན་མ་ཡིན་ཏེ། འཁྲུལ་པ་ཡིན་ན་ཡང་དེ་ལས་རྣམ་པ་གཞན་དུ་ཡང་དེ་སྲིད་པའི་ཕྱིར་རོ། །

[Block 2654]
དེ་ཡོད་པའི་ཕྱིར།

[Block 2655 [VERSE]]
དེ་རྟོགས་པར་རིགས་པ་མ་ཡིན་ནོ། །
གལ་ཏེ་རྗོད་བྱེད་རྣམས་ཀྱི་འཇུག །
བརྗོད་བྱ༌[^1820]མཐོང་བ་ཡིན་ཞེ་ན། །

[Block 2656]
དེ་ལྟར་ན་ནི་འགྱུར་ན། ཚིག་གི་འབྲས་བུ་ཉིད་ཡིན་ཏེ། །རྗོད་པར་བྱེད་པ་ནི་བརྗོད་བྱ་མཐོང་བས་འཇུག་པའི་ཕྱིར་རོ། །

[Block 2657]
དེ་ལྟར་ཡིན་ན་ནི།

[Block 2658 [VERSE]]
ཕན་ཚུན་དག་ནི་འགལ་བར༌[^1821]དོན། །
དེ་ནི་གཅིག་ལ་ཇི་ལྟར་འགྱུར། །

[Block 2659]
གལ་ཏེ་བརྗོད་བྱའི་དངོས་པོ་མེད་པར་སྒྲ་མི་འཇུག་གོ༌[^1822]ཞེས་བྱ་བའི་ངེས་པ་དེ་ནི་བརྗོད་པ་ཐ་དད་པ་དག་ཡོད་ན། དངོས་པོ་གཅིག་ལ་འགལ་བ་ནི་རང་བཞིན་ཉེ་བར་སྦྱོར་བས༌[^1823]འཇུག་པར་མི་འགྱུར་རོ། །

[Block 2660]
སྒྲ་གཅིག་རྣམ་གྲངས་མེད་པ་རྟག་པ༌[^1824]དང་མི་རྟག་པར་འགྱུར་རོ། །

[Block 2661]
ཞེས་བྱ་བ་འདི་ནི་སྲིད་པ་མ་ཡིན་ནོ། །

[Block 2662 [VERSE]]
དེས་ན་ལུང་གི་དངོས་པོ་རྣམས། །
རྟོགས་པ་པོ་ཡི་རྣམ་འགས་ཀྱང་། །
མེད་ན་མི་འབྱུང་གྲགས་མིན་ན། །
དེ་དག་ལས་དོན་ངེས་གང་ཡིན། །

[Block 2663]
སྐྱེ་བོ་མི་ཤེས་པ་ལུང་གི་ཚད་མ་དེས་ཀུན་ནས་བསྟན་པའི་དོན་རྟོགས་པར་བྱ་བའི་ཕྱིར། ཚོལ་བར་བྱེད་དེ། ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་རྟོགས་པར་བྱེད་པ་ནི་བསྟན་པ་ལ་ལྟོས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 2664]
དབང་པོ་ལས་འདས་པའི་ཡོན་ཏན༌[^1825]གྱི་སྐྱེས་བུ་རྣམ་པར་འབྱེད་པར་མི་ནུས་པའི་ཕྱིར། འདོད་པའི་དོན་ཡོད་པ་ཉིད་མེད་པར་ཚིག་རྣམས་ཀྱི་འཇུག་པ་མཐོང་བ༌[^1826]མི་ཤེས་པ་ནི་འཁྲུལ་པ་མ་མཐོང་བ་ཅན༌[^1827]གྱི་སྐྱེས་བུ་དག་གི་ཚིག་ལ་ཡང་ཅི་དོན་ཇི་ལྟ་བ་ཅན་ནམ། མ་ཡིན་ཞེས་ཐེ་ཚོམ་དུ་འགྱུར་རོ། །

[Block 2665]
དེས་ན་འདིས་ནི་འགའ་ཞིག་གི་ཚིག༌[^1828]གིས་ཅུང་ཟད་ཀྱང་ངེས་པར་འགྱུར་བ་རིགས་པ་མ་ཡིན་ནོ། །
--- END BLOCKS ---
