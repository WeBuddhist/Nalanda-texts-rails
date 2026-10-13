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
[Block 946]
ཡང་དུས་ཀྱི་དབང་གིས་དེ་དུམ་བུ་བཞིར་གས་ནས་གླིང་བཞི་དང་དཀྱིལ༌[^663]དུ་རི་རབ་ཀྱི་རྒྱལ་པོ་ཡང་དག་པར་བྱུང་བར་གྱུར་ཏོ།[^664] །

[Block 947]
དེ་ནས་དེ་དག་ཀྱང་དེ་ཉིད་དུ་བབས་སོ། །

[Block 948]
བག་ཆགས་ལྡང་བའི་ཤུགས་ཀྱིས་བུད་མེད་དང་སྐྱེས་པའི་རྟགས་སུ༌[^665]གྱུར་པས་ཕན་ཚུན་འབྲེལ་པའི་དབང་གིས་སྐྱེ་དགུ་དང་རིགས་བཞིའི་ཐ་སྙད་ཀྱང་འབྱུང་ངོ་། །མ་རྨོས་པར༌[^666]སྨིན་པའི་འབྲས་ལ་སོགས་པའི་འབྲུ་རྣམས་དང་། དེ་དག་བསྲུང་བར་བྱ་བའི་ཕྱིར་མཐའ་ཡས་གྲགས་པ་ལ་སོགས་པ་རྒྱལ་པོ་རྣམས་བྱུང་ངོ་། །བདག་དང་གཞན་གྱི་དབྱེ་བའི་དབང་གིས་ང་དང་བདག་ཏུ་འཛིན་པ་བྱུང་ངོ་། །དེའི་རྩ་བ༌[^667]ཅན་ནི་འདོད་ཆགས་ལ་སོགས་པའི་ཉོན་མོངས་པ་དང་དེ་ལས་བྱུང་བའི་དགེ་བ་དང་མི་དགེ་བའི་ལས་དང་། དེའི་རྒྱུ་ཅན་བདེ་འགྲོ་དང་ངན་འགྲོ་དག་ཅེས་ཟོ་ཆུན་གྱི་འཁྲུལ་འཁོར་བཞིན་དུ་ཡོངས་སུ༌[^668]འཁོར༌[^669]བའི་དགོན་པར་འཁོར་བར་གྱུར་ཏོ། །

[Block 949]
དེ་ནས་བཅོམ་ལྡན་འདས་རྡོ་རྗེ་འཆང་ཆེན་པོས་སྙིགས་མ་ལྔའི་དུས་སུ་ཉོན་མོངས་པ་ལྔས་དཀྲུགས་པའི་སེམས་ཅན་གྱི་ཁམས་ལ་གཟིགས་ཏེ། ཉན་ཐོས་ལ་སོགས་པའི་ལམ་གཞན་གྱིས་འདི་དག་འདུལ་བར་མི་འགྱུར་ཏེ་ཞེས་མཁྱེན་ནས་ཉོན་མོངས་པ་ཉིད་ཀྱིས་ཉོན་མོངས་པ་ཐམས་ཅད་ཉེ་བར་ཞི་བར་འགྱུར་ཞེས་དགོངས་ནས་སྒེག་པ་ལ་སོགས་པའི་ཆ་ལུགས་དང་ལྡན་པའི་དེ་བཞིན་གཤེགས་པ་ལྔ༌[^670]ཡེ་ཤེས་ལྔའི་ངོ་བོ་ཉིད་སྤྲོ་བར་མཛད་དེ། དེ་བཞིན་གཤེགས་པ་དེ་དག་གིས་དགའ་ལྡན་གྱི་ལྷའི་གནས་སུ་རིན་པོ་ཆེ་སྣ་བདུན་གྱི་རང་བཞིན་གྱི༌[^671]གཞལ་ཡས་ཁང་པ་ལ་བཞུགས་པའི་རྡོ་རྗེ་སེམས་དཔའ་ལ་གསོལ་བ་བཏབ་པར་གྱུར་པས་བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་རིག་མའི༌[^672]ཆུ་སྐྱེས་ཀྱི་ནང་དུ༌[^673]དཀྱིལ་འཁོར་སྤྲོས་ཏེ། དེ་བཞིན་གཤེགས་པ་རྣམས་ལ་རིག༌[^674]མའི་དབང་བསྐུར་ནས་ཕྱི་རོལ་དུ་སྤྲོས་ཏེ། དེ་ཁོ་ན་ཉིད་བསྟན་ཏོ་ཞེས་པ་དེ་ནི་དེ་བཞིན་གཤེགས་པའི་འབྲེལ་པའོ། །

