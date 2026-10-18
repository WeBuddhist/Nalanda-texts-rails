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
[Block 1646]
ཚེ་ཟད་པར་འཆི་བར་འགྱུར་ལ་བསོད་ནམས་ཟད་པས་མ་ཡིན་པ་ཡང་ཡོད་ཅེས་བྱ་བ་མུ་བཞི༌[^760]གསུངས་ཏེ། མུ་དང་པོ་ནི་ཚེ་རྣམ་པར་སྨིན་པ་ཅན་གྱི་ལས་ཡོངས་སུ་གཏུགས་པ་ལས་སོ། །

[Block 1647]
གཉིས་པ་ནི༌[^761]ལོངས་སྤྱོད་རྣམ་པར་སྨིན་པ་ཅན་གྱི་ལས་ཡོངས་སུ་གཏུགས་པ་ལས་སོ། །

[Block 1648]
གསུམ་པ་ནི་གཉི་གའོ། །

[Block 1649]
བཞི་པ་ནི་ཡ་ང་བ་ཡོངས་སུ་མ་སྤངས༌[^762]སོ། །

[Block 1650]
ཚེ་བཏང་བ་ལས་ཀྱང་བརྗོད་པར་བྱའོ། །

[Block 1651]
ཚེ་ཟད་ན་བསོད་ནམས་ཟད་པ་འཆི་བར་བྱ་བ་ལ་ནུས་པ་མེད་དོ། །

[Block 1652]
[^763]དེ་ལྟ་བས་ན་གཉི་ག་ཟད་ན་གཉི་ག་ཟད་པ་ལས་འཆི་བར་བཤད་དོ། །

[Block 1653]
ཡེ་ཤེས་ལ་འཇུག་པ་ལས།

[Block 1654]
ཚེ་རྒྱུད་ལ་རག་ལུས་ཏེ་འཇུག་པ་ཞེས་བརྗོད་པར་བྱའམ། ལན་ཅིག་སྐྱེས་ནས་གནས་པ་ཞེས་བརྗོད་པར་བྱ། སྨྲས་པ། འདོད་པ་ན་སྤྱོད་པའི་སེམས་ཅན་འདུ་ཤེས་མེད་པའི་སྙོམས་པར་འཇུག་པ་དང་། འགོག་པའི་སྙོམས་པར་འཇུག་པ་ལ་སྙོམས་པར་མ་ཞུགས་པ་རྣམས་ཀྱི་ནི་རྒྱུད་ལ༌[^764]རག་ལུས་ཏེ། འཇུག་པ་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 1655]
སྙོམས་པར་ཞུགས་པ་རྣམས་དང་། གཟུགས་དང་། གཟུགས་མེད་པ་ན་སྤྱོད་པའི་སེམས་ཅན་རྣམས་ཀྱི་ནི་ལན་ཅིག་སྐྱེས་ནས་གནས་པ་ཞེས་བརྗོད་པར་བྱའོ་ཞེས་གསུངས་པ་བཤད་པ་འདིའི་དོན་གང་ཡིན་ཞེ་ན། གང་ལ་ལུས་ལ་གནས་པས༌[^765]གནོད་པར་འགྱུར་བ་དེ་ནི་རྒྱུད་ལ་རག་ལུས་པའི་ཕྱིར་དང་པོ་ཡིན་ནོ། །

[Block 1656]
གང་གི་ལུས་ལ་གནོད་པ་ཉིད་མེད་པ་དེ་ནི་ཇི་ལྟར་སྐྱེས་པ་བཞིན་དུ༌[^766]གནས་པའི་ཕྱིར་གཉིས་པ་ཡིན་ནོ། །

[Block 1657]
ཁ་ཆེ་བ་རྣམས་ན་རེ་གློ་བུར་དང་བཅས་པ་ནི་དང་པོ་ཡིན་ནོ། །

