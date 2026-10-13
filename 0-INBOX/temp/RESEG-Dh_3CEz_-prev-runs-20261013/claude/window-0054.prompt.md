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
དབང་ཕྱུག་ནི་མ་ཧེ་ཤྭ་ར་སྟེ་ཀུན་ལ་དབང་བའི་བདག་པོའོ། །

[Block 1892 [VERSE]]
དབང་ཕྱུག་ཆེན་པོའམ་ལྷ་ཆེན་པོ་ཞེས་བརྗོད་དོ། །
བདག་ནི་རྟག་པའི་ཁྱད་པར་ལྡན་པའོ། །
གསོ་བ་ནི་འཛིན་པ་སྟེ་དབུགས་སོ། །

[Block 1893]
སེམས་ཅན་ནི་ཤེས་པ་སྟེ་ནུས་པ་ཤེས་ཅན་ནོ། །

[Block 1894]
དུས་ནི་ཡོན་ཏན་ནོ། །

[Block 1895]
གང་ཟག་ནི་པུང་གལ་སྟེ། བྱེད་པ་པོའམ། ལས་ཀྱི་འབྲས་བུ་གང་ཞིག་སྨིན་པར་འཛག༌[^863]པའོ། །

[Block 1896]
དེ་དག་ཏུ་བཏགས་པ་མ་ཟད་དེ། དངོས་པོ་ཀུན་གྱི་རང་བཞིན་ནི་མྱ་ངན་ལས་འདས་པའི་བར་དུའོ། །

[Block 1897]
སྒྱུ་མའི་ཚུལ་ལམ་གཟུགས་ནི་མ་ཧཱ་མཱ་ཡཱ་སྟེ། བདེན་པ་ཡང་མ་ཡིན་བརྫུན་པ་ཡང་མ་ཡིན་པའི༌[^864]སྒྱུ་མ་ཆེན་པོའོ། །

[Block 1898]
ཡང་དག་གནས་ནི་ཟག་པ་མེད་པའི་བདེ་བར་རང་སྣང་བའོ། །

[Block 1899]
དེའི་ཕྱིར་ཉེས་པ་མེད་པ་ཁོ་ནའོ། །

[Block 1900]
ད་ནི་ཐེ་ཚོམ་གྱི་ཡུལ་བསྟན་པ་དང་ལྷན་ཅིག་སྐྱེས་པ་ཇི་ལྟར་ཉམས་སུ་བླང་བའི་ཐབས་བསྟན་པའི་ཚིགས་སུ་བཅད་པ་གཅིག་སྟེ་གོ་སླའོ། །

[Block 1901]
དེ་བཞིན་གཤེགས་པ་དང་རྡོ་རྗེ་སྙིང་པོ་ནི་སྔོན་དུའོ། །

[Block 1902]
མཁས་པ་ནི་རྗེས་སུ་འཇུག་པའི་ཕ་རོལ་ཕྱིན་པ་ལའོ། །

[Block 1903]
དེ་སྐད་དེས་ཐོས་ནི་ཟག་པ་དང་བཅས་པ་ཆགས་པ་ལས་བྱུང་བའམ། ཟག་པའི་བདག་ཉིད་དུ་ཐོས་པའོ། །

[Block 1904]
མཆོག་ཏུ་ངོ་མཚར་ནི་དམན་པའམ་སྤྱོད་ཡུལ་མ་ཡིན་པས་སོ། །

[Block 1905]
བརྒྱལ་ཞིང་ས་ལ་འགྱེལ་བ་ནི་སྐྲག་པའམ་ཆེ་བའི་བདག་ཉིད་སྟོན་པའོ། །

[Block 1906]
ཡང་ན་བརྒྱལ་བ་ནི་སེམས་ཀྱི་ཁྱད་པར་རོ། །

[Block 1907]
འགྱེལ་བ་ནི་ལུས་ཀྱི་བཀོད་པའོ། །

[Block 1908]
འདིར་དགའ་བའི་གྲངས་ལ་ཐེ་ཚོམ་སྐྱེས་པ་ལྟར་བསྟན་ཀྱང་དོན་ལ་དབང་བཞི་པ་ལ་ཐེ་ཚོམ་སྐྱེས་ཏེ། ཤིན་ཏུ་ཟབ་པས་སྤྱོད་ཡུལ་མ་ཡིན་པར་དོགས་པ་དང་། ཡང་ན་ཤིན་ཏུ་དམན་པས་ངན་པ་རུ་རྟོག་པ་སྐྱེས་པའོ། །

[Block 1909]
ད་ནི་དེ་དག་གི་རྒྱུ་མཚན་སེམས་ལ་གནས་པའི་སོ་སོར་བརྗོད་པའི་ཕྱིར།

[Block 1910 [VERSE]]
དང་པོ་དགའ་བ་འགྲོ་བ་ནི་བརྟག༌[^865]པའོ། །
མཆོག་དགའ་འགྲོ་བའམ་བརྟག་པས་ཏེ་འཁོར་བར་རོ། །

[Block 1911]
དགའ་བྲལ་དགའ་བའང་འགྲོ་བའམ་བརྟག་པ་སྟེ་མྱ་ངན་ལས་འདས་པར་རོ། །

[Block 1912]
དེས་ན༌[^866]འཁོར་བ་དང་མྱ་ངན་ལས་འདས་པའི་མཐར་འགྲོ་བས་ངོ་མཚར་བའམ་བརྒྱལ་བའོ། །

