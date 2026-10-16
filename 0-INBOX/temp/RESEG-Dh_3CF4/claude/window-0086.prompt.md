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
[Block 3011]
འཇིང༌[^1909]ནི་རབ་ཏུ་འཇིགས་སུ་རུང་བ་སྟེ། དེའི་རབ་ཏུ་འཇིགས་སུ་རུང་བ་ནི། གློག་ཕྲན་འགྱུ་བའི་འོད་འབར་ལྕེ་གཡོ་བ། །ཞེས་བྱ་བའི་ཚིགས༌[^1910]བཅད་གསུམ་གྱིས་བསྟན་ཏེ། དེའི་རབ་ཏུ་འཇིགས་སུ་རུང་བ་ནི་སྤྲིན་དང་བ་དང་། སྣང་བ་ནུབ་པ་དང་། དེའི་མི་མཐུན་པའི་ཕྱོགས་ཀྱི་ལྟས་ངན་འབྱུང་བ་སྟོན་པས་སོ། །

[Block 3012]
གློག་ཕྲན་འགྱུ་བ་ཞེས་བྱ་བ་འདིའི་བསྡུས་པའི་དོན་ནི་མདོག་དང་ཚད་དང་། སྒྲ་དང་།[^1911] སྤྲིན་གྱི་ཁྱད་པར་ཏེ། གློག་ཕྲན་འགྱུ་བ་འོད་འབར་ལྕེ་གཡོ་བ། །ཞེས་བྱ་བ་དང་།

[Block 3013 [VERSE]]
སྔོ་བ་ཞེས་བྱ་བས་ནི་མདོག་བསྟན་ཏོ། །
སྤྲིན་གྱིས་ཉི་མའི་ལམ་ཡང་བསྒྲིབས་པར་འགྱུར། །

[Block 3014]
ཞེས་བྱ་བ་འདིས་ནི་ཚད་བསྟན་ཏོ། །

[Block 3015]
སེམས་སྟོབས་ཡོན་ཏན་བསམ་པ་སྟོན༌[^1912]ཞེས་བྱ་བ་ནི་སྙིང་སྟོབས་ཉིད་ཀྱི་ཡོན་ཏན་གང་ཡིན་པ་དེ་ནི་སེམས་སྟོབས་ཡོན་ཏན་ཏེ། སེམས་སྟོབས་ཀྱི་ཡོན་ཏན་ཇི་ལྟ་བ་བཞིན་དུ་བསམ་པ་ནི་འདོད་པ་སྟེ་སྟོན་ཅིང་སྨྲ་བའོ། །

[Block 3016]
དེ་དག་སྐྲག་ཅིང་སྤ༌[^1913]གོང་མི་སྨྲ་ཞུམ། །ཞེས་བྱ་བ་ནི་སེམས་ཅན་དམན་པའི་དབང་དུ་བྱས་པའོ། །

[Block 3017]
བརྟན་པོ་དག་ནི་ཐར་པའི་ཐབས་ལ་འབད། །ཅེས་བྱ་བ་ནི་སེམས་ཅན་དམན༌[^1914]པའི་དབང་དུ་བྱས་པའོ། །

[Block 3018]
ཁ་ཅིག་རང་གི་ལྷ་ལ་གསོལ་བ་འདེབས། །ཞེས་བྱ་བ་ནི་བར་མའི་དབང་དུ་བྱས་པའོ། །

[Block 3019]
འཇིགས་པ་དང་བག་ཚ་བ་ནི་འཇིགས་ཤིང་བག་ཚ་བ་སྟེ། སེམས་དང་ལུས་ལ་གོ་རིམས་བཞིན་དུའོ། །

[Block 3020]
དེ་གཉིས་ཀྱིས་ཅི་བྱ༌[^1915]གཏོལ་མེད་པ་ནི་འཇིགས་ཤིང་བག་ཚ་བས་ཅི་བྱ་གཏོལ་མེད་པའོ། །

[Block 3021]
ལྟས་ངན་གློ་བུར་དུ་བྱུང་བ་ནི༌[^1916]ལྟས་ངན་གློ་བུར་དུ་བྱུང་བར་གྱུར་པའོ།[^1917] །ལྟས་ངན་གློ་བུར་དུ་བྱུང་བ་ཡིན་ལ་འཁྲུགས་པ་ཡང་ཡིན་པས་ལྟས་ངན་གློ་བུར་བྱུང་བས་འཁྲུགས་པའོ། །

