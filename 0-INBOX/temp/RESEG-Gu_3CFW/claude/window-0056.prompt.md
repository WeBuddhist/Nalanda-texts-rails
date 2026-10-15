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
[Block 1961]
མགུ་བ་དང་དབྱུང་བ་ནི་གཉིས་ཀ་ཚོགས་པ་ལའོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་མ་གཉིས་ཀྱིས་མགུ་བར་བྱ་བ་དང་དབྱུང་བ་ནི་དགེ་སློང་མའི་དགེ་འདུན་འབའ་ཞིག་ལ་བྱ་བར་མ་ཟད་ཀྱི། གཉིས་ཀའི་དགེ་འདུན་ཚོགས་པ་དུས་གཅིག་ཏུ་གནས་གཅིག་ན་འཁོད་པ་དག་ལ་བྱའོ། །

[Block 1962]
བསྙེན་པར་རྫོགས་པར་བྱས་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་དེ་ཡང་གཉིས་ཀའི་དགེ་འདུན་ཚོགས་པ་ལ་བྱའོ། །

[Block 1963]
འདི་ལ་དེ་དག་གི་ཚོགས་ནི་བཅུ་གཉིས་སོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་མ་བསྙེན་པར་རྫོགས་པར་བྱ་བ་འདི་ལ་དགེ་སློང་མ་དེ་དག་གི༌[^1724]ཚོགས་བཅུ་གཉིས་ཡན་ཆད་དོ། །

[Block 1964]
སྔོན་རོལ་གྱི་སྡོམ་པ་གཉིས་དང་། འཁོར་དང་འཁོར་མང་པོ་ཉེ་བར་གཞག་པའི་གནང་བ་སྦྱིན་པ་དང་བཅས་པའི་དགེ་འདུན་གྱི་མཐའོ་ཞེས་བྱ་བ་ནི་དེ་ནི༌[^1725]དགེ་སློང་མ་བསྙེན་པར་རྫོགས་པའི་སྔོན་རོལ་གྱི་སྡོམ་པ་གཉིས་པོ་བསླབ་པའི་སྡོམ་པ་དང་། ཚངས་པར་སྤྱོད་པ་ལ་ཉེ་བར་གནས་པའི་སྡོམ་པ་སྦྱིན་པའོ། །

[Block 1965]
ཡང་འཁོར་ཉེ་བར་འཇོག་པའི་གནང་བ་དང་ལྷན་ཅིག་ཏུ་འཁོར་མང་པོ་ཉེ་བར་འཇོག་པའི་གནང་བ་དང་ལྷན་ཅིག་ཏུ་དེས་འདིར་བསྙེན་པར་རྫོགས་པ་དང་བཅས་པའི་དགེ་སློང་མའི་གྲངས་ཀྱི་མཐའ་ཡིན་ནོ། །

[Block 1966]
འདི་ཡང་སྡོམ་པ་བཞི་པོ་སྦྱིན་པ་ལ་དེ་རྣམས་ལ་ཚོགས་བཅུ་གཉིས་ཡན་ཆད་ཁོ་ནས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1967]
ལྷག་མ་དག་གི་ཚོགས་ནི་བཞིའོ༌[^1726]ཞེས་བྱ་བ་ནི་དགེ་སློང་མའི་ལས་ལྔ་པོ་ཇི་སྐད་བསྟན་པ་དེ་དག་གི་ལྷག་མ་དགེ་སློང་མའི་དགེ་འདུན་གྱི༌[^1727]ལས་གཞན་ཐམས་ཅད་ལ་ནི་དགེ་སློང་མ་བཞིའི་ཚོགས་ཡན་ཆད་ཀྱིས༌[^1728]ལས་བྱར་རུང་ངོ་། །དེ་ལྟར་ཡང་འདིར་གཞུང་ནི། དགེ་སློང་མ་རྣམས་ཀྱི༌[^1729]ཚོགས་བཞིས་ལས་དག་བྱའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཡིན་ནོ། །

[Block 1968]
ལས་བྱེད་པ་པོས་མ་ནུས་ན་དེས་དགེ་སློང་གིས་བྱས་པའི་ཚིག་ངེས་པར་བརྟགས་ན་རུང་ངོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་མ་ལས་བྱེད་པ་ལས་བྱེད་མི་ནུས་ན་དེས་དགེ་སློང་གིས༌[^1730]ལས་བྱེད་པའི་ཚིག་ངེས་པར་བརྟགས་ཤིང་ཐོས་ན་དེས་ལས༌[^1731]བྱས་པ་ཉིད་དུ་རུང་བར་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །ཇི་ཙམ་ཡན་ཆད་ཅེ་ན། དེའི་ཕྱིར་འདི་ལྟར་ཅང་མི་གསུང་བས་ཞེས་བྱ་བའི་གོང་ཡན་ཆད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་སློང་འཕགས་མ་རྣམས་ཀྱིས་བཟོད་ཅིང་གནང་ནས་ཞེས་བྱ་བ་དེ༌[^1732]ནས་ཇི་སྲིད་དུ་འདི་ལྟར་ཅང་མི་གསུང་བས་དེ་དེ་བཞིན་དུ་འཛིན་ཏོ་ཞེས་བྱ་བའི་བར་དུ་དགེ་སློང་མ་ལས་བྱེད་པ་ཉིད་ཀྱིས་ངེས་པ་ཁོ་ནར་བརྗོད་པར་བྱ་དགོས་སོ། །

