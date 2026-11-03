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
[Block 2241]
བརྒྱད་དང་ཞེས་བྱ་བ་ནི་སྤོ་བ་དང་མགུ་བར་བྱ་བ་དང་། གཞི་ནས་སྤོ་བ་དང་། གཞི་ནས་མགུ་བར་བྱ་བ་དང་། ཡང་གཞི་ནས་སྤོ་བ་སྦྱིན་པ་དང་། ཡང་གཞི༌[^2009]ནས་མགུ་བ་སྦྱིན་པ་དང་། སྲ་བརྐྱང་དབྱུང་བ་དང་ལྷག་མ་ལས་དབྱུང་བ་དག་ལ་གསོལ་བ་དང་། བཞིའི་ལས་བྱ་བ་དང་། བརྒྱད་སོ་སོར་བགྲང་ངོ་། །དྲན་དང་མི༌[^2010]མྱོས་དང་། དེ་ཉིད་ཚོལ༌[^2011]དུ་གཞུག་པ་དང་། །ཞེས་བྱ་བ་ནི་དྲན་པས༌[^2012]འདུལ་བར་འོས་པ་དང་། མ་མྱོས་པས༌[^2013]འདུལ་བར་འོས་པ་དང་། དེའི་ངོ་བོ་ཉིད་ཚོལ་དུ་གཞུག་པ་གསུམ་བསྡུས་པའོ། །

[Block 2242]
བསྐོ་བར༌[^2014]བྱ་བ་རྣམས་དང་ནི། །ཞེས་བྱ་བ་ནི་བཟློག་པའི་ཕྱིར་བསྒོ་བར་བྱ་བ་བཅུ་གཅིག་པོ་དག་གསུངས་ཏེ་དེ་ལ་དྲུག་ནི་དགེ་སློང༌[^2015]གི་རྣམ་པར་འབྱེད་པ་ལས་སྨོས་ཏེ། དགེ་འདུན་གྱི་དབྱེན་བྱེད་པ་ལ་སོགས་པ་རྣམས་སོ། །

[Block 2243]
གཉིས་ནི་དགེ་སློང་མའི་རྣམ་པར་འབྱེད་པ་ལས་ཐུན་མོང་མ་ཡིན་པར༌[^2016]གསུངས་ཏེ། ཕམ་པར་འགྱུར་བའི་སྐབས་ནས་གནས་ནས་དབྱུང་བའི་རྗེས་སུ་ཕྱོགས་པ་གཅིག་གོ། །

[Block 2244]
དགེ་འདུན་ལྷག་མའི་སྐབས་ནས་བཞི་བསྟན་ཏེ། སྡེ་ཚན་གཅིག་གོ། །

[Block 2245]
ཉམས་པ༌[^2017]སྦྱིན་པར་བྱ་བའི་བསླབ་པ་སྦྱིན་པའོ། །

[Block 2246]
གསོལ༌[^2018]དང་བཞི་ཡི༌[^2019]ལས་ཡིན་ནོ། །ཞེས་བྱ་བ་ནི་ལས་སུམ་ཅུ་པོ༌[^2020]ཇི་སྐད་བསྟན་པ་དེ་རྣམས་ནི་གསོལ་བ་དང་བཞིའི་ལས་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ནོ།[^2021] །ལྷག་པོར་མ་གཏོགས་པ་རང་གི་དོན་གྱི་སྔགས་བརྗོད་པ་ཡང་ངོ་ཞེས་བྱ་བ་ལ་རང་གི་དོན་ནི་བདག་གི་དོན་ཏེ།[^2022] སྔགས་བརྗོད་པ་ནི་སྔགས་གཞན་བརྗོད་པ་གང་ཡིན་པ་དེ་ཡང་ལན་གསུམ་བརྗོད་པར་བྱ་བ་ཁོ་ནའོ། །

[Block 2247]
འདི་ལྟ་སྟེ་འཁར་བ་དང་དྲ་བ༌[^2023]ལ་སོགས་པ་གསོལ་བ་གང་དག་ཡིན་པ་དང་། ཆོས་གོས་ལ་སོགས་པ༌[^2024]རྫས་གཞན་དང་། གསོ་སྦྱོང་དང་དགག་དབྱེ་དག་དང་གནས་པར་ཁས་བླངས་པ་དང་། མཚམས་ཀྱི་ཕྱི་རོལ་དུ་མི་འབྲལ་བར་བྱ་བའི་ཕྱིར་ཞག་གཅིག་ལ་སོགས་པ་བྱིན་གྱིས་བརླབ་པ་དང་། སྐྱབས་སུ་འགྲོ་བ་དང་། རབ་ཏུ་བྱུང་བ་དང་། སྡོམ་པ་མནོད་པ་གང་དག་ཡིན་པ་དང་། ལྟུང་བ་བཤགས་པ་དང་། འདུན་པ་དང་། ཡོངས་སུ་དག་པ་དབུལ་བ་དང་། དགག་དབྱེ་དག་པ་དབུལ་བ་ལའོ། །

