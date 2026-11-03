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
[Block 5671]
ཕོངས་ཤིང་ཉམ་ཐག་ཅེས་བྱ་བ་ནི་སྡུག་བསྔལ་བ་ཉིད་དོ། །

[Block 5672]
[^3617]འཇིགས་ལ༌[^3618]མྱ་ངན་གདུངས་ཞེས་བྱ་བ་ནི་རྗེས་སུ་འབྲང་བ༌[^3619]མེད་པའོ། །

[Block 5673]
སྤྱོད་བཟང་འདི་འདྲ་གང་དུ་བསླབས་ཞིག་གུ། །ཞེས་བྱ་བ་ནི་མཁན་པོ་གང་ཡིན་པའི་དོན་ཏོ། །

[Block 5674]
བླ་མ་གང་ལ་གནས་ནས་བསྙེན་བཀུར་བྱས། །ཞེས་བྱ་བ་ནི་དཔོན་གང་ལ་བསྙེན་བཀུར༌[^3620]བྱས་པའོ། །

[Block 5675]
དེ་ནི་འདི་ལས་མངོན་ཞེས་བྱ་བ་ནི་གཟུགས་དང་རྗེས་སུ་མཐུན་པ་ཉིད་ཀྱིས་ཡོན་ཏན་མངོན་པའི་དོན་ཏོ། །

[Block 5676]
གཟུགས་དང་རྗེས་སུ་མཐུན་པའི་ཡོན་ཏན་གང་ཡིན་པ་སྨྲས་པ། དེ་འདིར་དེ་ཉིད་མངོན་སུམ་དུ་མཐོང་བ་ཡིན་ཏེ། ཡོན་ཏན་དང་ལྡན་པ་དེ་ནི་གང་དུ་བསླབས་ཞེས་བྱ་བ་དང་སྦྱར་རོ། །

[Block 5677]
རང་བཞིན་ཡང་ཡིན་ལ་འཕགས་པ་ཡང་ཡིན་པས་རང་བཞིན་འཕགས་པའོ། །

[Block 5678]
དེའི་ཕུན་སུམ་ཚོགས་པ་དེ་ནི་རང་བཞིན་དུ་འཕགས་པ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 5679]
ཡང་ན་རང་བཞིན་འཕགས་པ་ཉིད་ཕུན་སུམ་ཚོགས་པ་ཡིན་པས་རང་བཞིན་འཕགས་པ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 5680]
རང་བཞིན་ཕུན་སུམ་ཚོགས་པ་དེས་དོན་བཞིན་བསྒྲུབ་པའི་དོན་དང༌[^3621]མཐུན་པ་ཡིན་པས་དོན་བཞིན་ནོ། །

[Block 5681]
དེ་བསྒྲུབས་པ་ཞེས་བྱ་བ་ནི་བཟང་པོ་ཞེས་བྱ་བ་གླང་པོ་ཆེ་བདག་ཉིད་གང་ཡིན་པ་དེ་ནི་དོན་བཞིན་བསྒྲུབས་ཞེས་བྱ་བ་འདིས་ནི༌[^3622]བསྟན་ཏོ། །

[Block 5682]
གང་གི་རང་བཞིན་ཕུན་སུམ་ཚོགས་པ་ཡིན་པ་དང་། ཇི་ལྟར་རང་བཞིན་ཕུན་སུམ་ཚོགས་པ་ཡིན་པར་ཤེས་པར་བྱ་ཞེ་ན། དེ་ཉིད་ཀྱི་ཕྱིར་སྨྲས་པ། འདི་ལྟར་ཤི་བར་འགྱུར༌[^3623]ན་ནི་དགོན་པ་བཞིན་དུ་ཤེས་པའོ། །

[Block 5683]
སྤྱོད་བཟང་འདི་འདྲ་གང་དུ་བསླབས་ཞིག་གུ། །ཞེས་བྱ་བ་འདི༌[^3624]བསྟན་པ་དེ་ལ་དེའི་སྤྱོད་པ་བཟང་པོ་བསྒྲུབ་པའི་ཕྱིར། ཀྱེ་མའོ་རང་བཞིན་འཕགས་པ་ཕུན་སུམ་ཚོགས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་པ་ཡིན་ནོ། །

