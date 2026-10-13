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
[Block 1156 [HEADING]]
##### རྣམ་པར་ལྡན་པ། ^3-3-4-1-0

[Block 1157]
ཡན་ལག་ཐམས་ཅད་ནི་གཏན་ཚིགས་ཉིད་མ་ཡིན་ཏེ། རྣམ་པར་ལྡན་པ་དང་བསལ་ཏེ་འོངས་པའི་ནང་དུ་འདུས་པའི་ཕྱིར་རོ། །

[Block 1158]
དེ་ལ་རེ་ཞིག་གཙོ་བོ་ཡོད་དེ་བསལ་བ་རྣམས་དང་རྗེས་སུ་འགྲོ་བ་མཐོང་བའི་ཕྱིར་ཞེས་པ་ལ། གལ་ཏེ་འདིར་གཙོ་བོའི་ཡོད་པ་ཉིད་བསྒྲུབ་བྱ་ཡིན༌[^881]ཞེ་ན། དེ་མ་ཡིན་ཏེ། ཚད་མའི་ཡུལ་མ་ཤེས་པའི་ཕྱིར་རོ།[^882] །

[Block 1159]
སྤྱིའི་མཚན་ཉིད་མ་ཡིན་པའི་ཡུལ་ལ༌[^883]རྗེས་སུ་དཔག་པ་ཡོད་པ་མ་ཡིན་ནོ་ཞེས་བསྟན་ཟིན་ཏོ། །

[Block 1160]
བསྒྲུབ་བྱའི་ཆོས་ཀྱང་སྒྲུབ་བྱེད་འགྱུར། །བསྒྲུབ་བྱར་གྱུར་པའི་ཆོས་སྒྲུབ་བྱེད་དུ་འགྱུར་བའི་རིགས་ཏེ། ཐ་དད་དུ་གྱུར་པ་མེད་པས་སོ། །

[Block 1161]
དེ་ལྟ་མ་ཡིན་ན་ནི་སྲེག་པར་བྱེད་པ་ཡིན༌[^884]པའི་ཕྱིར་ཞེས་པས་ཀྱང་སྒྲ་མི་རྟག་པར་གྲུབ་པར་གྱིས་ཤིག །གཞན་ཡང་། རྒྱས་པའི་ངག་ཡིན།[^885] ངག་རབ་ཏུ་རྒྱས་པ་ནི་སྒྲུབ་བྱེད་ཀྱི་གཏན་ཚིགས་སུ་རིགས་པ་མ་ཡིན་ཏེ། སྒྲུབ་པར་བྱེད་པ་ནི་བསྡུས་པའི་ངག་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1162]
དེ་ཡང་། བརྗོད་མ་ཡིན། གང་བསྡུས་པའི་ངག་དེ་ཡང་གཏན་ཚིགས་སུ་བརྗོད་པ་མ་ཡིན་ཏེ། [^886]སྒྲུབ་བྱེད་དུ་ནི་ཡན་ལག་ཐམས་ཅད་བརྗོད་པ་ཡིན་ནོ། །

[Block 1163]
དེར་མ་བསྟན་པའི་ཁྱད་པར་ནི་གོ་བར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 1164]
དཔེ་ཡང་གལ་ཏེ་གང་ལ་བསྒྲུབ་བྱ་སྒྲུབ་པ་ལ་སྟོན་པར་བྱེད་པ་ཡིན་ན་ནི། དེ་ཡང་རིགས་པ་མ་ཡིན་ཏེ་འདི་ལྟར། གཙོ་བོ་རྗེས་འགྲོ་དང་ལྡན་མིན། །ཤིང་གི་ཤུན་ལྤགས་ལ་སོགས་པ་ལ་རིགས་གཅིག་པ་དང་ལྡན་པའི་གཙོ་བོ་ནི་ཡོད་པ་མ་ཡིན་ནོ་ཞེས་རིག་པར་བྱའོ། །

[Block 1165]
ཡོད་དུ་ཆུག་ན་ཡང་མ་བསྟན་པ་ལ་ནི་རྗེས་སུ་འགྲོ་བ་མེད་པའི་ཕྱིར་དཔེ་ལྟར་སྣང་བ་ཡིན་ནོ། །

