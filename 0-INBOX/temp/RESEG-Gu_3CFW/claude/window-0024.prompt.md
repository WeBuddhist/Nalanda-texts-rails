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
[Block 841]
ཚ་བར་ནི་བསིལ་བ༌[^745]སྦྱར་རོ། །

[Block 842]
བསིལ་ཡབ་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་ལ། རླུང་བསྐྱབ་པར་བྱའོ་ཞེས་བྱ་བ་ནི་བསིལ་ཡབ་བོ། །

[Block 843]
འདིར་བཅོས་མ་ཉིད་ནི་གཙོ་བོ་སྟེ། གང་ཟག་ནི་མ་ཡིན་ནོ། །

[Block 844]
དེ་བས་ན་མ་ཞེན་པར་བྱས་པ་ནི་འདིར་མ་བསྡུས་པ་ཉིད་དོ། །

[Block 845]
བསིལ་ཡབ་མཁན་གྱིས་བྱས་པ་དང་། ཏ་ལའི་ཆང་བུའོ་ཞེས་བྱ་བ་ནི་སྐྱེད་པའི༌[^746]ཆ་བྱད་ནི་ཏ་ལའི་ལོ་མའི་ཚོགས་ཡིན་པའི་ཕྱིར་རོ། །

[Block 846]
ཁྲ་ཁྲ་བོ་མི་རུང་ངོ་ཞེས་བྱ་བ་ལ། འདི་ན་དབྱིག་པར་གཏོགས་པའི་ལུས་སྤྱི་ལ་བསྙེགས་ཏེ། དེའི་ཕྱིར་ལྷག་མའི་དོན་དུ་འདིའོ། །

[Block 847]
དགེ་འདུན་གྱིས་ནི་གཞན་ཡང་ངོ་ཞེས་བྱ་བ་ལ། དགེ་འདུན་གྱིས་ནི་བསིལ་ཡབ་མཁན་གྱིས་བྱས་པ་དང་ཏ་ལའི་ཆང་བུ་ལས་གཞན་ཀོ་ལྤགས་ལས་བྱས་པ་དང་རྨ་བྱའི་གཤོག་པ་ལ་སོགས་པ་ལས་བྱས་པ་དང་། ཁྲ་ཁྲ་བོ༌[^747]མ་ཡིན་པ་ལས་གཞན་པ་ཁྲ་ཁྲ་བོར་འདུག་པ་དང་། ཡུ་བ་རྩི་ཅན་དང་ཁྲ་བོ་ཡང་བཅང་བར་བྱའོ་ཞེས་ཏེ་དབྱུག་པ་དེ་ལྟ་བུ་ནི་གང་ཟག་ལ་བཀག་པར་རིག་པར་བྱའོ། །

[Block 848]
ནོར་བུ་དང་རྔ་མའི་བསིལ་ཡབ་རྙེད་ན་མཆོད་རྟེན་ལ་དབུལ་ལོ་ཞེས་བྱ་བ་ནི་དེའི་ཆེད་དུ་འདི་རྙེད་པར་གྱུར་པ་བླངས་པ༌[^748]ཞེས་བྱ་བར་འདིར་རྣམ་པར་གཞག་པར་རིག་པར་བྱ་སྟེ། [^749]འདི་ནི་མ་མོ༌[^750]དག་ལས་སོ། །

[Block 849]
མཆོད་རྟེན་ཀུན་ལ་ཡིན་ནམ་ཅི་སངས་རྒྱས་ཁོ་ནའི་ལ་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་ཉན་ཐོས་ཀྱི༌[^751]ལ་ཡང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སངས་རྒྱས་ཀྱི་འབའ་ཞིག་ཏུ་མ་ཟད་དོ། །

[Block 850]
འདིར་གཞུང་ནི་དགེ་སློང་གིས་རྔ་མའི་བསིལ་ཡབ་ནོར་བུ་ཅན་བཅང་བར་མི་བྱའོ། །

