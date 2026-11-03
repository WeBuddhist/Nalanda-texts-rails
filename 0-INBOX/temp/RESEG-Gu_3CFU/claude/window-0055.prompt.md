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
[Block 1926]
དེ་རྣམས་ཀྱི་བར་ཉིད་དེ་བར་ཆད་ནི་ངེས་པ་སྟེ། འདི་རྣམས་ལ་སོ་སོར་གནས་པ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 1927]
སོགས་པའི་སྒྲས་ནི་སོ་དང་སྣས་བར་དུ་བཅད་པ་བཟུང་བའོ། །

[Block 1928]
སོག་ཆགས༌[^1341]ལ་གཅིག་པ་ཉིད་ཀྱི་ཕྱིར་སྲོག་ཆགས་ཀྱི་ལུས་ཀྱི་བདག་ཉིད་ལ་གཅིག་པ་ཉིད་ཀྱི་ཕྱིར་དུ༌[^1342]གནས་ཀྱང་གཅིག་པ་ཉིད་ཅེས་བྱ་བའི་དོགས་པ་བཟློག་པའི་དོན་དུའོ།[^1343] །ཤ་དང་ཁྲག་ཉིད་ཉེ་བར་བརྟགས་པ་ཉིད་ལ་འདིའི་ཐ་དད་པར་བརྟག༌[^1344]ཏུ་རུང་བ་ཉིད་ཀྱི་ཕྱིར་རྩིབ་མ་ལ་སོགས་པ་རྣམས་ཉིད་ལ་གནས་པ་ཉིད་ཡིན་ཏེ་སྟོབས་ཆུང་བ་ཉིད་ལ་མ་ཡིན་ནོ། །

[Block 1929]
འདི་རྣམས་ཀྱི་ལུས་ཀྱི་བདག་ཉིད་ཀྱི་གནས་ལ་ཆ་ཤས་ཉིད་ཀྱི་ཕྱིར་སོ་སོར་གནས་པ་ཉིད་ཤེས་པར་བྱ་བ་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1930]
དེས་ན་རྩིབ་མ་ཞིག་གཅིག་གི༌[^1345]ཕྱོགས་ནས་རྩིབ་མ་ཐ་དད་པར་བརྟག༌[^1346]ཏུ་རུང་བ་ཉིད་གཞན་གྱི་བར་དུ་སྤོས་ན་བརྐུས་པ་ཉིད་དུ་བརྗོད་པར་བྱའོ། །

[Block 1931]
གདིང་བ་བཏིང་བ་ཉིད་གནས་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ས་ལ་སོགས་པ་གཞིར་རྩྭ་ལ་སོགས་པའི་གདིང་བ་བཏིང་བ་ཉིད་ཡོད་ན་གདིང་བ་དེ་ཉིད་ཀྱིས༌[^1347]དེ་ལ་གནས་པའི་རྫས་ལ་གནས་པ་ཉིད་དེ་ས་ལ་སོགས་པ་དེ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 1932]
གདིང་བ་བཏིང་བའི་སྒྲ་དག་ལ་ཡང་དག་པའི་སྒྲ་ཐོག་མར་ལྡན་པ་མ་བྱས་སོ། །

[Block 1933]
བྲག་ལ་སོགས་པ་གདིང་བ་ཐམས་ཅད་ལ་གདིང་བ་ཁོངས་སུ་བསྡུས་པའི་དོན་དུའོ། །

[Block 1934]
ཡང་དག་པར་གདིང་བ་བཏིང་བ་ཞེས་བྱ་བ་བརྗོད་པར་གྱུར་ན་རྩྭ་དང་ཤིང་ལོ་ལ་སོགས་པའི་རང་བཞིན་ཉིད་ཀྱི་གདིང་བ་ཉིད་ལ་གོ་བར་འགྱུར་རོ།[^1348] །སྐྱེ་བ་ནི་བཞག་པ་དང་འདྲའོ་ཞེས་བྱ་བ་ནི་རྩྭ་དང་གེལ་བ་དང་རྩི་དང་ནགས་ཚལ་ལ་སོགས་པ་འབྱུང་བའི་སྐྱེ་བ་ནི་དཔེར་ན་རྫས་བཞག་པ་བརྐུས་པ་དང་འདྲ་བས་དེ་བཞིན་དུ་བལྟ་བར་བྱའོ། །

