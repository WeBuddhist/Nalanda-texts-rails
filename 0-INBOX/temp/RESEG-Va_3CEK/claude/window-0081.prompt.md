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
[Block 2836]
རྣམ་པ་བདུན་དང་བརྒྱད་སྤངས་པ་དེ་ནི་འབྲས་བུ་གསུམ་པ་ལ་ཞུགས་པ་ཡིན་པར༌[^1955]རིག་པར་བྱའོ། །

[Block 2837]
སྔོན་རྣམ་པ་གསུམ་དང་བཞི་སྤངས་པའམ།

[Block 2838]
བདུན་པ་དང་བརྒྱད་པ་སྤངས་པ་འབྲས་བུ་ཐོབ་པ་ནི་ཇི་སྲིད་དུ་འབྲས་བུ་ཁྱད་པར་ཅན་གྱི་ལམ་མངོན་དུ་མ་བྱས་པ་དེ་སྲིད་དུ་རིགས་ནས་རིགས་སུ་སྐྱེ་བའམ་བར་ཆད་གཅིག་པ་མ་ཡིན་ནོ། །

[Block 2839 [HEADING]]
##### ཕྱིར་མི་འོང་བ། ^3-2-8-7-0

[Block 2840]
དེ་དགུ་ཟད་པས་ཕྱིར་མི་འོང་། །འབྲས་བུ་ལ་གནས་པ་དེ་ཉིད་རྣམ་པ་དགུ་སྤངས་པས་ཕྱིར་མི་འོང་བ་ཡིན་པར་རིག་པར༌[^1956]བྱ་སྟེ། འདོད་པའི་ཁམས་སུ་མི་འོང་བའི་ཕྱིར་རོ། །

[Block 2841]
ཀུན་ཏུ་སྦྱོར་བ་ཐ་མའི་ཆ་དང་མཐུན་པ་རྣམ་པ་ལྔ་སྤངས་པའི་ཕྱིར་ཞེས་འབྱུང་བ་ནི་སྤངས་པ་སྡོམ་པའི་ཕྱིར་ཏེ། གདོན་མི་ཟ་བར་སྔོན་གཉིས་སམ་གསུམ་སྤངས་པ་ཡིན་ནོ། །

[Block 2842 [HEADING]]
###### ཕྱིར་མི་འོང་བ་རྣམ་པ་ལྔ། ^3-2-8-7-1-0

[Block 2843 [VERSE]]
དེ་ནི་བར་སྐྱེས་འདུ་བྱེད་དང་། །
འདུ་བྱེད་མེད་སྤངས༌[^1957]མྱ་ངན་འདའ། །

[Block 2844]
གོང་དུ་འཕོ་བ་རྣམས་འདི་བར་མ་དོར་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བས་ན༌[^1958]བར་མ་དོར་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་སྟེ། དེ་བཞིན་དུ་སྐྱེས་ནས༌[^1959]དང་། འདུ་བྱེད་པ་དང་འདུ༌[^1960]བྱེད་པ་མེད་པ་ལ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 2845 [HEADING]]
###### **བར་མ་དོར་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ།** ^3-2-8-7-1-1-0

[Block 2846]
ཕྱིར་མི་འོང་བ་དེ་ཉིད་རྣམ་པ་ལྔ་ཡིན་ཏེ། བར་མ་དོར་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་ནི་སྲིད་པ་བར་མ་དོར་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ༌[^1961]གང་ཡིན་པའོ། །

[Block 2847 [HEADING]]
###### **སྐྱེས་ནས་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ།** ^3-2-8-7-1-2-0

[Block 2848]
སྐྱེས་ནས་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་ནི་སྐྱེས་པ་ཙམ་ལས་མི་འཆི་བར་ཕུང་པོའི་ལྷག་མ་དང་བཅས་པའི་མྱ་ངན་ལས་འདའ་བས་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་སྟེ། མངོན་པར་བརྩོན་པ་དང་། [^1962]ལམ་ངང་གིས་འབྱུང་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2849]
གཞན་དག་ན་རེ་དེ་ཡང་ཕུང་པོའི་ལྷག་མ་མེད་པས་སོ་ཞེས་ཟེར་རོ། །

[Block 2850]
མ་ཡིན་ཏེ། ཚེ་འདོར་བ་ལ་དབང་མེད་པའི་ཕྱིར་རོ། །

