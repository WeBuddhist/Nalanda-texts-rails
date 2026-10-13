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
[Block 701]
འདི་དག་ནི་མ་རིག་པ་ཙམ་དང་། བསྒོམ་པས་སྤང་བར་བྱ་བ་དང་། ཡིད་ཀྱི་ས་པ་ཁོ་ན་དང་མཚུངས་པར་ལྡན་པའི་ཕྱིར་ཉོན་མོངས་པ་ཆུང་ངུའི་ས་པར་བརྗོད་དོ། །

[Block 702]
འདི་དག་གི་རྒྱས་པར་བཤད་པ་ནི་ཕྱིས་འཆད་དོ། །

[Block 703 [HEADING]]
##### སེམས་གང་ལ་སེམས་ལས་བྱུང་བ་དུ་ཞིག་འབྱུང་བ། ^2-2-2-2-0

[Block 704]
སེམས་གང་ཞིག་ལ་སེམས་ལས་བྱུང་བ་དུ་ཞིག་གདོན་མི་ཟ་བར་འབྱུང་བ༌[^276]བརྗོད་པར་བྱ་སྟེ། རེ་ཞིག་འདོད་པ་ན་སྤྱོད་པའི་སེམས་ནི་རྣམ་པ་ལྔ་སྟེ་དགེ་བ་ལ་སོགས་པའོ། །

[Block 705]
དེ་ལ།

[Block 706 [VERSE]]
འདོད་པའི་དགེ་བའི་སེམས་ལ་ནི། །
རྟོག་དང་དཔྱོད་དང་བཅས་པའི་ཕྱིར། །
སེམས་ལས་བྱུང་བ་ཉི་ཤུ་གཉིས། །

[Block 707]
ས་མང་པོ་པ་བཅུ་དང་། དགེ་བའི་ས་མང་པོ་པ་བཅུ་དང་། རྟོག་པ་དང་། དཔྱོད་པ་དག་གོ། །

[Block 708]
ལ་ལ་དག་ཏུ་འགྱོད་པ་བསྣན། །དེ་ལ་གང་དགེ་བ་མ་བྱས་པ་དང་། མི་དགེ་བ་བྱས་ནས་གདུང་བ་གང་ཡིན་པ་སྟེ། དེ་ནི་མི་དགེ་བ་བྱས་པ་ལ་དམིགས་པའི་ཡིད་ལ་གཅགས་པ་དགེ་བ་ལ་འགྱོད་པའོ། །

[Block 709]
དེ་ནི་གང་ལ་ཡོད་པ་དེ་ལ་སེམས་ལས་བྱུང་བ་ཉི་ཤུ་རྩ་གསུམ་འབྱུང་ངོ་། །

[Block 710 [VERSE]]
མི་དགེ་ལ་ནི་མ་འདྲེས་དང་། །
ལྟ་དང་ལྡན་པའང་ཉི་ཤུ་འབྱུང་། །

[Block 711]
མ་འདྲེས་པ་ཞེས་བྱ་བ་ནི་སེམས་གང་ལ་མ་རིག་པ་འབའ་ཞིག་པ་སྟེ། དེ༌[^277]ལ་ས་མང་པོ་པ་བཅུ་དང་། ཉོན་མོངས་པའི་ས་མང་པོ་པ་དྲུག་དང་། མི་དགེ་བའི་ས་མང་པོ་པ་གཉིས་དང་། རྟོག་པ་དང་། དཔྱོད་པའོ། །

[Block 712]
མི་དགེ་བའི་ལྟ་བ་དང་ལྡན་པ་ཡང་ཉི་ཤུ་འབྱུང་སྟེ། གང་ཁོ་ན་མ་འདྲེས་པ་ལའོ། །

[Block 713]
ལྟ་བ་ཡང་མི་དགེ་བ་འཇིག་ཚོགས་དང་། མཐར་འཛིན་པ་མ་གཏོགས་པ་ཤེས་རབ་ཀྱི་རང་བཞིན་ཡིན་པས་བསྣན་པ་མ་ཡིན་ནོ། །

[Block 714 [VERSE]]
ཉོན་མོངས་བཞི་དང་ཁྲོ་སོགས་དང་། །
འགྱོད་པ་དང་ནི་ཉི་ཤུ་གཅིག །

