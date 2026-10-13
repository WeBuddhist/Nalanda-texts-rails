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
དེ་ནས་ཉམས་དགའ་བའི་གྲོང་ཁྱེར་ཡིན་པས་བྷ་ག་སྟེ། ཉོན་མོངས་པ་རྣམ་པར་འཇོམས་པ་དག་པའི་ཡེ་ཤེས་དང་ལྡན་པས་སོ། །བཞུགས་སོ་ཞེས་བྱ་བས་ནི་སེམས་དཔའ་སུམ་བརྩེགས་དང་ཡེ་ཤེས་ཀྱི་འཁོར་ལོ་དགུག་པ་དང་། སྐྱེ་མཆེད་བྱིན་གྱིས་བརླབ་པ་ནི་གཙོ་བོ་ལ་བསྐྱེད་ཚུལ༌[^52]དུ་བསྒོམ་མོ། །སྐུ་གསུང་ཐུགས་བྱིན་གྱིས་བརླབ་པ་དང་དབང་བསྐུར་བ་དང་། མཆོད་པ་དང་བསྟོད་པ་དང་བདུད་རྩི་མྱང་བ་དང་རྫོགས་པའི་རིམ་པ་ཉུང་ལྡན་དུ་བསྒོམ་མོ། །དག་པ་རྗེས་སུ་དྲན་པ་དང་སྔགས་བཟླས་པ་དང་གཏོར་མ་དང་ཡེ་ཤེས་པ་གཤེགས་པ་དང་དམ་ཚིག་པ་བསྡུ་བ་དང་བཅས་པ༌[^53]བཞུགས་སོ། །

[Block 72 [HEADING]]
###### **ཐུན་བཞིའི་རིམ་པ།** ^1-1-1-2-1-1-2-1-0

[Block 73]
དོ་ལ་མཉམ་གཞག་དང་རྗེས་ཐོབ་ཀྱི་རྟགས་འབྱུང་སྟེ། ཐུན་བཞིའི་རིམ་པར་ཞག༌[^54]གཉིས་དང་དེ་བཞིན་ཏེ་བརྟེན་པ་ཆོས་ནས་འཇུག་པ་དང་རྟེན་དང་པོ་ནང་ནས་འཇུག་པའོ། །

[Block 74 [HEADING]]
###### **དང་པོ་བརྟེན་པ་ཆོས་ནས་འཇུག་པ།** ^1-1-1-2-1-1-2-1-1-0

[Block 75]
དང་པོ་ནི་ཨེ་སྟེ་ཆོས་ཐམས་ཅད་སྟོང་པ་ཉིད་དང་བ༌[^55]སྟེ་ཐབས་སྣང་བ་དང་། ང་སྟེ་དབྱེར་མེད་བདག་གིས་ནི་བདག་ཉིད་དུ་ཐོས་ཤིང་གསལ་བའོ། །ཤྲུ་ཏ་སྟེ་བདེ་བ་གོང་ནས་གོང་དུ་འཕེལ་བའམ་ཡང་གསལ་རིག་གི་ཆ་མ་འགགས་པའོ། །དུས་ནི་དེ་ཉིད་སྣང་བ་དང་སྟོང་པ་དབྱེར་མེད་པའི་སྒོམ་པ་སྟེ། དེ་ཡང་ཕ་རོལ༌[^56]ཕྱིན་པ་ནི་ལུང་དང་རྒྱ་མཚོ་རིགས་པས་དཔྱད་དེ་བསྒོམས་ལ། འདིར་ནི་མན་ངག་གི་སྟོབས་ཀྱིས་ཆོས་རྣམས་ལས་ཡེ་ཤེས་སྐྱེ་བའི༌[^57]ཚུལ་དུ་བསྒོམ་མོ། །

[Block 76]
བཅོམ་ལྡན་འདས་ནི་དེས་མི་མཐུན་པ་འཇོམས་པ་དང་ཡེ་ཤེས་དང་ལྡན་པའོ། །དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད༌[^58]ནི་ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད་ལ་སོགས་པའོ། །སྐུ་གསུང་ཐུགས་ནི་རྣམ་པར་ཐར་པའི་སྒོ་གསུམ་མོ། །ཧྲྀ་ད་ཡ་ནི་སྙིང་པོ་སྟེ་བསྡུས་པའམ་དཀྱིལ་ལོ། །

[Block 77]
བཙུན་མོ་ནི་ཡུམ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་སྟེ་ཡོན་ཏན་བསྐྱེད་པའོ་ཞེས༌[^59]བཞུགས་སོ་ཞེས་པ་ནི་ཆོས་ཉིད་ཀྱིས་ཆོས་ཐམས་ཅད་ལ་ཁྱབ་པ་སྟེ། ཏིལ་ཅན་ནི་ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད་ལ་སོགས།

