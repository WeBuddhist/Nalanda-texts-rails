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
[Block 36 [VERSE]]
འདི་ཙམ་ཉི་ཤུ་ལྔ་ཤེས་ན། །
རལ་པའམ་སྤྱི་བོ་གཙུག་ཕུད་ཀྱི། །
བསྟི་གནས་གང་དུ་འགྲོ་བ་དེར། །
གྲོལ་འགྱུར་འདི་ལ་ཐེ་ཚོམ་མེད། །

[Block 37]
ཅེས་ཟེར་བ་དེ་བཟློག་པའི་ཕྱིར། མ༌[^30]ཡཱ་ནི་སྒྱུ་མའི་བདག་ཉིད་དུ་ཤེས་པར་བྱ་སྟེ། བདག་ནི་རྟག་པ་དང་གཅིག་པུ་དང་རང་དབང་དུ་འདོད་ལ། སྒྱུ་མ་ནི་དེ་དང་མཚན་ཉིད་མི་མཐུན་པས་ནི་དེ༌[^31]སྤོང་ངོ་། །ཐོས་པ་ཤྲུ་བ་ལའམ་ཤྲུ་ཏ་ཟེར་བ་ནི་མུ་སྟེགས་ཀྱི་རིག་བྱེད་པ་སྒྲ་ཡོན་ཏན་དུ་འདོད་པ་སྒྲས་ཆོག་པར་འཛིན་ཏེ། །

[Block 38]
དེའི་ལུང་ལས།

[Block 39 [VERSE]]
ཉེས་པ་རྣམས་དང་འབྲེལ་བའི་ཕྱིར། །
སྐྱེས་བུ་མ་བྱས་བདེན་དོན་ཅན། །

[Block 40]
ཞེས་སྒྲ་རྟག་པར་འདོད་པ་དེ་སྤོང་སྟེ། ཤྲུ་ཏ་རྒྱུ་བས་མ་ཤྲུ་ཏ་རིག་པ་ཤེས་པས་སྒྲ་རྟག་པ་དེ་ཐོས་བྱ་དང་ཐོས་བྱེད་ཀྱི་འབྲེལ་པ་མི་འཐད་པས་ན་དེ་བཟློག་གོ། །དུས་གཅིག་ན་ཨེ་ཀ་ཀཱ་ལ་མི་ཟེར་པར༌[^32]ས་མ་ཡ་ཟེར་བ་ནི་དུས་ཡོན་ཏན་དུ་འདོད་པ་ཡོད་དེ།

[Block 41]
དེ་ཡང་།

[Block 42 [VERSE]]
སྐྱེ་དགུ་འདི་དག་དུས་ཀྱིས་བསྡུས། །
དངོས་པོ་འདི་དག་དུས་ཀྱིས་བྱེད། །

[Block 43]
ཅེས་ཟེར་ཏེ། རིགས་པ་ཅན་ལ་སོགས་པ་འདོད་པ་བཟློག་པ༌[^33]སྟེ། ས་མ་ཡ་ནི་དམ་ཚིག་དེ་དུས་དང་མཉམ་པའི་དུས་དང་། ཡ་ཡོ་ག་སྦྱོར་བར་འགྲོ་བས་ན་དུས་རྟག་པ་ནི་དེ་དག་དང་འགལ་བས་ན་བཟློག་གོ། །

[Block 44]
དེ་སྐད་དུ་ཡང་།

[Block 45 [VERSE]]
དུས་ནི་རྣམ་པ་གསུམ་ཡིན་ཏེ། །
བདེ་བའི་དུས་དང་ངན་པའི་དུས། །
བསམ་གྱིས་མི་ཁྱབ་དུས་ཡིན་ཏེ། །

[Block 46]
ཞེས་གསུངས་སོ། །

[Block 47]
བི་ཛ་ཧ་རཾ་ལ་སྟ་ནའམ་སྟི་སྟི་བེ་སེ་པ་མི་ཟེར་བ་ནི་ཐེར་ཟུག་པའི་རྟག་པ་སྤོང་སྟེ། གྲངས་ཅན་ལ་སོགས་པ་རྫ་ཆག་བྱེ་འཕུར་དུ་འདོད་པ་སྟེ། ཧ་རས་སྤོང་སྟེ་རྗེས་སུ་མཐུན་པས་སྟོན་ཏེ། འཕགས་པའི་ཚུལ་དུ་བཞིས་བཞུགས་པ་དང་ཧ་རས་འཕྲོག་བྱ་དང་ཕྲོག་བྱེད་དུ་བཞུགས་པའམ། བི་ཛི༌[^34]ཡང་ཡོན་ཏན་དང་འཇོམས་པར་བཞུགས་པའོ། །

[Block 48 [HEADING]]
##### དོན་བཞིན་དུ་བཤད་པ། ^1-1-1-2-0

