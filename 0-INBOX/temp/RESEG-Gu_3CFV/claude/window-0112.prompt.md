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
[Block 3921]
གཞུང་ཁ་ཅིག་ལས་དེ་དག་དེར་མི་ཤོང་ནས་སྟེང་དུ་རིམ་ཁང་གཉིས་པ་བྱའོ་ཞེས་གསུངས་པ་དང་། དེ་གཉིས་ཀ་ཡང་འགལ་བ་མེད་པས་མདོ་འདིར་བསྡུས་པའོ། །

[Block 3922]
འཛེག་པའི་ཕྱིར་ཐེམ༌[^2699]སྐས་སོ་ཞེས་བྱ་བ་ནི། བྱའོ་ཞེས་བྱ་བར༌[^2700]སྦྱར་ཏེ་འཛེག་པའི་ཕྱིར་དེར་ཐེམ༌[^2701]སྐས་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3923]
མི་ལྟུང་བར་བྱ་བའི་ཕྱིར་ཁ་ཁྱེར་གྱིས་བསྐོར་བར་བྱའོ། །

[Block 3924]
དེ་མི་འགུལ་བར་བྱ་བའི་ཕྱིར་ལྕགས་ཀྱི་གཟེར་བུ་དག་གིས་གདབ་བོ་ཞེས་བྱ་བ་ནི། དེ་རྣམས་ཀྱིས་ནི་ཁ་ཁྱེར་དེ་དག་ལ༌[^2702]འཛེག་དཀའ་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ཐེམ༌[^2703]སྐས་བྱའོ། །

[Block 3925]
ལྟུང་བར་གྱུར་ནས། [^2704]ཁ་ཁྱེར་གྱིས༌[^2705]བསྐོར་བར་བྱའོ། །

[Block 3926]
དེ་འགུལ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ལྕགས་ཀྱི་གཟེར་བུ་དག་གིས་གདབ་པར་བྱའོ་ཞེས་གསུངས་པ་དེ་འདིས་བསྡུས་པ་ཡིན་ནོ། །

[Block 3927]
ཕྱི་རོལ་དུ་སྤོང་ཁང་ཆེན་པོའམ་གནས་ཁང་གི་ཚར་དག་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི། བྱའོ་ཞེས་བྱ་བའི་རྗེས་བསྙེག༌[^2706]པའི་ཕྱིར་ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲ་སྨོས་སོ། །

[Block 3928]
འདིར་ཡང་ངམ་ཞེས་བྱ་བའི་སྒྲ་ནི་ཚིག་གཉིས་ཀ་ཡང་བསྡུས་པའི་ཕྱིར་རོ། །

[Block 3929]
རབ༌[^2707]ཏུ་བྱུང་བ་འདི་ནི་ཕན་ཚུན་མི་སྣང་བའི་ཕྱིར་ནི་མ་ཡིན་ཏེ། གནས་ཁང་གི་ཚར་དག་ཀྱང་ཞེས་བྱ་བ་དེ་ཡང་། སྔར་ལྟར་ཚིག་གཉིས་ཀ་བསྡུ་བའི་ཕྱིར་ཀྱང་གི་སྒྲ་སྨོས་སོ། །

[Block 3930]
སྒོའི་ཐད་ཀར་སྒོ་གདོད་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལས།

[Block 3931]
འདིས་ནི་དེ་དག་ཉན༌[^2708]དུ་འགྱུར་བའི༌[^2709]སྒོ་དག་གདོད༌[^2710]ཅིང་ཕན་ཚུན་སྣང་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། སྒོ་དག་གཟུར་ཏེ་གདོད་པར་བྱའོ་ཞེས་གསུངས་པ་དེ་བསྡུས་པ་ཡིན་ནོ། །

[Block 3932]
གལ་ཏེ་ཕྱི་རོལ་གྱི་ཚར༌[^2711]གྱིས་དེ་མ་ཐག་པ་དེ་སྨོས་པ་ཡིན་ནོ། །

[Block 3933]
དེ་ལྟར་ཡང་ནང་དུ་ཉེས་པ་མི་འགྲུབ་པ་ཡིན་ནོ། །

[Block 3934]
དེ་ལྟ་བས་ན་དེ༌[^2712]འདི་ལས་ཐ་དད་པར་གྱུར་པ་གཉིས་ཀ་ལ་འགྲོ་བའི་ཚིག་ཏུ་གཏོགས་པར་བྱའོ། །

[Block 3935]
སྒོ་ཁང་བྱའོ་ཞེས་བྱ་བ་ནི། སྤོང་ཁང་ལ་སྒོ་ཁང་བྱའོ། །

[Block 3936]
ཕུག་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི། སྤོང་ཁང་གི་ཉེན་འཁོར༌[^2713]དུ་ཞེས་བྱ་བས་དེ་དག་འབྲེལ་པའི་ཆོ་ག་རྣམ་པར་བསྟན་པའི་སྐབས་ནས་ཤེས་པར་བྱའོ། །

