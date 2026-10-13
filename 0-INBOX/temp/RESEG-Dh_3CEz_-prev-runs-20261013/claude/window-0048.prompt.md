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
[Block 1681]
དེའི་ཕྱིར་དྲི་མེད་ཅེས་བྱ་བ་ལ་སོགས་པ་སྦྱར་ཏེ། ལྷའི་རྣམ་པར་མོས་པའོ། །

[Block 1682]
ཐམས་ཅད་རྣམ་པར་དག་ཅེས་པ་ནི་སྒྱུ་མ་ཡོངས་སུ་དག་པ་སྟེ། དེ་ཡོངས་སུ་ཤེས་པས་འགྲོ་བ་གྲོལ་བར་ཤེས་པའོ། །

[Block 1683]
ལེའུ་དགུ་པའོ།། །།

[Block 1684 [HEADING]]
### བཅུ་པ་རིམ་པ་གཉིས་དབང་ལམ་དུ་བྱེད་པས་རྒྱུད་ལ་སྐྱེ་བ། ^1-10-0

[Block 1685]
དེ་ནས་ནི་བདག་དོན་དག་པ་དང་ལྡན་པའི་རྗེས་ལ། གཞན་དོན་བསྟན་པའི་ཕྱིར་ཇི་ལྟར་དཀྱིལ་འཁོར་ཞེས་པ་ནི་རྡུལ་ཚོན༌[^788]ནོ། །

[Block 1686]
རིམ་པ་ཞེས་པ་ནི་སའི་ཆ་དབྱེ་བ་ལ་སོགས་པའོ། །

[Block 1687]
ཡང་དག་བཤད་ནི་སྡུད་པར་བྱེད་པ་ཁས་ལེན་པ་སྟེ། མ་ནོར་བའམ་གཞན་དོན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1688]
ཡང་གང་གིས་ཞེས་པ་ནི་ཇི་ལྟ་བ་བཞིན་ཏེ་དེ་ཁོ་ན་དྲིས་པའོ། །

[Block 1689]
སློབ་མ་ནི་དམ་ཚིག་དང་སྡོམ་པར་ལྡན་པའོ། །

[Block 1690]
དབང་བསྐུར་བ་ནི་རྒྱུད༌[^789]བརླན་པར་བྱེད་ཅིང་འཁྲུ་བ་སྟེ་ཞིང་ས་ཆུས་བརླན་པ་ལྟ་བུའོ། །

[Block 1691]
ཆོ་ག་ནི་ཐབས་ཀྱི་རིམ་པའོ། །

[Block 1692]
རབ་ཏུ་བཤད་པ་ནི་ཡང་དག་པ་ལས་བསྟན་པ༌[^790]སྟེ་སྡུད་པར་བྱེད་པ་ཁས་ལེན་པའོ། །

[Block 1693]
དེའི་རིམ་པ་ཅི་ཞེ་ན། དེ་དག་གི་གོ་རིམས༌[^791]ཀྱང་བླ་མ་ལ་རག་ལས་པར་བྱ་བའི་ཕྱིར་དཀྲུགས་ནས་བསྟན༌[^792]པའོ། །

[Block 1694]
དེ་ཡང་དང་པོ་གནས་བསྟན་པའི་ཕྱིར་ཚལ་ནི་ནགས་སམ་སྐྱེད་ཤིང༌[^793]གི་ར་བའོ། །

[Block 1695]
དབེན་པ་ནི་ཚལ་དེ་ཉིད་ལ་བྱ་བའམ༌[^794]དགོན་པའམ་བས་མཐའོ། །

[Block 1696]
ཡང་ན་སྐྱེ་བོ་མི་འདུ་བ་གང་ཡང་རུང་བའོ། །

[Block 1697]
བྱང་ཆུབ་སེམས་དཔའི་ཁྱིམ་ནི་རྣལ་འབྱོར་པའམ་རྒྱལ་པོ་ལ་སོགས་པ་སྙིང་རྗེ་དང་ལྡན་པའོ། །

