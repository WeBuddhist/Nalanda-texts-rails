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
[Block 981]
མཐོང་བསྒོམ་མི་སློབ་ལམ་ལ་དགུ། །གསུམ་ཡིན། ཡིད་དང་། བདེ་བ་དང་། ཡིད་བདེ་བ་དང་། བཏང་སྙོམས་རྣམས་དང་། དད་པ་ལ་སོགས་པ་ལྔ་དང་དབང་པོ་དགུ་པོ་དེ་དག་ནི་ལམ་གསུམ་དག་ཏུ་དབང་པོ་གསུམ་ཞེས་བྱ་སྟེ། མཐོང་བའི་ལམ་ལ་ནི་མི་ཤེས་པ་ཀུན་ཤེས་པར་བྱེད་པའི་དབང་པོ་ཞེས་བྱའོ། །

[Block 982]
བསྒོམ་པའི་ལམ་ལ་ནི་ཀུན་ཤེས་པའི་དབང་པོ་ཞེས་བྱའོ། །

[Block 983]
མི་སློབ་པའི་ལམ་ལ་ནི་ཀུན་ཤེས་པ་དང་ལྡན་པའི་དབང་པོ་ཞེས་བྱའོ། །ཅིའི་ཕྱིར་ཞེ་ན། མཐོང་བའི་ལམ་ལ་ནི་མི་ཤེས་པ་ཀུན་ཤེས་པར་བྱ་བར་ཞུགས་པ་ཡིན་ནོ། །

[Block 984]
བསྒོམ་པའི་ལམ་ལ་ནི་སྔོན་མ་མཐོང་བ་ཀུན་ཤེས་པར་བྱ་བ་ནི་མེད་ཀྱི། ཕྲ་རྒྱས་ལྷག་མ་སྤང་བར་བྱ་བའི་ཕྱིར་དེ་ཉིད་ཀུན་ཤེས་པར་བྱེད་དོ། །

[Block 985]
མི་སློབ་པའི་ལམ་ལ་ནི་ཀུན་ཤེས་སོ་སྙམ་དུ་རྟོགས་པ་ནི་ཀུན་ཤེས་པ་སྟེ། དེ་འདི་ལ་ཡོད་པས་སམ། འདི་ཀུན་ཤེས་པ་སྲུང་བའི་ངང་ཚུལ་ཅན་ཡིན་པས་ན་ཀུན་ཤེས་པ་དང་ལྡན་པའོ། །

[Block 986]
ཟད་པ་དང་མི་སྐྱེ་བའི་ཡེ་ཤེས་ཐོབ་པའི་ཕྱིར་བདག་གིས་སྡུག་བསྔལ་ཡོངས་སུ་ཤེས་ཏེ་ཡང་ཡོངས་སུ་ཤེས་པར་བྱར་མེད་དོ་སྙམ་པ་སྟེ། དེ་ལྟ་བུའི་དབང་པོ་ནི་ཀུན་ཤེས་པ་དང་ལྡན་པའི་དབང་པོ་ཡིན་ནོ། །

[Block 987 [HEADING]]
#### རྣམ་པའི་བྱེ་བྲག། ^2-1-4-0

[Block 988 [HEADING]]
##### ཟག་པ་དང་བཅས་པ་དང་ཟག་པ་མེད་པ། ^2-1-4-1-0

[Block 989]
རང་གི་ངོ་བོ་བསྟན་ནས་ཟག་པ་དང་བཅས་པ་རྣམས་ནི་དུ། ཟག་པ་མེད་པ་རྣམས་ནི་དུ་ཞེས་བྱ་བ་དེ་ལྟ་བུ་ལ་སོགས་པ་རྣམ་པའི་བྱེ་བྲག་བརྗོད་པར་བྱ་སྟེ། དེ་ལ་རེ་ཞིག་ཀུན་ཤེས་པར་བྱེད་པའི་དབང་པོ་ལ་སོགས་པ་བཤད་མ་ཐག་པ་གང་དག་ཡིན་པ་དེ། གསུམ་ནི་དྲི་མ་མེད་པ། [^427]ཟག་པ་མེད་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་སྟེ། དྲི་མ་རྣམས་ནི་ཟག་པའི་རྣམ་གྲངས་ཡིན་པའི་ཕྱིར་རོ། །

