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
[Block 4026]
དེ་དག་ཐམས་ཅད་ནི། རྣམ་གྲོལ་བློ། །དགེ་སྦྱོང་གི་ཚུལ་གྱི་འབྲས་བུ་བཞིན་དུ། རྣམ་པར་གྲོལ་བའི་ལམ་གྱི་ཤེས་རབ་ཀྱི་རང་བཞིན་ཡིན་ནོ། །

[Block 4027]
བཞི་ནི་ཀུན་རྫོབ་ཤེས་པ་སྟེ། །སེམས་ཀྱི་རྣམ་གྲངས་དང་། ཟག་པ་ཟད་པ་ཤེས་པའི༌[^2870]མངོན་པར་ཤེས་པ་མ་གཏོགས་སོ། །

[Block 4028]
སེམས་ལ་ཤེས་པ་ལྔ་ཡིན་ནོ། །

[Block 4029]
སེམས་ཀྱི་རྣམ་གྲངས་མངོན་པར་ཤེས་པ་ནི༌[^2871]ལྔ་ཡིན་ཏེ། ཆོས་ཤེས་པ་དང་། རྗེས་སུ་ཤེས་པ་དང་། ལམ་དང་ཀུན་རྫོབ་དང་། ཕ་རོལ་གྱི་སེམས་ཤེས་པ་རྣམས་སོ། །

[Block 4030]
ཟག་པ༌[^2872]མངོན་ཤེས་སྟོབས་བཞིན་ནོ། །

[Block 4031]
འདི་ནི་ཟག་པ་ཟད་པ་མཁྱེན་པའི་སྟོབས་ཇི་སྐད་དུ་བཤད་པ༌[^2873]དེ་བཞིན་དུ་ཤེས་པ་དྲུག་གམ་བཅུ་ཡིན་པ་དེ༌[^2874]ཡང་རིག་པར་བྱ་ལ། དེ་བཞིན་དུ་འདི་ནི་ས་ཐམས་ཅད་པ་ཡིན་པར་ཡང་ཤེས་པར་བྱའོ། །

[Block 4032]
ལྷག་མ། ལྔ་ནི་བསམ་གཏན་བཞི་དག་ན། །མངོན་པར་ཤེས་པ་ལྔ་ནི་བསམ་གཏན་བཞིའི༌[^2875]ས་པ་དག་ཡིན་ནོ། །ཅིའི་ཕྱིར་གཟུགས་མེད་པའི་ས་པ་དག་མེད་ཅེ་ན། རེ་ཞིག་གསུམ་ནི་མེད་དེ། གཟུགས་ལ་དམིགས་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4033]
སེམས་ཀྱི་རྣམ་གྲངས་མངོན་པར་ཤེས་པ་ཡང་མེད་དེ་གཟུགས་ལ་སྟེགས་བཅས་ནས་མངོན་པར་བསྒྲུབ་པར༌[^2876]བྱ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4034]
སྔོན་གྱི་གནས་རྗེས་སུ་དྲན་པ་ཡང་མེད་དེ༌[^2877]མཐར་གྱིས་སྔོན་གྱི་གནས་གཞན་རྗེས་སུ་དྲན་པས་མངོན་པར་འགྲུབ་པའི་ཕྱིར་དང་། གནས་དང་རུས་ལ་སོགས་པ་ལ་དམིགས་པ་ཡིན་པའི་ཕྱིར་ཏེ། གཞན་གྱི་སེམས་ཤེས་པར་འདོད་པ་ནི་བདག་གི་ལུས༌[^2878]འདི་འདྲ་བ་ཞིག་ལས་སེམས་ནི་འདི་འདྲ་བ་ཞིག་ཡིན་ནོ་ཞེས་ལུས་དང་སེམས་ཀྱི་མཚན་མ་འཛིན་ཅིང་དེ་བཞིན་དུ་ཕ་རོལ་པོ་དག་ལ་ཡང་གཏོད་དེ། སེམས་ཤེས་པ་ལས་མངོན་པར་འགྲུབ་པར་འགྱུར་རོ། །

[Block 4035]
མངོན་པར་ཤེས་པ་མངོན་པར་གྲུབ་ན་ནི་གཟུགས་ལ་མི་ལྟོས་པར་མངོན༌[^2879]པར་ཤེས་སོ། །

[Block 4036]
སྔོན་གྱི་གནས་རྗེས་སུ་དྲན་པར་འདོད་པ་ནི༌[^2880]ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་འགགས་མ་ཐག་པའི་མཚན་མ་བཟུང་ནས་དེའི་ལུགས་ལས་བཟློག་སྟེ། མཚམས་སྦྱོར་བའི་སེམས་ཀྱི་བར་དུ་དེ་མ་ཐག་པའི་གནས་སྐབས་གཞན་རྣམས་ཡིད་ལ་བྱེད་དོ། །

