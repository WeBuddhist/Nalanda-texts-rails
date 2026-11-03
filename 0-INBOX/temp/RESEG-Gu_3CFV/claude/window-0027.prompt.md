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
བརྟགས་པ་ནས་འདོམ་གང་འཁོར་ཡུག་ནི་དེ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཆུ་བརྟག་པའི་གནས་ནས་འདོམ་གང་འཁོར་ཡུག་ཚུན་ཆད་ནི་བརྟགས་པ་ཉིད་ཡིན་ནོ། །

[Block 947]
འདིར་གཞུང་ནི་བཙུན་པ་ཆབ་ཀའི་ཉེ་འཁོར་གང་ལགས། ཉེ་བ་འཁོར་འདོམ་གང་ངོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 948]
ཉེ་འཁོར་ཞེས་བྱ་བ་ནི་ཆབ་ཀའི་དཔེ་ཙམ་ཉིད་ཡིན་ནོ་ཞེས་བྱེ་བྲག་མེད་པར་གསུངས་སོ། །

[Block 949]
མིག་གིས་དག་པ་ཉིད་ཀྱིས་ཆུ་ནི་དག་པ་ཡིན་ནོ་ཞེས་བྱ་བ་སྟེ། མིག༌[^575]གང་གིས་ཤེ་ན། དེའི་ཕྱིར་ཐ་མལ་པས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་གཞུང་ནི་ཚེ་དང་ལྡན་པ་མ་འགགས་པས་ལྷའི་མིག་གིས་ཆུ་བརྟགས་པ་ན་དེའི་ཚེ་སྲིད་པ་བར་མ་པའི་སྲོག་ཆགས་དག་གིས་ཐམས་ཅད་ཁྱབ་པར་མཐོང་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ལྷའི་མིག་ནི་ཐ་སྙད་དུ༌[^576]གདགས་སུ་མི་རུང་སྟེ། དེ་བས་ན་ལྷའི་མིག་གིས་ཆུ་བརྟག་པར་མི་བྱ་བར་འདི་ལྟར་ཆུ་རུང་བ་ལྔ་བཤད་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 950]
མི་གཡོ་བ་ཉིད་དང་རྙོག་པ་མེད་པ་ཉིད་ལ་བརྟག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་བརྟག་པར་བྱ་བའི་ཆུ་ཞེས་བྱ་བ་ཤུགས་ཀྱིས་རྟོགས་པར་བྱའོ། །

[Block 951]
བུམ་པ་གང་བ་ཉིད་ལའོ་ཞེས་བྱ་བ་ནི་བརྟག་པར་བྱ་ཞེས་བྱ་བ་འཇུག་པ་ཡིན་ནོ། །

[Block 952]
དེ་ལ་བྱ་བ་ལས་འདས་པར་བགྲང་བའི༌[^577]ཡུན་རིང་པོ་ཉིད་དུ་མི་བྱའོ་ཞེས་བྱ་བ་ནི་དེ་བྱ་བ་ལས་འདས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ཡུན་རིང་བ་ཉིད་ཀྱིས་གྲངས་སུ་གྲགས་པ་འདིར་ནི་ཡུན་རིང་པོ་ཉིད་དུ་བརྟག་པར་མི་བྱའོ། །

[Block 953]
གང་གི་ཕྱིར་ཇི་ཙམ་གྱིས་སེམས་དག་པར་གྱུར་པ་དེ་ཙམ་དུ་བརྟག་པར་བྱའོ། །

[Block 954]
འོག་ཏུ་མ་གྲུབ་པ་ལ་སེམས་དག་པར་འགྱུར་བས་གདོན་མི་ཟ་བར་ཤིན་ཏུ་རིང་པོར་བྱས་པ་ཉིད་ཀྱི་ཕྱིར་ཤིན་ཏུ་རིང་པོར་བརྟག་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 955]
འོན་ཀྱང་ཇི་ཙམ་གྱིས་བ་ལང་དྲུག་དང་ལྡན་པའི་ཤིང་རྟ་རྨིག་པའི་ཤར་བས་བཀང་བ་གཡངས་ཀྱིས་འཁོར་བར་གྱུར་པ་དེ་སྲིད་དུ་བརྟག་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 956]
ཡང་དེ་སྲིད་དུ་སེམས་དག་པར་གྱུར་པ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 957]
དེ་ལ་སེམས་དག་པར་གྱུར་པ་ཞེས་བྱ་བ་དེ་ལ་སེམས་དག་པར་གྱུར་ཅེས་བྱ་བ་ནི་མིག་གིས་དག་པ་ཉིད་ཅེས་བྱ་བ་དེ་ཡིན་པས། དེའི་ཕྱིར་ཞེས་བྱ་བ་འདི་ལས་ལྷག་པར་གྱུར་པ་མ་ཡིན་ནོ། །

