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
[Block 876 [VERSE]]
འདུས་བྱས་མཚན་ཉིད་སྐྱེ་བ་དང་། །
གནས་འཇིག་གསུམ་པོ་འདི་ཡང་མེད། །
གང་ཕྱིར་འདུས་བྱས་མེད་འདི་ལས། །
འདུས་མ་བྱས་པ་ཅུང་ཟད་མེད། །

[Block 877]
དེ་ལ་འདིས༌[^639]མཚོན་པར་བྱེད་པས་ན་མཚན་ཉིད་དེ། རྒྱུ་དང་རྐྱེན་འདུས་པས་ཤེས་པས།[^640] འདུས་པ་ལས་འབྱུང་བར༌[^641]བྱེད་པ་འདུས་བྱས་ལ། འདུས་བྱས་དང་མཚན་ཉིད་པས་འདུས་བྱས་ཀྱི་མཚན་ཉིད་དེ། དེ་ཅི་ཞེ་ན། སྐྱེ་བ༌[^642]གནས་དང་འཇིག་པའོ། །

[Block 878]
སྐྱེ་གནས་འཇིག་པ་ཞེས་བྱ་བ་གསུམ་པོ་དེ་ཉིད་ཀྱང་མེད་ན། གང་གི་ཕྱིར་གསུམ་པོས་འདུས་བྱས་འཇུག་པ་མེད་པར་དེ་ནི་སྔར་ཉིད་དུ་བསྒྲུབས་ཏེ།

[Block 879]
ཡོད་པ་ཡོད་ཕྱིར་སྐྱེ་བ་མིན། །མེད་པ་མེད་ཕྱིར་མི་སྐྱེ་བ། །ཞེས་པས་འདིར་གང་གི་ཚེ་གང་ལས་འདུས་བྱས་འཇུག་པ་དེའི་གསུམ་པོ་མ་གྲུབ་ན། དེའི་ཚེ་འདུས་བྱས་མ་གྲུབ་པ་དོན་གྱིས་བསྒྲུབས་པར་འགྱུར་རོ། །

[Block 880]
གང་གི་ཕྱིར་འདུས་བྱས་མེད་ན་འདི་ལས་འདུས་མ་བྱས་ཡིན་པ་ཡང་ཅུང་ཟད་ཀྱང་མེད་དོ། །

[Block 881]
དེ་ལ་གཟུགས་མེད་པས་ནམ་མཁར་ཐ་སྙད་བྱས་ལ། འདུས་བྱས་རྣམས་རྐྱེན་མ་ཚང་བས་མི་སྐྱེ་བ་ལ་སོ་སོར་བརྟགས་པ་མ་ཡིན་པའི་འགོག་པའོ། །

[Block 882]
ཟག་པ་དང་བཅས་པའི་འདུས་བྱས་རྣམས༌[^643]ཉིད་ཤེས་རབ་ཀྱི༌[^644]སྟོབས་ཀྱིས་བྲལ་བའི་མཚན་ཉིད་ཀྱི་ཐོབ་བྱའི་འགོག་པ་ནི་སོ་སོར་བརྟགས་པའི་འགོག་པའོ། །

[Block 883]
འདུས་བྱས་མེད་ན་དེ་ལ་མ་ལྟོས་པར་འདུས་མ་བྱས་ཀྱང་མེད་པའི་ཕྱིར་འདུས་མ་བྱས་མེད་དོ་ཞེས་བྱའོ། །

[Block 884]
སྨྲས་པ། སླར་ཡང་སྐྱེ་བ་ལ་སོགས་པ་གསུམ་པོ་འདི་དག་ཅི་ལྟར་མེད་ཅེས་བརྗོད། འདི་ནི་སྐྱེས་པ་བསྐྱེད་བྱ་མིན། །ཞེས་པ་ལ་སོགས་པ་བསྟན་པས་བསྒྲུབས་པ་ཡང་མ་ཡིན་ནམ། དེ་ནི་རྒྱུ་བརྟག་པ་དང་འབྲེལ་པས་འདུས་བྱས་བརྟག་པ་དང་འབྲེལ་པར་བརྗོད་ལ། ཇི་ལྟར་དེ་ལྟར་སྨོས་པས་ཀྱང་འདི་དག་གསུངས་པར་འགྱུར་ལ། གལ་ཏེ་དེ་ལྟར་ཡང་འདུས་བྱས་དང་འདུས་མ་བྱས་དག་མེད་པར་བསྟན་ན། སླར་ཡང་དེ་བསྒྲུབ་པ༌[^645]བརྩམ་པའི་ཕྱིར། འདིར་གསུངས་པ།

