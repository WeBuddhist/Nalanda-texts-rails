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
[Block 2206 [VERSE]]
དེ་ལས་ཆེ་ལོང་བསྡུས་ནས་ནི། །
དགེ་དང༌[^877]མི་དགེ་ཅི་རིགས་པར། །
ལས་ཀྱི་ལམ་ནི་བཅུར་གསུངས་སོ། །

[Block 2207]
དགེ་བ་རྣམས་ནི་ལེགས་པར་སྤྱད་པ་དག་ལས་སོ། །

[Block 2208]
མི་དགེ་བ་རྣམས་ནི་ཉེས་པར་སྤྱད་པ་དག་ལས་སོ། །

[Block 2209]
འདིར་ཉེས་པར་སྤྱད་པ་ཅི་ཞིག་དང་། ལེགས་པར་སྤྱད་པ་ཅི་ཞིག་མ་བསྡུས་ཤེ་ན། རེ་ཞིག་མི་དགེ་བ་རྣམས་ལས་ལུས་ཀྱི་ཉེས་པར་སྤྱད་པའི་ཕྱོགས་སྦྱོར་བ་དང་། མཇུག་དང་། ཉོན་མོངས་པ་ཅན་རྡེག་པ༌[^878]ལ་སོགས་པ་དང་། ཡིད་ཀྱི་ཉེས་པར་སྤྱད་པའི་ཕྱོགས་སེམས་པ་མ་བསྡུས་སོ། །

[Block 2210]
དགེ་བ༌[^879]ལ་ལུས་ཀྱི་ལེགས་པར་སྤྱད་པའི་ཕྱོགས་སྦྱོར་བ་དང་། མཇུག་དང་། མྱོས་པར་འགྱུར་བ་ལ་སོགས་པ་སྤོང་བ་དང་། སྦྱིན་པ་དང་། མཆོད་སྦྱིན་ལ་སོགས་པ་དང་། ངག་གི་ཉེས་པར་སྤྱད་པ་ཡང་སྙན་པར་སྨྲ་བ་ལ་སོགས་པ་དང་། ཡིད་ཀྱི་ལེགས་པར་སྤྱད་པའི་སེམས་པ་མ་བསྡུས་སོ། །

[Block 2211]
ལས་ཀྱི་ལམ་དེ་རྣམས་ལས།

[Block 2212]
[^880]མི་དགེ་དྲུག་ནི་རྣམ་རིག་མིན། །འདོད་པས་ལོག་པར་གཡེམས་པ༌[^881]ལས་གཞན་དྲུག་པོ་ནི་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པའི་རང་བཞིན་ནོ། །

[Block 2213]
གཞན་བྱེད་དུ་བཅུག་པ་ནའོ། །

[Block 2214]
གཅིག་རྣམས༌[^882]གཉིས་སོ། །

[Block 2215]
འདོད་པས་ལོག་པར་གཡེམས་པ༌[^883]ནི་རྟག་ཏུ་རྣམ་པར་རིག་བྱེད་དང་། རྣམ་པར་རིག་བྱེད་མ་ཡིན་པའི་རང་བཞིན་ཡིན་ཏེ། རང་ཉིད་ཀྱི་དེ་མཐར་ཐུག་པར་བྱས་པའི་ཕྱིར་རོ། །

[Block 2216]
དེ་དག་ཀྱང་བྱེད་ན། ལས་ཀྱི་ལམ་དྲུག་པོ་འདི་དག་ཀྱང་བདག་ཉིད་བྱེད་པ་ན་རྣམ་པ་གཉིས་ཏེ། རྣམ་པར་རིག་བྱེད་དང་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པའོ། །

[Block 2217]
དགེ་བ་བདུན་རྣམ་གཉིས། ཡང་དག་པར་བླངས་པའི་ཚུལ་ཁྲིམས་ནི་རྣམ་པར་རིག་བྱེད་ལ་རག་ལུས་པའི་ཕྱིར་རོ། །

