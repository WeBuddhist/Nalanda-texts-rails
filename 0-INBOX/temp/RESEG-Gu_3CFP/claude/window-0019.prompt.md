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
[Block 666]
གང་དེ་ལྟར་འཇུག་པ་དེ་ཉིད་དང་པོར་འཇུག་པ་ཉིད་ཀྱང་ཡིན་ནོ། །

[Block 667]
ཡང་འདི་དག་གི་ཁྱད་པར་གང་ཡིན་ཞེ་ན། འཇུག་པ་ནི་ཁྱིམ་པ་དང་རབ་ཏུ་བྱུང་བའི༌[^491]གནས་སྐབས་གཉིས་དག་གི་བསླབ་པའི་གནས་ཡང་དག་པར་ལེན་པའོ། །

[Block 668]
དང་པོར་འཇུག་པ་ཡང་མ་ཡིན་ཏེ། རིག་པའི༌[^492]དོན་ལ་ཕན་ཡོན་མཐོང་ནས་འཇུག་པ་འདི་ཉིད་ལ་དང་པོར་འཇུག་པ་ཞེས་བརྗོད་དོ། །

[Block 669]
དང་པོར་འཇུག་པ་མ་ཡིན་པ་ནི། སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱིས༌[^493]བཏང་སྙོམས་མི་མཛད་པ་ལ་རྟེན༌[^494]ཅིང་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། འདི་ནི་ཁམས་བརྟས་པའི༌[^495]བཤད་པའོ། །

[Block 670]
དེ་ལ་རྣམ་པར་དག་པ་ཐག་རིང་བ་ནི། ལེ་ལོའམ། རྐྱེན་དང་མི་ལྡན་པ་སྟེ། སྔར་བརྩོན་འགྲུས༌[^496]བརྩམས་པའི་ཁམས་ལ་བརྟེན་པ་ཉིད་དང་། ལེ་ལོ་དང་རྐྱེན་དང་མི་ལྡན་པའོ། །

[Block 671]
དེ་ནས༌[^497]འདི་ལྟར་དེ་དང་མི་ལྡན་པ་སྟེ། རྣམ་པར་དག་པ་ཐག་རིང་བའི་ཕྱིར། རྣམ་པར་དག་པ་ཐག་ཉེ་བ་མ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 672]
སྦྱོར་བ་ནི་མི་རྩོམ༌[^498]པའི་ཉེས་དམིགས་མཐོང་བའོ། །

[Block 673]
ཡང་དག་པར་རྟོག་པའི༌[^499]བཟོད་པ་ལ་བརྟེན་ཅིང་ཞེས་བྱ་བ་ནི། ཆོས་ལ་རྣམ་པར་དཔྱོད་པའི་རྒྱུ་ལས་བྱུང་བའི་བཟོད་པ་ཐོབ་པོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 674]
ཆོས་འདུལ་བ་འདི་ལས་ཞེས་བྱ་བ་ནི། སངས་རྒྱས་ཀྱི་བསྟན་པ་ལས་སོ། །

[Block 675]
དཀོན་མཆོག་གསུམ་ལ་དད་པ་མི་གཡོ་བའི་གཏེར་མི་འཕྲོགས་པར་བྱ་བའི་ཕྱིར་ཏེ། བཟོད་པ་ཉིད་དུ་བྱེད་དོ། །

[Block 676]
གཞན་དག་གིས་རྟོགས་པ་ལ་ཡིད་ཆེས་པ་དང་། ཡོན་ཏན་འབྱུང་བ་རྟོགས་པ༌[^500]ནས་རང་གི་དོན་ཐོབ་པར་བྱ་བ་ལ་མི་དད་པས་གཡོ༌[^501]བ་ཉིད་གང་ཡིན་པ་འབྱུང་ངོ་། །སྦྱོར་བ་དང་བསམ་པ་ནི་འདི་དག་གོ། །

[Block 677]
ད་ལྟར་གྱི་རྐྱེན་བཤད་པ་ནི། དེ་ལ་ད་ལྟར་གྱི་རྐྱེན་ཡང་རྣམ་པ་གསུམ་སྟེ[^502]། [^503]ཆོས་ལ་ཕྱིན་ཅི་མ་ལོག་པའི་ཆོས་འཆད་པ་དང་། དེ་ལ་ཕྱིན་ཅི་ལོག་པར་འཛིན་པ་ཉིད་དང་། ཆོས་དང་རྗེས་སུ་མཐུན་པའི་ཆོས་ལ་ཇི་ལྟ་བ་བཞིན་དུ་ནན་ཏན་བྱེད་པ་ཞེས་བྱ་བ་སྟེ། དེ་ལ་ཕྱིན་ཅི་མ་ལོག་པར་འཛིན་པ་ཉིད་དོ། །

