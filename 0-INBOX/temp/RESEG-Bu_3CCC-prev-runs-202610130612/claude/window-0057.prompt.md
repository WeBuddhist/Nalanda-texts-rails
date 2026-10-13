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
དེ་ལྟ་བས་ན། དེ་ཡང་དེ་ཉིད་དང་གཞན་ཉིད་དུ་བརྗོད་པར་བྱ་བ་མ་ཡིན་པའི་ཕྱིར། རྟག་པ་ཡང་མ་ཡིན་ལ་ཆད་པ་ཡང་མ་ཡིན་པས་དེ་ཁོ་ནའི་མཚན་ཉིད་ཡིན་ནོ། །

[Block 1997 [VERSE]]
དོན་གཅིག་མིན་དོན་ཐ་དད་མིན། །
ཆད་པ་མ་ཡིན་རྟག་མིན་པ། །
དེ་ནི་སངས་རྒྱས་འཇིག་རྟེན་གྱི། །
མགོན་པོས༌[^1298]བསྟན་པ་བདུད་རྩི་ཡིན། །

[Block 1998]
དེ་ལྟར་མཐོ་རིས་དང་བྱང་གྲོལ་གྱི་ལམ་རྣམ་པར༌[^1299]འབྱེད་པ་དོན་གཅིག་པ་ཉིད༌[^1300]མ་ཡིན་ན༌[^1301]དོན་ཐ་དད་པ་མ་ཡིན་པ། ཆད་པ་མ་ཡིན་པ་རྟག་པ་མ་ཡིན་པ། གཅིག་པ་དང་ཐ་དད་པ་དང་ཆད་པ་དང་རྟག་པའི་སྐྱོན་ལས་ཕྱི་རོལ་དུ་གྱུར་པ། མཆོག་ཏུ་ཟབ་པ། དོན་དམ་པའི་དེ་ཁོ་ན་གསལ་བར་བྱེད་པ་དེ་ནི་འཇིག་རྟེན་དང་འཇིག་རྟེན་ལས་འདས་པའི་བདེ་བ་ཐོབ་པར་བྱ་བའི་ཕྱིར། སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཐམས་ཅད་མཁྱེན་པ་ཐམས་ཅད་གཟིགས་པ། སྟོབས་བཅུའི་སྟོབས་དང་ལྡན་པ། རྒྱུ་མེད་པར་བྱམས་པ་རྣམས་ཀྱིས༌[^1302]བསྟན་པ་བདུད་རྩི་ཡིན་ཏེ། དེ་བསྒྲུབ་པར༌[^1303]བྱའོ། །

[Block 1999]
འདི་ལྟར་དེར་ཞུགས་པ་རྣམས་ཀྱི་བདག་ཉིད་ཀྱི་མངོན་སུམ་དུ་གྱུར་པ་འཕྲལ་ཁོ་ན་ལ་འགྲུབ་པར་འགྱུར་རོ། །

[Block 2000]
གང་དག་ཚོགས་མ་བྱས་པ་ཉིད་ཀྱིས་འཕྲལ་ལ་མ་གྲུབ་པ་དེ་དག་ལ་ཡང་ཚེ་རབས་གཞན་དག་ལ་ངེས་པར་འགྲུབ་པར་འགྱུར་ཏེ། སློབ་དཔོན་འཕགས་པ་ལྷས་ཀྱང་།

[Block 2001 [VERSE]]
དེ་ཉིད་ཤེས་པས་འདི་ལ་ནི། །
འདོད་ཆགས་བྲལ་བ་མ་ཐོབ་ཀྱང་། །
ཚེ་རབས་གཞན་ལ་འབད་མེད་པར། །
ངེས་པར་ཐོབ་དེ༌[^1304]ལས་བཞིན་ནོ། །

[Block 2002]
ཞེས་གསུངས་སོ། །

[Block 2003 [VERSE]]
རྫོགས་སངས་རྒྱས་རྣམས་མ་བྱུང་ཞིང་། །
ཉན་ཐོས་རྣམས་ནི་ཟད་གྱུར་ཀྱང་། །
རང་སངས་རྒྱས་ཀྱི་ཡེ་ཤེས་ནི། །
བསྟེན་པ༌[^1305]མེད་ལས་རབ་ཏུ་སྐྱེ། །

