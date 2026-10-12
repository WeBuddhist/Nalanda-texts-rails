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
[Block 701]
དེ་ལྟ་ན་ནི་དེ་ལས་བྱུང་བའམ། དེའི་བདག་ཉིད་ཀྱི་འབྲེལ་པར་ཡང་འགྱུར་རོ། །

[Block 702]
ཅི་སྟེ་གལ་ཏེ་ན་འབྲེལ་པ་ཡིན་ནོ་ཞེ་ན་ནི་དེ་ཉིད་འགལ་བར་རྣམ་པར་གནས་པར་ཡང་མི་རུང་སྟེ། མེ་དང་དུ་བ་བཞིན་ནོ། །

[Block 703]
ཅི་སྟེ་འགལ་བ་ཡིན་ནོ་ཞེ་ན་ནི། དེ་ལྟ་ན་ནི་འདི་ལ་འདུག་ས་གཅིག་པ་ལ་གནོད་པ་ཅི་ཞིག་ཡོད། །གལ་ཏེ་མི་གནོད་པ་ཅི་ཞིག་ཡོད༌[^335]དོ་ཞེ་ན༌[^336]མངོན་སུམ་དང་འགལ་བར་འགྱུར་རོ། །

[Block 704]
དེ་བས་ན་དོན་གཞན་ནི་བརྗོད་བྱ་མ་ཡིན་ནོ། །

[Block 705]
དོན་གྱི་སྒོ་ནས་ཀྱང་སྒྲ་ལ་བཤད་པར་བྱ་བའི་ཕྱིར་རིགས་པ་མ་ཡིན་ཏེ་གལ་ཏེ་དེ་ལྟ་ན་ནི་དོན་གོང་དུ་གཏན་ལ་དབབ་པར་འགྱུར་རོ། །

[Block 706]
དེ་ལྟ་ཡིན་ན་ནི་དོན་མེད་དོ་དེ་ལྟ་མ་ཡིན་ན་ནི་ཇི་ལྟར་དེ་ལས་འགྱུར། ཇི་སྟེ་གལ་ཏེ་ཡིན་ནོ་ཞེ་ན་ནི་ཧ་ཅང་ཡང་ཐལ་བར་འགྱུར་རོ། །

[Block 707]
དོན་སྔོན་དུ་གཏན་ལ་མི་འབེབས་ན་ནི་ནམ་ཡང་བརྗོད་པར་མི་བྱའོ། །

[Block 708]
དེ་ལས་གཞན་ཞིག་བརྗོད་དོ་ཞེ་ན་ནི་བརྗོད་པར་བྱའོ། །

[Block 709]
གལ་ཏེ་གང་ཟག་གི་དབྱེ་བས་ཡིན་ན་ནི་འདི་ཉིད་ལ་རྣམ་པ་བཞིར་གསུངས་པར༌[^337]མི་རིགས་ཀྱི་རྣམ་པ་གཞན་ལས་གཞན་དུ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 710]
གལ་ཏེ་འདི་ནི་ཡིན་ལ་གཞན་ནི་མ་ཡིན་ནོ་ཞེས་པའི་ངེས་པར་གཟུང་བ་ནི་ཅི་ཡང་མེད་དོ། །

[Block 711]
ཇི་སྟེ་ཡོད་ན་ནི་ཧ་ཅང་ཡང་མེད་པར་འགྱུར་རོ། །

[Block 712]
དེ་ལྟ་ཡིན་ན་ནི་རྒྱས་པ་དང་བསྡུས་པ་ཡང་མི་རིགས་སོ། །དེ་ཅིའི་ཕྱིར་ཞེ་ན། དོན་གྱི་རྣམ་པ་གཅིག་ལ་རྒྱ་ཆེ་བ་དང་ཆུང་བའི་བྱེ་བྲག་གིས་བསྡུས་པ་དང་རྒྱས་པར་འགྱུར་གྱི། དོན་ཐ་དད་པ་ལ་ནི་ནམ་ཡང་བསྡུས་པ་དང་རྒྱས་པ་མི་རིགས་སོ། །

[Block 713]
ཇི་སྟེ་གལ་ཏེ་ཡིན་ནོ་ཞེ་ན་ནི་ཧ་ཅང་ཡང་ཐལ་བར་འགྱུར་རོ། །

[Block 714]
མི་རྟོགས་པར་བྱ་བའི་ཕྱིར་ཡིན་ནོ་ཞེ་ན་ནི། འདི་ཅིའི་དབང་པོ་རྣོ་བའི་དབང་དུ་འམ། གདུག་སེམས་ཀྱིས་སྨྲས་ཞེས་རྟོག་གྲང་ན་རེ་ཞིག་དང་པོ་ལྟར་ན༌[^338]ནི་མ་ཡིན་ཏེ། ཚོགས་ཀྱི་གང་ཟག་ལ་སོགས་པ་གཟུང་བའི་ཕྱིར་རོ། །