[Block 1935]
གནས་ནས་སྤོ་བ་ནི་འདི་ལ་རྐུ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1936]
འབྲེལ་པ་སེལ་བ་ཙམ་ནི་མ་ཡིན་ཏེ། གང་ཞིག་འདི་ལ་ས་ལ་སོགས་པ་བསྡུ་བའོ། །

[Block 1937]
འདིར་གཞུང་ནི། དགེ་སློང་གིས་མེ་ཏོག་གི་ཤིང་ལྗོན་པ་ཕྱུང་སྟེ། རྐུ་ན་ཇི་སྲིད་དུ་ནོམ་པར་མི་བྱེད་པའི་བར་དུ་ནི་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 1938]
ནོམ་པ་ནས་གནས་དང་སྤོ་བའི་བར་གྱིས་ནི་བརྐུས་པ་ཞེས་བྱ་བ་སྟེ། མེ་ཏོག་གི་ཤིང་གི་རིན་ཐང་བརྩི་བར་བྱའོ་ཞེས་བྱ་བ་གསུངས་པ་ཡིན་ནོ། །

[Block 1939]
ཁ་ཅིག་ནི་མེ་ཏོག་གི་ཤིང་ཕྱུང་སྟེ། རྐུ་ན་མེ་ཏོག་གི་ཤིང་གི་རིན་ཐང་བགྲང་བར་བྱེད་ཅེས་བྱ་བ་འདི་ཙམ་འདོན་པ་ཡིན་ཏེ་ལྷག་མ་ནི་མ་ཡིན་ནོ། །

[Block 1940]
འདོན་པ་འདི་ལ་ཡང་གནས་ནས་སྤོ་བ་ལས་ཆོ་ག་གཞན་ལ་ལྡང་བ་དོགས་པར་བྱ་བ་མ་ཡིན་ཏེ། འདིར་ཕྱུང་བ་ཉིད་རྐུ་བར་བརྗོད་པ་ཡིན་ཏེ། འདིར་རྐུ་བའི་ཁྱད་པར་ནི་འདོད་པ་ཞེས་བྱ་བར་རྣམ་པར་གནས་ཏེ་ཕྱུང་ནས་རྐུ་བ་ཞེས་བྱའོ། །

[Block 1941]
ཇི་ལྟར་ཁ་ཕྱེ་ནས་ཉལ་བ་དང་ཕྱེ་བའི་ཁས་ཉལ་བར་བྱེད་པ་ཞེས་བྱ་བ་ལྟ་བུའོ།[^1349] །ཕྱུང་བ༌[^1350]ཡང་གནས་ཉིད་ནས་སྤོས་པ་ཡིན་ཏེ་ས་དང་འབྲེལ་པ་བསལ་བའི་འོག་ཏུ་རྐུ་བ་འདི་ཡིན་ནོ། །

[Block 1942]
གང༌[^1351]དུ་ཐམས་ཅད་རྡུལ་ཕྲ་རབ་ཙམ་ཡང་འགྲོ་བ་ནི་འཕོ་བ་གནས་ལས་སོ། །

[Block 1943]
བསྐོན་པ་ནི་ཕུད་ནའོ་ཞེས་བྱ་བ་བརྐུས་པ་ཞེས་བྱ་བ་དང་རྗེས་སུ་འབྲེལ་ལོ། །

[Block 1944]
ཕུད་ནའོ་ཞེས་བྱ་བ་ནི་ཕུད་པ་དང་བཀྲོལ་བ་སྟེ་དེ་ལ་གང་དུ་ཡོངས་སུ་བསལ་བའོ། །

