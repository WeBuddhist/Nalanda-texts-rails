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
[Block 1751]
དེ་ལ་ཚིག་གི་དོན་ནི་གཉིས་ཏེ། བསྐྱེད་པའི་རིམ་པ་དང་རྫོགས་པའི་རིམ་པའོ། །

[Block 1752]
དེ་དག་གི༌[^1247]མ་ལུས་པ་དེ་ནི་དང་པོའི་དབྱེ་བ་གསུམ་དང་གཉིས་པའི༌[^1248]ལྔའོ། །

[Block 1753]
དེ་རྣམས་གྲུབ་པ་ནི་བཤད་པའི་རྒྱུད་ཀྱི༌[^1249]ཚིག་གིས་བསྟན་པའོ། །

[Block 1754]
དེ་བཞིན་དུ་ཡང་ལེའུ་བཅོ་བརྒྱད་པ་ལས།

[Block 1755 [VERSE]]
བསྐྱེད་པ་ཡི་ནི་རིམ་པ་དང་། །
རྫོགས་པ་ཡི་ནི་རིམ་པ་སྟེ། །
རིམ་པ་གཉིས་ལ་བརྟེན་ནས་ནི། །
རྡོ་རྗེ་ཅན་རྣམས་ཆོས་བསྟན་པའོ། །

[Block 1756]
ཞེས་རྩ་བའི་རྒྱུད་ཀྱི་ཚིག་གོ། །

[Block 1757 [VERSE]]
ཡི་གེའི་དོན་དང་སྤྱི་དོན་དང་། །
སྦས་པ་དང་ནི་མཐར་ཐུག་པ། །

[Block 1758]
ཞེས་བྱ་བའི་རྡོ་རྗེ་ཕྲེང་བའི་བཤད་པའི་རྒྱུད་ལས་གསུངས་པའི་ཚིག་གིས་བསྐྱེད་པའི་རིམ་པའི་དང་པོ་སྦྱོར་བ་ལ་སོགས་པ་གསུམ་དང་། རྫོགས་པའི་རིམ་པའི་རྡོ་རྗེ་བཟླས་པ་ལ་སོགས་པའི་ཚིག་གི་དོན་ལྔ་བསྟན་ཏོ། །

[Block 1759]
དེ་རྣམས་ཚང་བར་བསྟན་པ་ནི་མ་ཚང་བ༌[^1250]མེད་པ་ཞེས་བྱ་བའི་ཡན་ལག་བཞི་པའོ། །

[Block 1760 [HEADING]]
#### འདྲི་བ་དང་ལན་འདེབས་པ། ^1-6-5-0

[Block 1761]
འདྲི་བ་དང་ལན་འདེབས་པ་ནི་འདྲི་བ་དང་ལན་འདེབས་པའོ། །

[Block 1762]
དེ་དག་བསྟན་པ་ནི་འདྲི་བ་དང་ལན་འདེབས་པ་བསྟན་པའོ། །

[Block 1763]
ཇི་སྐད་དུ་ལེའུ་བཅོ་བརྒྱད་པ་ལས།

[Block 1764]
གསང་བ་ཞེས་བྱ་བ་ཇི་ལྟར་བཤད་བྱ་བ་ནས་བརྩམས་ཏེ་ཕྲིན་ལས་ཀྱི་ཚོགས་མཆོག་ཅེས་བྱ་བའི་བར་དུ་འདྲི་བའི་ཚིག་བདུན་ཅུ་རྩ་གཉིས་སོ། །

[Block 1765 [VERSE]]
སྐུ་གསུང་ཐུགས་ནི་རྣམ་པ་གསུམ། །
གསང་བ་ཞེས་བྱར་བཤད་པ་ཡིན། །
ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ།
ཁྲོས་པས་དྲག་པོ་ཀུན་ཏུ་སྤྱོད། །

[Block 1766]
ཅེས་བྱ་བའི་བར་དུ་ལན་འདེབས་པའི་ཚིག་ཀྱང་བདུན་ཅུ་རྩ་གཉིས་བསྟན་ཏོ། །

[Block 1767]
གང་གི་ཕྱིར་སྤྱིར་སྟོན་པ་ནི་འདྲི་བ་དང་ཁྱད་པར་སྟོན་པ་ནི་ལན་འདེབས་པའོ། །

[Block 1768]
དེ་ཡང༌[^1251]རྣམ་པ་གཉིས་ཏེ། སྒྲ་དང་དོན་གྱིས་སོ། །

