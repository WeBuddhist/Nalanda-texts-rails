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
[Block 876]
དབང་པོ་དུལ་ཞིང་ཞེས་བྱ་བ་ནི་དབང་པོ་བསྲུང་ཞིང་བསྡམས་པ༌[^485]ཡིན་པར་སྟོན་ཏོ། །

[Block 877]
དགེ་སློང་དཔལ་གྱི་རྗེས་འབྲང་བཞིན། །ཞེས་བྱ་བ་ནི་ཀུན་ཏུ་ལྟ་བ་དང་། རྣམ་པར་ལྟ་བ་དང་། སྣམ་སྦྱར་དང་། ལྷུང་བཟེད་དང་། ཆོས་གོས་འཆང་བ་ལ་སོགས་པ་ཇི་ལྟར་མདོ་སྡེ༌[^486]ལས་གསུངས་པ་བཞིན་དུ་རིག་པར་བྱའོ། །

[Block 878]
བཞི་ཞེས་སྨོས་པས་ནི་དགེ་འདུན་གྱི་ཚོགས་དང་རྗེས་སུ་མཐུན་པར་བསྟན་པའི་ཕྱིར་རོ། །

[Block 879]
འདིས་ནི་སྣོད་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 880]
དང་ཞིང་འཇམ་པ་ཞེས་བྱ་བ་ལ་དང་བ་ནི་དད་པའི་གཞི་སྟེ་འཇམ་པ་ཞེས་བསྟན་པ་ཡིན་ནོ། །

[Block 881]
སྦྱིན་པ་པོའི་ཕུན་སུམ་ཚོགས་པ་ནི་དང་བ་ཞེས་བྱ་བ་ལ་སོགས་པའི༌[^487]ཚིག་གིས་སོ། །

[Block 882]
ཚུལ་ཁྲིམས་ནི་སྔར་བཤད་པ་ཡིན་པས་ཡང་བཤད་པར་བྱ་བ་མ་ཡིན་ཏེ། ཚུལ་དང་ལྡན་ཡང་ནོར་ཙམ་གྱིས་ནི་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 883]
ཕྱག་བྱས་ནས་ཞེས་བྱ་བ་ནི་བཀུར་སྟི་དང་གུས་པ་དང་བཅས་པའི་སྦྱིན་པའོ། །

[Block 884]
བསྙེན་བཀུར་དང་བཅས་པས་བྱིན་པ་ནི་དེ་ཐོབ་པའོ། །

[Block 885]
ཟན་དྲོན་ཙམ་ཞིག་གུས་པར་བྱིན། །ཞེས་བྱ་བ་འདིས་ནི་སྦྱིན་པ་ཆུང་ཞེས་བྱ་བ་གང་ཡང་མེད་དོ། །ཞེས་གོང་དུ་བསྟན་པ་དེ་སྒྲུབ་པ་ཡིན་ནོ། །

[Block 886]
བདག་གི་ཁྱིམ་དུ་གུས་པར༌[^488]ཞེས་བྱ་བ་འདིས་ནི་སྦྱིན་པའི་དངོས་པོ་དག་པར་སྟོན་ཏོ། །

[Block 887]
དེ་ཡི་མྱུ་གུ་ཙམ་ཞིག་བྱུང་། །ཞེས་བྱ་བ་དག་གིས་ནི་གུས་པར་བྱས་ཏེ། བསོད་ནམས་བྱས་པས་བསྙེན་བཀུར་ཐོབ་པར་སྟོན་པ་ཡིན་ནོ། །

[Block 888]
ང་ཡིས་དེ་ལས་བསམས་ནས་ནི། །ཞེས་བྱ་བ་གོང་དུ་བཤད་པ་སྟེ། གང་ཡིན་ཞེ་ན། །རྒྱལ་པོ་ཆེན་པོ་ཅི་ལས་དགོངས། །ཞེས་བྱ་བ་ལ་སོགས་པ་དེ་ཉིད་བཤད་པའོ། །

[Block 889]
བསོད་ནམས་ཀྱིས་ནི་ངོམས་མི་མྱོང་། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཕྱེད་པོ་འདིས་ནི་ལས་ཀྱི་འབྲས་བུ་མངོན་སུམ་དུ་གྱུར་པའི་ཕྱིར་སྦྱིན་པའི་ཞིང་ལ་སྦྱིན་པའི་དངོས་པོ་བྱིན་པས་མི་ངོམས་པར་བསྟན་ཏོ། །

