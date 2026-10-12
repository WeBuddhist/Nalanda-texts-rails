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

[Block 216]
ཡི་གེ་གསུམ་དང་ཅི་རིགས་སུ་སྦྱར་རོ། །

[Block 217]
སྒྱུ་མ་ལྟ་བུའི་སྐུ་འབའ་ཞིག་གི་དབང་དུ་བྱས་པའི་ཡི་གེ་གསུམ་ནི་སྐུ་སྒྱུ་མ་ལྟ་བུ་དང་། གསུང་སྒྱུ་མ་ལྟ་བུ་དང་། ཐུགས་སྒྱུ་མ་ལྟ་བུའི་ཡི་གེ་གསུམ་དང་གོ་རིམས་སུ༌[^113]སྦྱར་རོ། །

[Block 218]
འོད་གསལ་འབའ་ཞིག་གི་དབང་དུ་བྱས་པའི་ཡི་གེ་གསུམ་ནི་འོད་གསལ་བའི་ཡེ་ཤེས་དང་། འོད་གསལ་བ་དང་ཆ་འདྲ་བའི་ཡེ་ཤེས༌[^114]དང་། ཀུན་རྫོབ་ཀྱི་བདེན་པ་ཡི་གེ་གསུམ་དང་གོ་རིམས་སུ༌[^115]སྦྱར་རོ། །

[Block 219]
ཟུང་དུ་འཇུག་པ་འབའ་ཞིག་པའི་དབང་དུ་བྱས་པའི་ཡི་གེ་གསུམ་ནི་རྩོལ་བ་དང་བཅས་པ་དང་རྩོལ་བ་མེད་པ་དང་ཤིན་ཏུ་རྩོལ་བ་མེད་པ་གསུམ་དང་གོ་རིམས་སུ༌[^116]སྦྱར་རོ། །

[Block 220]
ཡང་ན་སྤྲོས་པ་དང་བཅས་པ་དང་། སྤྲོས་པ་མེད་པ་དང་། ཤིན་ཏུ་སྤྲོས་པ་མེད་པའི་གོ་རིམས་སུ་སྦྱར་རོ། །

[Block 221]
[^117]དེ་བས་ན་དེ་བཞིན་གཤེགས་པའི་ཆོས་ཐམས་ཅད་ཀྱི་རྩ་བ་ནི་ཡི་གེ་གསུམ་མོ། །

[Block 222]
དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་དོན་གྱི་རྣམ་པ་ཇི་ལྟ་བ་བཞིན་དུ་སྒྲའི་རྣམ་པ་ལ་ཡང་དེ་བཞིན་ཏེ། དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་སྒྲའི་ཚོགས་ནི་ངག་གི་ལམ་ནས་འབྱུང་བ་ཡིན་ལ། དེ་ཡང་ལྷན་ཅིག་ཏུ་དབུགས་དང་གནས་པ་ཡིན་ཏེ། འབྱུང་བ་ལས་འབྱུང་བའི་སྒྲ་དང་། འཇུག་པ་ལས་འཇུག་པའི་སྒྲ་དང་། གནས་པ་ལས་གནས་པའི་སྒྲ་ནི་ཡི་གེ་གསུམ་ལས་བྱུང་བའི་སྒྲའོ། །

[Block 223]
གཞན་ལས་ཀྱང་།

[Block 224 [VERSE]]
ཨ་ནི་ཡིག་འབྲུ་ཀུན་གྱི་མཆོག །
དོན་ཆེན་ཡི་གེ་དམ་པ་ཡིན། །
ཁོང་ནས་འབྱུང་བ་སྐྱེ་བ་མེད། །
ཚིག་ཏུ་བརྗོད་པ་སྤངས་པ་སྟེ། །

[Block 225]
བརྗོད་པ་ཀུན་གྱི་རྒྱུ་ཡི་མཆོག །ཚིག་ཀུན་རབ་ཏུ་གསལ་བར་བྱེད། །ཅེས་འབྱུང་བ་དང་། །

[Block 226 [VERSE]]
གསང་བ་ཐིག་ལེའི་རྒྱུད་ལས། །
སྒྲ་རྣམས་ཡི་གེ་ལས་བྱུང་སྟེ། །
ཡི་གེ་ཡི་གེ་གསུམ་ལས་བྱུང་། །
དེ་ཕྱིར་སྒྲ་རྣམས་ཐམས་ཅད་ཀྱི། །

[Block 227]
རྒྱུ་ནི་ཡི་གེ་གསུམ་དུ་འདུས། །ཞེས་འབྱུང་བ་ལྟ་བུའོ། །

[Block 228]
དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་གསང་བ་འདུས་པ་དང་། དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་ཡི་གེ་རྣམ་པ་གསུམ་ནི་གཉིས་སུ་མེད་ཅིང་གཉིས་སུ་བྱར་མེད་སོ་སོ་མ་ཡིན་ཐ་མི་དད་དོ། །

