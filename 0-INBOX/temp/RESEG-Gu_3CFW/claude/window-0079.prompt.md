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
[Block 2766]
རྣམ་པ་གང་གིས་དེ་རྣམ་པར་གཞག་པར༌[^2594]བྱ་ཞེ་ན། དེའི་ཕྱིར་གསོལ་བས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གསོལ་བ་འབའ་ཞིག་གི་ལས་གྱིའོ། །

[Block 2767]
གང་གི་ཕྱིར་ཁས༌[^2595]སྦུབ་པ་དེའི་དོན་བརྗོད་པར་བྱ་སྟེ། ལྷུང་བཟེད་ཁས༌[^2596]སྦུབ་བའི་ཁྱིམ་དུ་འགྲོ་བར་མི་བྱའོ། །

[Block 2768]
སྟན་ལ་འདུག་པར་མི་བྱའོ། །

[Block 2769]
སྦྱིན་པར༌[^2597]བྱ་བའི་ཆོས་བཤམས་པ་ལས་ཡོངས་སུ་ལོངས་སྤྱོད་པར༌[^2598]མི་བྱའོ་ཞེས་བྱ་བ་ལ་འདིས་ནི་གཙུག་ལག་ཁང་ཡང་སྤང་བར་ཡང་རིག་པར་བྱའོ། །

[Block 2770]
དེ་ལྟར་ཡང་འདིར་གཞུང་ཁ་ཅིག་ལས་སྦྱིན་པར་བྱ་བའི་ཆོས་སྔར་བཤམས་པ་དག་ཡོངས་སུ་ལོངས་སྤྱད་པར་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2771]
བསོད་སྙོམས་བླང་བར་མི་བྱའོ། །

[Block 2772]
ཆོས་བསྟན་པར་མི་བྱའོ། །

[Block 2773]
གང་དུ་ལས་བྱ་བ་དེར་གཏོགས་པ་དག་ལ་ཁས་སྦུབ༌[^2599]པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 2774]
གནས་ཀྱི་གཞི་གང་དུ་ལས་བྱ་བ་དེར་གཏོགས་པའི་ཁྱིམ་བདག་རྣམས་ལ་ལྷུང་བཟེད་ཁས༌[^2600]སྦུབ་པ་ཉིད་ཡིན་ནོ། །

[Block 2775]
འདིར་གཞུང་ནི་དགེ་སློང་གི༌[^2601]ཁྱིམ་བདག་བཞིའི༌[^2602]གནས་བཞི་པོ་དག་ཏུ་ལྷུང་བཟེད་བཞི་ཁས༌[^2603]སྦུབ་པར་འགྱུར་བ་མཆིས་སམ། བཀའ་སྩལ་པ། ཡོད་དེ་ཁྲིའམ་ཁྲིའུ་འམ་ཤིང་ངམ༌[^2604]རེ་ལྡེས་གནས་བཞི་པོ་དག་གི་མཚམས་དག་མནན་ཏེ་ཁ་སྦུབ་པར༌[^2605]བྱེད་ནའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2776]
ཐ་ན་གནས་ནས་ཕྱུང་བ་ཕན་ཆད་རང་གི་ཕྱོགས་དང་མཐུན་པའི༌[^2606]མ་ཡིན་པའི་ཁྱིམ་དུ་དེ་མི་འཆགས་སོ་ཞེས་བྱ་བ་ནི་ཐ་ན་གནས་ནས་ཕྱུང་བ་ཕན་ཆད་ཀྱི་སྒྲ་དབྲི་བའོ། །

[Block 2777]
ཐ་ན་གནས་ནས་ཕྱུང་བ་ཕན་ཆད་ཀྱི་སྒྲས་ཕྱོགས་དང་མཐུན་པ་མ་ཡིན་པ་ཚུན་ཆད་ཀྱི་དགེ་སློང་གི་ཡོན༌[^2607]བདག་གི་ཁྱིམ་དུ་ལྷུང་བཟེད་ཁས་སྦུབ་པ༌[^2608]དེ་མི་འཆགས་སོ། །

[Block 2778]
འདིར་གཞུང་ནི་དགེ་སློང་ཁས་མ་བླངས་པ་དག་ལ་ཁས་བླངས་པ་དག་གིས་ཁྱིམ་དག་ཏུ་ལྷུང་བཟེད་ཁས༌[^2609]མ་སྦུབ་པར་བརྗོད་པར་བྱའོ། །

