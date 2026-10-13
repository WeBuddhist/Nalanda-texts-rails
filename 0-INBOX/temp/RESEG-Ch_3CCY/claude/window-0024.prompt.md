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
[Block 841]
གང་འདི་སྐད་དུ།

[Block 842 [VERSE]]
དངོས་པོ་ཡོད་ན་རྟག་པ་ཉིད། །
མེད་ན་ངེས་པར་ཆད་པ་ཉིད། །
དངོས་པོར་གྱུར་ན་དེ་གཉིས་ལ། །
དེ་ཕྱིར་དངོས་པོ་ཁས་མི་བླང་། །

[Block 843]
ཞེས་པ་དེ་ནི་མི་འཐད་དེ། །གལ་ཏེ་དངོས་པོ་ཁས་མི་ལེན་ན་དེའི་ཚེ་དུས་གསུམ་མེད་ལ། དུས་གསུམ་ཡོད་པས་དེའི་ཕྱིར་དངོས་པོ་ཡོད་དེ། དུས་གསུམ་གྱི་རྒྱུ་མཚན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 844]
འདིར་སྐྱེས་ལ་མ་འགགས་པའི་དངོས་པོ་ངོ་བོ་ཉིད་ཀྱིས་གནས་བཞིན་པའི་ཕྱིར་དང་། ཡོད་བཞིན་པའི་ཕྱིར་ད་ལྟར་བའི་སྒྲས་བརྗོད་པར་བྱ་བར་འགྱུར་རོ། །

[Block 845]
ད་ལྟར་བའི་གནས་སྐབས་མ་ཐོབ་པ་ལ་མ་འོངས་པ་ཞེས་བརྗོད་ལ། ད་ལྟར་བའི་གནས་སྐབས་ལས་འདས་པ་ཉིད་ལ་འདས་པ་ཞེས་བརྗོད་དོ། །

[Block 846]
གལ་ཏེ་དངོས་པོ་མེད་ན་དེ་ཅིའི་རྒྱུ་མཚན་གྱིས་དུས་གསུམ་འབྱུང་བར་འགྱུར། དེའི་ཕྱིར་དུས་གསུམ་ཡོད་པས་དངོས་པོ་ཡོད་དོ་ཞེ་ན། སྨྲས་པ། གལ་ཏེ་དུས་གསུམ་ཡོད་ན་དངོས་པོ་ཡོད་པར་འགྱུར་ལ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 847]
ཇི་ལྟར་མེད་པ་དེ་ལྟར་བསྟན་པའི་ཕྱིར་གསུངས་པ།

[Block 848 [HEADING]]
### ཚིགས་བཅད་ཉེར་དགུ་པ། ^1-29-0

[Block 849 [VERSE]]
གནས་མེད་ཕན་ཚུན་ལས་གྲུབ་པ། །
འཆོལ་ཕྱིར་རང་ཉིད་མ་གྲུབ་ཕྱིར། །
དངོས་པོ་མེད་ཕྱིར་ཡོད་མིན་ཏེ། །
དུས་གསུམ་པོ་ནི་བཏགས་པ་ཙམ། །

[Block 850]
གལ་ཏེ་དུས་ཞེས་བྱ་བ་འགའ་ཞིག་ཡོད་ན་དེ་ལ་འཛིན་ལ་རག་ན་མི་འཛིན་ལ། དེའི་ཕྱིར་འཛིན་པ་མེད་པས་དུས་མེད་དོ། །

[Block 851]
ཡང་ཅིའི་ཕྱིར་མི་འཛིན་ཞེ་ན། གནས་མེད་ཕྱིར་ཏེ། དུས་ཞེས་བྱ་བ་ཅུང་ཟད་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 852]
ཐེར་ཟུག་པའི་དངོས་པོ་ཡོད་ན་གང་ཞིག་འཛིན་ལ་རག་ན། དེ་ལས་མ་བཟུང་བའི༌[^626]ཕྱིར་དུས་མེད་དོ། །

[Block 853]
ཡང་ན་གལ་ཏེ་ཡང་ཐེར་ཟུག་པའི་དུས་གང་ཅུང་ཟད་མི་འཛིན་ལ། དེ་ལྟ་ན་ཡང་དུས་ཡོད་པ་ཉིད་དུ་འགྱུར་ཏེ། སྐད་ཅིག་ལ་སོགས་པས་མངོན་པར་གསལ་བར་བྱས་པའི་ཕྱིར་རོ། །

