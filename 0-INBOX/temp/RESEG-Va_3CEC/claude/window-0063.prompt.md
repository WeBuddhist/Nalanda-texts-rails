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
[Block 2206]
ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་ལ་གནས་པ་ནི་དེ་ལ་དམིགས་པའི་སྒོ་ནས་གནས་པའོ། །

[Block 2207]
ཡེ་ཤེས་དང་ལྡན་པ་ཐམས་ཅད་རྟོན་པ་ཡིན་ཞེས་པ་ནི་ཡེ་ཤེས་ཀྱི་ཚོགས་ཏེ། ཤེས་པ་དང་ལྡན་པའི་སེམས་ཅན་ཐམས་ཅད་ཀྱི་རྟོན་པ་ཡིན་ཏེ། དེ་ལ་བརྟེན་ཞིང་འདྲིས་པར༌[^1903]བྱེད་པའི་གནས་ཡིན་ཞེས༌[^1904]པའི་དོན་ཏོ། །

[Block 2208]
བདུད་ཐམས་ཅད་ཀྱིས་ཀྱང་ཞེས་བྱ་བ་ནི་ཡེ་ཤེས་ཀྱི་ཚོགས་དང་ལྡན་པ་དེ་ལ་བདུད་ཐམས་ཅད་ཀྱིས་བར་ཆད་བྱ་བའི་སྐབས་མི་རྙེད་པར་འགྱུར་རོ། །

[Block 2209]
དེ་ལ་སངས་རྒྱས་ཀྱི་ཆོས་ཞེས་བྱ་བ་ནི་ཡེ་ཤེས་ཀྱི་ཚོགས་དང་ལྡན་པའི་གང་ཟག་དེ་སངས་རྒྱས་ཀྱི་ཆོས་ཐམས་ཅད་ཀྱི་སྣོད་དུ་འགྱུར་བའོ། །

[Block 2210]
སངས་རྒྱས་ཀྱི༌[^1905]བྱིན་གྱི་རླབས༌[^1906]ཞེས་བྱ་བ༌[^1907]ནི་ཡོན་ཏན་ལས་མི་ཉམས་པར་སངས་རྒྱས་ཀྱིས་བྱིན་གྱིས་བརླབ་པར་མཛད་པའོ། །

[Block 2211]
ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་ཀྱང་ཐོབ་པར་བྱེད་དེ་ཞེས་བྱ་བ་ནི་ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་འཐོབ་པར་འགྱུར་བའི་རྒྱུ་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 2212]
ཡེ་ཤེས་ཀྱི་ཚོགས་མི་ཟད་པ་བཤད་ཟིན་ཏོ།། །།

[Block 2213 [HEADING]]
## བསྒོམ་པ་ལ་རབ་ཏུ་ཞུགས་པའི་བྱང་ཆུབ་སེམས་དཔའ། ^8-0

