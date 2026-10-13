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
[Block 71 [HEADING]]
#### ཡིད་ཀྱིས་བྱས་པ། ^1-1-2-0

[Block 72 [HEADING]]
##### དང་པོ་བདག་པོ་མེད་ཅིང་གཞན་གྱིས་ཡོངས་སུ་མ་བཟུང་བའི་རྫས། ^1-1-2-1-0

[Block 73]
ཡིད་ཀྱིས༌[^38]བྱས་པ་ལ་གཉིས་ཏེ། དང་པོ་ནི་ཕྱོགས་བཅུའི་འཇིག་རྟེན་ཁམས་ཀྱི༌[^39]བདག་པོ་མེད་ཅིང་། གཞན་གྱིས༌[^40]ཡོངས་སུ་མ་བཟུང་བའི་རྫས་ཕུལ་དུ་བྱུང་བ་མ་ལུས་པ་སྟེ། ཇི་ལྟར་འཕགས་པ་དཀོན་མཆོག་སྤྲིན་དང་། འཕགས་པ་དགོངས་པ་རྒྱུད་ཀྱི་ཕྲེང་བ་དང་། ཏིང་ངེ་འཛིན་གྱི་འཁོར་ལོའི་མཆོད་པའི་ཕྱག་རྒྱའི་མདོ་དང་། དཀོན་མཆོག་ཏ་ལ་ལའི་མདོ་དང་། སྤྱོད་པ་ལ་འཇུག་པ་ལས་གསུངས་པ་ལྟ་བུའོ། །

[Block 74 [HEADING]]
##### གཉིས་པ་ཡིད་ཀྱི་རྣམ་པར་འཕྲུལ་པ་ལས་བྱུང་བའི་བཀོད་པ། ^1-1-2-2-0

[Block 75]
གཉིས་པ་ནི་ཡིད་ཀྱི༌[^41]རྣམ་པར་འཕྲུལ་པ་ལས་བྱུང་བའི་བཀོད་པ་ནམ་མཁའི་མཛོད་ལས་བྱུང་བ་སྟེ། འདི་ལྟར་འཁོར་ལོས༌[^42]སྒྱུར་བའི་རྒྱལ་སྲིད་རིན་པོ་ཆེ་བདུན་དང་། ནོར་བུ་རིན་པོ་ཆེ་གསེར་དང་། དངུལ་དང་། དུང་དང་། མན་ཤེལ་དང་། ཆུ་ཤེལ་དང་། སྤུག་དང་། རྡོའི་སྙིང་པོ་དང་། མུ་ཏིག་དང་། མུ་ཏིག་དམར་པོ་དང་། མན་ཤེལ་དང་། པདྨ་རཱ་ག་དང་། ཨསྨ་གརྦྷ་དང་། མུ་ས་ལ་གལ༌[^43]པ་དང་། དུན་ལས་དང་། ཨིནྡྲ་ནཱི་ལ་དང་། མར་ཀ་ཏ་དང་། བཻ་ཌཱུརྱ་དང་། ཤཾ་ཀ་ཤི་ལ་དང་། བྱི་རུ༌[^44]དང་། ཀེ་ཀེ་རུ་དང་། ཀེ་ཀེ་རུ་ཆེན་པོ་ལ་སོགས་པའི་ནོར་བུ་དེ་དག་གི་ཆར་པ་འབབ་པ་དང་། དེ་དག་གི་གདུགས་དང་། རྒྱལ་མཚན་དང་། བ་དན་དང་། གཞལ་ཡས་ཁང་དང་། དྲ་བའི་ཚོགས་བརྗོད་དུ་མེད་པ་དག་གཞན་ཡང་དཀོན་མཆོག་ཏ་ལ་ལའི་གཟུངས་ལས་འབྱུང་བ་ལྟ་བུ་སྟེ།

[Block 76 [VERSE]]
མེ་ཏོག་ཕལ་ཆེར་མེ་ཏོག་བླ་རེ་དང་། །
མེ་ཏོག་བཀོད་པའི་འོད་ཟེར་རབ་འགྱེད་ཅིང་། །
མེ་ཏོག་སྣ་ཚོགས་ཀུན་དུ་བཀྲམ་བྱས་ཏེ། །
བདག་ཉིད་ཆེན་པོ་དེ་དག་རྒྱལ་བས༌[^45]མཆོད། །

