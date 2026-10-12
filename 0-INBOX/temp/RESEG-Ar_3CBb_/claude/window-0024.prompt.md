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
དེ་ནི་རྫོགས་པའི་དོན་ཏོ། །

[Block 842]
གང་གིས་གང་གི་རྣམ་པར་བཤད་པ་ཡོངས་སུ་རྫོགས་པར་གྱུར་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 843]
དེ་ནས་སྤྱིའི་དོན་བཤད་པར་འདོད་ནས་སྨྲས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་སོ། །གང་ལ་གང་གིས་གང་དུ་གང་གི་ཕྱིར་ཞེ་ན། སྒྲའི་ཚོགས་འདི་ཡོངས་སུ་རྒོལ་བ་སྨྲ་བར་འགྱུར་རོ། །

[Block 844]
གང་དུ་ཞེས་པའི་ལན་དུ་འདི་ལྟ་སྟེ། ཡི་གེའི་དོན་བཤད་པ་ཡོངས་སུ་རྫོགས་པའི་སྐབས་འདིར་སྨྲས་པ། དགོངས་པ་གང་གིས་ན༌[^394]སྡུད་པར་བྱེད་པས་གསུང་རབ་ཀྱི་མགོར་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། འདི་དག་གི་དོན་ཡང་སྡུད་པ་པོས་གསུང་རབ་ཀྱི་སླད་དུ་འདི་སྐད་ཅེས་བསྟན་པ་ཁོ་ན་ལ་དགོངས་པ༌[^395]ཅི་ཞིག་ཡོད་པར་འགྱུར།

[Block 845]
བཅོམ་ལྡན་འདས་ཀྱིས་ཅི་ལ་དགོངས་ཏེ་གསུངས།

[Block 846]
གལ་ཏེ་རྒྱུད་ཀྱི་དོན་མཐའ་དག་བསྡུས་པར་འདོད་པའམ་དེ་ལས༌[^396]གཞན་དུ་འགྱུར་ཞེས་པ་རྒལ་བའི༌[^397]དོན་ཏོ། །

[Block 847]
དེའི་ལན་དུ་གོང་མ་ལྟར་གྱུར་ན་ཅིར་འགྱུར་ཞེ་ན་མ་ངེས་པར་འགྱུར་ཏེ། འདི་དག་བདག་གིས་ཤེའམ།[^398] འདིའམ་འདི་རྣམས་འདི་ཙམ་བདག་གིས་ཐོས་ཞེས་པས་ཀྱང་རྒྱུད་ཀྱི་དོན་མ་ལུས་པར་ཡོངས་སུ་རྫོགས་པར་སྟོན་པར་འགྱུར་ཏེ་དེར་འགྱུར་རོ། །

[Block 848]
གང་གིས་གང་ཞིག་གང་ལ་ནུས་པ་དེས་ཀྱང་དེའི་དོན་ཡོངས་སུ་རྫོགས་པར་འགྱུར་ན་ནི་ཁོ་ན་ཞེས་བྱ་བ་གཞན་དང་ལྡན་པ་རྣམ་པར་གཅོད་པ་རྟོགས་པར་འགྱུར་བ་མེད་པ་ཉིད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 849]
གང་གིས་གང་ཞིག་གང་ལ་ཡོངས་སུ་མ་སྤངས་པ་དེ་ནི་དེའི་བྱ་བ་ཡོངས་སུ་རྫོགས་པར་འགྱུར་རོ་ཞེ་ན་སྨྲས་པ་ཞེས་པ་དེ་ནི་ལན་སྟོན་པར་འགྱུར་བ་སྟེ། གང་ཡང་གང་ཞིག་ཡོངས་སུ་མ་སྤངས་པ་དེ་ནི་དེའི་ཉེས་པར་འགྱུར་བ་མ་ཡིན་ཏེ་དེ༌[^399]ཅིའི་ཕྱིར་ཞེ་ན། དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་བརྡར་གྱུར་པ་ནི་རྒྱུད་ཀྱི་སྟོན་པ་པོ་ཐམས་ཅད་ཀྱི་བརྡར་གྱུར་པ་ཉིད་དེ། བརྡ་གང་ཞིག་སྟོན་པའི་བརྡ་ཡིན་ཞེ་ན། ཤེས་རབ་དང་ཐབས་སྟོན་པ་ཉིད་དོ། །