[Block 885 [HEADING]]
### ཚིགས་བཅད་སོ་གཅིག་པ། ^1-31-0

[Block 886 [VERSE]]
འཇིག་པ་མེད་པ་མི་འཇིག་ཅིང་། །
གནས་པ་གནས་པར་མི་འགྱུར་ལ། །
གནས་པ་མིན་པའང༌[^646]མི་གནས་ཏེ། །
སྐྱེས་པ་སྐྱེ་མིན་མ་སྐྱེས་པའང་། །

[Block 887]
འདིར་གལ་ཏེ་འཇིག་པ་ཞེས་བྱ་བ་ཅུང་ཟད་ཡོད་ན། དེ་བཞིན་གཤེགས༌[^647]པའི་དངོས་པོའམ། མི་འཇིག་པར་འགྱུར་ལ། དེ་ལ་རེ་ཞིག་འཇིག་པ་མེད་པ་ལ་མི་འཐད་དེ། ཅིའི་ཕྱིར་ཞེ་ན། གང་ལས་འཇིག་པ་མེད་པ་མི་འཇིག་སྟེ། །འཇིག་པ་མེད་པ་ཞེས་བྱ་བ་འཇིག་པ་དང་བྲལ་བ་དེ་འཇིག་པ་མེད༌[^648]ལ་འཇིག་པར་འགྱུར་རོ་ཞེས་བརྗོད་པར་ཇི་ལྟར་ནུས། དེའི་ཕྱིར་འཇིག་པ་མེད་པ་མི་འཇིག་ཅིང་། །ད་ནི་ཞིག་པའང་འཇིག་པར་མི་འགྱུར་ཏེ། ཞིག་པ་ཞེས་བྱ་བ་ཡོད་བཞིན་པ་མ་ཡིན་པའོ། །

[Block 888]
དེ་ཡང་འཇིག་ཅེས་བརྗོད་པར་ཇི་ལྟར་རུང་། ཞིག་པ་དང་མ་ཞིག་པ་དག་ལས་གཞན་དུ་རྣམ་པར་གཞག་པ་མེད་དོ། །

[Block 889]
གང་ཞིག་འཇིག་པར་འགྱུར་ཞེས་པ་ཡང་གང་གི་ཚེ་འཇིག་པ་མེད་པ་མི་འཇིག་ཅིང་ཞིག་པ་ཡང་མི་འཇིག་པ་དེའི་ཕྱིར། འཇིག་པ་མེད་དོ་ཞེས་གྲུབ་པོ། །ད་ནི་ཇི་ལྟར་གནས་པ་ཡང་མེད་དོ་ཞེས་བསྒྲུབ་པར་བྱ་སྟེ། འདིར་འདི་དག་གནས་པར་ཡོངས་སུ་རྟོག་པ་ན། གནས་པའི་དངོས་པོའམ་མི་གནས་པའི་དངོས་པོར་ཡོངས་སུ་རྟོག །[^649]གཉི་ག་ཡང་མི་འཐད་དོ་ཞེས་བསྒྲུབ་པའི་ཕྱིར་གསུངས་པ།

[Block 890]
གནས་པ་གནས་པར་མི་འགྱུར་ལ། །གནས་པ་མེད་པའང་མི་གནས་ཏེ། །ཞེས་པ་ལ། རེ་ཞིག་གནས་པའི་དངོས་པོ་ལ་གནས་པ་མེད་དེ། གནས་པར་བྱ་བ་དང་བྲལ་བའི་དངོས་པོ༌[^650]གནས་པ་ཞེས་བརྗོད་ལ། གནས་པ་ལ་གནས་པའི་བྱ་བ་དང་བྲལ་བ་མི་སྲིད་པས་དེའི་ཕྱིར་གནས་པ་གནས་པར་མི་འགྱུར་རོ། །

[Block 891]
གནས་པ་མེད་པའང་གནས་པའི་བྱ་བ་དང་བྲལ་བའོ། །

