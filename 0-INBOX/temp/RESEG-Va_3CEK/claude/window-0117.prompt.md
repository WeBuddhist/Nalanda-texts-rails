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
[Block 4096 [HEADING]]
##### མོས་པ་ལས་བྱུང་བ། ^4-17-1-3-0

[Block 4097]
མོས་པ་ལས་བྱུང་བ་ཡང་ཡོད་དེ། ཐག་རིང་པོ་ལ་ཉེ་བར་མོས་ནས་མྱུར་དུ་འགྲོ་བའི་ཕྱིར་རོ། །

[Block 4098 [HEADING]]
#### སྤྲུལ་པ། ^4-17-2-0

[Block 4099]
སྤྲུལ་པ་ནི་རྣམ་པ་གཉིས་ཏེ། འདོད་པ་ན་སྤྱོད་པ་དང་། གཟུགས་ན་སྤྱོད་པའོ། །

[Block 4100 [HEADING]]
##### འདོད་པར་གཏོགས་པའི་སྤྲུལ་པ། ^4-17-2-1-0

[Block 4101]
[^2936]དེ་ལ་རེ་ཞིག །འདོད་པར་གཏོགས་པའི་སྤྲུལ་པ་ནི། ཕྱིའི་སྐྱེ་མཆེད་བཞི། འདོད་པ་ན་སྤྱོད་པའི་སྤྲུལ་པ་ནི་གཟུགས་དང་དྲི་དང་རོ་དང་རེག་བྱའི་སྐྱེ་མཆེད་ཀྱི་རང་བཞིན་ཡིན་ནོ། །

[Block 4102]
དེ་ཡང་རྣམ་གཉིས། བདག་དང་གཞན་གྱི་ལུས་དང་སྤྲུལ་པའོ། །

[Block 4103 [HEADING]]
##### གཟུགས་ན་སྤྱོད་པའི་སྤྲུལ་པ། ^4-17-2-2-0

[Block 4104]
གཟུགས་གཏོགས༌[^2937]གཉིས། གཟུགས་ན་སྤྱོད་པའི་སྤྲུལ་པ་ནི། དེ་ན་དྲི་དང་རོ་མེད་པའི་ཕྱིར་གཟུགས་དང་རེག་བྱའི་སྐྱེ་མཆེད་གཉིས་ཡིན་ནོ། །

[Block 4105]
དེ་ཡང་འདོད་པའི་ཁམས་ཀྱི་ཇི་ལྟ་བ་དེ་ཁོ་ན་བཞིན་དུ་རྣམ་པ་གཉིས་ཡིན་ཏེ། འདི་ནི་སྤྲུལ་པ་རྣམ་པ་བཞི་ཡིན་ནོ། །

[Block 4106]
གཟུགས་ཀྱི་ཁམས་ན་ཡང་དེ་དང་འདྲ་བས་མདོར་བསྡུ་ན་སྤྲུལ་པ་ནི་རྣམ་པ་བརྒྱད་ཡིན་ནོ། །

[Block 4107]
གཟུགས་ཀྱི་ཁམས་སུ་སྐྱེས་པ་འདོད་པ་ན་སྤྱོད་པ་སྤྲུལ་པ་ན༌[^2938]ཇི་ལྟར་ན་དྲི་དང་རོ་དག་དང་མི་ལྡན་པ་ཡང་ཡིན་ཞེ་ན། གོས་དང་། རྒྱན་བཞིན་དུ་མི་ལྡན་ནོ། །

[Block 4108]
གཞན་དག་ན་རེ་སྐྱེ་མཆེད་གཉིས་སྤྲུལ་པར་བྱེད་དོ་ཞེས་ཟེར་རོ། །

[Block 4109 [HEADING]]
#### སྤྲུལ་པའི་སེམས། ^4-17-3-0

[Block 4110]
ཡང་ཅི་མངོན་པར་ཤེས་པ་ཁོ་ནས་སྤྲུལ་པ་སྤྲུལ༌[^2939]པར་བྱེད་དམ་ཞེ་ན། སྨྲས་པ། མ་ཡིན་ནོ། །

