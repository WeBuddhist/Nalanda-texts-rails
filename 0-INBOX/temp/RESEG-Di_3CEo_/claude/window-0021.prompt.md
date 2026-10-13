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
[Block 736]
གང་ཟག་ལ་དམིགས་པའི་དགའ་བ་དང་གུས་པ་དག་མེད་དོ། །

[Block 737]
རྣམ་པར་རྟོག་པ་དང་། དཔྱོད་པ་དག་ལ་ཐ་དད་དུ་བྱ་བ་ཅི་ཡོད་ཅེ་ན།

[Block 738 [VERSE]]
རྟོག་དང་དཔྱོད་པ་རྩིང་ཞིབ་ཉིད། །
སེམས་ཀྱིའོ་ཞེས་འོག་ནས་འཆད་དེ།
རྟོག་པ་ནི་སེམས་རྩིང་བའོ། །
དཔྱོད་པ་ནི་སེམས་ཞིབ་པའོ། །

[Block 739]
ང་རྒྱལ་དང་རྒྱགས་པ་དག་ལ་ཐ་དད་དུ་བྱ་བ་ཅི་ཞིག་ཡོད་ཅེ་ན།

[Block 740 [VERSE]]
ང་རྒྱལ་ཁེངས་པ་རྒྱགས་པ་ནི། །
རང་གི་ཆོས་ལ་ཆགས་པ་ཡི། །
སེམས་ནི་ཡོངས་སུ་གཏུགས་པའོ། །

[Block 741]
ཕ་རོལ་པོ་ལས་གང་ཡང་རུང་བའི་ཁྱད་པར་ཞིག་ཡོངས་སུ་བཏགས་ནས་སེམས་ཁེངས་པ་ནི་ང་རྒྱལ་ལོ། །

[Block 742]
རྒྱགས་པ་ནི་རང་གི་ཆོས་ཁོ་ན་ལ་ཆགས་པའི་སེམས་ཡོངས་སུ་གཏུགས་པ་གང་ཡིན་པའོ། །

[Block 743]
སེམས་ལས་བྱུང་བ་རྣམས་སེམས༌[^285]དང་བཅས་ཏེ་བཤད་ཟིན་ཏོ། །

[Block 744 [HEADING]]
##### སེམས་དང་སེམས་བྱུང་གི་མིང་། ^2-2-2-4-0

[Block 745]
གསུང་རབ་ལས་འདི་དག་གི༌[^286]ཐ་སྙད་དུ་འདོགས་པའི་ཕྱིར་དེ་དག་གི་མིང་འདི་དག་བརྗོད་དེ།

[Block 746 [VERSE]]
སེམས་དང་ཡིད་དང་རྣམ་ཤེས་ནི། །
དོན་གཅིག་འབྱེད་པས་ན་སེམས་སོ། །

[Block 747]
གོ་བས་ན་ཡིད་དོ། །

[Block 748]
རྣམ་པར་ཤེས་པས་ན་རྣམ་པར་ཤེས་པའོ། །

[Block 749]
སེམས་དང་སེམས་བྱུང་དང་།

[Block 750 [VERSE]]
རྟེན་དང་དམིགས་དང་རྣམ་བཅས་དང་། །
མཚུངས་པར་ལྡན་པའང་དོན་གཅིག་སྟེ། །

[Block 751]
སེམས་དང་སེམས་ལས་བྱུང་བ་དེ་དག་ཉིད་དབང་པོ་ལ་བརྟེན་པའི༌[^287]ཕྱིར་རྟེན་དང་བཅས་པ་དག་ཅེས་བྱའོ། །

[Block 752]
ཡུལ་ལ་འཛིན་པའི་ཕྱིར་དམིགས་པ་དང་བཅས་པ་དག་གོ། །

[Block 753]
དམིགས་པ་དེ་ཉིད་ལ་སེམས་རྣམ་པ་རེ་རེ་ནས་བྱེ་བྲག་ཏུ་གཅོད་པའི་ཕྱིར་རྣམ་པ་དང་བཅས་པ་དག་གོ། །

[Block 754]
མཉམ་པར་ལྡན་པའི་ཕྱིར་མཚུངས་པར་ལྡན་པ་དག་གོ། །

[Block 755]
རྣམ་པ་གང་དག་གིས་མཚུངས་པར་ལྡན་ཞེ་ན། གསུངས་པ། རྣམ་པ་ལྔ། མཚུངས་པ་རྣམ་པ་ལྔ་པོ་རྟེན༌[^288]དང་། དམིགས་པ་དང་། རྣམ་པ་དང་། དུས་དང་། རྫས་མཚུངས་པ་དག་གིས་མཚུངས་པར་ལྡན་ནོ། །

