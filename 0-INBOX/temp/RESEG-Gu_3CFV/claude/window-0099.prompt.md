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
[Block 3466]
དང་པོ་འཁྲུགས་པ༌[^2262]དང་། མ་ནིང་དང་། དགེ་སློང་མ་སུན་ཕྱུང་བས་ཉམས་པར་བྱས་པ་ནི་ཉེས་བྱས་སུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3467]
འདིར༌[^2263]རྐུ་ཐབས་སུ་གནས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་པ་ནི་མ་སྐྱེས་པ་ཐམས་ཅད་ཀྱི་དཔེ་ཙམ་དུ་ཟད་དོ། །

[Block 3468]
དེ་བས་ན་ཐམས་ཅད་མ་སྐྱེས་པའི་ཁོངས་སུ་བསྡུ་བར་བྱས་སོ། །

[Block 3469]
སྔར་ལྟུང་བ་བྱུང་བ་ཞེས་བྱ་བ་ནི་འདི་ལྟར་སྔར་བསྙེན་པར་རྫོགས་པ་ཉིད་ཀྱི་ཚེ་ན་ལྟུང་བ་བྱུང་བར༌[^2264]རིག་པར་བྱ་བའོ། །

[Block 3470]
བསྙེན་པར་མ་རྫོགས་ཤིང་རབ་ཏུ་བྱུང་བས་བླངས་པ་ལས་འདས་པ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ལ་ཉེས་བྱས་སོ་ཞེས་བྱ་བའི་རྗེས་སུ་སྙེག་པའི༌[^2265]ཕྱིར་ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲ་སྨོས་སོ། །

[Block 3471]
འདིར་དགེ་ཚུལ་དང་། དགེ་ཚུལ་མ་དང་། དགེ་སློང་མ་རྣམས་ཀྱིས་ཡང་དག་པར་བླངས་པའི་སྤྱོད་པ་ལས་འདའ་བར་བྱེད་པ་ནི་ཉེས་བྱས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3472]
ལྟུང་བ་ལ་སྦྱོར་བ་ལ་ནི་ཉེས་བྱས་སོ་ཞེས་སྔར་སྨོས་པས་འདིར་ཡང་ལྟུང་བ་དེ་དག་ཐམས་ཅད་ལ་ཡང་ཐལ་བ་བསལ་བའི་ཕྱིར་བླངས་པ་ལས་འདས་པ་ལ་ཞེས་གསུངས་སོ། །

[Block 3473]
དེའི་ཕྱོགས་དང་མཐུན་པ་ལ་ནི་ཡིད་ཀྱིའོ་ཞེས་བྱ་བ་ནི་བསྙེན་པར་མ་རྫོགས་ཤིང་རབ་ཏུ་བྱུང་བ་བླངས་པའི་ཕྱོགས་དང་མཐུན་པའི་ལྟུང་བྱེད་རྣམས་གང་ཡིན་པ་མ་བླངས་ཀྱང་བླངས་པའི་ཕྱོགས་ལ་བརྟེན་པ་སྟེ། དེ་དག་ལས་འདས་ཤིང་འགལ་བར་བྱས་པ་ནི་ཡིད་ཀྱི་ཉེས་བྱས་སུ་འགྱུར་ཏེ། བསྡམ་པར་བྱ་བའི་ཉེས་བྱས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3474]
དེའི་ཕྱོགས་དང་མཐུན་པ་དག་གང་ཞེ་ན། དེ་བསྟན་པའི་ཕྱིར་དགེ་སློབ་མའི་ནི།

[Block 3475 [VERSE]]
འཆང་བ་དང་ནི་འབྲལ་བ་དང་། །
མེ་ལ་རེག་དང༌[^2266]སྤངས་པ་དང་། །
ཟས་དང་ས་བོན་འཇིག་པ༌[^2267]དང་། །
རྩྭ་སྔོན་ཡོད་པའི་ས་ཕྱོགས་སུ། །

[Block 3476 [VERSE]]
མི་གཙང་འདོར་དང་ཤིང་འཛེག་དང་། །
བླངས་པ་མདོར་གཏོགས༌[^2268]དགེ་སློབ་མའི། །
དགེ་ཚུལ་གཉིས་ཀྱིས༌[^2269]རིན་ཆེན་རེག །
སོག་འཇོག༌[^2270]བྱས་པ༌[^2271]ཟ་བ་དང་། །