[Block 2214]
བསྒོམ་པ་ལ་རབ་ཏུ་ཞུགས་པའི་བྱང་ཆུབ་སེམས་དཔའ་ནི་བཞི་བཅུར་གཅིག་མེད་པས་བཤད་དེ། རང་གི༌[^1908]གནས་དང་ཤིན་ཏུ་ཚོར་བ་དང་ཤིན་ཏུ་གནས་པ་དང་ཤིན་ཏུ་རྣམ་པར་བྱང་བ༌[^1909]དང་། བརྩོན་འགྲུས་ཤིན་ཏུ་གཉེན་པོར་གྱུར་པ་དང་། བརྩོན་འགྲུས་ཤིན་ཏུ་སྦྱངས་པ་དང་། བརྩོན་འགྲུས་ཐོབ་པ་དང་། བརྩོན་འགྲུས་ཤིན་ཏུ་བརྟན་པ༌[^1910]དང་། མོས་པ་ལ་ཤིན་ཏུ་གནས་པའི་བརྩོན་འགྲུས་དང་། བརྩོན་འགྲུས་ལ་ཤིན་ཏུ་གནས་པ་དང་། སེམས་ལ་ཤིན་ཏུ་གནས་པ་དང་། དཔྱོད་པ་ལ་ཤིན་ཏུ་གནས་པ་དང་། དད་པའི་མཆོག་དང་། བརྩོན་འགྲུས་ཀྱི་མཆོག་དང་། དྲན་པའི་མཆོག་དང་། ཏིང་ངེ་འཛིན་གྱི་མཆོག་དང་། ཤེས་རབ་ཀྱི་མཆོག་དང་། དད་པ་མི་ཚུགས་པ་དང་། བརྩོན་འགྲུས་མི་ཚུགས་པ་དང་། དྲན་པ༌[^1911]མི་ཚུགས་པ་དང་། ཏིང་ངེ་འཛིན་མི་ཚུགས་པ་དང་། ཤེས་རབ་མི་ཚུགས་པ་དང་། དྲན་པ་ཤིན་ཏུ་འབྲེལ་པ་དང་། རབ་ཏུ་ཤེས་པ་ཤིན་ཏུ་འབྲེལ་པ་དང་། བརྩོན་འགྲུས་ཤིན་ཏུ་འབྲེལ་པ་དང་། དགའ་བ་ཤིན་ཏུ་འབྲེལ་པ་དང་། བག་ཡངས༌[^1912]ཤིན་ཏུ་འབྲེལ་པ་དང་། ཏིང་ངེ་འཛིན་ཤིན་ཏུ་འབྲེལ་པ་དང་། བཏང་སྙོམས་ཤིན་ཏུ་འབྲེལ་པ་དང་། རྣམ་པར་མི་རྟོག་པ་དང་། ཤིན་ཏུ་རྟོག་པ༌[^1913]དང་། དུལ་བ་དང་། ཞི་བ་དང་། རབ་ཏུ་ཞི་བ་དང་། ཤིན་ཏུ་འབྱུང་བ་དང་། དགའ་བ་དང་ལྡན་པ་དང་། མཐུ་ཆེ་བ་དང་། བསྡུས་པའི་རྣལ་འབྱོར་ལ་ཞུགས་པ་དང་། སྤྲོས་པའི་རྣལ་འབྱོར་ལ་ཞུགས་པའོ། །

[Block 2215 [HEADING]]
### དྲན་པ་ཉེ་བར་གཞག་པ་བཞི་བསྒོམ་པ་མི་ཟད་པ། ^8-1-0

[Block 2216]
དེ་ལ་རང་གི་གནས་དང་། ཤིན་ཏུ་ཚོར་བ་དང་། ཤིན་ཏུ་གནས་པ་དང་། ཤིན་ཏུ་རྣམ་པར་བྱང་བའི༌[^1914]དབང་དུ་བྱས་ནས། བཙུན་པ་ཤ་ར་དྭ༌[^1915]ཏིའི་བུ་གཞན་ཡང་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2217]
འདིར་ཡང་བསྟན་པ་དང་བཤད་པའི་ཚུལ་དུ་རིག་པར་བྱ་སྟེ། དེ་ལ་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི༌[^1916]དྲན་པ་ཉེ་བར་གཞག་པ༌[^1917]བཞི་བསྒོམ་པ་ཡང་མི་ཟད་པ་སྟེ། བཞི་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་བསྟན་པའི་ཚུལ་ལ། །ལྷག་མ་རྣམས་ནི་བཤད་པའི་ཚུལ་ལོ། །

[Block 2218]
བྱང་ཆུབ་ཀྱི་ཕྱོགས་ཀྱི་ཆོས་སུམ་ཅུ་རྩ་བདུན་ལ༌[^1918]དྲན་པ་ཉེ་བར་གཞག་པ༌[^1919]བཞི་ནས་སྟོབས་ལྔའི་བར་གྱིས་ནི་མཐོང་བའི་ལམ་ལ་སྦྱོར་བར་བྱེད་པ་ཡིན་པས་བསྡུས་པའི་དོན་སྦྱོར་བའི་ལམ་བསྟན་པར་སྦྱར་རོ། །

