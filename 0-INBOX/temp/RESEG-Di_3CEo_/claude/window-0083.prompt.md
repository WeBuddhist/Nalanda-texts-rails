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
[Block 2906]
དེ་བཞིན་དུ་སྲིད་པའི་ཟག་པ་ནི་སྲིད་པའི་ཆུ་བོ་དང་། སྲིད་པའི་སྦྱོར་བ་ཡིན་ནོ། །

[Block 2907]
ལྟ་བ་རྣམས་ནི་མ་གཏོགས་ཏེ། དེ་དག་ནི་ཆུ་བོ་དང་། སྦྱོར་བ་རྣམས་ལས་ལོགས་ཤིག་ཏུ་བཞག་སྟེ། གསལ་བའི་ཕྱིར་རོ། །

[Block 2908 [VERSE]]
ཟག་པར་མ་ཡིན་གྲོགས་མིང༌[^1155]རྣམས། །
འཇོག་པའི་རྗེས་སུ་མི་མཐུན་ལོ། །

[Block 2909]
ཟག་པ་རྣམས་ཀྱི་ངེས་པའི་ཚིག་ནི་འཇོག་པར་བྱེད་པས་ན་ཞེས་འོག་ནས་འཆད་ན། ལྟ་བ་འབའ་ཞིག་ནི་གསལ་བའི་ཕྱིར་འཇོག་པའི་རྗེས་སུ་མཐུན་པ་མ་ཡིན་པས་བསྲེས་ནས་གཞག་གོ། །

[Block 2910 [HEADING]]
#### ཉེ་བར་ལེན་པ། ^5-13-3-0

[Block 2911 [VERSE]]
ཇི་སྐད་བཤད་ཉིད་མ་རིག་བཅས། །
ཉེར་ལེན་རྣམས་ཏེ་ལྟ་རྣམས་གཉིས། །

[Block 2912]
ཕྱེ་བའི༌[^1156]ཕྱིར་རོ། །

[Block 2913]
འདོད་པའི་སྦྱོར་བ་ཉིད་མ་རིག་པ་དང་བཅས་པ་ནི་འདོད་པའི་ཉེ་བར་ལེན་པའོ། །

[Block 2914]
སྲིད་པའི༌[^1157]སྦྱོར་བ་ཉིད་མ་རིག་པ་དང་བཅས་པ་ནི་བདག་ཏུ་སྨྲ་བའི་ཉེ་བར་ལེན་པའོ། །

[Block 2915]
ལྟ་བའི་སྦྱོར་བ་དག་ལས་ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་ཕྱུང་སྟེ། ལྟ་བའི་ཉེ་བར་ལེན་པའོ། །

[Block 2916]
ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་ནི་ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་ཀྱི་ཉེ་བར་ལེན་པའོ། །ཅིའི་ཕྱིར་མ་རིག་པ་བསྲེས་ཏེ་ཉེ་བར་ལེན་པར་བཤད་ཅེ་ན། སྲིད་པ་འཛིན་པའི་ཕྱིར་ཉེ་བར་ལེན་པ་དག་ཡིན་ན། མ་རིག་པ་འཛིན་པར་བྱེད་པ་མིན་ཕྱིར་བསྲེས། མ་རིག་པ་ནི་མི་ཤེས་པའི་མཚན་ཉིད་ཀྱིས་མི་གསལ་བའི་ཕྱིར་འཛིན་པར་བྱེད་པ་མ་ཡིན་ཏེ། དེའི་ཕྱིར་བསྲེས་སོ། །

[Block 2917 [HEADING]]
#### ངེས་པའི་ཚིག། ^5-13-4-0

[Block 2918]
ཡང་དེ་དག་གི་ནང་ནས་ཕྲ་རྒྱས་ཀྱི་དོན་ཅི་ཡིན། ཉེ་བར་ལེན་པའི་བར་གྱི་དོན་ཅི་ཡིན་ཞེ་ན།

[Block 2919 [VERSE]]
གང་ཕྱིར་དེ་དག་ཕྲ་བ་དང་། །
རྗེས་འབྲེལ་རྣམ་གཉིས་རྒྱས་འགྱུར་དང་། །
རྗེས་སུ་འབྲེལ་པ་དེ་ཡི་ཕྱིར། །
ཕྲ་རྒྱས་དག་ཏུ་བཤད་པ་ཡིན། །

