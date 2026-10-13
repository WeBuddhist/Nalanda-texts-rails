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
[Block 4971]
འདིའི་དོན་ནི་བཤད་པའི་རྒྱུད་ལས་ཞེས་པ་ནི་རྡོ་རྗེ་ཕྲེང་བའི་རྒྱུད་ལས་སོ། །

[Block 4972 [VERSE]]
ཨོཾ་ནི་དང་པོར་ཤེས་པར་བྱ། །
ཞེས་པ་རྣམ་པར་སྣང་མཛད་དེ།
དེ་ནི་ཨོཾ་ལས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 4973]
དྷརྨ་ཞེས་བྱ་གཉིས་པའོ། །

[Block 4974]
ཞེས་པ་ནི་ཆོས་ཀྱི་ཕུང་པོ་བརྒྱད་ཁྲི་བཞི་སྟོང་གི་རྣམ་པར་དག་པའི་རང་བཞིན་གྱི་རྡོ་རྗེ་ཆོས་ཏེ་སྣང་བ་མཐའ་ཡས་སོ། །

[Block 4975]
དྷཱ་ཏུ་ཞེས་བྱ་གསུམ་པར་བཤད། །ཅེས་པ་ནི་ཆོས་ཐམས་ཅད་ཀྱི་རང་བཞིན་ཆོས་ཀྱི་དབྱིངས་རྣམ་པར་དག་པའི་ངོ་བོ་ནི་མི་བསྐྱོད་པའོ། །

[Block 4976]
སྭ་བྷཱ་བར་གྲགས་བཞི་པའོ། །ཞེས་པ་ནི་ནམ་མཁའི་ཁམས་ཀྱི་རང་བཞིན་རིན་ཆེན་འབྱུང་ལྡན་ནོ། །

[Block 4977]
ཨཱཏྨ་ཀོ྅་ནི་ལྔ་པ་ཡིན། །ཞེས་པ་ནི་ཐམས་ཅད་ཀྱི་བདག་ཉིད་ལས་ཐམས་ཅད་པ་སྟེ་དོན་ཡོད་པར་གྲུབ་པའོ། །

[Block 4978]
ཨ་ཧཾ་དུ་གྱུར་དྲུག་པར་འདོད། །ཅེས་པ་ནི་དེ་བཞིན་གཤེགས་པ་ལྔ་ཉེ་བར་སྡུད་པར་བྱེད་པའི་རྣམ་པ་ཅན་ཏེ་རྡོ་རྗེ་འཆང་ཆེན་པོའོ་ཞེས་པའི་དོན་ཏོ། །

[Block 4979]
སྔགས་ནི་དབང་པོ་ཐམས་ཅད་དང་རྣམ་པར་ཤེས་པ་རྣམ་པར་དག་པའི་མཚན་ཉིད་ཅན་གྱི་བསྒོམ་པའི༌[^2941]རྣམ་པའོ། །

[Block 4980]
འདི་བརྗོད་ནས་ཞེས་པ་ནི་དེ་བཞིན་གཤེགས་པ་དྲུག་གི་མོས་པ་བྱས་ནས་སོ། །

[Block 4981]
རྒྱུད་ཕྱི་མ་ལས་ཀྱང་།

[Block 4982 [VERSE]]
དབང་པོ་དང་ནི་ཡུལ་གྱིས་ཡིད། །
རྟེན་ཏེ་བྱུང་བ་གང་ཡིན་པ། །
དེ་ནི་མིན༌[^2942]ཞེས་བཤད་པ་སྟེ། །
ཏྲ་ནི་སྐྱོབ་པའི་དོན་ཡིན་ནོ། །

[Block 4983]
ཞེས་འབྱུང་ངོ་། །དེའི་འོག་ཏུ་ཞེས་པ་ནི་དེ་དང་འདྲ་བའི་ལྷག་པར་མོས་པ་བྱས་ནས་སོ། །

