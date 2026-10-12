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
ཨེ་ནི་ཤེས་རབ་ཉིད་འགྱུར་ལ། །ཞེས་པ་ནི་རླུང་ཉིད་དོ། །

[Block 912]
བ་ནི་རབ་དགའི་བདག་པོའོ།[^443] །ཞེས་པ་ནི་རྣམ་པ༌[^444]ཤེས་པ་ཉིད་དོ། །

[Block 913]
ཐིག་ལེ་མི་ཤིགས་དེ་ཉིད་དོ། །

[Block 914]
[^445]ཞེས་པ་ནི་འགྲོ་བ་ཐམས་ཅད་ཀྱི་སྙིང་གི་དབུས་ན༌[^446]རླུང་མི་ཤིགས་རྒྱལ་པོ་ཨ་ཐུང་ངུའི་ངོ་བོར་སྣང་བའོ། །

[Block 915]
དེ་ལས་ཡི་གེ་གཉིས་ཀྱང་སྐྱེ།[^447] །ཞེས་པ་ནི་ཨཱ་ལི་ཀཱ་ལིའི་སྡེ་ཚན་གྱི་ཡི་གེ་རྣམས་འབྱུང་བས་ཏེ་གང་ལ་གང་གིས་ཇི་ལྟར་ཡོངས་སུ་བྱེད་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 916]
དེ་བས་ན་འདི་དག་གིས་ནི་ཡི་གེ་གཉིས་པོ་ཕོ་དང་མོར་གྱུར་ཏེ། གང་དུ་སྐྱེ་བ་དང་ཡི་གེ་གཉིས་ཕོ་མོའི་མཚན་མར་གྱུར་པས་སེམས་ཅན་རྣམས་རང་གི་ས་བོན་ལས་སྐྱེ་བ་དང་། ཡི་གེ་གཉིས་ཀྱི་བརྡ་དེ་དག་གིས་བསྐྱེད་པ་གཙོ་བོ་ཡབ་ཡུམ་དང་དཀྱིལ་འཁོར་རྒྱལ་མཆོག་གང་གིས་ཡོངས་སུ་རྫོགས་པ་དང་། གང་གིས་ཡི་གེ་ལས་སྒྲའི་ཚོགས་འབྱུང་ཞིང་འདི་ལས་ཆོས་ཀྱི་ཕུང་པོ་བརྒྱད་ཁྲི་བཞི་སྟོང་ལ་སོགས་པ་འབྱུང་བའི་ཕྱིར་ཡི་གེ་གཉིས་ནི་བཞི་དང་ཕ་མ་ཉིད་དོ། །

[Block 917]
དེས་ཅིར་འགྱུར་ཞེ་ན། ཆོས་ཀྱི་ཕྱག་རྒྱ་ནི་གང་གིས་གང་ཞིག་ཡོངས་སུ་ཤེས་པ་དང་། བརྗོད་པར་རུང་བ་ཉིད་དོ། །

[Block 918]
དེ་གང་ཡིན་ཞེ་ན་ཡི་གེ་གཉིས་ཏེ་ཨེ་བཾ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 919]
དེའི་དེ་ཉིད་བརྡའི་དོན་ཡོངས་སུ་ཤེས་པ་གང་དང་གང་ཡིན་པའོ། །

[Block 920 [VERSE]]
དེས་ནི་སེམས་ཅན་ཐམས་ཅད་ལ། །
ཆོས་ཀྱི་འཁོར་ལོ་སྐོར་བྱེད་འགྱུར། །

[Block 921]
ཞེས་པ་སྟེ་དེའི་དོན་ཡང་གང་ཡིན། [^448]ཡི་གེ་གཉིས་ཤེས་པ་དེས་ནི་ཡི་གེའི༌[^449]བརྡའི་རྣམ་པར་ཤེས་པར་འགྱུར་རོ། །

[Block 922]
གང་གིས་ཡི་གེ་བརྡའི་རྣམ་པར་ཤེས་པ་དེས་ནི་ཡི་གེའི༌[^450]དེ་ཁོ་ན་ཉིད་ཤེས་པར་འགྱུར་རོ། །

[Block 923]
གང་གིས་ཡི་གེའི་དེ་ཁོ་ན་ཉིད་ཤེས་པ་དེ་ནི་སངས་རྒྱས་ཀྱི་ཆོས་ཡོངས་སུ་ཤེས་པར་འགྱུར་རོ། །

