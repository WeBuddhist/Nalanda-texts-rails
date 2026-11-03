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
[Block 736]
གང་ལ་གེགས༌[^313]ཡོད་པ་དེ་ནི་མི་སྐྱེ་བས་མ་སྐྱེས་པའི་ཕྱིར་བསྒྲིབས་པ་མི་མཐོང་ངོ་། །འོ་ན་གང་མདོ་ལས།

[Block 737]
གང་མིག་གིས་གཟུགས་རྣམས་མཐོང་ནས་ཞེས་གསུངས་སོ། །

[Block 738]
དེར་ནི་དགོངས་པ་ནི་དེ་ལ་བརྟེན་ཏེ་ཞེས་བྱ་བ་འདི་ཡིན་ཏེ། དཔེར་ན་ཡིད་ཀྱིས་ཆོས་རྣམས་རྣམ་པར་ཤེས་པར་བྱས་ནས་ཞེས་གསུངས་པ་ལྟ་བུའོ། །

[Block 739 [VERSE]]
ཡིད་ནི་འདས་པ་ཡིན་པའི་ཕྱིར། །
ཆོས་རྣམས་རྣམ་པར་མི་ཤེས་སོ། །
འོ་ན་ཅི་ལྟར༌[^314]ཞེ་ན།
ཡིད་ཀྱི་རྣམ་པར་ཤེས་པས་སོ། །

[Block 740]
ཡང་ན་བརྟེན་པའི་ལས་བརྟེན་ལ་ཉེ་བར་བཏགས་པ་ཡིན་ཏེ། དཔེར་ན་ཁྲིའུ༌[^315]དག་འབོད་དོ་ཞེས་གསུངས་པ་ལྟ་བུའོ། །

[Block 741]
ཇི་ལྟར་མདོ་ལས།

[Block 742]
མིག་གི་རྣམ་པར་ཤེས་པས་ཤེས༌[^316]པར་བྱ་བའི་གཟུགས་ཡིད་དུ་འོང་བ་སྡུག་པ་རྣམས་ཞེས་གསུངས་པ་ལྟ་བུ་སྟེ། དེ་དག་མིག་གིས་རྣམ་པར་མི་ཤེས་སོ། །

[Block 743]
མདོ་ལས།

[Block 744]
བྲམ་ཟེ་མིག་ནི་འདི་ལྟ་སྟེ། གཟུགས་རྣམས་མཐོང་བར་བྱ་བ་ལ་སྒོ་ཡིན་ནོ་ཞེས་ཀྱང་གསུངས་ཏེ། དེའི་ཕྱིར་མིག་གི་སྒོ་ནས་མིག་གི་རྣམ་པར་ཤེས་པས་མཐོང་ངོ་ཞེས་བྱ་བར་ཁོང་དུ་ཆུད་དོ། །

[Block 745]
དེར་ནི་ལྟ་བ་ལ་སྒོ་ཞེས་བྱ་བར་ཟད་དོ། །

[Block 746]
མིག་ནི་གཟུགས་རྣམས་མཐོང་བར་བྱ་བ་ལ་ལྟ་བ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་ནི་མི་རུང་ངོ་། །

[Block 747]
གལ་ཏེ་རྣམ་པར་ཤེས་པས་མཐོང་ན་གང་གིས་རྣམ་པར་ཤེས་ཤེ་ན། འདི་གཉིས་ལ་ཁྱད་པར་ཡང༌[^317]ཅི་ཞིག་ཡོད་དེ། གང་གིས་གཟུགས་རྣམ་པར་ཤེས་པ་དེ་ཉིད་ཀྱིས་འདི་མི་མཐོང་མོད། དཔེར་ན་ཤེས་རབ་འགའ་ཞིག་ལ་མཐོང་ཞེས་ཀྱང་བྱ། རབ་ཏུ་ཤེས་པ༌[^318]ཞེས་ཀྱང་བྱ་བ་དེ་བཞིན་དུ། རྣམ་པར་ཤེས་པ་འགའ་ཞིག་ལ༌[^319]མཐོང་ཞེས་ཀྱང་བྱ་སྟེ། [^320]རྣམ་པར་ཤེས་པ༌[^321]ཞེས་ཀྱང་བྱའོ། །

