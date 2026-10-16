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
[Block 2206]
དེ་ལྟར་ན།

[Block 2207 [VERSE]]
གལ་ཏེ་བྱ་བ་ཅུང་ཟད་ཅིག །
ཡོད་ན་གཞན་ལ་ལྟོས་འགྱུར་ན། །
དངོས་གང་ཅུང་ཞིག་མི་བྱེད་ལ། །
ཅི་ཕྱིར༌[^1564]འགའ་ཞིག་གིས་ལྟོས་འགྱུར། །

[Block 2208]
བྱ་བ་ཡོད་ན་བྱེད་པར་འགྱུར་ཏེ། དངོས་པོ་འཇིག་པའི་ངང་ཚུལ་ཅན་ལ་བྱ་བ་ཅུང་ཟད་ཀྱང་མེད་དོ་ཞེས་བཤད་ཟིན་ཏོ། །

[Block 2209]
དེ་བས་ན་འཇིག་པའི་རྒྱུ་ཞེས་བྱ་བ་དེ་ནི་དངོས་པོ་ལ་ཅུང་ཞིག་ཀྱང་མི་བྱེད་པ་དེ་ལྟར་ན་ཅུང་ཞིག་མི་བྱེད་པ་ལ་ལྟོས་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 2210]
དེ་ནི་དངོས་པོ་ཕུལ་དུ་བྱུང་བ་སྐྱེ་བ་མེད་པ་ཅན་དེའི་གནས་སྐབས་ཅན༌[^1565]ཉིད་ཇི་ལྟར་ན་འཇིག་པ་ཞེས་བྱ། ཕུལ་དུ་བྱུང་བ་སྐྱེ་བ་ཡིན་ན་ཡང་དེ་ཉིད་དེའི་ཕུལ་དུ་བྱུང་བ་སྐྱེ་བ་ཞེས་བྱ་བ་མ་ཡིན་ནམ། དེ་ཇི་ལྟར་ན་འཇིག་པ་ཞེས་བྱ། དེས་ན་དེའི་གནས་སྐབས་ཅན་འདི་འཇིག་པ་ཞེས་བྱ་བ་མ་ཡིན་ནོ། །

[Block 2211]
གང་གིས་བདག་ཉིད་མེད་པར་འགྱུར་བ་དེས་འཇིག་པ་ཡིན་གྱི། དོན་གཞན་སྐྱེ་བ་ལས་ནི་མ་ཡིན་ནོ་ཞེས་བཤད་ཟིན་ཏོ། །

[Block 2212]
ཕུལ་དུ་བྱུང་བ་བསྐྱེད་པས་བདག་ཉིད་འཇིག་པ་ཞེས་བྱ་བ་ནི་མ་ཡིན་ནོ། །

[Block 2213]
མེད་པ་ནི་ཕུལ་དུ་བྱུང་བ་ཉེ་བར་བརྗོད་པ་ཐམས་ཅད་ལོག་པའི་སྒོ་ནས་དངོས་པོའི་ཆོས་ཐམས་ཅད་ཀྱིས་དབེན་པའི་མཚན་ཉིད་ཅན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2214]
དངོས་པོ་ནི་སྐྱེ་བ་དང་འབྲེལ་པའི་མཚན་ཉིད་ཅན་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2215]
དེ་བས་ན་མེད་པ་ལ་ཡོད་པ་གཞན་འགའ་ཞིག་དགོད་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 2216]
དེ་ནི་རྒྱུ་མེད་ཅན་ཉིད༌[^1566]ཡང་། །མ༌[^1567]བྱུང༌[^1568]ཉིད་ནས་འཇིག་ཡོད་ཕྱིར། །

[Block 2217]
ཡོད་པ་ཉིད་དང་འཇིག་ཉིད་སྐྱོན།[^1569] །ཐལ་བར་འགྱུར་བ་བསལ་བ་ཡིན། །གང་ཡང་འཇིག་པ་རྒྱུ་མེད་པ་ཅན་ཡིན་ན་ཡང་མ་བྱུང་བ་ཉིད་ན་འདི་ཡོད་པའི་ཕྱིར་ཡོད་པ༌[^1570]ཉིད་དང་མི་རྟག་པ་ཉིད་བཟློག་པར་དཀའ་ཞིང་མ་བྱུང་བ་ཉིད་ན་འགྱུར་བ་དང་། རྒྱུ་མེད་པར་བྱུང་བ༌[^1571]ཡང་འགལ་བ་ཡིན་ནོ་སྙམ་དུ་སེམས་ན། དེ་ཡང་འདི་ཉིད་ཀྱིས་བསལ་བ་ཡིན་ཏེ། དངོས་པོ་འགའ་ཞིག་ཁས་མ༌[^1572]བླངས་པའི་ཕྱིར་རོ། །