[Block 2219]
གཞན་ཡང་ཞེས་བྱ་བ་ནི་གོང་དུ་བཤད་པར་ཟད་དོ། །

[Block 2220]
བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱིས་བསྒོམ་པར་བྱ་བའི་དྲན་པ་ཉེ་བར་གཞག་པ་ནི་དྲན་པ་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི༌[^1920]ཉེ་བར་གཞག་པ་སྟེ། དྲན་པ་ནི་ཤེས་རབ་པོ། །ཉེ་བར་གཞག་པ༌[^1921]ནི་ཏིང་ངེ་འཛིན་ཏོ། །

[Block 2221]
དེ་གཉིས་ཀྱིས༌[^1922]བསྒོམ་པའི་ཡུལ་བཞི་ཡོད་པས་དྲན་པ་ཉེ་བར་གཞག་པ༌[^1923]བསྒོམ་པའོ། །

[Block 2222]
དེ་དག་བསྒོམ་པ་མི་ཟད་པ་ཡང་སེམས་ཅན་རྣམས་ཀྱི་ལུས་དང་། ཚོར་བ་དང་། སེམས་དང་ཆོས་རྣམས་མི་ཟད་པའི་ཕྱིར་དེ་སྒོམ་པར༌[^1924]བྱེད་པའི་དྲན་པ་ཉེ་བར་གཞག་པ་ཡང་མི་ཟད་པའོ། །

[Block 2223 [HEADING]]
#### ལུས་དྲན་པ་ཉེ་བར་གཞག་པ། ^8-1-1-0

[Block 2224]
དེ་ལ་རང་གི་གནས་ཀྱི་བྱང་ཆུབ་སེམས་དཔའ་གང་ཞེ་ན། ལུས་དྲན་པ་ཉེ་བར་གཞག་པ་ལ་རབ་ཏུ་ཞུགས་པ་ཡིན་ཏེ། ལུས་ཐམས་ཅད་དང༌[^1925]ཡང་བྲལ་བར་གྱུར་ལ། མཚན་དང་དཔེ་བྱད་ཀྱི་ལུས་ཀྱང་རྫོགས་པར་བྱེད་པའོ། །

[Block 2225]
དེའི་དབང་དུ་བྱས་ནས། དེ་ལ་བྱང་ཆུབ་སེམས་དཔའི༌[^1926]ལུས་ལ་ལུས་ཀྱི་རྗེས་སུ་ལྟ་བའི་དྲན་པ་ཉེ་བར་གཞག་པ༌[^1927]ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2226]
གང་གོང་དུ་མདོར་སྨོས་པ་དེ་ནི་འདི་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན༌[^1928]ཏོ། །

[Block 2227 [HEADING]]
##### ལུས། ^8-1-1-1-0

