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
[Block 5776]
དེ་དང་དེ་དག་ཅེས་བྱ་བ་ནི་ཡོན་ཏན་གཞན་དག༌[^3695]ཡང་ལྡན་པ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 5777]
ཡོན་ཏན་ཡོད་པ་ནི་ཞེས་བྱ་བ་ནི་ཡོན་ཏན་ཉིད་ཡོད་པ་ཡིན་ཏེ།

[Block 5778 [VERSE]]
དེའི་ཡོན་ཏན་མང་པོ་ཞེས་བྱ་བའི་དོན་ཏོ། །
ལང་ཚོར་གྱུར་པའི་རྒྱན་གྱིས་བརྒྱན་པ་བཞིན། །

[Block 5779]
ཞེས་བྱ་བ་ནི། བྱང་ཆུབ་སེམས་དཔའི་རྒྱན་གྱིས་བརྒྱན་པའི་ལང་ཚོ་བཞིན་དུ་ཞེས་བྱ་བའི་དོན་ཏེ། [^3696]ལང་ཚོ་ནི་ད་ལྟར་བྱུང་བའི་ཡོན་ཏན་གྱིས་མཛེས་པ་ཡིན་ཏེ། དེ་བས་ན་ཡོན་ཏན་ལང་ཚོའི་རྒྱན་གྱིས་བརྒྱན་པ་ཉིད་དོ། །

[Block 5780]
ཡང་ན་ལང་ཚོར་གྱུར་པའི་རྒྱན་གྱིས་བརྒྱན་པ་བཞིན་དུ་ཡོན་ཏན་གསར་པ་དག་གིས་རབ་ཏུ་བརྒྱན་པ་སྟེ། དེ་བས་ན་ལང་ཚོར་གྱུར་པའི་རྒྱན་གྱིས་བརྒྱན་པ་ཞེས་བརྗོད་དོ། །

[Block 5781]
རྣམ་པར་དག་པ༌[^3697]ཡང་ཡིན་ལ་རྒྱ་ཆེ་བ་ཡང་ཡིན་པས་རྣམ་པར་དག་ཅིང་རྒྱ་ཆེ་བའོ། །

[Block 5782]
རྣམ་པར་དག་པ་དང་། རྒྱ་ཆེ་བ་གཉིས་ཀྱིས༌[^3698]ཡིད་དུ་འོང་བ་དེ་ནི་རྣམ་པར་དག་ཅིང་རྒྱ་ཆེ༌[^3699]ཡིད་དུ་འོང་བ་སྟེ། དེ་བཞིན་དུ་དེའི་ཡོན་ཏན་རྣམས་སོ། །

[Block 5783]
གནས་སུ་གྱུར་ཅེས་བྱ་བ་འདིས༌[^3700]ནི་ཡོན་ཏན་གྱི་འོད་ཟེར་བརྒྱ་དང་ལྡན་པའི་གནས་སུ་གྱུར་པའི་ཕྱིར་ཏེ། འདིས་ནི་གསང་ཚིག་གི་ནུས་པ་བསྟན་ཏོ། །

[Block 5784]
འབངས་རྣམས་སྐྱོང་ནུས་པ་དང་ཞེས་བྱ་བ་འདིས་ནི་སྤྲོ་བའི་ནུས་པ་བསྟན་ཏོ། །

[Block 5785]
མ་འཇུངས་ཤིང་རང་བཞིན་བཟང་བའི་ཕྱིར་ཞེས་བྱ་བ་འདིས་ནི་རྒྱུ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 5786]
རང་བཞིན་དང་རྒྱུ་དང་ས་བོན་ཞེས་བྱ་བ་ནི་དོན་གཞན་མ་ཡིན་ཏེ། འདིས་ནི་དེ་ཉིད་ཀྱི་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 5787]
དང་པོ་འདི་གཉིས་ཀྱིས་ནི་སྐྱེས་བུའི་བྱེད་པ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 5788]
རྒྱལ་ཚབ་ཀྱི་ལོངས་སྤྱོད་ཅེས་བྱ་བ་ནི་བདག་པོའི་ནུས་པ་བྱེད་དུ་བཅུག་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 5789]
རབ་ཏུ་མཁས་པས་ཞེས་བྱ་བ་ནི་སྔར་བསྟན་པའི་ཐོས་པ་དང་། ཤེས་རབ་དང་། ཡིད་གཞུངས་ཤིང་མངོན་པར་བརྩོན་པའི་སྦྱོར་བས་སོ། །

[Block 5790]
མཁས་པས་ཆོས་ལྡན་ཞེས་བྱ་བ་ནི་དོན་དང་འདོད་པ་དང་ཡང་ལྡན་པ་ཡིན་ནོ། །