[Block 756]
རྫས་མཚུངས་པ་ཡང་ཇི་ལྟར་སེམས་གཅིག་ཁོ་ན་ཡིན་པ་དེ་ཁོ་ན་བཞིན་དུ་སེམས་ལས་བྱུང་བ་རྣམས་ཀྱང་རེ་རེ་ཡིན་པའོ། །

[Block 757]
སེམས་དང་སེམས་ལས་བྱུང་བ་དག་བཤད་ཟིན་ཏོ། །

[Block 758 [HEADING]]
#### ལྡན་པ་མ་ཡིན་པའི་འདུ་བྱེད། ^2-2-3-0

[Block 759 [VERSE]]
མི་ལྡན་པ་ཡི་འདུ་བྱེད་རྣམས། །
ཐོབ་དང་མ་ཐོབ་སྐལ་མཉམ་དང་། །
འདུ་ཤེས་མེད་སྙོམས་འཇུག་དག་དང་། །
སྲོག་དང་མཚན་ཉིད་རྣམས་དང་ནི། །
མིང་གི་ཚོགས་ལ་སོགས་པ་ཡང་། །

[Block 760]
འདུ་བྱེད་འདི་དག་ནི་སེམས་དང་མཚུངས་པར་ལྡན་པ་ཡང་མ་ཡིན་ལ། གཟུགས་ཀྱི་རང་བཞིན་ཡང་མ་ཡིན་པས་སེམས་དང་ལྡན་པ་མ་ཡིན་པ་དག་ཅེས་བྱའོ། །

[Block 761 [HEADING]]
##### ཐོབ་པ་དང་མ་ཐོབ་པ། ^2-2-3-1-0

[Block 762]
དེ་ལ་རེ་ཞིག །ཐོབ་པ་རྙེད་དང་ལྡན་པའོ། །

[Block 763]
ཐོབ་པ་ནི་རྣམ་པ་གཉིས་ཏེ། མ་ཐོབ་པ་དང་། རྣམ་པར་ཉམས་པ་ལས༌[^289]རྙེད་པ་དང་། ཐོབ་ནས་ལྡན་པའོ། །

[Block 764]
བཟློག་པ་ནི་མ་ཐོབ་པའོ་ཞེས་བྱ་བར་གྲུབ་པོ། །འདི་དག་ཀྱང་གང་གི་ཡིན་ཞེ་ན། ཐོབ་དང་མ་ཐོབ་རང་རྒྱུད་དུ། །གཏོགས་པ་རྣམས་ཀྱིའོ། །

[Block 765]
གཞན་གྱི་རྒྱུད་དུ༌[^290]གཏོགས་པ་རྣམས་ཀྱི་ནི༌[^291]མ་ཡིན་ཏེ། གཞན་དག་དང་ནི་འགའ་ཡང་ལྡན་པ་མེད་དོ། །

[Block 766]
རྒྱུད་དུ་མ་གཏོགས་པ་རྣམས་ཀྱི་ནི་ཡང་མ་ཡིན་ཏེ། སེམས་ཅན་དུ་མི་བགྲང་བ་དག་ནི་འགའ་ཡང་ལྡན་པ་མེད་དོ། །

[Block 767]
སླར་ཡང་ཐོབ་པ་དང་མ་ཐོབ་པ་དག་ནི། འགོག༌[^292]གཉིས་ཀྱི། སོ་སོར་བརྟགས་པ་མ་ཡིན་པས་འགོག་པ་ནི་སེམས་ཅན་ཐམས་ཅད་དང་ལྡན་ནོ། །

[Block 768]
སོ་སོར་བརྟགས་པ་དང་ནི་འགའ་ཞིག་གོ། །

[Block 769]
ཐོབ་པ་དེ་ཡང་ནི། དུས་གསུམ་པ་ཡི་རྣམ་པ་གསུམ། །ཆོས་འདས་པ་རྣམས་ཀྱི་ཐོབ་པ་འདས་པ་ཡང༌[^293]ཡོད། མ་འོངས་པ་དང་། ད་ལྟར་བྱུང་བ་ཡང་ཡོད་ལ། དེ་བཞིན་དུ་མ་འོངས་པ་དང་། ད་ལྟར་བྱུང་བ་རྣམས་ཀྱི་ཡང་སོ་སོར་རྣམ་པ་གསུམ་མོ། །

[Block 770]
དགེ་ལ་སོགས་ཀྱི་དགེ་ལ་སོགས། །དགེ་བ་དང་མི་དགེ་བ་དང་། ལུང་དུ་མ་བསྟན་པ་རྣམས་ཀྱི་ཐོབ་པ་ནི་རིམ་པ་བཞིན་དུ་དགེ་བ་དང་། མི་དགེ་བ་དང་། ལུང་དུ་མ་བསྟན་པ་དེ༌[^294]ཁོ་ན་ཡིན་ནོ། །

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
--- END BLOCKS ---
