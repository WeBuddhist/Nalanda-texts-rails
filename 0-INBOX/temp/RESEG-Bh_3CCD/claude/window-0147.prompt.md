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
[Block 5146]
ཞེ་སྡང་ལས་འབྱུང་ན་མི་བསྐྱོད་པའི་རིགས་ལ་བསྡུའོ། །

[Block 5147]
དོན་ཡོད་གྲུབ་པ་ཡང་ཕྲག་དོག་གི་རང་བཞིན་ཏེ་ཕྲག་དོག་ཀྱང་ཞེ་སྡང་ལས་འབྱུང་བས་ན་ཐུགས་རྡོ་རྗེའི་རིགས་ཀྱི་ནང་དུ་བསྡུའོ། །

[Block 5148]
དེའི་ཕྱིར་རྣམ་པར་སྣང་མཛད་དང་མི་བསྐྱོད་པ་དག་གི་ཕྲ་མོའི་རྣལ་འབྱོར་གྱི་བསྒོམ་པ༌[^3036]གང་ཡིན་པ་དེ་དག་ནི་དེ་ཉིད་རིན་པོ་ཆེ་དང་དོན་ཡོད་གྲུབ་པའི་རྣལ་འབྱོར་པས་བསྒོམ་པར་བྱ་ཞེས་གུད་ནས་བཤད་པར༌[^3037]མི་བྱའོ། །

[Block 5149]
དེ་ཉིད་ཀྱི་ཕྱིར་རྒྱུད་ཕྱི་མ་ལས་ཀྱང་།

[Block 5150 [VERSE]]
སྐུ་གསུང་ཐུགས་ནི་རྣམ་པ་གསུམ། །
གསང་བ་ཞེས་བྱ་མངོན་པར་བཤད། །
རིགས་ནི་རྣམ་པ་བརྒྱར༌[^3038]བཤད་དེ། །
མདོར་བསྡུས༌[^3039]པས་ནི་རྣམ་པ་ལྔ། །

[Block 5151 [VERSE]]
སྐུ་གསུང་ཐུགས་ཀྱི་དབྱེ་བ་ཡིས། །
གསུམ་དུ་ཡང་ནི་བསྟན་པ་ཡིན། །

[Block 5152]
ཞེས་འབྱུང་ངོ་། །རྡོ་རྗེའི་བདག་ཉིད་ཅན་གྱི་ཚོགས་ཏེ་ཞེས་བྱ་བ་ནི་ཉེ་བར་བསྡུས་པའོ། །

[Block 5153]
ཡོངས་སུ་རྫོགས་པའི་ལྷའི་སྐུ་ཡིན་ལ་ཞེས་པ་ནི་བདག་ལ་བྱིན་གྱིས་བརླབ་པའི་རིམ་པས་ཡེ་ཤེས་ཀྱི་སྐུ་བསྐྱེད་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5154]
དེའི་དོན་སྟོན་པའི་ལེའུ་ལ་ཡང་དེ་སྐད་ཅེས་བྱའོ་ཞེས་པ་ནི། དེའི་དོན་སོ་སོར་སྟོན་པའི་ཚིག་གི་ཚོགས་ནི་ལེའུ་ཞེས་བྱའོ། །

[Block 5155]
བཤད་པའི་རྒྱུད་ནི་ཞེས་པ་ལ། །དགོངས་པ་ལུང་བསྟན་པ་འདུས་པའི་བཤད་པའི་རྒྱུད་ལས་སོ། །

[Block 5156]
གསལ་བར་སྟོན་པ་ཞེས་པ་ནི་ཐེ་ཚོམ་མེད་པའོ། །

[Block 5157]
དེ་འདིར་འཇུག་པར་བྱ་སྟེ་ཞེས་པ་ནི་འགྲེལ་པ༌[^3040]འདིར་ཡང་བསྟན་པར་བྱའོ། །

[Block 5158]
ཐོག་མཐའ་མེད་པ་ཞེས་པ་ནི། ཐོག་མ་དང་ཐ་མའི་སྐད་ཅིག་མ་དང་བྲལ་བའོ། །

[Block 5159]
དེ་ལ་ཐོག་མ་ནི་སྣང་བ་དང་སྣང་བ་མཆེད་པ་དག་གོ། །

[Block 5160]
ཐ་མ༌[^3041]ནི་སྣང་བ་ཉེ་བར་ཐོབ་པའོ། །

