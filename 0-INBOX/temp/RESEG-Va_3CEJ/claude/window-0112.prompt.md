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
[Block 3921]
ས་ཡ་ཕྲག་བཅུ་ལ་ནི་བྱེ་བའོ། །

[Block 3922]
བྱེ་བ་ཕྲག་བཅུ་ལ་ནི་དུང་ཕྱུར་རོ། །

[Block 3923]
དུང་ཕྱུར་ཕྲག་བཅུ་ལ་ནི་ཐེར་འབུམ་མོ། །

[Block 3924]
ཐེར་འབུམ་ཕྲག་བཅུ་ལ་ནི་ཐེར་འབུམ་ཆེན་པོའོ། །

[Block 3925]
ཐེར་འབུམ་ཆེན་པོ་ཕྲག་བཅུ་ལ་ནི་ཁྲག་ཁྲིག་གོ། །

[Block 3926]
ཁྲག་ཁྲིག་ཕྲག་བཅུ་ལ་ནི་ཁྲག་ཁྲིག་ཆེན་པོའོ། །

[Block 3927]
ཁྲག་ཁྲིག་ཆེན་པོ་ཕྲག་བཅུ་ལ་ནི་རབ་བཀྲམ་མོ། །

[Block 3928]
རབ་བཀྲམ་ཕྲག་བཅུ་ལ་ནི་རབ་བཀྲམ་ཆེན་པོའོ། །

[Block 3929]
རབ་བཀྲམ་ཆེན་པོ་ཕྲག་བཅུ་ལ་ནི་གཏམས་སོ། །

[Block 3930]
གཏམས་ཕྲག་བཅུ་ལ་ནི་གཏམས་ཆེན་ནོ། །

[Block 3931]
གཏམས་ཆེན་ཕྲག་བཅུ་ལ་ནི་དཀྲིགས་སོ། །

[Block 3932]
དཀྲིགས་ཕྲག་བཅུ་ལ་ནི་དཀྲིགས་ཆེན་ནོ།[^2232] །དཀྲིགས་ཆེན་ཕྲག་བཅུ་ལ་ནི་མི་འཁྲུགས་པའོ། །

[Block 3933]
མི་འཁྲུགས་པ་ཕྲག་བཅུ་ལ་ནི་མི་འཁྲུགས་པ་ཆེན་པོའོ། །

[Block 3934]
མི་འཁྲུགས་པ་ཆེན་པོ་ཕྲག་བཅུ་ལ་ནི་ཁྱད་ཕྱིན་ནོ། །

[Block 3935]
ཁྱད་ཕྱིན་ཕྲག་བཅུ་ལ་ནི་ཁྱད་ཕྱིན་ཆེན་པོའོ། །

[Block 3936]
ཁྱད་ཕྱིན་ཆེན་པོ་ཕྲག་བཅུ་ལ་ནི་པང་སྟེང་ངོ་། ། པང་སྟེང་ཕྲག་བཅུ་ལ་ནི་པང་སྟེང་ཆེན་པོའོ། །

[Block 3937]
པང་སྟེང་ཆེན་པོ་ཕྲག་བཅུ་ལ་ནི་དེད་འདྲེན་ནོ། །

[Block 3938]
དེད་འདྲེན་ཕྲག་བཅུ་ལ་ནི་དེད་འདྲེན་ཆེན་པོའོ། །

[Block 3939]
དེད་འདྲེན་ཆེན་པོ་ཕྲག་བཅུ་ལ་ནི་མཐའ་སྣང་ངོ་། །མཐའ་སྣང་ཕྲག་བཅུ་ལ་ནི་མཐའ་སྣང་ཆེན་པོའོ། །

[Block 3940]
མཐའ་སྣང་ཆེན་པོ་ཕྲག་བཅུ་ལ་ནི་རྒྱུ་རིག་གོ། །

[Block 3941]
རྒྱུ་རིག༌[^2233]ཕྲག་བཅུ་ལ་ནི་རྒྱུ་རིག་ཆེན་པོའོ། །

[Block 3942]
རྒྱུ་རིག་ཆེན་པོ་ཕྲག་བཅུ་ལ་ནི་འོད་མཛེས་སོ། །

[Block 3943]
འོད་མཛེས་ཕྲག་བཅུ་ལ་ནི་འོད་མཛེས་ཆེན་པོའོ། །

[Block 3944]
འོད་མཛེས་ཆེན་པོ་ཕྲག་བཅུ་ལ་ནི་དབང་པོའོ། །

[Block 3945]
དབང་པོ་ཕྲག་བཅུ་ལ་ནི་དབང་ཆེན་ནོ། །

[Block 3946]
དབང་ཆེན་ཕྲག་བཅུ་ལ་ནི་ལེགས་ཕྱིན་ནོ། །

[Block 3947]
ལེགས་ཕྱིན་ཕྲག་བཅུ་ལ་ནི་ལེགས་ཕྱིན་ཆེན་པོའོ། །

[Block 3948]
ལེགས་ཕྱིན་ཆེན་པོ་ཕྲག་བཅུ་ལ་ནི་རྟོགས་འགྲོའོ། །

[Block 3949]
རྟོགས་འགྲོ་ཕྲག་བཅུ་ལ་ནི་རྟོགས་འགྲོ་ཆེན་པོའོ། །

[Block 3950]
རྟོགས་འགྲོ་ཆེན་པོ་ཕྲག་བཅུ་ལ༌[^2234]འབྱིང་རྡུལ་ལོ། །

[Block 3951]
འབྱིང་རྡུལ་ཕྲག་བཅུ་ལ་ནི་འབྱིང་རྡུལ་ཆེན་པོའོ། །

[Block 3952]
འབྱིང་རྡུལ་ཆེན་པོ་ཕྲག་བཅུ་ལ་ནི་རྒྱ་རྟགས་སོ། །

[Block 3953]
རྒྱ་རྟགས་ཕྲག་བཅུ་ལ་ནི་རྒྱ་རྟགས་ཆེན་པོའོ། །

[Block 3954]
རྒྱ་རྟགས་ཆེན་པོ་ཕྲག་བཅུ་ལ་ནི་སྟོབས་འཁོར་རོ། །

[Block 3955]
སྟོབས་འཁོར་ཕྲག་བཅུ་ལ་ནི་སྟོབས་འཁོར་ཆེན་པོའོ། །

[Block 3956]
སྟོབས་འཁོར་ཆེན་པོ་ཕྲག་བཅུ་ལ་ནི་བརྡ་ཤེས་སོ། །

[Block 3957]
བརྡ་ཤེས་ཕྲག་བཅུ་ལ་ནི་བརྡ་ཤེས་ཆེན་པོའོ། །

[Block 3958]
བརྡ་ཤེས་ཆེན་པོ་ཕྲག་བཅུ་ལ་ནི་རྣམ་འབྱུང་ངོ་། །རྣམ་འབྱུང་ཕྲག་བཅུ་ལ་ནི་རྣམ་འབྱུང་ཆེན་པོའོ། །

[Block 3959]
རྣམ་འབྱུང་ཆེན་པོ་ཕྲག་བཅུ་ལ་ནི་སྟོབས་མིག་གོ། །

[Block 3960]
སྟོབས་མིག་ཕྲག་བཅུ་ལ་ནི་སྟོབས་མིག་ཆེན་པོའོ། །
--- END BLOCKS ---
