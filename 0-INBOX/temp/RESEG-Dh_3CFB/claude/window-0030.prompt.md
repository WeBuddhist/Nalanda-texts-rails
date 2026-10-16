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
[Block 1051]
བརྟེན་པ་གཅིག་པོ་གང་ལ་གནས་པ་དེ་ཉིད་ཀྱི༌[^884]ཚེ་བདག་ཉིད་དེས་དེ་ལ་གནས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་དེ་ནི་གཅིག་པོ་དེ་ལ་གནས་པ་དང་མི་གནས་པ་བདག་ཉིད་འགལ་བའི་ཕྱིར། རིགས་པ་མ་ཡིན་ནོ། །

[Block 1052]
གལ་ཏེ་ཐམས་ཅད་ལ་ཐམས་ཅད་དུ་རྣམ་པ་ཐམས་ཅད་ཀྱིས་གནས་པའི༌[^885]བདག་ཉིད་ཅན་ཡིན་ནོ་ཞེ་ན། དེ་ནི་རང་བཞིན་མཐོང་བའི་རྟེན་གྱི་ཤེས་པ་ནི་ཐམས་ཅད་ལ་རྣམ་པ་ཐམས་ཅད་དུ་འགྱུར་ལ། དེ་ལྟར་ན་ཡང་བ་ལང་ལ་ཡང་རྟ་ཡིན་ནོ་ཞེས་ཤེས་པར་འགྱུར་ཏེ། རྟ་ལ་གནས་པའི་བདག་ཉིད་ཅན་གྱི་རྫས་ཉིད་དང་འབྲེལ་པའི་ཕྱིར་དང་། དེའི་རང་བཞིན་རྟོགས་པས་དེ་ལྟར་རྣམ་པར་ངེས་པའི་ཕྱིར་དང་། གཅིག་པོ་དེ་ལ་ཡང་མ་མཐོང་བའི་རྣམ་པ་གཞན་མེད་པའི་ཕྱིར་རོ། །

[Block 1053]
དེའི་ཕྱིར་ཆ་མེད་པ་ཡུལ་དུ་མ་ལ་ཅིག་ཅར་བརྟེན་པ་མ་ཡིན་ནོ། །

[Block 1054]
རྟེན༌[^886]སྔ་མ་སྤངས་ནས་ཀྱང་ཡུལ་ཐ་དད་པ་ལ་གནས་པ་དེ་ཡང་མངོན་པར་འདོད་པ་མ་ཡིན་ནོ། །

[Block 1055 [VERSE]]
གཞན་པ༌[^887]གནས་པར་འགྱུར་བ་ནི། །
རང་གི་གནས་ལས་མི་གཡོ་བ། །
དེ་ལས༌[^888]གནས་གཞན་སྐྱེ་བ་ལ། །
གནས་ཤེས་ཤིན་ཏུ་རིགས་པར་ལྡན། །

[Block 1056 [VERSE]]
གང་དུ་དངོས་དེ་གནས་གྱུར་པ། །
དེ་དང་འབྲེལ་པ་མ་ཡིན་ལ། །
དེ་ཡུལ་དག་ཀྱང་ཁྱབ་བྱེད་པ། །
དེ་ནི་ཤིན་ཏུ་ངོ་མཚར་ཆེ། །

[Block 1057]
ཞེས་བྱ་བ་ནི་བར་སྐབས་ཀྱི་ཚིགས་སུ་བཅད་པའོ། །

[Block 1058]
སྤྱི་ཐམས་ཅད་ན་ཡོད་པར་སྨྲ་བ་གང་ཡིན་པ་དེའི་ཡང་།

[Block 1059 [VERSE]]
གལ་ཏེ་རིགས་ནི་ཀུན་ལ་ཡོད། །
གཅིག་དེ་བསལ་བས་བསལ་བ་ཉིད། །
ཐ་དད་མེད་ཕྱིར་ཀུན་ལ་མཐོང་། །

