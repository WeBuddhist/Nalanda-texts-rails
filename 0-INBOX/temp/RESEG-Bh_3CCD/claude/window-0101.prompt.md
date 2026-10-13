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
[Block 3536]
ཁམས་ཕྲ་བར༌[^2262]འཛིན་པར་མཛད་པས་ན། [^2263]ཞེས་པ་ལ། འོད་གསལ་བ་ལ་འཇུག་པར་བྱེད་དོ། །

[Block 3537]
ངེས་པའི་དོན་ནི་སེམས་རྣམ་པར་དག་པ་བརྗོད་པར་འདོད་པའི་ཕྱིར་རོ། །

[Block 3538]
བྱང་ཕྱོགས་སུ་བཞུགས་སོ་ཞེས་པ་ལ་སོགས་པ་ནི་སྔ་མ་བཞིན་ནོ། །

[Block 3539]
ཞེ་སྡང་ཞེས་བྱ་བ་ལ་སོགས་པས་ཞེ་སྡང་ལ་སོགས་པ་ཉོན་མོངས་པ་རྣམ་པར་དག་པའི་ངོ་བོ་དེ་བཞིན་གཤེགས་པ་ལྔ་ཡིན་ཞེས་ཉེ་བར་སྡུད་པ༌[^2264]བསྟན་ཏོ། །

[Block 3540]
གདུལ་བྱ་རྣམས་ཀྱི་ཐར་པའི་མངོན་པར་འདོད་པ་ཞེས་བྱ་བ་ལ་སོགས་པས་འདོད་པ་དང་ཐར་པ་དག་གི་ལམ་དང་འབྲས་བུའི་བྱེ་བྲག་བསྟན་ཏོ། །

[Block 3541]
དྲང་བའི་དོན་ནི་བསྐྱེད་པའི་རིམ་པའི༌[^2265]བསྟན་པས་སོ། །

[Block 3542]
འདོད་པ་ལ་ཉེ་བར་ལོངས་སྤྱོད་པས་ཐར་པ་རབ་ཏུ་ཐོབ་པའམ་ཞེས་པ་ནི་སྤྲོས་པ་དང་བཅས་པའི་སྤྱོད་པ་ཡིན་པའི་སྒོ་ནས་ཕྱག་རྒྱ་ཆེན་པོའི་དངོས་གྲུབ་སྟེར་བར་བྱེད་པའོ། །

[Block 3543]
ཡང་ན་ཞེས་བྱ་བ་ལ་སོགས་པས་འདོད་པ་དང་ཐར་པ་དག་ནི་ཅིག་ཅར་དུ་སྒྲུབ་པར་བྱེད་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 3544]
སྒྲ་ཇི་བཞིན་པ་ནི་སྤྱོད་པ་བརྗོད་པར་འདོད་པས་སོ། །

[Block 3545]
བཤད་པའི་རྒྱུད་ལས་ཞེས་པ་ལ། དགོངས་པ་ལུང་བསྟན་པའི་བཤད་པའི་རྒྱུད་ལས་སོ། །

[Block 3546]
ཕུང་པོ་འདི༌[^2266]དག་སངས་རྒྱས་ཏེ། །ཞེས་པ་ལ་ཕུང་པོ་ཁོ་ན་སངས་རྒྱས་ཉིད་ཡིན་ཏེ་དམ་བཅའ་བའོ། །

[Block 3547]
རྫོགས་པའི་བྱང་ཆུབ་རྐྱེན་དུ་འབྱུང་། །ཞེས་པ་ནི་ཕྱག་རྒྱ་ཆེན་པོའི་གཟུགས་བསྒྲུབ་པར་བྱ་བའི་ཕྱིར་ཕ་དང་མའི་བདེ་བ་དང་ཡིད་བདེ་བའི་མཚན་ཉིད་བདེ་བ་ཆེན་པོའི་རྒྱུ་མཐུན་པ་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་རྒྱུ་ལས་འབྱུང་བ་ནི་ཡང་དག་པར་སྐྱེས་པའོ། །

[Block 3548]
གཉིས་མེད་དེ་བཞིན་ཉིད་སྦྱོར་བས། །ཞེས་པ་ནི་འོད་གསལ་བ་ལས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 3549]
དེ་ཡང་དེ་བཞིན་གཤེགས་ཞེས་བྱ། །ཞེས་པ་ལ་རང་བཞིན་གྱིས་གྲུབ་པའི་དེ་བཞིན་གཤེགས་པའི་རྐྱེན་ལས་བྱུང་བ་ཁོ་ནའོ། །

[Block 3550]
དེ་བས་ན་ཕུང་པོ་ལྔ་རྣམ་པར་དག་པའི་ངོ་བོ་དེ་བཞིན་གཤེགས་པ་ལྔ་ཡིན་ཞེས་གསུངས་ཏེ་དགོངས་པའོ། །

[Block 3551]
ངེས་པའི་དོན་ནི་འོད་གསལ་བ་ཙམ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 3552]
ལོངས་སྤྱོད་ཀྱི་ཕྱིར་རོ༌[^2267]ཞེས་པ་ནི་མཆོག་ཏུ་དགའ་བའི་བདེ་བ་མྱོང་བའི་ཕྱིར་རོ། །

[Block 3553]
རྡོ་རྗེ་འཛིན་རྗེས་སུ་མཉེས་པར༌[^2268]བྱེད་པའི་དམ་ཚིག་ནི་མཱ་མ་ཀཱིའོ་ཞེས་པ་ལ། ཐུགས་ཀྱི་རྡོ་རྗེ་འཛིན་པའི་ཡིད་དུ་འོང་བའི་ལྷ་མོ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3554]
སྒྲ་ཇི་བཞིན་པ་ནི་ཏིང་ངེ་འཛིན་ཙམ་བསྟན་པས་སོ། །

