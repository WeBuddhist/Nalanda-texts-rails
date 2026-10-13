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
[Block 4026]
འདི་དག་ཇི་ལྟར་འཐོབ་ཅེ་ན། མ་འདྲིས་པ་རྣམས་ནི་སྦྱོར་བས། ཐོབ་བྱ་འདྲིས་པ་ཆགས་བྲལ་བས། །མངོན་པར་ཤེས་པ་ནི་ཚེ་རབས༌[^1560]གཞན་ན་གོམས་པ་རྣམས་ནི་འདོད་ཆགས་དང་བྲལ་བས་འཐོབ་བོ། །

[Block 4027]
གསུམ་པ་དྲན་པ་ཉེར་གཞག་གསུམ། །ཚོར་བ་དང་། སེམས་དང་ཆོས་དྲན་པ་ཉེ་བར་གཞག་པ་གསུམ་མོ། །

[Block 4028]
དང་པོ་རྫུ་འཕྲུལ་རྣ་བ་མིག །རྫུ་འཕྲུལ་དང་། ལྷའི་རྣ་བ་དང་། །མིག་གི་མངོན་པར་ཤེས་པ་ནི་ལུས་དྲན་པ་ཉེ་བར་གཞག་པའིའོ། །

[Block 4029]
ལྷག་མ་དག་ནི་དམིགས་ཀྱིས་མ་ཕྱེ་བའི་ཕྱིར་དྲན་པ་ཉེ་བར་གཞག་པ་བཞི་ཆར་གྱི་རང་བཞིན་ཡིན་ནོ་ཞེས་བྱ་བར་གྲུབ༌[^1561]པོ། །

[Block 4030 [VERSE]]
མིག་དང་རྣ་བའི་མངོན་ཤེས་ནི། །
ལུང་དུ་མ་བསྟན་ལྷག་རྣམས་དགེ། །

[Block 4031]
མིག་དང་རྣ་བའི་མངོན་པར་ཤེས་པ་དག་ནི་དེ་དག་དང་མཚུངས་པར་ལྡན་པའི་ཤེས་རབ་དག་ཡིན་ནོ། །

[Block 4032]
དེ་དག་ནི་གཙོ་བོ་འམ་ཕལ་ཆེ་བ་བསྟན་པ་ཡིན་ནོ། །

[Block 4033 [HEADING]]
##### རིག་པ་གསུམ། ^7-6-5-1-0

[Block 4034]
མངོན་པར་ཤེས་པ་འདི་རྣམས་ལས། །

[Block 4035]
གསུམ་ནི་རིག་པ། སྔོན༌[^1562]གྱི་གནས་དང་། འཆི་འཕོ་བ་དང་། སྐྱེ་བ་ཤེས་པ་དང་། ཟག་པ་ཟད་པའི་མངོན་པར་ཤེས་པ་རྣམས་ནི་མི་སློབ་པའི་རིག་པ་གསུམ་མོ། །ཅིའི་ཕྱིར་དེ་དག་ཁོ་ན་ཡིན་གྱི་གཞན་མ་ཡིན་ཞེ་ན། སྔོན་མཐའ་སོགས། མ་རིག་པ་ནི་བཟློག་ཕྱིར་རོ། །

[Block 4036]
འདི་དག་ནི་སྔོན་དང་། ཕྱི་མའི་མཐའ་དང་། བར་ལ་ཀུན་དུ་རྨོངས་པ་ཟློག༌[^1563]པར་བྱེད་དོ། །

[Block 4037]
དེ་དག་ལས་ཀྱང་དོན་དམ་པར། མི་སློབ་པ༌[^1564]ཐ་མ། ཟག་པ་ཟད་པའི་མངོན་པར་ཤེས་པ་ཉིད་ནི་མི་སློབ་པ་སྟེ། གཉིས་ནི་དེའི། རྒྱུད་ལ་སྐྱེས་ཕྱིར་དེའི་ཞེས་བྱ། །མི་སློབ་པའི་རྒྱུད་ལས་སྐྱེས་པའི་ཕྱིར་མི་སློབ་པ་ཞེས་བརྗོད་དོ། །

