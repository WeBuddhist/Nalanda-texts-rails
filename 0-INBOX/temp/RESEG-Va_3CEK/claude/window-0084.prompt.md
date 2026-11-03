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
[Block 2941]
གསུམ་པ་ལ༌[^2024]ནི་དགུའོ། །

[Block 2942]
བཞི་པ་ལ༌[^2025]བཅུ་གཉིས་སོ། །

[Block 2943]
ལྔ་པ་ལ་ནི་བཅོ་ལྔ་སྟེ། དེ་དག་གི་འབྲས་བུ་ནི་གྲངས་བཞིན་དུ་གནས་གཙང་མ་ལྔ་ཡིན་ལ་དེ་ལ་ཟག་པ་དང་བཅས་པ་གང་ཡིན་པ་དེའི་དབང་གིས་དེ་དག་ཏུ་སྐྱེའོ། །

[Block 2944]
གཞན་དག་ན་རེ་དད་པའི་དབང་པོ་ལ་སོགས་པ་ལྷག་པའི་ཕྱིར་ལྔ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 2945 [HEADING]]
###### ལུས་ཀྱིས་མངོན་དུ་བྱེད་པ། ^3-2-8-7-11-0

[Block 2946 [VERSE]]
འགོག་པ་ཐོབ་པའི་ཕྱིར་མི་འོང་། །
ལུས་ཀྱིས་མངོན་དུ་བྱེད་པར་འདོད། །

[Block 2947]
འདི་ལ་འགོག་པའི༌[^2026]ཐོབ་པ༌[^2027]ཡོད་པས་ན་འགོག་པ་ཐོབ་པ་སྟེ།[^2028] ཕྱིར་མི་འོང་བ་གང་ལ་ལ་འགོག་པ་ཐོབ་པ་དེ་ནི་མྱ་ངན་ལས་འདས་པ་དང་འདྲ་བའི་ཆོས་ལུས་ཀྱིས་མངོན་སུམ་དུ་བྱེད་པའི་ཕྱིར་ལུས་ཀྱིས་མངོན་སུམ་དུ་ཐོབ་པ༌[^2029]ཞེས་བྱའོ། །ཇི་ལྟར་ན་ལུས་ཀྱིས་མངོན་སུམ་དུ་བྱེད་ཅེ་ན། སེམས་མེད་པས་ལུས་ལ་བརྟེན་ཏེ་སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 2948]
འདི་ལྟ་བུ་ཡིན་པར་འགྱུར་ཏེ། དེ་འགོག་པ་དེ་ལས་ལངས་ནས་གང་ལས་དེ་ནི༌[^2030]འདི་སྙམ་དུ་ཀྱེ་མ་འགོག་པའི་སྙོམས་པར་འཇུག་པ་ནི་མྱ་ངན་ལས་འདས་པ་དང་འདྲ་བར་ཞི་བ་ཡིན་ནོ་སྙམ་དུ་སེམས་པར་འགྱུར་བ་རྣམ་པར་ཤེས་པ་དང་བཅས་པའི་ལུས་ཞི་བ་སྔོན་མ་ཐོབ་པ་ཐོབ་པར་འགྱུར་ཏེ། དེ་ལྟར་ན་འདིས་དེའི་ཞི་བ་ཉིད་དུ༌[^2031]ལུས་ཀྱིས་མངོན་དུ་བྱས་པ་ཡིན་ཏེ། ཐོབ་པ་དང་ཤེས་པས་མངོན་སུམ་དུ་བྱེད་པ་དག་གིས་མངོན་སུམ་དུ་གྱུར་པ་ནི་མངོན་དུ་བྱེད་པ་ཡིན་ནོ། །

[Block 2949]
མདོ་ལས་སློབ་པ་བཅོ་བརྒྱད་ཅེས་གསུངས་པ་དེར་ལུས་ཀྱིས་མངོན་དུ་བྱེད་པ་ཅིའི་ཕྱིར་མ་གསུངས་ཤེ་ན། རྒྱུ་མེད་པའི་ཕྱིར་རོ། །

