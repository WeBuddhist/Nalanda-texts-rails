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
[Block 946]
དེ་བཞིན་དུ་རྩ་བ་ལས་ཀྱང་།

[Block 947 [VERSE]]
ཕུང་པོ་ཁམས་དང་སྐྱེ་མཆེད་རྣམས། །
སྐྱེ་བ་མེད་པར་རྟོགས་གྱུར་པའི། །
རང་བཞིན་སྟོང་པ་ཉིད་ཤེས་པ། །
ཤེས་རབ་ཅེས་ནི་ཡོངས་སུ་བཤད། །

[Block 948]
ཅེས་སྨྲས་ཏེ། ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད་དུ་ཕྱི་ནང་གི་ཆོས་ཐམས་ཅད་འདུས་པ་ཡིན་ཏེ། བཅོམ་ལྡན་འདས་ཀྱི་ཞལ་ནས། བྲམ་ཟེ་ཐམས་ཅད་ཐམས་ཅད་ཅེས་བྱ་བ་ནི་ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད་རྣམས་སོ་ཞེས་གསུངས་སོ། །

[Block 949]
སྐྱེ་བ་མེད་པ་ནི་འོག་ནས་འཆད་པར་འགྱུར་རོ། །

[Block 950]
བཤད་ཅེས་པ་ནི་སངས་རྒྱས་དང་བླ་མས་གསུངས་ཞེས་པའོ། །

[Block 951]
འདིར་སྨྲས་པ།

[Block 952 [VERSE]]
ཕ་རོལ་ཕྱིན་དང་བསྡུ་བའི་དངོས་པོ་དང་། །
ཚད་མེད་བཞི་དང་ཡན་ལག་བདུན་པ་དང་། །
ཆོས་སྤྱོད་བཅུ་དང་དགེ་བའི་ལས་རྣམས་གཞན། །
འཕགས་པའི་ནོར་བདུན་རྗེས་དྲན་དྲུག་ལ་སོགས། །

[Block 953 [VERSE]]
མཎྜལ་ཚ་ཚ་སྐོར་བ་ལ་སོགས་པ། །
ཐབས་ཡིན་ལོངས་སྤྱོད་རྫོགས་དང་སྤྲུལ་པའི་སྐུ། །
ཤེས་རབ་ཕ་རོལ་ཕྱིན་པ་གཅིག་པུ་ཉིད། །
ཤེས་རབ་ཡིན་ཏེ་ཆོས་ཀྱི་སྐུ་ཡི་རྒྱུ། །

[Block 954 [HEADING]]
## གཏན་ཚིགས་ཆེན་པོ་བཞི། ^8-0

[Block 955]
སྨྲས་པ་རིགས་ཀྱི་བུ་དེ་ལྟ་བུའི་ཤེས་རབ་ཅེས་བྱ་བ་དེ་ཚུལ་ཇི་ལྟ་བུ་ཞིག་གིས་མངོན་སུམ་དུ་བྱེད་པར་འགྱུར་ཞེ་ན། སྨྲས་པ་གཏན་ཚིགས་ཆེན་པོ་བཞིས་ཤེས་པར་འགྱུར་རོ། །

[Block 956]
བཞི་གང་ཞེ་ན། མུ་བཞི་སྐྱེ་བ་འགོག་པའི་གཏན་ཚིགས་དང་། རྡོ་རྗེ་གཟེགས་མའི་གཏན་ཚིགས་དང་། གཅིག་དང་དུ་མ་བྲལ་བའི་གཏན་ཚིགས་དང་། རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་གཏན་ཚིགས་སོ། །

[Block 957]
དེ་དག་ཀྱང་གང་ཡིན་ཞེ་ན། ཡོད་པ་སྐྱེ་བ་རིགས་མིན་ཏེ། །ཞེས་པ༌[^526]ལ་སོགས་པ་ཤློ་ཀ་བཞིས་བསྟན་ཏོ། །

[Block 958 [HEADING]]
### མུ་བཞི་སྐྱེ་བ་འགོག་པའི་གཏན་ཚིགས། ^8-1-0

[Block 959]
དེ་ལ་ཡོད་པ་སྐྱེ་བ་རིགས་མིན་ཏེ། །

