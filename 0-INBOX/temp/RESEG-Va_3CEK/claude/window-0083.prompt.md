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
[Block 2906]
ཅིའི་ཕྱིར་འདི་དག་ཁོ་ན་སྐྱེས་བུ་དམ་པའི་འགྲོ་བ་ཡིན་ལ། སློབ་པའི་འགྲོ་བ་གཞན་དག་ནི་མ་ཡིན་ཞེ་ན། གང་དག་ལ་འགྲོ་བ་འདི་དག་ཡོད་པ་དེ་དག་ནི་ལས་དམ་པ་དགེ་བ་ཁོ་ན་ལ་འཇུག་ཅིང་དམ་པ་མ་ཡིན་པ་མི༌[^1997]དགེ་བ་ལ་མི་འཇུག་པ་དང་། འགྲོ་བ་འདི་དག་ཏུ་སོན་པ་རྣམས་ལ༌[^1998]ཡང་ཕྱིར་འོང་བ་མེད་པ་ཡིན་ལ་ཇི་སྐད་དུ་བཤད་པ་འདི་དག་གཞན་ལ་ནི་མེད་པས་དེའི་ཕྱིར།

[Block 2907 [VERSE]]
དམ་པ་དམ་མིན་འཇུག་མི་འཇུག །
སོན་པ་ཕྱིར་མི་འོང་ཕྱིར་ཏེ། །

[Block 2908]
སྐྱེས་བུ་དམ་པའི་འགྲོ་བ་དག་ཡིན་གྱི་གཞན་དག་ནི་མ་ཡིན་ནོ། །

[Block 2909]
འོ་ན་མདོ་ཁོ་ན་ལས་སྐྱེས་བུ་དམ་པ་གང་ཞེ་ན། སློབ་པའི་ཡང་དག་པའི་ལྟ་བ་དང་ལྡན་པའོ་ཞེས་རྒྱས་པར་གསུངས་པ་ཇི་ལྟ་བུ་ཞེ་ན། གཞན་དག་ལ་ཡང་སྡིག་པ་རྣམ་པ་ལྔ་གཏན་མི་བྱེད་པའི་སྡོམ་པ་ཐོབ་པའི་ཕྱིར་དང་། ཉོན་མོངས་པ་མི་དགེ་བ་ཕལ་ཆེར་སྤངས་པའི་ཕྱིར་རྣམ་གྲངས་པའི་སྐྱེས་བུ་དམ་པ་ཉིད་ཡོད་མོད་ཀྱི། འདིར་ནི་གང་དག་ལ་རྣམ་གྲངས་མེད་པར་ཡོད་པ་དེ་དག་གི་སྐབས་ཡིན་ནོ། །

[Block 2910 [HEADING]]
###### འདོད་པར་ཚེ་ཡོངས་སུ་གྱུར་པའི་འཕགས་པ། ^3-2-8-7-7-0

[Block 2911]
ཅི་ཕྱིར་མི་འོང་བ་ཚེ་ཡོངས་སུ་གྱུར་པ་ལ་ཡང་དབྱེ་བ་འདི་ཡོད་དམ་ཞེ་ན། མེད་དེ། འདི་ལྟར།

[Block 2912 [VERSE]]
འདོད་པར་ཚེ་ཡོངས་གྱུར་པའི་འཕགས། །
ཁམས་གཞན་དུ་ནི་འགྲོ་བ་མེད། །

[Block 2913]
འདོད་པའི་ཁམས་སུ་ཚེ་ཡོངས་སུ་གྱུར་པའི་འཕགས་པ་ནི་ཁམས་གཞན་དུ་མི་འགྲོ་སྟེ། ཚེ་འདི་ཉིད་ལ་ཕྱིར་མི་འོང་བའི་འབྲས་བུ་ཐོབ་ནས་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བའི་ཕྱིར་རོ། །

[Block 2914]
གཟུགས་ཀྱི་ཁམས་སུ་ཚེ་ཡོངས་སུ་གྱུར་པ་ནི་གལ་ཏེ་ན་གཟུགས་མེད་པའི་ཁམས་དག་ཏུ་ཡང་འཇུག་སྟེ། གོང་དུ་འཕོ་བ་སྲིད་པའི་རྩེ་མོའི་མཐར་ཐུག་པར་འགྲོ་བ་གང་ཡིན་པའོ། །

[Block 2915]
འོ་ན་བརྒྱ་བྱིན་གྱིས།

