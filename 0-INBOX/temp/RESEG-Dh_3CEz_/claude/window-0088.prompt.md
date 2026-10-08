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
[Block 3081]
ཞེས་གསུངས་ཏེ་འཁོར་རྗེས་སུ་མཐུན་པའི་བྱང་ཆུབ་པ་ལྔས༌[^1257]མངལ་སྐྱེས་ཀྱི་སྒོང་སྐྱེས་དང་འདྲ་བར་བསྐྱེད་དེ། གཾ་ཙཾ་ལ་སོགས་པ་ཚིག་གཉིས་སྦྱར་རོ། །

[Block 3082]
དེའི༌[^1258]དོན་ནི་སྙིང་ག་ནས་འོད་འཕྲོས་སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་བཀུག་ནས་ཞལ་དུ་ཞུགས། སྙིང་གར་ཞུ། སྲོག་དག་པའི་ལམ་ནས་བྱུང་སྟེ། ཡུམ་གྱི་པདྨར་ཐིག་ལེ་དེ་ལས་ས་བོན་བརྒྱད་དུ་གྱུར་པ་དང་། མདུན་གྱི་ཚངས་པའི་གདན་སྟེང་དུ་ཨཱ་ལི་ལས་ཟླ་བ་ཀཱ་ལི་ལས་ཉི་མ་དེའི་བར་ན༌[^1259]གཾ །དེ་ལས་གྲི་གུག །[^1260]དེ་སྤྲོ་བསྡུ་བྱས་ནས་ཞུ་བ་ལས་གཽ་རཱི་བསྐྱེད་དེ།

[Block 3083 [VERSE]]
དཀར་མོ་དབང་པོའི་ཕྱོགས་ཕྱུང་ནས། །
ཞེས་བྱ་བ་ལ་སོགས་པ་སྦྱར་རོ། །
རླུང་གི་མཚམས་སུ་གཡུང་མོ་ནི། །

[Block 3084]
ཞེས་པའི་མཐར་ཏེ། རླུང་མཚམས་ནི༌[^1261]ཉི་མའི་སྟེང༌[^1262]ན་ཐགས༌[^1263]བཟངས་རིས་མནན་པའི་སྟེང་དུ་ཨཱ་ལི་ལས༌[^1264]ཟླ་བ་ཀཱ་ལི་ལས་ཉི་མ། དེ་གཉིས་བར་དུ་ཌཾ་དེ་ལས་རྡོ་རྗེ་ལ་ཌཾ་གིས་མཚན་པ་དེ་སྤྲོས་བསྡུས་ནས་ཞུ་བ་ལ་གཡུང་མོ་བསྐྱེད་དོ། །

[Block 3085]
གཞན་ལ་ཡང་དེ་བཞིན་སྦྱར་རོ། །

[Block 3086]
དེ་སྐད་དུ།

[Block 3087 [VERSE]]
ཟླ་བ་ཉི་མའི་རབ་དབྱེ་བས། །
དཀར་མོ་ལ་སོགས་རབ་ཏུ་གྲགས། །

[Block 3088]
ཞེས་གསུངས་སོ། །

[Block 3089]
དེ་ལྟར་འཁོར་བསྐྱེད་ནས་གཙོ་བོ་འགྱུར་བ་ནི། དེ་ནས་རྡོ་རྗེ་ཆགས་ཆེན་ལས། །

[Block 3090]
རིག་མ་བཅས་པར་ཞུ་བར་འགྱུར།[^1265] །ཞེས་པ་སྟེ། རྒྱུའི་འགྱུར་བ་ནི་སྔར་གྱི་ཐིག་ལེ་བྱང་ཆུབ་སེམས་དཔའ་འབྲུ་ལྔར་གྱུར་པ་དེ་གཙོ་བོའི་ཞལ་དུ་ཞུགས་པས་གཙོ་བོ་དང་རིག་མར་བཅས་པ་ཞུའོ། །

[Block 3091 [VERSE]]
དེ་ནས་རྐྱེན་གྱིས་འགྱུར་བ་ནི། །
སྣ་ཚོགས་གླུ་ཡི་མཆོད་པ་ལས། །
དེ་ནས་ལྷ་མོ་རྣམས་ཀྱིས་བསྐུལ། །

[Block 3092]
ཞེས་པ་སྟེ་མཚམས་ཀྱི་ལྷ་མོས་བསྐུལ་ཏེ་ཆོས་ཅན་རྣམ་པར་དག་པ་འབྱུང་བ་བཞིས་འབྲས་བུ་བསྐྱེད་པ་དང་། ངོ་བོ་ཚད་མེད་པ་བཞེས༌[^1266]སེམས་ཅན་གྱི་དོན་བྱེད་པ་དང་ལས་སོ་སོར་ངེས་པ་སྟེ། མཚམས་མས་སློང་བའི་ལས་དང་། སྒོ་མས་ཡེ་ཤེས་ཀྱི་འཁོར་ལོ་དགུག་པ༌[^1267]ལ་སོགས་པའོ། །

