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
འབྲས་བུ་གང་ཞིག་ལས་ཡོངས་སུ་ཉམས་པ་ནི་འབྲས་བུ་དེ་ལ་གནས་པས་བྱ་བ་མ་ཡིན་པ་གང་ཡིན་པའི། བྱ་བ་མ་ཡིན་དེ་མི་བྱེད། །ཡོངས་སུ་ཉམས་ཀྱང་འབྲས་བུ་དེ་དང་འགལ་བའི་བྱ་བ་མི་བྱེད་དེ། རྩལ་པོ་ཆེ་བྲེད་པ༌[^2231]རྡེག་མི་འཆའ་བ་བཞིན་ནོ། །

[Block 3222 [HEADING]]
##### དབང་པོ་འཕོ་བ། ^3-2-12-7-0

[Block 3223]
ཡང་དབང་པོ་རྣམས་འཕོ་བ་ལ་བར་ཆད་མེད་པ་དང་རྣམ་པར་གྲོལ་བའི་ལམ་དུ་དག་ཅིག་སྐྱེ་ཞེ་ན། མི་གཡོ་རྣམ་གྲོལ་བར་ཆད་མེད། །ལམ་དགུའོ། །

[Block 3224]
རྟོགས་པའི་སྐལ་བ་ཅན་ཞིག་མི་གཡོ་བའི་རིགས་ཅན་རྟོགས་པར་བྱེད་ན་བར་ཆད་མེད་པའི་ལམ་དགུ༌[^2232]དང་། རྣམ་པར་གྲོལ་བའི་ལམ་དགུ་སྐྱེ་སྟེ། དཔེར་ན་དགྲ་བཅོམ་པ་ཉིད་ཐོབ་པ་བཞིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན། དབང་པོ་རྟུལ་པོའི་རིགས་དེ་ཤིན་ཏུ་བརྟེན༌[^2233]ཕྱིར་རོ། །

[Block 3225]
དེས་དབང་པོ་རྟུལ༌[^2234]པོའི་རིགས་དེ་ཤིན་ཏུ་གོམས་པར་བྱས་པ་ཡིན་པས་འབད་པ་ཆུང་ངུས་བཟློག་པར་མི་ནུས་ཏེ། སློབ་པ་དང་མི་སློབ་པའི་ལམ་དག་གིས་བརྟན་པོར་བྱས་པའི་ཕྱིར་རོ། །

[Block 3226]
མཐོང་བས་ཐོབ་ལ་རེ་རེའོ། །

[Block 3227]
མཐོང་བས་ཐོབ་པ་རྟོགས་པར་བྱེད་ན་བར་ཆད་མེད་པའི་ལམ་གཅིག་ཁོ་ན་དང་རྣམ་པར་གྲོལ་བའི་ལམ་གཅིག་ཁོ་ན་སྐྱེའོ། །

[Block 3228]
སྦྱོར་བའི་ལམ་ནི༌[^2235]ཐམས་ཅད་དུ་གཅིག་ཁོ་ན་ཡིན་ནོ། །

[Block 3229]
བར་ཆད་མེད་པ་དང་རྣམ་པར་གྲོལ་བའི་ལམ་དེ་དག་ཐམས་ཅད་ནི། ཟག་མེད། འཕགས་པ་རྣམས་ཀྱི་དབང་པོ་ནི་ཟག་པ་དང་བཅས་པའི་ལམ་གྱིས༌[^2236]འཕོ་བ་མེད་དོ། །

[Block 3230]
དབང་པོ་རྣམས་གང་དུ་འཕོ་ཞེ་ན། མི་ཡི་ནང་དུ་འཕོ། །མི་རྣམས་ཀྱི་ནང་ཁོ་ནར་དབང་པོ་འཕོའི༌[^2237]གཞན་དུ་ནི་མ་ཡིན་ཏེ། ཡོངས་སུ་ཉམས་པ་མི་སྲིད་པའི་ཕྱིར་རོ། །

[Block 3231]
གང་ཞིག་ས་གང་ལ་བརྟེན་ནས་དབང་པོ་རྣམས་འཕོ་བར་བྱེད་ཅེ་ན། མི་སློབ་པ༌[^2238]དགུ་ལ་བརྟེན་ཏེ། མི་ལྕོགས་པ་མེད་པ་དང་། བསམ་གཏན་ཁྱད་པར་ཅན་དང་། བསམ་གཏན་བཞི་དང་། གཟུགས་མེད་པ་གསུམ་པ༌[^2239]ལའོ། །

[Block 3232]
སློབ་པ་དྲུག་ལ། གཟུགས་མེད་པ་རྣམས་མ་གཏོགས་སོ། །ཅིའི་ཕྱིར་ཞེ་ན། གང་གི༌[^2240]ཕྱིར།

[Block 3233 [VERSE]]
འཕེལ་བ་འབྲས་བུ་ཁྱད་པར་ཅན། །
བཏང་སྟེ་འབྲས་བུ་ཐོབ་པར་འགྱུར། །

