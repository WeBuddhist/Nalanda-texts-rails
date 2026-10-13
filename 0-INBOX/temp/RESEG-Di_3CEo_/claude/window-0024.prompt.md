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
[Block 841]
བཟློག་པ་ནི་འདུས་མ་བྱས་པའོ། །

[Block 842]
སྐྱེ་བ་ལ་སོགས་པ་དེ་དག་ཀྱང༌[^321]འདུས་བྱས་ཡིན་པའི་ཕྱིར་སྐྱེ་བ་ལ་སོགས་པ་གཞན་ཡོད་པར་འགྱུར་རོ་ཞེ་ན། ཡོད་པ་དེ༌[^322]ཁོ་ན་སྟེ། དེ་དག་སྐྱེ་བའི་སྐྱེ༌[^323]ལ་སོགས། །དེ་དག་ལ་ཡང་སྐྱེ་བའི་སྐྱེ་བ་དང་། རྒ་བའི་རྒ་བ་དང་། གནས་པའི་གནས་པ་དང་། མི་རྟག་པ་ཉིད་ཀྱི་མི་རྟག་པ་ཉིད་དོ་ཞེས་བྱ་བ་རྗེས་སུ་མཐུན་པའི་མཚན་ཉིད་བཞི་ཡོད་དོ། །

[Block 843]
རེ་རེ་ལ་ཡང་མཚན་ཉིད་བཞི་པ་དང་། མཐར་ཐུག་པ་མེད་པར་འགྱུར་རོ་ཞེ་ན། མི་འགྱུར་ཏེ། འདི་ལྟར། དེ་ཆོས་བརྒྱད་དང་གཅིག་ལ་འཇུག །ཆོས་བདག་ཉིད་གཏོགས་པར་མཚན་ཉིད་དང་རྗེས་སུ་མཐུན་པའི་མཚན་ཉིད་བརྒྱད་དང་ལྷན་ཅིག་ཏུ་དགུ་སྐྱེ་ལ། དེ་ལ་སྐྱེ་བས་ནི་བདག་ཉིད་མ་གཏོགས་པ་ཆོས་གཞན་བརྒྱད་སྐྱེད་པར་བྱེད་དོ། །

[Block 844]
སྐྱེ་བའི་སྐྱེ་བས་ནི་དེ་ཁོ་ན་སྐྱེད་པར་བྱེད་དོ། །

[Block 845]
དེ་བཞིན་དུ་གནས་པ་ལ་སོགས་པས་གནས་པ་དང་། སྐྱེད་པ་དང་ཉམས་པར་བྱེད་པ་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 846]
གལ་ཏེ་མ་འོངས་པའི་སྐྱེ་བ༌[^324]བསྐྱེད་པར་བྱ་བ་སྐྱེད་པ་ཡིན་ན།[^325] མ་འོངས་པ་ཐམས་ཅད་ཅིག་ཅར་ཅིའི་ཕྱིར་མི་སྐྱེད་ཅེ་ན། འདི་ལྟར་རྒྱུ་དང་རྐྱེན་དག་མེད་པར་ནི། སྐྱེ་བ་བསྐྱེད་བྱ་སྐྱེད་བྱེད་མིན། །རྒྱུ་དང་རྐྱེན་ཚོགས་པ་མེད་པར་ནི་སྐྱེ་བ་སྐྱེད་པར་བྱེད༌[^326]པ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 847]
མཚན་ཉིད་དག་ནི་བཤད་ཟིན་ཏོ། །

[Block 848 [HEADING]]
##### མིང་གི་ཚོགས་ལ་སོགས་པ། ^2-2-3-7-0

[Block 849 [VERSE]]
མིང་གི་ཚོགས་ལ་སོགས་པ་ནི། །
མིང་དང་ངག་དང་ཡི་གེའི༌[^327]ཚོགས། །

[Block 850]
སོགས་པ་སྨོས་པ་ནི་ཚིག་དང་ཡི་གེའི་ཚོགས་གཟུང་ངོ་། །དེ་ལ་མིང་བྱེད་པས་ནི་མིང་སྟེ། དཔེར་ན་གཟུགས་སྒྲ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལྟ་བུའོ། །

[Block 851]
ངག་ནི་ཚིག་སྟེ་ཇི་ཙམ་གྱིས་དོན་ཡོངས་སུ་རྫོགས་པའོ། །

[Block 852]
ཡི་གེ་ནི་ཡི་གེ་སྟེ། མིང་ལ་སོགས་པ་དེ་དག་གི་ཚོགས་ནི་མིང་ལ་སོགས་པའི་ཚོགས་དག་ཡིན་ཏེ། མང་བའི་དོན་གང་ཡིན་པའོ། །