[Block 715]
གཞན་ཡང་འདི་ཉིད་ལས།

[Block 716]
ཐུབ་པ་ཆེན་པོས་ཆོས་ཕུང་པོ། །ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པའི་ཕྱིར་རོ། །

[Block 717]
ཅི་སྟེ་ཕྱི་མ་ལྟར་ན་ཡང་མ་ཡིན་ཏེ། དེ་བཞིན་གཤེགས་པ་རྣམས་ནི་ཐུགས་རྗེ་ཆེན་པོའི་སྟོབས་ཀྱིས་འཇུག་པའི་ཕྱིར་རོ། །

[Block 718]
གདུག་སེམས་དང་སྙིང་རྗེ་ནི་གཅིག་གིས་གཅིག་སྤངས་པ་ཡིན་པའི་ཕྱིར་འགལ་བ་ཡིན་ནོ། །

[Block 719]
ཅི་སྟེ་དེ་ལྟ་ན་ཡང་ཡིན་ནོ་ཞེ་ན་ནི་ཧ་ཅང་ཡང་ཐལ་བར་འགྱུར་རོ་ཞེས་བྱ་བ་འདི་ཡང་བརྗོད་པར་བྱ་སྟེ། རེ་ཞིག་སྒྲ་དངོས་ཀྱི་ནུས་པའམ། དགོངས་ནས་བཤད་པའི་ནུས་པ་ཞེས་རྟོག་གྲང་ན། སྒྲ༌[^339]དངོས་ཀྱི་ནུས་པ་ལྟར་ན༌[^340]ནི་བདེན་ཏེ། དེ་ནི་མ་ཡིན་ནོ། །

[Block 720]
འདི་ནི་དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱིས་དགོངས་ནས་སྨྲས་པ་སྟེ་འདི་ཅི་ལ་དགོངས་ཤེ་ན། བཅོམ་ལྡན་འདས་ཉིད་ཀྱིས་ཀྱང་དང་པོ་བཤད་པ་བཞི་ལ་དགོངས་ནས་གསུངས་སོ། །

[Block 721]
དེས་དེ་ལྟར་འགྱུར་བ་ཡང་མ་ཡིན་ཏེ། ཐུགས་རྗེ་ཆེན་པོའི་དོན་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 722]
དེ་ལྟ་ན་ནི་ཡང་ཡིན་ནོ་ཞེ་ན་མ་ཡིན་ཏེ། གསང་བ་འདི་ནི་སེམས་ཅན་ཐམས་ཅད་ཀྱི་ཐུན་མོང་དུ་མ་གྱུར་པའི་ཕྱིར་རོ། །

[Block 723]
ཡང་ན་འདི་ནི་ཕྱི་རབས་པའི་གང་ཟག་སློབ་དཔོན་དང་སློབ་མར་འབྲེལ་པར་བྱ་བའི་ཕྱིར་ཏེ། འོག་ནས་བཤད་པའི་ཕྱིར་རོ། །

[Block 724]
བླ་མ་ལ་རག་ལས་པ་ཉིད་ཅིའི་ཕྱིར་ཞེ་ན། རྩོད་པའི་དུས་ན་སེམས་ཅན་ཐམས་ཅད་འདོད་རྒྱལ་གྱི་ཞགས་པས་ཟིན་ཏེ་གཟུ་ལུམ༌[^341]ལ་མཆོག་ཏུ་གཞོལ་བར་འགྱུར་རོ། །

[Block 725]
གང་གི་ཚེ་གཟུ་ལུམ༌[^342]ལ་མཆོག་ཏུ་གཞོལ་བ་དེ་ནི་དེ་བཞིན་གཤེགས་པའི་བཀའ་ཡང་དག་པར་མྱུར་དུ་འཇུག་པར་འགྱུར་རོ། །

[Block 726]
གང་ཞིག་གང་མྱུར་དུ་ཞུགས་པ་དེས་ནི་དེ་མ་ཐག་ཏུ་དེ་ལ་སྐྱོ་བར་འགྱུར་རོ། །

[Block 727]
གང་ཞིག་གང་ལ་མྱུར་དུ་སྐྱོ་བ་སྐྱེ་བར་འགྱུར་བ་དེ་ནི་དེའི་བཀའ་མྱུར་དུ་སྤོང་བར་འགྱུར་རོ། །

[Block 728]
གང་གིས་གང་ཞིག་མྱུར་དུ་སྤངས་པར་གྱུར་པ་དེ་ནི་བསྟན་པ་ཡུན་རིང་དུ་གནས་པར་མི་བྱེད་དེ་ཡུན་ཐུང་བར་བྱེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 729]
དེ་བས་ན་དེ་བཞིན་གཤེགས་པ་རྣམས་ནི་སློབ་དཔོན་དང་སློབ་མར་འབྲེལ་པར་བྱ་བ་དང་། བསྟན་པ་ཡུན་རིང་དུ་གནས་པར་བྱ་བ་དང་བསྟན་པ་བརྟན་པ་དང་། གང་ཟག་རྣམས་ཀྱི་བློ་ཟབ་ཅིང་རྒྱ་ཆེ་བར་བྱ་བའི་ཕྱིར་བཤད་པ་བཞི་ལ་དགོངས་ནས་གསུངས་པ་ཡིན་ནོ། །

