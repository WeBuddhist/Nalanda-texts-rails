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
[Block 876]
གང་ཞིག་ཐ་དད་པ་གང་ལས་ལྡོག་པར་འགྱུར་བ་དེ་ཉིད་དེར་འགྱུར་བའི་ཕྱིར། འདི་འདི་ལས་ཐ་དད་པར་ཡིན༌[^731]ནོ་ཞེས་བྱ་བར་མི་འགྱུར་ཏེ། ཕན་ཚུན་ཐ་དད་པར་འགྱུར་བའི་འབྲེལ་པ་ནི་མེད་པའི་ཕྱིར་རོ། །

[Block 877]
འབྲེལ་པ་ཡོད་པ་ཡིན་ན་ཡང་དེ་རྒྱུ་དང་འབྲས་བུའི་དངོས་པོ་ཡིན་པས་དེ་ལས་སྐྱེས་པའི་དངོས་པོ་ཐ་དད་པ་ཞེས་བྱ་བར་བྱེ་བྲག་མེད་པའི་ཕྱིར། རང་གི་རྒྱུ་རྣམས་ཀྱི་འབྲས་བུ་ཐམས་ཅད་ལྡོག་པར་འགྱུར་རོ། །

[Block 878]
ཐ་དད་པའི་དངོས་པོ༌[^732]གཞན་ཡིན་པ༌[^733]དེ་ལས་ཀྱང་འདི་ཐ་དད་པ་ཡིན་པས༌[^734]ཐ་དད་པའི་ཁྱད་པར་ཉིད་ཀྱིས་རྫས་གཞན་དང་འདྲ་བར་ཐ་དད་པར་མི་འགྱུར་རོ། །

[Block 879]
ཐ་དད་པའི་ཁྱད་པར་ཁོ་ན༌[^735]ཐ་དད་པ་མ་ཡིན་ཏེ། འདི༌[^736]འདི་ལས་ཞེས་བྱ་བའི་ཁྱད་པར་བསྟན་པའི་ཕྱིར་རོ། །

[Block 880]
དེ་བས༌[^737]ན་ཁྱད་པར་གྱི་དངོས་པོ་མེད་པ་ལ་ཐ་དད་པ་ཉིད་ཀྱིས༌[^738]དངོས་པོ་མེད་པར་འགྱུར་བ་དེ་བས་ན་གཞན་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 881]
དེ་རྣམ་པ་གཞན་དུ་ཡོད་པ་མ་ཡིན་པའི་ཕྱིར་དངོས་སུ་ན་དོན་དམ་པ་མ་ཡིན་ནོ། །

[Block 882]
འོ་ན་ཅི་ལྟར་དངོས་པོ་ཐ་དད་པ་མེད་པ་སྒྲས་བརྗོད་པ་ན་དེ་ཉིད་གཞན་ལ༌[^739]ཐ་དད་པའི་ཕྱིར། ཆ་མེད་པའི་ཐ་དད་པ་གཅིག་བརྗོད་པ་ན་ཐ་དད་པ་ཐམས་ཅད་རྟོགས་པས་དེ་ལས༌[^740]སྒྲ་དང་ཚད་མ་གཞན་དོན་མེད་པར་ཇི་ལྟར་མི་འགྱུར་ཞེ་ན། འདི་ལ་ཉེས་པ་མེད་དེ་གང་གི་ཕྱིར།

[Block 883 [VERSE]]
འདྲེས་པ༌[^741]དོན་གཅིག་གཅོད་པ་ན། །
སྒྲའམ་རྟགས་ནི་གཅིག་པུ་ཡི། །
བྱ་བ་དེ་ལ་དངོས་པོ་ཡི། །
བརྗོད་བྱ་གཅད་པ༌[^742]ཅི་ཡང་མེད། །

[Block 884 [VERSE]]
གང་གི་རྗོད༌[^743]པར་བྱེད་པ་དང་། །
དངོས་པོའི་ནུས་པ༌[^744]མ་ལུས་པ། །
རྟོགས་འགྱུར་དེའི་ཕྱིར་ན་སྒྲ། །
འབྲས་བུ་དུ་མ་རྟེན༌[^745]གཅིག་འགྱུར། །