[Block 3022]
དེ་ནི་རྒྱུས་ཉོན་མོངས་པར་གྱུར་པ་ནི་ལྟས་ངན་གློ་བུར་དུ་བྱུང་བས་འཁྲུགས་ཤིང་ཉོན་མོངས་པར་གྱུར་པའོ། །

[Block 3023]
འདི་ལྟ་བུས་ཞེས་བྱ་བ་ནི་ངོ་མཚར་མི་ཆེ་བའི་ཕྱིར་རོ། །

[Block 3024]
ཞུམ་པས་ཕོངས་ལས་ཐར་ལ་མི་ཕན་གྱིས། །ཞེས་བྱ་བ་ནི་གང་སྔར་བསྟན་པ་དེ་དག་སྐྲག་ཅིང་མི་སྨྲ་བས་སྤ༌[^1918]གོང་ཞུམ་ཞེས་བྱ་བ་དེའི་དབང་དུ་བྱས་པའོ། །

[Block 3025]
མྱ་ངན་གདུང་བར་མ་བྱེད་པར། །ཞེས་བྱ་བ་ནི་གང་སྔར་བསྟན་པའི་རང་གི་ལྷ་ལ་གསོལ་བ་འདེབས་ཞེས་བྱ་བ་དེའི་དབང་དུ་བྱས་པ་སྟེ། གང་གི་ཕྱིར་མྱ་ངན་དང་གདུང་བས་ནི་རང་གི་སྐྱེས་བུ་བྱེད་པ་ཉམས་པར་འགྱུར་ཞིང་ལྷ་ལ་གསོལ་བ་མཆོག་ཏུ་འཛིན་པས་ཀྱང་ངོ་། །བརྟན་བྱས་ནས༌[^1919]ཞེས་བྱ་བ་ནི་གང་སྔར་བསྟན་པའི་བརྟན་པོ་དག་ནི་ཐར་པའི་ཐབས་ལ་འབད། །ཅེས་བྱ་བ་དེའི་དབང་དུ་བྱས་པའོ། །

[Block 3026]
འཇིགས་པ་དང་མི་དགའ་བ་ནི་འཇིགས་ཤིང་མི་དགའ་བའོ། །

[Block 3027]
མཁས་པ་ནི་ཐབས་ཤེས་པའོ། །

[Block 3028]
གཟི་བརྗིད་བརྟན་པས་ཞེས་བྱ་བ་ནི་སྐྱེས་བུ་བྱེད་པའི་གཟི་བརྗིད་ཀྱིས་ཏེ་གཟེངས་བསྟོད་པའོ། །

[Block 3029]
དོན་ཐམས་ཅད་གྲུབ་པ་ལག་པའི་རྩེ་ལ་ཡོད་པ་དེ་ནི་དོན་རྣམས་ཐམས་ཅད༌[^1920]གྲུབ་པ་ལག་ན་ཡོད་པའོ། །

[Block 3030]
སྟེང་དུ་འབྱུང་བ་ནི་གྱེན་དུ་འབྱུང་བའོ། །

[Block 3031]
འཇུག་པ་ནི་ནང་དུ་འཇུག་པའོ། །

[Block 3032]
གཡོ་བ་ནི་ཐད་ཀར་འགྲོ་བ་སྟེ། དེ་དག་གི་ཞར་ནི་ཞར་ཡིན་ཏེ། སྟེང་དུ་འབྱུང་ཞིང་ནང་དུ་འཇུག་པའི་ཞར་ལའོ། །

[Block 3033]
དེ་བས་ན་བདག་ཅག་ཡུལ་ནི་གཉིས༌[^1921]ལས་ཞེས་བྱ་བ་ནི་འདི་ལྟར་བདག་ཅག་ཡུལ་གང་ལས་བྱུང་བ་དང་། གང་དུ་འགྲོ་བར་འདོད་པའི་ཡུལ་ལོ། །

[Block 3034]
འབབ་པ་ནི་ཆུའི༌[^1922]རྒྱུན་ནོ། །

