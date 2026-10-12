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
[Block 911]
འཁོར་བ་ནི་ཕྱིན་ཅི་ལོག་གི་བདག་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 912]
གང་ཡང་ཆོས་ཀྱི་རྣམ་གྲངས་གཟིངས་ལྟ་བུར་ཤེས་པས་ཆོས་རྣམས་ཀྱང་སྤང་བར་བྱ་བས་ན། ཆོས་མ་ཡིན་པ་ལྟ་ཅི་སྨོས་ཞེས་གསུངས་པ་ནི། དེ་ལ་ཕྱིན་ཅི་ལོག་ཏུ་མངོན་པར་ཞེན་པ་སྤང་བར་བྱའོ་ཞེས་གསུངས་ཀྱི། དགོས་པའི་དོན་རྫོགས་པའི་དོན་དུ་ཡང་གནས་པར༌[^508]མི་བྱའོ་ཞེས་གསུངས་པ་ནི་མ་ཡིན་ནོ། །

[Block 913]
དེ་ཡང་ཆོས་ཡོངས་སུ་གཟུང་བར་བྱ་སྟེ། ལོག་པ་ནི་གཟུང་བར༌[^509]མི་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 914]
དེ་བས་ན།

[Block 915 [VERSE]]
དུས་ཀུན་དུ་ནི་ཐབས་དང་ནི། །
ཤེས་རབ་ཕ་རོལ་བདག་ཅན་ནི། །
བརྟེན་བྱ༌[^510]གང་ཕྱིར་དེ་ལས་ནི། །
མི་གནས་མྱ་ངན་འདས་པར་འགྱུར། །

[Block 916]
ཞེས་ཁུངས་དང་བཅས་པར་གསུངས་སོ། །

[Block 917]
བླ་མའི་ཞལ་ནས་ཀྱང་དེ་ལྟ་བས་ན་དུས་ཐམས་ཅད་དུ་ཐབས་དང་ཤེས་རབ་གཉིས་ཀ་དང་ལྡན་པར་བྱ་ཞིང་། བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་ཟུང་དུ་འབྲེལ་པར་བསག་པར་བྱའོ་ཞེས་གསུངས་སོ། །

[Block 918]
དེ་ལྟར་ཐབས་དང་ཤེས་རབ་གཉིས་ཟུང་དུ་འབྲེལ་པ༌[^511]འཇུག་པ་དེ་གཉིས་ཀ་དང་ལྡན་པར་བྱའོ་ཞེས་བྱ་བ་དེ་བསྟན་ནས། ད་ནི་ཐབས་ཞེས་བྱ་བ་དང་ཤེས་རབ་ཅེས་བྱ་བ་དེ་གཉིས་ཉིད་ཇི་ལྟ་བུ་ཡིན་པ་བཤད་པའི་ཕྱིར།

[Block 919 [VERSE]]
ཤེས་རབ་གང་དང་ཐབས་གང་ཞེས། །
ཐེ་ཚོམ་དག་ནི་སྤང་བའི་ཕྱིར། །
ཐབས་དེ༌[^512]དང་ནི་ཤེས་རབ་ཀྱི། །
ཡང་དག་དབྱེ་བ་གསལ་བར་བྱ། །

[Block 920]
ཞེས་བྱ་བ་དེ་སྨྲས་ཏེ། ཐེ་ཚོམ་དག་ནི་སྤང་བའི་ཕྱིར། །ཞེས་པ་ནི༌[^513]སྔོན་གྱི་སློབ་དཔོན་ཆེན་པོ་དག་འདི་གཉིས༌[^514]ལ་ཐ་དད་པར་གསུངས་སོ། །

[Block 921]
དེ་བས་ན་ཐབས་དང་ཤེས་རབ་ཀྱི་དབྱེ་བ་འདི་ལྟ་བུ་ཡིན་ཏེ།

[Block 922]
གཞུང་ཁ་ཅིག་ལས།

[Block 923 [VERSE]]
ཐབས་ནི་བྱང་ཆུབ་སེམས་དཔའ་ཡིད།[^515] །
འགྲོ་ལ་སྙིང་རྗེ་ཆེན་པོ་སྟེ། །
དེ་ཡང་དམིགས་པའི༌[^516]དབྱེ་བ་ཡིས། །
རྣམ་པ་གསུམ་དུ་འགྱུར་བ་ཡིན། །