[Block 2248]
གཞན་གྱི་དོན་དུ་གང་ཟག་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་གཞན་གྱི་དོན་དུ་སྔགས་གང་ཟག་ལ་བརྗོད་པ་གང་ཡིན་པ་དེ་ཡང་ལན་གསུམ་ཁོ་ན་བརྗོད་པར་བྱ་བའོ། །

[Block 2249]
འདི་ལྟ་སྟེ་འདུན་པ་དང་ཡོངས་སུ་དག་པ་དང་། དགག་དབྱེ་བརྗོད་པ་དག་དགེ་སློང་ལ་བརྗོད་པའི་ཕྱོགས་ལ་ནི་ལན་གསུམ་བརྗོད་པར་བྱའོ། །

[Block 2250]
དགེ་འདུན་ལ་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བའི་ཕྱོགས་ལ་ནི་ལན་ཅིག༌[^2025]བརྗོད་པར་བྱ་སྟེ། གང་ཟག་ལ་ཞེས་སྨོས་པའི་ཕྱིར་རོ། །

[Block 2251]
ལྷག་པོར་ཡང་མདུན་དུ་ཙོག་པུར་འདུག་སྟེའོ་ཞེས་བྱ་བ་ནི་གང་ཟག་འདི་གང་ཟག་ལ་ཡང་ངོ་ཞེས་བྱ་བ་སྨོས་པས་སོ། །

[Block 2252]
གང་ཡང་རང་གི་དོན་ལ་ཞེས་བྱ་བ་དགེ་འདུན་ཙམ་ཉིད་དང་། འདི་ལས་གཞན་རྣམ་པ་གཉིས་ལ་ཡང་དེ༌[^2026]བྱེད་པའོ། །

[Block 2253]
ལྷག་པོར་བྱ་བའི་སྔགས་བརྗོད་པ་གང་ཡིན་པ་དེ་ཡང་གང་ཟག་གི་མདུན་དུ་ཙོག་པུར་འདུག་སྟེ་བརྗོད་པར་བྱ་བ་གཞན་གྱིས་ནི་མ་ཡིན་ནོ། །

[Block 2254]
ཞུ་བ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་འདིར་རབ་ཏུ་དབྱུང་ངམ༌[^2027]ཞེས་དགེ་སློང་གི་དགེ་འདུན་ལ་ཞུ་བར་བྱེད་པ་ན། རབ་ཏུ་དབྱུང་བར་འདོད་པའི་དགེ་བསྙེན་དེས་ཀྱང་རྒན་པའི་མཐའ་ལོགས་སུ་ཙོག་པུར་འདུག་པར་བྱ་བ་སྟེ། གང་ཞིག་དགེ་འདུན་ལ་ཞེས་བྱ་བ་འདི་ལས་རྒན་པའི་མཐའ་ལོགས་སུ་ཞེས་བྱ་བ་རྟོགས་པའོ། །

[Block 2255]
བསྙེན་པར་རྫོགས་པར་བྱེད་ན་གསང་སྟེ་སྟོན་པ་མ་གཏོགས་པ་ཕ་གུ་ལ་རྟིང་པ་གཉིས་ཀྱིས་སོ་ཞེས་བྱ་བ་ནི་གསང་སྟེ་སྟོན་པ་མ་གཏོགས་པ་བསྙེན་པར་རྫོགས་པའི་ལས་བྱེད་པ་ན་མཁན་པོར་གསོལ་བ་དང་། ལས་ཀྱི༌[^2028]སློབ་དཔོན་གྱིས༌[^2029]བར་ཆད་དྲི་བ་མཉན་པ༌[^2030]དང་། དེའི་ལན་འདེབས་པ་དང་། བསྙེན་པར་རྫོགས་པར་བྱ་བ་ལ་སོགས་པའི་སྐབས་ཐམས་ཅད་དུ། བསྙེན་པར་རྫོགས་པར་བྱ་བའི་གང་ཟག་དེ༌[^2031]ཕ་གུའི་སྟེང་དུ་རྟིང་པ་ཉིད༌[^2032]ཀྱིས་འདུག་ཏུ་གཞུག་གོ། །

[Block 2256]
ཆོས་གོས་དང་ལྷུང་བཟེད་བྱིན་གྱིས་བརླབ་པ་ནི། སྔར་བྱས་ཟིན་པས་དེ་ལ་ནི་ཆོ་ག་འདི་ཐལ་བར་མི་འགྱུར་ཏེ། རྫས་བྱིན་གྱིས་བརླབ་པ་ལ་སོགས་པས་གནོད༌[^2033]པའོ། །

