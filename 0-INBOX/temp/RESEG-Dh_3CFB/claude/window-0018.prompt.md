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
[Block 631 [HEADING]]
### རང་གི་མཚན་ཉིད་ལ་སྒྲ་རྣམས་མི་སྦྱོར་བ། ^4-2-0

[Block 632]
ཡང་ཅིའི་ཕྱིར་རང་གི་མཚན་ཉིད་ལ་སྒྲ་རྣམས་མི༌[^474]སྦྱོར་ཞེ་ན།

[Block 633 [VERSE]]
སྒྲ་རྣམས་ཀྱིས་ནི་བརྡར་བཏགས༌[^475]སྟོན། །
དེ་ནི་ཐ་སྙད་ཆེད་དུ་བྱས། །
དེ་ཚེ་རང་གི་མཚན་ཉིད་མེད། །
དེས་ན་དེ་ལ་བརྡར་མ༌[^476]ཡིན། །

[Block 634]
སྒྲ་རྣམས་ཀྱིས་ནི་བརྡར་བཏགས་པའི་དོན་རབ་ཏུ་སྟོན་པར་བྱེད་ལ། བརྡ་ཡང་ཅི་ནས་ཀྱང་དུས་ཕྱིས་བརྡར་བྱས་པའི་སྒྲ་འདི་ལས་དོན་འདི་རྟོགས་པར་འགྱུར་སྙམ་ནས་ཐ་སྙད་ཀྱི་དོན་དུ་འདོགས་ན། སྔར་རང་གི་མཚན་ཉིད་ལ་བརྡར་བྱས་པའི་སྒྲ་ཕྱིས་སྦྱོར་བ་ནི་རིགས་པ་མ་ཡིན་ཏེ། དེ་ནི་བསལ་བ༌[^477]ཡུལ་དང་དུས་ཀྱི་ཐ་དད་པ་ལ་མི་འབྲང་བའི་ཕྱིར་རོ། །

[Block 635]
དེ་ལྟ་བས་ན་རང་གི་མཚན་ཉིད་ལ་བརྡར་བྱེད་པ་མ་ཡིན་ནོ། །

[Block 636]
འོ་ན་ཅི་ཐ་དད་པའམ་ཐ་མི་དད་པ་ཁྱད་པར༌[^478]ཞིག་སྒྲ་རྣམས་ཀྱིས་བརྗོད་དེ། དེ་བས་ན་ཐ་སྙད་ཀྱི་དུས་ན་མེད་པའི་ཉེས་པ་མེད་དོ་ཞེ་ན། དེ་ནི་མ་ཡིན་ཏེ། འདི་ལྟར།

[Block 637 [VERSE]]
ཅི་ལྟར༌[^479]སྐྱེས་བུ་དོན་བྱེད་པར། །
ནུས་པ་ཤེས༌[^480]ནས་དེ་བསྒྲུབ༌[^481]ཕྱིར། །
འཇུག་པར་འགྱུར་ཞེས་དོན་རྣམས་ལ། །
རྗོད་པར་བྱེད་པ་སྦྱོར་བར་བྱེད། །

[Block 638]
འཇིག་རྟེན་ལ་ནི་འདི་བརྡ་མི་བྱེད་པའམ། སྒྲ་མི་སྦྱོར་བས་སྡུག་བསྔལ་བར་འགྱུར་བའི་ཉམ་ང་བ་གང་ཡིན་པ་འདི་ནི་མེད་པ་ཉིད་དོ། །

[Block 639]
འོ་ན་ཅི་ཞེ་ན། འདིའི་རྩོམ་པ་འབྲས་བུའི་དོན་ཅན་རིལ་མཁོ་བ་ཁོ་ནར་བརྩི༌[^482]སྟེ། རྩོམ་པ་འབྲས་བུ་མེད་པ་ནི་ཡལ་བར་དོར་བར་བྱ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 640]
དེ་བས་ན་འགའ་ཞིག་ལ་སྒྲ་སྦྱོར་བ་འདིས་ཀྱང་འབྲས་བུ་འགའ་ཁོ་ན་ལ་བལྟ་བའི་རིགས་སོ། །

