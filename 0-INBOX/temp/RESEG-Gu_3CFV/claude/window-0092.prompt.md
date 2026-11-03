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
ཆེ་གེ་མོ་ཞིག་གི་རྐེད་པ་ནི་སྦོམ་མོ། །

[Block 3222]
ཆེ་གེ་མོ་ཞིག་གི་བརླ་ནི་གླང་པོ་ཆེའི་སྣ་འདྲའོ་ཞེས་ལུས་ཀྱི་ཡན་ལག་དང་གསང་བའི་ཕྱོགས་དག་གི༌[^2082]བརྗོད་པ་རྣམ་པ་མང་པོས་བསྙད་འདོགས་པ་ལས་འདི་བཅས་པ་ཡིན་ནོ། །

[Block 3223]
འདིས་ནི་རོ་སྟོད་མ་གཡོགས་པའི་ཁ་ན་མ་ཐོ་བ་ཉིད་དུ་ཤེས་པར་བྱ་སྟེ་ཞེས་བྱ་བ་འདིས་ཤེས་པར་བྱའོ། །

[Block 3224]
ཆུ་གོས་དང་ཁྲུས་རས་ཞེས་བྱ་བ་འདིའི་རྣམ་པར་འབྱེད་པ་ལས་སོ། །

[Block 3225]
ཆུ་གོས་འདི་དུས་ཐམས་ཅད་དུ་ཕྱི་རོལ་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 3226]
དེའི་ཕྱིར་དགེ་སློང་མ་རྣམས་ལ་དབྱར་གྱི་གོས་རས་ཆེན་མ་གསུངས་ཏེ། དེ་ཉིད་ཀྱིས་ཆོག་པའི༌[^2083]ཕྱིར་རོ། །

[Block 3227]
དེ་གཉིས་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་རྨེ་གབ་དང་ཆུ་གོས་དག་གོ། །

[Block 3228]
རང་ཉིད་ཀྱང་ཉེ་བར་གནས་པ་བཅའ་བ་བསྒྲུབ་པའི་ཕྱིར་བཅང་བར་བྱའོ། །

[Block 3229]
གང་ལ་རྨེ་གབ་འཆང་བར་གཏོགས་པའི་ལྟུང་བྱེད་གསུམ་པར་འགྱུར་བ་དེ་བརྗོད་པར་བྱའོ། །

[Block 3230]
དེའི་ཕྱིར༌[^2084]བཀྲུ་བཤལ་བ་ལ་གོས་འཁྲུར་འཇུག་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རང་གི་གོས་བྱིན་གྱིས་བརླབས་པ་རྙིང་པ་བཀྲུ་བར་འོས་པ་ཆོས་གོས་དང་གདིང་བ་དག་བཀྲུ་བཤལ་བ་ལ་འཁྲུར་འཇུག་པ་ལ་ཞེས་བྱ་བ་འདིས༌[^2085]ནི་འདིའི་བྱེ་བྲག་ཞིབ་ཏུ་ནི་འཁྲུར་འཇུག་པའི༌[^2086]སྤང་བའི་ལྟུང་བྱེད་ཀྱི་རྗེས་སུ་འབྲངས་ནས་ཤེས་པར་བྱའོ། །

[Block 3231]
གང་གི་ཕྱིར་ཁ་ན་མ་ཐོ་བ་ནི་རྣམ་པ་གཉིས་ཏེ། དེ་དང་འདྲ་བའི་ཉེས་དམིགས་ལ་ནི་བཅས་པའོ། །

[Block 3232]
འདིར་གླེང་གཞི་ནི། དགེ་སློང་མ་བཅུ་གཉིས་སྡེ་དག་རྨི་ལམ་ན་གནོད་པ་མཐོང་བས་མི་གཙང་བས་གོས་དག་ལ་གོས་པར་གྱུར་ནས་བཀྲུ་བཤལ་བ་ལ་འཁྲུར་འཇུག་པ་དང་། བཀྲུ་བཤལ་བ་དག་གིས་བླངས་ཏེ། ཁྱིམ་པའི་གོས་དག་དང་ལྷན་ཅིག་བཀྲུས་པས་ན། དེ་དག་གིས་འབགས་པ་ཁྱིམ་པའི་གོས་དཀར་པོ་དག་མི་གཙང་བས་མ་རུངས་པར་གྱུར་པ་དང་། ཁྱིམ་པ་རྣམས་ཀྱིས༌[^2087]བཀྲུ་བཤལ་བ་ལ་བདག་ཅག་གི་གོས་གང་གིས་འབགས་ཞེས་ཟེར་ཞིང་དྲིས་པ་དང་། དེས་སྨྲས་པ། དགེ་སློང་མ་རྣམས་ཀྱི༌[^2088]གོས་བདག་གིས་བཀྲུ་བའི་ཕྱིར་བླངས་ཏེ། དེ་དང་འབྲེལ་པས་འདི་རྣམས་འབགས་པ་ཡིན་ནོ་ཞེས་དེ་སྐད་ཅེས་ཟེར་བ་དེ་ཐོས་པས་ཁྱིམ་པ་རྣམས་འཕྱ་ཞིང་རབ་ཏུ་བྱུང་བ་དག་ནི་ཉེ་བར་མ་ཞིའོ་ཞེས་ཟེར་བའི༌[^2089]བར་ལས་བཅས་པ་ཡིན་ནོ། །

