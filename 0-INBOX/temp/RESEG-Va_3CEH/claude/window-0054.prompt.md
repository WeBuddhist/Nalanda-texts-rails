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
[Block 1891]
ཡང་ལོངས་སྤྱོད་རྫོགས་པ་དེ་ནི་གཅིག་ཉིད་ཡིན་ན་ཡང་གཞན་དང་གཞན་དུ་མཐོང་བར་འགྱུར་ལ། ཡང་དེ་ཉིད་ཁོ་ན་དེ་ལས་ཀྱང་གཞན་དུ་མཐོང་བར་འགྱུར་བས་དེ་ནི་གཡོ་བའི་ངོ་བོའི་ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར་ངོ་བོ་ཉིད་ཀྱི་སྐུ་ཡིན་པར་མི་རིགས་ཏེ། དེའི་ཕྱིར་ན་ཡང་ངོ་བོ་ཉིད་ཀྱི་སྐུ་མ་ཡིན་ནོ། །

[Block 1892 [HEADING]]
#### འཁོར་དང་རྟག་ཏུ་འདྲེས་པ། ^9-9-5-0

[Block 1893]
ཡང་ལོངས་སྤྱོད་རྫོགས་པ་དེ་ནི་ལྷ་ལ་སོགས་པའི་འཁོར་དང་རྟག་ཏུ་འདྲེས་ཤིང་བསྐོར་ནས་གནས་པ་ཡིན་གྱི། ངོ་བོ་ཉིད་ནི་འདྲེས་པར་མི་འགྱུར་ཏེ། དེའི་ཕྱིར་ན་ཡང་ངོ་བོ་ཉིད་ཀྱི་སྐུ་མ་ཡིན་ནོ། །

[Block 1894 [HEADING]]
#### ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ཡོངས་སུ་གྱུར་པ། ^9-9-6-0

[Block 1895]
གང་ཡང་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ཡོངས་སུ་གྱུར་པ་ནི་ངོ་བོ་ཉིད་ཡིན་ལ། གལ་ཏེ་དེ་དག་ངོ་བོ་ཉིད་གཅིག་པ་ཉིད་ཡིན་ན་དེ་ནི་ལོངས་སྤྱོད་རྫོགས་པ་ཡང་ཡིན་པས་འཇུག་པ༌[^1098]རྣམ་པར་ཤེས་པ་ཡོངས་སུ་གྱུར་པ་ལས་སྐུ་གང་མངོན་པར་འགྲུབ་པར་འགྱུར། དེའི་ཕྱིར་ན་ཡང་ལོངས་སྤྱོད་རྫོགས་པ་ནི་ངོ་བོ་ཉིད་མ་ཡིན་ཏེ། རྣམ་པ་དྲུག་པོ་དེ་དག་མི་རིགས་པའི་ཕྱིར་ན་ཡང་མི་རུང་ངོ་། །

[Block 1896 [HEADING]]
### སྤྲུལ་པའི་སྐུ་ངོ་བོ་ཉིད་ཀྱི་སྐུ་མ་ཡིན་པ། ^9-10-0

[Block 1897]
ད་ནི་གང་གི་ཕྱིར་སྤྲུལ་པའི་སྐུ་ངོ་བོ་ཉིད་ཀྱི་སྐུ་མ་ཡིན་པའི་ཚུལ་དེ་བསྟན་པར་བྱ་སྟེ། རྒྱུ་བརྒྱད་ཀྱི་ཕྱིར་རོ། །

[Block 1898]
དེ་ལ་རེ་ཞིག་མི་རིགས་པ་དང་པོ་ནི་བྱང་ཆུབ་སེམས་དཔའ་ཡུན་རིང་པོ་ནས་བསྐལ་པ་དུ་མར་ཡང་མི་མཉམ་པའི༌[^1099]ཏིང་ངེ་འཛིན་ཐོབ་པ་རྣམས་ནི་དགའ་ལྡན་གྱི་ལྷ་རྣམས་ཀྱི་ནང་དུ་ཡང་སྐྱེ་བར་མི་རིགས་ན་མི་རྣམས་ཀྱི་ནང་དུ་ལྟ་སྨོས་ཀྱང་ཅི་དགོས་ཏེ། སྤྲུལ་པ་དེ་ནི་ཡང་འཇིག་རྟེན་པ་ཡང་ཡིན་ནོ། །

