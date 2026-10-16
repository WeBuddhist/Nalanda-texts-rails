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
[Block 3711]
དེ་ལ་དོགས་པ་དང་བྲལ་བ་གང་ཡིན་པ་དེ་ནི་དེས་གནོད་པ་བྱས་སུ་མི་དོགས་པའོ། །

[Block 3712]
འདིས་ནི་འཇིག་རྟེན་འདིའི་འཇིགས༌[^2405]པ་མེད་པར་བསྟན་ཏོ། །

[Block 3713]
འདོད་པའི་འདོད་ཆགས་ཀྱི་དབང་དུ་ཡང་གྱུར་པས་ཞེས་བྱ་བ་ནི་འཇིག་རྟེན་ཕ་རོལ་གྱི་འཇིགས་པ་མེད་པར་སྟོན་ཏོ། །

[Block 3714]
འདོད་པའི་འདོད་ཆགས་ཀྱིས་ཟིལ་གྱིས་མནན་པ་དེས་ཆོས་ལ་མི་ལྟ་བས་སོ། །

[Block 3715]
འཇིགས་པ་དང་། བག་ཚ་བ་ནི་འཇིགས་པ་དང་བག་ཚ་བ་སྟེ། དེ་གཉིས་ཀྱིས་བཞིན་གྱུར་པ་གང་ཡིན་པ་དེ་ནི་འཇིགས་ཤིང་བག་ཚ་བས་ངོ་འཛུམ་འགྱུར་བའོ། །

[Block 3716]
རྒྱལ་པོའི་མཐུས་ཕོ་བྲང་གི་ནང་དུ་ཁྲིད་ཅེས་ཐོས་པས་ནི། གཅན་གཟན་མ་རུངས་པས་དགོ་བ་མོ་གཙེས་པ་བཞིན༌[^2406]དུ་འཇིགས་ཤིང་བག་ཚ་བས་ངོ་འཛུམ་འགྱུར་བའོ། །

[Block 3717]
འདིར་སྐྱོབ་པ་ནི་གཞན་མེད་པའི་ཕྱིར། སྐྱེ་དགུ་སྐྱོང་བའི་རྒྱལ་པོས་ཁྱེར་བར་གྱུར་ན། གཞན་སུ་ཞིག་སྐྱོབ་པར་འགྱུར་ཏེ། ནགས་ཀྱི་དགོ་བ་མོ་བཞིན་ནོ། །

[Block 3718]
དེ་བས་ན་དེ་ཉིད་ཀྱི་ཕྱིར། ནགས་ཞེས༌[^2407]སྨོས་པ་ཡིན་ཏེ། གང་གི་ཕྱིར་གཞན་དུ་ན་ནི་དགོ་བ་མོ་ཞེས་བྱ་བ་ཉིད་སྟོན་པར་འགྱུར་རོ། །

[Block 3719]
དེ་ཉིད་ཀྱི་ཕྱིར་འཇིགས་ཤིང་བག་ཚ་བས་ངོ་འཛུམ་འགྱུར་བ་ཉིད་ཀྱི་རྒྱུ་བསྟན་པའི་ཕྱིར། འཇིག་རྟེན་ཕོངས་ཤིང་ཞེས་བྱ་བའི་ཚིགས་བཅད་བརྩམས་པ་ཡིན་ནོ། །

[Block 3720]
དེ་ཉིད་གང་ལ་མི་རིགས་བྱེད་གྱུར་ན། །ཞེས་བྱ་བ་འདིས་ན༌[^2408]འཇིགས་པ་དང་། བག་ཚ་བའི་རྒྱུ་བསྟན་ཏོ། །

