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
[Block 771]
དེའི་འོག་ཏུ་ཇི་ལྟར་གནས་པར་བྱ་ཞེས་དྲིས་པ་ལ་གནས་པར་མི་བྱ་བ་ཡོངས་སུ་སྤངས་ཏེ་གནས་པར་བྱ་བས་གནས་པ་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་གནས་པ་ཞེས་བྱ་བར་སྟོན་ཏོ། །

[Block 772]
གཟུགས་ནི་གཟུགས་ཀྱིས་སྟོང་ངོ་ཞེས་བྱ་བ་ལ་སོགས་པས་སྟོང་པ་ཉིད་རྟོགས་པ་ནི་གནས་པའོ། །

[Block 773]
དམིགས་པའི་ཚུལ་ནི་གནས་པ་མ་ཡིན་ནོ་ཞེས་སྟོན་ཏེ། དེས་ནི་འདི་སྐད་དུ་གང་གི་ཕྱིར་གཟུགས་ལ་སོགས་པ་ཀུན་བརྟགས་པའི་ཆོས་འདི་དག་གཟུགས་ལ་སོགས་པའི་ངོ་བོ་ཉིད་ཀྱིས་ཡོད་པ་མ་ཡིན་ལ། བྱང་ཆུབ་སེམས་དཔའ་ཡང་བྱང་ཆུབ་སེམས་དཔའི་ངོ་བོ་ཉིད་ཀྱིས་མེད་པ་སྟེ། དེ་དག་གི༌[^522]སྟོང་པ་ཉིད་གང་ཡིན་པ་དེ༌[^523]ཐ་མི་དད་དེ་གཅིག་གོ། །

[Block 774]
དེ་བས་ན་ཆོས་ཉིད་ཀྱི་གཟུགས་ལ་སོགས་པ་ནི་ཡོངས་སུ་གྲུབ་པ་ཡིན་ལ་བྱང་ཆུབ་སེམས་དཔའ་ཡང་གཉིས་སུ་མེད་པ་སྟེ། གཅིག་པའི་ཆོས་ཉིད་དུ་གནས་པ་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་གནས་པའོ་ཞེས་བསྟན་ཏོ། །

[Block 775 [HEADING]]
###### གནས་པར་མི་བྱ་བའི་འགྲེས། ^1-2-1-2-1-0

[Block 776]
གནས་པར་མི་བྱ་བའི་འགྲེས་ལ་ཡང་རྣམ་པ་གསུམ་དུ་བསྟན་ཏེ། ཆོས་ལ་གནས་པར་མི་བྱ་ཞེས་བྱ་བ་ནི་གཅིག་པའོ། །

[Block 777]
ཆོས་ཉིད་ལ་གནས་པར་མི་བྱ་ཞེས་བྱ་བ་ནི་གཉིས་པའོ། །

[Block 778]
གང་ཟག་རྣམས་ལ་གནས་པར་མི་བྱ་ཞེས་བྱ་བ་ནི་གསུམ་པའོ། །

[Block 779 [HEADING]]
###### **ཆོས་ཀྱི་འགྲེས།** ^1-2-1-2-1-1-0

[Block 780]
དེ་ལ་ཆོས་ཀྱི་འགྲེས་ལ་ཡང་རྣམ་པ་གཉིས་སུ་བསྟན་ཏེ། ཆོས་བསྟན་པ་དང་། ཆོས་ཀྱི་མཚན་ཉིད་བསྟན་པའོ། །

[Block 781 [HEADING]]
###### **ཆོས་བསྟན་པ།** ^1-2-1-2-1-1-1-0

[Block 782]
དེ་ལ་གཟུགས་ལ་དམིགས་པའི་ཚུལ་གྱིས༌[^524]གནས་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནས། སངས་རྒྱས་ཉིད་ལ་དམིགས་པའི་ཚུལ་གྱིས་གནས་པར་མི་བྱའོ་ཞེས་བྱ་བའི་བར་དུ་ནི་ཆོས་བསྟན་པའོ། །

[Block 783 [HEADING]]
###### **ཆོས་ཀྱི་མཚན་ཉིད་བསྟན་པ།** ^1-2-1-2-1-1-2-0

[Block 784]
ཀཽ་ཤི་ཀ་དེ་ལྟར་ན་གཟུགས་ཞེས་བྱ་བར་གནས་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནས། དེ་ལྟར་ན་སངས་རྒྱས་ཉིད་ཅེས་བྱ་བར་དམིགས་པའི་ཚུལ་གྱིས་གནས་པར་མི་བྱའོ་ཞེས་བྱ་བའི་བར་ནི་ཆོས་ཉིད་ཀྱི་མཚན་ཉིད་བསྟན་པའོ། །

