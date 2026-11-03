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
དང་པོ་ལའང་རྣམ་པ་དྲུག་སྟེ་འཁོར་ཕུན་སུམ་ཚོགས་པ་དང་དུས་ཕུན་སུམ་ཚོགས་པ་དང་། སྤྱོད་ལམ་ཕུན་སུམ་ཚོགས་པ་དང་། རྒྱུ་ཕུན་སུམ་ཚོགས་པ་དང་། ཐོས་པ་ཕུན་སུམ་ཚོགས་པ་དང་། ལམ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 702]
ཚིགས་བཅད་དང་པོ་གཉིས་ཀྱིས་ནི་ཁྱིམ་ན་གནས་པ་བསྟན། དེའི་འོག་མ་གཉིས་ཀྱིས་ནི་རབ་ཏུ་བྱུང་བ་བསྟན་ཏོ། །

[Block 703]
མདོ་ལས།

[Block 704]
འཇིག་རྟེན་མགོན་པོ་དེ་ཡིས༌[^708]ཆོས་བཤད་པ། །ཞེས་པ་ནས། །སྲོག་ཆགས་སྟོང་ཕྲག་བྱེ་བ་དག་ལས༌[^709]བཤད། །ཅེས་པའི་བར་དུ་ནི་དུས་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 705]
མདོ་ལས་རྣམ་པར་འདྲེན་པ་ཞེས་པ་ནས་བཞུགས་ནས་བསམ་གཏན་མཛད་ཅེས་པའི་བར་དུ་ནི༌[^710]སྤྱོད་ལམ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏེ། དེ་ལ༌[^711]ཚིགས་བཅད་གཅིག་གིས་ནི་བསམ་གཏན་ལ་འཇུག་པ་བསྟན། དེའི་འོག་མ་གཉིས་ཀྱིས་ནི་སྣོད་དང་བཅུད་ཀྱི་འཇིག་རྟེན་བསྟན་ཏོ། །

[Block 706]
མདོ་ལས་རྫུ༌[^712]འཕྲུལ་གྱི་མེ་ཏོག་ཅེས་པ་ནས། ཞིང་རྣམས་ཐམས་ཅད་དེ་མ་ཐག་ཏུ་གཡོས། །ཞེས་པའི་བར་དུ་འདིས༌[^713]ནི་སྣོད་དང་བཅུད་ཀྱི་འཇིག་རྟེན་བསྟན་ཏེ། དེ་ལ་ཡང་སྙོམས་པར་འཇུག་པ་དང་མེ་ཏོག་གི་ཆར་འབབ་པ་དང་། མཆོད་པ་བསྟན་པས་གཡོ་བ་ལ་སོགས་པ་བསྟན་པའོ། །

[Block 707]
མདོ་ལས།

[Block 708]
དེ་ནི་ངོ་མཚར་རྨད་དུ་གྱུར། །ཅེས་པ་ནས། རབ་ཏུ་སྣང་བས་འཇིག་རྟེན་ཐམས་ཅད་མཛེས། །ཞེས་པའི་བར་དུ་ནི་རྒྱུ་ཕུན་སུམ་ཚོགས་པ་སྟེ། འོད་གཏོང་བ༌[^714]དང་ཡུལ་སྣང་བར་བྱས་པ་དང་། སངས་རྒྱས་ཀྱིས་ཀྱང་མངོན་དུ་སྣང་བ་སྟེ། འདི་ནི་དང་པོའོ། །

[Block 709]
མདོ་ལས།

[Block 710]
སེམས་ཅན་རྣམས་ཀྱི་ཤི་འཕོ་སྐྱེ་བ་སྟོན། །ཞེས་པ་ནས་དེས་མངོན་དུ་མཐོང་བ་བསྟན་ཏེ།

