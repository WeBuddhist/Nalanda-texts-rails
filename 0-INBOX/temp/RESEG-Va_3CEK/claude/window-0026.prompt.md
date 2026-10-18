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
[Block 911]
བཅོམ་ལྡན་འདས་ཀྱིས་ལོག་པའི་ངག་དང་། ལོག་པའི་ལས་ཀྱི་མཐའ་དང་། ལོག་པའི་འཚོ་བ་ཞེས་གང་གསུངས་པ་དེ་གཉིས་ལས་གཞན་པའི་ལོག་པའི་འཚོ་བ་གང་ཞིག་ཡིན་ཞེ་ན། འདི་གཞན་ནི་མེད་ཀྱི་དེ་ཉིད་ཡིན་ཏེ། ལུས་དང་ངག་ལས་ཆགས་ལས་སྐྱེས། །ལོག་འཚོ། ལུས་དང་ངག་གི་ལས་ཀྱི་མཐའ་ཞེ་སྡང་ལས་སྐྱེས་པ་དང་། གཏི་མུག་ལས་སྐྱེས་པ་ནི་ལོག་པའི་ངག་དང་། ལོག་པའི་ལས་ཀྱི་མཐའ་ཡིན་ནོ། །

[Block 912]
དེ་ནི་སྦྱང་དཀའི་ཕྱིར། དེ་གཉིས་ལས་ལོགས་ཤིག་ཏུ་བསྟན་ཏོ། །

[Block 913]
ཆགས་པའི་ཆོས་ནི་འཕྲོག་པར་བྱེད་པ་ཡིན་པས༌[^686]དེས་ཀུན་ནས་བསླང་བའི་ལས་ལས་སེམས་བསྲུང་བར༌[^687]སླ་བ་མ་ཡིན་ཏེ། དེའི་ཕྱིར་ཇི་སྲིད་འཚོའི་བར་དུ་སྦྱང་དཀའ་བས་བསྒྲིམ་པར་བྱ་བའི་ཕྱིར་དེ་ནི་དེར་ལོགས་ཤིག་ཏུ་བསྟན་ཏོ། །

[Block 914]
འདིར་སྨྲས་པ། རྟག་ཏུ་ལྟ་བ་སྣ་ཚོགས་ཀྱིས།[^688] །

[Block 915 [VERSE]]
ཁྱིམ་པས་ལྟ་བ་སྦྱང་བར་དཀའ། །
གཞན་ལ་འཚོ་བ་རག་ལུས་པའི། །

[Block 916]
དགེ་སློང་གིས་ནི་འཚོ་བར་དཀའ།[^689] །གལ་ཏེ་ཡོ་བྱད་ལ། ཆགས་བསླང་། གང་ཞིག་འཚོ་བའི་ཡོ་བྱད་ལ། །ཆགས་པས་བསླང་བའི་ལུས་དང་ངག་གི་ལས་ཁོ་ན་ལོག་པའི་འཚོ་བ་ཡིན་གྱི། གཞན་ནི་མ་ཡིན་ཏེ། བདག་དགའ་བར་བྱ་བའི་ཆེད་དུ་གར་དང་གླུ་ལེན་པ་ལ་སོགས་པ་ནི་ལོག་པའི་འཚོ་བ་ཡིན་པར་མི་རིགས་སོ་སྙམ་དུ་སེམས་པ་དེ་ནི། མདོ་དང་འགལ་ཕྱིར་མིན། བཅོམ་ལྡན་འདས་ཀྱིས་ཚུལ་ཁྲིམས་ཀྱི་ཕུང་པོའི་མདོ་ལས་གླང་པོ་ཆེ་འཐབ་པ་ལ་ལྟ་བ་ལ་སོགས་པ་ལ་ཡང་ལོག་པའི་འཚོ་བ་གཞག་སྟེ། དེ༌[^690]ཅིའི་ཕྱིར་ཞེ་ན། ལོག་པའི་ཡུལ་ལ་ཡོངས་སུ་ལོངས་སྤྱོད་པའི་ཕྱིར་རོ། །

[Block 917]
འདི་ནི་རྫོགས་སོ།། །།

[Block 918 [HEADING]]
### ལས་འབྲས་བུ་དང་བཅས་པ། ^1-56-0

[Block 919]
གོང་དུ་འབྲས་བུ་ལྔ་བཤད་པ་གང་དག་ཡིན་པ་དེ་དག་ལས་ལས་གང་ཞིག་འབྲས་བུ༌[^691]དུ་ཞིག་འབྲས་བུ་དང་བཅས་པ་ཡིན་ཞེ་ན།

