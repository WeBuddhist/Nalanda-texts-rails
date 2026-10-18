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
བདག་དང་བདག་གི་བས་སྟོང་པ་ཉིད་དང་ལྡན་པའི་ཕྱིར་སྟོང་པ་ཉིད་དོ། །

[Block 737]
འདུས་བྱས་ཀྱི་མཚན་མ་ཐམས་ཅད་དང་བྲལ་བའི་ཕྱིར་མཚན་མ་མེད་པའོ། །

[Block 738]
ཁམས་གསུམ་དུ་མི་སྨོན་པས་སྨོན་པ་མེད་པའོ། །

[Block 739]
ཕྱིས་ལས་མངོན་པར་འདུ་བྱེད་པ་མེད་པའི་ཕྱིར། མངོན་པར་འདུ་བྱེད་པ་མེད་པ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 740 [HEADING]]
###### ལམ་གྱི་རྣམ་པ་ཤེས་པ་ཉིད་ཀྱི་ཕྱོགས། ^1-2-1-1-2-0

[Block 741]
ཆོས་དང་ཆོས་རྣམས་སྦྱོར་བ་བྱེད་ཅེས་བྱ་བ་ལ་སོགས་པ་ལ། བྱང་ཆུབ་ཀྱི་སེམས་དང་། དགེ་བའི་རྩ་བའི་སེམས་དང་། ཡོངས་སུ་བསྔོ་བའི་སེམས་རྣམས་ཕན་ཚུན་དུ་འགྲོགས་པར་ཡིད་ལ་བྱེད་པ་ནི་སྦྱོར་བའོ། །

[Block 742]
གསུམ་ཆར་ཡང་བདག་གི༌[^490]ངོ་བོ་དང་། གཞན་གྱི༌[^491]ངོ་བོ་ལ་ཡོད་པ་མ་ཡིན་པར་ཡིད་ལ་བྱེད་པ་ནི་དཔྱོད་པར་བྱེད་པའོ། །

[Block 743]
གསུམ་ཆར་ཡང་སེམས་མ་ཡིན་པའི་ཕྱིར་བསམ་གྱིས་མི་ཁྱབ་པའོ། །

[Block 744]
བསམ་གྱིས་མི་ཁྱབ་པའི་ཕྱིར་སེམས་མ་ཡིན་པའོ་ཞེས་ཡིད་ལ་བྱེད་པ༌[^492]བཤད་ཟིན་པའི་དོན་ཡོངས་སུ་རྫོགས་པའོ། །

[Block 745]
དེ་ལྟར་ཆོས་ཐམས་ཅད་ལ་ཡང་སོ་སོར་རྟོག་ལ་ཆོས་གང་ལ་ཡང་མངོན་པར་ཞེན་པ་མེད་པ་ཞེས་བྱ་བ་ནི༌[^493]ཐམས་ཅད་དུ་རྒྱས་པ་སྟེ། འདི་ནི་བདག་མེད་པར་སོ་སོར་བརྟགས་པ༌[^494]བཞི་པའོ། །

[Block 746]
བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོའི་དགེ་བའི༌[^495]རྩ་བའི་སེམས་གང་ཡིན་པ༌[^496]དེ་བྱང་ཆུབ་ཀྱི་སེམས་དང་འགྲོགས་པ་མ་ཡིན་ཞེས་བྱ་བ་ལ་སོགས་པས་ཅི་བསྟན་ཞེ་ན། བྱང་ཆུབ་སེམས་དཔའ་ནི་སྔར་ཀུན་རྫོབ་ཀྱི་ཡིད་ལ་བྱེད་པས་དགེ་བའི་རྩ་བ་འདི་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཏུ་ཡོངས་སུ་བསྔོའོ་ཞེས་སྤྱིར་ཡོངས་སུ་བསྔོ་བར་བྱས་ནས། དོན་དམ་པའི་ཚུལ་དུ་སོ་སོར་བརྟགས་ནས༌[^497]དགེ་བའི་རྩ་བའི་སེམས་དང་། བྱང་ཆུབ་ཀྱི་སེམས་དང་ཡོངས་སུ་བསྔོ་བའི་སེམས་རྣམས་ཕན་ཚུན༌[^498]དུ་འགྲོགས་པ་མེད་དེ། དེ་ལྟར་འགྲོགས་པ་མེད་པས་ཡོངས་སུ་བསྔོ་བ་ཡོད་དམ་མེད་ཅེས་སོ་སོར་རྟོག་གོ། །

