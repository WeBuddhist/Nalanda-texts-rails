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
[Block 2696]
ཁྱིམ་པ་མོ་དང་མུ་སྟེགས་ཅན་མོ་དག་ལ་འདིར་སྡུག་བསྔལ་བ་དོན་འདིར༌[^1745]དགེ་སློང་མ་སྡེ་ཞིང་གནས་པ་ཞེས་བྱ་བ་འབྱུང་བར་དགའ་བ་ཉིད་ཀྱི་ཕྱིར་ཡང་མི་བསྟན༌[^1746]པའོ། །

[Block 2697]
སྐྱེས་པ་དང་ལྷན་ཅིག་སྡེ་ཞིང་གནས་པ་ལ་ཕམ་པའི་སྦྱོར་བ་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 2698]
རྣམ་པ་ཇི་ལྟར༌[^1747]སྡེ་ཞིང་གནས་པ་ལ་ཞེ་ན། དེའི་ཕྱིར་གཞོགས་སྟེགས་དང་འཕྱར་གཡེང་དང་རྩབ་ཧྲལ་གྱི་རྒྱུར་འགྱུར་བ་དག་གིས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་གཞོགས་སྟེགས་ལ་སོགས་པ་རྣམས་ཀྱི༌[^1748]དོན་ཐོ་འཚམས༌[^1749]པ་དང་ཀུན་དུ་རྩེ་བ་དང་། ཀུན་དུ་ཅ་ཅོ་འདོན་པ་རྣམ་གྲངས་ཇི་ལྟ་བ་བཞིན་དུ་དོན་བརྗོད་པའོ། །

[Block 2699]
ཆགས༌[^1750]དང་བཅས་པ་ཐམས་ཅད་ལ་འདུ་འཛིའི་སྐྱོན་ལ་འདིས་བསྡུས་པ་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 2700]
མཚན་ཉིད་ཇི་ལྟ་བར་ཡང་འདིར་ལྟུང་བ་གཞན་རྣམས་སྐྱེས་པའོ། །

[Block 2701]
བུད་མེད་དང་བསྟེན་པའི༌[^1751]དགེ་འདུན་ལྷག་མའོ། །

[Block 2702]
གང་ལ་བུད་མེད་དང་བསྟེན༌[^1752]དུ་འཇུག་པའི་དགེ་འདུན་ལྷག་མར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་སྡེ་པ་དེ་ཡང་དག་པར་འཛིན་དུ་འཇུག་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གཞོགས་སྟེགས་ལ་སོགས་པའི་རྒྱུར་འགྱུར་བའི་རྒྱུན་སྔར་བསྟན་མ་ཐག་པ་དག་གིས་དགེ་སློང་མ་དང་ལྷན་ཅིག་སྡེ་པ་དེ་ཡང་དག་པར་འཛིན་དུ་འཇུག་པ་ལ་མི་གཏོང་བ་ལའོ་ཞེས་བྱ་བ་དང་དགེ་འདུན་གྱི་དབྱེན་ལ་ཞུགས་པ་ལྟར་རོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2703]
ཡང་དག་པར་འཛིན་དུ་འཇུག་པའི་དགེ་འདུན་ལྷག་མའོ། །

[Block 2704]
གང་ལ་དགེ་འདུན་གྱི་དབྱེན་ལ་སོགས་པའི་དགེ་འདུན་གྱི་ལྷག་མ་བཞི་པོར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་དགེ་འདུན་འབྱེད་པ་ལ་སོགས་པ་བཞི་པ༌[^1753]ནི་དགེ་སློང་མའི་སྐབས་ལས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་སློང་མའི་དགེ་འདུན་འབྱེད་པའི་དགེ་སློང་མའི་རྗེས་སུ་འཇུག་པས་དགེ་སློང་མ་རྣམས་ལ་ལོག་པའི་འཇུག་པ་རྗེས་སུ་སྦྱར་བས་དགེ་སློང་མ་རྣམས་ལ༌[^1754]མི་སྨྲ་བ་ཉིད་དུ་བྱེད་པས་མི་གཏོང་བ་ལ་དགེ་འདུན་འབྱེད་པ་ལ་ཞུགས་པ་ལྟར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2705]
དགེ་སློང་མའི་དགེ་འདུན་ལྷག་མ་རྣམས་རྫོགས་སོ།། །།

