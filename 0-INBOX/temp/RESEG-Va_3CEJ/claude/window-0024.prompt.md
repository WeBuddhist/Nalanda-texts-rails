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
[Block 841]
ཡང་ལུས་དག་ལ༌[^365]གནས་ཏེ་མིག་གིས༌[^366]གཟུགས་རྣམས་ལ༌[^367]ལྟ་བ་ནས།[^368] ཅི་ལུས་དང་མིག་དང་གཟུགས་དང་རྣམ་པར་ཤེས་པ་དེ་རྣམས༌[^369]གཅིག་པ་ཁོ་ན་ཞིག་ཡིན་ནམ། འོན་ཏེ་གཞན་གྱི་ས་པ་ཡང་ཡིན་ཞེ་ན། སྨྲས་པ། ཐམས་ཅད་ལ་བྱེ་བྲག་ཡོད་དེ། འདོད་པའི་ཁམས་སུ་སྐྱེས་པ་རང་གི་མིག་གིས་རང་གི་གཟུགས་རྣམས་ལ་ལྟ་བ་ནི༌[^370]ཐམས་ཅད་རང་གི་ས་པ་ཡིན་ནོ། །

[Block 842]
དེ་ཉིད་རང་གི་གཟུགས་རྣམས་ལ་བསམ་གཏན་དང་པོའི་མིག་གིས་ལྟ་བ་ན་ལུས་དང་གཟུགས་དག་ནི་རང་གི་ས་པ་ཡིན་ལ། རྣམ་པར་ཤེས་པ་དང་མིག་དག་ནི་དེའི་ས་པ་ཡིན་ནོ། །

[Block 843]
བསམ་གཏན་དང་པོའི་ས་པ་དག་ལ་ལྟ་ན་ནི་གཟུགས་རྣམས་ཀྱང་དེའི་ས་པ་ཡིན་ནོ། །

[Block 844]
རང་གི་གཟུགས་རྣམས་ཀྱང༌[^371]བསམ་གཏན་གཉིས་པའི་མིག་གིས་ལྟ་བ་ན་ལུས་དང་གཟུགས་དག་ནི་རང་གི་ས་པ་ཡིན་ལ། མིག་ནི་དེའི་ས་པ་ཡིན་ནོ། །

[Block 845]
མིག་གི་རྣམ་པར་ཤེས་པའི་ས༌[^372]ནི་བསམ་གཏན་དང་པོའི་ས་པ་ཡིན་ནོ། །

[Block 846]
བསམ་གཏན་དང་པོའི་ས་པ་དག་ལ་ལྟ་བ་ན་རྣམ་པར་ཤེས་པ་དང་གཟུགས་དག་ནི་དེའི་ས་པ་ཡིན་ལ། ལུས་ནི་འདོད་པ་ན་སྤྱོད་པ་ཡིན་ནོ། །

[Block 847]
མིག་ནི་བསམ་གཏན་གཉིས་པའི་ས་པ་ཡིན་ནོ། །

[Block 848]
བསམ་གཏན་གཉིས་པའི་ས་པ་དག་ལ་ལྟ་བ་ན༌[^373]མིག་དང་གཟུགས་དག་ནི་དེའི་ས་པ་ཡིན་ལ།[^374] ལུས་ནི་འདོད་པ་ན་སྤྱོད་པ་ཡིན་ནོ། །

[Block 849]
རྣམ་པར་ཤེས་པ་ནི་བསམ་གཏན་དང་པོའི་ས་པ་ཡིན་ཏེ། དེ་ལྟར་བསམ༌[^375]གཏན་གསུམ་པ་དང་། བསམ་གཏན་བཞི་པའི་ས་པའི་མིག་གིས་དེ་དག་གི་ས་པ་དང་། ས་འོག་མ་པའི་གཟུགས་རྣམས༌[^376]ལ་ལྟ་བ་ཡང་དེ་བཞིན་དུ་སྦྱར་བར་བྱའོ། །

