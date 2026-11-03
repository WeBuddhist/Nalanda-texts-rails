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
གང་སྤངས་པ་ནི་ཉོན་མོངས་པ་ལ་སོགས་པ༌[^2547]སྤངས་སོ། །

[Block 2907]
དམིགས་པའི་ཡུལ་ལ་རྩེ་གཅིག་ཏུ་གནས་པར་ནུས་པ་ནི། ཞི་གནས་ལ་འཇུག་པའི་དམིགས་པ་ལ་སེམས་རྩེ་གཅིག་ཏུ་འཇུག་པར་ནུས་པའོ། །

[Block 2908]
ཞི་གནས་ཀྱི༌[^2548]དམིགས་པའི་དམིགས་པ་ནི། ཞི་གནས་ལ་དམིགས་པའི་དམིགས་པ་ཞེས་བྱའོ། །

[Block 2909 [HEADING]]
#### ཏིང་ངེ་འཛིན་ཤིན་ཏུ་འབྲེལ་པ། ^8-6-6-0

[Block 2910]
ཏིང་ངེ་འཛིན་ཤིན་ཏུ་འབྲེལ་པ་ནི། གང་ཏིང་ངེ་འཛིན་ཡང་དག་བྱང་ཆུབ་ཀྱི་ཡན་ལག་ལ༌[^2549]རབ་ཏུ་ཞུགས་པ་སྟེ། དེའི་དབང་དུ་བྱས་ནས། དེ་ལ་ཏིང་ངེ་འཛིན་ཡང་དག་བྱང་ཆུབ་ཀྱི་ཡན་ལག་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2911]
དེ་ཡང་ཏིང་ངེ་འཛིན་གང་གིས་དེ་བཞིན་ཉིད༌[^2550]སོ་སོར་རང་གིས་རིག་ཅིང་དེ་བཞིན་ཉིད་མངོན་སུམ་དུ་བྱེད་པ་ནི་ཏིང་ངེ་འཛིན་ཡང་དག་བྱང་ཆུབ་ཀྱི་ཡན་ལག་ཅེས་བྱའོ། །

[Block 2912]
སེམས་མཉམ་པར་གཞག་པ་ཞེས་བྱ་བ་ནི་སྟོང་པ་ཉིད་ལ་སེམས་རྩེ་གཅིག་ཏུ་གཞག་པས༌[^2551]སོ། །

[Block 2913]
ཆོས་ཀྱི་ཡེ་ཤེས་མངོན་པར་འཚང་རྒྱའི་ཞེས་བྱ་བ་ནི་རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་སོ་སོར་རང་གིས་རིག་པར་འགྱུར་གྱི་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2914]
མཉམ་པར་མི༌[^2552]གཞག་པས་ནི་མ་ཡིན་ཞེས་བྱ་བས་ནི་སེམས་སྤྲོས་པ་དང་བཅས་པས་ནི་རང་བཞིན༌[^2553]རིག་པར་མི་ནུས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2915]
ཆོས་དེ་དག་མངོན་པར་རྫོགས་པར༌[^2554]འཚང་རྒྱའི་ཞེས་བྱ་བ་ནི། སྟོང་པ་ཉིད་མངོན་སུམ་དུ་འགྱུར་གྱི༌[^2555]ཞེས་བྱ་བའི་ཐ་ཚིག་སྟེ། ཚིག་དེ་དག་ནི་སོ་སོའི་སྐྱེ་བོའི་དབང་དུ་བྱས་ནས་གསུངས་པའོ། །

[Block 2916]
ཉན་ཐོས་ལ་སོགས་པའི་དབང་དུ་བྱས་ནས་ལྟ་བ་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། ཉོན་མོངས་པ་འདོར་བ་ཙམ་གྱི༌[^2556]ཡེ་ཤེས་རང་གིས༌[^2557]རིག་ཅིང་ཆོས་ཀྱི་དབྱིངས་མངོན་སུམ་དུ་མི་འགྱུར་གྱི། འདུས་བྱས་དང་འདུས་མ་བྱས་ཀྱི་ཆོས་ཐམས་ཅད་དུ་སྟོང་པ་ཉིད་དུ་མཉམ་པ་དང་། ཐ་དད་མེད་པར༌[^2558]ཤེས་ནས་དེ་གཉིས་མངོན་པར་འཚང་རྒྱ་བར་འགྱུར་རོ་ཞེས་བྱ་བའི༌[^2559]དོན་ཏོ། །

[Block 2917 [HEADING]]
#### བཏང་སྙོམས་ཤིན་ཏུ་འབྲེལ་པ། ^8-6-7-0

