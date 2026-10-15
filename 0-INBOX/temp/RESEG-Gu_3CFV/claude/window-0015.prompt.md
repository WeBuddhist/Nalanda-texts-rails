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
[Block 526]
སྤངས་པ་ལ་སྟོབས་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 527]
ཤེས་གཙོ་བོ་ཞེས་བྱ་བ་ནི་འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་པོ་ཉིད་དོ། །གང་ལ་འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་པོ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་སོ་སོར་ངེས་པའི་ཟས་ཀྱི་གནས་ཅན་དག་ལས་གཞན་པའི་དགེ་སློང་དགེ་འདུན་དུ་གྱུར་པ་མཚམས་ཀྱི་ནང་ན་གནས་པ་དག་ཟན་ལྷན་ཅིག་མ་ཡིན་པ་ཉིད་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གནས་ཁང༌[^315]ན་ཟས་ཐ་དད་པ་ཉིད་དུ་ངེས་པ་དེ་ནི་སོ་སོར་ངེས་པའི་ཟས་སོ། །

[Block 528]
དགེ་སློང་གང་དག་ལ་གནས་དེ་དག་ནི་སོ་སོར་ངེས་པའི་ཟས་ཀྱི་གནས་ཅན་དག་གོ། །

[Block 529]
དེ་རྣམས་ལས་གཞན་དགེ་སློང་མཚམས་ཀྱི་ནང་ན་གནས་པའི་བཞི་ལ་སོགས་པ་དགེ་འདུན་དུ་གྱུར་པའི་དགེ་སློང་རྣམས་དང་ལྷན་ཅིག་མ་ཡིན་པ་ཉིད་ཀྱིས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 530]
འདིར་གཞུང་ནི་ཚོགས་ཤིང་ཟ་བ་བཟུང་བ་ནི་དགེ་འདུན་དུ་གྱུར་པ་རྣམས་ཀྱིས་ཞེས་བྱ་བ་རིག་པར་བྱའོ། །

[Block 531]
འདིར་རྣམ་པར་འབྱེད་པ་ལས༌[^316]ལ་གཡེང་བ་ཞེས་བྱ་བ་སྟེ། ཚོགས་ཤིང་ཟ་བ་ནི་ཚོགས་ནས་ཟ་བའོ། །

[Block 532]
གཡེང་བ་ཉིད་ཅེས་པ་ནི་དགེ་འདུན་གཉིས་འབྱེད་པའོ་ཞེས་བྱ་བ་འདིའི་དོན་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 533]
ཅི་གཅིག་པུ༌[^317]ཞིག་ཟན་ལྷན་ཅིག་མ་ཡིན་པ་ཉིད་ལ་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་ལྷན་ཅིག་པའི་འོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རྣམ་པ་གང་དང་ལྷན་ཅིག་པའི་ཞེ་ན། དེའི་ཕྱིར་ཅིག་ཅར་ཟ་བ་དང་ངོ་ཞེས་བྱ་བ་སྨོས་སོ། །སུ་དང་ལྷན་ཅིག་པའི་ཞེ་ན། དེའི་ཕྱིར་གསུམ་པོ་ལ་སོགས་པ་དང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ།

