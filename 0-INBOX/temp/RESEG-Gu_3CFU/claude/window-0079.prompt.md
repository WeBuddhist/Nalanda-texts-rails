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
[Block 2766]
གང་དུ་ཕམ་པར་གྱུར་པ་བཞི་པ་ཞེས་བྱ་བ་ལ་ལྟོས་ནས་བརྗོད་པར་བྱ་སྟེ། དེའི་ཕྱིར་འདུ་ཤེས་བསྒྱུར་ཏེ་བདག་ཉིད་མིའི་ཆོས་བླ་མ་དང་ལྡན་པ་ཉིད་དུ་སྨྲ་ནའོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་འདི་བདེན་པར་གྱུར་པ་དང་མིང་དུ་གྱུར་པའི་དོན་བཟུང་སྟེ་བསྒྱུར་ཏེ་སྦ་བར་བྱས་ནས་འོག་ཏུ་བྱས་ཏེ་བརྫུན་པའི་དོན་གྱིས་འདུ་ཤེས་གཞན་གྱིས་བཀབ་ནས་བདག་ཉིད་མིའི་ཆོས་བླ་མ་དང་ལྡན་པ་ཉིད་དུ་བརྗོད་པ་ལ་ཅི་བདག་ཉིད་དམ་གཞན་ལ་ཞེས་བྱ་བ་ནི་བདག་ཉིད་ལའོ། །

[Block 2767]
དེ་ཉིད་མཐོང་ངོ་བདག་མཐོང་ངོ་སྒྲ་ཐོས་སོ། །

[Block 2768]
བདག་གིས་ཐོས་སོ། །

[Block 2769]
འགྲོའོ། །

[Block 2770]
བདག་གི༌[^1885]དྲུང་དུ་འོང་ངོ་། །ལྷན་ཅིག་ཏུ༌[^1886]གཏམ་འདྲེའོ། །

[Block 2771]
ཕེབས་པར་སྨྲའོ། །

[Block 2772]
སོ་སོར་ཀུན་དགའོ། །

[Block 2773]
བདག་དང་རྟག་དུ་ཡང་ལྷན་ཅིག་གནས་པར་བྱེད་དོ་ཞེས་སྨྲས་པ་འདི་ཉིད་དོ་ཞེས་བྱ་བ་མཐོང་ངོ་ཞེས་བྱ་བ་ལ། སོགས་པ་སྨྲས་པ་དེ་ཉིད་ནི་བདག་ཉིད་མིའི་ཆོས་བླ་མ་དང་ལྡན་པ་ཉིད་དུ་སྨྲ་བ་ཉིད་ཡིན་པར་བལྟ་བར་བྱའོ། །

[Block 2774]
བདག་དང་ལྷན་ཅིག་གཏམ་འདྲེའོ་ཞེས་བྱ་བ་འདིས་ནི་གཏམ་འདྲེ་བར་བྱེད། ཕེབས་པར་སྨྲ་བར་བྱེད། ཕན་ཚུན་ཀུན་དགའ་བར་བྱེད། རྟག་ཏུ་ཡང་ལྷན་ཅིག་གནས་པར་བྱེད་དོ་ཞེས་དེ་ལྟར་ཡང་སྦྱར་བར་ཤེས་པར་བྱའོ། །

