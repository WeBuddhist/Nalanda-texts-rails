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
འཕགས་པའི་ཆོས་འདུལ་བ་ཞེས་བྱ་བ་ནི་ངོ་བོ་ཉིད་ཀྱིས་འདོད་ཆགས་ལ་སོགས་པ་འདུལ་བ་དང་། བསྒྲུབས་པས༌[^1793]འདུལ་བར་གནས་པའི་མཚན་ཉིད་དུ་སྟོན་ཏོ། །

[Block 2522]
འཕགས་པའི་ཆོས་འདུལ་བ་འདི་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱ་བའོ། །

[Block 2523]
འདི་ནི་ཆོས་ཐམས་ཅད་སྒོམ་པ༌[^1794]རྣམ་པར་འཇིག་པའོ་ཞེས་བྱ་བ་ནི། གཟུགས་ལ་སོགས་པའི་ཆོས་ཐམས་ཅད་སྒོམ་པ་མེད་པར་བྱེད་པའོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2524]
གཟུགས་དངོས་པོ་ཡོད་ཅེས་བྱ་བར་མི་སྒོམ་མོ་ཞེས་བྱ་བ་ནི་གཟུགས་དངོས་པོ་ཡོད་པའི་ངོ་བོ་ཉིད་དོ་སྙམ་དུ་མི་སྒོམ་པ་དེ་ནི་དངོས་པོ་ལ༌[^1795]འདི་ནི་བདག་གོ་ཞེས་བྱ་བར་མཐའ་གཉིས་ལ་ཆགས་ཏེ་ཞེས་བྱ་བ་ནི་དངོས་པོའི་འདུ་ཤེས་ཅན་ཏེ། འདི་ནི་བདག་སྟེ་གུད་ན་ཡོད་དོ་ཞེའམ། བདག་ནི་གཟུགས་སོ། །

[Block 2525]
བདག་ནི་ཚོར་བའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཆད་པ་དང་། རྟག་པའི་མཐའ་གཉིས་ལ་ཆགས་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2526]
རབ་འབྱོར་གཟུགས་སུ་འདུ་ཤེས་པ་ནི་གཉིས་སོ་ཞེས་བྱ་བ་ནི་གང་ལ་གཟུགས་སོ་ཞེས་བྱ་བའི་འདུ་ཤེས་ཡོད་པ་དེ་ལ། ཡོད་པ་དང་མེད་པའམ། དངོས་པོ་འམ། དངོས་པོ་མ་ཡིན་པར་རྣམ་པར་རྟོག་པ་གདོན་མི་ཟ་བར་འབྱུང་བར་འགྱུར་རོ། །

[Block 2527]
ཡང་ན་གཟུང་བ་དང་འཛིན་པའི་དངོས་པོར་འགྱུར་བའི་ཕྱིར་གཉིས་ཞེས་བྱའོ། །

[Block 2528]
ཇི་ཙམ་དུ་དངོས་པོ་ཡོད་པ་དེ་ཙམ་དུ་འདུ་བྱེད་དོ་ཞེས་བྱ་བ་ནི། དངོས་པོར་རྣམ་པར་རྟོག་པས། བསོད་ནམས་དང་། བསོད་ནམས་མ་ཡིན་པ་ལ་སོགས་པའི་འདུ་བྱེད༌[^1796]རྣམས་སྐྱེས་པར༌[^1797]འགྱུར་རོ། །

[Block 2529]
དངོས་པོ་ཡོངས་སུ་འདོར་རོ་ཞེས་བྱ་བ་ནི། རྣམ་པར་སྨིན་པ་ཡོངས་སུ་མི་འདོར་བའོ། །

[Block 2530]
ཆོས་ཐམས་ཅད་ལ་མངའ་བསྒྱུར་བ༌[^1798]ཞེས་བྱ་བ་ནི་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་པོ། །ཡུལ་ལ་མངའ་བརྙེས་པར་གྱུར་ཅེས་བྱ་བ་ནི་མངོན་པར་ཤེས་པ་དང་དབང་བཅུའོ། །