[Block 5161]
དེ་མེད་པ་ནི་ཐོག་མ་དང་ཐ་མ༌[^3042]མེད་པའོ། །

[Block 5162]
རྣལ་འབྱོར་ཞེས་པ་ནི་ཐབས་དང་ཤེས་རབ་ཡང་དག་པར་སྦྱོར་བས༌[^3043]ཐོབ་པར་བྱ་བ་སྟེ་རྒྱུ་ལ་འབྲས་བུའི་མིང་བཏགས་པའི་ཕྱིར་རོ། །

[Block 5163]
ཕྲ་མོ༌[^3044]ནི་ཞེས་པ་ལ་རྣལ་འབྱོར་གྱི་མངོན་སུམ༌[^3045]གྱི་ཚད་མས་ལྷག་པར་རྟོགས་པར་བྱ་བ་ཏིང་ངེ་འཛིན་གྱི་ཁྱད་པར་གྱིས་ཐོབ་པས་ཏེ་སངས་རྒྱས་ཀྱི་སྤྱོད་ཡུལ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 5164 [VERSE]]
ཕྲ་བར་གཟིགས་པའི་སངས་རྒྱས་ཀྱིས། །
ཕྲ་ཕྱིར་རང་གི་རིག་པ་ཡིན། །
རང་བཞིན་གནས་ཀྱང་བདག་འདྲ་བའི། །
བློ་རགས་པ་ནི་མ་མཐོང་ངོ་། །

[Block 5165]
ཞེས་འབྱུང་ངོ་། །

[Block 5166 [VERSE]]
དབྱིག་གཉེན་གྱི་ཞལ་སྔ་ནས་ཀྱིས་ཀྱང་། །
རྣམ་རིག་ཙམ་ནི་གྲུབ་པ་སྟེ། །
རང་ནུས་འདྲ་བ་བདག་གིས་ནི། །
བྱས་པ་ཐམས་ཅད་བསམ་མི་ཁྱབ། །

[Block 5167]
སངས་རྒྱས་རྣམས་ཀྱི༌[^3046]སྤྱོད་ཡུལ་ཡིན། །ཞེས་འབྱུང་ངོ་། །དེ་ལྟ་བུའི་འོད་གསལ་བའི་དེ་ཁོ་ན་ཉིད་དབྱངས་ཀྱི་ཡི་གེ་དང་པོ་གཟོད་མ་ནས་མ་སྐྱེས་པའི་ཡེ་ཤེས་ཀྱི༌[^3047]རང་བཞིན་གྱིས་མཚོན་པར་བྱ་བ་སྟེ། ཉེ་བར་བརྟགས་པས་ཡི་གེ་ཨ་ཡང་ཕྲ་མོའི་སྒྲས་བསྟན་ཏོ། །

[Block 5168]
དེ་ཡང་ཇི་ལྟ་བུ་ཡིན་ཞེ་ན། མི་གསལ་བ་ཞེས་པ་ནི་སྤྲོས་པ་ཐམས་ཅད་དང་བྲལ་བས་སོ། །

[Block 5169]
གསལ་བར་ཡང་དག་སྦྱོར་ཞེས་པ་ནི་དེ་ལས་དཀྱིལ་འཁོར་བཞི་ཕྱུང་བའི་ཕྱིར་རོ། །

[Block 5170]
དངོས་མེད་ཅེས་པ་ནི་གཟོད་མ་ནས་མ་སྐྱེས་པའོ། །

[Block 5171]
ངོ་བོ་ཉིད་དུ་བྱུང་ཞེས་པ་ནི་འོད་གསལ་བ་ལས་བྱུང༌[^3048]བའོ། །

[Block 5172]
ཨ་ཡིག་ཆོས་ཀུན་སྒོ་ཡིན་ཏེ། །གཟོད་མ་ནས་མ་སྐྱེས་པའི་ཕྱིར་ཞེས་འབྱུང་ངོ་། །རང་བཞིན་གྱིས་གྲུབ་པ་ཞེས་པ་ནི། ཆོས་ཉིད་ཀྱི་ངོ་བོ་ཡིན་པས་སོ། །

[Block 5173]
དང་པོ་ཞེས་པ་ནི་ཆོས་ཐམས་ཅད་ཀྱི་གཙོ་བོར་གྱུར་པའམ། ཨཱ་ལི་དང་ཀཱ་ལིར་ཐོག་མར་དམིགས་པའི་ཕྱིར་རོ། །

