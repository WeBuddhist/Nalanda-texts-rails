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
[Block 701]
དེ་ལ་འཇུག་པའི་རྣམ་པར་ཤེས་པ་གནས་གྱུར་པ་ལ་གཉེན་པོ་ནི་སྟོང་པ་ཉིད་དང་སྣང་བའི་ཡེ་ཤེས་སོ། །

[Block 702]
ཉོན་མོངས་པ་ཅན་གྱི་ཡིད་གནས་གྱུར་པ་ལ་གཉེན་པོ་ནི་སྣང་བ་མཆེད་པ་དང་ཤིན་ཏུ་སྟོང་པའོ། །

[Block 703]
ཀུན་གཞི་རྣམ་པར་ཤེས་པ་གནས་གྱུར་པ་ལ་གཉེན་པོ་ནི་སྣང་བ་ཐོབ་པ་དང་ཆེན་པོ་སྟོང་པའོ། །

[Block 704]
ཡེ་ཤེས་གསུམ་པོ་དེ༌[^462]རོ་གཅིག་པར་བྱེད་པ་འོད་གསལ་བའི་ཡེ་ཤེས་ཐམས་ཅད་སྟོང་པའི་ངོ་བོའོ། །

[Block 705]
རྣམ་པར་ཤེས་པ་གསུམ་པོའི་རང་བཞིན་ནི་བརྒྱད་ཅུའོ། །

[Block 706]
དེ་ལ་འཇུག་པའི་རྣམ་པར་ཤེས་པའི་རང་བཞིན་ཤེས་རབ་ཀྱི་ངོ་བོ་སྟེ་སུམ་ཅུ་རྩ་གསུམ་མོ། །

[Block 707]
ཉོན་མོངས་པ་ཅན་གྱི་ཡིད་ཀྱི་རང་བཞིན་ནི་བཅུ་སྟེ། ཐབས་ཀྱི་རང་བཞིན་ནོ། །

[Block 708]
ཀུན་གཞི་རྣམ་པར་ཤེས་པའི་རང་བཞིན་བདུན་པོ་ནི་མ་རིག་པའི་ངོ་བོ་ཉིད་དོ། །

[Block 709]
དེ་རྣམས་ཁོ་ན་ཉིན་མོ་དང་མཚན་མོའི་དབྱེ་བས་བརྒྱ་དྲུག་ཅུར་འགྱུར་རོ། །

[Block 710]
དེ་རྣམས་སྤང་བར་བྱ་བའི་ཕྱིར་སྔགས་ཀྱི་རིམ་པ་བསྟན་པར་བྱ་སྟེ། དང་པོར་ལྟེ་བར་རྩིབས་བརྒྱད་པའི་ཆོས་ཀྱི་དབྱིངས་ཀྱི་འཁོར་ལོའི་ལྟེ་བར་པདྨའི་སྟེང་དུ་ཟླ་བའི་དཀྱིལ་འཁོར༌[^463]ལ་ཐིག་ལེས་བརྒྱན་པའི་དབྱངས་ཡིག་དང་པོ་དགོད་པར་བྱས་ལ། སྤྱི་བོ་ལ་སོགས་པར་ཡི་གེ་གསུམ་ལ་དམིགས་ཏེ་ཨའི་ཐིག་ལེ་ལས་བྱུང་བའི་འོད་ཟེར་དཀར་པོས་སྤྱི་བོ་ནས་ཡི་གེ་ཨོཾ་འཇུག་པའི་རྣམ་པར་ཤེས་པའི་ངོ་བོ་ཉིད་བཀུག་ཅིང་དེ་ཉིད་དུ་འཇུག་པར་བྱ་སྟེ། དེ་ལ་ཡིད་རྩེ་གཅིག་པར་གནས་པར་བྱའོ། །

[Block 711]
དེའི་ཚེ་རང་བཞིན་སུམ་ཅུ་རྩ་གསུམ་དང་ལྡན་པའི་འཇུག་པའི་རྣམ་པར་ཤེས་པ་ལོག་པ་ལས་ཟླ་བའི་སྣང་བ་དང་འདྲ་བའི་སྣང་བའི༌[^464]ཡེ་ཤེས་སྐྱེ་བར་འགྱུར་རོ། །

