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
དེ་ཉིད་ངེས་པར་འཇུག་པ་ཞེས་བྱ་སྟེ། ཡང་དག་པ་ཉིད་དུ་ངེས་པར་ཞུགས་པའི་ཕྱིར་རོ། །

[Block 2662]
ཡང་དག་པ་ཉིད་ནི་མདོ་ལས་མྱ་ངན་ལས་འདས་པ་ཡིན་པར་བཤད་དོ། །

[Block 2663]
དེར་ངེས་པ་ནི་ངེས་པ་སྟེ་གཅིག་ཏུ་གྱུར་པའོ། །

[Block 2664]
དེར་འཇུག་པ་ནི་མངོན་པར་འགྲོ་བ་སྟེ། དེ་སྐྱེས་ན་འཕགས་པའི་གང་ཟག་ཅེས་བྱའོ། །

[Block 2665]
མ་འོངས་པས་ནི་སོ་སོའི་སྐྱེ་བོ་ཉིད་ཟློག་པར་བྱེད་དོ། །

[Block 2666]
[^1838]མ་འོངས་པ་དེའི་བྱ་བ་ནི༌[^1839]དེ་ཁོ་ན་ཡིན་པར་ཁས་ལེན་གྱི་གཞན་ནི་མ་ཡིན་ཏེ། མར་མེ་དང་སྐྱེ་བ་བཞིན་ནོ། །

[Block 2667]
གཞན་དག་ན་རེ་འཇིག་རྟེན་པའི་ཆོས་ཀྱི་མཆོག་རྣམས་ཀྱིས་བཟློག་གོ་ཞེས་ཟེར་རོ། །

[Block 2668]
མ་ཡིན་ཏེ། དེའི་ཆོས་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2669]
དེ་དང་འགལ་བ་ཡིན་པའི༌[^1840]ཕྱིར་ཉེས་པ་མེད་དེ། དགྲ་བོའི་ཕྲག་པ་ལ་ཞོན་ནས་དེ་ལ་འཚོག་པ་བཞིན་ནོ། །

[Block 2670]
གཞན་དག་ན་རེ་གཉི་གས་བཟློག༌[^1841]སྟེ། བར་ཆད་མེད་པ་དང་རྣམ་པར་གྲོལ་བའི་ལམ་དང་ཆོས་མཐུན་པའི་ཕྱིར་རོ་ཞེས་ཟེར་རོ། །

[Block 2671]
དེ་ནས་ནི་དེ་ཉིད་ལ་ཆོས་ཤེ་ན།[^1842] སྡུག་བསྔལ་ལ་ཆོས་ཤེས་པའི་བཟོད་པའི་མཇུག་ཐོགས་སུ་འདོད་པ་ན་སྤྱོད་པའི་སྡུག་བསྔལ་བ༌[^1843]དེ་ཁོ་ན་ལ་ཆོས་ཤེས་པ་སྐྱེ་སྟེ། དེ་ནི་སྡུག་བསྔལ་ལ༌[^1844]ཆོས་ཤེས་པ་ཞེས་བྱའོ། །

[Block 2672]
ཐམས་ཅད་དུ་ཡང་ཟག་པ་མེད་པའི་གནས་སྐབས་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 2673]
ཇི་ལྟར་འདོད་པ་ན་སྤྱོད་པའི་སྡུག་བསྔལ་ལ་ཆོས་ཤེས་པའི་བཟོད་པ་དང་ཆོས་ཤེས་པ་སྐྱེ་བ་དེ་བཞིན་དུ། སྡུག་བསྔལ་ལྷག་ལ་རྗེས་བཟོད་ཤེས། །སྡུག་བསྔལ་ལ་ཆོས་ཤེས་པའི་མཇུག་ཐོགས་སུ་གཟུགས་དང་གཟུགས་མེད་པ་ན་སྤྱོད་པའི་སྡུག་བསྔལ་ལ་རྗེས་སུ་ཤེས་པའི་བཟོད་པ་སྤྱི་ལ་དམིགས་པ་སྐྱེ་སྟེ། དེ་ནི་སྡུག་བསྔལ་ལ་རྗེས་སུ་ཤེས་པའི་བཟོད་པ་ཞེས་བྱའོ། །

[Block 2674]
དེ་ནས་ནི་རྗེས་སུ་ཤེས་པ་སྐྱེ་སྟེ། དེ་ནི་སྡུག་བསྔལ་ལ་རྗེས་སུ་ཤེས་པ་ཞེས་བྱའོ། །

[Block 2675]
དང་པོ་ཉིད་དུ་ཆོས་ཀྱི་དེ་ཁོ་ན་ཉིད་ཤེས་པའི་ཕྱིར་ཆོས་ཤེས་པ་ཡིན་ནོ། །

[Block 2676]
དེའི་རྒྱུ་ལས་བྱུང་བའི་ཕྱིར་གོང་མའི་སྡུག་བསྔལ་ལ་སོགས་པ་ལ་དམིགས་པ་ནི་རྗེས་སུ་ཤེས་པ་སྟེ། དེ་བཞིན་དུ་རྟོགས་པའི༌[^1845]ཕྱིར་རོ། །

