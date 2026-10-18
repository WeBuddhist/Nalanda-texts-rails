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
དགོངས་པ་དང་ལྡེམ་པོར་དགོངས་པ་ལ་ཐ་དད་དུ་བྱ་བ་ཅི་ཡོད་ཅེ་ན། བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང༌[^567]ཐུགས་ལ་བཞག་པ་སྟོན་པར་མཛད་པ་དེ་ནི་དགོངས་པ་ཡིན་ནོ། །

[Block 842]
གང་ཉིད་ཀྱིས༌[^568]ངེས་པར་བསྟན་པ་ལ་འཇུག་པར་མཛད་པ་དེ་ནི་ལྡེམ་པོར་དགོངས་པ་ཡིན་ནོ། །

[Block 843 [HEADING]]
##### བཞུགས་པ་ལ་ལྡེམ་པོར་དགོངས་པ། ^2-19-2-1-0

[Block 844]
དེ་ལ་བཞུགས་པ༌[^569]ལ་ལྡེམ་པོར་དགོངས་པ་ནི་གང་དུ་གང་ཟག་དང་ཆོས་ཀྱི་ངོ་བོ་དང་། ཁྱད་པར་དུ་ཀུན་རྫོབ་ཀྱི་བདེན་པའི་ཚུལ་དུ་སེམས་ཅན་རྣམས་བཞུགས་པའི༌[^570]ཕྱིར་བསྟན་པ་ལ༌[^571]ནི་བཞུགས་པ༌[^572]ལ་ལྡམ་པོར༌[^573]དགོངས་པའོ། །

[Block 845 [HEADING]]
##### མཚན་ཉིད་ལ་ལྡེམ་པོར་དགོངས་པ། ^2-19-2-2-0

[Block 846]
དེ་ལ་མཚན་ཉིད་ལ་ལྡེམ་པོར་དགོངས་པ་ནི་གང་དུ་ཆོས་ཀྱི་མཚན་ཉིད་བསྟན་པར་བྱ་བ་དེར་ངོ་བོ་ཉིད་གསུམ་སྟོན་པའོ། །

[Block 847 [HEADING]]
##### གཉེན་པོ་ལ་ལྡེམ་པོར་དགོངས་པ། ^2-19-2-3-0

[Block 848]
གཉེན་པོ་ལ་ལྡེམ་པོར་དགོངས་པ་ནི་གང་དུ་སེམས་ཅན་རྣམས་ཀྱི་སྤྱོད་པའི་གཉེན་པོ་བསྟན་པ་སྟེ། སེམས་ཅན་རྣམས་ཉོན་མོངས་པའི་གཉེན་པོ་ལ་གནས་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 849 [HEADING]]
##### བསྒྱུར་བ་ལ་ལྡེམ་པོར་དགོངས་པ། ^2-19-2-4-0

[Block 850]
བསྒྱུར་བ་ལ་ལྡེམ་པོར་དགོངས་པ་ནི་གང་དུ་ཚིག་གི་དོན་གཞན་དུ་བརྗོད་ལ། དོན་དེ་ཉིད་གཞན་དུ་སྟོན་པ་སྟེ། དཔེར་ན་སྙིང་པོ་མེད་པ༌[^574]ལ་སྙིང་པོར་ཤེས།

[Block 851 [VERSE]]
ཕྱིན་ཅི་ལོག་ལ་ཤིན་ཏུ་གནས། །
ཉོན་མོངས་ཀུན་ནས་རབ་ཉོན་མོངས། །
བྱང་ཆུབ་དམ་པ་ཐོབ་པར་འགྱུར། །

[Block 852]
ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 853]
དེ་ལ་སྙིང་པོ་མེད་ཅེས་བྱ་བ་ནི་ཏིང་ངེ་འཛིན་ཏེ། འཕྲོ་བ་མེད་པ་ནི་སྙིང་པོ་མེད༌[^575]པའོ་ཞེས་བྱས་ནས་ཏེ། དེ་ལ་བླ་མའི་བློ་འབྱུང་བ་ནི་སྙིང་པོར་ཤེས་པའོ། །

