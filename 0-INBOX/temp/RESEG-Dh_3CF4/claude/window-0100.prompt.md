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
[Block 3501]
སྤོབས་པ་ནི་དེའི་ལན་དེ་མི་སྤོབས༌[^2242]བཞིན་དུའོ། །

[Block 3502]
དར་ལ་བབ་ཅིང་བྱད་གཟུགས་བཟང་། །ཞེས་བྱ་བའི་དོན་ནི་བདག་གི་དབང་ངམ་གཞན་གྱི་དབང་གིས་རབ་ཏུ་བྱུང་བར་བྱེད་པའི་རྒྱུ་ཡིན་ན་རབ་ཏུ་བྱུང་བའི་རྒྱུ་དེ་གཉི་ག་མེད་པར་སྟོན་ཏོ། །

[Block 3503]
[^2243]བདག་གི་དབང་ཡང་རྣམ་པ་གཉིས་ཀྱིས་རབ་ཏུ་བྱུང་བ་ཡིན་ཏེ། ལོངས་སྤྱོད་སྤྱོད་པར་མི་ནུས་པ་དང་། དཀའ་ཐུབ་ཀྱི་ནགས་སུ་གནས་པར་འོས་པ་སྟེ་གཉིས་སོ། །

[Block 3504]
དེ་གཉི་ག་ཡང་མེད་པར་བསྟན་པའི་ཕྱིར་དང་པོའི་ཕྱེད་ཀྱིས་བསྟན་པ་ཡིན་ཏེ། དར་ལ་བབ་ཅིང་བྱད་གཟུགས་བཟང་། །ཞེས་བྱ་བ་འདི་གཉིས་ཀྱིས་ནི་ཉེ་བར་ལོངས་སྤྱོད་པར་རིགས་པར་བསྟན་ཏེ། དར་ལ་བབ་པས་ནི་རང་ཉིད་ཀྱིས་ལོངས་སྤྱོད་པར་ནུས་པ་དེས་སོ། །

[Block 3505]
བྱད་གཟུགས་བཟང་ཞེས་བྱ་བས་ནི༌[^2244]བུད་མེད་རྣམས་ཀྱིས་ཀྱང་འདོད་པར་བྱ་བ་དེས་སོ། །

[Block 3506]
གཞོན་ཤ་ཅན་དང་བདེ་བར་གསོས། །ཞེས་བྱ་བ་འདི༌[^2245]གཉིས་ནི་ནགས་སུ་གནས་པ་མི་རིགས་པར་བཤད་དེ། ལུས་གཞོན་ཤ་ཅན་ཡིན་པའི་ཕྱིར་དང་། བདེ་བ་དང་རྗེས་སུ་མཐུན་པའི་རྐྱེན་ཐོབ་པའི་ཕྱིར་རོ། །

[Block 3507]
དེ་ལྟར་བཞི་པོ་འདིས་བདག་གི་དབང་གིས་རབ་ཏུ་བྱུང་བ་མི་རིགས་པར་སྟོན་ཏོ། །

[Block 3508]
གཞན་གྱི་དབང་གིས་ཀྱང་རབ་ཏུ་འབྱུང་བ༌[^2246]མི་རིགས་པར་སྟོན་ཏོ། །

[Block 3509]
[^2247]དེ་ནི་རྒྱལ་པོའི་གནང་ཆེན་ཡིན། །ཞེས་པ་སྟེ། གལ་ཏེ་རྒྱལ་པོས་གཞན་དུ་སྤྱུགས་ན་ནི་རབ་ཏུ་འབྱུང་གི། དེ་ནི་གནང་ཆེན་ཡིན་ཞེས་བྱ་བའི་ཚིག་གིས་དེ་མེད་པར་སྟོན་ཏོ། །

[Block 3510]
དེ་ལྟར་ནགས་གནས༌[^2248]སུ་རིག་ནས་ཁྱིམ་ཡོངས་སུ་གཏོང་བའི་རྒྱུ་མེད་དོ། །