[Block 4111]
[^2940]འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན། མངོན་པར་ཤེས་པའི་འབྲས་བུ། སྤྲུལ་སེམས་དག་གིས་དེ་དག་ཀྱང་ནི་བཅུ་བཞིའོ། །

[Block 4112]
སྤྲུལ་པའི་སེམས་བཅུ་བཞི་པོ་དེ་དག་ནི། བསམ་གཏན་འབྲས་གཉིས་ནས་ལྔའི་བར་རིམ་བཞིན། བསམ་གཏན་དང་པོའི་འབྲས་བུ་སྤྲུལ་པའི་སེམས་ནི་གཉིས་ཏེ། འདོད་པའི་ཁམས་དང་བསམ་གཏན་དང་པོའི་ས་པ་དག་གོ། །

[Block 4113]
[^2941]བསམ་གཏན་གཉིས་པའི་འབྲས་བུ་ནི་གསུམ་སྟེ། འདོད་པའི་ཁམས་དང་། བསམ་གཏན་དང་པོ་དང་། གཉིས་པའི་ས་པ་དག་གོ། །

[Block 4114]
དེ་བཞིན་དུ་བསམ་གཏན་གསུམ་པ་དང་། བཞི་པའི་ས་པ་དག་ཀྱང་བཞི་དང་ལྔར་སྦྱོར་བར༌[^2942]བྱའོ། །

[Block 4115]
བསམ་གཏན་གྱི་འབྲས་བུ་སྤྲུལ་པའི་སེམས་ནི་རང་གི་ས་པ་དང་ས་འོག་མ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 4116]
གོང་མ་ལས་སྐྱེས་མིན། བསམ་གཏན་འོག་མའི་འབྲས་བུ་ས་གོང་མའི་སྤྲུལ་པའི་སེམས་ནི་མེད་དོ། །

[Block 4117]
འདོད་པ་ན་སྤྱོད་པའི་སྤྲུལ་པ་བསམ་གཏན་གཉིས་པ་ལ་སོགས་པའི་འབྲས་བུ་ནི། བསམ་གཏན་དང་པོའི་ས་པ་དེའི་འབྲས་བུ་ལས་འགྲོས་ཀྱི་སྒོ་ནས་ཁྱད་པར་དུ་འཕགས་སོ། །

[Block 4118]
དེ་རྙེད་བསམ་གཏན་བཞིན། སྤྲུལ་པའི་སེམས་དེ་དག་རྙེད་པ་ནི་བསམ་གཏན་བཞིན་ནོ། །

[Block 4119]
ཡང་ཅི་སྤྲུལ་པའི་སེམས་ཁོ་ན་ལས་ལྡང་བར་འགྱུར་རམ་ཞེ་ན། དེ་ལྟ་བུ་ནི་མེད་དེ། འདི་ལྟར། དེ་ནི། དག་དང་རང༌[^2943]ལས་སྐྱེ་བར་འགྱུར་ཏེ།[^2944] སྤྲུལ་པའི་སེམས་ནི་བསམ་གཏན་དག་པ་པའམ་སྤྲུལ་པའི་སེམས་ཀྱི་མཇུག་ཐོགས་སུ་སྐྱེའི་གཞན་དུ༌[^2945]ནི་མ་ཡིན་ནོ། །

[Block 4120]
དེ་ལས་གཉིས། སྤྲུལ་པའི་སེམས་ལས་ཀྱང་བསམ་གཏན་དག་པ་པ་དང་སྤྲུལ་པའི་སེམས་སྐྱེ་སྟེ། གཞན་དུ་ནི༌[^2946]མ་ཡིན་ནོ། །

[Block 4121]
ཏིང་ངེ་འཛིན་གྱི་འབྲས་བུ་ལ་གནས་པ་ནི༌[^2947]ཡང་ཏིང་ངེ་འཛིན་ལ་མ་ཞུགས་པར་ཏིང་ངེ་འཛིན་དེ་ལས་ལྡང་བ་མེད་དོ། །

