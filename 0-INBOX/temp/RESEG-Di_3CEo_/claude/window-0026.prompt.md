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
[Block 911 [HEADING]]
#### དུས་ངེས་པ། ^2-3-2-0

[Block 912]
དུས་ངེས་པ་མ་བཤད་པས་དེ་བརྗོད་པ། ཀུན་འགྲོ༌[^346]སྐལ་མཉམ་དུས་གཉིས་པ། །འདས་པ་དང་ད་ལྟར་བྱུང་བ་ཁོ་ནའོ། །

[Block 913]
གསུམ་པོ་དག་ནི་དུས་གསུམ་པ། །ལྷན་ཅིག་འབྱུང་བ་དང་མཚུངས་པར་ལྡན་པ་རྣམས་དང་། རྣམ་པར་སྨིན་པའི་རྒྱུ་དག་ནི་དུས་གསུམ་པ་ཡིན་ནོ། །

[Block 914 [HEADING]]
#### འབྲས་བུ། ^2-3-3-0

[Block 915]
རྒྱུ་དེ་དག་གང་ཡིན་པའི་འབྲས་བུ་དེ་དག་གང་ཞེ་ན། འདུས་བྱས་བྲལ་བཅས་འབྲས་བུ་ཡིན། །དེ་ལྟ་ན་འོ་ན་ནི་འདུས་མ་བྱས་འབྲས་བུ་ཡིན་པའི་ཕྱིར་དེ་དག་གི་འབྲས་བུ་ཡིན་པའི་རྒྱུར་ཡང་འགྱུར་ལ། རྒྱུ་ཡིན་པའི་ཕྱིར་དེ་དག་གི་རྒྱུ་ཡིན་པའི་འབྲས་བུར་ཡང་འགྱུར་རོ། །

[Block 916]
འདུས་བྱས་ཁོ་ན་ལ་རྒྱུ་དང་འབྲས་བུ་ཡོད་ཀྱི། འདུས་མ་བྱས་ལ་དེ་དག་མེད། །རྒྱུ་རྣམ་པ་དྲུག་མི་སྲིད་པའི་ཕྱིར་དང་། འབྲས་བུ་རྣམ་པ་ལྔ་མི་སྲིད་པའི་ཕྱིར་རོ། །

[Block 917]
ཡང་འབྲས་བུ་འདི་དག་ལས་འབྲས་བུ་གང་ཞིག་རྒྱུ་གང་གི་ཡིན་ཞེ་ན། རྣམ་སྨིན་འབྲས་བུ་ཐ་མའི་ཡིན། །རྣམ་པར་སྨིན་པའི་རྒྱུ་ནི་རྣམ་པར་སྨིན་པའི་འབྲས་བུའོ། །

[Block 918 [VERSE]]
བདག་པོའི་འབྲས་བུ་དང་པོའི་ཡིན། །
བྱེད་རྒྱུའི༌[^347]ནི་བདག་པོའི་འབྲས་བུའོ། །
རྒྱུ་མཐུན་སྐལ་མཉམ་ཀུན་འགྲོ་བའི།[^348] །

[Block 919]
འདི་གཉིས་དང་འདྲ་བའི་འབྲས་བུ་ཡིན་པའི་ཕྱིར་རྒྱུ་མཐུན་པའི་འབྲས་བུ་ཡིན་ནོ། །

[Block 920]
སྐྱེས་བུ་པ་ནི་གཉིས་ཀྱི་ཡིན། །སྐྱེས་བུ་བྱེད་པའི་འབྲས་བུ་ནི་ལྷན་ཅིག་འབྱུང་བ་དང་མཚུངས་པར་ལྡན་པའི་རྒྱུ་དག་གི༌[^349]ཡིན་ནོ། །

[Block 921]
ཡང་རྣམ་པར་སྨིན་པའི་འབྲས་བུ་འདི་ཅི་ཡིན། བདག་པོའི་འབྲས་བུའི་བར་དུ་ཡང་ཅི་ཞིག་ཡིན་ཞེ་ན།

[Block 922 [VERSE]]
རྣམ་སྨིན་ལུང་དུ་མ་བསྟན་ཆོས། །
སེམས་ཅན་བརྗོད་ལུང་བསྟན་ཕྱིས་འབྱུང་། །