[Block 1969]
འདིར་གཞུང་ནི། མགུ་བ་དང་དབྱུང་བར་གཏོགས་པའི་དགེ་སློང་མའི་སོ་སོར་ཐར་པ་དང་། དེའི་རྣམ་པར་འབྱེད་པ་ལས་འཁོར་ཉེ་བར་འཇོག་པ་དང་། འཁོར་མང་པོ་ཉེ་བར་འཇོག་པའི་གནང་བ་སྦྱིན་པ་དང་།

[Block 1970]
དགེ་སློང་མའི་རྣམ་པར་འབྱེད་པ་ལས།

[Block 1971]
སོ་སོའི་དགེ་འདུན་གྱི་ཚད་གཞན་དུ་དེ་ཐ་མའོ་ཞེས་གསུངས་པ་དང་། འདིར་ཕྲན་ཚེགས་ལས་ཚིག་ངེས་པར་བཏགས་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 1972]
དགེ་སློང་མའི་རྣམ་པར་འབྱེད་པ་ལས།

[Block 1973]
བསླབ་པའི་སྡོམ་པ་སྦྱིན་པ་དང་སོ་སོའི་དགེ་འདུན་གྱི་གྲངས་ཀྱང་གསུངས་སོ། །

[Block 1974]
དགག་དབྱེར་གཏོགས་པའི་དགག་དབྱེའི་གཞི་ནི་དགེ་སློང་མའི་སོ་སོར་ཐར་པ་དང་། [^1733]དེའི་རྣམ་པར་འབྱེད་པ་དག་ལས་ཀྱང་ངོ་། །གསོ་སྦྱོང་དུ་གཏོགས་པའི་དགེ་སློང་མའི་སོ་སོར་ཐར་པ་དང་། དེའི་རྣམ་པར་འབྱེད་པ་དག་ལས་ཀྱང་ངོ་། །མི་སྡུག་པར༌[^1734]འགྲེང་བ་ནི་ཁ་སྐོང་བ་ཉིད་མ་ཡིན་ནོ་ཞེས༌[^1735]བྱ་བ་ལ། མི་སྡུག་པར་འགྲེང་བ་གང་ཡིན་པ་དེ་ནི་དགེ་འདུན་ཁ་སྐོང་བར་བྱེད་པ་པོ་མ་ཡིན་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1975]
གང་ལ་ལས་བྱ་བ་ཡང་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། དེ་ཉིད་ཀྱང་ཁང་སྐོང༌[^1736]བ་ཉིད་མ་ཡིན་ནོ། །

[Block 1976]
དེའི་ཕྱིར་འདུན་པ་དང་ཡོངས་སུ་དག་པའི་ཆོ་ག་ལས་མ་ཡིན་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི། གང་ཞིག་འདུན་པ་དང་ཡོངས་སུ་དག་པར་གཏོགས་པ་འབུལ་བར་བྱེད་པ་དང་། བརྗོད་པའི་ཆོ་ག་ཚོགས་པ་མི་མཐུན་པའི་དོན་དུ་རྗེས་སུ་གནང་བ་དེའི་དབང་གིས༌[^1737]ཁ་སྐོང་བ་ཉིད་དུ་མ་ཡིན་ནོ། །

