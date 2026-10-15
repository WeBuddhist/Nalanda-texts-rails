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
[Block 1 [HEADING]]
## ༄༅། །འདུལ་བའི་མདོའི་འགྲེལ་པ་མངོན་པར་བརྗོད་པ་རང་གི་རྣམ་པར་བཤད་པ།༼དེབ་གསུམ་པ།༽

[Block 2 [HEADING]]
## སྲ་བརྐྱང་གི་གཞི། ^1-0

[Block 3]
སྲ་བརྐྱང་གདིང་བར༌[^1]བྱའོ་ཞེས་བྱ་བ་ལ། སྲ་བརྐྱང་ཞེས་བྱ་བ་ནི་གཏན་པ་སྟེ། འདི་ལྟར་འདི་ནི་གོས༌[^2]གདིང་བར་བྱེད་ཅིང་རྐྱོང་བར༌[^3]བྱེད་པ་མི་འཁུམས་པར་བྱེད་པའི་ཆོས་ཅན་ཤིང་ལ་སོགས་པ་ལས་བྱས་པའི་སྤང་ལེབ་ལ་གཏན་པ་ཞེས་བྱའོ། །

[Block 4]
དེ་ལ་གང་ཞིག་འདིས་ཚོགས་དེ་ལ་དགེ་སློང་གཅིག་ཚོགས་ཏེ༌[^4]མ་ལུས་པ་ལ་ཁྱེད་པར༌[^5]བྱེད་ན་ཚོགས་མ་ལུས་པ་ཉིད་ཀྱིས་རྒྱས་པར་འགྱུར་བ་དེའི་ཚོགས་འབྲེལ་པ་ཐམས་ཅད་ལ་རྗེས་སུ་ཞུགས་པ་ཐམས་ཅད་ལ་ངོ་བོ་གཅིག་པའི་གདིང་བར་འགྱུར་བ་དགེ་འདུན་མཐའ་དག་ལ་ཁྱབ་པར༌[^6]བྱེད་པས་དེའི་མིང་གཏན་པ་ཞེས་བྱ་བའོ།

[Block 5]
[^7] །དེ་ཉིད་ཀྱི་ཕྱིར་འདིར་འདི་བྱ་བ་ལ་གདིང་བ་ངེས་པར་དེ་ཞེས་བྱ་བར་བརྗོད་པ་ཡིན་ནོ། །

[Block 6]
ཅིའི་ཕྱིར་གོས་གསུམ་གདིང་བར་བྱ་བ་བཏིང་བ་ལ་འབྲས་བུ་ཅི་ཡོད་ཅེ་ན། དེའི་ཕྱིར་གསུམ་པོ་དག་ཇི་ལྟ་བ་བཞིན་དུ་སྲ་བརྐྱང་བཏིང༌[^8]ན་ཡང་ཡང་ཟ་བ་དང་འདུས་ཤིང་ཟ་བ་དང་། མ་སྨྲས་པར་གྲོང་དུ་འགྲོ་བ་དང་གོས་སློང་བ་ལ་ཡང་ཉེས་པ་མེད་ལ། དེ་ལྷག་མ་དག་དང་རྙེད་པ་ཐུན་མོང་དུ་འགྱུར་རོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རེ་ཞིག་གསུམ་པོ་དག་ཅེས་བྱ་བ་ནི་འཆང་བ་དང་འབྲལ་བ་དང་འཇོག་པའི་བདག་ཉིད་ཅེས་སྨོས་པ་ཁོ་ན་སྟེ། ཇི་ལྟར་བཞི་པོ་གཞན་འདི་ཐུན་མོང་གི་མཐར་ཐུག་པ་ལྔ་པོ་སྐྱོན་དང་བྲལ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 7]
སྨད་གཡོགས་དང་སྟོད་གཡོགས་སུ་བྱས་པའི་ཆོས་གོས་ཀྱིས་ལྗོངས་རྒྱུ་ཞིང་འགྲོ་བ་གང་ཡིན་པ་དང་། རུང་བར་བྱས་པའི་གོས་ཇི་ཙམ་འདོད་པ་འཆང་བ་ཞེས་བྱ་བ་གང་ཡིན་པ་གཉིས་པོ་འདི་བསྡུས་པ་སྟེ། གསུམ་པོ་བསྟན་པ་ཉིད་ཀྱིས་བསྡུ་བ༌[^9]བྱས་ཟིན་པའི་ཕྱིར་རོ། །

