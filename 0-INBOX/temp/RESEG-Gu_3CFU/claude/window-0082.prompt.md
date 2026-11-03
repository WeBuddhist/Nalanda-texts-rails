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
[Block 2871]
ཤུགས་ཀྱི་གནས་སྐབས་སུ་བཏང་ན་རྫོགས་པར་མ་བྱས་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་དེ་མ་ཐག་པར་འཕོ་བཞིན་པ་ནི་འཕོ་བ་སྟེ་ལུས་ཀྱི་བྱ་བ་བཏང་བ་ནི་སྤོང་བའོ། །

[Block 2872]
ཤུགས་ཀྱི་གནས་སྐབས་སུ་སྤོང་བ་ཡོད་པར་འགྱུར་བ་ལ་སྦྱོར་བ་སྔ་མའི་དབང་གིས་རྫོགས་པ་གང་ཡིན་པ་ནི་ཁུ་བ་ཕྱུང་བ་སྟེ། དེ་ལ་མ་བྱས་པ་ཉིད་ནི་སྦོམ་པོའི་ལྟུང་བ་ཉིད་དོ། །

[Block 2873]
དེ་བཞིན་དུ་དེར་སྦྱར་བ༌[^1972]ཉིད་ཀྱི་ཕྱིར་དགེ་འདུན་ལྷག་མ་ནི༌[^1973]མ་ཡིན་ནོ། །

[Block 2874]
དངོས་གཞི་བསྐྱེད་པ་ཡང་འདི་ལྟར་མཐོང་སྟེ། དཔེར་ན་འདིར་སྲོག་གཅོད་པ་ལ་བརྟེན་པ་ནི་དེ་ལ་ནི་གྲོལ་བ་མ་ཡིན་ཏེ་སྲོག་གཅོད་པ་ལ༌[^1974]ནི་སྲོག་ཆགས་རྣམས་ལ་རྣམ་པར་ལྟུང་བ་ཡིན་ཏེ། དེ་བས་ན་དེ་བཞིན་དུ་འདིར་སྤོང་བ་རྫོགས་པ་ལ་བྱས་པ་ཉིད་ཅེས་བྱ་བ་དེའི་ཕྱིར་འདི་རྣམ་པར་ཤེས་པའོ། །

[Block 2875]
འདིར་གཞུང་ནི་ཤུགས་བཏང་སྟེ། ཁུ་བ་ཕྱུང་ན་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2876]
ཡིད་ཀྱིས་ཀྱང་སྤོང་བ་ལ་ཚིག་འདི་གནས་པ་ཡིན་ཏེ། འཁྲུལ་པ༌[^1975]མེད་པའི་དོན་དུ་རྣམ་པ་ཐམས་ཅད་ཀྱིས་སྦྱོར་བའོ། །

[Block 2877]
དེ་བས་ན་གཞན་ལ་མེད་པའི་དབང་དུ་བྱས་ནས་འདི་བྱས་པའོ། །

[Block 2878]
འདིར་ཉེ་བར་བསྡུ་བ་ནི་སྤང་བའོ། །

[Block 2879]
དེ་མ་ཐག་ཏུ་འཕོ་བཞིན་པའི་གནས་སྐབས་ལ་ལུས་ཀྱི་བྱ་བ་བཟློག་པ་ལ་སྦྱོར་བ་སྔ་མའི་དབང་གིས་ཕྱུང་བ་གང་ཡིན་པ་དེ་རོ་མྱང་བ་ལ་སྦོམ་པོའོ། །

[Block 2880]
མ་མྱངས་པ་ལ་ནི་ལྟུང་བ་མེད་དོ། །

[Block 2881]
གར་བྱེད་པ་དང་རབ་ཏུ་གར་བྱེད་པ་གཉིས་ལ་ནི་ན༌[^1976]སྨད་པ་ཉིད་དོ། །

[Block 2882]
ནམ་མཁའ་ལ་རྐེད་པ༌[^1977]བསྐྱོད༌[^1978]པའོ། །

