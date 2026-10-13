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
[Block 4096]
ལུང་དུ་མ་བསྟན་པ་རྣམ་པ་གསུམ་མོ། །གང་རྟོག༌[^1584]དང་རིག་སྔགས་ཀྱིས༌[^1585]བྱས་པའང་། །

[Block 4097]
གང་ཡང་མཚན་མ་རྣམས་ཀྱིས༌[^1586]ཕ་རོལ་གྱི་སེམས་ཤེས་པ་དང་། གང་ཡང་རིག་སྔགས་ཀྱིས་བྱས་པ་དེ་ཡང་རྣམ་པ་གསུམ་མོ། །

[Block 4098]
གཞན་གྱི་སེམས་ཤེས་པ་དང་། སྔོན་གྱི་གནས་རྗེས་སུ་དྲན་པ་སྐྱེ་བས་ཐོབ་པ་དག་ནི། དམྱལ་བ་བས་ནི་དང་པོ་ཤེས། །སྡུག་བསྔལ་གྱི་ཚོར་བས་མཉེན་པའི་བར་དུའོ། །

[Block 4099]
འགྲོ་བ་གཞན་ན་གནས་པས་ནི་རྟག་ཏུ་ཤེས་སོ། །

[Block 4100]
མི་ལ་སྐྱེ་བས་ཐོབ་པ་མེད། །མི་རྣམས་ལ་ནི་རྫུ་འཕྲུལ་ལ་སོགས་པ་སྐྱེ་བས་ཐོབ་པ་མེད་དོ། །

[Block 4101]
ཡེ་ཤེས་བསྟན་པ་ཞེས་བྱ་བ་མཛོད་ཀྱི་གནས་བདུན་པའོ།། །།

[Block 4102 [HEADING]]
## སྙོམས་པར་འཇུག་པ་བསྟན་པ། ^8-0

[Block 4103 [HEADING]]
### བསམ་གཏན་དང་གཟུགས་མེད། ^8-1-0

[Block 4104]
ཤེས་པའི་གནས་སྐབས་ཀྱི་ཤེས་པའི་རང་བཞིན་གྱི་ཡོན་ཏན་རྣམས་བཤད་ནས། རང་བཞིན་གཞན་རྣམས་བརྗོད་པ། དེ་ལྟ་བས་ན༌[^1587]ཡོན་ཏན་ཐམས་ཅད་ཀྱི་རྟེན་ཡིན་པའི་ཕྱིར་དང་པོ་ཁོ་ནར་བསམ་གཏན་ལས་བརྩམས་ཏེ། བསམ་གཏན་དག་ནི་རྣམ་པ་གཉིས། །མདོར་བསྡུ་ན་སྐྱེ་བ་དང་། སྙོམས་པར་འཇུག་པའི་བྱེ་བྲག་གིས་སོ། །

[Block 4105]
དེ་དག་ཀྱང་། བཞི་བསམ་གཏན་དང་པོ་ནས་བཞི་པའི་བར་རོ། །

[Block 4106]
དེ་ལ། དེར་སྐྱེ་བ་དག་རབ་ཏུ་བཤད། །དེར་སོ་སོའི་བསམ་གཏན་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 4107 [HEADING]]
#### སྙོམས་པར་ཞུགས་པའི་བསམ་གཏན། ^8-1-1-0

[Block 4108]
སྙོམས་པར་ཞུགས་པའི་བསམ་གཏན་བརྗོད་པར་བྱ་སྟེ། སྙོམས་འཇུག་དགེ་བ་རྩེ་གཅིག་པ། །དགེ་བའི་སེམས་རྩེ་གཅིག་པ་ནི་བསམ་གཏན་ནོ། །

[Block 4109]
རྗེས་འབྲང་བཅས་ན་ཕུང་པོ་ལྔ། །འཁོར་དང་བཅས་ན་ནི་ཕུང་པོ་ལྔའི་རང་བཞིན་ཡིན་ནོ། །

[Block 4110]
ཡང་དགེ་བ་རྩེ་གཅིག་པའི་བསམ་གཏན་དང་པོ་ཇི་ལྟ་བུ། བཞི་པའི་བར་ནི་ཇི་ལྟ་བུ་ཞེ་ན། དཔྱོད་དང་དགའ་དང་བདེ་དང་ལྡན། །བསམ་གཏན་དང་པོ་ནི་དཔྱོད་པ་དང་། དགའ་བ་དང་བདེ་བ་དང་ལྡན་པ་ཡིན་ནོ། །

[Block 4111]
ལྷན་ཅིག་སྤྱོད་པའི་ཕྱིར་རྟོག་པ་དང་ཡང་ལྡན་ནོ། །

[Block 4112 [VERSE]]
བསམ་གཏན་ལྷག་མ་གསུམ་ན་ནི། །
ཡན་ལག་ལྔ་ལྔ་སྤངས་པ་ཡིན། །

[Block 4113]
གཉིས་པ་ནི་དགའ་བ་དང་། བདེ་བ་དང་ལྡན་པའོ། །

[Block 4114]
གསུམ་པ་ནི་དཔྱོད་པ་དང་དགའ་བ་སྤངས་པའོ། །

[Block 4115]
བཞི་པ་ནི་དཔྱོད་པ་དང་། དཀའ་བ་དང་བདེ་བ་སྤངས་པ་ཡིན་ནོ། །

[Block 4116 [HEADING]]
#### གཟུགས་མེད། ^8-1-2-0

