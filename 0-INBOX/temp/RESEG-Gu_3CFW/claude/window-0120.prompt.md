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
[Block 4201]
དཔལ་ལྡན་རྒྱལ་ཆེན་ཐམས་ཅད་ཀྱིས།[^4278] །རྒྱལ་སྲིད་བྱེད་དུས་འདི་བྱས་སོ། །

[Block 4202]
འདུལ་བ་མདོའི་འགྲེལ་པ་བཅོམ་བརླག་མ་ཞེས་བྱ་བ། ཡུལ་བཅོམ་བརླག་གི་འཕགས་པ་གཞི༌[^4279]ཐམས་ཅད་ཡོད་པར་སྨྲ་བའི་རྩོད་པ་པ་ཆེན་པོ་རྣམས་ཀྱི་ཁྱུ་མཆོག་བསྟན་བཅོས་དུ་མ་མཛད་པ་གཞུང་འབུམ་ཕྲག་བཅོ་བརྒྱད་ལ་ཁ་ཏོན་མཛད་པའི་སློབ་དཔོན་ཡོན་ཏན་འོད་ཀྱིས་མཛད་པ་རྫོགས་སོ།། །།

[Block 4203 [HEADING]]
### འགྱུར་བྱང། ^b-2-0

[Block 4204]
འདི་ནི་དཔལ་ས་ཉིའི༌[^4280]གཙུག་ལག་ཁང་ཆེན་པོར་རྗེ་བཙུན་དམ་པ་རྒྱལ་པོ་ཆེན་པོའི་ཡང་ཆེན་པོ་དབང་ཕྱུག་དམ་པ་དཔལ་ཚུལ་ཁྲིམས་ཉི་མའི་ལྷ་རབ་ཏུ་རྒྱས་པར་གྱུར་པ་རྣམ་པར་རྒྱལ་བའི་རྒྱལ་སྲིད་ཀྱི་ལོ་ལ་བྲིས་པ་ཡིན་ནོ། །

[Block 4205]
གང་འདི་འདུལ་བའི་སྡེ་སྣོད་སྟོང་ཕྲག་ཉི་ཤུ་རྩ་ལྔ་ལས་ལྷག་པའི་འབུམ་ཕྲག་གཅིག་གི་དོན་གསལ་བར་བྱེད་པ་རང་གི་རྣམ་པར་བཤད་པ་ཞེས་བྱ་བ་ལོ་ཙཱ་བ་ཤཱཀྱའི་དགེ་སློང་ཚུལ་ཁྲིམས་འབྱུང་གནས༌[^4281]ཀྱིས་བསྒྱུར་བའི་བསོད་ནམས་གང་དེས་མཁན་པོ་དང་སློབ་དཔོན་དང་ཕ་དང་མ་སྔོན་དུ་འགྲོ་བར་བྱས་པའི་མ་ལུས་པའི་སེམས་ཅན་གྱི་ཕུང་པོས་བླ་ན་མེད་པའི་ཡེ་ཤེས་ཀྱི་འབྲས་བུ་ཐོབ་པར་གྱུར་ཅིག། །

[Block 4206 [VERSE]]
འབུམ་གྱི་ཚད་ལྡན་འདུལ་བའི་རྒྱ་མཚོ་ཆེན་པོ་དག །
སྟོན་པས་གསུངས་པ་ལས་ནི་མན་ངག་ཚུལ་གྱིས་འདིར། །
གཟིངས༌[^4282]ནི་ཡང་དག་ཐོབ་ནས་བླ་མའི་དྲིན་གྱིས་ནི། །
གང་ཞིག་རིན་ཆེན་མདོ་རྣམས་ཡང་དག་མཛད་པར་གྱུར། །

[Block 4207 [VERSE]]
ས་གསུམ་བརྙེས༌[^4283]ནས་དཔལ་ལྡན་རྒྱལ་བ་རྣམས་ཀྱི༌[^4284]སྲས། །
ཡོན་ཏན་འོད་ཅེས་བྱ་བ་ཡོན་ཏན་རྣམས་ཀྱི་གཙོས། །
མདོ་ཡི་བཤད་པ་བདུད་རྩིའི་རོ་ཡིས་ཡང་དག་པར། །
རང་གིས་མཛད་འདི་འགྲོ་བ་ལ་ནི་ཕན་འདོད་ཅིང་། །

