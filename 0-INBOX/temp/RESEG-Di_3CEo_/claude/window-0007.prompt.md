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
[Block 246]
དྲུག་པོ་དེ་དག་ལས་ཀྱང་། ད་ལྟའི་དོན་ཕྱིར་དང་པོ་ལྔ། །མིག་ལ་སོགས་པ་ལྔའི་ཡུལ་ནི་ད་ལྟར་བ་ཡིན་པའི་ཕྱིར་སྔར་སྨོས་སོ། །

[Block 247 [VERSE]]
འབྱུང་བ་ལས་གྱུར་དོན་ཕྱིར་བཞི། །
དང་པོར་ཞེས་བྱ་བར་སྙེགས་སོ། །

[Block 248]
ལྔ་པོ་རྣམས་ལས་ཀྱང་བཞི་སྔར་སྨོས་པ་ནི་ཡུལ་འབྱུང་བ་ལས་གྱུར་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 249]
ལུས་ཀྱི་ཡུལ་ནི་མ་ངེས་ཏེ། རེས་འགའ་ནི་འབྱུང་བ་དག་ཡིན་ལ། རེས་འགའ་ནི་འབྱུང་བ་ལས་གྱུར་པ༌[^92]དག་ཡིན་ནོ། །

[Block 250 [VERSE]]
རེས་འགའ་ནི་གཉིས་ཀ་ཡིན་ནོ། །
གཞན་ནི་ཆེས་རིང་མྱུར་འཇུག་ཕྱིར། །

[Block 251]
ལྷག་མ་ནི་ཅི་རིགས་པར་ཆེས་རྒྱང་རིང་བ་དང་། མྱུར་བར་འཇུག་པས༌[^93]གཞན་པས་སྔར་སྨོས་ཏེ། མིག་དང་རྣ་བ་ནི་ཡུལ་རྒྱང་རིང་བའི་ཕྱིར་གཉིས་པས་དེ་དག་སྔར་སྨོས་སོ། །

[Block 252]
དེ་གཉིས་ལས་ཀྱང་མིག་ནི་ཆེས་རྒྱང་རིང་པོ་ལ་འཇུག་པ་དེའི་ཕྱིར་དེ་སྔར་སྨོས་སོ། །

[Block 253]
སྣ་དང་ལྕེ་ནི་རྒྱང་རིང་པོ་ལ་འཇུག་པ་མེད་མོད་ཀྱི་དེ་ཉིད་ལས༌[^94]ཀྱང་སྣ་ནི་ཆེས་མྱུར་བར་འཇུག་པའི་ཕྱིར་སྔར་སྨོས་སོ། །

[Block 254]
ཡང་ན་ཇི་ལྟར་གནས་རིམ་བཞིན།[^95] །ཡང་ན་ལུས་འདི་ལ༌[^96]མིག་གི་རྟེན་ནི་སྟེང་ན་གནས་སོ། །

[Block 255]
དེའི་འོག་ན་ནི་རྣ་བའིའོ། །

[Block 256]
དེའི་འོག་ན་ནི་སྣའིའོ། །

[Block 257]
དེ་ནས་ནི་ལྕེའིའོ།[^97] །

[Block 258]
ལུས་ཀྱི་ནི་ཕལ་ཆེར་དེའི་འོག་ནའོ། །

[Block 259]
ཡིད་ནི་དེ་དག་ལ་བརྟེན་པ་དང་ཡུལ་ན་མི་གནས་པའི་ཕྱིར་ཏེ། དེ་དག་གི་གོ་རིམས་ནི་ཇི་ལྟར༌[^98]གནས་པ་བཞིན་ཡིན་ནོ། །

[Block 260 [HEADING]]
### གཟུགས་ཀྱི་སྐྱེ་མཆེད་དང་ཆོས་ཀྱི་སྐྱེ་མཆེད། ^1-15-0

[Block 261]
ཡང་ཅིའི་ཕྱིར་གཟུགས་ཀྱི་ཕུང་པོ༌[^99]བསྡུས་པའི་སྐྱེ་མ་ཆེད་བཅུ་པོ་དག་ལས་གཅིག་གཟུགས་ཀྱི་སྐྱེ་མཆེད་དུ་བརྗོད་ལ། ཐམས་ཅད་ཀྱང་ཆོས་ཀྱི་རང་བཞིན་ཡིན་ན། གཅིག་ཆོས་ཀྱི་སྐྱེ་མཆེད་ཅེས་བྱ་ཞེ་ན། སྨྲས་པ།

[Block 262 [VERSE]]
བྱེ་བྲག་དོན་དང་གཙོ་བོའི་ཕྱིར། །
ཆོས་མང་བ་དང་མཆོག་བསྡུས་ཕྱིར།[^100] །
གཅིག་ནི་གཟུགས་ཀྱི་སྐྱེ་མཆེད་དང་། །
གཅིག་ནི་ཆོས་ཞེས་བྱ་བར་བརྗོད། །

