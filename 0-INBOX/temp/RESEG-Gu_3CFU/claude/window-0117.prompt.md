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
[Block 4096]
འདི་ནི་ལྟུང་བ་དང་ལྡན་པ་མ་ཡིན་ཏེ། སྔར་ཉིད་དུ་མི་འཇུག་པ་བྱ་བ་སྲིད་པ་ཡིན་ནོ། །

[Block 4097]
དེ་ལ་འདི་ལ་ཡང་དེའི་ཆོ་ག་ཡོངས་སུ་ཐོབ་པས་ཉེ་བར་བརྗོད་པ་མི་སླུ་བར་བྱེད་ཅིང་། དེའི་ཆོ་ག་ཡོངས་སུ་ཐོབ་པ་ལ༌[^2807]བསྒྲུབ་པའི་དོན་དུ་ཡུལ་འདི་ལ་མཚུངས་པ་ཉིད་དུ་བྱེ་བྲག་ལ་བརྗོད་པར་བྱ་སྟེ། སྦྱིན་པར་བྱེད་པ་སྤུངས་ཆེ༌[^2808]བ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་སྤགས་པ་མ་ཕུལ་བ་ཞེས་བྱ་བ་ནི་མ་སྤགས་པ་དང་འདྲའོ་ཞེས་བྱ་བར་སྦྱར་བར་བྱའོ། །

[Block 4098]
སྦྱོར་བ་གཅིག་པའི་ཕྱིར་ཐོབ་ན་གཅིག་ཉིད་དོ་ཞེས་བྱ་བ་ནི། སྦྱོར་བ་གཅིག་པའི་ཕྱིར་ཐོབ་ན་རྫས་ཐ་དད་པ་ཅན་ལ་ཡང་རྙེད་པ་ལ་གཅིག་པ་ཉིད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4099]
ལེན་པ་ལ་སོགས་པ་ལ་དུ་མ་ཉིད་ལ་ཡང༌[^2809]ཡོངས་སུ་རྫོགས་པའི་གོས་སྦྱིན་པ་དགེ་སློང་མ་ལ་ལྷུང་བཟེད་དང་དབྱར་གྱི་རས་ཆེན་ཐོབ་པ་ལ་ཡང་སྦྱོར་བ་གཅིག་པ་ཉིད་ཡིན་ན་ལྟུང་བ་གཅིག་ཅེས་བྱ་བ་དེ་འདིའི་བྱེད་པའོ། །

[Block 4100]
སོ་སོ་ནས་སྤགས་པ་སློང་བའི་སྤང་བའོ།། །།

[Block 4101]
ཅི་ཞིག་བྱས་ན་བསྐུར་བའི༌[^2810]སྤང་བར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་བསྐུར་བར༌[^2811]རུང་བ་མ་ཡིན་པ་ཆོས་གོས་ཀྱི་རིན་སྤངས་ནས་ཡོངས་སུ་དྲི་བ་སྔོན་དུ་བཏང་ཞིང་བསྟན་ཏེ་བསྒོ་ཞིང་སྨྲས་པ་བྱུང་བའི་མཐའ་རྗེས་སུ་བརྗོད་པ་སྔར་བྱས་པའི་ཞལ་ཏ་བྱེད་པ་ལ་བསྐུར་བར༌[^2812]གྱུར་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སྤངས་ནས་ཞེས་བྱ་བ་ནི་ཚེ་དང་ལྡན་པ་ཕོ་ཉ་དགེ་སློང་རྣམས་གོས་ཀྱི་རིན་དག་ལེན་དུ་མི་རུང་སྟེ་ཞེས་བྱ་བ་ལ་སོགས་པས་ཡོངས་སུ་དྲི་བ་སྔོན་དུ་བཏང་ཞིང་ཞེས་བྱ་བའོ། །

[Block 4102]
འཕགས་པ་རྣམས་ལ་ཞལ་ཏ་བྱེད་པ་འགའ་ཞིག་ཡོད་དམ་ཞེས་བྱ་བ་ལ་སོགས་པ་འདི་སྔོན་དུ་བཏང་ཞིང་ཞེས་བྱ་བ་སྨྲས་པ་ནི་བསྟན་ཏེ་ཞལ་ཏ་བྱེད་པ་ཞེས་བྱ་བ་ནི་དགེ་སློང་སྤོང་བར་བྱེད་པ་པོས་ཤེས་པར་བྱ་བ་གནས་སྐབས་ཀྱིས་ཤེས་པར་བྱའོ། །