[Block 854]
ཕྱིན་ཅི་ལོག་ལ་ཤིན་ཏུ་གནས། །ཞེས་བྱ་བ་ནི་མི་མཐུན་པ་ལ་རབ་ཏུ་གནས་ཞེས་བྱ་བའི་ཐ་ཚིག་སྟེ། མི་རྟག་པ་ལ་རྟག་པའོ་ཞེས་གང་ཕྱིན་ཅི་ལོག་པ་དེ་ནི་རྟག་པ་ལས་བཟློག་པའི་མི་རྟག་པ་ལ་རབ་ཏུ་གནས་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 855]
ཉོན་མོངས་ཀུན་ནས་རབ་ཉོན་མོངས། །ཞེས་བྱ་བ་ལ། ཉོན་མོངས་པ་ནི་ངལ་བ་སྟེ། དེ་ཉིད་ཀྱིས་ནི༌[^576]ཡུན་རིང་པོར་སེམས་ཅན་གྱི་དོན་ལ་རབ་ཏུ་ཉོན་མོངས་ཏེ། ཇི་ལྟར་ཉོན་མོངས་པར་གྱུར་ཀྱང་དུས་རིང་པོར་འཁོར་བ་ན་འདི་ལྟར་གནས་སོ་ཞེས་གསུངས་པ་ལྟ་བུའོ། །

[Block 856]
བྱང་ཆུབ་དམ་པ་ཐོབ་པར་འགྱུར། །ཞེས་བྱ་བའི་ཚིག་གི་དོན་ནི༌[^577]གོ་སླའོ། །

[Block 857 [HEADING]]
### ཆོས་རྣམས་བརྗོད་པའི་བག་ཆགས་ལས་འབྱུང་བ། ^2-20-0

[Block 858]
ཆོས་རྣམས་བརྗོད་པའི་བག་ཆགས་ལས་འབྱུང་སྟེ། དེ་དག་ཉིད་ལས་ཏེ་ཞེས་བྱ་བ་དེ་ལ་བརྗོད་པའི་བག་ཆགས་ལས་ཏེ། རྣམ་པར་རྟོག་པ་དང་ཕྱི་རོལ་གྱི་བག་ཆགས་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ལ་ཀུན་ཏུ་གནས་པའོ། །

[Block 859]
བག་ཆགས་དེ་ལས་བྱུང་བ་ནི་ཆོས་ཐམས་ཅད་དེ། གང་འཇུག་པའི་རྣམ་པར་ཤེས་པའི་ངོ་བོའོ། །

[Block 860]
དེ་དག་ཉིད་ལས་ཏེ་ཞེས་བྱ་བ་ནི་རྣམ་པར་རྟོག་པའི་བག་ཆགས་དེ་ཡང་ཆོས་ཀྱི་རྒྱུ་ལས་བྱུང་ངོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 861]
དེས་ནི་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་དང་འཇུག་པའི་རྣམ་པར་ཤེས་པ་དག་ཕན་ཚུན་གྱི་རྒྱུ་ཅན་དུ་བསྟན་ཏོ། །

[Block 862]
འཇུག་པའི་རྣམ་པར་ཤེས་པའི་མཚན་ཉིད་ཀྱི༌[^578]ཆོས་དེ་དག་ནི། རྒྱུ་མཚན་ལྟ་བ་དང་བཅས་པའི་རྣམ་པར་རིག་པའི་ངོ་བོ་ཉིད་དོ་ཞེས་བྱ་བ་ནི། གང་རྣམ་པར་རིག་པ་རྒྱུ་མཚན་དང་བཅས། ལྟ་བ་དང་བཅས་པ་དེའི་བདག་ཉིད་ཅན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 863]
དེ་དག་གི་མཚན་ཉིད་ཀྱང་རྣམ་པ་གསུམ་སྟེ་འདི་ལྟར་གནས་ཀྱི་མཚན་ཉིད་ཅེས་བྱ་བ་ནི་གཞན་གྱི་དབང་གི་མཚན་ཉིད་དོ། །

[Block 864]
དེ་ལྟར་བསྟན་པ་འདི་ནི་ངོ་བོ་ཉིད་གསུམ་གྱི་མཚན་ཉིད་བསྟན་པ་ཡིན་ནོ། །