[Block 2706 [HEADING]]
## དགེ་སློང་མའི་སྤང་བའི་ལྟུང་བྱེད་རྣམས། ^6-0

[Block 2707]
སྡོམ་གྱི་ཚིགས་སུ་བཅད་པ་དང་པོ་ལས།

[Block 2708]
འཆང་བ་ལ་སོགས་པ༌[^1755]ཇི་སྐད་གསུངས་པའི་རིམ་པས་སྤང་བ་རྣམས་ལ་དགེ་སློང་གི་རྣམ་པར་འབྱེད་པར་གཏོགས་པ་རྣམས་སྔར་ཇི་སྐད་བསྟན་པ་བཞིན་དུ་བལྟ་བར་བྱ་སྟེ། གསེར་དང་དངུལ་ལ་རེག་པ་དང་། མངོན་མཚན་ཅན་གྱི༌[^1756]སྤྱོད་པ་དང་། ཉོ་ཚོང་བྱེད་པ་དང་། ལྷུང་བཟེད་ཚོལ་བ་དང་། འཐག་ཏུ་འཇུག་པ་དང་། འཐག་པ་བསྐྱེད་པ་དང་། འཕྲོག་པ་དང་། བསྔོས་པ་ལས་བསྒྱུར་བ་དང་། སོག་འཇོག༌[^1757]ལས་གྱུར་པའོ་ཞེས་བྱ་བ་སྟེ། འདིར་གྱུར་པ་ཞེས་བྱ་བའི་སྒྲས་ནི་རེ་རེ་དང་སོ་སོར་སྦྱར་ཏེ། གསེར་དངུལ་ལ་རེག་པ་ལས་གྱུར་པ་ཞེས་བྱ་བའི༌[^1758]བྱེ་བྲག་ནི་སྔར་གྱི་མདོ་འདི་ལ་བརྟེན་ཏེ། ཕོ་ཉིད་ལ་ནི་མོ་ཉིད་དོ། །

[Block 2709]
དེ་ལ་ཕོ་ཉིད་དོ་ཞེས་བསྟན་པ་བཞིན་དུ་ཤེས་པར་བྱའོ། །

[Block 2710]
བྱེ་བྲག་འདི་ནི་འཁྲུར་འཇུག་པ་ལ་སོགས་པ་ལ་དམིགས་ཀྱིས་བསལ་བ་བསྟན་པའི་ཕྱིར་གཞན་དུ་གསལ་བ་ཉིད་ཀྱི་དོན་དུ་བསྡུས་པ་ལ་ཆུང་བ་ཉིད་ཀྱི་ཕྱིར་བསྟན་པ་དེ་བས་ན་ཉེ་བར་བསྟན་པར་བྱ་སྟེ། འཁྲུ་བ་ལ་སོགས་པའི་དགེ་སློང་གིའོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་དགེ༌[^1759]སློང་མས་དགེ་སློང་དབང་བའི་གོས་གང་ཡིན་པ་དེ་གོས་འཁྲུ་བ་ལ་སོགས་པ་སྤང་བའི་ལྟུང་བྱེད་དོ། །

