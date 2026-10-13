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
[Block 3816]
འོན་ཀྱང་དཀྱིལ་འཁོར་པ་ཐམས་ཅད་ལ་དེ་བཞིན་གཤེགས་པའི་ཚིག་གི་ཁྱད་པར་ནི་ལོངས་སྤྱོད་རྫོགས་པ་དང་སྤྲུལ་པའི་སྐུ་དབྱེར་མེད་པར་བསྟན་པའོ། །

[Block 3817]
གཟུགས་ལ་སོགས་པ་ཡང་རྣམ་པར་དག་པར་ཤེས་པར་བྱའོ། །

[Block 3818]
གང་གི་ཕྱིར་རྡོ་རྗེ་ཕྲེང་བ་ལས།

[Block 3819]
གཟུགས་རྡོ་རྗེ་མ་ལ་སོགས་པ་རྣམས་སྐུའི་དཀྱིལ་འཁོར་ལ་དགོད་པ༌[^2381]མ་བསྟན་ཏོ་ཞེས་པ༌[^2382]ནི་ལོགས་ནས་སྨྲ་བར་བྱའོ་ཞེ་ན། དེ་ནི་མ་ཡིན་ཏེ། དཀྱིལ་འཁོར་པ་རྣམས་ཀྱི་ཁ་དོག་ལྔ་གང་ཡིན་པ་དེ་ནི་གཟུགས་རྡོ་རྗེ་མའོ། །

[Block 3820]
སྔགས་བརྗོད་པའི་སྒྲའམ་རྗེས་སུ་ཆགས་པའི་སྒྲ༌[^2383]རྡོ་རྗེ་མའོ། །

[Block 3821]
ཞལ་གྱི་དྲི་འམ་ཆོས་འབྱུང་བའི་དྲི་ནི་དྲི་རྡོ་རྗེ་མའོ། །

[Block 3822]
བདུད་རྩི་ལ་སོགས་པའི་རོ་མྱང་བ་ནི་རོ་རྡོ་རྗེ་མའོ། །

[Block 3823]
རྣམ་པ་སྣ་ཚོགས་ལ་སོགས་པའི་སྐད་ཅིག་མས་ཐོབ་པར་བྱ་བའི་བདེ་བ་ཆེན་པོ་ཉམས་སུ་མྱོང་བའི་མཚན་ཉིད་ཅན་རང་རིག་པའི་རྣམ་པར་དག་པའི་ངོ་བོ་ཉིད་ནི་རེག་བྱ་རྡོ་རྗེ་མའོ། །

[Block 3824]
རྡོ་རྗེ་སློབ་དཔོན་ཉིད་ཀྱི༌[^2384]ལུས། །ཞེས་བྱ་བ་ལ་སོགས་པས་ཕུང་པོ་ལ་སོགས་པ༌[^2385]རྣམ་པར་དག་པའི་ཚུལ་དུ་བསྟན་པའོ། །

[Block 3825]
རྡོ་རྗེ་ཅན་ནི་རྡོ་རྗེ་སློབ་དཔོན་གྱི༌[^2386]གཟུགས་ཅན་རྡོ་རྗེ་སེམས་དཔའོ། །

[Block 3826]
སྦྱངས་ཞེས་པ་ནི་དོན་དང་ལྡན་པའི་བསྟན་བཅོས་བསྟན་པའོ། །

[Block 3827]
མྱ་ངན་འདས་པ་འཇུག་འགྱུར༌[^2387]ཞིང་། །ཞེས་པ་ནི་རྡོ་རྗེ་འཆང་ཆེན་པོའི་གནས་ཐོབ་པར་བྱེད་པའོ། །

[Block 3828]
ཁྱོད་ཀྱི་རིགས་ནི་ཡོངས་སྨིན་པས། །ཞེས་པ་ནི་བྱ་བ༌[^2388]བྱས་པའི་ཕྱིར་རོ། །