[Block 263]
བྱེ་བྲག་གི་དོན་ཇི༌[^101]ལྟ་བུ་ཞེ་ན། ཅི་ནས་ཀྱང་ཡུལ་དང་ཡུལ་ཅན་ཉིད་དུ་རྣམ་པར་གཞག་པའི་སྒོ་ནས་བཅུ་པོ་འདི་དག་སོ་སོར་སྐྱེ་མཆེད་ཉིད་ཡིན་གྱི་སྤྱིར་ནི་མ་ཡིན་ནོ་ཞེས་རྟོགས་པར་བྱ་བ་ཡིན་མིག་ལ་སོགས་པ་བྱེ་བྲག་ཏུ་བྱས་པ་དག་གིས་ནི་གང་མིག་ལ་སོགས་པར་ནི་མིང་མ་བཏགས་ལ། གཟུགས་ནི་ཡིན་པ་དེ་གཟུགས་ཀྱི་སྐྱེ་མཆེད་དུ་ཤེས་པར་རུང་བས་འདིའི་མིང་གཞན་མ་བརྗོད་དོ། །

[Block 264]
ཡང་གཟུགས་ཀྱི་སྐྱེ་མཆེད་ནི་གཙོ་བོ་ཡིན་པའི་ཕྱིར་ཏེ། དེ་ནི་ཐོགས་པ་དང་བཅས་པའི་ཕྱིར་ལག་པ་ལ་སོགས་པའི་འདུས་ཏེ་རེག་པ་དག་གིས་རེག་ན་གཟུགས་སུ་རུང་བ་དང་། བསྟན་དུ་རུང་བའི་ཕྱིར་ཏེ། འདི་ནི་འདི་ནའོ།[^102] །

[Block 265]
ཆེ་གེ་མོ་ཞིག་ནའོ་ཞེས་བརྟག༌[^103]ཏུ་རུང་བའི་ཕྱིར་རོ། །

[Block 266]
བྱེ་བྲག་གི་དོན་ཉིད་ཀྱིས་གཅིག་ནི་ཆོས་ཀྱི་སྐྱེ་མཆེད་དུ་བཤད་ཀྱི་ཐམས་ཅད་ནི་མ་ཡིན་ནོ། །

[Block 267]
གཞན་ཡང་འདིར་ཚོར་བ་ལ་སོགས་པ་ཆོས་མང་པོ་རྣམས་བསྡུས་ཏེ། དེའི་ཕྱིར་ཆོས་ཀྱི་སྒྲ་སྤྱིར་རྗོད་པར༌[^104]བྱེད་དོ། །

[Block 268]
ཆོས་ཀྱི་མཆོག་མྱ་ངན་ལས་འདས་པ་ཡང་འདིར་བསྡུས་ཏེ་གཞན་དག་ཏུ་མ་ཡིན་ནོ། །

[Block 269 [HEADING]]
### ཆོས་ཀྱི་ཕུང་པོ་བརྒྱད་ཁྲི། ^1-16-0

[Block 270]
མདོ་དག་ལས།

[Block 271]
ཕུང་པོ་དང་། སྐྱེ་མཆེད་དང་། ཁམས་ཤེས་པར་བྱ་བ་གཞན་དག་ཀྱང་དམིགས་ན། ཅི་དེ་རྣམས་འདི་དག་ཉིད༌[^105]ཀྱིས་བསྡུས་སམ། འོན་ཏེ་ཐ་དད་པ་ཞིག་ཡིན་ཞེ་ན། འདི་དག་ཉིད་ཀྱིས་བསྡུས་ཀྱི༌[^106]ཐ་དད་པ་ནི་མེད་དེ། དེ་ལ་རེ་ཞིག །

[Block 272 [VERSE]]
ཆོས་ཀྱི་ཕུང་པོ་བརྒྱད་ཁྲི་དག །
གང་རྣམས་ཐུབ་པས་གསུངས་དེ་དག །
ཚིག་གམ་མིང་ཡིན་དེ་དག་ནི། །
གཟུགས་དང་འདུ་བྱེད་དག་ཏུ་འདུས། །

[Block 273]
གང་དག་གི༌[^107]ལྟར་ན་སངས་རྒྱས་ཀྱི་གསུང་ཚིག་གི་རང་བཞིན་ཡིན་པ་དེ་དག་གི་ལྟར་ན་དེ་དག་ནི༌[^108]གཟུགས་ཀྱི་ཕུང་པོས་བསྡུས་སོ། །

[Block 274]
གང་དག་གི་ལྟར་ན་མིང་གི་རང་བཞིན་ཡིན་པ་དེ་དག་གི་ལྟར་ན་ནི་འདུ་བྱེད་ཀྱི་ཕུང་པོས་བསྡུས་སོ། །

