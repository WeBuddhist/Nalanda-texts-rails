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
[Block 806 [VERSE]]
བྷ་གའི་འོ་བྱེད་མི་རྟོག་གམ། །
བུ་ཁྱོད་སྨྲོས་ཤིག་རྡོ་རྗེ་ཅན། །
སློབ་མས་ཀྱང་འདི་ལྟར་བརྗོད་དེ། །
ཤུ་ཀྲ༌[^542]ཁྲག་སོགས་བཟའ་བ་ནི། །

[Block 807 [VERSE]]
ལྷ་མོ་ཅི་ཕྱིར་བདག་མི་ནུས། །
རཀྟ་ཤུ་ཀྲ་ཤ་ཆེན་དང་། །
བུད་མེད་རྣམས་ལ་དད་དེ་བཞིན། །
བྷ་གའི་པདྨར་ཙུམ་པ་ན། །

[Block 808]
ཐམས་ཅད་བདག་གི་ནུས་པ་ཉིད། །ཅེས་སློབ་མའི་ཚིག་ཐོས་ནས་ལག་པ་གཉིས་ཀྱིས་པདྨ་ཕྱེ་བར་བྱས་ཏེ། ནང་དུ་གནས་པའི་རྩའི་འཁོར་ལོ་བསྟན་པར་བྱེད་དེ། སྐྱེས༌[^543]བུ་གསང་བའི་པདྨ་འདི་ལ་རེ་ཞིག་བལྟ་བར་གྱིས་ཤིག །གང་གི་ནང་དུ་རྩ་རྣམ་པ་ལྔ་པོ་འདི་དག་ནམ་མཁའ་ལྔའི་ངོ་བོ་ཉིད་དུ་གནས་སོ། །

[Block 809]
དེ་ལ་འདོད་པའི་གདུགས་ཞེས་བྱ་བའི་རྩ་དབུ་མ་འདི་ནི་ཆུ་རྒྱུ་བ་ཐུགས་ཀྱི་རྡོ་རྗེའི་ངོ་བོ་ཉིད་དུ་ཤེས་པར་བྱའོ། །

[Block 810]
འདི་ནི་གཡོན་པའི་རྩ་སྟེ་རི་བོང་འཛིན་མ་ཞེས་བྱ་བ༌[^544]ཤུ་ཀྲ༌[^545]རྒྱུ་བ་སྟེ་བཅོམ་ལྡན་འདས་འོད་དཔག་ཏུ་མེད་པའི་བདག་ཉིད་དུ་ཤེས་པར་བྱའོ། །

[Block 811]
གཡས་པའི་རྩ་འདི་ཡང་ཁྲག་རྒྱུ་བ་སྟེ་རུས་སྦལ་མོ་ཞེས་བྱ་བ་བཅོམ་ལྡན་འདས་རིན་འབྱུང་གི༌[^546]ངོ་བོ་ཉིད་དུ་ཤེས་པར་བྱའོ། །

[Block 812]
དེ་བཞིན་དུ་མདུན་ན་གནས་པའི་རྩ་འདི་ཡང་ལྷ་སྦྱིན་མོ༌[^547]ཞེས་བྱ་བ་དྲི་ཆེན་རྒྱུ་བ་སྟེ། བཅོམ་ལྡན་འདས་རྣམ་པར་སྣང་མཛད་ཀྱི་ངོ་བོ་ཉིད་དུ་ཤེས་པར་བྱའོ། །

[Block 813]
དེ་བཞིན་དུ་ནུབ་ཀྱི་ཆ་ལ་གནས་པ་ནོར་རྒྱལ་མོ་ཞེས་བྱ་བ་རྩ་འདི་ནི་ཤ་རྒྱུ་བ་སྟེ་བཅོམ་ལྡན་འདས་དོན་ཡོད་གྲུབ་པའི་རང་བཞིན་དུ་ཤེས་པར་བྱའོ། །

[Block 814]
ནམ་མཁའ་ལྔའི་བདག་ཉིད་དེ་རྩ་བའི་འཁོར་ལོའི་ཕྱི་རོལ་དུ་འདབ་མ་བརྒྱད་པའི་པདྨ་འདི་འོད་གསལ་བའི་རྡོ་རྗེ་འཆང་ཆེན་པོའི་གཞལ་ཡས་ཁང་ཡིན་པར་ཤེས་པར་བྱའོ། །