[Block 885]
དཔེར་ན་ཕྱི་ནང་ཐ་དད་པའི་འདྲེས་པ་ཅན་གྱི་བློ༌[^746]རང་ཉིད་ཀྱི་སྣང་བ་ཐ་སྙད་ཀྱི༌[^747]ཡུལ་དོན་བྱེད་པར་རུང་བ་ངེས་པར་བྱས་ནས་སྒྲའི་དོན་ཉེ་བར་སྦྱོར་བར་བྱེད་དོ་ཞེས་སྔར་བཤད་པ་ལྟ་བུའོ། །

[Block 886]
འཁྲུལ་པའི་རྒྱུ་དེ་དང་དེ་དག་གིས་འདྲེས་པའི༌[^748]ངོ་བོ་ལྟ་བུར་སྣང་བ་བརྡ་ཇི་ལྟ་བ་བཞིན་དུ་རྣམ་པར་གཅད༌[^749]པའི། ཕྱིར་དེ་ཉིད་ལ་སྒྲ་དེ་དག་གི་བྱ་བ་ཉིད་ཡིན་ཏེ། གཅིག་པ་བསྒྲུབས༌[^750]ན་ཡང་གཞན་རྣམ་པར་གཅོད་པར་མི་བྱེད་དེ། བརྡ་སོ་སོར་ངེས་པའི་ཕྱིར་རོ། །

[Block 887]
དངོས་པོ་རྣམ་པར་གཅད་པས༌[^751]འཕངས་པ་ཅི་ཡང་མེད་མོད་ཀྱི། འོན་ཀྱང་གང༌[^752]གི་རྗོད་པར་བྱེད་པ་དང་། དངོས་པོ་ཉིད་ཀྱི་སྟོབས་ཀྱིས་ནི་མ་ལུས་པར་རྟོགས་པར༌[^753]འགྱུར་ཏེ། སྒྲ་རྣམས་ནི་བློའི༌[^754]བསླད་པའི་ཡུལ་ཅན་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 888]
དེ་ལ་དངོས་པོ་མེད་པ་ཡང་དངོས་པོའི་ནུས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 889]
ཐ་སྙད་འདི་ནི་ཡང་དག་པའི་དོན་དེ་བཞིན་དུ་མཐོང་བའི་སྒོ་ནས་ཆོས་དུ་མ་དང་། གཅིག་དང་། ཐ་དད་པ་དང་། ཐ་དད་པ་མ་ཡིན་པར་སྣང་བ་འཁྲུལ་པའི་རྗེས་སུ་འབྲང་བའི་ཕྱིར། དེ་དང་དེར་འབྲེལ་པར་འགྱུར་བ་ལས་དུ་མ་འཁྲུལ་པ་ཡིན་ནོ། །

[Block 890]
དེ་བཞིན་དུ་མ་ཡིན་པ་དེ་ལས་ཀྱང་མཐར་ཡང་དག་པ་ཉིད་ཀྱི་དངོས་པོ་ལ་ཤེས་པ་མི་བསླུ་བའི་ཕྱིར་རོ། །

[Block 891]
རྣམ་པ་ཐ་དད་པར་འཛིན་པའི་ཤེས་པ་དང་སྒྲ་ཐ་དད༌[^755]ཀྱང་དངོས་པོ་གཅིག་གི་ཡུལ་ཅན་ཉིད་ཡིན་པའི་ཕྱིར། སྒྲ་འབྲས་བུ་དུ་མ་ཅན་རྟེན༌[^756]གཅིག་པ་མ་ཡིན་ཏེ་འགལ་བའི་ཕྱིར་རོ། །

[Block 892]
ཇི་སྐད༌[^757]བརྗོད་པའི་བློའི་སྣང་བ་ལ་བརྟེན་པ་ལ་ཉེས་པ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 893 [VERSE]]
གཅིག་ཅིག་རྣམ་གཅོད་སྟོན་པ་ན། །
གང་ཚེ་གཞན་སྤོང་མི་འཇུག་པ། །
དེ་ནི་དེས་ཁྱབ་གཅིག་ཏུའང་སྣང་། །
དེ་ཚེ་བློ་ཡི་ངོར་བྱས་ནས། །

