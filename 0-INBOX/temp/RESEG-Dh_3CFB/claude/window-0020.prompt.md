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
འཁྲུལ་པའི་དབང་གིས་དེ་ལྟར་སྣང་བ་ལ་ནི་འགལ་བ་མེད་དོ། །

[Block 702]
གལ་ཏེ་རྒྱུ་མཚན་མེད་པའི་ཕྱིར་འཁྲུལ་པར་རིགས་པ་མ་ཡིན་ནོ་ཞེ་ན། དངོས་པོ་དོན་དེ་གཅིག་བྱེད་པ་དེ་དག་ཉིད༌[^550]ཉམས་སུ་མྱོང་བའི་སྒོ་ནས་རང་བཞིན་གྱིས༌[^551]འཁྲུལ་པའི་འབྲས་བུ་ཅན་གྱི་རྣམ་པར་རྟོག་པའི་བག་ཆགས་ཀྱི་རྒྱུ་ཡིན་པའི་ཕྱིར་རྒྱུ་མཚན་ཡིན་ནོ། །

[Block 703]
སྨིག་རྒྱུ་ལ་སོགས་པ་ལ་ཆུ་ལ་སོགས་པར་འཁྲུལ་པའི་རྒྱུ་ཡང་ཐ་དད་ཀྱང་རྣམ་པ་ཐ་མི་དད་པར་བསྙེམས་པའི༌[^552]ཤེས་པའི་རྒྱུ་མཚན་ཉམས་སུ་མྱོང་བ་སྐྱེད་པར་བྱེད་པའི་ངོ་བོ་དེ་དག་ཉིད་ཡིན་ནོ། །

[Block 704]
དེ་ལ་གང་དེ་ལྟར་ཤེས་པར་འགྱུར་བ་གཞན་སྤྱི་ནི་ཅུང་ཟད་ཀྱང་མེད་པ་ཁོ་ནའོ། །

[Block 705]
འོན་ཏེ་ཡོད་ན་ནི་དོན་ཡོད་པ་འཛིན་པའི་བློ་འཁྲུལ་པར་མི་འགྱུར་རོ། །

[Block 706]
གལ་ཏེ་ཡང་དག་པ་མ་ཡིན་པའི་རྣམ་པ་སྒྲོ་འདོགས་པའི་ཕྱིར་འཁྲུལ་པ་ཡིན་ནོ་ཞེ་ན། འོ་ན་ནི་དེས་དེ་དག་གི་སྤྱི་འཛིན་པ་མ་ཡིན་ཏེ། དེས་རྣམ་པ་གང་ཁོ་ན་སྒྲོ་འདོགས་པར་བྱེད་པ་དེ་ཉིད་འདིའི་ཡུལ་ཡིན་ནོ། །

[Block 707]
ཡུལ་དུ་མ་བྱས་པ་ལ་ནི་སྒྲོ་གདགས་པར་མི་ནུས་པའི་ཕྱིར་ཏེ། རྣམ་པ་གཞན་བཞིན་ནོ། །

[Block 708]
དེ་ཡང་དེ་ལ་མེད་པས་སྤྱི་མ་ཡིན་ནོ། །

[Block 709]
གལ་ཏེ་སྤྱི་འཛིན་པ་ཡོད་ན་དེར་སྒྲོ་འདོགས་ཀྱི་གཞན་དུ་ནི་མ་ཡིན་ཏེ། [^553]ཧ་ཅང་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ་ཞེ་ན། འབྲས་བུ་གཅིག་བྱེད་པ་ཅན་འཛིན་པ་ཡོད་ན་ཅི་སྟེ་མི་འདོད། སྤྱི་འདོད་པས་ཀྱང་གདོན་མི་ཟ་བར་བསལ་བ༌[^554]རྣམས་ཀྱི་དོན་གཅིག་བསྐྱེད་པའི་ནུས་པ་ནི་འདོད་པར་བྱ་དགོས་སོ། །

