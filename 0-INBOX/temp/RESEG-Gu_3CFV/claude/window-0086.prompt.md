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
འདིར་རིག་པ༌[^1940]ཞེས་བྱ་བ་ནི་དཔེ་ཙམ་དུ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 3012]
བསྒོམ་པར་བྱ་བ་མ་ཡིན་པ་ཐམས་ཅད་ལ་ཡོངས་སུ་རྫོགས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 3013]
ཁ་ན་མ་ཐོ་བ་འདི་བྱེད་དུ་བཅུག་ནས་དགེ་སློང་དང་ལྷན་ཅིག་པ་ཉིད་དུ་འདིར་དགེ་སློང་མ་དང་དགེ་སློབ་མ་སློབ་དཔོན་དུ་རིགས་པ་ཉིད་ཀྱི་ཕྱིར༌[^1941]ལྟུང་བ་མེད་པའོ། །

[Block 3014]
འདིར་ཡང་དགེ་སློང་དང་ལྡན་པ་ཉིད་ནི་དགེ་ཚུལ་ལ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 3015]
འདི་དང་ཡང་ལྷན་ཅིག་ཏུ་རིགས་པ་ཉིད་ཀྱི་ཕྱིར། དགེ་སློབ་མས་སློབ་མ་དང་སློབ་དཔོན་ཉིད་དུ་ཕྱི་རོལ་པའི་རབ་ཏུ་བྱུང་བ་ལ་ཁྱིམ་པ་ཉིད་ཡོངས་སུ་རྫོགས་པ་ཁོ་ནའོ། །

[Block 3016]
གང་དུ་བཅུ་གཅིག་པ་འདི་ལ་རིག་པར་བྱ་བ་མ་ཡིན་པ་དང་། བསྟེན་པ་ལས་གྱུར་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་སྒྱུ་ཐབས་ཀྱིས་རྨ་བཅིངས་ཤིང་འགྲོལ་དུ་འཇུག་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སྒྱུ་ཐབས་ཀྱིས་ཞེས་བྱ་བ་ནི་ཉོན་མོངས་པ་ཅན་གཙོ་བོ་ཉིད་ཀྱིས་སོ། །

[Block 3017]
རྨ་བཅིངས་ཤིང་ཞེས་པ་ནི་བཅིངས་ཤིང༌[^1942]བཅིངས་ཤིང་། སྐྱེས་པ་ལ༌[^1943]འགྲོལ་དུ་འཇུག་ན་དངོས་གཞིའོ། །

[Block 3018]
སྒྱུ་ཐབས་ཀྱིས་བུད་མེད་འགྲོལ་དུ་འཇུག་པ་ལ་ནི་ཉེས་བྱས་སོ། །

[Block 3019]
འདི་ནི་གཙུག་དགའ་མོའི་དཔུང་པ་གཡས་པར་ཕོལ་མིག་བྱུང་བའི་རྨ་དེ་སྨན་པས་ཟན་གྱིས་གླན་ནས་རས་མས་བཅིངས་པ་དང་། དེས་ཧ་ཅང་ལྷོད་དོ། །

[Block 3020]
ཧ་ཅང་དམ་མོ།[^1944] །ཞེས་ཟེར་ཞིང་ཡང་དང་ཡང་འགྲོལ་དུ་བཅུག་པ་དེ་གང་ཡིན་པ་ལས་བཅས་པ་ཡིན་ནོ། །

[Block 3021]
དེའི་ཕྱིར་དོན་བདེན་པ་ཉིད་ལ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ནི། གང་གི་ཕྱིར་སྒྱུ་ཐབས་ཀྱིས་འགྲོལ་དུ་འཇུག་པ་འདི་ལ་ལྟུང་བྱེད་ཡིན་པ་དེའི་ཕྱིར་དམ༌[^1945]ཡང་དག་གམ། ལྷོད་པ་ལ་སོགས་པ་བཅིངས་པ་ཉིད་ཀྱི་ཡང་དག་པའི་དོན་བདེན་པ་ཉིད་ལ་ནི་ལྟུང་བ་མེད་པར༌[^1946]བལྟ་བར་བྱའོ། །

[Block 3022]
འདིར་རེག་པ་ལ་གཞན་འདྲེན་མའི་ཁ་ན་མ་ཐོ་བའི་མཚན་ཉིད་ཇི་ལྟ་བར་རྟོགས་པར་བྱའོ། །

[Block 3023]
འདིར་དགེ་སློང་ལ་ཆུང་བ་ཉིད་ཀྱི་ཕྱིར་འདི་དང་འབྲེལ་བའི་རྒྱུད་ལ་སྐྱེས་པ་ལ་ནི་ཉེས་བྱས་སུ་རིག་པར་བྱའོ། །

