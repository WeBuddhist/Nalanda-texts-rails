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
[Block 806]
འགོག་པའོ། །

[Block 807]
གང་གིས་མ་འོངས་པའི་སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་འགོག་པ་དེ་ནི་འདུ་ཤེས་མེད་པ་པ་ཞེས་བྱ་བའི་རྫས་སོ། །

[Block 808]
དེ་ཡང་གཅིག་ཏུ་རྣམ༌[^302]སྨིན། འདུ་ཤེས་མེད་པའི་སྙོམས་པར་འཇུག་པའིའོ། །

[Block 809]
གང་དག་ན་འདུ་ཤེས་མེད་པའི་སེམས་ཅན་རྣམས་འཁོད་པའི་སེམས་ཅན་དེ་དག་གང་ཞེ་ན། དེ་འབྲས་ཆེ། ལྷ་དེ་དག་ནི་འབྲས་བུ་ཆེ་བ་ཞེས་བྱ་བ་ཡིན་ཏེ། དེ་དག་གི་ཕྱོགས་གཅིག་ནི་འདུ་ཤེས་མེད་པ་པ་ཡིན་ཏེ། བསམ་གཏན་ཁྱད་པར་ཅན་བཞིན་ནོ། །

[Block 810]
འདུ་ཤེས་མེད་པ་པ་བཤད་ཟིན་ཏོ། །

[Block 811 [HEADING]]
##### སྙོམས་པར་འཇུག་པ། ^2-2-3-4-0

[Block 812]
ཇི་ལྟར་སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་འགོག་པ་ལ་འདུ་ཤེས་མེད་པར་བཤད་པ། དེ་བཞིན་འདུ་ཤེས་མེད་སྙོམས་འཇུག །སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་ཀྱི་འགོག་པ་ཞེས་བྱ་བ་ཙམ་སྟེ། དེ་བཞིན་ཞེས་བྱ་བའི་སྒྲས་འདྲེན་ཏོ། །

[Block 813]
སྙོམས་པར་འཇུག་པ་དེ་ནི། བསམ་གཏན་ཐ་མར། འདི་བསམ་གཏན་བཞི་པ་ལ་སྙོམས་པར་ཞུགས་པ་ཡིན་ནོ། །

[Block 814]
དེ་ལ་ཡང་སྙོམས་པར་འཇུག་པ་ནི། འབྱུང་འདོད་པས། འདི་ལ༌[^303]ངེས་པར་འབྱུང་འདོད་ཅིང་སྙོམས་པར་འཇུག་གོ། །

[Block 815]
འདུ་ཤེས་མེད་པ་པ་ནི་རྣམ་པར་སྨིན་པ་ཡིན་པའི་ཕྱིར་ལུང་མ་བསྟན་པ་ཞེས་བྱ་བར་གྲུབ་བོ། །

[Block 816]
འདི་ནི་དགེ་བའོ། །

[Block 817]
དགེ་བ་ཡིན་ཡང་། སྐྱེས་ནས་མྱོང་གྱུར་ཉིད། མཐོང་བའི་ཆོས་དང་ལན་གྲངས་གཞན་ལ་མྱོང་བར་འགྱུར་བ་ཡང་མ་ཡིན་ལ། མ་ངེས་པ་ཡང་མ་ཡིན་ནོ། །

[Block 818]
དེ་ཡང་སོ་སོའི་སྐྱེ་བོ་ཁོ་ནའི་ཡིན་པར་འདོད་ཀྱི།[^304] འཕགས་པའི་མ་ཡིན། འཕགས་པ་རྣམས་ནི་འདི་ལ་ལྟུང་བའི་གནས་ལྟ་བུར་གཟིགས་པས་སྙོམས་པར་མི་འཇུག་གོ། །

[Block 819]
འདི་ནི་སེམས་མེད་པ་ཡིན་ཡང་མངོན་པར་འདུ་བྱ་བ་ཆེན་པོས་བསྒྲུབ་པར་བྱ་བ་ཡིན་པའི་ཕྱིར། དུས་གཅིག་ཐོབ། ད་ལྟར་གྱི་དུས་ཁོ་ན་ཐོབ༌[^305]པོ། །སྐད་ཅིག་མ་གཉིས་པ་ལ་སོགས་པར་ནི་ཇི་སྲིད་དུ་ཐོབ་པ་འདས་པ་དང་ལྡན་པ་ཡིན་ནོ། །

[Block 820]
འདུ་ཤེས་མེད་པའི་སྙོམས་པར་འཇུག་པ་ཇི་ལྟ་བར། འགོག་པ་ཞེས་པའང་དེ་བཞིན་ཉིད། །སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་འགོག་པའོ་ཞེས་བྱ་བ་ཙམ་དང་འབྲེལ་བར་བྱའོ། །

