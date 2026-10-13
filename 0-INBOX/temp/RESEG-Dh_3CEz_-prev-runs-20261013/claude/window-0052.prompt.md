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
[Block 1821]
གང་བའི་བུམ་པ་ནི་ངེས་པ་མེད་དེ་ཅི་འབྱོར་པ་དབུལ་བར་བྱའོ། །

[Block 1822]
རྣམ་པར་རྒྱལ་བ་ཤར་དུ་བཀོད་པ་ནི་བུམ་པ༌[^848]སྟེ། གཙོ་བོའི་མདུན་ནས་ཤར་དུའོ། །

[Block 1823]
ལས་ཐམས་ཅད་པའི་བུམ་པ་ནི་ཤར་གྱི་སྒོར་རོ། །

[Block 1824]
གཞན་དག་གོ་སླའོ། །

[Block 1825]
དེའི་རྗེས་ལ་ཇི་ལྟར་བསམ་གཏན་དེ་བཞིན་འདིར་ནི་དམ་ཚིག་གི་འཁོར་ལོ་སྒྲུབ་ཐབས་ལྟར་བསྐྱེད་པའོ། །

[Block 1826]
དེ་ཉིད་ཇི་ལྟར་ཞེ་ན། བསྲུང་བ་ནི་སྔགས་ཀྱིས་སོ། །

[Block 1827]
གསུངས་པའམ་བརྗོད་པ་ནི་ཨོཾ་རཀྵ་ལ་སོགས་པ་སྟེ། བདག་བསྲུང་བ་ནས་བརྩམས་ཏེ་བྱའོ། །

[Block 1828]
ཡང་ན་ཡེ་ཤེས་ཀྱི་འཁོར་ལོ་བཅུག་སྟེ་བགེགས་བསལ་བའོ། །

[Block 1829]
དེའི་རྗེས་ལ་མཆོད་པ་ནི་ལྷ་མོ་བརྒྱད་ལ་སོགས་པས། མདུན་དུ་འོད་ཟེར་གྱིས་སྤྱན་དྲངས་པ་ལའོ། །

[Block 1830]
གསོལ་བ་གདབ་པ་ནི་མཆོད་པས་མཉེས་པ་ནི་སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ༌[^849]ལའོ། །

[Block 1831]
དེ་ཡང་དེ་ནས་ཧེ་རུ་ཀའི་གཟུགས་ཀྱིས་དབང་བསྐུར་བར་འགྱུར་རོ། །

[Block 1832]
ཇི་ལྟར་བཤད་པ་ནི་བཤད་པའི་རྒྱུད་དག་གམ་རྣལ་འབྱོར་གྱི་རྒྱུད་དུའོ། །

[Block 1833]
འདིར་ཡང་བྱ་བ་ནི་མཆོད་བསྟོད་ལ་སོགས་པ་རྒྱས་པར་འདོད་ནའོ། །

[Block 1834]
དེའི་ཏིང་ངེ་འཛིན་ནི་འདི་ཡིན་ཏེ། ཕྱག་མཚན་བཀོད་ནས་མདང་སྟ་གོན་གྱི་དཀྱིལ་འཁོར་ནམ་མཁའ་ལ་བཀོད་པ་ཕབ་སྟེ། གཉིས་བསྲེ་བར་བྱའོ། །

[Block 1835]
དེ་ནས་བུམ་པ་དགོད་པ་དང་རྒྱན་བྲི་བ་དང་མཆོད་པ་རྣམས་བཤམས་ལ། བདག་ཉིད་ཁྲུས་དང་གཙང་སྦྲ་དང་རྒྱན་གྱོན་ནས། དཀྱིལ་འཁོར་གྱི་ཤར་སྒོར་སྟན་བདེ་བ་ལ་འདུག་སྟེ་གཙོ་བོ་དང་མོས་པར་གཅིག་ཏུ་བསམས་ཏེ། བདག་བསྲུང་བ་ནས་ཚོགས་བསགས་པ་དང་། རྟེན་གྱི་རྣལ་འབྱོར་བསྒོམ་པ་དང་། བརྟེན་པ་ལྷའི་དཀྱིལ་འཁོར་ལེའུ་བརྒྱད་པ་ལྟར་བསྒོམས་ཏེ། མཆོད་བསྟོད་བདུད་རྩི་མྱང་བའི་བར་དུ་བྱ་བ་ནི་བདག་ཉིད་ལ་ལྡན་པ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 1836]
དེ་ནས་དཀྱིལ་འཁོར་སྒྲུབ་པ་ནི་ས་བོན་ནམ་ཕྱག་མཚན་ཙམ་ལས་ལྷ་མོའི་འཁོར་ལོ་རྫོགས་པར་བསྐྱེད། ཡེ་ཤེས་པ་སྤྱན་དྲངས། སྐྱེ་མཆེད་བྱིན་གྱིས་བརླབས། སྐུ་གསུང་ཐུགས་ཀྱི༌[^850]བྱིན་གྱིས་བརླབས། །དབང་བསྐུར་མཆོད་པ་དང་བསྟོད་པ་རྒྱས་པར་བྱ། བདུད་རྩི་མྱང་། བཟླས་པའི་བར་དུ་བྱའོ། །

[Block 1837]
དེའི་རྗེས་ལ་གང་ཞིག་དབང་ནི་རབ་ཏུ་དབྱེ་བ་ནི༌[^851]དབང་བཞིའི་རིམ་པའམ་ཆུ་ལ་སོགས་པའོ། །

