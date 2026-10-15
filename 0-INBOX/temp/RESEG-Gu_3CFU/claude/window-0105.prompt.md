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
[Block 3676]
ཐུན་མོང་བ་ནི་སོང་ཟིན་ཏོ།། །།

[Block 3677]
དེ་ནས་སོ་སོའི་སྐབས་བརྗོད་པར་བྱ་སྟེ། གང་དུ་འཆང་བའི་སྤང་བའི་ལྟུང་བྱེད་བསྐྱེད་ཅེ་ན། དེའི་ཕྱིར་ཡོད་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ་སུ་ཡོད་ཅེ་ན། དེའི་ཕྱིར་རང་གི་ཉིད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཐམས་ཅད་ལ་ཡང་མ་ཡིན་ནོ། །

[Block 3678]
འོ་ན་གང་ཞེ་ན། དེའི་ཕྱིར་ཞག་བཅུར་རྗེས་སུ་ཞུགས་པ་ཉིད་དོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 3679]
དུས་གང་གི་ཚེ་སྤང་བར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་གཞན་གྱི་ཉི་མའི་དང་པོ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ་རྗེས་སུ་ཞུགས་པའི་དུས་འདི་ཞག་བཅུར་བརྗོད་པ་གང་ཡིན་པ་དེ་ལས་གཞན་པའི་ཞག་ལ་དང་པོར་སྐྱ་རེངས༌[^2528]འཆར་བའི་སྐད་ཅིག་མ་དང་པོ་ལའོ། །

[Block 3680]
རང་ཉིད་གང་དུ་སྟེ་དུས་ཙམ་གང་ཞིག་ལ་ཡོད་པ་ན་ཞེ་ན། དེའི་ཕྱིར་གོས་ལའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 3681]
ཐམས་ཅད་དུ་མ་ཡིན་ཏེ་འོན་ཀྱང་འཁོར་གསུམ་ཁེབས་པའི་མཐའི་ཚད་ལའོ་ཞེས་བྱ་བ་ལ༌[^2529]འཁོར་གསུམ་ཞེས་བྱ་བ་ནི་ལྟེ་བའི་དཀྱིལ་འཁོར་དང་པུས་མོའི་ལྷ་ངའི་ཚིགས༌[^2530]གཉིས་སོ། །

[Block 3682]
འཁོར་གསུམ་པོ་དེ་དག་ཆུབ་པར་ཁེབས་པའི་མཐར་གྱུར་པའི་ཁྱོན་གྱི་ཚད་གང་ལ་ཡོད་པ་དེ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3683]
འདི་ཡང་ཐམས་ཅད་དུ་ནི་མ་ཡིན་ཏེ་གཞན་ཡང་བྱིན་གྱིས་བརླབས་པ་དང་མ་འབྲེལ་པ་ལའོ། །

[Block 3684]
གཞན་ཡང་འབྲེལ་ཀྱང་རྗེས་སུ་ཞུགས་པ་དང་བཅས་པ་ལའོ་ཞེས་བྱ་བ་ནི་འབྲེལ་ཀྱང་རྗེས་སུ་ཞུགས་པ་དང་བཅས་པ་ལའོ། །

[Block 3685]
ཡོད་པ་ཉིད་དང་རྗེས་སུ་འཇུག་པ་ལྷན་ཅིག་ཏུ་རྗེས་སུ༌[^2531]འཇུག་པ་དང་བཅས་པའོ། །

[Block 3686]
རང་ཉིད་ལས་བྱུང་བ་དང་གཞན་ལས་བྱུང་བའོ། །

[Block 3687]
རང་ཉིད་ཀྱིས༌[^2532]རྗེས་སུ་ཞུགས་པ་དང་བཅས་པ་ལ་འབྲེལ་པ་ནི་ཡུལ་ཁྱད་པར་དུ་གྱུར་པ་ཡོངས་སུ་བཟུང་བ་ཡིན་ནོ། །

[Block 3688]
འདི་ལ་གཞན་ཡོད་ན་བྱིན་གྱིས་མ་བརླབས་པ་དེའི་ཤན་ཚུན་ཆད་ནས་སོ་ཞེས་བྱ་བ་ལ། འདི་ལ་ཞེས་བྱ་བ་ནི་རྗེས་སུ་ཞུགས་པ་དང་བཅས་པའི་གོས་ལའོ། །

[Block 3689]
བྱིན་གྱིས་བརླབས་པ་རྗེས་སུ་ཞུགས་པ་དང་བཅས་པ་དེ་ལས་གཞན་བྱིན་གྱིས་མ་བརླབས་པ་དེའི་ཤན་ཚུན་ཆད་ནས་ཡོད་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3690]
ཤན་ཚུན་ཆད་ནས་སོ་ཞེས་བྱ་བ་ནི་མ་ཚང་བ་ལ་གཙོ་བོར་འགྱུར་རོ། །