[Block 748]
གཞན་དག་ན་རེ་ནི་གལ་ཏེ་མིག་གིས་མཐོང་ན་མིག་བྱེད་པ་པོར་གྱུར་པའི་ལྟ་བའི་བྱ་བ་གཞན་གང་ཞིག་ཡིན་པ་བརྗོད་དགོས་སོ་ཞེས་ཟེར་རོ། །

[Block 749]
དེ་ནི་ཀླན་ཀར་མི་རུང་སྟེ། ཇི་ལྟར་རྣམ་པར་ཤེས་པས་ཤེས་སོ་ཞེས་བྱ་བར་འདོད་ལ། དེ་ལ་བྱེད་པ་པོ་དང་བྱ་བའི་བྱེ་བྲག་ཀྱང་མེད་པ་དེ་བཞིན་དུ་འདི་ལ་ཡང་རུང་བར་འགྱུར་རོ། །

[Block 750]
གཞན་དག་ན་རེ་ནི་མཐོང་བ་ནི་མིག་གི་རྣམ་པར་ཤེས་པ་ཡིན་ལ། མིག་ནི་དེའི་རྟེན་དུ་གྱུར་པའི་ཕྱིར་མཐོང་བ་ཞེས་བྱ་སྟེ། དཔེར་ན་སྒྲོགས་པའི་རྟེན་དུ་གྱུར་པའི་ཕྱིར་དྲིལ་སྒྲོགས་སོ་ཞེས་བྱ་བ་བཞིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 751]
དེ་ལྟར༌[^322]ན་མིག་གི་རྣམ་པར་ཤེས་པའི་རྟེན་དུ་གྱུར་པའི་ཕྱིར་རྣམ་པར་ཤེས་སོ་ཞེས་བྱ་བར་ཡང་འགྱུར་བ་མ་ཡིན་ནམ་ཞེ་ན། མི་འགྱུར་ཏེ། འཇིག་རྟེན་ན་རྣམ་པར་ཤེས་པ་དེ་ནི་མཐོང་བའོ་ཞེས་གྲགས་ཏེ། འདི་ལྟར་དེ་སྐྱེས་ན་གཟུགས་མཐོང་ངོ་ཞེས་ཟེར༌[^323]གྱི་རྣམ་པར་ཤེས་སོ་ཞེས་ནི་མི་ཟེར་རོ། །

[Block 752]
བྱེ་བྲག་ཏུ་བཤད་པ་ལས་ཀྱང་། མིག་དང་ཕྲད་ཅིང་རྣམ་པར་ཤེས་པས་ཉམས་སུ་མྱོང་བ་ལ་མཐོང་བ་ཞེས་བྱ་བའོ༌[^324]ཞེས་འབྱུང་སྟེ། དེ་ལྟ་བས་ན་མིག་གིས་མཐོང་བ་ཁོ་ན་ཞེས་བྱའི། རྣམ་པར་ཤེས་པ་ཞེས༌[^325]ནི་མི་བྱའོ། །

[Block 753]
རྣམ་པར་ཤེས་པ་ནི་ཡོད་པ་ཙམ་གྱིས་གཟུགས་རྣམ་པར་ཤེས་པས༌[^326]སོ་ཞེས་བྱ་སྟེ། དཔེར་ན་ཉི་མས་ཉིན་པར་བྱེད་དོ་ཞེས་བྱ་བ་བཞིན་ནོ། །