[Block 2779]
དེ་བཞིན་དུ་གནས་ནས་ཕྱུང་བ་དག་གིས་རང་བཞིན་དུ་གནས་པ་དག་གི་ཁྱིམ་བདག་རྣམས་ཀྱི་ཁྱིམ་བདག་ཏུ་ལྷུང་བཟེད་ཁས༌[^2610]སྦུབ་པར་བྱེད་ན་ཁས༌[^2611]མ་སྦུབ་པར་བརྗོད་པར་བྱའོ། །

[Block 2780]
དེ་བཞིན་དུ་གནས་པར་མི་བྱ་བ་དག་གིས་གནས་པར་བྱ་བ་དག་གི༌[^2612]ཁྱིམ་བདག་རྣམས་ཀྱི་ཁྱིམ་དག༌[^2613]ཏུ་ལྷུང་བཟེད་ཁས༌[^2614]སྦུབ་པར་བྱེད་ན་ཁས༌[^2615]མ་སྦུབ་པར་བརྗོད་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2781]
དེ་འགའ་ཞིག་གིས་གོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ལྷུང་བཟེད་ཁས༌[^2616]སྦུབ་པ་དེ་དགེ་སློང་འགའ་ཞིག་གིས་ཁྱིམ་བདག་དེ་ལ་དགེ་འདུན་གྱིས་ཁྱོད་ལ་ལྷུང་བཟེད་ཁས༌[^2617]སྦུབ་པོ་ཞེས་གོ་བར་བྱའོ། །

[Block 2782]
བཟོད་པར༌[^2618]གསོལ་བ་དང་ལྡན་ན་གསོལ་བས་བཟློག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ཁྱིམ་བདག་དེ་བཟོད་པར་གསོལ་བར་བྱེད་ན། དགེ་སློང་དེ་ལ་གསོལ་བ་འབའ་ཞིག་གི༌[^2619]ལས་ཀྱིས་ལྷུང་བཟེད་ཕྱིར་བཟློག་པར་བྱའོ། །

[Block 2783]
བཅབ་པའི་སེམས་མ་སྐྱེས་ན་མཐའ་ལས་ལྡང་བར་འགྱུར་རོ་ཞེས་བྱ་བ་ནི་གང་ལ་བཅབ་པའི་སེམས་གཅིག་ཀྱང་མ་སྐྱེས་ན་དེ་ཕམ་པར་འགྱུར་བའི་ལྟུང་བ་ལས་ལྡང་བར༌[^2620]འགྱུར་བའོ། །

[Block 2784]
ཐབས་གང་གིས་ལྡང་བར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་བསླབ་པ་སྤྱོད་པས་སོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 2785]
བསླབ་པ་སྤྱོད་པ་དེ་དག་གང༌[^2621]གིས་བསྒྲུབ་པར་བྱ་ཞེ༌[^2622]ན། དེའི་ཕྱིར། དེ་ཐོབ་པས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བསླབ་པ་ལ་སྤྱོད་པ་ཐོབ་པས་བསྒྲུབ་པར་བྱའི་མ་ཐོབ་པས༌[^2623]མ་ཡིན་ནོ། །སུ་ལས་ཐོབ་པ་ཞེ་ན། དེའི་ཕྱིར། དགེ་འདུན་ལས་སོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 2786]
དགེ་འདུན་གྱིས༌[^2624]དེ་ལ་ཇི་ལྟར་སྦྱིན་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར། ལས་ཀྱིས༌[^2625]སྦྱིན་ནོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 2787]
དུས་ཇི་སྲིད་དུ་ཞེ་ན། དེའི་ཕྱིར། ཇི་སྲིད་འཚོ་བའི་བར་དུའོ་ཞེས་བྱ་བ་སྨོས་ཏེ་འདིར་གཞུང་ནི་ཇི་ལྟར་དེ་སྙོམས་པར་ཞུགས་པ་ལ་དེ་ལྟར་དགྲ་བཅོམ་པ་ཉིད་བག་ཡངས་སུ༌[^2626]སྦྱོར་བའོ། །