[Block 711]
དང་པོ་ཚིགས་བཅད་ཕྱེད་དང་དྲུག་གིས་ནི་འགྲོ་བ་དྲུག་བསྟན། ཚིགས་བཅད་གསུམ་གྱིས་ནི་སངས་རྒྱས་མཐོང་བ་བསྟན། གཅིག་གིས་ནི་ཆོས་ཐོས་པ་བསྟན། གཅིག་གིས་ནི་འཁོར་བཞི་མཐོང་བ་བསྟན། ཚིགས་བཅད་བཞིས་ནི་བྱང་ཆུབ་སེམས་དཔའ་མཐོང་བ་བསྟན་ཏེ་འདི་ནི་དང་པོའོ། །

[Block 712]
འགྲོ་བ་ནི་ལས་དང་རྒྱུ་རྣམས་ཀྱིས་འགྲོ་བར་བྱེད་པའོ། །

[Block 713]
མདོ་ལས།

[Block 714]
འདི་ལྟར་དེ་ན་ལ་ལས་རིན་ཆེན་ཞིང་། །ཞེས་པ་ནས། །རྣམ་པར་འདྲེན་པའི་འོད་ཟེར་དེ་ཡི་མཐུས།[^715] །ཞེས་པའི་བར་ནི་སངས་རྒྱས་མཐོང་བ་བསྟན་ཏེ། ཞིང་མཐོང་བ༌[^716]དང་མཆོད་པ་མཐོང་བ་དང་སངས་རྒྱས་མངོན་དུ་མཐོང་བ་དང་གསུམ་སྟེ་འདི་ནི་དང་པོའོ། །

[Block 715]
ཤཱཀྱ་ཐུབ་པའི་འོད་ཀྱིས་ནི་གསེར་གྱི་ཁ་དོག་ཏུ་སྣང་བར་བྱས། ཉི་ཟླ་སྒྲོན་མའི་འོད་ཀྱིས་ཤེལ་དང་བཻ་ཌཱུརྱའི་འོད་དུ་སྣང་བར་བྱས་ཏེ། ཐེག་པ་ཆེན་པོ་འདི་གཞན་དང་མ་འདྲེས་པ་ཉིད་དམ་པ་ཡིན་པར་བསྟན་པའི་ཕྱིར་རོ། །

[Block 716]
མདོ་ལས།

[Block 717]
ལྷ་དང་མི་དང་དེ་བཞིན་གནོད་སྦྱིན་ཀླུ། །ཞེས་པ་ནས། གསེར་གྱི་མཆོད་སྡོང་ལྟ་བུར་བལྟ༌[^717]ན་མཛེས། །ཞེས་པའི་བར་དུ་ནི་འཁོར་བརྒྱད་རྣམས་ཀྱིས་མཆོད་ནས་དེ་བཞིན་གཤེགས་པ་མཐོང་བའོ། །

[Block 718]
མདོ་ལས།

[Block 719]
བཻ་ཌཱུརྱ་ཡི་དབུས་ན་གསེར་གཟུགས་བཞིན། །ཞེས་པ་ནས། ཆོས་འདི༌[^718]རབ་ཏུ་གསུངས་ཞེས་པའི་བར་དུ་ནི་ཆོས་ཐོས་པར་བསྟན་ཏོ། །

[Block 720]
མདོ་ལས།

[Block 721]
སོ་སོའི་ཞིང་དུ་རྣམ་པར་འདྲེན་པ་ཡི། །ཞེས་པ་ནས། འདིའི་ཅི་ཞིག་ཅེས་ནི་ཕན་ཚུན་འདྲི། །ཞེས་པའི་བར་དུ་འཁོར་རྣམ་བཞི་བསྟན་པ་དང་། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱིས་ཆོས་རྟོགས་ཤིང་མོས་པ་སྐྱེ་བ་དང་ཁྱིམ་ན་གནས་པ་དང་རབ་ཏུ་བྱུང་བ་གཉི་གས་བྱང་ཆུབ་ཀྱི་སྤྱོད་པ་ཐོབ་པ་དང་། ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་དབང་དུ་གྱུར་པར༌[^719]བསྟན་ཏོ། །

[Block 722]
མདོ་ལས།

