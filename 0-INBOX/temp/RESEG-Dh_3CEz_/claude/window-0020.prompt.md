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
[Block 701]
མི་བསྐྱོད་པ་བཏགས་པ༌[^249]ནི་བརྡུང༌[^250]བའོ། །

[Block 702]
ཉི་མ་གཟས་ཟིན་པ་ནི་རང་བྱུང་གི་མེ་ཏོག་གོ། །

[Block 703]
དགྲ་སྟ་ནི་གཅོད་པས་ན་དགྲ་སྟ་སྟེ་རྐང་པས་མནན་པ་དང་འདྲ་བ་སྟེ། འོག་ཏུ་འཇོམས་པའོ། །

[Block 704]
བཟླས་པ་ནི་ཡང་དང་ཡང་དུ་བསྒོམ་པ་སྟེ། ལྷ་གང་ལ་ཕྱག་བྱས་པ་ནི་དངོས་པོ་གཟུགས་ལ་སོགས་པ་དངོས་པོ་ལ་ཞེན་པ་གང་ཡང་རུང་བདེ༌[^251]འཇོམས་པའོ། །

[Block 705]
ལྷག་མ་རྣམས་ནི་གོ་སླ་བས་མ་བཤད་དོ། །

[Block 706]
རྡོ་རྗེ་མ་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་གོང་གི་རེངས་པ་ལ་སོགས་པའི་རྣལ་འབྱོར་མ༌[^252]རེ་རེ་དང་ལྷ་རེ་རེ༌[^253]སྦྱར་རོ། །

[Block 707]
བརྟུལ་ཞུགས་ཅན་ཞེས་པ་སྟེ་བསྐྱེད་པའི་རིམ་པ་ལ་མཚན་མ་ཐོབ་པར་བྱའོ། །

[Block 708]
རྫོགས་པའི་རིམ་པ་ལ་རང་གི་ཉམས་ཐོབ་ནས་བག་ཚ་བ་མེད་པས་བྱའོ། །

[Block 709]
ལེའུའི་མཚན་མ་ཡང་།[^254] སྔ་མ༌[^255]ལྟར་ཅི་རིགས་པར་སྦྱར་རོ། །

[Block 710]
ལེའུ་གཉིས་པའོ།། །།

[Block 711]
[^256]

[Block 712 [HEADING]]
### གསུམ་པ་ངོ་བོ། ^1-3-0

[Block 713]
དེ་ནས་ལྷའི་ལེའུ་བཤད་པར་བྱ་ཞེས་པ་ནི་ལྷ་སྟེ། ལུས་ལས་བྱུང་བ་དང་།

[Block 714 [VERSE]]
བདེ་བ་ལ་རོལ་བ་སྟེ་ལྷའོ། །
རྒྱུན༌[^257]ཞི་བའི་དོན་གྱིས་ན་ལྷའོ། །

[Block 715]
དེའི་རིམ་པ་ཡང་གཉིས་ཏེ་ཕྱག་གཉིས་པ་ལ་བཤད་པ་དང་གཞན་ལ་སྦྱར་བའོ། །

[Block 716 [HEADING]]
#### ཕྱག་གཉིས་པ་ལ་བཤད་པ། ^1-3-1-0

[Block 717]
བཤད་པ་ལ་ཡང་གཉིས་ཏེ། དཔའ་བོ་གཅིག་པ་བསྐྱེད་པ་དང་། དཀྱིལ་འཁོར་གྱི་འཁོར་ལོའོ། །

[Block 718 [HEADING]]
##### དཔའ་བོ་གཅིག་པ་བསྐྱེད་པ། ^1-3-1-1-0

