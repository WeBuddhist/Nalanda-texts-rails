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
དེར་གཏོགས་རྣམས་ཀྱི་རང་ཁམས་པ། །འདོད་པ་དང་། གཟུགས་དང་། གཟུགས་མེད་པ་ན་སྤྱོད་པ༌[^295]རྣམས་ཀྱི་ཐོབ་པ་ནི་རང་གི་ཁམས་པ་ཁོ་ནའོ། །

[Block 772]
མ་གཏོགས་རྣམས་ཀྱི་རྣམ་པ་བཞི། །ཟག་པ་མེད་པ་རྣམས་ཀྱི་ཐོབ་པ་ནི་རྣམ་པ་བཞི་སྟེ། སོ་སོར་བརྟགས་པས་འགོག་པའི་ནི་གཟུགས་དང་། གཟུགས་མེད་པ་ན་སྤྱོད་པའང༌[^296]ཡིན་ལ། ཟག་པ་མེད་པའང་ཡིན་ཏེ། ལམ་གྱི་དབང་གིས་སོ། །

[Block 773]
ལམ་གྱི་བདེན་པའི་ནི་ཟག་པ་མེད་པ་ཉིད་དོ། །

[Block 774]
སོ་སོར་བརྟགས་པ་མ་ཡིན་པས་འགོག་པའི་ནི་ཁམས་གསུམ་པ་མ༌[^297]ཡིན་ཏེ་སྐྱེ་བའི་དབང་གིས་སོ། །

[Block 775]
དེ་ནི་བསྡུས་ནས༌[^298]རྣམ་པ་བཞིར་འགྱུར་རོ། །

[Block 776]
སློབ་པ་རྣམས་ཀྱི་ཐོབ་པ་ནི་ཐོབ་པའི་སློབ་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 777]
མི་སློབ་པ་རྣམས་ཀྱི་ཐོབ་པ་ནི་མི་སློབ་པ་ཉིད་དོ། །

[Block 778]
སློབ་དང་མི་སློབ་མིན་གྱི་གསུམ། །དེ་དག་ཀྱང་ཟག་པ་དང་བཅས་པ་དང་འདུས་མ་བྱས་པའོ། །

[Block 779]
དེ་ལ་ཟག་པ་དང་བཅས་པ་རྣམས་ཀྱི་དང་སོ་སོར་བརྟགས་པ་མ་ཡིན་པས་འགོག་པའི་དང་། འཕགས་པ་མ་ཡིན་པས་ཐོབ་པ་སོ་སོར་བརྟགས་པས་འགོག་པའི་ཐོབ་པ་ནི་སློབ་པ་ཡང་མ་ཡིན་མི་སློབ་པ་ཡང་མ་ཡིན་ནོ། །

[Block 780]
དེ་ཉིད་ཀྱི་སློབ་པས་ཐོབ་པ་ནི་སློབ་པའོ། །

[Block 781]
མི་སློབ་པས་ཐོབ་པ་ནི་མི་སློབ་པའོ། །

[Block 782]
མཐོང་བ་དང་བསྒོམ་པས་སྤང་བར་བྱ་བ་རྣམས་ཀྱི་ཐོབ་པ་ནི་དེའི་རིགས་དག་ཁོ་ནས་སོ། །

[Block 783]
སྤང་བྱ་མིན་པའི་རྣམ་གཉིས་འདོད། །ཟག་པ་མེད་པ་རྣམས་ལ་སོ་སོར་བརྟགས་པ་མ་ཡིན་པའི་འགོག་པ་དང་། འཕགས་པ་མ་ཡིན་པས་ཐོབ་པ་སོ་སོར་བརྟགས་པས་འགོག་པའི་ཐོབ་པ་ནི་བསྒོམ་པས་སྤང་བར་བྱ་བའོ། །

[Block 784]
དེ་ཉིད་འཕགས་པའི་ལམ་གྱིས་ཐོབ་པ་དང་། ལམ་གྱི་བདེན་པའི་ནི་ཟག་པ་མེད་པ་སྟེ།