[Block 710]
དེའི་ཕྱིར་གཞན་དག་ལས་ཐ་དད་པ་དེ་དག་ཁོ་ནས་ཤེས་པ་དེ་ལྟ་བུ་བསྐྱེད་ན། དེ་ལ་སྤྱིས་ཅི་ཞིག་བྱ། གལ་ཏེ་དངོས་པོ་ཇི་ལྟ་བ་བཞིན་ཁྱད་པར་མ་འདྲེས་པ་ཅན་ཁོ་ན་ཅི་སྟེ་མི་རྟོགས་ཤེ་ན། མ་རིག་པའི་མཐུས་རྣམ་པར་རྟོག་པ༌[^555]རྣམས་ལ་ནུས་པ་འདི་མེད་དོ། །

[Block 711]
ཕྱི་རོལ་གྱི་དོན་ཁོ་ན་ལ་ལྟོས་ནས་འཁྲུལ་པར་འགྱུར་བ་ཡང་མ་ཡིན་གྱི།[^556] འོན་ཀྱང་ནང་གི་བསླད་པ་ལས་ཀྱང་འགྱུར་ཏེ། སྐྲ་ལ་སོགས་པར་འཁྲུལ་པ་བཞིན༌[^557]ནོ། །

[Block 712]
མ་རིག་པ་ལས་འབྱུང་བའི་ཕྱིར་བསླད་པ་ཡིན་ན་མིག་ལ་སོགས་པ་ལ་ཡང་ཐལ་བར་འགྱུར་རོ་ཞེ་ན། མ་ཡིན་ཏེ། དེའི་མཚན་ཉིད་ནི་རྣམ་པར་རྟོག་པ༌[^558]མེད་པའི༌[^559]ཕྱིར་རོ། །

[Block 713]
རྣམ་པར་རྟོག་པ་ཉིད་མ་རིག་པ་ཡིན་ཏེ། དེ་ནི་ངོ་བོ་ཉིད་ཁོ་ནས་ཕྱིན་ཅི་ལོག་པ་ཡིན་ནོ། །

[Block 714]
དབང་པོའི་ཤེས་པ་རྣམས་ནི་དེ་ལྟར་རྣམ་པར་རྟོག་པ་མ་ཡིན་ནོ། །

[Block 715]
ཡང་ན་དེ་དག་ལའང་འདི་ཉེས་པ་མེད་དེ། གཉིས་མེད་པ་དེ༌[^560]དག་གཉིས་སུ་སྣང་བའི་ཕྱིར་རོ། །ཞེས་བཤད་པར་བྱའོ། །

[Block 716]
ཐམས་ཅད་བསླང་བ་ཡིན་ཡང་ཚད་མ་དང་དེར་སྣང་བའི་རྣམ་པར་གཞག་པ་ནི་ཇི་སྲིད་གནས་གྱུར་པ་མ་ཡིན་གྱི། བར་དུ་དོན་བྱེད་པར་རུང་བ་དང་འདོད་པ་ཐོབ་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 717]
ནོར་པ་ཉིད་ཡིན་ཡང་རབ་ཏུ་ཞི་པ་དང་མཐུན་པའི་ཕྱིར་ཏེ། མ་ལ་སོགས་པར་འདུ་ཤེས་པ་བཞིན་ནོ། །

[Block 718]
སྨིག་རྒྱུ་ལ་ཆུར་འདུ་ཤེས་པ་དང་། གཞན་དངོས་པོ་ཐ་དད་པ་ལས་སྐྱེ་བ་དང་འཁྲུལ་པར་ཁྱད་པར་མེད་ཀྱང་མངོན་པར་འདོད་པའི་དོན་བྱ་བར་རུང་བ་དང་། མི་རུང་བ་ལས་སྐྱ་བའི༌[^561]ཕྱིར་དོན་ཐོབ་པར་བྱེད་པ་དང་། ཅིག་ཤོས་དག་ཡིན་ནོ། །

