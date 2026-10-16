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
[Block 2136]
ཇི་ལྟར་ན་མེད་པའི་འཇིག་པས་དངོས་པོ་འཇིག་པར་འགྱུར། །དེ་བས་ན་དངོས་པོ་འཇིག་པ་ཅན་དུ་མི་འགྱུར་རོ། ། ཞེས་བྱ་བ་ཡང་ཐལ་བར་འགྱུར་བ་ཉིད་མ་ཡིན་ཏེ། འཇིག་པ་ལས་དངོས་པོ་ཞིག་པ་ཁས་མི་ལེན་པའི་ཕྱིར་རོ། །

[Block 2137]
འཇིག་པ་ཞེས་བྱ་བ་ཅུང་ཞིག་ཀྱང་མེད་དོ་ཞེས་སྨྲ་བ་གང་ཡིན་པ་དེ་ཇི་ལྟར་དེ་ལས་དངོས་པོ་ཞིག་པར་འདོད། ད་ནི་འཇིག་པ་མེད་པ་ཡིན་ན་ཇི་ལྟར་དངོས་པོ་འཇིག་པ་ཞེས་བྱ། ད་ལྟར་བྱུང་བའི་གནས་སྐབས་འཇིག་པ་མེད་པ་ཅན་འཇིག་པར་མི་འགྱུར། [^1531]གང་ཞིག་གང་གིས་དེ་དང་ལྡན་པ་མ་ཡིན་པ༌[^1532]དེ་དེས་དེ་ལྟར་ཐ་སྙད་འདོགས་པ༌[^1533]འམ། ཤེས་པ་མ་ཡིན་ཏེ། དཔེར་ན་རྟ་ལ་རྭས་ཐ་སྙད་མི་འདོགས་པ་བཞིན་ནོ། །

[Block 2138]
འཇིག་པ་མེད་པ་ཉིད་མ་ཡིན་མོད་ཀྱི་དངོས་པོའི་འགྱུར་བ་གང་ཡིན་པ་དེ་ནི་ཡོད་པ་མ་ཡིན་ཏེ། དངོས་པོའི་སྐད་ཅིག་མར་གནས་པའི་ཆོས་ཅན་འཇིག་པ་ཡིན་ནོ། །

[Block 2139]
འདིའི་རང་བཞིན་དེ་དུས་ཕྱིས་འདི་འཇིག་པར་འགྱུར་བ་ཞེས་ངེས་པར་བྱས་ནས་ཇི་ལྟར་ཤེས་པ་བཞིན་དུ་ཐ་སྙད་འདོགས་པར་བྱེད་དོ། །ཞེས་བྱ་བ་ནི་བཤད་ཟིན་ཏོ། །

[Block 2140]
དངོས་པོ་ཅུང་ཞིག་ཀྱང་འགའ་ཞིག་གི་ཚེ་ཡང་འགྱུར་བ་མ་ཡིན་ནོ། །

[Block 2141]
འོན་ཀྱང་དེ་ཉིད་རང་གི་རྒྱུ་དག་ལས་དེ་ལྟ་བུར་འཇིག་པ་དག་ཏུ་འགྱུར་རོ། །

[Block 2142]
དེ་བས་ཡོད་པ་ཉིད་འགའ་ཞིག་གིས་ཀྱང་དེ་ཞིག་པ་མ་ཡིན་ནོ། །

[Block 2143]
འོ་ན་ཅི་ཡིན་ཞེ་ན། དེའི་རང་བཞིན་ཉིད་ཡིན་པ་ཞེས་བྱའོ། །

[Block 2144]
འོ་ན་ད་ཇི་ལྟར་ན་འཇིག་པ་རྒྱུ་མེད་པ་ཅན་དུ་འགྱུར་རོ་ཞེས་བརྗོད་ཅེ་ན།

[Block 2145 [VERSE]]
དངོས་འཇིག་གཞན་ལ་ལྟོས་མེད་ཕྱིར། །
དེ་ཤེས་ཕྱིར་ན་སེམས་ཀྱིས་ནི། །
དེ་ཡི་ཐ་སྙད༌[^1534]སྒྲོ་བཏགས་ནས། །
གནས་སྐབས་དེ་རྒྱུ་མེད་ཅན་བཤད། །

[Block 2146]
དངོས་པོ་སྐྱེས་པ་གཞན་ལས་འཇིག་པ་ཐོབ་པ་མ་ཡིན་ནོ།[^1535] །དེ་ལྟ་བུར་གྱུར་པ་ཉིད་རང་ཉིད་སྐྱེས་པའི་ཕྱིར་རོ། །

