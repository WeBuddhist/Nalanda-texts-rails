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
[Block 596]
གང་གིས༌[^627]ཕྱོགས་བཅུའི་དེ་དག་བརྒྱན་པ་ནི། །ཞེས་བྱ་བ་ནས། ལྷ་དང་བཅས་པའི་འཇིག་རྟེན་རྒྱས་པ་འདི།[^628] །ཞེས་པའི་བར་དུ་ནི་མཆོད་རྟེན་དེ་བྱས་པས་འཇིག་རྟེན་ཐམས་ཅད་ལ་མཛེས་པ་ནི་དཔེར་ན་ལྷའི་མེ་ཏོག་པ་རི་ཡ་ཏ་རྒྱས་པ་བཞིན་དུ་མཛེས་པ་བསྟན་ཏོ། །

[Block 597 [HEADING]]
###### དོན་འདྲི་བ། ^4-1-9-2-2-0

[Block 598]
མདོ་ལས།

[Block 599]
རྒྱལ་བས་འོད་ཟེར་གཅིག་པུ་འདི་བཏང༌[^629]བས། །ཞེས་པ་ནས། སྟོང་ཕྲག་མང་པོའི་ཞིང་རྣམས་སྟོན་པའོ། །ཞེས་པའི་བར་དུ་ཚིགས་བཅད་རྩ་བ་བརྒྱད་ཀྱིས་ནི་གསོལ་བའི་དོན་བསྟན་ཏེ། རྩ་བ་བཞིས་ནི་ལན་བཏབ་པའོ། །

[Block 600]
མདོ་ལས།

[Block 601]
ལྟས༌[^630]རྣམས་མཐོང་ནས་བདག་ཅག་ངོ་མཚར་ཐོབ། །ཅེས་པ་ནས། ཐེ་ཚོམ་སོལ་ལ་དགའ་བ་བསྐྱེད་པར་གྱིས།[^631] །ཞེས་པའི་བར་དུ་ནི་བདག་དང་གཞན་གྱི་རེ་བ་སྐོང་བར་བསྟན་པའོ། །

[Block 602]
མདོ་ལས།

[Block 603]
བདེ་གཤེགས་སྲས་པོ་ཁྱོད་ཀྱིས་ལུང་སྟོན་ཅིག །ཅེས་པ་ནས། འདི་འདྲའི་རྒྱ་ཆེན་འོད་ཀྱང་རབ་ཏུ་བཏང་།[^632] །ཞེས་པའི་བར་དུ་འདིས་ནི་དྲིས་པའི་ལན་གསོལ་བའོ། །

[Block 604]
མདོ་ལས།

[Block 605]
བདེ་གཤེགས་སྲས་པོ་ཁྱོད་ཀྱིས་ལུང་སྟོན་ལ། །ཞེས་པ་ནས། འདི་ཡི་རྒྱུ་ནི་ཆུང་བར་མི་འགྱུར་ཏེ། །ཞེས་པའི་བར་དུ་ནི་དྲིས་པའི་ལན་བཏབ་པ་དང་། ལུང་བསྟན་པ་དང་། དོན་ཆེ་བ་བསྟན་པ་དང་། ཞིང་རྣམ་པར་དག་པ་འདིའི་དོན་ཆུང་བ་མ་ཡིན་པར་བསྟན་པའོ། །

[Block 606]
མདོ་ལས།

[Block 607]
ཞིང་རྣམས་སྟོང་ཕྲག་དུ་མ་གང་བསྟན་པ། །ཞེས་པ་ནས། འཇམ་དབྱངས་འདི་རུ་ཅི་ཞིག་ལུང་སྟོན་ཅེས། །ཞེས་པའི་བར་དུ་ནི་དྲིས་པའི་ལན་དངོས་སུ་བཏབ་པའོ། །

[Block 608 [HEADING]]
#### འཇམ་དཔལ་གཞོན་ནུར་གྱུར་པས་ལན་གློན་པ། ^4-1-10-0

