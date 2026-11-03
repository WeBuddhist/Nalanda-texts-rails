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
[Block 2031]
ཡང་ན་ལྷག་མ་དང་བཅས་པའི་མྱ་ངན་ལས་འདས་པ་ཐོབ་ཏུ་ཟིན་གྱིས་ཀྱང་ལྷག་མ་མ་ལུས་པའི་མྱ་ངན་ལས་འདས་པ་མ་ཐོབ་པའི་ཕྱིར་སྦྱིན་པར་བྱས་པ་དེ་བླངས་སོ། །

[Block 2032 [HEADING]]
###### **ཕས་ཀུན་ལ་འདྲ་བར་བྱིན་པ།** ^4-3-5-4-1-1-2-2-0

[Block 2033]
མདོ་ལས་དེ་ནས་ཤཱ་རིའི་བུ་སྐྱེས་བུ་དེས་ཞེས་པ་ནས་བདག་གི་བུ་རྣམས་ལ་རླུང་ལྟར་མགྱོགས་ཤིང་མཐུ་དང་ལྡན་པའི་གླང་པོ་ཆེའི་ཤིང་རྟ་བྱིན་ཏེ་ཞེས་པའི་བར་དུ་ནི་ཕས་ཀུན་ལ་འདྲ་བར་བྱིན་པ་བསྟན་ཏེ་དེ་ཡང་ཤིང་རྟ་བྱིན་པ་དང་། དེའི་རྒྱན་དང་གླང་དེའི་མཚན་དང་དེའི་འཁོར་བསྟན་པ་ལ་འདི་ནི་དང་པོའོ། །

[Block 2034 [HEADING]]
###### **ཤིང་རྟ་བྱིན་པ།** ^4-3-5-4-1-1-2-2-1-0

[Block 2035]
གླང་པོ་ཆེའི་ཤིང་རྟ་ནི་ཐེག་པ་ཆེན་པོའི་འབྲས་བུ་བསྟན་ཏེ་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་ཀྱི་རང་བཞིན་ཅན་ནམ༌[^1687]ཡེ་ཤེས་བཞི་དང་ལྔའི་དངོས་པོའོ། །

[Block 2036]
མདོ༌[^1688]ལས་ཀྱང་དེ་བཞིན་ཉིད་ཀྱི་ངོ་བོ་ནི་དཔེས་ཤིང་རྟ་བཞིན་ནོ་ཞེས་འབྱུང་བ་ལྟ་བུ་སྟེ། གླང་དེ་ཡང་རླུང་བཞིན་དུ་མགྱོགས༌[^1689]པའི་དཔེས་ཐེག་པ་ཆེན་པོ་འདི་ལ་གནས་པས༌[^1690]ཕྱིར་མི་ལྡོག་པའི་ས་ལ་མྱུར་དུ་སོན་པར་བྱེད་པའི་ཕྱིར་མགྱོགས་པར༌[^1691]བསྟན་ཏོ། །

[Block 2037]
དེ་བཞིན་གཤེགས་པས་ཆོས་སྟོན་པ་ཡང་སེམས་ཅན་ལ་དབྱེ་བ་དང་རིམ་པ་མི་མཛད་མོད་ཀྱི་སོ་སོའི་སྣོད་ཇི་བཞིན་པ་ལས་མྱ་ངན་ལས་འདའ་བ་ཐོབ་པའང་ཁྱིམ་བདག་དེས་བུ་རྣམས་ལ་འདྲ་བར་གླང་པོ་ཆེའི་ཤིང་རྟ་བྱིན་པའི་དཔེ་བསྟན་ཏོ། །

[Block 2038 [HEADING]]
###### **ཤིང་རྟ་དེའི་རྒྱན།** ^4-3-5-4-1-1-2-2-2-0

[Block 2039]
མདོ་ལས་རིན་པོ་ཆེ་བདུན་ལས་བྱས་པ་ལོགས་དང་ལྡན་པ་དྲིལ་བུ་མང་པོས་རབ་ཏུ་དཔྱངས་པ༌[^1692]མཐོ་ཞིང་བརྟན་པ་ཞེས་པ་ནི་ཤིང་རྟ་དེའི་རྒྱན་བསྟན་ཏེ། དེ་ལ་ཡང་རྣམ་པ་བཅུ་ཡོད་པ་ལ་འདིར་བཞི་ཞིག་སྟོན་ཏེ། དེའི་ཚད་དང་རྒྱན༌[^1693]དང་ཁ་ལོ༌[^1694]སྒྱུར་བ་དང་འཕྱང་བ་མང་པོ་སྟོན་ཏོ། །

