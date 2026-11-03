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
[Block 3256]
དེ་བས་ན་འདིར་གཞན་ལ་བསྔགས་པ་ལ་སོགས་པ་ལྷག་པར༌[^2111]སྤྱོད་པའི་གཉེན་པོར་གྱུར་པ་ན་ལུས་ངག་ལ་སེར་སྣའི་དབང་གིས༌[^2112]བསྔགས་པ་ལ་སོགས་པའི་གེགས་སུ་གྱུར་པ་ཉིད་ཀྱིས༌[^2113]བསྔགས་པ་ལ་སོགས་པའི་སེར་སྣའི་སྒྲ་སྨོས་པ་ཡིན་གྱི་སེར་སྣའི་དྲི་མ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 3257]
འདིར་ནི་བསྒྲུབ་པ་བསྔགས་པ་ལ་སོགས་པ་ལ་སེར་སྣ་བྱེད་པ་ལ་ཡིན་གྱི་སེམས་ཀྱི་དྲི་མ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 3258]
དེ་ལྟར་ཡང་འདིར་གླེང་གཞི་ལས་སྦོམ་དགའ་མོས་དགེ་སློང་མ་གཞན་དག་གིས་ཡོན་ཏན་ཡང་དག་པར་བརྗོད་པ་ཐོས་པ་དང་སྨོད་པར༌[^2114]བྱེད་དེ། དེ་ལ་དགེ་སློང་མ་རྣམས་ཀྱིས་འཕགས་མ༌[^2115]ཅིའི་ཕྱིར་སྨོད་པར་བྱེད་ཅེས་སྨྲས་པ་དང་། སྦོམ་དགའ་མོས་སྨྲས་པ། བདག་ནི་ཤཱཀྱའི་རིགས་སུ་སྐྱེས་པས་སྡེ་སྣོད་གསུམ་གྱི་ཆོས་སྨྲ་བར་རིགས་པ་དང་། གྲོལ་བའི་སྤོབས་པ་དང་ལྡན་པ་ཁོ་མོའི་བསྔགས་པ་མི་བརྗོད་པར་གཞན་དག་གི་བསྔགས་པ་བརྗོད་དམ་ཞེས་བྱ་བ་དང་། སྦོམ་དགའ་མོས་དགེ་སློང་མ་གཞན་དག་ལ་ཁྱེད་ཀྱིས་གང་ན་བསོད་སྙོམས་བསོད་པ་རྙེད་ཅེས་དྲིས་པ་དང་། དགེ་སློང་མ་རྣམས་ཀྱིས་ཐམས་ཅད་སྨྲས་པ་དང་། དེ་ནས་སྦོམ་དགའ་མོ་སྨོད་ཅིང་དེ་དག་ཟློག༌[^2116]པར་བྱེད་དོ།[^2117] །ཁྱིམ་ག་གེ་མོ་ཞིག་ཏུ་ཁྱེད་ཅག་མ་འགྲོ་ཤིག༌[^2118]ཅེས་བྱ་བའི་བར་དང་། སྦོམ་དགའ་མོས་དེ་དགེ་སློང་མའི་དབྱར་ཁང་བྱེད་དུ་བཅུག་ནས། དེ་ན་དགེ་སློང་མ་རྣམས༌[^2119]གནས་ཤིང་ས་གཉིས་པ་གཞན་ལ་སྦོམ་དགའ་མོ་གནས་ཏེ། དེ་རྣམས་དེས་བག་ཡངས་སུ་རྐང་པ་དག་གིས་འཆག་ཅིང་སྤྱོད་པའི་སྒྲ་ཆེན་པོ་དག་གིས་གྲག་པར་གྱུར༌[^2120]ནས། སྦོམ་དགའ་མོ་དེ་རྣམས་ལ་སྨོད་ཅིང་འདི་ལྟར་རྣམ་པར་འགྱུར་བར་བྱེད་དོ། །

[Block 3259]
རྣམ་པར་འགྱུར་བ་དག་གིས་སྒེག་པ་དང་བཅས་པས་འཆག་པ༌[^2121]དེ་རྣམས་སུ་ཡིན་ཞེས་ཟེར་ནས། ཇི་ལྟར་བ་ལང་མོ་རྣམས་འཆག་པར༌[^2122]བྱེད་པ་ལྟར་མ་བསྡམས་པའི༌[^2123]སྒྲ་གང་གི་ཕྱིར་བྱུང་བར༌[^2124]གྱུར་ཏོ། །

