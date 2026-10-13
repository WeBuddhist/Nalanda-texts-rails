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
[Block 2311]
དེ་ཉིད་གསལ་བར་སྟོན་པ་ནི་ཞེས་པ་ལ་རབ་ཏུ་གྲགས་པའི་དེ་ཁོ་ན་ཉིད་བཤད་པའོ། །

[Block 2312]
དགོངས་པ་མིན་པས་བཤད་པའོ། །ཞེས་པ་ནི་འགལ་བའི་སྒྲ་མེད་པར་གསུངས་ཞེས་ཐ་ཚིག་གོ། །

[Block 2313]
འདི་ནི་དོན་གྱི་རྒྱན་ཡིན་ཏེ། དོན་ཁོ་ན་བརྒྱན་པར་བྱ་བ་ཡིན་པས་སོ། །

[Block 2314]
དཀྱིལ་འཁོར་ལ་སོགས་དང་ཞེས་པ་ནི་དཀྱིལ་འཁོར་སྣ་ཚོགས་འདྲི་བ༌[^1526]དང་། ཚད་ལ་སོགས་པའི་ཚིག་རྣམས་ལའོ། །

[Block 2315]
དེ་བཞིན་དུ་རྟོག་པ་ནི་གཤིན་རྗེ་གཤེད་ལ་སོགས་པའི་སྒོམ་པས་རྣམ་པར་སྡང་བ་ལ་སོགས་པ་ལས་ཀྱི་རབ་འབྱམས་སྟོན་པར་བྱེད་པ་ལའོ། །

[Block 2316]
སྤྱོད་པ་ནི་སྤྲོས་བཅས་ལ་སོགས་པའོ། །

[Block 2317]
ཇི་ལྟ་ཇི་ལྟར་གསུངས་ཞེས་པ་ནི་དེ་དང་དེ་སྟོན་པར་བྱེད་པའི་ཚིག་དག་ལའོ། །

[Block 2318]
དོན་ཟབ་མིན་བཤད་གང་ཡིན་པ། ཞེས་པ་ནི་དེ་ཁོ་ན་ཉིད་ཀྱི་དོན་དང་བྲལ་ཞིང་ཕྱིའི་སྤྲོས་པ་ཙམ་སྟོན་པར་བྱེད་པའོ། །

[Block 2319]
དེ་ནི་ཇི་བཞིན་སྒྲར་གསུངས་པའོ། །ཞེས་པ་ལ་སྒྲ་ཇི་ལྟར་ཡོད་པ་དེ་དང་འདྲ་བའི་དོན༌[^1527]སྟོན་པའོ། །

[Block 2320]
འདི་ཡང་སྒྲ་ཡི་རྒྱན༌[^1528]ཡིན་ཏེ། །ཇི་སྐད་དུ།

[Block 2321 [VERSE]]
ཐུགས་ཀྱི་དཀྱིལ་འཁོར་དམ་པ་སྟེ། །
ཁྲུ་ནི་བཅུ་གཉིས་ཚད་དུ་བྱ། །

[Block 2322]
ཞེས་གསུངས་པས་དེ་ལས་མང་བའམ་ཉུང་བར་མི་བྱའོ། །

[Block 2323]
དེ་བཞིན་དུ་རྟོག་པ༌[^1529]དང་དཔྱོད་པ༌[^1530]དག་ལས་ཤེས་པར་བྱའོ། །

[Block 2324]
ཀོ་ཊ་ཀྵ་ལ་སོགས་པ་ནི་འདིར་སྒྲ་གཉིས་ཏེ། འཇིག་རྟེན་པ་དང་། བསྟན་བཅོས་པའོ། །

[Block 2325]
དེ་ལ་འཇིག་རྟེན་པ་ནི། དཔེར་ན་བ་ལང་དང་རྟ་དང་སྐྱེས་པ་དང་བྱ་དང་རི་དགས་དང་གླང་པོ་ཆེ་དང་བྲམ་ཟེ་ཞེས་བྱ་བ་དང་། བསྟན་བཅོས་པ་ནི་དཔེར་ན་བདེན་པ་དང་དཀོན་མཆོག་གསུམ་དང་། དེ་བཞིན་ཉིད་དང་ཡང་དག་པའི་མཐའ་དང་སྟོང་པ་ཉིད་དོ་ཞེའོ།[^1531] །

