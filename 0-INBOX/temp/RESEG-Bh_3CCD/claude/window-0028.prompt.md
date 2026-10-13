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
[Block 981]
བཞི་པོ༌[^707]ནི་ཀུན་རྫོབ་ཀྱི་ཕྱོགས་ཀྱི་བཤད་པ་ལ་སྣོད་དུ་རུང་བ་དང་། གཅིག་ནི་དོན་དམ་པའི་མཆོག་གི༌[^708]བཤད་པའི་སྣོད་དུ་རུང་བའོ། །

[Block 982]
དེ་ཡང་ཤིན་ཏུ་རྒྱས་པར༌[^709]འོག་ནས་འཆད་པར་འགྱུར་རོ། །

[Block 983 [HEADING]]
### གང་ཟག་བཞི། ^1-5-0

[Block 984]
གཞན་དག༌[^710]ན་རེ་གང་ཟག་བཞི་ཡོད་དེ། མི་ཤེས་པ་དང་། ཐེ་ཚོམ་ཟ་བ་དང་། ཕྱིན་ཅི་ལོག་པའི་བློ་དང་། ངེས་པ་ཅན་གྱི་བློ་ཅན་ནོ། །

[Block 985 [HEADING]]
#### མི་ཤེས་པ། ^1-5-1-0

[Block 986]
དེ་ལ་མི་ཤེས་པ་ནི་རྣམ་པ་གཉིས་ཏེ། ཚད་མའི་རྗེས་སུ་འབྲང་བ་དང་། ཚད་མ་མ་ཡིན་པའི་རྗེས་སུ་འབྲང་བའོ། །

[Block 987]
དེ་ལ་ཚད་མའི་རྗེས་སུ་འབྲང་བ་ནི་གཞན་གྱི་རིགས་པ་ལེན་ཅིང་ཐོས་པ༌[^711]ལ་སོགས་པའི་རིམ་གྱིས་ལམ་ལ་བརྟེན་པའོ། །

[Block 988]
ཚད་མ་མ་ཡིན་པའི་རྗེས་སུ་འབྲང་བ་ནི་མཁས་པའི་ཚིག༌[^712]ལ་བརྟེན་ཏེ་ལམ་ལ་འཇུག་པའོ། །

[Block 989]
དེ་དག་གཉིས་ཀ་ཡང་ལམ་གྱི་སྣོད་དུ་རུང་བའོ། །

[Block 990 [HEADING]]
#### ཐེ་ཚོམ་ཟ་བ། ^1-5-2-0

[Block 991]
ཐེ་ཚོམ་ཟ་བ་ལ་ཡང་རྣམ་པ་གཉིས་ཏེ་སྔ་མ་བཞིན་ཏེ། ཐེ་ཚོམ་ཟ་བ་ཚད་མའི་རྗེས་སུ་འབྲང་བ་ནི་ཡང་དག་པར་ཚད་མ་བརྗོད་པས་ཐེ་ཚོམ་ལས་ལོག་ཅིང་ཡང་དག་པའི་ལམ་ལ་གཞག་པར༌[^713]བྱ་བ་ཞེས་རྗེས་སུ་གཟུང་བར༌[^714]བྱའོ། །

[Block 992]
ཚད་མའི་རྗེས་སུ་མི་འབྲང་བའི་ཐེ་ཚོམ་ཟ་བ་ནི་བཅོམ་ལྡན་འདས་དེ་བཞིན་གཤེགས་པས་ཀྱང་རྗེས་སུ་གཟུང་བར༌[^715]མི་སྤྱོད་དོ། །

[Block 993]
ཇི་སྐད་དུ།

[Block 994 [VERSE]]
མི་ཤེས་པ་ནི་བདེ་བར་མགུ་གྱུར་ཅིང་། །
ཁྱད་པར་ཤེས་པ་དེ་བས་མྱུར་བར་མགུ། །
དུམ་གཅིག་ཤེས་པས༌[^716]མེ་ཡིས་ཕྱེད་ཚིག་པ། །
མེ་དེ་སངས་རྒྱས་ཀྱིས་ཀྱང་མགུ་བྱ་མིན། །

[Block 995]
དེ་བས་ན་བཏང་སྙོམས་ཀྱི་གནས་སུ་བཤད་དོ། །

[Block 996 [HEADING]]
#### ཕྱིན་ཅི་ལོག་པའི་བློ་ཅན། ^1-5-3-0

[Block 997]
ཕྱིན་ཅི་ལོག་པའི་བློ་ཅན་ནི་རྣམ་པ་གསུམ་སྟེ། ཐེ་ཚོམ་ཟ་བ་ལ་ཕྱིན་ཅི་ལོག་པ་དང་། མི་ཤེས་པ་ལ་ཕྱིན་ཅི་ལོག་པ་དང་། ཤེས་པ་ལ་ཕྱིན་ཅི་ལོག་པའོ། །

[Block 998 [HEADING]]
##### ཐེ་ཚོམ་ཟ་བ་ལ་ཕྱིན་ཅི་ལོག་པ། ^1-5-3-1-0

[Block 999]
དེ་ལ་ཐེ་ཚོམ་ཟ་བ་ལ་ཕྱིན་ཅི་ལོག་པ་ནི་ཉན་ཐོས་ལྟ་བུ་སྔགས་ནི་ཡང་དག་པ་མ་ཡིན་ནོ་ཞེས་ཟེར་བ་ཐབས་གང་གིས་ཀྱང་རྗེས་སུ་གཟུང་བར་བྱ་བ་མ་ཡིན་པས་བཏང་སྙོམས་ཀྱི་གནས་ཁོ་ནའོ། །

