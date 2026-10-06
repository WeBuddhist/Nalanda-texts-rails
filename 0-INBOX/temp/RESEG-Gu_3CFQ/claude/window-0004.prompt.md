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
[Block 141]
རྣམ་པ་གཅིག་ཏུ་ན་ཕམ་པ་རྣམས་ཀྱི་གནས་ཡིན་ཏེ། ཕམ་པའི་ཆོས༌[^103]གང་ལ་གནས་པ་བསླབ་པའི་གཞི་བཅས་པ་ཆེན་པོ་ལ་གནས་སོ། །

[Block 142]
དེ་དང་མཐུན་པ༌[^104]རྣམས་ནི་ཕམ་པའི་གནས་ལྟ་བུ་རྣམས་ཏེ། དེ་དག་གི་གནས་ལྟ་བུ་ཉིད་ཆེན་པོའི་གནས་ནི་འདི་དག་གི་ཡང་ཡིན་ནོ། །

[Block 143]
དེ་ལྟ་བས་ན་ཆོས་བཞི་པོ་འདི་དག་ནི་ཕམ་པའི་གནས་ལྟ་བུ་ཞེས་བྱ་སྟེ། དཔེར་ན་སྡོམ་པའི་ཚུལ་ཁྲིམས་ཆེན་པོའི་ཆོས་རྣམས་ཇི་ལྟ་བ་བཞིན་དུ་འདི་དག་ཀྱང་དེ་དང་འདྲ་བའི་ཕྱིར་ཕམ་པའི་གནས་ལྟ་བུ་ཞེས་བྱའི༌[^105]རྣམ་པ་ཐམས་ཅད་དུ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཚིག་སྟེ། དེ་ནི༌[^106]འོག་ནས་བསྟན་ཏོ། །

[Block 144]
ཉན་ཐོས་ཀྱི་ཐེག་པ་པ་བསྙེན་པར་རྫོགས་པས་བསླབ་པ་མ་ཕུལ་བར་འཁྲིག་པའི་ཆོས་བསྟེན་པས་ཉེས་པ་ཐོབ་པ་གང་ཡིན་པ་དེ་ནི། རྙེད་པ་དང་བཀུར་སྟི་ལ་ལྷག་པར་ཞེན་ཏེ། [^107]བདག་ལ་སྟོད་པ༌[^108]དང་གཞན་ལ་སྨོད་པས་ཐོབ་པར་འགྱུར་ཏེ། གཞན་དག་ལ་ཡང་དེ་བཞིན་དུ་ཅི་རིགས་པར་སྦྱར་རོ། །

[Block 145]
སྡུག་བསྔལ་བ་ཞེས་བྱ་བ་ནི་སྙིང་རྗེའི་གཞིར་བསྟན་ཏོ། །

[Block 146]
བཀྲེན་པ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིག་གཞན་རྣམས་ནི་དེའི་བྱེ་བྲག་དང་ཕྱི་མ་ཕྱི་མ་བྱེ་བྲག་ཡིན་ནོ། །

[Block 147]
ཟང་ཟིང་མི༌[^109]གཏོང་བ་ནི་རྒྱུ་གསུམ་ལས་འགྱུར་ཏེ། སྦྱིན་པར་བྱ་བའི་དངོས་པོ་མེད་པའམ། སྦྱིན་པར་བྱ་བའི་དངོས་པོ་ཡོད་དུ་ཟིན་ཀྱང་སློང་བ་པོ་མ་འོངས་པའམ། སློང་བ་པོ་འོངས་སུ་ཟིན་ཀྱང་ལེགས་པར་འོངས་པ་མ་ཡིན་པ་སྟེ། བྱེ་བྲག་གསུམ་པོ་དག་གིས་དེ་མེད་པར་སྟོན་ཏོ། །

[Block 148]
ལེགས་པར་འོངས་པ་མ་ཡིན་པ་ནི་སྦྱིན་པའི་ལེའུ་ལས་དུག་ལ་སོགས་པ་སྦྱིན་པར་མི་བྱའོ་ཞེས་སྔར་བསྟན་པ་བཞིན་ཏེ། དེ་མེད་པ༌[^110]ནི་ལེགས་པར་འོངས་པ་མ་ཡིན་ནོ། །

[Block 149]
ཆོས་ཀྱི་སྦྱིན་པ་ལ་ཡང་རྒྱུ་རྣམ་པ་གསུམ་པོ་དེ་དག་ཉིད་ཅི་རིགས་པར་བརྗོད་པར་བྱའོ། །

[Block 150]
དེ་ལ་ལེགས་པར་འོངས་པ་ནི་གླགས་ཚོལ་བ་ལ་གླེགས་བམ་སྦྱིན་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ་སོགས་པས་སྦྱིན་པར་མི་བྱ་བའི་རྒྱུ་མེད་པའོ། །

[Block 151]
ལག་པའམ་བོང་བའམ་དབྱུག་པས་ཞེས་བྱ་བ་ལ། ལག་པ་ལ་སོགས་པས་རྣམ་པར་འཚེ་བ་ནི་སྲོག་གཅོད་པའི་མི་དགེ་བའི་ལས་ཀྱི་ལམ་ལ་མ་གཏོགས་པར་བསྟན་ཏོ། །