[Block 754]
མདོ་སྡེ་པ་རྣམས་ན་རེ་ནི་ནམ་མཁའ་ལྡན་པ༌[^327]འདིས་ཅི་དགོས། མིག་དང་གཟུགས་རྣམས་ལ་བརྟེན་ནས་མིག་གི་རྣམ་པར་ཤེས་པ་སྐྱེ་བ་དེ་ལ་ལྟ་བ་ནི་སུ་ཞིག་ཡིན། ལྟ་བ་ནི་གང་ཞིག་ཡིན་ཏེ། འདི་ནི་བྱེད་པ་མེད་པ་དང་ཆོས་ཙམ་དང་རྒྱུ་དང་འབྲས་བུ་ཙམ་དུ་ཟད་ལ། དེ་ལ་ཡང་ཐ་སྙད་དུ༌[^328]གདགས་པའི་དོན་དུ་འདུན་པའི་སྒོ་ནས་མིག་གིས་མཐོང་ངོ་། །རྣམ་པར་ཤེས་པས་རྣམ་པར་ཤེས་སོ་ཞེས་ཉེ་བར་འདོགས་པར་བྱེད་པས་འདི་ལ་མངོན་པར་ཞེན་པར་མི་བྱའོ། །

[Block 755]
བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་ལྗོངས་ཀྱི་མིའི་ཚིག་ལ་མངོན་པར་ཞེན་པར་མི་བྱའོ། །

[Block 756]
འཇིག་རྟེན་གྱི་མིང་ལ་མངོན་པར་བརྒྱུག་པར་མི་བྱའོ་ཞེས་གསུངས་སོ་ཞེས་ཟེར་རོ། །

[Block 757]
མིག་གིས་མཐོང་ངོ་། །རྣ་བས་ཐོས་སོ། །

[Block 758]
སྣས་ཚོར་རོ། །

[Block 759]
ལྕེས་མྱོང་ངོ་། །ལུས་ཀྱིས་རེག་གོ། །

[Block 760]
ཡིད་ཀྱིས༌[^329]རྣམ་པར་ཤེས་སོ་ཞེས་བྱ་བ་འདི་ནི་ཁ་ཆེ་བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ཀྱི་གྲུབ་པའི་མཐའ་ཡིན་ནོ། །

[Block 761 [HEADING]]
#### ཞར་ལ་འོངས་པ། ^1-3-19-0

[Block 762]
ཅི་མིག་གཅིག་གིས་གཟུགས་རྣམས་མཐོང་ངམ། འོན་ཏེ༌[^330]གཉི་གས་ཤེ་ན།

[Block 763 [HEADING]]
##### མིག་གཉི་གས་མཐོང་བ། ^1-3-19-1-0

[Block 764 [VERSE]]
འདི་ལ་ངེས་པ་མེད་དོ། །
[^331]མིག་ནི་གཉི་ག་དག་གིས་ཀྱང་། །
མཐོང་སྟེ་གསལ་བར་མཐོང་ཕྱིར་རོ། །

[Block 765]
ཆོས་མངོན་པ་པ་རྣམས་ན་རེ་མིག་གཉི་གས་ཀྱང་མཐོང་སྟེ། འདི་ལྟར་གཉི་ག་ཕྱེ་ན་གསལ་བར༌[^332]རབ་ཏུ་མཐོང་བར་འགྱུར་རོ། །

[Block 766]
མིག་གཅིག་ཕྱེ་ལ་གཉིས་པ་ཕྱེད་ཕྱེ་ན་ཟླ་བ་གཉིས་སུ་འཛིན་གྱི་གང་ཡང་རུང་བ་ཞིག་གཞན་དུ་གྱུར་ན་ནི་མ་ཡིན་ནོ། །

[Block 767]
རྟེན་རྣམ་པར་ཆད་པར་ཐལ་བར་ཡང་མེད་དེ། རྣམ་པར་ཤེས་པ་ནི་གཟུགས་བཞིན་དུ་ཡུལ་ན་མི་གནས་པའི་ཕྱིར་རོ་ཞེས་ཟེར་རོ། །

