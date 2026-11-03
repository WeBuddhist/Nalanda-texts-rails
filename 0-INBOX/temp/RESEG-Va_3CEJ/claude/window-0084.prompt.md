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
[Block 2941]
མ་རིག་པའི་རྒྱུ་མ་བསྟན་པའི་ཕྱིར་འཁོར་བ་ཐོག་མ་ཅན་དུ་ཡང་འགྱུར༌[^1636]ལ། རྒ་ཤིའི་འབྲས་བུ་མ་བསྟན་པའི་ཕྱིར་མཐའ་དང་ལྡན་པར་ཡང་འགྱུར་བའམ། ཡང་ན་ནི་ཡན་ལག་གཞན་གྱིས་ཁ་བསྐང་དགོས་སོ། །

[Block 2942]
དེ་ལ་ཡང་གཞན་ཞིག་ཡོད་ན་ནི་ཐུག་པ་མེད་པར་འགྱུར་རོ་ཞེ་ན། ཁ་བསྐང་བར་བྱ་མི་དགོས་ཏེ། འདི་ལྟར་འདིར་བཅོམ་ལྡན་འདས་ཀྱིས།

[Block 2943 [VERSE]]
ཉོན་མོངས་པ་ལས་ཉོན་མོངས་དང་། །
བྱ་བ་ཉིད་དོ་དེ་ལས་གཞི། །

[Block 2944]
དེ་ལས་གཞི་དང་ཉོན་མོངས་སྐྱེས།[^1637] །འདི་ནི་སྲིད་པའི་ཡན་ལག་ལུགས། །ཞེས་བསྟན་ཟིན་ཏོ། །

[Block 2945]
ཉོན་མོངས་པ་ལས་ཉོན་མོངས་པ་སྐྱེ༌[^1638]སྟེ། སྲེད་པ་ལས་ལེན་པའོ། །

[Block 2946]
ཉོན་མོངས་པ་ལས་ལས་ཏེ། ལེན་པ་ལས་ནི༌[^1639]སྲིད་པ་དང་། མ་རིག་པ་ལས་འདུ་བྱེད་རྣམས་སོ། །

[Block 2947]
ལས་ལས་གཞི་སྟེ། འདུ་བྱེད་རྣམས་ལས་རྣམ་པར་ཤེས་པ་དང་། སྲིད་པ་ལས༌[^1640]སྐྱེ་བའོ། །

[Block 2948]
གཞི་ལས་གཞི་སྟེ། རྣམ་པར་ཤེས་པ་ལས་མིང་དང་གཟུགས་ནས་རེག་པ་ལས༌[^1641]ཚོར་བའི་བར་དང་། སྐྱེ་བ་ལས༌[^1642]རྒ་ཤིའོ། །

[Block 2949]
གཞི་ལས་ཉོན་མོངས་པ་སྟེ། ཚོར་བ་ལས་སྲེད་པའོ། །

[Block 2950]
གང་གི་ཕྱིར༌[^1643]སྲིད་པའི་ཡན་ལག་རྣམས་ཀྱི་ལུགས་དེ་ལྟར་རྣམ་པར་གཞག་པ༌[^1644]དེའི་ཕྱིར་མ་རིག་པ་ཉོན་མོངས་པའི༌[^1645]རང་བཞིན་ཡང་གཞི་འམ་ཉོན་མོངས་པ་ལས་སྐྱེ་བར་འགྱུར་རོ་ཞེས་བསྟན་པ་ཡིན་ལ། རྒ་ཤི་ནི༌[^1646]ཚོར་བ་ལ་ཐུག་པའི་གཞི་ལས་ཀྱང་ཉོན་མོངས་པ་འབྱུང་ངོ་ཞེས་བསྟན་པ་ཡིན་པས༌[^1647]ཡང་འདི་ལ་ཁ་བསྐང་བར་བྱ་བ་ཅུང་ཟད་ཀྱང་མེད་དེ། དེ་ལྟར་ན་སྡུག་བསྔལ་གྱི་ཕུང་པོ་ཆེན་པོ་འདི་འབའ་ཞིག་ཡང་དག་པར་འབྱུང་བར༌[^1648]འགྱུར་རོ་ཞེས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 2951]
དེ་ལྟ་མ་ཡིན་ན་འདིའི༌[^1649]ནུས་པ་ཅི་ཞིག་ཡོད་པར་འགྱུར། གཞན་དག་ན་རེ་མདོ་གཞན་ལས་མ་རིག་པ་ཡང་ཚུལ་བཞིན་མ་ཡིན་པ་ཡིད་ལ་བྱེད་པའི་རྒྱུ་ལས་བྱུང་བ་ཡིན་ནོ། །

