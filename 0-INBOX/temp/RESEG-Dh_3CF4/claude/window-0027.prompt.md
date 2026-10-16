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
[Block 946]
སེལ་བ་ཡིན་པས་མེད་པ་སྟེ། དེ་ལ་མེད་པ་ནི་འཁོར་བའི་ལམ་བགྲོད་ངལ་བ་མེད་པའོ། །

[Block 947]
འདིས་ནི་སྡུག་བསྔལ་ལས་ལྡོག་པར་བསྟན་ཏོ། །

[Block 948]
སྡུག་བསྔལ་བསལ༌[^530]ནས་བདེ་བ་བསྒྲུབ་པའི༌[^531]དབང་དུ་བྱས་ནས། སྦྱིན་པ་བདེ་བ་མང་པོ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིག་རྐང་ཡིན་ཏེ། གཅིག་མ་ཡིན་པའི་བདེ་བ་ཡིན་ཏེ། བདེ་བ་མང་པོའོ། །

[Block 949]
དེ་དག་སྒྲུབ་པ་ནི་བདེ་བ་མང་པོ་འགྲུབ་པའོ། །

[Block 950]
གྲོགས་པོ་བཟང་པོ་ཞེས་བྱ་བ་ནི་གྲོགས་པོ་ཡང་ཡིན་ལ་བཟང་པོ་ཡང་ཡིན་པས༌[^532]གྲོགས་པོ་བཟང་པོའོ། །ཇི་ལྟར་གྲོགས་པོ་བཟང་པོ་ཡིན་ཞེ་ན། སྔར་བཤད་པའི་ཚུལ་གྱིས་ཏེ། བདེ་བ་མང་པོ་སྒྲུབ་པར་བྱེད་པས་སོ། །

[Block 951]
མཆོག་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་རྟག་ཏུ་ཉེ་བར་འཁོར་བའི་ཕྱིར་རོ། །

[Block 952]
དེ་ལྟར་སྦྱིན་པས་ཆོས་དང་། དོན་དང་། འདོད་པ་རྣམས་འགྲུབ་པར་བསྟན་ནས། སྦྱིན་པ་ནི་དང་པོ་ཡིན་ཏེ། དེས་ན་དེས་ཡོངས་སུ་བཟུང་བ་སྟེ། དེའི་དབང་དུ་བྱས་པ་ཡིན་པས་གཞན་ལས་གཙོར༌[^533]བྱས་པ་ཡིན་ནོ། །

[Block 953]
[^534]སྦྱིན་པ་ཉིད་ཀྱིས་བསོད་ནམས་ཀྱི་ཚོགས་ཀྱི་འབྲས་བུ་མཐའ་དག་ཐོབ་པར་འགྱུར་རོ་ཞེས་བསྟན་པའི་དོན་ཡིན་ཏེ། བསོད་ནམས་ཀྱི་ཚོགས་ཀྱང་རྣམ་པ་གསུམ་སྟེ། སྦྱིན་པ་དང་། ཚུལ་ཁྲིམས་དང་། བཟོད་པ་སྟེ་རྣམ་པ་གསུམ་མོ། །

[Block 954]
བསོད་ནམས་ཀྱི་ཚོགས་རྣམ་པ་གསུམ་ལས་འབྲས་བུ་ཡང་རྣམ་པ་གསུམ་སྟེ། སྦྱིན་པས་ནི་ལོངས་སྤྱོད་ཆེན་པོར་འགྱུར་རོ། །

[Block 955]
བཟོད་པས་ནི་འཁོར་མང་བ་ཉིད་དུ་འགྱུར་རོ། །

[Block 956]
ཚུལ་ཁྲིམས་ཀྱིས་ནི་བདེ་འགྲོར་སྐྱེ་བ་སྟེ་བདག་གི་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 957]
སྦྱིན་པའི་འབྲས་བུས༌[^535]ནི་འབྱོར་པ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 958]
བཟོད་པས་ནི་བཀའ་ལུང་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 959]
དེ་ཡང་སྦྱིན་པ་ཉིད་ཀྱིས་འགྲུབ་པ་སྟེ། སྔོན་སྦྱིན་པའི་དུས་སུ་སློང་མོ་པ་རྣམས་ཀྱི་ངག་བཞིན་དུ་བྱས་ཏེ། འདོད་པའི་དོན་རབ་ཏུ་བསྒྲུབས་པ༌[^536]ཡིན་པའི་ཕྱིར་བཀའ་ལུང་མཉན་པའི་ཡོན་ཏན་ཐོབ་པའོ། །

[Block 960]
སུམ་ཅུ་རྩ་གསུམ་ཕོ་བྲང་གནས་སམ་ཞེས་བྱ་བ་ནི་ཚུལ་ཁྲིམས་ཀྱི་འབྲས་བུ་སྟེ། སྦྱིན་པའི་དུས་སུ་སློང་མོ་པ་རྣམས་ཀྱི་ངག་བཞིན་དུ་བྱས་ཏེ། འདོད་པའི་དོན་རབ་ཏུ་བསྒྲུབས་པ་ཡིན་པའི་ཕྱིར་བདེ་བ་བསྐྱེད་པ་ཡིན་ཏེ། དེ་བས་ན་སུམ་ཅུ་རྩ་གསུམ་གྱི་ཕོ་བྲང་དུ་གནས་པའི་རྒྱུར་གྱུར་པ་ཉིད་དོ། །

