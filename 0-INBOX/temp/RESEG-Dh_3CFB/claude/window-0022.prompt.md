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
[Block 771]
དེ་མི་སྣང་བས་ཀྱང་ལྷག་པར་ཞེན་པའི་འཁྲུལ་པས་འཇིག་རྟེན་ཐ་སྙད་འདོགས་པར་བྱེད་དོ། །

[Block 772]
དེ་ལ་སྣང་བའི་རྣམ་པ་དེ་དོན་རྣམས་ལ་མེད་དེ། ཐ་དད་པའི་ཐ་མི་དད་པ་ནི་མ་གཏོགས་སོ། །

[Block 773]
དེ་ནི་མེད་པའི་ངོ་བོ་ཡིན་ཏེ། དེས་དེ་ཁོ་ན་འཛིན་པ་ན་དེ་ལྟར་བསླད་པར་འགྱུར་རོ་ཞེས་སྔར་བཤད་ཟིན་ཏོ། །

[Block 774]
གཞན་ཡང་སྤྱི་དངོས་པོར་སྨྲ་བའི། །ལྟར་ན་ཡང་གསལ་བ་རྣམས་ཐ་དད་པ་ཁོ་ན་ཡིན་ན་ཇི་ལྟར་དེ་དག་ལ་བློ་རྣམ་པ་ཐ་མི༌[^619]དད་པ་ཅན་ཡིན་ཏེ། ཀླན་ཀ་མཚུངས་སོ། །

[Block 775]
མཚུངས་པ་མ་ཡིན་ཏེ། དེ་ལ༌[^620]སྤྱི་ཐ་མི་དད་པའི་ཕྱིར་རོ་ཞེ་ན། དེ་ལ་དེ་ཡོད་ཀྱང་སྣང་བ་མི་རྟོགས་པ་མ་ཡིན་ནམ། དེ་ནི་ཁ་དོག༌[^621]དབྱིབས་སུ་སྣང་བར་ལྡན་པར་ཡིད་ཆེས་སོ། །

[Block 776]
སྤྱི་ནི་དེ་ལྟ་བུ་མ་ཡིན་ནོ།། །།

[Block 777]
བམ་པོ་བཞི་པ། དེ་ལ་མ་གཏོགས་པ་ཐ་མི་དད་པའི་རྣམ་པ་ཡང་འགའ་ཡང་མེད་དོ། །

[Block 778]
རྣམ་པ་སྤྱི་ཡིན་པར་སྨྲ་བའི་ལྟར་ན་ཡང་དེ་ཁྱད་པར་བཞིན་དུ་ཐ་མི་དད་པའི་སྒོ་ནས་དོན་གཞན༌[^622]ལ་མི་འཇུག་པས་ཐ་མི་དད་པའི་ཕྱིར། ཐ་མི་དད་པར་སྣང་བར་མི་རུང་ངོ་། །ཡང་ན་ཡིན་དུ་ཟད་དེ།

[Block 779 [VERSE]]
བློ་ཡི་སྣང་བ་ཐ་དད་དེ། །
དེ་དག་མཚུངས་ཞེས་འཛིན་ཕྱིར་རོ། །

[Block 780]
དེ་དག་ལ་ཐ་མི་དད་པར་སྣང་བ་ནི་མེད་པ་ཁོ་ན་སྟེ། མཚུངས་པ་ཞེས་འཛིན་པའི་ཕྱིར་རོ། །

[Block 781]
གཅིག་ཏུ་སྣང་བ༌[^623]ལ་མཚུངས་སོ་སྙམ་པ་ནི་རིགས་པ་མ་ཡིན་ནོ། །

[Block 782]
འོ་ན་ཅི༌[^624]ཞེ་ན། དེ་ཉིད་འདི་ཡིན་ནོ་སྙམ་མོ། །

[Block 783]
གལ་ཏེ་གཉི་ག་འཛིན་པའི་ཕྱིར་ཉེས་པ་མེད་དོ་ཞེ་ན། འོན་ཀྱང་དེ་འདི་ལའོ་སྙམ་པར་འགྱུར་གྱི་མཚུངས་སོ་སྙམ་པ་ནི་མ་ཡིན་ནོ། །

[Block 784]
གལ་ཏེ་དེ་ཉིད་དེ་དག་གི་མཚུངས་པ་ཡིན་ནོ་ཞེ་ན།[^625] ཇི་ལྟར་གཞན་དང་གཞན་དུ་མཚུངས་པ་ཡིན། གལ་ཏེ་དེ་དག་དང་འབྲེལ་པའི་ཕྱིར་རོ། །

