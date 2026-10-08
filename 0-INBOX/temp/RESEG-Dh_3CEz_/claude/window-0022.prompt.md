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
[Block 771 [VERSE]]
དེ་དག་གང་གིས་བསྐྱེད་ཅེ་ན། །
ཧཱུཾ་གི་ཡི་གེ་འདོན་པའི་བདག །

[Block 772]
ཅེས་སྨོས་ཏེ། དེ་ལ་ཡང་ཚུལ་གཉིས་ཏེ། ཡུམ་ཡོད་པ་དང་མེད་པའོ། །

[Block 773]
ཡུམ་མེད་ན་སྙིང་གའི་ཧཱུཾ་ལས་ཡིག་འབྲུ་སྤྲོས་ཏེ། འཁོར་རྣམས་རྗེས་སུ་མཐུན་པའི་མངོན་པར་བྱང་ཆུབ་པ་ལྔས༌[^294]བསྐྱེད་དེ། ཡུམ་ཡོད་ན་རྗེས་སུ་ཆགས་པ་ཞུ་བ་ལས་རྒྱུའི་རྡོ་རྗེ་འཆང་བཞེངས་ནས་བསྒྲུབ་པ༌[^295]དང་བསྲུབ་པའི་སྦྱོར་བ་ལས་འཁོར་མངལ་སྐྱེས་ཀྱི་ཚུལ་དུ་རྗེས་སུ་མཐུན་པའི་མངོན་པར་བྱང་ཆུབ་པ་ལྔས་བསྐྱེད། [^296]སྔ་མ་ལྟར་ན་ཧཱུཾ་གི་ཡི་གེ་ལས་འདོན་བའི་བདག་ཅེས་བརྗོད་དོ། །

[Block 774]
ཕྱི་མ་ལྟར་ན་ཧཱུཾ་གི་ཡི་གེ་སྒྲོགས་པའི༌[^297]བདག་ཅེས་བརྗོད་དོ། །

[Block 775]
ཡུམ་ནི་མན་ངག་གིས་བདག་མེད་མ༌[^298]ལ་བཞེད་དོ། །

[Block 776]
དེ་ལ་སེམས་དཔའ་སུམ་བརྩེགས་བསྒོམ། ཡེ་ཤེས་ཀྱི་འཁོར་ལོ་དགུག་གཞུག་བྱ། སྐྱེ་མཆེད་བྱིན་གྱིས་བརླབ་པ་དང་སྐུ་གསུང་ཐུགས་ཀྱི་བྱིན་གྱིས་བརླབ་པ༌[^299]དང་། དབང་བསྐུར་བ་དང་མཆོད་པ་དང་བསྟོད་པ༌[^300]དང་བདུད་རྩི་མྱང་བའི་བར་དུ་བྱའོ། །

[Block 777]
རྫོགས་པའི་རིམ་པ་ཡང་ཅུང་ཟད་བསྒོམས་ཏེ།[^301] དག་པ་རྗེས་སུ་དྲན་པ་བྱ། སྔགས་བཟླས་གཏོར་མ་གཏང་། ཡེ་ཤེས་པ་གཤེགས་སུ་གསོལ། དམ་ཚིག་པ་རང་ལ་བསྡུ། སྤྱོད་ལམ་བྱ། ཐུན་བཞིའི་རིམ་པས་དེ་བཞིན་དུ་བསྒོམ། དུར་ཁྲོད་དུ་ནི་མགོན་པོ་རོལ། །ཞེས་པ་ནི། གང་གི་ཕྱིར་དུར་ཁྲོད་ཅེས༌[^302]བྱ་ཞེ་ན། དབུགས་རྒྱུ་ཞེས་པའི་རིམ་པ་ཡིས། རོ་ཞེས་མངོན་པར་བརྗོད་པར་བྱའོ། །

[Block 778]
རོ་གནས་པའི་རིགས་པ་སྟེ། སྔར་གྱི་རོ་ཆོས་ཀྱི་དབྱིངས་ལ་གནས་པ་དེ་དུར་ཁྲོད་དོ། །

[Block 779]
འདིས་ནི་ཁམས་གསུམ་པ་བདག་མེད་པ་ཡང་མཚོན་ཏོ། །

