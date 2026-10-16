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
[Block 841 [VERSE]]
བློ་དོན་འགའ་ལས་རྣམ་བཟློག་ནས། །
དོན་འགའ་ཞིག་ལ་འཇུག་བྱའི་ཕྱིར། །
སྒྲ་ནི་རབ་ཏུ་སྦྱོར་བྱེད་དེ། །
དེའི་དོན་ངེས་པར་བཟུང་ཕྱིར་རོ། །

[Block 842 [VERSE]]
གཞན་དུ་སྦྱོར་བ་དོན་མེད་འགྱུར། །
དེས་ན་ཤེས་བྱ་ལ་སོགས་ཚིག །
ཐ་སྙད་དུ་ནི་རྟོགས་རྣམས་ལའང་། །
རྣམ་པར་གཅོད་པ་འགའ་ཞིག་ཡོད། །

[Block 843]
སྒྲ༌[^704]རབ་ཏུ་སྦྱོར་བར་བྱེད་པ་ཐམས་ཅད་ནི་རྗེས་སུ་འགྲོ་བ་དང་ལྡོག་པ་དག་ལས་མི་འདའ་སྟེ། དེ་ནི་འཇུག་པ་དང་ལྡོག་པའི་དོན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 844]
གལ་ཏེ་འདིས་འགའི་བློ་གང་ལས་ཀྱང་ལྡོག་པར་མི་བྱེད་པའམ། འཇུག་པར་མི་བྱེད་ན་ཇི་ལྟ་བ་བཞིན་དུ་གནང་བའི་ཕྱིར། ཐ་སྙད་ཐམས་ཅད་ལ་འགའ་ཡང་ཐ་སྙད་གདགས་པར་མི་འགྱུར་ཏེ། ཐ་སྙད་ནི་ངེས་པར་གཟུང་བ་མེད་ན་མེད་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 845]
དཔེར་ན་བུམ་པས་ཆུ་འོན་ཅིག་ཅེས་བྱ་བ་ལྟ་བུ་ལ། གལ་ཏེ་བུམ་པ་དང་སྙིམ་པས་ཆུ་ཅི་འདྲ་ཡང་རུང་བ་ཞིག་བླང་བར་འདོད་པར་གྱུར་ན་ནི། ཆུ་འོན་ཅིག་ཅེས་བྱ་བ་ཁོ་ན་བརྗོད་པར་བྱ་བར་འགྱུར་གྱི། བུམ་པས་ཞེས་བྱ་བ་ནི་མ་ཡིན་ནོ། །

[Block 846]
དེ་བཞིན་དུ་ཕྱག་དར་རམ། གཞན་གང་ཡང་རུང་བ་ཞིག་བླང་བར་དགོས་པར་འདོད་པ་ཞིག་ཏུ་གྱུར་ན་ནི། འོན་ཅིག་ཅེས་བྱ་བ་བྱེད་པ་དང་། ལས་མ་འཕངས་པ་ཅན་ཁོ་ན་བརྗོད་པར་བྱ་བར་འགྱུར་རོ། །

[Block 847]
དེ་བཞིན་དུ་བླང་བའམ་བསྒྲུབ་པར་བྱ་བའམ་བསྒྲུབ་པར་བྱ་བ་མ་ཡིན་པ་གཞན་ཅུང་ཟད་ཅིག༌[^705]ཡིན་པར་འདོད་ན་ནི། དེའི་ཚེ་འོན་ཅིག་ཅེས་བྱ་བ་ཡང་བརྗོད་པར་བྱ་བར་མི་འགྱུར་ཏེ། ཚིག་དོན་མེད་པའི་ཕྱིར་རོ། །

[Block 848]
དེ་བཞིན་དུ་ཞེས་བྱ་བ༌[^706]ལ་སོགས་པའི་ཚིག་ཐ་སྙད་དུ་གཏོགས་པ་རྣམས་ལ་ཡང་རྣམ་པར་བཅད་པར་བྱ་བ་འགའ་ཞིག་ཡོད་པར་འགྱུར་ཏེ། གཞན་དུ་དོགས་པ་མེད་ན་སྦྱོར་བ་མི་རུང་བའི་ཕྱིར་རོ། །

[Block 849]
དེ་ལ་ནི་བློ་གྲོས་རྨོངས་པའི་དོགས་པའི་གནས་གང་ཡིན་པ་དེ་ཉིད་བཟློག་པར་བྱ་བ་ཡིན་ནོ། །

[Block 850]
འོན་ཏེ་དོགས་པ་མེད་ན་ནི་གཞན་གྱིས༌[^707]གདམས་པ༌[^708]ཅི་ཞིག་ལྟོས་པར་འགྱུར་རོ། །

