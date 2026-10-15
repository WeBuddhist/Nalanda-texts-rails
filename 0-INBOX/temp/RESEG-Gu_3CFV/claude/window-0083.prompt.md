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
བསྙེན་པར་རྫོགས་པ་ཉིད་ལ༌[^1880]ཤིན་ཏུ་སྟོབས་དང་ལྡན་པ་ཉིད་མནན་པ་ལ་དགེ་སྦྱོང་དུ་མེད་པའི་ཆོས་དང་མཐུན་པ་ཉིད་གཤེ་བ་མཚང་འདྲུ་བ༌[^1881]ཞེས་བྱ་བ་ལ་བསྙེན་པར་རྫོགས་པ་ལ་འདི་བཀག་པའོ། །

[Block 2907]
སྐྱོན་ཅན་སྡུད་པ་ལས་གྱུར་པའི་ལྟུང་བྱེད་དུ་གཏོགས་པའོ། །

[Block 2908]
ཡལ་བར་འདོར་བ་ལས་གྱུར་པའི་ལྟུང་བ༌[^1882]བཞི་པོ་དག་ལས།

[Block 2909]
དེ་རྣམས་ཀྱི་དང་པོ་གང་ཡིན་ཞེ་ན། དེའི་ཕྱིར་རབ་ཏུ་ཕྱུང་བ་དང་བསྙེན་པར་རྫོགས་པར་བྱས་པ་དག་ལ༌[^1883]ཕན་མི་འདོགས་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། མཁན་མོ་ཉིད་ཀྱིས་ཞེས་བྱ་བ་ཐམས་ཅད་ཀྱི་དབང་དུ་བྱས་པར་རིག་པར་བྱའོ། །

[Block 2910]
རབ་ཏུ་བྱུང་བ་དང་བསྙེན་པར་རྫོགས་པར་བྱ་བ་དག་ལ་གདམས་ངག་ལ་སོགས་པས་ཡོངས་སུ་མི་སྐྱོང་ཞིང་། ཕན་མི་འདོགས་པ་དག་ལ་ལྟུང་བྱེད་དུ་འགྱུར་རོ། །

[Block 2911]
གང་ལ་བསླབ་པའི་གཞི་གཉིས་པར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་བར་ཆད་མཐོང་བ་ནི༌[^1884]མི་འདྲེན་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བདག་པོ་ལ་སོགས་པ་དག་གིས་བར་ཆད་དུ་འགྱུར་བ་མཐོང་ན་རབ་ཏུ་བྱུང་བ་དང་། བསྙེན་པར་རྫོགས་པ་དག་བར་ཆད་ཀྱི་གནས་དེ་ལས་མི་འདྲེན་ཏམ།[^1885] དེ་ཉིད་དུ་འཇིགས་པ་མེད་པའི་གནས་སུ་མི་འདྲེན་ན་ལྟུང་བྱེད་དོ། །

[Block 2912]
གང་ལ་བསླབ་པའི་གཞི་གསུམ་པར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་དགེ་སློང་མའི་བསླབ་པ་ལ་མི་སློབ་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་ཞིག་མཁན་མོ་ཉིད་ཀྱིས༌[^1886]རབ་ཏུ་ཕྱུང་བ་དང་། བསྙེན་པར་རྫོགས་པར་བྱས་པ་དག་ལ་མི་སློབ་པ་དེ་ལ་ལྟུང་བྱེད་དུ་འགྱུར་རོ་ཞེས་བྱ་བར་རྣམ་པར་གཞག་པ་ཡིན་ནོ། །

