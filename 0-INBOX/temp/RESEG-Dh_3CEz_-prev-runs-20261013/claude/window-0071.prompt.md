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
[Block 2486]
བདེ་ཆེན་ནི་རྒྱུན་མི་འཆད་པར་ཞུ་བ་དང་བཅས་པ་སྟེ་བརྟེན་པའོ། །

[Block 2487]
དེ་ནི་རང་ལུས་ཐབས་སོ། །

[Block 2488]
ཡང་ཨེ་ཝཾ་ཡི་གེར༌[^1075]རབ་ཏུ་གནས་ནི་ནམ་མཁའི་དཀྱིལ་དུ་ཟུག་པའི་ཕྱག་རྒྱ་ཆེན་པོ་སྟེ་རྟེན་ནོ། །

[Block 2489]
བདེ་ཆེན་ནི་ལྷན་ཅིག་པ་འབའ་ཞིག་སྟེ་བརྟེན་པའོ། །

[Block 2490]
དེ་དག་ནི་སྡོམ་པ་བཤད་ནས་ཐབས་བསྟན་པའི་ཕྱིར། དབང་ལས་ཡང་དག་ཤེས་པ་ནི་དགོངས་པའི་སྐད་ལ་སོགས་པ་ཡང་མཚོན་སྟེ་ཡང་དག་ཤེས་པའོ། །

[Block 2491]
དེ་ལ་དབང་ནི་ཕྱི་རོལ་གྱི་སྙོམས་འཇུག་གཞན་ལུས་ལ་བརྟེན་པ་དང་། ནང་གི་སྙོམས་འཇུག་རང་ལུས་ལ་བརྟེན་པ་དང་། ཕྱག་རྒྱ་ཆེན་པོ་གཉིས་མེད་ཀྱི་དབང་ངོ་། །

[Block 2492]
ད་ནི་མཁའ་འགྲོ་མའི་སྡོམ་པ་དེ་ཨེ་ཝཾ་དུ་བྲིས་པ་དེ༌[^1076]ལ་སོགས་པ་གོ་སླའོ། །

[Block 2493]
བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ་ཞེས་པ་ནི་ལན་ནོ། །

[Block 2494]
ཨེའི་ཆ་བྱད་ལ་སོགས་པའི༌[^1077]མཁའ་འགྲོ་མའི་སྡོམ་པ་ནི་བདེ་ཆེན་ཡིན་ལ། དེ་སྡོམ་པ་ནི་གླེང་གཞི་ཨེ་ཝཾ་ཡིན་ཏེ། དེ་དག་གི་བཤད་པ་ཡང་གཞན་ལུས་ཤེས་རབ་ལ་བརྟེན་པ་ལ་སོགས་པ་སྔ་མ་ལྟར་རོ། །

[Block 2495]
ད་ནི་ཐབས་བསྟན༌[^1078]པའི་གོ་རིམས་བཟློག་སྟེ། སྐད་ཅིག་ལ་བསྟན་པ་ཡང་སྐད་ཅིག་དབྱེ་བ་ནི་རྣམ་པ་སྣ་ཚོགས་པ་ལ་སོགས་པ་རྣམས་སོ། །

[Block 2496 [VERSE]]
དབྱེ་བ་ཉིད་ནི་དགའ་བ་རྣམས་སོ། །
དགའ་བ་བདེ་ལས༌[^1079]སྐྱེས་ཞེས་པ་ནི་དེའི་ཕྱིར་རོ། །

[Block 2497]
སྐད་ཅིག་ཤེས་ནས་ཞེས་པ་ནི་སྤོང་བའི་རིམ་པའོ། །

[Block 2498 [VERSE]]
བདེ་ཞེས་པ་ནི་ཐོབ་པའི་རིམ་པའོ། །
དེ་དག་ནི་གང་གིས༌[^1080]སྡོམ་པ། །
ཨེ་ཝཾ་ཡི་གེར་རབ་ཏུ་སྡོམ་པའོ། །

