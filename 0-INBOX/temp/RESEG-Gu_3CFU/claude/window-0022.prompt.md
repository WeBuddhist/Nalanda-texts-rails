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
[Block 771]
གལ་ཏེ་ཉམས་དམས་པར་གྱུར་ན་ཁྱེའུ་སུས་བྱའོ། །

[Block 772]
དེར་ངོ་མི་ཤེས་པ་ཞིག་ཤན་བསྲེ་བས་ཉེ་བར་གནས་པར་གྱུར་ན་དེར་གཏོགས་པས་ངེས་པར་ཤེས་པར་བྱ་བའི་ཕྱིར་དྲི་བར་བྱ་ཞིང་དེའི་ཆེད་དུ་མི་འཇུག་པར་བྱ་བའི་ཕྱིར་དགེ་སློང་བསྒོ་བ་བསྐོའོ༌[^549]ཞེས་བྱ་བ་ལ། ཤན་བསྲེ་བས་ཞེས་བྱ་བ་ནི་ཁོ་བོ་ཁྱེད་ཅག་ལས༌[^550]གང་ཡང་རུང་བ་ཞིག་ཡིན་ནོ་ཞེས་བྱ་བ་གསེབ་ཏུ་འཇུག་པར་བྱ་བས་སོ། །

[Block 773]
དེར་གཏོགས་པ༌[^551]ཞེས་བྱ༌[^552]ནི་བསྲོ་ཁང་ན་རྣམ་པར་གནས་པའི་དགེ་སློང་གིས་ཏེ་དེས་དྲི་བར་བྱའོ། །ཇི་ཞིག་གི་ཕྱིར་ཞེ་ན། ཇི་ཆོས་འདི་པའི་དགེ་སློང་ཞིག་གམ་འོན་ཏེ་འཚོ་བ་པ་ལ་སོགས་པ་ཞིག་ཡིན་ཞེས་ཏེ་དེ་ལྟར་ངེས་པར་ཤེས་པར་བྱ་བའི་ཕྱིར་དྲི་བར་བྱ་ཞིང་། དེའི་ཆེད་དུ་སྒོ་བ༌[^553]བསྐོའོ༌[^554]ཞེས་བྱ་བ་འདི་མི་ཤེས་པ་ཤན་བསྲེ་བས་ཉེ་བར་གནས་པར་གྱུར་པ་དེ་ངེས་པར་ཤེས་པར་བྱ་བའི་ཕྱིར་དྲི་བར་བྱ་བ་དང་མི་འཇུག་པར་བྱ་བའི་ཕྱིར་ཞེས་བྱ་བའོ། །

[Block 774]
འདི་ནི་བདག་ཅག་ལས་གང་ཡང་རུང་བ་ཡིན་པས་ཞེས་བྱ་བའི་དྲི་བས་འདི་ཤེས་པ་ལའོ། །

[Block 775]
བསྒོ་བ་ཇི་ལྟ་བུ་ཞིག་ཅེ༌[^555]ན། དགེ་སློང་ཞེས་བྱ་བ་སྨོས་ཏེ། འདི་ནི་དཔེ་ཡིན་གྱི་བསྙེན་པར་རྫོགས་པར་མ་བྱས་པའི་རབ་ཏུ་བྱུང་བ་ལ་ཡང་དགེ་སློང་མ་རྣམས་ལ་དེའི་ཕྱོགས་སུ་གྱུར་པའི་གང་ཟག་ལའོ། །

[Block 776]
དེར་མ་དད་པ་འཇུག་ཏུ་མི་གཞུག་པའོ་ཞེས་བྱ་བ་ལ། དེར་ཞེས་བྱ་བ་ནི་བསྲོ་ཁང་ལའོ། །

[Block 777]
སོ་སོར་གནས་བཞིན་པ་ལ་ཡང་ཤན་བསྲེ་བས་སོ། །

[Block 778]
འདི་ནི་འདིར་སྒོ་སྐྱོང་གི་དོན་གཞན་ཡིན་ནོ། །

[Block 779]
དེར་བྱི་དོར་གྱི་ལས་ནི་ལྷན་ཅིག་གནས་པ་དང་ཉེ་གནས་དག་གིས་བྱའོ་ཞེས་བྱ༌[^556]བ་ལ། དེར་ཞེས་བྱ་བ་ནི་བསྲོ་ཁང་ལའོ། །

