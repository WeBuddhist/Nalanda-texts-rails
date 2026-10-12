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
ལྷག་མས་ནི་ཡོན་ཏན་བསྟན་པ་ཉིད་དོ། །

[Block 1192]
དེ་ནས་སྐུ་དང་གསུང་དང་ཐུགས་བྱིན་གྱིས་བརླབ་པ་བསྟན་པར་བྱའོ་ཞེས་བྱ་བ་འབྱུང་བས་དེ་བཤད་པའི་ཕྱིར། ཐམས་ཅད་དེ་བཞིན་གཤེགས་པའི་ལུས། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ནི་རྡོ་རྗེ་འཆང་ཆེན་པོ་ལ་སོགས་པ་སྟེ། དེའི་ལུས་ཇི་ལྟར་བྱ་ཞེ་ན། ཕྱག་རྒྱ་བཞིས༌[^594]ནི་རྒྱས་བཏབ་ཅིང་། །ཞེས་བྱ་བ་ནི་ཆོས་དང་ལས་དང་དམ་ཚིག་དང་ཕྱག་རྒྱ་ཆེན་པོས་ཐོབ་པར༌[^595]བྱ་བའོ། །

[Block 1193]
མིག་ལ་སོགས་པའི་བདག་ཉིད་དེར། །ཞེས་བྱ་བ༌[^596]ནི་མིག་དང་རྣ་བ་ལ་སོགས་པའི་ནང་ལ་སོགས་པའོ། །

[Block 1194]
ཅི་བྱ་ཞེ་ན་ས་སྙིང་ལ་སོགས་རབ་ཏུ་བརྟག །ཅེས་པ༌[^597]སྟེ་མིག་ལ་སོགས་པར་སའི་སྙིང་པོ་ལ་སོགས་པ་བསྒོམ་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1195]
དེ་ནས་བདུད་ཐམས་ཅད་དང་བར་དུ་གཅོད་པ་ཐམས་ཅད་སྤང་བར་བྱ་བའི་ཕྱིར་ལུས་འདི་ནི་ཁྲོ་བོ་བདུད་ཐམས་ཅད་ངེས་པར་འཇོམས་པའོ་ཞེས་བསྟན་པར་འགྱུར་བས་རོལ་བའི་དགའ་བ་ནི་རོལ་པའི་དགའ་བ་སྟེ་སྙོམས་པར་འཇུག་པའི༌[^598]བདག་ཉིད་ཅན་ནོ། །

[Block 1196]
ཁྲོ་བོའི་རྒྱལ་པོ་ནི་ཁྲོ་བོའི་རྒྱལ་པོ་སྟེ། གང་ཞིག་གང་ལས་གང་དུ་གྱུར་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1197]
དེ་ཉིད་ནི་སྟོབས་ཆེན་ཏེ་གདུག་པ་ཐམས་ཅད་འདུལ་བའི་སྟོབས་ཆེན་པོ་དང་ལྡན་པ་གང་ཡིན་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1198 [VERSE]]
དགོད་པའི་གནས་བསྟན་པ་གསུངས་པ། །
དེ་ནི་ཕྱོགས་མཚམས་ངོ་བོ་རུ། །
དཔུང་པ་ཡན་ལག་རྣམས་སུ་བརྟག །

[Block 1199]
[^599]ཅེས་པ་ནི་ཕྱི་རོལ་གྱི་ཕྱོགས་དང་མཚམས་ཀྱི་ངོ་བོ་དང་ནང་གི་དཔུང་པ་ལ་སོགས་པར་གང་གིས་སྒོམ་པར་གྱུར་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1200]
འདི་དག་གིས་ནི་སྤྲུལ་པའི་དཀྱིལ་འཁོར་སྦྱོར་བ་གསུམ་ཡང་གསུངས་ལ། སྦྱོར་བ་གཅིག་ཀྱང༌[^600]གསུངས་སོ། །

[Block 1201]
འདི་དག་རྒྱས་པར་ནི། །

[Block 1202 [VERSE]]
སེམས་ཀྱིས་གཞན་ནི་མི་བསམ་པར། །
སེམས་དཔའ་ཆེན་པོས་མཉན་པར་གྱིས། །
རྡོ་རྗེ་སློབ་དཔོན་ལུས་འདི་ལ། །
རྒྱལ་བའི་སྐུ་ནི་རིམ་བཞིན་གནས། །
དང་པོ་སྐུ་ཡི་རྡོ་རྗེ་ནི། །

[Block 1203]
ཞེས་བྱ་བ་འོག་ནས་འཆད་དོ། །