[Block 2883]
ཕྱོགས་གཞན་དུ་རེག་པའོ། །

[Block 2884]
རྒྱུན་ལས་བཟློག་པའི་ཕྱོགས་སུ་གཏོད་པའོ། །

[Block 2885]
རྫི་ཕྱོགས་མ་ཡིན་པར་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཡན་ལག་གི་ཚོགས་ལ་རེག་པ་སེམས་ཅན་དུ་བགྲང་བས་ཕྱི་རོལ་པས་ཀྱང་གནས་པའི་དེའི་རྣམ་པ་ཞེས་བྱ་བ་གནས་འདི་ལ་གར་བྱེད་པ་ལ་སོགས་པ་རྣམས་བཟུང་བའོ། །

[Block 2886]
སྦྱོར་བ་འདི་རྣམས་ལ་ན༌[^1979]སྨད་པ་ཉིད་དོ། །

[Block 2887]
དེ་ལ་ནི་ཕྱུང་བ་དང་འདུན་པ་དང་རང་གི་ཁུ་བ་དང་པོ་ཞེས་བྱ་བ་འདི་རྣམས་ལ་འདིར་དངོས་གཞིའི་ཆོ་ག་ལ་སོན་པའི་ཡན་ལག་རྣམས་དང་འབྲེལ་ལོ། །

[Block 2888]
ཡན་ལག་གི་ཚོགས་ལས་ཕྱོགས་གཞན་པར་བྱའོ། །

[Block 2889]
བརླ་དང་གོས་དང་གཞན་གྱིས་རེག་པ་དང་། གཡན་པ་ཕྲུག་པ་དག་གིས་བབ་ཅོལ་དུ་དེའི་དོན་མ་ཡིན་པར་ཞུགས་པ་ལ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ལ། དེའི་དོན་མ་ཡིན་པ་ནི་མི་འབྱིན་པའི་དོན་དུ་རྒྱུག༌[^1980]ཅིང་འགྲོ་བ་ལ། ཀུན་ནས་འགྲོ་བ་དང་། རྒོད་བག་དང་། མཆོང་བ་ལ་སོགས་པའི་དོན་དུ་འཇུག་པ་ལ་བརླ་དང་གོས་ཀྱིས་རེག་པའོ། །

[Block 2890]
ཤུ་བ་དང་ཁྱི་རྔོ་དང་འབྲུམ་བུ་དང་། གཡན་པ་ཕྲུག་པ་དང་། བལ་ལྡགས་ཀྱི་ཚོགས་དང་། མེ་དབལ༌[^1981]ལ་སོགས་པའི་སྡུག་བསྔལ་གསོ་བའི་དོན་དུ་གཡན་པ་འཕྲུག་པའི་རྐོ་སྤྱད་འགྲུབ་པའི་ལས་སོ་སོར་ཉམས་སུ་མྱོང་བའི་དོན་དུ་བསྐུལ་བའི་གཞན་དང་མིས་རེག་པས་བབ་ཅོལ་དུ་སྦྱོར་བ་ལ་སོགས་པ་མེད་པར་བཙན༌[^1982]ཐབས་ཀྱིས༌[^1983]བབ་ཅོལ་དུ་བྱུང་བའི་ཤུགས་ཀྱིས་རྐུ༌[^1984]བཞིན་པ་ལ་འབྱིན་པ་གང་ཡིན་པ་དེ་ལ་ཡོད་པ་ལ་ལྟུང་བ་མེད་པ༌[^1985]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2891]
བརླ་དང་གོས་དང་གཞན་གྱིས་རེག་པ་དག་ལ་འདིར་ཡན་ལག་གི་ཚོགས་ལ་སྦྱར་བའོ། །