[Block 2218 [VERSE]]
ཇི་ལྟར་སྐྱེ་བ་ཅན་འགའ་ཞིག །
ཐོགས་པ་ཉིད་འདོད་དེ་བཞིན་དུ། །
གལ་ཏེ་དངོས་རྣམས་འཇིག་རང་བཞིན། །
ཡིན་གྱི་སྐྱེ་ལྡན་མིན་མ་ཡིན། །

[Block 2219]
ཅི་སྟེ་དངོས་པོ་རྣམས་ཀྱི་སྐད་ཅིག་མར་གནས་པའི་ཆོས་ཅན་གང་ཡིན་པ་དེ་ནི་དེའི་རང་བཞིན་དུ་འགྱུར་བ་བླ་སྟེ། དེ་ནི་སྐྱེ་བ་དང་ལྡན་པ་ཉིད་ཀྱིས་འགྱུར་བ་ཡིན་ནོ། །

[Block 2220]
རང་གི་ངོ་བོ་ཡིན་པའི་ཕྱིར། ཐམས་ཅད་ཐམས་ཅད་ཀྱི་རང་གི་ངོ་བོར་ནི་འགྱུར་བ་ནི༌[^1573]མ་ཡིན་ཏེ།

[Block 2221 [VERSE]]
ཐོགས་པར་བྱེད་པའི་བདག་ཉིད་བཞིན་ནོ། །
དེ་ནི་བདེན་ན་དེ་ལྟ་ནའང་། །
རྒྱུ་ཡི་རང་བཞིན༌[^1574]ངེས་པ་ལས། །
འབྲས་བུའི་རང་བཞིན་ངེས་ཡིན་གྱི། །

[Block 2222 [VERSE]]
ཐ་དད་བྱེད་རྣམས་མེད་ཉིད་ཕྱིར། །
མི་རྟག་ངོ་བོ་ཐ་དད་མེད། །

[Block 2223]
ཐོགས་པར་བྱེད་པའམ་གཞན་གློ་བུར་བའི་ངོ་བོ་ནི་སོ་སོ་ངེས་པ་དང་ལྡན་པ་མ་ཡིན་ནོ། །

[Block 2224]
རང་གི་རྒྱུའི་ནུས་པའི་གནས་པ་ཅི་འདྲ་བ་དེ་འདྲ་བའི་འབྲས་བུར་གྱུར་པའི་ཕྱིར། རྒྱུའི་རང་བཞིན་དེས་ན༌[^1575]ངེས་པ་ལས་འབྲས་བུའི་རང་བཞིན་ངེས་པ་ཡིན་གྱི། འདི་གློ་བུར་བ་ཉིད་ཡིན་པའི་ཕྱིར་ཡང་བཤད་ཟིན་ཏོ། །

[Block 2225]
ཐོགས་པར་བྱེད་པའི་བདག་ཉིད་ཅན་རྒྱུའི་ཚོགས་པའི་རང་བཞིན་ངེས་པ་བཞིན་དུ་འཇིག་པ་སྐྱེད་པར་བྱེད་པའི་རང་བཞིན་ཅན་དངོས་པོ༌[^1576]མཐོང་ན། གང་གིས༌[^1577]དེ་ལས་སྐྱེ་བ་དང་ལྡན་པ་དེ་ལྟར་འགྱུར་གྱི། གཞན་ནི་མ་ཡིན་ཏེ། རྣམ་པ་ཐམས་ཅད་པ་ལས་སྐྱེ་བ་ཅན་དག་གི་འཇིག་པ་མཐོང་བའི་ཕྱིར་རོ། །

