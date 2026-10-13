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
[Block 1401]
དེ་བཞིན་དུ་སྒྲ་ལ་སོགས་པ་དངོས་པོ་ཐམས་ཅད་ལ་ཡང་རྣམ་པ་བཞི་པོ་དག་མི་འཐད་པས་འགྲུབ་པར་བལྟ་བར༌[^872]བྱའོ། །

[Block 1402]
སྡུག་བསྔལ་བརྟག་པ་ཞེས་བྱ་བ་སྟེ་རབ་ཏུ་བྱེད་པ་བཅུ་གཉིས་པའོ།། །།

[Block 1403 [HEADING]]
## དེ་ཁོ་ན་ཉིད་བརྟག་པ། ^13-0

[Block 1404]
སྨྲས་པ། སྡུག་བསྔལ་ཡང་ཡོད་ཕྱི་རོལ་གྱི་དངོས་པོ་རྣམས་ཀྱང་ཡོད་དེ། དེ་དག་ཡོད་པ་ལ་རྣམ་པ་བཞི་པོ་འབའ་ཞིག་མི་འཐད་དོ། །

[Block 1405]
རྣམ་པ་བཞི་པོ་དག་མེད་དུ་ཟིན་ཀྱང་རེ་ཞིག །དངོས་པོ་རྣམས་ནི་རབ་ཏུ་གྲུབ་པོ། །བཤད་པ། ཅི་ཁྱོད་སྒྱུ་མའི་གླང་པོ་ཆེས་འགྲོ་བར་འདོད་དམ། ཁྱོད་རྣམ་པ་བཞི་པོ་དག་གིས་མ་བྱས་པའི་དངོས་པོ་རྣམས་ཡང་དག་པར་ཡོད་པར་རྟོག་གོ། །

[Block 1406]
འདིར་ཡང་དག་པ་གང་ཡིན་པ་དེ་ཉིད་གཟུང་བར་བྱ་བའི་རིགས་པ་སྙམ།

[Block 1407]
སྨྲས་པ། འདིར་ཡང་དག་པ་གང་ཡིན། བཤད་པ།

[Block 1408 [VERSE]]
ཆོས་གང་སླུ་བ༌[^873]དེ་བརྫུན༌[^874]ཞེས། །
བཅོམ་ལྡན་འདས་ཀྱིས་དེ་སྐད་གསུངས། །
འདུ་བྱེད་ཐམས་ཅད་སླུ་བའི༌[^875]ཆོས། །
དེས་ན་དེ་དག་བརྫུན་པ༌[^876]ཡིན། །

[Block 1409]
འདི་ལ་བཅོམ་ལྡན་འདས་ཀྱིས་མདོ་སྡེ་གཞན་ལས་ཆོས་གང་སླུ་བ༌[^877]དེ་ནི་བརྫུན༌[^878]པའོ། །

[Block 1410]
དགེ་སློང་དག་འདི་ལྟ་སྟེ། མི་སླུ་བའི་ཆོས་མྱ་ངན་ལས་འདས་པ་དེ་ནི་བདེན་པའི་མཆོག་གོ་ཞེས་གསུངས་སོ། །

[Block 1411]
དེ་བཞིན་དུ་བདེན་པ་གཅིག་སྟེ།

[Block 1412]
གཉིས་པ་མེད་ཅེས་ཚིགས་སུ་བཅད་པ་ཡང་གསུངས་སོ། །

[Block 1413]
དེ་བཞིན་དུ་གཞན་ནས་ཀྱང་འདུས་བྱས་དེ་ནི་སླུ་བའི༌[^879]ཆོས་ཀྱང་ཡིན། དེ་ནི་རབ་ཏུ་འཇིག་པའི་ཆོས་ཀྱང་ཡིན་ནོ་ཞེས་འདུ་བྱེད་ཐམས་ཅད་སླུ་བའི༌[^880]ཆོས་ཅན་ཡིན་པར་གསུངས་སོ། །

