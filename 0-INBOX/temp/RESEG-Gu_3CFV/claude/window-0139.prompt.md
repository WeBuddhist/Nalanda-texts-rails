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
[Block 4866]
གཞི་འམ་གང་ཟག་གམ་གཉིས་ཀ་བཞག་ནས་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་དགག་དབྱེ་བྱར་རུང་སྟེ་གཞིའི་སྒྲས་ནི་ལྟུང་བ་ཞེས་སྨོས་སོ། །

[Block 4867]
ཕམ་པར་འགྱུར་བ་ལས་ལྟུང་བྱེད་ཀྱི་སྡེ་ཚན༌[^3426]གཞན་དུ་གཞག་པའོ། །

[Block 4868]
དེ་ལྟར་ཡང་འདིར་གཞུང་ནི། གལ་ཏེ་དགེ་འདུན་ལྷག་མ་ཤེས་ན་བྱིན་གྱིས་བརླབས་ཏེ་དགག་དབྱེ་བྱའོ། །

[Block 4869]
ཕམ་པར་འགྱུར་བར་ཤེས་ན་ནི་བསྙིལ་བར༌[^3427]གསུངས་པས་བསྙིལ༌[^3428]ཏེ་དགག་དབྱེ་བྱའོ། །

[Block 4870]
དེ་ལས་གཞན་པ་དག་ཤེས་ན་ནི་བཤགས་ཏེ་དགག་དབྱེ་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4871]
ཆེ་གེ་མོ་ལ་ལྟུང་བ་བཞག་ནས་དགག་དབྱེ་བྱའོ༌[^3429]ཞེས་བྱ་བ་ནི་གཞག་པ་ལ་རིམ་པས་སོ། །

[Block 4872]
འདིར་གང་ཟག་གང་དུ་གཏོགས་པ་འདི་ལ་ཅུང་ཟད་འཇུག་པར་འགྱུར་བ་དེ་ནི་རིགས་པ་ཡིན་ཏེ། དེ་བསྐུལ་བ་པོའམ་གཞན་ཡང་རུང་སྟེ། གང་ཟག་ལྷག་མ་ཡོད་མོད་ཀྱི་གཞན་ཐམས་ཅད་ལ་ནི་འཇུག་པའི་དབང་དུ་བྱ་སྟེ། དགག་དབྱེའོ་ཞེས་བྱ་བ་འདིར་གཞག་པའི་རིམ་པ་འདི་ཡིན་ནོ། །

[Block 4873]
གཉིས་ཀ་ཞེས་བྱ་བ་ནི་གཞི་དང་གང་ཟག་གཉིས་ཀའོ། །

[Block 4874]
དེ་དག་མནོད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་དེ་ལྟ་བུའི་རྣམ་པས་དགག་དབྱེ་བྱེད་པའོ། །

[Block 4875]
གཞག་པར་བྱ་བ༌[^3430]མཐའ་མ་གཏོགས་པ་ཉིད་ཁས་བླང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ཕམ་པར་འགྱུར་བ་འདིར་དང་པོར་ཞེས་གསུངས་པས་ཕམ་པར་འགྱུར་བ་དེ་ལས་གཞན་པ་གཞག་པར་བྱ་བ་ལ་ཁས་བླངས་ནས་མནོད་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །ཇི་ལྟར་ཁས་བླང་བར༌[^3431]བྱ་ཞེ་ན། དེའི་ཕྱིར་ཚེ་དང་ལྡན་པ་ཁོ་བོ་ཅག༌[^3432]ནི་ཚེ་དང་ལྡན་པ་ཅི་ནས་ཀྱང་གཞི་འཇོག་པར་བྱེད་ཅིང་གང་ཟག་འཇོག་པར་མི་བྱེད་པ། དེའི་དོན་དང་དོན་དུ་འདུས་ཤིང་འདུག་པ་མ་ཡིན་གྱི། འདི་ལྟར་བཅོམ་ལྡན་འདས་ཀྱིས་ཚུལ་ཁྲིམས་རྣམ་པར་དག་པར་བྱ་བའི་ཕྱིར་ནི་གསོ་སྦྱོང་གསུངས་ལ། ཆོས་རྣམ་པར་དག་པར་བྱ་བའི་ཕྱིར་ནི་དགག་དབྱེ་གསུངས་པས་གལ་ཏེ་འདོད་ན་དགག་དབྱེ་གྱིས་ཤིག་ཅེས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། །འོ་ན་དེང་ཞེས་བྱ་བ་ནི་འདིར་གཞག་པ་ལ་དགོས་པ་མེད་དེ། །འོན་ཀྱང་ཁྱོད་རྣམ་པར་དག་པར་བྱ་བའི་དགོས་པ༌[^3433]ཡོད་པས། གལ་ཏེ་དེ་སྙམ་དུ་སེམས་ན་བདག་ལ་ཡང་དག་པ་ཉིད་འདོན་པར༌[^3434]མི་བྱ་བ་མེད་དེ། དེ་དགག་དབྱེ་གྱིས་ཤིག་ཅེས་བྱ་བའི་དོན་ཤེས་པར་བྱའོ། །

