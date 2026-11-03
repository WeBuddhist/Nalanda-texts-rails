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
རྨད་དུ་བྱུང་བ་ནི་མི་གཡོ་བར་དེ་བཞིན་འདུག་པ་སྟེ། ཤ་ཆོད་པ་དང་བཅད་པའི་ཚོར་བའི་སྡུག་བསྔལ་ཟིལ་གྱིས་ནོན་པའི༌[^1061]ཕྱིར་རོ། །

[Block 1822]
བདེན་ནམ་བརྫུན་ཞེས་དཔྱོད་ཅིང་ངོ་མཚར་སྐྱེས་ཞེས་བྱ་བ་ནི་ངོ་མཚར༌[^1062]རྨད་དུ་བྱུང་བ་སྐྱེས་པས༌[^1063]སོ། །

[Block 1823]
དེ་ལ་བསྟོད་ཅིང་ཕྱག་ཀྱང་འཚལ་བར་གྱུར། །ཞེས་བྱ་བ་ནི་དེ་ལ་བསྟོད་པ་དང་ཕྱག་འཚལ་བར་གྱུར་པ་སྟེ། དེ་ལ་བསྟོད་པ་དང་འདུད་པ་ནི།[^1064] ཁྲག་དང་ཤ་སྦྱིན་པས་ཕྱག་འཚལ་བའོ། །

[Block 1824]
གུས་པའི་དབང་གིས་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིའི་བསྡུས་པའི་དོན་ནི་གསང་ཚིག་དང་། གཙོ་བོ་དང་། སྤྲོ་བའི་ནུས་པ་བསྟན་ཏོ། །

[Block 1825]
དང་པོའི་རྐང་པས་ནི་གསང་ཚིག་གི་ནུས་པ་བསྟན་ཏེ། [^1065]གུས་པ་དང་གྲགས་པས་ནི་གསང་ཚིག་གི་ནུས་པ་བསྐྱེད་པས་སོ། །

[Block 1826]
ཚིག་རྐང་གཉིས་པས་ནི་བདག་པོའི་ནུས་པ་བསྟན་ཏེ། དཔལ་ཞེས་སྨོས་པའི་ཕྱིར་རོ། །

[Block 1827]
ཁྱེད་ཀྱི་མཐུས་བསྐྱབས༌[^1066]ཞེས་བྱ་བ་འདིས་ནི་སྤྲོ་བའི་ནུས་པ་བསྟན་ཏོ། །

[Block 1828]
བརྒྱ་བྱིན་མགོན་དུ་གྱུར་ལ་ཞེས་བྱ་བ་ལ། ནུས་པ་ཡིན་པས་བརྒྱ་བྱིན་ཏེ། སྤྲོ་བའི་ཡོན་ཏན་སྟན་པར་བྱེད་པའི་མིང་སྨོས་པས། སྤྲོ་བའི་ནུས་པའི་རྗེས་སུ་བསྟན་པའི་དོན་ཏོ། །

[Block 1829]
དེ་ལས་བྱང་ཆུབ་སེམས་དཔའི་སྤྲོ་བ་འདི་ཁྱད་པར་དུ་བསྟན་པའི་ཕྱིར། ཁྱོད་ལྟ་བུའོ་བརྒྱལ་བར༌[^1067]བགྱིས་ཕ༌[^1068]དེ་བས་ནའོ། །

[Block 1830]
ཐམས་ཅད་སའི་བདག་པོ་འམ་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིའི་བསྡུས་པའི་དོན་ནི། གཅིག་ཏུ་མངོན་པར་མཐོ་བའི་སྤྱོད་པ་ལས་ཀྱང་བརྩམས་པ་མ་ཡིན་ལ། ངེས་པར་ལེགས་པ་ལས་ཀྱང་བརྩམས་པ་མ་ཡིན་ནོ། །

[Block 1831]
རྣམ་པར་གྲོལ་བའམ་ཞེས་སྨོས་པ་ལ། རྣམ་པར་གྲོལ་བ་ནི་འདིར་ཉན་ཐོས་དང་རང་སངས་རྒྱས་ཏེ་རྣམ་པ་གཉིས་སོ། །

[Block 1832]
མངོན་པར་མཐོ་བ་ནི་འདོད་ཆགས་དང་བྲལ་བ་དང་འདོད་ཆགས་དང་མ་བྲལ་བའི་དབྱེ་བས་སོ། །

[Block 1833]
འདོད་ཆགས་དང་བྲལ་བའི་དབང་དུ་བྱས་ནས། ཚངས་པའམ་ཞེས་སྨོས་སོ། །

[Block 1834]
འདོད་པ་སྤྱོད་པའི་མངོན་པར་མཐོ་བ་ཡང་རྣམ་པ་གཉིས་ཏེ། ལྷ་དང་མིའི་དབང་དུ་བྱས་པའོ། །

