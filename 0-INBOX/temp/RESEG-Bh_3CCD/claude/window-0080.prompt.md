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
[Block 2801]
སྐལ་བ་དང་ལྡན་པའི་ཕྱིར་ཞེས་པ་ནི། ཇི་སྐད་དུ།

[Block 2802 [VERSE]]
དབང་ཕྱུག་མ་ལུས་པ་ཉིད་དང་། །
ཡེ་ཤེས་དང་ནི་གྲགས་པ་དཔལ། །
ཆགས་བྲལ་རྩོལ་བ་ཉིད་དང་ནི། །
བཅོམ་པ་རྣམ་པ་དྲུག༌[^1832]ཏུ་གྲགས། །

[Block 2803]
ཞེས་འབྱུང་བས་སོ། །

[Block 2804]
དེ་རྣམས་དང་ལྡན་པའི་ཕྱིར་ན་བཅོམ་ལྡན་འདས་སོ། །

[Block 2805]
མི་མཐུན་པ་ལ་རྣམ་པ་གཉིས་ཏེ། ཕྱི་དང་ནང་གི་དག་གོ། །

[Block 2806]
དེ་ལ་ཕྱིའི་ནི་ལྷའི་བུ་ལ་སོགས་པའི་བདུད་རྣམས་ཀྱིའོ། །

[Block 2807]
དེ་རྣམས་རྡོ་རྗེ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་གྱིས་བཅོམ་པའི་ཕྱིར་ན་བཅོམ་ལྡན་འདས་སོ། །

[Block 2808]
ནང་གི་ནི་ཉོན་མོངས་པ་དང་ཤེས་བྱ་དང་ལས་དང་རྣམ་པར་སྨིན་པའི་སྒྲིབ་པ་ཞེས་བྱ་བ་དེ༌[^1833]རྣམས་མཐོང་བ་དང་། བསྒོམ་པ༌[^1834]ལ་སོགས་པའི་རིམ་གྱིས་བཅོམ་པས་ན་བཅོམ་ལྡན་འདས་སོ། །

[Block 2809]
རབ་ཏུ་བྱེད་པ་ལས་ཀྱང་།

[Block 2810 [VERSE]]
སྐྱ་རེངས་འཆར་བའི་དུས་སུ་ནི། །
རྡོ་རྗེ་ལྟ་བུའི་ཏིང་འཛིན་གྱིས།[^1835] །
བྱང་ཆུབ་ཤིང་དྲུང་བཞུགས་ནས་ནི། །
དེས་ནི་བདུད་རྣམས་འཇོམས་པར་མཛད། །

[Block 2811]
ཅེས་འབྱུང་ངོ་། །

[Block 2812 [VERSE]]
ཇི་སྲིད་ཡིད་ནི་གཡོ་འགྱུར་བས།[^1836] །
དེ་སྲིད་བདུད་ཀྱི་སྤྱོད་ཡུལ་ཡིན། །
དེ་ལྟར་ཡོད་པས་སྐྱོན་མེད་ནི། །
འདི་ནི་ཅི་ཕྱིར་རིགས་པ་མིན། །

[Block 2813]
ཞེས་འབྱུང་ངོ་། །ཀྱང་གི་སྒྲས་ནི་མ་བཤད་པ་བསྡུ་བའི་དོན་ཡིན་ཏེ། དེ་ནས་བཅོམ་ནི་ཆོས་འབྱུང་བའི་ནང་དུ་བདེ་བ་ཆེན་པོའི་ཚུལ་ལམ་ཐིག་ལེའི་གཟུགས་སུ་གནས་པའི་ཕྱིར་རོ། །

[Block 2814]
བཅོམ་ལྡན་འདས་ཞེས་སྤྱིའི་དོན་གྱི་ཕྱོགས་སུ་འཆད་པར་འགྱུར་རོ། །

[Block 2815]
དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཅེས་བྱ་བ་ལ་སོགས་པས༌[^1837]ནི་གནས་ཕུན་སུམ་ཚོགས་པ་བསྟན་པ་ཡིན་ཏེ་ཞེས་པ་ནི་བཅོམ་ལྡན་འདས་གང་དུ༌[^1838]བཞུགས་ཞེས་འདྲི་བ་ལ། རྒྱུད་གང་དུ་བཤད་པར༌[^1839]དེར་བཞུགས་ཞེས་ལན་ནོ། །

