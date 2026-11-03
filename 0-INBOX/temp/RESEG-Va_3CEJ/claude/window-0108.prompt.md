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
[Block 3781]
འདིར་བསྐལ་པ་གང་ཞིག་ཡིན་པར་རིག་པར་བྱ། ཅི་བར་གྱི་བསྐལ་པ་ཉི་ཤུར་འཆགས་པ་དང་། གང་ཡང་ཆགས་ནས་བར་གྱི༌[^2154]བསྐལ་པ་ཉི་ཤུ༌[^2155]པ་ཆེན་པོ་ཞིག་ཡིན་ཞེ་ན།

[Block 3782 [VERSE]]
འོད་ཆུང་ནས་བཟུང་བསྐལ་ཆེན་ཏེ། །
དེ་ཡི་འོག་མ་ཕྱེད་ཡིན་ནོ། །

[Block 3783]
ལྷའི་རིས་འོད་ཆུང་ནས་བཟུང་བའི་ཚེའི་ཚད་ནི་བསྐལ་པ་ཆེན་པོར་རིག་པར་བྱའོ། །

[Block 3784]
དེའི་འོག་མ་ཚངས་ཆེན་ལ་སོགས་པའི་ཚེའི་ཚད་ནི་བསྐལ་པ་ཆེན་པོ་ཕྱེད་ལ་བསྐལ་པར་བྱས་ནས་རྣམ་པར་བཞག་གོ། །ཇི་ལྟ་བུ་ཞེ་ན། གང་ཡང་འཇིག་རྟེན་བར་གྱི་བསྐལ་པ་ཉི་ཤུར་ཆགས་པ༌[^2156]དང་། གང་ཡང་ཆགས་ནས་བར་གྱི་བསྐལ་པ་ཉི་ཤུར་འདུག་པ་དང་། གང་ཡང་བར་གྱི་བསྐལ་པ་ཉི་ཤུར་འཇིག་པ་དང་། བར་གྱི་བསྐལ་པ་དྲུག་ཅུ༌[^2157]པོ་དེ་དག་ལ་ཚངས་པ་ཆེན་པོའི་བསྐལ་པ་ཕྱེད་དང་གཉིས་སུ་བཤད་དེ། [^2158]དེ་ལྟར་བྱས་ན་བསྐལ་པ་ཆེན་པོའི་ཕྱེད་བར་གྱི་བསྐལ་པ་བཞི་བཅུ་ལ་བསྐལ་པར་བྱས་ནས་དེ་དག་གིས༌[^2159]ཚེའི་ཚད་དུ་བྱས་ནས་བཤད་པ་ཡིན་ནོ། །

[Block 3785]
བདེ་འགྲོའི་ཚེའི་ཚད་བཤད་ཟིན་ཏོ། །

[Block 3786 [HEADING]]
##### ངན་འགྲོའི་ཚེའི་ཚད། ^3-2-3-2-0

[Block 3787]
ད་ནི་ངན་འགྲོའི་བརྗོད་པར་བྱ་སྟེ། དེ་ལ་རེ་ཞིག །

[Block 3788 [VERSE]]
ཡང་སོས་ལ་སོགས་དྲུག་རིམ་བཞིན། །
འདོད་ལྷའི་ཚེ་དང་ཉིན་ཞག་མཉམ། །

[Block 3789]
འདོད་པ་ན་སྤྱོད་པའི་ལྷའི་རིས་དྲུག་པོ་དེ་དག་གི་ཚེ་ཇི་ཙམ་པར་བཤད་པ་དེ་དང་གོ་རིམས༌[^2160]བཞིན་དུ་ཡང་སོས་དང་། ཐིག་ནག་དང་། བསྡུས་འཇོམས་དང་། ངུ་འབོད་དང་། ངུ་འབོད་ཆེན་པོ་དང་། ཚ་བ་དང་། དམྱལ་བ་དྲུག་གི་ཉིན་ཞག་དང་མཉམ་པར་རིག་པར་བྱ་སྟེ།

[Block 3790 [VERSE]]
དེས་ན་དེ་དག་རྣམས་ཀྱི་ཚེ། །
འདོད་པའི་ལྷ་དང་འདྲ་བ་ཡིན། །