[Block 1769]
དེ་ལ་སྒྲ་ནི། སྐུ་གསུང་ཐུགས་ནི་རྣམ་པ་གསུམ། །ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 1770]
དོན་གྱིས༌[^1252]ནི།

[Block 1771 [VERSE]]
ཡུལ་དང་དབང་པོ་རྣམ་དག་ལ། །
བརྟེན་ཏེ་གང་ཞིག་ཡིད་སྐྱེས་པ། །
དེ་ནི་མན་ཞེས་བཤད་པ་སྟེ། །
ཏྲ་ནི་སྐྱོབ་པའི་དོན་ཡིན་ནོ། །

[Block 1772]
ཞེས་བྱའོ། །

[Block 1773]
དེ་ནི་འདྲི་བ༌[^1253]དང་ལན་བཏབ་པའི་མཚན་ཉིད་ཅན་ཡན་ལག་ལྔ་པའོ། །

[Block 1774 [HEADING]]
#### མདོར་བསྟན་པ་དང་རྒྱས་པར་བསྟན་པ། ^1-6-6-0

[Block 1775]
མདོར་བསྟན་པ་དང་རྒྱས་པར་བསྟན་པ་ནི་མདོར་བསྟན་པ་དང་རྒྱས་པར་བསྟན་པའོ། །

[Block 1776]
ཟླས་དབྱེ་བ་ཐམས་ཅད་ནི་ཕྱོགས་གཅིག་ཏུ་འགྱུར་རོ་ཞེས་གཅིག་གི་ཚིག་གི་མཐའ་ཅན་ནོ། །

[Block 1777]
མདོར་བསྡུས༌[^1254]པའི་ཚིག་ནི་མདོར་བསྟན་པའོ། །

[Block 1778]
འདི་ལྟ་སྟེ།

[Block 1779 [VERSE]]
ཐ་མལ་མཆོག་གི་དབྱེ་བ་ཡིས། །
བསྙེན་པ་རྣམ་པ་གཉིས་ཡིན་ཏེ། །
ཐ་མལ་པ་ནི་རྡོ་རྗེའི་གཞི། །
ཡན་ལག་དྲུག་ནི་མཆོག་ཡིན་ནོ། །

[Block 1780]
རྒྱ་ཆེ་བའི་ཚིག་ནི་རྒྱས་པར་བཤད་པ་འདི་ལྟ་སྟེ།

[Block 1781 [VERSE]]
དང་པོར་སྟོང་ཉིད་བྱང་ཆུབ་སྟེ། །
གཉིས་པ་ས་བོན་བསྡུས་པ་དང་། །
གསུམ་པ་གཟུགས་བརྙན་རྫོགས་པ་སྟེ། །
བཞི་པ་ཡིག་འབྲུ་རྣམས་དགོད་པའོ། །

[Block 1782 [VERSE]]
སོ་སོར་སྡུད་དང་བསམ་གཏན་དང་། །
སྲོག་རྩོལ་དེ་བཞིན་འཛིན་པ་དང་། །
རྗེས་སུ་དྲན་དང་ཏིང་འཛིན་ནི། །
རྣལ་འབྱོར་ཡན་ལག་དྲུག་ཏུ་བཤད། །

[Block 1783]
དེ་ནི་མདོར་བསྡུས་བསྟན་པ་དང་། །

[Block 1784]
རྒྱས་པར་བསྟན་པའི་མཚན་ཉིད་ཅན་ཡན་ལག་དྲུག་པའོ། །

[Block 1785 [HEADING]]
#### གོ་རིམས། ^1-6-7-0

[Block 1786]
ཚིག་གི་དོན་རིམ་པས་སྟོན་པ་ནི་གོ་རིམས་སོམོ། །

[Block 1787]
འདི་ལྟ་སྟེ།

[Block 1788]
[^1255]ལེའུ་དང་པོ་ལས།

[Block 1789]
བཛྲ་དྷྲྀཀ །ཛི་ན་ཛིཀ །རཏྣ་དྷྲྀཀ །ཨཱ་རོ་ལིཀ །པྲཛྙཱ་དྷྲྀཀ་ཅེས་བྱ་བས་དང་པོ་དེ་བཞིན་གཤེགས་པ་ལྔ་ཕྱུང་བའོ། །

[Block 1790]
དེའི་རྗེས་ལ་མོ་ཧ་ར་ཏི། དྭེ་ཥ་ར་ཏི། རཱ་ག་ར་ཏི། བཛྲ་ར་ཏི་ཞེས་བྱ་བས་དགའ་མ་རྣམས་ཕྱུང་བའོ། །
--- END BLOCKS ---
