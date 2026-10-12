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
[Block 806]
ཐོས་པར༌[^370]བྱེད་པ་པོ་གང་ཡིན་ཞེ་ན། འཕགས་པ་ཕྱག་ན་རྡོ་རྗེ༌[^371]ཞེས་པ་སྟེ་དགོངས་པ༌[^372]ཐམས་ཅད་འབྱུང་བར་བྱེད་པའི་རྡོ་རྗེ་ཐོགས་པ་གང་ཡིན་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 807]
དེས་ཇི་སྐད་དུ་ཐོས་པ་ཐུགས་ལ་བཞག་ནས་ཞེས་པ་ནི་ལྷག་པ་དང་ཆད་པ་ལ་སོགས་པའི་ཉེས་པ་དང་བྲལ་བར་བྱས་ནས་ཞེས་པའི་དོན་ཏོ། །

[Block 808]
དེས་ཅི་བྱེད་ཅེ་ན། གདུལ་བྱ་རྣམས་ལ་བསྟན་པའི་ཕྱིར། །ཞེས་སྨོས་ཏེ་རང་གི་གདུལ་བྱ་སྨིན་པ་དང་གྲོལ་བར་བྱེད་པའི་ཕྱིར་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 809]
འདི་སྐད་བདག་གིས་ཐོས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ཏེ་ཞེས་བྱ་བ་ནི་སྡུད་པ་པོ་རང་གི་ཚིག་ལེགས་པར་སྟོན་པ་ཡིན་ཏེ། འདི་སྐད་ཐོས་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 810]
འདི་སྐད་ཅེས་བྱ་བ་འདི་ཡང་། ཇི་སྐད་ཅེས་བྱ་བའི་ཚིག་ཡིན་ནོ༌[^373]ཞེ་ན། དེའི་ཕྱིར་འདི་སྐད་ཅེས་བྱ་བ་ནི་རྒྱུད་ཀྱི་དོན་མ་ལུས་པར་སྟོན་པའི་ཚིག་གི་ཕྲད་དོ་ཞེས་སྨོས་ཏེ་འདིས་ནི་བཤད་པར་བྱ་བའི་ཆོས་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 811]
དེ་ཡང་འདི་ཞེས་བྱ་བ་ཡང་ཉེ་བ་མངོན་སུམ་པའི་ཚིག་གོ། །

[Block 812]
འདི་ཞེས་བྱ་བ་ཡང་གང་ཡིན་ཞེ་ན། གསལ་བ་དེའི་ཞེས་བྱ་བ་ནས་རྗེས་སུ་ཡི༌[^374]རང་ངོ་ཞེས་བྱ་བའི༌[^375]བར་དུའོ། །

[Block 813]
དེ་བས་ན་འདི་སྐད་ཅེས་བྱ་བ་འདི་ནི་རྒྱུད་ཀྱི་དོན་ཐམས་ཅད་རྗོད་པར༌[^376]བྱེད་པའི་ས་བོན་ཅན་ནོ། །

[Block 814]
གང་གིས་ཐོས་ཤེ༌[^377]ན་བདག་གིས་ཐོས་ཞེས་བྱ་བར་སྦྱར་ཏེ། བདག་གིས་ཐོས་ཞེས་བྱ་བས་ནི་སྡུད་པ་པོ་ཕུན་སུམ་ཚོགས་པ་སྟོན་ཏེ། བདག་ཉིད་ཀྱིས་མངོན་སུམ་དུ་ཐོས་ཞེས་བྱ་བ་ནི་བདག་ཉིད་ཀྱིས༌[^378]ཉེ་བར་ཐོས་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 815]
འདི་སྐད་ཐོས་ཞེས་པ་འདིས་ནི་མ་ཐོས་པ་དང་། གཞན་ཐོས་པ་རྣམས་བསལ་བ་ཡིན་ནོ། །

[Block 816]
བདག་གིས་ཐོས་ཞེས་བྱ་བས་ནི་མ་ཐོས་པ་དང་གཅིག་ནས་གཅིག་ཏུ་བརྒྱུད་དེ་ཐོས་པ་དང་རྟོགས་པ་བསལ་ལོ། །

[Block 817]
དུས་གཅིག་ན་ཐོས་ཞེས་པ་སྨོས་པས་ནི་དུས་ཐམས་ཅད་དུ་ཐོས་པ་དང་ཐམས་ཅད་དུ་མ་ཐོས་པ་བསལ་ལོ། །

