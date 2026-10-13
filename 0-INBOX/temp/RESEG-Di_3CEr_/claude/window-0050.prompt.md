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
[Block 1751]
དེ་ལྟ་ན་རང་གི་དོན་ལ་མི་འཁྲུལ་བ་སྟེ། ཡན་གར་བ་ནི་གཞན་ལ་འཇུག་པ་མ་ཡིན་ནོ། །

[Block 1752]
ཉེས་པ་ཕྱི་མ་ཡང་ཡོད་པ་མ་ཡིན་ཏེ། ཇི་ལྟར་ཞེ་ན། དངོས་འཇུག་ཐ་དད་མིན་ཕྱིར་ཡང་། །དོན་གཞན་ཉེ་བར་ལེན་པའི་སྒྲས་རང་རང་གིས༌[^1375]ཐ་དད་པ་རྣམས་ལ་འཇུག་པ་ནི་མེད་དོ། །

[Block 1753]
དེའི་ཕྱིར་དང་གཞན༌[^1376]གྱི་དབང་གིས་རང་གི་ངང་གིས༌[^1377]ཐ་དད་པ་མི་འཕེན་པའི་ཉེས་པ་མེད་དོ། །

[Block 1754]
ཐ་དད་ཐུག་པ་མེད་ཕྱིར་དང་། །ཁྱབ་པར་བྱེད་པ༌[^1378]མ་ཡིན་པའི་ཕྱིར་རྗོད་པར་བྱེད་པ་མ་ཡིན་པས་སྤྱིའི་ཉེས་པ་ཡང་མེད་དོ། །

[Block 1755]
དོན་གཞན་སེལ་བ་ཙམ་ནི་ཐ་དད་པ་མ་ཡིན་པའི་ཕྱིར་དང་། རྫས་མ་ཡིན་པའི་ཕྱིར་ཡང་ངོ་། །དེ་ཉིད་ཀྱི་ཕྱིར་འདིར་སྤྱིའི་བྱེ་བྲག་གཞན་དང་ལྡན་པ་བཙལ་བར༌[^1379]མི་བྱ་སྟེ། དངོས་སུ་དོན་གཞན་འགེགས་པ་ཡིན་པའི་ཕྱིར་ནའོ། །

[Block 1756]
དེ་ལྟར་སྔར་བརྗོད་པའི་སྐྱོན་མེད་པའི་ཕྱིར་དོན་གཞན་སེལ་བ༌[^1380]ཉིད་སྒྲའི་དོན་ཡིན་ན་མཛེས་སོ། །གང་ལས་ཤེ་ན། རིགས་ཀྱི་ཆོས་རྣམས་རྣམ་པར་གནས། །རིགས་ཀྱི་ཆོས་རྣམས་ཞེས༌[^1381]པ་ནི་གཅིག་ཉིད་དང་། རྟག་པ་ཉིད་དང་། སོ་སོ་བ་ཀུན་ལ་ཁྱབ་པ་རྣམས་ཀྱི་མཚན་ཉིད་བརྟག་པར་བྱ། འདི་ཉིད་ལ་རྣམ་པར་གནས་པ་ཡིན་ཏེ། ཐ་མི་དད་པའི་ཕྱིར་དང་། རྟེན་རྣམ་པར་མ༌[^1382]ཆད་པའི་ཕྱིར་དང་། དོན་མ་ལུས་པ་རྟོགས་པའི་ཕྱིར་རོ་ཞེས་བྱའོ། །

[Block 1757]
དེ་ལྟར་ན་བརྗོད་པའི་ཉེས་པ་མེད་པའི་ཕྱིར་དང་། ཡོན་ཏན་ཡོད་པའི་ཕྱིར་དངོས་པོ་རྣམས་ཀྱི་སྒྲའི་དོན་གཞན་བཟློག་པས་ཁྱད་པར་དུ་བྱས་པ་ཉིད་བརྗོད་དོ། །

[Block 1758 [HEADING]]
### གཞན་སེལ་ངེས་པ། ^5-10-0