[Block 715]
དེ་ལ་ཉོན་མོངས་པ་བཞི་ནི་འདོད་ཆགས་དང་། ཁོང་ཁྲོ་དང་། ང་རྒྱལ་དང་། ཐེ་ཚོམ་མོ། །

[Block 716]
ཁྲོ་བ་ལ་སོགས་པ་ནི་བཤད་ཟིན་ཏོ། །

[Block 717]
འགྱོད་པ་ནི་མི་དགེ་བ་སྟེ་དགེ་བ་ལས་བཟློག་པས་སོ། །

[Block 718]
འདི་དག་གང་ལ་ཡོད་པ་དེ་ནི་ཉི་ཤུ་རྩ་གཅིག་ཡིན་ཏེ། འདི་དག་ཁོ་ན་ལས་གང་ཡང་རུང་བ་ཅིག་ལྷག་པར་བྱས་ནས་སོ། །

[Block 719]
བསྒྲིབས་ལ་བཅོ་བརྒྱད། འདོད་པའི་ཁམས་ན་འཇིག་ཚོགས་ལ་ལྟ་བ་དང་། མཐར་འཛིན་པར་ལྟ་བ་དང་མཚུངས་པར་ལྡན་པའི་སེམས་ནི་བསྒྲིབས་པ་སྟེ། དེ་ལ་སེམས་ལས་བྱུང་བ་བཅོ་བརྒྱད་འབྱུང་སྟེ། ས་མང་པོ་པ་བཅུ་དང་། ཉོན་མོངས་པའི་ས་མང་པོ་པ་དྲུག་དང་། རྟོག་པ་དང་། དཔྱོད་པའོ། །

[Block 720]
ལུང་མ་བསྟན། གཞན་ལ་བཅུ་གཉིས་དག་ཏུ་འདོད། །མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པའི་སེམས་ལ་ས་མང་པོ་པ་བཅུ་དང་། རྟོག་པ་དང་།

[Block 721 [VERSE]]
དཔྱོད་པ་ཞེས་བྱ་བ་བཅུ་གཉིས་སོ། །
གཉིད༌[^278]ནི་ཀུན་ལ་མི་འགལ་ཕྱིར། །
གང་ལ་ཡོད་པ་དེས་བསྣན་ཏོ། །

[Block 722]
གཉིད་ནི་ཇི་སྐད་བཤད་པ་ཐམས་ཅད་དང་མི་འགལ་ཏེ། དེའི་ཕྱིར་གང་ལ་ཡོད་པ་དེ་ལ་དེས་བསྣན༌[^279]པར་རིག་པར་བྱའོ། །

[Block 723]
གང་དེ་ལྟར་འདོད་པའི་ཁམས་ལ་སེམས་བྱུང་ངེས་པར་བཤད་པ།

[Block 724 [VERSE]]
དེ་ལས་འགྱོད་གཉིད་མི་དགེ་རྣམས། །
བསམ་གཏན་དང་པོ་དག་ན་མེད། །

[Block 725]
བསམ་གཏན་དང་པོ་ན་ནི་ཇི་སྐད་བཤད་པ་དེ་ལས་འགྱོད་པ་དང་། གཉིད་དང་། གང་ཡང་ཅུང་ཟད་མི་དགེ་བ་གཡོ་བ་ལ་སོགས་པ་ཐམས་ཅད་དུ་མེད་དེ། གཞན་ཐམས་ཅད་ནི་དེ་དང་འདྲའོ། །

[Block 726]
བསམ་གཏན་དང་པོ་ན་མེད་པ་གང་དག་ཡིན་པ་དེ་དག་ཁོ་ན་དང་། རྟོག་པའང་བསམ་གཏན་ཁྱད་པར་ཅན། །དེའི་གང༌[^280]ན་དཔྱོད་པ་ཡང༌[^281]མེད་དེ་ལྷག་མ་ནི་དེ་དང་འདྲའོ། །

[Block 727 [HEADING]]
##### ཐ་དད་དུ་བྱ་བ། ^2-2-2-3-0

