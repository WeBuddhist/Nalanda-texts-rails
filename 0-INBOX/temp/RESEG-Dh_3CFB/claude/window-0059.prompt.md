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
[Block 2066]
རྟག་པའི་གཏན་ཚིགས་གཞན་དག་ཀྱང་སྐྱོན་ཅན་དུ་བརྗོད་པར་བྱའོ། །

[Block 2067 [VERSE]]
བློ་ནི་སྐྱེས་བུའི༌[^1492]རྟེན་ཅན་མིན། །
ཁས་བླངས་མངོན་སུམ་གྲགས་པ་དང་། །
རྗེས་སུ་དཔག་པས་ཅིག་ཅར་གནོད། །

[Block 2068]
གལ་ཏེ་གསལ་བ་བློ་ཡིན་ན་ནི༌[^1493]དེའི་གོ་རིམས་ངག་ཡིན་ལ། དེ་སྐྱེས་བུས་མ་བྱས་པ་ཉིད་དུ་སྒྲུབ་པར་བྱེད་ན་བློ་རྣམས་ནི་སྐྱེས་བུའི་ཡོན་ཏན་ཉིད་དུ་ཁས་བླངས་པས་འདིའི་གྲུབ་པའི་མཐའ་ལ་གནོད་པར་འགྱུར་རོ། །

[Block 2069]
བློ་འདིའི༌[^1494]ནི་སྐྱེས་བུར་འགྲང་བ༌[^1495]ཅན་དང་། སྐྱེས་བུའི་ཡོན་ཏན་ཡིད་ལ་བྱེད་པ་ལ་སོགས་པ་དག་ལས་འགྱུར་རོ། །ཞེས་བྱ་བ་གང་ཡིན་པ་དེ་ཡང་མངོན་སུམ་ཡིན་ནོ། །

[Block 2070]
ཡོད་པ་དང་མེད་པའི་ཁྱད་པར་ལས་འབྲས་བུ་ཞེས་བྱ་བ་གཞན་མེད་དེ། ཡོད་པ་དེ་ཡང་མངོན་སུམ་ཡིན་ཞིང་མི་དམིགས་པའི་མཚན་ཉིད་ཅན་གྱི་མེད་པ་ཡང་མངོན་སུམ་གྱི་སྟོབས་ཀྱིས་གྲུབ་པ་ཡིན་ནོ། །ཞེས་འཆད་པར༌[^1496]འགྱུར་རོ། །

[Block 2071]
དེ་ཉིད་ཀྱི་ཕྱིར་བློ་རྣམས་ནི་སྐྱེས་བུའི་འབྲས་བུ་ཉིད་དུ་རྗེས་སུ་དཔག་པར་བྱ་སྟེ། འདི་ནི་རྗེས་སུ་འགྲོ་བ་དང་ལྡོག་པའི་རྟགས་ཅན་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2072]
གཞན་ཡང་།

[Block 2073 [VERSE]]
ཡི་གེ་རྣམས་ལས༌[^1497]ཐ་དད་པའི། །
གོ་རིམས་ཀྱང་གསལ་དཔྱད་ཟིན་ཏོ། །

[Block 2074 [VERSE]]
དེ་རྟོག༌[^1498]སྒྲོ་བཏགས་ཡིན་གྱུར༌[^1499]ན། །
ཇི་ལྟར་སྐྱེས་མིན་རྟེན་ཅན་ཡིན། །

[Block 2075]
ཡི་གེ་ལས་ཐ་དད་པ་ཅན་གྱི་གོ་རིམས་ནི་གསལ་བ༌[^1500]རྣམ་པར་དཔྱད་པའི་གོ་རིམས་ཀྱིས་ལན་བཏབ་ཟིན་ཏོ། །

[Block 2076]
དེ་ཡང་ཡི་གེའི་རང་བཞིན་ཅན་མ་ཡིན་ནོ། །

