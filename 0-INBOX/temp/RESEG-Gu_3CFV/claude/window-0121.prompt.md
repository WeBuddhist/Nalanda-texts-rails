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
[Block 4236]
དེའི་ཚེ་གནས་ན་སོ་སོར་ཐར་པའི་མདོ་གདོན༌[^2922]ནུས་པ་མེད་པར་ཤེས་ན་གསོ་སྦྱོང་ལ་བསྡད་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། དེའི་ཚེ་ཞེས་བྱ་བ་ལ་ནི་གསོ་སྦྱོང་ལ་ལྟོས་པའི་གསོ་སྦྱོང་གི་དུས་ལ་གང་དུ་སྟོན་པ་པོ་མེད་པར་གྱུར་ན་ཞེས་བྱའོ། །

[Block 4237]
གང་ན༌[^2923]དེ་ལས་འདའ་བར༌[^2924]དེར་ཉེ་བར་འགྲོ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ལས་ཞེས་བྱ་བ་ནི་གསོ་སྦྱོང་ལའོ། །

[Block 4238]
མདོ་འདོན་ནུས་པ་མེད་པ་ལ་ནི་འདི་སྨོས་སོ། །

[Block 4239]
ཚོགས་པ་མེད་པ་ལ་ཡང་དེ་ཉིད་ཀྱི་ཕྱིར་འདིའི་ལྟུང་བ་སྟེ།[^2925] བར་ཆད་གཞན་གྱིས་བསྟན་པ་མེད་པ་ལ་དེ་བས་ན་འདི་ལྟར་བྱའོ། །

[Block 4240]
གནས་པར༌[^2926]ཁས་བླངས་པ་ཕྱི་མའི་གོང་མ་བསྲུང་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི། ཁས་བླངས་པ་ཕྱི་མ་ཤོས་ཀྱིས་སྔ་མ་དེ་བསྲུང་བར་མི་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4241]
ཕྱི་མ་ཤོས་འགྲོ་བའི་ཕྱིར་སྔ་མ་དེ་སྒྲུབ་པ་ཞེས་བྱ་བར་དགོངས་པའོ། །

[Block 4242]
དེ་བས་ན་སྔ་མ་གཞན་ལས་དབྱར་དྲལ་བ་ལ་ཕྱི་མ་ཁས་བླང་བར༌[^2927]བྱའོ་ཞེས་བྱ་བ་འདིས་དེ་བྱས་པར་རིག་པར་བྱའོ། །

[Block 4243]
དེ་ལ་ཡང་ཟླ་བ་གཉིས་ལས་ལྷག་པའོ་ཞེས་བྱ་བ་ནི་ཁས་བླངས་པ་ཕྱི་མ་ཤོས་དེ་ཟླ་བ་གཉིས་བསྲུང་གི་གཉིས་ལས་ལྷག་པ་གསུམ་པ་བསྲུང་བར་མི་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4244]
གནས་དང་ལས་དང་རྙེད་པ་དང་བསྙེན་བཀུར་བསྟབས་པས་གདོན་པར༌[^2928]བྱེད་པ་བསྙེན་པར་བྱའོ་ཞེས་བྱ་བ་ནི། འདི་འདོན་པ༌[^2929]པོའི་ཕྱིར་འབད་པར་བྱེད་པ་མེད་པའོ། །

[Block 4245]
དེ་བས་ན་མ་གྲུབ་པ་ལ་འབད་པ་དེ་ལྟ་བུ་བྱས་ནས་ཀྱང་ཆོ་ག་བྱ་བ་ལ་རྗེས་སུ་བསྒྲུབ་པ་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 4246]
འདིར་གནས་ཞེས་བྱ་བ་ནི་གནས་ཁང་དང་། མལ་ཆ་དང་། སྟན་དང་བགོ་བ་ལ་སོགས་པ་ཡིན་པར་རིག་པར༌[^2930]བྱའོ། །

[Block 4247]
ལས་ཞེས་བྱ་བ་ནི་གང་གི་ལས་ཏེ་དེ་དག་ཏུ་མི་བསྐོ་བའོ། །

[Block 4248]
རྙེད་པ་ཞེས་བྱ་བ་ནི་ཆོས་གོས་དང་བསོད་སྙོམས་དང་སྣུམ་བག་ལ་སོགས་པའོ། །

[Block 4249]
འདི་དག་གིས་བསྙེན་བཀུར་བསྟབས་པ་ནི་འདོད་པ་འདི་དག་གིས་མ༌[^2931]བྲལ་བ་ཉིད་དུ་ངེས་པར་བྱེད་པའོ། །

