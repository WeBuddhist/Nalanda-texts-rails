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
[Block 2696]
ལྗགས་རིང་ཞིང་སྲབ་པ་ཞེས་བྱ་བ་རིང་བ་ནི་ཆེ་བའམ་ཁྲུན་རིང་བའོ། །

[Block 2697]
སྲབ་པ་ནི་མཉེན་པའོ། །

[Block 2698]
ཚངས་པའི་དབྱངས་ཞེས་བྱ་བ་ནི་ཚངས་པའི་དབྱངས་དང་མཚུངས་པའམ། དབྱངས་མཆོག་ཡིན་པའི་ཕྱིར་ཏེ། བྱ་ཀ་ལ་པིང་ཀའི་གསུང་ཞེས་བྱ་བ་ནི༌[^1935]བྱ་ཀུ་ར་བའི༌[^1936]སྐད་ལྟ་བུའོ། །

[Block 2699]
ཟླ་བའི་དཀྱིལ་འཁོར་མ་ཉ་བ་ཚེས་བཅུ་གཉིས་ཀྱི༌[^1937]ཤས་འདྲ་བར་འགྲམ་པའི་མཐའ་ཤ་མཁྲེགས་ཤིང་ལེགས༌[^1938]པར་ཟླུམ་པའི་ཕྱིར་འགྲམ་པ་སེང་གེའི་ལྟ་བུའོ། །

[Block 2700]
སྐར་མ་པ་བ་སངས་པས༌[^1939]ཀྱང་ལྷག་པར་འོད་གསལ་ཞིང་དཀར་བའི་ཕྱིར་ཚེམས་ཤིན་ཏུ་དཀར་བའོ། །

[Block 2701]
མཐོན་དམན་དང་མི་མཉམ་པ་མེད་པའི་ཕྱིར་ཚེམས་མཉམ་པའོ། །

[Block 2702]
ཚེམས་ཀྱི་མཚམས་དོད་པ་ལ་སོགས་པ་མེད་ཅིང་སྡུག་པའི་ཕྱིར་ཚེམས་ཐགས་བཟང་བའོ། །

[Block 2703]
མི་གཞན་དག་གི་སོ་ནི་སུམ་ཅུ་རྩ་གཉིས་སམ་ཉི་ཤུ་རྩ་བརྒྱད་ཡོད་ཀྱི། དེ་ལས་བཟློག་པ་ནི་གྲངས་བཞི་བཅུ་ཚང་བའི་ཕྱིར་ཚེམས་བཞི་བཅུ༌[^1940]མངའ་བའོ། །

[Block 2704]
སྤྱན་མཐོན་མཐིང་ཞེས་བྱ་བ་ནི། སྤྱན་གྱི་དཀྱིལ་འཁོར་གྱི༌[^1941]ནང་གི་འབྲས་བུ་སྣུམ་ཞིང་གནག་པ་སྟེ། འབྲས་བུ་ནག་པོའི་མཐའ་གཉིས་དཀར་ལ། རྫི་མ་གཉིས༌[^1942]གནས་པའི་སྐབས་སྣུམ་ཞིང་མཐིང་ཀར་འདུག་པ། གྲྭ་གཉིས་ཆུང་ཟད༌[^1943]དམར་བ། རྫི་མ་དང་སྤྱན་གྱི་བར་གསེར་གྱི་མདོག་ལྟ་བུ་སྟེ། དེ་ལྟར་དང་བ་རྣམ་པ་ལྔ་དང་ལྡན་དུ་ཟིན་གྱིས་ཀྱང་སྤྱན་གྱི་དཀྱིལ་གཙོ་བོ་ཡིན་པའི་ཕྱིར་སྤྱན་མཐོན་མཐིང་ཞེས་བྱའོ། །

