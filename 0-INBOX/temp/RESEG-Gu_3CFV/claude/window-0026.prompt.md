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
འདིར་བུམ་པའི་བུ་ག་ཆེན་པོ་གཅིག་གདོད་པར་བྱའོ་ཞེས་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 912]
དེ་ཡང་འདིར་དོན་གྱིས་ཐོབ་པ་སྟེ་དེ་བས་ན་འདིར་མ་བསྟན་ཏོ། །

[Block 913]
དེ་དག་ཏུ་རས་མ་དགབ་པ་ཉིད་དོ་ཞེས་བྱ་བ་ལ་དེ་དག་ཏུ་ཞེས་བྱ་བ་ནི་ནང་གི་བུ་ག་རྣམས་ལའོ། །

[Block 914]
འདིར་གཞུང་ནི་དེ་དག་གི་སྟེང་དུ་རས་གཡོགས་ཏེ་ཆུ་བཙགས་པར༌[^558]བྱའོ་ཞེས་གསུངས་པ་ཡིན་གྱི་བུམ་པའི་བུ་ག་ལ་ནི་མ་ཡིན་ནོ། །

[Block 915]
ཆུ་ཚགས་ཉེ་བར་གཞག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་བདག་གི་བ་འདི་ཤིན་ཏུ་བྱས་པ་ངེས་པར་བྱ་བའི་དོན་ཏོ། །

[Block 916]
ཆུ་ཚགས་གྲུ་གསུམ་མམ་རིལ་བ་ཞབས་ཚགས་ཅན་ནམ་གསལ་ཚགས་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་བུམ་ཚགས༌[^559]གཅེའུ་ཅན་ནི་ཚུ་ཚགས་ཉིད་མེད་པ་མ་ཡིན་ཏེ། དེ་བས་ན་འདིས་འདི་ལ་མ་བཟུང་བ་ཉིད་དུ་ཤེས་པར་མི་བྱའོ། །

[Block 917]
འཆང་བ་ཉེ་བར་དགོས་པར་བྱ་བ་ལ་གསལ་ཚགས་ཀྱི་ཚིག་གིས་བཟུང་བ་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 918]
འམ་ཞེས་བྱ་བའི་སྒྲ་ནི་འདིར་གཅིག་གི་རྣམ་པ་འདི་ཉེ་བར་གཞག་པ་ལ་འདི་ཉེས་པ་ལ་འདི་ཉེས་པ༌[^560]ཡིན་གྱི་དུ་མ་ལ་ནི་མ་ཡིན་ནོ་ཞེས་བསྟན་པའི་ཕྱིར་བྱ་མ་བུམ་དང་རིལ་བ་དག་གིས་ཆུ་རུང་བར་བཅུས་པ་ཉིད་དང་ཡོད་པ་ཉིད་ཀྱང་དེ་དང་ལྡན་པ་ཉིད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བྱ་མ་བུམ་ཞེས་བྱ་བ་ནི༌[^561]ལམ་ཇི་སྲིད་དུ་ཆུ་རུང་བ་བཅུས་པ་ཡོད་པ་དེ་སྲིད་དུ་ཆུ་ཚགས་དང་ལྡན་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ཤུགས་ཀྱིས་རྟོགས་པར་བྱའོ། །

[Block 919]
ཡོད་པ་ཉིད་ཀྱང་ཞེས་བྱ་བ་ནི། དེ་ནས་ལམ་གྱི་ཕྱིར་དེ་བཟུང་བ་ལ་བསྒྲུབ་པར༌[^562]འགྱུར་བའི་བྱ་མ་བུམ་ཉིད་ལ་ཉེ་བར་བརྩིས་པ་འདི་ཉིད་དོ། །

[Block 920]
དེ་དང་ལྡན་པ་ཉིད་དོ་ཞེས་བྱ་བ་ལ། ཉིད་དོ་ཞེས་བྱ་བ་ནི་ཆུ་ཚགས་ཉིད་དོ། །

[Block 921]
དེ་མེད་པར་ལྗོངས་རྒྱུ་ཞིང་འགྲོ་བར་མི་བྱའོ། །

[Block 922]
ནང་དང་བཅས་པ་དང་ལྷན་ཅིག་ཏུ༌[^563]མི་བྱའོ། །

