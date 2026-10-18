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
[Block 701]
[^465]

[Block 702 [HEADING]]
### རྒྱས་པར་བཤད་པ། ^1-2-0

[Block 703 [HEADING]]
#### ལྷའི་དབང་པོས་ཞུས་པ། ^1-2-1-0

[Block 704]
འདི་མན་ཆད་ནི་འདུལ་བའི་འགྲོ་བའི་ཡོངས་སུ་མ་སྨིན་པ་རྣམས་ཀྱི་ཐེ་ཚོམ་སྐྱེས་ཤིང་སྐྱེས་པ་རྣམས་བསལ་བས་ཡོངས་སུ་སྨིན་པར་བྱས་ནས་ཡོངས་སུ་སྨིན་པ་རྣམས་དེ་ཁོ་ན་ཉིད་ཀྱི་དོན་རྟོགས་པར་བྱེད་པ་ཀུན་རྫོབ་དང་དོན་དམ་པའི་ཚུལ་རྣམ་པར་དབྱེ་བས་རྒྱས་པ་རྣམ་པ་གཉིས་སུ་བསྟན་ཏེ། དེ་ནས་སྟོང་གསུམ་གྱི་སྟོང་ཆེན་པོའི་འཇིག་རྟེན་གྱི་ཁམས་འདི་ན་རྒྱལ་པོ་ཆེན་པོ་གང་དག་འཁོད་པ་དེ་དག་ཐམས་ཅད་དང་། ལྷའི་བུ་བྱེ་བ་ཁྲག་ཁྲིག་འབུམ་ཕྲག་དུ་མ་ལྷན་ཅིག་ཏུ་འཁོར་དེ་ཉིད་དུ་འདུས་པར་གྱུར་ཏོ༌[^466]ཞེས་བྱ་བ་ལ་སོགས་པས་ཅིའི་ཕྱིར་ལྷ་རྣམས་འདུས་པར༌[^467]ཡང་བསྟན་ལ། དེ་བཞིན་གཤེགས་པའི་མཐུ་བརྗོད་པའི་སྐབས་ནི་གང་ཡིན་ཞེ་ན། ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བསྟན་པ་འདི་སྔོན་མ་བྱུང་བའི་ཕྱིར་སྔོན་མ་བྱུང་བའི་ཆོས་བསྟན་པའི་ལྟས་སུ་འཁོར་འདུས་པ་ཡང་མདོར་བསྟན་དགོས་སོ། །

[Block 705]
འོད་ཟེར་འབྱིན་ཅིང་འོད་བཀོད་པ་ཡང་སྟོན་ཞེས་འབྱུང་བས་ན་ཆོས་བཤད་པའི་ལྟས་བསྟན་པའི་ཕྱིར་འོད་བསྟན་པ་མཛད་པར་རིག་པར་བྱའོ། །

[Block 706]
ཅིའི་ཕྱིར་ལྷའི་དབང་པོ་དེ་བཞིན་གཤེགས་པ་ལ་གསོལ་བ་མི་འདེབས་པར་གནས་བརྟན་རབ་འབྱོར་ལ་གསོལ་བ་འདེབས་ཤེ་ན། དེའི་ཚེ་འཁོར་རྣམས་ཉན་ཐོས་ཀྱིས་བཤད་པར་འདུལ་བའི་ཕྱིར་དེ་ལྟར་དེ་ལ་གསོལ་བ་བཏབ་པའི་སྒོ་ནས་དེ་བཞིན་གཤེགས་པ་ལ་ཡང་གསོལ་བ་བཏབ་པར་འགྱུར་རོ། །

[Block 707]
བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོས་ཇི་ལྟར་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་གནས་པར་བྱ། བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོའི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ནི་གང་ཡིན། བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ༌[^468]ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་ནི་ཇི་ལྟར་བསླབ་པར་བྱ་ཞེས་དྲིས་པ་འདི་གསུམ་གྱི་ལན་ནི་འོག་ནས་སྟོན་ཏོ། །

[Block 708]
དེ་ལ་སྔར་ནི་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ནས༌[^469]བརྩམས་ཏེ། རྣམ་པར་མི་རྟོག་པའི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བཟུང་ནས་འབྲིང་དུ་བཤད་པ་བསྟན་ཏོ། །

[Block 709]
འདིར་ནི་ལམ་གྱི་རྣམ་པ་ཤེས་པ་ཉིད་ནས༌[^470]བརྩམས་ཏེ། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་སྒྲུབ་པ་རྣམ་པར་རྟོག་པ་དང་བཅས་པ་དང་རྣམ་པར་མི་རྟོག་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བསྟན་ཏོ། །

[Block 710]
གང་དག་སྐྱོན་མེད་པ་ལ་ཞུགས་པ་དེ་དག་ནི་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་པའི་མཐུ་མེད་དེ་ཞེས་བྱ་བ་ནི་གང་དག་ལོག་པ་ཉིད་དུ་ངེས་པ་དེ་དག་ནི་རེ་ཞིག་སྐལ་བ་མེད་པ་ཞེས་བྱའོ། །

