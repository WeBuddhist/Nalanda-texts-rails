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
[Block 2731]
བུ་ལེགས་སོ་ལེགས་སོ་བྲམ་ཟེ་ཆེན་པོ་ལེགས་སོ་ཞེས་བྱ་བ་ནི་གང་གོང་དུ་བསྟན་པའི་རྒྱུ་དགུས་དུལ་བ་ཞེས་བྱ་བ་དང་། རང་གི་ཆོས་ཉིད༌[^1721]གྲགས་པ་ཞེས་བྱ་བ་སྟེ། དེ་དང་རྗེས་སུ་མཐུན་པའི་ཕྱིར་རོ། །

[Block 2732]
རབ་ཏུ་ཞི་བས་བརྒྱན་པ་ཞེས་བྱ་བ་ནི་གང་གོང་དུ་བསྟན་པའི་ལང་ཚོའི་ཚེ་ཡང་ཞི་ཞིང་ཆོས་བཟང་བས་ཞེས་བྱ་བ་དེ་དང་རྗེས་སུ་མཐུན་པའི་ཚིག་གོ། །

[Block 2733]
ཁྱོད་ཀྱི་ཤེས་རབ་ཅེས་བྱ་བ་ནི་གང་གོང་དུ་བསྟན་པའི། ཐོས་པ་ལྡོབ་ཅིང་འཛིན་གསལ་དང་། །ཞེས་བྱ་བ་ཡིན་ཏེ། དེ་དང་རྗེས་སུ་མཐུན་པའི་ཚིག་གོ། །

[Block 2734]
རང་གི་ཆོས་ཉིད་ལམ་ཡིན་པས་རང་གི་ཆོས་ལམ་སྟེ། རང་གི་ཆོས་ཀྱི༌[^1722]བདེ་འགྲོ་ཐོབ་པར་བྱེད་པ་ནི་ཆོས་ཡིན་ནོ། །

[Block 2735]
དཀའ་ཐུབ་ཅེས་སྨོས་པས་ནི་ངོ་ཚ་ཤེས་པ་དང་ཁྲེལ་ཡོད་པ་གཉིས་གཟུང་ངོ་། །ཐོས་པ་དང་ཤེས་པ་སྨོས་པས་ནི་སེམས་ལས་བྱུང་བ་ལྷན་ཅིག་སྐྱེས་པའི་ཤེས་རབ་གཟུང་སྟེ། འདི་དག་གིས་ནི་བདག་ལ་ཕན༌[^1723]པའི་ཐབས་བསྟན་ཏོ། །

[Block 2736]
དགེ་བ་རྣམས་ཞེས་བྱ་བ་འདིས་ནི་གཞན་ལ་ཕན་པ་སྒྲུབ་པ༌[^1724]རྣམས་ནི་ཕོངས་པར་གྱུར་ཀྱང་འགྱུར་བ་མེད་པར་བསྟན་ཏོ། །

[Block 2737]
ཡང་ན་ཁྲེལ་ཡོད་པ་ཞེས་བྱ་བ་བསྟན་པ་ལས་ངོ་ཚ་ཤེས་པ་དང་ཁྲེལ་ཡོད་པའི་དབང་དུ་བྱས་པ་ཡིན༌[^1725]པས། དེས༌[^1726]ཁྲེལ་ཡོད་པ་ཡང་མི་བརྗོད་དེ་གྲུབ་ཟིན་པའི་ཕྱིར་རོ། །

[Block 2738]
རྣམ་པར་གྲགས་པ་ནི་མཛེས་པར་སྤྱོད་པ་དང་། ལེགས་པར་སྦྱོར་བ་སྟེ། ཐོས་པ་དོན་དང་ལྡན་པའོ། །

[Block 2739]
ལེགས་པར་སྤྱོད་པ་སྤྱད་པའི་ཕྱིར་ཐོས་པ་གཟུང་སྟེ། དེ་ལ་ལེགས་པར་སྤྱོད་པ་ཡིན་པས་ཐོས་པ་དོན་དང་ལྡན་པ་སྟེ། དེ་འབྲས་བུ་དང་བཅས་པའོ། །

