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
[Block 2871]
མགུ་བར་བྱ་བ་ནི་སེམས་མགུ་བར་བྱ་བའི་ཕྱིར་ཡིན་ལ། ཡོངས་སུ་གནས་པ་ནི་བཅབས་པའི་ཁ་ན་མ་ཐོ་བ་གཞོམ་པའི་ཕྱིར་ཡིན་ནོ། །

[Block 2872]
དེ་བས་ན་འདི་གཉིས་ཅིག་ཅར་སྤྱད་པ་ནི་མི་སྲིད་དོ། །

[Block 2873]
དགེ་སློང་དག་ཁྱོད་ཀྱིས་གང་ཟག་དེ་ལ་ལྟུང་བ་གཉིས་པའི་རྒྱུ་ལ་སྔ་མ་ལ༌[^2713]ནི་ཇི་ལྟར་བཅབས་པའི་ཡོངས་སུ་གནས་པ་བྱིན་ཅིག །ཕྱི་མ་ལ་ནི་ཞག་དྲུག་མགུ་བ་བྱིན་ཅིག་ཅེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་པ་དེ་ནི་མགུ་བ་སྤྱོད་པའི་གནས་སྐབས་སུ་ཡོངས་སུ་གནས་པ་ལ༌[^2714]སྤྱད་པ་ཡང༌[^2715]དེ་ལྟར་བསྟན་པར་མི་བྱ་སྟེ་ད༌[^2716]ནི་ཕྱིར་བཅོལ་བ༌[^2717]ཙམ་བསྟན་པ་ཡིན་པས་ན་དེས་ནི་སྔར་བཅབས་པའི་ཕྱིར་ཡོངས་སུ་གནས་པ་བྱེད་དུ་བཅུག་ལ་དེའི་འོག་ཏུ་དབྱུང་བའི་ཕྱིར་མགུ་བར་བྱེད་དུ་བཅུག་ཅིག་ཅེས་གསུངས་པ་ཡིན་གྱི་མགུ་བ་དང་ཡོངས་སུ་གནས་པ་གཉིས་ཅིག་ཅར་སྤྱོད་དུ་གཞུག་པ་ནི་མ་ཡིན་ནོ། །

[Block 2874]
དུས་དང་དུས་མ་ཡིན་པར་བསྡུས་པའི་དབྱུང་བ༌[^2718]གཞིའོ་ཞེས་བྱ་བ་ནི་གཞི་འདི་ལ་མིང་དུ་བྱས་པའོ། །

[Block 2875]
འདི་ནི་ལྟུང་བ་བཅབས་པ་སྤྱད་པ་རྣམས་ཀྱི༌[^2719]ལྡང་བའི་དུས་སོ། །

[Block 2876]
འདི་ནི་དུས་མ་ཡིན་ནོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2877]
འདི་ནི་མི་ཤེས་པའི་དུས་ལ་བརྟེན་པར་བྱའོ། །

[Block 2878]
བསྡུས་པ་འབྱུང་བ་ཞེས་བྱ་བ་ནི་ལྟུང་བ་རྣམས་ཀྱི༌[^2720]ཆོ་ག་མདོར་བསྡུས་པ་འདི་ཅིག་ཅར་མངོན་དུ་འབྱུང་ངོ་ཞེས་བྱ་བའི༌[^2721]ཚིག་གིས་དེ་རིག་པར༌[^2722]བྱའོ། །

[Block 2879]
དུས་དང་དུས་མ་ཡིན་པར་བསྡུས་པ་འབྱུང་བའི་གཞིའོ།། །།

[Block 2880]
ཉིན་མཚན་གྱི་མཐའི་ཆ་མ་ཡིན་པ་ལ་འཆབ་པ་མི་འབྱུང་ངོ་ཞེས་བྱ་བ་ནི་སྐྱ་རེངས་ཤར་ན་ནི་འཆབ་པ་འབྱུང་བ་ཁོ་ནར་འགྱུར་རོ། །

