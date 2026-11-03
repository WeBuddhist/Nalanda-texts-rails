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
[Block 4096]
འདུན་པ་དང་ཡོངས་སུ་དག་པ་གཉིས་ལྷན་ཅིག་ཏུ་འདུན་པ་དང་དགག་དབྱེ་དག་ལ་ཡང་བརྗོད་དོ། །

[Block 4097]
བརྗོད་པ་ཡང་རིག་པར་བགྱིད་དོ་ཞེས་གསུངས་པ་གང་ཡིན་པ་དེ་འདིས་བསྡུས་པ་ཡིན་ནོ། །

[Block 4098]
བརྗོད་པར་བྱ་བ་རྩོམ་པ་འདྲ་བ་རྣམས་ཞེས་སྤྱིར་སྨོས་པ་གང་ཡིན་པ་དེ་ལ་རིག་པ༌[^2842]ནི་འདུན་པ་དང་ཡོངས་སུ་དག་པ་དང་། འདུན་པ་དང༌[^2843]དགག་དབྱེ་དག་ཀྱང་བརྗོད་པ་ཡང༌[^2844]རིག་པར་བགྱིད་དོ་ཞེས་གསུངས་པ་གང་ཡིན་པ་དེ་རྣམས་ཀྱིས་ནི་ཡུལ་གྱི་བྱེ་བྲག་ལ་བཅས་པ་ཞེས་བྱ་བ་དེ་ལྟ་བུར་གཞན་རྣམས་ལ་ཡང་འདིར་ཁོངས་སུ་བསྡུ་བའི་ཕྱིར་འདི་བསྟན་པ་ཡིན་ནོ། །

[Block 4099]
གཅིག་གིས་དུ་མའི་དེ་དག་ལེན་པ་ལ་ཡང་མེད་དོ་ཞེས་བྱ་བ་ནི། མི་རུང་བ་ཞེས་བྱ་བར་སྦྱར་ཏེ། དགེ་སློང་གཅིག་གིས་དགེ་སློང་དུ་མའི་རྒྱུད་དུ་གཏོགས་པའི་འདུན་པ་དང་། དགག་དབྱེ་ལ་སོགས་པ་ལེན་པ༌[^2845]ཡང་མི་རུང་བ་མེད་དོ། །

[Block 4100]
འདི་ལ་བརྗོད་ནུས་པའི་ཚིག་གིས་གཟུང་ངོ་ཞེས་བྱ་བ་ལ། འདི་ལ་ཞེས་བྱ་བ་ནི་དགེ་སློང་དུ་མའི་རྒྱུད་དུ་གཏོགས་པའི་འདུན་པ་ལ་སོགས་པ༌[^2846]ལེན་པ་འདི་ལ་གྲངས་ཀྱི་བྱེ་བྲག་ཡོངས་སུ་ཆད་པ་མེད་དོ། །

[Block 4101]
འོན་ཀྱང་བརྗོད་ནུས་པ་ལས་ཏེ༌[^2847]ཇི་སྙེད་བརྗོད་ནུས་པ་དེ་སྙེད་པ་རྣམས་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4102]
མི་ནུས་ན་དེ་དག་འབུལ་བ་གང་ཡང་རུང་བས་འགྲུབ་བོ་ཞེས་བྱ་བ་ནི། འདུན་པ་ལ་སོགས་པ་དེ་རྣམས་འབུལ་བ་གང་ཡིན་པ་དེ་རྣམས་ལ་གང་ཡང་རུང་བས་མི་ནུས་པར་གྱུར་ན་འགྲུབ་པའོ། །

[Block 4103]
ལུས་ཀྱིས༌[^2848]ཀྱང་ངོ་། །ཇི་ལྟར་ཡང་མི་ནུས་ན་ཡང་ན་དགེ་འདུན་དེར་འགྲོ་བར་བྱའོ། །

