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

[Block 4276]
རྐྱེན་དེ་ལྟ་བུ་ཉིད་ཡོད་ན་སྤྱོད་པ་བཟང་པོ་དང་ལྡན་པ་དང་། གནོད་པ༌[^2953]དང་ལྡན་པའི་གནས་བསྟན༌[^2954]ནས་དེར༌[^2955]འགྲོར་གཞུག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་སྤྱོད་པ་བཟང་པོ་དང་ལྡན་པ་དང་། བསྟན་པ༌[^2956]དང་ལྡན་པའོ། །

[Block 4277]
འདིར་གཞུང་ནི། གནས་ག་གེ་མོར་འཇུག་པར་བྱ་སྟེ། དེ་ནི་དགེ་སློང་གི་དགེ་འདུན་གྱིས༌[^2957]གནས་བརྟན་དང་བཅས་པ་སོ་སོར་ཐར་པ་དང་བཅས་ཤིང་དགེ་སློང་ཚུལ་ཁྲིམས་དང་ལྡན་པ་ཡོན་ཏན་དང་ལྡན་པ་དེས༌[^2958]དགེ་བའི་ཆོས་ཅན༌[^2959]དག་འཁོད་ཀྱི།[^2960] དེ་དག་གི་འགྱོད་པ་མ་སྐྱེས་པ་ནི་སྐྱེད་པར༌[^2961]མི་འགྱུར་ལ། སྐྱེས་པ་ནི་སྐད་ཅིག་མ་ཉིད་དུ་སླར་སེལ་བར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4278]
སོ་སོར་ཐར་པ་དང་བཅས་པ་ཞེས་བྱ་བ་འདིས་ནི་དགེ་འདུན་གྱི་གནས༌[^2962]བརྟན་གདོན་པ༌[^2963]དང་ལྡན་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 4279]
བསྒོ་བར༌[^2964]ད་ལས་འདའ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི། བརྟེན་པས་བརྗོད་པ་གང་ཡིན་པ་དེ་ཉིད་བསྒྲུབ་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4280]
ཕྱིས་འོངས་པ་རྣམས་ཀྱི་དོན་དུ་དེ་གཉིས་ཡང་བྱར་རུང་ངོ་ཞེས་བྱ་བ་ནི་གསོ་སྦྱོང་དང་དགག་དབྱེ་འདི་དག་ཡང་བྱེད་པའོ། །

[Block 4281]
གལ་ཏེ་ལེགས་པར་ན་དེ་ལ་ཅི་དགར་འཇུག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་གསོ་སྦྱོང་དང་དགག་དབྱེ་དེ་གཉིས་ལེགས་པར་བྱས་པ་ཡིན་ནོ།[^2965] །དེའི་ཚེ་འདོད་པ་ནི་འདོད་པ་སྟེ་ཡང་འཇུག་པ་ལའོ། །

[Block 4282]
འོན་ཏེ་འདིར་གཅིག་པ་ཉིད་མ་ཡིན་པའི་སྐྱོན་ནས་གཞན་ཡང་རུང་བ་ཡོད་པར་གྱུར་ན་འདོད་པ་ནི་མ་ཡིན་ཏེ། འོན་ཀྱང་གདོན་མི་ཟ་བར་ཡང་འཇུག་པར་བྱའོ། །

[Block 4283]
འདུ་བ༌[^2966]མཐུན་པ་དག་ལ༌[^2967]ཡང་ངོ་ཞེས་བྱ་བ་ནི། གཉུག་མར་གནས་པ་རྣམས་ནི་བྱས་པ་དང་ལྡན་པའི་གཉུག་མར་གནས་པ་རྣམས་དང་འདུ་བ་མཐུན་པ༌[^2968]ཡིན་ལ། གློ་བུར་དུ་ལྷགས་པ་རྣམས་ཀྱང་གཉུག་མར་གནས་པ་རྣམས་དང་མཐུན་པ་ཡིན་སྙམ་དུ་རྟོགས་པར༌[^2969]བྱའོ། །

[Block 4284]
འོན་ཀྱང་འདུ་བ་མཐུན་པ་ཡིན་པས། གཉུག་མར་གནས་པ་བྱས་ཟིན་པ་རྣམས་གློ་བུར་དུ་ལྷགས་པ་དག་ལ་ཡང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4285]
གཞན་གྱི༌[^2970]ཚོགས་པ༌[^2971]གསོལ་བར་བྱའོ་ཞེས་བྱ་བ་ལ། གཞན་གྱིས་ཞེས་བྱ་བ་ནི་གང་དག་གི་འདོད་པ་འདི་སྨོས་པ་དེ་དག་ལས་གཞན་པ་གསོལ་བར་བྱའོ། །