[Block 534]
གསུམ་པ་འམ་བཞི་ལ་སོགས་པའི་ཚོགས་དང་ངོ་། །འདིར་གཞུང་ནི་བཞི་པོ་དག་ལས་གཅིག་གིས་ཞལ་ཏ་བྱེད་ཅིང་གསུམ་ཟ་བ་ལ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །གང་གི་གསུམ་པོ་ལ་སོགས་པ་དང་ཞེ་ན། དེའི་ཕྱིར་དགེ་སློང་རྣམས་ཀྱིའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་གཞུང་ནི་ལྟུང་བ་བསྟན་པ་ལ་གསུམ་བསྙེན་པར་རྫོགས་པ་ཡིན་ལ་གཅིག་བསྙན་པར་མ་རྫོགས་པ་ཡིན་ན་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །ཅི་ཐམས་ཅད་དུ་ལྷན་ཅིག་པ་འདི་ཙམ་ལ་ཡང་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་དགེ་སློང་རྣམ་པ་ཇི་ལྟ་བུས་གོས་མེད་པའི་ཟས་གཉིས་པ་རྙེད་པ་བྱེད་པ་པོ་ཉིད་ཡིན་པ་བཞིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་སློང་རྣམ་པ་ཇི་ལྟ་བུ་གོས་མེད་པའི་ཟས་གཉིས་ཡང་ཡང་ཟ་བའི་བྱེད་པ་པོ་ཉིད་ཡིན་པ་དེ་བཞིན་དུ། འདིར་ཡང་མི་ན་བ་དང་ལས་མ་བྱས་པ་དང་ལམ་དུ་མ་ཞུགས་པ་དང་། གྲུར་མ་ཞུགས་པ་དེ་ལ་ཡང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 535]
ལམ་དཔག་ཚད་དམ་དཔག་ཚད་ཕྱེད་དུ་སོང་བའམ་སླར་འོང་བར་འགྱུར་ཞེས་བྱ་བ་འདི་ལ་ཁ་ཅིག་འགྲོ་བ་དང་སླར་འོང་བར་འགྱུར༌[^318]ཞེས་བྱ་བའི་གཞུང་བྱེད་པ་ཡིན་ཏེ། གཞན་དག་ནི་དཔག་ཚད་དུ་འགྲོ་བར་འགྱུར་བའམ་དཔག་ཚད་དུ་འགྲོ་བའམ། དཔག་ཚད་ཕྱེད་དུ་འགྲོ་བར་འགྱུར་བའམ་སླར་འོངས་པ་ཞེས་བྱ་བར་རྣམ་པར་རྟོག་པ༌[^319]ཡིན་ནོ། །

[Block 536]
འདི་གཉིས་ཀ་ཡང་བདེན་པ་མ་ཡིན་ཏེ། བཙུན་པ་རེ་ཞིག་དགེ་སློང་གི་དཔག་ཚད་ཕྱེད་ལས་འདས་པར་བགྱིས༌[^320]ནས་འདུས་པ་དང་ལྷན་ཅིག་འཚལ༌[^321]འཚལ་ན་ལྟུང་བ་ཅིར་འགྱུར་ཉེ་བ་འཁོར་ལྟུང་བ་མེད་དོ་ཞེས་ཞུ་བ་ལས་གསུངས་པ་ཡིན་ནོ། །ཅི་ཟན་ལྷན་ཅིག་མ་ཡིན་པ་ཉིད་ཐམས་ཅད་ལའམ་ཞེ་ན། དེའི་ཕྱིར་དུས་སྟོན་ཆེན་པོ་ལས་གཞན་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་དུས་སྟོན་ཆེན་པོ་ཞེས་བྱ་བའི་གཞུང་ནི་ཟན་སྤངས་པ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 537]
ཀུན་དུ་སྤྱོད་པ་གང་ལ་འདི་ལ་བྱེད་པ་པོ་ཉིད་ཅེས་བྱ་བ་འདི་ལ་ཟོས་ནའོ་ཞེས་འོག་ནས་འབྱུང་ན་ཅི་དུས་ལ་མ་བབ་པའི་བཟའ་བར་བྱ་བ་ཐམས་ཅད་ལ་ཟོས་ན་ཞེས་བྱ་བ་འདི་ལ་བརྗོད་པར་བྱ་སྟེ། དེའི་ཕྱིར་རྟགས་འདི་མེད་པའི་རབ་ཏུ་བྱུང་བའི་ཟས་ལས་གཞན་པའི་འོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རབ་ཏུ་བྱུང་བ་གང་ལ་རྟགས་འདི་མེད་པ་ཞེས་བྱ་བ་ནི་ཕྱི་རོལ་པའི་རབ་ཏུ་བྱུང་བའོ། །