[Block 5684]
གཉེན་དང་བཤེས་ནི་གཉེན་བཤེས་སོ། །

[Block 5685]
དེ་ཉིད་བྱམས་པ་ཡིན་པས་གཉེན་བཤེས་བྱམས་པའོ། །

[Block 5686]
དེ་དག་ལས་ཁྱད་པར་དུ་གཉེན་བཤེས༌[^3625]གང་ཡིན་པ་དེ་ནི་གཉེན་བཤེས་བྱམས་པ་བས་ཀྱང་ལྷག་པ་སྟེ། འདིས་ནི་བསམ་པ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 5687]
ཕན་འདོགས་པ་བདག་ཅག་ལ་ཕན་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་སྔར་བསྟན་པའི་དབུགས་ཕྱུང་ཞེས་བྱ་བ་དེ་ཉིད་བསྟན་ཏོ། །

[Block 5688]
རང་གི་སྲོག་གི་གསལ༌[^3626]ཏེ་རབ་ཏུ་ལེགས་པར༌[^3627]བྱེད་བྱེད་པ་ཞེས་བྱ་བ་ནི་གང་དེ་བདག་ཉིད་ཡོངས་སུ་བཏང་བ་དེ་ཉིད་བསྟན་ཏོ། །

[Block 5689]
དེ་ལྟར་མཆོད་པར་མི་འགྱུར་རོ་ཞེས་བྱ་བ་ནི་གང༌[^3628]སྔར་བསྟན་པ་འདི་ལ་མཆོད་པར་བྱ་སྟེ་ཞེས་བྱ་བ་དེ་ཉིད་ཡིན་ནོ། །

[Block 5690]
བཀུར་སྟི་བྱས་པར༌[^3629]མི་འགྱུར་གྱི། །ཞེས་བྱ་བ་ནི་གང་སྔར་བསྟན་པའི་མེར་སྲེག་པའི༌[^3630]ཞལ་ཏ་བྱོས་ཞེས་བྱ་བ་དེ་ཉིད་བསྟན་པ་ཡིན་ནོ། །

[Block 5691]
འདི་ཡི་བསམ་པ་རྫོགས་པར་བྱ། །[^3631]ཞེས་བྱ་བ་ནི་གང་གི་བསམ་པ་ཡིན་ཞེ་ན། བདག་ཡོངས་སུ་བཏང་བའི་བསམ་པ་རྫོགས་པར་བྱའོ།[^3632] །མཆོད་པར༌[^3633]བྱས་པར་འགྱུར་རོ༌[^3634]ཞེས་བྱ་བ་ནི་མཆོད་པ་བསྒྲུབས་པར་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5692]
འདི༌[^3635]བསམ་པ་རྫོགས་པར་བྱའོ་ཞེས་བསྟན་པ་ལ། བསམ་པ་གང་ཡིན་པ་དེ་བསྟན་པའི་ཕྱིར། བདག་ཅག་རྣམས་ནི་བསྒྲལ་བའི་ཕྱིར། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 5693]
བདག་ཅག་རྣམས་ཀྱི་བསྒྲལ་བ་ནི་བདག་ཅག་རྣམས་བསྒྲལ་བའོ། །

[Block 5694]
དེའི་ཆེད་དུ་གཏོང་བའི་ཚུལ་གང་ལ་ཡོད་པ་དེ༌[^3636]ནི་བདག་ཅག་བསྒྲལ་བའི་ཕྱིར་རོ། །

[Block 5695]
རབ་ཏུ་ཕོངས༌[^3637]པའི་ལུས་བཏང་བ། །ཞེས་བྱ་བ་ཡིན་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན།

[Block 5696 [VERSE]]
རབ་ཏུ་གཅེས་པའི་མགྲོན་བྱ་བའི་ཕྱིར་རོ། །
དེ་བས་དེ་ཡི་བསམ་པ་རྫོགས་པར་བྱ། །

[Block 5697]
ཞེས་བྱ༌[^3638]བ་ནི་བདག་བསྒྲལ་བའི་བསམ་པ་སྟེ། དགོན་པ་ལས་བསྒྲལ་བའི་ཕྱིར་རོ། །

[Block 5698]
བདག་ཅག་རྣམས་ཀྱིས༌[^3639]བྱ་བའི་རིགས་སོ། །

