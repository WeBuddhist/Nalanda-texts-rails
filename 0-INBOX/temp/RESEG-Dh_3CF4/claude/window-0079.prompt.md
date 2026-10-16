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
[Block 2766]
ཆོས་ཀྱི་ལམ་ནི་ཆོས་ཀྱི་ལམ་ཉིད་དོ། །

[Block 2767]
[^1745]ཆོས་ཀྱི་ལམ་འདུལ་བ་སྟེ། དེས་བསྐྱེད་པའི༌[^1746]ཆོས་ཀྱི་ལམ་གང་ཐོབ་པའོ། །

[Block 2768]
ཆོས་དེ་ལ་གནོད་པ་བྱས་པ་ནི་འདུལ་བ་ལ་གནོད་པ་བྱས་པས་ན་ཆོས་ལ་གནོད་པ་བྱས་པའོ། །

[Block 2769]
ཇི་ལྟར་བསྟན་པའི་རིམ་པ་བཞིན་དུ་ངེས་པར་བསྟན་པ་སྟེ། གསུམ་པོ་འདི་དག་གིས་ནི་འཇིག་རྟེན་འདི་དང་ཕ་རོལ་གཉི་ག་ལ་ཕན་པར་འཇུག་པའི་དབང་དུ་བྱས་པ་སྟེ། སྔར་བསྟན་པ་བཞིན་དུ་རིམ་པས་དགོད་དོ། །

[Block 2770]
དཔལ་མོ་གཟུགས་དང་ལྡན་པ་བཞིན། །ཞེས་བྱ་བ་ནི་གཟུགས་གཟི་མདངས་མཆོག་དང་ལྡན་པས་སོ། །

[Block 2771]
དགའ་བ་མངོན་སུམ་དུ་གྱུར་པ་བཞིན་ཞེས་བྱ་བ་ནི་བལྟ་ན་རབ་ཏུ་སྡུག་པས་སོ། །

[Block 2772]
ལྷ་མོ་བཞིན་དུ་ཞེས་བྱ་བ་ནི་བུད་མེད་རིན་པོ༌[^1747]ཆེར་གྱུར་པས་སོ། །

[Block 2773]
རྒྱུ་འདི་གསུམ་གྱིས་ནི་གཟུགས་མཛེས་ཤིང་བཟང་བར་བལྟའོ། །

[Block 2774]
མཐོང་ན་ཡིད་ནི་འཕྲོག་པ་མིའི་རིགས་ལས་ཡང་དག་པར་འདས་པ་སྟེ། བུད་མེད་རིན་པོ་ཆེར་བཀུར་བ་བཞིན་དུ་གྱུར་པར་བཤད་དོ། །

[Block 2775]
ཇི་སྲིད་ཅེས་བྱ་བ་འདིས་དུས་དང་ཡུལ་གཟུང་སྟེ། ཁྱད་པར༌[^1748]སེམས་དང་འབྲེལ་པར་སྟོན་པ་ཉིད་དེ། དེའི་ལུས་དུས་དང་ཡུལ་གང་ལ་མཐོང་བར་གྱུར་པ་དེ་སྲིད་ཀྱི་དུས་དང་། དེ་སྲིད་ཀྱི་ཡུལ་ལྟ་བ་ཟློག་པར་ནུས་པ་མེད་པའོ། །

[Block 2776]
དེ་བས་ན་ཞེས་བྱ་བ་ནི་གང་མཐོང་བ་རྣམས་ཀྱི་ལྟ་བ་ཟློག་པར༌[^1749]མི་ནུས་པའི་རྒྱུར་གྱུར་པས་སོ། །

[Block 2777]
མྱོས་པར་བྱེད་པས་ན་མྱོས་བྱེད་མ་ཞེས་བྱ་བར་བཏགས་ཏེ་མིང་གི་ཡོན་ཏན་བསྟན་པའོ། །

[Block 2778]
འདས་པ་ནི་རིགས་པར་གསོལ་བའོ། །ཇི་ལྟར་གསོལ་ཞེ་ན། དེ་ཉིད་བསྟན་པའི༌[^1750]ཕྱིར་ལྷ་ཁྱོད་ཀྱི་ཡུལ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཡིན་ནོ། །

[Block 2779]
ན་ཞེས་བྱ་བ་ནི་བུད་མེད་རིན་པོ་ཆེ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2780]
མིག་དང་ཡིད་ལ་དབང་ཡང་མེད་པར་གྱུར། །ཞེས་བྱ་བ་ནི་དེའི་གདོང་དུ་མིག་མི་འཛུམས་པར༌[^1751]ལྟ་བས་མིག་ལ་དབང་མེད་པའོ། །

