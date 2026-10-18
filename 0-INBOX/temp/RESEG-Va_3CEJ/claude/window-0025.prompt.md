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
[Block 876 [HEADING]]
#### རྟག་པ་དང་མི་རྟག་པ། ^1-3-21-0

[Block 877]
རྟག་པ་རྣམས་ནི་དུ། མི་རྟག་པ་རྣམས་ནི་དུ་ཞེ་ན། ཁམས་གཅིག་རིལ་པོར་རྟག་པ་ནི་མེད་མོད་ཀྱི། འོན་ཀྱང་། འདུས་མ་བྱས་ཆོས་རྟག་པའོ། །

[Block 878]
དེས་ན་ཆོས་ཀྱི་ཁམས་ཀྱི་ཕྱོགས་གཅིག་རྟག་ལ། ལྷག་མ༌[^392]རྣམས་ནི་མི་རྟག་པ་ཡིན་ནོ། །

[Block 879 [HEADING]]
#### དབང་པོ་དང་དབང་པོ་མ་ཡིན་པ། ^1-3-22-0

[Block 880]
དབང་པོ་རྣམས་ནི་དུ། དབང་པོ་མ་ཡིན་པ་རྣམས་ནི་དུ་ཞེ་ན།

[Block 881 [VERSE]]
ཆོས་ཀྱི་ཕྱེད་དང་གང་དག་ནི། །
བཅུ་གཉིས་ནང་གིར་བཤད་དབང་པོ། །

[Block 882]
མདོ་ལས།

[Block 883]
མིག་གི་དབང་པོ་དང་། རྣ་བའི་དབང་པོ་དང་། སྣའི་དབང་པོ་དང་། ལྕེའི་དབང་པོ་དང་། ལུས་ཀྱི་དབང་པོ་དང་། ཡིད་ཀྱི་དབང་པོ་དང་། མོའི་དབང་པོ་དང་། ཕོའི་དབང་པོ་དང་། སྲོག་གི་དབང་པོ་དང་། བདེ་བའི་དབང་པོ་དང་། སྡུག་བསྔལ་གྱི་དབང་པོ་དང་། ཡིད་བདེ་བའི་དབང་པོ་དང་། ཡིད་མི་བདེ་བའི་དབང་པོ་དང་། བཏང་སྙོམས་ཀྱི་དབང་པོ་དང་། དད་པའི་དབང་པོ་དང་། བརྩོན་འགྲུས་ཀྱི་དབང་པོ་དང་། དྲན་པའི་དབང་པོ་དང་། ཏིང་ངེ་འཛིན་གྱི་དབང་པོ་དང་། ཤེས་རབ་ཀྱི་དབང་པོ་དང་། མི་ཤེས་པ་ཀུན་ཤེས་པར་བྱེད་པའི་དབང་པོ་དང་། ཀུན་ཤེས་པའི་དབང་པོ་དང་། ཀུན་ཤེས་པ་དང་ལྡན་པའི་དབང་པོ་དང་། དབང་པོ་ཉི་ཤུ་རྩ་གཉིས་གསུངས་པ་ལ་ཆོས་མངོན་པ་པ་རྣམས་ནི་སྐྱེ་མཆེད་དྲུག་གི་གོ་རིམས༌[^393]རྣམ་པར་གཞག་པ་ལ་མ་གུས་པས་ཡིད་ཀྱི་དབང་པོ་སྲོག་གི་དབང་པོའི་མཇུག༌[^394]ཐོགས་སུ་འདོན་ཏེ། དམིགས་པ་དང་བཅས་པའི་ཕྱིར་རོ། །

[Block 884]
དེ་ལ་ཆོས་ཀྱི་ཕྱེད་ནི་སྲོག་གི་དབང་པོ་ལ་སོགས་པ་དབང་པོ་བཅུ་གཅིག་དང་། གསུམ་པོ་དག་གི་ཆ་སྟེ། ཆོས་ཀྱི་ཁམས་ཀྱི་ཕྱོགས་ཡིན་པའི་ཕྱིར་རོ། །

[Block 885]
ནང་གི་བཅུ་གཉིས་ནི་མིག་ལ་སོགས་པ་རང་གི་མིང་གིས་སྨོས་པ་ལྔ་དང་། ཡིད་ཀྱི་དབང་པོ་ནི་སེམས་ཀྱི་ཁམས་བདུན་ནོ། །

