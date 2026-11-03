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
[Block 316]
འཇམ་པ་ནི་ཚེ་འདི་ཉིད་ལ་བདེ་བ་ལ་རེག་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 317]
ཡིད་དུ་འོང་བ་ནི་དོན་བཟང་པོའི་ཕྱིར་རོ། །

[Block 318]
ཡིད་དུ་འཐད་པ་ནི་ཚིག་འབྲུ་བཟང་པོའི་ཕྱིར་རོ། །

[Block 319]
དག་པ་ནི་འཇིག་རྟེན་ལས་འདས་པ་བླ་ན་མེད་པའི་རྗེས་ལ་བྱུང་བའི་ཕྱིར་རོ། །

[Block 320]
དྲི་མ་མེད་པ་ནི་ཉོན་མོངས་པའི་བག་ལ་ཉལ་དང་། བག་ཆགས་ཐམས་ཅད་དང་བྲལ་བའི་ཕྱིར་རོ། །

[Block 321]
གསལ་བ་ནི་ཚིག་དང་ཡི་གེ་གྲགས་པའི་ཕྱིར་རོ། །

[Block 322]
སྙན་ཅིང་འཇེབས་པ་ནི་མུ་སྟེགས་ཅན་ཐམས་ཅད་ཀྱི་ལོག་པའི་བློ་གྲོས་དང་། ལྟ་བ་འཇིག་པའི་ཡོན་ཏན་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 323]
མཉན་པར་འོས་པ་ནི་སྒྲུབ་པས་ངེས་པར་འབྱིན་པའི་ཕྱིར་རོ། །

[Block 324]
མི་ཚུགས་པ་ནི་ཕས་ཀྱི་རྒོལ་བ་ཐམས་ཅད་ཀྱིས༌[^246]བར་མི་ཆོད་པའི་ཕྱིར་རོ། །

[Block 325]
སྙན་པ་ནི་དགའ་བར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 326]
དུལ་བ་ནི་འདོད་ཆགས་ཀྱི་གཉེན་པོར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 327]
མི་རྩུབ་པ་ནི་བསླབ་པ་བཅས་པ་ཐབས་སླ་བའི་ཕྱིར་རོ། །

[Block 328]
མི་བརླང་བ་ནི་དེ་ལས་འདས་པ་དག་ཡང་དག་པར་འབྱུང་བ་སྟོན་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 329]
རབ་ཏུ་དུལ་བ་ནི་ཐེག་པ་གསུམ་གྱིས་འདུལ་བ་སྟོན་པའི་ཕྱིར་རོ། །

[Block 330]
རྣར་སྙན་པ༌[^247]ནི་གཡེང་བའི་གཉེན་པོར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 331]
ལུས་སིམ་པར་བྱེད་པ་ནི་ཏིང་ངེ་འཛིན་ཐོབ་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 332]
སེམས་ཚིམ་པར་བྱེད་པ་ནི་ལྷག་མཐོང་གིས་མཆོག་ཏུ༌[^248]དགའ་བ་ཐོབ་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 333]
སྙིང་དགའ་བར་བྱེད་པ་ནི་ཐེ་ཚོམ་གཅོད་པའི་ཕྱིར་རོ། །

[Block 334]
དགའ་བདེ་བསྐྱེད་པ་ནི་ལོག་པར་ངེས་པ་སེལ་བའི་ཕྱིར་རོ། །

[Block 335]
ཡོངས་སུ་གདུང་བ་མེད་པ་ནི་བསྒྲུབ་པ་ལ་འགྱོད་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 336]
ཀུན་དུ་ཤེས་པར་བྱ་བ་ནི་ཐོས་པ་ལས་བྱུང་བའི་ཤེས་པ་ཕུན་སུམ་ཚོགས་པའི་གཞིར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 337]
རྣམ་པར་རིག་པར་བྱ་བ་ནི་བསམས་པ༌[^249]ལས་བྱུང་བའི་ཤེས་པ་ཕུན་སུམ་ཚོགས་པའི་གཞིར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 338]
རྣམ་པར་གསལ་བ་ནི་སློབ་དཔོན་གྱི་ཆོས་ཀྱི་དཔེ་མཁྱུད་མེད་པ་ལས་བྱུང་བའི་ཕྱིར་རོ། །

