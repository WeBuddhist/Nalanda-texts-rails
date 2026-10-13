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
[Block 736]
དབྱེ་བ་གོ་རིམས་ངེས་པ་ནི་སྐྱེ་བའི་གོ་རིམས་ཏེ། བྱམས་པ་ནི་བརྩེ་བ་དང་ལྡན་པ་ལས༌[^265]སྙིང་རྗེ་སྐྱེས་པས་དེ་བཞིན་དུ་སྦྱར་རོ། །

[Block 737]
དམིགས་པའི་ཡུལ་ནི་བདེ་འགྲོ་དང་ངན་འགྲོ་དང་། ཉན་ཐོས་དང་རང་སངས་རྒྱས་དང་། སེམས་ཅན་ནས་སངས་རྒྱས་ཀྱི་བར་དུ་རིམ་པར་སྦྱར་རོ། །

[Block 738]
བསྒོམ་པའི་ཐབས་ནི་ཆེ་འབྲིང་རྣམ་པ་དགུ་རུ་ཕྱེ་སྟེ།

[Block 739]
དང་པོ་བྱམས་པ་ཞེས་པ་བཤེས་འབྲེལ་ལྟ་བུ་སྟེ། རང་གི་སྙིང་དུ་བཅུག་པ་གཅིག་ལ་བྱམས་པ་སྐྱེ། དེ་བཞིན་དུ་གཉེན་རབ་འབྲིང་གསུམ་ལ་སྦྱར་རོ། །

[Block 740]
ཡང༌[^266]ཐ་མལ་པ་རབ་འབྲིང་གསུམ་དང་དགྲ་རབ་འབྲིང་གསུམ་དུ་སེམས་ཅན་ཐམས་ཅད་ལ་བསྒོམ་མོ། །

[Block 741]
ཡང་དེ་བཞིན་དུ་སྡུག་བསྔལ་ཆེ་འབྲིང་དགུ་དང་ཟག་པ་མེད་པ་བླ་ན་མེད་པའི་བདེ་བ༌[^267]རབ་འབྲིང་དགུ་རུ་གོང་མ་རྣམས་ལ་བསྒོམ་མོ། །

[Block 742]
བཏང་སྙོམས་ནི་དགའ་བའི་སྣོད་དུ་བསྒོམ་པའམ་ཡང་ན་དམིགས་པ་མེད་པར་བསྒོམ་མོ། །

[Block 743]
སྟོང་པ་ཉིད་སྔགས་དང་བཅས་པ་ཡེ་ཤེས་ཀྱི༌[^268]ཚོགས་བསགས་ལ། [^269]ཡང་ན༌[^270]སྟོང་པའི་བྱང་ཆུབ་ཅེས་པས་གཟུང་ངོ་། །ཡེ་ཤེས་ཀྱི༌[^271]ཚོགས་ཀྱི་རྗེས་ལ་རང་གི༌[^272]མདུན་མེད་དེ༌[^273]སྟོང་པ་ཞིག་ཅེ་ན། རང་གི་བློས་ཆོས་སྟོང་པར་བྱས་པས་རང་གི་ལུས་ཐ་མལ་པ་ལྟར་སྣང་བ་དེའིའོ། །

[Block 744]
མདུན་དུ་རེ་ཕ་ཉི་མ་ལ། །ཞེས་པ་ལ༌[^274]སོགས་པ་ཚིགས་སུ་བཅད་པ་གཉིས་ཀྱིས་རྟེན་བསྒྲུབས༌[^275]ཏེ། རཾ་ལས་ཉི་མའི་དཀྱིལ་འཁོར་ཧཱུཾ་ལས་སྣ་ཚོགས་རྡོ་རྗེ་ལ་ཧཱུཾ་གིས་མཚན་པ། དེ་ལས་འོད་ཟེར་འཕྲོས་པས་ཕྱོགས་སུ་རང་སྟེང་དུ་གུར་བཅིང་བ་ཞེས་བྱ་སྟེ།

[Block 745 [VERSE]]
འོག་ཀྱང་རྡོ་རྗེའི་ས་གཞིའོ། །
ཆོས་ཀྱི་འབྱུང་གནས་ནི་བསྒོམས༌[^276]ན་ཡང་སྒོམ།
མ་བསྒོམས་ཀྱང་འགལ་བ་མེད་དོ། །
དེའི་ནང་དུ་རོ་བསྒོམ་མོ། །

[Block 746]
ད་ནི་བརྟེན་པ༌[^277]ལྷ་བསྒོམ་པ་ནི་རྡོ་རྗེ་རྣམ་བཞིས་བསྐྱེད།

