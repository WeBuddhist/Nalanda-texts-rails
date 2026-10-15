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
[Block 1821]
གང་ཞེས་སྨོས་པ་དེ་ཅི་གཞན་གང་ཡང་རུང་བ་ལ་དེ་བྱེད་པ་པོ་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་འདོད་པས་ལམ་དུ་འགྲོ་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རང་དགར་ལམ་དུ་འགྲོ་ན་སྟེ། གཞན་དབང་གིས་ནི་མ་ཡིན་ནོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1822]
ལམ་ཇི་སྲིད་དུ་འགྲོ་བ་ལ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་རྒྱང་གྲགས་རེ་རེར་རོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ལྟུང་བྱེད་ཉིད་ལ་འདིར་བྱེད་པ་པོ་ཉིད་ནི་འདི་ཡིན་ནོ་ཞེས་བྱ་བ་བྱེ་བྲག་མ་བྱས་པ་ཉིད་ཀྱི་ཕྱིར་རྟོགས་པའོ། །

[Block 1823]
དེའི་ཕྱེད་རེ་རེ་ཉིད་ནི་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ནི་རྒྱང་གྲགས་ཀྱི་ཕྱེད་རེ་རེར་ནི་བུད་མེད་ཀྱི་ཉེས་བྱས་ཀྱི་བྱེད་པ་པོ་ཉིད་ཡིན་ནོ། །

[Block 1824]
རྒྱང་གྲགས་རེ་རེར་རིག་པའི་སྐྱེས་པ་མེད་པར་བུད་མེད་དང་ལྷན་ཅིག་ཏུ༌[^1156]རང་དགར་ལམ་དུ་འགྲོ་བ་ལ་སྤྲོས་པ་ནི་ཤེས་པར་བྱའོ། །

[Block 1825]
ཅི་བུད་མེད་ཀྱི་གནས་སྐབས་ཐམས་ཅད་དགེ་སློང་གི༌[^1157]གནས་སྐབས་རྣམས་ལ་བྱེད་པ་པོ་ཉིད་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་བསེལ་བྱེད་པ་ནི་མ་གཏོགས་སོ་ཞེས་བྱ་བ༌[^1158]སྨོས་ཏེ། དགེ་སློང་དེ༌[^1159]ཉིད་ཅེས་བྱ་བ་འདི་ལ་འདིར་ཉེ་བར་གནས་པ་ཉིད་ཀྱི་ཕྱིར་རྟོགས་པར་བྱའོ། །

[Block 1826]
དེ་ལྟར་ཡང་ཤུགས་ཀྱིས་ཏེ། གང་གི་དབང་གིས༌[^1160]ཉེས་པ་འདི་མ་བསྐྱེད་པ་ཞེས་བྱ་བ་རིགས་པ༌[^1161]ཉིད་དུ་དེ་འགྱུར་རོ། །

[Block 1827]
དེས༌[^1162]ལམ་ནོར་བ་ལ་ལམ་དུ་འཇུག་པར་བྱེད་པ་ཡང་ངོ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བ་ནི་དགེ་སློང་ངོ་། །མི་ནུས་པ་ཁྲིད་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཁྲིད་པར་མི་ནུས་པ་ཞེས་བྱ་བ་ལྟུང་བའི༌[^1163]མི་མཐུན་པའི་ཕྱོགས་དོར་ནས་ཞེས་བྱ་བ་འདི་ལྟར་འདི་བསེལ་བྱེད་པས་རྩོམ་པའི་དོན་དུ་འདིའོ། །

[Block 1828]
བུད་མེད་དང་ལྷན་ཅིག་ལམ་དུ་འགྲོ་བའི་ལྟུང་བྱེད་དོ།། །།

[Block 1829]
གང་ལ་རྐུན་མ་དང་ལྷན་ཅིག་འགྲོ་བའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་གྲོང་འཇོམས་པར་བྱེད་པའི་ཆོམ་རྐུན་དག་གམ་ཤོ་གམ་འདྲལ་བའི་ཚོང་པ་དག་དང་ལྷན་ཅིག་འགྲོ་བ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདོད་པས་ལམ་དུ་འགྲོ་ནའོ་ཞེས་བྱ་བ་ཐམས་ཅད་ལ་འདི་སྦྱར་བར་བྱའོ། །

