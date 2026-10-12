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
[Block 4901 [VERSE]]
སྔགས་ནི་རྣམ་ཤེས་ལས་འབྱུང་བའི། །
འབུམ་ཕྲག་དྲུག་ཏུ་བཟླས་བྱས་ཏེ། །
རྡོ་རྗེ་སེམས་ལ་ཕྱག་འཚལ་ནས། །
དེ་ནི་ཉ་ལ་འགྲུབ་པར་འགྱུར། །

[Block 4902]
ཞེས་འབྱུང་ངོ་། །རྣམ་པ་གཞན་གྱིས་ཀྱང་རྡོ་རྗེ་བཟླས་པ་བསྟན་པའི་ཕྱིར། ཨོཾ་ཤཱུ་ནྱ་ཏཱ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། ཟུང་ནི་ཚིག་གཉིས་སོ། །

[Block 4903]
དང་པོ་རྣམ་པར་སྣང་མཛད་དོ། །

[Block 4904]
ཛྙཱ་ན་བཛྲ་གཉིས་པོ་ཞེས་པ་ནི་སྣང་བ་མཐའ་ཡས་སོ། །

[Block 4905]
སྭ་བྷཱ་བ་ཨཱཏྨ་ཀོ྅ཧཾ་གྱུར་ཞེས་པ་ནི་ཚིག་གཉིས་ཀྱིས་མི་བསྐྱོད་པ་བསྟན་ཏོ། །

[Block 4906]
དེ་ཉིད་གསུམ་དུ་འདིར་བརྟགས་པའོ༌[^2905]ཞེས་པ་ལ་སྐུ་གསུང་ཐུགས་ཀྱི་བདག་ཉིད་ཅན་གྱི་རྡོ་རྗེ་འཆང་ཆེན་པོ་ཨ་ཧཾ་ཞེས་ཅིག་ཅར་དུ་ང་རྒྱལ་བསྐྱེད་ལ་སྔ་མ་བཞིན་དུ། ལྷ་ལ་སོགས་པའི་རྣལ་འབྱོར་གྱི་བཟླས་པ་བྱའོ། །

[Block 4907]
རབ་ཏུ་བྱེད་པ་ལས་ཀྱང་།

[Block 4908 [VERSE]]
འཇུག་པ་དང་ནི་གནས་པ་དང་། །
ལྡང་བ་ཡི་ནི་རིམ་པ་ཡིས། །
མཚོན་བྱ་མཚོན་བྱེད་གྲངས་ཀྱིས་ནི། །
ཡན་ལག་མ་ཉམས་གསང་སྔགས་བཟླས། །

[Block 4909]
ཞེས་འབྱུང་ངོ་། །ཡང་ན་སྐུ་རྡོ་རྗེ་ལ་སོགས་པ་རྣལ་འབྱོར་པ་གསུམ་གྱིས་སྣའི་རྩེ་མོར་ཡུངས་ཀར་གྱི་འབྲས་བུའི་ཚོད་ཙམ་གྱི༌[^2906]ཐིག་ལེ་ཕྲ་མོར་བསྒོམས༌[^2907]ལ་བརྟན་པའི་རྟགས་མཐོང་བའི་བར་དུ་བཟླས་པར་བྱའོ། །

[Block 4910]
དེ་ཉིད་གསུམ་ནི༌[^2908]གཅིག་གྱུར་པ། །ཞེས༌[^2909]པ་ནི་སྐུ་ལ་སོགས་པ་ཉེ་བར་སྡུད་པ་ལས་འབྱུང་བའི་གཟུགས་སོ། །

[Block 4911]
ཡང་དག་ཅེས་པ་ནི་རྣལ་འབྱོར་པའི་མངོན་སུམ་མམ་རང་རིག་པའི་མངོན་སུམ་གྱིས་ཐོབ་པར་བྱ་བ་གསལ་བར་སྣང་བ་རྣམ་པར་མི་རྟོག༌[^2910]མ་འཁྲུལ་པ་ཞེས་པའི་ཐ་ཚིག་གོ། །

[Block 4912]
གསལ་བ་ཞེས་བྱ་བ་ནི་དག་ཅིང་ཟླ་བ་དང་ཀུན་ད་ལྟར་མཚུངས་པའི་ཕྱིར་རོ། །

[Block 4913]
མི་གསལ་ཞེས་པ་ནི་ཁམས་ཉི་ཤུ་རྩ་བཞི་ཉེ་བར་བསྡུས་པ་ལས་བྱུང་བའི་ཞལ་དང་ཕྱག་དང་སྐུ་མདོག་དང་དབྱིབས་ལ་སོགས་པ་དང་བྲལ་བ་ཐིག་ལེའི་གཟུགས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4914]
ལྷ་མོ་བཞིས་ཡོངས་སུ་ཞུས་པའི་བཤད་པའི་རྒྱུད་ལས་ཀྱང་། །

