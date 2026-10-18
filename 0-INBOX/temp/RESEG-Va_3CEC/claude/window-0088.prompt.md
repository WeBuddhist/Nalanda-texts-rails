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
གཟུངས་དང་སྤོབས་པ་གཉིས་མི་ཟད་པར་ཡང་གཟུངས་ཀྱིས༌[^2679]དྲན་པར་བྱ་བའི་ཆོས་རྣམས་དང་། སྤོབས་པས༌[^2680]རྟོགས་པར་བྱ་ཞིང་བཤད་པར་བྱ་བའི་ཆོས་རྣམས་མི་ཟད་པས་ན་དྲན་པར་བྱེད་པ་དང་། འཆད་པར་བྱེད་པ་ཡང་མི་ཟད་པའོ། །

[Block 3082]
སོ་སོར་རྟེན་པའི་བྱང་ཆུབ་སེམས་དཔའ་ཡང་རྣམ་པ་གཉིས་ཏེ། ཐོས་པ་མི་བརྗེད་པ་དང་། མ་ཐོས༌[^2681]པ་འདོད་པའོ། །

[Block 3083 [HEADING]]
### ཐོས་པ་མི་བརྗེད་པ། ^9-1-0

[Block 3084]
ཐོས་པ་མི་བརྗེད་པ་གང་ཞེ་ན། གང་གསུངས་པ་སོ་སོར་ཐོབ་པ་སྟེ། དེའི་དབང་དུ་བྱས་ནས། དེ་ལ་གཟུངས་ནི་མི་བརྗེད་པ་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 3085]
དེ་ཡང་གང་གིས་མི་བརྗེད་པ་དང་། གང་མི་བརྗེད་པ་དང་། མི་བརྗེད་པ་ཉམས་པ་མེད་པའོ། །

[Block 3086]
དེ་ལ་གང་གིས་མི་བརྗེད་པ་ནི། དགེ་བའི་རྩ་བའི་ཚོགས་བསགས་པའི་དྲན་པ་ཞེས་བྱ་བ་ནས་བསྟན་ཏོ། །

[Block 3087]
གང་མི་བརྗེད་པ་ནི་ཆོས་ཀྱི་ཕུང་པོ་བརྒྱད་ཁྲི་བཞི་སྟོང་ཞེས་བྱ་བ་ནས། འདི་ནི་གཟུངས་ཞེས་བྱའོ་ཞེས་བྱ་བའི་བར་གྱིས་བསྟན་ཏོ། །

[Block 3088]
མི་བརྗེད་པ་ཉམས་པར་མི་འགྱུར་བ་ནི། གང་གི་ཚེ་བསྐལ་པ་གཞན་གྱི་རྗེས་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། སྐྱུ་རུ་རའི་འབྲུ་འདུག་པ་བཞིན་དུ་མཐོང་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས༌[^2682]བསྟན་ཏོ། །

[Block 3089]
སྔོན་གྱི༌[^2683]དགེ་བའི་རྩ་བའི་ཚོགས་བསགས་པའི་དྲན་པ་ཞེས་བྱ་བ་ནི་ཚེ་རབས་སྔ་མའི་དུས་ན་བསོད༌[^2684]ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་བསགས་པའི་རྒྱུ་ལས་བྱུང་བའི་དྲན་པས་སོ། །

[Block 3090]
འཛིན་པ་ནི་ཡི་གེ་རྣམས་སོ། །

[Block 3091]
ཀུན་འཛིན་པ་ནི་དོན་རྣམས་སོ། །

[Block 3092]
མི་བརྗེད་པ་ནི་ཕྱིས་ཀྱང་ཡི་གེ་མི་བརྗེད་པར་བྱེད་པའོ། །

[Block 3093]
དྲན་པས་ཡང་དག་པར་འཛིན་པ་ནི་ཕྱིས་ཀྱང་དོན༌[^2685]མི་བརྗེད་པར་བྱེད་པ་སྟེ། དེ་དག་གིས༌[^2686]ནི་གཟུངས་ཀྱི་གསུང༌[^2687]རབ་འཇིག་རྟེན་དུ་བཤད་དེ་གཞག་པ་རྣམས་མི་བརྗེད་པར་བྱེད་པ་བསྟན་ཏོ། །