[Block 785 [HEADING]]
###### **ཆོས་ཉིད་ཀྱི་འགྲེས།** ^1-2-1-2-1-2-0

[Block 786]
ཆོས་ཉིད་ཀྱི་འགྲེས་ལ་ཡང་རྣམ་པ་གསུམ་དུ་བསྟན་ཏེ། ཐམས་ཅད་ཤེས་པ་ཉིད་ཀྱི་ཕྱོགས་ཀྱི་ཆོས་ཉིད་བསྟན་པ་དང་། ལམ་གྱི་རྣམ་པ་ཤེས་པ་ཉིད་ཀྱི་ཕྱོགས་ཀྱི་ཆོས་ཉིད་བསྟན་པ་དང་། རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཀྱི་ཕྱོགས་ཀྱི་ཆོས་ཉིད་བསྟན་པའོ། །

[Block 787 [HEADING]]
###### **ཐམས་ཅད་ཤེས་པ་ཉིད་ཀྱི་ཕྱོགས་ཀྱི་ཆོས་ཉིད།** ^1-2-1-2-1-2-1-0

[Block 788]
གཟུགས་རྟག་གོ་ཞེས་གནས་པར་མི་བྱ། མི་རྟག་གོ་ཞེས་ཀྱང་གནས་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནས་དེ་བཞིན་གཤེགས་པ་དགྲ་བཅོམ་པ་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་ནི་སྦྱིན་གནས་སོ་ཞེས་བྱ་བར་དམིགས་པའི་ཚུལ་གྱིས་གནས་པར་མི་བྱའོ་ཞེས་བྱ་བའི་བར་དུ་ནི་ཐམས་ཅད་ཤེས་པ་ཉིད་ཀྱི་ཕྱོགས་ཀྱི་ཆོས་ཉིད་བསྟན་པའོ། །

[Block 789 [HEADING]]
###### **ལམ་གྱི་རྣམ་པ་ཤེས་པ་ཉིད་ཀྱི་ཕྱོགས་ཀྱི་ཆོས་ཉིད།** ^1-2-1-2-1-2-2-0

[Block 790]
ས་དང་པོ་ནས་ས་བཅུ་པའི་བར་ལ་གནས་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནས། སེམས་ཅན་ཚད་མེད་གྲངས་མེད་དཔག་ཏུ་མེད་པ་དག༌[^525]བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ལ་རབ་ཏུ་དགོད་པར་བྱའོ་ཞེས་བྱ་བར་དམིགས་པའི་ཚུལ་གྱིས་གནས་པར་མི་བྱའོ་ཞེས་བྱ་བའི་བར་དུ་ནི་ལམ་གྱི་རྣམ་པ་ཤེས་པ་ཉིད་ཀྱི་ཕྱོགས་དང་མཐུན་པའི༌[^526]ཆོས་ཉིད་བསྟན་པའོ། །

[Block 791 [HEADING]]
###### **རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཀྱི་ཕྱོགས་ཀྱི་ཆོས་ཉིད།** ^1-2-1-2-1-2-3-0

[Block 792]
མིག་ལྔ་བསྒྲུབ་པར་བྱ་སྟེ་ཞེས་བྱ་བ་ནས་བཟུང་སྟེ། [^527]དཔེ་བྱད་བཟང་པོ་བརྒྱད་ཅུ་ལུས་ལ་བསྒྲུབ་པར་བྱའོ་ཞེས་བྱ་བར་གནས་པར་མི་བྱའོ་ཞེས་བྱ་བའི་བར་དུ་ནི་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཀྱི་ཕྱོགས་ཀྱི་ཆོས་ཉིད་བསྟན་པའོ། །

[Block 793 [HEADING]]
###### **གང་ཟག་བསྟན་པའི་འགྲེས།** ^1-2-1-2-1-3-0

[Block 794]
གང་ཟག་བསྟན་པའི་འགྲེས་ལ་ཡང་ཐམས་ཅད་ཤེས་པ་ཉིད་ཀྱི་ཕྱོགས་ལ་སོགས་པའི་དབང་གིས་རྣམ་པ་གསུམ་དུ་སྦྱར་བར་བྱ་སྟེ། རྫུ་འཕྲུལ་གྱི་རྐང་པ་བཞི་ལ་གནས་ཏེ། ཏིང་ངེ་འཛིན་གང་ལ་སྙོམས་པར་ཞུགས་པས་ཞེས་བྱ་བ་ལ་སོགས་པ་ཡང་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཀྱི་སའི་ཕྱོགས་ཀྱི་ཆོས་སོ། །