[Block 2257]
འདིར་ཕ་གུ་ཞེས་བྱ་བ་ནི་དྲང་སྲོང་གི་རྗེས་སུ་འབྲངས་ནས་སྨོས་པའོ། །

[Block 2258]
དེ་ལྟར་འདི་ནི་དྲང་སྲོང་གི་ལུང༌[^2034]ལས་འབྱུང་བ་སྟེ། བོང་བའི་རིགས་ཀྱིས༌[^2035]དབང་དུ་བྱས་ནས་དེའོ། །

[Block 2259]
དུམ་བུ་ཡང་འདིས༌[^2036]རྗེས༌[^2037]བསྙེགས་པའོ། །

[Block 2260]
བུད་མེད་ནི་སྟན་ནང་ཚངས་ཅན་ལ་སོགས་པའོ་ཞེས་བྱ་བ་ནི་བུད་མེད་བསྙེན་པར་རྫོགས་པར་བྱེད་པ་ན་གསང་སྟེ་བསྟན་པ་མ་གཏོགས་པས་གནས་སྐབས་ཇི་སྐད་བསྟན་པ་དེ་དག་ཏུ་སྟན་ནང་ཚངས་ཅན་ལ་སོགས་པ་བུད་མེད་ཅི་བདེར་འདུག་ཏུ་གཞུག་པ་ཡིན་གྱི་ཙོག་པུར་འདུག་ཏུ་ཡང་མི་བཞུག་གོ། །

[Block 2261]
སོགས་པ་ཞེས་སྨོས་པའི་སྒྲས་ནི་རྫས་འཇམ་པ་དང་སྤངས་པ༌[^2038]གཞན་དག་བསྡུའོ། །

[Block 2262]
གཞན་གཙོ་བོ་མ་ཡིན་པ་ཉིད་ལ་ནི་དགེ་འདུན་ལ་རྒན་པའི་མཐར་རོ་ཞེས་བྱ་བ་ནི་རང་གི་དོན་གྱི་སྔགས་དགེ་འདུན་ལ་བརྗོད་པ་ན། དགེ་འདུན་ལས་གཞན་གཙོ་བོ༌[^2039]མ་ཡིན་པ་ཉིད་ལ་ནི། དེ་ལ་དེ་བསྡུ་བའི་གཏོགས་པའི་གང་ཟག་ལ་ཅུང་ཟད་ཀྱང་རག་ལས་པ་མ་ཡིན་པ་དེ་ནི་རང་གི་དོན་གྱིས་སྔགས་བརྗོད་པའོ། །

[Block 2263]
རྒན་པའི་མཐའ་ལོགས་སུ་ཙོག་པུར་འདུག་སྟེ་བརྗོད་པར་བྱའོ། །

[Block 2264]
འདི་ལྟ་སྟེ། འཇུག་པའི་སྔགས་རྣམས་ལྟ་བུའོ། །

[Block 2265]
གཞན་གྱི་གནས་ལ་སོགས་པའི་ཚུལ་བརྗོད་པ་ལའོ། །

[Block 2266]
སྔགས་མ་བརྗོད་པའི་གང་ཟག་དག་གིས་གསོལ་བ་གཞན་ལ༌[^2040]མཉན་ཏེ་བརྗོད་པར་བྱ་བ་དེ་ནི་གང་ཟག་ལ་རག་ལས་པ་མ་ཡིན་པས་དེ་ནི་དེ་རྣམས་ཀྱི་མདུན་དུ་གཙོ་པུར༌[^2041]འདུག་སྟེ་བརྗོད་པར་བྱའོ། །

[Block 2267]
འདུན་པ་དང་ཡོངས་སུ་དག་པ་དང་། [^2042]དགག་དབྱེ་བརྗོད་པ་གང་ཟག་གི་ཕྱོགས་ལས་ཡན་ལག་གི་ངོ་བོར་འགྲོ་བ་ཉིད་ཀྱིས་དེ་ལ་རག་ལས་པ་ཡིན་པས་དེས་དེ་ཉིད་ཀྱི་མདུན་དུ་གཙོག་པུར་འདུག་སྟེ་བརྗོད་པར་བྱ་སྟེ། འདི་ནི་བསྙེན་པར་རྫོགས་པའི་སྐབས་སུ་གསུངས་མོད་ཀྱི་ཐམས་ཅད་ལ་ཡང་འདུན་པ་དང་ཡོངས་སུ་དག་པ་དང་འདྲ་བས་སྤྱིར༌[^2043]མདོར་བྱས་སོ། །

