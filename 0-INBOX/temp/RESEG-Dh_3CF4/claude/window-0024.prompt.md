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
ལོངས་སྤྱོད་པའི་དངོས་པོ་ཡང་རྣམ་པ་གཉིས་ཏེ། རྫས་ལ་ཉེ་བར་ལོངས་སྤྱོད་པའི་དངོས་པོ་དང་། འཁྲིག་པ་ལ་ཉེ་བར་ལོངས་སྤྱོད་པའི་དངོས་པོར་བཤད་དེ། དེ་གཉིས་ཀྱང་གོ་རིམས་ཇི་ལྟ་བ་བཞིན་དུ་རང་བཞིན་གྱིས༌[^470]ཕུན་སུམ་ཚོགས་པ་དང་། ཉེ་བར་ལོངས་སྤྱོད་པའི་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 842]
འབྲས་བུ་གྲུབ་པ་བཟང་པོ་ཞེས་བྱ་བ་ནི་འབྲས་བུ་ཕུན་སུམ་ཚོགས་པ་སྟེ། བཟང་པོ་ནི་མཛེས་པའོ། །

[Block 843]
ཟན་དྲོན་ཆང་གཅིག་ཅེས་བྱ་བ་ནི་སྔར་བཤད་པས་མཚོན་པར་བྱའོ། །

[Block 844]
བློན་པོ་ཆེན་པོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཉིད་སྨོས་པ་ནི་ཐག་ཉེ་བ་ན་སྤྱོད་པ་དང་། རིགས་མཐོ་བ་ཕུན་སུམ་ཚོགས་པ་དང་། གློ་བ་ཉེ་ཞིང་ཞུ་བར་ནུས་པའོ། །

[Block 845]
སྨྲ་བའི་སྤོབས་པ་ནི་སྨྲ་བར་ནུས་པའོ། །

[Block 846]
ཐོགས་པ་མེད་པ་ནི་སྨྲ་བ་ཐོགས་པ་གང་ཡང་མེད་པ་གང་ལ་ཡོད་པའོ། །

[Block 847]
དེ་སྨྲ་བ་ནི་ཐོགས་པ་མེད་པས། གཏམ་གླེང་བའི་སྐབས་ནི་གཏམ་གླེང་བའི་དུས་སྐབས་ཏེ། དེ་བབ་པ་ནི་དེ་ཉིད་ལ་བབ་པའོ། །

[Block 848]
ངེས་པར་ནི་དུས་རྟག་ཏུའོ། །

[Block 849]
གསུང་བ་ནི་ཞེས་བྱ་བའི་དོན་ནི་གང་བཤད་པའི་ཚིགས་བཅད་དོ། །

[Block 850]
དེ་སྐད་ཅེས་བྱ་བ་འདི་ཚིགས་བཅད་གཉིས་སོ། །

[Block 851]
ངོ་མཚར་ཆེ་བ་དང་། རབ་ཏུ་གཡེང་བ་ནི་ངོ་མཚར་ཆེ་བས་རབ་ཏུ་གཡེངས་པའོ། །

[Block 852]
དེའི་དོན་ཐོས་པ་མངོན་པར་འདོད་པས་རབ་ཏུ་གཡེངས་པའམ། དེའི་དོན་ཡོངས་སུ་ཤེས་པར་འདོད་པས་སོ། །

[Block 853]
སྐྱེ་བོ་ནི་བློན་པོ་ལ་སོགས་པའི་མཚོན་པའོ། །

[Block 854]
ཡང་ན་བདག་ཉིད་ལ་སྟོན་ཅིག་པ་སྟེ། གཞན་ལ་བསྟན་དུ་མི་རུང་བར༌[^471]མངོན་པར་འདོད་པའི་དོན་འདྲི་བ་སྟེ། དེ་བས་ན་གསལ་བར་དྲིས་པའོ། །

[Block 855]
མི་བསྒྲག་ཅེས་བྱ་བ་ནི༌[^472]དོགས་པ་བསུ་ནས་སྨྲས་པ་སྟེ། གསང་ན་ཞེས་བྱ་བ་འདིའི་དོན་ཡིན་ནོ། །