[Block 2881]
བརྗོད་པའི་ཡན་ལག་མེད་ན་དེའི་སེམས་མ་ཡིན་པ་ཉིད་འཆབ་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་བརྗོད་པའི་རང་བཞིན་དུ་གྱུར་པ་དང་རང་བཞིན་དུ་གནས་པ་དང་། ལྟ་བ་ཐ་མི་དད་པ་དང་བསྙེན་པར་རྫོགས་པ་དང་བཅས་པ་དང་། མཚན་ཐ་མི་དད་པ་དང་། མཚམས་ཀྱི་ནང་ན༌[^2723]གནས་པ་ཞེས་བྱ་བ་ལ་སོགས་པའི་གང་ཟག་གང་ཡིན་པ་དེ་མེད་ན། ཉིན་མཚན་གྱི་ཐ་མའི་ཆ་དེ་ལ་ཡང་དེའི་སེམས་མ་ཡིན་པ་ཉིད་ཅེས་བྱ་བ་བརྗོད་པ༌[^2724]དེའི་སེམས་མ་ཡིན་པ་ཉིད་ཅེས་བྱ་བ་ཡོད་ཀྱང་དེ་འཆབ་བ་མ་ཡིན་ནོ། །

[Block 2882]
བརྗོད་པའི་ཡན་ལག་ཡོད་པ་གལ་ཏེ་མི་བརྗོད་དོ་སྙམ་དུ་མི་བརྗོད་པའི་བསམ་པ་སྐྱེ་ན་དེའི༌[^2725]ཚེ་འཆབ་པ་ཁོ་ནར་འགྱུར་རོ། །

[Block 2883]
བགྲོད་དུ་མེད་དམ་སོང་བའི་དབང་ནི་མེད་པ་དང་འདྲ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་བརྗོད་པའི་ཡན་ལག་ཡོད་དུ་ཟིན་ཀྱང་གལ་ཏེ་རྐྱེན་འགའ་ཞིག་གིས༌[^2726]བདག་ཉིད་དེར་བརྗོད་དུ་འགྲོ་བའི་སྐབས་མེད་དམ་གནས་དེ་ནས་སོང་བར༌[^2727]གྱུར་ན། དེའི་དབང་གིས༌[^2728]ཡན་ལག་དེ་མེད་པ་ནི་དེའི་བརྗོད་པའི་ཡན་ལག་མེད་པ་དང་འདྲ་བ་ཉིད་ཡིན་ནོ། །

[Block 2884]
བརྗོད་པའི་ཡན་ལག་ཉེ་བར་གནས་སུ་ཟིན་ཀྱང་རྐྱེན་འགའ་ཞིག་གིས་བདག་ཉིད་དེར་བརྗོད་དུ་འགྲོ་བའི་སྐབས་མེད་དམ་བདག་ཉིད་གནས་དེ་ནས་གཞན་དུ་སོང་བར་གྱུར་པའི་དབང་དག་གིས༌[^2729]བརྗོད་པའི༌[^2730]ཡན་ལག་མེད་པ་ན་མི་བརྗོད་པའི་སེམས་གང་ཡིན་པ་དེ་ནི་འཆབ་པ་མ་ཡིན་ནོ། །

[Block 2885]
བགྲོད་དུ་མེད་པ་དང་སོང་བ་དེ་གཉིས་ཀྱིས་བརྗོད་པ་མ་གྲུབ་པ་འགའ་ཞིག་མེད་པ་དང་འདྲ་བ་ཉིད་ཡིན་པར་མ་ཟད་ཀྱི་འོན་ཀྱང་འདི་ལྟར་དེའི་རྐྱེན་གྱི་དབང་གིས་བྱས་པ་ཡང་ངོ་ཞེས་བྱ་བ་ཡང་འཆབ་པར་གྱུར༌[^2731]དུ་དོགས་པའི་དབང་གིས་ཏེ་དེ་ལྟར་ན་ཡང་བཅབས་པར་མི་འགྱུར་བ་ཁོ་ན་ཡིན་ནོ། །

