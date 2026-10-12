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
འགལ་བ་ལ་གཉིས་ཏེ། འཇིག་རྟེན་པ་དང་འགལ་བ་དང་། །སྒྲ་དང་འགལ་བའོ། །

[Block 2592]
འཇིག་རྟེན་དང་འགལ་བ་ནི། དཔེར་ན། །

[Block 2593 [VERSE]]
ཕ་དང་མ་ནི་བསད་བྱ་ཞིང་། །
རྒྱལ་པོ་གཙང་མ་གཉིས་དང་ནི། །
ཡུལ་འཁོར་འཁོར་བཅས་བསད་བྱས་ན།[^1694] །
མི་དེ་དག་པར་འགྱུར་ཞེས་བཤད། །

[Block 2594]
ཅེའོ། །

[Block 2595]
སྒྲ་དང་འགལ་བ་ནི་དཔེར་ན་བུམ་པའི་དོན་རྗོད་པར་བྱེད་པའི༌[^1695]སྒྲ་སྨྲ་བ་ན་སྣམ་བུའི་སྒྲ་བཞིན་ནོ། །

[Block 2596]
འདི༌[^1696]ནི་སྒྲ་དང་འགལ་བ་ཡིན་ཏེ། དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་སྒྲས་རྣམ་པར་སྣང་མཛད་ལ་སོགས་པ་རྗོད་པར་མི་རིགས་ཏེ། འོན་ཀྱང་རིན་པོ་ཆེ་ལྟ་བུའི་གང་ཟག་རྣམས་བརྗོད་དོ། །

[Block 2597]
ཞེ་སྡང་གི་རིགས་ཞེས་བྱ་བ་ནས། སྒྲ་ཇི་བཞིན་པ་ཞེས་བྱ་བའི་བར་དུ་ནི། དཀྱིལ་འཁོར༌[^1697]རྒྱལ་བ་མཆོག་གི་ཏིང་ངེ་འཛིན༌[^1698]བཤད་པར་འོས་པའི་ཕྱིར་རོ། །

[Block 2598]
བཛྲ་དྷྲྀཀ་ཅེས་བྱ་བ་ནས། དྲང་བ་དང་ངེས་པའི་དོན་གྱི་བར་ནི་བརྟག་པའི༌[^1699]རྣལ་འབྱོར་དང་ཡོངས་སུ་དག་པའི་རྣལ་འབྱོར་གྱི་མཚན་ཉིད་དཀྱིལ་འཁོར་གྱི༌[^1700]འཁོར་ལོ་སྤྲོས་པའི་ཕྱིར་རོ། །

[Block 2599]
དེ་བས་ནི་བསྐྱེད༌[^1701]པའི་རིམ་པའི་ཕྱོགས་སུ་དཀྱིལ་འཁོར་རྒྱལ་བ་མཆོག་གི་ཏིང་ངེ་འཛིན་ཏོ། །

[Block 2600]
རྫོགས་པའི་རིམ་པའི་ཕྱོགས་སུ་བདག་ལ་བྱིན་གྱིས་རློབ་པའི་རིམ་པ་བསྟན་ཏོ། །

[Block 2601]
ལེའུ་དང་པོ་ཞེས་བྱ་བ་ལ་སོགས་པས་དང་པོའི་ལེའུ༌[^1702]བཤད་པའི་དབྱེ་བ་ཉེ་བར་བསྡུས་པ་བསྟན་ཏོ། །

[Block 2602]
[^1703]

[Block 2603]
དེ་ནས་ཞེས་བྱ་བ་ནས། སྒྲ་ཇི་བཞིན་པའི་བར་དུ་ནི་བདེ་བར་གཤེགས་པའི་གསུང་ཙམ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 2604]
ཁྱེད་ཀྱི་སེམས་ཞེས་བྱ་བ་ནས་དྲང་བ་དང་ངེས་པའི་དོན་ཞེས་བྱ་བའི་བར་དུ༌[^1704]རིམ་པ་གཉིས་བཤད་པར་འོས་པའི་ཕྱིར་རོ། །

