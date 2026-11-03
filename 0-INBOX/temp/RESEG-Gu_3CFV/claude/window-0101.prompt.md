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
[Block 3536]
མཚན་མཐུན་པ༌[^2305]བསྙེན་པར་རྫོགས་པ་ལ༌[^2306]གསོ་སྦྱོང་བྱེད་པ་འདི་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 3537]
སྔགས་ནི་འདི་ཡིན་ཏེ། ཆེ་གེ་མོ་ཞིག་དགོངས་སུ་གསོལ། དེང་དགེ་འདུན་གྱི་གསོ་སྦྱོང་བཅོ་ལྔ་པ་ལགས་ཏེ། བདག་དགེ་ཚུལ་མིང་འདི་ཞེས་བགྱི་བའི་གསོ་སྦྱོང་ཡང་གསོ་སྦྱོང་བཅོ་ལྔ་པ་ལགས་ན། བདག་དགེ་ཚུལ་མིང་འདི་ཞེས་བགྱི་བ། བར་ཆད་ཀྱི་ཆོས་རྣམས་ཡོངས་སུ་དག་གོ་ཞེས་བདག་ཉིད་ཆེ༌[^2307]ཞེས་བྱ་བ་ལ་སོགས་པ་ཡོད་པའི་ཕྱིར་རོ། །

[Block 3538]
བསླབ་པ་བྱིན་པ་ནི་འདྲ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་ལྟུང་བ་ལ་སྦྱོར་བ་དགེ་སློང་འདྲ་བ་ཉིད་དོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 3539]
འདིར་འདི་ལ་དགེ་སློང་མ་ཡང་དེ་བཞིན་དུ་ཕན་ཚུན་འདྲ་བ་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 3540]
དགེ་སློང་བཞིན་དུ་འདིས༌[^2308]ལྷག་པར་སྤྱོད་པ་ལ། དགེ་སློང་བཞིན་དུ་ཡང་གཞན་ལ་བརྡེག་པ་དང་། གཟས་པ་དང་། འགྱོད་པ་བསྐྱེད་པ་ལ་སོགས་པས་ལྟུང་བ་རྣམས་བསྐྱེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3541]
བསྙེན་པར་མ་རྫོགས་པ་དང་ལྡན་པ་ཉིད་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི། འདི་ལ་རྣམ་པ་འདིས་དགེ་སློང་དང་མཉམ་པ་ཉིད་ཡོད་པར་གྱུར་ཀྱང་གང་ལ༌[^2309]བྱིན་ལེན་བྱེད་པ་དང་ལྷན་ཅིག་ཉལ་བའི་ལྟུང་བྱེད་ལ་སོགས་པ་བསྙེན་པར་མ་རྫོགས་པ་ལ་བསྐྱེད་པ་དེ་ལ་དེ་ལས་མ་ཡིན་ཏེ། གང་ལ་ཡང་བསྙེན་པར་རྫོགས་པ་གཞན་ལས་སྐྱེས་པ་རང་གི་བདག་ཉིད་ལ་ཡང་སྐྱེས་པ་ཉིད་ཉེ་བར་གནས་པ་ཉིད་དང་། འཛིན་པ་ཉིད་ལས༌[^2310]སྐྱེས་པ་ཡིན་ནོ། །

[Block 3542]
དེ་ལ་འདིར་ཉམས་པ་དང་འདྲ་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 3543]
དེ་ལ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་བསླབ་པ་བྱིན་པ་དེ་ལ་བསྙེན་པར་མ་རྫོགས་པ་དང་ལྡན་པ་ཉིད་ནི་མ་ཡིན་ཏེ། ཕྱོགས་གཅིག་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 3544]
འདིར་གཞུང་ནི་ཞུ་བ་ལས།

[Block 3545]
བཙུན་པ་རེ་ཞིག་དགེ་སློང་ལ་རྒྱུ་དུས་གསོག་འཇོག་བགྱིས་པར་འགྱུར། གསུམ་གྱིས་ཏེ། གསུམ་གང་ཞེ་ན། བདག་ཉིད་ཀྱིས་གསོག་འཇོག་བྱས་པ་དང་། དགེ་སློང་གིས་གསོག་འཇོག་བྱས་པ་དང་། དགེ་སློང་གི་དགེ་འདུན་གྱིས་གསོག་འཇོག་བྱས་པའོ། །

