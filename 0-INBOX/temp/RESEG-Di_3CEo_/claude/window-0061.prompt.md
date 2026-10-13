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
[Block 2136]
མཐོང་བའི་ཆོས་ལ་མྱོང་བར་འགྱུར་བའི་ལས་ཞིང་གི་ཁྱད་པར་ལས་འགྱུར་རོ། །

[Block 2137]
བསམ་པའི་ཁྱད་པར་ལས་ཀྱང་ངོ་། །ཡང་། ས་དེའི་འདོད་ཆགས་གཏན་བྲལ་ཕྱིར། །ཡང་དགེ་བའམ་མི་དགེ་བའི་ལས་ས་གང་ཡིན་པ་དེ་ལས་གཏན་དུ་འདོད་ཆགས་དང་བྲལ་བ་ཡིན་པའི་ཕྱིར་དེ་མཐོང་བའི་ཆོས་ལ་མྱོང་བར་འགྱུར་རོ། །

[Block 2138]
ལས་ཇི་ལྟ་བུ་ཞིག་ཅེ༌[^843]ན། རྣམ་སྨིན་ངེས་པ་གང་ཡིན་པའོ། །

[Block 2139]
དེའི་ངེས་པ་འདི་ཡིན་ཏེ། གནས་སྐབས་ངེས་པའི་ཡང་མ་ཡིན་ལ་མ་ངེས་པའི་ཡང་མ་ཡིན་ནོ། །

[Block 2140]
གང་ངེས་པར་མྱོང་པའི་ཞིང་དེ་ཁོ་ན་ཅི་མཐོང་བའི་ཆོས་ལ་མྱོང་བ་ཡིན་ཞེ་ན། ཡིན་ཏེ། དེ་དང་གང་ཟག་ཁྱད་པར་ཅན་གཞན་ཡང་འདི་ལྟ་སྟེ།

[Block 2141 [VERSE]]
གང་དག་འགོག་བྱམས་ཉོན་མོངས་མེད། །
མཐོང་དང་དགྲ་བཅོམ་འབྲས་ལངས་པ། །
དེ་ལ་ཕན་གནོད་བྱས་པ་ཡིས།[^844] །
འབྲས་བུ་འཕྲལ་དུ་མྱོང་བར་འགྱུར། །

[Block 2142]
འགོག་པའི་སྙོམས་པར་འཇུག་པ་ལས་ལངས་པ་ནི་སྙོམས་པར་འཇུག་པ་མྱ་ངན་ལས་འདས་པ་དང་འདྲ་བའི་ཕྱིར་སེམས་མཆོག་ཏུ་ཞི་བ་འཐོབ་པོ། །ཉོན་མོངས་པ་མེད་པ་ལས་ལངས་པའི་རྒྱུ་ནི་སེམས་ཅན་ཚད་མེད་པ་ལ་ཉོན་མོངས་པ་མེད་པ་དང་ལྡན་པའི་ལྷག་པའི་བསམ་པ་དང་རྗེས་སུ་འབྲེལ་པ་དང་། ཤིན་ཏུ་གསལ་བའི་བསོད་ནམས་ཚད་མེད་པས་ཡོངས་སུ་བསྒོས་པ་དང་། རྗེས་སུ་འབྲེལ་པ་ཡིན་ནོ། །

[Block 2143]
བྱམས་པ་ལས་ལངས་པ་ཡང་དེ་དང་འདྲའོ། །

[Block 2144]
མཐོང་བའི་ལམ་ལས་ལངས་པའི་རྒྱུད་ནི་མཐོང་བས་སྤང་བར་བྱ་བ་མ་ལུས་པ་སྤངས་པའི་ཕྱིར་གནས་ཡོངས་སུ་གྱུར་པ་སར་པ་ཡིན་པས་དྲི་མ་མེད་པ་ཡིན་ནོ། །

[Block 2145]
དེ་བཞིན་དུ་དགྲ་བཅོམ་པའི་འབྲས་བུ་ལས་ལངས་པའི་རྒྱུད་ནི་བསྒོམ་པས༌[^845]སྤང་པར་བྱ་བ་མ་ལུས་པར་སྤངས་པས་སོ། །

[Block 2146]
རྣམ་པར་སྨིན་པའི་གཙོ་བོ་ནི་ཚོར་བ་ཡིན་པས་དེའི་ཕྱིར་འདི་དཔྱད་པར་བྱ་སྟེ།

[Block 2147 [VERSE]]
རྣམ་པར་རྟོག་པ་མེད་པ་ཡི། །
དགེ་བའི་ལས་ཀྱི་རྣམ་སྨིན་ནི། །
སེམས་ཀྱི་ཚོར་བ་ཁོ་ནར་འདོད། །

