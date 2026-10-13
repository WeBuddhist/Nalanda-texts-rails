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
[Block 946 [HEADING]]
#### བརྗོད་པར་འདོད་པའི་གྲངས་གཅིག་ཉིད། ^3-2-4-0

[Block 947]
གཏན་ཚིགས་ལ་སོགས་པ་འདི་དག་ཐམས་ཅད་ལ་ཡང་། བརྗོད་པར་འདོད་པའི་གྲངས་གཅིག་ཉིད། །རིགས་དང་རྫས་ལས་ཤེས་པར་བྱའོ་ཞེས་བྱ་བའི༌[^708]ཚིག་གི་ལྷག་མའོ། །

[Block 948]
གང་ཡང་གྲངས་གཅིག་ཅེས་པ་ནི་འདིར་གང་རིགས་དང་མཐུན་པར་ཡོད་པའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་དེ་བརྗོད་པར་འདོད་པ་སྟེ། ཅིའི་ཕྱིར་ཞེ་ན། འགལ་བ་དག་ལ་ཐེ་ཚོམ་ཕྱིར། །གལ་ཏེ་གང་ཕྱིར་འགལ་བ་མཚན་ཉིད་གཉིས་སུ་བརྗོད་པ་དག་ལས་གྲངས་གཅིག་པར་ནི་མཐོང་བ་ཉིད་དེ། དཔེར་ན་སྒྲ་ལ་བྱས་པ་ཉིད་དང་། མཉན་བྱ་དག་ལ་རྟག་པ༌[^709]དང་མི་རྟག་པ་ཉིད་དུ་ཐེ་ཚོམ་ཟ་བ་ཡིན་ནོ་ཞེ་ན།

[Block 949 [VERSE]]
[^710]དེ་བཞིན་ཐེ་ཚོམ་རྟགས་ཉིད་ལས། །
གཅིག་ཏུ་ངེས་པར་མཐོང་མ་ཡིན། །

[Block 950]
དཔེར་ན་སྒྲ་ལ་མིག་གི༌[^711]གཟུང་བྱ་མ་ཡིན་པ་དང་མངོན་སུམ་པ་ཉིད་དག་ལས་སྒྲ་ནི་རྫས་ཀྱང་མ་ཡིན་ལ། ལས་ཀྱང་མ་ཡིན་ནོ་ཞེས་ངེས་པ་ཡིན་ནོ། །

[Block 951]
དེའི་ཕྱིར་བརྗོད་པར་འདོད་པ་གཅིག་ཉིད་དོ། །

[Block 952]
གལ་ཏེ་འདི་ལྟར་བརྗོད་པར་འདོད་པ་གཅིག་ཉིད་ལས་ཐེ་ཚོམ་དང་ངེས་པ་གཉིས་དག་ཏུ་ནི་མི་འགྱུར་རོ་ཞེ་ན། སྐྱོན་དེ་ནི་མེད་དེ། གང་གི་ཕྱིར།

[Block 953]
མཚན་ཉིད་གཉིས་དང་ལྡན་པ་ནི། །གཉིས་གཉིས་སུ་འདོད་རེ་རེ་མིན། །

[Block 954]
འདིར་ནི་ཐེ་ཚོམ་དང་གཏན་ལ་དབབ་པ་དེ་གཉིས་ཀའི་མཚན་ཉིད་དང་ལྡན་པར་འཐད་ཀྱི་ཁ་ཡར་དུ་མ་ཡིན་ནོ། །

[Block 955]
འདིར་ཐེ་ཚོམ་གྱི་མཚན་ཉིད་ཅི་ཞིག་ཡིན་ཞེ་ན། འགལ་བ་མི་འཁྲུལ་བ་ཅན་ནོ། །

[Block 956]
རེ་ཞིག་གཅིག༌[^712]ལ་ནི་ཐེ་ཚོམ་གྱི་མཚན་ཉིད་མེད་པ་ནས༌[^713]ཐེ་ཚོམ་གྱི་མཚན་ཉིད་དང་ལྡན་པ་ལ་འཐད་པ་ཡིན་པའི་ཕྱིར་གཅིག་ཉིད་ཡིན་ནོ། །

