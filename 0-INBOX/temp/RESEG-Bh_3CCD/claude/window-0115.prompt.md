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
འདི་གསལ་བ་ལས་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་འོད་གསལ་བ་ལས་བྱུང་བའོ། །

[Block 4027]
ཡོངས་སུ་དག་པའི་ལྷའི་སྐུ་འཛིན་པའི་མཚན་ཉིད་ནི༌[^2494]ཐ་མལ་པའི་ཕུང་པོ་ལ་སོགས་པ་ལྡོག་པའི་མཚན་ཉིད་རྡོ་རྗེ་འཆང་གི་ཕྱག་རྒྱ་ཆེན་པོའི་སྐུ་རྫོགས་པའོ། །

[Block 4028]
བཞེངས་པ་ཞེས་བྱ་བ་ནི་དེ་ཉིད་དཀྱིལ་འཁོར་མ་ལུས་པ་སྤྲུལ་པར་བྱེད་པའོ། །

[Block 4029]
གང་གིས་རབ་ཏུ་སྒྲོགས་ཤིང་བརྗོད་པ་ཞེས་ངོ་མཚར་བའོ། །

[Block 4030]
དགོངས་པ་མ་ཡིན་པ་ཞེས་བྱ་བ་ནི་བསྐྱེད་པའི་རིམ་པའི་ཡན་ལག་ཏུ་གྱུར་པའི་དོན་དམ་པའི་དཀྱིལ་འཁོར་དང་དེ་ལས་བྱུང་བའི་དག་པའི་སྐུ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 4031]
ཚིགས་སུ་བཅད་པ་དེ་ཉིད་ཀྱང་བཤད་པར་བྱ་སྟེ། དོན་དམ་པའི་བདེན་པའོ་ཞེས་པ་ནི་སེམས་རྣམ་པར་དག་པའི་རིམ་པས་ཐོབ་པར་བྱ་བའི་འོད་གསལ་བའོ། །

[Block 4032]
དེར་ཡིད་ཀྱི་རང་བཞིན་གྱི་ལུས་འཇུག་པ་ནི་ཅིག་ཅར་དུ་སྤྲོས་པས་འཇའ་ཚོན་དང་འདྲ་བའི་སྐུ་མངོན་པར་བྱང་ཆུབ་པའི་རིམ་པའི་མཚན་ཉིད་ཀྱི་འོད་གསལ་བའི་དེ་ཁོ་ན་ཉིད་དང་གཅིག་ཏུ་གྱུར་པའོ། །

[Block 4033]
འོད་གསལ་བ་ལས་ནི་མན་ངག་བཞི་པ་ལས་ཡོངས་སུ་དག་པའི་ལྷའི་སྐུ་འཛིན་པའི་མཚན་ཉིད་ཅེས་པ་ནི་ཇི་སྲིད་འཁོར་བའི་བར་དུ་འགྲོ་བའི་དོན་མཛད་པར་བྱ་བའི་ཕྱིར་ཅིག་ཅར་དུ་འབྱུང་བའི་རྣམ་པ་སྣ་ཚོགས་པའི་སྤྲུལ་པ་རྣམས་ཀྱིས་ནམ་མཁའི་དབྱིངས་ཁྱབ་པ་སྲིད་པ་དང་ཞི་བ་རོ་གཅིག་པའི་མཚན་ཉིད་དབྱིག་སྙིང་ལ་སོགས་པའི་ལྷའི་མཆོག་གི༌[^2495]ཞབས་ཀྱི་པདྨ་མཆོད་པར་བྱ་བ་རྣམ་པ་ཐམས་ཅད་ཀྱི་མཆོག་དང་ལྡན་པ་མཚན་དང་དཔེ་བྱད་ཀྱིས་རྣམ་པར་མཛེས་པ་ཕྱག་རྒྱ་ཆེན་པོའི་རང་བཞིན་མི་གནས་པའི་མྱ་ངན་ལས་འདས་པའི་དབྱིངས་ཞེས་བྱ་བ་ཆོས་ཀྱི་དབྱིངས་ཀྱི་ཡེ་ཤེས་ཀྱི་རྣམ་གྲངས་ཤེས་པ་དང་ཤེས་བྱའི་བག་ཆགས་དང་བྲལ་བ་འོད་ཀྱི་ཚོགས་ཀྱིས་ཟླ་བ་དང་ཉི་མའི་གཟི་བརྗིད་ཟིལ་གྱིས་གནོན་པ་ཟུང་དུ་འཇུག་པའི་ཏིང་ངེ་འཛིན་རྡོ་རྗེའི་སྐུའི་མཚན་ཉིད་འཛིན་པ་ནི་དམིགས་པར་བྱའོ། །