[Block 1913]
ཡང་ན་ཟབ་པ་ཆེ་བའི་བདག་ཉིད་དགའ་བ་གསུམ་གྱིས་མི་རྟོག་པའོ། །

[Block 1914]
སྤྱོད་ཡུལ་མ་ཡིན་པར་དོགས་ན་ངོ་མཚར་ཞིང་བརྒྱལ་བའོ། །

[Block 1915]
དེའི་ཕྱིར། དགའ་བ་གསུམ་ལ་ལྷན་སྐྱེས་མེད། །ཅེས་པའོ། །

[Block 1916]
ད་ནི་ཐེ་ཚོམ་བསལ་བའི་ཕྱིར་སྡུད་པར་བྱེད་པས། བཅོམ་ལྡན་བཀའ་སྩལ་ཀྱེའི་རྡོ་རྗེ། །ཞེས་པའོ། །

[Block 1917]
སངས་རྒྱས་ཀུན་གྱི་སྐུ་གཅིག་ནི་བདེ་བ་ཆེན་པོའི་སྐུའོ། །

[Block 1918]
རྡོ་རྗེ་སྙིང་པོས་རྟོགས་བྱ་ནི་སྔོན་བྱུང་དག་གོ། །

[Block 1919]
ཐེ་ཚོམ་ནི་དམན་པའམ་སྤྱོད་ཡུལ་མ་ཡིན་པ་གོང་དུ་བརྗོད་པ་ཉིད་དོ། །

[Block 1920]
བཟང་བའམ་ལེགས་པར་སེལ་བ་ནི་ལས་ལེན་པའོ། །ཅི་ཞེ་ན། དེ་ཡང་དང་པོར་དམ་པ་དོགས་པ་སེལ་བའི་ཕྱིར་རོ། །

[Block 1921]
འདོད་ཆགས་མེད་ཅིང་ཆགས་བྲལ་མེད་ནི་དགའ་བ་དང་དགའ་བྲལ་ཏེ། བརྟག་པ་དེ་དག་ལྷན་ཅིག་སྐྱེས་པ་ལ་མེད་དོ། །

[Block 1922]
དབུ་མ་ཞེས་པ་ནི་དགའ་བ་སྟེ། གྲངས་ཀྱི་དབུ་མར་ཡང་མ་ཡིན་ལ། དོན་གྱི་དབུ་མ༌[^867]དེ་ཁོ་ན་ཉིད་ཀྱིས་ཁྱབ་པ་ཡང་མ་ཡིན་ཏེ་ཉམས་མྱོང་སྐྱེས་པའི་དབུ་མ་སྟེ། དེ་ཡང་མི་དམིགས་སོ། །

[Block 1923]
དེ་དག་ཀྱང་ལྷན་ཅིག་སྐྱེས་པ་ལ་མི་ལྡན་ཡང་བློས་བརྟགས་ནས་དམའ་བར་འགྲོའོ་ཞེ་ན། དེའི་ཕྱིར་གསུམ་པོ་སྤངས་པ༌[^868]ཉིད། །ཅེས་པ་ནི་སྤངས་ཏེ་ཉམས་སུ་བླང་བའི་ཕྱིར་རོ། །

[Block 1924]
ལྷན་ཅིག་སྐྱེས་པའི་བྱང་ཆུབ་ནི་དྲི་མ་དང་བྲལ་བས་རྟོགས་པ་སྟེ། ཡང་དག་པའི་འབྲས་བུར་བརྗོད་དོ། །

[Block 1925]
ད་ནི་སྤྱོད་ཡུལ་མ་ཡིན་པར་དོགས་པའི་ཐེ་ཚོམ་བསལ་བའི་ཕྱིར་རོ། །

[Block 1926]
ཡང་ན་ཞེས་པ་ནི་དམན་པར་དོགས་པ་ལས་ཕྱོགས་གཞན་དུའོ། །

[Block 1927]
དེ་ཉིད་ཅེས་པ་ནི་ལྷན་ཅིག་སྐྱེས་པའོ། །

[Block 1928]
ཐམས་ཅད་བདག་ཅེས་པ་ནི་དགའ་བ་གསུམ་གྱི་རང་བཞིན་ཡིན་པའི་ཕྱིར་དགའ་བ་གསུམ་དང་ལྡན་པའི་ཚེ། དེའི་བདག་ཉིད་ཀྱང་རྟོགས་པར་སྤྱོད་ཡུལ་མ་ཡིན་པ་ཁོ་ནའོ། །

[Block 1929]
ཡང་ན་ཞེས་པ་ནི་རང་བཞིན་གཅིག་ཀྱང་རྣམ་པའི་ཕྱོགས་གཞན་དུ་བསྟན་པའི་ཕྱིར། ཀུན་ནས༌[^869]རྣམ་པར་སྤངས་ནི་གསུམ་དང་ལྷན་ཅིག་སྐྱེས་པ་རྣམས་ཕན་ཚུན་སྤངས་པས་སོ། །

[Block 1930]
འོ་ན་རྣམ་པ་མི་མཐུན་ན་གསུམ་པོ་མི་དགོས་ལ། གསུམ་པོ་མེད་ན་སྤྱོད་ཡུལ་དུ་མི་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་དགའ་བྲལ་དང་པོ་མཚོན་ཞེས་པ་ནི་རྣམ་པར་མཚོན་པའི་ཐབས་ནི་གོ་རིམས་ཏེ། གཉིས་ཀྱི་འོག་དང་གཅིག་གི་གོང་སྟེ་གསུམ་པར་རོ། །
--- END BLOCKS ---
