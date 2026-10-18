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
[Block 561]
དགེ་བ་ལ་ཡང་ལུས་ཀྱི་ལེགས་པར་སྤྱད་པའི་ཕྱོགས་སྦྱོར་བ་དང་མཇུག་དང་། མྱོས་པར་འགྱུར་བ་ལ་སོགས་པ་སྤོང་བ་དང་། སྦྱིན་པ་དང་། མཆོད་སྦྱིན་ལ་སོགས་པ་མ་བསྡུས་སོ། །

[Block 562]
ངག་གི་ལེགས་པར་སྤྱད་པའི་ཡང་སྙན་པར་སྨྲ་བ་ལ་སོགས་པ་མ་བསྡུས་སོ། །

[Block 563]
ཡིད་ཀྱི་ལེགས་པར་སྤྱད་པའི་ཡང་སེམས་པ་མ་བསྡུས་སོ། །

[Block 564 [HEADING]]
### ལས་ཀྱི་ལམ་རྣམ་པར་རིག་བྱེད་དང་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ། ^1-40-0

[Block 565]
ལས་ཀྱི་ལམ་དེ་རྣམས་ལས།

[Block 566]
མི་དགེ་དྲུག་ནི་རྣམ་རིག་མིན། །མི་དགེ་བའི་ལས་ཀྱི་ལམ་དྲུག་པོ་སྲོག་གཅོད་པ་དང་། མ་བྱིན་པར་ལེན་པ་དང་། བརྫུན་དུ་སྨྲ་བ་དང་། ཕྲ་མ་དང་ཚིག་རྩུབ་པོ་དང་། ངག་ཀྱལ་པ་རྣམས་ནི་གཞན་བྱེད་དུ་འཇུག་པ་ལ་དངོས་ཀྱི་རྣམ་པར་རིག་བྱེད་མེད་པའི་ཕྱིར་གདོན་མི་ཟ་བར་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པའི་རང་བཞིན་དག་ཡིན་ནོ། །

[Block 567]
གཅིག་རྣམ༌[^389]གཉིས་སོ། །

[Block 568]
འདོད་པས་ལོག་པར་གཡེམ་པ་དེ་ནི་བདག་ཉིད་ཀྱིས༌[^390]མཐར་ཕྱིན་པར་བྱེད་པ་ལ་ནི་དུས་དེའི་ཚེ་ཤི་ན༌[^391]རྣམ་པར་རིག་བྱེད་དང་། རྣམ་པར་རིག་བྱེད་མ་ཡིན་པའི་རང་བཞིན་ཡིན་ཏེ། དེ་གཞན་བྱེད་དུ་བཅུག་པ་ནི་དེ་དང་འདྲ་བར་དགའ་བ་མ་ཡིན་ནོ། །

[Block 569]
དེ་དག་ཀྱང་བྱེད་ན། ལས་ཀྱི་ལམ་དྲུག་པོ་དེ་དག་ཀྱང་བདག་ཉིད་བྱེད་པ་ལ་ནི་དུས་དེའི་ཚེ་ཤི་ན་རྣམ་པར་རིག་བྱེད་དང་། རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་དང་རྣམ་པ་གཉིས་སུ་འགྱུར་རོ། །

[Block 570]
ཕྱིས་ཤི་ན་ནི་རྣམ་པར་རིག་བྱེད་དང་རྣམ་པར་རིག་བྱེད༌[^392]མ་ཡིན་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 571]
དགེ་བའི་ལས་ཀྱི་ལམ་རྣམས་ལས་ནི། དགེ་བ་བདུན་རྣམ༌[^393]གཉིས། ཡང་དག་པར་བླངས་པའི་ཚུལ་ཁྲིམས་ནི་རྣམ་པར་རིག་བྱེད་ལ་རག་ལུས་པའི་ཕྱིར་ལས་ཀྱི་ལམ་གཟུགས་ཅན་བདུན་ནི་གདོན་མི་ཟ་བར་རྣམ་པར་རིག་བྱེད་དང་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་དང་རྣམ་པ་གཉི་ག་ཡིན་ནོ། །