[Block 3093]
རྗེ་བཙུན་ཞེས་བྱམས་པ་ཆེན་པོ་པུཀྐ་སཱིའི་གླུ་སྟེ་སྲི་ཞུས་བོད་པའོ། །

[Block 3094]
སྙིང་རྗེའི་ཡིད་ཀྱིས་བཞེངས་ཤིག་པ་སྟེ་ཐིག་ལེ་ལས་བསྐུལ་བའོ། །

[Block 3095]
པུཀྐ་སཱི་ནི་བདག་ལ་སྐྱོབས༌[^1268]ནི་སེམས་ཅན་གྱི་དོན་མཛོད་ཅིག་པའོ། །

[Block 3096]
སྟོང་པའི་རང་བཞིན་ཉིད་སྤོངས་ལ་ནི་ཐིག་ལེ་སྟོང་པ་དང་འདྲ་སྟེ་གཞན་དོན་མི་ནུས་པའོ། །

[Block 3097]
བདག་ལ་བདེ་ཆེན་སྦྱོར༌[^1269]ནི་གཞན་དོན་ལ་བསྐུལ་བ་སྟེ་གཞན་བདེ་བས་བདག་བདེ་བའོ། །

[Block 3098]
ཁྱོད་མེད་ན་ནི་བདག་འགུམ་པས། །ཞེས་པ་སྙིང་རྗེ་ཆེན་པོ་ཤ་བ་རཱིའི་གླུ་སྟེ་བདག་གི་སྲོག་སྙིང་རྗེས་གཞན་དོན་མེད་ན་སྙིང་རྗེ་མེད་པ་བདག་འགུམ་པ་ཞེས་པའོ། །

[Block 3099 [VERSE]]
ཀྱེའི་རྡོ་རྗེ་ཞེས་བོད་པའོ། །
སྟོང་པ་སྔ་མ་དང་འདྲའོ། །

[Block 3100]
རི་ཁྲོད་མ་འབྲས་བསྒྲུབ་པ་ནི་གཞན་དོན་མཛོད་ཅིག་པའོ། །

[Block 3101]
དགའ་གཙོ་ཞེས་པ་ནི་དང་བའི་དགའ་བའི་གླུ་སྟེ། ཁྱེད་དང་པོ་སེམས་བསྐྱེད་ཙམ་ན་སེམས་ཅན་མགྲོན་དུ་བོས་ནས་ད་སྟོང་པ་ལ་ཅིའི་ཕྱིར་བཞུགས་ཞེས་བྱའོ། །

[Block 3102]
འོ་ན་རང་གིས་གཞན་དོན་བྱས་མོད་ཅེ་ན། ཁྱོད་མེད་ན་ནི་ཕྱོགས་མི་ཁུམས། །ཞེས་པ་སྟེ་བདག་གི་དོན་མི་ཤེས་པར་དགོངས་པའོ། །

[Block 3103]
དེའི་ཕྱིར་བདག་ཞུ་བར་བགྱིད་པའོ། །

[Block 3104]
མིག་འཕྲུལ་ལྟ་བུར་ཞེས་བྱ་བ་ཤློ་ཀ་གཅིག་སྦྱར་ཏེ། བཏང་སྙོམས་གཡུང་མོའི་གླུ་སྟེ། ཁྱེད་སྤྲུལ་པ་ལྟ་བུ་སྒྱུ་མ་ལྟ་བུ་མངའ་བ་སྟེ་དེ་ཅིའི་ཕྱིར་ཞེ་ན། བདག་གིས་ཁྱེད་ཀྱི་ཐུགས་འཚལ་ཞེས་པའོ། །

[Block 3105]
དེའི་འཐད་པ་གཡུང་མོ་བདག་ཉིད་དྲན་ཉམས་ནི་གྲོང་ཁྱེར་ཆེན་པོའི་མི་ཞེས་བྱ་སྟེ། སྙིང་རྗེ་རྒྱུན་ཆད་མ་མཛད་ནི་ཐིག་ལེ་སྤོངས་ཞེས་བྱའོ། །