[Block 78 [VERSE]]
[^60]ཏིལ་ལ་ཏིལ་མར་ཇི་བཞིན་དུ། །
བུ་རམ་ཤིང་ལ་བུ་རམ་བཞིན། །

[Block 79]
ཞེས་པའོ། །

[Block 80 [HEADING]]
###### **རྟེན་དང་པོ་ནང་ནས་འཇུག་པ།** ^1-1-1-2-1-1-2-1-2-0

[Block 81]
རྟེན་དང་པོ་ནང་ནས་འཇུག་པ་ནི་ཨེ་སྟེ་ཤེས་རབ་ལྷ་མོ་བླ་ན་མེད་པའོ། །བ་ནི་དེ་བརྟེན་པའི་ཐབས་ཏེ་ཡིད་འབྲིད་པའི་དུས་སུ་ཐབས་དུ་མའོ། །ང་ནི་དབང་པོ་རང་སྣང་སྟེ་རབ་འབྲིང་ཐ་མ་གསུམ་སྟེ་གསེར་འགྱུར་གྱི་ཚུལ་དང་བྱ་རོག་ལྡིང༌[^61]ཆགས་ཀྱི་ཚུལ་དང་རྒྱ་མཚོ་ལྟ་བུའི་ཚུལ་དང་ནང་ཕྱི་རོལ་དུ་སྣང་བ་དང་།[^62] ཕྱི་ནང་དུ་སྣང་བ་དང་། རང་སོར་གནས་པ་སྐྱེའོ། །མ༌[^63]ཡཱ་ནི་སྤྱོད་ལམ་དང་བསྲེ་སྟེ།ཟ་བ་དང་འགྲོ་ཉལ་དུ་ཡང་སྐྱེའོ། །ཤྲུ་ཏ་ནི་དོན་དམ་ལྷན་སྐྱེས་སོ། །དུས་གཅིག་ནི་ཀུན་རྫོབ་ལྷན༌[^64]སྐྱེས་པ་དང་དུས་གཅིག་གོ། །ལྷན་ཅིག་སྐྱེས་པ་དེ་ཉིད་བཅོམ་ལྡན་འདས་ཏེ་སྔ་མ་བཞིན་ནོ། །

[Block 82]
གནས་གང་ན་བཞུགས་ཤེ་ན། དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་དེ་སེམས་ཅན་ཐམས་ཅད་དོ། །སྐུ་གསུང་ཐུགས་ཀྱི་ལུས་ངག་ཡིད་གསུམ་སྟེ། དེ་ཁོ་ན་རྡོ་རྗེ་བཙུན་མོ་སྟེ། ཤེས་རབ་ལྷ་མོ་བླ་ན་མེད་པ་ཕྱག་རྒྱ་ཆེན་པོ་རྟེན་དང་བརྟེན་པའི་ཚུལ་དུ་གནས་པ་ན་བཞུགས་པའོ། །དེ་ནི་ཟག་པ་མེད་པའི་བརྟེན་པ་ཡིན་གྱི་ཟག་བཅས་ཀྱི་ཚུལ་ནི་མ་ཡིན་ནོ། །དེའི་ཕྱིར་དབང་རྟེན་མི་གནས་ཏེ། ཞིབ༌[^65]ཀྱང་དབང་པོ་འཇིག་པ་མ་ཡིན་ནོ། །

[Block 83]
གཉུག་མའི་དབང་པོ་ཡོད་པར་ཅིས་ཤེས་ཤེ་ན། དེ་ལུང་དང་རིགས་པས་ཤེས་ཏེ། ལུང་ནི།

[Block 84 [VERSE]]
ལྟེ་བར་ཕྱག་རྒྱ་ཆེན་པོ་གནས། །
དང་པོ་དབྱངས་ཡིག་རང་བཞིན་ཏེ། །

[Block 85]
ཞེས་བྱ་བ་དང་།

[Block 86 [VERSE]]
ཕྱག་རྒྱ་ཆེན་པོ་དབང་བསྐུར་བ། །
དེ་ནི་འདི་ཡི་བྱིན་རླབས་ཡིན། །

