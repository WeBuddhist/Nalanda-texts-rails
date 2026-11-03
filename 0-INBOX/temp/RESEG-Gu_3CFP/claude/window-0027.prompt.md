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
[Block 946]
ཇི་སྐད་དུ༌[^713]སྨྲས་པ་ཞེས་བྱ་བ་ནི་གསོལ་བ༌[^714]འདེབས་པ་ལ་ཁས་བླངས་པའོ། །

[Block 947]
ཇི་ལྟར་དམ་བཅས་པའི་ཞེས་བྱ་བ་ནི་རེ་ཞིག་བདག་ཉིད་ཀྱིས་སྦྱིན་ནོ་ཞེས་དམ་བཅས་པའོ། །

[Block 948]
བསྐྱུངས་ཏེ་ཞེས་བྱ་བ་ནི་གྲངས་ཀྱི་སྒོ་ནས་སམ་ཚད་ལས་སོ། །

[Block 949]
བཟང་པོ་ནི་ཁྱད་པར་དུ་འཕགས་པ་སྟེ། རྣམ་པ་གཉིས་ཀྱིས་གྱ་ནོམ་པ་ཡིན་ཏེ། རིགས་ཀྱིས་སམ། རིན༌[^715]ཐང་གིས་སོ། །

[Block 950]
དེའི་མི་མཐུན་པའི་ཕྱོགས་ནི་ངན་པ་ཐ་ཆད་དོ། །

[Block 951]
ཡིད་མི་དགའ་ལ་ཞེས་བྱ་བ་ནི་སེམས་རྣམ་པར་གཡེངས་པའོ། །

[Block 952]
ཁྲོས་པ་ནི་ཁྲོས་པས༌[^716]ཟིལ་གྱིས་ནོན་པའོ། །

[Block 953]
ཡིད་འཁྲུགས་པས་རྗེས་སུ་བཟུང་བ༌[^717]ཞེས་བྱ་བ་ནི་ཡིད་དྲི་མ་ཅན་གྱིས་སོ། །

[Block 954]
ཕན་བཏགས༌[^718]སོ་ཞེས་བྱ་བ་ནི་བདེ་བ་ཉེ་བར་བསྒྲུབ༌[^719]པའོ། །

[Block 955]
སྐྱེད་དོ་ཞེས་བྱ་བ་ནི་འཕེལ་བ་ཐོབ་པར་བྱས་པའོ། །

[Block 956]
དྲངས་སོ་ཞེས་བྱ་བ་ནི་རྒུད་པའམ། གཞན་པའི་སྡུག་བསྔལ་ལས་སོ། །

[Block 957]
སྨྲས་པ༌[^720]ནི་འགྱུར་བ་དང་བཅས་པ་སྨོད༌[^721]པའོ། །

[Block 958]
སྒྲུབ་པ་དམན་པ་ནི་ལོག་པར་སྒྲུབ་པའོ། །

[Block 959]
དེ་ལ་གནས་པ་ནི་ལོག་པར་སྒྲུབ་པ་ལ་གནས་པ་སྟེ། དེ་ལྟ་བུའི་ལོག་པར་སྒྲུབ་པ་རྣམ་པ་སྣ་ཚོགས་ལ་གནས་པ་དེ་དག་ལ་སྦྱིན་པའོ། །

[Block 960]
རྒོད་པ་ཞེས་བྱ་བ་ནི་དབུགས་མ་ཕྱིན་པའོ། །

[Block 961]
བདག་ཉིད་མ་བསྡམས་པ་ཞེས་བྱ་བ་ནི་སྡོམ་པ་མ་ཡིན་པ་ལ་གནས་པའོ། །

[Block 962]
མ་བརྗོད་པ་ཞེས་བྱ་བ་ནི་སྦྱིན་པ་པོས་སོ། །

[Block 963]
འཇིག་རྟེན་པ་དང་འཇིག་རྟེན་ལས་འདས་པའི་འདོད་ཆགས་དང་བྲལ་བའི་རྣམ་པར་དག་པ༌[^722]ཞེས་བྱ་བ་ལ། འཇིག་རྟེན་པ༌[^723]ནི་འདོད་ཆགས་དང་བྲལ་བའོ། །

[Block 964]
འཇིག་རྟེན་ལས་འདས་པ༌[^724]ནི་རྣམ་པར་དག་པ་སྟེ། ཁམས་གཉིས་སམ། ཁམས་གསུམ་ལས་སོ། །

