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
[Block 2906]
ལམ་དང་ཞེས་བྱ་བ་ནི་བསྐྱེད་པ་དང་རྫོགས་པའི་རིམ་པའོ། །

[Block 2907]
ལྷ་རྣམས་ཇི་ལྟར་ནི་ག་བུར་ཀུནྡ་བདེ་བ་རྣམས༌[^1208]ནམ་མཁའ་ལྟ་བུའོ། །

[Block 2908]
འབྱུང་བ་ཉིད་ནི་བསྐྱེད་པ་སྟེ་ཀུན་རྫོབ་དང་དོན་དམ་གྱི་སེམས་གཉིས་སོ། །

[Block 2909]
ཐམས་ཅད་བཅོམ་ལྡན་འདས་གསུངས་ནས། ཕྱག་རྒྱ་ཆེན་པོ་རྒྱས་བཏབ་པ་ཡང་གསུངས་པའོ། །

[Block 2910]
སྡོམ་པ་བདག་ལ་བཤད་དུ་གསོལ། །

[Block 2911 [VERSE]]
ཞེས་པ་ནི་དམ་ཚིག་གི་ཕྱག་རྒྱའི་ཚུལ་དུའོ། །
བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་ནི་དེའི་ལན་དུའོ། །

[Block 2912]
རྣལ་འབྱོར་མ་ལུས་ནི་བདག་མེད་པར་བསྒོམ་པའོ།[^1209] །དབུས་གནས་ནི་ལྟེ་བར་རོ། །

[Block 2913]
ཨཾ་སྡོམ་པར་གནས་ནི་བདག་མའི་ཡི་གེའི་རྣམ་པས་སོ། །

[Block 2914]
ཇི་ལྟར་ཕྱི་རོལ་དེ་དེ་བཞིན་དུ་སྙིང་གར་དགྱེས་པའི་རྡོ་རྗེ་ཧཱུཾ་གི་རྣམ་པར་རོ། །

[Block 2915]
སྡོམ་པ་དེ་ཉིད་ནི་སྙོམས་འཇུག་གོ། །

[Block 2916]
རབ་ཏུ་ཕྱེ་བའམ་བཤད་པ་ནི་རྣམ་པ་སྣ་ཚོགས་ལ་སོགས་པར་དབྱེ་བའོ། །

[Block 2917]
བོ་ལའི་བདེ་བ་ནི་གསང་བའི་གནས་ཀྱི་ཡང་བསྐུལ་པའམ་ཧཱུཾ་དེ་ཉིད་དོ། །

[Block 2918]
ཕྱག་རྒྱ་ཆེན་པོར་ཕྱག་རྒྱ་དེ་ཉིད་ལ་སྦྱར་བའམ་སྔར་གྱི་དང་འདྲ་བས་སོ། །

[Block 2919]
རྡོ་རྗེ་སྐྱེ་མཆེད་ཐབས་ཉིད་ནི་ཧཱུཾ་ཞུ་བ་གསང་བའི་དབང་པོར་ཉམས་སུ་མྱོང་བའོ། །

[Block 2920]
འདིས་ནི་གསང་བའི་སྙོམས་འཇུག་ནི་ནང་གི་སྙོམས་འཇུག་གིས་སོ། །

[Block 2921]
ཕྱི་རོལ་གཉིས་བསྟན་པ་མེད་དམ་དེ་བཞིན་ནི་བདག་མེད་མར་བསྒོམ་པ་ལའོ། །

[Block 2922]
དེས་ནི་འདི་སྐད་བསྟན་པར་འགྱུར་ཏེ། ཕྱག་རྒྱ་ལ་བརྟེན་པར་ཕྱག་རྒྱ་ཆེན་པོ་ཇི་ལྟར་འགྲུབ་ནུས་སྙམ་པའི་དོགས་པ་སེལ་བར་བྱ་བའི་ཕྱིར། སྔར་གྱི་ཧེ་རུ་ཀའི་གཟུགས་སུ་གྱུར་པའི༌[^1210]རྣལ་འབྱོར་མས་བྱ་བའི་ཐབས་ཡིན་ལ། འདིར་ནི་རྣལ་འབྱོར་པས་བདག་མེད་མ་བསྒོམ་པའི་ཐབས་སོ། །