[Block 815]
ཇི་སྐད་དུ་རྡོ་རྗེ་བདུད་རྩི་ལས།

[Block 816 [VERSE]]
བྷ་གའི་དབུས་སུ་ནམ་མཁའ་གང་། །
ནམ་མཁའ་ལྔ་པོ་རྣམ་པར་བརྒྱན།[^548] །
ལྟེ་བ་ཟེ་འབྲུ་རྣམས་དང་ལྡན། །
འདབ་མ་བརྒྱད་པོས་ཉེ་བར་མཛེས། །

[Block 817 [VERSE]]
དེར་གནས་རྟག་ཏུ་ཟག་པ་ནི། །
ཐིག་ལེ་བདུད་རྩིའི་ཚུལ་ཅན་ནོ། །

[Block 818]
ཞེས་འབྱུང་ངོ་། །དེ་བཞིན་དུ་དེ༌[^549]ཉིད་ལས་ཀྱང་གསུངས་ཏེ།

[Block 819 [VERSE]]
བདུད་རྩི་རྒྱུ་བའི་རྩ་གང་ནི། །
བྷ་གའི་གནས་སུ་རྣམ་པར་གནས།[^550] །
སུམ་ཅུ་རྩ་གཉིས་རྩ་གཞན་དག །
དེ་རྣམས་ཀྱི༌[^551]ནི་གཙོ་བོ་ཡིན། །

[Block 820]
ཞེས་འབྱུང་ངོ་། །གཞན་ཡང་། ཀྱེ་མའོ་ངའི་པདྨ་འདི། །

[Block 821 [VERSE]]
བདེ་བ་ཐམས་ཅད་ཡང་དག་ལྡན། །
ཆོ་ག་བཞིན་དུ་གང་བསྟེན་པ། །
དེ་ཡི་མདུན་ན་བདག་གནས་སོ། །
འདི་ནི་ཆོས་དབྱིངས་རྣམ་པར་དག །

[Block 822 [VERSE]]
སེམས་ཅན་ཁམས་ནི་གྲོལ་བར་བྱེད། །
བདེ་ཆེན་རྡོ་རྗེ་རྒྱལ་པོ་ཉིད། །
དངོས་ཀུན་གྱིས༌[^552]ནི་འདི་ལ་གནས། །

[Block 823]
ཞེས་སོ། །

[Block 824]
གཞན་ཡང་ནུ་མའི་སྣ་དང་པགས་པས༌[^553]གཡོགས་པ་སོར་བཞི་པའི་ལྟེ་བ་འཇམ་པ་དེ་ཉིད་བུད་མེད་ཀྱི་དབང་པོའོ། །

[Block 825]
གང་གི་ཕྱིར་དེ་ལ་ནི་རྩ་སྟོང་ཕྲག་བདུན་ཅུ་རྩ་གཉིས་དེ་ཉིད་དུ་འདུས་པ་དེའི་ཕྱིར་བདེ་བ་ཆེན་པོའི་མཚན་ཉིད་ཅན་གསང་བ་འདུས་པ་ཞེས་བྱའོ། །

[Block 826]
དེ་ལྟར་གཏམ་དག་སྨྲས་ཏེ་ལྷ་མོ་ཅང་མི་སྨྲ་བར་གྱུར་ཏོ། །

[Block 827]
སློབ་མས་ཀྱང་དེའི་པདྨར་ལག་པ་གཡོན་པའི་སོར་མོ་ཕྱག་རྒྱར་བཅིངས་ཏེ་འཇུག་པར་བྱ་སྟེ། མིག་དང་ལྕགས་ཀྱུ་དང་སྣམ་བུ་དང་བ་དན་ནོ། །

[Block 828]
ཕྱག་རྒྱའི་སྦྱོར་བ་དེས་དེ་སྲིད་བསྐྱོད་པར་བྱ་བ་ནི་ཇི་སྲིད་མཁུར་ཚོས་དམར་བ་དང་བ་སྤུ་ལྡང་བ་དང་། དགའ་བ་དམ་པ་སྐྱེས་པའི་དམ་ཚིག་གི་ཕྱག་རྒྱ་སློབ་པའི་མགྲིན་པར་རང་ཉིད་ཀྱིས་འཁྱུད་པའི་བར་དུ་བྱའོ། །

