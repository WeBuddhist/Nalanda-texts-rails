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
[Block 141]
དེ་ལ་རྣམ་པར་ཤེས་པའི་དུས་ནི་འཆད་པ་དང་ཉན་པ་རྣམས་ཀྱི༌[^220]ཡིད་ལ་དུས་གསུམ་ལྟ་བུར་སྣང་ཞིང་ཡུན་རིང་ཐུང་དང་ཉིན་མཚན་དུ་སྣང་བ་དེའི་དུས་ཏེ། ཇི་ལྟར་རྨི་ལམ་ན་ཡུན་རིང་དུ་ལོན་ཀྱང་སད་ན་དེ་ལྟ་མ་ཡིན་པ་བཞིན་ནོ། །

[Block 142]
ཡང་དུས་གཅིག་ཅེས་སྨོས་པ་ཡང་སྐད་ཅིག་མའི་དུས་དང་། དུས་བཞི་དང་དྲུག་དང་བརྒྱད་ལ་མི་བྱའི། ནམ་ཐུགས་རྗེས་ཕན་འདོགས་པ་དང་། དབང་པོ་སྨིན་པ་དུས་གཅིག་ཏུ་གྱུར་པ་དེ་ལ་དུས་ཤེས་པའོ།[^221] །

[Block 143 [HEADING]]
#### སྟོན་པ་ཕུན་སུམ་ཚོགས་པ། ^4-1-3-0

[Block 144]
བཅོམ་ལྡན་འདས་ཞེས་སྨོས་པ་ནི་སྟོན་པ་ཕུན་སུམ་ཚོགས་པ་སྟེ། དབང༌[^222]ཕུན་སུམ་ཚོགས་པ་ལ་སོགས་པའི་ཡོན་ཏན་དྲུག་དང་ལྡན་པ་ནི་བཅོམ་ལྡན་འདས་ཞེས་བྱའོ། །

[Block 145 [HEADING]]
#### གནས་ཕུན་སུམ་ཚོགས་པ། ^4-1-4-0

[Block 146]
རྒྱལ་པོའི་ཁབ་བྱ་རྒོད་ཕུང་པོའི་རི་ལ་བཞུགས་ཞེས་པ་ནི་གནས་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏེ། དེར་གནས་པ་དང་བཞུགས་པ་དང་བཞེངས༌[^223]ཞེས་པའི་དོན་ཏེ། འཕགས་པ་དང་ལྷ་དང་ཚངས་པའི་བཞུགས་ས༌[^224]ལས་ཁྱད་པར་དུ་བསྟན་པའི་ཕྱིར། བཅོམ་ལྡན་འདས་དེར་བཞུགས་ཞེས་སྨོས་སོ། །

[Block 147]
རྒྱལ་པོའི་ཁབ་ཅེས་སྨོས་པ་ནི་སྔོན་རྒྱལ་པོ་གསལ་རྒྱལ་གྱི་ཕོ་བྲང་འབངས་མང་པོ་དང་འདབ་ཆགས་སུ་འདུག་པ་ལ་རྟག་ཏུ་མེ་ཤོར་བས་བསྙེངས་ཏེ།

[Block 148]
རྒྱལ་ཁྲིམས་སུ་བཅས་པས་ད༌[^225]སླན་ཆད་སུའི་ཁྱིམ་ན༌[^226]མེ་ཤོར་བ་དེ་དུར་ཁྲོད༌[^227]གདོན་གྱི་གནས་སུ་གཅིག་པུར་སྤྱུགས༌[^228]པར་བྱས་པ་ལས། དང་པོ་རྒྱལ་པོའི་ཁབ་མེ་ཤོར་བས་རྒྱལ་པོ་ཉིད་དུར་ཁྲོད་དེར་འཕོས་ཏེ། ཕོ་བྲང་བཏབ་ནས་འབངས་དེར་འཕོས་པ་རྣམས་ཀྱང་འདྲེ་གདོན་གྱིས༌[^229]མི་གཙེ་བའི༌[^230]ཕྱིར་སྒོ་སྒོ་ལ་རྒྱལ་པོའི་ཁབ་ཅེས་བྲིས་པས། དེའི་ཕྱིར་ཡུལ་འཁོར་དེ་རྒྱལ་པོའི་ཁབ་ཏུ་ཆགས་སོ། །