[Block 950]
བཅོམ་ལྡན་འདས་དེ་ཉིད་ཀྱིས་འདོད་ཆགས་ཀྱི༌[^675]རིགས་ཅན་རྗེས་སུ་གཟུང་བར་བྱ་བའི་ཕྱིར། ལྷ་མོ་བཞི་སྤྲོས་ཏེ། དེ་རྣམས་ཀྱིས་ཡོངས་སུ་ཞུས་པས་དེ་ཁོ་ན་ཉིད་གསུངས་པ་དེ་ནི་ལྷ་མོའི་འབྲེལ་པའོ། །

[Block 951]
དབང་པོ་རྣམས་ལ་མངོན་པར་ཞེན་པའི་ཉོན་མོངས་པ་ལ་གནས་པའི་སེམས་ཅན་རྗེས་སུ་གཟུང་བར་བྱ་བའི་ཕྱིར་བྱང་ཆུབ་སེམས་དཔའི་ཚོགས༌[^676]སྤྲོས་ཏེ་དེ་ཁོ་ན་ཉིད་བསྟན་པ་ནི་བྱང་ཆུབ་སེམས་དཔའི་འབྲེལ་པའོ། །

[Block 952]
བརྒྱ་བྱིན་གྱིས་ཡོངས་སུ་ཞུས་པ་ལ་སོགས་པའི་བཤད་པའི་རྒྱུད་ལ་སོགས་པ་གང་གསུངས་པ་དེ་ནི་ལྷའི་འབྲེལ་པའོ། །

[Block 953]
མིའམ་ཅི་དང་ཀླུ་དང་དྲང་སྲོང་ལ་སོགས་པ་རྣམས་ལ་སྒྲོལ་མ་འབྱུང་བ་ལ་སོགས་པའི་རྒྱུད་བསྟན་པ་གང་ཡིན་པ་དེ་ནི་མི་འམ་ཅིའི་འབྲེལ་པའོ། །

[Block 954]
རབ་གསལ་ཟླ་བ་ལ་སོགས་པའི་རྒྱལ་པོ་རྣམས༌[^677]ཡུལ་དབུས་སུ་གྲོང་ཁྱེར་བཅོ་བརྒྱད་ལ་ཆོས་གསུངས་པ་དེ་ནི་མིའི་འབྲེལ་པའོ། །

[Block 955]
དེ་ལྟར་འབྲེལ་པ་དྲུག་པོ་རྒྱས་པ་དེ་མདོར་བསྡུས་པས་རྣམ་པ་གཉིས་སུ་འགྱུར་ཏེ། སྒྲ་དང་དོན་གྱི་འབྲེལ་པ་དང་། [^678]སྟོན་པ་དང་འཁོར་གྱི་འབྲེལ་པའོ། །

[Block 956]
ཇི་སྐད་དུ།

[Block 957 [VERSE]]
བསྟན་བཅོས་གང་ཟག་དབྱེ་བ་ཡིས། །
འབྲེལ་པ་རྣམ་པ་གཉིས་སུ་འདོད། །
བསྟན་བཅོས་སྒྲ་དང་དོན་འབྲེལ་པ། །
འཆད་དང༌[^679]ཉན་པའི་ཅིག་ཤོས་ཡིན། །

[Block 958 [VERSE]]
གཉིས་པའི་བྱེ་བྲག་དྲུག་ཡིན་ཏེ། །
གཅིག་ནས་གཅིག་ཏུ་བརྒྱུད༌[^680]རིམ་འོངས། །
དེ་བཞིན་གཤེགས་སོགས་དབྱེ་བ་ཡིས། །
བློ་ལྡན༌[^681]གྲགས་པ་རྣམས་ཀྱིས་གསུངས། །

[Block 959]
ཞེས་འབྱུང་ངོ་། །འདིར་ནི་དེ་བཞིན་གཤེགས་པའི་འབྲེལ་པ་གཅིག་པུ་ཡིན་ཏེ། དེ་བཞིན་གཤེགས་པ་ལྔས་དབུས་ཀྱི་གཙོ་བོ་ལ་གསོལ་བ་བཏབ་པས་སོ་ཞེས་འབྲེལ་པ་བསྟན་ཏོ། །