[Block 1759]
གལ་ཏེ་དེ་ལྟར་ན། གང་ལས་གཞན་སེལ་ངེས་ཤེ་ན། གལ་ཏེ་གཟུགས་ཀྱི་སྒྲས་རོ་ལ་སོགས་པ་སེལ་གྱི། ཁ་དོག་གིས་ལྷག་པར་མ༌[^1383]བརྗོད་པའི་ཕྱིར་ལྷག་མ་སེལ་དུ་ཟིན་ཀྱང་། ཤིན་ཏུ་ཐ་དད་པ་དེ༌[^1384]ཇི་ལྟར་བྱེད་པ་ཡིན། གང་དག༌[^1385]ཐ་མི་དད་པའི་གཟུགས་ཉིད་འདོད་པ་ལ་ནི་ཉེས་པ་དེ་དག་ཡོད་པ་མ་ཡིན་ཏེ། སྔོན་པོ་ལ་སོགས་པ་ཉིད་རོ་ལ་སོགས་པ་ཡོད་པ་མ་ཡིན་པས་སོ་ཞེ་ན། ཉེས་པ་དེ་ནི་མེད་དེ་འདི་ལྟར། འཇིག་རྟེན་གྲགས་པའི་རྗེས་མི་བཙལ། །བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་། སོ་སོའི་སྐྱེ་བོའི་མིང་ལ་མངོན་པར་ཞེན་པར་མི་བྱ་ཞིང་འཇིག་རྟེན་པའི་མིང་ལ་ཡང་མངོན་པར་མི་རྒྱུག་གོ་ཞེས་གསུངས་སོ། །

[Block 1760]
དེའི་ཕྱིར་ཁོ་བོ་ཅག་གིས་ནི་རྒྱུ་མཚན་ལས་བྱུང་བ་དང་། ཡོངས་སུ་བཤད་པ་ལས་བྱུང་བ་འཇིག་རྟེན་པའི་ཐ་སྙད་དུ་ཡིན་གྱི། ཡང་དག་པའི་དོན་ཉིད་དུ་ཚོལ་བར་མི་བྱེད་དོ།[^1386] །

[Block 1761]
འཇིག་རྟེན་པ་བཞིན་དུ་གོ་བར་བྱ་སྟེ།[^1387] འཇིག་རྟེན་པ་ལ་གཟུགས་ཀྱི་སྒྲ་སྔོན་པོ་ལ་སོགས་པ་ལས༌[^1388]གྲུབ་ཀྱི། །

[Block 1762]
རོ་ལ་སོགས་པ་ནི་མ་ཡིན་ནོ། །དེ་ལྟར་གཟུགས་ཉིད་ལ་མཚུངས་འགྱུར། །

[Block 1763]
གང་ཡང་ཤིན་ཏུ་ཐ་དད་པའི་སྔོན་པོ་ལ་སོགས་པ༌[^1389]འཇུག་པའི་གཟུགས་ཉིད་དེ༌[^1390]རོ་ལ་སོགས་པ་ལ་ཅིས་མ་ཡིན། རོ་ལ་སོགས་པ་ལ་མི་འཇུག་ན་ནི་དེར་སེར་པོ་ལ་སོགས་པ་ཡང་མི་འཇུག་གོ། །

[Block 1764]
གལ་ཏེ་འདི་ལ་རྒྱུ་ཡོད་དེ། [^1391]མིག་གི་གཟུང་བྱ་ཉིད་ནི་སྔོན་པོ་ལ་སོགས་པ་ཉིད་དང་ཐ་མི་དད་ཅིང་རོ་ལ་སོགས་པ་ལ༌[^1392]མེད་པ་ནི་རང་བཞིན་གྱིས་ཐ་དད་པ་ལས་སོ་ཞེ་ན། དེ་ལྟར་ན་ནི། [^1393]མིག་གཟུང་བྱ་ཉིད་བྱ་བར་བྱས། །མིག་གི་གཟུང་བྱར་གཟུང་བ་མིག་གི་གཟུང་བྱ་ཡིན་པ་དེ་ལྟ་ན་ནི་བྱ་བའི་རྒྱུ་མཚན་ནས་སྔོན་པོ་ལ་སོགས་པ་ལ་གཟུགས་ཀྱི་སྒྲར་འགྱུར་གྱི། རིགས་ཀྱི༌[^1394]རྒྱུ་མཚན་ནས་ནི་མ་ཡིན་ནོ། །