[Block 2918]
བཏང་སྙོམས་ཤིན་ཏུ་འབྲེལ་པ་ནི། གང་བཏང་སྙོམས་ཡང་དག་བྱང་ཆུབ་ཀྱི་ཡན་ལག་ལ༌[^2560]རབ་ཏུ་ཞུགས་པ་སྟེ། དེའི་དབང་དུ་བྱས་ནས། དེ་ལ་བཏང་སྙོམས་ཡང་དག་ཅེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2919]
སེམས་ཡོངས་སུ་མི་གཏུགས་པ་ཞེས་བྱ་བ་ནི་ཡིད་བདེ་བ་དང་མི་བདེ་བ་གང་གི༌[^2561]དབང་དུ་ཡང་མི་འགྱུར་ཞིང་ཆགས་པ་དང་། ཁོང་ཁྲོ་བས་སེམས་ཀུན་དུ་མི་ཟིན་པའོ། །

[Block 2920]
འཇིག་རྟེན་གྱི་ཆོས་རྣམས་ཀྱིས༌[^2562]མི་འཕྲོགས་ཞེས་བྱ་བ་ནི། འཇིག་རྟེན་གྱི༌[^2563]ཆོས་བརྒྱད་ཀྱི་དབང་དུ་མི་འགྱུར་བ་དང་། རྙེད་པ་ལ་སོགས་པ་དང་ལྡན་ཡང་མཐོ་བར་མི་སེམས། མ་རྙེད་པ་ལ་སོགས་པ་དང་ལྡན་ཡང་དམའ་བར་མི་སེམས་པའི་ཕྱིར། དེ་དག་གིས་མི་སྒུལ་བ་ནི་བཏང་སྙོམས་ཡང་དག་བྱང་ཆུབ་ཀྱི་ཡན་ལག་ཅེས་བྱའོ། །

[Block 2921]
གནོད་པ་མེད་པ་ནི་གནོད་པ་བྱས་ཀྱང་གནོད་པར་མི་ཚོར་བའོ། །

[Block 2922]
འཕྲོགས་པ་མེད་པ་ནི་མི་མཐུན་པའི་ཕྱོགས་ཀྱི་དབང་དུ་མི་འགྱུར་བའོ། །

[Block 2923]
རྗེས་སུ་ཆགས་པ་དང་ཞེ༌[^2564]འགྲས་པ་མེད་པ་ནི་འདོད་ཆགས་དང་ཁོང་ཁྲོ་མེད་པའོ། །

[Block 2924]
འཕགས་པའི་བདེན་པའི་ལམ་དང་མཐུན་པ་ནི། དེ་ལྟར་ཉོན་མོངས་པའི་དབང་དུ་མ་གྱུར་པ་སྟེ། བཏང་སྙོམས་པ་ལས་འཕགས་པའི་ལམ་གྱི་ཡན་ལག་འགྲུབ་པའི་ཕྱིར་རོ། །

[Block 2925 [HEADING]]
#### བྱང་ཆུབ་ཀྱི་ཡན་ལག་ཏུ་གཞག་པ། ^8-6-8-0

[Block 2926]
འདི་དག་བྱང་ཆུབ་ཀྱི་ཡན་ལག་ཏུ་གཞག་པ་ཡང་། དེ་ལ་དྲན་པ་ནི་རྟེན་གྱི་ཡན་ལག་སྟེ། དྲན་པ་ཉེ་བར་གནས་པར་གྱུར་ན། དགེ་བའི་ཆོས་ཐམས་ཅད་སེམས་ལ་གསལ་བའི་ཕྱིར་རོ། །

[Block 2927]
ཆོས་རྣམ་པར་འབྱེད་པ་ནི། རང་བཞིན་གྱི་ཡན་ལག་སྟེ། དེ་ཉིད་བྱང་ཆུབ་ཀྱི་མཚན་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2928]
བརྩོན་འགྲུས་ནི་ངེས་པར་འབྱུང་བའི་ཡན་ལག་སྟེ། དེས༌[^2565]ཇི་སྲིད་འགྲོ་བར་བྱ་བར་ཕྱིན་པར་འགྲོ་བའི་ཕྱིར་རོ། །

[Block 2929]
དགའ་བ་ནི་ཕན་ཡོན་གྱི་ཡན་ལག་སྟེ། དེས་རྒྱུད་ལ༌[^2566]ཚིམ་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 2930]
ཤིན་ཏུ་སྦྱངས་པ་དང་། ཏིང་ངེ་འཛིན་དང་། བཏང་སྙོམས་ནི་ཉོན་མོངས་པ་མེད་པའི་ཡན་ལག་གོ། །

[Block 2931]
དེ་ལ་ཤིན་ཏུ་སྦྱངས་པ་ནི་ཉོན་མོངས་པ་མེད་པ་སྟེ།

