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
[Block 1016]
སྐྱེས་བུ་ནི་རྒྱུ་ཡང་མ་ཡིན་འབྲས་བུ་ཡང་མ་ཡིན་ནོ། །

[Block 1017]
ཇི་སྐད་དུ།

[Block 1018 [VERSE]]
རྩ་བའི་རང་བཞིན་བྱ་བ་མ་ཡིན་ཏེ། །
ཆེན་པོ་ལ་སོགས་བདུན་པོ་རྒྱུ་འབྲས་ཡིན། །
བཅུ་དྲུག་པོ་ནི་འབྲས་བུ་ཉིད་ཡིན་ཏེ། །
རྒྱུ་མིན་འབྲས་མིན་སྐྱེས་བུ་དེ་ཡིན་ནོ། །

[Block 1019]
དེའི་དོན་ནི་འདི་ཡིན་ཏེ། ཡོན་ཏན་གསུམ་གྱི་བདག་ཉིད་ཅན་ལུས་ཅན་ཐམས་ཅད་ཀྱི་རྒྱུར་གྱུར་པའི་རང་བཞིན་ནི་གཙོ་བོའོ། །

[Block 1020]
སྙིང་སྟོབས་དང་། རྡུལ་དང་མུན་པ་གསུམ་ནི་ཡོན་ཏན་ནོ། །

[Block 1021]
དེ་ལ་སྙིང་སྟོབས་ནི་ཡང་ཞིང་གསལ་བར་བྱེད་པ་དགེ་བའི་བག་ཆགས་གཙོར་གྱུར་པ་སྟེ་མཐོ་རིས་ཀྱི་རྒྱུའོ། །

[Block 1022]
རྡུལ་ནི་གཡོ་བ་སྟེ་གཡོ་ཞིང་འཆིང་བར་བྱེད་པ་སྟེ་དམྱལ་བའི་རྒྱུའོ། །

[Block 1023]
མུན་པ་ནི་ལྕི་ཞིང་སྒྲིབ་པར་བྱེད་པ་མི་དགེ་བའི་བདག་ཉིད་དམྱལ་བ་ཉིད་ཀྱི་རྒྱུའོ། །

[Block 1024]
ཇི་སྐད་དུ།

[Block 1025 [VERSE]]
སྙིང་སྟོབས་ཡང་ཞིང་གསལ་བར་བྱེད་པར་འདོད། །
རྡུལ་ནི་འཆིང་བྱེད་གཡོ་བ་ཉིད་དུ་བཤད། །
མུན་པ་ལྕི་ཞིང་སྒྲིབ་པར་བྱེད་པ་སྟེ། །
དོན་ལ་མར་མེ་བཞིན་དུ་གནས་པར་འགྱུར། །

[Block 1026]
ཞེས་འབྱུང་ངོ་། །དེ་ལྟར་སྙིང་སྟོབས་ལ་སོགས་པའི་ཡོན་ཏན་གསུམ་རོ་གཅིག་པར་གྱུར་པ། དབང་པོ་ལ་སོགས་པ་རྣམས་ཀྱི་རྒྱུར་གྱུར་པ་རྟག་པའི་རང་བཞིན་ནི་བྱ་བའི་སྒོ་ནས་རྗེས་སུ་དཔག་པར་བྱ་བ་ཡིན་ཏེ་མེ་བཞིན་ནོ། །

[Block 1027]
དེ་ནི་རང་གི་གཟུགས་སུ་དམིགས་པར་མི་འགྱུར་ཏེ། ཕྲ་བའི་ཕྱིར་རོ། །

[Block 1028]
མི་དམིགས་པ་དེ་ཡང་རྣམ་པ་བདུན་དུ་འགྱུར་རོ། །

[Block 1029]
འདི་ལྟ་སྟེ་ཤིན་ཏུ་རིང་བས་ནམ་མཁར་འཕུར་བའི་བྱ་དང་། ཤིན་ཏུ་ཉེ་བས་མིག་གི་དབང་པོའི་རྫི་མ༌[^724]དང་། དབང་པོ་ཉམས་པས་ལོང་བ་ལ་སོགས་པས་གཟུགས་མི་མཐོང་བ་དང་། ཡིད་མི་བརྟན་པས་སྨྱོ་བ་ལ་སོགས་པ་རྣམས་ཀྱིས་དངོས་པོ་མི་མཐོང་བ་དང་ཕྲ་བས་ཕྲ་བ་ལ་སོགས་པ་མི་མཐོང་བ་དང་། ཟིལ་གྱིས་གནོན་པས་རླུང་དང་མཚོན་ཆ༌[^725]ལ་སོགས་པས་སྨས་པ༌[^726]དང་། མཚུངས་པ་དང་ཕྲད་པས་འོ་མ་དང་། ཆུ་དང་ཏིལ་དང་འབྲས་ཆང༌[^727]ལ་སོགས་པའོ།[^728] །

