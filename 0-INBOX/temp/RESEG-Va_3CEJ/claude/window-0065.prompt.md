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
[Block 2276]
ཉོན་མོངས་བློ་མ་སྦྱངས་པ་རྣམས༌[^1195]ནི་རང་རང་གི་རྣམ་པར་སྨིན་པའི་འབྲས་བུ་དང་། སྐྱེས་བུ་བྱེད་པའི་འབྲས་བུ་ཉམས་སུ་མྱོང་བ་ན་ལོག་པར་གཞན་དབང་ཕྱུག་ཏུ་ཡོངས་སུ་རྟོག་པར་བྱེད་དོ། །

[Block 2277]
དེ་ནི་རྫོགས་སོ།། །།

[Block 2278 [HEADING]]
#### འབྱུང་བ་དང་འབྱུང་བ་ལས་གྱུར་པའི་རྒྱུའི་རྐྱེན། ^2-5-5-0

[Block 2279]
ཡང་། གཞན་ནི་གཉིས་པོ་དག་ལས་སྐྱེ། །ཞེས་གང་བཤད་པ་དེ་ཇི་ལྟར་ན་འབྱུང་བ་རྣམས་འབྱུང་བ་རྣམས་ཀྱི་རྒྱུའི་རྐྱེན་ཡིན་ཞེ་ན། དེ་ཡི་འབྱུང་བ་རྣམ་པ་གཉིས། ། འབྱུང་བའི་རྒྱུ་ཞེས་བྱ་བའི་ཐ་ཚིག་སྟེ། སྐལ་བ་མཉམ་པ་དང་ལྷན་ཅིག་འབྱུང་བའི་རྒྱུ་དག་གིས་སོ། །

[Block 2280]
འབྱུང་ལས་གྱུར་པའི་རྣམ་པ་ལྔ། །བྱུང་བ་རྣམས་འབྱུང་བ་ལས་གྱུར་པའི་ནི་རྒྱུ༌[^1196]རྣམ་པ་ལྔ་ཡིན་ཏེ། ཇི་ལྟ་ཞེ་ན།

[Block 2281 [VERSE]]
སྐྱེད་ཕྱིར་བརྟེན༌[^1197]ཕྱིར་གནས་ཕྱིར་དང་། །
རྟོན་པའི༌[^1198]ཕྱིར་དང་འཕེལ་བྱེད་ཕྱིར། །

[Block 2282]
དེ་ཡང་བྱེད་རྒྱུའི༌[^1199]རྒྱུ་ཁོ་ན་རྣམ་པ་ལྔ་ཐ་དད་པ་ཡིན་ཏེ། སྐྱེད་པའི་རྒྱུ་ནི་དེ་དག་ལས་སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 2283]
བརྟེན་པའི༌[^1200]རྒྱུ་ནི་སྐྱེས་པ་འབྱུང་བའི་རྗེས་སུ་མཐུན་པར་བྱེད་པའི་ཕྱིར་ཏེ། སློབ་དཔོན་ལ་སོགས་པ་ལ་བརྟེན་པ་བཞིན་ནོ། །

[Block 2284]
གནས་པའི་རྒྱུ་ནི་རྟེན་དུ་གྱུར་པའི་ཕྱིར་ཏེ། རི་མོའི་རྩིག་པ་བཞིན་ནོ། །

[Block 2285]
རྟོན་པའི༌[^1201]རྒྱུ་ནི་རྒྱུན་མི་འཆད་པའི་རྒྱུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2286]
འཕེལ་བར་བྱེད་པའི་རྒྱུ་ནི་འཕེལ་བའི་རྒྱུ་ཡིན་པའི་ཕྱིར༌[^1202]ཏེ། དེ་ལྟ་བས༌[^1203]ན་དེ་དག་གི་སྐྱེ་བ་དང་། འགྱུར་བ་དང་། བརྟེན༌[^1204]པ་དང་གནས་པ་དང་། རྟོན་པ་དང་འཕེལ་བའི་རྒྱུ་ཉིད་དུ་བསྟན་པ་ཡིན་ནོ། །

[Block 2287]
འབྱུང་འགྱུར་རྣམ༌[^1205]གསུམ་ཕན་ཚུན་དུ། །རྒྱུ་ཡིན་ཏེ། ལྷན་ཅིག་འབྱུང་བ་དང་། སྐལ་བ་མཉམ་པ་དང་། རྣམ་པར་སྨིན་པའི་རྒྱུ་དག་གིས་སོ། །

[Block 2288]
བྱེད་རྒྱུའི་རྒྱུ་ནི་བྱེ་བྲག་མེད་པར་འཇུག་པའི་ཕྱིར་རྟག་ཏུ་མི་བགྲང་ངོ་། །དེ་ལ་ལྷན་ཅིག་འབྱུང་བའི་རྒྱུ་ནི་ལུས་དང་ངག་གི་ལས་སེམས་ཀྱི་རྗེས་སུ་འཇུག་པ་ཕན་ཚུན་དུ་ཡིན་གྱི་རྒྱུར་བྱས་པའི་གཟུགས་གཞན༌[^1206]མ་ཡིན་ནོ། །

