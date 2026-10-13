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
[Block 1856]
འདིར་ནི་སློབ་དཔོན་གྱིས་དེ་ཁོ་ན་ཉིད་ཉམས་སུ་མྱོང་བ་དེའི་ཆང༌[^859]བུ་ལ་སྦྱིན་ཞེས་བྱ་བའོ། །

[Block 1857 [VERSE]]
བརྟེན་པ་དེ་ལས་གང་བྱུང་བ། །
ཞེས་པ་བདུད་རྩི་དེ་ཉིད་དོ། །

[Block 1858]
ཐབས་ཀྱི་གདོང་ཡང་དེ་བཞིན་ཞེས་པ་ནི་སྟེར་བའི་དུས་སུ་སྟེ། སློབ་མའི་ཁར་ནི་ལྷུང་ཞེས་པར་འབྲེལ་བའོ། །

[Block 1859]
ད་ནི་གསུམ་པ་བསྟན་པའི་ཕྱིར། རོ་མཉམ་ནི་ལྷན་ཅིག་སྐྱེས་པའི་རོའོ། །

[Block 1860]
སློབ་མའི་སྤྱོད་ཡུལ་ནི་སྔོན་དུ་མན་ངག་བསྟན་པའོ། །

[Block 1861]
དེ་ཉིད་ལ་ཡང་དེ་གསང་བའི་རྟེན་ཉིད་ལའམ་རིག་མ་གཞན་ལའོ། །

[Block 1862]
བྱ་བར་བྱའམ་ངེས་པར་བྱ་ནི། སྔོན་དུ་མན་ངག་བསྟན་པ་བཞིན་དུ་ཉམས་སུ་བླངས་པའོ། །

[Block 1863]
དེས་ཅིར་འགྱུར་ཞེ་ན། རང་རིག་ཡེ་ཤེས་ནི་དོན་དམ་ལྷན་ཅིག་སྐྱེས་པའོ། །

[Block 1864]
གྱུར་པ་ནི་ཀུན་རྫོབ་ལྷན་སྐྱེས་ལས་ཏེ། དེ་དག་གི་རིམ་པ་བརྟག་པ་ཕྱི་མ་ལས་བསྟན་ཏོ། །

[Block 1865]
འདི་ལ་ཡང་བྱ་བའི་རིམ་པ་དང་ནོད་པའི་རིམ་པ་གཉིས་སོ། །

[Block 1866]
གསུམ་པས་གོ་ཕྱེ་བའི་སློབ་མའི་ཉམས་སུ་མྱོང་བ་དེ་ཉིད་བཤད་པ་ནི།

[Block 1867]
བཞི་པ་སྟེ།

[Block 1868 [VERSE]]
དེ་ལ་ཡང་རྟེན་ཅན་དང་རྟེན་མེད་གཉིས་སོ། །
སློབ་དཔོན་ལ་ལ་ནི་རྟེན་ཅན་དུ་ཡང་འདོད་དོ། །

[Block 1869]
བླ་མའི་གཞུང་གིས་ནི་ཚིག་དབང་རིན་པོ་ཆེ་ཞེས་བྱ་སྟེ་རྟེན་མེད་ཀྱི་ལུས་སོ། །

[Block 1870]
དེ་ལ་ཡང་དབང་བཞི་པ་ཚིག་དབང་དང་། མན་ངག་དང་གཉིས་སུ་བཞེད་དེ། བླ་མའི་ཞལ་ལས་ཤེས་པར་བྱའོ།[^860] །དེ་སྐད་དུ་ཡང་། དེ་ལྟར་དེ་བཞིན་ཡང་བཞི་པ། །ཞེས་གསུངས་པས་སོ། །

[Block 1871]
དེའི་ཁྱད་པར་བསྟན་པ་ནི་དབང་བཞི་པ་སྟེ། རང་བཞིན་ནི་གཟུང་འཛིན་ནོ། །

[Block 1872]
ཡང་དག་རིག་པ་ནི་དང་པོ་ཡིན་ཡང་གསུམ་པ་སྟེ། དེ་དག་དེས་སྤངས་པའོ། །

[Block 1873]
དེས་ཅིར་འགྱུར་ཞེ་ན། མི་རྟོག་པ་སྟེ། མཁའ་མཉམ་ནི་དཔེའོ། །

[Block 1874]
རྡུལ་ནི་རྣམ་པར་རྟོག་པ་དང་། ཉོན་མོངས་པའོ། །