[Block 4876]
དེ་ལ་བདག་ཅག་གཞག་པ་ལ་དགོས་པ་མེད་དེ། དེ་མེད་པར་གལ་ཏེ་དགག་དབྱེ་བྱེད་ན། དགག་དབྱེ་གྱིས་ཤིག་ཅེས་བྱའོ། །

[Block 4877]
ཆོས་རྣམ་པར་དག་པར་བྱ་བའི་ཕྱིར་ཞེས་བྱ་བ་ནི་ཁ་ན་མ་ཐོ་བ་མེད་པ་ཙམ་ནི་གསོ་སྦྱོང་གི་རྣམ་པར་དག་པའོ། །

[Block 4878]
འདི་ནི་ཅང་ཤེས་ཉིད་ཀྱང་ཡང་དག་པར་ཞུགས་པ༌[^3435]ཉིད་ལ་བསྐུལ་བ་དང་། གདམས་ངག་དང་རྗེས་སུ་བསྟན་པ་རྣམས་དང་། ས་དང་སེམས་ལས་བྱུང་བ་རྣམས་ལས༌[^3436]ཁྱད་པར་དུ་འཕགས་པ་ཉིད་ཅེས་བྱ་བ་དེ་ལྟར་བརྗོད་པའི་ཚིག་གོ། །

[Block 4879]
ཆོས་རྣམ་པར་དག་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི། འདིར་འདོན་པ་གཞན་དེ་འདིར་དོན་ནི་དེ་ཉིད་དོ། །

[Block 4880]
གང་ཟག་འཇོག་པར་བྱེད་ཅིང་གཞི་འཇོག་པར་མི་བྱེད་པ་དང་། གཞི་ཡང་འཇོག་པར་བྱེད་ཅིང་གང་ཟག་ཀྱང་འཇོག་པར་བྱེད་པའིའོ་ཞེས་བྱ་བ་ནི་འོན་ཀྱང་ཚེ་དང་ལྡན་པ༌[^3437]ཅི་ནས་ཀྱང་དེའི་དོན་དུ་འདུས་ཤིང་འདུག་པ་མ་ཡིན་གྱི། ཚེ་དང་ལྡན་པ་འགའ་ཞིག་ལ་གང་ཟག་འཇོག་པར་བྱེད་ཅིང་གཞི་མི་འཇོག་པ་དང་། ཚུལ་ཁྲིམས་རྣམ་པར་དག་པར་བྱ་བའི་ཕྱིར་ཞེས་བྱ་བ་ནི་ཚིག་དང་པོའོ། །

[Block 4881]
གཞན་ནི་འོན་ཀྱང་ཚེ་དང་ལྡན་པ་འགའ་ཞིག་གཞི་ཡང་འཇོག་པར་བྱེད་ཅིང་གང་ཟག་ཀྱང་འཇོག་པར༌[^3438]བྱེད་དེ། འོན་ཀྱང་ཚུལ་ཁྲིམས་རྣམ་པར་དག་པར་བྱ་བའི་ཕྱིར་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ནོ། །