[Block 572]
ཏིང་འཛིན་ལས་སྐྱེས་རྣམ་རིག་མིན། །བསམ་གཏན་དང་ཟག་པ་མེད་པའི་སྡོམ་པས་བསྡུས་པ་རྣམས་ནི་ཏིང་ངེ་འཛིན་ལས་སྐྱེས་པ་ཞེས་བྱ་སྟེ། དེ་དག་ནི་སེམས་ཙམ་ལ་རག་ལུས་པའི་ཕྱིར། རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 573]
ཉེར་བསྡོགས༌[^394]རྣམས་ནི་རྣམ་རིག་བྱེད། །ལས་ཀྱི་ལམ་ཉེར་བསྡོགས༌[^395]རྣམས་ནི་གདོན་མི་ཟ་བར་རྣམ་པར་རིག་བྱེད་ཀྱི་རང་བཞིན༌[^396]ཡིན་ནོ། །

[Block 574]
རྣམ་རིག་བྱེད་མིན་འགྱུར་བའམ། །མ་ཡིན། གལ་ཏེ་ཀུན་ནས་དཀྲིས་པ་དྲག་པོའམ། རབ་ཏུ་དང་བ་ལྷུར་ལེན་པ་ཆེན་པོས་སྦྱོར་བ་རྩོམ་པ༌[^397]རྣམ་པར་རིག་བྱེད་མ་ཡིན་པར་འགྱུར་གྱི། གཞན་དུ༌[^398]ནི་མ་ཡིན་ནོ། །

[Block 575]
བཟློག་པ་མཇུག༌[^399]ཡིན་ནོ། །

[Block 576]
ཉེར་བསྡོགས༌[^400]ལས་བཟློག་པ་ནི་ལས་ཀྱི་ལམ་རྣམས་ཀྱི་མཇུག་ཡིན་པར་བལྟ་བར་བྱ་སྟེ། དེ་དག་ནི་གདོན་མི་ཟ་བར་རྣམ་པར་རིག་བྱེད་ཀྱི་རང་བཞིན་ནི་མ་ཡིན་ནོ། །

[Block 577]
རྣམ་པར་རིག་བྱེད་དུ་ནི་འགྱུར་བའམ། ཡང་ན་མ་ཡིན་ཏེ། གལ་ཏེ་ལས་ཀྱི་ལམ་བྱས་ནས་དེའི་རྗེས་སུ་མཐུན་པའི་ཆོས་སྤྱོད་ན་ནི་རྣམ་པར་རིག་བྱེད་དུ་འགྱུར་གྱི། གཞན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 578 [HEADING]]
### སྦྱོར་བ་དང་དངོས་དང་མཇུག། ^1-41-0

[Block 579]
ཡང་ཇི་ཙམ་གྱིས་ན་སྦྱོར་བ་དང་དངོས་དང་མཇུག་འདི་དག་རྣམ་པར་བཞག་ཅེ་ན། འདི་ལྟར་རེ་ཞིག་འདི་ན་ཁ་ཅིག་ཕྱུགས་གསོད་པར་འདོད་ལ། ཁྲི་ལ་སོགས་པ་ལས་ལྡང་བར༌[^401]བྱེད། རིན་ལེན་པར་བྱེད། འགྲོ་བར་བྱེད། ནོམ་པར་བྱེད། ཕྱུགས་ཉོ་བར་བྱེད། འཁྲིད་པར་བྱེད། དྲན་པར་བྱེད། འཛུད་པར་བྱེད། གནོད་པར་བྱེད། མཚོན་ལེན་པར་བྱེད། མཚོན་ལན་གཅིག་གམ་ལན་གཉིས་འདེབས་པར་བྱེད་པ་ནས་ཇི་སྲིད་དུ་སྲོག་གཅོད་པར་མི་བྱེད་པ་དེ་སྲིད་དུ་ནི་སྦྱོར་བ་ཡིན་ནོ། །

[Block 580]
བསྣུན་པ་གང་གིས་སྲོག་གཅོད་པར་བྱེད་པ་དེའི་ཚེའི་རྣམ་པར་རིག་བྱེད་དང་། དེའི་སྐད་ཅིག་གི་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་གང་ཡིན་པ༌[^402]དེ་ནི་ལས་ཀྱི་ལམ་དངོས་ཡིན་ནོ། །

