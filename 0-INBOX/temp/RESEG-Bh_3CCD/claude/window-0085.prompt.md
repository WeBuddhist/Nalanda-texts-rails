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

[Block 2981]
སེམས་ཅན་ཁམས་ནི་མ་ལུས་པའི། །ཞེས་པ་ནི་ཁམས་གསུམ་ན་སྤྱོད་པའི་སེམས་ཅན་གྱི་ཁམས་ཀྱིའོ། །

[Block 2982]
རང་བཞིན་རྩ་བ་འདི་ཡིན་ནོ། །ཞེས་པ་ནི་ཤེས་རབ་དང་ཐབས་དང་མ་རིག་པའི་ངོ་བོ་ཉིད་འདོད་ཆགས་དང༌[^1943]བྲལ་བ་ལ་སོགས་པ་བརྒྱ་དྲུག་ཅུ་རྣམས་ཀྱི་རྩ་བ་སྟེ་རྒྱུའོ། །

[Block 2983]
དེ་རྣམས་རྣམ་པར་ཤེས་པ་གསུམ་ལས་བྱུང་བའི་ཕྱིར་རོ། །

[Block 2984]
ཇི་སྐད་དུ།

[Block 2985 [VERSE]]
ལེན་པའི་རྣམ་པར་ཤེས་པ་ཟབ་ཅིང་ཕྲ། །
ས་བོན་ཐམས་ཅད་ཆུ་བོའི་རྒྱུན་བཞིན་འབབ། །
བདག་ཏུ་རྟོག་པར་གྱུར་ན་མི་རུང་ཞེས། །
ཉན་ཐོས་བྱིས་པ་རྣམས་ལ་ངས་མ་བསྟན།[^1944] །

[Block 2986]
ཞེས་འབྱུང་བ་དང་། དེ་བཞིན་དུ་ཡང་།

[Block 2987 [VERSE]]
ཡང་དག་མ་ཡིན་ཀུན་བརྟགས་ནི། །
སེམས་དང་སེམས་བྱུང་ཁམས་གསུམ་པ། །

[Block 2988]
ཞེས་འབྱུང་ངོ་། །དེ་ནི༌[^1945]རླུང་དང་རྣམ་པར་ཤེས་པ་ཡང་དག་པར་སྦྱོར་བས་འགྲོ་བ་རྣམས་ཀྱི་སྐྱེ་བ་བསྟན་པར་བྱ་བའི་ཕྱིར། ཏཾ། ད་ནི་རེ་རེ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། མིག་ལ་སོགས་པའི་དབང་པོའི་སྒོ་ནས། སྔོན་པོ་ལ་སོགས་པའམ་བདེ་བ་ལ་སོགས་པའི་དོན་གང་དང་གང་སྣང་བ་དེ་དང་དེ་དག་རླུང་གིས་ཁོ་ན་ཡང་དག་པར་བླངས་ནས་འཛིན་པར་བྱེད་དེ། གཡོ་འགུལ་ལ་སོགས་པའི་ངོ་བོ་དེ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2989]
རྣམ་པར་ཤེས་པས་ནི་མ་ཡིན་ཏེ།

[Block 2990 [VERSE]]
གཡོ་འགུལ་ལ་སོགས་པ་མེད་པའི་ཕྱིར་རོ། །
དེ་བས་ན་འཕྱེ་བོ་དང་ལོང་བ་བཞིན་དུ། །

[Block 2991]
རླུང་དང་ལྡན་པའི་རྣམ་ཤེས་ནི། རྟག་ཏུ་འགྲོ་ལ་གནས་པར་འགྱུར། །ཞེས་བྱ་བ་འདི༌[^1946]སྲིད་པ་གསུམ་གྱི་བར་དུ་ཡང་འགྲོ་བ་དང་འོང་ཞིང་འཇུག་པར་འགྱུར་རོ། །

[Block 2992]
ལས་ཀྱི་ལུས་ཀྱིས་སྐྱེ་བ་བསྟན་པར་བྱ་བའི་ཕྱིར། །ཨེ། འདི་ནི་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། འཆི་བའི་སྲིད་པ་འདས་ནས་ཞག་ཉི་ཤུ་རྩ་གཅིག་གི་བར་དུ་བར་མ་དོའི་སྲིད་པ་ནམ་མཁའ་ལ་གནས་པར་འགྱུར་ཏེ། རང་གི་གཉེན་དང་གནས་ལ་སོགས་པ་དང་བདག་གི་ལུས་འདི་ཡིན་ཞེས་ཡོངས་སུ་ངོ་ཤེས་ཤིང་གནས་སོ། །