[Block 2950]
རྒྱུ་གང་ཞིག༌[^2032]ཡིན་ཞེ་ན། ཟག་པ་མེད་པའི་སློབ་པ་གསུམ་དང་དེའི་འབྲས་བུ་སྟེ། དེའི་ཁྱད་པར་གྱིས་སློབ་པ་རྣམས་རྣམ་པར་གཞག་གོ། །

[Block 2951]
འགོག་པའི་སྙོམས་པར་འཇུག་པ་ནི་སློབ་པ་ཡང་མ་ཡིན་ལ་སློབ་པའི་འབྲས་བུ་ཡང་མ་ཡིན་ཏེ། དེའི་ཕྱིར་དེ་དང་ལྡན་པས་སློབ་པའི་ཁྱད་པར་དུ་མ་གསུངས་སོ། །

[Block 2952]
འདི་ནི་རེ་ཞིག་ཕྱིར་མི་འོང་བ་རྣམས་ཀྱི་དབྱེ་བ་ཆེ་ལོང་ཡིན་ནོ། །

[Block 2953 [HEADING]]
###### ཞིབ་ཏུ་དབྱེ་བ། ^3-2-8-7-12-0

[Block 2954]
ཞིབ་ཏུ་དབྱེ་ན་ནི་སྟོང་ཕྲག་ཏུ་དབྱེ་བ་ཡོད་དེ། བར་མ་དོར་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་ལ་དབང་པོ་རྟུལ་པོ་དང་འབྲིང་པོ་དང་རྣོན་པོའི་བྱེ་བྲག་གིས་གསུམ་མོ། །

[Block 2955]
དེ་དག་ཉིད་སའི་བྱེ་བྲག་གིས་བཞིའོ། །

[Block 2956]
ཡོངས་སུ་ཉམས་པའི་ཆོས་ཅན་ལ་སོགས་པའི་རིགས་ཀྱི་བྱེ་བྲག་གིས་དྲུག་གོ། །

[Block 2957]
གནས་གཞན་གྱི༌[^2033]བྱེ་བྲག་གིས་བཅུ་དྲུག་གོ། །

[Block 2958]
ས་དང་འདོད་ཆགས་དང་བྲལ་བའི་བྱེ་བྲག་གིས་སུམ་ཅུ་རྩ་དྲུག་སྟེ། གཟུགས་ཀྱི་ཁམས་ཀྱི༌[^2034]འཆིང་བ་མཐའ་དག་དང་ལྡན་པ་ནས་བསམ་གཏན་བཞི་པའི་རྣམ་པ་བརྒྱད་ལས་འདོད་ཆགས་དང་བྲལ་བའི་བར༌[^2035]རོ། །

[Block 2959]
གནས་གཞན་དང་རིགས་དང་འདོད་ཆགས་དང་བྲལ་བ་དང་དབང་པོའི་བྱེ་བྲག་གིས་ཉིས་སྟོང་ལྔ་བརྒྱ་དགུ་བཅུ་རྩ་གཉིས་ཏེ། ཇི་ལྟར་བྱས་པས་ཤེ་ན། གནས་གཅིག་ན་རིགས་དྲུག་གོ། །

[Block 2960]
རིགས་རེ་རེ་ལ༌[^2036]འཆིང་བ་མཐའ་དག་དང་ལྡན་པ་ནས་རང་གི་གནས་ཀྱི་རྣམ་པ་བརྒྱད་ལས་འདོད་ཆགས་དང་བྲལ་བའི་བར་གང་ཟག་དགུ་དགུ་སྟེ། དགུ་དྲུག་ནི་ལྔ་བཅུ་བཞིའོ། །

[Block 2961]
ལྔ་བཅུ་རྩ་བཞི་ཕྲག་བཅུ་དྲུག་ནི་བརྒྱད་བརྒྱ༌[^2037]དྲུག་ཅུ་རྩ་བཞིའོ། །

[Block 2962]
ཡང་དབང་པོའི་བྱེ་བྲག་གིས་སུམ་འགྱུར་ཏེ། དེ་ལྟར་བྱས་པས་སོ། །