[Block 2147]
དེ་ལྟར་ན་གཞན་ལ་ལྟོས་པའི་ཆོས་གཞན་དགག་པའི་ཕྱིར་དང་། དེའི་རང་བཞིན་ཤེས་པའི་ཕྱིར། །སེམས་ཀྱིས་ཆོས་ཅན་ལས་ཆོས་དོན་གཞན་དུ་གྱུར་པ་བཞིན་དུ་རྣམ་པར་ཕྱེ་ནས། དེ་ཙམ་ཤེས་པར་འདོད་པའི་ཚེ་རང་བཞིན་ཉིད་ལ་དེ་སྐད་བརྗོད་དོ། །

[Block 2148]
འགའ་ཞིག་ཏུ་དེ་ལྟར་མཐོང་བ་ལས་སྒྲ་ཙམ་ཉིད་ཀྱིས་འཁྲུལ་པའི་བློ་དམན་པ་དག་གིས་དེ་དང་དེ་འཇིག་པའི་ཡོན་ཏན་དང་དེའི་ཡོད་པ་དང་རྒྱུ་དང་བཅས་པ་ཅན་ཡིན༌[^1536]ནམ། རྒྱུ་མེད་པ་ཅན་དུ་སྒྲོ་བཏགས་ནས་དེ་ཁོ་ན་ཉིད་ལ་གནས་པ་མེད་པ་ཅན་གྱིས་དངོས་པོ་དཔྱོད་པས་བདག་ཉིད་འཁྲུག་པར་བྱེད་དོ། །

[Block 2149]
གལ་ཏེ་མེད་པར་རང་ཉིད་ཀྱིས། །ཡོད་ན་འང་རྣམ་རྟོག་འདི་མཚུངས་སོ། །

[Block 2150]
གཞན་ལས་འབྱུང་བ་ཉིད་མ་ཡིན་དུ་ཟིན་ཀྱང་། དངོས་པོའི་འཇིག་པ་རང་གི་ངོ་བོ་ཉིད་ཀྱིས་ཡོད་པ་ཡིན་ན། དེ་ཉིད་དང་གཞན་ཉིད་དུ་རྣམ་པར་རྟོག་པ༌[^1537]འདི་མཚུངས་པ་མ་ཡིན་ནམ། དེའི་ཚེ་ཡང་དོན་གཞན་འབྱུང་བ་ན་དངོས་པོ་ཅིའི་ཕྱིར་མི་སྣང་། དེ་ན༌[^1538]གཞན་ཉིད་མ་ཡིན་ན་ཡང་དེ་ཉིད་དེ་ཡིན་པར་འགྱུར་རོ། །

[Block 2151]
དེ་བས་ན་འདིའི་སྐྱེ་བ་ཅུང་ཟད་ཀྱང་མེད་པ་དེ་ལྟར་ན་ཇི་ལྟར༌[^1539]འཇིག་པ་ཞེས་བྱ་བ་ཡིན།

[Block 2152 [VERSE]]
འདི་དེའི་ཅུང་ཟད་འགྱུར་བ་མེད། །
འོན་ཀྱང་འགྱུར་བ་མེད་པ་ཉིད། །

[Block 2153]
ཅེས་བཤད་པ་མ་ཡིན་ནམ། འདི་ནི་དངོས་པོའི་འཇིག་པའམ། གཞན་འགའ་ཞིག་ཏུ་འགྱུར་རོ། །ཞེས་ནི་མི་སྨྲའོ། །

[Block 2154]
འོ་ན་ཅི་ཞེ་ན། དེ་ཉིད་དངོས་པོར་འགྱུར་བ་མ་ཡིན་ཏེ། གལ་ཏེ་འགའ་ཞིག་དངོས་པོར་བརྗོད་ན་འདིས་དངོས་པོ་ལྡོག་པར་མི་འགྱུར་རོ། །

[Block 2155]
དེ་ལྟར་ན་དངོས་པོ་ལྡོག་པའི་སྐབས་སུ་སྐབས་མ་ཡིན་པ་ཉིད་བཤད་པར་འགྱུར་རོ། །

[Block 2156]
འགའ་ཞིག་འབྱུང་བས་དངོས་པོ་འཇིག་པ་ཞེས་བྱ་བ་མ་ཡིན་ལ། གང་གི་ཚེ་བདག་ཉིད་ཡོད་པ་མེད་པ་དེའི་ཚེ་འཇིག་པ་ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 2157]
ཡོད་པ་མེད་པ་ཞེས་བྱ་བ་དེ་ནི་མེད་པར་དགག་པ་ཡིན་གྱི་མ་ཡིན་པར་དགག་པ་ནི༌[^1540]མ་ཡིན་ནོ། །

