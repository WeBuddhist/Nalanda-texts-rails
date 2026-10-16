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
[Block 4691]
དགོན་པ་བགྲོད༌[^3039]དཀའ་འཇིགས་པ་འོང༌[^3040]ལ་ཞེས་བྱ་བ༌[^3041]གྲོང་གི་གན་དུ་ཕྱིན་པའོ། །ཇི་ལྟར་གྲོང་གི་གན་དུ་ཕྱིན་པར་ཤེས་པར་བྱ་ཞེ་ན། དགོན་པ་དང་ནགས་ཀྱི་མཐའ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4692]
བདེ་བར་སོང་ཞེས་བྱ་བ་འཇིགས་པ་མེད་པར་ཅི་བདེར་དེངས་ཤིག་པའོ། །

[Block 4693]
སྡིག་པའི་ལས་ཀྱང་ཡོངས་སུ་སྤང་བར་འབད་པར་གྱིས། །ཞེས་བྱ་བ་ནི། ཅིའི་ཕྱིར་ཞེ་ན། སྡུག་བསྔལ་གྱི་རྣམ་པར་སྨིན་པ་ནི་ངེས་པའི་ཕྱིར་རོ། །

[Block 4694]
འགྱོད་པའི་མེ་ཞེས་བྱ་བ་དང་། མཛེའི་ནད་ཅེས་བྱ་བ་འདི་གཉིས་ཀྱིས་ནི་མིང་དང་། གཟུགས་ལུས་ཀྱི་སྡུག་བསྔལ་བསྟན་ཏེ། དེའི་ལས་དང་། སྡིག་པ་མཐོང་བའི་ཆོས་ཉིད་ལ་དེ་ལྟར་སྡུག་བསྔལ་བར་འགྱུར་བ་ལས་བརྩམས༌[^3042]ཏེ། དེའི་ལས་ལུས་འཇིག་པ༌[^3043]ལ་ནི་མི་སྤྱོད་པས་སོ། །

[Block 4695]
རྨའི་ཞིགས་བ་ནི་རྨ་ཞིགས་པའོ། །

[Block 4696]
རྨའི་ཆུ་འཛག་པ་ནི་རྨ་ཞིགས་པའི་ཆུ་སེར་རོ། །

[Block 4697]
དེས་གཤེར་བའི་ལུས་གང་ཡིན་པ་དེ་ནི་རྨ་ཞིགས་པའི་ཆུ་སེར་གྱིས༌[^3044]ལུས་གཤེར་བར་གྱུར་པའོ། །

[Block 4698]
སྔངས་ཤིང་ངོ་མཚར་དུ་གྱུར་ཏེ་ཞེས་བྱ་བ་ནི་དེའི་འཇིགས་སུ་རུང་བས་སོ། །

[Block 4699]
ངོ་མཚར་ཆེར་བཟུང་སྟེ་ཞེས་བྱ་བ་ནི་མི་མ་ཡིན་པར་ཡིད་ཆེས་སུ་མི་རུང་བའི་གཟུགས་ཡོད་པས་སོ། །

[Block 4700]
སྐྱ་བསེང་ནི་ཕྱོགས་གང་ན་མཛེ་དང་།

[Block 4701 [VERSE]]
ཤ་བཀྲའི་ནད་མེད་པའི་ཕྱོགས་དེ་ནའོ། །
སྐྲ་ནི་རྡུལ་གྱིས་གང་ཞིང་གཡེངས། །

[Block 4702]
ཞེས་བྱ་བ་ནི་གློ་བུར་གྱི་དྲི་མས་གོས་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 4703]
ཅིག་ཤོས་ནི་ལྷན་ཅིག་སྐྱེས་པ་ལས་གྱུར་པའོ། །

[Block 4704]
ཡང་ན་སྔངས༌[^3045]ཤིང་ངོ་མཚར་དུ་བཟུང་སྟེ། དྲིས་པ་ཞེས་བྱ་བ་ནི་སྔངས་པས་ཚུལ་དང་བྲལ་བའི་ཕྱིར། མི་ཡིན་པར་ཡིད་མ་ཆེས་པས་ངོ་མཚར་ཆེར་གཟུང༌[^3046]སྟེ། གནས་སྐབས་འདི་ལྟ་བུ་རྟོགས་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 4705]
[^3047]དྲི་བའི་སྦྱོར་བའོ། །

[Block 4706]
འབྲས་བུ་གཞན་ནི་སླད་ཀྱིས་མཆི། །ཞེས་བྱ་བ་ནི་ངན་འགྲོར་འགྲོ་བའི་འབྲས་བུ་སྟེ། བྱམས་ལ་སྙིང་རིང་བྱས་པ་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ནོ། །

