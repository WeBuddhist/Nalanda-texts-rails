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
[Block 736 [VERSE]]
འཁོར་ལོའི་བདག་པོའི་བཟླས་པ་འབུམ། །
དཀྱིལ་འཁོར་བ་ཡི་དེ་བཞིན་ཁྲི། །

[Block 737]
ཞེས་བྱ་བ་ནི་སློབ་མས་ལན་གཉིས་ལན་གསུམ་གྱི་བར་དུ་གསོལ་བ་གདབ་པ་དང་། བསྙེན་པ་བྱ་སྟེ་བདག་མེད་མའི་ལེའུ་བརྒྱད་པ་ལྟར་རྫོགས་པར་བསྒོམས་ལ། མཆོད་བསྟོད་བདུད་རྩི་མྱང་བ་དང་རྫོགས་པའི་རིམ་པ་ཅུང་ཟད་བསྒོམ། ཟླ་བ་དང་ཆུ་ཟླ་ལྟ་བུའི་བསམ་གཏན་གྱི་སྒྲ་བརྙན་དང་བྲག་ཅ༌[^795]ལྟ་བུའི་བཟླས་པ་བྱ་སྟེ། །ཨོཾ་ཨ་ཨཱཿཧཱུཾ་ཕཊ་སྭཱ་ཧཱ་ཞེས་པ་རིམ་པ་ཀུན་ལ་སྦྱར་བ་ནི་རིམ་གྱིས་པའོ། །

[Block 738]
ཅིག་ཅར་བ་ནི་ཨོཾ་ཨ་ཨཱཿཞེས་པ་ལ་སོགས་པ་ཟངས་ཀྱིས་སྦྱར་ཏེ་ཧཱུཾ་ཕཊ་སྭཱ་ཧཱ་ཞེས་སྦྱར་ལ་བདག་མེད་མ་ལ་འབུམ་གཞན་ལ་ཁྲི་ཁྲི་བྱའོ། །དགྱེས་པའི་རྡོ་རྗེ་ལ་ནི་གོང་དུ་བསྟན་པ་དང་། འོག་ནས་འཆད་པ་དང་། །ཀུན་ལ་སྦྱོར་བ་གསུམ་མམ་ཡང་ན་ཡན་ལག་དྲུག་གི་རྣལ་འབྱོར་བྱས་ལ། དེ་ཝ་པི་ཙུའམ་ཨཥྚཱ་ན༌[^796]ན་འབུམ། བདག་མེད་མ་ལ་ཡང་། ཨོཾ་བཛྲ་ནཻ་རཱཏྨ་ཨོཾ་ཨཱཿཧཱུཾ་ཞེས་ཁྲི། ཨོཾ་བཛྲ་གཽ་རཱི་ཨོཾ་ཨཱཿཧཱུཾ་ཞེས་པ་ཀུན་ལ་ཁྲི་ཁྲིའོ། །གྲངས་ཀྱི༌[^797]བསྙེན་པ་བསྐྱལ་ལོ། །

[Block 739]
མཚན་མའི་བསྙེན་པ་འོག་ནས་རབ་མཐོང་སྔགས་ཀྱི་ཕ་རོལ་སོན་པ་སྟེ༌[^798]རབ་ཞལ་མཐོང་བ་དང་། ལུང་བསྟན་པ་དང་། རྨི་ལམ་གྱི་མཚན་མ་མ་བྱུང་བར་དུ་བྱའོ། །དུས་ཀྱི་བསྙེན་པ་འོག་ནས་ཟླ་དྲུག་གོམས་ཞེས་པ་ཟླ་དྲུག་གམ་ལོའམ། ཟླ་བ་གཅིག་གམ་ཐམ་ཚད་དུ་ཕྱིན་པའི་བར་དུ་བྱའོ། །དེ་ནས་དཀྱིལ་འཁོར་བྲི་བར་གསོལ་བ་གདབ་པའི་རྗེས་ལ་བསྒྲུབ་པ༌[^799]བསྟན་པའི་ཕྱིར་བདག་ཉིད་རྣལ་འབྱོར་པའོ། །དང་པོའི་ལ་ནི་མཆོག་གི་ལྷ་སྟེ་རྡོ་རྗེ་འཛིན་པའོ། །