[Block 854]
འདི༌[^627]སྐད་ཅིག་དང་ཐང་ཅིག་དང་། ཡུད་ཙམ་དང་། ཟླ་བ་ཕྱེད་དང་། ཟླ་བ་དང་། ལོ་ཕྱེད་དང་། ལོ་ལ་སོགས་པའི་དུས་ཀྱི་ཚད་ཀྱི་ཁྱད་པར་རྣམས་ཏེ། ཁྱད་པར་དེ་རྣམས་ཀྱིས་འཛིན་བཞིན་པའི་ཕྱིར། དུས་ཡོད་པ་ཉིད་དོ་ཞེ་ན། སྨྲས་པ། གལ་ཏེ་ལོ་ལ་སོགས་པ་ཉིད་ཡོད་ན། ལོ་ལ་སོགས་པའི་ཚད་དང་ལྡན་པའི་དུས་འཛིན་ལ་རག་ན། དེ༌[^628]སྐད་ཅིག་ལ་སོགས་པ་ལས་ཐ་དད་པའི་ཐེར་ཟུག་པའི་ལོ་ལ་སོགས་པ་མི་འཛིན་ནོ། །

[Block 855]
ཡང་ན་འདི་སྙམ༌[^629]དུ་སེམས་ན། རེ་ཞིག་སྐད་ཅིག་མ་ཡོད་ན། དེ་ལ་འཛིན་པས་དེས་ན་དེ་འདུས་པའི་རང་བཞིན་ཐང་ཅིག་ལ་སོགས་པ་འབྱུང་བར་འགྱུར་རོ་ཞེ་ན། སྨྲས་པ། གང་དུ་གནས་པ་མེད་པའི་སྐད་ཅིག་མ་རྣམས་ལ་འདུས་པ་ག་ལ་ཞིག་གང་དུ་ཐང་ཅིག་ལ་སོགས་པ་འཛིན་པར་གྱུར་ཅིང་སྐད་ཅིག་མ་ཡང་ཡོད་ན་ཐང་ཅིག་ལ་སོགས་པ་རྣམ་པར་འཇོག་གྲང་ན། སྐད་ཅིག་དེ་ལ་ཡང་ཐོག་མ་དང་བར་དང་ཐ་མ་ཡོད་ལ། ཐོག་མ་དང་བར་དང་ཐ་མ་དེ་རྣམས་ལ་ཡང་ཐོག་མ་དང་བར་དང་ཐ་མ་ཡོད་པའི་ཕྱིར། གནས་པ་མེད་པས་སྐད་ཅིག་མ་ཡང་མེད་ན། སྐད་ཅིག་མ་འདུས་པའི་ཐང་ཅིག་ལ་སོགས་པ་ག་ལ་འགྲུབ། བློའི་རང་བཞིན་གྱི་འདུས་པར་བརྟགས་པས༌[^630]སྐད་ཅིག་མ་གྲུབ་པ་མི་སྲིད་དེ། བློའི་སྐད་ཅིག་དེ་ཡང་ཡོངས་སུ་བརྟགས་པའི་ཕྱིར་དང་།

[Block 856]
དེ་ཉིད་གནས་པ་མེད་པའི་ཕྱིར་དུས་མེད་དོ། །དུས་མེད་ན་དུས་གསུམ་ནི་ག་ལ་ཞིག །

[Block 857]
གནས་པ་མེད་པ་འབའ་ཞིག་གིས་དུས་གསུམ་མེད་པར་མ་ཟད་ཀྱི། ཕན་ཚུན་ལས་གྲུབ་པས་ཀྱང་དུས་གསུམ་མེད་དེ། འདི་ལྟར་ད་ལྟར་བ༌[^631]འདས་པ་ལས་འདས་པའོ། །

[Block 858]
ད་ལྟར་བ༌[^632]མ་འོངས་པ་ལས་མ་འོངས་པ་ལ། གནས་བཞིན་པའི་ཕྱིར་ད་ལྟར་བའོ་ཞེས་དེ་ལྟར་ཕན་ཚུན་ལྟོས་ནས་གྲུབ་ལ། དུས་གསུམ་ཕན་ཚུན་ལྟོས་ནས་གྲུབ་པས་དེ་མ་གྲུབ་པ་ཉིད་དོ་ཞེས་བསྒྲུབས་པས༌[^633]སོ་ཞེས་བྱའོ། །

[Block 859]
དེས་ན་ཡང་དུས་གསུམ་མེད་དོ། །

[Block 860]
འདི་ལྟར་ཡང་དུས་གསུམ་མེད་དེ། འཆོལ་བའི་ཕྱིར་ཏེ། མ་འོངས་པའི་དུས་དེ་ཉིད་ད་ལྟར་བར་འོངས་པ་ལ་ད་ལྟར་བ་ཞེས་བརྗོད་ལ། ད་ལྟར་བ་ལ༌[^634]འདས་པར་ཞུགས་པས་འདས་པ་ཞེས་བྱའོ། །

