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
[Block 2836 [HEADING]]
###### **འཁོར་བསྡུ་བ།** ^4-5-4-4-2-2-0

[Block 2837]
མདོ་ལས།

[Block 2838]
ལྷ་དང་མི༌[^2428]ཚོགས་རྣམས་ཀྱང་ང༌[^2429]ལ་ཉོན། ངལ་ལྟ་བའི་ཕྱིར་ནི་ཉེ་བར་གཤེགས། །ཞེས་པས༌[^2430]འཁོར་བསྡུ་བའོ། །

[Block 2839 [HEADING]]
###### **ཕན་གདགས་ཤིང་དྲང་བ།** ^4-5-4-4-2-3-0

[Block 2840]
མདོ་ལས།

[Block 2841]
ང་ནི་དེ་བཞིན་གཤེགས་པ་བཅོམ་ལྡན་འདས། །

[Block 2842 [VERSE]]
ཟིལ་གྱིས༌[^2431]མི་ནོན་ཞེས་པ་ནས། །
དེ་ནི་རྣམ་གྲོལ་མྱ་ངན་འདས་པའོ། །

[Block 2843 [HEADING]]
###### **དམ་པའི་ཆོས་སྟོན་པ།** ^4-5-4-4-2-3-1-0

[Block 2844]
ཞེས་པའི་བར་དུ་ཕན་གདགས་པ་སྟེ། དམ་པའི་ཆོས་སྟོན་པ་དང་། ཐེག་པ་ཆེན་པོའི་རྒྱུ་སྟོན་པ་དང་། ཆོས་སྙོམས་པར་སྟོན་པ་དང་། གཅིག་ཏུ་ཕན་གདགས་པའི་ཕྱིར་དང་། བཟང་ངན་བཀོལ་བ་མེད་པ་སྟེ་འདི་ནི་དང་པོའོ། །

[Block 2845 [HEADING]]
###### **ཐེག་པ་ཆེན་པོའི་རྒྱུ་སྟོན་པ།** ^4-5-4-4-2-3-2-0

[Block 2846]
མདོ་ལས།

[Block 2847]
བྱང་ཆུབ་གཞུག་པའི་ཕྱིར་ནི་རྟག་པར་དེ། །ཞེས་པ་ནས། དབྱངས་གཅིག་གིས་ནི་རབ་ཏུ་ཆོས་བཤད་དེ། །ཞེས་པའི་བར་དུ་ནི་ཐེག་པ་ཆེན་པོའི་རྒྱུ་སྟོན་པ་སྟེ། དྲང་པོའི༌[^2432]དོན་རྣམ་པ་གཉིས་ཀ་ཡང་ཐེག་པ་ཆེན་པོའི་དོན་ཏེ། རྣམ་པ་ཐམས་ཅད་མཁྱེན་པའི་རྒྱུར་གྱུར་པའོ། །

[Block 2848 [HEADING]]
###### **ཆོས་སྙོམས་པར་སྟོན་པ།** ^4-5-4-4-2-3-3-0

[Block 2849]
མདོ་ལས།

[Block 2850]
དེ་ནི་སྙོམས་པའི་ཡིད་ཀྱིས་མ་སྙོམས་མེད། །ཅེས་པ་ནས། སེམས་ཅན་གཅིག་བཞིན་འགྲོ་བ༌[^2433]གཞན་ལའོ། །ཞེས་པའི་བར་དུ་ནི་འདི་སྙོམས་པར་སྟོན་པའོ།[^2434] །བདག་དང་བདག་གི་བ་དང་བྲལ་བ་དང་། བྱམས་སྡང་སྤངས་པ་དང་། ཉེ་རིང་གི་སེམས་མེད་པ་དང་། ཆོས་འཆབ་པ་མེད་པ་དང་། ཕྲག་དོག་མེད༌[^2435]པས་ཐམས་ཅད་ལ་འདྲ་བར་ཆོས་སྟོན་པའོ། །

[Block 2851 [HEADING]]
###### **གཅིག་ཏུ་ཕན་གདགས་པ།** ^4-5-4-4-2-3-4-0

[Block 2852]
མདོ་ལས།