[Block 87]
ཞེས་གསུངས་པ། དེའི་རྟེན་ཡང་ལུང་དེས་བསྒྲུབ་བོ། །ཕྱག་རྒྱ་ཆེན་པོ་ཉིད་དབང་རབ་དང་རབ༌[^66]ལས་བྱུང་བ་བསྒོམ་པ་རབ་དང་རབ་ཀྱིས་དང་མན་ངག་རབ་དང་རབ་ཀྱིས་བསྒྲུབ་པའོ། །དེ་ལ་དབང་རྟེན་ཡོད་པར་ཡང་ཡེ་ཤེས་ཡོད་པས་དེའི་རྟེན་ཡོད་དེ། །དཔེར་ན་མིག་གི་རྣམ་པར་ཤེས་པ་ཡོད་པས་རྐྱེན་གཞན་ཚང་ཡང་རེས་འགག་པར་འདུག་པས་གཞན་ཞིག་ཡོད་ཅེས་བྱ་བ་ལྟ་བུའོ། །

[Block 88]
དེ་ལ་གོམས་པ་ལས་རྟགས་གཞན་ཡང་གསུམ་སྟེ།

[Block 89 [VERSE]]
མི་འགྱུར་བ་ནི་ལྟ་བའི་རྟགས། །
དངོས་པོ་ཀུན་ལ་ཆགས་མེད་དྲོད། །
སྒོམ་པའི་རྟགས་སུ་ཤེས་པར་བྱ། །
འཇིག་རྟེན་ཆོས་བརྒྱད་སྤངས་པ་ནི། །

[Block 90]
སྤྱོད་པའི་རྟགས་སུ་ཤེས་པར་བྱ། །ཡང་སྔ་མའི་གསུམ་པོ་སེམས་ཟིན་པ་དང་དེ་ཁོ་ན་ལ་འཇུག་པ་དང་། དངོས་གྲུབ་འགྲུབ་པའོ། །དེ་ཁོ་ན༌[^67]ལ་ཡང་རྟགས་ལྔ་མཐོང་བའི་ལམ་དང་མཚུངས་པ་ཡིན་ནོ། །དེ་རྣམས་གསུམ་པ་རྟགས་དང་སྦྱར་ནས་སྤྱོད་པ་གསུམ་རིམ་གྱིས་བྱེད་པའམ་ཡང་ན་ཐོད་རྒལ་དུ་ཡང་བྱའོ། །གསུམ་པོས་ཀྱང་ལམ་མཇལ་བྱུང་བ༌[^68]མ་ཡིན་ཏེ། གཉིས་ཀྱིས་ནི་ཕྱག་རྒྱ་ཆེན་པོར་བརྒྱུད་དགོས་ལ། གཅིག་གིས་ནི་ཐལ་བྱུང་དུ་འགྲོའོ། །

[Block 91]
གཉིས་ནི་གང་ཟག་གི་རིམ་པས་བཤད་དེ། ཡང་།

[Block 92 [VERSE]]
ལས་ཀྱི་ཕྱག་རྒྱ་འཕྲོ༌[^69]རྒྱུ་ཅན། །
དེ་ཡང་རིང་དུ་སྤང་བྱ་སྟེ། །

[Block 93]
རང་ལུས་ཐབས་དང་ལྡན་པར་བསྒོམ་པར་བྱ་བ་དང་། དེ་ལ་སོགས་པ་དང་།

[Block 94 [VERSE]]
རང་བཞིན༌[^70]དོན་ནི་རབ་བསྒྲུབ་ཕྱིར། །
འཁོར་བར་ཐབས་གཞན་ཡོད་མ་ཡིན། །

[Block 95]
ཞེས་པ་དང་མང་དུ་བསྟན་ཏོ། །དེ་ཡང་རིམ་པར་འགྲོ་བའམ་ཡང་ན་རེ་རེ་ནས་བརྒྱུད་པ་ཡང་སྲིད་དོ། །
###### བརྟག་པ་ཕྱི་མའི་ཚུལ་གྱིས་མདོར་བསྡུས་ཏེ་བསྟན་པ། ^1-1-1-2-2-0