[Block 1830]
འདོད་པར་བྱེད་ཅིང་འཇུག་པ་ཞེས་བྱ་བ་འདི་ལ་ཡོངས་སུ་གྱུར་པར་རིག་པར་བྱའོ། །

[Block 1831]
ཟོལ་པ་དག་དང་རྐུ་ཐབས་སུ་རབ་ཏུ་བྱུང་བ་དག་དེ་དང་ལྷན་ཅིག་འགྲོ་བ་ལ་ནི་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ནི། འདིར་ཡང་འདོད་པས་ལམ་དུ་འགྲོ་ནའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྔར་བསྟན་པ་ཐམས་ཅད་སྦྱར་བར་བྱའོ། །

[Block 1832]
འདིར་རྒྱང་གྲགས་རེ་རེར་ནི་ཉེས་བྱས་ཞེས་བྱ་བ་ཐོབ་པའི་གནས་ལ་ཉེས་བྱས་ཞེས་སྨོས་པ་འདི་ཡིན་ཏེ། དེའི་དོན་དུ་སོ་སོར་ཉེས་བྱས་སོ། །

[Block 1833]
རྐུན་མ་དང་ལྷན་ཅིག་ལམ་དུ་འགྲོ་བའི་ལྟུང་བྱེད་དོ།། །།

[Block 1834]
ཅི་ཉི་ཤུ་མ་ལོན་པར་བསྙེན་པར་རྫོགས་པར་བྱེད་པའི་ལྟུང་བྱེད༌[^1164]ལ་བྱེད་པ་པོ་ཉིད་གང་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ཤེས་གཙོ་བོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་པོ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 1835]
བསྙེན་པར་རྫོགས་པར་བྱ་བ་ལ་ལོ་ཉི་ཤུ་མ་ལོན་པ་ཉིད་ལའོ་ཞེས་བྱ་བ་ནི་འཇུག་པ་གང་ལ་བྱེད་པ་པོ་ཉིད་ཅེས་བྱ་བ་འདི་ལ་བསྙེན་པར་རྫོགས་པར་ཞེས་འོག་ནས་སྟོན་ཏོ། །

[Block 1836]
ཡན་ལག་གང་གིས་བསྙེན་པར་རྫོགས་ཤེ་ན། དེའི་ཕྱིར་སྨོས་པ་ནི་མཁན་པོ་ཉིད་ཀྱིས་སོ་ཞེས་བྱ་བ་སྟེ། འོ་ན་འདིར་བསྙེན་པར་རྫོགས་པར་བྱེད་པ་ཐམས་ཅད་དབང་དུ་བྱེད་པ་ལྟུང་བའི་བཤད་པ་དང་དགེ་འདུན་ནོ། །

[Block 1837]
དེ་བས་ན་འགལ་ཚབས་དང་བཅས་པར་འགྱུར་རོ་ཞེ་ན། འོན་ཀྱང་བདེན་མོད་ཀྱི་ཉེས་བྱས་གཅིག་ཏུ་བྱས་ཏེ་ལྟུང་བྱེད་དོ། །

[Block 1838]
དེ་བས་ན་ཉེས་བྱས་འགྱོད་པ་དང་བཅས་པ་ཞེས་བྱ་བ་འདི་ལ་ལྟུང་བྱེད་ཀྱི་བཤད་པ་མི་བཟུང་བ་ཁོ་ན་མཁན་པོ་ལ་ལྟུང་བྱེད་དུ་འགྱུར་ཏེ། ལྷག་མ་ལ་ནི་ཉེས་བྱས་ཞེས་བྱ་བར་རབ་ཏུ་འབྱེད་པ་ལས་མངོན་པར་འདོད་པའོ། །

[Block 1839]
དེའི་ཕྱིར་འདིར་འདི་དག་གིས༌[^1165]ཉེས་པ་སྟེ། དགེ་སློང་གིས་སྦོམ་པོའི༌[^1166]ཕྱིར་བསྙེན་པར་རྫོགས་པར་བྱས་ནའོ་ཞེས་བྱ་བ་ནི་ལྟུང་བྱེད་ཅེས་སྦྱར་རོ། །

