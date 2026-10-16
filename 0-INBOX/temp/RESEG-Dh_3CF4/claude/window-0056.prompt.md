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
[Block 1961]
སྙིང་རྗེའི་གཞུ་དྲག་པ༌[^1171]ཉིད་ཀྱིས་ནི་སྦྱིན་པ་འཕེན་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 1962]
དེ་དང༌[^1172]ཞེས་བྱ་བ་ནི་འགྲོ་བ་རྣམས་ཀྱི་དབུལ་བའི་སྡུག་བསྔལ་འབྱུང་བ་དང་ངོ་། །བསླང་ས་པ་བས་ལྷག་པ་ནི་འདོད་པས༌[^1173]ལྷག་པ་སྟེ་འདིས་ནི་སྦྱིན་པའི་དངོས་པོ་མང་དུ་གཏོང་བར་བསྟན་ཏོ། །

[Block 1963]
ཉོན་མ༌[^1174]མོངས་པར་ཞེས་བྱ་བ་འདིས་ནི་བསམ་པ་ཕུན་སུམ་ཚོགས་པར་བསྟན་ཏེ། བདག་ནི༌[^1175]འཁོར་བའི་ཕུན་སུམ་ཚོགས་པའི་བདག་ཉིད་མྱ་ངན་ལས་འདས་པར་ཡོངས་སུ་བསྔོ་བས་སོ། །

[Block 1964]
ཚིག་འཇམ་པོ་དང་། གུས་པ་དང་ཡིད་དུ་འོང་བ་ཞེས་བྱ་བས༌[^1176]ནི་སྦྱོར་བ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏེ། ལུས་དང་ངག་གི་ལས་ཀྱིས་སློང་བ་རྣམས་ཀྱི་ཡིད་དུ་འོང་བའི་ཕྱིར་རོ། །

[Block 1965]
འདིས་ནི་འདས་པའི་དུས་སུ་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བསགས་པ་བསྟན་ཏོ། །

[Block 1966]
ད་ནི་དུས་མཚམས་ཀྱི་ཉི་མ་དག་ནས་ཞེས་བྱ་བ་ནས་བརྩམས་པ་ནི་ཚུལ་ཁྲིམས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་ལྡན་པར་བསྟན་ཏོ། །

[Block 1967]
གངས་རི་འདྲ་བ་ཞེས་སྨོས་པས་ནི་མདོག་དང་ཚད་ཀྱི་ཡོན་ཏན་བསྟན་ཏོ། །

[Block 1968]
དྲེགས་པའི་རྡུལ་གྱིས་ཞེས་བྱ་བ་འདིས་ནི་དྲེགས་པའི་གནས་སྐབས་སོ། །

[Block 1969]
དུལ་བ་ཞེས་སྨོས་པས་ནི་ལེགས་པར་བསླབ་པ༌[^1177]གཟུང་ངོ་། །ཅིའི་ཕྱིར་འབྲས་བུ་མ་སྨོས་ཤེ་ན། ཚད་དང་མཚན་ཉིད་སྨོས་པ་ཉིད་ཀྱིས་མ་བསྟན་ཀྱང་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 1970]
སྦྱིན་གཏོང་གི་ཁོང་པ་ཞེས་བྱ་བ་ནི་སྦྱིན་པ་གཏོང་བའི༌[^1178]གནས་སོ། །

[Block 1971]
དེས་ཉུལ་དུ་སོང་སྟེ་དགའ༌[^1179]བའི་ཁྱད་པར་ཞེས་བྱ་བ་སྦྱིན་གཏོང་གི་ཁྱད་པར་མ་མཐོང་བ་ཡིན་ཡང་སྔོན་བཅས་པའི་ཕྱིར་དགའ་བ་ཡོད་པ་ཡིན་ལ། མཐོང་བས་ཀྱང་ཁྱད་པར་དུ་དགའ་བར་གྱུར་པའོ། །

[Block 1972]
དེ་ཙམ་དུ་ཞེས་བྱ་བ་ནི་འབྱོར་པའོ། །

[Block 1973]
བསླུ་བར༌[^1180]ནུས་སོ་ཞེས་བྱ་བ་ནི་སྟེར་བར་བྱེད་ནུས་པའོ། །

[Block 1974]
བཏང་ངོ་ཞེས་བྱ་བ་ནི་བརྫངས་པའོ། །

[Block 1975]
ཁྱོད་ནི་སྦྱིན་ལ་དཔའ་བ་དང་ཞེས་བྱ་བའི་ཚིགས༌[^1181]བཅད་འདིའི་བསྡུས་པའི་དོན་ནི་རྣམ་པ་གཉིས་ཀྱིས་སླབ༌[^1182]པའི་འདོད་པ་འགྲུབ་པར་གྱུར་པ༌[^1183]སྟེ། བསླངས་པའི༌[^1184]དངོས་པོ་དང་སྦྱིན་པ་པོ་ཕུན་སུམ་ཚོགས་པ་སྟེ། དེ་གཉིས་གང་ཡང་རུང་བས་མ་ཚང་བ་ནི་སློང་བའི་དོན་གྲུབ་པར་མི་འགྱུར་རོ། །

