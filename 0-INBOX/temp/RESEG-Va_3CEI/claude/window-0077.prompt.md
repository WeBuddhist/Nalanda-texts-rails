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
[Block 2696]
དེ་རིང་བདག་ཅག་འཕྲལ་ལ་ངོ་མཚར་གྱུར། །ཞེས་པ་ནས། ཚངས་པར་སྤྱོད་པ་མཆོག་རབ་རྣམ་དག་གང་། །ཞེས་པའི་བར་དུ་ནི། རེ་བ་མེད་པ་ལས་འབྲས་བུ་ཆེན་པོ་ཐོབ་པར་བསྟན་པ་དང་། དེ་ཡང་ལམ་བསྒོམས་པ༌[^2301]དང་ཚུལ་ཁྲིམས་རྣམ་པར་དག་པའི་རྒྱུ་ལས་འབྲས་བུ་དེ་ཐོབ་ཅེས་པའོ། །

[Block 2697]
མདོ་ལས།

[Block 2698]
འདྲེན་པའི་བསྟན་པ་རྣམས་ལ་ཤིན་ཏུ་བསྙེན། །ཞེས་པ་ནས། འདི་འདྲ་བ་ཡི་དཀའ་བ་གང་མཛད་པ། །ཞེས་པའི་བར་དུ་ནི་འབྲས་བུ་ཆེན་པོ༌[^2302]མངོན་དུ་ཐོབ་སྟེ། འཕགས་པ་ཉན་ཐོས་སུ་ངེས་པ་གཞན་ལ༌[^2303]ཕན་འདོགས་པར་འོས་པ་མཆོད་པའི་གནས་སུ་གྱུར་པ་བསྟན་པའོ། །

[Block 2699]
དེ་བཞིན་གཤེགས་པའི་དྲིན་གྱི་ལན་ལྡོན་པ༌[^2304]ནི་གཞན་གྱིས༌[^2305]མ་ཡིན་གྱི༌[^2306]འདི་འདྲ་བ་ཐོབ་པ་ཞེས་སོ། །

[Block 2700 [HEADING]]
###### བཅོམ་ལྡན་འདས་ཀྱི་བཀའ་དྲིན་ཟབ་པ། ^4-4-2-2-2-0

[Block 2701]
མདོ་ལས།

[Block 2702]
མགོ་དང་ལག་པ་དང་ནི་རྐང་པས་ཀྱང་། ། ཞེས་པ་ནས། དེ་ལ་ནམས་ཀྱང༌[^2307]ལན་ལྡོན༌[^2308]མ་གྱུར་ཏོ། །ཞེས་པའི་བར་དུ་ནི། ནང་གི་རྫས་དྲུག་དང་། ཕྱིའི༌[^2309]སྤྱོད་པ་རྣམ་པ་བཞི་འདི་དག༌[^2310]གང་བྱས་ཀྱང་ལན་མི་ལོན་ཞེས་པའོ། །

[Block 2703 [HEADING]]
###### **ཡིད་དང་མཐུན་པར་ཆོས་སྟོན་པ།** ^4-4-2-2-2-1-0

[Block 2704]
མདོ་ལས།

[Block 2705]
ཉིད་ཀྱི༌[^2311]ཆེ་ཆོས་མཚུངས་པ་མེད་པའི་མཐུ། །ཞེས་པ་ནས། མཆན་མ་སྤྱོད་པ་རྣམས་ལ་ཆོས་བཤད་དེ། །ཞེས་པའི་བར་དུ་ནི་འདི་མན་ཆད་ཅི་ཕྱིར༌[^2312]ལན་དཀའ་བའི་གཏན་ཚིགས་རྣམ་པ་གསུམ་ཞིག་འཆད་པ་ལས༌[^2313]སངས་རྒྱས་བཅོམ་ལྡན་འདས་སྤྱོད་པ་ཞན་པ་མཚན་མར་འཛིན་པ་རྣམས་ལ་ཡིད་དང་མཐུན་པར་ཆོས་སྟོན་པ་དང་། སོ་སོའི་མོས་པ་དང་། དད་པར་མཐུན་པར་ཆོས་སྟོན་པས་དཀའ་བ་མཛད་པ་དང་། དབང་པོ་སྨིན་པ་དང་། མ་སྨིན་པ་རྣམས་ལ་ཆོས་སྟོན་པ་སྟེ། རྣམ་པ་གསུམ་གྱི་ཕྱིར་ལན་གླན་དཀའ་བའོ། །