[Block 1840]
གང་ཟག་དེ་ལ་བསྙེམ་པར༌[^1167]མ་རྫོགས་ལ་དགེ་སློང་དེ་རྣམས་ཀྱང་གཟུང་བར༌[^1168]བྱའོ་ཞེས་བྱ་བའི་མདོ་ལས་མཁན་པོ་ཉིད་ཀྱིས་བསྙེན་པར་རྫོགས་པའི་དབང་དུ་མཛད་ནས་འདི་བཅའ་བ་མཛད་དོ། །

[Block 1841]
འདི་ནི་གླེང་གཞི་ལས་ཤེས་པ་ཡིན་ཏེ༌[^1169]མཁན་པོ་འཕགས་པ་མཽད་གལ་གྱི་བུ་ཆེན་པོས་ལོ་བཅོ་བརྒྱད་ལོན་པ་རྣམས་ལ་བསྙེན་པར་རྫོགས་པའི་དབང་དུ་མཛད་ནས་འདི་བརྟགས༌[^1170]པའོ། །

[Block 1842]
དེས་དེ་ལ་ལོན་པ་ཉིད་མི་དྲི་བར་མི་བྱའོ་ཞེས་བྱ་བ་ལ་དེས་ཞེས་བྱ་བ་ནི་མཁན་པོའོ། །

[Block 1843]
དེ་ལ་ཞེས་བྱ་བ་ནི་བསྙེན་པར་རྫོགས་པར་བྱ་བ་ལའོ། །

[Block 1844]
རྫོགས་པ་ཞེས་བྱ་བ་ནི་ལོ་ཉི་ཤུ་ལོན་པ་ཉིད་མི་དྲི་བར་མི་བྱ་སྟེ་དྲི་བ་ཁོ་ནར་བྱའོ། །

[Block 1845]
གཞན་གྱིས་ཀྱང་མི་བྱའོ་ཞེས་བྱ་བ་ལ༌[^1171]མཁན་པོ་ལས་གཞན་བསྙེན་པར་རྫོགས་པར་བྱེད་པ་པོ་དག་གིས་ཀྱང་བསྙེན་པར་རྫོགས་པར་བྱེད་པ་དེ་ལ་མི་དྲི་བར་མི་བྱའོ། །

[Block 1846]
ངེས་པར་མི་ཤེས་པར་དེ་བསྙེན་པར་རྫོགས་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བ་ནི་བསྙེན་པར་རྫོགས་པའོ། །

[Block 1847]
མི་ཤེས་པར་དེ་བསྙེན་པར་རྫོགས་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 1848]
གང་ཞིག་འདི་རྣམས་ལ་སྨད༌[^1172]པར་བྱ་བ་ཞེས་བྱ་བ་ནི། དགེ་སློང་ལྷག་མ་རྣམས་ལ་ཉེས་བྱས་སྟོན་པར་བྱེད་པ་སྟེ། འདི་ནི་དེའི་བསྡུ་བ་ཡིན་ནོ། །

[Block 1849]
རྣམ་པ་ཐམས་ཅད་དུ་ལོ་ཉི་ཤུ་ལོན་པ་ལ་ནི་བསྙེན་པར་རྫོགས་པ་འཆགས་སོ་ཞེས་བྱ་བ་ནི། ཡོངས་སུ་མ་རྫོགས་པའི་འདུ་ཤེས་ཅན་ལ་བསྙེན་པར་རྫོགས་པར་བྱེད་པ་པོ་རྣམས་ལ་བློ་མི་མཐུན་པར་བྱེད་པ་ཉིད་ལ་ཡང་མ་དྲིས་སམ་མ་བརྗོད་པ་དག་ལ་ཡང་ཤེས་པར་བྱ་བ་རྣམ་པ་ཐམས་ཅད་དུ་ལོ་ཉི་ཤུ་ལོན་པ་ལ་བསྙེན་པར་རྫོགས་པ་འཆགས་ཏེ་གཞན་ནི་མ་ཡིན་ནོ། །

