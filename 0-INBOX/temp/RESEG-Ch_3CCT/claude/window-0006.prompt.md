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
[Block 211]
ཞེས་པ་གང་བསམ་གཏན་དང༌[^90]ལྡན་པ་ལས་བྱུང་བའི་བྱང་ཆུབ་སེམས་འཐོར་བ་ལ་སོགས་པའི་ཉེས་པ་དང་བྲལ་བ༌[^91]སྟེ། དེས་ནི་ངག་གི་སྡིག་པ་སྦྱོང་བར་བྱེད་པ་ཉིད་ཀྱི་ནུས་པ་ཡོད་པས་ནུས་པ་ཞེས་བྱ་བ་ནི་འདིར་མ་སྤངས་པའོ། །

[Block 212]
ངེས་པའི་ཚིག་བསྙད་པ་འདི་ཅིའི་ཕྱིར་གསང་བའི་དབང་ཡིན་སྙམ་པ་ལ།

[Block 213 [VERSE]]
གང་ཞིག་གསང་ལ་བྱང་ཆུབ་སེམས། །
ངག་ལ་བསྐུར་བར་བྱེད་ཕྱིར་རོ། །

[Block 214]
ཞེས་པ་ལ་གསང་བར༌[^92]བྱ་བ་ཉིད་དང་། བྱང་ཆུབ་སེམས་ཡིན་པ་ཉིད་དང་། ངག་གི་རྟོག་པ་སྦྱོང་བར་བྱེད་པ་ཉིད་ཀྱི་ཕྱིར་དེ་སྐད་ཅེས་བྱའོ། །

[Block 215]
གསང་བའི་དབང་ཞེས་བྱ་བའང་དུ་ཞིག་ཅེ་ན།

[Block 216 [VERSE]]
ཕྱི་དང་ནང་དང་སྦས་པ་དང་། །
གསང་བའི་དབང་ནི་གསུམ་དུ་ཤེས། །

[Block 217]
ཞེས་པ་ཕྱིའི་གསང་བའི་དབང་ནི་དུང་གི་ནང་དུ་གསང་བའི་བྱང་ཆུབ་སེམས་བསྐུར་བའོ། །

[Block 218]
ནང་གི་གསང་བ་ནི་བེའུ་བཞིན་པའམ་བུང་བ་བཞིན་གྱི་སྦྱོར་བ་བྱང་ཆུབ་སེམས་ལེན་པའོ། །

[Block 219]
སྦས་པའི་གསང་བ་ནི་གཉིས་སུ་མེད་པའི་སྦྱོར་མཚམས་ཀྱི་འོག་གི་ཕྱོགས་ལེན་པར་བྱེད་པའོ། །

[Block 220 [VERSE]]
གང་གིས་ཁ་ཡི་ཐད་ཀར་ནི། །
གཉི་ག་སྦྱོར་བའི་བྱིན་རླབས༌[^93]ལས། །
ཟླ་བ་ཉི་མ་འདྲེས་པ་ཡིས། །

[Block 221]
ཁ་ཡི་བུ་གར་འབྱུང་བར་བྱེད།[^94] ཅེས་པ་འདི་ནི་བར་སྐབས་ཀྱི་ཚིགས་སུ་བཅད་པའོ། །

[Block 222 [VERSE]]
འདིའི་རྣམ་གྲངས་ཀྱང་གང་ཡིན་ཞེ་ན། །
གསང་བ་དང་ནི་སྦས་པ་དང་། །
ཐུན་མོང་མིན་དང་མི་བསྟན་པའི། །
སྦྱོར་བ་འདི་ནི་རྣམ་གྲངས་སོ། །

[Block 223]
ཞེས་པ་ཀུན་ལ་མི་བསྟན་པའི་ཕྱིར་དང་། དེ་རྒྱལ་བ་ཀུན་གྱིས་སྦས་པ་དང་། ཚོགས་ལ་སོགས་པ་དང་ཐུན་མོང་མ་ཡིན་པ་ཉིད་དང་། དེ་དག་ལ་མི་བསྟན་པ་ཉིད་ཀྱིས་འདི་དག་ནི་རྣམ་གྲངས་སུ་ཤེས་པར་བྱའོ། །

[Block 224]
གསང་བའི་དབང་ཞེས་པ་འང་ཆོས་དུ་དང་ལྡན་པ་ཡིན་ཞེ་ན།

[Block 225 [VERSE]]
བྱང་ཆུབ་སེམས་དང་ཏིང་འཛིན་དང་། །
རོ་མྱང་དག་གི་སྡིག་པ་སྦྱོང་།
འདི་ནི་གསང་བའི་དབང་དུ་འདོད། །

