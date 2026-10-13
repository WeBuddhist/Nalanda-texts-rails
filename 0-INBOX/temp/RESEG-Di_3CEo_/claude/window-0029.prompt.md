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
[Block 1016]
དེ་ལས་དྲུག་སྟེ། རང་གི་ས་པ་གསུམ༌[^384]དང་། འདོད་པ་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་ཅན་དག་དང་། གཟུགས་མེད་པ་ན་སྤྱོད་པ་ཡང་ངོ་། །གཟུགས་ཀྱི་ཁམས་ཀྱི་མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་ཇི་སྐད་བཤད་པ་ལྟར། གཟུགས་མེད་པའང་དེའི་ཚུལ་ལོ། །

[Block 1017]
དེ་ན་ཡོད་པའི་ཡང་རང་གི་ས་པ་གསུམ་ཁོ་ན་ལས་འབྱུང་ལ། དེ་ལས་ཀྱང་རང་གི་ས་པ་གསུམ་པོ་དང་ས་འོག་མ་པའི་ཉོན་མོངས་པ་ཅན་རྣམས་དང་དྲུག་འབྱུང་ངོ་། །དགེ་བ་ལས་སེམས་དགུ་དག་གོ། །

[Block 1018]
གཟུགས་མེད་པ་ན་སྤྱོད་པའི་དགེ་བའི་སེམས་ལས་ནི་སེམས༌[^385]དགུ་འབྱུང་སྟེ། འདོད་པ་ན་སྤྱོད་པའི་དགེ་བ་དང་། འདོད་པ་དང་གཟུགས་ན་སྤྱོད་པའི་མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་དག་མ་གཏོགས་སོ། །

[Block 1019]
དེ་དྲུག་གོ།[^386] །

[Block 1020]
རང་གི་ས་པ་གསུམ་དང་། གཟུགས་ན་སྤྱོད་པའི་དགེ་བ་དང་། སློབ་པ་དང་མི་སློབ་པ་དག་ལས་སོ། །

[Block 1021]
བསྒྲིབས་པ་ལ་བདུན། རང་གི་ས་པ་གསུམ་དང་། གཟུགས་ན་སྤྱོད་པའི་དགེ་བ་དང་། བསྒྲིབས་པ་དང་། འདོད་པ་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་ཅན་གཉིས་སོ། །

[Block 1022]
དེ་དེ་བཞིན། དེ་ཡང་བདུན་ཁོ་ན་ལས་འབྱུང་སྟེ། འདོད་པ་དང་གཟུགས་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་ཅན་རྣམས་དང་། སློབ་པ་དང་མི་སློབ་པ་དག་མ་གཏོགས་སོ། །

[Block 1023]
སློབ་པ་བཞི་ལས།

[Block 1024]
ཁམས་གསུམ་པའི་དགེ་བ་དང་སློབ་པ་ལས་སོ། །

[Block 1025]
དེ་ལས་ལྔ། བཞི་པོ་དེ་དག་ཉིད་དང་། མི་སློབ་པའོ། །

[Block 1026]
མི་སློབ་པ་ནི་ལྔ་ལས་སོ། །

[Block 1027]
བཤད་མ་ཐག་པའི་ལྔ་པོ་དེ་ཉིད་ལས་སོ། །

[Block 1028]
དེ་ལས་སེམས་ནི་བཞི་དག་གོ། །

[Block 1029]
ཁམས་གསུམ་པའི་དགེ་བ་དག༌[^387]དང་། མི་སློབ་པའོ། །

[Block 1030]
སེམས་བཅུ་གཉིས་རྫོགས༌[^388]སོ།། །།

[Block 1031 [HEADING]]
#### སེམས་ཉི་ཤུ། ^2-4-2-0

[Block 1032]
ཡང་བཅུ་གཉིས་དེ་དག་ཉི་ཤུར་ཡང་། །བཤད་དེ།

[Block 1033 [VERSE]]
གསུམ་དུ་སྐྱེས་ནས་ཐོབ་པ་དང་། །
སྦྱོར་བྱུང་དགེ་རྣམ༌[^389]གཉིས་ཕྱེ་ནས། །

[Block 1034]
ཁམས་གསུམ་པོ༌[^390]དག་ཏུ་སྐྱེས་ནས་ཐོབ་པ་དང་། སྦྱོར་བ་ལས་བྱུང་བའི་དགེ་བའི་སེམས་རྣམ་པ་གཉིས་སུ་དབྱེའོ། །

[Block 1035 [VERSE]]
རྣམ་སྨིན་སྐྱེས་དང་སྦྱོར་ལམ༌[^391]པ། །
བཟོ་ཡི་གནས་དང་སྤྲུལ་པ་དང་། །
འདོད་ན་ལུང་བསྟན་མིན་རྣམས༌[^392]བཞི། །
གཟུགས་ན་བཟོ་མ་གཏོགས་པའོ། །

[Block 1036]
གཟུགས་ཀྱི་ཁམས་ན་བཟོའི་གནས་མ་གཏོགས་ཏེ། དེ་ན་བཟོ་མེད་པའི་ཕྱིར་རོ། །

[Block 1037]
དེ་ལྟར་བཅུ་གཉིས་པོ་དེ་དག་ཉི་ཤུར་འགྱུར་རོ། །