[Block 1765]
མིག་གི་གཟུང་བྱ་ཉིད་ཐ་མི་དད་ན་ནི་ཅིས་ན་གཟུགས་ཉིད་ཡིན། །ཅི་སྟེ་གཟུགས་ཉིད་དང་འབྲེལ་པའི་རྒྱུ་མཚན་མིག་གི༌[^1395]གཟུང་བྱ་ཉིད་བརྗོད་དོ་ཞེ་ན། །དེ་ལྟ་ན་ནི་མིག་གི་གཟུང་བྱ་ཉིད་ལ་བྱ་བར་བྱས་པས་འདུ་བའམ་གཟུགས་ཉིད་ཀྱི་མངོན་པར་གསལ་བ་འཐོབ་པར་འགྱུར་རོ། །

[Block 1766]
མིག་གི༌[^1396]གཟུང་བྱ་སྤྱི་ཉིད་ཀྱང་རུང་སྟེ། གལ་ཏེ༌[^1397]ངེས་པ་ཡིན་ཞེས་གདོན་མི་ཟ་བར་དངོས་པོ་པ་ཉིད་རྟེན་དུ་བྱའོ། །

[Block 1767]
རྫས་ལ་སོགས་པར་ཐལ་བར་འགྱུར། །རྫས་དང་གྲངས་དང་བོང༌[^1398]ཚོད་ལ་སོགས་པ་ཡང་མིག་གི་གཟུང་བར་བྱ་བ་ཡིན་པས་དེ་དག་ལའང་གཟུགས་ཉིད་ཡོད་པར་ཐལ་བར་འགྱུར་རོ། །

[Block 1768]
གཞན་ཡང་། དཀར་མིན་སོགས་ལ་ཁྱད་མེད་འགྱུར། །མིག་གི་གཟུང་བྱ་ཉིད་དུ་ཁྱད་པར་མེད་པ་ཡིན་པས་སྔོན་པོ་དང་སེར་པོ་དང་། ཆེས་སྔོ་བ༌[^1399]དང་། ཆེས་ཤིན་ཏུ་སྔོ་བའོ་ཞེས་བྱ་བའི་ཁྱད་པར་མེད་པར་འགྱུར།[^1400] །དེའི་ཕྱིར་གདོན་མི་ཟ་བར་མིག་གི་གཟུང་བྱ་ཉིད་མེད་པར། སྔོན་པོ་དང་སེར་པོ་ལ་སོགས་པའི་ཐ་དད་པ་ལ་ཡང་གཟུགས་ཀྱི་སྒྲ་འཇིག་རྟེན་ལ་གྲགས་པ་ཁས་བླང་བར༌[^1401]བྱ་བའི་རོ་ལ་སོགས་པ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 1769]
དེ་ལྟ་བས་ན་གཞན་སེལ་བ་ངེས་པ་ཡིན་ནོ། །

[Block 1770 [HEADING]]
### རྗེས་འགྲོ་འབའ་ཞིག་ལས་གྲུབ་འགྱུར་བ། ^5-11-0

[Block 1771]
གལ་ཏེ་དོན་གཞན་ལས་ལོག༌[^1402]པ་ལ་མི་ལྟོས་པར་སྒྲའི་དོན་རྗོད་པར་བྱེད་པ་དེའི་ལྟར་ན་ནི། རྗེས་འགྲོ་འབའ་ཞིག་ལས་གྲུབ་འགྱུར། །སྒྲའི་དོན་རྗོད་པར་བྱེད་པའི་ལྟ་ན་ནི་རྗེས་སུ་འགྲོ་བ་དང་ལྡོག་པ་དག་ལས་འདོད་པ་མ་ཡིན་ཏེ། ཁྱད་པར་གཞན་གཉིས་ཀ་ངེས་པར་བཟུང་བས་རྗོད་པར་བྱེད་པ་འབྲས་བུ་དང་བཅས་པའི་ཕྱིར་རོ། །

[Block 1772]
ལྡོག་པའི་ཕྱོགས་ལ་ནི་དོན་རྗོད་པར་བྱེད་པ་དཔེར་ན་ཆེས་ཤིན་ཏུ་བྱེད་པར་བྱེད་པ་དང་ལས་བཞིན་ནོ། །

