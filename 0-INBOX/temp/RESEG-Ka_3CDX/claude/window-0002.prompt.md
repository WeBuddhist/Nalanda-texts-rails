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
[Block 71]
གང་དག་རང་གི་ཕྱོགས་གྲུབ་པར་བྱ་བའི་ཕྱིར། མི་མཐུན་པའི་ཕྱོགས་གཅིག་ལ་ཡོད་པ་ལ༌[^51]ཡང་གཏན་ཚིགས་སུ་རྟོགས་པར༌[^52]བྱེད་དེ། འདི་ལྟ་སྟེ། སྒྲ་ནི་རྟག་པ་སྟེ། བརྩལ་མ་ཐག་ཏུ་འབྱུང་བ་ཡིན་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལྟ་བུ་དེ་རྣམ་པར་གཅད་པའི་ཕྱིར་ངེས་པའི་གཟུང༌[^53]བ་ཡིན་ནོ། །

[Block 72]
གཉི་གར་ཡང་ཁྱད་པར་ཅན་གྱི་གནས་སུ་ངེས་པར་གཟུང་བ་ནི་བརྩལ་མ་ཐག་ཏུ་འབྱུང་བ་ལ་སོགས་པ་མཐུན་པའི་ཕྱོགས་གཅིག་ལ་ཡོད་པ་ཡང་མི་རྟག་པ་ཉིད་ལ་སོགས་པ༌[^54]སྒྲུབ་པ་ཉིད་དུ་འགལ་བ་མེད་དོ་ཞེས་བྱ་བ༌[^55]རབ་ཏུ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 73]
ཚུལ་གསུམ་པའི་དངོས་ཀྱི་ཚུལ་དུ་ཡོད་ཀྱང་ཇི་སྲིད་དུ་རྟོགས་པར་མ་གྲུབ་པ༌[^56]དེ་སྲིད་དུ་དེ་ལ༌[^57]བསྒྲུབ་པར་བྱ་བ་རྟོགས་པར་མི་འགྱུར་རོ་ཞེས་བྱ་བ༌[^58]རབ་ཏུ་བསྟན་པའི་ཕྱིར། ངེས་པའི༌[^59]ཞེས་བྱ་བ་སྨོས་པ་ཡིན་ཏེ། དེ་བཞིན་དུ་དཔེར་བརྗོད་པ་ཡང་འདི་ཉིད་ལས་སྟོན་པར་འགྱུར་རོ། །

[Block 74]
རྗེས་སུ་དཔག་པར་བྱ་བ་ཆོས་དང་ཆོས་ཅན་གྱི་སྤྱི་ཡིན་པའི་ཕྱིར། དེ་མ་གྲུབ་པ་དེ་ལ་རྟག་པ༌[^60]ཡོད་པ་རྟག་ཏུ་མ་གྲུབ་པ་ཁོ་ནའོ། །

[Block 75]
འོན་ཏེ་སྒྲུབ་ན་ནི་བསྒྲུབ་པར་བྱ་བ་སྔ་ཉིད་ནས་གྲུབ་པའི་ཕྱིར། རྟགས་ཀྱི་རྗེས་སུ་འབྲང་བ་དོན་མེད་དོ་ཞེས་བྱ་བའི་ཀླན་ཀ་ཡོངས་སུ་སྤང་བའི་ཕྱིར། འདི་ལས་རྗེས་སུ་དཔག་པར་བྱ་བ་ནི། འདིར་ཞེས་བྱ་བ་ལ་སོགས་པ་བཤད་དོ། །

[Block 76]
གྲངས་ཅན་པ་ལ་སོགས་པ་གང་དག་བསྒྲུབ་པར་བྱ་བའི་ཆོས་དང་མི་འདྲ་བའི༌[^61]ཡང་ཕྱོགས་དང་མཐུན་པ་ཉིད་དུ་རྟོགས་པར༌[^62]བྱེད་དེ། འདི་ལྟ་སྟེ། མལ་ཆ་དང་སྟན་ལ་སོགས་པའི་ཡན་ལག་བཞིན་ནོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལྟ་བུ་སྟེ། དེའི་ཕྱིར་མཐུན་པའི་ཕྱོགས་བྱེ་བྲག་ཏུ་བཤད་དོ། །

