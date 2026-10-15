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
རྫས་ཀྱི་ཕྱིར་གཞན་འཆི་བར་འདོད་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ལྷུང་བཟེད་དང་། ཆོས་གོས་ལ་སོགས་པའི་རྫས་ཐོབ་པར་བྱ་བའི་དོན་དུའོ། །

[Block 2592]
བྱ་བ་མ་ཡིན་པ་བྱེད་པ་ལ་སེམས་ཀྱིས་རྗེས་སུ་ཡི་རང་བར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། བྱ་བ་མ་ཡིན་པ་ཉིད་བྱེད་པ་ནི་བྱ་བ་མ་ཡིན་པ་ཉིད་བྱེད་པའོ། །

[Block 2593]
རང་ངམ་གཞན་གྱིས་འདས་པའམ་མ་འོངས་པའམ།[^1753] ད་ལྟར་བྱུང་བ་ལ་དེའི་རྗེས་སུ་ཡི་རང་བར༌[^1754]སེམས་ཀྱིས་མ་བྱས་པ་ཉིད་དམ་ལུས་ཀྱི་བྱ་བས་ཀྱང་མ་ཡིན་ཞེས་བྱ་བ་སྟེ། འདི་དག་ལ་སེམས་སྔོན་དུ་འགྲོ་བ་ཉིད་ཀྱི་ཕྱིར་གྲུབ་པ་དམན་པའི་དེ་ཉིད་བརྗོད་པ་ལ་གཞན་དུ་གཏམ་གང་ཡང་མེད་དོ་ཞེས་བྱ་བ་རྟོགས་པའི་ཕྱིར་རོ། །

[Block 2594]
གཞུང་ཁ་ཅིག་ལས་ཚེ་དང་ལྡན་པ་ཉེ་སྡེའི་དབང་དུ་མཛད་ནས་གསུངས་པ། ཉེ་སྡེ་ཁྱོད་ཀྱིས་མངལ་ན་གནས་པ་རླུགས་པར་བྱས་པ་བདེན་ནམ། བཙུན་པ་མ་ལགས་ཏེ་འདི་ལྟར་བདག་གིས་རྗེས་སུ་ཡི་རང་བར་ནི་བགྱིས་སོ། །

[Block 2595]
བཀའ་སྩལ་པ། དགེ་སློང་དག་དགེ་སློང་ཉེ་སྡེ་ལ་ལྟུང་བ་མེད་དེ་སླར་དགེ་སློང་གིས༌[^1755]མངལ་ན་གནས་པ་རླུགས་པར་མི་བྱའོ། །

[Block 2596]
དགེ་སློང་མངལ་ན་གནས་པ་རླུགས་པར་བྱེད་ན་འགལ་ཚབས༌[^1756]ཅན་དུ་འགྱུར་རོ་ཞེས་གསུངས་ཏེ། དེ་བས་ན་མདོ་འདི་བྱས་སོ། །

[Block 2597]
[^1757]མཛེས་པ་འདི་བྱེད་པར་འགྱུར་བ་ཁྱེད་ནི་འདི་བྱེད་དུ་གཞུག་པ་མ་ཡིན་ཏེ། འཇུག་པ་མ་ཡིན་ཞེས་བྱ་བར་སེམས་པར་བྱེད་ན་འདིས་ནི་འདི་བྱེད་དེ་ཅིའི་ཕྱིར་མི་བྱེད། བདག་ལ་འདིས་ཅི་ཞིག་བྱ་ཞེས་བྱ་བའི་དབང་དུ་མཛད་ནས་འདོན་པ་འདི་ཡིན་ནོ། །