[Block 719]
གལ་ཏེ་མི་རུང་བ་ལས་ཇི་ལྟར་སྐྱེ་ཞེ་ན། རྣམ་པར་རྟོག་པ་རྣམས་དོན་དང་འབྲེལ་པར་ངེས་པ་མེད་པའི་ཕྱིར་ཏེ། རྣམ་པར་རྟོག་པ་རྣམས་ནི་དོན་ཇི་ལྟ་བ་བཞིན་སྐྱེ་བ་མེད་པ་ཉིད་དོ། །

[Block 720]
སྨིག་རྒྱུར་མཐོང་བ་ཡོད་ན་ཆུར་འཁྲུལ་པར་འགྱུར་བས༌[^562]དེ་ལས་སྐྱེ་བ་ཞེས་བྱའི་ཆུ་མ༌[^563]ཡིན་པ་དང་བྲལ་བའི་དོན་གྱི་རང་གི་ངོ་བོ་ཇི་ལྟ་བ་བཞིན་རང་གི་ངོ་བོའི་རྗེས་སུ་བྱེད་པ་འཇོག་པས་བསྐྱེད་པའི་ཕྱིར་ནི་མ་ཡིན་ནོ། །

[Block 721]
དེ་ནི་ཁྱད་པར་མཚོན་པ་ལ་མི་བསལ་བའི༌[^564]ཕྱིར། རང་གི་བག་ཆགས་སད་པ་རྐྱེན་ལ་ལྟོས་པས༌[^565]བསྐྱེད་དོ། །

[Block 722]
དེ་ལྟ་བས་ན་འཁྲུལ་པའི་རྣམ་པར་རྟོག་པ་དངོས་པོ་ཐ་དད་པ་ལས་སྐྱེ་བ༌[^566]ཅན་འཁྲུལ་པ་ལས་དེ་ཉིད་འདི་ཡིན་ནོ་སྙམ་དུ་ངོ་ཤེས་པ་ཡིན་ཏེ། སྤྱི་ཐ་དད་པ་མཐོང་བ་ལས་ནི་མ་ཡིན་ནོ། །

[Block 723]
ཐ་མི་དད་པ་ཡང་མ་ཡིན་ཏེ། བསལ་བ༌[^567]བཞིན་དུ་རྗེས་སུ་འགྲོ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 724]
གཞན་ཡང་།

[Block 725 [VERSE]]
གཞན་གྱི་ལྟར་ནའང་བློ་དེ་ནི། །
སྤྱི་ནི་འབའ་ཞིག་ཉིད་ལས་ཡིན། །

[Block 726]
གཞན་གྱིས༌[^568]ཀྱང་བློ་འདི་ནི་སྤྱི་འབའ་ཞིག་ལས་འབྱུང་བར་བརྗོད་པར་རིགས་པ་མ་ཡིན་ཏེ།

[Block 727 [VERSE]]
རྟག་ཏུ་དེ་ཙམ་རྣམ་ཤེས་ན། །
བསལ་བ༌[^569]མི་ཤེས་ཐལ་འགྱུར་ཕྱིར། །

[Block 728]
གལ་ཏེ་བློ་འདིས་རྟག་ཏུ་སྤྱི་ཁོ་ན་འཛིན་པར་བྱེད་ན་ཤེས་པ་འདིས་བསལ་བ༌[^570]མི་རྟོགས་པ་ཁོ་ནར་འགྱུར་རོ། །

[Block 729 [VERSE]]
དེ་ཡི་ཚེ་ན་ནམ་ཡང་ནི། །
དེ་ལྡན་འབྲེལ་པ་མ་བཟུང་ན། །
དེ་དང་ལྡན་ངེས་མི་འགྱུར་ན། །
དེ་ལས་ཇི་ལྟར་ཐ་སྙད་འདོགས། །