[Block 2228]
དེ་ལ་ལུས་ནི་གང་། ལུས་ལ་ལུས་ཀྱི་རྗེས་སུ་ལྟ་བ་ནི་གང་། དྲན་པ་ནི་གང་། དྲན་པ་ཉེ་བར་གཞག་པ༌[^1929]ནི་གང་ཞེ་ན། སྨྲས་པ་ལུས་ནི་རྣམ་པ༌[^1930]སུམ་ཅུ་རྩ་ལྔ་ཡོད་དེ། འདི་ལྟ་སྟེ། ནང་གི་དང་ཕྱི་རོལ་གྱི་དང་། དབང་པོས་ཟིན་པ་དང་། དབང་པོས་ཟིན་པ་མ་ཡིན་པ་དང་། སེམས་ཅན་དུ་བགྲང་བ་དང་། སེམས་ཅན་དུ་བགྲང་བ་མ་ཡིན་པ་དང་། གནས་ངན་ལེན་དང་ལྡན་པ་དང་། ཤིན་ཏུ་སྦྱངས་པ་དང་ལྡན་པ་དང་། འབྱུང་བའི་ལུས་དང་། འབྱུང་བ་ལས་གྱུར་པའི་ལུས་དང་། མིང་གི༌[^1931]ལུས་དང་། གཟུགས་ཀྱི་ལུས་དང་། སེམས་ཅན་དམྱལ་བ་པ་དང་། དུད་འགྲོའི་སྐྱེ་གནས་པ་དང་། ཡི་དགས་ཀྱི་ཡུལ་དང་། མིའི་དང་། ལྷའི་དང་། རྣམ་པར་ཤེས་པ་དང་བཅས་པ་དང་། རྣམ་པར་ཤེས་པ་མེད་པ་དང་། ནང་གི་ལུས་དང་། ཕྱི་རོལ་གྱི་ལུས་དང་། ཡོངས་སུ་གྱུར་པ་དང་། ཡོངས་སུ་མ་གྱུར་པ་དང་། བུད་མེད་ཀྱི་ལུས་དང་། སྐྱེས་པའི་ལུས་དང་། མ་ནིང་གི་ལུས་དང་། མཛའ་བཤེས་ཀྱི་ལུས་དང་། དགྲ་བོའི་ལུས་དང་། ཐ་མལ་པའི་ལུས་དང་། ལུས་ངན་པ་དང་། ལུས་འབྲིང་དང་། ལུས་བཟང་པོའི་ལུས་དང་། གཞོན་ནུའི་ལུས་དང་། ལང་ཚོའི་ལུས་དང་། རྒན་པོའི་ལུས་ཏེ། དེ་ནི་རེ་ཞིག་ལུས་ཀྱི་རབ་ཏུ་དབྱེ་བ་ཡིན་ནོ། །

[Block 2229 [HEADING]]
##### ལུས་ལ་ལུས་ཀྱི་རྗེས་སུ་ལྟ་བ། ^8-1-1-2-0

[Block 2230]
དེ་ལ་རྗེས་སུ་ལྟ་བ་ནི་རྣམ་པ་གསུམ་སྟེ།[^1932] ལུས་ཀྱི་དབང་དུ་བྱས་ནས་ཐོས་པ་ལས་བྱུང་བ་དང་། བསམས་པ༌[^1933]ལས་བྱུང་བ་དང་། བསྒོམས་པ༌[^1934]ལས་བྱུང་བའི་ཤེས་རབ་གང་ཡིན་པ་སྟེ། ཤེས་རབ་དེས་ལུས་ཐམས་ཅད་ལ་རྣམ་པ་ཐམས་ཅད་དུ་ཡང་དག་པ་ཁོ་ནར་ཉེ་བར་རྟོག་པར་བྱེད་ཅིང་། ཀུན་ཏུ་རྟོག་པར་བྱེད། རྗེས་སུ་འཇུག་པར་བྱེད། རྗེས་སུ་རྟོག་པར་བྱེད་པའོ།[^1935] །

[Block 2231 [HEADING]]
##### དྲན་པ། ^8-1-1-3-0

[Block 2232]
དེ་ལ་དྲན་པ་ནི་དེས་ལུས་ཀྱི་དབང་དུ་བྱས་ནས་ཆོས་གང་དག་གཟུང་བའི༌[^1936]ཆོས་ད་དག་ཁོ་ནའི་དོན་བསམ་པ༌[^1937]གང་ཡིན་པ་དང་། གང་དག་བསྒོམས་པས༌[^1938]མངོན་སུམ་དུ་བྱ་བའི༌[^1939]ཚིག་འབྲུ་དང་། དོན་དང་མངོན་སུམ་དུ་བྱས་པ་དེ་སེམས་ཀྱིས་མི་བརྗེད་པ༌[^1940]གང་ཡིན་པའོ། །

[Block 2233 [HEADING]]
##### དྲན་པ་ཉེ་བར་གཞག་པ། ^8-1-1-4-0

