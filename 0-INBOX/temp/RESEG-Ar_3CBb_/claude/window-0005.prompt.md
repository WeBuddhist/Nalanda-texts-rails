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
[Block 176]
སྔགས་དང་སེམས་དང་ལུས་དང་ནི། །ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་བཤད་ཟིན་ཏོ། །

[Block 177]
མདོར་བསྡུས་པ་ཞེས་བྱ་བ་འདི་ཡང་འོག་ནས་འབྱུང་བའི་དོན་ཉིད་ཡིན་ནམ་དེ་ལས་གཞན་ཞིག་ཡིན་ཞེ་ན། ཕྱོགས་དང་པོ་ལྟར་ནི་མ་ཡིན་ཏེ། དོན་མེད་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 178]
ཕྱོགས་ཕྱི་མ་ལྟར་ན་ཡང་རྒྱུད་འདི་ཉིད་ཀྱི་དོན་མདོར་བསྡུས་པ་ཞེས་འབྱུང་བའི་ཕྱིར་རོ་ཞེ་ན་མ་ཡིན་ཏེ། གང་ཟག་ཐམས་ཅད་ནི་རིགས་རྣམ་པ་གཉིས་ཏེ། དབང་པོ་རྣོན་པོ་མགོ་སྨོས་པས་གོ་བའི་གང་ཟག་དང་། དབང་པོ་རྟུལ་པོ་དོན་མཐའ་དག་ལ་གཞོལ་བའི་གང༌[^93]ཟག་གོ། །

[Block 179]
རེ་ཞིག་དབང་པོ་རྟུལ་པོ་དོན་མཐའ་དག་ལ་གཞོལ་བའི་དབང་དུ་ནི་མ་ཡིན་ཏེ། གོང་མའི་སྐྱོན་ཉིད་དུ་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 180]
འདི་ནི་དབང་པོ་རྣོན་པོ་མགོ་སྨོས་པས་གོ་བའི་དབང་དུ་བྱས་པའོ། །དེ་ཅིའི་ཕྱིར་ཞེ་ན། དབང་པོ་རྣོན་པོ་ནི་དེ་ཙམ་གྱིས་གོ་བར་འགྱུར་བ་དང་། དོན་རྒྱ་ཆེན་པོ་ལ་འཇུག་པར་མི་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 181]
དེ་བས་ན་དེ་བཞིན་གཤེགས་པའི་གསང་བ་འདུས་པའི་དོན་རྒྱ་ཆེར་བཤད་པ་འདིས་ནི་དབང་པོ་རྣོན་པོ་དང་། དབང་པོ་རྟུལ༌[^94]པོའི་གང་ཟག་གཉི་ག་གཟུང་བར༌[^95]འགྱུར་རོ། །

[Block 182]
དེ་དག་གིས༌[^96]ནི་དོན་མདོར་བསྡུས་པ་བསྟན་ཏོ། །

[Block 183]
དེ་ནས་རྒྱུད་ཀྱི་མཐའི་ཡི་གེ་ཤེས་པར་བྱ་བའི་ཕྱིར། ཤེས་ནས་མཐའ་དྲུག་ལ་འཇུག་གོ། །ཞེས་བྱ་བ་སྨོས་ཏེ། མཐའ་དྲུག་ལ་འཇུག་པ་ཡིན་པས་ན་མཐའ་དྲུག་ལ་འཇུག་པ་ཞེའོ།[^97] །

[Block 184]
མཐའ་དྲུག་པོ་འདི་ཡང་གང་ལ་འཇུག་ཅེ་ན། དེ་བཞིན་གཤེགས་པའི་གསང་བ་འདུས་པའི་རྒྱུད་ཆེན་པོ་ལ་སོགས་པ་ལ་འཇུག་གོ། །དེ་ཅིའི་ཕྱིར་ཞེ་ན། དེ་བཞིན་གཤེགས་པའི་རྒྱུད་ཐམས་ཅད་ནི་མཐའ་རྣམ་པ་དྲུག་ལས་མི་འདའོ། །

[Block 185]
དེ་བས་ན་དེ་བཞིན་གཤེགས་པའི་རྒྱུད་ཀྱི་མཐའི༌[^98]ཡི་གེ་ཤེས་པར་བྱ་སྟེ། དེ་ཡང་བཤད་པ།

[Block 186 [VERSE]]
ཇི་སྲིད་ཡ་ར་ལ་ཧའི་བར། །
ཀ་ག་གྷ་མཐའ་ན་ཛའི་མཐའ། །
ད་དྷའི་མཐའ་དང་མ་མཐར་བཅས། །

[Block 187]
ཞེས་པ་འདི་དག་ནི་རྣལ་འབྱོར་གྱི་རྒྱུད་ཀྱི་མིང་གི་མཐའི་ཡི་གེའོ། །