[Block 829]
དེའི་རྗེས་སུ་རྡོ་རྗེ་མཁྲེགས་མོའི་སྟེང་དུ་ཉེ་བར་འདུག་སྟེ་མཆོག་གི་བསྙེན་པ་ལ་སོགས་པའི་རིམ་པ་ཡང་དག་པར་བཟླ་བར༌[^554]བྱའོ། །

[Block 830]
དེ་ལ་བསྒྲུབ་བྱ་དང༌[^555]སྒྲུབ་བྱེད་ཀྱི་སྦྱོར་བ་ནི་བསྙེན་པའོ། །

[Block 831]
རྡོ་རྗེ་དང་པདྨ་མཉམ་པར་སྦྱོར་བ་ནི་ཉེ་བར་བསྒྲུབ༌[^556]པའོ། །

[Block 832]
ས་བོན་གྱི་བྱིན་གྱིས་བརླབས་པའི་རྡོ་རྗེ་དང་པདྨས་བསྐྱོད་པ་ནི་སྒྲུབ་པའོ། །

[Block 833]
བདེ་བ་ཆེན་པོ་ཉམས་སུ་མྱོང་བ་ནི་སྒྲུབ་པ་ཆེན་པོའོ༌[^557]ཞེས་མཆོག་གི་བསྙེན་པ་ལ་སོགས་པའོ། །

[Block 834]
རྒྱུད་ཕྱི་མ་ལས་ཀྱང་།

[Block 835 [VERSE]]
བསྒྲུབ་བྱ་སྒྲུབ་བྱེད་སྦྱོར་བ་ནི། །
གང་ཕྱིར་བསྙེན་པར་བརྗོད་པ་སྟེ། །
རྡོ་རྗེ་པདྨ་མཉམ་སྦྱོར་བས། །
ཉེ་བར་སྒྲུབ་པ་ཞེས་སུ་བསྟན། །

[Block 836 [VERSE]]
ཡི་གེ་ཧཱུཾ་དང་ཕཊ་ལྡན་པའི། །
བསྐྱོད་པ་སྒྲུབ་པར་རབ་ཏུ་གྲགས། །
རང་ཞི་རང་བདེ་རང་ངོ་བོ། །
སྒྲུབ་པ་ཆེན་པོར་རབ་ཏུ་བཤད། །

[Block 837 [VERSE]]
དཔལ་ལྡན་སངས་རྒྱས་ཀུན་གྱི་བདག །
རྡོ་རྗེ་འཆང་བའི་གོ་འཕང་ཆེ། །
ཆོ་གའི་སྦྱོར་བ་འདི་ཡིས་ནི། །
མྱུར་དུ་དངོས་གྲུབ་ཐོབ་པར་འགྱུར། །

[Block 838]
ཞེས་འབྱུང་ངོ་། །གནས་སྐབས་དེ་ལ་རྡོ་རྗེ་དབྱིངས་ཀྱི་དབང་ཕྱུག་མ་དང་། སྙོམས་པར་ཞུགས་པའི་སློབ་མ་མཐོང་ནས་རང་གི་སྙིང་ག་ནས་གཏི་མུག་དགའ་མ་ལ་སོགས་པ་བཞི་སྤྲོས་ཏེ་སློབ་མའི་ཁ་ལ་འཇུག་པར་བྱས་ལ། །གཏི་མུག་དང་ཞེ་སྡང་དང་འདོད་ཆགས་དང་ཕྲག་དོག་གི་རྒྱུན་རྣམས་ཀྱིས་སློབ་དཔོན་གྱིས༌[^558]རིམ་པ་འདིས་དབང་བསྐུར་བར་བྱ་སྟེ། རང་གི་སྙིང་གའི་ཡེ་ཤེས་སེམས་དཔའི་ཕྱག་མཚན་གྱི་ས་བོན་གྱི་ཐིག་ལེ་ལས་འོད་ཟེར་གྱི་སྒོ་ནས་སངས་རྒྱས་སྤྱན་མ་དང་སྙོམས་པར་ཞུགས་པའི་རྣམ་པར་སྣང་མཛད་སེམས་དཔའ་གསུམ་གྱི་བདག་ཉིད་ཅན་རྣམ་པར་སྤྲོ་ཞིང་སློབ་མའི་ཁ་ལ་འཇུག་པ་སྟེ། དེའི་ཡང་སྙིང་གར་ནམ་མཁའི་དབྱིངས་ནས་རྣམ་པར་སྣང་མཛད་ཀྱི་ཚོགས་འཇུག་པར་བྱས་ལ། །བདེ་བ་ཆེན་པོ་འབབ་པའི་དབང་གིས་ཞུ་ཞིང་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་ཐིག་ལེའི་གཟུགས་སུ་གྱུར་པ་གཏི་མུག་གི་རྒྱུན་དེས་དབང་བསྐུར་བར་བྱའོ་ཞེས་གཏི་མུག་གི་རྒྱུན་གྱི་དབང་ངོ་། །