[Block 2920]
དེ་ལ་ཕྲ་བ་ནི་རྟོགས་པར་དཀའ་བས་རྒྱུ་བ་ཕྲ་བའི་ཕྱིར་རོ། །

[Block 2921]
རྗེས༌[^1158]འབྲེལ་པ་ནི་ཐོབ་པ་དང་རྗེས་སུ་འབྲེལ་པས་སོ། །

[Block 2922]
རྒྱས་པར་འགྱུར་བ་ནི་དམིགས་པ་དང་མཚུངས་པར་ལྡན་པའི་སྒོ་ནས་སོ། །

[Block 2923]
རྗེས་སུ་འབྲང་བ་ནི་སྦྱོར་བ་མེད་པ་སྟེ། བཟློག་བཞིན་དུ་ཡང་ཡང་དུ་མངོན་དུ་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2924 [VERSE]]
དེ་དག་འཇོག་བྱེད་ཟག་བྱེད་དང་། །
འཁྱེར་བར་བྱེད་དང་འབྱར་བྱེད་དང་། །
ཉེ་བར་འཛིན་ཕྱིར་ཟག་ལ་སོགས། །
དེ་དག་གི་ནི་ངེས་ཚིག་ཡིན། །

[Block 2925]
འཁོར་བར་འཇོག་པར་བྱེད་པ་དང་། །སྲིད་པའི་རྩེ་མོ་ནས་མནར་མེད་པའི་བར་དུ་སྐྱེ་མཆེད་དྲུག་གི་རྨ་ནས་འཛག་པས་ན་ཟག་པ་དག་ཡིན་ནོ། །

[Block 2926]
འཁྱེར་བར་བྱེད་པས་ན་ཆུ་བོ་དག་ཡིན་ནོ། །

[Block 2927]
འབྱར་བར་བྱེད་པས་ན་སྦྱོར་བ་དག་གོ། །

[Block 2928]
ཉེ་བར་འཛིན་པར་བྱེད་པས་ན་ཉེ་བར་ལེན་པ་རྣམས་སོ། །

[Block 2929 [HEADING]]
### ཀུན་དུ་སྦྱོར་བ་ལ་སོགས་པ་རྣམ་པ་ལྔ། ^5-14-0

[Block 2930 [VERSE]]
དེ་དག་ཀུན་དུ་སྦྱོར་སོགས་ཀྱི།[^1159] །
དབྱེ་བས་ཡང་རྣམ་ལྔར་བཤད་དོ། །

[Block 2931]
ཕྲ་རྒྱས་དེ་དག་ཉིད་ཀུན་དུ་སྦྱོར་བ་དང་། འཆིང་བ༌[^1160]དང་། ཕྲ་རྒྱས་དང་། ཉེ་བའི་ཉོན་མོངས་པ་དང་། ཀུན་ནས་དཀྲིས་པའི་དབྱེ་བ༌[^1161]ཡང་རྣམ་པ་ལྔར་ཕྱེ་ནས་བཤད་དོ། །

[Block 2932 [HEADING]]
#### ཀུན་དུ་སྦྱོར་བ། ^5-14-1-0

[Block 2933]
དེ་ལ་ཀུན་དུ་སྦྱོར་བ་ནི་དགུ་སྟེ། རྗེས་སུ་ཆགས་པ་དང་། ཁོང་ཁྲོ་བ་དང་། ང་རྒྱལ་དང་། མ་རིག་པ་དང་། ལྟ་བ་དང་། མཆོག་ཏུ་འཛིན་པ་དང་། ཐེ་ཚོམ་དང་། ཕྲག་དོག་དང་། སེར་སྣའི་ཀུན་དུ་སྦྱོར་བ་རྣམས་སོ། །

[Block 2934]
ཡང་ཅིའི་ཕྱིར་ལྟ་བ་གསུམ་ནི་ལོགས་ཤིག་ཏུ་ལྟ་བའི་ཀུན་དུ་སྦྱོར་བར་བཤད་ལ། གཉིས་ནི་ལོགས་ཤིག་ཏུ་མཆོག་ཏུ་འཛིན་པའི་ཀུན་དུ་སྦྱོར་བར་བཤད་ཅེ་ན།