[Block 3094]
སངས་རྒྱས་ཐམས་ཅད་ཀྱིས་གསུངས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་འཕྲལ་དུ་གསུངས་པའི་དོན་དང་། ཚིག་མི་བརྗེད་པར་བྱེད་པ་བསྟན་ཏོ། །

[Block 3095]
ཆུད་ཟ་བར་མི་འགྱུར་བ་ནི་ཆོས་དང་དོན་དྲན་པའི་ཡེ་ཤེས་དེ་མེད་པར་མི་འགྱུར་བའོ། །

[Block 3096]
བརྗེད་པར་ཡང་མི་འགྱུར་བ་ནི་ཁ་ཅིག་དྲན་པ་ཁ་ཅིག་མི་དྲན་པ་སྟེ།[^2688] དྲན་པ་དྲི་མ་ཅན་དུ་མ་གྱུར་པའོ། །

[Block 3097]
འཕགས་པའི༌[^2689]ཤེས་རབ་ཀྱི་མིག་གིས་ཞེས་བྱ་བ་ནི་ཟག་པ་མེད་པའི་ཡེ་ཤེས་ཀྱི་མིག་དང་འདྲ་བས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3098 [HEADING]]
### མ་ཐོས་པ་འདོད་པ། ^9-2-0

[Block 3099]
མ་ཐོས་པ༌[^2690]འདོད་པ་གང་ཞེ་ན། གང་སྤོབས་པ་སོ་སོར་ཐོབ་པ་སྟེ། དེའི་དབང་དུ་བྱས་ནས། དེ་ལ་སྤོབས་པ་མི་ཟད་པ་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །གང་ལ་ཡང་བརྟེན་མི་དགོས་པར་བསྟན་པས་ན། [^2691]ཐོགས་པ་མེད་པའི་སྤོབས་པའོ། །

[Block 3100]
བསྐལ་པའམ་དེ་ལས་ལྷག་པར་ཡང་སྟོན་པས་ན་རྒྱུན་ཆད༌[^2692]མེད་པར་སྤོབས་པའོ། །

[Block 3101]
བདུད་དང་མུ་སྟེགས་ཅན་ལ་སོགས་པས་ཟིལ་གྱིས་མི་ནོན་ཅིང་ནམས་ཀྱང་ཉམས་པར་འགྱུར་བ་མེད་པས་ན་མི་འཕྲོགས་པའི་སྤོབས་པའོ། །

[Block 3102]
ཆོས་དང་དོན༌[^2693]མི་བརྗེད་པས་ན་མ་རྨོངས་པའི་སྤོབས་པའོ། །

[Block 3103]
དྲིས་པ་རྣམས་ལ་ལན་གློན་པས་ན་མྱུར་བའི་སྤོབས་པའོ། །

[Block 3104]
གང་དང་གང་བསྟན་པ་རྣམས་ཀྱིས་སེམས་ཀྱི་དབང་པོ་ལ་དགའ་བ་སྐྱེད་པར་བྱེད་པས་ན་དགའ་བའི་སྤོབས་པའོ། །

[Block 3105]
གཞན་དག་ཟིལ་གྱིས་གནོན་པར་བྱེད་པས་ན་ལ་གོར་དུ་སྤོབས་པའོ། །

[Block 3106]
ཇི་ལྟར་ཁས་བླངས་པ་ལས་བསྒྱུར་ཏེ་གཞན་དུ་འཆད་པར་བྱེད་པས་ན་མི་འགྱུར་བའི་སྤོབས་པའོ། །

[Block 3107]
ཆོས་ཀྱི་དོན་མྱུར་དུ་རྟོགས་པས་ན་རྣོ་བའི་སྤོབས་པའོ། །

[Block 3108]
ཟབ་མོའི་དོན༌[^2694]རྟོགས་པར་བྱེད་པས་ན་མགྱོགས་པའི་སྤོབས་པ་སྟེ། འདི་ནི་བྱང་ཆུབ་སེམས་དཔའི་སྤོབས་པའི་མཚན་ཉིད་དོ། །