[Block 149]
རྒྱལ་པོའི་ཁབ་དང་བྱ་རྒོད་ཕུང་པོའི་རི་གཉི་ག་སྨོས་པ་ནི་ཁྱིམ་ན་གནས་པ་དང་རབ་ཏུ་བྱུང་བ་གཉི་ག་ལ་ཕན་གདགས་པའི་ཕྱིར་གཉི་ག་སྨོས་སོ། །

[Block 150]
རྒྱལ་པོའི་ཁབ་དེ་རིན་པོ་ཆེ་ཐམས་ཅད་ཀྱི་འབྱུང་ཁུངས༌[^231]གནས་གཞན་ཐམས་ཅད་ལས་འཕགས་པ་བཞིན་དམ་པའི་ཆོས་འདི་དེར་བཤད་པ་ཡང་མདོ་སྡེ་གཞན་ཐམས་ཅད་ལས༌[^232]ཁྱད་པར་དུ་བསྟན་པ་དང་། བྱ་རྒོད་ཕུང་པོའི་རི་དེ་ཡང་རི་གཞན་ཐམས་ཅད་ལས་འཕགས་པ་བཞིན་ཐེག་པ་གཅིག་པའི་ཐེག་པ་འདི་ཡང་ཐེག་པ་གཉིས་ལས་ཁྱད་པར་དུ་འཕགས་པའི་ཕྱིར་གནས་དེར་བཤད་དོ། །

[Block 151 [HEADING]]
#### འཁོར་ཕུན་སུམ་ཚོགས་པ། ^4-1-5-0

[Block 152]
མདོ་ལས་དགེ་སློང་གི་དགེ་འདུན་ཆེན་པོ་དགེ་སློང་སྟོང་ཕྲག་བཅུ་གཉིས་ཞེས་འབྱུང་བ་འདི་ནི་འཁོར་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 153]
འཁོར་ཕུན་སུམ་ཚོགས་པ་དེ༌[^233]ཡང་རྣམ་པ་ལྔ་སྟེ། དེའི་གཏན་ཚིགས་བསྟན་པ་དང་། བཀྲི་བ༌[^234]དང་ངེས་པའི་དོན་རྣམས་གླེང་བ་དང་། གྲངས་མང་ཉུང་གཏན་ལ་དབབ་པ་དང་། འཁོར་རྣམས་ཀྱི་རིམ་པ་བསྟན་པ་དང་། འགྲེལ་པའི་དོན་བསྟན་པའོ། །

[Block 154 [HEADING]]
##### གཏན་ཚིགས་བསྟན་པ། ^4-1-5-1-0

[Block 155]
གཏན་ཚིགས་བསྟན་པ་ལ་ཡང་རིམ་པ་ལྔ་སྟེ། དད་པ་དང་ཡིད་ཆེས་པའི་གཏན་ཚིགས་སུ་དགའ་བོ་འདིས་རང་བཟོར་སྨྲས་པ་ནི་མ་ཡིན་པ་དང་། གཞན་ལས་བརྒྱུད་དེ་སྨྲས་པ་མ་ཡིན་པ་དང་། གཞན་གྱི་ཚིག་ཟློས་པ་མ་ཡིན་པར་བསྟན་པའི་ཕྱིར་ལྷན་ཅིག་ཏུ་ཐོས་པ་ཡང་མང་དུ་ཡོད་པར་བསྟན་པས་གཞན་དག་ཡིད་ཆེས་པར་འགྱུར་བའི་གཏན་ཚིགས་དང་གཉིས་སུ་ཕྱེ་བ༌[^235]ཕུན་སུམ་ཚོགས་པ་བསྟན་པས་གཞན་ཡིད་ཆེས་པར་འགྱུར་བའི་གཏན་ཚིགས་སྟེ། ལྷའི་རྒྱལ་པོ་བརྒྱ་བྱིན་དང་། ཚངས་པའི་འཁོར་གྱིས་བསྐོར་བ་སྨོས་པ་དང་། ཡང་ཤཱ་རིའི་བུ་དང་འཇམ་དཔལ་གཞོན་ནུར་གྱུར་པ་དང་། བྱམས་པ་དང་བྱང་ཆུབ་སེམས་དཔའ་བཀྲི་བ་དང་ངེས་པའི༌[^236]དོན་ལན་གཉིས་ལན་གསུམ་དུ་གསོལ་ཏེ། རྒྱུ་དང་འབྲས་བུ་དང་བསླབ་པའི་མདོ་བསྟན་པས་འཁོར་རྣམས་ལ་ཕན་པ་དང་བདེ་བས་ཡིད་ཆེས་པར་འགྱུར་བ་དང་། ཡང་སོ་སོའི་དབང་པོ་ལས་ཐེག་པ་གཅིག་པའི་གཞུང་འདི་ལན་གསུམ་བཟླས་ཏེ་བཤད་པ༌[^237]ཐེག་པ་ཆེན་པོར་སེམས་སྐྱེ་བ་དང་མི་སྐྱེ་བའི་ཆོས་ལ་བཟོད་པ་ཐོབ་པ་ལ་སོགས་པ་དབང་པོ་གསུམ་པོ་རྣམས་ལ་ཆོས་འདི་བསྟན་པ་དང་། ཡང་སྔོན་གྱི་དུས་ན་བྱུང་བ་བསྟན་པས་ད་ལྟར་གྱི་སེམས་ཅན་རྣམས་དད་པ་བསྐྱེད་པ༌[^238]སྟེ། དེ་ལྟ་བུའི་འཕགས་པ་སྟེ་དམ་པ་རྣམས་དང་ཐབས་ཅིག་པ་ལ༌[^239]ཞེས་དད་པ་སྐྱེ་བར་འགྱུར་རོ། །

