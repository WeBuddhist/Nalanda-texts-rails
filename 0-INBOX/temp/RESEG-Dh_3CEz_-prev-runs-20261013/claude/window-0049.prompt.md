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
[Block 1716]
དང་པོ་རྣམ་བཅད་ས་གཞི་བཟུང་།[^805] །

[Block 1717 [HEADING]]
#### དང་པོ་སའི་ཆོ་ག། ^1-10-1-0

[Block 1718]
གཉིས་པ་སྟ་གོན་གནས་པར་བྱ། །ནུབ་གསུམ་པ་ལ༌[^806]འཇུག་པའོ། །ཞེས་གསུངས་པས་དང་པོ་སའི་ཆོ་ག་ནི་དོན་རྣམ་པ་དྲུག་སྟེ། ས་བརྟག་པ་དང་། ས་བསླང་བ་དང་། ས་སྦྱང་བ༌[^807]དང་། བྱིན་གྱིས་བརླབ་པ་དང་། གཟུང་བ་དང་། བསྲུང་བའོ། །

[Block 1719 [HEADING]]
##### ས་བརྟག་པ། ^1-10-1-1-0

[Block 1720]
དེ་ལ་ས༌[^808]བརྟག་པ་ནི་ཕྱིའི་བརྟག་པ་དང་། །ནང་གི་བརྟག་པའོ། །

[Block 1721 [HEADING]]
###### ཕྱིའི་བརྟག་པ། ^1-10-1-1-1-0

[Block 1722]
དེ་ལ་ཕྱིའི་གནས་ལ་བརྟག་པ་ནི་གོང་གི ཚལ་དང་སྐྱེ་བོ་མི་གནས༌[^809]དང་། །ཞེས་པར་འབྲེལ་ལོ། །

[Block 1723]
ཕྱོགས་ལ་བརྟག་པ་ནི་དེ་རྣམས་ཀྱི་བྱང་དང་ཤར་གྱི་ཕྱོགས་སུའོ། །

[Block 1724]
ཁ་དོག་དང་དབྱིབས་ལས་བརྟག་པ་ནི། ཨུ་དུམྺཱ༌[^810]ར་ནྱ་གྲོ་ངྷ། །ཨ་ཤཏྠ་དང་པ་ལ་ཤ །

[Block 1725 [VERSE]]
བ་ཀུ་ལ་དང་ཨ་རྫུ་ནར། །
བཅས་པས་རུས༌[^811]སྦལ་རྒྱབ་འདྲ་བར། །
ས་ནི་དྲུག་པོ་སྤང་བར་བྱ། །

[Block 1726]
ཞེས་གསུངས་པ་ཚ་སྒོ་ཅན་ལ་སོགས་པ་དང་། རོ་ཁུང་དུ་ཆུ་སོང་བ་འདྲ་བ་ལ་སོགས་པ་མཚན་མ་ངན་པ་རྣམས་སྤང་བར་བྱའོ། །

[Block 1727 [HEADING]]
###### ནང་གི་བརྟག་པ། ^1-10-1-1-2-0

[Block 1728]
ནང་གི་བརྟག་པ་ནི་བདེ་བར་གཤེགས་པ་ལ་མཆོད་པ་བྱས་ལ་གཏོར་མ་བཏང་སྟེ། ལྷག་པའི་ལྷའི་རྣལ་འབྱོར་ཙམ་གྱིས་ཉལ་བར་བྱའོ། །

[Block 1729]
དེ་ལ་རྨི་ལམ་གྱི་མཚན་མ་ངན་ན་གཞན་དུ་འཕོའོ། །

[Block 1730]
བཟང་ན་དེ་ཉིད་དུ་བྲི་བར་བྱའོ། །

[Block 1731 [HEADING]]
##### ས་བསླང་བ། ^1-10-1-2-0

[Block 1732]
བསླང་བ་ལ་གཉིས་ཏེ། མངོན་པ་ལ་བསླང་བ་དང་། མི་མངོན་པ་ལ་བསླང༌[^812]བའོ། །

[Block 1733 [HEADING]]
###### མངོན་པ་ལ་བསླང་བ། ^1-10-1-2-1-0

[Block 1734]
མངོན་པ་ནི༌[^813]རྒྱལ་པོའམ་ཞིང་བདག་ལ་ཚིག་དང་རིན་གྱིས་ཀྱང་ཉོ་བར་བྱའོ། །

[Block 1735 [HEADING]]
###### མི་མངོན་པ་ལ་བསླང་བ། ^1-10-1-2-2-0

[Block 1736]
མི་མངོན་པ་ལ་བསླང་བ་ནི་དེ་བཞིན་གཤེགས་པ་ལ་མཆོད་པ་བྱས་ཏེ། ས་བདག་ལ་ཨ་ཀཱ་རོས་གཏོར་མ་བྱིན་ལ་བསླང་བར་བྱའོ། །

[Block 1737 [HEADING]]
##### ས་སྦྱང་བ། ^1-10-1-3-0

