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
ལེགས་པར་བཤད་པ་ལ་རྟོག་པ་ཞེས་བྱ་བ་ནི་དེ་བཞིན་གཤེགས་པས་གསུངས་པ་ཐོག་མར་ཡང་དགེ་བར་དུ་ཡང་དགེ་ཐ་མར་ཡང་དགེ་བའི་ཆོས་བཤད་པ་རྟོག་པས་སྒྲིབ་པ་ལྔ་སྐྱེ་བའི་སྐབས་མེད་པར་བྱེད་པ་ནི་རྣམ་པར་སྤོང་པའོ། །

[Block 2032]
ངེས་པར་འབྱིན་པའི་ཆོས་ནི་འཕགས་པའི་ལམ་སྟེ། ཁམས་གསུམ་ནས་ངེས་པར་འབྱིན་པའི་ཕྱིར་རོ། །

[Block 2033]
དེ་བསྟི་སྟང༌[^1795]དུ་བྱས་ཏེ་ཉན་པ་ཉིད་ཀྱི་བསོད་ནམས་ཀྱི༌[^1796]ཚོགས་ཡིན་ནོ། །

[Block 2034]
དཀའ་ཐུབ་བསྒོམ་པའི་ནགས་ཚལ་ནི་བརྟུལ་ཞུགས་ཀྱི་ནགས་ཚལ་ལོ། །

[Block 2035]
བྱང་ཆུབ་ཀྱི་ཤིང་དྲུང་གི་རྒྱན་ནི་བྱང་ཆུབ་ཀྱི་ཤིང་དྲུང་དུ་མངོན་པར་བྱང་ཆུབ་པར་འགྱུར་བའི་རྒྱུ་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་སམ། མངོན་པར་བྱང་ཆུབ་པ་ཉིད་བྱང་ཆུབ་ཀྱི་ཤིང་གི་རྒྱན༌[^1797]ནོ། །

[Block 2036]
དགེ་བའི་རྩ་བ་ཐམས་ཅད་སྔོན་དུ་འགྲོ་བས་ཞེས་བྱ་བ་ནི་སངས་རྒྱས་པར་འགྱུར་བའི་དགེ་བ༌[^1798]བསགས་པས༌[^1799]བྱང་ཆུབ་ཀྱི་སྙིང་པོའི་རྒྱན་དུ་འགྱུར་བའོ། །

[Block 2037]
ལས་དང་ཉོན་མོངས་པ་ཐམས་ཅད་ཀྱིས་མི་གོས་ཞེས་བྱ་བ་ནི་ཁམས་གསུམ་དུ་སྐྱེས་ཀྱང་འཁོར་བའི་སྐྱོན་ལས་དང་ཉོན་མོངས་པས་མི་གོས་པར་འཁོར་བར༌[^1800]སྐྱེ་བ་འང་སྐྱོན་མེད་པ༌[^1801]ལ་འཁོར་བ་ནས་ཤི་འཕོས་པ་ཡང་སྐྱོན་མེད་པའོ། །

[Block 2038]
དེ་ལ་ཤི་བ་ནི་འདིར་ཚེའི་དབང་པོ་འགགས་པའོ། །

[Block 2039]
འཕོ་བ་ནི་འདི་ནས་སྲིད་པ་གཞན་དུ་སོང་བའོ། །

[Block 2040]
རིན་པོ་ཆེ་དང་ཕངས་པའི་དངོས་པོ་ཞེས་བྱ་བ་ནི་གསེར་དང་དངུལ༌[^1802]སོགས་པའི་རིན་པོ་ཆེ་དང་། བུ་དང་ཆུང་མ་ལ་སོགས་པ་ཕངས་པའི་དངོས་པོ་ཐམས་ཅད་ལ་མ་ཆགས་པར་གཏོང་བས༌[^1803]རིན་པོ་ཆེ་སྣ༌[^1804]བདུན་དང་ལྡན་པའི་འཁོར་ལོས་སྒྱུར་བའི་རྒྱལ་པོར་འགྱུར་བ་འམ། ལག་ན་རིན་པོ་ཆེ་ཐོབ་པར༌[^1805]འགྱུར་བའོ། །

[Block 2041]
གཏེར་མི་ཟད་པ་འབྱིན་པ་ནི་ཚེ་འདིར་རོ། །

