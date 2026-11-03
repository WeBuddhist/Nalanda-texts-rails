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
[Block 4026]
ལྷའི་གདན་ཡང་ཡིན་པས་ལྷའི་གདན་རིམ་པ་དུ་མའོ། །

[Block 4027]
དེ་བཤམས་པ་ནི་ལྷའི་གདན་རིམ་པ་དུ་མར་བཤམས་པ་སྟེ། དེས་མངོན་པར་དགའ་བར་བྱ་བ་གང་ཡིན་པ་དེ་ནི་ལྷའི་གདན་རིམ་པ་དུ་མར་བཤམས་ཤིང་བཟང་བའོ། །

[Block 4028]
རྒྱབ་རྟེན་དང་བདེ་ཞིང་ཉམས་དགའ་བ་ནི་རྒྱབ་རྟེན་བདེ་ཞིང་ཉམས་དགའ་བའོ། །

[Block 4029]
བརྒྱན་པ་དང་བཅས་པ་ནི་རྒྱབ་རྟེན་བདེ་ཞིང་ཉམས་དགའ་བས་བརྒྱན་པའོ། །

[Block 4030]
བཙུགས་པའི་རྐང་རྟེན་གང་ཡིན་པ་འདི༌[^2601]ནི་རྐང་རྟེན་བཙུགས་པའོ། །

[Block 4031]
དྲིལ་བུ་བཞིན་དུ་སྙན་པ་ནི་དྲིལ་བུ་ལྟར་སྙན་པ་སྟེ་དེས་སོ། །

[Block 4032]
གཟི་བྱིན་ཆེ་ཞིང་མདངས་དང་ལྡན་པའི་སྐུ། །ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་དང་པོ་ལྔས་ནི་དགའ་བར་འགྱུར་བའི་གཏམ་ལས་བརྩམས་པ་སྟེ། འདིའི་བསྡུས་པའི་དོན་ནི་ལུས་ལ་རྣམ་པ་གཉིས་ཀྱིས་བདེའམ་མི་བདེ་ཞེས་དྲི་བ་བསྟན་ཏེ། གཟུགས་ཀྱི་ལུས་ལ་སྙུན༌[^2602]གསོལ་པ་ལས་བརྩམས་ཏེ། གཟི་བྱིན་ཆེ་ཞིང་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཕྱེད་ཀྱིས་བསྟན་ཏོ། །

[Block 4033]
གཟི་བྱིན་དང་མདངས་ནི། གཟི་བྱིན་དང་མདངས་སོ། །

[Block 4034]
གཟི་བྱིན་དང་མདངས་ཀྱི་གནས་སུ་གྱུར་པ་ནི་གཟི་བྱིན་དང་མདངས་ཀྱི༌[^2603]གནས་སོ། །

[Block 4035]
མདངས་སྨོས་པས་ནི་ཁ་དོག་གཟུང་ངོ་། །གཟི་བྱིན་སྨོས་པས་ནི་དབྱིབས་གཟུང་ངོ་། །

[Block 4036]
གཉིས་པ་ནི་གང་གི་ཕྱིར། མིག་གི་ཡུལ་གྱིས་བདེའམ་ཞེས་དྲིས་པ་ཡིན་ཏེ། ནད་མེད་པ་ནི་བདེ་བའི་གནས་ཡིན༌[^2604]ཏེ། སྔོན་དགེ་བ་བསགས་པའི་ཕྱིར་བདེ་བའི་གནས་སོ། །

[Block 4037]
ཆོས་ཀྱི་སྐུ་ལ་ཞེས་བྱ་བ་ལ། ཆོས་ཀྱི་སྐུ་ནི་བསོད་ནམས་ཀྱི་ཚོགས་བསགས་པ་སྟེ། ཕ་རོལ་ཏུ་ཕྱིན་པ་བཞི་ནི་ཆོས་ཀྱི་སྐུའོ། །

[Block 4038]
འདིས་ནི་རྒྱལ་པོའི་ཆོས་ཀྱི་ལུས་སྐྱེ་དགུ་སྲུང་ཞིང་སྐྱོབ་པར་བསྟན་ཏོ། །

[Block 4039]
རྨ་མེད་ཞེས་བྱ་བ་ནི་ཚུལ་ལས་མ་ཉམས་སོ༌[^2605]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4040]
བཀའ་ལུང་སྙན་པས་རྒྱ་ཆེར་དབུགས་ཕྱུང་ངམ་ཞེས་བྱ་བས་ནི་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བསྟན་ཏོ། །

