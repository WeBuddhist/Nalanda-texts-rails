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
དེ་ལ་ཟན་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བ་ནི་སྦྲུམ་མ་ལ་དགེ་སློང་མ་རྣམས་ཀྱིས་སོ། །

[Block 3922]
ཕ་མ་དག་ནས་བདུན་པ་ཚུན་ཆད་ལས་གང་ཡང་རུང་བ་སྔ་མ་གཅིག༌[^2687]ལས་སྐྱེས་པ་ཡང་ཉེ་དུ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་ཕ་མ་དག་ཅེས་བྱ་བ་ནི་ཕ་དང༌[^2688]མ་ནི་ཕ་མ་དག་གོ། །

[Block 3923]
འདིར་མའི་རྒྱུད་ཕའི་ཡན་ལག་དང་བཅས་པ་ལ་མའི་སྒྲའོ། །

[Block 3924]
ཕའི་སྒྲ་ཡང་མའི་ཡན་ལག་དང་བཅས་པ་ཕའི་རྒྱུད་ལ་ཕྲུགས་བདུན་དུ་གྱུར་པའི་ཕ་མ་དག་གིས་ཇི་སྲིད་དུ་གང་ཡང་རུང་བ་གཅིག༌[^2689]གིས་ཀྱང་ཕ་མ་དེ་དག་ལ་གཉིས་ཀ་དག་ཉིད་ཀྱིས་ནི་མ་ཡིན་ཏེ། གཅིག་སྔ་མ་ལས་སྐྱེས་པ་ཉིད་དང་མ་གཅིག་ལས་སྐྱེས་པ་ཉིད་དང་ཕ་གཅིག་ལས་སྐྱེས་པ་ཉིད་གང་ལ་ཡོད་པ་དེ་ནི་གཉེན་ཞེས་བྱ་བ་འདི་དག་གི་དོན་ཏོ། །

[Block 3925]
འཁྲུར་འཇུག་པའི་སྤང་བའི་བྱེད་པ་པོ་ཉིད་གང་ཡིན་ཞེ་ན། དེའི་ཕྱིར་འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་པོ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དོན་མེད་ན་ཡང་འདུ་ཤེས་ནི་གཙོ་ཆེར་བྱེད་པ་པོ་ཉིད་ཡིན་ཏེ་འདུ་ཤེས་ནི་གཙོ་ཆེར་རིག་པར་བྱའོ། །

[Block 3926]
གང་དུ་འདིའི་འོག་ཏུ་ཉེ་བར་གནས་པ་ཉིད་རྟོགས་པར་བྱའོ། །

[Block 3927]
དེ་ནི་འདུ་ཤེས་གཙོ་བོར་བྱ་བ་ལ། དེ་ནི་ཞེས་བྱ་བ་ནི་མིང་ཅན་ཏེ་འདུ་ཤེས་གཙོ་བོར་བྱེད་པ་པོ་ཉིད་ཡིན་ནོ། །

[Block 3928]
ཤེས༌[^2690]གཙོ་བོར་བྱ་བ་ནི་མིང་སྟེ་འདུ་ཤེས་གཙོ་བོར་བྱེད་པ་པོ་ཉིད་ཡིན་པ་དེའི་མིང་ངོ་། །དེ་ལྟར་ན་ཚིག་གི་དོན་འདི་འབྱུང་སྟེ་འདི་མན་ཆད་ཀྱི་མདོ་གང་དང་གང་ལ་ཤེས་གཙོ་བོ་ཞེས་བྱ་བའི་མིང་སྨོས་པ་དེ་དང་དེར་མིང་དེའི་རང་གི་མིང་ཅན་འདུ་ཤེས་གཙོ་བོར་བྱེད་པ་པོ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་སྟོན་པར་ཤེས་པར་བྱའོ། །