[Block 2040]
མཐོ་ཞིང་བརྟན་པ༌[^1695]ནི་ཚད་དེ་དེ་བཞིན་གཤེགས་པའི་ཡེ་ཤེས་ཀྱི་དཔེ་སྟེ། ཕྱོགས་ཐམས་ཅད་དུ་གཟིགས་ཤིང་འཕགས་པར་གྱུར་ཅེས་པའི་དོན་ཏོ། །

[Block 2041]
རིན་པོ་ཆེ་མང་པོ་ནི་དེའི་རྒྱན་ཏེ་ཡོན་ཏན་ཐམས་ཅད་ཀྱིས༌[^1696]བརྒྱན་པར་བྱ་བ་ནི་བཅོམ་ལྡན་འདས་ཀྱི་ཡེ་ཤེས་ཉིད་དོ། །

[Block 2042]
ལོགས་དང་ལྡན་པ་ཞེས་པ་ནི་ཁ་ལོ་སྒྱུར་བ་དང་ལྡན་པ་སྟེ་གཟུངས་རྣམ་བཞིས་བརྟན་ཞེས་པའི་དོན་ཏོ། །

[Block 2043]
དྲིལ་བུ༌[^1697]རབ་ཏུ་དབྱངས༌[^1698]ཞེས་པ་ནི་སྦྱང་པར་བྱ་བའི་རྒྱན་ཏེ་སྤོབས་པ་རྣམ་པ༌[^1699]བདུན་ལ་སོགས་པས་སྤོབས༌[^1700]པའི་རྒྱན་ཞེས་པའི་དོན་ཏེ།[^1701] །མདོ་ལས་རིན་པོ་ཆེ་ངོ་མཚར་རྨད་དུ་བྱུང་བའི་རྒྱན་གྱིས་བརྒྱན་ཞེས་པ་ནི་རྒྱན་དེ་ནི་གདུགས་ཀྱིས་འགེབས་པའི་རྒྱན་ཏེ། འགྲོ་བ་མང་པོ་ལ་ཚད་མེད་པ་བཞིའི་གདུགས་ཀྱིས་འགེབས་ཞེས་པའི་དོན་ཏོ། །

[Block 2044]
མདོ་ལས་རིན་པོ་ཆེའི་ཕྲེང་བས་མཛེས་པར་བརྒྱན་པ་ཞེས་པ་ནས་རྟེན་པ་དམར་བ་གཉིས་སུ་བཞག་པ་ཞེས་པའི་བར་དུ་ནི་འདི་ལ་རྒྱན༌[^1702]བཞི་སྟེ། ཕྲེང་བ་དང་མེ་ཏོག་དང་གདིང་བ་དང་རྒྱབ་རྟེན་དང་བཞི་ལ་ཕྲེང་བ་ནི་སྨོན་ལམ་རྒྱ་ཆེན་པོ་བཞིའི་དོན་ཏེ། བཞིའི༌[^1703]ནི་བྱང་ཆུབ་སེམས་དཔའ༌[^1704]དགེ་བ་ཅི་བརྩམས་པ་རྣམས་སེམས་ཅན་ཐམས་ཅད་ལ་བསྔོ་སྟེ། སེམས་ཅན་སྡུག་བསྔལ༌[^1705]ལས་ཐར་བར་གྱུར་ཅིག །བདེ་བ་མ་ཐོབ་པ་རྣམས་བདེ༌[^1706]དང་ལྡན་པར་ཤོག་ཤིག །[^1707]སྡིག་པ་སྤོང༌[^1708]དགེ་བ་ལ་འཇུག་པའི་བྱང་ཆུབ་ཀྱི་སེམས་མ་བསྐྱེད་པ༌[^1709]རྣམས་སེམས་དེ་བསྐྱེད་པར༌[^1710]གྱུར་ཅིག །བླ་ན་མེད་པའི་བྱང་ཆུབ་ཀྱི་འབྲས་བུ་མ་ཐོབ་པ་རྣམས་ཐོབ་པར་གྱུར་ཅིག་ཅེས་སྨོན་ལམ་འདེབས་པའོ། །

[Block 2045]
རིན་པོ་ཆེའི་མེ་ཏོག་གི་ཕྲེང་བ་ཞེས་པ་ནི་བསྡུ་བ་རྣམ་བཞིའི་དོན་ཏེ། སྦྱིན་པ་དང་ཚིག་སྙན་པ་དང་ཕན་པར་སྤྱོད་པ་དང་དོན་མཐུན་པའོ། །

