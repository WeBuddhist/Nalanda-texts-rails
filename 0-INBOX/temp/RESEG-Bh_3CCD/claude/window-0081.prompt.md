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
[Block 2836]
སྨྲས་པ་གལ་ཏེ་དེ་ལྟ་ན་ནི་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་སྡུད་པ་པོ་ཡོད་པར་མི་འགྱུར་ཏེ་ཞེས་བསྟན་ཏོ། །

[Block 2837]
སྡུད་པ་པོ་མེད་ཅེས་དམ་བཅའ་བའོ། །

[Block 2838]
འབྲེལ་པ་མེད་པའི་ཕྱིར་ཞེས་གཏན་ཚིགས་སོ། །

[Block 2839]
དགོངས་པ་ནི་འདི་སྐད་བདག་གིས་ཐོས་པ་འདིས་ཐབས་དང་ཤེས་རབ་མཚོན་པར་བྱེད་པས་བདག་གིས་ཐོས་པ་ཞེས་བྱ་བ་ལ་སོགས་པའི་བྱེད་པ་པོ་དང་བྱ་བ་ལ་སོགས་པའི༌[^1857]རྣམ་གྲངས་ཅན་གྱི་ལས་མེད་པས་འབྲེལ་པ་མེད་དོ། །

[Block 2840]
དེ་བས་ན་བདག་གིས་ཐོས་ཞེས་སྡུད་པར་བྱེད་པ་པོ་མེད་པར་ཐལ་བར་འགྱུར་རོ། །

[Block 2841]
རྒྱུད་ཀྱི་དོན་ཡང་མཆོག་ཏུ་འཛིན་པར་མི་འགྱུར་རོ་ཞེས་དྲིའོ། །

[Block 2842]
དེ་ནི་བདེན་ཏེ་སྨྲས་པ་ཞེས་པ་ནི་བདེན་ཏེ་ཞེས་པ་འདིས་ལན་ནོ། །

[Block 2843]
འདིར་སྡུད་པར་བྱེད་པ་པོ་ནི་མེད་དོ་ཞེས་པ་ནི་རྡོ་རྗེ་འཆང་ཆེན་པོ་ཉིད་ལོངས་སྤྱོད་དང་སྤྲུལ་པའི་སྐུ་ཉིད་ཀྱིས་འཆད་པ་པོ་ཡང་ཡིན་ལ༌[^1858]ཉན་པ་པོ་ཡང་ཡིན་ནོ། །

[Block 2844]
གང་གི་ཕྱིར་ཐམས་ཅད་སྟོང་པའི་ངོ་བོ་ཉིད་རྡོ་རྗེ་འཆང་ཆེན་པོ་ཟུང་དུ་འཇུག་པའི་ཏིང་ངེ་འཛིན་ལས་མི་གཡོ་བ་དེ་དང་ཐ་མི་དད་པའི་སྤྲུལ་པ་ཕྱག་ན་རྡོ་རྗེ་ལ་སོགས་པ་སྡུད་པ་པོ་རྣམས་ལ་ཐེ་ཚོམ་མེད་ན། གང་བཟློག་པར་བྱ་བའི་ཕྱིར་དེ་རྣམས་ལ་རྡོ་རྗེ་འཆང་ཆེན་པོས་ཆོས་བསྟན་པ་དང་དེ་རྣམས་ཀྱིས་ཀྱང་དེ་ལས་ཐོས་ནས་གཞན་རྣམས་ལ་སོ་སོར་བསྟན་པར་འགྱུར་རོ། །

[Block 2845]
དེ་བས་ན་མ་འོངས་པའི་སེམས་ཅན་གྱི་ཁམས་གདོན་པར་བྱེད་པའི་བསམ་པས་སྣ་ཚོགས་པ་སངས་རྒྱས་ཀྱི་རོལ་སྟོན་འདི་བསྟན་ཏོ་ཞེས་འཆད་པ་པོ༌[^1859]དང་ཉན་པ་པོ་ཐ་དད་པ་གང་ཞིག་ཡོད། དེའི་ཕྱིར་སྤྲོས་པ་མེད་པ་རྡོ་རྗེ་འཆང་ཆེན་པོ་གཅིག་པུ་ཉིད་རྡོ་རྗེ་འཆང་ཆེན་པོས་དབང་དུ་བྱས་པའི་ཐུགས་ཀྱི་རྒྱུད་ཀྱི༌[^1860]འཆད་པ་པོ་དང་། ཉན་པ་པོ་དང་སྡུད་པ་པོའི་དབྱེ་བས་བདག་ཉིད་ཁོ་ན་རབ་ཏུ་སྟོན་པར་མཛད་དོ། །

[Block 2846]
དེ་ལྟ་ན་སྨྲས་པ་ནི་འོ་ན་བཙུན་པ་ཀུན་དགའ་བོ་ཞེས༌[^1861]བྱ་བ་ལ་སོགས་པས་སླར་ཡང་འདྲི་བའོ། །

