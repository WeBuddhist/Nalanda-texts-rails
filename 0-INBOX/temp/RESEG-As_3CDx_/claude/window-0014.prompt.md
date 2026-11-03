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
[Block 491 [HEADING]]
###### རྒྱུ་ཕུན་སུམ་ཚོགས་པ། ^3-2-3-1-5-0

[Block 492]
དེའི་འོག་ཏུ་རྒྱུ་ཕུན་སུམ་ཚོགས་པ་བསྟན་པའི་དབང་དུ་མཛད་ནས། མང་དུ་ཐོས་པ། ཐོས་པ་འཛིན་པ། ཐོས་པ་བསགས་པ་ཞེས་བྱ་བ་གསུངས་ཏེ། དེ་ལ་མང་དུ་ཐོས་པ་ཞེས་བྱ་བ་ནི་སྡེ་སྣོད་གསུམ་ལས་བརྩམས་པ་སྟེ་གཞུང་དུ་མ་དག་མགོ་མཇུག་ཆུབ་པར༌[^374]ཉན་ཅིང་གཟུང་བའི་ཕྱིར་རོ། །

[Block 493]
ཐོས་པ་འཛིན་པ༌[^375]ཞེས་བྱ་བས་ནི་དེ་དག་གི་དོན་འཛིན་པ་སྟེ། ཐོས་པའི་དོན་ཀུན་འཛིན་པའི་ཕྱིར་རོ། །

[Block 494]
ཐོས་པ་བསགས་པ་ཞེས་བྱ་བ་ནི་དེ་གཉི་གའི༌[^376]དོན་སྟོན་པར༌[^377]བྱེད་པའི་ཕྱིར་རོ། །

[Block 495]
དེ་ལྟར་སྡེ་སྣོད་གསུམ་ལས་བརྩམས་ཏེ། མང་དུ་ཐོས་པ་དང་། ཐོས་པ་འཛིན་པ་དང་། ཐོས་པ་བསགས་པའི་བློ་རྒྱ་ཆེ་བ་ཡིན་པས་ན་དེའི་ཕྱིར་རྒྱུ་ཕུན་སུམ་ཚོགས་པ་ཞེས་བྱའོ། །

[Block 496 [HEADING]]
###### མཐུན་པའི་ལམ་དུ་འགྲོ་བ་ཕུན་སུམ་ཚོགས་པ། ^3-2-3-1-6-0

[Block 497]
དེའི་འོག་ཏུ་མཐུན་པའི་ལམ་དུ་འགྲོ་བ་ཕུན་སུམ་ཚོགས་པ་བསྟན་པའི་དབང་དུ་མཛད་ནས། ལེགས་པར་བསམ་པ་སེམས་པ། ལེགས་པར་སྨྲ་བ་བརྗོད་པ། ལེགས་པར་བྱ་བའི་ལས་བྱེད་པ་ཞེས་གསུངས་ཏེ། བྱིས་པ་རྣམས་ནི་ཡིད་ཀྱི་ཉེས་པར་སྤྱོད་པ་གསུམ་དང་། ངག་གི༌[^378]ཉེས་པར༌[^379]སྤྱོད་པ་བཞི་དང་། ལུས་ཀྱི་ཉེས་པར༌[^380]དགག་པ་གསུམ་སྤྱོད་པས། ཉེས་པར་བསམ་པ་སེམས་པ། ཉེས་པར་སྨྲ་བ་བརྗོད་པ། ཉེས་པར་བྱེད་པའི་ལས་བྱེད་པ་ཡིན་པའི་ཕྱིར་ངན་འགྲོ་དང་འཁོར་བའི་རྒྱུད་དུ་འགྲོ་བ་ཡིན་གྱི། འཕགས་པ་རྣམས་ནི་དེ་ལས་བཟློག་པ༌[^381]ཡིན་པའི་ཕྱིར་མངོན་པར་མཐོ་བ་དང་། ངེས་པར་ལེགས་པའི་ལམ་དང་མཐུན་པར་གཤེགས་པས་ན་དེའི་ཕྱིར༌[^382]མཐུན་ལམ་དུ་འགྲོ་བ་ཕུན་སུམ་ཚོགས་པ་ཞེས་བྱའོ། །

