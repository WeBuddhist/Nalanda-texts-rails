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
[Block 841 [VERSE]]
ཐ་སྙད་ཡིན་ཕྱིར་གཉིས་ཀ་ལའམ། །
གང་ཡང་རུང་བ་ལ་བཟློག་པའམ། །
ཐེ་ཚོམ་ཆོས་གྲུབ་འདོད་མ་ཡིན། །

[Block 842]
འདིར་གཉིས་ཀ་ལ་ཕྱིན་ཅི་ལོག་ཏུ་གྲུབ་པ་ནི། དོན་གྱི་ཤུགས་ཀྱིས་གཏན་ཚིགས་ཉིད་དུ་མི་འདོད་དེ། དཔེར་ན་སྒྲ་མི་རྟག་སྟེ། མིག་གི་གཟུང་བྱ་ཡིན་པའི་ཕྱིར་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 843]
གང་ཡང་རུང་བ་ལ་སྟེ་གཅིག་ཏུ་ཕྱིན་ཅི་ལོག་ཏུ་ཡང༌[^641]གྲུབ་པ་ནི་དཔེར་ན་མངོན་པར་གསལ་བར་སྨྲ་བ་ལ་བྱས་པ་ཉིད་ལྟ་བུའོ། །

[Block 844]
གཉིས་ཀའམ་གང་ཡང་རུང་བ་ལ་ཐེ་ཚོམ་དུ་གྱུར་པ་ནི་དཔེར་ན་དུད་པ་ཉིད༌[^642]ཐེ་ཚོམ་ཟ་བ་ལས་མེ་སྒྲུབ་པ་ལྟ་བུའོ། །

[Block 845]
ཆོས་གྲུབ་པ་ནི་དཔེར་ན་བདེ་བ་ལ་སོགས་པ་ཐམས་ཅད་ཡོད་པའི་ཕྱིར་བདག་ཁྱད་པར་ཡོད་དོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 846]
འདི་ལའང་ཕྱོགས་ཀྱི་ཆོས་ཉིད་དུ། །མི་འདོད་ཐམས་ཅད་སུན་འབྱིན་དུའང་། །

[Block 847]
འདི་ལྟར་ཅིག་ཤོས་སུ་གཉིས་ཀར་རབ་ཏུ་གྲུབ་ན་ནི། སུན་འབྱིན་པའམ༌[^643]གྲུབ་པ་ཡིན། །གང་ཞིག་གཉིས་ཀ་ལ་རབ་ཏུ་གྲུབ་པའི་ཕྱོགས་ཀྱི་ཆོས་མ་ཡིན་པ་ནི་དཔེར་ན་མིག་གི་གཟུང་བྱ་ཉིད་ལྟ་བུ་སྟེ་དེ་ནི་སུན་འབྱིན་པའོ། །

[Block 848]
སྒྲུབ་པ་ནི་དཔེར་ན་རྐྱེན་གྱི་བྱེ་བྲག་གིས༌[^644]ཐ་དད་པའི་ཕྱིར་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 849]
གཞན་ནི་འདི་ལྟར༌[^645]སྒྲུབ་པ་མ་ཡིན། སུན་འབྱིན་པ་ཡང་མ་ཡིན་པས་དེར་གང་གིས་རྟོགས་པ་བསྐྱེད། གཞན་གྱིས་སླར་ཡང་བསྒྲུབས༌[^646]ན་འདོད། །གལ་ཏེ་ཕྱོགས་ཀྱི་ཆོས་ཉིད་དུ་བསྒྲུབས་ན་དེ་སྒྲུབ་བྱེད་ཡིན་ཞིང་ཅི་སྟེ་ཕྱོགས་ཀྱི་ཆོས་མ་ཡིན་པ་ཉིད་དུ་བསྒྲུབས་ན་དེ་སུན་འབྱིན་པ་ཡིན་ནོ། །