[Block 850]
བསམ་གཏན་དང་པོའི་སྐྱེས་པ་རང་གི་མིག་གིས་རང་གི་གཟུགས་རྣམས་ལ་ལྟ་བ་ན་ཐམས་ཅད་རང་གི་ས་པ་ཡིན་ནོ། །

[Block 851]
འོག་མ་རྣམས་ལ་ལྟ་བ༌[^377]ནི་གསུམ་རང་གི་ས་པ་ཡིན་ནོ། །

[Block 852]
རང་གི་གཟུགས་རྣམས་ལ་བསམ་གཏན་གཉིས་པའི་མིག་གིས༌[^378]ལྟ་བ་ན་གསུམ་ནི་རང་གི་ས་པ་ཡིན་ལ། མིག་ནི་དེའི་ས་པ་ཡིན་ནོ། །

[Block 853]
འདོད་པ་ན་སྤྱོད་པ་རྣམས་ལ་ལྟ་བ་ན་ལུས་དང་རྣམ་པར་ཤེས་པ་དག་ནི་རང་གི་ས་པ་ཡིན་ལ། གཟུགས་རྣམས་ནི་འོག་མ་པ་ཡིན་ནོ། །

[Block 854]
མིག་ནི་དེའི་ས་པ་ཡིན་ནོ། །

[Block 855]
བསམ་གཏན་གཉིས་པ་རྣམས་ལ་ལྟ་བ་ན་མིག་དང་གཟུགས་ནི་དེའི་ས་པ་ཡིན་ལ། ལྷག་མ་ནི་རང་གི་ས་པ་ཡིན་ཏེ། བསམ་གཏན་གསུམ་པ་ལ་སོགས་པའི་མིག་གིས་ལྟ་བའི་ཡང་དེ་བཞིན་དུ་སྦྱར་རོ། །

[Block 856]
བསམ་གཏན་གཉིས་པ་ལ་སོགས་པར་སྐྱེས་པ་རང་དང་གཞན་གྱི་མིག་དག་གིས་རང་དང་གཞན་གྱི་ས་པའི་གཟུགས་རྣམས་ལ་ལྟ་བ་ལ་ཡང་ཅི་རིགས་པར་སྦྱར་བར་བྱའོ། །

[Block 857]
འདི་ནི་ངེས་པ་ཡིན་ཏེ། ལུས་ལ་འོག་མའི་མིག་མ་ཡིན། །ལུས་དང་མིག་དང་གཟུགས་རྣམས་ནི་འདོད་པ་ན་སྤྱོད་པ་ནས་བསམ་གཏན་བཞི་པའི་བར་ས་ལྔ་པ་ཡིན་ནོ། །

[Block 858]
མིག་གི་རྣམ་པར་ཤེས་པ་ནི་འདོད་པ་ན་སྤྱོད་པ་དང་། བསམ་གཏན་དང་པོའི་ས་པ་དང་། ས་གཉིས་པ་ཡིན་ནོ། །

[Block 859]
དེ་ལ་ས་གང་བའི་ལུས་ཡིན་པ་ས་དེ་པ་འམ། ས་གོང་མ་པའི་མིག༌[^379]ཡིན་གྱི་ས་འོག་མ་པ་ནི་མ་ཡིན་ནོ། །

[Block 860]
འདིའི་མིག་གི་ཡུལ་ནི་དེའི་ས་པ་འམ། ས་འོག་མ་པའི་གཟུགས་ཡིན་གྱི། མིག་གི་གོང་མའི་གཟུགས་མ་ཡིན། །ས་གོང་མ་པའི་གཟུགས་ས་འོག་མ་པའི་མིག་གིས་མཐོང་བར་ནི་ནམ་ཡང་མི་ནུས་སོ། །

[Block 861]
རྣམ་པར་ཤེས་པའང་། གོང་མ་ནི་མིག་གི་མ་ཡིན་ཏེ། གཟུགས་བཞིན་ནོ། །

