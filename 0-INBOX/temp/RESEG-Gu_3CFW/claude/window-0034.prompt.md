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
[Block 1191]
དེ་ལ་དེ་ལྟར་སྦྱར་བར༌[^1009]བྱའོ་ཞེས་བྱ་བ༌[^1010]ནི་དོམ་གྱི་པགས་པ་དེ་ལའོ། །

[Block 1192]
སྤུ་ལ་རེག་པས༌[^1011]ཕན་པར་བྱེད་པ་ཉིད་དུ་རེག༌[^1012]གོ་ཞེས་བྱ་བ་ནི་དོམ་ལྤགས་ཀྱི་སྤུ་ལས་སོ། །

[Block 1193]
དགེ་སློང་དག་དོམ་ལྤགས་ཀྱི་སྤུ་དག་འོག་ཏུ་སྟོན་པར༌[^1013]བྱེད་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། སྤུ་དག་གྱེན་དུ་བསྟན་པར་བྱའོ་ཞེས་གསུངས་པ་དེ༌[^1014]འདིས་བསྡུས་པ་ཡིན་ནོ། །

[Block 1194]
མཆིལ་ལྷམ་དག་རིམ་པ་མང་པོ་ཉིད་ཀྱིས་ཀྱང་ངོ་ཞེས་བྱ་བ་ཡང་ཕན་པ་བྱེད་པ་ཉིད་དུ་རིག་གོ་ཞེས་བྱ་བར༌[^1015]སྦྱར་ཏེ། རིམ་པ་གཅིག་པ་ཡང་ཐམས་ཅད་ཀྱིས་ཐམས་ཅད་དུ་ཕན་པར་བྱེད་པ་ཉིད་ཡིན་པས། དེ་བས་ན་རབ་ཀྱི་དགོངས་པ༌[^1016]ཅན་ཏེ་ཞེས་བྱ་བར་ཤེས་པར་བྱའོ། །

[Block 1195]
དུ་མའི་སྟེང་དུ་གཅིག་གཞག་པས་ཀྱང་ངོ༌[^1017]ཞེས་བྱ་བ་ནི་ཀོ་ལྤགས་བཞིན་རིམ་པ་དུ་མའི་སྟེང་དུ་དོམ་ལྤགས་གཅིག་གཞག་པས་ཀྱང་ཕན་པར་བྱེད་པ་ཉིད་དུ་རིག་གོ་ཞེས་བྱ་བར་སྦྱར་ཏེ། སྔ་མའི་རྣམ་པ་མེད་པ་ལ༌[^1018]གང་བསྟེན་པ༌[^1019]ཉིད་དུ་རིག་པར༌[^1020]བྱའོ། །

[Block 1196]
འདིར་གཞུང་ནི། རིམ་པ་མང་པོ་དག་རྙེད་པ་མེད་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། སྟེང་དུ་རིམ་པ་གཅིག་བཅུག༌[^1021]པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1197]
ཨཤྨ་པ་རནྟ་དག་ཏུ་ནི་ཀོ་ལྤགས་མི་བཅང་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི། ཡུལ་ཨཤྨ་པ་རནྟ་དག་ཏུ༌[^1022]ནི་ཀོ་ལྤགས་ནི་དགའ་མགུར༌[^1023]བཅང་དུ་གནང་བའོ། །

[Block 1198]
འདིར་གཞུང་ནི།

[Block 1199]
བེའུ་གསོད་པ་པའི་གླེང་གཞི་ལས།

[Block 1200]
དེ་ལྟ་བས་ན་དགེ་སློང་གིས༌[^1024]ཀོ་ལྤགས་མི་བཅང་བར་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1201]
སེང་གེ་ལ་སོགས་པའི་མི་བཅང་ངོ་ཞེས་བྱ་བ་ཡང་ཀོ་ལྤགས་ཞེས་བྱ་བར༌[^1025]སྦྱར་ཏེ། སེང་གེ་དང་སྟག་དང་། གླང་པོ་ཆེ་ཅང་ཤེས་དང་། རྟ་ཅང་ཤེས་ལ་སོགས་པ་རྣམས༌[^1026]ཀྱིས་ཉེ་བར་བསྡུ་བའོ།[^1027] །དེ་བས་ན་འདིར་ཡང་གླང་པོ་ཆེ་ལ་སོགས་པ་དག་ཀྱང་དེ་རྣམས་ཀྱིས་བསྙེགས་པ༌[^1028]ཉིད་དོ། །