[Block 3791]
དེ་ནི༌[^2161]རང་གི་ཉིན་ཞག་དེ་དག་གིས་དེ་དག༌[^2162]ཚེའི་ཚད༌[^2163]འདོད་པ་ན་སྤྱོད་པའི་ལྷའི་རིས༌[^2164]དྲུག་པོ་དེ་དག་གི་ཚེ་ཇི་ལྟ་བ་དེ་བཞིན་དུ་རིག་པར་བྱའོ། །ཇི་ལྟ༌[^2165]ཞེ་ན། རྒྱལ་ཆེན་བཞིའི་རིས་པ་རྣམས་ཀྱི་ཚེའི་ཚད་གང་ཡིན་པ་དེ་ནི་དམྱལ་བ་ཆེན་པོ་ཡང་སོས་ཀྱི་ཉིན་ཞག་གཅིག་ཡིན་ལ། དེས་ན་ཟླ་བ་བཅུ་གཉིས་པའི་ལོས་ཚེ་དེ་ན་ཡོད་པའི་ལོ་ལྔ་བརྒྱ་ཞེས་བྱ་བའི་བར་དུ་ཡིན་ནོ། །

[Block 3792]
སུམ་ཅུ་རྩ་གསུམ་པ་རྣམས་ཀྱི་ཚེའི་ཚད་གང་ཡིན་པ་དེ་ནི་སེམས་ཅན་དམྱལ་བ་ཆེན་པོ་ཐིག་ནག་གི་ཉིན་ཞག་གཅིག་ཡིན་ལ། ཉིན་ཞག་དེས་ན་དེའི་ཚེ་ལོ་སྟོང་སྟེ། དེ་བཞིན་དུ་གཞན་འཕྲུལ་དབང་བྱེད་པ་རྣམས་ཀྱི་ཚེའི་ཚད་དང་མཉམ་པའི་ཉིན་ཞག་གིས་དམྱལ་བ་ཆེན་པོ་ཚ་བ་ན་ཚེའི་ཚད་ལོ་ཁྲི་དྲུག་སྟོང་ཡིན་པའི་བར་དུ་གཞན་དག་ལ་ཅི་རིགས་པར་སྦྱར་བར་བྱའོ། །

[Block 3793]
རབ་ཏུ་ཚ་ཕྱེད། དམྱལ་བ་ཆེན་པོ་རབ་ཏུ་ཚ་བ་ན་ནི་ཚེའི་ཚད་བར་གྱི་བསྐལ་པ་ཕྱེད་དོ། །

[Block 3794]
མནར་མེད་ནི། བར་གྱི་བསྐལ་པའོ། །

[Block 3795]
དུད་འགྲོ་རྣམས༌[^2166]ནི་ངེས་པ་མེད་དོ། །

[Block 3796]
[^2167]དུད་འགྲོ་རྣམས། མཆོག་རིང་བསྐལ་པའོ། །

[Block 3797]
དུད་འགྲོའི་ཚེ་མཆོག་ཏུ་རིང་བ་ནི་བར་གྱི་བསྐལ་པ་གཅིག་སྟེ། ཀླུ་དགའ་བོ་དང་། ཉེ་དགའ་བོ་དང་། རྟ་མགོ་ལ་སོགས་པ་དག་སྟེ། བཅོམ་ལྡན་འདས་ཀྱིས། དགེ་སློང་དག་ཀླུ་བརྒྱད་པོ་འདི་དག་ནི་ཀླུ་ཆེན་པོ་སྟེ། བསྐལ་པར་གནས་པ། ས་འཛིན་པའོ་ཞེས་རྒྱས་པར་གསུངས་སོ། །

[Block 3798]
ཡི་དགས་རྣམས། ཟླ་བ་ཉིན་ཞག་གི་ལྔ་བརྒྱའོ། །

[Block 3799]
མི་རྣམས་ཀྱི་ཟླ་བ་གཅིག་གང་ཡིན་པ་དེ་ནི་ཡི་དགས་རྣམས་ཀྱི་ཉིན་ཞག་གཅིག༌[^2168]ཡིན་ལ། ཉིན་ཞག་དེས་ན་ཚེ་ལོ་ལྔ་བརྒྱའོ། །

[Block 3800]
ཡང་གྲང་བའི་དམྱལ་བ་དག་ན་ཚེའི་ཚད་ཇི་ཙམ་ཞེ་ན། ཇི་སྲིད་དུ།