[Block 4104]
ཡང་ན་དེ་ཁྲིས་བླང་བར་བྱའོ་ཞེས་བྱ་བ་ལ་ཇི་ལྟར་ཡང་ཞེས་བྱ་བ་ལ་ནི་ལུས་ཀྱིས་ཀྱང་མི་ནུས་པར་འགྱུར་ནའོ། །

[Block 4105]
ཡང་ན་དེ་ཞེས་བྱ་བ་ནི་འདུན་པ་ལ༌[^2849]སོགས་པ་འབུལ་བའི་ནད་པ་ལའོ། །

[Block 4106]
དེ་བླངས་པས་རྒྱུག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི། འདུན་པ་ལ་སོགས་པ་རྣམས་སོ། །

[Block 4107]
མགྱོགས་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། ལ་ལ་དག་ནི་མགྱོགས་པ་དང་རྒྱུག་པ་དག་གིས༌[^2850]གནས་ལ་མགྱོགས་པ་དང་། རྒྱུག་པར་མི་བྱའོ༌[^2851]ཞེས་ཟེར་རོ། །

[Block 4108]
དོན་དེ་ཉིད་འདིར་མཐོང་བ་ཡིན་ནོ། །

[Block 4109]
རྩེ་བའི༌[^2852]ངོ་བོས་ཅུང་ཟད་དལ་བའི་འགྲོ་བས་ཚིག་དང་བཅས་པས་རྒྱུག་པ་མཐོང་བའོ། །

[Block 4110]
ཚིག་དང་བཅས་པའི་མགྱོགས་པའང་མཐོང་བ་ཡིན་ནོ། །

[Block 4111]
རྒྱུག་པ་ནི་དེ་ཉིད་སྟེང་གི་ཆ་ལ་བསྙེན་ནས་མཆོང་བ་ལ་སོགས་པའི་ངོ་བོའོ། །

[Block 4112]
མཆོང་བར་མི་བྱའོ། །

[Block 4113]
ཕྱི་རོལ་ལ་མཆོང་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་འོབས་ལའོ། །

[Block 4114]
བང་རིམ་ལ་མི་བྱའོ་ཞེས་བྱ་བ་ནི་མཆོང་བ་སྟེ། ཕྱི་རོལ་གྱི་ཁྱམས་ཀྱི༌[^2853]བང་རིམ་ལའོ། །

[Block 4115]
ནམ་མཁའ་ལ་འདུག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི། ནམ་མཁའ་ལ་འཇུག༌[^2854]པའམ། འགྲོ་བར་མི་བྱའོ། །

[Block 4116]
ཕྱི་རོལ་དུ་མི་བྱའོ་ཞེས་བྱ་བ་ནི་མཚམས་ནས་མཚམས་ཀྱི་ཕྱི་རོལ་དུ་འགྲོ་བར་མི་བྱའོ། །

[Block 4117]
སྐས་ཀྱི་རིམ་པ་གཞན་བཞག་ནས་གཞན་དུ་གོམ་པ་དོར་བར་མི་བྱའོ། །

[Block 4118]
ཐེམ་སྐས་ཀྱི་ཐེམ་པར་མི་བྱའོ། །

[Block 4119]
ཆུ་ལྐོག་མ་ནུབ་ཙམ་ལ་འབོག་པར་མི་བྱའོ། །

[Block 4120]
གཉིད་ལོག་པ་དང་སྙོམས་པར་འཇུག་པར་མི་བྱའོ། །

[Block 4121]
དེ་གཉིས་ནི་མ་བཀླས་པ་ཉིད་ཀྱིས་ཀྱང་སྨད་པར་བྱ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། དེ་གཉིས་ཞེས་བྱ་བ་ནི་འདུན་པ་ལ་སོགས་པ་གཟུང་བ༌[^2855]གཉིད་ལོག་པ་དང་། སྙོམས་པར་འཇུག་པ་དག་ལའོ། །

[Block 4122]
མ་བཀླས་པ༌[^2856]ཉིད་ཅེས་བྱ་བ་ནི། ཐེ་ཚོམ་ཟ་བ་ཉིད་དང་། མ་ངེས་པ་ཉིད་དང་། མ་མོས་པ་ཉིད་དང་བསྟན་པ་ལ་མ་གུས་པ་ཉིད་དོ། །

