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
དོན་ཇི་ལྟ་བ་ཉིད་མ་ཡིན་པ་ལ་ཉེ་བའི་དངོས་གཞིའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2662]
དེ་ལྟར་ལྟུང་བ་རྟོགས་པར་བྱའོ། །

[Block 2663]
དྲི་བར་བྱས་པ་ལ་མ་སྨྲས་པར་ནད་པ་ལ་སྨན་སྦྱིན་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་གསོ་བ་ལ་མཁས་པས་ཚངས་པ་མཚུངས་པར་སྤྱོད་པའི་ནད་གཡོག་བྱའོ་ཞེས་གསུངས་པའི་ཚིག་གིས་གསོ་བར་བྱ་བ་ལ་མཁས་པ་མ་ཡིན་པ་དེའི་ཕྱིར་འདི་བཏགས་པའོ། །

[Block 2664]
འདིར་སུ་ཞིག་ལ་མངོན་པར་དྲི་བར་འདོད་ན་གང་གིས་མ་སྨོས་པའི་སྨན་སྦྱིན་པར་མི་བྱ་ཞེ་ན། དེའི་ཕྱིར་སྨན་པ་དང་དེ་རབ་ཏུ་བྱུང་བ་དང་། བཀོལ་བ་རྣམས་ལ་དྲི་བར་བྱ་བ༌[^1797]ཉིད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་རབ་ཏུ་བྱུང་བ་ཞེས་བྱ་བ་ནི་སྨན་པ་རབ་ཏུ་བྱུང་བའོ། །

[Block 2665]
འདིར་བཀོལ་བ་ལ་ཡང་ངོ༌[^1798]ཞེས་བྱ་བའི་སྒྲ་བཀོལ་བ་ཞེས་བྱ་བ་ཡང་སྦྱར་རོ། །

[Block 2666]
དེས་བཀོལ་བ་ཞེས་བྱ་བའི༌[^1799]སྨན་པས་བཀོལ་བའོ། །

[Block 2667]
ནད་ཀྱིས་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་བཀོལ་བ་ཞེས་བྱ་བར་སྦྱར་ཏེ། ནད་ཀྱིས་བཀོལ་པར་གྱུར་པ་རྣམས་ལ་ཡང་དྲི་བར་བྱ་བའི་དོན་ཏོ། །

[Block 2668]
དགེ་སློང་རྒན་རབས་རྒན་རབས་ཤེས་རབ་ཅན་རྣམས་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་དྲི་བར་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2669]
སྔ་མ་ཉིད༌[^1800]མེད་ན་ཕྱི་མ་ལའོ་ཞེས་བྱ་བ་ནི་དྲི་བར་བྱ་བ་འདི་རྣམས་ལ་གང་ཞིག་འདི་ལ་སྔ་རོལ་དུ་མེད་པ་ལ་འདིར་གཞན་ལ་དྲི་བར་བྱ་བ་ཉིད་དོ། །

[Block 2670]
འདི་རྣམས་ཀྱི་སྔ་མ་ནི་ཤིན་ཏུ་མཁས་པ་ཡིན་ཏེ། དྲི་བ་འདི་ནི་རྫས་ཀྱི་དོན་དུ་སྟེ། མེད་པ་ལ་ནི་ཕྱི་མ་ལ་དྲི་བའོ། །

[Block 2671]
ཕུན་སུམ་ཚོགས་པ་ལས་དྲི་བར་རིགས་ཏེ། སྨན་པ་མེད་ན་དེ་རབ་ཏུ་བྱུང་བ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 2672]
ཕན་པར་འདོད་པ་ཉིད་ཀྱིས་འཆི་བའི་ཕྱིར་སྨན་མ་ཡིན་པ་སྦྱིན་པ་ལ་ནི་ན་སྨད་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་རང་གིས་བསྒོ་བ༌[^1801]མ་བྱས་པར་ཅི་ཞིག་སྙམ་དུ་འདི་ལྟར་ཕན་པར་འདོད་པས་འཆི་བའི་དོན་དུ་སྨན་མ་ཡིན་པ་སྦྱིན་པ༌[^1802]ལ་ན་སྨད་པ་མེད་དོ། །

[Block 2673]
ཕན་པར་འདོད་པ་ཉིད་ཀྱིས༌[^1803]སྦྱིན་པ་འདི་དེའི་ཕྱིར་སྐྱོན་མེད་པ་ཉིད་དང་། ན་སྨད་པ་ལ་ཡང་འདིར་གང་ཞིག་གིས་འདོད་པ་དེ་བཟློག་པའི་དོན་དུ་ཡོངས་སུ་རྫོགས་པ་ཉིད་འདིར་ཁ་ན་མ་ཐོ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2674]
ཆོམ་རྐུན་པ་རྣམས་ཀྱི་ལག་པ་ལ་སོགས་པ་བཅད་དེ་ཚོར་བས་གནོད་པར་འགྱུར་བ་རྣམས་ལ་འཆི་བར་བྱ་བའི༌[^1804]ཕྱིར་གང་ཞིག་དགེ་སློང་མས་འགྱུར་བྱེད་ཀྱི་ལན་ཚྭ་བྱིན་པ་ལས་མདོ་འདི་བྱས་སོ། །

