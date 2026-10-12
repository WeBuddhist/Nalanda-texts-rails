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
[Block 1786]
ཚིག་གི་དོན་རིམ་པས་སྟོན་པ་ནི་གོ་རིམས་སོམོ། །

[Block 1787]
འདི་ལྟ་སྟེ།

[Block 1788]
[^1255]ལེའུ་དང་པོ་ལས།

[Block 1789]
བཛྲ་དྷྲྀཀ །ཛི་ན་ཛིཀ །རཏྣ་དྷྲྀཀ །ཨཱ་རོ་ལིཀ །པྲཛྙཱ་དྷྲྀཀ་ཅེས་བྱ་བས་དང་པོ་དེ་བཞིན་གཤེགས་པ་ལྔ་ཕྱུང་བའོ། །

[Block 1790]
དེའི་རྗེས་ལ་མོ་ཧ་ར་ཏི། དྭེ་ཥ་ར་ཏི། རཱ་ག་ར་ཏི། བཛྲ་ར་ཏི་ཞེས་བྱ་བས་དགའ་མ་རྣམས་ཕྱུང་བའོ། །

[Block 1791]
དེ་ནས་ཡང་ཡ་མཱནྟ་ཀྲྀཏ། པྲཛྙཱནྟ་ཀྲྀཏ། པད་མཱནྟ་ཀྲྀཏ། བིགྷྣཱནྟ་ཏ་ཀྲྀཏ། ཅེས་བྱ་བས་ཁྲོ་བོ་ཕྱུང་བ་ཞེས་གོ་རིམས༌[^1256]བྱ་བའི་ཡན་ལག་བདུན་པའོ། །

[Block 1792 [HEADING]]
#### མིང། ^1-6-8-0

[Block 1793]
མིང་དང་ཉེ་བར་བསྟན་པ་ནི་མིང་དང་ཉེ་བར་བསྟན་པ་དག་གོ། །

[Block 1794]
མིང་ཅན་རྟོགས་པར༌[^1257]བྱེད་པའི་སྒྲ་ནི་མིང་ངོ་། །དེ་ཡང་རྣམ་པ་གཉིས་ཏེ། དོན་གྱི་རྒྱུ་མཚན་ཅན་དང་། རང་གཟུགས༌[^1258]ཀྱི་རྒྱུ་མཚན་ཅན་ནོ། །

[Block 1795]
དེ་ལ་དོན་གྱི་རྒྱུ་མཚན་ནི། དོན་གྱི་དབང་གིས་དོན་གྱི་བྱ་བ་ལ་ལྟོས་པས་སོ། །

[Block 1796]
རིགས་ལ་སོགས་པའི་དོན་རང་གཟུགས་སུ་བསྡུས་པར་བྱ་སྟེ། ཇི་ལྟར་དོན་ཡིན་པ་དེ་ལྟ་བུར་གྱུར་པའི་མིང་ཅན་རྟོགས་པར་བྱེད་དོ། །

[Block 1797]
དཔེར་ན་འཚེད་པ་དང་། བྱེད་པ་དང་དྲ་བར་བྱེད་པའོ། །

[Block 1798]
རང་གཟུགས་ཀྱི་རྒྱུ་མཚན་ཅན་ནི་མིང་དང་རྟོགས་པར་བྱེད་པའི་ཐབས་ཙམ་ཡིན་ཏེ། རང་གཟུགས་ཙམ་ལ་ཕན་པར་བྱེད་པ་ཡན་ལག་གི་དོན་མ་གཏོགས་པར་རང་གི་བརྡའི་དབང་གིས་དེ་ལྟ་བུར་གྱུར་པའི་མིང་ཅན་ཡང་རྟོགས་པར་བྱེད་དོ། །

[Block 1799]
དཔེར་ན་གླང་པོའི་རྣ་བ་ཅན་དང་། རྟའི་རྣ་བ་ཅན་ནོ། །

[Block 1800]
དེ་ལ་བཅོམ་ལྡན་འདས་ཁམས་གསུམ་མ་ལུས་པའི་བདེན་པ་མཁྱེན་པས༌[^1259]ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་ཀྱི་དངོས་པོ་ཐམས་ཅད་ཀྱི་བདེན་པ་གཟིགས་ནས་མིང་བཏགས་པ༌[^1260]ལ་རང་གཟུགས་ཀྱི་རྒྱུ་མཚན་ཅན་གྱི་སྒྲ་མེད་དེ། [^1261]དཔེར་ན་མི་བསྐྱོད་པ་ཞེས་བྱ་བ་ནི་ཉོན་མོངས་པ་དང་ཤེས་བྱའི་སྒྲིབ་པའི་བག་ཆགས་ཀྱི་རླུང་གིས་མ་བསྐྱོད་པས་མི་བསྐྱོད་པ་སྟེ། ཆོས་ཀྱི་དབྱིངས་ཀྱི་ཡེ་ཤེས་ཀྱི་ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1801]
རྣམ་པར་སྣང་མཛད་པས་ན་རྣམ་པར་སྣང་མཛད་དེ་མེ་ལོང་ལྟ་བུའི་ཡེ་ཤེས་གསལ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1802]
དེ་ལྟར་ན་མིང་གི་བརྡ་དོན་དང་ལྡན་པ་གཞན་དག་ཏུ་ཡང་ཤེས་པར་བྱའོ་ཞེས་མིང་བསྟན་པ་ཞེས་བྱ་བ་ཡན་ལག་བརྒྱད་པའོ། །

