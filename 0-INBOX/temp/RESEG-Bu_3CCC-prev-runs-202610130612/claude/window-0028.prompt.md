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
[Block 981]
ཡང་གཞན་ཡང་། ལས་ཀྱང་བྱེད་པོ་མེད་པར་འགྱུར། །བྱེད་པ་པོ་གཞན་ཅི་ཡང་མི་བྱེད་པ་དེ་ལ་ལས་ཡོད་པར་ཡོངས་སུ་བརྟག་པ་གང་ཡིན་པ་དེ་ལ་ཡང་བྱེད་པ་པོ་མེད་པར་འགྱུར་རོ། །ཅིའི་ཕྱིར་ཞེ་ན། བྱེད་པ་པོ་ལས་བྱེད་ན་ལས་དེའི་བྱེད་པ་པོར་འགྱུར་ཞིང་། བྱེད་པ་པོ་བྱེད་པ་དེས་ཀྱང་ལས་དེ་བྱེད་པ་པོ་དང་བཅས་པར་འགྱུར་བ་ཡིན་ན་བྱ་བ་དང་བྲལ་ན་བྱེད་པ་པོ་ལས་དེ་མི་བྱེད་པའི་ཕྱིར་ཏེ། དེ་ལྟ་བས་ན་ལས་དེ་བྱེད་པ་པོ་མེད་པར་ཐལ་བར་འགྱུར་རོ། །

[Block 982]
དེ་བཞིན་དུ་ལས་ཡིན་པར་གྱུར་པ་ལ་བྱ་བ་མེད་དེ། འདི་ལ་ཡང་བྱ་བ་དང་ལྡན་པ་ཁོ་ན་ལས་ཡིན་པར་འགྱུར་ཏེ། འདི་ལྟར་བྱ་བ་ཁོ་ན་ལས་ཡིན་གྱི། མི་བྱ་བ༌[^622]མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 983]
དེའི་ཕྱིར་ལས་གང་བྱ་བ་དང་ལྡན་པ་དེ་ལས་ཡིན་པར་འགྱུར་ཞེས་བྱ་སྟེ། ལས་ཡིན་པར་གྱུར་པ་དེ་ལ་ནི། གང་གིས་བྱ་བ་ཡིན་ནོ། །ཞེས་བྱ་བའི་བྱ་བ་གཞན་མེད་དོ། །

[Block 984]
ཅི་སྟེ་ཡོད་ན་ནི། བྱ་བ་གཉིས་སུ་འགྱུར་ཏེ། ལས་གཅིག་ལ་བྱ་བ་གཉིས་ནི་མེད་དོ། །

[Block 985]
ཡང་གཞན་ཡང་། བྱེད་པ་པོ་ཡང་ལས་མེད་གྱུར།[^623] །ལས་མི་བྱ་བ་དེ་ལ་བྱེད་པ་པོ་ཡོད་པར་ཡོངས་སུ་བརྟག་པ་གང་ཡིན་པ་དེ་ལ་ཡང་ལས་མེད་པར་འགྱུར་རོ། །ཅིའི་ཕྱིར་ཞེ་ན། བྱེད་པ་པོའི་བྱ་བ་ཡིན་ན་བྱེད་པ་པོ་དེའི་ལས་སུ་འགྱུར་ཞིང་། ལས་བྱ་བ་དེས་ཀྱང་བྱེད་པ་པོ་དེ་ལས་དང་བཅས་པར་འགྱུར་བ་ཡིན་ན་བྱ་བ་དང་བྲལ་ན་ལས་དེ་བྱེད་པ་པོའི་བྱ་བ་མ་ཡིན་པའི་ཕྱིར་ཏེ། དེ་ལྟ་བས་ན་བྱེད་པ་པོ་དེ་ལས་མེད་པར་ཐལ་བར་འགྱུར་རོ། །

[Block 986]
དེ་ལྟ་བས༌[^624]ན་བྱ་བ་མེད་པའི་ཕྱིར་ལས་ཀྱང་བྱེད་པ་པོ་མེད་པར་ཐལ་བར་འགྱུར་ལ། བྱེད་པ་པོ་ཡང་ལས་མེད་པར་ཐལ་བར་འགྱུར་བས་བྱེད་པ་པོ་ཡིན་པར་གྱུར་པ་ལས་ཡིན༌[^625]པ་མི་བྱེད་དོ། །

[Block 987]
བྱེད་པ་པོ་མ་ཡིན་པར་གྱུར་པ་ཡང་ལས་མ་ཡིན་པར་གྱུར་པ་མི་བྱེད་དོ། །ཇི་ལྟར་ཞེ་ན།

