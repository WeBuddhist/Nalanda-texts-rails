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
རྒྱུའི་ཟུང་དུ་འཇུག་པ༌[^1379]ལ་བཞི་སྟེ། ཉན་ཐོས་དང་། རྣལ་འབྱོར་སྤྱོད་པ་དང་། དབུ་མ་དང་། སྔགས་ཀྱི་དབྱེ་བས་སོ། །

[Block 2032]
འབྲས་བུ་ལ༌[^1380]ཡང་བཞི་སྟེ། རིགས་དང་། ཡོན་ཏན་དང་། བྱ་བ་དང་། རྫས་ཀྱི་བྱེ་བྲག་གིས་སོ། །

[Block 2033]
ཀུན་ཏུ་བསྡུས་པས་དབྱེ་བ་ཉི་ཤུ་རྩ་བརྒྱད་ཀྱི་ཏིང་ངེ་འཛིན་ཏོ། །

[Block 2034]
དེ་རྣམས་ཀྱི་དོན་ནི་སྔོན་དུ་བཤད་ཟིན་ཏོ། །

[Block 2035]
དེ་བཞིན་དུ་ཡང་ཕུང་པོ་ལྔ་དང་འབྱུང་བ་ཆེན་པོ་དང་རྣམ་པར་ཤེས་པ་དང་། དབང་བསྐུར་བ་དང་། ལམ་དང་དེ་བཞིན་གཤེགས་པ་དང་། ཡེ་ཤེས་ལྔའི་ངོ་བོ་ཉིད་རིམ་པ་ལྔའོ། །

[Block 2036]
དེ་ལ་གཟུགས་ཀྱི་ཕུང་པོའི་སྐུ་རྣམ་པར་དག་པ་ནི་རྡོ་རྗེ་བཟླས་པའི་རིམ་པ་སྟེ། དེས་ཁྲག་དང་ཁུ་བ་ལས་བྱུང་བའི་གཟུགས་ཀྱི་ཕུང་པོ་ཕྲ་མོའི་རྣལ་འབྱོར་གྱིས་སྤོང་བའི་ཕྱིར་རོ། །

[Block 2037]
ཚོར་བའི་ཕུང་པོ་རྣམ་པར་དག་པས་སེམས་རྣམ་པར་དག་པ་སྟེ་བདེ་བ་ལ་སོགས་པའི་རྣམ་པ་ཅན་གྱི་སེམས་དེས་སྤོང་བའི་ཕྱིར་རོ། །

[Block 2038]
འདུ་ཤེས་ཀྱི་ཕུང་པོ་རྣམ་པར་དག་པས་བདག་བྱིན་གྱིས་རློབ་པ་སྟེ། གཟུགས་ལ་སོགས་པའི་ཡུལ་རྣམས་ཀྱི་མཚན་མ་ཐམས་ཅད་སྒྱུ་མ་ཙམ་དུ་མཐོང་བས་སོ། །

[Block 2039]
འདུ་བྱེད་ཀྱི་ཕུང་པོ་རྣམ་པར་དག་པས་མངོན་པར་བྱང་ཆུབ་པའི་རིམ་པ༌[^1381]སྟེ། འདོད་ཆགས་དང་འདོད་ཆགས་དང་བྲལ་བ་དང་འདོད་ཆགས་བར་པའི་འདུ་བྱེད༌[^1382]རྣམས་དེས་སྤོང་བའི་ཕྱིར་རོ། །

[Block 2040]
རྣམ་པར་ཤེས་པའི་ཕུང་པོ་རྣམ་པར་དག་པ་ནི་ཟུང་དུ་འཇུག་པའི་རིམ་པ་སྟེ། བག་ཆགས་དང་བཅས་པའི་རྣམ་པར་ཤེས་པའི་ཕུང་པོ་གནས་གྱུར་པས། འཇིག་རྟེན་ལས་འདས་པའི་རྡོ་རྗེ་ལྟ་བུའི་སྐུར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2041]
སའི་ཁམས་རྣམ་པར་དག་པས་རྡོ་རྗེ་བཟླས་པ་སྟེ་སྲ་བའི་གནས་བརྒྱད་ལ་བརྒྱབ་པ་ལས་སྔགས་སྐྱེས་པའི་ཕྱིར་རོ། །

