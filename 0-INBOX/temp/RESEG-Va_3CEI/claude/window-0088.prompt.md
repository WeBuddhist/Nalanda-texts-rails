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
[Block 3081]
ཚད་མེད་རྒྱལ་བ་ངོ་མཚར་འགྱུར།[^2600] །ཞེས་པ་ནས། འཇིག་རྟེན་རིག་པ་ཇི་ལྟར་དགྱེས་བཞིན་སྤྱོད། །ཞེས་པའི༌[^2601]བར་དུ་ནི་གཞལ་མེད་ཁང་དབུལ་བ་དང་། བསྟོད་དེ་ཕྱག་འཚལ་བའོ། །

[Block 3082]
མདོ་ལས་དེ་ནས་དགེ་སློང་རྣམས་ཚངས་པ་ཆེན་པོ་དེ་དག་ཅེས་པ་ནས་དེ་བཞིན་གཤེགས་པ༌[^2602]ལ་གསོལ་བ་ལགས་ཞེས་པའི་བར་དུ་ནི་ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་བར་གསོལ་བའོ། །

[Block 3083]
མདོ་ལས་དགེ་སློང་དག་དེ་ནས་ཚངས་པ་ཆེན་པོ་ཞེས་པ་ནས། དེ་ནས་དགེ་སློང་རྣམས་བཅོམ་ལྡན་འདས་དེས་ཚངས་པ་དེ་རྣམས་ལ་ཅང་མི་གསུང་བར་དེ་ན་བཞུགས་སོ་ཞེས་པའི་བར་དུ་ནི་ཆོས་བཤད་པར་གནང༌[^2603]བའོ། །

[Block 3084]
དེ་ནས་ཡང་དགེ་སློང་རྣམས་ཞེས་པ་ནས་ཕན་ཚུན་དོང་ཞིང་སྨྲའོ་ཞེས་པའི་བར་དུ་ནི་ཚངས་པ་རྣམས་ལ་བསྐུལ་བའོ། །

[Block 3085]
དེ་ནས་དགེ་སློང་རྣམས་ཞེས་པ་ནས་གདོན་མི་ཟ་བར་འབྱུང་བར་འགྱུར་ཞེས་པའི་བར་དུ་ནི་ལྷ་རྣམས་ཀྱིས་གསོལ་བའོ། །

[Block 3086]
དེ་ནས་དགེ་སློང་རྣམས་ཚངས་པ་བྱེ་བ་ཁྲག་ཁྲིག་ཅེས་པ་ནས་གཤེགས༌[^2604]སུ་གསོལ་ཞེས་པའི་བར་དུ་ནི་ཆོས་བཤད་པར་གསོལ་བ་དང་། མཆོད་པར་གསོལ་བའོ། །

[Block 3087]
དེ་ནས་དགེ་སློང་རྣམས་ཚངས་པ་ཆེན་པོ་དེ་དག་གིས་ཞེས་པ་ནས་ཕྱག་ཀྱང་འཚལ་ཞེས་པའི་བར་དུ་ནི་བསྟོད་དེ་ཕྱག་འཚལ་བའོ། །

[Block 3088]
མདོ་ལས།

[Block 3089]
ངོ་མཚར་གྱུར་པ་བརྒྱ་ལ༌[^2605]འཇིག་རྟེན་དུ། །ཞེས་པ་ནས་རྟག་ཏུ་མཉམ་པར་གྱུར་ཞེས་པའི་བར་དུ་ནི་འཇིག་རྟེན་དུ་གཤེགས་པ་དཀོན་པ༌[^2606]བསྟན་པའོ། །

[Block 3090]
མདོ་ལས་བསྐལ་པ་ཁྲག་ཁྲིག་བརྒྱད་ཅུ་ཞེས་པ་ནས། བསོད་ནམས་ཀྱིས་ནི་འཇིག་རྟེན་ཞེས་པའི་བར་དུ་ནི་སྤྱན་དུ་གྱུར་པ་དང་སྐྱབས་སུ་གྱུར་བ་བསྟན་ཏོ། །

[Block 3091]
མདོ་ལས་དེ་ནས་དགེ་སློང་རྣམས་ཞེས་པ་ནས་དུལ་ཞིང་ཞི་ལ་རབ་ཏུ་བདེ་བར་འགྱུར་ཞེས་པའི་བར་དུ་ནི་དེ་བཞིན་གཤེགས་པ་ལ་བསྟོད་པ་དང་། ཞི་ཞིང་དུལ་བས་འཕགས་པའི་ལམ་བསྒྲུབ་པ་བསྟན་ཏོ། །

[Block 3092]
མདོ་ལས་དེ་ནས་དགེ་སློང་རྣམས་བཅོམ་ལྡན་འདས་དེ༌[^2607]ཞེས་པ་ནས་མི་གསུང་བར་བཞུགས་སོ་ཞེས་པའི་བར་དུ་ནི་གནང་བ་བསྟན༌[^2608]ཏོ། །