[Block 2847]
དེའི་བསམ་པ་ནི་འཕགས་པ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལས་བཙུན་པ་ཀུན་དགའ་བོ་ནི་སྡུད་པ་པོ་སྟེ། དེ་བཞིན་དུ་ཡང་མདོ་སྡེ་དང་རྒྱུད་ཀྱི་རྒྱལ་པོ་གཞན་རྣམས་ལ་ཡང་འོད་སྲུངས༌[^1862]དང་མཽད་གལ་གྱི་བུ་ལ་སོགས་པ་སྡུད་པ་པོ་ཡོད་ཅེས་ཅིའི་ཕྱིར་འདིར༌[^1863]སྡུད་པ་པོ་མེད་ཅེས་སྨྲས་ཤེ་ན། སྨྲས་པ་ཞེས་བྱ་བ་ལ་སོགས་པས་ལན་ཡིན་ཏེ། ཀུན་དགའ་བོ་ནི་འདིར་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཀུན་ཏུ་བཟང་པོ་སྟེ་ཞེས་པ་ནི་ཉན་ཐོས་ཀྱི་སྡེ་སྣོད་རྣམས་ལ་གང་བཙུན་པ་ཀུན་དགའ་བོ་སྡུད་པ་པོ་ཡིན་པ་དེ་ཉིད་སྔགས་ཀྱི་བསྟན་པ་འདི་ལ་ཀུན་ཏུ་བཟང་པོ་ཞེས་བྱའོ། །

[Block 2848]
སྔགས་ཀྱི་ཐེག་པ་ལ་སྡུད་པ་པོ་ཕྱག་ན་རྡོ་རྗེ་གང་ཡིན་པ་དེ་ཉིད་རྡོ་རྗེ་འཆང་ཆེན་པོ་ཉིད་དེ། ལོངས་སྤྱོད་དང་སྤྲུལ་པའི་སྐུ་དག་ནི་དབྱེར་མེད་པའི་ཕྱིར་རོ། །

[Block 2849]
གཞན་དུ་ན་ཞེས་བྱ་བ་ལ་སོགས་པས་དེ་དག་དབྱེར་མེད་པ་ལ་ཚད་མ་ཉིད་གསུངས་སོ། །

[Block 2850]
ཆོས་ཀྱི་ཕུང་པོ་བརྒྱད་ཁྲི་བཞི་སྟོང་ཞེས་པ་ནི་ཉན་ཐོས་ཀྱི་སྡེ་སྣོད་ཀྱི་ཚད་དོ། །

[Block 2851]
ཉེ་བར་མཚོན་པ་ཡིན་པས་ཐེག་པ་ཆེན་པོ༌[^1864]ནི་སྟོང་ཕྲག་དགུ་བཅུ་རྡོ་རྗེ་ཐེག་པ་ཡང་ཞེས་པ་ནི་ཡང་གི་སྒྲས་ནི༌[^1865]ཁྲི་ཕྲག་བཅུའི་ཚད༌[^1866]ཅན་ནོ། །

[Block 2852]
ལྷག་ཆད་མེད་པར་ལན་ཅིག་གིས་འཛིན་པར་ག་ལ་ནུས་ཞེས་པ་ནི་མི་ནུས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2853]
དེ་བས་ན་རྡོ་རྗེ་འཆང་ཆེན་པོ་ཁོ་ནའོ། །

[Block 2854]
བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་ཞེས་པ་ལ་སོགས་པས་ལུང་ཚད་མ་ཉིད་དུ་བསྟན་པ་ཡིན་ཏེ། འདི་ལྟ་སྟེ། འཇམ་དཔལ་ནི་རྒྱལ་པོ་ཆེན་པོ༌[^1867]ཟས་གཙང་མར་གྱུར་ཏོ་ཞེས་པ་ནི། ཟས་གཙང་མ་ནི་བཅོམ་ལྡན་འདས་ཀྱི༌[^1868]ཡབ་སྟེ་རྒྱུའི་རྡོ་རྗེ་འཆང་བའོ། །

[Block 2855]
འཇམ་དཔལ་ནི་རྒྱལ་བའི་སྲས་ཏེ་སྤྲུལ་པའི་སྐུའོ། །

[Block 2856]
དེ་དག་ཐ་མི་དད་པ་ཡིན་ཏེ། མཛད་པ་གཅིག་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2857]
འཇིག་རྟེན་དབང་ཕྱུག་ནི་ལྷ་མོ་ཆེན་མོ་སྒྱུ་འཕྲུལ་དུ་གྱུར་ཏོ་ཞེས་པ་ནི་འདིས་ཀྱང་བུད་མེད་དང་སྐྱེས་པ་དབྱེར་མེད་པར་སྒྱུ་མ་ལྟ་བུར་མཐོང་བས་དངོས་པོ་ཐམས་ཅད་ལ་གཉིས་སུ་མེད་པའི་མཚན་ཉིད་བསྟན་ཏོ། །

