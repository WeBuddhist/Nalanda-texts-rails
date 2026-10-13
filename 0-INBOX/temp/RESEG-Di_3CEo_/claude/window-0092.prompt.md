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
[Block 3221]
དེ་ཐོད་པའི་ཕྱེད་ཀྱང་བར༌[^1269]ནས་སྨིན་མ་གཉིས་ཀྱི་བར་དུ་སེམས་འཛིན་པ་འདི་ནི་ཡིད་ལ་བྱེད་པ་རྫོགས་པའོ། །

[Block 3222]
ཡང་མི་སྡུག་པ་འདིའི་རང་བཞིན་ཅི་ཞིག་ཡིན། ས་ནི་དུ་བ་ཞིག་ཡིན། དམིགས་པ་ནི་ཅི་ཞིག་ཡིན། གང་དུ་ནི་སྐྱེད་པར་བྱེད་ཅེ་ན། གོ་རིམས་བཞིན་དུ།

[Block 3223 [VERSE]]
མི་སྡུག་མ་ཆགས་ས་བཅུ་དང་། །
དམིགས་པ་འདོད་སྣང་མི་སྐྱེད་དོ། །

[Block 3224]
མི་སྡུག་པ་འདིའི་རང་བཞིན་ནི་མ་ཆགས་པའོ། །

[Block 3225]
ས་ནི་བཅུ་པ་སྟེ། བསམ་གཏན་བཞི་ཡི་ཉེར་བསྡོགས་དང་། །བསམ་གཏན་ཁྱད་པར་ཅན་དང་བཅས་པ་དང་། འདོད་པའི་ཁམས་ན་ཡོད་དོ། །

[Block 3226]
དམིགས་པ་ནི་འདོད་པ་ན་སྤྱོད་པའི་ཁ་དོག་དང་དབྱིབས་སོ། །

[Block 3227]
མི་ཁོ་ན་ལས་སྐྱེ་བའི༌[^1270]གཞན་དུ་ནི༌[^1271]མ་ཡིན་ནོ། །

[Block 3228]
མི་སྡུག་པའི་རྣམ་པ་ཞེས་བྱ་བ་ནི་མིང་ཁོ་ནས་གྲུབ་པོ། །མི་སྡུག་པའི་མཚན་ཉིད་རབ་ཏུ་དབྱེ་བ་དང་བཅས་པ་བཤད་ཟིན་ཏོ། །

[Block 3229 [HEADING]]
##### དབུགས་རྔུབ་དབུགས་འབྱུང་དྲན་པ། ^6-1-4-2-0

[Block 3230 [VERSE]]
དབུགས་རྔུབ་དབུགས་འབྱུང་དྲན་པ་ནི། །
ཤེས་རབས་ལྔ་སྤྱོད་ཡུལ་རླུང་། །

[Block 3231]
འདོད་རྟེན་དབུགས་རྔུབ་པ་ནི་དབུགས་རྔུབ་པ་སྟེ་རླུང་འཇུག་པ་གང་ཡིན་པའོ། །

[Block 3232]
དབུགས་འབྱུང་བ་ནི་དབུགས་འབྱུང་བ་གང་ཡིན་པའོ། །

[Block 3233]
དེ་གཉིས་དྲན་པ་ནི་དབུགས་རྔུབ་པ་དང་འབྱུང་བ་དྲན་པ་སྟེ། དེ་ནི་ཤེས་རབ་ཀྱི་རང་བཞིན་ཡིན་ནོ། །

[Block 3234]
དྲན་པ་ཞེས་སྨོས་པ་ནི་དེའི་སྟོབས་བསྐྱེད་པས་འཇུག་པའི་ཕྱིར་རོ། །

[Block 3235]
ས་ལྔ་ནི་ཉེར་བསྡོགས་པ༌[^1272]གསུམ་དང་། བསམ་གཏན་ཁྱད་པར་ཅན་དང་། འདོད་པའི་ཁམས་ན་ཡོད་དེ། བཏང་སྙོམས་དང་། མཚུངས་པར་ལྡན་པའི་ཕྱིར་རོ། །

[Block 3236]
དེའི་དམིགས་པ་ནི་རླུང་ཡིན་ནོ། །

[Block 3237]
འདོད་པའི་ཁམས་ཀྱི་རྟེན་ཅན་ཡིན་ཏེ། ལྷ་དང་མི་དག་གི་ནང་དུ་བསྐྱེད་དོ། །

[Block 3238]
ཆོས་འདི་པ་རྣམས་ཁོ་ནའི་ཡིན་གྱི་བྱི་བའི་མ་ཡིན་ནོ། །

[Block 3239]
ལུང་མེད་པའི་ཕྱིར་དང་། བདག་ཉིད་ཀྱིས་ཆོས་ཟབ་མོ་མངོན་པར་མི་རྟོགས་པའི་ཕྱིར་རོ། །

[Block 3240]
དེ༌[^1273]ཡང་།

[Block 3241 [VERSE]]
བགྲང་ལ་སོགས་པ་རྣམ་པ་དྲུག །
དབུགས་རྔུབ་དབུགས་འབྱུང་དྲན་པ་འདི། །
བགྲང་དང་རྗེས་འགྲོ་འཇོག་པ་དང་། །
རྟོག་པ་དང་ནི་སྒྱུར་བ་དང་། །