[Block 609 [HEADING]]
##### མིང་སྨོས་ཏེ་མདོར་བསྟན་པ། ^4-1-10-1-0

[Block 610]
མདོ་ལས་དེ་ནས་ཞེས་པ་ནས་རིགས་ཀྱི་བུ་རྣམས་ཞེས་པའི་བར་དུ་ནི་འཇམ་དཔལ་གཞོན་ནུར་གྱུར་པ་ལན་གློན་པར་ནུས་པ་ནི་འགྲེལ་པ་ལས།

[Block 611]
འཇམ་དཔལ་སྔོན་གྱི་གནས་རྗེས་སུ་དྲན་པའི་ཡེ་ཤེས་ཀྱིས་འདས་པ་རྒྱུ་དང་འབྲས་བུ་ཕུན་སུམ་ཚོགས་པ་མངོན་དུ་གཟིགས་པའི་ཕྱིར་ལན་གློན་ནུས་པ་སྟེ། རྗེས་སུ་དཔག་པའམ་ཡིད་ཚོད་ཙམ་གྱིས་ལན་འདེབས་པ་མ་ཡིན་ནོ། །

[Block 612]
འཇམ་དཔལ་གྱིས་རང་གི་སྐུ་སངས་རྒྱས་མང་པོ་ལ་བྱ་བ་བྱས་པའི་རྒྱུ་དེ་ད་ལྟར་གྱི་འབྲས་བུ་འདི་ཉིད་པས་སྔོན་དམ་པའི་འོད་ཅེས་བྱ་བའི་དགེ་སློང་དུ་གྱུར་པ་ན། དེ་བཞིན་གཤེགས་པ་ལས་ཆོས་འདི་མངོན་དུ་ཐོས་པའི་ཕྱིར། ད་འགྲོ་བ་མང་པོ་ལ་སྟོན་ནུས་ཏེ། འདི་མན་ཆད་དུམ་བུ་གསུམ་དུ་བཅད་དེ་སྟོན་ཏོ། །

[Block 613]
དང་པོ་མིང་སྨོས་ཏེ་མདོར་བསྟན་པ་དང་། དྲིས་པའི་ལན་གདབ་པ་དང་། འོག་མ་ཉན་པ་རྣམས་ལ་གདམས་པ་དང་གསུམ་མོ། །

[Block 614 [HEADING]]
##### དྲིས་པའི་ལན་གདབ་པ། ^4-1-10-2-0

