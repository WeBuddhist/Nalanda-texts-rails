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
གང་ཞིག་སྨྲས་ན་དགེ་འདུན་ལྷག་མར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་འཁྲིག་པ་སྨྲས་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བུད་མེད་མཐུ་ཡོད་པ་ལ་ཀུན་ནས་ཆགས་པས་ཞེས་བྱ་བ་འདི་སྔར་བརྗོད་པ་རྟོགས་པར་བྱའོ། །

[Block 3082]
སླར་ཡང་འཁྲིག་པ་ནི་གཉིས་ཀྱིས་གཉིས་སྤྲོད་པ་སྟེ་དེ་སྨྲས་ནའོ། །

[Block 3083]
སྒྲ་ཇི་ལྟ་བུས་དེ་བརྗོད་པ་གང༌[^2108]ཞེ་ན། དེའི་ཕྱིར་རྒྱ་ལ་སོགས་པའི་དོན་གྱིས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར༌[^2109]རྒྱ་ལ་སོགས་པའི་སྒྲ་ནི་ཡ་ཡིག་དང་བྷ་ཡིག་གི་རང་བཞིན་ཞེས་བྱ་བ་བརྗོད་པའོ། །

[Block 3084]
དེའི་དོན་ཅན་རྒྱ་ལ་སོགས་པ་རྣམ་པ་གཞན་གྱིས་འཁྲིག་པ་བརྗོད་པ་གང་ཡིན་པར་སྟོན་པ་དེ་ནི་རྒྱ་ལ་སོགས་པ་ཞེས་བྱ་བ་གྲགས་པ་ཉེ་བར་སོང་བའོ། །

[Block 3085]
རྒྱའི་དོན་ནི་མཐོང་བར་རིག་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 3086]
དེ་ལྟར་ཡང་བཅོམ་ལྡན་འདས་ཀྱིས་བདག་དང་ལྷན་ཅིག་བུད་པར་གྱིས་ཤིག་ཅེས་བྱ་བ་དེ་ལ་ཉེས་པ་སྦོམ་པོར་གསུངས་པ་ཡིན་ནོ། །

[Block 3087]
བྱེ་བྲག་མ་བྱས་པའི་སྒྲ་ལ་ཡང་བརྗོད་པར་འདོད་པའི་དབང་གིས༌[^2110]ཁྱད་པར་དུ་གཞག་པ་སྟེ། དེ་བས་ན་བདག་ཉིད་ཀྱིས༌[^2111]བརྗོད་པར་འདོད་པ་གསལ་བར༌[^2112]བྱེད་པའི་སྒྲ་མེད་ཀྱང་རང་གིས༌[^2113]བརྗོད་པར་འདོད་པས་སྦྱོར་བར་རྟོགས་པ་ལ་དེའི་བརྗོད་པར་འདོད་པ་ཉིད་ལ་གཞན་གྱི་དངོས་གཞི་བསྐྱེད་པར་རིག་པར་བྱའོ། །

[Block 3088]
ཡ་ཡིག་བྷ་ཡིག་ལ་སོགས་པ་གང་ཡང་རུང་བའི་སྒྲ་ལ་བརྗོད་པར་འདོད་པ་ལ་ཡིན་ཏེ། བུད་མེད་ལ་གནས་པའི་བདག་ཉིད་བརྗོད་པར་འདོད་པས་ཐོས་སུ་བཅུག་པ་ཙམ་ལ་ཉེས་བྱས་ནི་ཡིན་ནོ། །

[Block 3089]
འདིར་བྱ་བའི་ཚིག་ནི་དགོངས་པ་མ་ཡིན་ནོ། །

[Block 3090]
བདག་ཉིད་དུ་རྣམ་པར་རིག་པར་བྱ་བ་དག་ལ་མཚམས་ཉེ་བར་སྦྱོར་བས་ཁས་ལེན་པའི་ངོ་བོས༌[^2114]ནི་མ་ཡིན་ནོ།[^2115] །འགྲོ་བ་བརྗོད་པ་ཉིད་ལ་འདིར་སྐྱོན་ཉིད་བསྟན་པས་དོན་གྱིས་བསྙེན་པ་རྩོམ་པར་གྱུར་པ་ཉིད་ལ་ནི་མ་ཡིན་ནོ། །