[Block 8]
གལ་ཏེ་དེ་ལ་སྣམ་སྦྱར་བསྐུར་བས་དགོས་པ་མེད་པས་དེས་ཅི་ཞིག་བྱ། ཇི་ལྟར་གང་གི་ཕྱིར་སྟོད་གཡོགས་སྨད་གཡོགས་སུ་བཅས་པ་མེད་ན་ངོ་ཚ་བའི་གནས་གཡོགས་པར་བྱ་བའི་ཕྱིར་དང་། རབ་ཏུ་འབྱུང་བའི་རྟགས་ཡང་དག་པར་བསྲུང་བར་བྱ་བའི་ཕྱིར་ཡིན༌[^10]གྱི། སྣམ་སྦྱར་བསྐུར་བ་ལ་དགོས་པ་མེད་པ་དེ་བཞིན་དུ་འདི་ལའོ། །

[Block 9]
གལ་ཏེ་བཏང་ན་འཆང་བ་ལ་ཉེས་པ་མེད་དེ་རྣམ་པར་རྟོག་པས༌[^11]ཅི་ཞིག་བྱ་ཞེས་བྱ་བའོ། །

[Block 10]
འོ་ན་བཅོམ་ལྡན་འདས་ཀྱིས། ཚིག་འདི་བརྗོད་པ་ཅི་ཞིག་བརྗོད་ཅེ་ན། སྟོད་གཡོགས་ཀྱི་ཁུར་ལས་ཐར་བར་བྱ་བའི་ཕན་ཡོན་བསྟན་པའི་ཕྱིར་རོ། །

[Block 11]
རུང་བ་མ་བྱས་པའི་གོས་འཆང་བ་དེ་ནི་རྣམ་པར་རྟོག་པའི་བྱ་བས་ཐར་པ་དང་བག་ཡངས་ཀྱི་བདེ་བའི་ཕན་ཡོན་ཡང་བསྟན་པའི་ཕྱིར་རོ། །

[Block 12]
གསུམ་པོ་དག་ཅེས་བྱ་བ་ལ་ལྟོས་པ་གང་ཡིན་ཞེ་ན། དེའི་ཕྱིར་གནས་པར་ཁས་མ་བླངས་པ་དང་། དབྱར་རལ་བ་དང་། དབྱར༌[^12]ཕྱི་མར་གནས་པར་ཁས་བླངས་པ་དག་ལ་དེ་མི་འབྱུང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ས་གཞན་ན་གནས་པ་དག་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་དབྱར་གནས༌[^13]གཞན་དུ་ཁས་བླངས་པ་ལ་སོགས་པ་སྟེ། དབྱར་གནས་པ་ཕྱི་མར་གནས་པར་ཁས་བླངས་པ་དེ་དང་རོ་གཅིག་པར་འདྲ་བའོ། །

[Block 13]
དབྱར་གནས་པར་ཁས་མ་བླངས་པ་དང་། དབྱར་རལ་བ་དག་ལ་དབྱར་གྱི་གཏན་པ་མི་འབྱུང་ངོ་། །དབྱར་གནས་གཞན་དུ་གནས་པར་ཁས་བླངས་པ་དག་ལ་ནི་གཏན་པ་གདིང་བ་དག་མི་འབྱུང་བ་སྟེ། གཏན་པ་གདིང་བ་ནི་དངོས་གཞིའི་ཆོ་ག་ལ་བརྟེན་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 14]
དངོས་གཞིའི་ཆོ་ག་ཞེས་བྱ་བ་གཏན་པ་བཏིང་བ་ལ་བྱའོ། །

[Block 15]
དབྱར་ཕྱི་མར་ཁས་བླངས་པ་ནི་མ་ཡིན་ནོ། །

[Block 16]
དགེ་འདུན་གྱི་དུས་ལས་འདའ་བས་དེ་བརྟེན་པ་དང་ལྡན་པའི༌[^14]ཚོགས་པ་སྦྱིན་པ་ལ་ཡང་དབྱར་གནས་པར་ཁས་ལེན་པ་མེད་པའོ། །

[Block 17]
འདི་ནི་སྐལ་བ་མི་མཉམ་པ་སྟེ། རང་བཞིན་གནས་པ་ཉིད་ཀྱི༌[^15]ཕྱིར་རོ། །

[Block 18]
གང་ཞིག་སའི་ནང་དུ་གནས་པ་ཉིད་ནི་རང་བཞིན་དུ་གནས་པ་ཉིད་མ་ཡིན་པའོ། །

[Block 19]
དེ་བས་ན་འདི་ལྟར་ལྷན་ཅིག་ཏུ་རོ་གཅིག་པ་འདི་ལ་ནི་རུང་བ་མ་ཡིན་ནོ། །

