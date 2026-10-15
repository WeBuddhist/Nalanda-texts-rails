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
རྐེད་བཅིངས་ཀྱིས༌[^1900]གློ་བཅིང་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་གློ་གཉིས་ཕྲ་མོར་འདུག་པར་བྱ་བའི་ཕྱིར་རྐེད་བཅིངས་འཆང་བའོ། །

[Block 2942]
འདིར་གློ་བཅིང་བར་བྱ་བའི་ཕྱིར་རྐེད་བཅིངས་ལ་སོགས་པའི་རྫས་གང་ཡང་རུང་བ་ཐམས་ཅད་ལས་སྤྱིར་རྐེད་བཅིངས་ཞེས་བྱའོ། །

[Block 2943]
བྲང་བཅིངས་ཀྱིས་ནུ་མ་གཉིས་མི་བྱའོ་ཞེས་བྱ་བ་ཡང་བཅིངས་པར༌[^1901]ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2944]
ནུ་མ་གཉིས་འཆིང་བའི་དོན་ཅན་རྐེད་དཀྲིས་ཐམས་ཅད་ལ་བྲང་བཅིངས་ཞེས་བྱ་སྟེ། ནུ་མ་གཉིས་འཕྱང༌[^1902]དུ་མི་གཞུག་པའི་དོན་དུ་དེ་འཆང་བའོ། །

[Block 2945]
མཛེས་འགྱུར་གྱི་བར་ཆད་ཀྱིས་བར་དུ་གཅད་པར༌[^1903]མི་བྱའོ་ཞེས་བྱ་བ་ཡང་ནུ་མ་གཉིས་མི་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2946]
ནུ་མ་གཉིས་ཕན་ཚུན་དུ་མི་འབྱར་བའི་དོན་དུ་བར་དུ་གཅོད་པའི་གོས་ནི་མཛེས་འགྱུར་གྱི་བར་ཆད་ཅེས༌[^1904]བྱ་སྟེ། དེས་ནུ་མ་གཉིས་ཀྱི་བར༌[^1905]དུ་གཅད་པར༌[^1906]མི་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2947]
འདིར་དེ་གསུམ་གྱི་གཞུང་ནི། དགེ་སློང་མས་རྐེད་བཅིངས་ཀྱིས་གློ་བཅིང་བར་མི་བྱའོ། །

[Block 2948]
བཅིངས་ན་འགལ་ཚབས་ཅན་དུ་འགྱུར་རོ། །

[Block 2949]
དགེ་སློང་མས་བྲང་ཆིངས༌[^1907]དང་མཛེས་འགྱུར་གྱི་བར་ཆད་བཅང་བར་མི་བྱའོ། །

[Block 2950]
བཅིངས་ན་འགལ་ཚབས་ཅན་དུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2951]
དེ་དག་ནི་དཔེའོ་ཞེས་བྱ་བ་ནི་རྐེད་བཅིངས་དེ་གཙོ་བོར་གྱུར་པ་གློའི་སྐ་རགས་དང་མཛེས་འགྱུར་གྱི་བར་ཆད་གསུམ་པོ་གང་ཡིན་པ་དེ་ནི་དཔེ་ཙམ་དུ་རིག་པར་བྱའོ། །

[Block 2952]
འདིས་རྐེད་བཅིངས་ལ་སོགས་པ་ཐམས་ཅད་ལ་དེའི་འབྲས་བུ་སྒྲུབ་པར༌[^1908]བྱེད་པ་འཕངས་པ་ཉིད་དེ། །[^1909]གཞན་གྱིས་ཀྱང་རྐེད་འཆིངས༌[^1910]ལ་སོགས་པར་གྱུར་པས་དོན་འདི་བསྒྲུབས་པས༌[^1911]ཁ་ན་མ་ཐོ་བ་མཉམ་པ་ཉིད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2953]
འདོད་པ་བསྟེན་པའི་ལྟུང་བྱེད་དོ། །

[Block 2954]
གང་ལ་འདོད་པ་བསྟེན་པ་ལྟར་འཆོས་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་སོར་མོའི་ཚིགས་གཉིས་ལས་ལྷག་པར་མོ་མཚན་གྱི་ནང་འཁྲུ་བ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་སོར་མོ་རྣམས་ཀྱི་ཚིགས་ནི་ཚིགས་ཉིད་ལ་བྱ་སྟེ། ཚིགས་ཀྱི་བར་རྣམས་ནི་མ་ཡིན་ནོ། །

