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
[Block 3921]
ངན་སོང་དང་བདེ་འགྲོའི་དབྱེ་བས་གཉིས་སུ་ཡང་འདོད་དོ། །

[Block 3922]
རྒ་བ་ཡང་ནུས་པ་དང་བྲལ་བའི་མཚན་ཉིད་ཀྱི༌[^2427]ཆོས་སོ། །

[Block 3923]
ཤི་བ་ནི་ཕུང་པོ་འདོར་བས༌[^2428]རྣམ་པར་ཤེས་པའི་སྐད་ཅིག་མ་ཚོར་བ་ལ་གནས་པའི་ངོ་བོ་ཆོས་བདུན་པོ་དེ་དག་ནི་སྐྱེ་བ་སྟེ་སྐྱེས༌[^2429]པ་ལ་ནི་རྣམ་པར་ཤེས་པ་ལ་སོགས་པའི་ཆོས་བདུན་དང་འབྲེལ་པའི་ཕྱིར་རོ། །

[Block 3924]
ཉོན་མོངས་པ་དང་ལས་དང་སྐྱེ་བ་འདི་དག་གིས་ཁམས་གསུམ་ན་གནས་པའི་སེམས་ཅན་གྱི་ཚོགས་ཟོ་ཆུན་གྱི་འཁྲུལ་འཁོར་བཞིན་དུ་འཁོར་བར་བྱེད་པས་འགྲོ་བ་གཅིག་ནས་གཅིག་ཏུ་ཐོབ་པར་གྱུར་ནས་ཉོན་མོངས་པ་ཚོན་པོ་མྱོང་བར་འགྱུར་རོ། །

[Block 3925 [VERSE]]
ཐལ་ཚན་གྱི་ཆུ་བོའི་མདོ་ལས་ཀྱང་། །
ནོར་ཕྲོགས་རྐུན་མ་ལས་ཀྱང་བདག་མི་འཇིགས། །
དེ་ཡིས་ནོར་ཕྲོགས་དེ་ཡང་ཡོད་མ་ཡིན། །
ཡིད་ལ་བསགས་ཤིང་བསགས་པའི་དག་པའི་ནོར། །

[Block 3926]
ཐ་མལ་རྟོག་པ༌[^2430]དག་གིས་ངེས་པར་འཕྲོག །ཅེས་དགོན་པའི་དགེ་སློང་གིས༌[^2431]ལག་པ་གྱེན་དུ་བརྐྱང་ཞེས་ཉིན་མོའི་འོ་དོད་འབོད་ཅེས་འབྱུང་ངོ་། །དེ་བས་ན་ཉོན་མོངས་པའི་དབང་གིས་ལས་འབྱུང་བ་དང་། ལས་ཀྱི་དབང་གིས་སྐྱེ་བ་དང་། དེ་ལས་ཀྱང་ལས་དང་། ཡང་ཉོན་མོངས་པ་སྐྱེ་ཞེས་འཁོར་བ་ཐ་མ་མེད་པ་འཁོར་ལོ་བཞིན་དུ་ཡོངས་སུ་འཁོར་བའོ། །

[Block 3927]
སྲིད་པའི་འཁོར་ལོ་འདི་ནི་བདག་ལ་སོགས་པ་གང་གིས་ཀྱང་མི་བསྐྱེད་དེ། །སྟོང་པ་ཁོ་ན་ལས་ཀྱང་ཆོས་སྟོང་པ་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 3928]
ཇི་སྐད་དུ།

[Block 3929 [VERSE]]
གསུམ་ལས་གཉིས་པོ་སྐྱེ་བར་འགྱུར་བ་སྟེ། །
གཉིས་ལས་བདུན་པོ་སྐྱེ་ཞིང་བདུན་ལས་ནི། །
གཉིས་པོ་ཡང་དག་སྐྱེ་འགྱུར་དེ་ཕྱིར་འདི། །
ཐོག་མ་མེད་པའི་སྲིད་པའི་འཁོར་ལོ་ཡིན། །

[Block 3930 [VERSE]]
སྟོང་པ་ཁོ་ནའི་ཆོས་ལས་ཆོས་རྣམས་ནི། །
སྟོང་པའི་རང་བཞིན་རབ་ཏུ་སྐྱེ་བར་འགྱུར། །

