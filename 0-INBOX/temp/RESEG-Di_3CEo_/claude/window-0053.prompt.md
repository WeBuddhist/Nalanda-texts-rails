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
[Block 1856]
ཀུན་ནས་སློང་བ་ནི་རྣམ་པ་གཉིས་ཏེ། རྒྱུའི་ཀུན་སློང་དང་། དེའི་དུས་ཀྱི་ཀུན་ནས་སློང་བ་སྟེ། དེའི་དུས་ཁོ་ན་ན་དེ་ཡོད་པའི་ཕྱིར་རོ། །

[Block 1857 [VERSE]]
གཉིས་ལས་དང་པོ་རབ་འཇུག་བྱེད། །
གཉིས་པ་རྗེས་སུ་འཇུག་བྱེད་ཡིན། །

[Block 1858]
རྒྱུའི་ཀུན་ནས་སློང་བ་ནི་འཕེན་པར་བྱེད་པ་ཡིན་པའི་ཕྱིར་རབ་ཏུ་འཇུག་པར་བྱེད་པ་ཡིན་ནོ། །

[Block 1859]
དེའི་དུས་ཀྱི་ཀུན་ནས་སློང་བ་ནི་བྱ་བའི་དུས་སུ་མཐུན་པར་འཇུག་པའི་ཕྱིར་རྗེས་སུ་འཇུག་པར་བྱེད་པ་ཡིན་ནོ། །

[Block 1860]
དེ་ལ་ཡང་། མཐོང་བས་སྤང་བྱའི་རྣམ་ཤེས་ནི། །རབ་ཏུ་འཇུག་བྱེད་ཡིན། མཐོང་བས་སྤང་བར་བྱ་བའི་སེམས་ནི་དེ་ཀུན་ནས་སློང་བར་བྱེད་པ་དཔྱོད་པ་དང་རྟོག་པ་དག་གི་གཞིར་གྱུར་པའི་ཕྱིར་རྣམ་པར་རིག་བྱེད་རབ་ཏུ་འཇུག་པར་བྱེད་པ་ཡིན་གྱི་སེམས་ཁ་ཕྱིར་བལྟས་པའི་ཕྱིར་རྗེས་སུ་འཇུག་པར་བྱེད་པ་ནི་མ་ཡིན་ནོ། །

[Block 1861]
དེ་ལྟ་བས་ན་མདོ་ལས་རྒྱུའི་ཀུན་ནས་སློང་བའི་དབང་དུ་མཛད་ནས་གསུངས་པའི་ཕྱིར་མི་འགལ་ལོ། །

[Block 1862]
ཡིད་ནི། བསྒོམ་པས་སྤང་བྱ་གཉིས་ཀ་ཡིན། །ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་བསྒོམ་པས་སྤང་བར་བྱ་བ་ནི་གཉིས་ཀ་ཡིན་ཏེ། རབ་ཏུ་འཇུག་པར་བྱེད་པ་ཡང་ཡིན་ལ་རྗེས་སུ་འཇུག་པར་བྱེད་པ་ཡང་ཡིན་ནོ། །

[Block 1863]
ལྔ་ནི་རྗེས་སུ་འཇུག་བྱེད་ཡིན། །རྣམ་པར་ཤེས་པའི་ཚོགས༌[^721]ལྔ་ནི་རྗེས་སུ་འཇུག་པར་བྱེད་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 1864]
ཡང་ཅི་རབ་ཏུ་འཇུག་པར་བྱེད་པ་ཇི་ལྟ་བར་རྗེས་སུ་འཇུག་པར་བྱེད་པ་ཡང་དེ་དང་འདྲ་འམ་ཞེ་ན། འདི་ནི་ངེས་པ་མེད་དེ།

[Block 1865 [VERSE]]
རབ་ཏུ་འཇུག་བྱེད་དགེ་སོགས་ལས། །
རྗེས་འཇུག་བྱེད་ཀྱང་རྣམ་གསུམ་འགྱུར། །

[Block 1866]
རབ་ཏུ་འཇུག་པར་བྱེད་པ་དགེ་བ་ལས་ཀྱང་རྗེས་སུ་འཇུག་པར་བྱེད་པ་དགེ་བ་དང་མི་དགེ་བ་དང་ལུང་དུ་མ་བསྟན་པར་ཡང་འགྱུར་ལ། མི་དགེ་བ་དང་ལུང་དུ་མ་བསྟན་པ་ལ་ཡང་དེ་དང་འདྲའོ། །