[Block 4103]
བསྟན་ཏེ་ཞེས་བྱ་བ་ནི་ཁྱོད་ཀྱི༌[^2813]རིན་བྱེད་པ་འདི་རྣམས་ཀྱིས་ཞེས་བྱ་བ་ལ་སོགས་པས་བསྐུལ་བར་གྱུར་ན་ཞེས་བྱ་བ་འདི་ལ་ལྟོས་པ་འདི་སྔོན་དུ་སྨོས་པར་རིག་པར་བྱའོ། །སུས་བསྟན་པ་ཞེ་ན། དེའི་ཕྱིར་བསྒོ་ཞེས་སྨྲས་པ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 4104]
བསྒོ་ཞིང་ཇི་སྐད་སྨྲས་ཤེ་ན། དེའི་ཕྱིར་བྱུང་བའི་མཐའ་རྗེས་སུ་བརྗོད་པ་སྔར་བྱས་པ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་ཞིག་འདི་འཕགས་པས་ཞལ་ཏ་བགྱིད་པ་བསྟན་པ་གང་ལགས་པ་དེ་ཞེས་བྱ་བ་ལ་སོགས་པས་སོ། །

[Block 4105]
བསྐུལ་བར་གྱུར་ནའོ་ཞེས་བྱ་བ་ནི། དགེ་སློང་གི་ཞལ་ཏ་བྱེད་པའོ། །

[Block 4106]
ཚེ་དང་ལྡན་པ་ཞལ་ཏ་བྱེད་པ་བདག་གོས་འདོད་དོ་ཞེས་བྱ་བ་ལ་སོགས་པས་སོ། །

[Block 4107]
འགྲོ་བར་མ་ནུས་པ་ཉིད་ནི་བསྐུལ་བ་འདི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དལ་བ་མ་ཡིན་པ་རྗོད་པར༌[^2814]བྱེད་པ་ལ་གང་དུ་གཞན་གྱི་ཚིག་ལ་སྐབས་མེད་པར་འགྱུར་བ་ཞེས་བྱ་བ་མྱུར་བར་བརྗོད་པ་ནི་འདིར་རྒྱུ་བསྟན་པ་ཡིན་ནོ། །

[Block 4108]
བཏང་བར་སྨྲས་པའམ་གཉིད་ལོག་པའམ། ར་རོ་བ་དང་འབྲེལ་པ་ཉིད་དམ། འོན་པ་ཉིད་དམ་ནད་ཀྱིས་བཏབ་པའམ། གཞན་གྱི་དབང་དུ་གྱུར་པ་ལ་སོགས་པའི་རྐྱེན་གྱིས་མི་འབྱུང་བར་འགྱུར་ཏེ། དེ་བས་ན་འདིར་འགྲོ་བ་མ་ནུས་པ་ཉིད་ཀྱི༌[^2815]དཔེ་ཡིན་ཏེ། དེའི་ཕྱིར་མྱུར་བར༌[^2816]བརྗོད་པ་ལ་སོགས་པ་འདི་རྣམས་ཀྱིས་མི་ནུས་པ་ཉིད་ལ་ཡང་དག་པར་འགྲོ་བས་བསྐུལ་བ་ནི་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4109]
གང་འགྲོ་བ་ཞེས་བྱ་བ་བྱེ་བྲག་མ་སྨོས་པ་ཐམས་ཅད་ལ་འདིའི་དོན་གྱིས་དངོས་པོ་དང་འབྲེལ་བའི་ཚིག་ལ༌[^2817]ཡང་བསྐུལ་བར་གྱུར་པའི་དོན་ལ་ཡང་མཚན་མ་འདི་ལ་ཡང་གང་དུ་མེད་པ་ཉེ་བར་འགྲོ་བའི་ལན༌[^2818]སྟེར་བ་ལ་དེའི་དོན་དུ་གནས་བརྟག་པར་རིག་པར་བྱའོ། །

[Block 4110]
དེ་འདིར་འདི་ལྟར་གཞན་ལ་ཡང་བསྐུལ་བར༌[^2819]བྱས་པ་ཉིད་དེ་ལ་འདིར་གང་ཞིག་གྲངས་གསུམ་གྱི་རྗེས་སུ་གནང་བ་དེའི་ཁ་བསྐང༌[^2820]བ་ཉིད་ཅེས་བྱ་བ་འདིའི་བྱེད་པ་བསྐུལ་བའི་སྒོ་དྲུག་པོ༌[^2821]གང་དག་གསུངས་པ་དེ་དག་ཀྱང་དུས་ལ་འཇུག་པ་ཞེས་བྱ་བ་དེར་ཆོས་ཀྱི་གཏམ་གྱི་སྒོའི༌[^2822]ཚིག་དེ་ལའོ། །

