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
[Block 2311]
ཞེས་སྨྲས་པས། དེས་ན་རྒྱུ་ལས་འབྲས་བུ་གཞན་ཉིད་མ་ཡིན་པའི་ཕྱིར་རྒྱུ་ཆད་པར་མི་འགྱུར་རོ། །

[Block 2312]
བཤད་པ། ཁོ་བོས་དེ་སྐད་སྨྲ༌[^1526]མོད་ཀྱི་ཁྱོད་ཀྱིས་དེའི་རྟེན༌[^1527]གྱི་དེ་ཁོ་ན་ཁོང་དུ་མ་ཆུད་དེ། འདི་ལྟར་གལ་ཏེ་དངོས་པོ་འགག་ཅིང་དངོས་པོ་ཉིད་སྐྱེ་བར་འགྱུར་ན། དེ་གཉིས་དེ་ཉིད་དམ་གཞན་ཉིད་དུ་ཇི་ལྟར་མི་འགྱུར། འདི་ལྟར་གལ་ཏེ་རེ་ཞིག་རྒྱུས་རྒྱུའི་གནས་སྐབས་སྤངས་ཏེ་འབྲས་བུའི་གནས་སྐབས་སུ་འཕོ་བར་གྱུར་ན་ནི། དེ་ལྟ་ན་དེ་ཉིད་རྒྱུ་ཡིན་ཏེ། དེའི་གནས་སྐབས་གཞན་དང་གཞན་དུ་གྱུར་པ་འབའ་ཞིག་ཏུ་ཟད་དོ། །

[Block 2313]
དཔེར་ན་བྲོ་གར་མཁན་གྱིས་ཆ་ལུགས་གཞན་སྤངས་ཏེ། ཆ་ལུགས་གཞན་ལེན་པར་བྱེད་པ་དེ་ལ་ཆ་ལུགས་ཐ་དད་པ་ཉིད་དུ་འགྱུར་བ་འབའ་ཞིག་ཏུ་ཟད་ཀྱི་བྲོ་གར་མཁན་ལ་ཐ་དད་པ་མེད་པ༌[^1528]དེ་ཆ་ལུགས་ཐ་དད་པར་གྱུར་ཀྱང་། དེ་ཉིད་བྲོ་གར་མཁན་ཡིན་པ་དེ་བཞིན་དུ། གནས་སྐབས་གཞན་དུ་འཕོས་སུ་ཟིན་ཀྱང་། དེ་ཉིད་རྒྱུ་ཡིན་ན་ཇི་ལྟར་དེ་ཉིད་ཡིན་པར་མི་འགྱུར། ཅི་སྟེ་ཡང་འདི་སྙམ་དུ་རྒྱུ་ནི་གནས་སྐབས་གཞན་དུ་མི་འཕོ་བར་རྒྱུ་འགག་པར་འགྱུར་ཏེ། རྒྱུ་འགགས་པ་ན་འབྲས་བུ་སྐྱེ་བར་འགྱུར་བར་སེམས་ན། དེ་ལྟ་ན་ཡང་གང་གི་ཚེ་གཞན་འགགས་པ་ལ་གཞན་སྐྱེས་པ་དེའི་ཚེ་ཇི་ལྟར་གཞན་ཉིད་དུ་མི་འགྱུར། ཁོ་བོ་ཅག་ལ་ནི་དངོས་པོ་ལ༌[^1529]བརྟེན་ནས་གདགས་པ་ངོ་བོ་ཉིད་སྟོང་པ་སྒྱུ་མ་དང་སྨིག་རྒྱུ་དང་གཟུགས་བརྙན་ལྟ་བུ་རྣམས་ལ་དངོས་པོ་དེ་གང་གིར་འགྱུར་ཏེ༌[^1530]དངོས་པོ་དེ་གང་ལས་གཞན་དུ་འགྱུར་ཏེ་དེ་ཉིད་དང་གཞན་ཉིད་དུ་འགྱུར་བ་མེད་དོ། །

