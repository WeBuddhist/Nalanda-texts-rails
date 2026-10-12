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
[Block 2941]
དེ་ལ་སེམས་ནི་རྣམ་གསུམ་སྟེ། སེམས་དང་། ཡིད་དང་། རྣམ་པར་ཤེས་པ་སྟེ། དེ་ཉིད་འཇུག་པའི་རྣམ་པར་ཤེས་པ་དང་། ཉོན་མོངས་པ་ཅན་གྱི་ཡིད་དང་། ཀུན་གཞི་རྣམ་པར་ཤེས་པའོ། །

[Block 2942]
དེ་ལ་འཇུག་པའི་རྣམ༌[^1924]པར་ཤེས་པ་གནས་གྱུར་པ་ཟླ་བའི་སྣང་བ་དང་འདྲ་བའི་སྣང་བའི་ཡེ་ཤེས་སྐྱེ་བར་གྱུར་པ་དང་། འདོད་ཆགས་བྲལ་བ་ལ་སོགས་པའི་རང་བཞིན་སུམ་ཅུ་རྩ་གསུམ་འགོག་པར་འགྱུར་རོ། །

[Block 2943]
ཉོན་མོངས་པ་ཅན་གྱི་ཡིད་གནས་གྱུར་པས་ཉི་མའི་འོད་ཟེར་དང་འདྲ་བའི་སྣང་བ་མཆེད་པའི་ཡེ་ཤེས་སྐྱེ་བ་དང་། འདོད་ཆགས་ལ་སོགས་པ་རང༌[^1925]བཞི་བཅུ་འགོག་པར་འགྱུར་རོ། །

[Block 2944]
ཀུན་གཞི་རྣམ་པར་ཤེས་པ་གནས་གྱུར་པས་མཚམས་ཀྱི་སྣང་བ་དང་འདྲ་བའི་སྣང་བ་ཉེ་བར་ཐོབ་པའི་ཡེ་ཤེས་སྐྱེ་བར་འགྱུར་བ་དང་། ཆགས་པ་བར་མ་ཞེས་བྱ་བ་ལ་སོགས་པས་རང་བཞིན་བདུན་འགོག་པར་འགྱུར་རོ། །

[Block 2945]
དེ་ཡང་གང་གི་ཚེ་ཐམས་ཅད་སྟོང་པ་ལ་འཇུག་པ་དེའི་ཚེ། སྤྲིན་མེད་པའི་ནམ་མཁའ་དང་འདྲ་བའི་འོད་གསལ་བའི་དེ་ཁོ་ན་ཉིད་འཆད་པར་འགྱུར་རོ། །

[Block 2946]
དེའི་ཕྱིར་རྣམ་པར་ཤེས་པ་གསུམ་པོའི་རྣམ་གྲངས་ནི་ཤེས་རབ་དང་ཐབས་དང་མ་རིག༌[^1926]པའོ། །

[Block 2947]
སྣང་བ་གསུམ་ནི་གཉེན་པོའི་ཕྱོགས་སོ། །

[Block 2948]
སྟོང་པ་ལ་སོགས་པ་གསུམ་ནི་དེ་རྣམ་པར་དག་པའི་ཐབས་སོ། །

[Block 2949]
འབྲས་བུར་གྱུར་པ་ནི་སེམས་ཀྱི་འོད་གསལ་བའོ། །

[Block 2950]
ལ་ལའི་སྐབས་སུ་མི་མཐུན་པའི་ཕྱོགས་ཀྱི་མིང་གིས་གཉེན་པོ་བསྟན་པ༌[^1927]དང་། གཉེན་པོའི་མིང་གིས་མི་མཐུན་པའི་ཕྱོགས་བསྟན་པ་དང་། དེའི་ཐབས་ཀྱི་མིང་གིས་ཀྱང་དེ་དག་བསྟན་པ་དང་། དེ་དག་གི་མིང་གིས་ཀྱང་དེ༌[^1928]ཉིད་བསྟན་པའོ། །

[Block 2951]
དཔེར་ན་ཆར་གྱིས་བྱས་པའི༌[^1929]མུ་གེ་ནི་ཆར་མེད་པས་མུ་གེ་བྱུང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2952 [HEADING]]
###### དང་པོ་ཤེས་རབ་ཀྱི་ཡེ་ཤེས། ^1-8-1-1-1-0

[Block 2953]
དེ་ལ་དང་པོ་ཤེས་རབ་ཀྱི༌[^1930]ཡེ་ཤེས་བསྟན་པར་བྱ་བའི་ཕྱིར། ཨེ་ནི་ཤེས་རབ་དམ་པ་ཞེས་སྨོས་ཏེ། ཤེས་རབ་ནི་འཇུག་པའི་རྣམ་པར་ཤེས་པའོ། །