[Block 1060]
རིགས་རྟག་པའི་བསལ་བ་འགའ་ཞིག་ཀྱང་ཡོད་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་དེ་ནི་བཀག་ཟིན་ཏོ། །

[Block 1061]
དེ་བས་རྟག་ཏུ་གཞན་གྱིས་ལེགས་པར་བྱས་པ་ལ་ལྟོས་པ་མེད་པ་ནི་མཐོང་བར་འགྱུར་བའམ། ནམ་ཡང་མ་བྱས་པ་ཡིན་ཏེ། དེའི་རང་བཞིན་དུ་གནས་པའི་ཕྱིར་རོ། །

[Block 1062]
རང་བཞིན་གཞན་ནི་འགའ་ཞིག་ལས་ཀྱང་མ་སྐྱེས་པའི་ཕྱིར་རོ། །

[Block 1063]
བསལ་བ་ཁས་བླངས་སུ་ཟིན་ཀྱང་ཁྱབ་པར་བྱེད་པ་ཡང་གཅིག་ལ་བསལ་བས་བསལ་བ་ཉིད་ན་ཐ་དད་པ་མེད་པའི་ཕྱིར། ཀུན་ལ་ཞེས་བྱ་བ་བསལ་བས་སྟོང་པའི་ཕྱོགས་དག་ལ་ཡང་མི་མཐོང་བར་འགྱུར་རོ། །

[Block 1064]
དེ་ཡང་བསལ་བ་ལ་ལྟོས་མིན། །གལ་ཏེ་བསལ་བ་ལྟོས་པ་ཅན་ཡིན་ན་ནི།

[Block 1065 [VERSE]]
བསལ་བྱེད་རྟོགས་པ་མ་ཡིན་ན། །
བསལ་བྱ་ཡང་དག་རྟོགས་པ་མིན། །
སྤྱི་དང་དེ་དང་ལྡན་པ་ཡང་། །
ཅི་ཡི་ཕྱིར་ན་བཟློག་པར་འདོད། །

[Block 1066]
རང་གི་རྟེན་དང་དབང་པོའི་ལྡན་པ་ལ་རྟོགས་པ་ཅན་གྱི་སྤྱི་ནི་རྟེན་གྱིས་སྟོང་པའི་ས་ཕྱོགས་ལ་མཐོང་བ་མ་ཡིན་ནོ་ཞེས་གང་ལས་ལན་བཏབ་པ་དེའི་ཡང་རང་གི་རྟེན་དང་དབང་པོའི་ལྡན་པས་ཕན་འདོགས་པ་ཡིན་པ༌[^889]ཉིད་ཀྱི་ཕྱིར། དེ་ལས་དེ་མཐོང་བ་ཅན་གྱིས་ཇི་ལྟར་གནས་པ་བཞིན་དུ་མཐོང་བར་འགྱུར་རོ། །

[Block 1067]
སྣང་བར་འགྱུར་བ་དེ་ནི༌[^890]མི་སྣང་བ་འདིར་ད་ལྟར་རིགས་པ་མ་ཡིན་ནོ། །

[Block 1068]
སྤྱི་ནི་བསལ་བས་བསལ་བར་བྱ་བ་ཉིད་ཡིན་པའི་ཕྱིར། བསལ་བར་བྱེད་པ་དང་བྲལ་བའི་ས་ཕྱོགས་དག་ཏུ་མཐོང་བ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ཡང་ལོག་པ་ཡིན་ནོ།[^891] །བསལ་བར་བྱ་བ་དང་བསལ་བར་བྱེད་པའི་དངོས་པོ་དེ་ལྟ་བུར་གྱུར་པ་ནི་དེ་ལ་མེད་པའི་ཕྱིར་རོ། །