[Block 3691]
དེ་ལྟར་ན་ཡོངས་སུ་དག་པ་ཉིད་བྱིན་གྱིས་བརླབས་པ་ལ་ཞེས་བྱ་བ་འདི་ཤེས་པའོ། །

[Block 3692]
འདིར་གཞུང་ནི་ཉེ་བ་འཁོར་གྱིས༌[^2533]ཞུས་པ་ལས།

[Block 3693]
བཙུན་པ་དགེ་སློང་གིས་ཆོས་གོས་དེ་ཉིད་ཞག་བཅུ་ལས་འདས་པ་ཡང་ལགས་ལ་དེ་ཉིད་ཞག་གཅིག་བྲལ་བ་ཡང་ལགས་པ་མཆིས་སམ་ཉེ་བ་འཁོར་ཡོད་དེ་འདི་ལྟ་སྟེ། དགེ་སློང་གིས་ཆོས་གོས་རྒྱུན་མ་ཆད་པར་རྒྱུན་འབྱུང་བ་ཡང་ཡིན་ལ། དེས་ཆོས་གོས་འབྱུང་བ་དེ་ཞག་བཅུ་པ་ལ་བྱིན་གྱིས་བརླབས་ནས་མཚམས་ཀྱི་ཕྱི་རོལ་དུ་ཆོས་གོས་དེ་མེད་པར་སྐྱ་རེངས༌[^2534]འཆར་བར་བྱེད་ན། དེ་ལྟར་ན་ཆོས་གོས་དེ་ནི་དེ་ཉིད་ཞག་བཅུ་འདས་པ་ཡང་ཡིན་ལ་དེ་ཉིད་ཞག་གཅིག་བྲལ་བ་ཡང་ཡིན་ནོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3694]
འཆང་བའི་སྤང་བའོ།། །།

[Block 3695]
གདིང་བ་དང་བྲལ་བ་ལ་ནི་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་འདིར་ཕྲན་ཚེགས་རྣམས་ལས་འདི་ལ་སོགས་པའི་ཤིན་ཏུ་མང་བ་ཟད་པས་ཞེས་བྱ་བའི་མཐར་འདི་སྙེགས༌[^2535]པའོ། །

[Block 3696]
གལ་ཏེ་དེང་ཉིད་ཕྱིར་ལྡོག་ཅིང་གནས་པར་བྱའོ་སྙམ་པ་མེད་ན་གདིང་བ་གཞག་སྟེ་འགྲོ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་འདི་ལྟར་དགོངས༌[^2536]ནས་འགྲོ་བ་ལ་དུས་འབྱོར་པར་འགྱུར་བ་ལ་དེར་སླར་འོངས་པ་ཉིད་ལ་དེར་གནས་པར་བྱའོ། །

[Block 3697]
གལ་ཏེ་དེང་ཉིད་ཀྱི་ཕྱིར་ལྡོག་ཅིང་འདིར་གནས་པར་བྱའོ་སྙམ་པའི་བསམ་པ་མེད་ན་གདིང་བ་མེད་པར་གང་དུ་ཡང་འགྲོ་བར་མི་བྱའོ། །

[Block 3698]
དེར་དུས་མ་འབྱོར་ན་ཡོད་པར་གྱུར་པ་ལ༌[^2537]བརྙས་ཏེ་གདིང་བ་ལ་གནས་པར་བྱའོ། །

[Block 3699]
མ་རྙེད་ན་བླ་གོས་བཞི་བལྟབ་ཏུ་བྱས་པའི་སྟེང་དུ་ཡུན་རིང་དུ་མི་ཉལ་བར་རོ། །

[Block 3700]
སྣམ་སྦྱར་གཞག་པར་མི་འོས་པའི་གནས་སུ་དབྱར་གྱི་གོས་རས་ཆེན་ཡང་གཞག་པར་མི་བྱའོ་ཞེས་བྱ་བ་གནས་གང་ན་དགེ་སློང་ཉིད་མེད་པ་དང་སྒོ་གླེགས་གཉིས་ཀ་འདོམ་པ་དེར་གཞག་པར་མི་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3701]
ཆར་འབབ་ན་མི་གཞག་གོ། །

[Block 3702]
ཆུ་ཀླུང་གིས་ཆོད་པར་འགྲོ་བ་ལ་ཡང་མི་གཞག་གོ། །

[Block 3703]
དེ་གཉིས་དོགས་པར་ཡང་མི་གཞག་གོ་ཞེས་བྱ་བ་ནི་དབྱར་གྱི་གོས་རས་ཆེན་ཞེས་བྱ་བ་འདི་ལ་ནི་འདིར་སོ་སོར་སྦྱར་བར་བྱའོ། །

[Block 3704]
འདི༌[^2538]གཉིས་ཞེས་བྱ་བ་ནི་ཆར་འབབ་པ་དང་ཆུ་ཀླུང་གིས་ཆོད་པ་དེ་གཉིས་ཡོད་པར་དོགས་པའི་གནས་སུ་འགྲོ་ན་ཡང་དབྱར་གྱི་གོས་རས་ཆེན་མི་གཞག་པར་བསྐུར༌[^2539]རོ། །