[Block 780]
གཞན་ལས་ནི་གཞོན་རབས་དག་གིས་ཞེའོ་ཞེས་བྱ་བ་ལ། འདི་ནི་འདོད་པ་གཞན་རབ་ཏུ་བསྟན་པ་ཡིན་ནོ། །

[Block 781]
ཁ་ཅིག་རྣམས་ལ་ནི་འདོན་པ་གཞན་ཡིན་ཏེ། གཞོན་རབས་དག་གིས་བྱི་དོར་གྱི་ལས་བསྲོ་ཁང་གི༌[^557]ལས༌[^558]ཞེས་བྱ་བའོ། །

[Block 782]
[^559]བྱི་དོར་གྱི་ལས་ཀྱི་ངོ་བོ་བསྟན་པའི་ཕྱིར་སྦྲེན་པ༌[^560]དང་ཟངས་དང་འབྲུ་མར་དང་། སོ་ཤིང་དང་བ་ལང་གི་ལྕི་བ་དང་། ས་དང་བྱེ་མ་དང་ཆུ་ལ་སོགས་པ་ཉེ་བར་གཞག་པ་དང་། ཤིང་བརྟག་པ་དང་དྲིལ་ཕྱིས་དང་། སྣུམ་གྱིས་བསྐུ་བ་དང་བཀྲུ་བ་དང་། ཕྱགས་པ༌[^561]དང་ཕྱག་དར་དོར་བ་ལ་སོགས་པའོ། །

[Block 783]
དེ་དག་གི་ནི་གཅིག་གིས་གཅིག་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གཙུག་ལག་ཁང་གི་ནང་ན༌[^562]གནས་པ་རྣམས་དང་ལྷན་ཅིག་ཏུ་དྲིལ་ཕྱིས་ལ་སོགས་པའི་ལས་ལ་གཅིག་ལ་གཅིག་བསྒོ་བའོ། །

[Block 784]
ཁྲིའུ༌[^563]དང་ཉ་ཕྱིས་དག་ཀྱང་གཙང་སྦྲ་ཉིད་བྱས་ནས་གནས་ཇི་ལྟ༌[^564]བར་གཞག་གོ་ཞེས་བྱ་བ་ལ་སོགས་པའི་སྒྲས་ནི་འཕེན་པའི་ལས་བསྡུ་བ་ནི༌[^565]མ་མོ་ལས་འདར་ཞེས་བྱ་བ་ལ་སོགས་པ་ནས་མདུན་དུ་འདུག་སྟེ་མེ༌[^566]མི་འདེའོ་ཞེས་བྱ་བའི་བར་དུའོ། །

[Block 785]
སྣོད་སྤྱད་ཐམས་ཅད་ལ་ཆོ་ག་དེ་བཞིན་ནོ་ཞེས་བྱ་བ་ནི་གཙང་སྦྲ་ཉིད་བྱས་ཏེ། [^567]གནས་ཇི་ལྟ་བར་གཞག་གོ་ཞེས་བྱ་བ་འདིའོ། །

[Block 786]
ཡོ་བྱད་ཐམས་ཅད་ལ་ལེགས་པར་སྦ་བ་དང་། བྱི་དོར་བྱའོ་ཞེས་བྱ་བ་ནི་སྣོད་ཀྱི་ཚིག་གིས་ཡོ་བྱད་གང་ཡང་བཟུང་བར་མི་བྱ་སྟེ། བསྲོ་ཁང་གི་ཐ་མ་ལས་གཞན་དུའོ། །

[Block 787]
མདོ་འདི་ནི་སྒྲུབ་པ་པོའི་དོན་དུ་སྟེ། དེར་སྒྲ་བསྐྱུངས་ཏེ་འཇུག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་བསྲོ་ཁང་དུའོ། །

[Block 788]
མཛེས་པར་རོ། །

