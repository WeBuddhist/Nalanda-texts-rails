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
[Block 2766 [VERSE]]
ཉེ་བར་ལེན་པ་མ་གཏོགས་པའི། །
བདག་ཡོད་མ་ཡིན་བྱས་པའི་ཚེ། །
ཉེ་བར་ལེན་ཉིད་བདག་ཡིན་ན། །
ཁྱོད་ཀྱི་བདག་ནི་མེད་པ་ཡིན། །

[Block 2767 [VERSE]]
ཉེ་བར་ལེན་ཉིད་བདག་མ་ཡིན། །
དེ་ནི་འབྱུང་དང་འཇིག་པ་ཡིན། །
ཉེ་བར་བླང་བ་ཇི་ལྟ་བུར། །
ཉེ་བར་ལེན་པོ༌[^1758]ཡིན་པར་འགྱུར། །

[Block 2768 [VERSE]]
བདག་ནི་ཉེ་བར་ལེན་པ་ལས། །
གཞན་དུ་འཐད་པ་ཉིད་མ་ཡིན། །
གལ་ཏེ་གཞན་ན་ལེན་མེད་པར། །
གཟུང་ཡོད་རིགས་ན་གཟུང་དུ་མེད། །

[Block 2769 [VERSE]]
དེ་ལྟར་ལེན་ནས༌[^1759]གཞན་མ་ཡིན། །
དེ་ནི་ཉེར་ལེན་ཉིད་ཀྱང་མིན། །
བདག་ནི་ཉེ་བར་ལེན་མེད་མིན། །
མེད་པ་ཉིད་དུའང་དེ་མ་ངེས། །

[Block 2770]
བདག་སྔོན་འདས་པའི་དུས་ན་བྱུང་བར་གྱུར་ཅེས་བྱ་བ་དེ་ནི་མི་འཐད་དོ། །ཅིའི་ཕྱིར་ཞེ་ན། སྔོན་གྱི་ཚེ་རབས་སུ་གང་བྱུང་བར་གྱུར་པ་དེ་ཉིད་ད་ལྟར༌[^1760]གྱི་བདག་འདི་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2771]
དེ་ལ་འདི་སྙམ་དུ་གལ་ཏེ་སྔོན་གྱི་ཚེ་རབས་རྣམས་སུ་གང་བྱུང་བར་གྱུར་པ་དེ་ཉིད་ད་ལྟར་གྱི་བདག་འདི་ཡིན་པར་གྱུར་ན་དེའི་ཕྱིར་སྐྱོན་ཅིར་འགྱུར་སྙམ་དུ་སེམས་ན་དེ་ལ་བཤད་པར་བྱ་སྟེ། གལ་ཏེ་སྔོན་གྱི་ཚེ་རབས་རྣམས་སུ་གང་བྱུང་བར་གྱུར་པ་དེ་ཉིད་ད་ལྟར་གྱི་བདག་འདི་ཡིན་པར་གྱུར་ན་དེ་ལྟ་ན་ཉེ་བར་ལེན་པ་ཐ་དད་པར་མི་འགྱུར་བ་ཞིག་ན་ཉེ་བར་ལེན་པ་ཐ་དད་པར་ཡང་འགྱུར་ལ། ཉེ་བར་ལེན་པ་མ་གཏོགས་པར་བདག་ཡོད་པར་ཡང་ཐལ་བར་འགྱུར་རོ། །

[Block 2772]
དེ་ལ་ཉེ་བར་ལེན་པ་མ་གཏོགས་པ་ཁྱོད་ཀྱི་བདག་དེ་གང་ཞིག་ཡིན་པར་སྨྲ་བར་ནུས་སམ། ཁོ་བོས་ནི་རྣམ་པ་ཐམས་ཅད་དུ་ཡང་མི་འཐད་པར་ཤེས་སོ། །

[Block 2773]
དེ་ལ་འདི་སྙམ་དུ་ཉེ་བར་ལེན་པ་མ་གཏོགས་པའི་བདག་ཡོད་པ་མ་ཡིན་ནོ་སྙམ་དུ་སེམས་ན་ནི། དེའི་ཕྱིར་ཉེ་བར་ལེན་པ་ཉིད་བདག་ཡིན་པར་འགྱུར་བའམ། ཡང་ན་ཁྱོད་ཀྱི་བདག་མེད་པ་ཡིན་ནོ། །