[Block 886]
ཕོ་དང་མོའི་དབང་པོ་དག་ནི་ལུས་ཀྱི་ཁམས་ཀྱི་ཕྱོགས་ཡིན་ནོ་ཞེས་འོག་ནས་འཆད་དོ། །

[Block 887]
ལྷག་མ་ཁམས་ལྔ་པོ་དེ༌[^395]དག་དང་ཆོས་ཀྱི་ཁམས་ཀྱི་ཕྱོགས་ནི་དབང་པོ་མ་ཡིན་པ་ཞེས་བྱ་བ་འགྲུབ་བོ། །

[Block 888]
[^396]ཆོས་མངོན་པའི་མཛོད་ཀྱི་རྣམ་པར་བཤད་པ་ལས་ཁམས་བསྟན་པ་ཞེས་བྱ་བ་སྟེ་མཛོད་ཀྱི་གནས་དང་པོའོ།། །།

[Block 889 [HEADING]]
## དབང་པོ་བསྟན་པ། ^2-0

[Block 890 [HEADING]]
### དབང་པོ་རྣམས་ཀྱི་རབ་ཏུ་དབྱེ་བ། ^2-1-0

[Block 891 [HEADING]]
#### དབང་པོའི་དོན། ^2-1-1-0

[Block 892]
དབང་པོ་རྣམས་བཤད་པ་ལ་དབང་པོའི་དོན་ཅི་ཞེ་ན། དབང་ནི་དབང་ཕྱུག་དམ་པའོ། །

[Block 893]
དེ་དབང་བྱེད་པས་ན༌[^397]དབང་པོ་རྣམས་ཏེ། དེའི་ཕྱིར་དབང་བྱེད་པའི་དོན་ནི་དབང་པོའི་དོན་ཏོ། །

[Block 894]
འདི་དག་ལས་གང་ཞིག་གང་ལ་དབང་བྱེད་ཅེ་ན། ལྔ་པོ་རྣམས་ནི་དོན་བཞི་ལ་དབང་བྱེད། རེ་ཞིག་མིག་དང་། རྣ་བ་དག་རེ་རེ་ཞིང་དོན་བཞི་ལ༌[^398]དབང་བྱེད་པ་ནི་ལོང་བ་དང་འོན་པ་དག་ནི་མི་མཛེས་པའི་ངོ་བོ་ཡིན་པའི་ཕྱིར་ལུས་མཛེས་པར་བྱ་བ་དང་། མཐོང་བ་དང་། ཐོས་ནས་ཡང༌[^399]བ་ཡོངས་སུ་སྤོང་བའི་ཕྱིར་ལུས་ཡོངས་སུ་བསྲུང་བ་དང་། མིག་དང་རྣ་བའི་རྣམ་པར་ཤེས་པ་མཚུངས་པར་ལྡན་པ་དང་བཅས་པ་དག་སྐྱེད་པ་དང་། གཟུགས་བལྟ་བ་དང་སྒྲ་མཉན་པ་དག་གི་ཐུན་མོང་མ་ཡིན་པའི་རྒྱུ་ཉིད་ལ་དབང་བྱེད་པའོ། །

[Block 895]
སྣ་དང་ལྕེ་དང་ལུས་རྣམས་ནི་སྔ་མ་བཞིན་དུ་མཛེས་པར་བྱ་བ་ལ་དབང་བྱེད་པ་དང་། དེ་དག་གི་ཁམ་གྱི་ཟས་ལ་ཡོངས་སུ་ལོངས་སྤྱོད་པའི་ཕྱིར་ལུས་ཡོངས་སུ་བསྲུང་བ་ལ་དབང་བྱེད་པ་དང་། སྣ་ལ་སོགས་པའི་རྣམ་པར་ཤེས་པས་མཚུངས་པར་ལྡན་པ་དང་བཅས་པ་རྣམས་སྐྱེད་པ༌[^400]དང་། དྲི་བསྣམས་པ༌[^401]དང་རོ་མྱང་བ་དང་། རེག་བྱ་རེག་པ་རྣམས་ཀྱི་ཐུན་མོང་མ་ཡིན་པའི་རྒྱུ་ཉིད་ལ་དབང་བྱེད་པའོ། །

[Block 896]
བཞི་རྣམས་གཉིས་ལ་ལོ། །

