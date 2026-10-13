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
[Block 246 [HEADING]]
###### **ཆགས་ཅན་ལྟ་བུ།** ^1-1-5-2-1-2-1-2-1-3-2-0

[Block 247]
དེ་ལ་ཆགས་ཅན་ལྟ་བུ་ནི་གཉུག་མའི་ལུས་ཏེ་དེ་ཡང་ལུས་ཞེས་པ་ནི་གཉུག་མ་དེ་ཉིད་ལའོ། །ཡེ་ཤེས་ཆེན་པོ་ནི་ཟག་པ་མེད་པའི་ཡེ་ཤེས་སོ། །གནས་ཞེས་པ་ནི་ཞུ་བ་བསྡུས་པས་རྟག་པ་མི་འགྱུར་བར་གནས་པ་ཉིད་དོ། །རྟོག་པ་ཐམས་ཅད་ཡང་དག་སྤངས། །ཞེས་པ་ནི་ཕྱག་རྒྱ་ཆེན་པོ་མཚོན་བྱེད་རང་རིག༌[^150]སྟེ། རྟོག་པ་རང་ཤུགས་སུ་གཅོད་པ་དང་མི་རྟོག་པ་རང་རྣལ་དུ་འཇུག་པའོ། །དངོས་པོ་ཀུན་ལ་ཁྱབ་ཅེས་པ་ནི་དབང་པོ་རང་སྣང་ལ་སྦྱར་བའམ། མཚོན་བྱ་ལྷན་སྐྱེས་སོ། །ལུས་གནས་ལུས་ལས་མ་སྐྱེས་པ་ནི་གཉུག་མའི་ལུས་ལ་གནས་ཀྱང་ཐ་མལ་གྱི་ལུས་ལས༌[^151]མ་སྐྱེས་པའམ།[^152] གསལ་བྱེད་ཀྱི་རྒྱུ་ཡིན་གྱི་སྐྱེད་བྱེད་ཀྱི་རྒྱུ་མ་ཡིན་པའོ། །

[Block 248 [HEADING]]
###### **འབྲས་བུ་ལམ་དུ་བྱས་པ།** ^1-1-5-2-1-2-1-2-2-0

[Block 249]
འབྲས་བུ༌[^153]ལམ་དུ་བྱས་པ་ནི་སྐུ་བཞི་སྟེ། ཚིག་དང་པོ་ལོངས་སྐུའོ། །ཚིག་གཉིས་པ་ནི་ཆོས་སྐུའོ། །གསུམ་པ་སྤྲུལ་སྐུའོ། །བཞི་པ་ནི་བདེ་བ་ཆེན་པོའི་སྐུའོ། །

[Block 250 [HEADING]]
###### **རྟེན་རྡོ་རྗེའི་ལུས་ལམ་དུ་བྱེད་པ།** ^1-1-5-2-1-2-2-0

[Block 251]
རྟེན་རྡོ་རྗེའི་ལུས་བསྟན་པ་ནི་ལུས་ལ་ཞེས་པ་ལ་སོགས་པ་སྟེ། རྡོ་རྗེ་སྙིང་པོས་གསོལ་པ་ཞེས་པ། ཀྱེ༌[^154]རྡོ་རྗེའི་ལུས་ལ་རྩ་དུ་ལགས། ཞེས་པ་ནི་དགྱེས་པའི་རྡོ་རྗེར་འབྲེལ་ལོ། །ཀུན་བརྟགས་ཀྱི་ལུས་ལ་ཀུན་བརྟགས་ཀྱི་རྩ་དུ་མཆིས་པ་དང་། གཞན་དབང་གི་ལུས་ལ་གཞན་དབང་གི་རྩ་དུ་མཆིས་པ་དང་། ཡོངས་གྲུབ་ཀྱི་ལུས་ལ་ཡོངས་གྲུབ་ཀྱི་རྩ་དུ་མཆིས་ཞེས་དགོངས་པའོ། །ལན་དུ་རྩ་སུམ་ཅུ་རྩ་གཉིས་ཏེ་ཕྱིར་ལེན༌[^155]བཏབ་སྟེ་ཀུན་བརྟགས་ཀྱི་ལུས་ལ་རྩ་སུམ་ཅུ་རྩ་གཉིས་གང་ཞེ་ན། མི་ཕྱེད་མ༌[^156]ཞེས་བྱ་བ་ལ་སོགས་པ་བྱང་ཆུབ་ཀྱི་སེམས་སུམ་ཅུ་རྩ་གཉིས་འབབ་པའོ་ཞེས་བྱ་བར་སྦྱར་ཏེ་རྣལ་འབྱོར་གྱི་ཀུན་རྫོབ་བོ། །ཀུན་བརྟགས་ཀྱི་ལུས་ལ་ཡང་སུམ་ཅུ་རྩ་གཉིས་ཏེ། ཡང་མི་ཕྱེད་མ་དང་ཕྲ་གཟུགས་མ༌[^157]ལ་སོགས་པ་སྟེ། ཁམས་དང་ཉེ་བའི་ཁམས་བསྐྱེད་པའོ། །

