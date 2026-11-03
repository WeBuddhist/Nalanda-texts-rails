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
[Block 1016 [VERSE]]
འདོད་པ་རྣམས་ཀྱི་རྒྱུར་གྱུར་པ་ཉིད་དོ། །
ཆོས་ཀྱང་འཁོར་གསུམ་གྱི་རྒྱུ་ཡིན་ཏེ།
རྒྱུན་དུ་འཁོར་གསུམ་གྱི་རྒྱུར་གྱུར་པས་སོ། །

[Block 1017]
མཐོང་བའི་ཆོས་ལ་ཡང་རེས་འགའ་དོན་དང་། འདོད་པའི་རྒྱུར་གྱུར་པ་ཡིན་ནོ། །

[Block 1018]
དེའི་ཕྱིར་ན་ཁྱད་པར་གྱི་རྒྱུ་ཞེས་སྨོས་སོ། །

[Block 1019]
དེ་མེད་བྱས་ན་ཞེས་བྱ་བ་ནི་འཁོར་གསུམ་གྱི་ཁྱད་པར་གྱི་རྒྱུ་ནོར་དང་ཆོས་མེད་པར་བྱས་ན་ཉམས་པར་བྱས་པའོ། །ཇི་ལྟར་ཞེ་ན། སྨྲས་པ། ནོར་ཆུད་གསན་པས་ཞེས་བྱ་བ་ཡིན་ཏེ། དེ་ལྟར་ནོར་ཉམས་པར་བྱས་ན་དམྱལ་བར་གནས་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 1020]
དམྱལ་བར་གནས་པར་འགྱུར་བ་དེ་ལྟར་རབ་ཏུ་བསྒྲུབ་པའི༌[^573]ཕྱིར། སྦྱིན་པའི་ཕྱིར་ནི་ཆོས་ཀྱི་རྩར་གྱུར་པའི། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ནོ། །

[Block 1021]
ཆུད་གཟན་སྡིག་བྱས་པས་ཞེས་བྱ་བ་ནི་ཆོས་ཉམས་པར་བྱས་པའོ། །

[Block 1022]
དེའི་ཕྱིར་ཞེས་བྱ་བ་ནི་རྒྱུ་འདིས་སོ། །

[Block 1023]
དམྱལ་བའི་གཤེད་པོ་ཞེས་བྱ་བ་ནི་མཐར་བྱེད་པའི་ཁ་ཡིན་པས་གཤེད་པོའོ། །

[Block 1024]
དེ་ལྟར་ཚིགས་སུ་བཅད་པ་དེ་དག་གིས་ཡང་དག་པར་བསྟན་པར་བྱས་ནས། ཡང་དག་པར་ལེན་དུ་གཞུག་པའི་ཕྱིར་རོ།[^574] །དེ་བས་བློ་ནི་སྦྱིན་ལས་བཟློག་ན་ལེགས། །ཞེས་བྱ་བའི་ཚིགས་སུ་བཅད་པ་བརྩམས་པ་ཡིན་ནོ། །

[Block 1025]
འོན་ཀྱང་འཕྲལ་དུ་ལྟུང་བར་ཁྱོད་མི་འགྱུར། །ཞེས་བྱ་བས་ནི་དུས་ཕྱི་ནས་ཀྱང་ལྟུང་བར་མི་འགྱུར་བ་སྟེ། ཆོས་ཀྱི་རྩ་བ་ནོར་ཡིན་པས་སོ། །

[Block 1026]
དེ་དང་འགལ་བས་ན་དང་པོའི་ཚིགས་བཅད་ཕྱེད་ཀྱིས་ནི་སྦྱིན་པ་ལས་ལྡོག་པའི་ཡོན་ཏན་བསྟན་ནས། སྦྱིན་པ་ལས་མི་ལྡོག་པའི་སྐྱོན་བསྟན་པའི་དབང་དུ་བྱས་ནས་སྨྲས་པ། སྙིང་རྗེ༌[^575]ངུ་ཞིང་ཞེས་བྱ་བ་ལ་སོགས་པ་འདིའི་དོན་ཡིན་ནོ། །