[Block 923]
ཅིའི་ཕྱིར་སེམས་ཅན་དུ་སྟོན་པ་མ་ཡིན་པའི་དོན་ལས་ལས་སྐྱེས་པ་མ་ཡིན་ནམ་ཞེ་ན། ཐུན་མོང་བའི་ཕྱིར་རོ། །

[Block 924]
ལུང་བསྟན་ཕྱིས་འབྱུང་བ་ནི་དགེ་བ་དང་མི་དགེ་བ་ལས་འབྱུང་བའོ། །

[Block 925]
རྒྱུ་མཐུན་རྒྱུ་དང་འདྲ་བའོ། །

[Block 926]
རྒྱུ་དང་འདྲ་བའི་ཆོས་གང་ཡིན་པ་དེ་ནི་རྒྱུ་མཐུན་པའི་འབྲས་བུའོ། །

[Block 927]
བྲལ་བ་བློ་ཡིས་ཟད་པའོ། །

[Block 928]
སོ་སོར་བརྟགས་པས་འགོག་པ་ནི་བྲལ་བའི་འབྲས་བུའོ། །

[Block 929 [VERSE]]
གང་གི་སྟོབས་ཀྱིས་གང་སྐྱེ་བའི།[^350] །
འབྲས་དེ་སྐྱེས༌[^351]བུའི་བྱེད་ལས་སྐྱེས། །

[Block 930]
དཔེར་ན་ས་འོག་མའི་སྦྱོར་བའི་སེམས་ཀྱིས་ས་གོང་མའི་ཏིང་ངེ་འཛིན་དང་། ཟག་པ་དང་བཅས་པའམ།[^352] ཟག་པ་མེད་པ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 931 [VERSE]]
སྔོན་བྱུང་མ་ཡིན་འདུས་བྱས་ནི། །
འདུས་བྱས་ཁོ་ནའི་བདག་པོའི་འབྲས། །

[Block 932]
སྔར་བྱུང་བ་ལས་གཞན་པའི་འདུས་བྱས་ཀྱི་ཆོས་ནི་འདུས་བྱས་ཐམས་ཅད་ཀྱི་བདག་པོའི་འབྲས་བུ་ཡིན་ནོ། །

[Block 933]
ཡང་རྒྱུ་འདི་དག་ལས་གང་ཞིག་དུས་གང་དུ་འབྲས་བུ་འཛིན་ཏམ་འབྱིན་ཅེ་ན། ལྔ་པོ་ད་ལྟ་འབྲས་བུ་འཛིན། །ཡོངས་སུ་བཟུང་ཟིན་པའི་ཕྱིར་འདས་པ་རྣམས་ཀྱང་མ་ཡིན་ལ། སྐྱེས་བུ་བྱེད་པ་མེད་པའི་ཕྱིར་མ་འོངས་པ་རྣམས་ཀྱང་མ་ཡིན་ནོ། །

[Block 934]
གཉིས་ནི་རབ་ཏུ་འབྱིན་པར་བྱེད། །ལྷན་ཅིག་འབྱུང་བ་དང་། མཚུངས་པར་ལྡན་པའི་རྒྱུ་དག་ནི་ད་ལྟར་འབྲས་བུ་འབྱིན་པར་བྱེད་དོ། །

[Block 935]
ད་ལྟར་གྱི་དང་འདས་པ་དག །གཉིས་ཁོ་ན་སྐལ་པ་མ་ཉམ་པ་དང་། ཀུན་དུ་འགྲོ་བའི་རྒྱུ་དག་གོ། །

[Block 936]
ད་ལྟར་བདག་ཀྱང་མཇུག་ཐོགས་སུ་སྒྲུབ་པའི་ཕྱིར་ཏེ།

[Block 937 [VERSE]]
དེ་ཡང་ཕྱིས་འདས་པ་དག་གོ། །
གཅིག་ནི་འདས་པས་འབྱིན་པར་འགྱུར། །

[Block 938]
འདི་ལྟར་ལྷན་ཅིག་གམ་དེ་མ་ཐག་ཏུ་རྣམ་པར་སྨིན་པའི་འབྲས་བུ་ནི་མེད་དོ། །