[Block 2711]
དེ་ལས་ལེན་ནའོ་ཞེས་བྱ་བ༌[^1760]ནི༌[^1761]དགེ་སློང་ལས་བླངས་ན་སྤང་བར་འགྱུར་བ་ཡིན་གྱི་དགེ་སློང་མ་ལས་ནི་མ་ཡིན་ཏེ་དགེ་སློང་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2712]
འོ་ན་གང་ཞིག་དགེ་སློང་ལ་ཁ་ན་མ་ཐོ་བ་དེ་ཉིད་འདིར་སྨོས་ན། འདིར་འཁྲུ་བ་ལ་སོགས་པའི་སྤང་བའི་ལྟུང་བ་ཉིད་རྟེན་ནམ་ཞེ་ན་མ་ཡིན་ཏེ། དེའི་ཕྱིར་རྣམ་པ་བདུན་པོ་དང་པོར་སྲིན་བལ་གྱི་སྟན་བྱེད་པ་ནས་བལ་རྨེལ་དུ་འཇུག་པའི་མཐར་ཐུག་པ་དག་དང་། བཅུ་པ༌[^1762]

[Block 2713]
གསུམ་པ་ལས་ལྷུང་བཟེད་འཆང་བ་དང་། བརྟད་པ༌[^1763]ལས་བྱུང་བ་དང་། ཞག་བདུན་ན་འབྲལ་བ་དང་། དབྱར་གྱི་རས་ཆེན་གྱི་སྤང་བ་ཞེས་བྱ་བ་བཞི་པོ་དག་སྟེ། རྣམ་པ་བཅུ་གཅིག་པོ་དེ་དག་ནི་འདིར་སྤངས་པའོ། །

[Block 2714]
ལྷ་རྟེན་བཅང་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་སྦོམ་དགའ་མོ་མཉན་ཡོད་དུ་བསོད་སྙོམས་ལ་ཞུགས་པ་ན། དེས་ལྷ་བོན་མོ་ལྷ་རྟེན་ཐོགས་ཤིང་རྒྱུ་བ་ཞིག་མཐོང་ནས། སྦོམ་དགའ་མོས་བསམས་པ།[^1764] ཐབས་འདི་ནི་བཟང་པོ་ཞིག་ཡིན་པས། བདག་གིས་སང་ཤེས་པར་བྱའོ་སྙམ་ནས། དེའི་ཕྱི༌[^1765]དེའི་ཉིན་པར་ལྷ་རྟེན་ཐོགས་ཏེ། མཉན་ཡོད་དུ་ཞུགས་ནས། ཁྱེའུ་དང་བུ་མོ་དག་ལ་སྲུང་སྐྱོབ་བྱེད་ཅིང་དེས་གང་དང་གང་ལ་སྲུང་སྐྱོབ་བྱས་པ༌[^1766]དེ་དང་དེ་དག་བདེ་བར་གནས་པར་གྱུར་ནས། དེའི་ཕྱིར་གང་དང་གང་དག་ལ་སྲུང་སྐྱོབ་བྱ་དགོས་པར་གྱུར་པ་དེ་དག་ཐམས་ཅད་ཀྱིས་སྦོམ་དགའ་མོ་སྲུང་སྐྱོབ་བྱེད་དུ་འཇུག་པར་བྱེད་ན༌[^1767]ལྷ་བོ་ན་མོ་འཕྱ་བར་གྱུར་པ་ནས། ཇི་སྲིད་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དེ་ལྟ་བས་ན་དགེ་སློང་མས་ལྷ་རྟེན་བཅང་བར་མི་བྱའོ་ཞེས་བྱ་བའི་བར་དུ་གསུངས་པ་ཡིན་ནོ། །

[Block 2715]
ལྷ་རྟེན་ཞེས་བྱ་བ་ནི་སྲུང་སྐྱོབ་བྱ་བ་དེའི་ཕྱིར་སྣོད་ཟ་མ་ཏོག་གིས་བརྒྱན་ཅིང༌[^1768]ས་ལས་བྱས་པའི་གཟུགས་ཀྱིས་བཀང་བ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 2716]
གང་ལ་ལྷུང་བཟེད་འཆང་བའི་སྤང་བའི༌[^1769]ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་ལྷུང་བཟེད་ལྷག་པ༌[^1770]ཞག་གཅིག་ལས་འདས་པར་འཆང་བ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བུད་མེད་རྣམས་ནི་ཡོ་བྱད་ལ་ལྷག་པར་ཆགས་པ་ཤིན་ཏུ་དམ་པས་ན་དེའི་ཕྱིར་ཞག་གཅིག་ལས་འདས་པར་འཆང་བ་ལ་ཁ་ན་མ་ཐོ་བ་འདིར་རྣམ་པར་གཞག་གོ། །

