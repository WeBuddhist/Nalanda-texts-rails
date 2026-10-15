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
[Block 3151]
ལས་བྱེད་པའི༌[^3064]གཞིའོ།། །།

[Block 3152]
ཆོས་མ་ཡིན་པ་སྨྲ་བ་དག་གིས་དབྱེ་བའི་སེམས་ཀྱིས་མཚམས་ཀྱི་ནང་དུ་ལས་ཐ་དད་པ་བྱས་ན་བྱེ་བ༌[^3065]ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ནང་དུ་བཅས་པ་འདི་རྣམས་བདག་ཅག་ལ་ནི་ཅི་དགོས། འདི་རྣམས་ཁོ་བོ་ཅག་ལས་ཐ་དད་པར་གྱུར་ཅིག་སྙམ་དུ་དབྱེ་བའི་སེམས་ཀྱིས་ཆོས་སྨྲ་བ་རྣམས་ཀྱི༌[^3066]མཚམས་ཀྱི་ནང་དུ་ཆོས་མ་ཡིན་པ་སྨྲ་བ་དག་ལས་ཐ་དད་པའི་ལས་བྱས་པ་ལས་དེ་བྱེ་བ་ནི་ལས་བྱེ་བ་ཞེས་བྱ་བའི་དོན་ནོ། །

[Block 3153]
འདིར་གཞུང་ནི་སིལ་བུ་དག་གིས་ཀཽ་ཤཱམྦཱི་པའི་དགེ་འདུན་ཕྱེ་བར་འགྱུར། [^3067]ཆོས་མ་ཡིན་པ་དག་གིས་མཚམས་ཀྱི་ནང་དུ་གསོ་སྦྱོང་མ་འདྲེས་པར་བྱས་པས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3154]
ཡང་ན༌[^3068]ཆོས་སྨྲ་བ་རྣམས་ཀྱིས་ཆོས་མ་ཡིན་པ་སྨྲ་བའི་ཕྱོགས་དག་ལ༌[^3069]ཐ་དད་པར་བྱས་པ་ནི་མཚམས་ཀྱི་ནང་དུ་ལས་བྱེད་པ་མ་ཡིན་ནོ། །

[Block 3155]
ཆོས་ལས་མི་གཡོ་བ་དེ་རྣམས་ཀྱིས་དེ༌[^3070]བྱས་པས་གནས་ནས་དབྱུང་བ་རྣམ་པ་དེས་ཆོས་མ་ཡིན་པ་སྨྲ་བ་རྣམས་ལ་ཞེས་བྱ་བའོ། །

[Block 3156]
འདི་ལ་སོ་སོ་རང་གི་ལས་ནི་འཆགས་སོ་ཞེས་བྱ་བ་ནི་ལས་བྱེད་པའི་བདག་ཉིད་ཀྱི་དགེ་འདུན་བྱེ་བ་འདི་ལ་ཕྱོགས་སོ་སོའི་ལས་ཐ་དད་པར་བྱས་པ་ནི་ཐ་དད་པར་འཆགས་པའོ། །

[Block 3157]
རང་གི་ཕྱོགས་དང་མཐུན་པ་མ་ཡིན་པ་ལ་ནི་མི་འཆགས་སོ་ཞེས་བྱ་བ་ནི་རང་གི་ཕྱོགས་དང་མཐུན་པ་མ་ཡིན་པའི་གང་ཟག་ལ་ནི་ལས་མི་འཆགས་སོ། །