[Block 498 [HEADING]]
###### མྱུར་བ་ཉིད་ཕུན་སུམ་ཚོགས་པ། ^3-2-3-1-7-0

[Block 499]
དེའི་འོག་ཏུ་མྱུར་བ་ཉིད་ཕུན་སུམ་ཚོགས་པ་བསྟན་པའི་དབང་དུ་མཛད་ནས། ཤེས་རབ་མྱུར་བ། ཤེས་རབ་མགྱོགས་པ། ཤེས་རབ་རྣོ་བ། ངེས་པར་འབྱུང་བའི་ཤེས་རབ་ཅན། ངེས་པར་རྟོགས་པའི་ཤེས་རབ་ཅན། ཤེས་རབ་ཆེ་བ། ཤེས་རབ་ཡངས་པ། ཤེས་རབ་ཟབ་པ། ཤེས་རབ་མཉམ་པ་མེད་པ། ཤེས་རབ་རིན་པོ་ཆེ་དང་ལྡན་པ་ཞེས་བྱ་བ་གསུངས་ཏེ། དེ་ལ་ཤེས་རབ་མྱུར་བ་ཞེས་བྱ་བ༌[^383]ནི་དེ་བཞིན་གཤེགས་པས་གསུངས་པའི་ཆོས་འདུལ་བའི་དོན་ལ་མྱུར་དུ་འཇུག་པའི་ཕྱིར་རོ། །ཤེས་རབ་མགྱོགས་པ་ཞེས་བྱ་བ་ནི་དེ་དག་ཉིད་ཀྱི་དོན་མང་པོ་ལ་འཇུག་པའི་ཕྱིར་ཏེ། མང་པོ་ལ་འགྲོ་བ་ནི་མགྱོགས་པ་ཞེས་བྱའོ། །ཤེས་རབ་རྣོ་བ་ཞེས་བྱ་བ་ནི་དོན་ཆ་ཕྲ་བ་ལ་འཇུག་པའི་ཕྱིར་རོ། །

[Block 500]
ངེས་པར་འབྱུང་བའི་ཤེས་རབ་ཅན་ཞེས་བྱ་བ་ནི་འཁོར་བ་ལས་ངེས་པར་འབྱུང་བའི་ཤེས་རབ་ཟག་པ་མེད་པ་ཐོབ་པའི་ཕྱིར་རོ། །

[Block 501]
ངེས་པར་རྟོགས་པའི་ཤེས་རབ་ཅན་ཞེས་བྱ་བ་ནི་མྱ་ངན་ལས་འདས་པའི་དགོས་པ་དང་ལྡན་པའི་ཕྱིར་ཏེ། ངེས་པར་རྟོགས་པ་ནི་གཏན་ལ་བབ་པར་རྟོགས་པ་དེ༌[^384]མྱ་ངན་ལས་འདས་པ་ཡིན་ནོ། །

[Block 502]
དེའི་དགོས་པ༌[^385]དང་ལྡན་པའི་ཤེས་རབ་ནི་ངེས་པར་རྟོགས་པའི་ཤེས་རབ་སྟེ། དེ་གང་ལ་ཡོད་པའི་གང་ཟག་ནི་ངེས་པར་རྟོགས་པའི་ཤེས་རབ་ཅན་ཞེས་བྱའོ། །ཤེས་རབ་ཆེ་བ་ཞེས་བྱ་བ་ནི་དྲིས་པ་ལན་གདབ་པ་ལ་མཐའ་ཐུག་པ་མེད་པའི་ཕྱིར་རོ། །ཤེས་རབ་ཡངས་པ་ཞེས་བྱ་བ་ནི་མངོན་པར་ཤེས་པ་རྒྱ་ཆེན་པོ་ཡོངས་སུ་རྫོགས་པའི་ཕྱིར་རོ། །ཤེས་རབ་ཟབ་པ་ཞེས་བྱ་བ་ནི་གཞན་དག་གིས་གཏིང་དཔག་དཀའ་བའི་ཕྱིར་རོ། །ཤེས་རབ་མཉམ་པ་མེད་པ་ཞེས་བྱ་བ་ནི་ཉན་ཐོས་དབང་པོ་རྟུལ་པོ་དག་ལས་ཁྱད་པར་དུ་འཕགས་པའི་ཕྱིར་རོ། །ཤེས་རབ་རིན་པོ་ཆེ་དང་ལྡན་པ་ཞེས་བྱ་བ་ནི་དོན་གྱི་མཆོག་ཐོབ་པར་བྱེད་པས་རིན་པོ་ཆེ་དང་འདྲ་བའི་ཕྱིར་རོ། །