[Block 3721]
ཡང་ན་དེ་ཉིད་གང་ལ་མི་རིགས་བྱེད་གྱུར་ན། །ཞེས་བྱ་བ་འདིས་ནི་འཇིགས་པའི་རྒྱུ་བསྟན་ཏེ། དེ་ཡིས་སུ་ལ་ཕ་སྐྱབས་བཙལ་བར་བྱ། །ཞེས་བྱ་བ་འདིས་ནི་བག་ཚ་བའི་རྒྱུ༌[^2409]བསྟན་ཏེ། ཕ་སྐྱབས་དེ་མེད་ཀྱང་གང་དག་འཇིག་རྟེན་སྐྱོང་བ་དང་། གཞན་ཡང་སྐྱེ་བོས་བྱེད་པ་དག །སྐྱབས་བྱེད་པ་མེད་ཅེས་བསྟན་པའི་ཕྱིར། ཀྱེ་མ་འཇིག་རྟེན་སྐྱོང་བའང་། །[^2410]ཞེས་བྱ་བའི་ཚིགས་བཅད་བརྩམས་པ་ཡིན་ཏེ། ཚུལ་ལས་ཉམས་ཞེས་བྱ་བ་ནི་འཇིག་རྟེན་སྐྱོང་བ་ཉིད་ཉམས་པའམ། འཇིག་རྟེན་སྐྱོང་བའི་མིང་ཉིད་ཉམས་ནས་མེད་པ་སྟེ། གཞན་གྱི་དོན་མི་བྱེད་པའི་ཕྱིར། [^2411]དེ་འཇིག་རྟེན་སྐྱོང་བ་དེ་ལས་ཉམས་པའམ་མེད་པའོ། །དེ་ཅིའི་ཕྱིར་ཞེ་ན། ལེགས་པར་མི་སྐྱོང་བས་སོ། །

[Block 3722]
ཤི་བར་གྱུར་ཏམ་ཅི་ཞེས་བྱ་བས་ནི་ལྷའི་འགྲོ་བ་དེ་ལས་ཉམས་པའོ། །

[Block 3723]
དེ་ནས་གལ་ཏེ་ཡོད་ཀྱང་ཚུལ་ལས་ཉམས་པ་དེས་མི་ནུས་པའམ། ཤི་བས་གང་དག་ཕོངས་པ་ལེགས་པར་སྐྱོབ་པར་མི་བྱེད་པའོ། །

[Block 3724]
རང་བཞིན་གྱིས་ཀྱང་ཡོངས་སུ་བསྲུང་བར༌[^2412]ནུས་མོད་ཀྱི། བདག་ལ་མི་བསྲུང་བ༌[^2413]ཡིན་ནོ་ཞེས་བསྟན་པའི་ཕྱིར། ཇོ་བོ་བཞུགས་བཞིན་ལྷ་ཡིས་ཅི་ཞིག་བགྱི། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 3725]
གཞན་ཞིག་ཡིན་ནའང་རྗེས་སུ་བསྲུང་བར་རིགས་ན་བདག་ནི་ཆོས་སྤྱོད་པའི་གྲོགས་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3726]
སྙིང་རྗེའི་སྣོད་དུ་མ་གྱུར༌[^2414]ཅེས་བྱ་བ་ནི་སྙིང་རྗེའི་དངོས་པོ་དང་བདག་ཉིད་སྐལ་བར༌[^2415]འགྱུར་བའི་ཕྱིར་གསོ་བའི་དངོས་པོར་མ་གྱུར་པ་སྟོན་ཏོ། །

[Block 3727]
བྱང་ཆུབ་སེམས་དཔའ་དེ་ནི་ཕོངས་པ་རྣམས་ལ་བསྒྲུབ་པ་དང་། རྗེས་སུ་མཐུན་པར་བསྟན་པའི་ཕྱིར། ཕོངས་ལ་སྙིང་རྗེ་ཅན་གྱིས་ཞེས་བྱ་བའི་ཚིགས་བཅད་འོག་མ་ཡིན་ཏེ། བདག་ནི་སྙིང་རྗེའི་དོན༌[^2416]མ་གྱུར་པ་ཉིད་དོ། །

