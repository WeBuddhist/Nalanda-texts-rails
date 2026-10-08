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
[Block 2031]
དབུགས་དང་སྦྱར་ཏེ་ལྟུང་བ་ནི་དབབ་པའི་ཐབས་སོ།[^893] །དབང་ནི་སྒྱེལ་བའོ། །

[Block 2032]
དགུག་པ་ནི་ཟློག་པའོ། །

[Block 2033 [VERSE]]
རེངས་པ་ནི་ནམ་མཁའི་དཀྱིལ་འཁོར་དུ་བཟུང་བའོ། །
དེ་དག་སོ་སོར་གཙོར་གང་ལ་བརྟེན་ཞེ་ན།
རློན་པའི་ཤིང་ནི་ཆོས་ཀྱི་ཕྱག་རྒྱའམ་ཡིད་སྐྱེས་སོ། །
མེ་ཏོག་ནི་དམ་ཚིག་གམ་ཞིང་སྐྱེས་སོ། །

[Block 2034 [VERSE]]
རྡོ་རྗེའི་ཤིང་ནི་ཕྱག་རྒྱ་ཆེན་པོའམ་སྔགས་སྐྱེས་སོ། །
གཡོ་བཅས་ནི་ལས་ཀྱི་ཕྱག་རྒྱའམ་ལྷན་སྐྱེས་སོ། །

[Block 2035]
ཟླ་བ་དྲུག་གོམས་པའི་སྦྱོར་བ་ནི་དབང་གི་ཚེ་བསྙེན་པའི་དུས་ཡིན་ལ། ། སྤྱོད་པའི་དྲོད་སྐྱེས་པའི་དུས་སོ། །

[Block 2036]
ཡང་འཁྲུལ་བ་མི་བྱ་བ༌[^894]ནི་ཐེ་ཚོམ་ཡིད་གཉིས་མི་བྱའོ། །

[Block 2037]
འདི་ལ་ཞེས་པ་ནི་ཕྱག་རྒྱའམ་རྣལ་འབྱོར་མ་དག་ལས་བསྒྲུབ་པས་སོ། །

[Block 2038]
སངས་རྒྱས་རྫུ་འཕྲུལ་བསམ་མི་ཁྱབ་ནི་ལྷན་ཅིག་སྐྱེས་པའི་སྡོམ་པ་རང་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2039]
ད་ནི༌[^895]བདག་གི་དོན་དུ་བསྒྲུབས་ནས་གཞན་དོན་ཇི་ལྟར་བྱ་ཞེ་ན། ལྟ་སྟངས་བཞི་པོ་བསྒྲུབ་ཅེས་པ་ནི་རླུང་ལ་སོགས་པ་ལ་ཡང་ངོ་། །

[Block 2040 [VERSE]]
མཁས་པ་ནི་བདག་མེད་མ་སྟེ་ཤེས་རབ་བོ། །
སེམས་ཅན་འཇུག་ནི་སྙིང་རྗེ་ཐབས་སོ། །

[Block 2041]
འོ་ན་སྙིང་རྗེ་འཇུག་པ་ཡིན་ན་རེངས་པ་ལ་སོགས་པ་གནོད་པར་མི་འགྱུར་རམ་ཞེ་ན། དེ་ཕྱིར་གསད་པ་ནི་མཱ་ར་ཎ་སྟེ། བརྡེག་པ་ཡང་མ་ཡིན་པའོ། །

[Block 2042]
དམ་ཚིག་ནི་ཞེ་སྡང་དག་པ་སྙིང་རྗེ་སྟེ་དེ་དང་བྲལ་བའི་ཕྱིར་རོ། །

[Block 2043]
འོ་ན་ཡང་གསད་པ་མ་ཡིན་ན། རེངས་པ་ལ་སོགས་པ་གནོད་དོ་ཞེ་ན། དེའི་ཕྱིར་སེམས་ཅན་སླུ་བ་ནི་གཞན་གྱི་དོན་ཀྱང༌[^896]སྤངས་པའོ། །

[Block 2044]
བྱ་བ་མ་ཡིན་ན་ནི༌[^897]ཁ་ན་མ་ཐོ་བར་གྲགས་ཀྱང་ངོ་། །ཐམས་ཅད་བྱ་ནི་མི་གནོད་པར་བྱེད་པའོ། །

[Block 2045]
སེམས་ཅན་གནོད་པ་ཙམ་ཞེས་པ་ནི་གནོད་པ་ཆུང་ཡང་ཉས་པར་འགྱུར་བའོ།[^898] །ཕྱག་རྒྱའི་དངོས་གྲུབ་མི་རྙེད་ཅེས་པ་ནི་གགས་བྱེད་པའི་ཕྱིར་རོ། །

[Block 2046]
ཡང་རྫོགས་པའི་རིམ་པ་བཤད་པ་ནི༌[^899]ལྟ་སྟངས་དབབ་པ་ལ་སོགས་པའི་མན་ངག་གོ། །

[Block 2047]
བཞི་པོ་སྒྲུབ་པ་ནི་ཕྱག་རྒྱ་དང་རྣལ་འབྱོར་མ་ལའོ། །

[Block 2048]
མཁས་པ་ནི་གཟུང་བ་ལ་སོགས་པའི་མན་ངག་གོ། །