[Block 3158]
འདིར་གཞུང་ནི་དགེ་སློང་བྱེ་བར་རྣམ་པར་གནས་ནས་ཕན་ཚུན་གྱི་ཕྱོགས་ནས་འབྱིན་པར་བགྱིད་ན། གནས་ནས་ཕྱུང་བར་བརྗོད་པར་བགྱིའམ། བཀའ་སྩལ་པ། གནས་ནས་མ་ཕྱུང་བ༌[^3071]བརྗོད་པར་བགྱིའོ༌[^3072]ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3159]
དགེ་འདུན་གྱི་ནི་ཆོས་སྨྲ་བར་བྱས་པ་ཉིད་ན་བྱས་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་གྱི་མཚམས་བཅད་པ་ལ་སོགས་པའི་ལས་གང་ཡིན་པ་དེ་ནི་ཆོས་སྨྲ་བ་དག་གིས་བྱས་པ་ཉིད་ན་བྱས་པ༌[^3073]ཉིད་ཡིན་གྱི་ཆོས་མ་ཡིན་པ་སྨྲ་བ་དག་གིས༌[^3074]བྱས་པ་ཉིད༌[^3075]ན་ནི་བྱས་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 3160]
འདིར་གཞུང་ནི་དགེ་འདུན་བྱེ་ན་གཅིག༌[^3076]གམ་ཅིག་ཤོས་ཀྱིས༌[^3077]མཚམས་དགྲོལ་བར་བགྱིད་ན་མཚམས་དགྲོལ་བར་བྱེད་པར༌[^3078]བརྗོད་པར་བགྱི་འམ། གལ་ཏེ་ཆོས་སྨྲ་བས་དགྲོལ་བར་བྱེད་ན་དགྲོལ་བར་བརྗོད་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3161]
འདི་ལ་གལ་ཏེ་གཟུ་བོ་དག་ཡོད་ན་དགེ་སློང་མ་རྣམས་ལ་བསྟན་པར་བྱ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་དབྱེ་བ་འདི་ལ་གལ་ཏེ་གཟུ་བོ༌[^3079]དག་ཡོད་ན་དེ༌[^3080]དག༌[^3081]གིས་དགེ་སློང་མ་རྣམས་ལ་བསྟན་པར་བྱ་བ་དག་ཡིན་ནོ། །

[Block 3162]
གལ་ཏེ་དེ་དག་མེད་ན་ཆོས་སྨྲ་བ་དག་ཉིད་ཀྱིས་སོ། །

[Block 3163]
འདིར་གཞུང་ནི་ཞུ་བ་ལས་བཙུན་པ་རེ་ཞིག་ཀཽ་ཤཱམྦཱི་བའི་དགེ་སློང་ཕྱོགས་གཉིས་སུ་འདུས་ཤིང་མཆིས་པར་གྱུར་ན། དེ་གཉིས་གང་གིས་དགེ་སློང་མ་རྣམས་ལ་བསྟན་པར་བགྱི། ཉེ་བ༌[^3082]འཁོར་གཟུ་བོ་དག་གིས་མཚམས་ཀྱི་ཕྱི་རོལ་དུ་སོང་སྟེ་བསྟན་པར་བྱའོ་ཞེས་གསུངས་པ་དང་བྲམ་ཟེའི་བུ་མོས་ཞུས་པ་ལས་ཀྱང་གལ་ཏེ་གཟུ་བོ༌[^3083]དག་མེད་ན་ཆོས་སྨྲ་བ་དག་ཁོ་ནས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3164]
དེ་དག་གིས༌[^3084]ནི་ཆོས་ཀྱི་ཕྱོགས་དང་མཐུན་པ་དག་གིས་མི་མཐུན་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་གཟུ་བོ་དེ་དག་གི་ལས་ནི་ཆོས་ཀྱི་ཕྱོགས་དང་མཐུན་པ་དག་གིས་མི༌[^3085]མཐུན་པར་འགྱུར་བ་སྟེ། དེ་དག་ནི་དགེ་འདུན་གྱི་ཁོངས་སུ་གཏོགས་པའི་ཕྱིར་དང་དགེ་འདུན་ལས་ཐ་མི་དད་པའི་ཕྱིར་རོ། །

[Block 3165]
ཆོས་མ་ཡིན་པའི་ཕྱོགས་དང་མཐུན་པ་དག་གིས་ནི་མ་ཡིན་ནོ། །

[Block 3166]
གཟུ་བོ་འམ་དགེ་སློང་དག་གིས་ལས་ལ་ཆོས་སྨྲ་བ་དག་དང་མི་མཐུན་པ་སྤང་བར་བྱ་ཞིང་དེ་དག་ལྷན་ཅིག་ཏུ་གནས་ན་ཡང་འཆགས་སོ། །

[Block 3167]
ཆོས་མ་ཡིན་པ་སྨྲ་བ་དག་ཀྱང་ནི་མ་ཡིན་ནོ། །

[Block 3168]
དེ་ལྟ་བས་ན་དེ་ལ་འདི་བསྟན་པའོ། །

