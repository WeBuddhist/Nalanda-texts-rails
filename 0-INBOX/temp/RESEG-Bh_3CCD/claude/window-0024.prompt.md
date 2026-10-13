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
ཨོཾ་དངོས་པོ་ཐམས་ཅད་ལས་འདས་ཤིང་། །
ཕུང་པོ་ཁམས་དང་སྐྱེ་མཆེད་བྲལ། །
གཟུང་དང་འཛིན་པ་རྣམ་སྤངས་པ། །
ཆོས་རྣམས་བདག་མེད་མཉམ་ཉིད་ཀྱིས། །

[Block 842 [VERSE]]
རང་སེམས་གདོད་ནས་མ་སྐྱེས་པ། །
སྟོང་པ་ཉིད་ཀྱི་ངོ་བོ་ཡིན། །

[Block 843]
ཞེས་བྱ་བ་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་སྔགས་འདི་བརྗོད་ཅིང་། བླ་མའི་ཞབས་ཀྱི་རྩ་བར་སྙིམ་པའི་མེ་ཏོག་དབུལ་བར་བྱའོ་ཞེས་འདི་ནི་ནང་གི་མངོན་པར་བྱང་ཆུབ་པའི་རིམ་པའོ། །

[Block 844]
དེའི་དཔེ་ནི་ཉིན་མོ་སྣང་བ་མཆེད་པའི་ཡེ་ཤེས་སོ། །

[Block 845]
མཚན་མོ་ནི༌[^580]སྣང་བའི་ཡེ་ཤེས་སོ། །

[Block 846]
ནུབ་ཀྱི་དུས་ཀྱི་མཚམས་ནི་སྣང་བ་ཐོབ་པའི་ཡེ་ཤེས་སོ། །

[Block 847]
སྐྱ་རེངས་ཀྱི་དུས་སུ་བཞི་པ་འོད་གསལ་བའི་ཡེ་ཤེས་ཏེ་ཕྱིའི་མངོན་པར་བྱང་ཆུབ་པའི་རིམ་པའོ། །

[Block 848 [HEADING]]
###### ནང་གི་མངོན་པར་བྱང་ཆུབ་པ། ^1-2-4-1-2-0

[Block 849]
རིམ་པ་འདིས་ཀྱང་ནང་གི༌[^581]མངོན་པར་བྱང་ཆུབ་པའི་རིམ་པ༌[^582]བསྟན་པ་ཡིན་ཏེ། དཔེར་ན། སྨིག་རྒྱུ་དང་། དུ་བ་དང་། མཁའ་སྣང༌[^583]དང་། མར་མེ་དང་། སྤྲིན་མེད་པའི་ནམ་མཁའ་དང་འདྲ་བའི་རྟགས་རྣམ་པ་ལྔའོ། །

[Block 850]
ཇི་སྐད་དུ།

[Block 851]
ལས་ཀྱི་མཐའ་རྣམ་པར་འབྱེད་པ་ལས།

[Block 852 [VERSE]]
དང་པོ་ས་ནི་ཆུར་ཐིམ་ཞིང་། །
ཆུ་ནི་མེ་ལ་ཐིམ་པར་འགྱུར། །
མེ་ནི་རླུང་གི་རྗེས་འགྲོ་ཞིང་། །
རླུང་ནི་ནམ་མཁར༌[^584]ཡང་དག་འཇུག །

[Block 853 [VERSE]]
ནམ་མཁའ་འཛིན་པ༌[^585]དེ་ཉིད་དེ། །
ཡེ་ཤེས་གསུམ་པོ་རྣམ་སྤངས་པའོ། །

[Block 854]
ཞེས་འབྱུང་ངོ་། །ཡང་ན་དམ་ཚིག་གི༌[^586]ཕྱག་རྒྱའི་སྒོ་ནས་ཕྱིའི་མངོན་པར་བྱང་ཆུབ་པ་དང་། ཡེ་ཤེས་ཀྱི་ཕྱག་རྒྱ་དང་ཕྱག་རྒྱ་ཆེན་པོའི་སྒོ་ནས་ནི་ནང་གི་མངོན་པར་བྱང་ཆུབ་པར་ཤེས་པར་བྱའོ། །

[Block 855 [HEADING]]
##### ཏིང་ངེ་འཛིན་གྱི་མངོན་པར་བྱང་ཆུབ་པ། ^1-2-4-2-0

