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
བརྗོད་པར་བྱ་བ་ནི་སྔོན་དུ་བཤད་པའི་རིམ་པ་གཉིས་ཏེ། དེ་ལ་ཡང་དང་པོ་ལ་རྣམ་པ་གསུམ་སྟེ། ལུས་རྣམ་པར་དབེན་པའི་བར་དུའོ། །

[Block 912]
གཉིས་པ་ནི་རྣམ་པ་ལྔ་སྟེ་ངག་རྣམ་པར་དབེན་པ་ནས་བརྩམས་ཏེ་མི་གནས་པའི་མྱ་ངན་ལས་འདས་པའི་བར་དུའོ་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 913 [HEADING]]
#### འབྲེལ་པ། ^1-3-3-0

[Block 914]
འབྲེལ་པ་ཞེས་བྱ་བ་ནི་སྒྲ་དང་དོན་དག་གིས༌[^630]ཐབས་དང་ཐབས་ལས་བྱུང་བའི་མཚན་ཉིད་དམ། རྒྱུ་དང་འབྲས་བུའི་ཚུལ་ལམ། རྗོད་པ་དང་བརྗོད་པར་བྱ་བའི་མཚན་ཉིད་ངེས་པར་ཤེས༌[^631]པར་བྱའོ། །

[Block 915]
གལ་ཏེ་སྒྲ་དང་དོན༌[^632]དག་གིས་འབྲེལ་པ་གཙོ་བོ་ཡོད་པ་མ་ཡིན་ཡང་བློས་བྱས་པ་ཁོ་ནའོ། །

[Block 916]
གང་གི་ཕྱིར་སྒྲ་དང་དོན་དག་ལ་འབྲེལ་པ་མེད་དེ་རང་གི་མཚན་ཉིད་སྟོན་མི་ནུས་པའི་ཕྱིར་རོ། །

[Block 917]
འབྲེལ་པ་ཞེས་བྱ་བ་ནི་རྣམ་པ་གཉིས་ཏེ། དེའི་བདག་ཉིད་དང་། དེ་ལས་བྱུང་བའོ། །

[Block 918]
དེ་ལས༌[^633]དེའི་བདག་ཉིད་ཅེས་བྱ་བ་ནི་དབྱེར་མེད་པའི་དངོས་པོ་གཅིག་པོ་ཁོ་ན་ལ་ལྡོག་པས༌[^634]བྱས་པའི་བྱེ་བྲག་ལ་བརྟེན་ཏེ་བསྒྲུབ་པར་བྱ་བ་དང་སྒྲུབ་པར་བྱེད་པ་དང་། རྟོགས༌[^635]པར་བྱ་བ་དང་རྟོགས་པར༌[^636]བྱེད་པའི་བསྒྲུབ་པ༌[^637]དག་སོ་སོར་བསྟན་པ་ནི་རྨོངས་པའི་བློ་ཅན་རྣམས་ཀྱི་རྨོངས་པ་སེལ་བར་བྱེད་པའོ། །

[Block 919]
དཔེར་ན་ཤིང་དང་། ཤ་བ་དག་དང་། བྱས་པ་དང་མི་རྟག་པ་དག་གི་དབྱེར་མེད་པ་ནི་ཤིང་དང་ཤ་བ་དག་དང་བྱས་པ་དང་མི་རྟག་པ་བཞིན་དུ་སྒྲ་དང་དོན་དག་ལ་དབྱེར་མེད་པ་ཉིད་མེད་དོ། །

[Block 920]
དཔེར་ན་སྒྲ་རྗོད་པར་གྱུར་པ་ན་སྐྱེས་བུའི་ཁ་ཡོངས་སུ་ཁེངས་པར་འགྱུར་བའི༌[^638]དོན་གྱིས་ནི་མ་ཡིན་ནོ། །

[Block 921]
སྒྲ༌[^639]ནི་སྐད་ཅིག་མ་ཡིན་པའི་ཕྱིར་བརྗོད་མ་ཐག་ཏུ་རྣམ་པར་འཇིག་གོ། །

