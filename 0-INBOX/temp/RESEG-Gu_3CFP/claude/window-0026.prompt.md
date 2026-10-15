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
[Block 911]
མཁས་པ་ནི་ཀུན་དུ་བརྟགས་པའི་ཤེས་རབ་གང་ཡིན་པའོ། །ཤེས་རབ་ཀྱིས༌[^681]འཇུག་པ་ནི་བསྟེན་པ་དང་། བརྗོད་པ་དང་། ཡོངས་སུ་དྲི་བ་དང་། འཕེལ་བའི་གཏམ་གཏན་ལ་དབབ་པ་ལས་ཀུན་དུ་ཤེས་པའི་དོན་ཁྱད་པར་ཅན་དུ་རྣམ་པར་ཤེས་པ་དང་ལྡན་པ་ནི་ཤེས་རབ་པོ། །ལུས་ཤིན་ཏུ་སྦྱངས་པ་ནི་ལུས་ལས་སུ་རུང་བ་ཉིད་དོ། །

[Block 912]
སེམས་ཤིན་ཏུ་སྦྱངས་པ་ནི་སེམས་ལས་སུ་རུང་བ་ཉིད་དོ། །

[Block 913]
གནས་ངན་ལེན་བསལ་བར་བྱ་བ༌[^682]ཞེས་བྱ་བ་ལ། གནས་ངན་ལེན་ཞེས་བྱ་བ་ནི་རྟེན་ལ་ཡོད་པའི་ཉོན་མོངས་པའི་ས་བོན་ནོ། །

[Block 914]
ཡེ་ཤེས་ནི་ལྐོག་ཏུ་གྱུར་པ་རྗེས་སུ་འཛིན་པའོ། །

[Block 915]
མཐོང་བ་ནི་མངོན་སུམ་གྱི་རྫས་འཛིན་པའོ། །

[Block 916]
ཡང་དག་པའི་ཡོན་ཏན་རྗོད་པར༌[^683]བྱེད་པས་སྙན་པར་སྨྲ་བའམ། ཡང་ན་ཡང་དག་པའི་ཡོན་ཏན་བརྗོད་པ་ཉིད་ནི་སྙན་པར་སྨྲ་བ་སྟེ། དེ་གང་ལ་ཡོད་པ་ནི་མཉན་པར་བྱ་བ་དང་། གཟུང་བར་བྱ་བ་སྟེ། ཐོས་པར་འདོད་པ་དང་། བསྒྲུབ་པར་འདོད་པས་ཞེས་བྱ་བའོ། །

[Block 917]
བརྒྱད་པ་རིགས་རྣམ་པར༌[^684]ཕྱེ་བ་རྫོགས་སོ།། །།

[Block 918 [HEADING]]
## སྦྱིན་པ་རིམ་པར་ཕྱེ་བ། ^4-0

[Block 919]
ངོ་བོ་ཉིད་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་སྡོམ་གྱི་ཚིགས་སུ་བཅད་པའི་བསྡུས་པའི་དོན༌[^685]དེ་ཉིད་ཀྱིས་བཤད་པས་དེས་ནི་བདག་གིས་ཡང་བརྗོད་པར་མི་བྱའོ། །

[Block 920]
ཡོ་བྱད་ཐམས་ཅད་དང་རང་གི་ལུས་ལ་མི་ལྟ་བ་ཞེས་བྱ་བ་འདིས་ནི་བྱང་ཆུབ་སེམས་དཔའི་སྦྱིན་པའི་ངོ་བོ་འདོད་པ་མེད་པའི་སེམས་ཀྱིས་སྦྱིན་པར་བྱ་བའི་རྫས་ལ་ལྟོས་པ་མེད་པ་ཉིད་དང་། ལུས་དང་ངག་གི༌[^686]ལས་ཁ་ན་མ་ཐོ་བ་མེད་པ་དག་གིས་སྦྱོར་བ་བསྟན་ཏོ། །

