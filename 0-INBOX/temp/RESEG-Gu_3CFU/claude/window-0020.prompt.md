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
གནང་བ་འདི་ཉིད་ལས་ནི་འདིས་ཡང་དག་པར་བླངས་པ་འདི་ལས་ཉམས་པར་འགྱུར་བ་མ་ཡིན་ཞེས་བྱ་བར་རིག་པར༌[^499]བྱའོ། །

[Block 702]
མེད་ན་མདུན་དང་རྒྱབ་ནས་ལོ་མ་དག་གིས་གླན་ལ་དབེན་པའི་ཕྱོགས་སུ་ཁྲུས་བྱའོ་ཞེས་བྱ་བ་ལ། ཐམས་ཅད་དུ་ཆོས་གོས་གསུམ་པ་ཉིད་ནི་མ་ཡིན་ཏེ། འདིར་གཞུང་ནི། གཞན་རྣམས་ལ་ཁྲུས་རས་ཀྱི་རྙེད་པ་མེད་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དེ་རྣམས་ཀྱི་མདུན་དང་རྒྱབ་ནས་ལོ་མ་རྣམས་ཀྱིས༌[^500]གླན་ལ་དབེན་པའི་ས་ཕྱོགས་སུ་ཁྲུས༌[^501]བྱའོ་ཞེས་བྱ་བ་ཁྱད་པར་མེད་པར་གསུངས་པ་ཡིན་ནོ།[^502] །སྲོག་ཆགས་ཆགས་ན་བཤལ་བས་མེད་པར་འགྱུར་རོ་ཞེས་བྱ་བ་ནི་རིམ་པ་གཅིག་ལས༌[^503]ཉི་རིམ་ལ་སྲོག༌[^504]ཆགས་ན་ཞེས་བྱ་བ་འདི་ལས་རྟོགས་པའོ། །

[Block 703]
ལྷན་པ་ཅན་ཡང་ཉི་རིམ༌[^505]མེད་པ་མ་ཡིན་ནོ། །

[Block 704]
དེ་བས་ན་འདིས་སྲོག་ཆགས་དང་བཅས་པའི་ཆུ་ལ་ཁྲུས་མི་བྱའོ་ཞེས་བྱ་བ་འདིར་གནས་པར་རིག་པར༌[^506]བྱའོ། །

[Block 705]
དེ་གཙུག་ལག་ཁང་དུ་ནི་སྟོར་ཁུང་དུའོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་གཙུག་ལག་ཁང་དུ་འདི་ཁྲུས་བྱེད་ན་སྟོར་ཁུང་ཉིད་དུ་བྱ་སྟེ་གཞན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 706]
བཙོག༌[^507]ཆུ་ཡང་དབོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་རྐང་པ་བཀྲུས་པ་ལ་སོགས་པའི་ཆུ་སྟོར་ཁུང་ཉིད་དུ་དབོ་བར་བྱའི༌[^508]གཞན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 707]
ཁྲུས་ཁང་བྱའོ། །

[Block 708]
དེར་སོ་ཕག་གི་གཅལ་དགྲམ་མོ་ཞེས་བྱ་བ་ལ། དེར་ནི་ཁྲུས་ཀྱི་ཁང་པ་ལ་བྱའོ། །

[Block 709]
སྟོར་ཁུང་གདོད་དོ། །

[Block 710]
ལྗན་ལྗིན་བསལ་བར་བྱའོ་ཞེས་བྱ་བ་ལ། འདིར་གཞུང་ནི་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། སྟོར་ཁུང་གདོད་པར་བྱའོ། །

[Block 711]
ལྗན་ལྗིན་ཡོད་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དུས་དུས་སུ་བསལ་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 712]
འོན་ཀྱང་སྟོར་ཁུང་ཁོ་ནར་ཁྲུས་བྱའོ་ཞེས་གསུངས་པས་དེ་བསྡུ་བའི་ཕྱིར། སྟོར་ཁུང་དུ་ཁྲུས་བྱེད་ན་དེ་མི་འབྱུང་ངོ་ཞེས་བྱ་བ་སྨོས༌[^509]ཏེ། ལྗན་ལྗིན་ཞེས་བྱ་བ་རྗེས་སུ་འབྲེལ་ལོ།[^510] །ཁྲུས་བྱེད་པ་ནི་ཁྲུས་བྱེད་པའོ། །