[Block 2935 [VERSE]]
རྫས་དང་མཆོག་འཛིན་འདྲ་བའི་ཕྱིར། །
ལྟ་གཉིས་ཀུན་དུ་སྦྱོར་གཞན་ནོ། །

[Block 2936]
ལྟ་བ་གསུམ་ཡང་རྫས་བཅོ་བརྒྱད་ཡིན་ལ། མཆོག་ཏུ་འཛིན་པའི་ལྟ་བ་གཉིས་ཀྱང་རྫས་བཅོ་བརྒྱད་ཁོ་ན་ཡིན་ཏེ། དེའི་ཕྱིར་རྫས་མཉམ་པས་འདི་གཉིས་ཀུན་དུ་སྦྱོར་བ་གཞན་དུ་བྱས་སོ། །

[Block 2937]
འདི་གཉིས་ནི་མཆོག་ཏུ་འཛིན་པའི་རང་བཞིན་ཡིན་ལ། ལྷག་མ་རྣམས་ནི་མ་ཡིན་པས་མཆོག་ཏུ་འཛིན་པར་འདྲ་བའི་ཕྱིར་ཡང་འདི་དག༌[^1162]གཉིས་ལོགས་ཤིག་ཏུ་བཤད་དེ། གཟུང་བ་དང་འཛིན་པ་ཐ་དད་པའི་ཕྱིར་རོ། །

[Block 2938]
ཡང་ཅིའི་ཕྱིར་ཀུན་དུ་སྦྱོར་བ་དག་ཕྲག་དོག་དང་། སེར་སྣ་ནི་ལོགས་ཤིག་ཏུ་ཀུན་དུ་སྦྱོར་བ་གཉིས་སུ་བཤད་ལ། ཀུན་ནས་དཀྲིས་པ་གཞན་ནི་མ་ཡིན་ཞེ་ན།

[Block 2939 [VERSE]]
གང་ཕྱིར་གཉིས་ཀའང་གཅིག་ཏུ་ནི། །
མི་དགེ་རང་དབང་དེ་ཡི་ཕྱིར། །
ཕྲག་དོག་སེར་སྣ་དེ་དག་ལས། །
ལོགས་ཤིག་ཀུན་སྦྱོར་གཉིས་སུ་བཤད། །

[Block 2940]
གང་ལ་གཅིག་ཏུ་མི་དགེ་བ་དང་། རང་དབང་ཅན་འདི་གཉིས་ག༌[^1163]ཡིན་པ་དེ་ལྟ་བུའི་ཀུན་ནས་དཀྲིས་པ་གཞན་ནི་མེད་དོ། །

[Block 2941]
ཡང་བཅོམ་ལྡན་འདས་ཀྱིས་ཀུན་དུ་སྦྱོར་བ། ཐ་མའི་ཆ་དང་མཐུན་རྣམ་ལྔ། །གསུངས་ཏེ། ཅིའི་ཕྱིར་རྣམ་པ་ལྔ་ཁོ་ན་ཡིན་ཞེ་ན། འདི་ལྟར།

[Block 2942 [VERSE]]
གཉིས་ཀྱིས་འདོད་ལས་མི༌[^1164]འདའ་ལ། །
གསུམ་པོ་ཡིས་ནི་ཕྱིར་ཟློག་བྱེད། །

[Block 2943]
འདོད་པ་ལ་འདུན་པ་དང་། གནོད་སེམས་དག་གིས་ནི་འདོད་པའི་ཁམས་ལས་མི་འདའོ། །

[Block 2944]
འཇིག་ཚོགས་ལ་ལྟ་བ་ལ་སོགས་པ་དག་གིས་ནི་འདས་ཀྱང་ཕྱིར་ཟློག་པར་བྱེད་དོ། །

[Block 2945]
འདིར་ཡང་གསུངས་པ། སྒོ་དང་རྩ་བས་བསྡུས་ཕྱིར་གསུམ། །ཁོ་ནར་གསུངས་སོ། །
--- END BLOCKS ---