[Block 2853]
ལས་གཞན་མི་བྱེད་རབ་ཏུ་ཆོས་འཆད་དེ། །ཞེས་པ་ནས། སྤྲིན་གྱིས་ཆར་པ་མངོན་པར་ཕབ་པ་བཞིན། །ཞེས་པའི་བར་དུ་ནི་གཅིག་ཏུ་ཕན་འདོགས་ཤིང་ཆོས་འཆད་པ་སྟེ། བཞུད་ཅེས་པ་ནི་མྱ་ངན་ལས་འདས་པའོ། །

[Block 2854]
བྱོན་ཞེས་པ་ནི་མངོན་པར་བྱང་ཆུབ་པར་སྟོན་པའོ། །

[Block 2855]
བཞུགས་ཞེས་པ་ནི་ཆོས་འཆད་ཅིང་ཕན་འདོགས་པའོ། །

[Block 2856]
ལངས༌[^2436]ཞེས་པ་ནི་སེམས་ཅན་གྱི་དབང་པོ་སྨིན་པ་ལ་བཞེངས་པ་སྟེ། ཐུགས་རྗེ་ཆེན་པོས་ནམ་ཡང་སེམས་ཅན་གྱི་དོན་མཛད་པ་ལ༌[^2437]སྐྱོ་བ་མི་མངའ་བའོ། །

[Block 2857 [HEADING]]
###### **བཟང་ངན་བཀོལ་བ་མེད་པ།** ^4-5-4-4-2-3-5-0

[Block 2858]
མདོ་ལས།

[Block 2859]
འཕགས་པ་དང་ནི་མ་རབས་མཚུངས་པའི་བློ། །ཞེས་པ་ནས། སྐྱོ་བ་ཐམས་ཅད་རབ་ཏུ་རྣམ་སྤངས་ནས། །ཞེས་པའི་བར་དུ་ནི་བཟང་ངན་བཀོལ་བ་མེད་པར་ཆོས་སྟོན་པ་སྟེ། དགེ་བའི་རྩ་བ་ལ་གཟིགས་ཤིང་ཆོས་སྟོན་པའོ། །

[Block 2860 [HEADING]]
###### **ཐོས་པ་རྣམས་ཕན་པ་འཐོབ་པ།** ^4-5-4-4-2-4-0

[Block 2861]
མདོ་ལས་ངས་ནི་ཡང་དག་ཆོས་ཀྱི་ཆར་པ་ཕབ། །ཅེས་པ་ནས། རྣམ་པ་མང་པོའི་ས་ལ་གནས་འགྱུར་བ། །ཞེས་པའི་བར་དུ་ནི་སེམས་ཅན་རྣམས་སུ་ཐོས་པས་བདེ་བ་རྙེད་པ་སྟོན་ཏེ། [^2438]དང་པོའི༌[^2439]ཚིག་དགུས་ནི་དཔེ་དང་དོན་དུ་སྦྱར། [^2440]དེའི་འོག་མ་ཚིག༌[^2441]ཕྱེད་དང་བཞིས་ནི་འབྲས་བུ་དང་མེ་ཏོག་རྒྱུ་མི་མཐུན་པའི་དཔེས་འབྲས་བུ་དང་སྦྱོར་བ་བསྟན། སྔར་ཚིག་བརྒྱད་ཀྱིས་ནི་དོན་བསྟན། [^2442]ཡང་ཚིག་ཕྱེད་ཀྱིས་ནི་དཔེ་བསྟན། ཚིག་དང་པོ་ལ་ཡང་གཉིས་སུ་ཕྱེ་སྟེ། སྔར་ཚིག་གཅིག་གིས་ནི་སྤྱིར་གླེང་།[^2443] ཚིག་བདུན་གྱིས་ནི་སོ་སོར་ཕྱེ་སྟེ་བསྟན་པ་ལ་འདི་ནི་དང་པོའོ། །

[Block 2862]
ས་ལ་གནས་འགྱུར་བ༌[^2444]ཞེས་པ་ནི་ཐེག་པ་ཆེན་པོའི་ས་བཅུ་དང་རིགས་ཀྱི་ས་དང་།