[Block 2781]
ཡིད་ལ་དབང་ཡང་མེད་པར་གྱུར་པ་ནི་ཆོས་ཀྱི་རྗེས་སུ་འབྲང་བའི་བག་ཆགས་ཕྲོགས་པ༌[^1752]ཡིན་ཏེ། མི་བརྟན་པར་གྱུར་པ་ཡིན་པའི་ཕྱིར་རོ། །ཇི་ལྟ་བུ་ཞེ་ན། མིག་ལ་དབང་བྱེད་པས་ལུས་མཐོང་བར་གྱུར་པ་དེ་སྲིད་ཀྱི་དུས་དང་ཡུལ་ཡིད་ལ་དབང་བྱེད་པར་གྱུར་པ་སྟེ། འདོད་པས་མྱོས་ནས་འདུ་ཤེས་ཉམས་པར་གྱུར་པའོ། །

[Block 2782]
མིག་ལམ་དུ་མི་སྣང་བར་གྱུར་པ་ཞེས་བྱ་བ་ནི་སྔར་བཤད་པ་དང་རྗེས་སུ་མཐུན་པ༌[^1753]ཡིན་ཏེ། འདོད་ཆགས་མ་བྲལ་བ་ཡིས་ཞེས་བྱ་བ་དེའི་ཚིགས་བཅད་ཀྱིས་སོ། །

[Block 2783]
ཆོས་དང་སྲིད་ནི་ཆོས་དང་སྲིད་དོ། །

[Block 2784]
སྲིད་ཀྱི་དོན་ཡང་ཡིན་ལ་སྒྲུབ་པ་ཡང་ཡིན་པས་སྲིད་ཀྱི་དོན་སྒྲུབ་པའོ། །

[Block 2785]
ཆོས་དང་སྲིད་དེ་གཉིས་ཀྱི་དོན་སྒྲུབ་པ་ཞེས་བྱ་བ་ལ། སྲིད་ཀྱི་དོན་སྒྲུབ་པ་ནི་ནོར་བསྒྲུབ་པ་ཞེས་བྱ་བའི་དོན་ཏེ། ནོར་སྒྲུབ་པ་ནི་མ་ཐོབ་པ་ཐོབ་པར་བྱ་བ་དང་། ཐོབ་པ་ཡོངས་སུ་བསྲུང་བ་དང་། བསྲུངས་པ་རབ་ཏུ་འཕེལ་བར་བྱའོ། །

[Block 2786]
ཆོས་ཀྱི་དོན་སྒྲུབ་པ་ནི་སྟེགས་ལམ་རབ་ཏུ་བསྒྲུབ་པའོ། །

[Block 2787]
རྒྱལ་པོའི་དོན་སྒྲུབ་པ་རྣམས་ཞེས་བྱ་བ་ནི་རྒྱལ་པོས་སྒྲུབ་པའི་དོན་ཏེ། བཞི་པོ་དེ་དག་ནི་རྒྱལ་པོའི་དོན༌[^1754]སྒྲུབ་པའོ། །

[Block 2788]
སྒྲུབ་པ་དེའི་དུས་ལས་ཡོལ་བ་ནི་འདས་པའོ། །

[Block 2789]
ཕན་པ་དང་བདེ་བ་ནི་ཕན་པ་དང་བདེ་བའོ། །

[Block 2790]
འབྱུང་བ་ནི་སྐྱེ་བ་སྟེ།[^1755] དེ་ནི་ལམ་ནི་སྐྱེ་བའི་ལམ་ཡིན་པས་ཕན་པ་དང་བདེ་བ་འབྱུང་བའི་ལམ་མོ། །

[Block 2791]
རྒྱལ་པོའི་དོན་སྒྲུབ་པ་ལས་ཡོལ་བ་དེ་ནི་འབངས་རྣམས་ལ་ཕན་པ་དང་བདེ་བའི་ལམ་ཆད་དེ་ཕུང་བར་འགྱུར་ཞེས་བསམས་པའོ། །

[Block 2792]
འདི་ནི་མཐོང་བ་ཙམ་གྱིས་ནི། །ཞེས་བྱ་བ་ནི་གང་ཡུལ་མངོན་སུམ་དུ་གྱུར་པས་ཀྱང་སྟེ། འདིས་ནི་དབང་པོའི་སྒོ་བསྡམས་པ་བསྟན་ཏོ། །