[Block 2004]
ཅི་སྟེ་ཡང་འདི་ལ་ཅུང་ཟད་གོམས་པར་བྱས་པ་རྣམས་ལ་བརྒྱ་ལ༌[^1306]རྫོགས་པའི་སངས་རྒྱས་རྣམས་མ་བྱུང་ངམ། ཉན་ཐོས་རྣམས་ཟད་པར་གྱུར་ཏེ། རྐྱེན་དང་མི་ལྡན་པར་གྱུར་དུ་ཟིན་ན་ཡང་། དེ་དག་གི་སྔོན་གོམས་པའི་རྒྱུ་ལས་བྱུང་བ་རང་སངས་རྒྱས་ཀྱི་ཡེ་ཤེས་གཞན་ལས་ཤེས་པ་མ་ཡིན་པ་བསྟེན་པ༌[^1307]མེད་པ་ཙམ་གྱིས༌[^1308]རྐྱེན་ལས་རབ་ཏུ་སྐྱེ་བར་འགྱུར་རོ། །

[Block 2005]
དེའི་དེ་ལྟར་བསྟན་པ་བདུད་རྩི་འདི་བསྒྲུབ་པ༌[^1309]ལ་འབྲས་བུ་ཡོད་པར་འགྱུར་བས། དེ་ལྟ་བས་ན་ཡོངས་སུ་རྟོག་པ་དང་ལྡན་པ་འཁོར་བའི་དགོན་པ་སྤོང་བར་འདོད་པ། བདུད་རྩིའི་གོ་འཕང་ཐོབ་པར་འདོད་པ་རྣམས་ཀྱིས་འདི་ཉིད་འབད་པས་བསྒྲུབ་པར་བྱ་སྟེ། འདི་ཁོ་ན་ལས་དོན་དམ་པ་ངེས་པར་འགྲུབ་པོ། །བདག་དང་ཆོས་བརྟག་པ་ཞེས་བྱ་བ་སྟེ་རབ་ཏུ་བྱེད་པ་བཅོ་བརྒྱད་པའོ།། །།

[Block 2006 [HEADING]]
## དུས་བརྟག་པ། ^19-0

[Block 2007]
སྨྲས་པ། འདི་ལ་ཁྱོད་ཀྱིས་བྱེད་པ་པོ་ལས་བརྟག་པའི་ཞར་ལ་འོངས་པ་དེ་གའི༌[^1310]རིགས་པ་རྗེས་སུ་བསྟན་པས་ཁོ་བོའི་ཡིད་ཀྱིས་དག་ལ་དངོས་པོ་ཡོད་པ་དང་མེད་པར་ལྟ་བའི་ཤིང་བརྟན་པོ་ཆེན་པོ་ཡུན་རིང་པོ་ནས་རབ་ཏུ་གནས་པའི་རྩ་བ་ཡང་ལེགས་པར་འགུལ་གྱི།[^1311] དེའི་ཕྱིར་ད་ཡང་ཁོ་བོ་ལ་ཕན་གདགས་པར་འདོད་པས་དུས་བརྟག་པར་བྱ་བའི་རིགས་སོ། །

[Block 2008]
བཤད་པ་ལེགས་སོ། །

[Block 2009]
སྨྲས་པ། འདི་ལ་བཅོམ་ལྡན་འདས་ཀྱིས་དེ་དང་དེར་དུས་གསུམ་བསྟན་པ་མཛད་དེ། མེད་ན་ནི་བསྟན་པར་མི་རིགས་པས་དུས་གསུམ་ནི་ཡོད་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 2010]
བཤད་པ། བཅོམ་ལྡན་འདས་ཀྱིས་འཇིག་རྟེན་གྱི་ཐ་སྙད་ཀྱི་དབང་གིས་དུས་གསུམ་བསྟན་པ་མཛད་ཀྱི། དེ་ཁོ་ནར་ནི་དུས་གསུམ་མི་འཐད་དོ། །

[Block 2011]
དེ་ཇི་ལྟར་ཞེ་ན། འདི་ལ་རེ་ཞིག་གལ་ཏེ་མ་འོངས་པའི་དུས་སུ་གྱུར་ནས་རིམ་གྱིས་ད་ལྟར༌[^1312]དུ་འགྱུར་ཞིང་། ད་ལྟར་དུ་གྱུར་ནས་ཀྱང་རིམ་གྱིས་འདས་པར་འགྱུར་བ་ནི། དེ་ལྟ་ན་དུས་གཅིག་ཏུ་འགྱུར་ཏེ། དཔེར་ན་ཙཻ་ཏྲ་གྲོང་དུ་ཕྱིན་ན་ཡང་ཙཻ་ཏྲ་ཉིད་ཡིན་ལ་གྲོང་ནས་ཐལ་ན་ཡང་ཙཻ་ཏྲ་ཉིད་ཡིན་ཏེ། དེ་ལ་མ་ཕྱིན་པ་དང་། ཕྱིན་པ་དང་ཐལ་བ་གསུམ་ཉིད་དུ་དབྱེར་མེད་པ་བཞིན་ནོ། །