[Block 2314]
དེ་ལྟ་བས་ན་དངོས་པོར་ལྟ་བ་ཡོད་ན་རྒྱུ་འགགས་པ་ཡང་སྐྱེ་བ་མེད་པའི་ཕྱིར་རྒྱུན་ཆད་པ་ཁོ་ནར་ཐལ་བར་འགྱུར་རོ། །

[Block 2315]
ཡང་གཞན་ཡང་།

[Block 2316 [VERSE]]
དངོས་པོ་ངོ་བོ་ཉིད་ཡོད་ན། །
དངོས་མེད་འགྱུར་བར་མི་རིགས་སོ། །

[Block 2317]
དངོས་པོ་ངོ་བོ་ཉིད་ཀྱིས་ཡོད་ན་ངོ་བོ་ཉིད་ཡོད་པ་ནི་དངོས་པོ་མེད་པར་འགྱུར་བར་མི་རིགས་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། རང་བཞིན་ནི་གཞན་དུ་མི་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2318]
དེའི་ཕྱིར་དངོས་པོར་ལྟ་བ་ཡོད་ན་རྒྱུ་ཡང་འགག་པར་མི་འཐད་ལ་འབྲས་བུ་ཡང་སྐྱེ་བར་མི་འཐད་དེ་སྐྱེ་བ་དང་འགག་པ་དག་ནི་བཀག་པར་གྱུར་པ་ཡིན་པའི་ཕྱིར། དེ་ལ་རྟག་པ་ཁོ་ནའི་སྐྱོན་དུ་ཐལ་བར་འགྱུར་རོ། །

[Block 2319]
ཡང་གཞན་ཡང་།

[Block 2320 [VERSE]]
མྱ་ངན་འདས་པའི་དུས་ན་ཆད། །
སྲིད་རྒྱུན་རབ་ཏུ་ཞི་ཕྱིར་རོ། །

[Block 2321]
མྱ་ངན་ལས་འདས་པའི་དུས་ན་དགྲ་བཅོམ་པའི་སྲིད་པའི་རྒྱུན་རབ་ཏུ་ཞི་བའི་ཕྱིར་ཆད་པ་ཁོ་ནའི་སྐྱོན་དུ་ཡང་ཐལ་བར་འགྱུར་རོ། །

[Block 2322]
དེ་ལྟ་བས་ན་སྲིད་པའི་རྒྱུན་དེ༌[^1531]ཡོད་པར་རྟོག་ན་ཡང་རྟག་པ་དང་ཆད་པ་ཁོ་ནའི་སྐྱོན་དུ་ཐལ་བར་འགྱུར་རོ། །

[Block 2323]
སྨྲས་པ། རེ་ཞིག་སྲིད་པའི་རྒྱུན་ནི་རབ་ཏུ་གྲུབ་པོ། །མྱ་ངན་ལས་འདས་པའི་དུས་ན་དགྲ་བཅོམ་པའི་སྲིད་པའི་རྒྱུན་ལྡོག་པ་ནི་ཁོ་བོ་ཅག་ལ་མི་གནོད་པས་མྱ་ངན་ལས་འདས་པའི་དུས་ན་དེ་ཆད་པར་འགྱུར༌[^1532]ཀྱང་སླའོ།[^1533] །བཤད་པ། ཁྱོད་ཀྱི་སྲིད་པའི་རྒྱུན་ཡོད་ན་རྟག་པ་དང་ཆད་པའི་སྐྱོན་དུ་ཐལ་བར་མི་འགྱུར་རོ་ཞེས་གང་སྨྲས་པ་དེ་ཉིད་ཀྱང་ཁོ་བོས་སྲིད་པའི་རྒྱུན་ཡོད་ཀྱང་རྟག་པ་དང་ཆད་པ་ཁོ་ནའི་སྐྱོན་དུ་ཐལ་བར་འགྱུར་རོ་ཞེས་རབ་ཏུ་བསྟན་ཟིན་ཏོ། །

[Block 2324]
རེ་ཞིག་སྲིད་པའི་རྒྱུན་ནི་རབ་ཏུ་གྲུབ་པོ་ཞེས་གང་སྨྲས་པ་དེ་ཡང་རིགས་པ་མ་ཡིན་ཏེ། སྲིད་པའི་རྒྱུན་ནི་ཇི་ལྟར་ཡང་མི་འཐད་པ་ཁོ་ནའོ། །ཅིའི་ཕྱིར་ཞེ་ན། འདི་ལྟར།