[Block 503]
དེ་ལྟར་ཤེས་རབ་མྱུར་བ་ལ་སོགས་པ་འཕགས་པ་ཉན་ཐོས་ཀྱི་ཤེས་རབ་རྣམ་པ་བཅུ་པོ་དེ་དག་དང་ལྡན་པ་ནི་མངོན་པར་ཤེས་པ་མྱུར་བ་ཡིན་པས་ན་དེའི་ཕྱིར་མྱུར་བ་ཉིད་ཕུན་སུམ་ཚོགས་པ་ཞེས་བྱའོ། །

[Block 504 [HEADING]]
###### རིང་དུ་འགྲོ་བ་ཕུན་སུམ་ཚོགས་པ། ^3-2-3-1-8-0

[Block 505]
དེའི་འོག་ཏུ་རིང་དུ་འགྲོ་བ་ཕུན་སུམ་ཚོགས་པ་བསྟན་པའི་དབང་དུ་མཛད་ནས། རིག་པ་གསུམ་དང་ལྡན་པ་ཞེས་བྱ་བ་གསུངས་ཏེ། རིག་པ་གསུམ་དང་ལྡན་པ་ནི་མི་སློབ་པའི་རིག་པ་གསུམ་ཐོབ་པའི་ཕྱིར་ཏེ། མི་སློབ་པའི་རིག་པ་གསུམ་ནི་སྔོན་གྱི་གནས་རྗེས་སུ་དྲན་པའི་ཤེས་པ་མངོན་དུ་བྱ་བའི་མངོན་པར་ཤེས་པའི་རིག་པ་དང་། འཆི་འཕོ་བ༌[^386]དང་སྐྱེ་བ་ཤེས་པ་མངོན་དུ་བྱ་བའི་མངོན་པར་ཤེས་པའི་རིག་པ༌[^387]དང་། ཟག་པ་ཟད་པ་ཤེས་པ་མངོན་དུ་བྱ་བའི་མངོན་པར་ཤེས་པའི་རིག་པའོ། །

[Block 506]
དེ་ལྟར་མི་སློབ་པའི་རིག་པ་གསུམ་གྱིས་སྔོན་དང་ཕྱི་མའི་མཐའ་དང་ཟག་པ་དང་བཅས་པ་དང་ཟག་པ་མེད་པའི་ཆོས་ཐམས་ཅད་ཀྱི་གཏིང་སླེབས་པར་འགྱུར་བས་ན་དེའི་ཕྱིར་རིང་དུ་འགྲོ་བ་ཕུན་སུམ་ཚོགས་པ་ཞེས་བྱའོ། །

[Block 507 [HEADING]]
###### འགྲོ་བ་བཟང་པོ་ཕུན་སུམ་ཚོགས་པ། ^3-2-3-1-9-0

[Block 508]
དེའི་འོག་ཏུ་འགྲོ་བ་བཟང་པོ་ཕུན་སུམ་ཚོགས་པ་བསྟན་པའི་དབང་དུ་མཛད་ནས། ཚེ་འདི་ལ་བདེ་བར༌[^388]གནས་པའི་མཆོག་ཐོབ་པ་ཞེས་བྱ་བ་གསུངས་ཏེ། ཚེ་འདི་ལ་བདེ་བར་གནས་པ་ནི་བསམ་གཏན་གྱི་དངོས་གཞི་ཡོངས་སུ་དག་པ་ལ་གནས་པའོ། །