[Block 839]
དེ་བཞིན་དུ་སྙིང་གའི་འོད་ཟེར་གྱིས་གོས་དཀར་མོ་དང་སྙོམས་པར་ཞུགས་པའི་སྣང་བ་མཐའ་ཡས་སེམས་དཔའ་གསུམ་གྱི་བདག་ཉིད་ཅན་རྣམ་པར་སྤྲོས་ཤིང་། སློབ་མའི་ཁ་ལ་བཅུག་སྟེ། དེའི་ཡང༌[^559]སྙིང་གར་སྣང་བ་མཐའ་ཡས་ཀྱི་ཚོགས་ནམ་མཁའི་དབྱིངས་ནས་བཀུག་ཅིང་བཅུག༌[^560]ལ་བདེ་བ་ཆེན་པོ་འབབ་པའི༌[^561]དབང་གིས་ཞུ་ཞིང་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་ཐིག་ལེའི་གཟུགས་སུ་གྱུར་པ་འདོད་ཆགས་ཀྱི་རྒྱུན་དེས་དབང་བསྐུར་བར་བྱའོ་ཞེས་འདོད་ཆགས་ཀྱི་རྒྱུན༌[^562]གྱི་དབང་ངོ་། །དེ་བཞིན་དུ༌[^563]སྙིང་གའི་འོད་ཟེར་གྱིས་མཱ་མ་ཀཱི་དང་སྙོམས་པར་ཞུགས་པའི་མི་བསྐྱོད་པ་སེམས་དཔའ་གསུམ་གྱི་བདག་ཉིད་ཅན་རྣམ་པར་སྤྲོ་ཞིང་སློབ་མའི་ཁ་ལ་བཅུག་སྟེ། དེའི་ཡང་སྙིང་གར་མི་བསྐྱོད་པའི་ཚོགས་ནམ་མཁའི་དབྱིངས་ནས་བཀུག་ཅིང་བཅུག་ལ་བདེ་བ་ཆེན་པོ་འབབ་པའི་དབང་གིས་ཞུ་ཞིང་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་ཐིག་ལེའི་གཟུགས་སུ་གྱུར་པ་ཞེ་སྡང་གི་རྒྱུན་དེས་དབང་བསྐུར་བར་བྱའོ་ཞེས་ཞེ་སྡང་གི་རྒྱུན་གྱི་དབང་ངོ་། །དེ་བཞིན་དུ་ཡང་སྙིང་གའི་འོད་ཟེར་གྱིས་དམ་ཚིག་སྒྲོལ་མ་དང་སྙོམས་པར་ཞུགས་པའི་དོན་ཡོད་གྲུབ་པ་སེམས་དཔའ་གསུམ་གྱི་བདག་ཉིད་ཅན་རྣམ་པར་སྤྲོས༌[^564]ཞིང་སློབ་མའི་ཁ་ལ་བཅུག་སྟེ། དེའི་སྙིང་གར་དོན་ཡོད་གྲུབ་པའི་ཚོགས་ནམ་མཁའི་དབྱིངས་ནས་བཀུག་ཅིང་བཅུག་ལ་བདེ་བ་ཆེན་པོ་འབབ་པའི་དབང་གིས་ཞུ་ཞིང་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི༌[^565]ཐིག་ལེའི་གཟུགས་སུ་གྱུར་པ་ཕྲག་དོག་གི་རྒྱུན་དེས་དབང་བསྐུར་བར་བྱའོ་ཞེས་ཕྲག་དོག་གི་རྒྱུན་གྱི་དབང་ངོ་། །དེ་ལྟར་དབང་བསྐུར་བ་བཞིས་དབང༌[^566]བསྐུར་བས་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི༌[^567]ངོ་བོ་ཉིད་ཀྱིས་ཕུང་པོ་དང་ཁམས་རྒྱས་པར་བྱས་པ་ཞེས་འབྱུང་བ་རྒྱས་པ་སྔོན་དུ་འགྲོ་བ་ཤེས་རབ་ཡེ་ཤེས་ཀྱི་དབང་ངོ་། །