[Block 740]
ཧཱུཾ་ལས་རྡོ་རྗེ་ཅན་དགྱེས་པའི་རྡོ་རྗེ༌[^800]བྱས་ཏེ་ནོར༌[^801]སྦྱང་བར་འབྲེལ་ཏེ། སའི་མཚན་ཉིད་བརྟག་པ་ཡང་བྱའོ། །ཕྱི་ནས་དཀྱིལ་འཁོར་བྲི་བ་ནི་དེ་དག་གི༌[^802]རྗེས་ལ་ཁས་ལེན་པའོ། །དེའི་རྗེས་ལ་གང་གིས་སྦྱང་ཞེ་ན། གོང་དུ་གསུངས་པའི་སྔགས་ཞེས་པ་ནི། ཨོཾ་རཀྵ་ལ་སོགས་པའོ། །མཁས་པས་འཛིན་པ༌[^803]སྦྱང་བ་ནི་ཕྱག་རྒྱ་དང་ཏིང་ངེ་འཛིན་ལ་མཁས་པས་ཀྱང་ངོ་། །གོང་གི་སྔགས་ནི་ཟང་ཟིང་གི་སྦྱིན་པས་རྒྱུད་ཚིམ་པ་བརྟག་པ་ཕྱི་མ་ལྟར་བྱས་ལ། ཨ་ཀཱ་རོ་མུ་ཁཾ་ལ་སོགས་པས་ཆོས་ཀྱི་སྦྱིན་པས་རྒྱུད་དག་པར་བྱས་པས་སོ། །དེ་ལ་གཏོར་མ་སྦྱིན་པ་ནི། ཕྱོགས་སྐྱོང་གི༌[^804]བདག་པོ་བཀུག་སྟེ་ཁྱད་པར་དུ་སའི་བདག་པོ་ལ་གཏོར་མ་དང་གཏེར་ཡང་གཞུག་པའོ། །དེའི་དོན་ནི་འདི་ཡིན་ཏེ།དང་པོ་རྣམ་བཅད་ས་གཞི་བཟུང་།[^805] །

[Block 741 [HEADING]]
#### དང་པོ་སའི་ཆོ་ག། ^1-10-1-0

[Block 742]
གཉིས་པ་སྟ་གོན་གནས་པར་བྱ། །ནུབ་གསུམ་པ་ལ༌[^806]འཇུག་པའོ། །ཞེས་གསུངས་པས་དང་པོ་སའི་ཆོ་ག་ནི་དོན་རྣམ་པ་དྲུག་སྟེ། ས་བརྟག་པ་དང་། ས་བསླང་བ་དང་། ས་སྦྱང་བ༌[^807]དང་། བྱིན་གྱིས་བརླབ་པ་དང་། གཟུང་བ་དང་། བསྲུང་བའོ། །

[Block 743 [HEADING]]
##### ས་བརྟག་པ། ^1-10-1-1-0

[Block 744]
དེ་ལ་ས༌[^808]བརྟག་པ་ནི་ཕྱིའི་བརྟག་པ་དང་། །ནང་གི་བརྟག་པའོ། །

[Block 745 [HEADING]]
###### ཕྱིའི་བརྟག་པ། ^1-10-1-1-1-0

[Block 746]
དེ་ལ་ཕྱིའི་གནས་ལ་བརྟག་པ་ནི་གོང་གི ཚལ་དང་སྐྱེ་བོ་མི་གནས༌[^809]དང་། །ཞེས་པར་འབྲེལ་ལོ། །ཕྱོགས་ལ་བརྟག་པ་ནི་དེ་རྣམས་ཀྱི་བྱང་དང་ཤར་གྱི་ཕྱོགས་སུའོ། །

[Block 747]
ཁ་དོག་དང་དབྱིབས་ལས་བརྟག་པ་ནི།

[Block 748 [VERSE]]
ཨུ་དུམྺཱ༌[^810]ར་ནྱ་གྲོ་ངྷ། །
ཨ་ཤཏྠ་དང་པ་ལ་ཤ །
བ་ཀུ་ལ་དང་ཨ་རྫུ་ནར། །
བཅས་པས་རུས༌[^811]སྦལ་རྒྱབ་འདྲ་བར། །
ས་ནི་དྲུག་པོ་སྤང་བར་བྱ། །

[Block 749]
ཞེས་གསུངས་པ་ཚ་སྒོ་ཅན་ལ་སོགས་པ་དང་། རོ་ཁུང་དུ་ཆུ་སོང་བ་འདྲ་བ་ལ་སོགས་པ་མཚན་མ་ངན་པ་རྣམས་སྤང་བར་བྱའོ། །

