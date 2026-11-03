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
སྐལ་བ་མཉམ་པའི་རྒྱུ་ནི་རང་གི་ས་པ་ཡིན་ནོ་ཞེས་བཤད་པ་གང་ཡིན་པ་ཅི་དེ་ལྟར་ངེས་སམ་ཞེ་ན། དེ་ཟག་པ་དང་བཅས་པ་ལ་ནི་ངེས་སོ། །

[Block 1927 [VERSE]]
ས་དགུའི་ལམ་ནི་ཕན་ཚུན་དུ། །
སྐལ་བ་མཉམ་པའི་རྒྱུ་ཡིན་ནོ། །

[Block 1928]
ཞེས་བྱ་བར་སྐབས་དང་སྦྱར་ཏེ། མི་ལྕོགས་པ་མེད་པ་དང་བསམ་གཏན་ཁྱད་པར་ཅན་དང་། བསམ་གཏན་བཞི་དང་། གཟུགས་མེད་པ་གསུམ་དག་གི་ལམ་གྱི་བདེན་པ་ནི་ཕན་ཚུན་དུ་སྐལ་བ་མཉམ་པའི་རྒྱུ་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན། འདི་ནི་ས་དེ་དག་ཏུ་གློ་བུར་དུ་འོངས་པ་ཡིན་ལ། ས་དེ་པ་དག་གིས༌[^965]བདག་གིར་མ་བྱས་པའི་ཕྱིར་ཁམས་དེ་དག་ཏུ་གཏོགས་པ་མ་ཡིན་ཏེ། དེ་བས་ན་ས་གཞན་པའི་རིགས་མཐུན་པའི༌[^966]སྐལ་བ་མཉམ་པའི་རྒྱུ་ཡང་ཡིན་ནོ། །

[Block 1929]
དེ་ཡང་།

[Block 1930 [VERSE]]
མཉམ་དང་ཁྱད་པར་ཅན་གྱི་ཡིན། །
ཆུང་ངུའི༌[^967]རྒྱུ་ནི་མ་ཡིན་ཏེ། །

[Block 1931]
འདི་ལྟ་སྟེ། སྡུག་བསྔལ་ལ་ཆོས་ཤེས་པའི་བཟོད་པ་ནི་དེ་ཉིད་མ་འོངས་པ་དང་མི་སྐྱེ་བ་ཤེས་པའི་ཁྱད་པར་ཅན་གྱི་རྒྱུ་ཡང་ཡིན་ནོ། །

[Block 1932]
མི་སྐྱེ་བ་ཤེས་པ་ནི་ཁྱད་པར་ཅན་གཞན་མེད་པའི་ཕྱིར་མི་སྐྱེ་བ་ཤེས་པ་ཁོ་ནའི་ཡིན་ནོ། །

[Block 1933]
མཐོང་བ་དང་བསྒོམ་པ་དང་མི་སློབ་པའི་ལམ་རྣམས་ནི་གསུམ་དང་གཉིས་དང་གཅིག་དག་གི་ཡིན་ནོ། །

[Block 1934]
དེ་ལ་ཡང་དབང་པོ་རྟུལ་པོའི་ལམ་ནི་དབང་པོ་རྟུལ་པོ་དང༌[^968]རྣོན་པོའི་ལམ་གྱི་རྒྱུ་ཡིན་ལ། དབང་པོ་རྣོན་པོའི་ལམ་ནི་དབང་པོ་རྣོན་པོའི་ལམ་ཁོ་ན༌[^969]ཡིན་ཏེ། འདི་ལྟ་སྟེ་དད་པས་རྗེས་སུ་འབྲང་བ་དང་དད་པས་མོས་པ་དང་དུས་ཀྱིས་རྣམ་པར་གྲོལ་བའི་ལམ་རྣམས་ནི་དྲུག་དང་བཞི་དང་གཉིས་དག་གི་ཡིན་ནོ། །

[Block 1935]
ཆོས་ཀྱིས༌[^970]རྗེས་སུ་འབྲང་བ་དང་མཐོང་བས་ཐོབ་པ་དང་། དུས་དང་མི་སྦྱོར་བར་རྣམ་པར་གྲོལ་བའི་ལམ་རྣམས་ནི་གསུམ་དང་གཉིས་དང་གཅིག་གི་ཡིན་ནོ། །

[Block 1936]
ཡང་ཇི་ལྟར་ས༌[^971]གོང་མ་པས༌[^972]འོག་མ་པའི་ལམ་དང་མཉམ་བའམ་ཁྱད་པར་ཅན་ཡིན་ཞེ་ན། དབང་པོ་དང་རྒྱུས་རྒྱས་པར་བྱས་པའི་སྒོ་ནས་ཏེ། དེ་ལ་རྒྱུས་ཤིན་ཏུ་རྒྱས་པར་བྱས་པ་ནི་མཐོང་བའི་ལམ་ལ་སོགས་པ་དང་། ཆུང་ངུའི་ཆུང་ངུ་ལ་སོགས་པ་གོང་ནས་གོང་དུའོ། །