[Block 920 [VERSE]]
དྲིར་བཅས་སྤོང་བའི་ལམ་དག་གིས། །
ལས་ནི་ལྔ་ཡི་འབྲས་བུར་བཅས། །
སྤོང་བའི་ཕྱིར་ལམ་ཡིན་པའམ། །

[Block 921]
འདིས་ཉོན་མོངས་པ་སྤོང་བར་བྱེད་པས་སྤོང་བའི་ལམ་སྟེ། བར་ཆད་མེད་པའི་ལམ་ཡིན་ནོ། །

[Block 922]
ཟག་པ་དང་བཅས་པ༌[^692]དེའི་ལས་གང་ཡིན་པ་དེ་ནི་འབྲས་བུ་ལྔས་འབྲས་བུ་དང་བཅས་པ་ཡིན་ཏེ། དེའི་རྣམ་པར་སྨིན་པའི་འབྲས་བུ་ནི་རང་གི་སར་གཏོགས་པའི་རྣམ་པར་སྨིན་པ་ཡིད་དུ་མི༌[^693]འོང་བ་ཡིན་ནོ། །

[Block 923]
རྒྱུ་མཐུན་པའི་འབྲས་བུ་ནི་ཏིང་ངེ་འཛིན་ལས་སྐྱེས་པའི་ཆོས་འདྲ་བ་ཕྱི་མ་རྣམས་སོ། །

[Block 924]
བྲལ་བའི་འབྲས་བུ་ནི་བྲལ་བ་ཁོ་ན་ཡིན་ཏེ། སྤངས་པ་གང་ཡིན་པ་དེ་ཡིན་ནོ། །

[Block 925]
སྐྱེས་བུ་བྱེད་པའི་འབྲས་བུ་ནི་དེས་དྲང་པའི༌[^694]ཆོས་འདི་ལྟ་སྟེ། རྣམ་པར་གྲོལ་བའི་ལམ་དང་དེ་དག༌[^695]ལྷན་ཅིག་འབྱུང་བ་དང་། གང་ཡང་མ་འོངས་པ་ཐོབ་པ༌[^696]དང་། སྤངས་པ་དེ་ཡང་ཡིན་ནོ། །

[Block 926]
བདག་པོའི་འབྲས་བུ་ནི་སྔར་བྱུང་བ་རྣམས་མ་གཏོགས་པ་རང་གི་ངོ་བོ་ལས་གཞན་པའི་འདུ་བྱེད་ཐམས་ཅད་དོ། །

[Block 927]
དྲི་མེད་བཞི་ཡིས། སྤོང་བའི་ལམ་ཟག་པ་མེད་པའི་ལས་གང་ཡིན་པ་དེ་ནི་འབྲས་བུ་བཞིས་འབྲས་བུ་དང་བཅས་པ་ཡིན་ཏེ། རྣམ་པར་སྨིན་པའི་འབྲས་བུ་མ་གཏོགས་སོ། །

[Block 928]
ཟག༌[^697]བཅས་གཞན། དགེ་དང་མི་དགེ་གང་ཡིན་པའང་། །སྤོང་བའི་ལམ་ལས་གཞན་པའི་ལས་དགེ་བ་ཟག་པ་དང་བཅས་པ་གང་ཡིན་པ་དང་། མི་དགེ་བ་གང་ཡིན་པ་དེ་ཡང་འབྲས་བུ་བཞིས་འབྲས་བུ་དང་བཅས་པ་ཡིན་ཏེ།

[Block 929 [VERSE]]
བྲལ་བའི་འབྲས་བུ་མ་གཏོགས་སོ། །
ཟག་པ་མེད་པ་ལྷག་མ་དང་། །
ལུང་བསྟན་མིན་གང་གསུམ་གྱིས་སོ། །

[Block 930]
སྤོང་བའི་ལམ་ལས་གཞན་པའི་ལས་ཟག་པ་མེད་པ་དང་ལུང་དུ་མ་བསྟན་པའི་ལས་གང་ཡིན་པ་དེ་ནི་འབྲས་བུ་གསུམ་གྱི༌[^698]འབྲས་བུ་དང་བཅས་པ་ཡིན་ཏེ། རྣམ་པར་སྨིན་པ་དང་བྲལ་བའི་འབྲས་བུ་དག་མ་གཏོགས་སོ། །

[Block 931 [VERSE]]
དགེ་བའི་དགེ་ལ་སོགས་པ་ནི། །
བཞི་དང་གཉིས་དང་དེ་བཞིན་གསུམ། །

[Block 932]
རིམ་པ་བཞིན་ནོ་ཞེས་འོག་ནས་འཆད་དོ། །

[Block 933]
ལས་དགེ་བའི་འབྲས་བུ་ཆོས་དགེ་བ་ནི་བཞི་སྟེ། རྣམ་པར་སྨིན་པའི་འབྲས་བུ་མ་གཏོགས་སོ། །