[Block 2886]
སོང་སྟེ་མ་བརྗོད་ན་བདག་ལ་བཅབས་པའི་ཉེས་པར་འགྱུར་རོ་སྙམ༌[^2732]དུ་དོགས་པའི་བསམ་པ་གལ་ཏེ་བརྗོད་པའི་ཡན་ལག་དྲུང་དུ་མི་འགྲོ་འམ། གནས་དེ་ནས་གཞན་དུ་སོང་བར་གྱུར་ན། དེ་ལྟར་ན་ཡང་བརྗོད་པའི་ཡན་ལག་མེད་པ་དང་འདྲ་བ་ཉིད་དུ་རིག་པར་བྱ་སྟེ་དེའི་ཚེ་ཡང་འཆབ་པར༌[^2733]མི་བྱའོ།[^2734] །

[Block 2887]
འདིར་གཞུང་ནི་བཙུན་པ་རེ་ཞིག་དགེ་སློང་ལྟུང་བ་དང་བཅས་པ་དགེ་སློང་མི་གནས་པའི་གནས་ན་མཆིས་ཤིང་གང་ལ་ཡང་བརྗོད་པར་མི་བགྱིད་ན་བཅབས་པར་བརྗོད་པར་བགྱི་འམ། ཉེ་བ༌[^2735]འཁོར་མི་བྱའོ། །

[Block 2888]
བཙུན་པ་རེ་ཞིག༌[^2736]དགེ་སློང་ལྟུང་བ་དང་བཅས་པ་དགེ་སློང་རྣམས་དང་ལྷན་ཅིག་གདུགས་ཡོལ་བར་བགྱིས་ནས་མཚན་མོ་དགེ་སློང་མི་གནས་པའི་གནས་ན་མཆིས་ཤིང་གང་ལ་ཡང་བརྗོད་པར་མི་བགྱི་ན་བཅབས་པར་བརྗོད་པར་མི་འགྱི་འམ་ཉེ་བ༌[^2737]འཁོར་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2889]
དོན་མེད་པས་ནི་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ནི་དོན་ཅུང་ཟད་ལ་ཡང་མི་ལྟོས་པར་མི་འགྲོ་འམ། གཞན་དུ་སོང་བས་ནི༌[^2738]ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 2890]
མཐའི་མདུན་རོལ་དུ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཉིན་མཚན་གྱི་མཐའི་མདུན་རོལ་དུ་བཅབས་པ་ཡང་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 2891]
འཆབ་པའི་སེམས་མ་བཏང་བ་ཉིད་ནི་དེའི་སེམས་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་འཆབ་པ་ཀུན་དུ་སྤྱོད་པ་དག་ཉིན་མཚན་གྱི་མཐར་འཆབ་པའི་སེམས་ཡིན་ཞིང་འཆབ་པར་འགྱུར་བ་འབའ་ཞིག་ཏུ་མ་ཟད་ཀྱི་ཇི་ལྟར་འཆབ་པའི་སེམས་མ་བཏང་ཞིང་ཡོངས་སུ་མ་སྤངས་པ་འདིས་ཀྱང་འཆབ་པ་དེའི་སེམས་ཉིད་ཡིན་པར་རིག་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2892]
འདིར་གཞུང་ནི་གང་གི་མདུན་དུ་འཆབ་པ་འབྱུང་བར་འགྱུར་བར༌[^2739]རང་བཞིན་དུ་གནས་པ་དང་། མཚམས་ཀྱི་ནང་ན་གནས་པ་ལ་གལ་ཏེ་མི་བརྗོད་ན་དེ་ཕྱིན་ཆད་འཆབ་པ༌[^2740]འབྱུང་བར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2893]
འདིར་བརྗོད་པ་རྗེས་སུ་སྒྲུབ་པར༌[^2741]མི་བྱེད་པ་ཙམ་ཁས་བླང་བར་བྱའི་འཆབ་པ་ལ་ཕྱོགས་པ་ཉིད་ནི་ཁས་བླང་བར་མི་བྱ་སྟེ། དེའི་ཕྱིར་དོན་འདི་ཐོས་པས་མདོ་འདི་བྱས་སོ། །

