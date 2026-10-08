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
[Block 1 [HEADING]]
## ༄༅། །རྒྱུད་ཀྱི་རྒྱལ་པོ་ཆེན་པོ་དཔལ་དགྱེས་པའི་རྡོ་རྗེའི་དཀའ་འགྲེལ་སྤྱན་འབྱེད།

[Block 2]
༄༅༅། །རྒྱ་གར་སྐད་དུ། ཤྲཱི་ཧེ་བཛྲ་ཏནྟྲ་མ་ཧཱ་རཱ་ཛ་སྱ་པཉྩི་ཀཱ་ནེ་ཏྲ་བི་བྷཾ་ག་ནཱ་མ། བོད་སྐད་དུ། རྒྱུད་ཀྱི་རྒྱལ་པོ་ཆེན་པོ་དཔལ་དགྱེས་པའི་རྡོ་རྗེའི་དཀའ་འགྲེལ་སྤྱན་འབྱེད་ཅེས་བྱ་བ།

[Block 3 [HEADING]]
## མཆོད་བརྗོད། ^I-0

[Block 4]
དཔལ་དགྱེས་པའི་རྡོ་རྗེ་ལ་ཕྱག་འཚལ་ལོ། །

[Block 5]
ས་མ་སརྦ༌[^1]ཨརྠ་སིདྡྷཿ། ན་མོ་གུ་རུ་པཱ་དཱ་ཡ།

[Block 6 [HEADING]]
## བརྟག་པ་དང་པོ། ^1-0

[Block 7 [HEADING]]
### ལེའུ་དང་པོ་རྡོ་རྗེ་རིགས་ཀྱི་ལེའུ། ^1-1-0

[Block 8 [HEADING]]
#### གླེང་གཞིའི་ངག། ^1-1-1-0

[Block 9]
ཨེ་ཝཾ་མ་ཡཱ་ཤྲུ་ཏ་ཨེ་ཀ་སྨིན་ས་མ་ཡེ་བྷ་ག་བཱན། སརྦ་ཏ་ཐཱ་ག་ཏ་ཀཱ་ཡ་བཱཀྩི་ཏྟ་ཧྲྀ་ད་ཡ་བཛྲ་ཡོ་ཥཱི་ཏ་བྷ་གེ་ཥུ་བི་ཛ་ཧཱ་ར། །གླེང་གཞིའི་ངག་དང་པོའོ། །

[Block 10]
འདི་ཡང་སྒྲའི་ཚུལ་དུ་བཤད་པ་དང་། དོན་གྱི་ཚུལ་དུ་བཤད་པའོ། །

[Block 11 [HEADING]]
##### སྒྲའི་ཚུལ་དུ་བཤད་པ། ^1-1-1-1-0

[Block 12]
སྒྲའི་ཚུལ་ལ་ཡང་གསུམ་སྟེ། སྒྲའི་བྱེད་པའི་གནས་དང་སྦྱར་བ་དང་། ནུས་པའི་རྩལ་དང་མིང་ཁྱད་པར་དུ་བཏགས་པའི་ཡོན་ཏན་ཏོ། །

[Block 13 [HEADING]]
###### སྒྲའི་བྱེད་པའི་གནས་དང་སྦྱར་བ། ^1-1-1-1-1-0

[Block 14]
བྱེད་པའི་དབང་དུ་བྱས་པ་ནི་སྒྲའི་གནས་དང་སྦྱར་ཏེ། དེ་ཡང་སྒྲ་པའི་ལུགས་ཀྱི་ཏི་ངན་ཏིའི་མཐའ་ཅན་དང་སུ་པནྟིའི་མཐའ་ཅན་ལས་འདིར་སུ་བནྟ་བྱཱ་ཀཱ་ར་ཎའི་གནས་བརྒྱད་དོ།[^2] །གང་ཞེས་བྱ་བ་ལ་སོགས་པ་ལས། །

[Block 15]
འདིར་གང་གིས་ཐོས་ན་བདག་གིས་ཐོས་ཞེས་གསུམ་པ་སྦྱར། གང་གི་ཚེ་སྟེ་དུས་ནི་དང་པོའམ་ཏི་ངན་ཏའི༌[^3]གནས་མི་སྦྱར། གང་ལས་ཐོས་ཞེས་པས་བཅོམ་ལྡན་འདས་ཞེས་ལྔ་པ་ལ་སྦྱར་བ་དང་། གང་དུ་ཞེ་ན། བྷ་ག་ལ་ཞེས་བདུན་པའམ་གཉིས་པ་སྦྱར་བ་དང་། བཞུགས་ཞེས་པར་འཁོར་བསྟན་པས་ཐོས་པ་དང་འབྲེལ་བས། འདི་རྣམས་ཀྱི་ཕྱིར་ཞེས་བྱ་སྟེ་བཞི་པའི་སྒྲ་སྦྱར་རོ། །

