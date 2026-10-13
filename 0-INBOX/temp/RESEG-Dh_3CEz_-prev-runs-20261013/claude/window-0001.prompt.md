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
[Block 36]
ཧ་ར་ནི་འཕྲོག་པ་སྟེ་གཙོ་བོའི་ཡོན་ཏན༌[^23]གྱིས་འཁོར་གྱི་ཐེ་ཚོམ་སྟོན་པས་འཕྲོག་པའོ། །

[Block 37]
བཞུགས་ཞེས་པས་ཡང་རྒྱལ་པོ་ཕོ་བྲང་ན་བཞུགས་པས་འཁོར་འདྲེན་ཏེ། རྒྱལ་པོ་གཅིག་ཏུ་བཞུགས་པ་མ་ཡིན་པ་དང་། ཐོས་པའི་འབྲེལ་པས་འཁོར༌[^24]དང་བཅས་པ༌[^25]སྟོན་པས་འཁོར་བསྟན་པ་དང་གཞན་དག་ནི་སྤྱོད་ལམ་དང་ཆོས་འཆད་པ་དང་ཏིང་ངེ་འཛིན་དང་ནང་དུ་ཡང་དག་འཇོག་པས་བཞུགས་ཞེས་ཀྱང་འཆད་དོ། །

[Block 38 [HEADING]]
###### མིང་ཁྱད་པར་དུ་བཏགས་པའི་ཡོན་ཏན། ^1-1-1-1-3-0

[Block 39]
མིང་ཁྱད་པར་ཅན་དུ་བཏགས་པ་ནི་འདི་སྐད་ལ་ཨེ་སིན་ནམ་ཨི་དཾ་ཞེས་མི་ཟེར་བར་ཨེ་ཝཾ་ཞེས་བཏགས་པས་ལོག་རྟོག་སེལ་ཏེ་ཁ་ཅིག་ཕྱྭ་དང་མེས་པོ་དང་དབང་ཕྱུག་ལ་སོགས་པ་རྒྱུར་སྨྲ་སྟེ།

[Block 40]
བྱེ་བྲག་པའི་ལུང་ལས།

[Block 41 [VERSE]]
བ་ནི་བ་སྨྲ་བ༌[^26]རྣམས་ཀྱི་རྒྱུ། །
འགྲོ་བའི་རྒྱུ་ནི་དབང་ཕྱུག་སྟེ། །
དབང་ཕྱུག་གིས་ནི་མཐོ་རིས་སམ། །
ངན་འགྲོ་དག་ཏུའང་ལྟུང་བར་བྱེད། །

[Block 42]
ཅེས་ཟེར་བ་དེ་ལྟ་བུ་དགག་པའི་ཆེད་དུ་སྟེ། །ཨེ་ཝཾ་ནི་ཆོས་ཐམས་ཅད་ཀྱི་ཕ་དང་མ༌[^27]ལྟ་བུའི་འབྱུང་ཁུངས་སུ་ཤེས་པར་བྱེད་ལ། ཨེ་ཝཾ་སྟེ་བདེ་སྟོང་དབྱེར་མེད་ཐབས་ཤེས་རབ་དང་དབྱེར་མེད་དུ་སྟོན་པས་ན་དེ་སྤོང་ངོ་། །དེ་ཡང༌[^28]ཨེ་ནི་མར་འགྱུར་ལ།

[Block 43 [VERSE]]
བི་ན་ཕ་ཞེས་བྱ་བར་གྲགས། །
ཐིག་ལེ་དེ་ནི་སྦྱོར་བ་སྟེ། །
སྦྱོར་ཏེ་དེ་ནི་རྨད་བྱུང་བའོ། །

[Block 44]
ཞེས་པ་དང་།

[Block 45 [VERSE]]
ཨེ་ནི་ཤེས་རབ་ཉིད་འགྱུར་ལ། །
ཝཾ་ནི་རབ་དགའི་བདག་པོའོ། །
འགྲོ་བ་གང་ཞིག་ཡི་གེ་གཉིས། །
མི་ཤེས་རྟག་ཏུ་འདོན་པ་དང་། །

[Block 46 [VERSE]]
དེས་ན་སངས་རྒྱས་ཆོས་རྣམས་ལས། །
ཕྱི་རོལ་སྦྱོར་སྤངས་ཐུབ་པ་བཞིན། །
ཨེ་ཝཾ་ཡིག་གཉིས་སྒྱུ་མ་ལ། །
ཐམས་ཅད་མཁྱེན་པ་འདིར་བཞུགས་པས། །