[Block 2598]
འདི་ལ་དཔེ་ཉིད་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 2599]
བྱེད་པར་འགྱུར་བ་ལ་གནས་པ་ཐམས་ཅད་ཉིད་ལ༌[^1758]བྱ་བ་ལ་གནས་པ་དང་བྱ་བ་མ་ཡིན་པ་བྱེད་པ་ལ་རྗེས་སུ་ཡི་རང་བ་ལ་ཁ་ན་མ་ཐོ་བ་དང་བཅས་པ་ཉིད་ཀྱི་ཕྱིར་ཤིན་ཏུ་ཡང་དགེ་སློང་ལ་མི་མཐུན་པ་ཉིད་ཀྱི་ཕྱིར་ཞེས་བྱ་བ་ལ༌[^1759]ཁྱད་པར་མི་བརྟེན་པའོ། །

[Block 2600]
ཇི་ལྟར་ཡང་རྗེས་སུ་ཡི་རང་བ་ལ་ལྟུང་བ་ཉིད་དེ་གང་གི་ཕྱིར་འདི་ལ་ལྟུང་བར་བྱ་བ་ཞེས་བྱ་བ་བརྗོད་པ་དང་སྦྱར་བའོ། །

[Block 2601]
ལྟུང་བ་ལ་བརྟེན་པའི་ཡིད་ཀྱི་སྒྲིབ་པ་འདི་ཞེས་བྱ་བའོ། །

[Block 2602]
གང་དུ་ཕམ་པ་གསུམ་པ་ཞེས་བྱ་བ་ལ་ལྟོས་ནས་བརྗོད་པར་བྱ་སྟེ། དེའི་ཕྱིར་སྲོག་བཅད༌[^1760]ནའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 2603]
སེམས་ཇི་ལྟ་བུས་ཤེ་ན། དེའི་ཕྱིར་དེ་ལྟར་བསམས་པས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སྲོག་གཅོད་པའི་སེམས་ཀྱིས་སོ། །སུའི་སྲོག་གཅོད་པ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་མིར་གྱུར་པའིའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་འགྲོ་བ་ཙམ་ལ་ནི་མཚན་མ་ཉིད་མ་ཡིན་ཏེ། བུད་མེད་དང་སྐྱེས་པ་དང་མ་ནིང་དང་མཚན་མེད་པ་དང་། མཚན་གཉིས་པ་དང་། མངལ་ནས་སྐྱེས་པ་ཉིད་ལ་སོགས་པ་ཁྱད་པར་འགའ་ཞིག་ལ་ཞེས་བྱ་བ་དེའི་ཕྱིར་འགྲོ་བའི་ཚིག་གོ། །

[Block 2604]
གཞན་དུ་འདུ་ཤེས་པས་སམ་ཞེ་ན་མ་ཡིན་ཏེ། དེའི་ཕྱིར་དེ་ལྟར་འདུ་ཤེས་པས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ་མ་ནོར་བར་རོ། །ཇི་ལྟར་རྣམ་པ་གང་གིས་ཤེ་ན། དེའི་ཕྱིར་གང་ཡང་རུང་བས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རྣམ་པ་གང་ཡང་རུང་བས་སོ། །

[Block 2605]
དེ་ཉིད་ཀྱི་སྤྲོས་པ་བསྟན་པའི་ཕྱིར། བྱེ་བྲག་མེད་པ་ནི་ལུས་དང་དེ་དང་འབྲེལ་པ་དང་། འཕངས་པ་དང་གཞན་དང་བསྒོ་བ་རྣམས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བྱེ་བྲག་མེད་པ་ཞེས་བྱ་བ་ནི་འདི་ནས་བརྩམས་ཏེ་ཇི་སྲིད་དུ་རྒྱུ་དེས་གཞན་གྱི་ཚེ་ཤི་ནའོ་ཞེས་འབྱུང་བ་ཡན་ཆད་ཀྱི་དབང་དུ་བྱས་ཏེ་རིག་པར་བྱའོ། །

[Block 2606]
བྱེ་བྲག་མེད་པ་ནི་ཐ་མི་དད་པ་སྟེ། ཤི་བའི་དོན་བྱེད་པ་ལ༌[^1761]འདི་རྣམས་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2607]
རྣམ་པ་གང་ཡང་རུང་བས་གསོད་པ་ལ་ཕམ་པར་འགྱུར་རོ་ཞེས་བྱ་བའི་དགོངས་པའོ། །