[Block 2049]
སེམས་ཅན་འཇུག་པ་ནི་རྡོ་རྗེ་འཛིན་པ་སྟེ་ནུས་པ་དང་ལྡན་པས་སོ། །

[Block 2050]
གསད་པ༌[^900]མ་ཡིན་པ་ནི་ལྷན་ཅིག་སྐྱེས་པ་གཉིས་དང་མི་འབྲལ་ལོ། །

[Block 2051]
ཉམས་པ་ནི་བྲལ་བའོ། །

[Block 2052]
དམ་ཚིག་ནི་ཚུལ་ཁྲིམས་ཏེ་ཚངས་པར་སྤྱོད་པའོ། །

[Block 2053]
ཡང་དམ་ཚིག་ནི་སྡོམ་པ་སྟེ། རྣལ་འབྱོར་པའི་སྲོག་གོ། །

[Block 2054 [VERSE]]
དེའི་ཕྱིར་མི་འབྲལ་བར་བྱ་བ་ཁོ་ནའོ། །
སེམས་ཅན་སླུ་བ་ནི་དབང་པོ་རང་སྣང་དང་བྲལ༌[^901]བའོ། །
ཡང་ནི་སྣང་བ་ལྷན་ཅིག་སྐྱེས་པར་སྦྱར་རོ། །

[Block 2055]
བྱ་བ་མ་ཡིན་ཐམས་ཅད་བྱ་བ་ནི་སྤྱོད་པ་ཀུན་ལ་འཇུག་པའོ། །

[Block 2056]
སེམས་ཅན་གནོད་པ་ཙམ་ནི་མན་ངག་དང་མི་ལྡན་པས་སྤྱོད་པའི་བྱ་བ་ཀུན་གྱིས་གནོད་པའོ། །

[Block 2057]
ཕྱག་རྒྱའི་དངོས་གྲུབ་ནི་ཡོངས་སུ་རྫོགས་པའི་ཕྱག་རྒྱ་ཆེན་པོའོ། །

[Block 2058]
རྙེད་མི་འགྱུར་ནི་མན་ངག་དང་བརྟུལ་ཞུགས་ལ་སོགས་པས་སོ། །

[Block 2059 [HEADING]]
#### དམ་ཚིག་གི་རྫས། ^1-11-1-0

[Block 2060]
དམ་ཚིག་གི་རྫས་ནི།

[Block 2061 [VERSE]]
དེ་ལ་དམ་ཚིག་བཟའ་བྱ་བ། །
ན་དང་ག་ཧ་དང་པོ་དང་། །
མཐའ་ཡི་ཤྭ་དང་དང་པོའི་ཤྭ། །
ཀྱེ་ཡི་རྡོ་རྗེ་དངོས་གྲུབ་ཕྱིར། །

[Block 2062]
བདུད་རྩི་ལྔ་ཡང་དེ་བཞིན་བཟའ། །ཞེས་བྱ་བ་ནི་ན་ན་ར་མིའི་ཤ །ག་གོ་ར་བ་ལང་གི་ཤ །ཧ་ཧ་སྟི་གླང་པོའི་ཤ་དང་། ཨ་ཤྭ་སྟེ་རྟའི་ཤ་དང་། ཤྭ་ན་སྟེ༌[^902]ཁྱིའི་ཤ་དང་ལྔའོ། །

[Block 2063]
བི་མུ་མར་ཤུ་བདུད་རྩི་ལྔ་ནི་བསྐྱེད་པའི་རིམ་པས་སྦྱང་བ་དང་སྤང་བ་དང་རྟོགས་པར་བྱས་ཏེ་བཟའ་བའོ། །

[Block 2064]
རྫོགས་པའི་རིམ་པ་ལ་ནི་བྱང་ཆུབ་སེམས་ཀྱི་རིམ་གྲོའི་དོན་དུ་བཟའ་བའོ། །

[Block 2065]
སྤྱིར་གང་ཟག་གི་རིམ་པས་བརྟགས་ཏེ་བཟའ་བ་དང་། བསྲེས༌[^903]ཏེ་བཟའ་བ་དང་། དངོས་སུ་བཟའ་བ་ཅི་རིགས་པར་ཤེས་པར་བྱའོ། །

[Block 2066 [VERSE]]
ཀྱེའི་རྡོ་རྗེས་གསུངས་མཚན་ཉིད། །
སྐྱེ་བ་བདུན་པ་དེ་ནས་བརྟག །

[Block 2067]
ཅེས་པ་ནི། སྐྱེ་བ་བདུན་པའི་ཤ་བཟའ་བ་སྟེ། དེ་ཡང༌[^904]བརྟག་པ་ནི་ནང་གི་བརྟག་པ་དང་ཕྱིའི་བརྟག་པའོ། །

[Block 2068 [HEADING]]
##### ནང་གི་བརྟག་པ། ^1-11-1-1-0

[Block 2069]
ནང་གི་བརྟག་པ་ནི། དགའ་བྲལ་དགའ་བ་ལ་སྨོད་པ། །ཞེས་ལས་ཀྱི་ཕྱག་རྒྱའི་དགའ་བ་སྤོང་བ་དང་། མིག་དང་ལྡན་ཞེས་བྱ་བ་ནི་ཤེས་རབ་ཤིན་ཏུ་ཆེ་བའོ། །

[Block 2070 [HEADING]]
##### ཕྱིའི་བརྟག་པ། ^1-11-1-2-0
--- END BLOCKS ---