[Block 615]
མདོ་ལས་འདི་ནི་བདེ་བར་གཤེགས་པས་ཆོས་ཆེན་པོ་བསྒྲགས་ཤིང་ཡང་དག་པར་བརྗོད་པར་མཛད་པར་དགོངས་པ་ཞེས་པ་ནི་དྲིས་པའི་ལན་གདབ་པ་སྟེ། འདི་འགྲེལ་པ་ལས་ལན་གདབ་པ་ལ་དོན་རྣམ་པ་བཅུ་སྟེ། དོན་ཆེན་པོ་མངོན་དུ་མཐོང་བའི་རྒྱུ་སྟེ་འདི་ཉིད་ཡིན་པ་དང་། རིགས་ཀྱི་བུ་རྣམས་ང༌[^633]སྔོན་འདས་པའི་དུས་འཇིག་རྟེན་གྱི་ཚིག་དང་འབྲུ་དང་ལེའུ་ཤིན་ཏུ་ཟབ་པའི་རྒྱུ་དང་མཐོང་བ་དང་། ཡང་རིགས་ཀྱི་བུ་རྣམས་སྔོན་འདས་པ་གྲངས་མེད་དཔག་ཏུ་མེད་པ་ནས་ངོ་མཚར་རྨད་དུ་བྱ་བའི་རྒྱུ་མཐོང་བ་སྔོན་ཡང༌[^634]དེ་བཞིན་གཤེགས་པ་ཉི་ཟླ་སྒྲོན་མ་ཞེས་བྱ་བ་ནས་རྒྱུ་དམ་པ་མཐོང་བ་དང་། ཡང་དེ་བཞིན་གཤེགས་པ་ནང་གི་ཐ་མ་ཁྱིམ་ནས་མ་བྱུང་བ་ནས་ལོངས་སྤྱོད་པའི་རྒྱུ་ཆེན་པོ་མཐོང་བ་དང་། སངས་རྒྱས་མྱ་ངན་ལས་འདས་པའི་འོག་ཏུ་དམ་པའི་འོད་བྱང་ཆུབ་སེམས་དཔའ་དམ་པའི་ཆོས་འདི་འཛིན་པ་ནས་དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱི་ཆོས་སྡུད༌[^635]ཅིང་འཛིན་པའི་རྒྱུ་མངོན་དུ་མཐོང་བ་དང་ཡང་ཉི་ཟླ་སྒྲོན་མ་དེ་བཞིན་གཤེགས་པའི་སྲས་བརྒྱད་པོ་ཡང༌[^636]དམ་པའི་འོད་ལ་བརྟེན་ནས་ཤིན་ཏུ་བརྟན་པའི༌[^637]དེ་བཞིན་གཤེགས་པ༌[^638]མངོན་དུ་མཐོང་བའི་རྒྱུ་དང་རྒྱལ་བུ་དེ་དག་གིས་མཆོད་པ་དང་རིམ་གྲོ་གྲངས་མེད་པར་བྱས་པས་འཇུག་པར་ནུས་པའི་རྒྱུ་མངོན་དུ་མཐོང་བ་དང་། དེ་བཞིན་གཤེགས་པ་ནང་གི༌[^639]ཐ་མར་མངོན་པར་སངས་རྒྱས་པ༌[^640]སྒྲོན་མ་མཛད་པ་ལ་མངོན་དུ་དྲན་པའི་རྒྱུ་མཐོང་བ་དང་། བྱམས་པ་ཁྱོད་ཀྱིས་ཤེས་པར་གྱིས་ཤིག །དེའི་ཚེ་དམ་པའི་དབྱངས་བྱང་ཆུབ་སེམས་དཔའ་དམ་པའི་འོད་ལ་བདག་ཉིད་ཀྱིས་མངོན་དུ་སྤྱད་པ་སྤྱད་པའི་རྒྱུ་མཐོང་བ་སྟེ། རྒྱུ་ནི་གཏན་ཚིགས་ཀྱི་དོན་ཏོ། །

[Block 616]
འཇམ་དཔལ་གཞོན་ནུར་གྱུར་པས་གཏན་ཚིགས་དེ་དག་མངོན༌[^641]དུ་གྱུར་པ་ལས་དཔག་ནས་འཕགས་པ་བྱམས་པ་ལ་ལན་བཏབ་པའོ། །

[Block 617]
རྒྱུ་དེ་བཅུ་ཡང་དོན་ལྔར་བསྡུས་ཏེ། དོན་བསྟན་པ་དང་། ཡ་མཚན་དུ་གྱུར་པ་དང་། གྲོལ་བ་དང་བཅིངས་པ་དང་། བརྩོན་འགྲུས་བསྟན་པ་དང་། བདག་དང་གཞན་དུ་སྦྱར་བའོ། །

[Block 618]
རྒྱུ་བཅུ་པོ་དེ་དག་ཀྱང་ལྟས་ལས་དཔགས་ཏེ་ལན་གདབ་པ་དང་། སྔོན་གྱི་དང་ད་ལྟར་སྦྱར་ཏེ་ལན་གདབ་པ་དང་། དོན་གཞན་ལས་གླེང་སྟེ༌[^642]ལན་གདབ་པ་དང་། སྔོན་གྱི་ལུགས་དང་སྦྱར་ཏེ་ལན་གདབ་པའོ། །