[Block 2234]
དེ་ལ་དྲན་པ་ཉེ་བར་གཞག་པ༌[^1941]ནི་བདག་གི༌[^1942]ཆོས་དེ་དག་ལེགས་པར་གཟུང༌[^1943]ངམ། འོན་ཏེ་མ་ཡིན། ཤེས་རབ་ཀྱིས༌[^1944]དེ་དང་དེ་དག་ལ༌[^1945]ལེགས་པར་བརྟགས༌[^1946]སམ་འོན་ཏེ་མ་ཡིན། རྣམ་པར་གྲོལ་བ་དེ་དང་དེ་དག་ལེགས་པར་རེག་པར་བྱས་སམ། འོན་ཏེ་མ་ཡིན་ཞེས་དྲན་པ་ཉེ་བར་གཞག་པ༌[^1947]ཡིན་ཏེ། དེ་ནི་དྲན་པ་ཉེ་བར་གཞག་པ༌[^1948]ཡིན་ནོ། །

[Block 2235 [HEADING]]
###### དྲན་པ་ཀུན་དུ་བསྲུང་བ། ^8-1-1-4-1-0

[Block 2236]
གཞན་ཡང་དྲན་པ་ཀུན་དུ་བསྲུང༌[^1949]བ་དང་། ཡུལ་གྱི་ཀུན་ནས་ཉོན་མོངས་པ་མེད་པ་དང་། དམིགས་པ་ལ་ཉེ་བར་གཏོད་པའི་ཕྱིར་དྲན་པ་ཉེ་བར་འཇོག་པ་ཡིན་ཏེ། དེ་ལ་དྲན་པ་ཀུན་དུ་བསྲུང་བ་ནི་དྲན་པ་ཀུན་དུ་བསྲུང་པ་དང་། དྲན་པ་ལ་རྟག་འགྲུས་མེད་པ་ཡིན་ནོ། །

[Block 2237 [HEADING]]
###### ཡུལ་གྱི་ཀུན་ནས་ཉོན་མོངས་པ་མེད་པ། ^8-1-1-4-2-0

[Block 2238]
དེ་ལ་ཡུལ་གྱི་ཀུན་ནས་ཉོན་མོངས་པ་མེད་པ་ནི་དྲན་པས་ཡིད་ཀུན་དུ་བསྲུང་བ་དང་། གནས་སྐབས་མཉམ་པ་ལ་འཇོག་པར་བྱེད་པ་དང་། མཚན་མར་མི་འཛིན་པ་དང་། མངོན་རྟགས་སུ་མི་འཛིན་པ་དང་། ཡིད་ཀྱི་དབང་པོ་བསྲུང་བ་དང་། ཡིད་ཀྱི་དབང་པོས་ཀྱང་སྡོམ་པ་སྒྲུབ་པར་བྱེད་པ་ཡིན་ནོ། །

[Block 2239 [HEADING]]
###### དམིགས་པ་ལ་ཉེ་བར་གཏོད་པ། ^8-1-1-4-3-0

[Block 2240]
དེ་ལ་དམིགས་པ་ལ་ཉེ་བར་གཏོད་པ་ནི་དམིགས་པ་རྣམ་པ་བཞི་པོ་འདི་ལྟ་སྟེ། ཁྱབ་པའི་དམིགས་པ་དང་། དཔྱོད་པ༌[^1950]རྣམ་པར་སྦྱོང་བའི་དམིགས་པ་དང་། མཁས་པའི་དམིགས་པ་དང་། ཉོན་མོངས་པ་རྣམ་པར་སྦྱོང་བའི་དམིགས་པ་ལ༌[^1951]དྲན་པ་ཉེ་བར་གཏོད་པ་ཡིན་ཏེ། རྒྱུ་གསུམ་པོ་དེ་དག་གིས་དྲན་པ་ལེགས་པར་ཉེ་བར་གཞག་པ༌[^1952]ཉིད་གང་ཡིན་པ་དེ་ནི་དྲན་པ་ཉེ་བར་གཞག་པ་ཞེས་བྱའོ། །

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
--- END BLOCKS ---