[Block 2608]
ལུས་ཞེས་བྱ་བ་ནི་ལུས་ཉིད་དོ། །

[Block 2609]
དེ་དང་འབྲེལ་པ་ཞེས་བྱ་བ་ནི་ལུས་དང་འབྲེལ་པ་དབྱིག་ལ་སོགས་པའོ། །

[Block 2610]
འཕངས་པ་ནི་ལུས་ཀྱིས་སམ་དེ་དང་འབྲེལ་པས་གཏང༌[^1762]བའོ། །

[Block 2611]
དེ་ལ་གཞན་གྱི་ངེས་པར་སྦྱར་བ་གསད་པར༌[^1763]བྱ་བ་ནི་བུད་མེད་ལ་སོགས་པའོ། །

[Block 2612]
བསྒོ་བ་ཞེས་བྱ་བ་ནི་གསད་པར༌[^1764]བྱ་བ་དེ་ཉིད་ལ་རང་གིས་བསྒོ་བའོ། །

[Block 2613]
དུག་དང་ཕྱེ་མ་དང་དོང་དང་ཤིང་དང་རང་བཞིན་ཉམས་པ་གཏོང་བ་དང་བྲང་དུ་འདེབས་པ་དང་། འཁྲུལ་འཁོར་དང་སྒྱུ་ཐབས་དང་རོ་ལངས་དང་རྗེས་སུ་སྦྱོར་བ་རྣམས་སོ་ཞེས་བྱ་བ་ནི་བྱེ་བྲག་མེད་པ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2614]
རང་བཞིན་ཉམས་པ་ཞེས་བྱ་བ་ནི་དེ་ཉིད་ཀྱིས༌[^1765]ཉམས་པ་འམ་གསོད་པ་འདི་ཉིད་ཀྱི༌[^1766]དོན་དུ་མཚན་མ་དེ་མེད་པར་ཉམས་པའི་རང་བཞིན་གྱིས་གང་ཞིག་དེར་འདི་ལྟ་བུར་གྱུར་པ་དེ་ལ་འཆི་བའི་རྐྱེན་ཉེ་བར་གནས་པར་འགྱུར་ཞེས་བྱ་བའི་བློས་བསྐུར་བ་ནི་རང་བཞིན་ཉམས་པས་བསྐུར་བའོ། །

[Block 2615]
རོ་ལངས་ཕྱེད་པ༌[^1767]དང་ཕྱེད་དུ་གྱུར་པ་ཉིད་ཀྱིས་ཡོ་བྱད་རྣམས་ལ་གཞན་དུ་མ་ཡིན་པར་བསྟན་པ་འདི་ལ་རོ་ལངས་ཉིད་མ་ཡིན་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་རོ་ལངས་ཀྱི་ཚིག་བཟུང་བ་ཉིད་དུ་ཤེས་པས་བསྡུས༌[^1768]པ་ཉིད་དུ་མ་བྱས་སོ། །

[Block 2616]
གཡང་དུ་གཏང་བའོ༌[^1769]ཞེས་བྱ་བ་ནི་གཡང་ལ་སོགས་པ་ལ་ཞེས་བྱ་བའི་དོན་གྱིས་གོ་བར་བྱའོ། །

[Block 2617]
མེ་དང་ཆུར་འཇུག་པའོ། །

[Block 2618]
གྲང་བ་དང་ཚ་བར་འདོགས་པ་ཞེས་བྱ་བ་ནི་རྐྱེན་འདི་དང་ལྡན་པ་འདི་ལ་འཆི་བ་འབྱུང་བར་འགྱུར་ཞེས་བྱ་བའི་བློས་སོ། །

[Block 2619]
ཕོ་ཉར་གཏོང་བ་ལ་སོགས་པའི་ཞེས་བྱ་བ་ནི་གང་དུ་འཇིགས་པ་སྲིད་པ་དེར་ཕོ་ཉ་དང་མངགས་པ༌[^1770]ཉིད་དུ་གཏོང་བའོ། །