[Block 77]
ཅེས་གསུངས་ཏེ། དེ་བཞིན་དུ་བདུག་པ་དང་། སྤོས་དང་། ཕྲེང་བ་དང་། ཕྱེ་མ་དང་། ན་བཟའ་དང་། རིན་པོ་ཆེ་དང་། པདྨ་དང་། རྒྱན་ཕྲེང༌[^46]དང་། རྒྱལ་མཚན་ཏེ། དེ་དག་ཀྱང་ཁ་དོག་སྣ་ཚོགས་པའོ། །

[Block 78]
སྔར་གྱི་ཚིགས་སུ་བཅད་པས་ཀུན་ལ་སྦྱར་བར་བྱའོ། །

[Block 79]
དེ་བཞིན་དུ་གདུགས་བཟོ་ལེགས་པ་ཡུ་བ་རིན་པོ་ཆེ་ལས་གྲུབ་པ་ཁ་དོག་སྣ་ཚོགས་པ་སངས་རྒྱས་ཀྱི་ཞིང་མ་ལུས་པ་ཁེབས་པ་བརྗོད་དུ་མེད་པ་དང་། དེ་བཞིན་དུ་རྒྱལ་མཚན་ཡང་དེ་བཞིན་ཏེ། ཐམས་ཅད་གདུགས་བཞིན་ནོ། །

[Block 80]
བ་དན་དང་རྣམ་པར་རྒྱལ་བའི་བ་དན་ཡང་ཚད་དང་རྒྱུ་དང་གྲངས་སྔ་མ་བཞིན་ནོ། །

[Block 81]
གཞན་ཡང་མེ་ཏོག་ཁ་དོག་དང་དབྱིབས་དང་དྲི་ཕུན་སུམ་ཚོགས་པའི་ཆར་དང་། དེའི་ཕྲེང་བ་དང་། དེའི་གདུགས་དང་། དེའི་རྒྱལ་མཚན་དང་། དེའི་བ་དན་དང་། རྣམ་པར་རྒྱལ་བའི་བ་དན་དང་། གཞལ་མེད་ཁང་བཀོད་པ་སྣ་ཚོགས་པ་དུ་མ་བརྗོད་དུ་མེད་པ་དང་། མར་མེ་ཡང་ཚུལ་དེ་བཞིན་པ་དང་། སྤོས་ཀྱི་ཆར་ལ་སོགས་པ་ཡང་སྔ་མའི་ཚུལ་དང་ལྡན་པ་དང་། ཞལ་ཟས་བཟའ་བ་དང་། བཏུང་བ་ཁ་དོག་དང་དྲི་དང་རོ་ཕུན་སུམ་ཚོགས་པ་དང་། ན་བཟའ་དྲི་ཞིམ་པོས་བསྒོས་པ་དང་། རོལ་མོའི་སྒྲ་དབྱངས་སྙན་ཅིང་ཡིད་འཕྲོག་པར་བྱེད་པའི་པི་ཝང་དང་། གླིང་བུ་དང་། རྔ་དང་། རྔ་པ་ཊ་ཧ་དང་། རྔ་བོ་ཆེ་དང་། རྔ་ཟླུམ་དང་། རྫ་རྔ་དང་། དུང་དང་། ཟངས་དུང་དང་། ཆ་ལང་དང་། ཏིང་ཏིང་ཤག་དང་། ཌ་མ་རུ་དང་། ལྷ་དང་། མིའི་གླུ་སྙན་པ་ཡིད་འཕྲོག་པར་བྱེད་པ་དང་། དཀོན་མཆོག་གསུམ་གྱི་བསྟོད་པའི་སྒྲ་དབྱངས་སྙན་ཅིང་དོན་དང་ལྡན་པ་དང་ཕྱེ་མའི་ཕུར་མ་རི་རབ་བྱེ་བ་ཕྲག་བརྒྱ་གཅིག་ཏུ་བསྡོམས་པ༌[^47]ཙམ་ལ་སོགས་པའོ། །

[Block 82]
དེ་ཡང་འཕགས་པ་དཀོན་མཆོག་སྤྲིན་ལས་འབྱུང་བ་བཞིན་ནོ། །

[Block 83 [HEADING]]
### སྒྲུབ་པའི་མཆོད་པ། ^1-2-0

