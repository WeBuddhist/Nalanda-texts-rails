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
[Block 1786 [VERSE]]
ང་ནི་དཔལ་ལྡན་རྡོ་རྗེ་འཆང་། །
ཉོན་ཅིག་བར་ཆད་བགེགས་ཀྱི་ཚོགས། །
སྲུང་བའི་འཁོར་ལོའི་སྦྱོར་བ་ཡིས། །
ལུས་ངག་ཡིད་ལ་གནོད་པ་རྣམས། །

[Block 1787]
འདིར་ནི་འཇིགས༌[^832]འཇོམས་གཞན་དུ་མིན། །ཞེས་རྡོ་རྗེའི་གནས་སུ་འཁོར་ལོ་དང་རིན་པོ་ཆེ་དང་། པདྨ་དང་རལ་གྲི༌[^833]སྦྱར་ལ་ཚིགས་སུ་བཅད་པ་ལྔ་སྦྱར་གྱིས༌[^834]བསྐྲད་པར་བྱའོ། །

[Block 1788 [HEADING]]
###### རྡོ་རྗེ་འགྲོས་ཀྱིས་བསྲུང་བ། ^1-10-1-6-4-0

[Block 1789]
རྡོ་རྗེ་འགྲོས་ཀྱིས༌[^835]བསྐྲད་པ་ནི་རྡོ་རྗེ་རྩེ་གཅིག་པ་དང་རྩེ་གསུམ་པ་དང་། སྣ་ཚོགས་རྡོ་རྗེའི་འགྲོས་ཀྱིས་དཀྱིལ་འཁོར་བསྐོར་ཞིང་བསྲུང་བར་བྱའོ། །

[Block 1790 [HEADING]]
###### སྟང་སྟབས་ཀྱིས་བསྲུང་བ། ^1-10-1-6-5-0

[Block 1791]
སྟང་སྟབས་ཀྱིས༌[^836]བསྲུང་བ་ནི་གཡས་བརྐྱང་དང་ནི་གཡོན་བརྐྱང་དང་། ས་ག་དང་ནི་ཟླུམ་པོ་དང་། །མཉམ་པའི་འདུག་སྟངས་རྣམ་པ་ལྔ། ཤར་ནས་བརྩམས་ཏེ་དབུས་ཀྱི་བར་དུ་བསྡུས་ནས་རྣམ་པ་ལྔ་པོ་བྱ། རྒྱས་པར་འདོད་ན་སྟང་སྟབས་ནི་དྲུག་ཅུ་རྩ་གཅིག་ལ་སོགས་ཏེ་སྒྱུ་འཕྲུལ་དྲ་བའི་ཚུལ་དུ་བྱ།

[Block 1792 [HEADING]]
###### རྡོ་རྗེ་ཕུར་པས་བསྲུང་བ། ^1-10-1-6-6-0

[Block 1793]
རྡོ་རྗེ་ཕུར་པས་བསྲུང་བ་ནི་ཕུར་བུ་རྣམ་པ་ལྔ། སྟོད་ཁྲོ་བོའི་རྣམ་པ་སྨད་ཕུར་བུ་རྩེ༌[^837]གཅིག་པར་བསྐྱེད་ལ། ཕུར་པའི་སྔགས་བརྒྱ་རྩ་བརྒྱད་བཟླས་ཏེ། །གྷ་གྷ་གྷཱ་ཏའི་སྔགས་ཀྱིས༌[^838]ཕྱོགས་བཞི་དབུས་དང་ལྔར་གདབ་པར་བྱའོ། །

[Block 1794 [HEADING]]
#### སྟ་གོན་གྱི་ཆོ་ག། ^1-10-2-0

[Block 1795]
སྟ་གོན་གྱི་ཆོ་ག་ནི་འོག་ནས་ཤེས་པར་བྱའོ། །

[Block 1796 [HEADING]]
#### ནུབ་གསུམ་པ་ལ་འཇུག་པ། ^1-10-3-0

[Block 1797]
དེའི་རྗེས་ལ་ཐིག་བྲི་བའི་ཕྱིར་ཐིག་སྐུད་སར་པ་ནི་གཞན་དུ་ལོངས་མ་སྤྱད་པའོ། །

