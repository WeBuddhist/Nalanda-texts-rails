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
[Block 4201]
དེ་དག་གི་ཡང་སྐྱེ་བ་རྣམས་ནི་བཤད་ཟིན་ཏོ། །

[Block 4202 [HEADING]]
##### སྙོམས་པར་འཇུག་པའི་གཟུགས་མེད་པ། ^5-1-2-2-0

[Block 4203]
སྙོམས་པར་འཇུག་པའི་གཟུགས་མེད་པ་རྣམས་ནི་བྱེ་བྲག་མེད་པར་དགེ་བའི་སེམས་རྩེ་གཅིག་པའི་རང་བཞིན་ཡིན་ནོ་ཞེས་བྱ་བའི་རྣམ་པ་དེས་བཤད་ཟིན་ཏོ། །

[Block 4204]
འཁོར་དང་བཅས་ན་ནི། ཕུང་པོ་བཞི་རྗེས་སུ་འབྲང་བའི་གཟུགས་མེད་པའི་ཕྱིར་རོ། །

[Block 4205]
འོག་མའི་ས༌[^3021]དབེན་ལས་སྐྱེས་པ། །བསམ་གཏན་བཞི་པ་ལས་དབེན་པ་ལས་སྐྱེས་པ་ནི་ནམ་མཁའ་མཐའ་ཡས༌[^3022]སྐྱེ་མཆེད་ཡིན་ནོ། །

[Block 4206]
དེ་ལས་དབེན་པ་ལས་སྐྱེས་པ་ནི་རྣམ་ཤེས་མཐའ་ཡས་སྐྱེ་མཆེད་ཡིན་ནོ། །

[Block 4207]
དེ་ལས་དབེན་པ་ལས་སྐྱེས་པ་ནི་ཅི་ཡང་མེད་པའི་སྐྱེ་མཆེད་ཡིན་ནོ། །

[Block 4208]
[^3023]དེ་ལས་དབེན་པ་ལས་སྐྱེས་པ་ནི་འདུ་ཤེས་མེད་འདུ་ཤེས་མེད་མིན་གྱི་སྐྱེ་མཆེད་ཡིན་ཏེ། དེ་ལྟར་ན་གཟུགས་མེད་པ་བཞི༌[^3024]ཡིན་ནོ། །

[Block 4209]
དབེན་པ་ཞེས་བྱ་བ་འདི་ཅི་ཞེ་ན། ལམ་གང་གིས་ནི༌[^3025]འོག་མ་ལས་རྣམ་པར་འབྱེད་པ་སྟེ། འདོད་ཆགས་དང་བྲལ་བར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 4210]
གཟུགས་མེད་པ་དེ་དག་ཀྱང་།

[Block 4211 [VERSE]]
ཉེར་བསྡོགས་གསུམ་དང་བཅས་པར་ནི། །
གཟུགས་ཀྱི་འདུ་ཤེས་བཤིག་ཅེས་བྱ། །

[Block 4212]
ནམ་མཁའ་མཐའ་ཡས་སྐྱེ་མཆེད་ཀྱི་ཉེར་བསྡོགས་ནི་བསམ་གཏན་བཞི་པ་ལ་དམིགས་པའི་ཕྱིར་གཟུགས་ཀྱི་འདུ་ཤེས་བཤིག་ཅེས་བྱ་བའི་མིང་མི་འཐོབ་བོ། །

[Block 4213]
དེ་ལ་ནི་གཟུགས་ཀྱི་འདུ་ཤེས་བཤིག་པ་མ་ཡིན་ཏེ། མ་བྲལ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 4214 [HEADING]]
#### གཟུགས་མེད་པ་དག་ན་གཟུགས་མེད་པ། ^5-1-3-0

[Block 4215]
ཕུང་པོ་བཞི་ཞེས༌[^3026]གང་བཤད་པ་རེ་ཞིག་གཟུགས་མེད་པ་དག་ན་གཟུགས་མེད་དོ་ཞེས་བྱ་བ་འདི་ནི་བསྒྲུབ་པར་བྱ་བ་ཡིན་ནོ། །