[Block 2993]
དེ་བས་ན་ལས་ཀྱི་རླུང་གིས་བསྐུལ་བས་ཕ་མའི་གཡེམ་པའི་དུས་སུ་ཞེ་སྡང་དང་བཅས་པའམ་འདོད་ཆགས་དང་བཅས་པར༌[^1947]སྐྱེ་གནས་སུ་འཇུག་ཅིང་ལུས་ལེན་པར་བྱེད་དོ། །

[Block 2994]
དེ་བས་ན་རྣམ་པར་ཤེས་པ་གསུམ་གྱི་ནི་བཞི་པ་སྟེ་སྐུལ་བར་བྱེད་པའོ། །

[Block 2995 [VERSE]]
དེ་ཡིས༌[^1948]རང་བཞིན་རྟག་ཏུ་ནི། །
ཇི་ལྟ་ཇི་ལྟར་ངེས་པར་འབྱུང་། །

[Block 2996]
ཞེས་པ་ནི་རྣམ་པར་ཤེས་པ་རྣམས་ལས།

[Block 2997]
སེམས་ལས་བྱུང་བའི་ངོ་བོ་ཉིད་ཀྱི་འདོད་ཆགས་བྲལ་བ་ལ་སོགས་པ་རང་བཞིན་རྣམས་སྐད་ཅིག་ལ་སོགས་པའི་དུས་ཀྱི་དབྱེ་བ་དང་། ཡུལ་གྱི་སྣང་བ་ཡོད་པ་ལས་སྐྱེ་བར་འགྱུར་རོ། །

[Block 2998]
མངལ་ནས་འབྱུང་བའི་ངོ་བོ་བསྟན་པར་བྱ་བའི་ཕྱིར། ཀ །སྲ་བའི་ཁམས་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། རླུང་ཉིད་ཀྱིས་འབྱུང་བ་ཆེན་པོ་བཞི་བླངས་ཏེ། ལུས་ཅན་རྣམས་ཁམས་གསུམ་དུ་འཁོར་བར་བྱེད་དོ། །

[Block 2999]
ཕུང་པོ་འབྱུང་བ་བསྟན་པར་བྱེད་པའི༌[^1949]ཕྱིར། སྨིན། འདི་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་པ་འདིས་དེ་ལྟ་བུའི་ལུས་པོ་གཟུགས་ལ་སོགས་པའི་ཕུང་པོ་ལྔའི་བདག་ཉིད་དུ་སྐྱེ་བར་འགྱུར་རོ། །

[Block 3000]
འདུས་བྱས་མཚན་ཉིད་ནི་དེ་དག་རྟེན་ཅིང་འབྲེལ་པ་ལས་འབྱུང་གི་རང་དབང༌[^1950]དུ་ནི་མ་ཡིན་ནོ། །

[Block 3001]
ཇི་སྐད་དུ།

[Block 3002 [VERSE]]
དངོས་པོ་ལས་ནི་དངོས་མི་སྐྱེ། །
དངོས་མེད་ལས་ཀྱང་འབྱུང་བ་ཡིན།[^1951] །
དངོས་པོ་རྟག་ཏུ་སྐྱེ་བ་ནི། །
འཁྲུལ་པས་མཁའ་ཡི༌[^1952]མེ་ཏོག་བཞིན། །

[Block 3003 [VERSE]]
བདག་ལས་མ་ཡིན་གཞན་ལས་མིན། །
གཉི་ག་ལས་མིན་རྒྱུ་མེད་མིན། །
དངོས་པོ་གང་དང་གང་ན་ཡང་། །
སྐྱེས་པ་ནམ་ཡང་ཡོད་མ་ཡིན། །

[Block 3004]
ཞེས་འབྱུང་བས་སོ། །

[Block 3005]
དེ་བས་ན་འཁྲུལ་པ་ཙམ་གྱི་ངོ་བོ་གཟུགས་ལ་སོགས་པ་ཕུང་པོ་ལྔ་ཞེས་ཐ་ཚིག་གོ། །

[Block 3006]
བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི༌[^1953]རྣམ་འགྲེལ་ལས་ཀྱང་།

[Block 3007 [VERSE]]
གཟུགས་ནི་ལྦུ་བ༌[^1954]ལྟ་བུ་སྟེ། །
ཚོར་བ་ཆུ་བུར་ལྟ་བུ་ཡིན། །
འདུ་ཤེས་སྨིག་རྒྱུ་ལྟ་བུ་སྟེ། །
འདུ་བྱེད༌[^1955]ཆུ་ཤིང་དང་འདྲ་ཞིང་། །