[Block 3829]
བཅོམ་ལྡན་མྱུར་དུ་མྱ་ངན་འདས། །ཞེས་པ་ནི། ཀྱེ་བཅོམ་ལྡན་འདས་ཁྱོད་ཀྱི་སྐུ་རྡོ་རྗེ་སློབ་དཔོན་གྱི་སྐུར་སྣང་བར་འགྱུར་ཏེ། གཞན་ལ་ལྟོས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 3830]
དེ་བས་ཞེས་བྱ་བ་ལ་སོགས་པས་རྡོ་རྗེ་སློབ་དཔོན་གྱི་ལུས་ལ་སྐུའི་དཀྱིལ་འཁོར་ཉེ་བར་བསྡུས་པ་བསྟན་ཏོ། །

[Block 3831]
མཐོང་ན་དོན་ནི་ཡོད་པ་སྐྱེ། །ཞེས་བྱ་བ་ལ་སོགས་པས་མ་འོངས་པའི་དུས་སུ་སེམས་ཅན་ཐམས་ཅད་ཀྱིས་རྡོ་རྗེ་སློབ་དཔོན་ཁོ་ན་ལ་བསྙེན་བཀུར་བྱ་ཞེས་ལུང་བསྟན་པ་ཉིད་དུ་གསུངས་སོ། །

[Block 3832]
དེ་ནས་མཐོང་བ་དོན་ཡོད་བཅས། །ཞེས་པ་ནི་གཤིན་རྗེ་གཤེད་དང་ལྷན་ཅིག་ཏུའོ། །

[Block 3833]
བྱང་ཆུབ་སེམས་དཔའ་ནི་བྱམས་པ་ལ་སོགས་པའོ། །

[Block 3834]
གྲགས་པ་ཆེ་ཞེས་བྱ་བ་ནི་འགྲོ་བའི་དོན་བྱེད་པས་གྲགས་པ་ཐོབ་པའོ། །

[Block 3835]
དགའ་ཞིང་མགུ་ལ་ཞེས་པ་ནི་སྐུའི་དཀྱིལ་འཁོར་ཐོབ་པས་སོ། །

[Block 3836 [VERSE]]
རབ་དང་བ་ནི་དེ་བསམས་པས་སོ། །
ཕྱག་འཚལ་ནས་ནི་མཆི་མ་བླགས། །

[Block 3837]
ཞེས་པ་ནི་དེ་བསྒོམས་པས་སོ། །ཞེས་རྡོ་རྗེ་ཕྲེང་བ་ལས་གསུངས་པ་འདིས་ལུང་ཚད་མ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 3838]
རིགས་པ་འདིས་ཞེས་པ་ནི་སྔར་བཤད་པས་སོ། །

[Block 3839]
བྲི་བའི་དཀྱིལ་འཁོར་དུ་ཡང་ཞེས་པ་ནི་སྒྲུབ་པའི་དཀྱིལ་འཁོར་དུའོ། །

[Block 3840]
ལྷ་སུམ་ཅུ་རྩ་གཉིས་དགོད་པར་བྱའོ་ཞེས་པ་ནི་སྔར་བཤད་པའི་ཞལ་དང་ཕྱག་མཚན་ལ་སོགས་པའི༌[^2389]དབྱེ་བ་དང་ལྡན་པའི་ལྷའི་འཁོར་ལོ་དགོད་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3841]
བསྡུས་པའི་དོན་ནི་གླེང་གཞིའི་ཚིག་གིས་རྒྱུད་ཀྱི་དོན་མ་ལུས་པ་སོ་སོར་བསྟན་ནས་འདོད་ཆགས་ཀྱི་རིགས་ཅན་གདུལ་བར་བྱ་བའི་ཕྱིར། ལྷ་མོ་དགུའི་དབུས་སུ་འདོད་ཆགས་ཆེན་པོའི་ཏིང་ངེ་འཛིན་བསྟན་ཏོ། །

[Block 3842]
དེའི་རྗེས་ལ་སྒྲུབ་པའི་ཐབས་ཀྱི་རིམ་པས་རྡོ་རྗེ་འཆང་ཆེན་པོ་ལ་ཞུགས་པའི་མཚན་ཉིད་ཅན་ཐུགས་རྡོ་རྗེ་འཛིན་པ་དབུས་ཀྱི༌[^2390]གཙོ་བོ་ཉིད་ཡིན་པས་དང་པོའི་སྦྱོར་བ་ཞེས་བྱ་བའི་ཏིང་ངེ་འཛིན་བསྟན་ཏོ། །

