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
[Block 3011]
ཉོན་མོངས་པ་དང་ཉེ་བའི་ཉོན་མོངས་པ་རྣམས་བཤད་ཟིན་ཏོ། །

[Block 3012 [HEADING]]
### རྣམ་ཤེས་དང་དབང་པོ་དང་མཚུངས་པར་ལྡན་པ། ^5-15-0

[Block 3013]
དེ་དག་ལས་ཀྱང་།

[Block 3014 [VERSE]]
མཐོང་སྤང་བྱ་གཉིད༌[^1188]ང་རྒྱལ་བཅས། །
ཡིད་ཀྱི་རྣམ་ཤེས་ས་པ་ཡིན། །

[Block 3015]
མཐོང་བས་སྤང༌[^1189]བར་བྱ་བ་ཐམས་ཅད་ནི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་ས་པ་དག་ཡིན་ཏེ། གཉིད༌[^1190]ང་རྒྱལ་བསྒོམ་པས་སྤང་བར་བྱ་བ༌[^1191]དག་དང་བཅས་པ་ཡང་ངོ་། །ཉེ་བའི་ཉོན་མོངས༌[^1192]རང་དབང་ཡང་། །ཉེ་བའི་ཉོན་མོངས་པ་རང་དབང་ཅན་གང་དག་ཡིན་པ་དེ་དག་ནི་ཡིད་ཀྱི་ས་པ་ཁོ་ན་ཡིན་པར་བལྟ་བར་བྱའོ། །

[Block 3016]
གཞན་ནི་རྣམ་ཤེས་དྲུག་རྟེན་ཅན། །ཉོན་མོངས་པ་དང་ཉེ་བའི་ཉོན་མོངས་པ་གཞན་དག་ནི་རྣམ་པར་ཤེས་པ་དྲུག་གི་ས་པ་དག་གོ། །

[Block 3017]
ཡང་དེ་དག་ལས་བདེ་བ་ལ་སོགས་པའི་དབང་པོ་དང་མཚུངས་པར་ལྡན་པ་བརྗོད་པར་བྱ་སྟེ། བདེ་བ་དག་དང་འདོད་ཆགས་སུ། །མཚུངས་ལྡན། འདོད་ཆགས་ནི་བདེ་བ་དང་ཡིད་བདེ་བ་དང་མཚུངས་པར་ལྡན་ནོ། །

[Block 3018]
ཞེ་སྡང་བཟློག་པའོ། །

[Block 3019]
ཞེ་སྡང་ནི་སྡུག་བསྔལ་དང་ཡིད་མི་བདེ་བ་དང་མཚུངས་པར་ལྡན་ནོ། །

[Block 3020]
མ་རིག་པ་དག་ཐམས་ཅད་དང་། །དབང་པོ་ལྔ་ཆར་དང་མཚུངས་པར་ལྡན་ནོ། །

[Block 3021]
མེད་ལྟ་ཡིད་བདེ༌[^1193]སྡུག་བསྔལ༌[^1194]དང་། །ལོག་པར་ལྟ་བ་ནི་ཡིད་བདེ་བ་དང་། ཡིད་མི་བདེ་བ་དག་དང་མཚུངས་པར་ལྡན་ཏོ།[^1195] །

[Block 3022]
བསོད་ནམས་དང་སྡིག་པའི་ལས་ཅན་དག་དང་གོ་རིམས་བཞིན་ནོ། །

[Block 3023]
ཡིད་མི་བདེ༌[^1196]དང་ཐེ་ཚོམ་མོ། །

[Block 3024]
གཞན་ཡིད་བདེ་དང་། ལྟ་བ་བཞི་དང་། ང་རྒྱལ་དང་ཡིད་བདེ་བ་དང་མཚུངས་པར་ལྡན་ནོ། །

[Block 3025]
འདི་དག །འདོད་ལས་སྐྱེས་པར་བསྟན་ནས་གཞན་བཤད་པར་བྱ་སྟེ། བཏང་སྙོམས་དང་ཀུན། ཉོན་མོངས་པ་རྣམས་ནི་རྒྱུན་ཆད་པའི་དུས་ན་གདོན་མི་ཟ་བར་བཏང་སྙོམས་ཀུན་དུ་གནས་པའི་ཕྱིར་རོ། །

[Block 3026]
ཡང་ས་གོང་མ་རྣམས་ཇི་ལྟ་བུ་ཞེ་ན། སྨྲས་པ། ས་གོང་མ། ས་ཇི་བཞིན་དུ་རང་རང་དང་། ས་གོང་མའི་ཕྲ་རྒྱས་རྣམས་ནི་ས་གང་ན་དབང་པོ་ཇི་སྙེད་པ་རང་རང་གི་དབང་པོ་དང་ལྡན་ནོ། །

