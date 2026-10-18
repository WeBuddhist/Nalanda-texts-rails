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
[Block 4026]
འོན་ཏེ༌[^2274]བཟོད་ན་ནི་སངས་རྒྱས་རྣམས་འཇིག་རྟེན་དུ་འབྱུང་བ་ནི་བསོད་ནམས་ཀྱི་གཞི་ཡིན་པས་འདི་ཡང་ཅིའི་ཕྱིར་མི་བཟོད་དེ། གལ་ཏེ་མང་པོ༌[^2275]ཞིག་ཏུ་ཕལ་པོ་ཆེ་ཞིག་འབྱུང་བར༌[^2276]གྱུར་ན་ཡང་སྐྱོན་དུ་མི་འགྱུར་གྱི་འཇིག་རྟེན་ཕལ་ཆེར་མངོན་པར་མཐོ་བ་དང་ངེས་པར་ལེགས་པ་དང་ལྡན་པར་འགྱུར་རོ། །

[Block 4027]
འོན་ཏེ་གཅིག་ཏུ་ཡང་དེ་བཞིན་གཤེགས་པ་གཉིས་ཅིའི་ཕྱིར་འབྱུང་བར་མི་འགྱུར་ཞེ་ན། དགོས་པ་མེད་པའི་ཕྱིར་དང་། སྨོན་ལམ་གྱི་དབང་གིས་ཏེ། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ནི་འདི་སྐད་དུ་ཀྱེ་མ་བདག་ནི་འདྲེན་པ་མེད་པ་ལྡོངས་པའི་འཇིག་རྟེན་དུ་མགོན་མེད་པ་རྣམས་ཀྱི་མགོན་དུ་སངས་རྒྱས་སུ་འབྱུང་བར་གྱུར་ཅིག་ཅེས་སྨོན་ལམ་འདེབས་པར་བྱེད་དོ། །

[Block 4028]
གུས་པ་དང་རིངས་པར་བྱ་བའི་ཡང་ཕྱིར་རོ་ཞེས་ཟེར་རོ། །

[Block 4029]
[^2277]སངས་རྒྱས་གཅིག་ལ་ནི་ཤིན་ཏུ་ཡང་གུས་པར་འགྱུར་ལ། འདི་ལྟ་བུ་གཞན་ལ༌[^2278]ནི་རྙེད་པར་དཀའོ་སྙམ་དུ་སེམས་པ་ནི་འདི་གཤེགས་སམ་ཡོངས་སུ་མྱ་ངན་ལས་འདས་ན་མགོན་མེད་པར་འགྱུར་དུ་འོང་ངོ་ཞེས་བསྟན་པ་བསྒྲུབ་པ༌[^2279]ལ་ཤིན་ཏུ་རིངས་པར་ཡང་བྱེད་དོ། །

[Block 4030]
ཡང་འཁོར་ལོས་སྒྱུར་བའི་རྒྱལ་པོ་དེ་དག་གསེར་ལ་སོགས་པའི་འཁོར་ལོ་དག་གིས་ས་ལས་རྒྱལ་བར་བྱེད་པ་ན་ཇི་ལྟར་རྒྱལ་བར་བྱེད་ཅེ་ན། གོ་རིམས་བཞིན་དུ། ཕས་བསུ་རང་འགྲོ་གཡུལ་བཤམས་དང་། །མཚོན་བརྩམས་པས་རྒྱལ། གང་ལ་གསེར་གྱི་འཁོར་ལོ་ཡོད་པ་དེ་ལ་ནི་ཁམས་ཀྱི་རྒྱལ་ཕྲན་རྣམས་འབྱོར་པ་དང་། རྒྱས་པ་དང་། བདེ་བ་དང་། [^2280]གང་ལོ་ལེགས་པ་དང་། སྐྱེ་བོ་དང་། མི་ཕལ་པོ་ཆེས་བལྟམས༌[^2281]པའི་ལྗོངས་འདི་དག་ནི་ལྷའི་ལགས་ཀྱི་ལྷས་དེ་དག་རྗེས་སུ་བསྟན་དུ་གསོལ། བདག་ཅག་ནི་ལྷའི་ཞམ་འབྲིང་འཚལ་ལོ་ཞེས་ཕས་བསུ་བར་བྱེད་དོ། །

[Block 4031]
གང་ལ་དངུལ་གྱི་འཁོར་ལོ་ཡོད་པ་དེ་ལ་ནི་བདག་ཉིད་དེ་དག་གི་ཐད་དུ་འགྲོ་སྟེ། ཕྱིས་འདུད་པར་འགྱུར་རོ། །

[Block 4032]
གང་ལ་ཟངས་ཀྱི་འཁོར་ལོ་ཡོད་པ་དེ་ནི་དེ་དག་གི་ཐད་དུ་སོང་ནས་གཡུལ་ཤོམ༌[^2282]པར་བྱེད་དེ། ཕྱིས་འདུད་པར་འགྱུར་རོ། །