[Block 3929]
དོན་གང་ལ་འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་པོ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་དགེ་སློང་མ་ཉིད་དང་དེ་ཉེ་དུ་མ་ཡིན་པ་ཉིད་དག་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་སློང་མ་ཉིད་དང་དགེ་སློང་མ་དེ་ཉེ་དུ་མ་ཡིན་པ་དག་ལ་འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3930]
འོག་མ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་འདིའི་རྗེས་ལ་བསླབ་པའི་གཞིའི་ཕྱིར་གཟུང་བ༌[^2691]དང་འབྲེལ་པ་དེ་ལ་ཡང་དགེ་སློང་མ་ཉིད་དང་དེ་ཉེ་དུ་མ་ཡིན་པ་དག་ལ་འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་པོ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་འདྲ་བར་བསྟན་པའོ། །ཅི་ཞིག་བྱས་ན་འཁྲུར་འཇུག་པའི་སྤང་བར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་བྱིན་གྱིས་བརླབས་པ་རང་གི་རྙིང་པ་འཁྲུར་འཇུག་པར་འོས་པ་ཆོས་གོས་དང་གདིང་བ་དག་ལས་འགའ་ཞིག་བསྒོ་བས་འཁྲུར་འཇུག་གམ་འཚེད་དུ་འཇུག་གམ་འཆག་ཏུ་འཇུག་པ་དག་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ་བྱིན་གྱིས་བརླབས་པ་རང་གི་རྙིང་ལ༌[^2692]འཁྲུར་འཇུག་པར་འོས་པ་ཆོས་གོས་དང་གདིང་བ་དག་ལས་འགའ་ཞིག་བསྒོ་བས་འཁྲུར་འཇུག་པ་ལ་སོགས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3931]
འདིར་རྙིང་པ༌[^2693]ཉིད་ནི་ལོངས་སྤྱད་པ་ཉིད་དོ། །

[Block 3932]
ཇི་སྲིད་དུ་ཡང་དུས་ཙམ་ལ་སོགས་པའི་ཚད་དེ་སྲིད་དུ་འདི་ནི༌[^2694]ཡོངས་སུ་རྫོགས་པའི་གཟུགས་ཀྱི་འདུ་བྱེད་མ་ཡིན་ཏེ། གང་ཞིག་མ་འོངས་པ་ན༌[^2695]འདུ་བྱེད་ཅེས་བྱ་བ་འཁྲུར་འཇུག་པར་འོས་པ་ཉིད་ལ་འདིར་ཡན་ལག་ཉིད་དེ། དེ་ལྟ་བུར་གྱུར་པའི་འཁྲུར་འཇུག་པ་ལ་སོགས་པའི༌[^2696]ཕྱོགས་ཉིད་དོ། །

[Block 3933]
འཁྲུར་འཇུག་པར་འོས་པ་མ་ཡིན་པ་རྙིང་པ་འདི་འཁྲུ་བ་ལ་སོགས་པ་ཉེས་བྱས་སུ་རིག་པར་བྱའོ། །

[Block 3934]
གདིང་བའི་ཚིག་ནི་ལུས་ཐམས་ཅད་ལ་ཡང་དག་པར་རེག་པས་ལོངས་སྤྱོད་པ་ཉིད་གང་ཡིན་པ་དེ་ནི་འདིར་ཤེས་པར་བྱ་ཞེས་པ་འདི་སྟན་ཙམ༌[^2697]དུ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 3935]
ལུས་ཀྱི་བསྙེན་བཀུར་བྱེད་པའི་རྣམ་པ་ཉིད་ནི་འདིར་ཉེས་པ་མཐོང་བ་ཡིན་ཏེ། དེ་བས་ན༌[^2698]གཞན་གྱིས་ཡོངས་སུ་ལོངས་སྤྱོད་པ་ཉིད་ལ་ན་སྨད་པ་ཞེས་བྱ་བ་རྟོགས་པར་བྱའོ། །

[Block 3936]
ངག་ཀྱང་ཞེས་བྱ་བའི་ཆོ་ག་འདི་ལ་འཇུག་པའི་དོན་དུ་བསྒོ་བ་ཞེས་བྱ་བའི་ཚིག་གོ། །

[Block 3937]
འདིར་གཞུང་ནི་བཙུན་པ་དགེ་སློང་ཆོས་གོས་རུང་བས་གྲོང་དུ་ཞུགས་ཤིང་དེའི་ཆོས་གོས་དེ་ཡང་ལུས་ལས་མ་ཕུད་པར་དེངས་པར་བགྱི་བའི་སླད་དུ་འབྱུང་བར་འགྱུར་བ་མཆིས་སམ། ཉེ་བ་འཁོར་ཡོད་དེ། འདི་ལྟ་སྟེ་ཁྱིམ་གྱི་ནང་དུ་ཞུགས་པའི་ཆོས་གོས་མི་གཙང་བ་ལ་སོགས་པས་གོས་པར་གྱུར་པ་དེ་དགེ་སློང་མ་ཉེ་དུ་མ་ཡིན་པ་ལ་འཁྲུར་འཇུག་ན་སྤང་བའི་ལྟུང་བྱེད་དུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཚིག་གིས་འདུ་བྱས་པ་ཙམ་གྱིས༌[^2699]འདི་ལ་འདི་དགོས་པའོ། །

[Block 3938]
ལོངས་སྤྱོད་པ༌[^2700]འདུ་བྱེད་དུ་བཅུག་པ་ཞེས་བྱ་བ་འདི་ཙམ་གྱིས་ཞེས་བྱ་སྟེ་དེ་བས་ན༌[^2701]འཁྲུར་འོས་པའི་ཚིག་གོ། །