[Block 2706]
འདི་ནི་དང་པོ་དང་སྦྱར་ཏེ་སྐུ་དག་པ་རྫོགས་ལོངས་སྤྱོད་པའི་ཡོན་ཏན་སྤངས་ཤིང་སྤྲུལ་པའི་སྐུ་འཇིག་རྟེན་རྙོག་པ་ཅན་དུ་གཤེགས་པ་དང་ཡང་དག་པའི་གཞུང་དམ་པ་བསྲི་སྟེ་ཚིག་མང་པོའི་སྒོ་ནས་དོན་སྟོན་པ་དང་། ཞིང་རྣམ་པར་དག་པ་སྤངས་ཏེ། ཕྱོགས་མ་དག་པར་གཤེགས་ཤིང་མ་རབས་ཀྱི་ཡིད་དང་མཐུན་པར་ཆོས་སྟོན་ཅིང་འདྲེན་པ་དེ་ལན་གླན་དཀའ་བ་མ་ཡིན་ནམ།

[Block 2707 [HEADING]]
###### **སོ་སོའི་མོས་པ་དང་དད་པ་བཞིན་དུ་ཆོས་སྟོན་པ།** ^4-4-2-2-2-2-0

[Block 2708]
མདོ་ལས།

[Block 2709]
ཆོས་ཀྱི་དབང་པོ་འཇིག་རྟེན་ཀུན་ལ་མངའ། །ཞེས་པ་ནས། བརྒྱ་ཕྲག་སྟོང་གི་བར་དུ༌[^2314]ཆོས་བཤད་དོ། །ཞེས་པའི་བར་དུ་ནི། སོ་སོའི་མོས་པ་དང་དད་པ༌[^2315]བཞིན་དུ་ཆོས་སྟོན་པ་དང་སྦྱར་རོ། །

[Block 2710 [HEADING]]
###### **དབང་པོ་སྨིན་པ་དང་མ་སྨིན་པ་རྣམས་ལ་ཆོས་སྟོན་པ།** ^4-4-2-2-2-3-0

[Block 2711]
མདོ་ལས།

[Block 2712]
དེ་བཞིན་གཤེགས་པས་སྤྱོད་པ༌[^2316]རབ་མཁྱེན་ནས། །ཞེས་པ་ནས། བྱང་ཆུབ་མཆོག་རབ་འདི་ནི་ཤིན་ཏུ་བསྟན། །ཞེས་པའི་བར་དུ་ནི་དབང་པོ་སྨིན་པ་དང་། མ་སྨིན་པ་དང་དབང་པོ་དུལ་བ་དང་། མ་དུལ་བ་དང་། བཀྲི་བ་དང་། ངེས་པའི་དོན་གང་གིས་གདུལ་བར་འོས་པ་རྣམས་ལ་མཐུན་མཐུན༌[^2317]དུ་ཆོས་སྟོན་པའོ།། །།

[Block 2713 [HEADING]]
### སྨན་གྱི་རྩི་ཤིང་ལས་དཔེ་བསྟན་པའི་ལེའུ། ^4-5-0

[Block 2714]
འདི་མན་ཆད་སྨན་གྱི་རྩི་ཤིང་ལས་དཔེ་བསྟན་པའི་ལེའུ་སྟེ། དེ་ལ་ཡང་ཅིའི་ཕྱིར་བཏགས་པ་དང་། ཅི་ལས་བཏགས་པ་རྣམ་པ་གཉིས་སོ། །

[Block 2715 [HEADING]]
#### ཅིའི་ཕྱིར་བཏགས་པ། ^4-5-1-0