[Block 2955]
དྲི་མར་གྱུར་པ་བསལ་བར་བྱ་བ་འདི་ཙམ་མེད་པའི་ཕྱིར་ཞེས་རྟོགས་པར་བྱའོ། །

[Block 2956]
གང་གི་ཕྱིར་སོར་མོ་རིང་བ་ཉིད་ཀྱི༌[^1912]ཚིགས་གཉིས་ཀྱིས་ཤེས་པར་གྱུར་པ་ལ་ཤིན་ཏུ་རིང་བ་བཅུག་པར་ཐལ་བར་འགྱུར་རོ། །

[Block 2957]
དེ་ཡང་ཆེ་བ་ཉིད་ཀྱིས་མི་འདྲ་བ་སྟེ་འདིའི་ཚད་ཀྱི་ཐ་སྙད་དོ། །

[Block 2958]
དེ་ལ་དབུས་མའི་ཆེ་བ་ཉིད་ལ་ཚིག་འདི་སྨོས་སོ། །

[Block 2959]
འདིར་ཡང་རང་གིས་ཞེས་བྱ་བར་སྦྱར་ཏེ། གཞན་བྱེད་དུ་བཅུག་པ་ལ་ནི་མི་ཚངས་པར་སྤྱོད་པར་གཏོགས་པའི་ཁ་ན་མ་ཐོ་བར་རྣམ་པར་གཞག་པའི་ཕྱིར་རོ། །

[Block 2960]
འདི་ནི་སྦོམ་དགའ་མོས་རྨའི་སྦུབས་སུ་ལག་པ་བཅུག་སྟེ་རྩོལ་བ་ལས་མདོར་བྱས་པ་གང་ཡིན་པ་དེས་སོ། །

[Block 2961]
འདོད་པ་བསྟེན་པ་ལྟར་བཅོས་པའི་ལྟུང་བྱེད་དོ། །

[Block 2962]
གང་ལ་འདོད་པ་བསྟེན་པ་ལྟར་གནོད་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་དེ་ལ་ལག་མཐིལ་གྱི་ཐལ་ལྕག་གིས་བསྣུན་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་ལ་ཞེས་བྱ་བ་ནི་མོ་མཚན་ལའོ། །

[Block 2963]
བསྣུན་པ་ལའོ་ཞེས་བྱ་བ་ནི་བྱེ་བྲག་མ་སྨོས་པའི་ཕྱིར་ཆགས་པ་ཅན་ནམ། མ་ཆགས་པའི་སེམས་ཀྱིས་ལྟུང་བྱེད་ཅེས་བྱ་བ་ཡིད་ཆེས་པའོ། །

[Block 2964]
འདོད་པ་བསྟེན་པ་ལྟར་གནོད་པའི་ལྟུང་བྱེད་དོ། །

[Block 2965]
གང་ལ་མཚན་མ་ཉེ་བར་འཆོས་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་དེ་ལ་སྤུ་འཐོག་པར་བྱེད་དམ་བྱེད་དུ་འཇུག་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་ལ་ཞེས་བྱ་བ་ནི་མོ་མཚན་ནོ། །

[Block 2966]
མདོ་ལས་གནོད་པ་ཅན་གྱི་གནས་ལ་སྤུའི་ལས་བྱེད་ནའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2967]
འདིར་རྣམ་པར་འབྱེད་པ་ལས་གནོད་པ་ཅན་གྱི་གནས་ལ་ཞེས་བྱ་བ་ནི་གསང་བའི་གནས་ལའོ། །

[Block 2968]
སྤུའི་ལས་ཞེས་བྱ་བ་ནི་སྤུ་འཐོག་པ་སྟེ་ལྟུང་བྱེད་ཀྱིས་སྲེག་པར་བྱེད་ཅེས་བྱ་བའི་དོན་ཏོ།[^1913] །འདིར་རེག་པའི་ཁ་ན་མ་ཐོ་བར་རྣམ་པར་མི་གཞག་སྟེ། འདིར་ཇི་ལྟར་བྱས་པ་ཉིད་འདི་བསྒྲུབས་པས༌[^1914]ལྟུང་བྱེད་དོ། །