[Block 2816]
དེ་བཞིན་ཉིད་དུ་གཤེགས་པས་ན་དེ་བཞིན་གཤེགས་པའོ་ཞེས་པ་ནི་འོད་གསལ་བ་ལ་འཇུག་པའམ་མཁྱེན་པའོ། །

[Block 2817]
དེ་བཞིན་གཤེགས་པ་ཡང་ཡིན་ལ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་རྡོ་རྗེ་འཆང་ཆེན་པོ་སྣོད་དང་བཅུད་ཀྱི་འཇིག་རྟེན་གཉིས་ཀྱི་ངོ་བོ༌[^1840]ཡིན་པའི་ཕྱིར་རོ། །

[Block 2818]
མགོན་པོ་སེམས་ཅན་ཀུན་བདག་ཉིད། །ཅེས་རབ་ཏུ་བྱེད་པ་ལས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 2819]
དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་སྐུ་དང་གསུང་དང་ཐུགས་ཀྱི་སྙིང་པོ་སྟེ། རྡོ་རྗེ་འཆང་ཆེན་པོ་ཞེས་པ་ནི་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱིས་ཡོངས་སུ་རྫོགས་པའི་ཕྱིར་རོ། །

[Block 2820]
གང་གི་ཕྱིར་རིགས་ལྔ་ཕུང་པོ་ལྔ་རྣམ་པར་དག་པར༌[^1841]གསུངས་ཏེ། དེ་དག་ཁོ་ན་སྐུ་དང་གསུང་དང་ཐུགས་ཀྱི་དབྱེ་བས་གསུམ་དུ་འགྱུར་རོ། །

[Block 2821]
དེ་རྣམས་ཀྱང་འོད་གསལ་བ་ལ་ཉེ་བར་བསྡུས་པས༌[^1842]རྡོ་རྗེ་སེམས་དཔའི་རིགས་གཅིག་པོ་ཁོ་ནར་འགྱུར་རོ། །

[Block 2822]
དེ་བས་རྡོ་རྗེ་འཆང་ཆེན་པོ་ཞེས་གསུངས་ཏེ། ཤེས་པ་དང་ཤེས་བྱའི་རྣམ་པར་དག་པའི་སྤྲོས་པ་ལས་ངེས་པར་གྲོལ་བ་ཐམས་ཅད་སྟོང་པའི་ངོ་བོ་ཉིད་དཔལ་རྡོ་རྗེ་སེམས་དཔའ༌[^1843]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2823]
དེའི་རྡོ་རྗེ་བཙུན་མོ་ནི་ཤེས་རབ་སྟེ་ཞེས་པ་ལ་འོད་གསལ་བའི་དེ་ཁོ་ཉིད་མངོན་དུ་བྱེད་པ་རྣལ་འབྱོར་གྱི་མངོན་སུམ་གྱི་ཚད་མས་ཡང་དག་པར་རྟོགས་པར་བྱ་བ་བསྒོམ་པའི་རང་བཞིན་གྱི་ཤེས་རབ་སྟེ་སྟོང་པ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 2824]
དེ་ཉིད་ཉོན་མོངས་པ་རྣམས་འཇོམས་པས་ན་བྷ་གའོ་ཞེས་པ་ནི་ཡེ་ཤེས་གསུམ་དང་དེ་དང་འབྲེལ་པའི་ཆགས་བྲལ་ལ་སོགས་པའི་རང་བཞིན་བརྒྱ་དྲུག་ཅུ་ནི་ཉོན་མོངས་པ་རྣམས་སོ། །

[Block 2825]
དེ་རྣམས་སྔགས་དང་ཕྱག་རྒྱའི་རིམ་པས་བཅོམ་ཞིང་རྣམ་པར་དག་པས་ན་བྷ་ག་ཞེས་བཤད་དོ། །

[Block 2826]
འདི་སྐད་སྟོན་པ་ཡིན་ཏེ་ཞེས་པ་འདིས་ཉེ་བར་སྡུད་པ༌[^1844]བསྟན་ཏོ། །

