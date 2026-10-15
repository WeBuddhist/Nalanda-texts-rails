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
གཞན་དུ་ཡང་གཉིས་པོ་འདི་དག་གང་ཟག་ལ་ཕྱིར་བཏང་བའི་སྔགས་ཀྱི༌[^2872]གཞུང་ནི་ཞུ་བ་ལས་བཙུན་པ་བཅོམ་ལྡན་འདས་ཀྱིས་གལ་ཏེ་ཡོངས་སུ་གནས་པར་བྱེད་པའི་དགྲ་བོ་འོངས༌[^2873]ན། དེ་ཡོངས་སུ་གནས་པའི་སྤྱོད་པ་བག་ཡངས་སུ་བྱའོ་ཞེས་བཀའ་སྩལ་ན༌[^2874]དེས་ཇི་ལྟར་བག་ཡངས་སུ་བགྱི། ཉེ་བ༌[^2875]འཁོར་དགེ་སློང་དེས་ཆོས་གོས་ཕྲག་པ་གཅིག་ཏུ་སྟེ། འཆིལ༌[^2876]ལྷམ་དག་ཕུད་ནས་དགེ་སློང་གི་མདུན་དུ་ཙོག་པུར་འདུག་སྟེ་འདི་སྐད་ཅེས་བརྗོད་པར་བྱའོ།[^2877] །བདག་དགེ་སློང་ཡོངས་སུ་གནས་པར་བགྱིད་པའི་དགྲ་བོ་དགེ་སློང་མཆིས་ཏེ། བདག་མིང་འདི་ཞེས་བགྱི་བ་ཡོངས་སུ་གནས་པའི་སྤྱོད་པ་བག་ཡངས་སུ་བགྱིད་ཅིང་སླར་ཡང་ལེན་པར་བགྱིད་དོ། །

[Block 3012]
ཡང་བླངས༌[^2878]ཏེ་སྤྱོད་པར་བགྱིད་ན་ཚེ་དང་ལྡན་པ་དག་གིས་བདག་ངོ་ཚ་མ་མཆིས་པར༌[^2879]གཟུང་དུ་གསོལ། །དེ་བཞིན་དུ་ལན་གཉིས། ལན་གསུམ་དུ་བཟླསཏེ།[^2880] ཐབས་ཡིན་ནོ་ལེགས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3013]
དགྲ་བོ་སོང་ན་ཕྱིར་ཡང་དེ་བཞིན་དུ་བླང་བར་བྱ་སྟེ། དེ་ནི་ཡོངས་སུ་གནས་པ་དང་མགུ་བར་བྱ་བར་སྤྱོད་པ་ཡིན་ནོ་ཞེས་གསུངས་ཏེ། དེ་ལ་གཉིས་ཀའི་སྦྱོར་བ་ཞེས་བྱ་བ་འདི་གཉིས་ཀ་བསྡུས་པའོ། །

[Block 3014]
འཇིགས༌[^2881]དང་བྲལ་ན་དེ་ཉིད་དུ་ཕྱིར་བླང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་གྱི་དྲུང་ངམ་གང་ཟག་ལའོ། །

[Block 3015]
ས་གཞན་ན་གནས་པའི་གཞིའོ།། །།

[Block 3016]
ཡོངས་སུ་གནས་པ་དང༌[^2882]མགུ་བར་བྱ་བ་སྤྱོད་པར༌[^2883]རང་བཞིན་དུ་གནས་པ་དང་ལྷན་ཅིག་ཏུ་གཡོགས་མ་གཅིག་པར་ཉལ་ན་ཉིན་མཚན་དེ་བཅད་དོ་ཞེས་བྱ་བ་ནི་ཇི་སྲིད་ཉལ་བའི་ཉིན་མཚན་དེ་ཡོངས་སུ་གནས་པར་བྱ་བ་དང་མགུ་བར་སྤྱད་པའི་ཞག་ཏུ་བགྲང་བར་མི་བྱ་ཞིང་བཅད་པར་བྱ་བའོ། །

