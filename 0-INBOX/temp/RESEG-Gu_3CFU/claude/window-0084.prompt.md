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
ཉེ་བར་འགྲོ་བ་ལས༌[^2018]ཤོར་ནའོ་ཞེས་བྱ་བ་ནི་འཁྱུད་པའི་དོན་དང་ཕྱུང་བའི་དོན་དུ་ཞེས་བྱ་བ་ཤུགས་ཀྱིས༌[^2019]ཤེས་པར་བྱའོ། །

[Block 2942]
འཁྱུད་པ་ནི་དོན་དུའམ་མི་ཚངས་པར་སྤྱོད་པའི་དོན་དུ་ཉེ་བར་འགྲོ་བཞིན་པ༌[^2020]གནས་ནས་གནས་གཞན་དུ་དེའི་དོན་ཉིད་དུ་འཇུག་པའི་ཕྱིར་ཞེས་བྱ་བ་རིག་པར་བྱ་སྟེ། དེའི་དོན་མ་ཡིན་པར་འཇུག་པ་ལ་ལྟུང་བ་མེད་པར་བརྗོད་པའི་ཕྱིར་རོ། །

[Block 2943]
ཚུལ་བཞིན་མ་ཡིན་པ་ཡིད་ལ་བྱེད་པ་ལས་སོ་ཞེས་བྱ་བ་ནི་བྱེ་བྲག་ངེས་པར་མྱོང་བ་ལ་སོགས་པའི་བདེ་བ་སོ་སོར་ཉམས་སུ་མྱོང་བ་ཉེ་བར་བསྒྲུབ་པ་ལ་བརྗོད་པ་ཉིད་ཀྱི་ཕྱིར་ལྟུང་བ་ལ་གཞན་གྱི་རྣམ་པ་ཚུལ་བཞིན་མ་ཡིན་པ་ཡིད་ལ་བྱེད་པ་བསྡུས་པའི་དོན་དུ་ནི་མདོ་ཡིན་ནོ། །

[Block 2944]
ཡན་ལག་གི་རྣམ་པ་འཛིན་པ་ལས་སོ་ཞེས་བྱ་བ་ནི་དོན་གཞན་ཉིད་ལ་སྐྱོན་དང་བྲལ་བ་ཉིད་ལ༌[^2021]རྣམ་པར་གཞག་པས་འབྱུང་བའི་ཕྱིར་ཡིད་ཆེས་པའོ། །

[Block 2945]
བྱ་བ་མེད་པའི་ཕྱིར་འདིར་དགེ་འདུན་ལྷག་མ་མི་བསྐྱེད་པ་སྟེ། བྱ་བ་དང་བྲལ་བའི་ལུས་ཀྱི་བྱ་བ་ལ་ཉེས་བྱས་ཞེས་བྱ་བ་དེའི་ཕྱིར་རིག་པར་བྱའོ། །

[Block 2946]
འཛག་སྣོད་ལ་དྲུད་པ་ལས་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ནི་བབ་ཅོལ་དུ་ཕྱུང་བ་བཞིན་དུ་དེའི་དོན་དུ་འཇུག་པ་ལ་ཞེས་བྱ་བ་ཤུགས་ཀྱིས་རྟོགས་པར་བྱའོ། །

[Block 2947]
འཛག་སྣོད་ལ་དྲུད་པ་ལས་ཞེས་བྱ་བ་ནི་ཆོས་གོས་ལ་ཁུ་བས་གོས་པའི་དོན་དུ་བསག་པ༌[^2022]དང་སོག་པའི༌[^2023]འཛག་སྣོད་ཀྱིས་སོ། །

[Block 2948]
སྔོན་གྱི་ཆུང་མས་འཁྱུད་པ་ལས་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་ཕ་མ་དང་སྲིང་མོ་དང་བུ་མོས་ཡུན་རིང་བར་བཟུང་བ་ལ་ཉེས་མེད་པ་འབའ་ཞིག་ཏུ་མ་ཟད་ཀྱི་གཞན་ལ་ཡང་དག་པར་ལོངས་སྤྱོད་པས་ཀྱང་ངོ་། །རྐང་པ་དང་བྱིན་པ་དང་དཔུང་པ་དང་མཐེ་བོང་ལ་སོགས་པ་ནས་བུད་མེད་ཀྱིས་བཟུང་བ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་བབ་ཅོལ་དུ་ཕྱུང་བ་ལ་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ཡང་གཉིས་ཀ་ལ་སྦྱར་བའོ། །