[Block 20]
གལ་ཏེ་སྐྱེ་བར་མ་གྱུར་ན་རང་བཞིན་དུ་གནས་པ་ཉིད་ནད་པར་གྱུར་ན་སྲ་བརྐྱང་བཏིང་བ་དང་། བཏིང་བ་ཆུད༌[^16]ཟོས་པ་མི་སྐྱེད༌[^17]པའོ། །

[Block 21]
དགེ་ཚུལ་དག་ལ་ནི་འདི་ལྟར་འདི་མི་སྐྱེད་པའོ༌[^18]ཞེས་འབྱུང་ངོ་། །དེ་དང་དེའི་ལས་ལ་འདི་མ་ཞུགས་པ་ལ་ཆོ་ག་གང་ཡིན་པ་དེ་ཉིད་ཀྱི་བྱས་པ་ཞེས་གསུངས་པ་དེའི་ཕྱིར་འདིར་བསྡུས་པ་མ་ཡིན་ནོ། །

[Block 22]
དེ་དག་ཉིད་ཐོབ་པ་ཡིན་ན་མི་འབྱུང་ངོ་ཞེས་བྱ་བ་ནི་སྲ་བརྐྱང་གདིང་བ་ཉིད་ལས་གཞན་ན་གནས་པ་དེ་དག་ཉིད་ཐོབ་པ་ལ་ནི༌[^19]མི་འབྱུང་བ་སྟེ། སྲ་བརྐྱང་གདིང་བ་མི་འབྱུང་ཞིང་སྦྱར་བ་ནི་མ་ཡིན་ནོ། །

[Block 23]
ཐ་མ་མ་གཏོགས་པ་དག་དང་ས་གཞན་ན་གནས་པ་དག་དང་དགེ་ཚུལ་ནི་རྙེད་པ་དབང་ངོ༌[^20]ཞེས་བྱ་བ་ལ། ཐ་མ་མ་གཏོགས་པ་ནི་ཐ་མ་མ་གཏོགས་པ་སྟེ། གནས་གཞན་དུ་གནས་པ་དང་དབྱར་ཕྱི་མར་ཁས་བླངས་པ་དང་དབྱར་གནས་པར་ཁས་མ་བླངས་པ་ལ་སོགས་པ་རྣམས་སོ། །

[Block 24]
གལ་ཏེ་ཡང་གཏན་པ་གདིང་བ་ལ་འདི་རྣམས་མི་འགྱུར་བ་དེ་ལྟར་ཡང་དེ་རྒྱུ་མཚན་ཅན་གྱི་རྙེད་པ་ལ་དེ་རྣམས་ལ་སྐལ་བ་དང་ལྡན་པ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 25]
འདི་ལྟར་དེ་དག་གི་དབྱར་གནས་པ༌[^21]དག་དང་དོན་གཅིག་པ་ཉིད་ཡིན་པས་བཟློག་པར་མི་བྱ་སྟེ་དེ་རྣམས་ཀྱི་དེ་སྐལ་བ་དང་ལྡན་པ་ཉིད་དོ། །

[Block 26]
ས་གཞན་ན༌[^22]གནས་པ་དག་ཅེས་སྨོས་པས་སྤངས་པ་ཡང་རྙེད་པ་དབང་བ་ཉིད་དུ་ཐལ་བར་འགྱུར་བས་དེ་བསལ་བའི་ཕྱིར་སྤངས་པ་ནི་མི་དབང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སྤངས་པ་ནི་དགེ་འདུན་ལས་ཐ་དད་དུ་གྱུར་པ་ཉིད་ཡིན་པས་དེའི་ཕྱིར་ན་གཏན་པ་བཏིང་བའི་རྙེད་པ་མི་དབང་བ་ཉིད་དུ་རིག་པར༌[^23]བྱའོ། །

[Block 27]
དེ་ལས་གཞན་པ་ཆད་པས་བཅད་པ་དང་སྤོ་བ༌[^24]ལ་སོགས་པ་བྱེད་པ་ནི་དགེ་འདུན་ལས་ཐ་དད་དུ་གྱུར་པ་ཉིད་མ་ཡིན་པས་དེའི་ཆོ་ག་འདི་མི་འཇུག་པའོ། །