[Block 2774]
ཉེ་བར་ལེན་པ་ཉིད་བདག་ཡིན་ནོ་ཞེས་བྱ་བ་དེ་ཡང་མི་འཐད་དེ། ཅིའི་ཕྱིར་ཞེ་ན། ཉེ་བར་ལེན་པ་དེ་ནི་འབྱུང་བ་དང་། འཇིག་པ་ཡིན་པས་སྐྱེ་བ་དང་འགག་པར་འགྱུར་བའི་ཕྱིར་རོ།[^1761] །དེ་ལྟ་བུ་ནི་བདག་གི་མཚན་ཉིད་མ་ཡིན་ནོ། །

[Block 2775]
ཡང་གཞན་ཡང་། ཉེ་བར་བླང་བ་གང་ཡིན་པ་དེ་ཉིད་ཇི་ལྟ་བུར་ཉེ་བར་ལེན་པ་པོ་ཡིན་པར་འགྱུར་ཏེ། སྐྱོན་དུ་མར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2776]
དེ་ལ་འདི་སྙམ་དུ་ཉེ་བར་བླང་བ་ལས་ཉེ་བར་ལེན་པ་པོ་གཞན་ཡིན་པར་སེམས་ན། དེ་ལ་བཤད་པར་བྱ་སྟེ། བདག་ནི་ཉེ་བར་ལེན་པ་ལས་གཞན་དུ་འཐད་པ་ཉིད་མ་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན། གལ་ཏེ་གཞན་ཡིན༌[^1762]ན་ཉེ་བར་ལེན་པ་མེད་པར་ཡང་མིག་ལ་སོགས་པའི་དབང་པོ་རྣམས་ཀྱིས་གཟུང་དུ་ཡོད་པའི་རིགས་ན་གཟུང་དུ་མེད་པའི་ཕྱིར་རོ། །

[Block 2777]
དེ་ལྟ་ན་བདག་ཉིད་ཉེ་བར་ལེན་པ་ལས་གཞན་ཡང་མ་ཡིན་ལ། དེ་ནི་ཉེ་བར་ལེན་པ་ཉིད་ཀྱང་མ་ཡིན། ཉེ་བར་ལེན་པ་མེད་པ་ཡང་མ་ཡིན། འགའ་ཡང་མེད་པ་ཉིད་དུ་ངེས་པ་ཡང་མ་ཡིན་ནོ། །

[Block 2778]
དེའི་ཕྱིར་རྟག་པ་འདིས་བདག་སྔོན་འདས་པའི་དུས་ན་བྱུང་བར་གྱུར་ཞེས་བྱ་བ་དེ་ནི༌[^1763]མི་འཐད་དོ། །

[Block 2779]
ད་ནི།

[Block 2780 [VERSE]]
འདས་པའི་དུས་ན་མ་བྱུང་ཞེས། །
བྱ་བ་དེ་ཡང་མི་འཐད་དོ། །
སྔོན་ཚེ་རྣམས་སུ་གང་བྱུང་བ། །
དེ་ལས་འདི་གཞན་མ་ཡིན་ནོ། །

[Block 2781 [VERSE]]
གལ་ཏེ་འདི་ནི་གཞན་གྱུར་ན། །
དེ་མེད་པར་ཡང་འབྱུང་བར་འགྱུར། །
དེ་བཞིན་དུ་ནི་གནས་འགྱུར་ཞིང་། །
དེར་མ་ཤི་བར་སྐྱེ་བར་འགྱུར། །

[Block 2782 [VERSE]]
ཆད་དང་ལས་རྣམས་ཆུད་ཟ་དང་། །
གཞན་གྱིས༌[^1764]བྱས་པའི་ལས་རྣམས༌[^1765]ནི། །
གཞན་གྱིས་སོ་སོར་མྱོང་བ་དང་། །
དེ་ལ་སོགས་པར་ཐལ་བར་འགྱུར། །
མ་བྱུང་བ་ལས་བྱུང་མིན་ཏེ།

[Block 2783]
[^1766] །

[Block 2784 [VERSE]]
འདི་ལ་སྐྱོན་དུ་ཐལ་བར་འགྱུར། །
བདག་ནི་བྱས་པར་འགྱུར་བ་དང་། །
འབྱུང་བ༌[^1767]རྒྱུ་མེད་ཅན་དུ་འགྱུར། །