[Block 2077]
དངོས་པོའི་རང་བཞིན་ནི་རྣམ་པར་རྟོག་པ་དེ་ལས་མ་འདས་པའི་ཕྱིར་རོ། །

[Block 2078]
དེ་བས་ན་དེའི་ངོ་བོ་ཅན་མ་ཡིན་པ་དག་ལ་དེའི་ངོ་བོར་སྒྲོ་བཏགས་པར་སྣང་བ་ཅན་གྱི་བློའི་གོ་རིམས་འདི་ཞེས་འཁྲུལ་བར་འགྱུར་ན། གང་ཡང༌[^1501]ཇི་ལྟར་ན་སྐྱེས་བུས་མ་བྱས་པ་ཡིན་ཏེ། བློའི་སྒྲུབ་པར་སོ་སོར་འཇོག་པའི་ཕྱིར་རོ། །

[Block 2079]
གཞན་ཡང་གཏན་དུ་བའི་རང་བཞིན་འགའ་ཞིག་ཀྱང་མེད་པའི་ཕྱིར། སྒྲ་ཡོད་པ་ལ༌[^1502]གཏན་དུ་བ་མ་ཡིན་པར་འགྱུར་རོ། །

[Block 2080]
དེ་ཡང་རྒྱུ་མེད་པ་ཅན་ནམ་གཞན་གྱི་རྒྱུ་ཅན་ཡིན་པར་འགྱུར་གྲང༌[^1503]ན། བརྟག་པར༌[^1504]འགྱུར་བ་དང་སྐྱེས་བུའི་བྱེད་པ་ལས་མ་ཡིན་ནོ། །

[Block 2081]
དེ་བས་ན་སྐྱེས་བུས་བྱས་པ་ཡིན་ནོ། །

[Block 2082]
སྒྲའམ་དངོས་པོ་གཏན་དུ་བ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་ཇི་ལྟར་རྟོགས་པར་འགྱུར་ཞེ་ན།

[Block 2083 [VERSE]]
འཇིག་པ་ཡོད་ཙམ་འབྲེལ་པ་ཅན། །
ཉིད་ཕྱིར་སྒྲ་ནི་མི་རྟག་ཉིད། །

[Block 2084]
དངོས་པོ་རྣམས་ཀྱི་འཇིག་པ་ནི་འགའ་ཞིག་ལས་ཀྱང་འགྱུར་བ་མ་ཡིན་ནོ། །

[Block 2085]
དེ་བས་ན་དངོས་པོའི་རང་བཞིན་གྱིས་འགྱུར་ཏེ། དངོས་པོ་ཉིད་ནི་རང་གི་རྒྱུ་ལས་དེའི་ཆོས་ཅན་དུ་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 2086]
དངོས་པོའི་ཁྱད་པར་གྱི་རང་བཞིན་ཡང་མ་ཡིན་ཏེ། དེ་ནི་འགོག་པར་འགྱུར་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2087]
དེ་བས་ནི༌[^1505]དངོས་པོ་ཙམ་གྱི་རང་བཞིན་གྱིས་འགྱུར་རོ། །

[Block 2088]
དེ་བས་ན་སྒྲའམ་གཞན༌[^1506]ཡོད་པ་ཉིད་བསྟེན་པའི༌[^1507]དངོས་པོ་ཐམས་ཅད་ནི་གཏན་དུ་བ་མ་ཡིན་ནོ་ཞེས་བྱ་བར་གྲུབ་པོ། །གྲུབ་པ་མ་ཡིན་ཏེ། འཇིག་པ་ཉིད་ཀྱི་གཞན་ལས་སྐྱེ་བ་མེད་པ་མ་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 2089]
དེ་ལྟར་ན་མེས་ཤིང་དང་དབྱུག་པས་བུམ་པ་ཞེས་བྱ་བ་འཇིག་པའི་རྒྱུ་དག་དངོས་པོ་རྣམས་ལ་སྣང་ཞིང་། རྒྱུ་དང་དེ་དང་ལྡན་པའི་མཚན་ཉིད་ནི་རྗེས་སུ་འགྲོ་བ་དང་ལྡོག་པའི་རྗེས་སུ་བྱེད་པ་ཡིན་པར་སྨྲའོ། །