[Block 2042]
ལོངས་སྤྱོད་མི་ཟད་པ་ནི་ཚེ་རབས་གཞན་དུ་མི་ཟད་པ་ཐོབ་པའོ། །

[Block 2043]
འོད་ཟེར་མཉམ་པར་གཏོང་བ་ནི་བྱམས་པ་དང་སྙིང་རྗེའི་བསམ་པས་སེམས་ཅན་ཀུན་ལ་མཉམ་པར་ལྟ་བའོ། །

[Block 2044]
མཉམ་པ་ཉིད་ཀྱི་རྒྱན༌[^1806]ཐོབ་པ་ནི་གང་ལ་ཡང་བྱམས་པ་དང་ཞེ་སྡང་མེད་པའི་སེམས་ཐོབ་པའོ། །

[Block 2045]
མ་ལོབས་པ་ནི་བསླབ་པ༌[^1807]མཐར་མ་ཕྱིན་པའོ། །

[Block 2046]
འོད་བཀོད་པ་གཏོང་བ་ནི་དེ་དག་ལ་སྤ་འགོང༌[^1808]བར་བྱེད་པ་མེད་པའོ། །

[Block 2047]
སྐྱེ་བ་ཡོངས་སུ་དག་ཅེས་བྱ་བ་ནི་ཚུལ་ཁྲིམས་དག་པའི་ཚོགས་དང་ལྡན་པས་སངས་རྒྱས་ཀྱི་ཞིང་དུ་སྐྱེ་བ་འམ། ངན་སོང་གསུམ་དུ༌[^1809]སྐྱེ་བ་འམ། སྡིག་པ་བྱེད་པའི་གནས་སུ་མི་སྐྱེ་བའོ། །

[Block 2048]
མངལ་གྱི་གནས་ཡོངས་སུ་དག་ཅེས་བྱ་བ་ནི་བདག་དང་གཞན་གྱི་ལྟུང་བ་ཆོས་བཞིན་དུ་གསོ་བར་བྱེད་ཀྱི་གླེང་བར་མི་བྱེད་པས་རྟག་ཏུ་རྫུས༌[^1810]ཏེ་སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 2049]
རྗེས་སུ་བསྟན་པ་ཐམས་ཅད་ལ་རྣམ་པར་མི་རྟོག་ཅེས་བྱ་བ་ནི་ཆོས་བསྟན་པ་ཐམས་ཅད་ལ་རྣམ་པར་མི་རྟོག་པའི་ཚུལ་དུ་གནས་པས་ལས་སུ་བྱས་པ་ཐམས་ཅད་དོན་ཡོད་དེ་ཆུད་ཟོས་པར་མ་གྱུར་པའོ། །

[Block 2050]
ཆོས་ཐམས་ཅད་ལ་དབང་ཞེས་བྱ་བ་ནི་ཆོས་ཐམས་ཅད་ཁོང་དུ་ཆུད་པའི་དབང་ཕྱུག་ཆེན་པོར་གྱུར་པའོ། །

[Block 2051]
བསམ་པ་ཡོངས་སུ་དག་པས་འཇིག་རྟེན་ཐམས་ཅད་ལ་དབང་བ་ཞེས་བྱ་བ་ནི་བསམ་པ་ཡོངས་སུ་དག་པས་ཇི་སྤྱད་དོ་ཅོག་ལ་གཡོ་སྒྱུ་མེད་པའི་ཕྱིར་འཇིག་རྟེན་ཐམས་ཅད་དེ་ལ་ཡིད་ཆེས་ཤིང་དེའི་དབང་དུ་འགྱུར་བའོ། །

[Block 2052]
སེམས་ཅན་ཡོངས་སུ་དག་པར་བྱེད་པས་རང་གི་སངས་རྒྱས་ཀྱི་ཞིང་ཡོངས་སུ་དག་པ་ཞེས་བྱ་བ་ནི་ཚེ་རབས་དེ་དང་དེ་དག་ཏུ་བདག་གིས་སྨིན་པར་བྱ་ཞིང་གདུལ་བར་བྱ་བའི་སེམས་ཅན་རྣམས་སྦྱིན་པ་དང་ཚུལ་ཁྲིམས་ལ་སོགས་པ་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་ལ་བཀོད་པ་དེ་དག་པར་བྱས་པས་ནམ་བདག་མངོན་པར་སངས་རྒྱས་པའི་སངས་རྒྱས་ཀྱི་ཞིང་ན་གནས་པའི་སེམས་ཅན་ཡང་སྦྱིན་པ་ལ་གནས་པ། ཚུལ་ཁྲིམས་ལ་གནས་པ་ཤ་སྟག་དང་ལྡན་པར་འགྱུར་བས་སངས་རྒྱས་ཀྱི་ཞིང་ཡོངས་སུ་དག་པའོ། །