[Block 3939]
ཕྱོགས་ལ་བྱས་པ་ཡང་ལས་བྱས་པ་ཉིད་དོ་ཞེས་བྱ་བ་ལ་ཕྱོགས་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་རྫས་ཕྱོགས་གཅིག་ཏུ་སོང་བ་ཉིད་དམ་རྒྱུན་དུམ་བུར་གྱུར་པ་ཉིད་ཀྱིས་ཕྱོགས་ཤེས་པར་བྱའོ། །

[Block 3940]
འདིར་གཞུང་ནི་འདིར་བཙུན་པ་འདི་ལྟར་ཡོད་པར་གྱུར་པ་ཞིག་ན་དགེ་སློང་ཆོས་གོས་རུང་བར་གྲོང་དུ་ཞུགས་ཤིང་དེའི་ཆོས་གོས་དེ་ཡང་ལུས་ལས་མ་ཕུད་པར་དེ༌[^2702]སྤང་བར་བགྱི་བའི་སླད་དུ་དབྱུང་བར་འགྱུར་བར་མཆིས་སམ། ཉེ་བ་འཁོར་ཡོད་དེ། ཇི་ལྟར་ཡང་དགེ་སློང་ཁྱིམ་གྱི་ནང་དུ་ཞུགས་པ་ལས་ཆོས་གོས་བཤང་བ་འམ་གཅི་བ་འམ་འདམ་གྱིས་སམ་ལུད་པས་སམ་མི་གཙང་བ་གཞན་དང་གཞན་གྱིས་གོས་པར་གྱུར་ཏེ། དེ་མ་གནང་བའི་དགེ་སློང་མ་ལ་འཁྲུར་འཇུག་ན་སྤང་བའི་ལྟུང་བྱེད་དུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3941]
འདི་ནི་རྫས་ཕྱོགས་གཅིག་ཏུ་སོང་བ་ཞེས་བྱ་བའོ། །

[Block 3942]
ཕྱོགས་གཅིག་ལས་ལྷག་པ་འདི་ནི་ལུས་ལས་མ་ཕུད་པའི་ཚིག་གིས་རྒྱུན་དུམ་བུར་གྱུར་པ༌[^2703]ཉིད༌[^2704]ཅེས་བྱ་བ་ཉིད་ཀྱིས་ཤེས་པར་བྱའོ། །

[Block 3943]
འདིར་འཁྲུར་འཇུག་པར་བྱ་ཞེས་བྱ་བ་ནི་ཐ་ན་ཆུར་སྙུག་པར་བྱེད་དམ། ཚོན་དུ་སྙུག་པར་བྱེད་དམ་འཚེད་དུ་འཇུག་པར་བྱེད་དམ་ཐ་ན་ཐལ་མོས་རྡེབ་པར་བྱེད་ན་ཡང་ངོ་ཞེས་གསུངས་པ་ལྟ་བུའོ། །

[Block 3944]
བྱས་པ་ཉིད་ན་བྱེད་དུ་བཅུག་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གང་གི་ཚེ་དེ་ལས་དེ་ངེས་པར་སྦྱོར་བ་བྱས་པར་འགྱུར་བ་དེའི་ཚེ་བྱེད་དུ་བཅུག་པ་ཉིད་འགྲུབ་པར་འགྱུར་ཏེ་ཉེས་བྱས་ཀྱི་སྦྱོར་བ་ཙམ་ལ་མ་ཡིན་ནོ། །

[Block 3945]
འབྲས་བུའི་མཐའ་མན་ཆད་གཅིག་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་འབྲས་བུའི་མཐར་ཐུག་པ་ནི་ཇི་སྲིད་དུ་ལས་ཀྱིས་གཅིག་པ༌[^2705]ཉིད་དོ། །

[Block 3946]
ཚིགས་སུ་གྱུར་པ་ཉིད་ལ་འབྲས་བུ་རྣམས་གཅིག་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་ཚིགས་སུ་གྱུར་པ་སྔ་མ་དང་ཕྱི་མའི་ཆ་ཉིད་ཀྱིས་ཡིད་ལ་འབྲེལ་པར་གྱུར་པ་དུ་མའི་འབྲས་བུ་རྣམས་གང་ཡིན་པ་ནི་འདི་ལྟ་སྟེ། རུང་བ་ཉིད་ཀྱིས་ཐོབ་པའི་མཐར་ཐུག་པ་འདུ་བྱེད་པའི་དགོངས་པས་རྩོམ་པ་ལ་འཁྲུར་འཇུག་པ་དང་འཚེད་དུ་འཇུག་པ་དང༌[^2706]འཆག་ཏུ་འཇུག་པར་བྱེད་པ་ཉིད་དག་གིས་གཅིག་པ་ཉིད་དོ། །