[Block 2793]
དྲང་སྲོང་རྣམས་ཀྱང་ཞེས་བྱ་བ་ནི་ཉོན་མོངས་པ་ཐུབ་པའོ། །

[Block 2794]
ཉོན་མོངས་པའི་བག༌[^1756]ཆགས་མ་སྤངས་པ་དང་། ཚུལ་བཞིན་མ་ཡིན་པ་ཡིད་ལ་བྱེད་པ་ལ་སོགས་པ་རྒྱུ་གསུམ་པོ་ཚང་བས་ནི་ཉོན་མོངས་པ་རྣམས་དུས་རེས་འགའ་སྐྱེ་བར་འགྱུར་ཏེ། ཡུལ་རྒྱ་ཆེར་མངོན་སུམ་དུ་གྱུར་པ་དང་། ཚུལ་བཞིན་མ་ཡིན་པ་ཡིད་ལ་བྱེད་པ་དང་། བག་ཆགས་མ༌[^1757]སྤངས་པ་སྟེ། དེའི་ཕྱིར་བཤད་པ།

[Block 2795 [VERSE]]
ཕྲ་རྒྱས་སྤངས་པ་མ་ཡིན་དང་། །
ཡུལ་འདི༌[^1758]ཉེ་བར་གནས་པ་དང་། །
ཚུལ་བཞིན་མ་ཡིན་ཡིད་བྱེད་པས། །
ཉོན་མོངས་རྒྱུ་ནི་ཚང་བ་ཡིན། །

[Block 2796]
ཞེས་གསུངས་སོ། །

[Block 2797]
འདོད་ཆགས་ཅན་གྱི་མིག་ལྟ་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཕྱེད་ཀྱིས༌[^1759]གོང་མ་ལས་བཟློག་པ་བསྟན་ཏོ། །

[Block 2798]
[^1760]འདོད་ཆགས་ཅན་གྱི་མིག་ཅེས་པས༌[^1761]ནི་དབང་པོའི་སྒོ་མ་བསྡམས་པ་དང་། བག༌[^1762]ཆགས་ཡང་དག་པར་མ་སྤངས་པ་ཉིད་དོ། །

[Block 2799]
རྒྱལ་པོ་ཞེས་བྱ་བ་འདིས་ཚུལ་བཞིན་ཡིད་ལ་བྱད་པ་ཡིན་ཏེ། རང་དབང་དུ་གྱུར་པས་ཚུལ་བཞིན༌[^1763]ཡིད་ལ་མི་བྱེད་པ་མི་ལྡོག་པའོ། །

[Block 2800]
བདེ་བར་གནས་པ་ཞེས་བྱ་བ་འདིས་ནི་ཡུལ་ཉེ་བར་གནས་པ་ཡིན་ཏེ། དེ་ལྟར་ཉོན་མོངས་པའི་རྒྱུ་ཚང་བར་གྱུར་པས་སོ། །

[Block 2801]
ཉོན་མོངས་པ་རྣམས་ནི་སེམས༌[^1764]རང་དབང་དུ་གྱུར་པ་ལས་ཀྱང་འབྱུང་སྟེ། སྔར་བསྟན་པ་ཐམས་ཅད་འདི་ལས་འབྱུང་བར་བསྟན་ཏོ། །

[Block 2802]
ཡང་ན་དོན་གཞན་དུ་ན་ཉོན་མོངས་པ་རྣམས་ནི་རྒྱུ་བཞིས་སྐྱེ་བར་འགྱུར་ཏེ། དབང་པོའི་སྒོ་མ་བསྡམས་པ་དང་། དེ་ནི༌[^1765]ཡུལ་མངོན་དུ་གྱུར་པ་དང་། ཡིད་ལ་བྱེད་པས་དེ་ལ་ལྟ་བ་དང་། རྒས་པས་ནི༌[^1766]མི་ནུས་པ་སྟེ། དེ་ལ་ནུས་པ་མ་ཚང་བས་སོ། །

[Block 2803]
ནང་ཡང་གཟུང༌[^1767]སྟེ། དེའི་རང་བཞིན་ཉིད་དོ། །

[Block 2804]
གཞན་དབང་ཡང་རང་ལ་ནུས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 2805]
དེ་ལ་འདོད་ཆགས་ཅན་གྱི་མིག་གིས་ལྟ་ཞེས་བྱ་བའི་སྐབས་ཀྱིས་ནི་དེ་ལས་བཟློག་པ་ལ་ཡང་མི་འབྱུང་བའི་ཕྱིར་རོ། །
--- END BLOCKS ---