[Block 2218]
ཏིང་འཛིན་ལས་སྐྱེས་རྣམ་རིག་མིན། །བསམ་གཏན་དང་ཟག་པ་མེད་པའི་སྡོམ་པས་བསྡུས་པ་ནི་སེམས་ཙལ་ལ་རག་ལུས་པའི་ཕྱིར་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པའོ། །

[Block 2219 [VERSE]]
ཉེར་བསྡོགས་རྣམས་ནི་རྣམ་རིག་བྱེད། །
རྣམ་རིག་བྱེད་མིན་འགྱུར་བའམ། །

[Block 2220]
མ་ཡིན། གལ་ཏེ་ཀུན་ནས་དཀྲིས་པ་དྲག་པོའམ། རབ་ཏུ་དང་བ་ལྷུར་ལེན་པ་ཆེན་པོས་སྦྱོར་བ་རྩོམ་ན་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པར་འགྱུར་གྱི་གཞན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 2221]
བཟློག་པ་མཇུག་ཡིན་ནོ། །

[Block 2222]
དེ་དག་ནི་གདོན་མི་ཟ་བར་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པའི་རང་བཞིན་ནི་ཡིན་ནོ། །

[Block 2223]
རྣམ་པར་རིག་བྱེད་དུ་ནི་འགྱུར་བའམ། ཡང་ན་མ་ཡིན་ཏེ། གལ་ཏེ་ལས་ཀྱི་ལམ་བྱས་ནས་ཡང་དེའི་རྗེས་སུ་མཐུན་པའི་ཆོས་སྤྱོད་ན་ནི་རྣམ་པར་རིག་བྱེད་དུ་འགྱུར་གྱི་གཞན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 2224]
མདོ་ལས།

[Block 2225 [HEADING]]
##### ལས་ཀྱི་ལམ་རྩ་གསུམ་ལས་སྐྱེས་པ། ^4-3-9-1-0

[Block 2226]
སྲོག་གཅོད་པ་ནི་ཆགས་པ་ལས་སྐྱེས་པ་དང་། ཞེ་སྡང་ལས་སྐྱེས་པ་དང་། གཏི་མུག་ལས་སྐྱེས་པའོ་ཞེས་བྱ་བ་ནས་ལོག་པར་ལྟ་བའི་བར་དུ་གསུངས་པ་དེ་ནི། སྦྱོར་བ༌[^884]རྩ་བ་གསུམ་ལས་སྐྱེས། །དེ་ལ་སྲོག་གཅོད་པ་ཆགས་པ་ལས་སྐྱེས་པའི་སྦྱོར་བ་ནི་འདི་ལྟ་སྟེ། དེའི་ལས་ཀྱི་ཡན་ལག་གི་ཕྱིར་རམ། ནོར་གྱི་ཕྱིར་རམ་རྩེ་མོ༌[^885]ལ་སོགས་པའི་ཕྱིར་སྦྱོར་ནའོ། །

[Block 2227]
ཞེ་སྡང་ལས་སྐྱེས་པ་ནི་འདི་ལྟ་སྟེ། ཁོ་ན་ལས་ངེས་པར་འབྱུང་བར་བྱ༌[^886]བའི་ཕྱིར་གསོད་པར༌[^887]བྱེད་པའོ། །

[Block 2228]
གཏི་མུག་ལས་སྐྱེས་པ་ནི་འདི་ལྟ་སྟེ་མཆོད་སྦྱིན་བྱེད་པ་ལ་སོགས་པའི་དོན་དུའོ། །

[Block 2229]
མ་བྱིན་པར་ལེན་པ་ཆགས་པ་ལས་སྐྱེས་པའི་སྦྱོར་བ་ནི་གང་ཞིག་གང་དོན་དུ་གཉེར་བ་དེས་དེ་འཕྲོག་པའམ། གཞན་གྱི་རྙེད་པའམ། བཀུར་སྟིའམ་གྲགས་པའི་ཕྱིར་རམ། བདག་གམ་མཛའ་བོ༌[^888]ཡོངས་སུ་བསྐྱབ་པའི་ཕྱིར་འཕྲོག་པའོ། །

