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
དཔེར་ན་མར་མེ་འམ། དྲིལ་བུའི་སྐད་འགག་པར་བྱེད་པ་དང་འདྲའོ། །

[Block 667]
ཡང་ན་སྲོག་གི་དབང་པོ་སྲོག་ཡིན་ཏེ། དེ་འགག་པར་བྱེད་དོ། །

[Block 668]
གལ་ཏེ་སྲོག་གི་དབང་པོའི་སྐད་ཅིག་མ་གཅིག་སྐྱེ་བ་ལ་བར་ཆད་བྱེད་ན་ཡང་སྲོག་གཅོད་པའི་ཁ་ན་མ་ཐོ་བས་རེག་པར་འགྱུར་གྱི་གཞན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 669]
དེ་མེད་པས་གང་ཞིག་འཆི་བར་འགྱུར་བའི་སྲོག་དེ་གང༌[^477]ཡིན་ཞེ་ན། གང་གི་ཞེས་བྱ་བའི་དྲུག་པ་ནི་གང་ཟག་ཏུ་སྨྲ་བ་དགག་པར་དཔྱད་པར་བྱའོ། །

[Block 670]
བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་།

[Block 671 [VERSE]]
གང་ཚེ་ཚེ་དང་དྲོད་རྣམས་ཤེས། །
འདི་དག་གིས་ནི་ལུས་འདོར་ཞིང་། །
བོར་ན༌[^478]དེ་ཚེ་འདུག་པ་ནི། །
ཇི་ལྟར་ཤིང་ལ་སེམས་མེད་བཞིན། །

[Block 672]
ཞེས་གསུངས་ཏེ། དེ་ལྟ་བས་ན་དབང་པོ་དང་བཅས་པའི་ལུས་ནི་གསོན་པོ་ཞེས་བྱ་ལ། དབང་པོ་མེད་པ་ནི་ཤི་བ་ཞེས་བྱའོ། །

[Block 673]
གཅེར་བུ་པ་རྣམས་ན་རེ་བློ་སྔར་མ་བཏང་བའི་སྲོག་གཅོད་པས་ཀྱང་བྱེད་པ་པོ་ཆོས་མ་ཡིན་པ་དང་ལྡན་པར་འགྱུར་ཏེ། དཔེར་ན་མེ་དང་རེག་པ་ལས་ཚིག་པར་འགྱུར་བ་བཞིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 674]
དེ་དག་གི་ལྟར་ན་གཞན་གྱི་ཆུང་མ་མཐོང་བ་དང་། རེག་པ་ལ་ཡང་དེ་ལྟར་ཐལ་བར་འགྱུར་རོ། །

[Block 675]
གཅེར་བུ་པ་སྐྲ་འབལ་བ་དང་། དཀའ་ཐུབ་དྲག་པོའི་ལུང་འབོགས་པ༌[^479]དང་། དེ་དག་གསད་དེ་ཤི་ན་ཡང་སྦྱིན་པ་པོ་ལ་དེ་ལྟར་ཐལ་བར་འགྱུར་རོ། །

[Block 676]
མ་དང་བུ་ལྟོ་ན་ཡོད་པ་དག་ཀྱང་ཕན་ཚུན་སྡུག་བསྔལ་གྱི་རྒྱུ་མཚན་དུ་གྱུར་པའི་ཕྱིར་དེ་ལྟར་ཐལ་བར་འགྱུར་རོ། །

[Block 677]
གསོད་པར་བྱ་བ་ཡང་དེའི་བྱ་བ་དང་འབྲེལ་པའི་ཕྱིར་དེ་ལྟར་ཐལ་བར་འགྱུར་ཏེ། མེས་རང་གི་རྟེན་སྲེག་པ༌[^480]བཞིན་ནོ། །

[Block 678]
བྱེད་དུ་འཇུག་པ་ལ་ཡང་ཐལ་བར་མི༌[^481]འགྱུར་ཏེ། གཞན་མེ་ལ་རེག་ཏུ་འཇུག་པ་མེ༌[^482]དེས་མི་འཚིག་པ་བཞིན་ནོ། །

