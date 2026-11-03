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
[Block 3536]
ཆོས་གྲོགས་བྱེད་ཅེས་བྱ་བ་ནི་བདེན་པའི་ཆུང་མའོ། །

[Block 3537]
བུད་མེད་སྤངས་པའི་རྒྱུ་གཞན་ཡང་ཡོད་དེ་སྔོན་ལས་ངན་པ་བྱས་པའི་རྒྱུ་དང་ལྡན་པ་ཡིན་ཏེ། དེས་ན་ཡིད་ལ་སྙིང་རྗེ་ཅུང་ཟད་མེད། །ཅེས་བྱ་བའི་ཚིགས་བཅད་བརྩམས་སོ། །

[Block 3538]
དེ་ཡོངས་སུ་བཏང་བ་དང་མཐུན་པ་ཉིད་ནི་བཏང་ཞིང་སྙང་རྗེ་སྤངས་པའི་ཕྱིར་ཏེ། འདིས༌[^2273]ནི་ཆོས་དང་མི་ལྡན་པར་སྟོན་ཏེ།

[Block 3539 [VERSE]]
སྙིང་རྗེ་ཅུང་ཟད་མེད་ཅེས་བྱ་བས་སོ། །
ཀྱེ་མའོ་ཆོས་ནི་ཅུང་ཟད་འགྲུབ་རེ༌[^2274]སྐན། །

[Block 3540]
ཞེས་བྱ་བ་ནི་སྐྱེ་བོ་སྙིང་ཉེ་བ་སྤངས་པའི་ཕྱིར་རོ། །

[Block 3541]
ཁྱིམ་ཐབ་རབ་ཏུ་བྱུང་བའི་སྨྲེ་སྔགས་འདོན་པ་གང་ཡིན་པ་དེ་ནི་དེས་སྨྲེ་སྔགས་འདོན་པའོ། །

[Block 3542]
བདེ་བ་དང་སྡུག་བསྔལ་མཚུངས་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཀྱི་བདེ་བ་སྤྱོད་པ་ནི་བདེ་བའི་རིམ་པའོ། །

[Block 3543]
སྡུག་བསྔལ་སྤྱོད་པ་ནི་སྡུག་བསྔལ་ཀྱི་རིམ་པའོ། །

[Block 3544]
ཐོས་ནས་ནི་སྐྱེ་བོ་འདི་དག་གང་ཞིག་ནས་ཞེས་བྱ་བ་ནི་གང་ལས་རབ་ཏུ་འབྱུང་ངོ་ཞེས་དེ་ཐོས་པའོ། །

[Block 3545]
དེ་ཐོས་ནས་བྱམས་པའི་དབང་གིས་དེར་ལྷགས་ཏེ། ཞེས་བྱ་བ་ནི་ཆོ་ངེས་འདེབས་པར་གྱུར་པའོ། །

[Block 3546]
ངོ་ཚ་ཞིང་མི་དགའ་བར་གྱུར་པ་གང་ཡིན་པ་དེ་ནི་ངོ་ཚ་ཞིང་མི་དགའ་བར་གྱུར་པའོ། །

[Block 3547]
ངོ་ཚ་ན༌[^2275]ནི་ཡོན་ཏན་དམ་པ་སྟེ། དམ་པ་དེ་ཡོད་པ་དང་། མི་དགའ་བ་ནི་རང་གི་ཁྱིམ་ཡོངས་སུ་སྤང་བར་འདོད་པ་སྟེ། དེ་གཉིས་ཀ་བསྒྲུབ་པའི་ཕྱིར། སྐྱེ་བོ་རྣམས་ཀྱི་ཡོན་ཏན་དུ་ཞེས་བྱ་བ་དང་། དེ་ལྟར་བདག་ནི་སྐྱོན་ལ་དད་གྱུར་ཅིང་། །ཞེས་བྱ་བའི་ཚིགས་བཅད་གཉིས་ཀྱིས་བསྟན་ཏོ། །