[Block 747]
འདིར་དགའ་ཞིག༌[^499]གལ་ཏེ་སེམས་རྣམ་པར༌[^500]འགྲོགས་པ་མེད་ཀྱང་འོན་ཀྱང་སེམས་སྔ་མའི་དབང་གིས་བསྐྱེད་པའི་འདུ་བྱེད་ཀྱི་བྱེ་བྲག་ནི་སེམས་ཕྱི་མ་དང་ལྷན་ཅིག་ཏུ་འགྲོགས་པར་འགྱུར་ཏེ། ཐམས་ཅད་ཀྱི་ཐ་མའི་སེམས་ལ་ནི་འདུ་བྱེད་ཐམས་ཅད༌[^501]རྫོགས་པར་འགྱུར་རོ། །

[Block 748]
དེ་བས་ན་སྒོ་འདིས་སེམས་རྣམ་པར༌[^502]འགྲོགས་པ་ཡོད་དོ་ཞེས་ཟེར་ཏེ། དེ་བས་ན༌[^503]དེ་བསྩལ་བའི་ཕྱིར། དགེ་བའི་རྩ་བའི་སེམས་གང་ཡིན་པ་དེ་ནི་བྱང་ཆུབ་ཀྱི་སེམས་ལ་མེད་ཅེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། བག་ཆགས་ཀྱི་འདུ་བྱེད་ལ་སོགས་པའི་སྒོ་ནས་སེམས་དེ་ལ་སེམས་གཞན་མེད་དོ་ཞེས་བྱ་བའི་ཐ་ཚིག་སྟེ། འདི་ལྟར་སེམས་ཉིད་མེད་པར་བསྟན་པས་བག་ཆགས་ཀྱི་འདུ་བྱེད་ལ་སོགས་པ་ནི་རི་བོང་གི་རྭ་རྣོ་བ་དང་རྟུལ་བའི་དངོས་པོ་ལྟ་བུར་མི་སྣང་ངོ་ཞེས་བྱ་བའི་ཕྱིར་དེ་སྐད་དུ་བཤད་དོ། །

[Block 749]
དེ་ལྟར་གཞན་གྱི་ངོ་བོ་ལ་མེད་པར་དཔྱད་ནས་ཡང་བདག་གི་ངོ་བོ་ལ་དཔྱོད་དོ། །

[Block 750]
དགེ་བའི་རྩ་བའི་སེམས་གང་ཡིན་པ་དེ་དགེ་བའི་རྩ་བའི་སེམས་ལ་མེད། བྱང་ཆུབ་ཀྱི་སེམས་གང་ཡིན་པ་དེ་ཡང་བྱང་ཆུབ་ཀྱི་སེམས་ལ་མེད་ཅེས་བྱ་བ་ལ་སོགས་པ་སྟེ། དེ་བཞིན་ཉིད་ཙམ་དུ་མཐོང་བ་ལ་ནི་དེ་ལྟ་བུའི་ཀུན་ཏུ་དཔྱོད་པ༌[^504]མེད་པའི་ཕྱིར་རོ། །

[Block 751]
ཀཽ་ཤི་ཀ་དགེ་བའི་རྩ་བའི་སེམས་གང་ཡིན་པ་དེ་ནི་སེམས་མ་ཡིན་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་དེ་བཞིན་ཉིད་ཙམ་ཁོ་ནར་སྟོན་ཏོ། །

[Block 752]
སེམས་ནི༌[^505]རང་གི་ཆོས་ཉིད་ཀྱི་དབང་གིས་སེམས་ཀུན་བརྟགས་པ་དང་བྲལ་བའི་ཕྱིར་སེམས་མེད་པའི་ངོ་བོ་ཉིད༌[^506]དེ་ཆོས་ཉིད་ཀྱི་སེམས་སུ་གྲག་གོ།[^507] ། སེམས་མེད་པ་ནི་སེམས་མེད་པ་དང་འགྲོགས་པར་མི་འགྱུར་ཞེས་བྱ་བ་ལ་སོགས་པ༌[^508]ནི་ཆོས་ཉིད་ཀྱི་སེམས་སུ་གྲག་པ་ལས་འགྲོགས་པའམ་ཡོད་པའམ་ཡོངས་སུ་བསྔོ་བ་ཐམས་ཅད་ཀྱི་ཐམས་ཅད་དུ་མ་གྲག་གོ༌[^509]ཞེས་སྟོན་ཏོ། །

