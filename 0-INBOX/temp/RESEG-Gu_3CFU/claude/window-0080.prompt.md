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
[Block 2801]
བདག་ནི་མི་སློབ་ཅེས་བྱ་བ་བསྟན་པ་དང་། འདུལ་བ་དང་སོ་སོར་ཐར་པའི་མདོ་ལ་སོགས་པ་དང་། ཆོས་མངོན་པ་ལ་སོགས་པ་སློབ་པ་ཉིད་དང་མི་བརྩོན་པ་ཉིད་ལྷུང་བཟེད་ལ་སོགས་པ་ལས་ལྷག་མ༌[^1908]མེད་པ་དང་། བདག་ལ་ཅིའང་མེད་དོ་ཞེས་བྱ་བ་སྐྱེ་བའི༌[^1909]ཐ་མ་བཟློག་པ་ཉིད་ཅེས་བྱ་བའོ། །

[Block 2802]
གྲུར་འགྲོ་བ་དག་ལ་རྒྱུན་དུ་ཞུགས་པའི་འབྲས་བུ་ཞེས་བྱ་བ་བསྟན་པ་ཉིད་དེར་འབྲས་བུ་འདི་ལ་མེ་ཏོག་ལ་སོགས་པ་བདག་ཉིད་ཀྱིས་བཟུང་ནས་འབྲས་བུ་ཐོབ་པོ་ཞེས་བྱ་བ་དང་། ཁྱོད་ནི་ཟག་པ་མེད་དོ་ཞེས་བྱ་བ་ལ་སོགས་པས་འདྲི་བའི་བདག་ཉིད་ལ་བདག་ལ་འཚོ་བ་ལ་སོགས་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་འདི་འདས་པའོ། །

[Block 2803]
འཚོ་བའི་འཇིགས་པ༌[^1910]ལས་བདག་ནི་འཇིགས་པ༌[^1911]མ་ཡིན་ཞེས་བྱ་བ་དང་བདག་ནི་ཀུན་ཏུ་སྦྱོར་བ་ལ་སོགས་པ་ལས་གྲོལ་ལོ་ཞེས་བྱ་བའི་མིང་དང་བཅས་པའི་དོན་ལ་དགོངས་ནས་བླ་མའི་མིང་དང་འདྲ་བའི་མིང་དེ་ལ་བླ་མ་བསྟན་པའི་འདུན་པས་བརྗོད་པ་ལ་སྦོམ་པོའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2804]
གཞན་གྱིས༌[^1912]ཐོས་པ་ལ་ཡོད་པར་འགྱུར་བ་འདི་རྟོགས་པར་བྱའོ། །

[Block 2805]
ནོར་ན་ཡང་ངོ་ཞེས་བྱ་བ་ནི་བརྗོད་པ་ཞེས་བྱ་བ་དང་སྦྱར་རོ། །

[Block 2806]
རྒྱུན་དུ་ཞུགས་པའི་འབྲས་བུ་ལ་སོགས་པ་མི་བདེན་པ་མིའི་ཆོས་བླ་མ་བརྗོད་པར་བྱའོ་སྙམ་པ་ལས་ནོར་ཏེ་ལན་ཅིག་ཕྱིར་འོང་བའི་འབྲས་བུ་ལ་སོགས་པ་གོང་མ་དག་བརྗོད་ན་སྦོམ་པོར་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2807]
གཞོགས་སྨོས་ཀྱང་ངོ་ཞེས་བྱ་བ་ལ། ཡང་གི་སྒྲས་ནི་སྦོམ་པོ་ཞེས་བསྙག་པའི་དོན་དུའོ། །

[Block 2808]
ཨེ་མའོ༌[^1913]ཁྱོད་ཁོ་བོ་ཅི་འདྲ་བ་དེ༌[^1914]འདྲ་བར་འགྱུར་རོ། །

[Block 2809]
ཁོ་བོ་དང་ཁྱོད་དང་འུ་ཅག་འདི་ལྟར་རྒྱུན་དུ་ཞུགས་པ་དང་། ལན་ཅིག་ཕྱིར་འོང་བ་དང་། ཕྱིར་མི་འོང་བ་དང་། དགྲ་བཅོམ་པ་རྣམས་སུ་གྱུར་ཅིག །བདག་ནི་རྒྱུན་དུ་ཞུགས་པ་མ་ཡིན་པ་ནས་ཇི་སྲིད་དུ་དགྲ་བཅོམ་པའི་བར་ཡང་མ་ཡིན་ནོ་ཞེས་དེ་སྐད་དུ་ཟེར་ཞིང་། གང་གི་ཕྱིར་བདག་ནི་རྒྱུན་དུ་ཞུགས་པ་དང་། ལན་ཅིག་ཕྱིར་འོང་བ་དང་། ཕྱིར་མི་འོང་བ་དང་། དགྲ་བཅོམ་པ་ཡིན་ཞེས་སུ་ཟེར་ཞེས་བྱ་བའོ། །

