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
[Block 4131]
དེ་ཡང་མི་བརྟན༌[^2955]ལ་མེད། མི་བརྟན་པའི༌[^2956]དངོས་པོ་ལ་ནི་བྱིན་གྱི་རླབས་མེད་དེ། འཕགས་པ་འོད་སྲུངས་ཆེན་པོས་ཤ་ལ་སོགས་པ་བྱིན་གྱིས་མ་བརླབས༌[^2957]པའི་ཕྱིར་རོ། །

[Block 4132]
གཞན་དག་མིན་གཞན་དག་ན་རེ། ཤི་བ་ལ་བྱིན་གྱི༌[^2958]རླབས་མེད་ཀྱི། རུས་པའི་ཀེང་རུས་གནས་པ་ནི་ལྷའི་མཐུས་སོ་ཞེས༌[^2959]ཟེར་རོ། །

[Block 4133]
ཅི་སེམས་གཅིག་གིས་སྤྲུལ་པ་གཅིག༌[^2960]ཁོ་ན་སྤྲུལ་པར་བྱེད་དམ་ཞེ་ན།

[Block 4134 [VERSE]]
དང་པོར་དུ་མས་གཅིག་ཡིན་ཏེ། །
བྱ་བར་གྱུར་ནས་བཟློག་པའོ། །

[Block 4135]
དང་པོ་ཉིད་དུ་ནི་སྤྲུལ་པའི་སེམས་དུ་མས་སྤྲུལ་པ་གཅིག་སྤྲུལ་པར་བྱེད་དོ། །

[Block 4136]
མངོན་པར་ཤེས་པ་བྱང༌[^2961]ནས་ནི་སེམས་གཅིག་གིས་སྤྲུལ་པ་པོ་ཇི་སྙེད་འདོད་པ་དུ་མ་སྤྲུལ་པར་བྱེད་དོ། །

[Block 4137]
ཡང༌[^2962]སྤྲུལ་པའི་སེམས་ཐམས་ཅད་ལུང་དུ་མ་བསྟན་པ་ཡིན་ནམ་ཞེ་ན། བསྒོམས་ལས༌[^2963]སྐྱེས་པ་ལུང་མ་བསྟན། །བསྒོམས་པའི་འབྲས་བུ་གང་ཡིན་པ་དེ་ནི་ངེས་པར་ལུང་དུ་མ་བསྟན་པ་ཡིན་ནོ། །

[Block 4138]
སྐྱེ་བ་ལས་སྐྱེས་རྣམ༌[^2964]གསུམ་མོ། །

[Block 4139]
ལྷ་དང་། ཀླུ་དང་། ཤ་ཟ་ལ་སོགས་པའི་སྐྱེ་བས་ཐོབ་པའི་སྤྲུལ་པའི་སེམས་ནི་དགེ་བ་དང་། མི་དགེ་བ་དང་།[^2965] ལུང་དུ་མ་བསྟན་པ་ཡིན་ནོ། །

[Block 4140]
དེ་དག་གིས༌[^2966]བྱས་པའི་སྤྲུལ་པ་རང་དང་གཞན་གྱི་ལུས་དང་འབྲེལ་བ་ནི་སྒྲ་མེད་པའི་གཟུགས་ཅན་གྱི་སྐྱེ་མཆེད་ཡིན་པའི་ཕྱིར། སྐྱེ་མཆེད་དགུ་པ་ཡིན་ཏེ། དབང་པོ་དང་ཐ་མི་དད་པའི་ཕྱིར་རོ། །

[Block 4141]
དབང་པོ་ནི་སྤྲུལ་པར་མི་བྱེད་དོ། །

[Block 4142 [HEADING]]
#### རྫུ་འཕྲུལ་རྣམ་པ་ལྔ། ^4-17-4-0