[Block 1069]
སྒྲོན་མ་ལ་སོགས་པ་བསལ་བར་བྱེད་པ་ནི་བདག་ཉིད་རྟོགས་ནས་གཞན་རྟོགས་པར་བྱེད་པའི་རྒྱུ་ནི་རང་གི་ངོ་བོས་སྟོང་པ་ལ་བསལ་བར་བྱ་བ་རང་ཉིད་མཐོང་བར་བྱེད་པ་མ་ཡིན་ལ། དེ་ལྟར་བསལ་བ་ཡང་མ་ཡིན་ཏེ། ཕྱིན་ཅི་ལོག་ཏུ་གྱུར་པའི་ཕྱིར་རོ། །

[Block 1070]
ཇི་ལྟར་ན་དེ་སྤྱི་བསལ་བར་བྱེད་པར་ཡང་འགྱུར་ཞིང་དེ་རྟོགས་པའི་སྒོ་ནས་སྣང་བར་འགྱུར། དེ་ལྟ་ན་དེ་ནི་སྒྲོན་མས་བུམ་པ་དང་འདྲ་བར་བསལ་བར་བྱ་བ་ཡང་ཐོག་པར༌[^892]འགྱུར་ཏེ། རྣམ་པ་འགའ་ཞིག་གིས་དེ་ལྟ༌[^893]རྟོགས་པ་མེད་པར་སྣང་བའི་ངོ་བོ་ཉིད་མེད་པའི་ཕྱིར་རོ། །

[Block 1071]
གཞན་ཡང་འདིས་མི་རིགས་པ་ཅི་ཞིག་མངོན་པར་དཔྱད་ནས་དེ་ལྟར་དུབ་པ་མང་པོའི་སྤྱིའི་སླ༌[^894]བ་ལ་བརྟེན་པ་ཡིན། ཕན་ཚུན་ཐ་དད་པའི་ཕྱིར། བསལ་བ་ལྡོག་པ་ཅན་དག་ལ་རྗེས་སུ་འགྲོ་བ་ཅན་གྱི་ཤེས་པ་མི་རུང་བའི་ཕྱིར་རོ། །

[Block 1072]
ད་ནི་ཇི་ལྟར།

[Block 1073 [VERSE]]
ཐ་དད་མེད་དོན་མེད་པར་ཡང་། །
འཚེད་པ་པོ་སོགས་དག་གི་སྒྲ། །

[Block 1074]
འཚེད་པ་པོ་དང་ཀློག་པ་ལ་སོགས་པར༌[^895]གཅིག་ལ་རྗེས་སུ་འགྲོ་བ་མེད་པ་དག་ལ་ཡང་། འཚེད་པ་དང་འཚེད་པ་པོ་ཞེས་བྱ་བའི་སྒྲ་དང་ཤེས་པ་འཇུག་པ་ཡོད་པ་ཡིན་ནོ། །

[Block 1075]
དེ་དག་ལ་ནི་ཐ་དད་པ་མེད་པ་གཞན་ཅིག་ཡོད་པ་མ་ཡིན་ན། [^896]གང་གིས་ཐ་དད་པ་དག་གིས་ནི་དེ་ལྟར་རྟོགས་པར་འགྱུར། གལ་ཏེ་ལས་ཡོད་དོ་ཞེ་ན། འོན་ཏེ་བསལ་བ་ཁོ་ན་ལས་ཤེས་པ་དེ་ཡིན་ཡང་བླ་སྟེ། འདི་ལས་སམ་གཞན་གྱིས་ཅི་ཞིག་བྱེད་པ་ཡིན། ཐ་དད་པ་ནི་ཐ་མི་དད་པའི་ཤེས་པའི་རྒྱུར་མི་འགྱུར་བས་ན། སྤྱི་གཅིག་འདོད་པ་དེ་གལ་ཏེ་ལས་ཐ་དད་པས་ཀྱང་ཐ་དད་པ་མེད་པའི་ཤེས་པ་བསྐྱེད་པར་འགྱུར་ན། བསལ་བ་དག་གིས་ཉེས་པ་ཅི་ཞིག་བྱས་ན་གང་གིས་དེ་དག་དེ་ལྟར་མི་འདོད། གལ་ཏེ་དེ་དག་ནི་ངོ་བོ་གཅིག་པ་ཉིད་ཀྱི་ཕྱིར། དེའི་རྣམ་པ་མ་ཡིན་པའི་ཁྱད་པར་ལྡན་པ་འདིའི་འདི་ཞེས་བྱ་བའི་ལྡོག་པ་རྟགས་པར༌[^897]མི་འགྱུར་རོ་ཞེ་ན། འདིར་ལྡོག་པ་ཇི་ལྟ་བ་བཞིན་དུ་ཁྱད་པར་ཤེས་པ་དག་ཀྱང་བརྡ་ཇི་ལྟ་བ་བཞིན་དུ་དོན་གཞན་རྣམ་པར་གཅོད་པའི་ཕྱིར་རོ་ཞེས་བཤད་དོ། །