[Block 252 [HEADING]]
###### **རྣམ་པར་གཞག་པ།** ^1-1-5-2-1-2-2-1-0

[Block 253]
དེ་ལ་རྣམ་པར་གཞག་པའི་ནི་གྲངས་དང་ལས་དང་སོ་སོའི་མཚན་ཉིད་དང་གནས་དང་། གཙོ་བོ་དང་། ཕལ་བར་དབྱེ་བའོ། །

[Block 254 [HEADING]]
###### **གྲངས།** ^1-1-5-2-1-2-2-1-1-0

[Block 255]
དེ་ལ་གྲངས་ནི་སུམ་ཅུ་རྩ་གཉིས་ཏེ། མི་ཕྱེད་མ་དང་ཕྲ་གཟུགས་མ་ལ་སོགས་པའོ། །

[Block 256 [HEADING]]
###### **ལས།** ^1-1-5-2-1-2-2-1-2-0

[Block 257 [VERSE]]
ལས་ནི་དྲང༌[^158]ངེས་པའི་རྒྱུ་མཚན་ཏེ།
བྱང་ཆུབ་ཀྱི་སེམས་འབབ་པའི་ཕྱིར་རོ། །

[Block 258 [HEADING]]
###### **སོ་སོའི་མཚན་ཉིད།** ^1-1-5-2-1-2-2-1-3-0

[Block 259]
སོ་སོའི་མཚན་ཉིད་ནི་ཐབས་དང་ཤེས་རབ་ལ་སོགས་པའི་མཚན་ཉིད་འཛིན་པའོ། །

[Block 260 [HEADING]]
###### **གནས།** ^1-1-5-2-1-2-2-1-4-0

[Block 261]
གནས་ནི་གཡས་དང་གཡོན་ལ་སོགས་པའོ། །བརྐྱང༌[^159]མི་མོ་བསྐྱོད་པ་འབབ་པ་སྟེ། སྐྱེས་པ་ལ་གཡོན་ན་གནས་ཏེ།མགྲིན་པར་གནས་ནས༌[^160]བཤང་ལམ་དུ་སེལ་བའོ། །རོ་མ་དེ་བཞིན་ཁྲག་འབབ་ཅིང་། །གཡས་ན་གནས་ཏེ་ལྟེ་བ་ལས་མགྲིན་པར་སེལ་བའོ། བུད་མེད་རྣམས་ལ་ནི་གོ་བཟློག༌[^161]ཤེས་པར་བྱའོ། །ཡོངས་གྲུབ་ཀྱི་རྩ་སུམ་ཅུ་རྩ་གཉིས་ནི་བཅོམ་ལྡན་འདས་རྩ་སུམ་ཅུ་རྩ་གཉིས་པོ་འདི་རྣམས་ཇི་ལྟ་བུ་ལགས་ཞེས་པ་ལ་སོགས་པ་སྟེ། རྩ་སུམ་ཅུ་རྩ་གཉིས་པོ་འདི་རྣམས་ཀྱི་སྤྱིའི་རང་བཞིན་ནམ་མཚན་ཉིད་ཇི་ལྟ་བུ་ལགས་ཞེས་དགོངས་པའོ། །དེ་རྣམས་ཀྱི་རང་བཞིན་ཡང༌[^162]སྲིད་གསུམ་ཡོངས་གྱུར་ནི་རྩ་འདི་གསུམ་དུ་གྱུར་པ་སྟེ། དེ་གཟུང་བ་དང་། འཛིན་པ་རྣམ་པར་སྤངས་ཞེས་པ་ཆོས་ཐམས་ཅད་སྟོང་པར་ཤེས་པའོ། །ཡང་ན་ཐབས་ནི༌[^163]ཐམས་ཅད་ཀྱིས།[^164] །དངོས་པོའི་མཚན་ཉིད་དུ་ནི་བརྟག །ཅེས་པ་ཐབས་རྣམ་པ་སྣ་ཚོགས་སུ་སྣང་བའོ། །