[Block 2677]
[^1846]ཇི་ལྟར་སྡུག་བསྔལ་གྱི་བདེན་པ་ལ་བཟོད་པ་དང་ཤེས་པ་བཞི་པོ་དེ་དག་སྐྱེ་བ་ལྟར། བདེན་པ་གསུམ་ལ་དེ་བཞིན་ནོ། །

[Block 2678]
སྡུག་བསྔལ་ལ༌[^1847]རྗེས་སུ་ཤེས་པའི་མཇུག་ཐོགས་སུ་འདོད་པ་ནི༌[^1848]སྤྱོད་པའི་ཀུན་འབྱུང་ལ་ཆོས་ཤེས་པའི་བཟོད་པ་སྐྱེ་ཞིང་། དེ་ནས་ཀུན་འབྱུང་ལ་ཆོས་ཤེས་པ་སྐྱེ་ལ། དེ་བཞིན་དུ་མཇུག་ཐོགས་སུ་སྐྱེ་བའི་རིམ་གྱིས་ཀུན་འབྱུང་ལྷག་མ་ལ་རྗེས་སུ་ཤེས་པའི་བཟོད་པ་དང་། ཀུན་འབྱུང་ལ་རྗེས་སུ་ཤེས་པ་སྐྱེའོ། །

[Block 2679]
འདོད་པ་ན་སྤྱོད་པའི་སྡུག་བསྔལ་འགོག་པ་ལ་ཆོས་ཤེས་པའི་བཟོད་པ་དང་། འགོག་པ་ལ་ཆོས་ཤེས་པ་སྐྱེའོ། །

[Block 2680]
འགོག་པ་ལྷག་མ་རྣམས༌[^1849]ལ་རྗེས་སུ་ཤེས་པའི་བཟོད་པ་དང་། འགོག་པ་ལ་རྗེས་སུ་ཤེས་པ་སྐྱེའོ། །

[Block 2681]
འདོད་པ་ན་སྤྱོད་པའི་སྡུག་བསྔལ་གྱི་གཉེན་པོ་ལམ་ལ་ཆོས་ཤེས་པའི་བཟོད་པ་དང་། ལམ་ལ་ཆོས་ཤེས་པ་སྐྱེའོ། །

[Block 2682]
ལམ་ལྷག་མ་རྣམས༌[^1850]ལ་རྗེས་སུ་ཤེས་པའི་བཟོད་པ་དང་། ལམ་ལ་རྗེས་སུ་ཤེས་པ་སྐྱེ་སྟེ། དེ་ལྟར་བདེན་པ་མངོན་རྟོགས་འདི། །སེམས་བཅུ་དྲུག་གོ། །

[Block 2683]
དེ་ལྟར་ན་རིམ་པ་འདིས་ན་བདེན་པ་མངོན་པར་རྟོགས་པ་འདི་ནི་སེམས་བཅུ་དྲུག་ཡིན་ནོ། །

[Block 2684 [HEADING]]
###### མངོན་པར་རྟོགས་པ་རྣམ་གསུམ། ^3-1-3-8-2-0

[Block 2685]
སྡེ་བ་གཞན་གང་དག་བདེན་པ་རྣམས་མངོན་པར་རྟོགས་པ་འདི་ནི་གཅིག་གོ་ཞེས་བརྗོད་པ་དེ་དག་གི་བསམ་པ་ལྟར༌[^1851]བྱ་སྟེ། བྱེ་བྲག་མེད་པར་ནི་མངོན་པར་རྟོགས་པ༌[^1852]ཞེས་བྱའོ། །

[Block 2686]
དེ་ནི་རྣམ་གསུམ་སྟེ། མཐོང་དམིགས་བྱ་བ་ཞེས་བྱའོ། །

[Block 2687 [HEADING]]
###### **མཐོང་བའི་མངོན་པར་རྟོགས་པ།** ^3-1-3-8-2-1-0

[Block 2688]
མཐོང་བའི་མངོན་པར་རྟོགས་པ་ནི་ཟག་པ་མེད་པའི་ཤེས་རབ་ཀྱི་བདེན་པ་རྣམས་མངོན་པར་རྟོགས་པའོ། །

[Block 2689 [HEADING]]
###### **དམིགས་པའི་མངོན་པར་རྟོགས་པ།** ^3-1-3-8-2-2-0

[Block 2690]
དམིགས་པའི་མངོན་པར་རྟོགས་པ་ནི་དེ་དང་མཚུངས་པར་ལྡན་པ་རྣམས་ཀྱིས་ཀྱང་མངོན་པར་རྟོགས་པའོ། །

[Block 2691 [HEADING]]
###### **བྱ་བའི་མངོན་པར་རྟོགས་པ།** ^3-1-3-8-2-3-0

[Block 2692]
བྱ་བའི་མངོན་པར་རྟོགས་པ་ནི་ལྡན་པ་མ་ཡིན་པ་ཚུལ་ཁྲིམས་དང་སྐྱེ་བ་ལ་སོགས་པས་ཀྱང་མངོན་པར་རྟོགས་པའོ། །