[Block 2012]
ཅི་སྟེ་ཡང་མ་འོངས་པ་ཡང་གཞན་ཉིད་ལ་ད་ལྟར་ཡང་གཞན་འདས་པ་ཡང་གཞན་ཡིན་པར་གྱུར་ན་ནི། དེ་ལྟ་ན་ཡང་གསུམ་ཅར་ཡང་རྟག་པ་ཉིད་དུ་འགྱུར་རོ། །

[Block 2013]
རྟག་པ་ཉིད་ཡིན་ན་དུས་སུ་བརྟག་པ་དོན་མེད་པ་ཉིད་དུ་འགྱུར་ཏེ་དགོས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 2014]
ཡང་གཞན་ཡང་། འདི་ལ་གལ་ཏེ་དུས་ཞེས་བྱ་བ་དངོས་པོ་འགའ་ཞིག་ཡོད་པར་གྱུར་ན། དེ་རང་ལས་སམ། ལྟོས་ནས་རབ་ཏུ་འགྲུབ་པར་འགྱུར་གྲང་ན། དེ་ལ་རེ་ཞིག་གལ་ཏེ་དུས་གསུམ་དུ་ལྟོས་ནས་རབ་ཏུ་འགྲུབ་པར་སེམས་ན། དེ་ལ་བཤད་པར་བྱ་སྟེ།

[Block 2015 [VERSE]]
ད་ལྟར་བྱུང་དང་མ་འོངས་པ། །
གལ་ཏེ་འདས་ལ་ལྟོས་གྱུར་ན། །

[Block 2016 [VERSE]]
ད་ལྟར་བྱུང་དང་མ་འོངས་པ། །
འདས་པའི་དུས་ན༌[^1313]ཡོད་པར་འགྱུར། །

[Block 2017]
ད་ལྟར་བྱུང་བ་དང་། མ་འོངས་པའི་དུས་དག་གལ་ཏེ་འདས་པའི་དུས་ལ་ལྟོས་ནས་ཡོད་པར་གྱུར་ན། དེ་ལྟ་ན་ད་ལྟར༌[^1314]བ་དང་མ་འོངས་པའི་དུས་དག་འདས་པའི་དུས་ན་ཡོད་པར་འགྱུར་རོ། །

[Block 2018]
འདས་པ་ན་ཡོད་པར་གྱུར་ན་དེ་གཉིས་ཀྱང་འདས་པ་ཡིན་པར་འགྱུར་རོ། །

[Block 2019]
དེ་ལྟ་ན་དུས་གཅིག་ཁོ་ནར་འགྱུར་རོ། །

[Block 2020]
དུས་གཅིག་ཁོ་ན་ཡིན་ན་ལྟོས་པ་མི་འཐད་དེ་འདི་ལྟར་དེ་ཉིད་དེ་ཉིད་ལ་ཇི་ལྟར་ལྟོས་པར་འགྱུར། ལྟོས་པ་མི་འཐད་པའི་ཕྱིར་དུས་ཀྱང་མི་འཐད་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 2021]
ཅི་སྟེ་འདས་པའི་དུས་ཞིག་ཅིང༌[^1315]འགགས་ཏེ་མེད་པ་ཁོ་ན་ཡིན་ན་ནི། དེ་ན་འདི་གཉིས་ཇི་ལྟར་ཡོད་པར་འགྱུར། ཅི་སྟེ་འདས་པ་ཡང་ཡོད་པ་ཁོ་ན་ཡིན་པར་སེམས་ན་ནི་ཡོད་པའི་ཕྱིར་ད་ལྟར་ཡིན་པར་འགྱུར་གྱི༌[^1316]འདས་པ་མ་ཡིན་པས་དེ་ནི་མི་འདོད་དོ། །

[Block 2022]
སྨྲས་པ། གང་གི་ཚེ་ད་ལྟར་བྱུང་བ་དང་མ་འོངས་པ་དག་འདས་པ་ལ་ལྟོས་ནས་འགྲུབ་པོ་ཞེས་སྨྲས་པ་དེའི་ཚེ་ཇི་ལྟར་དེ་གཉིས་འདས་པ་ན་ཡོད་པར་འགྱུར། བཤད་པ། གང་གི་ཕྱིར་དེ་ལ་ལྟོས་ནས་འགྲུབ་པོ་ཞེས་སྨྲས་པ་དེ་ཁོ་ནའི་ཕྱིར་དེ་གཉིས་དེ་ན་ཡོད་པར་ཐལ་བར་འགྱུར་རོ། །

