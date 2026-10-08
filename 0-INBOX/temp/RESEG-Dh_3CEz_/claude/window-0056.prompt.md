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

[Block 1966]
གསུངས་ཞེས་པ་ཐེ་ཚོམ་སེལ་བར་རོ། །

[Block 1967]
དེ་ཉིད་ཅི་ཞེ་ན། རློམ་སེམས་མེད་པའི་རང་བཞིན་ནི་སེམས་དག་པ་དེའོ། །

[Block 1968 [VERSE]]
བདག་ནི་འབྱུང་བའི་བདག་ཉིད་དོ། །
ཐམས་ཅད་ནི་འགྲོ་བ་ཀུན་གྱིའོ། །

[Block 1969]
ལུས་ལ་རྣམ་པར་གནས་ནི་གཉུག་མའི་དབང་པོ་ལ་བརྟེན་པའོ། །

[Block 1970]
བསྟན་པ་དེ་དག་ཀྱང་སོ་སོར་བཤད་པའི་ཕྱིར། ཀྱེ་བཅོམ་ལྡན་འདས་ཞེས་པ་ནི། མཛེས་པས་བོད་པའོ། །

[Block 1971]
ཅིའི་སླད་དུ་ཞེས་པ་ནི་ལུས་ལ་གནས་པ་ལུས་དག་པའི༌[^877]རྒྱུ་མཚན་དྲིས་པའོ། །

[Block 1972]
འབྱུང་བ་ཆེན་པོ་ལྔ་པོས་ཕུང་པོའི་རིགས་ནི་བསྡུས་པ་སྟེ་ལུས་སོ། །

[Block 1973]
དེ་ཇི་ལྟར་བསྐྱེད་ཅིང་རྟེན་ལགས་ཞེས་པའོ། །

[Block 1974]
ད་ལན་བསྟན་པ་ཡང་འབྱུང་བས་སྐྱེས་པའི་ཚུལ་བསྟན་པའི་ཕྱིར།

[Block 1975 [VERSE]]
བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ༌[^878]ཞེས་པའོ། །
གང་གི་དུས་སུ་ཞེ་ན།
བོ་ལ་ཀཀྐོ་ལ་སྦྱོར་བས། །

[Block 1976]
ཞེས་པ་ནི་ལྷན་ཅིག་སྐྱེས་པ་སྦྱོར་བའོ། །

[Block 1977]
རེག་པ་སྲ་བའི་ཆོས་ནི་སྙོམས་འཇུག་ལ་སའི་མཚན་ཉིད་ལྡན་པས་སོ། །

[Block 1978 [VERSE]]
ས་ནི་དེ་ལས་སྐྱེ་ཞེས་པ་སར་བསྒྲུབ་པའོ། །
བྱང་ཆུབ་སེམས་ཞུ་བ༌[^879]ནི་གཤེར་བ་སྟེ།

[Block 1979 [VERSE]]
སྙོམས་འཇུག་དེ་ལ་ཆུའི་མཚན་ཉིད་དང་ལྡན་པས་སོ། །
ཆུའི་ཁམས་ནི་འབྱུང་ཞེས་པ་ནི་དེ༌[^880]བསྒྲུབ་བོ། །

[Block 1980 [VERSE]]
བསྲུབ་བའམ་བསྐྱེད་པ་ནི་སྙོམས་འཇུག་ལའོ། །
དྲོད་ནི་མེའི་མཚན་ཉིད་ལྡན་པས་སོ། །
སྐྱེས་ཏེ་ཞེས་པ་ནི་མེར་གྲུབ་པོ། །

[Block 1981]
འགྲོ་ཞེས་པ་ནི་སྙོམས་འཇུག་གི་ཚེ་ཟླ་བ་གཡོ་བ་རླུང་གི་མཚན་ཉིད་དང་ལྡན་པས་སོ། །

[Block 1982]
རླུང་ནི་རབ་ཏུ་གྲགས་ཞེས་པ་པྲ་ཏི་སྟེ་རབ་ཏུ་བསྒྲུབ་བོ། །

[Block 1983]
བདེ་བ་ཞེས་པ་ནི་སྙོམས་འཇུག་གིས་སམ་ཞུ་བ་ལ་བརྟེན་པའི་ཆོས་སོ། །

[Block 1984]
ནམ་མཁའི་ཁམས་ཞེས་བྱ་བ་ནི་ཁྱད་པར་ནམ་མཁའི་མཚན་ཉིད་དང་ལྡན་པ་ནམ་མཁའི་སྒྲུབ་པའོ། །

[Block 1985]
ལྔ་ཡིས་ཡོངས་སུ་བསྐོར་ཞེས་པ་ནི་དེ་དག་ཡོངས་སུ་འདུས་པའོ། །

[Block 1986]
གང་ཕྱིར་འབྱུང་བ་ཆེ་བདེ་ཞེས་བྱ་བ་ནི་འབྱུང་བ་ལས་གྱུར་ཅིང་བསྐྱེད་པའོ། །