[Block 2499]
རབ་ཏུ་གནས་པ་ནི་བདེ་བ་ཆེན་པོ་རོ་གཅིག་པའོ། །

[Block 2500]
བདེ་བ་མཆོག་ཏུ་སྡོམ་པའོ། །

[Block 2501]
ད་ནི་རྣམ་པ་སྣ་ཚོགས་ལ་སོགས་པ་ནི་གྲངས་དང་མཚན་ཉིད་དང་སྦྱར་ཏེ། འཁྱུད་དང་འོ་བྱེད་ལ་སོགས་པ། །ཞེས་བྱ་བ་ལ་སོགས་པ་ལས་ཀྱི་ཕྱག་རྒྱའི་དགའ་བ་རྣམ་པ་བཞི་ནི་སློབ་དཔོན་ཁ་ཅིག་གསང་གནས་ཀྱི་ཁྱད་པར་རྡོ་རྗེའི་ནོར་བུའི་རྩ་བ་དང་། རྐེད་པ་དང་། བུམ་པར་ཐིག་ལེར་གནས་པ་ལ་འཆད་དོ། །

[Block 2502]
ཁ་ཅིག་ནི་གཉིས་རྡོ་རྗེ་ནོར་བུའི་ཆ་ལ་གནས་གཉིས། པདྨའི་ཆ་ལ་གནས་པ་ལ་ལྷན་ཅིག་སྐྱེས་པའི་དགའ་བ་བརྩིས༌[^1081]ནས་དེའི་རྗེས་ལ་དགའ་བྲལ་འདོད་དོ། །

[Block 2503]
དགོངས་པ་ནི་འདི་ཡིན་ཏེ། འོ་དང་འཁྱུད་པ་ལ་སོགས་པའི་ཀར་ནའི་བྱེ་བྲག་སྣ་ཚོགས་པ་ལ་རྟོག་པ་འདྲེས་མ་ནི་རྣམ་པ་སྣ་ཚོགས་ཀྱི་སྐད་ཅིག་ཅེས་བྱ་སྟེ། དེའི་རྣམ་པར་འཆད་པ་ལ༌[^1082]ཡོངས་སུ་གཅོད་པ་ཡེ་ཤེས་ཀྱི༌[^1083]ཆ་ཅུང་ཟད་ཐོབ་པ་དགའ་བའོ། །

[Block 2504]
རྣམ་པར་སྨིན་པ་དེ་ལས་བཟློག །ཅེས་ཕྱི་རོལ་གྱི་རྟོག་པ་སྤངས་ཏེ་ཤེས་པ་ནང་དུ་ཐིམ་ནས་ཀུན་དུ་རུའི་སྦྱོར་བའི་བར་ནི་སྔ་མ་ལས་ཁྱད་པར་དུ་སྨིན་པས་རྣམ་པར་སྨིན་པའི་སྐད་ཅིག་མའི༌[^1084]ཡོངས་གཅོད་ནི་མཆོག་དགའ༌[^1085]ཡེ་ཤེས་སོ། །

[Block 2505]
གྲོས་ནི་རྣམ་པར་ཉེད་པར་བརྗོད། །ཅེས་པ་ནི་བོ་ལའི་གནས་སུ་ཐིག་ལེ་བྱང་ཆུབ་ཀྱི་སེམས་ཕྱིན་པ་ལ་མི་མཐུན་པའི་རྣམ་པར་རྟོག་པ་སྤངས་ཏེ། གཉེན་པོ་ཡེ་ཤེས་སུ་གྱུར་པ་ནི་རྣམ་པར་ཉེད་པའི་སྐད་ཅིག་མའམ་ཡོངས་སུ་གཅོད་པ་ནི་དགའ་བྲལ་གྱི་ཡེ་ཤེས་སོ། །

