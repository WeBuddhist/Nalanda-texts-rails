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
[Block 981]
ལེའུ་ནི༌[^431]སྔ་མ་བཞིན་ཏེ་ཡས་བགྲངས་པའི་ལྔ་པའོ།། །།

[Block 982 [HEADING]]
### དྲུག་པ་སྤྱོད་པ། ^1-6-0

[Block 983]
དེ་ནས་ཡང་དག་བཤད་པར་བྱ། །ཞེས་པ་ནི་ལྟ་བ་དང་སྒོམ་པའི་རྗེས་སུ་འབྲས་བུ་སྤྱོད་པས་མཐར་ཕྱིན་པ་བཤད་པའོ། །

[Block 984 [VERSE]]
དེ་ཡང་སྤྱོད་པ་ནི་ཙརྱ་སྟེ་ཙརྱ༌[^432]ནི་རྒྱུ་བའོ། །
ཡ་ཡོ་གི་ནི་རྣལ་འབྱོར་མར༌[^433]སྦྱོར་བའོ། །

[Block 985]
དེས་ཅིར་འགྱུར་ཞེ་ན།

[Block 986 [VERSE]]
གནས་དག་ཏུ་རྒྱུ་ཞིང་སྦྱོར་བའམ། །
རྣལ་འབྱོར་གྱི༌[^434]རྣམ་པར་རྒྱུ་བའོ། །

[Block 987 [HEADING]]
#### རྫོགས་པའི་རིམ་པའི་སྤྱོད་པ། ^1-6-1-0

[Block 988]
སྤྱོད་པ་འདི་ཡང་བསྐྱེད་པའི་རིམ་པས་བརྟག་པ་ཕྱི་མར་སྟོན་ལ། །འདི་རྫོགས་པའི་རིམ་པ་སྟེ་དེ་ཡང་གཞན་ལུས་ཤེས་རབ་ལ་བརྟེན་པ་གསང་བའི་སྤྱོད་པ་དང་། རང་ལུས་ཐབས་ལ་བརྟེན་པ་ཅུང་ཟད་སྨྱོན་པ་བརྟུལ་ཞུགས་ཀྱི་སྤྱོད་པ་དང་། ཕྱག་རྒྱ་ཆེན་པོ་ལ་བརྟེན་པ་སྨྱོན་པའི་བརྟུལ་ཞུགས་མཆོག་ཏུ་གསང་བའི་སྤྱོད་པའོ། །

[Block 989]
དེ་དག་གི༌[^435]དགོས་པ་ནི་སྤྱོད་མཆོག་ཕ་རོལ་ཕྱིན་པ་སྟེ། ཕ་རོལ་ཏུ༌[^436]ཕྱིན་པའི་ཐུན་མོང་ངོ་། །མཆོག་ནི་ཐུན་མོང་མ་ཡིན་པ་སྟེ། དེས་ན་དངོས་གྲུབ་མཐར་འགྲོ་བ་སྟེ། ཕ་རོལ་ཏུ་ཕྱིན་པ་ལས་གྲུབ༌[^437]མཐའ་སྟེ།

[Block 990 [VERSE]]
སྣང་བ་སྟོང་པ་དབྱེར་མེད་པར་རྟོགས༌[^438]པའོ། །
དགྱེས་པའི་རྡོ་རྗེའི་དངོས་གྲུབ་ཀྱི་རྒྱུར་རོ། །

[Block 991]
གྲུབ་པའི་མཐུར་འགྲོ་བའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་བསྐྱེད་པའི་རིམ་པ་ལས་སོ་ཞེས་ཐུན་མོང་མ་ཡིན་ཞེ་ན། དགྱེས་པའི་རྡོ་རྗེའི་དངོས་གྲུབ་ཀྱི་རྒྱུས་ཏེ།

[Block 992 [VERSE]]
མཆོག་གི་དངོས་གྲུབ་མཐར་ཐུག་པ་ཐོབ་པའོ། །
དེ་ནི་གསང་བ་ལ་སོགས་པའི་ཐུན་མོང་ངོ་། །

[Block 993 [HEADING]]
##### གཞན་ལུས་ཤེས་རབ་ལ་བརྟེན་པ་གསང་བའི་སྤྱོད་པ། ^1-6-1-1-0

