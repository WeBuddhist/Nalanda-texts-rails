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
[Block 2031]
དེའི་རྒྱུ་ཅན་གྱི་ཕན་པ་མ་ཡིན་པར་འགྱུར་བ་ནི་ཉམས་པར་དོགས་པ་ཞེས་སྨོས་པ་སྟེ། ཕན་པ་མཆོག་ཏུ་བྱེད་པ་དེ་ལའོ། །

[Block 2032]
ལྷ་རྒྱལ་སྲིད་ཀྱི་དཔལ་འདི་ལྟར་ཚབ་བཙལ་ཀྱང་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་བྱམས་པའི་དབང་གིས་བསྟན་ཏོ། །

[Block 2033]
ལྷ་ཅི་མི་མཁྱེན་ནམ༌[^1237]ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་སྤོབས་པའི་དབང་དུ་བྱས་པའོ། །

[Block 2034]
ཚུལ་དང་འགལ་བའི་ལམ་ཞེས་བྱ་བ་འདི་དང་། རྒྱལ་པོ་ཆེན་པོ་ཐམས་ཅད་སྒྲོལ་འདི་ནི་དོན་འདི་ལྟ་བུ་དག་ལ་ཞེས་བྱ་བ་འདི་ནི་ཡིད་གཅུགས༌[^1238]པའི་དབང་ཉིད་དུ་བསྟན་ཏོ། །

[Block 2035]
གྲགས་པ་ཐོབ་པ་སེང་གེའི་ཁྲི་ལ་འོས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་ནི་འདིར་མཐོང་བའི་འབྲས༌[^1239]བུ་བསྐྱེད༌[^1240]པའོ། །

[Block 2036]
ས་ཡི་བདག་པོ་རྣམས་ཀྱི་ཚུལ་ཉེས་སྐྱོན། །ཞེས་བྱ་བ་འདིས་ནི་ཚུལ་མ་ཡིན་པ་བསྟན་ཏོ། །

[Block 2037]
འདི་ལ་མང་དུ་གསོལ་ཀྱང་ཅི་འཚལ་ཏེ། །ཞེས་བྱ་བ་འདིས་ནི་ཉམས་པར་དོགས་པ་བསྟན་ཏོ། །

[Block 2038]
ངོ་བཟློག༌[^1241]ཕོད་པ་ནི་དེ་ཐམས་ཅད་ལ་སྩལ་བ༌[^1242]མེད་པ་ཉིད་དུ་རྒྱལ་པོ་དེ་མི་འདོད་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2039]
རང་བཞིན་གྱིས༌[^1243]ཁོང་ངས་ཤིང་ངོ་ཚ་བཞིན་དུ་མགོ་སྨད་དེ་ཞེས་བྱ་བ་ལ། རང་བཞིན་གྱིས༌[^1244]ཁོང་ངས་པ་རྒྱུ་དང་བཅས་པར་མངོན་པར་གྱུར་པའི་ཕྱིར་དེ་ལ་སྤྱུགས་པ་ལ༌[^1245]ཁོང་ངས་པ༌[^1246]སྟེ། དེ་སྐྱོན་གྱིས་སྤྱུགས་པར་གྱུར་ཀྱང་བུ་དང་བྲལ་བས་སེམས་ཡོངས་སུ་གདུངས་པར་གྱུར་པའོ། །

[Block 2040]
ཁྱེད་དེ་ལྟར་གལ་གྱིས་འཆུ༌[^1247]ན་ཞེས་བྱ་བ་འདིས་ནི་བུ་དང་བྲལ་བའི་སྡུག་བསྔལ་གྱིས་ཀྱང་ཁོང་ངས་པའི་སྡུག་བསྔལ་དུ་བསྟན་ཏོ། །

[Block 2041]
དེ་ལ་རེ་ཞིག་ཉིན་ཞག་གཅིག་ཙམ་ཞིག་ཅེས་བྱ་བ་འདིས་ནི་བུ་ལ་བྱམས་པར་དམིགས་པ་དང་བཅས༌[^1248]ཏེ། དེ་ལ་རྗེས་སུ་དཔག་པའི་རྒྱུ་ནི་བབ་ཅོལ་དུ་བསྟན་པར་མི་ནུས་པའི་ཕྱིར་རོ། །

[Block 2042]
དེ་ལྟར་བགྱིའོ་ཞེས་བྱ་བ་ནི་དེ་ལྟར་བྱེད་པ་དང་རྗེས་སུ་མཐུན་པ་དེའོ། །