[Block 2023]
གཞན་དུ་ན།

[Block 2024 [VERSE]]
ད་ལྟར་བྱུང་དང་མ་འོངས་པ། །
གལ་ཏེ་དེ་ན་མེད་གྱུར་ན། །

[Block 2025 [VERSE]]
ད་ལྟར་བྱུང་དང་མ་འོངས་པ། །
ཇི་ལྟར་དེ་ལ་ལྟོས་པར་འགྱུར། །

[Block 2026]
ད་ལྟར་བྱུང་བ་དང་མ་འོངས་པའི་དུས་དག་གལ་ཏེ་འདས་པའི་དུས་དེ་ན་མེད་པར་གྱུར་ན། ད་ལྟར་བྱུང་བ་དང་མ་འོངས་པའི་དུས་དེ་ན་མེད་པ་དེ་དག་ཇི་ལྟར་དེ་ལ་ལྟོས་པར་འགྱུར་ཏེ། འདི་ལྟར་གསུམ་ཆར་ཡང་ཚོགས་པར་གྱུར་ན་ལྟོས་པར་འཐད་པའི་ཕྱིར་རོ། །

[Block 2027]
ཅི་སྟེ་ཡང་དེ་ན་ཡོད་པར་གྱུར་ན་ནི་དེ་གཉིས་ཡོད་པ་ལ་ཡང་ལྟོས་པས་ཅི་ཞིག་བྱ། དེ་ལྟ་བས་ན་རེ་ཞིག་ད་ལྟར་བྱུང་བ་དང་མ་འོངས་པ་དག་འདས་པ་ལ་ལྟོས་ནས་རབ་ཏུ་འགྲུབ་པར་མི་འཐད་དོ། །

[Block 2028]
དེ་ལ་འདི་སྙམ་དུ་ད་ལྟར་བྱུང་བ་དང་མ་འོངས་པ་དག་འདས་པ་ལ་མ་ལྟོས་པ་ཁོ་ནར་འགྲུབ་པར་སེམས་ན། དེ་ལ་བཤད་པར་བྱ་སྟེ།

[Block 2029 [VERSE]]
འདས་པ་ལ་ནི་མ་ལྟོས་པར། །
དེ་གཉིས་འགྲུབ་པ་ཡོད་མ་ཡིན། །

[Block 2030]
འདས་པའི་དུས་ལ་མ་ལྟོས་པར་ཡང་དེ་ལྟར༌[^1317]བྱུང་བ་དང་། མ་འོངས་པའི་དུས་དེ་གཉིས་རང་ལས་རབ་ཏུ་འགྲུབ་པ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2031 [VERSE]]
དེ་ཕྱིར་ད་ལྟར་བྱུང་བ་དང་། །
མ་འོངས་དུས་ཀྱང་ཡོད་མ་ཡིན། །

[Block 2032]
དེ་ལྟར་གང་གི་ཕྱིར་ད་ལྟར་བྱུང་བ་དང་མ་འོངས་པ་གཉིས་འདས་པའི་དུས་ན་ཡོད་པ་མ་ཡིན་པས་ལྟོས་པར་མི་འཐད་ལ། འདས་པ་ལ་མ་ལྟོས་པར་ཡང་དེ་གཉིས་འགྲུབ་པ་ཡོད་པ་མ་ཡིན་པ་དེའི་ཕྱིར་ད་ལྟར་བྱུང་བ་དང་མ་འོངས་པའི་དུས་ཀྱང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2033]
རིམ་པའི་ཚུལ་ནི་འདི་ཉིད་ཀྱིས།[^1318] །

[Block 2034 [VERSE]]
ལྷག་མ་གཉིས་པོ་བསྣོར་བ་དང་། །
མཆོག་དང་ཐ་མ་འབྲིང་ལ་སོགས། །
གཅིག་ལ་སོགས་པའང༌[^1319]ཤེས་པར་བྱ། །

[Block 2035]
རིམ་པའི་ཚུལ་འདི་ཉིད་ཀྱིས་དུས་ལྷག་མ་གཉིས་པོ་བསྣོར་བ༌[^1320]དང་། མཆོག་དང་ཐ་མ་དང་འབྲིང་དང་གཅིག་ལ་སོགས་པ་དག་ཀྱང་ཤེས་པར་བྱའོ། །
--- END BLOCKS ---