[Block 2952]
ཚུལ་བཞིན་མ་ཡིན་པ་ཡིད་ལ་བྱེད་པ་ཡང་མ་རིག་པའི་རྒྱུ་ལས་བྱུང་བ་ཡིན་ནོ། །ཞེས་གསུངས་ལ། དེ་ནི་འདིར་ཡང་ལེན་པའི་ནང་དུ་འདུས་པའི་ཕྱིར་བཤད་པ་ཡིན་ནོ་ཞེས་ཟེར་ཏེ། ཚུལ་བཞིན་མ་ཡིན་པ་ཡིད་ལ་བྱེད་པ། ལེན་པའི་ནང་དུ་ཇི་ལྟར་འདུས། གལ་ཏེ་མཚུངས་པར་ལྡན་པ་ལས་ཡིན་ནོ་ཞེ་ན་ནི་སྲིད་པ༌[^1650]དང་མ་རིག་པ་དག་གི་ནང་དུ་ཡང་དེ༌[^1651]འདུས་པར་ཐལ་བར་འགྱུར་རོ། །

[Block 2953]
ནང་དུ་འདུས་པ་ཡིན་དུ་ཆུག་ན་ཡང་ཇི་ལྟར་འདིར་མ་རིག་པ་ནི་ཚུལ་བཞིན་མ་ཡིན་པའི་རྒྱུ་ལས་བྱུང་བ་ཡིན་ནོ་ཞེས་བྱ་བར་བསྟན་པ་ཡིན། གལ་ཏེ་ནང་དུ་འདུས་པ་ཁོ་ནས་རྒྱུ་དང་འབྲས་བུའི་དངོས་པོར་ཤེས་པར་འགྱུར་ན། འོ་ན་ནི་སྲེད་པ༌[^1652]དང་མ་རིག་པ་དག་ཀྱང་དེའི་ནང་དུ་འདུས་པའི་ཕྱིར་ཡན་ལག་གཞན་ཉིད་དུ་མི་བྱ་བར་ནུས་སོ། །

[Block 2954]
གཞན་དག་ན་རེ་མདོ་གཞན་ལས་མ་རིག་པའི་རྒྱུ་ཚུལ་བཞིན་མ་ཡིན་པ་ཡིད་ལ་བྱེད་པ་ཡིན་པར་གསུངས་ཏེ། དེ་ཡང་མིག་དང༌[^1653]གཟུགས་རྣམས་ལ་བརྟེན་ནས་གཏི་མུག་ལས་སྐྱེས་པའི་ཡིད་ལ་བྱེད་པའི༌[^1654]རྙོག་པ་སྐྱེའོ་ཞེས་གསུངས་པའི་ཕྱིར་རེག་པའི༌[^1655]དུས་སུ་བསྟན་པ་ཡིན་ལ། མདོ་གཞན་ལས་མ་རིག་པའི་འདུས་ཏེ་རེག་པ་ལས་བྱུང་བའི་ཚོར་བ་ལ་བརྟེན་ནས་སྲེད་པ་སྐྱེའོ་ཞེས་གསུངས་པའི་ཕྱིར་ཚོར་བའི་དུས་སུ་ཡང་མ་རིག་པ་གདོན་མི་ཟ་བར་ཡོད་དོ། །

[Block 2955]
དེ་ལྟ་བས་ན་རེག་པའི་དུས་ན་ཡོད་པའི་ཚུལ་བཞིན་མ་ཡིན་པ་ཡིད་ལ་བྱེད་པ་ནི་ཚོར་བ་དང་ལྷན་ཅིག་འཇུག་པའི་མ་རིག་པའི་རྐྱེན་གྱི༌[^1656]ངོ་བོར་གྲུབ་པས༌[^1657]མ་རིག་པ་རྒྱུ་མེད་པ་ཉིད་ཀྱང་མ་ཡིན་ཞིང་། ཡན་ལག་གཞན་གྱིས༌[^1658]ཁ་བསྐང་བར་ཡང་མི་བྱའོ། །

[Block 2956]
ཐུག་པ་མེད་པར་ཐལ་བར་འགྱུར་བ་ཡང་མ་ཡིན་ཏེ། གཏི་མུག་ལས་སྐྱེས་པའི་ཡིད་ལ་བྱེད་པ་རྙོག་པ་ཞེས་འབྱུང་བས༌[^1659]ཚུལ་བཞིན་མ་ཡིན་པ་ཡིད་ལ་བྱེད་པ་དེ་ཡང་གཏི་མུག་ལས་སྐྱེས་པར་གསུངས་པའི་ཕྱིར་རོ། །

