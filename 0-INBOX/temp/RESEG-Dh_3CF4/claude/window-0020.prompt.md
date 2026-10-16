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
རྫིང་བུའི༌[^383]འགྲམ་ན་ཞེས་བྱ་བ་ནས་སྐྱིལ་མོ་ཀྲུང་བཅས་ཏེ་ཞེས་བྱ་བའི་བར་གྱི་ཚིག་གི་བསྡུས་པའི་དོན་ནི་མིག་གཉིས་མེད་པས་མིག་གི་ཡུལ་མ་བསྟན་ཏེ། རེག་བྱ་དང་། དྲི་དང་། སྒྲའི་ཡུལ་དང་ལྡན་པ་ཡིན་ནོ། །

[Block 702]
དེས་ཀྱང་ཡིད་དུ་འོང་བར་བསྟན་པ་ཡིན་ཏེ། ཇི་ལྟར་རིགས་པར་སྦྱར་བར་བྱའོ། །

[Block 703]
བརྒྱ་བྱིན་མདུན་དུ་འོངས་ནས་འདི་སུ་ཞེས་དྲིས་པ་སྟེ། མི་ལས་ཁྱད་པར་དུ་གྱུར་པ་ཞིག་ཡིན་པར་རྟོགས་སོ། །

[Block 704]
ཡང་ན་ལྷའི་དབང་པོ་ཉིད་ཀྱིས་རང་འོངས་པར་བརྡ་ཕྲད་པའི་ཕྱིར་རྐང་པའི་སྒྲ་བྱས་པར་གྱུར་ཏོ། །

[Block 705]
གཞན་དུ་ན་དྲི་བའི་སྐབས་མེད་པར་འགྱུར་རོ། །

[Block 706]
འདི་སུ་ཞེས་དྲིས་པ་དང་། འདི་ལྟར་དེ་ཉིད་སྨྲས་པ། ཁྱོད་ཀྱི་དྲུང་དུ་འོངས་སོ་ཞེས་པ་སྟེ་སྐབས་དབྱེ་བའི་ཕྱིར་རོ། །

[Block 707]
བཀའ་སྩལ་དུ་གསོལ་ཞེས་བྱ་བའི་ཚིག་ནི་ཞེ་ས༌[^384]དང་བཅས་པ་དང་ཞེས་བྱ་བ་ཡིན་ཏེ། མདུན་བསུ་བ་ལ་སོགས་པ་སྔོན་དུ་འགྲོ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 708]
མཆོག་སློངས་ཤིག་ཞེས་བཤད་པ་ནི་ཅི་འདོད་པ་སྨོས་ཤིག་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 709]
མཆོག་འདི་ཉིད་དུ་ངེས་པར་གཟུང་བའི༌[^385]དངོས་པོ་བསྟན་པའི་ཕྱིར། བརྒྱ་བྱིན་བདག་ལ་ནོར་མང་ཞིང་།[^386] །ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་བསྟན་པ་ཡིན་ཏེ། འདི་ལུས་སུ་གཞག་པ༌[^387]ནི་མཆོག་སློང་བའི་འབྱོར་པའི་མཚན་ཉིད་རྣམ་པ་གཉིས་ཏེ། ཕྱི་རོལ་གྱི་དངོས་པོ་དང་འབྲེལ་པ་དང་། ནང་གི་དངོས་པོ་དང་འབྲེལ་པ་དང་། དེ་གཉི་གའི་དོན་བསྟན་པའི་ཕྱིར་ཕྱི་རོལ་ཡང་རྣམ་པ་གཉིས་ཏེ། སེམས་ཅན་དང་སེམས་ཅན་མ་ཡིན་པའོ། །

[Block 710]
སེམས་ཅན་མ་ཡིན་པ་ནི་ནོར་དང་འབྲུ་ལ་སོགས་པ་ཡིན་ཏེ། ནོར་མང་ཞེས་བྱ་བ་སྨོས་པའོ། །

