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
[Block 946]
སྐྱེ་བ་ནི་མོ་དང་ཕོའི་དབང་པོ་དག་ཡིན་ཏེ། དེ་ལས་སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 947]
གནས་པ་ནི་སྲོག་གི་དབང་པོ་ཡིན་ཏེ། དེས་གནས་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 948]
ཚོར་བ་རྣམས་ཀྱིས་ནི་ཉེ་བར་སྤྱོད་པར་བྱེད་དེ། དེའི་ཕྱིར་དེ་དག་ནི་དབང་པོ་བཅུ་བཞི་ཡིན་ནོ། །

[Block 949]
རྣམ་པ་དེ་ཉིད་ཀྱིས་གཞན་དག་ནི་ལྡོག་པ་ཡིན་ཏེ། ལྡོག་པའི་རྟེན་ནི་དད་པ་ལ་སོགས་པ་ཡིན་ནོ། །

[Block 950]
སྐྱེ་བ་ནི་ཀུན་ཤེས་པར་བྱེད་པའི་དབང་པོ་ཡིན་ནོ། །

[Block 951]
གནས་པ་ནི་ཀུན་ཤེས་པའི་དབང་པོ་ཡིན་ནོ། །

[Block 952]
ཀུན་ཤེས་པ་དང་ལྡན་པའི་དབང་པོས་ནི་ཉེ་བར་སྤྱོད་པར་བྱེད་དོ་ཞེས་ཟེར་ཏེ། དེའི་ཕྱིར་དབང་པོ་དག་ནི་དེ་སྙེད་ཅིག་ཡིན་ལ། དེ་ཉིད་ཀྱི་ཕྱིར་དེ་དག་གི་གོ་རིམས་ཀྱང་དེ་ཡིན་ནོ། །

[Block 953]
ངག་གི་ཚིག་སྨྲ་བར་བྱ་བ་ལ་དབང་པོ་ཉིད་མ་ཡིན་ཏེ། སློབ་པའི་ཁྱད་པར་ལྟོས་པའི་ཕྱིར་རོ། །

[Block 954]
ལག་པ་དང་། རྐང་པ་དང་། ལེན་པ་དང་། འགྲོ་བ་ལས་གཞན་མ་ཡིན་པའི་ཕྱིར་ཏེ། དེ་དག་ཉིད་དེ་དག་ཡིན་ཏེ། གཞན་དང༌[^417]གཞན་དུ་འབྱུང་བ་ལ་ལེན་པ་དང་འགྲོ་བ་ཞེས་བྱའོ། །

[Block 955]
སྦྲུལ་ལ་སོགས་པ་ལ༌[^418]ལག་པ་དང་། རྐང་པ་མེད་པ༌[^419]བཞིན་དུ་ཡང་ལེན་ཞིང་འགྲོ་བའི་ཕྱིར་རོ། །

[Block 956]
རྐུབ་ཀྱང་རྟུག་པར་བྱ་བ་ལ་དབང་པོ་ཉིད་མ་ཡིན་ཏེ། ནམ་མཁའ་ལ་གནས་པའི་རྫས་ལྕི་བ་ཐམས་ཅད་དུ་ལྟུང་བའི་ཕྱིར་དང་། དེ་རླུང་གིས་ཀྱང་བྲོ་བར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 957]
མདོམས༌[^420]ཀྱང་ཀུན་ཏུ་དགའ་བར་བྱ་བ་ལ་དབང་པོ་ཉིད་མ་ཡིན་ཏེ། དགའ་བ་དེ་ནི་མོ་དང་ཕོའི་དབང་པོས་བྱས་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 958]
ལྐོག་མ་དང་། སོ་དང་། མིག་གི་ལམ་དང་ཚིགས་རྣམས་ཀྱང་མིད་པ་དང་། བཅའ་བ་དང་། འབྱེད་པ་དང་། འཛུམས་པ་དང་། བསྐུམས་པ༌[^421]དང་། བརྐྱང་བའི་བྱ་བ་དག་ལ་དབང་པོ་ཉིད་ཡིན་པའམ། རྒྱུར་གྱུར་པ་ཐམས་ཅད་རང་གི་བྱ་བ་ལ་དབང་པོ་ཉིད་ཡིན་པར་ཐལ་བར་འགྱུར་བས་ངག་ལ་སོགས་པ་དབང་པོ་ཉིད་ཡིན་པར་རིགས་པ་མ་ཡིན་ནོ། །