[Block 152]
ལག་པ་ལ་སོགས་པ་གསུམ་སྨོས་པ་ནི་ལག་པའམ། ལག་པས་འཕངས་པའམ། ལག་པ་དང་འབྲེལ་བས་འཚེ་བ་བསྟན༌[^111]པས་དེ་དང་མཐུན་པས༌[^112]འཚེ་བའི་རྫས་གཞན་ཡང་བསྡུ་བའི༌[^113]དོན་ཏོ། །

[Block 153]
རྡེག་ཅེས་བྱ་བ་ནི་བསད་པ་ནི་མ་ཡིན་གྱི་རྡེག་པ༌[^114]ཙམ་དུ་བསྟན་ཏོ། །

[Block 154]
རྣམ་པར་འཚེ་བ་ཞེས་བྱ་བ་ལ་ཅུང་ཟད་རྣམ་པར་འཚེ་བ་ནི་རྣམ་པར་འཚེ་བའོ། །

[Block 155]
རྣམ་པར་ཐོ་འཚམས༌[^115]པར་བྱེད་ཅེས་བྱ་བ་ལ། ཤིན་ཏུ་ཐོ་འཚམས༌[^116]པར་བྱེད་པ་ནི་རྣམ་པར་ཐོ་འཚམས༌[^117]པའོ། །

[Block 156]
རྡེག་པ༌[^118]ལ་སོགས་པས་ནི་ཆུང་ངུ་དང་འབྲིང་དང་ཆེན་པོ་བསྟན༌[^119]ཏོ། །

[Block 157]
ཁྲོ་བའི་བསམ་པ་ཁོ་ན་ཞེ་ལ་བཟུང་ལ༌[^120]ཞེས་བྱ་བ་ནི་རྣམ་པར་ཐོ་འཚམས་པར༌[^121]དེའི་ཕན་པ་མ་ཡིན་པའི་ཐབས་ཀྱི་དངོས་པོ་བསྟན་ཏོ། །

[Block 158]
ཤད་ཀྱིས་སྦྱངས་ཀྱང་མི་ཉན་པ་དང་། ཉན་དུ་ཟིན་ཀྱང་སྦྱོར་བས་མི་བཟོད་པ་དང་། ཉན་ཅིང་བཟོད་དུ་ཟིན་ཀྱང་བསམ་པས་མི་གཏོང་ངོ་། ། དམ་པའི་ཆོས་ལྟར་བཅོས་པ་རྣམས་ལ་མོས་པ་ཞེས་བྱ་བ་དེ་ལ། མོས་པ་ནི་འདུན་པ་སྐྱེད་པ་དང་། འདོད་པ་སྐྱེད་པའོ། །

[Block 159]
སྟོན་པ་ནི་འཆད་པའོ། །

[Block 160]
འཇོག་པ་ནི་འགོད་པའོ། །

[Block 161]
སོགས་པ་ཞེས་བྱ་བ་ནི་འཕེལ་བར་འགྱུར༌[^122]བའོ། །

[Block 162]
ཡོངས་སུ་འཛིན་པ་ཞེས་བྱ་བ་ནི་བསྐྱེད་པའི་ཕྱིར་རོ། །

[Block 163]
བསམ་པ་རྣམ་པར་དག་པ་ཞེས་བྱ་བ་ནི་ས་ལ་འཇུག་པར་བྱ་བའི་ཕྱིར་རོ་དེས་མགུ་བར་བྱེད་ཅེས་བྱ་བ་ནི་བསམ་པ་ཐག་པ་ནས་དགའ་བ་སྐྱེད་དོ། །

[Block 164]
དགའ་བ་ནི་སྦྱོར་བའི་སྒོ་ནས་གནས་པའོ། །

[Block 165]
ཡོན་ཏན་དུ་ལྟ་བ་ཅན་དུ་གྱུར་པ་ཞེས་བྱ་བ་ལ། ཕམ་པའི་གནས་ལྟ་བུའི་ཆོས་དེ་དག་ཉིད་ལ་འདི་དག་ནི་ཡོན་ཏན་ཡིན་ནོ་སྙམ་པའི་ངང་ཚུལ་ཅན་གང་ཡིན་པ་དེ་ནི་ཡོན་ཏན་དུ་ལྟ་བ་ཅན་ནོ། །

[Block 166]
འདི་ལྟ་སྟེ་ཕམ་པའི་ཆོས་རྣམས་བྱས་པས་དགེ་སློང་གིས་སོ་སོར་ཐར་པའི་སྡོམ་པ་གཏང་བར༌[^123]གྱུར་བ་བཞིན་དུ་བྱང་ཆུབ་སེམས་དཔའི་ཚུལ་ཁྲིམས་ཀྱི་སྡོམ་པ་ཡང་དག་པར་བླངས་པ་གཏོང་བར༌[^124]མི་འགྱུར་རོ། །