[Block 538]
དེའི་ཟས་ལས་གཞན་པ་ཞེས་བྱ་བ་ནི་བཟའ་བར་བྱ་བ་གང་ཡིན་པ་དེ་ཟོས་པ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 539]
དེར་འོང་བར་བྱ་བ་ཉིད་དུ་གནས་པ་མཚམས་ཀྱི་ནང་ན་འཁོད་པ་དག་གི་འོང་པ་ཉིད་མ་དྲིས་པར་ཟ་ན་འདའ་བའི་ཕྱེད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། གནས་པ་ཞེས་བྱ་བ་ནི་རྣམ་པར་གནས་པ་སྟེ། གནས་གང་ལ་རྩ་བའི་གནས་ཡོངས་སུ་རྩི་བ་ལ་སོགས་པ་ལ་ཁ་ཅིག་ནི་ཟ་བར་བྱེད་པ་དེ། དེར་ཁ་ཟས་ཀྱི་དོན་དུ་འོངས་པ་ཉིད་གང་རྣམས་ལ་གནས་གཞན་དུ་རྩ་བའི་གནས་ཡོངས་སུ་བརྩི་བ་ལ་སོགས་པ་ལ་མཚམས་ཐ་མི་དད་པར་གནས་པ་རྣམས་ལ་དེ་རྣམས་ནི་དེ་གནས་པ་དང་དེར་འོངས་པ་ཉིད་རྣམས་སོ། །

[Block 540]
དེ་རྣམས་ལ་འོང་བ་ཉིད་མ་དྲིས་པར་ཟ་ན་འདའ་བའི༌[^322]ཕྱེད་ཡིན་ཏེ་ཉེས་བྱས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 541]
གནས་པ་ལ་མ་ཡིན་པར་དེར་འོང་བ་ཉིད་མ་དྲིས་པར་ཟ་ན་ལྟུང་བྱེད་ཁོ་ན་སྟེ། དེ་བས་ན་མ་བྱས་པ་ཉིད་ཀྱི་དམིགས་ཀྱིས་བསལ་བར་དེ་རྟོགས་པར་བྱའོ། །

[Block 542]
འདིར་གཞུང་ནི་གཞིའི་འདུག་གནས་ཀྱི་ཉེ་འཁོར་ན་ཁང་ཁྱིམ་དག་ཡོད་པ་གཞིའི་འདུག་གནས་སུ་དགེ་སློང་དག་ཟན་ཟ་ན་དེ་དག་གིས༌[^323]ཁང་ཁྱིམ་གྱི་འདུག་གནས་ནས་དགེ་སློང་དག་འོངས་སམ་ཞེས་དྲི་བར་བྱའོ། །

[Block 543]
མ་དྲིས་པར་ཟ་ན་གཞིའི༌[^324]འདུག་གནས་པ་དག་ལ་ནི་ཉེས་བྱས་སུ་འགྱུར་ལ། ཁང་ཁྱིམ་གྱི་འདུག་གནས་པ་དག་ལ་ནི་ལྟུང་བྱེད་དུ་འགྱུར་རོ། །

[Block 544]
དགེ་སློང་དག་ཁང་ཁྱིམ་གྱི་འདུག་གནས་སུ་ཟན་ཟ་ན། དེ་དག་གིས༌[^325]གཞིའི་འདུག་གནས་ནས་དགེ་འདུན་དག་འོངས་སམ་ཞེས་དྲི་བར་བྱའོ། །

[Block 545]
མ་དྲིས་པར་ཟོས་ན་ཁང་ཁྱིམ་གྱི་འདུག་གནས་པ་དག་ལ་ནི་ཉེས་བྱས་སུ་འགྱུར་ལ། གཞིའི་འདུག་གནས་པ་དག་ལ་ནི་ལྟུང་བྱེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 546]
དོགས་པར་གྱུར་པ་མ་དཔྱད་པར་ཞེས་བྱ་བའི་དོན་འདི་ལ་འདིར་མཚོན་པ་དང་མ་དྲིས་པར་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 547]
དོགས་པར་བྱ་བ་མ་བཟུང་བ་ཉིད་ཀྱི་ཕྱིར་དྲི་བར་བྱ་བ་མ་ཡིན་ཏེ། དེ་བས་ན་ངེས་པ་རྣམས་ལ་ནི་ཉི་མ་གཅིག་གི་དོན་ལ་ཡང་དགེ་འདུན་གྱི་སྐབས༌[^326]ན་སྨད་པ་ཉིད་དོ། །