[Block 49]
དོན་བཞིན་དུ་བཤད་པ་ནི་གཉིས་ཏེ། །བཤད་ཚུལ་སོ་སོར་སྦྱོར་བ་དང་བརྟག་པ་ཕྱི་མའི་ཚུལ་གྱིས་མདོར་བསྡུས་ཏེ་བསྟན་པའོ། །

[Block 50 [HEADING]]
###### བཤད་ཚུལ་སོ་སོར་སྦྱོར་བ། ^1-1-1-2-1-0

[Block 51]
བཤད་ཚུལ་སྦྱར་བ་ནི་བསྐྱེད་རིམ་དང་རྫོགས་རིམ་མོ། །

[Block 52 [HEADING]]
###### **བསྐྱེད་རིམ།** ^1-1-1-2-1-1-0

[Block 53]
བསྐྱེད་རིམ་དམིགས་པར་བྱ་བའི་ཡུལ་གླེང་གཞི་བསྟན་པ་དང་། ཉམས་སུ་ལེན་པའི་ཐབས་བསྟན་པའོ། །

[Block 54 [HEADING]]
###### **དམིགས་པར་བྱ་བའི་ཡུལ་གླེང་གཞི་བསྟན་པ།** ^1-1-1-2-1-1-1-0

[Block 55]
གླེང་གཞི་ནི་འདི་སྐད་བདག་གིས་ཐོས་པ་ཞེས་བྱ་བས་ནི་སྡུད་པ་པོ་ཕུན་སུམ་ཚོགས་པ་སྟོན་ཏོ།[^35] །སྔར་བསྟན་པའི་ཡོན་ཏན་དང་ལྡན་པའི་ས་བཅུའི་བྱང་ཆུབ་སེམས་དཔའ་རྡོ་རྗེ་སྙིང་པོའོ། །

[Block 56]
དུས་གཅིག་ནི༌[^36]ཕུན་སུམ་ཚོགས་པ་སྟེ། སྟོན་པ་གནས་དང་འཁོར་ལ་སོགས།[^37] །འདུས་པ་དུས་ཞེས་བཤད་པ་ཡིན། །ཞེས་པ་མདོ་ལ་སོགས་པ་ལྟར་དཔྱིད་ཟླ་ར་བ་ལ་སོགས་པ་བསྟན་པ་བཞིའི་དུས་སོ། །

[Block 57]
སྟོན་པ་ནི་བྷ་ག་ཝཱན་ཏེ་གོང་མ་ལྟར་སྤངས་པ་དང་། ཡེ་ཤེས་ཏེ་དེ་དང་ལྡན་པའི་རྒྱུའི་རྡོ་རྗེ་འཆང་རིགས་བདུན་པ་སྟེ་དེ་ཡང་འོག་ཏུ་འཆད་དེ།

[Block 58 [VERSE]]
ཞལ་བརྒྱད་ཕྱག་ནི་བཅུ་དྲུག་སྟེ། །
དཔའ་བོ་ཐོད་པའི་ཕྲེང་བ་ཅན། །
ཕྱག་རྒྱ་ལྔ་ནི་འཛིན་ལྷ་ལ། །
བདག་མེད་མ་ནི་ཉིད་ཀྱིས་ཞུས། །

[Block 59]
གསུངས་པས་དེའི་དགོངས་པ་ཡང་རྒྱུའི་རྡོ་རྗེ་འཆང་འཆད་པ་པོར་འདོད་དོ། །

[Block 60]
གནས་ཕུན་སུམ་ཚོགས་པ་ནི་སརྦ་ཏ་ཐཱ་ག་ཏ་ནས་བྷ་ག་ག་ལའི་བར་ཏེ་ཁྲོ་བ་དང་ཆགས་པས་འདུལ་བ་ལ་ཕྱི་ཆོས་འབྱུང༌[^38]བ་དེར་ཐོས་སོ། །

[Block 61]
འཁོར་ཕུན་སུམ་ཚོགས་པ་ནི་རྣལ་འབྱོར་གྱི་དབང་ཕྱུག་བྱེ་བྲག་བརྒྱད་ཅུ་སྟེ། རིགས་ལྔ་དང་བྱང་ཆུབ་སེམས་དཔའ་ས་བཅུ་ལ་གནས་པ་རྣམས༌[^39]དང་། རྡོ་རྗེ་བདག་མེད་མ་དང་སྤྱན་ལ་སོགས་པ་སངས་རྒྱས་ཀྱི་སྤྲུལ་པ་རྡོ་རྗེ་མཁའ་འགྲོ་མ་རི་རབ་ཀྱི་རྡུལ་ཕྲ་རབ་དང་མཉམ་པ་རྣམས་ཏེ། དེ་ཡང་འོག་ལྡན་མ་དང་སྟེང་ཞལ་མ་ལ་སོགས་པས་འཆད་དོ། །

