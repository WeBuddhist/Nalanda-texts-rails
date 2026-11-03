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
སློབ་དཔོན་དཔའ་བོས་མཛད་པའི་སྐྱེས་པའི་རབས་རྒྱ་ཆེར་བཤད་པ་ལས་བྱང་ཆུབ་ཆེན་པོའི་སྐྱེས་པའི་རབས་སོ།། །།

[Block 4517 [HEADING]]
## སྤྲེའུ་ཆེན་པོའི་སྐྱེས་པའི་རབས། ^26-0

[Block 4518]
རྣམ་པ་སྣ་ཚོགས་པའི་འབྱུང་ཁུང༌[^2924]ནི། རྣམ་པ་སྣ་ཚོགས་པའི་འབྱུང་ཁུང་ངོ་། །རྣམ་པ་སྣ་ཚོགས་པའི་འབྱུང་ཁུང་གི་རྫས་གང་ཡིན་པའི་རིའི་ངོས་དེ་ནི་འབྱུང་ཁུང་གི་རྫས་རྣམ་པ་སྣ་ཚོགས་པའི་གངས་རིའི་ངོས་ཏེ་དེ་ནའོ། །

[Block 4519]
ཀཽ་ཤཱམྦཱིའི་དར་སྔོན་པོས་སྟོད་གཡོགས་སུ་གང་གིས་བྱས་པ་དེ་ནི་ཀཽ་ཤཱམྦཱིའི་དར་སྔོན་པོས་སྟོད་གཡོགས་གང་གིས༌[^2925]བྱས་པ་དེའོ། །

[Block 4520]
རྣམ་པ་དུ་མ་དག་གི་དབྱིབས་ཀྱི་རྣམ་པ་ནི༌[^2926]དབྱིབས་མང་པོའོ། །

[Block 4521]
ཁ་དོག་རྣམ་པ་དུ་མ་དང་། དབྱིབས་རྣམ་པ་མང་པོ་གང་ཡིན་པའི་ཐེལ་སྡིངས་དང་ཤང་ཤོང་དེ་ནི༌[^2927]རྣམ་པ་དུ་མའི་ཁ་དོག་དང་། དབྱིབས་རྣམ་པ་མང་པོ་དེའོ། །

[Block 4522]
བང་རིམ་རྣམ་པ་དུ་མ་ནི་བང་རིམ་རྣམ་པ་སྣ་ཚོགས་པ་སྟེ། ཐེལ་སྡིངས་དང་། ཤང་ཤོང་གི་བང་རིམ་རྣམ་པ་སྣ་ཚོགས་པ་དེའོ། །

[Block 4523]
གཅོང་རོང་གི་ནང་ནི་གཅོང་རོང་ངོ་། །གཅོང་རོང་ཡང་ཡིན་ལ་ཟབ་མོ་ཡང་ཡིན་པས་ན་གཅོང་རོང་ཟབ་མོའོ། །

[Block 4524]
གཅོང་རོང་ཟབ་མོ་གཡང་ཟབ་ནི་གཅོང་རོང་ཟབ་མོ་གཡང་ཟབ་སྟེ། དེ་མང་པོ་ཡོད་པ་ནི་གཅོང་རོང་ཟབ་མོ་དག་དེ་ན༌[^2928]ཡོད་པའོ། །

[Block 4525]
ཆོས་ཀྱི་འདུ་ཤེས་ནི་མ་ཉམས། བྱས་པ་གཟོ་བ་མ་འཇུངས་པའི་རང་བཞིན་ཅན་བཞིན་དུ་རབ་ཏུ་བརྟན་པ༌[^2929]དང་ལྡན་པ་ཞེས་བྱ་བ་འདི་བཞི་སྨོས་པ་ནི། རྒྱུ་འདི་བཞིས་ནི་སྙིང་རྗེ་གཏོང་བ་ཡིན་ཏེ། [^2930]འདི་ལྟར་ཆོས་ཀྱི་འདུ་ཤེས་ཉམས་ན་སྟེ། ཆོས་ནི་མི་འཚེ་བའི་མཚན་ཉིད་དེ། དེའི་འདུ་ཤེས་མ་ཉམས་པར་གྱུར་པའོ། །

[Block 4526]
ཆོས་དེ་བསྟན་ན་ནི་ཡུན་རིང་པོར་འདོད་པའི་འབྲས་བུ་འཐོབ་པར་འགྱུར་རོ། །

[Block 4527]
མི་བསྟེན་པ་དེས་ནི་མི་འདོད་པའི་འབྲས་བུ་འཐོབ་པར་འགྱུར་ཏེ། གང་འདིའི་འདུ་ཤེས་ཡོངས་སུ་ཉམས་པར་གྱུར་པའི་ཚེ་ནི་སྙིང་རྗེ་མེད་པ་ཡིན་ནོ། །

