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
བདག་གིས་ཞེས་པ་ལ་སོགས་པ་ནི་འཆང་བར་འགྱུར་བའོ། །

[Block 947]
རྡོ་རྗེའི་ཚིག་ནི་རྡོ་རྗེ་འཆང་ཆེན་པོའི་ཚིག་ཡིན་པ་དང་། རྟོགས་པར་དཀའ་བ་ཉིད་ཀྱི་ཕྱིར་དེ་སྐད་ཅེས་བྱའོ། །

[Block 948]
བཤད་པའི་རྒྱུད་ལས་བསྟན་པ་ཉིད་ལ་འཇུག་པ་ནི་རྩ་བའི་རྒྱུད་ལས་གསལ་བར་མ་གསུངས་པའི་ཕྱིར་རོ། །

[Block 949]
འཁོར་ལོ་སྤྲུལ་པའི་ངོ་བོ་ལ། །ཞེས་པ་ནི་ལྷའི་འཁོར་ལོ་གཙོ་བོ་དང་འཁོར་གྱི་དཀྱིལ་འཁོར་ལྟ་བུའོ། །

[Block 950]
བདག་གིས་ཐོས་པ་ཞེས་གསུངས་ཏེ། ཞེས་པ་ནི་གང་གིས་དྲང་བའི་དོན་དུ་ཡིན་གྱི་ངེས་པའི་དོན་དུ་མ་ཡིན་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 951]
ས་བོན་ལས་ནི་གང་སྤྲུལ་པ། །ཞེས་པ་ནི་གང་གིས་ས་བོན་གྱིས་བསྐྱེད་པ་ཉིད་ཀྱི་ཕྱིར་དེ་སྐད་ཅེས་བྱའོ། །

[Block 952]
ལྷ་རྣམས་ཀྱི༌[^465]ནི་འཁོར་ལོ་མཆོག །ཅེས་པ་ནི་འདི་དག་གིས་ཡོན་ཏན་ཕུན་སུམ་ཚོགས་པ་དང་། འདིས་འདོད་ཆགས་ཅན་ལ་སོགས་པའི་སེམས་ཅན་ཡོངས་སུ་འདུལ་བའི་ཕྱིར་རོ། །

[Block 953]
མཆོག་ཏུ་དགའ་བ༌[^466]ནི་སྙོམས་པར་ཞུགས་པའི་བདེ་བ་གང་ལ་ཡོད་པ་དེའི་དུས་ལ་དུས་གཅིག་ཅེས་བཤད་པའི་ཕྱིར་རོ། །

[Block 954]
དབང་ཕྱུག་བརྒྱད་ཀྱིས་བཅོམ་ལྡན་འདས། །ཞེས་པ་ནི་དབང་ཕྱུག་ཆེ་དང་གཟུགས་བཟང་བ་དང་གྲགས་པ་དང་དཔལ་ལ་སོགས་པའི་ཡོན་ཏན་གང་ལ་ཡོད་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 955]
ཁྱད་པར་ཇི་ལྟ་བུ་ཞིག་དང་ལྡན་པའི་བཅོམ་ལྡན་འདས་ཡིན་ཞེ་ན། བདེ་བ་ཆེན་པོའི་བདག་ཉིད་ཅན། །ཞེས་པ་ནི་གང་ཞིག་བདེ་བ་ཆེན་པོའི་ངོ་བོ་ཉིད་དུ་གྱུར་པ་གང་ཡིན་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 956]
དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཅེས་བྱ་བ༌[^467]ཇི་ལྟ་བུ་ཡིན་ཞེ་ན།

[Block 957 [VERSE]]
འདི་ཡི་ཕུང་པོ་ལྔ་རྒྱལ་བ། །
དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཡིན། །

[Block 958]
ཞེས་པ་ཕུང་པོ་ལྔ་ཉིད་སངས་རྒྱས་ཏེ། །

[Block 959 [VERSE]]
མདོར་ན་ཕུང་པོ་ལྔ་རྣམས་ནི། །
སངས་ལྔར་ནི་རབ་ཏུ་གྲགས། །

[Block 960]
ཞེས་བྱ་བ་ལ་སོགས་པ་རྒྱས་པར་གཞུང་འདི་ཉིད་ལས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 961]
སྐུ་དང་གསུང་དང་ཐུགས་ཞེས་བྱ་བ་ཡང་ཇི་ལྟ་བུ་ཡིན་ཞེ་ན། དེའི་བདག་ཉིད་དེ། གང་ཞིག་གང་དུ་ཐ་དད་དུ་དབྱེར་མེད་པ་དེའི་ཕྱིར་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 962]
རྡོ་རྗེ་ཞེས་བྱ་བ་ཡང་གང་ཞིག་ཡིན་ཞེ་ན་ཐུགས་ཏེ༌[^468]འདིར་བདེ་བ་ཆེན་པོ་ཞེས་བྱ་བ་བདེ་བ་ཆེན་པོ་རབ་ཏུ་མི་རྟོག་པའི་བདག་ཉིད་ཅན་གང་ཡིན་པ་སྟེ། གང་ཞིག་གང་གིས་གང་དུ་ཡོངས་སུ་མཁྱེན་པར་འགྱུར་བ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 963]
བཙུན་མོ་ཞེས་བྱ་བ་ཡང་གང་ཡིན་ཞེ་ན་ལེགས་སྦྱངས་ཕྱག་རྒྱ་སྟེ་ཞེས་བྱ་བ་སྨོས་ཏེ། རང་བཞིན་གྱིས་ལེགས་པར་སྦྱངས་པ་ནི་རྟགས་མཆོག་དང་ལྡན་པའོ། །