[Block 990]
གཟུགས་ཅན་སྲོག་དང་སྡུག་བསྔལ་དག །ཟག་དང་བཅས་པ། དབང་པོ་གཟུགས་ཅན་བདུན་དང་། སྲོག་གི་དབང་པོ་དང་། སྡུག་བསྔལ་དང་། ཡིད་མི་བདེ་བའི་དབང་པོ་དག་ནི་གཅིག་ཏུ་ཟག་པ་དང་བཅས་པ་ཡིན་ནོ། །

[Block 991]
གཟུགས་ཅན་བདུན་ནི་མིག་དང་། རྣ་བ་དང་། སྣ་དང་། ལྕེ་དང་། ལུས་དང་། མོ་དང་ཕོའི་དབང་པོ་རྣམས་ཏེ། གཟུགས་ཀྱི་ཕུང་པོས་བསྡུས་པའི་ཕྱིར་རོ། །

[Block 992]
དགུ་རྣམ་གཉིས། ཡིད་དང་བདེ་བ་དང་། ཡིད་བདེ་བ་དང་བཏང་སྙོམས་དག་དང་། དད་པ་ལ་སོགས་པ་ལྔ་དང་། དབང་པོ་དགུ་པོ་དེ་དག་ནི་ཟག་པ་དང་བཅས་པ་ཡང་ཡིན་ལ་ཟག་པ་མེད་པ་ཡང་ཡིན་ནོ། །

[Block 993]
ཁ་ཅིག་ན་རེ་དད་པ་ལ་སོགས༌[^428]པ་རྣམས་ནི་ཟག་པ་མེད་པ་ཁོ་ན་ཡིན་ཏེ། བཅོམ་ལྡན་འདས་ཀྱིས་གང་ལ་དབང་པོ་ལྔ་པོ་འདི་དག་ཐམས་ཅད་དུ་ཐམས་ཅད་མེད་པ་དེ་ནི་ཕྱི་རོལ་སོ་སོའི་སྐྱེ་བོའི་ཕྱོགས་ལ་གནས་པར་ང་སྨྲའོ་ཞེས་གསུངས་སོ་ཞེས་ཟེར་རོ། །

[Block 994]
དེ་ནི་ཁུངས་སུ་མི་རུང་སྟེ། ཟག་པ་མེད་པ་རྣམས་ཀྱི་དབང་དུ་མཛད་ནས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 995]
འདི་ལྟར་འཕགས་པའི་གང་ཟག་རྣམ་པར་གཞག་པ་མཛད་ནས་གང་ལ་དབང་པོ་འདི་དག་ཅེས་གསུངས་པའི༌[^429]ཕྱིར་རོ། །

[Block 996]
ཡང་ན་སོ་སོའི་སྐྱེ་བོ་ནི་རྣམ་པ་གཉིས་ཏེ། ནང་པ་དང་། ཕྱི་རོལ་པའོ། །

[Block 997]
ནང་པ་ནི་དགེ་བའི་རྩ་བ་ཀུན་ཏུ་མ་ཆད་པའོ། །

[Block 998]
ཕྱི་རོལ་པ་ནི་དགེ་བའི་རྩ་བ་ཀུན་ཏུ་ཆད་པ་སྟེ། དེའི་དབང་དུ་མཛད་ནས་ཕྱི་རོལ་སོ་སོའི་སྐྱེ་བོའི་ཕྱོགས་ལ་གནས་པར་ང་སྨྲའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 999]
མདོ་ལས་ཀྱང་སེམས་ཅན་འཇིག་རྟེན་དུ་སྐྱེས་ཤིང་འཇིག་རྟེན་དུ་རྒས་པ་རྣམས་ལ་དབང་པོ་རྣོན་པོ་དག་ཀྱང་མཆིས། དབང་པོ་འབྲིང་པོ་དག་ཀྱང་མཆིས། དབང་པོ་རྟུལ་པོ་དག་ཀྱང་མཆིས་སོ་ཞེས་ཆོས་ཀྱི་འཁོར་ལོ་མ་བསྐོར་བ་ཁོ་ནའི་ཚེ་གསུངས་ཏེ། དེའི་ཕྱིར་དད་པ༌[^430]ལ་སོགས་པ་ཟག་པ་དང་བཅས་པ་དག་ཀྱང་ཡོད་པ་ཉིད་དོ། །