[Block 851]
ཇི་སྟེ་རྙེད༌[^752]ན་བླངས་ཏེ་སངས་རྒྱས་ཀྱི་མཆོད་རྟེན་ནམ་ཉན་ཐོས་ཀྱི་མཆོད་རྟེན་ལ་དབུལ་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 852]
སྟན་ནང་ཚངས་ཅན་དང་ལ་བ་དང་སྔས་ནང་ཚངས་ཅན་དང་གོར་བུ་དག་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་མ་མོ་ལས།

[Block 853]
དགེ་སློང་རྣམས་ཀྱིས་གནས་མལ་དང་། སྟན་གྱི༌[^753]རྗེས་སུ་གནང་བ་ནི༌[^754]འདི་ལྟ་སྟེ། ཁྲི་དང་ཁྲིའུ་དང་སྟན་ནང་ཚངས་ཅན་དང་ལ་བ་དང་སྔས་ནང་ཚངས་ཅན་དང་། གོར་བུ་དང་བགོ་བའི་དགེ་འདུན་གྱི་ཡང་རུང་གང་ཟག་གི་ཡང་རུང་བའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 854]
བུ་དང་ཆུང་མའི་རྙེད་པ་ནི་སྦྱིན་པར་བྱེད་པའི་དབང་གིས་བསྒྲུབ་པོ་ཞེས་བྱ་བ་ནི་སྦྱིན་པར་བྱེད་པས་ཇི་ལྟར་རྣམ་པར་ངེས་པ༌[^755]བྱེད་པ་དེ་བཞིན་དུ་འདི་ལ་རྣམ་པར་ངེས་པར་བྱ་སྟེ། སིལ་བུ་དག་ལས་དེ་དང་པོར་བྱས་ནས་གཞན་ཞེས་བྱ་བའི་མཐར་ཐུག་པ་དང་། སྣོད་སྤྱད་སྦེད་པ་ཞེས་བྱ་བ་དང་པོར་བྱས་ཏེ་འདུག་པར་བྱའོ་ཞེས་བྱ་བའི་མཐར་ཐུག་པ་དང་། དཀོན་མཆོག་གི་དོན་དུ་ཞེས་བྱ་བ་དང་པོར༌[^756]བྱ་སྟེ། འཁོར་ལོ་བཅང་བར་བྱའོ་ཞེས་བྱ་བའི་མཐར་ཐུག་པ་དང་། བཅུ་སྟོན་ལ་སོགས་པའི་རྙེད་པ་ཞེས་བྱ་བ་དང་པོར་བྱ་སྟེ། འཆང་བ་བསྟན་པ་ཞེས་བྱ་བའི་མཐར་ཐུག་པའོ། །

[Block 855]
འདིར་གཞུང་ནི་མ་མོ་དག་ལས།

[Block 856]
གླེང་གཞི་རྣམས་ལས་སྦྱར་བ་ཞེས་བྱ་བ་དང་པོར་བྱས་ནས་སྦྱིན་པ་ཞེས་བྱ་བའི་མཐར་ཐུག་པ་དང་། ལྷུང་བཟེད་ཅེས་བྱ་བ་དང་པོར་བྱ་སྟེ། བྱིན་གྱིས་བརླབ་པར་མི་བྱའོ་ཞེས་བྱ་བའི་མཐར་ཐུག་པར༌[^757]གསུངས་པ་ཡིན་ནོ། །

[Block 857]
གལ་ཏེ་སླུ་བར༌[^758]བྱེད་ན་ཇི་ཙམ་དུ་འདོད་པ་དེ་ཙམ་དུ་བཙོང་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། གལ་ཏེ་སླུ་བར༌[^759]བྱེད་ན་ཞེས་བྱ་བ་གལ་ཏེ་སྦྱིན་པར་བྱེད་པས་རང་གི་བུ་དང་ཆུང་མ་ཕུལ་བ་ཕྱིར་སླུ་བར༌[^760]འདོད་ནའོ། །

[Block 858]
ཇི་ཙམ་དུ་འདོད་པ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བ་ནི་སྦྱིན་པར་བྱེད་པ་ལའོ། །

[Block 859]
དེ་ཙམ་དུ༌[^761]བཙོང་བར་འདོད་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ཇི་ཙམ་དུ་བུ་དང་ཆུང་མ་སྦྱིན་པར་འདོད་པས་སླུ་བར༌[^762]འདོད་ན། སྦྱིན་པར་བྱེད་པ་དེ་རིན་ཇི༌[^763]ཙམ་དུ་འདོད་པ་དེ་ཙམ་དུ་བཙོང་བ་ཉིད་ཡིན་ནོ། །