[Block 959]
དེ་ལ་མིག་ལ་སོགས་པ་ཕོའི་དབང་པོ་ལ་ཐུག་པ་རྣམས་ནི་བསྟན་ཟིན་ཏོ། །

[Block 960]
སྲོག་གི་དབང་པོ་ནི་ལྡན་པ་མ་ཡིན་པ་ཡིན་པའི་ཕྱིར་ལྡན་པ་མ་ཡིན་པ་དག་གི་ནང་ཁོ་ན་ནས་འཆད་པར་འགྱུར་རོ། །

[Block 961]
དད་པ་ལ་སོགས་པ་རྣམས་ནི་སེམས་ལས་བྱུང་བ་དག་གི་ནང་ནས་འཆད་པར་འགྱུར་རོ། །

[Block 962 [HEADING]]
#### བདེ་བ་ལ་སོགས་པ་དང་ཀུན་ཤེས་པར་བྱེད་པའི་དབང་པོ་ལ་སོགས་པ། ^2-1-3-0

[Block 963]
བདེ་བ་ལ་སོགས་པ་དང་ཀུན་ཤེས་པར་བྱེད་པའི་དབང་པོ་ལ་སོགས་པ་བཤད་པར་བྱ་སྟེ་དེ་བརྗོད་པར་བྱའོ། །

[Block 964]
ལུས་ཚོར་སིམ་པ་མ་ཡིན་གང་། །སྡུག་བསྔལ་དབང་པོའོ། །

[Block 965]
སིམ་པ་མ་ཡིན་པ་ཞེས་བྱ་བ་ནི་གནོད་པར༌[^422]བྱེད་པ་སྟེ་སྡུག་བསྔལ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 966]
སིམ་པ་ནི་བདེ་བའོ། །

[Block 967]
ལུས་ཀྱི་ཚོར་བ་སིམ་པ་ནི་བདེ་བའི་དབང་པོའོ། །

[Block 968]
སིམ་པ་ཞེས་བྱ་བ་ནི་ཕན་འདོགས་པ་སྟེ་བདེ་བ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 969]
བསམ་གཏན་གསུམ་པ་ན། སེམས་ཀྱི་དེ་ནི་བདེ་དབང་པོ། །བསམ་གཏན་གསུམ་པ་ན༌[^423]ནི་སེམས་ཀྱི་ཚོར་བ་སིམ་པ་དེ་ཉིད་བདེ་བའི་དབང་པོ་ཡིན་ཏེ། དེ་ན་རྣམ་པར་ཤེས་པའི་ཚོགས་ལྔ་མེད་པའི་ཕྱིར་ལུས་ཀྱི་ཚོར་བ་ནི་མེད་དོ། །

[Block 970]
གཞན་ན་དེ་ཡིས་བདེ་བ་ཡིན། །བསམ་གཏན་གསུམ་པ་ལས་གཞན་པ་འདོད་པའི་ཁམས་དང་། བསམ་གཏན་དང་པོ་དང་།

[Block 971]
གཉིས་པ་ན་ནི་སེམས་ཀྱི་ཚོར་བ་སིམ་པ་གང་ཡིན་པ་དེ་ཡིད་བདེ་བའི་དབང་པོ་ཡིན་ནོ། །

[Block 972]
བསམ་གཏན་གསུམ་པ་ན་ནི་དགའ་བའི་འདོད་ཆགས་དང་བྲལ་བའི་ཕྱིར་བདེ་བའི་དབང་པོ་ཁོ་ན་ཡིན་གྱི་ཡིད་བདེ་བ་ནི་མ་ཡིན་ཏེ། དགའ་བ་ནི་ཡིད་བདེ་བ་ཡིན་ནོ། །

[Block 973]
སེམས་ཀྱི་སིམ་པ་མ་ཡིན་པ། ཡིད་མི་བདེ་བའོ་བཏང་སྙོམས་ནི་བར་མའོ། །

[Block 974]
སིམ་པ་ཡང་མ་ཡིན་སིམ་པ་མ་ཡིན་པ་ཡང་མ་ཡིན། སྡུག་བསྔལ་ཡང་མ་ཡིན། བདེ་བ་ཡང་མ་ཡིན་པའི་ཚོར་བ་ནི་བར་མ་ཞེས་བྱ་སྟེ། དེ་ནི་བཏང་སྙོམས་ཀྱི་དབང་པོ་ཡིན་ནོ། །

[Block 975]
ཅི་ལུས་ཀྱི་འམ། སེམས་ཀྱི་ཞེས་བྱ་ཞེ་ན། སྨྲས་པ། གཉི་གའི་ཡིན་ནོ། །