[Block 2969]
འོན་ཀྱང་བཅོས་ཟིན་པ་ལ་མཉམ་པ་ཉིད་དུ་འདི་ལ་རང་དང་གཞན་གྱི་སྟེ།[^1915] དེ་ལྟ་བས་ན་བྱེད་པ་དང་བྱེད་དུ་འཇུག་པ་ཞེས་བྱ་བ་གཉིས་ཀ་བསྟེན༌[^1916]པའོ། །

[Block 2970]
འདིར་བཅོས་ཟིན་པ་ནི་དོན་ཏོ།[^1917] །དེ་བས་ནི༌[^1918]འདིར་སྤུ་གཅིག་བཏོགས་པ༌[^1919]ལ་ཡང་དངོས་གཞིའོ། །

[Block 2971]
གང་ཞིག་ཡང་བྱས་པ་ཉིད་ཀྱིས་འདིར་རྣམ་པར་གཞག་པར་རིགས་པ་དེ་དེ་ལས་ཡང་དག་པར་བྱས་པ་ཉིད་ཀྱིས་མོ་མཚན་ལ་ནི་འདིར་དངོས་གཞིའོ། །

[Block 2972]
རྩོམ་པ་གཅིག་པར་འགྱུར་བ་ཉིད་ཀྱིས་ལྷག་པའི༌[^1920]རྗེས་སུ་འགྲོ་བར་རིག་པར་བྱའོ། །

[Block 2973]
འདིར་སྐྱེས་པ་ལ་འདིར་རྒུད་པ་མེད་དེ། [^1921]བུད་མེད་ལ་ཇི་ལྟ་བ་དེ་བས་ན་དེ་ལ་འདིར༌[^1922]འཇུག་ན་ཉེས་བྱས་སུ་རྣམ་པར་གཞག་པ་ཡིན་ནོ། །

[Block 2974]
ལག་པས་སྟེང་དུ་ཐལ་ལྕག་གིས་བསྣུན་པ་ནི་གལ་ཏེ་འདོད་ཆགས་ཀྱིས་བྱེད་ན་ནི་སྦོམ་པོའོ། །

[Block 2975]
གལ་ཏེ་འདོད་ཆགས་མེད་ན་ནི་ཉེས་བྱས་སོ་ཞེས་རིག་པར་བྱའོ། །

[Block 2976]
བསྟེན་པར་བྱ་བ་འཆོས་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 2977]
ད་འདི་མན་ཆད་ནི་རེག་པར་བྱ་བ་མ་ཡིན་པ་དང་། བསྟེན་པའི་ལྟུང་བྱེད་བཅུ་གཅིག་པོ་རྣམས་སྟོན་ཏེ། དགེ་སློང་མས་སྐྱེས་པ་རེག་པར་བྱ་བ་མ་ཡིན་པ་དེ་དང་ལྷན་ཅིག་རེག་པའི་ཚུལ་གྱིས་བསྟེན་པ་གང་ཡིན་པ་དེ་རྣམས་ལ་རེག་པར་བྱ་བ་མ་ཡིན་པ་དང་བསྟེན་པའི་ལྟུང་བྱེད་རྣམས་ཤེས་པར་བྱའོ། །

[Block 2978]
དེ་ལ་དེ་དག་གི་དང་པོ་ཇེ་བཤད་པར་བྱ་སྟེ། དེའི་ཕྱིར་ཁྱིམ་པ་དང་ལྷན་ཅིག་དབེན་པ་སྐྱབས་ཡོད་པ་ན༌[^1923]འགྲེང་བ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདོམ་གང་གི་ནང༌[^1924]ཚུན་ཆད་ཅེས་བྱ་བ་དེ་དགེ་སློང་གི་དབང་དུ་བྱས་པའི་ཆོ་གའི་རྗེས་སུ་འབྲངས་ནས་ཤེས་པར་བྱའོ། །

[Block 2979]
འདུག་པ་ལ་ཡང་ལྟུང་བྱེད་འདི་ཡིན་ཏེ། འཇུག་པ་དེ་ལ་ཤིན་ཏུ་ལྕི་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2980]
མི་ཚངས་པར་སྤྱད་པའི་ཡན་ལག་ཏུ་གྱུར་པ་དེ་ཐམས་ཅད་ལ་མི་ཚངས་པར་སྤྱོད་པ་དང་འབྲེལ་པ་ལ་སྟོབས་དང་ལྡན་པ་ཉིད་ལ་འགལ་ཟླར་རྣམ་པར་གནས་པ་ཉིད་དོ། །
--- END BLOCKS ---