[Block 861]
གཅིག་ཉིད་ལ་དུས་གསུམ་དུ་རྣམ་པར་གཞག་པའི་ཕྱིར་འཆོལ་བའོ། །

[Block 862]
ཡང་ན་ཕན་ཚུན་ལྟོས་ནས་གྲུབ་པའི་ཕྱིར་དུས་གསུམ་པོ་མེད་དེ། འདས་པ་ནི་ད་ལྟར་བ་དང་མ་འོངས་པ་ལ་མ་ལྟོས་པར་མེད་ལ། གལ་ཏེ་ཡང་འདས་པར་ད་ལྟར་བ་དང་མ་འོངས་པ་ཡོད་ན་དེའི་ཚེ་དེ་ལ་ལྟོས་པ་འཐད་ཀྱི། འདས་པ་ནི་མོ་གཤམ་གྱི་བུ་བཞིན་དུ་མེད་ལ། ཡོད་བཞིན་པ་མ་ཡིན་པའི་མོ་གཤམ་གྱི་བུ་མི་ལྟོས་པ་བཞིན་ནོ། །

[Block 863]
གང་གི་ཚེ་ཡང་འདས་པར་ད་ལྟར་བ་དང་མ་འོངས་པ་དག་ཡོད་ན་དེའི་ཚེ། འདས་པར་ད་ལྟར་བ་ཡོད་པའི་ཕྱིར། འདས་པའི་རང་གི་བདག་ཉིད་བཞིན་འདས་པར་འགྱུར་ལ། དེ་ལྟར་འདས་པ་དང་མ་འོངས་པ་དག་འདས་པ་དང་ད་ལྟར་བ་ལ་ཡང་བསམ་པར་བྱའོ། །

[Block 864]
འདི་ལྟར་དེ་ནི་འདས་པ་དང་མ་འོངས་པ་དང་ད་ལྟར་བ་རྣམས་ལ་སོ་སོར་དུས་གསུམ་དུ་ཐལ་བར༌[^635]འཆོལ་བས། འཆོལ་བའི་ཕྱིར་ཡང་དུས་གསུམ་མེད་དོ། །

[Block 865]
འདི་ལྟར་ཡང་། དུས་གསུམ་མེད་དེ་རང་ཉིད་མ་གྲུབ་ཕྱིར། །འདིར་སྐད་ཅིག་མ་ལ་སོགས་པས་དུས་མངོན་པར་གསལ་བར་ཕ་རོལ་པོ་འདོད་དོ། །

[Block 866]
སྐད་ཅིག་མ་ལ་སོགས་པ་ལས་ཐ་དད་པའི་དུས་གང་ཅུང་ཟད་ཡོད་ཅིང་། གང་ཞིག་དེས་མངོན་པར་གསལ་བར་བྱེད་པ་ཡང་མ་ཡིན་ཏེ། རི་བོང་གི་རྭ་རང་གི་ངོ་བོར་མ་གྲུབ་པས་སུས་ཀྱང་མངོན་པར་གསལ་བར་བྱེད་པ་མ་ཡིན་ནོ། །

[Block 867]
དེས་ན་ངོ་བོ་ཉིད་ཀྱིས་དུས་མ་གྲུབ་བོ། །

[Block 868]
དུས་ཀྱང་མེད་ན་དེའི་གསུམ་ཉིད་ག་ལ་ཞིག་ཅེས་བྱ་སྟེ། དུས་གསུམ་མེད་དོ། །

[Block 869]
གཞན་ཡང་ཁྱོད་ཀྱིས་དངོས་པོ་བསྒྲུབ་པའི་ཕྱིར་དུས་གསུམ་ཉེ་བར་གཞག་ལ། དུས་དེ་ཡང་དངོས་པོ་ལ་མ་ལྟོས་པར་མ་གྲུབ་ལ། དངོས་པོ་ཉིད་ལ་བརྟེན་ནས་དེ་རྣམ་པར་གཞག་པའི་ཕྱིར་རོ། །