[Block 1202]
འདི་རྣམས་ལ་ཉེ་བར་གནས་པར༌[^1029]བྱ་བ༌[^1030]ཉིད་མ་ཡིན་པ་དེ་བས་ན་དེའི་བྱེད་པའོ།[^1031] །གང་གིས་ཀོ་ལྤགས་མི་རུང་བ་ཉིད་ཡིན་པ་དེའི་རྒྱུས་པ་དང་། རུས་པ་དང་སོ་དང་ཤ་ལ་སོགས་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་སྲོག་ཆགས་གང་གིས་ཀོ་ལྤགས་མི་རུང་བ་དེའི་རྒྱུས་པ་ལ་སོགས་པ་ཡང་མི་རུང་བ་ཉིད་ཡིན་པའོ། །

[Block 1203]
འགྲོ་བ་དམན་པའི་དེ་ལའོ། །

[Block 1204]
རྐྱལ་བ་སྐ༌[^1032]བ་ཅན་བཅང་བར་བྱའོ་ཞེས༌[^1033]བྱ་བ་ནི། ཆུ་ལ་རྒལ་བ་དང་ཆུ་འཛིན་པའི་དོན་དུའོ། །

[Block 1205]
ཡང་ན་རྐྱལ་སྐྱའོ་ཞེས་བྱ་བ་ནི། དཀར་པོ་རྐྱལ་སྐྱ༌[^1034]ཉིད་དུ་བརྗོད་པའོ། །

[Block 1206]
དོན་གསལ་བ་དོན་གྱིས་ཐོབ་པ་མཛད་པར་བྱ་སྟེ། དེའི་ཕྱིར་ཁྲ་བོ་བཀྲ་བ་མི་བཅང་ངོ་ཞེས་བྱ་བ་ནི། རྐྱལ་པ་དང་རྐྱལ་སྐྱའོ།[^1035] །རྐྱལ་མི་ཤེས་པས་སྟ་གོན་མ་བྱས་པར༌[^1036]ཆུའི་གཏིང་དུ་འཇུག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། མ་བྱས་པར་ཞེས་བྱ་བ་ནི༌[^1037]འདིར་གཞུང་ནི། གང་རྐྱལ་མི་ཤེས་པར་དེས་རང་གི༌[^1038]ལུས་སུ་ཡོངས་སུ་དོར་བར༌[^1039]མི་བྱའོ་ཞེས་འདོན་པ་གཅིག་ལས་གསུངས་པའི་དེའི་འདི་བསྡུས་པ་ཡིན་ནོ། །

[Block 1207]
དབེན་པའི་ཕྱོགས་སུ་རྐྱལ༌[^1040]བསླབ་པར་བྱའོ་ཞེས་བྱ་བ་ནི་འགྲོ་བའི་དོན་ཅན་ལ་རྒོད་བག་གི་རྣམ་པ་ཉིད་ཀྱིས་རྒལ་བ་ནི་མ་ཡིན་ཏེ། བསླབ་པར་བྱ་བ༌[^1041]ནི་རྒོད་བག་གི་རྣམ་པ་ཉིད་དེ་བསལ་ན་དེ་བཞིན་དུ་འདི་ལ་རྗེས་སུ་བསྒྲུབ་པའི་སྔ་རོལ་དུ་གནས་པར་མི་འགྱུར་རོ། །

