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
[Block 4481]
ཅེས་བྱ་བ་སྟེ། དེ་ལྟར་བསྟན་པ་དང་། སྤང་བའི་ཕན་ཡོན་ནི༌[^2902]གང་ཡིན་ཞེ་ན། དེའི་ཕན་ཡོན་བསྟན་པའི་ཕྱིར། འབངས་རྣམས་སྐྱོན་ལ༌[^2903]མི་དགའ་ཞེས་བྱ་བ་ཕྱེད་འོག་མའོ། །

[Block 4482]
ཕན་ཡོན་རྣམ་པ་སྣ་ཚོགས་པ་ནི་བདག་ཉིད་ཀྱི་གྲགས་པ་འཐོབ་པ་དང་། འབངས་རྣམས་ཀྱི་ཡོན་ཏན་དང་། སྐྱོན་གཉིས་ལ་དགའ་བ་དང་། མི་འགལ་བར་འགྱུར་བ་སྟེ།

[Block 4483]
དང་པོ་བདག་ཉིད་ཀྱི་ཕུན་སུམ་ཚོགས་པས་ནི་བདག་གི་གྲགས་པ་འཐོབ་པའོ། །

[Block 4484]
ཇི་ལྟར་འབངས་རྣམས་ཀྱི་ཡོན་ཏན་དང་། སྐྱོན་ལ་ཐོབ་པ་དང་མི་འགལ་བ་ཡིན་ཞེ་ན། དེ་སྒྲུབ་པའི་ཕྱིར། ཁྱོད་ཀྱིས་ཆོས་སྤྱོད༌[^2904]གྱུར་ན་མི་ཡི་འཇིག་རྟེན་ཕལ་ཆེར་ནི། །ཞེས་བྱ་བ་སྨོས་ཏེ། ཕལ་ཆེར་ཞེས་བྱ་བ་ནི་མང་པོར་སྟོན་པ་ཡིན་ཏེ། འདིས་ནི་གཏན་དུ་སྤྱོད་པ་དེ་མ་གཏོགས་པའོ། །

[Block 4485]
ལེགས་པར་སྤྱོད་ལ༌[^2905]ཕྱོགས་ཤིང་ཞེས་བྱ་བ་ནི་མཐོང་བའི་ཆོས་ཀྱི་སྒྲུབ་པའི་ཕན་ཡོན་ནོ། །

[Block 4486]
སྐྱེ་དགུ་རྣམས་ནི༌[^2906]མཐོ་རིས་ལམ་ལ་གནས་པར་འགྱུར། །ཞེས་བྱ་བ་ནི་འཇིག་རྟེན་ཕ་རོལ་གྱི་ཕན་ཡོན་ནོ། །

[Block 4487]
དེ་ལྟར་འབངས་རྣམས་བསྐྱངས་བའི་ཕན་ཡོན༌[^2907]བསྟན་པའི་ཕྱིར། ཁྱོད་ཀྱིས་བརྩོན་འགྲུས་བསྐྱེད་དེ་འགྲོ་བ་འདི་དག་ཅེས་བྱ་བའི་ཕྱེད་འོག་མའོ། །

[Block 4488]
འགྲོ་བ་འདི་དག་ཡོངས་སུ་སྐྱོང་བ་ནི་མཐོང་བའི་ཆོས་ཀྱི་ཕན་ཡོན་ནོ། །

[Block 4489]
དེ་ཡོངས་སུ་བསྐྱང་བར་དམ་བཅས་པའི་ཕྱིར། དམ་བཅས་པས་ཆོས་ལ་བརྟེན་ཞེས་བྱ་བ་ནི་འཇིག་རྟེན་ཕ་རོལ་གྱི་ཕན་ཡོན་ནོ། །

[Block 4490]
ཆོས་ཞེས་སྨོས་པས་ནི་ལེགས་པར་སྤྱད་པའི་འབྲས་བུ་གཟུང༌[^2908]ངོ་། །ཡང་ན་ལེགས་པར་སྤྱོད་པ་འདི་ཉིད་ཆོས་ཡིན་པས་དེ་ལ་བརྟེན་ཅིག་ཅེས་བསྟན་པ་ཡིན་ནོ། །

