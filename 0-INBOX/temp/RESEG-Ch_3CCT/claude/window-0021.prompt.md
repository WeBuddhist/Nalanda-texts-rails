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

[Block 741]
རྒྱས་པར༌[^306]བཤད་པ། །སྒྱུ་མ་ལ་དམིགས་ངོ་བོ་སྟེ། །ཞེས་པ་གང་སྒྱུ་མ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་འདི་ནི་ངོ་བོའོ། །ཅིའི་ཕྱིར་ཞེ་ན།

[Block 742 [VERSE]]
སྒྱུ་མའི་དཔེ་ཡིས་ཉེར་མཚོན་ཕྱིར། །
སྒྱུ་མ་ལྟ་བུའི་སྐུ་ཞེས་བཤད། །

[Block 743]
ཅེས་པ་གང་ལ་སྒྱུ་མ་ལྟ་བུ་སྟེ། །སྒྱུ་མའི་དཔེ་བཅུ་གཉིས་ཀྱིས་ཉེ་བར་མཚོན་པའི་ཕྱིར་སྒྱུ་མ་ལྟ་བུའི་སྐུའོ། །

[Block 744]
དབྱེ་བའང་དུ་ཞིག་ཅེ་ན། གང་དུ་རིམ་དང་ཅིག་ཅར་བའམ། མང་བ་དང་ནི་ཉུང་བའོ། །ཞེས་པ་བསྐྱེད་པ་བཞིན་ཏེ་གོང་བཞིན་ནོ། །

[Block 745 [VERSE]]
ཀུན་རྫོབ་བདེན་དང་སྒྱུ་མ་དང་། །
ཡིད་ཀྱིས༌[^307]གཟུགས་ནི་རྣམ་གྲངས་སོ། །

[Block 746]
ཞེས་པ་སྒྱུ་མ་ལྟ་བུ་དང་ཀུན་རྫོབ་ཀྱི་བདེན་པ་དང་། ཡིད་ཀྱི་རང་བཞིན་གྱི༌[^308]གཟུགས་ནི་རྣམ་གྲངས་སོ། །

[Block 747]
ཆོས་དུ་དང་ལྡན་ཞེ་ན།

[Block 748 [VERSE]]
སྐུ་དང་སྒྱུ་འདྲ་ཡིད་གཟུགས་དང་། །
ཏིང་ངེ་འཛིན་དམིགས་འདི་རྣམས་སོ། །

[Block 749]
ཞེས་པ་གང་ལ་འདི་དག་དང་ལྡན་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱ་སྟེ། འདིས་ནི་གཞན་སེལ་བའང་བསྙད་དོ། །

[Block 750]
རྒྱུ་གང་ཡིན་ཞེ་ན། ཐོབ་པ་ལས་བྱུང་འདི་ནི་རྒྱུ། །ཞེས་པ་སྣང་བ་ཐོབ་པའི་ཡེ་ཤེས་འདི་ནི་སྒྱུ་མ་ལྟ་བུའི་རྒྱུའོ། །

[Block 751]
དུས་གང་གི་ཚེ་བསྒོམ་ཞེ་ན།

[Block 752 [VERSE]]
སེམས་ལ་དམིགས་པ་མཐར་ཕྱིན་ནས། །
སྒྱུ་མ་ལྟ་བུར་ཡང་དག་གནས། །

[Block 753]
ཞེས་པ་གང་གིས་བསྐྱེད་པ་སྒྱུ་མ་ལྟ་བུ་བསྒོམ་པ་ནི་སེམས་ལ་དམིགས་ནས་སོ།[^309] །ནུས་པའང་ཅི་ཡོད་ཅེ་ན། འདི་ཡིས་སྐུ་གཉིས་ཐོབ་པར་བྱེད། །ཅེས་པ་སྒྱུ་མ་ལྟ་བུ་འདིས་སྦྱངས་ནས།[^310] །ལོངས་སྤྱོད་རྫོགས་པ་དང་སྤྲུལ་པའི་སྐུ་ཐོབ་པར་བྱེད་དོ་ཞེའོ། །

[Block 754]
དེ་ལས་གཞན་ཡང་བཤད་པ།