[Block 678]
བསམ་པའི་ཐབས་ཀྱིས་བཤད་པ་ནི་ཆོས་དང་རྗེས་སུ་མཐུན་པའི་ཆོས་ལ༌[^504]ནན་ཏན་བྱེད་པའོ། །

[Block 679]
སྦྱོར་བའི་ཐབས་ཀྱིས་བཤད་པ་ནི། ཟང་ཟིང་ཉེ་བར་བསྒྲུབ་པ༌[^505]ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། ཐབས་དྲུག་གོ། །

[Block 680]
ད་ལྟར་གྱི་རྐྱེན་ཉེ་བར་བསྒྲུབ་པ་འདི་ལ་མཐོང་བའི་ཆོས་ཕྱིན་ཅི་མ་ལོག་པར་སྟོན་པ་ནི་བཤད་པའོ། །

[Block 681]
ཆོས་སྟོན་པ་འབའ་ཞིག་ཏུ་ཡང་མ་ཟད་དེ། འདི་ལྟར་འོན་ཀྱང་གཞན་གྱི་བྱ་བ་ཐམས་ཅད་ཀྱི་ཐབས་མ་ལུས་པའི༌[^506]བཤད་པ་ཡང་ཡིན་ནོ། །

[Block 682]
ཟང་ཟིང་ཉེ་བར་བསྒྲུབ་པ༌[^507]དང་ཆོས་ཉེ་བར་སྒྲུབ་པ་ནི་བསྡུ་བའི་ཐབས་ཡིན་ནོ། །

[Block 683]
རྫུ་འཕྲུལ་གྱིས་འདུན་པར་བྱེད་པ་ནི། འདུན་པར་བྱ་བའི་ཐབས་ཡིན་ཏེ། མ་དད་པ་དད་པར་བྱེད་པའི་ཕྱིར་དང་། བསམ་པ་དག་པར་བྱེད་པའི་ཕྱིར་དང་། སྦྱོར་བ་དག་པར་བྱེད་པའི་དོན་གྱིས་སོ། །

[Block 684]
འདི་ལྟར་འདུན་པར་བྱེད་པའི་ཕྱིར་དགོས་པ་ཡང་གཉིས་སུ་བསྟན་ཏེ། རང་གིས༌[^508]བདག་གི་དོན་ཐོབ་པར་མི་ནུས་པ་དབང་པོ་རྟུལ་པོ༌[^509]དང་། དབང་པོ་རྣོན་པོ་མངོན་པར་ཤེས་པ་མྱུར་བ་དག་གིའོ། །

[Block 685]
གསང་སྟེ་ཆོས་བརྗོད་པ་ནི། སེམས་ཅན་བྱིས་པའི་སྤྱོད་པ་ཅན་གྱི་དབང་དུ་བྱིས་པའོ། །

[Block 686]
རྣམ་པར་ཕྱེ་སྟེ་ཆོས་བརྗོད་པ་ནི། ཤེས་རབ་རྒྱ་ཆེ་བའི་དབང་དུ་བྱས་པའོ། །

[Block 687]
ད་ལྟར་གྱི་སྐྱོན༌[^510]སྦྱོར་བ་ཆོས་དང་རྗེས་སུ་མཐུན་པའི་ཆོས་ལ་ནན་ཏན་བྱེད་པ་ལས་བརྩམས་ནས། ཆུང་ངུ་ལ་སོགས་པ་གསུམ་པོ་རྟག་ཏུ་སྦྱོར་བ་མེད་པ་དང་། གུས་བར༌[^511]སྦྱོར་བ་མེད་པ་དང་། དེ་གཉི་ག་ལས་གང་ཡང་རུང་བ་གཅིག་མེད་པ་དང་། དེ་གཉི་ག་དག་དང་ལྡན་པ་སྟེ་གོ་རིམ་བཞིན་ནོ། །

[Block 688]
ཐོས་པ་ལ་སོགས་པ་གསུམ་ལ་སྦྱོར་བ་ནི། སྔར་གྱི་ཟང་ཟིང་ཉེ་བར་བསྒྲུབ་པ༌[^512]དག་གོ། །

