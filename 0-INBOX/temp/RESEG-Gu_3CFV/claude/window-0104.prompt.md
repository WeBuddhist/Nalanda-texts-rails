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
[Block 3641]
ཉེས་པ་དེ་མེད་པ་ཉིད་ལ་འོང་བ་ནི་ཐ་དད་དོ་ཞེས་བྱ་བ་ནི་དེ་ལ་ནི་དེའི་ལས་ཀྱི་ཉེས་པ་སྐྱེད་པ༌[^2392]མ་ཡིན་པ་དེ་བས་ན་ཉེས་པ་དེ་མེད་པའོ། །

[Block 3642]
དེ་ཉིད་ཀྱི་གནས་སྐབས་ཅན་དུ་གྱུར་པ་ནི་ཐ་དད་པའོ། །

[Block 3643]
གང་ཞིག་དེར་དེའི་ཉེས་པ་ཉིད་ལ་བྱས་པ་དང་། གང་ཡང་དེའི་ཉེས་པ་ཉིད་མ་ཡིན་པ་དང་། གང་ཡང་སླར་དེའི་འོག་ཏུ་ཉེས་པ་དེ་ཡོད་པ༌[^2393]ལས་དེ་དག་ནི་ཕན་ཚུན་ཐ་དད་པར་ཤེས་པར་བྱའི༌[^2394]གཅིག་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 3644]
དུས་མ་ཡིན་པ་ཁོ་ན་སྟན༌[^2395]བརྩམས་ནས་ངལ་སོ༌[^2396]བར་བྱེད་པ་དེ་ཡང་བསྙེན་པར་རྫོགས་པར་བྱས་ནས་དུས་མ་ཡིན་པ་ཁོ་ནར་ཟིན་པར་བྱེད་པའོ། །

[Block 3645]
བུད་མེད་དུ་གྱུར་ནས་ཡང་སྐྱེས་པ་ཉིད་ཐོབ་ན་ཐ་དད་པ་ཉིད་དོ། །

[Block 3646]
གལ་ཏེ་ཡང་བསམ་པ་ཐག་པ་ནས་གཏང་བ༌[^2397]གང་ཡིན་པ་དེ་ནི་མ་སྐྱེས་པ་ཉིད་དུ་གྱུར་ནས་དེ་ལྟ་བུ་ཡང་ཐ་དད་པ་ཉིད་ཀྱིས་སྔ་མ་དང་ཕྱི་མའི་ཆ་གང་དག་ལས་ལྟུང་བའི་བྱེད་པ་པོ་ཉིད་དོ། །

[Block 3647]
གཙོ་བོ་མ་ཡིན་པས་བཏང་བ་དང་། གང་ཞིག་དེའི་སྔ་མ་ཕྱེད་བྱས་སམ་བྱེད་པ་ལ་གང་ཞིག་དེའི་ཕྱི་མ་དང་རབ་ཏུ་བྱུང་ནས་ཡང་བསྙེན་པར་རྫོགས་པ་ལ་ཐོག་མ་ཉིད་དུ་སྟན་གཞན་བྱས་པའི་དབང་གིས་དུས་མ་ཡིན་པ་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 3648]
དགེ་སློང་མ་ཉིད་ལས་ཡང་ལྟུང་བར་སྔར་བྱས་པ་ལ་ཡང་ངོ་། །བཏང་བ་ལ༌[^2398]ཡང་ངོ་ཞེས་བྱ་བ་ནི་ལས་གང་བརྩམས་པ་དེ་མ་ཟིན་པར་དེ་ཡང་དེའི་ཆད་པའོ། །

[Block 3649]
སྔར་བྱས་པ་ལ་དེ་ཙམ་ཉིད་དོ། །

[Block 3650]
ཡང་ལས་གཞན་ཉིད་ནི་བྱས་པ་ནས་བརྩམས་ཏེ༌[^2399]ཁང་པའམ་སྟན་བརྩམས་ནས་བཏང་སྟེ། ཡང་བྱེད་ན་སྔ་མ་དང་ཕྱི་མ་ཉིད་ལ་ལྟུང་བའི་བྱེད་པ་པོ་ཉིད་དོ། །