[Block 3024]
འདིར་ཡང་བྱ་བ་ཙམ་གཙོ་བོ་ཡིན་ཏེ། དེ་བས་ན་ཕྱེད་འགྲོལ་དུ་བཅུག་པ་ལ་ཡང་ལྟུང་བྱེད་འདིའོ། །

[Block 3025]
ལན་མང་པོ་འགྲོལ་དུ་འཇུག་ཅིང་སྒྱུ་ཐབས་ཀྱིས་བཀྲོལ་བ་ཇི་སྙེད་པ་དེ་རྣམས་ལ་ལྟུང་བྱེད་དུ་འགྱུར་རོ། །

[Block 3026]
རེག་པར་བྱ་བ་མ་ཡིན་པ་དང་བསྟེན་པ་ལས་གྱུར་པའི་ལྟུང་བྱེད་དེ་བཅུ་གཅིག་གོ། །།

[Block 3027]
[^1947]

[Block 3028]
གང་ལ་བུ་འཚོ་བའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་བུ་འཚོ་བ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བུ་ཕྲུག་འཚོ་ཞིང་རྩེ་བ་ལའོ། །

[Block 3029]
འདིར་གླེང་གཞི་ལས་ཁྱེའུ་ཞེས་སྨོས་པ་ནི་བུ་མོ་དང་མ་ནིང་གི་དཔེ་ཡིན་ཏེ། རྣམ་པར་འབྱེད་པ་ལས་ཀྱང་ཚིག་འདི་ཉིད་དོ། །

[Block 3030]
བུ་བཅང་བར་བྱ་སྟེ་ཁྱེའུ་ལ་ཉེ་གནས་བྱའོ། །

[Block 3031]
བུ་མོ་དང་མ་ནིང་དག་ལ་ནི་འཇུག་པའི་ཚུལ་འདྲའོ། །

[Block 3032]
དེ་ལྟ་བས་ན་འཇུག་པ་ཙམ་གཙོ་བོ་སྟེ། གླེང་གཞི་ལས་ནི་ཁྱེའུའི་ཚིག་གོ། །

[Block 3033]
དེའི་རྗེས་སུ་འགྲོ་བས་མཚོན་པ་ཙམ་གྱི་བསམ་པས་རྣམ་པར་འབྱེད་པ་ལས་བཤད་པའོ། །

[Block 3034]
བུ་ཐམས་ཅད་ནི་ཉེས་པ་ཡོངས་སུ་རྫོགས་པ་ཉིད་ཅེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 3035]
འདིར་ཡང་འཚོ་བར་ནི་ཁྱེའུ་ངུ་བར་ཤེས་པར་བྱ་བའི་ངོ་བོའམ་རྩེད་མོ་ལ་སོགས་པས་ཉེ་བར་གནས་པ་གང་ཡིན་པ་དེ་ལ་རྟོགས་པར་བྱའོ། །

[Block 3036]
གང་གི་བུ་ལ་རེག་པ་རྗེས་སུ་གནང་བའི་ཕྱིར་རང་གི་བུ་འཚོ་བ་ལ་ནི་ཉེས་པ་མེད་དོ། །

[Block 3037]
འདིར་དགེ་སློང་ལ་དམན་པ་ཉིད་ཀྱི་ཕྱིར་སྐྱེས་པ་ལ་མ་གྲུབ་པས་ཉེས་བྱས་སུ་རིག་པར་བྱའོ། །

[Block 3038]
བུ་འཚོ་བའི་ལྟུང་བྱེད་དོ།། །།

[Block 3039]
ད་ནི་འདི་མན་ཆད་ནི་གནོད་པར་འགྱུར་བའི་སྒོ་སྤང་བའི་ལྟུང་བྱེད་བཤད་པར་བྱ་སྟེ། སྐྱེས་པས་གནོད་པར་གྱུར་པ༌[^1948]གང་ཡིན་པ་དེ་འཇུག་པར་གྱུར་པའི་སྒོ་གང་ཡིན་པ་སྤང་བའི་ཕྱིར་རོ། །གང་ལ་དེ་རྣམས་ཀྱི་དང་པོ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ཁྱིམ་བདག་ལ་མ་དྲིས་པར་ཁྱིམ་གཞན་དུ་མཚན་མོ་འདའ་བར་བྱེད་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རང་གིས་ཀྱང་གནོད་པར་འགྱུར་བའི་ཁྱིམ་བདག་མ་མཐོང་བར་འདོད་ལ་རྩེ་གཅིག་པ་དེའི་ཁྱིམ་དུ་གཏོགས་པ་རྩིག་པ་ལ་སོགས་པས་བསྐོར་བའམ། གཞན་དུ་བཟློག་པའི་ཕྱིར་ཅི་ནས་ཀྱང་རྩོམ་པ༌[^1949]མེད་པ་ཞེས་བྱ་བ་འདི་བཏགས་སོ། །