[Block 2705]
བེའུ་འབྲངས་མ་ཐག་པ་གཞོན་ནུའི་རྫི་མ་དང་འདྲ་བར་རྫི་མ་བླ་འོག་གི་མདོག་ཤིན་ཏུ་སྣུམ་ཞིང་མ་འཛིངས་པའི་ཕྱིར་བའི་རྫི་མ་ལྟ་བུའོ།། །།

[Block 2706 [HEADING]]
###### དཔེ་བྱད་བཟང་པོ་བརྒྱད་ཅུ། ^1-2-7-55-9-0

[Block 2707]
བམ་པོ་ཉི་ཤུ༌[^1944]དྲུག་པ། དཔེ་བྱད་བཟང་པོ་བརྒྱད་ཅུ་ཞེས་བྱ་བ་ནི་མཚན་རྣམས་རྗེས་སུ་འབྱེད་པར་བྱེད་པའམ། མཚན་དང་རྗེས་སུ་མཐུན་པར་ཕྱེ་སྟེ། སྐྱེས་བུ་ཆེན་པོ་ཡིན་པར་སྟོན་པའམ། རྗེས་སུ་མཐུན་པར་མཛེས་པར་བྱེད་པའི་ཕྱིར་དཔེ་བྱད་བཟང་པོ་ཞེས་བྱའོ། །

[Block 2708]
སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས་སེན་མོ་ཟངས་ཀྱི་མདོག་ལྟ་བུ་ཡིན་ཞེས་བྱ་བས་དཔེ་བྱད་བཟང་པོ་བསྟན་ཏོ། །

[Block 2709]
འདུ་བྱེད་ཐམས་ཅད་ལས་དབེན་པ་ཞེས་བྱ་བ་ནི་དེའི་རྒྱུ་མཐུན་པ་སྟེ། དེ་བཞིན་དུ་ཐམས་ཅད་ལ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 2710]
ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་པོ་དེ་དག་གིས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོས་སྙན་པར་སྨྲ་བས་སེམས་ཅན་རྣམས་སྡུད་དོ་ཞེས་བྱ་བ་ནི་ཚིག་སྙན་པ་རྣམས་ཀྱིས་བཙུད་ནས། ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་པོ་དག་གིས་སྡུད་པར་བྱེད༌[^1945]པ་སྟེ། དེ་བས་ན་སྙན་པར་སྨྲ་བར་བགྲང་ངོ་། །ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་པོ་དེ་དག་ཉིད་ཀྱིས་དོན་སྤྱད་པས་སེམས་ཅན་རྣམས༌[^1946]སྡུད་དོ་ཞེས་བྱ་བ་ནི་དོན་བྱ་བའི་བསམ་པས་དེ་སྔོན་དུ་བཏང་བས་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་པོ་དག་གིས་སྡུད་པ་སྟེ། དེ་བཞིན་དུ་ཕྱི་མ་རྣམས་ལ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 2711]
ཡི་གེ་གཅིག་མངོན་པར༌[^1947]སྒྲུབ་པ་ལ་མཁས་པར་གྱིས་ཤིག་ཅེས་བྱ་བ་ནི་གཟོད་མ་ནས་མ་སྐྱེས་པའི་ཕྱིར་ཨ༌[^1948]ནི་ཆོས་ཐམས་ཅད་ཀྱི་སྒོའོ་ཞེས་བྱ་བ་ལ་སོགས་པ༌[^1949]ཡི་གེའི་གཟུངས་ཀྱི་སྒོའི་རིམ་པས་ཡི་གེ་གཅིག་གིས་མཚན་མ་མེད་པའི་ཏིང་ངེ་འཛིན་མངོན་པར་སྒྲུབ་པ༌[^1950]ལ་མཁས་པར་བྱ་བའོ། །