[Block 4528]
བདག་ལ་ཆགས་པ་དང་བཅས་པས་བྱས་པ་ནི༌[^2931]ཚོར་བའམ། འཁོར་བའི་ལམ་དག་ཏུ་ད་ལྟར་བྱུང་བ་དང་། འདས་པའི་དུས་སུ་སེམས་ཅན་རེ་རེ་ལ་ཡང་མཐའ་ཡས་པའི་མི་འདོད་པར་སྦྱར་བར་བྱས་པ་དང་། མཐའ་ཡས་པའི་མི་འདོད་པ་ལ་ཉེ་བར་སྦྱོར་བ་བྱས་པ་ཡིན་ཏེ། དེ་བས་ན་དེ་བྱས་པས་བདག་ཉིད་ཀྱིས་ཀྱང་སྙིང་རྗེ་གཏོང་བར་འགྱུར་རོ། །

[Block 4529]
མཐོང་བའི་ཆོས་ལ་འཇུངས་པའི་རང་བཞིན་ཅན་ཡིན་པའི་ཕྱིར། བདེ་བ་ཅུང་ཟད་ཙམ་འཐོབ་པའི་ཆེད་དུ་འཇུངས་པའི་ཕྱིར་སྙིང་རྗེ་གཏོང་བ་ཡིན་ནོ། །

[Block 4530]
མཐོང་བའི་ཆོས་ཉིད་ལ་སེམས་ཅན་རྣམས་དང་བདག་ཉིད་ཀྱི་མི་འདོད་པའི་རྒྱུས་མི་བརྟན་པའི༌[^2932]ཕྱིར། སྙིང་རྗེ་ཡོངས་སུ་གཏོང་བ་ཡིན་ནོ། །

[Block 4531]
བཞི་པོ་དེ་དག་མེད་པར་བསྟན་པའི་ཕྱིར། དེ་ལ་ཞེས་བྱ་བ་ཡིན་ཏེ། ཡོན་ཏན་བཞི་པོ་འདི་དང་ལྡན་པས༌[^2933]སྙིང་རྗེས་མ་བཏང་ངོ་ཞེས་བསྟན་པར་གྱུར་པ་ཡིན་ནོ། །

[Block 4532]
ནགས་ཚལ་ཞེས་བྱ་བས་ནི༌[^2934]ས༌[^2935]ཕྱོགས་ཉེ་བ་དང་མི་ཉེ་བར་གཟུང་ངོ་། །རི་མཆོག༌[^2936]ཅེས་བྱ་བས་ནི་ཕྱོགས་མཐོན་པོ་གཟུང་ངོ་། །རྒྱ་མཚོར་བཅས་པའི་ཞེས་བྱ་བ་ནི་བགས་ཀྱིས་གཞོལ་བའི་ཕྱོགས་གཟུང་ངོ་། །མེས་ནི་བསམ་གཏན་དང་པོའི་བར་དུ་འཇིག་པར་འགྱུར་རོ། །

[Block 4533]
ཆུས་ནི༌[^2937]བསམ་གཏན་གཉིས་པའི་བར་དུའོ། །

[Block 4534]
རླུང་གིས་ནི༌[^2938]བསམ་གཏན་གསུམ་པའི་བར་དུའོ། །

[Block 4535]
ནགས་ཀྱི་ཤིང་གི་ལོ་མ་དང་འབྲས་བུ་ཞེས་སྨོས་པས་ནི་གཞན་གྱིས་མ་གཟུང་བ་དང་། སྲོག་ཆགས་ལ་གནོད་པ་སྤངས་པའི་ཚུལ་ཉིད་དུ་བསྟན་པའི་ཕྱིར་ཏེ། འདི་ནི་སྲོག་གཅོད་པ་དང་། མ་བྱིན་པར་ལེན་པ་ལས་ལྡོག་པ་བསྟན་ཏོ། །

[Block 4536]
ས་ཕྱོགས་དེར་འོངས་སོ༌[^2939]ཞེས་བྱ་བ་ནི་གང་བྱང་ཆུབ་སེམས་དཔའ་གནས་པ་དེར་རོ། །

[Block 4537]
བཀྲེས་པ་དང་། སྐོམ་པ་དང་། ཚ་བ་དང་། ངལ་བས་ལུས་ནི་རྨྱ་ཞེས་བྱ་བ་ལ་བཀྲེས་པ་དང་། སྐོམ་པ་གཉིས་སྨོས་པས་ནི། ལྷན་ཅིག་སྐྱེས་པའི་སྡུག་བསྔལ་བསྟན་པའི༌[^2940]ཕྱིར། ཚ་བ་སྨོས་པ་ཡང་དེ་བཞིན་དུ་སྡུག་བསྔལ་བའོ། །

[Block 4538]
ངལ་བ་ནི་སྤྱོད་ཡུལ་ལས་གྱུར་པའི་ལུས་ཀྱི་སྡུག་བསྔལ་བའོ། །

[Block 4539]
ཡིད་མི༌[^2941]དགའ་བའི་མེ་ཞེས་བྱ་བ་ནི་སེམས་ཀྱི་སྡུག་བསྔལ་ལོ། །