[Block 870]
དངོས་པོ་དེ་ཡང་སྔར་ཉིད་དུ་མེད་དོ་ཞེས་བསྒྲུབས་ལ། དུས་གསུམ་པོ། དངོས་པོ་མེད་ཕྱིར་ཡོད་མིན་ཏེ། །གལ་ཏེ་དེ་ལྟར་དུས་གསུམ་པོ་མེད་ན། དེའི་ཚེ་ཇི་ལྟར་དུས་གསུམ་དུ་ཐ་སྙད་བྱེད་ཅེ་ན། སྨྲས་པ། དུས་གསུམ་པོ་བཏགས་པ༌[^636]ཙམ་ཡང་དག་པ་མ་ཡིན་པས་སྒྲོ་བཏགས་པ་ཙམ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 871]
དུས་གསུམ་མེད་ལ། དེའི་རྒྱུ་མཚན་གྱི་དངོས་པོ་ཡང་མེད་དོ་ཞེས་གྲུབ་པོ། །

[Block 872]
འདིར་སྨྲས་པ། དངོས་པོ་ཡོད་པ་ཉིད་དེ། དེ་ཡང་འདུས་བྱས་ཀྱི་རང་བཞིན་ཏེ་དེའི་མཚན་ཉིད་ཡོད་པའི་ཕྱིར་རོ། །

[Block 873]
ཡོད་བཞིན་པ་མ་ཡིན་པ་ལ་མཚན་ཉིད་མེད་དེ། འདི་ལྟ་སྟེ་མོ་གཤམ་གྱི་བུ༌[^637]ལྟ་བུའོ། །

[Block 874]
དངོས་པོ་ནི་འདུས་བྱས་ཀྱི་མཚན་ཉིད་སྐྱེ་བ་དང་འཇིག་པ་དང་གནས་པ་ཞེས་བྱ་བ་ཡོད་ལ། དེའི་ཕྱིར་མཚན་ཉིད་ཡོད་པས་འདུས་བྱས་ཀྱི་རང་བཞིན་གྱི་དངོས་པོ་ཡོད་དོ་ཞེ་ན། སྨྲས་པ། གལ་ཏེ་དེའི་འདུས་བྱས་ཀྱི་མཚན་ཉིད༌[^638]ཡོད་ན། འདུས་བྱས་ཀྱི་རང་བཞིན་ཡོད་ལ། ཡོད་པ་མ་ཡིན་ནོ་ཞེས་བསྟན་པའི་ཕྱིར་གསུངས་པ།

[Block 875 [HEADING]]
### ཚིགས་བཅད་སུམ་ཅུ་པ། ^1-30-0

[Block 876 [VERSE]]
འདུས་བྱས་མཚན་ཉིད་སྐྱེ་བ་དང་། །
གནས་འཇིག་གསུམ་པོ་འདི་ཡང་མེད། །
གང་ཕྱིར་འདུས་བྱས་མེད་འདི་ལས། །
འདུས་མ་བྱས་པ་ཅུང་ཟད་མེད། །

[Block 877]
དེ་ལ་འདིས༌[^639]མཚོན་པར་བྱེད་པས་ན་མཚན་ཉིད་དེ། རྒྱུ་དང་རྐྱེན་འདུས་པས་ཤེས་པས།[^640] འདུས་པ་ལས་འབྱུང་བར༌[^641]བྱེད་པ་འདུས་བྱས་ལ། འདུས་བྱས་དང་མཚན་ཉིད་པས་འདུས་བྱས་ཀྱི་མཚན་ཉིད་དེ། དེ་ཅི་ཞེ་ན། སྐྱེ་བ༌[^642]གནས་དང་འཇིག་པའོ། །

[Block 878]
སྐྱེ་གནས་འཇིག་པ་ཞེས་བྱ་བ་གསུམ་པོ་དེ་ཉིད་ཀྱང་མེད་ན། གང་གི་ཕྱིར་གསུམ་པོས་འདུས་བྱས་འཇུག་པ་མེད་པར་དེ་ནི་སྔར་ཉིད་དུ་བསྒྲུབས་ཏེ།

[Block 879]
ཡོད་པ་ཡོད་ཕྱིར་སྐྱེ་བ་མིན། །མེད་པ་མེད་ཕྱིར་མི་སྐྱེ་བ། །ཞེས་པས་འདིར་གང་གི་ཚེ་གང་ལས་འདུས་བྱས་འཇུག་པ་དེའི་གསུམ་པོ་མ་གྲུབ་ན། དེའི་ཚེ་འདུས་བྱས་མ་གྲུབ་པ་དོན་གྱིས་བསྒྲུབས་པར་འགྱུར་རོ། །

[Block 880]
གང་གི་ཕྱིར་འདུས་བྱས་མེད་ན་འདི་ལས་འདུས་མ་བྱས་ཡིན་པ་ཡང་ཅུང་ཟད་ཀྱང་མེད་དོ། །
--- END BLOCKS ---