[Block 509]
དེ་དག་གི་མཆོག་ཐོབ་པ་ནི་ཡོངས་སུ་མི་ཉམས་པའི་བསམ་གཏན་དང་འགོག་པའི་སྙོམས་པར་འཇུག་པ་ཐོབ་པའོ། །

[Block 510]
དེ་ལྟར་བསམ་གཏན་གྱི་དངོས་གཞི་དང་འགོག་པའི་སྙོམས་པར་འཇུག་པ་ཐོབ་པ་ནི་ཚེ་འདི་ལ་བདེ་བར་གནས་པའི་བགྲོད་པ་ཡིན་པས་ན་དེའི་ཕྱིར་འགྲོ་བ་བཟང་པོ་ཕུན་སུམ་ཚོགས་པ་ཞེས་བྱའོ། །

[Block 511 [HEADING]]
###### ཡོངས་སུ་སྤྱོད་པ་ཕུན་སུམ་ཚོགས་པ། ^3-2-3-1-10-0

[Block 512]
དེའི་འོག་ཏུ་ཡོངས་སུ་སྤྱོད་པ་ཕུན་སུམ་ཚོགས་པ་བསྟན་པའི་དབང་དུ་མཛད་ནས། ཡོན་ཡོངས་སུ་སྦྱོང་བ་ཆེན་པོ་བྱ་བ་གསུངས་ཏེ། གང་ཟག་ཚུལ་ཁྲིམས་འཆལ་པ་ཡོན་ཏན་དང་མི་ལྡན་པས་དད་པས་སྦྱིན་པ་ཡོངས་སུ་ལོངས་སྤྱད་པ་ནི་བུ་ལོན་དུ་གྱུར་པ་ཡིན་ལ། གང་ཟག་ཚུལ་ཁྲིམས་དང་ལྡན་པ་ཡོན་ཏན་གྱིས་ཡོངས་སུ་ལོངས་སྤྱོད་པ་ནི་སྤྱོད་དུ་དབང་བ་ཡིན་ན་ཡང་འབྲས་བུ་མྱུར་དུ་སྐྱེད་པ་མ་ཡིན་གྱི། འཇིག་རྟེན་གསུམ་གྱི་འདོད་ཆགས་དང་བྲལ་བ་དགྲ་བཅོམ་པ་རི་རབ་དང་འདྲ་བ་འདི་དག་ལ་ནི་ལྷ་དང་བཅས་པའི་འཇིག་རྟེན་ཀུན་གྱི་བདེ་བའི་ཡོ་བྱད་ཐམས་ཅད་ཀྱིས་བསྙེན་བཀུར་བྱས་ན་ཡང་། ཞིང་གཤིན་པ་དང་འདྲ་བར་འབྲས་བུ་བཟང་པོར་མྱུར་དུ་འགྲུབ་པའི་ཕྱིར་ཡོན་ཡོངས་སུ་སྤྱོད་པ་ཆེན་པོ་ཡིན་ནོ། །

[Block 513]
དེ་ལྟར་བདག་ཉིད་ལ་བུ་ལོན་དུ་མི་འགྱུར་ལ་སྦྱིན་བདག་ལ་ཡང་འབྲས་བུ་མྱུར་ཞིང་བཟང་བའི་ཕྱིར། ཞིང་གཤིན་པ་ལྟ་བུ་ཡིན་པས་ན་དེའི་ཕྱིར་ཡོངས་སུ་སྤྱོད་པ་ཕུན་སུམ་ཚོགས་པ་ཞེས་བྱའོ། །

[Block 514 [HEADING]]
###### ཉེ་བར་ཞི་བ་ཕུན་སུམ་ཚོགས་པ། ^3-2-3-1-11-0

