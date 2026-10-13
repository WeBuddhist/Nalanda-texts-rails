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
དེ་ལ་དང་པོ་སེམས་རྣམ་པར་དག་པའི་རིམ་པས་འོད་གསལ་བ་ཐོབ་པ་གང་ཡིན་པ་དེ་ལས་མི་དམིགས་པའི་སྙིང་རྗེའི་དབང༌[^486]གིས་འབད་པ་མེད་པར་རྣམ་པ་ཐམས་ཅད་ཀྱི་མཆོག་དང་ལྡན་པ། ཞལ་གསུམ་པ༌[^487]ལ་སོགས་པ་དང་ལྡན་པ། རིན་པོ་ཆེ་སྣ་ཚོགས་པའི་རང་བཞིན་གཞལ་ཡས་ཁང་པ་ལ་པདྨ་དང་ཟླ་བ་ལ་སོགས་པའི་གདན་ལ་བཞུགས་པ། དེ་བཞིན་གཤེགས་པ་དང་ལྷ་མོ་དང་བྱང་ཆུབ་སེམས་དཔའ་དང༌[^488]ཁྲོ་བོའི་ཚོགས་ཀྱིས་ཡོངས་སུ་བསྐོར་བ། དེའི་བ་སྤུའི་ཁུང་བུ༌[^489]ནས་བྱུང་བའི༌[^490]འོད་ཟེར་གྱི༌[^491]འཁོར་ལོས་ཁམས་གསུམ་པ་རྣམས་ཀྱི་རེ་བ་སྐོང་བར་བྱེད་ལ། ཡིད་བཞིན་གྱི༌[^492]ནོར་བུ་དང་དཔག་བསམ་གྱི་ཤིང་བཞིན་དུ་འདོད་པའི་དོན་སྟོབས་ཀྱིས་སྟེར་བར་བྱེད་པ་སར་ཞིང་སར་པའི་དཀྱིལ་འཁོར་གྱི་འཁོར་ལོ་སྤྲོས་པས་ནམ་མཁའི་དབྱིངས་མཐའ་མེད་པ་མ་ལུས་པ་ཁྱབ་པར་བྱེད་པ། རྡོ་རྗེ་འཆང་ཆེན་པོ་ལ་སོགས་པའི་ཕྱག་རྒྱ་ཆེན་པོའི་གཟུགས་མྱུར་དུ་སྤྲོས་ཏེ། དེ་ཉིད་སྒྱུ་མ་ལ་སོགས་པའི་དཔེ་བཅུ་གཉིས་ཀྱིས་ཡང་དག་པར་བལྟས་ཏེ། ཁམས་གསུམ་ཐམས་ཅད་ཀྱང་སྒྱུ་མ་ལྟ་བུར་ཤེས་ནས་སྔགས་དང་ཕྱག་རྒྱ་ལ་སོགས་པའི་སྦྱོར་བ་དང་། རབ་ཏུ༌[^493]གནས་པ་དང་། སྦྱིན་སྲེག་དང་། དཀྱིལ་འཁོར་དང་། བཟླས་པ་དང་། སྐུ་ཁྲུས་དང་། གཏོར་མ་དང་། སྤྱན་དྲང་བ༌[^494]དང་། བཞུགས་སུ་གསོལ་བ་དང་། གཤེགས་སུ་གསོལ་བ་དང་། རིམ་པ་གཉིས་བསྒོམ་པ་ལ་སོགས་པ་དང་། ཕྲིན་ལས་ཐམས་ཅད་དང་། དེ་བཞིན་དུ་ཡང་གར་དང་གླུ་དང་རོལ་མོ་དང་། སྒེག་པ་ལ་སོགས་པ་ལོངས་སྤྱོད་པ་དང་། ཇི་སྲིད་སྤྱོད་ལམ་བཞིའི་བར་དུ་སྒྱུ་མ་དང་དྲི་ཟའི་གྲོང་ཁྱེར་དང་། བྲག་ཅ༌[^495]དང་སྨིག༌[^496]རྒྱུ་དང་། ཆུ་ཟླ་དང་མེ་ལོང་གི་གཟུགས་བརྙན་དང་། ཆུ་ཤིང་དང་སེང་གེ་ཟླ་བའི་གྲོང་ཁྱེར་ལ་སོགས་པ་དང་འདྲ་བར་བལྟ་བར་བྱའོ། །