[Block 965]
རྣམ་པར་དག༌[^725]པ་ཞེས་བྱ་བ་ནི་རྣམ་པ་གཉིས་ལས་ཏེ། མ་དག་པ་ལས་སོ། །

[Block 966]
ལྷག་པར་གྱུར་པ་ནི་གཏང་བར་འོས་པའི་ཆོས་སུ་བྱས་པའོ། །

[Block 967]
གྲགས་པ་དང་སྒྲ་དང་ཚིགས་སུ་བཅད་པ་ལ་བརྟེན་པ་སྟེ། མངོན་སུམ༌[^726]དུ་བསྟོད་པ་ནི་གྲགས་པའོ། །

[Block 968]
སྒྲ་དང་ཚིགས་སུ་བཅད་པ་ནི་ལྐོག་ནས་བསྔགས་པ་བརྗོད་པ༌[^727]སྟེ། འཁོར་ལོས་སྒྱུར་བ་ཉིད་ལ་བརྟེན་པའམ། དབང་ཕྱུག་ལ་བརྟེན་པའོ། །

[Block 969]
བདུད་ཅེས་སྨོས་པ་ནི་འདོད་པའི་ཁམས་ཀྱི་དབང་ཕྱུག་ཉིད་དོ། །

[Block 970]
ས་ལ་བརྟེན་པའི་ཡུལ་གྱི་དབང་ཕྱུག་ཉིད་ཡིན་པས་བརྒྱ་བྱིན་ཞེས་སྨོས་སོ། །

[Block 971]
གླིང་བཞི༌[^728]དབང་ཕྱུག་ཡིན་པའི་ཕྱིར་འཁོར་ལོས་སྒྱུར་བ༌[^729]ཞེས་སྨོས་སོ། །

[Block 972]
དབང་ཕྱུག་ནི་དེ་དག་མ་ཡིན་པའི་ས་ཕུན་སུམ་ཚོགས་པའི་བདག་པོའོ། །

[Block 973]
ཉུང་ངུ་ལས་ཀྱང་སྦབས་ཆེར་སྦྱིན་པར་བྱེད་ཅེས་བྱ་བ་ནི་མྱུར་བར་སྦྱིན་པར་བྱེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 974]
ལོངས་སྤྱོད་མང་པོ་རྒྱ་ཆེ་ཞིང་རྒྱས་པ་ཞེས་བྱ་བ་ནི་རྣམ་པ་མང་པོ་དང་། ཤིན་ཏུ་ཡང་བའམ། ཡུལ་མང་པོ་ན་གནས་པའོ། །

[Block 975]
ཚིམ་པར་བྱ་བ་ནི་ནང་ཡོངས་སུ་གང་བར་བྱེད་པའོ། །

[Block 976]
འདོད་པ་བཞིན་དུ་ཡོངས་སུ་བཀང་བ༌[^730]ནི་ཡིད་ལ་བསམ་པ་ཡོངས་སུ་རྫོགས་པར་རོ། །

[Block 977]
རྣམ་གྲངས་ཞེས་བྱ་བ་ནི་སྦྱིན་པ་དང་། དོན་རྣམ་པར་གཏོང་བ་དང་། ཡོངས་སུ་གཏོང་བ་དང་། དོན་འགྲུབ་པར༌[^731]བྱེད་པ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 978]
མཚན་ཉིད་ཅེས་བྱ་བ་ནི་སྦྱིན་པའི་ངོ་བོ་ཉིད་ནི་སྦྱིན་པའི་ངོ༌[^732]བོ་ཇི་ལྟ་བ་བཞིན་དུ་བསྟན་པའོ། །

[Block 979]
ངེས་པའི་ཚིག་ཀྱང་ཕོངས་པ༌[^733]སེལ་བར་བྱེད་པས་ནི་སྦྱིན་པའོ། །

[Block 980]
རབ་ཏུ་དབྱེ་བ་ནི། བཟང་བ་བྱིན་པས༌[^734]སྟོབས་དང་ལྡན་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། ཆོས་ཀྱི་སྦྱིན་པ་དང་། ཟང་ཟིང་གི་སྦྱིན་པ་སྟེ། ཟང་ཟིང་གི་སྦྱིན་པ་ནི་ནང་གི་བདག་ཉིད་སྦྱིན་པ་དང་། ཕྱི་རོལ་གྱི་དངོས་པོ་སྦྱིན་པ་སྟེ། ནང་གི་བདག་ཉིད་སྦྱིན་པ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 981]
ཐམས་ཅད་སྦྱིན་པ་འདིའི་བསྡུས་པའི་དོན་དང་གོ་རིམ་བཤད་པར་བྱ་སྟེ། དེ་ལ་ཐམས་ཅད་སྦྱིན་པ་གང་ཞེ་ན་ཞེས་བྱ་བ་ལས་བརྩམས་ནས་ཇི་ལྟར་ངན་སོང་ཐམས་ཅད་ལས་ཤིན་ཏུ་འདས་པ་ཐོབ་པ་ཞེས་བྱ་བའི་བར་དུའོ། །

