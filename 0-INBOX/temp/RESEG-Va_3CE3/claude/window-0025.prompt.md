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
[Block 876]
གཟུགས་ཀྱང་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་མ་ཡིན་ཞེས་བྱ་བ་ནི་གཟུགས་དང་། ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་གཉིས་ཀ་ཡང་ཡོད་པ་མ་ཡིན་པར་བསྟན་པའོ། །

[Block 877]
གཟུགས་ལས་གུད་ན་ཡང་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་ཡོད་པ་མ་ཡིན་པ་ཉིད་ཀྱི་ཕྱིར་ཐ་དད་པར་བརྗོད་དུ་མི་རུང་ངོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 878]
དེ་བས་ན། ཀཽ་ཤི་ཀ་འདི་ལྟར་ཆོས་འདི་དག་ཐམས་ཅད་ནི་ཡོད་པ་མ་ཡིན་ཏེ་དམིགས་སུ་མེད་དོ་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 879]
དེ་ནས་ཡང་ཆོས་བཤད་པ་འདི་ངོ་མཚར་དུ་གཟུང་བར༌[^598]བསྟན་པའི་ཕྱིར་བརྒྱ་བྱིན་གྱིས༌[^599]ཚིག་རྣམ་པ་བཞི་བཀོད་དེ། ཕ་རོལ་ཏུ་ཕྱིན་པ་འདི་ནི་ཆེ་བ་སྟེ་ཞེས་བྱ་བ་དང་། ཕ་རོལ་ཏུ་ཕྱིན་པ་འདི་ནི་ཚད་མེད་པ་སྟེ་ཞེས་བྱ་བ་དང་། ཕ་རོལ་ཏུ་ཕྱིན་པ་འདི་ནི་དཔག་ཏུ་མེད་པ་སྟེ་ཞེས་བྱ་བ་དང་། ཕ་རོལ་ཏུ་ཕྱིན་པ་འདི་ནི་མཐའ་ཡས་པ་སྟེ་ཞེས་བྱ་བའོ།

[Block 880]
[^600] །གཟུགས་ཀྱི་སྔོན་གྱི་མཐའ་མི་དམིགས་ཞེས་བྱ་བ་ནི་དེའི་ཚེ་བྱུང་ངོ་ཞེས་བྱ་བའམ་མ་བྱུང་ངོ་ཞེས་བྱ་བར་སྦྱར༌[^601]རོ། །

[Block 881]
ཕྱི་མའི་མཐའ་མི་དམིགས་ཞེས་བྱ་བ་ནི་དེའི་ཚེ་འབྱུང་བར་འགྱུར་རོ་ཞེས་བྱ་བའམ། འབྱུང་བར་མི་འགྱུར་རོ་ཞེས་བྱ་བར་རོ། །

[Block 882]
དབུས་མི་དམིགས་ཞེས་བྱ་བ་ནི་ཡོད་དོ་ཞེས་བྱ་བའམ། མེད་དོ་ཞེས་བྱ་བར་མི་དམིགས་པ་སྟེ། དེ་ལྟར་དུས་གསུམ་དུ་དབྱེར༌[^602]མེད་པས་ཆེ་བའོ། །

[Block 883]
གཟུགས་ཀྱི་ཚད་ནི་དམིགས་སུ་མེད་དོ་ཞེས་བྱ་བ་ནི་དོན་དམ་པའི་གཟུགས་ལ་འདི་ཙམ་མོ་ཞེས་ཡོངས་སུ་བཅད་པ་མེད་པའི་ཕྱིར་ཚད་མེད་པ་ཉིད་དོ། །

[Block 884]
གྲངས་ཀྱིས་དཔག་ཏུ་མེད་པའི་ཕྱིར་དཔག་ཏུ་མེད་པའོ། །

[Block 885]
སྐད་ཅིག་ཡོངས་སུ་ཆད་པ་མེད་པའི་ཕྱིར་མཐའ་ཡས་པའོ། །

[Block 886]
སྔོན་གྱི་མཐའ༌[^603]ཞེས་བྱ་བ་ནི་སྐྱེ༌[^604]བའི་མཐའོ། །

[Block 887]
ཕྱི་མའི་མཐའ་ཞེས་བྱ་བ་ནི་འགག་པའི་མཐའོ། །

