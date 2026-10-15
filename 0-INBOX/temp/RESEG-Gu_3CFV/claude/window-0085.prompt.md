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
[Block 2976]
བསྟེན་པར་བྱ་བ་འཆོས་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 2977]
ད་འདི་མན་ཆད་ནི་རེག་པར་བྱ་བ་མ་ཡིན་པ་དང་། བསྟེན་པའི་ལྟུང་བྱེད་བཅུ་གཅིག་པོ་རྣམས་སྟོན་ཏེ། དགེ་སློང་མས་སྐྱེས་པ་རེག་པར་བྱ་བ་མ་ཡིན་པ་དེ་དང་ལྷན་ཅིག་རེག་པའི་ཚུལ་གྱིས་བསྟེན་པ་གང་ཡིན་པ་དེ་རྣམས་ལ་རེག་པར་བྱ་བ་མ་ཡིན་པ་དང་བསྟེན་པའི་ལྟུང་བྱེད་རྣམས་ཤེས་པར་བྱའོ། །

[Block 2978]
དེ་ལ་དེ་དག་གི་དང་པོ་ཇེ་བཤད་པར་བྱ་སྟེ། དེའི་ཕྱིར་ཁྱིམ་པ་དང་ལྷན་ཅིག་དབེན་པ་སྐྱབས་ཡོད་པ་ན༌[^1923]འགྲེང་བ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདོམ་གང་གི་ནང༌[^1924]ཚུན་ཆད་ཅེས་བྱ་བ་དེ་དགེ་སློང་གི་དབང་དུ་བྱས་པའི་ཆོ་གའི་རྗེས་སུ་འབྲངས་ནས་ཤེས་པར་བྱའོ། །

[Block 2979]
འདུག་པ་ལ་ཡང་ལྟུང་བྱེད་འདི་ཡིན་ཏེ། འཇུག་པ་དེ་ལ་ཤིན་ཏུ་ལྕི་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2980]
མི་ཚངས་པར་སྤྱད་པའི་ཡན་ལག་ཏུ་གྱུར་པ་དེ་ཐམས་ཅད་ལ་མི་ཚངས་པར་སྤྱོད་པ་དང་འབྲེལ་པ་ལ་སྟོབས་དང་ལྡན་པ་ཉིད་ལ་འགལ་ཟླར་རྣམ་པར་གནས་པ་ཉིད་དོ། །

[Block 2981]
དེ་བས་ན་སྟོབས་དང་མི་ལྡན་པ་ཉིད་དེ་ནི་འདིར་ན་སྨད་པར་རིག་པར་བྱའོ། །ཇི་ཙམ་དབེན་པ་སྐྱབས་ཡོད་པར་བརྗོད་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་རྩིག་པ་དང་སབ་མོ་དང་ཡོལ་བ་དང་། ཐིབས་པོ་དང་མུན་པ་དག་གིས་ནི་དེ་ཉིད་འགྲུབ་བོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ལྔ་པོ་འདི་རྣམས་ཀྱིས་དབེན་པ་སྐྱབས་ཡོད་པར་གྲུབ༌[^1925]པོ། །འདིར་རྩིག་པའི་སྒྲས་ནི་རྩིག་པ་ཉིད་བརྗོད་དོ། །

[Block 2982]
འདི༌[^1926]མན་ཆད་ནི་རེག་པར་བྱ་བ་མ་ཡིན་པ་དང་བསྟེན་པ་གང༌[^1927]ཡིན་ཞེ་ན། དེའི་ཕྱིར་དགེ་སློང་དང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་སློང་དང་ལྷན་ཅིག་དབེན་པ་སྐྱབས་ཡོད་པ་ན་འགྲེང་བ་ལའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2983]
གསུམ་པ་གང་དུ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་བླ་གབ་མེད་པར་སྔ་མ་དང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་དུ་བླ་གབ་མེད་པར༌[^1928]ཞེས་བྱ་བ་སྒྲིབ་པ་མེད་པའི་ཕྱོགས་ནི༌[^1929]སྔ་མ་དང་ངོ་ཞེས་བྱ་བ་ནི་ཁྱིམ་པ་དང་ལྷན་ཅིག་འགྲེང་བ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2984]
བཞི་པ་གང་ལ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ཕྱི་མ་དང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བླ་གབ་མེད་པར་དགེ་སློང་ཕྱི་མ་དང་ལྷན་ཅིག་གནས་པ་ལའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2985]
གསུམ་པོ་དེ་རྣམས་ལ་ནི་འདུག་པ་ལ་ཡང་ལྟུང་བྱེད་ཁོ་ནར་འགྱུར་རོ། །

[Block 2986]
དེ་གྲོགས་དང་བཅས་པ་ཉིད་ཡིན་ན་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ལ། དེ་ལ་ཞེས་བྱ་བ་ལ་དགེ་སློང་ལའོ། །

[Block 2987]
གྲོགས་དང་བཅས་པ་ཉིད་ཡིན་ན་ཞེས་བྱ་བ་ནི་གཉིས་དང་བཅས་པ་ཉིད་ལ་ནི་ལྟུང་བ་མེད་དོ། །