[Block 3233]
ཕྱོགས་གཅིག་བཀྲུས་ན་ཡང་བཀྲུས་པ་ཉིད་ཡིན་ནོ། །

[Block 3234]
བྱས་པ་ཉིད་ལ་བྱེད་དུ་བཅུག་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་དང་། འབྲས་བུའི་མཐའ་ཚུན་ཆད་གཅིག༌[^2090]ཉིད་དོ། །

[Block 3235]
བཤང་བ་དང་གཅི་བ་དང་། ལྗན་ལྗིན་དང་འདམ་རྫབ་ལ་སོགས་པས་མ་རུངས་པ་འཁྲུར་བཅུག་པ་ལ་ཡང་ན་སྨད་པ་མེད་དོ་ཞེས་སྔར་བསྟན་པ་དག་ཀྱང་འདིར་དེ་བཞིན་དུ་རིག་པར་བྱའོ། །

[Block 3236]
འདིར་གོས་ཁ་བསྒྱུར་བ་དང་མ་བསྒྱུར་བ་བཙོ་བླག་མཁན་ལ་ཁ་བསྒྱུར་དུ་བཅུག་པ་ནི་ཇི་ལྟར་ཐོབ་པ་ལས་ཉེས་བྱས་སུ་རིག་པར་བྱའོ། །

[Block 3237]
བསུ་བེལ་བ་ལས་གྱུར་པའི་ལྟུང་བྱེད་གསུམ་མོ།། །།

[Block 3238]
གང་ལ་ཆོས་ཀྱི་རྒྱལ་མཚན་ལ་མི༌[^2091]གུས་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་དགེ་སྦྱོང་གི༌[^2092]གོས་ཁྱིམ་པ་ལ་བགོ་བའི་ཕྱིར་སྦྱིན་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཚད་དང་ལྡན་པའི་གོས་སྣམ་སྦྱར་དང་བླ་གོས་ལ་སོགས་པ་ཁྱིམ་པ་ལ་བགོ་ཞིང་བསྐོན་པའི་ཕྱིར་སྦྱིན་པ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3239]
འདིར་མདོ་ལས་བྱིན་ན་ཞེས་གསུངས་པ་དེའི་རྣམ་པར་འབྱེད་པ་ནི། །བགོ་བར་བྱེད་ཅིང་བསྐོན་པར་བྱེད་ན་ཞེས༌[^2093]གསུངས་པ་ཡིན་ནོ། །

[Block 3240]
བསྐོན་པ་ལ་ངེས་པར་སྦྱོར་བར་འགྱུར་བས་སྦྱིན་པར་བྱའོ་སྙམ་པ༌[^2094]འདི་ནི་དོན་ལ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 3241]
ཚད་ནི་འཁོར་གསུམ་ཁེབས་པའི་མཐར་ཐུག་པ་ཡན་ཆད་ལ་ལྟུང་བྱེད་དོ། །

[Block 3242]
ཁྲུ་གང་ཡན་ཆད་ལ་ནི་ཉེས་བྱས་སོ། །

[Block 3243]
དེ་བས་ན༌[^2095]ཆུང་བ་གཞན་ལ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ༌[^2096]འདིར་རྣམ་པར་གཞག་པ་རིག་པ༌[^2097]ཡིན་པར་ཤེས་པར་བྱའོ། །