[Block 888]
དབུས་ཞེས་བྱ་བ་ནི་སྐད་ཅིག་པའི་གནས་སོ། །

[Block 889]
དེ་ལྟར་ཕ་རོལ་ཏུ་ཕྱིན་པ་མཐའ་ཡས་པ་གཅིག་གིས་བསྟན་ནས། དེའི་འོག་ཏུ་མཐའ་ཡས་པ་རྣམ་པ་བཞིས་སྟོན་ཏེ། རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་མཐའ་ཡས་པ་དང་། ཆོས་ཀྱི་སྐུ་མཐའ་ཡས་པ་དང་། དེ་བཞིན་ཉིད་མཐའ་ཡས་པ་དང་། སེམས་ཅན་མཐའ་ཡས་པའོ། །

[Block 890]
དེ་ལ་སེམས་ཅན་མཐའ་ཡས་པ་ཞེས་བྱ་བ་གང་ཡིན་ཞེ་ན། དེ་མཐའ་ཞེས་བྱ་བ་ནི་མཐའ་གཉིས་ཏེ། རྟག་པའི་མཐའ་དང་ཆད་པའི་མཐའོ། །

[Block 891]
མཐའ་དེ་གཉིས་མེད་པ་ནི་མཐའ་ཡས་པ་ཉིད་དེ་སེམས་ཅན་གྱི་མཐའ་མེད་པ་ནི༌[^605]སེམས་ཅན་མཐའ་ཡས་པའོ། །

[Block 892]
གལ་ཏེ་སེམས་ཅན་ཡོད་ན་ནི་དེ་ལྟར་གྱུར་ན་མཐའ་དང་ལྡན་པར་འགྱུར་བ་ཞིག་ན་འདི་ལྟར་སེམས་ཅན་ངོ་བོ་ཉིད་ཀྱིས་མེད་པ་ཁོ་ན་སྟེ། དེའི་ཕྱིར་ངོ་བོ་ཉིད་ཀྱི་སེམས་ཅན་མཐའ་ཡས་པ༌[^606]ཡོད་པ་མ་ཡིན་ནོ། །

[Block 893]
སེམས་ཅན་མཐའ་ཡས་པ་དེ་ཡང་ཆོས་བཤད་པ་འདི་ལ་ཡོད་པ༌[^607]མ་ཡིན་ནོ། །

[Block 894]
གལ་ཏེ་ཆོས་བཤད་པ་འདི་ལ་སེམས་ཅན་འགའ་ཞིག་བསྟན་ན༌[^608]ནི་དེ་ལྟར་གྱུར་ན་སེམས་ཅན་མཐའ་ཡས་པ་ཡང་བསྟན་པར་འགྱུར་བ་ཞིག་ན། འདི་ལྟར་སེམས་ཅན་མ་བསྟན་པས༌[^609]དེའི་ཕྱིར་འདི་ལ་སེམས་ཅན་མཐའ་ཡས་པ་ཡང་མེད་དོ། །

[Block 895]
དེ་བས་ན་ཀཽ་ཤི་ཀ་གང་ལ་སེམས་ཅན་དུ་བཤད་པ་གང་ཡང་མེད་པ་དེ་སེམས་ཅན་མཐའ་ཡས་པ་གང་ཡང་མེད་དེ་ཞེས་བྱ་བ་གསུངས་ཏེ། སེམས་ཅན་མ་བསྟན་པའི་ཕྱིར་སེམས་ཅན་མཐའ་ཡས་པ་ཡང་མ་བསྟན་ཏོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 896]
དེའི་འོག་ཏུ་ཀཽ་ཤི་ཀ་གལ་ཏེ་དེ་བཞིན་གཤེགས་པ་དགྲ་བཅོམ་པ་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་བསྐལ་པ་གང་གཱའི་ཀླུང་གི་བྱེ་མ་སྙེད་དུ་བཞུགས་ཏེ། སེམས་ཅན་སེམས་ཅན་ཞེས་གསུང་དུ་བརྗོད་ན་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་སེམས་ཅན་མཐའ་ཡས་པ་ཚིག་གི་ཁ་ན་ལས་པ་མ་ཡིན་གྱི། སེམས་ཅན་མེད་པ་ཉིད་ཀྱི་ཕྱིར་ངོ་བོ་ཉིད་ཀྱིས་མཐའ་ཡས་པའོ་ཞེས་སྟོན་ཏོ། །