[Block 753]
དེའི་ཚེ་ནི་དེ༌[^510]སོ་སོ་རང་གིས་རིག་པ་ཡིན་པས་བསམ་པའི་ལམ་ལས་འདས་པའི་ཕྱིར། བསམ་གྱིས་མི་ཁྱབ་པ་དང་། སེམས་མ་ཡིན་ནོ། །

[Block 754]
ཀཽ་ཤི་ཀ་འདི་ནི་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོའི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའོ་ཞེས་བྱ་བ་ནི་རྣམ་པར་མི་རྟོག་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་ཤེས་རབ་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 755]
གང་དེ་ལྟར་ཆོས་ཐམས་ཅད་ལ་སོ་སོར་རྟོག་པ་ཞེས་བྱ་བ་ནི་ཀུན་རྫོབ་ཏུའོ། །

[Block 756]
ཆོས་གང་ལ་ཡང་མངོན་པར་ཞེན་པ་མེད་ཅིང་མི་དམིགས་ཞེས་བྱ་བ་ནི་དོན་དམ་པར་རོ། །

[Block 757]
བདག་གིས་བྱས་པ་གཟོ་བར་བགྱི་སྟེ། བྱས་པ་མི༌[^511]གཟོ་བར་མི་བགྱིའོ་ཞེས་བྱ་བས་ཅི་བསྟན་ཞེ་ན། སྔོན་བདག་གི༌[^512]བཅོམ་ལྡན་འདས་བྱང་ཆུབ་སེམས་དཔར་གྱུར་པའི་ཚེ་སྔོན་གྱི་དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱི་འཁོར་ན་ཉན་ཐོས་ཆེན་པོ་རྣམས་ཀྱིས་གདམས་པ་དང་རྗེས་སུ་བསྟན་པས་ཡང་དག་པར་བསྟན་པ་དང་། ཡང་དག་པར་འཛིན་དུ་བཅུག་པ་བརྙེས་ནས་ཡང་དག་པར་སྒྲུབ་པ་ལ་བཅུག་སྟེ། དེ་དག་གིས༌[^513]བསྟན་པའི་རིམ་པས་བསྒྲུབས་ནས་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་སོ། །

[Block 758]
དེ་བས་ན་བདག་གིས་ཀྱང་འཁོར་འདིར་བྱང་ཆུབ་སེམས་དཔའ་འདི་རྣམས་ལ་གདམས་པ་དང་རྗེས་སུ་བསྟན་པས་ཡང་དག་པའི་སྒྲུབ་པ་ལ༌[^514]དགོད་པར་བགྱིའོ། །

[Block 759]
སྔོན་གྱི་དེས་བདག་ཅག་གིས་བསྟན་པའི་རིམ་པས་བསྒྲུབས་ན་མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་བར་འགྱུར་ཏེ། དེ་བས་ན་སྔོན་གྱི་ཉན་ཐོས་རྣམས་ཀྱིས་བྱས་པ་བདག་གིས་ཤེས་པར་བྱའོ་ཞེས་སྟོན་ཏོ། །

[Block 760]
གདམས་ཤིང་རྗེས་སུ་བསྟན་པ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིག་རྣམས་ལ་བྱེ་བྲག་ཅི་ཡོད་ཅེ་ན་འདི་ལ་ཐོག་མ་དང་བར་མ་དང་ཐ་མའི་གནས་སྐབས་གསུམ་སྟེ། །ཐོག་མར༌[^515]ནི་གདམས་ཤིང་རྗེས་སུ་བསྟན་པར་བྱའོ། །

[Block 761]
བར་དུ་ནི་སྒྲུབ་པའོ། །

[Block 762]
ཐ་མར་ནི་འབྲས་བུའོ། །

[Block 763]
དེ་ལ་ཐོག་མའི་གནས་སྐབས་སུ་འདི་དག་མ་བྱེད་ཅིག་ཅེས་བྱ་བ་མ་ཡིན་པ་ལས་བཟློག་པ་ནི་གདམས་པའོ། །

[Block 764]
འདི་དག་བྱོས་ཤིག་ཅེས་བྱ་བ་ལ་སྦྱོར་བ་ནི་རྗེས་སུ་བསྟན་པའོ། །

