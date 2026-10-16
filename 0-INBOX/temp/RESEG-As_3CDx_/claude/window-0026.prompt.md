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
དེ་ཡང་ཇི་ལྟ་བུ་ཞེ་ན། དེའི་ཕྱིར་འདུ་བྱེད་ཀྱི་མཚན་ཉིད་དང་། དོན་དམ་པའི་མཚན་ཉིད་ཐ་དད་པ་མ་ལགས་སོ་ཞེས་མཆི་ཞེས་བྱ་བ་དང་། ཐ་དད་པ་ལགས་སོ་ཞེས་མཆི་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། འདུ་བྱེད་ཀྱི་མཚན་ཉིད་ཅེས་བྱ་བ་ནི་ཕུང་པོ་ལ་སོགས་པ་གཞན་གྱི་དབང་གི་ངོ་བོ་ཉིད་ཀྱི་སྐྱེ་བ་དང་། གནས་པ་དང་། འཇིག་པའོ། །

[Block 912]
དོན་དམ་པའི་མཚན་ཉིད་ཅེས་བྱ་བ་ནི་ཆོས་རྣམས་ཀྱི་ཆོས་བདག་མེད་པ་ཡོངས་སུ་གྲུབ་པའི་ངོ་བོ་ཉིད་དོ། །

[Block 913]
དེ་གཉིས་ནི་ངེས་པའི་དོན་གྱི་མདོ་སྡེ་ལས་འདུ་བྱེད་རྣམས་ཀྱི་བདག་མེད་པ་ཙམ་དང་། ངོ་བོ་མེད་པ་ཙམ་ཉིད་དོན་དམ་པའི་མཚན་ཉིད་ཡིན་པས་ཐ་དད་པ་དང་། ཐ་དད་པ་མ་ཡིན་པ་ཉིད་ལས༌[^714]ཡང་དག་པར་འདས་པའི་མཚན་ཉིད་ཡིན་པར་གསུངས་ན།[^715] དེ་དག་ནི་ངེས་པའི་དོན་གྱི༌[^716]མདོ་སྡེ་ལས་ཕྱི་རོལ་དུ་གྱུར་པའི་ཕྱིར་དྲང་བའི་དོན་གྱི་མདོ་སྡེ་ལས་ཁ་ཅིག་ཏུ་འདུ་བྱེད་ནི་གཞན་གྱི་དབང་གི་ངོ་བོ་ཉིད་ཡིན་ལ། དོན་དམ་པ་ནི་ཡོངས་སུ་གྲུབ་པའི་ངོ་བོ་ཉིད་ཡིན་པས། ངོ་བོ་ཉིད་རྣམ་པར་གཞག་པའི་སྒོ་ནས་ཐ་དད་པ་སྐད་ཀྱང་བཀའ་སྩལ། ཁ་ཅིག་ཏུ་གཞན་གྱི་དབང་གི་ངོ་བོ་ཉིད་ཡོངས་སུ་དག་པ་ནི་ཡོངས་སུ་གྲུབ་པའི་ངོ་བོ་ཉིད་ཡིན་པས་རང་བཞིན་གཅིག་པའི་སྒོ་ནས་ཐ་དད་པ་མ་ཡིན་པ་སྐད་ཀྱང་བཀའ་སྩལ་པའི་མདོ་དེ་ཉིད་ཀྱི་རྗེས་སུ་འབྲང་བ་སྒྲ་ཇི་བཞིན་དུ་འཛིན་པས་ཁ་ཅིག་ནི་ཐ་དད་པ་མ་ཡིན་ཞེས་ཟེར་ཏེ། དེ་གཉིས་ཀ༌[^717]ཡང་གདགས་པ་ལ་གཅིག་ཏུ༌[^718]རྨོངས་པ༌[^719]དོན་དམ་པ་ལ་ཚུལ་བཞིན་མ་ཡིན་པས་སེམས་པ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 914]
ཐེ་ཚོམ་དུ་གྱུར་པའི་བློ་གྲོས་ཅན་ཡིད་གཉིས་སུ་གྱུར་པ་ཞེས་བྱ་བ་དག་ཀྱང་དེ་ཉིད་ཀྱི་ཁོངས་སུ་གཏོགས་པ་ཡིན་ནོ། །

[Block 915]
གང་ནི་མེད་པར་མཆི་བ་ལགས་གང་ནི་ཤོ་བེ་མཆི་བ་ལགས་ཞེས་བྱ་བ་ནི་འདིར་ངེས་པའི་དོན་གྱི་མདོ་སྡེ་བསམ་པའི་སྐབས་སུ་གཉིས་ཀ་ཡང་བརྫུན་པ༌[^720]ཡིན་པར༌[^721]བྱའོ། །