[Block 1945]
དེ་ལ་བསྐོན་པ་གང་ཡིན་པ་དེ་ནི་བརྐུས་པའོ། །

[Block 1946]
འདིར་གཞུང་ནི། དེ་དག་རྒྱན་སྣ་ཚོགས་དག་གིས་བརྒྱན་པར་གྱུར་པ་དགེ་སློང་གིས་བརྒྱན་པར༌[^1352]གྱུར་པ་དེའི་སྦྱོར་བས་ཁྲི་ལས་ལྡང་བ་ནས། ནོམ་ཉུག་མི་བྱེད་པའི་སྦྱོར་བའི་སྦྱོར་བ་ཇི་སྲིད་དུ་ནོམ་ཉུག་བྱེད་པ་ནས་གནས་ནས་གནས་གཞན་དུ་མ་སྤོས་པའི་བར་དུ༌[^1353]བྱེད་ན་སྦྱོར་བ་གནས་ནས་སྤོ་བའི་ཚེ་བརྐུས་པར་བརྗོད་པར་བྱ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ནོ། །

[Block 1947]
འདིར་བསྐོན་པ་ནི་གནས་གཞན་དུ་འཕོ་བ་ལ་མངོན་པར་འདོད་པས་རྣམ་པར་གནས་པ་སྟེ། དེའི་ཕྱིར་འདི་ལྟར་ཉེ་བར་བརྟགས་པའོ། །

[Block 1948]
ཇི་ལྟར་ཡང་རྣམ་པར་དབེན་པར་གནས་གཞན་ནས་འཕོ་བ་སྟེ་གང་གི་ཕྱིར་ཕྱུང་བ་ནི་བཏོན་པའོ། །

[Block 1949]
དེ་བས་ན་ཕྱུང་བར་བྱེད་པ་ནི་འདིར་མ་ཆད་པ་སྟེ། གཞན་པའི་གནས་དོར་བ་ནི་མ་ཡིན་ནོ། །

[Block 1950]
ཕྲལ་བའི་སྐབས་བཤལ་བ་ནི་ཕྱུང་བར་བྱེད་པའི་ཚུལ་མ་ཡིན་པ་ཞེས་བྱ་བའོ། །

[Block 1951]
ཤོ་གམ་ནི་ས་འདས་ནའོ་ཞེས་བྱ་བ་ནི་རྐུ་བ་ཞེས་བྱ་བ་དང་རྗེས་སུ་འབྲེལ་ཏོ། །

[Block 1952]
འདིར༌[^1354]ཤོ་གམ་གྱི་གནས་ནི་སའོ། །

[Block 1953]
དེ་ཡང་གང་དུ་ཇི་ཙམ་ཞུགས་པ་ལ་ཤོ་གམ་པ་ལ་སྦྱིན་པར་བྱ་བ་ཉིད་དེ། དེ་ཙམ་དུ་ས་དེ་ལས་འདས་པ་ནི་འདས་པའོ། །

[Block 1954]
གང་ཞིག་ཤོ་གམ་བྱ་བ་ཉིད་ཀྱིས་ཤོ་གམ་གྱི་ས་ལས་འདས་པ་ནི་ཤོ་གམ་གྱི་ས་དེ་ཉིད་ཀྱིས་ཡིན་གྱི་ཕྱོགས་གཞན་གྱིས་ནི་མ་ཡིན་ཏེ། འདས་པ་དེ་ན༌[^1355]ཤོ་གམ་རྐུ་བའོ། །