[Block 3937]
འདུག་པའི་ཆེད་དུ་སའི་སྟེགས་བུ་དག་དང་ཁྲིའུ་ཡང་བྱའོ༌[^2714]ཞེས་བྱ་བ་ནི་བྱའོ་ཞེས་བྱ་བ་འདི་གཉིས་ཀ་ལ་སྦྱར་རོ། །

[Block 3938]
དེའི་ཁོ་ར་ཁོར་ཡུག་ཏུ་ཁྲུ་བཞིས་འཁོར་བ་བཟང་ངོ་ཞེས་བྱ་བ་ནི། གྲུ་བཞི་པོའི་ངོས་རེ་རེ་ལ་ཁྲུ་གང་པའི་ཚད་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3939]
ཐགས་མ་ནི་རྣམ་པ་ལྔའོ་ཞེས་བྱ་བ་ནི། ཁྲིའུའི་སྟེང་དུའོ། །

[Block 3940]
མུན་ཛའི་དང་། ཤ་ནའི་དང་། གྲེས་མའི་དང་། རས་མའི་དང་། སྦ་ཕྲ་མོའིའོ་ཞེས་བྱ་བ་ནི། རུང་བར་གྲགས་པའི་ཕྱིར། དེ་རྣམས་ཉིད་དུ་གྲགས་པར་ཤེས་པར་བྱའོ། །

[Block 3941]
དེའི་ཐ་གུ་ལ་སོགས་པ་བཀག་པ་ནི་མ་ཡིན་པར་ཤེས་པར་བྱའོ། །

[Block 3942]
ཐགས་མ་དག་ཐ་གུ་དམས་པས་སྒྲོགས་པ་ལ། དེར་སྟན་ནང་ཚངས་ཅན་དག་གདིང་ངོ་ཞེས་བྱ་བ་ལ། དེར་ཞེས་བྱ་བ་ནི་ཁྲིའུ་ལའོ། །

[Block 3943]
དེའི་ཁོ་ར་ཁོར་ཡུག་ཏུ་མཐོ་གང་ལྷག་པ་ཉིད་བཟང་ངོ་ཞེས་བྱ་བ་ནི། ཁྲིའུ་དེའི༌[^2715]ཁོ་ར་ཁོར་ཡུག་ཏུ་སྟན་ནང་ཚངས་ཅན་དེའི་ཐ་མ་མཐོ་རེ་རེ་ལྷག་ན་བཟང་བ་སྟེ། དེ་ལྟར་འདུག་པ་ལ་སོགས་པ་ལ་ཁྲིའུ་དེ་མི་གནོད་ཅིང་སྟན་ནང་ཚངས་ཅན་དེའི་ཐ་མའི་རིག་པར༌[^2716]འགྱུར་བ་དེ་ལྟ་བས་ན་རྫས་སྲིད་དུ་ཁྲུ་བཞི་པ་ཞིང་དུ་ཁྲུ་དོ་ཡོད་པ་ཉིས་ལྟབ་ཏུ་བྱས་ཏེ་བཙེམ་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3944]
ཨརྐའི༌[^2717]དང་། ཀ་ཤི་དང་། ཨེ་ར༌[^2718]ཀའི་དང་། སྲ་བའི༌[^2719]དང་། ཤ་མ་ལ་དག་གི༌[^2720]བལ་གྱིས་དགང་ངོ་། །བལ་དང་། ཤ་ན་དང་། རས་བལ་དང་། རས་མ་དག་དང་། ལོ་མའི་ཚོགས་དག་གིས་ཀྱང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་རུང་བར་གྲགས་པ་བསྟན་པའི་ཕྱིར་དེ་དག་སྨོས་པར་མ་ཟད་ཀྱི།[^2721] བཟང་པོའི་སྒྲ་འཇུག་པ་ཡིན་ནོ། །

[Block 3945]
དོན་ཇི་ལྟ་བ་བཞིན་དུ་འདུག་པར་བྱ་བའི་ཕྱིར་མདོ་མདོར་བྱ་རོག་རྐང་དག་བྱའོ་ཞེས་བྱ་བ་ལ། དོན་ཇི་ལྟ་བ་བཞིན་དུ་ཞེས་བྱ་བ་ནི། ཐམས་ཅད་དུ་ཁོད་སྙོམས་པར་འགྱུར་བ་འདི་ནི་འདིར་དོན་ཏོ། །

