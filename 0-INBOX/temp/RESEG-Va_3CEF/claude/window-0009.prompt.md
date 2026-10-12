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
[Block 676]
ཆེད་དུ་བྱ་བ་དམ་པ་ནི༌[^258]སེམས་ཅན་ཐམས་ཅད་ཀྱི་དོན་བྱ་བའི་ཆེད་ཀྱི་ཕྱིར་རོ། །

[Block 677]
ཟད་མི་ཤེས་པ་དམ་པ་ནི་བྱང་ཆུབ་ཆེན་པོར་ཡོངས་སུ་བསྔོས་པས་གཏན་དུ་ཡོངས་སུ་གཏུགས་པར་མི་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 678]
རྒྱུན་མི་འཆད་པའི་དམ་པ་ནི་བདག་གཞན་མཉམ་པ་ཉིད་དུ་མོས་པའི་ཕྱིར་ཏེ། སེམས་ཅན་ཐམས་ཅད་ལ་སྦྱིན་པ་ལ་སོགས་པས་ཕ་རོལ་ཏུ་ཕྱིན་པ་རྣམས་ཡོངས་སུ་རྫོགས་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 679]
ཚེགས་མེད་པ་དམ་པ་ནི་གཞན་གྱི་སྦྱིན་པ་ལ་སོགས་པ་ལ་རྗེས་སུ་ཡི་རང་བ་ཙམ་གྱིས༌[^259]ཕ་རོལ་ཏུ་ཕྱིན་པ་ཡོངས་སུ་རྫོགས་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 680]
དབང་འབྱོར་པ་དམ་པ་ནི་ནམ་མཁའ་མཛོད་ཀྱི་ཏིང་ངེ་འཛིན་ལ་སོགས་པ་སྦྱིན་པ་ལ་སོགས་པ་ཡོངས་སུ་རྫོགས་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 681]
ཡོངས་སུ་གཟུང་བ་དམ་པ་ནི་རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་ཀྱིས་ཡོངས་སུ་བཟུང་བའི་ཕྱིར་རོ། །

[Block 682]
རྩོམ་པ་དམ་པ་ནི་མོས་པས་སྤྱོད་པའི་ས་ལ་བཟོད་པ་ཆེར་གྱུར་པའོ། །

[Block 683]
འཐོབ་པ་དམ་པ་ནི་ས་དང་པོ་ལའོ། །

[Block 684]
རྒྱུ་མཐུན་པ་དམ་པ་ནི་དེ་མ་ཡིན་པ་གཞན་བརྒྱད་པོ་དག་ལའོ། །

[Block 685]
འགྲུབ་པ་དམ་པ་ནི་ས་བཅུ་པ་དང་། དེ་བཞིན་གཤེགས་པའི་ས་ལ་བྱང་ཆུབ་སེམས་དཔའ་འགྲུབ་པ་དང་། སངས་རྒྱས་འགྲུབ་པའི་ཕྱིར་རོ། །

[Block 686]
དེའི་ཕྱིར༌[^260]དམ་པའི་དོན་གྱིས་ནི།[^261] །ཕ་རོལ་ཕྱིན་པ་བཅུར་འདོད་དོ། །

[Block 687]
འདི་ལྟར་དམ་པ་རྣམ་པ༌[^262]བཅུ་གཉིས་པོ་འདི་དག་ནི་དེ་དག་ལ་ཡོད་པའི་ཕྱིར༌[^263]དམ་པ་ཞེས་བྱ་སྟེ། དོན་འདིས་ཕ་རོལ་ཏུ་ཕྱིན་པ་བཅུ་པོ༌[^264]དག་ཏུ་འདོད་དོ། །

[Block 688]
ཁ་ཅིག་བཅུ་གང་ཡིན་སྙམ་དུ་སེམས་པ་ལ་དེ་དག་གི༌[^265]མིང་བསྟན་པར་བྱ་བའི་ཕྱིར།

[Block 689 [VERSE]]
སྦྱིན་དང་ཚུལ་ཁྲིམས་བཟོད་བརྩོན་འགྲུས། །
བསམ་གཏན་དང་ནི་ཤེས་རབ་ཐབས། །
སྨོན་ལམ་སྟོབས་དང་ཡེ་ཤེས་དང་། །