[Block 818]
འདི་དག་གི་སྒྲའི་སྦྱོར་བ་ཡང་གཞན་དག་ནི་མ་ཐོས་ཀྱི་འདི་ཁོ་ན་སྐད་ཐོས་ཞེས་པ་དང་། འོངས་པ་དང་། རྟོགས་པ་ནི་མ་ཡིན་ཏེ་བདག་གིས་ཐོས་ཞེས་པ་དང་ཐམས་ཅད་དུ་མ་ཐོས་པ་དང་ཐམས་ཅད་དུ་ཐོས་པ༌[^379]ནི་མ་ཡིན་གྱི་དུས་གཅིག་ཁོ་ནར་དེ་ཐོས་ཞེས་བྱའོ།[^380] །དུས་ཕུན་སུམ་ཚོགས་པ་དེ་ཉིད་རྒྱས་པར་བཤད་པ་དུས་གཅིག་གི་ཚེ་ན་འདི་ན་འདི་ཐོས་ལ་གཞན་དུ་ནི་གཞན་ཐོས་པའོ་ཞེས་པ་ནི་གསང་བ་འདུས་པ་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱིས་གསུངས༌[^381]པའི་དུས་སུ་ནི་འདི་ཐོས་ཀྱི། ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སོགས་པ་གསུངས༌[^382]པའི་དུས་སུ་ནི་གཞན་ཐོས་ཤེའོ།[^383] །དེ་ཉིད་རྙེད་དཀའ་བར་བསྟན་པ་ཡང་། གཞན་དག་ཏུ་ནི་འདི་མ་ཐོས་པའོ་ཞེས་པ་སྟེ།[^384] གཞན་དུ་ནི་འདི་ནམ་ཡང་ཐོས་པར་མི་འགྱུར་བའོ། །དེ་ཅིའི་ཕྱིར་ཞེ་ན། བཅུ་བདུན་པར་གསང་བའི་སྣོད་དུ་མ་གྱུར་པ་ཉིད་ཀྱིས་བསྟན་ཏོ། །

[Block 819]
བློ་རྣོ་བ་ནི་སྐད་ཅིག་མ་གཅིག་ལའོ་ཞེས་པས་སྟོན་ཏོ། །

[Block 820]
སྐད་ཅིག་ལ་སོགས་པས་ནི་ཡུད༌[^385]ཙམ་ལ་སོགས་པ་མ་ཡིན་པར་བསྟན་ཏོ། །

[Block 821]
གང་ལས་གང་དུ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་འོག་ནས་སྟོན་ཏེ། སྟོན་པ་ཕུན་སུམ་ཚོགས་པ་ནི་སྟོན་པ་ཕུན་སུམ་ཚོགས་པ་སྟེ་ཡོན་ཏན་ཆེན་པོ་དང་ལྡན་པའི་སྟོན་པ་གང་ཡིན་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 822]
ཡོན་ཏན་གང་ཞིག་དང་ལྡན་ཞེ་ན། སྐལ་བ་ཕུན་སུམ་ཚོགས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། [^386]ཕུན་སུམ་ཚོགས་པ་ནི་ཡང་དག་པའི་དོན་གྱི་སྐལ་བ་ཆེན་པོ་དང་ལྡན་པ་སྟེ། མདོ་དག་ལས་དེ་བཞིན་གཤེགས་པ་ནི་སྒྲིབ་པ་མ་ལུས་པར་བཅོམ་པའི་ཕྱིར་སྐལ་བ་ཆེན་པོ་དང་ལྡན་པའོ་ཞེའོ། །

[Block 823]
གཞན་ཡང་གང་གིས་ཚོགས་ཆེན་པོ་ཡོངས་སུ་བསགས་པ་ནི་སྐལ་བ་ཆེན་པོ་དང་ལྡན་པའོ། །

[Block 824]
སྐལ་བ་ཆེན་པོ་ནི༌[^387]ཐམས་ཅད་དེ། སྐལ་བ་མ་ལུས་པའི་བདག་ཉིད་ཅན་ནོ། །

[Block 825]
མི་མཐུན་པའི་ཕྱོགས་མ་ལུས་པར་བཅོམ་པ་ནི་ས་ཐམས་ཅད་ལ་སྒྲིབ་པ་ཡང་དག་པའི་ཡེ་ཤེས་ཀྱིས་སྤངས་པའོ། །

[Block 826]
གཞན་ཡང་འདི་དག་གིས་ནི་མི་སློབ་པའི་ཟུང་དུ་འཇུག་པ་བསྟན་ཏོ། །

