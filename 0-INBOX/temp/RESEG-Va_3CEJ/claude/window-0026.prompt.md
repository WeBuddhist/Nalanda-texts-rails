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
[Block 911 [VERSE]]
རང་གི་དོན་དང་ཐམས་ཅད་ལ། །
དམིགས་པར་དབང་བྱེད༌[^406]ཕྱིར་དབང་དྲུག །

[Block 912]
མིག་ལ་སོགས་པ་ལྔ་པོ་དག་ནི་རང་རང་གི་དོན་ལ་དམིགས་པར་བྱ་བ་ལ་དབང་བྱེད་དོ། །

[Block 913]
ཡིད་ནི་དོན་ཐམས་ཅད་ལ་དམིགས་པར་བྱ་བ་ལ་དབང་བྱེད་དེ། དེའི་ཕྱིར་དེ་དག་ནི་སོ་སོར་དབང་པོ་ཡིན་ནོ། །

[Block 914]
འདི་ལ་དོན་རྣམས་ཀྱང་དབང་བྱེད་པ་མ་ཡིན་ནམ་ཞེ་ན། དབང་བྱེད་པ་མ་ཡིན་ཏེ། ལྷག་པར་དབང་བྱེད་པ་ཉིད་ནི་དབང་བྱེད་པ་ཉིད་ཡིན་ལ། མིག་ནི་གཟུགས་ཐམས་ཅད་ལ་དམིགས་པར་བྱ་བ་ལ་ཐུན་མོང་གི་རྒྱུ་ཡིན་པའི་ཕྱིར་དང་། དམིགས་པ་དེ་གསལ་བ་དང་མི་གསལ་བ་ཉིད་ལ་སོགས་པའི་རྗེས་སུ་བྱེད་པའི་ཕྱིར་གཟུགས་ལ་དམིགས་པར་བྱ་བ་ལ་ལྷག་པར་དབང་བྱེད་པ་ཡིན་གྱི། དེ་ལས་བཟློག་པ་ཡིན་པའི་ཕྱིར་གཟུགས་ཀྱི་ནི་མ་ཡིན་ཏེ། ཡིད་ཆོས་རྣམས་ལ་དབང་བྱེད་པའི་བར་དུ་ཡང་དེ་བཞིན་དུ་སྦྱར་རོ། །

[Block 915 [VERSE]]
མོ་ཉིད་ཕོ་ཉིད་ལས་དབང་ཕྱིར། །
ལུས་ལས་མོ་དང་ཕོའི་དབང་དག །

[Block 916]
ལུས་ཀྱི་དབང་པོ་ཁོ་ན་ལས་མོ་དང་ཕོའི་དབང་པོ་དག་རྣམ་པར་བཞག་སྟེ། དོན་ཐ་དད་པར་གྱུར་པ་དག་ནི་མེད་ཀྱི་ལུས༌[^407]ཀྱི་དབང་པོའི་ཆ་འགའ་སྟེ། མདོམས་ཀྱི་ཕྱོགས་མོ་དང་ཕོའི་དབང་པོའི་མིང་འཐོབ་པ་གང་ཡིན་པ་དེ་ནི་རིམ༌[^408]བཞིན་དུ་མོ་ཉིད་དང་ཕོ་ཉིད་དག་ལ་དབང་བྱེད་པའི་ཕྱིར་རོ། །

[Block 917]
དེ་ལ་མོའི་ངོ་བོ་ནི་རང་བཞིན་ང་རོ་དང་གཡོ་བ་དང་བསམ་པ་དག་སྟེ། དེ་ནི་མོའི་མོ་ཉིད་ཡིན་ནོ། །

[Block 918]
ཕོའི་ངོ་བོ་ནི་རང་བཞིན་ང་རོ་དང་གཡོ་བ་དང་བསམ་པ་དག་པ་དག༌[^409]སྟེ།

[Block 919 [VERSE]]
དེ་ནི་ཕོའི་ཕོ་ཉིད་ཡིན་ནོ། །
རིགས་གནས༌[^410]ཀུན་ནས་ཉོན་མོངས་དང་། །
རྣམ་པར་བྱང་ལ་དབང་བྱེད་ཕྱིར། །
སྲོག་དང་ཚོར་བ་རྣམས་དང་ནི། །

[Block 920]
དད་སོགས་དབང་པོ་ལྔར་འདོད་དོ། །

[Block 921]
སྲོག་གི་དབང་པོ་ནི་རིས༌[^411]མཐུན་པར་གནས་པར་བྱ་བ་ལ་དབང་བྱེད་དོ། །

