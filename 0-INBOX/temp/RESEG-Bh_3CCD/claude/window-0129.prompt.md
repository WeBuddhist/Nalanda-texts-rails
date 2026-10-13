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
[Block 4516]
དོན་དམ་པའི༌[^2731]བདེན་པའི་སྒོ་ནས་སོ་ཞེས་པ་ནི་སེམས་རྣམ་པར་དག་པ་དང་མངོན་པར་བྱང་ཆུབ་པ་བསྟན་པའི་སྒོ་ནས་སོ། །

[Block 4517]
བདེན་པ་གཉིས་མི་ཕྱེད་པའི་ཞེས་བྱ་བ་ལ་སོགས་པས་ཟུང་དུ་འཇུག་པའི་ཏིང་ངེ་འཛིན་གསལ་བར་བྱེད་པའི་མན་ངག་གི་སྒོ་ནས་བསྟོད་པའོ། །

[Block 4518]
འོད་གསལ་བའོ་ཞེས་པ་ནི་སྔགས་དང་ཕྱག་རྒྱའི་རིམ་པས་ཐོབ་པར་བྱ་བའི་སེམས་རྣམ་པར་དག་པའི་མཚན་ཉིད་དོ། །

[Block 4519]
ཡོངས་སུ་དག་པའི་ལྷའི་སྐུ་སྟེ་ཞེས་པ་ནི་དེ་ལས་བྱུང་བ༌[^2732]ཡེ་ཤེས་ཀྱི་རང་བཞིན་གྱི་སྐུའོ། །

[Block 4520]
དེས་ནི་རིམ་པ་གཉིས་ཀྱི་སྒོ་ནས་བསྟོད་པའོ། །

[Block 4521]
དོན་དམ་པའི་བདེན་པ་ལས་ཡང་དག་པར་འཁྲུངས་ཞེས་པ་ནི་རིམ་པ་བཞི་པས་ཐོབ་པར་བྱ་བའི་འོད་གསལ་བའི་དེ་ཁོ་ན་ཉིད་ལས་ཟུང་དུ་འཇུག་པ་འབྱུང་བས་སོ། །

[Block 4522]
དེས་རིམ་པ་བཞི་པ་དང་ལྔ་པ་ཞེས་བྱ་བའི་རིམ་པ་གཉིས་སོ་སོར་བསྟན་པ་ཡིན་ནོ། །

[Block 4523]
རྫོགས་པའི་རིམ་པའོ་ཞེས་པ་ནི་སྔར་བཤད་པའི་སེམས་རྣམ་པར་དག་པ་ལ་སོགས་པའི་བདག་ཉིད་དོ། །

[Block 4524]
དེས་ནི་རྫོགས་པའི་རིམ་པས་སོ། །

[Block 4525]
གདུལ་བྱ་རྣམས་བསྐྱེད་པར་མཛད་པ་ཞེས་པ་ལ་རྡོ་རྗེ་འཆང་ཆེན་པོའི་སྐུ་ཉིད་དུ་རྫོགས་པར་བྱེད་པའོ། །

[Block 4526]
དེས་ནི་རང་གིས༌[^2733]གཟིགས་པའི་དེ་ཁོ་ན་ཉིད་ཀྱི་དོན་སྟོན་པས་ན་བཅོམ་ལྡན་འདས་སྐྱོབ་པ་ཞེས་བཤད་དོ། །

[Block 4527]
རང་མཐོང་ལམ་སྟོན་སྐྱོབ་པ་ཡིན། །ཞེས་འབྱུང་ངོ་། །དེས་ན༌[^2734]རང་གི་དོན་དང་གཞན་གྱི་དོན་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 4528]
རྟོག་པ་ཐམས་ཅད་ལས་འདས་པ།[^2735] །ཞེས་པ་ལ་ཆགས་བྲལ་ལ་སོགས་པའི་རང་བཞིན་རྣམས་དང་བྲལ་བའི་ཕྱིར་རོ། །

[Block 4529]
དམིགས་སུ་མེད་པ་སྟེ་དེ་ཉིད་ཀྱི་ཁྱད་པར་རོ། །

[Block 4530]
འཁོར་བ་དང་མྱ་ངན་ལས་འདས་པ་དག་ཏུ་བཟུང་བས་ན་ཞེས་པ་ལ་མི་གནས་པའི་མྱ་ངན་ལས་འདས་པའི་དབྱིངས་ཐོབ་པའི་ཕྱིར་ཀུན་ཏུ་བཟང་པོ་ནི་རྡོ་རྗེ་འཆང་ཆེན་པོ་ཉིད་དོ། །