[Block 4143]
ཅི་བསྒོམས་པ༌[^2967]ལས་བྱུང་བ་དང་། སྐྱེ་བས་ཐོབ་པའི་རྫུ་འཕྲུལ་རྣམ་པ་འདི་གཉིས་ཁོ་ནར་ཟད་དམ་ཞེ་ན། རྫུ་འཕྲུལ་རྣམ་པ་གཉིས་པ༌[^2968]དེ་དང་། གསང་སྔགས་སྨན་དག་དང་། ལས་ལས་སྐྱེས་དང་རྣམ་པ་ལྔ། །རྫུ་འཕྲུལ་ནི་མདོར་བསྡུ་ན་རྣམ་པ་ལྔའོ་ཞེས་བརྗོད་དེ། བསྒོམས་པའི༌[^2969]འབྲས་བུ་དང་། སྐྱེ་བས་ཐོབ་པ་དང་། གསང་སྔགས་ལས་སྐྱེས་པ་དང་། སྨན་ལས་སྐྱེས་པ་དང་། ལས་ལས་སྐྱེས་པ་སྟེ། དཔེར་ན་ང་ལས་ནུ་དང་། སྲིད་པ་བར་མ་པ་རྣམས་ཀྱི་ལྟ་བུའོ། །

[Block 4144 [HEADING]]
### ལྷའི་མིག་དང་རྣ་བ། ^4-18-0

[Block 4145]
ལྷའི་རྣ་བ་དང་མིག་ཏུ་བཤད་པ་གང་ཡིན་པ་དེ་དག་ཅི་ལྷའི་ཁོ་ན་ཡིན་ནམ། འོན་ཏེ་བྱང་ཆུབ་སེམས་དཔའ་དང་། འཁོར་ལོས་སྒྱུར་བ་དང་། ཁྱིམ་བདག་རིན་པོ་ཆེ་རྣམས་ཀྱི་ལྟ་བུར་ལྷའི་དང་འདྲ་བས་ལྷའི་ཡིན་ཞེ་ན། ལྷ་ཡི་མིག་དང་རྣ་བ་ཡིན། །འདི་ལྟར་དེ་གཉིས་ནི། བསམ་གཏན་ས་པའི་གཟུགས་དང་བ། བསམ་གཏན་ལ་སྙོམས་པར་ཞུགས་པའི་མིག་དང་རྣ་བའི་ཐོད་ཀོར་དུ་སྒྲ་དང་། སྣང་བ་ལ་གཏོད་པའི་སྦྱོར་བས༌[^2970]བསམ་གཏན་གྱི་ས་པའི་འབྱུང་བ་རྣམས་རྒྱུར་བྱས་པའི༌[^2971]གཟུགས་དང་།[^2972] སྒྲ་དག་མཐོང་བ་དང་། ཐོས་པའི་རྒྱུ་མངོན་པར་འགྲུབ་པས་བསམ་གཏན་གྱི་ས་པ་ཡིན་པའི་ཕྱིར་མིག་དང་། རྣ་བ་དེ་དག་ནི་ལྷའི་ཁོ་ན་ཡིན་ནོ། །

[Block 4146]
དེ་གཉིས་ཀྱང་རྟག་ཏུ་བརྟེན་བཅས་མ་ཚང་མེད། ཐག་རིང་ཕྲ་སོགས་སྤྱོད་ཡུལ་ཅན། །ལྷའི་མིག་དང་རྣ་བ་ནི་རྟག་ཏུ་རྣམ་པར་ཤེས་པ་དང་བཅས་པ་ཡིན་པའི་ཕྱིར་དེ་དང་མཚུངས་པ་མེད་དོ། །

[Block 4147]
ཞར་བ་དང་འོན་པ༌[^2973]མེད་པའི་ཕྱིར་མ་ཚང་བ་ཡང་མ་ཡིན་ཏེ། གཟུགས་ན་སྤྱོད་པའི་སེམས་ཅན་བཞིན་ནོ། །

[Block 4148]
དེ་གཉིས་ཀྱི་ཡུལ་ནི་གཟུགས་དང་། སྒྲ་ཐག་རིང་བ་དང་། ཕྲ་བ་དང་། བསྒྲིབས་པ་དག་ཀྱང་ཡིན་ནོ། །

[Block 4149]
འདིར་སྨྲས་པ།

[Block 4150 [VERSE]]
གང་ཕྱིར་ཤ་ཡི་མིག་གིས༌[^2974]གཟུགས། །
ཐག་རིང་གནས་དང་བསྒྲིབས་པ་དང་། །
ཕྲ་རྒྱས༌[^2975]ཐམས་ཅད་མི་མཐོང་བ། །
དེ་ཕྱིར་ལྷ་ཡིས་མཐོང་བར་འདོད། །

