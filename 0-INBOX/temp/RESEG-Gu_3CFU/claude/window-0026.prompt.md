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
[Block 911]
འདིར་ལྷན་པ༌[^646]ནི་དབེན་པའི་ཕྱོགས་སུ་བསྒྲུབ་པར་བྱའོ། །

[Block 912]
སོ་སོར་མ་སྦས་པར་འདི་བྱེད་པར་གྱུར་ན་མ་དད་པ་སྐྱེ་བའི་དངོས་པོར་འགྱུར་རོ་ཞེས་བྱ་བ་བསྟན་པའི་ཕྱིར་མདོ་འདིའོ། །

[Block 913]
དགེ་འདུན་གྱིས་མགར་སྤྱད་དག་བསྲེལ་བར་བྱའོ། །

[Block 914]
བུ་གུ་དེའི་ཞེས་བྱ་བ་ནི་ལྷན་པའོ། །

[Block 915]
བུ་རམ་དང་རྒྱ་སྐྱེགས་ཀྱི་ཚིགས་མ༌[^647]དང་སྤྲ་ཚིལ་དང༌[^648]ཞ་ཉེ་དཀར་པོ་དང་ཞ་ཉེ་ནག་པོ་རྣམས་ཀྱིས་མི་བཟང་ངོ་། །འོ་ན་གང་བཟང་ཞེ་ན། དེའི་ཕྱིར་ལྷན་རིངས་དང་ཐམ་ཕྲན༌[^649]དང་ལྷན་པ་དང་ཆུ་སྲིན་གྱི་སོ་ལྟ་བུ་དག་བཟང་ངོ་ཞེས་བྱ་བ་དག་སྨོས་ཏེ། ཕྱེ་མས་ཀྱང་ངོ་། ། ལྕགས་ཀྱི་འམ་རྡོའིའོ། །

[Block 916]
ལྷན་པ་བཟང་ངོ་ཞེས་བྱ་བ་རྗེས་སུ་འབྲེལ་ལོ། །

[Block 917]
འབྲུ་མར་གྱིས་བདར་རོ་ཞེས་བྱ་བ་སྟེ་ཕྱེ་མས་སོ། །

[Block 918]
ཇི་སྲིད་དུ་བདར་ཞེ་ན་དེའི་ཕྱིར་སྤྲ་ཚིལ་དང་འདྲ་བ་ལ་ཐུག༌[^650]པར་གྱུར་པས་སོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 919]
རྫས་ཅི་ཞིག་བདར་བར་བྱ༌[^651]ཞེ་ན། དེའི་ཕྱིར་ལྕགས་སམ་ཀུ་རུ༌[^652]བིན་དས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འབྲུ་མར་དང་ཕྱེ་མ་བསྲེས་ནས་གླན་པར་བྱ་སྟེ། ཇི་སྲིད་དུ་སྤྲ་ཚིལ་འདྲ་བར་གྱུར་པ་དེ་སྲིད་དུ་བདར་བར་བྱའོ༌[^653]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 920]
དྲོ་བ་ལ་གླན་ནོ་ཞེས་བྱ་བ་ནི་ལྷུང་བཟེད་ལ་ཞེས་བྱ་བ་སྐབས་ཀྱིས་རྟོགས་ཏེ་ལྷུང་བཟེད་དྲོ་བ་ལ་ཕྱེ་མ་བདར་བས་གླན་པའོ། །

[Block 921]
གྲོ་བས༌[^654]གཡོགས་ཏེ་འཇིམ་པ༌[^655]བསྐུས་ལ་ཇི་རན་ཙམ་དུ་བསྲོའོ་ཞེས་བྱ་བ་ལ་རྗེས་སུ་འབྲེལ་ལོ། །

[Block 922]
དྲོ་བ་ཇི་ལྟ་བུར་སྦྱར་ཞེ་ན། དེའི་ཕྱིར་བར་མ་ནི་འབྲུ་མར་གྱིས་བདར་རོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གླན་པ་དེ་ལ་འབྲུ་མར་གླན་ནས་བདར་བར་བྱའོ། །

[Block 923]
བུ་རམ་དང་འཇིམ་པས་སོ་ཞེས་བྱ་བ་ནི་ས་ལས་བྱས་པའི་ལྷུང་བཟེད་ལ་བུ་རམ་དང་འཇིམ་པས་གླན་པའོ། །

[Block 924]
ལྷན་རིངས་ཞེས་བྱ་བ་ལ་སོགས་པ་ལྔ་པོའི་གནས་སུ་བུ་རམ་དང་འཇིམ་པ་བཟུང་བའོ། །

[Block 925]
དེ་བས་ན་ལྷག་མ་འདི་ལས་སྔ་མ་ལ་རྗེས་སུ་འབྲེལ་བ་ཇི་ལྟར་རིགས་པ་རིག་པར་བྱའོ། །

[Block 926]
སྤྱོད་པ་ཉིད་ཡིན་ན་འདུས་བྱས་པ་ལ་སོ་སོར་ཉེ་བར་སྦྱོར་བ་ནི་ཐབས་སོ། །