[Block 4123]
དེས་ན་གཉིད་ལོག་པ་དང་། སྙོམས་པར་ཞུགས་པ་འདི་དག་ལ་སྨད་པར་བྱ་བ་ཉིད་དོ། །

[Block 4124]
ལྟུང་བ་འབྱིན་པ༌[^2857]པོ་ཉིད་ཀྱིས་ངོ་ཚ་བ་མེད་པ་འབའ་ཞིག་མ་ཟད་ཀྱི་མཚམས་ཀྱི་ཕྱི་རོལ་དུ་འགྲོ་བ་ལ་སྐྱོན་དང་བཅས་པ་ཉིད་ཀྱི་རྗེས་སུ་བསྒྲུབ་པ་ལ་གཏོགས་པའི་ལོ་རྒྱུས་ལ་སོ་སོར་ནུབ་པ་ཉིད་མ་ཡིན་གྱི། འདི་དག་ལ་ནི་འདི་སོ་སོར་མི་གནང་བར་འགྱུར་བ་དེ་བས་ན་འདི་དག་ཁོ་ན་ལས་མ་བཀླས་པ་ཉིད་ཀྱིས་ཀྱང་སྨད་པར་བྱ་བ་ཉིད་ཡིན་ནོ། །

[Block 4125]
དགེ་སློང་ལ་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་ནི། འདུན་པ་ལ་སོགས་པ་ལེན་པར་བྱེད་པ་དེས་གང་གི་ཚེ་དགེ་འདུན་གྱི་གནས་བརྟན་གྱིས་བརྗོད་པར་བྱ་སྟེ། འདིར་གཞུང་ནི། དེས་དྲུང་ན་འདུག་པའི་དགེ་སློང་ལ་ཚེ་དང་ལྡན་པ་དགེ་སློང་མ་ལྷགས་པ་རྣམས་ལ༌[^2858]འདུན་པ་དང་ཡོངས་སུ་དག་པར༌[^2859]བརྗོད་དོ། །

[Block 4126]
བརྗོད་པ་གང་རིག༌[^2860]པར་བགྱིད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4127]
ཁ་ཅིག་ལས་དགེ་འདུན་ལའོ་ཞེས་བྱ་བ་ནི། ལུགས་ཁ་ཅིག་ལས་དགེ་འདུན་ལ་བརྗོད་པར་བྱའོ་ཞེས་ཀྱང་འབྱུང་ངོ་། །བཙུན་པ་རྣམས་དགོངས་སུ་གསོལ་ཞེས་བྱ་བས་བརྩམ་མོ་ཞེས་བྱ་བ་ནི། དེ་ལྟར་འདུན་པ་ལ་སོགས་པ་བརྗོད་པར་བྱ་བ་ལ་སོགས་པ་ནི་རྩོམ་པ་རྩོམ་པའོ། །

[Block 4128]
བཙུན་པ་རྣམས་དགོངས་སུ་གསོལ་ཞེས་བྱ་བ་དང༌[^2861]གསན་དུ་གསོལ་ཞེས་བྱ་བ་ནི། དགེ་འདུན་གྱི་ནང་དུ་མ་ཕྱིན་པར་དུས་བྱས་སམ། ཁྱིམ་པ་ཉིད་ལ་སོགས་པའི་ཁས་བླངས་ན་མ་བླངས་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། འདུན་པ་ལ་སོགས་པ་དབང་དུ་བྱས་པས་རྗེས་སུ་འཇུག་པའོ། །

[Block 4129]
སོགས་པ་ཞེས་བྱ་བའི་སྒྲས་ནི་བསླབ་པ་དབུལ་བའི༌[^2862]ཚིག་དག་ཏུ་གཏོགས་པ་དགེ་ཚུལ་ཉིད་ཅེས་བྱ་བ་ལ་སོགས་པ་ནས། དེ་བཞིན་གཤེགས་པ་ལ་ངན་སེམས་ཀྱིས་ཁྲག་ཕྱུང་བ་ཞེས་བྱ་བའི༌[^2863]མཐར་ཐུག་པའི་བར་དག་བསྡུས་པའོ། །