[Block 96]
དེ་ལ་བརྟག་པ་ཕྱི་མའི་ཚུལ་གྱིས་དོན་བསྡུ་བ་ནི་འདི་ལྟར་སྣང་བ་ཐམས་ཅད་ལྷན་སྐྱེས་བདེ་བ་ཆེན་པོ་ཡིན་ཞིང་རང་བཞིན་ཀྱང་དེ་ལྟར་སངས་རྒྱས་དང་སེམས་ཅན་ཐམས་ཅད་ཀྱང་དེ་ལྟ་བུའི་ཡང་དག་པར་སྡོམ་པ་ཡིན་ཏེ། ཅིས་ཤེ་ན། ཨེ་ཝཾ་སྟེ་གནས་སམ་དེ་རུ༌[^71]དེས་སོ། །གང་གིས་སྡོམ་ཞེ་ན། མ༌[^72]ཡཱ་སྟེ་དབང་གི་བདག་ཉིད་དང་ནི་ཤེས་རབ་དང་ཐབས་དབང་རྣམས་ཀྱིས་སོ། །ཤྲུ་ཏ་སྟེ་དགོངས་པའི་སྐད་དུ་ཐོས་པ་དེའི་དབང་གིས་དུས་ལ་སོགས་པའི་སྐབས་ངག་བརྡ་དང་ལུས་བརྡས་སྨྲའོ། །ཨེ་ཀ་སྨིན༌[^73]ས་མ་ཡ་སྟེ་དགའ་བ་རྣམས་དང་སྐད་ཅིག་གི་དུས་སུ་གཅིག་པ་སྟེ། ཤེས་པ་སྐྱེས་པའི་ཚུལ་སྤོང་བ་དང་ཐོབ་པའི་ཚུལ་དུ་འབྱུང་བའོ། །ཡང་བཟའ་བ་སྟོན་མོའི་དུས་སུ་དམ་ཚིག་གཅིག་པའོ། །

[Block 97]
དེ་དག་གིས་ཀྱང་བརྗོད་བྱའི་ཆོས་ཐམས་ཅད་དང་རྗོད་བྱེད་ཀྱི་ཆོས་ཀྱི་ཕུང་པོ་བརྒྱད་ཁྲི་བཞི་སྟོང་རྣམས་དཔལ་དགྱེས་པའི་རྡོ་རྗེར་འདུས། དུས་ཟླ་བ་དང་ལོ་ལ་སོགས་པར་བསྒོམས་པས་དང་པོ་སྤྲིན་དང་འདྲ་བ་དང་། གཉིས་པ་དུ་བ་ལྟ་བུ་སྟེ། །གསུམ་པ་སྲིན་བུ་མེ་ཁྱེར་འདྲ། །བཞི་པ་མར་མེ་ལྟ་བུ་སྟེ། །ལྔ་པ་ཐམས་ཅད་སྣང་བ་སྟེ། །སྤྲིན་མེད་ནམ་མཁའ་ལྟ་བུའོ། །གཟུང་བ་དང་བྲལ་བ་དང་། འཛིན་པ་དང་བྲལ་བ་དང་། གཉིས་ག་དང་བྲལ་བ་དང་། ཡེ་ཤེས་རང་རིག་འཆར་བ་དང་།ཆོས་ཉིད་མཐོང་བ་ལྔ་བའོ། །

[Block 98 [VERSE]]
རྗེས་ཐོབ་སྒྱུ་མའི༌[^74]རྨི་ལམ་སོགས། །
སྒྱུ་མའི་དཔེ་བརྒྱད་རིམ་པར་མཐོང་། །
དེ་ལ་སྤྱོད་པ་རྣམ་གསུམ་བྱ། །
དེ་ནས་འབྲས་བུ་གོ་འཕང་གནས། །

[Block 99]
ཞེས་བྱ་སྟེ། གང་ཟག་སྤྲོས་པ་ལ་དགའ་བས་ལམ་དེ་བསྒོམ་མོ། །

[Block 100 [HEADING]]
###### **དེ་ཉིད་རྫོགས་པའི་རིམ་པར་བསྒོམ་པ།** ^1-1-1-2-1-2-0

[Block 101]
དེ་ཉིད་རྫོགས་པའི་རིམ་པར་བསྒོམ་པ་ནི་གསུམ་སྟེ། གང་ཟག་དབང་པོ་དམན་པ་ཆགས་པ་ཤས་ཆེ་བས་གཞན་ལུས་ལ་བརྟེན་པ་དང་དབང་པོ་འབྲིང་ཆགས་པ་ཡང་འབྲིང་ནི་རང་ལུས་དང་ལྡན་པ་དང་དབང་པོ་རབ་ཆགས་པ་ཆུང་བས་དབྱེར་མེད་ཕྱག་རྒྱ་ཆེན་པོ་དང་ལྡན་པའོ། །

[Block 102 [HEADING]]
###### **གཞན་ལུས་ལ་བརྟེན་པ།** ^1-1-1-2-1-2-1-0