[Block 853]
ཡང་ཅི༌[^328]མིང་གི་ཚོགས་ལ་སོགས་པ་འདི་དག་ལྡན་པའམ། སེམས་ཅན་དུ་སྟོན་པའམ། སེམས་ཅན་མ་ཡིན་པར་སྟོན་པའམ། རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པའམ། རྒྱས་པ་ལས་བྱུང་བའམ། རྒྱུ་མཐུན་པ་ལས་བྱུང་བ་འམ། དགེ་བའམ། མི་དགེ་བའམ། ལུང་དུ་མ་བསྟན་པ་གཅིག་ཅེས་བརྗོད་པར་བྱ་ཞེ་ན། སྨྲས་པ། འདོད་དང་གཟུགས་གཏོགས་སེམས་ཅན་སྟོན། །རྒྱུ་མཐུན་ལུང་བསྟན་མིན། འདོད་པར་གཏོགས་པ་དང་། གཟུགས་སུ་གཏོགས་པ་འདི་དག་ནི་སྟོན་པའོ། །

[Block 854]
གང་ཞིག་རྗོད་པར༌[^329]བྱེད་པ་དེ་དག་དང་ལྡན་གྱི་བརྗོད་པར་བྱ་བ་གང་ཡིན་པ་དང་ནི་མ་ཡིན་ནོ། །

[Block 855]
རྒྱུ་མཐུན་པ་ལས་བྱུང་བ་དང་། མ་བསྒྲིབས༌[^330]ལ་ལུང་དུ་མ་བསྟན་པ་དག་ཡིན་ནོ། །

[Block 856]
ཇི་ལྟར་འདི་དག་སེམས་ཅན་དུ་སྟོན་པ་དང་། རྒྱུ་མཐུན་པ་ལས་བྱུང་བ་དང་། མ་བསྒྲིབས་ལ༌[^331]ལུང་དུ་མ་བསྟན་པ་དག་ཡིན་པ་དེ་བཞིན་དུ། སྐལ་མཉམ།[^332] དེ་ནི་རྒྱུ་མཐུན་པ་ལས་བྱུང་བ་འབའ་ཞིག་མ་ཡིན་གྱི། རྣམ་པར་སྨིན་པའང་ཡིན། ཁམས་གསུམ་པ་སྟེ། འདོད་པ་དང་གཟུགས་དང་། གཟུགས་མེད་པ་ན་སྤྱོད་པ་ཡིན་ན། །ཐོབ་རྣམ་གཉིས། རྒྱུ་མཐུན་པ་ལས་བྱུང་བ་དང་། རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པ་དག་ཡིན་ནོ། །

[Block 857]
མཚན་ཉིད་རྣམས་ཀྱང་། རྣམ་པ་གཉིས་ཏེ། ཐོབ་པ་བཞིན་ནོ། །

[Block 858]
སྙོམས་འཇུག་དང་། མི་ལྡན་པ་དག་རྒྱུ་མཐུན་པ། །སེམས་མེད་པའི་སྙོམས་པར་འཇུག་པ་གཉིས་དང་མི་ལྡན་པ་རྣམས་ནི་རྒྱུ་མཐུན་པ་ལས་བྱུང་བ་དག་ཁོ་ན་ཡིན་ནོ། །

[Block 859]
འདི་དག་ནི་ལྷག་མ་བརྗོད་པར་བྱ་བ་བཤད་ཟིན་ཏོ། །

[Block 860 [HEADING]]
### རྒྱུ་དང་རྐྱེན། ^2-3-0

[Block 861 [VERSE]]
རྒྱུ་དང་རྐྱེན་དག་མེད་པར་ནི། །
སྐྱེ་བ་བསྐྱེད་བྱ་སྐྱེད་བྱེད་མིན། །

[Block 862]
ཞེས་གང་བཤད་པ་དེ་དག་གིས་རྒྱུ་དང༌[^333]རྐྱེན་རྣམས་གང་ཞེ་ན།

[Block 863 [HEADING]]
#### རྒྱུ་རྣམ་པ་དྲུག། ^2-3-1-0

[Block 864 [HEADING]]
##### བྱེད་རྒྱུ། ^2-3-1-1-0

[Block 865 [VERSE]]
བྱེད་རྒྱུ་ལྷན་ཅིག་འབྱུང་བ་དང་། །
སྐལ་མཉམ་མཚུངས་པར་ལྡན་པ་དང་། །
ཀུན་དུ་འགྲོ་དང་རྣམ་སྨིན་དང་། །
རྒྱུ་ནི་རྣམ་པ་དྲུག་ཏུ་འདོད། །
དེ་ལ་རང་ལས་གཞན་པ་བྱེད་རྒྱུའི་རྒྱུ།

