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
[Block 911]
བསྒོམ་བྱ་མེད་ཅེས་བྱ་བ༌[^384]ནི་འང་སྟེ། སྔ་མ་གཉིས་ལྟ་བུའོ། །

[Block 912]
དེ་ཡང་ལྟ་བའི་སྐབས་སུ་སེམས་དང་སེམས་ལས་བྱུང་བ་རང་བཞིན་མེད་པའི་ཕྱིར་རོ། །

[Block 913]
འོན་ཏེ་བསྒོམ་པ་ནི་ལམ་གྱི་གཙོ་བོ་ཡིན་ན། དེ་མེད་ན་འབྲས་བུ་དང་ལམ་གཞན་དག་ཇི་ལྟར་ཡོད་པར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར། ལྷ་དང་སྔགས་ཀྱང་ཡོད་མ་ཡིན། །ཞེས་གསུངས་སོ། །

[Block 914]
དེ་ཡང་འབྲས་བུ་གཞན་དག་ཉེ་བར་མཚོན་པ་སྟེ། སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཀྱང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 915]
ལམ་ཡང་གཞན་དག་ཉེ་བར་མཚོན་པ་སྟེ། ཕྱག་རྒྱ་དང་དཀྱིལ་འཁོར་དང་སྒྲུབ་པ་དང་ཕྲིན་ལས་ཀྱང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 916]
རྡོ་རྗེ་ཁུ་ཚུར་ལ་སོགས་པ༌[^385]བཏགས་པའི་ཕྱག་རྒྱ་ཡང་ཡོད་པ་མ་ཡིན། མེ་ལ་མར་ལྡུགས་པའི་སྦྱིན་སྲེག་ཀྱང་། རུ་རུ་སྥུ་རུ་ལ་སོགས་པ་སྙིང་པོ་དང་ཕྲེང་བའི་སྔགས་བཏགས་པར་ཡོད་པ་མ་ཡིན། ཁ་དོག་དང་དབྱིབས་སུ་བཏགས་པ་དང་རྩིག་པ༌[^386]ལ་སོགས་པའི་དཀྱིལ་འཁོར་དེ་ཡང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 917]
དེ་ལྟ་བུའི་སྒོམ་པའི་ཉམས་དེ་ཡང་རང་བཞིན་མེད་པ་ཙམ་དུ་བྱ་བའི་ཕྱིར་ཕུན་སུམ་ཚོགས་པའི་གཞིར་ཇི་ལྟར་འགྱུར་ཞེ་ན། སྤྲོས་པ་མེད་པའི་རང་བཞིན་ལས༌[^387]ཡང་དག་གནས་ཞེས་བྱ་བ་ལ་སོགས་པ༌[^388]གསུངས་སོ། །

[Block 918]
དེ་ཡང་ལྟ་བ་ལ་སོགས་པའི་སྐབས་སུ་སྐྱེད་བྱེད་མ་སོགས་པའི་ཐབས་ཐུན་མོང་མ་ཡིན་པའི་ཡིད་སོ་སོར་རྟོག་པའི་བདེ་བ་ཉམས་སུ་བླངས་པས། འདིར་སྒོམ་པའི་ཉམས་མཆོག་ཏུ་བདེ་བ་ཆེན་པོ་ཁོ་ནར་རང་སྐྱེ་བར་འགྱུར་ཏེ། དེ་ཡང་མི་རྟོག་པ༌[^389]རང་རྣལ་དུ་འཇུག་པས་སྤྲོས་པ་མེད་པའི་ཤེས་པའོ། །

[Block 919]
རང་བཞིན་ལས་ཞེས་པ་ནི་བདེ་བ་ཆེན་པོ་གཉུག་མ་ལས་སོ། །

[Block 920]
ལས་ཞེས་པ་ནི་ཐམས་ཅད་ཀྱི་འབྱུང་ཁུངས་ལྔ་པར་སྦྱར༌[^390]བའམ། ཡང་ན་ལས་ཞེས་འགར་བྱེད་ཀྱི་ལྔ་པར་སྦྱར་ཏེ། སྤྲོས་པ་མེད་པས་ཐམས་ཅད་བཀག་ནས་སྣང་བའི་ཡེ་ཤེས་ཆེན་པོ་ཉིད་ཡང་དག་གནས་ཞེས་པ་ནི་གཉིས་མེད་འོད་གསལ་བའི་བདག་ཉིད་དོ། །

[Block 921]
སྔགས་དང་ལྷ་ནི་ཉེ་བར་མཚོན་པའི་འབྲས་བུ་ནི། [^391]སྔགས་ནི་དེ་ཉིད་ཡིད་ཅན་ཐམས་ཅད་སྐྱོ་བར་བྱེད་པས་ན་སྔགས་སོ། །

[Block 922]
སྣང་བ་ཐམས་ཅད་རྒྱས་འདེབས་པར་བྱེད་པས་ན་ཕྱག་རྒྱའོ། །