[Block 2230]
ཞེ་སྡང་ལས་སྐྱེས་པ་ནི་ཁོན་ལས༌[^889]ངེས་པར་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 2231]
གཏི་མུག་ལས་སྐྱེས་པ་ནི་འདི་ལྟ་སྟེ། རྒྱལ་པོས་ཆོས་འདོན་པ་པོ་ཚད་མར་བྱས་ནས་སམ། མི་བགྲུངས་པ་ཆད་པས་བཅད་པའི་ཕྱིར་ཆོས་ཀྱི་བློས་འཕྲོག་པའོ། །

[Block 2232]
འདོད་པས་ལོག་པར་གཡེམ་པ་ཆགས་པ་ལས་སྐྱེས་པའི་སྦྱོར་བ་ནི་གཞན་གྱི་ཆུང་མ་ལ་སོགས་པ་ལ་ཆགས་པས་སམ། རྙེད་པ་དང་བཀུར་སྟི་ལ་སོགས་པའི༌[^890]ཕྱིར་མི་ཚངས་པར་སྤྱོད་པའོ། །

[Block 2233]
ཞེ་སྡང་ལས་སྐྱེས་པ་ནི་ཁོན༌[^891]ལས་ངེས་པར་འབྱུང་བར་བྱ་བའི་ཕྱིར་རོ། །

[Block 2234]
གཏི་མུག་ལས་སྐྱེས་པ་ནི་འདི་ལྟ་སྟེ། པར་སིག་པ་རྣམས་མ་ལ་སོགས་པ་ལ་བགྲོད་པའོ། །

[Block 2235]
བརྫུན་དུ་སྨྲ་བ་ལ་སོགས་པ་ཆགས་པ་ལས་སྐྱེས་པ་དང་ཞེ་སྡང་ལས་སྐྱེས་པ་སྔ་མ་བཞིན་ནོ། །

[Block 2236]
གཏི་མུག་ལས་སྐྱེས་པ་རྣམས་ནི་ཕལ་ཆེར་ལོག་པར་ལྟ་བས་རབ་ཏུ་བཅུག་པའོ། །

[Block 2237 [VERSE]]
དེ་ཡི་མཇུག་ཐོགས་ལས་བྱུང་ཕྱིར། །
བརྣབ་སེམས་སོགས་རྩ་གསུམ་ལས་སྐྱེས། །

[Block 2238]
ཆགས་པའི་མཇུག་ཐོགས་སུ་བྱུང་བ་ནི་ཆགས་པ་ལས་སྐྱེས་པ་རྣམས་སོ། །

[Block 2239]
མི་དགེ་བ་རྣམས་བཤད་ཟིན་ཏོ། །

[Block 2240 [VERSE]]
དགེ་བ་སྦྱོར་དང་མཇུག་བཅས་རྣམས། །
ཆགས་སྡང་གཏི་མུག་མེད་ལས་སྐྱེས། །

[Block 2241]
དགེ་བའི་སེམས་ཀྱིས་ཀུན་ནས་བསླང་བའི་ཕྱིར་དང་། དེ་ཡང་གདོན་མི་ཟ་བར་མ་ཆགས་པ་ལ་སོགས་པ་དང་མཚུངས་པར་ལྡན་པའི་ཕྱིར་དགེ་བ་ཐམས་ཅད་རྩ་བ་གསུམ་ལས་སྐྱེས་པ་ཡིན་ནོ། །

[Block 2242]
དེ་མི་དགེ་བའི་ལས་ཀྱི་ལམ་གྱི་སྦྱོར་བ་སྤོང་བ་ནི་དགེ་བའི་ལས་ཀྱི་ལམ་གྱི་སྦྱོར་བ་ཡིན་ནོ། །

[Block 2243]
དངོས་སྤོང་བ་ནི་དངོས་ཡིན་ནོ། །

[Block 2244]
མཇུག་སྤོང་བ་ནི་མཇུག་ཡིན་ནོ། །

[Block 2245]
སྡོམ་པ་ལེན་པ་ན་ཡང་སྦྱོར་བ་དང་དངོས་དང་མཇུག་རྣམས་སྦྱར་བར་བྱའོ། །
--- END BLOCKS ---