[Block 821]
ཁྱད་པར་དུ། འདི་གནས༌[^306]དོན་དུ། ཞི་བར་གནས་པའི་འདུ་ཤེས་མངོན༌[^307]དུ་བཏང་བའི་ཡིད་ལ་བྱེད་པས་འདི་ལ་སྙོམས་པར་འཇུག་གོ། །

[Block 822]
ཡང་དེ་ནི་བསམ་གཏན་བཞི་པའི་ས་པ་ཡིན་གྱི། འདི་ནི་སྲིད་རྩེར་སྐྱེས། འདི་ནི་དགེ་བའོ། །

[Block 823]
དགེ་བ་ཁོ་ན་ཡིན་གྱི་ཉོན་མོངས་པ་ཅན་ཡང་མ་ཡིན་ལ་ལུང་དུ་མ་བསྟན་པ་ཡང་མ་ཡིན་ནོ། །

[Block 824]
དགེ་བ་ཡིན་ཡང་། གཉིས་སུ་མྱོང་འགྱུར་དང་། མ་ངེས། སྐྱེས་ནས་མྱོང་བར་འགྱུར་བ་དང་། ལན་གྲངས་གཞན་ལས་མྱང་བར༌[^308]འགྱུར་བའི་ཕྱིར་དུས༌[^309]གཉིས་སུ་འགྱུར་བ་དང་། རྣམ་པར་སྨིན་པའི་ཕྱིར་མ་ངེས་པ་ཡང་མ་ཡིན་ནོ། །

[Block 825]
དེ་ཡང་མཐའ་གཅིག་ཏུ་འཕགས་པའི། འཕགས་པའི་ཡང་འདི་ནི་འདོད་ཆགས་དང་བྲལ་བས་ཐོབ་པར༌[^310]བྱ་བ་མ་ཡིན་ཏེ། འོན་ཀྱང་སྦྱོར་བས་འཐོབ། [^311]འདི་ནི་སྦྱོར་བས་ཐོབ་པར༌[^312]བྱ་བ་ཁོ་ན་ཡིན་པས་འདས་པ་ཡང་མི་ཐོབ༌[^313]ལ་མ་འོངས་པ་ཡང་མི་ཐོབ༌[^314]སྟེ། དེ༌[^315]ནི་སེམས་ཀྱི་སྟོབས་ཀྱིས་ཐོབ་པའི༌[^316]ཕྱིར་རོ། །

[Block 826]
ཅི་བཅོམ་ལྡན་འདས་ཀྱི་ཡང་སྦྱོར་བ་ལས་བྱུང་བ་ཡིན་ན་མ་ཞེ་ན། སྨྲས་པ་མ་ཡིན་ནོ། །

[Block 827]
འོན་ཀྱང་། ཐུབ་པའི་བྱང་ཆུབ་ཀྱིས་ཐོབ་བྱ། །སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས་ཀྱིས་ནི་འདི་ཟད་པ་མཁྱེན་པ་དང་། དུས་མཉམ་དུ་བརྙེས་སོ། །

[Block 828]
ནུབ་ཕྱོགས་པ་དག་ན་རེ་དེ་ནི་དང་པོ་ཁོ་ནར་བྱང་ཆུབ་སེམས་དཔའ་སློབ་པའི་གནས་སྐབས་ན་སྐྱེད་པར༌[^317]བྱེད་དོ་ཞེས་ཟེར་རོ། །

[Block 829]
ཁ་ཆེ་བ་རྣམས་ན་རེ། དང་པོར་མ་ཡིན། ཅིའི་ཕྱིར་ཞེ་ན། སྐད་ཅིག་མ། སུམ་ཅུ་རྩ་བཞིས་ཐོབ་ཕྱིར་རོ། །

[Block 830]
བྱང་ཆུབ་སེམས་དཔའ་ནི་སེམས་ཀྱི་སྐད་ཅིག་མ་སུམ་ཅུ་རྩ་བཞིས་བྱང་ཆུབ་རྗེས་སུ་ཐོབ༌[^318]སྟེ། བདེན་པ་མངོན་པར་རྟོགས་པ་ན་བཅུ་དྲུག་དང་། སྲིད་པའི་རྩེ་མོའི་འདོད་ཆགས་དང་བྲལ་བ་ན་ཉོན་མོངས་པའི་རྣམ་པ་དགུ་སྤོང་བར་བྱེད་པའི་བར་ཆད་མེད་པ་དང་རྣམ་པར་གྲོལ་བའི་ལམ༌[^319]དགུ་དགུ་སྐྱེ་བའི་ཕྱིར་བཅོ་བརྒྱད་དེ། དེའི་ཕྱིར་བར་སྐབས་འདིར་མི་འདྲ་བའི་སེམས་མི་སྲིད་པས་འགོག་པའི་སྙོམས་པར་འཇུག་པ་མི་རུང་ངོ་། །སྙོམས་པར་འཇུག་པ་འདི་གཉིས་ཀྱི་རྣམ་པའི་བྱེ་བྲག་མང་པོ་ཞིག་ཡོད་མོད་ཀྱི། གཉིས་ཀ་འདོད་དང་གཟུགས་རྟེན་ཅན། །སྙོམས་པར་འཇུག་པ་འདི་གཉིས་ཀ་ཡང་འདོད་པའི་ཁམས་དང་གཟུགས་ཀྱི་ཁམས་སུ་བསྐྱེད༌[^320]དོ། །