[Block 2810]
བདག་ནི་དེང་ནས་འཇིག་རྟེན་པའི་བསམ་གཏན་ལ་སྙོམས་པར་ཞུགས་པ་མ་ཡིན་ཏེ་ཁར་རྩང༌[^1915]ནི་མ་ཡིན་ནོ། །

[Block 2811]
དེ་བས༌[^1916]གཞན་པས་ཀྱང་དུས་གཅིག་གི་ཚེ་ན་ཡང་མ་ཡིན་ནོ། །

[Block 2812]
ཚུར་ཤོག་འབྲས་བུ་རྣམས་ལ་ལུང་བསྟན་པར་བགྱིའོ། །

[Block 2813]
རྒྱུན་དུ་ཞུགས་པའི་འབྲས་བུ་ལ་ལུང་བསྟན་པར་འགྱུར་བར་བགྱི་སྟེ། བདག་ནི་རྒྱུན་དུ་ཞུགས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་སོགས་པ་འདི་ལྟ་བུ་ལ་སོགས་པ་ལ་མཐར་བྱེད་པ་བླ་མ་མཚོན་པ་གཞན་གྱིས་ཐོས་བཞིན་པ་ལས་སྦོམ་པོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2814]
ཡང་དག་པར་ཕྱི་མ་ཉིད་ལ་དེ་མི་འབྱུང་བ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། ཡང་དག་པ་ནི་བདེན་པའོ། །

[Block 2815]
ཕྱི་མའི་གང་ལ་ཡོད་པ་ཞེས་བྱ་བའི་བསྡུ་བའོ། །

[Block 2816]
བདེན་པའི་དོན་ཅན་གཞན་མ་གྲོལ་བ་ལ་སྔ་མའི་ཚིག་ལ་གཞོགས༌[^1917]སྨོས་མ་བྱས་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 2817]
གང་གི་ཕྱིར་མ་བྱས་པ་ཉིད་ནི༌[^1918]བྱས་པའི་དོན་ཇི་ལྟར་ཡང་རྟོགས་པར་བཟོད་པ་མ་ཡིན་ནོ། །

[Block 2818]
འདིར་གཞུང་ནི། བཙུན་པ་དགེ་སློང་འདི་སྐད་ཅེས་སློང༌[^1919]མོ་སྟེར་བའི་ཁྱིམ་ཆེ་གེ་མོ་དགེ་སློང་གང་གི་ཡིན་པའི་དགེ་སློང་དེ་ནི་རྒྱུན་དུ་ཞུགས་པ་དང་ལན་ཅིག་ཕྱིར་འོང་བ་དང་ཕྱིར་མི་འོང་བ་དང་དགྲ་བཅོམ་པའོ། །

[Block 2819]
རིགས་དེ་སུ་ཞིག་གིས་ཏེ་དེ༌[^1920]ནི་བསོད་སྙོམས་པའི་རིགས་སོ། །

[Block 2820]
དེས་སྨྲས་པ། ཁོ་བོའི་སྟེ་ཁོ་བོ་ནི་རྒྱུན་དུ་ཞུགས་པ་དང་ལན་ཅིག་ཕྱིར་འོང་བ་དང་ཕྱིར་མི་འོང་བ་དང་དགྲ་བཅོམ་པ་མ་ཡིན་ཞེས་མཆི་ན་ལྟུང་བ་ཅིར་འགྱུར། ཉེས་པ་སྦོམ་པོར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2821]
ཕམ་པ་བཞི་པ་ལས་ཉེ་བ་འཁོར་གྱི༌[^1921]ཞུས་པའོ།། །།