[Block 1838 [VERSE]]
རང་གི་དཀྱིལ་འཁོར་ཚོགས་སྦྱིན། །
ཞེས་པ༌[^852]ནི་ཁྱད་པར་གྱི་ལུགས་ཀྱིས་སོ། །
མཆོད་དང་གསོལ་བ་གདབ་པ་ཉིད། །

[Block 1839]
ཅེས་འདིར་ཡང་འབྲེལ་ཏེ། མཆོད་པ་ནི་ཐུན་མོང་གི་མཆོད་པ་དང་། ཁྱད་པར་གྱི་མཆོད་པ་བརྟག་པ་ཕྱི་མ་ནས། ཞིམ་པའི་བཟའ་བ་བཏུང་བ་དང་། །ཞེས་འདིར་འབྲེལ། ཐུན་མོང་གི་གསོལ་བ་གདབ་པ་དང་། དགའ་ཆེན་ཁྱོད་བདག་སྟོན་པ་བས། །ཞེས་བྱ་བ་དང་། ཁྱད་པར་གྱི་གསོལ་བ་གདབ་པ་ནི། [^853]འཁོར་བ་འདམ་གྱི་ཚོགས་དག་ཏུ།

[Block 1840 [VERSE]]
བྱིང་བ་སྐྱབས་མེད་བདག་ལ་སྐྱོབས། །
ཞེས་བྱ་བ་ལ་སོགས་པ་འདིར་འབྲེལ་ལོ། །

[Block 1841]
དབང་བསྐུར་བ་ཐུན་མོང་རིག་པའི་དབང་ལྔ་དང་། ཁྱད་པར་བདག་པོའི་དབང་དང་དྲུག་སྟེ། །དེ་སྐད་དུ་ཡང་།

[Block 1842 [VERSE]]
དྲུག་པ་བདག་པོའི་དབང་གིས་དང་། །
ཞེས་བྱ་བ་གསུངས་པའི་ཕྱིར་རོ། །

[Block 1843]
དེའི་རྗེས་ལ་གསང་བའི་དབང་བསྟན་པའི་ཕྱིར། དེར་ཞེས་པ་ནི་བུམ་པའི་དབང་གིས་གནས་དེ་ཉིད་དུའོ། །

[Block 1844]
རིགས་ལྔ་ལས་བྱུང་བ༌[^854]ནི་དམན་པ་རྣམས་དང་། བྲམ་ཟེའི་རིགས་སུ་སྐྱེས་པ་སྟེ། དེས་རིག་པ་བསྐྱེད་པ་སྟེ་རིག་མའོ།[^855] །བཟང་མོ་ནི་སྒོ་གསུམ་གྱི་ཁྱད་པར་རོ། །

[Block 1845]
གཞུག་པ་ནི་ལས་དང་པོ་པ་ཡིན་ན་སློབ་མ་བཞིན་དུའོ། །

[Block 1846]
ཡང་ན་ཇི་ལྟར་གང་རྙེད་ནི་རིགས་དང་སྒོ་གསུམ་གྱི་ཡོན་ཏན་དང་མི་ལྡན་ཀྱང་ངོ་། །

[Block 1847 [VERSE]]
དེ་བཞིན་ནི་ཕྱོགས་གཉིས་པ་དེ་ལའོ། །
བཅུ་དྲུག་ལོན་པའི༌[^856]ན་ཚོད་གཙོ་བོར་གྱུར་པ༌[^857]ཁོ་ནའོ། །

[Block 1848]
ཁུ་བ་ལྡན་པ་ནི་ཤེས་རབ་རང་བཞིན༌[^858]མ་ཡིན་པའོ། །

[Block 1849]
ཇི་སྲིད་ནི་གང་གི་ཚེའོ། །

[Block 1850]
དེ་སྲིད་ནི་དེའི་ཚེའོ། །

[Block 1851]
ཕྱག་རྒྱ་བསྟེན་པ་ནི་ལང་ཚོ་དང་ལྡན་པ་དེ་ཉིད་ཆང་ལ་སོགས་པའོ། །

[Block 1852]
ཕྱག་རྒྱ་ནི་གདོང་བཅིང་བ་ནི་འཇུག་པའི་ཚུལ་ལོ། །

[Block 1853]
ཐབས་ཀྱི་གདོང་ཡང་དེ་བཞིན་ནི་སློབ་མ་འཇུག་པ་དང་ཕན་ཚུན་དུ་མཐུན་པའོ། །

[Block 1854]
ཡང་ན་ཕྱག་རྒྱ་ནི་གདོང་བཅིང་བ་ནི་བདུད་རྩི་ལེན་པའི་དུས་སུ་སྟེ། འདི་ཡང་བྱ་བའི་རིམ་པ་དང་ནོད་པའི་རིམ་པའོ། །

[Block 1855]
བྱ་བའི་རིམ་པ་ནི་སློབ་མ་འཇུག་པ་བཞིན་དུ་ཕྱག་རྒྱ་མ་ཡང་དཀྱིལ་འཁོར་དུ་གཞུག་པ་དང་། ཚུལ་བཞིན་དུ་བྱས་ལ་ནོད་པའི་བདུད་རྩི་ལེན་པའི་དུས་ཏེ་དེར་ཡང་གདོང་བཅིང་ངོ་། །སློབ་དཔོན་ལ་ལ་ནི་འདིར་ཟླ་བ་གཟུང་བའི་མན་ངག་ལ་ཡང་འཆད་དོ། །

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
--- END BLOCKS ---