[Block 226]
ཅེས་པ་གསང་བའི་དབང་ཞེས་བྱ་བའང་དང་པོར་བྱང་ཆུབ་ཀྱི༌[^95]སེམས་དཀར་དམར་ཡིན་པ་ཉིད་དང་། དེའང་ཏིང་ངེ༌[^96]འཛིན་ཡིན་པ་ཉིད་དང་། སློབ་མའི་ལྕེས་རོ་མྱང་བ་ཉིད་དང་། ངག་གི་སྡིག་པ་སྦྱོང་བ་ཞེས་བྱ་བ༌[^97]འདི་དག་དང་ལྡན་པ་ལ་གསང་བའི་དབང་ཞེས་བཤད་དོ། །

[Block 227]
འདིས་ཅི་ཞིག་བྱེད་ཅེ་ན།

[Block 228 [VERSE]]
གང་ཞིག་གཞན་ལ་ཐལ་འགྱུར་བ། །
འདི་ཡིས་སེལ་བར་བྱེད་པ་ཡིན། །
ཞེས་པ་འདི་ནི་གང་ཞིག་གིས། །
གང་ཞིག་ཐལ་བར་བྱེད་པའོ། །

[Block 229]
འོ་ན་གཅིག་གིས་འགྱུར་མོད༌[^98]ཅེ་ན། ངག་གི་སྡིག་པ་སྦྱོང་བ་ནི་བཟླས་པས་ཀྱང་འགྱུར་བས་བྱང་ཆུབ༌[^99]སེམས་ཡིན་ནོ། །

[Block 230]
གཞན་ཡང་བྱང་ཆུབ་སེམས་ཞེས་བྱ་བ༌[^100]ལས་གཞན་མ་སྨོས་ན། ཐ་མལ་པའི་བྱང་ཆུབ་སེམས་ཀྱིས་ཀྱང་འགྱུར་བས་དེ་བསལ་བའི་ཕྱིར་ཏིང་ངེ་འཛིན་ནོ། །

[Block 231]
གཞན་ལའང་ཅི་རིགས་སུ་སྦྱར༌[^101]རོ། །

[Block 232]
གསང་བ་ཞེས་བྱ་བ་འདིའི་སློབ་དཔོན་ཡང་གང་ཞིག་ཡིན་ཞེ་ན།

[Block 233 [VERSE]]
གང་ཞིག་དབབ༌[^102]དང་བཟློག་ཤེས་དང་། །
རིག་མ་ཡོན་ཏན་ལྡན་པ་དབུལ། །

[Block 234]
ཞེས་པ་སློབ་དཔོན་ཞེས་སྦྱར་རོ། །

[Block 235]
གང་ཞིག་བྱང་ཆུབ་སེམས་དབབ་པ་དང་བཟློག་པ་ཤེས་པ་དང་། རིག་མ་རྟོག་པའི་སྦྱོར་བ་ལ་མཁས་པ་རིག་མའང་ཡོན་ཏན་དང་ལྡན་པ་སྟེ། འདི་དག་ཀྱང་འབྲས་བུ་བདེ་བ་སྟེར་བའི་ཕྱིར་སློབ་དཔོན་ཞེའོ། །

[Block 236]
སློབ་དཔོན་དེས་ཀྱང་སློབ་མ་ཇི་ལྟ་བུ་ལ་བསྐུར་ཞེ་ན།

[Block 237 [VERSE]]
བུམ་པའི་དབང་རྫོགས་རྟོག་པ༌[^103]ཆུང་། །
གསང་ལ་དད་པས་གཞན་ལ་མིན། །

[Block 238]
ཞེས་པ་དང་པོར་སློབ་དཔོན་ལས༌[^104]ལེགས་པར་སྦྱངས་པའི༌[^105]བུམ་པའི་དབང་ཐོབ་པ་དང་། རྫས་ལ་སོགས་པ་ལ་རྟོག་པ༌[^106]ཆུང་ཞིང་དངོས་སུ་འཇུག་ནུས་པ་དང་། གསང་བའི་དོན་ལ་མི་སྐྲག་མི་དངངས་ཤིང་ཤིན་ཏུ་དད་པ་དང་། གཞན་ཡང་སྐད་སྙན་པ་དང་། བདེན་པར་སྨྲ་བ་དང་། ཚོད་རིག་པ་དང་། ལུས་ངག་གཟོབ་པ་འོང༌[^107]ངོ་། །དེ་ལ་དབང་བསྐུར་བའི་རྒྱུ་ཅི་ཞེ་ན།