[Block 2851 [HEADING]]
###### **མངོན་པར་འདུ་བྱེད་པ་དང་བཅས་པས་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ།** ^3-2-8-7-1-3-0

[Block 2852]
མངོན་པར་འདུ་བྱེད་པ་དང་བཅས་པས་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ༌[^1963]ནི་སྐྱེས་ནས་སྦྱོར་བ་མ་བཏང་ཞིང་མངོན་པར་འདུ་བྱེད་པ་དང་བཅས་པས་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་གང་ཡིན་པ་སྟེ། མངོན་པར་བརྩོན་པ་དང༌[^1964]ལམ་ངང་གིས་འབྱུང་བ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2853 [HEADING]]
###### **མངོན་པར་འདུ་བྱེད་པ་མེད་པར་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ།** ^3-2-8-7-1-4-0

[Block 2854]
མངོན་པར་འདུ་བྱེད་པ་མེད་པར་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་ནི་མངོན་པར་འདུ་བྱེད་པ་མེད་པར་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་སྟེ། མངོན་པར་མི་བརྩོན་པ་དང་ལམ་ངང༌[^1965]གིས་འབྱུང་བ་མེད་པའི་ཕྱིར་རོ་ཞེས་གྲག་གོ། །

[Block 2855]
གཞན་དག་ན་རེ་འདུས་བྱས་དང་འདུས་མ་བྱས་པ༌[^1966]ལ་དམིགས་པའི་ལམ་གྱིས་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བའི་ཕྱིར་རོ་ཞེས་ཟེར་རོ། །

[Block 2856]
དེ་ནི་མི་རུང་སྟེ། ཧ་ཅང་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2857]
མདོ་ལས་ནི་མངོན་པར་འདུ་བྱེད་པ་མེད་པར་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ༌[^1967]སྔར་འབྱུང་བས་དེ་ཁོ་ན་བཞིན་དུ་རུང་སྟེ། ལམ་ངང་གིས་འབྱུང་བ་དང་ངང་གིས་འབྱུང་བ་མ་ཡིན་པ་དག་ནི༌[^1968]འབད་པ་མེད་པ་དང་འབད་པས་འཐོབ་པའི་སྒོ་ནས་མངོན་པར་འདུ་བྱེད་པ་མེད་པ་དང་མངོན་པར་འདུ་བྱེད་པས་བསྒྲུབ་པར་བྱ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2858]
སྐྱེས་ནས་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་ནི་ལམ་ཆེས་ངང་གིས་འབྱུང་བ་དང་། ཆེས་ཆེ་བ་དང་། ཕྲ་རྒྱས་ཆེས་ཆུང་བ་ཡིན་ནོ། །

[Block 2859 [HEADING]]
###### **གོང་དུ་འཕོ་བ།** ^3-2-8-7-1-5-0

[Block 2860]
གོང་དུ་འཕོ་བ་ནི་གང་དུ་སྐྱེས་པ་དེ་ཉིད་དུ་ཡོངས་སུ་མྱ་ངན་ལས་མི་འདའ་བར་གོང་དུ་འགྲོ་བ་གང་ཡིན་པ་སྟེ། འཕོ་བ་དང་འགྲོ་བ་ཞེས་བྱ་བ་ནི་དོན་གཅིག་གོ། །

[Block 2861 [HEADING]]
###### **བསམ་གཏན་སྤེལ་ནས་འོག་མིན་འགྲོ་བ།** ^3-2-8-7-1-5-1-0

[Block 2862]
དེ་ནི་བསམ་གཏན་སྤེལ་ནས༌[^1969]འོག་མིན་འགྲོ། །གོང་དུ་འཕོ་བ་དེ་ནི་རྒྱུ་དང་འབྲས་བུའི་སྒོ་ནས་རྣམ་པ་གཉིས་ཏེ། རྒྱུའི་སྒོ་ནས་ནི༌[^1970]བསམ་གཏན་སྤེལ་བ་དང་། སྤེལ་བ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2863]
འབྲས་བུའི་སྒོ་ནས་ནི་འོག་མིན་དང་སྲིད་པའི་རྩེ་མོ་ལ་ཐུག་པའི་ཕྱིར་རོ། །

[Block 2864]
དེ་ལ་གང་གིས་བསམ་གཏན་སྤེལ་བ་དེ་ནི་འོག་མིན་དུ་སོང་ནས་ཡོངས་སུ་མྱ་ངན་ལས་འདས་པའོ།[^1971] །