[Block 982]
དེ་ལ་ཟང་ཟིང་གི་སྦྱིན་པ་ནི་མདོར་བསྡུ་ན༌[^735]རྣམ་པ་གསུམ་སྟེ། ཡོད་ཅིང་བདོག་བཞིན་དུ༌[^736]ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། ཡོད་ཅིང་བདོག་བཞིན་དུ་ཞེས་བྱ་བ་དང་། འདི་དང་གཞན་རྒྱས་པར་དབྱེ་བར་བྱ༌[^737]བ་ནས་བརྩམས་ནས་ཡང་དག་པར་སྦྱིན་པའི་ཆོས་དག་ཡོད་བཞིན་དུ་ཞེས་བྱ་བ་དང་། ཤེས་རབ་ཅན་གྱི་སྦྱིན་པ་ཡིན་པར་རིག་པར་བྱ་ཞེས་བྱ༌[^738]བའི་བར་དུའོ། །

[Block 983]
མེད་ཅིང་མི་བདོག་ཅེས་བྱ་བ་ནི་སྦྱིན་པར་བྱ་བའི་ཆོས་མེད་ཅིང་མི་བདོག་ནའོ། །

[Block 984]
བསམ་པ་དག་པ་ཞེས་བྱ་བ་ནས་བརྩམས་ནས་ཚེ་རབས་ཐམས་ཅད་དུ་ལོངས་སྤྱོད་ཟད་མི་ཤེས་པ་ཐོབ་ཅེས་བྱ་བ་དང་། དེ་བཞིན་དུ་དེས་ཆོས་ཀྱི་སྦྱིན་པ་ཉེ་བར་སྦྱིན་པར་བྱེད་པ་ན་མུ་སྟེགས་ཅན་གླགས་ཚོལ་བ་ལ་མི་སྦྱིན་ཞེས་བྱ་བ་ནས་བརྩམས་ནས་ཆོས་ཀྱི་སྦྱིན་པ་ལས་བརྩམས་ནས་ཤེས་རབ་དང་ལྡན་པའི་སྦྱིན་པར་རིག་པར་བྱའོ་ཞེས་བྱ་བའི་བར་དང་། སོ་སོ་ཡང་དག་པར༌[^739]རིག་པ་ལ་བརྟེན་པ་དང་། ཐམས་ཅད་སྦྱིན་པའི་ཆོས་དང་། ཟང་ཟིང་དང་མི་འཇིགས་པ་ལས་བརྩམས་ནས་རབ་ཏུ་དབྱེ་བ་ཡང་ཅི་ལྟ་བ་བཞིན་དུ༌[^740]རབ་ཏུ་ཤེས་སོ་ཞེས་བྱ་བའི་བར་དུ་སྟེ། ལྷག་པའི་བསམ་པ་ལ་བརྟེན་པ་ཞེས་བྱ་བ་ནི་གནོད་པ་བྱེད་པའི་སེམས་ཅན་ལ་ཞེས་བྱ་བ་ནས་བརྩམས༌[^741]ནས་གྲོགས་བཤེས་རྣམས་ཀྱི་བར་ལ་བཏང་སྙོམས་ཀྱི་བསམ་པ་བྱེད་པའོ། །

[Block 985]
སྦྱིན་པ་ལ་ཉེ་བར་བརྟེན་པ་ནི་སྦྱིན་པའི་གེགས༌[^742]ཡོད་ན་ཡང་ངོ་། །སྦྱིན་པ་ལ་གེགས༌[^743]བྱེད་པའི་གཉེན་པོ་ལས་ཀྱང་བརྩམས་ནས་གཉེན་པོའི་ཤེས་པ་ཐ་མ་འདིས་ནི་བསོད་ནམས་ཀྱི་འབྲས་བུ་ཡང་དག་པར༌[^744]ཡོངས་སུ་འཛིན་པར་བྱེད་དོ་ཞེས་བྱ་བའི་བར་དུའོ། །
--- END BLOCKS ---
