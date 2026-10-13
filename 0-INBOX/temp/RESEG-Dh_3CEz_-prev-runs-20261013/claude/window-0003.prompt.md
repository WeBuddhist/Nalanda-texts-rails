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
[Block 106]
བཙུན་མོ་ནི་ཡུམ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་སྟེ་ཡོན་ཏན་བསྐྱེད་པའོ་ཞེས༌[^59]བཞུགས་སོ་ཞེས་པ་ནི་ཆོས་ཉིད་ཀྱིས་ཆོས་ཐམས་ཅད་ལ་ཁྱབ་པ་སྟེ། ཏིལ་ཅན་ནི་ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད་ལ་སོགས།

[Block 107 [VERSE]]
[^60]ཏིལ་ལ་ཏིལ་མར་ཇི་བཞིན་དུ། །
བུ་རམ་ཤིང་ལ་བུ་རམ་བཞིན། །

[Block 108]
ཞེས་པའོ། །

[Block 109 [HEADING]]
###### **རྟེན་དང་པོ་ནང་ནས་འཇུག་པ།** ^1-1-1-2-1-1-2-1-2-0

[Block 110]
རྟེན་དང་པོ་ནང་ནས་འཇུག་པ་ནི་ཨེ་སྟེ་ཤེས་རབ་ལྷ་མོ་བླ་ན་མེད་པའོ། །

[Block 111]
བ་ནི་དེ་བརྟེན་པའི་ཐབས་ཏེ་ཡིད་འབྲིད་པའི་དུས་སུ་ཐབས་དུ་མའོ། །

[Block 112]
ང་ནི་དབང་པོ་རང་སྣང་སྟེ་རབ་འབྲིང་ཐ་མ་གསུམ་སྟེ་གསེར་འགྱུར་གྱི་ཚུལ་དང་བྱ་རོག་ལྡིང༌[^61]ཆགས་ཀྱི་ཚུལ་དང་རྒྱ་མཚོ་ལྟ་བུའི་ཚུལ་དང་ནང་ཕྱི་རོལ་དུ་སྣང་བ་དང་།[^62] ཕྱི་ནང་དུ་སྣང་བ་དང་། རང་སོར་གནས་པ་སྐྱེའོ། །

[Block 113]
མ༌[^63]ཡཱ་ནི་སྤྱོད་ལམ་དང་བསྲེ་སྟེ།

[Block 114 [VERSE]]
ཟ་བ་དང་འགྲོ་ཉལ་དུ་ཡང་སྐྱེའོ། །
ཤྲུ་ཏ་ནི་དོན་དམ་ལྷན་སྐྱེས་སོ། །

[Block 115]
དུས་གཅིག་ནི་ཀུན་རྫོབ་ལྷན༌[^64]སྐྱེས་པ་དང་དུས་གཅིག་གོ། །

[Block 116]
ལྷན་ཅིག་སྐྱེས་པ་དེ་ཉིད་བཅོམ་ལྡན་འདས་ཏེ་སྔ་མ་བཞིན་ནོ། །

[Block 117]
གནས་གང་ན་བཞུགས་ཤེ་ན། དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་དེ་སེམས་ཅན་ཐམས་ཅད་དོ། །

[Block 118]
སྐུ་གསུང་ཐུགས་ཀྱི་ལུས་ངག་ཡིད་གསུམ་སྟེ། དེ་ཁོ་ན་རྡོ་རྗེ་བཙུན་མོ་སྟེ། ཤེས་རབ་ལྷ་མོ་བླ་ན་མེད་པ་ཕྱག་རྒྱ་ཆེན་པོ་རྟེན་དང་བརྟེན་པའི་ཚུལ་དུ་གནས་པ་ན་བཞུགས་པའོ། །

[Block 119]
དེ་ནི་ཟག་པ་མེད་པའི་བརྟེན་པ་ཡིན་གྱི་ཟག་བཅས་ཀྱི་ཚུལ་ནི་མ་ཡིན་ནོ། །