[Block 2740]
ཐོས་པ་དེ་ཡང་ང་ཡི་འབད་པས་ལེགས་པར་འབྱུང་བ་སྟེ། དེ་ག༌[^1727]ལས་ཤེ༌[^1728]ན། དོན་ཡོད་པ་ལས་ཏེ། དེས་ན་འདི་ལས་འབྱུང་བའོ། །

[Block 2741]
བདེ་བ་འབྱུང་བ་ནི་ལེགས་པར་འབྱུང་བའོ། །

[Block 2742]
དེའི་ཕྱིར་འབད་པའི་དོན་ཡོད་པ་ཡིན་ཏེ། འབྲས་བུ་དང་བཅས་པ་ཉིད་པས་ངལ་བ་དོན་ཡོད་པ་ཉིད་དོ། །

[Block 2743]
བདག་ཉིད་ངོ་ཚ་བ་ཉིད་ཀྱིས་ཞེས་བྱ་བ་གང་གི་ཕྱིར་འཛེམ་པ༌[^1729]ཞེས་བྱ་བའི་དོན་དེ་ཉིད་འཇིག་རྟེན་གྱི་དབང་དུ་བྱས་པ་ཉིད་ཀྱིས་ཁྲེལ་ཡོད་པ་ཡང་དེ༌[^1730]ཉིད་ཡིན་ཏེ། ཁྲེལ་ཡོད་པ་བསྟན་པ་ནི་འདི་ལྟར། སྡིག་པའི་ལས་རྣམས་བྱེད་པ་ལ།[^1731] །ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་གཉིས་ཀྱིས་བསྟན་ཏོ། །

[Block 2744]
བདག་ཉིད་ཀྱི་ངོ་ཚ་ཤེས་པ་ཉིད་སྨྲས་པ། བདག་གིས་གང་ན་སྟོང་པ་ནི། །ཞེས་བྱ་བ་ལ་སོགས་པ་ཚིགས་བཅད་གསུམ་གྱིས་ཀྱང་དེ་བསྟན་པ་ཡིན་ནོ། །

[Block 2745]
སློབ་དཔོན་དཔའ་བོས་མཛད་པའི་སྐྱེས་པའི་རབས་རྒྱ་ཆེར་བཤད་པ་ལས་བྲམ་ཟེའི་སྐྱེས་པའི་རབས་སོ།། །།

[Block 2746 [HEADING]]
## མྱོས་བྱེད་མའི་སྐྱེས་པའི་རབས། ^14-0

[Block 2747]
སྡུག་བསྔལ་མི་བཟོད་པས༌[^1732]གདུངས་པས།[^1733] །ཞེས་བྱ་བ་ལ། འདིར་སྡུག་བསྔལ་ནི་རྣམ་པར་འགྱུར་བའི་སྡུག་བསྔལ་ལ་གསུངས་པར་དགོངས་པ་ཡིན་ཏེ། རྣམ་པར་འགྱུར་བའི་སྡུག་བསྔལ་ཡང་འདོད་ཆགས་ལས་སྐྱེས་པ་སྟེ། འདོད་པའི་འདོད་ཆགས་ཀྱིས་རྣམ་པར་འགྱུར་བའི་སེམས་སོ་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 2748]
ངན་པ་རྣམས་ཀྱི་ལམ་ཡིན་པས་ངན་པའི་ལམ་སྟེ། དེར༌[^1734]འཇུག་པར་མི་འགྱུར་བའོ། །

[Block 2749]
བདེན་པ་དང་། གཏོང་བ་དང་། ཉེ་བར་ཞི་བ་དང་། ཤེས་རབ་ཅེས་སྨོས་པ་ནི་བྱིན་གྱི་རླབས༌[^1735]བཞི་གཟུང་ངོ་། །དེ་དག་སྨོས་པས་ནི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་གཟུང་སྟེ། ཅི་ལྟ༌[^1736]ཞེ་ན། བདེན་པ་སྨོས་པས་ནི་ཚུལ་ཁྲིམས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་གཟུང་སྟེ། བདེན་པ་གཙོ་བོའི་ཕྱིར་རོ། །