[Block 4037]
དེ་ནས་སྲིད་པ་བར་མའི་སྐད་ཅིག་མ་གཅིག༌[^2881]དྲན་ན་ཡང་གྲུབ་པ་ཡིན་ནོ། །

[Block 4038]
དེ་བཞིན་དུ་གཞན་གྱི་ཡང་དྲན་ནོ། །

[Block 4039]
མངོན་པར་གྲུབ་ནས་ནི་ཐོད་རྒལ་དུ་ཡང་དྲན་ནོ། །

[Block 4040 [VERSE]]
སྔོན་ཉམས་སུ་མྱོང་བ་ཁོ་ན་དྲན་ནོ། །
གནས་གཙང་མ་རྣམས་ཇི་ལྟར་དྲན་ཞེ་ན།
ཐོས་པས་ཉམས་སུ་མྱོང་བའི་ཕྱིར་རོ། །

[Block 4041]
གཟུགས་མེད་པ་ནས་ཤི་འཕོས་ནས་འདིར་སྐྱེས་པ་ན༌[^2882]ཕ་རོལ་པའི༌[^2883]རྒྱུད་ལ་བརྟེན་ནས་སྐྱེད་དེ།[^2884] །གཞན་དག༌[^2885]ནི་རང་གི་རྒྱུད་ལ་བརྟེན་ནས་སོ། །

[Block 4042]
རྫུ་འཕྲུལ་ལ་སོགས་པའི་སྦྱོར་བ་ནི་ཡང་བ་དང་། སྒྲ་དང་། སྣང་བ་ཡིད་ལ་བྱེད་པ་ཡིན་ནོ། །

[Block 4043]
མངོན་པར་ཤེས་པ་ལྔ་པོ་འདི་དག་ནི། རང་དང་འོག་སའི་ཡུལ་ཅན་ཡིན། །རྫུ་འཕྲུལ་གྱི་མངོན་པར་ཤེས་པ༌[^2886]གང་ཡིན་པ་དེས་ས་དེའམ་འོག་མར་འགྲོ་བའམ་སྤྲུལ་པར་བྱེད་ཀྱི་གོང་དུ་ནི་མ་ཡིན་ནོ། །

[Block 4044]
དེ་བཞིན་དུ་ལྷའི་རྣ་བའི་མངོན་པར་ཤེས་པས་ཀྱང་རང་གི་ས་ཁོ་ནའམ་ས་འོག་མ་པའི་སྒྲ་ཐོས་ཀྱི་ས་གོང་མ་ནི་མ་ཡིན་ནོ། །

[Block 4045]
[^2887]སེམས་ཀྱི་རྣམ་གྲངས་མངོན་པར་ཤེས་པས་ཀྱང་ས་གོང་མ་པའི་སེམས་ནི༌[^2888]མི་ཤེས་སོ། །

[Block 4046]
སྔོན་གྱི་གནས་རྗེས་སུ་དྲན་པས་ཀྱང་མི་དྲན་ནོ། །

[Block 4047]
འཆི་འཕོ་བ་དང་། སྐྱེ་བ་མངོན་པར་ཤེས་པས་ཀྱང༌[^2889]མི་མཐོང་ངོ་། །དེ་ཉིད་ཀྱི༌[^2890]ཕྱིར་གཟུགས་མེད་པའི་ས་པའི་སེམས་ནི་ས་གོང་མ་པ་ཡིན་པའི་ཕྱིར། སེམས་ཀྱི་རྣམ་གྲངས་དང་། སྔོན་གྱི་གནས་མངོན་པར་ཤེས་པ་གཉིས་ཀྱིས་མི་འཛིན་ཏོ། །

[Block 4048]
འདི་དག་ཇི་ལྟར་འཐོབ་ཅེ་ན།

[Block 4049 [VERSE]]
མ་འདྲེས་པ༌[^2891]རྣམས་ཀྱི༌[^2892]སྦྱོར་བས། །
ཐོབ་བྱ་འདྲིས་པ་ཆགས་བྲལ་བས། །

[Block 4050]
མངོན་པར་ཤེས་པ་ཚེ་རབས་གཞན་ན་གོམས་པ་རྣམས་ནི་འདོད་ཆགས་དང་བྲལ་བས་འཐོབ་བོ། །

[Block 4051]
བྱེ་བྲག་ཅན་རྣམས༌[^2893]ནི་སྦྱོར་བས་སོ། །

[Block 4052]
ཐམས་ཅད་ཀྱང་སྦྱོར་བས་བསྐྱེད་པ༌[^2894]ཡིན་ནོ། །

[Block 4053]
གསུམ་པ་དྲན་པ་ཉེར་གཞག་གསུམ། །སེམས་ཀྱི་རྣམ་གྲངས་མངོན་པར་ཤེས་པ་ནི་སེམས་དང་སེམས་ལས་བྱུང༌[^2895]བ་ལ་དམིགས་པ་ཡིན་པའི་ཕྱིར།[^2896] ཚོར་བ་དང་། སེམས་དང་། ཆོས་དང༌[^2897]དྲན་པ་ཉེ་བར་གཞག་པ་གསུམ་གྱི་རང་བཞིན་ནོ། །