[Block 120]
དེའི་ཕྱིར་དབང་རྟེན་མི་གནས་ཏེ། ཞིབ༌[^65]ཀྱང་དབང་པོ་འཇིག་པ་མ་ཡིན་ནོ། །

[Block 121]
གཉུག་མའི་དབང་པོ་ཡོད་པར་ཅིས་ཤེས་ཤེ་ན། དེ་ལུང་དང་རིགས་པས་ཤེས་ཏེ། ལུང་ནི།

[Block 122 [VERSE]]
ལྟེ་བར་ཕྱག་རྒྱ་ཆེན་པོ་གནས། །
དང་པོ་དབྱངས་ཡིག་རང་བཞིན་ཏེ། །

[Block 123]
ཞེས་བྱ་བ་དང་།

[Block 124 [VERSE]]
ཕྱག་རྒྱ་ཆེན་པོ་དབང་བསྐུར་བ། །
དེ་ནི་འདི་ཡི་བྱིན་རླབས་ཡིན། །

[Block 125]
ཞེས་གསུངས་པ། དེའི་རྟེན་ཡང་ལུང་དེས་བསྒྲུབ་བོ། །

[Block 126]
ཕྱག་རྒྱ་ཆེན་པོ་ཉིད་དབང་རབ་དང་རབ༌[^66]ལས་བྱུང་བ་བསྒོམ་པ་རབ་དང་རབ་ཀྱིས་དང་མན་ངག་རབ་དང་རབ་ཀྱིས་བསྒྲུབ་པའོ། །

[Block 127]
དེ་ལ་དབང་རྟེན་ཡོད་པར་ཡང་ཡེ་ཤེས་ཡོད་པས་དེའི་རྟེན་ཡོད་དེ། །དཔེར་ན་མིག་གི་རྣམ་པར་ཤེས་པ་ཡོད་པས་རྐྱེན་གཞན་ཚང་ཡང་རེས་འགག་པར་འདུག་པས་གཞན་ཞིག་ཡོད་ཅེས་བྱ་བ་ལྟ་བུའོ། །

[Block 128]
དེ་ལ་གོམས་པ་ལས་རྟགས་གཞན་ཡང་གསུམ་སྟེ།

[Block 129 [VERSE]]
མི་འགྱུར་བ་ནི་ལྟ་བའི་རྟགས། །
དངོས་པོ་ཀུན་ལ་ཆགས་མེད་དྲོད། །
སྒོམ་པའི་རྟགས་སུ་ཤེས་པར་བྱ། །
འཇིག་རྟེན་ཆོས་བརྒྱད་སྤངས་པ་ནི། །

[Block 130]
སྤྱོད་པའི་རྟགས་སུ་ཤེས་པར་བྱ། །ཡང་སྔ་མའི་གསུམ་པོ་སེམས་ཟིན་པ་དང་དེ་ཁོ་ན་ལ་འཇུག་པ་དང་། དངོས་གྲུབ་འགྲུབ་པའོ། །

[Block 131]
དེ་ཁོ་ན༌[^67]ལ་ཡང་རྟགས་ལྔ་མཐོང་བའི་ལམ་དང་མཚུངས་པ་ཡིན་ནོ། །

[Block 132]
དེ་རྣམས་གསུམ་པ་རྟགས་དང་སྦྱར་ནས་སྤྱོད་པ་གསུམ་རིམ་གྱིས་བྱེད་པའམ་ཡང་ན་ཐོད་རྒལ་དུ་ཡང་བྱའོ། །

[Block 133]
གསུམ་པོས་ཀྱང་ལམ་མཇལ་བྱུང་བ༌[^68]མ་ཡིན་ཏེ། གཉིས་ཀྱིས་ནི་ཕྱག་རྒྱ་ཆེན་པོར་བརྒྱུད་དགོས་ལ། གཅིག་གིས་ནི་ཐལ་བྱུང་དུ་འགྲོའོ། །

[Block 134]
གཉིས་ནི་གང་ཟག་གི་རིམ་པས་བཤད་དེ། ཡང་།

[Block 135 [VERSE]]
ལས་ཀྱི་ཕྱག་རྒྱ་འཕྲོ༌[^69]རྒྱུ་ཅན། །
དེ་ཡང་རིང་དུ་སྤང་བྱ་སྟེ། །