[Block 2675]
ཁུར་འདེགས་པར་མི་ནུས་པ་ལ་གྲོགས་ཉིད་མི་བྱའོ། །

[Block 2676]
གལ་ཏེ་དེ་ལྟ་བུའི་རྐྱེན་གྱིས་མ་བྱིན་མ་དག་རུབ་པ་ཉིད་ལ་ཅིག་ཅར་འདེགས་པར་སྐད་སྦྱར་ཏེ་བྱའོ་ཞེས་བྱ་བ་ནི་བྱའོ་ཞེས་བྱ་བ་བྱེད་པའི་ཚིག་དང་པོར་སྨོས་པ་ན་འདིར་ཡང་ཅི་དགར་བསྟན་པ་ཡིན་ནོ། །

[Block 2677]
ཁུར་འདེགས་པར་མི་ནུས་པ་ཉིད་ལ་བར་བར་དུ་དེ་ལ་བརྩན་པའི་དོན་དུ་ནུས་པའི་ཁྱིམ་དུ་གནས་པ་རྣམས་ཀྱིས་རུབ་པ་ཉིད་ཤེས་པར་བྱའོ། །

[Block 2678]
གནས་པ་ཙམ་གྱིས༌[^1805]ཉེ་བར་གནས་པ་རྣམས་ནི་མ་ཡིན་ནོ། །

[Block 2679]
དེ་འདེགས་པའི་དུས་ནི་ཅིག་ཅར་འདེགས་པར་སྐད་སྦྱར་ཏེ་ཞེས་བྱ་བ་ནི་ཁྱིམ་པ་རྣམས་ལ་བསྒོ་བར་བྱ་ཞིང་སྐད་སྦྱར་ནས་གདེག༌[^1806]པར་བྱའི། ཅིག་ཅར་དུ་མི་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2680]
གཞག་པ་ལ་ཡང་ཅིག་ཅར་ཉིད་དུ་སྐད་སྦྱར་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ཁུར་མི་བཟོད་པ་དེ་ལ་གདེག་པའི་དུས་དང་གཞག་པ་ལ་ཡང་ཅིག་ཅར་ཉིད་དུ་སྐད་སྦྱར་ཏེ་བྱའོ། །

[Block 2681]
སོ་ཕག་མི་འཕང་ངོ་ཞེས་བྱ་བ་ནི་ལག་ནས་ལག་ཏུ་སྦྱིན་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2682]
དེ་ནི་ལག་གི་ལས་དག་བྱེད་པ་ལ་བསྟན་པ་ཡིན་ཏེ། གང་གི་ཚེ་བརྗོད་དོ། །

[Block 2683]
བྱེ་བ༌[^1807]དང་གས་པ་མ་བརྗོད་པར་དེ་ཉིད་སྦྱིན་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ཉིད་ཅེས་བྱ་བ༌[^1808]ནི་བྱེ་བ༌[^1809]དང་གས་པ་ཉིད་དོ། །

[Block 2684]
རྐུན་པོ་སྤ་བཀོང་བའི་ཕྱིར་ཚམ༌[^1810]ངམ་བྱའོ་ཞེས་བྱ་བ་ནི་ཅི་དགར་བསྟན་པའི་དོན་དུ་དང་པོ་བྱའོ་ཞེས་བྱ་བའི་ཚིག་གོ། །

[Block 2685]
དེ་བཞིན་དུ་གཞན་རྣམས་ལ་ཡང་དང་པོ་ཆོ་གའི་ཚིག་རྣམས་ལ་རིག་པར་བྱའོ། །

[Block 2686]
གཎྜཱི་ལ་སོགས་པ་མི་འཕོག་པར་འཕང་ངོ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་གཎྜཱི་ལ་སོགས་པ་ཆོམ་རྐུན་པ་རྣམས་ལ་ཕོག་པར་མི་འགྱུར་བ་དེ༌[^1811]ལྟར་འཕང་བར་བྱ་སྟེ། ཅི་ནས་ཀྱང་གཞན་ལ་གནོད་པར་མི་འགྱུར་བར་བྱ་བའི་དོན་ཏོ། །