[Block 4531]
ཕུན་སུམ་ཚོགས་པ་ཐམས་ཅད་ཅེས་པ་ནི་རང་གི་དོན་ལ་སོགས་པ་དེའི་ངོ་བོ་ནི་དེ་ཉིད་དོ། །

[Block 4532]
ལྷའི་དཀྱིལ་འཁོར་སྤྲོ་བར་མཛད་པས་ན་ཞེས་པ་ལ་བྲན་དང་བྲན་མོ་དང་ཕོ་ཉ་དང་ཕོ་ཉ་མོ་དང་། བཀའ་ཉན་དང་བཀའ་ཉན་མོ་ལ་སོགས་པ་དཀྱིལ་འཁོར་པ་དུ་མ་འོད་ཟེར་གྱི་སྦྱོར་བས་བསྐྱེད་པའི་ཕྱིར་རོ། །

[Block 4533]
དེས་ནི་ཟུང་དུ་འཇུག་པའི་ཏིང་ངེ་འཛིན་ལ་གནས་པའི་བཅོམ་ལྡན་འདས་ལ་བསྟོད་པ་བསྟན་པ་ཡིན་ནོ། །

[Block 4534]
བྱང་ཆུབ་པ་ནི་དོན་དམ་པའི་བདེན་པ་ལ་ཞེས་པ༌[^2736]རིམ་པ་བཞི་པ་ཐོབ་པར༌[^2737]བྱ་བའི་དེ་ཁོ་ན་ཉིད་དོ། །

[Block 4535]
དེ་གང་གིས་སྤྱད་ཅིང་ཐོབ་པར་བྱེད་པ་ནི་ཞེས་པ་ལ་རྡོ་རྗེ་འཆང་ཆེན་པོའི་གོ་འཕང་ཐོབ་པའི་མོས་པས་མན་ངག་བཞི་པ་ལ་རྣལ་འབྱོར་པ་རྣམས་བརྩོན་པར་བྱེད་པའོ། །

[Block 4536]
ཀུན་རྫོབ་ཀྱི་བདེན་པའོ་ཞེས་པ་ནི་སྒྱུ་མ་ལྟ་བུའི་ལྷའི་སྐུའི་རྣམ་པ་བཟུང་བའོ། །

[Block 4537]
རྡོ་རྗེ་ནི་བདེན་པ་གཉིས་ཀྱི་བདག་ཉིད་ཅན་ཏེ་ཞེས་པ་ལ་བདེན་པ་གཉིས་ཀྱི་བདག་ཉིད་ཅན་རྡོ་རྗེ་འཆང་ཆེན་པོ་ཉིད་དོ། །

[Block 4538]
དག་པ་ནི་དོན་དམ་པའི་བདེན་པ་སྟེ་ཞེས་པ་ནི། སྣང་བ་ལ་སོགས་པའི་ཡེ་ཤེས་གསུམ་དང་། འདོད་ཆགས་བྲལ་བ་ལ་སོགས་པའི་རང་བཞིན་གྱི་ཚོགས་བརྒྱ་དྲུག་ཅུ་དང་བྲལ་བའི་དེ་ཁོ་ན་ཉིད་དོ། །

[Block 4539]
དེས་ནི་རིམ་པ་གཉིས་པ་གསལ་བར་བསྟན་ཏོ། །

[Block 4540]
ཡོངས་སུ་དག་ཅིང་ཡིད་ཀྱི་རང་བཞིན་གྱི་སྐུ་ཞེས་པ་ནི༌[^2738]འཇའ་ཚོན་དང་དྲི་ཟའི་གྲོང་ཁྱེར་དང་ཆུ་ཟླ་ལ་སོགས་པ་སྒྱུ་མའི་དཔེས་ཉེ་བར་མཚོན་པའི་རྣམ་པ་ཐམས་ཅད་ཀྱི་མཆོག་དང་ལྡན་པ་འོད་གསལ་བ་ལ་ཅིག་ཅར་དུ་བྱུང་བའི་རྡོ་རྗེ་འཆང་ཆེན་པོའི་སྐུ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4541]
དེ་བཞིན་ཉིད་དུ༌[^2739]གཤེགས་པས་ན། །ཞེས་པ་ནི་སེམས་རྣམ་པར་དག་པས་ཐོབ་པར་བྱ་བའི་འོད་གསལ་བའི་དེ་བཞིན་ཉིད་དེ་བདེན་པར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 4542]
གཤེགས་པ་ནི་སྔགས་དང་ཕྱག༌[^2740]རྒྱའི་རིམ་པས་ཐོབ་པའི་ཕྱིར་རོ། །