[Block 262 [HEADING]]
###### **གཙོ་བོ་དང་ཕལ་པར་དབྱེ་བ།** ^1-1-5-2-1-2-2-1-5-0

[Block 263]
གཙོ་བོ་དང་ཕལ་པར་དབྱེ་བ་ནི་གསུམ་དུ་གཞག་གོ། །དེ་ཡང་སེམས་ཅན་རེ་རེ་ལ་རྩ་བྱེ་བ་ཕྱེད་དང་བཅུ་དང་སྟོང་ཕྲག་བདུན་ཅུ་གཉིས་སུ་བསྡུས་ཏེ། དེ་ཡང་བརྒྱ་ཉི་ཤུར་བསྡུས།[^165] དེ་ཡང་སུམ་ཅུ་རྩ་གཉིས་སུ་བསྡུས་ཏེ་རྣལ་འབྱོར་མ་བཅོ་ལྔར་ཤེས་པར་བྱའོ། །

[Block 264]
དེ་ཡང་།

[Block 265 [VERSE]]
རྩ་རྣམས་བྱེ་བ་ཕྱེད་དང་བཅུ། །
ལུས་ཀྱི་ལྟེ་བའི་པདྨར་གནས། །
འཁོར་ལོ་བཞི་ཡི་གྲངས་ཀྱིས་ནི། །
བརྒྱ་དང་ཉི་ཤུ་ལྷག་པ་ཡིན། །

[Block 266 [VERSE]]
བྱང་སེམས་སུམ་ཅུ་རྩ་གཉིས་ཀྱི། །
རྩ་མཆོག་སུམ་ཅུ་རྩ་གཉིས་སོ། །

[Block 267]
ཞེས་གསུངས་སོ། །དེ་ནི་རྣམ་པར་གཞག་པའོ། །

[Block 268 [HEADING]]
###### **བཤད་པའི་ཚུལ་རྣམ་པར་སྦྱར་བ།** ^1-1-5-2-1-2-2-2-0

[Block 269]
རང་བཞིན་ནི་བཤད་པའི་ཚུལ་རྣམ་པར་སྦྱར་བ་སྟེ། བཤད་པའི་ཚུལ་སྦྱར་བ་ཡང་ཀུན་ལ་ལྡན་པ་ཡིན་ཡང་། བླ་མའི་མན་ངག་གིས་སྐབས་སོ་སོར་སྦྱར་བ་ནི། ལྗོན་ཤིང་གི་ཡལ་ག་ལྟ་བུར་ཤེས་པར་བྱའོ། །

[Block 270]
དེ་ཡང་བསྐྱེད་པའི་རིམ་པ་དང་། རྫོགས་པའི་རིམ་པའོ། །

[Block 271 [HEADING]]
###### **བསྐྱེད་པའི་རིམ་པ།** ^1-1-5-2-1-2-2-2-1-0

[Block 272]
བསྐྱེད་པའི་རིམ་པ་ནི། སྲིད་གསུམ་ཡོངས་གྱུར་ཐམས་ཅད་ནི། །ཞེས་པ་ནི་ཆོ་གའི་རིམ་པ་ཐ་མལ་གྱི་སྒོ་གསུམ་ཡོངས་སུ་གྱུར་པའོ། །

[Block 273]
གཟུང་དང་འཛིན་པ་རྣམ་པར་སྤངས། །ཞེས་པ་ནི་བདག་མེད་རྣལ་འབྱོར་ལྡན་པའོ། །ཡང་ན་ཐབས་ནི་ཐམས་ཅད་ཀྱི། །ཞེས་པ་ནི་ཡང་ན་ཧེ་རུ་ཀ་དཔལ་མཚོན་པའོ། །དངོས་པོའི་མཚན་ཉིད་དུ་ནི་བརྟག །ཅེས་པ་ནི་ཕུང་པོ་ལ་སོགས་པའི་ཆོས་ཀུན་ཏེ་གཉིས་སྦྱོར་བ་ལས་བྱུང་བའི་ལྷའི་འཁོར་ལོར་བརྟགས་ཤིང་སྣང་བའོ། །