[Block 3091]
འདིར་རང་གི་འདོད་པ་ཉིད་སྨྲ་བ་ཡོད་པས་གྱུར་པ་ཡང་གཞན་གྱིས་མ་ཤེས་པ་ལ་སྦོམ་པོའོ་ཞེས་བྱ་བ་འདི་ཤེས་པའི་དོན་དུ་ངེས་པའི་མདོ་འདི་ལས་རྟོགས་པར་བྱའོ། །

[Block 3092]
རང་གི་སྨྲ་བར་གྱུར་པ་ཉིད་མེད་པ་ལ་སྦོམ་པོ་ཉིད་ནི་རང་གི་དོན་ཉིད་དོ། །

[Block 3093]
དེ་ནི་དེའི་གཙོ་བོ་ཞེས་བྱ་བ་འདི་ལས་སོ། །

[Block 3094]
གང་ལ་གོ་བར་བྱ་བ་ཉིད་དེ་བརྡ་ཕྲད་པ་ནི་མཐའོ་ཞེས་བྱ་བ་ནི་འདིར་བརྡ་ཕྲད་པ་ནི་བརྗོད་པར་འདོད་པའི་དོན་ཡོངས་སུ་ཐོབ་པའོ། །

[Block 3095]
བརྗོད་པར་འདོད་པའི་དོན་ཡོངས་སུ་ཐོབ་པར་བྱེད་པའི་དོན་ཅན་གྱི་ལུས་དང་ངག་ཕྲད་པར་བྱེད་པའི་བདག་ཉིད་ཅན་ཐམས་ཅད་ལ་དོན་གཅིག་ལ་རྩོམ་པར་གྱུར་པ་ཉིད་ཀྱི་ཕྱིར་སྐད་ཅིག་མ་གཅིག་ཏུ་གྱུར་པའོ། །

[Block 3096]
འདིར་ལྟུང་བ་རྣམ་པར་གཞག་པ་མེད་པར་གྱུར་པ་ཉིད་དེ་མཐའ་དང་མཐའ་མེད་པའི་དབྱེ་བ་ཇི་ཙམ་དུ་བྱས་པ་ལ་དངོས་གཞིའི་ལྟུང་བ་བསྐྱེད་པ་སྟེ་ཞེས་བྱ་བ་འདི་ལ་མདོ་འདིའོ། །

[Block 3097]
ཚིག་ལ་སོགས་པའི་མཐའ་ནི་མཐའ་ཞེས་བྱ་བ་འདི་རྣམ་པར་གཞག་པ་མ་ཡིན་ཏེ། འོན་ཀྱང་མཐའ་ལས་བྱུང་བའམ་མཐའ་མ་ཡིན་པ་གང་ཡིན་པ་གང༌[^2116]ཞིག་ལ་ཡི་གེ་ལ་སོགས་པ་གང་ཞིག་ལ་གཞན་གྱི༌[^2117]ཤེས་པར་རུང་བ་ཉིད་བརྗོད་པར་འདོད་པའི་དོན་ཤེས་པ་ལས་སྣོད་དུ་རུང་བ་ཉིད་དུ་གྱུར་པ་ལ་རྟོག་པ་པོ་ལ་རྣ་བའི་རྣམ་པར་ཤེས་པའམ་མིག་གི་རྣམ་པར་ཤེས་པ་ལ་བསྒྲུབ་པ་གང་ཡིན་པ་དེ་ནི་འདིར་མཐའོ། །

[Block 3098]
དེ་བས་ན་དེར་དངོས་གཞིའོ། །

[Block 3099]
དེའི་འོག་ཏུ་རྩོམ་པ་གཅིག་ཏུ་གྱུར་པའི་ཕྱིར་དེ་ཉིད་དུ་ཞུགས་པའོ། །

[Block 3100]
གལ་ཏེ་ཡི་གེ་དང་པོ་ཤེས་པའི་དུས་ན་ཡང་དེ་ལ་དངོས་གཞིའི༌[^2118]ཞེས་བྱ་བ་རིག་པར་བྱ་སྟེ། འདིར་ཤེས་པ་ལ་ཡན་ལག་ཉིད་དོ། །

[Block 3101]
དེ་དང་འབྲེལ༌[^2119]བའི་དོན་སྨྲས་པ་ནི་སྦྱོར་བ་མ་ཡིན་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་འདིར་དངོས་གཞིའི་དོན་གྱི་ཚིག་ཡ་ཡིག་དང་བྷ་ཡིག་གི༌[^2120]རང་བཞིན་ཅན་ལ་དེའི་སྒྲ་བཟུང་བའོ། །