[Block 2916 [VERSE]]
བདག་ནི་ཐ་མ༌[^1999]ཉམས་ན་ལྷ་གང་འོག་མིན་ཞེས། །
རྣམ་པར་གྲགས་པ་དེ༌[^2000]ནི་སྐྱེ་བར་འགྱུར་བར་ཤོག །

[Block 2917]
ཅེས་གང་སྨྲས་པ་ཇི་ལྟ་བུ་ཞེ་ན། བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ་ཆོས་མངོན་པ་མངོན་པར་མི་ཤེས་པའི་ཕྱིར་ཏེ། ཡང་དག་པར་དགའ་བར་བྱ་བ་ཡིན་པའི་ཕྱིར་བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་མ་བཀག་གོ་ཞེས་ཟེར་རོ། །

[Block 2918 [VERSE]]
དེ་དང་གོང་མར་སྐྱེས་པ་ནི། །
ཡོངས༌[^2001]ཉམས་དབང་པོ་འཕོ་མི་བསྟེན། །

[Block 2919]
འདོད་པའི་ཁམས་སུ་ཚེ་ཡོངས་སུ་གྱུར་པའི་འཕགས་པ་དེ་དང་། ཁམས་གོང་མར་སྐྱེས་པའི་འཕགས་པ་ནི་དབང་པོ་རྣམས་ཀྱང་མི་འཕོ་ལ་ཇི་ལྟར་ཡང༌[^2002]ཡོངས་སུ་ཉམས་པར་མི་འགྱུར་རོ། །

[Block 2920]
ཅིའི་ཕྱིར་འཕགས་པ་ཚེ་གཞན་དུ་ཡོངས་སུ་གྱུར་པ་གཟུགས་དང་གཟུགས་མེད་པར་འཇུག་པ་དང་། དབང་པོ་འཕོ་བ་དང་། ཡོངས་སུ་ཉམས་པ་དག་ཏུ་མི་འདོད་ཅེ་ན། འདི་ལྟར་མེད་པའི་ཕྱིར་རོ། །ཅིའི་ཕྱིར་མེད་ཅེ་ན། ཚེ་རབས་གཞན་ནས་ཡོངས་སུ་འདྲིས་པས་དབང་པོ་རྣམས༌[^2003]ཡོངས་སུ་སྨིན་པའི་ཕྱིར་དང་། རྟེན་ཁྱད་པར་ཅན་ཐོབ་པའི་ཕྱིར་རོ། །

[Block 2921]
ཡང༌[^2004]ཅིའི་ཕྱིར་སློབ་པ་འདོད་ཆགས་དང་མ་བྲལ་བ་བར་མ་དོར་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བར་མི་འགྱུར་ཞེ་ན། ལམ་མ་འདྲིས་པས་མངོན་སུམ་དུ་མི་འགྱུར་བའི་ཕྱིར་དང་། ཕྲ་རྒྱས་རྣམས་ཤིན་ཏུ་ཆུང་བ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2922]
བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ་འདོད་པའི་ཁམས་ལས་འདའ་བར་དཀའ་བའི་ཕྱིར་ཏེ། འདིས་ཉོན་མོངས་པ་མི་དགེ་བ་དང་ལུང་དུ་མ་བསྟན་པ་སྤངས་པ་དང་།[^2005] དགེ་སྦྱོང་གི་ཚུལ་གྱི་འབྲས་བུ་གཉིས་སམ་གསུམ་ཐོབ་པ་དང་། ཁམས་གསུམ་ལས་ཡང་དག་པར་འདའ་བ་དང་མང་པོ་ཞིག་བྱ་དགོས་ལ། དེ་ཡང་སྲིད་པ་བར་མ་ལ་གནས་པས་བྱ་བར་མི་ནུས་ཞེས་ཟེར་རོ། །

[Block 2923 [HEADING]]
###### བསམ་གཏན་སྤེལ་བ། ^3-2-8-7-8-0