[Block 239 [VERSE]]
གཉི་གའི་སྦྱོར་བ་ལས་བྱུང་བའི། །
ཤེས་རབ་ཏིང་འཛིན་འདི་ཁོ་ན། །

[Block 240]
ཞེས་པ་གསང་བའི་དབང་བསྐུར་བའི་རྒྱུའང་སློབ་དཔོན་དང་ཕྱག་རྒྱ་མའི་ཤེས་རབ་དང་ཏིང་ངེ་འཛིན་ཏེ་འདིས་དབང་ལ་ཕན་པར་བྱེད་པ་དང་། མེད་ན་མི་འབྱུང་བའི་ཕྱིར་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 241]
འོ་ན་འདི་དུས་གང་གི་དུས་སུ་བསྐུར་ཞེ་ན།

[Block 242 [VERSE]]
སློབ་དཔོན་གཉིས་ཡོད་གནང་བ་དང་། །
རྫས་རྣམས་ཕུན་སུམ་ཚོགས་པ་དུས། །

[Block 243]
ཞེས་པ་གསང་བའི་དབང་བསྐུར་བའི་དུས་ནི་དང་པོར་སློབ་དཔོན་ཁྱད་པར་ཅན་དང་། རིག་མ་ཡོན་ཏན་དང་ལྡན་པ་རྙེད་པ་དང་། །དེ་ཉིད་ཀྱིས༌[^108]གནང་བ་བྱིན་པ་དང་། ཁུ་བ་དང་རཀྟ་རྒྱས་ཤིང་འབབ་པ་དང་། རང་གི་ཡོན་ཏན་དང་རྫས་དང་གཟུགས་ལ་སོགས་པ་ཕུན་སུམ་ཚོགས་པའི་དུས་སོ། །

[Block 244]
འོ་ན་གསང་བའི་དབང་གི་གླེང་གཞི་ཞེས་བྱ་བའང་གང་ཡིན་ཞེ་ན།

[Block 245 [VERSE]]
གང་ཚེ་རྩ་བའི་རྒྱུད་དག་ཏུ། །
བདུད་རྩིའི་རོ་ལ་བརྒྱལ་བསླང་བའོ། །

[Block 246]
ཞེས་པ་རྩ་བའི་རྒྱུད་གསང་བ་འདུས་པ་ཞེས་བྱ་བ་རྣལ་འབྱོར་ཆེན་པོའི་རྒྱུད་ཀྱི་དཀྱིལ་འཁོར་དུ་དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱིས༌[^109]བདུད་རྩི་ལྔ་ལ་དངོས་སུ་སྤྱད་པའི་སྟོབས་ཀྱིས་འཁོར་བ༌[^110]ན་གནས་པའི་བྱང་ཆུབ་སེམས་དཔའ་དང་། ཉན་ཐོས༌[^111]འདོད་ཆགས་དང་བྲལ་བ་རྣམས་ཤིན་ཏུ་སྐྲག་པའི་སྟོབས་ཀྱིས༌[^112]དངངས་པ་དང་ངུས་པ་དང་བརྒྱལ་བ་ལ། མི་བསྐྱོད་པ་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོས་བསླངས༌[^113]ནས་དེ་དག་གི༌[^114]དོན་བསྟན་པ་འདི་ནི་བྱང་ཆུབ་སེམས་དཔའི་གསང་བའི་དབང་གི་གླེང་གཞིའོ། །

[Block 247]
[^115]དེ་ལ་གསང་བའི་དབང་གི་རྫས་གང་ལ་བྱ༌[^116]ཞེ་ན།

[Block 248 [VERSE]]
རྫས་ནི་དཀར་དམར་བཅུ་ཕྱེད་ལྡན། །
གང་དུ་འདི་ཡི་སྦྱོར་བ་བྱེད། །

[Block 249]
ཅེས་པ་ནི་བྱང་ཆུབ་ཀྱི༌[^117]སེམས་དཀར་དམར་དང་། དེ་ལས་གཞན་པའི༌[^118]དྲི་ཆེན་དང་། དྲི་ཆུ་དང་། ཤ་ཆེན་དང་། ཤེལ་ལ་སོགས་པ་འདི་དག་ནི་རྫས་ཏེ། འདི་ལ་བརྟེན་ནས་ངག་གི་རྣམ་པར་རྟོག་པ་ལྡོག་པར་བྱེད་དོ། །

[Block 250]
དེ་ཡང་གནས་གང་དུ་བསྐུར་ཞེ་ན།
--- END BLOCKS ---
