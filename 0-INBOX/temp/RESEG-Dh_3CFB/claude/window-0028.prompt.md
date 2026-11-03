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
[Block 981 [VERSE]]
དང་པོ་ཉིད་ནས་འདི་རུང་ཉིད། །
དེ་ལ་ལྟོས་པ་མི་རུང་སྟེ། །
འགྱུར་བའི༌[^839]མེད་པའི་སྤྱི་དེ་ནི། །
སྤྱི་དང་ལྡན་པ་གང་ལས་ཡིན། །

[Block 982]
བྱེད་པ་པོ་ལས་གསལ་བར་བྱེད་པ་ནི་ཁྱད་པར་ཅུང་ཞིག་ཀྱང་མེད་པ་ཡིན་ཏེ། གཞན་རང་གི་ཡུལ་ལ་རྣམ་པར་ཤེས་པ་བསྐྱེད་པར་ནུས་པ་རིགས་མཐུན་པའི་ཉེ་བར་ལེན་པ་ལ་ལྟོས་པའམ། ལྟོས་པ་མེད་པའི་དངོས་པོ་སྐྱེད་པར་བྱེད་པ་ཁོ་ན་གསལ་བར་བྱེད་པ་ཞེས་བྱའོ། །

[Block 983]
གཞན་དག་ཏུ་ནི་བསྐྱེད་པར་བྱ་བ་ལ་ཤེས་པ་སྐྱེ་བ་ནུས་པ་འཕངས་པ་མེད་པའི་ཕྱིར་སྐྱེད་པར་བྱེད་པ་ཙམ་གྱི་རྒྱུ་ཉིད་ཡིན་ནོ། །

[Block 984]
གལ་ཏེ་གང་ལས་རྣམ་པར་ཤེས་པ་བསྐྱེད་པར་རུང་བ་སོ་སོར་སྣང་བ་ཐོབ་པ་གང་ཡིན་པ་དེ་དེའི་བསྐྱེད་བྱར་མི་འགྱུར་ན། དེ་ནི་འདིའི་རང་བཞིན་དུ་གྱུར་པའི་རུང་བ་ཉིད་ནི་དང་པོ་ཉིད་ནས་ཡོད་པའི་ཕྱིར་རྣམ་པར་ཤེས་པ་སྐྱེད་པར་བྱེད་པ་དེ་ལ་ལྟོས་པ་མ་ཡིན་ནོ།[^840] །

[Block 985]
འདི་ནི་གཞན་དུ་འགྱུར་བ་ཉིད་ཡིན་ན་དེ་ཉིད་དེ་ལས་འགྱུར་བའི་ཕྱིར། གནས་པ་བཞིན་དུ་ཐལ་བར་འགྱུར་བ་དེ་བས་ན་གསལ་བར་བྱེད་པ་དེ་བྱེད་པ་མ་ཡིན་ཞིང་གཞན་ཡང་བྱེད་པ་མ་ཡིན་པ་དེ་ལྟར་ན་ཅུང་ཞིག་ཀྱང་མི་བྱེད་པ་དང་ལྟོས་པར་བྱ་བ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་འགལ་བ་ཡིན་ནོ། །

[Block 986]
འབྲས་བུ་ཉིད་ཡིན་པའི་ཕྱིར་སྐྱེད་པར་བྱེད་པ་མ་ཡིན་པ་དུ་བ་ལ་སོགས་པ་ཡང་གསལ་བར་བྱེད་པ་མ་ཡིན་ནམ། གསལ་བར་བྱེད་པ་ཡིན་པ་ནི་བདེན་ཏེ། དུ་བ་ལ་ལྟོས་ནས་མེས་ནི་རྣམ་པར་ཤེས་པ་སྐྱེད་པར་བྱེད་པ་མ་ཡིན་ཏེ། དེ་ལྟ་བུར་གྱུར་པའི་མེ་ནི་མངོན་སུམ་དུ་སྐྱེད་པར་བྱེད་པ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 987]
དེ་ལ་ཉེ་བར་ལེན་པའི་སྟོབས་ཁོ་ནས་ནི་ཤེས་པ་བསྐྱེད་པར་འགྱུར་གྱི། ཡུལ་གྱི་སྟོབས་ཀྱིས་ནི་མ་ཡིན་ཏེ། དེ་མེད་དུ་ཟིན་ཀྱང་དེ་ལ་བརྒྱུད་པས་རྟགས་ཀྱི་རྗེས་སུ་འབྲང་བའི་སྒོ་ནས་ཡོད་པའི་ཕྱིར་རོ། །