[Block 4491]
ཆོས་དེ་གང་ཡིན་ཞེ་ན། དེ་བསྟན་པའི་ཕྱིར་ཚུལ་ཁྲིམས་རྣམ་པར་སྦྱོང་ལ་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིའི་བསྡུས་པའི་དོན་ནོ། །

[Block 4492]
བསོད་ནམས་ཀྱི་ཚོགས་ཡོངས་སུ་འབྱུང་སྟེ། ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་པོ་བརྩོན་འགྲུས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་བར་དུ་བསྟན་ཏོ། །

[Block 4493]
ཚུལ་ཁྲིམས་རྣམ་པར་སྦྱོང་ལ་ཞེས་བྱ་བས༌[^2909]ནི་ཚུལ་ཁྲིམས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བསྟན་ཏེ། ཚུལ་ཁྲིམས་རྣམ་པར་སྦྱོང་ལ༌[^2910]ཞེས་བྱ་བས་ནི༌[^2911]སྐྱོན་མེད་པ་དང་མ་ཉམས༌[^2912]པ་ཞེས་བྱ་བ་ལ་སོགས་པ་གང་བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་པའི་རིམ་པས་སྦྱོང་བའོ། །

[Block 4494]
སྦྱིན་པའི་གྲགས་པ་སྤེལ་ཞེས་བྱ་བ་ནི་འདྲ་བ་མེད་པའི་སྦྱིན་པས་གྲགས་པར་འགྱུར་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4495]
བྱམས་པར་གྱིས་ཞེས་བྱ་བ་ནི་སྐྱེ་བོ་གཞན་དག་གནོད་པ་མེད་པ་ལ་ཡང་ནང་མི་ཇི་ལྟ་བ་བཞིན་དུ་ཞེས་བྱ་བ་ཡིན་ཏེ། ཇི་ལྟར་ཉེ་དུའི་སྐྱེ་བོ་བཞིན་དུའོ། །

[Block 4496]
ས་ལ་འཁོད་པ་ཆོས་ཀྱིས་སྐྱོང་ལ་བག་མེད་སྤོངས། །ཞེས་བྱ་བས་ནི་བརྩོན་འགྲུས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བསྟན་ཏེ། བརྩོན་འགྲུས་ལ་ཡང་རྣམ་པ་བཞི་སྟེ། དགེ་བའི་ཆོས་མ་སྐྱེས་པ་སྐྱེས་པ༌[^2913]དང་། དགེ་བའི་ཆོས་སྐྱེས་ཟིན་པ་རྣམ་པར་སྤེལ་བར་བྱ་བའི་ཕྱིར་ཏེ། དེ་གཉིས༌[^2914]ནི་ས་ལ་འཁོད་པ་ཆོས་ཀྱིས་སྐྱོང་ཞེས་བྱ་བ་འདི་བསྟན་པ་ཡིན་ནོ། །

[Block 4497]
སྡིག་པ་མི་དགེ་བའི་ཆོས་མ་སྐྱེས་པ་རྣམས་མི་སྐྱེད་པ་དང་། སྐྱེས་ཟིན་པ་རྣམས་སྤང་བའི་ཕྱིར་ཏེ། དེ་གཉི་ག་ནི་བག་མེད་སྤོངས་ཞེས་བྱ་བ་འདིས་བསྟན་པ་ཡིན་ནོ། །

[Block 4498]
འདི་ནི་བསོད་ནམས་ཀྱི་ཚོགས་ཀྱི་ཆོས་དང་། རྗེས་སུ་མཐུན་པའི་ཕན་ཡོན་གྱི་དབང་དུ་བྱས་པ་སྟེ། དེ་ལྟར་བྱས་ན་ཞེས་བྱ་བའི་ཚིག་རྐང་གཅིག་གོ། །

[Block 4499]
གྲགས་པ་འཐོབ་ཅེས་བྱ་བ་ནི་མཐོང་བའི་ཆོས་ཀྱི་ཕན་ཡོན་ནོ། །

[Block 4500]
མཐོ་རིས་འཐོབ་ཅེས་བྱ་བ་ནི་འཇིག་རྟེན་ཕ་རོལ་གྱི་ཕན་ཡོན་ནོ། །

