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
[Block 2241]
དགྱེས་པའི་རྡོ་རྗེའི་ང་རྒྱལ་གྱིས། །ཞེས་བྱ་བའི༌[^972]ཐ་ཚིག་གོ། །

[Block 2242]
འོ་ན་སྤྱོད་པ་ནི་སྒོ་གསུམ་གྱི་བདག་ཉིད་ཅན་ཡིན་ལ། གསང་བའི་སྤྱོད་པ་ནི་གྲོགས་དང་བཅས་པ་ཡིན་པས་བརྟན་པ་འཐོབ༌[^973]ན་གང་དང་འགྲོགས་ཤེ་ན། སྤྱོད་པའི་སྒོ་གསུམ་ནི་ལེའུ་དྲུག་པ་ལྟར་ཤེས་པར་བྱའོ། །

[Block 2243]
གསལ་བའི་སྤྱོད་པའི་གྲོགས་ནི་གཉིས་ཏེ་ཞིང་སྐྱེས་མ་དང་ལྷན་སྐྱེས་མའོ། །

[Block 2244]
བརྟན་པ་མ་ཐོབ་ཀྱི་བར་དུ་ལྷན་སྐྱེས་མ་དང་འགྲོགས་ཏེ་སྤྱོད་པའོ། །

[Block 2245]
ལྷན་སྐྱེས་མའི༌[^974]དེ་ཉིད་བསྟན་པའི་ཕྱིར། རྙེད་པ་དེ་ཡང་མིག་ཡངས་མ། །ཞེས་བྱ་བ་ལ་སོགས་པ་ཚིགས་སུ་བཅད་པ་གཉིས་ཏེ། རང་བཞིན་གྱི་ཡོན་ཏན་དང་སྦྱངས་པའི་ཡོན་ཏན་དང་ལྡན་པ་སྟེ། རང་བཞིན་གྱི་ཡོན་ཏན་ནི་བྱད་གཟུགས་དང་ལང་ཚོ་དང་རིགས་ཀྱི་ཡོན་ཏན་ནོ། །

[Block 2246]
སྦྱངས་པའི་ཡོན་ནི། དགེ་བ་བཅུ་ནས་བརྩམས་ནས་ནི། །ཞེས་པ༌[^975]ལ་སོགས་པ་སེམས་བསྐྱེད་པ་དང་སྡོམ་པ་དང་དམ་ཚིག་སྦྱིན་པ་དང་། དབང་བསྐུར་ནས་ལྷ་བསྒོམ་པ་དང་ལྡན་པར་བྱའོ། །

[Block 2247]
ད་ནི་ཡང་ན་ཡིད་སྐྱེས་དང་ལྷན་ཅིག་འགྲོགས་པ་བསྟན་པའི༌[^976]ཕྱིར། ཟླ་བ་གཅིག་ནི་སྔོན་དུ་དེ་ཉིད་སྒྲུབ་པའི་དོན་དུའོ། །

[Block 2248]
སྐལ་ལྡན་ཐེ་ཚོམ་མེད་ནི་སྤྱོད་པའི་གྲོགས་ནུས་པར་རོ། །

[Block 2249]
མཆོག་ཐོབ་ནི་ཡིད་ལས་བྱུང་བའི་ཆོས་ཀྱི་ཕྱག་རྒྱ་གསུངས་པའི་ཕྱིར་རོ། །

[Block 2250]
བུད་མེད་ནི་འདོད་པའི་བུད་མེད་འདྲ་བས་སོ། །

[Block 2251]
རྟོག༌[^977]ཀུན་ཡང་དག་སྤོང་བ་ནི་དེ་ལྟར་བརྟེན་པའི་ཡོན་ཏན་ནོ། །

[Block 2252]
དེས་ནི་ཅུང་ཟད་སྨྱོན་པའི་བརྟུལ་ཞུགས་ཀྱི་གྲོགས་བསྟན་ཏོ། །

[Block 2253]
དེ་སྐད་དུ་ཡང་། སྙིང་ལ་གནས་པའི་ལྷ་མོ་ཆེ། །ཡོན་ཏན་ཐམས་ཅད་སྐྱེད༌[^978]པའོ། །ཞེས་གསུངས་སོ། །