[Block 47 [VERSE]]
དམ་ཆོས༌[^29]བསྟན་པའི་ཐོག་མར་ནི། །
ཨེ་ཝཾ་དེ་ཕྱིར་རབ་ཏུ་བཤད། །

[Block 48]
ཅེས་གསུངས་སོ། །

[Block 49]
བདག་གིས་ལ་ཨཱཏྨའི་ཟེར་བ་ནི་མུ་སྟེགས་བདག་ཏུ་འདོད་པ་ཡང་གང་ཟག་བདག་ཏུ་འདོད་པ་སྟེ། གྲངས་ཅན་དག་ནི་ཡོན་ཏན་གསུམ་ཆེ་མཉམ་པ་ལས་གཙོ་བོ་ལས་བདག་སྟེ། དེ་ལས་འགྱུར་བ། དེ་ལས་ཡོན་ཏན་དུ་མ་སྐྱེ་སྟེ།

[Block 50 [VERSE]]
འདི་ཙམ་ཉི་ཤུ་ལྔ་ཤེས་ན། །
རལ་པའམ་སྤྱི་བོ་གཙུག་ཕུད་ཀྱི། །
བསྟི་གནས་གང་དུ་འགྲོ་བ་དེར། །
གྲོལ་འགྱུར་འདི་ལ་ཐེ་ཚོམ་མེད། །

[Block 51]
ཅེས་ཟེར་བ་དེ་བཟློག་པའི་ཕྱིར། མ༌[^30]ཡཱ་ནི་སྒྱུ་མའི་བདག་ཉིད་དུ་ཤེས་པར་བྱ་སྟེ། བདག་ནི་རྟག་པ་དང་གཅིག་པུ་དང་རང་དབང་དུ་འདོད་ལ།

[Block 52]
སྒྱུ་མ་ནི་དེ་དང་མཚན་ཉིད་མི་མཐུན་པས་ནི་དེ༌[^31]སྤོང་ངོ་། །ཐོས་པ་ཤྲུ་བ་ལའམ་ཤྲུ་ཏ་ཟེར་བ་ནི་མུ་སྟེགས་ཀྱི་རིག་བྱེད་པ་སྒྲ་ཡོན་ཏན་དུ་འདོད་པ་སྒྲས་ཆོག་པར་འཛིན་ཏེ། །དེའི་ལུང་ལས།

[Block 53 [VERSE]]
ཉེས་པ་རྣམས་དང་འབྲེལ་བའི་ཕྱིར། །
སྐྱེས་བུ་མ་བྱས་བདེན་དོན་ཅན། །

[Block 54]
ཞེས་སྒྲ་རྟག་པར་འདོད་པ་དེ་སྤོང་སྟེ། ཤྲུ་ཏ་རྒྱུ་བས་མ་ཤྲུ་ཏ་རིག་པ་ཤེས་པས་སྒྲ་རྟག་པ་དེ་ཐོས་བྱ་དང་ཐོས་བྱེད་ཀྱི་འབྲེལ་པ་མི་འཐད་པས་ན་དེ་བཟློག་གོ། །

[Block 55]
དུས་གཅིག་ན་ཨེ་ཀ་ཀཱ་ལ་མི་ཟེར་པར༌[^32]ས་མ་ཡ་ཟེར་བ་ནི་དུས་ཡོན་ཏན་དུ་འདོད་པ་ཡོད་དེ། དེ་ཡང་།

[Block 56 [VERSE]]
སྐྱེ་དགུ་འདི་དག་དུས་ཀྱིས་བསྡུས། །
དངོས་པོ་འདི་དག་དུས་ཀྱིས་བྱེད། །

[Block 57]
ཅེས་ཟེར་ཏེ། རིགས་པ་ཅན་ལ་སོགས་པ་འདོད་པ་བཟློག་པ༌[^33]སྟེ། ས་མ་ཡ་ནི་དམ་ཚིག་དེ་དུས་དང་མཉམ་པའི་དུས་དང་། ཡ་ཡོ་ག་སྦྱོར་བར་འགྲོ་བས་ན་དུས་རྟག་པ་ནི་དེ་དག་དང་འགལ་བས་ན་བཟློག་གོ། །

[Block 58]
དེ་སྐད་དུ་ཡང་།

[Block 59 [VERSE]]
དུས་ནི་རྣམ་པ་གསུམ་ཡིན་ཏེ། །
བདེ་བའི་དུས་དང་ངན་པའི་དུས། །
བསམ་གྱིས་མི་ཁྱབ་དུས་ཡིན་ཏེ། །