[Block 2043]
མྱ་ངན་གྱི་སྡུག་བསྔལ་གྱི་ཤུགས་ཀྱིས་ཞེས་བྱ་བ་ལ། མྱ་ངན་གྱི་སྡུག་བསྔལ་དང་བྲལ་བས་སྨྲེ་བའི་རྒྱུའི་རྣམ་པར་རྟོག་པ་མྱ་ངན་ནོ། །

[Block 2044]
སྡུག་བསྔལ་ནི་སྡུག་པ་དང་བྲལ་བ་སྟེ། ལུས་ཀྱིས་མི་འདོད་པར་རིག་པར་བྱའོ། །

[Block 2045]
དེ་ཉིད་ཀྱི་ཤུགས་ནི་མྱ་ངན་གྱི་སྡུག་བསྔལ་གྱི་ཤུགས་སོ། །

[Block 2046]
དེ་བས་ན་ཤིན་ཏུ་ཡང་སྐྱོ་བས་མི་དགའ་བར་གྱུར་པའོ། །

[Block 2047]
མི་དཀའ་བ༌[^1249]དང་ཚིག་མི་གསལ་བ་གང་ཡིན་པ་དེ་ནི་ཚིག་མི་གསལ་བ་སྟེ། མི་དགའ་བ་དང་ཚིག་མི་གསལ་བ་ནི་མི་དགའ་བས་ཚིག་མི་གསལ་བའོ། །

[Block 2048]
མཆི་མས་བརྣངས་ཤིང་སྐད་འཛེར་བ་གང་ཡིན་པ་དེ་ནི་དེ་སྟེ། མཆི་མས་བརྣངས་ཤིང༌[^1250]སྐད་འཛེར་བའོ་ཞེས་བསྟན་པ་ཡིན་ནོ། །

[Block 2049]
དབུགས་ཀྱིས༌[^1251]བརྣངས་པ་ནི་གནས་ལས༌[^1252]ཉམས་པའོ། །

[Block 2050]
མི་གསལ་བ་ནི༌[^1253]ཚིག་ནི༌[^1254]འཁྲུགས་པའི་ཚིག་སྟེ། ཚིག་འབྲུ་མི་གསལ་བའི་ཚིག་གང་ཡིན་པ་དེ་ནི་ཚིག་མི་གསལ་བའོ། །

[Block 2051]
འཇམ་པོར་སྩལ་བ་ཞེས་བྱ་བ་ནི་དེ་ལྟར་བྱའོ་ཞེས་བྱ་བ་ལ་སོགས་པས་བསྟན་ཏོ། །

[Block 2052]
ཉེས་པ་སྤྱོད་པ་མ་མཐོང་ན། །ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་རྒྱལ་པོའི་བཀའ་ཞེས་བྱ་བ་ལ་སོགས་པ༌[^1255]བསྟན་ཏོ། །

[Block 2053]
ཡུལ་ནས་འབྱིན་ཞེས་བྱ་བ་ལ་སོགས་པ༌[^1256]འདི་ལ་མང་དུ་གསོལ་ཏེ་ཞེས་བྱ་བ་ལ་སོགས་པས་བསྟན་ཏོ། །

[Block 2054]
འདུལ༌[^1257]དང་འགལ་བའི་ལམ་མི་འགྲོ། །ཞེས་བྱ་བ་འདིས་ནི་མི་དགེ་བ་ལས་ལྡོག་པ་བསྟན་ཏོ། །

[Block 2055]
བག་མེད་པ་ལའང་ང༌[^1258]མི་དགའ། །ཞེས་བྱ་བ་འདིས་ནི་དགེ་བ་ལ་འཇུག་པ་བསྟན་ཏེ། བག་ཡོད་པ་གང་ཞེ་ན། དགེ་བའི་ཆོས་རྣམས་བསྒོམ་པའོ༌[^1259]ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 2056]
ཉེས་པར་བྱས་པ་མ་མཐོང་ན། །ཞེས་བྱ་བ་ནི་དེ་ལ༌[^1260]འཁྲུགས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2057]
ཁྱོད་ནི་ཆགས་པ་མེད༌[^1261]ལ་དགའ་བར་གྱུར། །ཞེས་བྱ་བ་ལ་ཆགས་པ་མེད་པའི་སེམས་དང་ལྷན་ཅིག་སྐྱེས་པས་སོ། །