[Block 2894]
དགེ་སློང་ཕམ་པར་གྱུར་པས་ལྟུང་བ་ཕྱིར་མ་བཅོས་པ་ལ་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་ཇི་སྐད་དུ་འདི་ནི་ཡོད་ལ་ཕྱིར་མི་འཆོས་ན་ཡང་ཉེས་བྱས་སོ་ཞེས་སྔར་སྨོས་པ་དེའི་དམིགས་ཀྱིས་བསལ་བ༌[^2742]ཡིན་ཏེ་འབྱུང་བའི་ཡན་ལག་ཉིད་ཀྱི་ཕྱིར་འདིར་དེའི་སྡོམ་པ་ནི་དགོས་པ་མེད་པ་ཉིད་དུ་གྱུར་པའི་ཕྱིར་དེ་ལ་ཉེས་པ་མེད་པ་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 2895]
ཡང་དེའི་ཕྱིར་གང་ཟག་གི་གཞི་ལ་དུས་དང་དུས་མ་ཡིན་པར་བསྡུས་པ་འབྱུང་བའི་གཞི་ཞེས་མིང་དུ་བྱས་ཤེ་ན། འདི་ནི་ལྟུང་བ་དང་བཅབས་པ་སྤྱད་པ༌[^2743]རྣམས་ཀྱི་ལྡང་བའི་དུས་སོ་འདི་ནི་དུས་མ་ཡིན་ནོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2896]
བསྡུས་པ་འབྱུང་བ་ཞེས་བྱ་བ་ནི་ལྟུང་བ་རྣམས་ཀྱི་ཆོ་ག་མདོར་བསྡུས་པ་འདི་ཅིག་ཅར་དོན་གཅིག་ཏུ་འབྱུང་བའོ་ཞེས་བརྗོད་པའི་ཕྱིར་དེ་རིག་པར་བྱའོ། །

[Block 2897]
དུས་དང་དུས་མ་ཡིན་པར་བསྡུས་པ་འབྱུང་བའི་གཞི་ཞུ་བའི་སྐབས་སོ། །

[Block 2898]
དུས་དང་དུས་མ་ཡིན་པར་བསྡུས་པ་འབྱུང་བའི་གཞི་རྫོགས་སོ།། །།

[Block 2899 [HEADING]]
## ས་གཞན་ན་གནས་པ་སྤྱད་པའི་གཞི། ^8-0

[Block 2900]
ཡོངས་སུ་གནས་པ་དང༌[^2744]མགུ་བར་བྱ་བ་སྤྱོད་པ་དག་གིས་དགེ་སློང་རང་བཞིན་དུ་གནས་པ་ལས་མངོན་པར་སྨྲ་བ་དང་ཕྱག་དང་མངོན་དུ་ལྡང་བ་དང་ཐལ་མོ་སྦྱར་བ་དང་གུས་པའི་ལས་དག་བདག་གིར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ཡོངས་སུ་གནས་པ་དང་མགུ་བར་བྱ་བ་སྤྱོད་པ་དག་གིས་ཞེས་སྨོས་པས༌[^2745]ནི་གཞི༌[^2746]ནས་ཡོངས་སུ་གནས་པ་དང་། ཡང་གཞི་ནས་བསླང་སྟེ་ཡོངས་སུ་གནས་པ་དང་། གཞི་ནས་མགུ་བར་བྱ་བ་དང་། ཡང་གཞི་ནས་བསླང་སྟེ་མགུ་བར་བྱ་བ་སྤྱོད་པ་དག་ཀྱང་བསྡུས་པ་ཡིན་ཏེ། གང་གི་ཕྱིར་རྩོམ༌[^2747]པའི་བྱེ་བྲག་ལ་བརྟེན་པས་འདི་གཉིས་མངོན་པར་སྨྲ་བ་དག་གོ། །