[Block 2531]
དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་རབ་འབྱོར་འདི་ལ་ང་སྔོན་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་པོ་དག་ལ། བྱང་ཆུབ་སེམས་དཔའི་སྤྱད་པ་སྤྱོད་པའི་ཚེ་ཞེས་བྱ་བ་ལ་སོགས་པས་དེ་སྟོན་ཏེ། ང་ཕ༌[^1799]རོལ་ཏུ་ཕྱིན་པ་རྣམས་ལ་སྤྱོད་ཅིང་མངོན་པར་ཤེས་པ་ལ་སོགས་པ་ལ་ཡང་སྙོམས་པར་འཇུག་པ་དེ་ན། མཚན་མ་ལ་རོ་མྱང་བ་མེད་པར་དམིགས་པ་ཅན་གྱི་འདུ་ཤེས་བསལ་ཏེ། རང་བཞིན་གྱིས་ཡོངས་སུ་དག་པའི་འདུ་ཤེས་བསྐྱེད་ཅིང་སྤྱད་ནས། ནམ་མཁའ་ཡིད་ལ་བྱེད་པ་ཉིད་ཀྱིས་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་ནས། ཕྱིས་རྗེས་ལ་ཐོབ་པའི་ཡེ་ཤེས་ཀྱིས་ཀྱང་། འཕགས་པའི་བདེན་པ་བཞི་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་ནས། སངས་རྒྱས་ཀྱི་ཆོས་རྣམས་མངོན་སུམ༌[^1800]དུ་བྱས་ཏེ། ཀུན་རྫོབ་ཡིད་ལ་བྱེད་པས། སེམས་ཅན་རྣམས་ཕུང་པོ་གསུམ་དུ་ལུང་བསྟན་པར་གྱུར༌[^1801]ཏེ། དེ་བས་ན་མི་དམིགས་པ་ཉིད་ཀྱིས་སྤྱོད་པ་དང་། མི་དམིགས་པ་ཉིད་ཀྱིས་བྱང་ཆུབ་པར་འགྱུར་བས། ཉེས་པ་མེད་དོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2532]
བཅོམ་ལྡན་འདས་ཇི་ལྟར་དེ་བཞིན་གཤེགས་པ་དགྲ་བཅོམ་པ་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་ཀྱིས་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་གལ་ཏེ་བསམ་གཏན་དང་། མངོན་པར་ཤེས་པ་དང་། སེམས་ཅན་རྣམས་དངོས་པོ་མེད་པའི་ངོ་བོ་ཉིད་ཡིན་ན་དེ་དག་ཇི་ལྟར་བསྐྱེད། སེམས་ཅན་རྣམས་ཀྱང་ཇི་ལྟར་ལུང་བསྟན་ཞེས་གནས་བརྟན་གྱིས་ཞུས་པའོ། །

[Block 2533]
དེས་ན་བཅོམ་ལྡན་འདས་ཀྱིས་རབ་འབྱོར་གལ་ཏེ་འདོད་པ་རྣམས་དང་། སྡིག་པ་མི་དགེ་བའི་ཆོས་རྣམས་ཞེས་བྱ་བ་ལ་སོགས་པས། དངོས་པོ་མེད་པའི་ངོ་བོ་ཉིད་ཀྱི་ཕྱིར་ཐམས་ཅད་གྲུབ་ཀྱི། གཞན་དུ་ནི་མ་ཡིན་ནོ་ཞེས་བསྟན་ཏེ། འདི་ལྟར་འདོད་པ་རྣམས་དང་། སྡིག་པ་མི་དགེ་བའི་ཆོས་རྣམས་དངོས་པོ་མེད་པའི་ངོ་བོ་ཉིད་ཡིན་ཏེ་དེའི་ཕྱིར་ལུང་བསྟན་ཏོ། །

[Block 2534]
བསམ་གཏན་རྣམས་བསྐྱེད་དོ། །