[Block 28]
བྱེ་བ་དག་ནི་ཆོས་མ་ཡིན་པའི་ཕྱོགས་དང་མཐུན་པ་དག་ཏུ་སོང་བ་ནི་དེ་ཉིད་ཀྱིས་ཐོབ་པ་དང་འདྲའོ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བའི་སྒྲས་ནི་སྤངས་པ་ལ་སྙེགས་ཏེ༌[^25]སྤང་བའི་རྙེད་པ་དང་འདྲ་སྟེ། བྱེ་བ་དག་ན་འདོད་པ་གཞན་ལ་དམིགས་པས་ཆོས་མ་ཡིན་པའི་ཕྱོགས་དང་མཐུན་པ་དག་ཏུ་གནས་པ་རྣམས་ལྟུང་བའོ། །

[Block 29]
ཇི་ལྟར་སྤངས༌[^26]པ་ལ་མེད་པར་འགྱུར་བ་དེ་བཞིན་དུ་འདི་རྣམས་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 30]
གང་གི་དོན་དུ་སྲ་བརྐྱང་གདིང་བར་བྱ་ཞེས་བྱ་བ་དེ་བསྡུ་བ་བསྟན་ནས། ད༌[^27]ནི་འདིར་དངོས་པོ་གང་གདིང་བར་བྱ་བ་ལ་དེ་ལ་གཏན་པ་ཉིད་ཅེས་པ༌[^28]བརྗོད་པར་བྱ་སྟེ། དངོས་པོ༌[^29]གཞིའི་དུས་སུ་དགག་དབྱེའི་མཐར་དབྱར་གྱི་རྒྱུ་ལས་བྱུང་བའི་གདིང་བའི་ཉི་མའི་མཐར་གྲུབ་པ་གོས་ཀྱི་རྙེད་པར་བགྲང་བའི་ཆོས་གོས་གསུམ་མོ་ཞེས་བྱ་བ་ལ་འདིར་དབྱར་དང་པོ་རྣམས་བཟུང་བ་ཞེས་བྱ་བ་དེ་ནི་དབྱར་ཕྱི་མ་ལ་བརྟེན་པ་ལ་མི་འབྱུང་ངོ་ཞེས་གསུངས་པའི་ཚིག་གིས་ཤེས་པར་བྱ་སྟེ། སྟོན་ཟླ་འབྲིང་པོའི་ཚེས་བཅུ་དྲུག་ནི་གཏན་པ་གདིང་བའི་ཉི་མ་ཉིད་ཡིན་པར་གསུངས་པའི་ཕྱིར་རོ། །

[Block 31]
དངོས་གཞིའི་དུས་དེའི་དགག་དབྱེའི་ཞག་མན་ཆད་གཞན་ནམ་རྒྱུ་ལས་གཞན་པའི་རྙེད་པ་བྱེད་བཞིན་པའི་དགག་དབྱེའི་ཐ་མ་དེ་རྣམས་བསྡུས་པ་ནས་རྒྱུས་རྙེད་པ་ལ་མཐར་ཐུག་པ་དེ་དག་བསྡུས་པའི་རྒྱུ་ལས་བྱུང་བ་ཡིན་ནམ་ཞེ་ན། འདི་ལྟ་སྟེ་དབྱར་གནས་པའི་རྒྱུ་ལས་བྱུང་བའི༌[^30]རྙེད་པ་གང་ཡིན་པའོ། །

[Block 32]
ཡང་ན་སོ་སོ་བ་སྟེ། འདི་ལྟར་རྒྱུ་ལས་བྱུང་བའི་རྙེད་པ་གང་ལ་ཡོད་པ་དེ་ནི་དངོས་གཞིའི་དུས་ཀྱི་དགག་དབྱེའི་མཐར་དབྱར་གྱི་རྒྱུ་ལས་བྱུང་བས་ཏེ། དུས་གཞན་དུ་འབྱུང་བ་ནི་མ་ཡིན་ཏེ། གདིང་བའི་ཞག་རྣམས་ཀྱི་མཐའ་ཅན་འདི་རྣམས་དང་འབྲེལ་བའོ། །

[Block 33]
དེའི་དུས་ལས་དུས་གང་ཡང་རུང་བའི་ས་ལས་བསྒྲུབ་པ་སྟེ། དུས་གཞན་གྱི་རྒྱུ་ལས་བྱུང་བའི་རྙེད་པ་ནི་མ་ཡིན་ནོ། །

