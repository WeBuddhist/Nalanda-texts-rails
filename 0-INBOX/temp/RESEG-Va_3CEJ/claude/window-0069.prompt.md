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
[Block 2416]
ས་ལྷག་མ་རྣམས་སུ་ནི་རང་གི་ས་པ་ཁོ་ནའོ། །

[Block 2417]
འདོད་པའི་ཁམས་ན༌[^1269]ནི་ཡིད་ལ་བྱེད་པ་གསུམ་སྟེ། ཐོས་པ་དང་བསམས་པ་ལས་བྱུང་བ་དང་། སྐྱེས་ནས་ཐོབ་པ་རྣམས་སོ། །

[Block 2418]
གཟུགས་ཀྱི་ཁམས་ན་ནི་གསུམ་སྟེ། ཐོབ་པ༌[^1270]དང་བསྒོམས་པ་ལས་བྱུང་བ་དང་། སྐྱེས་ནས་ཐོབ་པ་རྣམས་སོ། །

[Block 2419]
བསམས་པ་ལས་བྱུང་བ་ནི་མེད་དོ། །

[Block 2420]
གང་གི་ཚེ་དེ་དག་སེམས་པར་རྩོམ་པ་དེའི་ཚེ་དེ་དག་གི་ཏིང་ངེ་འཛིན་ཁོ་ན་ཉེ་བར་གནས་པ་ཡིན་ནོ། །

[Block 2421]
གཟུགས་མེད་པའི་ཁམས་ན་ནི་བསྒོམས་པ་ལས་བྱུང་བ་དང་། སྐྱེས་ནས་ཐོབ་པ་དག་གོ། །

[Block 2422]
དེ་ལ་སྐྱེས་ནས་ཐོབ་པ་དག་མ་གཏོགས་པ་ཡིད་ལ་བྱེད་པ་རྣམ་པ་ལྔའི་མཇུག་ཐོགས་སུ་འཕགས་པའི་ལམ་མངོན་དུ་འགྱུར་ཏེ། སྦྱོར་བ་ལ་རག་ལུས་པའི་ཕྱིར་རོ། །

[Block 2423]
ལམ་གྱི་མཇུག་ཐོགས་སུ་ནི་འདོད་པ་ན་སྤྱོད་པའི་སྐྱེས་ནས་ཐོབ་པ་ཡང་མངོན་དུ་འགྱུར་ཏེ། གསལ་བའི་ཕྱིར་རོ། །

[Block 2424 [HEADING]]
#### སེམས་གང་ལ་དུ་ཞིག་རྙེད་པ། ^2-5-7-0

[Block 2425]
གང་དག་སེམས་བཅུ་གཉིས་བཤད་པ་དེ་དག་ལས་སེམས་གང་ལ་དུ་ཞིག་རྙེད་ཅེ་ན།

[Block 2426 [VERSE]]
ཁམས་གསུམ་པ་ཡི་ཉོན་མོངས༌[^1271]ཅན། །
དྲུག་དང་དྲུག་དང་གཉིས་རྙེད་དོ། །

[Block 2427]
འདོད་པ་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་ཅན་གྱི་སེམས་མངོན་དུ་གྱུར་ན། སེམས་དྲུག་པོ་འདི་དག་དང་མི་ལྡན་པ་ལས་རྙེད་དེ། ཐེ་ཚོམ་གྱིས་དགེ་བའི་རྩ་བའི་ཉིང་མཚམས་སྦྱོར་བ་དང་། ཁམས་སུ་སླར་ལྡོག་པ་ལས་འདོད་པའི་ཁམས་ཀྱི་དགེ་བ་དང་། ཁམས་སུ་སླར་ལྡོག་པ་དང་། ཡོངས་སུ་ཉམས་པ་ལས་མི་དགེ་བ་དང་། བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་དག་དང་། གཟུགས་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་ཅན་དང་། ཡོངས་སུ་ཉམས་པ་ལས་གཟུགས་མེད་པ་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་ཅན་དང་། སློབ་པའོ། །

[Block 2428]
གཟུགས་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་ཅན་ལ་ཡང་དྲུག་རྙེད་དེ། ཁམས་སུ་སླར་ལོག་པ༌[^1272]ལས་གཟུགས་ན་སྤྱོད་པ་གསུམ་དང་། འདོད་པ་ན་སྤྱོད་པའི་མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་དང་། ཡོངས་སུ་ཉམས་པ་ལས་གཟུགས་མེད་པ་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་ཅན་དང་། སློབ་པའོ། །

[Block 2429]
གཟུགས་མེད་པ་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་ཅན་ལ་ནི་གཉིས་རྙེད་དེ། ཡོངས་སུ་ཉམས་པ་ལས་ཉོན་མོངས་པ་ཅན་དེ་ཉིད་དང་། སློབ་པའོ། །

