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
[Block 3011]
གཏི་མུག་ལ་སོགས་པ་ནི་ཤེས་བྱའི༌[^1233]སྒྲིབ་པའོ། །

[Block 3012]
ཡང་ན་མ་རིག་པ་ལ་སོགས་པས་མི་འཛིན་ནི་སྔར་བདག་མེད་པར་བྱས་པས་སོ། །

[Block 3013]
གཏི་མུག་ལ་སོགས་པས་མི་འཆིང་ནི་ལྷན་ཅིག་སྐྱེས་པའི་བདེ་བས་སོ། །

[Block 3014]
རང་དང་རང་གི་བྱང་ཆུབ་ཕྱིར་ནི་གཉུག་མའི་ཡེ་ཤེས་ཡིན་པས་སོ། །

[Block 3015]
སངས་རྒྱས་མ་ཡིན་སེམས་ཅན་ནི། །ཞེས་པ་ནི་ལྷན་ཅིག་སྐྱེས་གཉིས་ལས་གཞན་པའི་ལུས་སེམས་སོ། །

[Block 3016]
གཅིག་ཀྱང་ཡོད་པ་མ་ཡིན་ནི་བདེ་ཆེན་དང་ལྡན་པའི་སངས་རྒྱས་འབའ་ཞིག་གོ། །

[Block 3017]
འོ་ན་དམྱལ་བ་ལ་སོགས་པ་ཅི་ཞེ་ན། དེའི་ཕྱིར་རྟག་ཏུ་རང་བཞིན་བདེ་བ་ཅན་ནི་གཉུག་མར་ལྡན་པ་ཡང་མ་ཤེས་སོ། །

[Block 3018]
འོ་ན་ལྷ་ལ་སོགས་པས་མྱོང་ཞིང་ཤེས་སོ་ཞེ་ན། །དེའི་ཕྱིར་ལྷ་དང་ལྷ་མིན་ཞེས་པ་ནི་བདེ་བ་མྱོང་ཞིང་ཤེས་ཀྱང་ངོ་། །བདེ་བ་གང་ཕྱིར་མི་ཤེས་ཞེས་པ་ནི་རྟག་ཏུ་གཉུག་མའི་རང་བཞིན་མི་ཤེས་པའོ། །

[Block 3019]
དེ་དག་བསྡུ་བའི་ཕྱིར་འཇིག་རྟེན་ཁམས་ནི་ལ་སོགས་པའི་རྡོ་རྗེ་སྙིང་པོ་སྙིང་རྗེ་ཆེ་ནི་ལྷ་མོ་རྣམས་དབུགས་ཕྱིན་ནས་དེའི་དོན་བསྡུས་ནས་འདིར་བརྗོད་པའོ། །

[Block 3020]
ཀྱེའི་རྡོ་རྗེའི་ཐབས་རྙེད་ནི་དབུགས་དབྱུང་གསུམ་པ་ལྟར་རོ། །

[Block 3021]
ཡུལ་རྣམས་ནི་གཟུགས་ལ་སོགས་པ་འདོད་པའི་ཡོན་ཏན་ནོ། །

[Block 3022 [VERSE]]
རྣལ་འབྱོར་ནི་བདག་མེད་པས་སོ། །
བླ་མེད་རྙེད་ནི་བདེ་བའི་རོས་སོ། །

[Block 3023]
ད་ནི་སྔར་བསྟན་པའི་ཕྱག་རྒྱ་ངེས་པའི་རྒྱུ་མཚན་བཤད་པའི་ཕྱིར། རྡོ་རྗེ་སྙིང་པོས་གསོལ་ཞེས་པ་ལ་སོགས་པ་གསུངས་ཏེ། རྡོ་རྗེ་སྙིང་པོས་གསོལ་བ་ནི་ས་ནི་པུཀྐ་སཱིར་བཤད་པ། གང་ཕྱིར་གཏི་མུག་སྲ་བ་ཉིད། །ཅེས་པ་ལ་སོགས་པ་ནི་སྔར་གྱི་ཕྱག་རྒྱའི་རྒྱུ་མཚན་དྲིས་པ་སྟེ། མ་ལ་སོགས༌[^1234]པ་ལ་ཕྱག་རྒྱ་ཞེས་པ་ནི་དེ་ཉིད་མི་འཐད་པར་སྟོན་ཏེ། ལུས་ལ་སེམས་ཀྱི་ཕྱག་རྒྱ་འདེབས་པ་དང་། ཐུགས་ལ་སྐུའི་ཕྱག་རྒྱ་འདེབས་པ་མི་རིགས་སོ་ཞེ་ན་འདིར་ནི་མི་འཐད་པ་མེད་དེ།