[Block 5791]
ལེགས་པར་སྨྲ་བ་ལ་ཇི་ལྟར་བྱེད་ཅེ་ན། མཆོད་པ་ཁྱད་པར་ཅན་གྱིས་ཞེས་བྱ་བ་ཡིན་ཏེ། དེས་ན་དེ་ཉིད་ཀྱི་ཕྱིར་ཏེ། ལེགས་པར་བཤད་པ་ལ་དགའ་བའི་ཕྱིར་རོ། །

[Block 5792]
དཔྱིད་ཟླའི་དུས་ལ་བབ་པ་ཞེས་བྱ་བ་ནི་མེ་ཏོག་འབྱུང་བའི་དུས་ཀྱི་ཟླ་བ་ལ་བབ་པའོ། །

[Block 5793]
ཤིང་ལོ་རྣམས་མཛེས་ཤིང་འཇམ་པོར་གྱུར་པ་གང་ཡིན་པ་དེ་དག་ནི་དཔྱིད་ཟླའི་དུས་ལ་བབ་པའི་མཐུས་ཤིང་ལོ་རྣམས་མཛེས་ཤིང་འཇམ་པོར་གྱུར་པའོ། །

[Block 5794]
མེ་ཏོག་ཉིད་ཁ་འབུས་པས་སྡུག་ཅིང་། དགོད་པ་ལྟར་གྱུར་པ་གང་ཡིན་པ་དེ་ནི་མེ་ཏོག་སྡུག་གུ་ཁ་འབུས་པ་རྣམས༌[^3701]ནི་དགོད་པ་བཞིན་ནོ། །

[Block 5795]
ནེའུ་གསིང༌[^3702]སྔོན་པོ་ནི་ནེའུ་གསིང༌[^3703]སྔོན་པོའོ། །

[Block 5796]
དེ་ཉིད་ཀྱི༌[^3704]རི་མོ་བཀྲམ་པ་ལྟ་བུ་ཡིན་པས་ནེའུ་གསིང༌[^3705]སྔོན་པོ་གསར་པ་རྣམས་ཀྱིས་རི་མོ་བཀྲམ་པའོ། །

[Block 5797]
དེས་ས་གཞི་མཛེས་པར་བྱས་པ་གང་ཡིན་པ་དེ་ནི། ས་གཞི་ནེའུ་གསིང༌[^3706]སྔོན་པོ་གསར་བུ༌[^3707]རྣམས་ཀྱིས་རི་མོ་བཀྲམ་པ་བཞིན་དུ་མཛེས་པར་བྱས་པའོ། །

[Block 5798]
ཡིད་དགའ་བ་འབྱུང་བ་ཡིན་པས་ཡིད་དགའ་བ་སྐྱེས་པའོ།[^3708] །སྐྱེད་མོས་ཚལ་ན་ལྡིང་ཁང་ཡོད་པ་དེ་ནི་ལྡིང་ཁང་སྐྱེད་མོས་ཚལ་ལོ། །

[Block 5799]
ཡིད་དུ་འོང་བའི་ལྡིང་ཁང་གི་རྒྱན་སྐྱེད་མོས་ཚལ་གང་ལ་ཡོད་པ་དེ་ནི་ལྡིང་ཁང་རྒྱན་ཅན་སྐྱེད་མོས་ཚལ་ལོ། །

[Block 5800]
བུད་མེད་རྣམས་ཀྱི་གླུ་སྒྲ་སྙན་དང་འབྲེལ། །ཞེས་བྱ་བ་ནི་རྣ་བའི་ཡུལ་གྱི་ལོངས་སྤྱོད་ཀྱི་དབང་དུ་བྱས་པའོ། །

[Block 5801]
འཛུམ་ལ་མཁས་པ་ཞེས་བྱ་བ་ནི་མིག་གི་ཡུལ་གྱི་ལོངས་སྤྱོད་ཀྱི་དབང་དུ་བྱས་པའོ། །

[Block 5802]
ཡན་ལག་མཛེས་པར༌[^3709]བསྒྱུར་བའི་ཞེས་བྱ་བ་ནི་རེག་བྱའི་ལོངས་སྤྱོད་ཀྱི་དབང་དུ་བྱས་པའོ། །

[Block 5803]
བཟང་མོ་མཛེས་པར་ཞེས་བྱ་བ་ནི༌[^3710]ལོངས་སྤྱོད་ཀྱི་དབང་དུ་བྱས་པ་སྟེ། དེ་ལྟར་འདི་དག་གིས་ནི་སེམས་ཅན་གྱི་ལོངས་སྤྱོད་ཀྱི་རྐྱེན༌[^3711]བསྟན་པའོ། །

[Block 5804]
ད་ནི་སེམས་ཅན་མ་ཡིན་པའི་ལོངས་སྤྱོད་ཀྱི་དབང་དུ་བྱས་ནས། སྐྱེད་མོས་ཚལ་བཟང་དེ་ན་དེ་ནི་དགའ་བར་གནས། །ཞེས་བྱ་བ་སྨོས་ཏེ། མིག་དང་། རྣ་བ་དང་། སྣའི་ལོངས་སྤྱོད་ཀྱི་དབང་དུ་བྱས་པའོ། །