[Block 768 [HEADING]]
##### ཡུལ་དང་ཕྲད་པ་དང་མ་ཕྲད་པ། ^1-3-19-2-0

[Block 769]
གལ་ཏེ་མིག་གིས་མཐོང་བ་དང་རྣ་བས་ཐོས་པ་ནས་ཡིད་ཀྱི༌[^333]རྣམ་པར་ཤེས་པའི་བར་དུ་ཡིན་ན་ཅི་འདི་དག་ཡུལ་དང་ཕྲད་པ་ཞིག་གམ། འོན་ཏེ་མ་ཕྲད་པ་ཞིག་ཡིན་ཞེ་ན། མིག་དང་ཡིད་དང་རྣ་བ་ནི། ཡུལ་དང་མ་ཕྲད། འདི་ལྟར་གཟུགས་རྒྱང་རིང་པོ་ནས་མཐོང་ཞིང་མིག་ལ་ཡོད་པའི་མིག་སྨན་མི་མཐོང་ལ། དེ་བཞིན་དུ་སྒྲ་རྒྱང་རིང་པོ་ནས་ཐོས་སོ། །

[Block 770]
ཡུལ་དང་ཕྲད་པ་ཉིད་ཅིག་ཡིན་ན་ནི་འདི་ན་བསམ་གཏན་པ་རྣམས་ལ་ལྷའི་མིག་དང་། རྣ་བ་སྐྱེ་བར་མི་འགྱུར་ཏེ། སྣ་ལ་སོགས་པ་བཞིན་ནོ། །

[Block 771]
གལ་ཏེ་མིག་ཡུལ་དང་མ་ཕྲད་པ་ཡིན་ན་ཅིའི་ཕྱིར་ཐག་རིང་བ་དང་བར་དུ་ཆོད་པ་མ་ཕྲད་པ་ཐམས་ཅད་མི་མཐོང་ཞེ་ན། རེ་ཞིག་ཁབ་ལོང་གིས་ཀྱང་ལྕགས་མ་ཕྲད་པ་ཐམས་ཅད་ཇི་ལྟར་མི་འདྲེན། ཡུལ་དང་ཕྲད་པ་ཉིད་ཅིག་ཡིན་ན་ཡང་ཅིའི་ཕྱིར་མིག་སྨན་ནམ་ཐུར་མ་ཕྲད་པ་ཐམས་ཅད་མི་མཐོང་སྟེ་དེ་ནི་མཚུངས་སོ། །

[Block 772]
ཇི་ལྟར་ཡང་སྣ་ལ་སོགས་པ་ཡུལ་དང་ཕྲད་པ་ཡིན་ཡང་ལྷན་ཅིག་སྐྱེས་པའི་དྲི་ལ་སོགས་པ་མི་འཛིན་པའི་ཕྱིར་ཐམས་ཅད་ནི་མ་ཡིན་པ་དེ་བཞིན་དུ། མིག་ཀྱང་མ་ཕྲད་པ་ཡིན་མོད་ཀྱི་ཐམས་ཅད་ནི་མ་ཡིན་ནོ། །

[Block 773]
ཡིད་ནི་གཟུགས་ཅན་མ་ཡིན་པའི་ཕྱིར་ཕྲད་པ་ཉིད་དུ་མི་ནུས་སོ། །

[Block 774]
ཡང་ཁ་ཅིག་ནི་རྣ་བའི་ནང་དུ་ཡང་སྒྲ་ཐོས་པའི་ཕྱིར། རྣ་བ་ནི་ཡུལ་དང་ཕྲད་པ་དང་མ་ཕྲད་པ་ཡང་ཡིན་པར་སེམས་སོ། །

[Block 775]
ལྷག་མ་སྣ་དང་ལྕེ་དང་ལུས་ཞེས་བྱ་བ། གསུམ་གཞན་དུ།
--- END BLOCKS ---