[Block 730]
འདི་ཉིད་ནི་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་གསང་བ་མངོན་པར་གྲུབ་པ་ཞེས་བྱ་བའི་རྒྱུད་ལས་ཀྱང་།

[Block 731 [VERSE]]
དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི། །
གསང་བ་དེ་ཉིད་མངོན་གྲུབ་འདི། །
བདེ་གཤེགས་རྣམས་ཀྱིས་བསྟན་པ་རྣམས། །
ཡུན་རིང་གནས་པར་བྱ་བའི་ཕྱིར། །

[Block 732]
བཤད་པའི་མཆོག་ནི་རབ་སྦས་ཏེ། །བླ་མ་ལས་ནི་རྟོགས་པར་བྱ། །ཞེས་འབྱུང་བ་དང་། སློབ་དཔོན་གྱིས་ཀྱང་། བླ་མ་ལ་བརྙས་སྒྱུ་ཅན་དད་པ་མེད། །ཅེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པའི་ཕྱིར་རོ། །

[Block 733]
གཞན་ཡང་གསང་བ་ཆེན་པོ་ཞེས་བྱ་བ་རྣལ་འབྱོར་ཆེན་པོའི་རྒྱུད་ལས་ཀྱང་། སེམས་དཔའ་ཆེན་པོ་འཇིག་རྟེན་གྱི་ཁམས་འདིར་རྩོད་པ་རྒྱས་པའི་དུས་འདིར༌[^343]སེམས་ཅན་གཟུ་ལུམ༌[^344]མཁན་བླ་མ་ལ་སྡང་བ་དང་། ཆོག་པར་འཛིན་པ་དང་། དེ་བཞིན་གཤེགས་པའི་བཀའ་ཟབ་མོ་ལ༌[^345]རང་འདོད་དུ་སྤྱོད་པ་འབྱུང་གི་དེ་ཡིས༌[^346]དེ་བཞིན་གཤེགས་པའི་བཀའ་ཟབ་ཅིང་རྒྱ་ཆེ་བ་རྟོགས་པར་མི་ནུས་སོ། །

[Block 734]
དེ་བས་ན་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་གསང་བ་ཆེན་པོ་འདི་ནི་ཐེག་པ་ཆེན་པོའི་རིགས་ཅན་གྱི་གང་ཟག་རྨད་དུ་བྱུང་བའི་ཡུལ་ཡིན་པར་འགྱུར་རོ། །

[Block 735]
དེ་ཡང་གང་ལས་ཤེས་ཤེ་ན་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་གསང་བའི་ལུང་ལས་ཤེས་པར་འགྱུར་ཏེ། ཇི་སྐད་དུ།

[Block 736 [VERSE]]
དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི། །
གསང་བ་ཆེན་པོའི་བདག་ཉིད་མཆོག །
རབ་ཏུ་གསང་བ་ཡིན་པའི་ཕྱིར། །
ཐམས་ཅད་ཀུན་གྱིས༌[^347]གསལ་མ་བྱས། །

[Block 737 [VERSE]]
གང་ཡང་དུས་གསུམ་སངས་རྒྱས་དང་། །
རྣལ་འབྱོར་རྣལ་འབྱོར་མ་རྣམས་ཀྱིས། །
གང་ཚེ་གསང་བའི་དོན་གསུངས་པ། །
ཕྱི་དང་ཤིན་ཏུ་ནང་དག་དང་། །

[Block 738 [VERSE]]
དེ་བཞིན་བླ་མེད་ལ་དགོངས་ནས། །
གསང་བའི་དོན་རྣམས་གསུངས་པ་ཡིན། །
དེ་ལས་གཞན་དུ་གསུངས་གྱུར་ན། །
ཇི་བཞིན་དོན་དུ་བཟུང་བ་སྟེ། །
དེས་ན་ལམ་ངན་དག་ཏུ་ལྟུང་། །

[Block 739]
ཞེས་པ་ལ་སོགས་པ་འབྱུང་བ་ལྟ་བུའོ། །

[Block 740]
དེས་ན་དེ་བཞིན་གཤེགས་པའི་གསང་བ་ཆེན་པོ་འདི་ནི་རྣལ་འབྱོར་གྱི་རྒྱུད་རྣམས་ཀྱིས་ཤིན་ཏུ་རྒྱས་བཏབ་པ་ཡིན་ནོ་ཞེས་བསྟན་པར་བྱའོ། །
--- END BLOCKS ---