[Block 957]
དེ་ལྟ་ན་ནི་མིག་གི༌[^714]གཟུང་བྱ་མ་ཡིན་པ་ཉིད་དང་མངོན་སུམ་མ་ཡིན་པ་ཉིད༌[^715]དག་དང་ལྡན་པའི་གཏན་ཚིགས་ཀྱི༌[^716]མཚན་ཉིད་ཇི་སྐད་བརྗོད་པ་ལྟར་ཡིན་གྱི་ཁ་ཡར་བ་ལ༌[^717]ནི་མ་ཡིན་ནོ། །

[Block 958]
གལ་ཏེ༌[^718]འདི་ལྟར་འགལ་བ་མེད་པ་རེ་རེ་ཞིག༌[^719]གཏན་ཚིགས་ཀྱི་མཚན་ཉིད་དུ་རིགས་ཀྱི། འདི་དཔེར་ན་བྱས་པའི་ཕྱིར་མི་རྟག་གོ། །

[Block 959]
རྩོལ་བ་ལས་བྱུང་བའི་ཕྱིར་མི་རྟག་གོ་ཞེས་བྱ་བ་ལྟ་བུ་དུ་མ་ལས་ཇི་ལྟར་ངེས་པར་སྐྱེ་ཞེ་ན།

[Block 960]
དུ་མ་ཡིན་ཡང་མི༌[^720]འགལ་ན། །ཤིན་ཏུ་བར་ཡང་གཅིག་ལ་འཇུག །

[Block 961]
འདིར་ནི་དུ་མ་ཡིན་ཡང་དོན་གཅིག་བྱེད་པའི་ཕྱིར་གཅིག་ཉིད་དོ་ཞེས་པ་འགལ་བ་མེད་དེ། དཔེར་ན་དོན་གཅིག་བརྗོད་པར་འདོད་པ་པོ་རྣམས་ན་རེ་འདི་ལ་ནི་ཁོ་བོ་ཅག་གཅིག་པ་ཡིན་ནོ་ཞེས་བརྗོད་པ་བཞིན་ནོ། །

[Block 962]
གལ་ཏེ་གང་དུ༌[^721]འདི་ལྟར་གཉིས་ཀྱི་དོན་དུ་མ་བྱེད་པར་གྱུར་པ་ནི་དཔེར་ན་བྱས་པའི་ཕྱིར་མི་རྟག་གོ། །

[Block 963]
སྡུག་བསྔལ་བའི་ཕྱིར་བདག་མེད་དོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 964]
དེ་ལ་ནི་འགལ་བ་མི་འཁྲུལ་བ་ཅན་བཞིན་ཐེ་ཚོམ་དུ་ཐལ་བར་འགྱུར་རོ་ཞེ་ན། དེ་ནི་ཡོད་པ་མ་ཡིན་ཏེ། དེ་ལ་ནི་རེ་རེས་ཀྱང་དོན་དུ་མ་བྱེད་པའི་ཕྱིར་སྔར་བཞིན་གཅིག་མ་ཡིན་པ་ལ་འཇུག་པ༌[^722]ཤིན་ཏུ་ཡང་རིགས་སོ། །

[Block 965]
གལ་ཏེ་གང་དུ་འདི་ལྟར་བསྒྲུབ་བྱ་དུ་མ་གཏན་ཚིགས་ཐ་དད་ཀྱིས་སྒྲུབ་པར་བྱེད་པ་ནི་དཔེར་ན་ཡན་ལག་ལས་ཡན་ལག་ཅན་གཞན་ཡིན་ཏེ། ཐེ་ཚོམ་དང་གཏན་ལ་ཕེབས་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ལྟ་བུའོ་ཞེ་ན། དེ་ལ་ཡང་ཕན་ཚུན་དུ་བརྟེན་པ་ལ་ལྟོས་ནས་གཉིས་ཀ་ལ་ཞུགས་པའི་གཞན་ཉིད་གཏན་ཚིགས་གཅིག་པ་ཉིད་ཡིན་ནོ། །