[Block 62 [HEADING]]
###### **ཉམས་སུ་ལེན་པའི་ཐབས་བསྟན་པ།** ^1-1-1-2-1-1-2-0

[Block 63]
དེ་ལྟ་བུར་བདག་གིས་ཐོབ་པར་བྱ་སྙམ་དུ་འདོད་པར་བྱ་ཞེས་བསྐྱེད་རིམ་གྱིས་དམིགས་པར་བྱས་ལ་དེ་ཉིད་ཉམས་སུ་ལེན་པ་ནི་སྒྲུབ་པ་པོ་ཐུན་མོང་དང་ཁྱད་པར་གྱི་ཡོན་ཏན་དང་ལྡན་པས། གནས་ཕུན་སུམ་ཚོགས་པ་བགེགས་དང་འཚེ་བ་མེད་པར་བྱ་བ་ལ་འཇུག་པ་སྔར་ལངས་ལ་ལྷའི་ང་རྒྱལ་གྱིས་འཆགས་ཡོད་པར༌[^40]ཕྱིན་ཏེ། བསམ་གཏན་གྱི་བར་ཆད་བསལ་ལ། འཆགས་ཆུང་ངུ་ཕྱིའི་ཁྲུས་ཙནྡན་ལ་སོགས་པ་སྦྱར་བའི་ཆུས་དབང་བསྐུར་བར་མོས་ཏེ་ཁྲུས་བྱའོ། །

[Block 64]
ནང་གི་ཁྲུས་བདུད་རྩིའི་བྱུག་པ་ལ་སོགས་པ་བྱ་བའོ།[^41] །དེ་ནས་ནང་དུ་མཎྜལ་དང་མཆོད་པ་བཤམས་ལ༌[^42]ཐང་ཀ་དང་འབུར་སྐུ་རྣམས་བཞུགས་པ༌[^43]བདག་དང་རྣལ་འབྱོར་ལ་སོགས་བསྲུང་བར༌[^44]བྱའོ། །དེ་ནས་མཆོད་པ་བྱིན་གྱིས་བརླབ་སྟེ། རང་རང་གི་ཕྱག་རྒྱ་དང་སྔགས་ཀྱི་རྫས་སུ་བྱིན་གྱིས་བརླབ་བོ། །

[Block 65]
དེ་ནས་བསོད་ནམས་ཀྱི་ཚོགས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་བསགས་ལ། རེ་ཕ༌[^45]སྔོན་དུ་ཞེས་པས་ར་བ་དྲ་བ་བསྒོམས་པའི་ནང་དུ་ཨེ་ཆོས་འབྱུང་བ་ཤྲཱི་དང་ནཱའི་གནས་ལྟ་བུར་བསམ་སྟེ་དོན་ལེའུ་བརྒྱད་པར་འཆད་དོ། །ཝཾ་གཞལ་ཡས་ཁང་འབྱུང་བས༌[^46]ཆུ་མེ་རླུང་རྣམས་ཞུ་བ་ལས་བྱུང་བ་དེ་ཡང་འོག་ནས་འཆད་དོ། །

[Block 66]
ཟེའུ་འབྲུ་དང་བཅས་པར་ཐིག་ལེ་བྱང་ཆུབ་སེམས་ལས་མ༌[^47]ཡཱ་དཀྱིལ་འཁོར་གྱི་བདག་པོ་བསྒོམ་སྟེ།

[Block 67 [VERSE]]
དེ་ཡང་ཟླ་བ་མེ་ལོང་ཡེ་ཤེས་ལྡན། །
བདུན་གྱི་བདུན་པ་མཉམ་པ་ཉིད། །
རང་ལྷའི་ས་བོན་ཕྱག་མཚན་ནི། །
སོ་སོར་རྟོག་པ་ཡིན་ཞེས་ཟེར། །

[Block 68 [VERSE]]
དེ་རྣམས་གཅིག་གྱུར་བྱ་ནན་ཏན། །
རྫོགས་པ་ཆོས་དབྱིངས་དག་པའོ། །

[Block 69]
ཞེས་བྱ་བས་མངོན་པར་བྱང་ཆུབ་པ་ལྔས་རྒྱུའི་རྡོ་རྗེ་འཆང་དུ་སྤྲུལ་ལོ། །