[Block 728]
ད་ནི་གཞུང་ལས་བྱུང་བ་ཁ་ཅིག་གི་ཐ་དད་དུ་བྱ་བ་འབྱུང་བ་བརྗོད་པར་བྱ་སྟེ། ངོ་ཚ་མེད་པ་དང་། ཁྲེལ་མེད་པ༌[^282]ཐ་དད་དུ་བྱ་བ་ཅི་ཞིག་ཡོད་ཅེ་ན། མ་གུས་ངོ་ཚ་མེད། ཡོན་ཏན་རྣམས་དང་ཡོན་ཏན་ཅན་རྣམས་ལ་མ་གུས་པ་ཉིད་ནི་བཀུར་པ་མེད་པ་ཉིད་དེ་ངོ་ཚ་མེད་པའོ། །

[Block 729]
ཁྲེལ་མེད། ཁ་ན་མ་ཐོ་འཇིགས་མི་ལྟ། །ཁ་ན་མ་ཐོ་བ་ཞེས་བྱ་བ་ནི་དམ་པ་རྣམས་ཀྱིས་སྨད་པ་སྟེ། དེ་ལ་འཇིག༌[^283]པར་མི་ལྟ་བ་ནི་ཁྲེལ་མེད་པའོ། །

[Block 730]
འདིར་འཇིགས་པ་ནི་མི་འདོད་པའི་འབྲས་བུ་སྟེ། འདི་ལས་འཇིགས་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 731]
བཟློག་པ་ནི་ངོ་ཚ་ཤེས་པ་དང་ཁྲེལ་ཡོད་པ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 732]
དགའ་བ་དང་གུས་པ་ལ་ཐ་དད་དུ་བྱ་བ་ཅི་ཞིག་ཡོད་ཅེ་ན། དགའ་དང་། དགའ་བ་ནི་རྣམ་པ་གཉིས་དང་། །ཉོན་མོངས་པ་ཅན་ནི་སྲེད་པ༌[^284]སྟེ། དཔེར་ན་བུ་དང་ཆུང་མ་ལ་སོགས་པ་ལྟ་བུའོ། །

[Block 733]
ཉོན་མོངས་པ་ཅན་མ་ཡིན་པ་ནི་དད་པ་སྟེ། དཔེར་ན་སྟོན་པ་དང་བླ་མ་དང་ཡོན་ཏན་ཅན་རྣམས་ལ་བྱ་བ་བཞིན་ནོ། །

[Block 734]
གུས་ཉིད་ངོ་ཚ་ཤེས། གུས་པ་ནི་ངོ་ཚ་ཤེས་པ་ཇི་སྐད་བཤད་པ་བཞིན་ནོ། །

[Block 735 [VERSE]]
དེ་གཉིས་འདོད་དང་གཟུགས་དག་ན། །
གཟུགས་མེད་པ་ཡི་ཁམས་ན་ནི། །

[Block 736]
གང་ཟག་ལ་དམིགས་པའི་དགའ་བ་དང་གུས་པ་དག་མེད་དོ། །

[Block 737]
རྣམ་པར་རྟོག་པ་དང་། དཔྱོད་པ་དག་ལ་ཐ་དད་དུ་བྱ་བ་ཅི་ཡོད་ཅེ་ན།

[Block 738 [VERSE]]
རྟོག་དང་དཔྱོད་པ་རྩིང་ཞིབ་ཉིད། །
སེམས་ཀྱིའོ་ཞེས་འོག་ནས་འཆད་དེ།
རྟོག་པ་ནི་སེམས་རྩིང་བའོ། །
དཔྱོད་པ་ནི་སེམས་ཞིབ་པའོ། །

[Block 739]
ང་རྒྱལ་དང་རྒྱགས་པ་དག་ལ་ཐ་དད་དུ་བྱ་བ་ཅི་ཞིག་ཡོད་ཅེ་ན།

[Block 740 [VERSE]]
ང་རྒྱལ་ཁེངས་པ་རྒྱགས་པ་ནི། །
རང་གི་ཆོས་ལ་ཆགས་པ་ཡི། །
སེམས་ནི་ཡོངས་སུ་གཏུགས་པའོ། །
--- END BLOCKS ---