[Block 2042]
ཆུའི་ཁམས་ཀྱི་རང་བཞིན་ནི་སེམས་རྣམ་པར་དག་པ་སྟེ་དེས་རྣམ་ཤེས་དང་ཡེ་ཤེས་ཀྱི་དྲི་མ་བཀྲུས༌[^1383]པའི་ཕྱིར་རོ། །

[Block 2043]
མེའི་ཁམས་ཀྱི་ངོ་བོ་ཉིད་ནི་བདག་ལ་བྱིན་གྱིས་རློབ་པ་སྟེ། དེས་དངོས་པོའི་མཚན་མའི་བུད་ཤིང་སྒྱུ་མ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་གྱི་མེས་བསྲེགས་པའི༌[^1384]ཕྱིར་རོ། །

[Block 2044]
རླུང་གི་ཁམས་ཀྱི་ངོ་བོ་ཉིད་མངོན་པར་བྱང་ཆུབ་པའི་རིམ་པ་སྟེ། འདུ་བྱེད་ཐམས་ཅད་འོད་གསལ་བ་དེས་སྦྱངས་པའི་ཕྱིར་རོ། །

[Block 2045]
ནམ་མཁའི་ཁམས་ཀྱི་ངོ་བོ་ཉིད་ཟུང་དུ་འཇུག་པ་སྟེ། ནམ་མཁའ་དང་མཚུངས་པ་མཐའ་ཡས་ཤིང་དྲི་མ་མེད་པ་གཉིས་སུ་མེད་པའི་ཡེ་ཤེས་གཅིག་པུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2046]
དེ་ལ་རྣམ་པར་ཤེས་པ་ལྔ་ནི་གཟུགས་ལ་སོགས་པ་སོ་སོར༌[^1385]སྣང་བའི་རྣམ་པར་ཤེས་པ་དང་། འཇུག་པའི་རྣམ་པར་ཤེས་པ་དང་། ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་དང་། ཉོན་མོངས་པ་ཅན་གྱི་ཡིད༌[^1386]རྣམ་པར་ཤེས་པ་དང་། ཀུན་གཞི་རྣམ་པར་ཤེས་པའོ། །

[Block 2047]
དེ་ལ་གཟུགས་ལ་སོགས་པའི་སོ་སོར་སྣང་བའི་རྣམ་པར་ཤེས་པའི་ངོ་བོ་ནི༌[^1387]རྡོ་རྗེ་བཟླས་པའི་རིམ་པ་སྟེ་དེ་ནི་བཟླས་པ་ལ་སོགས་པའི་སངས་རྒྱས་ཐམས་ཅད་ཀྱི་ངོ་བོར་གཟུགས་ལ་སོགས་པ་མཐོང་བའི་ཕྱིར་རོ། །

[Block 2048]
སྒོ་ལྔ་རྣམ་པར་དག་པ་ནི་སེམས་ལ་དམིགས་པ་ཐོབ་པའི་རིམ་པ་སྟེ། སྣང་བ་ཐོབ་པ་ལ་དེ་ཐིམ་པའི་ཕྱིར་རོ། །

[Block 2049]
ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་རྣམ་པར་དག་པ་ནི་བདག་བྱིན་གྱིས་རློབ་པ་སྟེ། སྒྱུ་མ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་མངོན་དུ་གྱུར་པས་ཡིད་ཀྱི་རྣམ་པར་རྟོག་པ་ནུབ་པའི་ཕྱིར་རོ། །