[Block 1658]
གློ་བུར་མེད་པ་ནི་གཉིས་པ་ཡིན་ནོ་ཞེས་ཟེར་ཏེ། དེ་ལྟ་བས་ན་དུས་མ་ཡིན་པར་འཆི་བ་ནི་ཡོད་དོ། །

[Block 1659]
མདོ་ལས་ལུས་ཐོབ་པ་ནི་བཞི་སྟེ། ལུས་ཐོབ་པ༌[^767]གང་ལ་བདག་ཉིད་འཆི་བར་འགྱུར་གྱི་གཞན་གྱིས༌[^768]གསོད་པས་མ་ཡིན་པ་ཡང་ཡོད་ཅེས་བྱ་བ་མུ་བཞིར༌[^769]གསུངས་པ། འདོད་པའི་ཁམས་ན་ལྷ་རྩེད་མོས་མྱོས་པ་རྣམས་དང་། ཡིད་རབ་ཏུ་འཁྲུགས་པ་རྣམས་ནི་བདག་ཉིད་འཆི་བ་ཁོ་ནར་འགྱུར་བ་ཡིན་ཏེ། དེ་རྣམས་ནི་རབ་ཏུ་དགའ་བ་དང་ཡིད་རབ་ཏུ་འཁྲུགས་པ་དག་གི༌[^770]གནས་དེ་ནས་འཆི་འཕོ་བར་འགྱུར་གྱི་གཞན་དུ་ནི༌[^771]མ་ཡིན་ནོ། །

[Block 1660]
སངས་རྒྱས་རྣམས་ཀྱི་ཡང་ཡིན་པར་བརྗོད་པར་བྱ་སྟེ། བདག་ཉིད་འགྲོངས་པའི་ཕྱིར་རོ། །

[Block 1661]
མངལ་དང་སྒོ་ང་ན་འདུག་པ་རྣམས་ནི་གཞན་གྱིས་གསོད་པ་ཁོ་ནར་འགྱུར་བ་ཡིན་ནོ། །

[Block 1662]
འདོད་པ་ན་སྤྱོད་པ་རྣམས་གཞན་དག་ཕལ་ཆེར་ནི་གཉི་ག་ཡིན་ནོ། །

[Block 1663]
སྲིད་པ་བར་མ་པ་ཐམས་ཅད་དང་། གཟུགས་དང་གཟུགས་མེད་པ་ན་སྤྱོད་པ་རྣམས་དང་། འདོད་པ་ན་སྤྱོད་པ་ཁ་ཅིག་འདི་ལྟ་སྟེ་དམྱལ་བ་པ་རྣམས་དང་། བྱང་གི་སྒྲ་མི་སྙན་པ་རྣམས་དང་། མཐོང་བའི་ལམ་དང་། བྱམས་པ་དང་འགོག་པ་དང་། འདུ་ཤེས་མེད་པའི་སྙོམས་པར་འཇུག་པ་ལ་སྙོམས་པར་ཞུགས་པ་རྣམས་དང་། རྒྱལ་པོའི་དྲང་སྲོང་དང་། རྒྱལ་པོའི་ཕོ་ཉ་དང་། རྒྱལ་བས་བསྟན་པ་དང་། [^772]ཆོས་ལེན་པ༌[^773]དང་། མཆོག་ཅན་དང་། གང་ལ་ལེན་པ༌[^774]དང་། ཚོང་དཔོན་གྱི་བུ་གྲགས་པ་གཞོན་ནུ་དང་། འཚོ་བྱེད་ལ་སོགས་པ་རྣམས་དང་། སྲིད་པ་ཐ་མ་པའི༌[^775]བྱང་ཆུབ་སེམས་དཔའ་རྣམས་དང་། བྱང་ཆུབ་སེམས་དཔའི་ཡུམ་དེ་ལྷུམས་ན་གནས་པ་དང་། འཁོར་ལོས་སྒྱུར་བ༌[^776]དང་། འཁོར་ལོས་སྒྱུར་བའི་མ་དེ་མངལ་ན་གནས་པ༌[^777]གཉི་ག་མ་ཡིན་ནོ། །