[Block 515]
དེའི་འོག་ཏུ་ཉེ་བར་ཞི་བ་ཕུན་སུམ་ཚོགས་པ་བསྟན་པའི་དབང་དུ་མཛད་ནས། སྤྱོད་ལམ་རབ་ཏུ་ཞི་བ་ཕུན་སུམ་ཚོགས་པ་ཞེས་བྱ་བ་གསུངས་ཏེ། འགྲོ་བ་དང་། སྡོད་པ༌[^389]དང་། འདུག་པ་དང་། ཉལ་བ་ལ་སོགས་པ་སྤྱོད་ལམ་ཐམས་ཅད་དུ་ཤེས་བཞིན་དུ་སྤྱོད་པ་གང་ཡིན་པ་དེ་ནི་སྤྱོད་ལམ་རབ་ཏུ་ཞི་བ་དང་ལྡན་པ་ཡིན་ནོ། །

[Block 516]
དེ་ལྟར་སྤྱོད་ལམ་ཐམས་ཅད་དུ་ཤེས་བཞིན་དུ་སྤྱོད་པ་ནི་ཚུལ་ཞི་བ་དང་ལྡན་པ་ཡིན་པས་ན་དེའི་ཕྱིར་ཉེ་བར་ཞི་བ་ཕུན་སུམ་ཚོགས་པ་ཞེས་བྱའོ། །

[Block 517 [HEADING]]
###### འགྲོགས་ན་བདེ་བ་ཕུན་སུམ་ཚོགས་པ། ^3-2-3-1-12-0

[Block 518]
དེའི་འོག་ཏུ་འགྲོགས་ན་བདེ་བ་ཕུན་སུམ་ཚོགས་པ་ཞེས་བྱ་བ་བསྟན་པའི་དབང་དུ་མཛད་ནས། བཟོད་པ་དང་དེས་པ་ཆེན་པོ་དང་ལྡན་པ་ཞེས་བྱ་བ་གསུངས་ཏེ། སྡུག་བསྔལ་ཇི་སྙེད་སྙམ་པའི་བཟོད་པ་ཆེན་པོ་དང་། བཀའ་བློ་བདེ་བའི་དེས་པ་ཆེན་པོ་དང་ལྡན་པ་ནི་བཟོད་པ་དང་དེས་པ་ཆེན་པོ་དང་ལྡན་པ་ཡིན་ནོ། །

[Block 519]
དེ་ལྟར་བཟོད་པ་དང་དེས་པ་ཆེན་པོ་དང་ལྡན་པ་ནི་བསྟེན་པར་བྱ་བའི་འོས་ཡིན་པས་ན། དེའི་ཕྱིར་འགྲོགས་ན་བདེ་བ་ཕུན་སུམ་ཚོགས་པ་ཞེས་བྱའོ། །

[Block 520 [HEADING]]
###### དབང་དུ་གྱུར་པ་ཕུན་སུམ་ཚོགས་པ། ^3-2-3-1-13-0

[Block 521]
དེའི་འོག་ཏུ་དབང་དུ་གྱུར་པ་ཕུན་སུམ་ཚོགས་པ་བསྟན་པའི་དབང་དུ་མཛད་ནས། དེ་བཞིན་གཤེགས་པའི་བཀའ་ལ་ཤིན་ཏུ་ཞུགས་པ་ཞེས་བྱ་བ་གསུངས་ཏེ། བསླབ་པ་དག་ལ་ཡོངས་སུ་རྫོགས་པར་བྱེད་པའི་ཕྱིར་དེ་བཞིན་གཤེགས་པའི་བཀའ་མི་འགལ་བར་སྤྱོད་པས་ན་བཀའ་ལ་ཤིན་ཏུ་ཞུགས་པ་ཡིན་ནོ། །

[Block 522]
དེ་ལྟར་དེ་བཞིན་གཤེགས་པའི་བཀའ་ལ་ཤིན་ཏུ་ཞུགས་པ་ནི་ཉོན་མོངས་པ་གཞན་གྱི་དབང་དུ་མི་འགྱུར་བའི་ཕྱིར་བསླབ་པ་དག་ལ་བག་ཡངས་སུ་སྤྱོད་པ་ཡིན་པས་ན། དེའི་ཕྱིར་དབང་དུ་གྱུར་པ་ཕུན་སུམ་ཚོགས་པ་ཞེས་བྱའོ། །