[Block 3705]
དགེ་སློང་དང་བཅས་པ་ཉིད་དང་སྒོ་གླེགས་དང་བཅས་པ་ཉིད་དུ་བཅས་པའི་གནས་དང་ཆར་འབབ་པ་དང་ཆར་འབབ་པར་དོགས་པ་དང་། བགྲོད་པར་བྱ་བ་ཆུ་ཀླུང་གིས་ཆོད་པ་ཉིད་འདི་ལྟ་བུ་མེད་ན་གནང་བ་མ་བྱིན་པ་དང་སྲ་བརྐྱང་མ་བཏིང་བས་སྣམ་སྦྱར་མེད་པར་གར་ཡང་འགྲོ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ལ་བཅས་པ་ཉིད་ཅེས་བྱ་བ་ནི་གཉིས་པོ་འདི་དང་ཡང་དག་པར་ལྡན་པའོ། །

[Block 3706]
ཆུ་ཀླུང་གིས་ཆོད་པ་ཞེས་བྱ་བ་ནི་འབད་པས་བརྒལ་བར་མི་བྱ་བའི་ཆུས་བར་དུ་ཆོད་པ་ཉིད་དོ། །

[Block 3707]
གཞི་སྣང་བ་ཡོད་པ་ལ་བར་དུ་མ་ཆོད་པ་ཉིད་དོ། །

[Block 3708]
འདི་ལྟ་བུ་མེད་ན་ཞེས་བྱ་བ་ནི་དགེ་སློང་དང་བཅས་པ་ཉིད་ཅེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 3709]
འདི་ཡོད་པ་ལ༌[^2540]འདི་དང་ལྷན་ཅིག་ཏུ་སྦྱོར་བ་མེད་པར་སྐྱོན་མེད་དེ། ཆར་འབབ་པ་དང་དགེ་སློང་དང་བཅས་པ་ཉིད་མི་བདེན་ཡང་སྒོ་གླེགས་དང་བྱས་པ་ཉིད་དུ་བཅས་པའི་གནས་ཞེས་བྱ་བར་སྦྱར་ཏེ་སྣམ་སྦྱར་ཞེས་བྱ་བ་འདིར༌[^2541]རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 3710]
དེས་བསྙེན་པར་མ་རྫོགས་པའི་ལག་ཏུ་སྣམ་སྦྱར་གཏམས་པ་ཡང་རུང་བར་སྣང་ངོ་། །གནས་སུ་ཕྱིན་པར་མི་འགྱུར་ན་ཆོས་གོས་ཀྱིས་ཕྱུང་སྟེ་གཞན་ལ་བྱིན་གྱིས་བརླབས་པ་ནི་ཆོ་གའི་རྣམ་པའོ་ཞེས་བྱ་བ་ནི་གནས་གཞན་ན་འདུག་པའི་བྱིན་གྱིས་བརླབས་པ་ཕྱུང་སྟེ། ཁྱིམ་པ་ཡན་ཆད་ཀྱི་གོས་སམ་གཞན་ལ་བརྙས་པ་ལ་ཡང་བྱིན་གྱིས་བརླབས་པ༌[^2542]བསྒྲུབ་པར་བྱའོ། །

[Block 3711]
འདི་ནི་ཆོས་གོས་ཀྱི་གནས་ལ་ཐོབ་པ་མི་སྲིད་པ་ལ་སླར་ཆོ་གའི་རྣམ་པ་སྟེ་ཐབས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3712]
སྣམ་སྦྱར་ལྕི་བ་ཉིད་ཡིན་ན་རྒན་པོ་དང་ནད་པ་དག་ལ་མི་འབྲལ་པའི་གནང་བ་སྦྱིན་ནོ་ཞེས་བྱ་བ་སྟེ་འབྲལ་པའི་སྤང་བའི་ཐབས་སོ། །

[Block 3713]
གང་ལ་གནང་བ༌[^2543]དང་སྤང་བའི་ལྟུང་བྱེད་ལ་བྱེད་པ་པོ་ཉིད་ཅེ་ན། དེའི་ཕྱིར་བྱིན་གྱིས་བརླབས་པ་དང་གནང་བ་མ་ཐོབ་པ་ནི་བྱེད་པ་པོ་ཉིད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གོས་ཞེས་བྱ་བ་འདི་ལ་གོས་ཀྱི་དངོས་པོར་ཡོངས་སུ་གྱུར་པ་ལ་སོ་སོར་ཉེ་བར་གནས་པའོ། །

[Block 3714]
དེ་བས་ན་ལྷུང་བཟེད་ལ་སྐབས་མ་ཡིན་ནོ། །

[Block 3715]
བྱིན་གྱིས་བརླབས་པའི་གོས༌[^2544]ལ་གང་ཟག་གནང་བ་མ་ཐོབ་པ་ནི་ལྷུང་བའི་བྱེད་པ་པོ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །
--- END BLOCKS ---