[Block 3946]
དེ་ཇི་ལྟ་བ་བཞིན་དུ་སྒྲུབ་པ་དེ་ལྟར་གནས་པའི་ཕྱིར་སྟན་ནང་ཚངས་ཅན་གྱི་ཕྱོགས་ཐམས་ཅད་དུ་སྙོམས་པར་ཁྱབ་ཅིང་། གཞན་དུ་མི་འཇུག་པར་བྱ་བའི་ཕྱིར་བྱ་རོག་གི་རྐང་པ༌[^2722]འདྲ་བ་དག་གིས་གཟུངས་གདབ་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3947]
བསྒོམ་པ་ན་གཉིད༌[^2723]ཀྱི་གནོད་པ་བསལ་བར་བྱ་བའི་ཕྱིར། གཉིད་བྲོ་ན་གདོས་བུ་གདགས་པར་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཤིང་བལ་ལ་སོགས་པ་ལས་བྱས་པའི་གདོས་བུ་ཆུང་ངུའི་ཚད་དེ་ལུང་མིག་ནས་སྐུད་པ་བཏགས་ཏེ། བསམ་གཏན་པ་རྣམས་གཉིད་བྲོ་ན་གདོས་བུ་དེ་རང་གི་རྣ་བ་ལ་བཏགས་ཏེ་སྤྱད་པར༌[^2724]བྱའོ། །

[Block 3948]
འདིར་གཞུང་ནི། གཉིད་བྲོ་ན་གདོས་བུ་གདགས་པར་བྱའོ། །

[Block 3949]
དེ་ལྷུང་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། སྐུད་པས་བཅིངས་ཏེ་རྣ་བ་ལ་བཏགས་ཤིང་བཅང་བར༌[^2725]བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3950]
དབྱུ༌[^2726]གུ་དལ་བུས་གཟུགས་པར་བྱའོ་ཞེས་བྱ་བ་ནི། དེའི་བསམ་གཏན་ཉིད་འགྲོགས་པར་མི་འགྱུར་བ་དེ་ལྟར་དལ་བུས་གཟུགས་པར་བྱའོ་ཞེས་སྨོས་སོ། །

[Block 3951]
འདི་ནི་སྤོང་བའི་ཞལ་ཏ་བའི་ལས་ཡིན་ཏེ། དེས་དབྱུག་གུ་དལ་བུས་བཙུགས་པ་དེས་དེའི་གཉིད་སད་པར༌[^2727]འགྱུར་རོ། །

[Block 3952]
གནོད་པར་མི་འགྱུར་བར་བྱ་བའི་ཕྱིར་བྲེའི་བཅད་འཕྲོ་ལྟ་བུར་རས་མ་དག་གིས་དཀྲིས་པས་སོ་ཞེས་བྱ་བ་ལས།

[Block 3953]
བྲེའི་བཅད་འཕྲོ་ལྟ་བུ་ཞེས་བྱ་བ་ནི། བྲེའི༌[^2728]བཅད་འཕྲོ་ལྟར་འདི་ལ་བཅད་པ་ཡོད་པས་ན་ཞེས་བྱ་བའི་བསྡུ་བའོ། །

[Block 3954]
རས་མ་དག་གིས་དཀྲིས་པ་གང་ཡིན་པ་དེ་ནི་སྡུག་བསྔལ་གྱིས་འབྱུང་བར་བྱ་བའི་ཕྱིར་བསྟན་པ་ཁོ་ནའོ། །

[Block 3955]
རས་མ་ཞེས་བྱ་བ་གཞན་དག་གི་དཔེ་ཙམ་དུ་ཟད་དེ། རས་བལ་ལ་སོགས་པ་གཞན་གྱིས་ཀྱང་དཀྲི་བར་བྱ་བ་ནི་རིགས་པ་ཡིན་ནོ། །

[Block 3956]
འདིར་གཞུང་ནི་འོན་ཀྱང་ཡུར་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དབྱུག་གུ་གཟུགས་པར་བྱའོ། །

[Block 3957]
དགེ་སློང་དག་གིས་སྨྱིག་མ༌[^2729]བརྩལ་ཏེ་དེས་འཛུག་པ་ལས་རྨ་བྱུང་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། བྲེའི་བཅད་འཕྲོ་ལྟ་བུར་བྱའོ། །

[Block 3958]
འོན་ཀྱང་སྣད་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། རས་མ་དག་གིས་དཀྲིས་ནས་དལ་བུས་ཁད་ཀྱིས༌[^2730]གཟུགས་པར་བྱའོ༌[^2731]ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3959]
ཕོ་ལང་འཕང་བར་བྱའོ། །

[Block 3960]
ཡང་ཕྱིར་འོང་བར་བྱ་བའི་ཕྱིར་ཐ་གུས་གདགས་པར་བྱའོ་ཞེས་བྱ་བ་ནི། ཕོ་ལང་དེ་ཡང་ཕྱིར་དྲང་བར་བྱ་བའི་ཕྱིར་ཐ་གུ་ཕྲ་མོ་རིང་མོས་བཏགས་ཏེ་འཕང་བར༌[^2732]བྱའོ། །
--- END BLOCKS ---