[Block 2605]
ཨེ་མའོ་ཞེས་བྱ་བ་ནས་དགོངས་པ་མ་ཡིན་པ་ཞེས་བྱ་བའི་བར་དུ་དེ་ཁོ་ན་ཉིད་ཤིན་ཏུ་གསལ་བར་བསྟན་པའི་ཕྱིར་རོ། །

[Block 2606]
དེ་ཡང་མྱུར་བའི་ཏིང་ངེ་འཛིན་གྱིས་རྫོགས་པའི་ཡེ་ཤེས་ཀྱི་སྐུ་འཆད་པར་འདོད་པའི་ཕྱིར་རོ། །

[Block 2607]
དངོས་པོ་མེད་པ་ཞེས་པ་ནས་རྣམ་པ་བཞི་ཡིས་བཤད་ཅེས་བྱ་བའི་བར་དུ་ནི་ཡི་གེའི་དོན་གྱིས་སྟོང་པ་ཉིད༌[^1705]བསྟན་ཏེ། རྣམ་པར་ཐར་པ་བཞི་སོ་སོར་བསྟན་པའི་སྒོ་ནས་སྟོང་པ་ཉིད་ཀྱི་དེ་ཁོ་ན་ཉིད་རྟོགས་པར་བྱ་བས་སོ། །

[Block 2608]
སྤྱིའི་དོན་གྱིས་ནི་མདོ་སྡེ་ལ་སོགས་པ་རྣམས་ཀྱི་འགྱོད་པ་བཟློག་པར་བསྟན་ཏོ། །

[Block 2609]
སྦས་པའི་ཕྱོགས་སུ་ནི་བདག་བྱིན་གྱིས་རློབ་པའི་རིམ་པ་བསྟན་པས་སོ། །

[Block 2610]
མཐར་ཐུག་པའི་ཕྱོགས་སུ་ནི་ཟུང་དུ་འཇུག་པའི་རིམ་པ་བསྟན་ཞེས་པའི་ཐ་ཚིག་གོ། །

[Block 2611]
དངོས་པོ་ཐམས་ཅད་ཅེས་བྱ་བ་ནས་དགོངས་པ་མ་ཡིན་པ་ཞེས་པའི་བར་དུ་ནི་དེ་ཁོ་ན་ཉིད་གསལ་བར་བཤད་པའི་ཕྱིར་རོ། །

[Block 2612]
དེ་ཁོ་ན་ཉིད་ནི་རྫོགས་པའི་རིམ་པའོ། །

[Block 2613]
བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་ཚིགས་སུ་བཅད་པ་ལྔ་པོས་རྡོ་རྗེ་བཟླས་པ་ལ་སོགས་པའི་རིམ་པ་ལྔ་པོ་མ་ངེས་པར་བསྟན་པའི་ཕྱིར་རོ། །

[Block 2614]
དེ་ནས་ཞེས་བྱ་བ་ནས་སྒྲ་ཇི་བཞིན་ཞེས་བྱ་བའི༌[^1706]བར་དུ་ནི་ཕྱག་འཚལ་བ་ཙམ་བཤད་པའི་ཕྱིར་རོ། །

[Block 2615]
ལེའུ་གཉིས་པའོ་ཞེས་པས་ཉེ་བར་སྡུད་པ༌[^1707]བསྟན་ཏོ། །

[Block 2616]
དེ་ནས་བཅོམ་ལྡན་འདས་ཞེས་བྱ་བ་ནས་དྲང་བའི་དོན་དང་ཞེས་བྱ་བའི་བར་དུ་ནི་སྐུ་རྡོ་རྗེ་ལ་སོགས་པའི་ངོ་བོ་དང་དེ་རྣམས་ཀྱི་དེ་ཁོ་ན་ཉིད་བསྟན་པའི་ཕྱིར་རོ། །