[Block 1166]
དེ་བཞིན་དུ་སྒྲུབ་པར་བྱེད་པའི་དོན་གང་ཡང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1167]
བརྗོད་པར་བྱ་བའི་ཆ་ཤས་ཉིད་ལ་ནི་ངག་གི་ཆ་ཤས་ཉིད་ཉམས་པ་ཡིན་ནོ། །

[Block 1168]
གལ་ཏེ་བརྗོད་པར་བྱ་བ་ལ་ཉེས་པ་ཡོད་པ༌[^887]མ་ཡིན་པས་གང་དག་དེ་སྟོན་པར་བྱེད་པ་དེ་དཔེ་ཡིན་ནོ་ཞེ་ན། དེ་མ་ཡིན་ཏེ། དེ་བརྗོད་པར་བྱ་བ་ཉིད་སྐྱོན་དང་བཅས་པ་ནི་མ་ཡིན་ཏེ་འདི་ལྟར། ངག་ཀྱང་། ངག་ཡིན་ཡང་ནི་དཔེ་ལ་ནི་དེ་ཉིད་སྐྱོན་དང་བཅས་པ་ཡིན་ཏེ། ངག་གིས་ཤིང་གི༌[^888]ཤུན་ལྤགས་ལ་སོགས་པ་ལ༌[^889]གཙོ་བོ་དེ་དང་རྗེས་སུ་འགྲོ་བ་བསྟན་པར་མི་ནུས་པའི་ཕྱིར་རོ། །

[Block 1169]
གཞན་ཡང་ཉེ་བར་འཇལ་མི་རིགས། །ངག་གི༌[^890]དཔེ་ལ་ཉེ་བར༌[^891]འཇལ་བར་ཡང༌[^892]རིགས་པ་མ་ཡིན་ཏེ། ངག་ཇི་ལྟ་བ་བཞིན་དུ་བསྒྲུབ་པར་བྱའོ་ཞེས་གཅིག་ཏུ་བྱས་པའི༌[^893]སྦྱོར་བ་ནི་མེད་དོ། །

[Block 1170]
དེ་བཞིན་དུ་གཙོ་བོ་ཡོད་པ་ཉིད་དུ་བསྒྲུབ་པར་བྱ་བ་ལ་ཆ་ཤས་ཀྱི་མཚན་ཉིད་ནི་རྣམ་པ་ཐམས་ཅད་དུ་འབྲེལ་པ་མེད་པ་ཉིད་དོ། །

[Block 1171]
རྩོད་པའི་སྒོའི་ཕྱོགས་ནི་འབྲེལ་པ་ཙམ་དུ་འགྱུར་ཏེ། རྒྱུ་གཅིག་པ་ཉིད་ཐ་དད་པ༌[^894]རྣམས་ཀྱི་བསྒྲུབ་བྱ་ཡིན་ནོ་ཞེས་བྱས་ནས་སོ། །

[Block 1172]
དེ་ལ་ཡང་དང་པོ་ཉིད། དམ་བཅའི་དོན་དང་འགལ་བར་འགྱུར། །རྒྱུ་གཅིག་པ་རྣམས་ཐ་དད་ཡིན་ནོ་ཞེས་པ་ནི་ཤིང་གི༌[^895]ཤུན་ལྤགས་ལ་སོགས་པ་ཐ་དད་པ་ཉིད་ལ་རྒྱུ་དུ་མ་ཉིད་ཁས་བླངས་པའི་ཕྱིར་དམ་བཅའ་བ་འགལ་བ་ཡིན་ནོ། །

[Block 1173]
ཁས་མ་བླངས་ན་ཡང་དཔེ་ནི་ཡོད་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཉེས་པ་ཡིན་ནོ། །