[Block 70]
ཤྲུ་ཏ་ནི་རིག་མ་དང་བཅས་པ་བཞུགས་པ༌[^48]ལས་བྱུང་བ་དེ་ཡང་། བར་དོར་བཞུགས༌[^49]ནས་བསྲུབ་དང་བསྲུབས་པས་གཙོ་བོ་ཞུ་རིག་མ་དང་བཅས་ཏེ་ཞུ་བའོ། །དུས་གཅིག་ནི་ཞུ་བ་དང་ལྡན་པའི་རིག་མ་དང་དུས་གཅིག་པའོ། །བཅོམ་ལྡན་འདས་ནི་གླུའི་ངོར་འབྲས་བུ་ཧེ་རུ་ཀར༌[^50]ལངས་ཏེ། ཐིག་ལེ་བཞི་ཆད་ནས་རྐྱེན་གླུས་བསྐུལ་ནས་ཡུད་ཙམ་གྱིས་མངོན་པར་བྱང་ཆུབ་པ་ལྔས་བསྐྱེད་པའོ། །དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ནི་ཉན་པའི་འཁོར་རྫོགས་པ་སྟེ། རང་བཞིན་སངས་རྒྱས་རྣམ་པ་རྡོ་རྗེ༌[^51]བཙུན་མོ་སྟེ། རྣལ་འབྱོར་མའི་འཁོར་རྗེས་སུ་མཐུན་པའི་བྱང་ཆུབ་པ་ལྔས་བསྐྱེད་པའོ། །

[Block 71]
དེ་ནས་ཉམས་དགའ་བའི་གྲོང་ཁྱེར་ཡིན་པས་བྷ་ག་སྟེ། ཉོན་མོངས་པ་རྣམ་པར་འཇོམས་པ་དག་པའི་ཡེ་ཤེས་དང་ལྡན་པས་སོ། །བཞུགས་སོ་ཞེས་བྱ་བས་ནི་སེམས་དཔའ་སུམ་བརྩེགས་དང་ཡེ་ཤེས་ཀྱི་འཁོར་ལོ་དགུག་པ་དང་། སྐྱེ་མཆེད་བྱིན་གྱིས་བརླབ་པ་ནི་གཙོ་བོ་ལ་བསྐྱེད་ཚུལ༌[^52]དུ་བསྒོམ་མོ། །སྐུ་གསུང་ཐུགས་བྱིན་གྱིས་བརླབ་པ་དང་དབང་བསྐུར་བ་དང་། མཆོད་པ་དང་བསྟོད་པ་དང་བདུད་རྩི་མྱང་བ་དང་རྫོགས་པའི་རིམ་པ་ཉུང་ལྡན་དུ་བསྒོམ་མོ། །དག་པ་རྗེས་སུ་དྲན་པ་དང་སྔགས་བཟླས་པ་དང་གཏོར་མ་དང་ཡེ་ཤེས་པ་གཤེགས་པ་དང་དམ་ཚིག་པ་བསྡུ་བ་དང་བཅས་པ༌[^53]བཞུགས་སོ། །

[Block 72 [HEADING]]
###### **ཐུན་བཞིའི་རིམ་པ།** ^1-1-1-2-1-1-2-1-0

[Block 73]
དོ་ལ་མཉམ་གཞག་དང་རྗེས་ཐོབ་ཀྱི་རྟགས་འབྱུང་སྟེ། ཐུན་བཞིའི་རིམ་པར་ཞག༌[^54]གཉིས་དང་དེ་བཞིན་ཏེ་བརྟེན་པ་ཆོས་ནས་འཇུག་པ་དང་རྟེན་དང་པོ་ནང་ནས་འཇུག་པའོ། །

[Block 74 [HEADING]]
###### **དང་པོ་བརྟེན་པ་ཆོས་ནས་འཇུག་པ།** ^1-1-1-2-1-1-2-1-1-0

[Block 75]
དང་པོ་ནི་ཨེ་སྟེ་ཆོས་ཐམས་ཅད་སྟོང་པ་ཉིད་དང་བ༌[^55]སྟེ་ཐབས་སྣང་བ་དང་། ང་སྟེ་དབྱེར་མེད་བདག་གིས་ནི་བདག་ཉིད་དུ་ཐོས་ཤིང་གསལ་བའོ། །ཤྲུ་ཏ་སྟེ་བདེ་བ་གོང་ནས་གོང་དུ་འཕེལ་བའམ་ཡང་གསལ་རིག་གི་ཆ་མ་འགགས་པའོ། །དུས་ནི་དེ་ཉིད་སྣང་བ་དང་སྟོང་པ་དབྱེར་མེད་པའི་སྒོམ་པ་སྟེ། དེ་ཡང་ཕ་རོལ༌[^56]ཕྱིན་པ་ནི་ལུང་དང་རྒྱ་མཚོ་རིགས་པས་དཔྱད་དེ་བསྒོམས་ལ། འདིར་ནི་མན་ངག་གི་སྟོབས་ཀྱིས་ཆོས་རྣམས་ལས་ཡེ་ཤེས་སྐྱེ་བའི༌[^57]ཚུལ་དུ་བསྒོམ་མོ། །
--- END BLOCKS ---