[Block 897]
ཕོ་དང་མོ་དང་སྲོག་དང་ཡིད་ཀྱི་དབང་པོ་རྣམས་ནི་རེ་རེ་ཞིང་དོན་གཉིས་ལ་དབང་བྱེད་དེ། རེ་ཞིག་ཕོ་དང་མོའི་དབང་པོ་དག་ནི་སེམས་ཅན་གྱི་བྱེ་བྲག་དང་། ཁྱད་པར་དག་ལ་དབང་བྱེད་དེ། དེ་ལ་སེམས་ཅན་གྱི་བྱེ་བྲག་ནི་ཕོའོ་མོའོ་ཞེས་བྱའོ། །

[Block 898]
སེམས་ཅན་གྱི་ཁྱད་པར་ནི་ནུ་མ་ལ་སོགས་པ་དབྱིབས་དང་ང་རོ་དང་སྤྱོད་པ་གཞན་པ་ཉིད་དོ། །

[Block 899]
གཞན་དག་ན་རེ་ནི་ཀུན་ནས་ཉོན་མོངས་པ་དང་རྣམ་པར་བྱང་བ་དག་ལ་དབང་བྱེད་དེ། འདི་ལྟར་དེ་དག་དང་མི་ལྡན་པ་དང་། ཉམས་པ་ཟ་མ་དང་མ་ནིང་དང་། མཚན་གཉིས་པ་རྣམས་ལ་སྡོམ་པ་མ་ཡིན་པ་དང་། མཚམས་མེད༌[^402]པ་དང་། དགེ་བའི་རྩ་བ་ཀུན་ཏུ་ཆད་པ་དང་། སྡོམ་པ་དང་། འབྲས་བུ་འཐོབ་པ་དང་། འདོད་ཆགས་དང་བྲལ་བ་རྣམས་མེད་དོ་ཞེས་ཟེར་རོ། །

[Block 900]
སྲོག་གི་དབང་པོ་ནི་རིས་མཐུན་པར་མཚམས་སྦྱོར་བ་དང་། ཡང་དག་པར་འཛིན་པ་དག་ལ་དབང་བྱེད་དོ། །

[Block 901]
ཡིད་ཀྱི་དབང་པོ་ནི་ཡང་སྲིད་པར་མཚམས་སྦྱོར་བ་དང་། དབང་གི་ངོ་བོ་དང་མཐུན་པར་བྱེད་པ་དག་ལ་དབང་བྱེད་དེ། དེ་ལ་ཡང་སྲིད་པར་མཚམས་སྦྱོར་བ་ལ་དབང་བྱེད་པ་ནི་ཇི་སྐད་དུ། དེའི་ཚེ་དྲི་ཟའི་སེམས་གཉིས་པོ་རྗེས་སུ་ཆགས་པ་དང་། ལྷན་ཅིག་པར་གྱུར་པ་འམ། ཁོང་ཁྲོ་བ་དང་ལྷན་ཅིག་པར་གྱུར་པ་གང་ཡང་རུང་བ་ཞིག་མངོན་དུ་གྱུར་ན་ཞེས་གསུངས་པ་ལྟ་བུའོ། །

[Block 902]
དབང་གི་ངོ་བོ་དང་མཐུན་པར་བྱེད་པ་ལ་དབང་བྱེད་པ་ནི་ཇི་སྐད་དུ། འཇིག་རྟེན་འདི་ནི་སེམས་ཀྱིས་ཁྲིད་དོ་ཞེས་རྒྱས་པར་གསུངས་པ་ལྟ་བུའོ། །

[Block 903]
བདེ་བ་ལ་སོགས་པའི་དབང་པོ་ལྔ་གང་ཡིན་པ་དང་། དད་པ་ལ་སོགས་པ་གང་དག་ཡིན་པ།

[Block 904 [VERSE]]
ལྔ་དང་བརྒྱད་པོ་དེ་རྣམས་ནི། །
ཀུན་ནས་ཉོན་མོངས་རྣམ༌[^403]བྱང་ལ། །
གོ་རིམས་བཞིན་དུ་དབང་བྱེད་དེ། །

[Block 905]
བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ། བདེ་བ་ལ་སོགས་པ་ལྔ་པོ་དག་ནི་ཀུན་ནས་ཉོན་མོངས་པ་ལ་དབང་བྱེད་དེ། དེ་དག་ལ་འདོད་ཆགས་ལ་སོགས་པ་རྒྱས་པར་འགྱུར་བ་ཉིད་ཀྱི༌[^404]ཕྱིར་རོ། །

[Block 906]
དད་པ་ལ་སོགས་པ་རྣམས་ནི་རྣམ་པར་བྱང་བ་ལ་དབང་བྱེད་དེ། དེ་དག་གིས་རྣམ་པར་བྱང་བར་བྱེད་དོ། །