[Block 3931]
ཁ་ཐོན་མར་མེ་མེ༌[^2432]ལོང་རྒྱ།

[Block 3932 [VERSE]]
མེ་ཤེལ་ས་བོན་སྐྱུར་དང་སྒྲ། །
ཕུང་པོ་ཉིང་མཚམས་སྦྱོར་བ་ཡང་།[^2433] །
མི་འཕོ་བར་ཡང་མཁན༌[^2434]རྟོགས་བྱ། །

[Block 3933]
ཞེས་འབྱུང་ངོ་། །དེའི་ཕྱིར་ཉོན་མོངས་པ་དང་ལས་དང༌[^2435]སྐྱེ་བ་ཉིད༌[^2436]ནི་ཉེ་བར་འཚེ་བ་སྟེ་སྐྱོན་ཆེན་པོའོ། །

[Block 3934]
དེ་རྣམས་རིམ་པ༌[^2437]གཉིས་སྒོམ་པའི་སྒོ་ནས་བཟློག་པ་ནི་ཉེ་བར་བྱེད་པས་གོས་དང་འདྲ་བས་གོས་སོ། །

[Block 3935]
དེ་ལེན་ཅིང་འཛིན་པས་ན་ཞེས་པ་ལ། བསྐྱེད་པ༌[^2438]དང་རྫོགས་པའི་མཚན་ཉིད་ཅན་གྱིས༌[^2439]བརྗོད་པར་བྱ་བའི་དོན་རྗོད་པར་བྱེད་པའི་ཚིག་གི་མཚན་ཉིད་དོ། །

[Block 3936]
དེ་སྟོན་པའི་གཞུང་གི་ཚོགས་ལ་ཡང་ལེའུ་ཞེས་བྱའོ་ཞེས་པ་ནི་རིམ་པ་གཉིས་ཀའི་ངོ་བོ་རྟོག་པ་དང་ཡོངས་སུ་རྫོགས་པའི་ལྷའི་སྐུ་སྟོན་པར་བྱེད་པའི་ཚིག་གི་ཚོགས་ནི་ལེའུ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3937]
ལ་ལ་ནི་རླུང་དང་ཆར་པ་ལ་སོགས་པའི་སྐྱོན་སེལ་བར་བྱེད་པའི་ཁྱིམ་གྱི་བླ་གབ་བཞིན་དུ༌[^2440]ཉོན་མོངས་པ་དང་ཞེས་བྱ་བ་ལ་སོགས་པའི་སྒྲིབ་པ་ཞི་བར་བྱེད་པས་ལེའུ་ཞེས་སྨྲའོ། །

[Block 3938]
སྒྲོན་མ༌[^2441]གསལ་བར་བྱེད་པ་ཞེས་བྱ་བའི་འགྲེལ་པའི་ཊཱི་ཀཱ་ལས་ལེའུ་དང་པོའོ།། །།

[Block 3939 [HEADING]]
## ལེའུ་གཉིས་པ། ^2-0

[Block 3940]
དེ་ལྟར་ལེའུ་དང་པོས༌[^2442]ཐམས་ཅད་བསྐྱེད་ནས་ཞེས་པ་ནི་ལེའུ་དང་པོས་ནི་རྒྱུད་ཀྱི་དོན་མ་ལུས་པ་མཚོན་པར་བྱེད་པ་གླེང་གཞིའི་ཚིག་གི་ཁྱད་པར་དུ་གྱུར་པའི་ལེའུས་སོ། །