[Block 5699]
[^3640]ཞེས་བྱ་བ་ནི་རིགས་པ་ཡིན་པའི་ཕྱིར། དེ་བས་ན་བསམ་པ་ཉིད་བདག་ཅག་རྣམས་ཀྱིས་བྱ་བའི༌[^3641]རིགས་ཏེ་དགོན་པ་འདི་ལས་བརྒལ་བར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5700]
གཞན་དུ་བྱས་ནས༌[^3642]ཞེས་བྱ་བ་ནི་གང་སྔར་བསྟན་པའི་མཆོད་པ་བྱས་ཏེ། མེར་སྲེག་པའི་ཞལ་ཏ་བྱས་ལ་ཞེས་བྱ་བ་དེ་ཡིན་ཏེ། འདི་ནས་བསྒྲལ་བའི་ཕྱིར་ལུས་བཏང་བ་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན། མ་འདྲིས་པའི་ཕྱིར་རོ། །

[Block 5701]
འདྲིས་པ་དག་ལ་ནི་འདྲིས་པ་ལ་ལྟོས་པས་ཕན་འདོགས་པར་བྱེད་པ་ཡིན་ཏེ། དེ་བས་ན་འདྲིས་པའང་མེད་དོ། །

[Block 5702]
བདག་ཅག་རྣམས་བསྒྲལ་བ་འདི་ལ་ཡོན་ཏན་ཅི་ཡོད་ཅེ་ན། སྨྲས་པ། དེས་ན་ལུས་ཤིན་ཏུ་གཅེས་པ་ཡིན་ཡང་བཏང་བ་ནི་རབ་ཏུ་གཅེས་པའི་མགྲོན་ཡིན་པའི་ཕྱིར་ཏེ། ལུས་པས་ཀྱང་རབ་ཏུ་གཅེས་པ་ནི་གང་གི་ཕྱིར༌[^3643]མགྲོན་ཡིན་པའི་ཕྱིར་ཏེ༌[^3644]ལུས་བཏང་བའོ། །

[Block 5703]
བསམ་པ་ནི་བདག་ཅག་བསྒྲལ་བའི་བསམ་པ་སྟེ། རབ་ཏུ་གཅེས་པའི་མགྲོན་ཡིན་པའི་ཕྱིར་ལུས་བཏང་བ་ཡིན་ནོ། །

[Block 5704]
དེ་བས་ན་གཞན་དུ་ན་ཞེས་བྱ་བ་སྟེ། དེའི་བསམ་པ་མ་བྱས་པར་གྱུར་ན་ནི་བྱས་པ་དོན་མེད་པར་འགྱུར་རོ། །

[Block 5705]
རབ་ཏུ་གཅེས་པའི་མགྲོན་ལ་རབ་ཏུ་ཕངས་པའི༌[^3645]ལུས་བཏང་བ་བྱས་པའི་འབད་པའོ། །

[Block 5706]
དེ་ལྟར་རེ་ཞིག་བྱང་ཆུབ་སེམས་དཔའ་ལས་རྗེས་སུ་མ་བླངས་ན་རིགས་པ་མ་ཡིན་པ་ཉིད་དུ་བསྟན་ནས། ད་ནི་བདག་ཅག་ཉིད་ཀྱིས་མ་བླངས་པ་མི་མཐུན་པ་ཉིད་དུ་བསྟན་པའི་ཕྱིར།

[Block 5707 [VERSE]]
འདི་ཡིས་བྱས་ཏེ་ཅི་བདོག་པ། །
ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་ཏེ།
གཞན་དུ་བྱས་ན་དོན་མེད་འགྱུར། །

[Block 5708]
ཞེས་བྱ་བ་འདི༌[^3646]དོན་མེད་པ་ཉིད་དུ་བསྒྲུབ༌[^3647]པའི་ཕྱིར། [^3648]བྱམས་པ་ཞེས་བྱ་བ་ནི་བསམ་པ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 5709]
ཅི་བདོག་པ་ཞེས་བྱ་བ་ནི་སྦྱོར་བ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 5710]
བདོག་པ་ཐམས་ཅད་ཅེས་བྱ་བ་ནི་སྦྱིན་པར་བྱ་བའི་དངོས་པོ་ཕུན་སུམ་ཚོགས་པའོ། །
--- END BLOCKS ---