[Block 5174]
གཅིག་ནི་སྡེ་ཚན༌[^3049]བརྒྱད་སྡུད་པར་བྱེད་པའི་དངོས་པོའི་ཡི་གེ་བརྒྱད།[^3050] །དེ་སྡུད་པར་བྱེད་པའི་ཡི་གེ་བཞི་ཡོངས་སུ་གྱུར་པ་ལས་ཡི་གེ་གསུམ་སྡུད་པར༌[^3051]བྱེད་པའི་རང་བཞིན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 5175]
ཇི་སྐད་དུ།

[Block 5176 [VERSE]]
དང་པོ་གཅིག་ནི་དགུ་དབུས་ན། །
གང་ཞིག་བཅུ་ཡིས་མ་བཅིངས་པ། །
དེ་ནི་བཅིངས་མེད་ཅེས་བྱ་སྟེ། །
ཡེ་ཤེས་པ་ནི་མཆོག་གི་གནས། །

[Block 5177 [VERSE]]
དབྱངས་དང་གསལ་བྱེད་ཡི་གེ་སྟེ། །
གྲངས་དགུ་ཡི་ནི་རྗེས་འཇུག་པ། །
ཨས་བཅིངས་ཕན་ཚུན་ཡང་དག་སྦྱོར། །
གང་གིས་ཤེས་ཏེ་འགྲོ་བའི་བླ། །

[Block 5178 [VERSE]]
འབྱུང་བའི་མཐའ་དང་ཡང་དག་ལྡན། །
ཆ་ལ་སོགས་པ་བཅུ་དྲུག་གནས། །
ལྔ་པ་ལྔ་དང་ཡང་དག་ལྡན། །
བཞི་ནི་གསུམ་དུ་ངེས་པར་སྦྱར། །

[Block 5179 [VERSE]]
ཡི་གེ་ཨོཾ་བཅས་རིང་པོར་བཅས། །
ཡོན་ཏན་སྦྱོར་སོགས་ཕྱིས་དང་མཚུངས། །
ཐུང་ངུ་མ་ལུས་ངག་ཏུ་འགྱུར། །
གཅིག་མིན༌[^3052]དུ་མ་མ་ཡིན་ནོ། །

[Block 5180 [VERSE]]
ཡི་གེ་གང་ཞིག་སྔར་བཤད་དང་། །
གང་ཡང་མངོན་པར་ཕྱོགས་པ་རྣམས། །
སྐྱེས་པ་བུད་མེད་མ་ནིང་དང་། །
ཁམས་ལ་སོགས་པ་ཡོངས་སུ་བརྟགས། །

[Block 5181 [VERSE]]
སྟེང་དང་འོག་ཏུ་བཅས་པར་ནི། །
ཤེས་ནས་བློ་ནི་ངེས་པར་སྦྱར། །
བརྗོད་པ་ཡི་ནི་སྔགས་འདི་དག །
དངོས་མེད་ངོ་བོ་ཉིད་དུ་འབྱུང་། །

[Block 5182]
ཞེས་གསུངས་སོ། །

[Block 5183]
གཅིག་དང་དུ་མ་རྣམས༌[^3053]སྤངས་པ། །ཞེས་པ་ནི་ཡི་གེ་ཕྱི་མོ་ཐམས་ཅད་དེ་ཉིད་ཀྱི་ནང་དུ་བསྡུས་པའི་ཕྱིར་དང་། །དེ་ཉིད་ལ་ངག་གི་སྤྲོས་པ་ཐམས་ཅད་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 5184]
རྟེན་ཅིང་འབྲེལ་འབྱུང་ཆོས་སུ་གྲགས། །ཞེས་པ་ནི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་རང་བཞིན་གྱིས༌[^3054]ལས་དང་། ཉོན་མོངས་པ་དང་། སྐྱེ་བའི༌[^3055]ངོ་བོ་སྲིད་པ་གསུམ་གྱི་བདག་ཉིད་ཅན་གྱི་འཁོར་བའི་འཁོར་ལོའི་ཆོས་ཉིད་ཡིན་ཏེ། དེ་དག་སྟོང་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 5185]
དེ་བཞིན་དུ། དངོས་པོ་ཀུན་གྱི་འབྱུང་གནས་གཅིག །ཅེས་པ་ནི་སེམས་ཅན་དང་སྣོད་ཀྱི་འཇིག་རྟེན་ཞེས་བྱ་བའི་འབྱུང་བའི་གནས་གཅིག་གོ། །
--- END BLOCKS ---