[Block 4882]
ཁས་བླངས་པ་ཉིད་ནི་གཞག་པའམ། གཞག་པ་བསྙོན་པས་ནི་ཁས་བླངས་པ་ཉམས་པར་མི་འགྱུར་རོ་ཞེས་བྱ་བ་ནི། དགག་དབྱེ་བྱེད་པར་ཁས་བླངས་པ་ལ་གལ་ཏེ་གཞག་པའམ་གཞག་པ་སྙོན༌[^3439]པར་བྱེད་པ་དེ་བདག་གིས༌[^3440]གཞག་པ་ཉིད༌[^3441]མ་བྱས་ཏེ། ཅུང་ཟད་ཀྱང་མ་བཞག་གོ་ཞེའམ། ཡང་ན་གཞག་སྟེ་བདག་གིས་འདི་མ་བཞག་གི་གཞན་གཞག་གོ་ཞེས་བསྙོན་ན། དེ་གཉིས་ཀ༌[^3442]ལྟར་ཡང་དགག་དབྱེ་ཁས་བླངས་པ་གང་ཡིན་པ་དེ་དག་ཉམས་པར་མི་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4883]
དེ་ལ་སྔ་མའམ་འདིའི་རྣམ་པ་དེ་ལྟ་བུ་ཅུང་ཟད་ཀྱང་མེད་དོ་ཞེས་ཟེར་ན་བརྫུན་ཉིད་དོ་ཞེས་བྱ་བ་ནི་གཞག་པ་སྔ་མ་ལ་དེ་ལྟར་བརྗོད་པ་ལ་གཞག་པ་འདི་ལ་ཡང་བརྫུན་ཉིད་དུ་ཤེས་པར་མི་བྱའོ། །

[Block 4884]
དེ་ལྟ་བུའི་ཆས༌[^3443]སྨོས་པ་དེ་ནི་བརྫུན་དུ་སྨྲ་བ་ཉིད་ཅེས་བྱ་བའམ། བརྫུན་དུ་སྨྲ་བའི་རབ་ཏུ་དབྱེ་བ་ཐེ་ཚོམ་བཟློག་པར་བྱ་བའི་དོན་ཏེ། དེ་འདི་ཞེས་བྱ་བར་ཡུལ་བསྟན་པའོ། །

[Block 4885]
སྔར་བསྟན་མ་ཐག་པའི་བསྙོན་པ་དེ་ལ་འཇུག་པ་ཞེས་བྱ་བའོ། །

[Block 4886]
གལ་ཏེ་གནས་པར་ཁས་བླངས་པ་དག་གིས་དགེ་སློང་འཐབ་ཀྲོལ་བྱེད་པ་དག་འོང་བར་ཐོས་པར་གྱུར་ན་གལ་ཏེ་གསོ་སྦྱོང་གཉིས་སམ་གསུམ་ཐལ་བར་གྱུར་ན༌[^3444]དགག་དབྱེ་བྱའོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་དེའི་ཚེ་ཁས་བླངས་པའི་ཚེ། གལ་ཏེ་གསོ་སྦྱོང་གཉིས་སམ་གསུམ་ཐལ་བར་གྱུར་པ་ཉིད་དུ་ཤེས་ན། དབྱར་གྱི་ནང་དུ་དགག་དབྱེ་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4887]
ཐམས་ཅད་ལ་ཡང་ཕྱེད༌[^3445]བྱས་པ་ནི་བྱས་པ་ཉིད་ཡིན་ནོ་ཞེས་འཇིག་རྟེན་པའི་གྲགས་པ་ཡིན་ལ། གང་ཞིག་ཕལ་ཆེར་བྱས་པ་ནི་བྱས་པ་ཉིད་ཡིན་ནོ་ཞེས་གྲགས་པའི་གྲགས་པ་ཡིན་པས་འདིར་ཡང་འདིའམ་གཞན་དུ་ལྟུང་བ་ལའོ། །