[Block 3511]
དེས་ན་ཁྱིམ་ཡོངས་སུ་གཏང་བའི༌[^2249]རྒྱུ་མེད་པར་བསྟན་བའི་ཕྱིར། ནང་མི་དག་དང་ཞེས་བྱ་བའི་ཚིགས་བཅད་བརྩམས་པ་ཡིན་ཏེ། རྒྱུ་གསུམ་གྱིས་ནི་ཁྱིམ་ཡོངས་སུ་གཏང་བར༌[^2250]བྱ་བ་ཡིན་ཏེ། རྣམ་པ་གསུམ་པོ༌[^2251]ཡང་བསོད་ནམས་ཀྱི་འབྲས་བུས་ཕོངས་པར་བསྟན་པའོ། །

[Block 3512]
དེ་མེད་ན་ཇི་ལྟར་བབ་ཅོལ་དུ་ཁྱིམ༌[^2252]ཡོངས་སུ་གཏད༌[^2253]ཞེས་བྱ་བ་ནི་ཚིགས་བཅད་འདིའི་བསྡུས་པའི་དོན་ཏོ། །

[Block 3513]
ནང་མི་དག་དང་འཁོན་མ་བྱུང་། །ཞེས་བྱ་བ་འདིས་ནི་བཟོད་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པས་ཕོངས་པ་མེད་པར་བསྟན་ཏོ། །

[Block 3514]
རྒས་པས་མི་སྡུག་མ་གྱུར་ཅིང་། །ཞེས་བྱ་བ་དང་། ནད་མེད་ཅེས་བྱ་བ་འདི་གཉིས་ཀྱིས་ནི་བདག་ཉིད་ཚུལ་ཁྲིམས་ཀྱི་བསོད་ནམས་ཀྱི་ཚོགས་ཀྱི་འབྲས་བུ་ཡོད་པར་བསྟན་ཏོ། །

[Block 3515]
ཁྱིམ་གྱི་ལོངས་སྤྱོད་སྤྱོད་པ་ཞེས་བྱ་བ་འདིས༌[^2254]ནི་སྦྱིན་པ་ལས་བྱུང་བའི་བསོད་ནམས་ཀྱི་ཚོགས་ཀྱི་འབྲས་བུ་ཕོངས་པ་མེད་པར་བསྟན་ཏོ། །

[Block 3516]
ཚིག་གཅིག་ཅེས་བྱ་བ་ནི་གསུམ་པོ་དེ་དག་མ་ཚང་བ་མེད་ཀྱང་བབ་ཅོལ་དུ་གཏོང་བར་ནུས་ཞེས་པའོ། །

[Block 3517]
དེ་མཆོག་ཏུ་གསལ་བའི་ཕྱིར། མཛངས༌[^2255]ཤིང་དུལ་བའི་རྒྱན་གྱིས་བརྒྱན། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ཏེ། རང་གི་ཆུང་མ་བོར་བ་མི་རིགས་པ་ལས༌[^2256]བརྩམས་པའོ། །

[Block 3518]
འདི་ལྟ་བུ་ཞེས་བྱ་བ་ནི་འདོད་པའི་དོན་དང་ལྡན་པའོ། །

[Block 3519]
ནང་མི་ནི་རང་གི་ཆུང་མའོ། །

[Block 3520]
མི་བརྟན་ནང་མི་སྙིང་རྗེ་མེད་པ་ནི་མི་བརྟན་སྙིང་རྗེ་མེད་པས་སོ། །ཇི་ལྟར་འདོད་པ་དང་འགལ་བ་ཡིན་ཞེ་ན། སྨྲས་པ། དུལ་བའི་རྒྱན་གྱིས་བརྒྱན་ཞེས་བྱ་བ་སྨོས་ཏེ། བརྒྱལ་འདོད་པའི་དོན་དུ་རང་གི་ཆུང་མ་ཡོངས་སུ་བཏང་སྟེ། བུད་མེད་གཞན་དག་ལ་ཆགས་ན་དེས་ནི་དེ་ལ་སྙིང་ཉེ་བ་མེད་ན་འདི་ནི་དེ་ལྟ་མ་ཡིན་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། དུལ་བའི་རྒྱན་གྱིས་བརྒྱན་པའི་ཕྱིར་ཏེ། གང་གི་ཕྱིར་མ་དུལ་བ་ནི་བུད་མེད་གཞན་ལ་ཡང་ཆགས་པར་འགྱུར་ན། དེ་མེད་པས་རང་གི་ཆུང་མ་ཡང་ཡོངས་སུ་གཏོང་བ་འདི་ནི་འདོད་བའི་དོན་དང་འགལ་བའོ། །