[Block 785]
ཞེ་ན་མ་ཡིན་ཏེ། རག་མ་ལས་པ་ལ་འབྲེལ་པར་མི་རུང་བའི་ཕྱིར་དང་།

[Block 786 [VERSE]]
ཧ་ཅང་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །
གལ་ཏེ་དེ་དག་མཚུངས་ན་ནི། །
ཇི་ལྟར་ཐ་དད་བློས་གཟུང་བྱ། །

[Block 787]
མཚུངས་པའོ་ཞེས་གཟུང་བ་མཐོང་ནས་འདི་དག་ལ་ཐ་མི་དད་པར་སྣང་བ་མ་ཡིན་ནམ་ཞེ་ན། དེ་མཐོང་བ་ལས་ཐ་དད་པ་དང་ཐ་མི་དད་པ་དག་སྣང་བའི༌[^626]ཕྱིར་མཚུངས་པར་གཏོགས་པ་ནི་མ་ཡིན་ནོ། །

[Block 788]
འོ་ན་ཅི་ཞེ་ན། འབྲས་བུ་གཅིག་འདྲ། ཁོ་བོས་ནི་དོན་གྱི་ཤེས་པ་ལ་རྣམ་པ་གཉིས་མ་མཐོང་སྟེ། མ་མཐོང་ན་ཇི་ལྟར་དོན་གཉིས་རབ་ཏུ་བརྟགས་པས་བདག་ཉིད་བསླུ་བར་བྱ། བསལ་བ༌[^627]འབྲས་བུ་གཅིག༌[^628]ཅན་རྣམས་ནི་རྟོག་པའི༌[^629]ཡུལ་དུ་ཉེ་བར་འགྲོ་སྟེ། དེའི་ཕྱིར་འདིས་འཁྲུལ་པས་དེ་ལྟར་བསྲེ་བར༌[^630]བྱེད་དོ། །ཞེས་བྱ་བ་འདི་ནི་སྐྱོན་མེད་དོ། །

[Block 789]
དེ་དག་གི། འབྲས་བློ་དེ་ཡང་ཐ་དད་དོ། །

[Block 790]
དངོས་པོ་རེ་རེ་ལ་དེ་སྣང་བའི་རྣམ་པར་ཤེས་པ་ཡང་དེ་དང་འདྲ་བར་ཐ་དད་པའི་ཕྱིར་རོ།[^631] །ཇི་ལྟར་འབྲས་བུ་གཅིག་པ་ཅན་དག་ཡིན། དེ་དག་གི་འབྲས་བུ་ནི་དེ་ཡིན་ན་དེ་ཡང་ཐ་དད་དོ། །

[Block 791]
བུམ་པ་ལ་སོགས་པའི་འབྲས་བུ་ཆུ་ཆུ༌[^632]བ་ལ་སོགས་པ་གཅིག་པོ་གང་ཡིན་པ་དེ་ཡང་རྫས་རེ་རེའི་ཁྱད་པར་གྱི་ཐ་དད་པ་ཁོ་ན་ཡིན་པས་ཐ་དད་པ་རྣམས་ལ་འབྲས་བུ་གཅིག་པ་མེད་དོ་ཞེ་ན། དེ་ནི་ཉེས་པ་མེད་དེ། འདི་ལྟར།

[Block 792 [VERSE]]
གཅིག་ཏུ་རྟོགས་པའི་རྒྱུ་ཡི་ཕྱིར། །
བློ་ནི་ཐ་དད་མེད་པ་ཡིན། །
བློ་གཅིག་རྒྱུ་ཡི་དངོས་པོ་ཡིས། །
བསལ་བ༌[^633]རྣམས་ཀྱང་ཐ་མི་དད། །

[Block 793]
ཇི༌[^634]ལྟར་དངོས་པོ་རྣམས་ལ་རང་བཞིན་འབྲེལ་པ་མེད་པ་འདི་ཡང་བཤད་ཟིན་ཏེ། [^635]དེ་ལ་བསྲེ་བའི༌[^636]རྣམ་པ་ཅན་གྱི་བློ་ནི་འཁྲུལ་པ་ཁོ་ན་ཡིན་ལ། དེ་ནི༌[^637]དངོས་པོ་ཐ་དད་པ་རིམ་གྱིས་རྣམ་པར་རྟོག་པའི་རྒྱུར་གྱུར་པ་རྣམས་ཀྱི༌[^638]ངོ་བོ་ཉིད་ཀྱིས་བསྐྱེད་དོ། །ཞེས་ཀྱང་བཤད་ཟིན་ཏོ། །