[Block 3024 [VERSE]]
སེམས་སྤངས་ནས་ནི་ལུས་ཀྱི་ནི། །
མཛེས་པ་གཞན་དུ་མི་འགྱུར་རོ། །

[Block 3025]
ཞེས་པ་ནི་བྱིན་གྱིས་བརླབ་བྱ་དང་རློབ་བྱེད་ཀྱི་དབང་དུ་བྱས་ཏེ་གསུངས་སོ། །

[Block 3026]
ཡང་། སེམས་སྤངས་ནས་ནི་ལུས་ཀྱི་ནི། །ཞེས་པ་སྔ་མ་དང་གཉིས་ཀ་ལ་རྩ་བའི་ཚིག་བསྒྱུར༌[^1235]ཏེ་འདིར་ནི་ལུས་སྤངས་ནས་ནི་ཞེས་བྱ་སྟེ་རྟེན་དང་བརྟེན་པའི་རྒྱུ་མཚན་ནོ། །

[Block 3027 [VERSE]]
རྡོ་རྗེ་སྙིང་པོས་གསོལ་པ། །
མེ་ནི་གདོལ་བ་མོར་བཤད་དེ། །

[Block 3028]
ཞེས་པ་ནི་འདོད་ཆགས་ཀྱི་ཕྱག་རྒྱར་རིགས་པ་ལས་རིན་ཆེན་འབྱུང་ལྡན་གྱི་ཕྱག་རྒྱར་ཇི་ལྟར་འགྱུར་ཞེ་ན། འདི་ནི་རྒྱུ་ལ་འབྲས་བུའི་རྒྱས་བཏབ་པའི་རིགས་པ་སྟེ།

[Block 3029 [VERSE]]
སེར་སྣ་དང་ཤ་རྒྱུ༌[^1236]འབྲས༌[^1237]ཡིན་པའི་ཕྱིར་རོ། །
རྡོ་རྗེ་སྙིང་པོས་གསོལ་པ།
གང་ཕྱིར་རླུང་གི་གཡུང་མོ་ཉིད། །

[Block 3030]
ཅེས་པ་ནི་གཡུང་མོ་ལ་ཕྲག་དོག་གི་ཕྱག་རྒྱས་རིགས་པ་ཡིན་ནོ་ཞེ་ན། འདོད་ཆགས་ཀྱི་ཕྱག་རྒྱས་ཕྲག་དོག་ལ་འདེབས་པ་ནི་འབྲས་བུ་ལ་རྒྱུ་ཡིས་རྒྱས་བཏབ་པའི་རྒྱུ་མཚན་དང་། དེ་བཞིན་དུ་གཽ་རཱི་དང་ཙཽ་རཱི་ལ་སོགས་བྱིན་གྱིས་བརླབ་བྱ་རློབ་བྱེད་དང་རྟེན་དང་བརྟེན་པའི་རྒྱུ་མཚན་གྱིས་སྔ་མ་དང་འདྲའོ། །

[Block 3031]
རོ་ལངས་མ་དང་གྷ་སྨ་རཱི་ཡང་རྒྱུ་ལ་འབྲས་བུས་རྒྱས་གདབ་པ་དང་། འབྲས་བུ་ལ་རྒྱུ་ཡིས་རྒྱས་གདབ་པ་སྔ་མ་བཞིན་ནོ། །

[Block 3032]
དེ་ནས་གཏོར་མ་བསྟན་པའི་ཕྱིར་དགྱེས་པའི་རྡོ་རྗེ་ནི་གྱུར༌[^1238]མ་ཐག་པ་དེའམ། རྡོ་རྗེ་འཛིན་ནི་ཉེ་བའི་རྒྱུའི་རང་བཞིན་ཡིན་པས་སོ། །

