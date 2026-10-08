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
[Block 1996]
དེ་ཡང་ཆོས་དུ་མ་དེ་དག་ཇི་ལྟར་བསྡུ་ཞེ་ན། ཕྱག་རྒྱ་རྒྱུ་དང་བྲལ་ཞེས་པ་ནི་བདག་མེད་མའི་ཕྱག་རྒྱ་སྔགས་ལ་སོགས་པ་བྲལ་བ་སྟོང་པ་སྟེ། ཤེས་རབ་ཀྱིས་བསྡུས་པའོ། །

[Block 1997]
དེ་བཞིན་དཀྱིལ་འཁོར་དང་ལྷ་དང་ཕྱག་རྒྱ་དང་སྦྱིན་སྲེག་དང་མཆོད་སྦྱིན་ལ་སོགས་པས་བརྟག་པ་རྣམས་མེད་པ་དང་། ཡང་དག་པའི་སྔགས་ལ་སོགས་པ་ཡོད་པར་བསྟན་པ་ནི་ལེའུ་ལྔ་པ་ལྟར་ཤེས་པར་བྱ་སྟེ། དེ་ཡང་ཐབས་ཀྱིས་བསྡུས་པ་ནི་ཡོ་གའི་རྣལ་འབྱོར་པའོ། །

[Block 1998 [VERSE]]
སྙིང་རྗེ་ནི་སྣང་བ་ཀུན་ནོ། །
ཐབས་ནི་བདེ་བའི་རོར་གྱུར་པའོ། །

[Block 1999]
དེ་དག་བསྡུས་ཏེ་མི་གདགས་པའི་ཕྱིར་ཡེ་ཤེས་ནི་སྟོང་པའོ། །

[Block 2000]
ཐབས་ནི་སྙིང་རྗེའོ། །

[Block 2001]
དབྱེར་མེད་ནི་དེ་དག་གིས་ཆོས་ཀུན་བསྡུས་ནས་དེ་དག་ཉིད་ཀྱང་ཟག་པ་མེད་པའི་ལྷན་ཅིག་སྐྱེས་པར་གཅིག་པའོ། །

[Block 2002]
དེས་ཅིར་འགྱུར་ཞེ་ན། སེམས་ཙམ་ཡིན་ཏེ། དེའི་བྱང་ཆུབ་སེམས་ཞེས་བརྗོད་པ་སྟེ་ལྷན་ཅིག་སྐྱེས་པའོ། །

[Block 2003]
ད་ནི་བསྟན་པ་དེ་དག་རྒྱུ་མཚན་སོ་སོར་བཤད་པའི་ཕྱིར། སྔགས་བཟླས་ཞེས་པ་ནི་བསྐྱེད་པའི་རིམ་པའི་རྣམ་པ་ཐམས་ཅད་ཀྱི་ཆོས་སོ། །

[Block 2004]
མེད་ཅེས་པ་ནི་བདག་མེད་མའི་ཕྱག་རྒྱ་གཅིག་དང་དུ་བྲལ་གྱིས་སོ། །

[Block 2005]
ཡང་མེད་ཅེས་པ་ནི་རྒྱུའམ་ངོ་བོ་ལ་སོགས་པ་དང་བྲལ་བས་སོ། །

[Block 2006]
དེ་བཞིན་དུ་གཞན་དག་ལ་ཡང་ངོ་། །ད་ནི་ཐབས་ཀྱི་བསྡུས་པ་བསྟན་པའི་ཕྱིར། དེའི་སྔགས་བཟླས་ཞེས་པ་ནི་སྙིང་རྗེ༌[^885]སྣང་བ་རྒྱུན་དུ་གནས་པས་སོ།[^886] །དེ་དཀའ་ཐུབ་ནི་ཐབས་བདེ་བ་ཞུ་བ་མི་འབྲལ་བར་ཚངས་པར་སྤྱོད་པས་སོ། །

[Block 2007]
སྦྱིན་སྲེག་ནི་སྙིང་རྗེ་སྣང་བའི་སྲེག་བླུགས་མཆོད་པས་རྣམ་རྟོག་དང་ཉོན་མོངས་པ་མེད་པའོ། །

[Block 2008]
དཀྱིལ་འཁོར་པ་ནི་སྙིང་རྗེ་སྣང་བ་བདེ་བའི་ལྷ་སྟེ་ཉོན་མོངས་པའི༌[^887]ཟུག་རྔུ་ཞི་བས་སོ། །

[Block 2009]
དཀྱིལ་འཁོར་ནི་ཐབས་བདེ་བ་སྟེ། ལྷན་ཅིག་སྐྱེས་པ་འདུས་པའི་གནས་ཡིན་པས་སོ། །

[Block 2010]
ད་ནི་རྣམ་པ་ཐམས་ཅད་སྡོམ་པ་གཅིག་གི་རྒྱུ་མཚན་བསྟན་པའི་ཕྱིར། མདོར་བསྡུས་ཞེས་པ་ནི་གང་དག་ཅེ་ན། སྔགས་ལ་སོགས་པ་རྣམ་པ་ཀུན་ནོ། །གང་ལྟར་ཞེ་ན། སྟོང་པ་ཉིད༌[^888]སྙིང་རྗེས་སོ། །