[Block 3651]
གཞི་གཅིག་ལ་དུ་མ་ཉིད་བཅས་པ་ལ་ནི་ཇི་སྙེད་ཀྱི་ཉེས་པར་འགྱུར་རོ་ཞེས་བྱ་བ་ནི་གང་དུ་གཞི་གཅིག་ལ་དུ་མ་ཉིད་ཐོབ་པར་འགྱུར་བ་ནི་འདི་ལྟ་སྟེ་དཔེར་ན་བརྫུན་དུ་སྨྲ་བ་དང་། སྐྱོན་ནས་སྨྲ་བ་དགག་པ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 3652]
བསྙིལ་བ་དང་ལྷན་ཅིག་ཞག་གསུམ་ཉལ་བ་ལའོ། །

[Block 3653]
དགེ་ཚུལ་བསྙིལ་བ༌[^2400]དང་བུད་མེད་བསྙེན་པར་མ༌[^2401]རྫོགས་པ་དང་ལྷན་ཅིག་ཞག་གསུམ་ཉལ་བ་ལ་བཅས་པ་སྟེ། དེ་ལ་ལྟུང་བྱེད་དོ། །

[Block 3654]
འདིར་གཞུང་ཁ་ཅིག་ལས་ནི། ཞར་བ་ལོངས་ཤིག་ཅེས་ཟེར་བ་ལ་ཞར་བ་མ་ཡིན་ན་ལྟུང་བྱེད་གཉིས་སུ་འགྱུར་ཏེ། ཤེས་བཞིན་དུ་བརྫུན་སྨྲ་བ་དང་མིའི་སྐྱོན་ནས་སྨྲ་བ་ལས་སོ། །

[Block 3655]
དགེ་སློང་གིས༌[^2402]དགེ་སློང་མ་བྲམ་ཟེའི་རིགས་ཅན་མོ་ལ་ཁྱོད་ཀྱིས་འདྲེག༌[^2403]མཁན་གྱི་ལས་བྱས་སོ་ཞེས་སྨྲས་ན༌[^2404]ལྟུང་བྱེད་དང་ཉེས་བྱས་སུ་འགྱུར་ཏེ། ཤེས་བཞིན་དུ་བརྫུན་དུ་སྨྲ་བ་ལས་ལྟུང་བྱེད་དང་སྐྱོན་ནས་སྨྲ་བ་ལ་ཉེས་བྱས་སོ། །

[Block 3656]
དགེ་སློང་མ་རྒྱལ་རིགས་ཀྱི་རིགས་ཅན་མོ་ལ་ཡང་དེ་བཞིན་ནོ་ཞེས་གསུངས་པ་དང་། དགེ་སློང་བསྙེན་པར་མ་རྫོགས་པའི་གང་ཟག་དང་ལྷན་ཅིག་དགུང་གསུམ་ཉལ་བ་ལ་ལྟུང་བྱེད་གཉིས་འབྱུང་བ་འགའ་མཆིས་སམ། ཡོད་དེ་ཞག་གཉིས་དགེ་ཚུལ་དང་ཉལ་བ། ཞག་གསུམ་པ་ལ་ཁྱིམ་པ་མོ་དང་ལྷན་ཅིག་ཉལ་བ་ལའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ནོ། །

[Block 3657]
དེའི་ཆ༌[^2405]ནི་དེར་གཏོགས་སོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་ཁ་ན་མ་ཐོ་བ་ནི་དེའི་ཆ་ཞེས་བྱ་བ་ཤན་ནམ་ལྷག་མ་ནི་དེ་དང་གཞན་མ་ཡིན་ནོ། །