[Block 712]
དེའི་འོག་ཏུ་ཆོས་ཀྱི༌[^465]དབྱིངས་ཀྱི་འཁོར་ལོ་དེ་ཉིད་དུ་ཉི་མའི་དཀྱིལ་འཁོར་དང་རྡོ་རྗེའི་ཆང་ཟུངས་ཀྱི་ནང་ན་གནས་པའི་ཐིག་ལེ་གཉིས་ཀྱིས་བརྒྱན་པའི་དང་པོའི་དབྱངས་ཡིག་ཁ་དོག་དམར་པོ་རྣམ་པར་བསམས་ཏེ། དེ་ལས༌[^466]བྱུང་བའི་འོད་ཟེར་དམར་པོ་མགྲིན་པ་ན་གནས་པའི་ཡི་གེ་ཨ་ཉོན་མོངས་པ་ཅན་གྱི་ཡིད་ཀྱི་ངོ་བོ་ཉིད་བཀུག་ལ་དེ་ཉིད་དུ་འཇུག་པར་བྱ་སྟེ། དེ་ཉིད་དུ་ཡིད་རྩེ་གཅིག་པར་གནས་པར་བྱའོ། །

[Block 713]
དེའི་ཚེ་རང་བཞིན་བཞི་བཅུ་དང་ལྡན་པའི་ཉོན་མོངས་པ་ཅན་གྱི་ཡིད་ལོག་པས་ཉི་མའི་སྣང་བ་དང་འདྲ་བའི་སྣང་བ་མཆེད་པའི་ཡེ་ཤེས་སྐྱེ་བར་འགྱུར་རོ། །

[Block 714]
དེའི་རྗེས་ལ་ས་བོན་དང་པདྨ་དང་ཟླ་བ་དང་ཉི་མ་དང་རྡོ་རྗེའི་དམིགས་པ་སྤངས་ཏེ། འཁོར་ལོ་ལ་གནས་པའི་ཐིག་ལེ་ཙམ་ལ་བལྟས་ཏེ། དེ་ལས་བྱུང་བའི་མཚམས་ཀྱི་སྣང་བ་དང་མཚུངས་པའི་འོད་ཟེར་གྱི་སྙིང་ག་ན་གནས་པའི་ཐུགས་ཀྱི་རྡོ་རྗེའི་ས་བོན་བཀུག་ལ་དེ་ཉིད་དུ་འཇུག་པར་བྱ་སྟེ་དེ་ཉིད་དུ་ཡིད་རྩེ་གཅིག་པར་གནས་པར་བྱའོ། །

[Block 715]
དེའི་ཚེ་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་རང་བཞིན་བདུན་དང་ལྡན་པ་ལོག་པས་མཚམས་ཀྱི་སྣང་བ་དང་མཚུངས་པའི་སྣང་བ་ཐོབ་པའི་ཡེ་ཤེས་སྐྱེ་བར་འགྱུར་རོ། །

[Block 716]
དེ་ནས་ཀྱང་རིམ་གྱིས་ཐིག་ལེ་དང་འཁོར་ལོ་ལྟེ་བའི་མཁའ་ལ་ཐིམ་པས་རྟགས་ལྔའི་སྣང་བ་སྔོན་དུ་འགྲོ་བར་ལུས་ལ་སོགས་པའི་རྣམ་པར་རྟོག་པའི༌[^467]བག་ཆགས་མ་ལུས་པ་ཟད་པས༌[^468]སྤྲིན་མེད་པའི་ནམ་མཁའ་དང་འདྲ་བའི༌[^469]ཆོས་ཀྱི་དབྱིངས་ཀྱི་ཡེ་ཤེས་འོད་གསལ་བའི་དེ་ཁོ་ན་ཉིད་སྐྱེ་བར་འགྱུར་རོ། །