[Block 927]
དེ་ལ་དུས་ཇི་ཙམ་གྱིས་ལྷུང་བཟེད་ལ་དེ་འདུས་མ་བྱས་པ་ཉིད་གང་གིས་བསྲེག་པར༌[^656]འོས་པ་ཉིད་ཅེ་ན། འདིར་བརྗོད་པར་བྱ་སྟེ་སྤྱོད་པ་ཉིད༌[^657]ཡིན་ན་ཟླ་བ་དྲུག་གི་འོག་ཏུ་བསྲེག་པ༌[^658]ཉིད་དོ་ཞེས་བྱ་སྟེ། བྱེ་བྲག་ཏུ་བརྗོད་པ༌[^659]ནི་ས་ལས་བྱས་པ་ལ་གསལ་བར་བྱེད་དེ། གལ་ཏེ་ས་ལས་བྱས་པའི་ཡིན་ན་ཟླ་བ་ཕྱེད་ནའོ་ཞེས་བྱ་བ་ནི་བསྲེག་པ༌[^660]ཉིད་དོ་ཞེས༌[^661]བྱ་བ་དང་རྗེས་སུ་འབྲེལ་ལོ། །

[Block 928]
སྤྱོད་པ་མ་ཡིན་པ་ཉིད་ལ་ཡང་ནི་ཇི་ལྟར་སྦྱོར་བས་ལྷུང་བཟེད་ལ་སོ་སོར་འདུ་བྱ་བ་བསྒྲུབ་པར་བྱའོ། །

[Block 929]
གལ་ཏེ་དབྱར་བྱུང་ན་དེའི་བྱ་བའི་བར་དུ་བསྐུ་བ་དང་རྩུབ་ཁྲུས་ཉིད་ཀྱིས་ལེགས་པར་བཅོས་པ་ཉིད་བྱའོ་ཞེས་བྱ་བ་ནི་སྲོག་ཆགས་རྣམས་ལ་ཉེ་བར་འཚེ་བ་མེད་ཅིང་ནུས་པ་མེད་པ་ཉིད་ལ་འདི་སྦྱིན་པ་ཉིད་དོ། །

[Block 930]
བསྲེགས་པ༌[^662]ལ་གནས་པས་འཚོ་བ་ལ་འདི་བརྗོད་པ་ཡིན་ནོ། །

[Block 931]
བྱ་བའི་བར་ནི་དགོས་པའི༌[^663]དུས་གཉིས་ཀྱི་བར་རོ། །

[Block 932]
དེར་ལྷུང་བཟེད་འདི་ལ་བཀྲུ་བ་དང་རྩུབ་ཁྲུས་ཉིད༌[^664]ཀྱིས་ལེགས་པ་ཉིད་དོ། །

[Block 933]
བྱ་བ་བྱས་པ་སྟེ་བསྐུ་བ་བྱས་ནས་གཞག་པར་བྱའོ། །

[Block 934]
བྱ་བའི་དུས་གཞན་ལ་རྩུབ་ཁྲུས་ཉིད་བྱ་ཞེས་བྱ་བའོ། །

[Block 935]
དེ་ལྟར་ན་འདི་ལེགས་པར་བཅོས་པ་ཞེས་བྱ་བ་དོན་གྱིས་གོ་བར་བྱའོ། །

[Block 936]
དེ་བསྲེག་པར་བྱའོ་ཞེས་བྱ་བ་ལ་དེ་ནི་ལྷུང་བཟེད་དོ། །

[Block 937]
འདི་ནི་བདག་ཉིད་ཀྱིས་བྱེད་པར་མི་རིགས་པ་མ་ཡིན་ཏེ། འདི་ནི་རབ་ཏུ་བྱུང་བ་ལ་བདག་ཉིད་ཀྱིས་བྱེད་པར༌[^665]རིགས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 938]
དེའི་ཆེད་དུ་རྫ་བོ་བསྲེལ་བར་བྱའོ་ཞེས་བྱ་བ་ལ། དེའི་དོན་དུ་ཞེས་བྱ་བ་ནི་བསྲེག་པའི་དོན་དུའོ། །

[Block 939]
དེ་ཇི་ལྟ་བུ་ཞིག་ཅེ་ན། དེའི་ཕྱིར་དེ་ཉིད་དུ་གྲུབ་པའམ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེའི་དངོས་པོ་དེ་ཉིད་ལ་རྫ་བོ་ཉིད་ཀྱིས་གང་གིས་བསྐྱེད་པའོ། །

[Block 940]
དེ་གྱུར་པ་ཉིད་ཀྱིས་གང་བྱེད་པ་དེ༌[^666]བུམ་པ་ལ་སོགས་པའི་ཡན་ལག་གཉིས་ཀྱིས་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 941]
ཅི་འདི་ཉིད་གཅིག་པུ་ལ་ཡིན་ནམ་མ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་དེ༌[^667]ཉིད་དུ་གྲུབ་པ་འམ་དབྱིབ་མོ་ཡང་རུང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཉེ་བར་གཞག་པ་ཞེས་བྱ་བ་དང་རྗེས་སུ་འབྲེལ་ལོ། །