[Block 1937]
རྒྱུད་གཅིག་ལ་དད་པས་རྗེས་སུ་འབྲང་བ་དང་། ཆོས་ཀྱིས༌[^973]རྗེས་སུ་འབྲང་བའི་ལམ་དག་མི་སྲིད་མོད་ཀྱི་འབྱུང་བ་ནི་མ་འོངས་པའི་རྒྱུ་ཡིན་ནོ། །

[Block 1938]
ཅི་ལམ་ཁོ་ན་མཉམ་པ་དང་ཁྱད་པར་ཅན་དག་གི་སྐལ་བ་མཉམ་པའི་རྒྱུ་ཡིན་ནམ་ཞེ་ན་སྨྲས་པ་མ་ཡིན་ཏེ། འཇིག་རྟེན་པ་དག་ཀྱང་། སྦྱོར་བྱུང་དེ་གཉིས༌[^974]ཁོ་ནའི་ཡིན། །མཉམ་པ་དང་ཁྱད་པར་ཅན་དག་གི་སྐལ་བ་མཉམ་པའི་རྒྱུ་ཡིན་གྱི་དམན་པའི་ནི་མ་ཡིན་ནོ། །

[Block 1939]
དཔེར༌[^975]ཇི་ལྟ་བུ་ཞེ་ན་སྨྲས་པ། ཐོས་དང་བསམས༌[^976]བྱུང་ལ་སོགས་པའང་།[^977] །ཐོས་པ་དང་བསམས་པ༌[^978]དང་བསྒོམས་པ་ལས་བྱུང་བ་སྦྱོར་བ་ལས་འབྱུང་བའི༌[^979]ཡོན་ཏན་དེ་དག་ཀྱང་ཉམས་པ་དང་ཁྱད་པར་ཅན་དག་ཁོ་ནའི་རྒྱུ་ཡིན་གྱི་དམན་པ་རྣམས་ཀྱི་ནི་མ་ཡིན་ཏེ། འདི་ལྟ་སྟེ། འདོད་པ་ན་སྤྱོད་པའི་ཐོས་པ་ལས་བྱུང་བ་རྣམས་ནི་ཐོས་པ་ལས་བྱུང་བ་དང་བསམས་པ་ལས་བྱུང་བ་རྣམས་ཀྱི་ཡིན་ནོ། །

[Block 1940]
བསམ་པ༌[^980]ལས་བྱུང་བ་རྣམས་ནི་བསམས་པ་ལས་བྱུང་བ་རྣམས་ཀྱི་ཡིན་ཏེ། བསྒོམས་པ་ལས་བྱུང་བ་ནི་མེད་པའི་ཕྱིར་རོ། །

[Block 1941]
གཟུགས་ན་སྤྱོད་པའི་ཐོས་པ་ལས་བྱུང་བ་རྣམས་ནི་ཐོས་པ་ལས་བྱུང་བ་དང་བསྒོམས་པ་ལས་བྱུང་བ་རྣམས་ཀྱི་ཡིན་ཏེ། བསམས་པ་ལས་བྱུང་བ་ནི་མེད་པའི་ཕྱིར་རོ། །

[Block 1942]
བསྒོམས་པ༌[^981]ལས་བྱུང་བ་རྣམས༌[^982]ནི་བསྒོམས་པ་ལས་བྱུང་བ་རྣམས་ཁོ་ནའི་ཡིན་ནོ། །

[Block 1943]
དེ་དག་ཀྱང་རྣམ་པ་དགུ་ཐ་དད་པའི་ཕྱིར་ཆུང་ངུའི་ཆུང་ངུ་དག་ནི་ཐམས་ཅད་ཀྱི་ཡིན་ལ། ཆུང་ངུའི་འབྲིང་པོ་དག་ནི་བརྒྱད་ཀྱི་ཡིན་ཏེ། ལུགས་ནི་དེ་ལྟ་བུའོ།[^983] །སྐྱེས་ནས་ཐོབ་པ་ཅན་གྱི་དགེ་བའི་ཆོས་རྣམས་ནི༌[^984]རྣམ་པ་དགུ་པོ་ཐམས་ཅད་ཕན་ཚུན་དུ་སྐལ་བ་མཉམ་པའི་རྒྱུ་ཡིན་ཏེ། ཉོན་མོངས་པ་ཅན་རྣམས་ཀྱང་དེ་དང་འདྲའོ། །