[Block 921]
གསུམ་པོ་འདི་ནི་ངེས་པའི༌[^687]སྦྱོར་བ་སྟེ། གཞན་དུ་གྱུར་ན་མ་ཚང་བ་ཡིན་ནོ། །

[Block 922]
ལུས་དང་ངག་གི་ལས་སྦྱིན་པར་བྱ་བའི་དངོས་པོ་ཁ་ན་མ་ཐོ་བ་མེད་པ་ཞེས་བྱ་བ་ནི་ཀུན་ནས་སློང་བ་ཁ་ན་མ་ཐོ་བ་མེད་པས་ཀུན་ནས་སློང་བ་ཉིད་ཀྱི་ལུས་དང་ངག་གི་ལས་ནི་དེས་ཀུན་ནས་བསླང་བ་ཡིན་ན་ཡང་སྦྱིན་པ་ཉིད་དེ། [^688]ཡང་དག་པར་གསོལ་བ་མ་བཏབ་ན་ནི་སྦྱིན་པར་མི་བྱེད་དེ། ཡང་དག་པར་གསོལ་བ་བཏབ་པ་ནི་སྦྱིན་པར་འདོད་པ་ཡིད་ལ་བྱེད་པ་དང་། [^689]ཡིད་མི་བདེ་བ་མེད་ཅིང་ཡིད་བདེ་བ་དང་འདུན་པས་ཁྲོ་བ་མེད་པ་སྔོན་དུ་འགྲོ་བས༌[^690]བུ་དང་ཆུང་མ་ལ་སོགས་པས་མི་བཟློགས༌[^691]པར་ནི་བརྩོན༌[^692]པར་བྱེད་དོ། །

[Block 923]
ཕ་དང་མ་ལ་མི་གནོད་པ་ཉིད་དུ་བསམ་པ་ཐག་པས་ཡོངས་སུ་གཏོང་བའོ། །

[Block 924]
སྡོམ་པ་ལ་གནས་པ་ཞེས་བྱ་བ་ནི་ཚུལ་ཁྲིམས་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 925]
འོང་བ་མཐོང་ཞིང་འབྲས་བུ་ལྟ་བ་ཞེས་བྱ་བ་ནི་ལྟ་བའི༌[^693]ཕུན་སུམ་ཚོགས་པའོ། །

[Block 926]
ཐམས་ཅད་སྦྱིན་པའི་བསྡུས་པའི་དོན་ནི་གང་ལ་གང་སྦྱིན་པ་དང་། ཇི་ལྟར་སྦྱིན་པའོ། །

[Block 927]
ཇི་དགའ་དགུར༌[^694]བྱེད་དུ་འཇུག་པ་ཞེས་བྱ་བ་ནི་གཏེའུ་དང་འཚོ་བ་ལ་སོགས་པ༌[^695]བྱེད་དུ་འཇུག་པའོ། །

[Block 928]
དབང་ཡོད་པ་ཞེས་བྱ་བ་ནི་གཞན་གྱི་དབང་འབའ་ཞིག་ཏུ་གྱུར་པས་གཞན་གྱི་ཚིག་གིས་དབང་སྒྱུར༌[^696]ཞིང་གཞན་གྱིས་འདི་ནི་ཁྱོད་ཀྱི་ལུགས་ཀྱི་བྱ་བའོ་ཞེས་གཏེའུ་འཇུག༌[^697]པའོ། །

[Block 929]
གང་གི་ཕྱིར་བྱང་ཆུབ་མཆོག་འདོད་པས་ནུས་པ་ལ་ངེས་པར་སྦྱོར་བ་དེའི་ཕྱིར་རང་གི་ལུས་ཅི་དགའ་དགུར༌[^698]བྱེད་དུ་འཇུག་པར་རྗེས་སུ་སྦྱིན་པར་གཞན་ལ་ཕན་པ་དང་བདེ་བར་འདོད་པས་བྱེད་དེ། དེ་ལྟ་བས་ན་གཞན་ལ་དབང་ཡོད་པར་རྗེས་སུ་སྦྱིན་པར་བྱེད་དོ། །