[Block 850]
ཕྱོགས་ཀྱི་ཆོས་ཀྱི་སྒྲུབ་པ་ཉིད་ནི།

[Block 851 [VERSE]]
ཆོས་ཅན་ཆོས་ཅན་གྱིས་སྒྲུབ་མིན། །
ཆོས་དེས་ཆོས་ཀྱང་མ་ཡིན་གྱི། །
འདི་ལྟར་ཆོས་ཀྱི༌[^647]ཆོས་སྒྲུབ་ཅིང་། །
སྒྲུབ་ཕྱིར་ཆོས་ཅན་ཡང་དེ་བཞིན། །

[Block 852]
དེ་ལ་རེ་ཞིག་གང་དག་འདི་སྐད་དུ་དུད་པས་མེ་སྒྲུབ་པ་ནི་ཆོས་ཅན་གྱི༌[^648]ཆོས་ཅན་སྒྲུབ་པའོ་ཞེས་ཟེར་རོ། །

[Block 853]
དེ་ཡང་རིགས་པ་མ་ཡིན་ཏེ། དེ་ལ་མེའི་ཡོད་པ་རྟོགས་པ་ནི་མ་ཡིན་གྱི་འདི་ལའོ་ཞེས་རྗོད་པར༌[^649]བྱེད་དོ། །

[Block 854]
གལ་ཏེ་དེར་དུད་པ་དང་འབྲེལ་བ་བསྒྲུབ་བྱར་བྱེད་ན་ནི་དམ་བཅའ་བའི་དོན་གྱི་ཕྱོགས་གཅིག་གཏན་ཚིགས་སུ་འགྱུར་རོ། །

[Block 855]
རྗེས་སུ་དཔག་པར་བྱ་བ་དུ་བ་ལ་མེ་མཐོང་བར་ཡང་རིགས་པ་མ་ཡིན་ཏེ། རྗེས་སུ་དཔག་པ་མེད་པར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 856]
དེའི་ཕྱིར་འདི་ལའོ་ཞེས་གདོན་མི་ཟ་བར་ས་ཕྱོགས་ཁས་བླང་བར་བྱ་སྟེ། དེ་ཡང་ཆོས་ཅན་ཉིད་ཡིན་ནོ། །

[Block 857]
འདིར་ཡོན་ཏན་དང་ཡོན་ཏན་ཅན་ཉིད་ཀྱི་ཚུལ་ནས་ཆོས་དང་ཆོས་ཅན་གྱི་རྣམ་པར་གཞག་པ༌[^650]བྱེད་པ་ནི་མ་ཡིན་ནོ། །

[Block 858]
དེ་ལྟར་ན་རེ་ཞིག་ཆོས་ཅན་གྱིས༌[^651]ཆོས་ཅན་བསྒྲུབ་པར་བྱ་བ་ཡང་མ་ཡིན་ནོ། །

[Block 859]
ཆོས་ཅན་གྱི་ཆོས་ཅན༌[^652]བསྒྲུབ་པར་བྱ་བ་ཡང་མ་ཡིན་ནོ་ཞེས་བརྗོད་པར་བྱ་སྟེ། དེ་ལ་གང་དག་མེས་རེག་བྱ་བསྒྲུབ་པར༌[^653]བྱེད་དོ་ཞེས་ཟེར་རོ། །

[Block 860]
དེ་ནི་རིགས་པ་མ་ཡིན་ཏེ། འདི་ལའོ་ཞེས་བརྗོད་པའི་ཕྱིར་སྔར་བཞིན་ནོ། །

[Block 861]
གལ་ཏེ་རེ་ཞིག་རིགས་པ་ཉིད་ཡིན་ཏེ། དུ་བ་ཐམས་ཅད་ལ་མེ་མ༌[^654]མཐོང་བའི་ཕྱིར་རོ། །