[Block 2785]
ད་ནི་བདག་སྔོན་འདས་པའི་དུས་ན་བྱུང་བར་མ་གྱུར་ཅེས་བྱ་བ་དེ་ཡང་མི་འཐད་དོ། །ཅིའི་ཕྱིར་ཞེ་ན། སྔོན་གྱི་ཚེ་རབས་རྣམས་སུ་གང་བྱུང་བར་གྱུར་པ་དེ་ལས་འདི་གཞན་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2786]
གལ་ཏེ་འདི་གཞན་ཡིན་པར་གྱུར་ན་དེའི་ཕྱིར་དེ་མེད་པར་ཡང་འདི་འབྱུང་བར་འགྱུར་རོ། །

[Block 2787]
ཡང་གཞན་ཡང་། སྔ་མ་དེ་དེ་བཞིན་དུ་དེ་ན་གནས་པར་འགྱུར་ཞིང་འདི་ཡང་དེར་མ་ཤི་བར་འདིར་སྐྱེ་བར་འགྱུར་རོ། །

[Block 2788]
དེ་ལྟ་ན་ཆད་པ་དང་ལས་རྣམས་ཆུད་ཟ་བ་དང་གཞན་གྱིས་བྱས་པའི་ལས་རྣམས་གཞན་གྱིས་སོ་སོར་མྱོང་བ་དང་དེ་ལ་སོགས་པ་སྐྱོན་མང་པོ་དག་ཏུ་ཐལ་བར་འགྱུར་རོ། །

[Block 2789]
ཡང་གཞན་ཡང་། དེ་ལྟ་ན་བདག་མ་བྱུང་བ་ལས་བྱུང་བར༌[^1768]ཐལ་བར་འགྱུར་ཏེ། བདག་མ་བྱུང་བ་ལས་བྱུང་བ༌[^1769]ནི་མ་ཡིན་པས། དེའི་ཕྱིར་འདི་ལ་ཡང་བདག་བྱས་པར་འགྱུར་བ་དང་། འབྱུང་བ་རྒྱུ་མེད་པ་ཅན་དུ་འགྱུར་བའི་སྐྱོན་དུ་ཐལ་བར་འགྱུར་བས་དེ་ནི་མི་འདོད་དོ། །

[Block 2790]
དེའི་ཕྱིར་རྟག་པ་འདིས་བདག་སྔོན་འདས་པའི་དུས་ན་བྱུང་བར་མ་གྱུར་ཅེས་བྱ་བ་དེ་ཡང་མི་འཐད་དོ། །

[Block 2791 [VERSE]]
དེ་ལྟར་བདག་བྱུང་བདག་མ་བྱུང་། །
གཉི་ག་གཉི་ག་མ་ཡིན་པར། །
འདས་ལ་ལྟ་བ་གང་ཡིན་པ། །
དེ་དག་འཐད་པ་མ་ཡིན་ནོ། །

[Block 2792]
དེ་ལྟར་ཡོངས་སུ་བརྟགས་ན་བདག་སྔོན་འདས་པའི་དུས་ན་བྱུང་བར་གྱུར་ཅེས་བྱ་བ་དང་། བདག་སྔོན་འདས་པའི་དུས་ན་བྱུང་བར་མ་གྱུར་ཅེས་བྱ་བ་དང་། སྔོན་འདས་པའི་དུས་ན་བྱུང་བར་གྱུར་ཀྱང་གྱུར་ལ། བྱུང་བར་མ་གྱུར་ཀྱང་མ་གྱུར་ཅེས་བྱ་བ་དང་། སྔོན་འདས་པའི་དུས་ན་བྱུང་བར་གྱུར་པ་ཡང་མ་ཡིན། བྱུང་བར་མ་གྱུར་པ་ཡང་མ་ཡིན་ནོ་ཞེས་བྱ་བར་འདས་པའི་དུས་ལ་ལྟ་བ་གང་ཡིན་པ་དེ་དག་འཐད་པ་མ་ཡིན་ནོ། །

[Block 2793]
ད་ནི།

[Block 2794 [VERSE]]
མ་འོངས་དུས་གཞན་འབྱུང་འགྱུར་དང་། །
འབྱུང་བར་མི་འགྱུར་ཞེས་བྱ་བར། །
ལྟ་བ་གང་ཡིན་དེ་དག་ནི། །
འདས་པའི་དུས་དང་མཚུངས་པ་ཡིན། །