[Block 1038]
ཡང་སེམས་ཉི་ཤུ་པོ་འདི་དག་ལས་གང་གི་མཇུག་ཐོགས་སུ་གང་ཞིག་འབྱུང་བ་དེ་བརྗོད་དེ། འདོད་ན་སྦྱོར་བའི་སེམས་ལས་བཅུ། །མངོན་པར་ཤེས་པའི་འབྲས་བུ་མ་གཏོགས་པ་རང་གི་ས་པ་བདུན་དང་། གཟུགས་ན་སྤྱོད་པའི་སྦྱོར་བ་ལས་བྱུང་བ་དང་། སློབ་པ་དང་མི་སློབ་པའོ། །

[Block 1039]
དེ་ཡང་བརྒྱད་ཀྱི་མཇུག་ཐོགས་སུ་རང་གི་དགེ་བ་དང་། ཉོན་མོངས་པ་ཅན་དག་དང་། གཟུགས་ན་སྤྱོད་པའི་སྦྱོར་བ་ལས་བྱུང་བ༌[^393]དང་། ཉོན་མོངས་པ་ཅན་དག་དང་། སློབ་པ་དང་མི་སློབ་པ་དག་ལས་སོ། །

[Block 1040]
སྐྱེས་ནས་ཐོབ་པའི་མཇུག་ཐོགས་སུ་དགུ། མངོན་པར་ཤེས་པའི་འབྲས་བུ་མ་གཏོགས་པ་རང་གི་ས་པ་བདུན་དང་། གཟུགས་དང་གཟུགས་མེད་པ་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་ཅན་དག་གོ། །

[Block 1041]
དེ་ཡང་བཅུ་གཅིག་མཇུག་ཐོགས་སུ། །བཅུ་གཅིག་གི་མཇུག་ཐོགས་སུ་འབྱུང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1042]
སྔ་མ་བཞིན་དུ་རང་གི་ས་པ་བདུན་དང་། གཟུགས་ན་སྤྱོད་པའི་སྦྱོར་བ་ལས་བྱུང་བ་དང་། །ཉོན་མོངས་པ་ཅན་དག་དང་། སློབ་པ་དང་མི་སློབ་པ་དག་ལས་སོ། །

[Block 1043 [VERSE]]
ཉོན་མོངས༌[^394]ཅན་སེམས་གཉིས་ལས་བདུན། །
སྔ་བཞིན༌[^395]རང་གི་དག་ཁོ་ནའོ། །
དེ་དག་བཅུ་བཞིའི་སེམས་མཇུག་ཐོགས། །

[Block 1044]
རང་གི་ས་པ་བདུན་དང་། སྦྱོར་བ་ལས་བྱུང་བ་དང་། མངོན་པར་ཤེས་པའི་འབྲས་བུ་མ་གཏོགས་པ་གཟུགས་ན་སྤྱོད་པ་བཞི་དང་། སྦྱོར་བ་ལས་བྱུང་བ་མ་གཏོགས་པ་གཟུགས་མེད་པ་ན་སྤྱོད་པ་གསུམ་ལས་སོ། །

[Block 1045]
སྤྱོད་ལམ་རྣམ་སྨིན་སྐྱེས་ཕྱིས༌[^396]བརྒྱད། །སྦྱོར་བ་ལས་བྱུང་བ་དང་། མངོན་པར་ཤེས་པའི་འབྲས་བུ་དག་མ་གཏོགས་པ་རང་གི་ས་པ༌[^397]དྲུག་དང་། གཟུགས་དང་གཟུགས་མེད་པ་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་ཅན་དག་གོ། །

[Block 1046]
དེ་དག་བདུན་པོ་ཉིད་ལས་སོ། །

[Block 1047]
སྔར་བཞིན་དུ་རང་གི་ས་པ༌[^398]བདུན་ཁོ་ན་ལས་སོ། །

[Block 1048]
བཟོའི་གནས་ལས་དྲུག །སྦྱོར་བ་ལས་བྱུང་བ་དང་། མངོན་པར་ཤེས་པའི་འབྲས་བུ་དག་མ་གཏོགས་པ་རང་གི་རྣམས་ཁོ་ནའོ། །

[Block 1049]
དེ་ཡང་།

[Block 1050]
བདུན་ལས།

[Block 1051]
མངོན་པར་ཤེས་པའི་འབྲས་བུ་མ་གཏོགས་པ་རང་གི་དག་ཁོ་ན་ལས་སོ། །

[Block 1052]
སྤྲུལ་སེམས་ཕྱི་ནས་གཉིས། མངོན་པར་ཤེས་པའི་འབྲས་བུ་རང་ཉིད་དང་། གཟུགས་ན་སྤྱོད་པའི་སྦྱོར་བ་ལས་བྱུང་བའོ། །

[Block 1053]
དེ་ཡང་གཉིས་ལས་བྱུང་། དེ་ཁོ་ན་ལས་སོ། །

[Block 1054]
འདོད་པ་ལས༌[^399]སྐྱེས་པ། བརྒྱད་པོ་དག་གོ། །

[Block 1055]
གཟུགས་གཏོགས་བརྗོད། སྦྱོར་བ་ལས་བྱུང་ལས༌[^400]བཅུ་གཉིས། །འདོད་པ་ན་སྤྱོད་པའི་དགེ་བ་དག་དང་། མངོན་པར་ཤེས་པའི་འབྲས་བུ་དང་། རང་གི་དྲུག་དང་། གཟུགས་མེད་པའི་སྦྱོར་བ་ལས་བྱུང་བ་དང་། སློབ་པ་དང་། མི་སློབ་པའོ། །
--- END BLOCKS ---
