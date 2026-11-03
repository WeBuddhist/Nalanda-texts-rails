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
[Block 4271]
འདོད་པ་ན་སྤྱོད་པའི་ལུས་དང་ངག་གི་ལས་ནི་འདོད་པ་ན་སྤྱོད་པའི་འབྱུང་བ་དག་ཁོ་ན་རྒྱུར་བྱས་པ་ཡིན་ལ། དེ་བཞིན་དུ་བསམ་གཏན་བཞི་པའི་ས་པའི་བར་དུ་ཡང་དེའི་ས་པའི་འབྱུང་བ་དག་ཁོ་ན་རྒྱུར་བྱས་པ་ཡིན་ནོ། །

[Block 4272]
ཟག་མེད་གང་དུ་སྐྱེས་པ་ཡིན། །ཟག་པ་མེད་པའི་ལུས་དང་ངག་གི་ལས་དེ་ནི་ས་གང་དུ་སྐྱེས་ཏེ༌[^2553]སྐྱེད་པར་བྱེད་པ་དེའི་ས་པའི་འབྱུང་བ་ཆེན་པོ་དག་རྒྱུར་བྱས་པ་ཡིན་ཏེ། ཁམས་གསུམ༌[^2554]མ་གཏོགས་པའི་ཕྱིར་དང་། ཟག་པ་མེད་པ་རྣམས་ལས་འབྱུང་བ་དག་མེད་པའི་ཕྱིར་དང་། དེའི་སྟོབས་ལས་སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 4273]
རྣམ་པར་རིག་བྱེད་དང་། རྣམ་པར་རིག་བྱེད་མ་ཡིན་པའི་ལས་དེ་ལས་ཀྱང་།

[Block 4274 [VERSE]]
རྣམ་རིག་བྱེད་མིན་མ་ཟིན་དང་། །
རྒྱུ་མཐུན་ལས་བྱུང་སེམས་ཅན་སྟོན། །

[Block 4275]
གཞན་ཡང་། རྒྱུ་མཐུན་ཟིན་པའི་འབྱུང་ལས་སྐྱེ།[^2555] །རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་ནི་རྒྱུ་མཐུན་པ་དང་ཟིན་པའི་འབྱུང་བ་དག་ཁོ་ན་རྒྱུར་བྱས་ནས་སྐྱེ་སྟེ། འདི་ནི་མཉམ་པར་གཞག་པ་མ་ཡིན་པའི་ས་པའི་རྣམ་པ་ཡིན་ནོ། །

[Block 4276 [VERSE]]
ཏིང་འཛིན་སྐྱེས་འབྱུང་མ་ཟིན་དང་། །
རྒྱས༌[^2556]བྱུང་ཐ་དད་མིན་ལས་སྐྱེ། །

[Block 4277]
ཏིང་ངེ་འཛིན་ལས་སྐྱེས་པ་ནི་བསམ་གཏན་དང་ཟག་པ་མེད་པའི་སྡོམ་པའི་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ༌[^2557]ཡིན་ཏེ་དེ་ནི་ཏིང་ངེ་འཛིན་ལས༌[^2558]སྐྱེས་པ་རྒྱས་པ་ལས་བྱུང་བ་དང་མ་ཟིན་པའི་འབྱུང་བ་ཆེན་པོ་དག་རྒྱུར་བྱས་ནས་སྐྱེའོ། །

[Block 4278]
ཐ་མི༌[^2559]དད་པ་དག་ཀྱང་འབྱུང་བ༌[^2560]ཡིན་ཏེ། འབྱུང་བ་ཆེན་པོ་གང་དག་ཁོ་ན༌[^2561]རྒྱུར་བྱས་ནས་སྲོག་གཅོད་པ་སྤོང་བ་སྐྱེ་བ་དེ་དག་ཁོ་ན་ལས་ཚིག་ཀྱལ་པ༌[^2562]སྤོང་བའི་བར་དུ་སྐྱེའོ། །ཅིའི་ཕྱིར་ཞེ་ན། སེམས་བཞིན་དུ་འབྱུང་བ་ཐ་མི་དད་པའི་ཕྱིར་རོ། །