[Block 794]
འདི་དག་གི་ཐ་དད་པ་དེ་བྱེད་པ་མ་ཡིན་པའི་ངོ་བོ་ཉིད༌[^639]ལས་ཐ་དད་པའི་དེ༌[^640]ནི་ཐ་མི་དད་པ་ཞེས་བྱ་སྟེ། ཤེས་པ་ལ་སོགས་པ་གཅིག་འབའ་ཞིག༌[^641]བྱེད་པའི་ཕྱིར་རོ། །

[Block 795]
དེ་ཡང་རྫས་རེ་རེ་ལ་ཐ་དད་ཀྱང་རང་བཞིན་གྱིས་གཅིག་ཏུ་རྟོགས་པ་ཐ་མི་དད་པར་སྙེམས༌[^642]པའི་རྒྱུར་གྱུར་པ་ན་ཐ་མི་དད་པར་སྣང་ངོ་། །རྟོགས་པ༌[^643]དེ་ལྟ་བུའི་རྒྱུ་ཐ་མི་དད་པར་སྣང་པའི་ཤེས་པ་ལ་སོགས་པའི་དོན་གྱི་རྒྱུ་ཡིན་པའི་ཕྱིར། བསལ་བ༌[^644]རྣམས་ཀྱིས་ཀྱང་རང་བཞིན་གྱིས་གཅིག་གི༌[^645]ཤེས་པ་རྣམ༌[^646]པར་བསྲེ་པ༌[^647]རང་གི་ངོ་བོའི་ཁྱད་པར་དོན་དམ་པ་ལ་བརྟེན་པ་ཅན་བསྐྱེད་དོ། །ཞེས་ལན་ཅིག་མ་ཡིན་པར་བཤད་ཟིན་ཏོ། །

[Block 796]
དེ་ལྟ་བས་ན་འབྲས་བུ་གཅིག་པ་ཁོ་ན་དངོས་པོ་རྣམས་ཀྱི་ཐ་མི་དད་པ་ཡིན་ནོ། །

[Block 797]
དེ། དེ་ཡི་འབྲས༌[^648]ཅན་མིན་བྲལ་བ། །ཁོ་ན་ཡིན་ཏེ།

[Block 798 [VERSE]]
དེ་ལས་གཞན་རྗེས་འགྲོ་བ་ཡི། །
དངོས་མ་མཐོང་ཕྱིར་བཀག་པའི་ཕྱིར། །

[Block 799]
ལྟར་རུང་བ་རྣམ་པར་དབྱེ་བར་མི་སྣང་བ་ནི་མེད་དོ་ཞེས་བྱ་བ་དང་། ཡོད་ན་ཡང་གང་ལ༌[^649]ཡང་མི་བརྟེན་ན་ཇི་ལྟར་ཤེས་པའི་རྒྱུ་ཡིན་ཞེས་དེ་ནི་བཤད་ཟིན་ཏོ། །

[Block 800]
བཀག་པ་བྱས་པའི་ཡང་ཕྱིར། [^650]དེར་བརྟག་པ་ནི་རིགས་པ་མ་ཡིན་ནོ། །

[Block 801]
དེའི་ཕྱིར། བརྡ་ནི༌[^651]ཡང་དེ་རིག་དོན་ཅན་ཡིན་པ་ཁོ་ནར༌[^652]རིགས་ཏེ། བརྡ་ཞིག་ཏུ་བྱས་ན་ཡང་དངོས་པོ་རྣམས་ཀྱི་ཕན་ཚུན་ཐ་དད་པ་གང་ཡིན་པ་དེ་ཁོ་ནར༌[^653]ཤེས་པར་བྱ་བའི་ཕྱིར། དེ་མི་བྱེད་པ་ལས་ཐ་དད་པས་འཇུག་པ་ཉིད་དུ་བྱེད་ན་མཛེས་སོ། །