[Block 939]
དེ་ལ་ཆོས་གང་ཞིག་རྒྱུ་དུས༌[^353]དག༌[^354]གིས་སྐྱེད་པར་བྱེད་ཅེ་ན། སྨྲས་པ། མདོར་བསྡུ་ན། ཆོས་རྣམས་ནི་རྣམ་པ་བཞི་པོ་དག་ཡིན་ཏེ། ཆོས་ཉོན་མོངས་པ་ཅན་རྣམས་དང་། རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པ་རྣམས་དང་། ཟག་པ་མེད་པའི་དང་པོ་རྣམས་དང་། དེ་དག་གི་ལྷག་མ་རྣམས་ནི་རྣམ་པར་སྨིན་པ་ལས་མ་གཏོགས་པའི་ལུང་དུ་མ་བསྟན་པ་རྣམས་དང་། ཟག་པ་མེད་པའི་སྐད་ཅིག་མ་དང་པོ་མ་གཏོགས་པའི་དགེ་བ་རྣམས་སོ། །

[Block 940]
དེ་དག་ནི།

[Block 941 [VERSE]]
ཉོན་མོངས་ཅན་དང་རྣམ་སྨིན་སྐྱེས། །
ལྷག་དང་དང་པོ་འཕགས་རིམ་བཞིན། །
རྣམ་སྨིན་ཀུན་འགྲོ་དེ་གཉིས་དང་། །
སྐལ་མཉམ་མ་གཏོགས་ལྷག་ལས་སྐྱེས། །

[Block 942]
ཆོས་ཉོན་མོངས་པ་རྣམས་ནི་རྣམ་པར་སྨིན་པའི་རྒྱུ་མ་གཏོགས་པ་ལྷག་མ་རྣམས་ལས༌[^355]སྐྱེའོ། །

[Block 943]
རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པ་རྣམས་ནི་ཀུན་འགྲོའི་རྒྱུ་མ་གཏོགས་པ་ལྷག་མ༌[^356]རྣམས་ལས་སོ། །

[Block 944]
ཆོས་ལྷག་མ་རྣམས་ནི་རྣམ་པར་སྨིན་པ་དང་། ཀུན་དུ་འགྲོ་བའི་རྒྱུ་དེ་དག་མ་གཏོགས་པ་ལྷག་མ་རྣམས་ལས་སོ། །

[Block 945]
ཟག་པ་མེད་པའི་དང་པོ་རྣམས་ནི་དེ་དག་དང་སྐལ་བ་མཉམ་པའི་རྒྱུ་མ་གཏོགས་པ་ལྷག་མ་རྣམས་ལས་སྐྱེའོ། །

[Block 946]
ཆོས་བསྟན་པ་དེ་དག༌[^357]གང་ཡིན་སྙོམ་པ༌[^358]ལ། སེམས་དང་སེམས་ལས་བྱུང་བ་ཡིན།[^359] །འོ་ན་གང་དག་སེམས་དང་ལྡན་པ་མ་ཡིན་པ་དང་། གཟུགས་ཅན་གྱི་ཆོས་དེ་དག་ཇི་ལྟ་བུ་ཞེ་ན། མཚུངས་ལྡན་མ་གཏོགས་གཞན་དེ་བཞིན། །མཚུངས་པར་ལྡན་པའི་རྒྱུ་གཅིག་པུ་མ་གཏོགས་པ་ཆོས་ཉོན་མོངས་པ་ཅན་ལ་སོགས་པ་སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་ཇི་ལྟ་བ་དེ་ཁོ་ན་བཞིན་དུ་སྐྱེ་སྟེ། རྒྱུ་རྒྱ་ཆེར་བཤད་པ་རྫོགས་སོ།། །།

[Block 947 [HEADING]]
#### རྐྱེན་བཞི། ^2-3-4-0

[Block 948]
རྐྱེན་རྣམས་གང་ཞེ་ན། རྐྱེན་ནི་བཞི་པོ་དག་ཏུ་གསུངས། །

[Block 949]
གང་ནས་གསུངས་ཤེ་ན། མདོ་ལས་རྐྱེན་ཉིད་ནི་བཞི་སྟེ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 950]
དེ་ལ་རྒྱུ་ཞེས་བྱ་བ་རྒྱུ་ལྔ་ཡིན། །བྱེད་རྒྱུའི་རྒྱུ་མ་གཏོགས་པ་རྒྱུ་ལྔ་ནི་རྒྱུའི་རྐྱེན་ཡིན་ནོ། །
--- END BLOCKS ---