[Block 4151]
ལྷའི་མིག་གིས་ཐག་ཇི་སྲིད་ཅིག་མཐོང་ཞེ་ན། གང་གི་མིག་ཇི་ལྟ་བུ་ཡིན་པའོ། །

[Block 4152]
ཉན་ཐོས་དང་རང་སངས་རྒྱས་དང་སངས་རྒྱས་རྣམས་ནི་མངོན་པར་འདུ་བྱེད་པ་མེད་པར་སྟོང་དང་སྟོང་གཉིས་པ༌[^2976]དང་སྟོང་གསུམ་པའི་འཇིག་རྟེན་གྱི༌[^2977]ཁམས་མཐོང་ངོ་། །མངོན་པར་འདུ་བྱེད་པས་ནི།

[Block 4153 [VERSE]]
དགྲ་བཅོམ་བསེ་རུ་སྟོན་རྣམས་ཀྱིས། །
སྟོང་གཉིས་གསུམ་དང་གྲངས་མེད་མཐོང་། །

[Block 4154]
ཉན་ཐོས་ཆེན་པོས་ཀྱང་མངོན་པར་འདུ་བྱེད་པ་ཐམས་ཅད་ཀྱིས་ལྷའི་མིག་གིས་སྟོང་གཉིས་པའི་འཇིག་རྟེན་གྱི་ཁམས་མཐོང་ངོ་། །བསེ་རུ་ལྟ་བུས་ནི་སྟོང་གསུམ་པ་མཐོང་ངོ་། །སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཀྱིས་ནི་ཇི་ཙམ་བཞེད་པར་འཇིག་རྟེན་གྱི་ཁམས་གྲངས་མེད་པ་གཟིགས་སོ། །

[Block 4155 [HEADING]]
### སྐྱེ་བས་ཐོབ་པ། ^4-19-0

[Block 4156]
ཅི་རྫུ་འཕྲུལ་ཁོ་ན་སྐྱེ་བས་འཐོབ་པ་ཡིན་ནམ། འོན་ཏེ་གཞན་ཡང་ཡིན་ཞེ་ན། གཞན་ཡང་སྐྱེ་བས་ཀྱང༌[^2978]འཐོབ། ལྷའི་རྣ་བ་ལ་སོགས་པ་བཞི་ཡང་སྐྱེ་བས་འཐོབ་པར་བྱ་བ་ཡོད་མོད་ཀྱི། སྐྱེ་བས་ཐོབ་པ༌[^2979]ནི་ཅུང་ཟད་ཀྱང་མངོན་པར་ཤེས་པའི་མིང་མི༌[^2980]འཐོབ་བོ། །

[Block 4157]
སྐྱེ་བས་འཐོབ་པའི་ལྷའི་མིག་གང་ཡིན་པ། དེས་ནི། སྲིད་པ་བར་མ་མི༌[^2981]མཐོང་ངོ་། །སྲིད་པ་བར་མ་ནི་མངོན་པར་ཤེས་པའི་མིག་ཁོ་ནས༌[^2982]མཐོང་གི །སྐྱེ་བས་ཐོབ་པ༌[^2983]ནི་མ་ཡིན་ནོ། །

[Block 4158]
སེམས་ཤེས་དེ་ནི་རྣམ་པ༌[^2984]གསུམ། སྐྱེ་བས་འཐོབ་པ་ཞེས་བྱ་བར་སྦྱར་ཏེ། ཕ་རོལ་གྱི་སེམས་ཤེས་པ་སྐྱེ་བས་འཐོབ་པ་དེ༌[^2985]ནི་དགེ་བ་དང་། མི་དགེ་བ་དང་། ལུང་དུ་མ་བསྟན་པ་དང་རྣམ་པ་གསུམ༌[^2986]ཡིན་པར་རིག་པར་བྱའོ། །

