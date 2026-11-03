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

[Block 2316]
འདོད་པ་ན་སྤྱོད་པའི་མ་བསྒྲིབས་ལ་ལུང་དུ༌[^1221]མ་བསྟན་པས༌[^1222]ལས་ནི་རང་གི་ས་པ་བཞི་དང་། གཟུགས་ན་སྤྱོད་པ་གཉིས་ཏེ། སྤྲུལ་པའི་སེམས་ཀྱི་མཇུག་ཐོགས་སུ་དགེ་བ་དང་། ཉིང་མཚམས་སྦྱོར་བའི་ཚེ་ཉོན་མོངས་པ་ཅན་དང་། ཉིང་མཚམས་སྦྱོར་བའི་ཚེ་གཟུགས་མེད་པ་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་ཅན་ཁོ་ནའོ། །

[Block 2317]
གཟུགས་ན་དགེ་བ་ལས་བཅུ་གཅིག་གོ། །

[Block 2318]
གཟུགས་ཀྱི་ཁམས་ན་དགེ་བའི་སེམས་གང་ཡིན་པ་དེའི་མཇུག་ཐོགས་སུ་སེམས་བཅུ་གཅིག་ཁོ་ན་འབྱུང་སྟེ། གཟུགས་མེད་པ་ན་སྤྱོད་པའི་མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་མ་གཏོགས་སོ། །

[Block 2319]
དེ་ནི་དགུ་ཡི་མཇུག་ཐོགས་སུ། །གཟུགས་ན་སྤྱོད་པའི་དགེ་བའི་སེམས་དེ་ནི་དགུའི་མཇུག་ཐོགས་སུ་འབྱུང་སྟེ། འདོད་པ་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་ཅན་གཉིས་དང་། གཟུགས་མེད་པ་ན་སྤྱོད་པའི་མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་མ་གཏོགས་སོ། །

[Block 2320]
བསྒྲིབས་པ་བརྒྱད་ལས།

[Block 2321]
གཟུགས་ན་སྤྱོད་པའི་སེམས་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་ནི་བརྒྱད་ལས་འབྱུང་སྟེ། འདོད་པ་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་ཅན་གཉིས་དང་། སློབ་པ་དང་། མི་སློབ་པ་གཉིས༌[^1223]མ་གཏོགས་སོ། །

[Block 2322]
དེ་ལས་དྲུག་གཟུགས་ན་སྤྱོད་པའི་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པའི་མཇུག་ཐོགས་སུ་ནི་དྲུག་སྟེ། རང་གི་ས་པ་གསུམ་དང་། འདོད་པ་ན་སྤྱོད་པའི་མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་མ་གཏོགས་པ་རྣམས་སོ། །

[Block 2323]
མ་བསྒྲིབས་པ་ནི་གསུམ་ལས་སོ། །

[Block 2324]
གཟུགས་ན་སྤྱོད་པའི་མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་ནི་གསུམ་ཁོ་ན་ལས་འབྱུང་སྟེ། རང་གི་ས་པ་དག་ཁོ་ན་ལས་སོ། །

[Block 2325]
དེ་ལས་དྲུག་སྟེ། རང་གི་ས་པ་གསུམ་དང་། འདོད་པ་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་ཅན་དག་དང་། གཟུགས་མེད་པ་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་ཅན་ནོ། །

[Block 2326]
གཟུགས་ཀྱི་ཁམས་ཀྱི་མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་ཇི་སྐད་དུ་བཤད་པ་ལྟར། གཟུགས་མེད་པའང་དེའི་ཚུལ་ལོ། །

[Block 2327]
དེ་ན་ཡོད་པའི་མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་ཡང་རང་གི་ས་པ་གསུམ་ཁོ་ན་ལས་འབྱུང་ལ། དེ་ལས་ཀྱང་རང་གི་ས་པ༌[^1224]གསུམ་དང་། ས་འོག་མ་པའི་ཉོན་མོངས་པ་ཅན་རྣམས་དང་དྲུག་འབྱུང་ངོ་། །དགེ་བ་ལས་སེམས་དགུ་དག་གོ། །

[Block 2328]
གཟུགས་མེད་པ་ན་སྤྱོད་པའི་དགེ་བའི་སེམས་ལས་ནི་སེམས་དགུ་འབྱུང་སྟེ། འདོད་པ་ན་སྤྱོད་པའི་དགེ་བ༌[^1225]དང་། འདོད་པ་དང་གཟུགས་ན་སྤྱོད་པའི་མ་བསྒྲིབས༌[^1226]ལ་ལུང་དུ་མ་བསྟན་པ་དག་མ་གཏོགས་སོ། །

[Block 2329]
དེ་དྲུག་གི །གཟུགས་མེད་པ་ན་སྤྱོད་པའི་དགེ་བ༌[^1227]ནི་རང་གི་ས་པ་གསུམ་དང་། གཟུགས་ན་སྤྱོད་པའི་དགེ་བ་དང་། སློབ་པ་དང་། མི་སློབ་པ་དག་ལས་སོ། །