[Block 690]
འདི་དག་ཕ་རོལ་ཕྱིན་པ་བཅུ།[^266] །ཞེས་བྱ་བ་བརྗོད་དོ། །

[Block 691]
འདི་དག་གི་སོ་སོའི་ལས་ཅི་ཞེ་ན།

[Block 692 [VERSE]]
ལས་ནི་རྗེས་སུ་འཛིན་བྱེད་དང་། །
གནོད་མི་བྱེད་དང་དེ་ལ་བཟོད། །
ཡོན་ཏན་འཕེལ་དང་འཛུད་ནུས་དང་། །
རྣམ་པར་གྲོལ་བར་བྱད་པ་དང་། །

[Block 693 [VERSE]]
མི་ཟད་པ་དང་རྟག་འཇུག་དང་། །
ངེས་པར་ལོངས་སྤྱོད་སྨིན་པར་བྱེད། །

[Block 694]
འདི་དག་ནི་གོ་རིམས་བཞིན་དུ་དེ་དག་གི་ལས་ཏེ། བྱང་ཆུབ་སེམས་དཔའི་སྦྱིན་པས་ནི་སེམས་ཅན་རྣམས་རྗེས་སུ་འཛིན་ཏོ། །

[Block 695]
ཚུལ་ཁྲིམས་ཀྱིས་ནི་དེ་དག་ལ་གནོད་པར་མི་བྱེད་དོ། །

[Block 696]
བཟོད་པས་ནི་གཞན་དག་གིས༌[^267]གནོད་པར་བྱས་པ་ལ་ཅི་མི་སྙམ་པར་བྱེད་དོ། །

[Block 697]
བརྩོན་འགྲུས་ཀྱིས་ནི་ཡོན་ཏན་རྣམས་འཕེལ་བར་བྱེད་དོ། །

[Block 698]
བསམ་གཏན་གྱིས་ནི་རྫུ་འཕྲུལ་ལ་སོགས་པས་མགུ་བར་བྱས་ཏེ་འཛུད་དོ། །ཤེས་རབ་ཀྱིས་ནི་ཡང་དག་པའི་གདམས་ངག་བྱིན་པས་རྣམ་པར་གྲོལ་བར་བྱེད་དོ། །

[Block 699]
ཐབས་ལ་མཁས་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པས་ནི་བྱང་ཆུབ་ཆེན་པོར་ཡོངས་སུ་བསྔོས་པས་སྦྱིན་པ་ལ་སོགས་པ་མི་ཟད་པར་བྱེད་དོ། །

[Block 700]
སྨོན་ལམ་གྱི་ཕ་རོལ་ཏུ་ཕྱིན་པས་ནི་མཐུན་པའི་སྐྱེ་བ་ཡོངས་སུ་འཛིན་པས་ཚེ་རབས་ཐམས་ཅད་དུ་སངས་རྒྱས་འབྱུང་བ་ལ༌[^268]མཉེས་པར་བྱེད་ཅིང་སྦྱིན་པ་ལ་སོགས་པ་ལ་རྟག་ཏུ་འཇུག་གོ། །

[Block 701]
སྟོབས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པས་ནི་སོ་སོར་རྟོག་པ་དང་། བསྒོམ་པའི༌[^269]སྟོབས་གཉིས་ཀྱིས་མི་མཐུན་པའི་ཕྱོགས་ཀྱིས་ཟིལ་གྱིས་མི་ནོན༌[^270]པའི་ཕྱིར་སྦྱིན་པ་ལ་སོགས་པ་ལ་ངེས་པར་འཇུག་གོ། །

[Block 702]
ཡེ་ཤེས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པས་ནི་ཆོས་ལ་སྒྲ་ཇི༌[^271]བཞིན་དུ་རྨོངས་པ་དང་བྲལ་བས་སྦྱིན་པ་ལ་སོགས་པའི་དབང་དུ་མཛད་པའི་ཆོས་ལ་ལོངས་སྤྱོད་པ་མྱོང་བ་དང་། སེམས་ཅན་རྣམས་ཀྱང་ཡོངས་སུ་སྨིན་པར་བྱེད་དོ། །

[Block 703]
དམ་པ་བསྒྲུབ་པ་བཤད་ཟིན་ཏོ། །