[Block 795]
འོ་ན༌[^528]ཇི་ལྟར་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་གནས་པར་བྱ་སྙམ་ཞེས་བྱ་བ་གནས་བརྟན་རབ་འབྱོར༌[^529]ཅི་ལས་སེམས་པར་གྱུར་ཅེ་ན། ཆོས་ཐམས་ཅད་ལ་གནས་པར་མི་བྱའོ་ཞེས་བཤད་ཅིང་སྟོང་པ་ཉིད་ལ་ནི་གནས་པར་མི་ནུས་ལ་གནས་པར་མི་བྱའོ་ཞེས་ཀྱང་བཤད་ན་དེ༌[^530]ཇི་ལྟར་རིགས་པར་འགྱུར་སྙམ་དུ་སེམས་པར་གྱུར་ཏོ། །

[Block 796]
དེ་ནས་གནས་བརྟན་རབ་འབྱོར་གྱིས་མི་གནས་པར་སྒྲུབ་པ་ཉིད། ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་གནས་པ་ཡིན་པར་བསྟན་པ། དེ་བཞིན་གཤེགས་པའི་ཐུགས་ནི་ཅི་ལའང་གནས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་སྟེ་མི་གནས་པའི་མྱ་ངན་ལས་འདས་པ་ལ་བཞུགས་པར་བསྟན༌[^531]ཏོ། །

[Block 797]
དེ་ལྟར་མི་གནས་པ་ལ་གནས་པའི༌[^532]བསྒྲུབ་པ་བཤད་པས་གདུལ༌[^533]བ་ལས་བརྩམས་ཏེ་བཤད་པ་ལ་བརྗོད་དུ་མེད་པར་བཤད་པས་འདུལ་བ་གང་ཡིན་པ་དེ་དག་ཐེ་ཚོམ་ཟོས་པར་གྱུར་ཏེ། དེ་བས་ན་དེ་དག་ལ་བརྩམས་ནས་བཤད་པ་གཞན་སྐབས་ཕྱ་སྟེ། ལྷའི་བུ་དག་གང་སྨྲས་པ་ཤེས་པར་མི་རུང་ངམ་ཞེས་བྱ་བ་ལ་སོགས་པས་གང་བརྗོད་པ་དེ་དག་ཅིའི་ཕྱིར་མི་ཤེས་སམ་ཞེས༌[^534]ལྷའི་བུ་རྣམས་ལ་དྲིས་པ་དང་། དེའི་ཕྱིར་དེ་དག་གིས། འཕགས་པ་རབ་འབྱོར་ཤེས་པར་མི་རུང་ངོ་ཞེས་སྨྲས་ཏེ། དེ་ནས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བརྗོད་དུ་མེད་པ་ཡིན་པའི་ཕྱིར་གནས་བརྟན་གྱིས༌[^535]ཡི་གེ་གཅིག་ཀྱང་མ་བརྗོད་དེ་ཞེས་བྱ་བ་གསུངས་ཏེ། འདི་ལྟར་དེ་ན་བཤད་པར་སྣང་བ་དང་། མཉན་པར༌[^536]སྣང་བ་དེ་ནི་ཀུན་བརྟགས་པ་ཡིན་ནོ་ཞེས་སྤྲུལ་པ་དང་། རྨི་ལམ་དང་། བྲག་ཅ་དང་། སྒྱུ་མ་ལྟ་བུར་བསྟན་པས༌[^537]ལྷའི་བུ་དེ་རྣམས་དགའ་བར་བྱས་སོ། །

[Block 798]
སངས་རྒྱས་ཀྱི༌[^538]སྤྲུལ་པ་ཞེས་བྱ་བ་ནི་དེ་བཞིན་གཤེགས་པའི༌[^539]སྤྲུལ་པའོ། །

[Block 799]
ལྷའི་བུ་དག་གཟུགས་ནི་ཟབ་པ་མ་ཡིན་ཕྲ་བ་མ་ཡིན་ཞེས་བྱ་བ་ནི་ཀུན་བརྟགས་པའི་གཟུགས་ཡང་དག་པ་མ་ཡིན་པའི་ཕྱིར་ཟབ་པ་མ་ཡིན་ཕྲ་བ་མ་ཡིན་ནོ། །

