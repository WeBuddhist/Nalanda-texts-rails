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
[Block 2591]
ཡོན་ཏན་གྱི་ཁྱད་པར་ལས་ནི་ཇི་ལྟར་ཚུལ་ཁྲིམས་དང་ལྡན་པ་ལ་བྱིན་ན་རྣམ་པར་སྨིན་པ་འབུམ་འགྱུར་རོ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 2592]
སྦྱིན་པ་ཐམས་ཅད་ཀྱི་ནང་ན། མཆོག་ནི་གྲོལ་བས་གྲོལ་བ་ལའང་། །འདོད་ཆགས་དང་བྲལ་བས་འདོད་ཆགས་དང་བྲལ་བ་ལ་བྱིན་པ་གང་ཡིན་པའོ། །

[Block 2593]
བྱང་ཆུབ་སེམས་དཔའ་ཡིས། གང་བྱང་ཆུབ་སེམས་དཔའ་སེམས་ཅན་ཐམས་ཅད་ལ་ཕན་པར་བྱ་བའི་ཕྱིར་སྦྱིན་པ་དེ་ཡང་མཆོག་ཡིན་ནོ། །

[Block 2594]
དེ་མ་གཏོགས་པ་བཅོམ་ལྡན་འདས་ཀྱིས་སྦྱིན་པ་བརྒྱད་གསུངས་པ་དེ་དག་གི་ནང་ན་ནི། བརྒྱད་པ། མཆོག་ཡིན་ནོ་ཞེས་སྦྱར་རོ། །

[Block 2595]
བརྒྱད་གང་ཞེ་ན། ཉེ་བ་ལ་སྦྱིན་པ་དང་། འཇིགས་པས་སྦྱིན་པ་དང་། བདག་ལ་བྱིན་པས་སྦྱིན་པ་དང་། བདག་ལ་སྦྱིན་པར་འགྱུར་བས་སྦྱིན་པ་དང་། སྔོན་བདག་གི་ཕ་དང་མེས་པོ་དག་གིས་བྱིན་པས་སྦྱིན་པ་དང་། མཐོ་རིས་ཀྱི་དོན་དུ་སྦྱིན་པ་དང་། གྲགས་པའི་དོན་དུ་སྦྱིན་པ་དང་། སེམས་ཀྱི་རྒྱན༌[^1036]དང་། སེམས་ཀྱི་ཡོ་བྱད་དང་། རྣལ་འབྱོར་གྱི་ཚོགས་དང་། དོན་གྱི་མཆོག་གི་དོན་དུ་སྦྱིན་པ་བྱིན་པའོ། །

[Block 2596]
དེ་དག་ལས་ཐ་མ་ནི་མཆོག་ཡིན་ནོ། །

[Block 2597]
བཅོམ་ལྡན་འདས་ཀྱིས་རྒྱུན་དུ་ཞུགས་པའི་འབྲས་བུ་ལ་ཞུགས་པ་དང་། རྒྱུན་དུ་ཞུགས་པའི་འབྲས་བུ་ལ་གནས་པ་ལ་བྱིན་པའི་རྣམ་པར་སྨིན་པ་གཞལ་དུ་མེད་པར་གསུངས་མོད་ཀྱི། གཞན་ཡང་།

[Block 2598 [VERSE]]
འཕགས་པ་མིན་ཡང་ཕ་མ་དང་། །
ནད་པ་དང་ནི་ཆོས་སྨྲ་དང་། །
སྐྱེ་མཐའི་བྱང་ཆུབ་སེམས་དཔའ་ལ། །
ཡོན་ནི་གཞལ་དུ་མེད་པ་ཡིན། །

[Block 2599]
ལྔ་པོ་འདི་དག་ལ་ནི་སོ་སོའི༌[^1037]སྐྱེ་བོར་གྱུར་པ་ཡིན་ཡང་འབྲས་བུའི་སྒོ་ནས་ཡོན་གནས་གཞལ་དུ་མེད་པ་ཡིན་ནོ། །

[Block 2600]
ལས་རྣམས་ཀྱི་ལྕི་བ་དང་ཡང་བ་ཉིད་ཤེས་པར་འདོད་པས་རྒྱུ་དྲུག་ཤེས་པར་བྱ་སྟེ། འདི་ལྟ་སྟེ།