[Block 3548]
དེ་ལ་སྐྱེ་བོ་རྣམས་ཀྱི༌[^2276]ཡོན་ཏན་དུ་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཀྱིས་ནི་ངོ་ཚ་ཞིང་ཞེས་བྱ་བ་དེ་ཉིད་བསྒྲུབ་པ་ཡིན་ཏེ། བདག་ལྟ་མིར་ཡང་ག་ལ་རུང་། །ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 3549]
དེ་ལྟར་བདག་ནི་སྐྱོན་ལ་དད་གྱུར་ཅིང་། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཀྱིས་ནི་མི་དགའ་བར་གྱུར་པ་དེ་ཉིད་བསྒྲུབ་པ་ཡིན་ཏེ། དེ་ལྟར་བདག་ནི་ཞེས་བྱ་བ་ནི་ཁྱིམ་ལ་མངོན་པར་ཕྱོགས་པ་ཉིད་དུ་སྟེ། ཡོན་ཏན་ཁྱད་དུ་གསོད་ལ་ཚུལ་ངན་པས་ཡོན་ཏན་གྱི་བསྔགས་པ་བརྗོད་པ་ལས་འཇུག་པའི་བྱ་བས་ལེགས་པར་མ་བསྐྱེད་པའི་ཕྱིར། བརྩི་བར་འགྱུར་ཞེས་བྱ་བ་ཡིན་ཏེ། སྐྱོན་ལ་དད་པར་གྱུར་ཅིང་ཡོན་ཏན་ལ་ནི་ཁྱད་དུ་གསོད་ལ་ཚུལ་ངན་པར་གྱུར་པ་འདི་གཉིས་ཀྱིས་སོ། །

[Block 3550]
དེ་ལྟར་གྱུར་ན་ཞེས་བྱ་བ་ནི་སྐྱེ་བོ་དགེ་བ་ཡང་བརྩི་བར་གྱུར་ན་གསོན་ཡང་ཅི་ཞིག་རུང་ཞེས་བྱ་བ་འདིས་ནི་མི་དགའ་བ་ཉིད༌[^2277]བསྟན་ཏོ། །

[Block 3551]
དེ་བས་སྐྱེ་བོ་རེ་བར་གྱུར་པ་ཞེས་བྱ་བའི་ཚིགས་བཅད་ནི་ཁྱིམ་ལ་མངོན་པར་ཕྱོགས་པའི་ཉེས་དམིགས་བསྟན་པ་དང་། དེ་དང་མི་མཐུན་ནགས་ན་གནས་པའི་དབང་དུ་བྱས་པ་སྟེ། རེ་བ་ནི་ཡོན་ཏན་ལ་རེ་བར་གྱུར་པའོ། །

[Block 3552]
དེ་བས་ན་ཞེས་བྱ་བ་ནི་ཁྱིམ་ལ་མངོན་པར་ཕྱོགས་ན་ནི་མིར་མི་རུང་བའི་ཕྱིར་རོ། །

[Block 3553]
སྐྱེ་བོ་དགེ་བས་ཡང་དག་པར་བརྩི་བར་འགྱུར་ཏེ། དེའི་འཚོ་བ་ནི་དགོས་པ་ཅི་ཡང་མེད་པའི་ཕྱིར་རོ། །

[Block 3554]
ཡོན་ཏན་ཉམས་སུ་བླངས་ཏེ་བསྐང་། །ཞེས་བྱ་བ་ནི་བསྒྲུབ་ཅིང་འབད་པས་རེ་བ་ཡོངས་སུ་བསྐང་བར་བྱ་སྟེ་ཉམས་སུ་བླངས་པས་སོ། །

[Block 3555]
ཕན་ཡོན་གྱི་དབང་དུ་བྱས་ནས།

[Block 3556 [VERSE]]
སྤྱོད་པ་ངན་པའི་ཉོན་མོངས་ཁྱིམ་སྤངས་ནས། །
དཀའ་ཐུབ་ནགས་ན་དགའ་བའི་ཡོན་ཏན་གྱིས། །

[Block 3557]
ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 3558]
ནོར་དང་ཐབས་ཞེས་བྱ་བ་འདིས་ནི་གཞུང་ལུགས་བསྟན་ཏེ། ནོར་གྱི༌[^2278]བསྡུ་བའམ་དབྱེ་བ་གཉིས་ཀྱིས་སོ། །

[Block 3559]
མཐུ་རྩལ་གང་དག་གིས་ཞེས་བྱ་བ་ནི་བཀའ་ཁྲིམས་ཀྱི་ཚུལ་གྱིས་སོ། །

[Block 3560]
རེ་ཞིག་ཚིགས་བཅད་དེས་ནི་རྒྱལ་པོ་གཞན་ལས་སྐྱེ་བའི་སྡུག་བསྔལ་གྱི་དབང་དུ་བྱས་པའོ། །

[Block 3561]
ད་ནི་རང་གི་ཡུལ་འཁོར་གྱི་དབང་དུ་བྱས་ནས། གལ་ཏེ་ནོར་འདོད༌[^2279]ཅེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ཏེ། ནོར་མ་ཚང་བའམ། གནོད་པ་ཐོབ༌[^2280]པས་རང་གི་ཡུལ་ལས་པས་མཐར་འགྲོ་ཞེས་བྱ་བ་དེའི་དབང་དུ་བྱས་ནས། ཅི་ཞིག་འདོད་ཕྱིར་ཞེས་བྱ་བ་ཡིན་ཏེ་རྒྱུ་གཞན་གང་གིས་སོ། །