[Block 3843]
པདྨའི་ནང་དུ་དམ་ཚིག་གི༌[^2391]དཀྱིལ་འཁོར་སྤྲུལ་པ་དང་རྣམ་པར་སྣང་མཛད་ལ་སོགས་པ་ལྷའི་འཁོར་ལོ་སྤྲོ་བ་དང་དགོད་པའི་རིམ་པས་དཀྱིལ་འཁོར་རྒྱལ་བ་མཆོག་གི་ཏིང་ངེ་འཛིན་བསྟན་ཏོ། །

[Block 3844]
དེའི་ནང་དུ་དབང་བསྐུར་བ་ལ་སོགས་པའི་མཚན་ཉིད་ལས་ཀྱི་རྒྱལ་བ་མཆོག་གི་ཏིང་ངེ་འཛིན་དང་རྫོགས་པའི་རིམ་པ་ཡང་བསྟན་ཏོ། །

[Block 3845]
དེ་གླེང་གཞིའི་ཚིག་གི་དོན་ཡིན་ཏེ། གང་གི་ཕྱིར་གླེང་གཞི་ནི་སྟོན་པ་པོ་དང་ཉན་པ་པོ་དང་། གནས་ཕུན་སུམ་ཚོགས་པ་གཙོ་བོར་གྱུར་པ་ཡིན་ནོ། །

[Block 3846]
དེ་ལ་བཅོམ་ལྡན་འདས་ཞེས་བྱ་བ་འདིས་སྟོན་པ་པོ་ཕུན་སུམ་ཚོགས་པ་གཙོར་གྱུར་པ་སྟེ་དང་པོའི་སྦྱོར་བ་བསྟན་ཏོ། །

[Block 3847]
དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཅེས་བྱ་བ་ལ་སོགས་པ་འདིས་གཞིའི་དཀྱིལ་འཁོར་གྱི་ངོ་བོ་དེ་ཉིད་ཀྱི་ཡན་ལག་སྟེ་གཞལ་ཡས་ཁང་པ་སོ་སོར་བསྟན་པའི་ཕྱིར་རོ། །

[Block 3848]
བཛྲ་དྷྲྀཀ་ཅེས་བྱ་བ་ལ་སོགས་པ་ཕྱུང་བའི་དཀྱིལ་འཁོར་སྤྲོ་བའི་སྒོ་ནས་དཀྱིལ་འཁོར་རྒྱལ་བ་མཆོག་གི་ཏིང་ངེ་འཛིན་བསྟན་ཏོ། །

[Block 3849]
ངེས་པའི་དོན་གྱི་ཕྱོགས་སུ་ཡང་དབང་བསྐུར་བ་ལ་སོགས་པའི་མཚན་ཉིད་ལས་ཀྱི་རྒྱལ་བ་མཆོག་གི་ཏིང་ངེ་འཛིན་དང་། རྫོགས་པའི་རིམ་པ་མཚོན་པའོ།[^2392] །

[Block 3850]
བསྐྱེད་པ་དང་རྫོགས་པའི་རིམ་པ་དག་ལས་མ་གཏོགས་པའི་རྒྱུད་ཀྱི་དོན་གཞན་མེད་དོ། །

[Block 3851]
དེ་ཉིད་བསྟན་པར་བྱ་བའི་ཕྱིར། གླེང་གཞི་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་པ་ལ། གླེང་གཞི་ནི་དང་པོའི་ཚིག་དང་དེའི་ལྷག་མར་གྱུར་པ་ལེའུ་དང་པོའོ། །

[Block 3852]
དབང་དུ་མཛད་ནས་ཀྱང་ཞེས་པ་ནི་དེ་ལ་བརྟེན་པས་སོ། །

[Block 3853]
དོན་གང་ཞེས་པ་ནི་རིམ་པ་གཉིས་ཀྱི་མཚན་ཉིད་དོ། །

[Block 3854]
བསྟན་པ་ཞེས་པ་ནི་སོ་སོར་བསྟན་པའོ། །

[Block 3855]
དེ་ཉིད་དུ་ནི༌[^2393]ཞེས་པ་ནི༌[^2394]གླེང་གཞིའི་ཚིག་ཁོ་ན་ལའོ། །
--- END BLOCKS ---