[Block 704 [HEADING]]
#### ཡིད་ལ་བྱེད་པ་བསྒྲུབ་པ། ^7-1-2-0

[Block 705]
ཡིད་ལ་བྱེད་པ་བསྒྲུབ་པ་གང་ཞེ་ན།

[Block 706 [VERSE]]
ཐེག་པ་ཆེན་པོར་ཅི་ལྟ་བུར། །
ཆོས་རྣམས་བཏགས་པར༌[^272]མཛད་པ་དག །
བྱང་ཆུབ་སེམས་དཔའ་རྟག་པར་ཡང་། །
ཤེས་རབ་གསུམ་གྱིས་ཡིད༌[^273]བྱེད་པའོ། །

[Block 707]
སྦྱིན་པ་ལ་སོགས་པའི་དབང་དུ་མཛད་ནས་ཐེག་པ་ཆེན་པོར་མདོ་ལ་སོགས་པ་ཇི་ལྟར་བཏགས་པའི་ཆོས་རྣམས་ཐོས་པ་དང་། བསམས་པ་དང་། བསྒོམས་པ་ལས་བྱུང་བའི༌[^274]ཤེས་རབ་ཀྱིས་རྒྱུན་དུ་ཡིད་ལ་བྱེད་པ་ནི་ཡིད་ལ་བྱེད་པ་བསྒྲུབ་པའོ། །ཤེས་རབ་རྣམ་པ་གསུམ་གྱིས་ཡིད་ལ་བྱེད་པ་དེས་ཡོན་ཏན་ཅི་ཞིག་ཐོབ་ཅེ་ན།

[Block 708 [VERSE]]
ཁམས་བརྟས༌[^275]བྱེད་དང་འཇུག་བྱེད་དང་། །
དེ་ནི་དོན་རྣམས་འགྲུབ་པར་འགྱུར། །

[Block 709]
ཐོས་པ་ལས་བྱུང་བའི་ཤེས་རབ་ཀྱིས་ཡིད་ལ་བྱེད་པས་ཁམས་བརྟས་པར༌[^276]འགྱུར་རོ། །

[Block 710]
བསམས་པ༌[^277]ལས་བྱུང་བས་ནི་ཐོས་པ་དེའི༌[^278]དོན་ལ་སྙིང་ནས་འཇུག་པར་བྱེད་དོ། །

[Block 711]
བསྒོམས་པ་ལས་བྱུང་བས་ནི་དོན་འགྲུབ་པར་འགྱུར་ཏེ། ས་ལ་འཇུག་པ་ཡོངས་སུ་སྦྱོང་བའི་ཕྱིར་རོ། །

[Block 712 [VERSE]]
དེ་ནི་ཆོས་སྤྱོད་རྣམ་བཅུ་དང་། །
ཡང་དག་ལྡན་པར་ཤེས་པར་བྱ། །

[Block 713]
ཡིད་ལ་བྱེད་པ་སྒྲུབ་པ་སྟེ།[^279] །དེ་ཡང་ཆོས་སྤྱོད་པ་རྣམ་པ་བཅུས་ཡོངས་སུ་གཟུང་བར་རིག་པར་བྱའོ། །

[Block 714]
ཆོས་སྤྱོད་རྣམ་པ་བཅུ་གང་ཞེ་ན།

[Block 715 [VERSE]]
ཡི་གེ་འདྲི་མཆོད་སྦྱིན་པ་དང་། །
ཉན་དང་ཀློག་དང་ལེན་པ་དང་། །
འཆད་དང་ཁ་ཏོན་བྱེད་པ་དང་། །

[Block 716]
དེ་སེམས་པ་དང་སྒོམ་པའོ།[^280] །ཐེག་པ་ཆེན་པོའི་ཡི་གེ༌[^281]འདྲི་བ་དང་། མཆོད་པ་དང་། གཞན་དག་ལ་སྦྱིན་པ་དང་། གཞན་ཀློག་པ་ལ་ཉན་པ་དང་། བདག་ཉིད་ཀློག་པ་དང་། ལེན་པ་དང་། ཚིག་དང་དོན་འཆད་པ་དང་། ཁ་ཏོན་བྱེད་པ་དང་། སེམས་པ་དང་སྒོམ་པའོ། །