[Block 689]
ཡོངས་སུ་སྨིན་པར་བྱེད་པ་ནི་རྣམ་པ་གཉིས་སུ་གྱུར༌[^513]ཏེ། ཡང་དག་པར་རབ་ཏུ་ཞུགས་པ་དང་། ལོག་པར་ཞུགས་པ་ཞེས་བྱ་བ་སྟེ། དེ་ལ་ཡང་དག་པར་མ་ཞུགས་པ་ནི་ཚར་བཅད༌[^514]པའོ། །

[Block 690]
དེ་ལ་མཐོང་བའི་ཆོས་ལ་གཞན་ལ་བརྟེན་པའི༌[^515]ཡོངས་སུ་སྨིན་པ་དེ་ནི་རྣམ་པ་གསུམ་སྟེ། རང་གིས༌[^516]བྱས་པ་ཉིད་དང་། གཞན་དག་གིས༌[^517]གསོལ་བ་བཏབ་པ་ཉིད་དང་། དེ་དག་གཉི་ག་ཉིད་ཅེས་བྱ་བའོ། །

[Block 691]
ཡོངས་སུ་སྨིན་པར་བྱེད་པའི་བྱང་ཆུབ་སེམས་དཔའ་དྲུག་གི་བསྡུས་པའི་དོན་ནི། ལྷག་པའི་བསམ་པ་དག་པ་དང་། ངེས་པ༌[^518]པ་དང་། ངེས་པའི་ས་ལ་གནས་པ་གསུམ་དང་། བྱང་ཆུབ་སེམས་དཔའ་གསུམ་པོ་དེ་དག་གི་སྦྱོར་བའི་ལམ་ལ་གནས་པ་གསུམ་སྟེ། མོས་པས་སྤྱོད་པའི་ས་ལ་གནས་པ་ནི། བསམ་པ་དག་པའི་ས་ལ་འཇུག་པའི་ཕྱིར་སྦྱོར་བའི་ལམ་ལ་གནས་པའོ། །

[Block 692]
དེ་བཞིན་དུ་གཞན་དག་ལ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 693]
རང་སངས་རྒྱས་དང་ཁྱད་པར་ནི་འདི་ཡིན་ཏེ། ལུས་ཐ་མ་ཐོབ་པར་གྱུར་པ་ན་སློབ་དཔོན་མེད་པ་ཉིད་དུ་དགྲ་བཅོམ་པ་ཆེན་པོ་ཉིད་དུ་ཐོབ་པར་བྱེད། མངོན་སུམ་དུ་བྱེད་པ་དེས་ན་རང་སངས་རྒྱས་ཞེས་བྱ་བའོ།

[Block 694]
[^519] །འདུན་པ་ཆུང་བར་གྱུར་པ་དང་། སྦྱོར་བ་ཆུང་བ་ཞེས་བྱ་བ་ནི། བསམ་པ་དང་སྦྱོར་བ་གཉི་ག་ཆུང་བའི་ཕྱིར་ཆུང་བ༌[^520]ཉིད་དོ། །

[Block 695]
དེ་བཞིན་དུ་གཞན་དག་ལ་ཡང་ངོ་། །ལེའུ་འདིའི་བསྡུས་པའི་དོན་གྱི་གོ་རིམ་ནི་མ་བྲིས་ཏེ། དེ་ཉིད་ཀྱིས་འདིར་ཡང༌[^521]ཡོངས་སུ་སྨིན་པ་ནི་རྣམ་པ་དྲུག་ཏུ་རིག་པར་བྱ་སྟེ་ཞེས་བྱ་བ་ལ་སོགས་པས་བསྟན་པའི་ཕྱིར་རོ། །

[Block 696]
བྱང་ཆུབ་སེམས་དཔའི་སའི་གཞིའི་རྣལ་འབྱོར་གྱི་གནས་ལས་རིམ་པར་ཕྱེ་བ་དྲུག་པ་རྫོགས་སོ།། །།

[Block 697 [HEADING]]
## བྱང་ཆུབ་སེམས་དཔའི་སའི་གཞིའི་རྣལ་འབྱོར་གྱི་གནས་ལས་བྱང་ཆུབ་སེམས་དཔའི་རིམ་པར་ཕྱེ་བ། ^2-0