[Block 156 [HEADING]]
##### བཀྲི་བ་དང་ངེས་པའི་དོན་གླེང་བ། ^4-1-5-2-0

[Block 157]
དེ་ལ་བཀྲི་བ༌[^240]དང་ངེས་པའི་དོན་བསྟན་པ་ནི་ཇི་ལྟར་བཅོམ་ལྡན་འདས་སྤྲུལ་པ་བཞུགས་པའི་ཞིང༌[^241]ཉན་ཐོས་རྣམས་ལ་ངེས་པའི་དོན་སྟོན། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ལ་བཀྲི་བའི་དོན་སྟོན། རྫོགས་ལོངས༌[^242]སྤྱོད་པའི་སྐུ་ནི་བྱང་ཆུབ་སེམས་དཔའ༌[^243]ལ་ནི་ངེས་པའི་དོན་སྟོན། ཉན་ཐོས་པ༌[^244]རྣམས་ལ་ནི་བཀྲི་བའི༌[^245]དོན་སྟོན། འདི་ནི༌[^246]བཀྲི་བ་དང་ངེས་པའི་དོན་གཉི་ག་སྟོན་པའི་ས་བསྟན་ཏོ། །

[Block 158 [HEADING]]
##### གྲངས་མང་ཉུང་གཏན་ལ་དབབ་པ། ^4-1-5-3-0

[Block 159]
དེ་ལ་གྲངས་མང་ཉུང་བསྟན་པ་ཡང་སྔར་འཁོར་བཅོ་ལྔ་སྟེ། ཡོན་ཏན་ཆེ་ལ་མིང་ཡོད་པ་རྣམས་དང་། ཡོན་ཏན་ཆེ་ལ་མིང་མེད་པ་རྣམས་དང་། དགེ་འདུན་མ་ཡོན་ཏན་ཆེ་བ་རྣམས་དང་། དགེ་འདུན་མ་ཉེ་བའི་འཁོར་རྣམས་དང་། ཡོན་ཏན་འཕགས་པ་བསམ་གྱིས་མི་ཁྱབ་པ་རྣམས་དང་། བརྒྱ་བྱིན་ལྷའི་དབང་པོ་རྣམས་དང་། རྒྱལ་ཆེན་བཞིའི་ལྷ་རྣམས་དང་། དབང་ཕྱུག་ལྷའི་བུ་རྣམས་དང་། གཟུགས་ཀྱི་ཁམས་ཀྱི་ལྷའི་བུ་རྣམས་དང་། ཀླུའི་རྒྱལ་པོ་རྣམས་དང་། མིའམ་ཅི༌[^247]རྣམས་དང་། དྲི་ཟ༌[^248]རྣམས་དང་། ལྷ་མ་ཡིན༌[^249]རྣམས་དང་། ནམ་མཁའ་ལྡིང༌[^250]རྣམས་དང་། མིའི་རྒྱལ་པོ༌[^251]རྣམས་སོ། །