[Block 3027 [VERSE]]
འགྱོད་དང་ཕྲག་དོག་ཁྲོ་བ་དང་། །
རྣམ་འཚེ་ཁོན་དུ་འཛིན་པ་དང་། །
འཚིག་པ་ཡིད་མི་བདེ་བ་དང་། །

[Block 3028]
མཚུངས་པར་ལྡན་པ་ཞེས་བྱ་བར་སྦྱར་ཏེ། སྐྱོ་བའི་རྣམ་པར་འཇུག་པའི་ཕྱིར་དང་།

[Block 3029 [VERSE]]
ཡིད་ཀྱི་ས་པ་ཡིན་པའི་ཕྱིར་རོ། །
སེར་སྣ་དག་ནི་བཟློག་པ་ཡིན། །

[Block 3030]
ཡིད་བདེ་བ་དང་མཚུངས་པར་ལྡན་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3031]
གཡོ་དང་སྒྱུ་དང་འཆབ་དང་གཉིད། །གཉིས་ཀ་དང་ལྡན། ཡིད་བདེ་བ་དང་། ཡིད་མི་བདེ་བ་དག་དང་མཚུངས་པར་ལྡན་པ་རྣམས་སོ། །

[Block 3032]
བདེ་བ༌[^1197]དག་དང་། རྒྱགས་པ། བསམ་གཏན་གསུམ་པ་ན་ནི་བདེ་བ་དང་མཚུངས་པར་ལྡན་ནོ། །

[Block 3033]
མན་ཆད་ན་ནི་ཡིད་བདེ་བ་དང་མཚུངས་པར་ལྡན་ནོ། །

[Block 3034]
ཡན་ཆད་ན་ནི་བཏང་སྙོམས་དང་མཚུངས་པར་ལྡན་ཏེ། འདི་ལྟར་བཏང་སྙོམས་ཀུན་དུ་འགྲོ། །ཐམས་ཅད༌[^1198]བཏང་སྙོམས་དང་མཚུངས་པར་ལྡན་ཏེ། དེ་ནི་མ་རིག་པ་བཞིན་དུ་གང་ལ་ཡང་དགག་པ་མེད་དོ། །

[Block 3035]
བཞི་པོ་གཞན་ནི་ལྔ་དག་དང་། ངོ་ཚ་མེད་པ་དང་། ཁྲེལ་མེད་པ་དང་། རྨུགས་པ་དང་། རྒོད་པ་དང་། ཀུན་ནས་དཀྲིས་པ་བཞི་པོ་འདི་དག་ནི་དབང་པོ་ལྔ་ཆར་དང་མཚུངས་པར་ལྡན་ནོ། །

[Block 3036]
མདོ་ལས།

[Block 3037 [HEADING]]
### སྒྲིབ་པ་ལྔ། ^5-16-0

[Block 3038]
འདོད་པ་ལ་འདུན་པ་དང་། གནོད་སེམས་དང་། རྨུགས་པ་དང་། གཉིད་དང་། རྒོད་པ༌[^1199]དང་། འགྱོད་པ་དང་། ཐེ་ཚོམ་དང་། སྒྲིབ་པ་ལྔ་པོ་གསུངས་པ་གང༌[^1200]དག་ཡིན་པ་དེ་ལ་རྨུགས་པ་དང་། རྒོད་པ་དང་། ཐེ་ཚོམ་ཁམས་གསུམ་པ་ཡིན་ཡང་གཅིག་ཏུ་མི་དགེ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3039]
འདོད་ན་སྒྲིབ་རྣམས། འདོད་པའི་ཁོ་ནར་སྒྲིབ་པའི་མིང་འཐོབ་བོ། །

[Block 3040]
དེ་ལ་ཡང་། མི་མཐུན་དང་། ཟད༌[^1201]དང་བྱ་བ་གཅིག་པའི་ཕྱིར། །གཉིས་གཅིག་རྨུགས་གཉིད་དག་དང་། རྒོད་པ་དང་འགྱོད་པ་དག་གཅིག་ཡིན་ཏེ། མི་མཐུན་པ་དང་། ཟས་དང་། བྱ་བ་གཅིག་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3041]
གཉིད་དང་རྨུགས་པ་དག་གི་མི་མཐུན་པ་གཅིག་སྟེ། སྣང་བའི་འདུ་ཤེས་སོ། །

