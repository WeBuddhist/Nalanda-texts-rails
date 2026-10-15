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
[Block 2171]
གསོལ་བ་དང་གཉིས་ཀྱི་ལས་ནི་བཞི་བཅུ་རྩ་བདུན་ནོ། །

[Block 2172]
གསོལ་བ་དང་བཞིའི་ལས་ནི་སུམ་ཅུའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2173]
ལས་ཀྱི་གཞི་ཉིད་ལས་དབྱེ་བའི་ཚད་དེ་ལྟ་བུ་རྣམས་ལ༌[^1965]ལས་རྣམ་པར་གཞག་པའི་སྐབས་སུ་ངོ་བོ་ཉིད་བརྗོད་པ་ཡིན་ནོ། །

[Block 2174]
དེའི་ཕྱིར།

[Block 2175 [VERSE]]
གསང་དང་ནང་དུ་དྲི་ཕྱིར་དང་། །
གསོ་སྦྱོང་དེ་ལ་ལྟུང་བཅས་དང་། །
དེ་ལ༌[^1966]དགེ་འདུན་ཡིད་གཉིས་དང་། །
རྩོད་དང་ངེས་ཉིད་མ་ཡིན༌[^1967]དང་། །

[Block 2176]
དེ་ཡི་དོན་དུ་ལྔ་པོ་དག །ཐམས་ཅད་དགག་དབྱེར་གཏོགས་པ་ཡིན།[^1968] །

[Block 2177 [VERSE]]
དབྱེར་གནས༌[^1969]ཁས་བླངས༌[^1970]ཉིད་དང་ནི། །
ཤི་བའི་རྫས་དང་ནོར་འདྲ་དང་། །
ཆོས་གོས་སྲ་བརྐྱང་གཏད་པ༌[^1971]དང་། །
གནས་ངན་ལེན་ནི་བརྗོད་པ་དང་། །

[Block 2178 [VERSE]]
ཆོས་གོས་སྦྱིན་པར༌[^1972]བྱ་བ་དང་། །
གྲངས་སུ་གཞུག་པའི་གཞི༌[^1973]དག་དང་། །
ཁྱིམ་གྱི་སྡོམ་དང་དེ་གཞིག་དང་། །
ལྷུང་བཟེད་ཁ་སྦུབ་བྱ་བ་དང་། །

[Block 2179 [VERSE]]
དེ་ཉིད་བཟློག་པར་བྱ་བ་དང་། །
གསོལ་བ་འབའ་ཞིག་ལས་ཡིན་ནོ། །
གནས་དང་མཚམས་ཀྱི་གཉིས་པོ་དང་། །
མི་འབྲལ་མྱོས༌[^1974]དང་དགག་དབྱེ་དང་། །

[Block 2180 [VERSE]]
གནས་མལ་སྟོབས་པར་བྱེད་པ་དང་། །
རུང་བའི་ས་གཞི་བསྐོ་བ་དང་།
སྲ་བརྐྱང་དང་ནི་དེ་གདིང་དང་། །
སྤོང་དང་ལག་གི་བླ་དང་ནི། །

[Block 2181]
གནས་ཁང་བསྐོ་ལ་སོགས་པ་དག །གཟུ་དང་གསོལ༌[^1975]དང་སྦེད་པ་དང་། ཚུལ་ཤིང་འདྲིམ་པར་བྱེད་པ་དང་།

[Block 2182 [VERSE]]
ཁང་པ་ཁང་ཆེན་བསྟན་པ་དང་། །
གླེང་དང་འབྲལ་བར་མི་འགྱུར་དང་། །
སྟན་དང་ལྷུང་བཟེད་འདྲིམ་པ་དང་། །
མ་དད་གོ་བར་བྱ་བ་དང་། །

[Block 2183 [VERSE]]
སྟོན་པ་དང་ནི་ནགས་ཉུལ་དང་། །
ཕྱག་མི་བྱ་དང་མང་ཕྱིར་དང་། །
ཁར་བ༌[^1976]དྲ་བའི༌[^1977]ཕྱིར་དང་ནི། །
རྙེད་པ་གཅིག་ཏུ་བྱ་ཕྱིར་དང་། །