[Block 789]
ལེགས་པར་བསྡམས་པ་དང་། སྤྱོད་ལམ་མཛེས་པ་དང་ཤེས་བཞིན་དུའོ་ཞེས་བྱ་བ་ལ། ལེགས་པར་བསྡམས་པ་ནི་རང་ཉིད་ཀྱི་ལུས་དང་ངག་མ་ཡེངས་པར་ལེགས་པར་བསྡམས་པ་ཉིད་ཀྱིས་སྟེན་པར༌[^568]བྱེད་དོ། །ཤེས་བཞིན་དུ་ཞེས་བྱ་བ་འདིས༌[^569]ནི་སེམས་ལའོ། །

[Block 790]
སྤྱོད་ལམ་མཛེས་པ་ཉིད་འདི་ལ་རབ་ཏུ་དབྱེ་བ་གཉིས་ཀྱིས་བསྟན་ཏོ། །

[Block 791]
མདུན་དུ་འདུག་སྟེ་མེ་མི་འདེའོ་ཞེས་བྱ་བ་ནི་གཞན་ཡང་མེ་དེ་བཞིན༌[^570]པ་ལ་བསྒྲིབས་ནས་བདག་ཉིད་ཀྱིས་མེ་མི་འདེའོ་ཞེས་བྱ་བའི་ཚིག་གོ། །

[Block 792]
འདུ་འཛིའི་གཏམ་ཡང༌[^571]ངོ་ཞེས་བྱ་བ་ནི་དེར་ཞེས་བྱ་བར་སྦྱར་ཏེ་འདི་ནི་འདོད་པ་དང་རྗེས་སུ་མཐུན་པར་བྱར༌[^572]ཤེས་ནས་བསྲོ་ཁང་དུ་འཇུག་པ་ན་འདོད་པ་རྣམས་ཡང་དག་པར་འབར་བ་ནི་འདུ་འཛི་ཞེས་བྱའོ།[^573] །དེ་བས་ན་འདིར་འདི་སྤོང་བ་ནི་བྱེ་བྲག་ཏུ་སྤོང་བའོ། །

[Block 793]
འཕགས་པའི་མི་སྨྲ་བ་ཉིད་ལ་དམིགས་པས་སོ་ཞེས་བྱ་བ་ནི་དེར་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 794]
རྟོགས་པ༌[^574]མི་བདེན་པ་དང་། དེ་དང་རྗེས་སུ་མཐུན་པའི་སེམས་རྣམ་པར་བཟློག་པའི་དོན་དུ་མདོ་འདིའོ། །

[Block 795]
འཕགས་པའི་མི་སྨྲ་བ་ཉིད་ནི་ཚུལ་བཞིན་དུ་ཡིད་ལ་བྱེད་པ་ལ་ཀུན་ནས་ཕྱོགས་པར་བྱེད་པར་རིག་པར༌[^575]བྱའོ། །

[Block 796]
མཇུག༌[^576]ཏུ་རྒྱུན་ཆགས་གསུམ་པ་གདོན་ནོ་ཞེས་བྱ་བ་ནི་འགྲོ་བའི་དུས་སུའོ། །

[Block 797]
གོས་གཅིག་པས་བྱི་དོར་གྱི་ལས་མི་བྱའོ་ཞེས་བྱ་བ་ནི་འདིར་ནི་བསྲོ་ཁང་གི་ཚིག་དང་ཁྲོ་བ་ལ་གནས་པར་གྲགས་པའི་གཞི་གཅིག་གིས་གཅིག་གི་ཚིག་ཀྱང་ཁ་ཅིག་བྱེད་དེ། ཆོས་གོས་གཅིག་པའི་དགེ་སློང་རྣམས་ཀྱིས་བསྲོ་ཁང་དུ་གཅིག་གིས༌[^577]གཅིག་ལ་ལས་མི་བྱ་ཞེས་བྱ་བའོ། །

[Block 798]
ལས་ཐམས་ཅད་ལ་ལུས་ལ་གནས་པ་ཉིད་གནས་ཐམས་ཅད་ལ་མ་ཡིན་ཏེ། བསྲོ་ཁང་ཉིད་ལ་ཆོ་ག་འདི་རྣམ་པར་གནས་པ་མ་ཡིན་པ་ཉིད་དེ། དེ་བས་ན་འདི་བསྟན་པ་མ་ཡིན་ནོ། །