[Block 641]
དེ་ནི་ཐམས་ཅད་ཀྱང་འདོད་པ་དང་མི་འདོད་པ་དག་འདོར་བ་དང་ཐོབ་པའི་མཚན་ཉིད་ཡིན་ཏེ། དེའི་ཕྱིར༌[^483]འདོད་པ་དང་མི་འདོད་པ་དག་གི་བསྒྲུབ་པ་དང་སྒྲུབ༌[^484]པ་མ་ཡིན་པར་ཤེས་པར༌[^485]བྱས་ནས། དེ་ལ་འཇུག་པ་དང་ལྡོག་པ་དག་བྱ་བའམ། བྱེད་དུ་གཞུག་པའམ། སྦྱོར་བ་ལ་གུས་པར་འགྱུར་བའི་སྒྲ་རྣམས་སྦྱར་བར་བྱའོ། །

[Block 642]
དེ་ལྟ༌[^486]མ་ཡིན་ན་ཡལ་བར་དོར་བར་བྱ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 643]
དེ་ལ་རིགས་དོན་བྱེད་རུང་མིན། །རིགས་ནི་གཞོན་པ༌[^487]དང་བཞོ་བ༌[^488]ལ་སོགས་པ་འགའ་ལ་ཡང་ཉེ་བར་གནས་པ་མ་ཡིན་ནོ། །

[Block 644]
དེ་ལྟ་བུའི་སྐབས་མེད་པར་འཇིག་རྟེན་ན༌[^489]ཐ་སྙད་དག་ལ་སྒྲ་སྦྱོར་བ་ཡང་མེད་དོ། །

[Block 645]
གལ་ཏེ་གསལ་བར་བསྟན་པར་མི་ནུས་པའི་ཕྱིར། མཚོན་ཟིན་པས་མཚོན་པར་བྱ་བའི་རིགས་བརྗོད་དོ་ཞེ་ན། འབྲེལ་པ་ཡིན༌[^490]དུ་ཟིན་ཀྱང་སྒྲས་མ་བརྗོད་པ་ལ་ཇི་ལྟར་འཇུག་པར་འགྱུར་ཏེ། འགའ་ཞིག་ལ་འཁར་བ་ཆོད་ཅིག་ཅེས་སྨྲས་ན། འཁར་བ༌[^491]ཐོགས་པ་གཅོད་པ་ནི་མེད་དོ། །

[Block 646]
མི་སྲིད་པའི་ཕྱིར་བསལ་བ༌[^492]ལ་འཇུག་པ་ཡང་མ་ཡིན་ཏེ། དེ་ལྟར་ན་རྣར་མི་འོང་བ་སྨྲ་བར་འགྱུར་གྱི། དེ་ལས་གཞན་ལ་འཇུག་པ་མ་ཡིན་ཏེ། གླང་འཇོ་བར་བརྗོད་པ་བཞིན་ནོ། །

[Block 647]
དོན་གཞན་བརྗོད་ན་དོན་གཞན་མཚོན་པ་ཡང་མ་ཡིན་ཏེ། འབྲེལ་པ་ཡིན་དུ་ཟིན་ཀྱང་འཁར་བ༌[^493]ཞེས་བྱ་བའི་སྒྲས་འཁར་བ་ཐོགས་པ་རྟོགས་པ་ནི་མེད་དོ། །

[Block 648]
གལ་ཏེ་འབྲེལ་པ་མ་ངེས་པ་ཅན་ཉིད་ཀྱི་ཕྱིར་དེ་ལ་མི་འཇུག་གོ་ཞེ་ན། དེ་ནི་རིགས་ལ་ཡང་མཚུངས་ཏེ། བསལ་བ༌[^494]རྣམས་བསལ༌[^495]ན་རིགས་འབའ་ཞིག་འདུག་པའི༌[^496]ཕྱིར་རོ། །

[Block 649]
སྤུན་དྲུང་ཞེས་བྱ་བ་ལ་སོགས་པའི་སྒྲ་རྣམས་ནི་འབྲེལ་པ་ཅན་གྱི་སྒྲ་ཡིན་པའི་ཕྱིར་གཞན་འཕེན་པར་འགྱུར་གྱི། [^497]བ་ལང་ཉིད་ལ་སོགས་པའི་སྒྲ་ནི་དེ་ལྟར་འབྲེལ་པ་ཅན་རྗོད་པར༌[^498]བྱེད་པ་མ་ཡིན་ཏེ། རིགས་བསལ༌[^499]བ་དང་བྲལ་བ་ཅན་དག་གིས་ཀྱང་དེའི་སྒྲ་དག་ལས་རྟག་ཏུ་རྗེས་སུ་འགྲོ་བར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 650]
གལ་ཏེ་དུས་ཐམས་ཅད་དུ་དེ་དང་འབྲེལ་བར་རུང་བ་ཉིད་དུ་ཤེས་པའི་ཕྱིར་འདོད་པ་ཁོ་ནའོ་ཞེ་ན། འོ་ན་ནི་དུས་ཐམས་ཅད་དུ་བ་ལང་ཞེས་བྱ་བའི་སྒྲ་ལས་འཇུག་པར་མི་འགྱུར་ཏེ། ལྷན་ཅིག་པ༌[^500]དང་ལྷན་ཅིག་པ་མ་ཡིན་པའི་གནས་སྐབས་དག་ཏུ་ཁྱད་པར་དུ་མ་འཕངས་པའི་ཕྱིར་རོ། །