[Block 2712]
ཡི་གེ་གཅིག་གིས་ཐམས་ཅད་འགྲིབ་པ་དང་ལྡན་པར་རྗེས་སུ་གཏོགས་པར༌[^1951]གྱིས་ཤིག་ཅེས་བྱ་བ་ནི་འགྲིབ་པ་དང་ལྡན་པས་འགྲིབ་པ་དང་ལྡན་པ་སྟེ། འདུས་བྱས་ཀྱི་ཆོས་རྣམས་ཡོངས་སུ་འགྱུར་བ་དང་ལྡན་པ༌[^1952]ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2713]
ཡི་གེ་གཅིག་ཏུ་ཡི་གེ་བཞི་བཅུ་རྩ་ལྔ་འདུས་པར་སྒོམས༌[^1953]ཤིག་ཅེས་བྱ་བ་ནི་སྐྱེ་བ་མེད་པའི་ཏིང་ངེ་འཛིན་སྒྲུབ་པ་ཨ་ཞེས་བྱ་བའི་ནང་དུ་ཡི་གེ་ཐམས་ཅད་ཀྱི་ཏིང་ངེ་འཛིན་འདུས་པར་སྒོམས༌[^1954]ཤིག་ཅེས་བྱ་བའོ། །

[Block 2714]
ཡི་གེ་བཞི་བཅུ་རྩ་ལྔ་རྣམས་སུ་ཡི་གེ་གཅིག་འདུས་པར་སྒོམས་ཤིག་ཅེས་བྱ་བ་ནི་ཡི་གེ་བཞི་བཅུ་རྩ་ལྔའི་ཏིང་ངེ་འཛིན་ཨ་ཞེས་བྱ་བ་ཉིད་དུ་སྒོམས་ཤིག་ཅེས་བྱའོ། །

[Block 2715]
རབ་འབྱོར་ཆོས་ཐམས་ཅད་ནི་ཡི་གེ་མེད་པའི་རྣམ་པས་སྤྲུལ་པའོ་ཞེས་བྱ་བ་ནི་ཆོས་ཀྱི་དབྱིངས་བརྗོད་དུ་མེད་པའི་རྣམ་པས་བསྐྱེད༌[^1955]ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2716]
ཇི་ལྟར་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་རྣམ་པར་སྨིན་པ་ལས་བྱུང་བའི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྤྱོད་པ་དང་ཞེས་བྱ་བ་ལ་སོགས་པས༌[^1956]འདི་སྐད་གསོལ་ཏེ། གལ་ཏེ་རྣམ་པར་སྨིན་པ་ལས་བྱུང་བ་ལ༌[^1957]སྤྱོད་ན་རྣམ་པར་སྨིན་པ་ལས་བྱུང་བ་རྣམ་པར་མི་རྟོག་པའི་ཕྱིར་སེམས་ཅན་རྣམས་དང་། ཆོས་རྣམས་མི་དམིགས་ཏེ་མི་སྣང་ན་ཆོས་བཤད་པ་ཇི་ལྟར་འབྱུང་། ཡོད་པ་མ་ཡིན་པའི་བྱང་ཆུབ་ཀྱི་ཕྱོགས་ཀྱི་ཆོས་རྣམས་ལ་སྦྱོར་ན་ཇི་ལྟར་ཕྱིན་ཅི་ལོག་ལ་སྦྱོར་བར་མི་འགྱུར་ཞེས་ཞུས་པའོ། །

[Block 2717]
དེ་སྐད་ཞུས་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས༌[^1958]རབ་འབྱོར་དེ་དེ་བཞིན་ནོ་དེ་དེ་བཞིན་ཏེ་ཞེས་བྱ་བ་ལ་སོགས་པས་དེའི་ཚིག་ལ་མངོན་པར་དགྱེས་པར་མཛད་ནས། དེ་ལྟར་ཆོས་དེ་དག་ཐམས་ཅད་སྟོང་པར་མཐོང་ནས་སེམས་ཅན་རྣམས་ལ་ཆོས་སྟོན་ཏེ་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་རབ་འབྱོར་སེམས་ཅན་དང་། ཆོས་རྣམས་སྟོང་པ་དེ་ནི་བདེན་མོད་ཀྱི། འོན་ཀྱང་དེ་དག་སྟོང་པ་ཉིད་དུ་སེམས་ཅན་རྣམས་ཀྱིས་མི་ཤེས་པས། དེ་ཤེས་པར་བྱ་བའི་ཕྱིར་བཅོམ་ལྡན་འདས་ཆོས་སྟོན་ཏེ་ཆོས་སྟོན་པ་ན་ཡང་ཅི་ནས་ཀྱང་སྟོང་པ་ཉིད་དེ་འཁྲུག་པར་མི་འགྱུར་བ་དེ་ལྟར་ཆོས་སྟོན་ཏོ་ཞེས་དེ་སྐད་བསྟན་པ་ཡིན་ནོ། །