[Block 2892]
གཞན་ལ་འདི་ལྟར་རེག་པར་བྱ་བ༌[^1986]ལ་མི་འགྲུབ་པའི་ཕྱིར་རེག་པ་དང་སྤྲུག་པ་དག་ལ་གཉིས་ཀ་ལ་ལུས་ཀྱི་ལས་ཀྱི་ཡན་ལག་གི་ཚོགས་ལ་ཡང་དག་པར་རེག་པས་བསྒྲུབ་པ་དང་འབྱིན་པར་འགྱུར་བ་ཡིན་ནོ། །

[Block 2893]
རེག་བྱ་མ་ཡིན་པ་ཉམས་སུ་མྱོང་ནའོ་ཞེས་བྱ་བ་ནི་རེག་བྱའི་ཡུལ་མ་གཏོགས་པ༌[^1987]གཟུགས་དང་སྒྲ་དང་དྲི་དང་རོ་རྣམས་ལ་གཟུགས་ཅན་གྱི་དབང་པོས་སོ་སོར་ཉམས་སུ་མྱོང་བ་ལ་དེའི་དོན་མ་ཡིན་པར་འཇུག་པ་ལ་བབ་ཅོལ་དུ་ཕྱུང་བ་ལ་ལྟུང་བ་མེད་དོ། །ཇི་ལྟར་ཡང་འདི་རྣམས་ལས་ཕྱུང་བ་དང་སྦྱར་བའོ་ཞེ་ན། དེའི་ཕྱིར་འདིར་གཞུང་ནི་དེ་ཉམས་སུ་མྱོང་བ་བཞིན་དུ་དེས་ཆུ་གཏོང་བ་ལ་རྣམ་པར་འགྱུར་བས་བསྒྲུབ་པས་སྣོད་མ་ཡིན་པ་ལས་ཆགས་པར་བྱ་བའི་གཟུགས་རྣམས་མཐོང་ནས་ཞེས་བྱ་བ་གསུངས་པ་ཡིན་ནོ། །

[Block 2894]
དྲན་པས་དེ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་རེག་པར་བྱ་བ་མ་ཡིན་པའི་སྒྲས་བརྗོད་པའི་ཡུལ་འདི་རྣམས་ལ་རེག་པར་བྱ་བ་དྲང་ཞིང་ཉམས་སུ་མྱོང་བ་ལ། དེའི་དོན་མ་ཡིན་པར་ཞུགས་པ་ལ་བབ་ཅོལ་དུ་བྱུང་བ་ལ་ལྟུང་བ་མེད་དོ། །

[Block 2895]
འདིར་དེའི་དོན་དུ་འཇུག་པ་ལ་བྱེ་བྲག་ངེས་པར་མྱོང་བའི་བདེ་བ་སོ་སོར་ཉམས་སུ་མྱོང་བར་ཉེ་བར་བསྒྲུབ་པའི་ཕྱིར་ཆོ་ག་འདིའོ། །

[Block 2896]
འདིའི་དོན་མ་ཡིན་པར་འཇུག་པ་ལ་ཡང་འདོད་པ་བཞིན་དུ་ཉེ་བར་ལྟུང་བ་རྗེས་སུ་ཆགས་པར་བྱ་བའི་གཟུགས་མཐོང་བ་ལ་སོགས་པས་འཇུག་པ་དེ་ལ་ཡང་དེའི་རྣམ་པར་ཉེས་བྱས་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 2897]
དེ་ལྟར་ཡང་བཅོམ་ལྡན་འདས་ཀྱིས་དེང་ཕྱིན་ཆད་མིག་གིས་མིག་ལ་བརྟེན་ཏེ་བུད་མེད་ཀྱི་ཚོགས་ལ་རྣམ་པར་བལྟ་བར་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2898]
དགེ་འདུན་གྱི་ལྷག་མ་དང་པོའི་རྣམ་པར་འབྱེད་པའོ།། །།