[Block 1899]
ཡང་བྱང་ཆུབ་སེམས་དཔའ་སྐྱེ་བ་དྲན་པ་རྣམས་ནི་ཡི་གེ་དང་། རྩིས་དང་། གྲངས་ལ་སོགས་པ་མི་མཁྱེན་པ་ནི་མི་རིགས་ཏེ། དེའི་ཕྱིར་ན་ཡང་སྤྲུལ་པ་ཉིད་སེམས་ཅན་དེ་རྣམས་གདུལ་བའི་དོན་དུ་བྱུང་བ་ཡིན་ནོ། །

[Block 1900]
ཡང་བསྐལ་པ་གྲངས་མེད་པ་གསུམ་དུ་བྱང་ཆུབ་སེམས་དཔའ༌[^1100]བསྒྲུབས་པར་གྱུར་ཀྱང་ཉེས་པར་བཤད་པ་དང་། ལེགས་པར་བཤད་པའི་ཆོས་དེ་དག་རྣམ་པར་མ་མཁྱེན་ན་ཡང་། དེ་ལས་གཞན་པ་མངོན་པར་རྫོགས་པར་བྱང་ཆུབ་པའི་དུས་ན་མཁྱེན་པར་འགྱུར་བས་དེའི་ཕྱིར་ན་ཡང་སྤྲུལ་པ་ནི་ངོ་བོ་ཉིད་ཀྱི་སྐུ་མ་ཡིན་ནོ། །

[Block 1901]
ཡང་འཛམ་བུའི་གླིང་བྱེ་བ་ཕྲག་བརྒྱ་བོར་ཏེ། གཅིག་ཏུ་མངོན་པར་རྫོགས་པར་བྱང་ཆུབ་པ་དང་། ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་བར་མི་རིགས་པས། སྤྲུལ་པ་ཡིན་པར་མི་རིགས་ཏེ། གང་གི་ཕྱིར་དེ་དག་ཐམས་ཅད་ཀྱིས་སྤྲུལ་པ་མཐོང་བར་མཐུན་པའི་ཕྱིར་རོ། །

[Block 1902]
གལ་ཏེ་གཅིག་ཏུ་མངོན་པར་རྫོགས་པར་བྱང་ཆུབ་ནས་གཞན་དག་ཏུ་སྤྲུལ་པ་རྣམས་འབྱུང་བར་མཛད་པ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཕྱོགས་ལེན་པར་བྱེད་པ་ཡིན་ན་ཡང་། དེ་ལྟ་ན་དགའ་ལྡན་ཉིད་ན་གནས་བཞིན་དུ། གླིང་བཞི་པ་ཐམས་ཅད་དུ་སྤྲུལ་པ་འགྱེད་པར་ཅིའི་ཕྱིར་མི་འདོད། ཡང་ལ་ལ་འདི་སྐད་དུ། སངས་རྒྱས་ཀྱི་ཞིང་དུ་གཏོགས་པའི་གླིང་བཞི་པ་ལ་ལ་ན་སངས་རྒྱས་མ་མཐོང་ངོ་ཞེས་ཟེར་ན། གླིང་བཞི་པ་ཐམས་ཅད་ན་མངོན་པར་རྫོགས་པར་བྱང་ཆུབ་པ་མེད་པ་ལ་ནི་ཡང་ལུང་དང་རིགས་པ་མེད་དོ། །

[Block 1903]
གལ་ཏེ་དེ་ལྟ་ཡིན་ན་མདོ་དང་འགལ་ཏེ། མདོ་ལས་ཀྱང་། སངས་རྒྱས་གཉིས་འབྱུང་བར་མི་འགྱུར་ཏེ། འཁོར་ལོས་སྒྱུར་བའི་རྒྱལ་པོ་གཉིས་མི་འབྱུང་བ་ཡིན་ནོ། །