[Block 2718]
དེས་ཆོས་ཐམས་ཅད་སྒྲིབ་པ་མེད་པར་ཡང་དག་པར་རྗེས་སུ་མཐོང་ཞེས་བྱ་བ་ནི་ཀུན་བརྟགས་པའི་སྒྲིབ་པ་རྣམས་དང་བྲལ་ཤིང༌[^1959]ཤིན་ཏུ་ཡོངས་སུ་དག་པར་མཐོང་ངོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2719]
དེ་བཞིན་གཤེགས་པའི་སྤྲུལ་པའི་དཔེ་ཡང་རྗེས་སུ་མཐུན་པར་ཟད་དོ། །

[Block 2720]
མ་བཅིངས་མ་གྲོལ་བ་ཞེས་བྱ་བ་ནི་དྲི་མ་དང་བཅས་པའི་གནས་སྐབས་ན་ཆོས་ཉིད་ཀྱི་གཟུགས་ཀུན་བརྟགས་པས་རང་བཞིན་གྱིས་དབེན་པའི་ཕྱིར་མ་བཅིངས་པའོ། །

[Block 2721]
དྲི་མ་མེད་པའི་གནས་སྐབས་ན་ཡང་གློ་བུར་གྱི་རྣམ་པར་བྱང་བ་མེད་པའི་ཕྱིར་མ་གྲོལ་བའོ། །

[Block 2722]
གཟུགས་ཀྱི་མ་བཅིངས་མ་གྲོལ་བ་ཉིད་གང་ཡིན་པ་དེ་གཟུགས་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་མ་བཅིངས་པ་ཉིད་དང་མ་གྲོལ་བ་ཉིད་ཅེས་བྱ་བ་ཡོངས་སུ་གྲུབ་པའི་གནས་སྐབས་ཡིན་ཏེ། དེ་ཀུན་བརྟགས་པའི་གཟུགས་ཀྱི་ངོ་བོ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2723]
ཤིན་ཏུ་རྣམ་པར་དག་པ་ཞེས་བྱ་བ་ནི་རང་བཞིན་ཉིད་ཀྱིས་ཞེས་བྱ་བར་དགོངས་པའོ། །

[Block 2724]
དངོས་པོ་མེད་པ་ཡང༌[^1960]དངོས་པོ་མེད་པ་ལ༌[^1961]མི་གནས་སོ་ཞེས་བྱ་བ་ནི་མི་བརྟེན་པའི་ཕྱིར་ཏེ། དཔེར་ན་ནམ་མཁའ་ལ་ནམ་མཁའ་མི་གནས་པ་ལྟ་བུའོ། །

[Block 2725]
རང་གི་དངོས་པོ་ཡང་དངོས་པོ་མེད་པ་ལ་མི་གནས་ཏེ་མེད་པའི་ཕྱིར། དཔེར་ན་རི་བོང་གི་རྭ་ལ་སོགས་པ་རྣོ་བ་མི་གནས་པ་ལྟ་བུའོ། །