[Block 4286]
དེ་མ་ཐོབ༌[^2972]ན་མཚམས་གཞན་དུ་བྱའོ་ཞེས་བྱ་བ་ནི་ཚོགས་པ་དེ་མ་ཐོབ་ན་མི་མཐུན་པ་ཉིད་ཀྱི་ཉེས་པ་སྤང་བའི་ཕྱིར། མཚམས་གཞན་དུ་ལས་བྱེད་པ་ནི་དེ་དག་ཉི༌[^2973]ཚེར་མ་ཟད་ཀྱི་ལས་ཐམས་ཅད་ལ་ཡང་དེ་བཞིན་ནོ། །

[Block 4287]
བྱེད་པའི་ཚེ་འོངས་ན་ལྷག་མ་ཉམས་སུ་མྱོང་བས་འགྲུབ་བོ་ཞེས་བྱ་བ་ནི། དགག་དབྱེ་བྱེད་པར་འགྱུར་བའི་ཚེ་གང་དག་འོངས་པར་གྱུར་ན་དེ་དག་ལ་རང་གི་དགག་དབྱེ་བྱ་སྟེ་གོང་མ་ནི་མ་ཡིན་ནོ། །

[Block 4288]
སྔ་མ་ཉིད་ཉམས་སུ་མྱོང་བར་མ་གྱུར་པ་ཉིད་ཀྱི་ཕྱིར་མ་གྲུབ་པ་སྟེ་འོན་ཀྱང་གྲུབ་པ་ཁོ་ནའོ། །

[Block 4289]
དེ་བཞིན་དུ་གསོ་སྦྱོང་བྱེད་པར་གྱུར་པ་ཉིད་ཀྱི་ཚེ་གང་དག་འོངས་པར་གྱུར་པ་དེ་རྣམས་ལ་དེར་སོ་སོར་ཐར་པ་ལས་གང་ཞིག་ལྷག་མ་མ་བཏོན༌[^2974]པར་གྱུར་པ་དེའི་འཕྲོ་ཉམས་སུ་མྱོང་བས་ཀྱང་གསོ་སྦྱོང་འགྲུབ་བོ། །

[Block 4290]
དེ་བས་ན་དེར་སླར་བྱེད་པ་དོན་མེད་པར་འགྱུར་བའི་ཕྱིར་མི་བྱ་བ་ཉིད་དོ། །

[Block 4291]
དེར་འདི་ལ་མ་གྲུབ་པ་ཇི་ལྟར་ཐོས་པ་ཉན་དུ་བཅུག་པ་ལ་ཡང༌[^2975]ཡིན་ཞེ་ན། གང་གི་ཕྱིར་འདིར་དེ་ལྟ་བུ་ལྷག་མ་ཉམས་སུ་མྱོང་བ་ཐམས་ཅད་སོ་སོར་གནས་པའི་ཚིག་ཡོད་པ་ཡིན་ཏེ། ཚེ་དང་ལྡན་པ་དག་བདག་ལས་སོ་སོར་ཐར་པའི་མདོ་ལས་བསྟན་པའི་གླེང་གཞི་ཡོད་དེ། ཕམ་པར་གྱུར་པ་བཞི་བསྟན་པ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 4292]
གནས་དེ་ནས༌[^2976]འགའ་ཡང་མ་སོང་བ་ཡིན་ན་ངེས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། གསོ་སྦྱོང་དང་དགག་དབྱེ་ཟིན་པའི་གནས་དེ་ནས་གཅིག་ཀྱང་མ་སོང་བ་ཉིད་ཡིན་ན། ཚོགས་པ་མ་བྱིན་པའི་ཕྱིར་ངེས་པ་སྟེ་འདོད་པས་ནི་མ་ཡིན་ནོ། །

[Block 4293]
མི་རིགས་པ་གནས་པ་ཚོགས་པས་རུང་བ་ཉིད་ལ་ཡན་ལག་གི་ངོ་བོ་འཇུག་པར་འགྱུར་བ་རྣམས་ཀྱིས་ཡན་ལག་གི་དངོས་པོས་འགྲོ་བར་མི་འགྱུར་རོ་ཞེས་བྱ་བ་ནི་འདིར་འཇུག༌[^2977]པའི་ངེས་པ་འདི་རྣམ་པར་གཞག་པའོ། །