[Block 800]
ཡང་ལྷའི་བུ་དག་འདི་ལྟར་གཟུགས་ཀྱི་རང་བཞིན་ནི་ཟབ་པ་མ་ཡིན་ཕྲ་བ་མ་ཡིན་ཞེས་བྱ་བ་ལ་སོགས་པས་ཆོས་ཉིད་ཀྱི་གཟུགས་ནི་ངོ་བོ་ཉིད་ཀྱིས་མི་གཡོ་བའི་ཕྱིར་ཟབ་པ་མ་ཡིན། ཕྲ་བ་མ་ཡིན་ནོ་ཞེས་བསྟན་ཏོ། །

[Block 801]
དེ་བས་ན་འདིར་ནི་འགྲེས་རྣམ་པ་གཉིས་ཏེ། ཆོས་ཀྱི་འགྲེས་དང་རང་བཞིན་གྱི་འགྲེས་སོ། །

[Block 802]
འོ་ན་ཆོས་བསྟན་པ་འདི་ལ་གཟུགས་སུ་བརྟགས་པ་ཡང་མེད་དམ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་གལ་ཏེ་ཆོས་ཐམས་ཅད་བརྗོད་དུ་མེད་ན་དེ་ལྟ་ན་ནི་གཟུགས་ལ་སོགས་པ་ལ་མ་བརྟགས་སམ། མ་བཤད་དམ་ཞེས་ལྷའི་བུ་རྣམས་ཀྱིས་དྲིས་པ་དང་། དེ་ནས་གནས་བརྟན་རབ་འབྱོར་གྱིས་ལྷའི་བུ་དག་དེ་དེ་བཞིན་ནོ་དེ་དེ་བཞིན་ཏེ་ཞེས་བརྟགས་པ་མེད་པ་དང་། བཤད་པ་མེད་པ་ཉིད་དུ༌[^540]བསྟན་ཏོ། །

[Block 803]
བཟོད་པ་འདི་ལ་མི་བརྟེན་དུ་མི་རུང་ཞེས་བྱ་བ་ནི་བརྗོད་དུ་མེད་པའི་བཤད་པ་འདི་ལའོ། །

[Block 804]
གནས་བརྟན་རབ་འབྱོར་ལ་ཆོས་ཉན་པ་རྣམ་པ་ཇི་ལྟ་བུ་དག་ཏུ་འདོད་པར་བྱ་སྙམ་མོ་ཞེས་བྱ་བ་ནི། གལ་ཏེ་དོན་དམ་པར༌[^541]བརྗོད་དུ་མེད་པ་ཡིན་ན། འཆད་པ་པོ་དང་ཉན་པ་པོ་མེད་པས། ཆོས་ཉན་པ་ཡང་མེད་པར་འགྱུར་རོ་ཞེས་སྟོན་ཏོ། །

[Block 805]
དེ་ན༌[^542]གནས་བརྟན་རབ་འབྱོར་གྱིས་ལྷའི་བུ་དག་བདག་ལ་ཆོས་ཉན་པ་ནི་སྒྱུ་མ་ལྟ་བུར་འདོད་པར་བྱའོ་ཞེས་བྱ་བ་ལ་སོགས་པས་དོན་དམ་པར་འཆད་པ་པོ་དང་། ཉན་པ་པོ་མེད་པ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 806]
བཙུན་པ་རབ་འབྱོར་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་འདི་ལྟར་ཟབ་པ། འདི་ལྟར་མཐོང་བར་དཀའ་བ་ཞེས་བྱ་བ་ལ། གཏིང་དཔག་དཀའ་བས་ན་ཟབ་པའོ། །

[Block 807]
རྣམ་པར་ཤེས་པའི་ཚོགས་ལྔའི་ཡུལ་མ་ཡིན་པའི་ཕྱིར་མཐོང་བར༌[^543]དཀའ་བའོ། །

[Block 808]
ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་ཡུལ་མ་ཡིན་པའི་ཕྱིར་རྟོགས་པར་དཀའ་བའོ། །

[Block 809]
ཉོན་མོངས་པ་དང་ཉེ་བའི་ཉོན་མོངས་པ་ཐམས་ཅད་ཉེ་བར་ཞི་བའི་ཕྱིར་ཞི་བའོ། །

[Block 810]
སྡུག་བསྔལ་ཐམས་ཅད་ཀྱི་བར་དག་ཉེ་བར་ཞི་བའི་ཕྱིར་གྱ་ནོམ་པའོ། །
--- END BLOCKS ---