[Block 2289]
སྐལ་བ་མཉམ་པའི༌[^1207]རྒྱུ་ནི་སྔར་བྱུང་བ་ཐམས་ཅད་སྐལ་བ་མཉམ་པའི་རྒྱུ་ཡིན་ནོ། །

[Block 2290]
རྣམ་པར་སྨིན་པའི་རྒྱུ་ནི་ལུས་དང་ངག་གི་ལས་གང་གི་རྣམ་པར་སྨིན་པ་མིག་ལ་སོགས་པ་ཡིན་པའོ།[^1208] །འབྱུང་བ་རྣམས་ཀྱི་དེ་རྣམས་གཅིག །འབྱུང་བ་ལས་གྱུར་པའི་གཟུགས་འབྱུང་བ་རྣམས་ཀྱི་ནི་རྣམ་པར་སྨིན་པའི་རྒྱུ་ཁོ་ན་ཡིན་ཏེ། ལུས་དང་ངག་གི་ལས་གང་གི་རྣམ་པར་སྨིན་པ་རྣམས་ཡིན་པའོ། །

[Block 2291 [HEADING]]
#### སེམས་གང་གི་མཇུག་ཐོགས་སུ་གང་འབྱུང་བ། ^2-5-6-0

[Block 2292]
སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་བྱེ་བྲག་མེད་པར་མཚུངས་པ་དེ་མ་ཐག་པའི་རྐྱེན་དུ་བཤད་ཀྱི།[^1209] སེམས་གང་གི་མཇུག་ཐོགས་སུ་གང་འབྱུང་ཞེས་བྱ་བ་ངེས་པ་ནི་མ་བཤད་པས་ད་ནི་དེ་བརྗོད་པར་བྱའོ། །

[Block 2293 [HEADING]]
##### སེམས་བཅུ་གཉིས། ^2-5-6-1-0

[Block 2294]
དེ་ལ་རེ་ཞིག་མདོར་བསྡུ་ན་སེམས་བཅུ་གཉིས་སོ། །ཇི་ལྟ་ཞེ་ན།

[Block 2295 [VERSE]]
འདོད་ཡིད་དགེ་དང་མི་དགེ་དང་། །
བསྒྲིབས་པ་དང་ནི་མ་བསྒྲིབས་པ། །

[Block 2296]
ཞེས་བྱ་བ་སྨོས་ཏེ། འདོད་པའི་ཁམས་ན་སེམས་བཞི་སྟེ། །དགེ་བ་དང༌[^1210]མི་དགེ་བ་དང༌[^1211]བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་དང་། མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པའོ། །

[Block 2297]
གཟུགས་དང་གཟུགས་མེད་པ་དག་ན། མི་དགེ་ལས་གཞན། གཟུགས་ཀྱི་ཁམས་ན་མི་དགེ་བ་མེད་ཀྱི་གསུམ་ཡོད་དོ། །

[Block 2298]
གཟུགས་མེད་པའི་ཁམས་ན་ཡང་དེ་དང་འདྲ་སྟེ། དེ་ལྟར་ན་བཅུ་པོ་དེ༌[^1212]དག་ནི་ཟག་པ་དང་བཅས་པའི་སེམས་ཡིན་ནོ། །

[Block 2299]
ཟག༌[^1213]མེད་གཉིས། སློབ་པ་དང་མི་སློབ་པ་སྟེ། དེ་ལྟར་ན་དེ་དག་ནི་སེམས་བཅུ་གཉིས་ཡིན་ནོ། །

[Block 2300]
དེ་ལ། འདོད་སེམས་དགེ་བ་ལས་སེམས་དགུ། །མཇུག་ཐོགས་སུ་ཞེས་འོག་ནས་འཆད་དེ། འདོད་པའི་ཁམས་ན་དགེ་བའི་སེམས་གང་ཡིན་པ་དེའི་མཇུག་ཐོགས་སུ་ནི་སེམས་དགུ་འབྱུང་སྟེ། རང་གི་ས་པ་བཞི་དང་སློབ་པ་དང་། མི་སློབ་པ་དང་། [^1214]གཟུགས་ན་སྤྱོད་པ་གཉིས་ཏེ། སྙོམས་པར་འཇུག་པའི་ཚེ་དགེ་བ་དང་། ཉིང་མཚམས་སྦྱོར་བའི་ཚེ་བསྒྲིབས་པའོ། །

[Block 2301]
གཟུགས་མེད་པ་ན་སྤྱོད་པ་ནི་ཉིང་མཚམས་སྦྱོར་བའི་ཚེ་བསྒྲིབས་པ་ཁོ་ན་སྟེ། ཤིན་ཏུ་བསྐལ་པའི་ཕྱིར་དགེ་བ་ནི་མ་ཡིན་ནོ། །