[Block 619]
དེ་ལའང་དང་པོའི་གཉིས་དང་། ཐ་མའི་གཅིག་ནི་གོང་མའི་རིམ་པ་བཞིན་དུ་སྦྱར། བར་གྱི་རྒྱུ༌[^643]བདུན་པོ་ནི་གཞན་ལས་གླེངས་ཏེ་ལན་གདབ་པ་དང་སྦྱར་རོ། །

[Block 620 [HEADING]]
###### ལྟས་ལས་དཔགས་ཏེ་ལན་གདབ་པ། ^4-1-10-2-1-0

[Block 621]
འདི་ནི་ལྟས་ལས་དཔགས་ཏེ་ལན་གདབ་པའོ། །

[Block 622]
འགྲེལ་པ་ལས་དོན་ཆེན་པོ་མཐོང་བའི་རྒྱུ་ཕུན་སུམ་ཚོགས་པ་མཐོང་བ་ནི་ལྟས་རྣམ་པ་བརྒྱད་དོ།[^644] །ཆོས་ཆེན་པོའི་ཆར་འབེབས་པ་དང་། །ཆོས་ཀྱི་རྔ་བརྡུང་བ་དང་དུང་འབུད་པ་ལ་སོགས་པའོ། །

[Block 623]
འགྲེལ་པ་ལས་ཐེ་ཚོམ་ཅན་རྣམས་ཐེ་ཚོམ་བསལ་བའི་ཕྱིར་ཆོས་ཆེན་པོ་འཆད་དེ་ཐེ་ཚོམ་མ་ཆོད༌[^645]ན་ཡེ་ཤེས་ཀྱི་ལུས་སྨིན་པར་བྱ་བའི་ཕྱིར་ཆོས་ཀྱི་ཆར་ཆེན་པོ་ཕབ་པས་དགེ་བའི་མྱུ་གུ་སྐྱེས་ཏེ་འཕགས་པའི་གནས་ཐོབ་པར༌[^646]འགྱུར་རོ། །

[Block 624]
དབང་པོ་སྨིན་པ་རྣམས་སྤྱོད་ཡུལ་གསང་བ་རྣམ་པ་གཉིས་སྟོན་ཏོ།[^647] །ཉན་ཐོས་རྣམས་ལ་ནི་ཆོས་ཀྱི་རྔ་ཆེན་པོ་བརྡུང་ངོ་། །བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ལ་བླ་མའི་བླ་མ་རྣམ་པར་དག་པའི་དོན་བསྟན་པའི་ཕྱིར་ཆོས་ཀྱི་རྒྱལ་མཚན་བསྒྲེང༌[^648]བ། བྱང་ཆུབ་སེམས་དཔའ་ཆོས་ཀྱི་ཡེ་ཤེས་རྟོགས་པའི༌[^649]ཕྱིར་ཡེ་ཤེས་ཀྱི་སྒྲོན་མ་སྣང་བར་མཛད་པས་ཆོས་ཀྱི་སྒྲོན་མ་འབར་བར་མཛད་པའོ། །

[Block 625]
ཡེ་ཤེས་ཐམས་ཅད་མངོན་དུ་གྱུར་པའི་ཕྱིར་ཚིག་འབྲུ་དང་དོན་བསྒྲགས་པའི༌[^650]ཕྱིར་ཆོས་ཀྱི་དུང་འབུད་པ་ཞེས་པའོ། །

[Block 626]
དེ་དག་ཀྱང་སྡིག་པ་སྤོང་ཞིང་དགེ་བར་འཇུག་པ་དང་། དྲང་བའི་དོན་གྱིས་ངེས༌[^651]པའི་དོན་སྟོན་པ་དང་། ཤེས་རབ་ཀྱིས༌[^652]ཡང་དག་པའི་དོན་ཆུད་པ་དང་། ཆོས་སྟོན་པས་འགྲོ་བ་ལ་ཕན་པའོ། །