[Block 923]
གལ་ཏེ་རྐྱེན་དེ་ལྟ་བུ་ཡོད་ན་བཟོད་པ་གསོལ་ཏེའོ། །

[Block 924]
བྱ་བ་བྱེད་པ་ན་ཡོད་པ་ཉིད་ནི་ཡོད་པ་ཉིད༌[^564]ཡིན་ནོ། །

[Block 925]
གཞན་གྱིས་འདི་ལྟར་དེར་བྱིན་ནོ་ཞེས་ཁས་བླངས་པ་ཉིད་དེ་དང་ལྡན་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་དེར་ཞེས་བྱ་བ་ནི་བྱ་བ་བྱེད་པའི་དུས་ལའོ། །

[Block 926]
ཆུ་བཙགས་པའི༌[^565]དུས་དེར་གཞན་གྱིས་ཁས་བླངས་པ་ལ་དེ་དང་ལྡན་པ་ཉིད་ནི་ཆུ་ཚགས་དང་ལྡན་པ་ཉིད་དོ། །

[Block 927]
གང་གི་ཕྱིར་བྱ་བ་བྱེད་པ་ལ་ཡོད་པ་ཉིད་གང་ཡིན་པ་དེ་ནི་འདིར་ཡོད་པ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 928]
ལྗོངས་རྒྱུ་བའི་ཚེ་འབྲལ་བ་ན་སྦྱིན་པར་ཁས་མ་བླངས་ན་དེ་ལ་བརྟེན་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི། གང་གི་ཚེ་འབྲལ་བ་ཡོད་པར་གྱུར་ན་དེའི་ཚེ་ཆུ་ཚགས་སྦྱིན་ནོ་ཞེས་དེ་ལྟར་ཆུ་ཚགས་དང་ལྡན་པས་ཆུ་ཚགས་སྦྱིན་པར་ཁས་བླངས་ན་ལྗོངས་རྒྱུ་བའི་ཚེ་འདི་སྦྱིན་པར་ཁས་བླངས་པ་དེ་དང་ལྡན་པ་ཉིད་གང་ཡིན་པ་དེ་ནི་ཆུ་ཚགས་དང་ལྡན་པ་ཉིད་དེ། དེ་ལ་བརྟེན་པར་མི་བྱ་སྟེ་འབྲལ་པའི་ཚེ་སྦྱིན་པར་ཁས་བླངས་པ་ནི་སྔ་མའི་ཁས་བླངས་པ་ནི་ཕྱིས་འབྲལ་པའི་ཚེ་ན་མེད་པའི་ཕྱོགས་དང་མཐུན་པ་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 929]
ཕོངས་པར་མི་འགྱུར་བའི་ཉེ་འཁོར་དུ་འགྲོ་བ་ནི་རྒྱུ་བ་མ་ཡིན་ནོ། །

[Block 930]
དེའི་ཕྱིར་རྒྱང་གྲགས་ལྔ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། ཕོངས་པར༌[^566]མི་འགྱུར་བ་ནི་ཉེ་འཁོར་དེ་ཉིད་དོ། །

[Block 931]
འདིར་དེ་དག་གི་གཞུང་ནི་གཞུང་ཁ་ཅིག་ལས་བཙུན་པ་ཆང༌[^567]ཚགས་མ་མཆིས་པར་གྲོང་གཞན་ནས་གཙུག་ལག་ཁང་གཞན་དུ་མཆིར་རུང་ངམ། རུང་སྟེ་གལ་ཏེ་དེར་སོང་ཡང་ཕོངས་པར་མི་འགྱུར་ནའོ་ཞེས་བྱ་བ་དང་། གཞུང་ཅིག་ཤོས་ཀྱིས༌[^568]ནི་ཆབ་ཚགས་མ་མཆིས་པར་ཤུལ་དུ་ཞུགས་ཏེ་མཆིར་རུང་ངམ་རུང་སྟེ་རྒྱང་གྲགས་ལྔ་ཚུན་ཆད་དོ། །

[Block 932]
དེ་དེས་དེར་སོན་པ་ན་ཕོངས་པར་མ་གྱུར་ན་ཞེས་བྱ་བ་གསུངས་པ་ཡིན་ནོ། །