[Block 966]
བསྡུས་ན་ནི་གཏན་ཚིགས་ཀྱི༌[^723]མཚན་ཉིད་དང་ལྡན་པ་གཉིས་ཀ་སྒྲུབ་པ་ཡིན་པས་ན་ཉེས་པ་མེད་དོ། །

[Block 967]
གལ་ཏེ་རྣམ་པ་བཞི་པོ་ཐེ་ཚོམ་གྱི་གཏན་ཚིགས་སུ་འགྱུར་བ་ནི་གཉིས་ཀ་ལ་ཡོད་པའི་ཕྱིར་ཡིན་ན། འོ་ན་མཉན་པར་བྱ་བ་ཉིད་ཇི་ལྟར༌[^724]ཞེ་ན། ཐུན་མོང་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 968]
གང་ཐུན་མོང་མ་ཡིན་པའི་བསྒྲུབ་པར་བྱ་བའི་ཆོས་དང་ཅིག་ཤོས་དེས་ཐ་དད་པའི་དངོས་པོ་ཐམས་ཅད་བསུས་པའི༌[^725]ཕྱིར་དེ་ལ་ཐེ་ཚོམ་གྱི་གཏན་ཚིགས་ཏེ། དེ་དང་ལྡན་པ་དེས་བསྡུས་པའི་ཕྱིར་རོ། །

[Block 969]
གང་མཐའ་གཅིག་ལས་ཀྱང་མ་ལོག་པ་སྟེ། ཐུན་མོང་དུ་རྣམ་པར་མ༌[^726]བཅད་པའི་གཏན་ཚིགས་དེ་ནི་དེ་དག་ཉིད་ལའོ་ཞེས༌[^727]གཉིས་ཀ་དང་མི་འགལ་བས་ན་ཐེ་ཚོམ་གྱི་གཏན་ཚིགས་ཉིད་དོ། །

[Block 970]
གང་འདིར་གཉིས་ཀའི་ཆ་ལ་ངེས་པ་སྟེ༌[^728]གཏན་ཚིགས་དེ་གཞན་ལས་ལོག་པའོ་ཞེས་པ་འདི༌[^729]ཁྱད་པར་རོ། །

[Block 971]
གལ་ཏེ་གང་གི་ཚེ་སྒྲ་རྟག་པར་ཁས་ལེན༌[^730]པ་དེའི་ཚེ་འདི་གཏན་ཚིགས་ཉིད་དུ་འགྱུར་རོ་ཞེ་ན། གལ་ཏེ་འདི་ལ་བྱས་པའི་ཕྱིར་ཞེས་པ་ལ་སོགས་པ་མི་རྟག་པ་ཉིད་ཀྱི་གཏན་ཚིགས་སུ་ནམ་ཡང་མི་སྟོན་ནའོ། །

[Block 972]
གཉིས་ཀ་དམིགས་པའི་དོན༌[^731]ལྟར་ན་ནི་འགལ་བའི་དོན་ཡིན་པའི་ཕྱིར་ཐེ་ཚོམ་གྱི་གཏན་ཚིགས་སོ། །

[Block 973]
འདི་ཡང་དེ་ཉིད་ངེས་པ་ནི་རྗེས་སུ་ཚོལ་བ་པོ་རྣམས་ཀྱི་མངོན་སུམ་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 974]
འདིའི་བསྡུ་བའི་ཚིགས་སུ་བཅད་པ་ནི།

[Block 975 [VERSE]]
གང་དག་ཐུན་མོང་མིན་པ་དང་། །
སྤྱི་དང་འགལ་བ་མིན་འཁྲུལ་པའི། །
ཆོས་རྣམས་ཐམས་ཅད་དུ་དེ་ལ། །
ཐེ་ཚོམ་བསྐྱེད་པའི་རྟགས་རྣམས་ཡིན། །

[Block 976 [VERSE]]
ཕྱོགས་ཀྱི་ཆོས་དང་ལྡན་གང་ལ། །
ཤེས་འདོད་བཟློག་པས་གནོད་པ་དང་། །
ཐེ་ཚོམ་ཉིད་དུ་གྱུར་ལས་གཞན། །
གཏན་ཚིགས་ལྟར་སྣང་ཡོད་མ་ཡིན། །