[Block 737]
ཏིང་ངེ་འཛིན་འདི༌[^497]སྤྱོད་པར་གྱུར་པའི་རྣལ་འབྱོར་པས་རང་དང་གཞན་གྱི་དོན་ཐམས་ཅད་འབད་པ་མེད་པར་འགྲུབ་པར་འགྱུར་རོ། །

[Block 738]
བསྐལ་པ་དང་བསྐལ་པ་སྟོང་གི་བར་དུ་གནས་པར་འགྱུར་རོ་ཞེས་འདི་ནི་མྱུར་བའི་ཏིང་ངེ་འཛིན་གྱིས་བདག་བྱིན་གྱིས་རློབ་པའི་རིམ་པ་གཅིག་གོ། །

[Block 739]
[^498]

[Block 740 [HEADING]]
##### གཉིས་པ་སྣང་བ་ཐོབ་པ་ལ་སོགས་པའི་རྣལ་འབྱོར། ^1-2-3-2-0

[Block 741]
གཉིས་པ་ནི་རེ་ཞིག་དང་པོ་སྤྲིན་མེད་པའི་ནམ་མཁའ་འདྲ་བའི་འོད་གསལ་བ་ལ་དམིགས་ཏེ། དེ་ལས་མཚམས་ཀྱི་སྣང་བ་དང་འདྲ་བའི་ཆོས་ཀྱི༌[^499]དབྱིངས་ཀྱི་འཁོར་ལོ་ལ་གནས་པའི་ཐིག་ལེ་ལ་བལྟས་ཏེ། དེའི་རྗེས་སུ་ཉི་མ་དང་རྡོ་རྗེའི་སྟེང་དུ་ཨཿཚེག་དྲག་ཅན་དམར་པོ་བསམས་ཏེ། དེའི་རྗེས་ལ་པདྨ་དང་ཟླ་བའི་དཀྱིལ་འཁོར་གྱི་སྟེང་དུ་ཐིག་ལེ་དང་བཅས་པ་དབྱངས་ཡིག་དང་པོ་དཀར་པོ་ལ་བལྟས་ཏེ། དེ་དག་ཐམས་ཅད་ཡོངས་སུ་གྱུར་པ་ལས་སྔ་མ་བཞིན་དུ་ལྷའི་གཟུགས་ཡོངས་སུ་རྫོགས་པ་ཞེས་བྱ་བའི་སྣང་བ་ཐོབ་པ་ལ་སོགས་པའི་རིམ་པས་བདག་བྱིན་གྱིས་རློབ་པའོ། །

[Block 742]
གལ་ཏེ་ཡང་ས་བོན་དང་མཚན་མ་ཡོངས་སུ་གྱུར་པ་ལས་བྱུང་བའི་རྣམ་པ་ཡིན་ཡང་། འོན་ཀྱང་སྒྱུ་མ་ལ་སོགས་པའི་དཔེ་རྣམས་ཀྱིས་ཉེ་བར་བརྒྱན་པས་ན་བསྐྱེད་པའི་རིམ་པ་ལས་ཁྱད་པར་དུ༌[^500]གྱུར་པའོ། །

[Block 743]
གང་གི་ཕྱིར་བསྐྱེད་པའི་རིམ་པ་ལས་སྒྱུ་མ་ཉིད་དུ་མཐོང་བ་མེད་དོ།[^501] །

[Block 744]
ལྷའི་ང་རྒྱལ་ཁོ་ན་དེར་བསྒྲུབ་པར་བྱ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 745]
ལྷའི་ང་རྒྱལ་དང་སྒྱུ་མ་ལྟ་བུར་མཐོང་བ་དག་ནི་ཕན་ཚུན་འགལ་བ་ཡིན་ནོ། །

