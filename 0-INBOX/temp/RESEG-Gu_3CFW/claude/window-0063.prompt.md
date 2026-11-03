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
[Block 2206]
མཚམས་གཉིས་པོ་དང་ཞེས་བྱ་བ་ནི། མཚམས་ཆེན་པོ་དང་། དཀྱིལ་འཁོར་བའི་མཚམས་བསྐོ་བའོ། །

[Block 2207]
མ་འབྲེལ་ཞེས་བྱ་བ་ནི་མཚམས་ཆེན་པོ་བཅད་པའི༌[^1995]ནང་དུ་གསོལ་བ་དང་། གཉིས་ཀྱི་ལས་ཀྱིས་ཆོས་གོས་དང་འབྲལ་བར་མི་འགྱུར་བའི་བསྐོ་བའོ། །

[Block 2208]
སྨྱོས་དང་ཞེས་བྱ་བ་ནི་མི་འབྲལ་བར་བསྐོ་བ་དང་། མྱོས་པའི༌[^1996]བསྐོ་བ་དང་། དགག་དབྱེ་བསྐོ་བ་དང་། གནས་མལ་སྟོབས་པར༌[^1997]བྱེད་པ་བསྐོ་བའོ། །

[Block 2209]
རུང་བའི་ས་གཞི་ཞེས་བྱ་བ་ནི་རུང་བའི་ཁང་པ་གསོལ་བ་དང་། གཉིས་ཀྱི་ལས་ཀྱིས་བསྐོ་བའོ། །

[Block 2210]
གཏན་པ་དང་ནི་ཞེས་བྱ་བ་གསོལ་བ་དང་གཉིས་ཀྱི་ལས་ཀྱིས་བསྐོ་བའོ། །

[Block 2211]
དེ་གདིང་དང་ཞེས་བྱ་བ་ནི་གསོལ་བ་དང་གཉིས་ཀྱི་ལས་ཀྱིས་བསྐོ་བའོ། །

[Block 2212]
སྤོང་དང་ཞེས་བྱ་བ་ནི་སྤོང་བའི་ཞལ་ཏ་བསྐོ་བའི་ལས་གཅིག་བསྟན་ཏོ། །

[Block 2213]
ལག་གི་བླ་དང་ཞེས་བྱ་བ་ནི། དེའི་ལག་གི་བླ༌[^1998]བསྐོ་བའི་ལས་གཅིག་བསྟན་ཏོ། །

[Block 2214]
གནས་ཁང་བསྐོ་བ་ལ་སོགས་པ་དང་ཞེས་བྱ་བ་ལ་སོགས་པའི་སྒྲས་ནི་འདུན་པ་དང་བཟློག་པའི་བར་དུ་བསྐོ༌[^1999]བའོ། །

[Block 2215 [VERSE]]
གཟུ་དང་གསལ་དང་སྦེད་པ་དང་། །
ཚུལ་ཤིང་འདྲིམ་པར་བྱེད་པ་དང་། །

[Block 2216]
ཞེས་བྱ་བ་ནི་དེ་བསྐོ་བའོ། །

[Block 2217]
སྦེད་པ་དང་ཞེས་བྱ་བ་ནི་གཞི་འདྲིམ་པར་བྱེད་པ་བསྐོ་བ་ལའོ། །

[Block 2218]
ཁང་པ་ཁང་ཆེན་བསྟན་པ་དང་། །ཞེས་བྱ་བ་ནི་དགེ་འདུན་ལྷག་མ་ལས་གསུངས་པའི་སྟོན་པ་གཉིས་བསྐོ་བའོ། །

[Block 2219]
གླེང་དང་ཞེས་བྱ་བ་ནི༌[^2000]བསྐོ་བའོ། །

[Block 2220]
འབྲལ་བར་མི་འགྱུར་དང་ཞེས་བྱ་བ་ནི་སྣམ་སྦྱར་དང་མི་འབྲལ་བའི་གནང་བ༌[^2001]སྦྱིན་པའོ། །

[Block 2221]
གདིང་དང་ཞེས་བྱ་བ་ནི་གདིང་བའི་ཐོག་མར་ལོ་དྲུག་ཏུ་གནང་བ་སྦྱིན་པའོ། །

[Block 2222]
ལྷུང་བཟེད་འདྲིམ་དང་ཞེས་བྱ་བ་ནི། ལྷུང་བཟེད་ལྷག་མ་འདྲིམ་པར་བསྐོ་བ་ལའོ། །