[Block 4294]
འདིར་འདོད་པས་འཇུག་པ་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4295]
གློ་བུར་དུ་ལྷགས་པ་ཆེས་མང་བ་ཉིད་ཡིན་ན་ཡང་ངོ་ཞེས་བྱ་བ་ནི། གལ་ཏེ་ཕྱིས་འོངས་པ་མང་བར་གྱུར་ན། སོང་བ་ལ་ཡང་གསོ་སྦྱོང་གི་གནས་ནས་འགའ་ཡང་འདིར་ངེས་པས་འཇུག་པ་ལ་ཆེས་མང་བ་ཉིད་ལ༌[^2978]རབ་ཏུ་འབྱུང་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 4296]
དུས་ཀྱི༌[^2979]ཕྱིར་ནི་ཆེས་མང་པོ་རྣམས་ཀྱི་རྗེས་སུ་འཇུག་པར་བྱ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་གཉུག་མར་གནས་པ་རྣམས་ཀྱི་ཚེས་བཅོ་ལྔ་ཡིན་ལ། གློ་བུར་དུ་ལྷགས་པ་རྣམས་ཀྱི་ནི་ཚེས་བཅུ་བཞི་ཡིན་པའམ། བཅུ་དྲུག་ཡིན་པའམ། གློ་བུར་དུ་ལྷགས་པ་རྣམས་ཀྱི་ནི་ཚེས་བཅུ༌[^2980]བཞི་འམ་བཅུ་དྲུག་ཡིན་པ་ལྟ་བུ་དེ་ལ་ནི་དགེ་སློང་གང་མང་ཤོས་ཀྱི་ཕྱོགས་ཀྱི་རྗེས་སུ་འབྲང་བར་བྱའོ། །

[Block 4297]
ཇི་སྟེ་ཕྱོགས་གཉིས་ཀ་གྲངས་མཉམ་པ་ཁོ་ན་ཡིན་ན་གཅིག་པ་ཡང་དགེ་སློང་དེ་སྙེད་པ་ཉིད་དེ་གཞན་ལ་ཡང་དེ་སྙེད་པ་ཉིད་དོ། །

[Block 4298]
གཉུག་མར་གནས་པའི་ཕྱོགས་སུ་གློ་བུར་དུ་འོངས་པའི་ཕྱོགས་ཀྱི༌[^2981]རྗེས་སུ་འཇུག་པར་བྱ་བ་ཉིད་ཡིན་ནོ། །

[Block 4299]
ཇི་སྐད་དུ་གསུངས་པ་མཉམ་པ་ཉིད་ཡིན་ན་གཉུག་མར་གནས་པ་རྣམས་ཀྱང་ངོ་ཞེས་བྱ་བའོ། །

[Block 4300]
དེར་རྗེས་སུ་འཇུག་པར་བྱ་བ་ཉིད་དུ༌[^2982]རུང་བ་ཡིན་ཏེ། ཕྱིས་འོངས་པ་རྣམས༌[^2983]ཀྱི་དོན་དུ་ཞེས་བྱ་བ་ཡང་བྱེད་པ་རུང་བ་ཉིད་བརྗོད་པ་ཡིན་ཏེ། འཇུག་པ་ལ་ནི་འདིར་འདོད་པ་ཐོབ་པ༌[^2984]དེ་འདིར་དུས་ཀྱི་སྐབས་སུ་དམིགས་ཀྱིས་བསལ་བ་དེ་བསྟན་པའི་ཕྱིར་འདི་ལ་ཡང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་ཡང་རྗེས་སུ་འཇུག་པར་བྱ་བ་ཉིད་ལ་ངེས་པ་སྟེ། འདིར་འཇུག་པ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4301]
གསོ་སྦྱོང་གི་ཆོ་གའི་སྐབས་སོ། །