[Block 3260]
དགེ་སློང་མ་རྣམས་ཀྱིས་འཕགས་མ་ཁྱོད་གནས་ལ་སེར་སྣ་བྱེད་དམ་ཞེས་སྨྲས་པ། ཅིའི་ཕྱིར་ཁོ་མོ་མི་བྱེད་བདག་གིས་བླངས་ཤིང་གཙུག་ལག་ཁང་བྱེད་དུ་བཅུག་སྟེ་ཆོས་བསྟན་པས་ལྕེ་ལ་ཆུ་བུར་བྱུང་བྱུང་གི་བར་དུ་བསྒྲུབས་པ་ཡིན་ནོ། །

[Block 3261]
བདག་གིས་སའི་ལས་བྱས་པས་རྐང་པ་བརྡོལ༌[^2125]ཞིང་ལག་པ་གཉིས་ལ་ཆུ་བུར་བསྐྱེད་པ་དེའི་ཕྱིར་བདག་སེར་སྣ་བྱེད་དོ། །

[Block 3262]
སྦོམ་དགའ་མོ་འདི་སྙམ་དུ་དགེ་སློང་མ་འདི་རྣམས་སྔ་མར་བསོད་སྙོམས་ལ་རབ་ཏུ་འཇུག་པས། ཁོ་མོས༌[^2126]རྙེད་པ་གང་ལ༌[^2127]ཐོབ་སྙམ་ནས།[^2128] ད་ཐབས་ཅུང་ཟད་བྱས་ཏེ། གང་གིས་བདག་ཁོ་ན་སྔར་ཞུགས་ལ་ཕྱིས་འདི་རྣམས་འཇུག་གོ་སྙམ་ནས། དེས་དེ་རྣམས་གདམས་ངག་དང་རྗེས་སུ་བསྟན་པ་སྟེར་བར་བྱེད་དེ་ཁྱེད་ཅག་ནི༌[^2129]ཟས་ཙམ་ལ་རྩེ་གཅིག་པ་ཟས་དང་འབྲེལ་པའི་སེམས་ཀྱིས་མཚན་མོ་འདའ་བར་བྱེད་དོ་ཞེས་ཟེར་ཞིང་། ཁྱེད་ཅག་རྣམས་ནི་མཁན་མོ་མ་ཡིན་ཏེ། ཉེ་གནས་དང་བསྙེན་བཀུར་གྱིས་ཤིག །ཁྱེད་ཅག་རྣམས་ནི་བཅོམ་ལྡན་འདས་ལ་མཎྜལ་དང་བསྟོད་པ་སྨྲ་བར་མི་བྱེད་དེ། གཅིག་པུ་ལྟུང་བྱེད་དེ་བླངས་ནས་སྔ་བར་བསོད་སྙོམས་ལ་རབ་ཏུ་ཞུགས་སོ་ཞེས་བྱ་བ་དང་། དེ་རྣམས་ཀྱི་བསམས་པ་འཕགས་མ༌[^2130]དེ་བཞིན་དུ་རིགས་སོ་ཞེས་ཟེར་ཏེ། དེ་རྣམས་འགྲོ་བར་མ་བརྩམས་པ་དང་། སྦོམ་དགའ་མོས་ཀྱང་སྐྱ་རེངས་ཤར་བའི་དུས་ཀྱི་ཚེ་བསོད་སྙོམས་ལ་ཞུགས་པ་ན། བྲམ་ཟེ་གཞན་དག་བཀྲ་ཤིས་དོན་དུ་གཉེར་བ་ཡུལ་གཞན་དུ་འགྲོ་བར་འདོད་པས་ཁྱིམ་ནས་བྱུང་བ་དང་། དེས་དེ་མཐོང་ནས་མགོ་རེག་མཐོང་ན་བཀྲ་མི༌[^2131]ཤིས་སོ་ཞེས་ཟེར་ཏེ། བཟུང་ནས་ཤིན་ཏུ་བརྡེགས་སོ་ཞེས་བྱ་བའི་བར་དང་། སྦོམ་དགའ་མོ་ལ་དགེ་སློང་མ་རྣམས་ཀྱིས་འཕགས་མས་བདག་ཅག་རྣམས་ལ་ལུང་དབོག་པར་འཚལ་ན། གལ་ཏེ་ཁྱེད་ཀྱིས་བདག་ཅག་ལ་གནང་བ་སྟེར་ན་ལུང་དབོག་ཏུ་གསོལ་ཞེས་གསོལ་བ་བཏབ་པ་དང་། དེས༌[^2132]ཐོས་ནས་ལུང་དབོག་པའི་དུས་དགེ་སློང་མ་དེ་རྣམས་འོངས་པ་དང་། དེས་ཁོ་མོ་རོ་རྒྱབ་ནས༌[^2133]ཤས་དུགས་གྱིས་ཤིག་ཅེས་ལས་བྱེད་དུ་འཇུག་པ་དང་། དེ་རྣམས་བྱེད་ཅིང་བདག་གི་གོས་རྣམས་དྲི་མ་ཅན་དུ་གྱུར་པས་ན། འཚེད་པའི་ལས་གྱིས་ཤིག་ཆུ་ལོང་ཅིག༌[^2134]ཅེས་བྱ་བ་ལ་སོགས་པ་འདི་ལྟར་བྱ་བ་མཐའ་ཡས་པ་ཡིན་ཏེ། དེ་རྣམས་ཀྱིས་འདི་ལྟར་བསམས་ཏེ། འཕགས་མ༌[^2135]ནི་ངེས་པར་ཆོས་ལ་སེར་སྣ་བྱེད་དོ་སྙམ་ནས་དེ་དག་གིས་དྲིས་པ། གཅིག་པུ་ཁོ་མོ་ཅག་ལ་ལས་བྱེད་དུ་བཅུག་སྟེ་གང་གིས་ཁོ་མོ་ཅག་ལ་གནང་བར་མི་བྱེད་དེ། དེས་སྨྲས་པ། ཁོ་མོ་ཅིའི་ཕྱིར་མི་བྱེད་ཅེས་བྱ་བའི་བར་དུའོ། །