[Block 4122]
སྤྲུལ་པ་ཐམས་ཅད་ཀྱང་། རང་གི་ས་པས་སྤྲུལ་པར་བྱེད། ས་གཞན་པའི་སྤྲུལ་པའི་སེམས་ཀྱིས་ས༌[^2948]གཞན་པའི༌[^2949]སྤྲུལ་པར་ནི་མི་བྱེད་དོ། །

[Block 4123]
སྨྲར་འཇུག་པ་ནི་འོག་མས་ཀྱང་། ཀྱང་ཞེས་བྱ་བའི་སྒྲ་ནི་རང་གི་ས་པས་ཀྱང་སྨྲར་འཇུག་གོ་ཞེས་བྱ་བ་ཡིན་ཏེ། འདོད་པའི་ཁམས་དང་། བསམ་གཏན་དང་པོའི་ས་པའི་སྤྲུལ་པ་ནི་རང་གི་ས་པའི་སེམས་ཁོ་ནས་སྨྲར་འཇུག་གོ། །

[Block 4124]
ས་གོང་མ་པ་ནི་བསམ་གཏན་དང་པོའི་ས་པ་སྟེ། ཡན་ཆད་ན་རྣམ་པར་རིག་བྱེད་ཀུན་ནས་སློང་བར་བྱེད་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 4125]
སྤྲུལ་པ་མང་པོ་རྣམས་སྨྲ་བ་ནི་སྟོན་མིན་སྤྲུལ་པ་དང་བཅས། སངས་རྒྱས་ལས་གཞན་པའི་སྤྲུལ་པ་ནི་སྤྲུལ་པ་དང་བཅས་ཏེ། སྨྲ་བས་གང་གི་ཚེ་སྤྲུལ་པ་མང་པོ་ཞིག་ཡིན་པ་དེའི་ཚེ་ཅིག་ཅར་སྨྲ་སྟེ།

[Block 4126 [VERSE]]
གཅིག་ཅིག༌[^2950]སྨྲ་བར་བྱེད་པ་ན། །
སྤྲུལ་པ་ཐམས་ཅད་སྨྲ་བར་བྱེད། །
གཅིག་མི་སྨྲ་བར་གྱུར་པ་དང་། །
དེ་དག་ཐམས་ཅད་སྨྲར་མི་འགྱུར། །

[Block 4127]
ཞེས༌[^2951]ཚིགས་སུ་བཅད་དེ་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 4128]
སངས་རྒྱས་ཀྱི་སྤྲུལ་པ་ནི་སྔ་ཕྱི་ཇི་ལྟར་བཞེད་པར་སྨྲའོ། །

[Block 4129]
གང་གི་ཚེ་སྨྲར་འཇུག་པའི་སེམས་ཡོད་པ་དེའི་ཚེ་སྤྲུལ་པའི་སེམས་མེད་པའི་ཕྱིར་སྤྲུལ་པ་མེད་ན་ཇི་ལྟར་སྨྲར་འཇུག་ཅེ་ན། བྱིན་གྱིས་བརླབས་ནས་གཞན་འཇུག་ཕྱིར། །གནས་པར་འདོད་པས་སྤྲུལ་པ་བྱིན་གྱིས་བརླབས་ནས་ཡིད་གཞན་རྣམ་པར་རིག་བྱེད་ཀུན་ནས་སློང་བར་བྱེད་པས་ངག་འཇུག་པར་བྱེད་དོ། །

[Block 4130]
ཅི་གསོན་པོ་ཁོ་ན་ལ་བྱིན་གྱི༌[^2952]རླབས་ཡོད་དམ། འོན་ཏེ་ཤི་བ་ལ་ཡོད་ཅེ་ན། ཤི་བ་ལ་ཡང་བྱིན་གྱི༌[^2953]རླབས་ཡོད། འཕགས་པ་འོད་སྲུངས་ཆེན་པོའི་བྱིན་གྱི༌[^2954]རླབས་ཀྱིས་དེའི་རུས་པའི་ཀེང་རུས་གནས་པའི་ཕྱིར་རོ། །

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
--- END BLOCKS ---