[Block 581]
རྒྱུ་གཉིས་ཀྱིས་ནི་སྲོག་གཅོད་པའི་ཁ་ན་མ་ཐོ་བས་རེག་པར་འགྱུར་ཏེ། སྦྱོར་བ་དང་འབྲས་བུ་ཡོངས་སུ་རྫོགས་པས་སོ། །

[Block 582]
དེ་ཕྱིན་ཆད་ཀྱི་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པའི་སྐད་ཅིག་མ་རྣམས་ནི་མཇུག་ཡིན་ནོ། །

[Block 583]
ཇི་སྲིད་དུ་ཕྱུགས་དེའི་པགས་པ་འཆུ་བའམ། བཀྲུ་བཤལ་བྱེད་པ་འམ། འཚོང་བའམ། འཚེད་པའམ། ཟ་བའམ་རྗེས་སུ་སྒྲོགས་པ་དེ་སྲིད་དུ་ནི་དེའི་རྣམ་པར་རིག་བྱེད་ཀྱི་སྐད་ཅིག་མ་དག་ཀྱང་མཇུག་ཡིན་ནོ། །

[Block 584]
དེ་བཞིན་དུ་གཞན་དྲུག་ལ་ཡང་ཅི་རིགས་པར་སྦྱར་བར་བྱའོ། །

[Block 585]
བརྣབ་སེམས་ལ་སོགས་པ་ནི་མངོན་དུ་གྱུར་པ་ཙམ་གྱིས་ལས་ཀྱི་ལམ་དུ་འགྱུར་བའི་ཕྱིར་སྦྱོར་བ་ཡང་མེད་ལ་མཇུག་ཀྱང་མེད་དོ། །

[Block 586]
འདིར་ཅི་རེ་ཞིག་སྲོག་ཆགས་དེ་འཆི་བའི་སྲིད་པ་ལ་གནས་པ་དེའི་ཚེ༌[^403]རྣམ་པར་རིག་བྱེད་དང་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་གང་དག༌[^404]ལས་ཀྱི་ལམ་ཡིན་ནམ་འོན་ཏེ་ཤི་བའི་སྲིད་པ་ལ་གནས་པ་དེའི་ཚེ༌[^405]ཡིན་པ༌[^406]ཞེས་བྱ་བ་འདི་བརྗོད་པར་བྱའོ། །

[Block 587]
དེ་ལས་ཅིར་འགྱུར། རེ་ཞིག་གལ་ཏེ་འཆི་བའི་སྲིད་པ་ལ་གནས་པ་ཡིན་ན་ནི་གསོད་པའམ། གསོད་དུ་འཇུག་པ་ལྷན་ཅིག་ཤི་བ་ཡང་སྲོག་གཅོད་པའི་ཁ་ན་མ་ཐོ་བ་དང་ལྡན་པར་འགྱུར་ཏེ། གྲུབ་པའི་མཐའ་ལས་ནི་དེ་སྐད་དུ་མི་འབྱུང་ངོ་། །འོན་ཏེ་ཤི་བ་ཡིན་ན་ནི་བསྣུན་པ་གང་གིས་སྲོག་གཅོད་པར་བྱེད་པ་དེའི་ཚེའི་རྣམ་པར་རིག་བྱེད་དང་། དེའི་སྐད་ཅིག་གི་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་གང་ཡིན་པ་དེ་ནི་ལས་ཀྱི་ལམ་དངོས་ཡིན་ནོ་ཞེས་གང་སྨྲས་པ་དེ་བརྗོད་པར་མི་བྱའོ། །