[Block 2716]
གོང་དུ་དབང་པོ་རྟུལ་པོའི་ཆེད་དུ་དཔེ་དང་དོན་དུ་སྦྱར་ཏེ་བསྟན་པས་འཕགས་པ་ཤཱ་རིའི་བུ་ལ་སོགས་པ་ཆོས་རྟོགས་ཤིང་ལུང་བསྟན་པ་དང་ཡང་འདིར་དབང་པོ་བར་མའི་ཆེད་དུ་དཔེས་ཆོས་སྟོན་ཅིང་། ལུང་བསྟན་པར་བཞེད་པའི་ཕྱིར་དཔེ་འདི་གསུངས་པ་ལས་བཤད་པ་དང་འགྲེལ་པ་ལས་ཀྱང་། ལེའུ་འདི་ནི་ཐེག་པ་ཆེན་པོ་ལ་ང་རྒྱལ་དུ་འཛིན་པ༌[^2318]དགོངས་པའི་ཕྱིར་ཐེག་པ་གཅིག་ལས་ལོགས་ཤིག་ན་གཉིས་དང་གསུམ་མེད་དོ་བར་བསྟན་པའི་ཕྱིར་ཏེ། དང་པོར་ཁང་ཁྱིམ་ཚིག་པའི་དཔེས་སེམས་ཅན་མ་རབས་རྣམས་ཐབས་ཀྱིས༌[^2319]དྲངས་ཏེ་ལྷ་དང་མིའི་བདེ་བ་ལ་དགོད་པ་དང་། དད་པའི་ལེའུ་བསྟན་པའི་ནང་དུ་ཐེག་པ་རྣམ༌[^2320]གཉིས་དེ་བཞིན་གཤེགས་པའི་ཐེག་པ་དང་མཉམ་པར་སེམས་ཤིང་ཐེག་པ་ཆེན་པོ་སྒྲུབ༌[^2321]ཏུ་མི་བཏུབ་པ་ཐེག་པ་ཆེན་པོ་བསྒྲུབ་ཏུ་གཞུག་པ་དང་། ལེའུ་འདིའི་ནང་ནས་ནི་ཐེག་པ་ཆེན་པོ་པ་གཅིག་ཏུ་ང་རྒྱལ་གྱི་ཐེག་པ་གསུམ་སྤོང་གིས་སོ་སོ་ན༌[^2322]ཡོད་པའི༌[^2323]སེམས་པའི་ང་རྒྱལ་གཞོམ་པར་ཐེག་པ་གཅིག་པོ་བསྟན་པའི་ཕྱིར་ཆར་པ་གཅིག་བབ་པའི༌[^2324]རླན་གྱིས༌[^2325]ཤིང་རྩི་མི་མཐུན་པར་སྐྱེ་བ་བཞིན་དུ་དེ་བཞིན་གཤེགས་པའི་གསུང་གཅིག་གིས་དགེ་བའི་རྩ་བ་སོ་སོར་སྨིན་པ་བཞིན་ཏེ། འཕགས་པ་མྱ་ངན་ལས་འདས་པ་ཆེན༌[^2326]པོའི་མདོ་ལས་ཀྱང་། དེ་བཞིན་གཤེགས་པ་ཆོས་སྟོན་པ་ན་ཐེག་པ་གཅིག་པ་ལམ་གཅིག་པོས་སྟོན་ཏེ་ཞེས་འབྱུང་སྟེ། བསྟན་པ་གཅིག་ལས་དབང་པོ༌[^2327]སོ་སོར་དབྱེ་བར་བསྟན་པའོ། །

[Block 2717]
ཐབས་མཁས་པའི་ལེའུ་ལས་ཡེ་ཤེས་དང་སྒོ་བསྟན་པ་གཉི་ག་ཡང་ཤིན་ཏུ་ཟབ་པ་ཐེག་པ་གཅིག་ཏུ་སྦྱར་བའོ། །

[Block 2718]
བདེན་པ་བཞི་ལ་དབང་པོ་མི་མཐུན་པས་སོ་སོར་གོ་བ་བཞིན་ནོ། །

[Block 2719 [HEADING]]
#### ཅི་ལས་བཏགས་པ། ^4-5-2-0