[Block 4034]
བཞེངས་པ་འདི་ནི་ཞེས་པ་ནི་ལྡང་བའོ། །

[Block 4035]
གང་གིས་རབ་ཏུ་བསྒྲགས་ཤིང་ནི་བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་པའོ། །

[Block 4036]
དགོངས་པ་མ་ཡིན་པ་ནི༌[^2496]རིམ་པ་ཐ་མ་དེ་ཁོ་ན་ཉིད་སོ་སོར་བསྟན་པའི་ཕྱིར་རོ། །

[Block 4037]
དེ་བཞིན་གཤེགས་པ་དྲུག་ཅེས་བྱ་བ་ལ་སོགས་པས་བཅོམ་ལྡན་འདས་རྡོ་རྗེ་འཆང་ཆེན་པོའི་བཀའ་ལུང་ཐོས་པའི༌[^2497]འོག་ཏུ་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་ངོ་བོ་དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱིས་ཐོས་པ་གང་ཡིན་པ་དེ་ཉིད་བསམས་ནས་བསྒོམས་ཏེ། དེའི་དོན་སྟོན་པར་བྱེད་པ་ཚིགས་སུ་བཅད་པ་དྲུག་དྲུག་གིས་འབྱུང་བར་བསྟན་ཏོ། །

[Block 4038]
དེ་ལ་རྡོ་རྗེ་འཆང་ཆེན་པོའི་ཚིགས་སུ་བཅད་པའི་དོན་ནི་སྟོང་པ་ཉིད་ཀྱི་དེ་ཁོ་ན་ཉིད་དང་དོན་དམ་པའི་དཀྱིལ་འཁོར་གྱི་རང་བཞིན་ནོ། །

[Block 4039]
གཞན་རྣམས་ཀྱི་དོན་ནི་རྡོ་རྗེ་བཟླས་པ་ལ་སོགས་པ་སྟེ་རྫོགས་པའི་རིམ་པའོ། །

[Block 4040]
ཚིགས་སུ་བཅད་པ་བརྗོད་པའི་སྔོན་དུ་དེ་དང་རྗེས་སུ་མཐུན་པའི་ཏིང་ངེ་འཛིན་རྣམས་བསྟན་པའི་ཕྱིར། བདེན་པ་གཉིས་གཉིས་སུ་མེད་པའི་མཚན་ཉིད་ཅེས་པ་ནི་ཟུང་དུ་འཇུག་པའི་ཏིང་ངེ་འཛིན་ནོ། །

[Block 4041]
དེ་མངོན་དུ་བྱ་བའི་ཐབས་ཞེས་པ་ལ། རིམ་པ་བཞི་པ་བསྒོམ་པའི་མཚན་ཉིད་དོ། །

[Block 4042]
གང་གི་ཕྱིར་རིམ་པ་བཞི་པས་རིམ་པ་ལྔ་པ་ཐོབ་པར་འགྱུར་ཞེས་པའི་དོན་ཏོ། །

[Block 4043]
དགོངས་པ་མ་ཡིན་པ་ཞེས་པ་ནི་འབྲས་བུར་གྱུར་པའི་དེ་ཁོ་ན་ཉིད་བསྟན་པས་སོ། །

[Block 4044]
དེ་ཉིད་བསྟན་པར་བྱ་བའི་ཕྱིར་བརྟན་པ་དང་གཡོ་བ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། འདི་ལྟར་སྣང་བར་གྱུར་པ་བརྟན་པ༌[^2498]དང་གཡོ་བའི་བདག་ཉིད་འདི་ཡོད་པ་མ་ཡིན་ཏེ། གཅིག་དང་དུ་མས་བྲལ་བ་དེ་མི་དམིགས་པའི་ཕྱིར་གཟུགས་བརྙན་བཞིན་ནོ་ཞེས་ཁྱབ་པར་བྱེད་པ་མི་དམིགས་པས་སོ། །

[Block 4045 [VERSE]]
དེའི་ཕྱིར་དངོས་པོ་རྣམས་མེད་དོ། །
བསྒོམ་པར་བྱ་བ་མེད་པའི་ཕྱིར། །

[Block 4046]
ཞེས་པ་ནི་ཤེས་བྱའི་ཡུལ་ཅན་གྱི་སྒོམ་པ་ཡང་མེད་དོ། །