[Block 960 [VERSE]]
མེད་པ་ནམ་མཁའི་མེ་ཏོག་བཞིན། །
ཉེས་པ་གཉིས་ཀར་ཐལ་འགྱུར་ཕྱིར། །
གཉིས་ཀ་དག་ཀྱང་འབྱུང་བ་མིན། །

[Block 961]
ཞེས་པས༌[^527]མུ་བཞི་སྐྱེ་བ་འགོག་པའི་གཏན་ཚིགས་བསྟན་ཏེ། འདི་ན་ཆོས་གང་དག་ཡོད་པ་དག་ནི་སྐྱེ་བར་མི་འགྱུར་ཏེ། སྐྱེས་ཟིན་པའི་ཕྱིར་རོ། །

[Block 962]
མེད་པའི་ཆོས་ཀྱང་སྐྱེ་བར་མི་འགྱུར་ཏེ། དེ་དག་རང་ཉིད་ཀྱིས་མ་གྲུབ་ཅིང་སྐྱེ་བའི་རྒྱུ་མེད་པའི་ཕྱིར་རོ། །

[Block 963]
གཉིས་ཀ་ཞེས་པའི་ཕུང་པོ་གསུམ་པ་ནི་འགའ་ཡང་འདི་ན་མེད་དོ། །

[Block 964]
འདིའི་དོན་སློབ་དཔོན་ཞི་བའི་ལྷས་ཀྱང་གསུངས་ཏེ། འདི་སྐད༌[^528]དུ།

[Block 965 [VERSE]]
དངོས་པོ་ཡོད་པར་གྱུར་པ་ལ། །
རྒྱུ་རྣམས་ཀྱིས་ནི་ཅི་ཞིག་བྱ། །
འོན་ཏེ་དེ་ནི་མེད་ན་ཡང་། །
རྒྱུ་རྣམས་ཀྱིས་ནི་ཅི་ཞིག་དགོས། །

[Block 966 [VERSE]]
བྱེ་བ་བརྒྱ་ཕྲག་རྒྱུ་ཡིས་ཀྱང་། །
དངོས་པོ་མེད་ལས་བསྒྱུར་དུ་མེད། །
གནས་སྐབས་དེ་དངོས་ཇི་ལྟ་བུ། །
དངོས་ལས་གཞན་པའང་གང་ཞིག་ཡིན། །

[Block 967 [VERSE]]
མེད་པའི་ཚེ་ན་དངོས་མེད་ན། །
ནམ་ཞིག་དངོས་པོ་འབྱུང་བར་འགྱུར། །
དངོས་པོ་སྐྱེ་བ་མེད་པ་ཡིས། །
དངོས་པོ་མེད་ནི་བྲལ་མི་འགྱུར། །

[Block 968 [VERSE]]
དངོས་པོ་མེད་དང་མ་བྲལ་ན། །
དངོས་པོ་ཡོད་པའི་སྐབས་མི་འབྱུང་། །
རང་བཞིན་གཉིས་སུ་ཐལ་འགྱུར་ཕྱིར། །
དངོས་པོ་དངོས་མེད་ཡོད༌[^529]མི་འགྱུར། །

[Block 969 [VERSE]]
དེ་བཞིན་ཆད་པ༌[^530]ཡོད་མིན་ཞིང་། །
རྟག་པར་ཡང་ནི་མི་དམིགས་སོ། །
དེ་བས་སྐྱེ་བོ་འདི་དག་ནི། །
སྐྱེ་བ་མེད་ཅིང་འགག་པ་མེད། །

[Block 970]
ཅེས་རྒྱས་པར་གསུངས་སོ། །

[Block 971 [HEADING]]
### རྡོ་རྗེ་གཟེགས་མའི་གཏན་ཚིགས། ^8-2-0

[Block 972 [VERSE]]
དངོས་པོ་རང་ལས་མི་སྐྱེ་ཞིང་། །
གཞན་དང་གཉིས་ཀ་ལས་ཀྱང་མིན། །
རྒྱུ་མེད་ལས་མིན་དེ་ཡི་ཕྱིར། །
ངོ་བོ་ཉིད་ཀྱིས་རང་བཞིན་མེད། །