[Block 2913]
གང་ལ་བཞི་པ་བཏང་སྙོམས་སུ་གཏོགས་པ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ནད་པ་དག་ལ་ནད་གཡོག་མི་བྱེད་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རབ་ཏུ་ཕྱུང་བ་དང་བསྙེན་པར་རྫོགས་པར་བྱས་པ་དག་གིས་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2914]
དེ་དག་གཅིག་པུར་མ་ཟད་ཀྱི་འོན་ཀྱང་འདི་ལྟར་ཉེ་གནས་དང་བཅས་པས་ཀྱང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གནས་སྦྱིན་པའི་གནས་ཉིད་དུ་གཞག་པའི་ཉེ་གནས་ནད་པ་དག་ལ་ནད་གཡོག་མི་བྱེད་པ་ལ་ཡང༌[^1887]ལྟུང་བྱེད་ཁོ་ན་སྟེ། རབ་ཏུ་བྱུང་བའི་བར་ཆད་མཐོང་བ་ལ་སྦོམ་དགའ་མོ་དང་ལྷན་ཅིག་གནས་པ་ཡུལ་གཞན་དུ་མ་ཁྲིད་པས། དེ་ཇོ་བོས་འགྲོས་མེད་པར་རབ་ཏུ་འབྱིན་དུ་བཅུག་པ་ལས་བསླབ་པའི་གཞི་བཅས་པ་ཡིན་ནོ། །

[Block 2915]
སྒོ་ཁང་ལ་སོགས་པ་རྣམས་སུ་མགོན་མེད་རྣམས་བཅད་ནས། དེ་ཉིད་ཀྱིས་རབ་ཏུ་འབྱིན་པ་རྣམས་ཉེ་བར་མ་བསྡུས་པའོ། །

[Block 2916]
དེ་ལྟར་རབ་ཏུ་བྱུང་བའི་བསླབ་པ་དང་ནད་པ་རྣམས་ཀྱི་ནད་གཡོག་མི་བྱེད་པའོ། །

[Block 2917]
ཡལ་བར་འདོར་བ་ལས་གྱུར་པའི་ལྟུང་བྱེད་བཞིའོ། །

[Block 2918]
གང་ལ་འདོད་པ་བསྟེན་པ་ལས་གྱུར་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་རང་གི་བསྟེན་པར་བྱ་བའི་ནང་དུ་རྒྱ་སྐྱེགས་ཀྱི་ཆང་བུ་འཇུག་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རང་གིས་ཞེས་བྱ་བ་ནི་རང་འཛུད་པ༌[^1888]ལ་བྱའི། གཞན་དང་གཞན་གྱིས་འཛུད༌[^1889]དུ་བཅུག་པ་མ་ཡིན་ཏེ། བསྟེན་པར་བྱ་བའི་ནང་དུ་གཞན་འཛུད༌[^1890]དུ་བཅུག་པ་ལ་ནི་མི་ཚངས་པར་སྤྱད་པར་གཏོགས་པའི་སྦོམ་པོར་རྣམ་པར་གཞག་པའི་ཕྱིར་རོ། །

[Block 2919]
བསྟེན་པར་བྱ་བ་ཞེས་བྱ་བ་ནི་མོའི་དབང་པོའོ། །

[Block 2920]
ནང་དུ་ཞེས་བྱ་བ་ནི་བསྟེན་པར་བྱ་བའི་དོན་དུའོ། །

[Block 2921]
རྒྱ་སྐྱེགས་ཀྱི་ཆང་བུ་ཞེས་བྱ་བ་ནི་མདོ་ལས་གྲོགས་པོ་རྒྱ་སྐྱེགས་ཀྱིས་བསྐུས་པ་འཆང་ན་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2922]
རྣམ་པར་འབྱེད་པ༌[^1891]ལས་ཀྱང་གྲོགས་པོ་རྒྱ་སྐྱེགས་ཀྱི་ཚིགས་མས་བསྐུས་པའི་རྒྱ་སྐྱེགས་ཀྱི༌[^1892]ཚིགས་མའི་ཆང་བུ་བདག་ཉིད་འཆང་ན་ཞེས་གསུངས་པས། བསྟེན་པར་བྱ་བའི་ནང་དུ་འཆང་ན་ཞེས་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 2923]
དེ་བས་ན་ཉེ་བར་འཇོག་ན་ཞེས་དེ་ལྟར་ཉེ་བར་འབྲེལ་པའོ། །