[Block 3546]
བཙུན་པ་རེ་ཞིག་དགེ་སློང་མ་ལ་རྒྱུ་དུས་གསོག་འཇོག་བྱས་པར་འགྱུར། གསུམ་གྱིས་ཏེ། གསུམ་གང་ཞེ་ན། བདག་ཉིད་ཀྱིས་གསོག་འཇོག་བྱས་པ་དང་། དགེ་སློང་མས་གསོག་འཇོག་བྱས་པ་དང་། དགེ་སློང་མའི་དགེ་འདུན་གྱིས་གསོག་འཇོག་བྱས་པའོ། །

[Block 3547]
བཙུན་པ་རེ་ཞིག་བསླབ་པ༌[^2311]བྱིན་པ་ལ་རྒྱུ་དུས་གསོག་འཇོག་བྱས་པར་འགྱུར། བཞི༌[^2312]སྟེ། བཞི་གང་ཞེ་ན། བདག་ཉིད་ཀྱིས་གསོག་འཇོག་བྱས་པ་དང་། བསླབ་པ་བྱིན་པས་གསོག་འཇོག་བྱས་པ་དང་། དགེ་སློང་གིས༌[^2313]གསོག་འཇོག་བྱས་པ་དང་། དགེ་སློང་གི་དགེ་འདུན་གྱིས་གསོག་འཇོག་བྱས་པའོ། །

[Block 3548]
བཙུན་པ་རེ་ཞིག་བསླབ་པ༌[^2314]བྱིན་པ་མོ་ལ་ཞེས་བྱ་བ་ནས། བཞི་གང་ཞེ་ན། བདག་ཉིད་ཀྱིས་གསོག་འཇོག་བྱས་པ་དང་། བསླབ་པ་བྱིན་པ༌[^2315]མོས་གསོག་འཇོག་བྱས་པ་དང་། དགེ་སློང་མས་གསོག་འཇོག་བྱས་པ་དང་། དགེ་སློང་མའི་དགེ་འདུན་གྱིས་གསོག་འཇོག་བྱས་པའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3549]
དགེ་སློབ་མ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ལ་ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲས་ནི་བསྙེན་པར་མ་རྫོགས་པ་དང་ལྡན་པ་ཉིད་མ་ཡིན་ནོ༌[^2316]ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 3550]
འདིར་གཞུང་ནི་ཞུ་བ་ལས།

[Block 3551]
བཙུན་པ་རེ་ཞིག་དགེ་སློབ་མ་ལ་ཞེས་བྱ་བ་ནས་ལྔ་སྟེ། ལྔ་གང་ཞེ་ན། བདག་ཉིད་ཀྱིས་གསོག་འཇོག་བྱས་པ་དང་། དགེ་སློབ་མས་གསོག་འཇོག་བྱས་པ་དང་། བསླབ་པ་བྱིན་པ་མོས་གསོག་འཇོག་བྱས་པ་དང་། དགེ་སློང་མས་གསོག་འཇོག་བྱས་པ་དང་། དགེ་སློང་མའི་དགེ་འདུན་གྱིས་གསོག་འཇོག་བྱས་པའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3552]
འགྲོ་བ་གཞན་གྱི་རྣམ་པ་བསྟེན་པ་ན་དགེ་སློང་གི་འདུ་ཤེས་ཡོད་པ་ལའོ་ཞེས༌[^2317]བྱ་བ་ལྟུང་བ་ལ་སྦྱོར་བ་འདྲ་བ་ཉིད་དོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 3553]
དགེ་སློང༌[^2318]སྔགས་དང་སྨན༌[^2319]ལ་སོགས་པའི་དབང་གིས་འགྲོ་བ་གཞན་གྱི་རྣམ་པ་ཞེས་བྱ་བ་དུད་འགྲོ་ལ་སོགས་པའི་གཟུགས་སུ་བསྒྱུར་ནས་བྱ་བ་མ་ཡིན་པ་བྱེད་པ་གང་ཡིན་པ་དེ་ལ་དེར་ལྟུང་བ་ཉིད་དོ། །

[Block 3554]
གལ་ཏེ་བྱེད་པའི་དུས་ན་དགེ་སློང་ལ་སོགས་པའི་འདུ་ཤེས་མ་བརྗེད་པར༌[^2320]གྱུར་ན་ལྟུང་བ་འདྲ་བ་ཉིད་དོ། །

