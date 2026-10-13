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
[Block 2031]
བསྙེན་གནས་ཀྱི་སྡོམ་པ་ནི་མཚན་མོ་འདས་པ་ལས་ཀྱང་ངོ་། །ཁ་ཅིག་ལྟུང་བར་འགྱུར་ལས་སྨྲ། །གཞན་དག་ན་རེ་ལྟུང་བར་འགྱུར་བ་བཞི་ལས་གང་ཡང་རུང་བ་ཞིག་གིས་དགེ་སློང་དང་དགེ་སྦྱོང་གི་སྡོམ་པ་གཏོང་ངོ་ཞེས་ཟེར་རོ། །

[Block 2032]
གཞན་དག་དམ་ཆོས་ནུབ་པ་ལས། །

[Block 2033]
འདི་ལྟར་དམ་པའི་ཆོས་ནུབ་ན་བསླབ་པའི་མཚམས་ཐམས་ཅད་དང་། །

[Block 2034 [VERSE]]
ལས་ཀྱི་མཐའ་རྣམས་མེད་པར་འགྱུར་རོ། །
ཁ་ཆེ་རྣམས་ནི་བྱུང་བ་ལ། །
བུ་ལོན་ནོར༌[^804]བཞིན་གཉིས་སུ་འདོད། །

[Block 2035]
ཁ་ཆེ་བ་རྣམས་ན་རེ་རྩ་བའི་ལྟུང་བ་ལ་ཡང་དགེ་སློང་གི་སྡོམ་པ་གཏོང་བ་མེད་དོ། །ཅིའི་ཕྱིར་ཞེ་ན། ཕྱོགས་གཅིག་ཉམས་པས་སྡོམ་པ་ཟད་པར་གཏོང་བ་ནི་མ་རིགས༌[^805]པའི་ཕྱིར་རོ། །

[Block 2036]
འོན་ཀྱང་འདི་ལ་ཚུལ་ཁྲིམས་དང་འཆལ་བའི་ཚུལ་ཁྲིམས་གཉིས་ཀ་ཡང་ཡོད་དེ། དཔེར་ན་འགའ་ཞིག་ལ་ནོར་ཡང་བདོག་ལ་བུ་ལོན་ཡང་ཆགས་པ་བཞིན་ནོ། །

[Block 2037]
ལྟུང་བ༌[^806]དེ་བཤགས་ན་ཚུལ་ཁྲིམས་དང་ལྡན་པ་ཁོ་ནར་འགྱུར་རོ། །

[Block 2038]
ཡང་བསམ་གཏན་དང་ཟག་པ་མེད་པའི་སྡོམ་པ་དག་ཇི་ལྟར་གཏོང་ཞེ་ན།

[Block 2039 [VERSE]]
བསམ་གཏན་གཏོགས་པའི་དགེ་བ་ནི། །
ས་འཕོས་ཉམས་པ་དག་གིས་གཏོང་། །

[Block 2040]
བསམ་གཏན་དུ་གཏོགས་པའི་དགེ་བ་ཐམས་ཅད་གཏོང་བ་ནི་གོང་མའམ་འོག་ཏུ་སྐྱེ་བ་སྟེ་ས་འཕོས་པ་ལས་སམ། སྙོམས་པར་འཇུག་པ་ལས་ཡོངས་སུ་ཉམས་པ་ལས་སོ། །

[Block 2041 [VERSE]]
ཇི་ལྟར་གཟུགས་སུ་གཏོགས་པ་ལྟར། །
དེ་བཞིན་གཟུགས་མེད་གཏོགས་འཕགས་པ། །
འབྲས་བུ་ཐོབ་སྦྱངས་ཉམས་པ་ལས། །

[Block 2042]
དགེ་བ་ཟག་པ་མེད་པ་ནི་འབྲས་བུ་ཐོབ་པ་ལས་ལམ་སྔ་མ་གཏོང་བར་འགྱུར་རོ། །

[Block 2043]
དབང་པོ་སྦྱངས་པ་ལས་དབང་པོ་རྟུལ་པོའི་ལམ་མོ། །

[Block 2044]
ཡོངས་སུ་ཉམས་པ་ལས་ལམ་གོང་མའོ། །

[Block 2045]
རེ་ཞིག་སྡོམ་པ་རྣམས་ནི་དེ་ལྟར་གཏོང་ངོ་། །

[Block 2046 [VERSE]]
སྡོམ་མིན་སྡོམ་པ་ཐོབ་པ༌[^807]དང་། །
ཤི་དང་མཚན་གཉིས་བྱུང་བ་དང་།[^808] །

[Block 2047]
སྡོམ་པ་ཐོབ་པ་ལས་ནི་གལ་ཏེ་སྡོམ་པ་ཡང་དག་པར་བླངས་པས་སམ། །བསམ་གཏན་གྱི་སྡོམ་པ་ཐོབ་པ་ནའོ། །

[Block 2048]
ལུས་བོར་བའི༌[^809]ཕྱིར་ཤི་བ་དང་། རྟེན་ཉམས་པའི་ཕྱིར་མཚན་གཉིས་བྱུང་བ་ལས་སོ། །

[Block 2049 [VERSE]]
བར་མ་ཤུགས་བླངས་བྱ་བ་དང་། །
དོན་ཚེ་རྩ་བ་ཆད་པ་ལས། །

[Block 2050]
རབ་ཏུ་དང་བ་དང་ཉོན་མོངས་པའི་ཤུགས་གང་གིས་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་འཕངས་པ༌[^810]དེ་ཆད་པ༌[^811]དེ་ཡང་རྣམ་པར་ཆད་པར་འགྱུར་རོ། །