[Block 2720]
མིང་ནི་སྨན་གྱིས་ནད་འཚོ་བར་བྱེད་པ་བཞིན་བླ་ན་མེད་པའི་སྨན་དམ་པ་འདིས་ཀྱང་ཉོན་མོངས་པའི་ནད་ཐམས་ཅད་འཚོ་བར་བྱེད་པའི་ཕྱིར་ལུང་དང་། གཞུང་དང་སྤྱོད་པ་དང་། འབྲས་བུ་ནི་སྨན་དམ་པ་ཞེས་བྱའོ། །

[Block 2721]
སྨན་ནད༌[^2328]ཆེ་ཆུང་སོ་སོར་ཕན་པ་བཞིན་བླ་ན་མེད་པའི་ཐེག་པ་འདི་ཡང་ཐེག་པ་རྣམ་གསུམ་གཅིག་ཏུ་སྨིན་པའི་ཕྱིར་རོ། །

[Block 2722 [HEADING]]
#### བསྟོད་པ། ^4-5-3-0

[Block 2723]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་ཚེ་དང་ལྡན་པ་ཞེས་པ་ནས་དེ་དག་གི་མཐའ་བདེ་བར་མི་རྟོགས་སོ་ཞེས་པའི་བར་དུ་ནི་ལེའུ་འདི་ལ་དང་པོར་བསྟོད་པ་དང་། འོད་སྲུངས་ཀྱིས་ཤེས་པར་བྱོས་ཤིག་པ་དང་། དོན་གྱི་མདོ་བསྡུས་ཏེ་ལུང་བསྟན་པ་ལ་འདི་ནི་དང་པོའོ། །

[Block 2724]
དེ་བཞིན་གཤེགས་པའི་ཡོན་ཏན་བརྗོད་པར་དཀའ་བས་མཐའ་མེད་ཅེས་པར་བསྡུས་པའོ། །

[Block 2725 [HEADING]]
#### འོད་སྲུངས་ཀྱིས་ཤེས་པར་བྱོས་ཤིག་པ། ^4-5-4-0

[Block 2726]
མདོ་ལས།

[Block 2727 [HEADING]]
##### དེ་བཞིན་གཤེགས་པའི་བཀའ་ཕུན་སུམ་ཚོགས་པ་མི་བརྫུན་པ། ^4-5-4-1-0

[Block 2728 [HEADING]]
###### དེ་བཞིན་གཤེགས་པ་འཇིག་རྟེན་དུ་འབྱུང་བ། ^4-5-4-1-1-0

[Block 2729]
འོད་སྲུངས་དེ་བཞིན་གཤེགས་པ་ནི། །ཞེས་པ་ནས། །དེ་དག་དེ་བཞིན་དུ་འགྱུར་རོ། །ཞེས་པའི་བར་དུ་ནི་དེ་བཞིན་གཤེགས་པ་འཇིག་རྟེན་དུ་འབྱུང་བ་དང་། འགྲོ་བ་མང་པོ་ལ་ཕན་པ་མཛད་པ་དང་། ཆོས་ཀྱི་དོན་རྟོགས་པ༌[^2329]ནི་མི་མཐུན་པ་དང་། བདག་ཉིད་ཀྱིས་རིག༌[^2330]པར་དཀའ་བ༌[^2331]སྟོན་པ་ལ་འདི་ནི་དང་པོ་སྟེ། །དེ་བཞིན་གཤེགས་པའི་བཀའ༌[^2332]ཕུན་སུམ་ཚོགས་པ་མི་བརྫུན་པར་བསྟན་པའོ། །

[Block 2730 [HEADING]]
###### འགྲོ་བ་མང་པོ་ལ་ཕན་པ་མཛད་པ། ^4-5-4-1-2-0

