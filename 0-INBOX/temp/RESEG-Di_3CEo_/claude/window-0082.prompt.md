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
[Block 2871 [VERSE]]
ཉོན་མོངས་ཕྲ་རྒྱས་བཅས་རྣམས༌[^1148]གཉིས། །
ཉོན་མོངས་ཅན་མིན་རྒྱས་འགྱུར་གྱིས། །

[Block 2872]
སེམས་ཉོན་མོངས་པ་ཅན་ནི་དེ་དང་མཚུངས་པར་ལྡན་པ་དང་། དེ་ལ་དམིགས་པ་མ་སྤངས་པའི་ཕྲ་རྒྱས་རྒྱས་པར་འགྱུར་བ་རྣམས་དང་།དེ་དང༌[^1149]མཚུངས་པར་ལྡན་པ་སྤངས་པ་རྒྱས་པར་མི་འགྱུར་བ་རྣམས་ཀྱི་ཕྲ་རྒྱས་དང་བཅས་པ་ཡིན་ཏེ། དེ་དང་ལྷན་ཅིག་པའི་ཕྱིར་རོ། །

[Block 2873]
སེམས་ཉོན་མོངས་པ༌[^1150]ཅན་མ་ཡིན་པ་ནི་དེ་ལ་དམིགས་པ་མ་སྤངས་པ་རྒྱས་པར་འགྱུར་བ་དག་ཁོ་ནས་ཕྲ་རྒྱས་དང་བཅས་པ་ཡིན་ནོ། །

[Block 2874 [HEADING]]
### ཕྲ་རྒྱས་བཅུ་པོའི་འཇུག་པའི་རིམ་པ། ^5-11-0

[Block 2875]
ཕྲ་རྒྱས་བཅུ་པོའི་འཇུག་པའི་རིམ་པ་བསྟན་པར་བྱ་སྟེ། རེ་ཞིག་དང་པོ་ཁོ་ནར་མ་རིག་པ་དང་ལྡན་པ་ལས་བདེན་པ་རྣམས་ལ་ཀུན་དུ་རྨོངས་པར་འགྱུར་ཏེ། དེའི་ཕྱིར། རྨོངས་ལ་ཐེ་ཚོམ། རྨོངས་པར་གྱུར་པ་ཕྱོགས་གཉིས་ཐོས་ནས་ཐེ་ཚོམ་སྐྱེ་བར་འགྱུར་རོ། །

[Block 2876]
དེ་ནས་ནི། ལོག་ལྟ། རབ་ཏུ་འཇུག་སྟེ། སྡུག་བསྔལ་མེད་དོ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 2877]
དེ་ནས་འཇིག་ཚོགས་ལྟ། སྡུག་བསྔལ་ལས་ཕུང་པོ་བསལ་ནས་བདག་ཏུ་མངོན་པར་ཞེན་པའི་ཕྱིར་རོ། །

[Block 2878]
དེ་ནས་མཐར་འཛིན། བདག་རྟག་པ་དང་ཆད་པའི་མཐར་འཛིན་པའི་ཕྱིར་རོ། །

[Block 2879]
དེ་ནས་ནི། ཚུལ་ཁྲིམས་མཆོག་འཛིན། གང་ཁོ་ན་ལ་མཐར་འཛིན་པ་དེས་དག་པར་ཡིད་ཆེས་པའི་ཕྱིར་རོ། །

[Block 2880]
དེ་ནས་ལྟ། མཆོག་ཏུ་འཛིན་ཞེས་སྦྱར་ཏེ། གང་གིས་དག་པར་ཡིད་ཆེས་པ་དེ་ལ་མཆོག་ཏུ་འཛིན་པའི་ཕྱིར་རོ། །

[Block 2881]
དེས་ནི།

[Block 2882 [VERSE]]
རང་གི་ལྟ་ལ་ང་རྒྱལ་ཆགས། །
དེ་ལ་ཆགས་པའི་ཕྱིར་དང་།
དེས་ཁེངས་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2883]
གཞན་ལ་ཞེ་སྡང་། རང་གི་ལྟ་བ་ལ་ལྷག་པར་ཞེན་པར་གྱུར་པས་དེའི་དགྲ་བོར་གྱུར༌[^1151]པ་གཞན་གྱི་ལྟ་བ་ལ་ཞེ་སྡང་འཇུག་གོ། །

[Block 2884]
གཞན་དག་ནི་རང་གི་ལྟ་ལ༌[^1152]བླངས་ནས་བོར་བ་གཞན་ལ་ཞེ་སྡང་བར་འདོད་དོ། །

[Block 2885]
དེ་ལྟར་རིམ། དེ་དག་གི་འཇུག་པའི་རིམ་པ་ནི་དེ་ཡིན་ནོ། །

[Block 2886 [HEADING]]
### ཉོན་མོངས་སྐྱེ་བའི་རྒྱུ་གསུམ། ^5-12-0

[Block 2887]
ཉོན་མོངས་སྐྱེ་ན་རྒྱུ་གསུམ་གྱིས་སྐྱེ་སྟེ།

[Block 2888 [VERSE]]
ཕྲ་རྒྱས་སྤངས་པ་མ་ཡིན་དང་། །
ཡུལ་ནི་ཉེ་བར་གནས་པ་དང་། །
ཚུལ་བཞིན་མ་ཡིན་ཡིད་བྱེད་ལས། །