[Block 2058]
ཆགས་པ་ལ་དགའ་བ་ཞེས་བྱ་བ་ནི་ལྷག་པར་ཆགས་པའི་སེམས་དང་ལྷན་ཅིག་སྐྱེས་པས་སོ།[^1262] །རང་གི་ཆོས་ཞེས་བྱ་བ་ནི་རང་གི་གཞུང་ལུགས་ཏེ། མི་འདའ་བ་དང་ཡོངས་སུ་མི་གཏོང་བ་ནི་རང་གི་གཞུང་ལུགས་ལས་མི་འདའ་བ་ཞེས་གཉིས་པའི་ཕྱེད་ཀྱིས་བསྟན་ཏོ། །

[Block 2059]
བྱང་ཆུབ་སེམས་དཔས༌[^1263]སྙིང་བརྩེ་བ་ལ་སོགས་པའི༌[^1264]ཤས་ཆེ་བ་དང་། སྐྱེ་བོ་སློང་བ་ལ་བྱམས་པ་དང་། རང་གི་བསྟན་པ་ཕུན་སུམ་ཚོགས་པ་བསྟན་པའི་ཕྱིར་དང་། ཡུལ་ཤི་བི་པ་རྣམས་ནི་ཞེས་བྱ་བའི་ཚིག་ཀྱང་ནི། འཇིག་རྟེན་དོན་དུ་ངའི་ལུས་འཛིན་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་གཉིས་ཀྱིས་བསྟན་ཏོ། །

[Block 2060]
རང་གི་མིག་དང་མགོ་ཡང་ངས་སྦྱིན་ན། །ཞེས་བྱ་བ་འདིའི༌[^1265]སྒྲུབ་པ་ནི། །འཇིག་རྟེན་དོན་དུ་ངའི་ལུས་འཛིན་ན། །ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་བསྟན་པ་ཡིན་ནོ། །

[Block 2061]
མིག་དང་མགོ་སྨོས་པ་ནི་གཙོ་བོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2062]
གཉིས་པོ་དེ་ནི་ཡུལ་གྱི་བྱེད་དམ། ཡང་ན་གདོང་ནི༌[^1266]ཐམས་ཅད་ཡིན་ནོ་ཞེས་བརྗོད་དེ། དེ་ཡང་སྣ་ནི་མཆོག་ཏུ་གྱུར་པ་ཡིན་ལ། དེ་བས་ཀྱང་མཆོག་ཏུ་གྱུར་པ་ནི་མིག་གོ་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 2063]
ཡང་ན་མགོ་སྨོས་པས༌[^1267]ནི་རང་གི་སྲོག་གཏོང་བ་བསྟན་ཏོ། །

[Block 2064 [VERSE]]
མིག་ཅེས་བྱ་བ་འདིས་ནི་ལུས་ཀྱི་སྦྱིན་པའོ། །
ཕྱི་རོལ་ནོར་ལྟ་སྨོས་ཀྱང་ཅི་ཞིག་དགོས། །

[Block 2065]
ཞེས་བྱ་བ་འདི༌[^1268]སྒྲུབ་པ་ནི། ཕྱི་རོལ་ནོར༌[^1269]སྦྱིན་སྨོས་ཀྱང་ཅི་ཞིག་དགོས། །ཞེས་བྱ་བ་འདིས་བསྟན་ཏོ། །

[Block 2066]
རང་གི་ལུས་ཀྱང་ཞེས་བྱ་བ་ནི་བསྟན་མ་ཐག་པར་བཤད་པ་སྟོན་ཏོ། །

[Block 2067]
རང་གི་མིག་དང་མགོ་ཡང་ངས་སྦྱིན་ན། །ཞེས་བྱ་བ་འདིས་ནི། སྐྲག་པར་བྱས་ན༌[^1270]མི་སྦྱིན་ཞེས་སྨོས་ཏེ། ཕྱི་རོལ་གྱི་དངོས་པོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2068]
གང་སྔར་བསྟན་པའི་རང་གི་བསྟན་པ་ཕུན་སུམ་ཚོགས་པ་བསྟན་པའི་ཕྱིར་ཞེས་བྱ་བ་དེའི་དབང་དུ་བྱས་པ་ནི། ཤི་བི་པ་རྣམས་ཐམས་ཅད་ཀྱིས༌[^1271]ཞེས་བྱ་བ༌[^1272]སྨོས་སོ། །

[Block 2069]
ངེས་པ་ནི་བསྐྲད་པར་འདོད་པ༌[^1273]ངེས་པར་བྱས་པའོ། །

[Block 2070]
ཅི་ཐོབ་དང་ཞེས་བྱ་བ་ནི་དེ་ཉིད་ངེས་པར་བྱས་པའི་ཕྱིར་ང་ལས་ཐོབ་པའི་ནོར་ཅི་ཡོད་པའོ། །
--- END BLOCKS ---
