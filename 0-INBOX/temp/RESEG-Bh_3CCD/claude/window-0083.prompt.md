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
ཐམས་ཅད་མཁྱེན་པ་འདིར་བཞུགས་པས། ཞེས་པ་ནི་དཀྱིལ་འཁོར་གྱི་བདག་པོ་ཉིད་དུ་རྡོ་རྗེ་འཆང་ཆེན་པོ་བཞུགས༌[^1902]པས་སོ། །

[Block 2907]
དམ་ཆོས་བསྟན་པའི་ཐོག་མར་ནི། །ཞེས་བྱ་བ་ལ་སོགས་པས་རྟག་པའི་གནས་ཐོབ་པར་འདོད་པས་དང་པོ་བསྟན་བཅོས་ཀྱི་ཐོག་མར་ཨེ་ཝཾ་ཞེས་བྱ་བ་སྦྱར་བར་བྱ་བ་དང་། བསྟན་བཅོས་ཀྱི་བཀུར་སྟི་བྱ་བ་དང་། ཡི་གེ་གཉིས་པོ་དྲན་པར་བྱའོ་ཞེས་བརྒྱ་བྱིན་ལ་འབོད༌[^1903]ཅིང་གདམས་པའོ། །

[Block 2908]
བདག་གིས་ཞེས་བྱ་བ་ལ་སོགས་པས་ལུང་ཚད་མ་ཉིད་བསྟན་ཏོ། །

[Block 2909]
བཤད་པའི་རྒྱུད་ལས་ཞེས་པ་ནི་རྡོ་རྗེ་ཕྲེང་བ་ལས་སོ། །

[Block 2910]
འཁོར་ལོས་སྒྱུར་བའི༌[^1904]ངོ་བོའོ། །

[Block 2911]
[^1905]ཞེས་པ་ནི་དབུས་ཀྱི༌[^1906]བདག་པོའི་ཚུལ་གྱིས་སོ། །

[Block 2912]
བདག་གིས་ཐོས་པ་ཞེས་གསུངས་པའི་ཐོས་ཞེས་བྱ་བའི་དོན་བཤད་པར་བྱ་སྟེ། ས་བོན་ངོ་བོས་གང་སྤྲུལ་པ། །ཞེས་པ་ནི་རྡོ་རྗེ་རྩེ་མོ་ལས་འཕྲོས་པའི་བྱང་ཆུབ་ཀྱི་སེམས་ལས་སྐྱེ་བའོ། །

[Block 2913]
ལྷ༌[^1907]རྣམས་ཀྱི་ནི་འཁོར་ལོ་མཆོག །ཅེས་པ་ནི་མི་བསྐྱོད་པ་ལ་སོགས་པ་ལྷ་སུམ་ཅུ་རྩ་གཉིས་ཀྱི་བདག་ཉིད་དཀྱིལ་འཁོར་གྱི་འཁོར་ལོའོ། །

[Block 2914]
དུས་བཤད་པར་བྱ་སྟེ།

[Block 2915 [VERSE]]
མཆོག་ཏུ་དགའ་བའི་དུས་གང་ཡིན། །
དུས་གཅིག་ན་ཞེས་བཤད་པ་ཡིན། །

[Block 2916]
ཞེས་པ་ནི་སྙོམས་པར་ཞུགས་པའི་དུས་སུ་བདེ་བ་ཆེན་པོ་མྱོང་ནས་ཕྱིས་དཀྱིལ་འཁོར་གྱི་འཁོར་ལོ་སྤྲོ་བ་ཡིན་ནོ། །

[Block 2917]
དབུས་ཀྱི་བདག་པོའི་ཁྱད་པར་བསྟན་པར་བྱ་བའི་ཕྱིར། དབང་ཕྱུག་བརྒྱད་ཀྱིས་བཅོམ་ལྡན་འདས། །ཞེས་བྱ་བ་སྨོས་ཏེ། དབང་ཕྱུག་བརྒྱད་ནི་སྐུའི་དབང་ཕྱུག་ལ་སོགས་པའམ་ཕྲ་བ་ལ་སོགས་པ་སྔོན་དུ་བཤད་ཟིན་ཏོ། །