[Block 1664]
ཡང་ཅིའི་ཕྱིར་མདོ་ལས།

[Block 1665]
བཙུན་པ་གང་དག་བདག་ཉིད་འགུམ་པར་ཡང་མི་འགྱུར་ལ༌[^778]གཞན་གྱིས་གསོད་པ་ཡང་མ་ལགས་པའི་སེམས་ཅན་དེ་དག་གང་ལགས། ཤཱ་རིའི་བུ་འདུ་ཤེས་མེད་འདུ་ཤེས་མེད་མིན་གྱི༌[^779]སྐྱེ་མཆེད་དུ་ཉེ་བར་འགྲོ་བ་རྣམས་ཡིན་ནོ་ཞེས་གསུངས་ཤེ་ན། བསམ་གཏན་དང་གཟུགས་མེད་པ་གཞན་དག་ནི་བདག་ཉིད་འཆི་བ་ནི་རང་གི་ས་པའི་འཕགས་པའི་ལམ་ཡིན་ལ། གཞན་གྱིས་གསོད་པ་ནི་ས་གོང་མའི་ཉེར་བསྡོགས་ཡིན་གྱི། དེ་ན་ནི་གཉི་ག་མེད་དོ་ཞེས་ཟེར་རོ་ཞེས་གྲག་གོ། །

[Block 1666]
དེ་ལྟ་ན་འོ་ན་དེ་ན་ཡང་གཞན་གྱི་ས་པའི་འཕགས་པའི་ལམ་གཞན་གྱིས་གསོད་པར་འགྱུར་བ་མ་ཡིན་ནམ་ཞེ་ན། འོ་ན་ནི་མཐར་སྨོས་པས་དེ་ལ་སོགས་པ་གོའོ། །

[Block 1667]
ལ་ལར་ནི་མཐའ་ཡང་དང་པོས་གོ་སྟེ། འདི་ལྟ་སྟེ་ཚངས་རིས་ཀྱི་ལྷ་དག་ལྟ་བུ་སྟེ། འདི་ནི་བདེ་བ་སྐྱེ་བ་དང་པོ་ཡིན་ནོ་ཞེས་གང་བཤད་པ་ལྟ་བུའོ། །

[Block 1668]
ལ་ལར་ནི་དང་པོ་ཡང་མཐས༌[^780]གོ་སྟེ། འདི་ལྟ་སྟེ། འོད་གསལ་བའི་ལྷ་རྣམས་ལྟ་བུ་སྟེ། འདི་ནི་བདེ་བ་སྐྱེ་བ་གཉིས་པ་ཡིན་ནོ་ཞེས་གང་བཤད་པ་ལྟ་བུའོ། །

[Block 1669]
འདིར་ནི་འདི་ལྟ་སྟེ་ཞེས་བྱ་བའི་སྒྲ་འདི་དཔེར་ན༌[^781]བརྗོད་པ་ཡིན་པས་འདི་ལས་ལྷག་མ་གོ་བར་ཡང་རིགས་ཏེ།[^782] དཔེའི་ཆོས་ནི་གང་གཅིག་ཡིན་ཡང་དེ་དང་འདྲ་བ་ཡང་སྟོན་པར་བྱེད་པ་འདི་ཡིན་ནོ། །