[Block 892]
གང་ཡང་གནས་པའི་བྱ་བ་དང་བྲལ་བ་དེ་ཇི་ལྟར་གནས་པར་འགྱུར། དེའི་ཕྱིར་གནས་པ་ཡང་མེད་དོ། །

[Block 893]
ད་ནི་སྐྱེ་བ་མི་སྲིད་པར་བསྒྲུབ་པའི་ཕྱིར་གསུངས་པ། སྐྱེས་པ་སྐྱེ་མིན་མ་སྐྱེས་པའང་། །ཞེས་པ་ལ། སྐྱེས་པ་རེ་ཞིག་མི་སྐྱེ་སྟེ། །སྐྱེ་བའི་བྱ་བ་དང་བྲལ་བའི་ཕྱིར་རོ། །

[Block 894]
མ་སྐྱེས་པའང་མི་སྐྱེ་སྟེ། །སྐྱེ་བའི་བྱ་བའི་ཡུལ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 895]
དེས་ན་འདུས་བྱས་མེད་ལ། དེ་མ་གྲུབ་ན། འདུས་མ་བྱས་ཀྱང་མེད་དོ་ཞེས་གྲུབ་པོ། །གལ་ཏེ་ན་ཡང་འདུས་བྱས་སམ། འདུས་མ་བྱས་གང་ཅུང་ཟད་ཡོད་ན། དེ་ངེས་པར་ཐ་དད་པའམ་ཐ་མི་དད་པ་ཞིག་གྲང་། གཉི་ག་ཡང་མི་འཐད་དོ་ཞེས་བསྒྲུབ་པའི་ཕྱིར་གསུངས་པ།

[Block 896 [HEADING]]
### ཚིགས་བཅད་སོ་གཉིས་པ། ^1-32-0

[Block 897 [VERSE]]
འདུས་བྱས་འདུས་མ་བྱས་པ་དག །
དུ་མ་མ་ཡིན་གཅིག་མ་ཡིན། །
མེད་མིན་ཡོད་མིན་ཡོད་མེད་མིན། །
མཚམས་འདིར་སྣ་ཚོགས་ཐམས་ཅད་འདུས། །

[Block 898]
རེ་ཞིག་འདུས་བྱས་དང་འདུས་མ་བྱས་དག་ཐ་དད་པར་གྲུབ་པ་མེད་ལ། གལ་ཏེ་ཡོད་ན་འདུས་བྱས་ལ་མ་ལྟོས་པར་འདུས་མ་བྱས་ཡོད་དེ། བུམ་པ་ལས་གཞན་པ་སྣམ་བུའི་རང་གི་ངོ་བོ་གྲུབ་པས་བུམ་པ་ལ་མི་ལྟོས་པ་བཞིན་ནོ། །

[Block 899]
འདུས་བྱས་ལ་མ་ལྟོས་པར་འདུས་མ་བྱས་ཀྱི་རང་གི་ངོ་བོ་གྲུབ་པ་མི་སྲིད་ལ། ཇི་ལྟར་མི་སྲིད་པ་དེ་ལྟར་ཡང་སྔར་བསྒྲུབས་སོ། །

[Block 900]
གཞན་ཡང་འདུས་མ་བྱས་ཀྱི་སྒྲས། འདུས་བྱས་རྣམ་པར་བཅད་ནས་རང་གི་དོན་རྟོགས་པར་བྱེད་དེ། འདི་ནི་འདུས་བྱས་མ་ཡིན་ལ་འོན་ཀྱང་འདུས་མ་བྱས་སོ་ཞེས་པའོ། །

[Block 901]
གང་གི་ཚེ་ཡང་དེ་དེ་ལྟར་ན་དེའི་ཚེ་འདུས་བྱས་ཁོ་ན་ལ་ལྟོས་ནས་འདུས་མ་བྱས་རྣམ་པར་གཞག་ལ། དུ༌[^651]མ་གྲུབ་པར་མི་འཐད་དོ། །