[Block 922]
དོན་ནི༌[^640]བུམ་པ་ལ་སོགས་པའི་མཚན་ཉིད་ཕྱི་རོལ་དུ་ཡོད་པ་དེ་ཡང་སྐད་ཅིག་མ་ཅན་མ་ཡིན་ཞེས་དེ་དག་ཐ་དད་པའོ། །

[Block 923]
ཐ་དད་པ་དང་ཐ་མི་དད་པ་དག་གིས་ཕན་ཚུན་སྤངས་པའི་མཚན་ཉིད་ཅན་གྱི༌[^641]འགལ་བས༌[^642]དེའི་བདག་ཉིད༌[^643]མེད་དོ། །

[Block 924]
གལ་ཏེ་སྐྱོན་དེ་བསལ་བར༌[^644]བྱ་བའི་ཕྱིར་ཐ་དད་པའི་དོན་ལ་ཡང་དོན་སྒྲར་མཚན༌[^645]བརྡའི་སྒོ་ནས་རྗོད་པར་བྱེད་ཅེ་ན། དེ་ཡང་མི་རིགས་ཏེ། གང་གི་ཕྱིར་དངོས་པོའི་ཆོས་ཉིད་དུ་གནས་པའི་རང༌[^646]གི་མཚན་ཉིད་མི་རྟོག་པའི་ཡེ་ཤེས་པའི་སྤྱོད་ཡུལ་ནི་བརྡས་བསྟན་པར་མི་ནུས་ཏེ། ཐ་དད་པ་དང་ཐ་མི་དད་པ་དང་། མིང་དང་རིགས་ལ་སོགས་པའི་དབྱེ་བས་ཀྱང་བརྗོད་པར་བྱ་བ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 925]
རེ་ཞིག་བརྗོད་བྱ་ནི་སྐད་ཅིག་མ་ཡིན་པའི་ཕྱིར་མི་གནས་ཏེ། རྗོད་པར་བྱེད་པ་དེ་ཡང་དེ་བཞིན་ཏེ། དངོས་པོ་ཐམས་ཅད་སྐད་ཅིག་མས་ཁྱབ་པའི་ཕྱིར་རོ། །

[Block 926 [VERSE]]
བརྡ་ནི་ཐ་སྙད་ལ་དགོས་པ་སྟེ། །
གང་ལ་བརྟེན་པའི་ཐ་སྙད་དེ། །
གལ་ཏེ་གནས་པར་མི་འགྱུར་ན། །
དེའི་ཚེ་གང་གི་བརྡ་ཡིན་ཏེ། །

[Block 927 [VERSE]]
མོ་གཤམ་གྱི་བུའི་བརྡ་བཞིན་ནོ། །
ཇི་སྐད་དུ་ཚད་མ་རྣམ་འགྲེལ་ལས།
སྒྲ་རྣམས་ཀྱིས་ནི་བརྡ་ཅན་སྟོན། །
དེ་ནི་ཐ་སྙད་ཕྱིར་བཤད་པ། །

[Block 928 [VERSE]]
དེ་ཚེ་རང་གི་མཚན་ཉིད་མེད། །
དེས་ན་དེ་ལ་བརྡ་མེད་དོ། །

[Block 929]
ཞེས་འབྱུང་ངོ་། །དེ་བས་ན་དེའི་བདག་ཉིད་ཀྱི་འབྲེལ་པ་མེད་པ་ཁོ་ནའོ། །

[Block 930]
དེ་ལས་བྱུང་བའི་འབྲེལ་པ་ཡང་མེད་དེ། ཅིའི་ཕྱིར་ཞེ་ན། དེ་ལས་བྱུང་བའི་མཚན་ཉིད་ཀྱི་འབྲེལ་པ་ནི་ཐ་དད་པའི་དངོས་པོ་དག་ལ་ཡོད་དེ། དོན་གྱི་རྗེས་སུ་འགྲོ་བ་དང་། ལྡོག་པ་རྗེས་སུ་འཇུག་པའི་ཕྱིར་ཏེ། དུ་བ་དང་མེ་བཞིན་ནོ། །