[Block 2889]
རྒྱུ་དང་། ཡུལ་དང་། སྦྱོར་བའི་སྟོབས་ཀྱིས། ཉོན་མོངས། སྐྱེ་སྟེ་གང་། རྒྱུ་ནི་ཚང་བ་ཡིན། རེས་འགའ་ནི་ཡུལ་གྱི་སྟོབས་ཁོ་ནས་སྐྱེ་སྟེ། དཔེར་ན་དགྲ་བཅོམ་པ་ཡོངས་སུ་ཉམས་པའི་ཆོས་ཅན་གྱི་ལྟ་བུའོ། །

[Block 2890 [HEADING]]
### ཟག་པ་དང་། ཆུ་བོ་དང་། སྦྱོར་བ་དང་། ཉེ་བར་ལེན་པ། ^5-13-0

[Block 2891]
ཡང་ཕྲ་རྒྱས་དེ་དག་ཉིད་ཟག་པ་དང་། ཆུ་བོ་དང་། སྦྱོར་བ་དང་། ཉེ་བར་ལེན་པའི་དབྱེ་བས་གསུངས་སོ། །

[Block 2892 [HEADING]]
#### ཟག་པ། ^5-13-1-0

[Block 2893]
དེ་ལ་རེ་ཞིག །

[Block 2894 [VERSE]]
འདོད་ན་གཏི་མུག་མ་གཏོགས་པའི། །
ཉོན་མོངས་ཀུན་ནས༌[^1153]དཀྲིས་བཅས་ཟག །

[Block 2895]
མ་རིག་པ་མ་གཏོགས་པ་འདོད་པ་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་རྣམས་ཀུན་ནས་དཀྲིས་པ་དང་བཅས་པ་འདོད་པའི་ཟག་པ་ཡིན་ནོ། །

[Block 2896 [VERSE]]
གཟུགས་དང་གཟུགས་ནི་མེད་པ་ན། །
ཕྲ་རྒྱས་ཁོ་ན་སྲིད་པའི་ཟག །

[Block 2897]
མ་རིག་པ་མ་གཏོགས་པ་གཟུགས་དང་གཟུགས་མེད་པ་ན་སྤྱོད་པའི་ཟག་པ་རྣམས་ནི་སྲིད་པའི༌[^1154]ཟག་པ་ཡིན་ནོ། །ཅིའི་ཕྱིར་གཅིག་ཏུ་བྱས་ཤེ་ན།

[Block 2898 [VERSE]]
དེ་ལུང་མ་བསྟན་ཁ་ནང་བལྟས། །
མཉམ་གཞག་ས་པའི་ཕྱིར་གཅིག་བྱས། །

[Block 2899]
འདི་དག་རྒྱུ་གསུམ་གྱི་ཕྱིར་གཅིག་ཏུ་བྱས་སོ། །

[Block 2900]
ཁམས་གསུམ་གྱི་མ་རིག་པ་ནི་མ་རིག་པའི་ཟག་པ་ཞེས་བྱ་བར་གྲུབ་པོ། །ཟག་པ་དེ་དག་གི་ཡང་།

[Block 2901 [VERSE]]
རྩ་བ་མ་རིག་ཡིན་པས་ན། །
ལོགས་ཤིག་ཏུ་ནི་ཟག་པར་བསྟན། །

[Block 2902]
ཟག་པ་དེ་དག་ཇི་སྐད་དུ་བཤད་པ་ལྟར།

[Block 2903 [HEADING]]
#### ཆུ་བོ་དང་སྦྱོར་བ། ^5-13-2-0

[Block 2904 [VERSE]]
ཆུ་བོ་སྦྱོར་བའང་དེ་བཞིན་དུ། །
ལྷ་རྣམས་གསལ་ཕྱིར་ལོགས་ཤིག་བསྟན། །

[Block 2905]
འདོད་པའི་ཟག་པ་ཉིད་དུ་འདོད་པའི་ཆུ་བོ་དང་། འདོད་པའི་སྦྱོར་བའོ། །

[Block 2906]
དེ་བཞིན་དུ་སྲིད་པའི་ཟག་པ་ནི་སྲིད་པའི་ཆུ་བོ་དང་། སྲིད་པའི་སྦྱོར་བ་ཡིན་ནོ། །

[Block 2907]
ལྟ་བ་རྣམས་ནི་མ་གཏོགས་ཏེ། དེ་དག་ནི་ཆུ་བོ་དང་། སྦྱོར་བ་རྣམས་ལས་ལོགས་ཤིག་ཏུ་བཞག་སྟེ། གསལ་བའི་ཕྱིར་རོ། །

[Block 2908 [VERSE]]
ཟག་པར་མ་ཡིན་གྲོགས་མིང༌[^1155]རྣམས། །
འཇོག་པའི་རྗེས་སུ་མི་མཐུན་ལོ། །

[Block 2909]
ཟག་པ་རྣམས་ཀྱི་ངེས་པའི་ཚིག་ནི་འཇོག་པར་བྱེད་པས་ན་ཞེས་འོག་ནས་འཆད་ན། ལྟ་བ་འབའ་ཞིག་ནི་གསལ་བའི་ཕྱིར་འཇོག་པའི་རྗེས་སུ་མཐུན་པ་མ་ཡིན་པས་བསྲེས་ནས་གཞག་གོ། །

[Block 2910 [HEADING]]
#### ཉེ་བར་ལེན་པ། ^5-13-3-0
--- END BLOCKS ---