[Block 2795]
ད་ནི་བདག་མ་འོངས་པའི་དུས་གཞན་དུ་འབྱུང་བར་འགྱུར་ཞེས་བྱ་བ་དང་། བདག་མ་འོངས་པའི་དུས་གཞན་དུ་འབྱུང་བར་མི་འགྱུར་ཞེས་བྱ་བར་མ་འོངས་པའི་དུས་ལ་ལྟ་བ་གང་ཡིན་པ་དེ་དག་ནི་འདས་པའི་དུས་དང་མཚུངས་པར་བསམ་པར་བྱ་སྟེ། འདས་པའི་དུས་ལས་བརྩམས་པའི་སྐྱོན་གང་དག་ཡིན་པ་དེ་དག་ཉིད་འདིར་ཡང་བྱེ་བྲག་ཏུ་ཤེས་པར་བྱའོ། །

[Block 2796]
ཡང་གཞན་ཡང་།

[Block 2797 [VERSE]]
གལ་ཏེ་ལྷ་དེ་མི་དེ་ན། །
དེ་ལྟ་ན་ནི་རྟག་པར་འགྱུར། །
ལྷ་ནི་མ་སྐྱེས་ཉིད་འགྱུར་ཏེ། །
རྟག་ལ་སྐྱེ་བ་མེད་ཕྱིར་རོ། །

[Block 2798]
གལ་ཏེ་ལྷ་དེ་ཉིད་མི་དེ་ཉིད་དུ་གྱུར་ན་དེ་ལྟ་ན་ནི་རྟག་པར་འགྱུར་རོ། །

[Block 2799]
ཡང་གཞན་ཡང་། ལྷ་མ་སྐྱེས་པ་ཉིད་དུ་ཡང་འགྱུར་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། རྟག་པ་ལ་སྐྱེ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 2800]
གང་གི་ཕྱིར་ལྷ་གང་ཡིན་པ་དེ་ཉིད་མི་མ་ཡིན་ཞིང་། ལྷ་མ་སྐྱེས་པ་ཉིད་ཀྱང་མ་ཡིན་པ་དེའི་ཕྱིར་རྟག་པ་མ་ཡིན་ནོ། །

[Block 2801 [VERSE]]
གལ་ཏེ་ལྷ་ལས་མི་གཞན་ན། །
དེ་ལྟ་ན་ནི་མི་རྟག་འགྱུར། །
གལ་ཏེ་ལྷ་མི་གཞན་ཡིན་ནོ། །
རྒྱུད༌[^1770]ནི་འཐད་པར་མི་འགྱུར་རོ། །

[Block 2802]
གལ་ཏེ་ལྷ་ལས་མི་གཞན་ཡིན་ན་དེ་ལྟ་ན་ནི་མི་རྟག་པར་འགྱུར་རོ། །

[Block 2803]
རྒྱུད་ཀྱི་གཏན་ཚིགས་ཀྱིས་ལྷ་ལས་མི་གཞན་ཡིན་པར་མི་འཐད་པས་དེའི་ཕྱིར་མི་རྟག་པ་མ་ཡིན་ནོ། །

[Block 2804 [VERSE]]
གལ་ཏེ་ཕྱོགས་གཅིག་ལྷ་ཡིན་ལ། །
ཕྱོགས་གཅིག་མི་ནི་ཡིན་གྱུར་ན། །
རྟག་དང་མི་རྟག་འགྱུར་བའི་ཕྱིར། །
དེ་ཡང་རིགས་པ་མ་ཡིན་ནོ། །

[Block 2805]
གལ་ཏེ་ཕྱོགས་གཅིག་ནི་ལྷ་ཡིན་ལ་ཕྱོགས་གཅིག་ནི་མི་ཡིན་པར་གྱུར་ན་དེ་ལྟ་ན་རྟག་ཀྱང་རྟག་ལ་མི་རྟག་ཀྱང་མི་རྟག་པར་འགྱུར་བ་ཞིག་ན། གང་གི་ཕྱིར་དེ་ལྟར་བདག་ཉིད་གཉིས་པ་ཉིད་མི་རིགས་པ་དེའི་ཕྱིར་རྟག་ཀྱང་རྟག་ལ་མི་རྟག་ཀྱང་མི་རྟག་པ་མ་ཡིན་ནོ། །
--- END BLOCKS ---