[Block 2148]
རྣམ་པར་རྟོག་པ་མེད་པའི་ལས་ནི་བསམ་གཏན་ཁྱད་པར་ཅན་ནས་སྲིད་པའི་རྩེ་མོའི༌[^846]བར་དག་ན་ཡོད་དེ། དགེ་བའི་ལས་རྣམ་པར་རྟོག་པ་མེད་པ་དེའི་རྣམ་པར་སྨིན་པ་ནི་སེམས་ཀྱི་ཚོར་བ་ཁོ་ན་ཡིན་ནོ། །

[Block 2149]
མི་དགེ་བའི་ནི་ལུས་ཀྱི་ཡི།[^847] །སེམས་ཀྱི་སྡུག་བསྔལ་གྱི་ཚོར་བ་ནི་ཡིད་མི་བདེ་བ་ཡིན་ཏེ། དེ་ཡང་རྣམ་པར་སྨིན་པ་མ་ཡིན་ནོ། །

[Block 2150]
དེའི་ཕྱིར་རྣམ་པར་སྨིན་པ་ནི་ལུས་ཀྱི་ཡིན་ནོ། །

[Block 2151]
འོ་ན་སེམས་ཅན་རྣམས་ཀྱི་སེམས་གཡེང་པར༌[^848]གྱུར་པ་གང་ཡིན་པ་དེ་ནི་སེམས་གང་ལ་ཞེ་ན། རྣམ་པར་རྟོག་པའི་ཕྱིར་ལྔ་དག་ལས་མ་ཡིན་ཏེ།

[Block 2152 [VERSE]]
གཡེངས༌[^849]པའི་སེམས་ནི་ཡིད་སེམས་ལ། །
དེ་ནི་ལས་ཀྱི་རྣམ་སྨིན་སྐྱེས། །

[Block 2153]
གང་ཞིག་གསང་སྔགས་ཀྱི་སྦྱོར་བ་ལ་སོགས་པས་ཕ་རོལ་པོའི་སེམས་གཡེང་པར༌[^850]བྱེད་པའི་ལས་དེའི་རྣམ་པར་སྨིན་པས་ཚེ་ཕྱི་མ་ལ༌[^851]སེམས་གཡེང་བར༌[^852]འགྱུར་རོ། །

[Block 2154]
སྐྲག་གནོད་མ་ཉམས་མྱ་ངན་གྱིས། །མི་མ་ཡིན་པ་ལ་སོགས་པའི་འཇིགས༌[^853]པས་སམ། ཁམས་མི་མཉམ་པས༌[^854]སམ། ཉེ་དུ་ཤི་བ་ལ་སོགས་པའི་མྱ་ངན་གྱིས༌[^855]སེམས་གཡེང༌[^856]བར་འགྱུར་རོ། །

[Block 2155]
གལ་ཏེ་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་གཡེང་བར༌[^857]འགྱུར་བ་སེམས་གཡེངས་པ་ཡང་ལས་ཀྱི་རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པ་ཡིན་ན་གོ། །

[Block 2156]
ཇི་ལྟར་སེམས་ཀྱི་ཚོར་བ་རྣམ་པར་སྨིན་པ་མ་ཡིན་པར་འགྱུར་ཞེ་ན། སེམས་དེ་ཉིད་རྣམ་པར་སྨིན་པ་ཡིན་ནོ༌[^858]ཞེས་མི་ཟེར་རོ། །

[Block 2157]
དེ་ལྟ་མོད་ཀྱི་འབྱུང་བ་ཆེན་པོ་རྣམས་འཁྲུགས་པ་གང་ཡིན་པ་དེ་རྣམ་པར་སྨིན་པ་ཡིན༌[^859]ལ། དེ་ལས་སྐྱེས་པས་དེའི་ཕྱིར་རྣམ་པར་སྨིན་པ་ཡིན་ནོ། །

[Block 2158]
སེམས་གཡེངས་པ་དེ་ཡང་། སྒྲ་མི་སྙན་མིན་འདོད་ལྡན་རྣམས། །སྒྲ་མི་སྙན་པ་མིན་པ་འདོད་པ་དང་ལྡན་པ་རྣམས་ནི་ལྷ་དག་གི་ནང་དུ་ཡང་ལྷ་སྨྱོན་པ་ཡོད་ན་མི་དང་ངན་སོང་རྣམས་ལྟ་སྨོས་ཀྱང་ཅི་དགོས། ཡང་གསུམ་སྟེ། ཡོན་པོ་དང་། སྐྱོན་དང་། སྙིགས་མ་དག་ཀྱང་གསུངས་ཏེ། དེ་ལ།

