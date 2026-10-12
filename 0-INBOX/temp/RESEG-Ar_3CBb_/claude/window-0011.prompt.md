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
[Block 386]
ཞེས་པ་འདོད་ཆགས་དང་ལྡན་པའི་དབང་དུ་བྱས་པ་ནི་མ་ཡིན་གྱི། འདོད་ཆགས་དང་བྲལ་བའི་དབང་དུ་བྱས་པའི་ཕྱིར་རོ། །

[Block 387]
དེ་བས་ན་འདོད་རྒྱལ་གྱི་ཞགས་པས་ཟིན་པ་རྣམས་ནི་དགོས་པ་མེད་ཀྱང་རྩོམ་པར་འགྱུར་གྱི། དེ་བཞིན་གཤེགས་པ་ཐུགས་རྗེ་ཆེན་པོ་དང་ལྡན་པ་རྣམས་ནི་སེམས་ཅན་གྱི་དོན་དང་མི་ལྡན་པར་ནམ་ཡང་རྩོམ་མི་སྲིད་དོ། །

[Block 388]
དེ་བས་ན་དགོས་པ་ཐམས་ཅད་ནི་རྣམ་པ་གཉིས་ཏེ། འདོད་ཆགས་དང་བྲལ་བ་རྣམས་འདུལ་བ་དང་འདོད་ཆགས་དང་ལྡན་པ་རྣམས་འདུལ་བའོ། །

[Block 389]
དང་པོའི་དབང་དུ་བྱས་པ་ནི་བཤད་ཟིན་ཏོ། །

[Block 390]
གཉིས་པའི་དབང་དུ་བྱས་ནས་བཤད་པ།

[Block 391 [VERSE]]
རིགས་ལྔའི་སངས་རྒྱས་བསྐྱེད་པ་ནི། །
རྒྱུད་ཅེས་བྱ་བར་བརྗོད་པ་སྟེ། །

[Block 392]
ཞེས་པ་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་བདག་པོ་རྡོ་རྗེ་འཆང་ཆེན་པོ་ཡབ་ཡུམ་གཉིས་སུ་མེད་པའི་སྦྱོར་བ་ལས་རིགས་རྣམ་པ་ལྔ་ལ་སོགས་པ་བསྐྱེད་པ་འདི་ནི་རྒྱུད་ཅེས་བྱ་བའོ། །

[Block 393]
འདི་ལ་ཡང་ཅིའི་ཕྱིར་རྒྱུད་ཅེས་བརྗོད་ཅེ་ན་གཉིས་སུ་མེད་པའི་སྦྱོར་བའི་དབང་དུ་ནི་འབྲེལ་པའི་ཕྱིར་རྒྱུད་དོ། །

[Block 394]
རིགས་ལྔའི་སངས་རྒྱས་སྐྱེ་བའི་དབང་དུ་ནི་འབྱུང་ཁུངས་ཀྱི་ཕྱིར་རྒྱུད་དོ། །

[Block 395]
དཔེར་ན་རི་ལས་གསེར་འབྱུང་ཞེས་བརྗོད་ན་རི་གསེར་གྱི་རྒྱུད་དུ་གཏོགས་པ་ལྟ་བུར་རིགས་ལྔའི་སངས་རྒྱས་བསྐྱེད་པས་ཐམས་ཅད་དེ་བཞིན་གཤེགས་པའི་རྒྱུད་དང་། འདོད་ཆགས་ཆེན་པོའི་ཆོས་དང་ལྡན་པའི་རྒྱུད་དུ་གཏོགས་པར་ཤེས་པར་བྱའོ། །

[Block 396]
གླེང་གཞི་ཡང་གང་ཞིག་ཡིན་ཞེ་ན།

[Block 397 [VERSE]]
སླར་ཡང་རིགས་གཅིག་གྱུར་པ་ནི། །
གླེང་གཞི་ཡིན་པར་རབ་ཏུ་བཤད། །

[Block 398]
ཅེས་པའོ། །

[Block 399]
དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་རིགས་བརྒྱའི་དབྱེ་བ༌[^195]ལ་རབ་ཏུ་བཞུགས་ནས་སླར་ཡང་རྡོ་རྗེ་བསྡུ་བའི་སྦྱོར་བས་བསྡུས་ཏེ། རིགས་གཅིག་ཏུ་གྱུར་པ་ནི་གླེང་གཞི་ཞེས་བརྗོད་དོ། །

[Block 400 [VERSE]]
རྡོ་རྗེ་ལ་སོགས་བཟུང་བ་ནི། །
ངེས་པའི་ཚིག་ཏུ་བརྗོད་པ་སྟེ། །