[Block 747 [VERSE]]
ཡང་ནི་སྟེ༌[^278]ཡེ་ཤེས་ཀྱི་ཚོགས་ལ་ལྟོས་པའོ། །
སྟོང་པ་སྟེ་ཆོས་ཉིད་དང་།

[Block 748]
བྱང་ཆུབ་སྟེ་ཡེ་ཤེས་སོ། །

[Block 749]
དེ་ནས་གཉིས་པ་ལ་ས་བོན་བསྡུ་བ་ནི་ཧཱུཾ་ལས་བྱུང་བའོ། །

[Block 750]
གསུམ་པ་ལ་གཟུགས་བརྙན་རྫོགས་པའོ།[^279] །རྡོ་རྗེ་ནི་ཁ་དོག་ནག་པོ་འཇིགས༌[^280]ཆེན་ནོ།[^281] །

[Block 751]
བཞི་པ་ལ་ནི་ཡིག་འབྲུ་དགོད་པ་ནི།

[Block 752 [VERSE]]
རྡོ་རྗེའི་ལྟེ་བའི་དབུས་གནས་པར། །
ཡང་ནི་ཧཱུཾ་གི་དེ་ཉིད་བསྒོམ། །

[Block 753]
དེ་ལས་ཅིར་འགྱུར་ཞེ་ན། ཧཱུཾ་གི་རྣམ་པར་གྱུར་པ་ལ་སོགས་པ་ཚིགས་སུ་བཅད་པ་ཕྱེད་དང་གཉིས་སོ། །

[Block 754]
སེམས་དཔའ་སུམ་བརྩེགས༌[^282]བསྒོམ། རང་འདྲ་བའི་ཡེ་ཤེས་པ་དགུག །སྐྱེ་མཆེད༌[^283]བྱིན་གྱིས་བརླབ་པ་མོས་ཚུལ་ལམ་བསྐྱེད་པའི་ཚུལ་གང་རུང་བྱའོ། །

[Block 755]
དབང་བསྐུར་བ་ནས་མཆོད་བསྟོད་བདུད་རྩི་མྱང་བ་བྱས་ལ། རྫོགས་པའི་རིམ་པ་ཅུང་ཟད་བསྒོམ། །སྔགས་ཀྱི་བཟླས་པ་བྱ། གཏོར་མ་བཏང་།[^284] ཡེ་ཤེས་པ་གཤེགས་སུ་གསོལ།

[Block 756 [VERSE]]
དམ་ཚིག་པ་རང་ལ༌[^285]བསྡུས་ལ་སྤྱོད་ལམ་བྱའོ། །
དེ་བཞིན་དུ་ཐུན་བཞིའི་རིམ་པ་བསྒོམ་མོ། །

[Block 757 [HEADING]]
##### དཀྱིལ་འཁོར་གྱི་འཁོར་ལོ། ^1-3-1-2-0

[Block 758]
དཀྱིལ་འཁོར་གྱི་འཁོར་ལོ་སྣ་ཚོགས་དང་རྟེན་བསྒྲུབ་པ་ནི་སྔ་མ་ལྟར་རོ། །

[Block 759]
རྟེན་ལ་ཁྱད་པར་འདི་ཡོད་དེ། གུར་བཅིངས་པ༌[^286]ཡང་རྣམ་པར་བསྒོམ་གྱི་ཚིགས་སུ་བཅད་པ་དང་པོས་ནང་ཆོས་འབྱུང་ལེའུ་བརྒྱད་པ་ལྟར༌[^287]འཁོར་ལོ་སྔོན་དུ་ཅི་རིགས་པ་ལ་སོགས་པས་གཞལ་ཡས་ཁང་བསྒོམས་ལ། དེ་ཡང་ཁྱད་པར་འདི་ཡིན་ཏེ། འཕར་མ་གཅིག་པའོ། །

[Block 760]
དེ་ནས་ཨཱ་ལི་ཟླ་བ་ཀཱ་ལི་ཉི་མ་ལ་སོགས་པ་ཚིགས་སུ་བཅད་པ་གཉིས་ཀྱིས་ཆོ་ག་བསྟན་པ་ནི། ཨཱ་ལི་ལས་ཟླ་བ་བསྒོམས་པ༌[^288]ནི་མེ་ལོང་ལྟ་བུའི་ཡེ་ཤེས་ལས་མངོན་པར་བྱང་ཆུབ་པའོ། །

[Block 761]
ཀཱ་ལི་ལས་ཉི་མ་བསྒོམས་པ༌[^289]ནི་མཉམ་པ་ཉིད་ཀྱི་ཡེ་ཤེས་ལས་མངོན་པར་བྱང་ཆུབ་པའོ། །

[Block 762 [VERSE]]
ས་བོན་ནང་དུ་སོན་གྱུར་པ། །
དེ་ཉིད་སེམས་དཔའ་ཞེས་བྱར་བརྗོད། །