[Block 860]
ཡང་དང་ཡང་འབུལ༌[^764]དུ་རུང་བའོ་ཞེས་བྱ་བ་ནི་ཕུལ་ཟིན་པའི་དངོས་པོ་ལེན་པ་པོ་ཉིད་ལ་ཡང་དང་ཡང་འབུལ༌[^765]དུ་རུང་བ་སྟེ། སྦྱིན་པར་བྱེད་པའི་དད་པ་སྤེལ་བའི་ཕྱིར་རོ། །

[Block 861]
ཤིང་ལྗོན་པ་ལ་ཕུལ་ན་གལ་ཏེ་རྒྱན་ཡིན་ན་གལ་ཏེ་དུས་སྟོན་གྱི་ཚེ་དེ་ཉིད་བརྒྱན་པའི་ཕྱིར་གཞག་གོ་ཞེས་བྱ་བ་ལ། དེ་ཉིད་ཅེས་བྱ་བ་ནི་ཤིང་ལྗོན་པ་དེ༌[^766]ཉིད་དོ། །

[Block 862]
དུས་སྟོན་གྱི་ཚེ་དེ་ཉིད་བརྒྱན་པའི་ཕྱིར་གཞག་གོ་ཞེས་བྱ་བ་ནི་དེ་དང་རིགས་མཐུན་པ་གཞན་མེད་ན་རིགས་མི་མཐུན་པ་གཞན་བརྒྱན་པའི་ཕྱིར་གཞག་པ་ལ་ལྟུང་བ་མེད་དོ། །

[Block 863]
ཡོངས་སུ་བཙལ་ནས་མ་རྙེད་ན་ཞེས་བྱ་བ་ཡང་ལྷག་མ་ཟ་བ་ལ་སྨོས་པའི་ཕྱིར་རྟོགས་པར་བྱའོ། །

[Block 864]
རྩིག་པ་ལ་གལ་ཏེ་གནས་ཁང་གི་ནི་རི་མོ་བྱ་བའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ལ། གལ་ཏེ་གནས་ཁང་ལ་ཕུལ་བར་གྱུར་ན། དེ་ནས་གནས་ཁང་གི་རྩིག་པ་ལ་རི་མོ་བྱ་བའི་ཕྱིར་གཞག་གོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 865]
འདིར་མེ་ཁང་ལ་སོགས་པར༌[^767]གཏོགས་པའི་རྩིག་པ་དང་ཀ་བ་དག་ལ་ཕུལ་བས་ལས་སར་པ་བྱ་ཞེས་བྱ་བའི་གཞུང་ཡང་། འདིར་རྩིག་པ་གནས་ཁང་གི་ཡིན་ལ་རྫས་དེ་གནས་ཁང་གི་ཡིན་ན་རྫས་དེ་གནས་ཀྱི་རྩིག་པའི་རི་མོ་བྲི་བའི་ཕྱིར་སྤྱད་པར་བྱའོ་ཞེས་གསུངས་པ་མཐོང་བ་ཡིན་ཏེ། དེ་གནས་ཁང་གི་རྩིག་པ་འདིར་བྱེ་བྲག་ཏུ་བརྗོད་པར་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 866]
གལ་ཏེ་དེ་མ་ཡིན་ནམ་ཀ་བ་ལ་ནི་ལས་སར་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་རྩིག་པ་དེ་གནས་ཁང་གི་མ་ཡིན་ནམ་ཀ་བ་ལ་ཕུལ་ན་མཁར་ལེན་གྱི་ཕྱིར་གཞག་པར་བྱའོ། །

[Block 867]
ས་ལ་ནའོ་ཞེས་བྱ་བ་འདི་ནི་འོག་མ་རྣམས་ལ་སྦྱར་བར་བྱའོ། །