[Block 1000]
ཡང་ངས་ཇི་སྲིད་དུ་དབང་པོ་ལྔ་པོ་འདི་དག་གི་ཀུན་འབྱུང་བ་དང་། མི་སྣང་བ་དང་། རོ་མྱོང༌[^431]བ་དང་། ཉེས་དམིགས་དང་། ངེས་པར་འབྱུང་བ་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་མ་ཤེས་པ་དེ་སྲིད་དུ་ང་འཇིག་རྟེན་ལྷ་དང་བཅས་པ་འདི་ལས་ཞེས་རྒྱས་པར་གསུངས་ཏེ། ཟག་པ་མེད་པ་རྣམས་ལ་ནི་ཡོངས་སུ་བརྟག་པའི་རྣམ་པ་འདི་མེད་དོ། །

[Block 1001 [HEADING]]
##### རྣམ་པར་སྨིན་པ། ^2-1-4-2-0

[Block 1002 [HEADING]]
###### ཚེའི་འདུ་བྱེད་འཇོག་པ་དང་གཏོང་བ། ^2-1-4-2-1-0

[Block 1003]
དབང་པོ་དུ་ནི་རྣམ་པར་སྨིན་པ་དག་ཡིན། དུ་ནི་རྣམ་པར་སྨིན་པ་མ་ཡིན་པ་དག་ཡིན་ཞེ་ན། རེ་ཞིག་གཅིག་ཏུ་སྲོག་ནི་རྣམ་སྨིན། འོ་ན་དགེ་སློང་དག་དགྲ་བཅོམ་པའི་ཚེའི་འདུ་བྱེད་དག་འཇོག་པར་བྱེད་པའི་སྲོག་གི་དབང་པོ་གང་ཡིན་པ་དེ་གང་གི་རྣམ་པར་སྨིན་པ་ཞེ་ན།

[Block 1004]
བསྟན་བཅོས་ལས།

[Block 1005]
ཚེའི་འདུ་བྱེད་དག་ཇི་ལྟར༌[^432]འཇོག་པར་བྱེད་ཅེ་ན། དགེ་སློང་དགྲ་བཅོམ་པ་རྫུ་འཕྲུལ་དང་ལྡན་པ་སེམས་ལ་དབང་ཐོབ་པས་དགེ་འདུན་ནམ་གང་ཟག་ལ་ལྷུང་བཟེད་དམ་ཆོས་གོས་སམ། དགེ་སྦྱོང་གི་འཚོ་བའི་ཡོ་བྱད་གང་ཡང་རུང་བ་ཕུལ་ནས། དེ་བསམས་ཏེ་རབ་ཀྱི་མཐའ་པའི་བསམ་གཏན་བཞི་པ་ལ་སྙོམས་པར་འཇུག་ཅིང་དེ་དེ་ལས་ལངས་ནས། བདག་གི་ལོངས་སྤྱོད་ཀྱི་རྣམ་པར་སྨིན་པ་གང་ཡིན་པ་དེ། ཚེའི༌[^433]རྣམ་པར་སྨིན་པར་གྱུར་ཅིག་སྙམ་དུ་སེམས་སྐྱེད་པར་བྱེད་ཅིང་ཚིག་ཏུ་ཡང་སྨྲ་བར་བྱེད་དོ། །

[Block 1006]
དེའི་ལོངས་སྤྱོད་ཀྱི་རྣམ་པར་སྨིན་པ་གང་ཡིན་པ་དེའི་ཚེའི་རྣམ་པར་སྨིན་པར་འགྱུར་རོ་ཞེས་འབྱུང་ངོ་། །གང་དག་རྣམ་པར་སྨིན་པའི་ལྷག་མ་རྣམ་པར་སྨིན་པར་བྱེད་དོ་སྙམ་དུ་སེམས་པ་དེ་དག་ན་རེ་ནི་དེས་ཚེ་རབས་སྔ་མ་ལ་ལས་བྱས་པའི་རྣམ་པར་སྨིན་པ་བསྒོམས་པའི་སྟོབས་ཀྱིས་དྲངས་ནས་སོ་སོར་མྱོང་བར་བྱེད་དོ་ཞེས་ཟེར་རོ། །