[Block 1000 [HEADING]]
##### མི་ཤེས་པ་ལ་ཕྱིན་ཅི་ལོག་པ། ^1-5-3-2-0

[Block 1001]
མི་ཤེས་པ་ལ་ཕྱིན་ཅི་ལོག་པ་ནི་ཆོས་བསྟན་པ་ཙམ་གྱིས་ཕྱིན་ཅི་ལོག་པ་ལས་ལོག་ཅིང་ལམ་དུ་འཇུག་པར་བྱའོ། །

[Block 1002 [HEADING]]
##### ཤེས་པ་ལ་ཕྱིན་ཅི་ལོག་པ། ^1-5-3-3-0

[Block 1003]
ཤེས་པ་ལ་ཕྱིན་ཅི་ལོག་པ་ལ་ཡང་གཉིས་ཏེ། ཚད་མའི་རྗེས་སུ་འབྲང་བ་དང་། ཚད་མའི་རྗེས་སུ་འབྲང་བ་མ་ཡིན་པའོ། །

[Block 1004 [HEADING]]
###### ཚད་མའི་རྗེས་སུ་འབྲང་བ་མ་ཡིན་པ། ^1-5-3-3-2-0

[Block 1005]
དེ་ལ་ཤེས་པ་ལ་ཚད་མའི་རྗེས་སུ་འབྲང་བ་མ་ཡིན་པའི༌[^717]ཕྱིན་ཅི་ལོག་པའི་བློ་ཅན་ནི་གང་གིས་ཀྱང་ལམ་དུ་འཇུག་པར་བྱེད་མི་ནུས་ཏེ། ཕྱིན་ཅི་ལོག་པའི་ལྟ་བ་དང་ལྡན་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1006 [HEADING]]
###### ཚད་མའི་རྗེས་སུ་འབྲང་བ། ^1-5-3-3-1-0

[Block 1007]
ཤེས་པ་ལ་ཚད་མའི་རྗེས་སུ་འབྲང་བ་ཕྱིན་ཅི་ལོག་པའི་བློ་ཅན་ལ༌[^718]རྣམ་པ་དྲུག་སྟེ། གྲངས་ཅན་པ་དང་། རིགས་པ་པ་དང་། འཇིག་རྟེན་རྒྱང་པན་པ་དང་། མཆོད་འོས་པ་དང་། ཞི་བ་པ་དང་། དཔྱོད་པ༌[^719]པའོ། །

[Block 1008 [HEADING]]
###### **གྲངས་ཅན་པ།** ^1-5-3-3-1-1-0

[Block 1009]
གཡོ་བ་དང་མི་གཡོ་བ་འདི་དག་ཐམས་ཅད་དེ་ཁོ་ན་ཉིད༌[^720]ཉི་ཤུ་རྩ་ལྔ་པའོ། །

[Block 1010]
བློའི་དབང་པོ་ལྔ་ནི་མིག་ལ་སོགས་པ་ལྔའོ། །

[Block 1011]
ལས་ཀྱི་དབང་པོ་ལྔ་ནི།[^721] ངག་དང་། ལག་པ་དང་། རྐང་པ་དང་། བཤང་ལམ་དང་། གསང་བའི་དབང་པོའོ། །

[Block 1012]
གཟུགས་ལ་སོགས་པ་ཡུལ་ལྔ་དང་། ས་ལ་སོགས་པ་འབྱུང་བ་ཆེན་པོ་ལྔ༌[^722]དང་། ནང་གི་བྱེད་པ་གསུམ་སྟེ། ཡིད་དང་། བློ་དང་། ང་རྒྱལ་ལོ། །

[Block 1013]
གཙོ་བོའི་རྣམ་གྲངས་ཅན་རང་བཞིན་དང་སྐྱེས་བུའོ། །

[Block 1014]
དེ་ལ་དེ་ཁོ་ན་ཉིད༌[^723]ཉི་ཤུ་རྩ་གསུམ་ནི་འབྲས་བུ་ཡང་ཡིན་ལ་རྒྱུ་ཡང་ཡིན་ནོ། །

[Block 1015]
རང་བཞིན་ནི་རྒྱུ་ཁོ་ནའོ། །

[Block 1016]
སྐྱེས་བུ་ནི་རྒྱུ་ཡང་མ་ཡིན་འབྲས་བུ་ཡང་མ་ཡིན་ནོ། །

[Block 1017]
ཇི་སྐད་དུ།

[Block 1018 [VERSE]]
རྩ་བའི་རང་བཞིན་བྱ་བ་མ་ཡིན་ཏེ། །
ཆེན་པོ་ལ་སོགས་བདུན་པོ་རྒྱུ་འབྲས་ཡིན། །
བཅུ་དྲུག་པོ་ནི་འབྲས་བུ་ཉིད་ཡིན་ཏེ། །
རྒྱུ་མིན་འབྲས་མིན་སྐྱེས་བུ་དེ་ཡིན་ནོ། །

[Block 1019]
དེའི་དོན་ནི་འདི་ཡིན་ཏེ། ཡོན་ཏན་གསུམ་གྱི་བདག་ཉིད་ཅན་ལུས་ཅན་ཐམས་ཅད་ཀྱི་རྒྱུར་གྱུར་པའི་རང་བཞིན་ནི་གཙོ་བོའོ། །

[Block 1020]
སྙིང་སྟོབས་དང་། རྡུལ་དང་མུན་པ་གསུམ་ནི་ཡོན་ཏན་ནོ། །
--- END BLOCKS ---