[Block 4130]
ཕྱིན་ན་བླངས་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བར༌[^2864]གོ་བར་མ་བྱས་སུ་ཟིན་ཀྱང་འདི་ལ་ཐེ་ཚོམ་མེད་པར་བྱའོ་ཞེས་གོ་བར་བྱ་བའི་ཕྱིར་བརྗོད་པ་ཡིན་པས་དགེ་འདུན་གྱི་ནང་དུ་འོངས་པ་ཉིད། དགེ་འདུན་གྱི་ཁོངས་སུ་གཏོགས་པས་དེའི་དངོས་པོ་ལ་འདིར་གཙོ་བོ་སྟེ། དེ་བས་ན་འདིར་དེ་ཤེས་པའོ། །

[Block 4131]
གཞན་གྱིས༌[^2865]ཚེས་བཅོ་ལྔ་ལ་དགེ་སློང་བཟུང་ན་དེ་ལ་དགེ་འདུན་གྱིས་འདི་བདག་ཅག་གི་ཚངས་པ་མཚུངས་པར་སྤྱོད་པ་ཡིན་གྱི་ཐོང་ཤིག༌[^2866]ཅེས་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་ལ། གཞན་གྱིས་ཞེས་བྱ་བ་ནི། རྒྱལ་པོ་ལ་སོགས་པའོ། །

[Block 4132]
དེ་ལ་ཞེས་བྱ་བ་ནི་གཞན་ལ་བརྗོད་པར་བྱའོ། །

[Block 4133]
གང་གིས་དགེ་སློང་བཟུང་བར་གྱུར་པ་དེ་ལ་མངོན་སུམ་དུའམ་འཕྲིན་པ་བཏང་སྟེ། དེར་རང་གིས་སམ་ཐམས་ཅད་ཀྱིས་མ་བཏང་བ་དང་མ་བཏང་བར་འགྱུར་བ་མ་ཡིན་ཏེ། ཕོ་ཉའི་ཁ་ནས༌[^2867]སྨྲ་བ་གང་ཡིན་པ་དང་། རང་གིས༌[^2868]ཁ་ནས་སྨྲ་བ་གང་ཡིན་པ་འདི་གཉིས་ཀའི་བསྡུ་བ་ལ་དགོངས་ནས། དེ་ལྟར༌[^2869]ཉེ་བར་བཏགས་པའོ། །

[Block 4134]
མ་བཏང་ན་བདག་ཅག་འདི་དང་ལྷན་ཅིག་བྱ་བ་ཅུང་ཞིག་ཡོད་དོ་ཞེས་སྔ་མ་དང་བཅས་ཏེའོ་ཞེས་བྱ་བ་ལ། སྔ་མ་དང་བཅས་ཏེ་ཞེས་བྱ་བ་ནི་མདོ་སྔ་མ་དེས། ཐོང་ཤིག༌[^2870]ཅེས་སྨོས་པའི་ཚིག་སྔ་མ་དེ་དག༌[^2871]དང་བཅས་ཏེ། བདག་ཅག་དགེ་སློང་འདི་དང་ལྷན་ཅིག་བྱ་བ་ཅུང་ཟད་ཅིག་ཡོད་དོ་ཞེས་བྱ་བ་འདི་ལྟར་གཞན་ལ་བརྗོད་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4135]
དེ་ལྟ་ན་ཡང་དཀྱིལ་འཁོར་པར་བྱའོ་ཞེས་བྱ་བ་ནི། ཚིག་གཉིས་པ་བརྗོད་ཀྱང་མ་བཏང་ན་དེའི་ཚེ་དགེ་འདུན་གྱིས་དཀྱིལ་འཁོར་དུ་གསོ་སྦྱོང་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །
--- END BLOCKS ---