[Block 988 [VERSE]]
གལ་ཏེ་བྱེད་པོར་མ་གྱུར་པ། །
ལས་སུ་མ་གྱུར་བྱེད་ན་ནི། །
ལས་ལ་རྒྱུ་མེད་ཐལ་བར་འགྱུར། །
བྱེད་པ་པོ་ཡང་རྒྱུ་མེད་འགྱུར། །

[Block 989]
བྱེད་པ་པོ་དང་ལས་དག་མ་ཡིན་པར་གྱུར་པ་ཞེས་བྱ་བ་ནི་གང་དག་བྱ་བ་དང་བྲལ་བ་དག་གོ། །

[Block 990]
དེ་ལ་གལ་ཏེ་བྱེད་པ་པོ་མ་ཡིན་པར་གྱུར་པ་བྱ་བ་དང་བྲལ་བ་ལས་མ་ཡིན་པར་གྱུར་པ་བྱ་བ་དང་བྲལ་བ་བྱེད་ན༌[^626]བྱེད་པ་པོ་དང་ལས༌[^627]རྒྱུ་མེད་པར་ཐལ་བར་འགྱུར་རོ། །ཅིའི་ཕྱིར་ཞེ་ན། འདི་ལྟར་བྱེད་པ་པོ་བྱ་བ་དང་ལྡན་པའི་རྒྱུ་ལས་བྱུང་བ་བྱེད་པ་པོ་ཉིད་ཡིན་ལ། ལས་ཀྱང་ལས་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 991]
དེ་ལྟ་བས་ན་བྱེད་པ་པོ་དང་ལས་དག་མ་ཡིན་པར་གྱུར་པ་བྱ་བ་དང་བྲལ་བ༌[^628]ཡོངས་སུ་རྟོག་ན་རྒྱུ་མེད་པ་ཉིད་དུ༌[^629]ཐལ་བར་འགྱུར་རོ། །

[Block 992]
དེ་ལ་འགའ་ཡང་བྱེད་པ་པོ་མ་ཡིན་པར་མི་འགྱུར་ལ་གང་ཡང་ལས་མ་ཡིན་པར་མི་འགྱུར་ཏེ། དེ་ལྟ་ན་འདི་ནི་བྱེད་པ་པོ་ཡིན་ནོ། །

[Block 993]
འདི་ནི་ལས་ཡིན་ནོ༌[^630]ཞེས་བྱ་བ་དག་མི་སྲིད་པར་འགྱུར་རོ། །

[Block 994]
དེ་དག་མི་སྲིད་ན་འདི་ནི་བསོད་ནམས་བྱེད་པ་ཡིན་ནོ། །

[Block 995]
འདི་ནི་མ་ཡིན་ནོ། །

[Block 996]
འདི་ནི་སྡིག་པ་བྱེད་པ་ཡིན་ནོ། །

[Block 997]
འདི་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་དག་ཀྱང་མི་འཐད་པར་འགྱུར་རོ། །

[Block 998]
དེ་དག་མི་འཐད་ན་འཆོལ་བའི་ཉེས་པ་ཆེན་པོར་འགྱུར་བས་དེའི་བྱེད་པ་པོ་མ་ཡིན་པར་གྱུར་པ་ལས་མ་ཡིན་པར་གྱུར་པ་མི་བྱེད་དེ།[^631] །ཡང་ན།

[Block 999 [VERSE]]
རྒྱུ་མེད་ན་ནི་འབྲས་བུ་དང་། །
རྒྱུ་ཡང་འཐད་པར་མི་འགྱུར་རོ། །

[Block 1000]
རྒྱུ་མེད་ན་འབྲས་བུ་ཅུང་ཟད་ཀྱང་འཐད་པར་མི་འགྱུར་ཏེ། རྒྱུ་མེད་པ་ལ་འབྲས་བུ་ཇི་ལྟར་འཐད་པར་འགྱུར། ཅི་སྟེ་འཐད་ན་ནི་གློ་བུར་དུ་ཐམས་ཅད་འབྱུང་བར་འགྱུར་ཞིང་། རྩོམ་པ་ཐམས་ཅད་དོན་མེད་པ་ཉིད་དུ་ཡང་འགྱུར་བས་དེ་ནི་མི་འདོད་དེ། དེ་ལྟ་བས་ན་རྒྱུ་མེད་ན་འབྲས་བུ་ཅུང་ཟད་ཀྱང་འཐད་པར་མི་འགྱུར་རོ། །

[Block 1001]
རྒྱུ་ཡང་འཐད་པར་མི་འགྱུར་རོ། །ཞེས་བྱ་བ་ནི་རྒྱུ་མེད་ན་རྐྱེན་ཀྱང་འཐད་པར་མི་འགྱུར་རོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1002]
དེ་ཡང་ཇི་ལྟར་འཐད་ཅེ༌[^632]ན། དངོས་པོ་རྒྱུ་ལས་བྱུང་བ་རྣམས་ལ་རྐྱེན་ཀྱང་ཕན་འདོགས་པར་བྱེད་པ་ཡིན་ན་རྒྱུ་མེད་ཅིང་དེ་ཉིད་མི་འབྱུང་ན་རྐྱེན་རྣམས་ཀྱིས་གང་ལ་ཕན་འདོགས་པར་འགྱུར་རོ། །