[Block 4216]
གལ་ཏེ་ཡོད་ན་ཇི་ལྟར་ན་གཟུགས་མེད་པ་རྣམས༌[^3027]བརྗོད་པར་འགྱུར། [^3028]གཟུགས་ཅུང་ཟད་ཅིག་ཡོད་པའི་ཕྱིར་ཏེ། ཅུང་ཟད་ཟེར་བ་བཞིན་ནོ། །

[Block 4217]
རེ་ཞིག་དེ་ནི་གཟུགས་ཇི་ལྟ་བུ་ཞིག་ཡོད་པར་འདོད། གལ་ཏེ་ལུས་དང་ངག་གི་སྡོམ་པ་ཙམ༌[^3029]ཞིག་གོ་ཞེ་ན། དེ་དག་མེད་ན་ཇི་ལྟར་དེ་དག་གི་སྡོམ་པར༌[^3030]འགྱུར། འབྱུང་བ་མེད་པར་ནི་འབྱུང་བ་ལས་གྱུར་པ་མི་རུང་ངོ་། །གལ་ཏེ་ཟག་པ་མེད་པའི་སྡོམ་པ་བཞིན་ནོ་ཞེ་ན། མ་ཡིན་ཏེ་ཟག་པ་དང་བཅས་པའི་འབྱུང་བ་ཡོད་པའི་ཕྱིར་རོ། །

[Block 4218]
སྙོམས་པར་འཇུག་པ༌[^3031]ལ་ཡང་དེ་དགག་པར་བཤད་དོ། །

[Block 4219]
འོན་ཏེ་ལུས་ཀྱང་ཡོད་ལ་དབང་པོ་གཟུགས་ཅན་རྣམས་ཀྱང་ཡོད་དོ་ཞེ་ན་ནི། ཇི་ལྟར་ན་དེ་དག་གཟུགས་ཅུང་ཟད་ཡོད་པར་འདོད། གལ་ཏེ་བོང་ཚོད་ཆུང་བའི་ཕྱིར་རོ་ཞེ་ན་ནི་ཆུང་ངུའི༌[^3032]སྐྱེ་བོ་གཟུགས་བལྟར་མི་སྣང་བ་དག་ལ་ཡང་ཐལ་བར་འགྱུར་རོ། །

[Block 4220]
གལ་ཏེ་དང་བའི་ཕྱིར་རོ་ཞེ་ན་ནི། སྲིད་པ་བར་མ་དག༌[^3033]དང་། གཟུགས་ན་སྤྱོད་པ་རྣམས༌[^3034]ལ་ཡང་ཐལ་བར་འགྱུར་རོ། །

[Block 4221]
གལ་ཏེ་གང་ལས་ཆེས་དང་བ་མེད་པ་ཡིན་ནོ་ཞེ་ན་ནི། སྲིད་པའི་རྩེ་མོ་ཁོ་ན་གཟུགས་མེད་པ་ཡིན་པར་འགྱུར་ཏེ། སྙོམས་པར་འཇུག་པ་བཞིན་དུ༌[^3035]སྐྱེ་བ་ཁྱད་པར་དུ་འཕགས་པའི་ཕྱིར་རོ། །