[Block 4888]
དེ་མེད་པ་ལ་སྔར་གྱི་ཉིད་ལ་བརྟེན་པར་རིག་པར་བྱ་བ་འདིས་གྲགས་པའི་དོན་དུ་རྣམ་པར་རྟོག་པའོ། །

[Block 4889]
འདི་ལ་ཚེས་བཅོ་ལྔ་སྨོས་པ་ལ་གཉིས་པ་དང་གསུམ་པ་འདའ་བར་བྱེད་པ་ལ་ལྟོས་པ་ཉིད་དེ། དེའི་ཚེ་དགག་དབྱེ་བྱ་བ་ཉིད་ཀྱི༌[^3446]ཕྱིར་དེ་ལྟ་བས་ན་དེ་ཉིད་འདའ་བར་བྱེད་པ་ཉིད་དུ་ཤེས་པར་བྱའོ། །

[Block 4890]
མ་གྲུབ་ན་དཀྱིལ་འཁོར་པ་ལྔའམ་དྲུག་ཏུ་བློ་མཐུན་པར་རོ་ཞེས་བྱ་བ་ནི་འདའ་བར་མ་གྱུར་ཏམ༌[^3447]བར་ཆད་ཀྱི་རྐྱེན་གཞན་གྱི་དབང་གིས་མ་གྲུབ་ན་འདིར་དགག་དབྱེ་དཀྱིལ་འཁོར་བ་ལྔ་འམ། དྲུག་ཏུ་བློ་མཐུན་པས་ཡང་དག་པར་ཤེས་པར་བྱའོ། །

[Block 4891]
ངག་གིས་བཤེས་པའི་ཚིག་གིས་བསུ་ནས་ལྷུང་བཟེད་དང་ཆོས་གོས་བླང་བ་དང་། གནས་ཁང་དང་ཁྱམས་དང་ཁང་པ་བརྩེགས་པ་བསྐོ་བ་དང་། ཁྲུས་དང་སྣུམ་བག་གི་རྙེད་པ་བསྟབས་པ༌[^3448]དང་། ཆོས་མཉན་པ་སྦྱིན་པ་དང་། དེ་ལྟ་བུ་མགུ་བར་བྱ་བ་དག་བྱའོ་ཞེས་བྱ་བ་ནི། སྐབས་དེར་འཐབ་ཀྲོལ་བྱེད་པ་དག་འོངས་ན། དེ་དག་ལ་ངག་གིས་བཤེས་པའི་ཚིག་གིས་བསུ་ནས་ལྷུང་བཟེད་དང་། ཆོས་གོས་བླང་བར་བྱ། གནས་ཁང་སྐྱོང་བས་གནས་ཁང་དང་ཁྱམས་དང་ཁང་པ་བརྩེགས་པ་བསྐོ་བར་བྱ། ཁྲུས་དང་སྣུམ་བག་གི་རྙེད་པ་བསྟབས་པར་བྱ། །ཆོས་མཉན་པ་སྦྱིན་པར་བྱ་ཞིང་གལ་ཏེ་དེ་སྲིད་དུ་ནུས་ན་དེ་ལྟ་བུ་ལ་སོགས་པའི་བཅོམ་གསག༌[^3449]མགུ་བར་འགྱུར་བའི་སྦྱོར་བ་གཞན་དག་ཀྱང་དེ་ལྟ་བུའི་མཁས་པས་ཞེས་བྱ་བ་དེ་ལྟ་བུའི་འདོན་པ་ལ་ཀུན་ནས་བརྟེན་ནས་འདིར་མདོར་བྱས་སོ། །

[Block 4892]
འདིར་ཁྲུས་འདི་ལ་འདོན་པ་གཞན་ལས་སྦྱར་བ་ལས༌[^3450]འཇུག་པ་ཉིད་ལ་ཀུན་ནས་བརྟེན་ནོ། །