[Block 1803 [HEADING]]
#### ཉེ་བར་བསྟན་པ། ^1-6-9-0

[Block 1804]
འདི་ལྟར་བྱ་བའི་འབྲས་བུ་ཡང་དག་པར་བསྟན་པ་ནི་ཉེ་བར་བསྟན་པའོ། །

[Block 1805]
འདི་ལྟ་སྟེ།

[Block 1806 [VERSE]]
དེ་ལྟར་བྱས་ན་སངས་རྒྱས་དང་། །
བྱང་ཆུབ་སེམས་དཔའ་གྲགས་ཆེན་མཉེས། །

[Block 1807]
ཞེས་འབྱུང་ངོ་། །དེ་བཞིན་དུ་ཡང་རྣལ་འབྱོར་འདི་དག་ཉིད་ཀྱིས་ནི། མྱུར་དུ་སངས་རྒྱས་ཉིད་ཐོབ་འགྱུར། །ཞེས་ཉེ་བར་བསྟན་པ་ཞེས་བྱ་བའི་ཡན་ལག་དགུ་པའོ། །

[Block 1808]
ལྔ་པ་དང་དྲུག་པ་གཉིས་གཉིས་སུ་བྱས་ཏེ། མདོ་སྡེ་ལ་སོགས་པ་རྒྱུད་ཀྱི་ཡན་ལག་བཅུ་གཅིག་ཡིན་ནོ་ཞེས་བྱ་བའི་སྒྲ་ནི་རྣམ་པའི་དོན་ཏོ། །

[Block 1809]
དེས་ན་དེ་ལྟ་བུའི་རྣམ་པ་ཅན་གཞན་རྣམས་ཀྱང་ཤེས་པར་བྱའོ། །

[Block 1810]
འདི་ལྟ་སྟེ། སྤྱིར་བཏང་བ་དང་། དམིགས་ཀྱིས་བསལ་བ་དང་། གཞན་གྱི༌[^1262]ཆོས་ཡོངས་སུ་ཐོབ་པའོ། །

[Block 1811]
ཇི་སྐད་དུ།

[Block 1812]
ལེའུ་ལྔ་པ་ལས།

[Block 1813 [VERSE]]
རིགས་ངན་སྨྱིག་མ༌[^1263]མཁན་ལ་སོགས། །
གསོད་དོན་དོན་གཉེར་སེམས་པ༌[^1264]རྣམས། །
ཐེག་ཆེན་བླ་ན་མེད་པ་ཡི། །
ཐེག་མཆོག་འདི་ལ་འགྲུབ་པར་འགྱུར། །

[Block 1814]
ཞེས་སྤྱིར་བཏང་བའོ། །

[Block 1815]
གཞན་ཡང་།

[Block 1816 [VERSE]]
སློབ་དཔོན་ལ་ནི་སྨོད་པ་དག །
བསྒྲུབས་ཀྱང་འགྲུབ་པར་ཡང༌[^1265]མི་འགྱུར། །

[Block 1817]
ཞེས་དམིགས་ཀྱིས་བསལ་བའོ། །

[Block 1818 [VERSE]]
ལེའུ་བཅོ་བརྒྱད་པ་ལས་ཀྱང་། །
ཇི་ལྟར་སྔོན་བྱུང་དེ་བཞིན་ཀུན། །
འདི་ནི་གསང་བ་ཡང་དག་སྟེར། །

[Block 1819]
ཞེས་གཞན་གྱི་ཆོས་ཐོབ་པོ། །ཡང་ན་འདམ་ཁ་ཡང་རྒྱུད་ཀྱི་ཡན་ལག་ཡིན་ཏེ། །

[Block 1820 [VERSE]]
སྐུ་གསུང་ཐུགས་ཀྱི་རྡོ་རྗེའམ། །
རང་སྔགས་དོན་གྱི་ཡོན་ཏན་ནམ། །
ཡང་ན་གཙུག་ཏོར་དམ་ཚིག་གིས། །
བཀའ་ཡི་འཁོར་ལོ་སྦྱར་བར་བྱ། །

[Block 1821]
ཞེས་འདམ་ཁའོ། །

[Block 1822]
བསྡུ་བ་ཡང་རྒྱུད་ཀྱི་ཡན་ལག་ཡིན་ཏེ། རྡོ་རྗེ་ཅན་གྱི་གཟུགས་སོགས་ཀྱིས།

[Block 1823 [VERSE]]
གཙུག་ཏོར་མཉེས་པར་བྱེད་པར་བཤད། །
ཁྲོ་བོ་རྣམས་ལའང་དེ་མཆོག་སྟེ། །
སངས་རྒྱས་རྡོ་རྗེ་རབ་བསྒོམ་པའོ། །

[Block 1824]
ཞེས་ལེའུ་བཅོ་ལྔ་པ་ལས་འབྱུང་ངོ་། །ངེས་པ་ཡང་རྒྱུད་ཀྱི་ཡན་ལག་ཡིན་ཏེ། །ལེའུ་དེ་ཉིད་ལས་ཀྱང་། །

[Block 1825 [VERSE]]
གནོད་སྦྱིན་མ་ཡི༌[^1266]སྔགས་རྒྱུད་ལ། །
གཤིན་རྗེ་གཤེད་ནི་ཉིད་དུ་བསྒོམ། །
--- END BLOCKS ---