[Block 4543]
རྡོ་རྗེ་གསུམ་ལ་སོགས་པའི་རྣམ་པར་ཞེས་བྱ་བ་ནི་སྐུ་རྡོ་རྗེ་ལ་སོགས་པའི་སྐུ་འམ་སེམས་རྣམ་པ་གསུམ་གྱི་བདག་ཉིད་ཅན་གྱི་རྡོ་རྗེ་འཆང་ཆེན་པོའི་སྐུ་ཡིས་སོ། །

[Block 4544]
གདུལ་བྱ་རྣམས་ལ་སྣང་བས་སོ། །ཞེས་བྱ་བ་ནི་ཁམས་གསུམ་གྱི་ནང་ན་གནས་པའི་སེམས་ཅན་རྣམས་ལ་རང་གི་སྐུ་གསལ་བར་མཛད་པའི་ཕྱིར་རོ། །

[Block 4545]
མི་གནས་པའི་མྱ་ངན་ལས་འདས་པའི་དབྱིངས་ལ་མངོན་པར་བྱང་ཆུབ་པ་ཐོབ་པའི་འོག་ཏུ་ཟུང་དུ་འཇུག་པའི་ཏིང་ངེ་འཛིན་ལ་འཇོག་པའི་དོན་ཏོ་ཞེས་བྱ་བའི་ཐ༌[^2741]ཚིག་གོ། །

[Block 4546]
དེས་ནི་སེམས་རྣམ་པར་དག་པ་དང་བདག་ལ་བྱིན་གྱིས་བརླབ་པ་དང་མངོན་པར་བྱང་ཆུབ་པ་དང་ཟུང་དུ་འཇུག་པའི་རིམ་པ་རྣམས་བསྟན་ཏོ། །

[Block 4547]
སྒྲ་ཇི་བཞིན་པར་བཤད་པ༌[^2742]ཞེས་པ་ནི་བསྟོད་པའི་མཚན་ཉིད་ཀྱི་དོན་བསྟན་པའི་ཕྱིར་རོ། །

[Block 4548]
དེ་ཡང་སོགས་པའི་སྒྲས་ཤེས་པར་བྱའོ། །

[Block 4549]
འདིར་ཚིགས་སུ་བཅད་པ་ལྔ་ནི་རྡོ་རྗེ་འཆང་ཆེན་པོས་རྗེས་སུ་ཞུགས་པའི་དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱིས་གསུངས་སོ། །

[Block 4550]
གཞན་དུ་ན་རྡོ་རྗེ་འཆང་ཆེན་པོ་སྟོན་པ༌[^2743]ཡིན་པས་གཞན་རྣམས་ཀྱིས་ཆོས་སྟོན་པར་མི་རིགས་སོ། །

[Block 4551]
ལ་ལ་ན་རེ་རྡོ་རྗེ་འཆང་ཆེན་པོ་ལོངས་སྤྱོད་རྫོགས་པའི་སྐུའི་ངོ་བོ་ཡིན་ལ་དེ་བཞིན་གཤེགས་པ་རྣམས་ནི་སྤྲུལ་པའི་སྐུའི་རང་བཞིན་ཡིན་ནོ་ཞེས་ལོངས་སྤྱོད་རྫོགས་པ་དང་སྤྲུལ་པའི་སྐུ་གཉིས་དབྱེར་མེད་པའི་ཕྱིར་རྡོ་རྗེ་འཆང་ཆེན་པོ་ཁོ་ནས་གསུངས་སོ་ཞེས་ཟེར་རོ། །

[Block 4552]
དབྱེར་མེད༌[^2744]ཡང་འགྲོ་བའི་དོན་དུ་གཅིག་པའི་ཕྱིར་རོ། །

[Block 4553]
བྱང་ཆུབ་ཀྱི་སེམས་རབ་ཏུ་སྟོན་པ་ཞེས་པ་ལ་བྱང་ཆུབ་སེམས་ནི་བསྐྱེད་པའི་རིམ་པའི་ཕྱོགས་སུ་སྟོང་པ་ཉིད་དོ། །

[Block 4554]
དེ་གསལ་བར་བྱེད་པས་ན༌[^2745]བྱང་ཆུབ་ཀྱི་སེམས་རབ་ཏུ་སྟོན་པའོ། །

[Block 4555]
དེ་ནས་རྫོགས་པའི་རིམ་པའི་ཕྱོགས་སུ༌[^2746]རྡོ་རྗེ་བཟླས་པ་ལ་སོགས་པའི་རིམ་པ་ལྔས༌[^2747]ཐོབ་པར་བྱ་བའི་སྟོང་པ་ཉིད་དང་སྙིང་རྗེ་དབྱེར་མེད་པའི་ངོ་བོ་རྡོ་རྗེ་འཆང་ཆེན་པོའི་གོ་འཕང་ནི་བྱང་ཆུབ་ཀྱི་སེམས་སོ། །
--- END BLOCKS ---
