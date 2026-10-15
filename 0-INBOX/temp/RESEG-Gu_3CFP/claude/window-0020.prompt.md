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
འདུས་བྱས་དང་འདུས་མ་བྱས་ཀྱི་དངོས་པོ་དེ་ཉིད་ལ་རྣམ་པར་ཕྱེ་བའི་རབ་ཏུ་དབྱེ་བ་ཚད་མེད་དེ་ཞེས་བྱ་བ་ལ། ཇི་ལྟར་བྱས་ནས་འདི་ལྟར་ཙམ༌[^522]ཞེ་ན། རང་གི་མཚན་ཉིད་ཕྱི་མ་ཕྱི་མའི་ཞེས་བྱ་བ་ལ་སོགས་པས་སོ། །

[Block 702]
འདུས་བྱས་ཀྱི་དངོས་པོ་ལ་ནི་རང་གི་མཚན་ཉིད་ལ་སོགས་པའི་རབ་ཏུ་དབྱེ་བ་ལེགས་པར་བསྟན་པ་ཡིན་ན། འདུས་མ་བྱས་ལ་རང་གི་མཚན་ཉིད་ལ་སོགས་པའི་དབྱེ་བ་ཇི་ལྟར་ཞེ་ན། དེ་དག་ཉིད་ཀྱི་རང་གི་མཚན་ཉིད་ལ་སོགས་པའི་དབྱེ་བས་ཐ་དད་པའི་འདུས་བྱས་ཀྱི་ཆོས་རྣམས་ཀྱི་ཆོས་ཉིད་དང་། དེ་བཞིན་ཉིད་ལ་འདིར་འདུས་མ་བྱས་ཞེས་འདུས་བྱས་ཀྱི་དངོས་པོས་བྱས་པ་ཉིད་ནི་འདུས་མ་བྱས་ཀྱི་དབྱེ་བ་ཞེས་བྱ་སྟེ། འདི་ལ་འགལ་བ་མེད་དོ། །

[Block 703]
རྣམ་གྲངས་གཞན་ཡང་ཞེས་བྱ་བ་ནི། སངས་རྒྱས་ཀྱི་ཆོས་ཐམས་ཅད་ཀྱི་བདག་ཉིད་ནི་སངས་རྒྱས་ཞེས་བྱ་བར་བསྟན་པའི་དོན་དུ་རྣམ་གྲངས་གཞན་བརྩམས་པའོ། །

[Block 704]
དམ་པ་བདུན་གྱི་བསྡུས་པའི་དོན་ནི། གང་ལ་བརྟེན་པ་དང་། གང་གི་དོན་དུ་བསྒྲུབ་པ་དང་། གང་ལ་གནས་པ་དང་། ཐབས་གང་གིས་དང་། འབྲས་བུ་གང་ཐོབ་པ་དང་། གནས་པ་གང་གིས་གནས་པ་ཞེས་བྱ་བའོ། །

[Block 705]
དམ་པ་འདི་དག་ཉིད་ནི་དམ་པ་བདུན་ཏེ། སྦྱོར་བ་གང་གིས་དམ་པ་ཡིན་པ་ནི་བྱང་ཆུབ་ཅེས་བརྗོད་དོ། །

[Block 706]
དེ་ལ་གང་ལ་རབ་ཏུ་གནས་ན་ནི། ཚུལ་ཁྲིམས་ལ་རབ་ཏུ་གནས་སོ། །

[Block 707]
ཐབས་གང་གིས་ཤེ་ན། ཡེ་ཤེས་དམ་པ་ཉིད་ཀྱིས་ཉོན་མོངས་པ་མེད་པའི་ཐབས་དང་མཐུ་ཉིད་ཀྱིས་སྐྱོ་བ་མེད་པའི་ཐབས་ཀྱིས་སོ། །

[Block 708]
འབྲས་བུ་གང་འཐོབ་པ་ནི་ཉོན་མོངས་པ་དང་ཤེས་བྱའི་སྒྲིབ་པ་སྤངས་པའི་འབྲས་བུའོ། །

[Block 709]
གང་གི༌[^523]གནས་ན་གནས་པ་གསུམ་གྱིས་སོ། །

[Block 710]
ཕྱིན་ཅི་མ་ལོག་པར་གསུངས་པས༌[^524]དེ་བཞིན་གཤེགས་པ་ཞེས་བྱའོ་ཞེས་བྱ་བ་ནི་དེ་བཞིན་གཤེགས་པ་ནི་འདིར༌[^525]འདི་ལྟར་ཡི་གེ་ཏར་བསྒྱུར་བ་བྱས་ནས་དེ་བཞིན་གཤེགས་པའོ། །