[Block 850]
ཡི་གེ་གཉིས་སུ་གྱུར་པ་འདི་ཁོ་ནས་བརྡར༌[^400]སྟོན་པར་བྱེད་ཀྱི༌[^401]གཞན་གྱིས་ནི་ནམ་ཡང་རྙེད་པར་འགྱུར་བ་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 851]
གསུང་རབ་ཀྱི་དང་པོར་ཞེས་བྱ་བ་ནི་གང་ཞིག་གང་གིས་སྟོན་ནུས་པ་དེའི་ཕྱིར་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 852]
གང་གིས་དེ་ཡོངས་སུ་ཤེས་པར་འགྱུར་བ་དེས་ནི་དེ་དང་དེ་དག་ཡོངས་སུ་ཤེས་པར་འགྱུར་བ་ཉིད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 853]
གཞན་ཡང་གང་གིས་དེ་ཉིད་བསྟན་པར་འགྱུར་བ་དེ་ནི་དེའི་གཞུང་ལུགས་ཡོངས་སུ་རྫོགས་པ་མ་ཡིན་ཏེ་ཅིའི་ཕྱིར་ཞེ་ན། སྡུད་པ་པོ༌[^402]མེད་པར་འགྱུར་བའི་ཕྱིར་ཏེ། འདི་སྐད་ཅེས་བྱ་བ་འདི་སྡུད་པ་པོའི་ཚིག༌[^403]སྒྲ་ཇི་བཞིན་པ་མ་ཡིན་པར་འགྱུར་ཏེ། དེ་ལྟ་ན་སྡུད་པ་པོ་མེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 854]
དེས་ཅིར་འགྱུར་ཞེ་ན་བདག་གིས་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིག་འབྲེལ་པ་མེད་པར་འགྱུར་ཏེ་དེ༌[^404]ཅིའི་ཕྱིར་ཞེ་ན། འདི་སྐད་ཅེས་བྱ་བ་ནི་བརྡར་གྱུར་པ་ཉིད་ཡིན་ལ་བདག་གིས་ཞེས་བྱ་བ་ནི་སྡུད་པ་པོ་རང་གི་མིང༌[^405]བརྗོད་པས་ཐ་དད་པར་འགྱུར་རོ། །ཅིའི་ཕྱིར་ཞེ་ན། གང་ལ་གང་ཞིག་ཡོད་པ་དེ་ལ་དེ་དང་བྲལ་བར་འགྱུར་བའི་ཕྱིར་གཅིག་གིས་གཅིག་སྤངས་པར་འགྱུར་བ་ཡིན་ནོ། །

[Block 855]
དེས་ན་སྡུད་པ་པོ་མེད་པར་འགྱུར་རོ་ཞེ་ན། སྡུད་པ་པོ་མེད་པར་ཐལ་བར་འགྲུབ་པ་འདི་ནི་ཐལ་བ་མ་ཡིན་པ་ཉིད་དེ་གསང་བ་འདུས་པའི་དོན་འདིར་སྡུད༌[^406]པ་པོ་ནི་མེད་དོ། །

[Block 856]
འོ་ན་ཞེས་བྱ་བ་ནི་མགུ་བ་མ་ཡིན་པའི་ཚིག་བརྗོད་པ་ཉིད་དོ། །

[Block 857]
བཙུན་པ་ཀུན་དགའ་བོ་ལ་སོགས་པ་འཇིག་རྟེན་ན་སྡུད་པ་པོར་ཅིའི་ཕྱིར་གྲགས་ཞེས་པ་ནི་ལྔ་སྡེ་བཟང་པོ་ལ་སོགས་པ་གང་ཞིག་གིས་གང༌[^407]ཞིག་ཡོངས་སུ་བཟུང་བ་དང་སྡུད་པ་གཟིགས་པ་མངོན་སུམ་དང་འགལ་བར་འགྱུར་རོ། །

[Block 858]
གང་ཞིག་གང་གིས་ཡོངས་སུ་འདྲི་བ་མེད་ན་དེ་ཡང་མེད་པར་འགྱུར་བས་དེ་རྗེས་སུ་དཔག་པ་དང་ཡང་འགལ་བར་འགྱུར་རོ། །

[Block 859]
གསུངས་པ་ལན་ལ་སོགས་པ་གང་ཞིག་སྣང་བ་དང་། གང་ཞིག་ཡོངས་སུ་བརྗོད་པ་དང་། གང་དང་ཡོངས་སུ་མཐུན་པར་གྱུར་པ་དེའི་ཕྱིར་དེ་དག་དང་འགལ་བར་འགྱུར་རོ། །