[Block 3658]
མི་ཚངས་པར་སྤྱོད་པའི་ཆ་གང་ཞེ་ན། ཁུ་བ་འབྱིན་པ་དང་། ལུས་ཀྱི་རེག་པ་དང་། འཁྲིག་པ་དང་ལྡན་པ་སྨྲ་བ་དང་། ཀུན་སྤྱོད་བསྔགས་པ་དང་། སྨྱན་བྱེད་པ་དང་། དགེ་སློང་མ་ཉེ་དུ་མ་ཡིན་པ་ལ་གོས་རྙིང་པ་འཁྲུར་འཇུག་པ་དང་། ལེན་པ་དང་དེ་ལས་གཞན་པའི་གོས་ཀྱི་ལས་བྱེད་པ་དང་། འདིས་བལ་རྨེལ་དུ་འཇུག་པ་དང་། རིག་པའི་སྐྱེས་བུ་མེད་པར་ཚིག་དྲུག་གམ་ལྔ་ལས་ལྷག་པར་ཆོས་སྟོན་པ་དང་། མ་བསྐོས༌[^2406]པར་གདམས་ངག་ལ་སོགས་པ་སྟོན་པ་བཅུ་དང་། བཟའ་བ་ཟ་བའི་དུས་སུ་ཁྱིམ་དུ་འདུག་ཅིང་མི་གནས་པ་དང་། ཁྱིམ་དུ་ཟ་བའི་ཕྱིར་འདུག་སྟེ་མི་གནས་པ་དང་། དགེ་ཚུལ་དང་། དགེ་ཚུལ་མ་ལ་བྱིན་པ་དང་། ཁྱིམ་དུ་ལྷན་ཅིག་ཉལ་བ་དང་། ལམ་དུ་འགྲོ་བ་དང་། སྐྱེས་པ་མེད་པར་བུད་མེད་དང་ལྷན་ཅིག་གྲོང་དུ་འཇུག་པ་དང་། ཉེ་དུ་མ་ཡིན་པའི་གྲོང་དུ་འགྲོ་བ་དང་། དགེ་སློང་མ་ལས་བླངས་ཏེ་ཟ་བ་དང་། དགེ་སློང་མའི་མིང་གིས་ངེས་པ་དང་བཅས་པས་ཁྱིམ་དུ་འགྲོ་བ་དེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 3659]
སྔར་མ་གནང་བའི་སྟན་ལ་འདུག་པ་ལ་འདི་ཡིན་ནོ། །

[Block 3660]
མ་བྱིན་པར་ལེན་པའི་ཆ་གང་ཡིན་ཞེ་ན། བྱིན་པ་ཕྲོགས་ཏེ་སྤྱོད་པ་དང་། མ་གནང་བར་སྟན་ལ་འདུག་པ་དང་། ཕྱིར་མ་བླངས་པར་སྤྱོད་པ་དང་། སོ་སོར་བསྡུས་ནས་ལོངས་སྤྱོད་པ་དང་། བསྔོས་པ་ལས་བསྒྱུར་བ་དང་། སྐྲོད་པ་དང་། སྦེད་པ༌[^2407]དང་། རྐུན་མ་དང་ལྷན་ཅིག་ལམ་དུ་འགྲོ་བའོ། །

[Block 3661]
མི་གསོད༌[^2408]པའི་ཆ་གང་ཞེ་ན། རྩོད་པ་དང་བཅས་པའི་གཞི་མི་གཏོང་བ་དང་། ས་བོན་གྱི་ཚོགས་དང་། [^2409]སྐྱེ་བའི་ཚོགས་འཇིག་པ༌[^2410]དང་། མཐོ་འཚམས་པ༌[^2411]དང་། ཕྱིས་གནོན་བྱས་ནས་འདུག་པ་དང་། བསྒོ་བ་བཅག་པ་དང་། རྩ་བ་འབྱུང་བ་ལ་འདུག་པ་དང་། སྲོག་ཆགས་དང་བཅས་པ་ལ་སྤྱོད་པ་དང་། དམག་ལ་ལྟ་བ༌[^2412]དང་། དམག་གི་ནང་ན་གནས་པ་དང་། བཤམས་པ་དཀྲུག་པ༌[^2413]དང་། བརྡེག་པ་དང་། གཟས་པ་དང་། ཟས་གཅོད་དུ་འཇུག་པ་དང་། དུད་འགྲོ་གསོད་པ་དང་། འགྱོད་པ་སྐྱེད་པ༌[^2414]དང་། ག་ག་ཚིལ་བྱེད་པ་དང་། སྔངས་པར་བྱེད་པ་དང་། ས་བརྐོ༌[^2415]བའོ། །

[Block 3662]
མིའི་ཆོས་བླ་མ་སྨྲ་བའི་ཆ་གང་ཞེ་ན། འདི་ལྟ་སྟེ་དཔེར་ན་ཕམ་པར་འགྱུར་བ་དང་། དགེ་འདུན་ལྷག་མ་གཉིས་ཀྱིས་འདུན་པ་ལ་སོགས་པ་འགྲོ་བར་བརྗོད་པའི་ཚིག་སྟེ། ཇི་ལྟར་བརྩམས་པས་བཤེས་ངོར་བྱེད་པ་དང་། འཕྱ་བ་དང་། གཞོགས༌[^2416]འཕྱས་བྱེད་པ་དང་། དགེ་འདུན་གྱི་དབྱེན་དང་། བརྫུན་གྱི་ལྷག་མ་དང་། མིའི་ཆོས་བླ་མ་བདེན་པར་སྨྲ་བའོ། །