[Block 2011]
གང་གིས་ཞེ་ན་འདུས་པའི་ཞེས་པ་སྟེ། དབྱེར་མེད་ཀྱིས་སོ། །གང་གི་ཕྱིར་ཞེ་ན། སེམས་ནི་ཞེས་པ་སྟེ། བྱང་ཆུབ་སེམས་སོ། །

[Block 2012]
གཟུགས་ཅན་ཞེས་པ་ནི་རཱུ་པ་སྟེ་ལྷན་ཅིག་སྐྱེས་པའི་ཚུལ་ལམ་རང་བཞིན་ནོ། །

[Block 2013]
ལེའུ་བཅུ་པའོ།། །།

[Block 2014 [HEADING]]
### བཅུ་གཅིག་པ་ཉམས་སུ་བླང་བའི་འབྲས་བུ། ^1-11-0

[Block 2015]
ད་ནི་ལེའུ་དང་པོ་ལ་ལྟ་སྟངས་ལ་སོགས་པ་རིམ་པ་གཉིས་ཀྱིས་དམིགས་པའི་ཡུལ་ཆེ་བའི་བདག་ཉིད་འདིར་འབྲས་བུ་འགྲུབ་པར་བསྟན་པའི་ཕྱིར་མཉམ་པ་ནི་མིག་འབྲས་གཉིས་སོ། །

[Block 2016]
མ་རུངས་ནི་ཧེ་རུ་ཀའི་ང་རྒྱལ་གྱིས་སོ། །

[Block 2017]
དཔྲལ་བ་ཅན་ནི་མིག་འབྲས་གཉིས་དཔྲལ་བ་ལ་བརྟེན་ཏེ་ཅུང་ཟད་གྱེན་དུ་བལྟས་ནས་ཐུར་དུ་འབེབས་པའོ། །

[Block 2018]
ལྟུང་བར་བརྗོད་ནི་བསྒྲུབ་བྱ་འགྱེལ་བར་བྱེད་པའོ། །

[Block 2019]
གཞན་དག་ནི་ལྟ་སྟངས་རྣམས་དང་། དབུགས་དང་དཔེ་དག་སྟེ།

[Block 2020 [VERSE]]
གཞན་དག་དབུགས་ཀྱིས༌[^889]བསྒྲུབ་པ་ཡང་། །
འབྱུང་བ་ཉིད་ཀྱིས་ལྟུང་བར་བྱེད། །
རྡུབ་པ་ཡིས་ནི་དབང་དུ་བྱེད། །
དགང་བ་ཡིས་ནི་འགུགས་པར་བྱེད། །

[Block 2021]
ཞི་བ་ཡིས་ནི་རེངས་པར་བྱེད། །ཅེས་བྱ་བ་ནི་ཕྱིར་འབྱུང་བ་དང་། ནང་དུ་རྔུབ་པ་དང་དབུགས་ནང་དུ་འགེངས་པ་དང་། དབུགས་ཞི་བས་རེངས་པར་བྱེད་དོ། །

[Block 2022]
དཔེ་གཏན་ལ་དབབ་པ་ནི་རློན་པའི་ཤིང་ལས་སྒྱེལ་བའི་ཉམས་སད་པའི་གནས་སོ། །

[Block 2023]
མེ་ཏོག་ཅན་ལ་ནི་དབང་གི༌[^890]ཉམས་སད་པའི་གནས་སོ། །

[Block 2024]
རྡོ་རྗེའི་ཤིང་ནི་ཤིང་ཐང་ཆུ་ཅན་དེ་དགུག་པའི་ཉམས་སད་པའི་གནས་སོ། །

[Block 2025]
གཡོ་བཅས་རྩ་ནི་འཇག་མ་སྟེ། རེངས་པའི་ཉམས་སད་པའི་གནས་སོ། །

[Block 2026]
ཟླ་བ་དྲུག་གོམས་པའི་སྦྱོར་བ་ནི། དང་ལ་ཧེ་རུ་ཀའི་བཟླས་པ་དང་བསྒོམ་པ་སྟེ།

[Block 2027 [VERSE]]
གཞན་དག་ཀྱང༌[^891]བཀག་པ་ནི་མ་ཡིན་ནོ། །
སྒྲུབ་པ་ནི་བསྒྲུབ་བྱ་ལྟུང་བ་ལ་སོགས་པའོ། །

[Block 2028]
ཐེ་ཚོམ་མེད་པ་ནི་འདི་ལ་སྟེ་དཔེ་ལ་གྲུབ་ནའོ། །

[Block 2029]
ཡང་དབང་ངམ་སྤྱོད་པའི་དུས་སུ་ལས་ཀྱི་ཕྱག་རྒྱ་ལ་བརྟེན་པ་ནི། མཉམ་པ་མ་རུངས་དཔྲལ་བ་ཅན་ནི། སྙོམས་པར་འཇུག་པའི་དུས་སུ་ཟླ་བ་ནམ་མཁའི་དཀྱིལ་འཁོར༌[^892]ལ་སོགས་པར་འབབ་པའོ། །

[Block 2030 [VERSE]]
དབང་ནི་སྒྱེལ་བའི་ཐབས་སོ། །
དགུག་པ་ནི་བཟློག་པའི་མན་ངག་གོ། །
རེངས་པ་ཡིས་ནི་གཟུང་བའི་ཐབས་སོ། །

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
--- END BLOCKS ---