[Block 2617]
རིན་ཆེན་ཞེས་བསྟན་པ་ནས་རྣམ་པ་བཞི་ཡིས་བཤད་ཅེས་པའི་བར་དུ་ནི་དེ་ལ་སྤྱིའི་དོན་གྱི་ཕྱོགས་སུ་གདོང་གི་སྣ་ལ་ཐིག་ལེ་བསྒོམ་པའོ། །

[Block 2618]
སྦས་པའི་ཕྱོགས་སུ་གསང་བའི་ཆུ་སྐྱེས་དང་རྡོ་རྗེའི་རྩེ་མོར་བསྒོམ་པའོ། །

[Block 2619]
མཐར་ཐུག་པའི་ཕྱོགས་སུ་སྙིང་གི་པདྨའི་སྣ་ལ་བསྒོམ་པ༌[^1708]སྟེ། གཏི་མུག་དང་འདོད་ཆགས་དང་ཞེ་སྡང་གི་རིགས་ཅན་རྣལ་འབྱོར་པའི་དབྱེ་བས་སོ། །

[Block 2620]
ཚིག་རེ་རེའི་བསྡུ་བ་དང་ཆོས་མཐུན་པ་བཤད་པ་ནི་ཡི་གེའི་དོན་ཏེ་ཐམས་ཅད་དུ་སྦྱོར་རོ། །

[Block 2621]
ནམ་མཁའི༌[^1709]ཞེས་པ་དྲང་བ་དང་ངེས་པའི་དོན་ཞེས་པའི་བར་དུ་ནི་རིམ་པ་གཉིས་འཆད་པར་འདོད་པའི་ཕྱིར་རོ། །

[Block 2622]
དེ་ལ་བསྐྱེད་པའི་རིམ་པ་ནི་རྣམ་པར་སྣང་མཛད་ལ་སོགས་པ་ལྷའི་ཚོགས་བསྒོམ༌[^1710]པའི་གཙོར་གྱུར་པའོ། །

[Block 2623]
རྫོགས་པའི་རིམ་པ་ནི་དཀྱིལ་འཁོར་བཞི་འཆར་བ་ན་རྡོ་རྗེ་བཟླས་པ་འཆད་པར་འདོད་པའི་ཕྱིར་རོ། །

[Block 2624]
ལེའུ་གསུམ་པའི་ཞེས་པ་འདིས་ཉེ་བར་སྡུད་པ་བསྟན་ཏོ། །

[Block 2625]
[^1711]

[Block 2626]
དེ་ནས་ཞེས་པ་ནས་སྒྲ་ཇི་བཞིན་པ་ཞེས་པའི༌[^1712]བར་དུ་ནི་བསྟོད་པ་ཙམ་གཙོ་བོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2627]
དཀྱིལ་འཁོར་ལ་སོགས་པ་ཞེས་པའི་སྒྲས་ཤེས་པར་བྱའོ་ཞེས་དགོངས་སོ། །

[Block 2628]
དེ་བཞིན་ཞེས་པ་ནས་དགོངས་པ་མ་ཡིན་ཞེས་པའི་བར་དུ་ནི་དཀྱིལ་འཁོར་གྱི་དེ་ཁོ་ན་ཉིད་བསྟན་པས་སོ། །

[Block 2629]
དེ་ལྟར༌[^1713]ན་དཀྱིལ་འཁོར་ལ་སོགས་ཞེས་བྱ་བ་འདིས་སྒྲ་ཇི་བཞིན་པར་ཇི་ལྟར་མི་འགྱུར་ཞེ་ན། སྨྲས་པ། [^1714]དཀྱིལ་འཁོར་གྱི་ཚད་ཙམ་དང་དགོད་པ་དེ༌[^1715]དག་ཏུ་སྒྲ་ཇི་བཞིན་པའོ། །

[Block 2630]
འདིར་ནི་དཀྱིལ་འཁོར་གྱི་དེ་ཁོ་ན༌[^1716]ཉིད་ཀྱི་སྐབས་ཡིན་པས་དགོངས་པ་མ་ཡིན་པའོ། །
--- END BLOCKS ---