[Block 1867]
ཐུབ་པའི་འདྲ་བའམ་དེ་དགེ་བ། །རབ་ཏུ་འཇུག་པར་བྱེད་པ་དགེ་བ་ལས་ཀྱང་རྗེས་སུ་འཇུག་པར་བྱེད་པ་འདྲ་བ་དང་། ལུང་དུ་མ་བསྟན་པ་ལས་ཀྱང༌[^722]རྗེས་སུ་འཇུག་པ་དགེ་བ་ཡིན་ནོ། །

[Block 1868]
བསྒོམ་པས་སྤང་བར་བྱ་བའི་ཡིད་ནི་རབ་ཏུ་འཇུག་པར་བྱེད་པ་ཡང་ཡིན་ལ་རྗེས་སུ་འཇུག་པར་བྱེད་པ་ཡང་ཡིན་ནོ་ཞེས་བཤད་པ། རྣམ་སྨིན་ལས་སྐྱེས་གཉིས་ཀ་ཡིན།[^723] །རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པའི་སེམས་ནི་མངོན་པར་འདུ་བྱ་བ་མེད་པར་འཇུག་པ་ཉིད་ཀྱི་ཕྱིར་རབ་ཏུ་འཇུག་པར་བྱེད་པ་ཡང་མ་ཡིན་ལ། རྗེས་སུ་འཇུག་པར་བྱེད་པ་ཡང་མ་ཡིན་ནོ། །

[Block 1869]
ཞར་ལ་འོངས་པ་རྫོགས་སོ།། །།

[Block 1870 [HEADING]]
### སྡོམ་པ་དང་སྡོམ་པ་མ་ཡིན་པ་དང་བར་མ། ^4-2-0

[Block 1871]
སྔར་བཤད་པ་དེ་ནི།

[Block 1872 [VERSE]]
རྣམ་རིག་མིན་རྣམ་གསུམ་ཞེས་བྱ།[^724] །
སྡོམ་དང་སྡོམ་པ་མིན་དང་གཞན། །

[Block 1873]
འཆལ་པའི་ཚུལ་ཁྲིམས་ཀྱི་རྒྱུན་སྡོམ་ཞིང་འགོག་པས་ན་སྡོམ་པའོ། །

[Block 1874]
དེ་ལ།

[Block 1875 [HEADING]]
#### སོ་སོར་ཐར་པ་དང་བསམ་གཏན་སྐྱེས་དང་ཟག་མེད་ཀྱི་སྡོམ་པ། ^4-2-1-0

[Block 1876 [VERSE]]
སྡོམ་པ་སོ་སོར་ཐར་ཅེས་བྱ། །
དེ་བཞིན་ཟག་མེད་བསམ་གཏན་སྐྱེས། །

[Block 1877]
དེ་ལ། སོ་སོར་ཐར་ཅེས་བྱ་རྣམ༌[^725]བརྒྱད། །དགེ་སློང་དང་། དགེ་སློང་མ་དང་། དགེ་སློབ་མ༌[^726]དང་། དགེ་ཚུལ་དང་། དགེ་ཚུལ་མ་དང་། དགེ་བསྙེན་དང་། དགེ་བསྙེན་མ་དང་། བསྙེན་གནས་པའི་སྡོམ་པ་སྟེ། སྡོམ་པ་འདི་ནི་མིང་དུ་རྣམ་པ་བརྒྱད་ཡིན་ནོ། །

[Block 1878]
རྫས་སུ་རྣམ་པ་བཞི་ཡིན་ནོ། །

[Block 1879]
དགེ་སློང་དང་། དགེ་ཚུལ་དང་། དགེ་བསྙེན་དང་། བསྙེན་གནས་ཀྱི་སྡོམ་པའོ། །ཇི་ལྟར་ཤེས་ཤེ་ན། མཚན་ལས་མིང་ནི་འཕོ་བའི་ཕྱིར། །མཚན་གྱུར་ན་དགེ་སློང་ནི་དགེ་སློང་མ་ཞེས་བྱ་ལ། དགེ་སློང་མ་ཡང་དགེ་སློང་ཞེས་བྱ་སྟེ། དེ་བཞིན་དུ་དགེ་བསྙེན་ནི་དགེ་བསྙེན་མ་ཞེས་བྱ་བའི་བར་དུའོ། །