[Block 2954]
དབང་པོ་དང་ཡུལ་དང་སྣང་བ་དང་ཡིད་ལ་བྱེད་པའི་རྟེན་ཅིང་འབྲེལ་པ་ཚོགས་པ་ལས་རབ་ཏུ་ཤེས་པ་སྟེ་རྣམ་པར་ཤེས་པའི་ཚོགས་དྲུག་གོ། །

[Block 2955]
འདོད་ཆགས་བྲལ་སོགས་སྐད་ཅིག་བདག །ཅེས་པ་ནི་འདོད་ཆགས་བྲལ་བ་ལ་སོགས་པ་རང་བཞིན་སུམ་ཅུ་རྩ་གསུམ་གྱི་ངོ་བོའོ། །

[Block 2956]
སྲིད་པ་གསུམ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་ཁམས་གསུམ་ན་གནས་པའི་གཟུགས་རྣམ་པ་གསུམ་ལ་སོགས་པ་ཡུལ་དག་ཏུའོ། །

[Block 2957]
ཡོངས་སུ༌[^1931]ཤེས་པ་ནི་ཡུལ་གཟུང་བའི༌[^1932]ངོ་བོ་ཉིད་དོ། །

[Block 2958]
འདི་ནི་རྩ་བར་ཞེས་པ་ལ་མིག་ལ་སོགས་པའི་རྣམ་པར་ཤེས་པའོ། །

[Block 2959 [HEADING]]
###### གཉིས་པ། ^1-8-1-1-2-0

[Block 2960]
གཉིས་པ་བསྟན་པར་བྱ་བའི་ཕྱིར་ཁམས་ནི་འོད་མ་འགྲེང་བ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་པ་ལ། རྣམ་པར་ཤེས་པ་ནི་ཉོན་མོངས་པ་ཅན་གྱི་ཡིད་གཉིས་པ་སྟེ་བདག་ཏུ་ལྟ་བ་ལ་སོགས་པ་བཞི་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 2961]
ཝཾ། འོད་མ་འགྲེང་བ་ལྟར་ཞེས་པ་ནི་དཔེར་ན་ཁོང་སྟོང་འོད་མ་ཡིན་ཡང་ཚིགས་མདུད་ཀྱི་དབང་གིས་བསྟན་པ་ཉིད་དུ་འགྱུར་རོ། །

[Block 2962]
དེ་བཞིན་དུ་རང་བཞིན་གྱིས་སྟོང་པ་ཡིན་ཡང་ཤེས་པ་དེ་ཉིད་ཉོན་མོངས་པའི་མདུད་པ་བཞིའི་དབང་གིས་བསྟན་པར་སྣང་བར་འགྱུར་རོ། །

[Block 2963]
སེམས་ལས་བྱུང་བ་བསྟན་པར་བྱ་བའི་ཕྱིར། འདོད་ཆགས་ལ་སོགས་རབ་སྐྱེ་ལྡན། །ཞེས་པ་ནི་ཐབས་ཀྱི་ངོ་བོ་ཉིད་རང་བཞིན་བཞི་བཅུའི་སྐད་ཅིག་མ་ལ་སོགས་པའི་དབྱེ་བས་སྐྱེ་བ་གང་ཡིན་པ་དེ་དང་ལྡན་པའོ། །

[Block 2964]
དེ་བཞིན་དུ་གཉེན་པོའི་མིང་གིས་སྣང་བ་མཆེད་པ་ཞེས་བརྗོད་དོ། །

[Block 2965]
[^1933]དེ་འགོག་པས་དེ་དམིགས་པའི་ཕྱིར་རོ། །

[Block 2966]
དེ་ཉིད་ཐབས་ཞེས་པ་ནི་འཁོར་བའི་གྲོང་ཁྱེར་སྣ་ཚོགས་པ་སྤྲུལ་པའི་རྒྱུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2967]
མིང་ཞེས་པ་ནི་དེ་ཉིད་ཀྱི་བརྡ༌[^1934]རུ་ཤེས་པར་བྱའོ། །

[Block 2968 [HEADING]]
###### གསུམ་པ། ^1-8-1-1-3-0