[Block 862]
དེ་ཡི་གཟུགས། ལུས་ཀྱིའང་གཉི་ག་ཐམས་ཅད་དུ། །དེའི་ཞེས་བྱ་བ་བཤད་མ་ཐག་པའི་མིག་གི་རྣམ་པར་ཤེས་པའི་ཡུལ་ནི་གོང་མ་དང་འོག་མ་དང་རང་གི་ས་པའི་གཟུགས་ཐམས་ཅད་དུ་ཡིན་ལ། ལུས་ཀྱིའང་གཟུགས་དང་། རྣམ་པར་ཤེས་པ་དག་ཐམས་ཅད་དུ་ཡིན་ནོ། །

[Block 863]
ཇི་ལྟར་མིག་འདི་རྒྱས་པར་བཤད་པ་ལྟར། རྣ་བའང་དེ་བཞིན་དུ་རིག་པར་བྱ་སྟེ།

[Block 864 [VERSE]]
ལུས་ལ་འོག་མའི་རྣ་བ༌[^380]ཡིན། །
རྣ་བའི་གོང་མའི་སྒྲ་མ་ཡིན། །
རྣམ་པར་ཤེས་པའང་དེའི་སྒྲ། །

[Block 865]
ལུས་ཀྱིའང་གཉི་ག་ཐམས་ཅད་དུ་ཞེས་རྒྱས་པར་སྦྱར་བར་བྱའོ། །

[Block 866]
གསུམ་དག་ནི། ཐམས་ཅད་རང་གི་ས་པ་ཉིད། །སྣ་དང་ལྕེ་དང་ལུས་ཀྱི་ཁམས་རྣམས་ཀྱི་ལུས་དང་རང་གི་ཡུལ་དང་རྣམ་པར་ཤེས་པ་རྣམས་རང་གི་ས་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 867]
དེ་ལྟར་བྱེ་བྲག་ཏུ་མ་ཕྱེ་བར་སྤྱིར་བསྟན་ནས། ཡང་བྱེ་བྲག་ཏུ་དབྱེ་བའི་ཕྱིར་དམིགས་ཀྱིས་བསལ་བ་རྩོམ་སྟེ། ལུས་ཀྱི་རྣམ་ཤེས་འོག་དང་ནི། །རང་གི་ས། ལུས་དང་ལུས་ཀྱི་ཁམས་དང་རེག་བྱ་ནི་རྟག་ཏུ་རང་གི་ས་པ་དག་ཁོ་ན་ཡིན་ནོ། །

[Block 868]
ལུས་ཀྱི་རྣམ་པར་ཤེས་པ་ནི་ཁ་ཅིག་གི་ནི་རང་གི་ས་པ་ཡིན་ཏེ། འདི་ལྟ་སྟེ་འདོད་པའི་ཁམས་དང་བསམ་གཏན་དང་པོར་སྐྱེས་པ་རྣམས་ཀྱི་ལྟ་བུའོ། །

[Block 869]
ཁ་ཅིག་གི༌[^381]ནི་ས་འོག་མ༌[^382]ཡིན་པས༌[^383]ཏེ། འདི་ལྟ་སྟེ། བསམ་གཏན་གཉིས་པ་ལ་སོགས་པར་སྐྱེས་པ་རྣམས་ཀྱི་ལྟ་བུའོ། །

[Block 870]
ཡིད་མ་ངེས་ཏེ། རེས་འགའ་ནི་ལུས་དང་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་དང་ཆོས་དག་དང་མཚུངས་པའི་ས་པའི་ཡིད་ཡིན་ལ། རེས་འགའ་ནི་ས་གོང་མ་དང་འོག་མ་པ་ཡིན་ཏེ། དེ་ཉིད་ཀྱི་ཕྱིར་ས༌[^384]ལྔ་པའི་ལུས་ལ་ཡང་སྙོམས་པར་འཇུག་པ་དང་། སྐྱེ་བའི་ཚེ་ཡིད་ལ་སོགས་པ་ཅི་རིགས་པར་ས་ཐམས་ཅད་པ་དག་ཡིན་ཏེ། འདི་རྒྱས་པར་ནི་སྙོམས་པར་འཇུག་པ་བསྟན་པའི་མཛོད་ཀྱི་གནས་ནས་འཆད་པར་འགྱུར་རོ། །