[Block 894 [VERSE]]
གཞི་མཐུན་པ་ནི་ཉིད་དུ་འགྱུར། །
སྒྲ་ནི་རྣམ་གཅོད་བྱེད་པ་ན། །
དངོས་པོའི་ཆོས་ལ་རེག་འགྱུར་བ། །
དེ་ནི་དེ་ལ་ཡོད་དོ་ཞེས། །

[Block 895 [VERSE]]
བྱའོ་དངོས་གཅིག་བརྗོད་བྱ་མིན། །
བློ་ལ་སྣང་བ་མིན་མཐོང་ལ། །
དངོས་པོ་མེད་པར་ངེས་ཕྱིར་རོ། །

[Block 896]
ཞེས་བྱ་བ་ནི་བར་སྐབས་ཀྱི་ཚིགས་སུ་བཅད་པའོ། །

[Block 897 [HEADING]]
### སྒྲ་དང་བློ་སྤྱིའི་སྤྱོད་ཡུལ་ཅན། ^4-3-0

[Block 898 [VERSE]]
དེ་ཕྱིར་གཞན་སེལ་ཡུལ་ལ་ནི། །
སྒྲ་རྣམས་ཀྱིས༌[^758]ནི་བློ་ཉིད་ཀྱང་། །
སྤྱིའི་སྤྱོད་ཡུལ་ཅན་བསྟན༌[^759]ཏེ། །
དངོས་ལ་དེ་དག་མི་སྲིད་ཕྱིར། །

[Block 899]
གལ་ཏེ་བསྒྲུབ་པའི༌[^760]ཚུལ་ལ༌[^761]དངོས་པོ་ཉིད་ལ་སྒྲ་དང་རྣམ་པར་རྟོག་པ་རྣམས་ཀྱིས་ཡུལ་དུ་བྱེད་ན་དེ་ནི་འདིར་དོན་ཐམས་ཅད་ལ་ཐམས་ཅད་དུ་རྟོགས་པར་ཐལ་བར་འགྱུར་བ་དང་། གཞི་མཐུན་པ་ཉིད་ལ་སོགས་པ་མེད་དོ་ཞེས་རིགས་པའི་བསྟན་བཅོས་མཛད་པ་པོས་དགོངས་ནས་གཞན་སེལ་བའི་ཡུལ་ཅན་ལ་དེ་དག་རབ་ཏུ་བསྟན་ཏོ། །

[Block 900]
དེ་ལྟར་ན། དངོས་པོའི་ངོ་བོ་གཅིག་ཉིད་ཕྱིར། །གང་ལས་ཐ་དད་ངོ་བོར་འདོད།[^762] །

[Block 901]
གཅིག་ལ་རྗེས་སུ་འགྲོ་བ་དང་། །ལྡོག་པའི༌[^763]དོན་གཅིག་སྤྱོད་ཡུལ་མིན། །

[Block 902]
དེ་ནི་དངོས་པོ་ཆ་མེད་པ་གཅིག་པོ་ཡིན་ན་ཇི་ལྟར་ན་བློ་རྣམ་པ་ཐ་དད་པ་དག་གི༌[^764]ཡུལ་དུ་བྱེད་དེ། རྣམ་པ་ཐ་དད་པ་ནི་ཐ་དད་པ༌[^765]ལ་བརྟེན་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 903]
དེ་ཡང་ཐ་མི་དད་པའི་ཕྱིར་ཏེ་སྤྱི་ནི་དེའི་བདག་ཉིད་ཡིན་དུ་ཟིན་ཀྱང་དེ་ནི་གྲུབ་པ་དང་བདེ་བ་གཅིག་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 904]
དེ་བས་ན་འདི་ནི་དོན་ཕན་ཚུན་སྤངས་པའི་སྒོ་ནས་ཡུལ་གཅིག་ལ་འཇུག་ཏུ་མི་རུང་བའི་ཕྱིར། གཞི་མཐུན་པ་ཉིད་ལ་སོགས་པར་མི་འགྱུར་རོ། །

