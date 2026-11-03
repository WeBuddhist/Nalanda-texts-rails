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
[Block 2031]
ད་ནི་བྲལ་བ་གང་ཞེ་ན། གང་སོ་སོར་བརྟགས་པས་འགོག་པའོ་ཞེས་བཤད་པས་ཕན་ཚུན་རྟེན་པའི་བཤད་པ་འདི་ནི་དེའི་རང་གི་ངོ་བོ་གསལ་བར་བྱ་བ་ལ་ནུས་པ་མ་ཡིན་ཏེ། དེ་ལྟ་བས་ན་དེའི་རང་གི་ངོ་བོ་གཞན་དུ་བརྗོད་པར་བྱའོ། །

[Block 2032]
དེའི་རང་གི་ངོ་བོ་ནི་འཕགས་པ་རྣམས་ཁོ་ནས་སོ་སོ་རང་གིས་རིག་པར་བྱ་བ་ཡིན་ཏེ། བྲལ་བ་ཞེས་བྱ་བ་དང་། སོ་སོར་བརྟགས་པའི་འགོག་པ་ཞེས་བྱ་བ་གང་ཡིན་པ་བརྟགས༌[^1042]པ་དང་དགེ་བའི་རྫས་གཞན་ཞིག་ཡོད་དོ་ཞེས་བྱ་བ་དེ་ཙམ་ཞིག་ནི་བརྗོད་པར་ནུས་སོ།[^1043] །མདོ་སྡེ་པ་རྣམས་ན་རེ་འདུས་མ་བྱས་ཐམས་ཅད་ཀྱང་རྫས་སུ་མེད་པ་ཁོ་ན་སྟེ། དེ་ནི་གཟུགས་དང་ཚོར་བ་ལ་སོགས་པ་བཞིན་དུ་རྫས་གཞན་དུ་ནི་མེད་དོ། །

[Block 2033]
འོ་ན་ཅི་ཞེ་ན། རེག་བྱ་མེད་པ་ཙམ་ནི་ནམ་མཁའ་ཡིན་ཏེ། འདི་ལྟར་མུན་པའི་ནང་དག་ན་ཐོགས་པ་མ་རྙེད་ན་ནམ་མཁའོ་ཞེས་ཟེར༌[^1044]ཏོ། །

[Block 2034]
ཕྲ་རྒྱས་དང་སྐྱེ་བ་སྐྱེས་པ་འགགས༌[^1045]ནས་སོ་སོར་བརྟགས་པའི་སྟོབས་ཀྱིས་གཞན་མི་སྐྱེ་བ་ནི་སོ་སོར་བརྟགས་པས་འགོག་པ་ཡིན་ནོ། །

[Block 2035]
སོ་སོར་བརྟགས་པ་མེད་པ་ཁོ་ནར་རྐྱེན་མ་ཚང་བས་མི་སྐྱེ་བ་ནི་སོ་སོར་བརྟགས་པ་མ་ཡིན་པས་འགོག་པ་སྟེ་དཔེར་ན་བར་མ་དོར་འཆི་བའི་རིས་མཐུན་པ་ལྷག་མ་ལྟ་བུའོ་ཞེས་ཟེར་རོ། །

[Block 2036]
སྡེ་པ་གཞན་དག་ན་རེ་ཕྲ་རྒྱས་རྣམས་མི་སྐྱེ་བར་བྱ་བ་ལ་ཤེས་རབ་ཀྱི་ནུས་པ་ཡོད་དོ། །

[Block 2037]
[^1046]དེའི་ཕྱིར་དེ་ནི་སོ་སོར་བརྟགས་པས་འགོག་པ་ཡིན་ནོ། །

[Block 2038]
སྡུག་བསྔལ་མི་སྐྱེ་བ་གང་ཡིན་པ་དེ་ནི་སྐྱེ་བའི་རྐྱེན་ཕྲ་རྒྱས་མེད་པ་ཁོ་ནའི་ཕྱིར་དེ་ལ་ཤེས་རབ་ཀྱི་ནུས་པ་མེད་དེ། དེའི་ཕྱིར་དེ་ནི་སོ་སོར་བརྟགས་པ་མ་ཡིན་པས་འགོག་པ་ཡིན་ནོ་ཞེས་ཟེར་ཏེ་དེ་ཡང་སོ་སོར་བརྟགས་པ་མེད་པས་མི་འགྲུབ་པས་དེ་ནི་སོ་སོར་བརྟགས་པས་འགོག་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 2039]
གཞན་དག་ན་རེ་སྔར༌[^1047]སྐྱེས་པ་ཕྱིས་མེད་པ་གང་ཡིན་པ་དེ་ཉིད་རང་གི་ངང་གིས་འགག་པའི་ཕྱིར་སོ་སོར་བརྟགས་པ་མ་ཡིན་པས་འགོག་པ་ཡིན་ནོ་ཞེས་ཟེར་ཏེ། [^1048]རྟོག་པ་དེ་ལ་ནི་སོ་སོར་བརྟགས་པ་མ་ཡིན་པས་འགོག་པ་མི་རྟག་པ་ཁོ་ནར་འགྱུར་ཏེ། མ་ཞིག་ན་དེ་མེད་པའི་ཕྱིར་རོ། །