[Block 711]
མང་པོ་ཞེས་བྱ་བ་སྨོས་པས་ནི་དེ་ལས་གཞན་པའི་སེམས་ཅན་མ་ཡིན་པ་གཟུང༌[^388]ངོ་། །སེམས་ཅན་ནི་མཐུ་དང་གུས་པ་དང་ལྡན་པར་བསྟན་པ་སྟེ། དམག་ཚོགས་ཆེ་ལ་ཞེས་སྨོས་པས་སོ། །

[Block 712]
ཕྱི་རོལ་དང་སེམས་ཅན་མཐའ་དག་ཕུན་སུམ་ཚོགས་པ་བཟུང་བས་ནི་ནང་གི་དངོས་པོ་ཡང༌[^389]ཕུན་སུམ་ཚོགས་པར་བསྟན་ཏོ། །

[Block 713]
འོན་ཀྱང་སྔར་དེ་ལྟ་བུའི་རྣམ་པ་ཡིན་ན་ཡང་ལོང་བ་དག་ལ༌[^390]མིག་བྱིན་པས་དེས་ན་མཆོག་འདི་སློང་ངོ་ཞེས་བྱ་བ་ཡིན་ཏེ། ལོང་བར་གྱུར་པས་ཞེས་བྱ་བ་སྨོས་པ་ཡིན་ནོ། །

[Block 714]
གང་གོང་དུ་བསྟན་པ་དེ་བསྟན་པས་ངོ་མཚར་མི་ཆེ་ཞིང་རླབས་ཅན་དུ་ཞེས་བྱ་བ་ཡིན་ཏེ། འདི་ནི་ངོ་མཚར་མི་ཆེ་ཞིང་བརྟན་པས་རླབས་ཅན་དུ་སྨྲས་པ་སྟེ། ངོ་མཚར་མེད་པས་གང་གི་ཕྱིར་མཆོག་དང་མཆོག་མ་ཡིན་པ་ཚོལ་བ༌[^391]ལའོ། །

[Block 715]
བདག་ཉིད་ཀྱི་ཡོན་ཏན་དང་ལྡན་པས་སྔོན་མ་བྱུང་བའི་ངོ་མཚར་མེད་པའི་ཕྱིར་རོ། །

[Block 716]
ནོར་མང་པོ་ཡོད་ཅིང་དམག་ཚོགས་ཆེ་ལ་མཐུ་དང་ཡང་ལྡན་པ་ཡིན་ནོ། །

[Block 717]
གལ་ཏེ་དེ་ལྟར་གཉི་ག་དང་ལྡན་པ་ཡིན་ན་ཅིའི་ཕྱིར་མཆོག་ཚོལ་བར༌[^392]བྱེད་ཅེ་ན། དེ་བསྟན་པ་ཡིན་ན།[^393] ལོང་བར་གྱུར་པས་འདི་ལྟ་བུའི་གནས་སྐབས་འདི་ལས་ནི་འཆི་བ་ཉིད་འདོད་དོ་ཞེས་མཆོག་སློང་བའི་ཚིག་གི་རྣམ་པ་ཡིན་ནོ། །

[Block 718]
ངོ་མཚར་མི་ཆེ་བ་དང་རླབས་ཅན་དུ་སྨྲ་བ་ནི་གང་གིས༌[^394]མཆོག་ཀྱང་མི་ལེན་པ་སྟེ། དེ་བས་ན་དེ་སྨོས་སོ། །