[Block 1987]
དེའི་ཕྱིར་ཞེས་པ་ནི་འདུས་བྱས་པའི་ཕྱིར་རོ། །

[Block 1988]
བདེ་བ་དེ་ཉིད་མིན་ཞེས་པ་ནི་ལྷན་སྐྱེས་མ་ཡིན་པའོ། །

[Block 1989]
དེ་དག་གིས་ནི༌[^881]འབྱུང་བ་དང་ལྡན་པའི་ལུས་ཀྱི་བསྐྱེད་པ་རྒྱུ་བྱེད་པ་ཙམ་གྱིས་ལུས་དག་པར་བསྟན་ནས། ད་ནི་ལྷན་ཅིག་སྐྱེས་པ་ཡིན་པས་ལུས་དག་པ་ལ་བསྟན་པའི་ཕྱིར། ལྷན་སྐྱེས་དགའ་ཞེས་པ་ནི་གཟོད་མ་ཉིད་ནས་ལུས་དང་སེམས་དང་ལྷན་ཅིག་སྐྱེས་པའི་ཕྱིར་རོ། །

[Block 1990]
འོ་ན་ལྷན་སྐྱེས་ཡིན་ཞེ་ན། །ལྷན་ཅིག་སྐྱེས་པ་གང་སྐྱེས་ཞེས་པ་དོན་དམ་དེ༌[^882]ལུས་དང་ལྷན་ཅིག༌[^883]སྐྱེས་པས་དེར་འགྱུར་རོ། །

[Block 1991]
གང་སྐྱེས་པ་ཞེས་པ་ནི་དེ་དང་ལྡན་པ་གང་དང་གང་ཡང་ངོ་། །ལྷན་ཅིག་སྐྱེས་པར་དེ་བརྗོད་དོ་ཞེས་པ་ནི་དེ་དང་དེ་ཀུན་ནོ། །

[Block 1992]
དེ་ཕྱིར་ཀུན་རྫོབ་ཀུན་དུ་ལུས་དང་ལྷན་ཅིག་སྐྱེས་པས་རང་བཞིན་ལྷན་ཅིག་སྐྱེས་ཞེས་བརྗོད་པ་སྟེ། དོན་དམ་ལྷན་སྐྱེས་བཞིན་དུ་ཀུན་རྫོབ༌[^884]ཀྱང་ཡིན་ལ་དེས་ན་ལུས་དག་པར་བསྟན་ཏོ། །

[Block 1993]
ད་ནི་ཕྱག་རྒྱ་ཆེན་པོའམ་དབྱེར་མེད་ལྷན་སྐྱེས་བསྟན་པའི་ཕྱིར། རྣམ་པ་ཐམས་ཅད་ཅེས་པ་ནི་བསྐྱེད་རིམ་ལ་སོགས་པ་ཆོས་དུ་མའོ། །

[Block 1994]
སྡོམ་ཞེས་པ་ནི་མདོར་བསྡུས་པའོ། །

[Block 1995]
ཅི་ཞེས་པ་ནི་སེམས་སུ་སྡུད་པའི་ཚུལ་ལོ། །

[Block 1996]
དེ་ཡང་ཆོས་དུ་མ་དེ་དག་ཇི་ལྟར་བསྡུ་ཞེ་ན། ཕྱག་རྒྱ་རྒྱུ་དང་བྲལ་ཞེས་པ་ནི་བདག་མེད་མའི་ཕྱག་རྒྱ་སྔགས་ལ་སོགས་པ་བྲལ་བ་སྟོང་པ་སྟེ། ཤེས་རབ་ཀྱིས་བསྡུས་པའོ། །

[Block 1997]
དེ་བཞིན་དཀྱིལ་འཁོར་དང་ལྷ་དང་ཕྱག་རྒྱ་དང་སྦྱིན་སྲེག་དང་མཆོད་སྦྱིན་ལ་སོགས་པས་བརྟག་པ་རྣམས་མེད་པ་དང་། ཡང་དག་པའི་སྔགས་ལ་སོགས་པ་ཡོད་པར་བསྟན་པ་ནི་ལེའུ་ལྔ་པ་ལྟར་ཤེས་པར་བྱ་སྟེ། དེ་ཡང་ཐབས་ཀྱིས་བསྡུས་པ་ནི་ཡོ་གའི་རྣལ་འབྱོར་པའོ། །

[Block 1998 [VERSE]]
སྙིང་རྗེ་ནི་སྣང་བ་ཀུན་ནོ། །
ཐབས་ནི་བདེ་བའི་རོར་གྱུར་པའོ། །

[Block 1999]
དེ་དག་བསྡུས་ཏེ་མི་གདགས་པའི་ཕྱིར་ཡེ་ཤེས་ནི་སྟོང་པའོ། །

[Block 2000]
ཐབས་ནི་སྙིང་རྗེའོ། །
--- END BLOCKS ---
