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
[Block 2836]
དེ་ལ་གནས་པའི་རྣམ་པ་དེ་ནི་དེ་ལྟར་གྱུར་པའོ། །

[Block 2837]
སེམས་རྩེ་གཅིག་ཏུ་དམིགས་པ་ནི་རྩེ་གཅིག་པའོ། །

[Block 2838]
དེ་ལ་རྩེ་གཅིག་ཏུ་གྱུར་པའི་སེམས་གང་ཡིན་པ་དེ་ནི་དེ་ལ་སེམས་རྩེ་གཅིག་པའོ། །

[Block 2839]
རེ་ཐག་ཆད་པའི་ཡིད་གང་ཡིན་པ་དེ་ནི་རེ་ཐག་བཅད་པའི་སེམས་སོ། །

[Block 2840]
དེ་ལ་སེམས་ཆགས་པ༌[^1799]བཞིན་དུ་ཞེས་བྱ་བ་ནི་རྣམ་པར་ཆགས་པ་ལྡོག་པར་མ་གྱུར་ཏེ། འདོད་བཞིན་དུ་གཞན་གྱི་ཆུང་མ་ཡིན་ནོ་ཞེས་པས་སོ། །

[Block 2841]
དོན་གྱི་རྗེས་སུ་འགྲོ་བ་ནི་དོན་དང་རྗེས་སུ་མཐུན་པའོ། །

[Block 2842]
སྙན་པ་དེ་དག་ནི་ཚིག་སྟེ་ཚིག་ཀྱང་སྙན༌[^1800]པའོ། །

[Block 2843]
དོན་དང་རྗེས་སུ་མཐུན་པ༌[^1801]ཡིན་ལ་ཚིག་སྙན་པ་ཡང་ཡིན་པས་དོན་དང་རྗེས་སུ་མཐུན་ཞིང་ཚིག་སྙན་པའོ། །

[Block 2844]
དོན་དང་རྗེས་སུ་མཐུན་པའི་ཚིག་གིས་འདི་ལྟར་བཏགས་པའི་མིང་གང་ཡིན་པ་དེ་ནི་དོན་དང༌[^1802]རྗེས་སུ་མཐུན་པའི་ཚིག་སྙན་མིང་དུ་བཏགས་པའོ། །

[Block 2845]
མིང་དེ་གང་ཡིན་ཞེ་ན། མྱོས་བྱེད་མ་ཞེས་པའོ། །

[Block 2846]
དོན་དང་རྗེས་སུ་མཐུན་པའི་ཚིག་ཉིད་བསྟན་པའི་ཕྱིར་སྨྲས་པ། བདག་ནི་མྱོས་པ་བཞིན་དུ་བྱེད། །ཅེས་བྱ་བ་ཡིན་ནོ། །

[Block 2847]
དེ་ནི་བརྗེད་པར་བདག་འདོད་ན། །ཞེས་བྱ་བ་ནི་གཞན་གྱི་ཆུང་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2848]
སེམས་ཀྱིས་མཐོང་བ་བཞིན་དུ་གྱུར། །ཞེས་བྱ་བ་ནི་དེའི་གཟུགས་ཕུན་སུམ་ཚོགས་པ་དང་འདོད་པས་དེ་ནི༌[^1803]བརྗེད་པར་བདག་འདོད་ན་མ་བརྗེད་པས་སོ། །

[Block 2849]
བདག་གི་སེམས་ནི་དེ་ལ་གནས། །ཞེས་བྱ་བ་ནི་སེམས་ཀྱིས་མཐོང་བ་བཞིན་དུ་གྱུར་ཞེས་བྱ་བ་ཡིན་ཏེ། གང་གི་ཕྱིར་ཞེ་ན། སེམས་དེ་དེའི་དབང་དུ་གྱུར་པས་སོ། །

[Block 2850]
དེའི་དབང་དུ་གྱུར་ཞེས་བྱ་བ་ནི་སེམས་དེའི་དབང་དུ་གྱུར་པ་སྟེ། དེ་ལྟར་བརྗེད་པར་འདོད་ཀྱང་མི་བརྗེད་པའི་རྒྱུ་དང་། མི་མཐོང་བར་འདོད་ཀྱང་མཐོང་བའི་རྒྱུས་ཞེས་ཚིགས་བཅད་འོག་མ་ཕྱེད་ཉིད་བསྟན་ཏོ། །

[Block 2851]
ཆུང་མ་ཡིན་བ་ལ་ཞེས་བྱ་བ་ནི་ཆུང་མའི་ཕྱིར་རོ། །