[Block 1027]
སྦྱིན་པ་ལས་ལྡོག་ན་ནི་འཕྲལ་དུ་དམྱལ་བར་མི་ལྟུང་བ་ཉིད་ཀྱི་ཡོན་ཏན་ཡོད་དེ། དེའི་གཉེན་པོར་གྱུར་པས་སོ། །

[Block 1028]
ད༌[^576]ནི་ལན་པ༌[^577]པོའི་ཕན་ཡོན་བསྟན་པའི་ཕྱིར་སྦྱིན་པ་ཚུལ་མིན་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་ཡིན་ཏེ། ཚུལ་བཞིན་བྱེད་པ་དང་ལེན་པ་པོ༌[^578]ནི་མཐོ་རིས་སུ་འགྲོ་བ་ཡིན་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། སྦྱིན་པ་ཚུལ་མིན་མི་བྱེད་པར་གྱུར་པས་སོ། །

[Block 1029]
ཆོས་ཀྱི་རྒྱུ་ནི་ནོར་རྣམ་པར་སྤེལ་བ་ན་ཆོས་རྣམ་པར་འཕེལ་བར་འགྱུར་རོ། །

[Block 1030]
འདིས་སྒྲིབ་པར་བྱེད་པ་ཡིན་པས་སྒྲིབ་པའོ། །

[Block 1031]
མཐོ་རིས་ཀྱི་ལམ་སྒྲིབ་པ་སྟེ། [^579]དེ་བས་ན་མཐོ་རིས་ཀྱི་ལམ་སྒྲིབ་པའོ།[^580] །ལྡོག་ལ་ཞེས་བྱ་བ་ནི་སྦྱིན་པ་ལས་ལྡོག་པའོ། །

[Block 1032]
འདི་ནི་ཞེས་བྱ་བ་ནི་བདུད་དོ། །

[Block 1033]
བདག་ཉིད་ཀྱི་སྙིང་སྟོབས་ནི་བདག་གི་སྙིང་སྟོབས་སོ། །

[Block 1034]
བདག་གི་སྙིང་སྟོབས་ཉིད་ཀྱི་ཁར་བོར་བ་ཡིན་པས་བདག་གི་སྙིང་སྟོབས་ཀྱི་ཁར་བོར་བའོ། །

[Block 1035]
བརྟན་པ༌[^581]ནི་བདག་གི་སྙིང་སྟོབས་ཀྱི་ཁར་བོར་བ་དེ་བརྟན་པར༌[^582]བྱས་པའོ། །

[Block 1036]
ཚིག་འཇམ་པོ་རྒྱུན་མི་འཆད་པ་གང་ཡིན་པ་དེ་ནི་ཚིག་འཇམ་པ༌[^583]རྒྱུན་མི་འཆད་པའོ། །

[Block 1037]
འདིས༌[^584]གནས་ནི༌[^585]བདག་ཅག་ལ་ཕན་པ་ཡིན་པའི་ཕྱིར་བདག་ཅག་འདྲ་ལ་ཕན་པའོ། །

[Block 1038]
བདག་ཅག་འདྲ་ལ་དགོངས་པ་ནི་བདག་ཅག་འདྲ་ལ་ཕན་པར་དགོངས་པ་སྟེ། དམྱལ་བར་ལྟུང་བ་ལས་བཟློག་པའོ། །

[Block 1039]
དེ་ལ་མཐུན་པ་ནི་ལེ་ལོ་མེད་པའོ། །

[Block 1040]
ཡང་ན་དགེ་བ་སྟེ་བདག་ཅག་འདྲ་ལ་ཕན་པར་དགོངས་པའོ། །

[Block 1041]
འཕགས་པའི་ལམ་ནི་ལམ་གཞན་ལ་འཇུག༌[^586]པའི་ལམ་མོ། །

[Block 1042]
དེ་ལྟར་ཞེས་བྱ་བ་ནི་ཁྱད་པར་དུ་སྟེ། ལས་ཀྱི་འབྲས་བུ་མངོན་སུམ་དུ་མཐོང་བའི་ལྷ་རྣམས་ཀྱིས་སོ། །

[Block 1043]
གཞན་ལ་ཕན་འདོགས་མཁས་པའི་སྤྱོད་པ་ཡིན། །ཞེས་བྱ་བ་ལ། ཕན་འདོགས་པའི་མཁས་པ་ནི་སྦྱིན་པ་ལས་ལྡོག་པའི་རྒྱུ་དམྱལ་བ་མངོན་སུམ་དུ་བསྟན་པས་སོ། །