[Block 2159 [HEADING]]
#### གཡོ་སྐྱོན་སྙིགས་མ། ^4-3-4-0

[Block 2160 [VERSE]]
ཡོན་སྐྱོན་སྙིགས་མར་གསུངས་པ་ནི། །
གཡོ་དང་ཞེ་སྡང་འདོད་ཆགས་སྐྱེས། །

[Block 2161]
ལུས་ངག་ཡིད་ཀྱི་ལས་གཡོ་ལས་སྐྱེས་པ་ནི་ལུས་ལ་སོགས་པ་ཡོན་པོར་བཤད་དེ། གྱ་གྱུའི་རྒྱུ་ལས་བྱུང་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2162]
ལུས་ལ་སོགས་པའི་ལས་ཞེ་སྡང་ལས་སྐྱེས་པ་སྐྱོན་དུ་བཤད་དེ། སྡང་བའི་རྒྱུ་ལས་བྱུང་བའི་ཕྱིར་རོ། །

[Block 2163]
ལུས་ལ་སོགས་པའི་ལས་འདོད་ཆགས་ལས་སྐྱེས་པ་ནི༌[^860]སྙིགས་མར༌[^861]བཤད་དེ། ཆགས་པའི་རྒྱུ་ལས་བྱུང་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2164 [HEADING]]
#### དཀར་གནག་ལ་སོགས་ལས་རྣམ་པ་བཞི། ^4-3-5-0

[Block 2165 [VERSE]]
དཀར་གནག་ལ་སོགས་བྱེ་བྲག་གིས། །
ལས་ནི་རྣམ་པ་བཞི་ཡིན་ནོ། །

[Block 2166]
དེ་ལ།

[Block 2167 [VERSE]]
མི་དགེ་གཟུགས་དང་འདོད་གཏོགས་པའི། །
དགེ་བ་ཉིད་ནི་རིམ་བཞིན་དུ། །
གནག་དང་དཀར་དང་གཉིས་ཀའི་ལས། །
དེ་ཟད་བྱེད་པ༌[^862]ཟག་མེད་ཡིན། །

[Block 2168]
མི་དགེ་བ་ནི་གཅིག་ཏུ་གནག་པ་ཡིན་ལ། ཡིད་དུ་མི་འོང་བའི་ཕྱིར་རྣམ་པར་སྨིན་པ་ཡང་ཡིན་ནོ། །

[Block 2169]
གཟུགས་སུ་གཏོགས་པའི་དགེ་བ་ནི་མི་དགེ་བ་དང་མ་འདྲེས་པའི་ཕྱིར་གཅིག་ཏུ་དཀར་བ་ཡིན་ལ། ཡིད་དུ་འོང་བའི་ཕྱིར་རྣམ་པར་སྨིན་པ་དཀར་བ་ཡིན་ནོ། །

[Block 2170]
འདོད་པར་གཏོགས་པའི་དགེ་བ་ནི། །མི་དགེ་བ་དང་འདྲེས་པའི་ཕྱིར་དཀར་གནག་ཡིན་ལ། རྣམ་པར་སྨིན་པ་འདྲེས་པའི་ཕྱིར་རྣམ་པར་སྨིན་པ་ཡང་དཀར་གནག་ཡིན་ནོ། །

[Block 2171]
འདི་ནི་རྒྱུད་ཀྱི་སྒོ་ནས་རྣམ་པར་གཞག་གི་ངོ་བོ་ཉིད་ཀྱི་སྒོ་ནས་ནི་མ་ཡིན་ནོ། །

[Block 2172]
ཟག་པ་མེད་པའི་ལས་ནི་ལས་གསུམ་པོ་དེ་དག་ཟད་པར་བྱེད་པ་ཡིན་ནོ། །

[Block 2173]
དེ་ནི་ཉོན་མོངས་པ་ཅན་མ་ཡིན་པའི་ཕྱིར་མི་གནག་པའོ། །

[Block 2174]
རྣམ་པར་སྨིན་པ་དཀར་པོ་ཉིད་མེད་པའི་ཕྱིར་མི་དཀར་བའོ། །

[Block 2175]
འཇུག་པ་དང་འགལ་བས༌[^863]ཁམས་སུ་མ་གཏོགས་པའི་ཕྱིར་རྣམ་པར་སྨིན་པ་མེད་པ་ཡིན་ནོ། །
--- END BLOCKS ---