[Block 868]
མེ་ཁང་གི་ནི་སྣང་བར་རོ་ཞེས་བྱ་བ་ནི་མེ་བུད་པའི་མེ་ཁང་གི་ས་ལ་ཕུལ་བའི་རྫས་ནི་དགེ་འདུན་གྱི་སྣང་བ་གང་དང་གང་དུ་དགོས་པའི་རྒྱུར་སྤྱད་ཀྱི་མེ་ཁང་དེ་ཉི༌[^768]ཚེར་ནི་མ་ཡིན་ནོ། །

[Block 869]
ཡང་ན་སྣུམ་བག་གི་རྙེད་པར་རོ་ཞེས་བྱ་བ་ནི་མེ་ཁང་གི་ས་ལ་ཕུལ་བའི་རྫས་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 870]
རུང་བའི་ཁང་པའི་ནི་ན་བའི་སྨན་དུ་གཞག་གོ་ཞེས་བྱ་བ་ནི་ཕུལ་བའི་རྫས་དེའོ། །

[Block 871]
བཀད་སའི་ནི་ཟས་སུ་བྱའོ། །

[Block 872]
སྐྱེམས་མལ་གྱི་ནི་བཏུང་བར་རོ་ཞེས་བྱ་བ་ནི། སྐྱེམས་མལ་གྱི་ས་ལ་ཕུལ་བའི་རྫས་ནི་བཏུང་བར་བསྒྱུར་བར་བྱའོ། །

[Block 873]
བསྲོ་ཁང་གི་གནས་ཀྱི་ནི་བསྲོ་ཁང་གི་ལམ༌[^769]སྣུམ་བག་གི་རྙེད་པར་རོ། །

[Block 874]
འཁོར་གྱི་ཁྱམས་དང་དཔོང༌[^770]སའི་ར་བའི་ནི་སྣུམ་བག་གི་རྙེད་པར་རོ། །

[Block 875]
ཡང་ན་སྐྱེས་པའི་རབས་ཀྱི་སྡེ་བྲི་བར་རོ་ཞེས་བྱ་བ་ནི། དཔོང༌[^771]སའི་ར་བའི་རྣམ་པ་ཉིད་དང་། འཁོར་གྱི་ཁྱམས་ལ་ཆོས་ཀྱི་གཉེར་ལ་དབང་བྱེད་པ་ཕལ་ཆེར་དེ་དག་གནས་པ་ཞེས་བྱ་བས་སྐྱེས་པའི་རབས་ཀྱི་སྡེ་བྲི་བར་རིགས་པ་ཡིན་ནོ་ཞེས་བྱ་བའི་དགོངས་པའོ། །

[Block 876]
བང་རིམ་དང་འཆག་ས་དང་སྒོ་ཁང་དང་། ཁྱམས་དག་ལ་ཕུལ་བའི་སྣོད་སྒོའོ། །

[Block 877]
རྫིང་བུའི་ཡང་ངོ་ཞེས་བྱ་བ་ནི། སྣོད་སྒོ་ཁང་ཞེས་བྱ་བ་འདོན་པ་འདི་འདིར་འདོན་པར་འདོད་པ་ཉིད་ཀྱིས་ཉེ་བར་བཏགས་པའོ། །

[Block 878]
ཁ་ཅིག་ལས་དེ་ནི་ཕྱོགས་བཞིའི་དགེ་འདུན་གྱི་ཉིད་དུ་གཞག་གོ་ཞེས་བྱ་བ་ལ། དེ་ནི་ཞེས་བྱ་བ་ནི་རྫིང་བུ་ལའོ། །

[Block 879]
ཁ་ཅིག་ལས་ཞེས་བྱ་བ་ནི་འདོད་པའོ། །

[Block 880]
དཀོན་མཆོག་གི་དོན་དུ་བླང་དུ་རུང་ངོ་། །བསྒྲག་ཏུ་ཡང་ངོ་ཞེས་བྱ་བ་ནི། དགེ་སློང་གི་བྱར་མི་རུང་བ་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །གང་གི་ཚེ་བསྒྲགས༌[^772]པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་ལེན་པའི་ཚེའོ་ཞེས་སྨོས་ཏེ། རྙེད་པ་འབུལ་བ་ལེན་པའི་ཚེ་ནའོ་ཞེས་བྱ་བའི་དོན་གྱིས་སོ། །
--- END BLOCKS ---