[Block 401]
ཞེས་པ་ནི་རྡོ་རྗེ་འཛིན་པའི་ཕྱིར་རྡོ་རྗེ་འཆང་ཆེན་པོའོ། །ཅིའི་ཕྱིར་རིན་ཆེན་འཆང་ཞེས་བྱ་ཞེ་ན། ཡིད་བཞིན་གྱི་ནོར་བུ་རིན་པོ་ཆེ་འཆང་བའི་ཕྱིར་རིན་ཆེན་འཆང་ཞེས་པའོ། །

[Block 402]
འདི་དག་གི་དོན་ནི་འོག་ནས་བཛྲ་དྷྲིཀ་ཅེས་བྱ་བ་ལ་སོགས་པའི་སྔགས་ཀྱི་དོན་བཤད་པ་ལས་ཤེས་པར་བྱའོ། །

[Block 403]
འདི་དག་གི་རྒྱུ་ཡང་གང་ཞིག་ཡིན་ཞེས་པའི་ལན་དུ།

[Block 404 [VERSE]]
སྒེག་པ་ལ་སོགས་སྤྱོད་པ་ནི། །
རྒྱུ་ཞེས་བྱ་བར་བརྗོད་པ་སྟེ། །

[Block 405]
ཞེས་པ་སྒེག་པ་དང་འཇོ་བ་ལ་སོགས་པ་ནི་སངས་རྒྱས་ཐམས་ཅད་ཀྱི་སྐྱེ་བའི་རྒྱུར་གྱུར་ཞེས༌[^196]པའི་དོན་ཏོ། །

[Block 406]
རིགས་པ་ཡང་ནི་འདས་ཟིན་ཏེ། །ཞེས་པ་ནི་རིགས་རྣམ༌[^197]པ༌[^198]བཞི་ནི་བཤད་ཟིན་ཏོ། །

[Block 407]
རྒྱན་ནི་གསུམ་པ་ཉིད་ཀྱང་ནི། །ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་རིགས་པ་རྣམ་པ་བཞི་བཤད་པའི་འོག་ཏུ་མཐའ་རྣམ་པ་དྲུག་བཤད་པར་རིགས་པས་དེ་བཤད་པར་བྱའོ། །

[Block 408]
མཐའ་ཡང་ཡིན་ལ་དྲུག་ཀྱང་ཡིན་པས་མཐའ་རྣམ་པ་དྲུག་སྟེ། མཐའ་དྲུག་གི་ཚིག་ཅེས་པ་ནི་དོན་མ་ཡིན་ཞེས་པའོ། །

[Block 409]
དེས་ངེས་པར་བྱས་པ་ནི་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་གསང་བ་འདུས་པ་མཐའ་དྲུག་གིས་རྒྱས་བཏབ་པ་གང་ཡིན་པ་དེ་ནི༌[^199]འདིས་རྟོགས་པར་བྱེད་དོ་ཞེས་པའི་དོན་ཏོ། །

[Block 410]
མཐའ་དྲུག་པོ་ཉིད་གང་ཡིན༌[^200]ཞེ་ན། དྲང་བ་དང་ནི་ངེས་དོན་བཅས། །ཞེས་བྱ་བ་སྨོས་ཏེ་འདི་དག་ལ་ཡང་ཅིའི་ཕྱིར་མཐའ་ཞེས་བྱ་ཞེ་ན། འདི་ལྟར་ཆོས་འགལ་བ་རྣམ་པར་གནས་པའི་ཕྱིར་མཐའ་སྟེ་གང་ཞིག་ཡོངས་སུ་གཅོད་པ་མེད་ན་གང་ཞིག་རྣམ་པར་གཅད་པ༌[^201]མེད་དེ། དེ་ནི་ཕན་ཚུན་སྤངས་ཏེ་གནས་པའི་མཚན་ཉིད་ཅན་གྱི་འགལ་བ་ཡིན་ཏེ། རྟག་པ་དང་མི་རྟག་པ་བཞིན་ནོ། །

[Block 411]
དྲང་བ༌[^202]དང་ངེས་པའི་དོན་རྣམ་པ་གཉིས་ཀྱང་ཡོངས་སུ་གཅོད་པ་མེད་ན་རྣམ་པར་བཅད་པ་མེད་པའི་ཕྱིར་འགལ་བ་ཡིན་ནོ། །

[Block 412]
དེ་བས་ན་དྲང་བའི་དོན་ལ༌[^203]ཇི་ལྟ་བ་བཞིན་དུ་སྒྲ་ཇི་བཞིན་པ་ལ་སོགས་པ་ལ་ཡང་ཤེས་པར་བྱ་སྟེ། འདི་ལྟར་དྲང་བའི་དོན་དང་ངེས་པའི་དོན་རྣམ་པ་གཉིས་ནི་དོན་གཅིག་གིས་གཅིག་སྤངས་པའི་མཐའ་ཡིན་ནོ། །