[Block 2046]
གདིང་བ་ནི་ཡང་དག་པའི་འཚོ་བ་སྟེ་རྒྱུ་དང་ལོག་པར་སྤྱོད་པ་སྒོ་གསུམ་ནས་མི་རྒྱུ་ཞེས་པའི་དོན་ཏོ། །

[Block 2047]
རྟེན་དམར་པོ་ཞེས་པ་ནི་མྱ་ངན་ལས་འདའ་བའི་བདེ་བ་ལ་བརྟེན་ནས་ཞེས་པའི་དོན་ཏེ། ཟག་པ་མེད་པའི་འགོག་པ་ལ་གནས་ཤིང་འཕགས་པའི་ལམ་འཕེལ་བར་བྱེད་པའི་དོན་ཏམ། དད་པའི་དབང་པོ་ལ་སོགས་པ་དབང་པོ་ལྔས་བརྟེན་ཞེས་པའི་དོན་ཏོ། །

[Block 2048 [HEADING]]
###### **གླང་དེའི་མཚན།** ^4-3-5-4-1-1-2-2-3-0

[Block 2049]
མདོ་ལས་གླང་དཀར་པོ་རབ་ཏུ་དཀར་ཞིང་ཞེས་པ་ནས་བྱིས་པ་རྣམས་ལ་རེ་རེ་བྱིན་ཏེ་ཞེས་པའི་བར་དུ་ནི་གླང་དཀར་པོ༌[^1711]རྩ་བའི་ཡེ་ཤེས་དང་སྦྱར་རོ། །

[Block 2050]
གླང་ཞེས་པ་ནི་ཤིང་རྟ་འདྲེན་པའི་དོན་ཏེ།[^1712] འགྲོ་བ་མང་པོ་འདྲེན་པའོ། །

[Block 2051]
དཀར་པོ་ཞེས་པ་ནི་ཁ་དོག་ཐམས་ཅད་ཀྱི་གཞི་སྟེ་པདྨོ་དཀར་པོ་དང་འདྲའོ། །

[Block 2052]
ཡང་གླང་དེ་ལ་ཡོན་ཏན་རྣམ་པ་གསུམ་སྟེ། དགྲ་འདུལ་བའི་དོན་ཏེ་སྒྲིབ་པ་རྣམ་གཉིས་འཇོམས་པའོ། །

[Block 2053]
མཛེས་པའི་དོན་ཏེ་འཕགས་པའི་ཡོན་ཏན་ཐམས་ཅད་ཀྱིས་བརྒྱན་པའོ། །

[Block 2054]
འདེགས་པའི་དོན་ཏེ་བདག་དང་གཞན་དགྲོལ་བའོ། །

[Block 2055]
ཡང་ན་གླང་གིས༌[^1713]དྲང་བའི་ཤིང་རྟ་ནི་ར་དང་རི་དྭགས་ཀྱིས་དྲང་བའི་ཤིང་རྟ་ལས་ཁྱད་པར་དུ་བསྟན་ཏེ་ཐེག་པ་ཆེན་པོ་འདི་ཡང་ཐེག་པ་རྣམ་པ༌[^1714]གཉིས་ལས་འཕགས་ཞེས་པའི་དོན་ཏོ། །

[Block 2056]
སྟོབས་དང་ལྡན་པ་ཞེས་པ་ནི་ཡང་དག་པའི་ཡེ་ཤེས་ཏེ། ནང་གི་ཡོན་ཏན་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 2057]
ཁ་དོག་དཀར་བ་ཞེས་པ་ནི་སྒྲིབ་པ་ཐམས་ཅད་བསལ་ཏེ་ཚུལ་ཁྲིམས་ཀྱི་ཡོན་ཏན་དང་ལྡན་པ་བསྟན་ཏོ། །

[Block 2058]
ཡང་མཛེས་པ་ཞེས་པ་ནི་མཚན་དང་དཔེ་བྱད་བཟང་པོས་བརྒྱན་པས་ལྷ་དང་མིས་མཆོད་པར་འོས་པ་བསྟན་ཏོ། །

[Block 2059]
ཡང་སྟོབས་དང་ལྡན་པ་ནི་མངའ་བ༌[^1715]ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏེ། རྣམ་པ་ཐམས་ཅད་ཀྱིས་མི་བསྙེངས་ཞེས་པའི་དོན་ཏོ། །