[Block 1835]
ནོར་གྱིས་ཕྱུག་པའམ་དབང་པོའམ༌[^1069]ཞེས་བྱ་བ་ལ། ལྷའི་མངོན་པར་མཐོ་བ་ཡང་རྣམ་པ་གཉིས་ཏེ། རྒྱལ་ཆེན་རིགས༌[^1070]བཞི་དང་སུམ་ཅུ་རྩ་གསུམ་པའི་དབྱེ་བས་སོ། །

[Block 1836]
དེ་ལ་རྒྱལ་ཆེན་རིགས༌[^1071]བཞི་དང་མངོན་པར་མཐོ་བའི་དབང་དུ་བྱས་ནས། ནོར་གྱིས་ཕྱུག་པའམ་ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 1837]
སུམ་ཅུ་རྩ་གསུམ་པའི་དབང་དུ་བྱས་ནས་དབང་པོའམ་ཞེས་བསྟན་ཏོ། །

[Block 1838]
མིའི་མངོན་པར་མཐོ་བའི་ཁྱད་པར་གྱི་དབང་དུ་བྱས་ནས། ཐམས་ཅད་སའི་བདག་པོའམ་ཞེས་བྱ་བ་ཡིན་ཏེ། འཁོར་ལོས་སྒྱུར་བའི་རྒྱལ་སྲིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 1839]
བཞེད་པའི་དོན་ནི་མི་རིང་སྟེ། རྩོལ་ཕོད་པ༌[^1072]གང་ཡིན་པས་ཐམས་ཅད་འཐོབ་པར་ནུས་པའོ། །

[Block 1840]
རྙེད་པར་བྱ་དཀའ་བ་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིའི་བསྡུས་པའི་དོན་ནི་སྲིད་པའི་ལོངས་སྤྱོད་ལ་མི་གནས་པ་སྟེ། ཉེས་པ་གསུམ་གྱིས་མ་རུངས་པར༌[^1073]བྱས་པར་སྟོན་ཏེ། དེ་ལ་ཉེས་པ་གསུམ་ནི་རྒྱུ་དང་། ངོ་བོ་དང་། འབྲས་བུའི་ཉེས་པས་སོ། །

[Block 1841]
རྒྱུའི་ཉེས་པའི་དབང་དུ་བྱས་ནས་རྙེད་པར་དཀའ་ལ་ཞེས་བྱ་བ་སྟེ། གལ་ཏེ་འབད་པ་ཕུན་སུམ་ཚོགས་པས་ཐོབ་པར་འགྱུར་བ་ཡིན་ཡང་རྟག་པ༌[^1074]མེད་པས་སོ། །

[Block 1842]
འདི་ལ་གང་གི་ཕྱིར་མི་རྟག་པ་ཡིན་ཞེ་ན། རང་བཞིན་གྱི་སྐྱོན་གྱི་དབང་དུ་བྱས་ནས། འཇིག་པར་སླ་བ་དང་ཞེས་བྱ་བ་ཡིན་ཏེ། རང་གི་ངང་གིས་འཇིག༌[^1075]པའོ། །

[Block 1843]
འཇིག་པར་སླ་བ་ཡིན་ཡང་། རང་གི་བྱ་བ་བྱེད་པར་ནུས་པར་གྱུར་ན། དེ་ལྟ་ན་ཡང་འདོད་པར་བྱ་བ་ཡིན་ན། དེ་མེད་པར་བསྟན་པའི་ཕྱིར། ཆོག་པའི་བདེ་མེད་ཅེས་སྨོས་ཏེ། དེ་ལ་དེ་ཉེ་བར་ལོངས་སྤྱོད་པས་ཕྱིས་ཀྱང་སྤྱད་མི་དགོས་པར་མི་འགྱུར་བས་སོ། །ཅིའི་ཕྱིར་ཞེ་ན། རབ་ཏུ་ཞི་མེད་པ་ཞེས་སྨོས་ཏེ། གང་ཕུན་སུམ་ཚོགས་པ་དོན་དུ་གཉེར་བ་དེ་དག་ལ་ཆགས་པ་ལས་ཞི་བར་མི་ནུས་སོ། །ཅིའི་ཕྱིར་ཞེ་ན། སྲིད་པའི་ལོངས་སྤྱོད་བདེ་བ་ཞེས་བྱ་བ་ཡིན་ཏེ། འདིས་ནི་འདོད་པའི་ཁམས་ཀྱི་འདོད་པར་རྟོགས་པར༌[^1076]བྱའོ། །ཅི་ལྟར་འདི་རྟོགས་པར་བྱ་ཞེ་ན། ལྷ་དབང་དཔལ་ཞེས་སྨོས་སོ། །

[Block 1844]
དེ་ལས་གཞན་པ་ཞེས་བྱ་བ་འདིས་ནི་ཐམས་ཅད་སའི་བདག་པོ་དང་། ནོར་གྱིས་ཕྱུག་པ་གཉིས་ནི་ཐ་མལ་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 1845]
བདག་གི་སྡུག་བསྔལ་ཟད་པ་ཙམ་གྱི་ཕྱིར། །ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་ནི། མྱ་ངན་ལས་འདས་པ་དོན་དུ་མི་གཉེར་བ་ཉིད་ཀྱི་དབང་དུ་བྱས་པ་སྟེ།[^1077] དེ་མི་བཞེད་པའི་ཕྱིར་དང་། ཚངས་པ་ཡང་ཡོངས་སུ་དགག་པར༌[^1078]བྱས་པ་ཡིན་ནོ། །