[Block 1904]
ཞེས་གསུངས་པས་སོ་ཞེ་ན། གང་གི་ཕྱིར་འདི་ལྟར་འཁོར་ལོས་སྒྱུར་བའི་རྒྱལ་པོ་གཉིས་མི་འབྱུང་ངོ་ཞེས་འབྱུང་བ་དེ་ནི། གླིང་བཞི་པ་གཅིག་ཏུ་མི་འབྱུང་བ་ཡིན་གྱི། ཡང་སངས་རྒྱས་ཀྱི་ཞིང་དུ་ནི་མ་ཡིན་ནོ། །

[Block 1905]
དེ་བཞིན་དུ་སངས་རྒྱས་གཉིས་མི༌[^1101]འབྱུང་བ་ཡང་གླིང་བཞི་པ་གཅིག་ཏུ་མི་རིགས་ཀྱི། འདི་ལྟར་འཇིག་རྟེན་གྱི་ཁམས་གཅིག་ཏུ་ནི་འདོད་དོ། །

[Block 1906 [HEADING]]
### མངོན་པར་རྫོགས་པར་བྱང་ཆུབ་པ་ཚིགས་སུ་བཅད་པས་བསྟན་པ། ^9-11-0

[Block 1907]
ད་ནི་མངོན་པར་རྫོགས་པར་བྱང་ཆུབ་པ་ཚིགས་སུ་བཅད་པས་བསྟན་པར་བྱ་བ་ནི། སངས་རྒྱས་རྣམ་འཕྲུལ་ཞེས་བྱ་བ་ལ་སོགས་པ་རྒྱས་པར་འབྱུང་བ་སྟེ།

[Block 1908]
དོན་ནི་དུས་གང་གི་ཚེ་དགའ་ལྡན་ན་བཞུགས་པ་ལས།

[Block 1909]
སངས་རྒྱས༌[^1102]མངལ་དུ་གཤེགས་པ་དེ་བཞིན་དུ་དུས་དེ་ཉིད་ཀྱི་ཚེ་ན། གནས་བརྟན་ཤཱ་རིའི་བུ་ལ་སོགས་པ་འཁོར་འདི་དག་ཀྱང་དེ་བཞིན་དུ་སྤྲུལ་པའི་གནས་སྐབས་ཀྱིས་དེ་དང་དེར་བཞུགས་པར་བལྟ་བར་བྱའོ། །

[Block 1910]
དེ་དག་རྣམ་པར་གཞག་པས་ཀྱང་དེ་ལྟར་བྱས་ན་རྣམ་པ་ཐམས་ཅད་མངོན་པར་རྫོགས་པར་བྱང་ཆུབ་པར་བསྟན་པར་བྱའོ། །

[Block 1911 [HEADING]]
### གཏན་དུ་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་མི་རིགས་པ། ^9-12-0

[Block 1912]
ད་ནི་གཏན༌[^1103]དུ་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་མི་རིགས་པར་བསྟན༌[^1104]པར་བྱ་སྟེ། [^1105]སེམས་ཅན་ཐམས་ཅད་ཀྱི་དོན་དུ་སྨོན་ལམ་བཏབ་པ༌[^1106]བྱས་པ་དང་། སེམས་ཅན་གྱི་དོན་དུ་སྒྲུབ་པ་ཉིད་བྱས་པ་ཇི་ལྟར་སེམས་ཅན་གྱི་དོན་བྱའོ་ཞེས་བྱ་བ་ལྟ་བུར་བྱས་པའོ། །

[Block 1913]
གལ་ཏེ་གཏན༌[^1107]དུ་མྱ་ངན་ལས་འདའ་བས་མྱ་ངན་ལས་འདས་པ་ཡིན་ན་གང་སྨོན་ལམ་བཏབ་པ་དང་། སྒྲུབ་པ་དག་འབྲས་བུ་མེད་པར་འགྱུར་རོ། །