[Block 922]
ཚོར་བ་རྣམས་ནི་ཀུན་ནས་ཉོན་མོངས་པར་བྱ་བ་ལ་དབང་བྱེད་དེ།

[Block 923]
འདི་ལྟར་མདོ་ལས།

[Block 924]
བདེ་བའི་ཚོར་བ་ལ་ནི་འདོད་ཆགས་རྒྱས་པར་འགྱུར། སྡུག་བསྔལ་ལ་ནི་ཁོང་ཁྲོ་བ། །སྡུག་བསྔལ་ཡང་མ་ཡིན་བདེ་བ་ཡང་མ་ཡིན་པ་ལ་ནི་མ་རིག་པ་ཞེས་གསུངས་སོ། །

[Block 925]
དད་པ་ལ་སོགས་པ་ལྔ་པོ་དག་ནི་རྣམ་པར་བྱང་བར་བྱ༌[^412]བ་ལ་དབང་བྱེད་དེ། འདི་ལྟར་དེ་དག་གིས་ཉོན་མོངས་པ་རྣམས་ཀྱང་རྣམ་པར་གནོན་ལ་ལམ་ཡང་འདྲེན་པར་བྱེད་དོ། །

[Block 926]
དེ་ཉིད་ཀྱི་ཕྱིར་དེ་དག་ཀྱང་སོ་སོར་དབང་པོ་ཡིན་པར་འདོད་དོ། །

[Block 927 [VERSE]]
མྱ་ངན་འདས་སོགས་གོང་ནས་གོང་། །
འཐོབ་པ་ལ་ནི་དབང་བྱེད་ཕྱིར། །
ཀུན་ཤེས་བྱེད་དང་ཀུན་ཤེས་དང་། །
དེ་བཞིན་ཀུན་ཤེས་ལྡན་དབང་པོ། །

[Block 928]
དེ་བཞིན་ཞེས་བྱ་བའི་སྒྲ་ནི་སོ་སོར་དབང་པོ་ཡིན་ནོ་ཞེས་བསྟན་པའི་ཕྱིར་རོ། །

[Block 929]
དེ་ལ་ཀུན་ཤེས་པར་བྱེད་པའི་དབང་པོ་ནི་ཀུན་ཤེས་པའི་དབང་པོ་འཐོབ་པར་བྱ་བ་ལ་དབང་བྱེད་དོ། །

[Block 930]
ཀུན་ཤེས་པའི་དབང་པོ་ནི། ཀུན་ཤེས་པ་དང་ལྡན་པའི་དབང་པོ་ཐོབ་པར་བྱ་བ་ལ་དབང་བྱེད་དོ། །

[Block 931]
ཀུན་ཤེས་པ་དང་ལྡན་པའི་དབང་པོ་ནི་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བར་བྱ་བ་ལ་དབང་བྱེད་དེ། སེམས་རྣམ་པར་མ་གྲོལ་བ་ལ་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 932]
སོགས་པ་ཞེས་བྱ་བའི་སྒྲ་ནི་རྣམ་གྲངས་གཞན་བསྟན་པར་བྱ་བའི་ཕྱིར་ཏེ། རྣམ་གྲངས་གཞན་གང་ཞེ་ན། ཀུན་ཤེས་པར་བྱེད་པའི་དབང་པོ་ནི་མཐོང་བས་སྤང་བར་བྱ་བའི་ཉོན་མོངས་པ་སྤོང་བ་ལ་དབང་བྱེད་དོ། །

[Block 933]
ཀུན་ཤེས་པའི་དབང་པོ་ནི་བསྒོམས་པས༌[^413]སྤང་བར་བྱ་བའི་ཉོན་མོངས་པ་སྤོང་བ་ལ་དབང་བྱེད་དོ། །

[Block 934]
ཀུན་ཤེས་པ་དང་ལྡན་པའི་དབང་པོ་ནི་མཐོང་བའི་ཆོས་ལ་བདེ་བར་གནས་པའི་ཕྱིར་དབང་བྱེད་དེ། རྣམ་པར་གྲོལ་བས་དགའ་བ་དང་བདེ་བ་ལ་སོ་སོར་ཡང་དག་པར་མྱོང་བའི་ཕྱིར་རོ། །

[Block 935 [HEADING]]
#### དབང་པོ་དེ་སྙེད་དང་དེ་དག་གི་གོ་རིམས། ^2-1-2-0