[Block 746]
དེ་བས་ན་ལྷའི་རྣལ་འབྱོར་རྣམ༌[^502]པ་གཉིས་ཏེ། རྟོག་པ་དང་ཡོངས་སུ་རྫོགས་པའོ། །

[Block 747]
དེ་ལ་རྟོག་པའི་རྣལ་འབྱོར་ནི་ཟླ་བ་དང་རྡོ་རྗེ་ལ་སོགས་པ་ཡོངས་སུ་གྱུར་པ་ལས་སྐྱེས་པ། བསྐྱེད་པའི་རིམ་པའི་རྣལ་འབྱོར་པའི་སྤྱོད་ཡུལ་སྔགས་ཀྱི་སྐུའོ། །

[Block 748]
ཡོངས་སུ་རྫོགས་པའི་རྣལ་འབྱོར་ནི་མྱུར་བའི་ཏིང་ངེ་འཛིན་གྱིས་རྫོགས་པའམ། སྣང་བ་ཐོབ་པ་ལ་སོགས་པའི་རིམ་པ་ལས་བསྐྱེད་པའི་ཡེ་ཤེས་ཀྱི་སྐུ་ཡིན་པས་ཁྱད་པར་ཡོད་པ་ཁོ་ནའོ་ཞེས་བདག་ལ་བྱིན་གྱིས་རློབ་པའོ། །

[Block 749 [HEADING]]
#### མངོན་པར་བྱང་ཆུབ་པའི་རིམ་པ། ^1-2-4-0

[Block 750]
ད་ནི་སྒྱུ་མ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་ཡང་རྣམ་པར༌[^503]དག་པར་བྱ་བ་ཡིན་ཏེ། རྟོག་པ་དང་བཅས་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 751]
དེའི་ཕྱིར་དོན་དམ་པའི་བདེན་པའི་ངོ་བོ་ཉིད་མངོན་པར་བྱང་ཆུབ་པའི་རིམ་པས་དེ་བཞིན་ཉིད་ཀྱིས་སྦྱང་བར་བྱ་བའི་ཕྱིར་མངོན་པར་བྱང་ཆུབ་པའི་རིམ་པ་བསྟན་པར་བྱ་སྟེ། དེ་ལ་ཡང་རྣམ་པ་གཉིས་ཡིན་ཏེ། ཕྱག་རྒྱ་དང་། ཏིང་ངེ་འཛིན་གྱི༌[^504]བྱེ་བྲག་གིས་སོ། །

[Block 752]
ཕྱག་རྒྱའི་རིམ་པ༌[^505]ལ་རྣམ་པ༌[^506]གཉིས་ཏེ། ཕྱིའི་མངོན་པར་བྱང་ཆུབ་པ་དང་། ནང་གི་མངོན་པར་བྱང་ཆུབ་པའོ། །

[Block 753]
ཏིང་ངེ་འཛིན་གྱི༌[^507]མངོན་པར་བྱང་ཆུབ་པ་རྣམ་པ་གཉིས་ཏེ། རིལ་པོ་འཛིན་པ་དང་། རྗེས་སུ་གཞིག་པའོ། །

[Block 754 [HEADING]]
##### ཕྱག་རྒྱའི་རིམ་པ། ^1-2-4-1-0

[Block 755]
དེ་ལ་ཕྱག་རྒྱའི་རིམ་པ་བསྟན་པར་བྱ་སྟེ།

[Block 756 [HEADING]]
###### ཕྱིའི་མངོན་པར་བྱང་ཆུབ་པ། ^1-2-4-1-1-0

[Block 757]
དང་པོ་རེ་ཞིག་སྒྲུབ་པ་པོས་སློབ་དཔོན་དང་གསང་བའི་དབང་ཐོབ་པས་ཤེས་རབ་ཀྱི་དབང་བསྐུར་བ་ཐོབ་པར་བྱ་བའི་ཕྱིར་ཕྱི་དང་ནང་དང་གསང་བའི་མཆོད་པ་རྣམས་ཀྱིས་རྡོ་རྗེ་སློབ་དཔོན་མཆོད་པར་བྱ་སྟེ།