[Block 961]
གཟུགས་བཟང་ཡོན་ཏན་ཞེས་བྱ་བ་ཡང་ཚུལ་ཁྲིམས་ཀྱི་འབྲས་བུ་ཉིད་དོ། །

[Block 962]
དེའི་ཕྱིར་ཇི་ལྟར་འདིས་ཐོབ་པ་ཡིན་ཏེ། མདོག་ཕུན་སུམ་ཚོགས་པ་སྦྱིན་པའི་དངོས་པོ་མ་ཡིན་པ་ལས་སོ། །

[Block 963]
གང་ཞིག་འདོད་པ་དེ་དག་ཐམས་ཅད་སྦྱིན་པས༌[^537]ཐོབ་པར་འགྱུར་ཞེས་བྱ་བ་ནི་རེ་ཞིག་འདོད་པའི་ཁམས་ཀྱི་བསོད་ནམས་ཀྱི་འབྲས་བུ་ཐམས་ཅད་འདིས་འཐོབ་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 964]
དེ་ལྟར་ངེས་དོན་གཏན་ལ་ཕབ་ན་ཞེས་བྱ་བ་ནི་འདི་ལྟར་བསྟན་ཅིང༌[^538]དེ་ལྟར་ངེས་པའི་དོན་དུ་གྱུར་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 965]
ཡང་དག་པར་བསྟན་པའི་ཕྱིར། སྦྱིན་པ་ནོར་གྱི་སྙིང་པོ་ཞེས་བྱ་བའི་ཚིགས་བཅད་བསྟན་པ་ཡིན་ཏེ། འཇིག་རྟེན་དང་འཇིག་རྟེན་ལས་འདས་པའི་ཕུན་སུམ་ཚོགས་པའི་རྒྱུ་ནི་སྦྱིན་པ་ཡིན་ཏེ། དེ་ལྟར་ངེས་དོན་གཏན་ལ་ཕབ་ན་སྦྱིན་པ་ནོར་གྱི་སྙིང་པོ་ཞེས་བྱ་བ་སྟེ། མཐོང་བའི་ཆོས་ཀྱི་ཐུན་མོང་དུ་གྱུར་པའི་ནོར་ལས་ཐུན་མོང་མ་ཡིན་པའི༌[^539]རྒྱུར་གྱུར་པ་ཡིན་པས་སྦྱིན་པ་ནི་སྙིང་པོ་ལེན་པའོ། །

[Block 966]
སྦྱིན་པ་དབང་ཕྱུག་རྣམས་ཀྱི་རྒྱུ། །ཞེས་བྱ་བ་ནི་མ་འོངས་པའི་མངོན་པར་མཐོ་བའི་རྒྱུར་བྱས་པའོ། །

[Block 967]
སྐྱེ་བོ་མཆོག་གི་ཚུལ་ཞེས་བྱ་བ་ནི་འཇིག་རྟེན་ལས་འདས་པའི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ཚུལ་ལོ། །

[Block 968]
རྡུལ་ཙམ༌[^540]སྦྱིན་པ་ཞེས་བྱ་བ་ལ། སྦྱིན་པ་རྡུལ་ཙམ་ཡང་སྦྱིན་པར་མི་བྱེད་པ་ནི་ཤེས་རབ་ཆུང་ངུ་དག་སྟེ། ངེས་དོན་གཏན་ལ་མ་ཕབ་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 969]
སྦྱིན་པ་ལ་སོགས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་པས་ཚུལ་ཁྲིམས་ལ་སོགས་པ་གཟུང༌[^541]ངོ་། །སློབ་དཔོན་དཔའ་བོས་མཛད་པའི་སྐྱེས་པའི་རབས་རྒྱ་ཆེར་བཤད་པ་ལས་ཟན་དྲོན་ཆང་པ་བྱིན་པའི་སྐྱེས་པའི་རབས་སོ།། །།

[Block 970 [HEADING]]
## ཚོང་དཔོན་གྱི་སྐྱེས་པའི་རབས། ^4-0

[Block 971]
བརླག་པར་འགྱུར་བ་ནི་ངན་སོང་གསུམ་དུ་འགྲོ་བས་ན༌[^542]བརླག་པའོ། །

[Block 972]
ངན་སོང་གསུམ་དུ་འགྲོ་བ་བརྗོད་པས་ནི་གཞན་མ་བརྗོད་པ༌[^543]ཡང་གྲུབ་པོ། སྐལ་བ་ཁྱད་པར་ཅན་དང་ལྡན་པ། ཡོན་ཏན་དང་སྤྲོ་བ་ཕུན་སུམ་ཚོགས་པ་ཞེས་བྱ་བས་ནི་སྐལ་བ་དང་སྐྱེས་བུ་བྱེད་པ་ཕུན་སུམ་ཚོགས་པ་གཉིས་ཡིན་ནོ། །