[Block 3017]
འདིར་གཞུང་ནི་ཡོངས་སུ་གནས་པར་བྱེད་པས༌[^2884]རང་བཞིན་དུ་གནས་པ་དང་ལྷན་ཅིག་གཡོགས་མ་གཅིག་པར་ཉལ་བ་དེའི་ཉིན་མཚན་ཡོངས་སུ་གནས་པ་དང་། མགུ་བར་བྱ་བ་སྤྱོད་པ༌[^2885]མི་བགྲང་བར་མཚན་མོ་དེ་བཅད་དེ་བགྲང་བར་བྱའོ། །

[Block 3018]
མགུ་བར་བྱ་བ་སྤྱོད་པ་ཡང་དེ་བཞིན་ནོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3019]
མཚམས་ཀྱི་ཕྱི་རོལ་དུ་སྤྱད་པ་ཡང་ངོ་ཞེས་བྱ་བ་ཡང་ཉལ་ན་ཉིན་མཚན་དེ་བཅད་དོ་ཞེས་བྱ་བའི་རྗེས་སྙེགས༌[^2886]པའི་ཕྱིར་ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲ་སྨོས༌[^2887]སོ། །

[Block 3020]
མ་བརྗོད་ན་ཡང་ངོ་ཞེས་བྱ་བ༌[^2888]ཡོངས་སུ་གནས་པ་དང་མགུ་བར་བྱ་བ་སྤྱོད་པ་ཞག་འདས་པ་དང་འབྱུང་བར་འགྱུར་བ་མ་བརྗོད་ན་ཡང་ཉིན་མཚན་དེ་བཅད་པར་བྱའོ། །

[Block 3021]
ཐོས་པར་བྱ་བ་དག་མཚམས་དེ་ན་ཉེ་བར་མི་འཁོད་ན་མི་འབྱུང་ངོ་ཞེས་བྱ་བ་ནི་མཚམས་གང་དུ་དེ་སྤྱད་པར་བྱ་བའི་མཚམས་དེ་གང་ན་མང་དུ་ཐོས་པར་བྱ་བ་རྣམས་ལ་ཉེ་བར་མི་གནས་ན་མ་བརྗོད་པ་དེ་མི་འབྱུང་བའོ། །

[Block 3022]
ཉི་མ་དེ་ཉིད་ལ་ཕྱིར་འོང་ན་མཚམས་གཞན་དུ་འགྲོ་བ་ལ་ཉེས་པ་མེད་དོ། །

[Block 3023]
ཡོངས་སུ་གནས་པར་བྱེད་པས་ཡོངས་སུ་གནས་པར་བྱེད་པ་དང་ལྷན་ཅིག་གཡོགས་མ་གཅིག་པར་ཉལ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ཉིན་མཚན་སྤྱད་པར་ནི་མི་འགྱུར་མོད་ཀྱི་འོན་ཀྱང་ཉིན་མཚན་གྱི་མཐའ་ཉེས་བྱས་རྫོགས་པར་འགྱུར་ལ། དེའི་མདུན་རོལ་དུ་ནི་སྦྱོར་བ་ལས་བྱུང་བའི་ཉེས་བྱས་སུ་འགྱུར་བར༌[^2889]ཤེས་པར་བྱའོ། །

[Block 3024]
རང་བཞིན་དུ་གནས་པ་དང་ལྷན་ཅིག་ཉལ་བ་ཡང་ཁ་ན་མ་ཐོ་བ་དེ་གཉིས་སུ་འགྱུར་བའི་སྟེང་དུ་དེའི་ཉིན་མཚན་བཅད་པར༌[^2890]ཡང་འགྱུར་རོ། །

[Block 3025]
དེ་དང་མུ་སྟེགས་ཅན་ཡོངས་སུ་གནས་པ་ལ་གནས་པ་དང་། དེར་ལྷན་ཅིག་པ་ལ་ནི་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་དེར་ལྷན་ཅིག་པ་ལ་ཞེས་བྱ་བ་ནི་མུ་སྟེགས་ཅན་གྱི་གནས་དེར་རོ། །

[Block 3026]
དེར་ཞེས་བྱ་བ་ནི་ཉལ་ས༌[^2891]དེར་རོ། །