[Block 3477 [VERSE]]
བྱིན་ལེན་མ་བྱས་ས་བརྐོ་དང་། །
སྐྱེ་བ་འཇིག༌[^2272]དང་བཅས་པ༌[^2273]དང་། །
མདོར་གཏོགས་པ་ནི་མ་གཏོགས་པར། །
དབྱར་གནས་གཅིག་ཏུ་གནས་པ་དང་། །

[Block 3478 [VERSE]]
གསོ་སྦྱོང་དགག་དབྱེ་བཅས་པ་དང་། །
དེ་ལ་སོགས་པ་དེ་ཡིས་ནི། །
བླངས་པའི་ཕྱོགས་དང་མཐུན་པ་ཡིན། །
རྟགས་དང་སློང་དང་སྣོད་དང་ནི། །

[Block 3479 [VERSE]]
ལོངས་སྤྱོད་འཕྱར་གཡེང་འདོད་པ་དང་། །
གནོད་པ་དང་ནི་གནས་པ་དང་། །
མི་གུས་མི་སྦྱོང་གཞི་ལས་བྱུང་། །

[Block 3480]
ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 3481]
དེ་ལ་འཆང་བ་ཞེས་བྱ་བ་ནི་ཆོས་གོས་དང་། ལྷུང་བཟེད་ལྷག་མ་འཆང་བའོ། །

[Block 3482]
འབྲལ་བ་ཞེས་བྱ་བ་ནི་ཆོས་གོས་དང་འབྲལ༌[^2274]བའོ། །

[Block 3483]
མེ་ལ་རེག་པ་ཞེས་བྱ་བ་ནི་མེ་འབུད་པ་ལ་སོགས་པ་དང་འབྲེལ་པའོ། །

[Block 3484]
སྤངས་པ་ཟ་བ་ཞེས་བྱ་བ་ནི་ཟས་སྤངས་པ་ཟ་བའོ། །

[Block 3485]
ས་བོན་གྱི་ཚོགས་འཇིག་པ་ཞེས་བྱ་བ་ནི། རུང་བར་མ་བྱས་པའི་ས་བོན་གྱི༌[^2275]ཚོགས་འཇིག༌[^2276]པའོ། །

[Block 3486]
རྩྭ་སྔོན་པོའི་ཕྱོགས་སུ་མི་གཙང་བ་འདོར་བ་ཞེས་བྱ་བ་ནི། རྩྭ་སྔོན་པོ་ཡོད་པའི་ས་ཕྱོགས་སུ་བཤང་བ་ལ་སོགས་པ་འདོར་བའོ། །

[Block 3487]
ཤིང་ལ་འཛེག་པ་ཞེས་བྱ་བ་ནི་ཤིང་ལ་མི་གང་ཙམ་ལས་མཐོར་འཛེག་པའོ་ཞེས་བྱ་བ་འདི་ནི་བསླབ་པ་རྣམས་སོ། །

[Block 3488]
བསླབ་པ་མདོར་གཏོགས་ཞེས་བྱ་བ་ནི་དགེ་སློབ་མ་དོར་ནས་སོ། །

[Block 3489]
མདོར་གཏོགས་པ་ནི་དགེ་ཚུལ་དང་དགེ་ཚུལ་མ་དག་གིས་ས་ལེ་སྦྲམ་ལ་སོགས་པ་འཆང་བའོ། །

[Block 3490]
སོག་འཇོག༌[^2277]བྱས་པ་ཟ་བ་ཞེས་བྱ་བ་ནི་ཉེ་བར༌[^2278]གནས་པའོ། །

[Block 3491]
བྱིན་ལེན་མ་བྱས་པ་ཞེས་བྱ་བ་ནི་གཞན་གྱིས་བྱིན་ལེན་མ་བྱས་པའི་ཟས་ཟ་བའོ། །

[Block 3492]
ས་རྐོ་བ་ཞེས་བྱ་བ་ནི་ས་རྐོ་བའམ་རྐོར་འཇུག་པའོ། །