[Block 2969]
གསུམ་པ་བསྟན་པར༌[^1935]བྱ་བའི་ཕྱིར། མ། རིག་ཆེན་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། རིག་ཆེན༌[^1936]ནི་ཆོས་ཀྱི་དབྱིངས་ཀྱི་ངོ་བོ་སྟེ་འོད་གསལ་བའོ། །གང་གི་ཕྱིར་ཞེ་ན། མ་རིག་པ་ནི་ཟླ་བ་ཡི། །[^1937]ཞེས་སྨོས་ཏེ། ཀུན་གཞི་རྣམ་པར་ཤེས་པ་རང་བཞིན་བདུན་དང་བཅས་པར་འགོག་པར་བྱེད་པས་སོ། །

[Block 2970]
མ་རིག་པ་ནི་ཀུན་གཞི་རྣམ་པར་ཤེས་པའོ། །

[Block 2971]
འདི་འབྱུང་བ་ཞེས་པ་ནི་དེ་སྤངས་པས་དེ་བས་སྣང་བ་འབྱུང་བ་ནི་མཚམས་ཀྱི་སྣང་བ་དང་འདྲ་བའི་སྣང་བ༌[^1938]ཐོབ་པ་སྐྱེ་བར་འགྱུར་རོ། །

[Block 2972]
རྣམ་པར་ཤེས་པ་གསུམ་གྱི་མཚན་ཉིད་བསྟན་ནས་གཉེན་པོའི་སྒོ་ནས་འོད་གསལ་བ་ལ་འཇུག་པ་བསྟན་པར་བྱ་བའི་ཕྱིར།[^1939] །ཡཱ། གང་ཡང་རྣམ་ཤེས་དང་པོ་སྟེ། །ཞེས་སྨོས་ཏེ། དང་པོའི་རྣམ་པར་ཤེས་པ་ནི་སྔགས་སམ་ཕྱག་རྒྱའི་རིམ་པས་སྦྱངས་པ་ན། སྣང་བ་མཆེད་པའི་མིང་ནི་ཡེ་ཤེས་གཉིས་པ་ཉིད་དུ་འགྱུར་རོ། །

[Block 2973 [VERSE]]
དེ་ནི་སྣང་བ་མཆེད་པ༌[^1940]དག་པའོ། །
དེ་ནི་སྟོང་པ་ཆེར༌[^1941]འགྱུར་ལ། །

[Block 2974]
ཞེས་པ་ནི་མཚམས་ཀྱི་སྣང་བ་དང་འདྲ་བའི་སྣང་བ་ཐོབ་པའི་ཡེ་ཤེས་ཀྱི་ངོ་བོ་ཉིད་དུ་འགྱུར་རོ། །

[Block 2975]
དེ་ནི་སྟོང་པ་ཆེན་པོའི་ངོ་བོ་ཉིད་སྣང་བ་མཆེད་པའི་ཡེ་ཤེས་དག་པར་འགྱུར་བས་འོད་གསལ་བ་ནི་ཐམས་ཅད་སྟོང་པ་འོད་གསལ་བར་འགྲོ་བ་ནི་འགྱུར་བའོ། །

[Block 2976]
དགོངས་པ་འདིས་རབ་ཏུ་བྱེད་མཁན་གྱིས་ཀྱང་གསུངས་ཏེ།

[Block 2977 [VERSE]]
སྟོང་ཉིད་ཤིན་ཏུ་སྟོང་པ་དང་། །
གསུམ་པ་སྟོང་པ་ཆེན་པོ་དང་། །
བཞི་པ་ཐམས་ཅད་སྟོང་པ་ནི། །
རྒྱུ་དང་འབྲས་བུའི་བྱེ་བྲག་གོ། །

[Block 2978 [VERSE]]
སྣང་བ་སྣང་བ་མཆེད་པ་དང་། །
དེ་བཞིན་སྣང་བ་ཉེར་ཐོབ་པ། །
སེམས་ནི་རྣམ་པ་གསུམ་བསྟན་པ། །
དེ་ཡི་བསྒྲུབ་པ༌[^1942]བཤད་པར་བྱ། །

[Block 2979]
ཞེས་འབྱུང་ངོ་། །བསྡུ་བ་བསྟན་ནས་བསྐྱེད་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 2980]
ཤྲུ། སྣང་བ་གསུམ་གྱིས་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། སྔོན་དུ་བཤད་པའི་རྣམ་པར་ཤེས་པ་གསུམ་པོ་གང་ཡིན་པ་དེ་སྣང་བ་གསུམ་གྱི་མཚན་ཉིད་ཅན་དེ་འགོག་པས་སྣང་བ་ལ་སོགས་པའི་སྒྲས་བརྗོད་པར་བྱ་བར་འགྱུར་རོ། །
--- END BLOCKS ---