[Block 851]
ཉན་པ་པོ་འབྱང་བར་བྱ་བ་མེད་པ་ཅན་སྨྲ་ན་ཡང་ཇི་ལྟར་བསྙོན་པ་མ་ཡིན་ཏེ། དེ་འབྱང་བར་བྱ་བ་ཁོ་ནའི་ཕྱིར་སྒྲ་རྣམས་བརྡར་བྱས་པའི་ཕྱིར་རོ། །ཞེས་བྱ་བ༌[^709]ལ་སོགས་པའི་སྒྲ་ཐ་དད༌[^710]དུ་མ་གཏོགས་པ་ནི་འགའ་ཡང་མེད་དེ། ངག་ཏུ་གཏོགས་པའི་ཚིག་གོ༌[^711]དོན་སེམས་པའི་ཕྱིར་རོ། །གང་ལ་དེ་དག་རབ་ཏུ་སྦྱོར་ཞེ་ན། སྦྱོར་བའི་ཡུལ་བསམ་པ་ལ་གཞན་སེལ་བ་ཞེས་བརྗོད་དོ། །

[Block 852]
སྦྱོར་བ་བསྟན་པ་མེད་པ་ལ་ཤེས་བྱ་ཞེས་བྱ་བའི་སྒྲའི་དོན་ཅི་ཡིན་ཞེས༌[^712]འདྲི་བའི་དོན་འགའ་ཡང་མེད་དེ། དེ་ལས་འགའ་ལ་ཡང་རྟོགས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 853]
བུམ་པ་ལ་སོགས་པའི་སྒྲ་ལ་ཡང་དེ་དང་འདྲའོ། །

[Block 854]
སྐབས་འགའ་ཞིག་ཏུ་མཉན་པ་ཡན་གར་བ་ལས་རྟོགས་པ་གང་ཡིན་པ་ཡང་སྦྱོར་བ་མཐོང་བའི་ཡུལ་གྱི་རྗེས་སུ་འབྲང་བས་ཐེ་ཚོམ་དང་བཅས་པའི་ཕྱིར། དེའི་དོན་ཡོངས་སུ་མ་རྫོགས་པ་ཅན་ཡིན་པས་བུམ་པ་ལ་སོགས་པའི་སྒྲ་ལ་བསླད་པ་ཡིན་ནོ། །

[Block 855]
དེ་དང་འདྲ་བའི་ནི་ཞེས་བྱ་བ་ལ༌[^713]སོགས་པའི་སྒྲ་ལ་ཡང་ཇི་ལྟར་མཐོང་བ་ལས་ཡོད་པ་ཉིད་དོ། །

[Block 856]
དེའི་ཕྱིར་སྒྲ་སྦྱོར་བ་ཐམས་ཅད་ནི་བློ་འབའ་ཞིག༌[^714]ལས་བཟློག་ནས་འགའ་ཞིག་ལ་གཞུག་པར་བྱ་བའི་ཕྱིར་དོན་ཡིན་ཏེ།

[Block 857 [VERSE]]
དེའི༌[^715]འབྲས་བུ་དང་བཅས་པའི་ཕྱིར་རོ། །
གང་ཞིག་གང་ལས་ཐ་དད་པ། །
དེ་རྣམས་བཟློག་ནས་ཁྱད་པར་གྱི། །
དེ་ལས་ཐ་དད་རྣམ་པ་ནི། །

[Block 858 [VERSE]]
མཚུངས་པ༌[^716]སྣང་བ་ཅན་ལ་འགོད། །
དེ་ཉིད་གཞན་ལས་ལྡོག་པ་ཡིས། །
དངོས་པོ་དེ་ཡི་ཆ་འགའ་ཞིག །
རྟོགས་འགྱུར་ཞེས་པས་རབ་ཏུ་བཤད། །

[Block 859 [VERSE]]
འདི་ལའང་ངོ་བོ་ཅུང་ཟད་མེད། །
སྒྲ་རྣམས་ལས་དེ་རྟོགས་ཉིད་ཀྱིས། །
གཞན་བཟློག་རྟོགས་འགྱུར་དེ་ལ་ནི། །
འགའ་ཡིས་ཁྱད་པར་དུ་བྱས་པ། །

[Block 860 [VERSE]]
རྟོགས་པར་འགྱུར་པ་གཞན་འགའ་མེད། །
སྒྲས་གཉིས་བྱེད་པའང་མ་ཡིན་ཏེ། །
ཕན་ཚུན་ཡོད་པའི༌[^717]མིན་ཕྱིར་དེ། །
དངོས་མེད་དངོས་པོ་ལྡན་ཉིད་དུ། །
མཐོང་བ་བློ་ཡིས་བསླད་པ་ཡིན། །