[Block 4047]
ཡང་ན། འགྲོ་བའི་དངོས་པོ་ཐམས་ཅད་འདི། མ་བརྟགས་པ་ལ་ཉམས་དགའ་བ། །ཞེས་འབྱུང་བས་སོ། །

[Block 4048]
[^2499]གང་གི་ཚེ་མི་དམིགས་པའི་སྦྱོར་བས་མི་སྤྱོད་དོ། །

[Block 4049]
འོན་ཀྱང་ཇི་ལྟར་སྣང་བ་ཙམ་ཡུལ་ཉིད་དུ་འདོད་པ་དེའི་ཚེ་དངོས་པོ་དེ་རྣམས་ཡོད་པ་ལྟར་སྣང་ངོ་ཞེས་འདོད་ན། དེ་ལ་སྨྲས་པ། གང་ཡོད་པར་སྒོམ་པ་ཞེས་པ་ནི་ཡོངས་སུ་བརྟགས་པའི་ཚུལ་དུ་སྣང་བར་གྱུར་པའི་དངོས་པོའི་སྒོམ་པ་གང་ཡིན་པ་དེ་ནི་རྗེས་སུ་དྲན་པའམ་འཇོག་པ་ཉིད་གང་ཡིན་པ་དེ་ཡང་མི་རིགས་ཏེ། སྒོམ་པ་མེད་པས་ཀྱང་ཡོད་པའི་ཕྱིར་རོ། །

[Block 4050]
དེའི་དགོངས་པ་ནི་གང་བརྟགས་པའི་དངོས་པོ་འདི་ཡིན་པ་དེ་རང་ལས་གྲུབ༌[^2500]ན་རང་ལས་གྲུབ་པ་ནི་གཞན་ལ་རག་མ་ལས་པས་སྒོམ་པ་མི་དགོས་སོ། །

[Block 4051]
ཡང་ན་གཞན་ལས་གྲུབ་པའི་དངོས་པོ་ཞེས་བརྗོད་ན་དེའི་ཚེ་དེ་ནི་ཡོད་པར་མི་བརྗོད་དེ་རྟེན་ཅིང་འབྲེལ་པ་ལས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 4052]
ཇི་སྐད་དུ།

[Block 4053 [VERSE]]
དེ་དེ་རྟེན་ནས་གང་བྱུང་བ། །
དེ་ཉིད་ཀྱིས་ནི་དེ༌[^2501]མ་སྐྱེས། །
ངོ་བོ་ཉིད་ཀྱིས་མ་སྐྱེས་གང་། །
དེ་ནི་སྐྱེ་ཞེས་ཇི་ལྟར་ཡིན། །

[Block 4054]
ཞེས་འབྱུང་ངོ་། །དེ་བས་ན་གཞན་ལས་གྲུབ་པའི་ཕྱོགས་སུ་ཡང་བསྒོམ་པ་ནི་དགོས་པ་མ་ཡིན་ནོ། །

[Block 4055]
གལ་ཏེ་མི་དམིགས་པའི་སྦྱོར་བས་དངོས་པོ་མེད་པར་གྲུབ་པ༌[^2502]དང་དེ་ནས་ཡོད་པའི་བསྒོམ་པ་བཀག་ནས་བསྒོམ་པ་ཡང་མེད་དོ་ཞེས་དགོངས་ན། དེའི་ཕྱིར་ཡོད་པ་དང་མེད་པར་འདྲེས་པའི་དངོས་པོ་ཁ་ཅིག་ཡོད་དེ་ཞེས་དགག་པར་བྱ་བའི་ཕྱིར། དངོས་པོ་མེད་པ་དང་ཡོད་པར་འདོད་པས་ལྡན་པ་ཞེས་བྱ་བ་ནི་དངོས་པོ་ཡིན་ན་རང་དང་རྗེས་སུ་མཐུན་པའི་ཚོགས་པ་ལས་བདག་ཉིད་རྙེད་པ་དོན་གྱི་བྱ་བ་བྱེད་པ་ཡིན་པ་དེས་དངོས་པོ་ཐམས་ཅད་ཀྱི་ནུས་པ་དང་བྲལ་བའི་མཚན་ཉིད་ནམ་ཡང་མེད་པའི་ཕྱོགས་སུ་མི་འགྱུར་རོ། །