[Block 931]
མེ་ཡོད་པས་དུ་བ་ཡོད་པ་དང་། མེ་མེད་པས་བུད་ཤིང་ལ་སོགས་པ་རྒྱུ་རྣམས་མ་ཚང་བ་མེད་པ་ཡོད་པས་ཀྱང་དུ་བ་ཡོད་པར་མི་འགྱུར་ཞེས་རྒྱུ་ཡོད་པ་དང་མེད་པ་དག་གིས་འབྲས་བུ་ལ་ཡང་ཡོད་པ་དང་མེད་པ་ཉིད་དེ། དེ་ནི་རྒྱུའི་རྗེས་སུ་འགྲོ་བའི་ཕྱིར་རོ། །

[Block 932]
དེ་བས་ན་ཡོད་པ་དང་མེད་པ་དག་གིས་བྱས་པའི་བདག་ཉིད་ཡོད་པ་དང་མེད་པ་ཅན་གྱི་དུ་བས་མེ་རྟོགས་པར་བྱེད་དོ། །

[Block 933]
རྟོགས་པ༌[^647]དང་རྟོགས་པར་བྱ་བའི་དངོས་པོའམ། བསྒྲུབ་བྱ་དང་སྒྲུབ་པར་བྱེད་པ་དངོས་པོ་དག་གི་རྗེས་སུ་འགྲོ་བ་དང༌[^648]ལྡོག་པ་ཁོ་ན་རྒྱུ་ཡིན་ནོ། །

[Block 934]
དེ་ལྟ་བུའི་རིགས་པ་སྒྲ་དང་དོན་དག་ལ་མེད་དེ། ཅིའི་ཕྱིར་ཞེ་ན། བུམ་པ་ལ་སོགས་པའི་དོན་ཡོད་པས་ཀྱང་དངོས་པོ་གཅིག་ལ་ཡིད་འབྲེལ་པ་ཅན་གྱི་སྐྱེས་བུས་སྒྲ་བརྗོད་པར༌[^649]མི་ནུས་པ་དང་། དོན་མེད་པས་ཀྱང་རྟོག་པ་དང་བཅས་པའི་རྣམ་པར་ཤེས་པ༌[^650]རང་དབང་དུ་སྒྲ་རྗོད་པར་བྱེད་པ་སྟེ། འཁོར་ལོས་སྒྱུར་བ༌[^651]དང་རྒྱ་མཚོ་ལ་སོགས་པའི་སྒྲ་བཞིན་ནོ། །

[Block 935]
དེའི་ཕྱིར་དོན་གྱི་རྗེས་སུ་འགྲོ་བ་དང་ལྡོག་པ་མེད་པས་སྒྲ་དང་དོན་དག་གིས་དེ་ལས་བྱུང་བའི་འབྲེལ་པ་མེད་དོ། །

[Block 936]
དེ་ལ་སྨྲས་པ། རང་གི་མཚན་ཉིད་ཀྱི་འབྲེལ་པ་མེད་དེ་སྤྱིའི་མཚན་ཉིད་ཀྱིས་བྱས་པའི་འབྲེལ་པ་ཡོད་པ་ཉིད་དེ་དཔེར་ན་རྟོག་བཅས་ཀྱི་ཤེས་པ་ལ་སྤྱིའི་ཚུལ་དུ༌[^652]དོན་གྱི་རྣམ་པ་གང་སྣང་བ་དེ་ཉིད་ཀྱིས་ཕ་རོལ་པོ་ལ་རྟོགས་པར་བྱ་བའི་ཕྱིར་འབྲས་བུར་གྱུར་པའི་སྒྲ་སྐྱེད་པར༌[^653]བྱེད་དོ། །

[Block 937]
སྤྱིའི་སྒྲའི་རྣམ་པ་དེས་ཀྱང་ཉན་པ་པོའི་རྒྱུད་ལ་རྟོག་པ་སྐྱེད་པར་བྱེད་དོ། །

[Block 938]
དེའི་ཕྱིར་སྒྲའི་ཡུལ་གང་ཡིན་པ་དེ་ཉིད་རྣམ་པར་རྟོག་པ༌[^654]རྣམས་ཀྱི་ཡུལ་ལོ། །