[Block 860]
དེས་ན་སྡུད་པ་པོ༌[^408]ཡོད་པར་སྣང་བ་ཉིད་དེ། འདོད་པ་འདི་ཐམས་ཅད་ཡོངས་སུ་བཤིག་པ་ཡིན་ནོ་ཞེས་སྐྱོན་བརྗོད་པ་དང་སྐྱོན་ཡོངས་སུ་སྤང་བའི་ཕྱིར་སློབ་དཔོན་གྱིས་གང་ལ་ཡོངས་སུ་ལེགས་པར་སྨྲས་པ་དེ་དང་འགལ་བ་ལ་སོགས་པའི་ཉེས་པ་འདི་སྣང་བའམ་ངེས་པའི་དོན་དུ་འགྱུར། །སྣང་བ་ལ་ནི་ནམ་ཡང་མི་འདོད་པ་མ་ཡིན་པས་ཉེས་པ་མེད་པ༌[^409]ཉིད་དོ། །

[Block 861]
ཕྱི་མ་ལྟར་ན༌[^410]ནི་མི་འདོད་པ་ཉིད་དེ་ཀུན་དགའ་བོ་ནི་འདིར་བྱང་ཆུབ་སེམས་དཔའ་ཀུན་དུ་བཟང་པོ་ཉིད་དེ་ཕྱག་ན་རྡོ་རྗེ་ཡིན་ལ་ཞེས་པ་ནི་ཕྱི་དང་ནང་གི་སྡུད་པ་པོ་གཉིས་སུ་མེད་པར་བསྟན་ཏོ། །

[Block 862]
རྡོ་རྗེ་འཆང་ཆེན་པོ་ཡང་དེ་ཉིད་ལས་གཞན་མ་ཡིན་ཏེ་ཞེས་པ་ནི་གང་གིས་རྡོ་རྗེ་འཆང་ཆེན་པོ་དང་སྡུད་པ་པོ་ཐ་དད་དུ་དབྱེ་བ་མེད་པ་ཉིད་དོ། །

[Block 863]
དེས་ན་སྡུད་པ་པོ་དང་སྟན་པ་ནི་གང་གིས་གང་ཞིག་ཡོངས་སུ་འཛིན་པ་དེ་ཡང་དེ་ཉིད་དོ། །

[Block 864]
གལ་ཏེ་ཐ་དད་དུ་གནས་ན་ཅིར་འགྱུར་ཞེ་ན། མདོ་སྡེ་ལ་སོགས་པ་ནི་མདོ་སྡེ་དང་འདུལ་བ་དང་མངོན་པའོ། །

[Block 865]
ཆོས་ཀྱི་ཕུང་པོ་བརྒྱད་ཁྲི་བཞི་སྟོང་ནི་བཤད་ཟིན་ཏོ། །

[Block 866]
དེ་བཞིན་གཤེགས་པ་ལས་ཕྱག་ན་རྡོ་རྗེས༌[^411]ལྷག་ཆད་མེད་པར་ལན་གཅིག༌[^412]གིས་ཐོས་ཤིང་འཛིན་པར་ག་ལ་ནུས་ཞེས་པ་ནི་མི་སྲིད་པར་བསྟན་ཏོ།[^413] །འདི་ལྟར་རྫོགས་པའི་སངས་རྒྱས་མ་ཡིན་པ་ནི་མཐར་ཕྱིན་པའི་ས་ལ་མི༌[^414]གནས་པར་གྱུར་པ་དེ་ནི་གང་གིས་རྟོག་པ་མ་སྤངས་སོ། །

[Block 867]
[^415]རྟོག་པ་ཐམས་ཅད་སྤངས་པར་མ་གྱུར་པ་དེ་ནི་མཐར་ཕྱིན་པའི་ལམ་ལ་མི་གནས་སོ། །

[Block 868]
གང་གིས་རྟོག་པ་ཐམས་ཅད་མ་སྤང་བ༌[^416]དེ་ནི་ཐོགས་པ་མེད་པའི་ཤེས་རབ་དང་མི་ལྡན་ནོ། །

[Block 869]
ཐོགས་པ་མེད་པའི་ཤེས་རབ་ཀྱང་རྟོག་པ་སྤངས་པ་ལས་འབྱུང་བར་རིག་པར་བྱའོ། །