[Block 2923]
དེ་ལྟར་སྙོམས་འཇུག་གི་སྡོམ་པ་བསྟན་ནས། ད་ནི་སྤྱིར༌[^1211]ལུས་ལ་གནས་བའི་སྡོམ་པ་བསྟན་པའི་ཕྱིར། སྐུ་གསུམ་ལུས་ཀྱི་ལ་སོགས་པ་སྟེ་ཚིགས་སུ་བཅད་པ་ཕྱེད་དང་གཉིས་ཀྱིས་བརྟེན་པ༌[^1212]ཁྱད་པར་དུ་བྱ་བའི་མིང་བསྟན་ཏོ། །

[Block 2924]
ཚིག་རྐང་གཉིས་རྟེན་དང་བརྟེན་པའི༌[^1213]སྐུ་སྟེ་བདེ་བ་ཆེན་པོ་ཡང་ལྷག་མའོ། །

[Block 2925]
ཡང་ཚིག་རྐང་གཉིས་ཀྱིས་ནི་ལུས་ཅན་ཀུན་ལ་ཡོད་པར་བསྟན་པའོ། །

[Block 2926]
སྤྲུལ་པར་གནས་བརྟེན་པ་ལ་སོགས་པ་ནི་རྒྱུ་མཚན་བཤད་པའོ། །

[Block 2927]
ཨེ་ཝཾ་ལ་སོགས་པ་བསྟན་པས་དེ་བཤད་པ་ཡང་ལས་ཀྱི་རླུང་གིས་བསྐུལ་ཞེས་པ་ནི་མདོམས་བར༌[^1214]དུ་ཡཾ་རཾ་ལས་བསྐུལ་བའམ་སྙོམས་འཇུག་གི་དུས་བསྐྱེད་པས་སོ། །

[Block 2928]
བཅོམ་ལྡན་འདས་ཤེས་རབ་བརྗོད་ནི་བདག་མེད་མ་ཨཾ་གི༌[^1215]གཟུགས་ཅན་ནོ། །

[Block 2929]
ཇི་ལྟར་བྱས་པ་ནི་དཀའ་བའི་བྱ་བ་དུ་མའོ། །

[Block 2930]
དེ་བཞིན་སྤྱོད་ནི་ཡེ་ཤེས་རྟོག་པ་དང་འདྲེན་མ་དུ་མ་སྐྱེད་ཅིང་ཉམས་སུ་མྱོང་བའི་ཕྱིར་རོ། །

[Block 2931]
རྒྱུ་མཐུན་ཞེས་པ་ནི་རབ་ཏུ་གྲགས་ནི་རྒྱུ་མཚན་དེས་བསྒྲུབ་པོ། །ཡང་ལས་ཆུང་ཞེས་པ་ནི་རླུང་དང་མེའམ་སྙོམས་འཇུག་ལ་མི་ལྟོས་པའོ། །

[Block 2932]
འབྲས་བུ་ཆེ་བ་ནི་ཡེ་ཤེས་རྩེ་གཅིག་པ་མྱོང་བའི་ཕྱིར་རོ། །

[Block 2933]
རྣམ་སྨིན་དེ་ལས་བཟློག་པ་ནི་རྒྱུ་འབྲས་ཆེ་ཆུང་བཟློག་པའམ་རྒྱུ་མཐུན་དང་མི་འདྲ་བར་བཟློག་པ་སྟེ་རྣམ་སྨིན་གྲུབ་པའོ། །

[Block 2934]
དེ་ནས་སྐྱེས་བུར་འབྲེལ་ཏེ་མགྲིན་པ་ལོངས་སྤྱོད་ཀྱི་བདག་པོར་བྱེད་པར་འདོད་པས་སྐྱེས་བུ་བྱེད་པའི༌[^1216]འབྲས་བུའོ། །

[Block 2935]
དེར་ནི་རྣལ་འབྱོར་བདག་ཕྱིར་ནི་བདེ་ཆེན་དུའོ། །

[Block 2936]
དྲི་མེད་ཉིད་ནི་གློ་བུར་བ་སྤངས་པ་སྟེ་བྲལ་བའི་འབྲས་བུའོ། །