[Block 780]
སྤྱིར་མགོན་པོ་རོལ་པ་ནི་གསུམ་སྟེ། །ཐབས་ཀྱི༌[^303]རོལ་པ་དང་ཤེས་རབ་ཀྱི༌[^304]རོལ་པ་དང་དབྱེར་མེད་པའི་རོལ་པའོ། །

[Block 781 [VERSE]]
ཐབས་ནི་ཆོས་ཀྱི་འབྱུང་གནས་སོ། །
ཤེས་རབ་ནི་དུར་ཁྲོད་དེ་རོའོ། །

[Block 782]
དབྱེར་མེད་ནི་རྟེན་དང་རྟེན་མེད༌[^305]པའི་དཀྱིལ་འཁོར་རོ། །

[Block 783 [HEADING]]
#### གཞན་ལ་སྦྱར་བ། ^1-3-2-0

[Block 784]
གཞན་ལ་སྦྱར་བ་ནི་ཕྱག་བཞི་པ་དང་དྲུག་པ་སྟེ། དེ་ལ་ཡང་གཉིས་ཏེ།

[Block 785 [HEADING]]
##### དཔའ་བོ་གཅིག་པ། ^1-3-2-1-0

[Block 786 [VERSE]]
དཔའ་བོ་གཅིག་པ་དང་དཀྱིལ་འཁོར་གྱི་འཁོར་ལོའོ། །
དཔའ་བོ་གཅིག་པ་དང༌[^306]རྡོ་རྗེ་རྣམ་བཞིས་བསྐྱེད་དོ། །
ཕྱག་བཞི༌[^307]ནི་བདུད་བཞི་ལས་རྒྱལ་བ་ཞེས་སྦྱར་ཏེ།

[Block 787]
གཞན་ཐམས་ཅད་སྔ་མ་དང་འདྲའོ། །

[Block 788 [HEADING]]
##### དཀྱིལ་འཁོར་གྱི་འཁོར་ལོ། ^1-3-2-2-0

[Block 789]
དཀྱིལ་འཁོར་གྱི་འཁོར་ལོ་ནི་མངོན་པར་བྱང་ཆུབ་པ་ལྔ་ཡིས་རྡོ་རྗེ་འཆང་དུ༌[^308]བསྐྱེད། རྗེས་སུ་ཆགས་པས་ཞུ།

[Block 790 [VERSE]]
འཁོར་བསྐྱེད་པ་སྔ་མ་དང་འདྲའོ། །
ཕྱག་དྲུག་པ་ཡང་དེ་དང་འདྲའོ། །

[Block 791]
ཁམས་གསུམ་གྱི་རོ་མནན་པ་ཞེས་པ་ནི། ཁམས་གསུམ་ཀུན་དུ་བརྟགས་པ་སྟེ། མ་གྲུབ་པ་མཚོན། དཀྱིལ་འཁོར་གྱི་འཁོར་ལོ་ནི་གཞན་གྱི་དབང་སྟེ། ཀུན་བརྟགས་སྤོང་བའོ། །

[Block 792]
འདིས་ནི་ཆོས་ཀྱི་དབྱིངས་དང་དུར་ཁྲོད་ཀྱི་ཡང་གོང་གི་ཡང་མཚོན་པ་སྟེ་སྔ་མ་བཞིན་ནོ། །

[Block 793]
ལེའུ་གསུམ་པའོ།། །།

[Block 794 [HEADING]]
### བཞི་པ་འབྲས་བུ་རྫོགས་པ། ^1-4-0

[Block 795]
ལྷ་དབང་བསྐུར་བའི་ལེའུ་བཤད་པར་བྱ་ཞེས་པ་ནི།

[Block 796]
དང་པོ་ཡིན་ཡང་གཉིས་པར་ཤེས་པར་བྱ་སྟེ་ལྷ་རྣམས་ལ་ཞེས་བདུན་པར་སྦྱར་བ་དང་། ལྷ་རྣམས་ཀྱི་ཕྱིར་ཞེས་བཞི་པ་སྦྱར་བ་དང་། ལྷ་རྣམས་ཀྱི༌[^309]ཞེས་གསུངས་པར་ཡང་སྦྱར་རོ། །