[Block 717 [VERSE]]
སྤྱོད་པ་དེ་བཅུའི་བདག་ཉིད་ནི། །
བསོད་ནམས་ཕུང་པོ་དཔག་ཏུ་མེད། །

[Block 718]
ཅིའི་ཕྱིར་མདོ་དག་ལས་ཐེག་པ་ཆེན་པོ་ཉིད་ཀྱི་ཆོས་སྤྱོད་པ་ནི༌[^282]ཤིན་ཏུ་འབྲས་བུ་ཆེ་བར་བསྟན་གྱི། ཉན་ཐོས་ཀྱི་ཐེག་པ་ལ་ནི་མ་ཡིན་ཞེ་ན། རྣམ་པ་གཉིས་ཀྱི་ཕྱིར་ཏེ།

[Block 719 [VERSE]]
ཁྱད་པར་ཕྱིར་དང་མི་ཟད་ཕྱིར། །
ཁྱད་པར་ཕྱིར་ནི་ཅི་ལྟ་བུ། །

[Block 720]
མི་ཟད་པའི་ཕྱིར་ཅི་ལྟ་བུ་ཞེ་ན། གཞན་ལ་ཕན་འདོགས་མ་ཞིའི་ཕྱིར། །གཞན་ལ་ཕན་འདོགས་པར་ཞུགས་པའི་ཕྱིར་ཁྱད་པར་དུ་འཕགས་སོ། །

[Block 721]
ཡོངས་སུ་མྱ་ངན་ལས་འདས་པ་ན་ཡང་ཞི་བ་མེད་ཅིང་རྒྱུན་མི་འཆད་པའི་ཕྱིར་མི་ཟད་པར་རིག་པར་བྱའོ། །

[Block 722]
ཡིད་ལ་བྱེད་པ་བསྒྲུབ་པ་བཤད་ཟིན་ཏོ། །

[Block 723 [HEADING]]
#### རྗེས་སུ་མཐུན་པའི་ཆོས་བསྒྲུབ་པ། ^7-1-3-0

[Block 724]
རྗེས་སུ་མཐུན་པའི་ཆོས་བསྒྲུབ་པ་གང་ཞེ་ན།

[Block 725 [VERSE]]
མི་གཡེང་ཕྱིན་ཅི་མ་ལོག་པར། །
གྱུར་པ་རྗེས་སུ་མཐུན་པའི་ཆོས། །

[Block 726]
རྣམ་པ་འདི་གཉིས་ནི་རྗེས་སུ་མཐུན་པའི་ཆོས༌[^283]སྒྲུབ་པ་སྟེ། འདི་ལྟར་རྣམ་པར་མི་གཡེང་བ་དང་ཕྱིན་ཅི་མ་ལོག་པར་གྱུར་པའོ། །

[Block 727]
དེ་ལ་རྣམ་པར་མི་གཡེང་བ༌[^284]རྣམ་པ་དྲུག་མེད་པའི་ཕྱིར་མི་གཡེང་བའོ། །

[Block 728]
གཡེང་བ་རྣམ་པ་དྲུག་ནི། རང་བཞིན་གྱིས་རྣམ་པར་གཡེང་བ་དང་། ཕྱི་རོལ་ཏུ་རྣམ་པར་གཡེང་བ་དང་། ནང་གི་རྣམ་པར་གཡེང་བ་དང་། མཚན་མའི་རྣམ་པར་གཡེང་བ་དང་། གནས་ངན་ལེན་གྱི་རྣམ་པར་གཡེང་བ་དང་། ཡིད་ལ་བྱེད་པའི་རྣམ་པར་གཡེང་བའོ། །

[Block 729]
འདི་དག་གི་མཚན་ཉིད་ཅི་ལྟ་བུར་རིག་པར་བྱ་ཞེ་ན།

[Block 730 [VERSE]]
ལྡང་དང་ཡུལ་ལ་འཇུག་པ་དང་། །
དེ་བཞིན་རོ་མྱང་བྱིང་དང་རྒོད། །
ཡིད་ཆེས་པ་ཡི་བསམ་པ་དང་། །
ཡིད་ལ་བྱེད་པ་ངར་འཛིན་དང་། །

