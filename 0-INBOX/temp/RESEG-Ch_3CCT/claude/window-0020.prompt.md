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
[Block 701 [VERSE]]
གནས་འཕོ་བ༌[^293]དང་དུ་མར་བྱེད། །
འདི་ནི་མཐར་ཕྱིན་ཚད་ཡིན་ནོ། །

[Block 702]
ཞེས་པ་ཕྲ་བའི་རླུང་རགས་པ་དང་། རགས་པའི་རླུང་ཕྲ་བར་བྱེད་པ་དང་། ཕྲ་བའི་རླུང་དང་རགས་པ་བཞིན༌[^294]དུ་མ་དང་དེ་ལས་བཟློག་པ༌[^295]ཤེས་པ་འདིའི་དུས༌[^296]སུ་དབུགས་ནང་དུ་བསྡུས་ན་གནོད་པ་མི་འབྱུང་བའོ། །

[Block 703]
གཞན་ནི།

[Block 704 [VERSE]]
གང་ཞིག་དང་པོ་གཉིས་པ་དང་། །
གསུམ་པའི་གང་ཟག་དབང་དག་ཏུ། །
དབྱིབས་དང་རླུང་དང་སྒྱུ་མར་དམིགས། །
རིགས་ཅན་ལ་ནི་འབྲས་བུ་སྐྱེ། །

[Block 705 [VERSE]]
ཀློག་དང་ཁ་དོག༌[^297]སྦྱོར་བ་མེད། །
ཕྲེང་བ་མི་དགོས༌[^298]བགྲང་མི་དགོས། །
འོན་ཀྱང་རླུང་ལ་བརྟེན་པའི་ཕྱིར། །
འདི་ནི་བཟླས་པར་བཤད་པ་སྟེ། །

[Block 706 [VERSE]]
གང་ཞིག་སྦྱོར་བ་འདི་ལ་གནས། །
ངག་གི༌[^299]དབང་ཕྱུག་ཐོབ་པར་འགྱུར། །

[Block 707]
ཞེས་པ་ནི་བར་སྐབས་ཀྱི་ཚིགས་སུ་བཅད་པའོ། །

[Block 708]
དེ་ལྟར་རྡོ་རྗེ་བཟླས་པ་རྒྱས་པར་བསྟན་ནས། ད་ནི་སེམས་ལ་དམིགས་པ་བཤད་པར་བྱ་སྟེ། དེ་ལ་སེམས་ལ་དམིགས་པ་དུ་ཞིག་ཅེ་ན་བཤད་པ།

[Block 709 [VERSE]]
གང་དུ་སེམས་ལ་དམིགས་པ་ལ། །
ངོ་བོ་དང་ནི་རྣམ་དབྱེ་དང་། །
ངེས་པའི་ཚིག་དང་རྣམ་གྲངས་དང་། །
ཆོས་རྣམས་གང་དང་ལྡན་པ་དང་། །

[Block 710]
གཞན་སེལ་རྒྱུ་དུས་ནུས་པའོ། །

[Block 711]
ངོ་བོ་ཡང་གང་ཡིན་ཞེ་ན།

[Block 712 [VERSE]]
སེམས་ལ་དམིགས་པའི་ཏིང་འཛིན༌[^300]ནི། །
རང་གི་ངོ་བོར་ཡང་དག་འདོད། །

[Block 713]
ཅེས་པ་གང་དུ་སེམས་ལ་དམིགས་པའི་ཏིང་ངེ་འཛིན་ནི་དེའི་རང་གི་ངོ་བོའོ། །ཅིའི་ཕྱིར་སེམས་ལ་དམིགས་པ་ཞེ་ན།

[Block 714 [VERSE]]
སྐུ་གསུང་ཐུགས་ཀྱི་སེམས་དཔའ་འམ། །
བྱང་ཆུབ་སེམས་ལ་དམིགས་པའམ། །
སེམས་སྣང་ཕྱིར་ནི་དེ་སྐད་བརྗོད། །

[Block 715]
ཅེས་འོག་ནས་སྟོན་ཏོ། །

[Block 716]
དབྱེ་བའང་དུ་ཞིག་ཅེ་ན།

[Block 717 [VERSE]]
རང་བཞིན་འཁྲུལ་པ་ལམ་དག་དང་། །
འབྲས་བུའི་རྣམ་པ་བཅུ་གཉིས་སོ། །

[Block 718]
ཞེས་པ་རང་བཞིན་སྣང་བ་གསུམ་དང་། འཁྲུལ་པའི་སྣང་བ་གསུམ་དང་། ལམ་གྱི་སྣང་བ་གསུམ་དང་། འབྲས་བུའི་སྣང་བ་གསུམ་མོ། །

[Block 719]
རྣམ་གྲངས་ནི།

[Block 720 [VERSE]]
སེམས་དཔའ་ལ་དམིགས་སེམས་ལ་དམིགས། །
ཡིད་དང་རྣམ་ཤེས་རྣམ་གྲངས་སོ། །

[Block 721]
ཞེས་པ་གོ་སླའོ། །

[Block 722 [VERSE]]
ཆོས་དུ་གཞན་སེལ་སྦྱོར་བ་ནི། །
ཐལ་འགྱུར་གཉེན་པོར་བརྗོད་པ་ཡིན། །