[Block 711]
འོན་ཀྱང་གལ་ཏེ་དེ་དག་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་པ༌[^471]དེ་དག་ལ་ཡང་རྗེས་སུ་ཡི་རང་ངོ་ཞེས་བྱ་བ་ནི་བཤད་པ་འདི་དེ་དག་གི་རྣ་བར་ཐོས་ན་ཡང༌[^472]དོན་མེད་པར་མི་འགྱུར་བས་བསྐལ་པ་བྱེ་བ་ཁྲག་ཁྲིག་བརྒྱ་སྟོང་དཔག་ཏུ་མེད་གྲངས་མེད་པའི་ཕ་རོལ་དུ། དེ་དག་སངས་རྒྱས་ཉིད་ལ་འཇུག་པར་འགྱུར་རོ་ཞེས་ལུང་ལས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 712 [HEADING]]
##### ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་གང་ཡིན་ཞེས་དྲིས་པའི་ལན། ^1-2-1-1-0

[Block 713]
ཀཽ་ཤི་ཀ་དེ་ལ་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོའི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི༌[^473]དྲིས་པ་རྣམ་པ་གསུམ་ལས་བར་མ་བསྟན་པ་ཡིན་ཡང་དང་པོར་བསྟན་པ་ནི་དེ་ལྟར་བསྟན་ན་གོ་སླ་བའི་ཕྱིར་རོ། །ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་འདི་ནི་ཉན་ཐོས་དང་རང་སངས་རྒྱས་ཀྱི་ས་ལ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཀྱི་ཕྱོགས་དང་། བྱང་ཆུབ་སེམས་དཔའི་ས་ལ་ལམ་གྱི་རྣམ་པ་ཤེས་པའི་ཕྱོགས་ཡིན་མོད་ཀྱི་གཉི་ག༌[^474]ཡང་འདིར་བྱང་ཆུབ་སེམས་དཔའ་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཐོབ་པར་འདོད་པ་ལ་ལམ་གྱི་རྣམ་པ་ཤེས་པ་བསྟན་པར་བྱའོ། །

[Block 714 [HEADING]]
###### ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཀྱི་ཕྱོགས། ^1-2-1-1-1-0

[Block 715]
དེ་ལ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཀྱི་ཕྱོགས་ནི། ཀཽ་ཤི་ཀ་འདི་ལ་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་རྣམ་པ༌[^475]ཐམས་ཅད་མཁྱེན་པ་ཉིད་དང་ལྡན་པའི་སེམས་བསྐྱེད་པས་གཟུགས་མི་རྟག་པར་ཡིད་ལ་བྱའོ། །

[Block 716]
དེ་བཞིན་དུ་སྡུག་བསྔལ་བ་དང་། བདག་མེད་པ་དང་། སྟོང་པ་དང་། ནད་དང་། འབྲས་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་ཡིད་ལ་བྱེད་པ་བཅོ་ལྔ་བསྟན་པ་དང་། རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་འགོག་པ་ལ་དམིགས་པའི་ཡིད་ལ་བྱེད་པ་བདུན་བསྟན་པས་བཤད་པར་རིག་པར༌[^476]བྱའོ། །

[Block 717]
ལམ་གྱི་རྣམ་པ་ཤེས༌[^477]པ་ཉིད་ཀྱི་ཕྱོགས་ནི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སོགས་པ་ནས༌[^478]མ་འདྲེས་པའི་མཐའི་བར་དུ་མི་དམིགས་པར་ཡིད་ལ་བྱེད་པ་རྣམས་དང་། ཆོས་དང་ཆོས་རྣམས་སྦྱོར་བ༌[^479]ཞེས་བྱ་བ་ལ་སོགས་པས་བསྟན་ཏོ། །

[Block 718]
དེ་ལ་ཉན་ཐོས་དང་རང་སངས་རྒྱས་ཀྱི་སའི་ཚུལ་གྱིས་མི་རྟག་པ༌[^480]ལ་སོགས་པའི་ཚིག་རྣམས་ཀྱི་དོན་བཤད་པར་བྱ་སྟེ། མ་བྱུང་བ་ལས་འབྱུང་བ་དང་བྱུང་ནས་ཀྱང་མེད་པར་འགྱུར་བའི་ཕྱིར། མི་རྟག་པར་ཡིད་ལ་བྱེད་དོ། །

[Block 719]
བདག་ཉིད་སྡུག་བསྔལ་གསུམ་དང་ལྡན་པ་དང་། གཞན་དག་གི་སྡུག་བསྔལ་གྱི་རྒྱུར་འགྱུར་བའི་ཕྱིར།[^481] སྡུག་བསྔལ་བའོ། །

[Block 720]
དབང་སྒྱུར་བ་མེད་པ་ལ་སོགས་པས་བདག་རང་ལ་བདག་གི་མཚན་ཉིད་དང་མི་ལྡན་པའི་ཕྱིར་བདག་མེད་པའོ། །

[Block 721]
ཆུ་ཤིང་གི་སྡོང་བོ་ལྟར་ནང་གི༌[^482]སྙིང་པོ་མེད་པས་ནང་བདག་གིས་སྟོང་པའི་ཕྱིར་སྟོང་པའོ། །