[Block 840]
དེའི་རྗེས་སུ་སློབ་མ་ལངས་ཏེ་ཐལ་མོ་སྦྱར་ཞིང་སློབ་དཔོན་གྱི་མདུན་དུ་འདུག་ནས་གསོལ་བ་འདེབས་པའི་སློབ་མ་ལ་མན་ངག་གདབང་བཞི་པ་འདི་བསྟན་པར་བྱ་སྟེ། ཐབས་དང་ཤེས་རབ་སྙོམས་པར་ཞུགས་པའི་དུས་སུ་ཚང་བའི༌[^568]བུ་ག་ནས་འཕོ་བའི་བྱང་ཆུབ་ཀྱི་སེམས་ལས་འབྱུང་བ་ཁྱོད་ཀྱིས་གང་མྱོང་བ་དེ་ནི་སྣང་བའི་ཡེ་ཤེས་དང་འདོད་ཆགས་དང་བྲལ་བ་དང་། རྣམ་པ་སྣ་ཚོགས་པའི་སྐད་ཅིག་མའི་བདག་ཉིད་དང་། དེ་ནས༌[^569]བསྙེན་པ་དང་དགའ་བའི་རྣམ་གྲངས་ཅན་དུ་ཤེས་པར་གྱིས་ཤིག །དེའི་རྗེས་ལ་བྱང་ཆུབ་ཀྱི་སེམས་ཡན་ལག་ཐམས་ཅད་དུ་ཁྱབ་པ་ན་ཁྱོད་ཀྱིས་བདེ་བ་གང་མྱོང་བ་དེ་ནི་སྣང་བ་མཆེད་པའི་ཡེ་ཤེས་ཏེ་རྣམ་པར་སྨིན་པའི་སྐད་ཅིག་མའི་བདག་ཉིད་ཅན་ཉེ་བར་སྒྲུབ་པ་དང་། མཆོག་ཏུ་དགའ་བའི་ངོ་བོ་ཉིད་དུ་ཤེས་པར་གྱིས་ཤིག །དེའི་འོག་ཏུ་རྡོ་རྗེའི་ནང་དུ་སོན་པའི༌[^570]བྱང་ཆུབ་ཀྱི་སེམས་ལས་ཁྱོད་ཀྱིས་བདེ་བ་གང་མྱོང་བ་དེ་ནི་སྣང་བ་ཐོབ་པའི་ཡེ་ཤེས་ཏེ་རྣམ་པར་འཇོམས་པའི་སྐད་ཅིག་མའི་བདག་ཉིད་ཅན་སྒྲུབ་པ་དང་། འདོད་ཆགས་བར་བའི་ངོ་བོ་ཉིད་དུ་ཤེས་པར་གྱིས་ཤིག །དེ་ནས་ཡང་རྡོ་རྗེ་ནོར་བུའི་རྩེ་མོར་ཕྱིན་པའི་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་བདེ་བ་ཆེན་པོ་ཉམས་སུ་མྱོང་བས་སྒོ་རྣམས་འགགས་པས་སེམས་ཀྱི་རྣམ་པར་རྟོག་པའི་ཚོགས༌[^571]ཐིམ་ཞིང་རབ་ཏུ་ཞི་བའི་གནས་ལ་སོགས་པའི་ཚོགས་རོ་གཅིག་པར་གྱུར་པ་ཡེ་ཤེས་མཐོང་བ་གང་ཡིན་པ་དེ་ནི་སྣང་བ་ལ་སོགས་པ་གསུམ་དང་བྲལ་བ། འདོད་ཆགས་དང་། འདོད་ཆགས་དང༌[^572]བྲལ་བ་དང་།[^573] འདོད་ཆགས་བར༌[^574]སྤངས་པ་ཐབས་དང་ཤེས་རབ་གཉི་ག༌[^575]ལས་འདས་པ་དེ་ནི་འོད་གསལ་བ་གཉིས་སུ་མེད་པའི་ཡེ་ཤེས་སྒྲུབ་པ་ཆེན་པོ་མཚན་ཉིད་དང་བྲལ་བའི་སྐད་ཅིག་མ་བདེ་བ་ཆེན་པོར་ཤེས་པར་གྱིས་ཤིག །དེ་ལྟར་དྲི་མ་ཐམས་ཅད་དང་བྲལ་བའི་ཡེ་ཤེས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་ཆོས་ཀྱི་དབྱིངས་ཀྱི་ངོ་བོ་ཉིད་དུ་ཤེས་པར་གྱིས་ཤིག །སྐྱེས༌[^576]བུ་མཚན་མོ་ཡང་མ་ཡིན། ཉིན་མོ་ཡང་མ་ཡིན། མཚམས་ཀྱང་མ་ཡིན་ཏེ། སྣང་བ་ཡང་མ་ཡིན། སྣང་བ་མཆེད་པ་ཡང་མ་ཡིན། [^577]སྣང་བ་ཐོབ་པ་ཡང་མ་ཡིན་པ། གཉིད་ལོག་པ་ཡང་མ་ཡིན་པ། སད་པ་ཡང་མ་ཡིན། ཆགས་པ་དང་། ཆགས་པ་དང༌[^578]བྲལ་བ་དང་། ཆགས་པ་བར་མའི་རང་བཞིན་རྣམས་དང་བྲལ་བའི་འོད་གསལ་བའི་ཡེ་ཤེས་ལ༌[^579]དུས་ཐམས་ཅད་དུ་གནས་པར་གྱིས་ཤིག །དེ་ནས་རྡོ་རྗེ་སློབ་དཔོན་གྱི་བཀའ་དྲིན་ཐོབ་པའི་སློབ་མ་ཐལ་མོ་སྦྱར་བར་གྱུར་པས་དེ་ཁོ་ན་ཉིད་ཐོབ་པ་ལ་རྗེས་སུ་ཡི་རང་ཞིང་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་ཚིགས་སུ་བཅད་པ་འདི་རྗོད་པར་བྱེད་དེ།