[Block 2050]
ཉོན་མོངས་པ་ཅན་གྱི་ཡིད་རྣམ་པར་དག་པ་ནི་མངོན་པར་བྱང་ཆུབ་པ་སྟེ་བདག་ཏུ་ལྟ་བ༌[^1388]ལ་སོགས་པའི་ཉོན་མོངས་པ་དེས་སྦྱངས་པའི་ཕྱིར་རོ། །

[Block 2051]
ཀུན་གཞི་རྣམ་པར་ཤེས་པ་རྣམ་པར་དག་པ་ནི་ཟུང་དུ་འཇུག་པ་སྟེ་བག་ཆགས་དང་བཅས་པའི་སྒྲིབ་པ་ཐམས་ཅད་རྣམ་པར་ཤེས་པ་ཐམས་ཅད་ཀྱི་གཞིར་གྱུར་པ་ནུབ་པའི་ཕྱིར་རོ། །

[Block 2052]
དབང་བསྐུར་བ་ལྔ་ནི་དེ་ལ་རིག་པའི༌[^1389]དབང་གི་ངོ་བོ་ནི་རྡོ་རྗེ་བཟླས་པའི་རིམ་པ་སྟེ་རིགས་ལྔའི༌[^1390]རྣམ་པར་ཤེས་པ་རྣམ་པར་དག་པའི་ཕྱིར་རོ། །

[Block 2053]
ཕྱིར་མི་ལྡོག་པའི་དབང་གི་ངོ་བོ་ནི་སེམས་རྣམ་པར་དག་པའི་རིམ་པ་སྟེ་ས་བཅུ་པ་ལས་སླར་མི་ལྡོག་པའི་ཕྱིར་རོ། །

[Block 2054]
གསང་བའི་དབང་གི་ངོ་བོ་ནི་བདག་ལ་བྱིན་གྱིས་རློབ་པའི་རིམ་པ་སྟེ་དེས་ནི་ཁ་དོག་དང་དབྱིབས་ཅན་ཡེ་ཤེས་ཀྱི་སྐུ་ཐོབ་པའི་ཕྱིར་རོ། །

[Block 2055]
ཇི་སྐད་དུ།

[Block 2056 [VERSE]]
དེས་དུས༌[^1391]བརྩམས་ནས་དེ་ནི་མི་ལྡོག་པ། །
དེ་ཡི་ཁ་དོག་དབྱིབས་དང་ཕྱག་མཚན་ཅན། །
བསམ་གྱིས་མི་ཁྱབ་རྣམ་པར་སྨིན་པའི་སྐུ། །
སྡོམ་པ་དེ་ལས་བྱ་བ་བྱས་པས༌[^1392]ཐོབ། །

[Block 2057]
ཅེས་བྱུང་ངོ་། །ཤེས་རབ་ཡེ་ཤེས་ཀྱི་དབང་གི༌[^1393]ངོ་བོ་ཉིད༌[^1394]ནི་མངོན་པར་བྱང་ཆུབ་པའི་རིམ་པ་སྟེ་དེས་དེ་ཐོབ་པའི་ཕྱིར་རོ། །

[Block 2058]
ངག་གི་དབང་བསྐུར་བའི་ངོ་བོ་ནི་ཟུང་དུ་འཇུག་པའི་རིམ་པ་སྟེ་སྲིད་པ་དང་མྱ་ངན་ལས་འདས་པ་རོ་གཅིག་པ་སྟེ་དེ་ཁོ་ན་ཉིད་ཐོབ་པའི་ཕྱིར་རོ། །

[Block 2059]
ཚོགས་ཀྱི་ལམ་གྱི་ངོ་བོ་ཉིད་ནི་རྡོ་རྗེ་བཟླས་པ་སྟེ། བཟླས་པའི་ཡན་ལག་བཅུ་གཉིས་མངོན་དུ་བྱས་པའི་ཕྱིར་རོ། །