[Block 924]
དེས་ནི་ཆོས་ཐམས་ཅད་ཀྱི་སྟོན་པ་ཕུན་སུམ་ཚོགས་པ༌[^451]ཤེས་པ་བསྟན་པ་ཡིན་ནོ། །

[Block 925]
དེ་ལས༌[^452]གཞན་དུ་གྱུར་པའི་སྐྱོན་བསྟན་པའི་ཕྱིར། འགྲོ་བ་གང་གིས་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། ཡི་གེ་གཉིས་ནི་ཨེ་བྃ་ཞེས་པའོ། །

[Block 926]
མི་ཤེས་པ་ནི་ཡི་གེའི་དེ་ཁོ་ན་ཉིད་མི་ཤེས་པའོ། །

[Block 927]
རྟག་ཏུ་འདོན་པ་ནི་བརྗོད་པའོ། །

[Block 928]
ཅིར་འགྱུར་ཞེ་ན།

[Block 929 [VERSE]]
དེ་ནི་སངས་རྒྱས་ཆོས་རྣམས་ཀྱི། །
སྦྱོར་སྤངས་ཕྱི་རོལ་དཀའ༌[^453]ཐུབ༌[^454]བཞིན། །

[Block 930]
གྲོལ་བར་མི་འགྱུར་ཞེས་བྱ་བ་ལྷག་མའོ། །

[Block 931]
འདི་དག་གིས་ནི་འདི་སྐད་སྟོན་པར་འགྱུར་ཏེ། གང་གིས་ཡི་གེ་གཉིས་མ་མཐོང་བར་བརྡ་ལ་སྤྱོད་པར་མི་འགྱུར་རོ། །

[Block 932]
གང་གིས་བརྡ་རྣམ་པར་སྤྱད་པར་མ་བྱས་པར་ནི་བརྡ་རྣམ་པར་ཤེས་པར་མི་འགྱུར་རོ། །

[Block 933]
གང་གིས་བརྡ་མ་ཤེས་པར་ནི་ཡི་གེའི་དེ་ཁོ་ན་ཉིད་ཤེས་པར་མི་འགྱུར་རོ། །

[Block 934]
གང་གིས་ཡི་གེའི་དེ་ཁོ་ན་ཉིད་ཤེས་པར་མ་གྱུར་པར་ནི་ཆོས་ཐམས་ཅད་ཀྱི་དེ་ཁོ་ན་ཉིད་ཤེས་པར་མི་འགྱུར་རོ། །

[Block 935]
གང་གིས་གང་དུ་གང་ཞིག་ཤེས་པ༌[^455]མ་གྱུར་པ་དེས་ནི་སྒྲ་ལ་འཇུག་པར་མི་འགྱུར་རོ། །

[Block 936]
གང་གིས་གང་ཞིག་གང་ལ་ཇི་ལྟར་གྱུར་པ་དེས་ནི་བསམ་གཏན་གྱི་སྦྱོར་བ་སྤངས་པར་འགྱུར་རོ། །

[Block 937]
གང་གིས་བསམ་གཏན་གྱི་སྦྱོར་བ་སྤངས་པ་དེས་ནི་ཐམས་ཅད་མཁྱེན་པ་དེ་ཁོ་ན་ཉིད་ཀྱི་དོན་ཡོངས་སུ་ཐོབ་པར་མི་འགྱུར་ཏེ༌[^456]ཕྱི་རོལ་པའི་དཀའ་ཐུབ་པ་གཞན་དུ་འགྱུར་བ་བཞིན་ནོ། །

[Block 938]
གཞན་ཡང་འདི་སྐད་དུ། སེམས་དཔའ་ཆེན་པོ་གཞན་ཡང་བྱང་ཆུབ་སེམས་དཔའ་ཆེན་པོས་དེ་ཁོ་ན་ཉིད་ཀྱི་སྦྱོར་བ་དང་བྲལ་ན་ནི་བདག་ཉིད་ཡོངས་སུ་གྲོལ་བར་མི་འགྱུར་རོ། །

[Block 939]
གང་གིས་གང་ཡོངས་སུ་གྲོལ་བར་མ་གྱུར་པ༌[^457]དེས་ནི་སེམས་ཅན་ཐམས་ཅད་འཁོར་བའི་རྒྱ་མཚོ་ལས་གྲོལ་བར་མི་ནུས་སོ། །