[Block 2822]
སྦོམ་པོ་ནི་བཙུན་པ་ནི་དགྲ་བཅོམ་པ་ཆོས་གོས་ལ་སོགས་པ་མཆོག་འོས་པ་བྲམ་ཟེ་སྡིག་པའི་ཆོས་བསལ་བ་བཙུན་པའི་དབང་པོ་དྲུག་པོ་དག་ནི་ཤིན་ཏུ་དུལ་བ་སྦས་པ། བསྲུངས་པ། བསྒོམས་པ༌[^1922]དག་ཡིན་ནོ་ཞེས་ཟེར་བ་ལ་ཅང་མི་སྨྲ་བས་དང་དུ་ལེན་པར་བྱེད་ནའོ་ཞེས་བྱ་བ་ལ། ཡང་དག་པར་ཞུགས་པ་ནི་ཡིད་ལ་དང་དུ་ལེན་པ་བརྗོད་ཡང་དོན་འདི་བསྒྲུབ་པ་སྟེ། དེ་བས་ན་ཅང་མི་སྨྲ་བའི་ངོ་བོ་ཞེས་བྱ་བ་ནི་བྱེ་བྲག་གོ། །

[Block 2823]
འདིར་ཅང་མི་སྨྲ་བ་ཉིད་ལ་རྣམ་པར་རིག་བྱེད་ཀྱིས༌[^1923]རྣམ་པ་ཉིད་བསྒྲུབ་པ་ཡིན་ཏེ། དེ་བས་ན་ཁ་ཅིག་རྣམས་ལ་རྟོགས་པའོ། །

[Block 2824]
དེ་བས་ན་འདིར་སྐྱོན་འདི་དང་དུ་བླངས་པ་གཞན་གྱིས་རྟོགས་པ༌[^1924]ཡོད་པར་འགྱུར་བ་ལ་འདི་སྦོམ་པོའོ། །

[Block 2825]
གཞན་དུ་ནི་འདི་ལྟ་བུ་ན་སྨད་པ་ཞེས་བྱ་བ་རིག་པར་བྱའོ། །

[Block 2826]
བཙུན་པ་གལ་ཏེ་དགྲ་བཅོམ་པ་ཡིན་ན་བདག་གི་བསོད་སྙོམས་ལོང་ཤིག༌[^1925]ཁྱིམ་དུ་ཞུགས་ཤིག་སྟན་ལ་འདུག་ཤིག༌[^1926]ལག་ཆུ་བཟེད་ཅིག །བཟའ་བ་དང་སྲན་ཚོད་དང་བཅའ་བ་ལོང་ལ་ཟོ་ཤིག །[^1927]རྗེས་སུ་ཡི་རང་བར༌[^1928]བྱོས་ཤིག །བྱུང་ཤིག༌[^1929]ཅེས་ཟེར་བ་ལ་དེ་བཞིན་དུ་བསྒྲུབ་ནའོ་ཞེས་བྱ་བ་ནི་སོ་སོར་འདིར་བརྗོད་པ་ཞེས་བྱ་བའི་ཚིག་ལ། བཙུན་པ་གལ་ཏེ་དགྲ་བཅོམ་པ་ཡིན་ན༌[^1930]ཞེས་བྱ་བ་འདི་ལོང་ཤིག༌[^1931]ཅེས་བྱ་བ་རྣམས་ལ་བསྒྱུར་བར༌[^1932]བྱའོ། །

[Block 2827]
བཟའ་བ་དང་སྲན་ཚོད་ཅེས་བྱ་བ་ནི་ལོང་ཤིག༌[^1933]ཅེས་བྱ་བ་འདི་གཉིས་ཀ་ཡང་སྦྱར་ཏེ་དེ་བཞིན་དུ་བསྒྲུབ་ནའོ་ཞེས་བྱ་བའོ། །

[Block 2828]
ཇི་སྐད་དུ་གསུངས་པ་དེ་ལྟར་བསྒྲུབ་པ་ལ་བཙུན་པ་གལ་ཏེ་དགྲ་བཅོམ་པ་ཡིན་ན་བདག་ཉིད༌[^1934]བསོད་སྙོམས་ལོང་ཤིག༌[^1935]ཅེས་ཟེར་བ་ལ་དེ་བཞིན་དུ་བསྒྲུབ་པ་ལ་བསོད་སྙོམས་ལེན་པར་བྱེད་ན་སྦོམ་པའོ།[^1936] །གཞན་དུ་ན་ཡང་ཇི་ལྟར་རིགས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2829]
བཙུན་པ་གལ་ཏེ་དགྲ་བཅོམ་པ་ཡིན་ན་རྗེས་སུ་ཡི་རང་བར་མཛོད་ཅིག་ཅེས་ཟེར་བ་ལ་ཅང་མི་སྨྲ་བའི་ངོ་བོས༌[^1937]རྗེས་སུ་ཡི་རང་བ༌[^1938]ལ་སྦོམ་པོའམ་འདིར་ཚིག་གིས་ནི་ཕམ་པའོ། །