[Block 3663]
ཕམ་པར་འགྱུར་བས་སྐུར་པ་འདེབས་པའི་ཆ་གང་ཞེ་ན། དགེ་འདུན་ལྷག་མས་སྐུར་པ་འདེབས་པའོ། །

[Block 3664]
དགེ་འདུན་གྱི་དབྱེན་བྱེད་པའི་ཆ་གང་ཞེ་ན། དགེ་སློང་ལ་ཕྲ་མ་བྱེད་པ་དང་། སྐྱོ་སྔོགས་བྱེད་པ་དང་། དད་པའི་ཕྱིར་བསྒྱུར་བ་དང་། ལས་ལས་འདའ་བར་བྱེད་པ་དང་། ལྟ་བར་གྱུར་པ་མི་འདོར་བ༌[^2417]དང་། བསླབ་པ་ལ་མ་གུས་པ་དང་། འདུས་ཤིང་ཟ་བ་དང་། སྤངས་པའི་རྗེས་སུ་ཕྱོགས་པ་དང་། ཚིག་མི༌[^2418]སྙན་པས་བསླབ་པ་ལ་ཁྱད་དུ་གསོད་པའོ། །

[Block 3665]
གསོག་འཇོག་བྱས་པ་ཟ་བའི་ཆ་ནི་དགེ་སློང་གིས་བཙོས་པ་ཟ་བའི་མཐར་ཐུག་པའོ། །

[Block 3666]
དེ་ལྟ་བས་ན་ཆའི་ངོ་བོ་ཉིད་ཅེས་བྱ་བ་ནི་མི་ཚངས་པར་སྤྱོད་པ་སྤྱད་པའི་ཕྱིར་འགྲོ་བ་གང་ཡིན་པ་དེ་ནི་ཉེས་བྱས་སོ། །

[Block 3667]
བདག་ཉིད་ཀྱི་ཀུན་དུ་སྤྱོད་པ་བསྔགས་པ་གང་ཡིན་པ་དེ་ནི་དགེ་འདུན་ལྷག་མའོ། །

[Block 3668]
གནས་ངན་ལེན་སྨྲ་བ་གང་ཡིན་པ་དེ་ནི་གཞན་མ་ཡིན་ནོ། །

[Block 3669]
བདག་ཉིད་ཀྱི་དོན་དུ་བུད་མེད་ལ་གཞོལ་བ་གང་ཡིན་པ་དེ་ནི་ཕམ་པར་འགྱུར་བར་གཏོགས་པའི་སྦོམ་པོའོ། །

[Block 3670]
ཀུན་དུ་སྤྱོད་པ་བསྔགས་པའི་དགེ་འདུན་ལྷག་མར་གཏོགས་པའི་ཉེས་བྱས་སོ། །

[Block 3671]
འཁྱུད་པ་དང་འོ་བྱེད་པ་དང་ཉལ་བ་དང་མཚམས་ཀྱི་ཕྱི་རོལ་དུ་འགྱུར་བ༌[^2419]དག་གང་ཡིན་པ་དེ་ནི་ལུས་ཀྱི་རེག་པའི་བདག་ཉིད་གཞན་ཡིན་ནོ། །

[Block 3672]
མཚན་གྱི་ནང་དུ་རེག་པ་ལ་ཉལ་ཏེ་རྨ་ཉམས་པ་མ་ཡིན་པ་གང་ཡིན་པ་དེ་ནི་ཕམ་པར་འགྱུར་རོ། །

[Block 3673]
གལ་ཏེ་ཉམས་པ་ཡིན་ན་གཞན་དང་ལྷན་ཅིག་རྩོད་པ་ན་མ་བྱུང་བའི་མདུན་རོལ་དུ་ནི་སྦོམ་པོའོ། །

[Block 3674]
བྱུང་ན་ནི་དགེ་འདུན་ལྷག་མའོ། །