[Block 711]
དེ་བཞིན་གཤེགས་པ་དེ་ཐོབ་པར་བྱ་བའི་དོན་ཐམས་ཅད་བརྙེས་པའི་ཕྱིར་དགྲ་བཅོམ་པའོ། །

[Block 712]
དེས༌[^526]ན་འཇིག་རྟེན་ན་དགྲ་བཅོམ་པ་ཆེན་པོ་ཞེས་བརྗོད་དོ།[^527] །ཐོབ་པར་བྱ་བའི་དོན་ཐམས་ཅད་ཀྱི་ཕྱིར་དང་། གང་འཇིག་རྟེན་གྱི་རིན་པོ་ཆེ་ལ་སོགས་པས་བཅོམ་ལྡན་འདས་དེ༌[^528]མཆོད་པར་འོས་པས་ཀྱང་བརྗོད་དེ། དེ་ཐོབ༌[^529]པར་བྱ་བའི་དོན་ཐམས་ཅད་ཐོབ་པའི་ཕྱིར་རམ། བླ་ན་མེད་པའི་བསོད་ནམས་ཀྱི་ཞིང་ཡིན་པ་ཉིད་དེ་གཉི་གས་ཀྱང་མཆོད་པར་འོས་པའི་ཕྱིར་ཡང་ངོ་། །ཆོས་རྣམས་ཇི་ལྟ་བ་བཞིན་དུ་དོན་དམ་པར་ཐུགས་སུ་ཆུད་པས་ཞེས་བྱ་བ་ལ། ཆོས་རྣམས་ཇི་ལྟ་བ་བཞིན་དུ་ཐུགས་སུ་ཆུད་པས་ཞེས་བྱ་བས་ནི། ཡང་དག་པར་ཞེས་བྱ་བའི་སྒྲའི་དོན་བསྟན་ཏོ། །

[Block 713]
དོན་དམ་པར་ཆོས་རྣམས་ཐུགས་སུ་ཆུད་པས་ཞེས་བྱ་བས་ནི། རྫོགས་པའི་ཞེས་བྱ་བའི་སྒྲའི་དོན་བསྟན་ཏོ། །

[Block 714]
རིག་པ་གསུམ་ཞེས་བྱ་བ་ནི། སྔོན་གྱི་གནས་རྗེས་སུ་དྲན་པ་མཁྱེན་པའི་རིག་པ་དང་། འཆི་འཕོ་དང་སྐྱེ་བ་མཁྱེན་པའི་རིག་པ་དང་། ཟག་པ་ཟད་པ་མཁྱེན་པའི་རིག་པའོ། །

[Block 715]
རིག་པ་དེ་དག་ནི་སྔོན་དང་ཕྱི་མ་ལ་སོགས་པ་མི་རིག་པ་ཟློག༌[^530]པར་བྱེད་པའི་མཚན་ཉིད་ཅན་ཏེ། མདོ་ལས་ཇི་སྐད་གསུངས་པ༌[^531]བཞིན་ནོ། །

[Block 716]
ཚུལ་ཁྲིམས་ལས་བརྩམས་ནས་ཏིང་ངེ་འཛིན་གྱི་བར་ནི་ཞབས་ཏེ་དེས་འགྲོ་བར་བྱེད་པས་སོ། །

[Block 717]
ལྷག་མཐོང་གི་ཕྱོགས་ནི་རིག་པའོ། །

[Block 718]
ཞི་གནས་ཀྱི་ཕྱོགས་ནི་ཏིང་ངེ་འཛིན་ཏོ། །

[Block 719]
དེ་གཉི་གའི་ཕྱོགས་ནི་ཚུལ་ཁྲིམས་ཏེ་མཆོག་ཏུ་མཐར་ཕྱིན་པར་བྱིན་པས་སོ། །

[Block 720]
ཇི་སྲིད་འགོད་པར༌[^532]བྱ་བར་བྱོན་པའི་དོན་གྱིས་དང་། ཡང་མི་ལྡོག་པར་གཤེགས་པས་བདེ་བར་གཤེགས་པའོ། །

