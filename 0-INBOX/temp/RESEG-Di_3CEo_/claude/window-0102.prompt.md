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
[Block 3571]
གལ་ཏེ་ཡོན་ཏན་ཐོབ་པར་བྱ་བ་མ་ཐོབ་ན་མ་ཐོབ་པ་ལས་ཡོངས་སུ་ཉམས་པའོ། །

[Block 3572]
གལ་ཏེ་ཡོན་ཏན་ཐོབ་པ་མངོན་སུམ་དུ་མི་བྱེད་ན་ཉེ་བར་སྤྱད་པ་ལས་ཡོངས་སུ་ཉམས་པའོ། །

[Block 3573]
ཡོངས་སུ་ཉམས་པ་འདི་རྣམས་ལས་ནི།

[Block 3574 [VERSE]]
སྟོན༌[^1408]ལ་ཐ་མ་མི་གཡོ་ལ། །
བར་མ་འང༌[^1409]གཞན་ལ་རྣམ་གསུམ་མོ། །

[Block 3575]
བཅོམ་ལྡན་འདས་ལ་ནི་ཉེ་བར་སྤྱད་པ་ལས་ཡོངས་སུ་ཉམས་པ་ཁོ་ན་མངའི་གཞན་ནི༌[^1410]མི་མངའོ། །

[Block 3576]
མི་གཡོ་བའི་ཆོས་ཅན་ལ་ནི་དེ་དང་མ་ཐོབ་པ་ལས༌[^1411]ཡོངས་སུ་ཉམས་པ་ཡང་ཡོད་དོ། །

[Block 3577]
གང་ཟག་ཁྱད་པར་ཅན་གྱི་ཆོས་མ་ཐོབ་པའི་ཕྱིར་རོ། །

[Block 3578]
དགྲ་བཅོམ་པ་གཞན་ལ་ནི་ཐོབ་པ་ལས་ཡོངས་སུ་ཉམས་པ་ཡང༌[^1412]ཡོད་དོ། །

[Block 3579]
ཡང་གང་ཞིག་དགྲ་བཅོམ་པའི་འབྲས་བུ་ལས་ཡོངས་སུ་ཉམས་ན། ཅི་དེ་ཡང་སྐྱེ་འམ་ཞེ་ན། དེ་ལྟ་བུ་ནི་མེད་དེ། འདི་ལྟར། འབྲས་ལས་ཉམས་པ༌[^1413]འཆི་བ་མེད། །འབྲས་བུ༌[^1414]ལས་ཡོངས་སུ་ཉམས་པ་ནི་འགའ་ཡང་འཆི་བ་མེད་དེ། འབྲས་བུ་གང་ཞིག་ལས་ཡོངས་སུ་ཉམས་པ་ནི་འབྲས་བུ་དེ་ལ་གནས་པས། བྱ་བ་མ་ཡིན་དེ་མི་བྱེད། །ཡོངས་སུ་ཉམས་ཀྱང་འབྲས་བུ་དེ་དང་འགལ་བའི་བྱ་བ་མི་བྱེད་དོ། །

[Block 3580 [HEADING]]
#### དབང་པོ་འཕོ་བ། ^6-2-8-0

[Block 3581]
ཡང་དབང་པོ་རྣམས་འཕོ་བ་ལ་བར་ཆད་མེད་པ་དང་། རྣམ་པར་གྲོལ་བའི་ལམ་དུ་དག་སྐྱེ་ཞེ་ན།

[Block 3582 [VERSE]]
མི་གཡོ་རྣམ་གྲོལ་བར་ཆད་མེད། །
ལམ་དགུའོ་ཤིན་ཏུ་བསྟེན་ཕྱིར་རོ། །

[Block 3583]
རྟོགས་པའི་སྐལ་བ་ཅན་ཞིག་མི་གཡོ་བའི་རིགས་ཅན་རྟོགས་པར་བྱེད་པ་ན་བར་ཆད་མེད་པའི་ལམ་དགུ་དང་། རྣམ་པར་གྲོལ་བའི་ལམ་དགུ་སྐྱེ་སྟེ། དགྲ་བཅོམ་པ་ཉིད་ཐོབ་པ་བཞིན་ནོ། །