[Block 4038]
མངོན་པར་ཤེས་པ་དེ་དག་སློབ་པ༌[^1565]ཡིན་པར་མི་འདོད་དམ་ཞེ་ན།

[Block 4039 [VERSE]]
སློབ་ལ་འདོད་དེ་མི༌[^1566]རིག་དང་། །
བཅས་རྒྱུད་ཕྱིར་ན་རིག་མ་བཤད། །

[Block 4040]
རྒྱུད་ལ་མ་རིག་པ་དང་བཅས་པ་ལ་རིག་པ་གཞག་ཏུ་མི་རུང་སྟེ།

[Block 4041 [HEADING]]
##### ཆོ་འཕྲུལ། ^7-6-5-2-0

[Block 4042 [VERSE]]
ཡང་དེ་ཟིལ་གྱིས་གནོན་པའི་ཕྱིར་རོ། །
མངོན་པར་ཤེས་པ་དེ་དག་ལས། །
དང་པོ་གསུམ་པ་དྲུག་པ་ནི། །

[Block 4043]
ཆོ་འཕྲུལ་རྣམས་ཡིན། རྫུ་འཕྲུལ་དང་། ཀུན་བརྗོད་པ་དང་། རྗེས་སུ་བསྟན་པའི་ཆོ་འཕྲུལ་རྣམས་ཡིན་ནོ། །

[Block 4044]
འདི་དག་གི་ནང་ན། བསྟན་པ་མཆོག །རྗེས་སུ་བསྟན་པའི་ཆོ་འཕྲུལ་ནི་མཆོག་སྟེ།

[Block 4045 [VERSE]]
མི་འཕྲུལ་ཕྱིར་དང་ཕན་པ་དང་། །
ཡིད་འོང༌[^1567]འབྲས་ལ་སྦྱོར་བྱེད་ཕྱིར། །

[Block 4046 [HEADING]]
##### རྫུ་འཕྲུལ། ^7-6-5-3-0

[Block 4047]
རྫུ་འཕྲུལ་ཅི་ཞེ་ན། རྫུ་འཕྲུལ་ཏིང༌[^1568]འཛིན། དེས་ཅི་ཞིག་ཡང་དག་པར་འབྱོར་པར་འགྱུར་ཞེ་ན། དེ་ལས་ནི། སྤྲུལ་དང༌[^1569]འགྲོ་བ། དེ་ལ་འགྲོ་བ་ནི་གསུམ་སྟེ། སྟོན་པ་ལ། ཡིད་མགྱོགས་འགྲོ་བ། ཡུལ་ཐག་རིང་པོར༌[^1570]ཡང་ཐུགས་བསྐྱེད་པའི་དུས་སུ་བྱོན་པའི་ཕྱིར་རོ། །

[Block 4048]
གཞན་དག་ལ། ཕྱིན་བྱེད་མོས་པ་ལས་བྱུང་ཡང་། །ཉན་ཐོས་དང་། རང་སངས་རྒྱས་རྣམས་ནི་ལུས༌[^1571]ཕྱིན་བྱེད་ཀྱི་འགྲོ་བ་ཡང་ཡོད་དེ། བྱ་བ་བཞིན་དུ་རིམ་གྱིས་ལུས་ཕྱིན་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 4049]
མོས་པ་ལས་བྱུང་བ་ཡང་ཡོད་དེ། ཐག་རིང་པོ་ལ་ཉེ་བར་མོས་ནས་མྱུར་དུ་འགྲོ་བའི་ཕྱིར་རོ། །

[Block 4050]
འགྲོ་བ་འདི་དག་ནི་སངས་རྒྱས་ལ་མ་བཤད་ཀྱང་འགྲུབ་པོ། །སྤྲུལ་པ་ནི་རྣམ་པ་གཉིས་ཏེ། དེ་ལ།

