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
[Block 701 [HEADING]]
#### མཐོང་བས་སྤང་བར་བྱ་བ་ལ་སོགས་པ། ^1-3-17-0

[Block 702]
མཐོང་བས་སྤང་བར་བྱ་བའི་ཁམས་རྣམས་ནི་དུ། བསྒོམས་པས༌[^292]སྤང་བར་བྱ་བ་རྣམས་ནི་དུ། སྤང་བར་བྱ་བ་མ་ཡིན་པ་རྣམས་ནི་དུ་ཞེ་ན། རེ་ཞིག་གཟུགས་ཅན་བཅུ་ནི་བསྒོམས་པས༌[^293]སྤང་བྱ་ཡིན། ལྔ་ཡང་ཡིན་ཏེ་རྣམ་པར་ཤེས་པའི་ཁམས་ལྔ་པོ་དག་གོ། །

[Block 703]
ཐ་མའི༌[^294]གསུམ་རྣམ་གསུམ། ཡིད་ཀྱི་ཁམས་དང་། ཆོས་ཀྱི་ཁམས་དང་། ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་ཁམས་དང་ཁམས་གསུམ་པོ༌[^295]འདི་དག་ནི་རྣམ་པ་གསུམ་པོ་འདི་དག༌[^296]སྟེ། ཕྲ་རྒྱས་བརྒྱད་ཅུ་རྩ་བརྒྱད་དང་། །དེ་དག་དང་ལྷན་ཅིག་འབྱུང་བ་དང་། དེ་དག་གི་ཐོབ་པ་རྗེས་སུ་འབྲང་བ་དང་བཅས་པ་རྣམས་ནི་མཐོང་བས་སྤང་བར་བྱ་བ་དག་ཡིན་ནོ། །

[Block 704]
ཟག་པ་དང་བཅས་པ་ལྷག་མ་རྣམས་ནི་བསྒོམས་པས༌[^297]སྤང་བར་བྱ་བ་དག་ཡིན་ནོ། །

[Block 705]
ཟག་པ་མེད་པ་རྣམས་ནི་སྤང་བར་བྱ་བ་མ་ཡིན་པ་དག་གོ། །

[Block 706]
སོ་སོའི་སྐྱེ་བོ་ཉིད་དང་། ངན་སོང་བའི་ལུས་དང་ངག་གི་ལས་ཀྱང་འཕགས་པའི་ལམ་དང་འགལ་བའི་ཕྱིར་མཐོང་བས་སྤང་བར་བྱ་བ་གཞན་ཡང་ཡོད་པ་མ་ཡིན་ནམ་ཞེ་ན། དེ་དག་ནི་མཐོང་བས་སྤང་བར་བྱ་བ་མ་ཡིན་ཏེ།

[Block 707 [VERSE]]
མདོར་བསྡུ་བ་ནི་འདི་ཡིན་ནོ། །
ཉོན་མོངས་ཅན་མིན་མཐོང་སྤང་མིན། །
གཟུགས་མིན་དྲུག་པ་མིན་སྐྱེས་མིན། །

[Block 708]
ཉོན་མོངས་པ་ཅན་མ་ཡིན་པ་ནི་མཐོང་བས་སྤང་བར་བྱ་བ་ཅུང་ཟད་ཀྱང་མེད་ལ་གཟུགས་ཀྱང་མ་ཡིན་ནོ། །

[Block 709]
སོ་སོའི་སྐྱེ་བོ་ཉིད་ནི་ཉོན་མོངས་པ་ཅན་མ་ཡིན་པའི་ལུང་དུ་མ་བསྟན་པ་ཡིན་ཏེ། དགེ་བའི་རྩ་བ་ཀུན་ཏུ་ཆད་པ་དང་། འདོད་ཆགས་དང་བྲལ་བ་རྣམས་ཀྱང་དེ་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 710]
ལུས་དང་ངག་གི་ལས་ནི་གཟུགས་ཡིན་ནོ། །