[Block 934]
མི་དགེ་བ་གཉིས་ཏེ། སྐྱེས་བུ་བྱེད་པ་དང་། བདག་པོའི་འབྲས་བུ་དང་། [^699]ལུང་དུ་མ་བསྟན་པ་གསུམ་སྟེ།

[Block 935 [VERSE]]
རྒྱུ་མཐུན་པའི་འབྲས་བུ་མ་གཏོགས་སོ། །
མི་དགེའི༌[^700]དགེ་སོགས་གཉིས་དང་ནི། །
གསུམ་དང་བཞི་སྟེ་རིམ་པ་བཞིན། །

[Block 936]
གོ་རིམས་ཇི་ལྟ་བ་བཞིན་ཞེས་བྱ་བའི་ཐ་ཚིག་སྟེ། ལས་མི་དགེ་བའི་འབྲས་བུ་ཆོས་དགེ་བ་གཉིས་ཏེ། སྐྱེས་བུ་བྱེད་པ་དང་བདག་པོའི་འབྲས་བུ་དག་གོ། །

[Block 937]
མི་དགེ་བ་ནི་གསུམ་སྟེ། རྣམ་པར་སྨིན་པ་དང་བྲལ་བའི་འབྲས་བུ་མ་གཏོགས་སོ། །

[Block 938]
ལུང་དུ་མ་བསྟན་པ་ནི་བཞི་སྟེ་བྲལ་བ་མ་གཏོགས་སོ། །

[Block 939]
ལུང་དུ་མ་བསྟན་པ་འཇིག་ཚོགས་དང་མཐར་འཛིན་པར་ལྟ་བ་དག་ནི་མི་དགེ་བ་ཀུན་ཏུ་འགྲོ་བ་རྣམས་དང་། སྡུག་བསྔལ་མཐོང་བས་སྤང་བར་བྱ་བ་རྣམས་ཀྱི་རྒྱུ་མཐུན་པའི་འབྲས་བུ་ཡིན་ནོ། །

[Block 940 [VERSE]]
ལུང་བསྟན་མིན་གྱི་དགེ་ལ་སོགས། །
དེ་དག་གཉིས་དང་གསུམ་དང་གསུམ། །

[Block 941]
ལས་ལུང་དུ་མ་བསྟན་པའི་འབྲས་བུ་ཆོས་དགེ་བ་གཉིས་ཏེ། སྐྱེས་བུ་བྱེད་པ་དང་བདག་པོའི་འབྲས་བུ་དག་གོ། །

[Block 942]
མི་དགེ་བ་ནི་གསུམ་སྟེ། བྲལ་བ་དང་རྣམ་པར་སྨིན་པའི་འབྲས་བུ་མ་གཏོགས་སོ། །

[Block 943]
སྡུག་བསྔལ་ལ་སོགས་པ་མཐོང་བས་སྤང་བར་བྱ་བའི་མི་དགེ་བ་རྣམས་ནི་ལུང་དུ་མ་བསྟན་པའི་ལྟ་བ་གཉིས་ཀྱི་རྒྱུ་མཐུན་པའི་འབྲས་བུ་ཡིན་ནོ། །

[Block 944]
ལུང་དུ་མ་བསྟན་པའི་ཆོས་ནི་གསུམ་སྟེ།[^701] རྒྱུ་དེ་དག་ཁོ་ན་ཡིན་ནོ། །

[Block 945]
འདས་པའི་ཐམས་ཅད་བཞི་ཡིན་ནོ། །

[Block 946]
ཐམས་ཅད་ཅེས་བྱ་བ་ནི་དུས་གསུམ་པ་རྣམས་ཏེ། འདས་པའི་ལས་ཀྱི་འབྲས་བུ་དུས་གསུམ་པའི་ཆོས་ནི་བཞི་སྟེ།

[Block 947 [VERSE]]
བྲལ་བའི་འབྲས་བུ་མ་གཏོགས་སོ། །
བར་མ་ཡི་ནི་མ་འོངས་པའང་། །

[Block 948]
ད་ལྟར་བྱུང་བའི་ལས་ཀྱི་འབྲས་བུ་ཆོས་མ་འོངས་པ་ཡང་བཞི་སྟེ། དེ་དག་ཉིད་དོ། །

[Block 949]
བར་མ་གཉིས་སོ། །

[Block 950]
ད་ལྟར་བྱུང་བའི་འབྲས་བུ་ད་ལྟར་བྱུང་བའི་ཆོས་ནི་གཉིས་ཏེ། སྐྱེས་བུ་བྱེད་པ་དང་བདག་པོའི་འབྲས་བུ་དག་གོ། །
--- END BLOCKS ---