[Block 274 [HEADING]]
###### **རྫོགས་པའི་རིམ་པ།** ^1-1-5-2-1-2-2-2-2-0

[Block 275 [HEADING]]
###### **གཞན་ལུས་ཤེས་རབ་ལ་བརྟེན་པ།** ^1-1-5-2-1-2-2-2-2-1-0

[Block 276]
དེ་ལ་རྫོགས་པའི་རིམ་པ་ཡང་གཞན་ལུས་ཤེས་རབ་ལ་བརྟེན་པ་དང་། རང་ལུས་ཐབས་དང་ལྡན་པ་དང་དབྱེར་མེད་ཕྱག་རྒྱ་ཆེན་པོའོ། །ཤེས་རབ་ལ་བརྟེན་པ་ཡང་། སྲིད་གསུམ་ཡོངས་གྱུར་ཐམས་ཅད་ནི། །ཞེས་པ་ནི་ཤེས་རབ་མའི་གསང་བའི་གནས་ཏེ་རྩ་གསུམ་ཡོངས་སུ་གྱུར་པའི་བྱ་རོག་གི་གདོང་ཅན་ནོ། །

[Block 277]
གཟུང་དང་འཛིན་པ་རྣམ་པར་སྤངས། །ཞེས་པ་ནི་དེའི་ནང་ཁོང་སྟོང་གི་རྣམ་པའོ། །ཡང་ན་ནི་ཨ་ཐ་སྟེ་དེ་ནས་སོ། །ཐམས་ཅད་ནི་ལུས་ཐམས་ཅད་དོ། །ཐབས་ནི་རིན་པོ་ཆེའི་ཟེ་འབྲུའི་བདེ་བ་གནས་པའི་ཐབས་སོ། །དངོས་པོའི་མཚན་ཉིད་དུ་ནི་བརྟག །ཅེས་པ་ནི་དངོས་པོ་ཞུ་བ་དང་མཚན་ཉིད་བདེ་བ་ལྷན་ཅིག་སྐྱེས་པའི་ངོ་བོ་བླ་མའི་མན་ངག་ནི་བསྒོམ་པས་བརྟག་པའོ། །

[Block 278 [HEADING]]
###### **རང་ལུས་ཐབས་དང་ལྡན་པ།** ^1-1-5-2-1-2-2-2-2-2-0

[Block 279]
དེ་ལ་རང་ལུས་ཐབས་དང་ལྡན་པ་ནི་སྲིད་པ་གསུམ་གྱི་རྩ་གསུམ་མོ། །ཡོངས་གྱུར་ནི་སྐྱེ་གནས་གྲུ་གསུམ་མོ། །ཐམས་ཅད་དེ་ལུས་ཀུན་འདུས་པའོ། །གཟུང་དང་འཛིན་པ་རྣམ་པར་སྤང་། །ཞེས་པ་ནི་ནང་ཁོང་སྟོང་ལྟ་བུའམ། ཡང་ན༌[^166]འོག་ན་གནས་པ་ཤེས་རབ་ཀྱི་རང་བཞིན་ཡིན་པས་སོ། །ཨ་ཐ་ནི་ཨ་ཀྲ་སྟེ་དེ་ལའོ། །ཐབས་ནི་བདེ་བ་ཆེན་པོའི་གནས་སོ། །ཐམས་ཅད་ནི་ལུས་ཀུན་ཞུ་བའོ། །དངོས་པོའི་མཚན་ཉིད་དུ་ནི་བརྟག །ཅེས་པ་སྔ་མ་ལྟར་ལྷན་ཅིག་སྐྱེས་པ་བསྒོམ་པའོ། །

[Block 280 [HEADING]]
###### **གཉིས་མེད་ཕྱག་རྒྱ་ཆེན་པོ།** ^1-1-5-2-1-2-2-2-2-3-0