[Block 711]
དེ་ལྟ་བས་ན་དེ་དག་ནི་མཐོང་བས་སྤང་བར་བྱ་བ་མ་ཡིན་ཏེ། བདེན་པ་དག་ལ་ལོག་པར་མི་རྟོག་པའི་ཕྱིར་དང་། སྡུག་བསྔལ་ལ་ཆོས་ཤེས་པའི་བཟོད་པ་ན་སོ་སོའི་སྐྱེ་བོ་ཉིད་དུ་ཐལ་བར་འགྱུར་བའི་ཡང་ཕྱིར་རོ། །

[Block 712]
དྲུག་པ་ལས་མ་སྐྱེས་པ་ཡང་མ་ཡིན་ཏེ།

[Block 713]
དྲུག་པ་ཞེས་བྱ་བ་ནི་ཡིད་ཀྱི་སྐྱེ་མཆེད་དོ། །

[Block 714]
དེ་ལས་གཞན་པ་ལས་སྐྱེས་པ་ནི་དྲུག་པ་ལས་མ་སྐྱེས་པ་སྟེ། དབང་པོ་ལྔ་ལས་སྐྱེས་པ་གང་ཡིན་པ་སྟེ། དེ་ཡང་མཐོང་བས་སྤང་བར་བྱ་བ་ནི་མེད་དོ། །

[Block 715 [HEADING]]
#### ལྟ་བ་དང་ལྟ་བ་མ་ཡིན་པ། ^1-3-18-0

[Block 716 [HEADING]]
##### ལྟ་བ་རྣམ་པ་བརྒྱད། ^1-3-18-1-0

[Block 717]
ཁམས་བཅོ་བརྒྱད་པོ་དག་ལས་ལྟ་བ་ནི་དུ། ལྟ་བ་མ་ཡིན་པ་ནི་དུ་ཞེ་ན། མིག་དང་ཆོས་ཀྱི་ཁམས་ཕྱོགས་ནི། ལྟ་བ་ཡིན་ཏེ། དེ་གང་ཞེ་ན། སྨྲས་པ། རྣམ་པ་བརྒྱད། འཇིག་ཚོགས་ལ་ལྟ་བ་ལ་སོགས་པ་ལ༌[^298]ལྟ་བ་ལྔ་དག་དང་། འཇིག་རྟེན་པའི་ཡང་དག་པའི་ལྟ་བ་དང་། སློབ་པའི་ལྟ་བ་དང་། མི་སློབ་པའི་ལྟ་བ་སྟེ། ཆོས་ཀྱི་ཁམས་རྣམ་པ་བརྒྱད་པོ་འདི་དག་ནི་ལྟ་བ་ཡིན་ནོ། །

[Block 718]
ལྷག་མ་ནི་ལྟ་བ་མ་ཡིན་ནོ། །

[Block 719]
དེ་ལ་འཇིག་ཚོགས་ལ་ལྟ་བ་ལ་སོགས་པ་ནི་ཕྲ་རྒྱས་བསྟན་པར་སྟོན་པའི་དུས་ལ་འབབ་པར་འགྱུར་རོ། །

[Block 720]
འཇིག་རྟེན་པའི་ཡང་དག་པའི་ལྟ་བ་ནི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་དང་མཚུངས་པར་ལྡན་པའི་ཤེས་རབ་དགེ་བ་ཟག་པ་དང་བཅས་པའོ། །

[Block 721]
སློབ་པའི་ཟག་པ་མེད་པའི་ལྟ་བ་ནི་སློབ་པའི་འོ། །

[Block 722]
མི་སློབ་པ༌[^299]ནི་མི་སློབ་པའི་འོ། །

[Block 723]
སྤྲིན་དང་བཅས་པ་དང་སྤྲིན་མེད་པའི་མཚན་མོ་དང་ཉིན་མོ་གཟུགས་ལ༌[^300]ལྟ་བ༌[^301]བཞིན་དུ་འཇིག་རྟེན་པ་ཉོན་མོངས་པ་ཅན་དང་ཉོན་མོངས་པ་ཅན་མ་ཡིན་པ་དང་། སློབ་པ་དང་མི་སློབ་པའི་ལྟ་བ་དག་གིས་ཆོས་ལ་ལྟ་བའོ།[^302] །ཡང་ཅིའི་ཕྱིར་ཡིད་ཀྱི༌[^303]རྣམ་པར་ཤེས་པ་དང་མཚུངས་པར་ལྡན་པ་ཁོ་ན་ལ་འཇིག་རྟེན་པའི་ཡང་དག་པའི་ལྟ་བ་ཞེས་བྱ་ཞེ་ན། འདི་ལྟར།