[Block 1798]
ཚད་ནི་ཉིས༌[^839]འགྱུར་དང་ཉི་ཤུ་ཆའོ། །

[Block 1799]
མཛེས་པ་ནི་དྲི་ཞིམ་པོའི་སྣོད་ཀྱིས་མཛེས་པའོ། །

[Block 1800]
རང་འདོད་ལྷའི་གཟུགས་ཀྱིས༌[^840]ནི་དགྱེས་པའི་རྡོ་རྗེ་དང་གྲོགས་བདག་མེད་མའམ་གཽ་རཱིས་སོ། །ཤེས་རབ་ཅན་གྱིས་གདབ་པ་ནི༌[^841]ལས་དང་བྱ་བ་ལ་མཁས་པས་སའི་ཆ་དབྱེ་བ་ལས་མ་འདས་པའོ། །

[Block 1801 [HEADING]]
##### ཐིག་སྒྲུབ་པའི་ཆོ་ག། ^1-10-3-1-0

[Block 1802]
དེ་ལ་ཐིག་སྒྲུབ་པའི་ཆོ་ག་ནི་རས་བལ་རིན་ལ་མ་རྩེགས་པར༌[^842]ཉོས་ལ། ཁྱེའུ་དང་བུ་མོ་གཞོན་ནུ་མས་བཀལ་ཏེ། སྲད་བུ༌[^843]ལྔ་ཁ་དོག་སོ་སོར་བསྒྱུར་ནས་སྣོད་གཙང་མའི་ནང་དུ་ཕྱོགས་སོ་སོར་བཞག་སྟེ། བྷྲཱུཾ་ཨཱཾ་ཛྲཱིཾ་ཁཾ་ཧཱུཾ་བཀོད་ལ་དེ་བཞིན་གཤེགས་པ་ལྔར་བསྐྱེད། རང་བཞིན་པ་སྤྱན་དྲངས་ལ་བསྟིམ། ཨ་ནྱོ་ནྱ་ཨ་ནུ་ག་ཏ་ལ་སོགས་པས་བཟླས་ལ་བསྒྲིལ་བར་བྱའོ། །

[Block 1803]
དེ་ལ་མཆོད་པ་ལྔས་མཆོད། །ཐིག་སྒྲུབ་པའི་རིམ་པའོ། །

[Block 1804]
དེ་ནས་བདག་ཉིད་གྲོགས༌[^844]དང་བཅས་པས༌[^845]ཡེ་ཤེས་ཀྱི་ཐིག་གདབ་པ་དང་ལས་ཀྱི་ཐིག་གདབ་པར་བྱའོ། །

[Block 1805]
དེས་ཅིར་འགྱུར་ཞེ་ན། འོག་ནས་སྟོན་པས་དཀྱིལ་འཁོར་འདི་སྐད་གསུངས་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1806]
དེའི་རྗེས་ལ་ཚོན་བསྟན་པར་བྱ་བའི་ཕྱིར། རྡུལ་ཚོན་དམ་པའི་ཚོན་དང་ནི་རིན་ཆེན་ལྔའི་ཕྱི་མར་འབྲེལ་ལོ། །

[Block 1807]
ཡང་འབྲིང་པོ་ནི་ཡང་ན་འབྲས་བུ་ལ་སོགས་པར་འབྲེལ་ལོ། །

[Block 1808]
ཐ་མ་ནི་སོ་ཕག་དང་ས་ལ་སོགས་པའི་ཚོན་ཏེ་བརྟག་པ་ཕྱི་མར་ཤེས་པར་བྱའོ། །

[Block 1809 [HEADING]]
##### ཚོན་སྒྲུབ་པ། ^1-10-3-2-0

[Block 1810]
ཚོན་སྒྲུབ་པ་ནི་ཚོན་རྩི་ཁ་དོག་ལྔ་ཕྱོགས་སོ་སོར་བཞག་ལ་སྔར་གྱི་ཡིག་འབྲུ་ལྔ་ཡིས་དེ་བཞིན་གཤེགས་པ་ལྔར་བསྐྱེད་རང་བཞིན་པ་བསྟིམ། མཆོད་པ་རྣམ་པ་ལྔས་མཆོད། བཛྲ་ས་མ་ཡའི་སྔགས་བཟླས་ལ་ཚོན་རྩི་སྤར་རོ། །

