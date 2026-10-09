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
[Block 491]
བཤད་པ།

[Block 492 [VERSE]]
གཟུགས་ཀྱི་རྒྱུ་ནི་མ་གཏོགས་པར། །
གཟུགས་ནི་དམིགས་པར་མི་འགྱུར་རོ། །

[Block 493]
འདི་ལ༌[^317]འབྱུང་བ་ཆེན་པོ་བཞི་པོ་དག་ནི་གཟུགས་ཀྱི་རྒྱུར་བསྟན། གཟུགས་ནི་དེ་དག་གི་འབྲས་བུར་བསྟན་ན། འབྱུང་བ་ཆེན་པོ་བཞི་པོ་དག་མ་གཏོགས་པར་འབྱུང་བ་ཆེན་པོ་བཞི་པོ་དེ་དག་ལས་དོན་གཞན་དུ་གྱུར་པ་གཟུགས་ཞེས་བྱ་བར་འབྲས་བུ་ནི་ཅི་ཡང་མེད་དེ། དེ་ལྟ་བས་ན་གཟུགས་ནི་མི་འཐད་དོ། །

[Block 494]
སྨྲས་པ། རེ་ཞིག་འབྱུང་བ་དག་ནི་ཡོད་དེ། དེ་ལ་རྒྱུ་ཡོད་པའི་ཕྱིར་འབྲས་བུ་ཡང་ཡོད་པས༌[^318]གཟུགས་ཀྱང་རབ་ཏུ་གྲུབ་པ་ཉིད་དོ། །

[Block 495]
བཤད་པ།

[Block 496 [VERSE]]
གཟུགས་ཞེས་བྱ་བ་མ་གཏོགས་པར། །
གཟུགས་ཀྱི་རྒྱུ་ཡང་མི་སྣང་ངོ་། །

[Block 497]
གཟུགས་མ་གཏོགས་པར་ཡང་འདི་ནི་གཟུགས་ཀྱི་རྒྱུའོ། །ཞེས་བྱ་བ་མི་སྣང་བ་ཉིད་དོ། །

[Block 498]
གཟུགས་ནི་མི་འཐད་པར་སྨྲས་ཟིན་ཏེ། དེ་ལྟར་གཟུགས་མི་འཐད་པའི་ཕྱིར་གཟུགས་ཀྱི་རྒྱུ་ཡང་མི་འཐད་དོ། །

[Block 499]
སྨྲས་པ། འདི་ལ་ཁྱོད་རྒྱུ་ལ་བརྟེན་ནས་འབྲས་བུ་སེལ་བར་བྱེད་ཅིང་། འབྲས་བུ་ལ་བརྟེན་ནས་རྒྱུ་སེལ་བར་བྱེད་པས་དེ་ལ་གང་ལ་བརྟེན་ནས་གཞན་ཞིག་སེལ་བར་བྱེད་པ་དེ་ནི་རེ་ཞིག་ཡོད་དོ། །

[Block 500]
དེ་ཡོད་ན་གཞན་ཡང་རབ་ཏུ་འགྲུབ་པར་འགྱུར་རོ། །

[Block 501]
བཤད་པ། གཞན་ཡོད་པ་ཉིད་དོ། །ཞེས་བརྗོད་པར་མི་ནུས་སོ། །ཅིའི་ཕྱིར་ཞེ་ན། འདི་ལྟར།

[Block 502 [VERSE]]
གཟུགས་ཀྱི་རྒྱུ་ནི་མ་གཏོགས་པར། །
གཟུགས་ན་གཟུགས་ནི་རྒྱུ་མེད་པར། །
ཐལ་བར་འགྱུར་ཏེ་དོན་གང་ཡང་། །
རྒྱུ་མེད་པ༌[^319]ནི་གང་ནའང་མེད། །

[Block 503]
གལ་ཏེ་རྒྱུ་བས༌[^320]ཀྱང་འབྲས་བུ་ཡོད་ན་ནི་དེའི་ཚེ་རྒྱུ་མེད་པ་ཅན་དུ་འགྱུར་ཏེ། དོན་གང་ཡང་རྒྱུ་མེད་པ་ཅན་ནི། མ་མཐོང་ཞིང་གང་དུ་ཡང་མ་བསྟན་ཏེ། རྟག་ཏུ་ཐམས་ཅད་ལས་ཐམས་ཅད་འབྱུང་བར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་དང་། རྩོམ་པ་ཐམས་ཅད་དོན་མེད་པ་ཉིད་ཀྱི་སྐྱོན་དུ་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 504]
དེ་བཞིན་དུ།