[Block 4250]
མདོ་སྡེ་འཛིན་པ་འོང་བ་ན༌[^2932]གདུགས་དང་། རྒྱལ་མཚན་དང་བ་དན་ལ་སོགས་པ་དག་གིས་བསུ་བར་བྱའོ། །

[Block 4251]
འདུལ་བ་དང་མ་མོ༌[^2933]ཡང་ངོ་ཞེས་བྱ་བ་ན༌[^2934]འདུལ་བ་འཛིན་པ་དང་མ་མོ་འཛིན་པ་འོང་བ༌[^2935]ལ་གདུགས་དང་རྒྱལ་མཚན་དང་བ་དན་ལ་སོགས་པ་དག་གིས་བསུ་བར་བྱའོ། །

[Block 4252]
ལམ་ཇི་སྲིད་དུ་ཞེ་ན། དེའི་ཕྱིར་དཔག་ཚད་ཕྱེད་དང་གསུམ་དུའོ། །

[Block 4253]
མ་ནུས་ན་རྒྱང་གྲགས་ལྔར་རོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ལམ་དེ་ཙམ་དུ་བསུ་བར་མི་ནུས་ན་རྒྱང་གྲགས་ལྔར་བསུ་བར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4254]
གསུམ་མམ་དཔག་ཚད་ཕྱེད་དམ་རྒྱང་གྲགས་སམ་རྒྱང་གྲགས་ཕྱེད་དམ་ཁྱམས་སུ་རུང་ངོ་ཞེས་བྱ་བ་ལ། གསུམ་ཞེས་བྱ་བ་ནི་རྒྱང་གྲགས་རྣམས་ཀྱང་ངོ་། །མ་ནུས་ན་ཞེས་བྱ་བ་ནི་ཐམས་ཅད་ལ་སྦྱར་བར་བྱའོ། །

[Block 4255]
དེ་ལྟར་བསུ་ནས་ཅི་ཞིག་བྱ་ཞེ་ན། དེའི་ཕྱིར་ངག་གི་བཤེས་པའི་ཚིག་གིས་བསུ་ནས་ལྷུང་བཟེད་དང་ཆོས་གོས་བླང་བར་བྱའོ། །

[Block 4256]
ཁྲུས་བྱའོ། །

[Block 4257]
དགེ་འདུན་ལ་ཡང་སྣུམ་བག་གིས་རྙེད་པའོ། །

[Block 4258]
གནས་ལ་སོགས་པ་བསྟབས་པ་སྦྱིན་ནོ། །

[Block 4259]
ཆོས་ཉན་པ་ཡང་ངོ༌[^2936]ཞེས་བྱ་བ་ནི། སྦྱིན་ནོ་ཞེས་བྱ་བར་སྦྱར་ཏེ། དེར་ཐམས་ཅད་ཀྱིས༌[^2937]སྤྲོ་བ་བསྐྱེད་པར་བྱ་ཞེས་བྱ་བ་ནི། མང་པོའི་ཚིག་གིས་བསྟན་པ་དེ་རྣམས་ཐམས་ཅད་ཀྱིས་སྨྲ་བར་མི་རིགས་པའི་ཕྱིར་རོ། །

[Block 4260]
དགེ་སློང་ཕྲག་དོག་ཅན་ལ་འདི་དག་སྟོན་པར་འཛིན་པ་ཡིན་ནོ་ཞེས་གོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི། འདི་སྟོན་པའོ་འདི་ནི་སྟོན་ཏེ་འདི་ལྟ་སྟེ། མདོ་སྡེ་དང་འདུལ་བ་འཛིན་པ་དང་མ་མོ་ཞེས་གསུངས་པ་དེ་འདིས་བསྡུས་པ་ཡིན་ནོ། །

[Block 4261]
གསོ་སྦྱོང་དང་དགག་དབྱེ་མ་བྱས་པས་དེའི་ཉིན་མོ་རང་གི་དེ་ཡོད་པའི་གནས་ནས་འགྲོ་བར་མི་བྱ་སྟེ། གལ་ཏེ་དེ་ཉིད་ཀྱི་ཚེ་རྣམ་པ་དེ་ལྟ་བུར་ཕྱིན་པའམ། འཐབ་ཀྲོལ་ཅན་དག་དང་དབྲལ་བའམ། སྤྱོད་པ་བཟང་པོ་དག་དང་ཕྲད་པ་དེ་ལྟ་བུར་འགྲོ་བ་ཉིད་མ་ཡིན་ནའོ་ཞེས་བྱ་བ་ལ། དེའི་ཉིན་མོ་ཞེས་བྱ་བ་ནི་གསོ་སྦྱོང་དང་དགག་དབྱེའི་ཉིན་མོ་ལའོ། །

