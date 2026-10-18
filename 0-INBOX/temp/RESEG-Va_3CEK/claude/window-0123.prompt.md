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
[Block 4306]
གཞན་དག་ན་རེ་སེམས་ལས་བྱུང་བའི་བདེ་བའི་དབང་པོ་ནི༌[^3095]ཁོ་ན་སྟེ། བསམ་གཏན་གསུམ་ཆར་ན་ཡང་ལུས་ཀྱི་བདེ་བ་ཁོ་ན་ཡན་ལག་ཏུ་རྣམ་པར་གཞག་གོ་ཞེས་ཟེར་རོ། །

[Block 4307]
འོ་ན་མདོ་ལས།

[Block 4308]
བདེ་བའི་དབང་པོ་གང་ཞེ་ན་བདེ་བ་མྱོང་བར་འགྱུར་བའི་རེག་པས་རེག་པ་ན་ལུས་ཀྱི་དང་སེམས་ལས་བྱུང་བའི་ཚོར་བའི་རྣམ་པ༌[^3096]བདེ་བ་སིམ་པ་སྐྱེ་བ་གང་ཡིན་པ་དེ་ནི་བདེ་བའི་དབང་པོ་ཞེས་བྱའོ་ཞེས་གང༌[^3097]གསུངས་པ་ཇི་ལྟ་བུ་ཞེ་ན། ཚིག་དེ་ནི་འགའ་ཞིག་གིས༌[^3098]སྒྲོ་བཏགས་པ་ཡིན་ཏེ། སྡེ་པ་གཞན་ཐམས་ཅད་ལས་ལུས་ཀྱི་ཞེས་བྱ་བ་ཁོ་ན་འབྱུང་བའི་ཕྱིར་དང་། བདེ་བ་ལུས་ཀྱིས་མྱོང་ལ་ཞེས་རང་གི་སྒྲས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 4309]
གལ་ཏེ་ཡིད་ཀྱི་ལུས་ཀྱིས་སོ་ཞེ་ན་ནི། དེ་སྐད་བཤད་པ་ལ་ཡོན་ཏན་ཅི་ཞིག་ཡོད། བསམ་གཏན་བཞི་པ་ལ་ཤིན་ཏུ་སྦྱངས་པ་མང་བཞིན་དུ་བདེ་བ་མ་སྨོས་པའི་ཡང་ཕྱིར་རོ། །

[Block 4310]
གལ་ཏེ་བདེ་བའི་ཚོར་བ་དང་མཐུན་པའི་ཤིན་ཏུ་སྦྱངས་པ་བདེ་བ་ཡིན་ནོ་ཞེ་ན་ནི།

[Block 4311]
གསུམ་པ་ན་ཡོད་པའི་ཤིན་ཏུ་སྦྱངས་པ་བདེ་བར་མ་གསུངས་པ༌[^3099]ཡང་ཅིའི་ཕྱིར། གལ་ཏེ་བཏང་སྙོམས་ཀྱིས་བཅོམ་པའི་ཕྱིར་རོ་ཞེ་ན། མ་ཡིན་ཏེ། སྔ་མ་གཉིས་པས་དེ་ཁྱད་པར་དུ་འཕགས་པས་བཏང་སྙོམས་ཁོ་ནས་དེ་འཕེལ་བའི་ཕྱིར་རོ། །

[Block 4312]
གང་གི་ཚེ་འཕགས་པ་ཉན་ཐོས་རབ་ཏུ་དབེན་པའི་བདེ་བ་ལུས་ཀྱིས་མངོན་སུམ་དུ་བྱས་ནས་རྫོགས་པར་བྱས་ཏེ་གནས་པ་ཞེས་འབྱུང་བའི་མདོ་འདི་ལས་ཀྱང་ཤིན་ཏུ་སྦྱངས་པ་དང་བདེ་བ་གཉིས་ཐ་དད་པར་འབྱུང་བའི་ཕྱིར་ཤིན་ཏུ་སྦྱངས་པ་ཁོ་ན་བདེ་བ་མ་ཡིན་ནོ། །

