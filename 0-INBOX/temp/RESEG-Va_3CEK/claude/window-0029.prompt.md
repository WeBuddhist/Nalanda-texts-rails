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
[Block 1016]
ངན་འགྲོ་རྣམ་པ་གསུམ་དང་། བདེ་འགྲོའི་ཕྱོགས་བྱང་གི་སྒྲ་མི་སྙན་པ་རྣམས་དང་། འདུ་ཤེས་མེད་པའི་སེམས་ཅན༌[^739]རྣམ་པར་སྨིན་པའི་སྒྲིབ་པ་ཡིན་ནོ། །

[Block 1017]
འདི་དག་གང་ལ་སྒྲིབ་ཅེ་ན། འཕགས་པའི་ལམ་དང་། འཕགས་པའི་ལམ་ལ་སྦྱོར་བར་བྱེད་པའི་དགེ་བའི་རྩ་བ་རྣམས་ལ་སྒྲིབ་བོ། །

[Block 1018]
ངན་སོང་ལ་སོགས་པར་ངེས་པར་འགྱུར་བ་དང་། སྒོ་ང་ལས་སྐྱེ་བར་འགྱུར་བ་དང་། དྲོད་གཤེར་ལས་སྐྱེ་བར་འགྱུར་བ་དང་། བུད་མེད་ཉིད་དུ་འགྱུར་བ་དང་། སྲིད་པ་བརྒྱད་པར་ངེས་པར་འགྱུར་བའི་ལས་གཞན་དང་གཞན་དག་ཀྱང༌[^740]བརྗོད་པར་བྱ་བར་འགྱུར་རོ་ཞེ་ན། གང་དག་གཞི་དང་། འབྲས་བུ་དང་། འགྲོ་བ་དང་། སྐྱེ་བ་དང་། གང་ཟག་དང་། རྒྱུ་ལྔས་བསྟན་པར་སླ་ཞིང་གདགས་པར་བྱ་བ་དེ་དག་ཁོ་ན་བཤད་ཀྱིས༌[^741]གཞན་དག་ནི་མ་ཡིན་ནོ། །

[Block 1019]
དེ་དག་ལས་ཉོན་མོངས་པའི་སྒྲིབ་པ་ནི་ཐམས་ཅད་ཀྱི་ཐ་ཤལ་ཡིན་ནོ། །

[Block 1020]
དེའི་འོག་ཏུ་ནི་ལས་ཀྱི་སྒྲིབ་པ་སྟེ། དེ་གཉིས་ཀྱིས་ནི་ཚེ་ཕྱི་མ་ལ་ཡང་གསོར་མི་རུང་བར་འགྱུར་རོ། །

[Block 1021]
བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ་ཕྱི་མ་ཕྱི་མ་འདྲེན་པའི་ཕྱིར་རོ་ཞེས་ཟེར་རོ། །

[Block 1022]
མཚམས་མེད་པ་རྣམས༌[^742]ཞེས་བྱ་བའི་དོན་ཅི་ཞེ་ན། ཚེ་རབས་གཞན་གྱི་འབྲས་བུ་ཅན་གྱི་ལས་དག་གི༌[^743]རྣམ་པར་སྨིན་པར་འགྱུར་བའི་བར་དུ་གཅོད་པར་མི་ནུས་པས་མཚམས་མེད་པ་རྣམས་ཏེ། ཟིལ་གྱིས་མི་གནོན་ཞེས༌[^744]བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1023]
ཡང་ན་དེ་བྱེད་པའི་གང་ཟག་འདི་ནས་ཤི་འཕོས་པ་དང་དམྱལ་བར་སྐྱེ་བར་འགྱུར་བ་ལ་བར་ཆད་མེད་པས་དེ་ནི་བར་ཆད་མེད་པའོ། །

[Block 1024]
དེའི་དངོས་པོ་ནི་བར་ཆད་མེད་པ༌[^745]ཉིད་དེ། ཆོས་གང་དང་ལྡན་པའི་ཕྱིར་དེ་བར་ཆད་མེད་པ་ཡིན་ཏེ། དགེ་སྦྱོང་གི་ཚུལ་བཞིན་ནོ། །