[Block 871]
ཚིག་གི་ཁུར་ཧ་ཅང་མངས་པ་ཡོངས་སུ་སྤང་བའི་ཕྱིར་ད་ནི་མི༌[^385]བཤད་དེ། དགོས་པ་ཆུང་ལ་ངལ་བ་ཆེ་བའི་ཕྱིར་རོ། །

[Block 872]
ཞར་ལ་འོངས་པའི་སྐབས་རྫོགས་སོ།། །།

[Block 873 [HEADING]]
#### རྣམ་པར་ཤེས་པ་གང་དག་གིས་རྣམ་པར་ཤེས་པར་བྱ་བ། ^1-3-20-0

[Block 874]
ད་ནི་འདི་དཔྱད་པར་བྱ་སྟེ། ཁམས་བཅྭ་བརྒྱད༌[^386]དང་། རྣམ་པར་ཤེས་པ་དྲུག་པོ་རྣམས་ལ་གང་ཞིག་རྣམ་པར་ཤེས་པ་གང་དག་གིས་རྣམ་པར་ཤེས་པར་བྱ་བ་ཡིན་ཞེ་ན། སྨྲས་པ། གཉིས་ཀྱིས་རྣམ་པར༌[^387]ཤེས་ཕྱིར་ལྔ།[^388] །གཟུགས་དང་སྒྲ་དང་དྲི་དང་རོ་དང་རེག་བྱ་རྣམས་ནི་གྲངས་བཞིན་དུ་མིག་དང་རྣ་བ་དང་སྣ་དང་ལྕེ་དང་ལུས་ཀྱི་རྣམ་པར་ཤེས་པ་དག་གིས༌[^389]ཉམས་སུ་མྱོང་ནས་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པས་རྣམ་པར་ཤེས་ཏེ། དེ་ལྟར་ན་དེ་དག་ནི་རེ་རེ་ཞིང་རྣམ་པར་ཤེས་པ་གཉིས་ཀྱིས༌[^390]རྣམ་པར་ཤེས་པར་བྱ་བ་ཡིན་ནོ། །

[Block 875]
ཁམས་ལྷག་མ་བཅུ་གསུམ་ནི་རྣམ་པར་ཤེས་པའི་ཚོགས་ལྔའི་ཡུལ་མ་ཡིན་པའི་ཕྱིར་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་གཅིག་པུས་རྣམ་པར་ཤེས་པར་བྱ་བ་ཡིན་ནོ༌[^391]ཞེས་རྣམ་པར་བཤད་པར་འགྱུར་རོ། །

[Block 876 [HEADING]]
#### རྟག་པ་དང་མི་རྟག་པ། ^1-3-21-0

[Block 877]
རྟག་པ་རྣམས་ནི་དུ། མི་རྟག་པ་རྣམས་ནི་དུ་ཞེ་ན། ཁམས་གཅིག་རིལ་པོར་རྟག་པ་ནི་མེད་མོད་ཀྱི། འོན་ཀྱང་། འདུས་མ་བྱས་ཆོས་རྟག་པའོ། །

[Block 878]
དེས་ན་ཆོས་ཀྱི་ཁམས་ཀྱི་ཕྱོགས་གཅིག་རྟག་ལ། ལྷག་མ༌[^392]རྣམས་ནི་མི་རྟག་པ་ཡིན་ནོ། །

[Block 879 [HEADING]]
#### དབང་པོ་དང་དབང་པོ་མ་ཡིན་པ། ^1-3-22-0

[Block 880]
དབང་པོ་རྣམས་ནི་དུ། དབང་པོ་མ་ཡིན་པ་རྣམས་ནི་དུ་ཞེ་ན།
--- END BLOCKS ---
