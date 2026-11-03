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
[Block 2731 [HEADING]]
#### འབྲས་བུ་དང་པོ་ལ་ཞུགས་པ། ^3-2-2-0

[Block 2732]
དེ་གཉིས་ནི།

[Block 2733 [VERSE]]
བསྒོམ་པས༌[^1884]སྤང་བྱ་མ་སྤངས་ན། །
འབྲས་བུ་དང་པོ་ལ་ཞུགས་པ། །

[Block 2734]
འབྲས་བུ་རྣམས་ཀྱི་དང་པོ་ནི་འབྲས་བུ་དང་པོ་སྟེ། རྒྱུན་དུ་ཞུགས་པའི་འབྲས་བུའོ། །

[Block 2735]
དེ་ནི་འབྲས་བུ་ཐོབ་པར་བྱ་བ་ཐམས་ཅད་ཀྱི་དང་པོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2736]
དད་པ་དང་ཆོས་ཀྱིས༌[^1885]རྗེས་སུ་འབྲང་བ་དེ་དག་ཉིད་གལ་ཏེ་སྔོན་འཇིག་རྟེན་པའི་ལམ་གྱིས་བསྒོམ་པས་སྤང་བར་བྱ་བ་མ་སྤངས་པ༌[^1886]འཆིང་བ་མཐའ་དག་དང་ལྡན་པ་ཞིག༌[^1887]ཡིན་ན་ནི་དེ་གཉིས་རྒྱུན་དུ་ཞུགས་པའི་འབྲས་བུ་ལ་ཞུགས་པ་ཞེས་བྱའོ། །

[Block 2737]
རྣམ་ལྔའི་བར་བཅོམ། གལ་ཏེ་སྔོན་འཇིག་རྟེན་པའི་ལམ་གྱིས་བསྒོམས་ཏེ་སྤང་བར་བྱ་བ་འདོད་པ་ན་སྤྱོད་པ་རྣམས་ལས་རྣམ་པ་ལྔའི་བར་དུ་སྤངས་པ་ཞིག་ཡིན་ན་ཡང་དེ་ཁོ་ན༌[^1888]བཞིན་དུ་དང་པོའི་འབྲས་བུ་ལ་ཞུགས་པ་དག་ཅེས་བྱའོ། །

[Block 2738 [HEADING]]
#### འབྲས་བུ་གཉིས་པ་ལ་ཞུགས་པ། ^3-2-3-0

[Block 2739]
གཉིས་པ་ལ།

[Block 2740]
དགུ་པ་ཚུན་ཆད་ཟད་པ་ཡིན། །

[Block 2741]
གཉིས་པ་ལ་ཞེས་བྱ་བ༌[^1889]ནི་གཉིས་པའི་ཕྱིར་ཏེ། གལ་ཏེ་དེ་གཉིས་ཀྱིས་དེ་ཡན་ཆད་རྣམ་པ་དྲུག་གམ། བདུན་ནམ་བརྒྱད་དག་ཅིག་སྔོན་སྤངས་པ་ཡིན་ན་ནི་དེ་གཉིས་འབྲས་བུ་གཉིས་པ་ལ་ཞུགས་པ༌[^1890]ཞེས་བྱ་སྟེ།

[Block 2742]
གཉིས་པ་གང་ཞེ་ན།

[Block 2743]
ལན་ཅིག་ཕྱིར་འོང་བའི་འབྲས་བུའོ། །

[Block 2744 [HEADING]]
#### འབྲས་བུ་གསུམ་པ་ལ་ཞུགས་པ། ^3-2-4-0

[Block 2745 [VERSE]]
འདོད་པའམ༌[^1891]ཡང་ན་གོང་མ་ལས། །
ཆགས་བྲལ་གསུམ་པ་ལ་ཞུགས་པ། །