[Block 2326]
ཀོ་ཊ་ཀྵ་ལ་སོགས་པ་ནི་འཇིག་རྟེན་པ་ཡང་མ་ཡིན་ལ། བསྟན་བཅོས་པ་ཡང་མ་ཡིན་ནོ། །

[Block 2327]
དེ་ལྟ་ཡིན་ན་ཅིའི་ཕྱིར་བརྗོད་ཅེ་ན། དེ་བཞིན་གཤེགས་པ་ཞེས་པ་ནི་རང་གིས་གླེགས་བམ་ལྟ་བ་རྣམས་ལ་འཁྲུལ་པ་བསྐྱེད་པར༌[^1532]བྱ་བའི་ཕྱིར་བཅོམ་ལྡན་འདས་དེ་བཞིན་གཤེགས་པ་རྩ་བ་དང་ཡན་ལག་གི་རླུང་རྣམས་ཀྱི་དེ་དག་བརྡར་གསུངས་སོ། །

[Block 2328]
དཔེར་ན་བྷུ་སུ་ཀོ༌[^1533]བཞིན་ནོ། །

[Block 2329]
ཟ་བ་དང་ཉལ་བ་དང་འཆག་ཏུ་འགྲོ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2330]
དེ་ནི་ཇི་བཞིན་མིན་སྒྲར་གྲགས། །ཞེས་པ་ནི་དོན་བརྗོད་པ་ལ་སྒྲ་མི་འདྲ་བའི་ཕྱིར་རོ། །

[Block 2331]
འདི་ཡང་སྒྲ་ཡི་རྒྱན་ཡིན༌[^1534]ཏེ། བརྡ་ཡང་སྒྲ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2332]
དེ་ལྟ་ན་སྒྲ་ཇི་བཞིན་པ་དང་དྲང་བའི་དོན་ལ་བྱེ་བྲག་གང་ཞེ་ན། སྨྲས་པ། སྒྲ་དང་དོན་གྱི་རྒྱན་གྱི་དབྱེ་བས་སོ། །

[Block 2333]
དྲང་བའི་དོན་དང་དགོས་པ་མ་ཡིན་པ་དག་གི་ཁྱད་པར་གང་ཞེ་ན། མི་གསལ་བ་དང་གསལ་བའི་བྱེ་བྲག་གིས་སོ། །

[Block 2334]
སྒྲ་ཇི་བཞིན་པ་དང་། དགོངས་པས་བཤད་པ་དག་གི་ནི། མི་འགལ་བ་དང་འགལ་བའི་སྒྲའི་དབྱེ་བས་སོ། །

[Block 2335]
ངེས་པའི་དོན་དང་། [^1535]དགོངས་པ་མ་ཡིན་པ་དག་གི་ནི། དབང་པོ་རྣོ་བ་དང་དབང་པོ༌[^1536]དམན་པའི་གང་ཟག་གི་དབྱེ་བས་སོ། །

[Block 2336]
དགོངས་པ་དང་སྒྲ་ཇི་བཞིན་མ་ཡིན་པ་དག་གི་ནི་འགལ་བ་དང་མ་གྲགས་པ་དག༌[^1537]གི་སྒྲའི་དབྱེ་བས་སོ། །

[Block 2337]
དེ་ལྟར་དྲང་བ་དང་ངེས་པའི་དོན་དང་དགོངས་པ་མ་ཡིན་པ་ནི༌[^1538]དོན་གྱི་རྒྱན་ནོ། །

[Block 2338]
དགོངས་པས་བཤད་པ་དང་སྒྲ་ཇི་བཞིན༌[^1539]མ་ཡིན་པ་ནི་སྒྲའི་རྒྱན་ཞེས་མཐའ་དྲུག་གི་དབྱེ་བ་ཞེས་བྱ་བ་བཤད་པའི་བྱེ་བྲག་བསྟན་ཏོ། །

[Block 2339]
རིམ་པ་གཉིས་པོ་གཅིག་པུ་སྟོན་པར་བྱེད་པ་བཤད་པའི་རྣམ་པ་བསྟན་པར་བྱ་བའི་ཕྱིར། བཤད་པའི་དབྱེ་བ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་སོ། །