[Block 4056]
དངོས་པོ་མེད་པ་ཡང་རི་བོང་གི་རྭ་དང་འདྲ་བ་དོན་གྱི་བྱ་བ་བྱེད་པའི་ནུས་པ་དང་བྲལ་བ་བརྗོད་པར་མི་ནུས་པས་ཇི་ལྟར་དངོས་པོའི་གནས་འཐོབ་པར༌[^2503]འགྱུར་ཏེ་ཕན་ཚུན་སྤངས་པའི་མཚན་ཉིད་ཅན་གྱི་འགལ་བ་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 4057]
དེ་ཉིད་ཀྱི་ཕྱིར་དངོས་པོ་ཡང་ཡིན་ལ། དངོས་པོ་མེད་པ་ཡང་ཡིན་ཞེས་གཅིག་ཏུ་གཉི་གའི་ཐ་སྙད་མི་རིགས་སོ། །

[Block 4058]
འོ་ན་དངོས་པོ་ཉིད་དང་སྐད་ཅིག་མ་དང་ཕན་ཚུན་འགལ་བ་ཇི་ལྟར་དངོས་པོ་གཅིག་ལ་ཡོད་པ་དེ་བཞིན་དུ་འདིར་ཡང་ཡིན་ནོ་ཞེ་ན། སྨྲས་པ། དངོས་པོ་ཉིད་དང་སྐད་ཅིག་མ་ཉིད་ནི་དངོས་པོ་གཉིས་ནི༌[^2504]འཐད་དེ། འོན་ཀྱང་སྐད་ཅིག་མ་ཉིད་གང་ཡིན་པ་དེ་ཉིད་དངོས་པོ་ཉིད་དོ། །

[Block 4059]
བརྟན་པ་ནི་དངོས་པོར་སྨྲ་བས་འདྲ་བ་གཞན་དང་གཞན་སྐྱེད་པས་སླུ་བའི༌[^2505]བློ་དང་ལྡན་པ་དངོས་པོ་བརྟན་པ་གཅིག༌[^2506]འདི་ཡིན་ནོ་ཞེས་སེམས་སོ། །

[Block 4060]
ཐོ་བ་ལ་སོགས་པ་འཇིག་པའི་རྒྱུ་དང་ཕྲད་པའི་དུས་སུ་རྨུགས་པའི་བློ་དང་ལྡན་པས་བུམ་པ་འཇིག་གོ་ཞེས་སེམས་སོ། །

[Block 4061]
དོན་དམ་པར་དེ་ནི་ཐོག་མར་འཇིག་པ་ཡིན་ཏེ། སྐད་ཅིག་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4062]
དེ་བས་ན་དངོས་པོར་སྨྲ་བ་བརྟན་པ་རྣམས་ཀྱི་འཁྲུལ་པ་བསལ་བར༌[^2507]བྱ་བའི་དོན་དུ་དངོས་པོ་ཉིད་དང་སྐད་ཅིག་མ་ཉིད་ལྡོག་པའི་དབྱེ་བས་བརྟགས་ཏེ་བསྒྲུབ་པར་བྱ་བ་དང་། སྒྲུབ་པར་བྱེད་པའི་འབྲེལ་པ་མཁས་པ་རྣམས་ཀྱིས་བྱས་སོ། །

[Block 4063]
དེ་བས་ན་འཁྲུལ་པ་ཉིད་བསལ་བར༌[^2508]བྱ་བའི་ཕྱིར་རྗེས་སུ་དཔག་པའི་ཚད་མ་བསྟན་ཏོ། །

[Block 4064]
ལྡོག་པ་མ་ལུས་པ་དང་ལྡན་པའི་རང་བཞིན་གྱི་དངོས་པོ་གཟུང་བ་ལ་མཁས་པ་མངོན་སུམ་གྱི་སྐད་ཅིག་མ་ཉིད་གཟུང་བ་ལ་ནུས་པ་མེད་དམ། འོན་ཀྱང་ངེས་པས་གང་ཞིག་ཆ་གཟུང༌[^2509]བ་མི་ནུས་པ་དེ་ལ་དེའི་ཚད་མ་ཡང་བསྟན་ཏོ། །

[Block 4065 [VERSE]]
ཆ་དང་བྲལ་བའི་ཁྱད་པར་ནི། །
མངོན་སུམ་གྱིས་ནི་གཟུང་བས་ཀྱང་། །
གང་ཞིག་ཁྱད་པར་རྟོགས་ངེས་པ། །
དེ་ནི་རྟོགས་པར་གྱུར་པ༌[^2510]ཡིན། །
--- END BLOCKS ---