[Block 2302]
གཟུགས་མེད་པ་ན་སྤྱོད་པ་རྣམས་ནི་འདོད་པའི་ཁམས་ནས་རིང་བ་ཉིད་བཞིས་རིང་བ་ཡིན་ཏེ། རྟེན་དང་རྣམ་པ་དང་། དམིགས་པ་དང་། [^1215]གཉེན་པོ་རིང་བ་ཉིད་དག་གིས་སོ། །

[Block 2303]
དེ་ལ་རྟེན་རིང་བ་ཉིད་ནི་སྙོམས་པར་འཇུག་པའི་མཚུངས་པ་དེ་མ་ཐག་པའི་རྐྱེན་གྱི་རྟེན་ཉིད་དུ་མི་སྲིད་པའི་ཕྱིར་རོ། །

[Block 2304]
རྣམ་པར་རིང་བ༌[^1216]ཉིད་ནི་འདོད་པའི་ཁམས་རགས་པ་ལ་སོགས་པའི་རྣམ་པ་དག་ཏུ་རྣམ་པར་མི་བྱེད་པའི་ཕྱིར་རོ། །

[Block 2305]
དེས་ན་དམིགས་པ་རིང་བ་ཉིད་ཀྱང་བཤད་པ་ཡིན་ཏེ། བསམ་གཏན་བཞི་པ་ཁོ་ན་ལ་རགས་པ་ལ་སོགས་པའི་རྣམ་པ་དག་ཏུ་དམིགས་སོ། །

[Block 2306]
གཉེན་པོ་རིང་བ་ཉིད་ནི་འདོད་པའི་འདོད་ཆགས་དང་མ་བྲལ་བ་ལ་དེ་མངོན་དུ་འགྱུར་མི་སྲིད་པའི་ཕྱིར་རོ། །

[Block 2307]
རྣམ་པར་སུན་འབྱིན་པ་ལ་སོགས་པ་ཡང་མི་འཐད་པའི་ཕྱིར་ཏེ། ཡུལ་མ་ཡིན་པ་ནི་རྣམ་པར་སུན་དབྱུང་བར་མི་ནུས་སོ། །

[Block 2308]
སློབ་པ་དང་མི་སློབ་པའོ། །

[Block 2309]
དེ་ནི་བརྒྱད་པོ་ཁོ་ན་ལས་འདོད་པ་ན་སྤྱོད་པའི་དགེ་བའི་སེམས་དེ་ནི་བརྒྱད་ཀྱི་མཇུག་ཐོགས་སུ་འབྱུང་སྟེ། རང༌[^1217]གི་ས་པ་བཞི་དང་། གཟུགས་ན་སྤྱོད་པ་གཉིས་ལས་ཏེ། ལྡང་བའི་ཚེ་དགེ་བ་དང་། ཉོན་མོངས་པ་ཅན་གྱི༌[^1218]སྙོམས་པར་འཇུག་པས་གཟིར་བ་ས་འོག་མའི་དགེ་བ་ལ་བརྟེན་པའི་ཕྱིར་བསྒྲིབས་པ་དང་། ལྡང་བའི་ཚེ་སློབ་པ་དང་མི་སློབ་པ་དག་ལས་སོ། །

[Block 2310]
མི་དགེ་བ་ནི་བཅུ་དག་ལས། །

[Block 2311]
སློབ་པ་དང་མི་སློབ་པ་དག༌[^1219]མ་གཏོགས་ཏེ། འདོད་པའི་ཁམས་སུ་ཉིང་མཚམས་སྦྱོར་བ་ན་གཟུགས་དང་གཟུགས་མེད་པའི་སེམས་ཐམས་ཅད་ཀྱི་མཇུག་ཐོགས་སུ་མི་དགེ་བའི་སེམས་འབྱུང་ངོ་། །དེ་ལས་བཞི་སྟེ། མི་དགེ་བའི་སེམས་ཀྱི་མཇུག་ཐོགས་སུ་ནི་སེམས་བཞི་འབྱུང་སྟེ། རང་གི་ས་པ་དག་ཁོ་ནའོ། །

[Block 2312]
ཇི་ལྟར་འདོད་པའི་ཁམས་ཀྱི་མི་དགེ་བའི་སེམས་བཤད་པ། བསྒྲིབས་དེ་བཞིན། བཅུ་པོ་ཁོ་ནའི་མཇུག་ཐོགས་སུ་འབྱུང་ལ།

[Block 2313 [VERSE]]
དེ་ལས་ནི་བཞི་ཁོ་ནའོ། །
མ་བསྒྲིབས་པ་ནི་ལྔ་དག་ལས། །

[Block 2314]
འདོད་པ་ན་ཞེས་བྱ་བར་སྦྱར་ཏེ། མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པའི་སེམས་ནི་ལྔའི་མཇུག་ཐོགས་སུ་འབྱུང་སྟེ། རང་གི་ས་པ་བཞི་དང་། གཟུགས་ན་སྤྱོད་པའི་དགེ་བ་ལས་སྤྲུལ་པའི་སེམས་སོ། །

[Block 2315]
དེ་ལས་མཇུག་ཐོགས༌[^1220]སེམས་བདུན་ནོ། །
--- END BLOCKS ---