[Block 3521]
མཛངས༌[^2257]ཤིང་ཞེས་བྱ་བ་འདིས་ནི་ནོར་དང་འགལ་བར་བསྟན་ཏེ། [^2258]གང་གི་ཕྱིར་མཛངས༌[^2259]ན་ནི་རིགས་ལ་སོགས་པའི་ཡོན་ཏན་དང་། ཡོན་ཏན་མ་ཡིན་པའི་བྱ་བྲག་མཐོང་བ་ཡིན་ཏེ། དེའི་ནུས་པ་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 3522]
རིགས་ལ་སོགས་པའི་ཡོན་ཏན་གྱིས༌[^2260]ཁྱད་པར་དུ་འཕགས་པ་དང་ལྡན་པ་གཞན་ནི་མ་མཐོང་ལ། དེ་དག་མ་མཐོང་ཡང་རང་གི་ཆུང་མ་ཡོངས་སུ་གཏོང་བས་ནི་ནོར་དང་འགལ་བར་གྱུར་པའོ།[^2261] །མཉེས་ཀྱང་གཤིན་ཞེས་བྱ་བ་འདིས་ནི་ཆོས་དེ་ལྟ་བུ་དང་ལྡན་ཡང་རང་གི་ཆུང་མ་ཡོངས་སུ་གཏོང་བ་ཉིད་དེ། དེ་ལྟར་རེ་ཞིག་བདག་ལ་ལྟོས་པ༌[^2262]ནང་མི་ཡོངས་སུ་གཏོང་བར་མི་རིགས་པར་བསྟན་ཏེ། [^2263]ད་ནི་ནང་མི་ལ་ལྟོས༌[^2264]ནས་ནང་མི་ཡོངས་སུ་གཏོང་བར༌[^2265]མི་རིགས་པར་སྟོན་ཏེ། གཞན་ལ་སྙིང་བརྩེ་བ་ཞེས་པས་སོ། །

[Block 3523]
གཞན་གྱི་སྡུག་བསྔལ་ལ་ལྟོས་པས་ཀྱང་གཞན་ལ་སྙིང་བརྩེ་བའི་ཕྱིར་ནང་མི་ཡོངས་སུ་གཏོང་བར༌[^2266]མི་རིགས་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 3524]
མཉེས་ཀྱང་གཤིན་ཞེས་བྱ་བ༌[^2267]བཤད་པས་མཉེས་གཤིན་པས་ནི་མཆོག་ཏུ་ནང་མི་ཡོངས་སུ་གཏང་བར་རིགས་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། རབ་ཏུ་བྱུང་བའི་ཆོས་དང་མཐུན་པར་འདོད་པས་སོ་ཞེས་གང་དག་ཡོངས་སུ་རྟོག་པ་ལ། དེའི་ལན་བརྩམས་པའི༌[^2268]ཕྱིར། དགེ་སྦྱོང་བྲམ་ཟེ་མཛའ་བོའི་རྟེན། །ཞེས་བྱ་བ་དང་། རྗེས་སུ་མཐུན་ཞིང་ཆོས་གྲོགས་བྱེད། །ཅེས་བྱ་བའི་ཚིག་གཉིས་ཡིན་ཏེ། དགེ་སྦྱོང་བྲམ་ཟེ་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཀྱི་དོན་ནི་རབ་ཏུ་བྱུང་ནས་ནགས་སུ་གང་རྙེད་པའི་ཆོས་དེ་ནི་ཁྱིམ་དུ་ཡང་རྙེད་པ་དང་། ཁྱད་པར་གྱི་ཆོས་ཀྱང་རྙེད་པ་ཉིད་དུ་བསྟན་པའི་ཕྱིར་སྨྲས་པའོ། །

