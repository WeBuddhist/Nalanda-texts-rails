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
[Block 3956]
ཆོས་གཞན་སློབ་དང་ཐུན་མོང་མིན།[^2793] །སངས་རྒྱས་རྣམས་ཀྱི་ཡོན་ཏན་གཞན་དག་ནི་ཉན་ཐོས་དང་ཐུན་མོང་ཡིན་ནོ། །

[Block 3957]
ཁ་ཅིག་སོ་སོའི་སྐྱེ་བོ་དང་། དེ་དག་ཀྱང་གང་ཞེ་ན། ཅི་རིགས་པར།

[Block 3958 [VERSE]]
ཉོན་མོངས་མེད་དང་སྨོན་ནས་ཤེས། །
སོ་སོ༌[^2794]ཡང་དག་རིག་སྔོན༌[^2795]སོགས། །

[Block 3959]
ཉོན་མོངས་པ་མེད་པ་དང་། སྨོན་ནས་ཤེས་པ་དང་། སོ་སོ་ཡང་དག་པར་རིག་པ་དང་། མངོན་པར་ཤེས་པ་དང་། བསམ་གཏན་དང་། གཟུགས་མེད་པ་དང་། ཚད་མེད་པ་དང་། རྣམ་པར་ཐར་པ་དང་། ཟིལ་གྱིས་གནོན་པའི་སྐྱེ་མཆེད་དང་། ཟད་པར་གྱི་སྐྱེ་མཆེད་ལ་སོགས་པའོ། །

[Block 3960 [HEADING]]
#### ཉོན་མོངས་པ་མེད་པ། ^4-13-1-0

[Block 3961]
དེ་ལ་ཉོན་མོངས་པ་མེད་པ་ཞེས་བྱ་བ་ནི་དགྲ་བཅོམ་པ་ལ་ལ་སེམས་ཅན་རྣམས་ཀྱི་སྡུག་བསྔལ་ནི་ཉོན་མོངས་པ་ལས་རབ་ཏུ་སྐྱེ་བ་དང་། བདག་ཉིད་ཀྱང་ཡོན་གནས་གྱི༌[^2796]ཁྱད་པར་ཡིན་པར་རིག་ནས་ཕ་རོལ་པོ་དག་དེ་ལ་དམིགས་ནས། ཉོན་མོངས་པ་སྐྱེ་བ་ཡོངས་སུ་སྤངས་པར་འདོད་དེ།[^2797] གང་གིས་ན་ཕ་རོལ་པོ་དག་རྣམ་པ་ཐམས་ཅད་དུ་ཉོན་མོངས་པ་སྐྱེ་བར༌[^2798]མི་བྱེད་ཅིང་འགའ་ཡང་དེ་ལ་དམིགས་ནས་འདོད་ཆགས་སམ། ཞེ་སྡང་ངམ། ང་རྒྱལ་སྐྱེ་བར་མི་འགྱུར་བ་དེ་ལྟ་བུའི་ཤེས་པ་སྐྱེད་པར་བྱེད་པ་སྟེ། ལམ་དེ་ནི་འགའ་ཡང་ཉོན་མོངས་པ་སྐྱེད༌[^2799]པར་མི་བྱེད་པས་ན་ཉོན་མོངས་པ་མེད་པ་ཡིན་ནོ། །

[Block 3962]
ཉོན་མོངས་པ་མེད་པ་དེ་ནི། ཀུན་རྫོབ་ཤེས། དེའི་རང་བཞིན་ནི་འདི་ཡིན་ནོ། །

[Block 3963]
བསམ་གཏན་མཐའ་ན་བསམ་གཏན་བཞི་པའི་ས་པ་ཡིན་ཏེ། [^2800]ལམ་སླ་བ་རྣམས་ཀྱི་མཆོག་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3964]
མི་གཡོ་བའི་ཆོས། དགྲ་བཅོམ་པ་གཞན་གྱིས་ནི་མ་ཡིན་ཏེ། གཞན་ནི་རེས་འགའ་རང་གི་རྒྱུད་ལས་ཀྱང་ཉོན་མོངས་པ་མཐའ་དག༌[^2801]ཡོངས་སུ་སྤང་བར་མི་ནུས་སོ། །

[Block 3965]
མིས་སྐྱེད། གླིང་གསུམ་དུ་མི་དག་གི་ནང་ཁོ་ནར་སྐྱེད་པར་བྱེད་དོ། །

[Block 3966]
[^2802]ཉོན་མོངས་འདོད༌[^2803]གཏོགས་པ། [^2804]མ་སྐྱེད་གཞིར༌[^2805]བཅས་སྤྱོད་ཡུལ་ཅན། འདིའི་དམིགས་པ་ནི་ཉོན་མོངས་པ་འདོད་པ་ན་སྤྱོད་པ་མ་འོངས་པ་གཞི༌[^2806]དང་བཅས་པ་རྣམས་ཡིན་ཏེ། ཕ་རོལ་པོ་དག་ཉོན་མོངས་པ་སྐྱེ་བར་མ་གྱུར་ཅིག་ཅེས་བྱ་བ་དེ་ལྟར་ཞུགས་པའི་ཕྱིར་རོ། །