[Block 988]
སྤྱིའི་མཚན་ཉིད་དུ་སྣང་བའི་ཤེས་པ་དེ་དག་ཀྱང་ཡུལ་ཉེ་བ་ཅན་ནམ། ཡུལ་གྱི་སྟོབས་ཀྱིས་སྐྱེས་པ༌[^841]མ་ཡིན་ནོ་ཞེས་བྱ་བ་དེ་བསྟན་པ་དང་སྟོན་པར་ཡང་འགྱུར་རོ། །

[Block 989]
དེ་བས་ན༌[^842]མངོན་སུམ་དུ་སྦྱོར་བས་རྣམ་པར་ཤེས་པ་བསྐྱེད་པའི་ཡུལ་གང་ཡིན་པ་དེ་ནི་འདིར་གཞན་ལ་ལྟོས་པར་འགྱུར་བས་གདོན་མི་ཟ་བར་དེ་ལས་བདག་ཉིད་ཐོབ་པར་འགྱུར་གྱི། བདག་ཉིད་ཐོབ་པ་འདི་ནི་སྤྱི་བརྟག་པ་གང་ལས་ཀྱང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 990]
དེའི་ཕྱིར་དེ་ནི་ཅི་ནས་ཀྱང་གསལ་བར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 991]
སྤྱི་ནི་གསལ་བར་རུང་བ་ཉིད་ཐོབ་པ་ཡིན་པར་མི་སྨྲའོ། །

[Block 992]
འོ་ན་ཅི༌[^843]ཡིན་ཞེ་ན། རང་གི་རྟེན་ལ་འཕྲོད་པ་འདུ་བ་ལས་ཏེ། རང་གི་རྟེན་ལས༌[^844]འཕྲོད་པ་འདུ་བས་འབྲེལ་པ་དེ་ནི་བདག་ཉིད་དམ་གཞན་ལ་རྣམ་པར་ཤེས་པའི་རྒྱུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 993]
འདིར་སྐྱེད་པར་བྱེད་པ་དང་བསྐྱེད་པར་བྱ་བ་དག་གི་རྟེན་དང་བརྟེན་པར་ཡོད་པའི་མཚན་ཉིད་ཀྱི་འཕྲོད་པ་འདུ་བ་འདི་ཅི་ཞིག་ཡིན་ཞེས་བཤད་པ་ཡིན་ནོ། །

[Block 994]
རང་གི་རྟེན་གྱིས་འཕྲོད་པ་འདུ་བ༌[^845]ལ་ལྟོས་པ་ཅན་རྣམ་པར་ཤེས་པའི་རྒྱུ་ཡིན་པ་དེས་བསྐྱེད་པར་བྱ་བ་ཁོ་ནར་འགྱུར་ཏེ། རྒྱུ་དེའི་ངོ་བོ་སྔ་ན་མེད་པའི་ཕྱིར་དང་། ཕྱིས༌[^846]དེ་ལས་ཡོད་པའི་ཕྱིར་རོ། །

[Block 995]
དེའི་ངོ་བོ་རྟག་ཏུ་ཡོད་པ་ཡིན་ན༌[^847]འཕྲོད་པ་འདུ་བ་ལས་སྔར་ཡང་རྣམ་པར་ཤེས་པ་སྐྱེ་བར་ཐལ་བའི་ཕྱིར་རོ། །

[Block 996]
གསལ་བ་ནི་སྤྱི་ལེགས་པར་བྱས་པས་གསལ་བར་བྱེད་པ་ནི་མ་ཡིན་ནོ། །

[Block 997]
འོ་ན་ཅི་ཡིན་ཞེ་ན། དེ་འཛིན་པའི་དབང་པོ་ལེགས་པར་བྱས་པས་སོ། །

[Block 998]
དེ་ཡང་།

[Block 999]
མིག་སྨན་སོགས་བཞིན་གསལ་བ་ལས།

[Block 1000]
[^848] །

[Block 1001 [VERSE]]
དབང་པོ་ལེགས་པར་བྱས་པ་མིན། །
དེ་ཡོད་མེད་པའི་དུས་རྟག་ཏུ། །
རྟོགས་པ་ཐ་དད་མེད་ཕྱིར་རོ། །

[Block 1002]
མིག་སྨན་ལ་སོགས་པས་དབང་པོ་ལེགས་པར་བྱས་པས་རྟོགས་པའི་ཕྱིར། ཕུལ་དུ་བྱུང་བ་འགའ་ཞིག་ཐོབ་པར་བྱེད་དེ། གསལ་བ་དང་མི་གསལ་བའི་ཁྱད་པར་གྱི་ཕྱིར་རོ། །