[Block 2053]
ཁ་ཅིག་ལས་སེམས་ཅན༌[^1811]ཡོངས་སུ་དག་པ་ཞེས་འབྱུང་སྟེ་དེར་ཡང་སངས་རྒྱས་ཀྱི་ཞིང་གྱོ་མོ་དང་། བོང་བ་ལ་སོགས་པ་མེད་ཅིང་མཉམ་པར་སྣང་བ་ཡང་བདག་གི་སེམས་ཡོངས་སུ་སྦྱངས་ཏེ། དེ་ལྟ་བུ་སྣང་བ་མེད་པ་གོམས་པ་ལས་བྱུང་བའི་དོན་དུ་ལྟའོ། །

[Block 2054]
ལས་ཀྱི་རྣམ་པར་སྨིན་པ་ལ་སྟོན་པས་ལྷག་པའི་བསམ་པ་ཡོངས་སུ་དག་པ་ཞེས་བྱ་བ་ལ་སེམས་ཅན་ལ་གནོད་པ་མི་བྱེད་ཅིང་ཕན་པར་བྱེད་པའི་བསམ་པ་ནི་ལྷག་པའི་བསམ་པ་སྟེ། ལེགས་ཉེས་ཇི་འབྱུང༌[^1812]ཡང་བདག་གི་ལས་ཀྱི་རྣམ་པར་སྨིན་པ་ལས་བྱུང་བར་ཤེས་ན། ཕ་རོལ་པོ་ལ་བྱམས་པ་དང་། སྡང་བ་མེད་པའི་ཕྱིར་ལྷག་པའི་བསམ་པ་དག་པའོ། །

[Block 2055]
ཉི་ཚེ་བའི་སྤྱོད་པ་མི་འདོད་ཅེས་བྱ་བ་ནི་བདག་གི༌[^1813]དོན་དུ་ཞུགས་པ་ཉན་ཐོས་དང་རང་སངས་རྒྱས་ཀྱི་ཐེག་པའི་ལམ་ལ་གནས་པར་མི༌[^1814]མོས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2056]
སངས་རྒྱས་ཀྱི་ཆོས་རྒྱ་ཆེན་པོ་ལ་མོས་པ་ཞེས་བྱ་བ་ནི་ས་དང་ཕ་རོལ་ཏུ་ཕྱིན་པ་སྤྱོད་པ་ལ་མོས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2057]
ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཀྱི་སེམས་མི་གཏོང་ཞེས་བྱ་བ་ནི་འགྲོ་བ་མ་ལུས་པ་བསྐྱབ༌[^1815]པར་བྱ་བའི་བྱང་ཆུབ་ཀྱི་སེམས་མི་གཏོང་བས་བླ་ན་མེད་པའི༌[^1816]བྱང་ཆུབ་ཏུ་འཚང་རྒྱ་བའི་བསོད་ནམས་ཀྱི་ཚོགས་དང་ལྡན་པའོ། །

[Block 2058]
དད་པ་སྔོན་དུ་འགྲོ་བ༌[^1817]ཞེས་བྱ་བ༌[^1818]ནི་དད་པ་དང་ལྡན་ཏེ། དད་པས་རྒྱུ་བྱས་པས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2059]
ལུས་དང་སྲོག་ལ་མི་ལྟ་ཞེས་བྱ་བ་ནི་ལུས་དང་སྲོག༌[^1819]ལ་ཡང་མི་ཕངས་པར་སངས་རྒྱས་ཀྱི་ཆོས་བཙལ་བས་ན་སྟོབས་དང་མི་འཇིགས་པ༌[^1820]ལ་སོགས་པ་སངས་རྒྱས་ཀྱི་ཆོས་ཐམས་ཅད་དང་ལྡན་པའོ། །