[Block 229]
དེ་བས་ན་ཡི་གེ་ལ་འདུས་པ་ཇི་བཞིན་དུ་དེ་བཞིན་གཤེགས་པའི་གསང་བ་འདུས་པ་ལ་ཡང༌[^118]འདུས་པར་ཤེས་པར་བྱའོ། །

[Block 230]
དེ་ཉིད་བཤད་པ། ཐུབ་པ་ཆེན་པོས་ཆོས་ཕུང་པོ། །བརྒྱད་ཁྲི་བཞི་སྟོང་གསུངས་པ་ཡིན།[^119] །ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱིས་ཉོན་མོངས་པ་བརྒྱད་ཁྲི་བཞི་སྟོང་གི་གཉེན་པོར་ཆོས་ཀྱི་ཕུང་པོ་བརྒྱད་ཁྲི་བཞི་སྟོང་གསུངས་ཏེ༌[^120]དེ་དག་གི་སྣོད་འདུས་པ་འདི༌[^121]གང་ཡིན་ཞེ་ན། དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ནི་དམ་ཚིག་གི་སྒོ་ནས་སངས་རྒྱས་ལ་དམ་ཚིག་དང་སྡོམ་པ་ཐམས་ཅད་ནི་ལུས་དང་ངག་འདུལ་བར་བྱེད་པས་འདུལ་བ་ཞེས་བྱ་སྟེ།

[Block 231]
གཞན་ལས།

[Block 232 [VERSE]]
བཞི༌[^122]དང་སྤྱི་དང་ཁྱད་པར་གྱི། །
དམ་ཚིག་མཆོག་ནི་རྨད་པོ་ཆེ། །
སྡོམ་པ་གསུམ་ལ་རབ་གནས་པ། །
འདུལ་བའི་སྡོམ་པ་ཀུན་གྱི་མཆོག །

[Block 233]
ཅེས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 234]
མདོ་སྡེ་དང་མངོན་པ་ལ་ཡང་དེ་བཞིན་ཏེ། འདི་དག་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་གསང་བ་ཆེན་པོ་མདོར་བསྡུས་པ༌[^123]གསུངས་པས། དཔལ་ལྡན་འདུས་འདི་སྣོད་ཡིན་ཏེ། །ཞེས་བྱའོ། །

[Block 235]
དེ་བས་འདིས༌[^124]ནི་རྒྱུད་ཀྱི་ཆེ་བ་ཡང་བསྟན་པར་བྱ༌[^125]སྟེ་མཆོག་ཡིན༌[^126]ཞེས་སྦྱར་རོ། །

[Block 236]
གཞུང་ཉུང་བ་ལ་དོན་མང་བ་ཞེས་པ་ནི་གཞུང་གི་ཚོགས་ཕྲ་མོ་ཙམ་གྱིས་དེ་བཞིན་གཤེགས་པའི་བཀའ་མཐའ་དག་གི་དོན་རྙེད་པར་འགྱུར་བའི་ཕྱིར་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 237]
འདི་དག་གིས་ནི་རྒྱུད་ཀྱི་ཆེ་བ་ཡང་བསྟན་པར་རིག་པར་བྱའོ། །

[Block 238]
དེ་ནས་རྒྱུ་རྙེད་པར་དཀའ་བ་བསྟན་པའི་ཕྱིར། འདུས་པའི་རྒྱུད་ནི་རྙེད༌[^127]དཀའ་ཞིང་། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། འདི་ནི་སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་ཀྱང་ཐེ་ཚོམ་སྐྱེད་པར་བྱེད་པ་ཡིན་ན་གཞན་ལྟ་ཅི་སྨོས་ཞེས་གཞུང་འདི་ཉིད་ལས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 239]
སངས་རྒྱས་ཐེ་ཚོམ་སྐྱེ་བ་ཅིའི་ཕྱིར་ཞེ་ན། སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་ལ་ནམ་ཡང་ཐེ་ཚོམ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 240]
དེ་བས་ན་འདི་དག་གི་དོན་ནི་ཚོགས་དང་བླ་མའི༌[^128]གང་ཟག་གསང་བ་འདུས་པའི་དཀྱིལ་འཁོར་དུ་ཉན་པའི་སྐལ་བ་དང་ལྡན་པ་རྣམས་ཀྱང་ཐེ་ཚོམ༌[^129]སྐྱེ་བར༌[^130]བྱེད་པ་ཡིན་ན། ཉན་ཐོས་དང་བྱང་ཆུབ་སེམས་དཔའི་རིགས་ལ་སོགས་པ་གཞན་ལྟ་ཅི་སྨོས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 241]
དེ་བཞིན་གཤེགས་པའི་གསང་བ་འདུས་པའི་དོན་རྙེད་པར་དཀའ་བ་ཡང་ཅིའི་ཕྱིར་ཞེ་ན། རྒྱན་བདུན་རྟོགས་པར་དཀའ་བས་ན། །ཞེས་པ་སྨོས་ཏེ་རྒྱན་བདུན་རྟོགས་པར་དཀའ་བས་དེའི་ཕྱིར་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 242]
དེས་ཅིར་འགྱུར་ཞེ་ན། ཐམས་ཅད་དུ་ནི་རྣམ་པར་འཁོར། །ཞེས་སྦྱར་རོ།[^131] །འདི་ཉིད་ཀྱང་གཞུང་འདི་ཉིད་ལས་བཞུགས་པའི་ཚོགས༌[^132]ནས་བརྩམས་ཏེ། མཐའ་རྣམ་པ་དྲུག་དང་རྣམ་པ་བཞིར་བཤད་པ་འདིས་གསང་བ་འདུས་པའི་དོན་ཕྱག་རྒྱས་བཏབ་པ་ཡིན་ལ་ཞེས་སྨོས་པའི་ཕྱིར་དང་།