[Block 973]
སྤྲོ་བ་ཕུན་སུམ་ཚོགས་པས་ཞེས་བཤད་པའི་སྤྲོ་བ་ཕུན་སུམ་ཚོགས་པ་གང་ཡིན་ཞེ་ན། དེ་ཉིད་སྨྲས་པ། སྤྱོད་ཚུལ་མི་མཐུན་པ་མེད་པའི་ངང་ཚུལ་ཅན་ཞེས་བྱ་བའོ། །

[Block 974]
ཆོ་རིགས་བཙུན་པ་དང་ལྡན་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། རིགས་བཙུན་པ་དང་། རིགས་པ༌[^544]དང་གཞུང་ལེན་པར་བསྟན་པ་ཡིན་ནོ། །

[Block 975]
ཕོངས་པ་རྣམས་ནི་དགར་གྱུར་པས། །ཞེས་བྱ་བ་འདིས་ནི་མཐོང་བའི་ཆོས་ཀྱི་འབྲས་བུ་གྲགས་པ་བསྟན་པའོ། །

[Block 976]
རྣམ་པར་རྟོག་པ་ཉིད་གཡོ་བ་ཡིན་པའི་ཕྱིར་རྣམ་པར་རྟོག་པ་གཡོ་བ་སྟེ། སྦྱིན་ནམ་མི་སྦྱིན་སྙམ་པའོ། །

[Block 977]
ཕྱོགས་གཉི་གར་རྒྱུ་བ་དང་། ཆོས་མཐུན་པ་རྣམ་པར་རྟོག་པའི་གཡོ་བས་བསྐྱོད་པའི་ཡིད་དང་ལྡན་པའི་ཕོངས་པ་གང་ཡིན་པ་དེ་ནི་རྣམ་པར་རྟོག་པའི་གཡོ་བས་བསྐྱོད་པ་ཡིན་ལ། སེམས་ཅན་ཕོངས་པ་རྣམས་ལའོ། །

[Block 978]
ཡིད་ཆེས་པས་སྤོབས་པའི་ཕོངས་པའི་སྦྱོར་བ་གང་ཡིན་པ་དེ་ནི་ཡིད་ཆེས་སྤོབས་ཤིང་སློང་བའོ། །

[Block 979]
དེ་ནི་བདག་གི་བདེ་ཕྱིར་ནོར་མི་སྦེད། །ཅེས་བྱ་བ་འདི་དག་གིས་བསྡུས་པའི་དོན་ཡོངས་སུ་བཟུང་བ་ཡིན་པས་ནོར་ཡོངས་སུ་བཟུང་བའི་བྱ་བ་ཡིན་པ་སྟེ། འཇིག་རྟེན་པ་རྣམས་ནི་བདག་གི་བདེ་བའི་དོན་དང་། མངོན་པར་ཆགས་པའི་དོན་དུ་བྱེད་པའོ། །

[Block 980]
གསུམ་པོ་དེ་མེད་པའི་ཕྱིར་རོ། །

[Block 981]
གཞན་གྱི་དོན་དུ་མེད་ཅེས་བྱ་བ་དང་། བཟློག་པ་དེ༌[^545]མི་ནུས་པའི་ཕྱིར་སྤངས་པར་གྱུར་པ་ཡིན་ཏེ། འདིས་ནི་འཇིག་རྟེན་ལས་འདས་པའི་ནོར་ཡོངས་སུ་བཟུང་བ་བསྟན་ཏོ། །

[Block 982]
མདོག་དང་བསུང་དང་འཇམ་པ་ལ་སོགས་པའི་ཞེས་པ༌[^546]སོགས་པའི་སྒྲས༌[^547]ནི་སྨིན་པའི་ནུས་པ་དང་བཟའ་བའི༌[^548]ཡོན་ཏན་ལ་སོགས་པ་དང་ལྡན་པའོ། །

[Block 983]
རྣམ་པ་སྣ་ཚོགས་ཞེས་བྱ་བ་ནི་དངོས་པོའི་རྣམ་པའོ། །

[Block 984]
ཡང་ན་བཅའ་བ་ལ་སོགས་པ་རེ་རེའི་རྣམ་པ་ཡང་སྣ་ཚོགས་པར་གྱུར་པ་ཡིན་པས་སྣ་ཚོགས་པར་བཤམས་པའོ། །

[Block 985]
བཟའ་བ་དང་བཅའ་བ་ལ་སོགས་པའི་སྒྲས་གཞིབ་པ༌[^549]དང་བལྡག་པ་ལ་སོགས་པ་ཡང་གཟུང༌[^550]ངོ་། །དེའི་བསོད་ནམས་ཀྱི་ཚོགས་རྣམ་པར་འཕེལ་བར་འདོད་པ་ཞེས་བྱ་བ་ལ། དེའི་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའི་འོ། །
--- END BLOCKS ---