[Block 77]
རིགས་པ་ཅན་ལ་སོགས་པ་གང་དག་མེད་པའི་ངོ་བོ་མི་མཐུན་པའི་ཕྱོགས་ཡིན་པར་མི་འདོད་དོ། །

[Block 78]
མེད་པའི་ངོ་བོ་ལས་འགའ་ཡང་ལྡོག་པར་མི་རུང་བའི་ཕྱིར་རོ། །

[Block 79]
དེའི་ཕྱིར་འདུས་མ་བྱས་མེད་པར་སྨྲ་བ་བྱས་པའི་ཕྱིར་མི་རྟག་གོ་ཞེས་བྱ་བ༌[^63]སྒྲུབ་པར་བྱེད་པ་རྣམས་ཀྱི་གཏན་ཚིགས་མ་ངེས་པ་ཡིན་ནོ་ཞེས་ཟེར་བ་དེ་དག་ལ་མི་མཐུན་པའི་ཕྱོགས་བྱེ་བྲག༌[^64]བཤད་དོ། །

[Block 80 [HEADING]]
### རྟགས་ཀྱི་རབ་ཏུ་ཕྱེ་བ། ^3-2-0

[Block 81]
ཁ་ཅིག་རྗེས་སུ་དཔག་པའི་རབ་ཏུ་དབྱེ་བ་དང་། རང་གི་ངོ་བོ་གཞན་དུ་བརྗོད་དེ། འདི་ལྟ་སྟེ། རིགས་པ་ཅན་རྣམས་ན་རེ། དེ་སྔོན་དུ་འགྲོ་བའི་རྗེས་སུ་དཔག་པ་ནི་རྣམ་པ་གསུམ་སྟེ། སྔ་མ་དང་ལྡན་པ་དང་། ལྷག་མ་དང་ལྡན་པ་དང་། སྤྱིར་མཐོང་བའི་རྗེས་སུ་དཔག་པའོ་ཞེས་ཟེར་རོ། །

[Block 82]
བྱེ་བྲག༌[^65]རྣམས་ནི་རྟགས་ལས་བྱུང་བ་ནི་འདིའི་འདི་ཞེས་བྱ་བ་སྟེ། འབྲས་བུ་དང་། རྒྱུ་དང་། འབྲེལ་པ་དང་། དོན་གཅིག་དང༌[^66]ལྡན་པ་དང་། འགལ་བའོ་ཞེས་ཟེར་རོ། །

[Block 83]
སེར་སྐྱ་པ་ལ་སོགས་པ་ནི་རྗེས་སུ་དཔག་པ་རྣམ་པ་གཉིས་ཏེ། སྤྱིར་མཐོང་བ་དང་། ཁྱད་པར་དུ་མཐོང་བའོ་ཞེས་ཟེར་རོ། །

[Block 84]
དེའི་ཕྱིར་འདི་དག་གི་ལོག་པར་རྟོགས་པ་བསལ་བའི་ཕྱིར་རྟགས་ཀྱི་རབ་ཏུ་ཕྱེ་བ་བརྗོད་དོ། །

[Block 85 [HEADING]]
### མི་དམིགས་པ་བྱེ་བྲག་ཏུ་བཤད་པ། ^3-3-0

[Block 86]
རྒྱལ་དཔོག་པ་ལ་སོགས་པ་ནི་ཐམས་ཅད་མཁྱེན་པ་ལ་སོགས་པ་དམིགས་པའི་རིག༌[^67]བྱར་མ་གྱུར་པ་ཡང་རང་གི་དམིགས་པ་ལ༌[^68]ལོག་པ་ཙམ་གྱི་སྒོ་ནས་འགོག་པར་བྱེད་དེ། དེའི་ཕྱིར་མི་དམིགས་པ་བྱེ་བྲག་ཏུ་བཤད་དོ། །

[Block 87 [HEADING]]
### རང་བཞིན་གྱི་གཏན་ཚིགས་ཀྱི་ཡུལ། ^3-4-0