[Block 3169]
རྗེས་སུ་ཞུགས་ན་དེ་ཉིད་ཉམས་སོ་ཞེས་བྱ་བ་ནི་གཟུ་བོ་རྣམས་གང་ཡང་རུང་བའི་ཕྱོགས་ཀྱི་རྗེས་སུ་ཞུགས་ན་གཟུ་བོ་ཉིད་ཉམས་སོ། །

[Block 3170]
གང་གི་ཕྱིར་དབུས་ན་གནས་པ་ཉིད་ནི༌[^3086]ཞལ་ཅེ་བ༌[^3087]ཉིད་ཡིན་ནོ། །

[Block 3171]
ཕྱོགས་དེ་གཉིས་ལས་ཕྱོགས་གང་ཡང་རུང་བ་ཅིག་ཤོས་སུ་ཡང་མ་ལྟུང་ལ་ཅིག་ཤོས་སུ་ཡང་མ་ལྟུང་བ་ཉིད་ཀྱིས་སྐབས༌[^3088]ལ་གནས་པ་ནི་གཟུ་བོ༌[^3089]ཞེས་བྱ་བར་བསྟན་པའོ། །

[Block 3172]
དེ་ལྟར་ཡང་འདིར་གཞུང་ནི་ཞུ་བ་ལས།

[Block 3173]
ཡངས་པ་ཅན་གྱི་དགེ་སློང་གི་གཞི་བཅུ་བྱུང་བ་ན། དགེ་སློང༌[^3090]གནས་བརྟན་གང་དག་ཕྱོགས་ཅིག་ཤོས་སུ་ཡང་མ་གཏོགས་ལ་ཕྱོགས་གཉིས་པར་ཡང་མ་གཏོགས་པ་དེ་དག་ཅི་ལགས་པར་བརྗོད་པར་བགྱི། སྐམ་ལ་གནས་པ་གཟུ་བོ་ཡིན་པར་བརྗོད་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3174]
འདིར༌[^3091]ཕྱོགས་འགའ་ཞིག་སྒྲུབ་པ་ལ་གཟུ་བོ་དང་། དབུས་ན་གནས་པ་དང་ཞལ་ཅེ་བ༌[^3092]མིན་པར་རིག་པར་བྱའོ། །

[Block 3175]
དེ་ནི་མི་བྱའོ་ཞེས་བྱ་བ་ནི་གཟུ་བོ་ཉིད་ཉམས་པ་ཉིད་མི་བྱའོ། །

[Block 3176]
འདིར་གཞུང་ནི་དགེ་འདུན་བྱེ་བར་རྣམ་པར་གནས་པ་ན༌[^3093]གཟུ་བོ་རྣམས་ཀྱིས་ཇི་ལྟར་བསྒྲུབ་པར་བགྱི། ཕྱོགས་ཅིག་ཤོས་སུ་ཡང་རང་འགྲོ་བར་མི་བྱའོ། །

[Block 3177]
མངག༌[^3094]པ་གཏང་བར༌[^3095]མི་བྱ་ཞིང་། ཕྱོགས་གཉིས་པར་ཡང་རང་འགྲོ་བར་མི་བྱ་ལ་མངག༌[^3096]པ་གཏང་བར༌[^3097]མི་བྱ་བར་ལུས་ཀྱིས་ཀྱང་བསྡམ་པར་བྱ། ངག་གིས་ཀྱང་བསྡམ་པར་བྱ་ཞིང་མཚམས་ཀྱི་ཕྱི་རོལ་དུ་སོང་སྟེ་གསོ་སྦྱོང་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3178]
དགེ་སློང་མའི་དགེ་འདུན་ཕྱོགས་དང་གཞན་གྱི་ཕྱོགས་སུ་རྣམ་པར་གནས་པ་ལ་གདམས་པར་བྱ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། འདིར་གཞུང་ནི་དགེ་སློང་མའི་དགེ་འདུན་ཕྱོགས་དང་ཕྱོགས་ལ་རྣམ་པར་གནས་པ་ལ་དགུང་ཟླ་ཕྱེད་ཕྱེད་ཅིང་གདམས་ངག་དང་རྗེས་སུ་བསྟན་པ་སྩལ་བར་བགྱི་འམ་བཀའ་སྩལ་པ། དགེ་སློང་མའི་དགེ་འདུན་བྱེ་བར་མི་འགྱུར་བའི་ཕྱིར་སྦྱིན་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3179]
བྱེ་བ་ལ་ནི་དེ་ལྟ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་མའི་དགེ་འདུན་ལས་དང༌[^3098]འཁོར་ལོ་བྱེ་བས་ཕྱོགས་དང་གཞན་གྱི་ཕྱོགས་སུ་རྣམ་པར་གནས་པ་ལ་ནི་སྔ་མ་ལྟར་གདམས་པར་མི་བྱ་བ་ཉིད་ཡིན་ནོ། །