[Block 2949]
དེའི་ཕྱིར་ཞུགས་པ་མ་ཡིན་པ་ལ་འདི་ཤུགས་ཀྱིས་གོ་བར་བྱའོ། །

[Block 2950]
དགེ་འདུན་གྱི་ལྷག་མ་དང་པོའི་འདུལ་བྱེད་རྣམས་སོ། །

[Block 2951]
འབྱིན་པའི་དགེ་འདུན་ལྷག་མ་རྫོགས་སོ།། །།

[Block 2952]
འདི་ལ་བྱེད་པ་པོ་ཉིད་ནི་བུད་མེད་དོ་ཞེས་བྱ་བ་ནི་རེག་པའི་བསླབ་པའི་གཞི་འདི་ལ་ལྟུང་བའི་བྱེད་པ་པོ་ཉིད་ནི་བུད་མེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2953]
དབེན་པ་ན་འདུག་པ་དང་འགྲེང་བ་གཉིས་ཀྱིའོ་ཞེས་བྱ་བ་ནི་སླར་དགེ་སློང་གང་ཞིག་བུད་མེད་ཀྱི་ཚོགས་དང་ལྷན་ཅིག་ཏུ་གཅིག་པུ་ཉིད་ཀྱིས་དབེན་པ་སྐྱབས་ཡོད་པ་ན་སྟན་ལ༌[^2024]འདུག་པར་བྱེད་པ་དང་། སླར་དགེ་སློང་གང་དགེ་སློང་མ་དང་། ལྷན་ཅིག་གཅིག་པུ་གཅིག་དང་དབེན་པ་སྐྱབས་ཡོད་པ་ན་འགྲེང་ན་ལྟུང་བྱེད་དོ་ཞེས་གསུངས་པ་འདི་དག་ལ་ཡང་བྱེད་པ་པོ་ཉིད་ནི་བུད་མེད་དོ། །

[Block 2954]
ཉལ་པོ་བྱེད་པར་ཤོམ་པ་ལ་ཡང་ངོ་ཞེས་བྱ་བའི༌[^2025]སྒྲ་ནི་འདུག་པ་དང་འགྲེང་བ་དག་ལ་ཡང་བྱེད་པ་པོ་ཉིད་བུད་མེད་དོ་ཞེས་བྱ་བའི་རྗེས་སུ་བསྙག་པའི་ཕྱིར་རོ། །

[Block 2955]
ཉལ་པོ་བྱེད་པར་ཤོམ་པའི་ཁྱིམ་ན་འདུག་པ་དང་འགྲེང་བ་དག་ལ་ཡང་བྱེད་པ་པོ་ཉིད་དུ༌[^2026]ནི་བུད་མེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2956]
ལྷན་ཅིག་ཉལ་བ་ལའོ་ཞེས་བྱ་བ་ནི་སླར་དགེ་སློང་གང་བུད་མེད་ཀྱི་ཡུལ་དང་ལྷན་ཅིག་གནས་གཅིག་ན་ཉལ་ན་ལྟུང་བྱེད་དོ་ཞེས་གསུངས་པ་འདི་ལ་བུད་མེད་ནི་ལྟུང་བའི་བྱེད་པ་པོ་ཉིད་དོ། །

[Block 2957]
རིག་པའི་སྐྱེས་པ་མེད་པའི་བུད་མེད་དང་ལྷན་ཅིག་ལམ་དུ་འགྲོ་བ་ལའོ་ཞེས་བྱ་བ་ནི་སླར་དགེ་སློང་གང་སྐྱེས་པ་མེད་པར་བུད་མེད་དང་ལྷན་ཅིག་འགྲོན་ལམ་དུ་འགྲོ་ན་ཞེས་བྱ་བའི་འཇུག་པ་འདི་ལ་བུད་མེད་ནི་བྱེད་པ་པོ་ཉིད་དོ། །

[Block 2958]
འདིར་རེག་པའི༌[^2027]སྒྲས་ནི་ཆོས་སྟོན་པའི་བསླབ་པའི་གཞིའི་རྗེས་སུ་འབྲངས་ནས་བྱས་པའོ། །