[Block 933]
མདོ་འདི༌[^569]ནི་གཞུང་ཕྱི་མ་ཤོས་བསྡུས་པ་ཡིན་ནོ། །

[Block 934]
གང་ཞིག་འདིར་གལ་ཏེ་དེར་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིག་གིས་བསྡུས་པ་ཡིན་ནོ། །

[Block 935]
གནས་སུ་བཞག་སྟེ་སོང་བ་དེ་དང་ལྡན་པ་ཉིད་མ་ཡིན་པ་དེ་ནི་རང་དགར་བྱེད་པ་མ་ཡིན་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་བདག་དེར་སོང་ན་དེ་དང་ལྡན་པ་ཉིད་ཅེས་བྱ་བ་དེ་ལྟར་ངེས་པ་མེད་ན་དེའི་ཚེ་ཆུ་ཚགས་མེད་པར་དེས་དེར་འགྲོ་བར་མི་བྱའོ། །

[Block 936]
དེ་བས་ན་དེ་ལ་འདི་ནི་བྱེད་པ་པོའོ། །

[Block 937]
འདོད་པས་བྱས་པ་ཉིད་དེ་ལ་ཆུ་ཚགས་ཉིད་མེད་པར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 938]
གཅིག་གིས་དགེ་འདུན་མན་ཆད་དུ་མ་དེ་དང་ལྡན་པ་ཉིད་མ་ཡིན་པར་མི་འགྱུར་རོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་མན་ཆད་དུ་མ་དག་ལ་གཅིག་གིས་ཆུ་ཚགས་དང་ལྡན་པ་ཉིད་མ་ཡིན་པར་མི་འགྱུར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 939]
རྒྱུན་མགྱོགས་པ༌[^570]ལ་ཕོངས་པར་མི་འགྱུར་བ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དེ་ལས་གཞན་པའི་རྒྱང་གྲགས་ལྔ་ལ་དེ་དང་ལྡན་པ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ༌[^571]འདི་ཤེས་པར་བྱའོ། །

[Block 940]
འདི་ལ་ཡང་ཆོ་ག་འདི་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 941]
འདིར་གཞུང་ནི་བཙུན་པ་ཆུ་ཀླུང་འབབ་པ་ལ་ཆབ་ཚགས་མ་མཆིས་པར་མཆིར་རུང་ངམ། ཉེ་བ་འཁོར་རུང་སྟེ་རྒྱང་གྲགས་ལྔ་ཚུན་ཆད་དུའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 942]
དེ་ལ་རྒྱུན་ཕྱོགས་སུ་རྗེས་སུ་འབྲལ་བར་འགྲོ་བ་ནི་རྒྱང་གྲགས་ཀྱི་བར་དུ་འཇུག་ཏུ་རུང་ངོ་ཞེས་པ་ལ། ཆུ་རྟོག་པ༌[^572]ལས་བརྩམས་ཏེ་རྗེས་སུ་འགྲོ་བར་བྱེད་པ་ན། རྒྱང་གྲགས་འདི་ལ་རྒྱུན་ཕྱོགས་སུ་ཆུ་བོ་ལ་ཆུ་རྟོག་པ༌[^573]དེ་ཉིད་ཀྱིས་འཇུག་པའོ། །

[Block 943]
དེའི་འོག་ཏུ་སླར་ཆུ་རྟོག་པས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 944]
ཆོ་ག་དེའི་དམིགས་ཀྱིས་བསལ་བ་བྱས་པ་ཡིན་ཏེ། གལ་ཏེ་ཆུ་གཞན་དང་འདྲེས་པར་གྱུར་ན་དེ་མན་ཆད་དུའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་ཞེས་བྱ་བ་ནི་ཆུའི་རྒྱུན་མགྱོགས་པ་དེ་རྒྱང་གྲགས་གཅིག་གི་མཐར་ཡང་ངོ་། །གལ་ཏེ་ཆུ་གཞན་དང་འདྲེས་པ་དེ་ལས་སྔ་རོལ་དུ་ཆུ་རྟོག་པ༌[^574]དེ་ཉིད་ཀྱི་འཇུག་པའོ། །

[Block 945]
ཆུ་འདྲེས་པ་མན་ཆད་ལ་ནི་དེས་ཡང་བརྟག་ཅིང་འཇུག་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

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
--- END BLOCKS ---
