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
སྔོན་གྱི་ལས་ཀྱང་ཕྱག་བརྐྱང༌[^1903]སྟེ་རིང་དུ་བྱས་ནས་གཞན་ལ་སྦྱིན་པ་བྱིན་པ་དང་། སྦྱིན་པར་བྱ་བའི་ཆོས་རྒྱ་ཆེ་བའི་ཕྱིར་མཐུན་ནོ། །

[Block 2662]
མདོམས་ཀྱི༌[^1904]སྦ་བ་སྦུབས་སུ་ནུབ་པ༌[^1905]ཞེས་བྱ་བ་ལ། མདོམས༌[^1906]ཀྱི་སྦ་བ་ནི་མདོམས༌[^1907]སུ་སྦ་བ་ཡིན་པས་མདོམས༌[^1908]ཀྱི་སྦ་བ་སྟེ། མདོམས༌[^1909]ཀྱི་སྦ་བ་སྦུབས་སུ་ནུབ་ཅིང་། མི་མངོན་པ་གང་ཡིན་པ་དེ་ལ་མདོམས༌[^1910]ཀྱི་སྦ་བ་སྦུབས་སུ་ནུབ་པ་ཞེས་བྱ་སྟེ། གསེར་གྱི་པདྨའི་སྙིང་པོ་སྦུབས་སུ་ནུབ་པ་འདྲ་བར་མདོམས༌[^1911]ཀྱི་སྦ་བའི་ཕྱོགས་སྦུབས་ཀྱི་ནང་དུ་མི་མངོན་པར་གྱུར་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2663]
སྔོན་གྱི་ལས་ཀྱང་མཛའ་བཤེས་དང་གཉེན་འདབ་ལ་སོགས་པ་འདུམ་པར་བྱས་པ་དང་། མ་ཕྱེ་བའི་ཕྱིར་སྦུབས་དང་སྦ་བ་དག་དེ་ལྟར་མཐུན་པར་གྱུར་ཏོ། །

[Block 2664]
གསང་ཐུབ་པར་བྱས་པས་སྦ་བའི་ཕྱོགས་མི་མངོན་པར་གྱུར་ཏེ་མཐུན་ནོ། །

[Block 2665]
མདོག་གསེར་འདྲ་བ་ཞེས་བྱ་བ་འདིས་ནི་སྐུ་མཁྲེགས་ཤིང་སྣུམ་ལ་ཁ་དོག་རབ་ཏུ་གསལ་བར་བསྟན་ཏོ། །

[Block 2666]
པགས་པ་སྲབ་ཅེས་བྱ་བ་འདིས་ནི་ཕྱི་དང་ནང་གི་རྡུལ་དང་དྲི་མ་ལ་སོགས་པས་སྐུ་ལ་གོས་པ་མེད་པར༌[^1912]བསྟན་ཏོ། །

[Block 2667]
ཕྱག་དང་ཞབས་བཀྲུ་བ་དང་ཁྲུས་བྱ་བ་ལ་སོགས་པ་ནི་དེར་རིམ་གྲོ་པ་རྣམས་བསོད་ནམས་ཐོབ་པར་བྱ་བ་དང་། དུས་སུ་བདེ་བར་བྱ་བའི་ཕྱིར་ཀུན་རྫོབ་ཀྱི་ཐ་སྙད་ཀྱི་ཕྱིར༌[^1913]མཛད་དོ། །

[Block 2668]
སྤུ་རེ་རེ་ནས་སྐྱེ་ཞིང་གཡས་སུ་འཁྱིལ་པ་ཞེས་བྱ་བ་ནི་སྤུའི་ཁུང་བུ་གཅིག་ནས་སྤུ་གཅིག་ཁོ་ན་སྐྱེ་བས་ན་སྤུ་རེ་རེ་སྐྱེ་བའོ། །

[Block 2669]
ཀྱིལ་ཀྱིལ་པོར་འཁྱིལ་བ་ནི༌[^1914]གཡས་ཕྱོགས་སུ་འཁྱིལ་བ་སྟེ། རྒྱན་གདུབ་ཀོར་སྦྲུལ་འཁྱིལ་བ་ལྟ་བུའམ། སྦྲུལ་འཁྱིལ་བའི་ཟླུམ་པ་ལྟ་བུ་སྟེ། གཉིས་ཀ་ཡང་གཡས་སུ་འཁྱིལ་བའོ། །