[Block 2535]
དངོས་པོའམ། དངོས་པོ་མེད་པའམ། རང་གི་དངོས་པོའམ། གཞན་གྱི་དངོས་པོ་ཞེས་བྱ་བ་ནི་ཀུན་བརྟགས་པའི་དངོས་པོའི་བདག་ཉིད་ཀྱིས་མ་ཡིན་གྱི།[^1802] རི་བོང་གི་རྭ་བཞིན་དུ་ཤིན་ཏུ་དངོས་པོ་མེད་པའི་བདག་ཉིད་ཀྱིས༌[^1803]ནི་མ་ཡིན་ལ། རང་གི་དངོས་པོའི་བདག་ཉིད་འགའ་ཞིག་ཏུ་ཡང་མ་ཡིན་གྱི། གཞན་གྱི་དངོས༌[^1804]པོའི་བདག་ཉིད་འགའ་ཞིག་ཏུ་མ་ཡིན་ནོ་ཞེས་བསྟན་པའོ། །

[Block 2536]
ཇི་ལྟར་མཐར་གྱིས་སྤྱོད་པ་དང་། མཐར་གྱིས་སློབ་པ་དང་། མཐར་གྱིས་ནན་ཏན་དུ་བགྱི་བ་མཆིས་པར་འགྱུར་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་སྒྱུ་མའི་གླང་པོ་ཆེ་ལ་སོགས་པར་དམིགས་པ་དང་། མི་དམིགས་པ་དག་འཕྲལ་ཁོ་ན་ལ་འགྱུར་བ་དེ་བཞིན་དུ། བྱང་ཆུབ་སེམས་དཔའ་ཡང་འཕྲལ་ཁོ་ན་ལ་དམིགས་སུ་མེད་པ་རྟོགས་པར་འགྱུར་གྱི་རིམ་གྱིས་ནི་མ་ཡིན་ནོ་ཞེས་དགོངས་པའོ། །

[Block 2537]
རབ་འབྱོར་འདི་ལ་བྱང་ཆུབ་སེམས་དཔས་ཐོག་མར་སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས་དང་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི། བཅོམ་ལྡན་འདས་ཀྱིས་འདི་སྐད་བསྟན་ཏེ། བྱང་ཆུབ་སེམས་དཔའ་ནི་བདག་གི་དོན་དུ་མཐར་གྱི༌[^1805]སྤྱོད་པ་མི་རྩོམ་གྱི། སེམས་ཅན་ཐམས་ཅད་ཀྱི༌[^1806]འཕྲལ་ལ་ཤེས་པར་མི་ནུས་ཏེ། རིམ་གྱིས་ཤེས་པར་བྱ་བའི་ཕྱིར་རིམ་གྱིས་རྩོམ་སྟེ། སེམས་དང་པོ་བསྐྱེད་པ་ནས་ཉེ་བར་བཟུང༌[^1807]ཞེས་བྱ་བ་ལ་སོགས་པས། དེ་དག་གི་རིམ་པ་སྟོན༌[^1808]ཏོ། །

[Block 2538]
ཞུགས་ནས་ཞེས་བྱ་བ་ནི་སེམས་སྐྱེད༌[^1809]ནས་སོ། །

[Block 2539]
ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་གི་ངོ་བོ་ཉིད་དང་། དངོས་པོ་མེད་པའི་ངོ་བོ་ཉིད་ཀྱི་ཆོས༌[^1810]ཐམས་ཅད་ལ་ཡོད་པའམ༌[^1811]མེད་པ་དམིགས་སུ་ཡོད་སྙམ་མམ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་མེད་པར་འཛིན་པར་གྱུར་ན་ཆད་པར་འགྱུར་རོ། །

[Block 2540]
དངོས་པོ་མེད་པ་དང་ངོ་བོ་ཉིད་དུ་སྨྲ་བ་རྣམས་དངོས་པོ་མེད་པར་སྨྲ་བ༌[^1812]དང་ངོ་བོ་ཉིད་ཡོད་པར་སྨྲ་བས། ཡོད་པའམ་མེད་པ་ཉིད་ཀྱི་མཐར་བྱར་མི་རུང་བས་བསྟན་པའོ། །

[Block 2541]
རབ་འབྱོར་མི་དམིགས་པ་ཉིད་ཐོབ་པའོ། །