[Block 4279]
སོ་སོར་ཐར་པའི་སྡོམ་པ་ནི་འབྱུང་བ་གཞན་དང་གཞན་དག་རྒྱུར་བྱས་ནས་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་བདུན་སྐྱེའོ། །

[Block 4280]
རྣམ་པར་རིག་བྱེད་ནི་རྒྱུ་མཐུན་པ་ལས་བྱུང་བ་སྟེ། ལུས་ཀྱིས༌[^2563]ནི་ཟིན་པ་ཡིན་ནོ། །

[Block 4281]
ཡང་ཅི་རྣམ་པར་རིག་བྱེད་འདི་སྐྱེ་བ་ན་དབྱིབས་སྔ་མའི་རྒྱུད་བཤིག་ནས་སྐྱེའམ། འོན་ཏེ་མ་ཡིན། དེ་ལས་ཅིར་འགྱུར། གལ་ཏེ་བཤིག་ནས་སྐྱེ་ན་ནི། །རྣམ་པར་སྨིན་པའི་གཟུགས་ཆད་པ་ཡང་རྒྱུན་ཆགས་པའི་ཕྱིར་འདི་བྱེ་བྲག་ཏུ་སྨྲ་བ་མ་ཡིན་པར་འགྱུར་རོ། །

[Block 4282]
འོན་ཏེ་མ་བཤིག་པར་སྐྱེ་ན་ནི་ཇི་ལྟར་འབྱུང་བའི་ཚོགས་གཅིག་ལ་དབྱིབས་གཉིས་འགྲུབ་པར་འགྱུར།[^2564] དེའི་ཚེ་གང་དག་རྒྱུར་བྱས་ནས་རྣམ་པར་རིག་བྱེད་སྐྱེ་བར་འགྱུར་བ་རྒྱུ་མཐུན་པ་ལས་བྱུང་བའི་འབྱུང་བ་ཆེན་པོ་གཞན་དང་། གཞན་དེ་དག་སྐྱེ་བར་འགྱུར་རོ། །

[Block 4283]
དེ་དག་དེ་ལྟ་ན་ནི་འོ་ན་དེའི་འབྱུང་བ་ཆེན་པོ་དེ༌[^2565]དག་གིས་མངོན་པར་ཁྱབ་པའི་ཕྱིར་ཡན་ལག་དང༌[^2566]གང་དང་གང་ལ་བརྟེན་ནས་རྣམ་པར་རིག་བྱེད་སྐྱེ་བར་འགྱུར་བའི་ཡན་ལག་དེ་དང་དེ་ཆེན་པོར་འགྱུར་རོ། །

[Block 4284]
མངོན་པར་མ་ཁྱབ་ན་ནི་ཇི་ལྟར་ན་ཡན་ལག་ཟད་པར་གྱིས་རྣམ་པར་རིག་པར་བྱེད་པར་འགྱུར། ལུས་ལ་གསེབ་ཡོད་པའི་ཕྱིར་དེ་དག་གི་གོ་སྐབས་ཡོད་དོ། །

[Block 4285 [HEADING]]
##### དགེ་བ་དང་མི་དགེ་བ་དང་ལུང་དུ་མ་བསྟན་པ། ^4-2-2-1-0

[Block 4286]
ཡང༌[^2567]ལས་དེ་རྣམ་གྲངས་ཀྱིས༌[^2568]རྣམ་པ་གཉིས་དང༌[^2569]རྣམ་པ་གསུམ་དང་། རྣམ་པ་ལྔར་བཤད་པ་དེ་ལ་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་ནི་དགེ་བ་དང་།

[Block 4287 [VERSE]]
མི་དགེ་བ་རྣམ་པ་གཉིས་སོ། །
རྣམ་རིག་མིན་ལུང་བསྟན་མིན་མེད། །

[Block 4288]
ཅིའི་ཕྱིར་ཞེ་ན། ལུང་དུ་མ་བསྟན་པའི་སེམས་ནི་སྟོབས་ཆུང་བ་ཡིན་ཏེ། དེའི་ཕྱིར་གང་འགགས་ཀྱང་དེའི་རྗེས་སུ་འབྲེལ་པར་འགྱུར་བའི་ལས་སྟོབས་དང་ལྡན་པ་འཕེན་པར༌[^2570]མི་ནུས་སོ། །