[Block 861]
དགོད་པར༌[^718]བྱ་བའི་སྒྲ་དེ་ལས་གཞན་བཟློག་པ་འཕངས་པ་དེ་ཡང་གང་ཞིག་གང༌[^719]ལས་ཐ་དད་པ་དེ་བཟློག་ནས་ཁྱད་པར་རྣམས་ཀྱི་ཐ་དད་པ་ངོ་བོ་མཚུངས་པར་སྣང་བ་ལ་འགོད་དོ། །

[Block 862]
དེ་ཉིད་དོན་གཞན་ལས་ལྡོག་པས་དངོས་པོའི་དེའི༌[^720]ཆ་འགའ་ཞིག་རྟོགས་པར་འགྱུར་རོ་ཞེས་བྱ་བ་དང་། སྒྲ་ནི་དོན་གཞན་ལས་ལྡོག་པ་འཕངས༌[^721]པས་ཁྱད་པར་དུ་བྱས་པའི་དངོས་པོ་དག་ཁོ་ན་བརྗོད་དོ་ཞེས་བྱ་བ་ལ་སོགས་པས་བསྟན་ཏོ། །

[Block 863]
དེ་ནི་ཐ་དད་པ་དེ་བརྗོད་པ་ན་དོན་ཐ་དད་པ་རྣམ་པར་གཅོད་པ་འཕེན་པ་ལྟ་བུར་འཇུག་སྟེ། གཅིག་ལ་ཡོད་པའི་ཐ་དད་པ་བརྗོད་པ་ནི་དེ་ལས་གཞན་པ་བཟློག་པ་མེད་ན་མེད་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 864]
ཐ་དད་པ་དེ་ཉིད་ནི༌[^722]ལྡོག་པས་ཆ་རྟོགས་པ་ཡིན་ནོ། །

[Block 865]
དེ་རྟོགས་པ་ནི་དེའི་ཁྱད་པར་ཅན་ཡིན་པའི་ཕྱིར། དེས་ཁྱད་པར་དུ་བྱས་པ་རྟོགས་པ་ཞེས་བྱ་བའི༌[^723]དོན་ཁ་ཅིག་ལ་ཁར་བ་ཐོགས་པ་བཞིན་དུ་གང་ཞིག་གང་གིས་ཁྱད་པར་དུ་བྱས་པ་རྣམས་སྒྲ་དག་གིས་བརྗོད་པར་འགྱུར་བ་དོན་གཞན་བཟློག་པ་བྱེ་བྲག་ཏུ་གྱུར་པ༌[^724]ཡོད་པ་ནི་མ་ཡིན་ནོ། །

[Block 866]
དབྱེ་བར་བྱ་བ་གཉིས་ཀྱི་ཐ་དད་པ་ནི་གཉི་ག་ལ་ཡོད་པའི་ཕྱིར། གཅིག་ལ་ཡོད་པའི་ཐ་དད་པར་བརྗོད་ན་ཡང་དེ་ལས་གཞན་པ་འཕེན་པ་མེད་ན་མེད་པ་ཡིན་ནོ། །

[Block 867]
དེ་བས་ན་དེ་དག་ལ་ཁྱད་པར་དང་ཁྱད་པར་གྱི་གཞིའི་དངོས་པོ་ནི་མེད་དོ། །

[Block 868]
ཐ་དད་པ་གཅིག་བརྗོད་ན་ཡང་གཞན་བཟློག་པ་རྟོགས་པའི་ཕྱིར། རྗེས་སུ་འགྲོ་བ་དང་ལྡོག་པ་བརྗོད་པས་སྒྲ་རྣམས་ཐ་སྙད་ཀྱི་ཡན་ལག་ཉིད་དུ་སྟོན་པ་ན་དེ་ལས་ལྡོག་པ་རྟོགས་པར་འགྱུར་བའམ། དེས་ཀྱང་ཁྱད་པར་དུ་བྱས་པ་ཞེས་བཤད་དོ། །

[Block 869]
དེ་ཉིད་ཀྱི་ཕྱིར་སྒྲ་ལ་དེ་ལས་གཞན་པ་བཟློག་པ་དང་། རང་གི་དོན་བརྗོད་པ་དང་བྱ་བ་གཉིས་ནི་མེད་དོ། །

[Block 870]
རང་གི་དོན་བརྗོད་པ་ཁོ་ནས་དེ་ལས་གཞན་པ་བཟློག་པ་རྟོགས་པའི་ཕྱིར་ཏེ། རང་གི་དོན་ནི་ཐ་དད་པའི་ངོ་བོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 871]
ལྡོག་པ་མེད་པ་ཅན་གྱི་རྗེས་སུ་འགྲོ་བ་མེད་ལ། རྗེས་སུ་འགྲོ་བ་མེད་པ་ཅན་གྱི་ལྡོག་པ་ཡང་མེད་དེ། གཅིག་རྗེས་སུ་འགྲོ་བ་ལ་ཡོངས་སུ་སྤང་བར་བྱ་བ་མེད་པ་དང་། དེ་བཞིན་དུ་གཅིག་ཡོངས་སུ་སྤང་བ་ལ་ཡང་འགའ་ཞིག་ལ་གནས་པ་མེད་ན་བརྗོད་པ་མེད༌[^725]པ་འབྲས་བུ་མེད་པའི་ཕྱིར་རོ། །