[Block 3027]
ཅིའི་ཕྱིར་ཡང་ཡོངས་སུ་གནས་པའི་གཞི་ལ་ས་གཞན་ན་གནས་པའི་སྤྱོད་པའི་གཞི་ཞེས་མིང་གཞན་དུ་བྱས་ཤེ༌[^2892]ན། ས་གཞན་ན་གནས་པ་དང་མགུ་བར་བྱ་བ༌[^2893]སྤྱོད་པ་དང་། བསླབ་པ་བྱིན་པ་ལ་སོགས་པ་གཞན་ན༌[^2894]གནས་པ་གང་ཇི་སྙེད་པ་དེ་དག་ཐམས་ཅད་གཞི་འདིས༌[^2895]སྤྱོད་པར་བསྟན་གྱི།[^2896] ཡོངས་སུ་གནས་པ་འབའ་ཞིག་ཏུ་ནི་མ༌[^2897]ཟད་པས་དེའི་དོན་དེ་བསྟན་པའི་ཕྱིར་དེ་ཤེས་པར་བྱའོ། །

[Block 3028]
ས་གཞན་ན་གནས་པ༌[^2898]སྤྱོད་པའི་གཞི་ཞུ་བའི་སྐབས་སོ། །

[Block 3029]
ས་གཞན་ན་གནས་པ་སྤྱད་པའི༌[^2899]གཞི་རྫོགས་སོ།། །།

[Block 3030 [HEADING]]
## ཡོངས་སུ་སྦྱང་བའི་གཞི། ^9-0

[Block 3031]
མ་གྲགས་པ་ནི་གཞི་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་འདོད་པ་རྣམས་ནི་ཞེ་སྡང་གིས་འཇུག་པ་ཡིན་ཏེ། དྲང་པོ་མ་ཡིན་པ་ལ་བརྟེན་ནས་འདི་རྣམས་ལ་མིའི་ཆོས་བླ་མར་གྱུར་པ་ཅིའི་ཕྱིར་ཞེ་ན། དེ་ལ་ཐ་དད་དུ་བྱ་བ་མ་ཡིན་པ་ལྟུང་བའི་ཐ་སྙད་ཁ་ཅིག་སྡིག་པ་འདོད་པ་རྣམས་ཀྱིས་དེ་ལྟ་བུའི་ངོ་བོ་ཉིད༌[^2900]འཇུག་པ་རྣམས་ཀྱིས་དགེ་སློང་རྣམས་ཉམས་པར་བྱས་པ་དེ་བས་ན་འདི་རྣམ་པར་གཞག་གོ། །

[Block 3032]
མ་གྲགས་པ་དེས་ཅིའི་ཕྱིར་གླེང་བར་མི་བྱ་ཞེ་ན། ཁ་ཅིག་མིའི་ཆོས་བླ་མ་དང་ལྡན་པས་སྔགས་ཀྱང༌[^2901]སྨན་གྱིས་བྱས་པའམ། སྐྱེ་བ་ལས་བྱུང་བ་གང་ཡིན་པ་འདི་ལྟ་སྟེ་དཔེར་ན་འཁོར་ལོས༌[^2902]སྒྱུར་བ་ལ་སོགས་པ་རྣམས་ཀྱིའོ། །

[Block 3033]
ཏིང་ངེ་འཛིན་ལས་གྲུབ་པའམ་མཉམ་པར་མ་བཞག༌[^2903]པའི་ས་ལ་གནས་པ་ནི་འདི་ལྟ་སྟེ། བྱེ་བྲག་ཅན་གྱི་ཡོན་ཏན་རྣམས་ཀྱི༌[^2904]རིགས་ལས་བྱུང་བ་ནི་འདོད་པ་ན་སྤྱོད་པ་རྣམས་སོ། །