[Block 765]
བར་དུ་ནི་མི༌[^516]སྒྲུབ་པ་དང་། ལོག་པར་སྒྲུབ་པ་དང་། ཅུང་ཟད་སྒྲུབ་པ་དང་། ཡང་དག་པར་སྒྲུབ་པ་སྟེ་གནས་སྐབས་བཞིའོ། །

[Block 766]
དེ་ལ་མི་ཤེས་པས་མི་སྒྲུབ་པ༌[^517]ལ་སྒྲུབ་ཏུ་འཇུག་པ་ནི་ཡང་དག་པར་བསྟན་པའོ། །

[Block 767]
ལོག་པར་ཤེས་པས་ལོག་པར་ཞུགས་པ་དག་ཡང་དག་པར་སྒྲུབ༌[^518]ལ་སྦྱོར་བ་ནི་ཡང་དག་པར་འཛིན་དུ་བཅུག་པའོ། །

[Block 768]
ལེ་ལོ་ལ་སོགས་པའི་སྐྱོན་གྱིས་ཅུང་ཟད་སྒྲུབ་པ་དག་ལེགས་པར་བརྩོན་འགྲུས་རྩོམ་དུ་འཇུག་པ་ནི་ཡང་དག་པར་གཟེངས་སྟོད༌[^519]པའོ། །ཤེས་རབ་ཀྱིས་ཡང་དག་པར་ཞུགས་པ་དག༌[^520]ལེགས་སོ་ཞེས་རྗེས་སུ་ཡི་རངས༌[^521]ནས་དེ་ཉིད་ལ་སྦྱོར་བ་ནི་ཡང་དག་པར་རབ་ཏུ་དགྱེས་པར་བགྱིད་པའོ། །

[Block 769]
ཐ་མར་ནི་ལམ་ལ་བཅུག་ཅིང་འབྲས་བུ་ལ་གཞག་ཅེས་བྱ་བར་སྦྱར་བར་བྱའོ། །

[Block 770 [HEADING]]
##### ཇི་ལྟར་གནས་པར་བྱ་ཞེས་དྲིས་པའི་ལན། ^1-2-1-2-0

[Block 771]
དེའི་འོག་ཏུ་ཇི་ལྟར་གནས་པར་བྱ་ཞེས་དྲིས་པ་ལ་གནས་པར་མི་བྱ་བ་ཡོངས་སུ་སྤངས་ཏེ་གནས་པར་བྱ་བས་གནས་པ་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་གནས་པ་ཞེས་བྱ་བར་སྟོན་ཏོ། །

[Block 772]
གཟུགས་ནི་གཟུགས་ཀྱིས་སྟོང་ངོ་ཞེས་བྱ་བ་ལ་སོགས་པས་སྟོང་པ་ཉིད་རྟོགས་པ་ནི་གནས་པའོ། །

[Block 773]
དམིགས་པའི་ཚུལ་ནི་གནས་པ་མ་ཡིན་ནོ་ཞེས་སྟོན་ཏེ། དེས་ནི་འདི་སྐད་དུ་གང་གི་ཕྱིར་གཟུགས་ལ་སོགས་པ་ཀུན་བརྟགས་པའི་ཆོས་འདི་དག་གཟུགས་ལ་སོགས་པའི་ངོ་བོ་ཉིད་ཀྱིས་ཡོད་པ་མ་ཡིན་ལ། བྱང་ཆུབ་སེམས་དཔའ་ཡང་བྱང་ཆུབ་སེམས་དཔའི་ངོ་བོ་ཉིད་ཀྱིས་མེད་པ་སྟེ། དེ་དག་གི༌[^522]སྟོང་པ་ཉིད་གང་ཡིན་པ་དེ༌[^523]ཐ་མི་དད་དེ་གཅིག་གོ། །

[Block 774]
དེ་བས་ན་ཆོས་ཉིད་ཀྱི་གཟུགས་ལ་སོགས་པ་ནི་ཡོངས་སུ་གྲུབ་པ་ཡིན་ལ་བྱང་ཆུབ་སེམས་དཔའ་ཡང་གཉིས་སུ་མེད་པ་སྟེ། གཅིག་པའི་ཆོས་ཉིད་དུ་གནས་པ་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་གནས་པའོ་ཞེས་བསྟན་ཏོ། །

[Block 775 [HEADING]]
###### གནས་པར་མི་བྱ་བའི་འགྲེས། ^1-2-1-2-1-0
--- END BLOCKS ---