[Block 3728]
རབ་ཏུ་བྱུང་བ་རྣམས་ནི་ཕོངས་པ་རྣམས་སྒྲུབ་པ་དང་མི་འགལ་བར་བྱེད་མོད་ཀྱི། འོན་ཀྱང་མི་སྒྲུབ་པའི་རྒྱུ་གཞན་བསྟན་པའི་ཕྱིར། བདག་ནི་སླད་དུ་བཟློག་ཀྱང་མ་ལོག་པར༌[^2417]ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 3729]
སོ་སོར་བརྟགས་པའི་སྟོབས་ཀྱིས་ཁྲོ་བའི་སྟོབས་བཅིལ་ཞེས་བྱ་བ་ནི་གང་སྔར་བསྟན་པའི་རྒྱགས་པས་བསྙེམས་སམ། གལ་ཏེ་མ་བརྟགས་པར་ཞེས་བྱ་བ་དེ་འདིས་བསྟན་པ་ཡིན་ནོ། །

[Block 3730]
དེ་འཁྲུགས་པ་དང་བྲལ་བ་གང་ཡིན་པ་དེ་ནི་འཁྲུགས་པ་མེད་པའོ། །

[Block 3731]
སེམས་རབ་ཏུ་ཞི་བ་གང་ཡིན་པ་དེ་ནི་སེམས་རབ་ཏུ་ཞི་བའོ། །

[Block 3732]
འཁྲུགས་པ༌[^2418]མེད་པ་དང་། སེམས་རབ་ཏུ་ཞི་བ་ནི་སེམས་འཁྲུགས་པ༌[^2419]མེད་ཅིང་རབ་ཏུ་ཞི་བའོ། །

[Block 3733]
འཁྲུགས་པ༌[^2420]མེད་པ་ནི་ཁྲོ་བོའི༌[^2421]སྟོབས་ཀྱིས་ཟིལ་གྱིས་མི་ནོན༌[^2422]པའི་ཕྱིར་རོ། །

[Block 3734]
སེམས་རབ་ཏུ་ཞི་བ་ནི་སོ་སོར་བརྟགས་པའི་སྟོབས་ཀྱིས་སོ། །

[Block 3735]
བསྙེངས༌[^2423]ཤིང་གསང་བསྟོད༌[^2424]ཅེས་བྱ་བ་ནི་གང་སྔར་བསྟན་པའི་རྒྱགས་པས་བསྙེམས་པས་ཞེས་བྱ་བའི་ཚིགས་བཅད་དོ། །

[Block 3736]
མཐུ་མེད་པས་ཞུམ་ཞིང་ཞི་བར་གྱུར་པ་གང་ཡིན་པ་དེ་ནི་མཐུ་མེད་པས་ཞུམ་ནས་རབ་ཏུ་ཞི་བ༌[^2425]སྟེ། གང་སྔར་བསྟན་པའི་སེམས་འཁྲུགས་པ་མེད་ཅིང་རབ་ཏུ་ཞི་བ་ཞེས་བྱ་བ་དེ་བསྟན་པའོ། །

[Block 3737]
མཐུ་རྩལ་ཞེས་བྱ་བ་དེ་ལུས་ཀྱི་སྟོབས་སོ། །

[Block 3738]
དཀའ་ཐུབ་གནས་པའི་གཟི་བརྗིད་བསགས་པའང་སྟོན།[^2426] །ཞེས་བྱ་བ་ནི་དཀའ་ཐུབ་བསྟན་པའི༌[^2427]སྟོབས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3739]
བདག་གི་ཚོད༌[^2428]དེ་བཟུང་བ་ནི་བདག་གི་ཚོད་བཟུང་བའོ། །