[Block 1850]
འདུ་ཤེས་སམ་ཡིད་གཉིས་ཟ་བ་ལ་སོགས་པ་རྣམས་ལ་ནི་འདིར་ནུས་པ་མ་ཡིན་ནོ། །

[Block 1851]
ཅིག་ཤོས་ལ་ནི་ལོན་པར་འདུ་ཤེས་པ་ཉིད་ནའོ་ཞེས་བྱ་བ་ནི། ཅིག་ཤོས་ཉི་ཤུ་མ་ལོན་པ་ལ་ལོ་ཉི་ཤུ་ལོན་པ་ཉིད་དུ་ཤེས་ན་བསྙེན་པར་རྫོགས་པ་འཆགས་སོ། །

[Block 1852]
མི་ཤེས་པ་དང་མི་དྲན་པ་དང་ཡིད་གཉིས་ཟ་བ་དག་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི།[^1173] ཅིག་ཤོས་ལ་བསྙེན་པར་རྫོགས་པ་འཆགས་སོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1853]
མི་ཤེས་པ་ཞེས་བྱ་བ་ནི་ལོ་གྲངས་མི་ཤེས་པས་སོ། །

[Block 1854]
མི་ཤེས་པ་དང་མི་དྲན་པ་དང་ཡིད་གཉིས་ཟ་བ་རྣམས་ནི་མི་ཤེས་པ་དང་མི་དྲན་པ་དང་ཡིད་གཉིས་ཟ་བ་དང་། ལོ་ཉི་ཤུ་མ་ལོན་པ་ལ་ལོ་ཉི་ཤུ་ལོན་པ་ཉིད་དུ་འདུ་ཤེས་པ་ཉིད་ཡིན་ནོ། །

[Block 1855]
གལ་ཏེ་མི་ཤེས་པ་ལ་སོགས་པར་གྱུར་ན་དེ་ལྟར་ཡང་གྲགས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1856]
འདིར་བྱེད་པ་པོ་རྣམས་ལྷ༌[^1174]འདུ་ཤེས་ཡོངས་སུ་མ་རྫོགས་པ་ཉིད་ཡིན་ཡང་གྲགས་པའོ། །

[Block 1857]
ཇི་ལྟར་ཉི་ཤུ་མ་ལོན་པ་ཞིང་ཉིད་ཡིན་ཡང༌[^1175]ཞེ་ན། འདིར་རྣམ་པ་གཉིས་ཀྱིས༌[^1176]ཞིང་ཉིད་དུ་རྣམ་པར་གཞག་སྟེ་དངོས་པོ་དང་ཡིད་ཀྱིས་སོ། །

[Block 1858]
ཡང་དག་པར་ལན་པར༌[^1177]བྱེད་པའི་ཡིད་ཀྱི་དབང་གིས༌[^1178]ཞིང་ཉིད་ཡིན་ཏེ༌[^1179]འོན་ཏེ། གང་ཞིག་ལོ་ཉི་ཤུ་མ་ལོན་པ་ལ་ལོ་ཉི་ཤུ་ལོན་པར་འདུ་ཤེས་པར་གྱུར་ན་ལོ་ཉི་ཤུ་མ་ལོན་པ་ལ་བསྙེན་པར་རྫོགས་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 1859]
ཆོ་ག་འདི་མི་ཤེས་ན་མཁན་པོས་མ་དྲིས་པའམ་དགེ་འདུན་གྱིས་ཀྱང་མ་དྲིས་པར་གྱུར་ན་དུས་དེ་ལ་གཏོགས་པ་ནི་མ་གྲགས་པ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1860]
འོ་ན་འདི་ལ་ཚར་བཅད་པའི་བློས་ཡང་དག་པར་གནས་པ་མ་ཡིན་ནོ་ཞེ་ན། འོན་ཀྱང་བདེན་མོད་ཀྱི་ཚར་བཅད་པའི་བློ་ཡིས་ནི་མ་གྲགས་པ་ཡན་ལག་མ་ཡིན་ཏེ། འོན་ཀྱང་ཞིང་ཉིད་དོ། །
--- END BLOCKS ---