[Block 2040]
སོ་སོར་བརྟགས་པས་འགོག་པ་ཡང་སོ་སོར་བརྟགས་པ་སྔོན་དུ་འགྲོ་བའི་ཕྱིར་མི་རྟག་པར་འགྱུར་བ་མ་ཡིན་ནམ། དེ་ནི་སོ་སོར་བརྟགས་པ་སྔོན་དུ་འགྲོ་བ་མ་ཡིན་ཏེ། སྔར་སོ༌[^1049]སོར་བརྟགས་པ་ཡིན་ལ་ཕྱིས་སྐྱེ་བ་རྣམས་ཀྱི་མི་སྐྱེ་བ་ནི་མ་ཡིན་ནོ། །

[Block 2041]
འོ་ན་ཅི་ཞེ་ན། དེ་དག་མི་སྐྱེ་བ་དེ་ནི་སྔ་ནས་ཡོད་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 2042]
[^1050]ཆོས་གང་དག་སོ་སོར་བརྟགས་པ་མེད་ན་སྐྱེ་བར་འགྱུར་བ་དེ་དག་སོ་སོར་བརྟགས་པ་སྐྱེས་ན་ཡང་མི་སྐྱེའོ། །

[Block 2043]
འདི་ལ་སོ་སོར་བརྟགས་པའི་མཐུ་ནི་འདི་ཡིན་ཏེ། འདི་ལྟ་སྟེ་གེགས་མ་བྱས་པ་རྐྱེན༌[^1051]རྣམས་སྐྱེ་བ་ལ་གེགས་བྱེད་པའི་དངོས་པོ་ཡིན་ནོ། །

[Block 2044]
གལ་ཏེ་མི་སྐྱེ་བ་ཁོ་ན་མྱ་ངན་ལས་འདས་པ་ཡིན་ན་འོ་ན་མདོའི་ཚིག་དབང་པོ་ལྔ་པོ་འདི་དག་ཀུན་ཏུ་བསྟེན། [^1052]གོམས་པར་བྱས། ལན་མང་དུ་བྱས་ན་འདས་པ་དང་མ་འོངས་པ་དང་ད་ལྟར་བྱུང་བའི་སྡུག་བསྔལ་སྤངས་པར་འགྱུར་རོ་ཞེས་བྱ་བ་འདི་ཇི་ལྟར་དྲང་། སྤངས་པ་ནི་མྱ་ངན་ལས་འདས་པ་ཡིན་ནོ། །

[Block 2045]
མི་སྐྱེ་བ་ནི་མ་འོངས་པ་ཁོ་ན་ཡིན་གྱི་འདས་པ་དང་ད་ལྟར་བྱུང་བ་ནི་མ་ཡིན་ནོ། །

[Block 2046]
དེ་སྐད་དུ་འབྱུང་བ་ཡང་ཡོད་མོད་ཀྱི་འོན་ཀྱང་། བཅོམ་ལྡན་འདས་ཀྱིས་དེ་ལ་དམིགས་པའི་ཉོན་མོངས་པ་སྤངས་པས་སྡུག་བསྔལ་སྤོང་བར་གསུངས་པ་ཡིན་ཏེ། གཟུགས་ལ་འདུན་པ་དང་འདོད་ཆགས་གང་ཡིན་པ་དེ་སྤོངས་ཤིག །འདུན་པ་དང་འདོད་ཆགས་སྤངས་ན་ཁྱེད་ཀྱིས༌[^1053]གཟུགས་དེ་ལྟ་བུ་དེ་ཡང་སྤངས་པ་དང་ཡོངས་སུ་ཤེས་པར་འགྱུར་རོ་ཞེས་བྱ་བ་ནས། རྒྱས་པར་རྣམ་པར་ཤེས་པའི་བར་དུ་གསུངས་ཏེ། དེ་ལྟར་ན་དུས་གསུམ་པའི་སྡུག་བསྔལ་ཡང་སྤངས་པར་རུང་ངོ་། །ཅི་སྟེ་འདས་པ་དང་མ་འོངས་པ་དང་ད་ལྟར་བྱུང་བའི་ཉོན་མོངས་པ་སྤངས་པར་འགྱུར་རོ་ཞེས་འབྱུང་བར་འགྱུར་ན། དེར་ཡང་ཚུལ་ནི་འདི་ཁོ་ན་ཡིན་ནོ། །