[Block 2184 [VERSE]]
བསླབ་པ་སྦྱིན་དང་ཉེར༌[^1978]གནས་དང་། །
བུ་དང་ཉེ་དུའི་ཕྱིར་འགྲོ་བ། །
གསོལ་དང་གཉིས་ཀྱི་ལས་ཡིན་ནོ། །

[Block 2185]
བསྙེན་པར་རྫོགས་པར་བྱ་བ་དང་།

[Block 2186 [VERSE]]
མུ་སྟེགས་གནས་དང་མཚམས་དགྲོལ་དང་། །
མཐུན་སྦྱིན་གསོ་སྦྱོང་བདུན་པོ་དང་།
བརྒྱད་དང་དྲན་དང་མ་མྱོས་དང་། །
དེ་ཉིད་ཚོལ༌[^1979]དུ་གཞུག་པ་དང་། །

[Block 2187 [VERSE]]
བགོ་བར་བྱ་བ་བརྒྱད་དང་ནི། །
ཉམས་པ་སྦྱིན་པར་བྱ་བ་ནི། །
གསོལ་དང་བཞི་ཡི༌[^1980]ལས་ཡིན་ནོ། །

[Block 2188]
ད་ནི་བསྡུ་བའི་ཚིགས་སུ་བཅད་པ་དེ་དག་བཤད་པར་བྱ་སྟེ། དེ་ལ། གསང་དང་ནང་དུ་དྲི་ཕྱིར་དང་། །ཞེས་བྱ་བ་ལ་དེ་ལ་གསང་སྟེ་དྲི་བའི༌[^1981]ཕྱིར་ཞེས་བྱ་བ་ནི་གསང་སྟེ་སྟོན་པས་བར་ཆད་ཀྱི་ཆོས་རྣམས་གསང་སྟེ་དྲི་བའི༌[^1982]ཕྱིར། གསོལ་བ༌[^1983]འབའ་ཞིག་གི་ལས་བྱའོ། །

[Block 2189]
ནང་དུ་དྲི་བའི༌[^1984]ཕྱིར་ཞེས་བྱ་བ་ནི་ལས་བྱེད་པས་བར་ཆད་ཀྱི་ཆོས་རྣམས་དགེ་འདུན་གྱི་ནང་དུ་དྲི་བའི༌[^1985]ཕྱིར་གསོལ་བ་འབའ་ཞིག་གི་ལས་སོ། །

[Block 2190]
གསོ་སྦྱོང་ཞེས་བྱ་བ་ནི་སོ་སོར་ཐར་པའི་མདོ་འདོན་པའི་ཕྱིར་གསོལ་བ་འབའ་ཞིག་གི་ལས་བྱ་བའོ། །

[Block 2191]
དེ་ལ་ཞེས་བྱ་བ་ནི་གསོ་སྦྱོང་དེ་ལའོ། །

[Block 2192]
དེ་ལ་ཅི་ཞེ་ན། དེའི་ཕྱིར་ལྟུང་བཅས་དང་ཞེས་བྱ་བ་སྨོས་ཏེ། ལྟུང་བ་ནི་ལྟུང་བ་ཞེས་བྱ་བ༌[^1986]བརྗོད་དོ། །

[Block 2193]
དགེ་འདུན་ཐམས་ཅད་ལྟུང་བ་དང་བཅས་པར་གྱུར་ན་གསོལ་བ་འབའ་ཞིག་གི་ལས་གྱིས་བྱིན་གྱིས་བརླབས་ཏེ་གསོ་སྦྱོང་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་ནི་འདི་ཡིན་ནོ། །

[Block 2194]
ཡིད་གཉིས་དང་ཞེས་བྱ་བ་ནི་དགེ་འདུན་ལའོ། །

[Block 2195]
དེ་ལ་ཞེས་བྱ་བ་ནི་ལྟུང་བ་དེ་ལའོ། །

[Block 2196]
རྩོད་དང་ངེས་ཉིད་མ་ཡིན་ཞེས་བྱ་བ་ནི་དེར་གཏོགས་པའི་རྩོད་པ་དང་མ་ངེས་པ༌[^1987]ཉིད་ལའོ། །

