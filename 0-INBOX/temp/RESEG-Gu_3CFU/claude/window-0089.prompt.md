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
[Block 3116]
སྨོན་པ་ཞེས་བྱ་བ་ནི་སྲུ་ནམ་ཞིག་ན་ཁོ་བོ་ཁྱོད་དང་ལྷན་ཅིག་དེ་དང་དེ་ལྟར་བྱེད་ཞིག་གུ་སྙམ་དུ་སྨོས༌[^2130]པའོ། །

[Block 3117]
གཤེ་བ་ཞེས་བྱ་བ་ནི་ཁྱོད་ལ་བོང་བུ་རྣམས་གང་དེ་ལྟར་བྱེད་པར་གྱུར་ཅིག་པའི་བློས་འདིར་མི་ལྟུང་ཞེས་གཤེ་བའོ། །

[Block 3118]
ཕྱིར་སྨྲ་བ་ཞེས་བྱ་བ་ནི་བུད་མེད་ཀྱིས་བརྗོད་པའི་བསྔགས་པ་ལ་སོགས་པ་ལ་དགེ་སློང་གིས་ཕྱིར་རྣམ་པ་དེ་རྣམས་ཀྱིས་སླར་ལན་འདེབས་པའོ། །

[Block 3119]
དོན་གཞན་ལ་བསམས་པས་ལྗོངས་ཀྱི་ངེས་པའི་ཚིག་གི་དབང་གིས་ན་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་འདི་ནི་མི་མཛེས་པ་ཞེས་བྱ་བ་བསམས་པར་གྱུར་པ་ལ་ལྟུང་བའི་བློས་འདིར་མི་ལྟུང་བའོ་ཞེས་བྱ་བ་དེའི་ཟློག༌[^2131]པའི་དོན་དུ་མདོ་འདི་དང་འོག་མའོ། །

[Block 3120]
ཅི་སྟེ་དོན་གཞན་ལ་བསམས་པ་ཞེས་བྱ་བ་ལྗོངས་ཀྱི་ཚིག་འདིའི་ངེས་པའི་ཚིག་གི་དབང་གིས༌[^2132]དོན་གཞན་གྱི་བསམ་པས༌[^2133]འཁྲིག་པ་སྨྲས་པ་གང་ཡིན་པ་དེ་ལ་ནི་ལྟུང་བ་མེད་དེ། གང་ཞིག་རུང་བ་ཙམ་གྱིས་གཞན་ལ་བསམ་པར་བྱེད་པ་ནི་མ་ཡིན་ཞེས་བྱ་བའོ། །

[Block 3121]
མིང་གི་ཆ་ཉིད་འདྲ་བ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི། ཆ་ཉིད་འདྲ་བ༌[^2134]གང་ཞིག་གི་དབང་གིས༌[^2135]འཁྲིག་པ་སྨྲས་པ་གང་ཡིན་པ་སྟེ་འདི་ལྟ་སྟེ་དཔེར་ན། རྒྱ་གར་སྐད་དུ་ནས་ལ་ནི་ཡ་བ་ཞེས་བྱ་བ། འཁྲིག་པ་ལ་ནི་ཡ་བྷ་ཞེས་བྱ་བ་དེ་ལ་ནས་ཀྱི་མིང་ཡ་བ་ཞེས་བརྗོད་པའི་བསམ་པས་དྲག་ཏུ་བརྗོད་པའི་དབང་གིས་བ་ཞེས་བྱ་བའི་གནས་སུ་བྷ་ཞེས་བརྗོད་པ་ལ་ལྟུང་བ་མེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 3122]
དགེ་འདུན་ལྷག་མ་གསུམ་པའི་རྣམ་པར་འབྱེད་པའོ།། །།

[Block 3123]
མཛེས་པ་ཡིན་ནོ། །

[Block 3124]
སྡིག་ཅན་ཡིན་ནོ། །

[Block 3125]
རྨའི་སྒོ་མཛེས་པ་འམ་སྡིག་ཅན་ཡིན༌[^2136]ནོ། །

[Block 3126]
བགོ་བཤའ་གྱིས་ཤིག་ཁོ་བོ་ལ་བགོ་བཤའ་གྱིས་ཤིག །ཁོ་བོ་དང་ལྷན་ཅིག་ཉོལ་ཅིག །ཕྲད་པར་གྱིས་ཤིག་ཅེས་སྨྲས་ན་སྦོམ་པོའོ་ཞེས་བྱ་བ་ནི་འདིར་ཁྱོད་ནི་སྡིག་པ་ཅན་ཞེས༌[^2137]བྱ་བ་ལ་སོགས་པ་རྣམས་ཀྱི་སྒྲ་བརྗོད་པ་དང་སོ་སོར་མངོན་པར་འབྲེལ་ལོ། །