[Block 2047]
ཡང་ན་དགོངས་པ་ནི་འདས་པའི་ཉོན་མོངས་པ་ནི་ཚེ༌[^1054]རབས་སྔ་མ་པ་ཡིན་ལ། ད་ལྟར་བྱུང་བའི་ཉོན་མོངས་པ་ནི་ཚེ་འདི་པ་ཡིན་ཏེ། དཔེར་ན་སྲེད་པ་རྣམ་པར་སྤྱད་པ་དག་ལ་འདས་པའི་དུས་ལ་བརྟེན་ནས་སྲེད་པ་རྣམ་པར་སྤྱད་པ་བཅྭ་བརྒྱད༌[^1055]དོ་ཞེས་འབྱུང་བ་འདས་པའི་ཚེ་རབས་ཀྱི་དབང་དུ་མཛད་ནས་གསུངས་པ་དང་། ད་ལྟར་བྱུང་བའི་བར་དུ་ཡང་དེ་དང་འདྲ་བ་ལྟ་བུའོ། །

[Block 2048]
ཉོན་མོངས་པ་གཉིས་པོ་འདིས་ཀྱང་རྒྱུད་འདི་ལ་མ་འོངས་པ་བསྐྱེད་པའི་ཕྱིར༌[^1056]ས་བོན་གྱི་དངོས་པོ་བཞག་པ་དེ་སྤངས་པས་དེ་ཡང་སྤངས་པ་ཡིན་ཏེ། དཔེར་ན་རྣམ་པར་སྨིན་པ་ཟད་པ་ལས་ཟད་པར་འགྱུར་བ་ལྟ་བུའོ། །

[Block 2049]
མ་འོངས་པའི་སྡུག་བསྔལ་ལ་ཉོན་མོངས་པ་ནི་ས་བོན་མེད་པའི་ཕྱིར་གཏན་དུ་མི་སྐྱེ་བ་སྤངས་པ་ཡིན་ནོ། །

[Block 2050]
དེ་ལྟ་མ་ཡིན་ན་འདས་པ་དང་ད་ལྟར་ལ་ཅི་ཞིག་སྤང་དུ་ཡོད་དེ། འགགས་ཟིན་པ་དང་། འགག་པ་ལ་མངོན་དུ་ཕྱོགས་པ་ལ་ནི་འབད་པ་དོན་དང་བཅས་པར་མི་འགྱུར་རོ་སྙམ་པ་འདི་ཡིན་པར་འགྱུར་རོ། །

[Block 2051]
གལ་ཏེ་འདུས་མ་བྱས་མེད་པ་ཁོ་ན་ཡིན་ན། བཅོམ་ལྡན་འདས་ཀྱིས་ཆོས་གང་དག་འདུས་བྱས་ཀྱང་རུང་འདུས་མ་བྱས་ཀྱང་རུང་དེ་དག་གི་མཆོག་ནི་འདོད་ཆགས་དང་བྲལ་བ་ཡིན་པར་བཤད་དོ་ཞེས་གང་གསུངས་པ། ཇི་ལྟར་ན་མེད་པ་རྣམས་ཀྱི་མཆོག༌[^1057]ཡིན་པར་འོས། འདུས་མ་བྱས༌[^1058]མེད་པ་ཁོ་ནའོ་ཞེས་ཀྱང་མི་སྨྲའི་དེ་ནི་ཁོ་བོ་ཅག་གིས་ཇི་སྐད་དུ་བཤད་པ་དེ་ལྟ་བུ་ཡིན་ནོ། །

[Block 2052]
དཔེར་ན་སྒྲ་ལ་སྔ་ན་མེད་པ་ཡང་ཡོད། ཕྱིས་མེད་པ་ཡང་ཡོད་ཅེས་བྱ་མོད་ཀྱི་འོན་ཀྱང་མེད་པ་ནི་ཡོད་པར་མི་འགྲུབ་པ་ལྟར་འདུས་མ་བྱས་ཀྱང་དེ་བཞིན་དུ་བལྟ་བར་བྱའོ། །