[Block 3040]
བསྐོར་བ་ཙམ་གྱི་ཁྱིམ་ཉིད་གང་ཡིན་པ་དེ་ནི་འདིར་ཡན་ལག་ཏུ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 3041]
འདིར་བསྒྲིབས་པ་ཉིད་ནི་ཡན་ལག་མ་ཡིན་ཏེ། ཡང་གང་ཞིག་འདིར་བསྐོར་བ་ཉིད་དེ་ནི་ཁྱིམ་གྱི༌[^1950]མཐར་ཐུག་པར་རིག་པར་བྱའོ། །

[Block 3042]
ཕྱུགས་ལྷས་སམ་མགྲོན་ཁང་ལ་སོགས་པ་ལ་ཡང་ཁ༌[^1951]ན་མ་ཐོ་བ་འདི་འགྲུབ་པའོ། །

[Block 3043]
བུད་མེད་ལ་རག་ལས་པ་ཉིད་ཡིན་ན་དེ་ལ༌[^1952]དྲིས་ན་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ནི། ཁྱིམ་གང་བུད་མེད་དབང་ཆེ་ཞིང་ཁྱིམ་བདག་གི་བུད་མེད་ཀྱི་ཚིག་ལས་འདའ་བར་མི་ནུས་པ་དེ་ནི་བུད་མེད་ལ་རག་ལས་པ་ཉིད་ཅེས་བྱ་སྟེ། དེར་བུད་མེད་ལ་དྲིས་ནས་ཁྱིམ་བདག་ལ་མ་དྲིས་པར་མཚན་མོ་འདའ་བར་བྱེད་པ་ལ་ལྟུང་བ་མེད་པའོ། །

[Block 3044]
གང་ལ་ལྟུང་བྱེད་གཉིས་པར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་མཚན་མོ་མ་བརྟགས་པར་སྐྱབས་ཡོད་པར་འདའ་བར་བྱེད་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སྐྱབས་ཡོད་པ་ཞེས་བྱ་བ་ནི། རྣམ་པ་གང་ཡང་རུང་བས་མི་སྣང་བ་ཉིད་སྒྲུབ་པར་བྱེད་པ། མུན་ཁུང་དང་ཐིབས་པོ་ལ་སོགས་པ་འདིར་སྐྱབས་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 3045]
[^1953]རྟེན་ཉིད་ལ་ནི་མ་ཡིན་ནོ། །

[Block 3046]
མ་མཐོང་བ་གནས་པའི་སྐྱེས་པ་ཡོད་པ་དང་། མེད་པ་ཉིད་ཤེས་པར་བྱ་བའི་ཕྱིར་བརྟགས་པ་འདིའོ། །

[Block 3047]
དེ་ལྟ་བས་ན་སྐྱབས་ཡོད་པ་ལ་སོ་སོར་བརྟག་པར་བྱ་བ་མ་བྱས་པར་མཚན་མོ་འདའ་བར་བྱེད་པ་ལ་ལྟུང་བྱེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3048]
གང་ལ་བསླབ་པའི་གཞི་གསུམ་པར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་གནས་ཁང་དུ་དགེ་སློང་མ་གཞན་མེད་པར་མཚན་མོ་འདའ་བར་བྱེད་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། མཚན་མོ་གནས་ཁང་དུ་དགེ་སློང་མ་གཞན་མེད་པར་གཅིག་པུ་ཉལ་ཞིང་འདའ་བར་བྱེད་པ་ལ་ལྟུང་བྱེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 3049]
འདིར་གནས་ཁང་ཞེས་སྨོས་པ་ནི་དཔེ་ཙམ་དུ་ཟད་ཀྱི། གཡོགས་པའི་ཕྱོགས་ཀྱི་གནས་ཁང་གཞན་ཡང་བསྡུས་པ་ཡིན་ནོ། །

[Block 3050]
དུས་འདེབས་པ་དང་སྐྱེས་པས་གནོད་པར་འགྱུར་བའི་གཞན་དང་ལྷན་ཅིག་ཉེས་དམིགས་མཉམ་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །
--- END BLOCKS ---