[Block 1044]
ཉེས་པ་བྱུང་བ་ཞེས་བྱ་བ་ནི་རླུང་དང་མཁྲིས་པ་དང་བད་ཀན་བྱུང་བའོ། །

[Block 1045]
འདིས༌[^587]ནི་རང་གི་འཚོ་བ་བསྟན་པ་ཡིན་ནོ། །

[Block 1046]
ཉེས་པ་བྱུང་བའི་འོག་ཏུ་ཡང་ཞེས་བྱ་བ་ནི་ཉེས་པ་བྱུང་མ་ཐག་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 1047]
ཞི་བའི་ལམ་དེར་ཞེས་བྱ་བ་ནི་ཉེས་པ་མི་འབྱུང་བའི་ལམ་དུ་སྟེ། ཉེས་པ་མི་སྐྱེ་བ་ནི་ཐ་མལ་པར་གནས་པའོ། །

[Block 1048]
ཉེས་པ་བྱུང་བའི་འོག་ཏུ་ཡང་ཉེས་པ་དེ་ཞི་བའི་ལམ་དུ་འགྲོ་བར་བྱ་བ་སྟེ། ནད་བྱུང་བ་དེ་མ་ཐག་པར་ཉེས་པ་དེ་དག་ཉིད་ལ་ཞི་བའི་ལམ་དུ་འགྲོ་བས་སོ། །

[Block 1049]
ཞི་བའི་ལམ་དུ་འགྲོ་བས་ཀྱང་མ་རུང་བ་ནི་ཚབས་ཆེར་གྱུར་ལ་ཞེས་བྱ་བ་ཡིན་ཏེ།

[Block 1050 [VERSE]]
གསོར་མི་རུང་བར་གྱུར་པའོ། །
ཆོ་ག་སྤྱད་པ་ནོངས་པ་ཡིས། །

[Block 1051]
ཞེས་བྱ་བ་ནི་མཐུན་པའི་ཟས་ཀྱིས་མ་བཟློག་པ༌[^588]དང་། མི་མཐུན་པའི་ཟས་བསྟན་པས༌[^589]ནི་སྨན་མི་ཐོགས་པ༌[^590]ཞེས་བྱ་བ་ཡིན་ཏེ། ངལ་བའི་འབྲས་བུ་ཉི་ཚེར་ཟད་དེ། དེ་ལྟར་ནད་ཉེ་བར་ཞི་བར་མི་འགྱུར་རོ། །

[Block 1052]
དེ་ལྟར་དཔེ་བསྟན་ནས་དཔེ་བསྒྲུབ་པར་བྱ་བ་དེ་བསྟན་པའི་ཕྱིར། སྦྱིན་ལ་ཞུགས་པ་བདག་གི༌[^591]སྡུག་བསྔལ་འདི། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ཏེ། །དཔྱད་ཀྱིས་སློན་པར༌[^592]རབ་ཏུ་མི་འགྱུར་དོགས། །ཞེས་བྱ་བ་ནི་ཕན་པར་བསྟན་པའི་དཔྱད་ཀྱིས་གསོ་བའི་ཡུལ་དུ་མི་འགྱུར་བའོ། །

[Block 1053]
དེ་བསྒྲུབ་པའི༌[^593]ཕྱིར་ཁྱོད་ཀྱིས༌[^594]ཕན་པ་བསྟན་པའང་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཕྱེད་བསྟན་པ་ཡིན་ཏེ། ཕན་པ་བསྟན་པ་ཡང་མི་ཉན་པར་ཞེས་བྱ་བ་ནི་ཕན་འདོགས་པའི་གདམས་ངག༌[^595]མི་སྒྲུབ་པའོ། །

[Block 1054]
སེམས་ཞེས་བྱ་བ་ནི་སྦྱིན་པར་འདོད་པའི་ཡིད་དོ། །

[Block 1055]
ནད་དང་འདྲ་བ་ནི་དེའི་སྦྱིན་པའི་སེམས་ཏེ། སེམས་ལ་གནས་པར་གྱུར་པས་དེའི་སྒྲར་བརྗོད་དེ།
--- END BLOCKS ---