[Block 2988]
འདིར་གཞུང་ནི། གལ་ཏེ་དགེ་སློང་གྲོགས་དང་བཅས་པ་ཉིད་ཡིན་ན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2989]
དགེ་སློང་མ་ཁྲིམས་ཟླ་དང་བཅས་པ་གཅིག་ཡིན་ན་ཡང་ངོ་ཞེས་བྱ་བ་ཡང་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་དང་སྦྱར་རོ། །

[Block 2990]
ཐག་ཇི་སྲིད་ཀྱི་དབང་གིས་གྲོགས་དང་ཐ་དད་པ་ཉིད་མ་ཡིན་པར་གནས་པའི་ཐག་དེ་ཙམ་ན་གྲོགས་འདུག་ན་ཁྲིམས་ཟླ་དང་བཅས་པ་ཉིད་ཡིན་ཏེ། དེ་ཕྱི་ནས་འབྲང་བའི་དགེ་སྦྱོང་ཉིད་དུ་གཏོགས་པར་བྱའོ། །

[Block 2991]
གང་ལ་བསླབ་པའི་གཞི་ལྔ་པར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་ཁྱིམ་པའི་རྣར་བཤུབ་ཅིང་སྨྲ་བ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བྱེ་བྲག་མ་བསྟན་པས་དབེན་པ་སྐྱབས་ཡོད་པ་ཡང་རུང་། བླ་གབ་མེད་པ་ཡང་རུང་། གྲོགས་ཡོད་པ་ཡང་རུང་། གཅིག་པུ་ཡང་རུང་བ་ཤེས་པར་བྱའོ། །

[Block 2992]
འདིར་སྨྲ་བ་ལའོ་ཞེས་བྱ་བ་ནི་གང་ཡང་རུང་བ་འབྲེལ་བའི་དོན་དང་འབྲེལ་པ་མེད་པའི་དོན་ནམ་དོན་དང་བཅས་པའམ། དོན་མེད་པའི་ཚིག་སྨྲ་བ་ལ་ཁ་ན་མ་ཐོ་བ་འདི་ཡིན་ནོ། །

[Block 2993]
དབེན་པར་སྨྲ་བ་ཉམས་སུ་མྱོང་བ་འདིར་གཙོ་བོ་ཉིད་དུ་རྣམ་པར་གཞག་པས་དཔུང་མགོའི་ཕྱི་རོལ་གྱི་མཐའ་ལས་སྨྲ་བ་མོའི་ཀོ་སྐོའི༌[^1930]མཐའ་ཆ་འདས་ན་དེ་ནི་རྣར་བཤུབ་ཅིང་ཉེ་བར་འབྲེལ་པའི་ལྟུང་བྱེད་ཀྱི་དང་པོར་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 2994]
མདུན་རོལ་དུ་སྙིང་གའི༌[^1931]རུས་པ་དང་། ཕྱི་ནས་མཆན་ཁུང་གི་ཕྱོགས་ནས་སྨྲ་སྟེ་གོ་ནའོ། །

[Block 2995]
དྲུག་པ་གང་ཞེ་ན་དེ་ལས་དེས་དེ་ཉན་པ་ལའོ་ཞེས་བྱ་བ་ནི། དེས་སྨྲས་པ་དེ་ཅུང་ཟད་པ༌[^1932]ལ་མཐའ་ཞེས་བྱ་བའོ། །

[Block 2996]
དེ་བཞིན་དུ་རྣ་བ་དང་ཉེ་བར་སྨྲ་བ་འདི་བཟུང་བ་ལ་ཁྱིམ་པ་དེ་ལས་རྣར་བཤུབ་ཅིང་སྨྲ་བ་ལའོ། །

[Block 2997]
བདུན་པ་ནི་དགེ་སློང་གིའོ་ཞེས་བྱ་བ་སྟེ། རྣར་བཤུབ་ཅིང༌[^1933]སྨྲ་བ་ལ་ཁ་ན་མ་ཐོ་བ་འདིར་འགྱུར་རོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2998]
བསླབ་པའི་གཞི་བརྒྱད་པ་ནི་དེ་ལས་ཀྱང་ངོ་ཞེས་བྱ་བ་ལ། ཀྱང་ངོ་ཞེས་བྱ་བའི་སྒྲས་ནི་རྣར་བཤུབ་ཅིང་སྨྲ་བ་ཉན་པ་ལའོ་ཞེས་བྱ་བའི་རྗེས་སུ་བསྙེགས༌[^1934]པའི་ཕྱིར་རོ། །

[Block 2999]
དེ་ལས་ཀྱང་ངོ་ཞེས་བྱ་བ་ཡང་སྒྲས་འདིས་དགེ་སློང་དང་ཁྱིམ་པ་གཉིས་ཀ་ཡང་བཟུང་བ་ཡིན་ཏེ། གཉིས་པོ་དེ་དག་གི་དྲུང་དུ་རྣར་བཤུབ་ཅིང་སྨྲ་བ་ཉན་པ་ལ་ལྟུང་བྱེད་དུ་བལྟ་བར་བྱའོ། །