[Block 1007]
དེའི་ཚེའི་འདུ་བྱེད་དག་ཇི་ལྟར་གཏོང་ཞེ་ན། དེ་བཞིན་དུ་སྦྱིན་པ་བྱིན་ནས་བསམས་ཏེ་རབ་ཀྱི་མཐའ་པའི་བསམ་གཏན་བཞི་པ་ལ་སྙོམས་པར་འཇུག་ཅིང་དེ་དེ་ལས་ལངས་ནས་བདག་གི་ཚེའི་རྣམ་པར་སྨིན་པ་གང་ཡིན་པ་དེ་ལོངས་སྤྱོད་ཀྱི་རྣམ་པར་སྨིན་པར་གྱུར་ཅིག་སྙམ་དུ་སེམས་སྐྱེད༌[^434]པར་བྱེད་ཅིང་ཚིག་ཏུ་ཡང་སྨྲ་བར་བྱེད་དེ། དེའི་དེ་ལྟ་བུར་འགྱུར་རོ། །

[Block 1008]
བཙུན་པ་དབྱངས་སྒྲོགས་ན་རེ་ནི་དེས་ལུས་དེ་ཉིད་ལ་གཟུགས་ན་སྤྱོད་པའི་འབྱུང་བ་ཆེན་པོ་ཚེ་དང་མཐུན་པ་འམ་འགལ་བ་དག་བསམ་གཏན་གྱི་སྟོབས་ཀྱིས་མངོན་དུ་བྱེད་དོ། །

[Block 1009]
དེ་ལྟར་ཚེའི་འདུ་བྱེད་དག་འཇོག་པར་བྱེད་ཅིང་། དེ་ལྟར་གཏོང་བར་བྱེད་དོ་ཞེས་ཟེར་རོ། །

[Block 1010]
འདི་ལྟ་བུ་ཡིན་ཏེ། དེ་དག་གི་དེ་ལྟ་བུ་དེ་ནི། ཏིང་ངེ་འཛིན་གྱི་མཐུ་ཁོ་ན་སྟེ། དེས་སྔོན་གྱི་ལས་ལས་སྐྱེས་པ༌[^435]དབང་པོའི་འབྱུང་བ་ཆེན་པོ་རྣམས་ཀྱི་གནས་པའི་དུས་འཕེན་པ་ནི་ཟློག༌[^436]པར་བྱེད་ལ། སྔོན་མེད་པ་ཏིང་ངེ་འཛིན་ལས་སྐྱེས་པའི་འཕེན་པ༌[^437]ནི་འཕེན་པར་བྱེད་དེ། དེ་ལྟ་བས་ན་སྲོག་གི་དབང་པོ་དེ་ནི་རྣམ་པར་སྨིན་པ་མ་ཡིན་ལ། དེ་ལས་གཞན་པ་ནི་རྣམ་པར་སྨིན་པ་ཡིན་ནོ། །

[Block 1011]
དྲི་བ་ལས་དྲི་བ་གཞན་འབྱུང་སྟེ། ཅིའི་ཕྱིར་ཚེའི་འདུ་བྱེད་དག་བྱིན་གྱིས་རློབ་པར་བྱེད་ཅེ་ན། གཞན་ལ་ཕན་པའི་དོན་ཏམ། བསྟན་པ་གནས་པར་བྱ་བའི་དོན་དུ་སྟེ། དེ་དག་ནི་བདག་ཉིད་ཚེ་ཟད་པར་མཐོང་ཞིང་དེ་ལས་གཞན་ནུས་པ་ཡང་མ་མཐོང་བ་ཡིན་ནོ། །

[Block 1012]
འོ་ན་ཅིའི་ཕྱིར་གཏོང་བར་བྱེད་ཅེ་ན། གསོན་ན་གཞན་ལ་ཕན་པ་ཆུང་བ་དང་། ལུས་ནད་ལ་སོགས་པ་ལྟ་བུར་མཐོང་བ་ཡིན་ཏེ། ཇི་སྐད་དུ།