[Block 2963]
འདྲ་བར་རྩེ་བའི༌[^2038]ཕྱིར་བསམ་གཏན་འོག་མའི་རྣམ་པ་དགུ་ལས་འདོད་ཆགས་དང་བྲལ་བ་གང་ཡིན་པ་དེ་ནི་གོང་མའི་འཆིང་བ་མཐའ་དག་དང་ལྡན་པར་བཤད་པ་ཡིན་ནོ། །

[Block 2964]
བར་མ་དོར་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་ཇི་ལྟ་བར་གོང་དུ་འཕོ་བའི༌[^2039]བར་དུ་ཡང་དེ་དང་འདྲ་བས་ཐམས་ཅད་བསྡུས་ན་ཕྱིར་མི་འོང་བ༌[^2040]ཁྲི་ཉིས་སྟོང་དགུ་བརྒྱ་དྲུག་ཅུ་ཡིན་ནོ། །

[Block 2965 [HEADING]]
##### དགྲ་བཅོམ་པ་ཉིད་ལ་ཞུགས་པ། ^3-2-8-8-0

[Block 2966 [VERSE]]
སྲིད་རྩེའི་བར་ཆ་བརྒྱད་ཟད་པ། །
དགྲ་བཅོམ་ཉིད་ལ་ཞུགས་པ་ཡིན། །

[Block 2967]
ཕྱིར་མི་འོང་བ་ཞེས་བྱ་བའི་དབང་དུ་བྱས་པ་སྟེ། ཡང་ཕྱིར་མི་འོང་བ༌[^2041]དེ་བསམ་གཏན་དང་པོའི་རྣམ་པ་གཅིག་ལས༌[^2042]འདོད་ཆགས་དང་བྲལ་བ་ནས་བཟུང་སྟེ། སྲིད་པའི་རྩེ་མོའི་རྣམ་པ་བརྒྱད་ཀྱི་བར་སྤངས་པས་དགྲ་བཅོམ་པ་ཉིད་ལ་ཞུགས་པ་ཡིན་ནོ། །

[Block 2968]
དགུ་ཡི༌[^2043]བར་ཆད་མེད་ལམ་ཡང་། །དེ་སྲིད༌[^2044]པའི་རྩེ་མོའི་རྣམ་པ༌[^2045]

[Block 2969]
དགུ་པ་སྤོང་བར་བྱེད་པའི་བར་ཆད་མེད་པའི་ལམ་ལ་གནས་པ་ན། ཡང་དགྲ་བཅོམ་པ་ཉིད་ལ་ཞུགས་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 2970 [HEADING]]
##### རྡོ་རྗེ་ལྟ་བུའི་ཏིང་ངེ་འཛིན། ^3-2-8-9-0

[Block 2971]
དེ་ནི་རྡོ་རྗེ་ལྟ་བུ་ཡིན། །བར་ཆད་མེད་པའི་ལམ་དེ་ནི་ཕྲ་རྒྱས་ཐམས་ཅད་འཇོམས་པར་བྱེད༌[^2046]པ་ཡིན་པའི་ཕྱིར་རྡོ་རྗེ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་ཞེས་བྱའོ། །

[Block 2972]
བཅོམ་ཟིན་པའི་ཕྱིར་འདིས་ཐམས་ཅད་འཇོམས་པ་ནི་མ་ཡིན་གྱི། བར་ཆད་མེད་པའི་ལམ་ཐམས་ཅད་ཀྱི་ནང་ནས༌[^2047]ཤིན་ཏུ་ཆེ་བ་ཡིན་པའི་ཕྱིར་ཐམས་ཅད༌[^2048]འཇོམས་པར་ནུས་པ་ཡིན་ནོ། །