[Block 758 [VERSE]]
དེ་ལ་ཕྱིའི་མཆོད་པ་ནི་མཆོད་པ་རྣམ་པ་ལྔའོ། །
ནང་གི་མཆོད་པ་ནི་གོ༌[^508]ཀུ༌[^509]ད་ཧ་ན།
མ་ར་བི་ཤ༌[^510]མུ་ཞེས་བྱ་བའི་མཚན་ཉིད་དོ། །

[Block 759]
གསང་བའི་མཆོད་པ་ནི་ལོ་བཅུ་གཉིས་པ་གཟུགས་བཟང་བ་རྒྱན་ཐམས་ཅད་ཀྱིས་བརྒྱན་པ། དྲི་དང་མེ་ཏོག་གིས་ཉེ་བར་མཛེས་པའི་ལུས་ཅན་རྡོལ་བའི༌[^511]རིགས་ཀྱི་བུ་མོ་དམ་ཚིག་དང་སྡོམ་པ་ལ་གནས་པ། ཐོས་པ་དང་བསམ་པ་དང་སྒོམ་པའི་རིམ་གྱིས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་རྣལ་འབྱོར་མ་རྡོ་རྗེ་སློབ་དཔོན་ལ་དབུལ་བར་བྱའོ། །

[Block 760]
དེའི་རྗེས་སུ་དཀོན་མཆོག་གསུམ་ཚིམ་པར་བྱ་བའི་ཕྱིར་ཚོགས་ཀྱི༌[^512]འཁོར་ལོའི་ནང་དུ་ཡང་དེ་མཆོད་པར་བྱའོ། །

[Block 761]
དེ་ལ་དང་པོ་རེ་ཞིག་ཉན་ཐོས་ཀྱི༌[^513]རིགས་མ་གཏོགས་པ་དགེ་སློང་དང་དགེ་ཚུལ་དང་རྡོ་རྗེ་སློབ་དཔོན་དང་དགེ་བསྙེན་རྣམས་སྤྱན་དྲངས་ཏེ། དེ་རྣམས་ལ༌[^514]གོ་རིམས་བཞིན༌[^515]དུ་བརྟུལ་ཞུགས་ཀྱི༌[^516]རྒན་གཞོན་གྱི་རིམ་པས་གདན་རྣམས་དབུལ་བར་བྱའོ། །

[Block 762]
དེ་ལ་རིམ་པ་གཅིག་ལ་དགེ་སློང་གི་ཚོགས་དགོད་པ་དང་།

[Block 763]
གཉིས་པ་ལ་དགེ་ཚུལ་གྱི་ཚོགས་དང་།

[Block 764]
གསུམ་པ་ལ་རྡོ་རྗེ་སློབ་དཔོན་གྱི་ཚོགས་དང་། དགེ་བསྙེན་གྱི་ཚོགས་སོ། །

[Block 765]
གལ་ཏེ་དགེ་སློང་རྣམས་རྡོ་རྗེ་སློབ་དཔོན་དུ་གྱུར༌[^517]ན་དེ་རྣམས་ཀྱི་མདུན་དུ་བརྟུལ་ཞུགས་ཅན་དང་བརྟུལ་ཞུགས་ཅན་མ་ཡིན་པ་རྣམས་དགོད་པར་བྱའོ། །

[Block 766]
གལ་ཏེ་དགེ་བསྙེན་རྡོ་རྗེ་སློབ་དཔོན་དུ་གྱུར་ན། དེའི་མདུན་དུ་དགེ་སློང་སློབ་མ་དང་སློབ་མ་མ་ཡིན་པ་རྣམས་དགོད་པར་བྱའོ། །

[Block 767]
རྣལ་འབྱོར་པའི་ཚོགས་རྣམས་ནི་རབ་ཏུ་བྱུང་བའམ། རབ་ཏུ་མ་བྱུང་བ་རྣམས་རྣམ་པ་ཐམས་ཅད་དུ་གོང་དུ་དགོད་པར་བྱའོ། །