[Block 679]
ཁྱིམ་རྡིབ༌[^483]ན་སྲོག་ཆགས་དག་འཆི་བའི་ཕྱིར་ཤིང་ལ་སོགས་པ༌[^484]མེད་པ་རྣམས་ཀྱང་སྡིག་པ་དང་ལྡན་པར་ཐལ་བར་འགྱུར་རོ། །

[Block 680]
ནད་པ་ལ་གནོད་པ་དང་། ཤི་བ་ན་སྨན་པ་རྣམས་ལ་ཡང་དེ་ལྟར་ཐལ་བར་འགྱུར་རོ། །

[Block 681]
ཡང་ན་དཔེ་ཙམ་གྱིས་ནི་འགྲུབ་པར་མི་འགྱུར༌[^485]རོ། །

[Block 682]
སྲོག་གཅོད་པ་བཤད་ཟིན་ཏོ། །

[Block 683 [HEADING]]
#### མ་བྱིན་པར་ལེན་པ། ^1-48-2-0

[Block 684 [VERSE]]
མ་བྱིན་ལེན་པ་གཞན་གྱི་ནོར། །
མཐུ་དང་འཇབ་བུས་བདག་གིར་བྱེད། །

[Block 685]
མ་ནོར་བ་ཞེས་བྱ་བར་སྦྱར་ཏེ། གལ་ཏེ་གཞན་གྱིས་བདག་གིར་བྱས་པ་ལ་མཐུ་དང་འཇབ་བུས་བདག་གིར་བྱེད་ཅིང་། གང་དུ་མཐུ་དང་འཇབ་བུས་བདག་གིར༌[^486]བྱ་བར་བསམས༌[^487]པ་དེ་ལས་གཞན་དུ་འདུ་ཤེས་ཀྱང་མ་འཁྲུལ་ན་དེ་ཙམ་གྱིས་མ་བྱིན་པར་ལེན་པ་ཡིན་ནོ། །

[Block 686]
མཆོད་རྟེན་ལས་ཕྲོགས་པ་ནི་སངས་རྒྱས་ལས་མ་བྱིན་པར་བླངས་པ་ཡིན་ཏེ། བཅོམ་ལྡན་འདས་ཡོངས་སུ་མྱ་ངན་ལས༌[^488]འདའ་བའི་ཚེ་དེ་དག་ཐམས་ཅད་ཡོངས་སུ་གཟུང༌[^489]བའི་ཕྱིར་རོ། །

[Block 687]
གཞན་དག་ན་རེ་སྲུང༌[^490]མ་གང་དག་ཡིན་པ་ལས་སོ་ཞེས་ཟེར་རོ། །

[Block 688]
བདག་པོ་མེད་པའི་གཏེར་བྲུས་ན་ནི་ཡུལ་གྱི་བདག་པོ་ལས་སོ། །

[Block 689]
ཤི་བའི་ནོར་ཕྲོགས་ན་ལས་བྱས་པ་ཞིག་ཡིན་ན་ནི་མཚམས༌[^491]ཀྱི་ནང་དུ་གཏོགས་པ་རྣམས་ལས་སོ། །

[Block 690]
མ་བྱས་པ་ཞིག་ཡིན་ན་ནི་སངས་རྒྱས་ཀྱི་སློབ་མ་ཐམས་ཅད་ལས་སོ། །

[Block 691 [HEADING]]
#### འདོད་པས་ལོག་པར་གཡེམ་པ། ^1-48-3-0

[Block 692 [VERSE]]
བགྲོད་མིན་འགྲོ་བ་འདོད་པ་ཡིས། །
ལོག་པར་གཡེམ་པ་རྣམ་པ་བཞི། །

[Block 693]
བགྲོད་པར་བྱ་བ་མ་ཡིན་པར་འགྲོ་བ་འདོད་པས་ལོག་པར་གཡེམ་པ་རྣམ་པ་བཞི་སྟེ། བགྲོད་པར་བྱ་བ་མ་ཡིན་པ་གཞན་གྱིས་ཡོངས་སུ་གཟུང་བ་འམ། མ་འམ། བུ་མོ་འམ། ཕ་དང་མ་དང་འབྲེལ་པའི་གན་དུ་འགྲོའམ།[^492] རང་གི་ཆུང་མ་ཡིན་ཡང་ཡན་ལག་མ་ཡིན་པར་འགྲོ་བ་སྟེ། ཁའམ་རྐུབ་ཏུ་འཇུག་པའམ། །ཡུལ་མ་ཡིན་པར་འགྲོ་བའམ།[^493] སྣང་བའམ། མཆོད་རྟེན་ནམ། གཙུག་ལག་ཁང་ངམ། དུས་མ་ཡིན་པར་འགྲོ་བ་སྟེ། དུས་མ་ཡིན་པ་གང་ཞེ་ན། སྦྲུམ་མའམ། ནུ་ཞོ་འཐུང་བའམ། ངེས་པ་དང་བཅས་པའི་གན་དུ་འགྲོ་བའོ། །