[Block 651]
གལ་ཏེ་བསལ་བ༌[^501]དང་འབྲེལ་པ་ཅན་གྱི་རིགས་བརྗོད་པའི་ཕྱིར་ཉེས་པ་མེད་དོ་ཞེ་ན། འོ་ན་ནི་དེ་ཡང་དེའི་ཁྱད་པར་ཉིད་དུ་གནས་པས་བསལ་བ༌[^502]འཕངས་པ་ཁོ་ནའི་ཕྱིར་དེ་དང་ལྡན་པ་བརྗོད་པར་བྱ་བ༌[^503]ཡིན་པར་འགྱུར་རོ། །

[Block 652]
རིགས་པ༌[^504]དང་བསལ་བ༌[^505]དག་འབྲེལ་བ་ཡང་འགའ་ཡང་མེད་དེ། ཕན་ཚུན་བསྐྱེད་པར༌[^506]བྱ་བ་དང་སྐྱེད་པར་བྱེད་པ་ཉིད་དུ་ཕན་འདོགས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 653]
དེའི་ཕྱིར་མཚོན་པར་ཡང་རིགས་པ༌[^507]མ་ཡིན་ནོ། །

[Block 654]
དེ་ལྟ་བས་ན་རིགས་ལ་སྒྲ་སྦྱོར་བ་ནི་མ་ཡིན་ཏེ། འབྲས་བུ་མེད་པའི་ཕྱིར་རོ། །

[Block 655]
དེ་ལྟ་ན་འོ་ན། དེ་ལྡན། དོན་བྱེད། ནུས་པ་ཞེས་བྱ་བ་དེ་ལ་སྒྲ་སྦྱོར་རོ་ཞེ་ན། དེ་ཡང་ནི། ཅིའི་ཕྱིར༌[^508]དངོས་སུ་སྦྱོར་མི་བྱེད། །གལ་ཏེ་བསལ་བ་ལ༌[^509]སྒྲ་སྦྱོར་བས་འབྲས་བུ་དང་ལྡན་པ་ཡིན་ན་སྒྲ་དེ་ཅིའི་ཕྱིར་བསལ་བ༌[^510]རྣམས་ལ་དངོས་སུ་མི་སྦྱོར། དེ་ལ་བར་དུ་གཅོད་པས༌[^511]གཞན་གྱིས་ཅི་ཞིག་བྱ། གལ་ཏེ་མཐའ་ཡས༌[^512]ཕྱིར་འདི་མཚུངས། །གལ་ཏེ་འདི་སྙམ་དུ་བསལ་བ༌[^513]རྣམས་ནི་མཐའ་ཡས་པའི་ཕྱིར་སྒྲས་བརྗོད་པར་མི་ནུས་སོ་སྙམ་དུ་སེམས་ན། དེ་ལྟ་ཡིན་ན་མཐའ་ཡས་པ་འདི་ནི་དེ་དང་ལྡན་པ་ལ་ཡང་མཚུངས་སོ། །

[Block 656]
རིགས་ཀྱི༌[^514]ཁྱད་པར་དུ་བྱས་པའི་བསལ་བ༌[^515]དག་ཀྱང་བརྗོད་པར་བྱ་བ་ཁོ་ན་ཡིན་པས་འབྲེལ་པ་མ་བྱས་པ་ཅན་ནི་བརྗོད་དུ་མི་རུང་བའི་ཕྱིར་གདོན་མི་ཟ་བར་དེ་ལ༌[^516]འབྲེལ་པ་བྱ་དགོས་ན་དེ་ཡང་མི་ནུས་སོ། །

[Block 657]
གལ་ཏེ་དེ་དང་འབྲེལ་པ་ཅན་ལ་བྱས་པའི་ཕྱིར། དེ་ལ་ཡང་བྱས་པ་ཁོ་ན་ཡིན་ནོ་ཞེ་ན། འདི་ལ་བཤད་ཟིན་ཏེ། འབྲེལ་པ་ཡོད་དུ་ཟིན་ཀྱང་གཅིག་ལ་བྱས་པས་གཞན་ལ་རྟོགས་པ་ནི་མེད་ལ། འབྲེལ་པ་ཡང་མེད་དོ་ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 658]
གཞན་ཡང་།