[Block 4041]
ད་ནི་རྒྱལ་པོའི་ཆོས་ཀྱི་དབང་དུ་བྱས་པ་སྟེ། ཕན་གདགས་ནན་ཏུར་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་སུ་བཅད་པ་གསུམ་མོ། །

[Block 4042]
དེ་ལ་ཕན་གདགས་ནན་ཏུར་ཞེས་བྱ་བ་དང་། བློན་པོ་མཛངས༌[^2606]ཤིང་གློ་བ་ཉེ་བ་ཞེས་བྱ་བའི་ཚིགས་བཅད་གཉིས་ནི་རང་གི་ཡུལ་འཁོར་གྱི་དབང་དུ་བྱས་པའི་རྒྱལ་པོའི་ཆོས་སོ། །

[Block 4043]
སྐྱེ་དགུ་བསྲུང་བ༌[^2607]དེ་ཡང་ཚུལ་ཡིན་ཏེ། ཕན་གདགས་ནན་ཏུར་བགྱི་བའི་བཀའ་ཁྲིམས་ཀྱིས། །ཞེས་བྱ་བ་ནི་མངོན་སུམ་དུ་བཏགས་ནས་བསྟན་པ་དང་། དང་བས་ཇི་ལྟར་རིགས་པར་ཆད་པས་བཅད་པ་དང་། གློ་བ་ཉེ་བ་ལ་ཕན་གདགས་པར་བྱ་བ་ཉིད་དོ། །

[Block 4044]
ནན་ཏུར་གྱིས་ནི་ཕན་པ་འབྱུང་བ་ཡིན་ཏེ། བསྲུང་བའི་དབང་བསྐུར་བའི༌[^2608]ཕྱིར་རོ། །

[Block 4045]
བདག་གི་གྲགས་པའི་གཏམ་སྙན་རྒྱས་གྱུར་ཏམ། །ཞེས་བྱ་བ་འདི་དག་གིས་ནི་མངོན་སུམ་ཉིད་དུ་རྒྱལ་པོའི་ཆོས་བསྟན༌[^2609]ཏེ། །རྒྱལ་པོའི༌[^2610]ཚུལ་ནི་མངོན་སུམ་དང་། །ལྐོག་ཏུ་གྱུར་པ་རྗེས་སུ་དཔག་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4046 [VERSE]]
དེ་ལ་བདག་གིས༌[^2611]མཐོང་བ་ནི་མངོན་སུམ་མོ། །
བློན་པོ་མཛངས༌[^2612]ཤིང་གློ་བ་ཉེ་བ་རྣམས། །

[Block 4047]
བརྟག་པའི་ཐབས་ཀྱིས་ཞེས་བྱ་བ་ནི་ལྐོག་ཏུ་གྱུར་པ་རྗེས་སུ་དཔག་པའི་ཚུལ་ལོ། །

[Block 4048]
ལེགས་པར་ཞེས་བྱ་བ་ནི་རང་བཞིན་མི་དགའ་བའི་ཕྱིར་བརྟག་པའི་ཐབས་ནི་རྣམ་པ་ལྔའོ། །

[Block 4049]
ཉེ་བར་སྩོགས་པ༌[^2613]དང་ཐབས་མཐར་མ་ཕྱིན་པ་ནི་བརྟག་པའི་ཐབས་ཞེས་བརྗོད་དོ། །

[Block 4050]
གློ་བ་ཉེ་བ་ཞེས་བྱ་བ་ནི་བསམ་པ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 4051 [VERSE]]
མཛངས་པ༌[^2614]ནི་སྦྱོར་བ་ཕུན་སུམ་ཚོགས་པའོ། །
འབངས་ལ་སྨན་པ་རྟག་ཏུ་དགོངས་ལགས་སམ། །

[Block 4052]
ཞེས་བྱ་བ་ནི་གསུམ་པོ་དེ་ལྐོག་ཏུ་གྱུར་པའི་རྒྱལ་པོའི་ཚུལ་སྟོན་པ་ཡིན་ནོ། །

[Block 4053]
དེ་དག་མི་མཁྱེན་པར་ནི་མི་ཞུགས་གྲང་། །ཞེས་བྱ་བས་ནི་རྗེས་སུ་དཔག་པ་ཉིད་སྟོན་ཏོ། །