[Block 88]
གནས་མའི་བུའི་སྡེ་པ་ལ་སོགས་པ་ནི་མི་རྟག་པ་ལ་སོགས་པ་ཕྱིས་འབྱུང་བ་ཡང་བྱས་པ་ལ་སོགས་པའི་རང་བཞིན་ཡིན་པར་བརྗོད་དོ། །

[Block 89]
[^69]དེ་བསལ་བའི་ཕྱིར་རང་བཞིན་གྱི་གཏན་ཚིགས་ཀྱི་ཡུལ་བསྙད་དོ། །

[Block 90 [HEADING]]
### འབྲས་བུའི་གཏན་ཚིགས། ^3-5-0

[Block 91]
བརྡ་སྤྲོད་པ་ལ་སོགས་པ་མེ་མ་ཡིན་པ་བརྒྱ་བྱིན་གྱི་སྤྱི་བོ་ལ་སོགས་པ་ལས་ཀྱང་དུ་བ་འབྱུང་བ་མཐོང་བས། [^70]མེ་ལ་སོགས་པ་འགྲུབ་པར་བྱ་བ་ལ་སོགས་པ་འབྲས་བུའི་རྟགས་འཁྲུལ་པ་སྨྲ་སྟེ། དེའི་ཕྱིར་འབྲས་བུའི་གཏན་ཚིགས་བརྗོད་དོ། །

[Block 92 [HEADING]]
### དངོས་པོ་རྣམས་ཀྱི་འབྲེལ་པ། ^3-6-0

[Block 93]
གྲངས་ཅན་པ་རྣམས་ནི་དངོས་པོ་རྣམས་ཀྱི་འབྲེལ་པ་རྣམ་པ་བདུན་བརྗོད་དོ། །

[Block 94]
[^71]འདི་ལྟ་སྟེ། བདག་དང་བདག་གིར་འབྲེལ་པ་ནི་ལྷ་སྦྱིན་དང་མཆོད་སྦྱིན༌[^72]ལྟ་བུའོ། །

[Block 95]
རང་བཞིན་དང་འབྲེལ་པ་ནི་འཇིམ་པ་དང་བུམ་པ་ལྟ་བུའོ། །

[Block 96]
རྒྱུ་དང་རྒྱུ་ཅན་དུ་འབྲེལ་པ་ནི་རྫ་མཁན་དང་བུམ་པ་ལྟ་བུའོ། །

[Block 97]
རྒྱུ་དང་འབྲས་བུར་འབྲེལ་པ་ནི་ས་བོན་དང་མྱུ་གུ་ལྟ་བུའོ། །

[Block 98]
ཕ་དང་མ་ལྟ་བུར་འབྲེལ་པ་ནི་ཡལ་ག་དང་ཤིང་ལྗོན་པ་ལྟ་བུའོ། །

[Block 99]
ལྷན་ཅིག་སྤྱོད་པའི་འབྲེལ་པ་ནི་ངུར་པ་དང་ཁྱོ་ཤུག༌[^73]ལྟ་བུའོ། །

[Block 100]
དགྲ་ཟླའི་འབྲེལ་པ་ནི་བྱ་རོག་དང་འུག་པ་ལྟ་བུའོ་ཞེས་ཟེར་རོ། །

[Block 101]
རིགས་པ་ཅན་ལ་སོགས་པ་ནི་རྣམ་པ་ལྔར་བརྗོད་དེ། [^74]འབྱོར་པའི་མཚན་ཉིད་ཀྱི་འབྲེལ་པ་ནི་དུ་བ་དང་མེ་ལྟ་བུའོ། །

[Block 102]
ལྡན་པའི་མཚན་ཉིད་ཀྱི་འབྲེལ་པ་ནི་དེ་ཉིད་དང་གཟུགས་ལྟ་བུའོ། །

[Block 103]
འཕྲོད་པའི་འདུ་བའི་མཚན་ཉིད་ཀྱི་འབྲེལ་པ་ནི་དེ་ཉིད་དང་གཟུགས་དང་ལྡན་པ་ཉིད་ལྟ་བུའོ། །