[Block 2223]
མ་དད་གོ་བར་བྱ་བ་དང་། །ཞེས་བྱ་བ་ནི། ཁྱིམ་རྣམས་སུ་གནས་ངན་ལེན་གོ་བར་བྱ་བའི་ཕྱིར་གང་ཟག་བསྐོ་བ་དང་། སྔོན་བཞིན་དུ་གང་ཞིག་བརྗོད་པ་སྨྲ་བ་ལ་དགེ་སློང་རྣམས་ཀྱིས་སོ། །

[Block 2224]
ནགས་ཉུལ་བ་ལ་སོགས་པ་གཉིས་བསྡུས་པ་ལ་དགེ་སློང་མའི་གདམས་ངག་སྟོན་པ་བསྐོ་བར་བསྟན་པའི་དོན་དུའོ། །

[Block 2225]
ཕྱག་མི་བྱ་དང་ཞེས་བྱ་བ་ནི་ཕྱག་མི་བྱ་བའི་ཕྱིར་བསྐོ་བ་སྟེ། དགེ་སློང་མའི་དགེ་འདུན་གྱིས་རྩ་བ་དང་འབྲས་བུ་མེད་པའི་སྦུན་པའི༌[^2002]རྣམ་པ་ཅན་རྣམས་ལའོ། །

[Block 2226]
མང་ཕྱིར་དང་ཞེས་བྱ་བ་ནི་འཁོར་དང་འཁོར་མང་པོ་ཉེ་བར་འཇོག་པའི་གནང་བ་སྦྱིན་པའོ། །

[Block 2227]
འཁར་བ་དྲ་བའི་ཕྱིར་དང་ནི། །ཞེས་བྱ་བ་ནི་བསླབ་པའི་དོན་དུ་འཁར་བ་དང་དྲ་བའི་སྡོམ་པ་གཉིས་སོ། །

[Block 2228]
རྙེད་པ་གཅིག་ཏུ་བྱ་ཕྱིར་དང་། །ཞེས་བྱ་བ་ནི་གཙུག་ལག་ཁང་མཚམས་ཐ་དད་པ་གཉིས་རྙེད་པ་གཅིག་ཏུ་བྱ་བའི་ཕྱིར་གསོལ་བ་དང་གཉིས་ཀྱི་ལས་བྱ་བའོ། །

[Block 2229]
བསླབ་པ་བྱིན་དང་ཞེས་བྱ་བ་ནི། དགེ་སློབ༌[^2003]མའི་བསླབ་པ་སྦྱིན་པའོ། །

[Block 2230]
ཉེར་གནས་དང་ཞེས་བྱ་བ་ནི། ཚངས་པར་སྤྱོད་པ་ལ་ཉེ་བར་གནས་པའི་སྡོམ་པ་སྦྱིན་པའོ། །

[Block 2231]
བུ་དང་ཞེས་བྱ་བ་ནི་ཉལ་བའི་གནང་བ་སྦྱིན་པ་བསྐོ་བ་སྟེ། གང་ཞིག་གནས་པའི་དོན་དུ་གསུངས་པའོ། །

[Block 2232]
ཉེ་དུའི་ཞེས་བྱ་བ་ནི་ཉེ་དུ་རྣམས་དང་ལྷན་ཅིག་འབྲེལ་བའི་ཉེ་བར་སྤྱོད་པའི་གནང་བའི་སྡོམ་པ་སྦྱིན་པའོ། །

[Block 2233]
དགེ་སློང་མས་མུ་གེའི་སྡུག་བསྔལ་བྱུང་བའི་ཚེ་ཇི་སྐད་བསྟན་པའོ། །

[Block 2234]
ཕྱིར་འགྲོ་བ་ཞེས་བྱ་བ་ནི། ཞག་བདུན་ལས་འོག་ཏུ་ཞག་བཞི་བཅུ་མཚམས་ཀྱི་ཕྱི་རོལ་དུ་འགྲོ་བའི་གནང་བ་སྦྱིན་པ༌[^2004]བསྐོ་བའོ། །

[Block 2235]
འདི་ནི་གསོ་སྦྱོང་ལ་བསྐོ་བ་ལ་སོགས་པ་ལས་བཞི་བཅུ་རྩ་བདུན་པོ་རྣམས་ལའོ། །