[Block 4289]
གཞན་ནི་རྣམ་གསུམ། ལས་གཞན་ནི་དགེ་བ་དང་། མི་དགེ་བ་དང་། ལུང་དུ་མ་བསྟན་པ་དང་། རྣམ་པ་གསུམ་ཡིན་ནོ། །

[Block 4290]
གཞན་དེ་ཡང་གང་ཞེ་ན། རྣམ་པར་རིག་བྱེད་དང་། སེམས་པའོ། །

[Block 4291]
མི་དགེ་ནི། འདོད་ནའོ། །

[Block 4292]
མི༌[^2571]དགེ་བའི་ལས་ནི་འདོད་པའི་ཁམས་ན་ཡོད་པར་རིག་པར་བྱའོ། །

[Block 4293]
གཞན་དག་ན༌[^2572]ནི་མེད་དེ། མི་དགེ་བའི་རྩ་བ་རྣམས་དང་། ངོ་ཚ་མེད་པ་དང་། ཁྲེལ་མེད་པ་དག་སྤངས་པའི་ཕྱིར་རོ། །

[Block 4294]
དགེ་བ་དང་ལུང་དུ་མ་བསྟན་པ་ནི་མ༌[^2573]བཀག་པའི་ཕྱིར་ཐམས་ཅད་ན་ཡོད་དོ། །

[Block 4295]
དེ་ལ་གཟུགས་ནའང་རྣམ་རིག་མིན། །ཡང༌[^2574]གི་སྒྲས་ནི་འདོད་པ་ན་ཡང་ཡོད་དོ། །

[Block 4296]
གཟུགས་མེད་པ་དག་ན་ནི་འབྱུང་བ་མེད་པའི་ཕྱིར་མེད་དོ། །

[Block 4297]
གང་ན་ལུས་དང་ངག་དང༌[^2575]འཇུག་པ་དེ་ན་ལུས་དང་ངག་གི་སྡོམ་པ་ཡོད་དོ། །

[Block 4298]
འོ་ན་འདིར་སྙོམས་པར་འཇུག་པ༌[^2576]ལ་ཡོད་པར་འགྱུར་ཏེ། ཟག་པ་མེད་པའི་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་བཞིན༌[^2577]ནོ་ཞེ་ན། མ་ཡིན་ཏེ། དེ་ནི་ཁམས་སུ་མ་གཏོགས་པའི་ཕྱིར་རོ། །

[Block 4299]
གཟུགས་མེད་པ་ན་སྤྱོད་པའི་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་ནི་སྐལ་པ་མི་མཉམ་པའི་འབྱུང་བ་རྒྱུར་བྱས་ནས་སྐྱེ་བ་ནི་འོས་པ་མ་ཡིན་ནོ། །

[Block 4300]
གཟུགས་ཐམས་ཅད་ལ་རྒྱབ་ཀྱིས་ཕྱོགས་པའི་ཕྱིར་ཡང་གཟུགས་མེད་པའི་སྙོམས་པར་འཇུག་པའི༌[^2578]གཟུགས་སྐྱེད་པར༌[^2579]མི་ནུས་ཏེ། གཟུགས་ཀྱི་འདུ་ཤེས་དང་བྲལ་བའི་ཕྱིར་རོ། །

[Block 4301]
བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ་ཚུལ་ཁྲིམས་ནི་འཆལ་པའི་ཚུལ་ཁྲིམས་ཀྱི་གཉེན་པོ་ཡིན་ལ། འཆལ་པའི་ཚུལ་ཁྲིམས་དེ་ཡང་འདོད་པ་ན་སྤྱོད་པ་ཡིན་ན་གཟུགས་མེད་པ་རྣམས་ནི་འདོད་པའི་ཁམས་ནས་རྟེན་དང་རྣམ་པ་དང་དམིགས་པ་དང་གཉེན་པོ་རིང་བ་དག་གིས་རིང་སྟེ། དེའི་ཕྱིར་འདི་དག་ན་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་མེད་དོ་ཞེས་ཟེར་རོ། །