[Block 3555]
དྲང་བའི་དོན་ནི་ཐུགས་ཀྱི་རྡོ་རྗེའི་བཙུན་མོ་བསྟན་པ་ཙམ་གྱིས་སོ། །

[Block 3556]
ངེས་པའི་དོན་ནི། དེ་རྣམ་པར་དག་པའི་རང་བཞིན་ལྷ་མོ་བསྟན་པས་སོ། །

[Block 3557]
མཱ་མ་ཀཱིའི་གཟུགས་སུ་གྱུར་ནས་ཞེས་པ་ནི་རྡོ་རྗེ་འཆང་ཆེན་པོ་ཉིད་ཀྱིས་མཱ་མ་ཀཱིའི་གཟུགས་སུ་བདག་ཉིད་སྤྲུལ་པ་ཡིན་གྱི་སྐྱེས་པ་དང་བུད་མེད་ཀྱི་དབྱེ་བ་དེ་ལ་གང་ཡང་མེད་དེ། སྤྲོས་པ་མེད་པའི་དེ་ཁོ་ན་ཉིད་ལ་གང་ཡང་བྱེ་བྲག་མེད་པའི་ཕྱིར་རོ། །

[Block 3558]
གདུལ་བྱ་རྣམས་འཇུག་པའི་ཕྱིར་སངས་རྒྱས་ཀྱི་རོལ་སྟོན་སྣ་ཚོགས་ཡིན་ཏེ་སྤྲུལ་པ་བཞིན་ནོ། །

[Block 3559]
ཤར་ཕྱོགས་ཀྱི་གྲར་ཞེས་བྱ་བ་ལ་སོགས་པས་མེའི་མཚམས་སུ་ཉེ་བར་བཞུགས་སོ། །

[Block 3560]
དེ་བཞིན་ཐམས་ཅད་དུ་ཤེས་པར་བྱའོ། །

[Block 3561]
རྣམ་པར་སྣང་མཛད་ནི་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་གོང་དུ་བྱུང་བའི་ཕྱིར་རོ། །

[Block 3562]
སྒྲ་ཇི་བཞིན་པས་ནི་སངས་རྒྱས་སྤྱན་གྱི་གཟུགས་ཙམ་བསྟན་པས་སོ། །

[Block 3563]
དྲང་བའི་དོན་ནི་རྣམ་པར་སྣང་མཛད་ལ་རྗེས་སུ་ཆགས་པའི་ལྷ་མོ་བསྟན་པས་སོ། །

[Block 3564]
ངེས་པའི་དོན་ནི་དེ་རྣམ་པར་དག་པ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 3565]
འདོད་ཆགས་འཛིན་པ་ནི་འོད་དཔག་ཏུ་མེད་པ་ཞེས་པ་ནི་འདོད་ཆགས་རྣམ་པར་དག་པའི་རང་བཞིན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3566]
གོས་དཀར་མོ་སྟེ་ཞེས་པ་ལ། གསུངས༌[^2269]རྡོ་རྗེའི་བཙུན་མོའོ། །

[Block 3567]
དྲང་བའི་དོན་ནི་གོས་དཀར་མོའི་གཟུགས་བསྟན་པས་སོ། །

[Block 3568]
ངེས་པའི་དོན་ནི་རྣམ་པར་དག་པ་བསྟན་པས་སོ། །

[Block 3569]
སྒྲ་ཇི་བཞིན་པ་ནི་ཞེས་པ་ནི་སྔ་མ་བཞིན་ནོ། །

[Block 3570]
མི་རྟག་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་ཉེ་བར་མཚོན་པ་སྟེ། ཆོས་སྒྲ་སྒྲོགས་པ་རྣམ་པ་བཞི་སྟེ། འདུས་བྱས་ཐམས་ཅད་མི་རྟག་པ་ཞེས་པ་དང་། ཟག་པ་དང་བཅས་པ་ཐམས་ཅད་སྡུག་བསྔལ་བའོ་ཞེས་པ་དང་། ཆོས་ཐམས་ཅད་བདག་མེད་པ་དང་། མྱ་ངན་ལས་འདས་པ་ཞི་བ་ཡིན་ནོ་ཞེས་སོ། །

[Block 3571]
གཞན་དག་ལ་རབ་ཏུ་སྟོན་པ་ན་གདུལ་བྱ་རྣམས་ལ་བསྟན་པའོ། །

[Block 3572]
ཡི་གེའི་དོན་ནི་ཆོས་བསྟན་པ་ཙམ་ཡིན་པས་སོ། །

[Block 3573]
ཆོས་ཐམས་ཅད་སྟོང་པའོ་ཞེས་པ་ནི་རྣམ་པར་ཐར་པའི་སྒོ་ནས་ཞེས་ཚིག་གི་ལྷག་མའོ། །

[Block 3574]
སྤྱིའི་དོན་ནི། མདོ་སྡེ་པ་ལ་སོགས་པའི་འགྱོད་པ་བཟློག་པས་སོ། །

[Block 3575]
སྣང་བ་གསུམ་གྱི་ངོ་བོ་ཉིད་ཅེས་པ་ནི་སྣང་བ་ལ་སོགས་པའི་རང་བཞིན་ནོ། །
--- END BLOCKS ---