[Block 4222]
བསམ་གཏན་དུ་སྐྱེ་བའི་གཟུགས་ཀྱང་ས་འོག་མའི་དབང་པོས་མི་ཟིན་པའི་ཕྱིར་དེ་དང་ཡང་ཁྱད་པར་ཅི་ཞིག་ཡོད།[^3036] གལ་ཏེ་གཉིས་ཀྱི་མིང་ནི་དོན་དང་མཐུན་པ་ཡིན་གྱི་གཟུགས་མེད་པའི་ཁམས་ཀྱི་ནི་མ་ཡིན་ནོ་ཞེ་ན། དེ་ལ་རིགས་པ་ཅི་ཞིག་ཡོད། གལ་ཏེ་ཚེ་དང་དྲོད་གཉིས་འདྲེས་པར་གསུངས་པའི༌[^3037]ཕྱིར་དང་། འདམ་བུའི་ཤོག་གཉིས༌[^3038]བཞིན་དུ་མིང་དང་གཟུགས་དག་ཕན་ཚུན་བརྟེན་ཏོ་ཞེས་གསུངས་པའི་ཕྱིར་དང་། །རྣམ་པར་ཤེས་པའི་རྐྱེན་ཀྱིས་མིང་དང་གཟུགས་ཞེས་གསུངས་པའི་ཕྱིར་དང་། གཟུགས་ནས་འདུ་བྱེད་རྣམས་ཀྱི་བར་ལས་གཞན་དུ་རྣམ་པར་ཤེས་པ་འོང་བའམ༌[^3039]འགྲོ་བ༌[^3040]བཀག་པའི་ཕྱིར་གཟུགས༌[^3041]མེད་པ་དག་ན་གཟུགས་ཡོད་པ་ཉིད་དུ་གྲུབ་བོ་ཞེ་ན། མ་ཡིན་ཏེ། དཔྱད་པར་བྱ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4223]
རེ་ཞིག་ཚེ་དང་དྲོད་གཉིས་འདྲེས་པ་ཉིད་དུ་གང་གསུངས་པ་འདི་ཅི་འདོད་པ་དང་གཟུགས་ན་སྤྱོད་པའི་ཚེ་ལས་དགོངས་ཏེ་གསུངས་སམ། འོན་ཏེ་ཐམས་ཅད་ལས་ཞེས་བྱ་བ་དང་། གང་ཡང་མིང་དང་གཟུགས་དག་ཕན་ཚུན་བརྟེན་པ་ཉིད་དུ་གསུངས་པ་འདི་ཅི་འདོད་པ་དང་གཟུགས་ན་སྤྱོད་པ་ལས་དགོངས་ཏེ་གསུངས་སམ། འོན་ཏེ་ཐམས་ཅད་ལས་ཞེས་བྱ་བ་དང་། གང་ཡང་རྣམ་པར་ཤེས་པའི་རྐྱེན་གྱིས་མིང་དང་གཟུགས་ཞེས་གསུངས་པ་འདི་ཅི་རྣམ་པར་ཤེས་པ་ཐམས་ཅད་མིང་དང་གཟུགས་ཀྱི་རྐྱེན་དུ་གསུངས་སམ། འོན་ཏེ་མིང་དང་གཟུགས་ཐམས་ཅད་རྣམ་པར་ཤེས་པའི་རྐྱེན་དུ་གསུངས་ཞེས་བྱ་བ་དང་། གང་ཡང་གཟུགས་ལ་སོགས་པ་ལས་གཞན་དུ་རྣམ་པར་ཤེས་པ་འོང་བ་དང་འགྲོ་བ་བཀག་པར༌[^3042]གསུངས་པ་འདི་ཅི་དེ་དག་ཐམས་ཅད་མེད་ན་དེ་བཀག་གམ། འོན་ཏེ་འགའ་ཞིག་ཀྱང་ཞེས་བྱ་བ་འདི་དཔྱད་པར་བྱ་དགོས་སོ། །

[Block 4224]
གལ་ཏེ་བྱེ་བྲག་མེད་པར་གསུངས་པའི༌[^3043]ཕྱིར་དཔྱད་པར་མི་བྱའོ་ཞེ་ན་ནི་ཧ་ཅང་ཐལ་བར་འགྱུར༌[^3044]ཏེ། ཚེ་མེད་པར་ཕྱིའི་དྲོ་བ༌[^3045]ཡང་ཡོད་པར་མི་འགྱུར་ལ། ཕྱིའི་གཟུགས་ཀྱང་རྣམ་པར་ཤེས་པ་ལ་བརྟེན་པ་ཉིད་དུ་འགྱུར་ཏེ། ཁྱད་པར་མེད་པར༌[^3046]འབྱུང་བའི་ཕྱིར་རོ། །