[Block 1076 [VERSE]]
དེ་བས་བསལ་བ་དང་འདྲ་བར། །
ཐ་དད་ཕྱིར་ལས་འདིའི་རྒྱུ་མིན། །

[Block 1077]
འཚེད་པ་པོ་ལ་སོགས་པ་ཐ་དད་པ༌[^898]མེད་པའི་ཤེས་པའི་འོ། །

[Block 1078]
གལ་ཏེ་དེ་དག་གི་ལས་ཀྱི་རིགས་ཐ་དད་པ་མེད་པའི་ཕྱིར་རྒྱུ་ཡིན་ནོ་ཞེ་ན། ལས་དང་འབྲེལ་ཕྱིར་རིགས་མ་ཡིན། འགྲོ་བ་ལ་སོགས་པ་བ་ལང་ཉིད་བཞིན་དུ་དོན་གཞན་འབྲེལ་པའི་རིགས་ནི་དོན་གཞན་ལ་ཤེས་པའི་རྒྱུ་མ་ཡིན་ལ་འཚེད་པ་པོའི་ལས་དག་ལ་ཡང་ལས་ཀྱི་རིགས་ཡིན་ན༌[^899]ལས་དེ་དག་ཀྱང་འཚེད་པ་པོའི་སྒྲས་བརྗོད་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 1079]
འོ་ན་ཅི་ཡིན་ཞེ་ན། ལས་དེའི་རྟེན་གྱི༌[^900]རྫས་ཡིན་ནོ། །

[Block 1080]
ལས་ཀྱི་སྤྱི་དེ་ཡང་། མཉན་པ་གཞན་གྱི་རྒྱུ་མཚན་ཕྱིར། །འཚེད་པ་འཚེད་པ་ཞེས་བྱ་བ་ནི་དེ་ལས་འགྱུར་གྱི། འཚེད་པ་པོ་ཞེས་བྱ་བར་ནི་མ་ཡིན་ཏེ། དེ་ནི་ལས་ཀྱི་རྒྱུ་མཚན་ཉིད་དུ་རབ་ཏུ་བཤད་དོ། །

[Block 1081]
གཞན་ཡང་། ལས་ནི་གནས་པ་མེད་ཕྱིར་དང་། ལས་མི་རྟག་པ་ནི་ཐམས་ཅད་དུ་ཡོད་པ་མ་ཡིན་ཏེ། ཤེས་པ༌[^901]དེའི་ལས་རྒྱུ་མཚན་ཉིད་ན་ལས་འགགས་པ་ལ་འཚེད་པ་པོ་ཞེས་བརྗོད་པར་མི་བྱ་སྟེ། འཚེད་པ་ན་ལས་ཡོད་པའི་ཕྱིར་རོ། །