[Block 717]
དེ་དག་རིམ་པ་ཇི་ལྟ་བ་བཞིན་དུ་སྟོང་པ་དང་ཤིན་ཏུ་སྟོང་པ་དང་སྟོང་པ་ཆེན་པོ་དང་ཐམས་ཅད་སྟོང་པ་སྟེ། སྣང་བ་ལ་སོགས་པའི་ཡེ་ཤེས་རྣམས་ཀྱི་རྣམ་གྲངས་སུ་ཤེས་པར་བྱ་སྟེ། ཀུན་ནས་ཉོན་མོངས་པ་དང་རྣམ་པར་བྱང་བ་དག་རང་བཞིན་གཅིག་པ་ཡིན་པའི་ཕྱིར་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ་ཞེས་སྔགས་ཀྱི་རིམ་པས་སེམས་རྣམ་པར་དག་པའི་རིམ་པ་བསྟན་ཏོ། །

[Block 718 [HEADING]]
##### ཕྱག་རྒྱའི་རིམ་པ། ^1-2-2-2-0

[Block 719]
ད༌[^470]ནི་ཕྱག་རྒྱའི་རིམ་པ་བཤད་པར་བྱ་སྟེ། རེ་ཞིག་དང་པོ་རྣལ་འབྱོར་པས་མྱུར་བའི་ཏིང་ངེ་འཛིན་གྱིས་རྡོ་རྗེ་འཆང་ཆེན་པོ་ལ་སོགས་པའི་ཕྱག་རྒྱ་བསྒོམས་ཏེ། སྨེ་ཤ་ཅན་ལ་སོགས་པའི་བུ་མོ་ལོ་བཅུ་གཉིས་པ༌[^471]ལ་སོགས་པ༌[^472]ན་སོ༌[^473]དང་ལྡན་པའི་ཕྱག་རྒྱ་བླངས་ཏེ་དེ༌[^474]ནི་མཱ་མ་ཀཱི་ལ་སོགས་པར༌[^475]ལྷག་པར་མོས་ཏེ་མཆོག་གི་བསྙེན་པ་ལ་སོགས་པས༌[^476]བདེ་བ་ཆེན་པོ་ཉེ་བར་མཚོན་པར་བྱ་བའི་ཕྱིར་དེ་དང་ལྷན་ཅིག་སྙོམས་པར་ཞུགས་པར་བྱའོ། །

[Block 720]
དེ་ལ་རྡོ་རྗེ་དང་པདྨ་བསྐྱོད་པ་ལ་འཇུག་པ་ཚངས་པའི་བུ་ག་ནས་ཞུ་བའི་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་གནས་སྐབས་སུ་སྣང་བའི་ཡེ་ཤེས་དང་རྣམ་པ་སྣ་ཚོགས་པའི་སྐད་ཅིག་དང་། འདོད་ཆགས་དང་བྲལ་བ་ལ་སོགས་པའི་རང་བཞིན་རྣམས་དང་། མཚན་མོ་དང་ཤེས་རབ་དང་ཟླ་བའི་སྣང་བ་ལྟ་བུ་དང་འཇུག་པའི་རྣམ་པར་ཤེས་པ་རང་གི་རང་བཞིན་དང་ལྡན་པ་རྣམས་འགོག་པར་འགྱུར་རོ། །

[Block 721]
ཡན་ལག་གི་ཚིགས་ཐམས་ཅད་ཁྱབ་པའི་དུས་སུ་སྣང་བ་མཆེད་པའི་ཡེ་ཤེས་དང་། རྣམ་པར་སྨིན་པའི་སྐད་ཅིག་མ་དང་། འདོད་ཆགས༌[^477]དང་འདོད་ཆགས་ཀྱི་རང་བཞིན་དང་བཅས་པ་དང་། ཉིན་མོ་དང་ཐབས་དང་ཉི་མའི་འོད་ཟེར་སྣང་བ་ལྟ་བུ་དང་། ཉོན་མོངས་པ་ཅན་གྱི་ཡིད་རང་གི་རང་བཞིན་དང་བཅས་པ་འགོག་པར་འགྱུར་རོ། །