[Block 1414]
དེའི་ཕྱིར་འདུ་བྱེད་ཐམས་ཅད་སླུ་བའི༌[^881]ཆོས་ཉིད་དེས། ཐམས་ཅད་བརྫུན་པ༌[^882]ཉིད་ཡིན་ཏེ། གང་དག་བརྫུན་པ༌[^883]དེ་དག་ཇི་ལྟར་རབ་ཏུ་འགྲུབ་པར་འགྱུར། ཁྱོད་ཀྱིས་དངོས་པོ་རྣམས་ནི་རབ་ཏུ་གྲུབ་པོ་ཞེས་གང་སྨྲས་པ་དེ་ནི་སྲེད་པས་བསྐྱོད་པར་ཟད་དོ། །

[Block 1415]
སྨྲས་པ། གལ་ཏེ་འདུ་བྱེད་ཐམས་ཅད་བརྫུན་པ༌[^884]ཡིན་ན་འཛིན་བཞིན་དུ་ཡང་དངོས་པོ་ཐམས་ཅད་མེད་དོ་ཞེས་དེ་དག་མི་གསལ་བར་བྱས་པར་མི་འགྱུར་རམ། བཤད་པ་མི་འགྱུར་ཏེ། གལ་ཏེ་སླུ༌[^885]ཆོས་གང་ཡིན་པ། །དེ་བརྫུན༌[^886]དེ་ལ་ཅི་ཞིག་སླུ།[^887] །

[Block 1416 [VERSE]]
བཅོམ་ལྡན་འདས་ཀྱིས་དེ་གསུངས་པ། །
སྟོང་ཉིད་ཡོངས་སུ་བསྟན་པ་ཡིན། །

[Block 1417]
གལ་ཏེ་སླུ་བའི༌[^888]ཆོས་ཞེས་གསུངས་པ་གང་ཡིན་པ་དེ་བརྫུན་པ༌[^889]ཡིན་ན། སླུ་བའི༌[^890]ཆོས་ནི་མེད་པ་ཉིད་དོ་ཞེས་སྨྲ་བ་ཡིན་པས་སླུ་བའི༌[^891]ཆོས་མེད་པ་དེ་ལ་ཅི་ཞིག་སླུ་བར༌[^892]འགྱུར་བ་དེ་ཇེ་སྨྲོས་ཤིག །འདི་ལྟར་མེད་པ་ལ་ཅི་ཞིག་སླུ་བར༌[^893]འགྱུར། ཅི་སྟེ་སླུ་བར༌[^894]འགྱུར་ན་ནི། ཕྱུགས་བདག་པ་དང་གཅེར་བུ་པའི་ནོར་ལ་ཡང་ཆོམ་རྐུན་པ་དག་འཚེ་བར་འགྱུར་རོ། །

[Block 1418]
དེ་ལྟ་བས་ན་བརྫུན་པ༌[^895]ཞེས་གསུངས་པས་དངོས་པོ་རྣམས་མེད་པར་བསྟན་པ་མ་ཡིན་ནོ། །

[Block 1419]
བཅོམ་ལྡན་འདས་སྒྲིབ་པ་མི་མངའ་བའི་མཁྱེན་པ་དང་རྣམ་པར་ཐར་པ་བརྙེས་པ་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་གཟིགས་པས་སླུ་བའི༌[^896]ཆོས་གང་ཡིན་པ་དེ་ནི་བརྫུན་པའོ༌[^897]ཞེས་བྱ་བ་དེ་གསུངས་པས་ནི་དངོས་པོ་རྣམས་ཀྱི་ངོ་བོ་ཉིད་སྟོང་པ་ཉིད་མུ་སྟེགས་བྱེད་ཐམས་ཅད་ཀྱིས་མི་རྟོགས་པ་ཡོད་པ་ཉིད་དང་མེད་པ་ཉིད་ཀྱི་སྐྱོན་དང་བྲལ་བ་ཡོངས་སུ་བསྟན་པ་ཡིན་ནོ། །