[Block 719]
བདག་ལ་ནོར་མང་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིའི་དོན་གཞན་དུ་ནི་བསོད་ནམས་ཀྱི་ཚོགས་ཀྱི་འབྲས་བུའི་མཚན་ཉིད་ནི་རྣམ་པ་གསུམ་སྟེ་མཆོག་སྦྱིན་པར་བྱ་བ་དང་། ཁྱོད་ཀྱིས་སྦྱིན་པར་བྱ་བ་དང་། བདག་ལ་སྦྱིན་པའོ་སྦྱིན་པར་བྱ་བ་དེ་ལས་ནི་གཉིས་ཡོད་དེ། བཟོད་པའི་བསོད་ནམས་ཀྱི་ཚོགས་ཀྱི་འབྲས་བུའི་མཐུ་དང་ལྡན་པ་དང་། དམག་ཚོགས་ཡོད་པའོ། །

[Block 720]
ད་ནི་ཞེས་བྱ་བས་ནི་ཚུལ་ཁྲིམས་ཀྱི་བསོད་ནམས་ཀྱི་ཚོགས་ཀྱི་འབྲས་བུ་ནང་གི་ཕུན་སུམ་ཚོགས་པ་ཡིན་ཏེ། དེ་ཡང་ཡོད་པ་ལས་མེད་པ་སྟེ། གང་ཡིན་ཞེ་ན། མིག་མེད་པའོ། །

[Block 721]
དེ་མཆོག་འདི་སློང་ངོ་ཞེས་བྱ་བ་ནི་འདི་ལྟར་ལོང་བའི༌[^395]གནས་སྐབས་སུ་གྱུར་པས་འཆི་བ་འབའ་ཞིག་མངོན་པར་འདོད་ཅེས་བྱ་བ་ཡིན་ནོ། །

[Block 722]
སྔར་བཤད་པ་སྟེ། ངོ་མཚར་མི་ཆེ་བའི་རླབས་ཅན་དུ་འདིས་བསྟན་པ་ཡིན་ཏེ། ཚིགས་བཅད་འདིའི༌[^396]དོན་གྱིས་སོ། །

[Block 723]
ཚིགས་བཅད་ཀྱི་དོན་གཉིས་སུ་ཡང་འགྱུར་བ་སྟེ། ལོང་བར་གྱུར་པས༌[^397]ཞེས་བྱ་བ་ནི་ལྔ་པ་རྒྱུའི་མཚན་ཉིད་དེ། ལོང་བ་ཉིད་ཀྱི་རྒྱུས་འཆི་བ་འབའ་ཞིག་མངོན་པར་འདོད་ཅེས་སྦྱར་ཏེ། འདི་ལྟར་འདིའི་དོན་དུ་ཡང་འགྱུར་རོ། །

[Block 724]
འདི་ལྟའི་གནས་སྐབས་གྱུར་བྱས་ནས།[^398] །ཞེས་བྱ་བ་ནི་མིག་མེད་པའི་གནས་སྐབས་སོ། །

[Block 725]
ད་ནི་དེ་ལ་ཁྱོད་ཀྱི་ཡིད་ནི་ཅི་སྙམ་སེམས། །ཞེས་བྱ་བ་ནི་འདི་དང་རྗེས་སུ་མཐུན་པའི་ཚིག་བཤད་པ་སྟེ། ཚིག་རྐང་གསུམ་གྱིས་སོ། །

[Block 726]
ཅི་ནས་ཡིད་ནི་རབ་ཏུ་ཆེས་པར་འགྱུར་བ༌[^399]རུ། །ཞེས་བྱ་བ་ནི་དེ་དང་རྗེས་སུ་མཐུན་པར་བཤད། །བདག་གི་མིག་ནི་ཡ་གཅིག་མཐོང་བར་ཤོག །ཅེས་བྱ་བའི་བདེན་པའི་བྱིན་རླབས་ཀྱི་མཐུ༌[^400]ཞེས་བྱ་བ་ནི་ད་ལྟར་བྱུང་བའི་དགེ་བའི་སེམས་ཀྱི་སྟོབས་སོ། །

[Block 727]
བསོད་ནམས་སྤེལ་བའི༌[^401]ཁྱད་པར་གྱིས། །ཞེས་བྱ་བ་ནི་རྒྱུའི་སྟོབས་སོ། །