[Block 2865 [HEADING]]
###### **འཕར་བ།** ^3-2-8-7-1-5-1-1-0

[Block 2866]
དེ་འཕར་ཕྱེད་འཕར་ཐམས་ཅད་དུ། །འཆི་འཕོ་གོང་དུ་འཕོ་བ་འོག་མིན་གྱི་མཐར་ཐུག་པ་དེ་ཡང་འཕར་བ་ལ་སོགས་པའི་བྱེ་བྲག་གིས་རྣམ་པ་གསུམ་སྟེ། དེ་ལ་འཕར་བ་ཞེས་བྱ་བ་ནི་འདིར་བསམ་གཏན་རྣམ་པར༌[^1972]སྤེལ་ནས་བསམ་གཏན་དང་པོའི་རོ་མྱངས་ཏེ་བསམ་གཏན་གསུམ་ལས་ཡོངས་སུ་ཉམས་པ་ཚངས་རིས་པ་དག་གི་ནང་དུ་སྐྱེས་ནས་སྔོན་གོམས་པའི་དབང་གིས་བསམ་གཏན་བཞི་པ་སྤེལ་ཏེ། དེ་ནས་ཤི་འཕོས་ནས་འོག་མིན་པ་དག་གི་ནང་དུ་སྐྱེ་བ་གང་ཡིན་པ་སྟེ། དེ་ནི་བར་དུ་མི་འགྲོ་བས་ན་འཕར་བ་ཞེས་བྱའོ། །

[Block 2867 [HEADING]]
###### **ཕྱེད་དུ་འཕར་བ།** ^3-2-8-7-1-5-1-2-0

[Block 2868]
ཕྱེད་དུ་འཕར་བ་ཞེས་བྱ་བ་ནི་དེ་ནས༌[^1973]གནས་གཙང་མ་རྣམས་སུ་སྐྱེས་ལ་བར་ནས་གནས་གཞན་འགའ་ཙམ་ཡང་རྒལ༌[^1974]ཏེ་འོག་མིན་དུ་འཕོས་ནས་འོག་མིན་དུ༌[^1975]འཇུག་པ་གང་ཡིན་པའོ། །

[Block 2869]
འཕགས་པ་ནི་ཚངས་ཆེན་པ་དག་གི་ནང་དུ་མི་སྐྱེ་སྟེ། ཅིའི་ཕྱིར་ཞེ་ན། [^1976]ལྟ་བའི་གནས་ཡིན་པའི་ཕྱིར་དང་། གཙོ་བོ་གཅིག་ཏུ་ཟད་པའི་ཕྱིར་དང་། [^1977]

[Block 2870 [HEADING]]
###### **གནས་ཐམས་ཅད་དུ་འཆི་འཕོ་བ།** ^3-2-8-7-1-5-1-3-0

[Block 2871]
གནས་ཐམས་ཅད་དུ་འཆི་འཕོ་བ་ཞེས་བྱ་བ་ནི་གནས་གཞན་ཐམས་ཅད་དུ་འཕོས་ནས་འོག་མིན་དུ་འཇུག་པ་གང་ཡིན་པའོ། །

[Block 2872]
ཕྱིར་མི་འོང་བ་ནི་ནམ་ཡང་སྐྱེ་བའི་སྐྱེ་མཆེད་དེ་ཉིད་དུ་ཚེ་གཉིས་པ་མངོན་པར་འགྲུབ་པར་མི་བྱེད་དེ། ཁྱད་པར་དུ་འགྲོ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2873]
འདི་ལྟར་ན་འདིའི་ཕྱིར་མི་འོང་བ་ཉིད་ཡོངས་སུ་རྫོགས་པ་ཡིན་ཏེ། གང་དུ་སྐྱེས་པ༌[^1978]དེ་འོག་དང་དེར་གཏན་དུ་མི་འོང་བའི་ཕྱིར་རོ། །

[Block 2874]
རེ་ཞིག་བསམ་གཏན་སྤེལ་ནས༌[^1979]འོག་མིན་དུ་འགྲོ་བ་ནི་དེ་ལྟ་བུ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 2875 [HEADING]]
###### **སྲིད་པའི་རྩེ་མོར་འགྲོ་བ།** ^3-2-8-7-1-5-2-0
--- END BLOCKS ---