[Block 588]
གང་ཡང་བསྟན་བཅོས་ལས་འདི་སྐད་དུ། སྲོག་ཆགས་བསད་ལ་སྲོག་གཅོད་པ་མ་འགགས་པ༌[^407]ཡོད་དམ་ཞེ་ན། ཡོད་དེ། འདི་ལྟ་སྟེ། དཔེར་ན་སྲོག་ཆགས་ཀྱི་སྲོག་གཅོད༌[^408]ལ་སྦྱོར་བ་མེད་པར་མི་འགྱུར་བ༌[^409]ལྟ་བུའོ་ཞེས་གསུངས་པ་འདིར་མཇུག༌[^410]སྦྱོར་བའི་སྒྲར་གསུངས་སོ༌[^411]ཞེས་བྱ་བ་བྱེ་བྲག་ཏུ་སྨྲ་བའི་དོན་ནི་འགལ་ཏེ། དེའི་ཚེ་དངོས་ཁོ་ན་མ་འགགས་པའི་ཕྱིར་རོ། །

[Block 589]
ཇི་ལྟར་ཉེས་པ་མེད་པ་དེ་ལྟ་བུ་ཡིན་ནོ། །

[Block 590]
ཇི་ལྟར་ན་ཉེས་པ་མེད་པ་དེ༌[^412]དངོས་ཁོ་ན་སྦྱོར་བའི་སྒྲར་གསུངས་ཞེས་བྱ་བའོ། །

[Block 591]
འོ་ན་དེའི་ཚེ་རྣམ་པར་རིག་བྱེད་ཇི་ལྟར་ལས་ཀྱི་ལམ་དངོས་སུ་འགྱུར། ཇི་ལྟར་ན་མི་འགྱུར། མི་ནུས་པའི་ཕྱིར་རོ། །

[Block 592]
དེ་ནི་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པར་ཇི་ལྟར་འགྱུར་ཏེ། དེའི་ཕྱིར་སྦྱོར་བའི་འབྲས་བུ་ཡོངས་སུ་རྫོགས་པའི་ཚེ་གཉི་ག་ལས་ཀྱི་ལམ་ཡིན་ནོ། །

[Block 593]
ལས་ཀྱི་ལམ་གཞན་གྱི་སྦྱོར་བའམ་མཇུག༌[^413]ལས་ཀྱི་ལམ་གཞན་ཡིན་པ་ཡང་ཡོད་དམ་ཞེ་ན། ཡོད་དེ། སྲོག་གཅོད་པའི་སྦྱོར་བ་ལས་ཀྱི་ལམ་བཅུ་ཆར་ཡང༌[^414]ཡིན་ཏེ། དཔེར་ན་དགྲ་གསད་པའི༌[^415]ཕྱིར་གཤེད་བྱེད་གསད་པར༌[^416]གཞན་གྱི་ནོར་འཕྲོགས༌[^417]ནས་ཕྱུགས་ཀྱིས༌[^418]གཏོར་མ་བྱེད་པ་དང་། དེ་ཉིད་ཀྱིས་དེ་གསོད་དུ་གཞུག་པའི་ཕྱིར་དེའི་ཆུང་མ་ལ་ཉལ་པོ་བྱེད་པ་དང་། དེ་ལ་གང་དག་ཡོངས་སུ་སྐྱོབ་པར་འགྱུར་བ་དེའི་མཛའ་བོ་ལ་བརྫུན་དང་། ཕྲ་མ་དང་། ཚིག་རྩུབ་པོ་དང་། ཀྱལ་པ༌[^419]དག་གིས་དབྱེན་བྱེད་པ་དང་། དེའི་ནོར་ལ་བརྣབ་སེམས་བྱེད་པ་དང་། དེ་ཉིད་ལ་གནོད་སེམས་བྱེད་པ་དང་། དེ་གསད་པའི༌[^420]ཕྱིར་ལོག་པའི་ལྟ་བ་འཕེལ་བར་བྱེད་པ་ལྟ་བུ་སྟེ། དེ་བཞིན་དུ་གཞན་དག་ལ་ཡང་ཅི་རིགས་པར་སྦྱར་བར་བྱའོ། །

[Block 594]
བརྣབ་སེམས་ལ་སོགས་པ་ནི་སྦྱོར་བ་ཡིན་པར་མི་རུང་སྟེ། བྱ་བ་མ་བརྩམས་པའི་ཕྱིར་སེམས་བསྐྱེད་པ་ཙམ་གྱིས་ནི་སྦྱོར་བ་བྱས་པ་མ་ཡིན་ནོ། །