[Block 4984]
སྒོམ་པའི་བདག་ཉིད་ཅན་གྱིས་ཞེས་པ་ནི་རྫོགས་པའི་རིམ་པའི་རྣལ་འབྱོར་པས་སོ། །

[Block 4985]
བསྒོམ་ཞེས་པ་ནི་ཟུང་དུ་འཇུག་པའི་རིམ་པའི་ཏིང་ངེ་འཛིན་གྱི་དེ་བཞིན་གཤེགས་པ་དྲུག་གི་ང་རྒྱལ་བྱ་ཞེས༌[^2943]བྱ་བའི་དོན་ཏོ། །

[Block 4986]
ངེས་པའི་དོན་ནི་རྫོགས་པའི་རིམ་པ་སོ་སོར་བསྟན་པའི་ཕྱིར་རོ། །

[Block 4987]
དེ་ལྟར་ལེའུ་ནས་བརྩམས་ཏེ་ཡོངས་སུ་དག་པ་དང་ཡོངས་སུ་མ་དག་པའི་ལྷའི་སྐུའི་དབྱེ་བས་རིམ་པ༌[^2944]གཉིས་བསྟན་ཏོ། །

[Block 4988]
བསྐྱེད་པའི་རིམ་པའི་ཕྱོགས་སུ་དང་པོའི་སྦྱོར་བ་དང་དཀྱིལ་འཁོར་རྒྱལ་བ་མཆོག་གི་ཏིང་ངེ་འཛིན་དག་གིས་རྣམ་པར་སྣང་མཛད་ལ་སོགས་པ་དེ་བཞིན་གཤེགས་པ་ལྔ་དང་དེའི་ལྷའི་དཀྱིལ་འཁོར་བསྟན་ཏོ། །

[Block 4989]
རྫོགས་པའི་རིམ་པའི་ཕྱོགས་སུ་ཡང་རྡོ་རྗེ་བཟླས་པ་ལ་སོགས་པའི་རིམ་པས་ཟུང་དུ་འཇུག་པའི་བར་དུ་རྡོ་རྗེ་འཆང་ཆེན་པོའི་སྐུ་རྫོགས་པར་བསྟན་ཏོ། །

[Block 4990 [HEADING]]
### ཕྲ་མོའི་རྣལ་འབྱོར་རྣམ་པ་གསུམ། ^3-2-0

[Block 4991]
ད་ནི་ཞེས་པ་ནི་བསྐྱེད་པའི་རིམ་པའི་ཡན་ལག་ཏུ་གྱུར་པའི་ལས་ཀྱི་རྒྱལ་བ་མཆོག་གི་ཕྱོགས་གཅིག་ཕྲ་མོའི་རྣལ་འབྱོར་ཞེས་བྱ་བ་ཡན་ལག་དང་པོ་བསྟན་པར་བྱ་བ་ཡིན་ནོ། །

[Block 4992]
རང་གི་སེམས་བརྟན་པར་བྱ་བའི་ཕྱིར་ཞེས་པ་ནི་རྡུལ་ཕྲ་རབ་དང་ཤིན་ཏུ་རགས་པའི་བསྒོམ་པའི་མཐའི་བར་དུ་སེམས་དབང་དུ་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 4993]
དགོངས་པ་ནི་ས་འོག་བདུན་གྱི་བར་དུ་ཁྱབ་པར་བྱེད་པའི་ཞབས་ཀྱི་པདྨ་དང་། སྲིད་པའི་རྩེ་མོའི་བར་དུ་སྤྱི་བོས་ཁྱབ་པ༌[^2945]ཕྱག་རྣམས་ཀྱིས་ཕྱོགས་བཅུ་དང་ནམ་མཁའི་དཀྱིལ་ཁྱབ་པར་བྱེད་པའི་རྡོ་རྗེ་འཆང་ཆེན་པོ་ལ་སོགས་པའི་ལྷའི་སྐུ་སྣ་ཚོགས་པའི་རང་བཞིན་ཡིན་ནོ་ཞེས་གང་གི་ཚེ་རྣལ་འབྱོར་པས་བསྒོམས་ན་དེའི་ཚེ་རང་གི་སེམས་བརྟན་པར་འགྱུར་རོ། །