[Block 3263]
སེར་སྣ་བྱེད་པ་ལས་གྱུར་པའི་ལྟུང་བྱེད།།[^2136] །།

[Block 3264]
ད་འདི་མན་ཆད་ནི་སྐྲོད་པ་ལས་གྱུར་པའི་ལྟུང་བྱེད་གཉིས་བསྟན༌[^2137]ཏེ། དེ་གཉིས་ཀྱི་དང་པོ་ནི་དབྱར་ཁང་ནས་དགེ་སློང་མ་གང་ཡང་རུང་བས་སྐྲོད་པ༌[^2138]ལའོ་ཞེས་བྱ་བ་སྟེ། གང་ཡང་རུང་བས་ཞེས་བྱ་བ་ནི་གཅིག་ཉིད་ལ་གཞན་གྱི༌[^2139]ངེས་པ༌[^2140]རྣམས་སོ། །

[Block 3265]
བཀྲུ་བའི་དོན་དུ་རང་གི་ལུས་སམ་ངག་གིས་གཞན་ལ་བཅོལ་བའམ། སྤྲིང་ཡིག་ལ་སོགས་པའི་རྣམ་པ་གང་ཡང་རུང་བས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3266]
འདིར་སྦོམ་དགའ་མོས་དགེ་སློང་མ་སྔ་ནས་འཁོད་པ་དག་རྐང་པ་དང་། ལག་པ་དག་གིས་མནན་པ་དང་། དེ་དག་གིས་སྨྲས་པ། འཕགས་མ་ཅིའི་ཕྱིར་གནོད་པ་བྱེད། དེས་སྨྲས་པ། སུ་ལ་གནོད་པ་དེ་དག་འགྲོ་ལ་རག་གོ། །

[Block 3267]
དེ་རྣམས་ཀྱིས་ཕན་ཚུན་སྨྲས་པ། སྦོམ་དགའ་མོ་ནི་སྟོབས་དང་ལྡན་པ་སྟེ། དུས་ནམ་གྱི་ཚེ་བདག་ཅག་ལ་རྒྱབ་ཏུ་རྐང་པའི་རྡོག་པ་དང་། ལག་པ་རྣམས་ཀྱིས་སྲོག་དང་འབྲལ་བ་འོང་ངོ་སྙམ་ནས་སྟན་ལས་ལངས་ཤིང་བདག་ཅག་རྣམས་འགྲོ་བར་བྱའོ་ཞེས་ཟེར་ཏེ། དེ་ལྟར་དགེ་སློང་མ་རྣམས་ཐམས་ཅད་དོང་བ་ལས་བཅས་པ་ཡིན་ཏེ། ཕྱི་མའི་གླེང་གཞི་གང་ཡིན་པ་དེ་འདིར་ཡང་སྦྱར་བར་རིག་པར་བྱའོ། །