[Block 731 [VERSE]]
ཆུང་ངུའི་སེམས་ནི༌[^285]གཡེང་བ་སྟེ། །
བློ་ལྡན་རྣམས་ཀྱིས་ཤེས་པར་བྱ། །

[Block 732]
རྣམ་པར་གཡེང་བ་རྣམ་པ་དྲུག་གི་མཚན་ཉིད་ནི་དེ་ལྟ་བུ་ཡིན་ཏེ། དེ་བྱང་ཆུབ་སེམས་དཔས༌[^286]ཡོངས་སུ་ཤེས་པར་བྱའོ། །

[Block 733]
དེ་ལ༌[^287]ལྡང་བ་ནི་རྣམ་པར་ཤེས་པའི་ཚོགས་ལྔ་རྣམས་ཀྱིས་ཏིང་ངེ་འཛིན་ལས་ལྡང་བ་སྟེ། རང་བཞིན་གྱིས་རྣམ་པར་གཡེང་བའོ། །

[Block 734]
ཡུལ་ལ་འཇུག་པ་ནི་ཕྱི་རོལ་དུ་རྣམ་པར་གཡེང་བའོ། །

[Block 735]
ཏིང་ངེ་འཛིན་གྱི༌[^288]རོ་མྱང་བ་དང་། བྱིང་བ་དང་། རྒོད་པ་ནི་ནང་གི་རྣམ་པར་གཡེང་བའོ། །

[Block 736]
ཡིད་ཆེས་པའི་བསམ་པ་ནི་མཚན་མའི་རྣམ་པར་གཡེང་བ་སྟེ། དེ་མཚན་མར་བྱས་ནས་སྦྱོར་བའི་ཕྱིར་རོ། །

[Block 737]
ངར་འཛིན་པ་དང་བཅས་པའི་ཡིད་ལ་བྱེད་པ་ན༌[^289]གནས་ངན་ལེན་གྱི་རྣམ་པར་གཡེང་བ་སྟེ། གནས་ངན་ལེན་གྱི་དབང་གིས་ངའོ་སྙམ་པའི་ང་རྒྱལ་ཀུན་ཏུ་འབྱུང་བའི་ཕྱིར་རོ།[^290] །དམན་པའི་སེམས་ནི་ཡིད་ལ་བྱེད་པའི་རྣམ་པར་གཡེང་བ་སྟེ། ཐེག་པ་དམན་པ་ཡིད་ལ་བྱེད་པ་ཀུན་ཏུ་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 738]
དེ་ལ་ཕྱིན་ཅི་མ་ལོག་པའི་དངོས་པོ་ནི་རྣམ་པ་བཅུས་རིག་པར་བྱ་སྟེ། འདི་ལྟ་སྟེ།

[Block 739 [VERSE]]
ཡི་གེ་དོན་དང་ཡིད་བྱེད་དང་། །
མི་འཕྲོ་བ་དང་མཚན་ཉིད་གཉིས། །
མ་དག་དག་དང་གློ་བུར་དང་། །
མི་སྡང་བ་དང་ཁེངས་པ་མེད། །

[Block 740]
དེ་ལ།

[Block 741 [VERSE]]
འབྲེལ་པའི་ཕྱིར་དང་འདྲིས༌[^291]ཕྱིར་དང་། །
མ་འབྲེལ་ཕྱིར་དང་མ་འདྲིས༌[^292]ཕྱིར། །
དོན་ཡོད་པ་དང་མེད་པ་སྟེ། །
དེ་ནི་ཡི་གེ༌[^293]མ་ལོག་པའོ། །

[Block 742]
ཡི་གེ་རྣམས་དང་འབྲེལ་ཏེ་རྒྱུན་མི་འཆད་པར་བརྗོད་པ་དང་། འདིའི་མིང་ནི་འདི་ཞེས་བྱའོ་ཞེས་འདྲིས་པས་དོན་ཡོད་པ་ཉིད་དོ། །

[Block 743]
བཟློག་པ་ནི་དོན་མེད་པ་ཉིད་དོ་ཞེས་དེ་ལྟར་མཐོང་བ་གང་ཡིན་པ་དེ་ནི་ཡི་གེ་ལ་ཕྱིན་ཅི་མ་ལོག་པར་རིག་པར་བྱའོ། །