[Block 1013 [VERSE]]
[^438]ཚངས་སྤྱོད་འདི་ལ་ལེགས་སྤྱད་ཅིང་། །
ལམ་ལའང་ཤིན་ཏུ་བསྒོམས་ན་ནི། །
ཚེ་ཟད་པ་ལ་དགའ་འགྱུར་ཏེ། །
དཔེར་ན་ནད་དང་བྲལ་བ་བཞིན། །

[Block 1014]
ཞེས་གསུངས་པ་ལྟ་བུའོ། །

[Block 1015]
འོ་ན་གང་དུ་འམ། གང་ཞིག༌[^439]གི་ཚེའི་འདུ་བྱེད་དག་འཇོག་པ་འམ། གཏོང་བ་དེ་རིག་པར་བྱ་ཞེ་ན། མིའི་ནང་ཁོ་ན་དག་ཏུ་སྟེ་གླིང་གསུམ་པོ་དག་ཏུའོ། །

[Block 1016]
གང་ཞིག་གི་ཞེ་ན། དགྲ་བཅོམ་པ་ཕོ་མོ་རབ་ཀྱི་མཐའི་བསམ་གཏན་ཐོབ་པ་དུས་དང་མི་སྦྱོར་བར་རྣམ་པར་གྲོལ་བ༌[^440]སྟེ། དེ་ནི་ཏིང་ངེ་འཛིན་ལ་ཡང་དབང་ཞིང་ཉོན་མོངས་པ་དག་གིས་ཀྱང་རྒྱུ༌[^441]ཉེ་བར་མ་བསྟན་པ་ཡིན་ནོ། །

[Block 1017]
མདོ་ལས་བཅོམ་ལྡན་འདས་ཀྱིས། སྲོག་གི་འདུ་བྱེད་དག་བྱིན་གྱིས་བརླབས་ནས་ཚེའི་འདུ་བྱེད་དག་བཏང་ངོ་ཞེས་གསུངས་པ་དེ་དག་ལ་ཁྱད་པར་ཅི་ཞིག་ཡོད་ཅེ་ན། ཁ་ཅིག་ན་རེ་ཅུང་ཟད་ཀྱང་མེད་དེ། འདི་ལྟར་སྲོག་གི་དབང་པོ་གང་ཞེ་ན། ཁམས་གསུམ་པའི་ཚེ་ཡིན་ནོ་ཞེས་གསུངས་སོ་ཞེས་ཟེར་རོ། །

[Block 1018]
ཁ་ཅིག་ན་རེ་ནི་སྔོན་གྱི་ལས་ཀྱི་འབྲས་བུ་ནི་ཚེའི་འདུ་བྱེད་དག་ཡིན་ལ། ད་ལྟར་བྱུང་བའི་ལས་ཀྱི་འབྲས་བུ་ནི་སྲོག་གི་འདུ་བྱེད་དག་ཡིན་ནོ་ཞེས་ཟེར་ཏེ། གང་དག་གིས་རིས་མཐུན་པར་གནས་པར་འགྱུར་བ་དེ་དག༌[^442]ནི་ཚེའི་འདུ་བྱེད་དག་ཡིན་ལ། གང་དག་གིས་དུས་གཞན་གྱི་བར་དུ་འཚོ་བ་དེ་དག་ནི་སྲོག་གི་འདུ་བྱེད་དག་ཡིན་ནོ། །

[Block 1019]
མང་པོའི་ཚིག་ནི་ཚེ་དང་སྲོག་གི་འདུ་བྱེད་ཀྱི་སྐད་ཅིག་མ་རྣམ་པ༌[^443]མང་པོ་རྣམས་ལ་གཏོང་ཞིང་བྱིན་གྱིས་རློབ་པའི་ཕྱིར་ཏེ། སྐད་ཅིག་མ་གཅིག་ལ་ནི་གཏོང་བ་འམ་བྱིན་གྱིས་རློབ་པ་མེད་དོ། །

[Block 1020]
ཁ་ཅིག་ན་རེ་དུས་གཞན་གྱི་བར་དུ་འདུག་པ༌[^444]ཚེའི་རྫས་གཅིག་པུ་ནི་མེད་དོ་ཞེས་བསྟན་པའི་ཕྱིར་རོ་ཞེས་ཟེར་རོ། །
--- END BLOCKS ---