[Block 722]
རྐྱེན་དུ་མས་གསོ་དགོས་པ་དང་། ལུས་དང་ཡིད་ཀྱི་སྡུག་བསྔལ་གྱི་རྩ་བ་ཡིན་པའི་ཕྱིར་ནད་དང་འདྲ་བས་ནད་དོ། །

[Block 723]
ཞེན་པའི་གནོད་པ་དང་ལྡན་པ་དང་། ཉོན་མོངས་པའི་མི་གཙང་བ་ཟག་པ་དང་། སྐྱེ་བ་དང་། རྒ་བ་དང་། འཇིག་པས་རིམ་བཞིན་དུ་སྐྲངས་པ་དང་སྨིན་པ་དང་། རྡོལ་བའི་ཕྱིར་འབྲས་དང་འདྲ་བས་ན་འབྲས་སོ། །

[Block 724]
ཕྱི་ནང་གི་གནོད་པས་ཟུག་པར་བྱེད་ཅིང་བཅོས་དཀའ་བས་ཟུག་རྔུ་དང་འདྲ་བའི་ཕྱིར་ཟུག་རྔུའོ། །

[Block 725]
སྨད་པར་བྱ་བ་ཡིན་པ་དང་། གནོད་པར་འགྱུར་བའི་ཕྱིར་སྡིག་ཏོ་དང་འདྲ་བས་ན་སྡིག་པའོ། །

[Block 726]
རྐྱེན་གྱི་ཁར་ལས་པ་དང་། ལས་བདག་གིར་བྱ་བ་ཡིན་པས། [^483]གཞན་ལས་དབང་བསྒྱུར་བ༌[^484]མེད་པའི་ཕྱིར་གཞན་ལ་རག་ལས་པའོ། །

[Block 727]
[^485]ནད་དང་རྒ་བ་དང་། འཆི་བ་རྣམས་ཀྱིས་རབ་ཏུ་འཇིག་པའི་རང་བཞིན་ཡིན་པའི་ཕྱིར། འཇིག་པའི་ཆོས་ཅན་ནོ། །

[Block 728]
འདུས་བྱས་ཀྱི་མཚན་ཉིད་གསུམ་དང་ལྡན་ཞིང་འཇིག་རྟེན་གྱི་ཆོས་མི་བརྟན་པ་བརྒྱད་དང་ལྡན་པའི་ཕྱིར་མི་བརྟན་པའོ། །

[Block 729]
རང་གི་ངང་དང་། གནོད་པས་ཀྱང་འཇིག་པར་འགྱུར་བའི་ངང་ཚུལ་ཅན་ཡིན་པའི་ཕྱིར། རབ་ཏུ་འཇིག༌[^486]པའོ། །

[Block 730]
མི་འཇིགས་པ་ཞེས་བྱ་བ་ཉེ་བར་ཞི་བ་བདེ་བའི༌[^487]གཉེན་པོ་ཡིན་པ་དང་། འཇིགས་པ་ཐམས་ཅད་ཀྱི་རྒྱུ་ཡིན་པའི་ཕྱིར་འཇིགས་པའོ། །

[Block 731]
མ་ཚོར༌[^488]བཞིན་དུ་གནོད་པ་སྣ་ཚོགས་ཀྱིས་འཚེ་བའི་ཕྱིར། འཚེ་བའོ། །

[Block 732]
གནོད་པ་རྣམ་པ་མང་པོ་དང་། འདྲེ་བ་དང་། འགོ་བའི་ནད་དང་འདྲ་བའི་ཕྱིར། འགོ་བའི་ནད་དོ། །

[Block 733]
བདག་མེད་པ་དང་། ཞི་བར་ཡིད་ལ་བྱའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། །ངག༌[^489]གི་མཚན་ཉིད་དང་བྲལ་བའི་ཕྱིར་བདག་མེད་པའོ། །

[Block 734]
སྡུག་བསྔལ་ཐམས་ཅད་ཉེ་བར་ཞི་བའི་ཕྱིར་ཞི་བའོ། །

[Block 735]
ཉོན་མོངས་པ་དང་མི་ལྡན་པའི་ཕྱིར་དབེན་པའོ། །

[Block 736]
བདག་དང་བདག་གི་བས་སྟོང་པ་ཉིད་དང་ལྡན་པའི་ཕྱིར་སྟོང་པ་ཉིད་དོ། །

[Block 737]
འདུས་བྱས་ཀྱི་མཚན་མ་ཐམས་ཅད་དང་བྲལ་བའི་ཕྱིར་མཚན་མ་མེད་པའོ། །

[Block 738]
ཁམས་གསུམ་དུ་མི་སྨོན་པས་སྨོན་པ་མེད་པའོ། །

[Block 739]
ཕྱིས་ལས་མངོན་པར་འདུ་བྱེད་པ་མེད་པའི་ཕྱིར། མངོན་པར་འདུ་བྱེད་པ་མེད་པ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 740 [HEADING]]
###### ལམ་གྱི་རྣམ་པ་ཤེས་པ་ཉིད་ཀྱི་ཕྱོགས། ^1-2-1-1-2-0
--- END BLOCKS ---