[Block 3584]
དེ་ལ་དབང་པོ་རྟུལ་པོའི་རིགས་དེ་ཤིན་ཏུ་གོམས་པར་བྱས་པའི་ཡིན་པས་འབད་པ༌[^1415]ཆུང་ངུས་བཟློག་པར་མི་ནུས་ཏེ། སློབ་པ་དང་མི་སློབ་པའི་ལམ་དག་གིས་བརྟན་པོར་བྱས་པའི་ཕྱིར་རོ། །

[Block 3585]
མཐོང་བས་ཐོབ་ལ་རེ་རེའོ། །

[Block 3586]
མཐོང་བས་ཐོབ་པ་རྟོགས་པར་བྱེད་ན་བར་ཆད་མེད་པ་དང་རྣམ་པར་གྲོལ་བའི་ལམ་རེ་རེ་སྐྱེའོ། །

[Block 3587]
བར་ཆད་མེད་པ་དང༌[^1416]རྣམ་པར་གྲོལ་བའི་ལམ་དེ་དག་ནི། ཟག་མེད། འཕགས་པ་རྣམས་ཀྱི་དབང་པོ་ཟག་པ་དང་བཅས་པའི་ལམ་གྱིས་འཕོ་བ་མེད་དོ། །

[Block 3588]
དབང་པོ་རྣམས་གང་དུ་འཕེལ་ཞེ་ན། མའི་ནང་དུ་འཕེལ། མི་རྣམས་ཀྱི་ནང་དུ་དབང་པོ་འཕོའོ། །

[Block 3589]
ཡང་གང་ཞིག་ས་གང་ལ་བརྟེན་ན་དབང་པོ་རྣམས་འཕོ་བར་བྱེད་ཅེ་ན། མི་སློབ་ས་དགུ་ལ་བརྟེན་ཏེ། །མི་ལྕོགས་པ་མེད་པ་དང་། བསམ་གཏན་ཁྱད་པར་ཅན་དང་། བསམ་གཏན་བཞི་དང་། གཟུགས་མེད་པ་གསུམ་ལའོ། །

[Block 3590]
སློབ་པ་དྲུག་ལ། གཟུགས་མེད་པ་གསུམ་མ་གཏོགས་སོ། །ཅིའི་ཕྱིར་ཞེ་ན། གང་གི་ཕྱིར།

[Block 3591 [VERSE]]
འཕེལ་བ་འབྲས་བུ་ཁྱད་པར་ཅན། །
བཏང་སྟེ་འབྲས་བུ་ཐོབ་པར་འགྱུར། །

[Block 3592]
དབང་པོ་རྣམས་འཕོ་བ་ན་དབང་པོ་རྟུལ་པོའི་ལམ་གྱི་འབྲས་བུ༌[^1417]ཁྱད་པར་ཅན་བཏང་སྟེ། དབང་པོ་རྣོན་པོའི་ལམ་གྱི་རིགས་ཀྱི་འབྲས་བུ་ཐོབ་པར་འགྱུར་ན། ཕྱིར་མི་འོང་བའི་འབྲས་བུ་གཟུགས་མེད་པས་བསྡུས་པ་ནི་མེད་དོ་ཞེས་བྱ་བ་འདི་ནི་གཏན་ཚིགས་ཡིན་ནོ། །

[Block 3593 [HEADING]]
#### དབང་པོ་རྣམ་དགུ་ཅན་དང་གང་ཟག་བདུན། ^6-2-9-0

[Block 3594]
དགྲ་བཅོམ་པ་འདི་དག་ཐམས་ཅད་ལ་དབང་པོའི་བྱེ་བྲག་གིས་དགུ་ཁོ་ན་ཡིན་ཏེ། ཇི་ལྟར་བྱས་ནས་ཤེ་ན།

[Block 3595 [VERSE]]
སངས་རྒྱས་གཉིས་དང་ཉན་ཐོས་བདུན། །
དེ་དགུ་དབང་པོ་རྣམ་དགུ་ཅན། །