[Block 136]
རང་ལུས་ཐབས་དང་ལྡན་པར་བསྒོམ་པར་བྱ་བ་དང་། དེ་ལ་སོགས་པ་དང་།

[Block 137 [VERSE]]
རང་བཞིན༌[^70]དོན་ནི་རབ་བསྒྲུབ་ཕྱིར། །
འཁོར་བར་ཐབས་གཞན་ཡོད་མ་ཡིན། །
ཞེས་པ་དང་མང་དུ་བསྟན་ཏོ། །

[Block 138]
དེ་ཡང་རིམ་པར་འགྲོ་བའམ་ཡང་ན་རེ་རེ་ནས་བརྒྱུད་པ་ཡང་སྲིད་དོ། །

[Block 139 [HEADING]]
###### བརྟག་པ་ཕྱི་མའི་ཚུལ་གྱིས་མདོར་བསྡུས་ཏེ་བསྟན་པ། ^1-1-1-2-2-0

[Block 140]
དེ་ལ་བརྟག་པ་ཕྱི་མའི་ཚུལ་གྱིས་དོན་བསྡུ་བ་ནི་འདི་ལྟར་སྣང་བ་ཐམས་ཅད་ལྷན་སྐྱེས་བདེ་བ་ཆེན་པོ་ཡིན་ཞིང་རང་བཞིན་ཀྱང་དེ་ལྟར་སངས་རྒྱས་དང་སེམས་ཅན་ཐམས་ཅད་ཀྱང་དེ་ལྟ་བུའི་ཡང་དག་པར་སྡོམ་པ་ཡིན་ཏེ། ཅིས་ཤེ་ན། ཨེ་ཝཾ་སྟེ་གནས་སམ་དེ་རུ༌[^71]དེས་སོ། །གང་གིས་སྡོམ་ཞེ་ན། མ༌[^72]ཡཱ་སྟེ་དབང་གི་བདག་ཉིད་དང་ནི་ཤེས་རབ་དང་ཐབས་དབང་རྣམས་ཀྱིས་སོ། །

[Block 141]
ཤྲུ་ཏ་སྟེ་དགོངས་པའི་སྐད་དུ་ཐོས་པ་དེའི་དབང་གིས་དུས་ལ་སོགས་པའི་སྐབས་ངག་བརྡ་དང་ལུས་བརྡས་སྨྲའོ། །

[Block 142]
ཨེ་ཀ་སྨིན༌[^73]ས་མ་ཡ་སྟེ་དགའ་བ་རྣམས་དང་སྐད་ཅིག་གི་དུས་སུ་གཅིག་པ་སྟེ། ཤེས་པ་སྐྱེས་པའི་ཚུལ་སྤོང་བ་དང་ཐོབ་པའི་ཚུལ་དུ་འབྱུང་བའོ། །

[Block 143]
ཡང་བཟའ་བ་སྟོན་མོའི་དུས་སུ་དམ་ཚིག་གཅིག་པའོ། །

[Block 144]
དེ་དག་གིས་ཀྱང་བརྗོད་བྱའི་ཆོས་ཐམས་ཅད་དང་རྗོད་བྱེད་ཀྱི་ཆོས་ཀྱི་ཕུང་པོ་བརྒྱད་ཁྲི་བཞི་སྟོང་རྣམས་དཔལ་དགྱེས་པའི་རྡོ་རྗེར་འདུས། དུས་ཟླ་བ་དང་ལོ་ལ་སོགས་པར་བསྒོམས་པས་དང་པོ་སྤྲིན་དང་འདྲ་བ་དང་།

[Block 145 [VERSE]]
གཉིས་པ་དུ་བ་ལྟ་བུ་སྟེ། །
གསུམ་པ་སྲིན་བུ་མེ་ཁྱེར་འདྲ། །
བཞི་པ་མར་མེ་ལྟ་བུ་སྟེ། །
ལྔ་པ་ཐམས་ཅད་སྣང་བ་སྟེ། །
--- END BLOCKS ---