[Block 2937]
གང་ཕྱིར་སྤྲུལ་པ་ལ་སོགས་པ་ནི་དེ་རྣམས་དང་ཆོས་མཐུན་དུ་བྱས་པའམ། འབྲས་བུ་སྐུ་གསུམ་ཡོངས་སུ་ཤེས་པ་བདེ་བ་ཆེན་པོའི་སྐུ་སྟེ། སྐྱེ་བ་གང་ལ་ཞེས་པ་སེམས་ཅན་ཐམས་ཅད་སྐྱེ་བ་ལྟེ་བ་ནས་འབྱུང་ལ། སྤྲུལ་པའི་སྐུ་ལས་སེམས་ཅན་གྱི་དོན་བྱེད་པས་དེ་དང་ཆོས་མཐུན་པའོ། །

[Block 2938]
སྙིང་ག་དང་ཆོས་སྐུ་ཡང་ཆོས་ཐམས་ཅད་སེམས་ལས་བྱུང་བ་དང་། ཆོས་སྐུ་ཡང་ཐམས་ཅད་ཀྱི་རྟེན་བྱེད་དེ།

[Block 2939 [VERSE]]
ཡོན་ཏན་བསམ་ཡས་ཀུན་རྟེན་ཕྱིར། །
སྐྱོབ་པ་རྣམས་ཀྱི་ཆོས་སྐུར་བཞེད། །

[Block 2940]
ཅེས་གསུངས་སོ། །

[Block 2941]
མགྲིན་པ་དང་ལོངས་སྐུ་ཡང་རོ་དྲུག་ནི་མངར་བ་དང་། སྐྱུར་བ་དང་། ཁ་བ་དང་། ཚ་བ་དང་། བསྐ་བ་དང་། ལན་ཚྭ་དེ་རྣམས་མགྲིན་པར་མྱོང་གི་འདས་ནས་མ་ཡིན་པ་ལྟར་ལོངས་སྐུའི་ཞིང་ཁམས་དང་འཁོར་དང་ཆོས་ལ་ལོངས་སྤྱོད་པའོ། །

[Block 2942]
སྤྱི་བོ་བདེ་ཆེན་གྱི་སྐུ་ཡང་སྤྱི་བོར་བདེ་བ་ཁྱད་པར་དུ་འཕགས་པ་བདེ་བ་ཆེན་པོའི་སྐུ་ཡང་སྐུ་གསུམ་ཡོངས་སུ་ཤེས་པས་ཁྱད་པར་དུ་འཕགས་པའོ། །

[Block 2943]
ཨེ་ཝཾ་རྒྱུ་མཐུན་ནི་ཨེ་སྟེ་སྤྲུལ་པ་ལ་སོགས་པ་ཨེ་ཝཾ་མ་ཡཱ་སྦྱར་རོ། །

[Block 2944]
ཕ་རོལ་ཕྱིན་པ་ལ་འབྲས་བུ་བཞི་སྟེ། འཁོར་ལོ་བཞི་དང་ཆོས་མཐུན་བསྟན་ཏེ། དང་པོར་རྒྱུ་མཐུན་པའི་འབྲས་བུ་ནི། རྒྱུ་མཐུན་དང་འདྲ་བ་ཉིད་ཅེས་པ་བཟོ་ལ་སོགས་པ་ལས་མ་འོངས་པ་ན་ཡང་དེ་དང་མཐུན་པར་འབྱུང་སྟེ། ལས་ཀྱི་རླུང་གིས་མེ་ལ་སོགས་པ་བསྐུལ་བས་ལྟེ་བའི་གནས་སུ་རྟོག་པ་དང་འདྲེན་པར་ཉམས་སུ་མྱོང་བས་སོ། །

[Block 2945]
རྣམ་པར་སྨིན་པའི་འབྲས་བུས་ནི་དེ་ལས་དགེ་མི་དགེ་ཅུང་ཟད་ལས་མ་འོངས་པའི་དུས་སུ་ལྷ་མིན་ཁྱད་པར་ཅན་དང་ངན་སོང་དུ་སྨིན་པས་ལས་ཆུང་ལ་འབྲས་བུ་ཆེ་བ་ཞེས་བྱ་སྟེ། དེ་ལྟར་ལྟེ་བ་ནས་སྙིང་གར་ཁྱད་པར་དུ་མྱོང་བའོ། །
--- END BLOCKS ---