[Block 2053]
མེད་པ་ཡང་ཁ་ཅིག་ཤིན་ཏུ་བསྔགས་པ་ཡོད་དེ། གང་གནོད་པ་ཐམས་ཅད་དང་བྲལ་བ་དེ་ནི་འདུལ་བ༌[^1059]རྣམས་དེ་ལ་འདུན་པར་བྱ་བའི་ཕྱིར་གཞན་དག་གི་མཆོག་ཡིན་ནོ་ཞེས་བསྔགས་པ་འཐོབ་པར་འོས་སོ། །

[Block 2054]
གལ་ཏེ་འདུས་མ་བྱས་མེད་པ་ཙམ་ཞིག་ཡིན་ན་འགོག་པ་འཕགས་པའི་བདེན་པ་ཡིན་པར་མི་འགྱུར་ཏེ། དེ་ཅུང་ཟད་ཀྱང་མེད་པའི་ཕྱིར་རོ། །

[Block 2055]
རེ་ཞིག་འགོག་པའི་བདེན་པའི་དོན་འདི་གང་ཡིན། ཕྱིན་ཅི་མ་ལོག་པའི་དོན་མ་ཡིན་ནམ། འཕགས་པ་རྣམས་ཀྱིས་འདི་ལྟ་སྟེ། སྡུག་བསྔལ་ལ་ཡང་སྡུག་བསྔལ་ཁོ་ནའོ། །

[Block 2056]
སྡུག་བསྔལ་མེད་པ་ལ་ཡང་མེད་པ་ཁོ་ནའོ་ཞེས་འདི་གཉི་ག་ཡང་ཕྱིན་ཅི་མ་ལོག་པར་གཟིགས་ན་འདི་འཕགས་པའི་བདེན་པ་ཉིད་ཡིན་པར་འགལ་བ་ཅི་ཞིག་ཡོད། ཇི་ལྟར་མེད་པ་ཡང་ཡིན་ལ་འཕགས་པའི་བདེན་པ་གསུམ་པ་ཡང་ཡིན་པར་འགྱུར། ཇི་ལྟར་འཕགས་པའི་བདེན་པ་ཡིན་པ་ནི་བཤད་ཟིན་ཏོ། །

[Block 2057]
གཉིས་པའི་འོག་ཏུ་མཐོང་བ་དང་བསྟན་པས་ན་གསུམ་པ་ཡིན་ནོ། །

[Block 2058]
གལ་ཏེ་འདུས་མ་བྱས་དངོས་པོ་མེད་པ་ཙམ་ཡིན་ན་ནམ་མཁའ་དང་མྱ་ངན་ལས་འདས་པ་ལ༌[^1060]དམིགས་པའི་ཤེས་པ་མེད་པ་ལ་དམིགས་པར་འགྱུར་རོ། །

[Block 2059]
འདི་ནི་འདས་པ་དང་མ་འོངས་པ་ཡོད་པ་ཉིད་བསམ་པར་བྱའོ། །

[Block 2060]
གལ་ཏེ་འདུས་མ་བྱས་རྫས་ཁོ་ནར་འདོད་པར་གྱུར༌[^1061]ན་ཅིར་འགྱུར། ཅི་ཞིག་ཏུ་ཡང་འགྱུར། བྱེ་བྲག་ཏུ་སྨྲས་པའི༌[^1062]ཕྱོགས་བསྐྱབ༌[^1063]པར་འགྱུར་རོ། །

[Block 2061]
གལ་ཏེ་འདི་བསྐྱབ་པར་བྱ་བ་ཡིན་པར་སེམས་ན་ལྷ་སྐྱོབ་པར་འགྱུར་གྲང་། ཡང་དག་པ་མ་ཡིན་པ་ཀུན་ཏུ་བརྟགས་པར་འགྱུར་རོ། །ཅིའི་ཕྱིར་ཞེ་ན། གཟུགས་དང་ཚོར་བ་ལ་སོགས་པ་བཞིན་དུ་དེའི་རང་གི་ངོ་བོ་ཡང་མི༌[^1064]དམིགས་ལ་མིག་ལ་སོགས་པ་བཞིན་དུ་ལས་ཀྱང་མི་དམིགས་སོ། །

[Block 2062]
དངོས་པོ་ཆེ་གེ་མོ་ཞིག་གི་འགོག་པ་འདི་ཡིན་ནོ་ཞེས་རྣམ་པར་གཞག་པ་ཡང་ཇི་ལྟར་རབ་ཏུ་བརྟགས་ཏེ།[^1065] རྒྱུ་དང་འབྲས་བུ་ལ་སོགས་པའི་དངོས་པོ་མི་སྲིད་པའི་ཕྱིར་དེ་ནི་དེ་དང་ལྷན་ཅིག་འབྲེལ་པ་འགའ་ཡང་མེད་ཀྱི་ཆེ་གེ་མོ་ཞིག་མེད་པའོ་ཞེས་འགག་པ་ཙམ་དུ༌[^1066]རུང་ངོ་། །དངོས་པོ་གཞན་ཉིད་ཡིན་ན་ཡང་ཉོན་མོངས་པ་གང་གི་ཐོབ་པ༌[^1067]ཆད་ནས་འགོག་པ་གང་ཐོབ་པ་དེ་དེའི་ཡིན་ནོ་ཞེས་ཐ་སྙད་གདགས༌[^1068]སོ། །