[Block 916]
གང་ནི་ཚུལ་བཞིན་དུ་ཞུགས་པ་ལགས། གང་ནི་ཚུལ་བཞིན་མ་ལགས་པར་ཞུགས་པ་ལགས་ཞེས་བྱ་བ་ཡང་གཉི་ག་ངེས་པའི་དོན་ལ་ཚུལ་བཞིན་མ་ཡིན་པར་ཞུགས་པ་ཡིན་པར་སྦྱར་རོ། །

[Block 917]
བདག་འདི་སྙམ་བགྱིད་དེ་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་དེ་དག་ངེས་པའི་དོན་གྱི་མདོ་སྡེ་ལས་ཕྱི་རོལ་དུ་གྱུར་པ་དངོས་སུ་སྟོན་ཏོ། །

[Block 918]
བྱིས་པ་རྨོངས་པ་མི་གསལ་བ། མི་མཁས་པ་ཞེས་བྱ་བ་དག༌[^722]ནི་རྣམ་གྲངས་སོ། །

[Block 919]
རྟོགས་པ་དང་མངོན་སུམ་དུ་བྱེད་པ་ཞེས་བྱ་བ་ནི་སྔར་བཤད་པ་བཞིན་ཏེ་དེ་དག་ནི་གདགས་པ་ལས་ཤིན་ཏུ་རྨོངས་པའི་ཚིག་གི་དོན་བཤད་པ་ཡིན་ནོ། །

[Block 920 [HEADING]]
###### རིགས་པ་ལ་ཤིན་ཏུ་རྨོངས་པ། ^4-1-3-2-2-0

[Block 921]
དེ་ལ་རིགས་པ་ལ་ཤིན་ཏུ་རྨོངས་པ་ལ་ཞེས་བྱ་བ་ནི་གཏན་ཚིགས་དང་དཔེའི་ཡན་ལག་མངོན་པར་མི་ཤེས་པའི་ཕྱིར་ཏེ། གཏན་ཚིགས་ཀྱི་ཡན་ལག་རྗེས་སུ་དཔག་པར་བྱ་བ་ལ་ཡོད་པ་དང་། མཐུན་པའི་ཕྱོགས་ལ་ཡོད་པ་དང་། མི་མཐུན་པའི་ཕྱོགས་ལས་ལྡོག་པ་དང་། དཔེའི་ཡན་ལག་ཆོས་མཐུན་པའི༌[^723]དཔེ་དང་། ཆོས་མི་མཐུན་པའི་དཔེ་དག་མི་ཤེས་པས་ན་གལ་ཏེ་ཐ་དད་པ་མ་ཡིན་པར་གྱུར་ན་ནི་སྐྱོན་འདིར་འགྱུར་རོ། །

[Block 922]
གལ་ཏེ་ཐ་དད་པ་ཡིན་པར་གྱུར་ན་ནི་སྐྱོན་འདིར་འགྱུར་རོ་ཞེས་བྱ་བའི་རིགས་པ་ལ་ཤིན་ཏུ་རྨོངས་པས་དོན་དམ་པ་ལ་ཚུལ་བཞིན་མ་ཡིན་པས་སེམས་པ་ཡིན་ནོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 923]
དེ་ཡང་ཇི་ལྟ་བུ་ཞེ་ན། དེའི་ཕྱིར་དེ་ཅིའི་ཕྱིར་ཞེ་ན། བློ་གྲོས་ཤིན་ཏུ་རྣམ་དག་ཅེས་བྱ་བ་ལ་སོགས་པས་ཐ་དད་པ་དང་། ཐ་དད་པ་མ་ཡིན་པ་ཉིད་ལས་ཡང་དག་པར་འདས་པའི་གཏན་ཚིགས་སྟོན་ཏེ། བསྒྲིམ་མི་དགོས་པར་ཤེས་པ་དང་། བསྒྲིམས་ཀྱང་མི་ཤེས་པ་ནི་གཏན་ཚིགས་ཉེས་པར་ཐལ་བར་འགྱུར་བ་མེད་པས་གཏན་ཚིགས་ཡིན་ནོ། །

