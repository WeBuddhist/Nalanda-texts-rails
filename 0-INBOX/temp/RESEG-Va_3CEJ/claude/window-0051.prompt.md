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
ཡི་གེ་རྣམས་ཀྱང་ཡི་གེ༌[^861]འབྲུའི་ཡན་ལག་དག་གི་མིང་དག་མ་ཡིན་ནམ༌[^862]ཞེ་ན། ཡི་གེ༌[^863]འབྲུའི་ཡན་ལག་རྣམས་གོ་བར་བྱ་བའི་ཕྱིར་ཡི་གེ་རྣམས་བྱས་པ་ནི་མ་ཡིན་གྱི། ཇི་ལྟར་ན་མིང་ཐོས་པ་བྲིས་པས་གོ་བར་འགྱུར་ཞེས་ཡི་གེ་རྣམས་གོ་བར་བྱ་བའི་ཕྱིར་ནི་ཡི་གེའི༌[^864]འབྲུ་རྣམས་བྱས་པ་ཡིན་པས། ཡི་གེ་རྣམས་ནི་དེ་དག་གི་མིང་མ་ཡིན་ནོ། །

[Block 1787]
མིང་ལ་སོགས་པ་དེ་དག་གི་ཚོགས་ནི་མིང་ལ་སོགས་པའི་ཚོགས་དག་ཡིན་ཏེ། མང་པོའི་དོན་གང་ཡིན་པའོ། །

[Block 1788]
དེ་ལ་མིང་གི་ཚོགས་ནི་དཔེར་ན་གཟུགས་སྒྲ་དྲི་རོ་རེག་བྱ་དག་ཅེས་བྱ་བ་སྟེ། དེ་ལྟ་བུ་ལ་སོགས་པའོ། །

[Block 1789]
ཚིག་གི་ཚོགས་ནི་དཔེར་ན་འདུ་བྱེད་ཐམས་ཅད་མི་རྟག་པ་དག་གོ། །

[Block 1790]
མྱ་ངན་ལས་འདས་པ་ནི་ཞི་བའོ་ཞེས་བྱ་བ་སྟེ། དེ་ལྟ་བུ་ལ་སོགས་པའོ། །

[Block 1791]
ཡི་གེའི་ཚོགས་ནི་དཔེར་ན་ཀ་ཁ་ག་གྷ་ང་ཞེས་བྱ་བ་སྟེ། དེ་ལྟ་བུ་ལ་སོགས་པའོ། །

[Block 1792]
དེ་དག་ཀྱང་ངག་གི་རང་བཞིན་ཡིན་པའི་ཕྱིར་སྒྲའི་བདག་ཉིད་ཡིན་པས་གཟུགས་ཀྱི་རང་བཞིན་དག་མ་ཡིན་ནམ་ཅིའི་ཕྱིར་སེམས་དང་ལྡན་པ་མ་ཡིན་པ་རྣམས་ཞེས་བྱ་ཞེ་ན། དེ་དག་ནི་ངག་གི་རང་བཞིན་མ་ཡིན་ཏེ། ངག་གི༌[^865]སྒྲ་ཡིན་ན་སྒྲ་ཙམ་གྱིས་ནི་དོན་གང་དག་གོ་བར་མི་འགྱུར་རོ། །

[Block 1793]
འོ་ན་ཅི་ཞེ་ན། ངག་ནི་མིང་ལ་འཇུག་ལ་མིང་གིས་ནི་དོན་རྗོད་པར་བྱེད་དོ། །

[Block 1794]
སྒྲ་ཙམ་ཁོ་ན་ནི་ངག་མ་ཡིན་གྱི་སྒྲ་གང་གིས་དོན་གོ་བར་འགྱུར་བའི་སྒྲ་དེ་ངག་ཡིན་ནོ། །

[Block 1795]
ཡང༌[^866]སྒྲ་གང་གིས་དོན་གོ་བར་འགྱུར་ཞེ་ན། གང་གིས་སྨྲ་བ་པོ་རྣམས་ཀྱིས་དོན་དག་ལ་མཚམས་བཅད་པ་སྟེ། དཔེར་ན་གཽ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 1796]
སྒྲ་དེ་ནི་དོན་དགུ་དག་ལ་མཚམས་བཅད་པ་ཡིན་ཏེ།