[Block 4501]
དེ་ལྟར་རེ་ཞིག་རྒྱལ་པོས་སྤང་བ་དང་། །བླང་བ་ལ་སོགས་པའི་སྒྲུབ་པས་འཛིན་དུ་བཅུག་ནས་ཡུལ་གྱི་མིའི་རང་བཞིན་བསྒྲུབ་པའི་དབང་དུ་བྱས་ནས། ཆུན་པ་རྣམས་དང་ཕྱུགས་ལུག་འཚོ་བ་རྣམས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 4502]
ཅིའི་ཕྱིར་ལུགས་ཀྱི་བསྟན་བཅོས་ལས༌[^2915]བཤད་པའི་རིམ་པ་ལས་འདའ་བར་བྱ་སྟེ། དང་པོ༌[^2916]ཡུལ་གྱི་མིའི་ཆོས་སྨོས་ཤིང་བློན་པོའི་རང་བཞིན་མ་བསྟན། རྗེ་བོ་དང་། བློན་པོ་དང་། ཡུལ་མི་དང་། མཁར་དང་། དཀོར་དང་། བཀའ་ཁྲིམས་དང་། གྲོགས་པོ་རྣམས་ཀྱི་རང་བཞིན་རྣམས་ཏེ། འདི་ལྟར་བསྟན་བཅོས་ལས་བརྗོད་པའི་རིམ་པ་འདི་ཉིད་ནི་རིགས་པའི་ཚུལ་ཉིད་དུ་འགྱུར་ཏེ། ལུགས་ཀྱི་བསྟན་བཅོས་ལས་བཤད་པའི་རིམ་པའོ། །

[Block 4503]
འདིར་ཅི་ཞིག་བྱས་ཤེ་ན། བདག་པོས་གང་བསྲུང་བ་དང་། གང་དང་ལྷན་ཅིག་བསྲུང་བ་ཞེས་བྱ་བ་ཡིན་ཏེ། གང་བསྲུང་བ་ནི་ཡུལ་མི་དང་། རྫོང་དང་། ནོར་རོ། །

[Block 4504]
གང་དང་ལྷན་ཅིག་བསྲུང་ཞེ་ན། བཀའ་ཁྲིམས་དང་། བློན་པོ་དང་། གྲོགས་པོ་རྣམས་ཡིན་ཏེ། དེ་བས་ན་རིམ་པ་འདི་ནི་རིགས་པ་ཉིད་དོ། །

[Block 4505]
དེ་ལ་ཡུལ་མིའི་རང་བཞིན་གྱི་སྒྲུབ་པ་ཡང༌[^2917]རྣམ་པ་གཉིས་ཏེ། སྲུང་བའི་སྒྲུབ་པ༌[^2918]དང་། རྗེས་སུ་ཕན་གདགས་པ་དང་། དཔྱ་དབུལ་བའི་སྒྲུབ་པའོ། །

[Block 4506]
དེ་ལས་སྲུང་བའི༌[^2919]སྒྲུབ་པའི་དབང་དུ་བྱས་ནས། ཆུན་པ་རྣམས༌[^2920]ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིའོ། །

[Block 4507]
ཆུན་པ་ཞེས་བྱ་བ་ནི་ཞིང་ལས་གཙོར༌[^2921]བྱེད་པ་ཡིན་ནོ། །

[Block 4508]
ཕྱུགས་ལུག་འཚོ་བ་རྣམས་ཞེས་བྱ་བ་ནི་བ་ལང་ལ་སོགས་པ་བསྐྱང་བ་ལ་འབད་པ་སྟེ། འཚོ་ཚིས་ལ་འཇུག་པའོ། །

[Block 4509]
ཡུལ་མི་ཡོངས་སུ་བསྐྱང་བ་ལ་ཅིའི་ཕྱིར་ཚོང་ལ་འཇུག་པ་སྨོས་ཤེ་ན། འོག་ཏུ་ནོར་གྱི་སྒོ་ནས་རྗོད་པར་བྱེད་པས་སོ། །