[Block 719]
དེ་ལ་དཔའ་བོ་གཅིག་པ་ནི། དེ་ལ་སྒྲུབ་པོ་ཕུན་སུམ་ཚོགས་པ་དང་ལྡན་པས་རང་གི་སྙིང་ག་ལ་སོགས་པ་ཚིགས་སུ་བཅད་པ་གཅིག་གིས་རང་མོས་པའི་རྣལ་འབྱོར་གྱི༌[^258]ས་བོན་གྱི་འོད་ཟེར་ལས་ཞེས་པ་ལ་སོགས་པ་གནས་བསྲུང་བ་ནས་བརྩམས་ཏེ། བྱ་བའི་རིམ་པ་རྣམས་མཆོད་པ་བྱིན་གྱིས་བརླབ་པ་ཡན་ཆད་སྔ་མ་ལྟར་བྱས་ལ་ནམ་མཁར་རྗེ་བཙུན་ལ་སོགས་པ་ཚིགས་སུ་བཅད་པ་ཕྱེད་དང་བཞིས་མཆོད་ནས་བཤགས་པ་ལ་སོགས་པ་ཡང་བྱ་སྟེ། ཅིའི་ཕྱིར་ཚོགས་མ་བསགས་པར་ལྷ་མི་བསྒོམ་ཞེ་ན། རྒྱུ་དང་རྐྱེན་སྔོན་དུ་མ་སོང་བར་མི་འབྱུང་སྟེ། དཔེར་ན་མྱུ་གུ་སྔོན་པོ་བསྐྱེད༌[^259]པ་ལ་ཉེར་ལེན་གྱི་རྒྱུ་ས་བོན་མྱུ་གུ་ལྷན་ཅིག་བྱེད་པའི་རྐྱེན་ཆུ་ལུད་དང་དྲོད་ཚད་མེད་པར་མི་འབྱུང་བ་ལྟར། རྒྱུ་བསོད་ནམས་ཀྱི་ཚོགས་དང་རྐྱེན་ཡེ་ཤེས་ཀྱི་ཚོགས་གཉིས་བསགས་དགོས་ཏེ། བསོད་ནམས་ཀྱི་ཚོགས་བསགས་པ་ལ་ཡང་ཞིང་སྤྲུལ་དགོས་པས་དེ་ཡང་ལུགས་བཞི་སྟེ། སྙིང་ག་ནས་སྤྲུལ་པ་དང་བཀོད་པ་གསལ་བ་དང་། རང་བཞིན་དུ་གནས་པ་དང་། སྤྱན་དྲངས་པ་ལས་འདིར་སྤྱན་དྲང་པ་སྟེ། ཧེ་རུ་ཀ་ཕྱག་བཅུ་དྲུག་པ་ལ་ལྷ་མོ་བརྒྱད་ཀྱིས་བསྐོར་བ་གཅིག་གོ། །

[Block 720]
དེ་ལ་མཆོད་པ་ཕྱི་ནང་གསང་བ་དེ་ཁོ་ན་ཉིད་ཀྱིས་མཆོད་དོ། །

[Block 721]
ཕྱི་ནི་སྤོས་དང་མེ་ཏོག་ལ་སོགས་པའོ། །

[Block 722]
ནང་གི་ལྷ་མོ་བརྒྱད་པོ་རྣམས་ཀྱིས་མཆོད་དེ།[^260] །དཀར་མོ་རི་དགས་མཚན་མ་འཛིན། །ཞེས་པ་ནི་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱིས་གང་བའི་ཐོད་པ་ལག་པར་འཛིན་ཞེས་པ་ནི་རྒྱུད་ཀྱི་ཚིག་ཟོར་ཡང་དུ་བྱས་པའོ། །

[Block 723]
ལག་པ་ཞེས་པ་དང་། སྣོད་ཅེས་པ་དང་འཛིན་པ་ཞེས་གོང་འོག་ཀུན་ལ་སྦྱར་རོ། །

[Block 724]
བདུད་ལས་རྒྱལ་བ་ནི་རང་བྱུང་གི་རཀྟའོ། །

[Block 725]
ཆུ་ནི་དྲི་ཆུའོ། །

[Block 726]
སྨན་ནི་དྲི་ཆེན་ནོ། །

[Block 727]
རྡོ་རྗེ་ནི་ཤ་ཆེན་ནོ། །

[Block 728]
རོ་ནི་སྦྲང་རྩི་སྟེ་མཚོན་པས་ཆང་ངོ་། །ཅང་ཏེའུ་ནི་ཕྱིའི་མཆོད་པའོ། །