[Block 755 [VERSE]]
གང་ཞིག་གིས་ནི་དངོས་པོ་རྣམས། །
སྒྱུ་མའི་དཔེས་ནི་ཉེར་མཚོན་ནས། །
ཕྱིས་ནི་དེ་ཡི་རྣམ་པ་ལས། །
གཞན་དུ་མི་མཐོང་མཐར་ཕྱིན་ཚད། །

[Block 756 [VERSE]]
ལུས་དང་ངག་ཡིད་སྦྱོར་བ་ཡིས། །
འདི་ཡི་སྦྱོར་བ་འགྲུབ་པ་ཡིན། །

[Block 757]
ཞེས་པ་ནི་བར་སྐབས་ཀྱི་ཚིགས་སུ་བཅད་པའོ། །

[Block 758]
དེ་ནས་འོད་གསལ་བ་བཤད་པར་བྱ་སྟེ། དེའི་ངོ་བོ་བཤད་པ།

[Block 759 [VERSE]]
གང་ཞིག་རྟོག་པ་དང་བྲལ་བ། །
དེ་ནི་འོད་གསལ་ངོ་བོའོ། །

[Block 760]
ཞེས་པ་གཟུང་བ་དང་འཛིན་པའི་རྟོག་པ་དང་བྲལ་བ་དེ་ནི་འོད་གསལ་བའི་ངོ་བོའོ། །

[Block 761]
འདི་ལ་ཅིའི་ཕྱིར་ཞེ་ན།

[Block 762 [VERSE]]
རང་བཞིན་འོད་གསལ་རྟོག་སེལ་ཕྱིར། །
འོད་གསལ་ཞེས་ནི་རྣམ་པར་བཤད། །

[Block 763]
ཅེས་པ་རང་བཞིན་གྱིས་འོད་གསལ་བའི་ཕྱིར་དང་། གང་གིས་རྟོག་པ་ཐམས་ཅད་སེལ་བའི་ཕྱིར་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 764]
དབྱེ་བའང་དུ་ཞིག་ཅེ་ན།

[Block 765 [VERSE]]
ཤེས་པ་དང་ནི་ཤེས་བྱ་ཡི། །
འོད་གསལ་བ་ནི་འདིར་བཤད་དོ། །

[Block 766]
ཞེས་པ་ཤེས་བྱ་འོད་གསལ་ནི་དབྱིངས་སོ། །ཤེས་པ་འོད་གསལ་ནི་ཡེ་ཤེས་སོ། །

[Block 767]
དེའང་གཉིས་ཏེ། རང་བཞིན་འོད་གསལ་གློ་བུར་གྱི། །དྲི་མ་དང་བྲལ་རྣམ་གཉིས་ནི།[^311] །ཞེས་པ་བཤད་ཟིན་ཏོ། །

[Block 768]
རྣམ་གྲངས་བཤད་པ།

[Block 769 [VERSE]]
འོད་གསལ་རྟོག་བྲལ་འདུས་མ་བྱས། །
རྣམ་གྲངས་ཡིན་པར་ཤེས་པར་བྱ། །

[Block 770]
ཞེས་པ་གོ་སླའོ། །

[Block 771]
ཡང་བཤད་པ།

[Block 772 [VERSE]]
སློབ་པ་དང་ནི་མི་སློབ་པས། །
འོད་གསལ་གཉིས་སུ་ཤེས་པར་བྱ། །
རིལ་པོར་འཛིན་དང་རྗེས་སུ་གཞིག །
[^312]སློབ་པའི་འོད་གསལ་ཞེས་སུ་བཤད། །

[Block 773 [VERSE]]
མི་སློབ་པ་ནི་རྟོག་དང་བྲལ། །
དམིགས་མེད་རྣམ་དག༌[^313]གདོད་ནས་དག །
རྣམ་གྲངས་དཔག་ཏུ་མེད་པ་དག །
རྒྱལ་བ་སྲས་ཀྱིས་གསུངས་པ༌[^314]ཡིན། །

[Block 774]
ཞེས་པ་ནི་བར་སྐབས་ཀྱི་ཚིགས་སུ་བཅད་པའོ། །

[Block 775]
གཞན་ཡང་།
--- END BLOCKS ---