[Block 958]
བ་ལང་དྲུག་གིས་ཞེས་བྱ་བ་ནི་དེ་ཉིད་འདིར་ཚད་མ་ཡིན་ཏེ། དུས་འདི་ཙམ་གྱིས་དེ་ལ་ཕལ་ཆེར་བསྒྲུབ་པར་འགྱུར་ཞེས་བྱ་བའོ། །

[Block 959]
ཧ་ཅང་ཡུན་རིང་དུ་བརྟག་པར་མི་བྱ་བར་ཞེས་བྱ་བ་འདིས་འདི་བསྡུས་པ་ཡིན་ནོ། །

[Block 960]
འདིར་རྩེ་གཅིག་པ་ནི་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 961]
རྩེ་མོ་འཇམ་པོས་སྲོག་ཆགས་དག་བསྟན་ལའོ། །

[Block 962]
དེ་དག་འཆི་བར་འགྱུར་བའི་ལམ་དུ་མི་འདོར་རོ་ཞེས་བྱ་བ་ནི་ཆུའི་སྲོག་ཆགས་དེ་དག་དོར་བའི་ལམ་གྱི་ཐག་ཇི་སྲིད་ཀྱིས་འཆི་བར་འགྱུར་བའི་ལམ་གྱི་ཐག༌[^578]དེ་སྲིད་དུ་དོར་བར་མི་བྱའོ། །

[Block 963]
གཞན་ཡང་མི་དོར་རོ་ཞེས་བྱ་བ་ནི་ཆུའི་སྲོག་ཆགས་དག་ལས་གཞན་ལ་ཤིག་དང་རྩྭ༌[^579]ཤིག་ལ་སོགས་པ་དག་ཀྱང་འཆི་བར་འགྱུར་བའི་ལམ་གྱི་ཐག་དེ་སྲིད་དུ་མི་དོར༌[^580]རོ། །

[Block 964]
གལ་ཏེ་མར་མེའི་ནང་དུ་སྲོག་ཆགས་ལྟུང་ན་དེ་བྱེད་པས་དེ་གཡོགས་པར༌[^581]བྱའོ་ཞེས་བྱ་བ་ནི་མར་མེད་དེ་བྱེད་པས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 965]
དེའི་ངོ་བོ་ཉིད་ཇི་ལྟ་བུ་ཞེ་ན། དེའི་ཕྱིར་སྨྱིག་ཚལ་གྱི་གཟེབ་དར་དཀར་རམ་ལྷང་ཚེར་སྲབ་མོས་གཡོགས་པ༌[^582]སྟེ་དེ་ཞེས་བྱ་བ་ནི་འོད་ཁང་ཞེས་བྱའོ། །

[Block 966]
མིག་བརྒྱ་པ་ཡང་རུང་ངོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 967]
འདིར་གཞུང་ནི་འོད་ཁང་གི༌[^583]གཟེབ་དར་དཀར་གྱིས་གཡོགས་པར་བྱའོ། །

[Block 968]
དེ་མི་རྙེད་ན་ལྷང་ཚེར་སྲབ་མོས་གཡོགས་པར༌[^584]བྱའོ། །

[Block 969]
དེ་ཡང་མ་རྙེད་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། མིག་བརྒྱ་པ་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 970]
མིག་བརྒྱ་པ་ཇི་ལྟ་བུ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་དང་པོ་ནས་བྱས་པའམ་བུམ་པ་ལ་སོགས་པའི་སྣོད་བུ་ག་ཅན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ།

[Block 971]
དང་པོ་ཉིད་དུ་སྐྱེད་པར་བྱེད་པའི་བྱས་པ་འདི་ལ་ཡོད་པས་ན་དང་པོ་ཉིད་དུ་བྱས་པའོ། །