[Block 2430]
གཟུགས་སྐྱེས་དགེ་ལ་གསུམ་དག་གོ། །

[Block 2431]
གཟུགས་ན་སྤྱོད་པའི་དགེ་བ་ལ་སེམས་གསུམ་རྙེད་དེ། དགེ་བ་དེ་ཉིད་དང་། འདོད་པ་དང་གཟུགས་ན་སྤྱོད་པའི་མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་དག་གོ། །

[Block 2432]
སློབ་པ་ལ་བཞི། སློབ་པ་དེ་ཉིད་དང་། འཕགས་པའི་ལམ་གྱིས་འདོད་པ་དང་གཟུགས་ཀྱི་ཁམས་ལས་འདོད་ཆགས་དང་བྲལ་བར་བྱེད་པ་ན་འདོད་པ་དང་གཟུགས་ན་སྤྱོད་པའི་མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་དག་དང་། གཟུགས་མེད་པའི་དགེ་བའོ། །

[Block 2433]
ལྷག་མ༌[^1273]དེ། ལྷག་མར་བྱས་པས་ལྷག་མ་སྟེ། །སེམས་གང་ལ་རྙེད་པ་མ་བཤད་པ་དེ་ལ་ནི་དེ་ཉིད་རྙེད་པར་བལྟ་བར༌[^1274]བྱའོ། །

[Block 2434]
གཞན་དག་ལ༌[^1275]ནི་ཁྱད་པར་མེད་པར་ཉོན་མོངས༌[^1276]ཅན་གྱི་སེམས་ལ་ནི།

[Block 2435 [VERSE]]
མཁས་པ་རྣམས་ཀྱི༌[^1277]དགུ་རྙེད་བརྗོད། །
དགེ་བའི་སེམས་ལ་དྲུག་ཡིན་ཏེ། །
ལུང་མ་བསྟན་ལ་དེ་ཉིད་དོ། །

[Block 2436]
ཞེས་འཆད་དེ། དེར་མི་དགེ་བའི་སེམས་ལ་བདུན་ཡིན་ཏེ། ཞེས་བརྗོད་པར་བྱ་སྟེ། ཡང་དག་པའི་ལྟ་བས་དགེ་བའི་རྩ་བའི་ཉིང་མཚམས་སྦྱོར་བ་ལས་འདོད་པ་ན་སྤྱོད་པའི་དགེ་བ་དང་འདོད་ཆགས་དང་བྲལ་བ་ལས་འདོད་པ་དང་གཟུགས་ན་སྤྱོད་པའི་མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་དག་དང་། དེ་ནི༌[^1278]ཡོད་པའི་ཏིང་ངེ་འཛིན་དེ་ཐོབ་པ་ལས་གཟུགས་དང་གཟུགས་མེད་པ་ན་སྤྱོད་པའི་དགེ་བ་དག་དང་།

[Block 2437 [VERSE]]
ངེས་འཇུག་དགྲ་བཅོམ་ཉིད་ཀྱི་ཚེ། །
སློབ་པ་དང་ནི་མི་སློབ་པའོ། །

[Block 2438]
ལྷག་མ་ནི་རྣམ་པར་བཤད་པ་འདི་ཉིད་ཀྱིས༌[^1279]ཁོང་དུ་ཆུད་པར་བྱའོ། །

[Block 2439]
བསྡུ་བའི་ཚིགས་སུ་བཅད་པ་ནི།

[Block 2440 [VERSE]]
སྐྱེ་དང་སྙོམས་པར༌[^1280]འཇུག་པ་དང་། །
འདོད་ཆགས་བྲལ་དང་ཡོངས་ཉམས་དང་། །
དགེ་བའི་ཉིང་མཚམས་སྦྱོར་བའི་ཚེ། །
སེམས་དེ་ལྡན་པ་མིན་ལས་རྙེད། །

[Block 2441]
རྐྱེན་གྱི་སྐབས་རྫོགས་སོ།། །།

[Block 2442]
དབང་པོ་བསྟན་པ་ཞེས་བྱ་བ་མཛོད་ཀྱི་བཤད་པ་ལས་གནས་གཉིས་པ་རྫོགས་སོ།། །།

[Block 2443 [HEADING]]
## འཇིག་རྟེན་བསྟན་པ། ^3-0

[Block 2444 [HEADING]]
### སེམས་ཅན་གྱི་འཇིག་རྟེན། ^3-1-0

[Block 2445 [HEADING]]
#### འདོད་པ་དང་གཟུགས་དང་གཟུགས་མེད་པའི་ཁམས། ^3-1-1-0