[Block 1174]
ཅི་སྟེ་ཡོད་པ་སྔོན་དུ་སོང་བ་ཅན་ཉིད་བསྒྲུབ་པར་བྱ་བ་ཡིན་གྱི་གཅིག་ཉིད་ནི་མ་ཡིན་ཏེ། འདི་ཉིད་ཀྱིའོ་ཞེས་བསྟན་པའི་ཕྱིར་རོ་ཞེ་ན། རྩོད་པ་མེད་ཕྱིར། རྩོད་པ་མེད་པའི་ཕྱིར་ཡང་འབྲས་བུའི་རྒྱུ་ཡོད་པ་ཉིད་དུ་ནི་མ་ཡིན་ཏེ། དེ་ལྟར་རྩོད་པ༌[^896]མེད་པ་ནི་མི་རིགས་པ་ཉིད་དོ། །

[Block 1175]
གཞན་དུ་ནི༌[^897]གཅིག་ཉིད་མ་ཡིན་ཞིང་། ཡོད་ཙམ་མ་མིན། ཡོད་པ་ཙམ༌[^898]ཡང་བསྒྲུབ་བྱ་མ༌[^899]ཡིན་ནོ་ཞེས་བརྗོད་དོ། །

[Block 1176]
བདེ་བ་ལ་སོགས་པའི་རིགས་དང་རྗེས་སུ་འགྲོ་བ་མ་ཡིན་ཏེ། ཐ་དད་ཤིང་ཤུན་ལས་སོགས༌[^900]བཞིན། །གལ་ཏེ་དེའི་རིགས་ཀྱི་རྒྱུ་གཅིག་པ་ཉིད་བསྒྲུབ་བྱའོ་ཞེ་ན་དེ་ནི་མ་ཡིན་ཏེ། ཐ་དད་རྣམས་ལ་རིགས་གཅིག་པ་ཉིད་དང་རྗེས་སུ་འགྲོ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 1177]
རྗེས་འགྲོ་ཐམས་ཅད་སྒྲུབ་ཅེ་ན། །མ་ཡིན་ཏེ། དཔེ་མེད་པའི་ཕྱིར་དང་། མི་རྟག་པ་ཉིད་དང་། འབྲས་བུ་ཉིད་ལ་སོགས་པའི་རྗེས་སུ་སོང་བའི་ཕྱིར་དང་། རྣམ་པར་ལྡན་པ་གཞན་རྣམས་ལ་ཡང་མ་འབྲེལ་བའི་ཕྱིར་རོ། །

[Block 1178]
གཏན་ཚིགས་ལ་ཡང་སྐྱོན་གདུག་པ་ཅན་མ་གྲུབ་པ་དང་འགལ་བ་དང་མ་ངེས་པ་རྣམས་ཉིད་ཡོད་དེ། རེ་ཞིག་མ་གྲུབ་པ་ནི་རིགས་གཅིག་དང་རྗེས་སུ་འགྲོ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 1179]
མ་ཡིན་ཏེ། གང་གི་ཕྱིར་ཐ་དད་རྣམས་འབྲས་བུ་གཅིག་པ་དེའི་ཕྱིར། རིགས་གཅིག་རྗེས་སུ་འགྲོ་བ་ཅན་དེ་ལྟར་ཡང་མཐོང་སྟེ། གཞན་དུ་འབྲས་བུ་གཅིག་པ་ཉིད། །མེད་པར་ཡང་འབྲས་བུ་གཅིག་པ་ཉིད་སྙིང་སྟོབས་ལ་སོགས་པ་རྣམས་ལ༌[^901]རྗེས་སུ་འགྲོ་བ་ལས་མཐོང་ངོ་ཞེ་ན། སྒྲ་ལ་སོགས་པ་ཐ་མི་དད་པའི་འབྲས་བུ་དེ་དག་ནི་འཇིག་རྟེན་པའི་མིག་ལ་སོགས་པའི་ཤེས་པ་ལ་སོགས་པ་ཡང་ཡོད་པ་དེའི་ཕྱིར་འདི་མ་ངེས་སོ། །