[Block 160]
ཡང་འཁོར་རྣམ་པ་དྲུག་སྟེ། བཅོམ་ལྡན་འདས་རིན་ཆེན་མང་གི་འཁོར་དང་། སྐུས་སྤྲུལ་པའི་འཁོར་དང་། ཀླུའི་ཕོ་བྲང་ནས་ལྷགས་པ༌[^252]དང་། སའི༌[^253]རུམ་ནས་འཐོན་པའི་འཁོར་དང་། བྱང་ཆུབ་སེམས་དཔའ་སང་སང་པོའི་དབྱངས་དང་། ཀུན་ཏུ་བཟང་པོའི་འཁོར་རོ། །

[Block 161]
འཁོར་དེ་དག་ཀྱང་ཆོས་ཉན་པ་དང་། ཆོས་རྟོགས་པ༌[^254]དང་། ཆོས་སྤྱོད་པ་དང་། ཆོས་འཛིན་པ་དང་། ཆོས་འཆད་པ་དང་། ཆོས་རིག་པའི་བྱེ་བྲག་གིས༌[^255]ཐ་དད་པ་ཤ་སྟག༌[^256]གོ། །

[Block 162]
འཁོར་འདིར༌[^257]རང་སངས་རྒྱས་ཀྱི་འཁོར་མ་སྨོས་པ་ནི་རང་སངས་རྒྱས་སངས་རྒྱས་འཇིག་རྟེན་ན་མི་བཞུགས་པའི་ཚེ་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 163]
གཟུགས་མེད་པའི་ཁམས་ཀྱི་ལྷ་རྣམས་ཀྱང་དེ་བཞིན་གཤེགས་པའི་འོད་ཀྱིས༌[^258]རེག་པ་རྣམས་ཆོས་ཉན་ཅིང་འཁོར་དུ་འདུ་བ་ཡིན་ན། ཁམས་དེ་དབང་པོ་མ་སྨིན་པས་འོད་ཀྱིས༌[^259]སྣང་བར་མི་མཛད་དེ། དེ་ནས་འདིར་མ་སྨོས་སོ། །

[Block 164]
སེམས་ཅན་དམྱལ་བ་འདིར་མ་སྨོས་པ་ནི་སྐལ་བ་དང་མི་ལྡན་པའི་ཕྱིར་འདིར་མ་སྨོས་སོ། །

[Block 165]
དེ་བཞིན་གཤེགས་པའི་བྱིན་གྱི་རླབས་ཀྱིས༌[^260]གཟུངས་ཀྱི་སྒོ་འཆད་པའི་ཚེ་ངན་སོང་ཞི་བར་མཛད་པའི་ཕྱིར་དེ་དག་ཏུ་སྨོས་པ་ཡང་ཡོད་དོ། །

[Block 166]
འཁོར་གོང་དུ་མ་སྨོས་པ་རྣམས་ཀྱང་འོག་ནས་བསྟན་པ་ཡིན་ནོ། །

[Block 167 [HEADING]]
##### འཁོར་རྣམས་ཀྱི་རིམ་པ་བསྟན་པ། ^4-1-5-4-0

[Block 168]
འཁོར་དེ་དག་གི་རིམ་པ་ནི་སྤྱིར་རྣམ་པ་བཞི་སྟེ། ཉན་ཐོས་པའི་འཁོར་དང་། བྱང་ཆུབ་སེམས་དཔའི་འཁོར་དང༌[^261]རྒྱལ་པོ་དང་རྒྱལ་པོ་རྣམས་ཀྱི་འཁོར་རོ། །

[Block 169]
དེ་ཡང་ཕྱི་ནང་དུ་དབྱེ་ན་ཉན་ཐོས་དང་བྱང་ཆུབ་སེམས་དཔའི་འཁོར་ནི་ནང་གི་འཁོར་རོ། །

[Block 170]
ལྷ་མ་སྲིན་འཁོར་བརྒྱད་པོ་ནི་ཕྱིའི་འཁོར་རོ། །

[Block 171]
བྱང་ཆུབ་སེམས་དཔའི༌[^262]ཉན་ཐོས་པའི་འཁོར་སྔར་སྨོས་པ་ནི་རྣམ་པ་བཞིའི་ཕྱིར་ཏེ། ཉན་ཐོས་པ་རབ་ཏུ་བྱུང་བས་དེ་བཞིན་གཤེགས་པའི་ཆ་ལུགས་དང་མཐུན་པའི་ཕྱིར་ཉན་ཐོས་པ་སྔར་སྨོས་པ་དང་། ཉན་ཐོས་པ་རྟག་ཏུ་ཞབས༌[^263]འབྲིང་ན་མཆིས་ཤིང་གནས་ཏེ། རིང་དུ་མ་གྱུར་པའི་ཕྱིར༌[^264]སྔར་སྨོས་པ་དང་། རབ་ཏུ་བྱུང་བ་ཚུལ་ཁྲིམས་བསྲུང་བའི་སྒོ་ནས་སྔར་སྨོས་པ་དང་། ཁྱིམ་པས་རབ་ཏུ་བྱུང་བ་ལ་གུས་པ་བསྟན་པའི་ཕྱིར་སྔར་སྨོས་སོ། །