[Block 721]
དེ་ཉིད་ཀྱིས་ན་བཅོམ་ལྡན་འདས་བླ་ན་མེད་པ་སྐྱེས་བུ་འདུལ་བ་ཁ་ལོ་སྒྱུར་བ༌[^533]ཞེས་བྱའོ། །

[Block 722]
སེམས་འདུལ་བའི་ཐབས་དམ་པ་མཁྱེན་པ་ཞེས་བྱ་བ་ནི། སྐྱེས་བུ་དམ་པས་འདུལ་བ་ནི་འདུལ་བར༌[^534]བྱ་བ་སྟེ། ཅི་ཞེ་ན་སེམས་སོ། །

[Block 723]
དེ་འདུལ་བའི་ཐབས་མཁྱེན་པའི་ཕྱིར་བླ་ན་མེད་པ། [^535]སྐྱེས་བུ་འདུལ་བ་ཁ་ལོ་སྒྱུར་བ་ཞེས་བྱ་བ་ལ། ཁ་ལོ་སྒྱུར་བ་ནི་འཇིག་རྟེན་ན་འདུལ་བའི་ཐབས་ཤེས་པ་ལྟ་བུའོ། །

[Block 724]
དེས་ན་དེ་བླ་ན་མེད་པ་ཞེས་བྱ་བ་སྟེ། ཁྱད་པར་དུ་འཕགས་པའི་འདུལ་བའི་ཐབས་མཁྱེན་པའི་ཕྱིར༌[^536]རོ། །

[Block 725]
ལྷ་དང་མི་རྣམས་ཀྱི་སྟོན་པ་ཞེས་བྱ་བ་ལ། ལེགས་པར༌[^537]སྟོན་པར་མཛད་པ་ཉིད་ཀྱི༌[^538]སྟོན་པ་སྟེ། དོན་འདི་ཉིད་གསལ་བར་བསྟན་པའི་ཕྱིར་སྨྲས་པ། ཡང་དག་པར་ཞེས་བྱ་བས་སྟོན་པའི་དོན་བཤད་དེ། ཅི་ཞིག་བཤད་ཅེ་ན། སྨྲས་པ། སྡུག་བསྔལ་ཐམས་ཅད་ལས་ངེས་པར་འབྱུང་བའོ། །གང་གི་ཞེ་ན། སྨྲས་པ། ལྷ་དང་མི་རྣམས་ཀྱིའོ། །ཇི་ལྟར་བསྟན་ཞེ་ན། འདིའི་དོན་བསྟན་པར་བྱ་བའི་ཕྱིར་སྨྲས་པ། མིག་ཏུ་གྱུར་པའི་ཕྱིར་དང་། ཡེ་ཤེས་སུ་གྱུར་པའི་ཕྱིར་དང་། དོན་དུ་གྱུར་པའི་ཕྱིར་དང་། ཆོས་སུ་གྱུར་པའི་ཕྱིར་རོ། །ཇི་ལྟར་མིག་ཏུ་གྱུར་པ་ཡིན་ཞེ་ན། སྨྲས་པ། དོན་གསལ་བ་གཏན་ལ་འབེབས་པའི་ཕྱིར་རོ། །

[Block 726]
དོན་གསལ་བ༌[^539]གཏན་ལ་འབེབས་པ་ཉིད་ཡང་དག་པར་བསྟན་པ་ནི།

[Block 727]
ཇི་ལྟར་སློབ་དཔོན་མ་ཁོལ་གྱིས༌[^540]བསྟོད་པ་བཞི་བརྒྱ་པ་ལས།

[Block 728 [VERSE]]
ཁྱོད་ཀྱི་བསྟན་ལ་མ་བརྟེན་པར། །
དེ་ཉིད་མཐོང་བ་འགའ་ཡང་མེད། །
ལོང་བ་ལྟ་བུའི་འཇིག་རྟེན་གྱི། །
མིག་ཏུ་གྱུར་པ་ཁྱོད་ལ་འདུད། །

[Block 729]
ཅེས་བསྟན་པས་དེ་ཁོ་ན་ཉིད་གསལ་བར་བརྗོད་པས་དེ་སྟོན་པས་སམ། ཡང་ན་དོན་གསལ་བར་གཏན་ལ་འབེབས་པ་ཉིད་ཀྱིས་མིག་ཏུ་གྱུར་པ་སྟེ། རང་ཉིད་ཀྱིས༌[^541]རབ་ཏུ་བསྟན་པའི་དོན་ངེས་པར་མཛད་པའི་ཕྱིར། ངེས་པར་སྐྱེད་པར་བྱེད་པའི་དོན་ཏོ། །