[Block 4313]
གལ་ཏེ་སྙོམས་པར་ཞུགས་པ་ལ་ཇི་ལྟར་ལུས་ཀྱི་རྣམ་པར་ཤེས་པ་འབྱུང་ཞེ་ན། ཏིང་ངེ་འཛིན་གྱི་ཁྱད་པར་ལས་སྐྱེས་པ་ཤིན་ཏུ་སྦྱངས་པ་ཞེས་བྱ་བ་བདེ་བ་མྱོང་བར་འགྱུར་བའི་རླུང་གིས་ལུས་ལ་རྒྱས་པའི་ཕྱིར་རོ། །

[Block 4314]
གལ་ཏེ་ཕྱི་རོལ་དུ་རྣམ་པར་གཡེངས་པའི་ཕྱིར་ཏིང་ངེ་འཛིན་ལས་ཉམས་པར་འགྱུར་རོ་ཞེ་ན། མ་ཡིན་ཏེ། ཏིང་ངེ་འཛིན་ལས་སྐྱེས་པ་ལུས་ཀྱི་བདེ་བ་ནང་དུ་འབྱུང་བའི་ལུས་ཀྱི་བདེ་བ༌[^3100]ནི་ཏིང་ངེ་འཛིན་དང་མཐུན་པའི་ཕྱིར་རོ། །

[Block 4315]
གལ་ཏེ་ལུས་ཀྱི་རྣམ་པར་ཤེས་པ་སྐྱེས་པའི་ཚེ་ལངས་པར་འགྱུར་རོ་ཞེ་ན། མ་ཡིན་ཏེ། དེ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 4316]
གལ་ཏེ་འདོད་པ་ན་སྤྱོད་པའི་ལུས་ཀྱི་དབང་པོས་གཟུགས་ན་སྤྱོད་པའི༌[^3101]རེག་བྱ་ལ་རྣམ་པར་ཤེས་པ་མི་སྐྱེའོ་ཞེ་ན། མ་ཡིན་ཏེ། ཤིན་ཏུ་སྦྱངས་པའི་རྣམ་པར་ཤེས་པ་སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 4317]
གལ་ཏེ་ཡན་ལག་ཅུང་ཟད་ཅིག་ནི་ཟག་པ་དང་བཅས་པ་ཅུང་ཟད་ཅིག་ནི་ཟག་པ་མེད་པ་ཡིན་ན་མི་རུང་བས་རེག་བྱ་དང་ལུས་ཀྱི་རྣམ་པར་ཤེས་པ་ཟག་པ་མེད་པ་དག་ཏུ་ཡང་འགྱུར་རོ་ཞེ་ན། ལུས་ཤིན་ཏུ་སྦྱངས་པ་ཡང་དག་བྱང་ཆུབ་ཀྱི་ཡན་ལག་ཏུ་གསུངས་པས་འདོད་པའི་ཕྱིར་རོ། །

[Block 4318]
གལ་ཏེ་བྱང་ཆུབ་ཀྱི་ཡན་ལག་དང་མཐུན་པའི་ཕྱིར་རོ་ཞེ་ན་ནི་ཟག་པ་མེད་པ༌[^3102]ཉིད་ཀྱང་དེ་དང་འདྲའོ། །

[Block 4319]
གལ་ཏེ་ཟག་པ་དང་བཅས་པའི་ཆོས་རྣམས་གང་ཞེ་ན། མིག་ཇི་སྙེད་པ་ཞེས་འབྱུང་བའི་མདོ་འདི་དང་འགལ་ལོ་ཞེ་ན། མ་ཡིན་ཏེ། རེག་བྱ་དང་ལུས་ཀྱི་རྣམ་པར་ཤེས་པ་གཞན་ལས་དགོངས་ཏེ་གསུངས་པའི་ཕྱིར་རོ། །

