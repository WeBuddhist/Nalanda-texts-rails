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
[Block 2241 [HEADING]]
##### ལུས་ལ་ལུས་ཀྱི་རྗེས་སུ་ལྟ་ཞིང་གནས་པ། ^8-1-1-5-0

[Block 2242]
ཇི་ལྟར་ན་བྱང་ཆུབ་སེམས་དཔའ་ལུས་ལ་ལུས་ཀྱི༌[^1953]རྗེས་སུ་ལྟ་ཞིང་གནས་ཤེ༌[^1954]ན་ཞེས་བྱ་བ་ནི་དྲིས་པའོ། །

[Block 2243]
དྲིས་པའི་ལན་གདབ་པའི་ཕྱིར་དེ༌[^1955]རང་གི་ལུས་དང་གཞན་གྱི་ལུས་ལ་ལུས་ཀྱི་རྗེས་སུ་ལྟ་ཞིང་གནས་ཏེ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2244]
དེ་ལ་རང་གི་ལུས་ནི་བྱང་ཆུབ་སེམས་དཔའ་ཉིད་ཀྱི་ལུས་སོ། །

[Block 2245]
གཞན་གྱི་ལུས་ནི་སེམས་ཅན་རྣམས་ཀྱི་ལུས་སོ། །

[Block 2246]
ཡང་ན་རང་གི་ལུས་ནི་མིག་དང་རྣ་བ་དང་། སྣ་དང་ལྕེ་དང་ལུས་ཀྱི་དབང་པོས་ཟིན་པའི་གཟུགས་སོ། །

[Block 2247]
གཞན་གྱི་ལུས་ནི་གཟུགས་དང་སྒྲ་ལ་སོགས་པའི་ཕྱིར༌[^1956]སྐྱེ་མཆེད་རྣམས་སོ། །

[Block 2248]
ལུས་ཀྱི་རྗེས་སུ་ལྟ་བ་ནི་ཤེས་རབ་སྟེ༌[^1957]རང་དང་གཞན༌[^1958]གྱི་ལུས་ཀྱི་རང་དང་སྤྱིའི་མཚན་ཉིད་གང་ཡིན་པ་ལ་རྟོག་པར་བྱེད་པའོ། །

[Block 2249]
གནས་པ་ནི་ཏིང་ངེ་འཛིན་ཏེ་ཤེས་རབ་ཀྱིས༌[^1959]བརྟགས་པའི་ཆོས་དེ་ལ་རྒྱུན་དུ་དམིགས་པའོ། །

[Block 2250]
དེ་ལྟར་ཤེས་རབ་ཀྱིས་རྟོག་ཅིང་ཏིང་ངེ་འཛིན་གྱིས་དམིགས་པ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 2251]
ལུས་ཀྱི་སྔོན་གྱི་མཐའ་ལ་ཡང་རྟོག་ལུས་ཀྱི་ཕྱི་མའི་མཐའ་ལ་ཡང་རྟོག་ཅེས་བྱ་བ་གསུངས་ཏེ། ལུས་ཀྱི་སྔོན་གྱི་མཐའ་ནི་ལུས་དང་པོ་མའི་མངལ་དུ་བྱུང་བའི་དུས་ཏེ། དེ་ལ་ལུས་འདི་ལ་ཡང་ཕྱིན་ཅི་ལོག་གིས་རྒྱུ་བྱས་ཤིང་ཕ་མའི་ཁུ་བ་དང་ཁྲག་ལ་སོགས་པ་བྱུང་བ་མེར་མེར་པོ་དང༌[^1960]ནུར་ནུར་པོ་ལ་སོགས་པའི་མཚན་ཉིད་དོ་ཞེས་སྔོན་ཇི་ལྟར་གྱུར་པ་ལ་རྟོག༌[^1961]པའོ། །

[Block 2252]
ལུས་ཀྱི་ཕྱི་མའི་མཐའ་ནི་རྒ་བ་དང་འཆི་བ་སྟེ། ལུས་འདི་མཐར་རྒས་ཤིང༌[^1962]འཆི་བ་དང་། ཀེང་རུས་ལ་སོགས་པར་འགྱུར་རོ་ཞེས་རྟོག་པའོ། །