[Block 4707]
བྱམས་ལ་སྙིང་རིང་བས་ནི་འཇིག་རྟེན་གཉི་གར་མི་བཟད་པའི་འབྲས་བུ་བསྟན་པའི་ཕྱིར། དེ་བས་བྱམས་ལ་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 4708]
ཡང་དག་པར་འཛིན་དུ་གཞུག་པའི་ཕྱིར། གྲོགས་པོ་གསུམ་དུ་སྒྲུབ་པའི་བྱེ་བྲག་གིས༌[^3048]འཛིན་དུ་གཞུག་པ་ཡིན་ནོ། །

[Block 4709]
མཛའ་བོ་དག་ལ་ལོག་པར་སྒྲུབ་པའི་ཉེས་དམིགས་བསྟན་པའི་ཕྱིར། བྱམས་ཕ་རྣམས་ལ་སྡང་བར་སྤྱོད་པའི་ཚུལ་བཟུང༌[^3049]ན། ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 4710]
འཇིག་རྟེན་གཉི་ག་ལ་ཕན་པ་ཉིད་དུ་བསྟན་པའི་ཕྱིར། མཛའ་བོ་རྣམས་ལ་སེམས་ཤིང༌[^3050]བྱམས་པས༌[^3051]གྲགས་པ་འཐོབ། །ཅེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་ཏེ། མཛའ་བོ་རྣམས་ལ་ལེགས་པ་སྒྲུབ་པའི་ཕན་ཡོན་བསྟན་པའི་ཕྱིར་ཏེ། ཕན་ཡོན་ཡང་རྣམ་པ་གཉིས་ཏེ།[^3052] ཚེ་འདིའི་དང་། ཚེ་ཕྱི་མའི་འོ། །

[Block 4711]
ཚེ་ཕྱི་མའི་མཐོ་རིས་འཐོབ་པར་འགྱུར་ཞེས་བྱ་བ་ཡིན་ཏེ། འདི་ན༌[^3053]ཕྱི་མའི་ཕན་ཡོན་ནོ། །

[Block 4712]
དང་པོ་ཚེ་འདིའི༌[^3054]ཕན་ཡོན་ལ་ནི་བདག་དང་། གཞན་གྱི་རྣམ་པ་གཉིས་ཏེ། མཐོང་བའི་ཆོས་ལ་ཡིད་དགའ་བ་ནི་བདག་གི་ཕན་ཡོན་ཏེ། འཆི་བའི་དུས་སུ་ཡིད་ལ་གཅགས་པ་མེད་པས། བདག་ཉིད་ཡིད་དགའ་བར་འགྱུར་རོ། །

[Block 4713]
གཞན་དང་འབྲེལ་པའི་ཕན་ཡོན་ནི་རྣམ་པ་གསུམ་སྟེ། ཐ་མལ་པ་དང་། མཛའ་བཤེས་དང་། དགྲའོ། །

[Block 4714]
དེ་ལ་ཐ་མལ་པའི་ཕན་ཡོན་གྱི་དབང་དུ་བྱས་ནས་གྲགས་པ་འཐོབ་པ་དང་། ཡིད་བརྟན་པ་སྟེ། ཐ་མལ་པ་དག་ལས་མ་བཏང་བ་ནི། །ཡིད་ཀྱི་ལས་ཀྱི་ཕན་ཡོན་ནོ། །

[Block 4715]
རིམ་གྲོ་བྱེད་པའི་བདེ་བ་དང་། ངན་གྲོགས་བྱེད་པའི་ཡོན་ཏན་ནི་མཛའ་ཤེས༌[^3055]ལས་འཐོབ་པ་སྟེ། ལུས་ཀྱི་ལས་ཀྱི་ཕན་ཡོན་ནོ། །

[Block 4716]
རིམ་གྲོ་བྱེད་ཅིང་བདེ་བ་འདོད་པ་བསྟན་པ་ལ་སོགས་པས་ངན་གྲོགས་བྱེད་པའི་ཡོན་ཏན་ནི་གྲོགས་པོ་དམན་པ་དག་ལས།

[Block 4717]
རིམ་གྲོ་ཤས་ཆེར་འཐོབ་པའི་ཕན་ཡོན་ནོ། །