[Block 4033]
གང་ལ་ལྕགས་ཀྱི་འཁོར་ལོ་ཡོད་པ་དེ་ནི་དེ་དག་གི་ཐད་དུ་སོང་ནས་ཕན་ཚུན་མཚོན་བརྩམས་པ་ལས་ཕྱིས་འདུད་པར་བྱེད་དོ། །

[Block 4034]
འཁོར་ལོས་སྒྱུར་བ་ཐམས་ཅད་ཀྱང་། གནོད་པ་མེད། མཚོན་ཆས་རྒྱལ་ཡང་གསོད་དུ་མི་འཇུག་གོ། །

[Block 4035]
རྒྱལ་ནས་ཡང་སེམས་ཅན་རྣམས་དགེ་བ་བཅུའི་ལས་ཀྱི་ལམ་དག་ལ་འཇོག་པར་བྱེད་དོ། །

[Block 4036]
དེ་གཉིས༌[^2283]ཀྱི་ཕྱིར་དེ་དག་ནི་ངེས་པར་ལྷ་རྣམས་ཀྱི་ནང་དུ་སྐྱེ་བར་འགྱུར་རོ། །

[Block 4037]
མདོ་ལས།

[Block 4038]
འཁོར་ལོས་སྒྱུར་བའི་རྒྱལ་པོ་དེ༌[^2284]དག་འཇིག་རྟེན་དུ་བྱུང་བས་འཇིག་རྟེན་དུ་རིན་པོ་ཆེ་སྣ་བདུན་པོ་འདི་ལྟ་སྟེ། འཁོར་ལོ་རིན་པོ་ཆེ་དང་། གླང་པོ་རིན་པོ་ཆེ༌[^2285]དང་། རྟ་རིན་པོ་ཆེ་དང་། ནོར་བུ་རིན་པོ་ཆེ་དང་། བུད་མེད་རིན་པོ་ཆེ་དང་། ཁྱིམ་བདག་རིན་པོ་ཆེ་དང་། བློན་པོ་རིན་པོ་ཆེ་འབྱུང་བར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཇི་ལྟར་ན་སེམས་ཅན་ཞེས་བྱ་བ་གླང་པོ་ཆེ་ལ་སོགས་པ་གཞན་གྱི་ལས་ཀྱིས་འབྱུང་ཞེ་ན། གཞན་གྱི་ལས་ཁོ་ནས་འབྱུང་བ་ནི་མ་ཡིན་གྱི། སེམས་ཅན་གང་དག་གིས་དེ་དང་འབྲེལ་པར་འགྱུར་བའི་ལས་བརྩམས་པ༌[^2286]དེ་ནི་དེ་བྱུང༌[^2287]ན་རང་གི་ལས་དེ༌[^2288]དག་ཁོ་ནས༌[^2289]སྐྱེད་པར་བྱེད་དོ། །

[Block 4039]
ཅི་འཁོར་ལོས་སྒྱུར་བ་རྣམས་རྒྱལ་པོ་གཞན་དག་ལས་ཁྱད་པར་དེ་ཁོ་ན་ཡོད་དམ་ཞེ་ན། ཁྱད་པར་གཞན་ཡང་ཡོད་དེ། དེ་དག་ལས་སྐྱེས་བུ་ཆེན་པོའི་མཚན་སུམ་ཅུ་རྩ་གཉིས་ཀྱང་ཡོད་དེ། དཔེར་ན་སངས་རྒྱས་རྣམས་ཀྱི་བཞིན་ནོ། །

[Block 4040]
དེ་ལ།

[Block 4041 [VERSE]]
[^2290] ཐུབ་མཚན་ཡུལ་ན་གནས་པ་དང་། །
གསལ་ལ་རྫོགས་པས་འཕགས་པ་ཡིན། །

[Block 4042]
སངས་རྒྱས་རྣམས་ཀྱི་མཚན་ནི་ཤིན་ཏུ་ཡུལ་ལ་གནས་པ་དང་། ཤིན་ཏུ་གསལ་བ་དང་། ཤིན་ཏུ་ཀུན་རྫོགས་པ་དག་ཡིན་པས་དེ་དག་གི༌[^2291]ཁྱད་པར་ནི་དེ་ཡིན་ནོ། །

[Block 4043 [HEADING]]
##### བསྐལ་པ་དང་པོ་པའི་མི། ^3-2-5-9-0

[Block 4044]
ཡང་ཅི་བསྐལ་པ་དང་པོ་པའི་མི་རྣམས་ཀྱང་རྒྱལ་པོ་དང་བཅས་པར་གྱུར་ཏམ་ཞེ་ན། སྨྲས་པ་མ་ཡིན་ནོ། །