[Block 104]
འདུ་བའི་ལྡན་པའི་མཚན་ཉིད་ཀྱི་འབྲེལ་པ་ནི་དཔེར་ན་དེ་ཉིད་དང་དུ་བ་ལ༌[^75]ཡོད་པའི་གཟུགས་ལ་སོགས་པ་ལྟ་བུའོ། །

[Block 105]
ལྡན་པའི་འཕྲོ་བའི༌[^76]འདུ་བའི་མཚན་ཉིད་ཀྱི་འབྲེལ་པ་ནི། དཔེར་ན་མེ་དེ་ཉིད་དང་དུ་བ་ལ་ཡོད་པའི་གཟུགས་ལ་སོགས་པ༌[^77]དང་ལྡན་པ་ཉིད་ལྟ་བུའོ། །

[Block 106]
[^78]དེ་དག་གི་གཞུང་ལུགས་ཀྱི༌[^79]འབྲེལ་པ་དེ་དག་ཁོ་ནར༌[^80]འབྲེལ་པའི་གཏན་ཚིགས་ནི་རྟོགས་པར་བྱེད་པ༌[^81]ཡིན་ཏེ། དེ་བསལ་བའི་ཕྱིར་འབྲེལ་པ་གཉིས་པ༌[^82]བརྗོད་དོ། །

[Block 107 [HEADING]]
### མི་དམིགས་པའི་རབ་ཏུ་དབྱེ་བ། ^3-7-0

[Block 108]
སྤྱོད་པ་པ་རྣམས་ནི་ད་ལྟར་ཐམས་ཅད་མཁྱེན་པ་ལ་སོགས་པ་མི་དམིགས་པའི་ཕྱིར། མ་འོངས་པའི་དུས་ན་ཡང་དེའི་སྒོ་ནས་དེ་མེད་པར་ཤེས་ཏེ། དེ་བསལ་བའི་ཕྱིར་མི་དམིགས་པ་བརྗོད་དོ། །

[Block 109]
རྒྱལ་དཔོག་པ་ལ་སོགས་པ་གང་དག་རང་གི་དམིགས་པ་ལ་སོགས་པ་རྒྱུ་མ་ཡིན་པ་དང་། ཁྱད་པར༌[^83]བྱེད་པ་མ་ཡིན་པ་དང་། འབྲས་བུ་མ་ཡིན་པའི་བཀག་པ་དང་། ཚིག་ལ་སོགས་པ་དངོས་པོ༌[^84]དང་བསྒྲུབ་པས༌[^85]ཀྱང་མི་འགལ་བ་བསྒྲུབ་པའི་སྒོ་ནས་ཐམས་ཅད་མཁྱེན་པ་ལ་སོགས་པ་འགོག་པར་སྨྲ་སྟེ། དེ་དག་གི་དེ་རིགས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བར་བསྟན་པའི་ཕྱིར་དང་། འཇིག་པ༌[^86]རྒྱུ་དང་བཅས་པར་སྨྲ་བ་འགག་པའི༌[^87]ཕྱིར། མི་དམིགས་པའི་རབ་ཏུ་དབྱེ་བ་བརྗོད་དོ། །

[Block 110]
དགག་པའི་གཏན་ཚིགས་ཀྱི་སྦྱོར་བའི་དབྱེ་བ་རྣམ་པ་མང་པོ་ཞིག་ཡོད་ཀྱང་། མེ་ལ་སོགས་པ་མེ་ཉིད་ལ་སོགས་པ་གཞན་ལས་དགག་པ་འགྲུབ་པ་མ་ཡིན་གྱི། འོན་ཀྱང་རང་བཞིན་མི་དམིགས་པ་ཁོ་ནས་ཡིན་ནོ་ཞེས་བྱ་བ༌[^88]བསྟན་པའི་ཕྱིར། ཁོངས་སུ་འདུ་བ་འཐད་པ་དང་བཅས་པ་བརྗོད་དེ། འཐད་པ་ནི་ཐམས་ཅད་ལ་ཞེས་བྱ་བ་ལ་སོགས་པས་བསྟན་ཏོ། །
--- END BLOCKS ---