[Block 4510]
དང་པོ་གཉིས་ཀྱི་གོ་རིམས་ནི་ཆུན་པ་ནི་མེ་ཏོག་དང་ལྡན་པའི་ལྗོན་ཤིང་ལྟ་བུ་སྟེ། རིམ་གྱིས་འབྲས་བུ་སྟེར་བའི་ཕྱིར་རོ། །

[Block 4511]
ཕྱུགས་ལུག་འཚོ་བ་རྣམས་ཞེས་བྱ་བ་ནི་འབྲས་བུ་ལྡན་པའི་ལྗོན་ཤིང་ལྟ་བུ་སྟེ། དེ་མ་ཐག་ཏུ་འབྲས་བུ་སྟེར་བའི་ཕྱིར་རོ། །

[Block 4512]
སྨན་རྣམས་ཀུན་དང་ཞེས་བྱ་བ་ནི་འབྲས་སཱ་ལུ་ལ་སོགས་པ་དང་ཕྱུགས་ལུག་ལ་སོགས་པ་ཆོས་ཀྱི་འབྲས་བུ་ཆེན་པོ་ཡིན་ཞེས་བྱ་བ་འདིའི་དོན་ཏོ། །

[Block 4513]
བདེ་བ་འདོད་ཕྱིར་འབངས་རྣམས་སེམས་པར་མཛོད། །ཅེས་བྱ་བས་ནི་གང་སྔར་བསྟན་པའི། ཁྱོད་ཀྱིས༌[^2922]ཆོས་སྤྱད་གྱུར་ན་མི་ཡི་འཇིག་རྟེན་ཕལ་ཆེར༌[^2923]ནི། །ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིར་ཡང་སྦྱར་བར་བྱའོ། །

[Block 4514]
ཆགས་དང་ཞེ་སྡང་མེད་པའི་ནན་ཐུར་གྱིས། །ཞེས་བྱ་བ་ནི་གང་སྔར་བསྟན་པའི་རང་བཞིན་དག་ལ་ཇི་ལྟར་སྦྱར་བ་བཞིན་དུ་ཐམས་ཅད་ལ་ཡང་བརྗོད་དོ། །

[Block 4515]
འཇིག་རྟེན་བསྲུངས་ཞེས་བྱ་བ་ནི་བདག་གི་རང་བཞིན་བསྲུང་བ་དང་། འཇིག་རྟེན་གྱི་མཐོ་རིས་ཀྱི་འདོད་པ་ཐོབ་པའི་ཆེད་དུ་སྤྱད་དོ། །

[Block 4516]
སློབ་དཔོན་དཔའ་བོས་མཛད་པའི་སྐྱེས་པའི་རབས་རྒྱ་ཆེར་བཤད་པ་ལས་བྱང་ཆུབ་ཆེན་པོའི་སྐྱེས་པའི་རབས་སོ།། །།

[Block 4517 [HEADING]]
## སྤྲེའུ་ཆེན་པོའི་སྐྱེས་པའི་རབས། ^26-0

[Block 4518]
རྣམ་པ་སྣ་ཚོགས་པའི་འབྱུང་ཁུང༌[^2924]ནི། རྣམ་པ་སྣ་ཚོགས་པའི་འབྱུང་ཁུང་ངོ་། །རྣམ་པ་སྣ་ཚོགས་པའི་འབྱུང་ཁུང་གི་རྫས་གང་ཡིན་པའི་རིའི་ངོས་དེ་ནི་འབྱུང་ཁུང་གི་རྫས་རྣམ་པ་སྣ་ཚོགས་པའི་གངས་རིའི་ངོས་ཏེ་དེ་ནའོ། །

[Block 4519]
ཀཽ་ཤཱམྦཱིའི་དར་སྔོན་པོས་སྟོད་གཡོགས་སུ་གང་གིས་བྱས་པ་དེ་ནི་ཀཽ་ཤཱམྦཱིའི་དར་སྔོན་པོས་སྟོད་གཡོགས་གང་གིས༌[^2925]བྱས་པ་དེའོ། །

[Block 4520]
རྣམ་པ་དུ་མ་དག་གི་དབྱིབས་ཀྱི་རྣམ་པ་ནི༌[^2926]དབྱིབས་མང་པོའོ། །
--- END BLOCKS ---