[Block 4051 [VERSE]]
འདོད་པར་གཏོགས་པའི་སྤྲུལ་པ་ནི། །
ཕྱི་ཡི་སྐྱེ་མཆེད་བཞི་རྣམ༌[^1572]གཉིས། །

[Block 4052]
བདག་དང་གཞན་གྱི་ལུས་དང་འབྲེལ་བའི་གཟུགས་དང་དྲི་དང་རོ་དང་རེག་བྱའི་སྐྱེ་མཆེད་ཀྱི་རང་བཞིན་ནོ། །

[Block 4053]
གཟུགས་གཏོགས་གཉིས། དེ་ན་དྲི་དང་རོ་མེད་པའི་ཕྱིར་རོ། །

[Block 4054]
དེ་ཡང་རྣམ་པ་གཉིས་ཏེ། འདོད་པའི་ཁམས་ཇི་ལྟ་བར་འདི་ནི་སྤྲུལ་པ་རྣམ་པ་བཞི་ཡིན་ནོ། །

[Block 4055]
གཟུགས་ཀྱི་ཁམས་ན་ཡང་དེ་དང་འདྲ་བས༌[^1573]མདོར་བསྡུ་ན་སྤྲུལ་པ་ནི་རྣམ་པ་བརྒྱད་ཡིན་ནོ། །

[Block 4056]
དེ་ཡང་སྤྲུལ་པ་ནི་སྤྲུལ་སེམས་དག་གིས།

[Block 4057 [VERSE]]
དེ་དག་ཀྱང་ནི་བཅུ་བཞིའོ། །
བསམ་གཏན་འབྲས་གཉིས་ལྔ་ཡི་བར། །

[Block 4058]
རིམ་བཞིན། བསམ་གཏན་དང་པོའི་འབྲས་བུ་ནི་གཉིས་ཏེ། འདོད་པའི་ཁམས་དང་། བསམ་གཏན་དང་པོའི་ས་པ་དག་སྟེ། དེ་བཞིན་དུ་བསམ་གཏན་བཞི་པའི་བར་དག་ཀྱང་བཞི་དང་ལྔར་སྦྱར་བར་བྱའོ། །

[Block 4059]
བསམ་གཏན་གྱི་འབྲས་བུ་སྤྲུལ་པའི་སེམས་ནི་རང་གི་ས་དང་ས་འོག་མ་པ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 4060]
གོང་མ་ལས་སྐྱེས་མིན། ས་གོང་མའི་སྤྲུལ་པའི་སེམས་ནི་བསམ་གཏན་འོག་མའི་འབྲས་བུར་མེད། [^1574]དེ་རྙེད་བསམ་གཏན་བཞིན། ཡང་ཅི་སྤྲུལ་པའི་སེམས་ཁོ་ན་ལས་ལྡང་བར་འགྱུར་རམ་ཞེ་ན། དེ་ལྟ་བུ་ནི་མེད་དེ། དེ་ནི།

[Block 4061]
ངག་དང་རང་ས་ལས།

[Block 4062]
སྐྱེ་བར་འགྱུར་ཏེ། སྤྲུལ་པའི་སེམས་ནི་བསམ་གཏན་དག་པ་པའི་མཇུག་ཐོགས་སུ་སྐྱེ་བའམ། སྤྲུལ་པའི་སེམས་ཀྱི་མཇུག་ཐོགས་སུ་སྐྱེའོ། །

[Block 4063]
དེ་ལས་གཉིས། བསམ་གཏན་དག་པ་པ་དང་སྤྲུལ་པའི་སེམས་དག་སྐྱེའོ། །

[Block 4064]
སྤྲུལ་པའི་སེམས་ཐམས་ཅད་ཀྱང་།

[Block 4065 [VERSE]]
རང་གི་ས་པས་སྤྲུལ་བར་བྱེད། །
ས་གཞན་པ་ཡིས་ནི་མ་ཡིན་ནོ། །
སྨྲར་འཇུག་པ་ནི་འོག་མས་ཀྱང་། །
--- END BLOCKS ---