[Block 3562]
གལ་ཏེ་ནོར་འདོད་ཅེས་བྱ་བ་དེས་ནི་སྡུག་བསྔལ་ལམ་གནོད་པ་སྟེ། སྔར་བསྟན་པའི་སྡུག་བསྔལ་གང་གིས་ཁྱོད་ནི་བས་མཐར་འགྲོ་ཞེས་བྱ་བ་དེ་གསལ་བ་ཡིན་ནོ། །

[Block 3563]
[^2281]སྐྱེ་བོའི་ཚིག་བསྲུངས་པ་ཙམ་གྱིས་ཞེས་བྱ་བ་ནི་གང་དེ་འཇིག་རྟེན་གྱི་ཚིག་ནི་འཇིག་རྟེན་གྱི༌[^2282]གཏམ་ལ་ཞེན་པའོ། །

[Block 3564]
དེ་ལས་ཞེས་བྱ་བ་ནི་དགེ་བའི་ཆོས་ལས་ཉམས་པར་མི་བགྱི་བ་སྟེ། ཆོས་ཞེས་བྱ་བ་ནི་བདག་ལ་ཕན་པར་འདོད་པ་སྟེ། དེ་ལྟར་བདག་ཉིད་ཀྱི་ཆོས་ལ་ལྟོས་པར༌[^2283]བསྟན་པའོ། །

[Block 3565]
ངོ་ཚའི་ཕྱིར་ཡང་ཞེས་བྱ་བ་ནི་བལྟས་པས༌[^2284]ཀྱང་སྟེ། ངོ་ཚའི་ཕྱིར༌[^2285]ཡང་རབ་ཏུ་འབད་པའི་རིགས། །ཞེས་བྱ་བ་ཡིན་ཏེ། ངོ་ཚའི་ཕྱིར་ཡང་ཆོས་དང་ལྡན་པ་ལ་འབད་པར་བྱ་བའོ།[^2286] །དེའི་ཕན་ཡོན་བསྟན་པའི་ཕྱིར། ཡོན་ཏན་ཡོད་ཅེས་གྲགས་ཤིང་རེ་བ་དག །ཅེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ཏེ། ཡོན་ཏན་འབྱུང་བ་ཡིན་པས་ཡོན་ཏན་ཡོད་ཅེས་པའོ། །

[Block 3566]
ཇི་ལྟར་གྱུར་ཀྱང་རུང་སྟེ་ཞེས་བྱ་བ་ནི་ངོ་ཚ་བའི་ཕྱིར་ཡང་གཏམ་སྙན་འཕེལ་བར་འགྱུར་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། གྲགས་པ་རབ་ཏུ་འགྲུབ་པས་ངོ་ཚའི་ཕྱིར་ཡང་དེ་རབ་ཏུ་འབད་པའི་རིགས་ཏེ། འདི་ལྟར་གྲགས་པས་རབ་ཏུ་འགྱུར་བས་སོ། །

[Block 3567]
གཞན་དུ་བགྱིས་ན་ཞེས་བྱ་བ་ནི་བདག་ཉིད་ཀྱི་ཕུན་སུམ་ཚོགས་པའི་ཡོན་ཏན་ཐམས་ཅད་མེད་བར་བྱས་པ་སྟེ། རེ་བའི་ཚུལ་གྱིས་ལྟ་བ་ན་ཆུ་མིག་སྐམ་པོའི་གནས་དང་འདྲ་བར་འགྱུར་ཏེ། དེ་ལྟར་ཆུ་མིག་སྐམ་པོ༌[^2287]ལ་སྐོམ་ཞིང་ཆུ་འདོད་པ་རྣམས་ཀྱིས་ཆུ་དོན་དུ་གཉེར་ཞིང་རེ་བ་དང་བཅས་པ་ལས་སྐམས་པར༌[^2288]གྱུར་ན་དེ་དག་གི་རེ་བ་ཉམས་པར་འགྱུར་ཏེ། དེ་བཞིན་དུ་འདིར་ཡང་ཡོན་ཏན་ཡོད་པར་རེ་བ་དང་བཅས་པ་རྣམས་ཏེ། ཡོན་ཏན་ལ་སྐོམ་པའི་སྐྱེ་བོ་དགའ་བ་རྣམས་ཀྱིས༌[^2289]རེ་བ་དང་བཅས་པ་ལས་མ་མཐོང་ན་ནི་འཇིག་པ་ཡིན་ཏེ། ཡོན་ཏན་གཉེར་བ་རྣམས་ཀྱིས༌[^2290]ཁྲོན་པ་སྐམ་པོ་བཞིན་དུ་མཐོང་བར་འགྱུར་རོ། །

