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

[Block 1931]
རང་བཞིན་མཚོན་པའི་ཐབས་དང་ཤེས་རབ་ཀྱི་ཚུལ་དུ་མཐུན་ན་དགའ་བ་གསུམ་ལ་གནས་པའོ། །

[Block 1932]
དེའི་ཕྱིར་ན་དགའ་བ་གསུམ་པོ་སྤངས། །ཞེས་པ་ནི་ལྷན་ཅིག་སྐྱེས་པ་སྟེ་སྤྱོད་ཡུལ་དུ་གྱུར་པ་ཁོ་ནའོ། །

[Block 1933]
ད་ནི་ཐེ་ཚོམ་མེད་པར་ཉམས་སུ་བླང་བའི་རྟགས་ཇི་ལྟ་བུ་ཞེ་ན།

[Block 1934]
དང་པོ་སྤྲིན་དང་འདྲ་བ་ནི། དབང་གི༌[^870]དུས་ཀྱི་སྟོབས་ཏེ་དེ་ཡང་ས་ཧ་ཛའམ༌[^871]ལས་ཀྱི་ཕྱག་རྒྱ་ལ་བརྟེན་ནས། སྤྲིན་ཁྲོལ་བུའི་ཟླ་བ་ལྟ་བུ་མཐོང་བ་དང་མ་མཐོང་བའི་གནས་སྐབས་སོ། །

[Block 1935]
མཐོང་བ་དེ་ཡང་དོན་རང་གི་མཚན་ཉིད་ཀུན་དུ་སྦྱོར་བ་ནི་རྒྱ་མཚོའི་ལན་ཚྭའི་ཆུ་ཉུང༌[^872]ཟད་ཀྱིས་ཀུན་ཤེས་པའོ། །

[Block 1936]
གྲུབ་པ་སྒྱུ་མ་ལྟ་བུ་ནི་སྒོམ་པའི་དུས་ཀྱི་སྟོབས་ཏེ། མཾ་ན་ཛའམ་དྷརྨཱ་མུ་དྲ་ལ་བརྟེན་པས་རང་གི་མཚན་ཉིད་མ་ཡིན་པ། སྒྱུ་མའི་གཟུགས་བརྙན་ལྟ་བུ་སྣང་བའོ། །

[Block 1937]
དེ་ནས་རྨི་ལམ་འདྲ་བ་ནི་སྤྱོད་པའི་སྟོབས་ཏེ། ཁེ་ཏྲ་ཛའམ་ས་མ་ཡ་མུ་དྲ་ལ་བརྟེན་པས། དོན་རང་གི་མཚན་ཉིད་ལ་ཕྱོགས་པ་རྨི་ལམ་བེའུར་ཆད་པ་ལྟ་བུར་སྣང་ངོ་། །སད་པ་ནི་སྔར་གྱི་སྤྲིན་དང་འདྲ་བར་སྣང་བ་སྟེ་གསལ་བའི་ཕྱིར་རོ། །

[Block 1938]
གཉིད་ལོག་ནི་སྒྱུ་མ་དང་རྨི་ལམ་སྟེ་མི་གསལ་བའི་ཕྱིར་རོ། །

[Block 1939]
དེ་དག་ནི་འཆར་བ་དང་ནུབ་པ་སྟེ་ཐབས་དང་ཤེས་རབ་ཡིན་པས་མི་ཕྱེད་པ་ནི་ཕྱག་རྒྱ་ཆེན་པོའོ། །

[Block 1940]
གྲུབ་ཅེས་པ་ན་ཡང་མི་ཕྱེད་ཅེས་སྨོས་པ་ནི་འབྲས་བུའི་དུས་ཀྱི་སྟོབས་མནྟྲའམ་མ་ཧཱ་མནྟྲ་ལ་བརྟེན་ནས་མཚན་ཉིད་མ་གྲུབ་པར་སྣང་ངོ་། །ཕྱག་རྒྱའི་རྣལ་འབྱོར་ཞེས་པ་ནི་ཕྱག་རྒྱ་ཆེན་པོའོ། །

[Block 1941]
གྲུབ་ཅེས་པ་ནི་གདོན་མི་ཟ་བའོ། །

[Block 1942]
དེའི་རྗེས་ལ་མན་ངག་བསྟན་པར་བྱ་བའི་ཕྱིར་ཕྱི་ནས་ཞེས་པ་ནི་དབང་གི་རྗེས་ལའོ། །

[Block 1943]
དེ་ཉིད་ཡང་དག་བཤད་ནི་དབྱེར་མེད་པའི་མན་ངག་སྡུད་པར་བྱེད་པས་ཁས་ལེན་པའོ། །

[Block 1944]
ཡང་དང་ནི་དོན་དམ་ལྷན་ཅིག་སྐྱེས་པ་ནི་ཤེས་རབ་ཀྱི་མན་ངག་བསྟན་པའི་ཕྱིར། རྣམ་དག་ཡེ་ཤེས་ནི་སེམས་རང་བཞིན་གྱིས་དག་པར་དམ་བཅའ་བ་སྟེ་བསྟན་པའོ། །

[Block 1945]
བཤད་པར་འདོད་ནས་འཁོར་བ་དང་མྱ་ངན་ལས་འདས་ཞེས་པ་ནི་དངོས་པོ་དང་དངོས་མེད་ལ་སོགས་པ་གཞན་དག་ཀྱང་ངོ་། །