[Block 890]
དགའ་བ་ནི་ཡིད་ཚིམ་པ་སྟེ། བདག་ཉིད་ཀྱིས་ཀྱང་ལས་ཀྱི་འབྲས་བུ་དེ་དང་མཉམ་པར་མངོན་སུམ་དུ་གྱུར་པའི་ཕྱིར་རོ། །

[Block 891]
ངོ་མཚར་ཆེ་བ་ནི་སྦྱིན་པའི་དངོས་པོ་ཆུང་བ་ལས་འབྲས་བུ་ཆེན་པོ་སྟོན་པས་སོ། །

[Block 892]
རབ་ཏུ་གུས་པ་ནི་སླར༌[^489]ཡང་བསོད་ནམས་ལ་བརྩོན་པས་འཇུག་པར་སྟོན་ཏོ། །

[Block 893]
བསོད་ནམས་ཀྱིས་ཞེས་བྱ་བ་ནི་དང་ཞིང་འཇམ་པའི་ཡིད་ཀྱིས་ཞེས་བྱ་བ་ལ་སོགས་པ་གང་གོང་དུ་བསྟན་པ་དེའམ། ཡང་ན། །བདེ་བར་གཤེགས་ལ༌[^490]བཀུར་སྟི་བྱས་པ་ཆུང་ངུ་ཡང་། །ཞེས་བྱ་བའི་ཚིགས་སུ་བཅད་པ་གང་བསྟན་པ་འདི་རུ་བཤད་དོ། །

[Block 894]
མངོན་པར་མཐོ་བའི་ཁྱད་པར་འདི་ལྟ་བུའི་རྣམ་པར་སྨིན་པ་ཞེས་བྱ་བ་ནི། ཤིང་རྟ་སྣ་ཚོགས་རྟ་དང་གླང་པོ་འགྱིང་བ་དང་། །ཞེས་བྱ་བའི་ཚིགས་བཅད་གང་བསྟན་པ་དེས་བསྟན་པ་ཡིན་ཏེ། རྣམ་པར་སྨིན་པ་ཉིད་མངོན་པར་མཐོ་བ་ཡིན་པས་རྣམ་པར་སྨིན་པ་མངོན་པར་མཐོ་བའོ། །

[Block 895]
མངོན་པར་མཐོ་བ་ཉིད་བྱེ་བྲག་ཡིན་པས་ན་མངོན་པར་མཐོ་བའི་ཁྱད་པར་རོ། །

[Block 896]
བསོད་ནམས་ཀྱི་འབྲས་བུ་མངོན་སུམ་དུ་གྱུར་པས་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་གང་གོང་དུ་བསྟན་པའི། །བསོད་ནམས་ཀྱིས་ནི་ངོམས་མི་མྱོང་། །ཞེས་བྱ་བའི་དབང་དུ་བྱས་པ་ཡིན་ནོ། །

[Block 897]
དངོས་སྡིག་མི་མཛད་པ་ཞེས་བྱ་བའི་ལྡོག་པའི་ཚུལ་འདིས་ནི་ཚུལ་ཁྲིམས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བསྟན་ཏོ། །

[Block 898]
སྐྱེ་དགུ་རྣམས་ལ་ཕ་བཞིན་དུ། །ཞེས་བྱ་བས་ནི་བཟོད་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བསྟན་ཏེ། ཁོ་ན་མེད་པའི་ཕྱིར་རོ། །

[Block 899]
བསོད་ནམས་ཀྱི་ཡོན་ཏན་སྒྲུབ་པ་ལ་མངོན་པར་ཕྱོགས་པ་ཞེས་བྱ་བ་འདིས་ནི་བརྩོན་འགྲུས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བསྟན་ཏོ། །

[Block 900]
བསོད་ནམས་ཀྱི་ཡིད་ཡོན་ཏན་ཡིན་པས་གཙོ་བོར་ཡང་དག་པར་བཟུང་བས་སོ། །