[Block 831]
ཡང་། འགོག་པ་དང་པོར་མིའི་ནང་དུ། འགོག་པའི་སྙོམས་པར་འཇུག་པ་ནི་དང་པོར་མི་དག་གི་ནང་དུ་སྐྱེད་དོ། །

[Block 832]
ཕྱིས་ནི་སྔར་ཡོངས་སུ་ཉམས་པ་དེ་དག་གིས་གཟུགས་ཀྱི་ཁམས་སུ་ཡང་སྐྱེད་དོ། །

[Block 833]
སྙོམས་པར་འཇུག་པ་དག་བཤད་ཟིན་ཏོ། །

[Block 834 [HEADING]]
##### སྲོག། ^2-2-3-5-0

[Block 835]
སྲོག་ནི་ཚེ་ཡིན། ཚེ་ཞེས་བྱ་བའི་ཆོས་དེ་གང་ཡིན་པ་དེ་ཡང་མི་ཤེས་པས། དྲོད་དང་ནི། རྣམ་ཤེས་རྟེན་གང་ཡིན་པའོ། །

[Block 836]
གང་དྲོད་དང་རྣམ་པར་ཤེས་པའི་རྟེན་དུ་གྱུར་པའི་ཆོས་གནས་པའི་རྒྱུ་གང་ཡིན་པ་དེ་ནི་ཚེ་ཡིན་ནོ། །

[Block 837]
སྲོག་བཤད་ཟིན་ཏོ། །

[Block 838 [HEADING]]
##### མཚན་ཉིད། ^2-2-3-6-0

[Block 839 [VERSE]]
མཚན་ཉིད་དག་ནི་སྐྱེ་བ་དང་། །
རྒ་དང་གནས་དང་མི་རྟག་ཉིད། །

[Block 840]
བཞི་པོ་འདི་རྣམས་ནི་འདུས་བྱས་ཀྱི་མཚན་ཉིད་དག་ཡིན་ཏེ། གང་ལ་འདི་དག་ཡོད་པའི་ཆོས་དེ་ནི་འདུས་བྱས་སུ་མངོན་ནོ། །

[Block 841]
བཟློག་པ་ནི་འདུས་མ་བྱས་པའོ། །

[Block 842]
སྐྱེ་བ་ལ་སོགས་པ་དེ་དག་ཀྱང༌[^321]འདུས་བྱས་ཡིན་པའི་ཕྱིར་སྐྱེ་བ་ལ་སོགས་པ་གཞན་ཡོད་པར་འགྱུར་རོ་ཞེ་ན། ཡོད་པ་དེ༌[^322]ཁོ་ན་སྟེ། དེ་དག་སྐྱེ་བའི་སྐྱེ༌[^323]ལ་སོགས། །དེ་དག་ལ་ཡང་སྐྱེ་བའི་སྐྱེ་བ་དང་། རྒ་བའི་རྒ་བ་དང་། གནས་པའི་གནས་པ་དང་། མི་རྟག་པ་ཉིད་ཀྱི་མི་རྟག་པ་ཉིད་དོ་ཞེས་བྱ་བ་རྗེས་སུ་མཐུན་པའི་མཚན་ཉིད་བཞི་ཡོད་དོ། །

[Block 843]
རེ་རེ་ལ་ཡང་མཚན་ཉིད་བཞི་པ་དང་། མཐར་ཐུག་པ་མེད་པར་འགྱུར་རོ་ཞེ་ན། མི་འགྱུར་ཏེ། འདི་ལྟར། དེ་ཆོས་བརྒྱད་དང་གཅིག་ལ་འཇུག །ཆོས་བདག་ཉིད་གཏོགས་པར་མཚན་ཉིད་དང་རྗེས་སུ་མཐུན་པའི་མཚན་ཉིད་བརྒྱད་དང་ལྷན་ཅིག་ཏུ་དགུ་སྐྱེ་ལ། དེ་ལ་སྐྱེ་བས་ནི་བདག་ཉིད་མ་གཏོགས་པ་ཆོས་གཞན་བརྒྱད་སྐྱེད་པར་བྱེད་དོ། །

[Block 844]
སྐྱེ་བའི་སྐྱེ་བས་ནི་དེ་ཁོ་ན་སྐྱེད་པར་བྱེད་དོ། །

[Block 845]
དེ་བཞིན་དུ་གནས་པ་ལ་སོགས་པས་གནས་པ་དང་། སྐྱེད་པ་དང་ཉམས་པར་བྱེད་པ་ཞེས་བརྗོད་པར་བྱའོ། །
--- END BLOCKS ---