[Block 722]
དེའི་རྗེས་སུ་རྡོ་རྗེའི༌[^478]ཆང་ཟུངས་སུ་གནས་པའི་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་ཐིག་ལེ་གསུམ་གྱི་བདག་ཉིད་ཀྱི་སྐབས་སུ་སྣང་བ་ཐོབ་པའི་ཡེ་ཤེས་དང་རྣམ་པར་འཇོམས་པའི་སྐད་ཅིག་མ་དང་། ཆགས་པ་བར་མ་རང་བཞིན་དང་བཅས་པ་དང་། མཚམས་ཀྱི་དུས་དང་། ཐབས་དང་ཤེས་རབ་སྙོམས་པར་ཞུགས་པ་དང་། མུན་པ་ལྟ་བུའི་སྣང་བ་དང་། ཀུན་གཞི་རྣམ་པར་ཤེས་པ་རང་གི་རང་བཞིན་བདུན་དང་བཅས་པ་འགོག་པར་འགྱུར་རོ། །

[Block 723]
དེའི་རྗེས་སུ་རྡོ་རྗེའི་ནོར་བུའི་རྩེ་མོར་བྱང་ཆུབ་ཀྱི་སེམས་ཕྱིན་པའི་གནས་སྐབས་སུ་སྔ་མ་བཞིན་དུ་རྟགས་ལྔ་སྔོན་དུ་འགྲོ་བའི་ཐབས་དང་ཤེས་རབ་དང་། ཉེ་བར་ཐོབ་པ་དང་བྲལ་བ། ཟླ་བ་དང་ཉི་མ་དང་མཚམས་ཀྱི་མུན་པའི་སྣང་བ་ལ་སོགས་པ་ཆགས་པ་དང་ཆགས་བྲལ་དང་། ཆགས་པ་བར་མ་དང་བྲལ་ཞིང་། །སྒོ་འགགས་པ་དང༌[^479]འགྲོ་བ་དང་འོང་བ་དང་བྲལ་བ་སྣང་བ་ལ་སོགས་པའི་ཡེ་ཤེས་སྤངས་པ་སྤྲིན་མེད་པའི་ནམ་མཁའ་དང་འདྲ་བའི་འོད་གསལ་བའི༌[^480]ཡེ་ཤེས་རྣལ་འབྱོར་པས་མཐོང་བར་འགྱུར་རོ། །

[Block 724]
ཇི་སྐད་དུ།

[Block 725 [VERSE]]
དེ་ཉིད་ཡེ་ཤེས་གཉིས་མེད་དེ། །
ཆོས་དབྱིངས་ཤེས་རབ་ཕ་རོལ་ཕྱིན། །

[Block 726]
ཞེས་འབྱུང་ངོ་། །

[Block 727 [VERSE]]
རབ་ཏུ་བྱེད་པ་ལས་ཀྱང་། །
སྒྱུ་མ་དག་ནི་ཐམས་ཅད་ལས། །
བུད་མེད་སྒྱུ་མ་ཁྱད་པར་འཕགས། །
ཡེ་ཤེས་གསུམ་གྱི་དབྱེ་བ་ན།[^481] །

[Block 728]
འདི་ཉིད་དུ་ནི་གསལ་བར་མཚོན། །ཞེས་འབྱུང་ངོ་། །སེམས་རྣམ་པར་དག་པའི་རིམ་པ་འདིས་རྣལ་འབྱོར་པ་ས་བཅུ་པ་ལ༌[^482]གནས་པར་འགྱུར་རོ། །

[Block 729]
རབ་ཏུ་བྱེད་པ་ལས་ཀྱང་།

[Block 730 [VERSE]]
དང་པོ་ལས་ཀྱི་སྦྱོར་བ་ཡིས། །
ས་བརྒྱད་པ་ནི་ཐོབ་པར་འགྱུར།
སྣང་བ་གསུམ་པོ་མཐོང་བ༌[^483]ནི། །
ས་བཅུ་ལ་ནི་གནས་པར་འགྱུར། །