[Block 2670]
ཞལ་ལ་མཛོད་སྤུའི་མཚན་མངའ་བ་ཞེས་བྱ་བ་ནི་སྨིན་མཚམས་ཀྱི་ཐིག་ལེའི་གནས་ན་སྤུ་མཉེན་ཞིང་འཇམ་ལ་ཁ་དོག་དཀར་ཞིང་སྣུམ་པ། དྲངས་ན་ཁྲུ་གང་ངམ་ཁྲུ་དོ་འམ་ཁྲུ་གསུམ་ལ་སོགས་པའི་སྲིད་དུ་འབྱུང་ལ་སླར་བཏང་ན།[^1915] གཡས་སུ་འཁྱིལ་བ་རྩེ་མོ་གྱེན་དུ་ཕྱོགས་པ་དང་། ཤིང་ཏོག་སྐྱུ་རུ་ར་ཙམ་ལ་དངུལ་གྱི་སྒོ་ང་འདྲ་བ་གང་གི་ཞལ་ན་མཛེས་པར་འདུག་པ་དེ་ལ་ཞལ་ལ་མཛོད་སྤུའི་མཚན་མངའ་བ་ཞེས་བྱའོ། །

[Block 2671]
མཚན་འདི་གཉིས་ཀྱི་སྔོན་གྱི་ལས་ཀྱང་། འདུ་འཛི་སྤངས་པས་ནི་སྤུ་རེ་རེ་བར་གྱུར་ཏོ། །

[Block 2672]
ཕ་མ་ལ་སོགས་པ་ཇི་ལྟར་རིགས་པའི་གནས་སུ་བཀོད་པ་དང་། རིམ་གྲོ་བྱས་པ་དང་། སྦྱིན་པ་བྱིན་པ་དང་། མ་མགུ་བར༌[^1916]མ་བྱས་པ་ལ་སོགས་པས་གཡས་སུ་འཁྱིལ་ཞིང་རིང་བ༌[^1917]དང་། དབྱིབས་ལེགས་པར་གྱུར་ཏོ། །

[Block 2673]
རོ་སྟོད་སེང་གེའི་ལྟ་བུ་ཞེས་བྱ་བ་ནི་དེའི་རོ་སྟོད་སེང་གེའི་རོ་སྟོད་འདྲ་བའི་ཕྱིར་སེང་གེའི་རོ་སྟོད་ལྟ་བུ་སྟེ་བྲང་གི་དབྱེས་ཡངས་ཤིང་ཆེ་ལ་ཤ༌[^1918]རྒྱས་པས་སྤངས༌[^1919]ཤིང་ཆེ་བ་ཕུན་སུམ་ཚོགས་པའི་ཕྱིར་དེ་སྐད་ཅེས་བྱའོ། །

[Block 2674]
དཔུང་མགོ་ལེགས་པར་གྲུབ་པ་ཞེས་བྱ་བ་ལ། ལེགས་པའི་སྒྲ་ནི་ཟླུམ་པ་ལ་བྱའོ། །

[Block 2675]
གྲུབ་པའི་སྒྲ་ནི་མགུལ་པ་རྩའི་དྲ་བ་མི་མངོན་པ་བསྟན་པ་སྟེ། གསེར་གྱི་བུམ་པའི་མགུལ་པ་ལྟར་ཡོངས་སུ་ཟླུམ་ཞིང་ཤིན་ཏུ་མཁྲེགས༌[^1920]ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2676]
སྔོན་གྱི་ལས་ཀྱང་མི་སྙན་པར༌[^1921]མི་ཟེར་བ་ནི་སེང་གེའི་ཚུལ་དང་འདྲ་བ་དང་། མགུལ་མཛེས་པའི་རྒྱུ་ཡིན་ནོ། །

[Block 2677]
གཞན་ལ་མི་སྨོད་པ་ནི་སེང་གེ་ལྟར་ཡངས་པའི་རྒྱུའོ། །

[Block 2678]
སྙན་པར་སྨྲ་བ་དང་། ལེགས་པར་སྨྲ་བ་བརྗོད་པ༌[^1922]དང་། སེང་གེའི་སྒྲ་དང་མཐུན་པར་སྨྲ་བ་ནི་ལྐོག་མ་མཛེས་པའི་རྒྱུའོ། །

[Block 2679]
ཐལ་གོང་རྒྱས་པ༌[^1923]ཞེས་བྱ་བ་ནི་ཐལ་གོང་རྒྱས་ཤིང་ཡངས་པའོ། །

[Block 2680]
རོ་བྲོ་བ་མཁྱེན་པ་ཞེས་བྱ་བ་ནི་རོ་དྲུག་པོ་དག་གི་རོ་བྲོ་བ་མཁྱེན་པ་ལ་རོ་བྲོ་བ་མཁྱེན་པ་ཞེས་བྱའོ། །