[Block 1003]
དེ་མི་བྱེད་པ་ཡང་དེ་ལེགས་པར་བྱས་པ་ཉིད་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1004]
དེ་ལྟར་གསལ་བ་ལས་དབང་པོའི་ལེགས་པར་བྱས་པ་འགའ་ཞིག་ཀྱང་ཡོད་པ་མ་ཡིན་ཏེ། དེ་ཡོད་པ་དང་མེད་པའི་དུས་རྟག༌[^849]ཏུ་རྟོགས་པ་ལ་ཁྱད་པར་མེད་པའི་ཕྱིར་རོ། །

[Block 1005]
ཡུལ་ལེགས་པར་བྱ་བ༌[^850]ནི་དབང་པོའི་ཁྱད་པར་མེད་ན་ཡང་དེ་ཁྱད་པར་བྱ་བའི་ཕྱིར་ཕན་འདོགས་པར་འགྱུར་གྱི། དབང་པོ་ལེགས་པར་བྱས་པ་ལས་ནི་མ་ཡིན་ནོ།། །།

[Block 1006]
བམ་པོ་ལྔ་པ། གལ་ཏེ་སྔར་མ་མཐོང་བ་མཐོང་བའི་ནུས་པ་བྱེད་པའི་ཕྱིར། ཕན་འདོགས་པར་བྱེད་པ་ཡིན་ནོ་ཞེ་ན། དེ་ནི་དབང་པོ་ལས་འདས་པའི་དོན་མཐོང་བས་ཇི་ལྟར་རྟོགས་པར་ཁྱད་པར་མེད་པར་གྱུར།[^851] གཅིག་སོ་སོར་ངེས་པ་ཡིན་ན་ཡང་སྤྱི་གཞན་མཐོང་བ་པོར་མི་འགྱུར་ལ། བསལ་བས༌[^852]ཀྱང་ལེགས་པར་བྱས་པའི་ཕྱིར། དེ་དག་མཐོང་བ་ན་དེས་བསལ་བར་བྱེད་པ༌[^853]སྤྱི་དག་ནི་ནམ་ཡང་མ་ངེས་པའམ། གཞན་གཅིག་ཀྱང་ངེས་པར༌[^854]མི་འགྱུར་ཏེ། དབྱེ་བ་མེད་པ་དེ་ནི་དེ་དག་ལ་ཁྱད་པར་མེད་པའི་ཕྱིར་རོ། །

[Block 1007]
གལ་ཏེ་གསལ་བས་དབང་པོ་ལེགས་པར་བྱས་ཀྱང་རུང་། གལ་ཏེ་དབང་པོ་ལེགས་པར་མ་བྱས་ཀྱང་རུང་། སྤྱི་ནི་རྣམ་པར་ཤེས་པ་སྐྱེད་པར་བྱེད་པའི་རང་བཞིན་ཡིན་པས་རང་བཞིན་ལས་མི་འདའ་བའི་ཕྱིར། དབང་པོ་ལེགས་པར་བྱ་བ༌[^855]ལྟོས་པ་མེད་པ༌[^856]ཁོ་ནར་རྣམ་པར་ཤེས་པ་བསྐྱེད་དོ། །

[Block 1008]
གལ་ཏེ་དབང་པོ་ལེགས་པར་བྱ་བའི༌[^857]ལྷན་ཅིག་བྱེད་པ་ཅན་ཉིད་ཡིན་པའི་ཕྱིར་གཅིག་པུ་ནི་ནུས་པ་མ་ཡིན་ནོ་ཞེ་ན། བྱེད་པ་མེད་པ་ཕུལ་དུ་བྱུང་བ་འདིའི་ལྷན་ཅིག་བྱེད་པའི་དོན་གང་ཡིན། ལྷན་ཅིག་བྱེད་པས་ཁྱད་པར་དུ་བྱས་པའི་བདག་ཉིད་ཐོབ་པའི་ཕྱིར། དངོས་པོ་མི་རྟག་པ་དག་ནི་དེ་ལ་ལྟོས་པ་ཡིན་ཏེ། དེ་དག་གིས་སྐྱེད་པར་བྱེད་པའི་བདག་ཉིད་གང་ཡིན་པ་དེ་ནི་དེའི་ཚེ་དེ་ཉིད་ལས་འགྱུར་བའི་ཕྱིར་སྐྱེད་པར་བྱེད་པ་དག་ཉིད་ནི་ཕན་ཚུན་ལྟོས་པ་ཡིན་ནོ། །

[Block 1009]
སྤྱི་གཞན་གྱིས་མ་བསྒྲུབ་པ་རྟག་པའི་རང་བཞིན་དེ་ཡང་ཅིའི་ཕྱིར་དབང་པོ་ལ་ལྟོས་པ་ཡིན། ཡན་གར་བ་དེ་ནི་རང་བཞིན་མེད་པ་གང་ཡིན་པ་དེས་ཀྱང་ཇི་ལྟར་ཡང་མི་འགྱུར་རོ། །