[Block 924]
ཞེས་བྱ་བ་འབྱུང་བ་དང་། ཡང་གཞན་དག་ནི་ཀུན་རྫོབ་ཀྱི་རྣམ་པའི་བྱང་ཆུབ་ཀྱི་སེམས་དེ་ནི་ཐབས་ཡིན་ཞེས་འབྱུང་ངོ་། །བླ་མ་དཔལ་བྱང་ཆུབ་བཟང་པོའི་ཞལ་ནས༌[^517]འདི་སྐད་དུ།

[Block 925 [VERSE]]
ཤེས་རབ་ཕ་རོལ་ཕྱིན་སྤངས་པའི། །
སྦྱིན་པའི་ཕ་རོལ་ཕྱིན་ལ་སོགས། །
དགེ་བའི་ཚོགས་རྣམས་ཐམས་ཅད་དག །
རྒྱལ་བ་རྣམས་ཀྱིས་ཐབས་སུ་བཤད། །

[Block 926]
ཅེས་གསུངས་པ་དེ་བདག༌[^518]གི་རྩ་བར་བཀོད་པ་ཡིན་ནོ། །

[Block 927]
སྦྱིན་པའི་ཕ་རོལ༌[^519]ཕྱིན་ལ་སོགས། །ཞེས་བྱ་བ་ནི། འདིར་སྦྱིན་པ་ནི་རྣམ་པ་གསུམ་སྟེ། སྦྱིན་བདག་དང་། རྫས་དང་། ཞིང་གི་དབྱེ་བས་སོ། །

[Block 928]
སྦྱིན་བདག་ནི་རྙེད་པ་དང་བཀུར་སྟིའམ། གྲགས་པ་དང་སྙན་པའི་ཕྱིར་རམ། གཞན་གྱིས༌[^520]བསྐུལ་བའི་ཕྱིར་རམ། སྙིང་རྗེའི་ཕྱིར་རམ་སྲི་ཞུའི༌[^521]ཕྱིར་ལ་སོགས་པའོ། །

[Block 929]
རྫས་ནི་འདི་ལྟར་ཆོས་དང་ཟང་ཟིང་དང་མི་འཇིགས་པ་དང་། བྱམས་པ་ལ་སོགས་པའོ། །

[Block 930]
ཞིང་ནི༌[^522]འདི་ལྟར་དཀོན་མཆོག་གསུམ་དང་བླ་མའི་གནས་དང་། འགྲོ་བ་ལྔའི་སེམས་ཅན་ཐམས་ཅད་དོ། །

[Block 931]
དེ་ཡང་རྡོ་རྗེ་གདན་བཞི་པའི་རྒྱུད་ལས།

[Block 932]
དམངས་རིགས་སྟོང་ཕྲག་དྲུག་ཅུ་ནི། །བྲམ་ཟེ་གཙང་མ་གཅིག་ལ་སྦྱར། །ཞེས་བྱ་བ་ལ་སོགས་པ་རྒྱས་པར་གསུངས་པ་དང་།

[Block 933]
ཡང་མདོ་ལས།

[Block 934]
དགེ་བསྙེན་སྟོན་པ་གཞན་ལ་མི་བརྟེན་པ། །ཞེས་བྱ་བ་ལ་སོགས་པ་རྒྱས་པར་གསུངས་པ་དང་། ཆོས་བཤད་པ་བརྒྱ་པ་ལས་ཀྱང་རྒྱས་པར་གསུངས་སོ། །

[Block 935]
གཞན་ཡང་བཅོམ་ལྡན་འདས་ཀྱིས་འཇིག་རྟེན་གསུམ་ལས་རྣམ་པར་རྒྱལ་བ་ཞེས་བྱ་བ་རྣལ་འབྱོར་གྱི་རྒྱུད་ལས།

[Block 936]
འདི་སྐད་དུ། དབང་བསྐུར་བའི་སྦྱིན་པ་དང་། ཆོས་ཀྱི་སྦྱིན་པ་དང་། ནོར་གྱི་སྦྱིན་པ་དང་། ཟས་ཀྱི་སྦྱིན་པ་དང་། མི་འཇིགས་པའི་སྦྱིན་པ་དང་། བྱམས་པའི་སྦྱིན་པའོ། །

[Block 937]
དེ་དག་སློབ་མ་དང་མི་སྣང་བའི་སེམས་དང་། དགེ་སྦྱོང་དང་བྲམ་ཟེ་དང་ཕོངས་པ་དང་དུད་འགྲོ་དང་གྱོད་ཀྲིན་ཅན་དང་། འགྲོ་བ་མཐའ་དག་གོ་རིམས་བཞིན་ནོ། །