[Block 2681]
སྐབས་འདིར་མཁྱེན་པ་ནི་དགའ་བ་ལ་བྱ་སྟེ། ཕར་འཛིན་མར་འཛིན་ཞེས་བྱ་བ་ལ་སོགས་པ་བཞིན་དུ། རོ་རྣམས་ཀྱིས་དགའ་ཞིང་ཚིམ་པར་གྱུར་པའི་ཕྱིར་རོ་བྲོ་བ་ཤེས་པ་ཞེས་བྱ་སྟེ་སྐྱེས་བུ་ཆེན་པོ་རྣམས་ཀྱིས༌[^1924]མིད་པ་ན་ནི་རོ་ཚོར་བར་བྱེད་པའི་རྩ་བདུན་སྟོང་གྱེན་དུ་ལྟ་བ་ཡོད་དོ། །

[Block 2682]
ཐ་ན་ཏིལ་གྱི་འབྲུམ་བུ་ཙམ་ཞིག་གསོལ་ན་ཡང་སྐུ་ཐམས་ཅད་དུ༌[^1925]ཁྱབ་པར་འགྱུར་རོ། །

[Block 2683]
རོ་ཐམས་ཅད་ཀྱི༌[^1926]ཞལ་དུ་བཅུག་ན། བདུད་རྩིའི་རོ་དང་འདྲ་བར་འགྱུར་ཏེ། དེ་ནི་མཚན་གྱི་ལས་སོ། །

[Block 2684]
སྔོན་གྱི་ལས་དང་མཐུན་པ་ནི་གོ་སླའོ། །

[Block 2685]
ཤིང་ནྱ་གྲོ་དྷ་ལྟར་ཆུ་ཞེང་གབ་པ་ཞེས་བྱ་བ་འདི་ལ་ཁ་ཅིག་ན་རེ་ནྱ་གྲོ་ཞེས་བྱ་བ་ནི་ངན་པ་སྟེ། རོ་སྨད་ལ་བྱའོ། །

[Block 2686]
རོ་དྷ་ཞེས་བྱ་བ་ནི་རོ་སྟོད་དོ། །

[Block 2687]
ཆུ་ཞེང་གབ་པ་ཞེས་བྱ་བ་ནི་མཐུན་པ་ལ་བྱ་སྟེ། གང་གི་སྐུ་ལྟེ་བ་ནས་བཟུང་སྟེ། རོ་སྟོད་དང་རོ་སྨད་ཚད་མཉམ་པར་གྱུར་པ་དེ་ལ་ནྱ་གྲོ་དྷ་ལྟར་ཆུང་ཞེང་གབ་པ་ཞེས་བྱ་བའོ་ཞེས་ཟེར་རོ། །

[Block 2688]
གཞན་དག་ན་རེ་ནྱ་གྲོ་ཞེས་བྱ་བ་ནི་སྐུའི་དབུ་ནས་ཞབས་ཀྱི་བར་གྱི་ཚད་ལ་བྱའོ། །

[Block 2689]
རོ་དྷ་ནི་ཞེང་ལ་བྱའོ། །

[Block 2690]
ཆུ་ཞེང་གབ་པ་ཞེས་བྱ་བ་ནི་འདོམ་ལ་བྱ་སྟེ། དེ་ལ་གང་གི་སྐུའི་ཆུ་ཞེང་འདོམ་དང་མཉམ་པར་གྱུར་པ་དེ་ལ་ནྱ་གྲོ་དྷ་ལྟར་ཆུ་ཞེང་གབ་ཅེས༌[^1927]བྱའོ་ཟེར་རོ། །

[Block 2691]
གཞན་དག་ནི་ཤིང་ནྱ་གྲོ་དྷ་ཞེས་བྱ་བ་སྡོང་པོ་དང་ཡལ་ག་རྣམས་ཆུ་ཞེང་མཉམ་པ་ཞིག་ཡོད་དེ། དེ་དང་འདྲ་བར་སྐྱེས་བུ་ཆེན་པོ་རྣམས་ཀྱི་སྐུ་ཐམས་ཅད་ཀྱང་འདོམ་གྱི་ཚད་དང་མཉམ་པ་ནི་ཤིང་ནྱ་གྲོ་དྷ་ལྟར་ཆུ་ཞེང་གབ་པ་ཞེས་བྱའོ་ཞེས་སྨྲའོ།[^1928] །དབུ་གཙུག་ཏོར་དང་ལྡན་པ་ཞེས་བྱ་བ་ནི་དབུ་ཟེའུ་ཀ་བཅིངས་པ་དང༌[^1929]འདྲ་བ་ལ་བྱ་སྟེ། གཞན་དག་གི་མགོ་ནི་ཡོངས་སུ་མ་རྒྱས་ཤིང་མཐོ་དམན་ཅན་ལ། མི་མཉམ་པ་དག་ཡོད་ཀྱི། སྐྱེས་བུ་ཆེན་པོ་རྣམས་ཀྱི་དབུ་ནི་གཙུག་ཏོར་བཞིན་དུ་སྙོམས་ཤིང་ཡོངས་སུ་ཟླུམ་པ་དང་། ཡོངས་སུ་རྫོགས་ཤིང་དབྱིབས་ལེགས་པ་དང་། ལེགས་པར་རྒྱས་པ་ཡིན་ནོ་ཞེས་འཆད་དོ། །

