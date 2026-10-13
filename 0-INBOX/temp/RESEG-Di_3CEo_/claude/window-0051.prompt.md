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
དེ་ལ་ཡང་།

[Block 1787 [VERSE]]
སེམས་པ་ཡིད་ཀྱི་ལས་ཡིན་ནོ། །
དེས་བསྐྱེད་ལུས་དང་ངག་གི་ལས། །
སེམས་པས་བསྐྱེད་པ་གང་ཡིན་པ། །

[Block 1788]
བསམས་པའི་ལས་ཞེས་གསུངས་པ་གང་ཡིན་པ་དེ་དག་ནི་ལུས་དང་ངག་གི་ལས་སུ་རིག་པར་བྱའོ། །

[Block 1789]
དེ་དག་རྣམ༌[^676]རིག་རྣམ༌[^677]རིག་མིན། །དེ་དག་ཀྱང་རྣམ་པར་རིག་བྱེད་དང་། རྣམ་པར་རིག་བྱེད་མ་ཡིན་པའི་རང་བཞིན་ནོ། །

[Block 1790 [HEADING]]
#### ལུས་རྣམ་རིག་བྱེད། ^4-1-1-0

[Block 1791]
དེ་ལ། ལུས་རྣམ༌[^678]རིག་བྱེད་དབྱིབས་སུ་འདོད། །སེམས་ཀྱི་དབང་གིས༌[^679]ལུས་དེ་ལྟར་གནས་པ་ནི་ལུས་ཀྱི་རྣམ་པར་རིག་བྱེད་ཡིན་ནོ། །

[Block 1792]
འགྲོ་བ་ཞེས༌[^680]ཁ་ཅིག་གི་སྟེ། དེ་བརྗོད་པ། འགྲོ་མིན་གང་ཕྱིར་འདུས་བྱས་ནི། །སྐད་ཅིག་པ་ཡིན། འདུས་བྱས༌[^681]ཐམས་ཅད་ནི་སྐད་ཅིག་ལས་ཕན་ཆད་དུ་མེད་པའི་ཕྱིར་དེ་ནི་ཡུལ་གཞན་དུ་འཕོ་བ་ནི་མི་རིགས་ཏེ། དེ་ལྟ་བས་ན་འགྲོ་བ་མ་ཡིན་ནོ། །

[Block 1793]
སྐད་ཅིག་མར་ཤེས་པར་བྱ་སྟེ། འདུས་བྱས་ནི་གདོན་མི་ཟ་བར་འཇིག་ཕྱིར་རོ། །

[Block 1794]
དངོས་པོ་རྣམས་འཇིག་པ་ནི་རྒྱུ་མེད་པ་ལས་འབྱུང་བ་ཡིན་ནོ། །

[Block 1795]
དེ་ཡང་གལ་ཏེ་སྐྱེས་པ་ཙམ་ལ་མ་ཡིན་ན་ཕྱིས་ཀྱང་མི་འབྱུང་བར་འགྱུར་རོ། །

[Block 1796]
དེ་ཡང་མཐོང་སྟེ་གལ་ཏེ་འཇིག་པ་རྒྱུ་དང་ལྡན་པ་ཞིག་ཏུ་གྱུར་ན། བློ་དང་སྒྲ་དང་མེ་ལྕེ་དག་འཇིག་པ་མེད་པ་ལས་འབྱུང་བ་ཡང་མཐོང་བས་འདི་རྒྱུ་ལ་ལྟོས་པ༌[^682]མ་ཡིན་ནོ། །

[Block 1797]
ཡང་གང་ཞིག་གཟུགས་ལ་སོགས་པ་མེ་དང་འབྲེལ་པས་འཇིག་པར་འདོད་པ་དེ་དག་གི་ལན་ཡང་འདི་ཡིན་ཏེ། རྒྱུ་མེད་པ་ལས་འགའ་མི་འབྱུང་། །གཞན་ཡང་། རྒྱུ་ཡང་འཇིག་པ་པོར་འགྱུར་རོ། །

[Block 1798]
མེ་དང་འབྲེལ་པ་གང་ལས་ཚོས་བྱེད་ལས་སྐྱེ་བ་འབྱུང་བ་དེ་ཉིད་དེ༌[^683]དང་འདྲ་བར་ཚོས་པ་དང་། ཆེས་ཚོས་པ་དང་། ཆེས་ཆེར་ཚོས་པ་བྱུང་ན་དེ་དག་འཇིག་པས་རྒྱུ་དེ་དག་གི་འཇིག་པ་པོར་འགྱུར་བའམ། ཡང་ན་བྱེ་བྲག་མེད་པར་འགྱུར་རོ། །