[Block 4111]
དུས་ཞེས་བྱ་བ་ནི་དེའི་སྒོ་ཐོབ་པ་ལ་རྒྱས་པ་ཙམ་བསྟན་པ་སྟེ། འདི་ནི་དཔེ་ཡིན་ནོ། །

[Block 4112]
ཚེ་དང་ལྡན་པ་དག་ནི་གོས་དེ་དོན་དུ་གཉེར་བ་སྟེ།

[Block 4113 [VERSE]]
བདག་ནི་ཅུང་ཟད་ཅིག་སྨྲ་ཡིས། །
ཚེ་དང་ལྡན་པ་ཁྱོད་ཉོན་ཅིག །
སོང་ཤིག་ནི་གོས་དེ་དོན་དུ། །
གཉེར་བས༌[^2823]བདག་ལ་གོས་བྱིན༌[^2824]ཅིག །

[Block 4114]
ཞེས་བྱ་བ༌[^2825]ལ་སོགས་པ་ཡང་གཏམ་གཞན་དུ་གྱུར་པ་འབྲེལ་པ་ཅན་གྱི་གཏམ་གྱི་སྒོ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 4115]
འདི་ལྟ་སྟེ། མངོན་པར་སྨྲ་བ་དང་། ལེགས་པར་སྦྱོར་བ་དང་། ཟས་སྐོམ་དག་གི་དབང་དུ་བྱས་ནས་རེ་རེ་ལ་ཡང་གཉིས་གཉིས་ཏེ་དྲུག་ཏུ་འགྱུར་རོ། །

[Block 4116]
དེ་ལ་མངོན་པར་སྨྲ་བ་ནི། ཁྱོད་འོངས་སམ་ཞེས་ཟེར་བ་ལ་དེའི་ཕྱིར་རོ་ཞེས་ཟེར་བ་དང་། ལེགས་པར་འོངས་སམ་ཞེས་ཟེར་བ་ལ་དེའི་ཕྱིར་རོ་ཞེས་ཟེར་བའོ། །

[Block 4117]
ལེགས་པར་སྦྱོར་བ་ནི་སྟན་འདི་ལ་འདུག་ཅེས་ཟེར་བ་ལ་དེའི་ཕྱིར་རོ་ཞེས་ཟེར་བ་དང་། རྐང་པ་ཁྲུས་གྱིས་ཤིག་ཅེས་ཟེར་བ་ལ་དེའི་ཕྱིར་རོ་ཞེས་ཟེར་བའོ། །

[Block 4118]
ཟས་སྐོམ་གྱི་དབང་དུ་བྱས་པ་ནི་ཟན་ཟོ་ཞིག་ཟེར་བ་ལ་དེའི་ཕྱིར་རོ་ཞེས་ཟེར་བ་དང་། སྐོམ་འཐུངས་ཤིག༌[^2826]ཟེར་བ་ལ་དེའི་ཕྱིར་རོ་ཞེས་ཟེར་བའོ། །

[Block 4119]
སོ་སོའི་དངོས་པོས་བྱས་པའི་དེ་རྣམས་ལ་དེའི་དོན་དུ་འགྲོ་བ་ལ་རྣམ་པ་གང་གིས་ཀྱང་ཉེ་བར་བཀོད་པ་ལ་དེའི་ཕྱིར་རོ་ཞེས་བྱ་བ་བསྟན་པར་རིག་པར་བྱའོ། །

[Block 4120]
གང་གི་ཕྱིར་མི་རིགས་པའི༌[^2827]ངོ་བོ་འདི་ནི་གཞན་དུ་འགྱུར་རོ། །

[Block 4121]
མ་གྲུབ་ན་ལན་གཉིས་སུ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་བསྐུལ་བ་དང་པོ་དེས་མ་གྲུབ་ན་ལན་གཉིས་སུ་ཡང་བསྐུལ་བར་བྱའོ། །

[Block 4122]
ལན་གསུམ་དུ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ལན་གཉིས་སུ་བསྐུལ་བ་དེས་ཀྱང་མ་གྲུབ་ན་ལན་གསུམ་དུ་ཡང་བསྐུལ་བར་བྱའོ། །