[Block 3568]
གཞན་དུ་བགྱིས་ན༌[^2291]ཞེས་བྱ་བས་ཡོན་ཏན་ཡེད་ཅེས་གྲགས་ཤིང་རེ་བ་དག་ལས་མཐོང་ན་མི་མཛེས་པར་འགྱུར་རོ། །ཇི་ལྟར་མི་མཛེས་པར་འགྱུར་ཞེ་ན། དེ་ཉིད་བསྒྲུབ་པའི་ཕྱིར་དོན་བཞིན་མ་ཡིན་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 3569]
དོན་བཞིན་མ་ཡིན་ཡོན་ཏན་གྲགས་པ་འཕེལ། །ཞེས་བྱ་བ་ནི་ཡོན་ཏན་གྱི་གནས་སྐབས་མ་ཡིན་པའི༌[^2292]ཡོན་ཏན་གྱི་འཕེལ་བ་སྟེ། གང་མི་རྣམས་ཀྱི་གྲགས་པ་མདུན་ན་བརྗོད་པ་མ་ཡིན་ཏེ། དོན་བཞིན་མ་ཡིན་པ་ཡུན་རིང་དུ་འཕེལ་བའོ། །

[Block 3570]
རྣམ་པར་རྟོག་པའི་རླུང་གིས་བསྐྱོད་པ་ནི་རྟོག་པའི་རླུང་གིས་ཉམས་པར་བྱས་པའོ། །

[Block 3571]
མི་རྣམས་ཀྱི༌[^2293]གྲགས་པ་དེ་ཉམས་པར་གྱུར་ན་ནི་དེ་ཕྱིས་ཡང་གྲགས་པར་འགྱུར་བ་ཞེས་བྱ་བ་ནི་འཕེལ་བར་འགྱུར་བའོ། །

[Block 3572]
སྦྲུལ་ནག་ཅེས་བྱ་བ་འདི་ནི་མཇུག་བསྡུ་བའི་ཚིགས་བཅད་ཡིན་ཏེ། ལྷ་གཅིག་བདག་ནི་བཟློག་པར་མི་རིགས་སོ། །ཞེས་བྱ་བ་ནི་བཟློག་པ༌[^2294]རིགས་པ་ཡང་ཡིན་མོད་ཀྱི་འོན་ཀྱང་བདག་ནི་བཟློག་པར་མ་མཛད་ཅིག་ཅེས་པ་སྟེ། ངེས་པར་གཟུང་བ༌[^2295]མ་ཡིན་བ་དང་ངེས་པར་གཟུང་བའི་རྒྱུ་སྟེ། གུས་པར་མཁྱེན་ནས་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་ཏེ། གུས་པར་མཁྱེན་ནས༌[^2296]ཞེས་བྱ་བའི་ཚིགས་བཅད་ཕྱད་ཀྱིས་ནི་ངེས་པར་གཟུང་བ་མ་ཡིན་པའི་རྒྱུ་བསྟན་ཏེ། །ངེས་པར་གཟུང་བ༌[^2297]ནི། བདག་ནི་སེམས་ཀྱིས་རབ་ཏུ་བྱུང་། ། ཞེས་བྱ་བ་ཕྱེད་འོག་མས་བསྟན་ཏོ། །

[Block 3573]
བྱམས་པ་ཡིས་ཞེས་བྱ་བ་ནི་རྗེ་བོའི་ཡོན་ཏན་ནོ། །

[Block 3574]
གུས་པར་མཁྱེན་ནས་ཞེས་བྱ་བ་ནི་འབངས་ཀྱང་ཡོན་ཏན་གུས་པ་དང་ལྡན་པར་ཁྱོད་ཀྱིས་དེ་མི་ཤེས་པ་ཡང་མ་ཡིན་ཏེ། ཁྱོད་ཀྱིས༌[^2298]འབངས་ཀྱི་སྐྱེ་བོ་ལ་དེ་ལྟར་བགྱི་བ་རིགས་ཏེ། དེ་བས་ན་ཁྱོད་ཀྱིས་བཟློག་པའི་རིགས་སོ། །

[Block 3575]
བདག་ནི་རེ་ཞིག་བཟློག་པར་བྱ་བ་མ་ཡིན་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། སེམས་ཀྱིས༌[^2299]རབ༌[^2300]བྱུང་ཟིན་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