[Block 3093]
མདོ་ལས་དེ་ནས་ཡང་དགེ་སློང་རྣམས་ཞེས་པ་ནས་ཡང་ན་འདིར་ནི་སངས་རྒྱས་མངོན་པར་བྱུང་ཞེས་པའི་བར་དུ་ནི་གོང་མ་དང་འདྲ་བར་སྦྱར་རོ། །

[Block 3094]
ཆོས་བཤད་པར་གསོལ་བའོ། །

[Block 3095]
མདོ་ལས་དེ་ནས་དགེ་སློང་རྣམས་འཇིག་རྟེན་གྱི་ཁམས་ཞེས་པ་ནས། བདག་ཅག་ལ་ནི་བརྩེ་ཕྱིར་ཡོངས་སུ་སྤྱོད། །ཅེས་པའི་བར་དུ་ནི་བཤད་པའི་ཚུལ་གོང་མ་དག་དང་འདྲ་བར་སྦྱར་རོ། །

[Block 3096]
མདོ་ལས་དེ་ནས་དགེ་སློང་རྣམས་ཚངས་པ་ཆེན་པོ་དེ་དག་ཅེས་པ་ནས་བྱང་ཆུབ་མཆོག་ལ་རེག་པར་རོ་ཞེས་པའི་བར་དུ་ནི་ལམ་འདི་སྡིག་ཅན་ཞེས་པ་ནི་ཁྱིམ་ན་གནས་པས་སྡིག་པ༌[^2609]སྤྱོད་པ་མུ་སྟེགས་ཅན་སྤྱོད་པ་ངན་པ་ལ་གནས་པ༌[^2610]སྡིག་སྤྱོད་པའོ། །

[Block 3097]
བདེ་བའི་འདུ་ཤེས་ནི་གཉེན་པོས་གནས་པ་སྟེ། སྡུག་བསྔལ་སྐད་ཅིག་ཙམ་ཞི་བ་ལ་བདེ་བར་སེམས་པ་ལ་བདེ་བ་དེ་ཉིད་ཀྱང་སྟོར་ཞེས་པའོ། །

[Block 3098]
མདོ་ལས་དེ་ནས་དགེ་སློང་རྣམས་ཚངས་པ་ཆེན་པོ་དེ་དག་གིས་ཞེས་པ་ནས་བསྐལ་པ་བྱེ་བ་སྟོང་དུ་བསྒྲུབས་པའོ་ཞེས་པའི་བར་དུ་ནི་བསྟོད་དེ་བཤད་པར་གསོལ་བའོ། །

[Block 3099 [HEADING]]
##### ཕྱོགས་བཅུའི་ལྷ་དང་ཚངས་པ་ལ་བཤད་པར་གནང་བ། ^4-7-6-2-0

[Block 3100]
མདོ་ལས་དེ་ནས་དགེ་སློང་རྣམས་བཅོམ་ལྡན་འདས་མངོན་པར་ཤེས་པ་ཆེན་པོའི་ཡེ་ཤེས་ཀྱི་ཟིལ་གྱིས་གནོན༌[^2611]ཞེས་པ་ནས་རྣམ་པ་བཅུ་གཉིས་སུ་བསྐོར་བ་ཞེས་པའི་བར་དུ་ནི་དེ་ལྟར་ཆོས་བཤད་པར་གནང་ནས་བཤད་དོ་ཞེས་པ་དང་། གཞན་གྱིས་མི་ནུས་ཞེས་པ་དང་། བཤད་པའི་དུས་དང་། བཤད་པས་ཕན་པ་ཐོབ་པ་དང་བཞིར་དབྱེ་སྟེ། འདི་ནི་དང་པོའོ། །

[Block 3101]
ཆོས་ཀྱི་འཁོར་ལོ་གསུམ་དུ་བཟླས་ཏེ་ཞེས་པ་ནི་བདག་གི་དོན་དང་། གཞན་གྱི་དོན་ལ་འདི་ནི་གཞན་གྱི་དང་སྦྱར་རོ། །

[Block 3102]
[^2612]སྡུག་བསྔལ་ཞེས་པ་ནི་སྡུག་བསྔལ་གྱི་བདེན་པ་སྟེ། མཚན་ཉིད་དེ་བསྟན་པའི་ཕྱིར་ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་བའོ། །

[Block 3103]
འཁོར་ལོའི༌[^2613]དོན་ནི་གོང་དུ་བསྟན་པ་ཡིན། འཁོར་ལོ་དེ་བསྐོར་བས་ཟག་པ་མེད་པའི་ཡེ་ཤེས་སྐྱེ་བར་འགྱུར་བའི་ཕྱིར་བསྟན་ཏོ། །

[Block 3104]
ལན་གསུམ་བཟླས་པ་ཡང་དེ་གཅིག་ཅིང་ཡང་མཚན་ཉིད་བཅུ་གསུམ་དང་ལྡན་པར་སྟོན་པའོ། །

[Block 3105]
དགེ་སྦྱོང་དང་། ཚངས་པ་གཞན་གྱིས་བསྐོར་མི་ནུས་ཀྱི༌[^2614]བཅོམ་ལྡན་འདས་ཐམས་ཅད་མཁྱེན་པ་ཉག་གཅིག་གིས་ཞེས་པའོ། །