[Block 930]
གང་གི་ཕྱིར་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་རྫོགས་པར་འདོད་པས་དེའི་ཕྱིར་གཞན་གྱི་དབང་ཡིན་ནོ། །

[Block 931]
ཡང་ན་ཅི་དགའ་དགུར༌[^699]བྱེད་དུ་འཇུག་པ་ལ་སོགས་པ་གསུམ་རབ་ཏུ་སྦྱིན་པར་བྱེད་པས་སོ། །གང་གི་དོན་དུ་ཞེ་ན། དེ་ལ་སྨྲས་པ། བྱང་ཆུབ་དམ་པ་འདོད་པ་དང་། ཕ་རོལ་ལ་བདེ་བར་འདོད་པས་དང་པོར་སེམས་བསྐྱེད་པའི་དུས་དང་། དེ་བཞིན་དུ་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྦྱོར་བའི་དུས་སུའོ། །

[Block 932]
ཕ་རོལ་ཏུ་ཕྱིན་པ་ཡོངས་སུ་རྫོགས་པར་འདོད་པས་ལག་པ་དང་རྐང་པ་ལ་སོགས་པ་ན༌[^700]ཐ་ན་ལུས་ཀྱི་སྦྱིན་པ་ལས་བརྩམས་པའོ། །

[Block 933]
མཆོད་སྦྱིན་ངན་པ་ཞེས་བྱ་བ་ནི་རྣམ་པར་འཚེ་བ་དང་བཞད་གད་ལ་རྩོམ་པ་ཆེན་པོ་རྩོམ་པ༌[^701]སྟེ། རྣམ་པར་འཚེ་བ་དང་། རྩོམ་པ་ཆེན་པོ་གང་ལ་ཡོད་པའི་མཆོད་སྦྱིན་ནོ། །

[Block 934]
ནུ་མ་སྣུན་པ༌[^702]ཞེས་བྱ་བ་ནི་ནུ་མ་ལྡུད་པའོ། །

[Block 935]
གསོ་བ་ཞེས་བྱ་བ་ནི་རྒྱས་པར་བྱེད་པའོ། །

[Block 936]
སྐྱེད་པ་ནི་འཕེལ་བ་ཐོབ་པར་བྱེད་པའོ། །

[Block 937]
ཇི་ལྟར་སེམས་ཏེ་ཞེས་བྱ་བ་ནི་ཡིད་ཀྱིས་ཀྱང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 938]
སྦྱིན་པར་ལྟ་ག་ལ་བྱེད་ཅེས་བྱ་བ་ནི་ལུས་དང་ངག་གིས་སོ། །

[Block 939]
རྒྱལ་པོ་ཞེས་བྱ་བ་ནི་རིགས་ཉིད་དོ། །

[Block 940]
རྒྱལ་པོའི་རིགས་སུ་སྐྱེས་པར༌[^703]འགྱུར་བའོ། །

[Block 941]
སྤྱི་བོ་ནས་དབང་བསྐུར་བ༌[^704]ཞེས་བྱ་བ་ནི་བྱེ་བྲག་ཉིད་ཀྱི༌[^705]འཁོར་རྣམས་ཀྱིས་ཡོངས་སུ་བཟུང་བ་ཉིད་དོ། །

[Block 942]
བདག་པོ་ཞེས་བྱ་བ་ནི་དབང་ཕྱུག་དང་ལྡན་པ་དབང་ཕྱུག་མ་ཉམས་པ་སྟེ། བདག་ཉིད་ཀྱིས་བྱིན་པ་མ་གཏོགས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 943]
བརྗེད་ང་བ་ནི་བསོད་པའི་ལས་སོ། །