[Block 3801 [VERSE]]
ཏིལ་སྦྱང༌[^2169]ནས་ནི་ལོ་བརྒྱ་ཞིང་། །
ཏིལ་གཅིག་ཕྱུང༌[^2170]བས་ཟད་གྱུར་པ། །
ཆུ་བུར་ཅན་གྱི་ཚེ་ཡིན་ཏེ། །

[Block 3802]
གཞན་གྱི་ཚེ་ནི་ཉི་ཤུར་འགྱུར།[^2171] །བཅོམ་ལྡན་འདས་ཀྱིས་དེ་དག་གི་ཚེའི་ཚད་ཀྱི་དཔེ་ཙམ་དུ་དགེ་སློང་དག་དཔེར་ན་འདི་ན་ཡུལ་མ་ག་དྷཱའི་ཏིལ་གྱི་སྦྱང༌[^2172]ཁལ་བརྒྱད་ཅུ་པ་ཞིག་ཏིལ་དག་གིས་བྱུར་བུར་བཀང་སྟེ། དེ་ནས་ལ་ལ་ཞིག་གིས་ལོ་བརྒྱ་བརྒྱ་འདས་ཤིང་ཏིལ་རེ་རེ་བོར་ན་དགེ་སློང་དག་རིམ་པ་དེས༌[^2173]ན་ཡུལ་མ་ག་དྷཱའི་ཏིལ་གྱི་སྦྱང༌[^2174]ཁལ་བརྒྱད་ཅུ་པ་དེ་མ་ལུས་པར་ཡོངས་སུ་ཟད་པར་གྱུར་པ་ནི་ཆེས་མྱུར་གྱི་ཆུ་བུར་ཅན་དུ་སྐྱེས་པའི་སེམས་ཅན་རྣམས་ཀྱི་ཚེ་ཡོངས་སུ་གཏུགས་པར་ནི་ང་མི་སྨྲའོ། །

[Block 3803]
དགེ་སློང་དག་ཆུ་བུར་ཅན་ཉི་ཤུ་ཇི་ལྟ་བ་དེ་བཞིན་དུ་ཆུ་བུར་རྡོལ་པ་གཅིག་ཡིན་ནོ་ཞེས་བྱ་བ་ནས་རྒྱས་པར་ཡང༌[^2175]དགེ་སློང་དག་པདྨ་ལྟར་གས་པ་ཉི་ཤུ་ཇི་ལྟ་བ་དེ་བཞིན་དུ་པདྨ་ལྟར་གས་པ་ཆེན་པོ་གཅིག་ཡིན་ནོ་ཞེས་གསུངས་སོ། །

[Block 3804 [HEADING]]
##### བར་མ་དོར་འཆི་བ། ^3-2-3-3-0

[Block 3805]
དེ་ལྟར༌[^2176]ཚེ་དང་ལྡན་པའི་སེམས་ཅན་དེ་དག་ཚེ་ཡོངས་སུ་མ་རྫོགས་པར་བར་མ་དོར་འཆི་བ་ཡོད་དམ་འོན་ཏེ། མེད་ཅེ་ན། ཐམས་ཅད་ལ་ཡོད་དེ། སྒྲ་མི་སྙན་མ་གཏོགས་པར་འཆི། །བྱང་གི་སྒྲ་མི་སྙན་དག་ན༌[^2177]ནི་སེམས་ཅན་རྣམས་ཚེ་ངེས་པ་ཡིན་ཏེ། གདོན་མི་ཟ་བར་ཚེ་རངས་པར་འཚོའོ། །

[Block 3806]
གཞན་དག༌[^2178]ནི་མ་ངེས་སོ། །

[Block 3807]
གང་ཟག་རྣམས་ལས་བར་མ་དོར་འཆི་བ་མེད་པ་ཡང་མང་སྟེ། བྱང་ཆུབ་སེམས་དཔའ་སྐྱེ་བ་གཅིག་གིས་ཐོགས་པ་དགའ་ལྡན་ན་བཞུགས་པ་དང་། སེམས་ཅན་སྲིད་པ་ཐ་མ་པ༌[^2179]དང་། རྒྱལ་བས་བསྟན་པ་དང་། རྒྱལ་བའི་ཐད་དུ་བཏང་བའི་ཕོ་ཉ་དང་། དད་པ་དང་ཆོས་ཀྱི་རྗེས་སུ་འབྲང་བ་དག་དང་། བྱང་ཆུབ་སེམས་དཔའ་དང་། འཁོར་ལོས་སྒྱུར་བའི༌[^2180]ཡུམ་དེ་དག་ལྷུམས་ན་ཡོད་པ་དང་། དེ་ལྟ་བུ་ལ་སོགས་པའོ། །