[Block 1204]
ཡང་འདི་སྐད་དུ། གང་གི་ཕྱིར་སྤྲུལ་པའི་སྐུ་གསང་བ་འདི་དངོས་སུ་ཐ་དད་པའམ། ཐ་མི་དད་པའམ་བསྟན་ནས་སྣང་ངམ་འོན་ཏེ་མ་བསྟན་ན་སྣང་དེ་ལས་ཅིར་འབྱུང་།[^601] གལ་ཏེ་ཐ་དད་ན་ནི་གཅིག་པ་ཉིད་དུ་བཤད་པར་མི་འགྱུར། གང་ཞིག་གང་ལས་གྱུར་པ་དེ་ཡང་འདི་ལས་མ་གྱུར་པ་མེད་པ་དང་འགལ་བར་གནས་པ་དང་རྣམ་པར་བཤད་པ་མི་རིགས་སོ་ཞེས་པ་དེ་གསལ་བར་བཤད་པའི་ཕྱིར། །དེ་དང་དེ་ཡི་རིགས་བྱུང་བ། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། དེ་དང་དེ་ནི་རྡོ་རྗེའི་རིགས་ལ་སོགས་པ་སྟེ་གང་དང་གང་ཞེ་ན་ལྷ་དང་ལྷ་མོ་སྟེ། རིགས་ཅན་རྣམས་སྨིན་པ་དང་གྲོལ་བར་བྱ་བའི་ཕྱིར་སྣང་ཞེའོ། །

[Block 1205]
འདི་དག་གིས་ཀྱང་འདི་སྐད་དུ་སྟོན་པར་འགྱུར་ཏེ། གང་གི༌[^602]ཕྱིར་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ནི་ཐུགས་རྗེ་དང་སྨོན་ལམ་གྱི་དབང་གིས་སེམས་ཅན་གྱི་དོན་དུ་མི་འགྱུར་བ་ནམ་ཡང་མི་མཛད་ལ། སངས་རྒྱས་ཀྱི་རོལ་མོ་འདིས་ཀྱང་སེམས་ཅན་ཐམས་ཅད་སྨིན་ཅིང་གྲོལ་བར་འགྱུར་བས་ན་དེ་ལ་དེ་བསྟན་ཏོ་ཞེའོ། །

[Block 1206]
འདི་དག་གིས་ནི་ལྷའི་སྐུ་སྣ་ཚོགས་པར་སྣང་བ་དྲང་བའི་དོན་ཡིན་ཞེས་པའོ། །

[Block 1207]
འོ་ན་ངེས་པའི་དོན་གང་ཡིན་ཇི་ལྟར་མཐོང་ཞེ་ན། གཉིས་སུ་མེད་ཅིང་དབྱེར་མེད་པ་རང་བཞིན་གྱིས༌[^603]འོད་གསལ་བ་ཡིན་ནོ་ཞེས་རྟོགས་པར༌[^604]བྱ་བའི་ཕྱིར། དེ་བས་གཉིས་མེད་མཐོང་བ་ཡི། །ཞེས་བྱ་བ་ལ་སོགས་པ༌[^605]སྨོས་ཏེ༌[^606]དེ་བས་ན་ཞེས་པ་ནི་ཚིགས་སུ་བཅད་པ༌[^607]གོང་མ་གཏན་ཚིགས་ཉིད་ཡིན་པར་བསྟན་ཏོ། །

[Block 1208]
གཉིས་མེད་མཐོང་བ་ནི་གཉིས་མེད་མཐོང་བ་སྟེ་གང་གིས་འོད་གསལ་བ་མཐོང་བའོ། །

[Block 1209]
དེས་ཅིར་འགྱུར་ཞེ་ན། ཡེ་ཤེས་གསུམ་མཐོང་ཕྱིར་ཞེས་པ་སྣང་བ་གསུམ་གྱི་དེ་བཞིན་ཉིད་གང་དུ་མཐོང་བར་འགྱུར་བ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1210]
འདི་དག་གིས་ནི་དེ༌[^608]ཁོ་ན་ཉིད་གང་ཡིན་པ་འདི་ཉིད་ངེས་པའི་དོན་ཡིན་ལ་བླང་བར་བྱ་བ་ཡང་ཡིན་པས་ཐབས་གཞན་གྱིས་ཀྱང་རྙེད་པ་མ་ཡིན་པར་བསྟན་ཏོ། །

[Block 1211]
འོ་ན་ཅི་རྙེད་པར་འགྱུར་ཞེ་ན། སྣང་བ་ལ་སོགས་པས་རྙེད་པར་འགྱུར་བའི་ཕྱིར།

[Block 1212 [VERSE]]
དམན་དང་བར་མ་མཆོག་དང་ནི། །
དམ་པའི་ཡུལ་ལ་གཞག་པར༌[^609]བྱ། །

[Block 1213]
ཞེས་པ་སྣང་བ་དང་སྣང་བ་མཆེད་པ་དང་། སྣང་བ་ཐོབ་པ་ལ་གནས་པར་བྱ་ཞེས་པའི་དོན་ཏོ། །