[Block 1846]
བདག་གི་སྡུག་བསྔལ་ཟད་པ་ཙམ་གྱི་ཕྱིར། །ཞེས་བྱ་བ་ནི། ཉན་ཐོས་དང་རང་སངས་རྒྱས་ཀྱི་མྱ་ངན་ལས་འདས་པ་ཐོབ་པའོ། །

[Block 1847]
སྡུག་བསྔལ་མི་བཟད་ནད་ཀྱིས་ཉེན་པའི་ཞེས་བྱ་བ་འདི་ལ། རབ་ཏུ་ཉེན་པ་ནི་རྟག་ཏུའོ། །

[Block 1848]
མི་བཟད་པ་ནི་ཤས་ཆེ་བའོ། །

[Block 1849]
སྡུག་བསྔལ་མི་བཟད་པ་དེས་བྱས་པའི་ངལ་བ་ནི་སྡུག་བསྔལ་མི་བཟད་པའི་ངལ་བ་སྟེ། དེའི་ནད་ཀྱིས་ཉེན་པའོ། །

[Block 1850]
གལ་ཏེ་འདི་ཐམས་ཅད་དོན་དུ་མི་གཉེར་ན་གཞན་གང་དོན་དུ་གཉེར་བ་ཡིན་ཞེ་ན། བསོད་ནམས་འདི་ཡིས་ཐམས་ཅད་ཅེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 1851]
ཐམས་ཅད་གཟིགས་པའི་གོ་འཕང་ཐོབ་ཅིང་། ཞེས་བྱ་བ་འདིས་ནི་ཤེས་བྱ༌[^1079]སྒྲིབ་པ་སྤངས་པ་བསྟན་ཏོ། །

[Block 1852]
སྐྱོན་གྱི་དགྲ་བཏུལ་ནས་ཞེས་བྱ་བ་འདིས་ནི་ཉོན་མོངས་པའི་སྒྲིབ་པ་ཐམས་ཅད་སྤངས་སོ། །

[Block 1853]
བསོད་ནམས་འདི་ཡིས་ཞེས་བྱ་བ་འདིས་ནི་ཚོགས་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 1854]
ཐམས་ཅད་གཟིགས་པའི་གོ་འཕང་ཐོབ་ཅིང་སྐྱོན་གྱི་དགྲ་བཏུལ་ནས། ཞེས་པ༌[^1080]འདིས་ནི་འབྲས་བུ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 1855]
རྒ་བ་དང་ན་བ་ཞེས་བྱ་བའི་ཚིགས་སུ་བཅད་པ་འོག་མ་ཕྱེད་ཀྱིས་ནི་དོན་ཐམས་ཅད་ཀྱི་བྱ་བ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏེ། རྒ་ནད་འཆི་བའི༌[^1081]རླབས་ཆེན་པོ་དང་ཆོས་མཐུན་པ་སྟེ། ཆེན་པོ་ཡིན་པའི་ཕྱིར་དང་། ཡང་དང་ཡང་དུ་རྒྱུན་མི་འཆད་པར་འཇུག་པའོ། །

[Block 1856]
འདི་ལྟ་བུའི་བརྩལ་བ༌[^1082]ཞེས་བྱ་བ་ནི། སངས་རྒྱས་ཉིད་དོན་དུ་གཉེར་བའི་བརྩལ་བ༌[^1083]གང་ཡིན་པ་སྟེ། བྱང་ཆུབ་ཀྱི་སེམས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1857]
ལས་འདི་ཞེས་བྱ་བ་ནི། རང་གི་ཤ་དང་ཁྲག་སྦྱིན་པའི་ལས་སོ། །

[Block 1858]
ཁྱོད་ལྟ་བུ་ཞེས་བྱ་བ་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་སོ། །

[Block 1859]
འཇིག་རྟེན་ཕན་པའི་ཕྱིར་ལགས་ཀྱང་། །ཞེས་བྱ་བ་ནི་འགྲོ་བ་མཐའ་དག་ཡོངས་སུ་བསྐྱབ་པའི་ཕྱིར་ཏེ། ཐམས་ཅད་ཀྱི་ནོར་བུར་ཁྱོད་གྱུར་པས་བདག་ཀྱང་འགྲོ་བའི་ཁོངས་སུ་གཏོགས་པར་གྱུར་པ་སྟེ། དེ་བས་ན་ཇི་ལྟར་ཡང་དོན་དུ་གཉེར་པར་བྱའོ། །

[Block 1860]
བདག་ཅག་རང་ལ་ཕན་འཚལ་བ། །ཞེས་སྨོས་ཏེ། ཡང་འབྱོར་པ་དོན་དུ་གཉེར་བའོ་ཞེས་བྱ་བ་སངས་རྒྱས་ཉིད་ཐོབ་པའོ། །
--- END BLOCKS ---