[Block 972]
ས་ལས་བྱས་པའི་སྣོད་བུམ་པའི་དབྱིབས་འདྲ་བ་གྱོ་མོག་གི་རྣམ་པ་ལྟ་བུའི་སྣོད་ཀྱི་ཚོགས་བྱ་སྟེ་སོ་བཏང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 973]
འདིར་བརྒྱའི་ཚིག་ནི་མང་པོ་ཉིད་དུ་བསྟན་པ་ཙམ་དུ་རྣམ་པར་གནས་པ་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 974]
སྐྲའི་རྙིས་སྦྲུལ་གཟུང་བར༌[^585]མི་བྱ་བ་ནི་འོ་ན་འདི་ཇི་ལྟར་བསལ་བར་བྱ་ཞེ་ན། དེའི་ཕྱིར་སེ་གོལ་གྱི་སྒྲ་ཕྱུང་སྟེ། བཞིན་བཟངས༌[^586]མིག་ལམ་ན་མ་འདུག་ཤིག༌[^587]ཅེས་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 975]
དེ་སྐད་བརྗོད་ཀྱང་མིག་ལམ་ན་འདུག་ན་དེའི་ཚེ་ཇི་ལྟར་བྱ་ཞེ་ན། དེའི་ཕྱིར་མི་འདུག་ན་དབྱུག་གུ་སྐམ་ཁས་དལ་བུ་དལ་བུས་རྫ་མའམ་བུམ་པར་བཅུག་སྟེ་ཁ་བཅད་ནས་བུ་ག་བཏོད༌[^588]དེ་བསལ་བར་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཁ་ཞེས་བྱ་བ་ནི་བུམ་པའམ་རྫ་མ་དེའོ། །

[Block 976]
མ་གྲུབ་ན་ལྕག་པོད༌[^589]དམ་ཤུར་བུ་ཕྲེའུ་འམ་ཐེ་གུ་རས་མས༌[^590]དཀྲིས་པས་ཞགས་མིག་གིས་མགུལ་པར་བཅིངས་ཏེ་དོར་བར་བྱའོ། །

[Block 977]
དེ་དག་ནི་གཞུག་པ་ཡང་ངོ༌[^591]ཞེས་བྱ་བ་ནི། ལྕག་པོད༌[^592]ལ་སོགས་པ་འདི་རྣམས་དོར་བ་འབའ་ཞིག་ལ་བྱ་བར་མ་ཟད་ཀྱི་བུམ་པ་ལ་སོགས་པ་ལ་གཞུག་པ་ལ་ཡང་བྱའོ། །

[Block 978]
ཚང་ཚིང་གི་ནང་དུ་དོར་བར་མི་བྱའོ་ཞེས་བྱ་བ་འདི་ནི་སྐྱེ་བ་བསལ་བའི་དོན་དུའོ། །

[Block 979]
ཁུང་དུ་ཞུགས་ཀྱི་བར་དུ་བསྡད་པར་བྱའོ་ཞེས་བྱ་བ་ནི། འདིར་བར་དུ་ཞེས་བྱ་བའི་སྒྲ་ནི་བཞག་པ་སྟེ། ཇི་སྲིད་ཁུང་དུ་ཞུགས་ཀྱི་བར་དུ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 980]
འོལ་བ་ལ་སོགས་པ་རྣམས་ཀྱིས་འདི་ལ་སྲོག་གཅོད་པར་མ་གྱུར་ཅིག་ཅེས་བྱ་བ་ནི་འདིར་དོན་ཏོ། །

[Block 981]
དེ་བས་ན་བླ་གབ༌[^593]མེད་པར་ནི་འདི་རྣམས་ལ་ནི་བྱེད་པ་པོ་སྟེ། ནགས་ལ་ནི་མ་ཡིན་ཞེས་བྱ་བ་དོན་གྱིས་རྟོགས་པར་བྱའོ། །

[Block 982]
ཤིག་རྣམས་ནི་རས་མར་གཞུག་པར་བྱའོ། །

[Block 983]
དེ་ནི་གསེབ་དག་ཏུའོ་ཞེས་བྱ་བ་ནི་རས་མ་དེ་ནི་ཀ་བ་ལ་སོགས་པའི་གསེབ་དག་ཏུ་གཞུག་པར་བྱའོ། །

[Block 984]
འདིར་གཞུང་ནི་རས་མའི་ནང་དུ་དཀྲིས་ཏེ་ཀ་བའི་གསེབ་བམ་རྩིག་པའི་གསེབ་དག་ཏུ་གཞུག་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 985]
རྩ༌[^594]ཤིག་རྣམས་ནི་བསིང་མར་རོ། །
--- END BLOCKS ---