[Block 4994]
གང་གི་ཚེ་ཡུངས་ཀར་གྱི་འབྲུའི་ཚད་ཙམ་གྱི་ཕྲ་བ་བརྟན་པ་དང་གཡོ་བའི་ཁམས་གསུམ་གྱི་རང་བཞིན་སྐྲའི་རྩེ་མོའི་བརྒྱ་སྟོང་གི་ཆའི་ཚད་ཙམ་ཐིག་ལེའི་བདག་ཉིད་བསྒོམས༌[^2946]ན་དེའི་ཚེ་རང་གི་སེམས་དབང་དུ་འགྱུར་རོ། །

[Block 4995]
འདིར་ནི་རྡུལ་ཕྲ་རབ་བསྒོམ་པའི་གནས་སྐབས་ཡིན་ཏེ། ཤིན་ཏུ་རགས་པའི་བསྒོམ་པ་ནི་སྔར་བཤད་པའི་ཕྱིར་རོ། །

[Block 4996]
ཕྲ་མོའི༌[^2947]རྣལ་འབྱོར་རྣམ་པ་གསུམ་བསྒོམ་པ་གསུངས་ཏེ་ཞེས་པ་ནི་བསྐྱེད་པའི་རིམ་པའི་རྣལ་འབྱོར་པའི་གཅིག་དང་གཞན་མ་གཉིས་རྫོགས་པའི་རིམ་པའི་རྣལ་འབྱོར་པའོ།[^2948] །

[Block 4997]
འཆད་པར་འགྱུར་བའི་གསུམ་པ་ལ་ཡང་རྫོགས་པའི་རིམ་པའི་རྣལ་འབྱོར་པ་ཉིད་ཀྱིའོ། །

[Block 4998]
བསྡུས་པའི་དོན་ནི་འདི་ཡིན་ཏེ། སྤྱིའི་དོན་གྱི་ཕྱོགས་སུ་བསྐྱེད་པའི་རིམ་པའི་རྣལ་འབྱོར་པས་ཕྲ་མོའི་རྣལ་འབྱོར་བསྒོམ་པ་དང་། སྦས་པ་དང་མཐར་ཐུག་པའི་བཤད་པའི་ཕྱོགས་དང་འོག་ནས་བཤད་པའི་ངེས་པའི་དོན་གྱི་ཕྱོགས་སུ་ཡང་རྫོགས་པའི་རིམ་པའི་རྣལ་འབྱོར་པས་ཕྲ་མོའི་རྣལ་འབྱོར་བསྒོམ་པའོ། །

[Block 4999]
དེ་ལྟར་བསྐྱེད་པའི་རིམ་པ་དང་རྫོགས་པའི་རིམ་པའི་རྣལ་འབྱོར་པ་དག་ལ་ཕྲ་མོའི་རྣལ་འབྱོར་རྣམ་པ་གསུམ་གྱི་བསྒོམ་པ་བསྟན་ཏེ། འདོད་ཆགས་དང་ཞེ་སྡང་དང་གཏི་མུག་གི་རིགས་ཅན་གྱི་རྣལ་འབྱོར་པའི་དབྱེ་བས་སོ། །

[Block 5000 [HEADING]]
#### དང་པོ་འདོད་ཆགས་ཀྱི་རིགས་ཅན་གྱི་རྣལ་འབྱོར་པའི་ཕྲ་མོའི་རྣལ་འབྱོར། ^3-2-1-0

[Block 5001]
དེ་ལ་དང་པོ་བཤད་པའི་ཕྱིར། །རྡོ་རྗེ་ལ་སོགས་པའི་ཕྱག་མཚན་ཏེ་ཞེས་པ་ནི་རྡོ་རྗེ་དང་འཁོར་ལོ་དང་རིན་པོ་ཆེ་དང་པདྨ་དང་རལ་གྲི་ལ་སོགས་པའོ། །