[Block 5805]
ལང་ཚོ་ལ་བབ་པ་ནི་ཞེས་བྱ་བ་ནི་འདིའི་འདོད་པའི་ཡུལ་ལ་ཆགས་པ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 5806]
བསོད་ནམས་ཕུན་སུམ་ཚོགས་པའི་མཐུ་ལས་བྱུང་བ་ཞེས་བྱ་བ་ནི་སྦྱིན་པ་དང་། ཚུལ་ཁྲིམས་ལ་སོགས་པའི་བསོད་ནམས་ཕུན་སུམ་ཚོགས་པའི་ཁྱད་པར་དུ་གྱུར་པ་སྟེ། དེའི་མཐུ་ནི་བསོད་ནམས་ཕུན་སུམ་ཚོགས་པའི་མཐུའོ། །

[Block 5807]
དེ་ལས་བྱུང་བ་ནི་བསོད་ནམས་ཕུན་སུམ་ཚོགས་པའི་མཐུ་ལས་བྱུང་བ་སྟེ། འདིས་ནི་འབད་པ་མེད་པར་བྱུང་བ་ཉིད་དེ་རྒྱུའི་སྟོབས་ལས་བྱུང་བ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 5808]
རོལ་མོའི་དགའ་བ་ལ་གནོད་པ་ཞེས་བྱ་བ་ནི་སྔར་སྐྱེས་པའི་དགའ་བ་ཉམས་པ་ཡིན་ཏེ། བུད་མེད་དང་སྐྱེས་པ་རྣམས་ཀྱི༌[^3712]བསྟན་ནས། ད་ནི་བུད་མེད་ཀྱི་དབང་དུ་བྱས་ནས། བུད་མེད་གཞོན་ནུ་རྣམས་འཇིགས་ཤིང་བག་འཁུམས་པར་བྱེད་པ་ཞེས་བྱ་བས་བསྟན་ཏོ། །

[Block 5809]
མིའི་སྟོབས་དང་། མཐུ་རྩལ་ལ་སོགས་པ་ལས་འདས་པ་གང་ལ་ཡོད་པ་དེ་ནི་སྟོབས་དང་། མཐུ་རྩལ་ལ་སོགས་པ་མི་པས་ལྷག་པའོ། །

[Block 5810]
སྲིན་པོ་དག་པས་ཀྱང་ལྷག་པར་མི་བཟད་པའི་གཟུགས་གང་ལ་ཡོད་པ་དེ་ནི། སྲིན་པོ་བས་ཀྱང་ལྷག་པར་མི་བཟད་པའི་གཟུགས་ཅན་ནོ། །

[Block 5811]
ཤིང་རྟ་དང་། རྟ་དང་། གླང་པོ་ཆེ་དང་། དམག་མི་བརྟན་པ་ཉམས་པར་གྱུར་པ་གང་ཡིན་པ་དེ་ནི། ཤིང་རྟ་དང་། རྟ་དང་། གླང་པོ་ཆེ་དང་། དམག་མི་བརྟན་པ་ཉམས་པར་གྱུར་པའོ། །

[Block 5812]
ཅི་ལེགས་མཛད་པ་ནི་གོ་ཆ་བགོ་བ་ལ་སོགས་པའོ། །

[Block 5813]
ངང་ཚུལ་གྱི་སྐྱོན་ཤེས་པ་གང་ཡིན་པ་དེ་ནི་དེ་སྟེ། ངང་ཚུལ་གྱི་སྐྱོན་ནི་མ་བསྔགས་པའི་དངོས་པོ་ཡིན་ནོ། །

[Block 5814]
སྔར་ཆབ་སྒོ་པས་བསྟེན་པའི༌[^3713]སྟེ། ལྷ་དེ་ལས་ཅི་ལེགས་པར་མཛད་ཅིང་བཀའ་གྲོས་མཛད་པའི་དུས་ལ་བབ་པོ་ཞེས་གསོལ་ཏོ་ཞེས་བྱ་བ་དེ་གཉི་ག་དུས་ལ་བབ་པ་ཉིད་དུ་བསྟན་པ་དེའི་དེ་ལྟར་མི་བྱ་བའི་རྒྱུ་ཉིད་དུ་བསྟན་པའི་ཕྱིར། མི་ཤ་འདོད་པ་ཞེས་བྱ་བ་དང་། བདག་གིས་བརྒལ་བའི་གོ་སྐབས་ཞེས་བྱ་བའི་ཚིགས་བཅད་གཉིས་སྨོས་སོ། །

[Block 5815]
མི་ཤ་འདོད་པས་རྒྱལ་སྲིད་ཉམས་པར་གྱུར། །ཞེས་བྱ་བས་ནི་འདོད་པ་ཉམས་པ་ཉིད་དུ་སྟོན་ཏོ། །
--- END BLOCKS ---