[Block 3102]
འབྲེལ་བ་ཞེས་བྱ་བ་ནི་དངོས་གཞིའི་དོན་ཉིད་ཀྱི་ཚིག་དང་འབྲེལ་པའི་དོན་གང་ཡིན་པའོ། །

[Block 3103]
དེ་སྨྲས་པ་གང་ཡིན་པ་ནི་འདི་ལྟ་སྟེ། དཔེར་ན་བསྔགས་པ་བྱེད་པ་ལ་སོགས་པ་ལ་སྲུ་ཁྱོད་ཀྱི་རྨའི་སྒོ་གསུམ་པོ་རྣམས་ལེགས་པར་དོད༌[^2121]དམ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨྲས་པའོ། །

[Block 3104]
ཡ་ཡིག་བྷ་ཡིག་གི་རང་བཞིན་གྱི་སྒྲ་མེད་པར་དེ་ལ་སྦྱོར་བ་མེད་པ་ཉིད་དོ། །

[Block 3105]
མ་སྨྲས་པ་ལ་དངོས་གཞི་བྱས་པའི་སྒྲ་ལ་དེ་དང་འབྲེལ་པ་མེད་པ་ཉིད་ཀྱི་ཕྱིར་སྨྲ་བ་འདི་ལ་སྦྱོར་བ་མ་ཡིན་པ་ཉིད་གང་ཞིག་འདོད་པ་དེ་འདོད་པ་བཟློག་པའི་དོན་དུ་མདོ་འདི་བྱས་ཏེ། རྒྱ་ཞེས་བྱ་བ་དང༌[^2122]རྣ་རུ་ཞེས་བྱ་བ་ལ༌[^2123]སོགས་པའི་སྒྲ་བརྗོད་པ་ལ་ནི་སྦྱོར་བ་ཉིད་ཐེ་ཚོམ་མེད་པའོ། །

[Block 3106]
བསྔགས་པ་དང་བསྔགས་པ་མ་ཡིན་པ་དང་། གསོལ་བ་དང་ཉེ་བར་གསོལ་བ་དང་། འདྲི་བ་དང་ཉེ་བར་འདྲི་བ་དང་། བརྗོད་པ་དང་སྨོན་པ་དང་གཤེ་བ་དང་། ཕྱིར་སྨྲ་བ་བསྒྲུབ་པ་དག་ལ་ནི་བྱེ་བྲག་མེད་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་བསྔགས་པ་ལ་སོགས་པའི་བདག་ཉིད་ཅན་གྱིས༌[^2124]སྨོན་པ་ཐམས་ཅད་ཉིད་རྣམས་ལ་དངོས་གཞིའི་བྱེད་པ་ཉིད་དེ། བྱེ་བྲག་ཅུང་ཟད་ཀྱང་མེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3107]
དེ་ལ་བསྔགས་པ་ཞེས་བྱ་བ་ནི་སྲུའི་རྨའི་སྒོ་གསུམ་རྣམས་ལེགས་པར་དོད་པ་ཡིན་ནམ་ཞེས་བྱ་བའོ། །

[Block 3108]
བསྔགས་པ་མ་ཡིན་པ་ཞེས་བྱ་བ་ནི་དེ་ལས་བཟློག་པར་སྨོད་པའོ། །

[Block 3109]
གསོལ་བ་ཞེས་བྱ་བ་ནི་སྲུ་ཚུར་ཤོག་དེ་དང་དེ་བྱའོ་ཞེས་བརྗོད་ཅིང་། རྒྱ་ཞེས་བྱ་བ་དང་རྣ་རུ་ཞེས་བྱ་བ་གཉིས་ཀྱིས་བརྗོད་པ་གང་ཡིན་པའོ། །

[Block 3110]
ཉེ་བར་གསོལ་བ་ཞེས་བྱ་བ་ནི་སྲུ་བུད་མེད་དམ་སྐྱེས་པ་གང་ལ་ལ་འདི་དང་འདི་བྱེད་དེ། དེ་ལ་དགའ་བ་དང་ཡིད་དུ་འོང་བར་འགྱུར་རོ། །

[Block 3111]
སྲུ་ཡང་བདག་ཅག་ལ་དེ་དང་དེ་བྱེད་དོ། །