[Block 1180]
དེ་ལྟར་གཞན་ཡང་། ཉེ་བར་ལེན་པའང༌[^902]དར་འགྱུར། །ཉེ་བར་ལེན་པར་གྱུར་པ་ལ་ཡང་རྒྱུའི་འབྲས་བུ་ཡིན་པས་དེའི་རིགས་སུ༌[^903]རྗེས་སུ་དཔག་པའི་རིགས་ཏེ་ཡུལ་དུ་གྱུར་པའི་སྒྲ་ལ་སོགས་པ་ལ་ནི་མ་ཡིན་ནོ་ཞེ་ན། མ་ཡིན་དུ་ཆུག་ན་ཡང་སྐྱེས་བུ་ལ་ཡང་ཡོན་ཏན་གསུམ་རྗེས་སུ་དཔག་པར་ཐལ་བར་འགྱུར་ཏེ། རྣམ་པར་ཤེས་པ་དེ་ནི་མཐར་སྤྲོ་བ་ལ་སོགས་པའི་འབྲས་བུ་མཐོང་བའི་ཕྱིར་རོ། །

[Block 1181]
ཅི་སྟེ་ཕྱི་རོལ་གྱི་སྒྲ་ལ་སོགས་པར་གྱུར་པ་ལ་སྤྲོ་བ་ལ་སོགས་པའི་འབྲས་བུ་མཐོང་བ་ཡིན་ནོ་ཞེས་བརྗོད་པར་བྱའོ་ཞེ་ན། དེ་ནི། ཕྱི་མིན་གཉིས་ཀར་སྐྱོན་ཡོད་ཕྱིར། །སྤྲོ་བ་ལ་སོགས་པའི་འབྲས་བུ་དེ་ནི་རྣ་བ་ལ་སོགས་པའི་འཇུག་པ་ཐ་མི་དད་པའམ་ཐ་དད་དུ་འཛིན་ཀྱང་རུང་སྟེ་སྐྱོན་ཅན་ནོ། །

[Block 1182]
གལ་ཏེ་ཐ་མི་དད་དུ་འཛིན་ན་ནི་རང་རང་གི་ཡུལ་དུ་མངོན་པར་ཞེན་པ་ལ་གནོད་དོ། །

[Block 1183]
དེ་སྟེ་ཐ་དད་ན་ནི་རིགས་གཅིག་རྗེས་སུ་དཔོག་པ་ལ་གནོད་དོ། །

[Block 1184]
དེ་ནི་ཕྱི་རོལ་གྱི་སྒྲ་ལ་སོགས་པ་རྣམས་ཀྱི་འབྲས་བུ་མ་ཡིན་ཏེ། སྒྲ་ནི༌[^904]འདུས་པ་ལས་བཏགས་པའི་ཕྱིར་རོ། །

[Block 1185]
རྣམ་པ་ལ་སོགས་པ་ལས་ལ་སོགས་པར་བཏགས་པ་བཞིན་ནོ། །

[Block 1186]
ཡང་ངེས་པར་བཟུང་བའམ། ངེས་པར་མ་བཟུང་ཡང་རུང་གཉིས་ཀ་ལྟར་ཡང་མ་ཡིན་ཏེ། སྐྱོན་དང་བཅས་པའི་ཕྱིར་རོ། །

[Block 1187]
གལ་ཏེ་རྗེས་སུ་དཔག་པ་དེ་ལས་གཅིག་ཁོ་ན་རིགས་ཀྱི་རྗེས་སུ་འགྲོ་བའོ་ཞེས་ངེས་པར་གཟུང་བར༌[^905]བྱེད་ན་ནི། དེ་སྣ༌[^906]ཚོགས་ཀྱི་རང་བཞིན་ཉིད་ལ་གནོད་དོ། །

[Block 1188]
ཅི་སྟེ་ངེས་པར་གཟུང་བར༌[^907]མི་བྱེད་ན་ནི་བསལ་ཏེ་འོངས་པ་གཞན་ཉིད་མེད་པར་འགྱུར་ཏེ། གཉིས་ཀ་ཡང་ངེས་པར་གཟུང་བར་མ་བྱས་པའི་ཕྱིར་སྤྱི་དང་བྱེ་བྲག་གཉིས་རེ་རེ་བསལ་ཏེ་འོངས་པར་འགྱུར་རོ། །