[Block 4320]
གལ་ཏེ་ཟག་པ་མེད་པ་ལ་ཡན་ལག་ཅུང་ཟད་ཅིག་ནི་ཟག་པ་དང་བཅས་པ་ཅུང་ཟད་ཅིག་ནི་ཟག་པ་མེད་པར་འགྱུར་བ་མ་ཡིན་ནམ་ཞེ་ན། ཅིག་ཅར་མ་ཡིན་པའི་ཕྱིར་ཉེས་པ་ཅི་ཞིག་ཡོད། གལ་ཏེ་བདེ་བ་དང་དགའ་བ་ཕྲད་པ་མེད་པའི་ཕྱིར་ཡན་ལག་ལྔ་པར་མི་འགྱུར་རོ་ཞེ་ན། མ་ཡིན་ཏེ། སྲིད་པའི་ཕྱིར་བསྟན་པས་རྟོག་པ་དང་དཔྱོད་པ་བཞིན་ནོ། །

[Block 4321]
གལ་ཏེ་བསྒྲུབ་པར་བྱ་བ་ཡིན་ནོ་ཞེ་ན། སེམས་རྩིང་བ་དང་ཞིབ་པ་གཉིས་འགལ་བའི་ཕྱིར་དང་། ཉེས་པ་སྨོས་པའི་ཕྱིར་གྲུབ་པ་ཡིན་ནོ། །

[Block 4322]
དེ་ལྟ་བས་ན་བསམ་གཏན་དང་པོ་ལ་ཡོད་པའི་ཡན་ལག་ལྔ་པོ་གང་དག༌[^3103]ཡིན་པ་དེ་དག་ཁོ་ན་ལས་ཡན་ལག་གཉིས་དང་གསུམ་དང་བཞི་བོར་ནས་བསམ་གཏན་གཉིས་པ་ལ་སོགས་པ་རྣམ་པར་གཞག་གོ། །

[Block 4323]
དེ་ཉིད་ཀྱི༌[^3104]ཕྱིར་བསམ་གཏན་དང་པོ་ལ་ནི༌[^3105]ཡན་ལག་ལྔ༌[^3106]ཉིད་དུ་བཤད་ལ། དེ་དག་ལས་བོར་བས་ནི་བསམ་གཏན་ཕྱི་མ་རྣམ་པར་གཞག་པའི་ཕྱིར་འདུ་ཤེས་ལ་སོགས་པ་ནི་མ་ཡིན་ནོ། །

[Block 4324]
ཡང་ན་ཅིའི་ཕྱིར་ལྔ་ཁོ་ན་ཡན་ལག་ཉིད་ཡིན། གལ་ཏེ་ཕན་པའི་ཕྱིར་རོ་ཞེ་ན། མ་ཡིན་ཏེ། [^3107]རྟོག་པ་དང་དཔྱོད་པ་གཉིས་པས་དྲན་པ་དང་ཤེས་རབ་དག་ཆེས་ཕན་པའི་ཕྱིར་རོ། །

[Block 4325]
ཁ་ཅིག་དེ་སྐད་དུ་རྒོལ་བ་ཡོད་མོད༌[^3108]ཀྱི་སྔོན་གྱི་སློབ་དཔོན་རྣམས་ནི༌[^3109]ཇི་སྙེད་མངོན་པ་དེ་ལྟར༌[^3110]མི་སྟོན་ཏེ། [^3111]དེ་ལྟ་བས་ན་འདི་ནི་དཔྱད་པར་བྱ་བ་ཡིན་ནོ། །

[Block 4326 [HEADING]]
###### ནང་རབ་ཏུ་དང་བ། ^5-1-6-6-2-0

[Block 4327]
ནང་རབ་ཏུ་དང་བ༌[^3112]ཞེས་བྱ་བའི་ཆོས་འདི་ཅི་ཞེ་ན། རྟོག་པ་དང་དཔྱོད་པའི་འཁྲུག་པ་དང་བྲལ་བས་རྒྱུད་རབ་ཏུ་ཞི་བར་གྱུར་པ་ནི་ནང་རབ་ཏུ་དང་བ་ཡིན་ཏེ། རྟོག་པ་དང་དཔྱོད་པས་དཀྲུགས་པའི་རྒྱུད་ནི་ཆུ་བོ་དབའ་རླབས་དང་བཅས་པ༌[^3113]བཞིན་དུ་རབ་ཏུ་མ་དང་བ་ཡིན་ནོ། །