[Block 1025]
ཡང་སྒྲིབ་པ་འདི་དག་ལས་གང་ཞིག་ཁམས་གང་ན་ཡོད་པར་རིག་པར་བྱ་ཞེ་ན། རེ་ཞིག་གཅིག་ཏུ། མཚམས་མེད་གླིང་གསུམ་དག་ན་ཡོད། །བྱང་གི་སྒྲ་མི་སྙན་དང་། འགྲོ་བ་གཞན་དག་ན་ཡང་མེད་ན༌[^746]ཁམས་གཞན་ན་ལྟ་སྨོས་ཀྱང་ཅི་དགོས། དེ་དག་ན་ཡང་སྐྱེས་པ་དང་བུད་མེད་རྣམས་ཁོ་ན་ལ་ཡོད་ཀྱི། ཟ་མ༌[^747]ལ་སོགས་པ༌[^748]མི་འདོད་དོ། །ཅིའི་ཕྱིར་ཞེ་ན། སྡོམ་པ་མེད་པའི་གཏན་ཚིགས་གང་ཡིན་པ་དེ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1026]
གཞན་ཡང་། ཕན་དང་ངོ་ཚ་ཆུང་བའི་ཕྱིར། །ཕ་མ་དང་དེ་དག་དང་གོ་རིམས་བཞིན་ཏེ། ཕ་མ་ནི་དེ་དག་གི་ལུས་མ་ཚང་བའི་བདག་པོར་འགྱུར་བའི༌[^749]ཕྱིར་དང་། བྱམས་པ་ཆུང་བའི་ཕྱིར་ཕན་པ་ཆུང་བ་ཡིན་ནོ། །

[Block 1027]
དེ་དག་ཀྱང་ཕ་མ་ལ་གང་དག༌[^750]མེད་པར་བྱས་པས་མཚམས་མེད་པའི་ཁ་ན་མ་ཐོ་བས་རེག་པར་འགྱུར་བ་ངོ་ཚ་ཤེས་པ་དང་ཁྲེལ་ཡོད་པའི་ཤས་ཆེན་པོ་ཉེ་བར་མི་གནས་ཏེ། དེ་ཉིད་ཀྱི་ཕྱིར་ཡི་དགས་དང་། དུད་འགྲོ་རྣམས་ལ་ཡང་མི་འདོད་དོ་ཞེས་གྲག་གོ། །

[Block 1028]
བཙུན་པ་ན་རེ་བློ་གསལ་བ་རྣམས་ལ་འགྱུར་ཏེ་རྟ་ཅང་ཤེས་བཞིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 1029]
མིའི་ཡང་ཕ་མ་མི་མ་ཡིན་པ་བསད་ན་མཚམས་མེད་པར་མི་འགྱུར་རོ། །

[Block 1030]
ལས་ཀྱི་སྒྲིབ་པ་བཤད་ཟིན་ཏོ། །

[Block 1031]
ལྷག་མ་འགྲོ་བ་ལྔ་དག་ན། །ལྷག་མ་གང་དག་ཅི༌[^751]ཡིན་ཞེ་ན། ཉོན་མོངས་པ་དང་རྣམ་པར་སྨིན་པའི་སྒྲིབ་པ་སྟེ། མི་དག་གི་ནང་ན་ནི་སྒྲ་མི་སྙན་པ༌[^752]རྣམ་པར་སྨིན་པའི་སྒྲིབ་པ་ཡིན་ནོ། །

[Block 1032]
ལྷ་དག་གི་ནང་ན་ནི་འདུ་ཤེས་མེད་པའི་སེམས་ཅན་རྣམས་སོ། །

[Block 1033 [HEADING]]
### མཚམས་མེད་པ་རྣམས་ཀྱི་རང་བཞིན། ^1-60-0

[Block 1034]
མཚམས་མེད་པ་རྣམས་ཀྱི་རང་བཞིན་ཅི་ཞེ་ན།

[Block 1035 [VERSE]]
བཞི་ནི་ལུས་ཀྱི་ལས་ཡིན་ལ། །
གཅིག་ནི་ངག་གི་ལས་ཡིན་ཏེ། །
གསུམ་ནི་སྲོག་གཅོད་པ་ཡིན་ནོ། །
གཅིག་ནི་བརྫུན་དུ་སྨྲ་བ་ཡིན་ནོ། །

[Block 1036]
གཅིག་ནི་སྲོག་གཅོད་པའི་སྦྱོར་བ་སྟེ། དེ་བཞིན་གཤེགས་པ་རྣམས་ནི་ཉེ་བར་མི་བརྫི་བའི་ཆོས་ཅན་ཡིན་ནོ། །

[Block 1037 [HEADING]]
### དགེ་འདུན་གྱི་དབྱེན། ^1-61-0

[Block 1038]
རྒྱུ་ལ་འབྲས་བུ་བཏགས་པའམ། འདིས་འབྱེད་པར་བྱེད་པས་ན་དགེ་འདུན་གྱི་དབྱེན་ལ་མཚམས་མེད་པ་ཞེས་བཤད་ཀྱི།

[Block 1039 [VERSE]]
དགེ་འདུན་དབྱེན་ནི་མི་འཕྲོད་པའི། །
རང་བཞིན་ལྡན་པས༌[^753]མ་ཡིན་ཆོས། །
ཉོན་མོངས་ཅན་མིན་ལུང་བསྟན་མིན། །