[Block 1946 [VERSE]]
ཁྱད་པར་ནི་བརྟག་པའི་ཁྱད་པར་རོ། །
ཅུང་ཟད་ནི་ཉུང་བ་བག་ཙམ་ཕྲ་བ་སྟེ།

[Block 1947]
སེམས་ཙམ་དུ་ཡང་ངོ་། །ཡོད་མ་ཡིན་ནི་གཅིག་དང་དུ་བྲལ་གྱིས་སོ། །

[Block 1948]
འོ་ན་ལམ་གྱི་དུས་སུ་ལྟ་བ་ཇི་ལྟ་བུ་ཞེ་ན། ཚིག་རྐང་གཉིས་ཏེ་གོ་སླའོ། །

[Block 1949]
ཡང་སྤྱོད་པ་ཇི་ལྟ་བུ་ཞེ་ན་ཚིགས་སུ་བཅད་པ་གཅིག་སྟེ་གོ་སླའོ། །

[Block 1950]
ཡང་སྒོམ་པ་ཇི་ལྟ་བུ་ཞེ་ན། རྐང་པ་གཅིག་གོ། །

[Block 1951]
འབྲས་བུ་དོན་གྱི་རང་བཞིན་ཇི་ལྟ་བུ་ཞེ་ན། རྐང་པ་གཅིག་གོ། །

[Block 1952]
ད་ནི་ཀུན་རྫོབ་ལྷན་སྐྱེས་སམ། ཐབས་ཀྱི་མན་ངག་བསྟན་པའི་ཕྱིར། རྡོ་རྗེ་སྙིང་པོས་གསོལ་བ་ཞེས་པ་ནི་ཡེ་ཤེས། རྣམ་པར་དག་པ་ནི་རིགས་ན་ལུས་དག་པ་མི་རིགས་པ་ཁོང་དུ་བཞག་སྟེ་དྲིས་པའོ། །

[Block 1953]
གཟོད་ནས་རང་བཞིན་མེད་པའི་ཞེས་པ་ནི་སེམས་དག་པ་དེས་སོ། །

[Block 1954]
ལུས་ཀྱི་རང་བཞིན་དག་པ་ན་ཕྲ་རུ་སྟེ་དེ་རུ་དེའི་ཕྱིར་གང་དུ་ལོགས་སུ་འབྲེལ་ལོ། །

[Block 1955]
དེ་ཡང་རྒྱུ་མཚན་ནི་ལུས་འབྱུང་བའི་བདག་ཉིད་ཡིན་པའི་ཕྱིར། དག་པ་མི་རིགས་སོ་ཞེ་ན། དག་པ་ཡིན་ན་འབྱུང་བ་མ་ཡིན་ན་དག་པའི་ལྷན་སྐྱེས་མ་ཡིན་ཞེ་ན། ཀུན་རྫོབ་ལྷན་སྐྱེས་ལེན༌[^873]བཏབ་པ་ནི་འབྱུང་བ་ཡིན། དེ་ནས་དེ་ལའོ། །

[Block 1956]
བཅོམ་ལྡན་རྡོ་རྗེ་ཅན་ནི་རྡོ་རྗེ་འཛིན་པའོ། །

[Block 1957]
དེའི་ཁྱད་པར་བསྟན་པའི་ཕྱིར་མཁའ་འགྲོ་ནི་བདག་མེད་མ་པུཀྐ་སཱི་ལ་སོགས་པ་བཞིའོ། །

[Block 1958]
བདེ་བ་སྟེར་ནི་རྒྱུའི་རྡོ་རྗེ་འཆང་སྙོམས་པར་འཇུག་པའམ། གླུའི་ངོར་འབྲས་བུ་ཧེ་རུ་ཀ་ལྡང་བ་དེའི༌[^874]དགྱེས་པའི་རྡོ་རྗེའོ། །

[Block 1959]
ཡང་མཁའ་འགྲོ་ནི་ཌཱ་ཀི༌[^875]ནི་སྟེ་ཞིང་དག་ཏུ་རྒྱུ་བའི་ལས་ཕྱག་རྒྱའོ། །

[Block 1960]
བདེ་བ་སྟེར་ནི་ལྷན༌[^876]སྐྱེས་པའི་རོ་དང་མི་འབྲལ་བའི་ཐབས་ཀྱིས་དགྱེས་པའི་རྡོ་རྗེའོ། །

[Block 1961 [VERSE]]
དེ་ནི་གཞན་ལུས་ཤེས་རབ་ལ་བརྟེན་པའོ། །
ཡང་མཁའ་འགྲོ་ནི་རྩ་རྣམས་སོ། །

[Block 1962]
བདེ་སྟེར་ནི་ཀུནྡ་ལྷན་སྐྱེས་ཏེ་ལུས་ལ་གནས་པའི་དགྱེས་པ་རྡོ་རྗེའོ། །

[Block 1963 [VERSE]]
དེ་ནི་རང་ལུས་ཐབས་དང་ལྡན་པའོ། །
ཡང་མཁའ་འགྲོ་ནི་ཕྱག་རྒྱ་ཆེན་པོའོ། །

[Block 1964]
བདེ་སྟེར་ནི་གནས་པ་སྟེ། ཟག་པ་མེད་པའི་བདེ་བ་ཆེན་པོ་སྟེ་གཉིས་སུ་མེད་པའི་དགྱེས་པའི་རྡོ་རྗེའོ། །

[Block 1965]
དེ་ནི་དབྱེར་མེད་དོ། །
--- END BLOCKS ---