[Block 2506]
མཚན་ཉིད་བྲལ་བ་གསུམ་ལས་གཞན། །ཞེས་པ་ནི་དེའི་ཚེ་ཐིག་ལེ་བྱང་ཆུབ་ཀྱི་སེམས་ཟིན་པ་ནི་མི་ཐུན་པའི་ཕྱོགས་ཐམས་ཅད་བྲལ་ཏེ། གཉེན་པོ་ཡེ་ཤེས་འབའ་ཞིག་ཏུ་གནས་པ་ནི་མཚན་ཉིད་བྲལ་བའི་སྐད་ཅིག་མ་རྣམ་པར་བཅད་ནས་ཏེ། ཡོངས་གཅོད་ནི་ལྷན་ཅིག་སྐྱེས་པའི་ཡེ་ཤེས་སོ། །

[Block 2507]
འདི་རྣམས་སྐྱེས་པ་ནི་མན་ངག་ལུས་ཀྱི་འཁྲུལ་འཁོར་དང་། [^1086]རྩའི་འཁྲུལ་འཁོར་གསུམ་ནི་དབང་གི་དུས་སུ་བླ་མ་ལས་ཤེས་པར་བྱའོ། །

[Block 2508]
དེ་བཞིན་དུ་དབང་གི་མན་ངག་ཀྱང་བསྒོམ་པའི་མན་ངག་བླ་མ་ལས་ཤེས་པར་བྱའོ། །

[Block 2509]
གཞན་ཡང་དམ་ཚིག་གི་ཕྱག་རྒྱའི་དགའ་བ་བཞི་དང་། ཕྱག་རྒྱ་ཆེན་པོའི་དགའ་བ་བཞི་དང་། སྐད་ཅིག་མ་བཞི་ཡང་སྤོང་བའི་ཚུལ་ཡང་ཐོབ་པའི་ཚུལ་དུ་ལུགས་ལས་འབྱུང་བ་དང་ལུགས་ལས་བཟློག་པ༌[^1087]ཅི་རིགས་པར་ཤེས་པར་བྱའོ། །

[Block 2510]
ཡང་དག༌[^1088]སློབ་དཔོན་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་སྐད་ཅིག་སྤོང་བའོ། །

[Block 2511]
མཆོག་དགའ་བ་ཐོབ་པའི་ཆ་ལ་འཇུག་པ་བཞིན་དུ་དབང་དབྱེར་མེད་ལ་འཇུག་པ། །དབྱེ་བའི་གྲངས་དང་སྦྱར་བ་བསྟན་པ་དང་། མཚན་ཉིད་དཔེ་ལས་བཤད་པ་སྟེ། དེ་དག་ཀྱང་ཅིའི་ཕྱིར་བཞི་རུ་གྲངས་ངེས་ཤེ་ན་འཇིག་རྟེན་པ་ལ་དགོད་པ་དང་ལྟ་བ་དང་ལག་བཅང༌[^1089]ལ་སོགས་པ་བཞིར་བསྡུས་པས། དེ་སྦྱང་བའི་དོན་དུ་རྒྱུད་རྣམ་པ་བཞིར་བསྟན་ལ། དབང་ཡང་རྣམ་པ་བཞི་རུ་བསྟན་ཏོ། །

[Block 2512 [HEADING]]
#### ངེས་ཚིག་བསྡུ་བ། ^2-3-1-0

[Block 2513 [VERSE]]
ད༌[^1090]ནི་ངེས་ཚིག་བསྡུ་བ་སྟེ། །
གཏོར་དང་བླུགས་པ་ཞེས་བྱ་འདིས། །

[Block 2514]
དབང་ཞེས་མངོན་པར་བརྗོད་པར་བྱ།