[Block 595 [HEADING]]
### མི་དགེ་བའི་ལས་ཀྱི་ལམ་རྩ་བ་གསུམ་ལས་སྐྱེས་པ། ^1-42-0

[Block 596]
མདོ་ལས་དགེ་སློང་དག་སྲོག་གཅོད་པ་ནི་རྣམ་པ་གསུམ་སྟེ། ཆགས་པ་ལས་སྐྱེས་པ་དང་། ཞེ་སྡང་ལས་སྐྱེས་པ་དང་། གཏི་མུག་ལས་སྐྱེས་པའོ་ཞེས་བྱ་བ་ནས་ལོག་པར་ལྟ་བའི་བར་དུ་གསུངས་པ་དེ་ལ་སྲོག་གཅོད་པ་ཆགས་པ་ལས་སྐྱེས་པ་ནི་ཅི་འདྲ་བ་ཞིག་ཅེས་བྱ་བ་དེ་ལ་སོགས་པ་བརྗོད་པར་བྱ་སྟེ། འདི་ལ་ལས་ཀྱི་ལམ་ཐམས་ཅད་ཆགས་པ་ལ་སོགས་པས་མཐར་ཕྱིན་པར་བྱེད་པ་ནི་མ་ཡིན་གྱི། སྦྱོར་བ་རྩ་བ་གསུམ་ལས༌[^421]སྐྱེས། །དེ་དག་གི་སྦྱོར་བ་ནི་མི་དགེ་བའི་རྩ་བ་གསུམ་ལས་སྐྱེས་པ་ཡིན་པས་ན་དང་པོ༌[^422]ཀུན་ནས་སློང་བའི་ཚིག་ལས་དེ་སྐད་བཤད་དོ། །

[Block 597]
དེ་ལ་སྲོག་གཅོད་པ་ཆགས་པ་ལས་སྐྱེས་པ་ནི་འདི་ལྟ་སྟེ། དེའི་ལུས༌[^423]ཀྱི་ཡན་ལག་གི་ཕྱིར་རམ། ནོར་གྱི་ཕྱིར་རམ། རྩེད་མོའི་ཕྱིར་རམ། བདག་གམ་མཛའ་བོ་ཡོངས་སུ་བསྐྱབ་པའི་ཕྱིར༌[^424]སྲོག་གཅོད་པར་བྱེད་པའོ། །

[Block 598]
ཞེ་སྡང་ལས་སྐྱེས་པ་ནི་འདི་ལྟ་སྟེ། ཁོན་ལས་ངེས་པར་འབྱུང་བར་བྱ་བའི་ཕྱིར་གསོད་པར་བྱེད་པའོ། །

[Block 599]
གཏི་མུག་ལས་སྐྱེས་པ་ནི་འདི་ལྟ་སྟེ། མཆོད་སྦྱིན་བྱེད་པ་རྣམས་དང་། རྒྱལ་པོས་ཆོས་འདོན་པ་ཚད་མར་བྱས་ནས་ཆོས་ཀྱི་བློས་གསོད་པ་དག་སྟེ། མི་བསྒྲུངས་པ་རྣམས་ཆད་པས་བཅད་ན། རྒྱལ་པོ་བསོད་ནམས་ཀྱི་སྣོད་དུ་འགྱུར་རོ་ཞེས་གྲགས་པ༌[^425]ལྟ་བུ་དང་། པར་སིག་པ་རྣམས་ཀྱི་ལྟ་བུ་སྟེ། དེ་དག་ནི་འདི་སྐད་དུ། ཕ་དང་མ་རྒས་སམ་ནད་ཚབས་ཆེན་པོས་ཐེབས་ན་གསད་པར༌[^426]བྱའོ་ཞེས་ཟེར་རོ། །

[Block 600]
གང་ཡང་འདི་སྐད་དུ་སྦྲུལ་དང་སྡིག་པ་དང་སྦྲང་བུ་ཏྲྱ༌[^427]མ་བུ་ཀ་ལ་སོགས་པ་རྣམས་ནི་མི་རྣམས་ལ་གདུང་བར་བྱེད་པ་ཡིན་པས་གསད་པར༌[^428]བྱའོ། །
--- END BLOCKS ---