[Block 1003]
ཕན་འདོགས་པར་མི་བྱེད་ན་ནི་ཇི་ལྟར་རྐྱེན་རྣམས་སུ་འགྱུར།

[Block 1004]
དེ་ལྟ་བས་ན་རྒྱུ་མེད་ན་འབྲས་བུ་ཡང་འཐད་པར་མི་འགྱུར་ལ།

[Block 1005 [VERSE]]
རྒྱུ་ཡང་འཐད་པར་མི་འགྱུར་རོ། །
དེ་མེད་ན་ནི་བྱ་བ་དང་། །
བྱེད་པ་པོ་དང་བྱེད་མི་རིགས། །

[Block 1006]
དེ་མེད་ན་ནི་ཞེས་བྱ་བ་ནི་དེ་མེད་ན་སྟེ། འབྲས་བུ་དེ་མེད་ན་བྱ་བ་དང་བྱེད་པ་པོ་དང་། བྱེད་པ་དག་ཀྱང་མི་རིགས་སོ། །ཇི་ལྟར་ཞེ་ན། འདི་ན་གཅད༌[^633]པར་བྱ་བ་གཅོད་པ་ན་གཅོད་པ་པོས་གཅད་པས༌[^634]གཅོད་པར་བྱེད་དེ། དེ་ལ་གཅད་པར༌[^635]བྱ་བ་འབྲས་བུ་ཡོད་ན་གཅད་པའི༌[^636]བྱ་བ་ཡོད་ཅིང་གཅད་པའི༌[^637]བྱ་བའི་བྱེད་པ་པོ་གཅོད་པ་པོ་ཡང་ཡོད་ལ། གཅོད་པ་པོ་དེ་ཡང་གཅད་པའི༌[^638]བྱེད་པས་གཅོད་པར་བྱེད་དེ། གཅད༌[^639]པར་བྱ་བ་འབྲས་བུ་མེད་ན་གཞི་མེད་པ་ལ་གཅད་པའི༌[^640]བྱ་བ་ཇི་ལྟར་ཡོད་པར་འགྱུར། གཅད་པའི༌[^641]བྱ་བ་མེད་ན་དེའི་བྱེད་པ་པོ་གཅོད་པ་པོ་ཡོད་པར་ག་ལ་འགྱུར། གཅོད་པ་པོ་མེད་ན་གཅད་པའི༌[^642]བྱེད་པ་ག་ལ་ཡོད།

[Block 1007 [VERSE]]
བྱ་བ་ལ་སོགས་མི་རིགས་ན། །
ཆོས་དང་ཆོས་མིན་ཡོད་མ་ཡིན། །

[Block 1008]
བྱ་བ་ལ་སོགས་པ་མི་རིགས་པར་ཐལ་བར་གྱུར་ན་ཆོས་དང་ཆོས་མ་ཡིན་པ་དག་ཀྱང་ཡོད་པ་མ་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན། འདི་ལ་ཆོས་དང་ཆོས་མ་ཡིན་པ་ལུས་དང་ངག་དང་ཡིད་ཀྱི་བྱ་བའི་ཁྱད་པར་ཅན་དག་ནི་བྱེད་པ་པོ་དང་བྱ་བ་ལ་བརྟེན་པར་འདོད་པའི་ཕྱིར་ཏེ། དེ་ལྟ་བས་ན། བྱ་བ་དང་བྱེད་པ་པོ་དང་བྱེད་པ་དག་མི་རིགས་ན་དེ་དག་ལ་བརྟེན་པའི་ཆོས་དང་ཆོས་མ་ཡིན་པ་དག་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1009 [VERSE]]
ཆོས་དང་ཆོས་མིན་མེད་ན་ནི། །
དེ་ལས་བྱུང་བའི་འབྲས་བུ་མེད། །

[Block 1010]
དེ་ལྟར་ཆོས་དང་ཆོས་མ་ཡིན་པ་དག་མེད་ན་ཆོས་དང་ཆོས་མ་ཡིན་པ་དེ་དག་ལས་བྱུང་བའི་འབྲས་བུ་ཡང་མེད་པར་ཐལ་བར་འགྱུར། ཅིའི་ཕྱིར་ཞེ་ན། ས་བོན་ལ་སོགས་པ་ལས་ལོ་ཏོག་སྐྱེ་བ་བཞིན་དུ་ཆོས་དང་ཆོས་མ་ཡིན་པ་དག་ལས་འབྲས་བུ་འགྲུབ་པར་འདོད་པའི་ཕྱིར་རོ། །