[Block 2717]
ལྷུང་བཟེད་འཆང་བའི་སྤང་བའོ། །

[Block 2718]
གང་ལ་བྱིན་གྱིས་མི་རློབ༌[^1771]པའི་སྤང་བར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་བྱིན་གྱིས་བརླབ་ཏུ་རུང་བ་ཉི་མ་དང་པོ་ལའམ། ཟླ་བ་ཕྱེད་ཕྱེད་ཅིང་བྱིན་གྱིས་མ་བརླབས་པ༌[^1772]ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་ཕྱེད་ཕྱེད་ཀྱི་སྒྲས༌[^1773]ནི་ལན་གཉིས་སུ་བརྗོད་པའོ། །

[Block 2719]
ཟླ་བ་ཕྱེད་ཕྱེད་ཅེས་བྱ་བ་ལྔ་པོ་མེད་པ་ཉིད་ཀྱིས་ཉི་མ་གང་ལ་ཆོས་གོས་གང་ཡང་རུང་བ་ཞིག་རྙེད་ན་ཉི་མ་དེ་ཉིད་ལ་བྱིན་གྱིས་བརླབ་པར་བྱ་སྟེ། དེ་ཡང་དེ་ཕྱིན་ཆད་ཟླ་བ་ཕྱེད་ཕྱེད་ཅིང་བྱིན་གྱིས་བརླབ་པར་བྱའོ་ཞེས་བྱ་བ་འདི༌[^1774]འདིར་རྣམ་པར་གཞག་པའོ། །

[Block 2720]
དེར་མེད་པ་ཉིད་ལ་ཆོས་གོས་རྙེད་པའི་ཞག་ལ་བྱིན་གྱིས་མི་རློབ་ནའོ། །

[Block 2721]
ཡོད་པ་ཉིད་ལ་ནི་ཟླ་བ་ཕྱེད་ཕྱེད་ཅིང་བྱིན་གྱིས་མ་བརླབས་ན་སྤང་བར་འགྱུར་རོ། །

[Block 2722]
ཆོས་གོས་བྱིན་གྱིས་བརླབས་པ་དེ༌[^1775]ཉིད་ཀྱང་ཉིན་ཞག་བར་མ་ཆད་པ་དེ་ཉིད་དང་པོར་བྱ་སྟེ། ཐོག་མ་ཉིད་དུ་མངོན་པར་བསྟན༌[^1776]ནས་ཉི་མ་དང་པོ་དེ་ལ་ཟླ་བ་ཕྱེད་ཕྱེད་དུ་ཆོས་གོས་བྱིན་གྱིས་བརླབ་རྒྱུ་བྱིན་གྱིས་མ་བརླབས་ན་ཞག་བཅུ་དྲུག་པ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2723]
འདིར་དགེ་སློང་ལ་ནི་ཆོས་གོས་བྱིན་གྱིས་བརླབ་ཏུ་རུང་བ་མེད་ན་འདི་དང་བྲལ་བའི་སྐྱ་རེངས་ཤར་བ་སྤང་བར་མི་འགྱུར་བ་དེ་བས་ན་ཉེས་བྱས་སུ་རིག་པར་བྱ་སྟེ། གཞན་ལ་ནི་ལྟུང་བ་མེད་དོ། །