[Block 827]
དེ་ལྟ་བུའི་སྟོན་པ་དེས་གནས༌[^388]གང་དུ་གསུངས་ཤེ་ན་བཤད་པ། དེ་བཞིན་ཉིད་ནི་དེ་བཞིན་ཉིད་དེ་སྤྲོས་པ་དང་བྲལ་ཞིང་རྟོག་པ་ཐམས་ཅད་ལས་ཉེ་བར་གྲོལ་བའོ། །

[Block 828]
དེར་གཤེགས་པ་ནི་དེ་ལས་གྲོལ་བ་སྟེ། རྟོག་པ༌[^389]ཐམས་ཅད་ཡོངས་སུ་སྤངས་པ་དེ་ཉིད་མངོན་སུམ་དུ་གྱུར་པ་དང་ལྷུན་གྱིས་གྲུབ་པ་ཞེས་བྱ་བའི་བར་དུའོ། །

[Block 829]
དེ་བཞིན་གཤེགས་པ་ཡང་ཡིན་ལ་ཐམས་ཅད་ཀྱང་ཡིན་པ་ནི་སྤྲོས༌[^390]པའི་མཐའ་གཉིས་བསལ་བ་སྟེ། གྲངས་དང་གྲངས་ཅན་གཞན༌[^391]ལ་ཐལ་བ་ཡོངས་སུ་བསལ་བ་གང་ཡིན་པའོ། །

[Block 830]
བདག་ཉིད་ཅེས་པ་ནི་རང་བཞིན་ནམ་ངོ་བོ་ཉིད་དོ་ཞེས་པའི་དོན་ཏོ། །

[Block 831]
སྐུ་དང་གསུང་དང་ཐུགས་ཀྱི་སྙིང་པོ་ནི་ཡོངས་སུ་འཛིན་པ་ཞེས་བྱ་བའོ། །

[Block 832]
དེའི་བཙུན་མོ་ནི་དེས་བསྟེན་པ་སྟེ། གཞལ་ཡས་ཁང་གི་རྣམ་པ་ཉིད་ཡོངས་སུ་གསལ་བའོ། །

[Block 833]
དེར་གནས་པ་ནི་དེ་ཉིད༌[^392]ལ་བསྟེན་པ༌[^393]ཉིད་དོ། །

[Block 834]
དེ་བཞིན་ཉིད་དང་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་གང་གི་དུས་སུ་ཡོངས་སུ་སྣང་བ་ཉིད་དེ། རྣམ་གྲངས་དེས་ན་མ་འོངས་པའི་རྣལ་འབྱོར་པ་རྣམས་ཀྱིས་ཀྱང་ཇི་སྐད་འཆད་པར་འགྱུར་བའི་གཞལ་ཡས་ཁང་དུ་མོས་པའི་དཀྱིལ་འཁོར་དང་ཡོངས་སུ་བསྡུ་བའི་ཆོ་ག་དང་། རྣལ་འབྱོར་གསུམ་བསྒོམ་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 835]
ཡི་གེའི་དོན་ནི་སྒྲ་ཙམ་ལ་གཞོལ་བའི་དབང་དུ་བྱས་ཏེ་འདིའི་ཚེ་ཞེས་བྱ་བ་ལ་སོགས་པ་བྱ་བ་བཤད་པ་གོང་མ་ཉིད་དོ། །

[Block 836]
ཚོགས་ལ་བཤད་པ་ཡང་དེ་ཉིད་དེ་ཟབ་མོའི་དོན་མ་ཡིན་པ་ཉིད་དོ། །

[Block 837]
དེ་བས་ན་བཤད་པའི་སྒྲའི་དབང་དུ་བྱ་སྟེ་ཡི་གེའི་དོན་ཏོ། །

[Block 838]
བསྐྱེད་པའི་རྣལ་འབྱོར་གྱི་དབང་དུ་བྱས་ཏེ་ཚོགས་ལ་བཤད་པའོ། །

[Block 839]
གང་ཞིག་ལ་གང་ཞིག་གིས་གང་དུ་ཇི་ལྟར་གནས་པར་འགྱུར་བ་དང་། གང་གིས་གང་གི་སྤྱོད་ཡུལ་དུ་གང་བསྟན་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 840]
གཞན་ཡང་གང་གིས་གང་ཞིག་གཏན་ལ་འབེབས་པར་འགྱུར་བ་དང་། གང་གིས་གང་ཞིག་ཉམས་སུ་ལེན་པར་བྱེད་པ་དང་། གང་དང་གང་གིས་ཡུལ་དུ་བྱས་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

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
--- END BLOCKS ---