[Block 1797 [VERSE]]
ངག་ཕྱོགས་པ༌[^867]དང་འོད་ཟེར་དང་། །
ཕྱུགས་དང་མིག་དང་རྡོ་རྗེ་དང་། །
མཐོ་རིས་ཆུ་དང་དོན་དགུ་ལ། །
མཁས་པས་གཽ་སྒྲ་དེས་གཟུང་བྱ། །

[Block 1798]
ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 1799]
གང་ཡང་མིང་གིས་དོན་རྗོད་པར་བྱེད་དོ་སྙམ་དུ་སེམས་པ་དེས་ཀྱང་གདོན་མི་ཟ་བར་གལ་ཏེ་དོན་གོ་བར་བྱེད་པ་ཡིན༌[^868]ཞེས་བྱ་བ་འདི་ཁས་བླང་བར་བྱ་དགོས་ཏེ། དེ་ནི་དོན་གོ་བར་བྱེད་པའི་སྒྲ་ཙམ་ཁོ་ནས་འགྲུབ་ན་དོན་གཞན་རྫས་མིང་བཏགས་ཏེ་ཅི་ཞིག་བྱ། ཇི་ལྟར་ན་ངག་མིང་ལ་འཇུག་པ་འདི་ཡང་མི་ཤེས་སོ། །

[Block 1800]
ཅི་རེ་ཞིག་སྐྱེད་པར་བྱེད་དམ། འོན་ཏེ་གསལ་བར་བྱེད། གལ་ཏེ་སྐྱེད་པར་བྱེད་ན་ནི་ངག་ནི་སྒྲའི་རང་བཞིན་ཡིན་པའི་ཕྱིར་སྒྲ་ཙམ་ཐམས་ཅད་ཀྱིས་མིང་སྐྱེད་པར་འགྱུར་རོ། །

[Block 1801]
འོན་ཏེ་སྒྲའི་ཁྱད་པར་དེ་ལྟ་བུ་ཞིག་མིང་སྐྱེད་པར༌[^869]བྱེད་པ་ཡིན་པར་འདོད་ན་ནི༌[^870]དེ་ཉིད་དོན་རྗོད་པར༌[^871]བྱེད་པ་ཡིན་པར་འགྱུར་རོ། །

[Block 1802]
འོན་ཏེ༌[^872]གསལ་བར་བྱེད་པ་ཡིན་ནོ་ཞེ་ན་ནི་ངག་གི༌[^873]སྒྲའི་རང་བཞིན་ཡིན་པའི་ཕྱིར་སྒྲ་ཙམ་ཐམས་ཅད་ཀྱི༌[^874]མིང་གསལ་བར་བྱེད་པར་འགྱུར་རོ། །

[Block 1803]
འོན་ཏེ་སྒྲའི་ཁྱད་པར་དེ་ལྟ་བུ་ཞིག༌[^875]གསལ་བར་བྱེད་པ་ཡིན་པར་འདོད་ན་ནི་དེ་ཉིད་དོན་གསལ་བར་བྱེད་པ་ཡིན་པར་འགྱུར་རོ། །

[Block 1804]
ཡང་སྒྲ་རྣམས་ནི་ཚོགས་པ་མེད་ལ་ཆོས་གཅིག་ལ་ཆ་ཤས་ཀྱི༌[^876]སྐྱེད་པ་ཡང་རིགས་པ༌[^877]མ་ཡིན་ལ། སྐྱེད་པར་བྱེད་པ་ན་ཇི་ལྟར་ངག་གིས་མིང་སྐྱེད་པར་བྱེད། རེ་ཞིག་ཇི་ལྟར་ན་འདས་པ་ལ་ལྟོས་པའི་རྣམ་པར་རིག་བྱེད་ཀྱི་སྐད་ཅིག་མ་ཐ་མས་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་སྐྱེད་པར་བྱེད། དེ་ལྟ་ན་འོ་ན་ནི་སྒྲ་ཐ་མ་ཁོ་ནས་མིང་སྐྱེད་པའི་ཕྱིར་གང་གིས་དེ་གཅིག་ཁོ་ན༌[^878]ཐོས་པ་དེས་ཀྱང་དོན་གོ་བར་འགྱུར་རོ། །