[Block 2750]
ཚུལ་ཁྲིམས་གཟུང་ཡང་ཚུལ་ཁྲིམས་ལ་དྲན་པ་ཉམས་པར་གྱུར་ན་དེའི་ཉེས་པས་ལྟུང་བར་འགྱུར་ཏེ། བདེན་པ་མེད་པས་ཆོས་བཞིན་དུ་གསོ་བར་མི་ནུས་ཏེ། ཚུལ་ཁྲིམས་ཀྱིས་ཕོངས་པར་འགྱུར་རོ། །

[Block 2751]
དེས་ན་དེ་གཙོ་བོ་ཡིན་ནོ། །

[Block 2752]
གཏོང་བ་སྨོས་པས་ནི་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་གཟུང་ངོ་། །ཉེ་པར་ཞི་བ་སྨོས་པས་ནི་བཟོད་པ་དང་བསམ་གཏན་གྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་གཟུང༌[^1737]ངོ་། །ཤེས་རབ་སྨོས་པས་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་གཟུང་ངོ་། །བརྩོན་འགྲུས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ནི་ཐམས་ཅད་ཀྱི་རྗེས་སུ་འབྲང་བའི་ཕྱིར་མ་སྨོས་ཀྱང་གཟུང་བར་བྱའོ། །

[Block 2753]
[^1738]སོགས་པའི་སྒྲས་ནི་བསྡུ་བའི་དངོས་པོ་ལ་སོགས་པ་ཐེག་པ་ཆེན་པོ་ལས་བཤད་པ་གཞན་དག་ཀྱང་མ་ལུས་པར་གཟུང༌[^1739]ངོ་། །ཡོན་ཏན་ཁྱད་པར་ཅན་ཞེས་བྱང་ཆུབ་སེམས་དཔའི་ཡོན་ཏན་ཁྱད་པར་ཅན༌[^1740]དག་ཀྱང་བསྟན་ཏོ། །

[Block 2754]
མངོན་སུམ་གྱི་སྒྲ་ནི་ཆོས་དང་འདུལ་བ་གཉིས་དང་སྦྱར་རོ། །

[Block 2755]
སྐྱེ་དགུ་རྣམས་ལ་ཕ་དང་འདྲ་བར་ཕན་འདོགས་པར་བྱེད་དོ་ཞེས་བྱ་བ་དེ་ཡང་ཇི་ལྟར་སྐྱེ་དགུ་རྣམས་ལ་ཕ་དང་འདྲ་བར༌[^1741]ཕན་འདོགས་པར་གྱུར་ཅེ་ན། དེ་ཉིད་བསྟན་པའི་ཕྱིར།

[Block 2756 [VERSE]]
ཉེས་པར་སྤྱོད་ལས་རྣམ་པར་བཟློག་པ་དང་། །
ཞེས་བྱ་བའི་ཚིགས་བཅད་བརྩམས་པ་ཡིན་ནོ། །
རྣམ་པར་བཟློག་པ་ནི་རྣམ་པར་འདུལ་བའོ། །

[Block 2757]
འཇིག་རྟེན་གར་ཞེས་བྱ་བ་ནི་འཇིག་རྟེན་འདི་དང་འཇིག་རྟེན་ཕ་རོལ་ཏུ་ཡོན་ཏན་དང་སྐྱོན་ལ་འཇུག་པ་དང་ལྡོག་པའི་རྒྱུར་གྱུར་པ་སྟེ། གཅིག༌[^1742]ན་ཡང་ཕ་དང་འདྲ་བ་སྟེ། ཆོས་མངོན་སུམ་དུ་གྱུར་པ་བཞིན་དུའོ། །

[Block 2758]
སྐྱེ་དགུ་རྣམས་ལ་ཕ་དང་འདྲ་བར་ཕན་འདོགས་པར་གྱུར་ཏེ་ཞེས་བྱ་བའི་དབང་དུ་བྱས་ནས། ནང་གི་མི་དང་འདྲ་བར་སྙོམས་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ཏེ། ནང་གི་མི་དང་ཕྱིའི་མི་ལ་ཆོས་དང་རྗེས་སུ་མཐུན་པའི་ཕྱིར་རོ། །