[Block 936]
དབང་བྱེད་པའི་ཕྱིར་དབང་པོ་ཉིད་ཡིན་ན། མ་རིག་པ་ལ་སོགས་པས་ཁ་བསྐང་དགོས་ཏེ། མ་རིག་པ་ལ་སོགས་པ་དག་ཀྱང་འདུ་བྱེད་ལ་སོགས་པ་རྣམས་ལ་དབང་བྱེད་པས། དེའི་ཕྱིར་དེ་དག་ཀྱང་དབང་པོ་ཉིད་དུ་ཁ་བསྐང་བར་བྱ༌[^414]ལ། ངག་ལ་སོགས་པ་དག་དང་། ལག་པ་དང་། རྐང་པ་དང་། རྐུབ་དང་། མདོམས༌[^415]རྣམས་ཀྱང་ཚིག་དང་། ལེན་པ་དང་། འགྲོ་བ་དང་། རྟུག་པ་དང་། ཀུན་ཏུ་དགའ་བའི་བྱ་བ་དག་ལ་དབང་བྱེད་པའི་ཕྱིར་དབང་པོ་ཉིད་དུ་ཁ་བསྐང་བར་བྱའོ་ཞེ་ན།[^416] ཁ་བསྐང་བར་མི་བྱ་སྟེ་འདི་ལྟར་འདིར་ནི།

[Block 937 [VERSE]]
སེམས་ཀྱི་རྟེན་དང་དེའི་བྱེ་བྲག །
གནས་དང་ཀུན་ནས་ཉོན་མོངས་ཉིད། །
ཚོགས་དང་རྣམ་བྱང་ཇི་སྙེད་པ། །
དབང་པོ་དག་ཀྱང་དེ་སྙེད་དུ། །

[Block 938]
འདོད་དེ། དེ་ལ་སེམས་ཀྱི་རྟེན་ནི་དབང་པོ་དྲུག་དག་ཡིན་ཏེ། སྐྱེ་མཆེད་དྲུག་པོ་དེ་ནི་སེམས་ཅན་གྱི་རྫས་ཀྱི་གཞི་ཡིན་ནོ། །

[Block 939]
མོ་དང་ཕོའི་དབང་པོ་དག་གིས་ནི་དེ་མོ་དང་ཕོར་བྱེ་བྲག་ཏུ་འབྱེད་དོ། །

[Block 940]
སྲོག་གི་དབང་པོས་ནི་གནས་པར་བྱེད་དོ། །

[Block 941]
ཚོར་བ་རྣམས་ཀྱིས་ནི་ཀུན་ནས་ཉོན་མོངས་པར་བྱེད་དོ། །

[Block 942]
དད་པ་ལ་སོགས་པ་ལྔས་ནི་རྣམ་པར་བྱང་བའི་ཚོགས་སོགས་པར་བྱེད་དོ། །

[Block 943]
གསུམ་གྱིས་ནི་རྣམ་པར་བྱང་བར་བྱེད་དེ། དེའི་ཕྱིར་མ་རིག་པ་ལ་སོགས་པ་ནི་དབང་པོ་ཉིད་དུ་མི་འདོད་དོ། །

[Block 944 [VERSE]]
ཡང་ན་འཇུག་པའི་རྟེན་དང་ནི། །
སྐྱེ་དང་གནས་དང་ཉེར་སྤྱོད་ལས། །
བཅུ་བཞི་དེ་བཞིན་ལྡོག་པ་ལ། །
དབང་པོ་རྣམས་ནི་གཞན་ཡིན་ནོ། །

[Block 945]
ཡང་ན་ཞེས་བྱ་བའི་སྒྲ་ནི་གཞུང་ལུགས་ཐ་དད་པར་བསྟན་པའི་ཕྱིར་ཏེ། གཞན་དག་ན་རེ་འཇུག་པའི་རྟེན་ནི་དབང་པོ་དྲུག་ཡིན་ནོ། །

[Block 946]
སྐྱེ་བ་ནི་མོ་དང་ཕོའི་དབང་པོ་དག་ཡིན་ཏེ། དེ་ལས་སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 947]
གནས་པ་ནི་སྲོག་གི་དབང་པོ་ཡིན་ཏེ། དེས་གནས་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 948]
ཚོར་བ་རྣམས་ཀྱིས་ནི་ཉེ་བར་སྤྱོད་པར་བྱེད་དེ། དེའི་ཕྱིར་དེ་དག་ནི་དབང་པོ་བཅུ་བཞི་ཡིན་ནོ། །

[Block 949]
རྣམ་པ་དེ་ཉིད་ཀྱིས་གཞན་དག་ནི་ལྡོག་པ་ཡིན་ཏེ། ལྡོག་པའི་རྟེན་ནི་དད་པ་ལ་སོགས་པ་ཡིན་ནོ། །

[Block 950]
སྐྱེ་བ་ནི་ཀུན་ཤེས་པར་བྱེད་པའི་དབང་པོ་ཡིན་ནོ། །
--- END BLOCKS ---