[Block 2325 [VERSE]]
ཐ་མ་འགགས་པར་གྱུར་པ་ནི། །
སྲིད་པ་དང་པོར་སྦྱོར་མི་འགྱུར། །

[Block 2326]
ད་ལྟར་གྱི༌[^1534]སྲིད་པའི་མཇུག་གི་སེམས་ནི་སྲིད་པ་ཐ་མའོ། །

[Block 2327]
མ་འོངས་པའི་སྲིད་པའི་སེམས་སྐྱེ་བའི་དང་པོ་ནི་སྲིད་པ་དང་པོའོ། །

[Block 2328]
དེ་ལ་རེ་ཞིག་སྲིད་པ་ཐ་མ་འགགས་པ་ནི་སྲིད་པ་དང་པོ་དང་ཉིང་མཚམས་སྦྱོར་བ་མེད་དེ། སྲིད་པ་ཐ་མ་འགགས་པ་ཡོད་པ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2329]
འདི་ལྟར་དངོས་པོ་འགགས་ཤིང་མེད་པ་ལས་ཇི་ལྟར་དངོས་པོ་སྐྱེ་བར་འགྱུར། ཅི་སྟེ་སྲིད་པ་ཐ་མ་འགགས་ཀྱང་སྲིད་པ་དང་པོ་སྐྱེ་བར་འགྱུར་ན་ནི། དེ་ལྟ་ན་སྲིད་པ་དང་པོ་རྒྱུ་མེད་པ་ལས་འབྱུང་བར༌[^1535]འགྱུར་བས། དེ་ནི་མི་འདོད་དེ་སྐྱོན་དུ་མར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2330]
དེ་ལ་འདི་སྙམ་དུ་སྲིད་པ་ཐ་མ་མ་འགགས་པ་སྲིད་པ་དང་པོ་དང༌[^1536]ཉིང་མཚམས་སྦྱོར་བར༌[^1537]སེམས་ན། དེ་ལ་བཤད་པར་བྱ་སྟེ།

[Block 2331 [VERSE]]
ཐ་མ་འགགས་པར་མ་གྱུར་པ། །
སྲིད་པ་དང་པོར་སྦྱོར་མི་འགྱུར། །

[Block 2332]
སྲིད་པ་ཐ་མ་མ་འགགས༌[^1538]པ་ཡང་སྲིད་པ་དང་པོ་དང་ཉིང་མཚམས་སྦྱོར་བ་མེད་དེ།[^1539] ཅིའི་ཕྱིར་ཞེ་ན། སྲིད་པ་གཉིས་སུ་ཐལ་བར་འགྱུར་བའི་ཕྱིར་དང་། རྒྱུ་མེད་པ་ལས་བྱུང་བའི་སྐྱོན་དུ་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2333]
སྨྲས་པ། སྲིད་པ་ཐ་མ་འགགས་པ་དང་མ་འགགས་པ་སྲིད་པ་དང་པོ་དང་ཉིང་མཚམས་སྦྱོར་བ་མེད་མོད་ཀྱི་འོན་ཀྱང་འགག༌[^1540]བཞིན་པ་ཉིང་མཚམས་སྦྱོར་རོ། །

[Block 2334]
བཤད་པ།

[Block 2335 [VERSE]]
གལ་ཏེ་ཐ་མ་འགག༌[^1541]བཞིན་པ། །
དང་པོ༌[^1542]སྐྱེ་བར་འགྱུར༌[^1543]ན་ནི། །
འགག་བཞིན་པ་ནི་གཅིག་འགྱུར་ཞིང་། །
སྐྱེ་བཞིན་པ་ཡང་གཞན་དུ་འགྱུར། །