[Block 281]
གཉིས་མེད་ཕྱག་རྒྱ་ཆེན་པོ་ལ་གཉིས་ཏེ། བརྟེན་པ་ཆོས་ལ་འཇུག་པ་དང་། རྟེན་ནང་ནས་འཇུག་པའོ། །

[Block 282 [HEADING]]
###### **བརྟེན་པ་ཆོས་ལ་འཇུག་པ།** ^1-1-5-2-1-2-2-2-2-3-1-0

[Block 283]
བརྟེན་པ་ཆོས་ལ་འཇུག་པ་ནི་ཤེས་རབ་དང་ཐབས་དབྱེར་མེད་པའོ། །དེ་ལ་ཤེས་རབ་ནི་སྲིད་གསུམ་སྟེ་ཁམས་གསུམ་མོ། །ཡོངས་གྱུར་ནི་གཅིག་དང་དུ་མ་དང་བྲལ་བའི་སྦྱོར་བས་རང་བཞིན་མེད་པས་ཐམས་ཅད་ཡོངས་སུ་གྱུར་པའོ། །དེ་ལ་ཤེས་རབ་ཀྱི་ཇི་ལྟར་བལྟ་ཞེ་ན། དེའི་ཕྱིར། གཟུང་དང་འཛིན་པ་རྣམ་པར་སྤང་། །ཞེས་གསུངས་སོ། །དེ་ལ་ཐབས་ཀྱི་ཇི་ལྟར་བལྟ་ཞེ་ན། ཕ་རོལ་ཕྱིན་པའི་ཐེག་པ་ལྟར་གཅིག་དང་དུ་བྲལ་ལ་སོགས་པ་སྦྱོར་བ་ལ་མི་ལྟོས་པས་ཨ་ཐ་བ་སྟེ། རྣམ་གྲངས་སམ་ཐབས་སྣང་བའི་བདག་ཉིད་ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་། ཚད་མེད་པ་ལ་སོགས་པའི་དངོས་པོའི་མཚན་ཉིད་དུ་བརྟག་པའོ། །

[Block 284 [HEADING]]
###### **རྟེན་ནང་ནས་འཇུག་པ།** ^1-1-5-2-1-2-2-2-2-3-2-0

[Block 285]
ཡང་ན། སྲིད་གསུམ་ཡོངས་གྱུར་ཐམས་ཅད་ནི། །ཞེས་པ་ནི་ལུས་ངག་ཡིད་གསུམ་གྱི་ཁམས་གཉུག་མའི་ཨ་ཝ་དྷཱུ་ཏཱི་དེས་བསྡུས་པའོ། །གཟུང་དང་འཛིན་པ་རྣམ་པར་སྤང་།[^167] །ཞེས་པ༌[^168]ནི་དེར་སྐྱེས་པའི་ཡེ་ཤེས་ཀྱི་རྟོག་པ་གཅོད་ཅིང་མི་རྟོག་པ་སྐྱེ་བའོ། །ཐབས་ནི་ཞེས་པ་ནི་བདེ་བའི་རོར་རང་སྣང་བས་མི་རྟོག་པ་རང་རྣལ་དུ་འཇུག་པའོ། །ཐམས་ཅད་ཀྱི་ཞེས་པ་ནི་ཐབས་དང་ཤེས་རབ་དབྱེར་མེད་དོ། །དེ་ལྟ་བུའི་ཡེ་ཤེས་ཆེན་པོ་དེ་གང་དུ་གནས་ཤིང་བརྟེན་ཞེ་ན། དེའི་ཕྱིར། དངོས་པོའི་མཚན་ཉིད་དུ་ནི་བརྟག །ཅེས་པ་སྟེ། དངོས་པོ་ནི་བསྟན་དུ་མེད་ལ་ཐོགས་པ་མེད་པའི་གཟུགས་གཉུག་མའི་དབང་པོའོ། །མཚན་ཉིད་ནི་དེར་གནས་པའི་ཡེ་ཤེས་ཆེན་པོའོ། །དུ་ནི་བརྟག་ཅེས་པ་སྟེ་དབང་པོ་རང་སྣང་བ་དང་ཡེ་ཤེས་རང་འབར་བའི་མན་ངག་གོ། །དེ་རྣམས་ལ་ཆོ་ག་ཁ་བསྐང་བ་སྔ་མ་དང་འདྲའོ། །
--- END BLOCKS ---