[Block 2775]
ཅི་མཐོང་ངོ་། །བདག་མཐོང་ངོ་ཞེས་བྱ་བ་དེ་ཙམ་གྱི་ཚིག་ཁོ་ན་ལས་ཕམ་པར་འགྱུར་རམ། འོན་ཏེ་ཟླ་ཅུང་ཟད་ཅིག་ལ་ལྟོས་ནས་ཡིན། དེ་ལྟར་ན་ཡང་ཟླ་གང་ཡང་རུང་བ་ཞིག་ཡིན་ནམ་འོན་ཏེ་ཁྱད་པར་ཅན་ཞིག་ཡིན་ནམ༌[^1887]ཞེ་ན། །དེའི་ཕྱིར། ལྷ་དང་། ཀླུ་དང་། གནོད་སྦྱིན་དང་། དྲི་ཟ་དང་། མིའམ་ཅི་དང་། ལྟོ་འཕྱེ་ཆེན་པོ་དང་། ཡི་དགས་དང་། ཤ་ཟ་དང་། གྲུལ་བུམ་དང་། སྲུལ་པོ་དང་། ལུས་སྲུལ་པོའི་ཟླ་ཉིད་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེའི་ཕྱིར་ལྷ་རྣམས་བདག་གིས་མཐོང་ངོ་། ། ལྷ་རྣམས་ཀྱིས་བདག་མཐོང་ངོ་། །ལྷ་རྣམས་དང་ལྷན་ཅིག་བདག་གནས་སོ་ཞེས་བྱ་བ་ཉེ་བར་གནས་པ་འདི་རྣམས་ཀྱི་ཚིག་དང་ལྡན་པས་བདག་ཉིད་མིའི་ཆོས་བླ་མ་དང་ལྡན་པ་ཉིད་སྨྲ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2776]
སྦོམ་པོའི་དབང་དུ་བྱས་པ་ཉིད་ནི་དུར༌[^1888]ཁྲོད་ཀྱི་ཤ་ཟའོ་ཞེས་བྱ་བ་ནི་དུར་ཁྲོད་ཀྱི་ཤ་ཟ་བ་ལ་སོགས་པ་འགལ་བའི་ཟླ་ལ་བདག་གིས་རགས་པ༌[^1889]མཐོང་ངོ་ཞེས་བྱ་བ་འདི་ལྟ་བུ་ལ་སོགས་པ་ཚིག་རྣམས་གཞན་སོ་སོ་ཉིད་ཀྱི་ཕྱིར་འདི་ལ་དེ་ལྟར་འདི་དང་ལྷན་ཅིག་བདག་ལ་སྟོད་པར༌[^1890]བྱེད་ཅེས་བྱ་བ་འདི་ཤེས་པའོ། །

[Block 2777]
འབྲས་བུ་དང་ལྷན་ཅིག་ཏུ་མིའི་ཆོས་བླ་མ་བསྟན་པའི་ངོ་བོ་ཉིད༌[^1891]ལ་བརྗོད་པར་བྱ་སྟེ། མི་རྟག་པ་ལ་སོགས་པའི་འདུ་ཤེས་དང་། བསམ་གཏན་རྣམས་དང་། ཚད་མེད་པ་རྣམས་དང་། གཟུགས་མེད་པ་རྣམས་དང་། འབྲས་བུ་རྣམས་དང་། མངོན་པར་ཤེས་པ་ལ་སོགས་པ་ནི་ཆོས་བླ་མའོ་ཞེས་བྱ་བ་ནི་མི་རྟག་པའི་འདུ་ཤེས་དང་། མི་རྟག་པ་ལ་སྡུག་བསྔལ་བའི་འདུ་ཤེས་དང་། སྡུག་བསྔལ་བ་ལ་བདག་མེད་པའི་འདུ་ཤེས་དང་། ཟས་ལ་མི་མཐུན་པའི་འདུ་ཤེས་དང་། འཇིག་རྟེན་ཐམས་ཅད་ལ་མངོན་པར་མི་དགའ་བའི་འདུ་ཤེས་དང་། ཉེས་དམིགས་ཀྱི་འདུ་ཤེས་དང་། སྤོང་བའི་འདུ་ཤེས་དང་། འདོད་ཆགས་དང་བྲལ་བའི་འདུ་ཤེས་དང་། འགོག་པའི་འདུ་ཤེས་དང་། འཆི་བའི་འདུ་ཤེས་དང་། མི་སྡུག་པའི་འདུ་ཤེས་དང་། རྣམ་པར་བསྔོས་པའི་འདུ་ཤེས་དང་། རྣམ་པར་རྣགས༌[^1892]པའི་འདུ་ཤེས་དང་། རྣམ་པར་བམ་པའི་འདུ་ཤེས་དང་། རྣམ་པར་འབུས་གཞིགས་པའི་འདུ་ཤེས་དང་། རྣམ་པར་ཟོས་པའི་འདུ་ཤེས་དང་། རྣམ་པར་དམར་བའི་འདུ་ཤེས་དང་། རྣམ་པར་འཐོར་བའི་འདུ་ཤེས་དང་། རུས་གོང་གི་འདུ་ཤེས་དང་། སྟོང་པ་ཉིད་ལ་སོ་སོར་རྟོགས་པའི༌[^1893]འདུ་ཤེས་སོ་ཞེས་བྱ་བའི་མདོ་སྡེ་རྣམས་ལས་ཡང་དག་པར་འབྱུང་བའི་འདུ་ཤེས་རྣམས་ཉེ་བར་བསྡུ་བའི་ཕྱིར་རོ། །