[Block 2932 [VERSE]]
དེས་གནས་ངན་ལེན་སྤོང་བར་བྱེད་པའི་ཕྱིར་རོ། །
ཏིང་ངེ་འཛིན་ནི་ཉོན་མོངས་པ་མེད་པ་སྟེ།
དེ་ལ་གནས་པའི་གནས་གཞན་དུ་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2933]
བཏང་སྙོམས་ནི་ཉོན་མོངས་པ་མེད་པ་སྟེ། དེའི་དུས་ན་ཆགས་སེམས་དང་ཡིད་བདེ་བ་དང་བྲལ་བའི་ཕྱིར་རོ། །

[Block 2934]
བྱང་ཆུབ་ཀྱི་ཡན་ལག་མི་ཟད་པ་བདུན་བཤད་ཟིན་ཏོ།། །།

[Block 2935 [HEADING]]
### འཕགས་པའི་ལམ་ཡན་ལག་བརྒྱད་པ་མི་ཟད་པ། ^8-7-0

[Block 2936]
རྣམ་པར་མི་རྟོག་པ་དང་། ཤིན་ཏུ་རྟོག་པ་དང་། དུལ་བ་དང་། ཞི་བ་དང་། རབ་ཏུ་ཞི་བ་དང་། ཤིན་ཏུ་བྱུང་བ་དང་། དགའ་བ་དང་ལྡན་པ་དང་། མཐུ་ཆེ་བ་དང་། བསྡུས་པའི་རྣལ་འབྱོར་ལ་སྤྱོད་པ་དང་། སྤྲོས་པའི་རྣལ་འབྱོར་ལ༌[^2567]སྤྱོད་པ་བསྟན་པའི་ཕྱིར། བཙུན་པ་ཤ་ར་དྭ༌[^2568]ཏིའི་བུ་གཞན་ཡང་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ལམ་མི་ཟད་པ་སྟེ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2937]
དེ་དག་ལས་འཕགས་པའི་ལམ་ཡན་ལག་བརྒྱད་པས་ནི་བསྡུས་པའི་དོན་བསྒོམ་པའི་ལམ་བསྟན་ལ། ཞི་གནས་དང་ལྷག་མཐོང་གིས་ནི་སྦྱོར་བ་བསྟན་པ༌[^2569]སྦྱར་རོ། །

[Block 2938]
དེ་མི་ཟད་པ་ཡང་དེས་བསྒྲུབ་པར་བྱ་བའི་ཆོས་མི་ཟད་པའི་ཕྱིར། །སྒྲུབ་པར༌[^2570]བྱེད་པའི་ལམ་རྣམས་ཀྱང་མི་ཟད་པའོ། །

[Block 2939]
འདིར་ཡང་བསྟན་པ་དང་བཤད་པའི་ཚུལ་དུ་རིག་པར་བྱ་སྟེ། ལམ་ཞེས་བྱ་བ་ནི་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། ཡང་དག་པའི་ཏིང་ངེ་འཛིན་ཏོ་ཞེས་བྱ་བ་ཡན་ཆད་ནི་བསྟན་པའི་ཚུལ་ལོ། །

[Block 2940]
ལྷག་མ་རྣམས་ནི་བཤད་པའི་ཚུལ་ལོ། །

[Block 2941]
ལམ་ཞེས་བྱ་བ་ནི་འཕགས་པའི་ལམ་ཡན་ལག་བརྒྱད་པ་སྟེ་ཞེས་བྱ་བ་ལ། འཕགས་པ་རྣམས་ཡེ་ཤེས་གང་གིས་བླ་ན་མེད་པའི་བྱང་ཆུབ་འགྲུབ་པའི་ཡེ་ཤེས་དེ་ལ་ལམ་ཞེས་བྱའོ། །

[Block 2942]
ལྟ་བ་ལ་སོགས་པ་བརྒྱད་པོ་དེ་རྣམས་ལམ་གྱི་ཡེ་ཤེས་དེའི་གྲོགས་སུ་གྱུར་པའི་ཕྱིར༌[^2571]ཡན་ལག་ཅེས་བྱ་སྟེ། འཇིག་རྟེན་པའི་ལོག་པར་ལྟ་བ་ལས་བཟློག༌[^2572]པས་ན༌[^2573]ཡང་དག་པའོ། །

[Block 2943 [HEADING]]
#### རྣམ་པར་མི་རྟོག་པ། ^8-7-1-0

[Block 2944]
རྣམ་པར་མི་རྟོག་པའི་བྱང་ཆུབ་སེམས་དཔའ་ནི་བསྒོམ་པའི༌[^2574]ལམ་ན་ཡང་དག་པའི་ལྟ་བ་ཐོབ་པ་སྟེ། དེའི་དབང་དུ་བྱས་ནས་ཡང་དག་པའི་ལྟ་བ་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2945]
གང་འདི་འཕགས་པ་འཇིག་རྟེན་ལས་འདས་པ་ཞེས་བྱ་བ་ལ། ཟག་པ་མེད་པ་གཉིས་སུ་མེད་པའི་ཡེ་ཤེས་ནི་ཡང་དག་པའི་ལྟ་བའོ། །
--- END BLOCKS ---