[Block 744]
དོན་ལ་ཕྱིན་ཅི་མ་ལོག་པ་ཇི་ལྟ་བུ་ཞེ་ན།

[Block 745 [VERSE]]
གཉིས་སུ་སྣང་བར་གྱུར་པ་ནི། །
དེ་ལྟར་ཡོད་པ་མ༌[^294]ཡིན་ཏེ། །
དེ་ནི་དོན་ལ་མ་ལོག་པ། །
ཡོད་དང་མེད་པ་རྣམ་པར་སྤངས། །

[Block 746]
གཉིས་ནི་གཟུང་བ་དང་འཛིན་པར་སྣང་བ་སྟེ་དེའི་རྣམ་པར་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 747]
ཇི་ལྟར་སྣང་བ་དེ་ལྟར་ནི་ཡོད་པ་མ་ཡིན་ཏེ། དེ་ལྟར་དོན་ལ་མཐོང་བ་གང་ཡིན་པ་དེ་ནི་དེ་ལ་ཕྱིན་ཅི་མ་ལོག་པའོ། །

[Block 748]
དོན་གྱི་ཡོད་པ་སྤངས་པ་ནི་གཟུང་བ་དང་འཛིན་པ་དངོས་པོ་མེད་པའི་ཕྱིར་རོ། །

[Block 749]
མེད་པ་སྤངས་པ་ནི་དེར་སྣང་བའི་འཁྲུལ་པ་ཡོད་པའི་ཕྱིར་རོ། །

[Block 750]
[^295]རྟོག་པ་དེ་ཡིས་བསྒོས་པ་ཡི།[^296] །

[Block 751 [VERSE]]
རྟོག་པ་ཡིད་བྱེད་དེའི་གནས་ནི། །
ཡིད་ལ་བྱེད་པ་མ་ལོག་པ། །
གཉིས་སུ་སྣང་བའི་རྒྱུ་ལའོ། །

[Block 752]
གཟུང་བ་དང་འཛིན་པར་རྟོག་པས་ཡོངས་སུ་བསྒོས་པ་ནི་རྟོག་པའི་ཡིད་ལ་བྱེད་པ་སྟེ། གཟུང་བ་དང་འཛིན་པ་རྣམ་པར་རྟོག་པ་དེའི་རྟེན་ཡིན་པས། འདི་ནི་ཡིད་ལ་བྱེད་པ་ལ་ཕྱིན་ཅི་མ་ལོག་པའོ། །

[Block 753]
ཡིད་ལ་བྱེད་པ་གང་ལ་ཕྱིན་ཅི་མ་ལོག་ཅེ་ན། གཟུང་བ་དང་འཛིན་པ་གཉིས་སུ་སྣང་བའི་རྒྱུ་ལ་སྟེ། རྟོག་པ་ཡིད་ལ་བྱེད་པ་དེ་ནི་བརྗོད་པའི་འདུ་ཤེས་ཀྱིས་ཡོངས་སུ་བསྒོས་པའི་ཕྱིར་རོ། །

[Block 754 [VERSE]]
དོན་གྱི༌[^297]མེད་དང་ཡོད་པ་སྟེ། །
སྒྱུ་མ་ལ་སོགས་བཞིན་དུ་འདོད། །
དེ་ནི་མི་འཕྲོ་མ་ལོག་སྟེ། །
ཡོད་དང་མེད་པ༌[^298]མི་འཕྲོའི་ཕྱིར། །

[Block 755]
དོན་གྱི་མེད་པ་དང་ཡོད་པ་གོང་དུ་བཤད་མ་ཐག་པ༌[^299]གང་ཡིན་པ་དེ་ནི་སྒྱུ་མ་ལ་སོགས་པ་བཞིན་དུ་འདོད་དེ། དཔེར་ན་སྒྱུ་མའི་གླང་པོ་ཆེ་ལ་སོགས་པའི་དངོས་པོར་ཡོད་པ་ཡང་མ་ཡིན་ལ། དེའི་འཁྲུལ་པ་ཙམ་དུ་ཡོད་པའི་ཕྱིར་མེད་པ་ཡང་མ་ཡིན་ནོ། །
--- END BLOCKS ---