[Block 1914 [HEADING]]
### རྟག་པའི་སྐུ། ^9-13-0

[Block 1915]
གང་ཡང་དེ་བཞིན་གཤེགས་པའི་རྟག་པའི་སྐུ་ཡིན་ནོ་ཞེས་བྱ་བ་དེ་ལོངས་སྤྱོད་རྫོགས་པ་དང་། སྤྲུལ་པ་དག༌[^1108]མི་རྟག་པ་ཡིན་པའི་ཕྱིར། ཇི་ལྟར༌[^1109]རྟག་པའི་སྐུ་ཡིན་ཞེ་ན། དེ་བསྒྲུབ་པར་བྱ་སྟེ། དེ་དག་ཉིད་རྟག་པ་ཉིད༌[^1110]ཡིན་ཏེ། གང་གི་ཕྱིར་རྟག་པའི་སྐུ་ཆོས་ཀྱི་སྐུ་ལ་བརྟེན་པའི་ཕྱིར་དེས་ན་རྟག་པ་ཡིན་ནོ། །

[Block 1916]
ཡང་ལོངས་སྤྱོད་རྫོགས་པ་ནི་རྫོགས་པའི་ལོངས་སྤྱོད་དེ་ལ་རྒྱུན་ཆད་པ་མེད་པའི་ཕྱིར་རྟག་པ་ཡིན་ནོ། །

[Block 1917]
སྤྲུལ་པ་ཡང་མངོན་པར་རྫོགས་པར་བྱང་ཆུབ་པ་དང་། ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་སྟོན་པའི་རྒྱུན་ཆད་པ་མེད་པས་རྟག་པ་ཡིན་ནོ། །

[Block 1918]
དེ་དག་གཉི་ག་ཡང་རྟག་པ་ཉིད་ཡིན་པའི་དཔེ་བསྟན་པ་ནི། ཇི་ལྟར་ན་འཇིག་རྟེན་ན་རྟག་ཏུ་བདེ་བ་ལ་སྤྱོད་དོ་ཞེས་བརྗོད་པ་ལྟ་བུ་སྟེ། དེ་ནི་རྟག་ཏུ་རྒྱུན་མི་འཆད་པར་བྱེད་པར་འགྱུར་བ་ནི་མ་ཡིན་ནོ། །

[Block 1919]
འོན་ཀྱང་རྟག་ཏུ་བདེ་བ་ལ་སྤྱོད་དོ་ཞེས་ནི་རྗོད་པར་བྱེད་དོ། །

[Block 1920]
ཡང་གང་དག་འདི་ནི་རྟག་ཏུ་སློང༌[^1111]མོ་སྦྱིན་པ་ཡིན་ནོ་ཞེས་ཟེར་ན། ཡང་དེ་ནི་རྟག་ཏུ་སྦྱིན་པ་ནི་མ་ཡིན་ཏེ། རེས་འགའ་ཞིག་སྦྱིན་པར་བྱེད་པ་ཡིན་ན་ཡང་། འོན་ཀྱང་རྟག་ཏུ་སློང༌[^1112]མོ་སྦྱིན་པ་པོ་ཡིན་ནོ་ཞེས་རྗོད་པར་བྱེད་པ་ལྟར་རྟག་པ་དེ་དག་ཀྱང་དེ༌[^1113]བཞིན་ནོ། །

[Block 1921 [HEADING]]
### སེམས་ཅན་གྱི་དོན་དུ་འབད་པ། ^9-14-0

[Block 1922]
འདིར་རྒོལ་བར་བྱེད་དོ།[^1114] །ཡང་གལ་ཏེ་སངས་རྒྱས་རྣམས་ཀྱི་ཆོས་ཀྱི་སྐུ་ཐོག་མ་མེད་པའི་དུས་ནས་བྱེ་བྲག་མེད་པ་དཔག་ཏུ་མེད་པ་དེ་དག༌[^1115]ཉིད་སེམས་ཅན་གྱི་དོན་བྱ་བ་ལ་ནུས་པ་ཡོད་པའི་ཕྱིར། ཡང་ཅིའི་ཕྱིར་སེམས་ཅན་གྱི་དོན་དུ་འབད་པར་བྱེད་ཅེ་ན། ལན་ཚིགས་སུ་བཅད་པས་བསྟན་པ་ཡིན་ནོ། །