[Block 905]
དངོས་པོའི་བདག་ཉིད་གཅིག་པུ་དེ་ཉིད་ལ་འཇུག་པ་དང་མི་འཇུག་པ་མི་རིགས་ཏེ་འགལ་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 906]
གཞན་དུ་མི་འཇུག་པ་ཡང་སྤྱི་ཉིད་དུ་མི་འགྱུར་རོ། །

[Block 907]
གལ་ཏེ་སྤྱིའི་འཇུག་པ་ཡིན་གྱི་ཁྱད་པར་གྱི་མ་ཡིན་ནོ་ཞེ་ན། མ་ཡིན་ཏེ། ཐ་དད་པ་མེད་པའི་ཕྱིར་ཏེ། [^766]དེ་ནི་ངོ་བོ་གཅིག་པ་སྤྱི་འམ་ཁྱད་པར་དུ་འགྱུར་གྲང༌[^767]ན། ངོ་བོ་ཐ་དད་པ་མེད་པ་འདི༌[^768]ལ་ནི་རབ་ཏུ་དབྱེ་བ་མི་རིགས་པ་ཡོད་ན་ཡང་ཐ་དད་པ་མེད་པར་མི་འགྱུར་རོ་ཞེས་བསྟན་པའི་ཕྱིར་རོ།[^769] །དེ་བས་ན་དབྱེ་བ་མེད་པ་འདི་ནི་རྗེས་སུ་འགྲོ་བ་མེད་པ་ཡང་རྗེས་སུ་འགྲོ་བ་དང་ལྡན་པ་ཡང་མ་ཡིན་ནོ། །

[Block 908]
གང་ཡང་སྤྱི་ནི་ཐ་དད་པ་ཉིད་དུ་སྨྲ་བ་དེ་ལ་ཡང་།

[Block 909 [VERSE]]
ཐ་དད་གྱུར་ན་ཐ་དད་མེད། །
ཐ་སྙད་དག་ཀྱང་རྒྱུ་མེད་འགྱུར། །

[Block 910]
སྒྲ་དག་གིས་བདག་ཉིད་ཇི་ལྟ་བ་བཞིན་དུ་དོན་ཐ་དད་པ་བརྗོད་པ་ན་ཇི་ལྟར་དོན་གཅིག་པ་ཅན་གྱི་བློའི་རྟེན༌[^770]དུ་འགྱུར། དོན་གཞན་བརྗོད་པ་ན་ཡང་ཐེ་ཚོམ་མེད་པ་ཉིད་ཀྱི་ཕྱིར་ལྟོས་པ་མེད་པ་ཉིད༌[^771]ན་ཇི་ལྟར་ཁྱད་པར་དང་ཁྱད་པར་གྱི༌[^772]གཞིའི་དངོས་པོ་ལ་བརྟེན་པར་འགྱུར།

[Block 911 [VERSE]]
ལྡོག་པ་ཀུན་ལ་ཡོད་པའི་ཕྱིར། །
ཐལ་འགྱུར་ཉེས་པ་དེ་དག་མེད། །

[Block 912]
ཇི་ལྟར་གཅིག་པོ་དེ་ལས་ཐ་དད་པ་དེ་བཞིན་དུ་གཞན་དག་ཀྱང་ཡིན་པའི་ཕྱིར། ཐ་དད་པ་ལ་སྤྱི་མེད་པའི་ཉེས་པ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 913]
ཉེས་པ་ལྷག་མ་མེད་པར་ནི་སྔར་བསྟན་ཏོ། །

[Block 914]
འོན་ཀྱང་།

[Block 915 [VERSE]]
དེ་ཡི་འབྲས་བུ་ཡོངས་བསྟན་ཕྱིར། །
ཐ་དད་འབྲས་བུ་གཅིག་དད་ལ། །
མཁས་པས་སྒྲ་གཅིག་བརྡར་བྱས་པ། །
དེ་ཡི་འབྲས་བུ་མེད་པ་ཅན། །
--- END BLOCKS ---