[Block 2620]
དེར་སོང་ན་འདི་དང་འདི་ལྟ་བུ་རྙེད་པར་འགྱུར་རོ་ཞེས་བྱ་བའི་རྣམ་པས་བསྐུལ་བ་གང་ཡིན་པ་དེ་ཉེ་བར་བསྡུ་བའི་དོན་དུ་སོགས་པའི་སྒྲའོ། །

[Block 2621]
དེའི༌[^1771]རྗེས་སུ་བསྒྲུབ་པ་ཆུང་ངུ་ཉིད་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་རྐང་པའི་མཐེ་བོང་དང་རྒྱ་ཤུག༌[^1772]གི་ཚི་གུ༌[^1773]དང་ཤིང་བལ་ལ་སོགས་པ་བསྣུན་པ་ལྟ་བུ་དག་གོ། །

[Block 2622]
རྗེས་སུ་བསྒྲུབ་པ་ལ་ཆུང་བ་འདི་ནི་མཚན་ཉིད་འདི་ལས་གྲུབ་སྟེ་བྱེ་བྲག་མ་སྨོས་པ་དེ་གསལ་བར་བསྟན་པའི་ཕྱིར་འདི་སྤྲོས་པའོ། །

[Block 2623]
གསད་པར༌[^1774]བྱ་བ་ནི་སྐྱེས་པ་དང་བུད་མེད་དང་མ་ནིང་ཉིད་དོ་ཞེས་བྱ་བ་ནི་བྱེ་བྲག་མེད་པར་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2624]
གནས་དེ་དག་བསྟན་པ་ནི་སྤྲོས་པའི་དོན༌[^1775]བསྟན་པ་ཡིན་ནོ། །

[Block 2625]
གཞི་དེས་གཞན་གྱི༌[^1776]ཚེ་ཤི་ནའོ་ཞེས་བྱ་བ་ལ་འདིར་གཞུང་ནི་དེས་དེའི་ཚེ་མ་ཡིན་ཡང་འོན་ཀྱང་དེས་དེའི་འོག་ཏུའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2626]
འདུན་པ་བཟློག་པའི་འོག་ཏུ་ནི་རྒྱུ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཤི་ན་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2627]
ཤི་བའམ་འགྲོ་བ་ལ་འཇིགས་པ་དང་བཅས་པའི་གནས་ལ་བསྒོ་བར་བྱ་བའམ། ངེས་པར་སྦྱར་ཏེ་གསད་པར༌[^1777]བྱ་བའམ། གཞན་ལ་དེའི་དོན་དུ་འདུས་པ༌[^1778]ཟློག་པར་བྱེད་པ་དེ་ལས་གཞན་ལ་འདའ་བར་བྱས་ནས༌[^1779]དེའི་ཚིག་མ་ཡིན་ནོ། །

[Block 2628]
སྦྱར་བར་བྱས་པའི་ཤི་བ་ལ་སྦྱོར་བར་བྱེད་པ་པོའི་རྒྱུ་མཚན་ཉིད་དུ་སྔར་འདུན་པ་ཟློག་པར་བྱེད་པར་གྱུར་པའི་ཤི་བ་ལ་དེ་ལས་ཕམ་པ་འདའ་བར་འགྱུར་རོ། །

[Block 2629]
ཕྱིས་དེས་སྐྱེ་བ་ཡིན་ཏེ། འདི་ལ་ནི་སྦྱོར་བ་ཙམ་ཉིད་ཡིན་ཏེ། དངོས་གཞིའི་ཕམ་པ་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2630]
དཀུ་མཉེས་པས་མ་དང་མངལ་ན་གནས་པ་གཉིས་ལས་མ་བསམས་པ་ཤོས་ན་སྦོམ་པོའོ་ཞེས་བྱ་བ་ནི༌[^1780]ཤི་ནའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །
--- END BLOCKS ---