[Block 856]
གསང་བ་ནི་གསལ་བར༌[^473]མི་བསྒྲག༌[^474]པའོ། །

[Block 857]
གྲགས་པ་ཞེས་བྱ་བ་ནི་གསལ་བར་བདག་གིས་དྲིས་པའོ། །

[Block 858]
དེ་དགའ་ཞིང་རབ་ཏུ་བྱམས་པས་ཞེས་བྱ་བ་ནི་ལྷག་པར་དགའ་ཞིང་བྱམས་པ་ཉིད་དེ། སྔ་མ་བས་ཀྱང་ད་ལྟར་རབ་ཏུ་བྱམས་པ་སྟེ། བྱམས་པ་ནི་མངོན་པར་འདོད་པ་ཡང་དག་པར་བསྒྲུབས་པས་སོ། །

[Block 859]
བྱམས་པའི་ལྟབས་བཞིན་གསལ་ཞིང་དགའ་བའི་མཚན་མས་ཕྱོགས་གཅིག་ཏུ་ཟུར་གྱིས་ལྟ་ཞིང་དང་བའི་ལྟ་བས་ཏེ་དགའ་བའི་མཚན་མ་དག་གིས་སོ། །

[Block 860]
དོན་དང་རྒྱུ་མཚན་མ་ཕྱེ་བར་ཞེས་བྱ་བ་ལ་རྒྱུ་མཚན་དང་དོན་ནི་དོན་དང་རྒྱུ་མཚན་ནོ། །

[Block 861]
གང་གི་དོན་དང་རྒྱུ་མཚན་མ་ཕྱེ་བར་སྨྲས་པ་དེ་ནི་དོན་དང་རྒྱུ་མཚན་མ་ཕྱེ་བར་རོ། །

[Block 862]
རྒྱུ་མཚན༌[^475]ཅི་ཞིག་བསྟན་པ་དང་། འདིའི་དོན་ཅི་སྟོན་པ་སྟེ། དེ་ལྟར་མ་ཕྱེ་བར་སྨྲས་པའོ། །

[Block 863]
ངོ་མཚར་ཆེ་བ་དང་ཡིད་གཡོས་པ་ནི་སྔར་བསྟན་པ་གང་ཡིན་པ་སྟེ། ངོ་མཚར་ཆེ་བས་རབ་ཏུ་གཡེངས་བར་གྱུར་ཞེས་བྱ་བར་བསྟན་པ་ཡིན་ནོ། །

[Block 864]
ངོ་མཚར་ཆེན་པོས་རབ་ཏུ་གཡོས་པར་གྱུར་པ་ནི་བསྐྱོད་པ་སྟེ། ངོ་མཚར་ཆེན་པོས་རབ་ཏུ་གཡོས་པར་གྱུར་པ་ཉིད་རབ་ཏུ་གཡེངས་པ་ཡིན་ནོ། །

[Block 865]
ཡིད་ནི་སེམས་ཏེ་ངོ་མཚར་ཆེན་པོས་རབ་ཏུ་གཡོས་པའི་ཡིད་དོ། །

[Block 866]
གང་གི་ཕྱིར་ཞེས་བྱ་བ་ནི་གང་གི་རྒྱུའམ༌[^476]གང་གི་མཚན་མའོ། །

[Block 867 [VERSE]]
ཞིག་ཏུ་ཞེས་བྱ་བ་ནི་སྐྱེས་པའོ། །
འདིར་ཞེས་བྱ་བ་ནི་འདི་ཉིད་དུའོ། །
ནོར་ཙམ་གྱིས་ནི་མཐོ་བ་ལ། །

[Block 868]
ཞེས་བྱ་བ་ནི་ཚུལ་ཁྲིམས་ལ་སོགས་པའི་ཡོན་ཏན་ནི་མ་ཚང་བ་ཞེས་བྱ་བའི་དོན་ཏེ། [^477]ལས་དག་གིས༌[^478]མགུ་བ་ནི་ལས་ཀྱིས་མགུ་བ་སྟེ། དེས་སྒྲུབ་པ་ནི་བྱས་པའོ། །