[Block 505 [VERSE]]
གལ་ཏེ་གཟུགས་ནི་མ་གཏོགས་པར། །
གཟུགས་ཀྱི་རྒྱུ་ཞིག་ཡོད་ན་ནི། །
འབྲས་བུ་མེད་པའི་རྒྱུར་འགྱུར་ཏེ། །
འབྲས་བུ་མེད་པའི་རྒྱུ་མེད་དོ། །

[Block 506]
གལ་ཏེ་འབྲས་བུ་བསལ་ཀྱང་རྒྱུ་ཡོད་ན་ནི་རྒྱུ་དེ་འབྲས་བུ་མེད་པ་ཅན་དུ་ཐལ་བར་འགྱུར་རོ། །

[Block 507]
འབྲས་བུ་མེད་པ་ཅན་གྱི་རྒྱུ་ནི་མེད་དེ། འདི་ནི་འདིའིའོ་ཞེས་བྱ་བའི་ཐ་སྙད་ཀྱང་མི་འཐད་པའི་ཕྱིར་དང་། ཐམས་ཅད་ཀྱི་རྒྱུ་ཐམས་ཅད་ཡིན་པར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་ཏེ། དེ་ལྟ་བས་ན་གཟུགས་ཀྱི་རྒྱུ་དག་ཀྱང་མི་འཐད་པ་ཉིད་ཡིན་ལ། གཟུགས་ཀྱང་འབྲས་བུར་མི་འཐད་དོ། །

[Block 508]
ཡང་གཞན་ཡང་།

[Block 509 [VERSE]]
གཟུགས་ཡོད་ན་ཡང་གཟུགས་ཀྱི་ནི། །
རྒྱུ་ཡང་འཐད་པར་མི་འགྱུར་ཉིད། །
གཟུགས་མེད་ན་ཡང་གཟུགས་ཀྱི་ནི། །
རྒྱུ་ཡང་འཐད་པར་མི་འགྱུར་ཉིད། །

[Block 510]
འདི་ལ་གཟུགས་ཀྱི་རྒྱུ་ཅི༌[^321]ཞིག་བརྟགས༌[^322]ན་གཟུགས་ཡོད་པ་ལ་བརྟག་གམ། འོན་ཏེ་གཟུགས་མེད་པ་ལ་བརྟག་གྲང་ན། གཟུགས་ཡོད་པ་ལ་ནི་གཟུགས་ཀྱི་རྒྱུ་མི་འཐད་དེ། མེད་པ་ལ་ཡང་མི་འཐད་དོ། །

[Block 511]
དེ་ལ་རེ་ཞིག་ཡོད་པ༌[^323]ནི་མི་འཐད་དེ། འདི་ལྟར་ཡོད་པ་ལ༌[^324]རྒྱུས་ཅི་ཞིག་བྱ། ཅི་སྟེ་ཡོད་པ་ལ་ཡང་རྒྱུའི་བྱ་བ་ཡོད་པར་འགྱུར་ན་ནི་ནམ་ཡང་མི་བྱ་བར་མི་འགྱུར་རོ། །

[Block 512]
དེ་ཡང་མི་འདོད་དེ། དེ་ལྟ་བས་ན་གཟུགས་ཡོད་པ་ལ་གཟུགས་ཀྱི་རྒྱུ་མི་འཐད་དོ། །

[Block 513]
གཟུགས་མེད་པ་ལ་ཡང་གཟུགས་ཀྱི་རྒྱུ་མི་འཐད་དེ། འདི་ལྟར་གཟུགས་མེད་ན་དེ་གང་གི་རྒྱུར་འགྱུར། དེ་ལྟ་བས་ན་གཟུགས་མེད་པ་ལ་ཡང་གཟུགས་ཀྱི་རྒྱུ་མི་འཐད་དོ། །

[Block 514]
དེ་ནི་རྐྱེན་དགག་པར་ཡང་མེད་དམ། ཡོད་པའི་དོན་ལ་ཡང་། རྐྱེན་ནི་རུང་བ་མ་ཡིན་ཏེ། །ཞེས་རབ་ཏུ་བསྟན་ཟིན་མོད་ཀྱི། ཡང་འདི༌[^325]ཡང་སྐབས་སུ་བབ་པས༌[^326]བསྟན་ཏོ། །