[Block 3947]
དེ་རྣམས་ལ་དེའི་དབྱེ་བ་དང་བསྒོ་བ་དང་ལས་ཀྱི་དབྱེ་བས་གཅིག་པ་ཉིད་དོ། །

[Block 3948]
དེ་ལ་ཐ་མའི་ཚིགས་ཀྱི་ཐ་མའི་བར་དུ་འཁྲུར་འཇུག་པ་ལ་སོགས་པའི་ལས་གསུམ་པོ་རྗེས་སུ་བསྒྲུབ་པ༌[^2707]ལ་གང་ཞིག་ལྟུང་བ་རེ་རེར་གསུངས་པ་དེ་བས་མདོ་འདི་དང༌[^2708]སྔ་མའོ། །

[Block 3949]
འདུ་ཤེས་གཙོ་བོ་ཉིད་ལ་དོན་ཇི་ལྟ་བ་ཉིད་ལ་ནི་དངོས་གཞིའོ། །

[Block 3950]
དོན་ཇི་ལྟ་བ་མ་ཡིན་པ་ཉིད་ལ་ནི་དངོས་གཞི་དང་ཉེ་བའོ་ཞེས་བྱ་བ་ནི་གང་དུ་འདུ་ཤེས་གཙོ་ཆེ་བ་ཉིད་དེ་ལ་ཆོ་ག་ནི་འདི་རིག་པར་བྱའོ། །

[Block 3951]
འདུ་ཤེས་པ་ནི་དོན་ཇི་ལྟ་བ་ཉིད་ལ་ནི་དངོས་གཞིའི་ལྟུང་བའོ། །

[Block 3952]
དོན་ཇི་ལྟ་བ་ཉིད་མ་ཡིན་པ་ལ་ནི་གང་ཞིག་དེ་དང་ཉེ་བའོ་ཞེས་བྱ་བ་ནི་བར་མེད་པའི་ཚིགས་སུ་གྱུར་པའོ། །

[Block 3953]
ཡིད་གཉིས་ནི་འདུ་ཤེས་དང་འདྲའོ་ཞེས་བྱ་བ་ནི་ཡིད་གཉིས་ནི་འདུ་ཤེས་དང་འདྲ་བ་ཉིད་དོ། །

[Block 3954]
ཡིད་གཉིས་ཟ་བ་ལ་ཡང༌[^2709]དོན་དེ་ལ་ལྟུང་བ་དེ་ཉིད་དུ་འགྱུར་རོ། །

[Block 3955]
གང་ཞིག་དེ་ལ་འདུ་ཤེས་ཤིང་ཞེས་བྱ་བའོ། །

[Block 3956]
དགེ་འདུན་གྱི་ཁྲིམས་སུ་བཅའ་བ་བསྲུང་བར་བྱའོ། །

[Block 3957]
གློ་བུར་དུ་འོངས་པས་ཀྱང་དེ་ལས་མི་འགལ་བ་ཉིད་དུ་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ལས་ཞེས་བྱ་བ་ནི་ཁྲིམས་སུ་བཅའ་བ་རྗེས་སུ་བསྲུང་བ་ལས་སོ། །

[Block 3958]
གློ་བུར་དུ་འོངས་པས་ཀྱང་དེ་ལ་རྗེས་སུ་བསྲུང་བར་བྱ་བ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 3959]
ཡོད་དམ་མེད་པ་ཉིད་དང་ཇི་ལྟ་བུ་ཡོངས་སུ་ཤེས་པར་བྱ་བའི་ཕྱིར་དེས་དེ་དྲི་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ཚོགས་འདི་ན་དགེ་འདུན་གྱི་ཁྲིམས་སུ་བྱ་བ་འགའ་ཞིག་ཡོད་དམ་འོན་ཏེ་མེད་ཡོད་ན་ཇི་ལྟ་བུ་ཞིག་ཅེས་བྱ་བ་དེ་ཡོངས་སུ་ཤེས་པར་བྱ་བའི་ཕྱིར་གློ་བུར་དུ་འོངས་པ་དེས་དེ་དྲི་བར་བྱའོ། །

[Block 3960]
དུས་གང་གི་ཚེ་ཞེ་ན། དེའི་ཕྱིར་ཧ་ཅང་ཡུན་རིང་བའོ་ཞེས་བྱ་བ་སྨོས་ཏེ་ཧ་ཅང་ཡུན་རིང་དུ་གནས་པ་བས་སྔ་རོལ་དུ་ཞེས་བྱ་བའི་དོན་ཏོ། །
--- END BLOCKS ---