[Block 1977]
དེ་འབུལ་བ་པོ་ལས་སྐྱེས་པར་མི་འགྱུར་བ་དེ་ལྟ་བས་ན། གསུམ་གྱིས་འདུན་པ་དང་ཡོངས་སུ་དག་པ་དག་བླངས་ནས་གསོ་སྦྱོང་དང་དགག་དབྱེ་དག་མི་བྱ་སྟེ། ལས་ཀྱི་འདུན་པ་གཞན་མ་བླངས་པར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1978]
དེ་གཉིས་དབུལ་བར༌[^1738]བྱ་བ་དག་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཁ་སྐོང་བ་ལ་འདུན་པ༌[^1739]ཡོངས་སུ་དག་པ་དེ་གཉིས་འོས་པ་ཉིད་མ་ཡིན་ཏེ། དགེ་འདུན་གྱི་ཁ་སྐོང་བར་བྱེད་པ་པོས་འདུན་པ་དང་ཡོངས་སུ་དག་པ་གཉིས་དབུལ་བར༌[^1740]བྱ་བ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1979]
དགག་དབྱེ་བྱེད་པ་ཉིད་དུ་མི་བསྐོའོ་ཞེས་བྱ་བ་ནི་ཁ་སྐོང་བར་བྱེད་པ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1980]
བསྙེན་པར་མ༌[^1741]རྫོགས་པ་དང་ཉམས་པ་དང་མཚམས་མེད་པ་བྱས་པ་དང་། སྡིག་པའི་ལྟ་བ་ཅན་དང་ས་གཞན་ན་གནས་པ་དང་། ཐ་དད་པར་གནས་པ་རྣམས་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དེ་དག་ཀྱང་ཁ་སྐོང་བ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དབང་དུ་བྱས་པའོ། །

[Block 1981]
དེ་ལ་ཉམས་པ་ཞེས་བྱ་བ་ནི་ཕམ་པའོ། །

[Block 1982]
འདི་ལ་བསྙེན་པར་མ་རྫོགས་པ་ཞེས་བྱ་བ༌[^1742]སྨོས་སོ། །

[Block 1983]
ཉམས་པ་ཞེས་བྱ་བ་སྨོས་པ་ཡང་མཚམས་མེད་པ་བྱས་པའི་ཚིག་གོ། །

[Block 1984]
གང་གི་ཕྱིར་མ་ཉམས་པར་འགྱུར་ལ་མཚམས་མེད་པ་བྱས་པ་པོར་ཡང་འགྱུར་བ་དེ་ནི་འདི་ལྟ་སྟེ། དེ་བཞིན་གཤེགས་པའི་དྲུང་དུ་ངན་སེམས་ཀྱིས་ཁྲག་འབྱིན་པ་དང་། དགེ་འདུན་གྱི་དབྱེན་ནོ། །

[Block 1985]
ལྟ་བའི་རྣམ་པ་དྲུག་ཅུ་རྩ་གཉིས་པོ་དག་ལས་གང་ཡང་རུང་བ་ལྟ་བ་མ་ཡིན་པར་གཏོགས་པ་དེ་ནི་སྡིག་པའི་ལྟ་བ་ཅན་ནོ། །

[Block 1986]
འདིས་ནི་ཐམས་ཅད་ལྟ་བ་མཐུན་པ་ཚུལ་ཁྲིམས་ཡོངས་སུ་དག་པ་འདུས་པ་འཁོད་པ་དག་གིས༌[^1743]གསོ་སྦྱོང་དང་། དགག་དབྱེ་དང་གསོལ་བ་དང་། གཉིས་དང་གསོལ་བ་དང་བཞིའི་ལས་བྱའོ་ཞེས་གསུངས་པ་དེ་བསྡུས་པ་ཡིན་ནོ། །

[Block 1987]
ས་གཞན་ན༌[^1744]གནས་པ་ཞེས་བྱ་བ་ནི་སྤོ་བ་ལ་སོགས་པ་ཆད་པ་ནི་ལས་བྱེད་པའོ། །

[Block 1988]
འདིས་ནི་བཞིའི་ཚོགས་ཀྱིས་ལས་བྱས་ཏེ། སྤོ་བ་བྱེད་པ་དང་ལས་བཞིས་བྱེད་པ་ཆོས་མ་ཡིན་པས་ལས་བྱེད་པ་ཡིན་ནོ། །

[Block 1989]
གཞི༌[^1745]ནས་སྤོ་བ་བྱེད་པ་དང་། མགུ་བ་སྤྱོད་པ་དང་གཞི་ནས་མགུ་བ་སྤྱོད་པ་སྤངས་པ༌[^1746]དང་བཞིས་བྱེད་ན་ཆོས་མ་ཡིན་པ་བྱེད་པ་ཡིན་ན༌[^1747]ཞེས་བསྡུས་པ་ཡིན་ནོ། །