[Block 1976]
རླབས་ཆེ་བའི་སློང་བ་དེས་ཕོད་པ་ནི་རླབས་ཆེར་སློང་ཕོད་པའོ། །

[Block 1977]
ཡང་ན་རླབས་ཆེ་བ་ཡང་ཡིན༌[^1185]པས་རླབས་ཆེར་སློང་བ་དེ༌[^1186]དེས་ཕོད་པའོ། །

[Block 1978]
བརྐམ་པ་དང་ཕྲག་དོག་གི་སྐྱོན་གྱིས་ཡིད་དཀྲུགས་པ་ཞེས་བྱ་བ་ལ། བརྐམ་པ་ནི་གླང་པོ་ཆེ་ལའོ། །

[Block 1979]
ཕྲག་དོག་ནི་བྱང་ཆུབ་སེམས་དཔའི་ཕུན་སུམ་ཚོགས་པ་མི་བཟོད་ཅིང་ཞེ་སྡང་བ་སྟེ། རང་བཞིན་གྱིས་ས་གཞན་དུ་གྱུར་པས་དགྲ་བོར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 1980]
འདོད་ཆེན་གྱིས་སྦྱར་ཏེ་ཞེས་བྱ་བ་ནི་ངན་པའི་སྦྱོར་བས་གྲགས་པ་མ་ཡིན་པ་དང་། འདོད་ཆེན་གྱི་སྦྱོར་བར་འགྱུར་ཞིང་ལེགས་པའི་སྤྱོད་པ་ཉིད་ཀྱིས་ནི་གྲགས་པར་འགྱུར་རོ། །

[Block 1981]
ཆོས་མ་ཡིན་པ་ནི་བརྐམ་པ་དང་། ཕྲག་དོག་དང་། ཞེ་སྡང་གིས་ཡིད་དཀྲུགས་པ་ཉིད་ཀྱིས་གྲུབ་པ་ཉིད་དེ། དེ་བས་ན་གྲགས་པའི་རྒྱུར་གྱུར་པ་དང་། བྱང་ཆུབ་སེམས་དཔའ་དང་ལྡན་པས་འགའ་ཞིག་འདོད་ཆེན་གྱིས་སྦྱར་བ་ཡིན་ནོ་ཞེས་སེམས་པའོ། །ཅིའི་ཕྱིར་དང་པོའི༌[^1187]ཞེ་ན། ནོར་གྲུབ་ནོར་ནི་ཞེས་བྱ་བའི་ཚིགས་བཅད་བརྩམས་ཏེ། རྒྱལ་པོའི་གཙུག་ལག་དག་ལ་མཁས་གྱུར་དང་། ། ཆོས་ལ་དགའ་བས་དེ་ནས་གླང་ཆེན་བྱིན།[^1188] །ཚུལ་དང་འགལ་བས་དེ་ནི་གཡོས་མ་གྱུར། །ཞེས་བྱ་བ་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན། ནོར་གྲུབ་ནོར་ནི་ཆོས་ལམ་མི་མཐུན་པའི་ཕྱིར་དང་། གླང་པོ་ཆེ་བྱིན་པ་ནི་ཆོས་ཀྱི་ལམ་ཡིན་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་འདི་ཉིད་བསྟན་པ་ནི་ཆོས་ལ་དགའ་བ་ཞེས་སྨོས་སོ། །

[Block 1982]
གཡོས་མ་གྱུར་ཞེས་བྱ་བ་ནི་སྦྱིན་པ་ལས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1983]
དེ་གཉི་ག༌[^1189]སྦྱིན་པ་ཞེས་ངེས་པར་བཟུང་བས༌[^1190]བསྙད་པ༌[^1191]ཡིན་ཏེ། ངེས་པར་བཟུང་བ༌[^1192]ཐ་མལ་པའི་དོན་བསྒྲུབ་པའི༌[^1193]ཕྱིར། གཡོས་མ་གྱུར་ཞེས་བསྟན་པ་ཡིན་ནོ། །

[Block 1984]
གཞན་དུ་ན་ཁྱོད་ཅེས་བྱ་བའི་སྒྲ་བསྟན་ཏོ། །

[Block 1985]
ཀུན་ཏུ་འཁྲུགས་ཤིང་ཁྲོ་བ་དང་རྟབ་རྟབ་པོ་གང་ཡིན་པ་དེ་ནི་ཀུན་ཏུ་འཁྲུགས་ཤིང༌[^1194]ཁྲོ་བའི་རྟབ་རྟབ་པོའོ། །

[Block 1986]
ཁྲོ་བ་ནི་ད་ལྟར་བྱུང་བའི་གནོད་པ་ལ་རྟོག་པའི་སེམས་ཀྱིས་ཁོང་ནས་འཁྲུགས༌[^1195]པའོ། །