[Block 2515]
དང་པོ་ལ་བུམ་པའི་དབང་ངམ་སློབ་དཔོན་གྱི་དབང་ཞེས་བྱ་བ་ནི། ཨ་བྷི་ཥིཉྩ་དྲི་མ་འཁྲུད་པས༌[^1091]ན་དབང་སྟེ་ལུས་ཀྱི་དྲི་མ་འཁྲུད་པར་བྱེད། བུམ་པས་ཉེ་བར་མཚོན་པས་བུམ་པའི་དབང་ཞེས་བྱ། སྡིག་པ་མི་དགེ་བ་ལས་རིང་དུ་འགྲོ་བས་ན་སློབ་དཔོན་གྱི་དབང་ཞེས་བྱ། མ་རིག་པ་ལྔ་བཟློག་ཅིང་རིག་པའི་ཡེ་ཤེས་ལྔ་བསྐྱེད་པའི་ཕྱིར་རིག་པའི་དབང་ཞེས་བྱ། ཨ་བྷི་ཥེ་ཀ་སྟེ་ནུས་པ་འཇོག་པ་ནི་སྤྲུལ་པའི་སྐུའི་ནུས་པ་འཇོག །བསྐུར་བའི༌[^1092]གནས་ནི་ལུས་ལ་བསྐུར་ལ། དབང་རྫས་ནི་བུམ་པ་དང་དབུ་རྒྱན་ལ་སོགས་པའོ། །

[Block 2516]
གསང་བའི་དབང་ལ་ཨ་བྷི་ཥིཉྩ་སྟེ་ཉོན་ཐོས་དང་རང་སངས་རྒྱས་རྣལ་འབྱོར་གྱི་རྒྱུད་མན་ཆད་ལ་གསང་བས་ན་གསང་བའི་དབང་ཞེས་བྱའོ། །

[Block 2517]
ངག་གི་དྲི་མ་འཁྲུ་བས་ན་དབང་ཞེས་བྱའོ། །

[Block 2518]
ཨ་བྷི་ཥེ་ཀ་སྟེ་ལོངས་སྤྱོད་རྫོགས་པའི་སྐུའི་ནུས་པ་འཇོག་པའོ། །

[Block 2519]
བསྐུར་བའི་གནས་ནི་མགྲིན་པར་བསྐུར་ལ། བསྐུར་བའི་རྫས་ནི་སློབ་དཔོན་གྱིས་ཉམས་སུ་མྱོང་བའི་ཐིག་ལེ་བྱང་ཆུབ་ཀྱི་སེམས་སོ། །ཤེས་རབ་ཡེ་ཤེས་ཀྱི་དབང་ནི་ཤེས་རབ་མ་ལ་བརྟེན་ནས་ཡེ་ཤེས་སྐྱ་བར་བྱེད་པས་ན་ཤེས་རབ་ཡེ་ཤེས་ཀྱི་དབང་ཞེས་བྱའོ། །

[Block 2520]
ཨ་བྷི་ཥིཉྩ་སྟེ་ཡིད་ཀྱི་དྲི་མ་འཁྲུ་བར་བྱེད་དོ། །

[Block 2521]
ཨ་བྷི་ཥེ་ཀ་སྟེ་ཆོས་ཀྱི་སྐུའི་ནུས་པ་འཇོག་པར་བྱེད་པས་དབང་ཞེས་བྱའོ། །

[Block 2522 [VERSE]]
གནས་གང་དུ་བསྐུར་ན་གསང་བའི་གནས་སུ་བསྐུར་རོ། །
བསྐུར་བའི་རྫས་ནི་ཕྱག་རྒྱ་མ༌[^1093]མཚན་དང་ལྡན་པའོ། །

[Block 2523]
དབང་བཞི་པ་ནི་དེ་ལྟར་དེ་བཞིན་ཡང་བཞི་པ་ཞེས་པ་ནི་གསུམ་པས་གོ་ཕྱེ་བའི་ཚིག་དབང་རིན་པོ་ཆེ་སྟེ། ཨ་བྷི་ཥིཉྩ་སྟེ་ལུས་དག་ཡིད་གསུམ་གྱི་བག་ལ་ཉལ་གྱི་དྲི་མ་འཁྲུད་པར་བྱེད་དོ། །

[Block 2524]
ཨ་བྷི་ཥེ་ཀ་སྟེ་བདེ་བ་ཆེན་པོའི་སྐུའི་ནུས་པ་འཇོག་པར་བྱེད་དོ། །

[Block 2525]
བསྐུར་བའི་གནས་ནི་ལུས་ངག་ཡིད་གསུམ་ཆར་ལའོ། །
--- END BLOCKS ---