[Block 4302]
རྣམ་རིག་དཔྱོད་དང་བཅས་དག་ན། །རྣམ་པར་རིག་བྱེད་ནི་ས་གཉིས་པོ་འདོད་པའི་ཁམས་དང་། བསམ་གཏན་དང་པོ་ཁོ་ན་ན་ཡོད་ཀྱི་དེ་ཡན་ཆད་ན་ནི་མེད་དོ། །

[Block 4303]
འདོད་པ་ན་ཡང་བསྒྲིབས་པ༌[^2580]མེད་ན། བསྒྲིབས་པ་མེད༌[^2581]པའི་རྣམ་པར་རིག་བྱེད་ནི་འདོད་པའི་ཁམས་ན་ཡང་མེད་ཀྱི་ཚངས་པའི་འཇིག་རྟེན་ཁོ་ན་ན་ཡོད་དོ། །

[Block 4304]
ཚངས་པ་ཆེན་པོ་ལ་ཡང་གཡོས་ཀུན་ནས་སློང་བའི༌[^2582]ངག་གི་ལས་ཡོད་དེ། དེས་རང་གི་འཁོར་གྱི་ནང་དུ་ཚེ་དང་ལྡན་པ་རྟ་ཐུལ་ལ་གཏམ་རླུང་བསྐུར་བའི་ཕྱིར་བདག་ཉིད་རྣམ་པར་བསྔགས་སོ་ཞེས་གྲག་གོ། །

[Block 4305]
དེ་ཡན་ཆད་ནི་ངག་གི་རྣམ་པར་རིག་བྱེད་མེད་ན་སྒྲའི་སྐྱེ་མཆེད་ཇི་ལྟར་ཡོད་ཅེ་ན། ཕྱིའི་འབྱུང་བ་ཆེན་པོའི༌[^2583]རྒྱུར་བྱས་པ་ཡོད་དོ། །

[Block 4306]
གཞན་དག་ན་རེ་བསམ་གཏན་གཉིས་པ་ལ་སོགས་པ་དག་ན༌[^2584]ཡང་མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པའི་རྣམ་པར༌[^2585]རིག་བྱེད་ནི་ཡོད་ཀྱི་དགེ་བ་ཡང་མེད་ལ། ཉོན་མོངས་པ་ཅན་ཡང་མེད་དོ། །

[Block 4307]
[^2586]ཅིའི་ཕྱིར་ཞེ་ན། དེ་དག་ཏུ་སྐྱེས་པ་ནི་ས་འོག་མ་པའི༌[^2587]སེམས་གང་གིས་ན་རྣམ་པར་རིག་བྱེད་ཀུན་ནས་སློང་བར་འགྱུར་བ་དེ་ལྟ་བུ་ནི་མངོན་སུམ་དུ་མི་བྱེད་དེ། དམན་པ་དང་སྤངས་ཟིན་པའི་ཕྱིར་རོ་ཞེས་ཟེར་ཏེ་སྔ་མ་ཁོ་ན་བརྗོད་དོ། །

[Block 4308]
ཅིའི་ཕྱིར་ཚངས་པའི་འཇིག་རྟེན་ཡན་ཆད་ན་རྣམ་པར་རིག་བྱེད་མེད་ལ། འདོད་པའི་ཁམས་ན་ཡང་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་མེད་ཅེ་ན། གང་ཕྱིར་ཀུན་སློང་མེད། རྟོག་པ་དང་དཔྱོད་པ་དང་བཅས་པའི་སེམས་ཀྱིས་རྣམ་པར་རིག་བྱེད་ཀུན་ནས་སློང་བར་བྱེད་ན། དེ་ཡང་བསམ་གཏན་གཉིས་པ་ལ་སོགས་པ་དག་ན་མེད་དོ། །

[Block 4309]
བསྒོམ་པས་སྤང་བར་བྱ་བས་སློང་བར་བྱེད་ཀྱི་དེ་ཁ་ནང་དུ་བལྟས་པའི་ཕྱིར་མཐོང་བས་སྤང་བར་བྱ་བ་ནི་མ་ཡིན་ནོ། །

[Block 4310]
[^2588]བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པའི་སེམས་དེ་ཡང་འདོད་པའི་ཁམས་ན་མེད་དོ། །
--- END BLOCKS ---