[Block 3808 [HEADING]]
#### དཔག་ཚད་དང་ལོའི་ཚད། ^3-2-4-0

[Block 3809]
དཔག་ཚད་ཀྱི་ཚད་ཀྱིས་གནས་རྣམས་དང་། ལུས་རྣམས་ཀྱང༌[^2181]ལོའི་ཚད་ཀྱིས་ཚེ༌[^2182]ཡང་བཤད་ན། དེ་གཉིས་ཀྱི་ཚད་ནི་མ་བཤད་པས་བརྗོད་པར་བྱ་ལ། དེ་དག་ཐམས་ཅད་ཀྱི་རྣམ་པར་གཞག་པ་ཡང་མིང་ཡིན་པས་དེའི་མཐའ་ཡང་བརྗོད་པར་བྱ་སྟེ། དེ་རྣམས་ཡང་དག་པར་བསྟན་པའི་ཕྱིར་དང་པོའི་རིམ་པ་བརྩམ་མོ། །

[Block 3810 [HEADING]]
##### གཟུགས་མིང་དུས་ཀྱི་མཐའ། ^3-2-4-1-0

[Block 3811]
གཟུགས་མིང་དུས་མཐའ༌[^2183]རྡུལ་ཡིག་དང་། །སྐད་ཅིག །གཟུགས་འགྲིབ་པའི་མཐའ་ནི་རྡུལ་ཕྲ་རབ་ཡིན་ནོ། །

[Block 3812]
དུས་ཀྱི་མཐའ་ནི་སྐད་ཅིག་མའོ། །

[Block 3813]
མིང་གི་མཐའ་ནི་ཡི་གེ་སྟེ། དཔེར་ན་བ་ལང་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 3814]
ཡང༌[^2184]སྐད་ཅིག་མའི་ཚད་ཇི་ཙམ་ཞེ་ན། རྐྱེན་རྣམས་ཚོགས་ན་ཇི་སྲིད་དུ་ཆོས་ཀྱི་བདག་ཉིད་ཐོབ་པའམ། ཆོས་འགྲོ་བ་ན་ཇི་སྲིད་དུ་རྡུལ་ཕྲ་རབ་ནས་རྡུལ་ཕྲ་རབ་གཞན་དུ་འགྲོ་བ་ཡིན་ནོ། །

[Block 3815]
ཆོས་མངོན་པ༌[^2185]རྣམས་ན་རེ་སྐྱེས་བུ་སྟོབས་དང་ལྡན་པའི་སེ་གོལ་གཏོགས་པ་ཙམ་གྱིས་སྐད་ཅིག་མ་དྲུག་ཅུ་རྩ་ལྔ་འདའོ་ཞེས་ཟེར་རོ། །

[Block 3816 [HEADING]]
##### དཔག་ཚད་ཀྱི་ཚད། ^3-2-4-2-0

[Block 3817 [VERSE]]
དེ་ལ་ཕྲ་རབ་རྡུལ་དང་ནི། །
རྡུལ་ཕྲན་དང་ནི་དེ་བཞིན་དུ། །
ལྕགས་ཆུ་རི་བོང་ལུག་དང་གླང་། །
ཉི་ཟེར་རྡུལ་དང་སྲོ་མ་དང་། །

[Block 3818 [VERSE]]
དེ་ལས་བྱུང་དང་དེ་བཞིན་དུ། །
སོར་ཚིགས་ཞེས་བྱ་གོང་བདུན་འགྱུར། །

[Block 3819]
རྡུལ་ཕྲ་རབ་ལ་སོགས་པ་འདི་དག་ནི་གོང་ནས་གོང་དུ་བདུན་འགྱུར་དུ་རིག་པར་བྱ་སྟེ། རྡུལ་ཕྲ་རབ་བདུན་ལ་ནི་རྡུལ་ཕྲན་ནོ། །

[Block 3820]
རྡུལ་ཕྲན་བདུན་ལ་ནི་ལྕགས་རྡུལ་ལོ། །
--- END BLOCKS ---