[Block 4054]
དང་པོ་རྫུ་འཕྲུལ་རྣ་བ་མིག །མངོན་པར་ཤེས་པ་ཞེས་བྱ་བར་སྦྱར་ཏེ། རྫུ་འཕྲུལ་དང་ལྷའི་རྣ་བ་དང་ལྷའི་མིག་གི༌[^2898]མངོན་པར་ཤེས་པ་ནི་གཟུགས་ལ་དམིགས་པ་ཡིན་པའི་ཕྱིར་དྲན་པ་ཉེ་བར་གཞག་པ་དང་པོ་ཡིན་ཏེ། ལུས་དྲན་པ་ཉེ་བར་གཞག་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 4055]
རྫུ་འཕྲུལ་གྱི་དམིགས་པ་ནི་ཕྱིའི་སྐྱེ་མཆེད་བཞི་ཡིན་ཏེ། སྒྲ་མ་གཏོགས་སོ། །

[Block 4056]
ལྷའི་རྣ་བ་དང་མིག་གི༌[^2899]མངོན་པར་ཤེས་པའི་དམིགས་པ་ནི་སྒྲ་དང་གཟུགས་ཀྱི་སྐྱེ་མཆེད་ཡིན་ནོ། །

[Block 4057]
འདི༌[^2900]ཇི་ལྟར་ན། འཆི་འཕོ༌[^2901]དང་སྐྱེ་བ་ཤེས་པས་འདི་ལྟར་སེམས་ཅན་འདི་དག་ནི་ལུས་ཀྱི༌[^2902]ཉེས་པར་སྤྱད་པ་དང་ལྡན་ནོ་ཞེས་བྱ་བ་དེ་ལྟ་བུ་ལ་སོགས་པར༌[^2903]ཤེས་ཤེ་ན། དེ་ནི་དེས་མི་ཤེས་ཀྱི་འཕགས་པ་རྣམས་ལ་དེ་ལས་གཞན་པ་གང་གིས་ན༌[^2904]དེ་ལྟ་བུར་ཤེས་པར་འགྱུར་བ་མངོན་པར་ཤེས་པའི་འཁོར་དུ་གྱུར་པའི་ཤེས་པ་སྐྱེའོ། །

[Block 4058]
ལྷག་མ་ནི་དམིགས་ཀྱིས༌[^2905]མ་ཕྱེ་བའི་ཕྱིར་དྲན་པ་ཉེ་བར་གཞག་པ་བཞི་ཆར་གྱི་རང་བཞིན་ཡིན་ནོ་ཞེས་བྱ་བར་གྲུབ་བོ། །

[Block 4059]
མིག་དང་རྣ་བའི་མངོན་ཤེས་ནི། །ལུང་དུ་མ་བསྟན་ལྷག་རྣམས་དགེ །ལྷའི་མིག་དང་རྣ་བའི་མངོན་པར་ཤེས་པ་ནི༌[^2906]ལུང་དུ་མ་བསྟན་པ་ཡིན་ནོ། །

[Block 4060]
དེ་དག་ཀྱང་མིག་དང་རྣ་བའི་རྣམ་པར་ཤེས་པ་དང་མཚུངས་པར་ལྡན་པའི་ཤེས་རབ་ཡིན་ནོ། །

[Block 4061]
འོ་ན་དེ་དག་ཇི་ལྟར་བསམ་གཏན་བཞིའི་ས་པར་གྲུབ་ཅེ་ན། རྟེན་གྱི་དབང་གིས་དེའི་ས་བསྟན་པའི་ཕྱིར་ཏེ། དེའི་རྟེན༌[^2907]མིག་དང་རྣ་བ་ནི༌[^2908]བསམ་གཏན་བཞིའི༌[^2909]ས་པ་ཡིན་ནོ། །

[Block 4062]
ཡང་ན་བར་ཆད་མེད་པའི་ལམ་གྱི་དབང་གིས་སོ། །

[Block 4063]
གཞན་བཞི་ནི་དགེ་བ་དག་ཡིན་ནོ། །

[Block 4064]
འོ་ན་རབ་ཏུ་བྱེད་པ་ལས་མངོན་པར་ཤེས་པ་གང་ཞེ་ན། ཤེས་པ་དགེ་བ་ཡིན་ནོ་ཞེས་གང༌[^2910]བཤད་པ་ཇི་ལྟ་བུ་ཞེ་ན། དེ་ནི་གཙོ་བོའམ་ཕལ༌[^2911]ཆེ་བ་བསྟན་པ་ཡིན་ནོ། །

[Block 4065 [HEADING]]
### རིག་པ་གསུམ། ^4-15-0
--- END BLOCKS ---