[Block 869]
དམན་ཚིས༌[^479]ཀྱིས་འཚོ་བ་གང་ཡིན་པ་དེ་ནི་ལས་ཀྱིས༌[^480]མགུ་བར་བྱས་ནས་དམན་ཚིས་ཀྱིས་འཚོ་བ་སྟེ། ལུས་ངག་གི་འཚོ་ཞིང་སྤྱད་པར༌[^481]བྱེད་པ་ནི་འཚོ་བའོ། །

[Block 870]
དེའི་འབྱོར་པ་དམན་ཞིང་། ཞུས་པ་སྐྱེད་པར་བྱད་པ་ཡིན་པས་དམན་ཚིས་སོ། །

[Block 871]
གླ་འདིས་སྲོག་བཟུང་བ་ཡིན་པས་གླ་མི་སྟེ། གཞན་དག་གིས༌[^482]ལས་བྱེད་པས་ན་སེམས་ཀྱིས་བསམས་ཤིང་དེ་ལ་ཞུགས་ཏེ་ཞེས་བྱ་བ་ནི་ཞུགས་པར་གྱུར་པའོ། །

[Block 872]
མཚན་ཉིད་ཇི་ལྟ་བུ་ཞེ་ན། བརྙས་ཤིང་ཞེས་བྱ་བ་ཡིན་ཏེ། གཞན་གྱིས༌[^483]ཁྱད༌[^484]དུ་གསད་པའི་གཞིར་གྱུར་པའོ། །

[Block 873]
ངལ་བ་ནི་རང་གི་ལུས་ཡོངས་སུ་དུབ་པར་གྱུར་པའོ། །

[Block 874]
དམན་པ་ནི་སེམས་ཞུམ་པའོ། །

[Block 875]
དེས་བརྙས་ཤིང་ངལ་བ་དམན་པའི་གནས་ནི་བརྙས་ཤིང་ངལ་བ་དམན་པའི་གནས་ཏེ། གནས་དེས་ཡོངས་སུ་བརྙས་ཤིང་ངལ་བ་ཡིན་པས་སོ། །ཅིའི་ཕྱིར་དེ་ལྟར་ཉེས་པས་མ་རུང་བ་དེ་ལ་འཇུག་ཅེ་ན། སྨྲས་པ། མི་འཚོར་དོགས་ནས་ཞེས་བྱ་བ་ཡིན་ཏེ། འཚོ་བ་མེད་པས་འཇིགས་པས་སོ། །

[Block 876]
དབང་པོ་དུལ་ཞིང་ཞེས་བྱ་བ་ནི་དབང་པོ་བསྲུང་ཞིང་བསྡམས་པ༌[^485]ཡིན་པར་སྟོན་ཏོ། །

[Block 877]
དགེ་སློང་དཔལ་གྱི་རྗེས་འབྲང་བཞིན། །ཞེས་བྱ་བ་ནི་ཀུན་ཏུ་ལྟ་བ་དང་། རྣམ་པར་ལྟ་བ་དང་། སྣམ་སྦྱར་དང་། ལྷུང་བཟེད་དང་། ཆོས་གོས་འཆང་བ་ལ་སོགས་པ་ཇི་ལྟར་མདོ་སྡེ༌[^486]ལས་གསུངས་པ་བཞིན་དུ་རིག་པར་བྱའོ། །

[Block 878]
བཞི་ཞེས་སྨོས་པས་ནི་དགེ་འདུན་གྱི་ཚོགས་དང་རྗེས་སུ་མཐུན་པར་བསྟན་པའི་ཕྱིར་རོ། །

[Block 879]
འདིས་ནི་སྣོད་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 880]
དང་ཞིང་འཇམ་པ་ཞེས་བྱ་བ་ལ་དང་བ་ནི་དད་པའི་གཞི་སྟེ་འཇམ་པ་ཞེས་བསྟན་པ་ཡིན་ནོ། །
--- END BLOCKS ---