[Block 1875 [VERSE]]
དེའི་ཕྱིར་སྟོང་པ་ཉིད་དཔེ་དེ་ལས་བྱུང་བའོ། །
དེ་དང་ལྷན་ཅིག་ཚིམ་པ་ནི་ཐབས་ཅི་ཞེ་ན།

[Block 1876]
དངོས་དང་དངོས་མེད་ནི་ཆོས་ཅན་ནོ། །

[Block 1877]
བདག་ཉིད་མཆོག་ནི་བདེ་བ་ཆེན་པོའི་རང་བཞིན་ནོ། །

[Block 1878 [VERSE]]
དེ་དག་ནི་དབྱེར་མེད་པ༌[^861]བསྟན་པའི་ཕྱིར།
ཤེས་རབ་ཐབས་ནི་མི་རྟོག་པ་དང་བདེ་བའོ། །
ཤིན་ཏུ་འདྲེས་པ་ནི་དབྱེར་མི་ཕྱེད་པའོ། །

[Block 1879 [VERSE]]
ཡང་ཆགས་པ་དང་ཆགས་བྲལ་ནི།
མཆོག་དགའ་དང་དགའ་བྲལ་གྱི་རྣམ་པས་སོ། །

[Block 1880]
འདྲེས་པ་ནི་དབྱེར་མི་ཕྱེད་པ་སྟེ་ལྷན་ཅིག་སྐྱེས་པའི་རོའོ། །

[Block 1881]
ད་ནི་དེའི་རང་བཞིན་ནམ་ཆེ་བའི་བདག་ཉིད་བསྟན་པའི་ཕྱིར། དེ་ཉིད་སྲོག་ཆགས་རྣམས་ཀྱི་སྲོག་ནི་སེམས་ཅན་ཀུན་ཡང་ལྷན་ཅིག་སྐྱེས་པའི་འཚོ་བ་ལ༌[^862]བརྟེན་པ་ཡིན་ཏེ། ཡི་གེ་དམ་པ་ཞེས་པ་ནི་ཨཀྵར་སྟེ་མི་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 1882]
འགྲོ་བའི་བདག་ཉིད་ནི་ལྷན་ཅིག་སྐྱེས་པ་དེའོ། །

[Block 1883]
ཐམས་ཅད་ཁྱབ་པ་ནི་སེམས་ཏེ་དོན་དམ་ལྷན་ཅིག་སྐྱེས་པའི་ཕྱིར་རོ། །

[Block 1884]
ལུས་ཀུན་ལ་གནས་པ་ནི་ཀུན་རྫོབ་པོ། །དངོས་དང་དངོས་མེད་དེ་ལས་བྱུང་ནི་དངོས་པོ་ཀུན་རྫོབ་ལྷན་ཅིག་སྐྱེས་པ་ནི། དངོས་མེད་དོན་དམ་དུ་གནས་པའོ། །

[Block 1885]
ཡང་ན་དངོས་པོ་སྟེ་གཟུགས་ལ་སོགས་པ་ལྔ་དང་། དངོས་མེད་དེ་ཆོས་སོ། །

[Block 1886]
གཞན་ནི་དབང་པོའོ། །

[Block 1887 [VERSE]]
གང་རྣམས་དེ་རྣམས་ནི་བརྟན་གཡོའོ། །
རྣམ་ཤེས་ནི་མིག་ལ་སོགས་པའོ། །

[Block 1888]
ཀུན་གྱི་ཚུལ་ནི་གཟུགས་ལ་སོགས་པ་དེ་དག་དང་ལྷན་ཅིག་སྐྱེས་པར་སྣང་བའོ། །

[Block 1889]
འོ་ན་ལྷན་ཅིག་སྐྱེས་པ་དེ་ཉིད་ཆོས་ཀུན་གྱི་རང་བཞིན་ཡིན་ན་གྲུབ་མཐའ་ངན་པས་བརྟགས་པའི་ཆོས་རྣམས་སུ་མི་འགྱུར་རམ་ཞེ་ན། ཉེས་པ་མེད་དེ་སྐྱེས་བུ་ནི་པུ་རུ་ཥ་སྟེ་སྣོད་ཀྱི་འཇིག་རྟེན་དུ་བཅུད་ཀྱིས་འགེངས་པར་བྱེད་པའོ། །

[Block 1890]
སྔོན་རབས་ནི་བྲི་ཏ་ཀ་སྟེ་ཕྱའམ་མེས་པོ་སྟེ་ཚངས་པའོ། །

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
--- END BLOCKS ---