[Block 938]
སོགས་ཞེས་བྱ་བ་ནི་ཕ་རོལ་ཏུ་ཕྱིན་པ་གཞན་ཡང་བཤད་པ་ཡིན་ཏེ། ཚུལ་ཁྲིམས་ནི་འདི་ལྟར་སེམས་དང་པོ་བསྐྱེད་པའི་བྱང་ཆུབ་སེམས་དཔའ་དང་། སྤྱོད་པ་ལ་ཞུགས་པ་དང་། ཕྱིར་མི་ལྡོག་པ་དང་། མི་སྐྱེ་བའི་ཆོས་ལ་བཟོད་པ་ཐོབ་པ་དང་། སྐྱེ་བ་གཅིག་གིས་ཐོགས་པ་དང་། སྲིད་པ་ཐ་མའི་བྱང་ཆུབ་སེམས་དཔའི་ཚུལ་ཁྲིམས་དག་གོ། །

[Block 939]
ཕ་རོལ་ཏུ་ཕྱིན་པ་གཞན་ནི་མདོ་ལས་འབྱུང་བ་བཞིན། དགེ་བའི་ཆོས་རྣམས་ཐམས་ཅད་དག །ཅེས་པ་ནི་འོག་ནས་འཆད་པར་འགྱུར་རོ། །

[Block 940]
གཞན་ཡང་འདི་དག་གི་དོན་རྒྱས་པ་ནི་མདོ་སྡེ་དང་གཞན་ཡང་མདོ་སྡེའི་དོན་གསལ་བར་བྱེད་པ་མདོ་ཀུན་ལས་བཏུས་པ་དང་། བྱང་ཆུབ་སེམས་དཔའི་ས་དང་། སྤྱོད་འཇུག་དང་། བསླབ་པ་ཀུན་ལས་བཏུས་པ་དང་། སློབ་དཔོན་དཔའ་བོའི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་གཏམ་དག་ཏུ་བལྟ་བར་བྱའོ། །

[Block 941]
ཐབས་གོམས་དབང་གིས་ཞེས་པའི་ཤློ་ཀ་ནི་དཀྱུས་ཇི་ལྟ་བ་བཞིན་ནོ།[^523] །

[Block 942]
ཤེས་རབ་གང་ཡིན་ཞེ་ན། འདི་ལྟར་ལྷན་ཅིག་སྐྱེས་པའམ། ཐོས་པ་ལས་བྱུང་བའམ། བསམས་པ༌[^524]ལས་བྱུང་བའམ། བསྒོམས་པ༌[^525]ལས་བྱུང་བའམ།

[Block 943]
ཡང་གཞུང་དག་ལས།

[Block 944 [VERSE]]
གང་ཞིག་སྤྲོས་པ་ཐམས་ཅད་ཀྱི། །
གནས་དང་ཚིག་ཏུ་མ་གྱུར་པ། །
འཇུག་དེ་ཐུགས་ཀྱི་རྡོ་རྗེ་ཡིས། །
ཤེས་རབ་ཅེས་ནི་བྱ་བར་བསྒྲགས། །

[Block 945]
ཞེས་གསུངས་ཏེ་དེ་ཉིད་དོ། །

[Block 946]
དེ་བཞིན་དུ་རྩ་བ་ལས་ཀྱང་།

[Block 947 [VERSE]]
ཕུང་པོ་ཁམས་དང་སྐྱེ་མཆེད་རྣམས། །
སྐྱེ་བ་མེད་པར་རྟོགས་གྱུར་པའི། །
རང་བཞིན་སྟོང་པ་ཉིད་ཤེས་པ། །
ཤེས་རབ་ཅེས་ནི་ཡོངས་སུ་བཤད། །

[Block 948]
ཅེས་སྨྲས་ཏེ། ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད་དུ་ཕྱི་ནང་གི་ཆོས་ཐམས་ཅད་འདུས་པ་ཡིན་ཏེ། བཅོམ་ལྡན་འདས་ཀྱི་ཞལ་ནས། བྲམ་ཟེ་ཐམས་ཅད་ཐམས་ཅད་ཅེས་བྱ་བ་ནི་ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད་རྣམས་སོ་ཞེས་གསུངས་སོ། །

[Block 949]
སྐྱེ་བ་མེད་པ་ནི་འོག་ནས་འཆད་པར་འགྱུར་རོ། །

[Block 950]
བཤད་ཅེས་པ་ནི་སངས་རྒྱས་དང་བླ་མས་གསུངས་ཞེས་པའོ། །
--- END BLOCKS ---