[Block 1214]
དེ་ནས་ལངས་པའི་དུས་སུ་སྤྱོད་ལམ་ལ་མི༌[^610]གནས་ན་ཡོངས་སུ་གྲོལ་བར་མི་འགྱུར་བས་མཐོང་བ་ལ་སོགས་པ་འདི༌[^611]གང་དང༌[^612]གང་དུ་བརྟག་ཅེ་ན། དེ་བསྟན་པའི་ཕྱིར་དབང་པོ་རང༌[^613]ཉིད་ཅེས་བྱ་བ་ལ༌[^614]སོགས་པ་སྨོས་ཏེ། མིག་གི་དབང་པོ་ལ་སོགས་པ་གང་ཞིག་གཟུགས་ལ་སོགས་པ་གང་དག་ལ་དམིགས༌[^615]པར་གྱུར་པ་སྟེ། དེ་ཅི་ལྟར་བྱ་ཞེ་ན། དབང་པོ་གང་དང་གང་སྤྱོད་ཡུལ། དེ་དེ་སྣང་བ་ཅན༌[^616]ཉིད་ཙམ།[^617] །ཞེས་པ་གཟུགས་ལ་སོགས་པ་འདི་དག་སེམས་ཀྱི་སྣང་བ་ཙམ་ཡིན་གྱི་ཕྱི་རོལ་ན་ནི་མ་ཡིན་ནོ། །

[Block 1215]
དེ༌[^618]ཅིའི་ཕྱིར་ཞེ་ན། ཡུལ་གཅིག༌[^619]ལ་འདོད་པའི་དབང་གིས་ཐ་དད་དུ་གནས་པའི་ཕྱིར་རོ། །

[Block 1216]
ཡང་ཡུལ་འདི་དག་ནི་སེམས་ཙམ་ཉིད་ཡིན་ཏེ། ཡོད་པ་མ་ཡིན་པ་ལ་དོན་དུ་སྣང་བ་ཉིད་དེ་རབ་རིབ་ཅན་གྱི་ཤེས་པ་བཞིན་ནོ་ཞེས་པ་དང་།

[Block 1217 [VERSE]]
ཇི་ལྟར་བྱིས་པས་རྣམ་བརྟགས༌[^620]པའི། །
ཕྱི་རོལ་དོན་ནི་ཡོད་མ་ཡིན། །
བག་ཆགས་ཀྱིས༌[^621]ནི་དཀྲུགས༌[^622]པའི་སེམས། །
དོན་དུ་སྣང་བར་རབ་ཏུ་འབྱུང་། །

[Block 1218]
ཞེས་པ་ལ་སོགས་པའི་ལུང་དང་རིགས་པ་དག་གིས༌[^623]ཕྱི་རོལ་གྱི་ཆོས་ཐམས་ཅད་སེམས་ཙམ་ཉིད་དུ་བསྟན་པ་ནི་གོང་དུ་བཤད་པ་ཉིད་དོ། །

[Block 1219]
དེ་བས་ན་ཕྱག་ན་རྡོ་རྗེས་བཤད་པ། ཐབས་ཀྱི་རྒྱུད་དུ་ནི་ཤེས་རབ་ཀྱི་རྒྱུད་ཤེས་པར་བྱའོ། །ཤེས་རབ་ཀྱི་རྒྱུད་དུ་ནི་ཐབས་ཀྱི་རྒྱུད་ཤེས་པར་བྱ་བ་ལ་སོགས་པ་གསུངས་པས་འདི་ནི་འདི་ལྟར་ཤེས་པར་བྱའོ། །

[Block 1220]
དེ་བས་ན་བདག་ཉིད་ཀྱི༌[^624]སྤྱོད་ལམ་འདི་ནི་བསྟན་པར་འགྱུར་བས་ཀུན་རྟོག་ལ་སོགས་པ་ཉེ་བར་དགག་པར་དགོངས་སོ། །

[Block 1221]
དེ་ནི་དབང་པོས་གཟུགས་ལ་སོགས་པའི་ཞེན་པ་བཟློག་ནས་བདག་ཉིད་ཚིམ་པར་བྱའོ་ཞེས་འབྱུང་བས་དེ་བསྟན་པར་བྱ་བའི་ཕྱིར་གསུངས་པ། དབང་པོ་དེ་དེའི་ལམ་ནས་ནི། །ཞེས་བྱ་བ་དབང་པོ་ལ་བརྟེན་ནས་གཟུགས་ཡོངས་སུ་མཐོང་བར་གྱུར་པའོ། །ཅིར་འགྱུར་ཞེ་ན། སྒྲུབ་པ་པོས་ནི་ཡུལ་ཐོབ་པ། །ཞེས་པ། སྒྲུབ་པ་པོ་བདག་ཉིད་ཀྱིས༌[^625]ལྷ་དང་ལྷ་མོར་བྱས་པ་དེ་ནི་ཡུལ་ལ༌[^626]དབང་ཐོབ་པར་གྱུར་པའོ།[^627] །