[Block 1011]
བྱ་བ་ལ་སོགས་པ་མི་རིགས་པའི་ཕྱིར་རོ།[^643] །ཆོས་དང་ཆོས་མ་ཡིན་པ་དེ་དག་མེད་དོ། །

[Block 1012]
དེ་དག་མེད་པས་དེ་ལས་བྱུང་བའི་འབྲས་བུ་ཡོད་པར་ག་ལ་འགྱུར།

[Block 1013 [VERSE]]
འབྲས་བུ་མེད་ན་ཐར་པ་དང་། །
མཐོ་རིས་འགྱུར་བའི་ལམ་མི་འཐད། །
འབྲས་བུ་མེད་པར་ཐལ་བར་གྱུར་ན། །

[Block 1014]
མཐོ་རིས་སུ་འགྱུར་བ་དང་ཐལ་བར་འགྱུར་བའི་ལམ་ཡང་མི་འཐད་པར་འགྱུར་རོ། །

[Block 1015]
ཅིའི་ཕྱིར་ཞེ་ན། མཐོ་རིས་དང་བྱང་གྲོལ་དག་ནི་ཆོས་ཀྱི་འབྲས་བུ་ཡིན་ལ་དེ་དག་འཐོབ་པའི་ཐབས་ནི་ལམ་ཡིན་ན་མཐོ་རིས་དང་བྱང་གྲོལ་ཞེས་བྱ་བ་འབྲས་བུ་དེ་དག་མེད་ན་ལམ་དེ་གང་གིས་འཐོབ་པའི་ཐབས་སུ་འགྱུར། བྱ་བ་དག་ནི་ཐམས་ཅད་ཀྱང་། །དོན་མེད་ཉིད་དུ་ཐལ་བར་འགྱུར། འབྲས་བུ་མེད་པས་མཐོ་རིས་དང་བྱང་གྲོལ་གྱི་ལམ་མི་འཐད་པར་ཐལ་བར་འགྱུར་བ་འབའ་ཞིག་ཏུ་ཡང་མ་ཟད་ཀྱི། འཇིག་རྟེན་ན་ཞིང་ལས་ལ་སོགས་པའི་བྱ་བ་གང་དག་ཡིན་པ་དེ་དག་ཀྱང་དོན་མེད་པ་ཉིད་དུ་ཐལ་བར་འགྱུར་ཏེ། འཇིག་རྟེན་ནི་འབྲས་བུའི་དོན་དུ་བྱ་བ་དེ་དང་དེ་དག་རྩོམ་པར་བྱེད་པ་ཡིན་ན་འབྲས་བུ་དེ་དང་དེ་དག་མི་འཐད་ཅིང་འབྲས་བུ་མེད་ན་བྱ་བ་སྒྲུབ་པ་དག་དུབ་པའི་སྣོད་དུ་ཟད་པས་དོན་མེད་པ་ཉིད་དུ་ཐལ་བར་འགྱུར་རོ། །

[Block 1016]
དེའི་ཕྱིར་དེ་ལྟར་རྒྱུ་མེད་ན་ཉེས་པ་མང་པོ་དང་ཆེན་པོ་དག་ཏུ་ཐལ་བར་འགྱུར་བས་བྱེད་པ་པོ་མ་ཡིན་པར་འགྱུར་བས༌[^644]ལས་མ་ཡིན་པར་གྱུར་པ་བྱེད་དོ། །ཞེས་བྱ་བ་དེ་ནི་ཤིན་ཏུ་ཚིག་ངན་པ་ཡིན་ནོ། །

[Block 1017]
དེ་ལ་འདི་སྙམ་དུ་བྱེད་པ་པོ་ཡིན་པ་དང་མ་ཡིན་པར་གྱུར་པ་ལས་ཡིན་པ་དང་མ་ཡིན་པར་གྱུར་པ་བྱེད་པར་སེམས་ན། དེ་ལ་བཤད་པར་བྱ་སྟེ།

[Block 1018 [VERSE]]
བྱེད་པ་པོར་གྱུར་མ་གྱུར་པ། །
གྱུར་མ་གྱུར་དེ་མི་བྱེད་དེ། །

[Block 1019]
བྱེད་པ་པོ་ཡིན་པ་དང་མ་ཡིན་པར་གྱུར་པ་ནི་བྱ་བ་དང་ལྡན་པ་དང་བྱ་བ་དང་མི་ལྡན་པའོ། །

[Block 1020]
ལས་ཡིན་པ་དང་མ་ཡིན་པར་གྱུར་པ་ཡང་བྱ་བ་དང་ལྡན་པ་དང་བྱ་བ་དང་མི་ལྡན་པའོ། །
--- END BLOCKS ---