[Block 2827]
དེ་བཞིན་ཉིད་ཅེས་བྱ་བ་ལ་སོགས་པ་འདིས་བགེགས་བསྐྲད་པར་བྱས་ནས་ཆོས་ཀྱི་དབྱིངས་ཀྱི་ཤེས་ཀྱི་ངོ༌[^1845]བོ་ཉིད་སྟོང་པ་ཉིད་བསྒོམས་ཏེ། སླར་ཡང་དེ་བཞིན་གཤེགས་པ་ལྔའི་རང་བཞིན་ཡེ་ཤེས་ཀྱིས༌[^1846]ས་གཞི་བྱིན་གྱིས་བརླབས་ལ། དེའི་སྟེང་དུ་རི་རབ་ཡོངས་སུ་གྱུར་པའི་གཞལ་ཡས་ཁང་པའི་ནང་དུ་མྱུར་དུ་ལྷག་པར་མོས་པའི་དཀྱིལ་འཁོར་རྣམ་པར་བསམས༌[^1847]ལ། རྡོ་རྗེ་ཕྲེང་བ་ལས་གསུངས་པའི་རིམ་པས་དོན་དམ་པའི་དཀྱིལ་འཁོར་ལ་དམིགས་ཤིང་སྟོང་པ་ཉིད་ཀྱི༌[^1848]སྔགས་མངོན་དུ་བྱས་ཏེ། ཡི་གེ་གསུམ་སྤྲོ་བ་དང་བསྡུ་བའི་རིམ་པས་པདྨ་དང་ཟླ་བ་དང་ཉི་མ་བསམས་ལ་སླར་ཡང་དེའི་སྟེང་དུ་ཡི་གེ་གསུམ་བཀོད་ལ། དེ་ཡོངས་སུ་གྱུར་པའི་ཟླ་བའི་དཀྱིལ་འཁོར་དུ་སྔར་བཤད་པའི་ཉི་མ་ལ་སོགས་པ་དེ་ཉིད་དུ་འཇུག་པར༌[^1849]བྱས་ལ། ཆོས་ཀྱི་དབྱིངས་ཞེས་བྱ་བའི་སྔགས་བརྗོད་པ་སྔོན་དུ་འགྲོ་བས་རང་གི་སེམས་བརྟན་པར༌[^1850]བྱས་ལ། སླར་ཡང་ཟླ་བ་དེ་ལ་ཡི་གེ་གསུམ་བཀོད་ཅིང་དེ་ཉིད་ལས་སྤྲོ་བ་དང་བསྡུ་བའི་རིམ་པས་རྡོ་རྗེ་དཀར་པོ་རྩེ་ལྔ་པ་ས་བོན་དང་བཅས་པར་བསམས་ལ། དེ་ཡོངས་སུ་གྱུར་པ་ལས་བཅོམ་ལྡན་འདས་རྡོ་རྗེ་སེམས་དཔའ་བསྐྱེད་ལ་དེའི་ཐུགས་ཀར་ཡེ་ཤེས་སེམས་དཔའ་དེའི་ཐུགས་ཀར་ཏིང་ངེ་འཛིན་སེམས་དཔའ་རྣམ་པར་བསྒོམས་ཏེ། མིག་ལ་སོགས་པའི་དབང་པོ་རྣམས་ལ་བྱང་ཆུབ་སེམས་དཔའི་ས་བོན་རྣམ་པར་དགོད་པའི་མཚན་ཉིད་ཅན་ཤིན་ཏུ་རྣལ་འབྱོར་རྫོགས་པར་བྱས་ལ། སྐུ་གསུང་ཐུགས་ཀྱི་བྱིན་གྱིས་རློབ་པའི་མཚན་ཉིད་ཅན་རྣལ་འབྱོར་ཆེན་པོ་ཡོངས་སུ་རྫོགས་པར་བྱས་པ་དང་། པདྨ་དང་ཟླ་བའི་དཀྱིལ་འཁོར་གྱི་སྟེང་དུ་ཞལ་གསུམ་ལ་སོགས་པའི་རྣམ་པ་ཅན་རྡོ་རྗེ་འཆང་ཆེན་པོས་རྒྱུད་གསུངས་སོ་ཞེས་དགོངས་སོ། །

[Block 2828]
ཡི་གེའི་དོན་ཏེ་ཞེས་པ་ནི་བསྐྱེད་པའི་རིམ་པ་སྟོན་པ་ལ་དང་པོའི་སྦྱོར་བ༌[^1851]ཙམ་ཚིག་གི་སྦྱོར་བས་སྟོན་པ་དང་སྒྲ་ལ་རྣམ་པར་ཞེན་པ་རྣམས་ལ་འདི་སྐད་ཅེས་བྱ་བ་ལ་སོགས་པ་རྣམས་སུ་བྱ་བ་དང་བྱེད་པ་དང་བསྡུ་བ་ལ་སོགས་པ་བཤད་པའི་ཕྱིར་རོ། །

