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
[Block 3711]
བཞི་པའི་ནི་སྟོང་གསུམ་པ་ཙམ་མོ་ཞེས་ཟེར་རོ། །

[Block 3712]
གཞན་དག་ན་རེ་དང་པོ་ལ་སོགས་པ་ནི་སྟོང་ལ་སོགས་པའི་ཚད་ཙམ་མོ། །

[Block 3713]
བཞི་པ་ནི་ཚད་མེད་དོ་ཞེས་ཟེར་རོ། །

[Block 3714 [HEADING]]
##### སྟོང་ཆུང་ངུ་དང་སྟོང་གཉིས་པ་དང་སྟོང་གསུམ། ^3-2-1-19-0

[Block 3715]
ཡང་སྟོང་ཆུང་ངུའི་འཇིག་རྟེན་གྱི་ཁམས་འདི་ཅི། སྟོང་གཉིས་པ་འམ། སྟོང་གསུམ༌[^2119]པ་ནི་ཅི་ཞེ་ན།

[Block 3716 [HEADING]]
###### སྟོང་སྤྱི་ཕུད། ^3-2-1-19-1-0

[Block 3717 [VERSE]]
གླིང་བཞི༌[^2120]དང་ནི༌[^2121]ཉི་ཟླ་དང་། །
རི་རབ་དང་ནི་འདོད་ལྷ་དང་། །
ཚངས་པའི་འཇིག་རྟེན་སྟོང་ལ་ནི། །
སྟོང་ནི་སྤྱི་ཕུད་ཡིན་པར་འདོད། །

[Block 3718]
འཛམ་བུའི་གླིང་དང་། ཤར་གྱི་ལུས་འཕགས་དང་། ནུབ་ཀྱི་བ་ལང་སྤྱོད་དང་། བྱང་གི་སྒྲ་མི་སྙན་སྟོང་དང་། ཉི་མ་དང་། ཟླ་བ་དང་། རི་རབ་སྟོང་དང་། རྒྱལ་ཆེན་བཞིའི་རིས་ཀྱི་ལྷ་རྣམས་ནས་གཞན་འཕྲུལ་དབང་བྱེད་ཀྱི་བར་སྟོང་དང་། ཚངས་པའི་འཇིག་རྟེན༌[^2122]འདི་ནི་སྟོང་སྤྱི་ཕུད་ཀྱི་འཇིག་རྟེན་གྱི་ཁམས་ཞེས་བྱའོ། །

[Block 3719 [HEADING]]
###### སྟོང་གཉིས་པ་བར་མའི་འཇིག་རྟེན་གྱི་ཁམས། ^3-2-1-19-2-0

[Block 3720 [VERSE]]
དེ་སྟོང་ལ་ནི་སྟོང་གཉིས་པ། །
བར་མའི་འཇིག་རྟེན་ཁམས་ཡིན་ནོ། །

[Block 3721]
སྟོང་ཆུང་ངུའི་འཇིག་རྟེན་གྱི་ཁམས་དེ་དག་སྟོང་ནི་སྟོང་གཉིས་པ་བར་མའི་འཇིག་རྟེན་གྱི་ཁམས་ཡིན་ནོ། །

[Block 3722 [HEADING]]
###### སྟོང་གསུམ་གྱི་སྟོང་ཆེན་པོའི་འཇིག་རྟེན་གྱི་ཁམས། ^3-2-1-19-3-0

[Block 3723]
དེ་སྟོང་ལ་ནི་སྟོང་གསུམ་མོ། །

[Block 3724]
སྟོང་གཉིས་པའི་འཇིག་རྟེན་གྱི་ཁམས་དེ་དག་སྟོང་ནི་སྟོང་གསུམ་གྱི་སྟོང་ཆེན་པོའི༌[^2123]འཇིག་རྟེན་གྱི་ཁམས་ཡིན་ཏེ། འདི་ཐམས་ཅད་ནི། མཉམ་དུ་འཇིག་ཅིང་འབྱུང་བ་ཡིན། །མཉམ་དུ་འཇིག་ཅིང་མཉམ་དུ་འབྱུང་སྟེ། འབྱུང་བ་ནི་ཆགས་པ༌[^2124]ཡིན་ནོ་ཞེས་འོག་ནས་བཤད་པར་བྱའོ། །

[Block 3725 [HEADING]]
#### སེམས་ཅན་རྣམས་ཀྱི་ཚད། ^3-2-2-0

[Block 3726]
ཡང་ཇི་ལྟར་སྣོད་རྣམས་ཀྱི་ཚད་བྱེ་བྲག་ཡོད་པ་དེ་བཞིན་དུ་དེ་ན་གནས་པའི་སེམས་ཅན་རྣམས་ཀྱི་ཚད་ཀྱང་། [^2125]བྱེ་བྲག་ཡོད་དམ་ཞེ་ན། སྨྲས་པ་ཡོད་དེ། དེ་ལ་རེ་ཞིག །

[Block 3727 [VERSE]]
འཛམ་བུའི་གླིང་པ་རྣམས་ཀྱི་ཚད། །
ཁྲུ་བཞི་པ་དང་ཕྱེད་དང་བཞི། །

[Block 3728]
འཛམ་བུའི་གླིང་པའི་མི་རྣམས་ནི་ཕལ་ཆེར་ཁྲུ་ཕྱེད་དང་བཞི་པའོ། །

[Block 3729]
ཁ་ཅིག་ནི་ཁྲུ་བཞི་པ་དག་ཡིན་ནོ། །

[Block 3730 [VERSE]]
ཤར་དང་བ་ལང་སྤྱོད་དང་ནི། །
བྱང་ཞེས་བྱ་བ་གཉིས་འགྱུར༌[^2126]བསྐྱེད། །