[Block 750 [HEADING]]
###### ནང་གི་བརྟག་པ། ^1-10-1-1-2-0

[Block 751]
ནང་གི་བརྟག་པ་ནི་བདེ་བར་གཤེགས་པ་ལ་མཆོད་པ་བྱས་ལ་གཏོར་མ་བཏང་སྟེ། ལྷག་པའི་ལྷའི་རྣལ་འབྱོར་ཙམ་གྱིས་ཉལ་བར་བྱའོ། །དེ་ལ་རྨི་ལམ་གྱི་མཚན་མ་ངན་ན་གཞན་དུ་འཕོའོ། །བཟང་ན་དེ་ཉིད་དུ་བྲི་བར་བྱའོ། །

[Block 752 [HEADING]]
##### ས་བསླང་བ། ^1-10-1-2-0

[Block 753]
བསླང་བ་ལ་གཉིས་ཏེ། མངོན་པ་ལ་བསླང་བ་དང་། མི་མངོན་པ་ལ་བསླང༌[^812]བའོ། །

[Block 754 [HEADING]]
###### མངོན་པ་ལ་བསླང་བ། ^1-10-1-2-1-0

[Block 755]
མངོན་པ་ནི༌[^813]རྒྱལ་པོའམ་ཞིང་བདག་ལ་ཚིག་དང་རིན་གྱིས་ཀྱང་ཉོ་བར་བྱའོ། །

[Block 756 [HEADING]]
###### མི་མངོན་པ་ལ་བསླང་བ། ^1-10-1-2-2-0

[Block 757]
མི་མངོན་པ་ལ་བསླང་བ་ནི་དེ་བཞིན་གཤེགས་པ་ལ་མཆོད་པ་བྱས་ཏེ། ས་བདག་ལ་ཨ་ཀཱ་རོས་གཏོར་མ་བྱིན་ལ་བསླང་བར་བྱའོ། །

[Block 758 [HEADING]]
##### ས་སྦྱང་བ། ^1-10-1-3-0

[Block 759]
ས་སྦྱང་བ་ནི་སྦྱང༌[^814]དགོས་པ་དང་མི་དགོས་པའོ། །

[Block 760]
སྦྱང་མི་དགོས་པ་ནི།

[Block 761 [VERSE]]
ཕྱུགས་ལྷས་དང་ནི་ཆུ་འགྲམ་དང་། །
རྡོ་ལེབ་དང་ནི་གཙུག་ལག་ཁང་། །

[Block 762]
དཀྱིལ་འཁོར་ཁང་པའི་ནང་དུ་ཡང་། ཡང་ཐོགས༌[^815]ལས་ཀྱི་སྦྱང་བ་མིན།[^816] །སྦྱང་བ་ལ་གསུམ་སྟེ།ལས་དང་བྱ་བས་སྦྱང་བ་དང་། །སྔགས་དང་ཕྱག་རྒྱས་སྦྱང་བ་དང་། །ཏིང་ངེ་འཛིན་གྱིས་སྦྱང་བའོ། །

[Block 763 [HEADING]]
###### ལས་དང་བྱ་བས་སྦྱང་བ། ^1-10-1-3-1-0

[Block 764]
ལས་དང་བྱ་བས་སྦྱང་བ་ནི། ལྟོ་འཕྱེའི་རིམ་པར་ཤེས་པར་བྱ་སྟེ། སྟོན་ཟླ་ཐ་ཆུངས༌[^817]ལ་སོགས་པ་ནས་བརྩམས་ནས་ཟླ་བ༌[^818]གསུམ་གསུམ་དུ།

[Block 765 [VERSE]]
ལྟོ་འཕྱེ་ལྷོ་དང་ནུབ་དང་ནི། །
[^819]ཤར་དང༌[^820]དེ་ཡི་མགོ་བོ་སྟེ། །
གཡོན་པའི་ཟུར་གྱིས་ཉལ་བ་ཡིན། །
དེ་ཡིས་ལྟོ་ཤེས་བྱས་ལ་བརྐོ། །

[Block 766 [VERSE]]
མགོ་དང་རྒྱབ་སོགས་ནས་བརྐོས་ནས། །
སྐྱོན་ནི་རྒྱས་པ་ལས་ཤེས་བྱ། །

[Block 767]
དེ་ཡང་།