[Block 729]
འདོད་ཆགས་ཆེན་པོ་རྗེས་ཆགས་ཞེས་པ་ནི་གསང་བའི་མཆོད་པ་སྟེ། འདོད་ཆགས་ཆེན་པོ་ནི་གཙོ་བོའམ། རྗེས་ཆགས་ནི་གཡུང་མོ་སྟེ། གཡུང་མོས༌[^261]མགུལ་ནས་འཁྱུད་པ་ཉིད། །ཅེས་པ་ནི་མཆོད་བྱའི་ལྷ་མོ་རྣམས་གཙོ་བོ་ལ་བསྡུ། མཆོད་བྱེད་ཀྱི་ལྷ་མོ་རྣམས་གཡུང་མོ་ལ་བསྡུ་ལ། ཀུན་དུ་རུའི་རྗེས་སུ་ཆགས་པའམ་ཡང་ན་མཆོད་བྱེད་ཀྱི་ལྷ་མོ་རྣམས་རང་ལ་བསྡུ་ཞིང་གཡུང་མོས་རླུང༌[^262]མཚམས་ནས་འཁྱུད་པའི་ཚུལ་གྱིས་མཆོད་པའོ། །

[Block 730]
དེའི་དུས་སུ་བདེ་བའི་རོ་ཉམས་སུ་མྱོང་བ་ནི་དེ་ཁོ་ན་ཉིད་ཀྱི་མཆོད་པའོ། །

[Block 731]
དེའི་མདུན་དུ་བདུན་རྣམ་དག་བྱ་སྟེ། དེ་སྐད་དུ།

[Block 732 [VERSE]]
བླ་མ་རྡོ་རྗེ་འཆང་མཆོད་ཅིང་། །
བདུན་པ་ཡོངས་སུ་དག་པར་བྱ། །

[Block 733]
ཞེས་གསུངས་སོ། །

[Block 734]
དེ་ནས་དང་པོར་བྱམས་པ་ལ་སོགས་པ་ཚིགས་སུ་བཅད་པ་གཅིག་གིས་ཚོགས་རྒྱས༌[^263]འདེབས་ཏེ། ཚིག་དང་པོ་གཉིས༌[^264]ཀྱིས་བསོད་ནམས་ཀྱི་ཚོགས་ནུས་པ་དང་ལྡན་པར་བྱེད། ཚིག་འོག་མ་གཉིས་ཀྱིས་ཡེ་ཤེས་ཀྱི་ཚོགས་ནུས་པ་དང་ལྡན་པར་བྱེད་པའི་དགོས་པའོ། །

[Block 735]
ངེས་པའི་ཚིག་ནི་དམིགས་པ་ཚད་མེད་པས་སམ། འབྲས་བུ་ཚད་མེད་ཐོབ་པས་སོ། །

[Block 736]
དབྱེ་བ་གོ་རིམས་ངེས་པ་ནི་སྐྱེ་བའི་གོ་རིམས་ཏེ། བྱམས་པ་ནི་བརྩེ་བ་དང་ལྡན་པ་ལས༌[^265]སྙིང་རྗེ་སྐྱེས་པས་དེ་བཞིན་དུ་སྦྱར་རོ། །

[Block 737]
དམིགས་པའི་ཡུལ་ནི་བདེ་འགྲོ་དང་ངན་འགྲོ་དང་། ཉན་ཐོས་དང་རང་སངས་རྒྱས་དང་། སེམས་ཅན་ནས་སངས་རྒྱས་ཀྱི་བར་དུ་རིམ་པར་སྦྱར་རོ། །

[Block 738]
བསྒོམ་པའི་ཐབས་ནི་ཆེ་འབྲིང་རྣམ་པ་དགུ་རུ་ཕྱེ་སྟེ།

[Block 739]
དང་པོ་བྱམས་པ་ཞེས་པ་བཤེས་འབྲེལ་ལྟ་བུ་སྟེ། རང་གི་སྙིང་དུ་བཅུག་པ་གཅིག་ལ་བྱམས་པ་སྐྱེ། དེ་བཞིན་དུ་གཉེན་རབ་འབྲིང་གསུམ་ལ་སྦྱར་རོ། །

[Block 740]
ཡང༌[^266]ཐ་མལ་པ་རབ་འབྲིང་གསུམ་དང་དགྲ་རབ་འབྲིང་གསུམ་དུ་སེམས་ཅན་ཐམས་ཅད་ལ་བསྒོམ་མོ། །
--- END BLOCKS ---