[Block 2924]
དེ་ནི་བསམ་གཏན་སྤེལ་ནས༌[^2006]འོག་མིན་འགྲོ། །ཞེས་བཤད་པ། ཡང་དང་པོ་ཉིད་དུ་བསམ་གཏན་གང་སྤེལ་བར་བྱེད་ཅེ་ན། དང་པོར་བཞི་པ་སྤེལ་བར་བྱེད། ། ཏིང་ངེ་འཛིན་དེ་ནི་ཐམས་ཅད་པས་ལས་སུ་རུང་བ་དང་། ལམ་སླ་བ་རྣམས་ཀྱི་ནང་ན་མཆོག་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2925]
འདི་ལྟར་སྤེལ་བར་བྱེད་དེ། དགྲ་བཅོམ་པ་འམ་ཕྱིར་མི་འོང་བ་ཡང་རུང་སྟེ༌[^2007]ཟག་པ་མེད་པའི་བསམ་གཏན་བཞི་པ་རྒྱུན་དང་ལྡན་པ་ལ་སྙོམས་པར་འཇུག་ཅིང་། དེ་ལས༌[^2008]ལངས་ནས་དེ་ཉིད་ཟག་པ་དང་བཅས་པ་རྒྱུན་དང་ལྡན་པ་ལ་སྙོམས་པར་འཇུག་ལ། ཡང་ཟག་པ་མེད་པ་ལ་སྙོམས་པར་འཇུག་སྟེ། དེ་བཞིན་དུ་རྒྱུན་ཕྲི་ནས། གང་གི་ཚེ་སྐད་ཅིག་མ་གཉིས་ཟག་པ་མེད་པ་ལ་སྙོམས་པར་འཇུག་ཅིང་སྐད་ཅིག་མ་གཉིས་ཟག་པ་དང་བཅས་པ་ལ་སྙོམས་པར་འཇུག༌[^2009]ལ་ཡང་ཟག་པ་མེད་པ་ལ་སྙོམས་པར་འཇུག་གོ་ཞེས་གྲག་སྟེ། འདི་ནི་སྤེལ་བའི་སྦྱོར་བ་ཡིན་ནོ། །

[Block 2926]
སྐད་ཅིག་མ་ནི་བསྲེས་པས་འགྲུབ། །བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ་གང་གི་ཚེ་ཟག་པ་མེད་པའི་སྐད་ཅིག་མའི་མཇུག་ཐོགས་སུ་ཟག་པ་དང་བཅས་པ་མངོན་སུམ་དུ༌[^2010]བྱེད་ཅིང་། ཟག་པ་དང་བཅས་པའི་མཇུག་ཐོགས་སུ་ཡང་ཟག་པ་མེད་པ་མངོན་སུམ་དུ་བྱེད་ལ། དེ་ལྟར་ཟག་པ་དང་བཅས་པའི་སྐད་ཅིག་མ་དང་ཟག་པ་མེད་པ་དག་ཏུ་བསྲེས་པས་སྤེལ་བ་འགྲུབ་པ་ཡིན་ཏེ། སྐད་ཅིག་མ་གཉིས་ནི་བར༌[^2011]ཆད་མེད་པའི་ལམ་ལྟ་བུ་ཡིན་ལ།

[Block 2927]
གསུམ་པ་ནི་རྣམ་པར་གྲོལ་བའི་ལམ༌[^2012]ལྟ་བུ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 2928]
དེ་ལྟར་བསམ་གཏན་བཞི་པ་སྤེལ་ནས། དེའི་སྟོབས་ཀྱིས་གཞན་དང་གཞན་དག་ཀྱང་སྤེལ་བར་བྱེད་དེ། དང་པོར་འདོད་པའི་ཁམས་སུ་གླིང་གསུམ་དག་ཏུ་སྤེལ་བར་བྱེད་ལ། ཕྱིས་ནི་ཡོངས་སུ་ཉམས་པས་གཟུགས་ཀྱི་ཁམས་སུ་སྤེལ་བར་བྱེད་དོ། །

[Block 2929]
སངས་རྒྱས་མ་གཏོགས་པས་སྐད་ཅིག་མ་སྤེལ་བར་མི་ནུས་ཏེ། དེའི་ཕྱིར་རྒྱུན་ཆགས་གསུམ་ལ་ཇི་སྲིད་དུ༌[^2013]འདོད་པར་སྙོམས་པར་འཇུག་པའི་སྒོ་ནས་རྫོགས་པ་ཡིན་ནོ་ཞེས་བྱ་བར་བལྟའོ། །

[Block 2930 [HEADING]]
###### བསམ་གཏན་སྤེལ་བར་བྱེད་པའི་རྒྱུ། ^3-2-8-7-9-0

[Block 2931]
ཅིའི་ཕྱིར་བསམ་གཏན་སྤེལ་བར་བྱེད་ཅེ་ན།