[Block 3127]
གནས་ངན་ལེན་དང་བཅས་པའི་སེམས་ཀྱིས་གནས་ངན་ལེན་གྱི་ཚིག་བརྗོད་པ་ལ་སྦོམ་པོའོ། །

[Block 3128]
རྣམ་པ་གང་ཡིན༌[^2138]སྦྱར་བར་གྱུར་པ་དེའི་རྣམ་པའི་གནས་ངན་ལེན་གྱིས་ཐ་ན་རྒོད་བག་ཙམ་གྱིས་སྨྲས་ན་ཡང་ཐམས་ཅད་དུ་སྦོམ་པོར་རིག་པར་བྱའོ།[^2139] །ཀུན་དུ་ཆགས་པར་གྱུར་པས་ནི་མ་ཡིན་ཏེ་དེ༌[^2140]ཡང་མཐུ་ཡོད་པ་ཅན་ལའོ། །

[Block 3129]
དགེ་འདུན་ལྷག་མ་གསུམ་པའི་ཞུ་བའི་སྐབས་སོ།། །།

[Block 3130]
དེ་བཞིན་དུ་རྫུ་འཕྲུལ་གྱི་རྣམ་པར་འཕྲུལ་པའི་ཆོས་ཅན་མོ་ལ་སྨྲ་ནའོ་ཞེས་བྱ་བ་ལ། དེ་བཞིན་དུ་ཞེས་བྱ་བའི་སྒྲ་ནི་སྦོམ་པོའོ་ཞེས་སྔར་བསྟན་པའི་རྗེས་བསྙགས༌[^2141]པའི་ཕྱིར་རོ། །

[Block 3131]
རྫུ་འཕྲུལ་གྱི་རྣམ་པར་འཕྲུལ་བའི་ཆོས་གང་ལ་ཡོད་པ་དེ་ནི་རྫུ་འཕྲུལ་གྱི་རྣམ་པར་འཕྲུལ་པའི་ཆོས་ཅན་ནོ། །

[Block 3132]
དེའི་གནས་ངན་ལེན་ཅན་སྨྲས་ན་ནི་སྦོམ་པོའོ། །

[Block 3133]
འདིར་སེམས་ནི་འཇིགས་པར་འགྱུར་ཏེ། མངོན་པར་ཞེན་པ་དམན་པས་རབ་ཏུ་འགྲོ་བ་མི་སྲིད་པའི་ཕྱིར་དང་། མཐུ་མཐོང་བའི་ཕྱིར་རོ། །

[Block 3134]
དེ་བས་ན་འདིར་ན་སྨད་པའོ། །

[Block 3135]
དེ་བཞིན་དུ་ཞེས་བྱ་བ་ནི་འདིས་ཐམས་ཅད་ཀྱི་དབང་དུ་བྱ་བར་རིག་པར་བྱའོ། །

[Block 3136]
སྲུ་ཁོ་བོ་ལ་ནས་བྱིན་ཅིག །སྲུ་ཁྱོད་ལ་ཅི་མཐོང་བ་དེ་བྱིན་ཅིག །སྲུ་ཁྱོད་ཀྱི་མདུན་ན་མོ་གང་ཡིན་པ་དེ་བྱིན་ཅིག །སྲུ་ཁྱོད་ཀྱི་ཡིད་དུ་འོང་བ་གང་ཡིན་པ་དེ་བྱིན་ཅིག །ཁྱོད་ལ་ཅི་དགའ་བ་བྱིན་ཅིག་ཅེས་བདག་ལ་སྨྲས་པ་ཁྱོད་ཅི་ལ་དགའ་ཞེས་ཟེར་བ་ལ་སྲུ་ཁྱོད་ལ་ཁོ་བོ་དགའོ༌[^2142]ཞེས་བྱ་བ་དང་། སྲུ་ཁོ་བོ་ལ་ཆུ་དང་བཅའ་བ་དང་ཐུག་པ་དང་བཟའ་བ་བྱིན་ཅིག །ཁྱོད་ཉིད་དེ་དག་ཡིན་ནོ་ཞེས་སྨྲས་པ་དག་ལའོ་ཞེས་བྱ་བ་ནི་ཁྱོད་ཅི་ལ་དགའ་བ་སྦྱིན་པར༌[^2143]བྱ་ཞེས་ཟེར་བ་ལ་བདག་ནི་ཁྱོད་ཀྱི༌[^2144]སྦྱིན་བདག་གིས་སྨྲས་པ་དེ་བས་ན་ཁྱོད་ལ་དྲི་བར་བྱ་སྟེ། ཁྱོད་ཅི་ལ་དགའ་ཞེས་ཟེར་བ་ལ་བུད་མེད་དེ་ལ་འདི་སྐད་ཅེས་སྲུ་ཁྱོད་ལ་ཁོ་བོ་དགའ་འོ༌[^2145]ཞེས་ཟེར་བའོ། །