[Block 3555]
མེད་ན་ནི༌[^2321]སྨད་པའོ་ཞེས་བྱ་བ་དེའི་ཚེ་ལྟུང་བ་འབྱིན་པ་དེ་ལ་བདག་ཉིད་དགེ་སློང་ཡིན་པའི་འདུ་ཤེས་མེད་ཅིང་བརྗེད་པར༌[^2322]གྱུར་པ་ཉིད་ཡིན་ན་ནི་ལྟུང་བ་ལ་སྦྱོར་བ་དེའི་ཚིག༌[^2323]འོག་མར་ན་སྨད་པ་ཡིན་ནོ། །

[Block 3556]
ཚིག་སྔ་མར་སྦྱོར་བ་བྱས་པ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ན་སྨད་པ་ཉིད་དོ་ཞེས་བྱ་བའི་རྗེས་སྙེག༌[^2324]པའི་ཕྱིར་ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲ་སྨོས་སོ། །

[Block 3557]
ཁྱིམ་པ་ཉིད་དུ་སྦྱོར་བ་ཙམ་གྱི་དབང་གིས་གང་ཞིག་དགེ་ཚུལ་ཉིད་ལ་ཚིག༌[^2325]སྔ་མར་སྦྱོར་བ་བྱས་པ་ཙམ་གྱི༌[^2326]དབང་གིས་བསྙེན་པར་རྫོགས་པ་ཉིད་ལ་དེ་ལ་ཡང་མ་རྫོགས་པ་ཉིད་ནི་ན་སྨད་པ་ཉིད་ཡིན་ཏེ། དེ་མ་ཐག་པའི་ཚིག༌[^2327]ཉིད་དོ། །

[Block 3558]
དེ་ལྟར་ཡང་འདིར་གཞུང་ནི་བསྙེན་པར་མ་རྫོགས་པས་བརྐུ་བ༌[^2328]ལ་སྦྱོར༌[^2329]ཞིང་བསྙེན་པར་མ་རྫོགས་པའི་ཕྱིར་རྐུ་བར་བྱེད་ན་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 3559]
བསྙེན་པར་མ་རྫོགས་པ་བརྐུ་བ་ལ་ཇི་སྲིད་དུ་བསྙེན་པར་རྫོགས་པའི་ཕྱིར་རྐུ་ན་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཡིན་ནོ། །

[Block 3560]
འདིར་དེའི་ཕྱིར་ཞེས་བསྟན་པར་ཤེས་པར་བྱ་སྟེ། ཚིག༌[^2330]སྔ་མར་སྦྱོར་བ་ཙམ་གྱི་དབང་ཁོ་ན་ལས་མེད་ན། དེའི་ཚེ་སྦྱོར་བ་ན་སྨད་པའོ། །

[Block 3561]
སྦྱོར་བ་ཡོད་ན་ནི་དེའི་ཚེ་བྱས་པ་ཉིད་ལ་དངོས་པོ་ལ་ན་སྨད་པའི་རིགས་པའི་ཕྱིར་ལེན་པའི་དབང་དང་རྟེན་གྱི་བྱེ་བྲག་གི་དབང་གིས་འདི་ཚིག༌[^2331]འོག་མར་གཏན་དུ་བའི་སྦྱོར་བ༌[^2332]ལ་ལྟུང་བར་འགྱུར་བའི་རྣམ་པར་རིག་པར་སྐྱེས་པའི་བདག་གི༌[^2333]དངོས་པོའི་དབང་དུ་བྱས་པ་ལ་ལྟུང་བྱེད་དུ་རྣམ་པར་གནས་པ་ལ་ལྕི་བ་ཉིད་ནི་ཡང་བསྙེན་པར་རྫོགས་པ་ཉིད་ལ་ཡང་རྣམ་པར་གཞག་པའོ། །

[Block 3562]
ན་སྨད་པའི་སྦྱོར་བ་དེའི་ཚེ་ན་མེད་པས་དེ་བཞིན་དུ་འོག་མའི་ཚིག་སྦྱོར་བའི་དབང་གིས་ཚིག༌[^2334]སྔ་མ་ལ་འཆད་པར་འགྱུར་བའི་ལྟུང་བར་འགྱུར་བའི་རྣམ་པར་རིག་པ་ལས་སྐྱེས་པ། བདག་གི་དངོས་པོ༌[^2335]རྣམ་པར་འགྱུར་བ་ལ་ལྟུང་བྱེད་དུ་རྣམ་པར་གཞག་པ་ལ་ཡང་བ་ཉིད་ནི་ཡང་དགེ་ཚུལ་ཉིད་ལ་སོགས་པ་ལ་རྣམ་པར་གཞག་པའོ། །

[Block 3563]
འདིར་སྦྱོར་བ་གང་ཡིན་པ་དེ་ལ་མཚན་ཉིད་ཇི་ལྟ་བར་ལྟུང་བ་དང་ལྟུང་བ༌[^2336]མེད་པར་རིག་པར་བྱའོ། །