[Block 4262]
རང་གི་ཞེས་བྱ་བ་ནི་དགེ་སློང་རྣམས་དང་ལྷན་ཅིག་མདོ་འདོན་པ་དང་སྤྱོད་པའོ། །

[Block 4263]
ཡང་ན་རང་གི་ཞེས་བྱ་བ་ནི་དགེ་སློང་མའི་དགག་དབྱེ་དགེ་སློང་དང་དགེ་སློང་མ་རྣམས་ལྷན་ཅིག་ཏུ་མདོ་འདོན་པའི་ཚེ་དགེ་སློང་གི་ཚོགས་པ་གྲུབ་པ་དགེ་སློང་མ་རྣམས་དང་ལྷན་ཅིག་ཏུའོ། །

[Block 4264]
དེ་ཞེས་བྱ་བ་ནི་གསོ་སྦྱོང་དང་དགག་དབྱེ་ལ་ལྟོས་ནས་བདག་ཉིད་ཀྱིས༌[^2938]གསོ་སྦྱོང་ངམ་དགག་དབྱེ་རབ་ཏུ་ཤེས་བཞིན་དུ་རང་དགག་དབྱེ༌[^2939]ཉིད་དུ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4265]
དེ་ཉིད་ཀྱི༌[^2940]ཚེ་ཞེས་བྱ་བ་ནི་གསོ་སྦྱོང་དང་དགག་དབྱེའི་ཉི་མ་དེ་ཉིད་ལ་རྣམ་པ་དེ་ལྟ་བུའི་ཚིག་གིས་རབ་ཏུ་ཤེས་བཞིན་པ་དེ་བས་ན་གནས་འཛིན་པའོ། །

[Block 4266]
འཐབ་ཀྲོལ་ཅན་ཞེས་བྱ་བ་ནི་འཐབ་ཀྲོལ༌[^2941]བྱེད་པ་པོ་རྣམས་ལས་བདག་འབྲལ་བར་འགྱུར་སྙམ་ནས་གལ་ཏེ་འདི་ཉིད་གཞན་དབང་ཉིད་དུ་ཐོབ་པར་བྱེད་པའོ། །

[Block 4267]
སྤྱོད་པ་བཟང་པོ་དག་དང་ཕྲད་པ་དེ་ལྟ་བུར་འགྲོ་བ་ཉིད་མ་ཡིན་ནའོ་ཞེས་བྱ་བ་ནི། གལ་ཏེ་སྤྱོད་པ་བཟང་པོ་དག་ཕྲད་པ་དེ་ལྟ་བུ་འགྲོ་བ་ཉིད་ཡིན་ན་འགྲོ་བ་ལ་ཉེས་པ་མེད་དོ། །

[Block 4268]
གནས་གང་ན་རང་གི་གསོ་སྦྱོང་དང་དགག་དབྱེའམ། གཞན་གང་ཡང་རུང་བ་མེད་པར་གྱུར་ན་ཡང་གནས་དེ་ནས་འགྲོ་བར་བྱ་བ་ཉིད་དོ། །

[Block 4269]
དེ་ལ་སྟོན་པས་ཀྱང་དེ་ལྟ་བུའི་འཐབ་ཀྲོལ་ཅན་མ་ཡིན་པ༌[^2942]རང་འཇུག་པ་རྣམས་ལ་ཡང་གསོ་སྦྱོང་དང་རྣམ་པར་དག་པ་ཁས་ལེན་པ་དགག་དབྱེས༌[^2943]ཀྱང་ངོ་། །གང་ན་འོངས་པ་མེད་ན་གཅིག་པུ་རབ་ཏུ་ཞི་བའི་སེམས་ཀྱིས་སྤྱོད་པ་བཟང་པོའི་ནང་ན་གནས་པའི་བྱིན་གྱིས་བརླབས་པའི་སྔ་རོལ་དུ་དགེ་སློང་དག་དང་བཅས་པའི་གནས་ནས་གནས་མེད་ཀྱང་དགེ་སློང་དེ་འགྲོ་བར་བྱ་སྟེ། གང་ན་དགེ་སློང་ཚུལ་ཁྲིམས་ཡོངས་སུ་དག་པ་ལྟ་བ་མཐུན་པ་དག་པས་འཛིན་པ་དགེ་སློང་དང་བཅས་པའི་གནས་སུ་འགྲོ་བར་བྱའོ་ཞེས་མདོར་བྱས་སོ། །

