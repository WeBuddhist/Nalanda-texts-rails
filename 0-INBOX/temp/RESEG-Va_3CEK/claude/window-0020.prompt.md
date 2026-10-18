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

[Block 706]
མངོན་པར་མ་གོ་ན་ཅིར་འགྱུར་ཞེ་ན། ཚིག་ཀྱལ་པར་འགྱུར་རོ། །

[Block 707]
ཚིག་ཅེས་བྱ་བ་ནི་རེས་འགའ་ཡི་གེ་མང་པོ་ཞིག་ལས་ཚིག་ཏུ་འགྱུར་ན་དེ་ལ་ལས་ཀྱི་ལམ་གང་ཞིག་ཡིན་ཞེ་ན། ཐ་མ་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་དང་བཅས་པའོ། །

[Block 708]
ཡང་ན་གང་ལས་དོན་གོ་བར་འགྱུར་བ་སྟེ། ཡི་གེ་སྔ་མ་རྣམས་ནི་སྦྱོར་བ་ཡིན་ནོ། །

[Block 709]
དོན་མངོན་པར་གོ་བ་ཞེས་བྱ་བ་ཅི་རེ་ཞིག་ཉན་པ་པོས་དོན་མངོན་པར་གོ་བ༌[^506]ཡིན་ནམ།[^507] འོན་ཏེ་མངོན་པར་གོ་བར༌[^508]ནུས་པ་ཞིག་ཡིན། དེ་ལས༌[^509]ཅིར་འགྱུར། གལ་ཏེ་དོན་མངོན་པར་གོ་བ་ཡིན་ན་ནི་ཚིག་གི་དོན་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་ཡུལ་ཡིན་པའི་ཕྱིར་དང་ངག་གི་རྣམ་པར་རིག་བྱེད་རྣ་བའི་རྣམ་པར་ཤེས་པ་དང་ལྷན་ཅིག་འགགས་པའི་ཕྱིར། རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་ཁོ་ན་ལས་ཀྱི་ལམ་དུ་འགྱུར་རོ། །

[Block 710]
འོན་ཏེ་མངོན་པར་གོ་བར་ནུས་པ་མ༌[^510]ཡིན་ན་ནི་དེ་ལྟ་ནི་ཉེས་པར་མི་འགྱུར་ཏེ། ཇི་ལྟར་ན་མངོན་པར་གོ་བར་ནུས་པ་ཡིན་ཞེ་ན། སྐད་བྱང་བ་དང་རྣ་བའི་རྣམ་པར་ཤེས་པ་སྐྱེས་པའོ། །

[Block 711]
ཇི་ལྟར་ཉེས་པ་མེད་པ་དེ༌[^511]ལྟ་བུ་ཡིན་ནོ། །

[Block 712]
མདོ་ལས་ཐ་སྙད་བཅུ་དྲུག་གསུངས་པ་ལ་མ༌[^512]མཐོང་བ་ལ་མཐོང་ཞེས་སྨྲས་པ་དང་། མ་ཐོས་པ་དང་། མ་རྟོགས་པ་དང་། རྣམ་པར་མ་ཤེས་པ་ལ་རྣམ་པར་ཤེས་སོ་ཞེས་སྨྲ་བ་དང་། མཐོང་བ་ལ་མ་མཐོང་ངོ་ཞེས་སྨྲ་བ་དང་། རྣམ་པར་ཤེས་པའི་བར་ལ་རྣམ་པར་མ་ཤེས་སོ་ཞེས་སྨྲ་བ་དང་བརྒྱད་པོ་འདི་ནི་འཕགས་པ་མ༌[^513]ཡིན་པའི་ཐ་སྙད་དག་ཡིན་ནོ། །

[Block 713]
མཐོང་བ་ལ་མཐོང་ངོ་ཞེས་སྨྲ་བ་ནས་རྣམ་པར་ཤེས་པ་ལ་རྣམ་པར་ཤེས་སོ་ཞེས་སྨྲ་བའི་བར་དང་། མ་མཐོང་བ་ལ་མ་མཐོང་ངོ་ཞེས་སྨྲ་བ་ནས་རྣམ་པར༌[^514]མ་ཤེས་སོ་ཞེས་སྨྲ་བའི་བར་བརྒྱད་པོ་འདི་ནི་འཕགས་པའི་ཐ་སྙད་དག་ཡིན་ནོ། །

[Block 714]
དེ་ལ་མཐོང་བ་དང་ཐོས་པ་དང་། རྟོགས་པ་དང་། རྣམ་པར་ཤེས་པ་དེ་དག་གི་མཚན་ཉིད་ཅི་ཞེ་ན། མིག་རྣ་ཡིད་ཀྱི་རྣམ༌[^515]ཤེས་དང་། །གསུམ་གྱིས་ཉམས་སུ་མྱོང་གང་དེས།[^516] །

[Block 715 [VERSE]]
མཐོང་ཐོས་རྣམ་པར་ཤེས་པ་དང་། །
རྟོགས་པ་ཡིན་ཏེ་གོ་རིམས༌[^517]བཤད། །