[Block 940]
སེམས་དཔའ༌[^458]ཆེན་པོ་རྣམ་གྲངས་དེས་ན་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོས་དེ་ཁོ་ན་ཉིད་དང་བྲལ་བར་མི་བྱའོ། །ཞེས་འབྱུང་བ་ལྟ་བུའོ། །

[Block 941]
གཞན་དག་ལས་ཀྱང་རིགས་ཀྱི་བུ་འམ་རིགས་ཀྱི་བུ་མོ་ལ་ལ་བདག་དང་གཞན་གྱི་དོན་ཐམས་ཅད་ཡོངས་སུ་རྫོགས་པར་འདོད་པས་མ་ནོར་བའི༌[^459]དེ་ཁོ་ན་ཉིད་དང་། གཞན་མ་ཡིན་པའི་དེ་ཁོ་ན་ཉིད་དང་། ཆོས་ཉིད་དང་ཆོས་ཀྱི་དབྱིངས་ཉིད་དང་། ཆོས་གནས་པ་ཉིད་དང་། ཆོས་སྐྱོན་མེད་པ་ཉིད་དང་། ཡང་དག་པའི་མཐའ་དང་། བསམ་གྱིས་མི་ཁྱབ་པའི་དབྱིངས་ཉིད་ལ་བསླབ་པར་བྱའོ། །དེ་ཅིའི་ཕྱིར་ཞེ་ན། འདི་ལྟར་གང་གིས༌[^460]ཚོགས་ཡོངས་སུ་རྫོགས་པར་འདོད་པ་དང་། བདག་དང་གཞན་ལ་ཕན་འདོགས་པར་འདོད་པའི་གང་ཟག་གིས་ལམ་འདི་ལ་མ་བརྟེན་པར་ནམ་ཡང་ཐོབ་པར་མི་འགྱུར་བའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ལ་སོགས་པ་རྒྱས་པར་གསུངས་སོ། །

[Block 942]
དེ་བས་ན་འདི་ནི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱིས༌[^461]ལམ་འདི་ལ་གནས་པར་བྱའོ། །

[Block 943]
ཨེ་ཝཾ་ཡིག་གཉིས་སྒྱུ་མ་ལ། །ཞེས་པ་ནི་ཇི་སྐད་དུ་བཤད་པའི་ཕྱིར་རོ། །

[Block 944]
ཐམས་ཅད་མཁྱེན་པ་འདིར་ཞུགས་པས་ཞེས་པ་ནི་ཐམས་ཅད་མཁྱེན་པ་ཐོབ་པའི་རྒྱུའི་གཙོ་བོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 945]
དེ་བས་ན༌[^462]ཞེས་པའི༌[^463]དོན་ནི་གོ་བར༌[^464]ཟད་དོ། །

[Block 946]
བདག་གིས་ཞེས་པ་ལ་སོགས་པ་ནི་འཆང་བར་འགྱུར་བའོ། །

[Block 947]
རྡོ་རྗེའི་ཚིག་ནི་རྡོ་རྗེ་འཆང་ཆེན་པོའི་ཚིག་ཡིན་པ་དང་། རྟོགས་པར་དཀའ་བ་ཉིད་ཀྱི་ཕྱིར་དེ་སྐད་ཅེས་བྱའོ། །

[Block 948]
བཤད་པའི་རྒྱུད་ལས་བསྟན་པ་ཉིད་ལ་འཇུག་པ་ནི་རྩ་བའི་རྒྱུད་ལས་གསལ་བར་མ་གསུངས་པའི་ཕྱིར་རོ། །

[Block 949]
འཁོར་ལོ་སྤྲུལ་པའི་ངོ་བོ་ལ། །ཞེས་པ་ནི་ལྷའི་འཁོར་ལོ་གཙོ་བོ་དང་འཁོར་གྱི་དཀྱིལ་འཁོར་ལྟ་བུའོ། །

[Block 950]
བདག་གིས་ཐོས་པ་ཞེས་གསུངས་ཏེ། ཞེས་པ་ནི་གང་གིས་དྲང་བའི་དོན་དུ་ཡིན་གྱི་ངེས་པའི་དོན་དུ་མ་ཡིན་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །
--- END BLOCKS ---