[Block 413]
སྒྲ་ཇི་བཞིན་པ་དང་ཇི་བཞིན༌[^204]མ་ཡིན་པ་རྣམ་པ་གཉིས་ནི་དོན་ལ་མ་ངེས་པའི་ཕྱིར་སྒྲ་མཐའ་ཞེས་བྱའོ། །

[Block 414]
དགོངས་པས་བཤད་པ་དང་དགོངས་པ་མ་ཡིན་པས་བཤད་པ་ནི་སྒྲ་དང་དོན་རྣམ་པ་གཉིས༌[^205]གསལ་བར་གནས་པའི་ཕྱིར་གཉི་ག་མཐའ་ཞེས་སྦྱར་རོ། །

[Block 415]
མཐའ་ཡང་ཡིན་ལ་དྲུག་ཀྱང་ཡིན་པས་འདི་ནི་མཐའ་རྣམ་པ་དྲུག་གོ། །

[Block 416]
དེ་ནས་མཐའ་དྲུག་གི་རང་རང་གི་མཚན་ཉིད་བསྟན་པའི་ཕྱིར་ཐེ་ཚོམ་དང་། མ་རྟོགས་པ་དང་ལོག་པར་རྟོག་པ་སེལ་ནུས་པའི་གང་ཟག་ཅིག་སློབ་དཔོན་གྱི་གན་དུ་འོངས་ཏེ། འདི་སྐད་ཅེས་འདྲིའོ། །

[Block 417]
དྲང་བའི་དོན་ཞེས་བྱ་བ་གང་ཞིག༌[^206]ཡིན། ཅི་ཕྱིར༌[^207]དྲང་བའི་དོན་དུ་བརྟག་ཅེ་ན་བཤད་པ། །

[Block 418 [VERSE]]
སྐལ་ངན་རྣམས་ལ་རྒྱལ་བ་ཡིས། །
སྦས་ཏེ་བཤད་པ་དྲང་བའི་དོན། །

[Block 419]
ཞེས་པ་སྐལ་བ་ངན་པ་ནི་སྐལ་བ་ངན་པ་སྟེ་ཉན་ཐོས་ཀྱི་རིགས་ཅན་ལ་སོགས་པའོ། །

[Block 420]
ཡང་ན་སྐལ་བ་ངན་པ་ནི་རྣམ་པ༌[^208]གཉིས་ཏེ། དངོས་སུ་སྐལ་བ་ངན་པ་ལ་ལྟོས༌[^209]ནས་སྐལ་བ་ངན་པའོ། །

[Block 421]
དངོས་སུ་སྐལ་བ་ངན་པ་ནི་རིགས་ཆད་པའི་གང་ཟག་འབའ་ཞིག་གོ། །

[Block 422]
རིགས་ཆད་པའི་ཞེས་བྱ་བ་ཡང་ས་བོན་དང་བྲལ་བ་ནི་མ་ཡིན་གྱི། ཉོན་མོངས་པའི་སྤྱོད་པ་འབའ་ཞིག་ལ་ལྟོས༌[^210]ནས་སྐལ་བ་ངན་པ་ནི་རྣམ་པ་གཉིས་ཏེ། དངོས་སུ་ན༌[^211]ཉན་ཐོས་ལ་སོགས་པའི་ཕྱིའི་ཕྱོགས་སུ་གཏོགས་པ་དང༌[^212]ཚོགས་ཀྱི་གང་ཟག་ནང་པའི་ཕྱོགས་སུ་གཏོགས་པའོ། །

[Block 423]
འདི་དག་ལ་ཡང་ཅིའི་ཕྱིར་སྐལ་བ་ངན་པ་ཞེས་བྱ་ཞེ་ན། དམ་པའི་ཆོས་ཟབ་ཅིང་རྒྱ་ཆེ་བ་ཉན་པའི༌[^213]སྐལ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 424]
སྐལ་བ་མེད་པའི་ཕྱིར་རིགས་ཆད་པ་མ་ཡིན་ནམ། ཅིའི་ཕྱིར་ལྟོས༌[^214]ནས་སྐལ་བ་ངན་པ་ཞེས་བྱ་ཞེ་ན། རིགས་ཆད་པ་ཞེས་བྱ་བ་ནི་ཐམས་ཅད་ཀྱི་འབྲས་བུ་མི་ཐོབ་པ་གང་ཡིན་པའོ། །

[Block 425]
འགའ་འགས་ཀྱང་ནི༌[^215]མི་ཐོབ་པ་ནི་མ་ཡིན་ནོ། །
--- END BLOCKS ---