[Block 1990]
འདིར་ཆོས་མ་ཡིན་པའི་ལས་བྱེད་པ་དཔེ་ཙམ་ཡིན་ཏེ། སྤོ་བ་བྱེད་པ་རྣམས་ལ་སྤངས་པའི་ཚིག་ཏུ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 1991]
སྤོ་བ་བྱེད་པ་ལ་སོགས་པ་སྨོས་པ་ནི་བསླབ་པ་བྱིན་པ་ཡང་བཟུང་བར་གྲུབ་སྟེ། བསླབ་པ་བྱིན་པ་ནི༌[^1748]ཆོས་དམན་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1992]
ཐ་དད་པར་གནས་པ༌[^1749]ཞེས་སྨོས་པ་ནི་འདིར་ཆོས་དང་མཐུན་པའི་ཕྱོགས་ཁས་བླངས་པ་ཡིན་པར་ཤེས་པར་བྱ་སྟེ། ཆོས་མ་ཡིན་པའི་ཕྱོགས་དང་མཐུན་པར་ཁས་བླངས་པའི་ཐ་དད་པར་གནས་པ་ནི་ཁོངས་སུ་བསྡུ་བ་བསྒྲུབ་པའི་དོན་དུ་ཆོས་མ་ཡིན་པའི་ཕྱོགས་དང་མཐུན་པར་ཁས་བླངས་པའི་ཐ་དད་པར་གནས་པ་ནི་སྡིག་པའི་ལྟ་བ་ཅན་ཞེས་སྨོས་པ་ཉིད་ཀྱིས་བསྡུས་པའི་ཕྱིར་རོ། །

[Block 1993]
འཁྲུལ་པ་དང་བཅས་པ་ཡང་ངོ་ཞེས་བྱ་བ་ཡང་། ཁ་སྐོང་བ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་རྗེས་སྙེགས༌[^1750]པའི་ཕྱིར་ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲས་སྨོས་ཏེ། ཐམས་ཅད་ཚུལ་ཁྲིམས་ཡོངས་སུ་དག་པ་ཞེས་གསུངས་པས་དེའི་ཕྱིར་མདོ་འདི་བྱས་སོ། །

[Block 1994]
འདི༌[^1751]ཚུལ་ཁྲིམས་ཡོངས་སུ་དག་པ་ནི་ལྟུང་བ༌[^1752]ཐམས་ཅད་ཡོངས་སུ་དག་པས་ཡོངས་སུ་དག་པ་ཡིན་གྱི༌[^1753]ཕམ་པར་འགྱུར་བ་ཉིད་ཙམ་གྱིས༌[^1754]ནི་མ་ཡིན་ནོ། །

[Block 1995]
རང་བཞིན་དུ་གནས་པ་མ་ཡིན་པ་དེ་ཉིད་ཀྱིས་ཁ་སྐོང་བར་འོས་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 1996]
འདིར་གཞུང་ནི་སིལ་བུ་དག་ལས།

[Block 1997]
བཙུན་པ། ཇི་ཙམ་གྱིས་རང་བཞིན་དུ་གནས་པ་མ་ལགས་པར་འགྱུར། ཉེ་བ༌[^1755]འཁོར་ཇི་ཙམ་གྱིས་ལྷག་པར་སྤྱད་པ་མ་ཡིན་པ་ལྷག་པར་སྤྱོད་ཅིང་དགེ་སློང་གི༌[^1756]བསླབ་པ་ལ་མི་བསླབ་པ་སྟེ། ཉེ་བ༌[^1757]འཁོར་དེ་ཙམ་གྱིས་རང་བཞིན་དུ་གནས་པ་མ་ཡིན་པར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1998]
འདིས་ནི་གང་ཡང་རུང་བས་འཁྲུལ་པར་གྱུར་ཅིང་དགེ་སློང་གི་རང་བཞིན་ལས་ཉམས་པར་འགྱུར་བ་ཉིད་ཅེས་བྱ་བའོ། །

[Block 1999]
དེ་ཉིད་ཀྱིས༌[^1758]རང་བཞིན་དུ་གནས་པ༌[^1759]ཡིན་པ་དེ་བསྟན་ཏོ། །

[Block 2000]
རང་བཞིན་དུ་གནས་པ་མ་ཡིན་པ་དེ་ཉིད་ཀྱིས་ནི་ཕྱིར་ཟློག་པར་འོས་པ་ཉིད་མ་ཡིན་པར་གསུངས་ཏེ། དེ་ལྟར་ཡང་འདིར་གཞུང་ནི། བཙུན་པ། གང་ཟག་དུ་དག་གིས༌[^1760]སླར་བཟློག་པ་མི་ཆགས། ཉེ་བ༌[^1761]འཁོར་བཅུ་གཉིས་ཏེ། བྱིས་པ་དང་རྨོངས་པ་མི་གསལ་བ་དང་། མི་མཁས་པ་དང་ངོ་ཚ་མེད་པ་དང་། ནད་དང་བཅས་པ་དང་། མཚམས་ཀྱི་ཕྱི་རོལ་ན་གནས་པ་དང་། གནས་ནས་ཕྱུང་བ་དང་ཚིག་ཡང་དག་པར་མ་བསྡམས་པ༌[^1762]དང་། སྤྱོད་ལམ་ལས་ཉམས་པ་དང་། རང་བཞིན་དུ་གནས་པ་མ་ཡིན་པ་དང་། བསླབ་པ་བྱིན་པས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །
--- END BLOCKS ---