[Block 3244]
གང་ཞིག་བསྲུང་བའི་དོན་དུ་བྱིས་པ་དག་ལ་མགྲིན་པར་གོས་བཏགས་ཏེ། ཆ་ལུགས་བསྒྱུར་བའམ་ཞེས་བྱ་བ་སྨོས་པས༌[^2098]ལྟུང་བ་བསྐྱེད་པའི་ཚད་དང་ལྡན་པ་ལ་ཡང་དེར་ཉེས་པ་མེད་པར་རིག་པར་བྱའོ། །

[Block 3245]
དེ་ཡང་རབ་ཏུ་བྱུང་བའི་ཕྱོགས་ལ་གཞག་པ་ཉིད་ཀྱི་ཕྱིར་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 3246]
ཆོས་ཀྱི་རྒྱལ་མཚན་ལ་མི་གུས་པའི་ལྟུང་བྱེད་དོ། །

[Block 3247]
གང་ལྕི་བའི་ཆོས་ལས་འདའ་བར་བྱེད་པའི་ཕྱོགས་དང་མཉམ་པར་བྱེད་པར་གྱུར་པས༌[^2099]རང་གི་ཕྱོགས་ཀྱིས་ལྕི་བའི་ཕྱོགས་ལ་རྒྱལ་མཚན་བརྗེ་བའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་དགེ་སློང་དང་ལྷན་ཅིག་སྣམ་སྦྱར་བརྗེ་བ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཆོས་གོས་ཆེན་པོ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 3248]
དེ་བས་ན་ཁ་ན་མ་ཐོ་བ་འདི་སྐྱེད་པའོ། །

[Block 3249]
[^2100]འདིར་གཞན་ལས་ལེན་ཡང་ཁ་ན་མ་ཐོ་བ་འདིར་འགྱུར་གྱི་སྦྱིན་པ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 3250]
དེ་ལྟ་བས་ན་བཟང་ངན་བརྗེ་བ་མ་གཏོགས་པར་དགེ་སློང་ལ་སྣམ་སྦྱར་ལེན་པ་ལ་ལྟུང་བྱེད་འདི་རྣམ་པར་གཞག་པ་ཁོ་ནའོ། །

[Block 3251]
བརྗེ་བ༌[^2101]ཞེས་བྱ་བ་ནི་ལེན་པའི་དཔེ་ཙམ་དུ་ཟད་དོ། །

[Block 3252]
རྒྱལ་མཚན་བརྗེ་བའི་ལྟུང་བྱེད་དོ།། །།

[Block 3253]
ད་འདི་མན་ཆད་སེར་སྣ་བྱེད་པའི་ལྟུང་བྱེད་ལྔ་སྟོན་ཏེ། གང་ལ་དེ་རྣམས་ཀྱི་དང་པོར༌[^2102]འགྱུར་ཞེ་ན། དེའི་ཕྱིར་བསྔགས་པ་ལ་སེར་སྣ་བྱེད་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་སློང་མ་གཞན་དག་གི་བསྔགས་པ་བརྗོད་པ་ལ༌[^2103]སེར་སྣ་བྱེད་པར་འགྱུར་བ་ལ་ལྟུང་བྱེད་ཅེས་བྱ་བའི་དོན་ཏོ། །གང་ལ་ལྟུང་བྱེད་བཞི་པོར་འགྱུར་ཞེ་ན། དེ་བརྗོད་པར་བྱ༌[^2104]སྟེ་ཁྱིམ་དང་། གནས་དང་། རྙེད་པ་དང་ཆོས་ལ་སེར་སྣ་བྱེད་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ལའོ་ཞེས་བྱ་བའི་སྒྲ་ནི་འདིར་ཁྱིམ༌[^2105]ལ་སོགས་པ་རེ་རེ་ལ་སེར་སྣ་བྱེད་པ༌[^2106]ལའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 3254]
སྡོམ་པར༌[^2107]བྱེད་པ་ཐམས་ཅད་ལ་ཉེས་བྱས་ཉིད་དེ་བསྡམ་པར་བྱ་བ་ཐམས་ཅད་ཀྱང་ཡིད་ཀྱི༌[^2108]ལྟུང་བ་ཐམས་ཅད་ལ་ཞེས་བྱ་བར༌[^2109]རྣམ་པར་གཞག་པའོ། །

[Block 3255]
འདིར་ཡིད་ཙམ་གྱི་སེར་སྣ་བྱེད་པ་ན༌[^2110]བསྡམ་པར་བྱ་བ་ཉིད་ཡིན་ཏེ་ཉེས་བྱས་སོ། །

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
--- END BLOCKS ---