[Block 713]
ལྗན་ལྗིན་བྱུང་བ་སོ་སོའི་ཆོ་ག་ལ་བརྗོད་པ་འདི་ཡིན་ནོ། །

[Block 714]
སྟོར་ཁུང་དུ་ཁྲུས་བྱེད་ན་ལྗན་ལྗིན་མི་འབྱུང་ངོ་ཞེས་བྱ་བ་སྟེ། སྟོར་ཁུང་ཉིད་དུ་ཁྲུས་བྱ་བ་ནི་མ་ཡིན་ནོ། །

[Block 715]
དེའི་ཕྱིར་ངེས་པར་གྱུར་པ་སྟེ། ཁང་པ་ནི་ཁྲུས་ཀྱི་ཁང་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 716]
སོ་ཕག་གི་དུམ་བུས་བྲུད་པས་རྐང་པ་གཉིས་ལས་གཞན་པའི་ལུས་ལ་བྲུད་པར་མི་བྱའོ་ཞེས་བྱ་བ༌[^511]ནི་སོ་ཕག་གི་དུམ་བུས་དགེ་སློང་གིས་ལུས་བྲུད་པར་བྱ་བ་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་གཞུང་ལས་སོ། །

[Block 717]
གཞན་པའི་ཞེས་བྱ་བ་ནི་རྐང་པ་གཉིས་ལས་ཐ་དད་པའོ། །

[Block 718]
དེ་དག་ལས་ནི་བཀག་པ་མེད་དོ། །

[Block 719]
དེ་ནི་དཔེ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་བྲུད་པའོ། །

[Block 720]
རྫས་ཇི་ལྟ་བུ་ལ་ཤེས་པར་བྱ་ཞེ༌[^512]ན། རྣོན་པོ་དང་བཞར་སྤྱད་དག་ལའོ། །

[Block 721]
རྣོན་པོ་ཞེས་བྱ་བ་ནི་མཚོན་ལ་སོགས་པའོ། །

[Block 722]
བཞར་སྤྱད་ཅེས་བྱ་བ་ནི་སྤུ་བ་ལ་སོགས་པ་སྟེ། སེམས་ཀྱི་རྣམ་པར་འགྱུར་བ༌[^513]སྒྲུབ་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 723]
འདིར་གཞུང་ནི་བཅོམ་ལྡན་འདས་ཀྱིས་སོ་ཕག་གི༌[^514]དུམ་བུས་ལུས་ལ་བྲུད་པར་མི་བྱའོ་ཞེས་བྱ་བ་བཀའ་སྩལ་པ་དང་། དགེ་སློང་དག་ཉ་ཕྱིས་ཀྱིས་བྲུད་པར་བྱེད་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ཉ་ཕྱིས་མི་རྣོ་བས་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 724]
འདིར་ཉ་ཕྱིས་རྣོ་བ་ཉིད་འདིར་བཀག་པའོ། །

[Block 725]
དེ་བས་ན་སོ་ཕག་གི་དུམ་བུ་ནི་དཔེ་ཡིན་ནོ། །

[Block 726]
རྣོན་པོ་བཞན༌[^515]ལ་ཡང་གཞར༌[^516]སྤྱད་ཀྱི་རྫས་ལ་དེས་ཀྱང་ལུས་ལ་བྲུད་པར་མི་བྱའོ། །

[Block 727]
ཉ་ཕྱིས་ནི་མེས༌[^517]སྦྱང་ངོ་ཞེས་བྱ་བ་ནི་འདི་ལ་མེས་རབ་ཏུ་གདུང་བ་ཙམ་སྦྱང་བ་སྟེ། གཞན་ནི་ཉ་ཕྱིས་ཉམས་པའི་ཕྱིར་རོ། །