[Block 4270]
འདིར་ལྟ་བ་ཡང་ཚུལ་ཁྲིམས༌[^2944]ཉིད་ཀྱིས་སྨོས་པར་རིག་པར་བྱའོ། །

[Block 4271]
གནས་གང་ན་དགེ་སློང་དང་བཅས་ཀྱང་དགེ་སློང་འཐབ་ཀྲོལ་བྱེད་པ་ཡོད་པ་དེར་འགྲོ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི། གང་ཞིག་འཐབ་ཀྲོལ་བྱེད་པ་སྤང་བའི་ཕྱིར་གསོ་སྦྱོང་དང་དགག་དབྱེ་དག་བཤོལ་བར་གསུངས་པ་དེ་ནི་འཐབ་ཀྲོལ་ཅན་དག་ཅེས་བྱ་བའི་མདོར་བྱས་སོ། །

[Block 4272]
གང་གི་ཕྱིར་དེར་འགྲོ་བ་བཀག་པ་དེའི༌[^2945]ཕྱིར་སྤྱོད་པ་བཟང་པོ་ཅན་གྱི་དགེ་སློང་དང་བཅས་པ་ནས་འཐབ་ཀྲོལ་ཅན་གྱི་དགེ་སློང་དང་བཅས་པར་འགྲོ་བར་མི་བྱའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 4273]
དགེ་སློང་མེད་པར་འགྲོ་བར་མི་བྱའོ་ཞེས་བྱ་བའི་ཉེས་པ་གཞན་སྟོན་པའི་ཚིག་བསྡུ་བའི་ཕྱིར། དགེ་སློང་དང་བཅས་པ་ནས་དགེ་སློང་མེད་པར་ལྷག་མ་རྣམས་དང་ལྷན་ཅིག་མ་ཡིན་པའམ་གནོད་པ་དང་ལུས་དང་སེམས་ཤིན་ཏུ་སྦྱངས་པའི་དབང་མ་གཏོགས་པར་འགྲོ་བར་མི་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཅི་དགེ་སློང་དང་བཅས་པའི་གནས་ན་གནས་པའི་དགེ་སློང་རྣམས་དང་ཡང་ལྷན་ཅིག་ཏུ་མི་རིགས་སམ་ཞེ་ན། དེའི་ཕྱིར་འདིར་ལྷག་མ་རྣམས་དང་ལྷན་ཅིག་མ་ཡིན་པར་ཞེས་བྱ་བ༌[^2946]སྨོས་ཏེ། དགེ་སློང་དང་བཅས་པའི་གནས་ས་མ་གཙུག་ལག་ཁང་ན་གནས་པའི་དགེ་སློང་རྣམས་ཀྱིས་སོ། །ཅི་འདི་ངེས་པ༌[^2947]ཁོ་ནར་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་ལུས་དང་སེམས་ཤིན་ཏུ་སྦྱངས་པའི་དབང་མ་གཏོགས་པར་ཞེས་བྱ་བ་སྨོས་ཏེ། གལ་ཏེ་དེར་སོང་ནས་ལུས་དང་སེམས༌[^2948]ཤིན་ཏུ་སྦྱངས་པ་སྐྱེ་བར་འགྱུར་ཞང་དེའི་དབང་གིས༌[^2949]ནི་དགེ་སློང་དང་བཅས་པའི་གནས་ནས་དགེ་སློང་མེད་པའི་གནས་སུ་འགྲོ་བར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4274]
དགེ་སློང་གསོ་སྦྱོང་རྗེས་སུ་གཟུང་བར༌[^2950]བྱ་བ་ཉིད་དུ་གྱུར་པས་ཀྱང༌[^2951]རུང་བ་ཉིད་དང་ཐུགས་བརྩེ་བ་ཉིད་ཅེས་བྱ་བ་འདི་རིགས་པ་ཡིན་ཏེ། དེའི་དོན་དུ་གསོ་སྦྱོང་དང་དགག་དབྱེ་དག་བྱིན་གྱིས་བརླབ་པ༌[^2952]ཙམ་དུ་རིགས་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 4275]
འགྲོ་བའི་ཕྱིར་གནས་པའི་གསོ་སྦྱོང་དང་དགག་དབྱེ་མ་བྱས་པར་དོར་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི། དེའི་ཉིན་མོ་ཞེས་བྱ་བར་སྦྱར་རོ། །
--- END BLOCKS ---