[Block 3967]
ཉོན་མོངས་པ་གཞི༌[^2807]མེད་པ་རྣམས་ནི་ཡོངས་སུ་སྤང་བར་མི་ནུས་ཏེ། ཐམས་ཅད་དུ་འགྲོ་བ་རྣམས་ནི་རང་གི་ས་མཐའ་དག་ལ་དམིགས་པའི་ཕྱིར་རོ། །

[Block 3968 [HEADING]]
#### སྨོན་ནས་ཤེས་པ། ^4-13-2-0

[Block 3969]
ཉོན་མོངས་པ༌[^2808]མེད་པ༌[^2809]ཇི་སྐད་དུ་བཤད་པ། སྨོན་ནས་ཤེས་པའང་དེ་བཞིན་ནོ། །

[Block 3970 [VERSE]]
དེ༌[^2810]ཡང་ཀུན་རྫོབ་ཤེས་པ་དང་། །
བསམ་གཏན་མཐའ་ན་ཡོད་པ་དང་། །

[Block 3971]
མི་གཡོ་བའི་ཆོས་ཅན་གྱི་ཡིན་པ་དང་། མིའི་རྟེན་ཅན༌[^2811]ཡིན་ནོ། །

[Block 3972]
དེའི་དམིགས་པ་ཐམས་ཅད་དོ། །

[Block 3973]
སྨོན་ནས་ཤེས་པའི་དམིགས་པ་ནི་ཆོས་ཐམས་ཅད་ཡིན་པས་འདི་ནི་བྱེ་བྲག་ཡིན་ནོ། །

[Block 3974]
བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ་སྨོན་ནས་ཤེས་པ༌[^2812]གཟུགས་མེད་པ་རྣམས་མངོན་སུམ་དུ༌[^2813]མི་ཤེས་སོ། །

[Block 3975]
འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན། རྒྱུ་མཐུན་པ་དང་སྤྱོད་པའི་བྱེ་བྲག༌[^2814]ལས་ཤེས་ཏེ། འདིར་དཔེ་ནི་ཞིང་པ་ལྟ་བུའོ་ཞེས་ཟེར་རོ། །

[Block 3976]
སྨོན་པ་སྔར་བཏང་བའི་ཤེས་པ་ནི་སྨོན་ནས་ཤེས་པ་སྟེ། འདི་ཤེས་པར་བྱའོ་སྙམ་དུ་སྨོན་ནས་རབ་ཀྱི་མཐའི༌[^2815]བསམ་གཏན་བཞི་པ་ལ་སྙོམས་པར་འཇུག་ཅིང་། ཏིང་ངེ་འཛིན་དེའི་ཡུལ་དུ་ཇི་ཙམ་ཞིག་གྱུར་པ་གང་ཡིན་པ་དེ་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་རབ་ཏུ༌[^2816]ཤེས་པའོ། །

[Block 3977 [HEADING]]
#### སོ་སོ་ཡང་དག་པར་རིག་པ། ^4-13-3-0

[Block 3978 [VERSE]]
དེ་བཞིན་ཆོས་དོན་ངེས་ཚིག་དང་། །
སྤོབས་པ་སོ་སོ་ཡང་དག་རིག །

[Block 3979]
སོ་སོ་ཡང་དག་པར་རིག་པ་ནི་བཞི་སྟེ། ཆོས་སོ་སོ་ཡང་དག་པར་རིག་པ་དང་། དོན་སོ་སོ་ཡང་དག་པར་རིག་པ་དང་། ངེས་པའི་ཚིག་སོ་སོ་ཡང་དག་པར་རིག་པ་དང་། སྤོབས་པ་སོ་སོ་ཡང་དག་པར་རིག་པའོ། །

[Block 3980]
དེ་དག་ཀྱང་ཉོན་མོངས་པ་མེད་པ༌[^2817]ཇི་ལྟ་བ་དེ་དང་འདྲའོ། །

[Block 3981]
དེ་དག་གི་དེ་དང་འདྲ་བ་ཅི་ཞེ་ན། མི་གཡོ་བའི་ཆོས་ཅན་གྱི་ཡིན་པ་དང་། མིའི་རྟེན་ཅན་ཉིད་ཡིན་ནོ། །

[Block 3982]
འདི་དག་གི་དམིགས་པ་དང་། ས་དང་། རང་གི་ངོ་བོའི་བྱེ་བྲག་ནི་ཐ་དད་པར་བརྗོད་དེ།