[Block 872]
ཐ་དད་པ་དེ་ཡང་དངོས་པོ་མེད་པ་ཡིན་ཏེ། དངོས་པོ་དང་ལྡན་པ་ཉིད་དུ་མཐོང་བ་ནི་བློའི་བསླད་པ་ཡིན་པ་འབའ་ཞིག་ཏུ་ཟད་དོ། །

[Block 873 [VERSE]]
དེ་ཕྱིར་དེ་ཉིད་དོན་དམ་མིན། །
གཞན་དུ༌[^726]དངོས་པོར་འགྱུར་ལྡོག་པ། །
དངོས་པོར་མི་འགྱུར༌[^727]འདི་འདི་ལ། །
ཐ་དད་ཅེས་ནི་བརྗོད་ཕྱིར་རོ། །

[Block 874]
དངོས་པོ་ནི་དོན་དམ་པ་ཡིན་ལ། གལ་ཏེ་ཐ་དད་པ༌[^728]དངོས་པོར་འགྱུར་བ་དེའི་དངོས་པོའམ། དེའི་དངོས་པོ་མ་ཡིན་པར་འགྱུར། དེའི་དངོས་པོ་ཉིད་ཡིན་ན་དེ་ཉིད་ཡིན༌[^729]པས་ན་གཞན་དེ་ལས་ཐ་དད་པ་མ་ཡིན་ཏེ། དེའི་དངོས་གཞན་གྱིར༌[^730]མི་འགྱུར་རོ། །

[Block 875]
དེ་ཉིད་མ་ཡིན་ཏེ། ཐ་དད་པའི་དངོས་པོ་ཡིན་ན་ནི་དངོས་པོ་ཡང་གཞན་ཉིད་དུ་འགྱུར་བ་དེ་བས་ན་དངོས་པོ་དེ་ལས་ལྡོག་པར་འགྱུར་བ་དེའི་ཕྱིར། འདི་ལས་འདི་ཐ་དད་པ་ཡིན་ནོ་ཞེས་བྱ་བར་མི་འགྱུར་རོ། །

[Block 876]
གང་ཞིག་ཐ་དད་པ་གང་ལས་ལྡོག་པར་འགྱུར་བ་དེ་ཉིད་དེར་འགྱུར་བའི་ཕྱིར། འདི་འདི་ལས་ཐ་དད་པར་ཡིན༌[^731]ནོ་ཞེས་བྱ་བར་མི་འགྱུར་ཏེ། ཕན་ཚུན་ཐ་དད་པར་འགྱུར་བའི་འབྲེལ་པ་ནི་མེད་པའི་ཕྱིར་རོ། །

[Block 877]
འབྲེལ་པ་ཡོད་པ་ཡིན་ན་ཡང་དེ་རྒྱུ་དང་འབྲས་བུའི་དངོས་པོ་ཡིན་པས་དེ་ལས་སྐྱེས་པའི་དངོས་པོ་ཐ་དད་པ་ཞེས་བྱ་བར་བྱེ་བྲག་མེད་པའི་ཕྱིར། རང་གི་རྒྱུ་རྣམས་ཀྱི་འབྲས་བུ་ཐམས་ཅད་ལྡོག་པར་འགྱུར་རོ། །

[Block 878]
ཐ་དད་པའི་དངོས་པོ༌[^732]གཞན་ཡིན་པ༌[^733]དེ་ལས་ཀྱང་འདི་ཐ་དད་པ་ཡིན་པས༌[^734]ཐ་དད་པའི་ཁྱད་པར་ཉིད་ཀྱིས་རྫས་གཞན་དང་འདྲ་བར་ཐ་དད་པར་མི་འགྱུར་རོ། །

[Block 879]
ཐ་དད་པའི་ཁྱད་པར་ཁོ་ན༌[^735]ཐ་དད་པ་མ་ཡིན་ཏེ། འདི༌[^736]འདི་ལས་ཞེས་བྱ་བའི་ཁྱད་པར་བསྟན་པའི་ཕྱིར་རོ། །

[Block 880]
དེ་བས༌[^737]ན་ཁྱད་པར་གྱི་དངོས་པོ་མེད་པ་ལ་ཐ་དད་པ་ཉིད་ཀྱིས༌[^738]དངོས་པོ་མེད་པར་འགྱུར་བ་དེ་བས་ན་གཞན་པ་ཉིད་མ་ཡིན་ནོ། །
--- END BLOCKS ---