[Block 2060]
རླུང་བཞིན་དུ་མགྱོགས་པ་ཞེས་པ་ནི་ཐུགས་རྗེས་སེམས་ཅན་འདྲེན་པ་དང་ཡོད་པ་དང་མེད་པའི་ཆོས་གཟིགས་པ་ལ་ཐོགས་པ་མེད་པར་འཇུག་པའི་དོན་ཏེ།

[Block 2061 [HEADING]]
###### **ཕ་དེའི་བསམ་པ།** ^4-3-5-4-1-1-2-3-0

[Block 2062]
མདོ་ལས་ཤཱ་རིའི་བུ་དེ་ཅིའི་ཕྱིར་ཞེ་ན་ཞེས་པ་ནས་དེས་འདི་སྙམ་དུ་བསམས་སོ་ཞེས་པའི་བར་དུ་ནི་ཕ་དེའི་བསམ་པ་བསྟན་ཏེ། བང་མཛོད་དང་ནོར་མང་པོ་དག་ནི་འདུས་བྱས་དང་འདུས་མ་བྱས་པའི་ཡོན་ཏན་ནོ། །

[Block 2063]
བང་མཛོད་ཅེས་པ་ནི་སྡེ་སྣོད་གཉིས་དང་གསུམ་དུ་ལྡན་པའོ། །

[Block 2064]
མདོ་ལས་བདག་གིས་བྱིས་པ་འདི་རྣམས་བཞོན་པ༌[^1716]ངན་པ་བྱིན་ཏེ་ཅི་ཞིག་བྱ་སྙམ་ཞེས་པ་ནས་འདི་དག་ཐམས་ཅད་ལ་སྙོམས་པར་བསམ་གྱི་མི༌[^1717]སྙོམས་པར་མི་བྱའོ་ཞེས་པའི་བར་དུ་ནི་བྱང་ཆུབ་ཏུ་སེམས་མ་བསྐྱེད་པ་ཕྱིར་བུས་པ་ཞེས་གདགས་སོ། །

[Block 2065]
ཐེག་པ་ཆེན་པོ་ལ་ཞུགས་པའི་ཕྱིར་ངའི་བུར་འདྲའོ་ཞེས་སྨས་སོ། །

[Block 2066]
ཐུགས་རྗེས་དགོངས་པ་གཉིས་སུ་མི་མཛད་པའི་ཕྱིར་སྙོམས་པའོ། །

[Block 2067]
མདོ་ལས་བདག་ཀྱང་བང་མཛོད་མང་གི་ཞེས་པ་ནས་བདག་གི་བུ་རྣམས་ལྟ་ཅི་སྨོས་ཞེས་པའི་བར་དུ་ནི་བཅོམ་ལྡན་འདས་ཐུགས་རྗེ་ཆེན་པོ་དང་ལྡན་པས་འགྲོ་བ་ལྔར་སྐྱེས་པའི༌[^1718]སེམས་ཅན་ཐམས་ཅད་དང་རིགས་མེད་པ་དང་རིགས་ངེས་པ་རྣམས་ལ་ཡང་སྙོམས་པར་སྟོན་ན་ཐེག་པ་ཆེན་པོའི་རིགས་ཅན་དང་རིགས་མ་ངེས་པ་རྣམས་ལ་ལྟ་ཅི་སྨོས་ཞེས་པའི་དོན་ཏོ། །

[Block 2068 [HEADING]]
###### **བུས་པ་རྣམས་ཀྱི་བསམ་པ་དང་འགལ་བ།** ^4-3-5-4-1-1-2-4-0

[Block 2069]
མདོ་ལས་དེའི་ཚེ་བྱིས་པ་དེ་དག་ཀྱང་ཞེས་པ་ནས་དེ་ཇི་སྙམ་དུ་སེམས་ཞེས་པའི་བར་དུ་ནི་བུ་རྣམས་ཀྱིས༌[^1719]སྔར་བསམ་པའི་རེ་བ་ལས་འགལ་བ་བསྟན་ཏེ། སྔར་ཐེག་པ་རྣམ་གསུམ་བསྟན་ལ་ཕྱིས་ཐེག་པ་ཆེན་པོ་འབའ་ཞིག་བསྟན་པས། འགལ་ཞེས་པའི་དོན་ཏོ། །

[Block 2070 [HEADING]]
###### **ཐེ་ཚོམ་དགྲོལ་བའི་དཔེ།** ^4-3-5-4-1-1-3-0
--- END BLOCKS ---