[Block 716]
མིག་གི་རྣམ་པར་ཤེས་པས་ཉམས་སུ་མྱོང་བ་གང་ཡིན་པ་དེ་ནི་མཐོང་བ་ཞེས་བཤད་དོ། །

[Block 717]
རྣ་བའི་རྣམ་པར་ཤེས་པས་ཉམས་སུ་མྱོང་བ་གང་ཡིན་པ་དེ་ནི་ཐོས་པ་ཞེས་བཤད་དོ། །

[Block 718]
ཡིད་ཀྱི་རྣམ་པར་ཤེས་པས་ཉམས་སུ་མྱོང་བ་གང་ཡིན་པ་དེ་ནི་རྣམ་པར་ཤེས་པ་ཞེས་བཤད་དོ། །

[Block 719]
སྣ་དང་ལྕེ་དང་ལུས་ཀྱི་རྣམ་པར་ཤེས་པས་ཉམས་སུ་མྱོང་བ་གང་ཡིན་པ་དེ་ནི་རྟོགས་པ་ཞེས་བཤད་དོ། །

[Block 720]
ཅིའི་ཕྱིར་ཞེ་ན། བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ། དྲི་དང་རོ་དང་རེག་བྱ་རྣམས་ནི་ལུང་དུ་མ་བསྟན་པའི་ཕྱིར་ཤི་བ་དང་འདྲ་སྟེ། དེའི་ཕྱིར་དེ་དག་ལ་ནི་རྟོགས་པ༌[^518]ཞེས་ཟེར་རོ། །

[Block 721]
འདི་ལ་ཁུངས་ཅི་ཞིག་ཡོད་ཅེ་ན། མདོ་དང་། རིགས་པ་ཡོད་དེ། རེ་ཞིག་མདོ་ནི་མཆོད་བྱེད་ཀྱི་མ་ཅན་འདི་ཇི་སྙམ་དུ་སེམས། གཟུགས་གང་དག་ཁྱོད་ཀྱི་མིག་གིས་མ༌[^519]མཐོང་སྟེ་སྔོན་མ་མཐོང་ཞིང་མི་ལྟ་ལ། ཁྱོད་འདི་སྙམ་དུ་བལྟ་བར༌[^520]བྱའོ་སྙམ་དུ་ཡང་མི་སེམས་ན། གཞི་དེ་ལས་ཁྱོད་འདུན་པའམ། འདོད་ཆགས་སམ་འདོད་པའམ་དགའ་བའམ། ཆགས་པའམ། འཆུམས་པའམ། ལྷག་པར་ཆགས་པ་སྐྱེ་བའམ།[^521] བཙུན་པ་མ་ལགས་སོ། །

[Block 722]
སྒྲ་གང་དག་ཁྱོད་ཀྱི༌[^522]རྣ་བས་མ་ཐོས་ཏེ། སྔོན་མ་ཐོས་ཞེས༌[^523]བྱ་བ་དང་། རྒྱས་པར་ཡིད་ཀྱིས་ཆོས་རྣམས་རྣམ་པར་མ་ཤེས་ཏེ་ཞེས་བྱ་བ་ནས་རྒྱས་པར་བཙུན་པ་མ་ལགས་སོ་ཞེས་བྱ་བའི་བར་དུའོ། །

[Block 723]
མཆོད་བྱེད་ཀྱི་མ་ཅན་ཁྱོད་འདི་ལ་མཐོང་ན་ཡང་མཐོང་བ་ཙམ་དུ་འགྱུར་ལ། ཐོས་པ་དང་། རྟོགས་པ་དང་། རྣམ་པར་ཤེས་པ་ཡང་རྣམ་པར་ཤེས་པ་ཙམ་དུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ཏེ། དེའི་ཕྱིར་ཡུལ་གསུམ་ལ་མཐོང་བ་དང་། ཐོས་པ་དང་། རྣམ་པར་ཤེས་པའི་སྒྲས་བསྟན་པའི་ཕྱིར་དྲི་ལ་སོགས་པ་ལ་རྟོགས༌[^524]ཞེས་བྱ་བར་གོ་འོ།[^525] །དེ་ལྟར་མི་འདོད་ན་མཐོང་བ་ལ་སོགས་པའི་དངོས་པོའི་ནང་དུ་མ་གཏོགས་པའི་ཕྱིར་དྲི་ལ་སོགས་པ་ལ་ཐ་སྙད་འདོགས་པར་ཡང་མི་འགྱུར་ཏེ། འདི་ནི་རིགས་པ་ཡིན་ནོ། །

[Block 724]
རེ་ཞིག་མདོ་འདི༌[^526]དོན་གཞན་ཡིན་པའི་ཕྱིར། ཁུངས་མ་ཡིན་ཏེ། བཅོམ་ལྡན་འདས་ཀྱིས་མདོ་འདི་ལ༌[^527]ཐ་སྙད་རྣམས་ཀྱི་མཚན་ཉིད་བསྟན་པ་དེ༌[^528]ནི་མ་ཡིན་ནོ། །