[Block 2601 [VERSE]]
མཇུག་དང་ཞིང་དང་གཞི་དང་ནི། །
སྦྱོར་དང་སེམས་པ༌[^1038]བསམ་པ་སྟེ། །
དེ་དག་ཆུང་དང་ཆེ་བ་ལས། །
ལས་ཀྱང་ཆུང་དང་ཆེ་བ་ཉིད། །

[Block 2602]
མཇུག་ཅེས་བྱ་བ་ནི་བྱས་པའི་རྗེས་ལ་ཡང་བྱེད་པ་གང་ཡིན་པའོ། །

[Block 2603]
ཞིང་ཞེས་བྱ་བ་ནི་ཕན་པ་དང་གནོད་པ་དག་བྱེད་པའོ། །

[Block 2604]
གཞི་ནི་ལས་ཀྱི་ལམ་མོ། །

[Block 2605]
སྦྱོར་བ་ནི་དེའི་དོན་དུ་ལུས་དང་ངག་གི་ལས་སོ། །

[Block 2606]
སེམས་པ་ནི་ངག་གི་ལས་ཀྱི་ལམ་མཐར་ཕྱིན་པར་བྱེད་པའོ། །

[Block 2607]
བསམ་པ་ནི་དེ་དག་ལས་དེ་དང་འདི་དག་ཅིག༌[^1039]ནི་བྱའོ། །

[Block 2608]
དེ་དང་འདི་ལྟ་བུ་ཞིག་ནི་ཕྱིས་བྱའོ་སྙམ་དུ་སེམས་པའོ། །

[Block 2609]
ལས་བྱས་པ་དང་། བསགས་པ་ནི་ཇི་ལྟ་བུ་ཞེ་ན།

[Block 2610 [VERSE]]
བསམས་བཞིན་པ་དང་རྫོགས་པ་དང་། །
མི་འགྱོད་གཉེན་པོ་མེད་པ་དང་། །
འཁོར་དང་རྣམ་པར་སྨིན་པ་ལས། །
བསགས་པའི་ལས་ཞེས་བྱ་བ་ཡིན། །

[Block 2611]
ཆེད་དུ་བསམས་ནས་བྱས་པ་ཡིན་གྱི་བློ་སྔོན་དུ་མ་བཏང་བ་ཡང་མ་ཡིན་པ་བབ་ཅོལ་དུ་བྱས་པ་ཡང་མ་ཡིན་ནོ། །

[Block 2612]
རྫོགས་པ་ནི་ཁ་ཅིག་ནི་ཉེས་པར་སྤྱད་པ་གཅིག་གིས་ངན་སོང་དུ་འགྲོ་བ།[^1040] ཁ་ཅིག་ནི་གསུམ་གྱི་བར་གྱིས་འགྲོ་བའོ། །

[Block 2613]
དེ་གང་ཞིག་གིས་ཇི་ཙམ་གྱིས་འགྲོ་བ་དེ་རྫོགས་ན༌[^1041]བསགས་པ་ཡིན་ནོ། །

[Block 2614]
མི་འགྱོད་པ་དང་གཉེན་པོ་མེད་པ་ནི་ཡིད་ལ་བཅགས་པ་མེད་པ་དང་། གཉེན་པོ་མེད་པ་ཡིན་ནོ། །

[Block 2615]
འཁོར་ལས་ནི་མི་དགེ་བ་ལ་འཁོར་བ་ཡང་མི་དགེ་བ་ཡིན་ནོ། །

[Block 2616]
རྣམ་པར་སྨིན་པ་ལས་ནི་རྣམ་པར་སྨིན་པ་འབྱིན་པར་ངེས་པ་ཡིན་ནོ། །

[Block 2617]
དེ་བཞིན་དུ་དགེ་བ་ལ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 2618]
དེ་ལས་གཞན་དུ་བྱས་པའི་ལས་ནི་མ་བསགས་པ་ཡིན་ནོ། །

[Block 2619]
འདོད་ཆགས་དང་བཅས་པས་མཆོད་རྟེན་ལ་སྦྱིན་པ་བྱིན་པ་ནི་བདག་གི་དོན་དུའོ་ཞེས་བཤད་པ་དེ་ལ་ལོངས་སྤྱོད་པ་དང་ལེན་པ་པོ་མེད༌[^1042]ན་བསོད་ནམས་ཇི་ལྟར་འབྱུང་ཞེ་ན།