[Block 2778]
མི་རྟག་པ་ལ་སོགས་པ༌[^1894]འདི་ལ་འདིར་སོགས་པའི་སྒྲ་དང་མངོན་པར་ཤེས་པ་ལ་སོགས་པ་ཞེས་བྱ་བ་འདིར་ཡང་སོགས་པའི་སྒྲས་འདི་ལྷག་མ་འདི་ལྟ་བུའི་རྣམ་པའི་ཡོན་ཏན་རྣམས་བསྡུ་བའི་དོན་དུའོ། །

[Block 2779]
སྦོམ་པོའི་དབང་དུ་བྱས་པ་ཉིད་ནི་ཞི་གནས་ཀྱི་རྒྱུ་མཚན་རང་གི་མཚན་ཉིད་འཛིན་པ་ཉོན་མོངས་པ་རྣམ་པར་གནོན་པའོ་ཞེས་བྱ་བ་ནི་མོས་པ་ཡིད་ལ་བྱེད་པའི་བདག་ཉིད་ཚད་མེད་པ་ལ་སོགས་པ་རྣམས་ལའོ། །

[Block 2780]
དེ་ཁོ་ན་ཡིད་ལ་བྱེད་པའི་བདག་ཉིད་ཅན་རྣམས་ལ་ཡང་མི་རྟག་པའི་འདུ་ཤེས་ལ་སོགས་པའི་དགེ་བའི་རྣམ་པ༌[^1895]རྣམས་ཡོངས་སུ་རྫོགས་པ་གང་ཡིན་པ་དེ་ལ་ཚུ་རོལ་གྱི་ཆ་གང་ཡིན་པ་དེ་འདིར་རང༌[^1896]གི་མཚན་ཉིད་འཛིན་པ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིག་གིས་བརྗོད་པའོ། །

[Block 2781]
ཞི་གནས་ཀྱི་དོན་ནི་ཏིང་ངེ་འཛིན་གྱི་དོན་ཏོ། །

[Block 2782]
ཡོངས་སུ་རྫོགས་པ་དང་མི་རྟག་པ་ལ་སོགས་པའི་འདུ་ཤེས་རྣམས་ལ་མི་རྟག་པ་ལ་སོགས་པའི་འདུ་ཤེས་ཉིད་ཀྱིས་བཀའི་ཚིག་གོ། །

[Block 2783]
དེ་བས་ན་ཕྱིར་མི་བཟློགས༌[^1897]པས་བསྡུས་པའི་དགེ་བའི་རྩ་བ་རྣམས་ཡོངས་སུ་རྫོགས་པ་ལུང་བསྟན་པ་ལ་ནི་ཕམ་པའོ། །

[Block 2784]
ཚུ༌[^1898]རོལ་ཉིད་ལ་ཡོངས་སུ་རྫོགས་པ་ལུང་བསྟན་པ་ནི་སྦོམ་པོའི་ལྟུང་བ་ཞེས་བྱ་བ་རྣམ་པར་གཞག་པ་རྟོགས་པར་བྱའོ། །

[Block 2785]
དེ་དང་ལྡན་པའི་ཆོས་ཅན་ཉིད་དུ་སྨྲ་བ་ནི་དེ་དང་ལྡན་པ་ཉིད་མ་སྨྲས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། དེ་དང་ལྡན་པ་ཉིད་ཀྱི་ཆོས་གང་ཡིན་པ་དེ་ལ་བརྗོད་པ་གང་ཡིན་པ་འདི་ནི་དེ་དང་ལྡན་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 2786]
དེ་བས་ན་མི་མ་ཡིན་པ་རྣམས་མི་འཚེ་བ་ཉིད་དང་། ཁྲ་བོ་བཀྲ་བ་ལ་སོགས་པ་འཐོབ་པའི་ཆོས་ཞེས་བྱ་བ་ལ་སོགས་པ། རྒྱུན་དུ་ཞུགས་པ་ལ་སོགས་པའི་ཆོས་ཉིད་ཀྱིས༌[^1899]རྣམ་པར་གནས་པ་ལ་བརྗོད་པ་གང་ཡིན་པ་དེ་ནི་རྒྱུན་དུ་ཞུགས་པ་ལ་སོགས་པ་མ་ཡིན་ཞེས་བྱ་བར་ཤེས་པར་མི་བྱ་སྟེ་བརྗོད་པ་འདི་ལ་ཕན་པ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 2787]
དེ་ཡོད་དོ་ཞེས་རང་གི་བསམ་པ་གཞན་ལ་སྦྱོར་ཞིང་སྟོན་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་ཡོད་དེ༌[^1900]གང་ཞིག་ལྷ་རྣམས་མཐོང་བ་ཞེས་བྱ་བ་ལ་སོགས་པ་གང་ཡིན་པ་བདག་ཉིད་ལ་དགོངས་ནས་འདི་ཡོད་དོ་ཞེས་བྱ་བ་བསམས་པས་ཚིག་གོ། །