[Block 902]
འདུས་བྱས༌[^652]འདུས་མ་བྱས་དག་འགལ་བས་ཀྱང་འགལ་ཟླའི་དངོས་པོ་གཞན་ལ་མ་ལྟོས་པར་རང་ཉིད་དང་འགལ་བ་མི་རིགས་སོ་ཞེས་བྱ་སྟེ། དེས་ན་ཡང་འདུས་བྱས་ལ་མ་ལྟོས་པར་འདུས་མ་བྱས་མི་སྲིད་དོ། །

[Block 903]
དེ་བཞིན་དུ་འདུས་བྱས་ལ་ཡང་བརྗོད་དོ་ཞེས་བྱ་སྟེ། དེ་ལྟར་ན་རེ་ཞིག་དུ་མ་འདུས་བྱས་དང་འདུས་མ་བྱས་མ་ཡིན་ནོ། །

[Block 904]
ད་ནི་གཅིག་ཉིད་ལ་ཡང་འདུས་བྱས་དང་འདུས་མ་བྱས་དག་མེད་དེ། སྣང་བ་དང་མུན་པ་བཞིན་ཕན་ཚུན་འགལ་བར་ཁས་བླངས་པའི་ཕྱིར་དང་། མཚན་ཉིད་ཐ་དད་པར་ཁས་བླངས་པའི་ཕྱིར་དང་། གཉིས་ཉིད་དུ་ཁས་བླངས་པའི་ཕྱིར་རོ། །

[Block 905]
གཞན་ཡང་འདུས་བྱས་ཞེས་བྱ་བ་ཅུང་ཟད་ཡོད་ན། དེ་ཡོད་པའམ་མེད་པའམ་ཡོད་མེད་སྐྱེ། དེ་ལ་རེ་ཞིག་ཡོད་པ་མི་སྐྱེ་སྟེ་ཡོད་བཞིན་པའི་ཕྱིར་རོ། །

[Block 906]
མེད་པ་ཡང་མི་སྐྱེ་སྟེ་མེད་བཞིན་པའི་ཕྱིར་རོ། །

[Block 907]
ཡོད་མེད་ཀྱང་མི་སྐྱེ་སྟེ་ཕན་ཚུན་འགལ་བ་དག་གཅིག་པ་མི་སྲིད་དོ། །

[Block 908]
ཡང་ན་གལ་ཏེ་འདུས་བྱས་ཞེས་བྱ་བ་ཅུང་ཟད་ཡོད་ན། དེ་ཡོད་པའམ་མེད་པའམ་ཡོད་མེད་དུ་ཡོད་པར་འགྱུར་ལ། དེ་ལ་རེ་ཞིག་ཡོད་པ་མ་ཡིན་ཏེ། ཡོད་པ་རྒྱུ་ལ་མི་ལྟོས་པའི་ཕྱིར་དང་། རྒྱུ་མེད་པ་ལ་ཡོད་བཞིན་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 909]
ཇི་སྲིད༌[^653]དུ། འཕགས་པ་ལྷས།

[Block 910 [VERSE]]
མ་བརྟེན་ཡོད་པ་ནམ་ཡང་ནི། །
འགའ་ཞིག་གང་ནའང་ཡོད༌[^654]མ་ཡིན། །
ནམ་ཡང་འགའ་ཞིག་གང་ན་ཡང་། །

[Block 911]
མེད་པ་དེས་ན་རྟག་མ་ཡིན།[^655] །ཞེས་སོ། །

[Block 912]
མེད་པ་ཡང་མ་ཡིན་ཏེ། ངོ་བོ་ཉིད་མ་གྲུབ་པ་ཁོ་ནས་དངོས་པོ་མེད་པ་ཡང་མེད་པའི་ཕྱིར་རོ། །

[Block 913]
དངོས་པོ་རབ་ཏུ་མ་གྲུབ་ན། །དངོས་མེད་འགྲུབ་པར་ག་ལ་འགྱུར། །ཞེས་པའི་ཚིག་ལས་སོ། །

[Block 914]
ཡོད་མེད་ཀྱང་མ་ཡིན་ཏེ། གཅིག་ལ་འགལ་བའི་ཆོས་གཉིས་ཀྱི་བདག་ཉིད་ཅན་མེད་པའི་ཕྱིར་རོ། །

[Block 915]
དེ་བཞིན་དུ་འདུས་མ་བྱས་ལ་ཡང་བརྗོད་པར་བྱའོ། །
--- END BLOCKS ---