[Block 1030]
འདིར་ནི་རང་བཞིན་ཕྲ་བའི་ཕྱིར་མི་དམིགས་པས་འབྲས་བུས་དཔག་པར་བྱ་བ་ཡིན་ནོ། །

[Block 1031]
ཇི་སྐད་དུ། ཤིན་ཏུ་རིང་བ་དང་ནི་ཤིན་ཏུ་ཉེ་བ་ཡིས། །

[Block 1032 [VERSE]]
དབང་པོ་ཉམས་དང་ཡིད་ནི་མི་གནས་པས། །
ཕྲ་བ་ཉིད་དང་ཟིལ་གྱིས་ནོན་པས་ནི། །
དེ་བཞིན་མཚུངས་པ་ཕན་ཚུན་རྣམས་ཚོགས་པས། །
ཕྲ་ཕྱིར་དེ་ནི་མི་དམིགས་པ་ཉིད་དེ། །

[Block 1033 [VERSE]]
དེ་ནི་མེད་མིན་བྱ་བས་དམིགས་པ་ཡིན། །
བྱ་བ་དེ་ཡང་ཆེན་པོ་ལ་སོགས་ཏེ། །
རང་བཞིན་དང་ནི་འདྲ་དང་མི་འདྲ་ཡིན། །

[Block 1034]
ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 1035]
དེ་ལ་རྒྱུ་དང་འབྲས་བུའི་ཚུལ་ནི་རང་བཞིན་ལས་བློ་དང་། དེ་ལས་ཀྱང་ང་རྒྱལ༌[^729]དང་། དེ་ཉིད་ལས་ཀྱང་བློའི་དབང་པོ་ལྔ་དང་ལས་ཀྱི་དབང་པོ་ལྔ་དང་དེ་ཙམ་ལྔ་དང་ཡིད་ཀྱང་སྐྱེ་བར་འགྱུར་རོ། །

[Block 1036]
དེ་ཙམ་རྣམ་པ་ལྔ་ལས་འབྱུང་བ་ཆེན་པོ་ཡོན་ཏན་གསུམ་གྱི་བདག་ཉིད་སྐྱེ་བར་འགྱུར་ཏེ། ཡང་དང་ཡང་དུ་འཇིག་ཅིང་སླར་ཡང་སྐྱེ་བར་འགྱུར་ཞེས་རྒྱུ་དང་འབྲས་བུའི་ཚུལ་དུ་འཁོར་བ་པ་རྣམས་ཡོངས་སུ་འཁོར་བར་གྱུར་པ་སྟེ་དབྱེར་མེད་པར་ཤེས་པའི་ཕྱིར་རོ། །

[Block 1037]
དབྱེར་ཡོད་པར་ཤེས་པས་རང་བཞིན་དང་སྐྱེས་བུ་དག་ལས་འདི༌[^730]ནི་རང་བཞིན་དང་འདི་ནི་སྐྱེས་བུའོ་ཞེས་པས་གྲོལ་བའོ། །

[Block 1038]
སྐྱེས་བུ་ནི་དྲི་མ༌[^731]མེད་པ་ཤེལ་གྱི་རྣམ་པ་མཐོང་བ་པོ་སྟེ། །བཏང་སྙོམས་པ་ཉིད་ཀྱིས་རང་བཞིན་གྱི༌[^732]སྒོ་ནས་ཐམས་ཅད་མཐོང་བར་བྱེད་དོ། །

[Block 1039]
མཐོང་ནས་ཀྱང་རང་བཞིན་ཁ་དྲག་ཡིན་པས་མཐོང་བར་མི་འགྱུར་ཏེ། དགེ་བ་དང༌[^733]མི་དགེ་བའི་རྒྱུ་གཉིས་ལས་སྐྱེ་བ་དང་། ཚེ་དང་ལོངས་སྤྱོད་ཀྱི་མཚན་ཉིད་ཀྱི་འབྲས་བུ་མྱོང་བར་འགྱུར་རོ། །

[Block 1040]
ཇི་སྐད་དུ།

[Block 1041 [VERSE]]
དགེ་བ་ཡིས་ནི་སྟེང་དུ་འགྲོ་འགྱུར་ཏེ། །
མི་དགེ་བ་ཡིས་འོག་ཏུ་འགྲོ་བར་འགྱུར། །
ཡེ་ཤེས་ཀྱིས་ནི་གྲོལ་བ་ཉིད་འགྱུར་ཞིང་། །
ཕྱིན་ཅི་ལོག་པས་འཆིང་བ་ཉིད་དུ་འདོད། །