[Block 3000]
ཁྱིམ་པ་དང་ལྷན་ཅིག་པ་ཉིད་ལ་རྣམ་པ༌[^1935]འདིར་འགྱུར་བའམ་བྱེ་བྲག་མེད་པར་རོ། །

[Block 3001]
དེ་ལ་ཁྱིམ་པ་དང་ལྷན་ཅིག་པའི་རྣམ་པའམ་དགེ་སློང་དང་ལྷན་ཅིག་ཏུ་གྱུར་པ་ལ་ལྟུང་བ་མེད་པ་ཐོབ་པའོ། །

[Block 3002]
བྱེ་བྲག་མེད་པར་སྨྲ་བ་ལ་དགེ་སློང་དང་ལྷན་ཅིག་པ་ཉིད་ནི་དགེ་འདུན་གྱི༌[^1936]ཁོངས་སུ་འདུས་པ་ཉིད་ཀྱི་ཕྱིར་འདི་ལ་ཉེས་པ་མེད་དོ། །

[Block 3003]
དེ་ལྟ་བས་ན་དགོས་པ༌[^1937]འདི་ལ་ལྟུང་བ་མེད་ཅེས་བྱ་བའོ། །

[Block 3004]
དེ་བས་ན་ཁྱིམ་པ་དང་དགེ་སློང་གི་དབྱེ་བ་ལ་སོགས་པ་ལ་བརྟེན་ནས་བཅས་པ་འདི་རྣམས་མཛད་དོ། །

[Block 3005]
དགེ་སློང་དང་ལྷན་ཅིག་པ་ཉིད་ལ་དགེ་ཚུལ་ལ་འདིར་དགེ་སློང་ཉིད་ཅེས་སྨོས་ཏེ། ཉེས་དམིགས་མཚུངས་པ་ཉིད་ཀྱི་ཕྱིར་འདིར་ཡོངས་སུ་རྫོགས་པ་ཉིད་དང་། འདིར་ཕྱི་རོལ་པའི་རབ་ཏུ་བྱུང་བ་ལ་ཁྱིམ་པ་ཉིད་ཅེས་གོ་བར་བྱའོ། །

[Block 3006]
དགུ་པ་གང་ལ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ཁྱིམ་པ་ལས་རིག་པ་ལེན་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་སློང་མས་ཁྱིམ་པ་ལས་རིག་པ་གང་ཡང་རུང་བ་ལན་པ༌[^1938]ལ་ལྟུང་བྱེད་འདིར་འགྱུར་རོ། །

[Block 3007]
འདི་ནི་སྦོམ་དགའ་མོས་ཆགས་པར་གྱུར་པས་སྐྱེས་པ་ལས་རིག་པ་བླངས་ནས། དེའི་ཚིག་ཉན་དུ་གཞུག་པའི་ཕྱིར། ཡང་དང་ཡང་དུ་བཟླས་པ་འཆོལ་བར་བྱེད་པ་དེ་ལས་བཅས་པ་ཡིན་ན། །[^1939]

[Block 3008]
བཅུ་པ་ནི་དེ་ལས་དེ་ཀློག་པ་ལའོ་ཞེས་བྱ་བ་ལ། དེ་ལས་ཞེས་བྱ་བ་ནི་ཁྱིམ་པ་ལའོ། །

[Block 3009]
དེ་ཞེས་བྱ་བ་ནི་རིག་པའོ། །

[Block 3010]
ཀློག་པ་ལ་ནི་ལྟུང་བྱེད་དོ། །

[Block 3011]
འདིར་རིག་པ༌[^1940]ཞེས་བྱ་བ་ནི་དཔེ་ཙམ་དུ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 3012]
བསྒོམ་པར་བྱ་བ་མ་ཡིན་པ་ཐམས་ཅད་ལ་ཡོངས་སུ་རྫོགས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 3013]
ཁ་ན་མ་ཐོ་བ་འདི་བྱེད་དུ་བཅུག་ནས་དགེ་སློང་དང་ལྷན་ཅིག་པ་ཉིད་དུ་འདིར་དགེ་སློང་མ་དང་དགེ་སློབ་མ་སློབ་དཔོན་དུ་རིགས་པ་ཉིད་ཀྱི་ཕྱིར༌[^1941]ལྟུང་བ་མེད་པའོ། །

[Block 3014]
འདིར་ཡང་དགེ་སློང་དང་ལྡན་པ་ཉིད་ནི་དགེ་ཚུལ་ལ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 3015]
འདི་དང་ཡང་ལྷན་ཅིག་ཏུ་རིགས་པ་ཉིད་ཀྱི་ཕྱིར། དགེ་སློབ་མས་སློབ་མ་དང་སློབ་དཔོན་ཉིད་དུ་ཕྱི་རོལ་པའི་རབ་ཏུ་བྱུང་བ་ལ་ཁྱིམ་པ་ཉིད་ཡོངས་སུ་རྫོགས་པ་ཁོ་ནའོ། །
--- END BLOCKS ---