[Block 2692]
གཞན་དག་ན༌[^1930]རེ་མཚན་འདི་ནི་འཕྲལ་བའི་དབྱེས་ཡོངས་སུ་རྒྱས་པ་བསྟན་པའི་ཕྱིར་ཏེ། སྐྱེས་བུ་ཆེན་པོ་རྣམས་ཀྱི་འཕྲལ་བ༌[^1931]ནི་རྣ་བ་གཡས་པའི་གོང་ནས་རྣ་བ་གཡོན་པའི་གོང་གི་བར་དུ་ཤའི་དབྱིབས་ལེགས་པ། འཕྲལ་བའི༌[^1932]དབྱེས་ཡོངས་སུ་རྫོགས་པ། རྒྱལ་པོ་གསེར་གྱི་གཙུག་ཏོར་བཅིངས་པ༌[^1933]འདྲ་བར་མཛེས་པའོ་ཞེས་སྨྲའོ། །

[Block 2693]
སྔོན་གྱི་ལས་ཀྱང་དགེ་བའི་ལས་བྱེད་པ་ཐམས་ཅད་ཀྱི་ཐོག་མར་འགྲོ་བ་གཙོ་བོར་གྱུར་ནས་ཁོར་ཡུག་ཏུ་ཀུན་དགའ་ར་བ་དང་། འདུན་ཁང་དང་། བཏུང་བའི་གནས་ལ་སོགས་པ་བྱས་པ་སྟེ། དེའི་ཕྱིར་ནྱ་གྲོ་དྷ་ལྟར་ཆུ་ཞེང་གབ་པའོ། །

[Block 2694]
གང་གི་ཕྱིར་ཚོགས་ཀྱི་གཙོ་བོར་གྱུར་ནས། མ་ཞུམ་པར་མགོ་བསྟོད་དེ་འཇིག་པ༌[^1934]མེད་པར་སྦྱོར་བ་དེའི་ཕྱིར་དབུ་གཙུག་ཏོར་ཅན་དུ་གྱུར་ཏོ། །

[Block 2695]
དེ་བས་ན་མངའ་དབང་ཆེན་པོ་མངའ་བའི་སྔ་ལྟས་ཞེས་བྱའོ། །

[Block 2696]
ལྗགས་རིང་ཞིང་སྲབ་པ་ཞེས་བྱ་བ་རིང་བ་ནི་ཆེ་བའམ་ཁྲུན་རིང་བའོ། །

[Block 2697]
སྲབ་པ་ནི་མཉེན་པའོ། །

[Block 2698]
ཚངས་པའི་དབྱངས་ཞེས་བྱ་བ་ནི་ཚངས་པའི་དབྱངས་དང་མཚུངས་པའམ། དབྱངས་མཆོག་ཡིན་པའི་ཕྱིར་ཏེ། བྱ་ཀ་ལ་པིང་ཀའི་གསུང་ཞེས་བྱ་བ་ནི༌[^1935]བྱ་ཀུ་ར་བའི༌[^1936]སྐད་ལྟ་བུའོ། །

[Block 2699]
ཟླ་བའི་དཀྱིལ་འཁོར་མ་ཉ་བ་ཚེས་བཅུ་གཉིས་ཀྱི༌[^1937]ཤས་འདྲ་བར་འགྲམ་པའི་མཐའ་ཤ་མཁྲེགས་ཤིང་ལེགས༌[^1938]པར་ཟླུམ་པའི་ཕྱིར་འགྲམ་པ་སེང་གེའི་ལྟ་བུའོ། །

[Block 2700]
སྐར་མ་པ་བ་སངས་པས༌[^1939]ཀྱང་ལྷག་པར་འོད་གསལ་ཞིང་དཀར་བའི་ཕྱིར་ཚེམས་ཤིན་ཏུ་དཀར་བའོ། །
--- END BLOCKS ---