[Block 923]
རྣམ་པར་རྟོག་པ་ཐམས་ཅད་སྲེག་པར་བྱེད་པས་སྦྱིན་སྲེག་གོ། །

[Block 924]
ཁ་དོག་སྣ་ཚོགས་པར་སྣང་བས་ན་རྟེན་གྱི་དཀྱིལ་འཁོར་རོ། །

[Block 925]
དེ་ནས་ཕུན་སུམ་ཚོགས་པའི་བདག་ཉིད་གདོད་མ་ནས་གྲུབ་པའི་ཕྱིར་ལྷན་ཅིག་སྐྱེས་པའོ། །

[Block 926]
ད་ནི་འབྲས་བུ་ཕུན་སུམ་ཚོགས་པ་དེ་བཤད་པའི་ཕྱིར་རྣམ་སྣང་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 927]
དེ་ལ་ཡང་བདེ་བའི་ཡེ་ཤེས་དེ་ཉིད་འོད་ཟེར་མཐར༌[^392]ཐུག་པ་མེད་པར་ཁྱབ་པས་རྣམ་སྣང་ངོ་། །མི་བསྐྱོད་ཅེས་པ་ནི་མི་མཐུན་པས་སོ། །

[Block 928]
དོན་ཡོད་གྲུབ་ཅེས་པ་ནི་སངས་རྒྱས་ཀུན་གྱི་ལས་སོ། །

[Block 929 [VERSE]]
རིན་ཆེན་ཞེས་པ་ནི་རྟོག་པ་དཀོན་པས་སོ། །
དཔག་མེད་ཅེས་པ་ནི་བདེ་ཆེན་གྱི་ཆེ་བའོ། །
སེམས་དཔའ་ཞེས་པ་ནི་རྡོ་རྗེ་སེམས་དཔའ་སྟེ།

[Block 930]
མཆོག་ཏུ་བདེ་བ་ཉིད་དོ། །

[Block 931]
དེ་དག་ནི་འཇིག་རྟེན་ལས་འདས་པའི་ལྷ་ཡིན་ན། འཇིག་རྟེན་པའི་འབྲས་བུ་ཕུན་སུམ་ཚོགས་པ་མེད་དམ་ཞེ་ན། དེའི་ཕྱིར་ཚངས་པ་ལ་སོགས་པ་བསྟན་ཏོ།[^393] །དེ་བཤད་པ་ཡང་ཚིག༌[^394]གསུམ་གྱིས་བསྟན་ཏེ། ཡང་བདེ་བ་ཆེན་པོ་དེ་ཉིད་མི་རྟོག་པ་ལ་ཁྱབ་པ་དང་། བདེ་བ་དང་གཅིག༌[^395]གསལ་བར་བསྟན་པའི་ཕྱིར། ཐམས་ཅད་སངས་རྒྱས་དེ་ཉིད་བརྗོད། །ཅེས་པའོ། །

[Block 932]
ཐམས་ཅད་ཅེས་པ་ནི་བཤད་པའི་སྐབས་སུ། ཐམས་ཅད་ཀུན་གྱི་བདག་ཉིད་གནས། །ཞེས་པ་སྟེ།[^396] མི་རྟོག་པས་ཁྱབ་པའོ། །

[Block 933]
དེ་ཉིད་བརྗོད་ཅེས་པ་ནི་བཤད་པའི་སྐབས་སུ་དམ་པའི་བདེ་བས་དེ་ཉིད་ཅེས་པ་སྟེ།

[Block 934 [VERSE]]
བདེ་བ་རོ་གཅིག་ཏུ་བསྡུས་པའོ། །
སངས་རྒྱས་ཞེས་པ་ནི་བཤད་པའི་སྐབས་སུ།

[Block 935]
བདེ་བ་རྟོགས༌[^397]ཕྱིར་རྣམ་སངས་རྒྱས། །ཞེས་པ་སྟེ། གཉིས་མེད་རང་རིག་འོད་གསལ་བའོ། །

[Block 936]
འཇིག་རྟེན་དང་འཇིག་རྟེན་ལས་འདས་པའི་ཕུན་སུམ་ཚོགས་པ་དེ་ལ་ལྷན་ཅིག་ཅེས༌[^398]ཅིའི་ཕྱིར་ཞེ་ན་གང་གི་ཕྱིར་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 937]
དེ་ཡང་ཧ་ནི་ལུས་སོ། །

[Block 938]
བྷ་ག་ནི་འབྱུང་བ་དེ་སྟེ་དེའི་ལུས་ལས་འབྱུང་བས་ལྷའོ། །