[Block 188]
འདི་དག་ནི་དཔལ་ཡེ་ཤེས་རྡོ་རྗེ་ཀུན་ལས་བཏུས་པ་ལས་ཀྱང་། བཅོམ་ལྡན་འདས་རྣལ་འབྱོར་གྱི་རྒྱུད་ཀྱི་མིང་གི་མཐའི་ཡི་གེ་གང་ལགས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། བྱམས་པ་རྣལ་འབྱོར་གྱི་རྒྱུད་དང་། རྣལ་འབྱོར་ཆེན་པོའི་རྒྱུད་རྣམས་ཀྱི་མིང་གི་མཐའི་ཡི་གེ་ནི་འདི་དག་ཙམ་དུ་ཟད་དེ། ཨ་ཀ་ཁ་ག་གྷ་ང་། ཙ་ཚ་ཛ་ཛྷ་ཉ། ཊ་ཋ་ཌ་ཌྷ་ཎ། ཏ་ཐ་ད་དྷ་ན། པ་ཕ་བ་བྷ་མ། ཡ་ར་ལ་ཝ། [^99]ཤ་ཥ་ས་ཧ་ཀྵཿབྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཀའི་མཐའ་ཅན་ནི་སུམ་ཅུ་རྩ་གཉིས་སོ། །

[Block 189]
དེ་བཞིན་དུ་ཧའི་མཐའ་ཅན་གྱི་བར་དུ་ཡང་སུམ་ཅུ་རྩ་གཉིས་སོ། །

[Block 190]
དེ་བས་ན་རྣལ་འབྱོར་དང་། རྣལ་འབྱོར་ཆེན་པོའི་རྒྱུད་ནི་སྟོང་ཕྲག་བདུན་ཅུ་རྩ་གཉིས་སོ། །

[Block 191]
ཡང་ན། ཇི་སྲིད་ཡ་ར་ལ་ཧའི་བར། །ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་ཨཱ་ལི་ཀཱ་ལི་ཡང་གཟུང་བར་བྱ་སྟེ། ཇི་སྐད་དུ། རྡོ་རྗེ་རྒྱན་གྱི་རྒྱུད་ལས་ཀྱང་།

[Block 192]
ཨཱ་ལི་ཀཱ་ལི་མཉམ་སྦྱོར་བས། །འཁོར་ལོ་བཞི་ནི་འགྲུབ་པ་ཡིན། །ཞེས་གསུངས་ཏེ། འཁོར་ལོ་བཞི་ནི་ཨཱ་ལི་ཀཱ་ལི་ལས་གཞན་མ་ཡིན་ནོ། །

[Block 193]
འཁོར་ལོ་བཞི་ལས་ནི་རྡོ་རྗེ་བཟླས་པ༌[^100]དང་། སེམས་ལ་དམིགས་པ་དང་། སྒྱུ་མ་ལྟ་བུའོ།[^101] །འོད་གསལ་བ་ལ་སོགས་པ་འབྱུང་བར་འགྱུར་རོ། །

[Block 194]
གཞན་ལས་ཀྱང་།

[Block 195]
སྙིང་གི་དབུས་ན་མི་ཤིགས་པ། །འབར་བ་མར་མེའི་རྩེ་ལྟར་འབར། །ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ལྟ་བུའོ། །

[Block 196]
གཞན་ལས་ཀྱང་།

[Block 197 [VERSE]]
འཁོར་ལོ་ས་བོན་འོད་ཟེར་ལས། །
རྡོ་རྗེ༌[^102]བཟླས་དང་སེམས་ལ་དམིགས། །
སྒྱུ་མའི༌[^103]འོད་གསལ་ཟུང་དུ་འཇུག །
ཐམས་ཅད་འདི་ལས་འབྱུང་བ་ཡིན། །

[Block 198]
ཞེས་འབྱུང་བའི་ཕྱིར། དེ་བས་ན་རླུང་ལས་ནི་རྣམ་པར་ཤེས་པ་འབྱུང་ངོ་། །རྣམ་པར་ཤེས་པ་ལས་ནི་ཉེ་བར་ལེན་པའི་ལུས་འབྱུང་ངོ་། །དེ་བས་ན་ཉམས་སུ་ལེན་པའི་རྣལ་འབྱོར་པས་ཀྱང་དང་པོ་ནི་རླུང་ལ་བསླབ་པར་བྱའོ། །

[Block 199]
དེ་ནས་ནི་རྣམ་པར་ཤེས་པ་ལ་བསླབ་པར་བྱའོ། །

[Block 200]
རྣམ་པར་ཤེས་པ་ལས་རླུང་ལ་ལོབས་པར་འདོད་པས་ཀྱང་འཁོར་ལོ་རྣམ་པ་བཞིའི་ཡི་གེའི་དོན་ཇི་ལྟ་བ་བཞིན་དུ་ཤེས་པར་བྱའོ། །