[Block 3137]
བདག་ལ་བྱིན་ཅིག་ཅེས་བྱ་བ་ནི་བཟའ་བ་ལ་སོགས་པ་གསུམ་པོ་འདི་ལ་ཡང་སོ་སོར་རྗེས་སུ་འབྲེལ་ལོ། །

[Block 3138]
ཁྱོད་ཉིད་དེ་དག་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཆུ་ལ་སོགས་པ་བཞི་པོ་ལ་ཡང་ཚིག་ལྷག་མ་འདི་རྣམས་སོ། །

[Block 3139]
སྲུ་ཁོ་བོ་ལ་ཆུ་བྱིན་ཅིག །སྲུ་ཁྱོད་ཉིད་ནི་ཆུ་ཡིན་ཏེ་ཞེས་བྱ་བ་ནས་ཇི་སྲིད་དུ་སྲིང་མོ་བདག་ལ་བཟའ་བ་བྱིན་ཅིག་ཅེས་བྱ་བའི་བར་དུ་སྨྲས་པ་དག་ལ་འདི་ལྟ་བུའི་ངོ་བོ་བཞི་པོ་སྨྲ་བ་འདི་རྣམས་ལ་སྦོམ་པོའི་ལྟུང་བའོ། །

[Block 3140]
ཁྱོད་ལ་བོང་བུ་དག་དེ་བྱེད་པར་གྱུར་ཅིག །སྲུ་སྐྱེས་བུ་འཕྱོན་པ་དག༌[^2146]ལ་བསོད་སྙོམས་སྤྱོད་དམ་ཞེ༌[^2147]ན་ཡང་ངོ་ཞེས་བྱ་བ་འདི་ལ། སྤྱོད་དམ་ཞེས་བྱ་བ་འདི་དང་འབྲེལ་ཏོ། །

[Block 3141]
བསོད་སྙོམས་ཀྱི་སྤྱོད་པ་ཁྱོད་ཀྱིས་སྤྱོད་ཅེས་ཟེར་ཞིང་གྲོང་བའི་རོ་ལ་ཉེ་བར་བརྟེན་པ་རྣམས་ལ་ཁྱོད་ནི་སྤྱོད་པ་འདིས་སྤྱོད་པར་བྱེད་དེ་གང་ལ་བསོད་སྙོམས་ཤེས་པའི་དོན་ཏོ། །

[Block 3142]
དེར་མགལ་དུམ་ཆུག་ཅིག་ཅེས་ན༌[^2148]ཡང་ངོ་། །རང་བཞིན་གྱིས༌[^2149]གནས་ངན་ལེན་བརྗོད་པས་གནས་ངན་ལེན་སྨྲས་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་རྒྱའི་དོན་ཅན་གྱི་སྒྲ་རྣམས་ཀྱིས་ཀྱང་སྨྲས་པ་ལ་སྦོམ་པོ་འདིའོ། །

[Block 3143]
ཀུན་ནས་ཆགས་པ་མེད་པའི་ཕྱིར་འོ་ན་ཅིའི་ཕྱིར་ལྟུང་བ་མེད་པ་ཉིད་དུ་མི་འགྱུར་ཏེ་རྒོད་པར་གྱུར་པའི་གནས་ངན་ལེན་ཡོད་པའི་ཕྱིར་རོ། །

[Block 3144]
དགེ་འདུན་གྱི་ལྷག་མ་གསུམ་པོ་འཁྲིག་པ་དང་ལྡན་པ་སྨྲ་བའི་འདུལ་བྱེད་རྣམས་སོ།། །།

[Block 3145]
གང་དུ་བསྔགས་པ་དགེ་འདུན་གྱི་ལྷག་མར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་བདག་ཉིད་འཁྲིག་པ་ཀུན་ཏུ་སྤྱོད་པ་བསྔགས་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བུད་མེད་དོན་ཀུན་ཤེས་པར་བྱ་བའི་མཐུ་ཡོད་པ་ལ་དེས་ཞེས་བྱ་བ་འདི་འདིར་སྔར་བཤད་པ་རྗེས་སུ་དྲན་པར་བྱའོ། །