[Block 768 [VERSE]]
ལྟེ་བ་ལྐོག་མ་པུས་ནུབ་ཙམ། །
ས་དེ་ཡོངས་སུ་བརྐོས་ནས་ནི། །
སླར་ཡང་ས་དེས་དགང་བར་བྱ། །
གལ་ཏེ་ལྷག་པར་གྱུར་ན་ནི། །
དངོས་གྲུབ་ཡོད་པར་སྟོན་པ་ཡིན། །

[Block 769]
དེ་ལྟར་བརྐོས་པས་སའི་མཚན་མ་ངན་པ་བྱུང་ན་བསལ་ལས་བཟང་པོས་བཀང་སྟེ། གཏེར་ཀྱང་གཞུག་གོ། །དེར་ཁྲུ་གང་ཙམ་གྱི་དོང་བྲུས་ཏེ་ཆུ་དང་མེ་ཏོག་བླུགས་ཏེ་ཕར་གོམ་པ་བརྒྱད་ཙམ་དུ༌[^821]འགྲོ་བར་བྱའོ། །ཆུ་དེ་ཤར་ནས་ནུབ་ཏུ་རྒྱུ་བ་དང་། །ལྷོ་ནས་བྱང་དུ་རྒྱུ་བ་དང་། གཡས་སུ་འཁོར་ཞིང་འཁྱིལ་ན་མཚན་མ་བཟང་བ་དང་ངན་པ་ཡང་ཤེས་པར་བྱའོ། །

[Block 770 [HEADING]]
###### སྔགས་དང་ཕྱག་རྒྱས་སྦྱང་བ། ^1-10-1-3-2-0

[Block 771]
སྔགས་དང་ཕྱག་རྒྱས་སྦྱང་བ་ནི་ལག་པ་གཡས་པ་རྡོ་རྗེ་རྩེ་གསུམ་པའི་ཕྱག་རྒྱ་བཅས་ལ། ས་ལ་བརྡབ་ཅིང་ཨོཾ་སརྦ་པཱ་བཾ་ད་ཧ་ན་མཱ་མ་རཀྵ་རཀྵ་ཧཱུཾ་ཕཊ་སྭཱ་ཧཱ་ཞེས་བརྗོད་དོ། །

[Block 772 [HEADING]]
###### ཏིང་ངེ་འཛིན་གྱིས་སྦྱང་བ། ^1-10-1-3-3-0

[Block 773]
ཏིང་ངེ་འཛིན་ནི་ས་གཞི་དེ་མི་དམིགས་པར་བསྒོམ་ཞིང་ཤིན་ཏུ་དག་པར་བསམ་མོ། །ཁ་ཅིག་ཏུ་ནི་ལས་དང་བྱ་བས་སྦྱང་ངོ་། །ཁ་ཅིག་ཏུ་ནི་སྔགས་དང་ཕྱག་རྒྱས་སྦྱང་ངོ་། །ཁ་ཅིག་ཏུ་ནི་ཏིང་ངེ་འཛིན་ཙམ་མོ། །དེ་དག་ནི་ཅི་རིགས་པར་ཤེས་པར་བྱའོ། །

[Block 774 [HEADING]]
##### བྱིན་གྱིས་བརླབ་པ། ^1-10-1-4-0

[Block 775]
དེ་ནས་བྱིན་གྱིས་བརླབ་པ་ནི་ཁཾ་ལས་ས་གཞི་སྟོང་པ་ཉིད་དུ་བསམ། ལཾ་ལས་གསེར་གྱི་ས་གཞི་ཆེན་པོར་བྱིན་གྱིས་བརླབ། སུཾ་ལས་རི་རབ་རིན་པོ་ཆེ་སྣ་བཞིའི་རང་བཞིན་དུ་བྱིན་གྱིས་བརླབ།[^822] ཧཱུཾ་ལས་ས་གཞི་རྡོ་རྗེར༌[^823]བྱིན་གྱིས་བརླབ།[^824] ཨོཾ་བཛྲ་མེ་དི་ནཱི་བཛྲི་བྷ་བ་བནྡྷ་ཧཱུཾ་ཞེས་བརྗོད་དོ། །རྡོ་རྗེའི་ས་གཞིའི་རང་བཞིན་ནམ་མཁའི་ཁམས་རྣམ་པར་དག་པར་བསམ་མོ། །
--- END BLOCKS ---