[Block 2759]
བཀའ་ཁྲིམས་ནི་ཆོས་མ་ཡིན་པའི་ལམ་གཅོད་པར་བྱེད་པ་ཡང༌[^1743]ཡིན་ཏེ། མངོན་སུམ་དུ་ཆོས་བཞིན་དུ་གྱུར་པ་ཡིན་ནོ། །

[Block 2760]
ཐེམ་སྐས་རིམ་པ་བཞིན་ཞེས་བྱ་བ་ནི། མངོན་པར་མཐོ་བ་ཡང་དག་པར་ཐོབ་པ་ཡིན་ནོ། །

[Block 2761]
ཚིག་སྔ་མ་ནི་མཐོང་བའི་ཆོས་ཀྱི་ཡོན་ཏན་དང་ཉེས་པ་ལས༌[^1744]འཇུག་པ་དང་། ལྡོག་པའི་རྒྱུས་ཕ་དང་འདྲ་བར་སྟོན་པ་ཡིན་ནོ། །

[Block 2762]
འདིས་ནི་འཇིག་རྟེན་ཕ་རོལ་གྱི་ཆོས་དང་ཆོས་མ་ཡིན་པ་ལ་འཇུག་པ་དང་། ལྡོག་པའི་རྒྱུས་མངོན་སུམ་ཆོས་དང་འདྲ་བར་བསྟན་པ་ཡིན་ནོ། །

[Block 2763]
མངོན་སུམ་འདུལ་བ་བཞིན་དུ་སྐྱེ་དགུ་རྣམས་ལ་ཕན་འདོགས་པར་གྱུར་ཏོ་ཞེས་བསྟན་པ་དེའི་དབང་དུ་བྱས་ནས། འཇིག་རྟེན་ཕན་པ་ཆོས་ལྡན་དེ་མཐོང་ནས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ཏེ། ལྡན་པ་ནི་དེ་དང་ལྡན་པས་ན་ལྡན་པའོ། །

[Block 2764]
ཆོས་དང་ལྡན་པའི་ཕན་པ་གང་ཡིན་པ་དེ་ནི་འཇིག་རྟེན་པའོ། །

[Block 2765]
ཆོས་དང་ལྡན་པ་ནི་རྩེ་གཅིག་ཏུ་སྤྱོད་པ་སྟེ། ཆོས་ཉིད་འབའ་ཞིག་སྤྱོད་ཅེས་པའོ། །

[Block 2766]
ཆོས་ཀྱི་ལམ་ནི་ཆོས་ཀྱི་ལམ་ཉིད་དོ། །

[Block 2767]
[^1745]ཆོས་ཀྱི་ལམ་འདུལ་བ་སྟེ། དེས་བསྐྱེད་པའི༌[^1746]ཆོས་ཀྱི་ལམ་གང་ཐོབ་པའོ། །

[Block 2768]
ཆོས་དེ་ལ་གནོད་པ་བྱས་པ་ནི་འདུལ་བ་ལ་གནོད་པ་བྱས་པས་ན་ཆོས་ལ་གནོད་པ་བྱས་པའོ། །

[Block 2769]
ཇི་ལྟར་བསྟན་པའི་རིམ་པ་བཞིན་དུ་ངེས་པར་བསྟན་པ་སྟེ། གསུམ་པོ་འདི་དག་གིས་ནི་འཇིག་རྟེན་འདི་དང་ཕ་རོལ་གཉི་ག་ལ་ཕན་པར་འཇུག་པའི་དབང་དུ་བྱས་པ་སྟེ། སྔར་བསྟན་པ་བཞིན་དུ་རིམ་པས་དགོད་དོ། །

[Block 2770]
དཔལ་མོ་གཟུགས་དང་ལྡན་པ་བཞིན། །ཞེས་བྱ་བ་ནི་གཟུགས་གཟི་མདངས་མཆོག་དང་ལྡན་པས་སོ། །
--- END BLOCKS ---