[Block 16 [HEADING]]
###### ནུས་པའི་རྩལ། ^1-1-1-1-2-0

[Block 17]
ནུས་པའི་རྩལ་ནི་འདི་སྐད་ཀྱིས་འདི་སྐད་ནས༌[^4]འབྲུ་ལ་ཨའི་རྣམ་པའོ་ཞེས་པ་རྒྱུད་མགོ་ཞབས་ཀྱི་དོན་འདྲེན་པ༌[^5]དང་། འདི་སྐད་ཀྱིས་ཡང་སྒྲོ་མ་བཏགས་པ་དང་། སྐུར་པ་མ་བཏབ་པར་བཅོམ་ལྡན་འདས་ལས་ཐོས་ཤིང་གཟུངས་ནས་བསྡུས་ཞེས་པ་དང་། ཉན་པ་རྣམས་གུས་པ་དང་བཅས་པའོ། །

[Block 18]
བདག་གིས་ཞེས་པ་ནི་བདག་གིས་མངོན༌[^6]སུམ་དུ་ཐོས་ཀྱི་རྒྱུད་ཀྱི་བརྒྱུད་པས༌[^7]མ་ཡིན་པར་སྟོན་པ་དང་། ཐོས་པ་ཞེས་པ་ནི་ཐོས་པ་རྐྱང་བ༌[^8]སྟེ། རྟོགས་པ་ནི་མ་ཡིན་པའོ། །

[Block 19]
ཐོས་པའི་གནས་སྐབས་ན་ཐོས་ཀྱིས་རྟོགས་པ་ནི་མ་ཡིན་ཏེ་རང་གི༌[^9]བྱས་པ་སྟོན་པ་ལ་ཁྱད་པར་མེད་པ་དང་། གཞན་མི་གུས་པས༌[^10]འགྱུར་བས༌[^11]སོ། །

[Block 20]
སྡུད་པ་པོའི་གནས་སྐབས་ནི་དོན་དང་ཚིག་དང་བཅས་པར་བསྡུས་པས་ཁྱད་པར་དུ་འགྱུར་རོ། །

[Block 21]
དུས་གཅིག་གིས་ནི་ཡོན་ཏན་གསུམ་འདྲེན་པར་བྱེད་དེ། དུས་གཅིག་ན་འདི་ཐོས་པ་གཞན་དག་ཀྱང་ཐོས་ཞེས་པས་མང་བར་སྟོན་པ་དང་། གཞན་དུ་མ་ཐོས་པ་དག་སྲིད་དོ་ཞེ་ན། བྱང་ཆུབ་སེམས་དཔའ་བརྩོན་འགྲུས་རྒྱུན་མི་འཆད་པ་དང་།

[Block 22 [VERSE]]
ཤེས་བྱའི་སྒྲིབ་པ་སྤོང་བར་གཙོར་བྱེད་པས་སོ། །
དེས་ནི་སྡུད་པ་པོ་ཆེ་བར་བསྟན་ཏོ། །

[Block 23]
ཡང་དུས་གཅིག་གིས་བསྟན་པ་དཀོན་པར་སྟོན་ཏོ།[^12] །དེའི་ཚེ་ཁོ་ན་གསུངས་ཀྱི་གཞན་གང་དུ་ཡང་མ་བསྟན་པས་ན་དཀོན་པའོ། །

[Block 24]
དུས་གཅིག་སྟོན་པ་ཆེ་བར་སྟོན་ཏེ།[^13] སྐད་གཅིག༌[^14]མ་ལ་ཐོས་པས་འཁོར་རྣམས་རྣམ་པར་ཐར་པའི་སྐྱེ་མཆེད་སྒྲུབ་ནུས་པའམ་བྱ་བ་རྫོགས་པའི་སྐད་ཅིག་གཅིག་ཅེས་བྱའོ། །

[Block 25]
བྷ་ག་ཝཱན་གྱིས་ནི་ཡོན་ཏན་གཉིས་འདྲེན་ཏེ། བྷ་ག་རྣམ་པ་དྲུག་ཏུ་བརྗོད། །ཅེས་བྱ་བ།

[Block 26 [VERSE]]
[^15] དཔལ་དང་གྲགས་དང་ཡེ་ཤེས་དང་། །
དབང་ཕྱུག་དང་ནི་གཟུགས་བཟང་དང་། །
བརྩོན་འགྲུས་ཕུན་སུམ་ཚོགས་ལྡན་དང་། །
དྲུག་པོ་དེ་ལ་ལྡན་ཞེས་བརྗོད། །

[Block 27]
ཅེས་པས་ཡེ་ཤེས་ཕུན་སུམ་ཚོགས་པར་བསྟན་ཏོ། །