[Block 907]
གཞན་དག་ན་རེ་བདེ་བ་ལ་སོགས་པ་རྣམས་ནི་རྣམ་པར་བྱང་བ་ལ་ཡང་དབང་བྱེད་དེ། འདི་ལྟར་བདེ་བར་གྱུར་པའི་སེམས་མཉམ་པར་འཇོག་པར་འགྱུར་རོ་ཞེས་བྱ་བ་དང་། སྡུག་བསྔལ་གྱི་རྒྱུ་ཅན་གྱི་དད་པ་ཞེས་བྱ་བ་དང་། ཡིད་བདེ་བ་ལ་སོགས་པ་ངེས་པར་འབྱུང་བ་ལ་རྟེན་པ༌[^405]དྲུག་ཅེས་འབྱུང་བའི་ཕྱིར་རོ་ཞེས་ཟེར་རོ། །

[Block 908]
གཞན་དག་ན་རེ་རྣམ་པར་ཤེས་ནས་ཡང་བ་ཡོངས་སུ་སྤོང་བའི་ཕྱིར་མིག་དང་རྣ་བ་དག་གིས་ལུས་ཡོངས་སུ་བསྲུང་བ་ནི་མ་ཡིན་པ་ཉིད་ཀྱི་དེ་གཉིས་རྣམ་པར་ཤེས་པ་ལ་ནི་དབང་བྱེད་དོ། །

[Block 909]
གང་གི་ཕྱིར་དེ་གཉིས་ཐུན་མོང་མ་ཡིན་པའི་རྒྱུ་ཉིད་ལ་སོ་སོར་དབང་བྱེད་པར་རུང་བར་འགྱུར་བ་རྣམ་པར་ཤེས་པ་ལས་གཞན་པ་གཟུགས་མཐོང་བ་འམ་སྒྲ་ཐོས་པ་ཡང་མེད་པ་དེའི་ཕྱིར་དེ་དག་དེ་ལྟ་བུར་ནི་དབང་པོ་ཉིད་མ་ཡིན་ནོ། །

[Block 910]
འོ་ན་ཇི་ལྟ་བུ་ཡིན་ཞེ་ན།

[Block 911 [VERSE]]
རང་གི་དོན་དང་ཐམས་ཅད་ལ། །
དམིགས་པར་དབང་བྱེད༌[^406]ཕྱིར་དབང་དྲུག །

[Block 912]
མིག་ལ་སོགས་པ་ལྔ་པོ་དག་ནི་རང་རང་གི་དོན་ལ་དམིགས་པར་བྱ་བ་ལ་དབང་བྱེད་དོ། །

[Block 913]
ཡིད་ནི་དོན་ཐམས་ཅད་ལ་དམིགས་པར་བྱ་བ་ལ་དབང་བྱེད་དེ། དེའི་ཕྱིར་དེ་དག་ནི་སོ་སོར་དབང་པོ་ཡིན་ནོ། །

[Block 914]
འདི་ལ་དོན་རྣམས་ཀྱང་དབང་བྱེད་པ་མ་ཡིན་ནམ་ཞེ་ན། དབང་བྱེད་པ་མ་ཡིན་ཏེ། ལྷག་པར་དབང་བྱེད་པ་ཉིད་ནི་དབང་བྱེད་པ་ཉིད་ཡིན་ལ། མིག་ནི་གཟུགས་ཐམས་ཅད་ལ་དམིགས་པར་བྱ་བ་ལ་ཐུན་མོང་གི་རྒྱུ་ཡིན་པའི་ཕྱིར་དང་། དམིགས་པ་དེ་གསལ་བ་དང་མི་གསལ་བ་ཉིད་ལ་སོགས་པའི་རྗེས་སུ་བྱེད་པའི་ཕྱིར་གཟུགས་ལ་དམིགས་པར་བྱ་བ་ལ་ལྷག་པར་དབང་བྱེད་པ་ཡིན་གྱི། དེ་ལས་བཟློག་པ་ཡིན་པའི་ཕྱིར་གཟུགས་ཀྱི་ནི་མ་ཡིན་ཏེ། ཡིད་ཆོས་རྣམས་ལ་དབང་བྱེད་པའི་བར་དུ་ཡང་དེ་བཞིན་དུ་སྦྱར་རོ། །

[Block 915 [VERSE]]
མོ་ཉིད་ཕོ་ཉིད་ལས་དབང་ཕྱིར། །
ལུས་ལས་མོ་དང་ཕོའི་དབང་དག །
--- END BLOCKS ---