[Block 728]
ཇི་ལྟ་བུའི་བསོད་ནམས་བསགས་པའི་ཁྱད་པར་གྱིས་ཤེ་ན་སྨྲས་པ། མིག་གི་སྦྱིན་པ་ལ་བྱུང་བའི་ལས་བྱས་པ་ལས་ཉེ་བར་བསགས་པས་སོ། །

[Block 729]
དེ་སྐད་སྨྲས་མ་ཐག་ཏུ་ཞེས་བྱ་བ་ནི་བདེན་པའི་བྱིན་གྱི༌[^402]རླབས་ཀྱི་མཐུས་སྐྱེས་མ་ཐག་ཉིད་དོ། །

[Block 730]
ཨནྡ་རྙིལ་གྱིས་སྤྲས་པ་ཞེས་བྱ་བ༌[^403]ལ་སོགས་པས་ནི༌[^404]བདེན་པའི་བྱིན་གྱི་རླབས་ཀྱི་སྟོབས༌[^405]ཀྱིས་མིག༌[^406]ཁྱད་པར་ཅན་སྐྱེས་པར་སྟོན་པ་ཡིན་ནོ། །

[Block 731]
མིག་སྔ་མ་ལ་འགྲན་པ་བཞིན་ཞེས་བྱ་བ་ནི་སྔར་སྐྱེས་པའི་མིག་གི་ཡོན་ཏན་དང་ལྡན་པ་བཞིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 732]
ལྷ་རྣམས་ཀྱིས་ནི༌[^407]རྔ་བོ་ཆེ་དག་ཀྱང་། །ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་རེག་པར་བྱ་བ་དང་བལྟ་བར་བྱ་བ་དང་། བསྣམ༌[^408]པར་བྱ་བ་སྟེ་དོན་གསུམ་སྟོན་ཏོ། །

[Block 733]
ཡིད་དུ་འོང་བ་ཞེས་བྱ་བས་ནི། རེག༌[^409]པར་བྱ་བའོ། །

[Block 734]
རྒྱལ་པོའི་སྤྱོད་མཆོག་བསྟོད་པའི་གཞི་ཞེས་བྱ་བ་ནི་དོན་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 735]
སྙན་པའི་ཚིག་རྣམས་ཀུན་ཏུ་ཞེས་བྱ་བས་ནི་སྒྲ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 736]
སྤྱོད་མཆོག་བསྟོད་པའི་གཞི་ཞེས་བསྟན་པའི་སྤྱོད་པའི༌[^410]མཆོག་གི་གཞི་དེ་ཉིད་ཀྱི་དབང་དུ་བྱས་ནས་སྨྲས་པ།

[Block 737 [VERSE]]
ཀྱེ་མའོ་རླབས་ཆེན་ཞེས་བྱ་བ་ནས། །
ཁྱོད་ཀྱིས་འགྲོ་བ་མགོན་བཅས་བགྱིས་པ་ལེགས། །

[Block 738]
ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། ཀྱེ་མའོ་རླབས་ཆེན་ཞེས་བྱ་བའི་བསྡུས་པའི་དོན་ནི་འདི་ཡིན་ཏེ། སྦྱོར་བ་ཕུན་སུམ་ཚོགས་པས༌[^411]བསམ་པ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 739]
དང་པོའི་གཉིས་པོ་སྟེ། ཀྱེ་མའོ་རླབས་ཆེན་ཞེས་བྱ་བ་འདིས་ནི་སྦྱིན་པའི་དབང་པོ༌[^412]ལ་ཆགས་པ་མེད་པར་བསྟན་ཏོ། །

[Block 740]
ཨེ་མའོ་སྙིང་རྗེ་ཅན་ཞེས་བྱ་བ་འདིས་ནི་རབ་ཏུ་འཛིན་པར་བྱེད་པའི་སྙིང་རྗེ་དང་ལྡན་པ་སྟེ།
--- END BLOCKS ---