[Block 2863]
བརྒྱད་པ་དང་། དེ་བཞིན་གཤེགས་པའི་སའི་བར་དུ་སོ་སོར་ཕྱེ་སྟེ་བསྟན༌[^2445]པའོ། །

[Block 2864]
མདོ་ལས།

[Block 2865]
ལྷ་མིའི༌[^2446]ནང་ནས༌[^2447]ཡིད་དུ་འོང་བ་དང་། །ཞེས་པ་ནས། དེ་དག་རབ་ཏུ་ཕྲ་ཞིང་ཕྲ་བའི་སྨན། །ཞེས་པའི་བར་དུ་ནི་དཔྱད༌[^2448]ན་རིགས་མེད་པའི་དཔེ་སྟེ། ཇི་ལྟར་རྩ་བ་རབ་ཏུ་ཕྲ་ལ་ཆར་གྱིས་བརླན་པ་བཞིན་ནོ། །

[Block 2866]
འཕགས་པ་ཉན་ཐོས་རྣམས་ནི་སྨན་པར་མ་བཞིན་ནོ། །

[Block 2867]
འཕགས་པ་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ནི་སྨན་གྱི་སྡོང་པོ་ཆེན་པོ་བཞིན་ནོ། །

[Block 2868]
མདོ་ལས།

[Block 2869]
དེ་དག་ཆུང་སྟེ་འཇིག་རྟེན་འདི་ན༌[^2449]གང་། ། ཞེས་པ་ནས། དེ་ནི་སྨན་གྱི་མཆོག་ཅེས་བྱ་བ་ཡིན། །ཞེས་པའི་བར་དུ་ནི་སྨན་གྱི་སྡོང་པོའི་དཔེ་རྣམ་པ་གཉིས་བསྟན་པ་སྟེ། སངས་རྒྱས་སུ་དེ་འདྲ་བའི་སྤྱོད་པ་ཅན་སངས་རྒྱས་སུ་ངེས་ཞེས་པའི་དོན་ཏོ། །

[Block 2870]
བྱང་ཆུབ་སེམས་དཔའ་ས་བདུན་པ་མན་ཆད་ནི་སྨན་ཆུང་ངུ་ཞེས་བྱ། ས་བརྒྱད་པ་ཡན་ཆད་ནི། སྨན་གྱི་སྡོང་པོ་ཆེན་པོ་ཞེས་བྱ་སྟེ་སྤྱོད་པ་མི་ཉམས་པ༌[^2450]ཞེས་པའི་དོན་ཏོ། །

[Block 2871]
མདོ་ལས།

[Block 2872]
བདེ་བར་གཤེགས་པའི་སྲས་པོ་གང་བཞུགས༌[^2451]པ། །ཞེས་པ་ནས། དེ་ལྟ་བུ་ཡི་དཔེ་དག་བསྟན་པ་ཡིས། །ཞེས་པའི་བར་དུ་ནི་རིགས་ཅན་གྱི་ས་ནས་ཐེག་པ་ཆེན་པོའི་འབྲས་བུ་ཐོབ་པ་དང་། མྱ་ངན་ལས་འདས་པའི་བར་དུ་འབྲས་བུ་ཆེ་ཆུང་ཐོབ་པ་དང་། གྲུབ་པའི་དཔེ་བསྟན་པ་ཡིན་ནོ། །

[Block 2873]
མདོ་ལས།

[Block 2874]
དེ་བཞིན་གཤེགས་པའི་ཐབས་རྣམས་ཤེས་པར་གྱིས།[^2452] །ཞེས་པ་ནས། ཕྱོགས་བཅུ་ཀུན་ན་ཇི་ལྟར་མཛེས་པ་བཞིན། །ཞེས་པའི་བར་དུ༌[^2453]ནི་འབྲས་བུ་སོ་སོར་སྨིན་ཅིང་ཐོབ་པ་ཁྱད་པར་དུ་གྱུར་པ་དང་དཔེ༌[^2454]དོན་དུ་སྦྱར་ཏེ་རྒྱས་པར་བསྟན་པའོ། །

[Block 2875]
མདོ་ལས།
--- END BLOCKS ---