[Block 60]
ཞེས་གསུངས་སོ། །

[Block 61]
བི་ཛ་ཧ་རཾ་ལ་སྟ་ནའམ་སྟི་སྟི་བེ་སེ་པ་མི་ཟེར་བ་ནི་ཐེར་ཟུག་པའི་རྟག་པ་སྤོང་སྟེ། གྲངས་ཅན་ལ་སོགས་པ་རྫ་ཆག་བྱེ་འཕུར་དུ་འདོད་པ་སྟེ། ཧ་རས་སྤོང་སྟེ་རྗེས་སུ་མཐུན་པས་སྟོན་ཏེ། འཕགས་པའི་ཚུལ་དུ་བཞིས་བཞུགས་པ་དང་ཧ་རས་འཕྲོག་བྱ་དང་ཕྲོག་བྱེད་དུ་བཞུགས་པའམ།

[Block 62]
བི་ཛི༌[^34]ཡང་ཡོན་ཏན་དང་འཇོམས་པར་བཞུགས་པའོ། །

[Block 63 [HEADING]]
##### དོན་བཞིན་དུ་བཤད་པ། ^1-1-1-2-0

[Block 64]
དོན་བཞིན་དུ་བཤད་པ་ནི་གཉིས་ཏེ། །

[Block 65]
བཤད་ཚུལ་སོ་སོར་སྦྱོར་བ་དང་བརྟག་པ་ཕྱི་མའི་ཚུལ་གྱིས་མདོར་བསྡུས་ཏེ་བསྟན་པའོ། །

[Block 66 [HEADING]]
###### བཤད་ཚུལ་སོ་སོར་སྦྱོར་བ། ^1-1-1-2-1-0

[Block 67]
བཤད་ཚུལ་སྦྱར་བ་ནི་བསྐྱེད་རིམ་དང་རྫོགས་རིམ་མོ། །

[Block 68 [HEADING]]
###### **བསྐྱེད་རིམ།** ^1-1-1-2-1-1-0

[Block 69]
བསྐྱེད་རིམ་དམིགས་པར་བྱ་བའི་ཡུལ་གླེང་གཞི་བསྟན་པ་དང་། ཉམས་སུ་ལེན་པའི་ཐབས་བསྟན་པའོ། །

[Block 70 [HEADING]]
###### **དམིགས་པར་བྱ་བའི་ཡུལ་གླེང་གཞི་བསྟན་པ།** ^1-1-1-2-1-1-1-0

[Block 71]
གླེང་གཞི་ནི་འདི་སྐད་བདག་གིས་ཐོས་པ་ཞེས་བྱ་བས་ནི་སྡུད་པ་པོ་ཕུན་སུམ་ཚོགས་པ་སྟོན་ཏོ།[^35] །

[Block 72]
སྔར་བསྟན་པའི་ཡོན་ཏན་དང་ལྡན་པའི་ས་བཅུའི་བྱང་ཆུབ་སེམས་དཔའ་རྡོ་རྗེ་སྙིང་པོའོ། །

[Block 73]
དུས་གཅིག་ནི༌[^36]ཕུན་སུམ་ཚོགས་པ་སྟེ། སྟོན་པ་གནས་དང་འཁོར་ལ་སོགས།[^37] །འདུས་པ་དུས་ཞེས་བཤད་པ་ཡིན། །ཞེས་པ་མདོ་ལ་སོགས་པ་ལྟར་དཔྱིད་ཟླ་ར་བ་ལ་སོགས་པ་བསྟན་པ་བཞིའི་དུས་སོ། །

[Block 74]
སྟོན་པ་ནི་བྷ་ག་ཝཱན་ཏེ་གོང་མ་ལྟར་སྤངས་པ་དང་། ཡེ་ཤེས་ཏེ་དེ་དང་ལྡན་པའི་རྒྱུའི་རྡོ་རྗེ་འཆང་རིགས་བདུན་པ་སྟེ་དེ་ཡང་འོག་ཏུ་འཆད་དེ།

[Block 75 [VERSE]]
ཞལ་བརྒྱད་ཕྱག་ནི་བཅུ་དྲུག་སྟེ། །
དཔའ་བོ་ཐོད་པའི་ཕྲེང་བ་ཅན། །
ཕྱག་རྒྱ་ལྔ་ནི་འཛིན་ལྷ་ལ། །
བདག་མེད་མ་ནི་ཉིད་ཀྱིས་ཞུས། །
--- END BLOCKS ---