[Block 2254]
འདིའི་སྤྱོད་པའི་ལྡང་ཚད་ཀྱང་ལེའུ་དྲུག་པ་རུ།

[Block 2255 [VERSE]]
ཅང་ཏེའུའི་སྒྲ་ནི་བཟླས་པ་སྟེ། །
ཞེས༌[^979]བྱ་བ་ལ་སོགས་པ་འདིར་སྦྱར་རོ། །

[Block 2256]
ད་ནི་སྔགས་སྐྱེས་དང་སྤྱོད་པ་བསྟན༌[^980]པའི་ཕྱིར། ཡང་ན་ཕྱོགས་གཞན་ཏེ་སྔར་གྱི་དག་ལ་ཡང་ངོ་། །བདག་གི་ནུས་པ་ནི་སྒོམ་པ་དང་སྔགས་ཀྱིས་སོ། །

[Block 2257]
ལྷ་དང་ལྷ་མིན་ལ་སོགས་པ་དགུག་པ་ནི་ཏིལ་མཆོག་མ་དག་གོ། །

[Block 2258]
ཁྱེར་ལ་སྤྱད་ནི་སྔ་མ་ལྟར་རོ། །

[Block 2259]
འདིས་ནི་སྨྱོན་པའི་བརྟུལ་ཞུགས་ཆེན་པོའི་གྲོགས་གང་ཡང་རུང་བ་དང་འགྲོགས་སམ་གྲོགས་བྱེད་པར་འགལ་བ་མེད་དོ། །

[Block 2260]
འདིའི་སྤྱོད་པའི་རྒྱུ་མཚན་ཡང་། ཨཱ་ལི་ཀཱ་ལིར་རབ་བརྟགས༌[^981]པས། བརྗོད་པ༌[^982]བཟླས་པར་ཡང་དག་བཤད། །ཅེས་བྱ་བ་ལ་སོགས་པ་ལེའུ་དྲུག་པ་ལྟར་ཤེས་པར་བྱའོ། །

[Block 2261]
ད་ནི་ཐ་མལ༌[^983]དགག་པའི་ཕྱིར་བདག་གི་དཀྱིལ་འཁོར༌[^984]བསྟན་པ་ནི་ཏིང་ངེ་འཛིན་ནོ། །

[Block 2262]
མངོན་དུ་ནི་པྲ༌[^985]ཏ་ཡ་སྟེ་རྐྱེན་ནམ་ཡིད་ཆེས་སུ་ཡང་ངོ་། །གང་བཤད་ནི་ཐབས་དང་ཤེས་རབ་གཉིས་མེད་དང་ལྡན་པའོ། །

[Block 2263]
འཇིགས་པའི༌[^986]གཟུགས་སམ་ཚུལ་ནི་ཧེ་རུ་ཀ་དང་བདག་མེད་པའི་ང་རྒྱལ་གྱིས་སོ། །

[Block 2264]
སྤྱོད་པ་ལོངས་སྤྱོད་ཕྱིར༌[^987]ཞེས་པ་ནི་ཐ་མལ་གྱི་གྲོགས་སོ། །

[Block 2265]
སྤྱོད་པ་མ་གསུངས་པ་ནི་ཐ་མལ་ལམ་ལྟོ་དགང་བའི་དཔུང་གཉེན་ནོ། །

[Block 2266]
དེ་སྐད་དུ་ཡང་ཀྱེ་བཅོམ་ལྡན་འདས་གལ་ཏེ་སིཧླ་ལ་སོགས་པ་དེ་ཟོས་ན་ཇི་ལྟར་མི་གཙང་བར་མི་འགྱུར། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ།

[Block 2267 [VERSE]]
ཕོ་ཉ་གཙང་སྦྲ་དང་པོ་སྟེ། །
གཉིས་པ་ཞི་བའི་བཏུང་བ་ཡིན། །
སྣོད་གཅིག་ཏུ་ནི་ཟས་ཟ་བ། །
གཙང་སྦྲ་གསུམ་པ་ཡིན་པར་བརྗོད། །