[Block 1944]
མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་རྣམས་ནི་རྣམ་པ་བཞི་སྟེ། རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པ་དང་། སྤྱོད་ལམ་པ་འམ།[^985] བཟོའི་གནས་པ་དང་། སྤྲུལ་པའི་སེམས་ལྷན་ཅིག་སྐྱེས་པ་རྣམས་ཏེ། དེ་དག་ནི་གོ་རིམས་བཞིན་དུ་བཞི་དང་། གསུམ་དང་། གཉིས་དང་། གཅིག་དག་གི་སྐལ་བ་མཉམ་པའི་རྒྱུ་ཡིན་ནོ། །

[Block 1945]
སྤྲུལ་པའི་སེམས་བསམ་གཏན་བཞིའི་འབྲས་བུ་འདོད་པ་ན་སྤྱོད་པ༌[^986]ཡང་ཡིན་ཏེ། དེ་ལ་བསམ་གཏན་གོང་མའི་འབྲས་བུ་ནི་བསམ་གཏན་འོག་མའི་འབྲས་བུ་ནི་མ༌[^987]ཡིན་ནོ། །

[Block 1946]
འབད་པ༌[^988]འབྲས་བུ་མེད་པར་འགྱུར་དུ་འོང་བའི་ཕྱིར་སྐལ་བ་མཉམ་པའི་རྒྱུ་མངོན་པར་འདུ་བྱེད་པ་ཅན་གྱི་འབྲས་བུ་ནི་དམན་པ་མ་ཡིན་ཏེ། དཔེར་ན་སཱ་ལུ་དང་ནས་ལ་སོགས་པའི་ལྟ་བུའོ། །

[Block 1947]
དེ་ཉིད་ཀྱི་ཕྱིར་ཟག་པ་མེད་པ་སྐྱེས་པ་ཟག་པ་མེད་པ་མ་སྐྱེས་པའི་རྒྱུ་མ་ཡིན་པ་ཡོད་དམ་ཞེ་ན་ཡོད་དེ། དཔེར་ན་སྡུག་བསྔལ་ལ་ཆོས་ཤེས་པའི༌[^989]བཟོད་པ་མ་སྐྱེས་པ་རྣམས་ཀྱི་ལྟ་བུ་དང་། ཁྱད་པར་ཅན་ཐམས་ཅད་དམན་པའི་ལྟ་བུའོ། །

[Block 1948]
རྒྱུད་གཅིག་ལ་ངེས་པའི་ཟག་པ་མེད་པའི་ཆོས་སྔོན་ཐོབ་པ་ཕྱིས་སྐྱེས་པའི་རྒྱུ་མ་ཡིན་པ་ཡོད་དམ་ཞེ་ན། ཡོད་དེ་སྡུག་བསྔལ་ལ་ཆོས་ཤེས་པའི་བཟོད་པ་མ་འོངས་པ་དག་སྡུག་བསྔལ་ལ་ཆོས་ཤེས་པའི་ལྟ་བུའོ། །

[Block 1949]
[^990]འདི་ལྟར་འབྲས་བུ་སྔ་མའམ།[^991] སྐལ་བ་མཉམ་པའི་རྒྱུ་མ་འོངས་པ་ནི་མེད་དོ། །

[Block 1950]
ཟག་པ་མེད་པའི་ཆོས་སྔར་སྐྱེས་པ་རྣམས་ཟག་པ་མེད་པའི་ཆོས་ཕྱིས་སྐྱེ་བའི་རྒྱུ་མ་ཡིན་པ་ཡོད་དམ་ཞེ་ན་ཡོད་དེ། ཆེན་པོ་ཆུང་ངུའི་ལྟ་བུ་སྟེ། འདི་ལྟ་སྟེ། འབྲས་བུ་གོང་མ་ལས་ཡོངས་སུ་ཉམས་པ་འབྲས་བུ་འོག་མ་མངོན་དུ་བྱེད་པའི་ཚེ་དང་སྡུག་བསྔལ་ལ་ཆོས་ཤེས་པའི་ཐོབ་པ༌[^992]སྐད་ཅིག་མ་ཕྱི་མ་དང་ལྷན་ཅིག་སྐྱེས་པ་སྡུག་བསྔལ་ལ་ཆོས་ཤེས་པའི་བཟོད་པའི་ཐོབ་པ་རྣམས་ཀྱི་ལྟ་བུ་སྟེ། དམན་པའི་ཕྱིར་རོ་ཞེས་གསུངས་སོ། །

[Block 1951]
སྐལ་བ་མཉམ་པའི་རྒྱུ་བཤད་ཟིན་ཏོ། །

[Block 1952 [HEADING]]
###### མཚུངས་པར་ལྡན་པའི་རྒྱུ། ^2-4-1-1-4-0