[Block 2090]
མ་ཡིན་ཏེ། སྔ་མ་རང་གི་ངང་གིས་འགོག་པ་ན། །ཁྱད་པར་ཅན་གྱི་རྐྱེན་ལ་བརྟེན་ནས་མི་འདྲ་བ་གཞན་སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 2091]
མེ༌[^1508]ཤིང་འཇིག་པའི་རྒྱུ་ཡིན་པ་ནི་བླ་སྟེ། མེ་ལས་སྐྱེ་བ་ཅན་གྱི་འཇིག་པ་དེ་ཅི་ཤིང༌[^1509]ཉིད་དམ་འོན་ཏེ་དོན༌[^1510]གཞན་དུ་གྱུར་པ་ཡིན་ན།

[Block 2092 [VERSE]]
མེ་ལས༌[^1511]དོན་གཞན་གྱུར་པ་དག །
སྐྱེ་ན་འཇིག་པ་མེད་པའི་ཕྱིར། །
ཤིང་ནི་མཐོང་བ་ཉིད་དུ་འགྱུར། །

[Block 2093]
ཅིའི་ཕྱིར་དོན་གཞན་དུ་གྱུར་པ་ལས་དོན་གཞན་དུ་གྱུར་པ་སྐྱེ་བ་ཡིན་ན། ཤིང་འཇིག་པའམ་མི་སྣང་བ་ཞེས་བྱ་བ་དེ་ལྟར་ན་ཤིན་ཏུ་ཐལ་བར་འགྱུར་རོ། །

[Block 2094]
གལ་ཏེ་དེ་ཡི་འཇིག་ཡིན་ཞེས། །གལ་ཏེ་དོན་དེ་ཉིད་མེ་ལས་སྐྱེ་བ་ཅན་གྱི་ཤིང་མེད་པ་ཡིན་པ་དེ་བས་ན་འདི་འཇིག་པ་ཉིད་ཀྱི་ཕྱིར་མི་སྣང་བ་ཡིན་ནོ་ཞེ་ན། དེའི་མེད་པ་ཞེས་བྱ་བ་འདི་ཡིན་པ་ནི་བླ་སྟེ། དེ་ལྟར་ན་ཡང་། ཇི་ལྟར་གཞན་ནི་གཞན་འཇིག་ཡིན། དོན་འགའ་ཞིག་ལ་མིང་དུ་བྱས་པ་ཙམ་གྱིས་ཤིང་མི་སྣང་ངོ་ཞེས་བྱ་བ་རིགས་པ་མ་ཡིན་ནོ། །

[Block 2095]
གཞན་ནི་གཞན་གྱི་འཇིག་པ་ཡང་མ་ཡིན་ཏེ། ཐལ་ཆེས་པའི་ཕྱིར་དང་། དོན་གཞན་དུ་གྱུར་པ་ཉིད་ཀྱིས་དངོས་པོར་གྱུར་པ་དེ་ནི་དེ་ལས་གཞན་པ་དག་ལ༌[^1512]ཡང་ཁྱད་པར་མེད་པའི་ཕྱིར་རོ། །