[Block 1773]
གལ་ཏེ་སྒྲའི་དོན་གཞན་སེལ་བ་ཙམ་ཡིན་ན་ནི་ལྡོག་པ་འབའ་ཞིག་རྗོད་པར་བྱེད་པ་ཡིན་པར་འགྱུར་རོ་ཞེ་ན། གལ་ཏེ་རྗེས་སུ་འགྲོ་བ་མི་འདོད་ན་ནི་དེ་ལྟར་འགྱུར་ན་དངོས་པོའི་ཕྱོགས་ནས་ནི། ཁྱབ་པ་དངོས་སུ་འདོད་མ་ཡིན། །དངོས་པོ་རྣམས་ལ་ཐ་དད་པའམ་ཐ་མི་དད་པར་འགྱུར་བའི་རིགས་ནི་སྲིད་པ་མ་ཡིན་ནོ་ཞེས་བརྗོད་ཟིན་ཏོ། །

[Block 1774]
སྒྲའི་དོན་གཞན་མ་མཐོང་ཡང་ཞེས་བྱ་བ་འདིའི༌[^1403]སྐབས་སུ་རིགས་མེད་པར་དོན་གཞན་གསལ་བས༌[^1404]ཁྱད་པར་དུ་བྱས་པའི་དོན་ལ་སྒྲའི་རྗེས་སུ་འགྲོ་བ་དང་ལྡོག་པ་ནི་དོན་གཞན་མེད་པ་ཡིན་ནོ་ཞེས་བསྟན་ཏོ། །

[Block 1775 [HEADING]]
### ཐམས་ཅད་མེད་པ་དང་འབྲེལ་བ། ^5-12-0

[Block 1776]
འགའ་ཞིག་ན་རེ་འདི་སྐད་དུ། །བ་ལང་ལ་སོགས་པའི་བསལ་བ་ཐམས་ཅད་མེད་པ་ལས་རྣམ་པར་གྱུར་པ་སྟེ། །ཐམས་ཅད་ཀྱི་བདག་ཉིད་དུ་ཐལ་བར་འགྱུར་བའི་ཕྱིར་ཡོད་པ་མ་ཡིན་པའི་བདག་ཉིད་དུ༌[^1405]རབ་ཏུ་ཐོབ་པ་ཉིད་དོ་ཞེས་ཟེར་བ་ལ། འདིར།

[Block 1777 [VERSE]]
ཐམས་ཅད་མེད་པ་དང་འབྲེལ་ཞེས། །
གང་ཞིག་ཁས་ལེན་དུ་འགྲོ་ན། །
ཡོད་དེ་དུ་མའི་བདག་ཉིད་ལས། །
ཡིན་ཞེས་ཅི་ཞིག་གང་གིས་སྦྱོར། །

[Block 1778]
གལ་ཏེ་དེ་ལྟར་ཁས་ལེན་པར་བྱེད་ན་ནི་ཐམས་ཅད་མེད་པ་དང་འབྲེལ་པ་ཡིན་ནོ་ཞེས་པ༌[^1406]དེ་ལ་ཡོད་པའི་རང་བཞིན་ལས་གཞན་བ་ལང་ལ་སོགས་པའི་མེད་པ་ནི་གང་ཡིན། བ་ལང་ལ་སོགས་པ་ཡོད་པར་སྒྲོ་བཏགས་པ་ཐམས་ཅད་ནི་རྗེས་སུ་འགྲོ་བ་ལས་ཁས་བླང་བར་བྱའོ། །

[Block 1779]
ཐམས་ཅད་མེད་པར་ཐལ་བར་འགྱུར་རོ་ཞེས་པའི་ལན་འདི་ནི་སྦྱར་བར་མི་བྱའོ། །

[Block 1780 [HEADING]]
### འཇིམ་པ་ཐ་དད་ལ་ཁམ་ཕོར་ལ་སོགས་ཐ་དད་བློ། ^5-13-0

[Block 1781]
གང་འགའ་ཞིག་ན་རེ། མེད་པ་དང་ཡོད་པ་དག་ཤེས་པ་ཐ་དད་དུ་མི་འགྱུར་ཏེ། ཁམ་ཕོར་ལ་སོགས་པ་ལ་འཇིམ་པའི་ཤེས་པ་བཞིན་རང་བཞིན་གྱི་ཤེས་པ་འགྱུར་བ་ལ་ཡང་མཐོང་བའི་ཕྱིར་རོ་ཞེས་ཟེར་བ་དེ་ལ།