[Block 2340]
ཡི་གེ་དོན་ཞེས་བྱ་བ་ལ་སོགས་པས་མདོར་བསྟན་པའོ། །

[Block 2341]
དང་པོ་གཅིག་པུ་ཁོ་ན་ཉིད། །ཅེས་བྱ་བ་ལ་སོགས་པས་གྲངས་སྔོན་དུ་འགྲོ་བས་རྒྱས་པར་བཤད་པའོ། །

[Block 2342]
ཀུན་དུ་བསྡུས་ཏེ་རྣམ་པ་བརྒྱད་དུ་འགྱུར་རོ། །

[Block 2343]
སོ་སོར་བསྟན་པར་བྱ་བའི་ཕྱིར། སྒྲ་ཙམ་ལ་ནི་རབ་གཞོལ་བ། །ཞེས་པ༌[^1540]ནི་སྒྲ་ཙམ་ལ་མངོན་པར་ཞེན་པའོ། །

[Block 2344]
ཕྱི་རོལ་བསྟན་བཅོས་མཁས་པ་ཡིས། །ཞེས་པ་ནི་རྟོག་གེ་དང་སྒྲའི་བསྟན་བཅོས་ལ་སོགས་པར་བྱེད་པའི་ཚིག་དང་བྱེད་པ་པོ་དང་རྟགས་དང་བསྡུ་བ་ལ་སོགས་ལ་མཁས་པའོ། །

[Block 2345]
དེ་ཡི་སྒྲུབ་པ་རབ་སྟོན་པ། །ཞེས་པ་ནི་དེ་དང་རྗེས་སུ་མཐུན་པའི་བསྟན་པ་བཅོམ་ལྡན་འདས་ཀྱིས་གང་བསྟན་པ་དེ་ནི་ཡི་གེའི་དོན་ཏེ། ཡི་གེ་ཙམ་གྱི་དོན་བརྗོད་ཅིང་བརྗོད་པར་བྱ་བ་གང་ཡང་རུང་བ་སྟེ། རྫོགས་པའི་རིམ་པ་སྤངས་པའི་བསྐྱེད་པའི་རིམ་པའི་ཕྱོགས་གཅིག་གི་མཚན་ཉིད་དོ། །

[Block 2346]
དེ་བས་འདི་སྒྲའི་རྒྱན་ཡིན་ཏེ། སྒྲ་སྣ་ཚོགས་པ་ཙམ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2347]
སྤྱིའི་དོན་བསྟན་པར་བྱ་བའི་ཕྱིར། མདོ་སོགས་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། མདོ་སྡེ་ལ་སོགས་པ་ནི་ཉན་ཐོས་དང་མདོ་སྡེ་པ་དང་རྣལ་འབྱོར་སྤྱོད་པ་དང་། དབུ་མ་པ་རྣམས་སོ། །

[Block 2348]
གང་གི་ཚེ་སྔོན་གྱི་བག་ཆགས་ཀྱི་འབྲེལ་པའམ། དགེ་བའི་བཤེས་གཉེན་དང་ཕྲད་པས་སྔགས་ཀྱི་ཐེག་པ་ཆེན་པོ་བསྟན་པར་གྱུར་པ་དེའི་ཚེ་རང་གི་སྡོམ་པ་དང་འགལ་བའི་དམ་ཚིག་དང་སྡོམ་པ་ཐོས་ནས་འགྱོད་པར་གྱུར་པས་གསང་སྔགས་ཀྱི་གསུང་ལ་སྐུར་བ༌[^1541]བཏབ་པའི་སྡིག་པ་མེ་ལ་ཕྱེ་མ་ལེབ་བཞིན་དུ་ལྟུང་བར་འགྱུར་རོ། །

[Block 2349]
དེ་རྣམས་ཀྱི་འགྱོད་པ་བཟློག་པར་བྱ་བའི༌[^1542]ཕྱིར་དེ་དང་མཐུན་པར་བཅོམ་ལྡན་འདས་ཀྱི་བསྟན་པ་གསུངས་སོ། །

[Block 2350]
གང་གིས་འདི་ནི་རིགས་པ་ཡིན། །ཞེས་ལམ་དེ་ཉིད་དུ་ཞུགས་ཤིང་སྐུར་བ༌[^1543]མི་འདེབས་སོ། །
--- END BLOCKS ---