[Block 84]
སྒྲུབ་པའི་མཆོད་པ་ནི་གཉིས་ཏེ། སྒྲུབ་པའི་མཆོད་པ་ཉིད་དང་། བླ་ན་མེད་པའི༌[^48]མཆོད་པའོ། །

[Block 85 [HEADING]]
#### དང་པོ་སྒྲུབ་པའི་མཆོད་པ་ཉིད། ^1-2-1-0

[Block 86]
དང་པོ་ལ་བདུན་ཏེ། ཕྱག་འཚལ་བའི་མཆོད་པ་དང་། ཟང་ཟིང་གི་མཆོད་པའི་མཆོད་པ་དང་། སྡིག་པ་བཤགས་པའི་མཆོད་པ་དང་། རྗེས་སུ་ཡི་རང་བའི་མཆོད་པ་དང་། དེ་བཞིན་དུ་བསྐུལ་བ་དང་། གསོལ་བ་གདབ་པ་དང་། ཡོངས་སུ་བསྔོ་བའི་མཆོད་པ་ཞེས་བྱ་བ་དག་གོ། །

[Block 87 [HEADING]]
##### ཕྱག་འཚལ་བའི་མཆོད་པ། ^1-2-1-1-0

[Block 88]
དེ་ལ་ཕྱག་འཚལ་བའི་མཆོད་པ་ལ་ཡང་གཉིས་ཏེ། ལུས་ཀྱི་མཆོད་པ་དང་། ངག་གི་མཆོད་པའོ། །

[Block 89 [HEADING]]
###### ལུས་ཀྱི་མཆོད་པ། ^1-2-1-1-1-0

[Block 90]
ལུས་ཀྱི་མཆོད་པ་ནི་འཕགས་པ་བཟང་པོ༌[^49]སྤྱོད་པ་ལས།

[Block 91]
ཇི་སྙེད་སུ་དག་ཅེས་པ་ལ་སོགས་པ་དང་། བཟང་པོའི་སྤྱོད་ལ་དད་པའི་སྟོབས་དག་གིས། །ཞེས་པ་ལ་སོགས་པ་དང་། རྡུལ་གཅིག་སྟེང་ན་རྡུལ་སྙེད་ཅེས་པ་ལ་སོགས་པའོ། །

[Block 92]
དེ་དག་གིས༌[^50]ནི་དམིགས་པའི་ཡུལ་དུ་བྱ་བ་དང་། ལུས་དབུལ་བ་དང་། ཕྱག་བྱ་བ་དེ་གསུངས་སོ། །

[Block 93]
དོན་དེ་ཉིད་འཕགས་པ་ཕུང་པོ་གསུམ་པའི་མདོ་ལས་གསུངས་ཏེ། དེ་པུས་མོ་གཡས་པ་ས་ལ་འཛུགས་པ་ན་ཞེས་པ་དང་། དེ་པུས་མོ་གཡོན་པ་ས་ལ་འཛུགས་པ་ན་ཞེས་པ་དང་། དེ་ལག་པ་གཡས་པ་ས་ལ་འཛུགས་པ་ན་སེམས་ཅན་ཐམས་ཅད་གཡས་ཕྱོགས་ཀྱི་ལམ་ལ་གནས་པར་གྱུར་ཅིག་སྙམ་དུ་སེམས་བསྐྱེད་དོ་ཞེས་པ་དང་། དེ་བཞིན་དུ་ལག་པ་གཡོན་པ་དང་མགོ་ས་ལ་གཏུགས་པ་ན་ཞེས་པའི་ཚུལ་དེ་བཞིན་དུ་ཤེས་པར་བྱ། དེའི་བསྔོ་བ་དེ་ཉིད་ལས་འདི་སྐད་དུ་བདག་གི་ཡན་ལག་ལྔས་ཕྱག་བཙལ་བ་འདིས་སེམས་ཅན་ཐམས་ཅད་ཀྱི་སྒྲིབ་པ་ལྔ་སེལ་བར་གྱུར་ཅིག །

[Block 94]
མིག་ལྔ་ཡོངས་སུ་དག་པར་གྱུར་ཅིག །དབང་པོ་ལྔ་ཡོངས་སུ་རྫོགས་པར་གྱུར་ཅིག །