[Block 1670]
འདི་ལྟ་སྟེ་ཞེས་བྱ་བའི་སྒྲ་དེ་ཡང་འདི་ན་མེད་པས་འདི་ནི་ཉེ་བར་སྦྱར་དུ་མི་རུང་ངོ་། །གལ་ཏེ་འདི་ལྟ་སྟེ་ཞེས་བྱ་བའི་སྒྲ་འདི་དཔེར་བརྗོད་པ་ཡིན་ན་ནི་སེམས་ཅན་ལུས་ཐ་དད་ཅིང་འདུ་ཤེས་ཐ་དད་པ་དག༌[^783]ཀྱང་ཡོད་དེ། འདི་ལྟ་སྟེ་མི་རྣམས་དང་ལྷ་ཁ་ཅིག་གོ་ཞེས་བྱ་བ་འདིར་ཐོབ་པར་མི་འགྱུར་ཏེ། དེ་ལྟ་བས་ན་འདི་ནི་ཉེ་བར་བསྟན་པའི་དོན་ཁོ་ནར་བལྟ་བར་བྱའོ། །

[Block 1671]
ཧ་ཅང་ཐལ་བས་ཆོག་གོ། །

[Block 1672]
སྲོག་བཤད་ཟིན་ཏོ། །

[Block 1673 [HEADING]]
#### འདུས་བྱས་ཀྱི་མཚན་ཉིད། ^2-3-7-0

[Block 1674 [VERSE]]
མཚན་ཉིད་དག་ནི་སྐྱེ་བ་དང་། །
རྒ་དང་གནས་དང་མི་རྟག་ཉིད། །

[Block 1675]
བཞི་པོ་འདི་རྣམས་ནི་འདུས་བྱས་ཀྱི་མཚན་ཉིད་དག་ཡིན་ཏེ། གང་ལ་འདི་དག་ཡོད་པའི་ཆོས་དེ་ནི་འདུས་བྱས་སུ་མངོན་ནོ། །

[Block 1676]
བཟློག་པ་ནི་འདུས་མ་བྱས་སོ། །

[Block 1677]
དེ་ལ་སྐྱེ་བས་ནི་ཆོས་དེ་སྐྱེད་པར་བྱེད་དོ།[^784] །གནས་པས་ནི་གནས་པར་བྱེད་དོ། །

[Block 1678]
རྒ་བས་ནི་རྙིངས་པར་བྱེད་དོ། །

[Block 1679]
མི་རྟག་པ་ཉིད་ཀྱིས་ནི་འཇིག་པར་བྱེད་དོ། །

[Block 1680]
མདོ་ལས་གསུམ་པོ་འདི་དག་ནི་འདུས་བྱས་ཀྱི༌[^785]མཚན་ཉིད་ཡིན་ནོ་ཞེས་གསུངས་པ་མ་ཡིན་ནམ། དེར་བཞི་པ་ཡང་བརྗོད་པར་བྱ་དགོས་པར་འགྱུར་རོ། །

[Block 1681]
དེར་གང་ཞིག་མ་གསུངས།

[Block 1682]
སྨྲས་པ། གནས་པའོ། །

[Block 1683]
འོ་ན་ནི་གནས་པ་གཞན་དུ་འགྱུར་བ་ཞེས་བྱ་བ་གང་ཡིན་པ་འདི་ཡིན་ནོ། །

[Block 1684]
འདི་ནི་རྒ་བའི་རྣམ་གྲངས་ཡིན་ཏེ། དཔེར་ན་སྐྱེ་བའི་འབྱུང་བ་ཞེས་བྱ་བ་དང་། མི་རྟག་པ་ཉིད་ཀྱི་འཇིག་པ་ཞེས་བྱ་བ་བཞིན་ནོ། །

[Block 1685]
མདོ་ལས་ནི་ཡིད་འབྱུང་བར་བྱ་བའི་ཕྱིར་ཆོས་གང་དག་འདུ་བྱེད་རྣམས་ཀྱི་དུས་འཕོ་བར་བྱ་བའི་ཕྱིར་ཞུགས་པ་དེ་དག་ཉིད་མཚན་ཉིད་དུ་གསུངས་ཏེ། སྐྱེ་བས་ནི་འདུ་བྱེད་རྣམས་མ་འོངས་པའི་དུས་ནས་ད་ལྟར་བྱུང་བའི་དུས་སུ་སྐྱེད་པར་བྱེད་དོ། །
--- END BLOCKS ---