[Block 3180]
འཁོར་གྱི་བྱེ་བས་གནས་ཐ་དད་པ་རྣམས་ཡང་ངོ་། །མཚམས་གཞན་དུ་གཏོགས་པ་ཉིད་ཀྱིས་ཐ་དད་པ་ཉིད་རྙེད་པ་ཉིད་ཀྱིས་བྱེ་བྲག་ཏུ་བསྐུལ་བར་བྱ་བ་མ་ཡིན་པ་ཉིད་དོ། །

[Block 3181]
གསོལ་བ་ན་མཐུན་པར་བྱེ་བ་ཉིད་ལ་ངེས་པར་སྦྱར༌[^3099]བར་བྱ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་དགེ་སློང་མ་བྱེ་བ༌[^3100]ཕྱོགས་གཞན་དང་གཞན་གྱི་ཕྱོགས་སུ་རྣམ་པར་གནས་པ་དག་གདམས་ངག་གསོལ་བ་ནི་སྲིང་མོ་དག་རྗེས་སུ་མཐུན་པར་གྱིས་ཤིག་ཅེས་མཐུན་པ་ཉིད་ལ་ངེས་པར་སྦྱར་བར་བྱའོ། །

[Block 3182]
དབྱར་གྱི་རྙེད་པ་ནི་ཆོས་སྨྲ་བ་དབང་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་བྱེ་བ་ན་དབྱར་གནས་པའི་རྒྱུ་ལས་བྱུང་བའི་རྙེད་པ་ནི་ཆོས་སྨྲ་བ་དག་དབང་བ་ཡིན་གྱི་ཆོས་མ་ཡིན་པ་སྨྲ་བ་དག་མི་དབང་ངོ་། །

[Block 3183]
གཉིས་ཀ་འདུས་པ་ལ་བྱེ་བྲག་ཏུ་མ་བྱས་པར་བགོ་བཤའ་བྱ་བ་དགེ་འདུན་ལ་ཕུལ་བ་ཡང་ངོ་ཞེས་བྱ་བ་ནི༌[^3101]ཆོས་དང་ཆོས་མ་ཡིན་པ་སྨྲ་བའི་ཕྱོགས་གཉིས་ཀ་འདུས་པ་ལ་བྱེ་བྲག་ཏུ་མ་བྱས་པར་དགེ་འདུན་ཙམ་ལ་ཕུལ་བའི་བགོ་བཤའ་བྱ་བར་འོས་པ་གང་ཞིག་བདག་གིས་མ་ཡིན༌[^3102]ཞིང་། ཆོས་གོས་ལ་སོགས་པའི་དངོས་པོ་ཕུལ་བ་དེ་གཉིས་ཀ་མ་ཡིན་པ་དང་། ཆོས་མ་ཡིན་པར་སྨྲ་བ་དག་ཀྱང་མི་དབང་ངོ་ཞེས་བགོ་བཤའ་བྱས་ནས་དེ་ལ་ཆོས་སྨྲ་བ་རྣམས་དབང་བ་ཉིད་དོ།[^3103] །ཆོས་མ་ཡིན་པ་སྨྲ་བ་དག་ནི་མི་དབང་ངོ་། །ཅི་ཐམས་ཅད་ལ་དེ་ལྟར་རྣམ་པར་གཞག་ཅེ་ན། དེའི་ཕྱིར་དེ་ལ་གལ་ཏེ་དགེ་འདུན་གྱི་ཚད་ཉིད་ཡིན་ན་དེ་དག་གོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གལ་ཏེ་ཆོས་སྨྲ་བ་དག་བཞི་ཡན་ཆད་ཡིན་ན་དེའི་ཚེ་རྙེད་པ་དེ་དག་དབང་བ་རྣམ་པར་གཞག་གོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3184]
དེ་དག་ཉུང་བ་ཉིད་ཡིན་ན་ཇི་ལྟར་བསྒྲུབ་པར་བྱ་ཞེ་ན་དེའི་ཕྱིར་གལ་ཏེ་ཉུང་བ་ཉིད་ཡིན་ལ་ཅིག་ཤོས་ཀྱིས༌[^3104]ནི་དེ་ཉིད་ཡིན་ན་གང་གིས་ཕང་བར་ཕུལ་བའི་འོ༌[^3105]ཞེས་བྱ་བ་སྨོས་ཏེ། གལ་ཏེ་དེ་ན་ཆོས་སྨྲ་བ་དག་ནི་དགེ་འདུན་གྱི་ཚད་ལ༌[^3106]ཉུང་བ་ཉིད་ཡིན་ལ་ཆོས་མ་ཡིན་པ་སྨྲ་བ་ཅིག་ཤོས་ན༌[^3107]དགེ་འདུན་གྱི་ཚད་དེ་ཡིན་ན་ནི་ཕྱོགས་དེ་གཉིས་ཀྱི་གང་ཟག་གི་ཕང་བར༌[^3108]རྙེད་པ་དེ་ཕུལ་བའི་ཕྱོགས་དེ་རྙེད་པ་དེ་དབང་ངོ་། །ཕང་པ༌[^3109]ཞེས་སྨོས་པ་ནི་ལག་པ་དང་རྐང་པའི་དྲུང་དག་ཀྱང་དཔེ་ཡིན་ནོ། །