[Block 3106]
དེའི་རྗེས་སུ། ཨཾ་དང་ཧཱུཾ་གིས་རྡོ་རྗེ་ཆེ། ཞེས་བྱ་བ་ཤློ་ཀ་གཅིག་སྦྱར་ཏེ་འབྲས་བུ་ཧེ་རུ་ཀར་བཞེངས་པ་ནི་རྫུས༌[^1270]སྐྱེས་དང་མཐུན་པ། ཡུད་ཙམ་གྱིས༌[^1271]མངོན་པར་བྱང་ཆུབ་པ་བསྐྱེད་དེ། བདག་པོ་ས་བོན་དག་གིས་ནི་ཚིག་གཉིས་སྦྱར་ཏེ། ཐིག་ལེ་དེ་ཆ་གཉིས་ལས་འོག་ཟླ་བ་མེ་ལོང་ལྟ་བུ་སྟེང་ཉི་མ་མཉམ་པ་ཉིད་དེ། བར་དུ་ཡི་གེ་ཨཾ་དང་ཧཱུཾ་ལས་རྡོ་རྗེ་ཆེན་པོ་སྟེ། གྲི་གུག་དེ་ལས་ས་བོན་གྱིས་མཚན་མ་ནི་སོ་སོར་རྟོག་པའི་ཡེ་ཤེས་དེ་ལས་སྤྲོ་བ་དང་བསྡུས་ནས་ཞུ་བ་ནི་བྱ་བ་ནན་ཏན་ནོ། །

[Block 3107]
དེ་ལས་སྐུར་བཞེངས་པ་ནི་ཆོས་ཀྱི་དབྱིངས་ཀྱི་ཡེ་ཤེས་སོ། །

[Block 3108]
དེའི་མོད་ལ་ཞབས་རྣམས་ས་ལ་བརྡབས་པ་ལ་སོགས་པར་གྱུར་ཏོ། །

[Block 3109]
འདིར་ཐིག་ལེ་གཉིས་བྱས་ལ་ཡུམ་ཡང་འགྲན་ཐུབ་ཏུ་བསྐྱེད་དེ་བདག་མེད་མ་གཙོ་བོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3110]
ཞལ་བརྒྱད་པ་ལ་ཞབས་བཞི་ཞེས་སྦྱར་ཏེ་རྣམ་དག་ཕལ་ཆེར་སྔར་བཤད་དོ། །

[Block 3111]
སྣ་ཚོགས་རྡོ་རྗེ་ནི་མི་བསྐྱོད་པའི་རིགས་མཚོན་པའོ། །

[Block 3112]
ཐལ་བས་ལུས་ལ་བྱུགས་པ་ནི་དྲུག་པ་རྡོ་རྗེ་འཆང་གི་དག༌[^1272]པའོ། །

[Block 3113]
དབའ་རླབས་མེད་པའི་བདེ་བ་ཞེས་པ་ལྷན་ཅིག་སྐྱེས་པའི་ངོ་བོའོ། །

[Block 3114]
དེའི་རྗེས་ལ་གླང་པོ་རྟ་བོང་ཞེས་སྦྱར་ཏེ། གློ་དང་དབུགས་དང་དེ་བཞིན་སྨྱོ། །ཁྲག་སྐྱུག༌[^1273]མཛེ་དང་བིརྫི༌[^1274]ཀ །

[Block 3115 [VERSE]]
མཆེར་པ་མཆིན་པར༌[^1275]རང་གཟུགས་ནི། །
གོ་རིམས་བཞིན་དུ་སྤོང་ཕྱིར་རོ། །
ཕྲ་བ་ཡང་བ་མཆོད་པར་བསྟན། །
བདག་པོར་གྱུར་པར་བདག་ལྡན་པ། །

[Block 3116 [VERSE]]
གང་ཡང་ཕྱིན་ཅིང་འདོད་དགུར་ལྡན། །
དགའ་མགུར་སྤྱོད་པ་བདེ་བས་སོ། །

[Block 3117]
དེ་སྐད་དུ་ཡང་།

[Block 3118 [VERSE]]
འགྲོ་བ་རྣམས་ཀྱི་ནང་ན་ནི། །
མི་རྣམས་ཀྱི་ནི་འགྲོ་བ་མཆོག །
དེ་རྣམས་ནད་ནི་ཞི་དོན་དུ། །
གླང་པོ་ལ་སོགས་འཛིན་པ་ནི། །

[Block 3119]
ཉིད་ཀྱི་སྐུ་ལ་ཟློག་པར་མཛད། །ཅེས་པའོ། །

[Block 3120 [VERSE]]
སྒེག་ཅིང་དཔའ་བ་མི་སྡུག་པ། །
རྒོད་ཅིང་དྲག་ཤུལ་འཇིགས་སུ་རུང་། །
སྙིང་རྗེ་རྔམ་དང་ཞི་བ་ཡི། །
གར་དགུའི་རོ་དང་ལྡན་པ་ཉིད། །
--- END BLOCKS ---