[Block 3106]
མདོ་ལས་འདི་ལྟ་སྟེ༌[^2615]འདི་ནི་སྡུག་བསྔལ་ལོ་ཞེས་པ་ནས་འགྲོ་བ་བསྒྲུབ་པའི༌[^2616]བདེན་པའོ་ཞེས་པའི་བར་དུ་ནི་ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་བ་ཡང་བདེན་པ་བཞི་ལ་བརྟེན་ཏེ་བསྐོར་བ་དང་། རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་བཅུ་གཉིས་ལ་བརྟེན༌[^2617]ཏེ་བསྐོར་བའོ། །

[Block 3107]
སྡུག་བསྔལ་བ༌[^2618]ནི་འཇིག་རྟེན་རྣམ་གཉིས་ཀྱི་ཆོས་ཟག་པ་དང་བཅས་པ་ཐམས་ཅད་དོ། །

[Block 3108]
ཀུན་འབྱུང་ནི་སྡུག་བསྔལ་སྐྱེ་ཞིང་འབྱུང་བའི་རྒྱུ་འབྱིན་པ་ལས་དང་ཉོན་མོངས་པའི་རང་བཞིན་ཅན་ནོ། །

[Block 3109]
འགོག་པ་ནི་ཡང་དག་པ་དང་བརྟགས་ཏེ་འགོག་པ་དང་། མི་གཡོ་བ་དང་། འདུས་མ་བྱས་འགོག་པའི་བདེན་པ་སྟེ། ཡང་དག་པའི་ལམ་གྱིས༌[^2619]སྡུག་བསྔལ་མི་སྐྱེ་བར་གྱུར་པའོ། །

[Block 3110]
ལམ་ནི་ཟག་པ་མེད་པའི་ཕུང་པོ་ལྔ་སྟེ། ཚོགས་སོགས༌[^2620]པའི་ལམ་དང་། ལྷག་པར་སྤྱོད་པའི་ལམ་དང་། མཐོང་བའི་ལམ་དང་། བསྒོམ་པའི་ལམ་དང་། མཐར་གྱུར་པའི་ལམ་སྟེ། ལམ་གྱི་འཁོར་རྣམས་ཐམས་ཅད་ནི་ལམ་གྱི་བདེན་པའོ། །

[Block 3111]
བདེན་པ་ཞེས་པ་ནི་འཕགས་པ་རྣམས་ཀྱིས་ཆུད་པའི་ཆོས་པས་འཕགས་པའི་བདེན་པའོ། །

[Block 3112]
མདོ་ལས་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཞེས་པ་ནས་འགག་པར་འགྱུར་རོ་ཞེས་པའི་བར་དུ་ནི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ལུགས་ལས་བཟློག་པ་བསྟན་པ་སྟེ། ཉོན་མོངས་པ་དང་། རྣམ་པར་བྱང་བའི་ཚུལ༌[^2621]ཅི་རིགས་པར་སྦྱར་རོ། །

[Block 3113]
མ་རིག་པ་ཞེས་པ་ནི་ཉོན་མོངས་པ་མི་ཤེས་པའི་རང་བཞིན་ཅན། འདུ་བྱེད་ནི་ལུས་དང་ངག་དང་ཡིད༌[^2622]གསུམ་གྱི་སྒོ་ནས་དགེ་བ་དང་མི་དགེ་བར༌[^2623]འཇུག་པའོ། །

[Block 3114]
རྣམ་པར་ཤེས་པ་ཞེས་པ་ནི་རྣམ་པར་སྨིན་པའི་རང་བཞིན་ཅན་ས་བོན་གྱི་བག་ཆགས་སུ་གནས་པའི་རྣམ་པར་ཤེས་པའོ། །

[Block 3115]
མིང་དང་གཟུགས་ཞེས་པ་ནི་དེའི་འོག་མའི་རྐྱེན་གསུམ་སྤངས་པ་ཐམས་ཅད་ནི་མིང་དང་གཟུགས་སོ། །

[Block 3116]
སྐྱེ་མཆེད་དྲུག་ནི་རྣམ་པར་སྨིན་པའི་དབང་པོ་དྲུག་ཅན་ནོ། །

[Block 3117]
རེག་པ་ནི་རྣམ་པར་སྨིན་པའི་རེག་པ་མྱོང་བ་ཉིད་རེག་པའོ། །

[Block 3118]
ཚོར་བ་ནི་རྣམ་པ་གསུམ་མྱོང་བའོ། །

[Block 3119]
སྲེད་པ་ནི་ཕྱི་ནང་གི་ཡུལ་ལ་ཆེ་ཆུང་རྣམ་པ་གསུམ་དུ་ཞེན་པའོ། །

[Block 3120]
ལེན་པ་ནི་ཉོན་མོངས་པའི་བདག་ཉིད་ཅན་གཟུང་བ་དང་འཛིན་པའི་ཆོས་ཀྱི་ཉོན་མོངས་པའི་ཕུང་པོ་ལེན་པའོ། །
--- END BLOCKS ---