[Block 1010]
བསལ་བ་དབང་པོ་ལེགས་པར་བྱས་པའི་ཕྱིར་དེའི་ལྷན་ཅིག་བྱེད་པ་ཅན་གྱི་སྤྱིའི་ནི་རྣམ་པར་ཤེས་པའི་རྒྱུ་ཡིན་པ་དེ་ལྟར་ན་བརྒྱུད་པས་སྤྱི་བསལ་བའི་འབྲས་བུ་ཉིད་དུ་བསྟན་པར་འགྱུར་རོ། །

[Block 1011]
གཞན་ཡང་།

[Block 1012 [VERSE]]
གལ་ཏེ་རིགས་དང་བསལ་བྱེད་དག །
རིགས་དང་ལྡན་པ་ཉིད་འདོད་ན། །
སྒྲོན་མ་ལ་སོགས་བསལ་བྱེད་ནི། །
བ་ལང་ཉིད་སོགས་དེ་ལྡན་ཐོབ། །

[Block 1013]
གང་ཞིག་རྣམ་པར་ཤེས་པའི་རྒྱུ་གང་ཡིན་པ་དེ་ནི་དེའི་བསལ་བར་བྱེད་པ༌[^858]ཡིན་ལ། བ་ལང་ཉིད་ལ་སོགས་པ་ལ་སྒྲོན་མ་ལ་སོགས་པ་ཡང་རྣམ་པར་ཤེས་པའི་རྒྱུ་ཉིད་ཡིན་ཏེ། སྣང་བ༌[^859]ལེགས་པར་བྱས་པ་ལ་ལྟོས་པའི༌[^860]མིག་གིས་དོན་རྟོགས་པའི་ཕྱིར་རོ། །

[Block 1014]
དེ་བས་ན་སྒྲོན་མ་ལ་སོགས་པ་ནི་བ་ལང་ཉིད་ལ་སོགས་པ་དེ་དང་ལྡན་པར་འགྱུར་རོ། །

[Block 1015]
དེ༌[^861]བསལ་བ་ལས་ཀྱང་རྣམ་པར་ཤེས་པའི༌[^862]རྒྱུ་ཉིད་ལ་མ་གཏོགས་པ་གཞན་སྤྱི་མངོན་པར་བསལ་བ་འགའ་ཞིག་ཀྱང་ཡོད་པ་མ་ཡིན་ཏེ། ཕུལ་དུ་བྱུང་བའི་རང་གི༌[^863]ངོ་བོ་ཉིད་བྱ་བར་མི་ནུས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1016]
གལ་ཏེ་འཕྲོད་པ་འདུ་བ་མངོན་པར་བསལ་བ་ཡིན་ནོ་ཞེ་ན། དེའི་ལན་ནི་དེའི་འཕྲོད་པ༌[^864]འདུ་བ་ནི་མི་རུང་བའི་ཕྱིར་རོ་ཞེས་བྱ་བས་བཤད་ཟིན་ཏོ། །

[Block 1017]
འདི་ནི་བསལ་བ་དང་ལྷན་ཅིག་འཕྲོད་པ་འདུ་བ་ཙམ་དུ་སྐྱེས་པ་ཡིན་གྱི༌[^865]ཁྱད་པར་འགའ་ཞིག་ཀྱང་མ་ཡིན་པ་སྔ་མ་བཞིན་དུ་ཕྱིས་ཀྱང་ཤེས་པའི་རྒྱུ་ཉིད་དུ་མི་འགྱུར་རོ། །

[Block 1018]
འཕྲོད་པ་འདུ་བ་ཁོ་ན་ལས་ཤེས་པའི་རྒྱུ་ཉིད་ཡིན་ན་ནི་གཞན་རང་གི་རྟེན་ལ་འཕྲོད་པ་འདུ་བ་དག་ཀྱང་མཐོང་བར་འགྱུར་བ་དེ་བས་ན་བསལ་བར་བྱེད་པ་ཉིད་ནི་ཤེས་པའི་རྒྱུ་ཉིད་ཡིན་ནོ། །

[Block 1019]
དེ་ཡང་སྒྲོན་མ་ལ་སོགས་པ་དང་འདྲ་བའི་ཕྱིར། ཐལ་བར་འགྱུར་བ་དེ་ཉིད་དོ། །

[Block 1020]
དེ་བས་ན་སྤྱིའི་གནས་པ་ནི། རྟེན་མ་ཡིན་པ་དང་། བསལ་བ་མ་ཡིན་པས་ན་མི་གནས་པའི་ཕྱིར་ཤེས་པའི་རྒྱུ་མ་ཡིན་ནོ། །
--- END BLOCKS ---