[Block 4208 [VERSE]]
དགེ་སློང་ཕ་མ་ལ་སོགས་འདུལ་བའི་སྣོད་གྱུར་པའི། །
འཇིག་རྟེན་ཚིམ་པར་མཛད་ཅིང་གྲགས་པས་ཀུན་ལ་ཁྱབ། །

[Block 4209]
[^4285]རྒྱལ་བའི་ཡུམ་ལ་ལེགས་པའི་བློ་མངའ་འཕགས་པ་ཐོགས་མེད་བཞིན་དུ་དྲི་མེད་དོན་ཤེས་ཁྱོད། །ཕྱོགས་ཀྱི་གླང་པོའི་བསྡུས་དོན་འདི་ལ་ཡང་ནི་མི་མཉམ་དེ་དང་འདྲ་བར་ཁྱོད་ཀྱིས་གཟུང་།[^4286] །སློབ་དཔོན་ཆོས་མཆོག་བཞིན་དུ་ཚད་མ་ལ་མཁས་ཁྱོད་ཀྱིས་ཕྱི་རོལ་དོན་གྲུབ་ལ༌[^4287]སྟེར་བ། །སློབ་དཔོན་དབྱིག་གཉེན་ལྟ་བུར་སེམས་ཅན་རྣམས་ལ་ཁྱོད་ནི་དོན་གཉེར་ལ་དགའ་མཛོད་ནི་སྟེར། །དཔལ་ལྡན་བློ་གྲོས་འབྱུང་གནས་ཞེས་བྱ་བཅོམ་ལྡན་འདས་ཀྱི༌[^4288]བསྟན་པའི་བསླབ་འཛིན་ནི། །གསོལ་དང་བཞི་ཡི་ལས་ཀྱི་ཆོ་གས་དགེ་སློང་རྣམ་དག་བསྙེན་རྫོགས་མཆོག་ནི་ཐོབ་གྱུར་ནས། །གཞན༌[^4289]རྣམས་ལ་ཡང་རུང༌[^4290]དབང་ཐོབ་ནས་རང་གིས༌[^4291]རབ་ཏུ་དབྱུང་ཕྱིར་མཁན་པོ་མཛད་པ་སྟེ། །རང་གི་རྣམ་བཤད་སྒྱུར་བར༌[^4292]བྱེད་པའི་སྦྱིན་བདག་དེ་ནི་ཡུན་རིང་པོར་ནི་གནས་གྱུར་ཅིག །

[Block 4210 [VERSE]]
བསྒྱུར་བའི་ཡོན་བདག་ཉིད་མཛད་པས། །
ཁྱེད༌[^4293]ཀྱིས་དགེ་བ་གང་ཐོབ་པ། །
དེས་ནི་ཚོགས་གཉིས་མྱུར་རྫོགས་ནས། །
ཁྱོད་ཉིད་སངས་རྒྱས་ཉིད་གྱུར་ཅིག།། །།

[Block 4211]
རྒྱ་གར་གྱི་མཁན་པོ་པཎྜི་ཏ་ཨ་ལངྐ་ར་དེ་བ་དང་། ཞུ་ཆེན་གྱི་ལོ་ཙཱ་བ་ཤཱཀྱའི་དགེ་སློང་ཚུལ་ཁྲིམས་འབྱུང་གནས་སྦས་པ་གཉིས་ཀྱིས་དཔལ་སྒྱེའུ་རིའི་རྩ་ཆོས་སྐོར་དབེན་ཚའི་གཙུག་ལག་ཁང་དུ་བསྒྱུར། འདི་ལ་ཤློ་ཀ༌[^4294]སྟོང་ཕྲག་བཅུ་བཞི་ཡོད་དོ།། །།

[Block 4212]
[^4295]
--- END BLOCKS ---