[Block 799]
ལུས་ཀྱི་དེ་ལ་མ་དད་པ་བྱེད་དུ་མི་གཞུག་གོ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བ་ནི་ལས་སོ། །

[Block 800]
ཁུར་ཁུར་བ་ལ་སོགས་པ་ཕྱི་རོལ་གྱི་ལས་ནི་བཀག་པ་མ་ཡིན་ནོ། །

[Block 801]
འདི་དང་གོང་མ་ལ་ཡང་བསྟན་པ༌[^578]ནི་དད་པ་ཅན་དུ་འདོད་དོ་ཞེས་བྱ་བ་ལ། བསྟན་པ༌[^579]ཞེས་བྱ་བ་ནི་དུས་རིང་པོ་ནས་སྐྱེས་པས་གང་ཞིག་མི་གཡོ་བ་དེ་ནི་བསྟན༌[^580]པའོ། །

[Block 802]
འདི་དང་ཞེས་བྱ་བས་དེ་མ་ཐག་ཏུ་བརྗོད་པའི་ལས་ཀྱི་ཆོ་ག་ལའོ། །

[Block 803]
གོང་མ་ལ་ཡང་ཞེས་བྱ་བ་ནི་དད་པ་ཅན་མ་ཡིན་པ་འདིར་ཞུགས་པ་མི་སྦྱིན་ཞེས་བྱ་བ་འདི་ལའོ། །

[Block 804]
འདོད་དོ་ཞེས་བྱ་བ་ནི་མངོན་པར་འདོད་པའོ། །

[Block 805]
སེང་གེ་ལྟ་བུས་ཝ་ལྟ་བུ་ལ་བསྙེན་བཀུར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ཚུལ་ཁྲིམས་དང་ལྡན་པས་ཚུལ་ཁྲིམས་འཆལ་པ་ལ་ཉེ་བར་གནས་པར་མི་བྱ༌[^581]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 806]
འདི་ལ་གསལ་བར༌[^582]བྱེད་པ་ཡིན་པ་ནི། སློབ་དཔོན་དང་མཁན་པོ་མཆོག་ཏུ་ཚུལ་ཁྲིམས་འཆལ་པ་ལ་ཡང་བསྙེན་བཀུར་བྱའོ། །

[Block 807]
ཕ་མ་དང་ནད་པ་དག་ནི་ཁྱིམ་པ་ཡིན་ན་ཡང་ངོ་ཞེས་བྱ་བ་ནི་མཆོག་ཏུ་འདི་རྣམས་ལ་ཕན་པར་བྱེད་པ་ཉིད་ཀྱི་ཕྱིར་དེ་བས་ན་འདི་སྔོན་དུ་གནང་ངོ་། །ལེགས་པར་སྦྱར་བའི་ཁྲུས་ཀྱིས་བཀྲུའོ་ཞེས་བྱ་བ་ནི་འདིར་གླེང་གཞི་ལས་འདོད་པ་ཡིན་ཏེ། ནད་པའི་ཚིག་ནི་ཐ་སྙད་དུ་མ་བྱས་པ༌[^583]ཡིན་ཏེ། འདི་ལ་གཞན་དུ་མཐུན་པ་ཉིད་ཀྱང་མ་ཡིན་ཏེ། ཁྱད་པར་ཡོངས་སུ་མི་འཛིན་པའི་ཕྱིར་ཐམས་ཅད་ཀྱི་དབང་དུ་མཛད་ནས་ཉེ་བར་བརྟགས་པའོ། །

[Block 808]
དེའི་རང་གི་ངོ་བོ་ཉིད་བསྟན་པའི་ཕྱིར། རླུང་འདྲེན་པའི་རྩ་བ་དང་སྡོང་བུ་དང་ལོ་མ་དང་མེ་ཏོག་དང་འབྲས་བུ་བསྐོལ་བས་ཁྲུས་བྱ་བ་ནི་དེའི་མིང་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ལེགས་པར་སྦྱར་བའི་ཁྲུས་ཀྱིས་བཀྲུའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 809]
བཅུད་ནི་ཁྲུས་ཀྱི་དོན་ཏོ། །

[Block 810]
དེ་བས་ན་འདི་རྣམས་ལ་འདིར་ཡན་ལག་ཉིད་དོ། །
--- END BLOCKS ---