[Block 2788]
གང་གི་ཚེ་འཁྲུལ་པའི་རྒྱུ་ཟད་ནས་བསྙེན་པར་རྫོགས་པ་ལ་དེའི་ཚེ་ན་ནི་བསླབ་པ་སྦྱིན་པ་ཞེས་མི་བྱ་སྟེ། བསྙེན་པར་རྫོགས་པ་སྔོན་དུ་འགྲོ་བའི་ངོ་བོ་ཞེས་བྱ་བའོ། །

[Block 2789]
འདིར་གཞུང་ནི་ཕྲན་ཚེགས་དག་ལས་འདི་དང་པོར་བྱ་བ་སྟེ་མཐར་སོང་བ་ཞེས་བྱ་བའི་བར་དུ་གསུངས་པ་ཡིན་ནོ། །

[Block 2790]
ངོ་ཚ་དང་ལྡན་པ་དང་། མདོ་སྡེ་འཛིན་པ་དང་། འདུལ་བ་འཛིན་པ་དང་། མ་མོ་འཛིན་པ་དང་། ཤེས་པས་ནི་གཅིག་གི་མདུན་དུ་བཤགས་པས། དགེ་འདུན་ལྷག་མ་ལས་བདག༌[^2627]གོ་ཞེས་བྱ་བ་ལ་འདིས་སྤོ་བར་བྱ་བ་དང་མགུ་བར་བྱ་བ་དག་ལ་རྩོམ་པ༌[^2628]མི་དགོས་པ་ཉིད་ཅེས་བྱ་བ་ཤེས་པར་བྱའོ། །

[Block 2791]
བསམ་པས་ལྟུང་བ་ལས་ལྡང་གི་ཆད་པའི་ལས་ཀྱིས་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་བསམ་པའི༌[^2629]ཁྱད་པར་སྐྱེད་པའི༌[^2630]ཕྱིར་ཆད་པའི་ལས་བྱ་བ་ཡིན་ནོ། །

[Block 2792]
དེ་བས་ན་འདིར་ཆད་པའི་ལས་མེད་པར་བསམ་པའི་ཁྱད་པར་གནས་པ་ཡོད་ན་འདི༌[^2631]དོན་མེད་པར་བྱེད་པ་ཉིད་དོ། །

[Block 2793]
འདིར་གཞུང་ནི་སིལ་བུ་དག་ལས།

[Block 2794]
དེ་ལྟ་བས་ན་གང་དག་རྣམ་པ་དེ་ལྟ་བུར་རང་བཞིན་གྱིས་ངོ་ཚ་ཤེས་པ་དང་ལྡན་པ་དེ་དག་གིས་ནི་གཅིག་གི་མདུན་དུ་བཤགས་པར་རྗེས་སུ་གནང་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ནོ། །

[Block 2795]
ལྟུང་བ་མིང་དང་རིགས་དང་ལྡན་པར་བརྗོད་པར་བྱའོ་ཞེས་གང་ཞིག་གསུངས་པ་དེ་ལ། འདིར་མིང་ནི་རྣམ་པ་ཇི་ལྟ་བུ་ཞིག་ཡིན། རིགས་ནི་རྣམ་པ་ཇི་ལྟ་བུ་ཞིག་ཡིན་པར་ཤེས་པར་བྱ་ཞེ་ན་དེའི་ཕྱིར། འདིར་མིང་ནི་ལྟུང་བྱེད་ཀྱི་སྡེ་ཚན་ལས་མིང་ངོ་། །བྱུང་བ་ནི་རིགས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་ལྟུང་བ་ལས་ལྡང་བ་ལ་སྡེ་ཚན་ལ་བརྟེན་ནས་མིང་དུ་གྲགས་པ་གང་ཡིན་པ་དེ་ནི་མིང་དུ་ཤེས་པར་བྱའོ། །

[Block 2796]
དེ་བས་ན་ཕམ་པར་འགྱུར་བ་དང་དགེ་སློང༌[^2632]ལྷག་མར་ཞེས་བྱ་བ་ལ་སོགས་པས་སོ། །

[Block 2797]
བསམས་བཞིན་དུ་ཁུ་བ་འབྱིན་པ་ལ་སོགས་པ་བྱུང་བ༌[^2633]གང་ཡིན་པ་དེ་ནི་རིགས་ཡིན་པར་ཤེས་པར་བྱའོ། །