[Block 960 [HEADING]]
#### དགོས་པ། ^1-3-4-0

[Block 961]
དགོས་པ་ཞེས་བྱ་བ་ནི་ཐོས་པ༌[^682]དང་བསམ་པ༌[^683]དང་བསྒོམ་པའི༌[^684]རིམ་པས་བསྒྲུབ་བྱར་གྱུར་པའི་རྡོ་རྗེ་འཆང་ཆེན་པོའི་གནས་ཐོབ་པའོ། །

[Block 962 [HEADING]]
#### དགོས་པའི་དགོས་པ། ^1-3-5-0

[Block 963]
དེ་ཐོབ་ནས་ཁམས་གསུམ་པ་ཐམས་ཅད་ཀྱང་དེའི་གནས་སུ་དགོད་པ་ནི་བྱ་བ་བྱས་པའི་ཕྱིར་དགོས་པའི་དགོས༌[^685]པའོ། །

[Block 964]
གཞན་དག་ན་རེ་ཐོས་པ་ལ་སོགས་པའི་རིམ་གྱིས་རྟོགས་པ་ནི་དགོས་པའོ། །

[Block 965]
དེ་ལས་ཀྱང་ཐ་མལ་པའི་ལུས་བཟློག༌[^686]པས་འཇིག་རྟེན་ལས་འདས་པའི་ལྷའི་རྣམ་པ་བསྒྲུབ་པ་ནི་དགོས་པའི་དགོས་པ་ཡིན་ནོ་ཞེས་བརྗོད་པ་དེ་ནི་མི་རིགས་ཏེ། གང་གི་ཕྱིར་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱིས་རང་གི་དོན་སྒྲུབ་པ་ལ་འབད་པ༌[^687]མ་ཡིན་ཏེ། དེ་རྣམས་ཀྱིས༌[^688]ནི་གཞན་གྱི་དོན་གཙོ་བོ་ཡིན་གྱི་རང་གི་དོན་ནི་མ་ཡིན་ནོ། །

[Block 966]
ཇི་སྐད་དུ། འགྲོ་བ་མ་ལུས་རང་གཞན༌[^689]དོན་མཛད་པའི། །

[Block 967]
དེ་བཞིན་གཤེགས༌[^690]ཉིད་དེ་ཡི༌[^691]ཞར་ལ་འབྱུང་། །ཞེས་འབྱུང་ངོ་། །[^692]དེའི་ཕྱིར་གཞན་གྱི་དོན་ཁོ་ན་དགོས་པའི་གཙོ་བོ་ཡིན་གྱི། གཞན་དུ་ན་རང་གི་དོན་ནི༌[^693]དགོས་པ་ཉིད་དུ་མི་འགྱུར་རོ། །

[Block 968]
སྒྲུབ་པར་སྣང་བ་དང་། དོན་གྱི་བྱ་བར་སྣང་བའི༌[^694]ཤེས་པ༌[^695]གཉིས་བཞིན་ནོ། །

[Block 969]
དཔེར་ན་དང་པོ་མིག་ཕྱེ་བའི་དུས་སུ་སྲེག་པ་དང་འཚེད་པ་ལ་སོགས་པའི་དོན་གྱི་བྱ་བ་བྱེད་ནུས་པ་ཡང་མེ་ལ་སོགས་པ་ཙམ་དུ་སོ་སོར༌[^696]སྣང་བ་ཡིན་ཏེ། དོན་གྱི་བྱ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 970]
མེ་ལ་སོགས་པ་ཐོབ་ནས་སྲེག་པ་དང་འཚེད་པ་ལ་སོགས་པའི་བྱ་བ་དངོས་སུ་བྱེད་པའི་ཤེས་པ་ནི་དོན་གྱི་བྱ་བ༌[^697]སྣང་བར་བཤད་དོ། །

[Block 971]
དེ་ཉིད་དུ་བྱ་བ་བྱས་པའི་ཕྱིར་རོ། །

[Block 972]
གང་དོན་གྱི་བྱ་བ་བྱེད་པ་དེ་ཉིད་དམ་པའི་དོན་དུ་ཡོད་ཅེས་འབྱུང་ངོ་། །འདིར་ཡང་དགོས་པ་ནི་སྒྲུབ་པར་སྣང་བའོ། །