[Block 1880]
མཚན་གྱུར་པ་ལ་སྔོན་གྱི་སྡོམ་པ་གཏོང་བའི་རྒྱུ་ཡང་ཡོད་པ་མ་ཡིན་ལ་སྔོན་མེད་པའི་སྡོམ་པ་འཐོབ་པའི་རྒྱུ་ཡང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1881]
སྡོམ་པ་འདི་སྐྱེ་བ་ན་ཡང་། ཐ་དད། སྐྱེས་ཏེ་མ་འདྲེས་པ་ཉིད་དོ། །

[Block 1882]
དགེ་བསྙེན་གྱིས་དགེ་ཚུལ་དང་དགེ་སློང་གི༌[^727]སྡོམ་པ་བླངས་པས་སྔར་གྱི་རྣམས་ལས་སྡོམ་པ་གཞན༌[^728]བསྣན་པས་ལྷག་པར་ནི་མི་བྱེད་དོ། །

[Block 1883]
དེ་བཞིན་གཞན་ཡང་ངོ་། །དེ་དག་འགལ་བ་མེད། སྡོམ་པ་ཕྱི་མ་ཡང་དག་པར་བླངས་པས་སྔོན་ཐོབ་པ་གཏོང་བ་ནི་མ་ཡིན་ཏེ། དེ་ལྟ་མ་ཡིན་ན་དགེ་སློང་གི་སྡོམ་པ་ཡོངས་སུ་བཏང་བས་དགེ་བསྙེན་ཡང་མ་ཡིན་པ་ཁོ་ནར་འགྱུར་དུ་འོང་ངོ་། །ཇི་ལྟར་ན་དགེ་བསྙེན་ཡིན་པ་ནས། དགེ་སློང་གི་བར་དུ་ཡིན་ཞེ་ན།

[Block 1884 [VERSE]]
སྤང་བྱ་ལྔ་བརྒྱད་ཅུ་དང་ནི། །
ཐམས་ཅད་སྤོང་བ་མནོས་པ་ལས། །
དགེ་བསྙེན་དང་ནི་བསྙེན་གནས་དང་། །
དགེ་ཚུལ་ཆེད༌[^729]དང་དགེ་སློང་ཉིད། །

[Block 1885]
སྤང་བར་བྱ་བ་ལྔ་པོ་ལས་སླར་ལྡོག་པ་ཡང་དག་པར་བླངས་པས་ནི་དགེ་བསྙེན་གྱི་སྡོམ་པ་དང་། བརྒྱད་པོ་ལས་བསྙེན་གནས་ལ་གནས་པ་དང་། གསེར༌[^730]དངུལ་འཛིན་པ་ལས་སླར་ལྡོག་པ་བརྒྱད་པོ་ལ་བསྣན་ནས་བཅུ་པོ་ལས་དགེ་ཚུལ་ཡིན་ནོ། །

[Block 1886]
འདིར་ཡང་གར་དང་། གླུ་དང་། རོལ་མོ་དང་། དྲི་དང་། ཕྲེང་བ་དང་། བྱུག་པ་གཉིས་སུ་བྱས་ན་ནི་བཅུར་འགྱུར་རོ། །

[Block 1887]
སྤང་བར་བྱ་བ་ཐམས་ཅད་ལས་སླར་ལྡོག་པ་ཡང་དག་པར་བླངས་པས་ནི་དེ༌[^731]དགེ་སློང་ཡིན་ནོ། །

[Block 1888]
སོ་སོར་ཐར་པའི་སྡོམ་པ་ཉིད་ནི།

[Block 1889 [VERSE]]
ཚུལ་ཁྲིམས་དང་ནི་ལེགས་སྤྱད་དང་། །
ལས་དང་སྡོམ་པ་ཞེས་བྱའོ། །

[Block 1890]
ལས་མི་མཉམ་པ་ལས་ལོག་པ་ཡང་དག་པར་བླངས་པས་ན་ཚུལ་ཁྲིམས་སོ། །

[Block 1891]
མཁས་པས་བསྔགས་པས་ན་ལེགས་སྤྱད་དོ། །

[Block 1892]
བྱ་བའི་རང་བཞིན་ཡིན་པས་ན་ལས་སོ། །

[Block 1893]
དེ་ལྟར་ན་རེ་ཞིག་བྱེ་བྲག་མེད་པར་སོ་སོར་ཐར་པའི་སྡོམ་པ་ཡང་དག་པར་བསྟན་ནོ། །

[Block 1894]
ཡང་།

[Block 1895 [VERSE]]
དང་པོའི་རྣམ་རིག་རྣམ༌[^732]རིག་མིན། །
སོ་སོར་ཐར་དང་བྱ་བའི་ལམ། །
--- END BLOCKS ---