[Block 3146]
ལོག་པར་བསྒྲུབས་པ༌[^2150]ལ་ལེགས་པ་ཉིད་ཀྱིས་སྤྱོད་པ་ནི་བསྔགས་པའོ། །

[Block 3147]
འོན་ཏེ་བསྒྲུབ་པ་འདི་མཆོག་ཅེས་བྱ་བ་ལ་སོགས་པའི་རྣམ་པ་དང་ཁྱད་པར་དུ་འཕགས་པས་ལོག་པའི་བསྒྲུབ་པ་དོར་བས་ཁ་ན་མ་ཐོ་བ་དེ་ཉིད་དུ་རྣམ་པར་གཞག་པ་ཡིན་ནོ། །

[Block 3148]
བདག་ཉིད་དང་འཁྲིག་པ་ཀུན་དུ་སྤྱོད་པ་སྨྲ་བ་ལ་གལ་ཏེ་འགྲོ་བ་བརྗོད་པར་སྦྱོར་ན་སྨྲ་བ་ལ་དགེ་འདུན་གྱི་ལྷག་མ་ཉིད་དོ། །

[Block 3149]
སྨྲ་བའི་བདག་ཉིད་ཅན་ལ་ཡང་སྐད་ཅིག་མ་གཅིག་ཏུ་གྱུར་པ་ཉིད་ཀྱི་ཕྱིར་དོན་གཅིག་གོ་བར་བྱེད་པའི་སྔོན་གྱི་རྣམ་པ་མེད་པ་ལ་ཐ་སྙད་འདིའོ། །

[Block 3150]
དེ་བས་ན་གཞན་གྱིས་འགྲོ་བ་བརྗོད་པའི་ཕྱིར་འཁྲིག་པའི་ཚིག་ནི་དགེ་འདུན་གྱི༌[^2151]ལྷག་མ་ལ་ཡན་ལག་ཏུ་རྟོགས་པར་བྱའོ། །

[Block 3151]
དེས་བསྔགས་པ་ལ་རྗེས་སུ་ཡི་རང་བའི་དོན་གྱི་ཚིག་ནི་དེ་དང་འདྲའོ་ཞེས་བྱ་བ་ནི་འདིར་བུད་མེད་གང་ཞིག་འགལ་ཟླ་ཉིད་ཀྱིས་གནས་པ་དེ་དང་ལྷན་ཅིག་དགེ་སློང་དེ་ལ་བསྙེན་བཀུར་བྱས་པ་འདི་ནི་འཕགས་པ་ལ་བསྙེན་བཀུར་བྱས་པ་རྣམས་ཀྱི་མཆོག་སྟེ། གང་གི་ཕྱིར་ཁྱེད་ལྟ་བུའི་དགེ་སློང་ཚུལ་ཁྲིམས་དང་ལྡན་པ་ལ་ཞེས་བྱ་བ་ལ་སོགས་པས་བསྔགས་པ་ལ། གང་ཞིག་འདི་ནི་དེ་ལྟར༌[^2152]ཡིན་ནོ་ཞེས་བྱ་བ་རྗེས་སུ་ཡི་རང་བའི་དོན་དུ་བརྗོད་པ་ནི་བསྔགས་པ་བཞིན་དུ་བལྟ་བར་བྱའོ། །

[Block 3152]
འདིར་དངོས་གཞི་ཁོ་ནའི་ཁ་ན་མ་ཐོ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3153]
དེ་ཉིད་ཕྱིར་བཟླས་ནའོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་འདི་བསྙེན་བཀུར་བྱས་པ་རྣམས་ཀྱི་མཆོག་ཅེས་བྱ་བ་ལ་སོགས་པ་དེས་བཟླས་ན་དགེ་སློང་གི་ཕྱིར་ཟློ་བར་བྱེད་དེ། དེས་བསྔགས་པ་ཉིད་ནི་ཡོད་པ་མ་ཡིན་ཏེ་དེ་ལས་བཟླས་པར་བྱས་པའོ། །

[Block 3154]
དེ་ལྟ་དེ་ལྟར་ཕྱིས་རྗེས་སུ་སྨྲ་བ་ཞེས་བྱ་བ་གང་གསུངས་པ་དེ་འདིས་བསྡུས་པ་ཡིན་ནོ། །

[Block 3155]
དེ་དང་འཁྲིག་པ་དང་ཉེ་བར་མ་སྦྱར་ན་སྦྱོར་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་གང་དུ་ཉེ་བར་མ་སྦྱར་བ་ལ་དེས་སྦྱོར་བ་ཉིད་དོ། །
--- END BLOCKS ---