[Block 723]
གནོད་སྦྱིན་ལྷ་མིས་དེ་མཆོད་མ་ཐོགས་པར། །ཞེས་པ་ནས། ང་ཡི༌[^720]ཆོས་མཛོད་འདི་ལ་ཁྱོད་མངོན་སུམ། །ཞེས་པའི་བར་དུ་ནི་ལན་བཏབ་པ་ཕུན་སུམ་ཚོགས་པ་སྟེ། ཚིགས་བཅད་དང་པོ་གཅིག་གིས་ནི་བཤད་པའི་རྒྱུ་བསྟན། ཕྱི་མ་གཉིས་ཀྱིས་ནི་ཡུན་རིང་ཐུང་བསྟན། ཏིང་ངེ་འཛིན་ལས་བཞེངས་མ་ཐག་ཏུ་སེམས་ཅན་རྣམས་བྱང་ཆུབ་ལ་འཛུད་ཅེས་པའི་དོན་ཏོ། །

[Block 724]
མདོ་ལས།

[Block 725]
ཇི་ལྟར་སྲོག་ཆགས་ཕན་ཕྱིར་ངས་བསྟན་པ། །ཞེས་པ་ནས། །

[Block 726 [VERSE]]
དེ་ཚེ་རྒྱལ་བས་ཆོས་རབ་འདི་གསུངས་པ། །
བར་གྱི་བསྐལ་པ་དྲུག་ཅུ་ཚང་བར་དེ། །

[Block 727]
ཞེས་པའི་བར་དུ་ནི་དུས་རིང་བ་བསྟན་པ་དང་། ལྟས་མཐུན་པ་བསྟན་པ་དང་། བརྩོན་འགྲུས་ཀྱིས༌[^721]འབྱུང་བར་བསྟན་པ་དང་། དེ་བཞིན་གཤེགས་པ༌[^722]ཡང་བསྐལ་པར་ཏིང་ངེ་འཛིན་ལས་མི་བཞེངས་ནས་སེམས་ཅན་མ་རབས༌[^723]ཉོན་མོངས་པ་སྤོང་བར་མི་རྩོལ་བ་མི་རིགས་པར་བསྟན་པ་དང་། སེམས་ཅན་ལ་ཐུགས་རྗེ་ཞིང་ཕན་གདགས་པར་དགོངས་པ་དང་དུས་ལ་བབ་པ༌[^724]རྣམས་ལུང་བསྟན་ཞིང་མྱ་ངན་ལས་འདས་པའི་བདེ་བ་ལ་འཇོག་པ་དང་ལོངས་སྤྱོད་ཆེ་བའི་རྒྱུ་བསྟན་ཏེ་ཆོས་འཛིན་ཅིང་དགེ་བའི་རྒྱུ་ལ་འཇུག་པར་བསྟན་པའོ། །

[Block 728 [HEADING]]
###### **རྒྱུ་བཞི་པོ།** ^4-1-10-2-5-2-0

[Block 729]
མདོ་ལས། །

[Block 730]
དེ་ཡི་སློབ་མར་གྱུར་པ་བརྒྱད་བརྒྱ་དག །ཅེས་པ་ནས། །དེ་དག་སངས་རྒྱས་བྱེ་བ་མང་པོ་མཐོང་། ། ཞེས་པའི་བར་དུ་འདིས་ནི་དེ་བཞིན་གཤེགས་པ་ཤིན་ཏུ་བསྟན་པའི་ཆོས་ཀྱི་རྒྱུ་བསྟན་པ་སྟེ། ཐེག་པ་ཆུང་ངུའི་ཚུལ་དུ་བསྐལ་པ་གྲངས་མེད་པ་གསུམ་ནི་ལུགས་ལས་བཟློག་པ༌[^725]བསྟན་པའོ། །