[Block 924]
དེ་ཡང་ཇི་ལྟ་བུ་ཞེ་ན། སར་ཆུད་པའི་བྱང་ཆུབ་སེམས་དཔའ་དོན་དམ་པའི་མཚན་ཉིད་ལ་མཁས་པ་རྣམས་ཀྱིས་ནི་སྔོན་གོམས་པའི་དབང་གིས་བསྒྲིམ་མི་དགོས་པ༌[^724]དོན་འདི་ཤེས་པས་དེ་དག་ལ་ཡང་གཏན་ཚིགས་འདི་ཉེས་པར་ཐལ་བར་འགྱུར་བ་མེད་པས་གཏན་ཚིགས་ཡོངས་སུ་དག་པ་ཡིན་ལ། མོས་པས༌[^725]སྤྱོད་པའི་ས་ལ་གནས་པ་དོན་དམ་པའི་མཚན་ཉིད་ལ་མི་མཁས་པ་རྣམས་ཀྱིས་ནི་སྔོན་མ་གོམས་པའི་ཕྱིར་བསྒྲིམས་ཀྱང་དོན་འདི་མི་ཤེས་ཏེ་མི་ཤེས་པ་ནི་དེ་དག་ཉིད་ཀྱི་ཉེས་པ་ཡིན་གྱི། གཏན་ཚིགས་ཀྱི་ཉེས་པ་མ་ཡིན་པས་དེ་དག་ལ་ཡང་། ཡང་གཏན་ཚིགས་ཀྱི་ཉེས་པར་ཐལ་བར་འགྱུར་བ་མེད་པས་གཏན་ཚིགས་ཡོངས་སུ་དག་པ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 925]
དེ་ལྟར་གཏན་ཚིགས་ཡོངས་སུ་དག་པ་འདིས་བརྟགས་ན་ཐ་དད་པ་ཡིན་པར་གྱུར་ན་ཡང་སྐྱོན་དུ་འགྱུར་ལ། ཐ་དད་པ་མ་ཡིན་པར་གྱུར་ན་ཡང་སྐྱོན་དུ་འགྱུར་བར་སྣང་བ་ལགས༌[^726]ན། མོས་པས༌[^727]སྤྱོད་པའི་ས་ལ་གནས་པ་དེ་དག་གིས་ཐ་དད་པ་དང་། ཐ་དད་པ་མ་ཡིན་པའི་སྐྱོན་མ་རྟོགས་ན༌[^728]མཐའ་གཉིས་སུ་སོ་སོར་སྨྲ་བ་ནི་རིགས་པ་ལ་ཤིན་ཏུ་རྨོངས་པས་དོན་དམ་པ་ལ་ཚུལ་བཞིན་མ་ཡིན་པའི༌[^729]སེམས་པ་ཡིན་ནོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 926]
དེ་ལ་གལ་ཏེ་འདུ་བྱེད་ཀྱི་མཚན་ཉིད་དང་། དོན་དམ་པའི་མཚན་ཉིད་ཐ་དད་པ་མ་ཡིན་པར་གྱུར་ན་ནི་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚར་གྱིས་ནི་ཐ་དད་པ་མ་ཡིན་པར་གྱུར་ན་བདེན་པ་མཐོང་བ་རྣམས་འདུ་བྱེད་ཀྱི་མཚན་མ་དང་མ་བྲལ་བར་གྱུར་པ་ལ་སོགས་པ་སྨྲས་པར༌[^730]ཐལ་བར་འགྱུར་བ༌[^731]སྟོན་ཏོ། །

[Block 927]
ད་ནི་ཚིག་གི་དོན་བཤད་པར་བྱ་སྟེ། དེ་ལ་བྱིས་པ་སོ་སོའི་སྐྱེ་བོ་ཐམས་ཅད་བདེན་པ་མཐོང་བ་ཡིན་པར་ཡང་འགྱུར་ཞེས་བྱ་བ་ནི་དེ་དག་གིས་མཚན་མ་དང་བྲལ་བར་རྟོགས་པའི་ཕྱིར་རོ། །

[Block 928]
སོ་སོའི་སྐྱེ་བོ་ཁོ་ནར་འགྱུར་བཞིན་དུ་ཞེས་བྱ་བ་ནི་བདེན་པ་རྟོགས་པར་བྱ་བའི་ཕྱིར་སྦྱོར་བ་མ་བརྩམས་པ་ཁོ་ནར་རོ། །

[Block 929]
གྲུབ་པ་དང་བདེ་བ་ཞེས་བྱ་བ་ལམ་མ་ཐོབ་པ་ཐོབ་པ་ནི་གྲུབ་པའོ། །