[Block 1208]
དབེན་པ་ཞེས་བྱ་བ་ནི་རབ་ཏུ་དབེན་པའི་ས་ཕྱོགས་སུ་དབེན་པའི་ཁྱམས་ཀྱི༌[^1042]དངོས་པོ་བྱེད་པ་དེ་བས་ན་དེའི་སྤྲོས་པ་འདིའོ། །

[Block 1209]
ཁ་ཅིག་ལས་མི་འདོད་བཞིན་དུ་རྒལ་བར་འདོད་པ་དེ་ན་མི་བདེན་ཏེ། གང་གི་ཕྱིར་སྟོབས་ལ་སོགས་པ༌[^1043]མེད་པའི་ཕྱིར་དང་། དམིགས་ཀྱིས་བསལ་བའི༌[^1044]བར་མེད་པའི་ཕྱིར་རོ། །

[Block 1210]
དེ་མ་ཡིན་པའི་གཏིང་དུ་ཁྱུ་མཆོག་མ་གཏོགས་པའི་བ་ལང༌[^1045]ལ་བརྟེན་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་མ་ཡིན་པའི་གཏིང་ཞེས་བྱ་བ་ནི་བ་ལང་གིས་རྒལ་མི་ནུས་པའི་གཏིང་དུའོ། །

[Block 1211]
མདོར༌[^1046]གྱུར་པ་ལ་ཡང་བྱེ་བྲག་མ་བཟུང་བར་ཆོ་ག་འདིའོ། །

[Block 1212]
དེ་ལ་མདོར༌[^1047]གྱུར་པ་འདི་ལ་བརྟེན་ནས་ནི་བསླབ་པའི་གཞི་འདི་ལས་འགལ་བའི་ཉེས་བྱས་གཅིག་དང་། མོ་ལ་རེག་པའི་ཉེས་བྱས་གཞན་ཅིག་དང་གཉིས་སུ་འགྱུར་རོ། །

[Block 1213]
ཆོ་ག་འདི་འདའ་བར་གྱུར་པ་ལ༌[^1048]ཞུས་པ་ལས།

[Block 1214]
མོ་ལ་རེག་པར་མི་བྱའོ་ཞེས་གསུངས་པ་ལས་ཤེས་པ་ཡིན་ནོ། །

[Block 1215]
གླང་པོ་ཆེ་དང་རྟ་དང་མ་ཧེ་དང་གཡག་དག་ལ་བརྟེན་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ཁ་ཅིག་འདིར་གཡག་གི་གནས་སུ་རྔ་མོ་འདོན་པ་ཡིན་ནོ། །

[Block 1216]
འདི་ནི་མི་རིགས་ཏེ༌[^1049]དེས་རྒལ་མི་ནུས་པ་ཉིད་ཀྱི༌[^1050]ཕྱིར་རོ། །

[Block 1217]
ཀོ་ལྤགས་ཀྱི་གཞི་རྫོགས་སོ།། །།

[Block 1218 [HEADING]]
## སྨན་གྱི་གཞི། ^4-0

[Block 1219]
སྨན་བསྟེན་པར་བྱའོ། །

[Block 1220]
དེ་ནི་རྣམ་པ་བཞིའོ། །

[Block 1221]
དུས་སུ་རུང་བ་དང་། ཐུན་ཚོད་དུ་རུང་བ་དང་། ཞག་བདུན་པ་དང་། འཚོ་བའི་བར་དུ་བཅང་བ་ཉིད་དོ། །

[Block 1222]
དང་པོ་མ་ཡིན་པ་ཉིད་དག་ནི་ནད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ལ། འདིར་དང་པོ་ཞེས་བྱ་བ་ནི་དུས་སུ་རུང་བ་སྟེ། དེ་མ་ཡིན་པ་གཞན་ཐུན་ཚོད་དུ་རུང་བ་ལ་སོགས་པ་ནི་དང་པོ་མ་ཡིན་པ་ཉིད་དོ། །

[Block 1223]
དེའི་དངོས་པོ་ནི་དང་པོ་མ་ཡིན་པ་ཉིད་དོ། །