[Block 3033]
སྙོམས་འཇུག་གནས་པ་ནི༌[^1239]དགྱེས་པའི་རྡོ་རྗེའོ། །

[Block 3034]
ལྷ་ཉིད་ནི་ལུས་ལས་འབྱུང་བ་སྟེ་ཞུ་བ་དང་བཅས་པ་ལའོ། །

[Block 3035]
སེམས་ཅན་དོན་ཕྱིར་ནི་འཆད་པར་འགྱུར་བའི་ཕན་ཡོན་ནོ། །

[Block 3036]
གཏོར་མ་ཆེ་ནི་བ་ལིཾ་སྟེ་སྟོབས་སམ་ནུས་པ་དང་ལྡན་པའོ། །

[Block 3037]
བདག་མེད་མས་ཞུས་པ་ནི་གཞན་གྱི་དོན་དུའོ། །

[Block 3038]
ཨེ་ཝཾ་རྣམ་པར་བཞུགས་ནི་སྙོམས་འཇུག་གི་ཚུལ་ལམ།

[Block 3039 [HEADING]]
#### ཨེ་ཝཾ་ངེས་བཞུགས། ^2-4-5-0

[Block 3040 [HEADING]]
##### སྔོན་བྱུང། ^2-4-5-1-0

[Block 3041]
ཨེ་ཝཾ་ངེས་བཞུགས་ནི་སྔོན་བྱུང་དང་རྗེས་སུ་འཇུག་པ་གཉིས། སྔོན་བྱུང་དུ་བཅོམ་ལྡན་འདས་ཆོས་འབྱུང་དང་གཞལ་ཡས་ཁང་ན་གནས་པའོ། །

[Block 3042 [HEADING]]
##### རྗེས་སུ་འཇུག་པ། ^2-4-5-2-0

[Block 3043]
རྗེས་སུ་འཇུག་པ་ནི་སྒྲུབ་པ་དང་མགྲོན་ཏེ། ཆོས་འབྱུང་གི་ནང་གི༌[^1240]པདྨ་སུམ་བརྩེགས་བསྒོམས༌[^1241]པ་ལ༌[^1242]དབུས་ཀྱི་ལྟེ་བ་ལ་རང་གནས་སོ། །

[Block 3044]
འདབ་མ་ལ་མགྲོན་དམིགས་པར༌[^1243]བྱའོ། །

[Block 3045]
ཡང་གཏོར་མ་ཨེ་ཝཾ་སྟེ་རླུང་དང་མེ་དང་ཐོད་པར་སྦྱར་བ་ལ་སོགས་པའོ། །

[Block 3046]
བྱིན་གྱིས་རློབ་པའི༌[^1244]ཚེ། ཨཾ་ཧཱུཾ་ཨེ་ཝཾ་གྱི་བརྡས་ཤེས་རབ་དང་ཐབས་སུ་བྱས་པའོ། །

[Block 3047]
གཞན་དག་ནི་དེ་བཞིན་ནོ། །

[Block 3048]
དེའི་དོན་ནི་འདི་ཡིན་ཏེ། གཏོར་མ་སྔར་བཤད་པའི་བདུད་རྩི་སྦྱངས་པས་བསྒྲུབས༌[^1245]ནས་ཆོས་ཀྱི་འབྱུང་གནས་ནང་དུ་ནི།

[Block 3049 [VERSE]]
པདྨ་འདབ་མ་སུམ་བརྩེགས་བསམ། །
དཀར་དང་སྔོ་དང་དམར་བ་སྟེ། །
སྟེང་དུ་ཨོཾ་ལས་ཚངས་ལ་སོགས། །
བར་དུ་ཧཱུཾ་ལས་བརྒྱ་བྱིན་སོགས། །

[Block 3050 [VERSE]]
འོག་ཏུ་ཨཱཿལས་མཐའ་ཡས་སོགས། །
པདྨའི་མདོག་བཞིན་བསྐྱེད་པར་བྱ། །
རང་བཞིན་སྤྱན་དྲང༌[^1246]གཉིས་མེད་བསྟིམ། །
བྱིན་བརླབ་དབང་བསྐུར་ཚུལ་བཞིན་བྱ། །
--- END BLOCKS ---