[Block 515]
རྒྱུ་མེད་པ་ཡི་གཟུགས་དག་ནི། །འཐད་པར་མི་རུང་རུང་མིན་ཉིད།[^327] །རྒྱུ་མ་བསྟན་པ་གློ་བུར་གྱི་གཟུགས་ནི་འཐད་པར་མི་རུང་བ༌[^328]ཉིད་དེ་རུང་བ་མ་ཡིན་པ་ཉིད་དོ། །ཅིའི་ཕྱིར་ཞེ་ན། རྟག་ཏུ་ཐམས་ཅད་འབྱུང་བར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་དང་། རྩོམ་པ་ཐམས་ཅད་དོན་མེད་པ་ཉིད་ཀྱི་སྐྱོན་དུ་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 516]
དེ་བས་ན་རྒྱུ་མེད་པ་ཅན་གྱི་ཕྱོགས་ནི་ཐམས་ཅད༌[^329]ཁོ་ན་ཡིན་པའི་ཕྱིར་འཐད་པར་མི་རུང་བ་ཉིད་དེ་རུང་བ་མ་ཡིན་པ་ཉིད་དོ། །ཞེས་ཡང་དང་ཡང་དུ་ངེས་པར་བཟུང༌[^330]སྟེ་བཤད་དོ། །

[Block 517 [VERSE]]
དེ་ཕྱིར་གཟུགས་ཀྱི་རྣམ་པར་རྟོག །
འགའ་ཡང་རྣམ་པར་བརྟག་མི་བྱ། །

[Block 518]
གང་གི་ཕྱིར་གཟུགས་ཀྱི་རྒྱུ་མ་གཏོགས་པར་གཟུགས་དམིགས་པར་མི་འགྱུར་བ་དང་། གཟུགས་ཡོད་པ་དང་མེད་པ་ལ་ཡང་གཟུགས་ཀྱི་རྒྱུ་མི་འཐད་པ་དང་། རྒྱུ་མེད་པའི་གཟུགས་ནི་འཐད་པར་མི་རུང་བ་ཉིད་དེ་རུང་བ་མ་ཡིན་པ་ཉིད་ཡིན་པ་དེའི་ཕྱིར་ཁྱོད་ལྟ་བུ་མཁས་པའི་རང་བཞིན་ཅན་དེ་ཁོ་ན་རྟོགས་པར་འདོད་པས་གཟུགས་ཀྱི་རྣམ་པར་རྟོག་པ་འགའ་ཡང་རྣམ་པར་བརྟག་པར་མི་བྱ་བར་རིགས་ཏེ། འདི་ལྟར་གནས་མེད་པ་ལ་བསམ་པ་ཇི་ལྟར་རིགས་པར་འགྱུར། ཡང་གཞན་ཡང་། འབྲས་བུ་རྒྱུ་དང་འདྲ་བ་ཞེས་བྱ་བ་འཐད་པ་མ་ཡིན་ཏེ།

[Block 519 [VERSE]]
འབྲས་བུ་རྒྱུ་དང་མི་འདྲ་ཞེས། །
བྱ་བའང་འཐད་པ་མ་ཡིན་ནོ། །

[Block 520]
འབྲས་བུ་དང་རྒྱུར་བརྟགས༌[^331]ན། འབྲས་བུ་རྒྱུ་དང་འདྲ་བའམ། མི་འདྲ་བར་བརྟག་གྲང་ན། དེ་ལ་འབྲས་བུ་རྒྱུ་དང་འདྲ་བ་ཞེས་བྱ་བ་ནི༌[^332]ཕྱོགས་དེ་ལ་ནི་གཟུགས་འབྱུང་བ་རྣམས་ཀྱི་འབྲས་བུར་མི་འཐད་པ་ཉིད་དོ། །

[Block 521]
འབྲས་བུ་རྒྱུ་དང་མི་འདྲ་བ་ཞེས་བྱ་བའི་ཕྱོགས་དེ་ལ་ཡང་གཟུགས་འབྱུང་བ་རྣམས་ཀྱི་འབྲས་བུར་མི་འཐད་པ་ཉིད་དོ། །ཇི་ལྟར་ཞེ་ན། འདི་ལ་འབྱུང་བ་རྣམས་ནི་སྲ་བ་དང་། གཤེར་བ་དང་། ཚ་བ་དང་གཡོ་བའི་ངོ་བོ་ཉིད་དུ་བསྟན་ན་འབྱུང་བའི་ཡོན་ཏན་དེ་དག་ནི་གཟུགས་ལ་དམིགས་སུ་མེད་དེ། འདི་ལྟར་ས་ནི་སྲ་བ་ཉིད། ཆུ་ནི་གཤེར་བ་ཉིད། མེ་ནི་ཚ་བ་ཉིད། རླུང་ནི་གཡོ་བ་ཉིད་དུ་དམིགས་པས་དེའི་ཕྱིར་དེ་ལྟར་འབྲས་བུ་རྒྱུ་དང་འདྲ་བ་ཡང་མེད་ལ། རྒྱུ་དང་མི་འདྲ་བ་ཡང་མེད་པ་དེའི་ཕྱིར་གཟུགས་འབྲས་བུའོ། །ཞེས་བྱ་བར་མི་འཐད་པ་ཉིད་དོ། །