[Block 856]
རིམ་པ་དེ་དག་གིས༌[^587]དེ་ཁོ་ན་ཉིད་རྟོགས་པའི་རྣལ་འབྱོར་པས་བརྟན་པར་བྱ་བའི་ཕྱིར་ཏིང་ངེ་འཛིན་རྣམ་པ་གཉིས་ཀྱིས་ཀྱང་དེ་བཞིན་ཉིད་ལ་འདུན་པར་བྱའོ། །

[Block 857 [HEADING]]
###### རིལ་པོ་འཛིན་པ། ^1-2-4-2-1-0

[Block 858]
དེ་ལ་ལྟེ་བའི་ཕྱོགས་སུ་རྩིབས་བརྒྱད་པའི་ཆོས་ཀྱི་འཁོར་ལོའི་དཀྱིལ་འཁོར་དུ་མེའི་འོད་འཕྲོ་བའི་ཡི་གེ་རཾ་འབར་བ་བསྒོམས་ཏེ། དེའི་སྣང་བས་སྤྱི་བོ༌[^588]ནས་ལུས་མ་ལུས་པ་ལ་ཁྱབ་པར་བྱ་སྟེ། སྟོང་པ་ཉིད་ཀྱི་རང་བཞིན་འོད་གསལ་བར༌[^589]གནས་པར་བྱའོ་ཞེས་རིལ་པོར་འཛིན་པ་ཞེས་བྱ་བའི་ཏིང་ངེ་འཛིན་ཏོ། །

[Block 859 [HEADING]]
###### རྗེས་སུ་གཞིག་པ། ^1-2-4-2-2-0

[Block 860]
དེ་བཞིན་དུ་ཡང་བརྟན་པ་དང་གཡོ་བའི་རང་བཞིན་ཁམས་གསུམ་པོ་དང་པོ་འོད་གསལ་བར་བྱ་སྟེ། ཕྱིས་དེ༌[^590]བཞིན་དུ་བདག་ཉིད་ལ་བྱ་བ་ནི་རྗེས་སུ་གཞིག་པའི་ཏིང་ངེ་འཛིན་ཏོ། །

[Block 861]
ཏིང་ངེ་འཛིན་གཉིས་ཀྱི་དཔེ་ནི་ཇི་སྐད་དུ། །ཆུ་བོའམ་ལྟེང༌[^591]ཀའི་ཆུ་ནི་དྲི་མེད་དག་ལ་ཟླ་བ་གནས་པ་ལྟར། །དེ་བཞིན་དེ་ལ་རྗེས་སུ་འཇིག་པར་བྱེད་པ་རྣལ་འབྱོར་པས་ནི་རྟག་ཏུ་བསམ། །མེ་ལོང་ལ་ནི་དབུགས་རླུང་རིམ་གྱིས་ཟད་འགྱུར་དེ་བཞིན་ཡང་དག་བལྟ། །རིལ་པོར་འཛིན་པའི༌[^592]རིམ་པ་འདི་ཡང་རྣལ་འབྱོར་པ་ཡིས༌[^593]རྟག་ཏུ་བརྟག །ཅེས་འབྱུང་ངོ་། །མངོན་པར་བྱང་ཆུབ་པའི་རིམ་པས༌[^594]འདིས་ཡེ་ཤེས་ལྔའི་ངོ་བོ་ཉིད་རྣམ་པར་རྟོག་པ་མ་ལུས་པ་རིང་དུ་སྤངས་པ་མཆོག་ཏུ་དགའ་བའི་རང་བཞིན་རྣལ་འབྱོར་པ་གསོན་བཞིན་གྲོལ་བར་གནས་པར་བྱའོ་ཞེས་མངོན་པར་བྱང་ཆུབ་པའི་རིམ་པའོ། །

[Block 862]
[^595]

[Block 863 [HEADING]]
#### ཟུང་དུ་འཇུག་པའི་རིམ་པ། ^1-2-5-0

[Block 864]
ད་ནི་ཟུང་དུ་འཇུག་པའི་རིམ་པ་བསྟན་པར་བྱ་སྟེ། དེ་ཡང་གཉིས་སོ། །

[Block 865]
རྒྱུའི་ཟུང་དུ་འཇུག་པ་དང་། འབྲས་བུའི་ཟུང་དུ་འཇུག་པའོ། །

[Block 866 [HEADING]]
##### རྒྱུའི་ཟུང་དུ་འཇུག་པ། ^1-2-5-1-0

[Block 867]
རྒྱུའི་ཟུང་དུ་འཇུག་པ་ལ་རྣམ་པ་བཞི་སྟེ། ཉན་ཐོས་དང་། རང་སངས་རྒྱས་དང་། དབུ་མ་དང་། སྔགས་ཀྱི་ལྟ་བའི་བྱེ་བྲག་གིས་སོ། །