[Block 4045]
འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན། སྔར་བྱུང་སེམས་ཅན་གཟུགས་ཅན་བཞིན། །བསྐལ་པ་དང་པོ་པའི་མི་རྣམས་ནི་གཟུགས་ན་སྤྱོད་པ་བཞིན་དུ་འགྱུར༌[^2292]ཏེ།

[Block 4046]
མདོ་ལས།

[Block 4047]
དེ་དག་ནི་གཟུགས་དང་ལྡན་པ། ཡིད་ལས༌[^2293]བྱུང་བ། ཡན་ལག་དང་ཉིང་ལག་ཐམས་ཅད་དང་ལྡན་པ། དབང་པོ་མ་ཚང་བ་མེད་པ། ངན་པ་མ་ཡིན་པ། མཛེས་པ། ཁ་དོག་ལ་གནས་པ། རང་གི་འོད་ཅན་ནམ་མཁའ་ལ་འགྲོ་ཞིང་། དགའ་བ་ཟ་ཞིང་ཟས་སུ་དགའ་བ་ཟ་བ། ཚེ་རིང་བ། ཡུན་རིང་པོར༌[^2294]གནས་པ་ཡིན་ནོ༌[^2295]ཞེས་གསུངས་སོ། །

[Block 4048 [VERSE]]
དེ་ནས་རིམ་གྱིས་རོ་ལ་ཆགས། །
ལེ་ལོས་གསོག་འཇོག་བྱས་ནས་ནི། །

[Block 4049]
འཛིན་ཆགས༌[^2296]རྣམས་ཀྱིས་ཞིང་དཔོན་བཏབ།[^2297] །དེ་བཞིན་དུ་འབྱུང་བ༌[^2298]དེ་དག་ལས་སའི་རོ་སྦྲང་རྩིའི་རོ་བྲོ་བ་ཞིག་བྱུང་བ་དང་། སེམས་ཅན་བརྐམ་པའི་རང་བཞིན་ཅན་གང་ཡང་རུང་བ་ཞིག་གིས་དེའི་དྲི་བསྣམས༌[^2299]ནས་རོ་མྱངས་ཤིང་ཟོས་སོ། །

[Block 4050]
དེ་ནས་སེམས་ཅན་གཞན་དག་ཀྱང་དེ་བཞིན་དུ་བྱེད་པར་འགྱུར་ཏེ། ཁམ་གྱི་ཟས་ཟ་བའི་རྩོམ་པ་ནི་དེ་ཡིན་ནོ། །

[Block 4051]
དེ་དག་ཟས་དེ་ལ༌[^2300]གོམས་པའི་ཕྱིར་ལུས་ལ་རྩུབ་པ་ཉིད་དང་། ལྕི་བ་ཉིད་ནི་ཞུགས། འོད་ནི་ནུབ་པར་གྱུར་ཏོ། །

[Block 4052]
དེའི་འོག་ཏུ་མུན་པ་འབྱུང་བ༌[^2301]དང་། ཉི་མ་དང་ཟླ་བ་དག་ཀྱང་བྱུང་བར་གྱུར། རོ་ལ་ཆགས་པ་དེ་དག་ལས༌[^2302]སའི་རོ་དེ་ཡང་རིམ་གྱིས་ནུབ་ནས་ས༌[^2303]ཞག་ཅིག་བྱུང་བར་གྱུར་ཏོ། །

[Block 4053]
དེ་ལ་ཡང་ཆགས་པར་གྱུར་པ་དང་། དེ་ཡང་ནུབ་ནས་མྱུག་གུའི་ཚལ་ཞིག་བྱུང་བར་གྱུར་ཏོ། །

[Block 4054]
དེ་ལ་ཡང་ཆགས་པར་གྱུར་པ་དང་དེ་ཡང་ནུབ་ནས་མ་རྨོས༌[^2304]མ་བཏབ་པའི་འབྲས་སཱ་ལུ་ཞིག་བྱུང་བར་གྱུར་ཏོ། །

[Block 4055]
དེའི་ཚེ་དེ་ཟོས་པ་དང་དེ་ནི་ཆེས་རགས་པ་ཡིན་པའི་ཕྱིར་ན༌[^2305]རྒྱུ་མཐུན་པ་འབྱུང་བར་བྱ་བའི་ཕྱིར་སེམས་ཅན་རྣམས་ཀྱི་གཅིན་དང་ཕྱི་སའི་ལམ་དང༌[^2306]ཕོ༌[^2307]མོའི་དབང་པོ་དང་བཅས་པ་དང་། དབྱིབས་ཐ་དད་པ་ཡང་བྱུང་བར་གྱུར་ཏོ། །