[Block 862]
ས་ཕྱོགས་ཀྱི་བསྒྲུབ་བྱ་ཉིད་ཡིན་ཡང་མེའི་བྱེ་བྲག་དྲོ་བ་བསྒྲུབ་བྱ་ཡིན་པའི་ཕྱིར་ས་ཕྱོགས་བརྟགས་པ་དོན་མེད་དོ། །

[Block 863]
དམ་བཅའ་བའི་ཕྱོགས་གཅིག་གི་གཏན་ཚིགས་མ་ཡིན་ཏེ། མེའི་བྱེ་བྲག་བསྒྲུབ་བྱ་ཡིན་པའི་ཕྱིར་དང་། སྤྱི་གཏན་ཚིགས་ཡིན་པའི་ཕྱིར་རོ་ཞེ་ན། མེའི་བྱེ་བྲག་བསྒྲུབ་བྱ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ས་ཕྱོགས་ཀྱི༌[^655]ཁྱད་པར་བྱས་པའི་དུ་བའི་བསྒྲུབ་བྱ་ཉིད་དུ་ཁས་བླང་བར་བྱའོ། །

[Block 864]
དེར་ས་ཕྱོགས་ཀྱི་བྱེ་བྲག་ལ་ཅིའི་ཕྱིར་ཞེ་སྡང་། མེའི་བྱེ་བྲག་ལ་གང་གིས་ན་ངོ་སྲུང་བར་བྱེད། གང་དག་ཆོས་ཀྱི༌[^656]ཆོས་མི་བསྒྲུབ༌[^657]ཅིང་ཆོས་ཅན་ཡང་མི་སྒྲུབ་པོ༌[^658]ཞེས་སྨྲ་བ་ནི། དཔེར་ན་གཙོ་བོ་གཅིག་ཡོད་དེ་ཐ་དད་རྣམས་དང་རྗེས་འགྲོ་མཐོང་བའི་ཕྱིར་ཞེས་པ༌[^659]ལྟ་བུའོ། །

[Block 865]
དེར་ནི་ཐ་དད་པ༌[^660]ཉིད་རྒྱུ་གཅིག་པ་ཉིད་དུ་བསྒྲུབ་པར་བྱ་བ་དང་།[^661] འདི་ལྟར་གྱོ་དུམ་ལ་སོགས་པ་རྒྱུ་གཅིག་པ་ཉིད་དུ་དཔེར་བརྗོད་པ་བཞིན་ནོ། །

[Block 866]
དེའི་ཕྱོགས་ཆོས་གཞན་ཉིད་བསྒྲུབ་པར་བྱ་བ་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན། སྒྲུབ་ཕྱིར་ཆོས་ཅན་ཡང་དེ་བཞིན། །དེ་བཞིན་ཞེས་བྱ་བ་ནི་ཆོས་གཞན་པོ་དེས་ཁྱད་པར་དུ་བྱ་བའི་ཆོས་ཅན་བསྒྲུབ་བྱར་བསྟན་པ་སྟེ། གང་གི་ཕྱིར་དེ་ལྟ་ཡིན་པ་དེའི་ཕྱིར། གཏན་ཚིགས་ཀྱི་ཆོས་དང་བསྒྲུབ་པར་བྱ་བའི་ཆོས་མེད་ན་མི་འབྱུང་བར་བསྒྲུབ་པ༌[^662]ཡིན་ནོ། །

[Block 867]
གཞན་གྱིས༌[^663]སྦྱོར་བའི་དོགས་པ་བསུ་བའི་ཕྱིར་སྨྲས་པ།

[Block 868 [VERSE]]
དམ་བཅའ༌[^664]རྟགས་ཀྱི་ངག་གིས༌[^665]གང་། །
མི་འདོད་པ་ལ་ཐལ་བ་རྩོམ། །
དེ་ནི་ལན༌[^666]ཞེས་ཤེས་བྱ་སྟེ། །
དེ་ཡི་སྒོ་ནས་སྦྱོར་ཕྱིར་རོ། །