[Block 627]
མདོ་དང་འབྲེལ་པ༌[^653]ལས་འབྱུང་བ་འདི་དག་ཅི་རིགས་པ་དང་གར་འོས་སུ་སྦྱར་རོ། །

[Block 628 [HEADING]]
###### སྔོན་གྱི་དང་ད་ལྟར་སྦྱར་ཏེ་ལན་གདབ་པ། ^4-1-10-2-2-0

[Block 629]
མདོ་ལས་རིགས་ཀྱི་བུ་འདི་ནི་དེ་བཞིན་གཤེགས་པས་ཆོས་ཆེན་པོ་བཤད་པར་དགོངས་པ་སྟེ་ཞེས་པ་ནི་འཇིག་རྟེན་གྱི་ཚིག་འབྲུའི་དོན་ཤིན་ཏུ་ཟབ་པའི་རྒྱུ་སྟོན་ཏེ། དེ་ནི་སྔོན་གྱི་ལུགས་ལས་དྲང་སྟེང༌[^654]འདི་ལྟའོ་ཞེས་དོན་སྦྱར་བའོ། །

[Block 630]
མདོ་ལས་རིགས་ཀྱི་བུ་རྣམས་བདག་གིས་ཇི་ལྟ་བུར་སྤོབས་པ༌[^655]དང་། ཇི་ལྟར་སྔོན་གྱི་དེ་བཞིན་གཤེགས་པ་ཞེས་པ་ནས་འོད་ཟེར་བཏང་ཞིང་སྣང་བ་ཐོག་མ་མཐོང་བ་མངོན་པར་བསྟན་ཏོ་ཞེས་པའི་བར་དུ་ནི་གཞུང་བཞིན་དུ༌[^656]ཆུད་པར་བྱའོ། །

[Block 631 [HEADING]]
###### དོན་གཞན་ལས་གླེང་སྟེ་ལན་གདབ་པ། ^4-1-10-2-3-0

[Block 632]
མདོ་ལས་རིགས་ཀྱི་བུ་རྣམས་བདག་གིས་དྲན་པ་འདས་པའི་དུས་བསྐལ་བ་གྲངས་མེད་པའི་ཡང་གྲངས་མེད་པ་ཞེས་པ་ནི་རྒྱུ་བརྒྱད་སྦྱར༌[^657]དུམ་བུ་གཉིས་སུ་ཕྱེ་སྟེ། ཚིག་ལྷུག་པ་དང་ཚིགས་སུ་བཅད་པས་བསྡུ་བའོ། །

[Block 633]
སྔར་རྒྱུན་གྱིས༌[^658]ན་དོན་གཞན་ལས་གླེངས་ཏེ་ལན༌[^659]བཏབ། རྒྱུ་གཅིག་གིས་སྔོན་གྱི་ལུགས་ལས་དྲས༌[^660]ཏེ་ལན་བཏབ།

[Block 634 [HEADING]]
###### **ངོ་མཚར་དུ་གྱུར་པ་ལས་བསྟོད་དེ་ལན་བཏབ་པ།** ^4-1-10-2-3-1-0

[Block 635]
དང་པོ་ལ་ཡང་རྣམ་པ་གསུམ་སྟེ། ངོ་མཚར་དུ་གྱུར་པ་ལས་བསྟོད་དེ་ལན་བཏབ་པ་དང་། ཕྱིས་ཁྱད་པར་དུ་གྱུར་པ་ལས་ལན་བཏབ་པ་དང་། ཕྱི་མ་ལྔས་ནི་དོན་མཐུན་པ་ལས་དྲས༌[^661]ཏེ་ལན་བཏབ། ངོ་མཚར་དུ་གྱུར་པ་ལས་བསྟོད་དེ་ལན་བཏབ་པ་ནི་འགྲེལ་པ་ལས་ཡ་མཚན་མངོན་དུ་གྱུར་པའི་རྒྱུ་དང་སྦྱར་རོ། །
--- END BLOCKS ---