[Block 976]
ཅིའི་ཕྱིར་འདི་བསྡུས་ནས་དབང་པོ་གཅིག་ཏུ་བྱས་ཤེ་ན།[^424] མི་རྟག༌[^425]ཕྱིར། སེམས་ཀྱི་བདེ་བ་དང་། སྡུག་བསྔལ་ནི་ཕལ་ཆེར་རྣམ་པར་རྟོག་པ་ལས་སྐྱེའི་ལུས་ཀྱི་ནི་མ་ཡིན་ནོ། །

[Block 977]
ཡུལ་གྱི་དབང་གིས་ནི་དགྲ་བཅོམ་པ་རྣམས་ལ་ཡང་སྐྱེ་བས། དེའི་ཕྱིར་དེ་དག་དབང་པོ་ཉིད་དུ་ཐ་དད་ཀྱི་ལུས་ཀྱི་དང་སེམས་ཀྱི་བཏང་སྙོམས་ནི་རྣམ་པར་མི་རྟོག་པ་ཁོ་ནར་རང་གི་ངང་གིས་སྐྱེ་བས་དབང་པོ༌[^426]གཅིག་ཏུ་བྱས་སོ། །

[Block 978]
ལུས་ཀྱི་བདེ་བ་ཡང་གཞན་དུ་ཕན་འདོགས་ལ། སེམས་ཀྱི་ཡང་གཞན་དུ་ཕན་འདོགས་སོ། །

[Block 979]
དེ་བཞིན་དུ་ལུས་ཀྱི་སྡུག་བསྔལ་ཡང་གཞན་དུ་གནོད་པ་བྱེད་ལ། སེམས་ཀྱི་ཡང་གཞན་དུ་གནོད་པ་བྱེད་དོ། །

[Block 980]
བཏང་སྙོམས་ལ་ནི་བྱེ་བྲག་དེ་མེད་དེ། དེ་བས་ན། བཏང་སྙོམས་ནི་བྱེ་བྲག་མེད་པས་ཐ་དད་པ་མེད་དོ། །

[Block 981]
མཐོང་བསྒོམ་མི་སློབ་ལམ་ལ་དགུ། །གསུམ་ཡིན། ཡིད་དང་། བདེ་བ་དང་། ཡིད་བདེ་བ་དང་། བཏང་སྙོམས་རྣམས་དང་། དད་པ་ལ་སོགས་པ་ལྔ་དང་དབང་པོ་དགུ་པོ་དེ་དག་ནི་ལམ་གསུམ་དག་ཏུ་དབང་པོ་གསུམ་ཞེས་བྱ་སྟེ། མཐོང་བའི་ལམ་ལ་ནི་མི་ཤེས་པ་ཀུན་ཤེས་པར་བྱེད་པའི་དབང་པོ་ཞེས་བྱའོ། །

[Block 982]
བསྒོམ་པའི་ལམ་ལ་ནི་ཀུན་ཤེས་པའི་དབང་པོ་ཞེས་བྱའོ། །

[Block 983]
མི་སློབ་པའི་ལམ་ལ་ནི་ཀུན་ཤེས་པ་དང་ལྡན་པའི་དབང་པོ་ཞེས་བྱའོ། །ཅིའི་ཕྱིར་ཞེ་ན། མཐོང་བའི་ལམ་ལ་ནི་མི་ཤེས་པ་ཀུན་ཤེས་པར་བྱ་བར་ཞུགས་པ་ཡིན་ནོ། །

[Block 984]
བསྒོམ་པའི་ལམ་ལ་ནི་སྔོན་མ་མཐོང་བ་ཀུན་ཤེས་པར་བྱ་བ་ནི་མེད་ཀྱི། ཕྲ་རྒྱས་ལྷག་མ་སྤང་བར་བྱ་བའི་ཕྱིར་དེ་ཉིད་ཀུན་ཤེས་པར་བྱེད་དོ། །

[Block 985]
མི་སློབ་པའི་ལམ་ལ་ནི་ཀུན་ཤེས་སོ་སྙམ་དུ་རྟོགས་པ་ནི་ཀུན་ཤེས་པ་སྟེ། དེ་འདི་ལ་ཡོད་པས་སམ། འདི་ཀུན་ཤེས་པ་སྲུང་བའི་ངང་ཚུལ་ཅན་ཡིན་པས་ན་ཀུན་ཤེས་པ་དང་ལྡན་པའོ། །
--- END BLOCKS ---