[Block 4718]
དགྲ་རྣམས་ཀུན་གྱིས་མི་ཚུགས་པ་ནི་དགྲའི་ཕན་ཡོན་ནོ།[^3056] །བྱམས་པའི་ཕྱོགས་ལ་ལེགས་ནོངས་ཅི་བགྱིས་པའི། །ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་ནི་སྔར་བཤད་པའི་དོན་གྱི་མཇུག་སྡུད་པ༌[^3057]ཡིན་ཏེ། བྱམས་པའི་ཕྱོགས་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཀྱི་དང་པོ་ཕྱེད་ཀྱིས་ནི། ཡིད་ཀྱིས་མཁྱེན་ཅིང་རིག་པར༌[^3058]བྱ་བ་སྟེ། ཡིད་ཀྱི་ལས་ཀྱིས་བསྟེན༌[^3059]ཅིག་པའོ། །

[Block 4719]
སྐྱེ་བོ་དམ་པ་འདོད་པའི་ལམ་ལ་ཞེས་བྱ་བ་ནི། ལུས་དང་། ངག་གི་སྒྲུབ་པ་ཡིན་ནོ། །

[Block 4720]
ལམ་དེར་སོང་ན་འབྱོར་པ་རྗེས་སུ་འབྲང་། ཞེས་བྱ་བ་ནི་ལུས་དང་། ངག་དང་། ཡིད་ཀྱི་ཕན་ཡོན༌[^3060]ནོ། །

[Block 4721]
ལེགས་ནོངས་ཅི་བགྱིས་པའི་མཐུ་རྣམས་གྲུབ་པ་ཞེས་བྱ་བ་ལ། ནོངས་པ་བགྱིས་པའི་མཐུ་རྣམས་གྲུབ་པ་ཞེས་བྱ་བ་ནི་བྱམས་པ་རྣམས་ལ་སྡང་བར་སྤྱོད་པའི་ཚུལ་བཟུང་ན་ཞེས་བྱ་བའི་ཚིགས་བཅད་དེར་ཉེས་དམིགས་བསྟན་པའོ། །

[Block 4722]
ལེགས་པ་བགྱིས་པའི་མཐུ་རྣམས་གྲུབ་པ་ནི། །མཛའ་བོ་རྣམས་ལ་སེམས་ཤིང༌[^3061]བྱམས་པས༌[^3062]གྲགས་པ་འཐོབ། །ཅེས་བྱ་བ་དེས་ཕན་ཡོན་བསྟན་ཏོ། །

[Block 4723]
སློབ་དཔོན་དཔའ་བོས་མཛད་པའི་སྐྱེས་པའི་རབས་རྒྱ་ཆེར་བཤད་པ་ལས་སྤྲེའུ་ཆེན་པོའི་སྐྱེས་པའི་རབས་སོ།། །།

[Block 4724 [HEADING]]
## རི་དགས་ཤ་ར་བྷའི་སྐྱེས་པའི་རབས། ^27-0

[Block 4725]
གང་ན་མི་དང་བྲལ་ཞིང་རྒྱུན་ལུགས་མེད་པའི་འབྲོག་དགོན་པའི་ཕྱོགས་ནི་མིའི་རྒྱུན་ལུགས་མེད་པའོ། །

[Block 4726]
གང་གི་ཕྱིར་སྒྲ་མེད་པ་དེ་ནི་སྒྲ་མི་གྲག་པ་སྟེ། མིའི་རྒྱུན་ལུགས་མེད་པའང་ཡིན་པས་མིའི་རྒྱུན་ལུགས་མེད་ཅིང་སྒྲ་མི་གྲག༌[^3063]པའོ། །

[Block 4727]
རྩྭ་སྟུག་པོའི་ནང་དུ་ཤིང་གི་རྩ་བ་ལྡམ་ལྡུམ་ནུབ་པ་གང་ཡིན་པ་དེ་དག་ནི་ཤིང་གི་རྩ་བ་དང་། ལྡུམ་བུ་མང་པོ་རྩ༌[^3064]སྟུག་པོའི་ནང་དུ་ནུབ་པའོ། །

[Block 4728]
གང་དུ་དེ་མེད་པ༌[^3065]ནི་ཤིང་གི་རྩ་བ་དང་། ལྡུམ་བུ་ནུབ་པ་དེ་ནའོ། །

[Block 4729]
འགྲོན་པོ་རྣམས་དང་། ཤིང་རྟ་དང་། བཞོན་པ་ནི་འགྲོན་པོ་རྣམས་ཀྱི་ཤིང་རྟ་དང་བཞོན་པའོ། །

[Block 4730]
དེ་རྣམས་ཀྱི་རྐང་པ་ནི་འགྲོན་པོ་རྣམས་ཀྱི་ཤིང་རྟ་དང་བཞོན་པའི་རྐང་པ་སྟེ་དེས་སོ། །
--- END BLOCKS ---