[Block 964]
རྙེད་པས་ལེགས་པར་སྦྱངས་པ་ནི་ནན་གྱིས་ལེན་པ་ལ་སོགས་པ་དང་བྲལ་བའོ། །

[Block 965]
བསམ་པས་ལེགས་པར་སྦྱངས་པ་ནི་ཆགས་པ་དང་བྲལ་བ་དང་རྣམ་པར་འཚེ་བ་དང་བྲལ་བ་ཞེས་བྱ་བ་ལ་སོགས་པའི་བར་དུའོ། །

[Block 966]
ཐབས་ཀྱིས་ལེགས་པར་སྦྱངས་པ་ནི་གང་གིས་གསང་བ༌[^469]བདག་ཉིད་ལེགས་པར་རྙེད་པའོ། །

[Block 967]
སྔགས་དང་རྒྱུད་ཀྱིས་ལེགས་པར་སྦྱངས་པ་ནི་གང་གི་བདག་ཉིད་དེ་ལས་གཞན་དུ་ཉེ་བར་བྱས་པའོ། །

[Block 968]
ཀུན་དུ་ཚོགས་པས་ལེགས་པར་སྦྱངས་པ་ནི་དད་པ་ལ་སོགས་པ་དང་ལྡན་པའོ། །

[Block 969]
ལེགས་པར་སྦྱངས་པ་ཞེས་བྱ་བ་ཡང་གང་ཞིག་ཡིན་ཞེ་ན། ལེགས་པར་སྦྱངས་པ་ནི་འདིར་སྐྱོན་མེད་པ་ཉིད་དེ། གང་གིས་གང་དུ་ཉེ་བར་གནས་པ་དེའི་ཕྱིར་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 970]
བྷ་ག་ཞེས་བྱ་བ་ཡང་གང་ཡིན་ཞེ་ན། ལེགས་སྦྱངས་པདྨ་བྷ་ག་ཡིན། །ཞེས་པ་བཙུན་མོ་དམ་པར་གྱུར་པ་གང་ཡིན་པ་དེའི་པདྨ་སྟེ་ཡོངས་སུ་དག་པར་གྱུར་པ་དང་གང་དུ་ཀུན་དུ་གནས་པར་འགྱུར་བ་དང་། ཉེ་བར་འཇོམས་པར་འགྱུར་བ་གང་ཡིན་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 971]
བཞུགས་སོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གི་དོན་ཇི་ལྟར་གཞག༌[^470]ཅེ་ན།

[Block 972 [VERSE]]
བཞུགས་པ་རྡོ་རྗེ་འཛིན་པ་དེར། །
ཐིག་ལེའི་གཟུགས་ཀྱིས་གནས་པའོ། །

[Block 973]
ཞེས་གསུངས་ཏེ་རྡོ་རྗེ་འཛིན་པ་ཡང་ཐིག་ལེའི་གཟུགས་ཉིད་དོ། །

[Block 974]
འདི་སྐད་དུ་སྟོན་ཏེ། གང་གིས་ཐབས་དང་ཤེས་རབ་གཉིས་སུ་མེད་པར་སྙོམས་པར་ཞུགས་ཏེ། བྱང་ཆུབ་ཀྱི་སེམས་བཙུན་མོའི་བྷ་ག་ལ་གནས་པའོ། །

[Block 975]
ཡང་ན་གང་གིས་གང་ཞིག་གང་དང་གང་དུ་འགྲུབ་པའི་ཕྱིར་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 976]
འདི་དག་གིས༌[^471]ཉེ་བར་བཤད་པ་འདིར་བཤད་པ་ནི་སྤྱིའི་དོན་གྱི༌[^472]སྐབས་འདིར་ཞེས་བྱའོ། །

[Block 977]
ཆ་གཉིས་པ་ནི་དགུ་པ་ཉིད་ཀྱིས་བཤད། །ཅེས་བྱ་བ་ལ་སོགས་པ་ལ། ཆ་གཉིས་པ་ནི། ཨ་དང་ཨུའོ། །

[Block 978]
དགུ་པ་ནི་ཨོའོ། །

[Block 979]
འདི་དག་ལ་གང་གིས་ཡི་གེ་དང་ལྡན་པ་ནི་ཨོཾ་ཞེས་བྱ་བར་འགྱུར་རོ། །

[Block 980]
སུམ་ཅུ་པ་ནི་དའོ། །

[Block 981]
བཅུ་པ་ནི་ཧ་སྟེ་གང་གིས་གང་གི་དོན་དུ་གནས་པ་ཉིད་དོ། །

[Block 982]
ཡང་ན་སུམ་ཅུ་པ་ནི་ཀྵ་སྟེ། ཆ་གཉིས་པོ་ནི༌[^473]ཀྵའོ། །

[Block 983]
དགུ་པ་ནི་དེ་ཉིད་དོ། །

[Block 984]
བཅུ་པ་ནི་ལའོ། །

[Block 985]
ལྔ་པ་ནི་ཧའོ། །
--- END BLOCKS ---