[Block 3941]
ཐམས་ཅད་བསྐྱེད་པ་ནི་བཅོམ་ལྡན་འདས་རྡོ་རྗེ་འཆང་ཆེན་པོས་མ་འོངས་པའི་སེམས་ཅན་གདུལ་བར་བྱ་བའི་ཕྱིར་འདོད་ཆགས་ཆེན་པོའི་ཏིང་ངེ་འཛིན་གྱིས་ལྷ་མོའི་འཁོར་ལོ་ཉེ་བར་སྤྱོད་པ་དང་། བགེགས་བསྐྲད་པ་ནས་བརྩམས་ཏེ་གཞལ་ཡས་ཁང་པ་དང་ལྷག་པར་མོས་པའི་དཀྱིལ་འཁོར་དང་དོན་དམ་པའི་དཀྱིལ་འཁོར་དང་། [^2443]པདྨ་ལ་སོགས་པའི་གདན་དང་ཆོས་ཀྱི་དབྱིངས་ཀྱི་དེ་ཁོ་ན་ཉིད་མངོན་དུ་བྱ་བ་དང་། ཡི་གེ་གསུམ་ཡོངས་སུ་གྱུར་པ་ལས་སྐྱེས་པའི་དཀྱིལ་འཁོར་གྱི་གཙོ་བོ་བསྒོམ་པ་དང་མིག་ལ་སོགས་པ་བྱིན་གྱིས་རློབ་པ་དང་། སྐུ་གསུང་ཐུགས་བྱིན་གྱིས་རློབ་པའི་བར་དུ་དང་པོ་སྦྱོར་བའི་ཏིང་ངེ་འཛིན་གྱི་འོག་ཏུ་ཕྱག་རྒྱ་སྦྱང་བ༌[^2444]དང་། རྡོ་རྗེ་དང་པདྨ་སྙོམས་པར་ཞུགས་པ་དང་། དེ་ལས་མི་བསྐྱོད་པ་ལ་སོགས་པ་དཀྱིལ་འཁོར་པ་སྤྲོ་བ་དང་། དེ་དག་གིས་སེམས་ཅན་གྱི་དོན་བྱ་བ་དང་། དཀྱིལ་འཁོར་གྱི་ཤར་ལ་སོགས་པའི་ཕྱོགས་སུ་དགོད་པ་དང་། ཅོད་པན་དུ་བྱ་བ་བསྟན་ཏོ། །

[Block 3942]
སེམས་རྣམ་པར་དག་པ་ལ་སོགས་པའི་རིམ་པས་ཡང་དག་པར་འབྱུང་བའི་ཡོངས་སུ་དག་པའི་ལྷའི་སྐུ་རྫོགས་པའི་རིམ་པའི་ཕྱོགས་སུ་བསྟན་པ་ནི་དེ་དག་ཐམས་ཅད་བསྐྱེད་པར༌[^2445]བསྟན་ཏོ། །

[Block 3943]
རྫོགས་པའི་རིམ་པ་གསལ་བར་བྱ་བའི་ཕྱིར་ཞེས་པ་ནི་དཔལ་གསང་བ་འདུས་པའི་རྒྱུད་བསྟན་པའི་ཆེད་དུ་ལྷའི་རྣལ་འབྱོར་གཉིས་ཀྱི་རང་བཞིན་དམ་ཚིག་གི་དཀྱིལ་འཁོར་སྤྲོས་ཏེ། ད་ནི་དོན་དམ་པའི་བདེན་པ་གཅིག་པུ་གཏོད་པའི་རང་བཞིན་གྱི་དེ་ཁོ་ན་ཉིད་བསྐྱེད་པའི་རིམ་པའི༌[^2446]རྒྱུར་གྱུར་པ་དང་། རྡོ་རྗེ་བཟླས་པ་ལ་སོགས་པའི་མཚན་ཉིད་རྫོགས་པའི་རིམ་པ་ལྔ་ཡང་གསལ་བར་བྱ་བའི་ཕྱིར་རོ། །

[Block 3944]
བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་ལེའུ་ནི་གདོད་མ་ནས་མ་སྐྱེས་པའི་རང་བཞིན་སྟོན་པར་བྱེད་པའི་ལེའུའོ། །

[Block 3945]
གསུངས་ཏེ་ནི་གསུངས་པའོ་ཞེས་སྦྱར་བ་ནི་བྱ་བ་དང་བྱེད་པ་པོའི་སྒྲ་དག་གི་ཕན་ཚུན་འབྲེལ་པའོ། །

[Block 3946]
རྡོ་རྗེ་འཆང་ཆེན་པོ་ནི་སྐུ་ལ་སོགས་པ་ཉེ་བར་བསྡུས་པའི་མཚན་ཉིད་དཔལ་རྡོ་རྗེ་སེམས་དཔའ་ལའོ། །