[Block 1082]
དེ་ཉིད་ཀྱི་ཕྱིར། སྤྱི་ནི་འབྲེལ་པ་མེད་པའི་ཕྱིར། །སྒྲ་ཡི་རྒྱུ་ཉིད་ཐལ་འགྱུར་ཕྱིར། འབྲེལ་མེད་མ་ཡིན། ལས་ཞིག་པ་དེའི་སྤྱི་ནི་ལས་མ་ཡིན་ཞིང་བྱེད་པ་མ་ཡིན་པའི་ཕྱིར། རག་ལུས་པའི་འབྲེལ་པ་འདི་ལ་ཡང་ཡོད་པ་མ་ཡིན་པ་དེ་ལྟར་ན་འབྲེལ་པ་མེད་པའི་ཕྱིར་སྒྲ་དང་ཤེས་པའི་རྒྱུ་མ་ཡིན་ནོ། །

[Block 1083]
གཞན་དུ་ནི་ཧ་ཅང་ཐལ་བར་འགྱུར་རོ། །

[Block 1084]
གལ་ཏེ་འདས་པ་དང་མ་འོངས་པ་རྒྱུ་མཚན་དུ་བྱས་ནས་དེ་དག་འཇུག་གོ་ཞེ་ན། མེད་པའི་ལས་ཀྱང་ཤེས་བརྗོད་དག་གི་མིན་ཏེ་རྒྱུ་མཚན་མ་ཡིན་ནོ། །

[Block 1085]
དེ་དག་ནི་རྒྱུ་མཚན་ཅན་མིན་ཐོབ་ཕྱིར་རོ། །

[Block 1086]
མེད་པ་སྟེ་ནུས་པ་མེད་པ་ནི་ཇི་ལྟར་རྒྱུ་མཚན་དུ་འགྱུར། དངོས་པོའི་དེ་ཉིད་ནི་བྱ་བ་བྱེད་པའི་མཚན་ཉིད་ཅན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1087]
དེ་བས་ན་འདས་པ་དང་མ་འོངས་པའི་ལས་འགགས་པ་དང་ངོ་བོ་མ་ཐོབ་པ་ཅན་གྱི་རྒྱུ་མཚན་མ་ཡིན་ནོ། །

[Block 1088]
བསལ་བ་ལ་སོགས་པ་གཞན་དག་ཀྱང་མི་འདོད་པའི་ཕྱིར། དེ་དག་ནི་རྒྱུ་མཚན་མེད་པ་ཅན་དུ་འགྱུར་རོ། །

[Block 1089]
དེ་ལྟར་ན་རིགས་ཀྱང་གྲུབ་པ་མ་ཡིན་ཏེ། དེ་ནི་ཤེས་པ་དང་བརྗོད་པ་དག་གི་མཚན་ཉིད་དུ་འདོད་པའི་ཕྱིར་རོ། །

[Block 1090]
གལ་ཏེ་ནུས་པ་འཚེད་པ་པོ་ལ་སོགས་པའི་སྒྲའི་རྒྱུ་མཚན་མིན༌[^902]གྱི་ལས་དང་སྤྱི་ནི་མ་ཡིན་ཞེ་ན། རྗེས༌[^903]འགྲོ་མེད་ཕྱིར་ནུས་པའང་མིན། །འཚེད་པ་པོ་ལ་སོགས་པ་དག་གི་ནུས་པ་ཞེས་བྱ་བ་གཞན་ཅུང་ཞིག་ཀྱང་ཡོད་པ་མ་ཡིན་ཏེ། འདི་ཉིད་ནི་འཚེད་པ་ལ་སོགས་པའི་དོན་གྱི་བྱ་བ་ལས་ཉེ་བར་སྦྱོར་བ་ཡིན་པས་ན་རྫས་ནི་ཉེ་བར་སྦྱོར་བ་མ་ཡིན་པར་ཐལ་བའི་ཕྱིར་རོ། །
--- END BLOCKS ---