[Block 731]
ཞེས་འབྱུང་ངོ་། །ས་བཅུའི་དབང་ཕྱུག་རྣལ་འབྱོར་པས་ཡེ་ཤེས་ལ་དབང་ཐོབ་པའི་དབང་གིས་ཀུན་ལ་དབང་བྱེད་པར་འགྱུར་རོ་ཞེས་ཕྱག་རྒྱའི་རིམ་པས་སེམས་ལ་དམིགས་པ་ཐོབ་པའོ། །

[Block 732 [HEADING]]
#### སྒྱུ་མ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་བདག་བྱིན་གྱིས་རློབ་པ། ^1-2-3-0

[Block 733]
ད༌[^484]ནི་ལུས་དང་ངག་དང་ཡིད་རྣམ་པར་དག་པས་དོན་དམ་པའི་བདེན་པ་ལ་འཇུག་པ་ཉིད་ཀྱིས་གཞན་གྱི་དོན་དང་བྲལ་བ་དང་། ཆད་པར་ཐལ་བར་འགྱུར་བ་དང་། སྔོན་གྱི་སྨོན་ལམ་གྱི་འབྲས་བུ་མེད་པ་དང་། འགྲོ་བའི་དོན་མི་བྱེད་པས་ཉན་ཐོས་ཀྱི་བྱང་ཆུབ་བཞིན་དུ་རང་གི་དོན་ཙམ་ལ་ལྟ་བ་དེ་དག་བཟློག་པར་བྱ་བའི་ཕྱིར་དང་། ཀུན་རྫོབ་ཀྱི་བདེན་པ་ཡང་དག་པར་མཐོང་བའི་ཕྱིར་སྒྱུ་མ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་ཞེས་བྱ་བ༌[^485]བདག་བྱིན་གྱིས་རློབ་པ་མྱུར་བའི་རྣམ་པས་ཡོངས་སུ་རྫོགས་པ་རྡོ་རྗེ་འཆང་ཆེན་པོའི་ཕྱག་རྒྱའི་གཟུགས་རིམ་པ་འདིས་བསྒོམ་པར་བྱའོ། །

[Block 734]
དེ་ལ་རྣལ་འབྱོར་གཉིས་ཏེ། མྱུར་བའི་རྣམ་པའི་རྣལ་འབྱོར་དང་། སྣང་བ་ཐོབ་པ་ལ་སོགས་པའི་རྣལ་འབྱོར་རོ། །

[Block 735 [HEADING]]
##### དང་པོ་མྱུར་བའི་རྣམ་པའི་རྣལ་འབྱོར། ^1-2-3-1-0