[Block 2924]
དགེ་སློང་མ་རྣམས་ལ་ཁུ་བ་འབྱིན་པའི་ཁ་ན་མ་ཐོ་བ་གཞན་དུ་རྣམ་པར་གཞག་པའི་ཕྱིར༌[^1893]རོ། །

[Block 2925]
ནང་དུ་འཛིན་པར་ནུས་པ་ཁ་ན་མ་ཐོ་བ་ཞེས་བྱ་བ་མཐོང་བ་ཡིན་ནོ། །

[Block 2926]
འདི་ལྟར་དངོས་སུ་ཡང་གཏམ་གྱི་གཞི་ལས།

[Block 2927]
དགེ་སློང་གིས༌[^1894]བསམས་བཞིན་དུ་ཁུ་བ་ཕྱུང་ན་དགེ་འདུན་ལྷག་མའོ། །

[Block 2928]
དགེ་སློང་མས་ཕྱུང་ན་ལྟུང་བྱེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2929]
རང་གིས་རྩོལ་བར་བྱེད་ན་བུད་མེད་རྣམས་ལ་སྟོབས་དང་ལྡན་པའི་སྐུད་པ་སྟེ། དེ་བས་ན་འདིར་དགེ་འདུན་གྱི་ལྷག་མར་རྣམ་པར་གཞག་པའོ། །

[Block 2930]
མི་ཚངས་པར་སྤྱོད་པ་ལས་གྱུར་པའི་འཇུག་པ་འདི་ཞེས་བྱ་བ་ནི། རྒྱ་སྐྱེགས་ཀྱི་ཚིགས་མའི་ཆང་བུ་བཅུག་པ་ཙམ་ལ་ནི་ལྟུང་བྱེད་ཁོ་ནར་འགྱུར་རོ། །

[Block 2931]
འདིར་དེ་ཡན་ཆད་དུ་བྱེད་པ་ལས༌[^1895]ཐམས་ཅད་ནི་རྩོམ་པ་གཅིག་ཏུ་གྱུར་པས་བྱེད་ན་ནི་ལས་སུ་གཅིག་པ་ཡིན་ཏེ། ཁུ་བ་ཕྱུང་བའི་མཐར་ལྟུང་བྱེད་ཁོ་ནར་ཤེས་པར་བྱའོ། །

[Block 2932]
བཀྲུ་བའི་ཕྱིར་སོར་གཉིས་ཙམ་གཞུག་པ་རྗེས་སུ་གནང་བའི་ཕྱིར་དེ་ཡན་ཆད་ནི་འདིར་དང་པོ་ཡིན་གྱི། པགས་པའི་རིམ་པ་ནི་དང་པོ་མ་ཡིན་ནོ་ཞེས་བྱ་བར༌[^1896]ཤེས་པའོ། །

[Block 2933]
འདིར་རྒྱ་སྐྱེགས་ཀྱི་ཆང་བུ་ཞེས་སྨོས་པ་ནི་དཔེ་ཙམ་དུ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 2934]
འཇམ་པ་དང་ཧ་ཅང་ཕྲ་མོ་མ་ཡིན་པ་ཉིད་དང་། མི་འཇམ་པ་དང་ཧ་ཅང་ཕྲ་མོ་ཉིད་ལ་ནི་འདིར་དངོས་གཞིའི་མཐར༌[^1897]ཉེས་བྱས་སོ། །

[Block 2935]
ཕོ་ལ་ནི་ཇི་ཙམ་དུ་རེག་པ་ཚོར་གྱི་བར་དུ་འདིར་དེ་ཙམ་འཇམ་པ་ཉིད་ལ་མཐར་རྣམ་པར་གནས་པ་ཡིན་ཏེ། ཇི་ཙམ་དུ་འདོད་པ་ཉམས་སུ་མྱོང་བར་གྱུར་པའི་བར་དུ་ནི་སྦོམ་པོར་འགྱུར་རོ། །