[Block 4225]
རྣམ་པར་ཤེས་པ་གནས༌[^3047]བཞིན་དུ་ཟས་བཞི་གསུངས་པའི་ཕྱིར་གཟུགས་དང་གཟུགས་མེད་པའི་ཁམས་དག་ན་ཡང་ཁམ་དུ་བྱེད་པའི་ཟས་ཡོད་པར་ཐལ་བར་ཡང་འགྱུར་རོ། །

[Block 4226]
གལ་ཏེ་ཁམ་དུ་བྱེད་པའི་ཟས་ཟ་བའི་ལྷ་རྣམས་ལས་འདས་ཏེ་ཞེས་གསུངས་པའི་ཕྱིར་དང་། དགའ་བའི་ཟས་ཞེས་གསུངས་པའི་ཕྱིར་ཐལ་བར་མི་འགྱུར་རོ་ཞེ་ན་ནི་གཟུགས་མེད་པ་དག་ན་ཡང་གཟུགས་ཡོད་པར་ཐལ་བར་མི་འགྱུར་ཏེ། གཟུགས་མེད་པ་རྣམས་ནི་གཟུགས་རྣམས་ལས་ངེས་པར་འབྱུང་བ་ཡིན་ནོ་ཞེས་བྱ་བ་དང་། གཟུགས་མེད་པའི་རྣམ་པར་ཐར་པ༌[^3048]ཞི་བ་གང་དག་གཟུགས་རྣམས་ལས་འདས་ནས་ཞེས་བྱ་བ་དང་། གཟུགས་ཅན་མ་ཡིན་པའི་སེམས་ཅན་དག་ཡོད་ཅེས་བྱ་བ་དང་། རྣམ་པ་ཐམས་ཅད་དུ་གཟུགས་ཀྱི་འདུ་ཤེས་རྣམས༌[^3049]ལས་ཡང་དག་པར་འདས་ནས་ཞེས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 4227]
གཟུགས་ཤིག་ཡོད་ན་ནི་རང་གི་གཟུགས་གདོན་མི་ཟ་བར་འདུ་ཤེས་པར་བྱེད་པར་འགྱུར་རོ། །

[Block 4228]
གལ་ཏེ་ས་འོག་མ་པའི་གཟུགས་རགས་པ་ལས་དགོངས་ཏེ་གསུངས་པ་ཡིན་ནོ་ཞེ་ན་ནི། ཁམ་གྱི༌[^3050]ཟས་ལ་ཡང་མཚུངས་སོ། །

[Block 4229]
བསམ་གཏན་རྣམས་ཀྱང་ས་འོག་མ་པ༌[^3051]ལས་ངེས་པར་འབྱུང་བ་ཡིན་པའི་ཕྱིར་གཟུགས་མེད་པར་ཐལ་བར་འགྱུར་རོ།[^3052] །ས་འོག་མ་པའི་ཚོར་བ་ལ་སོགས་པ་ལས་ངེས་པར་འབྱུང་བའི་ཕྱིར་ཚོར་བ་ལ་སོགས་པ་ལས་ཀྱང་ངེས་པར་འབྱུང་བ་ཡིན་པར་ཅིའི་ཕྱིར་མ་བཤད་དེ། གཟུགས་ཀྱི་རྣམ་པ་ཟད་པར་ལས་འདས་ལ་ཚོར་བ་ལ་སོགས་པའི་རྣམ་པ་ལས་ནི་མ་ཡིན་པས་དེའི་ཕྱིར་གཟུགས་རྣམས་ལས་ངེས་པར་འབྱུང་བ་ཞེས་གསུངས་སོ། །