[Block 2973]
རྡོ་རྗེ་ལྟ་བུ་རྣམས་ཀྱི་བྱེ་བྲག་ནི་རྣམ་པ་མང་པོ་ཞིག་ཏུ་བརྗོད་དེ། མི་ལྕོགས་པ༌[^2049]མེད་པས་བསྡུས་པ་སྲིད་པའི་རྩེ་མོའི་སྡུག་བསྔལ་དང་ཀུན་འབྱུང་ལ་དམིགས་པས༌[^2050]སྡུག་བསྔལ་དང་ཀུན་འབྱུང་ལ་རྗེས་སུ་ཤེས་པའི་རྣམ་པ་དག་དང་མཚུངས་པར་ལྡན་པ་བརྒྱད་དང་། འགོག་པ་དང་ལམ་ལ་ཆོས་ཤེས་པའི་རྣམ་པ་དག་དང་མཚུངས་པ༌[^2051]ལྡན་པ་བརྒྱད་དང་། འགོག་པ་ལ་རྗེས་སུ་ཤེས་པའི་རྣམ་པ་དག་དང་མཚུངས་པར་ལྡན་པ་བསམ་གཏན་དང་པོའི་འགོག་པ་ལ་དམིགས་པ་བཞི་ནས་དེ་བཞིན་དུ་སྲིད་པའི་རྩེ་མོའི་འགོག་པ་ལ་དམིགས་པའི་བར་དུ་བཞི་དང་། ལམ་ལ་རྗེས་སུ་ཤེས་པའི་རྣམ་པ་དག་དང་མཚུངས་པར་ལྡན་པ་བཞི་སྟེ། རྗེས་སུ་ཤེས་པའི་ཕྱོགས་དང་མཐུན་པ་ཟད་པར༌[^2052]ལ་དམིགས་པའི་ཕྱིར་རོ། །

[Block 2974]
དེ་དག་ནི་ཤེས་པའི་དམིགས་པ་དང་རྣམ་པའི་བྱེ་བྲག་གིས་ཐ་དད་པའི་ཕྱིར་རྡོ་རྗེ་ལྟ་བུ་ལྔ་བཅུ་རྩ་གཉིས་ཡིན་ནོ། །

[Block 2975]
མི་ལྕོགས་པ༌[^2053]མེད་པས་བསྡུས་པ་ཇི་ལྟ་བར་བསམ་གཏན་བཞི་པས་བསྡུས་པའི་བར་དག་ཀྱང་དེ་དང་འདྲའོ། །

[Block 2976]
ནམ་མཁའ་དང་རྣམ་ཤེས་མཐའ་ཡས་དང་ཅི་ཡང་མེད་པའི་སྐྱེ་མཆེད་ཀྱིས༌[^2054]བསྡུས་པ་རྣམས་ནི་གྲངས་བཞིན་དུ་ཉི་ཤུ་རྩ་བརྒྱད་དང་ཉི་ཤུ་རྩ་བཞི་དང་ཉི་ཤུ་ཡིན་ཏེ། དེ་དག་ནི༌[^2055]ཆོས་ཤེས་པ་དང་རྗེས་སུ་ཤེས་པས་ས༌[^2056]འོག་མའི་འགོག་པ་ལ་དམིགས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 2977]
ས་འོག་མིའི༌[^2057]གཉེན་པོ་ལ་དམིགས་པ་ནི་ཡོད་དེ།[^2058] དེ་ནི་ཕན་ཚུན་དུ་རྒྱུ་བའི་ཕྱིར་རོ། །

[Block 2978]
གང་དག་ལམ་ལ་རྗེས་སུ་ཤེས་པ་ཡང་ས་རེ་རེའི་གཉེན་པོ་ལ་དམིགས་པ་ཡིན་པར་འདོད་པ་དེ་དག་གི་ལྟར་ན་ཉི་ཤུ་རྩ་བརྒྱད་ལྷག་པར་བསྣན་ནས་མི་ལྕོགས་པ་མེད་པས་བསྡུས་པ་རྡོ་རྗེ་ལྟ་བུ་ནི་བརྒྱད་ཅུ་ཡིན་ཏེ། བསམ་གཏན་བཞི་པས་བསྡུས་པའི་བར་དུ་ཡང་དེ་དང་འདྲའོ། །

[Block 2979]
ནམ་མཁའ་མཐའ་ཡས་སྐྱེ་མཆེད་ལ་སོགས་པ་དག་ནི་གོ་རིམས་བཞིན་དུ་བཞི་བཅུ་དང་། སུམ་ཅུ་རྩ་གཉིས་དང་། ཉི་ཤུ་རྩ་བཞི་ཡིན་ནོ། །

[Block 2980]
ཡང་རིགས་དང་དབང་པོའི་བྱེ་བྲག་གིས་ནི་ཆེས་མང་བ་ཡིན་ནོ། །
--- END BLOCKS ---