[Block 3112]
སྲུ་ཡང་བདག་ཅག་ལ་དགའ་བ་དང་ཡིད་དུ་འོང་བར་འགྱུར་རོ་ཞེས་བྱ་བ་དགའ་བ་ཉེ་བར་བསྒྲུབ་པས་འདུན་པ་སྐྱེད་པ༌[^2125]སྟེ། འདི་ནི་དགའ་བ་ཉེ་བར་བསྒྲུབ་པ། འདི་ནི་གསོལ་པའོ། །

[Block 3113]
འདྲི་བ༌[^2126]ཞེས་བྱ་བ་ནི་སྲུ་སྐྱེས་པ་གང་དང་བུད་མེད་གང་དེ་དང་དེ་བྱེད་པ་དེ་ནི་དགའ་བ་དང་ཡིད་དུ་འོང་བར་འགྱུར་ན་ཁོ་བོས་ཀྱང་སྲུ་ལ་དེ་དང་དེ་བྱས་ན་སྲུ༌[^2127]ཁོ་བོ་ལ་དགའ་བ་དང་ཡིད་དུ་འོང་བར་འགྱུར་རམ་ཞེས་འདྲི་བའོ། །

[Block 3114]
ཉེ་བར་འདྲི་བ༌[^2128]ཞེས་བྱ་བ་ནི་སྲུའི་རྨའི་སྒོ་གསུམ་པོ་རྣམས་ལེགས་པར་དོད་པ་དང་། ལེགས་པར་གནས་པ་དང་། ལེགས་པར་གྱུར་པ་བདེན་ནམ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཡོངས་སུ་འདྲི་བའོ། །

[Block 3115]
བརྗོད་པ་ཞེས་བྱ་བ་ནི༌[^2129]ཁོ་བོ་ནི་ཁྱོད་ལ་དགའ་བ་དང་ཡིད་དུ་འོང་བ་བདེན་ན་ཁྱོད་དེ་ལ་ཇི་ལྟར་ཞེས་བརྗོད་པའོ། །

[Block 3116]
སྨོན་པ་ཞེས་བྱ་བ་ནི་སྲུ་ནམ་ཞིག་ན་ཁོ་བོ་ཁྱོད་དང་ལྷན་ཅིག་དེ་དང་དེ་ལྟར་བྱེད་ཞིག་གུ་སྙམ་དུ་སྨོས༌[^2130]པའོ། །

[Block 3117]
གཤེ་བ་ཞེས་བྱ་བ་ནི་ཁྱོད་ལ་བོང་བུ་རྣམས་གང་དེ་ལྟར་བྱེད་པར་གྱུར་ཅིག་པའི་བློས་འདིར་མི་ལྟུང་ཞེས་གཤེ་བའོ། །

[Block 3118]
ཕྱིར་སྨྲ་བ་ཞེས་བྱ་བ་ནི་བུད་མེད་ཀྱིས་བརྗོད་པའི་བསྔགས་པ་ལ་སོགས་པ་ལ་དགེ་སློང་གིས་ཕྱིར་རྣམ་པ་དེ་རྣམས་ཀྱིས་སླར་ལན་འདེབས་པའོ། །

[Block 3119]
དོན་གཞན་ལ་བསམས་པས་ལྗོངས་ཀྱི་ངེས་པའི་ཚིག་གི་དབང་གིས་ན་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་འདི་ནི་མི་མཛེས་པ་ཞེས་བྱ་བ་བསམས་པར་གྱུར་པ་ལ་ལྟུང་བའི་བློས་འདིར་མི་ལྟུང་བའོ་ཞེས་བྱ་བ་དེའི་ཟློག༌[^2131]པའི་དོན་དུ་མདོ་འདི་དང་འོག་མའོ། །

[Block 3120]
ཅི་སྟེ་དོན་གཞན་ལ་བསམས་པ་ཞེས་བྱ་བ་ལྗོངས་ཀྱི་ཚིག་འདིའི་ངེས་པའི་ཚིག་གི་དབང་གིས༌[^2132]དོན་གཞན་གྱི་བསམ་པས༌[^2133]འཁྲིག་པ་སྨྲས་པ་གང་ཡིན་པ་དེ་ལ་ནི་ལྟུང་བ་མེད་དེ། གང་ཞིག་རུང་བ་ཙམ་གྱིས་གཞན་ལ་བསམ་པར་བྱེད་པ་ནི་མ་ཡིན་ཞེས་བྱ་བའོ། །
--- END BLOCKS ---