[Block 523]
ཤ་སྟག་དང་ཞེས༌[^390]བྱ་བ་ནི་ཉན་ཐོས་ཀྱི་འཁོར་ཕུན་སུམ་ཚོགས་པ་ཡོན་ཏན་ཚད་མེད་པ་དེ་ལྟ་བུ་དང་ལྡན་པ་གྲངས་ཚད་མེད་པ་ཤ་སྟག་དང་། བྱང་ཆུབ་སེམས་དཔའི་འཁོར་ཕུན་སུམ་ཚོགས་པ་དང་ཡང་ཐབས་ཅིག༌[^391]གོ་ཞེས་ཚིག་འོག་མ་དང་སྦྱར་རོ། །

[Block 524]
ཉན་ཐོས་ཀྱི་འཁོར་ཕུན་སུམ་ཚོགས་པའི་ཚིག་གི་དོན་ལ་སོགས་པ་བཤད་ཟིན་ཏོ།། །།

[Block 525 [HEADING]]
##### བྱང་ཆུབ་སེམས་དཔའི་འཁོར་ཕུན་སུམ་ཚོགས་པ། ^3-2-3-2-0

[Block 526]
དེ་ལྟར་ཉན་ཐོས་ཀྱི་འཁོར་ཕུན་སུམ་ཚོགས་པ་བསྟན་ནས། དེའི་འོག་ཏུ་བྱང་ཆུབ་སེམས་དཔའི་འཁོར་ཕུན་སུམ་ཚོགས་པ་བསྟན་པའི་དབང་དུ་མཛད་ནས། [^392]སངས་རྒྱས་ཀྱི་ཞིང་ཐ་དད་པ་ནས་འདུས་པའི་བྱང་ཆུབ་སེམས་དཔའ་དཔག་ཏུ་མེད་པ་ཐམས་ཅད་ཀྱང་གནས་ཆེན་པོ་ལ་ཡང་དག་པར་ཞུགས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 527]
དེ་ལ་བྱང་ཆུབ་སེམས་དཔའི་ཡོན་ཏན་བསྟན་པའི་དགོས་པ་ནི་དེ་དག་ལ་ཁ་ཅིག་བརྙས་པ་བཟློག་པའི་ཕྱིར་ཏེ། ཉན་ཐོས་ཡུན་རིང་དུ་ཚངས་པར་སྤྱད་པ་རྣམས་ཀྱིས་བྱང་ཆུབ་སེམས་དཔའ་དག་ལ་གདུང་བར་བྱའོ་ཞེས་གསུངས་པའི་ཕྱིར་དང་། ཁ་ཅིག་བྱང་ཆུབ་སེམས་དཔའ་དག་ཀྱང་ཡོན་ཏན་དེ་ལྟ་བུ་དང་ལྡན་པ་ཡིན་ན། དེ་བཞིན་གཤེགས་པ་ལྟ་སྨོས་ཀྱང་ཅི་དགོས་སྙམ་དུ་དད་པ་བསྐྱོད་པའི་ཕྱིར་རོ། །

[Block 528 [HEADING]]
###### ཆེན་པོ་རྣམ་པ་གསུམ། ^3-2-3-2-1-0

[Block 529]
དེ་ལ་བྱང་ཆུབ་སེམས་དཔའི་ཕུན་སུམ་ཚོགས་པ་ནི་ཆེན་པོ་རྣམ་པ་གསུམ་གྱིས་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ཆེན་པོ་བརྗོད་དེ། གྲངས་ཆེན་པོ་དང་། ཡོན་ཏན་ཆེན་པོ་དང་། ལས་ཆེན་པོས་སོ། །

[Block 530 [HEADING]]
###### **གྲངས་ཆེན་པོ།** ^3-2-3-2-1-1-0
--- END BLOCKS ---