[Block 2957]
འོ་ན་ནི་དེ་ནི་གཞན་དུ་གསུངས་པས་འདིར་ཡང་བརྗོད་པར་བྱ་དགོས་སོ་ཞེ་ན། བརྗོད་པར་བྱ་མི་དགོས་སོ། །

[Block 2958]
མ་བརྗོད་བཞིན་དུ་ཇི་ལྟར་གོ་ཞེ་ན་རིགས་པ་ལས་སོ། །

[Block 2959]
རིགས༌[^1660]པ་གང་གིས་ཤེ༌[^1661]ན། དགྲ་བཅོམ་པ་རྣམས་ཀྱི་ཚོར་བ་མ་རིག་པ་མེད་པ་ནི་སྲེད་པའི་རྐྱེན་མ་ཡིན་ནོ། །

[Block 2960]
ཕྱིན་ཅི་ལོག་མེད་པའི་སྲིད་པ༌[^1662]ཡང་ཉོན་མོངས་པ་ཅན་གྱི་ཚོར་བའི་རྐྱེན་མ་ཡིན་ལ། དགྲ་བཅོམ་པ༌[^1663]མ་རིག་པ་མེད་པའི་རེག་པ༌[^1664]ཡང་ཕྱིན་ཅི་ལོག་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་རིགས་པ༌[^1665]འདིས་སོ། །

[Block 2961]
ཇི་སྙེད་རིགས་པས༌[^1666]འཐད་པ་དེ་སྙེད་མ་བཤད་བཞིན་དུ་ཡང་གོ་བར་འགྱུར༌[^1667]ན། དེ་ལྟ་ན་ནི་ཧ་ཅང་ཐལ་བར་འགྱུར་ཏེ། དེ་ལྟ་བས་ན་འདི་ནི་ལན་མ་ཡིན་ནོ། །

[Block 2962]
མ་རིག་པ་དང་། རྒ་ཤི་དག་ལས་གཞན་མ་བསྟན་པའི་ཕྱིར་འཁོར་བ་ལ་ཐོག་མ་དང་ཐ་མ་དང་ལྡན་པར་ཐལ་བར༌[^1668]འགྱུར་རོ་ཞེས་བྱ་བ་འདི་ནི་ཀླན་ཀར་མི་རུང་བ་ཁོ་ན་ཡིན་ལ་མ་ཚང་བར་བསྟན་པ་ཡང་མ་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན། འདིར་ནི་ཇི་ལྟར་ན་འཇིག་རྟེན་ཕ་རོལ་ནས་འཇིག་རྟེན་འདིར། འཇིག་རྟེན་འདི་ནས་ཡང་འཇིག་རྟེན་ཕ་རོལ་དུ་འབྲེལ་སྙམ་དུ་འཇུག་པ་ལ་རྨོངས་པའི་གདུལ་བ་རྣམས་ལ་དེ་ཙམ་ཞིག་བརྗོད་པར་བཞེད་པའི་ཕྱིར་ལ། དེ་ནི།

[Block 2963 [VERSE]]
སྔོན་དང་ཕྱི་མཐའི༌[^1669]བར་དག་ལ། །
རྨོངས་པ་རྣམ་པར་བཟློག༌[^1670]ཕྱིར་རོ། །

[Block 2964]
ཞེས་བྱ་བ་འདིས་སྔར་བཤད་ཟིན་པའི་ཕྱིར་རོ། །

[Block 2965 [HEADING]]
##### རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་དང་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་ཆོས་རྣམས་ཀྱི་ཁྱད་པར། ^3-1-11-6-0

[Block 2966]
བཅོམ་ལྡན་འདས་ཀྱིས་དགེ་སློང་དག་ཁྱེད་ལ་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་དང་། རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་ཆོས་རྣམས་ཀྱང་བསྟན་པར་བྱའོ་ཞེས་གསུངས་པ། ཡང་དེ་དག་ལ་ཁྱད་པར་ཅི་ཞིག་ཡོད་ཅེ་ན། རེ་ཞིག་བསྟན་བཅོས་ལས་ནི་ཁྱད་པར་ཅུང་ཟད་ཀྱང་མེད་དེ། གཉི་ག་ཡང་འདུས་བྱས་ཀྱི༌[^1671]ཆོས་ཐམས་ཅད་ཡིན་པར་གསུངས་སོ། །