[Block 28]
ཡང་ན་ཉོན་མོངས་ལ་སོགས་བདུན། །ཞེས་བྱ་སྟེ། བྷ་ག་ཝཱན་ནའི་སྒྲ་ལས་འཇོམས་པ་སྟེ། ཉོན་མོངས་པའི་བདུད་འདོད་ཆགས་ལ་སོགས་པ་དང་། ཕུང་པོའི་བདུད་དེ་རང་དབང་དུ་མ་ཐོབ་པ་དང་། འཆི་བདག་གི་བདུད་དེ་འཆི་བའི་དུས་ན་གཤིན་རྗེའི་ལག་ཏུ་འགྲོ་བ་དང་ལྷའི་བུའི་བདུད་ནི་དགའ་རབ་དབང་ཕྱུག་གིས་བར་ཆད་བྱེད་པ་སྟེ། དེ་རྣམས་བཅོམ་ལྡན་འདས༌[^16]བྷ་ག་ཝཱན་ནོ། །

[Block 29]
སརྦ་ཏ་ཐཱ་ག་ཏ་ནི་ཏ་ཐཱའི་སྒྲས་དེ་ཁོ་ན་ཉིད་དུ་གཤེགས་པའམ་སོན་ཞེས་བྱ་སྟེ་ཆོས་སྐུར་གནས་པའོ། །

[Block 30]
ག་ཏས་མི༌[^17]རྟོགས་པའམ་བྱོན་པ་སྟེ་སྐུ་གཉིས་སོ། །

[Block 31]
དེ་ཡང་།

[Block 32 [VERSE]]
[^18]དཔལ་ལྡན་དེ་བཞིན་ཉིད་གཤེགས་ཤིང་། །
དེ་བཞིན་སླར༌[^19]ཡང་གཤེགས་པ་ཉིད། །

[Block 33]
ཅེས་གསུངས་ཏེ། སརྦ་སྟེ་རྣམ་པར་སྣང་མཛད་ལ་སོགས་པ་དེ་རྣམས་ཀྱི་སྐུ་གསུང་ཐུགས་བསྡུས་པ་ནས་ཧྲྀ་ད་སྟེ་སྙིང་པོ་བསྡུས་པ་དེ་རྡོ་རྗེ་ལྟར་དབྱེར་མི་ཕྱེད་པས་རྡོ་རྗེའོ། །

[Block 34]
བཙུན་མོ་ལ་བཞུགས༌[^20]པ་སྟེ། སྤྱན་ལ་སོགས་པ་དེ་རྣམས་འདུས་པ་བྷ་ག་རྣམས༌[^21]ཁྲོ་བ་དང་ཆགས་པ་ཅན་འདུལ་བ་ལ་གནས་དེར་བཞུགས་པ་སྟེ། ཡེ་ཤེས་ཀྱི་སྣང་བ་ཉིད་གནས་སུ་སྣང་བ་དེ་ལ་རྡོ་རྗེ་འཆང་བཞུགས་པའོ། །

[Block 35]
བི་ཛ་ཧ་ར་སྟེ་གཞི༌[^22]མཐུན་པའི་འབྲུ་མང་པོ་པའོ། །

[Block 36]
ཧ་ར་ནི་འཕྲོག་པ་སྟེ་གཙོ་བོའི་ཡོན་ཏན༌[^23]གྱིས་འཁོར་གྱི་ཐེ་ཚོམ་སྟོན་པས་འཕྲོག་པའོ། །

[Block 37]
བཞུགས་ཞེས་པས་ཡང་རྒྱལ་པོ་ཕོ་བྲང་ན་བཞུགས་པས་འཁོར་འདྲེན་ཏེ། རྒྱལ་པོ་གཅིག་ཏུ་བཞུགས་པ་མ་ཡིན་པ་དང་། ཐོས་པའི་འབྲེལ་པས་འཁོར༌[^24]དང་བཅས་པ༌[^25]སྟོན་པས་འཁོར་བསྟན་པ་དང་གཞན་དག་ནི་སྤྱོད་ལམ་དང་ཆོས་འཆད་པ་དང་ཏིང་ངེ་འཛིན་དང་ནང་དུ་ཡང་དག་འཇོག་པས་བཞུགས་ཞེས་ཀྱང་འཆད་དོ། །

[Block 38 [HEADING]]
###### མིང་ཁྱད་པར་དུ་བཏགས་པའི་ཡོན་ཏན། ^1-1-1-1-3-0

[Block 39]
མིང་ཁྱད་པར་ཅན་དུ་བཏགས་པ་ནི་འདི་སྐད་ལ་ཨེ་སིན་ནམ་ཨི་དཾ་ཞེས་མི་ཟེར་བར་ཨེ་ཝཾ་ཞེས་བཏགས་པས་ལོག་རྟོག་སེལ་ཏེ་ཁ་ཅིག་ཕྱྭ་དང་མེས་པོ་དང་དབང་ཕྱུག་ལ་སོགས་པ་རྒྱུར་སྨྲ་སྟེ།

[Block 40]
བྱེ་བྲག་པའི་ལུང་ལས།
--- END BLOCKS ---