[Block 2253]
ལུས་ཀྱི་ད་ལྟར༌[^1963]བྱུང་བ་ནི་ད་ལྟར་དངོས་སུ་གནས་པའི་ལུས་ཏེ། དེ་ལ༌[^1964]ཡང་བཀྲུ་བ་དང་མཉེ་བ་དང་བཟའ་བ་དང་། བགོ་བ་ལ་སོགས་པས་བསྐྱང་དགོས་སོ་ཞེས་རྟོག་པའོ། །

[Block 2254 [HEADING]]
###### དུས་གསུམ་གྱི་ལུས་ལ་རྟོག་པ། ^8-1-1-5-1-0

[Block 2255]
དུས་གསུམ་གྱི་ལུས་ལ་རྟོག་པ་དེ་ཉིད༌[^1965]དོན་རྒྱས་པར་བསྟན་པའི་ཕྱིར། ཀྱེ་མ་ལུས་འདི་ནི་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུང་སྟེ།[^1966] དེ་ཡང་དབུགས་དབྱུང་དུ་མེད་པ་དང་། ལས་དང་ཉོན་མོངས་པ་ལས་བྱུང་བ་དང་། གང་ཟག་གི་དངོས་པོ་མེད་པ་དང་། ཆོས་ཀྱི་དངོས་པོ་མེད་པ་དང་། དཔེ་དང་བཅས་བས་བསྟན་ཏོ། །

[Block 2256 [HEADING]]
###### **དབུགས་དབྱུང་དུ་མེད་པ།** ^8-1-1-5-1-1-0

[Block 2257]
དེ་ལ་ཀྱེ་མ་ཞེས་བྱ་བས། དབུགས་དབྱུང་དུ་མེད་པ་བསྟན་ཏེ། ལུས་འདི་སྡུག་བསྔལ་རྣམ་པ་སྣ་ཚོགས་ཀྱི་འབྱུང་གནས་ཡིད་ལ་སྡུག་བསྔལ་བར་གྱུར་ན་ཡང་དེ་ལས་བཟློག་པའི༌[^1967]སྐབས་མེད་པས། ཀྱེ་མའོ་ཞེས་གསུངས་ཏེ། དེ་ནི་ཡི་ཆད་པ་དང་མི་དགའ་བའི་ཚིག་གོ། །

[Block 2258 [HEADING]]
###### **ལས་དང་ཉོན་མོངས་པ་ལས་བྱུང་བ།** ^8-1-1-5-1-2-0

[Block 2259]
ཕྱིན་ཅི༌[^1968]ལོག༌[^1969]ལས་བྱུང་ཞེས་བྱ་བ་ལས་དང་ཉོན་མོངས་པ་ལས་བྱུང་བ་བསྟན་ཏེ། ལྟ་བ་ཕྱིན་ཅི་ལོག་དང་། འདུ་ཤེས་ཕྱིན་ཅི་ལོག༌[^1970]དང་། སེམས་ཕྱིན་ཅི་ལོག་ལས་བྱུང་བ་དང་། ལས་དང་ཉོན་མོངས་པའི་རྒྱུ་དང་རྐྱེན་གྱིས་བསྐྱེད་པའོ། །

[Block 2260 [HEADING]]
###### **གང་ཟག་གི་དངོས་པོ་མེད་པ།** ^8-1-1-5-1-3-0

[Block 2261]
ཚོར་བ་མེད་པ་དང་། [^1971]བྱེད་པ་མེད་པ་ཞེས་བྱ་བ་ལ་སོགས་པས་གང་ཟག་གི་དངོས་པོ་མེད་པ་བསྟན་ཏེ། ལུས་དེའི་ནང་དུ་ན༌[^1972]མུ་སྟེགས་ཅན་དག་གིས་བཏགས་པའི་བདག་མེད་པའི་ཕྱིར་རོ། །

[Block 2262 [HEADING]]
###### **ཆོས་ཀྱི་དངོས་པོ་མེད་པ།** ^8-1-1-5-1-4-0

[Block 2263]
རྒྱུ་དང་རྐྱེན་རྣམས་ཀྱིས་བྱུང་བ་སྟེ་ཞེས་བྱ་བས་ཆོས་ཀྱི་དངོས་པོ་མེད་པ་བསྟན་ཏེ། ལུས་ཉིད་ཀྱང་སྒྱུ་མ་བཞིན་དུ་རྒྱུ་རྐྱེན་གྱི་མཐུ་ལས་བྱུང་ནས་རྨི་ལམ་ན་སྣང་བ་ཙམ་དུ་སྣང་བར་ཟད་ཀྱི་ཡོད་པ་མ་ཡིན་ཞེས་རྟོག་པར༌[^1973]སྦྱར་རོ། །