[Block 897]
གལ་ཏེ་སེམས་ཅན་མཐའ་ཡས་པ་ཚིག་གི་ཁར་ལས་པ་ཞིག་ཡིན་ན་ནི་དེ་བཞིན་གཤེགས་པའི་གསུང༌[^610]ལས་སེམས་ཅན་སྐྱེ་བའམ། འགག་པར་འགྱུར་བ་ཞིག་ན། འདི་ལྟར་དེ་ལྟར་ཡང་མ་གྱུར་ཏེ་དེའི་ཕྱིར་སེམས་ཅན་མཐའ་ཡས་པ་ཚིག་ལས་གྱུར་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 898]
ཀཽ་ཤི་ཀ་རྣམ་གྲངས་དེས་ན་སེམས་ཅན་མཐའ་ཡས་པའི་ཕྱིར་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་མཐའ་ཡས་པར་རིག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་བཤད་པ་འདི་ལ་སེམས་ཅན་ཞིག་བསྟན་ན་ནི་དེ་ན་དེ་ཡོད་པའི་ཕྱིར་མཐའ་གཉིས་ཀྱང་ཡོད་པར་འགྱུར་ན་དེ་གཉིས་ཀྱང་མ་བསྟན་པས་ཕ་རོལ་ཏུ་ཕྱིན་པ་འདི་མཐའ་ཡས་པར་འགྱུར་རོ། །

[Block 899]
གང་གི་ཕྱིར་སེམས་ཅན་མ་བསྟན་པ་དེའི་ཕྱིར་སེམས་ཅན་མེད་དོ། །

[Block 900]
དེ་མེད་པས་མཐའ་གཉིས་ཀྱང་མེད་དོ། །

[Block 901]
དེ་བས་ན་སེམས་ཅན་མ་བསྟན་པའི་ཕྱིར་ཕ་རོལ་ཏུ་ཕྱིན་པ་འདི་མཐའ་ཡས་པ་ཞེས་བྱའོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 902]
ཆོས་གང་ལ༌[^611]ཡང་དམིགས་སུ་མ་མཆིས་ཀྱང་། ཐེག་པ་གསུམ་རྣམ་པར་དགོད་པ་ཡང་མཆིས་ཏེ་ཞེས་བྱ་བ་ནི་དོན་དམ་པ་དང༌[^612]ཀུན་རྫོབ་ཏུའོ། །

[Block 903]
སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལས་གུད་ན་ཡང་དེ་བཞིན་གཤེགས་པ་དམིགས་སུ་མེད་ཅེས་བྱ་བ་ནི་ཆོས་ཀྱི་སྐུའི་དེ་བཞིན་གཤེགས་པ་ནི༌[^613]སངས་རྒྱས་ཀྱི་ཆོས་ཀྱི་ངོ་བོ་ཉིད་དོ། །

[Block 904]
བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱང་དེ་ལ་སློབ་པ་ནི་དོན་དམ་པར་སངས་རྒྱས་ཀྱི་ཆོས་ཀྱི་ངོ་བོ་ཉིད་ཡིན་པས་དེའི་ཕྱིར་བྱང་ཆུབ་སེམས་དཔའ་དང་དེ་བཞིན་གཤེགས་པ་ལ་བྱེ་བྲག་མེད་པས་དེ་བཞིན་གཤེགས་པ་ཉིད་དོ་ཞེས་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 905]
བྱང་ཆུབ་སེམས་དཔའ་སངས་རྒྱས་ཀྱི་ཆོས་རྣམས་ལ་གསར་དུ་སློབ་པ་རྣམས་སངས་རྒྱས་ཀྱི་ཆོས་ཀྱི་ངོ་བོ་ཉིད་ཡིན་པས་བསྟན་པའི་ཕྱིར་དེ་བཞིན་གཤེགས་པ་མར་མེ་མཛད་ཀྱིས་ཀྱང་སངས་རྒྱས་ཀྱི་ཆོས་དང་མ་བྲལ་བར་གཟིགས༌[^614]ནས། དེ་བཞིན་གཤེགས་པར༌[^615]ལུང་བསྟན་ཏོ་ཞེས་མར་མེ་མཛད་ཀྱི་དཔེ་བསྟན་ཏོ། །