[Block 1805]
འོན་ཏེ་འདི་སྙམ་དུ་ངག་གིས་ནི༌[^879]ཡི་གེ་སྐྱེད་པར་བྱེད་ལ། ཡི་གེས་ནི་མིང་སྐྱེད་པར་བྱེད་དོ་སྙམ་དུ་རྟོག་པར་བྱེད་ན། འདི་ལ་ཡང་སྐྱོན་དེ་ཉིད་ཡོད་དེ། ཡི་གེ་རྣམས་ཚོགས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 1806]
ངག་མིང་གསལ་བར་བྱེད་པ་ཡིན་ན་ཡང་སྐྱོན་དེ་ཉིད་ཡོད་དོ།[^880] །ཡི་གེ་ཡང་ངག་ལས་ཁྱད་པར་དུ༌[^881]ཡོད་པར་ཤེས་རབ་དང་ལྡན་པར་ཡིད་བརྟན་པས་ཀྱང་མཚན་ཉིད་ཀྱི་སྒོ་ནས་ཡོངས་སུ་བཅད་པར་མི་ནུས་པས་ངག་ནི་ཡི་གེ་སྐྱེད་པར་བྱེད་པ་ཡིན་པར་ཡང་མི་རུང་ལ། གསལ་བར་བྱེད་པ་ཡིན་པར་ཡང་མི་རུང་ངོ་། །འོན་ཏེ་མིང་དོན་དང་ལྷན་ཅིག་སྐྱེད་པ་ཡིན་ཏེ། སྐྱེ་བ་ལ་སོགས་པ་བཞིན་ནོ་ཞེས་བྱ་བར་འདོད་ན་ནི་དེ་ལྟ་ན་དོན་འདས་པ་དང་མ་འོངས་པའི་མིང་ད་ལྟ་བ༌[^882]ཡིན་པར་མི་འགྱུར་རོ། །

[Block 1807]
ཕ་རྣམས་ཀྱིས༌[^883]བུ་དག་གི༌[^884]མིང་དགའ་མགུར་འདོགས་ན་མིང་གང་ཞིག་དེ་དང་ལྷན་ཅིག་སྐྱེས་པ་ཡིན་པར་འགྱུར། ཆོས་འདུས་མ་བྱས་པ་རྣམས་ཀྱི་མིང་ཡང་གང་དང་ལྷན་ཅིག་སྐྱེས་པ༌[^885]ཡིན་པར་འགྱུར། དེ་ལྟ་བས་ན་འདི་ཉིད་མི་འདོད་པ་ཉིད་དོ། །

[Block 1808]
གང་ཡང་བཅོམ་ལྡན་འདས་ཀྱིས།

[Block 1809 [VERSE]]
ཚིགས་བཅད་མིང་ལ་བརྟེན་པ་སྟེ། །
ཚིགས་བཅད་བཞི་ནི་སྙན་དངགས་མཁན། །

[Block 1810]
ཞེས་གསུངས་པ་དེར་ཡང་དོན་རྣམས་ལ་མཚམས་བཅད་པའི་སྒྲ་ནི་མིང་ཡིན་ལ། མིང་རྣམས་བཀོད་པའི་ཁྱད་པར་ཡང་ཚིགས་སུ་བཅད་པ་ཡིན་པས་མིང་ལ་བརྟེན་པ་ཡིན་ནོ། །

[Block 1811]
བཀོད་པའི་ཁྱད་པར་ཡང་རྫས་གཞན་དུ་མི་འཐད་དེ་ཕྲེང་བ་ལྟ་བུ་དང་སེམས་ཀྱི་རིམ་པ་བཞིན་ནོ། །

[Block 1812]
ཡི་གེ་ཙམ་ཞིག་རྫས་གཞན་གྱི་དངོས་པོར་ཡོངས་སུ་རྟོག་པ་ཡིན༌[^886]དུ་ཆུག་ན་ཡང་དེའི་ཚོགས་ཁོ་ན་མིང་གི་ཚོགས་ལ་སོགས་པ་ཡིན་བར་འགྱུར་བས་དེ་དག་ཏུ་རྟོག་པ་དོན་མེད་པ་ཡིན་ནོ། །

[Block 1813]
བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ་ཆོས་ཐམས་ཅད་རྟོག་གེའི་སྤྱོད་ཡུལ་མ་ཡིན་པས་ལྡན་པ་ཡང་མ་ཡིན་པའི་འདུ་བྱེད་ཀྱི་རང་བཞིན་མིང་གི་ཚོགས་ལ་སོགས་པ་ནི་རྫས་སུ་ཡོད་པ་ཁོ་ནའོ་ཞེས་ཟེར་རོ། །