[Block 4054]
དེ་ལྟར་རེ་ཞིག་བྱ་བ་མ་ཡིན་པ་བྱེད་པ་ལས་ལྡོག་པའི་ཚུལ་བསྟན་ཏེ། ཆོས་ཀྱི་སྐུ་ལ་ཞེས་བྱ་བ་ནི་བྱ་བ་མ་ཡིན་པ་ལས་ལྡོག་པའི་ཚུལ་ལོ། །

[Block 4055]
ཕན་གདགས་ནན་ཏུར་ཞེས་བྱ་བ་དང་། བློན་པོ་མཛངས༌[^2615]ཤིང་ཞེས་བྱ་བ་གཉིས་ཀྱིས༌[^2616]ནི་སྐྱེ་དགུ་སྐྱོང་བ་ལ༌[^2617]འཇུག་པའི་ཚུལ་ལོ། །

[Block 4056]
དཔའ་ཞིང་ཐབས་མཁས་ཞེས་བྱ་བའི་ཚིགས་སུ་བཅད་པ་ནི་རྒྱལ་པོའི་ཆོས་ཀྱི་དབང་དུ་བྱས་པ་སྟེ། ཡུལ་ཕྱོགས་གཞན་གྱི་དབང་དུ་བྱས་ནས་ཐབས་མཁས་པ་ཞེས་སྨོས་ཏེ། བསྡུམ་པ༌[^2618]དང་དབྱེ་བའི་ཐབས་ཀྱིས་བྱ་བ་ཡིན་པས་ཐབས་མཁས་པ༌[^2619]ཞེས་བརྗོད་དོ། །

[Block 4057 [VERSE]]
དཔའ་བས་ཞེས་བྱ་བ་ནི་བཀའི་བཀའ་ཁྲིམས་བསྟན་ཏོ། །
ཐུགས་རྗེ་ཆེན་པོའི་མཛད་པ༌[^2620]མ་ཆིས་ལགས་སམ། །

[Block 4058]
ཞེས་བྱ་བ་ནི་བཟོད་པའི༌[^2621]ཕ་རོལ་ཏུ་ཕྱིན་པའོ། །

[Block 4059]
ཐུགས་རྗེ༌[^2622]བག་མེད་པར་ནི་མི་མནལ་གྲང་། །ཞེས་བྱ་བ་ནི་བརྩོན་འགྲུས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་སྟེ། ཆགས་པའི་དབང་དུ་མི་གཏང་བར་སྟོན་པ་ཡིན་ནོ། །

[Block 4060]
ཆོས་དང་བདེ་དང་སྲིད་རྣམས་མཐུན་ལགས་སམ། ། ཞེས་བྱ་བ་འདི་ཡང་བརྩོན་འགྲུས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་དབང་དུ་བྱས་པ་སྟེ། ཆོས་དང་བདེ་དང་སྲིད་རྣམས་མཐུན་ལགས་སམ། །ཞེས་བྱ་བ་ནི་རྒྱལ་པོའི་འཁོར་གསུམ་གཙོ་བོ་ཡིན་པའི་ཕྱིར། བརྩོན་འགྲུས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་མཐུན་པར་གྱུར་པའི་སྤྱོད་པ་སྟོན་པ་ཡིན་ནོ། །

[Block 4061]
ཤུགས་འབྱིན་སྨོད་པར་འགྱུར་ལགས་སམ། །ཞེས་བྱ་བ་ནི་དེའི༌[^2623]ཡོན་ཏན་ཐོས་ན་མཁས་པའི་ཕྱིར་རོ། །

[Block 4062]
[^2624]མི་བཟོད་པ་ཡིན་པས། ཤུགས་འབྱིན་པ་ཡིན་ཏེ༌[^2625]སྨོད་པར་འགྱུར་རོ། །ཞེས་སྟོན་ཏོ། །

[Block 4063]
དི་རིང་བདག་ཀྱང་བདེ་ཞེས་བྱ་བ་ནི་ཅིའི་ཕྱིར་ཞེ་ན། ཕྲད་པས་ཡུན་རིང་པོར་བསམས་པ་འབྱོར་ཅིང་ཐོབ་པའི་ཕྱིར་རོ། །

[Block 4064]
ཐམས་ཅད་དུ་ཡང་བདེ་ཞེས་བྱ་བ་ཡང་དེ་དང་ཕྲད་པས་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 4065]
ངང་པ་དེ་རིང་བདག་ཀྱང་བདེ། །ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་ནི་སྔར་བཤད་པའི་དྲི་བ་མཐའ་དག་གི་ལན་ཡིན་ནོ། །
--- END BLOCKS ---