[Block 2620 [VERSE]]
མཆོད་རྟེན་ལ་བཏང་རྒྱུས་བྱུང་བའི། །
བསོད་ནམས་ལེན་མེད་བྱམས་སོགས་བཞིན། །

[Block 2621]
ཇི་ལྟར་བྱམས་པ་ལ་སོགས་པ་ལ༌[^1043]ལེན་པར་བྱེད་པའམ་གཞན་ལ་ཕན་འདོགས་པ་མེད་ཀྱང་རང་གི་སེམས་ཀྱི་མཐུས་བསོད་ནམས་སུ་གྱུར་པ་དེ་བཞིན་དུ། ཡོན་ཏན་དང་ལྡན་པ་འདས་ཀྱང་དེ་ལ་དད་པར་བྱས་པས་རང་གི་སེམས་ལ་བསོད་ནམས་སུ་འགྱུར་རོ། །

[Block 2622]
གལ་ཏེ་ཞིང་བཟང་པོ་ལ་སྦྱིན་པར་བྱ་བའི་འབྲས་བུ་ས་བོན་ཡིད་དུ་འོང་བ་ཅན་ཡིན་ན། འོ་ན་ནི་ཞིང་ངན་པ་ལ་བྱིན་ན་འབྲས་བུ་ཡིད་དུ་མི་འོང་བར་འགྱུར་ཞེ་ན།

[Block 2623 [VERSE]]
རྒྱུན་ལས༌[^1044]འབྲས་བུ་མི་འཁྲུལ་ཕྱིར། །
ངན་པའི་ཞིང་ལའང་འབྲས་ཡིད་འོང་། །

[Block 2624]
ཞིང་ངན་པ་ལ་ཡང༌[^1045]ས་བོན་ལས་འབྲས་བུ་མི་འཁྲུལ་བ་མཐོང་སྟེ། རྒྱུན་གྱི་ས་བོན་ལས་ནི་རྒྱུན་གྱི་འབྲས་བུ་མངར་བ་སྐྱེ་བ་དེ་བཞིན་དུ་ཞིང་ངན་པ་ལ་ཡང་གཞན་ལ་ཕན་པའི་ལྷག་པའི་བསམ་པ་ལ་ཞུགས་པའི་སྦྱིན་པའི་ས་བོན་གྱི་འབྲས་བུ་ཡང༌[^1046]ཡིད་དུ་འོང་བ་ཁོ་ན་འགྲུབ་ཀྱི་ཡིད་དུ་མི་འོང་བ་ནི་མ་ཡིན་ནོ། །

[Block 2625 [HEADING]]
##### ཚུལ་ཁྲིམས། ^4-3-14-2-0

[Block 2626]
སྦྱིན་པ་ལས་བྱུང་བ་བཤད་ནས། ཚུལ་ཁྲིམས་ལས་བྱུང་བ་བརྗོད་པར་བྱ་སྟེ།

[Block 2627 [VERSE]]
འཆལ་པའི་ཚུལ་ཁྲིམས་མི་དགེའི་གཟུགས། །
དེ་སྤོང་ཚུལ་ཁྲིམས་རྣམ་གཉིས་སོ། །

[Block 2628]
རྣམ་པར་རིག་བྱེད་གང་སྤོང་བར་བྱེད་པ་དང་། རྣམ་པར་རིག་བྱེད་མ་ཡིན་པས་སྤོང་བ་གང་ཡིན་པའོ། །

[Block 2629]
ཚུལ་ཁྲིམས་ནི་འཆལ་པའི་ཚུལ་ཁྲིམས་ཁོ་ན་སྤོང་བ་འབའ་ཞིག་མ་ཡིན་གྱི། འོན་ཀྱང་སངས་རྒྱས་ཀྱིས་ནི་བཅད་པ༌[^1047]ཡང་། རང་བཞིན་གྱི༌[^1048]འཆལ་བའི་ཚུལ་ཁྲིམས་མ་ཡིན་པ་ཡང་བཅོམ་ལྡན་འདས་ཀྱིས་བཅད་པ་དུས་མ་ཡིན་པའི་ཟས་ལ་སོགས་པ་གང་དག་ཡིན་པ་དེ་དག་སྤོང་བ་རྣམ་པ་གཉིས་ཀྱང་ཚུལ་ཁྲིམས་ཡིན་ནོ། །

[Block 2630]
ཚུལ་ཁྲིམས་མདོར་བཤད་ཟིན་ཏོ། །
--- END BLOCKS ---