[Block 2687]
རྫི༌[^1812]ཕྱོགས་ན་རྡུལ་གྱི་བུམ་པ་དང་ཐལ་བའི་གྱོ་མོ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་འདིར་ཕོག་པ༌[^1813]ཡོངས་སུ་སྤོང་བ་ནི་མ་ཡིན་ཏེ་དེའི་ཕྱིར་འདིས༌[^1814]རྩོམ་པའོ། །

[Block 2688]
རྡུལ་གྱི་བུམ་པ་དང་ཐལ་བའི་གྱོ་མོ་སྟེ་ཞེས་བྱ་བའི་བསྡུ་བའོ། །

[Block 2689]
རྡུལ་དང་ཐལ་བ་དག་ནི་དཔེ་ཡིན་ཏེ། རྡུལ་འབྱིན་པའི་རྫས་རྣམས་ལ་བུམ་པ་དང་གྱོ་མོ་དག་ཀྱང་དེ་སྡུད༌[^1815]པར་བྱེད་པ་པོས་སོ། །

[Block 2690]
འུར་རྡོ་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་རྐུན་པོ་སྤ་བཀང༌[^1816]བར་བྱ་བའི་ཕྱིར་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2691]
དེའི་ཕྱིར་འཕེན་པར་བྱའོ། །

[Block 2692]
འདིར་འུར་རྡོ་འཕངས་པའི་དགོས་པ་ནི་ཆོམ་རྐུན་པ་རྣམས་ཕམ་པར་བྱ་བའི་དོན་དུ་ཆགས་པ་ཡོངས་སུ་སྤངས་པས་འདི་བཅང་བར་བྱ་སྟེ། འདིའི་དོན་དུ་ཞེས་བྱ་བ་འདིས་བྱ་བ་ཉིད་དོ། །

[Block 2693]
དགེ་སློང་ངལ་བ་མི་ཕུལ་ལོ་ཞེས་བྱ་བ་ནི་གཞན་ངལ་བ་ལ་དེ་དང་འདྲ་བས་ཉེས་བྱས་ཕྲ་མོར་རིག་པར་བྱའོ། །

[Block 2694]
དེའི་གྲོགས་བྱའོ་ཞེས་བྱ་བ་ལ། དེའི་ཞེས་བྱ་བ༌[^1817]ནི་དགེ་སློང་ངལ་བ་དེའོ།[^1818] །ཆོས་འདི་པའི་རབ་ཏུ་བྱུང་བ་ཉིད་འདི་ལྟ་བུའི་རིགས་ཅན་རྣམས་ལ་དགེ་སློང་གི་ཚིག་རྣམ་པར་གནས་སོ། །

[Block 2695]
དེ་བས་ན་དགེ་ཚུལ་ལ་ཡང་འདི་བྱའོ་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 2696]
གྲོགས་ཇི་ལྟ་བུས་ཤེ་ན༌[^1819]དེའི་ཕྱིར་ངལ༌[^1820]སོར་གཞུག་གོ། །

[Block 2697]
སྣོད་སྤྱད་བླང་བར་བླའོ།[^1821] །གལ་ཏེ་ལྷན་ཅིག་ཏུ་གནས་སུ་ཕྱིན་པར་མི་ནུས་ལ་ཟན་དང་སྒོམ་གྱི་དུས་སུ་མ་ཡིན་ན་ལྷུང་བཟེད་བཀྲུ་བ་དང་བྱུག་རིས་གཞག་པ་དང་བྱིན་ལེན་དང་བརྟག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་ཁྱོད་ལ་གྲོགས་པོ་དང་མཉམ་པར་གནས་སུ་ཕྱིན་པར་མི་ནུས་ལ་ཟན་དང་སྐོམ་གྱི་དུས་སུ་མ་ཡིན་ན་ལྷུང་བཟེད་བཀྲུ་བ་དང་བྱུག་རིས་གཞག་པ་དང་བྱིན་ལེན་དང་བརྟག་པར་བྱའོ། །

[Block 2698]
གལ་ཏེ་དུས་སུ་ན་ཁྱེར་ཏེ་བསུ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ཅི་སྟེ་དུས་ལ་ཡང་ཟས་དང་བཏུང་བ་དག་ལ་ཕྱིན་པར་ནུས་པ་མེད་ན་དེའི་ཕྱིར་ཁྱེར་ཏེ་བསུ་བར་བྱས་ཏེ་ཟན་དང་སྐོམ་དེ༌[^1822]བླངས་ནས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2699]
འདིར་ལྟུང་བས༌[^1823]ནི་ཕྱི་དྲོ་བཟུང༌[^1824]ངོ་ཞེས་བྱ་བ་ཤུགས་ཀྱིས་གོ་བར་བྱའོ། །

[Block 2700]
ཕམ་པར་འགྱུར་བ༌[^1825]གསུམ་པའི་རྣམ་པར་འབྱེད་པའོ།། །།
--- END BLOCKS ---