[Block 3675]
མདོ་འདིས་ནི་དེའི་ཆ་མ་བརྗོད་པ་ཅུང་ཟད་ཀྱང་མ་བརྗོད་ཀྱི་ཧ་ཅང་ཐལ་བ་དེ་དམིགས་ཀྱིས་བསལ་བར་བྱེད་དེ་ཁུ་བ་འབྱིན་པ་ལ་སོགས་པ་མི་ཚངས་པར་སྤྱོད་པ་སྤྱད་པར་གཏོགས་པའི་སྦོམ་པོ་ལ་སོགས་པ་ལ་ཁ་ན་མ་ཐོ་བ་གཞན་དུ་ཐལ་བར་འགྱུར་བ་སྟེ། དེའི་ཆ་ནི་དར་གཏོགས་སོ་ཞེས་བྱ་བའི་མདོ་འདིས་སྦོམ་པོ་ལ་སོགས་པ་ཁ་ན་མ་ཐོ་བ་གཞན་དུ་འགྱུར་བ་དམིགས་ཀྱིས་བསལ་བ་འདི་བྱས་པ་ཡིན་ནོ། །

[Block 3676]
ཕྱུང་བ་ཐམས་ཅད་ལ་མཐའ་ཉིད་མ་གཏོགས་པ་ནི་དགེ་འདུན་ལྷག་མའོ་ཞེས་བྱ་བ་ནི་དཔེར་ན་སྤྱད་མི་བཟོད་པའི་བུད་མེད་དང་ལྷན་ཅིག་ཉམས་པར་བྱེད་པ་དང་། མགོ་བཅད་པའི་ཁ་ལ་སོགས་པ་དག་ཏུ་ཉམས་པར་བྱེད་པ་ནི་སྦོམ་པོར་འགྱུར་རོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཞུ་བ་ཁ་ཅིག་དང་གཞན་དག་ལས་ཁུ་བ་འབྱིན་པའི་རྣམ་པ་གསུངས་པ༌[^2420]དག་གམ། དེ་ཐམས་ཅད་ལ་ཐ་མ་ཉིད་མེད་པ༌[^2421]ལ་ཁུ་བ་འབྱིན་པའི་འདུན་པས་ཁུ་བ་འབྱིན་པ་ལ་ཕམ་པ་ཉིད་མ་ཡིན་པ་ཐམས་ཅད་དུ་ནི་ཁུ་བ་འབྱིན་པའི་དགེ་འདུན་ལྷག་མར་ཤེས་པར་བྱའོ། །

[Block 3677]
མདོ་འདི་ནི་སྔར་དེའི་ཆ་ནི་དེར་གཏོགས་སོ་ཞེས་བསྟན་པ་དེའི་སྤྲོས་པ་འདི་ཡིན་ནོ། །

[Block 3678]
འདིར་གང་དག་དགེ་འདུན་གྱི་ལྷག་མར་མི་འགྱུར་ཏེ། མི་ཚངས་པར་སྤྱོད་པའི་སྐབས་ཉིད་ཀྱི་ཕྱིར་འདི་སྙམ་དུ་སེམས་པ་དེའི་བསམ་པ་བཟློག་པའི་ཕྱིར་སྨོས་སོ། །

[Block 3679]
སྦྱོར་བ་གང་ལ་ལྟུང་བ་རྣམ་པར་མ་བཞག་པ་དེ་ལ་ན་སྨད་པའི་ལྟུང་བ་རྣམ་པར་གཞག་པ་ཡང་ཡོད་དེ། གང་དུ་རྣམ་པར་གཞག་པ་དེར་ལྟུང་བྱེད་དོ། །

[Block 3680]
མི་ཚངས་པར་སྤྱོད་པའི་བསམ་པས་བུད་མེད་ཀྱི་ཚོགས་ལ་རེག་པ་ལ་ནི་དགེ་འདུན་ལྷག་མ་ཡིན་ཏེ། སྦྱོར་བ་དེར་གཏོགས་པ༌[^2422]གང་ཞེ་ན། གང་ནས་བརྩམས་ཏེ་དེ་དང་འདྲ་བའི་ཁུ་བ་འབྱིན་པའི་མཐར་ཐུག་པ་ཉིད་དེ་ནས་བརྩམས་ཏེ། དགེ་འདུན་ལྷག་མར་འགྱུར་བ་དང་། སྦྱོར་བ་སྔ་མ་ནི་ཕམ་པར་འགྱུར་བའི་སྦྱོར་བ༌[^2423]ཞེས་བྱའོ། །
--- END BLOCKS ---