[Block 4117]
བསམ་གཏན་རྣམས་ཇི་ལྟ་བར། དེ་བཞིན་གཟུགས་མེད་ཕུང་པོ་བཞི། །རྗེས་སུ་འབྲང་བའི་གཟུགས་མེད་པའི་ཕྱིར་རོ། །

[Block 4118]
འོག་མའི་ས་ལས་དབེན་ལས་སྐྱེས། །བསམ་གཏན་བཞི་པ་ལས་སྐྱེས་པ་ནི་ནམ་མཁའ་མཐའ་ཡས་སྐྱེ་མཆེད་ནས་འདུ་ཤེས་ཡོད་མིན་མེད་མིན་སྐྱེ་མཆེད་ཀྱི་བར་རང་རང་གི་འོག་མ་ལས་དབེན་པ་ལས་སྐྱེས་པ་རྣམས་སོ། །

[Block 4119]
གཟུགས་མེད་པ༌[^1588]དེ་དག་ཀྱང་།

[Block 4120 [VERSE]]
ཉེར་བསྡོགས་གསུམ་དང་བཅས་པར་ནི། །
གཟུགས་ཀྱི་འདུ་ཤེས་བཤིག༌[^1589]ཅེས་བྱ། །

[Block 4121]
ནམ་མཁའ་མཐའ་ཡས་སྐྱེ་མཆེད་ཀྱི་ཉེར་བསྡོགས་ནི་བསམ་གཏན་བཞི་པ་ལ་དམིགས་པའི་ཕྱིར་གཟུགས་ཀྱི་འདུ་ཤེས་བཤིག་པ༌[^1590]ཞེས་བྱ་བའི་མིང་མི་འཐོབ་པོ། །གཟུགས་མེད་པ་ན་གཟུགས་མེད་དོ། །

[Block 4122]
དེ་ནི་ཇི་ལྟར་ན་དེ་ནས་འཆི་འཕོ་བ་རྣམས་ཀྱི་གཟུགས་བསྐལ་པ་མི་ཉུང་བ་ཞིག་ཏུ་རྒྱུན་ཆད་པ༌[^1591]ལས་ཡང་སྐྱེ་བར་འགྱུར་ཞེ་ན། གཟུགས་ནི་སེམས་ལས་སྐྱེ་བར་འགྱུར། །གཟུགས་ནི༌[^1592]དེའི་རྣམ་པར་སྨིན་པའི་རྒྱུས་ཡོངས་སུ་བསྒོས་པའི་སེམས་འཇུག་པ་རྙེད་པ་ལས་སྐྱེ་བར་འགྱུར་རོ། །

[Block 4123]
ཅི་ནམ་མཁའ་མཐའ་ཡས་སྐྱེ་མཆེད་ལ་སོགས་པ་དེ་དག་ནམ་མཁའ་ལ་སོགས་པ་ཁོ་ན་ལ་དམིགས་པ་ཡིན་པས་དེ་སྐད་ཅེས་བྱའམ་ཞེ་ན། མ་ཡིན་ཏེ། འོན་ཀྱང་།

[Block 4124 [VERSE]]
རྣམ་ཤེས་མཐའ་ཡས༌[^1593]མཁའ་མཐའ་ཡས། །
ཅི་ཡང་མེད་ཅེས་བྱ་དེ་ལྟར། །

[Block 4125]
སྦྱོར་ཕྱིར། གྲངས་བཞིན༌[^1594]དུ་ནམ་མཁའ་མཐའ་ཡས་སོ། །

[Block 4126]
རྣམ་པར་ཤེས་པ་མཐའ་ཡས་སོ། །

[Block 4127]
ཅི་ཡང་མེད་ཅེས་ཡིད་ལ་བྱེད་ཅིང་སྦྱོར་བའི་ཕྱིར་དེ་དག་གི་མིང་དེ་སྐད་ཅེས་བྱའོ། །

[Block 4128]
དམན་ཕྱིར་འདུ་ཤེས་མེད། འདུ་ཤེས་མེད་པའང་མ་ཡིན་ནོ། །

[Block 4129]
འདུ་ཤེས་ཆུང་བའི་ཕྱིར་འདུ་ཤེས་མེད་འདུ་ཤེས་མེད༌[^1595]མིན་ཞེས་བྱའོ། །

[Block 4130 [HEADING]]
#### སྙོམས་འཇུག་དངོས་གཞིའི་རྫས། ^8-1-3-0

[Block 4131]
དེ་ལྟར་སྙོམས་འཇུག་དངོས་གཞིའི༌[^1596]རྫས། །རྣམ་པ་བརྒྱད། བསམ་གཏན་བཞི་དང་། གཟུགས་མེད་པ་བཞིའོ། །

[Block 4132]
དེ་དག་ལས།

[Block 4133]
བདུན༌[^1597]རྣམ་པ་གསུམ། སྲིད་པའི་རྩེ་མོ་ལས་གཞན་པ་བདུན་ནི་རྣམ་པ་གསུམ་ཡིན་ཏེ། རོ་མྱང་ལྡན་དང་དག་པ་དང་། །ཟག་མེད། རོ་མྱོང༌[^1598]བ་དང་མཚུངས་པར་ལྡན་པ་དང་། དག་པ་བ་དང་། ཟག་པ་མེད་པ་རྣམས་སོ། །

[Block 4134]
བརྒྱད་པ་རྣམ་པ་གཉིས། ཟག་པ་མེད་པ་མ་གཏོགས་སོ། །

[Block 4135]
དེ་ལ།
--- END BLOCKS ---