[Block 4328]
འོ་ན་ནི་དེ་རྫས་གཞན་མ་ཡིན་པས༌[^3114]ཇི་ལྟར་ན་རྫས་སུ་ཡན་ལག་བཅུ་གཅིག་ཡིན། དེ་ལྟ་བས་ན། རབ་ཏུ་དང་བ༌[^3115]དད་པ༌[^3116]ཡིན། །དེ་ནི་བསམ་གཏན་གཉིས་པ་ཐོབ་པའི་ཕྱིར་མཉམ་པར་གཞག་པའི་ས་ལས་ངེས་པར་འབྱུང་བ་ལ་ཡིད་ཆེས་པ་སྐྱེ་སྟེ། དེ་ནི་འདིར་ནང༌[^3117]རབ་ཏུ་དང་བ་ཞེས་བྱའོ། །

[Block 4329]
གཞན་དག་ན་རེ་རྟོག་པ་དང་དཔྱོད་པ་དང་། ཏིང་ངེ་འཛིན་རྣམས་ཀྱང་རྫས་གཞན་མ་ཡིན་ལ་ནང་རབ་ཏུ་དང་བ་ཡང་རྫས་གཞན་མ་ཡིན་ནོ། །

[Block 4330]
རྫས་གཞན་མེད་ན་ཇི་ལྟར་སེམས་ལས་བྱུང་བ་ཉིད་དུ་འགྲུབ་ཅེ་ན། སེམས་ཅན་གྱི༌[^3118]གནས་སྐབས་ཀྱི་བྱེ་བྲག་ཀྱང་སེམས་ལས་བྱུང་བ་ཡིན་ནོ་ཞེས་ཟེར་ཏེ། འདི་ནི་བསྟན་བཅོས་ཀྱི་གྲུབ་པའི་མཐའ་མ་ཡིན་ནོ། །

[Block 4331 [HEADING]]
###### དགའ་བ་ནི་ཡིད་བདེ་བ། ^5-1-6-6-3-0

[Block 4332]
[^3119]དགའ་བ་ནི་ཡིད་བདེ་བ་ཡིན་ནོ་ཞེས་གང་བཤད་པ་འདི་ཇི་ལྟར་ཁོང་དུ་ཆུད། གཞན་ཅི་ཞིག་ཡིན། ཇི་ལྟར་སྡེ་པ་གཞན་དག་འདོད་པ་ལྟ་བུ་ཡིན་ནོ། །

[Block 4333]
སྡེ་པ་གཞན་དག་ཇི་ལྟར་འདོད་ཅེ་ན། དགའ་བ་ནི་སེམས་ལས་བྱུང་བའི་ཆོས་གཞན་དག༌[^3120]ཁོ་ན་ཡིན་ལ་ཡིད་བདེ་བ་ནི་བསམ་གཏན་གསུམ་ཆར་གྱི་ཡང་བདེ་བ་ཡིན་པར་འདོད་དོ། །

[Block 4334]
བསམ་གཏན་དག་ན་ཡོད་པའི་བདེ་བ་ནི་ཡིད་བདེ་བ་ཡིན་པར་མི་རུང་བ་ཉིད་ཀྱི། ལུས༌[^3121]རྣམས་གཉིས་ཕྱིར་དགའ་ཡིད་བདེ། །བཅོམ་ལྡན་འདས་ཀྱིས༌[^3122]རྣམ་པར་སྒྱུར་བའི་མདོ་ལས་བསམ་གཏན་གསུམ་པ་བཀའ་སྩལ་ནས་འདིར་འདིའི་ཡིད་བདེ་བའི་དབང་པོ་སྐྱེས་པ༌[^3123]མ་ལུས་པར་འགག་པར་འགྱུར་རོ་ཞེས་བཀའ་སྩལ་ལ། [^3124]བསམ་གཏན་བཞི་པ་ལ་ནི་བདེ་བའི་དབང་པོ་འགག་པར་འགྱུར་རོ་ཞེས་བཀའ་སྩལ་ཏོ། །