[Block 1224]
དུས་སུ་རུང་བའི་སྤངས་པའི་ཐུན་ཚོད་དུ་རུང་བ་ལ་སོགས་པ་གསུམ་ལ་ནད་པའི་ཡུལ་ལ་བརྟེན་པར་བྱ་བ་ཉིད་ཡིན་གྱི་མིན་པའི་ཡུལ་ལ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏེ། [^1051]འདིར་གཞུང་ནི།

[Block 1225]
དགེ་སློང་བྲམ་ཟེའི་བུ་མོས་ཞུས་པ་ལས།

[Block 1226]
བཙུན་པ་ཐུན་ཚོད་དུ་རུང་བ་དང་། ཞག་བདུན་པ་དང་། འཚོ་བའི་བར་དུ་བཅང་བར་བྱ་བའི་སྨན་བྱིན་གྱིས་བརླབས་པ་གང་དག་ལགས་པ་དེ་དག་བྲོ་མི་འཚལ་བས་ཡོངས་སུ་སྤྱད་དུ་རུང་ངམ། ཉེ་བ༌[^1052]འཁོར་མི་རུང་ངོ་། །བྱིན་ལེན་བགྱིས་པ་དང་བྱིན་གྱིས་བརླབས་པ་དེ་དག་བྲོ་འཚལ་བས་ཡོངས་སུ་སྤྱད་དུ་རུང་ངམ། ཉེ་བ༌[^1053]འཁོར་རུང་ངོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1227]
བཙོ་ཚ༌[^1054]དང་ཆུ་ཤིང་གི་འབྲས་བུ་དང་། རྒྱ་ཤུག༌[^1055]དང་ཨ་ཤྭདྠ་དང་། ཨུ་དུམ་བཱ་ར་དང་རྩུབ་འགྱུར་དང་། རྒུན་ཆུ་དང་། འབྲ་གོའི་བཏུང་བ་རྣམས་ནི་ཐམས་ཅད་དུའོ་ཞེས་བྱ་བ་ལ་ཐམས་ཅད་དུའོ༌[^1056]ཞེས་བྱ་བ་ནི་ན་བ་དང་། མི་ན་བའི་ཕྱིར་བཙོ་ཚ༌[^1057]ལ་སོགས་པའི་བཏུང་བ་བརྒྱད་པོ་འདི་རྣམས་ལ་ཐམས་ཅད་ཉིད་ཀྱི་ཕྱིར་དང་པོ་མ་ཡིན་པ་ཉིད་དོ། །

[Block 1228]
ནད་པ་མ་ཡིན་པའི་ཕྱིར་ཏེ། ནད་པ་ཁོ་ནའི་ཕྱིར་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1229]
བཙོས་པའི་ཚ༌[^1058]དང་། འབྲུའི་ཚ་དང༌[^1059]ཞོ་ག་ཆུ༌[^1060]དང་། དར་བའི་དངས་མ་དང་། རྩབ་མོ་ཆུས་བཏབ་པ་ཚགས་ཀྱིས་བཙགས་པ་ཤིན་ཏུ་སླ་བ༌[^1061]བཞིན་སྣང་བ་འདམ་བུའི་ཉག༌[^1062]མའི་མདོག་ལྟ་བུ༌[^1063]དག་ཀྱང་དེ་དང་འདྲའོ་ཞེས་བྱ་བ་ལ་དེ་དང་འདྲའོ་ཞེས་བྱ་བ་སྟེ་བཙོ་ཚ༌[^1064]ལ་སོགས་པའི་བཏུང་བའང་དེ་དང་འདྲའོ་ཞེས་སྦྱར་རོ། །

[Block 1230]
འདི་རྣམས་ཀྱང་ཞོ་ག༌[^1065]ཆུའི་བྱེ་བྲག་དང་ལྡན་པ་རྣམས་ལ་ཐམས་ཅད་ཀྱི་ཕྱིར་དང་པོ་མ་ཡིན་པ་དང་བཏུང་བའི་ཞེས་བྱ་བའི་དོན་ཏོ། །
--- END BLOCKS ---