[Block 841 [VERSE]]
ཨོཾ་དངོས་པོ་ཐམས་ཅད་ལས་འདས་ཤིང་། །
ཕུང་པོ་ཁམས་དང་སྐྱེ་མཆེད་བྲལ། །
གཟུང་དང་འཛིན་པ་རྣམ་སྤངས་པ། །
ཆོས་རྣམས་བདག་མེད་མཉམ་ཉིད་ཀྱིས། །

[Block 842 [VERSE]]
རང་སེམས་གདོད་ནས་མ་སྐྱེས་པ། །
སྟོང་པ་ཉིད་ཀྱི་ངོ་བོ་ཡིན། །

[Block 843]
ཞེས་བྱ་བ་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་སྔགས་འདི་བརྗོད་ཅིང་། བླ་མའི་ཞབས་ཀྱི་རྩ་བར་སྙིམ་པའི་མེ་ཏོག་དབུལ་བར་བྱའོ་ཞེས་འདི་ནི་ནང་གི་མངོན་པར་བྱང་ཆུབ་པའི་རིམ་པའོ། །

[Block 844]
དེའི་དཔེ་ནི་ཉིན་མོ་སྣང་བ་མཆེད་པའི་ཡེ་ཤེས་སོ། །

[Block 845]
མཚན་མོ་ནི༌[^580]སྣང་བའི་ཡེ་ཤེས་སོ། །
--- END BLOCKS ---