[Block 2236]
གསོལ༌[^2005]དང་གཉིས་ཀྱི༌[^2006]ལས་ཡིན་ནོ། །ཞེས་བྱ་བ་ནི་གསོལ་བ་དང་གཉིས་ཀྱི་ལས་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2237 [VERSE]]
བསྙེན་པར་རྫོགས་པར་བྱ་བ་དང་། །
མུ་སྟེགས་གནས་དང་མཚམས་དགྲོལ་དང་། །

[Block 2238]
ཞེས་བྱ་བ་ལ༌[^2007]མཚམས་དགྲོལ་བ་ནི་མཚམས་བཅད་པ་གསོལ་བ་དང་། བཞིའི་ལས་ཀྱིས་དགྲོལ་བའོ། །

[Block 2239]
མཐུན་སྦྱིན་ཞེས་བྱ་བ་ནི། མཐུན་པ་སྦྱིན་པ་དང་གསོ་སྦྱོང་སྦྱིན་པའོ། །

[Block 2240]
འདུན་པ་པོ་དང་ཞེས་བྱ་བ་ནི། དེའི་རིགས་ཅན་གྱི་ནན་ཏུར་གྱི༌[^2008]ལས་བདུན་པོ་རྣམས་ཀྱི་ནན་ཏུར་བྱ་བའི་ལས་གཅིག །བཟོད་པར་གསོལ་བའི་ལས་གཅིག་དང་ལས་གཉིས་སོ། །

[Block 2241]
བརྒྱད་དང་ཞེས་བྱ་བ་ནི་སྤོ་བ་དང་མགུ་བར་བྱ་བ་དང་། གཞི་ནས་སྤོ་བ་དང་། གཞི་ནས་མགུ་བར་བྱ་བ་དང་། ཡང་གཞི་ནས་སྤོ་བ་སྦྱིན་པ་དང་། ཡང་གཞི༌[^2009]ནས་མགུ་བ་སྦྱིན་པ་དང་། སྲ་བརྐྱང་དབྱུང་བ་དང་ལྷག་མ་ལས་དབྱུང་བ་དག་ལ་གསོལ་བ་དང་། བཞིའི་ལས་བྱ་བ་དང་། བརྒྱད་སོ་སོར་བགྲང་ངོ་། །དྲན་དང་མི༌[^2010]མྱོས་དང་། དེ་ཉིད་ཚོལ༌[^2011]དུ་གཞུག་པ་དང་། །ཞེས་བྱ་བ་ནི་དྲན་པས༌[^2012]འདུལ་བར་འོས་པ་དང་། མ་མྱོས་པས༌[^2013]འདུལ་བར་འོས་པ་དང་། དེའི་ངོ་བོ་ཉིད་ཚོལ་དུ་གཞུག་པ་གསུམ་བསྡུས་པའོ། །

[Block 2242]
བསྐོ་བར༌[^2014]བྱ་བ་རྣམས་དང་ནི། །ཞེས་བྱ་བ་ནི་བཟློག་པའི་ཕྱིར་བསྒོ་བར་བྱ་བ་བཅུ་གཅིག་པོ་དག་གསུངས་ཏེ་དེ་ལ་དྲུག་ནི་དགེ་སློང༌[^2015]གི་རྣམ་པར་འབྱེད་པ་ལས་སྨོས་ཏེ། དགེ་འདུན་གྱི་དབྱེན་བྱེད་པ་ལ་སོགས་པ་རྣམས་སོ། །

[Block 2243]
གཉིས་ནི་དགེ་སློང་མའི་རྣམ་པར་འབྱེད་པ་ལས་ཐུན་མོང་མ་ཡིན་པར༌[^2016]གསུངས་ཏེ། ཕམ་པར་འགྱུར་བའི་སྐབས་ནས་གནས་ནས་དབྱུང་བའི་རྗེས་སུ་ཕྱོགས་པ་གཅིག་གོ། །

[Block 2244]
དགེ་འདུན་ལྷག་མའི་སྐབས་ནས་བཞི་བསྟན་ཏེ། སྡེ་ཚན་གཅིག་གོ། །

[Block 2245]
ཉམས་པ༌[^2017]སྦྱིན་པར་བྱ་བའི་བསླབ་པ་སྦྱིན་པའོ། །
--- END BLOCKS ---