[Block 3564]
ཕྱི་མ་ལ་ཡང་དེ་དང་ལྡན་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། འདིར་གང་དུ་ཚིག༌[^2337]ཕྱི་མ་སྟེ། དགེ་ཚུལ་ཉིད་ལ་སོགས་པ་ལ་བསྙེན་པར་རྫོགས་པའི་གནས་སྐབས་ཀྱི་སྦྱོར་བ་ཙམ་གྱི་དབང་གིས་བསྒྲུབ་པ་ནི་དེ་དང་ལྡན་པ་ཉིད་དང་ཚིག༌[^2338]སྔ་མ་ཉིད་དེ་ལ་ཉེས་བྱས་ཡོངས་སུ་རྫོགས་པར་བསྐྱེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3565]
འདི་ཡང་བསྙེན་པར་རྫོགས་པའི་གནས་སྐབས་ལ་སྦྱོར་བ་བྱས་པ་གང་ཡིན་པ་དེ་ལ་མཚན་ཉིད་ཇི་ལྟ་བར་ལྟུང་བ་རྣམ་པར་གཞག་པ༌[^2339]རིག་པར་བྱའོ། །

[Block 3566]
རྫས་བཀག་པས་བཟང་པོ་ལ་ཡང་དེ་དང་ལྡན་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་བཀག་པ་ལས་ཤིན་ཏུ་ཁྱད་པར་འཕགས་པའི་རྫས་གང་ཡིན་པ་དེ་ལ་ཡང་གང་ཞིག་གཞན་ཉིད་ནི་དེ་དང་ལྡན་པར་འགྱུར་བ་ཉིད་བཀག་པར་གྱུར་པ་ནི།

[Block 3567]
དཔེར་ན་བལ་ནག་པོ་འབའ་ཞིག་ལས་སྟན་བྱེད་ན་སྤང་བའི་ལྟུང་བྱེད་དུ་འགྱུར་བ་དེ་བཞིན་དུ་དེ་ལས།

[Block 3568]
དེ་བཞིན་དུ་སྲིན་བལ་དང་རྫས་རིན་པོ་ཆེ་ལས་སྟན༌[^2340]བྱེད་པ་ལས༌[^2341]ཡང་བཀག་སྟེ། སྤང་བའི་ལྟུང་བྱེད་ཁོ་ནར་འགྱུར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3569]
འདྲ་བ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་རྫས་བཟང་ངན་འདྲ་བ་ལ་ཡང་བཀག་པ་ཉིད་ཀྱིས་སྙིང་པོ་དང་ལྡན་པ་ཉིད་ཀྱིས་སྤང་བའི་ལྟུང་བ་ཁོ་ནར་འགྱུར་རོ། །

[Block 3570]
གང་ཞིག་བལ་གྱི་གོས་དང་འདྲེས་པའི་སྲིན་བལ་དང་བལ་ནག་པོ་འབའ་ཞིག་གམ། བལ་དཀར་པོ་དང་བཅས་པའམ་བལ་དཀར་པོའི་སྟན་བྱེད་པ་ལ་ཡང་སྤང་བ་ཁོ་ནར་འགྱུར་རོ། །

[Block 3571]
མཚན་གྱུར་པ་ནི་དེའི་ཞིང་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ལྟུང་བ་དེའི་ཞིང་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 3572]
ཞིང་ཉིད་གང་ཡིན་པ་དེ་ནི་ལྟུང་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3573]
དེ་བས་ན་མཚན་གྱུར་པ་ཞེས་བྱ་བ་ནི་མཚན་མ་སྔ་མ་ཉིད་སྦྱོར་བ་ཙམ་གྱི༌[^2342]དབང་གིས་བསྒྲུབ་པར་གྱུར་པའི་ལྟུང་བྱེད་དོ། །

[Block 3574]
གང་ཞིག་ལྟུང་བ་ལ་དེའི་མཚན་མ་ཉིད་ཞིང༌[^2343]དུ་གྱུར་པ་ན་གལ་ཏེ་དེ་ཉིད་ལ་ཞིང་ཉིད་གང་གི་དོན་དུ་སྦྱོར་བ་དང་བཅས་པ་ད༌[^2344]ཉིད་དོ། །

[Block 3575]
གལ་ཏེ་ན་སྨད་པ་ཉིད་ཡིན་ན་སྨད་པའོ། །
--- END BLOCKS ---