[Block 2060]
སྔོན་དམ་བཅས་པ་ཉམས་འོག་ཏུ་ཆུད་པར་བྱེད་པ་ཞེས་བྱ་བ་ནི་དང་པོ་བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་པའི༌[^1821]ཚེ་སེམས་ཅན་ཐམས་ཅད་བླ་ན་མེད་པའི་བྱང་ཆུབ་ཏུ་བསྒྲལ་ལོ་ཞེས་ཁས་བླངས་པ་དེ་བཞིན་དུ་མངོན་པར་བྱང་ཆུབ་པ་ནི་སེམས་ཅན་ཐམས་ཅད་བསྒྲལ་བས་འཇིག་རྟེན་ཐམས་ཅད་ལ་མི་བསླུ་བའོ། །

[Block 2061]
དགེ་བའི་ཆོས་ཐམས་ཅད་ཡོངས་སུ་རྫོགས་པར་བྱེད་པ་ཞེས་བྱ་བ་ནི་སངས་རྒྱས་ཀྱི་ཆོས་ཐམས་ཅད་རྫོགས་པར་བྱེད་པ་འམ། མཐར་འབྱིན་པར་བྱེད་པའི་རྒྱུ་དགེ་བའི་ཆོས་བསོད་ནམས་ཡིན་ཏེ། [^1822]བསོད་ནམས་དང་ལྡན་ན༌[^1823]ས་དང་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སོགས་པའི་ཆོས་རྣམས་རྫོགས་པར་འགྱུར་བས་སངས་རྒྱས་ཀྱི་ཆོས་ཐམས་ཅད་རྫོགས་པར་འགྱུར་བ་ཞེས་བྱའོ། །

[Block 2062]
བསོད་ནམས་ཀྱི་ཚོགས་རྒྱ་ཆེར་བཤད་པའི་དོན་བསྡུས་ཏེ་བསྟན་པའི་ཕྱིར། དེ་ལྟར་རྒྱུ་གང་དང་རྐྱེན་གང་གིས་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། དེ་ལྟར་ནི་གོང་དུ་བཤད་པ་ལྟར་རོ། །

[Block 2063]
མདོར་ན་དགེ་བའི་རྩ་བའི་རྒྱུ་གང་དང་གང་གིས་ས་དང་ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་མཚན་དང་དཔེ་བྱད་དང་། སྟོབས་དང་མི་འཇིགས་པ་དང་། སྐུ་ལ་སོགས་པ་ཐོབ་པར་བྱེད་པའི་རྒྱུ་དེ་དང་དེ་དག་བསྒྲུབ་པའི༌[^1824]བསོད་ནམས་ཀྱི་ཚོགས་མི་ཟད་པ་ཞེས་བྱའོ། །

[Block 2064]
རྒྱ་ཆེར་ནི་བསྐལ་པ་ཞེས་བྱ་བ་ལ་བསོད་ནམས་ཀྱི་ཚོགས་ཞིབ་ཏུ་བསྟན་ཅིང་མ་ལུས་པར་བསྟན་ན་ནི། བསྐལ་པ་འམ་བསྐལ་པ་བས་ལྷག་པར་ཡང་བཤད་དགོས་ལ་དེས་ཀྱང་རྫོགས་པར་མི་ནུས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2065]
བསོད་ནམས་ཀྱི་ཚོགས་མི་ཟད་པ་བཤད་ཟིན་ཏོ།། །།

[Block 2066]
[^1825]

[Block 2067 [HEADING]]
### ཡེ་ཤེས་ཀྱི་ཚོགས་མི་ཟད་པ། ^7-2-0

[Block 2068]
ཐེ་ཚོམ་ཐམས་ཅད་གཅོད་པའི་དབང་དུ་བྱས་ནས། དེ་ལ་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ཡེ་ཤེས་ཀྱི་ཚོགས་མི་ཟད་པ་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2069]
ཡེ་ཤེས་རྟོགས་པར༌[^1826]འགྱུར་ཞེས་བྱ་བ་ནི་གཉིས་སུ་མེད་པའི་ཡེ་ཤེས་ཁོང་དུ་ཆུད་ཅིང་མངོན་སུམ་དུ་འགྱུར་བའོ། །

[Block 2070]
དེ་ལ་ཡེ་ཤེས་ཡོངས་སུ་ཚོལ་བ་ལ་འདུན་པ་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། ཕྱི་རོལ་མ་ཡིན་པའི་ཆོས་སྟོན་ཏོ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་རྒྱུ་བསྟན་ཏོ། །
--- END BLOCKS ---