[Block 3035]
ནུབ་ཕྱོགས་ནས་ཞེས་བྱ་བ་ནི་ནུབ་ཕྱོགས༌[^1923]ཀྱི་ཕྱོགས་ནས་སོ། །

[Block 3036]
དངུལ་གྱི་མདོག་ནི་དངུལ་གྱི་ཁ་དོག་སྟེ། དེ་དང་འདྲ་བའི་ཆུ་དཀར་པོ་གང་ཡིན་པ་དེ་ནི་དངུལ་གྱི་མདོག་འདྲ་བའི་ཆུ་དཀར་པོའོ། །

[Block 3037]
དབུ་བ་མང་པོ་འཁྲིགས་ཤིང་སྐྱ་བ་དེ་ནི་དབུ་བ་མང་པོ་འཁྲིགས་ཤིང་སྐྱ་བའོ། །

[Block 3038]
འོ་མའི་རྒྱ་མཚོ་ཞེས་བྱ་བ་དེ་ནི་འཇིག་རྟེན་པ་རྣམས་ཀྱིས་དེ་ལྟར་མིང་དུ་བརྗོད་པ་སྟེ། ཞོའི་ཕྲེང་བ་ཞེས་བརྗོད་དོ། །

[Block 3039]
མི་མཐུན་པའི་རླུང་གིས་ཞེས་བྱ་བ་ནི་འདོད་པའི་ཡུལ་དང་མི་མཐུན་པར་གྱུར་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3040]
གསེར་གྱི་མདོག་འདྲ་བའི༌[^1924]རླབས་ཀྱི་ཕྲེང་བ་རབ་ཏུ་འཁྲུགས་པ་གང་ཡིན་པ་དེ་ནི་རླབས་ཀྱི་ཕྲེང་བ་རབ་ཏུ་འཁྲུགས་པའི༌[^1925]གསེར་གྱི་མདོག་འདྲ་བའོ། །

[Block 3041]
མེ་འབར་བ་ཉིད་སེར་སྐྱ་ཡིན་པས་ཆུའི་མདོག་མེ་འབར་བ་སེར་སྐྱ་སྟེ་ཆུ་དེའོ། །

[Block 3042]
སྔོ་བ་མ་ཡིན་ཏེ་ཞེས་བྱ་བ་ནི་རང་བཞིན་གྱིས་དམར་བ་ཡིན་པས་སྔོན་པོ་དགག་པ་སྟེ། གནས་སྐབས་ཀྱི་དབང་གིས༌[^1926]དེ་དམར་བར་རྟོགས་པར་བྱའོ། །

[Block 3043]
སྦུར་ལོང༌[^1927]དང་ཨནྡ་རྙིལ་ནི་སྦུར་ལོང༌[^1928]དང་ཨནྡ་རྙིལ་ལོ། །

[Block 3044]
དེ་གཉིས་ཀྱི་མདོག་གང་ལ་ཡོད་པ་དེ་ནི་སྦུར་ལོང༌[^1929]དང་ཨནྡ་རྙིལ་གྱི་མདོག་གོ། །

[Block 3045]
དེ་གཉིས་དང་འདྲ་བའི་ཆུ་གང་ཡིན་པ་དེ་ནི་སྦུར་ལོང༌[^1930]དང་ཨནྡ་རྙིལ་གྱི་མདོག་འདྲ་བའོ། །

[Block 3046]
ཆུ་དེ་ཡོངས་སུ་སྨིན་པའི་ཀུ་ཤ༌[^1931]དང་འདྲ་བའི་ཁ་དོག་ཀྱང་ཡོད་པས་སོ། །

[Block 3047]
སྨྱིག་མའི་མདོག་དང་། བཻ་ཌཱུརྱའི་འོད་ནི་སྨྱིག་མའི་མདོག་དང་བཻ་ཌཱུརྱའི་འོད་དོ། །

[Block 3048]
དེ་དང་འདྲ་བར༌[^1932]ནི་མཐུན་པར་སྣང་བ་སྟེ། སྔོ་བའི་ཆུ་གང་ཡིན་པའོ། །

[Block 3049]
རྒྱ་མཚོ་ཡང་བླ་འོག་བཟློག་པ་འདྲའོ། །

[Block 3050]
ཞིང་ཞེས་བྱ་བ་ནི་ཁས་བུབ་ཏུའོ། །
--- END BLOCKS ---