[Block 3034]
འདིར་གཞུང་ནི། དགེ་སློང་དག་ལྷའི་མིག་ནི་ཐ་སྙད་དུ་བྱ་བ་མ་ཡིན་ཏེ། དེ་བས་ན་དགེ་སློང་གིས་ལྷའི་མིག་གིས་མཐོང་བས་གླེང་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནས་དེ་བཞིན་དུ་ལྷའི་རྣ་བས་གླེང་བར་མི་བྱའོ་ཞེས་བྱ་བ་ལ་སོགས་པའི་བར་དུ་གསུངས་པ་ཡིན་ནོ་ཞེ་ན་བདེན་མོད་ཀྱི། གཞན་དུ་ཡང་གྲགས་པ་ལས་མི་འདའ་བས་བྱས་ནས་འདི་ལ་འདོད་པ་ཉིད་རྣམ་པར་གནས་པ་ཡིན་ཏེ་སྐྱོན་མཚུངས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 3035]
ཐ་སྙད་དུ་བྱས་པ་མ་ཡིན་ཞེས་སྨོས་པས་ལོག་པར་རྟོག་པ་དེ་བས་ན་འདི་ལྟར་སྦྱར་བའོ། །

[Block 3036]
དགག་དབྱེ་བརྗོད་པ་རྫོགས་ན་དགག་དབྱེ་གཞག་པ་མི་འཆགས་སོ་ཞེས་བྱ་བ་ནི། གང་ཟག་གང་གིས་དགག་དབྱེ་བརྗོད་པ་རྫོགས་ན་མི་འཆགས་པའོ། །

[Block 3037]
དགག་དབྱེ་བརྗོད་པ་རྫོགས་པར་དགག་དབྱེ་འཇོག་པར་བྱེད་ན་ནི་འཆགས་སོ། །

[Block 3038]
དགག་དབྱེའི་སྔགས་ལན་ཅིག༌[^2905]བརྗོད་པ་ལ་ནི་དེའི་མཐར་ཕྱིན་པ་ཉིད་བརྗོད་པ་ཡིན་ཏེ། ལན་གཉིས་བརྗོད་པ་ལ་ནི་གཉིས་པའི་མཐར་ཕྱིན་པ་ཉིད་རྫོགས་པ་ཡིན་ནོ། །

[Block 3039]
ལན་གསུམ་དུ་བརྗོད་པ༌[^2906]གསུམ་པའི་མཐར་ཕྱིན་པ་ཉིད་རྫོགས་པ་ཡིན་ནོ། །

[Block 3040]
དགག་དབྱེའི་གཞི་ལས་དེ་ལ་སོགས་པས་དྲན་པ༌[^2907]ཉེ་བར་གཞག་སྟེ་ཞེས་བྱ་བ་ནས་ཤེས་བཞིན་ཞེས་བྱ་བའི་བར་དུ་གསུངས་པ་ཡིན་ནོ། །

[Block 3041]
བྱེད་པ་པོ་ནད་པ་དང་ལྡན་པ་ཉིད་ལ་ཡང་དེ་བཞིན་ནོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་དགག་དབྱེ་འཇོག་པ་པོ་ནད་པར་གྱུར་ན་དེས་དགག་དབྱེ་འཇོག་ཏུ་འཇུག་པ་ཡང་སྔ་མ་བཞིན་དུ་མི་འཆགས་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3042]
ཅི་དེས་མངོན་སུམ་དུ་འཇོག་པ་མི་འཆགས་པར་ཟད་དམ་ཞེ་ན། དེའི་ཕྱིར་མངགས་པས༌[^2908]ཀྱང་ངོ་ཞེས་བྱ་བ་ལས་ཀྱང་ངོ་ཞེས་བྱ་བའི་སྒྲས་ནི་རང་གིས་འཇོག་ཏུ་འཇུག་ན་ཡང་མི་འཆགས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3043]
ནད་པ་ཉིད་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་གཞན་གྱིས་ནད་པའི་དགག་དབྱེ་འཇོག་པར་བྱེད་ན། དེས་ཀྱང་ནད་པའི་དགག་དབྱེ་གཞག་པ་མི་འཆགས་པའོ།[^2909] །འདིར༌[^2910]དགག་དབྱེ་ཞེས་སྨོས་པས་ནི་གསོ་སྦྱོང་དང་གདམས་ངག་གཞག་པ་ལ་ཡང་ཆོ་ག་འདི་རིག་པར་བྱའོ། །

[Block 3044]
དེ་མནོད་པར༌[^2911]མི་བྱའོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་དགག་དབྱེ་གཞག་པ་མི་འཆགས་པ་བསྟན་པ་གང་ཡིན་པ་དེ་མནོད་པར༌[^2912]མི་བྱའོ། །