[Block 939]
དེ་ཡང་ལྷན་ཅིག་སྐྱེས་པའི་དོན་ཡིན་ཏེ། ཚངས་པ་ལ་སོགས་པ་ནི་ཀུན་རྫོབ་ལྷན་ཅིག་སྐྱེས་པས་བསྡུས་ལ༌[^399]རྣམ་སྣང་ལ་སོགས་པ་དོན་དམ་ལྷན་ཅིག་སྐྱེས་པས་བསྡུས་པས་ཚིགས་སུ་བཅད༌[^400]པ་གཉིས༌[^401]ཀྱི་དོན་ནོ། །

[Block 940]
ཡང་ན་ཕུན་སུམ་ཚོགས་པའི་བྷ་ག་ཝཱན་ཇི་ལྟ་བུ་ཞེ་ན། བུདྡྷ་འདི་ལ་ཞེས་པ་སྟེ། གོང་གི་འོད་གསལ་བའོ། །

[Block 941]
བྷ་ག་ཝཱན་ཞེས་པ་བྷ་བཱན་ཛི་བ་སྟེ་རྟོག་པ་ལ་སོགས་པ་རང་ཤུགས་ཀྱིས་འཇོམས་པ༌[^402]གང་ལ་ཡོད་པ་དེ་ལ་བཅོམ་ལྡན་འདས་ཞེས་བྱའོ། །

[Block 942]
ཡང་ན༌[^403]བྷ་ག་ནི་སྐལ་བ་སྟེ༌[^404]དབང་ཕྱུག་ལ་སོགས་པའོ། །

[Block 943]
དེས་ན་ཚིགས་སུ་བཅད་པ་ཕྱེད་དང་གཉིས་ཀྱིས་བསྟན་ཏོ། །

[Block 944]
འོན་ཏེ་ཆོས་ཐམས་ཅད་ལ་ལྟ་བ་ཤེས་རབ་དང་ཐབས་དབྱེར་མེད་དུ་གཏན་ལ་དབབ་པ་དང་། སྒོམ་པའི་ཉམས་རང་སྐྱེས་པའི་དེ་ཁོ་ན་ཉིད་དེ་ལྟ་བུ་ཡིན་ན་རྟེན་ལས་ཀྱི་ཕྱག་རྒྱ་མ་དང་སྲིང་མོ་ལ་སོགས་པའི་དེ་ཁོ་ན་ཉིད་ཇི་ལྟ་བུ་ཞེ་ན། དེ་རྣམས་ཐབས་དང་ཤེས་རབ་དབྱེར་མེད་དུ་ཤེས་པར་བྱ་བའི་ཕྱིར། གང་གི་ཕྱིར་ཞེས་བྱ་བ་ལ་སོགས་པས་སྟོན་ཏོ། །ཤེས་རབ་ཅེས་བརྗོད་པར་བྱ་བ་ཞེས་པ་ནི་ཤེས་རབ་ཀྱི་དེ་ཁོ་ན་ཉིད་སྟོང་པ་ཉིད་དོ། །

[Block 945]
གང་ཕྱིར་སྐྱེ་འགྲོ་སྐྱེད་པ་ཞེས་པ་ནི་སྟོང་པ་ཉིད་ཀྱི་མཚན་ཉིད་ཀྱི་མཚན༌[^405]མ་ཅིར་ཡང་སྣང་བ༌[^406]ཡང་། མི་འགོག་པར་ཡུམ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་མའོ། །ཤེས་རབ་སྲིང་མོ་ཞེས་བྱ་ཉིད། །ཅེས་བྱ་བ་ནི། བྷ་ག་ཝཱན་ནི་སྟེ༌[^407]སྐལ་པ་དང་ལྡན་པའོ། །

[Block 946]
དེའི་ཕྱིར་གང༌[^408]ཕྱིར་སྐལ་བ་སྟོན། །ཞེས་པ་སྟེ། སྐལ་པ་ནི་ཐབས་ཏེ་ཤེས་རབ་སྟོང་པ༌[^409]ཉིད་དང་བཅས་པའི་ཕྱིར་རོ། །

[Block 947]
དེ་བཞིན་དུ་བཙོ་བླག༌[^410]མོ་དང་གར་མ་ལ་ཡང་ཐབས་དང་ཤེས་རབ་གོ་རིམས་བཞིན་ནོ། །

[Block 948]
གཡུང་མོ་ཡང་ཐབས་སུ་བསྟན་པ་སྟེ། དེ་བཞིན་དུ་གདོལ་བ་མོ་དང་། བྲམ་ཟེ་མོ་ལ་ཡང་ཐབས་སུ་ཤེས་པ་ཤུགས་ཀྱིས་བསྟན་ནོ། །

[Block 949]
དེ་དག་ནི་ལྟ་བ་དང་སྒོམ་པ་སྟེ་ཤེས་བྱའི་དེ་ཁོ་ན་ཉིད་དོ། །

[Block 950 [HEADING]]
#### སྒོ་གསུམ་ནུས་པ་ཅན་དུ་བྱེད་པ་སྒྲུབ་པ་པོ་དེ་ཁོ་ན་ཉིད། ^1-5-3-0
--- END BLOCKS ---