[Block 2336]
གལ་ཏེ་སྲིད་པ་ཐ་མ་འགག་བཞིན་པ་སྲིད་པ་དང་པོ་དང་ཉིང་མཚམས་སྦྱོར་བར་གྱུར་ན། འགག་བཞིན་པ་ནི་ཕྱེད་འགགས་པའི་ཕྱིར་དང་། སྐྱེ་བཞིན་པ་ཡང་ཕྱེད་སྐྱེས་པའི་ཕྱིར་དེ་གཉིས་སྲིད་པ་གཉིས་སུ་ཐལ་བའི་སྐྱོན་དུ་འགྱུར་ཏེ། འགག་བཞིན་པ་དང་སྐྱེ་བཞིན་པ་དག་ཡོད་པའི་ཕྱིར་རོ། །

[Block 2337]
སྨྲས་པ། སྲིད་པ་ཐ་མ་འགགས་པ་དང་འགག་བཞིན་པ་སྲིད་པ་དང་པོ་དང་ཉིང་མཚམས་སྦྱོར་བ་མེད་དོ་ཞེས་བྱ་བ་དེས་ཁོ་བོ་ལ་ཅི་བྱ། ཡོད་ན༌[^1544]རེ་ཞིག་སྲིད་པ་དང་པོའི་སྐྱེ་བ་ནི་ཡོད་དེ། དེ་ཡོད་པས་སྲིད་པའི་རྒྱུན་ཡང་འཐད་དོ། །

[Block 2338]
བཤད་པ།

[Block 2339 [VERSE]]
གལ་ཏེ་འགག་བཞིན་སྐྱེ་བཞིན་དག །
ལྷན་ཅིག་སྦྱོར་བའང་ཡོད་མིན་ན། །
ཕུང་པོ་གང་ལ་འཆི་འགྱུར་བ། །
དེར་ནི་སྐྱེ་བའང་འབྱུང་བར་འགྱུར། །

[Block 2340]
ལྷན་ཅིག་སྦྱོར་བའང་ཞེས་བྱ་བའི་འང་གི་སྒྲ་ནི་སྲིད་པ་ཐ་མ་འགགས་པ་དང་མ་འགགས་པ་ཡང་བསྡུ་བའི་དོན་ཏོ། །

[Block 2341]
གལ་ཏེ་སྲིད་པ་ཐ་མ་འགག་བཞིན་པ་སྲིད་པ་དང་པོ་སྐྱེ་བཞིན་པ་དང་ལྷན་ཅིག་ཉིང་མཚམས་སྦྱོར་བའང་ཡོད་པ་མ་ཡིན་ཞིང་སྲིད་པ་ཐ་མ་འགགས་པ་ཡང་སྲིད་པ་དང་པོ་དང་ཉིང་མཚམས་སྦྱོར་བ་ཡོད་པ་མ་ཡིན་ལ། སྲིད་པ་ཐ་མ་འགགས་པ་ཡང་སྲིད་པ་དང་པོ་དང་ཉིང་མཚམས་སྦྱོར་བ་ཡོད་པ་མ་ཡིན་པ་བཞིན་དུ། སྲིད་པ་དང་པོའི་སྐྱེ་བ་ནི་ཡོད་དོ་ཞེས་ཟེར་ན། དེ་ལྟ་ན། ཕུང་པོ་གང་དག་ཁོ་ན་ལ་འཆི་བར་འགྱུར་བ་དེ་དག་ཁོ་ན་ལ་སྐྱེ་བ་ཡང་འབྱུང་བར་ཐལ་བར་འགྱུར་ཏེ། སྐྱེ་བ་གཞན་མི་འཐད་པའི་ཕྱིར་རོ། །

[Block 2342]
དེ་ཡང་མི་འདོད་དེ་དེ་ལྟ་བས་ན་དེ༌[^1545]གསུམ་མ་གཏོགས་པར་སྲིད་པ་འབྱུང་བར༌[^1546]མི་འཐད་དོ། །

[Block 2343 [VERSE]]
དེ་ལྟར་དུས་གསུམ་དག་ཏུ་ཡང་། །
སྲིད་པའི་རྒྱུན་ནི་མི་རིགས་ན། །
དུས་གསུམ་དག་ཏུ་གང་མེད་པ། །
དེ་ནི་ཇི་ལྟར་སྲིད་པའི་རྒྱུན། །