[Block 4893]
བདག་ཉིད་ཀྱི་དངོས་པོར་མ་གྲུབ་ན་དཀྱིལ་འཁོར་བ་དག་ཏུ་གསོ་སྦྱོང་བྱའོ། །

[Block 4894]
འོ་ན་དེང་ཁྱེད་ཀྱིས་དགག་དབྱེ་མ་ཡིན་ནམ་ཞེས་ཟེར་བ་དག་ལ་ཚེ་དང་ལྡན་པ་དག་སྡོད་ཅིག །ཁྱེད་ཅག་གློ་བུར་དུ་ལྷགས་པ་ཡིན་གྱི།[^3451] དོན་འདི་གཉུག་མར་གནས་པ་དག་གི་ཡིན་ནོ་ཞེས་ལན་གདབ་པར་བྱའོ། །

[Block 4895]
དོང་བ་དག་ན་དགག་དབྱེ་བྱའོ་ཞེས་བྱ་བ་ནི་བྱའོ་ཞེས་བྱ་བའི་ཁྱད་པར་རོ། །

[Block 4896]
གསོ་སྦྱོང་གི་ཉི་མ་ཁོ་ན་ལ་འདི་ཉིད་བྱའོ། །

[Block 4897]
ཐ་དད་པ་ཡོད་ཀྱང་ལས་འདི་ལ༌[^3452]གསོ་སྦྱོང་རིགས་མཐུན་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 4898]
དགག་དབྱེའི་གཞིའོ།། །།

[Block 4899]
ནང་དང་བཅས་པས་བཟོད་པར་མ་བྱས་པར༌[^3453]དགག་དབྱེ་མི་བྱའོ་ཞེས་བྱ་བ་ལ། འདིས༌[^3454]ནི་བཟོད་པར་མ་བྱས་པ་ཞེས་བྱ་བ་སྟེ། བཟོད་པ་མ་བྱས་པའོ། །

[Block 4900]
ནང་དང་བཅས་པ་ཞེས་བྱ་བ་ནི་ཐམས་ཅད་ཀྱིས་ནི་མ་ཡིན་ནོ། །

[Block 4901]
ཞག་བཅུའམ་ཟླ་བ་ཕྱེད་ཀྱིས་དེ་འབྱུང་བར་འགྱུར་བ་ཉིད་ནི་དེའི་དུས་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བ་ནི་དགག་དབྱེ་དེའོ། །

[Block 4902]
དེའི་དུས་ཞེས་བྱ་བ་ནི་དེ་ལ་སྨོས་པའི་བཟོད་པར་བྱ་བ་དེའི་དུས་ཡིན་ནོ། །

[Block 4903]
ཁ་ཅིག་ལས་ནི་བདུན་ནམ་བརྒྱད་ན་ཞེས་བྱ་བ་ནི། ཉི་མ་བདུན་ནམ་བརྒྱད་ཀྱིས་དེ་འབྱུང་བར་འགྱུར་བ་ཉིད་ཀྱི་དུས་ན་དགག་དབྱེ་དེ་ལ་བཟོད་པར་བྱ་བ་དེའི་དུས་ཡིན་ནོ་ཞེས་ཁ་ཅིག་ལས་འབྱུང་ངོ་། །འདུས་པ་ལ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། དེའི་ཚེ་འདུས༌[^3455]ཞེས་བྱ་བར་སྦྱར་ཏེ། འདིར་དགག་དབྱེའི་དོན་དུ་འདོན་པ་ཡིན་མོད་ཀྱི་འདུས་པ་གཞན་ལ་ཡང་དེ་བཞིན་དུ་འདི་རིགས་པ་མ་ཡིན་ནོ། །

[Block 4904]
དེའི་ཕྱིར་འདིར་བྱེ་བྲག་ཏུ་མ་བྱས་སོ། །

[Block 4905]
དེས་བཟོད་པར༌[^3456]མ་བྱས་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ནང་དང་བཅས་པ་དེས་བཟོད་པར༌[^3457]མ་བྱས་པར་དགག་དབྱེ་མི་བྱའོ། །
--- END BLOCKS ---