[Block 1955]
ཤོ་གམ་ཉིད་ལ་ནི་དེ་འདའ་བར་བྱེད་པ་སྟེ། གང་ཞིག་ཤོ་གམ་བྱ་བ༌[^1356]ལ་ཤོ་གམ་བྱ་བའི་ཆར་གྱུར་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1956]
རྒྱུད་པས་ཀྱང་ས་ལ་བརྟེན་པ་ཉིད་ཀྱིས༌[^1357]དགོས་པ་ནི་མ་ཡིན་ཏེ། དེ་བས་ན་ཁུར་བས་སམ་རང་གི་ལུས་ཀྱིས༌[^1358]སམ། ཟླ༌[^1359]ལ་སོགས་པས་སམ་རང་གི་ལུས་ཀྱིས་ཁུར་བ་དང་འབྲེལ་པས་ཤོ་གམ་གྱི་བྱ་བ་འདའ་བར་བྱེད་པ་ནི་གང་ཞིག་ཤོ་གམ་འདའ་བར་བྱེད་པ་འདི་ལ་ས་ཡིས་ནི་མ་ཡིན་ནོ། །

[Block 1957]
དེ་བས་ན་འདིར་འདི༌[^1360]ཡང་དག་པར་བསྡུས་ནས་འདའ་བར་བྱེད་པ་བཟུང་བ་མ་ཡིན་པ་ཤེས་པར་བྱའོ། །

[Block 1958]
ཤོ་གམ་གྱི་གནས་སུ་ཞུགས་པ་ལ་གང་ཞིག་ཆུ་ཞེང་དུ་འཇུག་པས་འདའ་བར་བྱེད་པ་དེ་ལ་རེ་ཞིག་ཐེ་ཚོམ་མེད་པ་ཉིད་དུ་དེས་ས་ལས་འདའ་བར་བྱེད་པའོ། །

[Block 1959]
ལོག་ནས་གནས་གཞན་དུ་འགོ་བ་ལ་གལ་ཏེ་ཞུགས་པ་ལས༌[^1361]ས་ལ་སོགས་པ༌[^1362]ཡང་སྦྱིན་པར༌[^1363]བྱ་བ་ཉིད་ཡོད་པ་འདི་ནི་འདའ་བར་བྱེད་པའོ། །

[Block 1960]
དེ་ཡང་ལོག་པ་གང་ཞིག་འདི་དེ་ཉིད་ཡིན་གྱི་གཞན་ནི་མ་ཡིན་ཞེས་བྱ་བའོ། །

[Block 1961]
འོ་ན་སྦྱིན་པར་བྱ་བ་ཉིད་མ་ཡིན་ན༌[^1364]ལོག་པ་ལ་འདའ་བར་བྱེད་པ་འདི་ཡོད་པ་མ་ཡིན་ཞེས་བྱ་བར༌[^1365]རིག་པར་བྱའོ། །

[Block 1962]
རྣམ་པར་གཞག་པའི་དབང་གིས་འདི་སྦྱིན་པ་ཉིད་དོ། །

[Block 1963]
གང་དུ་འདའ་བར་བྱེད་པ་མཐོང་བར་སྒོ་ཆེ་གེ་མོར་ཞུགས་པ་ལ་སྦྱིན་པར་བྱ་བ་ཉིད་མ་ཡིན་ཞེས་བྱ་བ་ལ་སོགས་པའི་རྣམ་པར་གཞག་པར་བྱས་པར་འགྱུར་བ་དེ་ལ་སྦྱིན་པ་ཉིད་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1964]
མི་ལ་གལ་ཏེ་བརྡས་ནི་དེ་གྲུབ་པ་ནའོ་ཞེས་བྱ་བ་ལ་མི་རྐུ་བ་ནི་རྣམ་པ་མང་དུ་འགྱུར་ཏེ་མི་འདོད་བཞིན་དུ་དཀྲིས་པ༌[^1366]དང་གཞག་པ་དག་གིས་སོ། །

[Block 1965]
འཇིག་པའི་རྒྱུ་མཚན་གྱིས་སམ་ཀུན་དུ་རྒྱུ་བས་རྣམ་པར་རྨོངས་པར་གྱུར་པ་ལ་ཡང་སྔགས་དང་སྨན་དག་གིས་སོ། །
--- END BLOCKS ---