[Block 2096]
གལ་ཏེ་ཤིང་ལ་མེས་བྱས་པའི་རང་བཞིན་གྱི་འཇིག་པ་ཡིན་གྱི་ཐམས་ཅད་ལ་ནི་མ་ཡིན་ནོ་ཞེ་ན། ཤིང་ལ་ཞེས་བྱ་བའི་འབྲེལ་པ་གང་ཡིན། གལ་ཏེ་རྟེན་དང་བརྟེན་པའི་ངོ་བོ་ཡིན་ནོ་ཞེ་ན། མ་ཡིན་ཏེ། དེ་དག་ནི་དགག་པར་བྱ་བ་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2097]
གལ་ཏེ་བསྐྱེད་པར་བྱ་བ་དང་སྐྱེད་པར་བྱེད་པའི་དངོས་པོ་ཡིན་ནོ་ཞེ་ན། མེ་ལ་ཞེས་བྱ་བས་ཅི་ཞིག་བྱ། ཤིང་ཉིད་ལས་བྱུང་བའི་ཕྱིར་རོ། །

[Block 2098]
གལ་ཏེ་དེ་མེ༌[^1513]ལས་ལྟོས་པ་ཅན་ལས་སྐྱེ་བའི་ཕྱིར་སྐྱོན་མེད་དོ་ཞེ་ན། ཕུལ་དུ་བྱུང་བ་ཐོབ་པ་མེད་པ་ཅན་ལ་ལྟོས་སུ་ཅི་ཡོད། ཐོབ་ན་ཡང་ཤིང་གཞན་སྐྱེ་བར་འགྱུར་རོ། །

[Block 2099]
འཕོ་བའི་རྒྱུ་མེད་པ་ཅན་སྔ་མ་ཡང་དེ་ཁོ་ན་བཞིན་དུ་མཐོང་བར་འགྱུར་རོ། །

[Block 2100]
གལ་ཏེ་མེ་དེ་ཉིད་ལས་སྔ་མ་འཇིག་པ་ཡིན་ནོ་ཞེ་ན། སྔ་མ་དང་འདིའི་འབྲེལ་པ་གང་ཡིན། དེ་ལྟར་ན་ཐལ་བར་འགྱུར་བ་དེ་ཉིད་དང་ཐུག་པ་མེད་པར་འགྱུར་རོ། །

[Block 2101]
དེ་བས་ན་གདོན་མི་ཟ་བར་འཇིག་པ་དང་འབྲེལ་པར་རུང་བ་ཕྱིས་ཕུལ་དུ་བྱུང་བ་ཉེ་བར་བྱེད་པས་མེས་སྔ་ན་མེད་པ་བསྐྱེད་པའི་ཕྱིར། སྔ་མའི་གནས་སྐབས་ཅན་དེ་སྣང་བར་འགྱུར་རོ། །

[Block 2102]
ཤིང་འཇིག་པ་ཞེས་བྱ་བ་ཡང་ཤིང་མེད་པ་ཉིད་བརྗོད་པ་ཡིན་ལ། མེད་པ་ནི་འབྲས་བུ་ཡང་མ་ཡིན་ནོ། །

[Block 2103]
དེ་བྱེད་པ་ཡང་བྱེད་པ་པོ་ཉིད་མ་ཡིན་པའི་ཕྱིར་ལྟོས་པར་བྱ་བ་མ་ཡིན་ནོ། །ཞེས་བྱ་བ་ཡང་བཤད་ཟིན་ཏོ། །

[Block 2104]
རང་གི་ངོ་བོ་མེད་པ་དེ་ལས་ཐ་དད་པ་ཡིན་ན། དེ་ལས་བཟློག་པའི་དངོས་པོའི་ངོ་བོ་ཉིད་བསྒྲུབ་པར་འགྱུར་བའི་ཕྱིར་ཇི་ལྟར་ཞིག་པ་ཞེས་བྱ། དེ་བས་ན་གཞན་ནི་གཞན་གྱི་འཇིག་པ་མ་ཡིན་ནོ། །

[Block 2105]
བླ་སྟེ་ཅི་ཕྱིར་ཤིང་མི་སྣང་། །དོན་གཞན་འབྱུང་བ་དང་ཤིང་མཐོང་བ་འདི་ལ་འགལ་བ་ཅི་ཡོད།། །།
--- END BLOCKS ---