[Block 2268]
གཞན་གྱི་དོན་དུ་ནི་འགྲེང་སྟེ༌[^2044]འདུད་པ་དང་བཅས་པར་རོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་ལ་ཡང་གཞན་གྱི༌[^2045]དོན་དུ་བརྗོད་པ་གང་ཡིན་པ་དེ་ནི་རྒན་པའི་མཐར་འགྲེངས་ཏེ༌[^2046]འདུད་པ་དང་བཅས་པས་བརྗོད་པར་བྱ་སྟེ། འདི་ལྟ་སྟེ་ཞུ་བ་དག་དང་འདུན་པ་དང་ཡོངས་སུ་དག་པ་དང་། དགག་དབྱེ་བརྗོད་པ་དགེ་འདུན་གྱི་ཕྱོགས་ལ་བྱ་བ་དང་། དབྱར་གནས་པའི་དགེ་འདུན་གྱི་དགག་དབྱེ་མཛད་ལགས་སོ་ཞེས་བྱ་བ་དང་། ཁྲིམས་སུ་བྱ་བ་བཟང་པོ་བརྗོད་པ་དང་། རྩོད་པ་མི་སྐྱེད་པ༌[^2047]ཉིད་དང་། ཚུལ་ཤིང་གི༌[^2048]གྲངས་དང་གནས་མལ་ལས་ལོག་པར་ལོངས་མི་སྤྱོད་པར་བྱེད་པ་ཉིད་ནི་འབྲས་བུ་གོ་བར་བྱེད་པ་དག་གོ། །

[Block 2269]
ཁ་ཅིག་ལས་གསང་སྟེ་སྟོན་པ་ཉིད་ནི་ལམ་གྱི་དབུས་ནས་ཞེས༌[^2049]སོ་ཞེས་བྱ་བ་ནི་ལམ་གྱི་དབུས་ནས་གསང་སྟེ་སྟོན་པ༌[^2050]དགེ་འདུན་བཙུན་པ་རྣམས་གསན་དུ་གསོལ་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 2270]
ལམ་གྱི་དབུས་ན༌[^2051]གནས་པ་དེས་འདུད་པ་དང་བཅས་པས་ཞེས་བྱ་བ་ནི་འདོད་པ་གཅིག་གོ། །

[Block 2271]
གཞུང་ཁ་ཅིག་ལས་རྒན་པའི་མཐར་འགྲེངས་ཏེ༌[^2052]ཞེས་བྱ་བ་ནི་གཞན་དག་གོ། །

[Block 2272]
རྫས་བྱིན་གྱིས་བརླབ་པ་ཡང་ངོ་ཞེས་བྱ་བ་ལ། འགྲེངས་ཏེ༌[^2053]ཞེས་བྱ་བ་ནི་དེ་ཙམ་ལ་འདིར་འདོད་པས་འགྲེངས་ཏེ༌[^2054]བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2273]
མདུན་དུ་ཞེས་བྱ་བ་ནི་དེ་ཉིད་འདིར་ཤུགས་ཀྱིས་ཐོབ་པ་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 2274]
འདིར་གཞུང་ནི་སྨན་བྱིན༌[^2055]གྱིས་བརླབ༌[^2056]པ་ལས།

[Block 2275]
དགེ་སློང་གི་མདུན་དུ་འགྲེངས་ཏེ༌[^2057]འདི་སྐད་བརྗོད་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ཏེ། དེའི་རྗེས་སུ་འབྲང་བས༌[^2058]ཐམས་ཅད་ཀྱི་དབང་དུ་བྱས་པའི་ཕྱིར་མདོ་འདི་བྱས་སོ། །

[Block 2276]
ཕལ་ཆེ་བ་ལ་རབ་ཏུ་གྲགས་པ་ལ་བརྟེན་པའོ། །

[Block 2277]
དབྱུང་བར་བྱ་བ་ལ་ཡང་དེའི་རྗེས་སུ་འབྲངས་ནས་ཆོ་གའི་སྐྱོན་ཤེས་པར་བྱའོ། །

[Block 2278]
འགལ་བའི་ཟླ་ནི་བྱིན་གྱིས་བརླབས༌[^2059]པའམ། དབྱུང་བར་བྱ་བ་དག་གཞན་དུ་གནས་པས་མི་རིགས་སོ། །

[Block 2279]
དེ་ལྟ་བས་ན་གང་གི་མདུན་དུ་བྱིན་གྱིས་བརླབ་པའམ་དབྱུང་བར་བྱ་བ་དེ་ལ་ཡང་སྤྱོད་ལམ་དེ་ཁོ་ན་དང་འདྲའོ། །

[Block 2280]
འགྲེངས་ཏེ༌[^2060]འདུག་པ༌[^2061]རྣམས་ཀྱིས་དུས་སུའོ། །
--- END BLOCKS ---