[Block 2936]
ཕོ་ལ་ནི་རྒྱ་སྐྱེགས་ཀྱི་ཚིགས་མའི་ཆང་བུ་གཞུག་པའི་གནས་གཉིས་ཡོད་དེ། ཁ་དང་བཤང་བའི་ལམ་སྟེ། འདིར་ཤིན་ཏུ་སྟོབས་དང་ལྡན་པ་ཉིད་ཀྱི་ཕྱིར་སྐྱེས་པ་ལ་སྐུད་པས་དགེ་སློང་ལ་ནི་ཉེས་པ་སྦོམ་པོར་རིག་པར་བྱའོ། །

[Block 2937]
རྒྱུན་ལས་བཟློག་ཕྱོགས་སུ་བརྩལ་བར༌[^1898]མི་བྱའོ་ཞེས་བྱ་བ་ནི། དེ་ལ་སོགས་པ་འདི་མན་ཆད་ནི་ཉེས་བྱས་སུ་རིག་པར་བྱའོ། །

[Block 2938]
འདི་དག་ནི་ཕྲན་ཚེགས་དག་ལས་འབྱུང་སྟེ། འདི་དག་ཀྱང་འདི་ལྟ་བུ་དང་མཐུན་པ་གཞན་དག་གི་དཔེ་ཡིན་ནོ། །

[Block 2939]
མདོ་འདི་ནི་སྦོམ་དགའ་མོ་ཆུ་ཀླུང་གནས་ཅན་གྱི་ནང་དུ་ཞུགས་ཏེ། རྒྱུན་ལས་བཟློག་ཕྱོགས་སུ་རྩོལ་བར་བྱེད་པ་ན། དེ་དགེ་སློང་མ་རྣམས་ཀྱིས་ཅི་བྱེད་ཅེས་དྲིས་པ་དང་། རེག་པ་བདག་གིར་བྱེད་དོ་ཞེས༌[^1899]ཟེར་བ་ལས་བསྡུས་པ་ཡིན་ཏེ། དེ་བས་འདི་བསྟན་པ་ཡིན་ནོ། །

[Block 2940]
མངལ་གྱི་སྒོར་ཁུ་ཆུ་བླུགས་པར་མི་བྱའོ་ཞེས་བྱ་བ་དེ་ནི། སྦེད་མའི་གླེང་གཞི་ལས་སོ། །

[Block 2941]
རྐེད་བཅིངས་ཀྱིས༌[^1900]གློ་བཅིང་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་གློ་གཉིས་ཕྲ་མོར་འདུག་པར་བྱ་བའི་ཕྱིར་རྐེད་བཅིངས་འཆང་བའོ། །

[Block 2942]
འདིར་གློ་བཅིང་བར་བྱ་བའི་ཕྱིར་རྐེད་བཅིངས་ལ་སོགས་པའི་རྫས་གང་ཡང་རུང་བ་ཐམས་ཅད་ལས་སྤྱིར་རྐེད་བཅིངས་ཞེས་བྱའོ། །

[Block 2943]
བྲང་བཅིངས་ཀྱིས་ནུ་མ་གཉིས་མི་བྱའོ་ཞེས་བྱ་བ་ཡང་བཅིངས་པར༌[^1901]ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2944]
ནུ་མ་གཉིས་འཆིང་བའི་དོན་ཅན་རྐེད་དཀྲིས་ཐམས་ཅད་ལ་བྲང་བཅིངས་ཞེས་བྱ་སྟེ། ནུ་མ་གཉིས་འཕྱང༌[^1902]དུ་མི་གཞུག་པའི་དོན་དུ་དེ་འཆང་བའོ། །

[Block 2945]
མཛེས་འགྱུར་གྱི་བར་ཆད་ཀྱིས་བར་དུ་གཅད་པར༌[^1903]མི་བྱའོ་ཞེས་བྱ་བ་ཡང་ནུ་མ་གཉིས་མི་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །
--- END BLOCKS ---