[Block 2932 [VERSE]]
སྐྱེ་དང་གནས་པར་བྱ་ཕྱིར་དང་། །
ཉོན་མོངས་པས་ནི་འཇིག་ཕྱིར་ཡང་། །

[Block 2933]
རྒྱུ་གསུམ་གྱིས་ན་བསམ་གཏན་སྤེལ་བར་བྱེད་དེ། ཕྱིར་མི་འོང་བ་དབང་པོ་རྣོན་པོ་རྣམས་ནི་གནས་གཙང་མ་རྣམས་སུ་སྐྱེ་བར་བྱ༌[^2014]བའི་ཕྱིར་དང་། མཐོང་བའི་ཆོས་ལ་བདེ་བར་གནས་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 2934]
དབང་པོ་རྟུལ་པོ་རྣམས་ནི་ཉོན་མོངས་པས་འཇིགས༌[^2015]པའི་ཡང་ཕྱིར་ཏེ། རོ་མྱང་བ་དང་མཚུངས་པར་ལྡན་པའི་ཏིང་ངེ་འཛིན་ཐག་བསྲིངས་པའི༌[^2016]སྒོ་ནས་ཡོངས་སུ་མི་ཉམས་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 2935]
དགྲ་བཅོམ་པ་དབང་པོ་རྣོན་པོ་རྣམས་ནི་མཐོང་བའི་ཆོས་ལ་བདེ་བར་གནས་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 2936]
དབང་པོ་རྟུལ་པོ་རྣམས་ནི་ཉོན་མོངས་པས་འཇིགས་པའི་ཡང་ཕྱིར་ཏེ། ཡོངས་སུ་མི་ཉམས་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 2937 [HEADING]]
###### གནས་གཙང་མར་སྐྱེ་བ་ལྔ། ^3-2-8-7-10-0

[Block 2938]
ཡང་ཅིའི་ཕྱིར་གནས་གཙང་མར་སྐྱེ་བ་ལྔ་ཁོ་ན༌[^2017]ཡིན་ཞེ་ན། བསམ་གཏན་བཞི་པ་སྤེལ་མར་བསྒོམས་པར༌[^2018]བཤད་པ་གང་ཡིན་པ༌[^2019]དེ་ནི་རྣམ་པ་ལྔའི་ཕྱིར།[^2020] གནས་གཙང་སྐྱེ་བ་ལྔ་ཁོ་ན། །སྤེལ་མར་བསྒོམ་པ༌[^2021]དེ་ནི་ཆུང་ངུ་དང་འབྲིང་དང་ཆེན་པོ་དང་། ཤིན་ཏུ་ཆེ་བ་དང་། ཤིན་ཏུ་ཆེས་ཆེ་བའི་བྱེ་བྲག་གིས་རྣམ་པ་ལྔ་ཡིན་ཏེ།

[Block 2939]
དང་པོ་ལ་ནི་ཟག་པ་མེད་པ་དང་ཟག་པ་དང་བཅས་པ་དང་ཟག་པ་དང་བཅས་པ་དང་པོ༌[^2022]དང་སེམས་གསུམ་མངོན་སུམ༌[^2023]དུ་བྱེད་དོ། །

[Block 2940]
གཉིས་པ་ལ་ནི་དྲུག་གོ། །

[Block 2941]
གསུམ་པ་ལ༌[^2024]ནི་དགུའོ། །

[Block 2942]
བཞི་པ་ལ༌[^2025]བཅུ་གཉིས་སོ། །

[Block 2943]
ལྔ་པ་ལ་ནི་བཅོ་ལྔ་སྟེ། དེ་དག་གི་འབྲས་བུ་ནི་གྲངས་བཞིན་དུ་གནས་གཙང་མ་ལྔ་ཡིན་ལ་དེ་ལ་ཟག་པ་དང་བཅས་པ་གང་ཡིན་པ་དེའི་དབང་གིས་དེ་དག་ཏུ་སྐྱེའོ། །

[Block 2944]
གཞན་དག་ན་རེ་དད་པའི་དབང་པོ་ལ་སོགས་པ་ལྷག་པའི་ཕྱིར་ལྔ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 2945 [HEADING]]
###### ལུས་ཀྱིས་མངོན་དུ་བྱེད་པ། ^3-2-8-7-11-0
--- END BLOCKS ---