[Block 994]
སྒོམ་པ་པོ་ལ་སོགས་པ་ཚིགས་བཅད་གཉིས་དང་། ཚིག་རྐང་པ་གཅིག་གིས་གསང་བའི་སྤྱོད་པའི་ཆ་ལུགས་ཙམ་སྟེ། རུས་པའི་རྒྱན་ཆ་རྣམས་ཀྱིས་བཟང་བའོ། །

[Block 995]
དེའི་དགོས་པ་དང་རྣམ་པར་དག་པ་ནི་གོ་སླའོ། །

[Block 996]
ཧེ་རུ་ཀ་སྦྱོར་སྐྱེས་བུ་ཉིད་ནི་རྫོགས་པའི་རིམ་པའི་ཉམས་ཀྱིས་སྤྱོད་པ་བྱེད་ཀྱང་བསྐྱེད་པའི་རིམ་པ་ཉུང་ལྡན་གྱི་ང་རྒྱལ་གྱིས་གནས་པ་སྟེ། དེའི་ཡོན་ཏན་ནི་རིགས་ལྔ་དག་གི༌[^439]ལ་སོགས་པ་སྟེ་གོ་སླའོ། །

[Block 997]
དེ་ཡང་གསང་བའི་སྤྱོད་པའི་ཐུན་མོང་མ་ཡིན་པའི་གནས་ནི༌[^440]ཤིང་གཅིག་ལ་སོགས་པ་སྟེ། ཤིང་གཅིག་ནི་ཤིང་གཞན་གྱི་གྲིབ་མས་མ་ཕོག་པའོ། །

[Block 998]
དུར་ཁྲོད་ནི་རོ་མང་པོ་གནས་པའོ། །

[Block 999]
མ་མོའི་ཁྱིམ་ནི་འཇིག་རྟེན་ན་གྲགས་པ་མ་མོ་བདུན་གྱི༌[^441]གནས་སོ། །

[Block 1000]
མཚན་མོ་ནི་དུས་མཚན་མ་རྒྱུ་བའི་གནས་སོ། །

[Block 1001 [VERSE]]
དབེན་པ་ནི་སྐྱེ་བོ་ཉུང་བའོ། །
བས་མཐའ་ནི་དགོན་པའི་ཚད་དེ།

[Block 1002]
རྒྱང་གྲགས་གཅིག་གམ་མཚོའི་ཀློང་ངམ་སྒྲིབ༌[^442]གཡོགས་ཀྱིས་ཆོད་པའོ། །

[Block 1003]
དེ་ནི་ཕྱེ་སྟེ་བསྐྱེད་པའི་རིམ་པ་དང་ཐུན་མོང་ངོ་། །འདིར་བསྐྱེད་པའི་རིམ་པ་ལ་བརྟེན་ནས་གནས་དང་སྤྱོད་པ་སྟོན་པ་ཡིན་ན་ཕྱག་རྒྱ་མོ་དང་རྩ་རླུང་དང་རྫོགས་རིམ་ལ་འབྲེལ་བ་ཡོད་དོ་ཞེ་ན། དེ་བདེན་ཏེ་སྔར་ནི་མ་སྨིན་པའི་དབང་དུ་བྱས་ལ་དེ་ཡང་གང་གིས་དངོས་གྲུབ་མཐར་འགྲོ་བ་ནས་ཚིག་རྐང་གསུམ་བརྗོད་པ་དང་། ཧེ་རུ་ཀ་ཁ༌[^443]སྦྱོར་ནས། ཁ་དོག་ལྔ་ལ་རྣམ་པར་གནས། །ཞེས་ཟེར་བས་སོ། །

[Block 1004]
འདིར་ནི་དཔེར་ན་ཨ་མྲའི་འབྲས༌[^444]དང་འདྲ་སྟེ་ཕྱི་ནང་གཉི་ག་མ་སྨིན་པའི་ཛོ་གི་ལ་ཐབས་གཙོར༌[^445]བྱས་ཏེ། ལས་ཀྱི་ཕྱག་རྒྱ་ལ་བརྟེན་པ་དང་། ཕྱི་སྨིན་ཅིང་ནང་མ་སྨིན་པའི་ཛོ་གི་ཐབས༌[^446]ཤེས་རབ་ཟུང་འབྲེལ་གྱི་སྒོ་ནས་རྩ་རླུང་ལ་བརྟེན་པ་དང་ཕྱི་ནང་གཉིས་ཀ་སྨིན་པའི་རྣལ་འབྱོར་པ་ལ་ཤེས་རབ་གཙོར༌[^447]བྱས་ཏེ། ནམ་མཁའ་ལམ་ཁྱེར་ཏེ་མན་ངག་ལ་བརྟེན་པའོ། །