[Block 724 [VERSE]]
རྣམ་ཤེས་ལྔ་དང་མཚུངས་སྐྱེས་བློ། །
ངེས་རྟོག་མེད་ཕྱིར་ལྟ་མ་ཡིན། །

[Block 725]
རྟོག་པར་བྱེད་པ་ནི་ལྟ་བ་ཡིན་ཏེ། ངེས་པར་སེམས་པ་ལ་ཞུགས་པ་དག་ལྟ་བ་ཡིན་ན་རྣམ་པར་ཤེས་པ་ལྔ་དང་ལྷན་ཅིག་སྐྱེས་པའི་ཤེས་རབ་ནི་དེ་ལྟ་མ་ཡིན་ཏེ། དེ་ལྟ་བས་ན་འདི་ནི་ལྟ་བ་མ་ཡིན་ནོ། །

[Block 726]
དེ་ཉིད་ཀྱི་ཕྱིར་ཤེས་རབ་ཉོན་མོངས་པ་ཅན་ནམ་ཉོན་མོངས་པ་ཅན་མ་ཡིན་པ་གཞན་ཡང་ལྟ་བ་མ་ཡིན་ནོ། །

[Block 727 [HEADING]]
##### མིག་གིས་མཐོང་བ། ^1-3-18-2-0

[Block 728]
འོ་ན་ནི་མིག་ཀྱང་རྟོག་པར་བྱེད་པ་ཉིད་མེད་ན། ཇི་ལྟར་ལྟ་བ་ཡིན་ཞེ་ན། གཟུགས་ལ་ལྟ་བའི་དོན་གྱིས་ཏེ། གང་གི་ཕྱིར། མིག་གིས་གཟུགས་རྣམས་མཐོང་། གལ་ཏེ་མིག་གིས་མཐོང་བར་གྱུར་ན། རྣམ་པར་ཤེས་པ་གཞན་དང་ལྡན་པས་ཀྱང་མཐོང་བར་འགྱུར་རོ་ཞེ་ན། མིག་ཐམས་ཅད་ཀྱིས༌[^304]མཐོང་བ་ནི་མ་ཡིན་པ་ཉིད་དོ། །

[Block 729]
འོ་ན་ཅི་ཞེ་ན། བརྟེན༌[^305]བཅས། གང་གི་ཚེ་རྣམ་པར་ཤེས་པ་དང་བཅས་པ་དེའི་ཚེ་མཐོང་གི་གཞན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 730]
དེ་ལྟ་ན་འོ་ན་ནི་མིག་ལ་བརྟེན་པའི་རྣམ་པར་ཤེས་པ་དེ་ཁོ་ནས་མཐོང་བར་འགྱུར་རོ༌[^306]ཞེ་ན། དེ་ལ་བརྟེན་པའི་རྣམ་པར་ཤེས་པས་མཐོང་ངོ་ཞེས་ངེས་པར་བྱ་བར་ནུས་པ་ནི་མིན༌[^307]ནོ། །ཅིའི་ཕྱིར་ཞེ་ན།

[Block 731 [VERSE]]
གང་ཕྱིར་བར་དུ་ཆོད་པ་ཡི། །
གཟུགས་ནི་མཐོང་བ་མིན་ཕྱིར་ལོ། །

[Block 732]
གང་གི་ཕྱིར་རྩིག་པ་ལ་སོགས་པས་བར་དུ༌[^308]ཆོད་པའི་གཟུགས་མི་མཐོང་ངོ་ཞེས་གྲག་གོ། །

[Block 733]
གལ་ཏེ་རྣམ་པར་ཤེས་པས་མཐོང་བར་གྱུར་ན་དེ་ནི་ཐོགས་པ་མེད་པའི་ཕྱིར་རྩིག་པ་ལ་སོགས་པ་ལ་ཡང་ཐོགས་པ་མེད་པས་གཟུགས་བསྒྲིབས་པ་ལ༌[^309]ཡང་མཐོང་བར་འགྱུར་རོ། །