[Block 2693]
སྡུག་བསྔལ་མཐོང་ན་དེའི་མངོན་པར་རྟོགས་པ་ནི་གསུམ་མོ། །

[Block 2694]
ཀུན་འབྱུང་ལ་སོགས་པ༌[^1853]ནི་བྱ་བའི་མངོན་པར་རྟོགས་པ་ཡིན་ཏེ། སྤོང་བ་དང་མངོན་གསུམ༌[^1854]དུ་བྱེད་པ་དང་སྒོམ་པའི་ཕྱིར་རོ། །

[Block 2695]
དེ་ལྟ་བས་ན༌[^1855]གལ་ཏེ་བདེན་པ་རྣམས་མཐོང་བའི་མངོན་པར་རྟོགས་པའི་མངོན༌[^1856]པར་རྟོགས་པ་གཅིག་གོ་ཞེས་སྨྲ་ན་ནི་རྣམ་པ་ཐ་དད་པའི་ཕྱིར་མི་རིགས་པར་སྨྲ་བ༌[^1857]ཡིན་ནོ། །

[Block 2696]
འོན་ཏེ་ཐམས་ཅད་བདག་མེད་པའི་རྣམ་པར་མཐོང་ངོ་ཞེས་ཟེར་ན་ནི། འོ་ན་ནི་བདེན་པ་རྣམས་ལ་སྡུག་བསྔལ་ལ་སོགས་པར་མཐོང་བར་མི་འགྱུར་བས་དེ་ལྟ་བས༌[^1858]ན། འཕགས་པ་ཉན་ཐོས་སྡུག་བསྔལ་ལ་སྡུག་བསྔལ་དུ་ཡིད་ལ་བྱེད་པའམ། ཀུན་འབྱུང་ལ་ཀུན་འབྱུང་དུ་ཡིད་ལ་བྱེད་པའམ། ལམ་ལ་ལམ་གྱི་བར་དུ་ཡིད་ལ་བྱེད་པའི༌[^1859]ཟག་པ་མེད་པའི་ཡིད་ལ་བྱེད་པ་དང་མཚུངས་པར་ལྡན་པའི་ཆོས་རྣམས་རྣམ་པར་འབྱེད་པ་གང་ཡིན་པ་ཞེས་གསུངས་པའི་མདོ་དང་འགལ་ལོ། །

[Block 2697]
གལ་ཏེ་དེ་ལྟ་བུ་ནི་བསྒོམ་པའི་ལམ་མ༌[^1860]ཡིན་ནོ་ཞེ་ན། མ་ཡིན་ཏེ། ཇི་ལྟར་མཐོང་བ་བཞིན་བསྒོམ་པའི་ཕྱིར་རོ། །

[Block 2698]
འོན་ཏེ་གཅིག་མཐོང་བས་ལྷག་མ་རྣམས་ལྔ༌[^1861]དབང་ཐོབ་པའི་ཕྱིར་མངོན་པར་རྟོགས་པ་གཅིག་ཁོ་ན༌[^1862]ཞེས་ཟེར་ན་ནི་ཉེས་པ་མེད་དེ་བར་སྐབས་སུ་ལྡན་པ༌[^1863]ཡོད་དམ་མེད་ཅེས་དཔྱད་པར་བྱ་བ་ཡིན་ནོ། །

[Block 2699]
འོན་ཏེ་སྡུག་བསྔལ་ཁོ་ན་ཡོངས་སུ་ཤེས་ན་ཀུན་འབྱུང་ཡང་སྤོངས༌[^1864]ལ་འགོག་པ་ཡང་མངོན་སུམ་དུ་བྱེད་ཅིང་ལམ་ཡང་སྒོམ་པར་བྱེད་པས་དེའི་ཕྱིར་མངོན་པར་རྟོགས་པ་གཅིག་གོ་ཞེས་ཟེར་ན་དེ་ལྟ་ན་ཡང་ཉེས་པ་མེད་དེ། གཅིག་མཐོང་ན་ལྷག་མ་རྣམས་ཀྱང༌[^1865]བྱ་བའི་མངོན་པར་རྟོགས་པ་ཡིན་ནོ་ཞེས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 2700]
མདོ་ལས་མཐོང་བའི་མངོན་པར་རྟོགས་པའི་ཕྱིར་བདེན་པ་རྣམས་རིམ་གྱིས༌[^1866]མངོན་པར་རྟོགས་པར་གསུངས་པར་མངོན་ཏེ། ཁྱིམ་བདག་བདེན་པ་རྣམས༌[^1867]མངོན་པར་རྟོགས་པ་གཅིག་པ་ནི་མེད་པ་ཉིད་དེ། འོན་ཀྱང་མཐར་གྱིས་མངོན་པར་རྟོགས་སོ་ཞེས་རྒྱས་པར་གསུངས་པ་དཔེ་དང་བཅས་པའི་མདོ་གསུམ་ཁུངས་སུ་ཡོད་དོ། །
--- END BLOCKS ---