[Block 2788]
གལ་ཏེ་ཡང་དེར་བདག་ཉིད་མངོན་པར་བསམས་པ་དེ་ལྟར་ན་ཡང་གཞན་ལ་སྦྱོར་བ་ཉིད་དེ་ལ་ཚིག་གི་ངོ་བོ་རང་དང་གཞན་ལ་སྦྱོར་བ་རྣམ་པར་གཞག་པ་རང་གི་བསམ་པས་གདུག་པ་ཅན་དང་གདུག་པ་ཅན་མ༌[^1901]ཡིན་པ་ཉིད་ལ་དེ་བས་ན་ཚིག་ལ་ཚིག་འདི་ལས༌[^1902]རྣམ་པར་གཞག་པ་མེད་དོ།[^1903] །དེ་བས་ན་འདིར་ཁ་ན་མ་ཐོ་བ་མ་ཡིན་པ་ཆད་པ་ལ་ཕམ་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2789]
གལ༌[^1904]ཏེ་འདི་ཡོད་ཅེས་བསམས་པ༌[^1905]རྣམས་ལ་མ་བསྟན་པ་ཡང་བདག་ཅེས་བྱ་བ་ལ་སོགས་པའི་སྒྲས་ཉེ་བར་བསྡུ་བའོ། །

[Block 2790]
འདི་ནི་བདག་ཉིད་ཅེས་བྱ་བ་ལ་སོགས་པར་འགྱུར་ན་དེའི་ཚེ་ན་ཡང་གཞན་ལ་སྦྱོར་ཞིང་ཞེས་བྱ་བ་ཅི་ཞིག་བྱ་ཞེ་ན། དེའི་ཕྱིར་ཉེ་བར་སྦྱོར་ན་མ་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རང་ལ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2791]
དགེ་སློང་འདི་ཡོད་དེ་གང་ཞིག་ལྷ་རྣམས་མཐོང་ཞེས་བྱ་བ་འདི་ལ་གལ་ཏེ་རང་གི་སྟོན་པའི་སྒྲ་ལ་བདག་ཉིད་འདི་ཡིན་ཞེས་བྱ་བ་བསམ་པར་བྱེད་ན་དེ་བས་ན་གཞན་གྱི་བསྟན་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 2792]
རང་བསྟན་པ་ཉིད་ཀྱིས་དེར་ལྟུང་བ་ཡོངས་སུ་རྫོགས་པ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 2793]
དེ་ལྟར་ཡང་གཞུང་ནི་འདི་སྐད་ཅེས་ང་ཉིད་དོ་ཞེས་མི་སྨྲ་ན་ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 2794]
མ་བསམས་པར་བསྟན་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་བསླུ་བའི་བློས་ཡིད་ཆེས་དང་བྲལ་བའི་ཚིག་གིས་གླགས་མི་རྙེད་པ་དེ་བཞིན་དུ། སོ་སོར་བརྟགས་པ༌[^1906]མ་བྱས་པར་ལུང་བསྟན་པར་མི་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2795]
ཕམ་པར་འགྱུར་བ་བཞི་པ་རྣམ་པར་འབྱེད་པའི་སྐབས་སོ།། །།

[Block 2796]
བླ་མ་ཐོབ་པ་ཡོངས་སུ་ཉམས་པ་གོ་བར་བྱེད་པ་ནི་མ་བརྗོད་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་བདག་ཉིད་དམན་པ་སྟེ། བདག་ནི་དགེ་སྦྱོང་གི་འབྲས་བུ་བཞི་ལས་ཉམས་པའོ་ཞེས་བྱ་བ་ལ་སོགས་པས་ཐོབ་པ་ལས་ཡོངས་སུ་ཉམས་པ་ལས་བསྟན་པ་གང་ཡིན་པ་དེ་ཡང་མིའི་ཆོས་བླ་མ་མ་བརྗོད་པ་མ་ཡིན་ཏེ་བརྗོད་པ་ཁོ་ན་ཉིད་ཡིན་པས། འདིར་གལ་ཏེ་བརྫུན་དུ་སྨྲ་བ་ཉིད་ཡོད་པར་གྱུར་པ་ལ་ཕམ་པར་མི༌[^1907]འགྱུར་བ་མ་ཡིན་ཏེ། ཕམ་པར་འགྱུར་བ་ཁོ་ན་ཡིན་ནོ། །