[Block 2158]
འདི་ལ་ཡང་འགའ་ཞིག་བསྒྲུབས༌[^1541]ན་མེད་པ་དང་མ་ཡིན་པར་དགག་པ་དག་གི་ངོ་བོ་ཐ་དད་པ་མེད་པར་འགྱུར་ཏེ། གཉི་ག་ལ་ཡང་སྒྲུབ་པ་གཙོ་བོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2159]
དེ་ལྟར་ན་འགའ་ཞིག་ཀྱང་དགག་པ་མེད་པའི་ཕྱིར། འགའ་ཞིག་ཏུ་ཡང་མ་ཡིན་པར་དགག་པར༌[^1542]ཡང་མི་འགྱུར་རོ། །

[Block 2160]
གལ་ཏེ་འགའ་ཞིག་ལས་ལྡོག་པར་འགྱུར་བ་དེའི་ཚེ། དེ་ལས་བཟློག་པ་དེ་མ་ཡིན་པར་དགག་པ་ལ་རེག་པར་འགྱུར་ན༌[^1543]ཡང་ཡོད་པ་མ༌[^1544]ཡིན་ནོ། །

[Block 2161]
ཐམས་ཅད་དུ་ལོག་པར་འགྱུར་རོ་ཞེས་བཤད་པ་ན་དངོས་པོ་འགའ་ཞིག་རྟོགས་པའི་ཕྱིར་རོ། །

[Block 2162]
དེ་ལྟར་འདི་ནི་དོན་གཞན་ཡོད་པ་ཉིད་བསྟན་པར་འགྱུར་རོ། །

[Block 2163]
དེ་དག༌[^1545]ནི་ཕན་ཚུན་ཐ་དད་པ་མེད་དོ། །

[Block 2164]
ཐ་དད་པ་མེད་ན་ཡང་མ་ཡིན་ནོ། །

[Block 2165]
དེ་ལྟར་ལོག་པ་མེད་པའི་ཕྱིར་རྗེས་སུ་འགྲོ་བར་ཡང་མི་འགྱུར་ཏེ། དེ་ནི་གཅིག་གི་རང་བཞིན་ལ་གནས་པའི་མཚན་ཉིད་ཅན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2166]
གནས་པ་དེ་ཡང་དེ་ལས་གཞན་ལྡོག་པ་ན་ཡོད་པར་འགྱུར་རོ། །

[Block 2167]
དེ་ཡང་ཡོད་པ་མ་ཡིན་པའི་ཕྱིར་འགྲོ་བའི་འཇུག་པ་དང་ལྡོག་པ་མེད་པ་ཅན་དུ་འགྱུར་རོ། །

[Block 2168]
དེ་བས་ན་གང་འཇིག་པར་འགྱུར་རོ་ཞེས་བརྗོད་པས་དེ་བདག་ཉིད་ཡོད་པ་མེད་དོ་ཞེས་བཤད་པར་འགྱུར་རོ། །

[Block 2169]
སྒྲ་མཚུངས་པའི་ཕྱིར་ཡུལ་གཞན་ལ་མཐོང་བའི་བྱ་བ་ཐམས་ཅད་ལ་སྦྱར་བར་རིགས་པ་མ་ཡིན་ཏེ། བོང་བུ་ཞེས་མིང་དུ་བྱས༌[^1546]ལས་མི་ལ་བོང་བུའི་ཆོས་ཀྱང་སྦྱར་བར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 2170]
དེ་ལྟར་ན་ནག་པའི་བུ་ཞེས་བྱ་བ་འདི་ལ་མཐོང་བའི་བྱ་བ་འཇིག་པ་ལའང་སྦྱར་བར་བྱ་བ་མ་ཡིན་ཏེ་འགལ་བའི་ཕྱིར་རོ། །

[Block 2171]
དེ་སྐད་དུ་བརྗོད་པའི་དགོངས་པ་ཡང་བསྟན་ཟིན་ཏོ། །

[Block 2172]
དེའི་ཕྱིར།

[Block 2173 [VERSE]]
ཡོད་ལ་རྣམ་རྟོག་དེར་འགྱུར་ཏེ། །
བྱ་བ་དངོས་དང་འབྲེལ་ཕྱིར་རོ། །

[Block 2174]
ཡོད་པ་ནི་གདོན་མི་ཟ་བར་སྐྱེ་བ༌[^1547]དང་ལྡན་པ་ལ་རག་ལས་པ་ཡིན་ནོ། །

[Block 2175]
དེ་ཡང་རང་བཞིན་ཉིད་ཡིན་ཏེ། རང་བཞིན་མེད་པ་ནི་བྱ་བ་འགའ་ཞིག་དང་ཡང་འབྲེལ་པ་མེད་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