[Block 1987]
རྟབ་རྟབ་པོར་གྱུར་པ་ནི་སྐྱོབ་པ་སྟེ། གནོད་པར་བྱེད་པ་དེ་ལ་མི་སྡུག་པར་འདོད་པས་སོ། །

[Block 1988]
རྟབ་རྟབ་པོར་གྱུར་པ་དང་། མི་བཟོད་པ་ནི་རྟབ་རྟབ་པོར་གྱུར་ཅིང་མི་བཟོད་པ་དང་རྔམ་པའོ། །

[Block 1989]
རྟབ་རྟབ་པོར་གྱུར་པ་ནི་ལུས་ཀྱི་འགྱུར་བའི་རྣམ་པར་གཡོ་བའོ། །

[Block 1990]
མི་བཟོད་པ་ནི་གནོད་པ་བྱེད་པ་ལ་མི་བཟོད་པ་སྟེ། དེ་ཉིད་ཀྱི༌[^1196]རྔམ་པ་གང་ཡིན་པ་དེ་ནི་རྟབ་རྟབ་པོར་གྱུར་ནས་རྔམ་པས་དེ་བས་ནའོ། །

[Block 1991]
ཞེ་སའི་ཚུལ་ནི་ཞེས་བྱ་བའི་རིམ་པས་སོ། །ཞེས་བཏང་ནས་རྐོ་ལོང་དུ༌[^1197]གྱུར་པ་གང་ཡིན་པ་དེ་ནི་ཞེས་བཏང་ནས་རྐོ་ལོང་དུ་སྨྲས་པའོ། །

[Block 1992]
ཟ་བ་དག་ཅེས་བྱ་བ་ནི་དེ་ལྟ་བུའི་རྣམ་པ་གཞན་ཡང་དེའི་རང་བཞིན་ནོ། །

[Block 1993]
ཚུལ་དང་འགལ་བའི་ལམ་ཞེས་བྱ་བ་ལ། ཚུལ་ནི་སྙན་ངག་གི་བསྟན་བཅོས་ཏེ། དེ་ལས་འདས་པའི་ལན༌[^1198]ནི་ཚུལ་དང་འགལ་བའི་ལམ་མོ། །

[Block 1994]
ཇི་ལྟར་འགོ་བར་འགྱུར་ཞེས་བྱ་བ་ནི་ཡུན་རིང་པོ༌[^1199]དེ་ན་གནས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1995]
ཁྱོད་ཀྱི་དགྲ་ནི་མདུན་ནས་དགའ་བར་བྱེད། །ཅེས་བྱ་བ་ནི༌[^1200]འདིས་ནི༌[^1201]ལྷ་རིང་པོ་མི་ཐོགས་པར་ཕྱིར་རྒོལ་བར་བྱེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1996]
[^1202]དགོས་པའི་དབང་གིས་ཞེས་བྱ་བ་ནི༌[^1203]དགོས་པ་ལ་རྗེས་སུ་དགའ་བའོ། །

[Block 1997]
སྦྱིན་པ་ལ་ཆགས་ཤིང་ཞུགས་པ་ཞེས་བྱ་བ་ནི་སྦྱིན་པ་ལ༌[^1204]དགའ་བ་ཉིད་དུ༌[^1205]ཞུགས་པ་ཡིན་ཏེ། ཞེན་པ་ཉིད་དུ༌[^1206]ཞུགས་པ་སྟེ། གཏོང་བར༌[^1207]དཀའ་བ་དེས་སེམས་ཟིལ་གྱིས་གནོན་པ་ལ་གནས་པས། སྦྱིན་པ་ལ་ཆགས་ཤིང་ཞུགས་པ་འདི་ལྟར་ཤེས་པའོ། །

[Block 1998]
གང་གི་འགྲམ་པ་བུང་བ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་གསུམ་གྱི་ལན་ནི་ཚུལ་གྱི་རིམ་པ་ལ་མི་ལྟ་བ་ཞེས་བྱ་བ་འདི་ཡིན་ནོ། །

[Block 1999]
ཚུལ་དང་འགལ་བའི་ལམ་དུ་སོང་བ་འདིས་ཞེས་བྱ་བའི་ལན་ནི། རྒྱལ་སྲིད་ལ་དབང་བྱེད་དུ་བཅུག་པ་ནི༌[^1208]དེ་ལྟར་བྱ་བ་ཡང་མི་རིགས་སོ་ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 2000]
རྒྱལ་པོའི༌[^1209]དཔལ་ནི་ཇི་ལྟར་འགོ་བར་འགྱུར། །ཞེས་བྱ་བའི་ལན་ནི། འདིས་ཀྱང་རང་གི་གླང་པོ་ཆེ་བྱིན་ཟིན་པས་སྒྱུགས་པ༌[^1210]འདྲ་བ་ལྟ་སུ་ཞིག་འཕྲོག་པར་བྱེད་ཅེས་བྱ་བ་ཡིན་ནོ། །
--- END BLOCKS ---