[Block 339]
དགའ་བར་བྱེད་པ་ནི་བདག་གི་དོན་རྗེས་སུ་ཐོབ་པ་རྣམས་དགའ་བར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 340]
མངོན་པར་དགའ་བར་བྱེད་པ་ནི་བདག་གི་དོན་མ་ཐོབ་པ་རྣམས་རེ་བར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 341]
ཀུན་ཤེས་པར་བྱེད་པ་ནི་བསམ་གྱིས་མི་ཁྱབ་པའི་ཆོས་ཡང་དག་པར་སྟོན་པའི་ཕྱིར་རོ། །

[Block 342]
རྣམ་པར་རིག་པར་བྱེད་པ་ནི་བསམ་དུ་ཡོད་པའི་ཆོས་ཡང་དག་པར་སྟོན་པའི་ཕྱིར་རོ། །

[Block 343]
རིགས་པ༌[^250]ནི་ཚད་མ་དང་མི་འགལ་བའི་ཕྱིར་རོ། །

[Block 344]
འབྲེལ་བ་ནི་ཅི་རིགས་པར༌[^251]འདུལ་བ་ལ་སྟོན་པའི་ཕྱིར་རོ། །

[Block 345]
ཟློས་པའི་སྐྱོན་མེད་པ་ནི་དོན་མེད་པ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 346]
སེང་གེའི་སྒྲའི་ཤུགས་ནི་མུ་སྟེགས་ཅན་གྱི་ཚོགས་ཐམས་ཅད་སྐྲག་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 347]
གླང་པོ་ཆེའི་སྒྲ་སྐད་ནི་སྒྲ་གསང་མཐོ་བའི་ཕྱིར་རོ། །

[Block 348]
འབྲུག་གི་སྒྲ་དབྱངས་ནི་ཟབ་པའི་ཕྱིར་རོ། །

[Block 349]
ཀླུའི་དབང་པོའི་སྒྲ་ནི་གཟུང་བར་འོས་པའི་ཕྱིར་རོ། །

[Block 350]
དྲི་ཟའི་གླུ་དབྱངས་ནི་སྙན་པའི་ཕྱིར་རོ། །

[Block 351]
བྱ་ཀ་ལ་པིང་ཀའི་སྒྲ་དབྱངས་བསྒྲགས་པ་ནི་མྱུར་དུ་འགྱུར་བའི་ངང་ཚུལ་ཅན་གྱི་ཕྱིར་རོ། །

[Block 352]
ཚངས་པའི་སྒྲ་དབྱངས་བསྒྲགས་པ་ནི་རྒྱང་རིང་དུ་གྲགས་པའི་ཕྱིར་རོ། །

[Block 353]
ཤང་ཤང་ཏེའུའི་སྒྲ་དབྱངས་སུ་གྲགས་པ༌[^252]ནི་ཐམས་ཅད་དུ༌[^253]གྲུབ་པ་ཐོག་མར་འགྲོ་བའི་བཀྲ་ཤིས་ཡིན་པའི་ཕྱིར་རོ། །

[Block 354]
ལྷའི་དབང་པོའི་དབྱངས་ལྟར་སྙན་པ་ནི་འགལ་བར་བྱ་བ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 355]
རྔའི་སྒྲ་ནི་བདུད་ཕྱིར་རྒོལ་བ་ཐམས་ཅད་ཕམ་པར་བྱ་བ་ལ་ཐོག་མར་འགྲོ་བའི་ཕྱིར་རོ། །
--- END BLOCKS ---