[Block 1005]
དེ་ཡང་འོག་ནས།

[Block 1006 [VERSE]]
ཆོས་འབྱུང་ལས་སྐྱེས་ཡེ་ཤེས་ནི། །
མཁའ་མཉམ་ལྷན་ཅིག་ཐབས་དང་བཅས། །

[Block 1007]
ཞེས་པ་དང་། གང་ཕྱིར་ཡིད་ཀྱིས་མི་བསྒོམ་པར། །འགྲོ་བ་ཐམས་ཅད་བསྒོམ་པར་བྱ།[^448] །ཞེས་དང་།

[Block 1008 [VERSE]]
གཞན་གྱིས་བརྗོད་མེད་ལྷན་ཅིག་སྐྱེས། །
ཞེས་པ༌[^449]ནས་བླ་མའི་དུས་ཐབས་ཞེས་པའོ། །
དེ་ནས་འབྲེལ་བ་ཡོད་པའོ། །

[Block 1009]
གཞན༌[^450]ལུས་ཤེས་རབ་ལ་བརྟེན་པ་ལས་ཀྱི་ཕྱག་རྒྱའི་ཁྱད་པར་ལ་བྱ༌[^451]སྟེ། ཤིང་གཅིག་ནི་གཏུམ་མོའོ། །

[Block 1010]
དུར་ཁྲོད་ནི་གཡུང་མོའོ། །

[Block 1011]
མ་མོའི་ཁྱིམ་ནི་གར་མའོ། །

[Block 1012]
མཚན་མོ་ནི་ཚོས་མའོ། །

[Block 1013]
དབེན་པ་དང་བས་མཐའ་ནི་བྲམ་ཟེ་མའོ། །

[Block 1014]
དེ་དག་ཅིའི་ཕྱིར་ཞེ་ན། རྣམ་པར་རྟོག་པ་འཇོམས་པ་ལ་དཔའ་བ་དང་སྨེ་ཞིང་རེག༌[^452]ཏུ་མི་རུང་བ་དང་མང་པོ་དག་ཏུ་འགྱུར་ཞིང་སྤྱོད་པ་དང་། ཐ་མལ་པའི་རྣམ་པར་བསྒྱུར་བ་དང་། ཉོན་མོངས་པ་དང་རྣམ་པར་རྟོག་པའི་སྐྱོན་དང་བྲལ་བའི་ཕྱིར་རོ། །

[Block 1015]
རང་ལུས་ཐབས་ལ་བརྟེན་པ་ནི་ཤིང་གཅིག་ནི་ཨ་ཝ་དྷཱུ་ཏཱིའོ། །

[Block 1016 [VERSE]]
དུར་ཁྲོད་ནི་བྱ་རོག་གི་གདོང་ཅན་ནོ། །
མ་མོའི་ཁྱིམ་ནི་རྩ་གཞན་དག་གོ། །
དུས་མཚན་མོ་ནི་འཁོར་ལོ་གསུམ་མོ། །

[Block 1017]
དབེན་པའམ་བས་མཐའ་ནི་བདེ་བ་ཆེན་པོའི་འཁོར་ལོའོ། །

[Block 1018]
དེ་དག་ཅིའི་ཕྱིར་ཞེ་ན། དེ་ཉིད་དུ་འདུ་ཞིང་དེ་ལས་བྱུང་བ་དང་རང་གིས་བསྐུལ་བ་གཡོ་བ་དང་བྲལ་བ་དང་དེ་དག་ཏུ་བྱང་ཆུབ་སེམས་འཆར་བ་དང་གནས་གསུམ་དུ་ངལ་སོ་ཞིང་ནུབ་པ་དང་ཆགས་པ་དང་ཆགས་བྲལ་གྱི་སྐྱོན་དང་བྲལ་བའི་ཕྱིར་རོ། །

[Block 1019]
གཉིས་སུ་མེད་པ་ཕྱག་རྒྱ་ཆེན་པོ་ནི། ཤིང་གཅིག་སྟེ༌[^453]ཤེས་རབ་ལྷ་མོ་བླ་ན་མེད་པའོ། །

[Block 1020]
དུར་ཁྲོད་ནི་ལུས་སོ། །
--- END BLOCKS ---