[Block 522 [VERSE]]
ཚོར་བ༌[^333]འདུ་ཤེས་འདུ་བྱེད་དང་། །
སེམས་དང་དངོས་པོ་ཐམས་ཅད་ཀྱང་། །
རྣམ་པ་དག་ནི་ཐམས་ཅད་དུ། །
གཟུགས་ཉིད་ཀྱིས་ནི་རིམ་པ་མཚུངས། །

[Block 523]
ཚོར་བ་དང་། འདུ་ཤེས་དང་། འདུ་བྱེད་དང་། རྣམ་པར་ཤེས་པ་དེ་དག་ཀྱང་གཟུགས་མི་འཐད་པ་ཉིད་ཀྱིས་མི་འཐད་པར་རིམ་པ་མཚུངས་ཏེ། ཇི་ལྟར་འབྱུང་བ་མ་གཏོགས་པར་གཟུགས་མེད་པ་དེ་བཞིན་དུ་རེག་པ་མ་གཏོགས་པར་ཚོར་བ་མེད་ལ། ཇི་ལྟར་གཟུགས་མ་གཏོགས་པར་གཟུགས་ཀྱི་རྒྱུ་མེད་པ་དེ་བཞིན་དུ་ཚོར་བ་མ་གཏོགས་པར་ཡང་རེག་པ་མེད་དེ། དེ་ལྟར་བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་། བདེ་བ་མྱོང་བར་འགྱུར་བའི་རེག་པ་ལ་བརྟེན་ནས་བདེ་བའི་ཚོར་བ་སྐྱེའོ་ཞེས་གསུངས་སོ། །

[Block 524]
ལྷག་མ་རྣམས་ལ་ཡང་དེ་བཞིན་དུ་སྦྱར་བར་བྱ་སྟེ་དེ་ལྟ་བས་ན་ཕུང་པོ་རྣམས་ཡོད་དོ་ཞེས་བྱ་བ་དེ་མི་འཐད་པ་ཉིད་དོ། །

[Block 525]
བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་སྒྱུ་མ་འདི་ནི་བྱིས་པ་འདྲིད་པའོ། །ཞེས་གསུངས་སོ། །

[Block 526]
དེ་ལྟར་ཡང་།

[Block 527 [VERSE]]
གཟུགས་ནི་དབུ་བ་རྡོས་པ་འདྲ། །
ཚོར་བ་ཆུ་བུར་དག་དང་མཚུངས། །
འདུ་ཤེས་སྨིག་རྒྱུ་འདྲ་བ་སྟེ། །
འདུ་བྱེད་རྣམས་ནི་ཆུ་ཤིང་བཞིན། །

[Block 528]
རྣམ་ཤེས་སྒྱུ་མ་ལྟ་བུ་ཞེས། །ཉི་མའི་གཉེན་གྱིས་བཀའ་སྩལ་ཏོ། །ཞེས་ཀྱང་གསུངས་སོ། །

[Block 529]
ཕུང་པོ་རྣམས་ཉི་ཚེ་གཟུགས་མི་འཐད་པ་ཉིད་ཀྱིས་མི་འཐད༌[^334]པར་རིམ་པ་མཚུངས་པར་མ་ཟད་ཀྱི། ཆོས་ཐམས་ཅད་ཀྱང་གཟུགས་མི་འཐད་པ་ཉིད་ཀྱིས་མི་འཐད་པར་རིམ་པ་མཚུངས་སོ། །

[Block 530]
དེ་ལྟར་གང་གི་ཕྱིར་ཆོས་ཐམས་ཅད་གཟུགས་མི་འཐད་པ་ཉིད་ཀྱིས་མི་འཐད་པར་རིམ་པ་མཚུངས་པ་དེའི་ཕྱིར།
--- END BLOCKS ---