[Block 694]
ཁ་ཅིག་ན་རེ་གལ་ཏེ་ཁྱོས༌[^494]གནང་ན་ངེས་པ་དང་བཅས་པ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 695]
མ་ནོར་བ་ཞེས་བྱ་བར་སྦྱར་ཏེ། གལ་ཏེ་བདག་གི་ཡིན་པའི་འདུ་ཤེས་ཀྱིས་གཞན་གྱི་ཆུང་མའི་གན་དུ་སོང་ན་ལས་ཀྱི་ལམ་དུ་མི་འགྱུར་རོ། །

[Block 696]
གལ་ཏེ་གཞན་གྱི་ཆུང་མ་མ༌[^495]ཡིན་པའི་འདུ་ཤེས་ཀྱིས་གཞན་ཞིག་གི་གན་དུ་སོང་ན། ཁ་ཅིག་ན་རེ་གཞན་གྱི་ཆུང་མ་ལ་སྦྱར་བར༌[^496]བྱས་པའི་ཕྱིར་དང་། དངོས་པོ༌[^497]ཡོངས་སུ་ལོངས་སྤྱད་པའི་ཕྱིར་འགྱུར་རོ་ཞེས་ཟེར་རོ། །

[Block 697]
གཞན་དག་ན་རེ་སྦྱོར་བ་གཞན་དུ༌[^498]བྱས་པའི་ཕྱིར་མི་འགྱུར་ཏེ། སྲོག་གཅོད་པ་བཞན༌[^499]ནོ་ཞེས་ཟེར་རོ། །

[Block 698]
དགེ་སློང་མའི་གན་དུ་འགྲོ་བ་སུ་ལས་འདོད་པ་ལ༌[^500]ལོག་པར་གཡེམ་པ་ཡིན་ཞེ་ན། ཡུལ་གྱི་བདག་པོ་ལས་ཏེ་དེས་ནི་དེ་མི་བཟོད་པར་བྱ་བ་ཡིན་ནོ། །

[Block 699]
དེས༌[^501]ནི་རང་གི་ཆུང་མ་ངེས་པ་དང་བཅས་པ་བཞིན་དུ་བགྲོད་པར་བྱ་བ༌[^502]མ་ཡིན་པ་ཡང་ཡིན་ནོ། །

[Block 700]
གཞོན་ནུ་མའི་གན་དུ་འགྲོ་བ་ནི་གང་ལ་བྱིན་པ་ལས་སོ། །

[Block 701]
གལ་ཏེ་སྦྱིན་པ༌[^503]མེད་ན་སྲུང་བ་གང་ཡིན་པ་དང་།

[Block 702]
ཐ་ན་རྒྱལ་པོ་ལས་སོ། །

[Block 703 [HEADING]]
#### བརྫུན་དུ་སྨྲ་བ། ^1-48-4-0

[Block 704 [VERSE]]
བརྫུན་ཚིག་འདུ་ཤེས་གཞན་བསྒྱུར་བའི། །
ཚིག་དོན་མངོན་པར་གོ་བའོ། །

[Block 705]
དོན་སྨྲ་བ་གང་ཡིན་པ་དེ་ལ་འདུ་ཤེས་གཞན་དུ་བསྒྱུར་ལ་དེས༌[^504]གང་གི་དབང་དུ་བྱས་ནས་སྨྲས་པའི༌[^505]ཚིག་དེའི་དོན་ཡང་གོ་ན་ཚིག་དེ་ནི་བརྫུན་དུ་སྨྲ་བའི་ཡིན་ནོ། །
--- END BLOCKS ---