[Block 2726]
གཞན་དག་གི༌[^1962]དངོས་པོ་ཡང་དངོས་པོ་མེད་པའམ། རང་གི་དངོས་པོ་ལ་མི་གནས་ཏེ། གཞན་གྱི་དངོས་པོ་དང་རང་གི་དངོས་པོ་གཉིས་ཀ་ཡང་མེད་པའི་ཕྱིར་རོ། །

[Block 2727]
དེ་བཞིན་དུ་གཞན་དག་ལ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 2728]
འདི་ལྟར་སངས་རྒྱས་བཅོམ་ལྡན་འདས་དེ་དག་དང་། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་དང་། རང་སངས་རྒྱས་རྣམས་དང་། ཉན་ཐོས་རྣམས་ཀྱིས་ཀྱང་ཆོས་རྣམས་ཀྱི་ཆོས་ཉིད་འདི་ཉིད་རྟོགས་ཏེ་ཞེས་བྱ་བས་ནི་ཐམས་ཅད་ཀྱང་ཆོས་མངོན་པར་རྟོགས་པ་གཅིག་པ་ཉིད་དོ་ཞེས་སྟོན་ཏོ། །

[Block 2729]
ཆོས་རྣམས་ཀྱི་ཆོས་ཉིད་དེ་ལས་ཀྱང་མི་འདའོ་ཞེས་བྱ་བ་ནི་ཆོས་འཆད་པའི་ཚེ་དེ་དག་ལས་མི་འདའ་བའོ། །

[Block 2730]
རབ་འབྱོར་ཆོས་ཀྱི་དབྱིངས་ནི་འདའ་བ་མེད་དོ། །

[Block 2731]
དེ་བཞིན་ཉིད་དང་། ཡང་དག་པའི་མཐའ་ནི་འདའ་བ་མེད་དོ་ཞེས་བྱ་བ་ནི་སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས་ཀྱི་ཆོས་ཀྱི་དབྱིངས་ནི་ཆོས་ཀྱི་སྐུ་སྟེ་འདའ་བ་མེད་དོ། །

[Block 2732]
བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་དེ་བཞིན་ཉིད་འདའ་བ་མེད་དོ། །

[Block 2733]
རང་སངས་རྒྱས་དང་། ཉན་ཐོས་རྣམས་ཀྱི་ཡང་དག་པའི་མཐའ་ལ་འདའ་བ་མེད་དོ་ཞེས་བྱ་བར་བྱེ་བྲག་ཏུ་ཕྱེ་སྟེ་གཟུང་བར༌[^1963]བྱའོ། །

[Block 2734]
འདི་ལྟར་དེ་དག་ལ་གང་འདའ་བར་འགྱུར་བའི་རང་བཞིན་མེད་དོ་ཞེས་བྱ་བ་ནི་འདའ་བར་བྱ་བའི་ངོ་བོ་ཉིད་མེད་དོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2735]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ཆོས་ཀྱི་དབྱིངས་དང་། དེ་བཞིན་ཉིད་དང་། ཡང་དག་པའི་མཐའ་ལས༌[^1964]འདའ་བ་མ་མཆིས་ན་ཞེས་བྱ་བ་ལ་སོགས་པས་འདི་སྐད་ཞུས་ཏེ། གཟུགས་དང་ཚོར་བ་ལ་སོགས་པ་ནི་རྣམ་པར་འགྱུར་བའི་ངོ་བོ་ཉིད་ཡིན་པས་འདའ་བར་སྣང་ན། འདི་ལྟར་གཟུགས་ལ་སོགས་པ་ལ་ནི་འདའ་བ་ཡོད་ཀྱི། ཆོས་ཀྱི་དབྱིངས་ལ་སོགས་པ་ལ་ནི༌[^1965]མེད་ན་དེའི་ཚེ་ཅི་གཟུགས་ལ་སོགས་པ་དང་། ཆོས་ཀྱི་དབྱིངས་ལ་སོགས་པ་ལ་ཐ་དད་པ་ཡོད་དམ་ཞེས་ཞུས་པའོ། །
--- END BLOCKS ---