[Block 243]
བཅོམ་ལྡན་འདས་ཀྱིས་དགོངས་པ་ལུང་བསྟན་པའི་རྒྱུད་ལས།

[Block 244 [VERSE]]
གསང་བའི་བདག་པོ་དོན་རྒྱས་པའི། །
ཚུལ་ཆེན་འདི་ནི་རྙེད་གྱུར་ནས། །
ཇི་བཞིན་དོན་ནི་རྙེད་བཟུང་བ། །
དེས་ན་ལམ་ངན་དག་ཏུ་ལྟུང་། །

[Block 245]
ཞེས་བྱ་བ་ལ་སོགས་པ་བཤད་པའི་ཕྱིར་རོ། །

[Block 246]
དེ་ནས་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་གསང་བ་འདུས་པ་ཤེས་པར་བྱ་བ་ཡིན་པར་བསྟན་པའི་ཕྱིར།

[Block 247 [VERSE]]
དེ་བས་བླ་མའི་བཀའ་དྲིན་གྱིས། །
འབད་དེ་རྣམ་པར་ཤེས་ནས་ནི། །

[Block 248]
ཞེས་པ་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་གསང་བ་འདུས་པ་ནི་དབང་དང་དམ་ཚིག་དང་མི་ལྡན་པ་ལ་གསང་བ་སྟོན་པར་བྱེད་པ་དང་། སློབ་དཔོན་སྨོད་པར་བྱེད་པ་དང་། སློབ་དཔོན་གྱི་གདམས་ངག་རྗེས་སུ་མི་འཛིན་པ་དང་ཉན་ཐོས་ཀྱི་རིགས་ཅན་དང་། རང་སངས་རྒྱས་ཀྱི་རིགས་ཅན་དང་། བྱང་ཆུབ་སེམས་དཔའི་རིགས་ཅན་དང་། རིགས་མ་ངེས་པ་ལ་སོགས་པ་རྣམས་ཀྱིས༌[^133]ནམ་ཡང་རྙེད་པར་མི་འགྱུར་ཞིང་། བླ་མའི་གདམས་ངག་རྗེས་སུ་འཛིན་པར་བྱེད་པ་དང་། དད་པ་དང་དམ་ཚིག་ལ་སོགས་པ་དང་ལྡན་པ་དང་། ཐེག་པ་ཆེན་པོའི་རིགས་ཅན་གྱི་གང་ཟག་རྒྱུའི་རྒྱུད་ཀྱང་ཤེས་པར་བྱའོ། །

[Block 249]
དེ་ནས་གཞན་ལ་ཆོས་བསྟན་པར་འདོད་ནས་བཤད་པའི་དབྱེ་བར་བསྟན་པའི་ཕྱིར། སེམས་ཅན་རྗེས་སུ༌[^134]གཟུང་འདོད་པས། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། བླ་མའི་གདམས་ངག་ལ་བརྟེན་ནས། དེ་བཞིན་གཤེགས་པའི་གསང་བ་འདུས་པའི་དོན་ཇི་ལྟ་བུ་རྣམ་པར་ཤེས་པའི་གང་ཟག་དེས་མ་འོངས་པའི་སེམས་ཅན་བློ་དམན་པ་རྗེས་སུ་གཟུང་བར་བྱ་བའི་ཕྱིར་བཤད་པའི་རྒྱུད་ཀྱི་རྗེས་སུ་འབྲངས༌[^135]ཏེ་བཤད་པའི་ཕྱིར། དེའི་རྣམ་པར་དབྱེ་བ་ཞེས་བྱ་བ་སྨོས་པའི་ཕྱིར་རོ། །

[Block 250]
འདིས་རྒྱན་བདུན་བཤད་པར་དམ་བཅས་པ་ཡང་ཡིན་ནོ། །
--- END BLOCKS ---