[Block 172 [HEADING]]
##### འགྲེལ་པའི་དོན་བསྟན་པ། ^4-1-5-5-0

[Block 173]
ཡང་འཁོར་ཕུན་སུམ་ཚོགས་པ་ལ་རྣམ་པ་བཞི་སྟེ། གྲངས་ཕུན་སུམ་ཚོགས་པ་དང་། སྒྲུབ་པ་ཕུན་སུམ་ཚོགས་པ་དང་། ཡོན་ཏན་ཕུན་སུམ་ཚོགས་པ་དང་། སྤྱོད་ལམ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 174]
གྲངས་ཕུན་སུམ་ཚོགས་པ་ནི་འཁོར་གྲངས་མེད་པ་ཞེས་སྨོས་པའོ། །

[Block 175]
སྒྲུབ་པ་ཕུན་སུམ་ཚོགས་པ་ནི་ཉན་ཐོས་པ་རྣམས་ཐེག་པ་ཆུང་ངུ་སྒྲུབ་པ་དང་། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ནི་ཐེག་པ་ཆེན་པོ་སྒྲུབ་ཅིང་། གཞན་གྱི་དོན་བྱེད་པའོ། །

[Block 176]
ཡོན་ཏན་ཕུན་སུམ་ཚོགས་པ་ནི་ཉན་ཐོས་པ༌[^265]རྣམས་ཚིག་གི་དོན་རྣམ་པ་བཅུ་དྲུག་ཏུ་བསྟན་པ་དང་། བྱང་ཆུབ་སེམས་དཔའ༌[^266]རྣམས་ཚིག་གི༌[^267]དོན་རྣམ་པ་བཅུ་གསུམ་གྱིས༌[^268]སྟོན་པའོ། །

[Block 177]
སྤྱོད་ལམ་ཕུན་སུམ་ཚོགས་པ་ནི་བཅོམ་ལྡན་འདས་འཁོར་རྣམས་ཀྱིས༌[^269]བསྐོར་ཏེ༌[^270]གུས་པ་རི་མོ་བྱེད་པའི་ཚུལ་གྱིས༌[^271]མཛེས་པར་གནས་པ་རྣམས་སོ། །

[Block 178]
དེ་ལ་དགེ་སློང་ཞེས་བྱ་བའི་དོན་རྣམ་པ་གསུམ་སྟེ། བདུད་དང་མུ་སྟེགས་འཇིག་པར་བྱེད་པ་དང་། སློང་བ་དང་ཚུལ་ཁྲིམས་བསྲུང་བས་དགེ་འདུན་གྱི་གྲངས་སུ་འགྲོ་བ་དང་། འཚོ་བ་གཙང་མས༌[^272]འཚོ་ཞིང་སྒོ་གསུམ་དག་པར་གནས་པའོ། །

[Block 179]
དགེ་འདུན་གྱི༌[^273]དགེ་སློང་བཞི་ཡན་ཆད་དེ་མང་བ་མཐུན་པ་རིགས་དང་གཞུང་མ༌[^274]འདྲེས་པའི་དོན་ཏོ། །

[Block 180]
ཆེན་པོ་ནི་ཆོས་དང་གྲངས་ལ་སོགས་པའི་ཆེན་པོ་རྣམས་དང་ལྡན་པ་དང་། སློབ་པ་དང་མི་སློབ་པ་ལས་འཕགས་པའི་ཕྱིར་ཁྱད་པར་ཆེ་བ་དང་། ཤེས་རབ་དང་ཡེ་ཤེས་མཐོང་བའི་ཕྱིར་ཡོན་ཏན་ཆེ་བ་དང་། སྟོང་ཕྲག་བཅུ་གཉིས་སྙེད་བཞུགས་པའི་ཕྱིར་གྲངས་མང་བས་ཆེ་བའོ། །
--- END BLOCKS ---