[Block 3525]
[^2269]དགེ་སྦྱོང་དང་བྲམ་ཟེ་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཕྱེད་ཀྱིས་ནི་སྦྱིན་པའི་ཞིང་རྙེད་པར་དཀའ་བ་བསྟན་ཏེ། དགེ་སྦྱོང་བྲམ་ཟེ་ཞེས་བྱ་བ་སྨོས་པས་ནི་ཡོན་ཏན་གྱི་ཞིང་ངོ་། །མཛའ་བོའི་རྟེན་དང་ནང་མི་ཞེས་སྨོས་པས་ནི་ཕན་འདོགས་པའི་ཞིང་ཉིད་དོ། །

[Block 3526]
ཕོངས་པ་ཞེས་སྨོས་པས་ནི་སྙིང་རྗེའི་ཞིང་ཉིད་དོ། །

[Block 3527]
འདི་ནི་རེ་ཞིག་ནགས་ན་གནས་པ་ལས་ཁྱད་པར་དུ་བྱ་བའི་ཆོས་སོ། །

[Block 3528]
གཙང་སྦྲ་ཚུལ་ཁྲིམས་ནོར་ཞེས་བྱ་བ་འདིས་ནི་ནགས་དང་ཁྱིམ་གཉིས་ཀྱི་ཐུན་མོང་གི་ཐོབ་པའི་ཆོས་བསྟན་ཏོ། །

[Block 3529]
ནགས་ཚལ་དགོན་པར་གང་བཙལ་བ། ཞེས་བྱ་བ་ནི་གང་ནགས་ཀྱི་ཕྱོགས་སུ་འདོད་ཅིང་བཙལ་བ་དེ་ཅི་ཁྱིམ་འདིར་མི་རྙེད་དམ་ཞེས་པའོ། །

[Block 3530]
དེ་ལྟར་ཡང་ནགས་སུ་འཇུག་པ་ལ་ནི་སྐྱོན་དང་འབྲེལ་པའོ་ཞེས་བསྟན་པའི་ཕྱིར། རྗེས་སུ་མཐུན་ཞིང་ཆོས་གྲོགས་བྱེད། །ཅེས༌[^2270]བྱ་བའི་ཚིགས་བཅད་བརྩམས་སོ། །

[Block 3531]
རྒྱུ་གསུམ་གྱིས་བུད་མེད་ཡོངས་སུ་སྤང་བར་བྱ་བ་ཡིན་ཏེ། རྒྱུ་གསུམ་མ་གཏོགས་པར་རང་གི་ཆུང་མ་ཡོངས་སུ་གཏོང་བ་ལས་ནི་ཆོས་མ་ཡིན་པར་འགྱུར་ཏེ། ཅི་ཆོས་མ་ཡིན་པ་ལ་མི་ལྟ། ཞེས་བྱ་བ་ནི་བསྡུས་པའི་དོན་ཏོ། །

[Block 3532]
ཉེས་པ་བའམ། རྗེས་སུ་མི་མཐུན་པའམ། རང་དགར་བྱེད་པའི་གཡོག་འཁོར་ནི་ཡོངས་སུ་སྤངས་ཀྱང་ཆོས་མ་ཡིན་པ་ཐོབ་པར་མི་འགྱུར་རོ། །

[Block 3533]
ཡོན་ཏན་གསུམ་དང་ལྡན་ན་ནི་ཆོས་མ་ཡིན་པ་ཐོབ་པར༌[^2271]འགྱུར་རོ། །

[Block 3534]
ཉེས་པ་མ་བྱས་པ་ནི་གུས༌[^2272]པའི་སྐྱེ་བོ་སྤངས་པ་ཉིད་ཡིན་ཏེ། འཁྲུལ་པའི་སྐྱོན་མེད་པས་སོ། །

[Block 3535]
རྗེས་སུ་མཐུན་ཞེས་བྱ་བ་ནི་ཁྱིམ་ཐབ་ལས་མི་འཕྱོ་བའོ། །

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
--- END BLOCKS ---