[Block 1420]
སྨྲས་པ། བརྫུན་པ༌[^898]ཞེས་གསུངས་པ་ནི། དངོས་པོ་རྣམས་ཀྱི་ངོ་བོ་ཉིད་སྟོང་པ་ཉིད་ཡོངས་སུ་སྟོན་པ་ཡིན་པར་མ་གསུངས་ཀྱི། [^899]བཅོམ་ལྡན་འདས་ཀྱིས་དེ་སྐད་གསུངས་པ་ནི།

[Block 1421 [VERSE]]
དངོས་རྣམས་ངོ་བོ་ཉིད་མེད་དེ། །
གཞན་དུ་འགྱུར་བ་སྣང་ཕྱིར་རོ། །

[Block 1422]
བརྫུན་པ༌[^900]ཞེས་གསུངས་པ་ཉིད་གང་ཡིན་པ་དེས་ནི་དངོས་པོ་རྣམས་ལ་ངོ་བོ་ཉིད་མེད་པ་ཁོ་ནར་ཡོངས་སུ་བསྟན་པ་མ་ཡིན་གྱི། དེ་ནི་དངོས་པོ་རྣམས་གཞན་དུ་འགྱུར་བ་སྣང་བའི་ཕྱིར་དང་། རྣམ་པར་འགྱུར་བ་སྣང་བའི་ཕྱིར་དང་། ངེས་པར་མི་གནས་པའི་ངོ་བོ་ཉིད་དུ་སྣང་བའི་ཕྱིར་ཡོངས་སུ་བསྟན་པ་ཡིན་ནོ། །

[Block 1423]
གལ་ཏེ་ཇི་ལྟར་ཞེ་ན།

[Block 1424 [VERSE]]
ངོ་བོ་ཉིད་མེད་དངོས་མེད་དེ། །
གང་ཕྱིར་དངོས་རྣམས་སྟོང་པ་ཉིད། །

[Block 1425]
གང་གི་ཕྱིར་ངོ་བོ་ཉིད་མེད་པའི་དངོས་པོ་མེད་ལ་དངོས་པོ་རྣམས་ཀྱི་སྟོང་པ་ཉིད་ཀྱང་བསྟན་པ། དེའི་ཕྱིར་དངོས་པོ་རྣམས་ཀྱི་ངོ་བོ་ཉིད་ངེས་པར་མི་གནས་པའི་ཕྱིར་དང་། གཞན་དུ་འགྱུར་བ་སྣང་བའི་ཕྱིར། དངོས་པོ་རྣམས་ངོ་བོ་ཉིད་མེད་པ་ཉིད་ཅེས་གསུངས་པར་ཁོང་དུ་ཆུད་པར་བྱའོ། །

[Block 1426]
དེ་ནི་ངེས་པ་ཁོ་ནར་དེ་ལྟར་ཁོང་དུ་ཆུད་པར་བྱའོ།[^901] །

[Block 1427]
གཞན་དུ་ན།

[Block 1428 [VERSE]]
གལ་ཏེ་ངོ་བོ་ཉིད་མེད་ན། །
གཞན་དུ་འགྱུར་བ་གང་གི་ཡིན། །

[Block 1429]
གལ་ཏེ་དངོས་པོ་རྣམས་ལ་ངོ་བོ་ཉིད་མེད་པ་ཁོ་ན་ཡིན་ན། གཞན་དུ་འགྱུར་བ་དེ་གང་གི་ཡིན་པར་འགྱུར། གཞན་དུ་འགྱུར་བ་ཞེས་བྱ་བ་ནི་ངོ་བོ་ཉིད་ལས་བཟློག་པ་ཡིན་ན། དེ་ལ་གལ་ཏེ་ངོ་བོ་ཉིད་མེད་པ་ཁོ་ན་ཡིན་ན་གཞན་དུ་འགྱུར་བ་ཡང་མེད་པར་འགྱུར་བར་ཐེ་ཚོམ་མེད་པ་ཞིག་ན། གཞན་དུ་འགྱུར་བ་ནི་ཡོད་པས་དེའི་ཕྱིར་ངོ་བོ་ཉིད་ཀྱང་ཡོད་པ་ཁོ་ནའོ། །

[Block 1430]
བཤད་པ།