[Block 2858]
དཔལ་ལྷ་མོ་ནི་གྲགས་འཛིན་ནོ་ཞེས་པ་ནི་བཅོམ་ལྡན་འདས་ཀྱི་བཙུན་མོ་དམ་པའོ། །

[Block 2859]
དེ་ཉིད་དཔལ་གྱི་ལྷ་མོ་ནི་རེག་བྱ་རྡོ་རྗེ་མའོ། །

[Block 2860]
རྡོ་རྗེ་སེམས་དཔའ་ནི་སྒྲ་གཅན་འཛིན་ནོ་ཞེས་པ་ནི་ཤཱཀྱ་སེང་གེའི་སྲས་ཏེ་སྤྲུལ་པའི་སྐུའོ། །

[Block 2861]
རྡོ་རྗེ་སེམས་དཔའ་ནི་ལོངས་སྤྱོད་རྫོགས་པའི་སྐུའོ་ཞེས་དེ་དག་དབྱེར་མེད་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 2862]
དེ་བཞིན་དུ་ཐམས་ཅད་དུ༌[^1869]ཤེས་པར་བྱའོ། །

[Block 2863]
རིགས་པ་འདིས་ནི༌[^1870]ཞེས་བྱ་བ་ལ་བརྩོན་པས་ཉེ་བར་སྡུད་པ་བསྟན་ཏོ། །

[Block 2864]
འདིར།[^1871] སངས་རྒྱས་མྱ་ངན་མི་འདའ་ཞིང་། །ཞེས་པ་ནི་རྡོ་རྗེའི་སྐུ་ཉིད་ཀྱིས་མི་ཟད་པའི་ཕྱིར་རོ། །

[Block 2865]
ཆོས་ཀྱང་ནུབ་པར་མི་འགྱུར་ཏེ། །ཞེས་པ་ནི་སངས་རྒྱས་ཀྱིས་བྱིན་གྱིས་རློབ་པ༌[^1872]དེ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2866]
སེམས་ཅན་རྣམས་ནི་གདུལ་བྱའི་ཕྱིར། །ཞེས་པ༌[^1873]ནི་མ་འོངས་པའི༌[^1874]སེམས་ཅན་སྦྱོར་བའི༌[^1875]ཕྱིར་རོ། །

[Block 2867]
མྱ་ངན་ལས་འདས་པ་ནི་ཡོངས་སུ་མྱ་ངན༌[^1876]འདས་པ་དང་ནུབ་པ་ཡང་ཉེ་བར་བསྟན་ཏོ། །

[Block 2868]
དེ་ལྟར་སྡུད་པ༌[^1877]པོ་རྣམས་དང་དབྱེར་མེད་པ་ཉིད་དུ་བསྟན་ནས། གླེང་གཞིའི་ཚིག་རབ་ཏུ་བསྟན་པར་བྱ་བའི་ཕྱིར། འདི་སྐད་ཅེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2869]
བཅོམ་ལྡན་འདས་ཞེས་བྱ་བ་ལ་སོགས་པས་ལུང་ཚད་མ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 2870]
བརྒྱ་བྱིན་གྱིས་གསོལ་པ་ནི་དྲི་བའོ། །

[Block 2871]
དྲི་བ་དེ་ཉིད་ཅིའི་ཕྱིར་ཞེས་བྱ་བ་ལ་སོགས་པས་བསྟན་ཏེ། འདིར་ནི་སྐད་ཀྱི༌[^1878]ཡི་གེའི་དོན་གང་ཡིན་པ་དང་ཅིའི་སླད་དུ་དང་པོ་སྦྱོར་བ་དང་སངས་རྒྱས་ཀྱིས་གསུངས་པའམ་ཉན་ཐོས་ཀྱིས་གསུངས་སམ་ཞེས་འདྲི་བའོ། །

[Block 2872]
དམ་ཆོས་ཡོན་ཏན་སྨྲ་བ་ཡི། །ཞེས་བྱ་བ་ལ་སོགས་པས་ལན་གསུངས་སོ། །

[Block 2873]
དྲི་བ་མཆོག་ཡིན་པའི་ཕྱིར་ལེགས་སོ་ཞེས་བྱ་བ་བྱིན་པའོ། །

[Block 2874]
གང་ཕྱིར་ཐམས་ཅད་གཟིགས་པ་ཞེས་བྱ་བ་ལ་སོགས་པས་དང་པོར་སྦྱོར་བའི་དྲི་བའི་ལན་ནོ། །

[Block 2875]
གང་གི་ཕྱིར་གྱིས་ནི་དོན་གང་ཡིན་ཞེས་དྲི་བའི་ལན་ནོ། །
--- END BLOCKS ---
