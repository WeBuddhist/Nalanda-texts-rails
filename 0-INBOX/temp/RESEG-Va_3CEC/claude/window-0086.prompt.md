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
[Block 3011]
གཙོ་བོར་གྱུར་པ་མ་ཡིན་པའི་ཚོགས་ཀྱི་དབང་དུ་བྱས་ནས། སེམས་ཞི་བ་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 3012]
ནང་དུ་སེམས་རྣམ་པར་རྟོག་པ་མི་མང་བ་ནི་སེམས་ཞི་བའོ། །

[Block 3013]
ཕྱི་རོལ་གྱི་ཡུལ་རྣམས་ལ་རྟོག་པར་མི་དགའ་བ་ནི་རབ་ཏུ་ཞི་བའོ། །

[Block 3014]
ཕྱི་ནང་གཉིས་ལ་རྟོག་པ་མེད་པའམ། གཉིད་དང་རྨུགས་པ་མེད་པ་ནི་ཉེ་བར་ཞི་བའོ། །

[Block 3015]
ནང་དུ་སེམས་རྣམ་པར་རྟོག་པ་མི་མང་བ་སྟེ་ཞི་བས་ན། རྣམ་པར་མི་གཡེང་བའོ།[^2637] །ཕྱི་རོལ་དུ་རྟོག་པ༌[^2638]མེད་དེ་རབ་ཏུ་ཞི་བས་ན། དབང་པོ་ལེགས་པར་བསྡོམས༌[^2639]པའོ། །

[Block 3016]
ཕྱི་ནང་གཉི་གར་རྟོག་པ་མེད་པས་ན༌[^2640]མི་རྒོད་པ་དང་མི་འཕྱར་བའོ། །

[Block 3017]
རྒྱལ་པོ་དང་རྐུན་པོ་ལ་སོགས་པའི་གཏམ་མང་པོ་ལ་མི་འཇུག་པས་ན་མུ་ཅོར༌[^2641]མི་སྨྲ་བའོ། །

[Block 3018]
ཉོན་མོངས་པའི་དབང་དུ་མི་འགྱུར་བས་ན་ཡབ་ཡབ་པོ་མ་ཡིན་པའོ། །

[Block 3019]
ཏིང་ངེ་འཛིན་གྱི༌[^2642]མི་མཐུན་པའི་ཕྱོགས་ཀྱིས་བསྐྱོད་པར༌[^2643]མི་ནུས་པས་ན་མི་འགྱུར་བའོ། །

[Block 3020]
གཞན་གྱི་རྗེས་སུ་འཇུག་ཅིང་ཞེ་སྡང་བའི་སེམས་མེད་པས་ན་ཞི་དེས་སོ། །

[Block 3021]
མིག་ལ་སོགས་པ་དབང་པོའི་ཡུལ་ལ་མི་འཇུག་པར་སྡོམ་པས་ན་བསྲུངས་པའོ། །

[Block 3022]
ཉོན་མོངས་པ་སྤོང་བའི་ལམ་ལ་ཞུགས་པས་ན་ཅང་ཤེས་པའོ། །

[Block 3023]
གཉིད་དང་རྨུགས་པ་མེད་པས་ན་ལས་སུ་རུང་བའོ། །

[Block 3024]
དམིགས་པའི་ཡུལ་ལ༌[^2644]སེམས་གཞན་དུ་མི་འགྲོ་བས་ན་རྩེ་གཅིག་པའོ། །

[Block 3025]
གཅིག་པུར་གནས་པར་མོས་པས༌[^2645]ན་མོས་པའོ། །

[Block 3026]
འགྲོ་བ་མང་པོ་དང་ལྷན་ཅིག་མི་གནས་པས་ན་འདུ་འཛི་ཡོངས་སུ་སྤོང་བའོ། །

[Block 3027]
སེམས་རྩེ་གཅིག་པ་ལ་མོས་པའི་ཕྱིར་དབེན་པར་དགའ་བའོ། །

[Block 3028]
གཅིག་པུ་དགའ་ཞིང་འདུ་འཛི་སྤོང་བས་ན་ལུས་དབེན་པའོ། །

[Block 3029]
ཉོན་མོངས་པས༌[^2646]སེམས་དཀྲུགས་པ༌[^2647]མེད་པས་ན་སེམས་མ་བསླད་པའོ། །

[Block 3030]
རི་དང་བྲག་ཕུག་ལ་སོགས་པར་གནས་པར་སེམས་མངོན་པར་འདུ་བྱེད་པས་ན་དགོན་པར་མངོན་དུ་ཕྱོགས་པར་ཡིད་ལ་བྱེད་པའོ། །

[Block 3031]
ཆོས་གོས་དང་ལྷུང་བཟེད་ལ་སོགས་པ་ཉི་ཚེ་ཙམ་འཆང་བས་ན་འདོད་པ་ཉུང་བའོ། །

[Block 3032]
དེ་ལས་ལྷག་པར་མི་འདོད་པས་ན་འདོད་པ་མེད་པའོ། །

[Block 3033]
ངན་པས་ཆོག་པར་འཛིན་པས་ན་འདོད་ཆེན་མེད་པའོ། །