[Block 103]
དེ་ལ་དབང༌[^75]བསྐྱེད་པའི་རིམ་པ་ཉུང་ལྡན་ཏེ་སྔར་མཎྜལ་དང་མཆོད་པ་ཅུང་ཟད་ཙམ་ལ་བརྟེན་པའི་སྒྲུབ་པ་པོས་མོས་པའི་རྣལ་འབྱོར་རམ། བསྐྱེད༌[^76]པའི་རྣལ་འབྱོར་རམ་བྱིན༌[^77]གྱིས་ཐ་མལ་གྱི་རྣམ་པ་བསྒྱུར་ཏེ། དེ་ཡང་། བདག་མེད་རྣལ་འབྱོར་ལྡན་པའམ། ཡང་ན་ཧེ་རུ་ཀ་དཔལ་བརྩོན། །ཞེས་པ་རྟེན་ཁྱད་པར་ཅན་ནམ་ལྷན་ཅིག་བསྒོམས་ལ། ལས་ཀྱི་ཕྱག་རྒྱ་ཡང་འོག་ནས་གཡུང་མོ་རྡོ་རྗེ་རིགས་ཞེས་བྱ་བ་དང་།

[Block 104 [VERSE]]
གཞན་གྱི་རིགས་ལས་བྱུང་བའམ།
གང་གི་སྲིན་ལག་རྩ་བ་ན། །
རྡོ་རྗེ་རྩེ་དགུ་པར་གྱུར་པ། །

[Block 105]
ཞེས་བྱ་བ་ལ་སོགས་པས་བརྟགས་ཤིང་བཙལ་ལ།

[Block 106 [VERSE]]
དགེ་བ་བཅུ་ནས་བརྩམས་ནས་ནི། །
དེ་ནི༌[^78]ཆོས་ནི་རབ་ཏུ་དབྱེ། །

[Block 107]
དབང་བསྐུར་སྙིང་རྗེར་ལྡན་པ་དེ་དང་ལྷན་ཅིག་བསྒོམས་ཏེ། དེ་ཡང་ལྷར་མོས་པ་ལ་སོགས་པ་བསྒོམས་ལ། སྟན་བདེ་བ་ལ་འདུག་སྟེ་དེ་ལ་ཨེ་སྟེ་ཤེས་རབ་ཀྱི་གསང་བའི་གནས་སུ། ཝ་སྟེ་ཐབས་ཀྱི་གསང་བའི་གནས་སུ། ད་ཐིག་ལེ་ཟླ་བ་དང་ཉི་མ་འདྲེས་པའོ། །

[Block 108]
དེ་ཉིད་སྟོན་པའི་བདག་ཉིད་མ༌[^79]ཡཱ་སྟེ་ཕྱག་རྒྱའི་བདག་པོ་བསྒོམ་མོ། །ཤྲུ་ཏ་ནི་འཛག་ཅིང་རྒྱུ་བ་སྟེ་སེམས་དབབ་པ་དང་གཟུང་བ་དང་བཟློག་པ་ལ་སོགས་པའོ། །དུས་གཅིག་ནི་ལྷན་ཅིག་སྐྱེས་པའི་དགའ་བའི་དུས་སུ་གཅིག་པ་སྟེ།དགའ་བ་གསུམ་གྱི་རིམ་གྱིས་བསྐྱེད་ནས་བསྒོམ་པའོ། །བཅོམ་ལྡན་འདས་དེ་ཐིག་ལེ་དེ་སྟོན་པར་བཤད་དེ།བཅོམ་ལྡན་འདས་ལ་སོགས་པའི་ཡོན་ཏན་དང་ལྡན་པའོ། །དེ་བཞིན་གཤེགས་པ་ནས་བྷ་ག་རྣམས་ལ་ཡིས་ནི་ཨེ་ཝཾ་དེ་གནས་སུ་བསྟན་པའི་ཕྱིར་ཡོན་ཏན་གྱི་ཁྱད་པར་བརྗོད་པའོ།[^80] །དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་ཕུང་པོ་ལྔ་དང་ལུས་ངག་ཡིད་གསུམ་ཧྲྀ་ད་ཡ་བཅུད་དུ་བསྡུས་པ་བཙུན་མོ་ནི་ཕྱག་རྒྱའི་ཕུང་པོ་དང་འབྱུང་བས་བསྡུས་པས་ཧྲྀ་ད་ཡ་སྟེ་ཐིག་ལེར་གསང་བའི་གནས་སུ་བཞུགས་ཞེས་བྱ་སྟེ། ས་སྟེངས་སུ་ཟུང་ས་འོག་ཏུ་གནས་པ་སྟེ།

[Block 109]
དེ་ཡང་།

[Block 110 [VERSE]]
གཉིས་འདས་ནས་ནི་གཉིས་གནས་པ། །
རྒྱུ་ལ་འབྲས་བུས་རྒྱས་གདབ་པའམ། །
འབྲས་བུ་ལ་ཡང་རྒྱུས་རྒྱས་གདབ། །
--- END BLOCKS ---