[Block 167]
བྱང་ཆུབ་སེམས་དཔས༌[^125]ནི་ཡང་དག་པར་བླངས་པ་ཡོངས་སུ་བཏང་དུ་ཟིན་ཀྱང་ཚེ་འདི་ལ་བྱང་ཆུབ་སེམས་དཔའི་ཚུལ་ཁྲིམས་ཀྱི་སྡོམ་པ་ཡང་དག་པར་བླངས་པའི༌[^126]ཕྱིར་ནོད་པའི་སྐལ་བ་ཡོད་དེ་ཞེས་བྱ་བ་ནི་ཁྱད་པར་དེ་གཉིས་ཡོད་པ་ཁོ་ནའི་ཕྱིར་ཕམ་པའི་གནས་ལྟ་བུ་ཞེས་བྱའི༌[^127]དེ་མ་ཡིན་པར་གལ་ཏེ་རྣམ་པ་ཐམས་ཅད་དུ་འདྲ་བར་འདོད་ན་ནི་ཕམ་པའི་ཆོས་རྣམས་ཞེས་བརྗོད་པའི་རིགས་སོ། །

[Block 168]
གཞན་ཡང་ཕམ་པའི་ཆོས་གཞན་དག་ལས་ཁྱད་པར་དུ་གྱུར་པ་གསུམ་བསྟན་པའི་ཕྱིར། ཚེ་བརྗེས་སུ༌[^128]ཟིན་ཀྱང་ཞེས་བྱ་བ་ལ་སོགས་པ༌[^129]བརྩམས་སོ། །

[Block 169]
མཆོད་པའི་དམ་པས་ཞེས་བྱ་བ་ནི་སྒྲུབ་པའི་མཆོད་པ་ཡང་བསྡུའོ། །

[Block 170]
ཇི་སྐད་ཡོངས་སུ་བརྗོད་པའི་གཞི་ལས་བྱང་ཆུབ་སེམས་དཔའི་འདུལ་བ་དང་འགལ་བ་ཉེས་བྱས་ཀྱི་ནོངས་པ་བྱུང་སྟེ་ཞེས་བརྗོད་ལ་ལྷག་མ་ནི་དགེ་སློང་ཉེས་བྱས་འཆགས་པ་ཇི་ལྟ་བ་དེ་བཞིན་དུ་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ཉེས་བྱས་ཀྱི་ནོངས་པ་བྱུང་བ་དེ་བདག་གིས་བཙུན་པའི་སྤྱན་སྔར་ནོངས་པ་ལ་ནོངས་པར་མཐོལ་ལོ། །

[Block 171]
བཤགས་སོ། །

[Block 172]
བསྒྲགས་སོ། །

[Block 173]
མི་འཆབ་པོ། །མཐོལ་ཞིང་བཤགས་ཏེ་བསྒྲགས་ན་བདག་བདེ་བར་འགྱུར་གྱི་མ་མཐོལ་མ་བཤགས་མ་བསྒྲགས་ན་ནི་དེ་ལྟ་མ་ལགས་སོ་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 174]
ཉེས་པ་དེ་དག་མཐོང་ངམ། དེས་ཀྱང་མཐོང་ངོ་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 175]
ཕྱིན་ཆད་སྡོམ་པར་བྱེད་དམ། ལེགས་པར་བསྡམས་པར༌[^130]འཚལ་ལོ་ཞེས་དེ་སྐད་ལན་གཉིས་ལན་གསུམ་དུ་བརྗོད་པར་བྱའོ། །

[Block 176]
བྱང་ཆུབ་སེམས་དཔའི་ཉེས་པ་རྣམས་ནི་ཆུང་ངུ་དང་འབྲིང་དང་ཆེན་པོར་རིག་པར་བྱའོ། །

[Block 177]
འདི་ལྟ་སྟེ་གཞི་བསྡུ་བ་ལས་འབྱུང་བ་བཞིན་ནོ་ཞེས་བྱ་བ་ནི་རྣམ་པ་ལྔས་ཉེས་པ་རྣམས་ཆུང་ངུ་དང་། འབྲིང་དང་། ཆེན་པོར་འགྱུར་བར་རིག་པར་བྱ་སྟེ། ལྔ་གང་ཞེ་ན། ངོ་བོ་ཉིད་དང་། བྱེད་པ་དང་། བསམ་པ་དང་། གཞི༌[^131]དང་། བསྩོགས༌[^132]པའོ། །

[Block 178 [VERSE]]
དེ་ལ་ཕམ་པ་ནི༌[^133]ཉེས་པ་ཆེན་པོ་ཡིན་ནོ། །
དགེ་འདུན་ལྷག་མ་ནི་འབྲིང་ངོ་། །
དེ་མ་ཡིན་པ་ནི་ཉེས་པ་ཆུང་ངུའོ། །

[Block 179]
རྣམ་གྲངས་གཞན་ཡང་ཕམ་པ་དང་དགེ་འདུན་ལྷག་མ་རྣམས་ནི་ལྕི་བའོ། །

[Block 180]
སོ་སོར་བཤགས་པར་བྱ་བ་ནི་འབྲིང་ངོ་། །ཉེས་བྱས་ནི་ཡང་བར་རིག་པར་བྱའོ། །
--- END BLOCKS ---