[Block 2268 [VERSE]]
རྣལ་འབྱོར་ཕྱི་རོལ་ལ་དགའ་བ། །
སྦྲང་རྩི་འདི་ནི་བརྩམ་པར་བྱ། །
རང་སེམས་དྲི་མ་ཅན་འགྱུར་ན། །
གཙང་སྦྲ་འདི་ཡིས་ཅི་ཞིག་བྱ། །

[Block 2269 [VERSE]]
འདོད་དོན་ཐམས་ཅད་སྒྲུབ་བྱེད་པའི། །
མི་མཐུན་ཆོས་རྣམས་གང་ཞིག་དང་། །
ཟས་དང་ལོངས་སྤྱོད་ཕྱིར་བྱས་ན། །
ཁྱི་ཡི་སྐྱེ་གནས་བརྒྱར་སྐྱེ་ཞིང་། །

[Block 2270 [VERSE]]
སྨེ༌[^988]ཤ་ཅན་དུ་སྐྱེ་བར་འགྱུར། །
དཔེར་ན་ལ་ལ་མར་འདོད་པས། །
འབད་པས་ཆུ་ནི་བསྲུབས་གྱུར༌[^989]ཀྱང་། །
མར་སར་འབྱུང་བར་མི་འགྱུར་གྱི། །

[Block 2271 [VERSE]]
ལུས་ཉོན་མོངས་པ་ཁོ་ནར་ཟད། །
འཚོ་བའི་ཐབས་ཀྱི་རྒྱུར་འགྱུར་བ། །
འཛིན་ཅིང་མཆོད་པར་བྱེད་པ་ཡི། །
རྣལ་འབྱོར་གཞན་ལ་བརྟེན་པ་ཡང་། །

[Block 2272]
དེ་བཞིན་ངལ་བ་དོན་མེད་འགྱུར། །ཞེས་གསུངས་པ་དང་།

[Block 2273 [VERSE]]
དེ་ཁོ་ན་ཉིད་ཀྱི་དོན་དང་ལྡན་ན། །
དུང་དང་ཉ་ཕྱིས་མུ་ཏིག་སྟེ། །
གསུམ་ཀ་རྒྱུ་ལས་བྱུང་ཡིན་ན། །
ཆོས་ཀྱི་ཡེ་ཤེས་ལུས་ཅན་གྱི། །

[Block 2274]
ཐོད་པ་ལ་ནི་སུ་ཞིག་སྨོད། །ཅེས་གསུངས་སོ། །

[Block 2275]
ད་ནི་བསམ་པའི་ཁྱད་པར་ཡང་། ཡིད་ནི་བརྟན་ནམ་གཡོ་ཞེས་བྱ་བ་ནི་བསྐྱེད་པའི་རིམ་པ་སྤྱིའི་མཚན་ཉིད་ཙམ་མོ། །

[Block 2276]
རང་གི་སེམས་བརྟན་པ་ནི་ཡིད་མི་གཡོ་བར་རོ། །

[Block 2277]
རྡོ་རྗེ་སྙིང་པོས་གསོལ་ཞེས་པ་ནི་གཞན་ལ་ཇི་ལྟར་རིགས་པའོ། །

[Block 2278]
བདག་མེད་རྣལ་འབྱོར་ནི་བདག་མེད་པར་བསྒོམས་པར༌[^990]ལྡན་པའི་བུད་མེད་དོ། །

[Block 2279]
ཕྱག་རྒྱ་ཉིད་ཅེས་ཇི་ལྟར་ཞེས་པ༌[^991]ནི་སྤོང་བ་སྟེ། རང་ཉིད་ཕྱག་རྒྱ་ཡིན་ན། དེའི་རྒྱུ་མཚན་བསྟན་པའི་ཕྱིར་ཕྱག་རྒྱ་ནི་རང་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2280]
ཕྱག་རྒྱ་གཉིས་ནི་ཡང་ཕྱག་རྒྱ་ལ་བརྟེན་པའི་དངོས་གྲུབ་ཇི་ལྟར་འགྱུར་ཞེས་པ་ནི་ཐབས་ལ་མ་བརྟེན་པས་སྤོང་བའི་སྒྲའོ། །
--- END BLOCKS ---