[Block 2746]
གལ་ཏེ་རྣམ་པ་དགུ་པ་ཡང་སྤངས་པའི་ཕྱིར་འདོད་པའི་ཁམས་ལས་འདོད་ཆགས་དང་བྲལ་བ་ཞིག་ཡིན་ནམ། གོང་མ་ཅི་ཡང་མེད་པའི་སྐྱེ་མཆེད་ཀྱི་བར་ལས་འདོད་ཆགས་དང་བྲལ་བ་ཞིག་ཡིན་ན་དེ་གཉིས་འབྲས་བུ༌[^1892]

[Block 2747]
གསུམ་པ་ལ་ཞུགས་པ་ཞེས་བྱ་སྟེ། གསུམ༌[^1893]གང་ཞེ་ན།

[Block 2748]
ཕྱིར་མི་འོང་བའི་འབྲས་བུའོ། །

[Block 2749 [HEADING]]
#### འབྲས་བུ་ལ་གནས་པ། ^3-2-5-0

[Block 2750 [VERSE]]
གང་ཞིག་གང་ལ༌[^1894]ཞུགས་པ་ནི། །
བཅུ་དྲུག་པ་ལ་དེ་འབྲས་གནས། །

[Block 2751]
སེམས་བཅུ་དྲུག་པ་སྐྱེས་ན་དེ་གཉིས་དད་པ་དང་ཆོས་ཀྱིས༌[^1895]རྗེས་སུ་འབྲང་བ་ཞེས་ཀྱང་མི་བྱ་ལ། ཞུགས་པ་ཞེས་ཀྱང་མི་བྱའོ། །

[Block 2752]
འོ་ན་ཅི་ཞེ་ན། འབྲས་བུ་ལ་གནས་པ་དག་ཡིན་ཏེ། གང་ཞིག་རྒྱུན་དུ་ཞུགས་པའི་འབྲས་བུ་འམ། ལན་ཅིག་ཕྱིར་འོང་བའི་འབྲས་བུ་འམ། ཕྱིར་མི་འོང་བའི་འབྲས་བུ་ཡང་རུང་འབྲས་བུ་གང་ལ་ཞུགས་པར་གྱུར་པ་དེ་ནི་དེའི་ཚེ་འབྲས་བུ་དེ༌[^1896]ལ་གནས་པ་ཡིན་ནོ། །

[Block 2753]
དགྲ་བཅོམ་པ་ཉིད་ནི་དང་པོ་ཉིད་དུ་ཐོབ་པར་མི་ནུས་ཏེ། མཐོང་བའི་ལམ་གྱིས་བསྒོམ་པས་སྤང་བར་བྱ་བ་མི་སྤོང་བའི་ཕྱིར་དང་། སྔར་ཡང་སྲིད་པའི་རྩེ་མོ་ལས་འདོད་ཆགས་དང་བྲལ་བ་མི༌[^1897]སྲིད་པའི་ཕྱིར་རོ། །

[Block 2754 [HEADING]]
#### དད་པས་མོས་པ་དང་མཐོང་བས་ཐོབ་པ། ^3-2-6-0

[Block 2755 [VERSE]]
དེའི༌[^1898]ཚེ་དབང་པོ་རྣོ་རྟུལ་དག །
དད་པས་མོས་དང་མཐོང་བས་ཐོབ། །

[Block 2756]
དེའི་ཚེ་དབང་པོ་རྟུལ་པོ་སྔོན་དད་པས་རྗེས་སུ་འབྲང་བ་གང་ཡིན་པ་དེ་ནི་དད་པས་མོས་པ་ཞེས་བྱའོ། །

[Block 2757]
དབང་པོ་རྣོན་པོ་སྔོན་ཆོས་ཀྱིས༌[^1899]རྗེས་སུ་འབྲང་བ་གང་ཡིན་པ་དེ་ནི་མཐོང་བས་ཐོབ་པ་ཞེས་བྱ་སྟེ། དད་པ་དང་ཤེས་རབ་ལྷག་པས་མོས་པ་དང་མཐོང་བས་རབ་ཏུ་ཕྱེ་བའི་ཕྱིར་རོ། །

[Block 2758 [HEADING]]
#### མི་བརྩོན་པ་ནི་ཞུགས་མ་ཡིན་པ། ^3-2-7-0