[Block 4915 [VERSE]]
དེ་ཕྱིར་ལྷ་མོ་བཤད་བྱ་བ། །
སྙིང་པོ་ལས་ནི་སྙིང་པོ་མཆོག །
སངས་རྒྱས་ཀུན་གྱི་གསང་བ༌[^2911]ན། །
ཐམས་ཅད་བདག་ཉིད་གང་ཞིག་གནས། །

[Block 4916 [VERSE]]
དེ་ཉིད་ཡེ་ཤེས་ལྔ་རང་བཞིན། །
ཡུངས་ཀར་གྱི་ནི་འབྲུ་ཚོད་ཙམ། །
དེ་ཡི་དབུས་ན་གནས་པའི་ལྷ། །
མི་གསལ་གསལ་བའི༌[^2912]བདག་ཉིད་ཅན། །

[Block 4917]
ཞེས་འབྱུང་ངོ་། །

[Block 4918 [HEADING]]
### སེམས་ལ་དམིགས་པ་ལ་སོགས་པའི་རིམ་པ་བཞི། ^3-1-0

[Block 4919]
རྡོ་རྗེ་བཟླས་པ་བཤད་ནས། སེམས་ལ་དམིགས་པ་ལ་སོགས་པའི་རིམ་པ་བཞི་བསྟན་པར་བྱ་བའི་ཕྱིར། །ཡང་དག་པར་སྦྱོར་བ༌[^2913]གསུམ་གྱི་སྐུར་བསྒོམ་ཞིང་ཞེས་པ་ནི་སྣང་བ་ལ་སོགས་པ་གསུམ་གྱིས་ཉེ་བར་མཚོན་པའི་འོད་གསལ་བའི་དེ་ཁོ་ན་ཉིད་དོ། །

[Block 4920]
སྣང་བ་གསུམ་གྱི་ཚོགས་ཀྱིས༌[^2914]སྣང་བ་འཁྲིགས་པའོ་ཞེས་པ་ནི་སྔགས་དང་ཕྱག་རྒྱའི་རིམ་པས་ཐོབ་པའི་ཟླ་བ་དང་ཉི་མ་དང་མཚམས་ཀྱི་སྣང་བ་དང་འདྲ་བའི་སྣང་བ་ལ་སོགས་པའི་ཡེ་ཤེས་ཀྱི་ངོ་བོ་སྟེ་དེ་ཁོ་ན་ཉིད་བཞི་པོ༌[^2915]འོད་ཀྱི་ཚོགས་དང་བཅས་པ་སྤྲིན་མེད་པའི་ནམ་མཁའ་དང་མཚུངས་པ་ཐམས་ཅད་སྟོང་པ་ཞེས་བྱ་བའི་དེ་ཁོ་ན་ཉིད་བསྒོམ་པར་བྱའོ། །

[Block 4921]
དེས་ནི་སེམས་ལ་དམིགས་པའི་རིམ་པ་བསྟན་ཏོ། །

[Block 4922]
འཇའ་ཚོན་ལྟར་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་སྔོན་གྱི་སྨོན་ལམ་གྱི་ཤུགས་ཀྱིས༌[^2916]ཡེ་ཤེས་ཀྱི༌[^2917]སྐུ་སྒྱུ་མའི་དཔེ་བཅུ་གཉིས་ཀྱིས་ཉེ་བར་མཚོན་པ་བསྒོམ་པར་བྱའོ། །

[Block 4923]
དཀར་པོ་ལ་སོགས་པའི་འོད་ཟེར་ལྔས་བརྒྱན་པའོ༌[^2918]ཞེས་པ་ནི་དཀར་པོ་ལ་སོགས་པའི་སྐུ་མདོག་ལྔས་ཉེ་བར་མཚོན་པའི་དེ་བཞིན་གཤེགས་པ་རིགས་ལྔ་ལས་འབྱུང་བ་ལྷ་མོ་དང་བྱང་ཆུབ་སེམས་དཔའ་དང་ཁྲོ་བོའི་རྒྱལ་པོ་དང༌[^2919]བཅས་པའོ། །

[Block 4924]
ཁམས་ཕྲ་བ་ཞེས་པ་ལ། འོད་གསལ་བའི་དེ་ཁོ་ན་ཉིད་དོ། །

[Block 4925]
སྣང་བ་མཆེད་པ་ལ་སོགས་པའི་རིམ་པའམ་ཅིག་ཅར་གྱི་རྣལ་འབྱོར་གྱིས་དེ་ལས་འབྱུང་བའི་ཡོངས་སུ་རྫོགས་པ༌[^2920]ཞེས་བྱའོ། །