[Block 3947]
མཆོད་པ་ནི་མེ་ཏོག་མ་ལ་སོགས་པའི༌[^2447]ལྷ་མོ་སྤྲོས་པས་སོ།[^2448] །

[Block 3948]
བཅོམ་ལྡན་འདས་ལ་གསོལ་བ་བཏབ་པ་ནི་བྱང་ཆུབ་སེམས་ཀྱི་ལེའུ་ཉན་པའི་དོན་དུའོ། །

[Block 3949]
སྐུ་དང་གསུང་དང་ཐུགས་དང༌[^2449]གསུམ་གྱི་མི་ཕྱེད་པའི་ངོ་བོ་ཉིད་ནི་ཐ་མལ་པའི་ལུས་ལ་སོགས་པ་སྟོང་པ་ཉིད་ཀྱི་བསྒོམ་པས་མི་སྣང་བར་བྱས་པས་རྡོ་རྗེའི་རང་བཞིན་དུ་སྐྱེ་བར་འགྱུར་རོ། །

[Block 3950]
རྒྱུ་ལ་འབྲས་བུའི་ཉེ་བར་གདགས་པས་མཆོག་ནི་རྒྱུ་ནི་སྟོང་པ་ཉིད་ཀྱི་དེ་ཁོ་ན་ཉིད་དོ། །

[Block 3951]
འབྲས་བུ་ནི་དེའི་དབང་གིས་སྐུ་ལ་སོགས་པ་མི་ཕྱེད་པར་ཐོབ་པའོ། །

[Block 3952]
དེ་དག་དབྱེར་མེད་པར་བྱས་ཏེ་སྐུ་གསུང་ཐུགས་ཁོ་ན་མཆོག་ཏུ་བཤད་དོ། །

[Block 3953]
གང་གི་ཕྱིར་ཉེ་བར་བཏགས་པ༌[^2450]ནི་རྒྱུ་མཚན་གསུམ་གྱིས་འགྱུར་ཏེ། དོན་གཙོ་བོ་བཀག་པ་དང་། རྒྱུ་མཚན་དང་དགོས་པས༌[^2451]སོ། །

[Block 3954]
དཔེར་ན་ཚོང་དཔོན་བ་ལང་ཡིན་ཏེ། བ་ལང་དང་ཚོང་དཔོན་ཕྱུགས་དང་མི་དང་ཤིན་ཏུ་འགལ་བ་ཡིན་པས་དོན་གཙོ་བོ་བཀག་པའོ། །

[Block 3955]
རྒྱུ་མཚན་ནི་གསལ་བ་དང་བླུན་པ་ལ་སོགས་པའི་ཡོན་ཏན་དང་འབྲེལ་པའོ། །

[Block 3956]
གང་གི་དབང་གིས་གཞི་མཐུན་པའི་སྒོ་ནས་བ་ལང་དང་ཚོང་དཔོན་དག་བྱེད་པའི་ཚིག་དང་པོས་སོ་སོར་བསྟན་ཏོ། །

[Block 3957]
དགོས་པ༌[^2452]ནི་བ་ལང་དང་འདྲ་བར་རྨོངས་པར་གྱུར་པའི་ཚོང་དཔོན་ལ་མི་རྩི་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3958]
དེ་བཞིན་དུ་འདིར་ཡང་སྐུ་གསུང་ཐུགས་དང་བྱང་ཆུབ་ཀྱི་སེམས་ཕན་ཚུན་འགལ་བ་སྟེ་འདུས་བྱས༌[^2453]པ་དང་འདུས་མ་བྱས་པ༌[^2454]ཉིད་ཀྱིས་དོན་གཙོ་བོ་བཀག་པའོ། །

[Block 3959]
རྒྱུ་མཚན་ནི་དེ་ལ་དམིགས་པའི་ཡོན་ཏན་གྱི་འབྲེལ་པའོ། །

[Block 3960]
གང་གི་དབང་གིས་སྐུ་གསུང་ཐུགས་ནི་བྱང་ཆུབ་ཀྱི་སེམས་ཞེས་གཞི་མཐུན་པས་དོན་གཉིས་ཀ་ཡང་བྱེད་པའི་ཚིག་དང་པོས་བརྗོད་དོ། །
--- END BLOCKS ---