[Block 4159]
གང་རྟོགས༌[^2987]དང་རིག་སྔགས་ཀྱིས་བྱས་པའང་། གང་ཡང་མཚན་མ་པ་རྣམས་ཀྱིས༌[^2988]ཕ་རོལ་གྱི་སེམས་ཤེས་པ་དང༌[^2989]རྟོག་གེ་བ་དང་། གང་ཡང་རིག་སྔགས་ཀྱིས་བྱས་པ་དེ་ཡང་རྣམ་པ་གསུམ་ཡིན་པར་རིག་པར་བྱ་སྟེ། ཇི་ལྟར་བསྒོམས་པའི་འབྲས་བུ༌[^2990]དགེ་བ་ཁོ་ན་ཡིན་པ་ལྟ་བུ་ནི་མ༌[^2991]ཡིན་ནོ། །

[Block 4160]
ཕ་རོལ་གྱི་སེམས་ཤེས་པ་དང་། སྔོན་གྱི་གནས་རྗེས་སུ་དྲན་པ་སྐྱེ་བས་ཐོབ་པ་དག་གིས་ནི་དམྱལ་བ་པས་ནི་དང་པོ་ཤེས། ཇི་སྲིད་དུ་སྡུག་བསྔལ་གྱི་ཚོར་བས་མ་ཉེན་པ་དེ་སྲིད་དུ་ཤེས་སོ། །

[Block 4161]
འགྲོ་བ་གཞན་ན་གནས་པས་ནི་རྟག་ཏུ་ཤེས་སོ། །

[Block 4162]
མི་ལ་སྐྱེ་བས་ཐོབ་པ་མེད། །མི་རྣམས་ལ་ནི་རྫུ་འཕྲུལ་ལ་སོགས་པ་ཇི་སྐད་བཤད་པ་དེ་སྐྱེ་བས་ཐོབ་པ་མེད་དོ། །

[Block 4163]
འོ་ན་རང་བཞིན་གྱིས༌[^2992]ཚེ་རབས་དྲན་པ་གང་ཡིན་པ༌[^2993]ཇི་ལྟ་བུ་ཞེ་ན། དེ་དག་གི་དེ་ནི་ལས་ཀྱི་ཁྱད་པར་ལས་སྐྱེས་པ་ཡིན་ཏེ། སྔོན་གྱི་གནས་རྗེས་སུ་དྲན་པ་ནི་རྣམ་པ་གསུམ་སྟེ། བསྒོམས་པའི༌[^2994]འབྲས་བུ་དང་། སྐྱེ་བས་ཐོབ་པ་དང་། ལས་ལས་སྐྱེས་པའོ། །

[Block 4164]
ཆོས་མངོན་པ༌[^2995]མཛོད་ཀྱི་རྣམ་པར༌[^2996]བཤད་པ་ལས་ཡེ་ཤེས་བསྟན་པ་ཞེས་བྱ་བ་མཛོད་ཀྱི་གནས་བདུན་པའོ། །

[Block 4165 [HEADING]]
## སྙོམས་པར་འཇུག་པ་བསྟན་པ། ^5-0

[Block 4166]
[^2997]ཤེས་པའི་སྐབས་ཀྱིས་ཤེས་པའི་རང་བཞིན་གྱི་ཡོན་ཏན་རྣམས་ནི༌[^2998]བཤད་ཟིན་ཏོ།། །།

[Block 4167 [HEADING]]
### བསམ་གཏན་རྣམས། ^5-1-0

[Block 4168 [HEADING]]
#### བསམ་གཏན་རྣམ་པ་གཉིས། ^5-1-1-0

[Block 4169]
རང་བཞིན་གཞན་རྣམས་བརྗོད་པར་བྱ་སྟེ། དེ་ལྟ་བས་ན་ཡོན་ཏན་ཐམས་ཅད་ཀྱི་རྟེན་ཡིན་པའི་ཕྱིར་དང་པོ་ཁོ་ནར་བསམ་གཏན་རྣམས་བརྩམས་ཏེ། བསམ་གཏན་དག་ནི་རྣམ་པ་གཉིས། །བསམ་གཏན་རྣམས་ནི་མདོར་བསྡུ་ན་སྐྱེ་བ་དང་སྙོམས་པར་འཇུག་པའི་བསམ་གཏན་གྱི༌[^2999]བྱེ་བྲག་གིས་རྣམ་པ་གཉིས་སོ། །

[Block 4170]
དེ་དག་ཀྱང་བཞི། བསམ་གཏན་དང་པོ་ནས་བཞི་པའི་བར་རོ། །
--- END BLOCKS ---