[Block 939]
དེ་བས་སྒྲ་དང་དོན་རྣམས་ཀྱི་བཏགས་པ་པའི་འབྲེལ་པ་ཡོད་པ་ཁོ་ནའོ། །

[Block 940]
དེ་ཉིད་ལ་བརྟེན་ཏེ་ཉེ་བར་བརྟགས་པས༌[^655]རང་གི་མཚན་ཉིད་ལ་ཡང་སྒྲ་འཇུག་གི་འཇུག་པ་གཙོ་བོས་ནི་མ་ཡིན་ནོ། །

[Block 941]
འབྲེལ་པ་དེ་ཡང་རྣམ་པ་དྲུག་ཏུ་འགྱུར༌[^656]ཏེ། དེ་བཞིན་གཤེགས་པ་དང་ལྷ་མོ་དང་བྱང་ཆུབ་སེམས་དཔའ་དང་། ལྷ་དང་། མིའམ་ཅི་དང་། མི་རྣམས་ཀྱིའོ།[^657] །

[Block 942]
དེ་ལ་དང་པོ་འགྲོ་བ་འདི་དག་མུན་པར་གྱུར་པ་སྟོང་པ་ཉིད་ཀྱི་རང་བཞིན་དུ་ཡོད་དེ། དེ་ནས་བསམ་གཏན་བཞི་པའི་གཟུགས་ཁམས་སུ་གནས་པ་དང་། ནམ་མཁའ་མཐའ་ཡས་ཀྱི་སྐྱེ་མཆེད་དུ་གནས་པ་དང་། རྣམ་པར་ཤེས་པ་མཐའ་ཡས་སྐྱེ་མཆེད་དང་། ཅི་ཡང་མེད་པའི་སྐྱེ་མཆེད་དང་། འདུ་ཤེས་ཡོད་མིན་མེད་མིན༌[^658]སྐྱེ་མཆེད་དུ་གནས་པ་རྣམས་ཀྱི༌[^659]ཡུན་རིང་བའི་དབང་གིས། ཆང་གིས་མྱོས་པའི་ནུས་པ་བཞིན་དུ་འདོད་ཆགས་ཀྱི་བག་ཆགས་འབྱུང་བར་འགྱུར་རོ། །

[Block 943]
དེའི་དེ་མ་ཐག་ཏུ་དེ་རྣམས་གཟུགས་ཅན་དུ་གྱུར་ཏོ།[^660] །

[Block 944]
དེ་ནས་ཆགས་པ་དང་མངོན་པར་འབྲེལ་པའི་དབང་གིས་རང་གི་ལུས་ལས་བཅུད་ཀྱི་རང་བཞིན་ཆར་གྱི་རྒྱུན་འབབ་པར་འགྱུར་རོ། །

[Block 945]
བབ་པ་དེ་རྣམས་ཀྱིས༌[^661]ཀྱང་ཁ་དོག་སེར་པོ་སའི་ཆ་འདམ་དུ་ཆགས་སོ།[^662] །

[Block 946]
ཡང་དུས་ཀྱི་དབང་གིས་དེ་དུམ་བུ་བཞིར་གས་ནས་གླིང་བཞི་དང་དཀྱིལ༌[^663]དུ་རི་རབ་ཀྱི་རྒྱལ་པོ་ཡང་དག་པར་བྱུང་བར་གྱུར་ཏོ།[^664] །

[Block 947]
དེ་ནས་དེ་དག་ཀྱང་དེ་ཉིད་དུ་བབས་སོ། །