[Block 2959]
རིག་པ་དང་རྩོམ་པའི་འདུན་པ་ལ་སྔར་ཉིད་དུ་སྐུར་པ་འདེབས་པ་ལ་བརྟེན་པ་ལ་མ་བསྒྲུབས་པ༌[^2028]ནི་འདིར་སྐྱེས་པའི་དོན་ཏོ། །

[Block 2960]
འདི་ནི་ཀུན་ནས་འགྲོ་བའི་ཁྱེའུ་དང་དུད་འགྲོ་རྨོངས་པས་ཀྱང་བསྒྲུབ་པ་མ་ཡིན་ནོ། །

[Block 2961]
འོག་མ་གཉིས་ལའོ་ཞེས་བྱ་བ་ནི་འདི་ལས་འོག་མ་གང་ཡིན་པ་འཁྲིག་པ་དང༌[^2029]ལྡན་པ་སྨྲ་བ་དང་། བསྙེན་བཀུར་བསྔགས་པ་གཉིས་པོ་དག་ལ་ཡང་འདིར་བྱེད་པ་པོ་ནི་བུད་མེད་ཉིད་དོ། །

[Block 2962]
ཁྱིམ་པ་མོ་ལ་སྟོན་པ་ལའོ་ཞེས་བྱ་བ་ནི་ཁྱིམ་པ་མོ་ལ་ཚིག་དྲུག་གམ་ལྔ་ལས་ལྷག་པར་ཆོས་འཆད་པའི་ལྟུང་བྱེད་ལ་ཡང་བྱེད་པ་པོ་ཉིད་བུད་མེད་དོ། །

[Block 2963]
དེ་ལྟར་རབ་ཏུ་བྱུང་བ་ལ་སློབ་མར་གྱུར་པ་ཉིད་ཀྱི་ཕྱིར་ལྟུང་བ་མི་སྐྱེད༌[^2030]པའོ། །

[Block 2964]
ཕྱི་རོལ་གྱི་རབ་ཏུ་བྱུང་བ་མོ་ལ་ནི་ཉེས་བྱས་ཉིད་དོ། །

[Block 2965]
ཞུ་བའི༌[^2031]ངེས་པར་བྱེད་པ་འཆད་པར་འགྱུར་ཏེ། དེ་བས་ན་བུད་མེད་ཁྱིམ་ན་གནས་པ་ཉིད་བྱེད་པ་པོ་ཞེས་བྱ་བའོ། །

[Block 2966]
ཅི་ཁྱིམ་པ་མོ་ལ་སྟོན་པའི་གནས་སྐབས་ཐམས་ཅད་ཀྱིས་བྱེད་པ་པོ་ཉིད་བུད་མེད་ཡིན་ནམ༌[^2032]ཞེ་ན་མ་ཡིན་ཏེ། དེའི་ཕྱིར་སྐྱེས་པ་མེད་པར་རོ་ཞེས་བྱ་བ་སྨོས་སོ། །ཇི་ལྟར་ཞེ་ན། དེའི་ཕྱིར་རིག་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འཁྲིག་པ་དང་ལྡན་པའི་བརྗོད་པ་དང་སྤྱོད་པ་དག་ལ་མངོན་པར་ཤེས་པ་ཉིད་ནི་འདིར་རིག་པ་ཉིད་དུ་ཤེས་པར་བྱའོ། །

[Block 2967]
འདི་ལ་རིག་པ་མ་ཡིན་པ་ཡོད་པ་ནི་མེད་པ་ཉིད་དེ་དོན་ཡོད་པ་ནི་མ་ཡིན་ནོ། །

[Block 2968]
དེ་བས་ན་ཡོངས་སུ་རྫོགས་པ་ཉིད་ནི་འདི་དག་ལས་རིག་པ་མེད་པར་ཉེ་བར་གྱུར་པ་ལ་སྟོན་པ་དང་། ལམ་དུ་འགྲོ་བ་དག་ལ་ཁ་ན་མ་ཐོ་བ་མི་སྐྱེད༌[^2033]དེ་ན་སྨད་པ་ཡང་ནི་མ་ཡིན་ནོ། །

[Block 2969]
ཡོད་ཀྱང་མི་རུང་བ་ལའོ་ཞེས་བྱ་བ་ནི་སྦྱར་མའི་སྤྱོད་པ་གང་དག་ཡིན་པ་དེ་དག་ཉེ་བར་སྟོན་པར་བྱེད་པ་སྟེ། དངོས་སུ་ཡོད་པ་ལ་ནི་རིག་པའི་སྐྱེས་པ་ཡོད་ཀྱང་བུད་མེད་ནི་བྱེད་པ་པོ་ཡིན་ནོ། །