[Block 201]
ཡི་གེ་དེ་དག་ཀྱང་མཐའ་གང་དུ་འདུས་ཤེ་ན། དེ་དེའི་རྩ་བ་ཡི་གེ་གསུམ། །ཞེས་སྨོས་ཏེ། མཐའ་ཅན་གྱི་རྒྱུད་དེ་དང་དེའི་རྩ་བ་བྱེད་ཅེས་སྦྱར་རོ། །

[Block 202]
ཡི་གེ་གསུམ་པའི་ངོ་བོ་གང་ཡིན་ཞེ་ན། སྐྱེས་བུ་སྒྲ་ལ་གཞོལ་བ་རྣམས་ཀྱི་དབང་དུ་བྱས་ཏེ། ས་མ་ཛ་ཞེས་པ་ནི་འདུས་པའི་མིང་གི་ཡི་གེའོ། །

[Block 203]
ཡང་ན་སྒོམ་པ་ལ་མཆོག་ཏུ་བྱས་ཏེ། དེ་དེའི་རྩ་བ་ཡི་གེ་གསུམ། །པ་ཞེས༌[^104]པ་ནི་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་ཐབས་ཀྱི་ཡི་གེ་དང་ཤེས་རབ་ཀྱི་ཡི་གེའི་རྩ་བ་ནི་ཨོཾ་ཨཱཿཧཱུཾ་ཞེས་པ་སྟེ། དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་གསང་བའི་ཡི་གེ་གསུམ་ལས་མི་འདའོ། །

[Block 204]
ཡི་གེ་གསུམ་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་ཐོབ་པར་བྱེད་པའི་ཐབས་ལས༌[^105]མི་འདའ་ལ། ཡི་གེ་གསུམ་དུ་ཡང་ཐམས་ཅད་ཇི་ལྟར་འདུ༌[^106]ཞེ་ན། འདི་ལྟར་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་སྐུ་ནི་རྡོ་རྗེ་གསུམ་ལས་མི་འདའ་སྟེ། འདི་ལྟར་ཡི་གེ་ཨོཾ་ནི་སྐུ་རྡོ་རྗེའོ། །

[Block 205]
ཨཱཿནི་གསུང་རྡོ་རྗེའོ། །

[Block 206]
ཧཱུཾ་ནི་ཐུགས་རྡོ་རྗེའོ། །

[Block 207]
འདི་ལྟར་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ནི་སྐུ་རྣམ་པ་གསུམ་ལ་མི་འདའ་ལ། ཡི་གེ་ཨོཾ་ནི་ཆོས་ཀྱི་སྐུའོ། །

[Block 208]
ཨཱཿནི་ལོངས་སྤྱོད་རྫོགས་པའི་སྐུའོ། །

[Block 209]
ཧཱུཾ་ནི་སྤྲུལ་པའི་སྐུའོ། །

[Block 210]
དེ་བཞིན་གཤེགས་པ་བསྐྱེད་པའི་རིམ་པའི་དབང་དུ་བྱས་པ་དེ་བཞིན་ནོ། །

[Block 211]
དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་སྨིན་པར་བྱེད་པའི་དབང༌[^107]ཇི་ལྟར་འདུ༌[^108]ཞེ་ན། ཡི་གེ་ཨོཾ་ནི་བུམ་པའི་དབང་ངོ་། །ཡི་གེ་ཨཱཿནི་གསང་བའི་དབང་ངོ་། །ཧཱུཾ་ནི་ཤེས་རབ་ཡེ་ཤེས་ཀྱི་དབང་ངོ་། །དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་རིམ་པ་ལྔ་པ་ཇི་ལྟར་འདུ་ཞེ་ན། འདི་ལྟར་ཡི་གེ་ཨཱཿནི་རྡོ་རྗེ་བཟླས་པའོ། །

[Block 212]
ཧཱུཾ་ནི་སེམས་ལ་དམིགས་པ༌[^109]དང་འོད་གསལ་བ་དང་། ཟུང་དུ་འཇུག་པའོ། །

[Block 213]
ཨོཾ་ནི་སྒྱུ་མ་ལྟ་བུའི་སྐུའོ། །

[Block 214]
རྡོ་རྗེ་བཟླས་པ་འབའ་ཞིག་གི་དབང་དུ་བྱས་ཏེ། ཡི་གེ་གསུམ་ནི་འདི་ལྟར་འབྱུང་བ་དང་། འཇུག་པ་དང་གནས་པ་གསུམ་དུ༌[^110]ཡི་གེ་གསུམ་ནི༌[^111]ཅི་རིགས་སུ་སྦྱར་རོ། །

[Block 215]
སེམས་ལ་དམིགས་པ་འབའ་ཞིག་གི༌[^112]དབང་དུ་བྱས་པའི་ཡི་གེ་གསུམ་ནི་སྣང་བ་དང་། སྣང་བ་མཆེད་པ་དང་། སྣང་བ་ཐོབ་པའི་ཡེ་ཤེས་སོ། །
--- END BLOCKS ---