[Block 3185]
གང་དུ་བཞག་པའི་གང་ཟག་དེ་ལ་གཞག་པ་ཉིད་ཅེས་བྱ་བ་ཡིན་ཏེ། དེ་ལ་རྣམ་པར་གཞག་པ་ཉིད་དོ། །

[Block 3186]
གང་ཞིག་འདིར་ཆོས་སྨྲ་བ་རྣམས་ཉུང་ལ་ཅིག་ཤོས་ཚད་པ་ཉིད་ལ་དགེ་སློང་གཉིས་ཀ་ལ་གཅིག་ལ་གཅིག་གི༌[^3110]ཕྱོགས་དང་གཞན་ལ་གཞན་གྱི་ཕྱོགས་པའི་ཕང༌[^3111]ལ་སོགས་པའི་ཕུལ་བ་དེ་ལ་ཇི་ལྟར་བསྒྲུབ་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་གལ་ཏེ་གཉིས་ཀའི་ན་གཉིས་ཀའི་འོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གལ་ཏེ་ཕྱོགས་གཉིས་ཀའི་དགེ་སློང་དག་གི་ཕྱོགས་གཅིག་དང་འབྲེལ་པ་ཅན་གཅིག་དང་། ཕྱོགས་གཞན་དང་འབྲེལ་པ་ཅན་གཞན་གྱི་ཕང་བ༌[^3112]ལ་སོགས་པར་ཕུལ་ན་ཕྱོགས་གཉིས་ཀ་དབང་བ་ཉིད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3187]
དེ་ལ་ཕྱོགས་གཉིས་ཀས་དབང་བ་ཉིད་ལ་ནི༌[^3113]ཅི་ཕྱོགས་བརྒྱ་ལ་གང་ཟག་གི་ལ༌[^3114]བགོ་བར་བྱ་བ་འམ་ཞེ་ན་དེའི་ཕྱིར། དེ་ལ་གང་ཟག་ལས་ཆ་ཉིད་ཡིན་གྱི་དགེ་འདུན་ལས་མ་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་ཟག་ཇི་སྙེད་ཡོད་པ་དེ་སྙེད་ཀྱི་ཆ་ཉིད་དུ་བྱའོ་ཞེས་བྱ་བའི༌[^3115]དོན་ཏོ། །

[Block 3188]
ལས་བྱེ་བའི་གཞི་ཞུ་བ་དང་བྲམ་ཟེའི་བུ་མོའི་སྐབས་སོ། །

[Block 3189]
ལས་བྱེ་བའི་གཞི་རྫོགས་སོ།། །།

[Block 3190 [HEADING]]
## རྩོད་པའི་གཞི། ^11-0
--- END BLOCKS ---