[Block 2051]
གལ་ཏེ་ཡང་དག་པར་གཏོང་ན༌[^812]བླངས་པ་གཏོང་བ་ལས་སོ། །

[Block 2052]
ཇི་ལྟར་བླངས་པ་མི་བྱེད་ན་བྱ་བ་རྣམ་པར་ཆད་པ་ལས་སོ། །

[Block 2053]
མཆོད་རྟེན་དང་། ཀུན་དགའ་ར་བ་དང་། གཙུག་ལག་ཁང་དང་། མལ་ཆ་དང་། སྟན་དང་། གོས་དང་། རྒྱན་ལ་སོགས་པའི་དངོས་པོའི་དོན་ཆད་པ་ལས་སོ། །

[Block 2054]
ཚེ་ཆད་པ་ལས་ཀྱང་ངོ་། །གང་གི་ཚེ་དགེ་བའི་རྩ་བ་ཀུན་དུ་གཅོད་པར་བྱེད་པ་རྩོམ་པ༌[^813]ན༌[^814]ཡང་ངོ་། །དེ་ལྟར་ན་བར་མའི་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་གཏོང་བར་འགྱུར་རོ། །

[Block 2055 [VERSE]]
འདོད་གཏོགས་དགེ་བ་གཟུགས་མིན་ནི། །
རྩ་ཆད་གོང་དུ་སྐྱེས་པ་ལས། །

[Block 2056]
དགེ་བའི་རྩ་བ་ཀུན་དུ་ཆད་པའམ། གཟུགས་དང་། གཟུགས་མེད་པའི་ཁམས་སུ་སྐྱེ་བ་ལས་སོ། །

[Block 2057 [VERSE]]
ཉོན་མོངས་པ་ཅན་གཟུགས་མིན་ནོ།[^815] །
གཉིས་པོ༌[^816]སྐྱེས་པས་རྣམ་ཉམས་འགྱུར། །

[Block 2058]
ཉེ་བའི་ཉོན་མོངས་པའི་རྣམ་པ་གང་གི་སྤོང་བའི་ལམ་གང་ཡིན་པ་དེས་འདི་འཁོར་དང་བཅས་པ་ཡོངས་སུ་སྤོང་བར་བྱེད་ཀྱི་གཞན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 2059 [HEADING]]
#### སྡོམ་པ་སེམས་ཅན་གང་དག་ལ་ཡོད་པ། ^4-2-6-0

[Block 2060]
ཡང་སྡོམ་པ་མ་ཡིན་པ་དང་། སྡོམ་པ་ནི་སེམས་ཅན་གང་དག༌[^817]ལ་ཡོད་ཅེ་ན།

[Block 2061 [VERSE]]
ཟ་མ་མ་ནིང་སྒྲ་མི་སྙན། །
མཚན་གཉིས་མ་གཏོགས་མི་རྣམས་ལ། །
སྡོམ་མིན་སྡོམ་པའང་དེ་བཞིན་ལ། །

[Block 2062]
ལྷ་ལའང་།[^818] བྱང་གི༌[^819]སྒྲ་མི་སྙན་པ་རྣམས་ལ་ནི་ཡང་དག་པར་ལེན་པ་དང་། ཏིང་ངེ་འཛིན་མེད་པའི་ཕྱིར་དང་། སྡིག་པ་བྱ་བའི༌[^820]བསམ་པ་མེད་པའི་ཕྱིར་སྡོམ་པ་དང་སྡོམ་པ་མ་ཡིན་པ་མེད་དོ། །

[Block 2063]
ངན་སོང་རྣམས་ལ་ཡང་གང་དང་ལྡན་པ་དང་། གང་མེད་པས་སྡོམ་པ་དང་སྡོམ་པ་མ་ཡིན་པ་དག་ཏུ་འགྱུར་བ་ངོ་ཚ་ཤེས་པ་དང་ཁྲེལ་ཡོད་པ་ཤས་ཆེན་པོ་མེད་དོ། །

[Block 2064]
ཟ་མ་ལ་སོགས་པ་དེ་དག་གི༌[^821]ལུས་དེ་ལྟ་བུ་གང་ལ་སྡོམ་པ་མ་ཡིན་པ་མི་སྐྱེ་ལ། སྡོམ་པ་ཡང་ངོ་། །

[Block 2065]
དེ་ལ་ཡང་། མི་རྣམས་ལ་གསུམ་མོ། །

[Block 2066]
མི་རྣམས་ལ་ནི་སོ་སོར་ཐར་པའི་སྡོམ་པ་ལ་སོགས་པ་ཐམས་ཅད་ཡོད་དོ། །

[Block 2067]
འདོད་དང་གཟུགས་སྐྱེས་ལྷ་རྣམས་ལ། །བསམ་གཏན་སྐྱེས་ཡོད། བསམ་གཏན་གྱི་སྡོམ་པ་ནི་འདོད་པ་དང་གཟུགས་ཀྱི་ཁམས་སུ་སྐྱེས་པའི་ལྷ་རྣམས་ཁོ་ན་ལ་ཡོད་དོ། །

[Block 2068]
ཟག་མེད་ནི།

[Block 2069 [VERSE]]
བསམ་གཏན་ཁྱད་པར་འདུ་ཤེས་མེད། །
སེམས་ཅན་མ་གཏོགས་གཟུགས་མེད་ན་འང་། །

[Block 2070]
འདོད་པ་དང་གཟུགས་ཀྱི་ཁམས་སུ་སྐྱེས་པ་རྣམས་ལ༌[^822]ཡང་ཡོད་དོ།[^823] །
--- END BLOCKS ---