[Block 2731]
མདོ་ལས་འོད་སྲུངས་དེ་བཞིན་གཤེགས་པས༌[^2333]ཆོས་ཐམས་ཅད་རིག་པར་འཇོག་སྟེ་ཞེས་པ་ནས་དེ་ལྟར་འཇོག་གོ་ཞེས་པའི་བར་དུ་ནི་ཆོས་བཤད་པས་ཕན་འདོགས་པ་སྟེ། དེ་བཞིན་གཤེགས་པ་ཐུགས་རྗེ་ཆེན་པོ་དང་། ཐབས་མཁས་པ་དང་ལྡན་པས་མཚན་མ་དང་བྲལ་བའི་ཆོས་སྟོན་པས་འགྲོ་བ་སྨིན་པར་བྱེད་དེ། ལུང་ནི་རིགས་པ་ཅན་རིག་པའི༌[^2334]གཞུང་བསྒྲུབས་པས༌[^2335]འབྲས་བུ་ཐོབ་པར་བྱེད་པ་ཉིད་ཡེ་ཤེས་ཀྱི་ས་ལ་འཇོག་པའོ། །

[Block 2732 [HEADING]]
###### ཆོས་ཀྱི་དོན་རྟོགས་པ་མི་མཐུན་པ། ^4-5-4-1-3-0

[Block 2733]
མདོ་ལས་ཆོས་ཐམས་ཅད་ཀྱི་དོན་གྱི་རིམ་པ་ལ་ཞེས་པ་ནས་དམ་པའི་མཆོག་ཐོབ་སྟེ་ཞེས་པའི་བར་དུ་ནི་ཆོས་སྟོན་པའི་རིམ་པ༌[^2336]གསུམ་དུ་མི་མཐུན་པའི་ཕྱིར་སེམས་ཅན་རྣམས་ནི་ཡོད་པ་དང་མེད་པར་ལྟ་བ་གཉིས་ལས་མི་འདའ་བ་དང་། ཡང་དག་པའི་དོན་གྱི་མཐའ་དང་། སེམས་ཅན་རྣམས་ཀྱི་སེམས་ཀྱི་སྤྱོད་པ་མི་མཐུན་པས་སྐྱེད་པ་སྟེ། མདོ་ལས་ཀྱང་ཡོད་པ་དང་མེད་པའི་ཕྱོགས་ལ་འཛུད་ཅིང་མོས་པ་དང་མཚན་ཉིད་གསུམ་གྱིས༌[^2337]ཡང་དག་པའི་མཐའ་ལ་འཇུག་པའོ་ཞེས་འབྱུང་སྟེ། སྤྱོད་པ་ཐམས་ཅད་དང་མཐུན་པར་འཇུག་པ་ལ་མཁས་པས་མཁྱེན་པ་ཐོགས་པ་མེད་པའི་ཕྱིར་སེམས་ཅན་གྱི་སེམས་ཀྱི་རིམ་པ་བཞིན་དུ་ཆོས་སྟོན་པའོ། །

[Block 2734 [HEADING]]
###### བདག་ཉིད་ཀྱིས་རིག་པར་དཀའ་བ། ^4-5-4-1-4-0

[Block 2735]
མདོ་ལས་འོད་སྲུངས་དེ་བཞིན་གཤེགས་པ་དགྲ་བཅོམ་པ་ཡང་དག་པར༌[^2338]ཞེས་པ་ནས་ཡེ་ཤེས་ལ་མངོན་པར་འཇོག་གོ་ཞེས་པའི་བར་དུ་ནི་སེམས་ཅན་རྣམས་ཀྱི་དེ་བཞིན་ཉིད་ཡང་དག་པ༌[^2339]ཇི་ལྟ་བ་བཞིན་རང་གིས་མི་ཤེས་པའི་ཕྱིར་དེ་བཞིན་གཤེགས་པ་གདོན་མི་ཟ་བའི་མཐའ་མཁྱེན་པ་སེམས་ཅན་གྱི་དབང་པོའི་རིམ་པ་མཁྱེན་པས་སེམས་ཅན་རྣམས་ལ་དེ་བཞིན་གཤེགས་པ༌[^2340]ཡེ་ཤེས་བསྟན་ཏེ། མ་བསྟན་པར་ནི་བདག་དང་གཞན་གྱི་མཚན་ཉིད་མི་ཤེས་པའོ། །
--- END BLOCKS ---