[Block 2918]
བདེ་བ་ཆེན་པོ་ནི་བདེ་བ་ཆེན་པོ་རྒྱུ་མཐུན་པར་གྱུར་པ་བྱང་ཆུབ་ཀྱི་སེམས་ལས་སྐྱེས་པའི་དཀྱིལ་འཁོར་གྱི་འཁོར་ལོ་དེ་ཉིད་གནས་ཞེས་པ༌[^1908]ནི་བཞུགས་གནས་ཏེ་གཞིའི་དཀྱིལ་འཁོར་རོ། །

[Block 2919]
དེར་བཞུགས་པ་ནི་དེར་བདག་པོ་ཉིད་དུ་བཞུགས་སོ། །

[Block 2920]
འདི་ནི་ཕུང་པོ་ལྔ་རྒྱལ་བ། །ཞེས་བྱ་བ་ལ་སོགས་པ་ཕུང་པོ་ལྔ་དང་སྐུ་གསུང་ཐུགས་ཀྱི་བདག་ཉིད་རྡོ་རྗེ་འཆང་ཆེན་པོ་ཁོ་ན་བཞུགས་སོ། །

[Block 2921]
དེ་ཙམ་གྱིས་ནི་དཀྱིལ་འཁོར་རྒྱལ་བ་མཆོག་གི་ཏིང་ངེ་འཛིན་བཤད་དོ། །

[Block 2922]
བཙུན་མོ་ཞེས་བྱ་བ་ལ་སོགས་པ་རྣམས་ནི་རེག་བྱ་རྡོ་རྗེ་མའོ། །

[Block 2923]
བྷ་ག་ལེགས་སྦྱངས་ཞེས་པ་ནི་དེའི་པདྨའོ། །

[Block 2924]
བཞུགས་པ་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་ཕྲ་མོའི་རྣལ་འབྱོར་ལ་སོགས་པ་བྱས་ནས། དཀྱིལ་འཁོར་གྱི་འཁོར་ལོ་ཉེ་བར་བསྡུས་ལ། སྐུ་དང་གསུང་དང་ཐུགས་ཀྱི་མཚན་ཉིད་ཡི་གེ་གསུམ་པོ་ཙམ་ལ་དམིགས་ཏེ། དེ་ཡང་ཆ་ཤས་ཀྱི་དབྱེ་བས་བསྡུས་ཏེ་ཐིག་ལེ་ཙམ་ལ་དམིགས་ཤིང་གནས་པར་བྱའོ། །

[Block 2925]
དེ་བས་ན་འདིར་བཤད་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་ཆ་གཉིས་པ་ནི་ཡི་གེ་ཨའོ། །

[Block 2926]
དགུ་པ་ནི་མ་ནིང་གི་ཡི་གེ་སྤངས་ཏེ་ཨོའོ། །

[Block 2927]
སུམ་ཅུ༌[^1909]པ་ལྔ་པའི་ས་བོན་ནི་ཧའོ།[^1910] །

[Block 2928]
ཆ་གཉིས་ནི་ཚེག་དྲག་གོ། །

[Block 2929]
ལྔ་པ་ནི༌[^1911]མའོ། །

[Block 2930]
དེ་ཉིད་རྗེས་དབྱངས་སོ། །

[Block 2931]
དྲུག་པ་ནི་ཨུའོ། །

[Block 2932]
ཐིག་ལེ་ནི་རྗེས་དབྱངས་སོ། །

[Block 2933]
དེ་ལྟར་ཨོཾ་ཨཱཿཧཱུཾ་འབྱུང་ངོ་། །སྐུ་གསུང་ཐུགས་ཀྱི་དཀྱིལ་འཁོར་ཉེ་བར་བསྡུས་ཏེ་གནས་པར་བྱའོ། །

