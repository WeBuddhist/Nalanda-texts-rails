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
[Block 841]
བྱམས་པ་དང་ལྡན་པ་ནི། གར་སྐྱེས་ཀྱང་དབང་པོ་གསལ་ཞིང་དབང་པོ་ཚང་བར་སྐྱེ་བར་འགྱུར་བས་ན། དབང་པོ་ཉམས་པ་དང་མ་ཚང་བ་ཐམས་ཅད་སྤངས་པ༌[^741]ཞེས་བྱའོ། །

[Block 842]
བདེ་འགྲོ་ཐམས་ཅད་དང་མྱ་ངན་ལས་འདས་པའི་ལམ་དང་མཐུན་པ་ཞེས་བྱ་བ་ལ། ཇི་ལྟར་ཚུལ་ཁྲིམས་དང་སྦྱིན་པ་ལ་སོགས་པས་ལྷ་དང་མིར༌[^742]སྐྱེ་བ༌[^743]དང་། འཕགས་པའི་ལམ་ཡན་ལག་བརྒྱད་པས་མྱ་ངན་ལས་འདས་པ་ཐོབ་པར་འགྱུར་བ་བཞིན་དུ་བྱམས་པ་ལ་གནས་པས་ཀྱང་རྟག་ཏུ་ལྷ་དང་མིར་སྐྱེ་བ་དང་། མྱ་ངན་ལས་འདས་པ་ཐོབ་པར་འགྱུར་བས་ན་བདེ་འགྲོ་ཐམས་ཅད་དང་མྱ་ངན་ལས་འདས་པའི་ལམ་དང་མཐུན་པ་ཞེས་བྱའོ། །

[Block 843]
ངན་སོང་ཐམས་ཅད་དང་། མི་ཁོམ་པ་བརྒྱད་ལས་འདས་པ་ཞེས་བྱ་བ་ནི་བྱམས་པ་དང་ལྡན་པ་དེ་ནམས་ཀྱང་ཉམས་ང་བའི་གནས་དག་ཏུ་མི་སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 844]
འབྲས་བུ་བཤད་ཟིན་ཏོ།། །།

[Block 845 [HEADING]]
#### རང་བཞིན། ^2-1-4-0

[Block 846]
རང་བཞིན་བསྟན་པའི་ཕྱིར། ཆོས་ཀྱི༌[^744]ཀུན་དགའ་ལ་དགའ་མོས་པ་ཞེས་བྱ་བ་གསུངས་ཏེ། སྟོང་པ་ཉིད་ལ་དད་པ་ནི་ཆོས་ཀྱི་ཀུན་དགའ་ལ་དགའ་བའོ། །

[Block 847]
དེ་སྟོན་པར་བྱེད་པའི་གཞུང་དེ༌[^745]ལ་དད་པ་ནི་ཆོས་ཀྱི༌[^746]ཀུན་དགའ་ལ་མོས་པའོ། །

[Block 848]
ཡང་ན་ཆོས་སྤྱད༌[^747]པར་འདོད་པ་ནི་ཆོས་ཀྱི་ཀུན་དགའ༌[^748]ལ་དགའ་བའོ། །

[Block 849]
དེ་སྒྲུབ་པར་བྱེད་པ་ནི་ཆོས་ཀྱི་ཀུན་དགའ་ལ་མོས་པ་སྟེ། དེ་བས་ན་འདོད་པ་དང་ལོངས་སྤྱོད་ལ་མི་འདོད་ཅེས་བྱ་བར༌[^749]སྦྱར་རོ། །

[Block 850]
འདོད་པ་ནི་གཟུགས་དང་སྒྲ་ལ་སོགས་པའོ། །

[Block 851]
ལོངས་སྤྱོད་པ་ནི་བཟའ་བ་དང་། བཏུང་བ་ལ་སོགས་པའོ། །

[Block 852]
དབང་ཕྱུག་ནི་རྒྱལ་པོའི་སྲིད་ལ་སོགས་པའོ། །