[Block 901]
བརྩོན་འགྲུས་ཞེས་བྱ་བ་འདིས་ཀྱང་དགེ་བའི་ཆོས་མ་སྐྱེས་པ་རྣམས༌[^491]བསྐྱེད་པ་དང་། སྐྱེས་པ་རྣམས་ཕྱིར་ཞིང་འཕེལ་བར་བྱེད་པའོ། །

[Block 902]
སྦྱིན་པ་ཕུན་སུམ་ཚོགས་པ་ཞེས་བྱ་བས༌[^492]ནི་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བསྟན་ཏོ། །

[Block 903]
གྲགས་པ་ཉིད་དཔལ་ཡིན་པས་གྲགས་དང་དཔལ་ལོ། །

[Block 904]
དེས་ན་གྲགས་པ་དང་དཔལ་ནི། སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་མཐོང་བའི་ཆོས་ཀྱི་འབྲས་བུའོ། །

[Block 905]
དེ་བཞིན་དུ་ཆོས་ཀྱིས༌[^493]ཚུལ་བཞིན་དུ་ཡུན་རིང་ས་ཆེན་སྐྱོང་བར་གྱུར། ཞེས་བྱ་བ་ནི་ཇི་ལྟ་བདེ་བཞིན་དུ་ཡུན་རིང་དུ་སྐྱོང་བར་གྱུར་ཅིག་པའོ། །

[Block 906]
ལྷ་མོ་དེ་དེ་ལྟར་གལ་ཞིག་མ་ཡིན་ཞེས་བྱ་བ་ནི་གོང་དུ་བསྟན་མ་ཐག་པ་སྟེ། དེ་བས་ན་འདི་ལྟར་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 907]
དེ་ཉིད་ལ་ནི་ཞེས་བྱ་བ་ནི་ལེགས་པའི་ལམ་ལ་སྟེ། ད་དུང་བརྩོན་པས་བསྟན་པར༌[^494]བྱའོ། །

[Block 908]
[^495]ཅིའི་ཕྱིར་ཞེ་ན། དེའི་འབྲས་བུ་ཉམས་སུ་མྱོང་བ་སྟེ། མངོན་སུམ་དུ་མཐོང་བས་སོ། །

[Block 909]
དཔལ་ཕུན་སུམ་ཚོགས་པའི་རྒྱུ་ཡིན་པས་དཔལ་ཕུན་སུམ་ཚོགས་པའི་རྒྱུ་དེ་ལ༌[^496]སེམས་ཞེན་པ་གང་ཡིན་པ་དེ་ནི་དཔལ་ཕུན་སུམ་ཚོགས་པ་ལ་ཞེན་པ༌[^497]ཞེས་བྱའོ། །

[Block 910]
ཅིའི་ཕྱིར་རྒྱལ་པོ་ལ་དཔལ་ཕུན་སུམ་ཚོགས་པའི་རྒྱུ་འདི་འདྲ་བར་འགྱུར། ཅི་ཐམས་ཅད་ཉིད་སྐྱེ་བ་དྲན་པར་འགྱུར་རོ་ཞེ་ན། དེ་ནི་མ་ཡིན་པར་བསྟན་པའི་ཕྱིར་དེ་ལྟ་བས་ན་འདྲི་བ་སྟེ། དེ་ནས་ལྷ་མོ་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 911]
བསོད་ནམས་ཀྱི་ཡོན་ཏན་ཞེས་བྱ་བ་ལ་སོགས་པས་ཀྱང་བསྐྱེད་པའི་གནས་ཡིན་པའི་ཕྱིར་དྲི་བ་ཡིན་ནོ། །

[Block 912]
གང་གིས་ཐོབ་པའི་མཚན་མ་དེས་ན་ཟན་ཆང་གཅིག་ཅེས་བྱ་བའི་སྐལ་པ་སྒོམ་པའོ། །

[Block 913]
ཐུབ་པ་ནི་རབ་ཏུ་བྱུང་བ་ལའོ། །

[Block 914]
གུས་པར་ཕུལ་བ་ཞེས་བྱ་བ་ནི་སྲི་ཞུས་བྱིན་པའོ། །

[Block 915]
དེ་ཚེ་གཉིད་ཀྱིས་ལོག་ལས་ཞེས་བྱ་བས་ནི་སྔ་མའི་ལུས་ཡང་དག་པར་རྟོགས་པའོ། །
--- END BLOCKS ---