[Block 768]
དགེ་སློང་ངམ་དགེ་ཚུལ་ལམ་དགེ་བསྙེན་ཡིན་ཡང་རུང་ལ། རྣལ་འབྱོར་པས༌[^518]རྟགས་དང་ལྡན་པ་ཡིན་ན་ཚོགས་ཀྱི་བདག་པོར་བྱའོ། །

[Block 769]
ཐམས་ཅད་རིམ་པ་བཞིན་དུ་བཞུགས་པར་མཐོང་ནས་ལས་ཀྱི་རྡོ་རྗེ་མདུན་དུ་ཕྱིན་ཏེ་ཕྱག་འཚལ་བ་སྔོན་དུ་འགྲོ་བར་རྒན་གཞོན་གྱི་རིམ་པས་རེ་རེ་ལ་ཞབས་བསིལ་དབུལ་བར་བྱའོ། །

[Block 770]
དེའི་རྗེས་སུ་མཆོད་པ་རྣམ་པ་ལྔས་མཆོད་དེ་ལག་པ་གཡས་པས་བདུད་རྩི་ལྔས་བཀང་བའི་པདྨའི་སྣོད་བླངས་ཏེ། ལག་པ་གཡོན་པའི་སྲིན་ལག་དང་མཐེ་བོང་གིས་དེ་རྣམས་ཀྱི་མདུན་དུ་གྲུ་གསུམ་པ་ཆོས་འབྱུང་བའི་ཕྱག་རྒྱ་བྲི་བར་བྱའོ། །

[Block 771]
དེའི་ནང་དུ་ཐིག་ལེ་ཟླུམ་པོ་བྲིས་ཏེ། དེའི་ཡང་ནང་དུ་དཀྱིལ་འཁོར་གྱི་འཁོར་ལོ་དག༌[^519]བལྟ་བར་བྱའོ། །

[Block 772]
དཀྱིལ་འཁོར་གྱི་བདག་པོ་ལ་སོགས་པའི་ཐུགས་ཀར་སེམས་དཔའ་གཉིས་པོ་སྣོད་དང་བཅུད་ཀྱི་ངོ་བོ་ཉིད་མ་ལུས་པར་བལྟ་བར་བྱའོ། །

[Block 773]
དེའི་ཤར་གྱི་ཟུར་གྱི་སྟེང་དུ་བདུད་རྩི་ལྔས་གང་བའི་སྣོད་དང་། ཐབས་དང་ཤེས་རབ་ཀྱི་ངོ་བོ་ཉིད་ཧྲི་ཧཱུཾ་དག་གིས་བྱིན་གྱིས་བརླབས་པ་མྱོས་བྱེད་དང་སྦྱར་བའི་ཆང་གིས་བཀང་བའི་སྣོད་གཉིས་ནི་དབུས་ཀྱི་སྣོད་ཀྱི་ལོགས་གཉིས་སུ་གཞག་པར་བྱས་ལ། ནག་པོ་དང་དམར་པོ་དང་དཀར་པོའི་རས་ཀྱིས་ཁ་བཀབ་ལ་མེ་ཏོག་སྙིམ་པས༌[^520]གཏོར་བར་བྱས་ཏེ། ཐུགས་རྡོ་རྗེ་ལ་སོགས་པའི་སྔགས་ཀྱིས་བྱིན་གྱིས་བརླབ༌[^521]པར་བྱའོ། །

[Block 774]
དེ

[Block 775]
་ནས་ཕྱག་བྱས་ཏེ་དབུས་ཀྱི་སྣོད་ལས་ཐིགས་པ་གསུམ་གསུམ་བླངས་ཏེ། གཡས་གཡོན་གྱི་སྣོད་དག་ཏུ༌[^522]གཏོར་བར་བྱ་ཞིང་མྱོས་བྱེད་ཀྱི་སྣོད་དམ་ཆང་གི་སྣོད་བླངས་ལ་རྣལ་འབྱོར་པ་རྣམས་ལ་ལས་ཀྱི་རྡོ་རྗེས༌[^523]
--- END BLOCKS ---