[Block 2829]
ཚོགས་པ་ལ་བཤད་པའི་ཞེས་པ་ནི་ཡན་ལག་ལྔ་དང་ལྡན་པ་དེའི་ཡང་གཅིག་གིས་ཀྱང་ཐ་སྙད་དུ་རིགས་ཏེ། ཚིག་རྣམས་ལ་ཚིག་གི་ཕྱོགས་གཅིག་ཡོད་དོ་ཞེས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 2830]
དཔེར་ན་ཡུལ་ཚིག་པ་དང་སྣམ་བུ་ཚིག་པ་བཞིན་ནོ། །

[Block 2831]
ད་ནི་སྤྱིའི་དོན་གྱི་སྐབས་ལ་དང་པོ་རྒོལ་བ་དང་ལན་གྱི་སྒོ་ནས་སོ་སོར་བསྟན་པར་བྱ་བའི་ཕྱིར། འདིར་སྨྲས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨྲས༌[^1852]སོ། །

[Block 2832]
དགོངས་པ་གང་གིས་ན་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་དགོངས་པ་ནི་འདི་ཡིན་ཏེ། འདས་པ་དང་ད་ལྟར་བྱུང་བ་དག་རྗོད་པར༌[^1853]བྱེད་པ་དེ་དང་འདིར་ཞེས་སྒྲ་གཉིས་པོ་ཡོད་ན་འདི་སྐད་ཅེས་བྱ་བའི་ཚིག་གི་ཕྲད་ཅིའི་ཕྱིར་གཟུང་ཞེ་ན། སྨྲས་པ་ཞེས་བྱ་བ་འདིས་ལན་ཡིན་ནོ། །

[Block 2833]
དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ནི་སྤྱན་ལ་སོགས་པ་ལྷ་མོ་དང་བཅས་པ་རྣམས་ཀྱིའོ། །

[Block 2834]
བརྡར་གྱུར་པ་ནི་བརྡ་ཙམ་ཉིད་དུ་བཟུང་བའོ། །

[Block 2835]
དེ་བས་ན་ཐབས་དང་ཤེས་རབ་སྟོན་པ་ཉིད་ཀྱིས་ན་ཞེས་པ་ནི་སྟོང་པ༌[^1854]ཉིད་དང་སྙིང་རྗེའི་དེ་ཁོ་ན་ཉིད་ཐོབ་པར་བྱེད་པ་བསྒྲུབ༌[^1855]བྱ་དང་སྒྲུབ་བྱེད་དང་། རྡོ་རྗེ་དང་པདྨ་དང་དེ་དག་གི་སྙོམས་པར་ཞུགས་པ་ལས་སྐྱེས་པའི་བདེ་བ་ཆེན་པོའི༌[^1856]རྗོད་པར་བྱེད་པ་ཞེས་བར་དུའོ། །

[Block 2836]
སྨྲས་པ་གལ་ཏེ་དེ་ལྟ་ན་ནི་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་སྡུད་པ་པོ་ཡོད་པར་མི་འགྱུར་ཏེ་ཞེས་བསྟན་ཏོ། །

[Block 2837]
སྡུད་པ་པོ་མེད་ཅེས་དམ་བཅའ་བའོ། །

[Block 2838]
འབྲེལ་པ་མེད་པའི་ཕྱིར་ཞེས་གཏན་ཚིགས་སོ། །

[Block 2839]
དགོངས་པ་ནི་འདི་སྐད་བདག་གིས་ཐོས་པ་འདིས་ཐབས་དང་ཤེས་རབ་མཚོན་པར་བྱེད་པས་བདག་གིས་ཐོས་པ་ཞེས་བྱ་བ་ལ་སོགས་པའི་བྱེད་པ་པོ་དང་བྱ་བ་ལ་སོགས་པའི༌[^1857]རྣམ་གྲངས་ཅན་གྱི་ལས་མེད་པས་འབྲེལ་པ་མེད་དོ། །

[Block 2840]
དེ་བས་ན་བདག་གིས་ཐོས་ཞེས་སྡུད་པར་བྱེད་པ་པོ་མེད་པར་ཐལ་བར་འགྱུར་རོ། །
--- END BLOCKS ---