[Block 3034]
བཟང་པོ་མི་ཚོལ་བས་ན་ཆོག་ཤེས་པའོ། །

[Block 3035]
ལོག་པའི་འཚོ་བ་མེད་པས་ན་འཚོ་བ་ཡོངས་སུ་དག་པའོ། །

[Block 3036]
ཚུལ་ཁྲིམས་རྣམ་པར་དག་པས་ན་ཆོ་ག་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 3037]
སྤྱོད་ལམ་ཐམས་ཅད་དུ་ཉོན་མོངས་པ་མི་སྐྱ་ཞིང་སྤྱོད་ལམ་མཛེས་པས་སྤྱོད་ལམ་བསྲུངས་པའོ། །

[Block 3038]
དུས་དང་ཚོད་དང་། དུས་མིན་ཤེས་པ་ནི་སྔར་བཤད་པ་བཞིན་དུ་ལྟའོ།[^2648] །ཁ་ཟས་མང་དུ་ཡང་མི་ཟ་ཉུང་ངུ་ཡང་མི་ཟ་སྟེ་རན་པར་བྱེད་པས་ན་རན་དྲོད་ཤེས་པའོ། །

[Block 3039]
ཅུང་ཟད་ཙམ་གྱིས་ཆོག་ཤེས་པར་འཛིན་པས་ན༌[^2649]དགང་སླ་བ་དང་། གསོ་སླ་བའོ། །

[Block 3040]
སོ་སོར་བརྟགས་པའི་སྟོབས་ཀྱིས་མི་མཐོ་མི་དམའ་ཞེས་བྱ་བ་ནི། ཏིང་ངེ་འཛིན་དང་ལྡན་པའི༌[^2650]ཤེས་རབ་ཀྱི་མཐུས། ཆོས་རྣམས་ཇི་ཡང་མ་ཡིན་པར་རྟོགས་པའི་ཕྱིར་བསྟོད་པ་ལ་སོགས་པས་མཐོ༌[^2651]བར་ཡང་མི་འགྱུར། སྨད་པ་ལ་སོགས་པས་དམས་པར༌[^2652]མི་འགྱུར་བའོ། །

[Block 3041]
ངན་དུ་བརྗོད་པ་ནི་སྔོན་འདས་པའི་དུས་སུའོ། །

[Block 3042]
ངན་དུ་སྨྲས་པ་ནི་ད་ལྟར་གྱི་དུས་ཉིད་ནའོ། །

[Block 3043 [HEADING]]
###### གཙོ་བོའི་ཚོགས། ^8-8-1-1-2-0

[Block 3044]
གཙོ་བོའི་ཚོགས་བསྟན་པའི་ཕྱིར། རྣལ་འབྱོར་ལ་མངོན༌[^2653]དུ་ཕྱོགས་པའི་སེམས་བསྐྱེད་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 3045]
ཞི་གནས་དང་ལྷག་མཐོང་བསྒོམ་པའི་སེམས་བསྐྱེད་པ་ནི་རྣལ་འབྱོར་ལ་མངོན་དུ་ཕྱོགས༌[^2654]པའི་སེམས་བསྐྱེད་པའོ། །

[Block 3046]
ཡང་དག་འཇོག་ལ་མངོན་པར་དགའ་ཞེས་བྱ་བ་ནི་དེ་ཉིད་ཀྱི་ཏིང་ངེ་འཛིན་བསྒོམ་པ༌[^2655]ལ་མོས་པའོ། །

[Block 3047]
བསམ་གཏན་གྱི་ཡན་ལག་ཡིད་ལ་བྱེད་པ་དང་ཞེས་བྱ་བ་ནི་བསམ་གཏན་ལ་སོགས་པའི་ཡན་ལག་རྟོག་དཔྱོད་དང་བཅས་པ་དང་། རྟོག་དཔྱོད་མེད་པ་ལ་སོགས་པ་བསྒོམ་པ་སྔ་ནས་ཡིད་ལ་བྱེད་ཅིང་རྩོམ་པའོ། །

[Block 3048]
བྱམས་པ་བསྐྱེད་པ༌[^2656]དང་། སྙིང་རྗེ་མངོན་པར་བསྒྲུབ་པ༌[^2657]ཞེས་བྱ་བས་ནི་ཏིང་ངེ་འཛིན་གྱི་རྩ་བར་གྱུར་པ་ཚད་མེད་པ་གཉིས་སྔ་ནས་སྐྱེད་ཅིང་སྒྲུབ་པར༌[^2658]བྱེད་པའོ། །

[Block 3049]
དགའ་བ་ལ་གཞོག་ཅེས་བྱ་བ་ལ་སོགས་པ་ནི་ཏིང་ངེ་འཛིན་མི་འཁྲུག་པར་བྱེད་པ་དགའ་བ་ཚད་མེད་པ་ལ་སེམས་གཞོག་ཅིང་བཏང་སྙོམས་ཚད་མེད་པ་བསྒོམ༌[^2659]ལ། དེ་གཉིས་ཀྱི་སེམས་དང་རྟག་པར་ལྡན་པར་བྱེད་པའོ། །

[Block 3050 [HEADING]]
##### ཞི་གནས་ཉིད། ^8-8-1-2-0
--- END BLOCKS ---