[Block 868]
དེ་ལ་རིམ་པ་བཞི་པོ་འོད་གསལ་བ་ཐོབ་ནས་དེའི་རྗེས་སུ་ཀུན་རྫོབ་དང་དོན་དམ་པ༌[^596]དབྱེར་མེད་པ་དཔལ་རྡོ་རྗེ་འཆང་ཆེན་པོའི་ཕྱག་རྒྱ་ཆེན་པོ༌[^597]རྣམ་པ་ཐམས་ཅད་ཀྱི་མཆོག་དང་ལྡན་པ། སེམས་ཅན་མ་ལུས་པའི་དོན་བྱེད་པ་མྱུར་དུ་སྤྲོས་ཏེ་གཉིས་པ་ཐམས་ཅད་ཀྱི་སྣང་བ་དང་བྲལ་ཞིང་། བླ་ན་མེད་པའི་སྐུ་ཐོབ་པར་འགྱུར་ཞེས་ཟུང་དུ་འཇུག་པའི་ཏིང་ངེ་འཛིན་མདོར་བསྡུས་པའོ། །

[Block 869]
དེ་ལ་ནི་ལྷག་མ་དང་བཅས་པ་དང་ལྷག་མ་མེད་པའི་མྱ་ངན་ལས་འདས་པའི་དབྱིངས་གཉིས་ཀྱི་རྣམ་པར་རྟོག་པ་དང་། གང་ཟག་ལ་བདག་མེད་པ་དང་ཆོས་ལ་བདག་མེད་པ་ཉིད༌[^598]དང་། འདུ་ཤེས་མེད་པའི་སྙོམས་པར་ཞུགས་པ་དང་འགོག་པའི་སྙོམས་པར་ཞུགས་པ་དང་། རྣམ་པ་དང་བཅས་པ་དང་། རྣམ་པ་མེད་པ་དང་། རྟག་པ་དང་ཆད་པ་དང་། ཀུན་རྫོབ་དང་། དོན་དམ་པ་དང་། རྟག་པ་དང་། མི་རྟག་པ་དང་། གཙང་བ་དང་མི་གཙང་བ་དང་། ཡོད་པ་དང་མེད་པ་དང་། དངོས་པོ་དང་དངོས་པོ་མེད་པ་དང་། སྔགས་ཀྱི་སྐུ་དང་། ཡེ་ཤེས་ཀྱི་སྐུ་དང་། བསྐྱེད་པ་དང་། རྫོགས་པ་དང་། རྟོག་པའི་རྣལ་འབྱོར་དང་། ཡོངས་སུ་རྫོགས་པ་དང་། སྟོང་པ་ཉིད་དང་སྙིང་རྗེ་དང་། ཐབས་དང་ཤེས་རབ་ལ་སོགས་པའི་གཉིས་པར་འཛིན་པའི་བག་ཆགས་ཐམས་ཅད་མེད་པས་བཅུ་གཉིས་པ་ཀུན་ཏུ་འོད་ཅེས་བྱ་བ་ལ་གནས་པའོ། །

[Block 870 [HEADING]]
##### འབྲས་བུའི་ཟུང་དུ་འཇུག་པ། ^1-2-5-2-0

[Block 871]
དེ་བས་ན་དེ་ལས་ལྡང་བའི་དག་པ་འཇིག་རྟེན་པའི་ཡེ་ཤེས་ལ་གནས་པ་ས་བཅུ་གསུམ་པ་ཐོབ་པ༌[^599]ཡོངས་སུ་རྫོགས་པའི་སྤྱོད་པ་ཟུང་དུ་འཇུག་པའི་ངོ་བོ་ཉིད་དོ། །

[Block 872]
དཔེར་ན་བྲམ་ཟེ་དང་གདོལ་པ༌[^600]དང་། སྨད་འཚོང་མ་དང་། བུ་མོ་དང་ཆུང་མ་དང་། ག་བུར་དང་། བཤང་བ༌[^601]དང་། དྲག་པོ་དང་། རྡོ་རྗེ་འཆང་བ་དང་། མཐོ་རིས་དང་ངན་སོང་དང་། བདེ་བ་དང་སྡུག་བསྔལ་བ་དང་། གྲགས་པ་དང་གྲགས་པ་མ་ཡིན་པ་དང་། རྙེད་པ་དང་རྙེད་པ་མ་ཡིན་པ་དང་། བསྟོད་པ་དང་སྨད་པ་ལ་སོགས་པ་དང་བྲལ་བ། རྗེས་སུ་དྲན་པ་དང་མ་འདྲེས་པའི་ཆོས་དང་ལྡན་པ། སངས་རྒྱས་ཀྱི་སྐུ་འཛིན་པ། སངས་རྒྱས་ཀྱི་ཞིང་གཅིག་ནས་གཅིག་ཏུ་སེམས་ཅན་གྱི་དོན་མཛད་པ་ལ་བརྩོན་པ་དཔལ་བདེ་བ་ཆེན་པོའི་རྣམ་གྲངས་ཅན་རྡོ་རྗེ་སེམས་དཔའ་ཉིད་དུ་འགྱུར་རོ། །