[Block 659 [VERSE]]
དེ་བྱེད་དེ་བྱེད་མ་ཡིན་ལས། །
ལོག་པར་མཚུངས་པ༌[^517]ཅིས་མ་བྱས། །

[Block 660]
དོན་བྱེད་པ་གང་གི་དབང་དུ་བྱས་ནས་དོན་རྣམས༌[^518]གཞན་དག་ལས་ཐ་དད་པའི་ཕྱིར། དེ་དག་གི་ཐ༌[^519]དད་པ༌[^520]ཁོ་ན་ལ་སྒྲ་ཅི་སྟེ་མི་སྦྱོར།

[Block 661 [VERSE]]
གལ་ཏེ་དེ་ལྡན་ཉེས་མཚུངས་ཕྱིར། །
བླ་སྟེ་རིགས་གཞན་མི་དགོས་སོ། །

[Block 662]
གལ་ཏེ་འདི་སྙམ་དུ་སྒྲའི་དོན་དེ་ལས་གཞན་པ་ལས་ལྡོག༌[^521]པ་ལ་ཡང་ལྡོག་པས་ཁྱད་པར་དུ་བྱས་ཤིང་དེ་དང་ལྡན་པ༌[^522]བརྗོད་པའི་ཕྱིར་དེའི་ཕྱོགས་ལས་ཁྱད་པར་མེད་དེ། ལྡོག་པ་དང་རིགས་དང་། ལྡོག་པ་དང་ལྡན་པ་དང་། [^523]རིགས་དང་ལྡན་པ་ཞེས་བྱ་བ་འདི་ལ་ཁྱད་པར་ཅི་ཞིག་ཡོད་སྙམ་དུ་སེམས་ན། དེ་དང་ལྡན་པའི་ཉེས་པ་ལྟ་བུར་གྱུར་ཀྱང་བླ་སྟེ། རིགས་གཞན་ནི་མི་དགོས་སོ། །

[Block 663]
རིགས་ཁས་ལེན་པས་ཀྱང་གདོན་མི་ཟ་བར་དངོས་པོ་རྣམས་ཁས་བླངས༌[^524]དགོས་ཏེ། དེ་མེད་ན་དེ་ཡང་མེད་པར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 664]
གཅིག་ལས་ཐ་དད་པ་དེ་ལས་གཞན་པ་རྣམས་ཀྱི་ཐ་མི་དད་པ་དེ་ཉིད་དེས་ཁྱད་པར་དུ་བྱས་པའི་དོན་རྣམས་ལ་རྟོགས་པར་འགྱུར་ཏེ། རྣམ་པ་ཐམས་ཅད་དུ་ཉེས་པ་ཡོངས་སུ་སྤང་བར་བྱ་བར་མི་ནུས་བའི་ཕྱིར་རོ། །

[Block 665]
དོན་གཞན་ཁས་བླང་དུ་ནི༌[^525]དགོས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 666]
དོན་དེ་ནི་གཞན་གྱིས་བསྒྲུབ་པའི༌[^526]ཕྱིར་རོ། །

[Block 667]
དེ་ལ་ཁས་བླངས་པ་ཡང་གདོན་མི་ཟ་བར་བྱ་དགོས་པའི་ཕྱིར་རོ། །

[Block 668]
གཞན་ཡང་།

[Block 669 [VERSE]]
དེ་ལས་གཞན་པ་ཡོངས་སྤངས་ནས། །
འཇུག་འགྱུར་ཞེས་ཀྱང་སྒྲ་བརྗོད་དེ། །
དེ་ཡིས་དེ་དག་རྣམས་ལས་འདི། །
རྣམ་མི་གཅོད་པ༌[^527]དེ་ཇི་ལྟར། །

[Block 670]
འདི་དོན་རྣམས་ལ་སྒྲ་སྦྱོར་བ་ན་མི་འདོད་པ་ཡོངས་སུ་སྤངས་ནས་འཇུག་པར་འགྱུར་སྙམ་ནས་སྦྱོར་ཏེ། དེ་དང་གཞན་ལ་ཡང་འཇུག་ཏུ་སྣང་ལ། འཇུག་པ་དང་ལྡོག་པ༌[^528]ཡང་འཇུག་ཏུ་སྣང་ན་ནི་མིང་སྨོས་པ་དོན་མེད་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