[Block 698]
མདོར་བསྡུ་ན་སྤངས་པ་རྣམ་པ་གཉིས་དང་། ཡེ་ཤེས་རྣམ་པ་གཉིས་ལ་ནི་བྱང་ཆུབ་ཅེས་བྱ་སྟེ་ཞེས་བྱ་བ་ལ། འདིར་སྤངས་པ་རྣམ་པ་གཉིས་སྨོས་པ་ནི། ཡེ་ཤེས་ཉིད་ལ་འདི་ལྟར་བྱང་ཆུབ་ཅེས་བྱ་སྟེ། ཡེ་ཤེས་རྣམ་པ་གཉིས་ཐོབ་པ་ནི། སྤངས་པ་རྣམ་པ་གཉིས་བྱས་པས་ཡེ་ཤེས་ཀྱི་རྒྱུར་ཡང་དག་པར་བསྟན་པའོ། །

[Block 699]
རྣམ་གྲངས་གཞན་ཡང་ཞེས་བྱ་བ་ལ། འདིར་ཁྱད་པར་ནི་སྔ་མའི་རྣམ་གྲངས་ལས་ནི་ཤེས་བྱའི་སྒྲིབ་པ་སྤངས་པ་དང་། གང་ཤེས་བྱ་ཐམས་ཅད་ལ་ཐོགས་པ་མེད་ཅིང་སྒྲིབ་པ་མེད་པ་ནི། རྣམ་གྲངས་ཏེ་མ་ལས་མ་ཕྱེ་བར་ཡེ་ཤེས་བསྟན་ཏོ། །

[Block 700]
འདིར་ནི་ཡེ་ཤེས་དེ་ཉིད་རྣམ་པར་ཕྱེ་ནས་རབ་ཏུ་བསྟན་ཏོ། །

[Block 701]
འདུས་བྱས་དང་འདུས་མ་བྱས་ཀྱི་དངོས་པོ་དེ་ཉིད་ལ་རྣམ་པར་ཕྱེ་བའི་རབ་ཏུ་དབྱེ་བ་ཚད་མེད་དེ་ཞེས་བྱ་བ་ལ། ཇི་ལྟར་བྱས་ནས་འདི་ལྟར་ཙམ༌[^522]ཞེ་ན། རང་གི་མཚན་ཉིད་ཕྱི་མ་ཕྱི་མའི་ཞེས་བྱ་བ་ལ་སོགས་པས་སོ། །

[Block 702]
འདུས་བྱས་ཀྱི་དངོས་པོ་ལ་ནི་རང་གི་མཚན་ཉིད་ལ་སོགས་པའི་རབ་ཏུ་དབྱེ་བ་ལེགས་པར་བསྟན་པ་ཡིན་ན། འདུས་མ་བྱས་ལ་རང་གི་མཚན་ཉིད་ལ་སོགས་པའི་དབྱེ་བ་ཇི་ལྟར་ཞེ་ན། དེ་དག་ཉིད་ཀྱི་རང་གི་མཚན་ཉིད་ལ་སོགས་པའི་དབྱེ་བས་ཐ་དད་པའི་འདུས་བྱས་ཀྱི་ཆོས་རྣམས་ཀྱི་ཆོས་ཉིད་དང་། དེ་བཞིན་ཉིད་ལ་འདིར་འདུས་མ་བྱས་ཞེས་འདུས་བྱས་ཀྱི་དངོས་པོས་བྱས་པ་ཉིད་ནི་འདུས་མ་བྱས་ཀྱི་དབྱེ་བ་ཞེས་བྱ་སྟེ། འདི་ལ་འགལ་བ་མེད་དོ། །

[Block 703]
རྣམ་གྲངས་གཞན་ཡང་ཞེས་བྱ་བ་ནི། སངས་རྒྱས་ཀྱི་ཆོས་ཐམས་ཅད་ཀྱི་བདག་ཉིད་ནི་སངས་རྒྱས་ཞེས་བྱ་བར་བསྟན་པའི་དོན་དུ་རྣམ་གྲངས་གཞན་བརྩམས་པའོ། །

[Block 704]
དམ་པ་བདུན་གྱི་བསྡུས་པའི་དོན་ནི། གང་ལ་བརྟེན་པ་དང་། གང་གི་དོན་དུ་བསྒྲུབ་པ་དང་། གང་ལ་གནས་པ་དང་། ཐབས་གང་གིས་དང་། འབྲས་བུ་གང་ཐོབ་པ་དང་། གནས་པ་གང་གིས་གནས་པ་ཞེས་བྱ་བའོ། །

[Block 705]
དམ་པ་འདི་དག་ཉིད་ནི་དམ་པ་བདུན་ཏེ། སྦྱོར་བ་གང་གིས་དམ་པ་ཡིན་པ་ནི་བྱང་ཆུབ་ཅེས་བརྗོད་དོ། །
--- END BLOCKS ---