[Block 2901]
དེ་བས་ན་དེ་སྤྱོད་པ་རྣམས་ལ་འདིར་མ་བསྡུས་པ་ཉིད་ནི་མ་ཡིན་ནོ། །

[Block 2902]
མངོན་པར་སྨྲ་བ་ཞེས་བྱ་བ་ནི་ཕྱག་འཚལ་ལོ་ཞེས་ཟེར་བ་སྟེ། མངོན་པར་ཞེས་བྱ་བ་སྟེ་བརྗོད་པའི་ཚིག་ཡིན་ལ། སྨྲས་པ་ཞེས༌[^2748]བྱ་བ་ནི་ཕྱག་འཚལ་བའི་ཚིག་ཡིན་པར་སྦྱར་རོ། །

[Block 2903 [VERSE]]
ཕྱག་ཅེས་བྱ་བ་ནི་ལུས་འདུད་པ་བསྡུས་པའོ། །
གུས་པའི་ལས་ཞེས༌[^2749]བྱ་བ་ནི་ལག༌[^2750]རྐྱོང་བ་དང་།
བསུ་བ་ལ་སོགས་པ་མཆོད་པའི་ལས་གཞན་དག་བསྡུའོ། །

[Block 2904]
དེ་གཉིས་ཀྱིས་མི་བྱ་བ་གང་ཡིན་པ་དེའི་སྐབས་གཞན་དག་གིས་ཀྱང་དེ་དག་ལའོ་ཞེས་བྱ་བ་ལ༌[^2751]དེ་གཉིས་ཀྱིས་ཞེས་བྱ་བ་ནི་ཡོངས་སུ་གནས་པ་དང་མགུ་བར་བྱ་བར་སྤྱོད་པ་དེ་གཉིས་ཀྱིས་སོ། །

[Block 2905]
མི་བྱ་བ་གང་ཡིན་པ་དེའི་སྐབས་ཞེས་བྱ་བ་ནི་རང་བཞིན་དུ་གནས་པ་ལས་ཅིག་ཤོས་རྣམས་ཀྱིས་སོ། །

[Block 2906]
དེ་དག་ལའོ་ཞེས་བྱ་བ་ནི་ཡོངས་སུ་གནས་པ་མགུ་བར་བྱ་བ་སྤྱོད་པ་དེ་དག་ལ་མངོན་པར་སྨྲ་བ་ལ་སོགས་པ་སྐབས་དེ་དག་མི་བྱ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2907]
རང་བཞིན་དུ་གནས་པ་རྣམས་ཀྱིས༌[^2752]དེ་དག་ལ་མངོན་པར་སྨྲ་བ་དང་ཕྱག་འཚལ་བ་ལ་སོགས་པ་མི་བྱའོ། །

[Block 2908]
དེ་དང་ལྷན་ཅིག་ཏུ་གོམ་པ་བསྲི་བ་ཉིད་ལས་གཞན་པས་བཅག་པར་མི་བྱའོ། །

[Block 2909]
སྟན་ཆས་དམའ་བ་ཉིད་ལས་གཞན་ལ༌[^2753]འདུག་པར་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ལྷན་ཅིག༌[^2754]པར་ཡང་མི་བྱ་ན་སྟན་གཅིག་ལ་ལྟ་སྨོས་ཀྱང་ཅི་དགོས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2910]
ཕྱི་བཞིན་འབྲེང་བའི་དགེ་སྦྱོང་གི་བདག་ཉིད་ལས༌[^2755]གཞན་པས་ཁྱིམ་དག༌[^2756]ཏུ་འགྲོ་བ་ཡང་ངོ་། །གཡོགས་མ་གཅིག༌[^2757]ཏུ་མལ་བཤམ་པར༌[^2758]མི་བྱའོ། །
--- END BLOCKS ---