[Block 2798]
འདིར་གཞུང་ནི་བཙུན་པ་ལྟུང་བ་རྣམས་ཀྱི༌[^2634]མིང་ཞེས་བགྱི། རིགས་ཞེས་ཀྱང་བགྱི་ན། བཙུན་པ་མིང་གང་ལགས། རིགས་ནི་གང་ལགས། ཉེ་བ༌[^2635]འཁོར་ཕམ་པར་འགྱུར་བ་ཞེས་བྱ་བ་ནི་མིང་ངོ་། །བྱུང་བ་ནི་རིགས་སོ། །

[Block 2799]
དགེ་འདུན་ལྷག་མ་ཞེས་བྱ་བ་ནི་མིང་ངོ་། །ལྟུང་བྱེད་དང༌[^2636]སོ་སོར་བཤགས་པར་བྱ་བ་དང་། ཉེས་བྱས་ཞེས་བྱ་བ་ནི་མིང་ངོ་། །བྱུང་བ་ནི་རིགས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2800]
འདི་ནི་གླེང་གཞི་དག་ལས་ཀོའུ༌[^2637]ཤཱམྦཱི་དང་། དམར་སེར་ཅན་གྱི་གཞི་གཉིས་ལ་ཕྱིར་བཅོས་པའི་གཞི་ཞེས༌[^2638]བྱ་བའི་མིང་གཞན་དུ་བྱས་ཏེ། ཕྱིར་བཅོས་པར་བྱ་བའི་གང་ཟག་གི་བྱེ་བྲག་ཐམས་ཅད་བསྟན་པའི་ཕྱིར། འཐབ་ཀྲོལ་བྱེད་པ་ལ་སོགས་པའི་གང་ཟག་གང་ཇི་སྙེད་ཕྱིར་བཅོས་པར་བྱ་བ་དེ་དག་ཐམས་ཅད་དེ་གཉིས་ཀྱིས༌[^2639]ཕྱིར་བཅོས་པར་བྱ་བ༌[^2640]གསུངས་པས་དེའི་ཕྱིར་དོན་དང་མཐུན་པར་མིང་བསྟན་པར་བྱ་བའི་ཕྱིར་དེ་གཉིས་ལ་ཕྱིར་བཅོས་པའི་གཞི་ཞེས་བྱ་བའི་མིང་དུ་གཞན་དུ་བྱ་སྟེ་དེས་ན༌[^2641]མིང་བརྗོད་པ༌[^2642]ཁོ་ནས་བརྡ་ཕྲད་སླ་བར་འགྱུར་རོ་ཞེས་བྱ་བར་ཤེས་པར་བྱའོ། །

[Block 2801]
ཕྱིར་བཅོས་པའི་གཞི་ཞུ་བ་ལ་སོགས་པའི་སྐབས་སོ། །

[Block 2802]
ཕྱིར་བཅོས་པའི༌[^2643]གཞི་རྫོགས་སོ།། །།

[Block 2803 [HEADING]]
## དུས་དང་དུས་མ་ཡིན་པར་བསྡུས་པ་འབྱུང་བའི་གཞི། ^7-0

[Block 2804]
འདི་ལ་དགེ་འདུན་ལྷག་མར༌[^2644]མི་ཤེས་པ་ཉིད་དང་། བཅབ་པའི་སེམས་མ་བཞག་པས་བརྗེད་པ་དང་། བྱས་སམ་མ་བྱས་ཅི་ཞིག་ཇི་ལྟ་བུ་ཞིག་ཅེས་དྲན་པར་མི་ནུས་པ་ཉིད་དང་། བསྙེན་པར་མ་རྫོགས་པ་ཉིད་དང་། གནས་ནས་ཕྱུང་བ་ཉིད་ལ་འཆབ་པ་མི་འབྱུང་ངོ་ཞེས་བྱ་བ་ནི་འཆབ་པའི་ཉེས་པ་མི་འབྱུང་ངོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2805]
གང་གི༌[^2645]ཕྱིར་ཤེས་ཏེ་སྦས་ན་ནི་འཆབ་པར་འགྱུར་རོ། །
--- END BLOCKS ---