[Block 2542]
མི་དམིགས་པ༌[^1813]ཉིད་མངོན་པར་རྟོགས་པའོ་ཞེས་བྱ་བ་ནི་མི་དམིགས་པ་ཐོབ་པ་དང་། མི་དམིགས་པའི་མངོན་པར་རྟོགས་པ་ཞེས་བརྗོད་ན་ཐོབ་པར་བྱ་བ་དང་། མངོན་པར་རྟོགས་པར་བྱ་བའི་ཕྱིར་མི་དམིགས་པ་ཡོད་པར་འགྱུར་ཏེ། དེ་ལྟ་ན་ནི་དམིགས་པ༌[^1814]ཉིད་ཐོབ་པ་དང་། མངོན་པར་རྟོགས་པ་དང་།[^1815] ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཅེས་བརྗོད་པར་བསྟན་ཏོ། །

[Block 2543]
རྣམ་པར་སྨིན་པ་ལས་བྱུང་བའི་མངོན་པར་ཤེས་པ་ཡང་ག་ལ་མཆིས་ཞེས་བྱ་བ་ནི་ས་བརྒྱད་པ་ཡན་ཆད་ལ་རྣམ་པར་སྨིན་པའི་མངོན་པར་ཤེས་པ་དང་། རྣམ་པར་སྨིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་རྣམས་ཉེ་བར་གནས་སོ། །

[Block 2544]
མཐར་གྱིས་གྲུབ་པ་བསྟན་པ་ཐམས་ཅད་ནི་གོ་སླའོ། །

[Block 2545]
བཅོམ་ལྡན་འདས་ཇི་ལྟར་ན་སེམས་གཅིག་གིས་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་ཡོངས་སུ་རྫོགས་པར་འགྱུར་བ་ལགས་ཞེས་བྱ་བ་ལ་སོགས་པ་ཞུས་པ་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པས་ཡོངས་སུ་ཟིན་པར་སྦྱིན་པ་བྱིན་ན་ཞེས་བྱ་བ་བརྗོད་པས། ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པས་ཡོངས་སུ་ཟིན་པའི་ཕྱིར་སེམས་ཅན་ཐམས་ཅད་ཀྱང་གཅིག་ཏུ་འགྱུར་རོ་ཞེས་བསྟན་པའོ། །

[Block 2546]
གཞན་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གཅིག་ཁོ་ནར་རོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2547]
དེ་ནས་ཞུས་པ་གཉིས་པ་ལ་ཡང་། སེམས་གཉིས་སུ་མེད་པའི་ཕྱིར་སེམས་གཅིག་གོ་ཞེས་སྟོན་ཏོ། །

[Block 2548]
གཉིས་ཀྱི་འདུ་ཤེས་མེད་པར་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་ལ་སོགས་པ་ཆོས་ཐམས་ཅད་སྒོམ་པ་ནི་གོ་སླའོ། །

[Block 2549]
མཚན་མ་དང་བྲལ་བའི་སེམས་ཟག་པ་མེད་པས་སྦྱིན་པ་བྱིན་ན་རྣམ་པར་སྨིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཡོངས་སུ་རྫོགས་པར་འགྱུར་ཞེས་བྱ་བ་ནི་ས་བརྒྱད་པ་ཡན་ཆད་ཉོན་མོངས་པ༌[^1816]འབྱུང་བ་མེད་པ་དང་། རྣམ་པར་སྨིན་པ་ཡིན་པའི་ཕྱིར་དེ་སྐད་ཅེས་བསྟན་ཏོ། །

[Block 2550]
སྦྱིན་པ་དེས་ཅི་ཞིག་བྱ་བ་ཞེས་བྱ་བ་ནི་བདུད་ཀྱི་རིས་རྣམས་སྨྲ་བའོ། །

[Block 2551]
དེའི་འོག་ཏུ་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་རྣམ་པར་སྨིན་པའི་མངོན་པར་ཤེས་པ་དང་བཅས་པ་རྣམས་ཡོངས་སུ་རྫོགས་པ་ནི༌[^1817]གཞུང་ཉིད་ལས་གཟུང་བར་བྱའོ། །