[Block 2063]
འོ་ན་དེ་ཐོབ་པར་འདོད་པའི༌[^1069]རྒྱུ་གང་ཞིག་ཡིན། མདོ་ལས་མཐོང་བའི་ཆོས་ལ༌[^1070]མྱ་ངན་ལས་འདས་པ་ཐོབ་པའི་དགེ་སློང་ཞེས་གསུངས་པ་དེ་ཇི་ལྟར་ན་མེད་པ་ཐོབ་པར་རུང་། གཉེན་པོ་ཐོབ་པས་ཉོན་མོངས་པ་དང་། ཡང་སྲིད་པའི་སྐྱེ་བ་དང་ཤིན་ཏུ་འགལ་བའི་རྟེན་ཐོབ་པའི་ཕྱིར་མྱ་ངན་ལས་འདས་པ་ཐོབ་པ་ཞེས་བྱའོ། །

[Block 2064]
ལུང་ལས་ཀྱང་དངོས་པོ་མེད་པ་ཙམ་ཉིད་དུ་བརྗོད་པར་མཛད་དེ། འདི་སྐད་དུ་སྡུག་བསྔལ་འདི་མ་ལུས་པར་སྤངས་པ། ངེས་པར་སྤངས་པ།[^1071] བྱང་བར་འགྱུར་བ། ཟད་པ། འདོད་ཆགས་དང་བྲལ་བ། འགོག་པ། རྣམ་པར་ཞི་བ། ནུབ༌[^1072]པ། སྡུག་བསྔལ་གཞན་དང་ཉིང་མཚམས་སྦྱོར་བ་མེད་པ། ལེན་པ་མེད་པ། འབྱུང་བ་མེད་པ་གང་ཡིན་པ་འདི་ལྟ་སྟེ། ཕུང་པོ་ཐམས་ཅད་ངེས་པར་སྤངས་པ། སྲེད་པ་ཟད་པ། འདོད་ཆགས་དང་བྲལ་བ། འགོག་པ།[^1073] མྱ་ངན་ལས་འདས་པ་འདི་ནི་ཞི་བའོ། །

[Block 2065]
འདི་ནི་གྱ་ནོམ་པའོ་ཞེས་གསུངས་སོ། །

[Block 2066]
འདིར་ཡིན་ན་འབྱུང་བར་མི་འགྱུར་བས་དེའི་ཕྱིར་འབྱུང་བ་མེད་པ༌[^1074]ཞེས་བྱ་བ༌[^1075]དེ་ལྟར་ཅི་སྟེ་མི་འདོད་ཅེ་ན།

[Block 2067]
བདུན་པ་འདི་ནི་ནུས་པ་མེད་པར་ལྟའོ། །

[Block 2068]
འདིར་ཡིན་ན་འབྱུང་བར་མི་འགྱུར་རོ་ཞེས་བྱ་བ་ཇི་སྐད་དུ་བཤད་པ་ཡིན། གལ་ཏེ་ཡོད་ན་ཞེས་བྱ་བར་སྦྱར་ན་ནི༌[^1076]མྱ་ངན་ལས་འདས་པ་ནི་མི༌[^1077]རྟག་པའི་ཕྱིར་རྟག་ཏུ་མི་འབྱུང་བ་ཁོ་ནར་ཐལ་བར་འགྱུར་རོ། །

[Block 2069]
འོན་ཏེ་ཐོབ་ན་ཞེས་བྱ་བར་སྦྱར་ན་ནི་གང་ཁོ་ནས་དེ་འཐོབ་པར་ཡོངས་སུ་རྟོག་པ་དེ་ཉིད་ཡོད་དམ་ཐོབ་ན་སྡུག་བསྔལ་མི་འབྱུང་བར་འདོད་པར་གྱིས་ཤིག །དེ་ལྟར་ན།

[Block 2070 [VERSE]]
མར་མེ་ཤི་བར་གྱུར་པ་ལྟར། །
དེ་ཡི་སེམས་ཀྱི་རྣམ་པར་ཐར། །
--- END BLOCKS ---