[Block 2967]
ད་ནི་ཇི་ལྟར་ན་མ་འོངས་པ་མ་བྱུང་བ་རྣམས་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་དག་ཅེས་བྱ། རེ་ཞིག་མ་འོངས་པ་མ་བྱས་པ་རྣམས་ཁོ་ན་ཡང་ཇི་ལྟར་ན་འདུས་བྱས་དག་ཅེས་བྱ། མངོན་པར་འདུ་བྱེད་པའི༌[^1672]སེམས་པས་བསམས་པའི༌[^1673]ཕྱིར་རོ། །

[Block 2968]
ཟག་པ་མེད་པ་རྣམས་ཇི་ལྟར། དེ་དག་ཀྱང་ཐོབ་པར་བྱ་བའི་ཕྱིར་སེམས་པ་དགེ་བས་བསམས་པ༌[^1674]དག་ཡིན་ནོ། །

[Block 2969]
མྱ་ངན་ལས་འདས་པ་ལ་ཡང་ཐལ་བར་འགྱུར་རོ་ཞེ་ན། [^1675]དེ་དང་རིགས་མཐུན་པའི་ཕྱིར་དེ་ཁོ་ན་བཞིན་དུ་མཐུན་པར་བསྒྲེས་པ་ཡིན་ཏེ། དཔེར་ན་རེ་ཞིག་གཟུགས་སུ་མི་རུང་བ་ཡང་དེ་དང་རིགས་མཐུན་པའི་ཕྱིར་གཟུགས་ཞེས་བྱ་བ་བཞིན་པས་དེ་ནི་ཉེས་པ་མེད་དོ། །

[Block 2970]
མདོའི་དགོངས་པ་ནི།

[Block 2971 [VERSE]]
འདིར་ནི་འབྱུང་བ་རྒྱུ་ཡིན་ཏེ། །
བྱུང་བ་འབྲས་བུ་ཡིན་པར་འདོད། །

[Block 2972]
ཅེས་པ་འདི་ཡིན་ཏེ། རྒྱུར་གྱུར་པའི་ཡན་ལག་ནི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཡིན་ཏེ།[^1676] འདི་ལས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 2973]
འབྲས་བུར་གྱུར་པའི་ཡན་ལག་ནི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་སྟེ། དེ་ལྟར་ན་ཡན་ལག་ཐམས་ཅད་ཀྱང་རྒྱུ་དང་འབྲས་བུར་གྱུར་པའི་ཕྱིར་གཉི་གར་འགྲུབ་པར་འགྱུར་རོ། །

[Block 2974]
དེ་ལྟ་ཡིན་ཡང་ལྟོས་པའི་བྱེ་བྲག་གིས་རྣམ་པར་གཞག་པ་མེད་པ་ཡང་མ་ཡིན་ཏེ། གང་ལ་ལྟོས་ནས་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཡིན་པ་དེ་ཉིད་ལ་ལྟོས་ནས་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་དེ༌[^1677]མ་ཡིན་ཏེ། རྒྱུ་དང་འབྲས་བུ་བཞིན་དང་ཕ་དང་བུ་བཞིན་ནོ། །

[Block 2975]
གནས་བརྟན་བསམ་རྫོགས་ན་རེ། རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཡིན་ལ། རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་ཆོས་དག་མ་ཡིན་པ་ཡང་ཡོད་དེ་ཞེས་བྱ་བ་མུ་བཞི་སྟེ། མུ་དང་པོ་ནི་ཆོས་མ་འོངས་པ་རྣམས་སོ། །

[Block 2976]
གཉིས་པ་ནི་དགྲ་བཅོམ་པའི་ཆོས་ཐ་མ་འདས་པ་དང་། ད་ལྟར་བྱུང་བ་རྣམས་སོ། །

[Block 2977]
གསུམ་པ་ནི་དེ་ལས་གཞན་པའི་ཆོས་འདས་པ་དང་། ད་ལྟར༌[^1678]བྱུང་བ་རྣམས་སོ། །

[Block 2978]
བཞི་པ་ནི་ཆོས་འདུས་མ་བྱས་རྣམས་སོ་ཞེས་ཟེར་རོ་ཞེས་གྲག་གོ། །

[Block 2979]
འདིར་མདོ་སྡེ་པ་རྣམས་རྒོལ་བར་བྱེད་དེ། ཅི་འདི་དག་གང་ཞིག་གང་འདོད་པའི་འདོད་རྒྱལ་དུ་འཆད་པ་ཞིག་གམ། འོན་ཏེ་མདོའི་དོན་ཡིན། སྨྲས་པ། མདོའི་དོན་ཡིན་ནོ། །

[Block 2980]
གལ༌[^1679]ཏེ་མདོའི་དོན་ཡིན་ནོ་ཞེ་ན། འདི་ནི་མདོའི་དོན་མ་ཡིན་ནོ། །
--- END BLOCKS ---