[Block 3740]
དེ་མི་རིགས་པ༌[^2429]ནི་བདག་གི་ཚོད་ཀྱང་བཟུང་བར་མ༌[^2430]ཤེས་པ་སྟེ། བདག་ཉིད་མི་ཤེས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3741]
གཡོ་བ་བཞིན་དུ་ཡང་བདག་གིས་ཡོངས་སུ་མ་བཏང་བ་ཞེས་བྱ་བ་ནི་གང་སྔར་བསྟན་པའི་རྒྱགས་པས་བསྙེམས་སམ་ཞེས་བྱ་བ་སྟེ་ཁྲོ་བའི་དབང་དུ་བྱས་པའོ། །

[Block 3742]
མངོན་སུམ་དུ་ཡང་ཞི་བར་བགྱིས་ཞེས་བྱ་བ་ནི་གང་སྔར་བསྟན་པའི་མ་བརྟགས་པ་ཞེས་བྱ་བ་ཡིན་ཏེ། ཁྲོ་བའི་སྟོབས་མ་བརྟགས་པ་དེ་ཉིད་བསྟན་པ་ཡིན་ནོ། །

[Block 3743]
རྟོག་པ་སྐྱེས་ནས་ཞེས་བྱ་བ་ནི༌[^2431]དཔྱོད་པ་སྐྱེས་པའོ། །

[Block 3744]
སྐྱེས༌[^2432]ནའང་གང་ཞིག་མི་མངོན་ལ། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཀྱི་བསྡུས་པའི་དོན་ནི་ཁྲོ་བའི་མཚན་ཉིད་ཀྱི་ངོ་བོ་ཉིད་དང་། ལས་བསྟན་ཏེ་སྐྱེས་ན་གང་ཞིག་ཅེས་བྱ་བ་ནི་ཁྲོ་བ་སྐྱེས་པ་དེས་སོ། །

[Block 3745]
ཁྲོ་བ་གང་ཞིག་སྐྱེས་ན་མི་མངོན་པ་ནི་ཁྲོ་བའི་ལམ༌[^2433]ཡིན་ཞིང་བཟང་བ་སྟེ་དགེ་བ་ཉིད་དོ། །

[Block 3746]
ཡང་ན་སྐྱེས་པར་སྣང་བ་དེ་གང་ཡིན་ཞེ་ན། དགེ་བ་སྟེ་མཁས་པའོ། །

[Block 3747]
དེས་ན་སྐྱེས་བུ་ཡང་མི་མངོན་པ་དེ་ནི་དགེ་བ་ཡིན་ཏེ། མཁས་པ་འང་བདག་ཉིད་ལ་ཕན་པའོ། །

[Block 3748]
འདི་ནི་ཁྲོ་བའི་རང་གི་ངོ་བོའོ། །

[Block 3749]
མ་གྱུར་ཏོ་ཞེས་བྱ་བ་ནི་ཤོར་བར་མ་གྱུར་པའོ། །ཇི་ལྟར་མ་ཤོར་བ་ཡིན་ཞེ་ན། འདོད་པ་ནི༌[^2434]སྤྱོད་པའི་ཉོན་མོངས་པ་སྤངས་པའི་ཕྱིར། ནན་གྱིས་མ་བཏང་བ་སྟེ་ནང་ཉིད་དུ་དེ་འགག་པའོ། །

[Block 3750]
བདག་ལ་གནོད་པ་ཞེས་བྱ་བ་ནི་ལུས་ལ་གནས་ཤིང་བདག་ལ་གནོད་པ་སྟེ། ཁྲོ་བའི་རང་བཞིན་དང་ལས་ལ་ཚིགས་བཅད་བདུན་གྱིས་བསྟན་པ་ལ། སྐྱེས་ན་གང་ཞིག་མི་མངོན་ལ། །ཞེས་བྱ་བའི་ཕྱེད་འོག་མས་ནི་བདག་ལ་གནོད་པའི་ལས་བསྟན་ཏོ། །
--- END BLOCKS ---