[Block 763]
ཅེས་པ་ནི་ཧཱུཾ་ལས་རྡོ་རྗེར་གྱུར་པ་ནི་སོ་སོར་རྟོག་པའི༌[^290]ཡེ་ཤེས་ལས་མངོན་པར་བྱང་ཆུབ་པའོ། །

[Block 764 [VERSE]]
ནམ་མཁའི་དཀྱིལ་འཁོར་ཁྱབ་པར་ནི། །
རང་གི་ལུས་མཚུངས་རྣམ་པར་སྤྲོ། །
བསྡུས་ནས་སྙིང་གར་བཀུག་པ་ན། །

[Block 765]
བྱ་བ་ནན་ཏན་གྱི་ཡེ་ཤེས་ལས་མངོན་པར་བྱང་ཆུབ་པའོ། །

[Block 766]
རང་གི་ལུས་མཚུངས་རྣམ་པར་སྤྲོ་བ་ནི་དོན་དེ་བཞིན་གཤེགས་པ་ཡིན་ཡང་རྣམ་པ་ལྷ་མོར་སྤྲོ༌[^291]སྟེ། །སྙིང་གར་བཀུག་ཅེས་པ་ནི་ཧྲྀ་ད་ཡ་སྙིང་པོ་སྟེ།[^292] རྡོ་རྗེའི་ལྟེ་བ་ལ་བསྡུ་བའོ། །

[Block 767]
དེ་རྣམས་ཡོངས་སུ་གྱུར་པ་ནི་བྱ་བ་ནན་ཏན་གྱི་ཡེ་ཤེས་ལས་མངོན་པར་བྱང་ཆུབ་པའོ། །

[Block 768]
ཡོ་གཱི་ཞེ་སྡང་བདག་ཉིད་གྱུར་པ་ནི་སྐུ་རྫོགས་པ༌[^293]ཆོས་ཀྱི་དབྱིངས་ཀྱི་ཡེ་ཤེས་ལས་མངོན་པར་བྱང་ཆུབ་པའོ། །

[Block 769]
འདིར་ནི་ལུགས་གཉིས་ཏེ། སྔོ་དང་ཉི་མ་མཚུངས་པ་ལ་སོགས་པ་གཙོ་བོ་བསྟན་པའམ། ཡང་ན་རྒྱུའི་རྡོ་རྗེ་འཆང་དཀར་པོར་བསྐྱེད་དེ། དེ་ནས་ཤིང་འབྲས་འཆོས་པའི་ཚུལ་དུ་ནག་པོར་གྱུར་པའོ། །

[Block 770]
རྣལ་འབྱོར་མ་ལ་སོགས་པས་འཁོར་བསྟན་ཏེ།

[Block 771 [VERSE]]
དེ་དག་གང་གིས་བསྐྱེད་ཅེ་ན། །
ཧཱུཾ་གི་ཡི་གེ་འདོན་པའི་བདག །

[Block 772]
ཅེས་སྨོས་ཏེ། དེ་ལ་ཡང་ཚུལ་གཉིས་ཏེ། ཡུམ་ཡོད་པ་དང་མེད་པའོ། །

[Block 773]
ཡུམ་མེད་ན་སྙིང་གའི་ཧཱུཾ་ལས་ཡིག་འབྲུ་སྤྲོས་ཏེ། འཁོར་རྣམས་རྗེས་སུ་མཐུན་པའི་མངོན་པར་བྱང་ཆུབ་པ་ལྔས༌[^294]བསྐྱེད་དེ། ཡུམ་ཡོད་ན་རྗེས་སུ་ཆགས་པ་ཞུ་བ་ལས་རྒྱུའི་རྡོ་རྗེ་འཆང་བཞེངས་ནས་བསྒྲུབ་པ༌[^295]དང་བསྲུབ་པའི་སྦྱོར་བ་ལས་འཁོར་མངལ་སྐྱེས་ཀྱི་ཚུལ་དུ་རྗེས་སུ་མཐུན་པའི་མངོན་པར་བྱང་ཆུབ་པ་ལྔས་བསྐྱེད། [^296]སྔ་མ་ལྟར་ན་ཧཱུཾ་གི་ཡི་གེ་ལས་འདོན་བའི་བདག་ཅེས་བརྗོད་དོ། །

[Block 774]
ཕྱི་མ་ལྟར་ན་ཧཱུཾ་གི་ཡི་གེ་སྒྲོགས་པའི༌[^297]བདག་ཅེས་བརྗོད་དོ། །

[Block 775]
ཡུམ་ནི་མན་ངག་གིས་བདག་མེད་མ༌[^298]ལ་བཞེད་དོ། །
--- END BLOCKS ---