[Block 866]
རང་གི་ངོ་བོ་མ་གཏོགས་པ་ཆོས་ཐམས་ཅད་ནི་ཆོས་འདུས་བྱས་ཀྱི་བྱེད་རྒྱུ་སྟེ། སྐྱེ་བ་ལ་གེགས་མི་བྱེད་པའི་ངོ་བོར་གནས་པའི་ཕྱིར་རོ། །

[Block 867 [HEADING]]
##### ལྷན་ཅིག་འབྱུང་བའི་རྒྱུ། ^2-3-1-2-0

[Block 868]
ལྷན་ཅིག་འབྱུང་གང་ཕན་ཚུན་འབྲས། །ཆོས་གང་དག་ཕན་ཚུན་གྱི་འབྲས་བུ་ཡིན་པ་དེ་དག་ནི་ཕན་ཚུན་ལྷན་ཅིག་འབྱུང་བའི་རྒྱུའོ། །

[Block 869]
དཔེ་ཇི་ལྟ་བུ་ཞེ་ན།

[Block 870 [VERSE]]
འབྱུང་བཞིན་སེམས་ཀྱི་རྗེས་འཇུག་དང་། །
སེམས་དང་མཚན་ཉིད་མཚན་གཞི་བཞིན། །

[Block 871]
འབྱུང་བ་ཆེན་པོ་བཞི་དག་ནི་ཕན་ཚུན་ལྷན་ཅིག་འབྱུང་བའི་རྒྱུ་ཡིན་ནོ། །

[Block 872]
སེམས་ནི་སེམས་ཀྱི་རྗེས་སུ་འཇུག་པའི་ཆོས་རྣམས་ཀྱི་ཡིན་ལ། དེ་དག་ཀྱང་དེའིའོ། །

[Block 873]
འདུས་བྱས་ཀྱི་མཚན་ཉིད་རྣམས་ནི་མཚན་གཞིའི་ཡིན་ལ་དེ་ཡང་དེ་དག་གི་ཡིན་ནོ། །

[Block 874]
སེམས་ཀྱི་རྗེས་སུ་འཇུག་པའི་ཆོས་དེ༌[^334]དག་ཀྱང་གང་ཞེ་ན།

[Block 875 [VERSE]]
སེམས་ལས་བྱུང་དང་སྡོམ་གཉིས་དང་། །
སེམས་དང་དེ་དག་གི་མཚན་ཉིད། །
སེམས་ཀྱི་རྗེས་འཇུག །

[Block 876]
སེམས་ལས་བྱུང་བ་ཐམས་ཅད་དང་། བསམ་གཏན་གྱི་སྡོམ་པ་དང་། ཟག་པ་མེད་པའི་སྡོམ་པ་དང་། དེ་དག་དང་། སེམས་ཀྱི་སྐྱེ་བ་ལ་སོགས་པ་གང་ཡིན་པའི་ཆོས་དེ་དག་ནི་སེམས་ཀྱི་རྗེས་སུ་འཇུག་པ་ཞེས་བྱའོ། །

[Block 877]
དེ་དག་ཇི་ལྟར་སེམས་ཀྱི་རྗེས་སུ་འཇུག་ཅེ་ན། མདོར་བསྡུ་ན། དུས་དང་ནི། འབྲས་སོགས་དགེ་ལ་སོགས་པས་སོ། །

[Block 878]
རེ་ཞིག་དུས་ལས་ནི། སེམས་དང་ལྷན་ཅིག་སྐྱེ་བ་དང་། །གནས་པ་དང་། འགག་པ་གཅིག་པ་ཉིད་དང་། དུས་གཅིག་ཏུ་གཏོགས་པ་ཉིད་ཀྱིས་སོ། །

[Block 879]
འབྲས་བུ་ལ་སོགས་པས་ནི། འབྲས་བུ་དང་། རྣམ་པར་སྨིན་པ་དང་། རྒྱུ་མཐུན་པ་གཅིག་པ་ཉིད་ཀྱིས་ཏེ། དགེ་བ་ལ་སོགས་པས་ནི་དགེ་བ་ལ་སོགས་པའི་སེམས་ལ་དགེ་བ་ལ་སོགས་པ་ཉིད་ཀྱིས་སོ། །

[Block 880]
ལྷན་ཅིག་འབྱུང་བའི་རྒྱུ་བཤད་ཟིན་ཏོ། །
--- END BLOCKS ---