[Block 853]
སེམས་ཅན་ཐམས་ཅད་ལ་སེམས་སྙོམས་པ་ཞེས་བྱ་བ་ནི་བྱམས་པ་དེས་ཕྱོགས་དང་དུས་ཆད་པ་མེད་དེ། ཕྱོགས་བཅུ་དང་དུས་གསུམ་ཐམས་ཅད་ཀྱི་སེམས་ཅན་ཐམས་ཅད་ལ་འདྲ་བར་དམིགས་པའི་ཕྱིར་རོ། །

[Block 854]
སྦྱིན་པའི་སྦྱོར་བ་ཐ་དད་པ་དང་བྲལ་བ་ཞེས་བྱ་བ་ནི་འདི་ལ་ནི་སྦྱིན། འདི་ལ་ནི་མི༌[^750]སྦྱིན་ཞེས་བྱ་བ་དང་། འདི་ནི་སྦྱིན།[^751] འདི་ནི་མི་སྦྱིན་ཞེས་བྱ་བ་མེད་ཀྱི། སེམས་ཅན་ཐམས་ཅད་ལ་དངོས་པོ་ཐམས་ཅད་སྦྱིན་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 855]
ཚུལ་ཁྲིམས་དང་བསླབ་པ་ཐམས་ཅད་ཀྱི་སྒོ་ཞེས་བྱ་བ་ནི་བྱམས་པ་དང་ལྡན་ན་སེམས་ཅན་གྱི་སྲོག་གཅོད་པ་དང་། ལོངས་སྤྱོད་ལས་མ་བྱིན་པར་ལེན་པ་ལ་སོགས་པ་མི་བྱེད་དེ། [^752]ཚུལ་ཁྲིམས་སྐྱེ་བའི་རྒྱུ་དང་རྐྱེན་ཡིན་པའི་ཕྱིར་ཚུལ་ཁྲིམས་དང་བསླབ་པ་ཐམས་ཅད་ཀྱི་སྒོ་ཞེས་བྱའོ། །

[Block 856]
ཚུལ་ཁྲིམས་འཆལ་པ་ཐམས་ཅད་ཡོངས་སུ་སྐྱོབ་པ་ཞེས་བྱ་བ་ནི་ཚུལ་ཁྲིམས་ཉམས་པ༌[^753]རྣམས་མི་དགེ་བའི་གནས་ནས་བསྐྱོད་དེ་དགེ་བའི་གནས་སུ་འགོད་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 857]
བཟོད་པའི་སྟོབས་སྟོན་པ་ཞེས་བྱ་བ་ནི་སེམས་ཅན་མཐུ་ཆུང་ངུ་རྣམས་ཀྱིས་གནོད་པར༌[^754]བྱས་ཀྱང་སླར་གནོད་པར༌[^755]མི་བྱེད་པའི་ཕྱིར་ཏེ། དེ་བས་ན་ང་རྒྱལ་དང་རྒྱགས་པ་དང་དྲེགས་པ་ཐམས་ཅད་དང་བྲལ་བའོ། །

[Block 858]
དེ་ལ་ང་རྒྱལ་ནི་ང་རྒྱལ་རྣམ་པ་བདུན་ནོ། །

[Block 859]
རྒྱགས་པ་ནི་ལོངས་སྤྱོད་སྙེམས་པའོ། །

[Block 860]
དྲེགས་པ་ནི་བྱད་ལག་དང་ཤེས་པ་སྙེམས་པ་སྟེ། བྱམས་པ་དང་ལྡན་པ་ལ་ཉེས་པ་དེ་ལྟ་བུ་མེད་པས་ན་བྲལ་བ་ཞེས་བྱ་སྟེ། [^756]རྩ་བ་ཞེས་བྱ་བ་ནི་ཏིང་ངེ་འཛིན་དེ་རྣམས་ཀྱི་རྒྱུ་བྱམས་པ་ཡིན་པས་སོ། །