[Block 4540]
བཀྲེས་པས་ཉེན་པ་དེས་རབ་ཏུ་ཞིམ་པར་རྟོགས༌[^2942]ཏེ། ཞེས་བྱ་བ་ནི་གང་གི་ཕྱིར་ལྟོགས་པས༌[^2943]ཞིམ་པར་བྱེད་པ་ཡིན་གྱི། འབྲས་བུ་དེ་ནི་ཞིམ་པོ་མ་ཡིན་ནོ། །ཞེས་པའི་དོན་ཏོ། །

[Block 4541]
འདི་ལས་འབྱུང་བ༌[^2944]ཡིན་པས་དེ་ལས་བྱུང་བ་སྟེ། དེ་ལས་བྱུང་བ་དེ་ཚོལ་བའོ། །

[Block 4542]
དེ་འདོད་པའི་ཕྱིར༌[^2945]ཞེས་བྱ་བ་ནི་ཏིན་དུའི་འབྲས་བུ་འདོད་པའོ། །

[Block 4543]
དེའི་ཞེས་བྱ་བ་ནི་དེའི་ཡལ་གའོ། །

[Block 4544]
ལྗོན་པའི་ཤིང་ཞེས་བྱ་བ་ནི་ཏིན་དུ་ཀ་ཞེས་བྱ་བ་དེའི་མིང་ཅན་ཏེ། རང་བཞིན་ཉིད་ཀྱིས་ཤིང་ཏིན་དུ་ཀ་ནི་རབ་ཏུ་ཕྲ་བའི་ངོ་བོ་ཉིད་དང་། ཤུན་ཕྲགས༌[^2946]མེད་པའི་ཕྱིར་ཏེ། དེ་བས་ན་སྨྲས་པ། ལྕི་བའི་ལྕིད་ཀྱིས་ནོན་པ་དང་། དེ་འཛེགས་པའི་ཕྱིར་དང་། ཕྲ་བའི་ཕྱིར་དང་། ཐོར་ཏོ་ལ་སོང་བའི་ཕྱིར། [^2947]སྟ་རེས་ཆེད་དུ་རྩ་བ་ནས་བཅད་པ་བཞིན་ཞེས་བྱ་བ་ཡིན་ཏེ། མ་ལུས་པར་ཆད་པ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 4545]
སྒྲ་དང་བཅས་པར་ཆག༌[^2948]ནས་ཞེས་བྱ་བ་ནི་ཤིང་ཏིན་དུ་ཀ་སྲབ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 4546]
དེ་ནས་ལྷན་ཅིག་ཏུ་ལྟུང་བར་གྱུར་ཏོ་ཞེས་བྱ་བ་འདིས་ནི༌[^2949]བར་དུ་འཆི་བ་མེད་པའི་རྒྱུ་བསྟན་ཏོ། །

[Block 4547]
འཆིའོ་སྙམ་སྟེ་གསོན་དུ་རེ་བ་ནི་མེད་ཅེས་བྱ་བ་ནི་འཚོ་བའི་རེ་བ་བཏང་བར་གྱུར་པའོ། །

[Block 4548]
ནགས་ཁུང་བགྲོད༌[^2950]དཀའ་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་ནི་སྐྱེ་བོ་དང་འབྲེལ་པ་མེད་པ་སྟེ། ཡོངས་སུ་སྐྱོབ་པ་མེད་པར་བསྟན་ཏོ། །

[Block 4549]
གཉེན་བཤེས་ཀུན་དང་བྲལ་ནས་ཞེས་བྱ་བ་འདིས་ནི་སྐྱེ་བོ་འདྲིས་པ་དང་བྲལ་བ་ཉིད་ཀྱི་ཕྱིར་ཏེ་དེས་ན༌[^2951]ཡོངས་སུ་སྐྱོབ་པ་མེད་པའོ། །

[Block 4550]
གཅིག་པུར་གྱུར་པ་དང་། ཤ་སྦྲང་མང་པོ་འདུན་མ༌[^2952]འདུ་བའི་ས། །ཞེས་བྱ་བ་འདིས་ནི། འཆི་བ་དང་ཉེ་བ་ཉིད་དུ་སྟོན་པའོ། །

[Block 4551]
རི་དགས་འདྲ་བ་ཞེས་བྱ་བ་ནི་སྐྱེ་བོ་མེད་པའི་ཕྱིར་རོ། །

[Block 4552]
བཀྲ་བ་ནོར་བུ་ནི་ནོར་བུ་བཀྲ་བའོ། །

[Block 4553]
བཀྲ་བ་ནི་ནོར་བུ་ཉིད་སྐར་མ་ཡིན་པས། བཀྲ་བའི་ནོར་བུ་རིན་ཆེན་སྐར་མའོ། །

[Block 4554]
དེས་མཛེས་པའི་སྤྲིན་གང་ཡིན་པ་དེ་ནི་ནོར་བུ་རིན་ཆེན་སྐར་མ་བཀྲ་བས༌[^2953]མཛེས་པའོ། །

[Block 4555]
འདིར་འོངས་ཞེས་བྱ་བ་གློ་བུར་དུའོ། །
--- END BLOCKS ---