[Block 1738]
ས་སྦྱང་བ་ནི་སྦྱང༌[^814]དགོས་པ་དང་མི་དགོས་པའོ། །

[Block 1739]
སྦྱང་མི་དགོས་པ་ནི།

[Block 1740 [VERSE]]
ཕྱུགས་ལྷས་དང་ནི་ཆུ་འགྲམ་དང་། །
རྡོ་ལེབ་དང་ནི་གཙུག་ལག་ཁང་། །

[Block 1741]
དཀྱིལ་འཁོར་ཁང་པའི་ནང་དུ་ཡང་། ཡང་ཐོགས༌[^815]ལས་ཀྱི་སྦྱང་བ་མིན།[^816] །སྦྱང་བ་ལ་གསུམ་སྟེ།

[Block 1742 [VERSE]]
ལས་དང་བྱ་བས་སྦྱང་བ་དང་། །
སྔགས་དང་ཕྱག་རྒྱས་སྦྱང་བ་དང་། །
ཏིང་ངེ་འཛིན་གྱིས་སྦྱང་བའོ། །

[Block 1743 [HEADING]]
###### ལས་དང་བྱ་བས་སྦྱང་བ། ^1-10-1-3-1-0

[Block 1744]
ལས་དང་བྱ་བས་སྦྱང་བ་ནི། ལྟོ་འཕྱེའི་རིམ་པར་ཤེས་པར་བྱ་སྟེ། སྟོན་ཟླ་ཐ་ཆུངས༌[^817]ལ་སོགས་པ་ནས་བརྩམས་ནས་ཟླ་བ༌[^818]གསུམ་གསུམ་དུ།

[Block 1745 [VERSE]]
ལྟོ་འཕྱེ་ལྷོ་དང་ནུབ་དང་ནི། །
[^819]ཤར་དང༌[^820]དེ་ཡི་མགོ་བོ་སྟེ། །
གཡོན་པའི་ཟུར་གྱིས་ཉལ་བ་ཡིན། །
དེ་ཡིས་ལྟོ་ཤེས་བྱས་ལ་བརྐོ། །

[Block 1746 [VERSE]]
མགོ་དང་རྒྱབ་སོགས་ནས་བརྐོས་ནས། །
སྐྱོན་ནི་རྒྱས་པ་ལས་ཤེས་བྱ། །

[Block 1747]
དེ་ཡང་།

[Block 1748 [VERSE]]
ལྟེ་བ་ལྐོག་མ་པུས་ནུབ་ཙམ། །
ས་དེ་ཡོངས་སུ་བརྐོས་ནས་ནི། །
སླར་ཡང་ས་དེས་དགང་བར་བྱ། །
གལ་ཏེ་ལྷག་པར་གྱུར་ན་ནི། །

[Block 1749]
དངོས་གྲུབ་ཡོད་པར་སྟོན་པ་ཡིན། །དེ་ལྟར་བརྐོས་པས་སའི་མཚན་མ་ངན་པ་བྱུང་ན་བསལ་ལས་བཟང་པོས་བཀང་སྟེ། གཏེར་ཀྱང་གཞུག་གོ། །

[Block 1750]
དེར་ཁྲུ་གང་ཙམ་གྱི་དོང་བྲུས་ཏེ་ཆུ་དང་མེ་ཏོག་བླུགས་ཏེ་ཕར་གོམ་པ་བརྒྱད་ཙམ་དུ༌[^821]འགྲོ་བར་བྱའོ། །

[Block 1751]
ཆུ་དེ་ཤར་ནས་ནུབ་ཏུ་རྒྱུ་བ་དང་། །ལྷོ་ནས་བྱང་དུ་རྒྱུ་བ་དང་། གཡས་སུ་འཁོར་ཞིང་འཁྱིལ་ན་མཚན་མ་བཟང་བ་དང་ངན་པ་ཡང་ཤེས་པར་བྱའོ། །

[Block 1752 [HEADING]]
###### སྔགས་དང་ཕྱག་རྒྱས་སྦྱང་བ། ^1-10-1-3-2-0

[Block 1753]
སྔགས་དང་ཕྱག་རྒྱས་སྦྱང་བ་ནི་ལག་པ་གཡས་པ་རྡོ་རྗེ་རྩེ་གསུམ་པའི་ཕྱག་རྒྱ་བཅས་ལ། ས་ལ་བརྡབ་ཅིང་ཨོཾ་སརྦ་པཱ་བཾ་ད་ཧ་ན་མཱ་མ་རཀྵ་རཀྵ་ཧཱུཾ་ཕཊ་སྭཱ་ཧཱ་ཞེས་བརྗོད་དོ། །

[Block 1754 [HEADING]]
###### ཏིང་ངེ་འཛིན་གྱིས་སྦྱང་བ། ^1-10-1-3-3-0

[Block 1755]
ཏིང་ངེ་འཛིན་ནི་ས་གཞི་དེ་མི་དམིགས་པར་བསྒོམ་ཞིང་ཤིན་ཏུ་དག་པར་བསམ་མོ། །
--- END BLOCKS ---