[Block 2446]
ད་ནི་འདོད་པ་དང་གཟུགས་དང་གཟུགས་མེད་པའི་ཁམས་ཀྱི་ངེས་པ་ཉིད་ཀྱི་སེམས་ལ་སོགས་པ་བསྟན་པ་བྱས་པ་དེ་ལ། འདོད་པ་དང་གཟུགས་དང་གཟུགས་མེད་པའི་ཁམས་དེ་དག་གང་ཡིན་པ་བརྗོད་པར་བྱ་སྟེ། དེའི་ཕྱིར།

[Block 2447 [VERSE]]
དམྱལ་བ་ཡི་དགས་དུད་འགྲོ་དང་། །
མི་རྣམས་དང་ནི་ལྷ་དྲུག་དག །

[Block 2448]
འདོད་པའི་ཁམས་ཡིན་ཞེས་བྱ་བ་འདི་སྨོས་ཏེ། འགྲོ་བ་བཞི་དང་། ལྷའི་རིས་དྲུག་པོ་འདི་ལྟ་སྟེ། རྒྱལ་ཆེན་བཞི་པོ༌[^1281]རྣམས་དང་། སུམ་ཅུ་རྩ་གསུམ་པ་རྣམས༌[^1282]དང་། འཐབ་བྲལ་བ་རྣམས༌[^1283]དང་། དགའ་ལྡན་པ་རྣམས་དང་། འཕྲུལ་དགའ་བ་རྣམས་དང་། གཞན་འཕྲུལ་དབང་བྱེད་པ་རྣམས་ཏེ། དེ་ལྟར་ན་དེ་དག་སྣོད་ཀྱི་འཇིག་རྟེན་དང་བཅས་པ་ནི་འདོད་པའི་ཁམས་ཡིན་ནོ། །

[Block 2449]
དེ་ལ་གནས་དུ་ཞིག་ཡོད་ཅེ་ན། དམྱལ་བ་དང་། གླིང་དབྱེ་བ་ལས་དེ་ཉི་ཤུ་ཞེས་བྱ་བ་སྨོས་ཏེ། གནས་རྣམས༌[^1284]ཞེས་བྱ་བའི་ཚིག་གི་ལྷག་མ་དང་སྦྱར༌[^1285]རོ། །

[Block 2450]
དམྱལ་བ་ཆེན་པོ་བརྒྱད་ཡོད་དེ།[^1286] ཡང་སོས་དང་། ཐིག་ནག་དང་། བསྡུས་འཇོམས་དང་། ངུ་འབོད་དང་། ངུ་འབོད་ཆེན་པོ་དང་། ཚ་བ་དང་། རབ་ཏུ་ཚ་བ་དང་། མནར་མེད་པ་དང་། གླིང་བཞི་སྟེ། འཛམ་བུའི་གླིང་དང་། ཤར་གྱི་ལུས་འཕགས་གླིང་དང་། ནུབ་ཀྱི་བ་ལང་སྤྱོད་དང་། བྱང་གི་སྒྲ་མི་སྙན་དང་། བཤད་མ་ཐག་པའི་ལྷའི་རིས་དྲུག་དང་། ཡི་དྭགས་རྣམས་དང་། དུད་འགྲོ་སྟེ། དེ་ལྟར་ན་གཞན་འཕྲུལ་དབང་བྱེད་པ་དག་ནས་མནར་མེད་པའི་བར་གྱི་གནས་ཉི་ཤུ་པོ་དེ་དག་ནི་འདོད་པའི་ཁམས་ཡིན་ནོ། །

[Block 2451]
སྣོད་དང་བཅས་པར་བཟུང་ན་ནི་རླུང་གི་དཀྱིལ་འཁོར་གྱི་བར་ཡིན་ནོ། །

[Block 2452]
འདོད་པའི་ཁམས་འདིའི། གོང་མའི་གནས་དག་བཅུ་བདུན་ནི། །གཟུགས་ཁམས་ཡིན། ཇི་ལྟ་ཞེ་ན། དེར་སོ་སོའི། བསམ་གཏན་ས་ནི་གསུམ་པ་ཡིན། །ཞེས་བྱ་བ་སྨོས་ཏེ། བསམ་གཏན་དང་པོ་དང་།

[Block 2453]
གཉིས་པ་དང་།

[Block 2454]
གསུམ་པ་དག་ན༌[^1287]རེ་རེ་ཞིང་ས་གསུམ་པ་དག་ཡིན་ནོ། །

[Block 2455]
བཞི་པ་ས་ནི་བརྒྱད་པ་ཡིན། །དེ་ལ་བསམ་གཏན་དང་པོ་ནི་ཚངས་རིས་རྣམས་དང་། ཚངས་པའི་མདུན་ན་འདོན་རྣམས་དང་། ཚངས་ཆེན་རྣམས་སོ། །
--- END BLOCKS ---