[Block 861]
མི་འཁྲུགས་པའི་བརྩོན་འགྲུས་བརྩམས་ཤིང་ཡང་དག་པར་སྦྱོར་བ་བྱ་བ་ཐམས་ཅད་ལས་སྒྲོལ་བ་ཞེས་བྱ་བ་ནི་བརྩོན་འགྲུས་ཀྱི་བྱ་བ་འདི་ལྟ་བུ་ཡང་བྱམས་པས་མཐར་འབྱིན་པར་བྱེད་དེ་ཞེས་བྱ་བར་སྦྱར་ཏེ། ལེ་ལོའི་དབང་དུ་མི་འགྱུར་ཞིང་གྲང་བ་དང་ཚ་བ་ལ་སོགས་པ་དང་། བདུད་དང་མུ་སྟེགས་ཅན་ལ་སོགས་པས་མི་བཟློག་པའི༌[^757]བརྩོན་འགྲུས་བརྩམས་པ་ནི་མི་འཁྲུགས་པའི་བརྩོན་འགྲུས་བརྩམས་པ་ཞེས་བྱའོ། །

[Block 862]
ཕ་རོལ་དུ་ཕྱིན་པ་དྲུག་བསྒྲུབས་པ༌[^758]དང་། སེམས་ཅན་ཐམས་ཅད་ཀྱི་དོན་བྱ་བར་སྦྱོར་བ་ནི། ཡང་དག་པར་སྦྱོར་བ་ཞེས་བྱའོ། །

[Block 863]
བྱ་བ་དེ་དག་ཐམས་ཅད་མཐར་འབྱིན་པར་བྱེད་པ་ནི་ཡང་དག་པར་སྒྲོལ་བ་ཞེས་བྱའོ། །

[Block 864]
ཉོན་མོངས་པ་ཐམས་ཅད་ལས་ངེས་པར་འབྱུང་བ་ཞེས་བྱ་བ་ནི་ཏིང་ངེ་འཛིན་ལ་སེམས་རྩེ་གཅིག་ཏུ་བཞག་པས་ཉོན་མོངས་པ་ཐམས་ཅད་ཀྱང་སྤོང་བར་བྱེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 865]
གསང་སྔགས་དང་ཐོས་པ་འཛིན་པས་ངེས་པར་སེམས་པའི་ཤེས་རབ་ཀྱི་རྒྱུ་བསྐྱེད་པ༌[^759]ཞེས་བྱ་བ་ལ། ཆོས་ཀྱི་དོན་ཟབ་མོའམ། བསམ་གཏན་གྱི་མན་ངག་ཐོབ་པ་ཕྱིན་ཅི་མ་ལོག་པར་འཛིན་པ་ནི་གསང་སྔགས་དང་ཐོས་པ་འཛིན་པ་ཞེས་བྱའོ། །

[Block 866]
དེ་ལྟར་བཟུང་ནས་སེམས་ལ་བསམ་གཏན་དུ་བྱ་ཞིང་ངེས་པར་རྟོག་ནུས་པའི་ཤེས་རབ་ཀྱང་བྱམས་པ་ལས་འབྱུང་བས༌[^760]ཤེས་རབ་ཀྱི་རྒྱུ་བསྐྱེད་པ༌[^761]ཞེས་བྱའོ། །

[Block 867]
རང་གི་ཕྱོགས་དང་གཞན་གྱི་ཕྱོགས་ལ་ངེས་པ་ཞེས་བྱ་བ་ལ་རང་གི་ཕྱོགས་ནི་རྣམ་པར་བྱང་བའི་ཆོས་སོ། །

[Block 868]
གཞན་གྱི་ཕྱོགས་ནི་བདུད་དང་ཉོན་མོངས་པའི་ཕྱོགས་ཏེ། ངེས་པ་ནི་དེ་གཉིས་ལ་མཁས་ཤིང་དེ་གཉིས་བྱེ་བྲག་ཕྱེད་པའོ། །

[Block 869]
དེ་ལྟར་བྱེ་བྲག་ཕྱེད་ནས་བདུད་ཀྱི་ཕྱོགས་དང་ཉོན་མོངས་པ་ནི་སྤོང་བར་བྱེད། རྣམ་པར་བྱང་བའི་ཕྱོགས་རྣམས་ནི་འཕེལ་བར་བྱེད་པའི་ཕྱིར། བདུད་ཀྱི་ཕྱོགས་དང་ཉོན་མོངས་པ་རྣམས་བསལ་བ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 870]
བསྙེན་བཀུར་དང་འཇུག་པའི་རྒྱུ་མཐུན་པ་ལ་སེམས་ཞེས་བྱ་བ་ལ། བསྙེན་བཀུར་ནི་སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་ལ་སོགས་པ་ལ་བསྙེན་བཀུར་བྱེད་པའོ། །