[Block 2552]
ཆོས་ཐམས་ཅད་ཀྱི་མཚན་ཉིད་ཤེས་པ་བསྟན་པས་རྣམ་པར་སྨིན་པ་ལས་བྱུང་བའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བསྟན་པ་ཡང་གོ་སླ་བ་ཉིད་དོ། །

[Block 2553]
དེའི་འོག་ཏུ་བཅོམ་ལྡན་འདས་ཆོས་ཐམས་ཅད་རྨི་ལམ་ལྟ་བུ་དངོས་པོ་མ་མཆིས་པའི༌[^1818]ངོ་བོ་ཉིད་ཀྱི༌[^1819]རང་གི་མཚན་ཉིད་ཀྱིས་སྟོང་པ་རྣམས་ལ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཞུས་པ་དང་། ལན་དང་ངོ་མཚར་རྨད་དུ་བྱུང་བ་བསྟན་པ་དང་། འཇིག་རྟེན་དང་འཇིག་རྟེན་ལས་འདས་པའི་ཆོས་ཀྱི་སྦྱིན་པ་དག་ཀྱང་གཞུང་ཉིད་ལས་གཟུང་བར་བྱའོ། །

[Block 2554 [HEADING]]
##### འཇིག་རྟེན་ལས་འདས་པའི་ཆོས་ཀྱི་སྦྱིན་པ་བསྟན་པའི་ལྷག་མ། ^1-2-7-55-0

[Block 2555]
དེ་ལ་འཇིག་རྟེན་ལས་འདས་པའི་ཆོས་ཀྱི་སྦྱིན་པ་བསྟན་པའི་ལྷག་མ་ནི་སྔར་བསྟན་ཟིན་ཏེ། སྔར་མ་བསྟན་པ་དག་བསྟན་ཏོ། །

[Block 2556 [HEADING]]
###### ཉོན་མོངས་པ་མེད་པ། ^1-2-7-55-1-0

[Block 2557]
དེ་ལ་ཉོན་མོངས་པ་མེད་པ་གང་ཞེ་ན་ཞེས་བྱ་བ་ནི་བདག་གི་ཕྱིར་གཞན་དག་ལ་ཉོན་མོངས་པ་སྐྱེ་བར་མ་གྱུར་ཅིག་ཅེས་བྱིན་གྱིས་བརླབས་ནས་ཏིང་ངེ་འཛིན་ལ་སྙོམས་པར་ཞུགས་ཏེ། སྔོན་གྱི་སྨོན་ལམ་གྱི་སྟོབས་ཀྱིས་གཞན་གྱི་རྒྱུད་ལ་ཉོན་མོངས་པ་སྐྱེ་བའི་སྐབས་མི་འབྱེད་པ་དེ་ནི་ཉོན་མོངས་པ་མེད་པའི་སྙོམས་པར་འཇུག་པ་ཞེས་བྱའོ། །

[Block 2558 [HEADING]]
###### སྨོན་ལམ་གྱི་ཤེས་པ། ^1-2-7-55-2-0

[Block 2559]
དེ་ལ་སྨོན་ལམ་གྱི་ཤེས་པ་གང་ཞེ་ན་ཞེས་བྱ་བ་ནི་དུས་གསུམ་དང་ཁམས་གསུམ་གྱི་ཆོས་རྣམས་ལས་ཤེས་པར་བྱ་བར་བསྡུས་པའི་ཆོས། འཇིག་རྟེན་དང་འཇིག་རྟེན་ལས་འདས་པར་གཏོགས་པ་གང་ཡང༌[^1820]རུང་བ་འགའ་ཞིག་ཤེས་པར་བྱ་བའི་ཕྱིར་སྨོན་ལམ་བཏབ་པས་ན་དེ་དེ་མ་ཐག་ཏུ་ཤེས་པ་གང་གི༌[^1821]ཤེས་པར་གྱུར་པ་དེ་སྨོན་ལམ་སྔོན་དུ་འགྲོ་བའི་ཤེས་པ་ཡིན་པས་སྨོན་ནས༌[^1822]ཤེས་པ་ཞེས་བྱའོ། །

[Block 2560 [HEADING]]
###### ཡོངས་སུ་དག་པ་བཞི། ^1-2-7-55-3-0
--- END BLOCKS ---