[Block 548]
གཞན་དུ་ནི་ཁ་ན་མ་ཐོ་བ་ཡོངས་སུ་རྫོགས་པར་འགྱུར་རོ།[^327] །དེ་བས་ན་དེ་ལ་འདི་ནི་བྱེད་པ་པོ་ཡིན་ནོ། །

[Block 549]
དེ་ལྟར་ན་གནས་པ་གཅིག་ཡིན་ལ། དེ་ཉིད་ན་དགེ་སློང་གང་དག་སོ་སོ་ན་ཟན་ཟ་ཞིང་དེ་དག་གིས་ཀྱང་འདུས་ཤིང་ཟ་བར་མངོན་སུམ་དུ་ཤེས་སམ་དོགས་པ་དག་ཡོད་ན་དགེ་འདུན་གྱི་ལྷག་མ་ཐམས་ཅད་ལ་ཁོངས་སུ་གཏོགས་པའི་ཉེས་བྱས་བསྐྱེད་པ་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 550]
གང་ཡང་རུང་བ་ཅུང་ཟད་ཅིག་བྲིམས་ན་ཡང་ཟན་གཅིག་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཟན་བཟའ་བར་བྱ་བ་གང་ཡང་རུང་བ་ཅུང་ཟད་ཅིག་དགེ་འདུན་གྱིས་ལོགས་ཤིག་ན་ཟ་བའམ། ཟན་ལོགས་ཤིག་ན་ཟ་བ་བས་དགེ་འདུན་ལ་བྲིམས་ཀྱང་རུང་སྟེ་ལྟུང་བ་མེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 551]
འགྲོ་བར་ཆས་པ་དང་གློ་བུར་དུ་འོངས་པ་དང་ནད་པ་དང་ནད་གཡོག་དང་དགེ་སྐོས་ལས་གཞན་པ་ཐམས་ཅད་ཀྱིས་མ་ཟོས་པར་གཡོས་མལ་དང་སྤྱི་བུངས་ལས་མནོས་ཏེ་བཟའ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་སྨན་གྱི་གཞི་དང་ཕྲན་ཚེགས་དག་ལས་ཀྱང་མགྲོན་དུ་བོས་པ་ན་ཐམས་ཅད་ཀྱིས་མ་ཟོས་པ་བཟའ་བར་མི་བྱ་བ་ཉིད་དེ། དེ་བས་ན་དེར་ཡང་ཆོ་ག་འདི་རིག་པར་བྱའོ། །

[Block 552]
འདིར་ནི་དགེ་འདུན་གྱི་དོན་དུ་ཞེས་བྱ་བ་གསུངས་པ་མ་ཡིན་ཏེ། གཉིས་གང་ལ་ཡང་མ་ཡིན་ནོ། །

[Block 553]
གསུམ་བོས་པ་ལ་ཡང་གཅིག་པ་ཉིད་དེ་བོས་པ་ལ་ནི་ཁ་ཟས་གྱ་ནོམ་པ་ལ་རིགས་པའི༌[^328]ངོ་བོ་ཉིད་དོ། །

[Block 554]
དེ་བས་ན་འདིར་ཆོ་ག་འདི་མེད་པ་མ་ཡིན་ནོ། །

[Block 555]
གཙུག་ལག་ཁང་ན་དགེ་སློང་གཅིག་པུ་ཞིག་གནས་པ་ན་ཡང་དེས་ཀྱང་བཀད་ས་ལས་གཞན་དུ་ཟན་བཟའ་བར་མི་བྱ་སྟེ། ཟོས་ན་འདས་པར་འགྱུར་རོ། །