[Block 2197]
དེ་ཡི་དོན་དུ་ལྔ་པོ་དག །ཅེས༌[^1988]བྱ་བ་ནི་གསོ་སྦྱོང་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ལ་གསོ་སྦྱོང་གསུངས་པས་དགག་དབྱེ་ལ་སྦྱར་རོ། །

[Block 2198]
ཤི་བའི་རྫས་དང་ཞེས་བྱ་བ་ནི་ཤི་བ་དང་འབྲེལ་པའི་རྫས་བགོ་བ་ལའོ། །

[Block 2199 [VERSE]]
ཆོས་གོས་སྲ་བརྐྱང་གཏད་པ༌[^1989]དང་། །
གནས་ངན་ལེན་ནི་བརྗོད་པ་དང་། །
ཆོས་གོས་སྦྱིན་པར་བྱ་བ་དང་། །

[Block 2200]
ཞེས་བྱ་བ་ནི་གལ་ཏེ་གཏན་པ་ཕུལ་ན་དེ་བས་ན་ཉེ་བར་སྦྱར་བའོ། །

[Block 2201]
གྲངས་སུ་གཞུག་པ་བཞི༌[^1990]དག་དང་། །ཞེས་བྱ་བ་ནི་ངོར་འཕྱ་བའི༌[^1991]གྲངས་སུ་གཞུག་པ་ལ་སོགས་པའོ། །

[Block 2202]
ཁྱིམ་གྱི་སྡོམ་དང་དེ་གཞིག༌[^1992]ཅེས་བྱ་བ་ནི་གང་ཞིག་ཅེས་བྱ་བ་འདའ༌[^1993]བྱེད་ཅིང་ལོངས་སྤྱོད་འགྲིབས་པ་ལས༌[^1994]དེ་གཞིག་པའོ། །

[Block 2203 [VERSE]]
ལྷུང་བཟེད་ཁ་སྦུབ་བྱ་བ་དང་། །
དེ་ཉིད་བཟློག་པར་བྱ་བ་དག །
གསོལ་བ་འབའ་ཞིག་ལས་ཡིན་ནོ། །

[Block 2204]
ཞེས་བྱ་བ་ནི་ལས་ཉི་ཤུ་རྩ་བཞི་པོ་གསུངས་པ་རྣམས་ལའོ། །

[Block 2205]
གནས་དང་ཞེས་བྱ་བ་ནི། གསོ་སྦྱོང་གི་གནས་ལ་གསོལ་བ་དང་། གཉིས་ཀྱི་ལས་ཀྱིས་བསྐོ་བའོ། །

[Block 2206]
མཚམས་གཉིས་པོ་དང་ཞེས་བྱ་བ་ནི། མཚམས་ཆེན་པོ་དང་། དཀྱིལ་འཁོར་བའི་མཚམས་བསྐོ་བའོ། །

[Block 2207]
མ་འབྲེལ་ཞེས་བྱ་བ་ནི་མཚམས་ཆེན་པོ་བཅད་པའི༌[^1995]ནང་དུ་གསོལ་བ་དང་། གཉིས་ཀྱི་ལས་ཀྱིས་ཆོས་གོས་དང་འབྲལ་བར་མི་འགྱུར་བའི་བསྐོ་བའོ། །

[Block 2208]
སྨྱོས་དང་ཞེས་བྱ་བ་ནི་མི་འབྲལ་བར་བསྐོ་བ་དང་། མྱོས་པའི༌[^1996]བསྐོ་བ་དང་། དགག་དབྱེ་བསྐོ་བ་དང་། གནས་མལ་སྟོབས་པར༌[^1997]བྱེད་པ་བསྐོ་བའོ། །

[Block 2209]
རུང་བའི་ས་གཞི་ཞེས་བྱ་བ་ནི་རུང་བའི་ཁང་པ་གསོལ་བ་དང་། གཉིས་ཀྱི་ལས་ཀྱིས་བསྐོ་བའོ། །

[Block 2210]
གཏན་པ་དང་ནི་ཞེས་བྱ་བ་གསོལ་བ་དང་གཉིས་ཀྱི་ལས་ཀྱིས་བསྐོ་བའོ། །
--- END BLOCKS ---