[Block 4230]
སྲིད་པས་སྲིད་པ་ལས་ངེས་པར་མི་འབྱུང་བར་གསུངས་པ་ནི་དེ་ཉིད་ཀྱིས་དེ་ལས་ངེས་པར་མི་འབྱུང་བའི་ཕྱིར་དང་། ཐམས་ཅད་དང་གཏན་དུ་ངེས་པར་འབྱུང་བ༌[^3053]མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4231]
བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་བསམ་གཏན་དག་ལ་ནི་གང་དེ་ན་གཟུགས་ཀྱི་རྣམ་པ༌[^3054]ཡོད་པའང་རུང་རྣམ་པར་ཤེས་པའི་རྣམ་པའི་བར་ཡོད་པའང་རུང་ཞེས་གསུངས་ལ། གཟུགས་མེད་པ་དག་ལ་ནི་གང་དེ་ན་ཚོར་བའི་རྣམ་པ་ཡོད་པའང་རུང་རྣམ་པར་ཤེས་པའི་རྣམ་པའི་བར་ཡོད་པའང་རུང་ཞེས་གསུངས་ཏེ། དེ་དག་ན་གཟུགས་ཀྱི་རྣམ་པ་ཞིག་ཡོད་ན་ཅིའི་ཕྱིར་གཟུགས་ཀྱི་རྣམ་པ་ཡོད་པའང་རུང་ཞེས་གསུངས་པར་མི་འགྱུར་ཏེ་དེ༌[^3055]ལྟ་བས་ན་གཟུགས་མེད་པ་ན་གཟུགས་མེད་དོ། །

[Block 4232]
དེ་ནི་ཇི་ལྟར་ན་དེ་ནས་ཤི་འཕོས་པ་རྣམས་ཀྱི་གཟུགས་བསྐལ་པ་མི་ཉུང་བ་ཞིག་ཏུ་གཟུགས་རྒྱུན་ཆད་པ་ལས་ཡང་སྐྱེ་བར་འགྱུར་ཞེ་ན། གཟུགས་ནི་སེམས་ལས་སྐྱེ་བར་འགྱུར། །གཟུགས་ནི་དེའི་རྣམ་པར་སྨིན་པའི་རྒྱུས་ཡོངས་སུ་བསྒོས་པའི༌[^3056]སེམས་འཇུག་པ་རྙེད་པ་ལས་སྐྱེ་བར་འགྱུར་རོ། །ཇི་ལྟར་ན་སེམས་གཟུགས་ལ་མ་བརྟེན་པར་གནས་ཤེ་ན། ཅིའི་ཕྱིར་གནས་པར་མི་འགྱུར། འདི་ན་དེ་ལྟ་བུ་མ་མཐོང་བའི་ཕྱིར་རོ། །

[Block 4233]
ཁམ་གྱི་ཟས་མེད་པར་ཡང་གཟུགས་ཀྱི་ཁམས་ན་གནས་པར་མི་འགྱུར་རོ། །ཅིའི་ཕྱིར་ཞེ་ན། འདི་ན་དེ་ལྟ་བུ་མ་མཐོང་བའི་ཕྱིར་རོ། །

[Block 4234]
ཇི་ལྟར་གནས་པ་ནི་སྔར་བཤད་ཟིན་ཏོ། །

[Block 4235]
འདི་ནི་རྫོགས་སོ།། །།

[Block 4236 [HEADING]]
#### ནམ་མཁའ་མཐའ་ཡས་སྐྱེ་མཆེད་ལ་སོགས་པའི་མིང། ^5-1-4-0

[Block 4237]
འདི་བརྗོད་པར་བྱ་སྟེ། ཅི་ནམ་མཁའ་མཐའ་ཡས་སྐྱེ་མཆེད་ལ་སོགས་པ་དེ་དག་ནམ་མཁའ་ལ་སོགས་པ་ཁོ་ན་ལ་དམིགས་པ་ཡིན་པས་དེའི་ཕྱིར་དེ་སྐད་ཅེས་བྱའམ་ཞེ་ན། མ་ཡིན་ནོ། །

[Block 4238]
[^3057]འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན། རེ་ཞིག་གསུམ་མོ། །

[Block 4239 [VERSE]]
[^3058]རྣམ་ཤེས་མཐའ་ཡས་མཁའ་མཐའ་ཡས། །
ཅི་ཡང་མེད་ཅེས་བྱ་དེ་ལྟར། །

[Block 4240]
སྦྱོར་ཕྱིར༌[^3059]གྲངས་བཞིན་དུ་ནམ་མཁའ་མཐའ་ཡས་སོ། །
--- END BLOCKS ---