[Block 2934]
ཡང་ན་ཡི་གེ་ཨ་དགག་པར་བྱེད་པ་སྦྲེལ་ཏེ། ཐིག་ལེ་ཙམ་དུ་དམིགས་ཏེ་གནས་པར་བྱའོ། །

[Block 2935]
དེའི་བསྡུས་པའི་དོན་ནི་འདི་ཡིན་ཏེ། ཡི་གེའི་དོན་གྱི་ཕྱོགས་སུ་དང་པོ་སྦྱོར་བའི་ཏིང་ངེ་འཛིན་གྱིས་དབུས་ཀྱི་བདག་པོར་གྱུར་ནས་སྨེ་ཤ་ཅན་ལ་སོགས་པའི་རིགས་སུ་སྐྱེས་པའི་དམ་ཚིག་གི་ཕྱག་རྒྱ་བླངས་ཏེ། ཡེ་ཤེས་སེམས་དཔའི་ས་བོན་གྱི་ཐིག་ལེ་ལས་བྱུང་བའི་འོད་ཟེར་གྱི་འཁོར་ལོ་སྣའི་བུག་པ་གཡས་པ་ནས་འབྱུང་བས་དེའི་ལུས་པོ་བསྲེག་པར་བྱ་སྟེ། དེའི་རྣམ་པར་ཤེས་པ་དྲི་མ་མེད་པ་རླུང་གིས་མ་བསྐྱོད་པའི་མར་མེ་ལྟ་བུ་དེ་ཉིད་ལྕགས་ཀྱུའི་རྣམ་པས་རྣམ་པར་བཅིངས་ཏེ་བཀུག་ལ་སྣའི་བུག་པ་གཡོན་པ༌[^1912]ནས་བཅུག་ལ་འདོད་པའི་གདུགས་ཞེས་བྱ་བའི༌[^1913]ལམ་ནས་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་གཟུགས་སུ་རྣམ་པར་སྤྲོས་ཏེ། རེག་བྱ་རྡོ་རྗེ་མའི་ཆོས་འབྱུང༌[^1914]པདྨ་དང་ཟླ་བའི་གདན་གྱི༌[^1915]སྟེང་དུ་དེ་དང་འདྲ་བའི་སེམས་མ་གསུམ་གྱི་བདག་ཉིད་བསྐྱེད་པར་བྱས་ལ། ཤིན་ཏུ་རྣལ་འབྱོར་དང་རྣལ་འབྱོར་ཆེན་པོའི་རིམ་པས་ལྷ་མོ་ཐམས་ཅད་ཀྱི་ངོ་བོར་བྱས་ལ་ཕྱིར་སྤྲོས་ཏེ། འཁྱུད་པའི་རེག་བྱ་རྡོ་རྗེ་མ་དང་གཉིས་སུ་མེད་པར་བྱས་ལ་རྡོ་རྗེ་དང་པདྨ་སྦྱར་བ༌[^1916]སྔོན་དུ་འགྲོ་བའི་རིན་ཆེན་འབྱུང་ལྡན་དང་དོན་ཡོད་གྲུབ་པའི་སྔགས་དག་གིས་སྙོམས་པར་ཞུགས་ཏེ་བསྐྱེད་པར༌[^1917]བྱས་ལ། རྗེས་སུ་ཆགས་པ་དམ་པའི་སྒྲས་ནམ་མཁའི་དབྱིངས་ཀུན་དུ་གནས་པའི་དེ་བཞིན་གཤེགས་པའི་ཚོགས་བཀུག༌[^1918]ཅིང་འཇུག་པར་བྱས་ལ། སྔ་མ་བཞིན་དུ་དབུས་མའི་ལམ་ནས་ཐིག་ལེའི་གཟུགས་སུ་དམིགས་ཏེ། བཛྲ་དྷྲྀཀ་ཅེས་བྱ་བ་ལ་སོགས་པ་ཕྱུང་བའི་སྔགས་ཀྱིས་མི་བསྐྱོད་པ་ནས་བརྩམས་ཏེ། སྒོ་སྐྱོང་གི་བར་དུ་དཀྱིལ་འཁོར་གྱི་འཁོར་ལོ་དེ་ཉིད་དུ་སྤྲོས་ཏེ། སེམས་དཔའ་གསུམ་གྱི་བདག་ཉིད་དུ་བྱས་ནས་སླར་ཡང་རྣམ་པར་སྤྲོས་ཏེ། སེམས་ཅན་གྱི་དོན་བྱས་ནས་སླར་ཡང་གཤེགས་ཏེ་ཤར་ལ་སོགས་པའི་ཕྱོགས་རྣམས༌[^1919]སུ་རྣམ་པར་དགོད་ཅིང་དབང་བསྐུར་བ་དང་ཕྱག་རྒྱ་གདབ་པར་བསམས་ཏེ། ཕྲ་མོའི་རྣལ་འབྱོར་དང་བཟླས་པ་བྱས་ནས་བྱ་བ་བྱས་པའི་ཕྱིར་རྣམ་པར་ཞུ་བ་ལྷ་མོའི་གླུས་བསྐུལ་བས་བཞེངས་ཏེ། དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱིས་བསྟོད་པ་གསན་ནས་ཚིམ་པར་བྱེད་པའི་ཆོ་ག་ལ་སོགས་པ་རྫོགས་ནས་ཕྱིའི་དཀྱིལ་འཁོར་ལུས་ཀྱི་དཀྱིལ་འཁོར་དུ་བཅུག་ལ། ཡི་གེ་གསུམ་གྱི་བདག་ཉིད་དུ་གྱུར་ནས་དེ་ཡང་ཡོངས་སུ་གྱུར་ཅིང་བདེ་བ་ཆེན་པོའི་རང་བཞིན་ཐིག་ལེ༌[^1920]ཙམ་དུ་མཐར་ཐུག་ལ་རྡོ་རྗེ་འཛིན་པར་འགྱུར་རོ་ཞེས་བྱའོ། །