[Block 948]
བག་ཆགས་ལྡང་བའི་ཤུགས་ཀྱིས་བུད་མེད་དང་སྐྱེས་པའི་རྟགས་སུ༌[^665]གྱུར་པས་ཕན་ཚུན་འབྲེལ་པའི་དབང་གིས་སྐྱེ་དགུ་དང་རིགས་བཞིའི་ཐ་སྙད་ཀྱང་འབྱུང་ངོ་། །མ་རྨོས་པར༌[^666]སྨིན་པའི་འབྲས་ལ་སོགས་པའི་འབྲུ་རྣམས་དང་། དེ་དག་བསྲུང་བར་བྱ་བའི་ཕྱིར་མཐའ་ཡས་གྲགས་པ་ལ་སོགས་པ་རྒྱལ་པོ་རྣམས་བྱུང་ངོ་། །བདག་དང་གཞན་གྱི་དབྱེ་བའི་དབང་གིས་ང་དང་བདག་ཏུ་འཛིན་པ་བྱུང་ངོ་། །དེའི་རྩ་བ༌[^667]ཅན་ནི་འདོད་ཆགས་ལ་སོགས་པའི་ཉོན་མོངས་པ་དང་དེ་ལས་བྱུང་བའི་དགེ་བ་དང་མི་དགེ་བའི་ལས་དང་། དེའི་རྒྱུ་ཅན་བདེ་འགྲོ་དང་ངན་འགྲོ་དག་ཅེས་ཟོ་ཆུན་གྱི་འཁྲུལ་འཁོར་བཞིན་དུ་ཡོངས་སུ༌[^668]འཁོར༌[^669]བའི་དགོན་པར་འཁོར་བར་གྱུར་ཏོ། །

[Block 949]
དེ་ནས་བཅོམ་ལྡན་འདས་རྡོ་རྗེ་འཆང་ཆེན་པོས་སྙིགས་མ་ལྔའི་དུས་སུ་ཉོན་མོངས་པ་ལྔས་དཀྲུགས་པའི་སེམས་ཅན་གྱི་ཁམས་ལ་གཟིགས་ཏེ། ཉན་ཐོས་ལ་སོགས་པའི་ལམ་གཞན་གྱིས་འདི་དག་འདུལ་བར་མི་འགྱུར་ཏེ་ཞེས་མཁྱེན་ནས་ཉོན་མོངས་པ་ཉིད་ཀྱིས་ཉོན་མོངས་པ་ཐམས་ཅད་ཉེ་བར་ཞི་བར་འགྱུར་ཞེས་དགོངས་ནས་སྒེག་པ་ལ་སོགས་པའི་ཆ་ལུགས་དང་ལྡན་པའི་དེ་བཞིན་གཤེགས་པ་ལྔ༌[^670]ཡེ་ཤེས་ལྔའི་ངོ་བོ་ཉིད་སྤྲོ་བར་མཛད་དེ། དེ་བཞིན་གཤེགས་པ་དེ་དག་གིས་དགའ་ལྡན་གྱི་ལྷའི་གནས་སུ་རིན་པོ་ཆེ་སྣ་བདུན་གྱི་རང་བཞིན་གྱི༌[^671]གཞལ་ཡས་ཁང་པ་ལ་བཞུགས་པའི་རྡོ་རྗེ་སེམས་དཔའ་ལ་གསོལ་བ་བཏབ་པར་གྱུར་པས་བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་རིག་མའི༌[^672]ཆུ་སྐྱེས་ཀྱི་ནང་དུ༌[^673]དཀྱིལ་འཁོར་སྤྲོས་ཏེ། དེ་བཞིན་གཤེགས་པ་རྣམས་ལ་རིག༌[^674]མའི་དབང་བསྐུར་ནས་ཕྱི་རོལ་དུ་སྤྲོས་ཏེ། དེ་ཁོ་ན་ཉིད་བསྟན་ཏོ་ཞེས་པ་དེ་ནི་དེ་བཞིན་གཤེགས་པའི་འབྲེལ་པའོ། །

[Block 950]
བཅོམ་ལྡན་འདས་དེ་ཉིད་ཀྱིས་འདོད་ཆགས་ཀྱི༌[^675]རིགས་ཅན་རྗེས་སུ་གཟུང་བར་བྱ་བའི་ཕྱིར། ལྷ་མོ་བཞི་སྤྲོས་ཏེ། དེ་རྣམས་ཀྱིས་ཡོངས་སུ་ཞུས་པས་དེ་ཁོ་ན་ཉིད་གསུངས་པ་དེ་ནི་ལྷ་མོའི་འབྲེལ་པའོ། །
--- END BLOCKS ---