[Block 3268]
བུད་མེད་རྣམས་ལ་འཇུག་པ་འདི་ནི་ཤིན་ཏུ་སྟོབས་དང་ལྡན་པ་མི་མཐུན་པ་ཞེས་བྱ་བ་འདིར་འདི་ཤེས་པའོ། །

[Block 3269]
ལྷག་མ་ནི་དགེ་སློང་སྐྲོད་པའི་ལྟུང་བྱེད་དང་འབྲེལ་པ་དེར་གཏོགས་པ་ཐམས་ཅད་འདིར་ཤེས་པར་བྱའོ། །

[Block 3270]
གང་དུ་གཉིས་པ་དེ་བརྗོད་པར་བྱ་སྟེ། དེའི་ཕྱིར་ཁྱིམ་གཞན་ནས་དགེ་སློང་མ་སྔ་ན་གནས་པ་སྐྲོད་པ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲས་ནི་དགེ་སློང་མ་གང་ཡང་རུང་བས་སྐྲོད་པ་ལའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 3271]
སྐྲོད་པ་ལས་གྱུར་པའི་ལྟུང་བྱེད་གཉིས་སོ།། །།

[Block 3272]
གང་ལ་ཆོས་ལ་རྨོངས་པས་ཐོ་འཚམས༌[^2141]པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་ལེགས་པར་མ་མཐོང་བ་ལ་སོགས་པས་གླེང་བ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་སློང་མ་ལའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 3273]
སོགས་པ་ཞེས་བྱ་བའི་སྒྲས་ནི། ལེགས་པར་མ་ཐོས་པ་དང་ལེགས་པར་མི་དོགས་པ༌[^2142]གཉིས་སུ་བསྡུའོ། །

[Block 3274]
གཞི་ལེགས་པ༌[^2143]མེད་པ་ལས་གཞི་མེད་པ༌[^2144]ཉིད་ཆེས་སྡིག་ཆེ་བས་དེའི་ཕྱིར་འདིར་ཡང་ཁ་ན་མ་ཐོ་བ་འདིའོ། །

[Block 3275]
ཕམ་པར་འགྱུར་བ་དང་དགེ་འདུན་ལྷག་མ་གཉིས་གླེང་བ་སྔར་བསྟན་ཟིན་པའི་ཕྱིར་ལྷག་མས་གླེང་བ་ཡིན་ནོ། །

[Block 3276]
དྲན་པར་བྱ་བ་ཡང་གླེང་བའི་རྣམ་པ་ཡིན་པས། དེ་བས་ན་འདིར་ཡང་གླེང་བ་དང་འབྲེལ་པ་འདི་ལ་ཐ་དད་པར་རྩོམ་པ་ཉིད་མེད་པས་ལྷག་མ་འདི་ནི་འདིའི་ཡུལ་ལོ། །

[Block 3277]
གླེང་བ་ལས་གདམས་ངག་ལ་སོགས་པ་འཇོག་པ་དང་། གྱོད་ལ་བཏགས་པ་ཆེས་སྡིག་ཆེ་བས་དེ་བས་ན་གཉིས་པོ་འདི་དག་ཀྱང་གཞི་ལེགས་པ་མེད་པ་དང་གཞི་མེད་པ་དག་ལ་འདིའོ། །

[Block 3278]
འདིར་གླེང་གཞི་ནི། དེ་དག་གིས་ལེགས་པར་མ་མཐོང་བ་དང་། ལེགས་པར་མི་ཐོས་པ་དང་། ལེགས་པར་མི་དོགས་པས་དགེ་སློང་མ་ལ་གླེང་བར་བྱེད་པ་དང་དྲན་དུ་བཅུག་པའོ། །

[Block 3279]
དགེ་སློང་མ་ཆེ་གེ་མོ་ཞིག་འདི་འདྲའོ་ཞེས་གླེང་བར་བྱེད་ཅིང་དེ་རྣམས་ལ་གསོ་སྦྱོང་དང་དགག་དབྱེ་འཇོག་པར་བྱེད་པ་དང་། དེ་བཞིན་དུ་གཞི་མེད་པར་བརྫུན༌[^2145]གྱིས་དགེ་སློང་མ་རྣམས་ལ་གླེང་གཞི་མི་མཐུན་པར་གནས་པར་བྱེད་ཅེས་བྱའོ། །

[Block 3280]
དེ་བཞིན་དུ་འདིར་རང་ལ་ཡང་ཁ་ན་མ་ཐོ་བ་རྣམས་ལ་མཚོན་པ་ཉིད་ཀྱིས་འདིར་གླེང་གཞི་མི་མཐུན་པར་གནས་པར་བྱེད་དོ་ཞེས་བྱ་བ་འདི་ལས་ཤེས་པར་རོ། །