[Block 34]
ལག་གི་བླ་དང་རྒྱན་འདོགས་པ་དང་བ་གླང་གི་དང་མ་ཧེ༌[^31]དང་མལ་སྟན་དང་དེར་གཏོགས་པའི་དགག་དབྱེ་ལ་སོགས་པའི་བྱེ་བྲག་གི་དོན་དུ་སྦྱིན་པ་མ་ཡིན་ཏེ། དེའི་གྲངས་དང་ལྡན་པ་ཆོས་གོས་གསུམ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 35]
གཙུག་ལག་ཁང་ན་གོས་ཀྱི་རྙེད་པར་ངེས་པ་གང་ཡིན་པ་དེ་ཡང་འདིར་བསྡུས་པར་ཤེས་པར་བྱ་སྟེ། དེ་ལྟ་བས་ན་གོས་ཀྱི་དོན་དུ་རྙེད་པའི་རིན་དག་གིས་རྙེད་པ་བཟུང་ངོ་། །དེ་ལྟ་བས་ན་ཆོས་གོས་གསུམ་དུ་ཤེས་པར་བྱ་བ་མ་ཡིན་ཏེ། གང་ཞིག་གོས་རྙེད་པ་ཞེས་བྱ་བ་བརྗོད་པར་བྱ་བ་ལ༌[^32]རིན་ཐང་སྔོན་དུ་འགྲོ་བས་བསྒྲུབ་པ་ལ་སྐྱེད་པར་བྱེད་པ་ཉིད་དེ་དེ༌[^33]བས་ན། གོས་གསུམ་ལ་སྲ་བརྐྱང་ཉིད་གདིང་བར་བྱའོ་ཞེས་བྱ་བ་འདིར་དངོས་སུ༌[^34]སྒྲུབ་བྱེད་ཅུང་ཟད་ཀྱང་མ་མཐོང་ངོ་། །རྟགས་ནི་ཡོད་དེ། དེ༌[^35]གང་ལས་ཤེས་ཤེ་ན། ཚེ་དང་ལྡན་པ་དག་བདག་སང་གཏན་པ་གདིང་བར༌[^36]འགྱུར་གྱི༌[^37]ཁྱེད་ཅག་གིས་རང་རང་གི་ཆོས་གོས་རྣམས་དབྱུང་བར་བྱའོ་ཞེས་གསུངས་པའི་ལུང་ལས་ཤེས་ཏེ། གང་གི་ཕྱིར་གཅིག་པུ་ཞིག་གདིང་བར་བྱ་བ་ཉིད་ཡིན་ན་ནི་དེའི་ཚེ་རང་གི་ཞེས་བྱ་བ་གཅིག་གི་ཚིག་འཐོབ་པའོ། །

[Block 36]
གཅིག་ཅིག་བྱིན་གྱིས་བརླབས་པ༌[^38]ལ་གསུམ་ཆར་གྱིས་དབྱུང་བ་ཡང་མི་རིགས་པའི་ཕྱིར་རོ། །

[Block 37]
དེ་ལྟར་ཡང༌[^39]འདིར་གཞུང་ནི་བཙུན་པ། གང་ཟག་གི་སྣམ༌[^40]སྦྱར་གྱི་གཏན་ལ༌[^41]གདིང་དུ་རུང་ངམ། ཉེ་བ༌[^42]འཁོར་མི་རུང་ངོ་། །གལ་ཏེ་དགེ་འདུན་ལ་ཕུལ་ན་ནི་རུང་ངོ་། །བླ་གོས་དང་མཐང་གོས་ཀྱང་དེ་བཞིན་ནོ་ཞེས་གསུངས་པ་ཡིན་ཏེ། བླ་གོས་དང་མཐང༌[^43]གོས་གཉིས་ཀྱང་ངོ་། །གཅིག་གིས་གདིང་བ་ཡོད་པར་གྱུར་པ་ལ༌[^44]འདི་རིགས་པར་གྱུར་པ་མཐོང་བ་ཡིན་ནོ། །

[Block 38]
གང་ཡང་གདིང་བར་བྱ་ཞེས་བྱ༌[^45]བ་གཅིག་གིས་ཚིག་དེ་ལ་ནི་དེ་ལྟར་གནོད་པ་མ་ཡིན་ཏེ། འདིར་དགེ་འདུན་རྒྱས་པ་བསྒྲུབ་པ་ཅན་གྱི་སྲ་བརྐྱང་གི་སྒྲས་ཆོས་གོས་བརྗོད༌[^46]པའི་ཕྱིར་དང་། [^47]གཅིག་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 39]
ཆོས་གོས་ཐམས་ཅད་གཅིག་པ་ཉིད་ཀྱི་ཕྱིར་རྒྱས་པར་སྒྲུབ་པ་ཉིད་ལ་གནས་པ༌[^48]མེད་དོ། །

[Block 40]
དེ་ལྟ་བས་ན་བྱིན་གྱིས་བརླབ་པ༌[^49]ཐམས་ཅད་ལ་འདི་ཐམས་ཅད་སྟོན་པའོ། །
--- END BLOCKS ---