[Block 3242]
ཡོངས་དག་རྣམ་པ་དྲུག་ཏུ་འདོད། །དེ་ལ་བགྲང་བ་ནི་དབུགས་རྔུབ་པ་དང་། དབུགས་འབྱུང་བ་གང་ལ་སེམས་གཏང་ནས་མངོན་པར་འདུ་བྱ་བ་མེད་པར་ལུས་དང་སེམས་ཙམ་གྱིས་གཅིག་དང་གཉིས་དང་གཉིས་ནས་བཅུའི་བར་དུ་བགྲང་བར་བྱེད་པའོ། །

[Block 3243]
སེམས་མངོན་པར་སྡུད་པ་དང་རྣམ་པར་གཡེང་བར་དོགས་པས་ཧ་ཅང་མང་བ་དང་། ཉུང་ངུར་ནི་མ་ཡིན་ནོ། །

[Block 3244]
བར་སྐབས་སུ་སེམས་རྣམ་པར་གཡེངས་ན་ཡང་མགོ་ནས་ཇི་སྲིད་དུ་ཏིང་ངེ་འཛིན་མ་ཐོབ་ཀྱི་བར་དུ་བགྲང་པར་བྱའོ། །

[Block 3245]
རྗེས་སུ་འགྲོ་བ་ནི་འདི་དག་ཐག་ཇི་སྲིད་ཅིག༌[^1274]ཏུ་འབྱུང་ངམ་འཇུག་ཅེས་དབུགས་འབྱུང་བའི་འགྲོས་ཀྱི་རྗེས་སུ་འགྲོ་བའོ། །

[Block 3246]
འཇིག་པ༌[^1275]ནི་ནོར་བུའི་ཐག་པ་བཞིན་དུ་སྣའི་རྩེ་མོ་ནས་རྐང་པའི་མཐེ་བོང་གི་བར་དུ་གནས་པར་ལྟ་ཞིང་། ཅི་འདི་དག་ཕན་འདོགས་པར་བྱེད་པ་ཞིག་གམ་གནོད་པར་བྱེད་པ་ཞིག་ཅེས་རྟོག་པའོ། །

[Block 3247]
ཉེ་བར་རྟོགས་པ༌[^1276]ནི་འདི་དག་རླུང་འབའ་ཞིག་མ་ཡིན་གྱི་འབྱུང་བ་ཆེན་པོ་དག་དང་འབྱུང་བ་དག༌[^1277]ལས་མངོན་པར་གྲུབ་པ་རྒྱུར་བྱས་པའི་གཟུགས་དང་། དེ་དག་ལ་བརྟེན་པའི་སེམས་དང་སེམས༌[^1278]ལས་བྱུང་བ་རྣམས་ཀྱང་ཡོད་དོ་ཞེས་ཕུང་པོ་ལྔ་ལ་ཉེ་བར་རྟོག་པར་བྱེད་པའོ། །

[Block 3248]
སྒྱུར་བ་ནི་ཕྱི་རོལ་དུ་དམིགས་པའི་བློ་བསྒྱུར་ཏེ། ཆོས་ཀྱི་མཆོག་གི་བར་དུ་གོང་ནས་གོང་དུ་དགེ་བའི་རྩ་བ་རྣམས་ལ་ཡང་དག་པར་སྤྱད་པར་བྱའོ། །

[Block 3249]
ཡོངས་སུ་དག་པ་ནི་མཐོང་བའི་ལམ་ལ་སོགས་པར་འཇུག་པའོ། །

[Block 3250]
དེ་ལ་ཡང་། དབུགས་རྔུབ་དབུགས་འབྱུང་གང་ལས་ལུས། །ལུས་གང་གི༌[^1279]ས་པ་ཡིན་པ་དེའི་ས་པ་དག་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 3251]
སེམས་ཅན་ཞེས་བྱ་མ་ཟིན་པའོ། །

[Block 3252]
དབང་པོ་དང་ཐ་དད་པའི་ཕྱིར་རོ། །

[Block 3253]
རྒྱུ་མཐུན་ལས་བྱུང་། ལུས་རྒྱས་པས་འགྲིབ་པར་འགྱུར་བའི་ཕྱིར་དང་། ཆད་ནས་ཡང་ཉིང་མཚམས་སྦྱོར་བའི་ཕྱིར་རྒྱས་པ་ལས་བྱུང་བ་དང་། རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པ་ནི་མ་ཡིན་ནོ། །

[Block 3254]
འོག་མ་ཡི། ཡིད་ཀྱིས་དེ་གཉིས་མི་རྟོགས་སོ། །

[Block 3255]
དེ་གཉིས་ནི་རང་གི་ས་པ་དང་ས་གོང་མའི་སེམས་ཀྱིས་རྟོགས་ཀྱི། འོག་མ་སྤྱོད་ལམ་པ་དང་། སྤྲུལ་པའི་སེམས་ཀྱིས་མི་རྟོགས་སོ། །

[Block 3256]
འཇུག་པའི་སྒོ་གཉིས་བཤད་ཟིན་ཏོ། །

[Block 3257 [HEADING]]
#### དྲན་པ་ཉེར་གཞག། ^6-1-5-0

[Block 3258]
དེ་གཉིས་ཀྱིས་ཏིང་ངེ་འཛིན་ཐོབ་ནས།

[Block 3259 [VERSE]]
ལྷག་མཐོང་བསྒྲུབ་པར་བྱ་བའི་ཕྱིར། །
ཞི་གནས་གྲུབ་པར་གྱུར་པ་ཡིས། །
དྲན་པ་ཉེར་གཞག་བསྒོམ་པར་བྱ། །

[Block 3260]
ཇི་ལྟར་བྱ་ཞེ་ན།
--- END BLOCKS ---