[Block 2226]
ཚོགས་པ་ཐམས་ཅད་ལས་སྐྱེ་བ༌[^1578]དང་ལྡན་པ་དག་འཇིག་པར་འགྱུར་རོ་ཞེས་བྱ་བ་འདི་ཡང་དེ་དག་མ་ལུས་པ་མཐོང་བ་མེད་པའི་ཕྱིར། ངེས་པ་མེད་པ་ཉིད་མ་ཡིན་ནམ། ཚོགས་པ་ནུས་པ་སྣ་ཚོགས་པ༌[^1579]མཐོང་བར་འགྱུར་བ་དེ་ལས་འགའ་ཞིག་འགྱུར་ན་ཡང་། གང་གིས་འཇིག་པའི་ངང་ཚུལ་ཅན་མ་ཡིན་པའི་བདག་ཉིད་བསྐྱེད་པར་འགྱུར་ཞེ་ན། མ་ཡིན་ཏེ། ཤེས་བྱའི་སྐབས་ཡིན་པའི་ཕྱིར་རོ།[^1580] །འགའ་ཞིག་གི་ཚེ་འགའ་ཞིག་ཏུ་འགའ་ཞིག་གིས་ཤེས་པར་མི་འགྱུར་བ་གང་ཡིན་པ་དེ་དག་ནི་ཡོད་པ་ཉིད་དང་རྗེས་སུ་འབྲེལ་པ་ཅན་གྱི་འཇིག་པ་ཞེས་བརྗོད་དོ། །

[Block 2227]
དེ་དག་ཉིད་བྱས་པ་ཉིད་ཀྱིས་མི་རྟག་པ་ཉིད་དུ་བསྒྲུབ་པར༌[^1581]འགྱུར་རོ། །

[Block 2228]
གང་ཞིག་སྐྱེད་པར་བྱེད་པའི་རང་བཞིན་ཅན་དེ་དག་འཇིག་པ་མེད་པ་ཅན་ཡིན་པས་ན་ཡང་བསྐྱེད་པར་མི་འགྱུར་བའམ། གཞན་ལ་ལྟོས་པར་འགྱུར་བ་སྲིད་པ་ཡོད་པ་མ་ཡིན་ཏེ། དེའི་སྐྱེད་པར་བྱེད་པའི་རང་བཞིན་ནི་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 2229]
ལྟོས་པ་མེད་པ་ཅན་དེ་དག་འགའ་ཞིག་གི་ཚེ་ཡང་འགའ་ཞིག་གི་ཤེས་པ་འགའ་ཞིག༌[^1582]ཀྱང་ལྡོག་པ་མ་ཡིན་ནོ། །

[Block 2230]
དེ་ལྟ་བུར་གྱུར་པ་ཅུང་ཞིག་ཀྱང་ཡོད་པ་མ་ཡིན་ཏེ། ཐམས་ཅད་འགའ་ཞིག་གི་ཚེ་འགའ་ཞིག་གིས་ཤེས༌[^1583]པའི་ཕྱིར་རོ། །ཤེས་པ་ཙམ་གྱི་དོན་བྱེད་པའི་ནུས་པ་མེད་ན་ཡང་དངོས་པོ་ཉིད་དུ་མི་འགྱུར་རོ། །

[Block 2231]
དེ་ལྟར་ན་དེའི་མཚན་ཉིད་ཅན་དངོས་པོ་ཡིན་ནོ་ཞེས་འཆད་པར་འགྱུར་རོ། །

[Block 2232]
དེ་ཡང་འཇིག་པར་འཁྲུལ་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 2233]
དེ་ཡོད་པ་ཉིད་དང་འབྲེལ་པ་ཅན་ཡིན་ནོ། །

[Block 2234 [VERSE]]
དེ༌[^1584]ཕྱིར་དེ་རྣམས་འབྲེལ་པ་ཡང་། །
རྟག་པ་ཉིད་ནི་བསལ་བྱ་ཡིན། །

[Block 2235]
འཇིག་པ་ནི་ཇི་སྐད་དུ་བཤད་པའི་དངོས་པོ་ཙམ་དང་འབྲེལ་པ་ཡིན་པ་དེ་ཉིད་ཀྱི་ཕྱིར། སྒྲ་དང་འདྲ་བར་འབྲེལ་པ་རྟག་པ་ཉིད་ཀྱང་བསལ་བར་བྱ་བ་ཡིན་ནོ། །