[Block 865]
དེ་དག་གི་དོན་ཡང་ཚིགས་སུ་བཅད་པ་ཕྱེད་ཀྱིས་བསྟན་ཏེ།

[Block 866 [VERSE]]
རྒྱུ་མཚན་ལྟ་དང་བཅས་པ་ལས། །
དེ་དག་མཚན་ཉིད་གསུམ་ཤེས་བྱ། །

[Block 867]
ཞེས་བཤད་པ་ཇི་ལྟ་བ་བཞིན་དུ་བསྟན་པར་བྱའོ། །

[Block 868 [HEADING]]
### དེ་གཉི་ག་ཡོད་པ་དང་མེད་པ་མི་དམིགས་པའམ་དམིགས་པ། ^2-21-0

[Block 869]
དེ་གཉི་ག་ཡོད་པ༌[^579]དང་མེད་པ༌[^580]མི་དམིགས་པའམ། དམིགས་པའམ། དེ་ཁོ་ན་ཉིད་མ༌[^581]མཐོང་བ་དང་མཐོང་བ་དག་དུས་མཉམ་པ་ཉིད་དུ་ཞེས་བྱ་བ་ལ། དེ་གཉི་ག་ཙམ་ནི་ཀུན་ཏུ་བརྟགས་པ་དང་། ཡོངས་སུ་གྲུབ་པའོ། །

[Block 870]
དེ་གཉིས་ལས་གཅིག་ནི་མེད་པའོ། །

[Block 871]
གཉིས་པ་ནི་ཡོད་པ་སྟེ། དེས་ན་དེ་དག་གཉི་ག་མེད་པ་དང་ཡོད་པར་ཞེས་གསུངས་པ་ཡིན་ཏེ། གང་གི་ཕྱིར་དེ་ཁོ་ན་ཉིད་མ་མཐོང་བ་ལ་ནི་ཀུན་ཏུ་བརྟགས་པ་ཉེ་བར་དམིགས་ཤིང་ཡོངས་སུ་གྲུབ་པ་དམིགས་པར་མི་འགྱུར་རོ། །

[Block 872]
དུས་དེ་ཉིད་ན་དེ་ཁོ་ན་ཉིད་མཐོང་བ་ལ་ཀུན་ཏུ་བརྟགས་པ་ནི་མི་དམིགས་ལ་ཡོངས་སུ་གྲུབ་པ་ནི་དམིགས་པར་འགྱུར་རོ། །

[Block 873]
དོན་དེ་དག་ཉིད་ཚིགས་སུ་བཅད་པས་སྟོན་པ་ནི།

[Block 874 [VERSE]]
གཞན་དབང་ལ་ནི་བརྟགས་པ་མེད། །
ཅེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ།
དེ༌[^582]ཕྱིར་དེ་ལ་གཉི་ག་མཉམ། །

[Block 875]
ཞེས་བྱ་བ་ལ། མཉམ་པ་ཞེས་བྱ་བ་ནི་དུས་གཅིག་ཏུའོ། །

[Block 876]
དེ་ལ་ཞེས་བྱ་བ་ནི་གཞན་གྱི་དབང་དེ་ལའོ། །

[Block 877]
གཉི་ག་ཞེས་བྱ་བ་ནི་དེ་ཁོ་ན་ཉིད་མཐོང་བ་དང་། མ་མཐོང་བ་དག་གོ། །

[Block 878]
དེ་ཕྱིར་ཞེས་བྱ་བ་ནི་རྒྱུ་དེས་ན་ཞེས་བྱ་བའི་ཐ་ཚིག་སྟེ་འདི་ལྟར་གཞན་གྱི་དབང་ལ་ཀུན་ཏུ་བརྟགས་པ་ནི་མེད་ལ། ཡོངས་སུ་གྲུབ་པ་ནི་ཡོད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 879 [HEADING]]
### སྔར་བསྟན་པའི་ཚིག་གི་དོན་ཚིག་གི་ལྷག་མས་སྟོན་པ། ^2-22-0

[Block 880 [HEADING]]
#### ཤིན་ཏུ་རྣམ་པར་དག་པའི་བློ་མངའ་བ། ^2-22-1-0
--- END BLOCKS ---