[Block 1799]
དེ་ཡང་རིགས་པ་མ་ཡིན་ཏེ། དེའི་ཕྱིར་འགྲོ་བ་མེད་ན་ལུས་ཀྱི་རྣམ་པར་རིག་བྱེད་དབྱིབས་ཡིན་ནོ་ཞེས་བྱ་བར་གྲུབ་པོ། །མདོ་སྡེ་པ་རྣམས་ན་རེ་དབྱིབས་ནི་རྫས་སུ་མེད་དེ། གལ་ཏེ་ཡོད་ན་ནི། གཉིས་གཟུང་འགྱུར། མིག་གིས་མཐོང་ན་ཡང་རིང་པོའོ་སྙམ་དུ་ཤེས་པར་འགྱུར་ལ། ལུས་ཀྱིས་རེག་ནའང་ཤེས་པར་འགྱུར་བས་གཟུགས་ཀྱི་སྐྱེ་མཆེད་ལ་ནི་གཉིས་ཀྱིས་འཛིན་པ་མེད་དོ། །

[Block 1800]
གང་ཡང་ཐོགས་པ་དང་བཅས་པའི་གཟུགས་ཅུང་ཟད་ཡོད་པ་དེ་ནི་གདོན་མི་ཟ་བར་རྡུལ་ཕྲ་རབ་ལ་ཡོད་པ་ཡིན་ན། དེ་རྡུལ་ལ་མེད། རིང་པོ་ལ་སོགས་པའི་དབྱིབས་ནི་རྡུལ་ཕྲ་རབ་ལ་མེད་དོ། །

[Block 1801]
དེ་ལྟ་བས་ན་མང་པོ་གནས་པ་ཁོ་ན་ལ་རིང་པོ་ལ་སོགས་པར་འདོགས་པར་ཟད་དོ། །

[Block 1802]
བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ། དབྱིབས་ཀྱང་རྫས་ཁོ་ན་ཡིན་ལ། ལུས་ཀྱི་རྣམ་པར་རིག་བྱེད་ཀྱང་དབྱིབས་ཀྱི་བདག་ཉིད་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 1803 [HEADING]]
#### ངག་རྣམ་རིག་བྱེད། ^4-1-2-0

[Block 1804]
ངག་རྣམ༌[^684]རིག་བྱེད་ནི་ངག་སྒྲ། །ངག་གི་རང་བཞིན་གྱི་སྒྲ་གང་ཡིན་པ་དེ་ཉིད༌[^685]ངག་གི་རྣམ་པར་རིག་བྱེད་ཡིན་ནོ། །

[Block 1805 [HEADING]]
#### རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ། ^4-1-3-0

[Block 1806]
རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་ནི་སྔར་བཤད་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 1807]
མདོ་སྡེ་པ་རྣམས་ན་རེ། དེ་ཡང་རྫས་སུ་མེད་དེ། ཁས་བླངས་ནས་མི་བྱེད་པ་ཙམ་གྱི་ཕྱིར་རོ། །

[Block 1808]
བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ་ཡོད་དོ་ཞེས་ཟེར་རོ། །ཇི་ལྟར་ཤེས་ཤེ་ན།

[Block 1809 [VERSE]]
རྣམ་གསུམ་དྲི་མེད་གཟུགས་གསུངས་དང་། །
འཕེལ་དང་མ་བྱས་ལམ་སོགས་ཕྱིར། །

[Block 1810]
བཅོམ་ལྡན་འདས་ཀྱིས་གཟུགས་ནི་རྣམ་པ་གསུམ་དུ་གསུངས་ཏེ། བསྟན་དུ་ཡོད་ལ་ཐོགས་པ་དང་བཅས་པ་དང་། བསྟན་དུ་མེད་ལ་ཐོགས་པ་དང་བཅས་པ་དང་། བསྟན་དུ་ཡང་མེད་ལ་ཐོགས་པ་ཡང་མེད་པའོ་ཞེས་སོ། །

[Block 1811]
ཟག་པ་མེད་པའི་གཟུགས་ཀྱང་གསུངས་ཏེ། གཟུགས་གང་ལ་རྗེས་སུ་ཆགས་པ་འམ། ཁོང་ཁྲོ་བ༌[^686]མི་སྐྱེ་བ་ཞེས་བྱ་བ༌[^687]དཔག་ཏུ་མེད་པའོ། །

[Block 1812]
རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་མ་གཏོགས་པ་ནི་བསྟན་དུ་ཡང་མེད་ལ། ཐོགས་པ་ཡང་མེད་པའི་གཟུགས་ཀྱང་མེད་ལ། ཟག་པ་མེད་པ་ཡང་མེད་དོ། །

[Block 1813]
འཕེལ་བར་ཡང་གསུངས་ཏེ། རྫས་ལས་བྱུང་བའི་དངོས་པོ༌[^688]འདི་དག་དང་ལྡན་པ་ནི་རྟག་ཏུ་རྒྱུན་མི་འཆད་པར་བསོད་ནམས་མངོན་པར་འཕེལ་བ༌[^689]ཁོ་ནར་འགྱུར་རོ། །