[Block 1431 [VERSE]]
གལ་ཏེ་ངོ་བོ་ཉིད་ཡོད༌[^902]ན། །
གཞན་དུ་འགྱུར་བ་གང་གི་ཡིན། །

[Block 1432]
ཞེས་གང་སྨྲས་པ་དེ་ལ་བཤད་པར་བྱ་སྟེ།

[Block 1433 [VERSE]]
གལ་ཏེ་ངོ་བོ་ཉིད་ཡོད་ན། །
ཇི་ལྟ་བུར་ན་གཞན་དུ་འགྱུར། །

[Block 1434]
གལ་ཏེ་དངོས་པོ་རྣམས་ལ་ངོ་བོ་ཉིད་ཡོད་ན། གཞན་ལ་མི་ལྟོས་པར་རང་ལས་རབ་ཏུ་གྲུབ་པ་རྟག་པ་མི་འགྱུར་བ་ཡོད་པ་དེ་ལ་ཇི་ལྟར་གཞན་དུ་ཡང༌[^903]འགྱུར་བ་ཡོད་པར་འགྱུར་ཏེ། གཞན་དུ་འགྱུར་བ་ནི་གཞན་ལ་རག་ལས་པའི་ཕྱིར་འགྱུར་བ་ཡིན་གྱི་ངོ་བོ་ཉིད་ནི་མ་ཡིན་པས། དེའི་ཕྱིར་ངོ་བོ་ཉིད་ལ་གཞན་དུ་འགྱུར་བ་མི་འཐད་པའོ།[^904] །

[Block 1435]
སྨྲས་པ། གལ་ཏེ་ངོ་བོ་ཉིད་ལ་གཞན་དུ་འགྱུར་བ་མི་འཐད་ན། འོ་ན་ངོ་བོ་ཉིད་ལས་གཞན་པ་དེ་ཇི་ལྟར་གཞན་དུ་འགྱུར། བཤད་པ།

[Block 1436 [VERSE]]
དེ་ཉིད་ལ་ནི་གཞན་འགྱུར་མེད། །
གཞན་ཉིད་ལ་ཡང་ཡོད་མ་ཡིན། །

[Block 1437]
དངོས་པོར་ཡོངས་སུ་བརྟག་པ་གང་ཡིན་པ་དེ་ཉིད་ལ་ཡང་གཞན་དུ་འགྱུར་བ་ཡོད་པར་མི་འཐད་ལ། དེ་ལས་གཞན་པ་ཉིད་གང་ཡིན་པ་དེ་ལ་ཡང་གཞན་དུ་འགྱུར་བ་ཡོད་པར་མི་འཐད་དོ། །ཅིའི་ཕྱིར་ཞེ་ན།

[Block 1438 [VERSE]]
གང་ཕྱིར་གཞོན་ནུ་མི་རྒ་སྟེ། །
གང་ཕྱིར་རྒས་པའང་མི་རྒའོ། །

[Block 1439]
འདི་ལས་གཞན་དུ་འགྱུར་བ་ཞེས་བྱ་བ་ནི་རྒ་བ་སྟེ། རྒ་བ་དེ་ཡང་གང་གི་ཕྱིར་གཞོན་ནུའི༌[^905]གནས་སྐབས་ཉིད་དུ་རྒ་བར༌[^906]བབ་པ་ལ་ཡང་མེད་ལ། གཞོན་ནུ་ལས་གཞན་པ་རྒས་པའི་གནས་སྐབས་ལ་བབ་པ་ལ་ཡང་མེད་པས། དེའི་ཕྱིར་དེ་ཉིད་ལ་ཡང་གཞན་དུ་འགྱུར་བ་མེད་ལ་གཞན་ཉིད་ལ་ཡང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1440]
གལ་ཏེ་གཞོན་ནུ་གཞོན་ནུའི་གནས་སྐབས་ཉིད་དུ་རྒ་བར་འགྱུར་ན། དེ་ལྟ་ན་རྒས་པ་དང་གཞོན་པ་གཉིས་གཅིག་ལ་ལྷན་ཅིག་གནས་པར་ཡང༌[^907]འགྱུར་རོ། །
--- END BLOCKS ---