[Block 4926]
དངོས་པོ་ཐམས་ཅད་ཀྱི་ངོ་བོ་ཉིད་དོ་ཞེས་པ་ལ་བརྟན་པ་དང་གཡོ་བའི་བདག་ཉིད་དམ། རང་དང་གཞན་གྱི་རྒྱུད་སྒྱུ་མའི་དཔེ་བཅུ་གཉིས་ཀྱིས༌[^2921]ཉེ་བར་མཚོན་པའི་རང་བཞིན་ཡིན་ནོ། །

[Block 4927]
རྒྱུ་བ་ལ་སོགས་པའི་འོད་ཟེར་ལྔ་སྟེ་ཞེས་པ་ལ་རྒྱུ་བ༌[^2922]དང་རྣམ་པར་རྒྱུ་བ་དང་ཡང་དག་པར་རྒྱུ་བ་དང་།

[Block 4928]
རབ་ཏུ་རྒྱུ་བ་དང་ངེས་པར་རྒྱུ་བ་དང་ཞེས་བྱ་བ་ཡན་ལག་གི་རླུང་ལྔ་སྟེ་སྒྲ་ཇི་བཞིན་མ་ཡིན་པས་རྡོ་རྗེའི་སྒོ་ཞེས་བྱ་བའི༌[^2923]རྣལ་འབྱོར་ཆེན་པོའི་རྒྱུད་ལས།

[Block 4929 [VERSE]]
སྦྲུལ་དང་རུས་སྦལ་རྩངས་པ་དང་། །
ལྷ་སྦྱིན་དང་ནི་གཞུ་ལས་རྒྱལ། །

[Block 4930]
ཞེས་འབྱུང་ངོ་། །

[Block 4931]
དེ་རྣམས་ཀྱི་འོད་ཟེར་ནི་ཡུལ་གཟུང་བར༌[^2924]བྱ་བའི་ཕྱིར་མིག་ལ་སོགས་པའི་དབང་པོ་རྣམས་འཇུག་གོ། །

[Block 4932]
དེ་དང་ལྡན་པ་ནི་སོ་སོར་སྡུད་པ་དང་བསམ་གཏན་གྱི་ཡན་ལག་དག་གིས་ཡུལ་དང་དབང་པོའི་ཉེ་བར་སྤྱོད་པ་དང་ལྡན་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 4933]
ཇི་སྐད་དུ།

[Block 4934 [VERSE]]
གང་ཞིག་མཐོང་བ་རེག་པ་དང་། །
ཐམས་ཅད་སྒྱུ་མ་བཞིན་མཐོང་སྟེ། །
ཀུན་རྫོབ་ཏུ་ནི་མི་གནས་པས། །
སྒྱུ་མ་བཞིན་དུ་མཚོན་པར་བྱ། །

[Block 4935 [VERSE]]
དབང་པོ་གང་དང་གང་ལམ་གྱིས། །
དེ་དང་དེ་ཡི་རང་བཞིན་འགྲོ། །
མཉམ་པར་མ་བཞག་སྦྱོར་བ་ཡིས། །
སངས་རྒྱས་ཀུན་གྱི༌[^2925]རང་བཞིན་ལྷ། །

[Block 4936 [VERSE]]
གཟུགས་དང་སྒྲ་དང་དེ་བཞིན་དྲི། །
རོ་དང་རེག་བྱ་ཉིད་དག་ལ། །
མིག་ལ་སོགས་པའི་འཇུག་པ་ནི། །
སྒྱུ་མ་བཞིན་དུ་མཚོན་པར་བྱ། །

[Block 4937 [VERSE]]
འདིར་ནི་མང་པོ་སྨོས་ཅི་དགོས། །
རྡོ་རྗེ་ཐེག་པར་དེ་ཉིད་ལ། །
གང་ཡང་རྣལ་འབྱོར་པས་དམིགས་པའི།
དེ་དེ་སྒྱུ་མ་བཞིན་གཞན་མིན། །

[Block 4938]
ཞེས་འབྱུང་ངོ་། །ཡུལ་རྣམས་ལ་ཉེ་བར་ལོངས་སྤྱོད་པ་ཞེས་པ་ནི་སོ་སོར་སྡུད་པའི་རིམ་པས་གཟུང༌[^2926]སྟེ། བསམ་གཏན་གྱི་རིམ་པས་རྣམ་པར་དག་པ་ཐོབ་པ་གང་ཡིན་པའོ། །

[Block 4939]
དབང་པོ་ལྔ་རྣམས་སོ་ཞེས་པ་ནི་མིག་ལ་སོགས་པའོ། །

[Block 4940]
དེ་རྣམས་ཀྱིས་བརྒྱན་པ་ཞེས་པ་ལ་སྒྱུ་མ་ལྟ་བུའི་དབང་པོ་དང་ལྡན་པ་ཡིན་གྱི། ཁྲག་དང་ཤ༌[^2927]ལ་སོགས་པའི་རང་བཞིན་ནི་མ་ཡིན་ནོ། །
--- END BLOCKS ---