[Block 3045]
ཚེ་དང་ལྡན་པ་ནད་པ་ནི་སྦྱོར་མི་བཟོད་པ་ཡིན་གྱི་ཁྱེད་སྡོད་ཅིག་ཅེའམ། ཚེ་དང་ལྡན་པ་ཕོ་ཉ་དེ་ལ་ནི་བརྒལ༌[^2913]ཞིང་བརྟག་པ་མ་ཡིན་ནོ་ཞེས་ལན་གདབ་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་ནད་པ་རང་གི་དགག་དབྱེ་འཇོག་ཏུ་འཇུད༌[^2914]ན་དེའི་ཚེ་ཚེ་དང་ལྡན་པ་ནད་པ་ནི་སྦྱོར་མི་བཟོད་པ་ཡིན་གྱི༌[^2915]ཁྱོད་རང་སྡོད་ཅིག་ཅེས་ལན༌[^2916]གདབ་པར་བྱའོ། །

[Block 3046]
འོན་ཏེ་ནད་པས་མངགས་པ་དེ་ལ་ཚེ་དང་ལྡན་པ་ཕོ་ཉ་ནད་པ་དེ་ལ་བརྒལ༌[^2917]ཞིང་བརྟག་པར་བྱ་བ་མ་ཡིན་ནོ་ཞེས་ལན་གདབ་པར་བྱའོ། །

[Block 3047]
བྱས་པ་དང་བྱེད་པའི་རང་གི་ངོ་བོ་མ་རྟོགས་པ་ཉིད་ན་ཡང་གླེང་བ༌[^2918]མི་འཆགས་སོ་ཞེས་བྱ་བ་ལ་བྱས་པའི་རང་གི་ངོ་བོ་མ་རྟོགས་པ་ཉིད་ཅེས་བྱ་བ་ནི་འཕགས་པ་ཆེ་གེ་མོས་ཉེས་པ་བྱས་པ་ཞེས་ཐོས་ཀྱིས་ཉེས་པ་འདི་དང་འདི་ལྟ་བུ་བྱས་ཞེས་བྱ་བ༌[^2919]མ་ཐོས་སོ་ཞེས་ཟེར་བའོ། །

[Block 3048]
བྱེད་པའི༌[^2920]རང་གི་ངོ་བོ་མ་རྟོགས་པ་ཉིད་ཅེས་བྱ་བ་ནི་འཕགས་པས་ཉེས་པ་འདི་དང་འདི་ལྟ་བུ་བྱས་ཞེས་ནི་ཐོས་ཀྱི༌[^2921]ཆེ་གེ་མོ་ཞིག་གིས་ནི་མ་ཐོས་སོ་ཞེས་ཟེར་བ༌[^2922]སྟེ། དེ་ལྟར་བྱས་པ་དང་བྱེད་པའི་རང་གི་ངོ་བོ་མ་རྟོགས་པ་ཉིད་ཡིན་ན་ཡང་གླེང་བ་མི་འཆགས་སོ། །

[Block 3049]
ལྷག་མས་ཀྱང་དུས་མ་ཡིན་པར་འཇུག་པར༌[^2923]མི་བྱའོ་ཞེས་བྱ་བ་ལ་གནས༌[^2924]གང་དུ་གླེང་བར་བྱ་བའི་གང་ཟག་དེའི་བསྲུང་བར་བྱ་བ་རྣམས་ཀྱི༌[^2925]མདུན་དུ་དེས་བདག་ལ་བརྙས་ཐབས་བྱས་པར་འགྱུར་བའི་གནས་དེ་ལས་ལྷག་མས་ཀྱང་ཞེས་བྱ་བས་ནི་བྱེད་པ་པོ་ནད་པ་ལ་སོགས་པས་གླེང་བ་དེ་ལས་གཞན་པས་ཀྱང་དུས་མ་ཡིན་པར༌[^2926]འཇུག་པར་མི་བྱའི་དུས་སུ་འཇུག་པར་བྱའོ། །

[Block 3050]
དྲན་པ་དང་ཤེས་བཞིན་ཉེ་བར་མ་བཞག་པར་མི་བྱའོ། །
--- END BLOCKS ---