[Block 736]
དེ་ལ་དང་པོ་སེམས་རྣམ་པར་དག་པའི་རིམ་པས་འོད་གསལ་བ་ཐོབ་པ་གང་ཡིན་པ་དེ་ལས་མི་དམིགས་པའི་སྙིང་རྗེའི་དབང༌[^486]གིས་འབད་པ་མེད་པར་རྣམ་པ་ཐམས་ཅད་ཀྱི་མཆོག་དང་ལྡན་པ། ཞལ་གསུམ་པ༌[^487]ལ་སོགས་པ་དང་ལྡན་པ། རིན་པོ་ཆེ་སྣ་ཚོགས་པའི་རང་བཞིན་གཞལ་ཡས་ཁང་པ་ལ་པདྨ་དང་ཟླ་བ་ལ་སོགས་པའི་གདན་ལ་བཞུགས་པ། དེ་བཞིན་གཤེགས་པ་དང་ལྷ་མོ་དང་བྱང་ཆུབ་སེམས་དཔའ་དང༌[^488]ཁྲོ་བོའི་ཚོགས་ཀྱིས་ཡོངས་སུ་བསྐོར་བ། དེའི་བ་སྤུའི་ཁུང་བུ༌[^489]ནས་བྱུང་བའི༌[^490]འོད་ཟེར་གྱི༌[^491]འཁོར་ལོས་ཁམས་གསུམ་པ་རྣམས་ཀྱི་རེ་བ་སྐོང་བར་བྱེད་ལ། ཡིད་བཞིན་གྱི༌[^492]ནོར་བུ་དང་དཔག་བསམ་གྱི་ཤིང་བཞིན་དུ་འདོད་པའི་དོན་སྟོབས་ཀྱིས་སྟེར་བར་བྱེད་པ་སར་ཞིང་སར་པའི་དཀྱིལ་འཁོར་གྱི་འཁོར་ལོ་སྤྲོས་པས་ནམ་མཁའི་དབྱིངས་མཐའ་མེད་པ་མ་ལུས་པ་ཁྱབ་པར་བྱེད་པ། རྡོ་རྗེ་འཆང་ཆེན་པོ་ལ་སོགས་པའི་ཕྱག་རྒྱ་ཆེན་པོའི་གཟུགས་མྱུར་དུ་སྤྲོས་ཏེ། དེ་ཉིད་སྒྱུ་མ་ལ་སོགས་པའི་དཔེ་བཅུ་གཉིས་ཀྱིས་ཡང་དག་པར་བལྟས་ཏེ། ཁམས་གསུམ་ཐམས་ཅད་ཀྱང་སྒྱུ་མ་ལྟ་བུར་ཤེས་ནས་སྔགས་དང་ཕྱག་རྒྱ་ལ་སོགས་པའི་སྦྱོར་བ་དང་། རབ་ཏུ༌[^493]གནས་པ་དང་། སྦྱིན་སྲེག་དང་། དཀྱིལ་འཁོར་དང་། བཟླས་པ་དང་། སྐུ་ཁྲུས་དང་། གཏོར་མ་དང་། སྤྱན་དྲང་བ༌[^494]དང་། བཞུགས་སུ་གསོལ་བ་དང་། གཤེགས་སུ་གསོལ་བ་དང་། རིམ་པ་གཉིས་བསྒོམ་པ་ལ་སོགས་པ་དང་། ཕྲིན་ལས་ཐམས་ཅད་དང་། དེ་བཞིན་དུ་ཡང་གར་དང་གླུ་དང་རོལ་མོ་དང་། སྒེག་པ་ལ་སོགས་པ་ལོངས་སྤྱོད་པ་དང་། ཇི་སྲིད་སྤྱོད་ལམ་བཞིའི་བར་དུ་སྒྱུ་མ་དང་དྲི་ཟའི་གྲོང་ཁྱེར་དང་། བྲག་ཅ༌[^495]དང་སྨིག༌[^496]རྒྱུ་དང་། ཆུ་ཟླ་དང་མེ་ལོང་གི་གཟུགས་བརྙན་དང་། ཆུ་ཤིང་དང་སེང་གེ་ཟླ་བའི་གྲོང་ཁྱེར་ལ་སོགས་པ་དང་འདྲ་བར་བལྟ་བར་བྱའོ། །

[Block 737]
ཏིང་ངེ་འཛིན་འདི༌[^497]སྤྱོད་པར་གྱུར་པའི་རྣལ་འབྱོར་པས་རང་དང་གཞན་གྱི་དོན་ཐམས་ཅད་འབད་པ་མེད་པར་འགྲུབ་པར་འགྱུར་རོ། །

[Block 738]
བསྐལ་པ་དང་བསྐལ་པ་སྟོང་གི་བར་དུ་གནས་པར་འགྱུར་རོ་ཞེས་འདི་ནི་མྱུར་བའི་ཏིང་ངེ་འཛིན་གྱིས་བདག་བྱིན་གྱིས་རློབ་པའི་རིམ་པ་གཅིག་གོ། །

[Block 739]
[^498]

[Block 740 [HEADING]]
##### གཉིས་པ་སྣང་བ་ཐོབ་པ་ལ་སོགས་པའི་རྣལ་འབྱོར། ^1-2-3-2-0
--- END BLOCKS ---