[Block 797]
དབང་བསྐུར་བ་ནི་ཨ་བྷི་ཥིཉྩ་ཨ་བྷི་ཥེ་ཀ་ཏེ། དྲི་མ་འཁྲུད་པའམ་ནུས་པ་འཇོག་པས༌[^310]ན་དབང་ངོ་། །རང་གི་སྙིང་གར་ཞེས་པ་ནི་ཕྱག་གཉིས་པ་ལ་སོགས་པ་སྔ་མ་ལྟར་བསྐྱེད་པ་ལ་ཡེ་ཤེས་ཀྱི་འཁོར་ལོ་དང་དེ་གཅིག་ཏུ་བྱས་ནས་གཙོ་བོའི༌[^311]སྙིང་གར་རོ། །

[Block 798]
ས་བོན་བསམ་ཞེས་པ་ནི་ཧཱུཾ་ངམ་ཨཾ་ངོ་། དེའི་འོད་ཟེར་ལྕགས་ཀྱུའི་རྣམ་པའི་གཟུགས་ཞེས་པ་ནི་ཁ་དོག་དང་དབྱིབས་ཀྱི་རྣམ་པའོ། །

[Block 799]
དགུག་པའི་ཡོན་ཏན་དང་ལྡན་པས་སོ། །

[Block 800]
དེས་ཅི་བྱེད་ཅེ་ན་ཁམས་གསུམ་དུ་བཞུགས་པ་ལ་སོགས་པ་སྨོས་ཏེ། སྤྱན་དྲངས་པ༌[^312]ལ་རང་གི་སྙིང་ག་ནས་ལྷ་མོ་བརྒྱད་བཏོན༌[^313]ནས་མཆོད་པ་བྱ་སྟེ་གསོལ་བ་གདབ་པར་བྱའོ། །

[Block 801]
དེ་ནས་དེ་རྣམས་ཡོངས་སུ་གྱུར་ནས་དབང་བསྐུར་རོ། །

[Block 802]
དེས་ཅིར་གྱུར་ཞེ་ན། ཧེ་རུ་ཀ་ཡོངས་སུ་རྫོགས་པ་ཉིད་ཅེས་སོ། །

[Block 803]
དེ་ཡང་རྣམ་པར་བསྒོམ་པ་དང་བྱིན་གྱིས་བརླབས་པ༌[^314]བསྒོམ་ཞེས་པ་ནི་སྒྲུབ་ཐབས༌[^315]ལས་འབྱུང་བ་བཞིན་དུ་ཡན་ལག་དྲུག་དང་། ཏིང་ངེ་འཛིན་གསུམ་མམ། ཡང་ན་རྣམ་པར་བསྒོམ་པ་ནི་བསྐྱེད་པ༌[^316]དང་། བསྐྱེད་པའི༌[^317]རིམ་པ་ཡིན་ལ། བྱིན་གྱིས་བརླབས་པའི༌[^318]སྒོམ་པ་ནི་རྫོགས་པ་དང་ཡོངས་སུ་རྫོགས་པའི་རིམ་པའོ། །

[Block 804]
ཐུན་གསུམ་ཞེས་པ་ནི་ཉིན་གཅིག་ལའོ། །

[Block 805]
ལངས་ཏེ་ཞེས་པ་ནི་གཙོ་བོའི་ང་རྒྱལ་གྱིས་སོ། །

[Block 806]
ལྷའི་གཟུགས་སུ་གནས་སོ་ཞེས་བྱ་བ་འདིས༌[^319]ནི་རྫོགས་པའི་རིམ་པའི་སྤྱོད་ལམ་ཡང་གཟུང༌[^320]སྟེ།

[Block 807 [VERSE]]
དེ་གཉིས་ཀ་ཡང་འོག་ནས་འཆད་དོ། །
ལེའུ་བཞི་པ་སྟེ་སྔ་མ་བཞིན་ནོ།། །།

[Block 808 [HEADING]]
### ལྔ་པ་རྫོགས་པའི་རིམ་པའི་ལྷ་བསྒོམ། ^1-5-0

[Block 809]
དེ་ནས་ཞེས་པ་ནི་བསྐྱེད་པའི་རིམ་པའི་རྗེས་ཐོགས་ལའོ། །

[Block 810]
དེ་ཁོ་ན་ཉིད་ཀྱི་ལེའུ་རྫོགས་པའི་རིམ་པ་བཤད་པར་འདོད་ནས་བཤད་པར་བྱའོ་ཞེས་མཚམས་སྦྱར་བའོ། །
--- END BLOCKS ---