[Block 2759]
ཅིའི་ཕྱིར་རྣམ་པ་ལྔ་སྤངས་ཀྱང་སེམས་བཅུ་དྲུག་པ་ལ་རྒྱུན་དུ་ཞུགས་པ་ཁོ་ན་ཞེས་བྱ་ལ།[^1900] ལན་ཅིག་ཕྱིར་འོང་བའི་འབྲས་བུ་ལ་ཞུགས་པ་ཞེས་མི་བྱ་ཞེ་ན། གང་གི་ཕྱིར།

[Block 2760 [VERSE]]
འབྲས་ཐོབ་འབྲས་བུའི༌[^1901]ཁྱད་པར་གྱིས། །
ལམ་ཐོབ་མེད་པས་དེ་ཡི་ཕྱིར། །
འབྲས་གནས་ཁྱད་པར་བྱ་བའི་ཕྱིར། །
མི་བརྩོན་པ་ནི་ཞུགས་མ་ཡིན། །

[Block 2761]
འབྲས་བུ་ཐོབ་ན་འབྲས་བུ་ཁྱད་པར་ཅན་གྱི་ལམ་མི་འཐོབ་བོ་ཞེས་བྱ་བ་འདི་ནི་ངེས་སོ། །

[Block 2762]
དེ་ལྟ་བས་ན་འབྲས་བུ་ལ་གནས་པ་ཇི་སྲིད་དུ་ཁྱད་པར་དུ་བྱ་བའི་ཕྱིར་འབྲས་བུ་གཞན་ཐོབ་པར་བྱ་བ་ལ་མི་བརྩོན་པ་དེ་སྲིད་དུ་ཞུགས་པ་ཞེས་མི་བྱ་སྟེ། དེ་བཞིན་དུ་འབྲས་བུ་གཞན་ལ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 2763]
གང་ཞིག་བསམ་གཏན་གསུམ་པ་ལས་འདོད་ཆགས་དང་བྲལ་ལ། ས་འོག་མ་ལ་བརྟེན་ཏེ་ངེས་པར་འཇུག་པ་དེ་ནི་གདོན་མི་ཟ་བར་འབྲས་བུ་ཁྱད་པར་ཅན་གྱི་ལམ་མངོན་དུ་བྱེད་དོ། །

[Block 2764]
དེ་ལྟ་མ་ཡིན་ན་དེའི་གོང་དུ་སྐྱེས་པ་དེ་བདེ་བའི་དབང་པོ་དང་མི༌[^1902]ལྡན་པར་འགྱུར་རོ། །

[Block 2765]
རེ་ཞིག་ཕལ་ཆེར་ལས་དང་འདོད་པ་ལས་འདོད་ཆགས་དང་བྲལ་བ་རྣམས་ཀྱིས་ངེས་པར་འཇུག་པའི་གང་ཟག་རྣམ་པར་གཞག་པ་ནི་དེ་ལྟ་བུ་ཡིན་ནོ། །

[Block 2766 [HEADING]]
#### མཐར་གྱིས་འཇུག་པ། ^3-2-8-0

[Block 2767]
མཐར་གྱིས་འཇུག་པ་བརྗོད་པར་བྱ་སྟེ། དེའི་ཕྱིར་རེ་ཞིག་འདི་རྣམ་པར་གཞག་པར་བྱའོ། །

[Block 2768 [HEADING]]
##### ས་དང་ས་ན་ཉེས་པ་རྣམ་པ་དགུ། ^3-2-8-1-0

[Block 2769]
ཇི་ལྟར་འདོད་པའི་ཁམས་ཀྱི་ཉོན་མོངས་པ་རྣམ་པ་དགུ་པོ་དེ་དག་བསྟན་པ་དེ་བཞིན་དུ།

[Block 2770 [VERSE]]
ས་དང་ས་ན་ཉེས་རྣམ་དགུ། །
སྲིད་པའི་རྩེ་མོའི་བར་དུའོ། །
--- END BLOCKS ---