[Block 802]
གལ་ཏེ་དེ་ཤེས་པར་བྱ་བའི་དོན་དུ་བརྡར་འདོགས་པ་མ་ཡིན་ན། དེ་ཐ་སྙད་ཀྱི་དུས་སུ་ཡང་མི་རེག་པའི་ཕྱིར་གཞན་སྤངས་ནས་འཇུག་པར་མི་འགྱུར་ཏེ། དེ་རྣམས་ཀྱི་དེ་དག་ལས་ཐ་དད་པ་དེ་སྒྲས་བརྗོད་པ་ནི་མ་ཡིན་ནོ། །

[Block 803]
མཉན་པ་དེ་ནི།

[Block 804 [VERSE]]
དེ་བྱེད་མིན་ལ་དེ་བྱེད་དང་། །
འདྲ་བའི་ངོ་བོ་སྣང་བ་ཅན། །
དངོས་པོ་ཐ་དད་དངོས་ཙམ་གྱིས། །
ས་བོན་ཅན་དོན་མེད་པའི་བློ། །

[Block 805 [VERSE]]
སྐྱེད་པར་བྱེད་པའང་དེ་མི་བྱེད། །
ཡོངས་སྤོང་ཡན་ལག་ངོ་བོའི་ཕྱིར། །
དངོས་པོ་ཐ་དད་རྟེན༌[^654]ཅན་ཕྱིར། །
དོན་ལ་མི་བསླུ༌[^655]ཡིན་པར་འདོད། །

[Block 806]
དེའི་ཕྱིར༌[^656]གཞན་སེལ་ཡུལ་ཅན་དེ།[^657] །དེ་བྱེད་བརྟེན་པའི་ངོ་བོའི་བྱེད།[^658] །ངོ་བོ་ཉིད་གཅིག་དང་བྲལ་བའི་དོན་རྣམས་ལ་དེ་སྒྲོ་བཏགས་ནས་སྐྱེ་བའི་བློ་ཕྱིན་ཅི་ལོག་ཏུ་སྣང་བའི་ཕྱིར་བྱ་བ་བྱེད་པ་མ་ཡིན་ཡང་དེ་བྱེད་པ་ལྟ་བུར༌[^659]ལྷག་པར་ཞེན་པའི་དངོས་པོ་ཐ་དད་པའི་ངོ་བོ་ཙམ་གྱིས་ས་བོན་ཅན༌[^660]མཚུངས་པ་ཉིད་དུ་ལྷག་པར་ཞེན་པ༌[^661]ཕྱིན་ཅི་ལོག་པ་བསྐྱེད་པའི་མཉན་པ་ཡང་དེ་ལས་གཞན་པའི་ཡོངས་སུ་སྤོང་བའི་ཡན་ལག་གི་ངོ་བོའི་ཕྱིར། དོན་དམ་པར་དེ་ལས་ཐ་དད་པའི་དོན་དག་ལ་མི་སླུ་བ་ཞེས་བྱའོ། །

[Block 807]
འདི་ལྟར་ཐ་དད་པ་དེ་ནི་དེ་དག་ལ་ཡང་དག་པ་ཡིན་ཏེ། རྣམ་པ༌[^662]ཐམས་ཅད་དུ་འདའ་བར་བྱ་བ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 808]
ཐ་དད་པའམ་ཐ་མི་དད་པ་ནི་མ་ཡིན་ཏེ། རྣམ་པ་ཐམས་ཅད་དུ་མི་རུང་བའི་ཕྱིར་རོ། །

[Block 809]
དེ་དངོས་པོ་ལ་འགོད་ན་ནི་སྒྲ་དང་ཤེས་པ་དག་ལས་དངོས་པོ་ཐག་བསྲིངས་པ་ཁོ་ནར་འགྱུར་ཏེ། དེའི་ཡུལ་དུ་འདོད་པ༌[^663]མེད་པའི་ཕྱིར་དང་། དངོས་པོའི་ཆོས་གཞན་ཡང་འགགས་ལ༌[^664]ཡང་རེག་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 810]
དེ་ཉིད་ཀྱི་ཕྱིར་མཉན་པ་དེ་ནི་གཞན་སེལ་བའི་ཡུལ་ཅན་ཞེས་བྱ༌[^665]སྟེ། གཞན་ལོག་པའི་དོན་རྣམས་ལ་བྱེ་བྲག་མེད་པར་ལྡོག་པའི་ཁྱད་པར་ལ་བརྟེན་ནས་བཀོད་པའི༌[^666]ཕྱིར་དང་། ཐ་སྙད་ལ་ཡང་གཞན་སྤངས་ནས་འཇུག་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