[Block 973]
དགོས་པའི་དགོས་པ་ནི་དོན་གྱི་བྱ་བར་སྣང་བ་ཡིན་ཞེས་རྒྱས་པས༌[^698]ཆོག་གོ། །

[Block 974 [HEADING]]
### གང་ཟག་ལྔ། ^1-4-0

[Block 975]
དགོས་པ་ལ་སོགས་པའི་སྒོ་ནས་གདུལ༌[^699]བྱ་འཇུག་པ་ཡིན་པས་དེ་དག་བསྟན་པར་བྱ་བའི་ཕྱིར་གང་ཟག་ལྔ་བརྟག་པར༌[^700]བྱ་སྟེ། དེ་ཡང་ཙནྡན་ལ་སོགས་པའི་གོང༌[^701]དུ་བཤད་པ་སྟེ། དེ་ལ་ཙནྡན་ཞེས་བྱ་བ་ནི་གཏི་མུག་འབའ་ཞིག་གི་རིགས་ཅན་ཐོས་པ་ཆུང་ཞིང་ང་རྒྱལ་གྱི་དབང་གིས་གཞན་རྣམས་སྐྱོ་བར་བྱེད་པ་དེ་ལས་གཞན་དང་རང་གི་དོན་སྒྲུབ་པར་མི་ནུས་ཏེ། བླུན་པོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 976]
ཨུཏྤ་ལ་ཞེས་བྱ་བ་ནི་ཐོས་པ་ལ་སོགས་པའི་རིམ་གྱིས་འཇུག་པ་ཡང་བརྗེད་ངས་པའི་ངང་ཚུལ་ཅན་ཡིན་ཏེ། དབང་པོ༌[^702]དམན་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 977]
དེའི་རང་གི་དོན༌[^703]སྐྱེ་བ་འདི་ལ་མེད་དེ་སྐྱེ་བ་གཞན་ལ་འབྱུང་བར་འགྱུར་བའི་ཕྱིར་རོ།[^704] །

[Block 978]
པདྨ་དཀར་པོ་ནི་ཐོས་པ་ལ་སོགས་པ༌[^705]རང་གི་སེམས་ལ་འཛིན་ཅིང་གཞན་ལ་སྟོན་པར་མི་ནུས་པས་རང་གི་དོན་ཙམ་ཡོད་དེ།[^706] དབང་པོ་བར་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 979]
པདྨ་ཞེས་བྱ་བ་ནི་གཞན་རྣམས་ལ་སྟོན་པར་བྱེད་ནུས་ཏེ། དབང་པོ་རྣོན་པོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 980]
རིན་པོ་ཆེ་ཞེས་བྱ་བ་ནི་རང་གི་དོན་དང་གཞན་གྱི་དོན་ཕུན་སུམ་ཚོགས་པ་དང་ལྡན་པ་ཚུལ་ཁྲིམས་ལ་སོགས་པའི་ཡོན་ཏན་དང་བཅས་པ་བྱང་ཆུབ་སེམས་དཔའི་རིགས་ཅན་དབང་པོ་རབ་ཀྱི་རབ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 981]
བཞི་པོ༌[^707]ནི་ཀུན་རྫོབ་ཀྱི་ཕྱོགས་ཀྱི་བཤད་པ་ལ་སྣོད་དུ་རུང་བ་དང་། གཅིག་ནི་དོན་དམ་པའི་མཆོག་གི༌[^708]བཤད་པའི་སྣོད་དུ་རུང་བའོ། །

[Block 982]
དེ་ཡང་ཤིན་ཏུ་རྒྱས་པར༌[^709]འོག་ནས་འཆད་པར་འགྱུར་རོ། །

[Block 983 [HEADING]]
### གང་ཟག་བཞི། ^1-5-0

[Block 984]
གཞན་དག༌[^710]ན་རེ་གང་ཟག་བཞི་ཡོད་དེ། མི་ཤེས་པ་དང་། ཐེ་ཚོམ་ཟ་བ་དང་། ཕྱིན་ཅི་ལོག་པའི་བློ་དང་། ངེས་པ་ཅན་གྱི་བློ་ཅན་ནོ། །

[Block 985 [HEADING]]
#### མི་ཤེས་པ། ^1-5-1-0
--- END BLOCKS ---