[Block 973]
ཅེས་བྱ་བ་འདིས་ནི་རྡོ་རྗེ་གཟེགས་མ་བསྟན་ཏེ། འདི་ལྟར་བདག་དང་། ཕྱག༌[^531]དང་། དབང་ཕྱུག་དང་། སྐྱེས་བུ་དང་། ལས་དང་། རང་བཞིན་དང་། ཡོན་ཏན་དང་། ཚངས་པ་དང་། ཁྱབ་འཇུག་དང་། ལྷ་ཆེན་པོ་ལ་སོགས་པ་ཕྱི་དང་ནང་གི་བྱེད་པའི་སྐྱེས་བུ་དང་། གཞན་ཡང་རང་གི་སྡེ་པ་དག་ཀྱང་རྒྱུ་དྲུག་དང་། རྐྱེན་བཞིས་དངོས་པོ་སྐྱེ་བར་ཁས་ལེན་པ་དེ་དག་ནི་ལོག་པར་རྟོགས་པ་ཡིན་ཏེ། དེ་དག་དགག་པའི་ཕྱིར་འཕགས་པ་ཀླུ་སྒྲུབ་ཀྱི་ཞལ་ནས།

[Block 974 [VERSE]]
བདག་ལས་མ་ཡིན་གཞན་ལས་མིན། །
གཉིས་ལས་མ་ཡིན་རྒྱུ་མེད་མིན། །
དངོས་པོ་གང་དག་གང་ན་ཡང་། །
སྐྱེ་བ་ནམ་ཡང་ཡོད་མ་ཡིན། །

[Block 975]
ཞེས་དབུ་མའི་རྩ་བ་ཤེས་རབ་ལས༌[^532]གསུངས་སོ། །

[Block 976]
དོན་འདི་རྒྱས་པར་དེ་ཉིད་དང་དེའི་འགྲེལ་པ་ཆེན་པོ་དྲུག་དང་། ཊཱི་ཀ་ཆེན་པོ་གཉིས་དང་། དབུ་མ་རྣམ་པར་འཐག་པ་དང་།[^533] ཚིག་དོན་གསལ་བ་དང་། རྟོག་གེ་འབར་བ་དང་། དབུ་མ་ལ་འཇུག་པ་དག་ཏུ་བལྟ་བར་བྱའོ། །

[Block 977 [HEADING]]
### གཅིག་དང་དུ་མ་བྲལ་བའི་གཏན་ཚིགས། ^8-3-0

[Block 978 [VERSE]]
ཡང་ན་ཆོས་རྣམས་ཐམས་ཅད་དག །
གཅིག་དང་དུ་མས་རྣམ་དཔྱད་ན། །
ངོ་བོ་ཉིད་ཀྱིས་མི་དམིགས་པས། །
རང་བཞིན་མེད་པ་ཉིད་དུ་ངེས། །

[Block 979]
ཞེས་བྱ་བ་འདིས་ནི་གཅིག་དང་དུ་མ་དང་བྲལ་བའི་གཏན་ཚིགས་བསྟན་ཏེ། ཡང་ན་ཞེས་བྱ་བ་འདིའི་དོན་ནི་བསྟན་པའོ། །

[Block 980]
གཅིག་དང་དུ་མས་རྣམ་དཔྱད་ན། །ཞེས་པའི་དོན་ནི་སློབ་དཔོན་ཞི་བ་འཚོས་བཤད་དེ།

[Block 981 [VERSE]]
བདག་དང་གཞན་སྨྲས་དངོས་འདི་དག །
ཡང་དག་དོན་དུ་རང་བཞིན་མེད། །
གཅིག་དང་དུ་མར་བྲལ་བའི་ཕྱིར། །
རང་བཞིན་མེད་དེ་གཟུགས་བརྙན་བཞིན། །

[Block 982]
ཞེས་གསུངས་པ་དང་། སློབ་དཔོན་དཔལ་སྦས་ཀྱིས་ཀྱང་།

[Block 983 [VERSE]]
ཕྱི་དང་ནང་ན་གནས་འདི་ཀུན། །
ཡང་དག་དོན་དུ་རང་བཞིན་མེད། །
གཅིག་པ་ཉིད་དང་དུ་མ་དང་། །
བྲལ་བའི་ཕྱིར་ན་གཟུགས་བརྙན་བཞིན། །

[Block 984]
ཞེས་གསུངས་སོ། །

[Block 985]
དེ་དག༌[^534]གི་དོན་རྒྱས་པར་གཞུང་དེ་དག་ཉིད་དུ་བལྟ་བར་བྱའོ། །
--- END BLOCKS ---