[Block 2797]
མ་ཐོབ་པ་ལ་ཉམས་པ་གང་ཞིག་བསྟན་པ་དེ་གལ་ཏེ་སྐྱོན་དང་བཅས་ན་ཁྱད་པར་སུ་ཞིག་སྲིད་པའི་འདུན་པས་ཡང་དག་པར་མཚོན་པ་ཉིད་དེ་ལ་རིག་པར་བྱའོ། །

[Block 2798]
སླར་གང་ཞིག་སྐྱོན་དང་བྲལ་བ་དེ་ལ་སྐྱོན་དང་བྲལ་བ་ཉིད་དོ། །

[Block 2799]
བླ་མ་བརྗོད་པའི་འདུན་པས་མིང་མཐུན་པའི་དོན་བརྗོད་ན་སྦོམ་པོའོ་ཞེས་བྱ་བ་ནི་མིང་འདྲ་བའི་དོན་བརྗོད་པ་ནི་མིང་དང་མཐུན་པའི་དོན་བརྗོད་པའོ། །

[Block 2800]
བདག་སློབ་པ་ཞེས་བྱ་བ་སོ་སོར་ཐར་པའི་སྡོམ་པ་ལ་སོགས་པ་ལ་སློབ་པའོ། །

[Block 2801]
བདག་ནི་མི་སློབ་ཅེས་བྱ་བ་བསྟན་པ་དང་། འདུལ་བ་དང་སོ་སོར་ཐར་པའི་མདོ་ལ་སོགས་པ་དང་། ཆོས་མངོན་པ་ལ་སོགས་པ་སློབ་པ་ཉིད་དང་མི་བརྩོན་པ་ཉིད་ལྷུང་བཟེད་ལ་སོགས་པ་ལས་ལྷག་མ༌[^1908]མེད་པ་དང་། བདག་ལ་ཅིའང་མེད་དོ་ཞེས་བྱ་བ་སྐྱེ་བའི༌[^1909]ཐ་མ་བཟློག་པ་ཉིད་ཅེས་བྱ་བའོ། །

[Block 2802]
གྲུར་འགྲོ་བ་དག་ལ་རྒྱུན་དུ་ཞུགས་པའི་འབྲས་བུ་ཞེས་བྱ་བ་བསྟན་པ་ཉིད་དེར་འབྲས་བུ་འདི་ལ་མེ་ཏོག་ལ་སོགས་པ་བདག་ཉིད་ཀྱིས་བཟུང་ནས་འབྲས་བུ་ཐོབ་པོ་ཞེས་བྱ་བ་དང་། ཁྱོད་ནི་ཟག་པ་མེད་དོ་ཞེས་བྱ་བ་ལ་སོགས་པས་འདྲི་བའི་བདག་ཉིད་ལ་བདག་ལ་འཚོ་བ་ལ་སོགས་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་འདི་འདས་པའོ། །

[Block 2803]
འཚོ་བའི་འཇིགས་པ༌[^1910]ལས་བདག་ནི་འཇིགས་པ༌[^1911]མ་ཡིན་ཞེས་བྱ་བ་དང་བདག་ནི་ཀུན་ཏུ་སྦྱོར་བ་ལ་སོགས་པ་ལས་གྲོལ་ལོ་ཞེས་བྱ་བའི་མིང་དང་བཅས་པའི་དོན་ལ་དགོངས་ནས་བླ་མའི་མིང་དང་འདྲ་བའི་མིང་དེ་ལ་བླ་མ་བསྟན་པའི་འདུན་པས་བརྗོད་པ་ལ་སྦོམ་པོའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2804]
གཞན་གྱིས༌[^1912]ཐོས་པ་ལ་ཡོད་པར་འགྱུར་བ་འདི་རྟོགས་པར་བྱའོ། །

[Block 2805]
ནོར་ན་ཡང་ངོ་ཞེས་བྱ་བ་ནི་བརྗོད་པ་ཞེས་བྱ་བ་དང་སྦྱར་རོ། །
--- END BLOCKS ---