[Block 1698]
ཡང་གཙུག་ལག་ཁང་སྟེ་པོ་ཏི་གླེགས་བམ་གནས་པའོ། །

[Block 1699]
དེའི་བདག་པོ་བྱང་ཆུབ་སེམས་དཔའ་ཡིན་པའི་ཕྱིར། དཀྱིལ་འཁོར་ཁང་པ་ནི་སྒྲུབ་པའི་གནས་སམ་ལྷ་ཁང་ངོ་། །དཀྱིལ་འཁོར་བཞེངས་པ་ནི་བསྙེན་པ་དང་འབྲེལ་པའི་ཚེ་མཎྜལ་བྲི་བ་དང་དམ་ཚིག་བསྒོམ་པ་ཡིན་ལ། སྒྲུབ་པ་འཕེལ་བའི་ཚེ་དཀྱིལ་འཁོར་ཁང་པ་ཡང་ཚལ་ལ་སོགས་པ་དང་ལྡན་པ། དཀྱིལ་འཁོར་གྱི་དོན་དུ་ཁང་པ་བརྩིགས་པ་དང་དཀྱིལ་འཁོར་མཆོག་ནི་བྲི་བའོ། །

[Block 1700]
དེའི་རྗེས་ལ།

[Block 1701 [VERSE]]
འཁོར་ལོའི་བདག་པོའི་བཟླས་པ་འབུམ། །
དཀྱིལ་འཁོར་བ་ཡི་དེ་བཞིན་ཁྲི། །

[Block 1702]
ཞེས་བྱ་བ་ནི་སློབ་མས་ལན་གཉིས་ལན་གསུམ་གྱི་བར་དུ་གསོལ་བ་གདབ་པ་དང་། བསྙེན་པ་བྱ་སྟེ་བདག་མེད་མའི་ལེའུ་བརྒྱད་པ་ལྟར་རྫོགས་པར་བསྒོམས་ལ། མཆོད་བསྟོད་བདུད་རྩི་མྱང་བ་དང་རྫོགས་པའི་རིམ་པ་ཅུང་ཟད་བསྒོམ། ཟླ་བ་དང་ཆུ་ཟླ་ལྟ་བུའི་བསམ་གཏན་གྱི་སྒྲ་བརྙན་དང་བྲག་ཅ༌[^795]ལྟ་བུའི་བཟླས་པ་བྱ་སྟེ། །ཨོཾ་ཨ་ཨཱཿཧཱུཾ་ཕཊ་སྭཱ་ཧཱ་ཞེས་པ་རིམ་པ་ཀུན་ལ་སྦྱར་བ་ནི་རིམ་གྱིས་པའོ། །

[Block 1703]
ཅིག་ཅར་བ་ནི་ཨོཾ་ཨ་ཨཱཿཞེས་པ་ལ་སོགས་པ་ཟངས་ཀྱིས་སྦྱར་ཏེ་ཧཱུཾ་ཕཊ་སྭཱ་ཧཱ་ཞེས་སྦྱར་ལ་བདག་མེད་མ་ལ་འབུམ་གཞན་ལ་ཁྲི་ཁྲི་བྱའོ། །

[Block 1704]
དགྱེས་པའི་རྡོ་རྗེ་ལ་ནི་གོང་དུ་བསྟན་པ་དང་། འོག་ནས་འཆད་པ་དང་། །ཀུན་ལ་སྦྱོར་བ་གསུམ་མམ་ཡང་ན་ཡན་ལག་དྲུག་གི་རྣལ་འབྱོར་བྱས་ལ། དེ་ཝ་པི་ཙུའམ་ཨཥྚཱ་ན༌[^796]ན་འབུམ། བདག་མེད་མ་ལ་ཡང་། ཨོཾ་བཛྲ་ནཻ་རཱཏྨ་ཨོཾ་ཨཱཿཧཱུཾ་ཞེས་ཁྲི། ཨོཾ་བཛྲ་གཽ་རཱི་ཨོཾ་ཨཱཿཧཱུཾ་ཞེས་པ་ཀུན་ལ་ཁྲི་ཁྲིའོ། །