[Block 3983 [VERSE]]
གསུམ་ནི་གོ་རིམས་བཞིན་མིང་དང་། །
དོན་དང་ངག་ལ་ཐོགས་མེད་ཤེས། །

[Block 3984]
ཆོས་དང་དོན་དང་ངེས་པའི་ཚིག་སོ་སོ་ཡང་དག་པར་རིག་པ་རྣམས་ནི་གོ་རིམས་བཞིན་དུ་མིང་དང་ཚིག་དང་ཡི་གེའི་ཚོགས་རྣམས་དང་། དོན་དང་ངག་ལ༌[^2818]ཐོགས་པ་མེད་པར་ཤེས་པ་ཡིན་ནོ། །

[Block 3985 [VERSE]]
བཞི་པ་རིགས་པ༌[^2819]ཐགས་ཐོགས་མེད། །
མངོན་བརྗོད་ལམ་ལ་དབང་ཉིད་དང་། །

[Block 3986]
ཐོགས་པ་མེད་པར་ཤེས་པ་ཞེས་བྱ་བར་སྦྱར་ཏེ། སྤོབས་པ་སོ་སོ་ཡང་དག་པར་རིག་པ་ནི་རིགས་པ༌[^2820]དང་། ཐགས༌[^2821]ཐོགས་མེད་པར་མངོན་པར་བརྗོད་པ་ཉིད་དང་། ཏིང་ངེ་འཛིན་ལ་དབང༌[^2822]གསལ་བར་བྱ་བ་ལ་ཐོགས་པ་མེད་པར་ཤེས་པ་ཡིན་ནོ། །

[Block 3987]
དེ་ཡི་དམིགས་པ་ངག་དང་ལམ། །དེའི་དམིགས་པ༌[^2823]ནི་ངག་ཀྱང་ཡིན་ལ་ལམ་ཡང་ཡིན་ནོ། །ཤེས་པ་དགུའོ། །

[Block 3988]
སྤོབས་པ་སོ་སོ་ཡང་དག་པར་རིག་པ་ནི་ཤེས་པ་དགུའི་རང་བཞིན་ཡིན་ཏེ། འགོག་པ་ཤེས་པ་མ་གཏོགས་སོ། །

[Block 3989]
ས་ཐམས་ཅད། འདི་ནི་ངག་དང་ལམ༌[^2824]གཉིས་ལས་གང་ཡང་རུང་བ་ཞིག་ལ་དམིགས་པའི་ཕྱིར་འདོད་པའི་ཁམས་ནས་སྲིད་པའི་རྩེ་མོའི་བར་ས་ཐམས་ཅད་པ་ཡང་ཡིན་ནོ། །

[Block 3990]
ཡང་དག་དོན་རིག་བཅུའམ་དྲུག །དོན་སོ་སོ་ཡང་དག་པར༌[^2825]རིག་པ་ནི་གལ་ཏེ་དོན་ཆོས་ཐམས་ཅད་ཡིན་ན་ནི༌[^2826]ཤེས་པ་བཅུ་ཡིན་ནོ། །

[Block 3991]
གལ་ཏེ་དོན་མྱ་ངན་ལས་འདས་པ་ཡིན་ན་ནི་ཤེས་པ་དྲུག་སྟེ། ཆོས་ཤེས་པ་དང་། རྗེས་སུ་ཤེས་པ་དང་། འགོག་པ་དང་ཟད་པ་དང་མི་སྐྱེ་བ་དང་། ཀུན་རྫོབ་ཤེས་པ་རྣམས་སོ། །

[Block 3992]
དོན༌[^2827]ནི་ཀུན་ན། དོན་སོ་སོ་ཡང་དག་པར་རིག་པ་དེ་ནི་ས་ཐམས་ཅད་པ་ཡིན་ནོ། །

[Block 3993]
གཞན་ཀུན་རྫོབ། གཞན་ཆོས་དང་ངེས་པའི་ཚིག་སོ་སོ་ཡང་དག་པར་རིག་པ་གཉིས་ནི་ཀུན་རྫོབ་ཤེས་པའི་རང་བཞིན་དག་ཡིན་ཏེ། [^2828]མིང་གི་ཚོགས་ལ་སོགས་པ་དང་།

[Block 3994 [VERSE]]
ངག་ལ་དམིགས་པའི་ཕྱིར་རོ། །
ཆོས་རིག་འདོད་དང་བསམ་གཏན་ན། །

[Block 3995]
ཆོས་སོ་སོ་ཡང་དག་པར་རིག་པ་ནི༌[^2829]ས་ལྔ་པོ་འདོད་པའི་ཁམས་དང་། བསམ་གཏན་བཞིས་བསྡུས་པ་ཡིན་ཏེ། ཡན་ཆད་ན་མིང་གི་ཚོགས་མེད་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