[Block 2830]
ཕམ་པར་འགྱུར་བ་བཞི་པ་འདུལ་བྱེད་ཀྱི་སྐབས་ལས་བླ་མ་བརྗོད་པའོ།། །།

[Block 2831 [HEADING]]
## དགེ་འདུན་ལྷག་མ་རྣམས། ^6-0

[Block 2832]
རྨི་ལམ་ནི་མེད་པ་དང་འདྲའོ་ཞེས་བྱ་བ་ནི་ཐ་སྙད་ཀྱི་ཆོས་ལས་ཡང་དག་པར་འདས་པ་ཉིད་ཀྱི་ཕྱིར་རྨི་ལམ་གྱི་དངོས་པོ་མེད་པ་དང་འདྲ་བ་ཉིད་དོ། །

[Block 2833]
དེའི་འབྲས་བུ་ནི་མ་བྱས་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་རྨི་ལམ་གྱི་འབྲས་བུ་ལ་རྨི་ལམ་གྱི་བདག་ཉིད་ཀྱིས༌[^1939]སེམས་དམིགས་པའི་བུད་མེད་ལ་སོགས་པས་གང་ཞིག་བྱས་པས་ཁུ་བ་འབྱིན་པ་ནི་བྱ་བའོ། །

[Block 2834]
ཚིག་ཀྱང་བྱེད་པ་དང་བཅས་པའི་བྱ་བ་ཅན་ནོ། །

[Block 2835]
བྱ་བ་མ་བྱས་པ་དེ་ནི་ལྟུང་བ་མ་ཡིན་ཏེ། ལྟུང་བའི་མཚན་མ་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །གང་དུ་ཁུ་བ་འབྱིན་པ་དགེ་འདུན་གྱི་ལྷག་མ་ཞེས་བྱ་ཞེ་ན། དེའི་ཕྱིར་ཕྱུང༌[^1940]ནའོ་ཞེས་བྱ་བ༌[^1941]སྨོས་སོ། །

[Block 2836]
སེམས་ཇི་ལྟ་བུ་ཞེ་ན། དེའི་ཕྱིར་དེར་འདུན་པས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འབྱིན་པར་འདུན་པས་ཡིན་གྱི་རྒྱུག་པ་ལ་སོགས་པའི་སེམས་ནི་མ་ཡིན་ནོ། །སུ་ལས་ཕྱུང་བ་ཞེ་ན། དེའི་ཕྱིར་རང་གི་ཁུ་བའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རང་གི་ཁུ་བ་ཡིན་གྱི་གཞན་གྱི་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2837]
འདི་ལ་ཁུ་བ་ཕྱུང་བ་ནི་མང་དུ་ཡོད་དེ། གནས་ནས་དབྱུང་བ་དང་གཞན་ཡང་སྦུབས་སུ་འོང་བས་དབྱུང་བ་དང་། དབང་པོའི་མཐའ་ནས་དབྱུང་བ་ནི་གསུམ་པ་ཞེས་བྱའོ། །

[Block 2838]
འདི་རྣམས་འདི་ལ་སུ་ཞིག་ལས་ཕྱུང་བ་ཞེ་ན། དེའི་ཕྱིར་དང་པོ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རང་གི་ཁུ་བ་ཡིན་པ་ནི་དང་པོ་སྟེ་ཕྱུང་བ་དེ་ལའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2839]
ཁུ་བ་ལ་ནི་མ་ཡིན་ཏེ་འོན་ཀྱང་ལུས་འདི་ལ་ཁུ་བའི་གནས་སུ་གྱུར་པ་ལོགས་ཤིག་ན་འཁྲིས་པ་ལྟ་བུ་མེད་དེ། ཡན་ལག་རྣམས་ལས་འབྱུང་བ་སྟེ། དཔེར་ན་བུ་རམ་ཤིང་ལས་ཁུ་བ་དང་ཤ་ལས་ཚིལ་དང་། ཞོ་ལས་མར་རོ། །

[Block 2840]
དེ་བཞིན་དུ་འདིར་འཕོ་བ་རྟོགས་པར་བྱའོ། །
--- END BLOCKS ---