[Block 1814]
རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་མ་གཏོགས་པ་ནི་ཡིད་གཞན་དང་ལྡན་པའི་བསོད་ནམས་ཀྱང་མངོན་པར་འཕེལ་བར་མི་རུང་ངོ་། །རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་མེད་ན་བདག་ཉིད་ཀྱིས་མ་བྱས་ལ་གཞན་བྱེད་དུ་བཅུག་པའི་ལས་ཀྱི་ལམ་དག་ཀྱང་འགྲུབ་པར་མི་འགྱུར་རོ། །

[Block 1815]
རྣམ་པར་རིག་བྱེད་མ་ཡིན་པའི་གཟུགས་མེད་ན་ལམ་ཡན་ལག་བརྒྱད་པར་མི་འགྱུར་ལ། སོ་སོར་ཐར་པའི་སྡོམ་པ་ཡང་མེད་པར་འགྱུར་ཏེ། ཡང་དག་པར་བླངས་པའི་འོག་ཏུ་གང་གིས་ན་ཡིད་གཞན་དང་ལྡན་པ་འདི་ཡང་དགེ༌[^690]སློང་དུ་འགྱུར་བ་དེ་ནི་མེད་དོ། །

[Block 1816]
དེ་བས་ན་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་དེ་ནི་ཡོད་པ་ཁོ་ནའོ། །

[Block 1817]
ཡང་ཅི་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་ཡོད་པ༌[^691]དེའི་ཚེ་ཡོད་པའི་འབྱུང་བ་ཆེན་པོ་དག་ཁོ་ན་རྒྱུར་བྱས་ནས་འབྱུང་ངམ་ཞེ་ན། མ་ཡིན་ཏེ། རྟག་ཏུ་བ༌[^692]འདི་ལྟ་སྟེ།

[Block 1818 [VERSE]]
འདོད་རྟོགས་རྣམ་རིག་མིན་སྐད་ཅིག །
ཕྱིན་ཆད་འདས་པའི་འབྱུང་ལས་སྐྱེས། །

[Block 1819]
འདོད་པ་ན་སྤྱོད་པའི་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་ནི་སྐད་ཅིག་མ་དང་པོ༌[^693]ཕྱིན་ཆད་འདས་པའི་འབྱུང་བ་རྒྱུར་བྱས་ནས་སྐྱེའོ། །

[Block 1820]
དེ་དག་ནི་འདིའི་བཞིའི༌[^694]དོན་དུ་འགྱུར་ལ། ལུས་ཀྱི་འབྱུང་བ་ཆེན་པོ་ད་ལྟར་བྱུང་བ་རྣམས་ནི་རྟེན་དུ་འགྱུར་ཏེ། འཁོར་ལོ་ས་ལ་འདྲིལ་བ་ལག་པས་འཕུལ་བ་དང་། སའི་ཕྱོགས་བཞིན་ནོ། །

[Block 1821]
ཡང་གང་ན་ཡོད་པའི་ལུས་དང་ངག་གི་ལས་གང་ན་ཡོད་པའི་འབྱུང་བ་ཆེན་པོ་དག་རྒྱུར་བྱས་པ་ཡིན་ཞེ་ན།

[Block 1822 [VERSE]]
ཟག་བཅས་ལུས་དང་ངག་གི་ལས། །
རང་གི་འབྱུང་བ་དག་རྒྱུར་བྱས། །

[Block 1823]
འདོད་པ་ན་སྤྱོད་པ་ནས་བསམ་གཏན་བཞི་པའི་བར་གྱི་ལུས་དང་ངག་གི་ལས་དེའི་ས་པའི་འབྱུང་བ་དག་ཁོ་ན༌[^695]རྒྱུར་བྱས་པ་ཡིན་ནོ། །

[Block 1824]
ཟག་མེད་གང་དུ་སྐྱེས་པའི་ཡིན། །ས་གང་དུ་སྐྱེས་པ་དེ་སྐྱེད་པར༌[^696]བྱེད་པ་དེའི་ས་པའི་འབྱུང་བ་ཆེན་པོ་དག་རྒྱུར་བྱས་པར༌[^697]རིག་པར་བྱ༌[^698]སྟེ། རྣམ་པར་རིག་བྱེད་མ་ཡིན་པའི་ལས་དེ་ལས་ཀྱང་།

[Block 1825 [VERSE]]
རྣམ་རིག་བྱེད་མིན་མ་ཟིན་དང་། །
རྒྱུ་མཐུན་ལས་བྱུང་སེམས་ཅན་སྟོན། །
--- END BLOCKS ---