[Block 2936]
སྤྱིའི་དོན་ཞེས་བྱ་བ་ནི་བསྐྱེད་པའི་རིམ་པས་སོ་ཞེས་ཚིག་གི་ལྷག་མའོ། །

[Block 2937 [HEADING]]
##### ཡེ་ཤེས་གསུམ་པོ་རྣམ་པར་དཔྱོད་པའི་མཚན་ཉིད་ཅན་སྦས་པའི་དོན། ^1-8-1-1-0

[Block 2938]
ཡང་ལུང་གིས་བཤད་པ་ཞེས་བྱ་བ་འདིས་ལུང་ཚད་མ་ལས་སྦས་པའི་དོན་བཤད་པར་བྱ་བའི་ཕྱིར། ཨེ།

[Block 2939 [VERSE]]
[^1921]ཨེ་ནི་ཤེས་རབ་དམ་པ་སྟེ། །
འདོད་ཆགས་བྲལ་སོགས་སྐད་ཅིག་བདག །
སྲིད་པ་གསུམ་ན་ཡོངས་ཤེས་པ། །
འདི་ནི་རྩ་བར་རྣམ་པར་བསྟན། །

[Block 2940]
ཞེས་སྨོས་ཏེ། [^1922]འདིར་དང་པོ་ཡེ་ཤེས་གསུམ་པོ་རྣམ་པར་དཔྱད་པའི་མཚན་ཉིད་ཅན་སྦས་པའི་དོན་བཤད་པར་བྱ་སྟེ། སེམས་རྣམ་པར་དག་པར༌[^1923]བྱེད་པར་འདོད་པའི་རྣལ་འབྱོར་པས་དང་པོ་སྔགས་སམ་ཕྱག་རྒྱའི་རིམ་པ་ལ་དམིགས་པར་བྱའོ། །

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
--- END BLOCKS ---