[Block 1189]
དེ་དག་ནི་རེ་ཞིག་མ་གྲུབ་པ་ཉིད་དོ། །

[Block 1190]
རྗེས་སུ་འགྲོ་བ། ཁས་བླངས་ན་ཡང་འགལ་བ་ཉིད། །ཐ་དད་པ་རྣམས་དང་རྗེས་སུ་འགྲོ་བའི་རིགས་གཅིག་ཉིད་ཁས་བླངས་ཀྱང་གཏན་ཚིགས་ལ་འགལ་བའི་སྐྱོན་ཡོད་པ་ཉིད་དེ། འདི་ལྟར་དུ་མ་སྔོན་དུ་སོང་བ་ཅན་ཉིད་རིགས་གཅིག་དང་ལྡན་པར་ནི་མ་མཐོང་ངོ་། །དེ་ལ་ཤིང་ལ་སོགས་པ་རྣམས་ལ་གཅིག་ཉིད་གྲུབ་པ་ནི་མེད་ལ། དེ་ཤིང་གི་ཤུན་ལྤགས་ལ་སོགས་པ་རྣམས་ཀྱི་སྔོན་དུ་སོང་བ་ཅན༌[^908]ཡང་མ་ཡིན་ཏེ། ཤིང་ལ་སོགས་པའི་ཉེ་བར་ལེན་པ་ཡོད་པའི་ཕྱིར་རོ། །

[Block 1191]
ཁས་བླངས་པའི་གཏན་ཚིགས་ལ་འགལ་བའི་སྐྱོན་འབའ་ཞིག་ཏུ་ནི་མ་ཟད་ཀྱི་འདི་ལྟར། མ་ངེས་པར་ཡང་འགྱུར། ཁས་བླངས་ཀྱང་ཤིང་ལ་སོགས་པ་ཤིང་ཤུན་ལ་སོགས་པ་རྣམས་ཀྱི་སྔོན་དུ་འགྲོ་བ་ཅན་ཉིད་ཀྱི་གཏན་ཚིགས་ལ་ངེས་པའི་སྐྱོན་ཡིན་ནོ། །

[Block 1192]
དེ་ལྟ་ན་ནི་ཤིང་ཤུན་དང་གྱོ་མོ་དང་ཁམ་ཕོར་དང་རྒྱན་ལ་སོགས་པ་ཐམས་ཅད་བདེ་བ་ལ་སོགས་པའི་རིགས་དང་ལྡན་པ་དང་དུ་མ་སྔོན་དུ་འགྲོ་བ་ཅན་ཡང་ཡིན་ནོ། །

[Block 1193]
དེ་ལྟར་ན་རེ་ཞིག་གཏན་ཚིགས་ཀྱི་སྐྱོན་གསུམ་ཀའོ། །

[Block 1194]
ཡང་གང་གི་ཕྱིར་གཅིག་སྔོན་དུ་སོང་བ་ཅན་གྱི་ཐ་དད་པ་རྣམས་སོ་ཞེས་དམ་བཅས་པ༌[^909]དེའི་ཕྱིར། དཔེ་ནི། བསྒྲུབ་བྱས་འཕངས༌[^910]འགྱུར། ཐམས་ཅད་ཀྱི་སྔོན་དུ་གཙོ་བོ་འགྲོ་བ་ཅན་ཉིད་དུ་ཁས་བླང་བར༌[^911]མི་བྱ་སྟེ། ཤིང་གི་ཤུན་ལྤགས་ལ་སོགས་པའི་སྔོན་དུ་ཤིང་ལ་སོགས་པ་སོང་བར་སྦྱར་བར་བྱའོ། །

[Block 1195]
དེ་ཡོད་མིན། དཔེ་དེ་ཡང་ཡོད་པ་མ་ཡིན་ཏེ། ཤིང་ཤུན་ལ་སོགས་པ་རྣམས་ཐ་དད་དུ་ཡོད་པའི་ཕྱིར་དང་། དེ་དག་ནི་བསྒྲུབ་པར་བྱ་བ་ནི་གཅིག་སྔོན་དུ་འགྲོ་བ་ཅན་ཡིན་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