[Block 3234]
དབང་པོ་རྣམས་འཕོ་བ་ན་དབང་པོ་རྟུལ༌[^2241]པོའི་ལམ་གྱི་འབྲས་བུ་དང་འབྲས་བུ་ཁྱད་པར་ཅན་བཏང་སྟེ་དབང་པོ་རྣོན་པོའི་རིགས་ཀྱི་ལམ་གྱི་འབྲས་བུ་ཁོ་ན་འཐོབ་པར༌[^2242]འགྱུར་ན། ཕྱིར་མི་འོང་བའི་འབྲས་བུ་གཟུགས་མེད་པས་བསྡུས་པ་ནི་མེད་དོ་ཞེས་བྱ་བ་འདི་ནི་གཏན་ཚིགས་ཡིན་ནོ། །

[Block 3235 [HEADING]]
##### དབང་པོ་རྣམ་པ་དགུ་ཅན། ^3-2-12-8-0

[Block 3236]
དགྲ་བཅོམ་པ་འདི་དག་ཐམས་ཅད་ནི་དབང་པོའི་བྱེ་བྲག་ལས་དགུ་ཁོ་ན་ཡིན་ཏེ། ཇི་ལྟར་བྱས་པས་ཤེ་ན།

[Block 3237 [VERSE]]
སངས་རྒྱས་གཉིས་དང་ཉན་ཐོས་བདུན། །
དེ་དགུ་དབང་པོ་རྣམ་དགུ་ཅན། །
ཉན་ཐོས་བདུན་གང་ཞེ་ན། །

[Block 3238]
ཡོངས་སུ་ཉམས་པའི་ཆོས་ཅན་ལ་སོགས་པ་ལྔ་དང་། མི་གཡོ་བའི་ཆོས་ཅན་རྣམ་པ་གཉིས་ཏེ། སྦྱངས་པ་ལས་གྱུར་པ་དང་། དང༌[^2243]པོ་ནས་དེའི་རིགས་ཅན་ནོ།[^2244] །སངས་རྒྱས་གཉིས་ནི་མི་གཡོ་བའི་བྱེ་བྲག་ཁོ་ན་ཡིན་ཏེ། རང་སངས་རྒྱས་དང་། སངས་རྒྱས་སོ། །

[Block 3239]
དེ་ལྟར་ན་དེ་དག་ནི་ཆུང་ངུའི་ཆུང་ངུ་ལ་སོགས་པ་དབང་པོ་རྣམ་པ་དགུའི་བྱེ་བྲག་གིས་གང་ཟག་དགུ་ཡིན་ནོ། །

[Block 3240 [HEADING]]
#### འཕགས་པའི་གང་ཟག་བདུན། ^3-2-13-0

[Block 3241]
འཕགས་པའི་གང་ཟག་རྣམས་ནི་ཐམས་ཅད་དུ་བདུན་ཡིན་ཏེ། དད་པས་རྗེས་སུ་འབྲང་བ་དང་། ཆོས་ཀྱིས་རྗེས་སུ་འབྲང་བ་དང་། དད་པས་མོས་པ་དང་། མཐོང་བས་ཐོབ་པ་དང་། ལུས་ཀྱིས༌[^2245]མངོན་སུམ་དུ་བྱེད་པ་དང་། ཤེས་རབ་ཀྱིས༌[^2246]རྣམ་པར་གྲོལ་བ་དང་། གཉི་གའི་ཆ་ལས་རྣམ་པར་གྲོལ་བའོ། །

[Block 3242]
གང་ཟག་བདུན་པོ་དེ་དག་ཀྱང་སྦྱོར་བ་དང་། དབང་པོ་སྙོམས་འཇུག་རྣམ་གྲོལ་དང་། །གཉི་གས་བྱས་པའོ། །

[Block 3243]
སྦྱོར་བ་ལས་ནི་དད་པས་རྗེས་སུ་འབྲང་བ་དང་། ཆོས་ཀྱིས་རྗེས་སུ་འབྲང་བ་དག་སྟེ། [^2247]

[Block 3244]
དང་པོ་ཉིད་ནས་གཞན་གྱི༌[^2248]དྲིང་འཇོག་པ་དང་། ཆོས་ཀྱིས༌[^2249]རྗེས་སུ་འབྲང་བ་དག་གིས༌[^2250]དོན་རྣམས་ལ་སྦྱོར་བའི་ཕྱིར་རོ། །

[Block 3245]
དབང་པོ་ལས་ནི་དད་པས་མོས་པ་དང་། མཐོང་བས་ཐོབ་པ་དག་སྟེ། དད་པས་མོས་པ་དང་ཤེས་རབ་ལྷག་པའི་སྒོ་ནས་དབང་པོ་རྟུལ་པོ་དང་རྣོན་པོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3246]
སྙོམས་པར་འཇུག་པ་ལས་ནི་ལུས་ཀྱིས༌[^2251]མངོན་སུམ་དུ་བྱེད་པ་སྟེ། འགོག་པའི་སྙོམས་པར་འཇུག་པ་མངོན་སུམ་དུ་བྱེད་པའི་ཕྱིར་རོ། །