[Block 731]
བསྐལ་པ་དང་པོའི་ཚེ་སངས་རྒྱས་ཤཱཀྱ་ཐུབ་པ་མཐོང་། དེའི་འོག་ཏུ་སངས་རྒྱས་ཁྲག་ཁྲིག༌[^726]བདུན་ཅུ་རྩ་ལྔ་མཐོང་། བསྐལ་པ་གཉིས་པར་སངས་རྒྱས་རིན་ཆེན་གཙུག་ཕུད་མཐོང་སྟེ། ཡང་སངས་རྒྱས་ཁྲི་ཕྲག་བདུན་ཅུ་རྩ་དྲུག་མཐོང་། བསྐལ་པ་གསུམ་པར་སངས་རྒྱས་མར་མེ་མཛད་མཐོང་སྟེ།

[Block 732]
སངས་རྒྱས་ཁྲི་ཕྲག་བདུན་ཅུ་རྩ་བདུན་མཐོང་ངོ་། །མདོ་ལས།

[Block 733]
དྲང་སྲོང་ཆེན་པོ་དེ་དག་བཀུར་སྟི་བྱས། །ཞེས་པ་ནས། །བྱང་ཆུབ་མཆོག་ཏུ་གཅིག་གིས་གཅིག་ལུང་བསྟན། །ཞེས་པའི་བར་གྱིས་ནི་འཇུག་པར་འགྱུར་བའི་རྒྱུ་བསྟན་ཏེ། ཀུན་གྱིས་བྱང་ཆུབ་ཆེན་པོ་ཐོབ༌[^727]ཅེས་པའི་དོན་ཏོ། །

[Block 734]
མདོ་ལས།

[Block 735]
སངས་རྒྱས་དེ་དག༌[^728]རིམ་གྱིས་འབྱུང་བ་ཡིན།[^729] །ཞེས་པ་ནས། །སྲོག་ཆགས་བྱེ་བ་སྟོང་ཡང་དུལ་བར་བྱས། །ཞེས་པའི་བར་དུ་ཚིགས་བཅད་དྲུག་གིས་ནི་དྲན་པའི་རྒྱུ་བསྟན་ཏེ། ཚིགས་བཅད་དང་པོ་གཅིག་གིས་ནི་རྒྱལ་བུ་བརྒྱད་ལ་དགོངས་པ་བསྟན། དེའི་འོག་མ་ལྔས་ནི་འཁོར་བརྒྱད་བརྒྱ་ལ་དགོངས་པ་བསྟན་ཏོ། །

[Block 736]
མདོ་ལས། །

[Block 737]
གང་སྔོན་བདེ་བར་གཤེགས་པ་དེ་ཡི་སྲས། །ཞེས་པ་ནས། །ཕྱོགས༌[^730]རྣམ་པར་གྲགས་ཞེས་པའི་བར་དུ་ནི་འཁོར་རྣམས་ལ་དགོངས་པ་བསྟན་ཏེ། ཚིགས་བཅད་ཕྱེད༌[^731]དང་གསུམ་གྱིས་ཉོན་མོངས་པའི་རྒྱུ་བསྟན། ཡང་ཚིགས་བཅད་ཕྱེད༌[^732]དང་གསུམ་གྱིས་ནི་དག་པའི་རྒྱུ་བསྟན་ཏེ། འདི་ནི་དང་པོ་དང་སྦྱར་རོ། །

[Block 738]
ཁེ་དང་གྲགས་པ་དང་ཆོ་རིགས་ལ་ཆགས་པ༌[^733]ཐོས་པར་རྩོལ་བའི་ཆགས་པ་དེ༌[^734]དག་གྲགས་པར་འདོད་པའོ། །

[Block 739]
མདོ་ལས།

[Block 740]
དེ་ཡང་དགེ་བ་རྣམས་ཀྱིས༌[^735]ལས་དེ་དག །ཅེས་པ་ནས། །སྲོག་ཆགས་སྟོང་ཕྲག་བྱེ་བ་འདུལ་བར་འགྱུར། །ཞེས་པའི་བར་གྱིས་ནི་རྣམ་པར་དག་པའི་རྒྱུ་བསྟན་ཏོ། །
--- END BLOCKS ---