[Block 2899]
འཕོ་བར༌[^1988]འགྱུར་བ་དང་འཕོས་མ་ཐག་པ་ནི་ཤུགས་དང་སྦུབས་སུ་འོངས་པའོ་ཞེས་བྱ་བ་ལ། གང་ཞིག་ཤུགས་ཞེས་བྱ་བ་དེ་མ་ཐག་ཏུ་བརྗོད་པ་དེ་གནས་ལས་འཕོ་བར་འགྱུར་བ་ལ་རིག་པར་བྱའོ། །

[Block 2900]
གང་གི་ཕྱིར་འདིར་མ་ཞུགས་པ་ནི་ཞུགས་པ་ཞེས་བརྗོད་དོ། །

[Block 2901]
སྦུབས་སུ་འོངས་པའོ་ཞེས་བྱ་བ་སྨྲས་པ་གང་ཡིན་པ་དེ་ནི་དེ་མ་ཐག་ཏུ་གནས་ནས་འཕོ་བའོ། །

[Block 2902]
སྐད་ཅིག་མ་གཉིས་པ་ལ་གང་ལ་འཕོ་བ་དེ་ནི་འདིར་འཕོ་བར་གྱུར་པ་བརྗོད་པར་རིག་པར་བྱའོ། །

[Block 2903]
བརྩམས་པ་ཙམ་ན་སྦྱོར་བ་ཉིད་མ་ཡིན་པ་མ་ཡིན་ནོ། །

[Block 2904]
མདོ་འདི་ནི་ཤུགས་ཀྱི་གནས་སྐབས་ལ་སྦོམ་པོའི་ལྟུང་བ་བརྗོད་པའི་འོག་ཏུ་གང་ཞིག་ན་སྨད་པར་འདོད་པ་དེའི༌[^1989]བཟློག་པའི་དོན་དུའོ། །

[Block 2905]
དེ་ལྟར་ཡང་གསུངས་པས་དེས་བདུད་འཇོམས་ཤིང་སོ་སོར་སྡུད་པར་བྱེད་ན་ལྟུང་བ་ཅིར་འགྱུར། ཉེས་པ་སྦོམ་པོར་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2906]
འདིར་བྱས་པ༌[^1990]ལ་སྦྱར་བ་མ་བྱས་པ་ཉིད་ནི་མ་ཡིན་ཞེས་བྱ་བ་ནི་འདིའི་དོན་ཏོ། །

[Block 2907]
སྦྱོར་བ་མེད་པར་ཕྱུང་བ་ལ་རོ་མྱོང༌[^1991]བར་བྱེད་པ་ནི་དེ་དང་ལྡན་པ་ཉིད་དོ་ཞེས༌[^1992]བྱ་བ་དེ་དང་ལྡན་པ་ཉིད་ཅེས་བྱ་བ་ནི་སྦྱོར་བ་མ་ཡིན་པ་ཉིད་ནི་མ་ཡིན་ནོ། །

[Block 2908]
སྦྱོར་བ་མེད་པར་ཞེས་བྱ་བ་ནི་གཉིད་ལོག་པའི་གནས་སྐབས་ན་རྩོམ་པ་གང་ཡིན་པ་དང་འདབ་ཆགས་སུ་ཕྱུང་བ་གང་ཡིན་པ་སྦྱོར་བ་མེད་པར་གང་ཞིག་ཕྱུང་བ་ལ་རོ་མྱང་བ་ལ་སྦྱོར་བ་དེ་དང་ལྡན་པ་ཉིད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2909]
འདིར་གཞུང་ནི་ཉལ་བའི་བརྩལ་བ་ལ་དེ་སྐད་ཅེས་བྱ་སྟེ། གལ་ཏེ་རོ་མྱོང༌[^1993]བར་བྱེད་ན་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2910]
ཡན་ལག་གི་རྣམ་པ་ཅུང་ཟད་ཉེད་པ༌[^1994]དང་། ཡོངས་སུ་ཉེད་པ༌[^1995]དང་འཚིར་བའོ་ཞེས་བྱ་བ་ལ་དེ་དང་ལྡན་པ་ཉིད་ཅེས་བྱ་བར་སྦྱར་རོ། །
--- END BLOCKS ---