[Block 871]
འཇུག་པས་ནི་ས་དང་བྱང་ཆུབ་ཀྱི་ཕྱོགས་ཀྱི་ཆོས་རྣམས་སྤྱོད་པ་ལ་ཞུགས་པ་སྟེ།[^762] བྱམས་པ་ནི་རྒྱུད་ལྟ་བུ་དག་དང་འདྲ་བ་ལས་བྱུང་བའི་འབྲས་བུ་ལ་སེམས་པས་ནི་རྒྱུ་མཐུན་པ་ལ་སེམས་པའོ།[^763] །སྤྱོད་ལམ་སྲུང་བར་བྱེད་ཅེས་བྱ་བ་ནི་བྱམས་པས་སྤྱོད་ལམ་ཐམས་ཅད་དུ་ཉོན་མོངས་པ་མི་འབྱུང་བར་བསྲུང་ཞིང་སྤྱོད་ལམ་མི་མཛེས་པ་རྣམས་མེད་པར་བྱེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 872]
རྒོད་པ་ཐམས་ཅད་ལས་འདས་པ་ཞེས་བྱ་བ་ནི་དབང་པོ་དང་། རྣམ་པར་ཤེས་པ་ཡུལ་ལ་མི་འཇུག་ཅིང་ཞི་བར་གནས་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 873]
ང་རྒྱལ་གྱི༌[^764]ལས་སེལ་བ་ཞེས་བྱ་བ་ནི་བྱམས་པས་ང་རྒྱལ་གྱི་རྒྱུ་ལས་བྱུང་བའི་ལས་མགོ་འཕང་བསྟོད་པ༌[^765]དང་། ལག་པ་བརྐྱང་བ་ལ་སོགས་པ་ཁེངས་པའི་མཚན་མ་རྣམས་མེད་པར་བྱེད་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 874]
ངོ་ཚ་ཤེས་པ་དང་ཁྲེལ་ཡོད་པས་བྱུགས་ཤིང་ཞེས་བྱ་བ་ལ། བདག་ལ་ལྟོས་ནས་སྡིག་པ་མི་དགེ་བའི་ཆོས་མི་བྱེད་པ་ནི་ངོ་ཚ་ཤེས་པའོ། །

[Block 875]
གཞན་ལ་ལྟོས་ནས་སྡིག་པ་མི་དགེ་བའི་ཆོས་མི་བྱེད་པ་ནི་ཁྲེལ་ཡོད་པ་སྟེ། ཆོས་དེ་དག་གཉིས་དང་ལྡན་པ་ནི་བྱུགས་པ་ཞེས་བྱའོ། །

[Block 876]
དྲི་ཞིམ་པོ་ནི་ངོ་ཚ་ཤེས་པ་དང་ཁྲེལ་ཡོད་པ་དང་ལྡན་པས༌[^766]ཁ་ན་མ་ཐོ་བ་དང་ལྡན་པ་མི་རིགས་པའི༌[^767]ཆོས་དེ་ལ་མེད་པའི་ཕྱིར་ཏེ། དེ་བས་ན་དྲི་ང་བ་སྦྱོང་བ༌[^768]ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 877]
ལས་བཤད་ཟིན་ཏོ།། །།

[Block 878 [HEADING]]
#### ཁྱད་པར། ^2-1-5-0

[Block 879]
ཁྱད་པར་བསྟན་པའི་ཕྱིར། བཙུན་པ་ཤ་ར་དྭ་ཏིའི་བུ་བྱམས་པ་ནི་སེམས་ཅན་ཐམས་ཅད་ཡོངས་སུ་སྐྱོབ་པ་སྟེ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། ཐམས་ཅད་སྐྱོབ་པ་ཞེས་བྱ་བའི་ཚིག་འདི་ནི་བསྟན་པའོ། །

[Block 880]
ལྷག་མ་རྣམས་ནི་ཇི་ལྟར་བྱམས་པ་སེམས་ཅན་ཐམས་ཅད་སྐྱོབ་པར་བྱེད་པའི་བཤད་པའོ། །
--- END BLOCKS ---