[Block 723]
ཞེས༌[^301]བཤད་ཟིན་ཏོ། །

[Block 724 [VERSE]]
རྒྱུ་ནི་བྱང་ཆུབ་སེམས་ཡིན་ཏེ། །
ཤེས་རབ་དང་ནི་སྙིང་རྗེའོ། །

[Block 725]
ཞེས་པ་གང་གིས་རྡོ་རྗེ་བཟླས་པ་མཐར་ཕྱིན་ནས། དེའི་ཡེ་ཤེས་བསྐྱེད་པ་གང་ཡིན་པ་དེ་ནི་དེའི་རྒྱུའོ། །

[Block 726]
དུས་ནི་བཟླས་པ་མཐར་ཕྱིན་པའོ། །ཞེས་པ་གང་གི་ཚེ་རྡོ་རྗེ་བཟླས་པ་མཐར་ཕྱིན་ནས། དེའི་དུས་སུ་བྱེད་པ་གང་ཡིན་པ་དེ་ནུས༌[^302]སོ། །

[Block 727 [VERSE]]
ནུས་པའང་ཅི་ཡོད་ཅེ་ན། །
སེམས་ཀྱི་དྲི་མ་འཁྲུ་བར་བྱེད། །

[Block 728]
ཅེས་པ༌[^303]སེམས་ཀྱི་འཁྲུལ་པ་གང་གིས་སྤོང་བར་ནུས་པ་དེ་ནི་ནུས་པའོ། །

[Block 729]
གཞན་ཡང་།

[Block 730 [VERSE]]
བསྐྱེད་པའི་སྐུ་ལ་རྟག་གནས་ཤིང་། །
རྡོ་རྗེ་བཟླས་པ་མཐར་ཕྱིན་ནས།
སྙིང་གར་སེམས་གསུམ་མཚན་མའམ། །
འོད་ཀྱི་ཐིག་ལེ་གསལ་བ་ནི། །

[Block 731 [VERSE]]
སྣང་བ་ཟླ་བ་ལྟ་བུའོ། །
དེ་ལས་འོད་བྱུང་བདག་དང་བཅས། །
ཞུ་བ་སྣང་བ་མཆེད་པ་སྟེ། །
ཉི་མ་ལྟ་བུའོ༌[^304]འདུས་པ་ནི། །

[Block 732 [VERSE]]
སྣང་བ་ཐོབ་པ་ཞེས་སུ་བཤད། །
དམིགས་པའི་དབང་དུ་བཤད་པའོ། །
སྤྱི་བོ་མགྲིན་པ་སྙིང་གའམ། །
ཡང་ན་གསང་བའི་ཆ་ལ་གནས། །

[Block 733 [VERSE]]
གནས་ཀྱི་རྣམ་པར་གནས་པའོ། །
སྐད་ཅིག་ལ་སོགས་རྣམ་པ་ལ། །
གནས་པ་དུས་ཀྱི་སྣང་བའོ། །
ཟླ་བ་ཉི་མ་ནུབ་པའི་ཚུལ། །

[Block 734 [VERSE]]
དཔེ་ཡི་དབང་དུ་བྱས་པའོ། །
མངལ་ལ་སོགས་པའི་རིམ་པ་ལ། །
ཤེས་པ་འཕེལ་བར་གྱུར་པ་དང་། །
གང་ཞིག་དམིགས་པ་ལ་སོགས་པ། །

[Block 735]
དུས་ལས་འཁྲུལ་པ་འབྱུང་བར་འགྱུར། །ཞེས་པ་ནི་བར་སྐབས་ཀྱི་ཚིགས་སུ་བཅད་པའོ། །

[Block 736]
གཞན་ཡང་།

[Block 737 [VERSE]]
འཁྲུལ་བ་རྣམས་ལ་རྒྱུ་དང་རྐྱེན། །
འབྲས་བུ་སྐྱེ་བའི་རིམ་པ་དང་། །
གང་ཞིག་སྣང་བ་གསུམ་པོ་དག །
འབྱུང་ངོ་འོད་གསལ་ངང་ལས་དང་། །

[Block 738 [VERSE]]
ཐོབ་པས་ལུགས་ལས་བཟློག་པ༌[^305]དང་། །
འདི་དག་འབྲས་བུའི་སྣང་བའོ། །
སེམས་ནི་རླུང་ལ་ཞོན་པ་ཡིས། །
རང་བཞིན་འདི་དག་འབྱུང་བ་ཡིན། །

[Block 739]
ཞེས་པ་ནི་བར་སྐབས་ཀྱི་ཚིགས་སུ་བཅད་པའོ། །

[Block 740]
དེ་ལྟར་སེམས་ལ་དམིགས་པ་རྒྱས་པར་བཤད་ནས། ད་ནི་སྒྱུ་མ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་བཤད་པར་བྱ་སྟེ། དེ་ལ། སེམས་དམིགས་སྦྱོར་བ་གོང་བཞིན་ཏེ། །ཞེས་པ་ངོ་བོ་ལ་སོགས་པ་གོང་བཞིན་ནོ། །
--- END BLOCKS ---