[Block 2344]
དེའི་ཕྱིར་དེ་ལྟར་ཡོངས་སུ་བརྟགས་ན་སྲིད་པ་ཐ་མ་འགགས་པ་དང་མ་འགགས་པ་དང་འགག་བཞིན་པ་སྲིད་པ་དང་པོ་དང་ཉིང་མཚམས་སྦྱོར་བར་མི་འཐད་པའི་ཕྱིར་དུས་གསུམ་དག་ཏུ་ཡང་སྲིད་པའི་རྒྱུན་མི་རིགས་སོ།[^1547] ། དུས་གསུམ་དག་ཏུ་སྲིད་པའི་རྒྱུན་གང་མེད་པ་དེ་དང་ཇི་ལྟར་སྲིད་པའི་རྒྱུན་དུ་འཐད། སྲིད་པའི་རྒྱུན་ཡོད་པ་མ་ཡིན་ན། འབྱུང་བ་དང་འཇིག་པ་དག་ཡོད་པར་ག་ལ་འགྱུར། འབྱུང་བ་དང་འཇིག་པ་དག་ཡོད་པ་མ་ཡིན་ན་ཁྱོད་ཀྱི་དུས་ལ་སོགས་པ་དག་འགྲུབ་པར་ག་ལ་འགྱུར། འབྱུང་བ་དང་འཇིག་པ་བརྟག་པ༌[^1548]ཞེས་བྱ་བ་སྟེ་རབ་ཏུ་བྱེད་པ་ཉི་ཤུ་གཅིག་པའོ།། །།

[Block 2345 [HEADING]]
## དེ་བཞིན་གཤེགས་པ་བརྟག་པ། ^22-0

[Block 2346]
སྨྲས་པ། སྲིད་པའི་རྒྱུན་ནི་ཡོད་པ་ཁོ་ན་སྟེ། ཅིའི་ཕྱིར་ཞེ་ན། དེ་བཞིན་གཤེགས་པ་ཡོད་པའི་ཕྱིར་རོ། །

[Block 2347]
དེ་བཞིན་གཤེགས་པ་ནི་བཅོམ་ལྡན་འདས་དགྲ་བཅོམ་པ་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་ཡོད་དོ། །

[Block 2348]
དེས་བསྐལ་པ་གྲངས་མེད་པ་དག་གིས་བྱང་ཆུབ་ཡང་དག་པར་བསྒྲུབས༌[^1549]ཏེ། དེ་ལྟར་ཡང་མདོ་སྡེ་གཞན་དག་ལས་དེའི་ཚེ་དེའི་དུས་ན་ང་བྲམ་ཟེའི་ཁྱེའུ་མིག་བཟང་ཞེས་བྱ་བར་གྱུར་ཏོ། །

[Block 2349]
དེའི་ཚེ་དེའི་དུས་ན་ང་རྒྱལ་པོ་ང་ལས༌[^1550]ནུ་ཞེས་བྱ་བར་གྱུར་ཏོ་ཞེས་གསུངས་ཏེ། སྲིད་པའི་རྒྱུན་མེད་ན་དེ་མི་འཐད་པས་དེའི་ཕྱིར་སྲིད་པའི་རྒྱུན་ནི་ཡོད་པ་ཁོ་ནའོ། །

[Block 2350]
བཤད་པ། གལ་ཏེ་དེ་བཞིན་གཤེགས་པ་ཉིད་འཐད་ན་ནི། སྲིད་པའི་རྒྱུན་ཡང་ཡོད་པར་འགྱུར་གྲང་ན། དེ་བཞིན་གཤེགས་པ་ཉིད་མི་འཐད་པས་དེའི་སྲིད་པའི་རྒྱུན་ཡོད་པར་ག་ལ་འགྱུར། ཇི་ལྟར་ཞེ་ན། འདི་ལ་གལ་ཏེ་དེ་བཞིན་གཤེགས་པ་ཞེས་བྱ་བ་འགའ་ཞིག་ཡོད་པར་གྱུར་ན། དེ་ཕུང་པོ་རྣམས་ཉིད་དམ། ཕུང་པོ་རྣམས་ལས་གཞན་ཞིག་ཡིན་གྲང་ན། དེ་ལ།
--- END BLOCKS ---