[Block 725]
འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན། འདིར་ནི་ཁྱོད་ཡུལ་རྣམ་པ་དྲུག་པོ་འདི་ལ་མཐོང་བ་ལ་སོགས་པའི་ཐ་སྙད་བཞི་ལ་མཐོང་བ་ལ་སོགས་པའི་ཐ་སྙད་ཙམ་དུ་འགྱུར་གྱི་སྡུག་པ་དང་མི་སྡུག་པའི་མཚན་མར་སྒྲོ་འདོགས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་ནི༌[^529]མདོའི་དོན་ཡིན་པར་སྣང་ངོ་། །ཡང་མཐོང་བ་ནི་ཅི་ཞིག་ཡིན། རྣམ་པར་ཤེས་པའི་བར་དུ་ཡང་ཅི་ཞིག་ཡིན་ཞེ་ན། རེ་ཞིག་ཁ་ཅིག་ན་རེ་དབང་པོ་ལྔས་མངོན་སུམ་དུ་བྱས་པ་གང་ཡིན་པ་དེ་ནི་མཐོང་བའོ། །

[Block 726]
ཕ་རོལ་ལས་འོངས་པ་གང་ཡིན་པ་དེ་ནི་ཐོས་པའོ། །

[Block 727]
བདག་ཉིད་ཀྱི༌[^530]རིགས་པས་རྗེས་སུ་དཔག་པའི་སྒོ་ནས་འདོད་པ་གང་ཡིན་པ་དེ་ནི་རྟོགས་པའོ། །

[Block 728]
ཡིད་ཀྱི་མངོན་སུམ་དུ་གྱུར་པ་བསྒོམས་ནས་རྟོགས་པ་སོ་སོ་རང་གིས་རིག་པར༌[^531]བྱ་བ་གང་ཡིན་པ་དེ་ནི་རྣམ་པར་ཤེས་པའོ། །

[Block 729]
ཡང་ཡུལ་ལྔ་པོ་འདི་དག་རེ་རེ་ལ་ཡང་མཐོང་བའམ་ཐོས་པའམ། རྟོགས་པའམ། རྣམ་པར་ཤེས་པ་ཡིན་ནོ་ཞེས་ཐ་སྙད་གདགས་ལ།

[Block 730]
དྲུག་པ་ལ་ནི་མཐོང་བ་མ་གཏོགས་ཏེ། དེ་ལྟར་ན་དྲི་ལ་སོགས་པ་ལ་ཐ་སྙད་འདོགས་པ་མེད་པར་ཐལ་བར་འགྱུར་བ་ཡང་མེད་དེ། དེ་ལྟ་བས་ན་རིགས་པ་དེ་ཡང་རིགས་པ་མ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 731]
སྔོན་གྱི་སློབ་དཔོན་རྣམས་ནི་འདི་སྐད་དུ། མིག་གིས་མངོན་སུམ་དུ་བྱས་པ་གང་ཡིན་པ་དེ་ནི་མཐོང་བའོ། །

[Block 732]
རྣ་བས་ཐོས་པ་དང་། ཕ་རོལ་ལས་འོངས་པ་གང་ཡིན་པ་དེ་ནི་ཐོས་པའོ། །

[Block 733]
བདག་ཉིད་ཀྱིས་བསམ་པ་གང་ཡིན་པ་དེ་ནི་རྟོགས་པའོ། །

[Block 734]
བདག་ཉིད་ཀྱིས་སོ་སོར་ཡང་དག་པར་རིག་པ་དང་རྟོགས་པ་གང་ཡིན་པ་དེ་ནི་རྣམ་པར་ཤེས་པའོ་ཞེས་ཟེར་རོ། །

[Block 735]
ཞར་ལ༌[^532]འོངས་པ་རྫོགས་སོ།། །།

[Block 736]
བསྟན་བཅོས་ལ་འཇུག་པར་བྱ་སྟེ། གང་ཞིག་ལུས་ཀྱི༌[^533]དོན་གཞན་གོ་བར་བྱེད་ན་བརྫུན་དུ་སྨྲ་བར་འགྱུར་རམ་ཞེ་ན། འགྱུར་རོ། །

[Block 737]
དེ་ཉིད་ཀྱི་ཕྱིར། ལུས་ཀྱིས༌[^534]མི་བྱེད་ན་སྲོག་གཅོད་པའི་ཁ་ན་མ་ཐོ་བའི༌[^535]རེག་པར་འགྱུར་བ་ཡོད་དམ་ཞེ་ན་ཡོད་དོ། །

[Block 738]
ངག་གིས༌[^536]བྱེད་པར་འགྱུར་ནའོ། །

[Block 739]
ངག་གིས་མི་བྱེད་ན་བརྫུན་གྱི༌[^537]ཁ་ན་མ་ཐོ་བས་རེག་པར་འགྱུར་བ་ཡོད་དམ་ཞེ་ན་ཡོད་དོ། །

[Block 740]
[^538]ལུས་ཀྱིས་བྱེད་པར་འགྱུར་ནའོ། །
--- END BLOCKS ---