[Block 906]
དེ་ནས་ལྷའི་བུ་དེ་དག་གིས་བཅོམ་ལྡན་འདས་ལ་འདི་སྐད་ཅེས་གསོལ་ཏོ་ཞེས་བྱ་བ་ནི་མར་མེ་མཛད་ཀྱིས་ལུང་བསྟན་པ་ཐོབ་པས། བཅོམ་ལྡན་འདས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་རྣམས་ཀྱི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་འདི་གཟུགས་མི་ལེན་མི་འདོར་བའི་ཚུལ་དང་ཞེས་བྱ་བ་ནས་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་དང༌[^616]མཐུན་པར་ཡོངས་སུ་འཛིན་པ་ནི་ངོ་མཚར་ཏོ་ཞེས་བྱ་བ་སྨྲས་ཏེ། གཟུགས་ལ་སོགས་པའི་ཆོས་རྣམས་ལ་ཁྱད་པར་དུ་འཕགས་པ་དང་། ངན་པའི་དངོས་པོ་མེད་པའི་ཕྱིར་ལེན་པ་དང་འདོར་བ་གཉིས་ཀྱང་མེད་དོ། །

[Block 907]
འོན་ཀྱང་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་སྔོན་མ་བྱུང་བ་ཡོངས་སུ་འཛིན་པ་དེ་ངོ་མཚར་ཏོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 908]
དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་འཁོར་བཞི་པོ༌[^617]དགེ་སློང་དང་དགེ་སློང་མ་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་བཤད་པར་བྱ་བའི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལས་བརྩམས་པའོ། །

[Block 909 [HEADING]]
#### ཡོན་ཏན་གྱི་ཕན་ཡོན། ^1-2-2-0

[Block 910]
འདི་མན་ཆད་ནི་དོན་གྱི་བདག་ཉིད་ཀྱི་ཆོས་བཤད་པ་འདིའི་ཡོན་ཏན་གྱི་ཕན་ཡོན་ཚེ་འདི་དང་ཚེ་ཕྱི་མ་ལ་འབྱུང་བ་དང་། བསོད་ནམས་མང་པོ་འཕེལ་བའི་རྒྱུར་གྱུར་པ་སྟོན་ཏོ། །

[Block 911]
སྟོང་པ་ཉིད་ཤིན་ཏུ་བྱིན་གྱིས་བརླབས་པར་འགྱུར་རོ་ཞེས་བྱ་བ་ནི་སྟོང་པ་ཉིད་ཀྱི་བྱིན་གྱི་རླབས་ཀྱིས༌[^618]རྒྱུ་མཐུན་པ་ཉིད་སྟོན་ཏེ།[^619] དེ་ལ་འཇིག་རྟེན་པ་ཐམས་ཅད་སྟོང་པར་སྣང་ལ།[^620] བདག་ཀྱང་སྟོང་པར་སྣང་ངོ་། །འདིར་ཇི་ལྟར་ན་སྟོང་པ་ཉིད་ཀྱིས༌[^621]སྟོང་པ་ཉིད་ལ་གླགས་རྙེད་པར་མི་འགྱུར་བ་སྟོན་ཏོ། །

[Block 912]
[^622]གང་གིས་གླགས་རྙེད་པར་འགྱུར་བ་ཞེས་བྱ་བ་ནི་སྡིག་པའི་ལས་ཀྱིས་སོ། །

[Block 913]
གང་དུ་གླགས་རྙེད་པར་འགྱུར་བ་ཞེས་བྱ༌[^623]བ་ནི་སའི་སྟེང་ངམ། ལྷ་ཡུལ་དུའོ། །

[Block 914]
གང་ལ་གླགས་རྙེད་པར་འགྱུར་བ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའ་ལ༌[^624]སྟེ། འདི་ལྟར་དེ་དག་ཐམས་ཅད་མེད་པའི་ཕྱིར་རོ། །

[Block 915]
འདིར་ནི་གཞུང་བརྡ་ཕྲད་སླ་བས་མ་བྲིས་སོ། །
--- END BLOCKS ---