[Block 1222]
དེ་ཇི་ལྟར་བྱ་ཞེ་ན། དེ་ནས་དེ་རྣམས་མ་ལུས་པར། །ཚིམ་པར་བྱ་ཕྱིར་དབུལ་བར་བྱ།[^628] །ཞེས་པ་གང་གིས་བདག་ཉིད་ཕྱག་རྒྱ་ཆེན་པོར་ཡོངས་སུ་རྫོགས་པར་བྱ་སྟེ་བདག་ཉིད་ལ་ཀུན་དུ་དབུལ་ཞེས་པའི་དོན་ཏོ།[^629] །དེ་དག་གི་དོན་ཡང་འདི་སྐད་དུ་སྟོན༌[^630]པར་འགྱུར་ཏེ། གང་གིས་རང་ཉིད་ལྷའི་ཆོ་ག༌[^631]ཡོངས་སུ་རྫོགས་པར་བྱ་སྟེ། རྣལ་འབྱོར་མ་དང༌[^632]ཐམས་ཅད་ཀུན་དུ་གང་གིས་ལེགས་པར་གནས་ནས་ལ་ལ་ནི་གཟུགས་ཀྱི་ལྷ་མོར་གྱུར་ཏེ་བདག་ཉིད་ཀུན་དུ་མཉེས་པར༌[^633]གྱུར་ཏོ། །

[Block 1223]
ལ་ལ་ནི་སྒྲའི་ལྷ་མོར་གྱུར་ཏེ་བདག་ཉིད་ཀུན་དུ་མཉེས་པར་གྱུར་ཏོ། །

[Block 1224]
ལ་ལ་ནི་དྲིའི་ལྷ་མོར་གྱུར་ཏེ་བདག་ཉིད་ཀུན་དུ་མཉེས་པར་གྱུར་ཏོ། །

[Block 1225]
ལ་ལ་ནི་རོའི་ལྷ་མོར་གྱུར་ཏེ་བདག་ཉིད་ཀུན་དུ་མཉེས་པར་གྱུར་ཏོ། །

[Block 1226]
ལ་ལ་ནི་རེག་བྱའི་ལྷ་མོར་གྱུར་ཏེ་བདག་ཉིད་ཀུན་དུ་མཉེས་པར་གྱུར་ཏོ། །

[Block 1227]
ལ་ལ་ནི་སྙོམས་པར་ཞུགས་པའི་ཡུམ༌[^634]དུ་གྱུར་ཏེ་བདག་ཉིད་ཀུན་དུ་མཉེས་པར་གྱུར་ཏོ། །

[Block 1228]
འདི་དག་གི་དུས་སུ་ཡང་རོལ་པ་སྣ་ཚོགས་ཀྱི་གླུ་དང་རོལ་མོ་སྣ་ཚོགས་ཀྱི་གར་དང་། རོལ་པ་སྣ་ཚོགས་ཀྱིས༌[^635]འཕྱང་བ་དང་། རོལ་པ་སྣ་ཚོགས་ཀྱིས་སྒེག༌[^636]པ་དང་། རོལ་པ་སྣ་ཚོགས་ཀྱིས༌[^637]རྩེ་བ་ལ་སོགས་པ་ལ༌[^638]ཀུན་དུ་སྤྱོད་པ་ཡོངས་སུ་སྤྱོད་དོ། །

[Block 1229]
[^639]ད་ནི་སྐུ་གསུམ་ཡང་བཤད་པར་བྱ་སྟེ། ཆོས་ཀྱི་སྐུ་ལ་སོགས་པ་འདི༌[^640]གཅིག་པའམ་ཐ་དད་པར་འགྱུར།[^641] དེ་ལས་ཅིར་འགྱུར་གལ་ཏེ་གཅིག་པ་ཡིན་ན་ནི་སྣང་བ༌[^642]ཉིད་དང་འགལ་བར་འགྱུར་ལ། ཐ་དད་ན་ནི་རིགས་པས་འཁྲུགས་སོ་ཞེ་ན་མ་ཡིན་པའི་ཕྱིར། [^643]སྐུ་གསུམ་དག་ནི་ཞེས་པ་ཆོས་ཀྱི་སྐུ་དང་ལོངས་སྤྱོད་རྫོགས་པའི་སྐུ་དང་སྤྲུལ་པའི་སྐུའོ། །

[Block 1230]
ཐ་དད་ན་ནི་འགལ་བར་གནས་སོ། །
--- END BLOCKS ---