[Block 1814]
ཡང་ཅི་མིང་གི་ཚོགས་ལ་སོགས་པ་འདི་དག་ལྡན་པ་འམ། སེམས་ཅན་དུ་སྟོན་པ་འམ། སེམས་ཅན་དུ་སྟོན་པ་མ་ཡིན་པ་འམ། རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པ་འམ། རྒྱས་པ་ལས་འབྱུང་བ༌[^887]འམ། རྒྱུ་མཐུན་པ་ལས་བྱུང་བ་འམ། དགེ་བ་འམ། མི་དགེ་བ་འམ། ལུང་དུ་མ་བསྟན་པ་དག་ཅིག་ཅེས་བརྗོད་པར་བྱ་ཞེ་ན། སྨྲས་པ།

[Block 1815 [VERSE]]
འདོད་དང་གཟུགས་གཏོགས་སེམས་ཅན་སྟོན། །
རྒྱུ་མཐུན་ལས་བྱུང་ལུང་བསྟན་མིན། །
འདི་དག་ནི་འདོད་པར་གཏོགས་པ་དང་།
གཟུགས་སུ་གཏོགས་པ༌[^888]དག་ཡིན་ནོ། །

[Block 1816]
གཞན་དག་ན་རེ་གཟུགས་མེད་པར་གཏོགས་པ་ཡང་ཡོད་མོད་ཀྱི་དེ་དག་ནི་བརྗོད་པར་བྱ་བ་མ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 1817]
དེ་དག་ནི་སེམས་ཅན་དུ་སྟོན་པ་ཡིན་ནོ། །

[Block 1818]
གང་ཞིག་རྗོད་པར༌[^889]བྱེད་པ་དེ་དག་དང་ལྡན་གྱི་བརྗོད་པར་བྱ་བ་གང་ཡིན་པ་དང་ནི་མ་ཡིན་ནོ། །

[Block 1819]
རྒྱུ་མཐུན་པ་ལས་བྱུང་བ་དང་། མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་དག་ཡིན་ནོ། །

[Block 1820]
ཇི་ལྟར་མིང་གི་ཚོགས་ལ་སོགས་པ་འདི་དག་སེམས་ཅན་དུ་སྟོན་པ་དང་། རྒྱུ་མཐུན་པ་ལས་བྱུང་བ་དང་། མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་དག་ཡིན་པ་དེ་བཞིན་སྐལ་མཉམ་དེ་ནི་རྒྱུ་མཐུན་པ་ལས་བྱུང་བ་འབའ་ཞིག་མ་ཡིན་གྱི། རྣམ་པར་སྨིན་པ་འང༌[^890]ཡིན། ཁམས་གསུམ་པ་སྟེ། འདོད་པ་དང་གཟུགས་དང་གཟུགས་མེད་པ་ན་སྤྱོད་པ་ཡིན་ནོ། །

[Block 1821]
ཐོབ་རྣམ་གཉིས། ཐོབ་པ་རྣམས་ནི་རྒྱུ་མཐུན་པ་ལས་བྱུང་བ་དང་། རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པ་དག་ཡིན་ནོ། །

[Block 1822]
མཚན་ཉིད་རྣམས་ཀྱང་། རྣམ་གཉིས་ཞེས་བྱ་བར་སྦྱར་ཏེ་ཐོབ་པ་བཞིན་ནོ། །

[Block 1823]
སྙོམས་འཇུག་དང་། མི་ལྡན་པ་དག་རྒྱུ་མཐུན་པ། སེམས་མེད་པའི་སྙོམས་པར་འཇུག་པ༌[^891]གཉིས་དང་མི་ལྡན་པ་རྣམས་ནི་རྒྱུ་མཐུན་པ་ལས་བྱུང་བ་དག་ཁོ་ན་ཡིན་ནོ། །

[Block 1824]
འདི་དག་གི་བརྗོད་པར་བྱ་བ་ལྷག་མ་དང་། ལྷག་མ་འདུ་ཤེས་མེད་པ་པ་དང་། སྲོག་གི་དབང་པོ་དག་གིས༌[^892]ནི་བཤད་ཟིན་པས་དེའི་ཕྱིར་ཡང་མི་བརྗོད་དོ། །

[Block 1825]
ཇི་ལྟར་ཐོབ་པ་རྣམས་ཀྱི་སེམས་ཅན་དུ་སྟོན་པ་ཉིད་བཤད་ཟིན་ཅེ་ན། ལྡན་པ་ཞེས་བཤད་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