[Block 930]
ཐོབ་པ་ཆུད་མི་ཟ་བ་ནི་བདེ་བའོ། །

[Block 931]
འདུ་བྱེད་ཀྱི་མཚན་མ་དང་མ་བྲལ་བར་འགྱུར་ཞེས་བྱ་བ་ནི་གཞན་མཐོང་བས་གཞན་དང་བྲལ་བར་མི་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 932]
མཚན་མའི་འཆིང་བ་ལས་རྣམ་པར་མ་གྲོལ་བར་ཡང་འགྱུར་ཞེས་བྱ་བ་ནི་འདུ་བྱེད་ཀྱི་མཚན་མ་དང་མ་བྲལ་བའི་ཕྱིར་གཟུགས་ལ་སོགས་པའི་མཚན་མ་ལས་རྣམ་པར་མི་གྲོལ་བའི་ཕྱིར་རོ། །

[Block 933]
གནས་ངན་ལེན་གྱི་འཆིང་བ་ལས་ཀྱང་རྣམ་པར་མ་གྲོལ་བར༌[^732]འགྱུར་ཞེས་བྱ་བ་ནི་མཚན་མ་མ་སྤངས་པས་དེ་ཡང་མ་སྤངས་པར་རྗེས་སུ་དཔག་པའི་ཕྱིར་ཡིན་གྱི། འདི་ནི་སྤོང་བ་ནི་དེ་ལ་སྤོང་བ་ལ་རག་ལས་པ༌[^733]མ་ཡིན་ཏེ། དེ་ལས་བཟློག་པ༌[^734]ཡིན་པའི་ཕྱིར་རོ། །

[Block 934]
གང་དག་ཅེས་བྱ་བ་ནི་མོས་པས་སྤྱོད་པའི་ས་ལ་རིགས་པ་ལ་ཤིན་ཏུ་རྨོངས་པ་སྔ་མ་དག་གོ། །

[Block 935]
འདུ་བྱེད་ཀྱི་མཚན་ཉིད་ཀུན་ནས་ཉོན་མོངས་པའི་མཚན་ཉིད་དུ་རྟོགས་པ་ཞེས་བྱ་བ་ནི་ཡང་དག་པ་མ་ཡིན་པའི་ཕྱིར། ཀུན་དུ་རྟོག་པའི་མཚན་ཉིད་དང་ལྡན་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 936]
སྤྱིའི་མཚན་ཉིད་དུ་གྱུར་པ་མ་ཡིན་པར་འགྱུར་རོ་ཞེས་བྱ་བ་ནི་ཐ་དད་པ་ཡིན་ན། དཔེ་གཟུགས་དྲི་ལ་སོགས་པ་གཞན་གྱི་སྤྱིའི་མཚན་ཉིད་ཡིན་པར་གྲགས་པ་མེད་པ་ལྟ་བུར་འགྱུར་བའོ། །

[Block 937]
བྱེ་བྲག་མེད་པར་ཞེས་བྱ་བ་ནི་དེ་བཞིན་ཉིད་ཀྱི་འདུ་བྱེད་ཐམས་ཅད་ལ་སྤྱིར་ཁྱབ་པའོ། །

[Block 938]
གོང་དུ་དོན་དམ་པ་ཡོངས་སུ་ཚོལ་བར༌[^735]ཡང་མི་འགྱུར་རོ་ཞེས་བྱ་བ་ནི་མཚན་མ་རྟོགས་ནས་དེའི་གོང་དུ་དེ་བཞིན་ཉིད་ཡོངས་སུ་ཚོལ་བར་མི་འགྱུར་རོ། །

[Block 939]
འདུ་བྱེད་རྣམས་ཀྱི་བདག་མེད་པ་ཙམ་དང་། ངོ་བོ་ཉིད་མེད་པ་ཙམ་ཉིད་དོན་དམ་པའི་མཚན་ཉིད་ཡིན་པར་ཡང་མི་འགྱུར་རོ་ཞེས་བྱ་བ་ནི་དེའི་མཚན་ཉིད་ཐ་དད་པ་བརྒྱུད་ན་ཞེས་བྱ་བར་དགོངས་སོ། །

[Block 940]
ཀུན་ནས་ཉོན་མོངས་པའི་མཚན་ཉིད་དང་རྣམ་པར་བྱང་བའི་མཚན་ཉིད་ཀྱང་དུས་གཅིག༌[^736]ཏུ་མཚན་ཉིད་ཐ་དད་དུ་གྲུབ་པར་འགྱུར་རོ་ཞེས་བྱ་བས་ནི་གང་ལ་མཚན་མ་ལས་དེ་བཞིན་ཉིད་ཐ་མི་དད་པ་དེ་ལ་ནི་དུས་གཅིག༌[^737]ཏུ་འགྲུབ་པར་བརྟག་མི་ནུས་སོ། །