[Block 5002]
རིན་ཆེན་ལྟར་རིན་ཆེ་བ་ཉིད་དོ་ཞེས་པ་ནི་མཐའ་ཡས་པའི་འཇིག་རྟེན་གྱི་ཁམས་ལ་གནས་པའི་སེམས་ཅན་རྣམས་ཀྱི་བསམ་པ་ཐམས་ཅད་ཅིག་ཅར་དུ་རྫོགས་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 5003]
རིགས་ལས་བྱུང་བས༌[^2949]སོ་ཞེས་པ་ནི་རིགས་ལྔའི་འབྲེལ་པ་དང་ལྡན་པའི་དེ་བཞིན་གཤེགས་པ་ལ་སོགས་པ་སྤྲོ་བའི་རྒྱུ་སྟེ་ཐིག་ལེའི༌[^2950]ཁྱད་པར་རོ། །

[Block 5004]
དེ་ནི་ཡུངས་ཀར་གྱི་འབྲུའི་ཚད་ཙམ་ཞེས་པ་ནི་ནས་དང་ཙ་ན་ཀ་ལ་སོགས་པའི་འབྲུའི་ཚད་ཙམ་ཡང་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 5005]
སྣའི་རྩེ་མོར་ཞེས་པ་ནི་རེག་བྱ་རྡོ་རྗེ་མའི་ཆོས་འབྱུང་བ་ལའོ། །

[Block 5006]
རང་གི་ལྷ་ཡི་རྣལ་འབྱོར་གྱིས། །ཞེས་པ་ནི་རྣམ་པར་སྣང་མཛད་ལ་སོགས་པའི་ལྷའི་ཕྱག་རྒྱ་ཆེན་པོ་ལ་སོགས་པའི་གཟུགས་ཀྱིས་སོ། །

[Block 5007]
ཉིན་མཚན་དུ་ནི་དུས་ཇི་སྲིད་ཀྱི་སེམས་རྩེ་གཅིག་ཏུ་འགྱུར་བའོ། །

[Block 5008]
གང་གི་ཚེ་མཐོང་བའི་མཚན་མ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་གང་གི་ཚེ་ཐིག་ལེ་བསྒོམ་པ་བརྟན་པར༌[^2951]འགྱུར་ན་དེའི་ཚེ་རྣལ་འབྱོར་པ་ལ་མཚན་མ་འདི་ལྟར་འབྱུང་སྟེ། ཐིག་ལེ་ཙམ་ལ་ཁམས་གསུམ་ཐམས་ཅད་ཀྱི་ང་རྒྱལ་དང་ཕྱིའི་སེམས་ཅན་དུ་གྱུར་པའི་རྣམ་པར་རྟོག་པ་དང་བྲལ་བ་དང་། སེམས་དང་སེམས་ལས་བྱུང་བའི་ཆོས་མི་འབྱུང་བ་དང་། གམ་ན་གནས་པའི་སྒྲ་ལ་སོགས་པ་མི་ཟིན་པ་དང་། རང་གི་ལུས་མི༌[^2952]ཚོར་བ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 5009]
དེའི་ཚེ་རྡོ་རྗེ་ལ་སོགས་པ་ཞེས་པ་ནི་ཐུགས་རྡོ་རྗེ་ལ་སོགས་པའི་རྣལ་འབྱོར་པ་རྣམས་ཀྱིས་བསྒོམ་པར་གྱུར་པའི་རང་གི་ཕྱག་མཚན་ནོ། །

[Block 5010]
བསྒོམ་པས་མི་གཡོ་བར་ཤེས་ནས་ཞེས་པ་ནི་བསྒོམ་པར་བྱ་བ་དང་སྒོམ་པ༌[^2953]དག༌[^2954]གཅིག་ཏུ་གྱུར་པའི་མཚན་ཉིད་ཀྱིས་དེའི་བདག་ཉིད་དུ་ཤེས་ནས་སོ། །
--- END BLOCKS ---