[Block 1923]
གལ་ཏེ་སངས་རྒྱས་བརྙེས་པ་ཁྱད་མེད་དཔག་མེད་པ། །ཞེས་བྱ་བའི་རྒྱུ་འདི་ཉིད་ཀྱིས་འབད་པར་མི་བྱའོ་ཞེས་ཟེར་ན། དེའི་ཕྱིར་སངས་རྒྱས་རྣམས་ཐོག་མ་མེད་པའི་དུས་ཅན་ཡིན་པའི་ཕྱིར། སྐྱོན་ཐམས་ཅད་འབྱུང་བར་ཐལ་བར་འགྱུར་བ་ཐོབ༌[^1116]པའམ། ཐམས་ཅད་རྒྱུ་མེད་པ༌[^1117]ཉིད་དུ་འགྱུར་བའམ། རྒྱུ་རྒྱུན་ཆད་པ་མེད་པར་འགྱུར་རོ་ཞེས་བྱ་བའོ། །

[Block 1924]
གཞན་ཡང་སྙིང་རྗེས་རྒྱུད་བསྒོས་པའི༌[^1118]བྱང་ཆུབ་སེམས་དཔའ་རྣམས་སེམས་ཅན་ཐམས་ཅད་ལ་བུ་གཅིག་པ་བཞིན་དུ་བརྩེ་བ་འབྱུང་བས། སེམས་ཅན་གྱི༌[^1119]དོན་ལ་གཞན་བྱེད་པར་འགྱུར་གྱི་ཞེའམ། [^1120]གཞན་བྱེད་ཀྱང་རུང་། མི་བྱེད་ཀྱང་རུང་། བདག་གིས་ནི་མི་བྱའོ་ཞེས་བྱ་བ་མི་རིགས་སོ། །

[Block 1925 [HEADING]]
## མཇུག་བྱང། ^b-0

[Block 1926 [HEADING]]
### མཛད་བྱང། ^b-1-0

[Block 1927]
ཐེག་པ་ཆེན་པོ་བསྡུས་པའི་འགྲེལ་པ། ཐེག་པ་ཆེན་པོ་ལ་རབ་ཏུ་གནས་པ། བསྟན་བཅོས་ཕུལ་དུ་བྱུང་བ་དུ་མ་མཛད་པའི་སློབ་དཔོན་དབྱིག་གཉེན་གྱིས་མཛད་པ་རྫོགས་སོ།། །།

[Block 1928 [HEADING]]
### འགྱུར་བྱང། ^b-2-0

[Block 1929]
རྒྱ་གར་གྱི་མཁན་པོ་དཱི་པཾ་ཀ་ར་ཤྲཱི་ཛྙཱ་ན་དང་། ལོ་ཙྪ་བ་དགེ་སློང་ཚུལ་ཁྲིམས་རྒྱལ་བས། ཡུལ་བྲག་དམར་ལྷ་སྡིངས། རི་ཁས་པོ༌[^1121]རིའི་རྩ། ཆུ་བོ་ལོ་ཧི་ཏའི་འགྲམ། དཔལ་བསམ་ཡས་ལྷུན་གྱིས་གྲུབ་པའི་གནས། དབྱིག་འདུལ་པེ་ཀར༌[^1122]གླིང་དུ་བསྒྱུར་ཅིང་ཞུས་ཏེ་གཏན་ལ་ཕབ་པའོ། །

[Block 1930]
[^1123]འདི་ལ་ཤློ་ཀ་ཉིས་སྟོང་ཆིག་བརྒྱ་བརྒྱད་ཅུ་ཡོད་དེ། བམ་པོ་ནི་བརྒྱད་དུ་བྱས་སོ།། །།
--- END BLOCKS ---