[Block 869]
དཔེར་ན་སྒྲ་རྟག་པ་མ་ཡིན་ཏེ། ལས་རྟག་པར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རམ། རྟག་ཏུ་དམིགས་པར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 870]
ཕྱོགས་ཀྱི་ཆོས་དེ་ཡང་གཏན་ཚིགས་ཉིད་དུ།

[Block 871 [VERSE]]
གཏན་ཚིགས་བསྒྲུབ་བྱའི་རྗེས་འགྲོ་གང་། །
མེད་ལ་མེད་པར་བརྗོད་པར་བྱ། །
དེར༌[^667]ནི་ལྔ་པའི་མཐའ་ཅན་དཔེ། །

[Block 872]
འདི་ལྟ་སྟེ་དཔེར་ན་སྒྲ་མི་རྟག་སྟེ། བྱས་པ་མི་རྟག་པའི་ཕྱིར་ཞེས་པའམ། རྟག་སྟེ་མ་བྱས་པའི་ཕྱིར་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 873]
འདི་ལ་ཕྱོགས་ཀྱི་ཆོས་ཉིད་དུ་ནི༌[^668]ཡོད་པ་མ་ཡིན་གྱི། དཔེའི་མཚན་ཉིད་དུ་ཡོད་པ་མ་ཡིན་པས་ན།[^669] རྟགས་ནི་ཉེ་བར་སྦྱར་ལས་འདོད། །འདིར་ཕྱོགས་ཀྱི་ཆོས་ནི་ཉེ་བར་སྦྱར་བ་ལས་བསྟན་པར་བྱ་སྟེ། དེ་ལྟ་བུ༌[^670]ཡང་། སྒྲ་བྱས་སོ་ཞེས་པའམ་མ་བྱས་པ༌[^671]མ་ཡིན་ནོ་ཞེས་པ་བཞིན་ནོ། །

[Block 874]
གང་དུ་བསལ་འོངས་ཀྱིས་བརྗོད་ན།

[Block 875 [VERSE]]
གཏན་ཚིགས་མེད་པར་འགྱུར་བ་ནི། །
དཔེ་གཉིས་ལས་དེ་གྲུབ་ཕྱིར་རོ། །

[Block 876]
གང་ཡང་བསལ་ཏེ་འོངས་པས་བརྗོད་ན་ནི་གཏན་ཚིགས་མེད་པར་ཐལ་བར་འགྱུར་བས༌[^672]བརྗོད་པར་བྱའོ། །

[Block 877]
དེ་བསལ་བ་ལས་སྐྱེ་བ་ནི་མ་ཡིན་ཏེ། རྒྱུ་ལ་མེད་པས་ན་ཐ་དད་དུ་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 878]
དེ་ལ་མེད་པ་སྔོན་དུ་སོང་བ་ཅན་གྱི་ཐ་དད་དམིགས་པར་འགྱུར་ན་ནི་རྗེས་སུ་འགྲོ་བ་དམིགས་པར་མི་འགྱུར་ཏེ། ཕྱིན་ཅི་ལོག་ཏུ་སྒྲོ་འདོགས་པ༌[^673]མི་འདོད་པར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 879]
འདི་ལྟར་གང་གི་ཕྱིར་རྗེས་སུ་འགྲོ་བ་གཅིག་སྔོན་དུ་འགྲོ་བ་ཅན་ནི་མཐོང་ཞིང་དེ་མེད་པ་ལ་མ་མཐོང་བ་དེས་ན་གཅིག་སྔོན་དུ་སོང་བ་ཅན་ནོ། །

[Block 880]
དེ་ཁས་མི་ལེན་ཡང་རྗེས་སུ་འགྲོ་བ་མེད་པར་ཐལ་བར་འགྱུར་རོ། །
--- END BLOCKS ---