[Block 941]
ཡང་ན་མཚན་མ་རྣམ་པར་གཞིག་པ་དེ་བཞིན་ཉིད་ཡིན་ན་ཡང་མཚན་མའི་དུས་ན་ནི་དེ་བཞིན་ཉིད་མེད་ལ་དེ་བཞིན་ཉིད་ཀྱི་དུས་ན་ཡང་མཚན་མ་མེད་པ་ཁོ་ན་ཡིན་པས༌[^738]དུས་གཅིག༌[^739]ཏུ་འགྲུབ་ཏུ་མི་རུང་བ་དེ་དུས་གཅིག༌[^740]ཏུ་འགྲུབ་པའི་སྐྱོན་དུ་འགྱུར་རོ། །

[Block 942]
ཚུལ་བཞིན་དུ་ཞུགས་པ་མ་ཡིན་པར་རིག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གདགས་པ་ལ་ཤིན་ཏུ་རྨོངས་པ་དང་། རིགས་པ་ལ་ཤིན་ཏུ་རྨོངས་པས་ངེས་པའི་དོན་ལ་ཚུལ་བཞིན་དུ་ཞུགས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བར་སྦྱར་ཏེ། དེ་ནི་དེ་ལ་ཤིན་ཏུ་རྨོངས་པའི་མཚན་ཉིད་རྣམ་པར་གཞག་པ་ཡིན་ནོ། །

[Block 943 [HEADING]]
##### དེ་དག་གི་དཔེའི་མཚན་ཉིད་རྣམ་པར་གཞག་པ། ^4-1-3-3-0

[Block 944]
དེའི་འོག་ཏུ་དེ་དག་གི་དཔེའི་མཚན་ཉིད་རྣམ་པར་གཞག་པའི་ཚིག་གི་དོན་ལ་སོགས་པ་བཤད་པར་བྱ་སྟེ། དེ་དག་གི་དཔེའི་མཚན་ཉིད་རྣམ་པར་གཞག་པ་ཞེས་བྱ་བ་ནི་དོན་དམ་པ་ཐ་དད་པ་དང་། ཐ་དད་པ་མ་ཡིན་པ་ཉིད་ལས་ཡང་དག་པར་འདས་པའི་མཚན་ཉིད་དང་ལྡན་པ་སྔར་བསྟན་པའི་གཏན་ཚིགས༌[^741]དེ་དག་གི་དཔེའི་མཚན་ཉིད་རྣམ་པར་གཞག་པ་གང་ཡིན་པའོ། །

[Block 945]
དེའི་ཕྱིར་དེ་བསྟན་པའི་དབང་དུ་མཛད་ནས། བློ་གྲོས་ཤིན་ཏུ་རྣམ་པར་དག་པ་འདི་ལྟ་སྟེ། དཔེར་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 946]
དེ་ལ་དཔེའི་མཚན་ཉིད་རྣམ་པར་གཞག་པ་ནི་གདུལ་བའི་བསམ་པ་དང་། མོས་པ་ཐ་དད་པའི་དབང་དུ་མཛད་ནས་འཇིག་རྟེན་ལ་གྲགས་པའི་གཟུགས་དང་སྒྲ་དང་། དྲི་དང་། རོ་དང་། རེག་བྱ་དང་། ཆོས་རྣམས་ཀྱི་མཚན་གཞི་དང་མཚན་ཉིད་ཐ་དད་པ་དང་། ཐ་དད་པ་མ་ཡིན་པ་ཉིད་ལས་ཡང་དག་པར་འདས་པའི་མཚན་ཉིད་དང་ལྡན་པ་རྣམས་རྨོངས་སོ། །

[Block 947]
དེ་ལ་དུང་དང་གསེར་ནི་གཟུགས་སོ། །

[Block 948]
པི་ཝང་གི་སྒྲ་ནི་སྒྲའོ། །

[Block 949]
ཨ་ཀ་རུ་ནག་པོའི་དྲི་ནི་དྲིའོ། །

[Block 950]
ན་ལེ་ཤམ་གྱི་ཚ་བ་དང་ཨ་རུ་རའི་མངར་བ་ནི་རོའོ། །
--- END BLOCKS ---