[Block 1042]
ཅེས་འབྱུང་ངོ་། །དེ་བས་ན་སྐྱེས་བུ་དུ་མ་ཉིད་དེ། གང་གི་ཕྱིར་གཅིག་ཡིན་ན་སྐྱེས་བུ་གཅིག་གྲོལ་བས་ཐམས་ཅད་གྲོལ་བར་ཐལ་བ་དང་། གཅིག་སྐྱེ་བའམ་འཆི་བས་ཐམས་ཅད་དེ་བཞིན་དུ་ཐལ་བར་འགྱུར་རོ། །

[Block 1043]
རང་བཞིན་ནི་བེམས་པོས་ཀྱང་ལེགས་པ་དང་། མི་ལེགས་པའི་ལས་དག༌[^734]ཏུ་སྐྱེས་བུ་རབ་ཏུ་འཇུག་པར་བྱེད་དེ་འོ་མ་བཞིན་ནོ། །

[Block 1044]
ཇི་སྐད་དུ།

[Block 1045 [VERSE]]
བེའུ་སྐྱེད༌[^735]པར་བྱེད་པའི་རྒྱུ་མཚན་གྱིས། །
བེམས་པོ་འོ་མ་ཇི་བཞིན་འབྱུང་གྱུར་པ། །
དེ་བཞིན་སྐྱེས་བུ་གྲོལ་བའི་ཆེད་དུ་ནི། །
རང་བཞིན་གཙོ་བོས་རབ་ཏུ་འཇུག་པར་བྱེད། །

[Block 1046]
ཅེས་འབྱུང་ངོ་། །དེ་ལྟར་དེ་ཁོ་ན་ཉིད་ཉི་ཤུ་རྩ་གསུམ་རང་བཞིན་དང་ལྷན་ཅིག་ཏུ་བེམས་པོ་ཡིན་ཏེ། ཐ་དད་པ་མེད་པས་འབྱུང་པོ་རྣམ་པ་བཅུ་བཞིའི་འཁོར་བར་ཡོངས་སུ་འཁོར་བར་འགྱུར་རོ། །

[Block 1047]
ཐ་དད་པར་ཡོངས་སུ་ཤེས་པ་ཙམ་གྱིས་གྲོལ་བར་འགྱུར་རོ། །

[Block 1048]
རང་བཞིན་བེམས་པོ་ཡིན་ཡང་སྐྱེས་བུ་དང་འབྲེལ་པའི་དབང་གིས་དངོས་པོ་ཐམས་ཅད་ལ་འཇུག་པ་དང་ལྡོག་པར་བྱེད་དེ་འཕྱེ་བོ་དང་ལོང་བ་བཞིན་ནོ། །

[Block 1049 [VERSE]]
འཕྱེ་བོ་དང༌[^736]ལོང་བའི་འབྲེལ་པ་བཞིན། །
དེ་ཡིས་བྱས་པ་འདི་དག་འགྲོ་བ་ཡིན། །

[Block 1050]
ཞེས་འབྱུང་ངོ་། །བྱེ་བྲག་དེ་ཡང་ཚིག་གི་དོན་དྲུག་ཅུ་ཡོངས་སུ་ཤེས་པས་སྐྱེ་བར་འགྱུར་ཏེ།

[Block 1051 [VERSE]]
གཙོ་བོ་ཡོད་དང་གཅིག་པ་ཉིད། །
དོན་ལྡན་ཉིད་དང་དེ་ལས་གཞན། །
གཞན་དོན་ཉིད་དང་དུ་མ་དང་།
བྲལ་བ་དང་ནི་མ་བྲལ་ཉིད། །

[Block 1052 [VERSE]]
ལྷག་མའི་སྐབས་དང་བྱེད་མིན་ཉིད། །
དོན་ནི་གཙོ་བོ་བཅུ་རུ་བཤད། །

[Block 1053 [VERSE]]
ཕྱིན་ཅི་ལོག་པའི་བྱེ་བྲག་ལྔ་ཡིན་ཏེ། །
བྱེད་པ་མ་ཚང་བས་ནི་མི་ནུས་པ། །
དབྱེ་བ་ཉི་ཤུ་རྩ་བརྒྱད་ཅན་ཞེས་བྱ། །
དགའ་བ་དགུ་དང་དངོས་གྲུབ་རྣམ༌[^737]བརྒྱད་དོ། །

[Block 1054]
ཞེས་མདོར་བསྟན་པའོ། །

[Block 1055]
རྒྱས་པར་བསྟན་པ་ཡང་མུན་པ་དང་གཏི་མུག་དང༌[^738]གཏི་མུག་ཆེན་པོ་དང་། མུན་པ་ཐིབས་པོ་དང་། ཤིན་ཏུ་མུན་ནག་ཐིབས་པོ་ཞེས་ཕྱིན་ཅི་ལོག་པ་ལྔའོ། །
--- END BLOCKS ---