[Block 2852]
བདག་ཀྱང་ཞེས་བྱ་བ་ནི་སྔར་བཤད་པའི་ཡོན་ཏན་གྱི་མཚན་ཉིད་དང་ལྡན་པར་བསྟན་པའོ། །

[Block 2853]
དེ་ལྟར་མི་བརྟན་པ་ཞེས་བྱ་བ་ནི། །

[Block 2854 [VERSE]]
དེ་ནི་བརྗེད་པར་འདོད་པ་ལ། །
སེམས་ཀྱིས་མཐོང་བ་བཞིན་དུ་གྱུར། །

[Block 2855]
ཞེས་བྱ་བ་དེ་ཉིད་སྟོན་པར་བྱེད་པ་ཡིན་ནོ། །

[Block 2856]
དེ་བས་ན་གོང་དུ་བཤད་པའི་རྒྱུ་དེ་དག་གིས་ངོ་ཚ་བ་དང་བྲལ་བཞིན་དུ་ཞེས་བྱ་བ་ནི་དེ་མི་བརྟན་པ་ཉིད་ཡིན་ཏེ། བག་ཆག་ས་ཞེན་པ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 2857]
གཉིད་དང་བྲལ་བ་ཞེས་བྱ་བ་ནི་དེའི་མི་བརྟན་པ་ཡིན་ཏེ། ཤས་ཆེར་སྟོན་པའོ། །

[Block 2858]
སེམས་ཀྱིས་མཐོང་བ་བཞིན་དུ་ཞེས་བྱ་བ་ནི་གང་གོང་དུ་བསྟན་པ་ཡིན་ཏེ། ཇི་ལྟར་མཐོང་བ་ཡིན་ཞེ་ན། དེ་ཉིད་བསྟན་པའི་ཕྱིར། དེའི་ལུས་བཟང་ཆས་ཤིང་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ན། །[^1804]ལུས་བཟང་ཞེས་བྱ་བ་སྨོས་པས་ནི་སྔ་མ་བཞིན་དུ་མདོག་དང་དབྱིབས་གཉིས་གཟུང༌[^1805]ངོ་། །ཆས་ཤིང་འགྲེང་དང་ལྟ་བ་ལ། །ཞེས་བྱ་བ་ནི་སྔར་བཤད་པའི་ཉེ་བར་སྤྱོད་པའི་དབྱེ་བ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 2859]
ཆགས་པས་མ་གཡོས་པའི་ཡིད་གང་ཡིན་པ་དེ་ནི་ཆགས་པས་རྩེ་གཅིག་པའི་ཡིད་དུ་གྱུར་པའོ། །

[Block 2860]
དེ་བས་ན་གཞན་དོན་སྒྲུབ་པ༌[^1806]དེའི་གོ་རིམས་ནི་རིམ་གྱིས་ཡིན་ཏེ། དེའི་སྦྲོན་པ་ནི་དོན་སྒྲུབ་གོ་རིམས་སྦྲོན་པ་སྟེ། དེ་ལ་སྒྲ་གྲག་པ༌[^1807]གང་ཡིན་པ་དེའོ། །

[Block 2861]
ཞེ་སྡང་ནི་ཁྲོ་བའོ། །

[Block 2862]
སེམས་ལ་སྡང༌[^1808]ཞེས་བྱ་བ་ནི་རབ་ཏུ་སད་པར༌[^1809]བྱེད་པ་སྟེ། རབ་ཏུ་ཉལ་ཏེ་ཞེན་པ༌[^1810]ལས་སད་པར་བྱེད་པའོ། །

[Block 2863]
བརྣགས༌[^1811]ཏེ་བོར་ཡང་ཞེས་བྱ་བ་ནི་འདོད་པས་མྱོས་པའི་མཐུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2864]
བརྣགས༌[^1812]ཀྱང་བརྟན་པ་ཉམས་པར་གྱུར་ཏོ། །

[Block 2865]
མདངས་ནི་སེར་སྐྱར་གྱུར་ཅིང་ལུས་ཀྱང་ཤ་བྲི་སྟེ་སྲབ་མོར་གྱུར་ཞེས་བྱ་བ་ནི་འདོད་ཆགས་ཀྱིས་མྱོས་པར་གྱུར་པའི་རྣམ་པ་རབ་ཏུ་མངོན་པར་གྱུར་པའོ། །

[Block 2866]
སེམས་ཁོང་དུ་ཆུད་ཅིང་ཤུགས༌[^1813]ནར་ཞེས་འབྱུང་ལ། གླལ་ཡང་དང་ཡང་དུ་འབྱུང་བ་ཞེས་བྱ་བ་ནི་བྱ་བའི་ཚུལ་ལས་འདོད་ཆགས་ཀྱིས་མྱོས་པར་གྱུར་པ་རབ་ཏུ་མངོན་པའོ། །