[Block 3596]
དེ་ལ་ཉན་ཐོས་བདུན་ནི་ཡོངས་སུ་ཉམས་པའི་ཆོས་ཅན་ལ་སོགས་པ་ལྔ་དང་། མི་གཡོ་བའི་ཆོས་ཅན་རྣམ་པ་གཉིས་ཏེ། སྦྱངས་པ་ལས་གྱུར་པ་དང་།

[Block 3597]
དང་པོ་ནས་དེའི་རིགས་ཅན་ཡིན་ནོ། །

[Block 3598]
མི་གཡོ་བའི་བྱེ་བྲག་ཁོ་ན་རང་སངས་རྒྱས་དང་། སངས་རྒྱས་སོ། །

[Block 3599]
དེ་ལྟ་ན་དེ་དག་ནི་ཆུང་ངུའི་ཆུང་ངུ་ལ་སོགས་པ་རྣམས༌[^1418]དབང་པོ༌[^1419]དགུའི་བྱེ་བྲག་གིས་གང་ཟག་དགུ་ཡིན་ནོ། །

[Block 3600]
སློབ་པ་དང་མི་སློབ་པ་བསྡུས་པའི་ཕྱིར་ཡང་འཕགས་པའི་གང་ཟག་རྣམས་ནི་ཐམས་ཅད་དུ་བདུན་ཡིན་ཏེ། དད་པས་རྗེས་སུ་འབྲང་བ་དང་། ཆོས་ཀྱི་རྗེས་སུ་འབྲང་བ་དང་། དད་པས་མོས་པ་དང་མཐོང་བས་ཐོབ་པ་དང་། ལུས་ཀྱིས་མངོན་སུམ་དུ་བྱེད་པ་དང་། ཤེས་རབ་ཀྱིས་རྣམ་པར་གྲོལ་བ་དང་། གཉིས་ཀའི་ཆ་ལས་རྣམ་པར་གྲོལ་བའོ། །

[Block 3601]
གང་ཟག་བདུན་པོ། །དེ་དག་ཀྱང་། སྦྱོར་བ་དང་། དབང་པོ་སྙོམས་འཇུག་རྣམ་གྲོལ་དང་། །གཉིས་ཀ་བྱས་པའོ། །

[Block 3602]
སྦྱོར་བ་ལས་ནི་དད་པ་དང་། ཆོས་ཀྱི་རྗེས་སུ་འབྲང་བ་དག་སྟེ།

[Block 3603]
དང་པོ་ཉིད་ནས་གཞན་གྱི་དྲིང་འཇོག་པ་དང་། ཆོས་ཀྱི༌[^1420]རྗེས་སུ་འབྲང་བ་དག་གིས་དོན་རྣམས་ལ་སྦྱོར་བའི་ཕྱིར་རོ། །

[Block 3604]
དབང་པོ་ལས་ནི་དད་པས་མོས་པ་དང་། མཐོང་བས་ཐོབ་པ་དག༌[^1421]སྟེ། དབང་པོ་རྟུལ་པོ་དང་རྣོན་པོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3605]
སྙོམས་པར་འཇུག་པ་ལས་ནི་ལུས་ཀྱིས་མངོན་དུ་བྱེད་པ་སྟེ། །འགོག་པའི་སྙོམས་པར་འཇུག་པ་མངོན་དུ་བྱེད་པའི་ཕྱིར་རོ། །

[Block 3606]
རྣམ་པར་གྲོལ་བ་ལས་ནི་ཤེས་རབ་ཀྱིས་རྣམ་པར་གྲོལ་བའོ། །

[Block 3607]
སྙོམས་པར་འཇུག་པ༌[^1422]རྣམ་པར་གྲོལ་བ་ལས་ནི་གཉིས་ཀའི་ཆ་ལས་རྣམ་པར་གྲོལ་བའོ། །

[Block 3608]
མིང་གི༌[^1423]སྒོ་ནས་ནི་གང་ཟག་དེ་བདུན་ཡིན་ནོ། །

[Block 3609]
དེ་དག་དྲུག །

[Block 3610 [VERSE]]
རྫས་སུ་ནི་དེ་དག་དྲུག་ཡིན་ནོ། །
འདི་ལྟར་ལམ་གསུམ་ལ་གཉིས་གཉིས། །
--- END BLOCKS ---