[Block 785 [VERSE]]
སྤང་བར་བྱ་བ་མ་ཡིན་པའོ། །
དུས་གསུམ་པ་ཡི་རྣམ་པ་གསུམ། །

[Block 786]
ཞེས་སྤྱིར་བསྟན་པ་གང་ཡིན་པ་དེའི་དམིགས་ཀྱིས་གསལ་བ༌[^299]ནི་འདི་ཡིན་ཏེ། ལུང་བསྟན་མིན་ཐོབ་ལྷན་ཅིག་སྐྱེས། །མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་རྣམས་ཀྱི་ཐོབ་པ་ནི་ལྷན་ཅིག་སྐྱེས་པ་ཁོ་ནའོ། །

[Block 787]
མངོན་ཤེས་སྤྲུལ་པ་མ་གཏོགས་པ། །མངོན་པར་ཤེས་པ་དང་ལུང་དུ་མ་བསྟན་པ་གཉིས་དང་སྤྲུལ་པའི་སེམས་མ་གཏོགས་པའོ། །

[Block 788]
དེ་དག་ནི་སྦྱོར་བའི་ཁྱད་པར་གྱིས་འགྲུབ་པས་སྟོབས་དང་ལྡན་པའི་ཕྱིར་སྔར་དང་ཕྱིས་དང་ལྷན་ཅིག་སྐྱེས་པ་ཡང་ཡོད་དོ། །

[Block 789]
ཅི་མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་ཁོ་ནའི་ཐོབ་པ་དང་ལྷན་ཅིག་སྐྱེས་པ་ཡིན་ནམ་ཞེ་ན། སྨྲས་པ་བསྒྲིབས་པའི་གཟུགས་ཀྱི་ཐོབ་པ་ནི་ལྷན་ཅིག་སྐྱེས་པ་ཁོ་ནའོ། །

[Block 790]
ཆེན་པོས་ཀྱང་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་མི་སློང་བས༌[^300]སྟོབས་ཆུང་བར་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 791]
དུས་གསུམ་པ་ཡི་རྣམ་པ་གསུམ། །ཞེས་བྱ་བའི་དམིགས་བསལ་ནི། འདོད་པ་ན། གཟུགས་ཀྱི་སྔར་ནི་སྐྱེ་བ་མེད། །ལྷན་ཅིག་སྐྱེ་བ་དང་། དུས་ཕྱིས་སྐྱེ་བ་ནི་ཡོད་དོ། །

[Block 792]
ཐོབ་པའི་རྣམ་པའི་བྱེ་བྲག་ནི་བཤད་ཟིན་ཏོ། །

[Block 793]
མ་ཐོབ་མ་བསྒྲིབས་ལུང་མ་བསྟན། །མ་ཐོབ་པ་ཐམས་ཅད་ནི་མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 794]
འདས་མ་སྐྱེས་ཀྱི་དེ་རྣམ་གསུམ། །ད་ལྟར་བྱུང་བ་མ་ཐོབ་པ་ནི་མེད་དེ། འདས་པ་དང་། མ་འོངས་པ་དག་ནི་དུས་གསུམ་པ་ཡིན་ནོ། །

[Block 795]
འདོད་སོགས་གཏོགས་དང་དྲི་མེད་ཀྱིའང་། །རྣམ་པ་གསུམ་ཞེས་བྱ་བར་སྦྱར་ཏེ། འདོད་པར་གཏོགས་པ་རྣམས་ཀྱི༌[^301]ནི་འདོད་པ་དང་། གཟུགས་དང་གཟུགས་མེད་པ་ན་སྤྱོད་པའི་ཡིན་ཏེ། རིགས་པའི་དབང་གིས་སོ། །

[Block 796]
གཟུགས་དང་། གཟུགས་མེད་པར་གཏོགས་པ་རྣམས་དང་། ཟག་པ་རྣམས་ཀྱི་ཡང་དེ་དང་འདྲའོ། །