[Block 944]
སྙོམས་པར༌[^706]སེམས་ཀྱིས་སྦྱིན་པའི༌[^707]མཚན་ཉིད་ཅི་ལྟ་བུ༌[^708]ཞེ་ན། སེམས་སྙོམས་པ་ཉིད་ནི་ཡོན་གནས་ཀྱི་བློའི་མཚན་ཉིད་ཀྱིས་སོ། །གང་ལ་ན། སེམས་ཅན་ཐམས་ཅད་དེ། མཛའ་བཤེས་དང་། དགྲ་བོ་དང་། ཐ་མལ་པ་ལ་ཕན་པ་བྱེད་པ་དང་། དེའི་མི་མཐུན་པའི་ཕྱོགས་དང་། དེ་གཉི་ག་མ་ཡིན་པ་དང་། ཕན་འདོགས་པའི་ཞིང་ལ་ཡོན་ཏན་དང་ལྡན་པའི་ཕྱོགས་དང་། དེ་ལས་བཟློག་པའི༌[^709]ཕྱོགས་དག་དང་། འགྲོ་བའི་ཞིང་གི་ཕྱོགས་ལ་ནི་དམའ་བ་དང་། མཚུངས་པ་དང་། ཁྱད་པར་དུ་འཕགས་པ་དག་ལའོ། །

[Block 945]
སྙིང་རྗེའི་ཞིང་གི་ཕྱོགས་ལ་སྐྱིད་པ་ཉིད་ལ་སོགས་པ་ལ་ཇི་ལྟར་མཛའ་བཤེས་པ་དང་། མཛའ་བཤེས་མ་ཡིན་པ་དང་། ཐ་མལ་པ་དག་ལ་ཡོན་གནས་ཇི་ལྟ་བ་བཞིན་དུ་བློ་ཉེ་བར་གཞག་གོ་ཞེས་ཐམས་ཅད་དུ༌[^710]བརྗོད་པར་བྱ་སྟེ། ཡོན་ཏན་དང་ལྡན་པ་ལ་ཇི་ལྟ་བ་དང་། ཁྱད་པར༌[^711]དུ་འཕགས་པ་ལ་ཇི་ལྟ་བ་དེ་བཞིན་དུ་དམན་པ་དང་མཚུངས་པ་དག་ལ་ཡང་ངོ་། །བདེ་བ་དང་ལྡན་པ་ལ་ཇི་ལྟ་བ་བཞིན་དུ་སྡུག་བསྔལ་དང་ལྡན་པ་ལ༌[^712]ཡང་དེ་བཞིན་དུ་བྱེད་པའོ། །

[Block 946]
ཇི་སྐད་དུ༌[^713]སྨྲས་པ་ཞེས་བྱ་བ་ནི་གསོལ་བ༌[^714]འདེབས་པ་ལ་ཁས་བླངས་པའོ། །

[Block 947]
ཇི་ལྟར་དམ་བཅས་པའི་ཞེས་བྱ་བ་ནི་རེ་ཞིག་བདག་ཉིད་ཀྱིས་སྦྱིན་ནོ་ཞེས་དམ་བཅས་པའོ། །

[Block 948]
བསྐྱུངས་ཏེ་ཞེས་བྱ་བ་ནི་གྲངས་ཀྱི་སྒོ་ནས་སམ་ཚད་ལས་སོ། །

[Block 949]
བཟང་པོ་ནི་ཁྱད་པར་དུ་འཕགས་པ་སྟེ། རྣམ་པ་གཉིས་ཀྱིས་གྱ་ནོམ་པ་ཡིན་ཏེ། རིགས་ཀྱིས་སམ། རིན༌[^715]ཐང་གིས་སོ། །

[Block 950]
དེའི་མི་མཐུན་པའི་ཕྱོགས་ནི་ངན་པ་ཐ་ཆད་དོ། །
--- END BLOCKS ---