[Block 3281]
ཐོ་འཚམས༌[^2146]པ་ལས་གྱུར་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 3282]
གང་ལ་རབ་ཏུ་བྱུང་བའི་བསམ་པ་ལོག་པར༌[^2147]སྟོན་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་མནའ་དོར་བ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རབ་ཏུ་བྱུང་བ་རྣམས་ཀྱི༌[^2148]བསམ་པ་ནི་བདེན་པས་འཇུག་པ་ཡིན་ན། དེ་མནས་ལོག་པར་སྟོན་པ་སྟེ། ཁོ་མོ་ཐམས་ཅད་བདེན་པས་འཇུག་པ་མ་ཡིན་གྱི། འདི་ལྟར་གང་ལ་མནའ་དོར་བར་འཇུག་པ་དེ་གཅིག་པུ་བདེན་ནོ་ཞེས་བྱ་བར༌[^2149]གྱུར་པས་སོ། །

[Block 3283]
གཞན་གྱི་མདུན་མ་ཡིན་པར་མནའ་དོར་བ་ནི་ཚིག་ཀྱལ་པ༌[^2150]ཙམ་དུ་ཟད་པས། སྔ་མའི་རྗེས་སུ་འབྲང་བས་ན་འདི་ཉེས་བྱས་སུ་ཤེས་པར་བྱེད་པའོ། །

[Block 3284]
འདི་ལ་ཤེས་པ་གཞན་ལ་དངོས་གཞི་འབྱུང་བའོ། །

[Block 3285]
རྗེས་སུ་སྤྲོ་བ་ལ་ནི་ཉེས་བྱས་སོ། །

[Block 3286]
གཞན་ཉེ་བར་གནས་པ་ནི་ཚིག་ཀྱལ་པ༌[^2151]ཙམ་དུ་རིག་པར་བྱའོ། །

[Block 3287]
ལོག་པར་སྟོན་པའི་ལྟུང་བྱེད་དོ། །

[Block 3288]
གང་ལ་མི་བརྟན་པས་རྣམ་པར་འགྱུར་བའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་ཁྲོ་བས་བདག་ཉིད་ལ་གནོད་པར་བྱེད་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གནོད་པ་བྱེད་པའི་སྒྲ་ནི་རྡེག་པ༌[^2152]ལའོ། །

[Block 3289]
བདག་ཉིད་ལ་གནོད་པར་བྱེད་ཅེས་བྱ་བའི་རྣམ་པར་འབྱེད་པ་ནི་རྡེག་པར༌[^2153]བྱེད་པའོ་ཞེས༌[^2154]གསུངས་པ་ཡིན་ནོ། །

[Block 3290]
མི་བརྟན་པས་རྣམ་པར་འགྱུར་བ་ཞེས་བྱ་བ་འདི་ནི་འདི་ཡིན་ཏེ། དེ་བས་ན་མི་བརྟན་པ་རྣམ་པར་འགྱུར་བ་ཉིད་ཀྱིས་འདི་བརྗོད་པའོ། །

[Block 3291]
མི་བརྟན་པས༌[^2155]རྣམ་པར་འགྱུར་བའི་ལྟུང་བྱེད་དོ།། །།

[Block 3292]
ད་འདི་མན་ཆད་ནི་བླ་མར་གྱུར་པ་ལ་བརྙས་ཐབས་བྱེད་པའི་ལྟུང་བྱེད་གསུམ་སྟོན་ཏེ། དེ་རྣམས་ཀྱི་དང་པོ་ནི་དགེ་སློང་མའི་ཚོགས་པ༌[^2156]ལ་བརྙས་ཐབས་བྱེད་པ་ལའོ། །

[Block 3293]
ཚོགས་ཀྱི་སྒྲ་ནི་དགེ་འདུན་འདི་དང་འོག་མ་ལའོ། །

[Block 3294]
དགེ་སློང་མའི་ཚོགས་ཞེས་བྱ་བའི་རྣམ་པར་འབྱེད་པ་ནི་དགེ་སློང་མའི་དགེ་འདུན་ཞེས༌[^2157]གསུངས་པ་ཡིན་ནོ། །

[Block 3295]
གསུམ་མམ་གཉིས་སམ་གཅིག་པོ་རྣམས་ཀྱི་རྗེས་སུ་འབྲངས་པས་ཉེས་བྱས་སུ་རིག་པར་བྱའོ། །
--- END BLOCKS ---