[Block 2236]
རྒྱལ་དཔོག་པ་དག་གིས་སྒྲའི་ནུས་པ་རུང་བ་ཉིད་ཅེས་བྱ་བའི་དོན་རྟོགས་པའི་རྟེན་དུ་བརྗོད་པ་གང་ཡིན་པ་དེ་ནི་དོན་གཞན་ཉིད་དུ་འགྱུར་བ་མ་ཡིན་ནོ། །

[Block 2237]
དེ་ལྟར་ན་རུང་བ་ཉིད་ཅེས་བྱ་བ་དངོས་པོ་རྣམས་ཀྱི་ངོ་བོའི་ཕུལ་དུ་བྱུང་བ་ཉིད་ཡིན་ནོ་ཞེས་སྔར༌[^1585]བརྗོད་ཟིན་ཏོ། །

[Block 2238]
དོན་གཞན་ཡིན་པ་ཡང་བླ་སྟེ། དེ་ལྟར་ན་ཡང་འབྲེལ་པའི་སྔར་བཤད་སྐྱོན་རྣམས་ཀྱི། སྒྲ་ཡི་ནུས་པ་བསལ་བ་ཡིན། །འབྲེལ་པ་དོན་དུ་གྱུར་པ་ཡིན་པར་སྨྲ་བ་ལ་སྐྱོན་རྣམ་པ་དུ་མ་བཤད་ཟིན་པ་དེ་ཉིད་ཀྱིས་སྒྲའི་ནུས་པ་དེ་སུན་ཕྱུང་བ་ཉིད་ཀྱིས་ཕྱིར་ཡང་མི་བརྗོད་དོ། །

[Block 2239]
གཞན་ཡང་།

[Block 2240 [HEADING]]
### སྐྱེས་བུས་མ་བྱས་པ་ཇི་བཞིན་དོན་ཤེས་སྒྲུབ་བྱེད་མིན་པ། ^7-3-0

[Block 2241 [VERSE]]
སྐྱེས་བུས་མ་བྱས་ཤེས་བྱ་ཉིད། །
ཇི་བཞིན་དོན་ཤེས་སྒྲུབ་བྱེད་མིན། །
སྐྱེས་བུའི་ཉེས་པས་སྐྱོན་མེད་པའི། །
མེ་སོགས་རྣམ་པ་གཞན་དུའང་མཐོང་། །

[Block 2242]
རིག་བྱེད་པའི་སྒྲ་སྐྱེས་བུས་མ་བྱས་པ་ཡིན་པ་ཡང་བླ་སྟེ། དེ་ལྟར་ན་ཡང་དེ་དག་དོན་ཇི་ལྟ་བ་བཞིན་མ་ཡིན་པའི་ཤེས་པའི་རྒྱུ་ཉིད་ཡིན་པར་བསམ་པར་བྱ་བ་ཡིན་ནོ། །

[Block 2243]
སྐྱེས་བུའི་སྐྱོན་གྱིས་ཉེ་བར་བསྒྱུར་བ་ཉིད་དོན་དག་ལས་ཤེས་པ་འཁྲུལ་པ་མ་ཡིན་ཏེ། དེ་དང་བྲལ་བའི་སྒྲོན་མ་ལ་སོགས་པ་དག་གིས་ཀྱང་ཨུཏྤལ་ལ་སོགས་པ་དག་ལ་ལོག་པའི་རྣམ་པར་ཤེས་པ་བསྐྱེད་པའི་ཕྱིར་རོ། །

[Block 2244]
དེ་བས་ན་འདུས་བྱས་པ་ལ་ལྟོས་པ་མེད་པའི་སྒྲ་འདི་དག་ནི་ངོ་བོ་ཉིད་ཀྱིས་དོན་རྣམས་ལ་སློབ་པའི༌[^1586]རྒྱུར་འགྱུར་ཏེ། རང་བཞིན་གྱི་ཁྱད་པར་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2245]
ལོག་པར་བསལ་བ་ཅན་དག་ཀྱང་ངེས་པར་འགྱུར་ཏེ། མེ་ལ་སོགས་པ་བཞིན་ནོ། །
--- END BLOCKS ---