[Block 1953]
མཚུངས་ལྡན་རྒྱུ་ནི་སེམས་དག་དང་། །སེམས་བྱུང་། དེ་ལྟ་ན་ནི་དུས་དང༌[^993]རྒྱུད་ཐ་དད་པ་ལས་སྐྱེས་པ་རྣམས་ཕན་ཚུན་དུ་མཚུངས་པར་ལྡན་པའི་རྒྱུ་ཉིད་དུ་ཐལ་བར་འགྱུར་རོ། །

[Block 1954]
འོ་ན་ནི་རྣམ་པ་དང་དམིགས་པ་གཅིག་ལ་དག༌[^994]པ༌[^995]ཡིན་ནོ། །

[Block 1955]
དེ་ལྟ་ན་ཡང་དེ་ཉིད་དུ་ཐལ་བར་འགྱུར་རོ། །

[Block 1956]
འོ་ན་ནི་དུས་གཅིག་པ་དག་ཡིན་ནོ། །

[Block 1957]
དེ་ལྟ་ན་ཟླ་བ་ཚེས་པ་ལ་སོགས་པ་ལ་ལྟ་བའི་ལྟ་བུར༌[^996]རྒྱུད་ཐ་དད་པ་ལས་སྐྱེས་པ་རྣམས་ལ་ཡང་ཐལ་བར་འགྱུར་ཏེ། དེ་ལྟ་བས་ན་རྟེན་མཚུངས་པ་ཅན་རྣམས་སོ། །

[Block 1958]
གང་དག་ལ་རྟེན་མཚུངས་པ་ཡོད་པའི་སེམས་དང་སེམས་ལས་བྱུང་བ་དེ་དག་ནི་ཕན་ཚུན་དུ་མཚུངས་པར་ལྡན་པའི་རྒྱུ་ཡིན་ནོ། །

[Block 1959]
མཚུངས་པ་ཞེས་བྱ་བ་ནི་ཐ་མི་དད་པ་སྟེ། འདི་ལྟ་སྟེ། མིག་གི་རྣམ་པར་ཤེས་པའི་རྟེན༌[^997]མིག་གི་དབང་པོའི་སྐད་ཅིག་མ་གང་ཡིན་པ་དེ་ཉིད་དེ་དང་མཚུངས་པར་ལྡན་པ་ཚོར་བ་ལ་སོགས་པ༌[^998]རྣམས་ཀྱི་ཡང་ཡིན་པ་ལྟ་བུ་སྟེ། ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་དང་དེ་དང་མཚུངས་པར་ལྡན་པ་རྣམས་ཀྱི་ཡིད་ཀྱི་སྐད་ཅིག་མ་ཡིན་པའི་བར་དུ་ཡང་དེ་བཞིན་དུ་རིག་པར་བྱའོ། །

[Block 1960]
མཚུངས་པར་ལྡན་པའི་རྒྱུ་གང་ཡིན་པ་དེ་ནི་ལྷན་ཅིག་འབྱུང་བའི་རྒྱུ་ཡང་ཡིན་ནོ། །

[Block 1961]
ཡང་དོན་གང་གིས་ན་ལྷན་ཅིག་འབྱུང་བའི་རྒྱུ་ཡིན། གང་གིས་ན་མཚུངས་པར་ལྡན་པའི་རྒྱུ་གང་ཡིན་ཞེ་ན། ཕན་ཚུན་འབྲས་བུའི་དོན་གྱིས་ན་ལྷན་ཅིག་འབྱུང་བའི་རྒྱུ་ཡིན་ཏེ། འདྲོན་པ༌[^999]རྣམས་ཕན་ཚུན་གྱི་སྟོབས་ཀྱིས༌[^1000]ལྷན་ཅིག་ལམ་དུ་འགྲོ་བ་ཡིན་ནོ། །

[Block 1962]
མཚུངས་པ་ལྔས་མཚུངས་པར་ལྡན་པའི་དོན་གྱིས་ན་མཚུངས་པར་ལྡན་པའི་རྒྱུ་ཡིན་ཏེ། འདྲོན་པ་དེ་དག་ཉིད་ཟས་ལ་སོགས་པ་ཡོངས་སུ་ལོངས་སྤྱོད་པའི་བྱ་བ་ལ༌[^1001]འདྲ་བར་སྦྱོར་བ་བཞིན་ནོ། །

[Block 1963]
གཅིག་མེད་ན་ཡང་ཐམས་ཅད་མཚུངས་པར་མི་ལྡན་པས་འདི་ནི་དེ་དག་གི་རྒྱུའི་དངོས་པོ་ཡིན་ནོ། །

[Block 1964 [HEADING]]
###### ཀུན་ཏུ་འགྲོ་བའི་རྒྱུ། ^2-4-1-1-5-0

[Block 1965]
ཀུན་ཏུ་འགྲོ་བའི་རྒྱུ་གང་ཞེ་ན།
--- END BLOCKS ---