[Block 873]
དེ་ལྟ་ན་གལ་ཏེ་འབྲས་བུ་དེ་ཡིན་ན་རྒྱུ་ཉིད་དུ་ཇི་ལྟར་འགྱུར་ཏེ། གང་གི་ཕྱིར་རིམ་པ་བཞི་པོ་ནི་ཐབས་ཏེ་རྒྱུའོ། །

[Block 874]
ལྔ་པ་ནི་མི་སློབ་པའི་ངོ་བོ་ཉིད་འབྲས་བུའོ། །

[Block 875]
དེ་ཅིའི་ཕྱིར་གཅིག༌[^602]ལ་རྒྱུ་ཉིད་དང་འབྲས་བུ་ཉིད་འཐད་ཅེ་ན། སྨྲས་པ་རོ་གཅིག་པའི་ཟུང་དུ་འཇུག་པ་ལ་བློས་བརྟགས་པའི་རྒྱུ་དང་འབྲས་བུའི་ཐ་སྙད་ཡིན་གྱི་དམ་པའི་དོན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 876]
དེ་ལྟར་ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་ཐོབ་པའི་རྣལ་འབྱོར་པ་ལ་རྒྱུ་དང་འབྲས་བུའི་བྱེ་བྲག་ཏུ་གནས་པའི་དངོས་པོ་ཐམས་ཅད་ངོ་བོ་གཅིག་ཁོ་ན་ཡིན་གྱི་བྱེ་བྲག་ཏུ་དེ་ལ་དེ་རྣམས་སྣང་བ་མ་ཡིན་ནོ། །

[Block 877]
བདག་ཅག་ལྟ་བུ་གཞལ་བར་བྱེད་པ་རྣམས་ཀྱིས་དེ་ལྟར་འདོད་པ་ལ་སྐྱོན་མེད་དོ། །

[Block 878]
ཡང་ན་སྲིད་པ་དང་མྱ་ངན་ལས་འདས་པའི་རྣམ་པར་རྟོག་པ༌[^603]ཕན་ཚུན་བྱེ་བྲག་ཏུ་རབ་ཏུ་འཇུག་པ་དེ་རྣམས་ཁོ་ན་རོ་གཅིག་པར་ཤེས་པས་ཏིང་ངེ་འཛིན་མངོན་དུ་འགྱུར་ཞེས༌[^604]རྒྱུ་དང་འབྲས་བུའི་བྱེ་བྲག་འདི་ནི་བརྟགས་པ་ཡིན་པས་གནོད་པ་གང་ཡང་མེད་དོ། །

[Block 879]
དེ་ལྟ་ན་གལ་ཏེ་ཏིང་ངེ་འཛིན་འདི་ཡིན་ན། ཇི་ལྟར་ལྡང་བར་འགྱུར་ཏེ། ལྡང་བ་མེད་ན་དེའི་ཚེ་སེམས་ཅན་གྱི་དོན་མེད་ཅེས་ཕན་ཚུན་འགལ་བ་ཐོབ་པར་འགྱུར་ཞེ་ན། སྨྲས་པ་ལྡང་བ་ཞེས་བྱ་བ་ནི་ཏིང་ངེ་འཛིན་ཉམས་པར་བྱེད་པ་ནི༌[^605]མ་ཡིན་ཏེ། འོན་ཀྱང་ཏིང་ངེ་འཛིན་ལ་ཞུགས་པ་ཉིད་ཀྱིས་འགྲོ་བའི་དོན་མཛད་པའོ། །

[Block 880]
གང་གི་ཕྱིར་སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས༌[^606]ཀྱི་སྤྱོད་ལམ་རྣམ་པ་བཞི་སྟེ། སྤྱོད་ལམ་གྱི་བཞུགས་པ་དང་། བསྟན་པའི་བཞུགས་པ་དང་། ཏིང་ངེ་འཛིན་གྱི་བཞུགས་པ་དང་། སོ་སོར་ཡང་དག་པའི་འཇུག་པའི་བཞུགས་པའོ། །
--- END BLOCKS ---