[Block 4056]
དེ་དག་ཕན་ཚུན་མཐོང་བ་དང་སྔོན་གོམས་པའི་དབང་གིས་ཚུལ་བཞིན་མ་ཡིན་པ་ཡིད་ལ་བྱེད་པ་ཆུ་སྲིན་འཛིན་ཁྲིའི་ཁམ་དུ་གྱུར་པ་རྣམས་འདོད་པའི་འདོད་ཆགས་ཤས་ཆེར་སྐྱེས་ནས་དེ་ནས་ལོག་པར་ཞུགས་པ་ཡིན་ཏེ། འདོད་པ་ཅན་རྣམས་ཀྱི་འདོད་པའི་འབྱུང་པོའི་གདོན་གྱིས་རློམ་པའི་རྩོམ་པ་ནི་དེ་ཡིན་ནོ། །

[Block 4057]
ཡང་དེ་དག་གི་འབྲས་སཱ་ལུ་དེ་ནང་བཟའ་བར་བྱ་བ་དེ་ནང་ལེན།[^2308]

[Block 4058]
ནུབ་བཟའ་བར་བྱ་བ་ཡང་ནུབ་ལེན༌[^2309]པ་ལས།

[Block 4059]
ཡང་སེམས་ཅན༌[^2310]ལེ་ལོའི་རང་བཞིན་ཅན་གང་ཡང་རུང་བ་ཞིག་གིས་གསོག་འཇོག་བྱས་པ་དང་། སེམས་ཅན་གཞན་དག་ཀྱང་གསོག་འཇོག་བྱེད་པར་གྱུར་ཏོ། །

[Block 4060]
དེ་དག་དེ་ལ་བདག་ཏུ་འཛིན་པ་སྐྱེས་པ་དང་། འབྲས་བུ༌[^2311]དེ་བརྔས་ཤིང་བརྔས་པ་དང་ཡང་མི་སྐྱེ་བར་གྱུར་ཏོ། །

[Block 4061]
དེ་ནས་ཞིང་རྣམས་བགོས་ཏེ་དེ༌[^2312]བདག་གིས༌[^2313]ནི་ཀུན་ཏུ་བཟུང་ནས་གཞན་གྱི་ལ་ནི་དབྲོག་པར་རྩོམ་སྟེ།[^2314] ཆོམ་རྐུན་གྱི་རྩོམ་པ་དང་པོ་ནི་དེ་ཡིན་ནོ། །

[Block 4062]
དེ་དག་གིས་དེ་དག་དགག་པའི་ཕྱིར་འདུས་ནས་མིའི་ཁྱད་པར་གང་ཡང་རུང་བ་ཞིག་ཞིང་རྣམས་སྲུང་བར་དྲུག་ཤས་བསྟབས་ཏེ། དེ་ལ་ཞིང་རྣམས་ཀྱི་དཔོན་པོ༌[^2315]རྒྱལ་རིགས་རྒྱལ་རིགས་ཞེས་བྱ་བའི་མིང་བྱུང་ངོ་། །སྐྱེ་བོའི་ཚོགས་ཕལ་པོ་ཆེས་བཀུར་བ་དང་། སྐྱེ་དགུ་ཡང་དགའ་བར་བྱེད་པས་རྒྱལ་པོ་མང་པོས་བཀུར་བ༌[^2316]ཞེས་བྱ་བའི་མིང་བྱུང་སྟེ། རྒྱལ་པོ་གཅིག་ནས་གཅིག་ཏུ་བརྒྱུད་པའི་རྩོམ་པ་ནི་དེ་ཡིན་ནོ། །

[Block 4063]
དེ་ལ་གང་དག་ཁྱིམ་དག་ནས་ཡིད་ཕྱིར་ཕྱོགས་པ་དེ་དག་ལ་ནི་བྲམ་ཟེ་ཞེས་བྱ་བའི་མིང་བྱུང་ངོ་། །དེ་ནས་གང་ཡང་རུང་བའི་རྒྱལ་པོ་ཞིག་གིས་ཆགས་པས༌[^2317]སེམས་ཅན་རྣམས་ལ་མ་བགོས་པ་དང་རྐུན་པོ་མང་དུ་གྱུར་ཏེ། [^2318]དེ་དག་ལ་མཚོན་གྱིས་འདེབས་པར་གྱུར་ཏོ། །

[Block 4064]
དེ་ནས་གཞན་དག་ན་རེ་ཡང་བདག་ཅག་གིས་དེ་ལྟ་བུ་བགྱིས་པ་མ་མཆིས་སོ་ཞེས་བརྫུན་དུ་སྨྲ་བར་བརྩམས་སོ། །

[Block 4065 [VERSE]]
དེ་ནས་ལས་ཀྱི་ལམ་ལྷག་པས། །
ཚེ་ཐུང་ལོ་ནི་བཅུ་ཡིན་ནོ། །
--- END BLOCKS ---