[Block 2867]
སྤྱོད་ཡུལ་གྱི་མཚན་ཉིད་ཡིན་པའི་ཕྱིར་ཤིན་ཏུ་གསལ་བའི་དོན་ཏེ། སྤྱོད༌[^1814]ཚུལ་འདིའི་རྣམ་པ་ཡིན་པ་སྟེ། འདོད་པས་མྱོས་པར༌[^1815]གྱུར་པའི་རྣམ་པའོ། །

[Block 2868]
འདོད་ཆགས་ཀྱིས་མྱོས་པར་གྱུར་པའི་རྣམ་པ་རབ་ཏུ་མངོན་པར་གྱུར་པ་གང་ཡིན་པ་དེ་ནི་འདོད་པས་མྱོས་པར་གྱུར་པའི་རྣམ་པ་རབ་ཏུ་མངོན་པ་སྟེ། རྣམ་པའམ༌[^1816]སྤྱོད་ཚུལ་རབ་ཏུ་གསལ་ཞིང་མངོན་པར་གྱུར་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2869]
འདོད་ཆགས་ཀྱིས་མྱོས་པར་གྱུར་པའི་རྣམ་པ་རབ་ཏུ་མངོན༌[^1817]ཞེས་བྱ་བ་འདིའི་དོན་ནི་བསྟན་པ༌[^1818]ཆེན་པོས་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་ས་སྟོན་པ་ཡིན་ཏེ། འདིའི་དོན་ནི་བརྣགས༌[^1819]ཤིང་བསྒྲིམས་པ་ནི་རབ་ཏུ་བཀག་པ་བཞིན་དུའོ། །

[Block 2870]
ཡིད་གྱུར་པ་ནི་ལུས་ཀྱི་བྱ་བ་དང་སྤྱོད་པ་གྱུར་པའི་རྣམ་པ་སྣང་བ་ལས་མངོན་པར་གྱུར་པ་ཡིན་ཏེ། ཚིགས་བཅད་འདིས་ནི་བཤད་པའི་དོན་དེ་ཉིད་བསྟན་ཏོ། །

[Block 2871]
ཡིད་གྱུར་པ་ནི་འདོད་ཆགས་ཀྱིས་མྱོས་པར་གྱུར་པའོ། །

[Block 2872]
སེམས་ཁོང་དུ་ཆུད་པའི་མིག་དང་། བཞིན་དང་མདངས་ཞེས་བྱ་བ་ནི་གང་གོང་དུ་བསྟན་པའི་སེམས་ཁོང་དུ་ཆུད་ཅིང་ཤུགས་ནར་ཞེས་འབྱུང་ལ་གླལ་ཡང་དང་ཡང་དུ་འབྱུང་ཞེས་བྱ་བ་དེ་ཉིད་སྟོན་ཏོ། །

[Block 2873]
ཤ་བྲི་སྲབ་མོར་གྱུར་ཞེས་བྱ་བ་འདིས་ནི་སེར་སྐྱར་གྱུར་ཅིང་ཤ་བྲི་སྟེ་སྲབ་མོར་གྱུར་ཞེས་བྱ་བ་དེ་ཉིད་བསྟན་པ་ཡིན་ནོ། །

[Block 2874]
དེས་བརྡ་དང་མཚན་མ་ལ་མཁས་པ་ཞེས་བྱ་བ་ལ་བརྡ་ནི་གང་གོང་དུ་བསྟན་པའི་སེམས༌[^1820]ཁོང་དུ་ཆུད་ཅིང་ཤུགས་ནར་ཞེས་འབྱུང་ལ། གླལ་ཡང་དང་ཡང་དུ་འབྱུང་ཞེས་བྱ་བ་དེ་ཉིད་ཀྱིས་བསྟན་པ་ཡིན་ནོ། །

[Block 2875]
མཚན་མ་ནི་གང་གོང་དུ་བསྟན་པའི་སེར་སྐྱར་གྱུར་ཅིང་ལུས་ཀྱང་ཤ་བྲི་སྟེ་སྲབ་མོར་གྱུར་ཞེས་པ་དང་། འདོད་ཆགས་ཀྱིས་མྱོས་པར་གྱུར་པའི་རྣམ་པ་མངོན་པར་གྱུར་པ་ཞེས་གང་བསྟན་པའོ། །
--- END BLOCKS ---