[Block 1040]
དགེ་འདུན་གྱི་དབྱེན་ནི་མི་འཕྲོད་པ་ཞེས་བྱ་བ་སེམས་དང་ལྡན་པ་མ་ཡིན་པའི་འདུ་བྱེད་དེ། མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་ཡིན་ན་དེ་ཇི་ལྟར་མཚམས་མེད་པར་འགྱུར། དེ་དང་བྱེད་པ༌[^754]པོར་ཡང་མི་ལྡན་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 1041]
འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན།

[Block 1042 [VERSE]]
དེ་དང་དགེ་འདུན་ཡང་དག་ལྡན། །
གང་བྱེ་བ་དེ་དབྱེན་དང་ལྡན་གྱི།
འབྱེད་པ་པོ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 1043]
འོ་ན་འབྱེད་པ་པོ་ཅི་དང་ལྡན་ཞེ་ན།

[Block 1044 [VERSE]]
དེ་ཡི་ཁ་ན་མ་ཐོ་བརྫུན། །
དེ་དང་བྱེད་པོ༌[^755]ཡང་དག་ལྡན། །

[Block 1045]
འབྱེད་པ་པོ་ནི་དགེ་འདུན་གྱི་དབྱེན་གྱི་ཁ་ན་མ་ཐོ་བ་དང་ལྡན་ཏེ། དེ་ནི་བརྫུན་ཡིན་ནོ། །

[Block 1046]
དེ་ཡང་དགེ་འདུན་གྱི་དབྱེན་དང་ལྷན་ཅིག་སྐྱེས་པའི་ངག་གི་རྣམ་པར་རིག་བྱེད་དང་། རྣམ་པར་རིག་བྱེད༌[^756]མ་ཡིན་པ་དག་ཡིན་ནོ། །

[Block 1047]
ཁ་ན་མ་ཐོ་བ་དེ་དང་ལྡན་པའི་བྱེད་པ༌[^757]པོ་དེ་ནི། བསྐལ་པར་མནར་མེད་པར་སྨིན་འགྱུར། །བར་གྱི་བསྐལ་པར་མནར་མེད་པའི་སེམས་ཅན་དམྱལ་བ་ཆེན་པོར་སྨིན་པར་འགྱུར་རོ། །

[Block 1048]
གཞན་གྱིས་ནི་མནར་མེད་པར་མ་ངེས་སོ། །

[Block 1049]
ཡང་གང་ཞིག་གིས་མཚམས་མེད་པ་མང་པོ་བྱས་པ་ཡིན་ལ། དེ་དག་བར་ཆད་མེད་པ་ཁོ་ན༌[^758]སྨིན་པར་འགྱུར་ན་དེ་ལ་དེ་དག་གིས་ཅི་ཞིག་ཏུ་འགྱུར་ཞེ་ན། ལྷག་པས་གནོད་པ་ལྷག་པར་འགྱུར། །དེ་མཚམས་མེད་པ་མང་པོས་མནར་མེད་པ་དེར་གང་གིས་ན་གཉིས་དང་གསུམ་དང་བཞི་དང་ལྔར་འགྱུར༌[^759]གྱི་ཚོར་བ་མྱོང་བར་འགྱུར་བའི་ལུས་ཆེན་པོ་དང་། ཤིན་ཏུ་གཞོན་ཤ་ཅན་གྱི་ལུས་འཐོབ་ཅིང་། གནོད་པ་ཡང་རབ་ཏུ་མང་བ་དང་ཤིན་ཏུ་མི་བཟད་པར་འགྱུར་རོ། །

[Block 1050]
དགེ་འདུན་འབྱེད་པར་བྱེད་པ་དེ་སུ་ཞིག་ཡིན་ཞེ་ན། དགེ་སློང་དཀའ་སྤྱོད༌[^760]ཚུལ་ལྡན་པས། །འབྱེད་དོ། །

[Block 1051]
དགེ་སློང་གིས་འབྱེད་ཀྱི་ཁྱིམ་པ་ཡང་མ་ཡིན་ལ། དགེ་སློང་མ་ལ་སོགས་པ་ཡང་མ་ཡིན་ནོ། །

[Block 1052]
དེ་ཡང་ལྟ་བ་སྤྱོད་པ་ཁོ་ནས་འབྱེད་ཀྱི་སྲེད་པ་སྤྱོད་པས་ནི་མ་ཡིན་ནོ། །

[Block 1053]
ཚུལ་དང་ལྡན་པས་འབྱེད་ཀྱི་ཚུལ་ཉམས་པས་ནི་མ་ཡིན་ཏེ། དེའི་ཚིག་མི་བཙན་པའི་ཕྱིར་རོ། །གང་དུ་འབྱེད་ཅེ་ན།

[Block 1054]
གང་ན་བཅོམ་ལྡན་འདས་མངོན་སུམ་དུ་བཞུགས་པ་དེ་ལས།

[Block 1055]
གཞན་དུའོ། །
--- END BLOCKS ---