[Block 4335]
ཡང་བདེ་བ་ཡང་སྤངས་ཏེ་སྔ་ནས་སྡུག་བསྔལ་ཡང་སྤངས་ཤིང་ཡིད་བདེ་བ་དང་ཡིད་མི་བདེ་བ་ཡང་ནུབ་པས་ཞེས་གསུངས་པས་དེའི་ཕྱིར་ཡང་བསམ་གཏན་གསུམ་པ་ན༌[^3125]ཡིད་བདེ་བའི་དབང་པོ་མེད་དེ། དེ་ལྟར༌[^3126]བས་ན་དགའ་བ་ཁོ་ན་ཡིད་བདེ་བ་ཡིན་གྱི་བདེ་བ་ནི་མ་ཡིན་ནོ། །

[Block 4336 [HEADING]]
#### ཉོན་མོངས་པ་ཅན་གྱི་བསམ་གཏན། ^5-1-7-0

[Block 4337]
ཅི་ཉོན་མོངས་པ༌[^3127]ཅན་གྱི་བསམ་གཏན་དག་ལ་ཡང་ཇི་སྐད་དུ་བཤད་པ་ལྟར་ཡན་ལག་དེ་དག་ཡོད་དམ་ཞེ་ན།[^3128] མེད་དོ། །

[Block 4338]
དེ་དག་ན་ཅི་ཞིག་མེད་ཅེ་ན།

[Block 4339 [VERSE]]
ཉོན་མོངས་ཅན་ལ་དགའ་བདེ་དང་། །
དྲན་དང་ཤེས་བཞིན་དྲན་པ་དང་། །
བཏང་སྙོམས་དྲན་པ་དག་པ་མེད། །

[Block 4340]
བསམ་གཏན་དང་པོ་ལ་ནི་བདེ་བ༌[^3129]ལས་སྐྱེས་པའི་དགའ་བ་དང་བདེ་བ་མེད་དེ། ཉོན་མོངས་པ་ལས་དབེན་པ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4341]
གཉིས་པ་ལ་ནི་ནང་རབ་ཏུ་དང་བ་མེད་དེ། ཉོན་མོངས་པས་རྙོག་པའི༌[^3130]ཕྱིར་རོ། །

[Block 4342]
གསུམ་པ་ལ་ནི་དྲན་པ་དང་ཤེས་བཞིན་མེད་དེ། ཉོན་མོངས་པ་ཅན་གྱི་བདེ་བས༌[^3131]ཀུན་དུ་རྨོངས་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 4343]
བཞི་པ་ལ་ནི་བཏང་སྙོམས་དང་དྲན་པ་ཡོངས་སུ་དག་པ་མེད་དེ། ཉོན་མོངས་པས་དྲི་མ་ཅན་དུ་བྱས་པའི་ཕྱིར་རོ། །

[Block 4344]
རེ་ཞིག་ཁ་ཅིག་དེ་སྐད་ཟེར་རོ། །

[Block 4345]
ཁ༌[^3132]ཅིག་ཤིན་ཏུ་སྦྱངས་བཏང་སྙོམས། །ཁ་ཅིག་ན་རེ་ཉོན་མོངས་པ་ཅན་དང་པོ་དང་གཉིས་པ་དག་ན་ནི་ཤིན་ཏུ་སྦྱངས་པ་མེད་ལ་གསུམ་པ་དང་བཞི་པ་དག་ན་ནི་བཏང་སྙོམས་མེད་དེ། །དེ་གཉིས་ནི་དགེ་བའི་ས་མང་པོ་པ་ཡིན་པའི་ཕྱིར་རོ་ཞེས་ཟེར་རོ། །
--- END BLOCKS ---