[Block 730]
ཇི་ལྟར་སྣང་བས་ཡོངས་སུ་འཛིན་པའི༌[^542]གཟུགས་ནི་རབ་ཏུ་མཐོང་བར་གྱུར་པ༌[^543]དེ་བཞིན་དུ། བཅོམ་ལྡན་འདས་ཁོ་ན་སྣང་བར་གྱུར་པ་ཡིན་ཏེ། དོན་གསལ་བར་གཏན་ལ་འབེབས་པའི་ཕྱིར་རོ། །

[Block 731]
དེ་ལྟ་བས་ན་བཅོམ་ལྡན་འདས་ནི་སྣང་བར་གྱུར་པ་ཡིན་ཏེ།

[Block 732]
ཇི་ལྟར་སློབ་དཔོན་མ་ཁོལ་གྱིས༌[^544]བསྟོད་པ་བཞི་བརྒྱ་པ་དེ་ཉིད་ལས།

[Block 733 [VERSE]]
[^545] མེ་དང་མར་མེའི་འོད་ཡོད་ཅིང་། །
ཟླ་སྐར་ནོར་བུ་ཡོད་གྱུར་ཀྱང་། །
ཉི་མ་མེད་ན་ས་སྟེང་འདི། །
གསལ་བས་རྒྱས་པར་མི་འགྱུར་ལ། །

[Block 734 [VERSE]]
དེ་ལས་གཞན་པའི་སྣང་བའམ། །
དེ་ལས་ཁྱད་འཕགས་གཞན་དག་ནི། །
ཡོད་ཀྱང་ཁྱོད་མེད་འགྲོ་བ་འདི། །
སྣང་བ་མེད་པར་གྱུར་པ༌[^546]ཡིན། །

[Block 735 [VERSE]]
ཇི་ལྟར༌[^547]མ་རིག་མུན་པ་ཡི། །
སྒྲིབ་པས་སེམས་ནི་ཡོངས་བཀག༌[^548]པས། །
མུན་པར་གྱུར་པའི་འཇིག་རྟེན་གྱི། །
སྣང་བར་གྱུར་པ་ཁྱོད་ལ་འདུད། །

[Block 736]
ཅེས་བསྟན་པས་དེ་ལྟ་བས་ན་སྣང་བར་གྱུར་པ་ཉིད་ཀྱིས་སྣང་བར་གྱུར་བ་ཞེས་བརྗོད་པ་ཡིན་ནོ། །ཇི་ལྟར་དོན་དུ་གྱུར་བ་ཡིན་ཞེ་ན། སྨྲས་པ། དོན་ཐམས་ཅད་སྟོན་པའི་ཕྱིར་ཞེས་བྱ་བ་སྟེ། དོན་ཐམས་ཅད་ནི་འདུས་བྱས་དང་འདུས་མ་བྱས་ལ་སོགས་པའོ། །

[Block 737]
འདི་ལྟར་རོ་ཞེས་སྟོན་པར་བྱེད་པའི་དོན་གྱིས་སྟོན་པ༌[^549]སྟེ། ཤེས་པར་འདོད་པས་སྟོན་པ་དེ་ཡང་བཅོམ་ལྡན་འདས་ལ༌[^550]མ་བརྟེན་པར་དེ་རྟོགས་པ་མེད་པས་སོ། །

[Block 738]
དེ་ཡང་ཇི་ལྟར་སློབ་དཔོན་མ་ཁོལ་གྱིས༌[^551]བསྟོད་པ་དེ་ཉིད་ལས།

[Block 739 [VERSE]]
དོན་ནི་དོན་དུ་མ་རིག་ཅིང་། །
དོན་མ་ཡིན་ཡང་དོན་མིན་དུ། །
བློ་ཡིས་ཆོས་ནི་མ་རྟོགས་པ། །
ཁྱོད་ལ་བརྟེན་ནས་རྟོགས་པ་ཡིན། །

[Block 740 [VERSE]]
ཕལ་ཆེར་དོན་མིན་སྤོང་འདོད་ཀྱང་། །
རྨོངས་པས་དོན་ནི་སྤོང་འགྱུར་ཏེ། །
མི་ཤེས་པ་ནི་དོན་འདོད་ཀྱང་། །
དོན་མ་ཡིན་པ་གྲུབ་པར༌[^552]འགྱུར། །
--- END BLOCKS ---