[Block 728]
དགེ་སློང་མས་ནི་གང་དུ་ཡང་ཁུ་ཚུར་དག་དང་གོས་གྲིལ་བ་དག་ཡན་ཆད་གང་གིས་ཀྱང་བྲུད་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ཅུང་ཟད་ཅེས་བྱ་བ་ནི་ལུས༌[^518]ཏེ། འཇམ་པའི་བུད་མེད་ཀྱི་ལུས་ཏེ། འཇམ་པ་དང་རྩུབ་པ་མ་ཡིན་པ་ལས་ཀྱང་དེ་ལ༌[^519]རྣམ་པར་འགྱུར་བ་བསྒྲུབ་པའོ། །

[Block 729]
ཤིན་ཏུ་ཁྲུས་པས་འདི་བྱེད་པ་ལ་བུད་མེད་ལ་བཞར་སྤྱད་ཉིད་ནི། དེའི་ཕྱིར་དགེ་སློང་མ་རྣམས་ལ་ཐམས་ཅད་བཀག་པའོ། །

[Block 730]
ཅུང་ཟད་ཁུ་ཚུར་ལས་འཇམ་པ་ལས་གཞན་པའི་གོས་འབྱུང་བ་ཡིན་ནོ་ཞེས་བྱ་བའོ། །

[Block 731]
ཁུ་ཚུར་ཙམ་ཉིད་ཀྱིས་བརྗོད་ནས་གོས་དྲིལ་བའི་ཚིག་གོ། །

[Block 732]
གཤེར་འགྱུར་གྱི་ཆུ་དང་མ་བྲལ་བས་ཆོས་གོས་དག་བགོ༌[^520]བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་བགོ་བར་གྱུར་པའི༌[^521]གོས་ཉམས་པ་ཡོངས་སུ་བསལ་བའི་དོན་དུ་འདི་ཡིན་ནོ། །

[Block 733]
དེ་བས་ན་འདི་རྣམས་ལ་གཤེར་འགྱུར་གྱི་ཆུ་དང་མ་བྲལ་བས་གང་ལ་ཞེས་བྱ་བ་ཤེས་པའོ། །

[Block 734]
གང་ཞིག་མཐོང་བའི་ཕྱིར་བཅུག་པ་མི་འདོད་པ་དེའི་སླད་དུ་འོག་མའི་ཆོ་ག་དག་གོ། །

[Block 735]
ལུས་ཕྱིས་བཅང་བར་བྱའོ། །

[Block 736]
མེད་ན་ཡུད་ཙམ་ཞིག་ཙོག་པུར༌[^522]འདུག་ལ་ཁྲུས་རས་ཀྱིས་ཕྱི་བར་བྱའོ་ཞེས་བྱ་བ་ནི་འཇུག་པ༌[^523]ཇི་ཙམ་གྱིས་འགྲུབ་པས་ཁྲུས་རས་ཀྱིས་ཕྱིས་པས༌[^524]དོན་བསྒྲུབ་པ་དེ་ཙམ་གྱིས་འདི་ལ་ཇི་ཙམ་པའི་དུས་ཀྱི་ཚད་ཀྱིས་བསྒྲུབ་པ༌[^525]དེ་ཉེ་བར་མཚོན་པ་ནི་འདར་ནི་ཡུད་ཙམ་མོ། །

[Block 737]
ཆུང་བ་དག་གིས་དེ་ལ་ཡུད་ཙམ་ཞེས་བྱ་བ་འདི་བརྗོད་པའོ། །

[Block 738]
ཙོག་པུར་འདུག་པ་ཞེས་བྱ༌[^526]ནི་དེ་བཞིན་དུ་མྱུར་དུ་འགྲོ་བའི་ཆུ་ལ་ལུས་ལས་བསྒྲུབ༌[^527]པའོ། །

[Block 739]
འདིར་གནས་པའི་སྦས་པའི་ངོ་བོ་སྟེ། དེ་བས་ན་འདི་སྒྲེན་མོས་བསྟེན་པ༌[^528]རིགས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་ཡང་དག་པར་བསྟན༌[^529]པའོ། །

[Block 740]
བསྲོ་ཁང་བསྟེན་པར་བྱའོ། །
--- END BLOCKS ---