[Block 977]
གལ་ཏེ་འདི་ལྟར་འདོད་པ་ལ་གནོད་པ་བྱེད་པའི་འགལ་བ་དེ་བཟློག་པའི་གཏན་ཚིགས་སོ་ཞེས་ཇི་ལྟར་བརྗོད་པར་བྱ་ཞེ་ན། གལ་ཏེ་གཞན་མ་ཡིན་པའི་དོན་བྱེད་པ་ཉིད་གང་ཡིན་ན་གང་གི་ཕྱིར་མི་འགྲུབ་པར་འགྱུར། གལ་ཏེ་གཞན་གྱི་དོན་བྱེད་པའི་གཏན་ཚིགས་ཡོད་པའི་ཕྱིར་རོ། །

[Block 978]
དེ་བཞིན་དུ་བྱས་པའི་ཕྱིར་མི་རྟག་གོ་ཞེས་པ་ལ་བྱས་པས་མི་རྟག་པ་འགྲུབ་པར་འགྱུར་ཏེ། རྟགས་ཉིད་དུ་སྒྲུབ་པའི་གཏན་ཚིགས་མཉན་པར་བྱ་བ་ཉིད་ཡིན་པའི་ཕྱིར་རོ་ཞེ་ན། རྒལ༌[^732]བ་འདི་ནི་མི་བཟད་པར་བཀོད་པ་སྟེ། དེ་ལ་ནི་རྟག་པ་ཉིད་ཀྱི་གཏན་ཚིགས་དང་ལྡན་པ༌[^733]གཅིག་གཟུང་བའི་ཕྱིར་སྒྲུབ་པར་བྱེད་པ་མ་ཡིན་པ་ཉིད་དུ་འགྱུར་རོ། །

[Block 979]
གལ་ཏེ་འདི་ལྟར་གཅིག་པོ་དེ་ལ་བསྒྲུབ་བྱའི་བྱེ་བྲག་གིས་གཉིས་སུ་རྟོག་པར༌[^734]བྱེད་དེ། དཔེར་ན་མིག་གི༌[^735]གཟུང་བྱ་མ་ཡིན་པ་ཉིད་དང་། མངོན་སུམ་པ་ཉིད་བཞིན་ནོ་ཞེ་ན། དེ་ལྟ་ན་ནི་འགལ་བ་མི་འཁྲུལ་བ་ཅན་ལས་ཐ་དད་པར་འགྱུར་རོ། །

[Block 980]
འདི་ལ་ཐེ་ཚོམ་མ་མཐོང་ངོ་ཞེས་བརྟག་པར་མི་བྱའོ། །

[Block 981]
འདི་ལྟར་གཞན་གྱི་དོན་བྱེད་པ་ཁྱད་པར་ཅན་ལས་བཟློག་པ་བསྒྲུབ་པའི༌[^736]ཕྱིར་དེ་ནི་འགལ་བ་ཉིད་དོ། །

[Block 982]
དེ་ལྟར་ན་འདུས་པ་གཞན་གྱི་དོན་བྱེད་པ་ལ་འདུས་པ་མ་ཡིན་པ་རྣམས་ཀྱི་དོན་བྱེད་པར་སྒྲུབ་འདོད་པ་འདི་ནི་གཞན་འདུས་པ་ཉིད་ཀྱི་རྟགས་ཡིན་ནོ། །

[Block 983]
དེའི་འདུས་པ་མ་ཡིན་པ་ཉིད་ནི་མངོན་སུམ་མམ་རྗེས་སུ་དཔག་པས་གྲུབ་པ་མ་ཡིན་ནོ། །

[Block 984]
དེ་ཡོད་པར་མ་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 985]
འདི་ནི་ཐེ་ཚོམ་མ་ཡིན་ཏེ་ཁྱད་པར་ཅན་བཟློག་པའི་གཏན་ཚིགས་འདི་ཉིད་ཀྱིས་གཞན་འགལ་བ་མི་འཁྲུལ་བ་ཅན༌[^737]ཉིད་ལས་ཐ་དད་དུ་ཕྱེ་བ་ཡིན་ནོ། །
--- END BLOCKS ---