[Block 95]
ལམ་ལྔ་ལ་གནས་པར་གྱུར་ཅིག །མངོན་པར་ཤེས་པ་ཉམས་པ་མེད་པ་ལྔ་ཐོབ་པར་གྱུར་ཅིག །སེམས་ཅན་འགྲོ་བ་ལྔར་སྐྱེས་པ་དག་འགྲོ་བ་ལྔ་ལས་ཁྱད་པར་དུ་འཕགས་པ་དང་། ཚུལ་ཁྲིམས་ཁྱད་པར་དུ་འཕགས་པ་དང་། ཏིང་ངེ་འཛིན་ཁྱད་པར་དུ་འཕགས་པ་དང་། ཤེས་རབ་ཁྱད་པར་དུ་འཕགས་པ་དང་། རྣམ་པར་གྲོལ་བ་ཁྱད་པར་དུ་འཕགས་པ་དང་། རྣམ་པར་གྲོལ་བའི་ཡེ་ཤེས་མཐོང་བ་ཁྱད་པར་དུ་འཕགས་པ་ཐོབ་པར་གྱུར་ཅིག །སངས་རྒྱས་ལ་ལྟ་བ་དང་། ཆོས་ཉན་པ་དག༌[^51]དགེ་འདུན་དང་འགྲོགས་པ་ཐོབ་པར་གྱུར་ཅིག་ཅེས་གསུངས་པ་ལྟ་བུའོ། །

[Block 96 [HEADING]]
###### ངག་གིས་མཆོད་པ། ^1-2-1-1-2-0

[Block 97]
ངག་གིས༌[^52]མཆོད་པ་ཡང་ལུས་ཀྱིས༌[^53]ཕྱག་བྱེད་པའི་དུས་དེ་ཉིད་ཀྱི་ཆོ་ག་རྟོགས་པ་ཅི་ཡོད་པས་དཀོན་མཆོག་གསུམ་གྱི་བསྟོད་པ་གླུ་དབྱངས་ཀྱིས་ཚིག་ཏུ་འདོན་ཅིང་ཕྱག་བྱེད་པའོ། །

[Block 98 [HEADING]]
##### ཟང་ཟིང་གི་མཆོད་པའི་མཆོད་པ། ^1-2-1-2-0

[Block 99]
ཟང་ཟིང་གི་མཆོད་པ་ནི་སྔར་བརྗོད་ཟིན་ཏོ།། །།

[Block 100 [HEADING]]
##### སྡིག་པ་བཤགས་པའི་མཆོད་པ། ^1-2-1-3-0

[Block 101]
སྡིག་པ་བཤགས་པའི་མཆོད་པ་ནི་གསེར་འོད་དམ་པའམ། ལྟུང་བ་བཤགས་པའམ། ཕུང་པོ་གསུམ་པའི་མདོའམ། ལས་ཀྱི་སྒྲིབ་པ་རྒྱུན་གཅོད་པ་ལ་སོགས་པའོ། །

[Block 102]
སྡིག་པ་བཤགས་པ་དེ་ཡང་མཆོད་པ་ཉིད་ཡིན་ཏེ།

[Block 103]
ཇི་སྐད་དུ་འཕགས་པ་བློ་གྲོས་མི་ཟད་པས་བསྟན་པའི་མདོ་ལས།

[Block 104]
བདག་དང་གཞན་གྱི་སྡིག་པ་བཤགས་པ་ཡང་བསོད་ནམས་སུ་འགྱུར་རོ་ཞེས་གསུངས་སོ། །

[Block 105 [HEADING]]
##### རྗེས་སུ་ཡི་རང་བའི་མཆོད་པ། ^1-2-1-4-0

[Block 106]
རྗེས་སུ་ཡི་རང་བའི་མཆོད་པ་ཡང་འཕགས་པ་ཟླ་བ་སྒྲོན་མའི་མདོ་ལས་འབྱུང་བ་བཞིན་ཏེ་མཆོད་པ་ཉིད་ཡིན་ནོ། །

[Block 107 [HEADING]]
##### བསྐུལ་བ། ^1-2-1-5-0

[Block 108]
བསྐུལ་བ་དང་།

[Block 109 [HEADING]]
##### གསོལ་བ་གདབ་པའི་མཆོད་པ། ^1-2-1-6-0

[Block 110]
གསོལ་བ་གདབ་པའི་མཆོད་པ་དང་།
--- END BLOCKS ---