[Block 730]
གང་གི་ཚེ་སྤྱི་འཛིན་པའི་རྣམ་པར་ཤེས་པས་ཁྱད་པར་རྣམས་དམིགས་པ་ཉིད་དུ་ཉེ་བར་མི་སྦྱོར་བ་དེའི་ཚེ་ནམ་ཡང་དེ་དག་འབྲེལ་པར་མ་བཟུང་བས་འདི་ནི་འདིའི་སྤྱིའོ། །

[Block 731]
འདི་ནི་དེ་དང་ལྡན་པའོ་ཞེས་བྱ་བར་ཡང༌[^571]མི་འགྱུར་རོ། །

[Block 732]
དེ་ལྟ་ན་ནི་དེ་རྟོགས་པས་དེ་དང་ལྡན་པ་ལ་འཇུག་པར་མི་འགྱུར་ཏེ། དོན་གཞན་བཞིན་ནོ། །

[Block 733 [VERSE]]
གལ་ཏེ་དངོས་གཅིག་གྲོགས་བྱེད་པའི། །
བསལ༌[^572]རྣམས་ཤེས་པའི་རྒྱུ་ཞེ་ན། །

[Block 734]
གལ་ཏེ་འདི་སྙམ་དུ་བསལ་བ༌[^573]རྣམས་ནི་དེའི་དམིགས་པའི་དངོས་པོའི༌[^574]རྒྱུ་ཡིན་ལ། འབའ་ཞིག་པ་རྣམས་ནི་མ་ཡིན་ཏེ། གང་གི་ཚེ་འདི་དག་ལ་གཅིག་ལྷན་ཅིག་བྱེད་པ་ཡོད་པ་དེའི་ཚེ་དེ་དང་ལྷན་ཅིག་ཏུ་འཛིན་ཏོ་སྙམ་དུ་སེམས་ན།

[Block 735 [VERSE]]
དངོས་པོ་གཅིག་དེས་དེ་རྣམས་ཀྱི། །
ཐ་དད་པ་ཉིད་སེལ་ཏམ་ཅི། །
[^575]ཐ་དད་ཕྱིར་ནི་དེ་དག་ལ། །
གཅིག་རྣམ༌[^576]ཤེས་ཀྱི་རྒྱུར་མི་འདོད། །

[Block 736]
གཅིག་པུ་དེས་དེ་རྣམས་ཀྱི་ཐ་སྙད་པ་ཉིད་སེལ་ཏམ། ཅི་སྟེ་ཐ་དད་པ་ཉིད་ནི་དེ་དག་ལ་གཅིག་གི་རྣམ་པར་ཤེས་པ་མི་བསྐྱེད་པ༌[^577]ཉིད་ཀྱི་རྒྱུ་ཡིན་པར་བརྗོད་དོ། །

[Block 737 [VERSE]]
གལ་ཏེ་དུ་མའང་གཅིག་ལྟོས་ནས། །
ཐ་དད་མིན་བློ་སྐྱེད་ཅེ་ན། །

[Block 738]
ཐ་དད་པའི་ཕྱིར་དུ་མས་གཅིག་གི་ཤེས་པ་མི་བསྐྱེད་དོ་ཞེས་ནི་མི་སྨྲ་སྟེ། ཐ་དད་པས་སྐྱེ་བ་ལ་འགལ་བ་མེད་དོ། །

[Block 739]
འོ་ན་ཅི་ཞེ་ན། བྲལ་བས་འགལ་ཏེ། དེས་ན་གཅིག་དང་ལྷན་ཅིག་པས་སྐྱེད་པར༌[^578]བྱེད་པ་ཁོ་ནའོ་ཞེ་ན། དེ་ལྟར་ན་འོ་ན་ནི།

[Block 740 [VERSE]]
དེ་དག་རེ་རེ་མེད་པར་ཡང་། །
དེ་གཅིག་གིས་ཀྱང་བསྐྱེད་བྱ་བའི། །
བློ་ལ་དེ་རྣམས་ནུས་མེད་ཕྱིར། །
བློ་ཡིས་འཛིན་པ་མེད་པ་ཡིན། །
--- END BLOCKS ---