[Block 556]
དེས་ན་བསླབ་པའི་གཞི་འདིའོ། །

[Block 557]
གཅིག་པུ་ཞིག་མགྲོན་དུ་བོས་པར་འགྱུར་བ་དེས་ཀྱང་སྦྱིན་བདག༌[^329]གིས་བསྐོས་པའི་དབང་བ་མ་གཏོགས་པར་གང་ཞིག་མ་ཟོས་པར༌[^330]ཟན་དེ་ནི་འདི་ལས་འདའ་བར་རྗེས་སུ་བྱེད་པ་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 558]
མ་ཟོས་པ་ཉིད་ལ་ཞེས་བྱ་བ་ནི་ཚངས་པ་མཚུངས་པར་སྤྱོད་པ་དགེ་སློང་མ་ལ་སོགས་པ་གཅིག་ཏུ་འདུས་ནས་ཁ་ཟས་མི་མཐུན་པ་འདི་འཇུག་པ་དེ་ནི་བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་དོན་དུ་རྗེས་སུ་གནང་སྟེ། དགེ་སློང་འགའ་འོང་ཡང་སྲིད་པས་དེའི་ཆེད་དུ་གྲལ་གྱི་དང་པོར་སྟན་གཅིག་གཞག་སྟེ། ཁ་ཟས་ཀྱི་མདུན་དུ་དགེ་སློང་མ་རྣམས་བཀོད་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 559]
དེ་བས་ན་མཚན་མཐུན་པའི་ཚངས་པར་སྤྱོད་པ་དང་མཚུངས་པ་ལ་དོན་འདི་མི༌[^331]འཕངས་པར་ཤེས་པར་བྱའོ། །

[Block 560]
འདུས་ཤིང་ཟ་བའི་ལྟུང་བྱེད་དོ།། །།

[Block 561]
རང་གི་ཕྱེད་ཡོལ་ནས་སྐྱ་རེངས་འཆར་བའི་བར་དུས་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། རང་གི་ཞེས་བྱ་བ་ནི་ཕྱེད་ཡོལ་བ་དང་སྐྱ་རེངས་ཤར་གྱིས༌[^332]ཀྱང་འདི་ལ་འབྲེལ་པའོ། །

[Block 562]
རང་གི་ཕྱེད་ཡོལ་བའི་མཐར་ཐུག་པ་ལ་རང་གི༌[^333]སྐྱ་རེངས༌[^334]འབྱུང་བ་ལ་ཡང་བར་དུ་ཞེས་བྱ་བ་ནི་ཕྱེད་ཡོལ་མན་ཆད་ནས་སྐྱ་རེངས་འཆར་བའི་བར་གང་ཡིན་པ་དེ་ནི་འདིར་མངོན་པར་འདོད་པར་རིག་པར་བྱའོ། །

[Block 563]
འདིར་གཞུང་ནི་འཛམ་བུའི་གླིང་ལ་སོགས་པ་གནས་གང་ན་སོ་སོར་གནས་པ་དེ་ལ་རང་གི་ཞེས་བྱ་བར་འགྱུར་རོ། །

[Block 564]
དགེ་སློང་གིས༌[^335]དུས་མ་ལགས་པར་བཅའ་བར་བགྱི་བ་དང་བཟའ་བར་བགྱི་བ་འཚལ་བ་ལྟུང་བར་མི༌[^336]འགྱུར་བ་མཆིས་སམ། ཡོད་དེ་འཛམ་བུའི་གླིང་པའི་དུས་ཀྱིས་གླིང་གསུམ་པ་དག་ཏུ་ཟོས་ན་ལྟུང་བར་མི་འགྱུར་བའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ནོ། །

[Block 565]
དེ་ཉིད་ལ་ཤེས་གཙོ་བོ་ཞེས་བྱ་བ་ནི་དུས་མ་ཡིན་པ་དེ་ཉིད་ལ་འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་པོ་ཡིན་ནོ། །
--- END BLOCKS ---