[Block 870]
ཐོགས་པ་མེད་པའི་ཤེས་རབ་མེད་པས་ནི་ཆོས་ཀྱི་ཕུང་པོ་བརྒྱད་ཁྲི་བཞི་སྟོང་ལྷག་ཆད་མེད་པར་ལན་གཅིག་གིས༌[^417]འཛིན་པར་མི་ནུས་སོ། །དེ་ཅིའི་ཕྱིར་ཞེ་ན། ཆོས་ཀྱི་ཕུང་པོ་བརྒྱད་ཁྲི་བཞི་སྟོང་ཡོངས་སུ་འཛིན་པ་ནི་ཐོགས་པ་མེད་པའི་ཤེས་རབ་མེད་ན་མེད་པའི་ཕྱིར་རོ་ཞེས་འབྱུང་བས་སྡུད་པ་པོ་ནི་རྫོགས་པའི་སངས་རྒྱས་ལས་ཐ་དད་དུ་མི་འཇུག་གོ། །

[Block 871]
དེ་ཡང་གང་ལས་ཤེས་ཤེ་ན། བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་འདི་ཉིད་དུ་ཐུན་མོང་མ་ཡིན་པའི་གསང་བ་ཞེས་བྱ་བ་རྣལ་འབྱོར་ཆེན་པོའི་རྒྱུད་ལས་གསུངས་ཞེས་སྨོས་སོ། །

[Block 872]
ཇི་སྐད་གསུངས་ཤེ་ན་འདི་ལྟ་སྟེ་ཞེས་པ་ནི་ཡོངས་སུ་སྟོན་པའི་དོན་ཏོ། །

[Block 873]
འཇམ་དཔལ་ནི་ཟས་གཙང་མར་གྱུར་ཏོ་ཞེས་བྱ་བ་ནི་གང་ལ་གང་གིས་འདུལ་བ་དེ་ལ་དེར་བསྟན་ཞེས་པའི་དོན་ཏོ། །

[Block 874]
འཇིག་རྟེན་དབང་ཕྱུག་ནི་ལྷ་མོ་སྒྱུ་འཕྲུལ་དུ་གྱུར་ཏོ་ཞེས་བྱ་བ་ནི་ལྷ་མོ་ཆེན་མོ་སྒྱུ་འཕྲུལ་ནི་འཇིག་རྟེན་དབང་ཕྱུག་གོ། །

[Block 875]
གཞན་ཡང་གང་གི་ཕྱིར་ལྷ་མོ་ཆེན་མོ་སྒྱུ་འཕྲུལ་ཉིད་ཀྱིས་གང་དུ་ཡོངས་སུ་འདུལ་བ་དེའི་ཕྱིར་དེ་ལ༌[^418]དེ་བསྟན་ཏོ། །

[Block 876]
བསྟན་པ་འདི་དག་གང་ཞིག་གང་གིས་ཇི་ལྟར་ཡོངས་སུ་སྣང་བ་དེ་ལྟར་གནས་པ་ནི་མེད་དོ།[^419] །

[Block 877]
དེ་ཅིའི་ཕྱིར་ཞེ་ན། ཐམས་ཅད་རོ་གཅིག༌[^420]པའི་རང་བཞིན་ཅན་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 878]
རིགས་པ་འདིས་ནི་ཞེས་པ་ནི་མི་སླུ་བར་བྱེད་པའི་ཚད་མ་དེ་ལྟ་བུ་ཡོད་པའི་ཕྱིར་རོ་ཞེས་སོ།

[Block 879]
[^421] །འོ་ན་དེ་ལྟར་བསྟན་པ་ལ་དགོས་པ་ཅི་ཡོད་ཅེ་ན། ལས་དང་པོ་པའི་སེམས་ཅན་རྣམས་འཇུག་པར་བྱ་བའི་ཕྱིར་ཞེས་པ་ནི་ལས་དང་པོ་པ་ནི་འཇིག་རྟེན་པ་དང་མཐུན་པའི་ཆོས་ལ་འཇུག་པར་འགྱུར་རོ། །

[Block 880]
འཇིག་རྟེན་ན་ནི་རྒྱལ་པོ་དང་། འཁོར་དང་ཞུ་བ་པོ་ལ་སོགས་པ་སྣང་བར་བྱ་བ་དང་མི་མཐུན་པར་སྟོན་ཏོ། །
--- END BLOCKS ---