[Block 3247]
རྣམ་པར་གྲོལ་བ་ལས༌[^2252]ནི་ཤེས་རབ་ཀྱིས་རྣམ་པར་གྲོལ་བའོ། །

[Block 3248]
སྙོམས་པར་འཇུག་པ་དང་རྣམ་པར་གྲོལ་བ་ལས་ནི་གཉི་གའི་ཆ་ལས་རྣམ་པར་གྲོལ་བའོ། །

[Block 3249]
མིང་གི༌[^2253]སྒོ་ནས་ནི་གང་ཟག་དེ་བདུན་ཡིན་ནོ། །

[Block 3250]
དེ་དག་དྲུག །རྫས་སུ་ནི་དེ་དག་དྲུག་ཡིན་ཏེ། འདི་ལྟར་ལམ་གསུམ་ལ་གཉིས་གཉིས། མཐོང་བའི་ལམ་ལ་གང་ཟག་གཉིས་ཏེ། དད་པས་རྗེས་སུ་འབྲང་བ་དང་། ཆོས་ཀྱིས༌[^2254]རྗེས་སུ་འབྲང་བ་དག་གོ། །

[Block 3251]
དེ་དག་ཉིད་བསྒོམ་པའི༌[^2255]ལམ་ལ་གཉིས་ཏེ། དད་པས་མོས་པ་དང་། མཐོང་བས་ཐོབ་པ་དག་གོ། །

[Block 3252]
དེ་གཉིས༌[^2256]ཀྱང་མི་སློབ་པའི་ལམ་ལ་གཉིས་ཡིན༌[^2257]ཏེ། དུས་ཀྱིས༌[^2258]རྣམ་པར་གྲོལ་བ་དང་། །དུས་དང་མི་སྦྱོར་བར་རྣམ་པར་གྲོལ་བ་དག་གོ། །

[Block 3253]
དེ་ལ་དད་པས་རྗེས་འབྲང་བ་དབང་པོའི་སྒོ་ནས་ནི་གསུམ་མོ། །

[Block 3254]
རིགས་ཀྱི་སྒོ་ནས་ནི་ལྔའོ། །

[Block 3255]
ལམ་གྱི་སྒོ་ནས༌[^2259]བཅོ་ལྔ་སྟེ། བཟོད་པ་བརྒྱད་དང་ཤེས་པ་བདུན་ལ་གནས་པའོ། །

[Block 3256]
འདོད་ཆགས་དང་བྲལ་བའི་སྒོ་ནས་ནི༌[^2260]བདུན་ཅུ༌[^2261]རྩ་གསུམ་སྟེ། འཆིང་བ་མཐའ་དག་དང་ལྡན་པ་དང་འདོད་པ༌[^2262]ལས་འདོད་ཆགས་དང་བྲལ་བའི་ཕྱིར་དགུ་ནས་དེ་བཞིན་དུ་ཅི་ཡང་མེད་པའི་སྐྱེ་མཆེད་ལས་འདོད་ཆགས་དང་བྲལ་བའི་ཕྱིར་གྱི་བར་དུའོ། །

[Block 3257]
རྟེན་གྱི་སྒོ་ནས་ནི་དགུ་སྟེ། གླིང་གསུམ་དང་ལྷའི་རིས་དྲུག་ཏུ་སྐྱེས་པའོ། །

[Block 3258]
དབང་པོ་དང་རིགས་དང་ལམ་དང་འདོད་ཆགས་དང་བྲལ་བ་དང་རྟེན་གྱི་སྒོ་ནས་བསྡོམས༌[^2263]ན་ནི། འབུམ་བཞི་ཁྲི་བདུན་སྟོང་བརྒྱད་བརྒྱ་ཉི་ཤུ་རྩ་ལྔར་འགྱུར་ཏེ། གང་ཟག་གཞན་དག་ཀྱང་ཅི་རིགས་པར་དེ་བཞིན་དུ་བརྩི་བར་བྱའོ། །

[Block 3259 [HEADING]]
##### གཉི་གའི་ཆ་ལས་རྣམ་པར་གྲོལ་བ་དང་ཤེས་རབ་ཀྱིས་རྣམ་པར་གྲོལ་བ། ^3-2-13-1-0

[Block 3260]
གཉི་གའི་ཆ་ལས་རྣམ་པར་གྲོལ་བ་ཞེས་བྱ་བ་འདི་ནི་གང་། ཤེས་རབ་ཀྱིས༌[^2264]རྣམ་པར་གྲོལ་བ་ནི་གང་ཞེ་ན།
--- END BLOCKS ---