[Block 2970]
དེ་ནི་ཉེས་བྱས་ཀྱིའོ་ཞེས་བྱ་བ་ནི་དངོས་སུ་གནས་པ་ལ་ཡང་མི་རུང་བ་ལ་བྱེད་པ་པོ་ཉིད་གང་ཡིན་པ་འདི་ཉེས་བྱས་ལ་སྟེ་དངོས་གཞི་ལ་ནི་མ་ཡིན་ནོ། །

[Block 2971]
འདིར་གཞུང་ནི་ཞུ་བ༌[^2034]ལས།

[Block 2972]
བུད་མེད་མི་རུང་བ་ལས་སྐྱེས་པ་རུང་བ་དང་ལྷན་ཅིག་ཆོས་སྟོན་ན་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2973]
གླིང་གཞན་ནས་སྐྱེས་པ་དང་འགྱུར་བ་བརྟེན་པ༌[^2035]གཉིས་ནི་མ་ཆོག་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་བྱང་གི་སྒྲ་མི་སྙན་ལ་སོགས་པའི་གླིང་གཞན་ནས་སྐྱེས་པ་དང་། ལུས་སམ་ངག་གིས་བུད་མེད་ཀྱི་སྐབས་སམ་སྐྱེས་པའི་སྐབས་སུ་འཁྲིག་པ་དང་ལྡན་པའི་རྣམ་པར་འགྱུར་བ་གང་གིས་བསྟེན་པར་འགྱུར་བ་ནི་དཔེར་ན་བསྙོན༌[^2036]ཐབས་མཁན་ནམ་མ་ནིང་ལྟ་བུ་དེ་གཉིས་ནི་སྟོན་པའི་སྐབས་འདིར་རིག་པར་མ་ཆོག་པ་ཉིད་དོ། །

[Block 2974]
འདིར་རུང་བ་ལ་སྟོན་པ་ཡོད་པར་གྱུར་པ་ལ་ནི་ཉེས་བྱས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2975]
མི་རུང་བ་ལ་ནི་ཤིན་ཏུ་ལྕི་བ་འདིའི་རྗེས་སུ་འབྲངས་པས་ཉེས་བྱས་ཤེས་པར་བྱའོ། །

[Block 2976]
འདིར་གཞུང་ནི་ཞུ་བ༌[^2037]ལས་བཙུན་པ་དགེ་སློང་གིས་རེ་ཞིག་འཛམ་བུའི་གླིང་གི་བུད་མེད་ལ་བྱང་གི་སྒྲ་མི་སྙན་པ་དང་ལྷན་ཅིག་ཆོས་སྟོན་ན་ལྟུང་བ་ཅིར་འགྱུར། ཉེས་བྱས་སོ། །

[Block 2977]
དེ་བཞིན་དུ་གླིང་གཞན་པ་རྣམས་དང་ལྷན་ཅིག་ཆོས་སྟོན་པ་ལ་ཡང་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2978]
བཅོམ་ལྡན་འདས་ཀྱིས་རིག་པའི་སྐྱེས་པ་མེད་པར་བུད་མེད་ལ་ཆོས་བསྟན་པར་མི་བྱའོ་ཞེས་གང་གསུངས་པ་དེ་ལ་རིག་པའི་སྐྱེས་པ་ཇི་ལྟ་བུ་ཞིག་དང་ལྷན་ཅིག་ཏུ་བུད་མེད་ལ་ཆོས་བསྟན་པར་བྱ་ཞེ་ན། རུང་བ་གང་ཡིན་པའོ། །

[Block 2979]
རུང་བ་ཇི་ལྟ་བུ་ཞེ་ན། སྨྲས་པ། ཁྱིམ་པ་ཡང་རུང་རབ་ཏུ་བྱུང་བ་ཡང་རུང་སྟེ། འགྱུར་བ་བསྟེན་པར་མི་བྱེད་པ་གང་ཡིན་པའོ། །

[Block 2980]
རྣམ་པར་འགྱུར་བའི་སྒོ་འབྲེལ་བའི་དོན་དུ་འདིར་རིག་པའི་སྐྱེས་པ་ལ་བརྟེན་པའོ། །
--- END BLOCKS ---