[Block 3493]
སྐྱེ་བའི་ཚོགས་འཇིག་པ་ཞེས་བྱ་བ་ནི་ཤིང་ལྗོན་པ་ལ་སོགས་པ་གཅོད་པའོ། །

[Block 3494]
བཅས་པ་ནི་འདི་དང་བཅས་པའོ། །

[Block 3495]
བླངས་པ་ནི་དགེ་ཚུལ་དང་དགེ་ཚུལ་མ་དང་། དགེ་སློང༌[^2279]མ་འདི་རྣམས་ཀྱིས་ཡང་དག་པར་བླངས་པའོ། །

[Block 3496]
མདོར་གཏོགས་པ་ཞེས་བྱ་བ་ནི། དགེ་སློང་དང་དགེ་སློང་མའི་སོ་སོར་ཐར་པའི་མདོ༌[^2280]དག་ལས་འདོན་པ་དོར་ནས་ལྷག་མ་སོ་སོར་ཐར་པའི་མདོ་ལས་གཏོགས་པའོ། །

[Block 3497]
དབྱར་གནས་ཞེས་བྱ་བ་ནི་དབྱར་གནས་པར་ཁས་བླངས་པའོ། །

[Block 3498]
གསོ་སྦྱོང་ལ་སོགས་པ་ཞེས་བྱ་བ་ནི་གསོ་སྦྱོང་དང་དགག་དབྱེ་ལ་སོགས་པའོ། །

[Block 3499]
དེ་ལ་སོགས་པ་དེ་ཡི་ནི་ཞེས་བྱ་བ་ནི་རབ་ཏུ་བྱུང་བ་བསྙེན་པར་མ་རྫོགས་པ་ལ་བླངས་པའི་ཕྱོགས་དང་མཐུན་པར་རིག་པར་བྱའོ། །

[Block 3500]
གང་ཞིག་དེ་དག་ལས་འདའ་བར་བྱེད་པ་ལ་ཡིད་ཀྱི་ཉེས་བྱས་སོ། །

[Block 3501]
འདིར་རྣམ་པ་གང་གིས་དེ་རྣམས་ནི་སོགས་པའི་སྒྲས་འཕངས་པའོ། །

[Block 3502]
དེ་བསྟན་པའི་དོན་དུ་འདིར་རྟགས་ལ་སོགས་པའི་གཞི་བརྗོད་པའོ། །

[Block 3503]
འདིར་གཞིའི་སྒྲ་ནི་རེ་རེ་ཞིང་སྦྱར་བར་བྱའོ། །

[Block 3504]
རྟགས་ཀྱི་གཞི་ལས་བྱུང་བ་དང་། སློང་བའི་གཞི་ལས་བྱུང་བ་དང་། སྣོད་ཀྱི་གཞི་ལས་བྱུང་བ་དང་། འཕྱར་གཡེངས་ཀྱི་གཞི་ལས་བྱུང་བ་དང་། འདོད་པའི་གཞི་ལས་བྱུང་བ་དང་། གནོད་པའི་གཞི་ལས་བྱུང་བ་དང་། མི་གུས་པའི་གཞི་ལས་བྱུང་བ་དང་། མི་སྦྱང་བའི༌[^2281]གཞི་ལས་བྱུང་བའོ། །

[Block 3505]
དེ་ལ་རབ་ཏུ་བྱུང་བའི་རྟགས་ཡང་དག་པར་ལེན་ཏོ་ཞེས་སྨོས་པའི་ཚིག་གང་ཡིན་པ་དེ་ནི་རེ་ཞིག་བླངས་པ་ཡིན་པ་དང་། [^2282]དེའི་ཕྱིར་མུ་སྟེགས་ཅན་གྱི་རྟགས་འཆང་བ་ལ་ནི་ཇི་ལྟར་ཁྱིམ་པའི་རྟགས་འཆང་བ་བཞིན་དུ་རབ་ཏུ་བྱུང་བའི་རྟགས་ཡང་དག་པར་བླངས་པ་ལས་འདས་པ་ཡིན་པས་དེ་ལ་ནི་བཤགས་པར་བྱ་བའི་ཉེས་བྱས་སུ་འགྱུར་རོ། །
--- END BLOCKS ---