[Block 1811]
གཟི་བསྐྱེད་དེ་དབང་ལྡན་གྱི༌[^846]མཚམས་ནས་ཚིགས་སུ་བཅད་པ་རེ་བརྗོད་ཅིང་མཐོ་གང་ཙམ་དྲང་བར་བྱའོ། །

[Block 1812]
དེ་ཡང་།

[Block 1813 [VERSE]]
དཀར་པོ་སེར་པོ་དམར་པོ་ལྗང་། །
མཐིང་ག་ནང་དུ་ཤེས་བྱ་སྟེ། །
འདི་ནི་ཚོན་གྱི་རིམ་པར་བཤད། །
དེ་བཞིན་ཕྱོགས་ཀྱང་ཤེས་པར་བྱ། །

[Block 1814]
དེའི་རྗེས་ལ་དཀྱིལ་འཁོར་གྱི་མཚན་ཉིད་བསྟན་པའི་ཕྱིར་སྟོན་པ་ཞེས་པ་ལ་སོགས་པ་གསུངས་ཏེ། སྟོན༌[^847]པ་གཞན་དག་ཀྱང་ངོ་། །

[Block 1815 [VERSE]]
ཡང་ན་སྡུད་པར་བྱེད་པ་ཁས་ལེན་པའོ། །
དཀྱིལ་འཁོར་འདི་སྐད་གསུངས་པ་ནི། །
གཞན་དག་དང་འདྲ་བས་འདིར་ཡང་འདོད་པའོ། །
དེ་ཡང་ཚིགས་བཅད་གཉིས་ཏེ་གོ་སླའོ། །

[Block 1816]
དེའི་རྗེས་ལ་དཀྱིལ་འཁོར་ཁྱད་པར་བྱ་བ་མཚན་མ་དགོད་པའི་ཕྱིར། འཕར་མ་གཉིས་བཟང་ལ་སོགས་པ་ཚིགས་སུ་བཅད་པ་གཉིས་ཏེ་གོ་སླའོ། །

[Block 1817]
དེའི་རྗེས་སུ་བུམ་པ་ལ་སོགས་པ་རྫས་དགོད་ཅིང་འབྲེལ་བ་བསྟན་པའི་ཕྱིར་བུམ་པ་བརྒྱད་ལ་སོགས་པ་ནི་བཅུ་སྟེ། རྣམ་པར་རྒྱལ་བ་དང་ལས་ཐམས་ཅད་པའོ། །

[Block 1818]
འདིར་ནི་བུམ་པ་རྒྱས་པ་ནི་བཅུ་དྲུག་སྟེ། ལྷ་མོ་བཅོ་ལྔ་ལ་བུམ་པ་རེ་རེ།

[Block 1819 [VERSE]]
ལས་ཐམས་ཅད་པ་དང་བཅུ་དྲུག་གོ། །
དཔལ་དགྱེས་པ་རྡོ་རྗེ་ལ་ནི་བུམ་པ་བཅུའོ། །

[Block 1820]
བསྡུ་བ་ནི་དྲུག་ཏུ་ཤེས་པར་བྱ་སྟེ། རིགས་ལྔ་ལ་རེ་རེ་ལས་ཐམས་ཅད་པ་དང་དྲུག་གོ། །

[Block 1821]
གང་བའི་བུམ་པ་ནི་ངེས་པ་མེད་དེ་ཅི་འབྱོར་པ་དབུལ་བར་བྱའོ། །

[Block 1822]
རྣམ་པར་རྒྱལ་བ་ཤར་དུ་བཀོད་པ་ནི་བུམ་པ༌[^848]སྟེ། གཙོ་བོའི་མདུན་ནས་ཤར་དུའོ། །

[Block 1823]
ལས་ཐམས་ཅད་པའི་བུམ་པ་ནི་ཤར་གྱི་སྒོར་རོ། །

[Block 1824]
གཞན་དག་གོ་སླའོ། །

[Block 1825]
དེའི་རྗེས་ལ་ཇི་ལྟར་བསམ་གཏན་དེ་བཞིན་འདིར་ནི་དམ་ཚིག་གི་འཁོར་ལོ་སྒྲུབ་ཐབས་ལྟར་བསྐྱེད་པའོ། །
--- END BLOCKS ---