[Block 4123]
དེའི་འོག་ཏུ་ལན་གསུམ་གྱི་བར་དུ་ཕྱོགས་སུ་བསྡད་པར་བྱའོ་ཞེས་བྱ་བ་ལ་དེའི་ཞེས་བྱ་བ༌[^2828]ནི་ལན་གསུམ་བསྐུལ་བས་གོས་ཀྱི་རྙེད་པ་མ་གྲུབ་ན་ཕྱོགས་སུ་གང་དུ་འདི་དོན་གྱིས༌[^2829]ཐོབ་པར་བྱ་བ་དེ་གནས་དེར་ལན་གསུམ་གྱི་བར་དུ་བསྡད་པར་བྱས། ལན་བཞི་འམ་ལྔ་འམ་དྲུག་གི་བར་དུ་བྱ༌[^2830]སྟེ། དེའི་འོག་ཏུ་ཅང་མི་སྨྲ་བས་ཕྱོགས་སུ་བསྡད་པར་བྱ་ཞེས་གསུངས་སོ། །

[Block 4124]
འདིར་གཞུང་ནི་བསྐུལ་བ་དང་འབྲེལ་པའི་གཅིག་ལ་སོགས་པའི་གྲངས་དང་ལྷན་ཅིག་ཏུ་འདི་ནི་གྲངས་ཡིན་གྱི་རང་དང་འབྲེལ་པས་ནི་མ་ཡིན་ཏེ་མ་གསུངས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 4125]
འདིར་འདི་ལ་ལན་གཅིག་གམ་ལན་གཉིས་སམ་གསུམ་མམ་བཞི་འམ་ལྔ་འམ་ལན་དྲུག་གི་བར་དུ་བྱ་སྟེ་འདི་ལྟར་བརྗོད་ན་དེའི་རིགས་སོ། །

[Block 4126]
བསྟན་པ་ནི་བཞི་སྟེ། ཀུན་ནས་ཞུགས་པ་དང་། ངེས་པར་ཞུགས་པ་དང་། ལས་ཀྱི་མཐའ་དང་། ལས་ཀྱི་ཁང་པ་ཞེས་བྱ་བ་དེར་གསུངས་སོ། །

[Block 4127]
གཞན་དུ་ན་ཡང་ཀུན་ནས་འཇུག་པ་དང་། ངེས་པར་འཇུག་པ་དང་། ཀུན་ནས་སྤྱོད་པ་དང་། ཚོང་པ་ཞེས་བྱ་བ་ཤིན་ཏུ་གྲགས་པ་དང་། གང་ན་ཀུན་ནས་སྡོད་པ་རྣམས་ཀྱིས༌[^2831]དཔེ་འདི་རྟོགས་པར་བྱའོ། །

[Block 4128]
འདིར་ཡང་སྔ་མ་བས་ནི་ཡོ་བྱད་ཆུང་བའི་ཚོང་པ་རྣམས་ཀྱི་དབང་དུ་བྱས་ནས་སོ། །

[Block 4129]
གཉིས་པ་ནི་ཚོང་པ་ཙམ་ལའོ། །

[Block 4130]
མ་གྲུབ་ན་སྦྱིན་པར་བྱེད་པ་ལ་བསྒྲག་པར་བྱའོ། །

[Block 4131]
དེ་ལྟར་སྤངས་པར་གྱུར་ཟིན་པ་ནི། འབུལ་བར་བྱེད་ན་སྤངས་པར་སྨྲ་སྟེ། སྦྱིན་པར་བྱེད་པའི་སེམས་བསྡུ་བར་རྗེས་སུ་བསྒྲུབ་པ་ཁས་ལེན་པ་ལས་བླང་བར་བྱའོ་ཞེས་བྱ་བ་ལ་འབུལ་བར་བྱེད་ན་ཞེས་བྱ་བ་ནི་ཞལ་ཏ་བྱེད་པས་སོ། །

[Block 4132]
སྤངས་པ་སྨྲ་ཏེ༌[^2832]ཞེས་བྱ་བ་ནི། སྦྱིན་བདག་ལ་སླར་སྦྱིན་པ་ཉིད་འདི་ལ་ཞེས་བྱ་བ་འདིས་བསྡུས་པའོ། །

[Block 4133]
གཞན་བསྐུལ་བ་ལ་གནས་ཀྱི་ཁས་བླངས་པ་ལའོ། །

[Block 4134]
བསྐུལ་བ་ལ་ཡང་གཞན་སྒོ་གསུམ་ལས་གནས་དང་ཕྱོགས་ལ་སྒོ་གསུམ་ལས་གཞན་དུ་ཁས་མི་ལེན་པ་ལ་ཡང་ཁས་བླངས་པ་ཉིད་ལ་སྦྱིན་པར་བྱེད་པ་ནི། སེམས་བསྡུ་བར་རྗེས་སུ་བསྒྲུབ་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4135]
འདིར་འཇུག་པ་ནི་གཙོ་བོ་སྟེ་རིམ་པས་ནི་མ་ཡིན་ནོ། །
--- END BLOCKS ---