[Block 3042]
ཟས་གཅིག་པ་ནི་ཆོས་ལྔ་སྟེ། རྨྱ་བ་དང་། མི་དགའ་བ་དང་། བྱ་རྨྱང༌[^1202]དང་། ཁ་ཟས་ཀྱི་དྲོད་མི་ཟིན་པ་དང་། སེམས་ཞུམ་པ་ཉིད་དོ། །

[Block 3043]
འདི་དག་གི་བྱ་བ་ཡང་གཅིག་སྟེ། འདི་གཉིས་ཀས་ཀྱང་སེམས་ཞུམ་པར་བྱེད་དོ། །

[Block 3044]
རྒོད་པ་དང༌[^1203]འགྱོད་པ་དག་གི་ཡང་མི་མཐུན་པ་གཅིག་སྟེ། ཞི་གནས་སོ། །

[Block 3045]
ཟས་གཅིག་པ་ནི་ཆོས་བཞི་སྟེ། ཉེ་དུའི་རྣམ་པར་རྟོག་པ་དང་། ཡུལ་གྱི་རྣམ་པར་རྟོག་པ་དང་། མི་འཆི་བའི་རྣམ་པར་རྟོག་པ་དང་། སྔོན་རྒོད་པ་དང་རྩེས་པ་དང་། །དགའ་བ་དང་། དགའ་མགུར་ཡོངས་སུ་སྤྱོད་པ་རྣམས་རྗེས་སུ་དྲན་པ་ཡིན་ནོ། །

[Block 3046]
འདི༌[^1204]གཉིས་ཀྱི་བྱ་བ་ཡང༌[^1205]གཅིག་སྟེ། འདི་གཉིས་ཀས༌[^1206]ཀྱང་སེམས་རྣམ་པར་མ་ཞི་བར་བྱེད་དོ། །གང་གི་ཚེ་ཉོན་མོངས་པ་ཐམས་ཅད་ཀྱང་སྒྲིབ་པ་ཡིན་ན། ཅིའི་ཕྱིར་ལྔ་ཁོ་ནར་བཤད་ཅེ་ན། ཕུང་པོ་གནོད་བྱེད་དང་། ཐེ་ཚོམ་ཕྱིར་ན་ལྔ་ཉིད་དོ། །

[Block 3047]
འདོད་པ་ལ་འདུན་པ་དང་། གནོད་སེམས་དག་གིས་ནི་ཚུལ་ཁྲིམས་ཀྱི་ཕུང་པོ་ལ་དང་། རྨུགས་པ་དང་། གཉིད་དག་གིས་ནི་ཤེས་རབ་ཀྱི་ཕུང་པོ་ལ་དང་། རྒོད་པ་དང་འགྱོད་པས་ནི་ཏིང་ངེ་འཛིན་གྱི་ཕུང་པོ་ལ་གནོད་པར་བྱེད་པའོ། །

[Block 3048]
ཏིང་ངེ་འཛིན་དང་ཤེས་རབ་དག་མེད་ན་བདེན་པ་དག་ལ་ཐེ་ཚོམ་ཟ་བར་འགྱུར་ཏེ། དེའི་ཕྱིར་སྔར་བཤད་ཟིན་ཏོ། །

[Block 3049 [HEADING]]
### ཉོན་མོངས་པ་སྤོང་བ། ^5-17-0

[Block 3050]
འདི་དཔྱད་པར་བྱ་སྟེ། སྐལ་བ་མི་མཉམ་པའི་ཁམས་ཀུན་དུ་འགྲོ་བ་རྣམས་དང་། འགོག་པ་དང་ལམ་མཐོང་བས་སྤང་བར་བྱ་བ་ཟག་པ་དང་བཅས་པ་ལ་དམིགས་པ་རྣམས་གང་གི་ཚེ་དམིགས་པ་ཡོངས་སུ་ཤེས་པ་དེའི་ཚེ་སྤོང་བར་མི་འགྱུར་ལ། གང་གི་ཚེ་སྤོང་བར་འགྱུར་བ་དེའི་ཚེ་ནི་དམིགས་པ་ཡོངས་སུ་མི་ཤེས་ན་ཇི་ལྟར་དེ་དག་སྤོང་ཞེ་ན། ཉོན་མོངས་པ་རྣམས་ནི་དམིགས་པ་ཡོངས་སུ་ཤེས་པས་ཟད་པར་ངེས་པ་མ་ཡིན་ནོ། །
--- END BLOCKS ---