[Block 2330]
བསྒྲིབས་པ་ལས་བདུན། གཟུགས་མེད་པ་ན་སྤྱོད་པའི་བསྒྲིབས་པ་ལས་ནི་རང་གི་ས་པ་གསུམ་དང་། གཟུགས་ན་སྤྱོད་པའི་དགེ་བ་དང་། བསྒྲིབས་པ་དང་། འདོད་པ་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་ཅན་གཉིས་སོ། །

[Block 2331]
དེ་དེ་བཞིན། དེ་ཡང་བདུན་ཁོ་ན་ལས་འབྱུང་སྟེ། འདོད་པ་དང་གཟུགས་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་ཅན་རྣམས་དང་། སློབ་པ་དང་མི་སློབ་པ་དག་མ་གཏོགས་སོ། །

[Block 2332]
སློབ་པ་བཞི་ལས།

[Block 2333]
ཁམས་གསུམ་པའི་དགེ་བ་དང་། སློབ་པ་ལས་སོ། །

[Block 2334]
དེ་ལས་ལྔ། བཞི་པོ་དེ་དག་ཉིད་དང་། མི་སློབ་པའོ། །

[Block 2335]
མི་སློབ་པ་ནི་ལྔ་ལས་སོ། །

[Block 2336]
བཤད་མ་ཐག་པའི་ལྔ་པོ་དེ༌[^1228]ཉིད་ལས་སོ། །

[Block 2337]
དེ་ལས་སེམས་ནི་བཞི་དག་གོ། །

[Block 2338]
མི་སློབ་པའི་སེམས་དེའི་མཇུག་ཐོགས་སུ་ནི་སེམས་བཞི་འབྱུང་སྟེ། ཁམས་གསུམ་པའི་དགེ་བ་དང་། མི་སློབ་པའོ། །

[Block 2339]
སེམས་བཅུ་གཉིས་རྫོགས་སོ།། །།

[Block 2340 [HEADING]]
##### སེམས་ཉི་ཤུ། ^2-5-6-2-0

[Block 2341]
ཡང་བཅུ་གཉིས་དེ་དག་ཉི་ཤུར་ཡང་བཤད་དེ། ཇི་ལྟར་བྱས་ནས་ཤེ་ན།

[Block 2342 [VERSE]]
གསུམ་དུ་སྐྱེས་ནས༌[^1229]ཐོབ་པ་དང་། །
སྦྱོར་བྱུང་དགེ་རྣམས༌[^1230]གཉིས་ཕྱེ་ནས། །

[Block 2343]
ཁམས་གསུམ་པོ་དག་ཏུ་སྐྱེས་ནས་ཐོབ་པ་དང་སྦྱོར་བ་ལས་བྱུང་བའི་དགེ་བའི་སེམས་རྣམ་པ་གཉིས་སུ་དབྱེའོ། །

[Block 2344 [VERSE]]
རྣམ་སྨིན་སྐྱེས་དང་སྤྱོད་ལམ་པ། །
བཟོ་ཡི་གནས་དང་སྤྲུལ་པ་དང་། །
འདོད་ན་ལུང་བསྟན་མིན་རྣམ་བཞིར། །

[Block 2345]
ཕྱེ་ནས་ཞེས་བྱ་བར་སྦྱར་ཏེ། འདོད་པ་ན་སྤྱོད་པའི་མ་བསྒྲིབས༌[^1231]ལ་ལུང་དུ་མ་བསྟན་པ་ལ༌[^1232]ནི་རྣམ་པར་སྨིན་པ༌[^1233]ལས་སྐྱེས་པ་དང་། སྤྱོད་ལམ་པ་དང་། བཟོའི་གནས་པ་དང་། སྤྲུལ་པའི་སེམས་དང་རྣམ་པ༌[^1234]བཞིར་དབྱེའོ། །

[Block 2346]
གཟུགས་ན་བཟོ་མ་གཏོགས་པའོ། །

[Block 2347]
གཟུགས་ཀྱི་ཁམས༌[^1235]ནི་རྣམ་པ་གསུམ༌[^1236]དབྱེ་སྟེ། དེ་ན་བཟོ་མེད་པའི་ཕྱིར་བཟོའི་གནས་པ་མ་གཏོགས་སོ། །

[Block 2348]
དེ་ལྟར་ན་སེམས་བཅུ་གཉིས་པོ་དེ་དག་ནི་ཡང་དགེ་བ་དྲུག་དང་། མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་བདུན༌[^1237]དུ་ཕྱེ་ནས་ཉི་ཤུར་འགྱུར་རོ། །

[Block 2349]
གཟུགས་མེད་པའི་ཁམས་ན་ནི་སྤྱོད་ལམ༌[^1238]ལ་སོགས་པ་མེད་པའི་ཕྱིར་སྤྱོད་ལམ་པ་ལ་སོགས་པའི་སེམས་མེད་དོ། །

[Block 2350]
དེ་དག་གི་དམིགས་པ་ནི་གཟུགས་དང་། དྲི་དང་རོ་དང་རེག་བྱ་རྣམས་ཡིན་ནོ། །
--- END BLOCKS ---