[Block 2724]
སྤོང་བ༌[^1777]འོག་མ་རྣམས་ལ་ཡང་ཐ་མ་གཉིས་ནི་ལྟུང་བ་མེད་དེ་གཞན་ལ་ནི་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 2725]
བྱིན་གྱིས་མི་རློབ་པའི་སྤང་བའོ། །གང་ལ་འབྱིན་པའི་སྤང་བར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་དཔྱིད་ཟླ་ར་བའི་ཉའི་ཉིན་མོའི་མདུན་རོལ་དུ་སྲ་བརྐྱང་འབྱིན་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དཔྱིད་ཟླ་ར་བའི་ཉའི་ཉིན་མོ་གང་ཡིན་པ་དེའི་མདུན་རོལ་ཕན་ཆད་ཀྱི་དུས་གང་ཡང་རུང་བར་སྲ་བརྐྱང་འབྱིན་པའི་དགེ་འདུན་མ་རྣམས་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2726]
ཤིན་ཏུ་སྟོབས་དང་ལྡན་པ་ཉིད་ཀྱི་ཕྱིར་བུད་མེད་རྣམས་ཀྱི་རྙེད་པ་ལ་ཐ་སྙད་འདི་ནི་དགེ་འདུན་བྱེད་པ་པོ་ཉིད་ཡིན་གྱི་གང་ཟག་ལ་ནི་མ་ཡིན་ནོ། །

[Block 2727]
དེ་ལྟ༌[^1778]བས་ན་དགེ་འདུན་ཐམས་ཅད་ལ་སོ་སོར་འདི་བསྐྱེད་པར་འགྱུར་རོ། །

[Block 2728]
དགེ་འདུན་མའི་ཚད་རྣམ་པར་ཆད་པ་ལ་སྤང་བའི་ལྟུང་བྱེད་བསྐྱེད་པའོ། །

[Block 2729]
དེ་བས་ན་རྣམ་པར་འབྱེད་པ་མ་ཡིན་པ་ལས་འདི་ནི་སྤང་བ་ཉིད་དོ། །

[Block 2730]
དེའི་ཚེ་ན་སྒྲུབ་པ་མ་བྱས་པ་དང་རྣམ་པར་མ་ཕྱེ་བ་ལ་སྤང་བར་བྱ་བ་ཉིད་མེད་དོ། །

[Block 2731]
དགེ་སློང་མ་ཆོམ་རྐུན་པས་ཀྱང༌[^1779]བཅོམ་པའི་དོན་ཉིད་དུ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བར༌[^1780]ནི་འདིར་དོན་གཅིག་ལ་མདུན་རོལ་དུ་སྲ་བརྐྱང་འབྱིན་པ་ལ་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2732]
གང་གི་ཚེ་དགེ་སློང་མ་ཆོམ་རྐུན་པ་དག་གིས་བཅོམ་པར་གྱུར་ན་དེའི་དོན་ཉིད་དུ་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ནི་བྱེ་བྲག་བཤད་མཚོ་ལས་ཤེས་པར་བྱའོ། །

[Block 2733]
སྲ་བརྐྱང་འབྱིན་པའི་སྤང་བའོ། །གང་ལ་མི་འབྱིན་པའི་སྤང་བར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་མི་འབྱིན་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སྲ་བརྐྱང་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2734]
མི་འབྱིན་པ་ཞེས་བྱ་བ་ནི་ཚོགས་པ་སྦྱིན་པར་མི་བྱེད་པར་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 2735]
དེ་ལ་ཞེས་བྱ་བ་ནི་གང་ཞིག་སྲ་བརྐྱང་འབྱིན་པའི་དོན་དུ་སྲ་བརྐྱང་འབྱིན་པའི་ལས་ལ་ཚོགས་པ་སྦྱིན་པ་ཞེས་བྱ་བ་ལྟུང་བྱེད་འབའ་ཞིག་པར་རྣམ་པར་གཞག་པ་དེ་ནས་འདི་ལ་དུས་ཀྱི་བྱེ་བྲག་ཙམ་གྱི་བྱེ་བྲག་ཤེས་པར་བྱའོ། །
--- END BLOCKS ---