[Block 3008 [VERSE]]
རྣམ་ཤེས་སྒྱུ་མ་ལྟ་བུ་སྟེ། །
ཕུང་པོའི་བསྟན་པ་འདི་ཡིན་ནོ། །

[Block 3009]
ཞེས་འབྱུང་ངོ་། །ཀུན་ནས་ཉོན་མོངས་པའི་ཕྱོགས་བསྟན་ནས་རྣམ་པར་བྱང་བའི་ཕྱོགས་བསྟན་པར་བྱ་བའི་ཕྱིར། ས། མཉམ་ཉིད་ཅེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། ཕུང་པོ་ལྔ་གནས་གྱུར་པས་ཡེ་ཤེས་ལྔ་ཐོབ་པའི་རྣམ་པར་ཤེས་པ་གསུམ་ཁོ་ན་རྒྱུ་ཡིན་ནོ། །

[Block 3010]
དེ་མེད་པས་ཕུང་པོ་ཡང་མེད་དོ། །

[Block 3011]
ཅིའི་རྣམ་པར་དག་པར་བྱ་བའི་ཕྱིར་ཡེ་ཤེས་སྐྱེའོ། །

[Block 3012]
སྐྱེ་མཆེད་ཀྱི་བསྐྱེད་པ་བསྟན་པར་བྱ་བའི་ཕྱིར། མ། [^1956]ཡིད་ཀྱི་སྐྱེ་མཆེད་ཅེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། ཡིད་ལ་སོགས་པ་ནང་གི་སྐྱེ་མཆེད་དྲུག་སྟེ། གང་གིས༌[^1957]ལས་ཀྱི་ལུས་པོ་འདི་དང་ཡུལ་རྣམས་དང་ལེན་པར་བྱེད་དེ། འདིར་ནི་ཚིགས་སུ་བཅད་པ་གཅིག་འདོར༌[^1958]ཏེ་བཤད་པར་བྱ་བ་ཡིན་ནོ། །

[Block 3013]
ལུས་སྐྱེས་པས་ལས་ཀྱི་དབང་གིས་སྐྱེ་བ་ལེན་པ་བསྟན་པར་བྱ་བའི་ཕྱིར། བྷ། འབྱུང་བ་འདི༌[^1959]ལས་རང་བཞིན་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། འདོད་ཆགས་ལ་སོགས་པའི་རང་བཞིན་བརྒྱ་དྲུག་ཅུའི་དབང་གིས་དགེ་བ་དང་མི་དགེ་བའི་ལས་བྱས་ནས་དེ་ནས་ཤི་འཕོས་ཏེ་ངན་སོང་དང་བདེ་འགྲོ་ལ་སོགས་པའི་མཚན་ཉིད་ཅན་སྐྱེ་བ་ཐོབ་པ་གང་ཡིན་པ་དེའི་རྒྱུ་ནི་རྣམ་པར་ཤེས་པ་གསུམ་པོ་ཁོ་ན་ལས་གཞན་མ་ཡིན་ནོ། །

[Block 3014]
བསྐྱེད་པའི་རིམ་པ་ཕུང་པོ་རྣམ་པར་དག་པ་བསྟན་པར་བྱ་བའི་ཕྱིར། ག །འགྲོ་བར་བྱེད་ཅེས༌[^1960]བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། འགྲོ་བ་ནི་མི་ལ་སོགས་པའི་འགྲོ་བའོ། །

[Block 3015]
དེས་ན་བདེ་འགྲོ་དང་ངན་འགྲོ་དག་ཏུ་ཉེ་བར་ལེན་པའི་ཕུང་པོ་ལྔ་གཟུགས་ལ་སོགས་པ་གང་ཡིན་པ་དེ་དག་འབྱུང་བ༌[^1961]ནི་སྐྱེ་བར་འགྱུར་ཏེ་ཉོན་མོངས་པ་དང་ལས་དང་རྣམ་པར་སྨིན་པའི་ངོ་བོ་ཉིད་ཀྱི༌[^1962]རྟེན་ཅིང་འབྲེལ་པ་ཡན་ལག་བཅུ་གཉིས་ཀྱི་མཚན་ཉིད་ཅན་སྲིད་པའི་འཁོར་ལོས་ཡོངས་སུ་འཁོར་རོ། །
--- END BLOCKS ---