[Block 1705]
གྲངས་ཀྱི༌[^797]བསྙེན་པ་བསྐྱལ་ལོ། །

[Block 1706]
མཚན་མའི་བསྙེན་པ་འོག་ནས་རབ་མཐོང་སྔགས་ཀྱི་ཕ་རོལ་སོན་པ་སྟེ༌[^798]རབ་ཞལ་མཐོང་བ་དང་། ལུང་བསྟན་པ་དང་། རྨི་ལམ་གྱི་མཚན་མ་མ་བྱུང་བར་དུ་བྱའོ། །

[Block 1707]
དུས་ཀྱི་བསྙེན་པ་འོག་ནས་ཟླ་དྲུག་གོམས་ཞེས་པ་ཟླ་དྲུག་གམ་ལོའམ། ཟླ་བ་གཅིག་གམ་ཐམ་ཚད་དུ་ཕྱིན་པའི་བར་དུ་བྱའོ། །

[Block 1708]
དེ་ནས་དཀྱིལ་འཁོར་བྲི་བར་གསོལ་བ་གདབ་པའི་རྗེས་ལ་བསྒྲུབ་པ༌[^799]བསྟན་པའི་ཕྱིར་བདག་ཉིད་རྣལ་འབྱོར་པའོ། །

[Block 1709]
དང་པོའི་ལ་ནི་མཆོག་གི་ལྷ་སྟེ་རྡོ་རྗེ་འཛིན་པའོ། །

[Block 1710]
ཧཱུཾ་ལས་རྡོ་རྗེ་ཅན་དགྱེས་པའི་རྡོ་རྗེ༌[^800]བྱས་ཏེ་ནོར༌[^801]སྦྱང་བར་འབྲེལ་ཏེ། སའི་མཚན་ཉིད་བརྟག་པ་ཡང་བྱའོ། །

[Block 1711]
ཕྱི་ནས་དཀྱིལ་འཁོར་བྲི་བ་ནི་དེ་དག་གི༌[^802]རྗེས་ལ་ཁས་ལེན་པའོ། །

[Block 1712]
དེའི་རྗེས་ལ་གང་གིས་སྦྱང་ཞེ་ན། གོང་དུ་གསུངས་པའི་སྔགས་ཞེས་པ་ནི། ཨོཾ་རཀྵ་ལ་སོགས་པའོ། །

[Block 1713]
མཁས་པས་འཛིན་པ༌[^803]སྦྱང་བ་ནི་ཕྱག་རྒྱ་དང་ཏིང་ངེ་འཛིན་ལ་མཁས་པས་ཀྱང་ངོ་། །གོང་གི་སྔགས་ནི་ཟང་ཟིང་གི་སྦྱིན་པས་རྒྱུད་ཚིམ་པ་བརྟག་པ་ཕྱི་མ་ལྟར་བྱས་ལ། ཨ་ཀཱ་རོ་མུ་ཁཾ་ལ་སོགས་པས་ཆོས་ཀྱི་སྦྱིན་པས་རྒྱུད་དག་པར་བྱས་པས་སོ། །

[Block 1714]
དེ་ལ་གཏོར་མ་སྦྱིན་པ་ནི། ཕྱོགས་སྐྱོང་གི༌[^804]བདག་པོ་བཀུག་སྟེ་ཁྱད་པར་དུ་སའི་བདག་པོ་ལ་གཏོར་མ་དང་གཏེར་ཡང་གཞུག་པའོ། །

[Block 1715]
དེའི་དོན་ནི་འདི་ཡིན་ཏེ།

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
--- END BLOCKS ---