[Block 797]
མ་ཐོབ་པ་ཟག་པ་མེད་པ་ནི་མེད་དེ། འདི་ལྟར། ལམ་མ་ཐོབ་པ་སོ་སོ་ཡི། །སྐྱེ་བོར་འདོད་དོ། །

[Block 798]
གང་གི་ཕྱིར་སོ་སོའི་སྐྱེ་བོ་ཉིད་ནི་ཟག་པ་མེད་པ་ཡིན་པར་མི་འོས་སོ། །

[Block 799]
ཡང་མ་ཐོབ་པ་ནི་ཇི་ལྟར་ཉམས་ཤེ་ན། ཆོས་གང་གི་མ་ཐོབ་པ་གང་ཡིན་པ་དེ་ནི། དེ་ཐོབ་པ་དང་། ས་འཕོས་ནས་ནི་རྣམ་ཉམས་འགྱུར། །རེ་ཞིག་འདི་ལྟ་སྟེ། འཕགས་པའི་ལམ་གྱི་མ་རྙེད་པ་ནི་སོ་སོའི་སྐྱེ་བོ་ཉིད་དེ། དེ་ནི་རྙེད་པ་དང་། ས་འཕོས་པ་ལས་རྣམ་པར་ཉམས་པར་འགྱུར་ཏེ། གཞན་དག་གི་ཡང་དེ་བཞིན་དུ་སྦྱར་བར་བྱའོ། །

[Block 800 [HEADING]]
##### སྐལ་བ་མཉམ་པ། ^2-2-3-2-0

[Block 801]
ཡང་སྐལ་བ་མཉམ་པ་འདི་ཅི་ཞེ་ན། སྐལ་མཉམ་སེམས་ཅན་འདྲ་བའོ། །

[Block 802]
སྐལ་བ་མཉམ་པ་ཉིད་ནི་སེམས་ཅན་རྣམས་ཀྱི་འདྲ་བ་ཡིན་ཏེ། དེ་ཡང་ཐ་དད་པ་མ་ཡིན་པ་དང་། ཐ་དད་པ་སྟེ། དེ་དག་ཁོ་ནའི་ས་དང་། ཁམས་དང་། འགྲོ་བ་དང་། སྐྱེ་གནས་ལ་སོགས་པའི་དབྱེ་བས་སོ། །

[Block 803 [HEADING]]
##### འདུ་ཤེས་མེད་པ་པ། ^2-2-3-3-0

[Block 804]
ཡང་འདུ་ཤེས་མེད་པ་པ་ཞེས་བྱ་བ་འདི་ཅི་ཞེ་ན།

[Block 805 [VERSE]]
འདུ་ཤེས་མེད་པ་པ་འདུ་ཤེས། །
མེད་པར་སེམས་དང་སེམས་བྱུང་རྣམས། །

[Block 806]
འགོག་པའོ། །

[Block 807]
གང་གིས་མ་འོངས་པའི་སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་འགོག་པ་དེ་ནི་འདུ་ཤེས་མེད་པ་པ་ཞེས་བྱ་བའི་རྫས་སོ། །

[Block 808]
དེ་ཡང་གཅིག་ཏུ་རྣམ༌[^302]སྨིན། འདུ་ཤེས་མེད་པའི་སྙོམས་པར་འཇུག་པའིའོ། །

[Block 809]
གང་དག་ན་འདུ་ཤེས་མེད་པའི་སེམས་ཅན་རྣམས་འཁོད་པའི་སེམས་ཅན་དེ་དག་གང་ཞེ་ན། དེ་འབྲས་ཆེ། ལྷ་དེ་དག་ནི་འབྲས་བུ་ཆེ་བ་ཞེས་བྱ་བ་ཡིན་ཏེ། དེ་དག་གི་ཕྱོགས་གཅིག་ནི་འདུ་ཤེས་མེད་པ་པ་ཡིན་ཏེ། བསམ་གཏན་ཁྱད་པར་ཅན་བཞིན་ནོ། །

[Block 810]
འདུ་ཤེས་མེད་པ་པ་བཤད་ཟིན་ཏོ། །
--- END BLOCKS ---