[Block 734]
བསྒྲིབས་པ་ལ་ནི་མིག་གི་རྣམ་པར་ཤེས་པ་མི་སྐྱེ་བ་ཉིད་དེ། དེ་བས་ན་མ་སྐྱེས་པས་ཇི་ལྟར་མཐོང་བར་འགྱུར། ཅི་སྟེ་མི་སྐྱེ། གང་གི་ལྟར་ན་མིག་གིས་མཐོང་བ་དེའི་ལྟར་ན་ནི་མིག་ཐོགས་པ་དང་བཅས་པའི་ཕྱིར༌[^310]བསྒྲིབས་པ་ལ་འཇུག་པ་མེད་པས་རྣམ་པར་ཤེས་པ༌[^311]ཡང་རྟེན་དང་ལྷན་ཅིག་ཏུ་ཡུལ་གཅིག་ལ་འཇུག་པའི་ཕྱིར་མི་སྐྱེ་བར་མི་རུང་ངོ་། །མིག་ཀྱང་ལུས་ཀྱི་དབང་པོ་བཞིན་དུ་ཡུལ་དེ་ཕྲད་པ་ཞིག་ཡིན་ནམ་ཅི་ན། འདི་ལྟར་ཐོགས་པ་དང་བཅས་པའི་ཕྱིར་བསྒྲིབས་པ་མི་མཐོང་མཆིང་བུ་དང་། ལྷང་ཚེར་དང་ཤེལ་དང་ཆུ་དག་གིས་བར་དུ་ཆོད་པ་ཡང་ཇི་ལྟར་མཐོང་བར་འགྱུར་ཏེ། དེ་ལྟ་བས་ན་མིག་ཐོགས་པ་དང་བཅས་པའི་ཕྱིར་གཟུགས་བསྒྲིབས་པ་མི་མཐོང་བ་ནི་མ་ཡིན་ནོ། །

[Block 735]
འོ་ན་ཇི་ལྟ་ཞེ་ན། གང་ལ་སྣང་བ་ལ་གེགས་མེད་ན་གཟུགས་བསྒྲིབས་བཞིན་དུ་ཡང་དེ་ལ་མིག་གི་རྣམ་པར་ཤེས་པ་སྐྱེ་བ་ཉིད་ཡིན༌[^312]ལ།

[Block 736]
གང་ལ་གེགས༌[^313]ཡོད་པ་དེ་ནི་མི་སྐྱེ་བས་མ་སྐྱེས་པའི་ཕྱིར་བསྒྲིབས་པ་མི་མཐོང་ངོ་། །འོ་ན་གང་མདོ་ལས།

[Block 737]
གང་མིག་གིས་གཟུགས་རྣམས་མཐོང་ནས་ཞེས་གསུངས་སོ། །

[Block 738]
དེར་ནི་དགོངས་པ་ནི་དེ་ལ་བརྟེན་ཏེ་ཞེས་བྱ་བ་འདི་ཡིན་ཏེ། དཔེར་ན་ཡིད་ཀྱིས་ཆོས་རྣམས་རྣམ་པར་ཤེས་པར་བྱས་ནས་ཞེས་གསུངས་པ་ལྟ་བུའོ། །

[Block 739 [VERSE]]
ཡིད་ནི་འདས་པ་ཡིན་པའི་ཕྱིར། །
ཆོས་རྣམས་རྣམ་པར་མི་ཤེས་སོ། །
འོ་ན་ཅི་ལྟར༌[^314]ཞེ་ན།
ཡིད་ཀྱི་རྣམ་པར་ཤེས་པས་སོ། །

[Block 740]
ཡང་ན་བརྟེན་པའི་ལས་བརྟེན་ལ་ཉེ་བར་བཏགས་པ་ཡིན་ཏེ། དཔེར་ན་ཁྲིའུ༌[^315]དག་འབོད་དོ་ཞེས་གསུངས་པ་ལྟ་བུའོ། །
--- END BLOCKS ---