[Block 2264 [HEADING]]
###### **དཔེ།** ^8-1-1-5-1-5-0

[Block 2265]
འདི་ལྟ་སྟེ་དཔེར་ན་ཕྱི་རོལ་གྱི་ཞེས་བྱ་བ་ལ་སོགས་པས་དཔེ་བསྟན་ཏེ། ཕྱི་རོལ་གྱི་དངོས་པོ་ལ་སོགས་པ་འང་རྒྱུ༌[^1974]རྐྱེན་ལས་བྱུང་ཞིང་བདག་དང་བྱེད་པ་པོ་མེད་པའོ། །

[Block 2266]
དེ་བཞིན་དུ་ཞེས་བྱ་བ་ནི་དེ་དང་འདྲ་བར་ཞེས་བྱ་བའི་ཐ་ཚིག་སྟེ༌[^1975]རྒྱུ་རྐྱེན་ལས་བྱུང་བ་དང་བདག་དང་བྱེད་པ་པོ་མེད་པར་འདྲ་བའོ། །

[Block 2267]
ཡོངས་སུ་བཟུང་བ་ཞེས་བྱ་བ་ནི་ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད་ཀྱི་མཚན་ཉིད་ཙམ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2268]
མི་གཡོ་བ་འམ། མི་གནོད་པ་འམ། མི་འགྱུར་བའི་ཆོས་ཅན་གྱིས་སྟོང་སྟེ་ཞེས་བྱ་བ་ནི་མུ་སྟེགས་ཅན་གྱི་བདག་མི་གཡོ་མི་གནོད་མི་འགྱུར་ཞེས་བྱ་བ་དེ་ལྟ་བུའི༌[^1976]དངོས་པོ་མེད་པའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2269]
ཡང་ན་རྟག་པ་དང་བརྟན་པ༌[^1977]ལ་སོགས་པ་ནི་བདག་ཏུ་བཏགས་པའི༌[^1978]མཚན་ཉིད་དེ།[^1979] ལུས་དེ་ལྟ་བུའི་མཚན་ཉིད་མ་ཡིན་པས་ན༌[^1980]ཆོས་ཅན་གྱིས་སྟོང་པའོ། །

[Block 2270]
དེ་ལ་རྟག་པ༌[^1981]ནི་མི་རྟག་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 2271]
བརྟན་པ་ནི་སྐད་ཅིག་མ་འཇོག་པ་མེད་པའི་ཕྱིར་ཏེ། [^1982]དུས་གཞན་ཡང་གནས་པའོ། །

[Block 2272]
ཐེར་ཟུག་ནི་རྒྱུད་འཇམ༌[^1983]མེད་པའི་ཕྱིར་རོ། །

[Block 2273]
མི་གཡོ་བ་ནི་ཕན་པའི་དངོས་པོས་ཕན་པར་གྱུར་པ་མེད་པའོ། །

[Block 2274]
མི་གནོད་པ་ནི་སྡུག་བསྔལ་གྱིས༌[^1984]གནོད་པ་མེད་པའོ། །

[Block 2275]
མི་འགྱུར་བའི་ཆོས་ཅན་ནི་མི་འདྲ་བ་དུ་མར་གྱུར་པ༌[^1985]མེད་པའོ། །

[Block 2276]
ཡང་ན་ནི་མི་གཡོ་བས་རྟག་པའོ། །

[Block 2277]
མི་འགྱུར་བས་ན་ཐེར་ཟུག་པའོ།[^1986] །ལུས་འདི་ལ་བདག་གིར༌[^1987]མི་བྱའོ་ཞེས་བྱ་བ་ལ་ལུས་འདི་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའ་ཉིད་ཀྱི་ལུས་ལ་བསྙེགས་སོ། །

[Block 2278]
བདག་གིར་མི་བྱ༌[^1988]ཞེས་བྱ་བ་ནི་ལུས་དེ་ལ་བདག་གི་དོན་དུ་མི་བྱའོ། །

[Block 2279]
ཡང་ན་ལུས་དེ་ལ་ཆགས་པར་མི་བྱའོ། །

[Block 2280]
ཡང་ན་ལུས་དེ་ལ་བདག་ཏུ་འཛིན་པར་མི་བྱ་སྟེ། འདི་ནི་ལུས་ཐམས་ཅད་དང་བྲལ་བར་གྱུར་པའོ། །
--- END BLOCKS ---