[Block 275]
ཡང་ཆོས་ཀྱི་ཕུང་པོའི་ཚད་ནི་ཇི་ཙམ་ཞེ་ན། ཁ་ཅིག་བསྟན་བཅོས་ཚད་ཅེས་ཟེར། ཁ་ཅིག་ན་རེ་དེ་ནི་ཆོས་ཀྱི་ཕུང་པོ་ཞེས་བྱ་བའི་ཆོས་མངོན་པའི་ཚད་ཙམ་མོ་ཞེས་ཟེར་ཏེ། དེ་ནི་ཤློ་ཀ་དྲུག་སྟོང་ངོ་། །ཡང་གཞན་དག་ན་རེ། ཕུང་པོ་ལ་སོགས་པ་གཏམ་རེ་ཡིན་ཞེས་ཟེར་ཏེ། ཕུང་པོ་དང་། སྐྱེ་མཆེད་དང་། ཁམས་དང་། རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་ལ་སོགས་པའི་གཏམ་རྒྱུད་རེ་རེ་ནི་ཆོས་ཀྱི་ཕུང་པོའོ་ཞེས་ཟེར་རོ། །

[Block 276 [VERSE]]
སྤྱོད་པ་རྣམས་ཀྱི་གཉེན་པོར་ནི། །
ཆོས་ཀྱི་ཕུང་པོ་མཐུན་པར་གསུངས། །

[Block 277]
འདི་སྐད་དུ་སེམས་ཅན་རྣམས་ཀྱི་སྤྱོད་པ་འདོད་ཆགས་དང་། ཞེ་སྡང་དང་། གཏི་མུག་དང་། ང་རྒྱལ་ལ་སོགས་པ་སྤྱོད་པ་ཐ་དད་པ་བརྒྱད་ཁྲི་ཡོད་དེ། དེ་དག་གི༌[^109]གཉེན་པོར་ཆོས་ཀྱི་ཕུང་པོ་བརྒྱད་ཁྲི་གསུངས་སོ་ཞེས་བརྗོད་དོ། །

[Block 278]
དེ་ལྟར་ཆོས་ཀྱི་ཕུང་པོ་བརྒྱད་ཁྲི་ཕུང་པོ་འདི་དག་ཉིད་དུ་བསྡུས་པ།

[Block 279 [HEADING]]
### ཕུང་པོ་སྐྱེ་མཆེད་ཁམས་གཞན་བསྡུ་བ། ^1-17-0

[Block 280 [VERSE]]
དེ་བཞིན༌[^110]གཞན་ཡང་ཅི་རིགས་པར། །
ཕུང་པོ་སྐྱེ་མཆེད་ཁམས་རྣམས༌[^111]ནི། །
རང་གི་མཚན་ཉིད་ལེགས་དཔྱད་དོ། །
ཇི་སྐད་བཤད་པར༌[^112]བསྡུ་བར་བྱ། །

[Block 281]
མདོ་གཞན་དག་ལས།

[Block 282]
ཕུང་པོ་དང་། སྐྱེ་མཆེད་དང་། ཁམས་གཞན༌[^113]གང་དག་གསུངས་པ་དེ་དག་ཀྱང་བསྟན་བཅོས་འདི་ལས་ཇི་སྐད་བཤད་པ་བཞིན་དེ་དག་གི་རང་རང་གི་མཚན་ཉིད་ལེགས་པར་དཔྱད་ནས་ཕུང་པོ་ལ་སོགས་པ་འདི་སྐད་བཤད་པ་འདི་དག་ཉིད་དུ་བསྡུ་བར་བྱ་སྟེ། དེ་ལ་རེ་ཞིག་ཚུལ་ཁྲིམས་དང་། ཏིང་ངེ་འཛིན་དང་། ཤེས་རབ་དང་། རྣམ་པར་གྲོལ་བ་དང་། རྣམ་པར་གྲོལ་བའི་ཡེ་ཤེས་མཐོང་བའི་ཕུང་པོ་དག་ལས་ཚུལ་ཁྲིམས་ཀྱི་ཕུང་པོ་ནི་གཟུགས་ཀྱི་ཕུང་པོས་བསྡུས་སོ། །

[Block 283]
ལྷག་མ་རྣམས་ནི་འདུ་བྱེད་ཀྱི་ཕུང་པོས་བསྡུས་སོ། །

[Block 284]
ཟད་པར་གྱི་སྐྱེ་མཆེད་བཅུ་པོ་དག་ལས་བརྒྱད་ནི་མ་ཆགས་པའི་རང་བཞིན་ཡིན་པའི་ཕྱིར་ཆོས་ཀྱི་སྐྱེ་མཆེད་ཀྱིས་བསྡུས་སོ། །

[Block 285]
འཁོར་རྣམས་དང་བཅས་ན་ནི་ཕུང་པོ་ལྔའི་རང་བཞིན་ཡིན་པའི་ཕྱིར་ཡིད་དང་ཆོས་ཀྱི་སྐྱེ་མཆེད་དག་གིས་བསྡུས་ཏེ། ཟིལ་གྱིས་གནོན་པའི་སྐྱེ་མཆེད་དག་ཀྱང་དེ་དང་འདྲའོ། །
--- END BLOCKS ---