[Block 942]
ཇི་ལྟར་དབྱིབ་མོ་འདོད་པས་རྫ་བོ་འདི་ལ་བསྒྲུབ་པའི་དོན་དུ་བུམ་པ་ལ་སོགས་པ་བཅག་པ་བཟང་སྟེ་བསྟན་པའི་ཕྱིར། ཐལ་བས་བཀང་སྟེ་རྫ་གཟང༌[^668]གིས་བརྐོས་ན་བཟང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བུམ་པ་བཅག་པས་ཆག་པའོ། །

[Block 943]
ཅི་ཞིག་གིས༌[^669]ཤེ་ན་རྫ་གཟང༌[^670]གིས་ཞེས་བྱ་བ་སྨོས་ཏེ། ལྕགས་ལས་བྱས་པའི་ཕུར་པ་འདིའི་མིང་ངོ་། །བུམ་པ་བཅག་པ་དེ་སུ་ཞིག་ལ་དགབ་པར༌[^671]བྱ་ཞེ་ན། དེས་དུ་བ་མི་འཆོར་བ་སྟེ་རྫ་བོས་ལྷུང་བཟེད་ལའོ། །

[Block 944]
དགབ་པ༌[^672]ཇི་ལྟ་བུ་ཞེ་ན། དུ་བ་མི་འཆོར་བར་ཏེ། གང་ལྟ་བུ་ལ་དུ་བ་མི་འཆོར་བ་དེ་ལྟ་བུ་འདི་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ།[^673] །ཅི་ཞིག་ཕྱི་རོལ་མ་བྱུགས་པ་ཉིད་ཀྱི༌[^674]རྫ་བོས་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་ཕུབ་མ་དང་འཇིམ་པར་སྦྱར་བས་ཕྱི་རོལ་བྱུགས་པས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཕུབ་མ་དང་འཇིམ་པ་སྦྱར་བས་ཕྱི་རོལ་བྱུགས་པ་གང་ལ་དེས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 945]
འདི་ལ་རྫས༌[^675]ཅི་ཞིག་བྱུགས་པས་ནང་དུ་མ་བྱུགས་པ༌[^676]ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་འབྲུ་མར་གྱི་ཚིགས་མའམ་ལྕི་བས་ནང་བྱུགས་པས་སོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 946]
ཅི་བྱུགས་པ༌[^677]སྦྱར་བས་སྐམས༌[^678]པས་ཡིན་ནམ་ཞེ་ན། དེ༌[^679]བསྐམས་པར་གྱུར་པས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ས་ཅི་ལྟ་བུ་དང་ཅི་ཞིག་བཏིང་བའི་ས་ལ་ལྷུང་བཟེད་བཞག་པ་ལ་འདིས་དགག༌[^680]ཅེ་ན། དེའི་ཕྱིར་ས་གཞི་བྱི་དོར་བྱས་པར་ཕུབ་མ་བཏིང་ཞིང་དུ་བ་འཆོར་བར་བྱེད་པ༌[^681]འབྲུ་མར་གྱི་ཚིགས་མ་ལ་སོགས་པའི་རྫས་བཀྲམ་པའི་སྟེང་དུ་ཁ་བུབ་ཏུ་བཞག་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཕུབ་མའི་སྟེང་དུ་སྣང་བའི་ངང་ཚུལ་ཅན་འབྱུང་བར་བྱེད་པའི་འབྲུ་མར་གྱི་ཚིགས་མ་ལ་སོགས་པའི་རྫས༌[^682]རྣམས་བཀྲམ་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །ཇི་ལྟར་གཞག་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་ཁ་བུབ་ཏུ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 947]
འདིའི་རྗེས་སུ་ཅི་བྱ་ཞེ་ན། དེའི་ཕྱིར་ལྕི་བ་དག་དང་སོགས་མ་བཅེར་ཏེ་སྦར་རོ། །

[Block 948]
ཏེ་པོར་གྲངས་ནས་དབྱུང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ།[^683] ལྷུང་བཟེད་ཁ་དོག་རྫོགས་པ་ཕུན་སུམ་ཚོགས་པར་འགྱུར༌[^684]གྱི་བར་དུ་བཟླས་པར་བྱའོ་ཞེས་བྱ་བ་ལ། ཇི་སྲིད་དུ་ཁ་དོག་གྲུབ་པ༌[^685]དེ་སྲིད་དུ་བསྲེག་པ་སྦྱིན་པར་བྱའོ། །

[Block 949]
བྱི་དོར་བྱས་ཤིང་བྱི་དོར་བྱས་ཤིང་གཞུག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་བསྲེག་པ༌[^686]རེ་རེ་ལ་བྱི་དོར་བྱ༌[^687]ཞེས་བྱ་བའི་དོན་ནོ། །

[Block 950]
སྲོག་ཆགས་རྣམས་ལ་སྙིང་བརྩེ་བས་ཉེ་ཀོར་ཕྱག་དར་དང་ཆག་ཆག་བྱའོ་ཞེས་བྱ་བ་ནི་ཆུས་ཉེ་འཁོར་ཉིད་ལའོ། །
--- END BLOCKS ---