[Block 1782 [VERSE]]
འཇིམ་པ་ཐ་དད་ལ་ཁམ་ཕོར། །
ལ་སོགས་ཐ་དད་བློར་འདོད་ན། །
མེད་ཐ་དད་པ་གཞན་མིན་ཡང་། །
ཐ་དད་ཅི༌[^1407]བློ་ཅི་སྟེ་དགག །

[Block 1783]
ཇི་ལྟར་འཇིམ་པ་ལས་གཞན་མ་ཡིན་ན་ནི་དེ་ཙམ་གྱི་བློར་ཐལ་བར་འགྱུར་བ་ལ། གང་གིས་ན་བསྒྲུབ་པའི༌[^1408]སྒོ་ནས་ཁམ་ཕོར་ལ་སོགས་པའི༌[^1409]བློ་ཐ་དད་ཁས་ལེན་པར་བྱེད། དེ་བཞིན་དུ་མེད་པ་ལ་ཡོད་པའི་བློ་ཐ་དད་པ་ནི་སྒྲའི་རང་བཞིན་ཐ་དད་པའི་དབང་གིས་སོ་ཞེས་ཅི་ནས་མི་འདོད། ཁྱེད་ཀྱི་ཡང་།

[Block 1784 [VERSE]]
ཡོན་ཏན་རྣམས་ཀྱི༌[^1410]རང་བཞིན་མཆོག །
སྣང་བའི་ལམ་དུ་གང་མ་གྱུར། །
སྣང་བའི་ལམ་དུ་གང་གྱུར་པ། །
སྒྱུ་མ་བཞིན་དུ་ཤིན་ཏུ་སྟོང་། །

[Block 1785 [VERSE]]
ཕན་ཚུན་ཐ་དད་དག་ཡོད་ཀྱང་། །
ནོག་ལ་སོགས་པ་མཐོང་བ་ལས། །
དེའི་བློ་དཔེར་བརྗོད་འགལ་བ་དེ། །
ཁྱེད་ཀྱི་ལུགས་ལ་བརྟེན་པ༌[^1411]ཡིན། །

[Block 1786]
གང༌[^1412]བ་ལང་མ་ཡིན་པ་ལས་ལོག༌[^1413]པའི་བ་ལང་གི་བློ་དེ་ཇི་ལྟར་ན༌[^1414]ནོག་ལ་སོགས་པ་མཐོང་བའི་རྒྱུ་མཚན༌[^1415]དུ་སྨྲ་བར་བྱེད། བ་ལང་དང་ནོག་ལ་སོགས་པ་སྒྲ་ཐ་དད་པས་ཐ་དད་དུ་སེལ་བ་ཅན་ཡིན་ཡང་ཁྱོད་ཀྱི་ལུགས་ཁས་བླངས་ནས། འགལ༌[^1416]བཞིན་དུ་ཡང་དེ་ངེས་པར་བསྟན་ཏོ། །

[Block 1787 [VERSE]]
དེ་མི་ལྟོས་ཤེས་པ་འདི་ནི། །
རང་གི་རྣམ་རྟོག་སྤྲོས་པར་ཟད། །
སེལ་བ་མིན་པའི་སྒྲ་ཡིས་ནི། །
རང་བཞིན་འགའ་ཡང་བརྗོད་མི་བྱ། །

[Block 1788]
ནོག་ལ་སོགས་པ་ལ་སྤྱིའི་ངོ་བོ་དང་ལྡན་པ་གཞན་མེད་པར་མི་ལྟོས་པ་ནི་མི་སྲིད་དོ་ཞེས་སྔར་བཤད་ཟིན་ཏོ། །

[Block 1789]
རང་གི་ངོ་བོ་ནི༌[^1417]བརྗོད་པར་བྱ་བ་མ་ཡིན་པའི་ཕྱིར་དེའི་སྒོ་ནས་ཐ་སྙད་དུ་མི་བྱའོ། །

[Block 1790 [HEADING]]
### དང་པོའི་ཤེས་པ་མེད་པ། ^5-14-0
--- END BLOCKS ---