[Block 3109]
དེའི་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའ་དེའི་འོ།[^2695] །དེ་ཞེས་བྱ་བ་ནི་གོང་དུ་བཤད་པའི་སྤོབས་པ་དེའོ། །

[Block 3110]
ལས་ཀྱི་རྣམ་པར་སྨིན་པས་ཡོངས་སུ་སྦྱངས་པ་ཞེས་བྱ་བ་ནི་ལུས་དང་། ངག་དང་ཡིད་ཀྱི་ལས་ཡོངས་སུ་དག་པས་དེའི་ཤེས་རབ་ཀྱིས༌[^2696]རང་བཞིན་སྤོབས་པ་དེ་ཡང་ཡོངས་སུ་དག༌[^2697]ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 3111]
སངས་རྒྱས་ཀྱིས་བྱིན་གྱིས་བརླབས་པ་ཞེས་བྱ་བ་ནི་སངས་རྒྱས་ཀྱི་མཐུས་བསྟངས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3112]
ལྷ་རྣམས་ཀྱིས་ཡོངས་སུ་བཟུང་བ་ཞེས་བྱ་བ་ནི་དྲིས་པའི་ལན་གདབ་པ་དང་། བཤད་པ་ལ་སོགས་པ་རྫོགས་ཤིང་མ་ལུས་པར་སྟོན་པའམ་ཟུར་ཆག་ཅིང་ཉམས་པ་མེད་པར་སྟོན་ནུས་པའོ། །

[Block 3113]
འབྲས་བུ་ཡོད་པར་ཆོས་སྟོན་པ་ཞེས་བྱ་བ་ནི་དོན་གང་དང་གང་གི་ཕྱིར། ཆོས་བསྟན་པའི་དོན་དེ་དང་དེ་དག་དེ་བཞིན་དུ་ཡོད་པར་འགྱུར་བའོ། །

[Block 3114]
མྱ་ངན་ལས་འདས་པའི་ལམ་དུ་འགྲོ་ཞེས་བྱ་བ་ནི་སྤོབས་པས་ཆོས་བཤད་པ་རྣམས། མྱ་ངན་ལས་འདས་པ་ཐོབ་པར་བྱེད་པའི་ལམ་དང་མཐུན་པར༌[^2698]འགྱུར་བའོ། །

[Block 3115]
དེས༌[^2699]ཞེས་བྱ་བ་ནི་སྤོབས་པ་རྣམ་པར་དག་པ་དང་ལྡན་པའི་བྱང་ཆུབ་སེམས་དཔའ་དེའོ། །

[Block 3116]
དེ་ལྟར་སྤོབས་པ་ཕུན་སུམ་ཚོགས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གོང་དུ་བཤད་པ་ལྟ་བུར་ན་སྤོབས་པ་མཐར་ཕྱིན་པ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3117]
གཟུགས་སུ་སྣང་བ་ཇི་སྙེད་པ་ཞེས་བྱ་བ་ནི་གཟུགས་སུ་སྣང་བའི་ཆོས་ཇི་སྙེད་པ་རྣམས་མི་རྟག་པ༌[^2700]ལ་སོགས་པར་སུན་འབྱིན་པ་དང་། ཆོས་དེ་དག་གི༌[^2701]མཚན་ཉིད་ཚིགས་སུ་བཅད་དེ་སྦྱར་ཏེ་བསྟན་པར་ནུས་པའི་ཤེས་རབ་ཀྱང་དེ་སྙེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3118]
དེ་བཞིན་དུ་སྒྲ་ལ་ཡང་སྦྱར་རོ། །

[Block 3119]
དེ་དང་དེར་ཞེས་བྱ་བ་ནི་འཁོར་དེ་དང་དེ་དག་ཏུའོ། །

[Block 3120]
དེའི་ལྷུན་གྱིས་གྲུབ་པ༌[^2702]ཉིད་དུ་ཞེས་བྱ་བ་ནི། བྱང་ཆུབ་སེམས་དཔའ་དེའི་སྤོབས་པ་རྩོལ་བ་དང་འབད་པ་མེད་པར་ཞེས་བྱ་བའི་དོན་ཏོ། །
--- END BLOCKS ---