[Block 2060]
སྦྱོར་བའི་ལམ་གྱི་ངོ་བོ་ནི་སེམས་ལ་དམིགས་པ་སྟེ་སྣང་བ་ལ་སོགས་པའི་ཡེ་ཤེས་ཀྱི༌[^1395]ས་བཅུ་ལ་སྦྱོར་བའི་ཕྱིར་རོ། །

[Block 2061]
མཐོང་བའི་ལམ་གྱི་ངོ་བོ་ནི་རང་བྱིན་གྱིས་རློབ་པ་སྟེ། ཡན་ལག་བདུན་དང་ལྡན་པའི་ཡིད་ཀྱི་རང་བཞིན་གྱི་སྐུ་སྒྱུ་མའི་དེ་ཁོ་ན་ཉིད་དུ་མཐོང་བའི་ཕྱིར་རོ། །

[Block 2062]
བསྒོམ་པའི༌[^1396]ལམ་གྱི་ངོ་བོ་ནི་མངོན་པར་བྱང་ཆུབ་པའི་རིམ་པ༌[^1397]སྟེ་ཕྱི་དང་ནང་གི་མངོན་པར་བྱང་ཆུབ་པའི་རིམ་པའི་ལམ་གྱི་ཡན་ལག་བརྒྱད་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 2063]
མི་སློབ་པའི་ལམ་གྱི་ངོ་བོ་ནི༌[^1398]ཟུང་དུ་འཇུག་པའི་རིམ་པ་སྟེ། དེ་ལས་སློབ་པའི་རྒྱུ་མེད་པའི་ཕྱིར་རོ། །

[Block 2064]
རྣམ་པར་སྣང་མཛད་ཀྱི་ངོ་བོ་ནི་རྡོ་རྗེ་བཟླས་པའི་ངོ་བོ་སྟེ། རླུང་རྣམ་པར་དག་པས་མེ་ལོང་ལྟ་བུའི་ཧ་ཧུ་མེད་པར་སྣང་བའི་ཕྱིར་རོ། །

[Block 2065]
རིན་ཆེན་འབྱུང་ལྡན་གྱི་ངོ་བོ་ནི་སེམས་རྣམ་པར་དག་པ་སྟེ་རང་བཞིན་གྱིས་ཚོགས་འགོག་པས་ཐམས་ཅད་མཉམ་པ་ཉིད་དུ་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2066]
སྣང་བ་མཐའ་ཡས་ཀྱི་ངོ་བོ་ནི་བདག་ལ་བྱིན་གྱིས་རློབ་པ་སྟེ་ཆོས་ཐམས་ཅད་སྒྱུ་མ་ཉིད་དུ་སོ་སོར་རྟོག་པའི་ཕྱིར་རོ། །

[Block 2067]
མི་བསྐྱོད་པའི་ངོ་བོ་ནི་མངོན་པར་བྱང་ཆུབ་པ་སྟེ་འོད་གསལ་བ་ནི་ཤིན་ཏུ་རྣམ་པར་དག་པ་ཆོས་ཀྱི་དབྱིངས་ཀྱི་ཡེ་ཤེས་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2068]
དོན་ཡོད་གྲུབ་པའི་ངོ་བོ་ཉིད་ནི་ཟུང་དུ་འཇུག་པའི་རིམ་པ་སྟེ་བྱ་བ་བྱས་པའི་ཕྱིར་རོ། །

[Block 2069]
ཡེ་ཤེས་ལྔ་ནི་འདིར་དེ་བཞིན་གཤེགས་པ་དང་དབྱེར་མེད་པའི་ཕྱིར་མ་བསྟན་ཏོ། །

[Block 2070]
གཏི་མུག་རྣམ་པར་དག་པའི་ངོ་བོ་ནི་རྡོ་རྗེ་བཟླས་པ༌[^1399]སྟེ། སྔགས་ཐམས་ཅད་ལ་མ་རྨོངས་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