[Block 4302]
ཏིང་ངེ་འཛིན་ལས་བསླང་བར་མི་བྱའོ་ཞེས་བྱ་བར་འདིར་རྣམ་པར་འབྱེད་པ་དང་མདོ་ཕྱི་མའི་ཡང་གཞུང་ངོ་། །གདམས་ངག་མེད་པར་བསྒོམ་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་གདམས་ངག་སྟོན་པ་པོ་མེད་པར་བསྒོམ་པར་མི་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4303]
གདོས་བུ་དང་ཕོ་ལོང་གི་སྦྱོར་བ་རིགས་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། རྩ་བའི་གཞི་ལས་འདིའི་ཚིག་གང་ཡིན་པ་དེ་ནི་ངན་པར་འགྲོ་བར་གྱུར་པ་འདི་ཡོད་པ་དང་། རྩེ་བར་གྱུར་པ་ལ་ཡང་མ་ཡིན་ཞེས་རྟོགས་པར་མི་བྱའོ་ཞེས་བྱ་བ་འདི་བསྟན་པའི་དོན་དུ་མདོ་འདིའོ། །

[Block 4304]
འདིར་གཞུང་ནི།

[Block 4305]
ཕྲན་ཚེགས་ཀྱི་མདོ་ཕྱི་མ་དག་ལས།

[Block 4306]
དགེ་སློང་དག་དེ་ལྟ་བས་ན་ཇི་ལྟར་ཆུ་ཀླུང་ཡིད་འོང་ལྡན་གྱི་ངོགས་ཀྱི་དགེ་སློང་དག་གིས༌[^2985]བརྩོན་འགྲུས་བརྩམས་པ་དེ་ལྟར་གདོས་བུ་དང་ཕོ་ལོང་གི་སྦྱོར་བས་བརྩོན་འགྲུས་བརྩམ་པར༌[^2986]བྱའོ་ཞེས་བྱ་བ་ཕྱི་མ་ལས་ཀྱང་དགེ་སློང་གིས་བརྩོན་འགྲུས་གློད་པར་མི་བྱའོ། །

[Block 4307]
བརྩོན་འགྲུས་གློད༌[^2987]པར་བྱེད་ན་འགལ་ཚབས་ཅན་དུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4308]
གང་དུ་འདི་ལས་འོག༌[^2988]ཏུ་གཞུང༌[^2989]མ་བཤད་པ་དེར་ཡང་གཞུང་འདི་ཕྲན་ཚེགས་དག་ལས་རིག་པར་བྱའོ། །

[Block 4309]
བརྩོན་འགྲུས་གློད་པར༌[^2990]མི་བྱའོ། །

[Block 4310]
འདི་ནི་མདོ་འདི༌[^2991]ལས་གསུངས་པ་བཞིན་ནོ་ཞེས་བྱ་བ་ནི་འདིར་དགེ་སློང་ཉིན་མོ་འདུག་པ༌[^2992]དང་འཆག་པ་དག་གིས་སྒྲིབ་པར་འགྱུར་བའི་ཆོས་རྣམས་ལས་སེམས་ཡོངས་སུ་སྦྱོང་བར་བྱེད་ཅིང་མཚན་མོའི་ཐུན་དང་པོ་ལ་འདུག་པ་དང་འཆག་པ་དག་གིས་སྒྲིབ་པར་འགྱུར་བའི་ཆོས་རྣམས་ལས་སེམས་ཡོངས་སུ་སྦྱོང་བར་བྱེད་ཅིང་ནམ་གྱི་གུང་ཐུན་ལ་གཙུག་ལག་ཁང་གི་ཕྱི་རོལ་དུ་རྐང་པ་བཀྲུས་ནས་གཙུག་ལག་ཁང་དུ་ཞུགས་ཏེ། གློ་གཡས་པ་ཕབ་སྟེ་རྐང་པ་རྐང་པའི་སྟེང་དུ་བཞག་ནས་སྣང་བའི་འདུ་ཤེས་དང་ལྡན་པས་དྲན་པ་དང་ཤེས་བཞིན་དང་ལྡན་པས་དབུགས་དབྱུང་བ་མ་ཡིན་པའི་འདུ་ཤེས་སུ་བྱེད་ཅིང་། དེ་མཚན་མོའི་ཐུན་ཐ་མ་ལ་མྱུར་བ་མྱུར་བར་རབ་ཏུ་སད་ནས་འདུག་པ་དང་། འཆག་པ་དག་གིས་སྒྲིབ་པར་འགྱུར་བའི་ཆོས་རྣམས་ལས་སེམས་ཡོངས་སུ་སྦྱོང་བར་བྱེད་ཅིང་། དེ་ཙམ་གྱིས་དགེ་སློང་བརྩོན་འགྲུས་བརྩམས་པར་འགྱུར་རོ། །
--- END BLOCKS ---