[Block 3731]
ཤར་གྱི་ལུས་འཕགས་པ་རྣམས་དང་ནུབ་ཀྱི་བ་ལང་སྤྱོད་པ་རྣམས་དང་། བྱང་གི་སྒྲ་མི་སྙན་པ་རྣམས་ནི་རིམ་བཞིན་དུ་ཁྲུ་བརྒྱད་པ་དང་། བཅུ་དྲུག་པ་དང་།

[Block 3732 [VERSE]]
སུམ་ཅུ་རྩ་གཉིས་པ་དག་ཡིན་ནོ། །
འདོད་དང་ལྡན་པའི་ལྷ་ཡི་ལུས། །
བཞི་ཆ་ནས་ནི་རྒྱང་གྲགས་དག །
ཕྱེད་དང་གཉིས་ཀྱི་བར་དུ་བསྐྱེད། །

[Block 3733]
བཞི་ཆ་ཞེས་བྱ་བ་ནི་རྒྱང་གྲགས་ཀྱི་བཞི་ཆ་སྟེ། རྒྱལ་ཆེན་བཞིའི་རིས་པ་རྣམས་ཀྱི་ལུས་ནི་དེ་ཙམ་མོ། །

[Block 3734]
སུམ་ཅུ་རྩ་གསུམ་པ་རྣམས་ཀྱི་ནི་བཞི་ཆ་གཉིས་སོ། །

[Block 3735]
འཐབ་བྲལ་བ་རྣམས་ཀྱི་ནི་བཞི་ཆ་གསུམ་མོ། །

[Block 3736]
དགའ་ལྡན་པ་རྣམས་ཀྱི་ནི་རྒྱང་གྲགས་གཅིག་གོ། །

[Block 3737]
འཕྲུལ་དགའ་བ་རྣམས་ཀྱི་ནི་རྒྱང་གྲགས་གཅིག་དང་བཞི་ཆ་གཅིག་གོ། །

[Block 3738]
གཞན་འཕྲུལ་དབང་བྱེད་པ་རྣམས་ཀྱི་ནི༌[^2127]རྒྱང་གྲགས་ཕྱེད་དང་གཉིས་སོ། །

[Block 3739]
གཟུགས་ཅན་དང་པོ་དཔག་ཚད་ཕྱེད། །གཟུགས་ཅན་གྱི་ལྷ་རྣམས་ཀྱི་གནས་ཀྱི་དང་པོ་ནི༌[^2128]ཚངས་རིས་པ་རྣམས་ཀྱི་ལུས་ནི་དཔག་ཚད་ཕྱེད་ཙམ་མོ། །

[Block 3740]
དེ་ཡི་གོང་མ་ཕྱེད་ཕྱེད་བསྐྱེད། །གནས་གསུམ་དག་ན་ཚངས་པའི་མདུན་ན་འདོན་རྣམས་ཀྱི་དཔག་ཚད་གཅིག་གོ། །

[Block 3741]
ཚངས་པ་ཆེན་པོའི་ནི་ཕྱེད་དང་གཉིས་སོ། །

[Block 3742]
འོད་ཆུང་པ་རྣམས་ཀྱི༌[^2129]ནི་དཔག་ཚད་གཉིས་སོ། །

[Block 3743 [VERSE]]
འོད་ཆུང་རྣམས་ཀྱི་ལྷ་ཡན༌[^2130]ཆད། །
ལུས་ནི་ཉིས་འགྱུར་ཉིས་འགྱུར་ཏེ། །
སྤྲིན་མེད་དཔག་ཚད་གསུམ་དོར་རོ། །

[Block 3744]
ཚད་མེད་འོད་རྣམས་ཀྱི་ནི༌[^2131]དཔག་ཚད་བཞིའོ། །

[Block 3745]
འོད་གསལ་བ་རྣམས་ཀྱི་ནི་བརྒྱད་དེ། དེ་བཞིན་དུ་དགེ་རྒྱས་པ་རྣམས་ཀྱི་ནི་དྲུག་ཅུ་རྩ་བཞི་ཡིན་པའི་བར་དུ་ཉིས་འགྱུར་དུ་བསྐྱེད་དོ། །

[Block 3746]
སྤྲིན་མེད་པ་རྣམས་ཀྱི་ནི་ཉིས་འགྱུར་དུ་བསྒྱུར་ནས་དེ་ལས་དཔག་ཚད་གསུམ་ཕྲི་ནས་དཔག་ཚད་བརྒྱ་ཉི་ཤུ་རྩ་ལྔ་པའོ།[^2132] །དེ་ཡན་ཆད་བསོད་ནམས་སྐྱེས་པ་ལ་སོགས་པ་ནས་འོག་མིན་པ་རྣམས་ཀྱི་ལུས་དཔག་ཚད༌[^2133]ཁྲི་དྲུག་སྟོང་ཡིན་པའི་བར་དུ་ཉིས་འགྱུར་ཉིས་འགྱུར་དུ་བསྒྱུར༌[^2134]རོ། །

[Block 3747 [HEADING]]
#### ཚེའི་ཚད། ^3-2-3-0

[Block 3748 [HEADING]]
##### བདེ་འགྲོའི་ཚེའི་ཚད། ^3-2-3-1-0

[Block 3749 [HEADING]]
###### མི་རྣམས། ^3-2-3-1-1-0

[Block 3750]
ཅི་དེ་ལྟར་བོང་ཚོད་ཐ་དད་པ་རྣམས་ཀྱི་ཚེ་ཡང་བྱེ་བྲག་ཡོད་དམ་ཞེ་ན། སྨྲས་པ་ཡོད་དེ། སྒྲ་མི་སྙན་ན་ཚེ་སྟོང་སྟེ། །ལོ་རྣམས་སོ། །
--- END BLOCKS ---
