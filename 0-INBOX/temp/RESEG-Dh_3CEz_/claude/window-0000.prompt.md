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

━━━ TOPIC SHIFT vs CONTINUATION (from the editors' corrections) ━━━

The editors' blocks are large (median ≈ 55 syllables; whole explanations of
100–250 syllables are normal). A sentence end is NOT a boundary. Inside one
explanation they cut only where the commentary turns to something new:
  START a new block at   "ཡང་ན་ …" (an alternative explanation)
                         "ཁ་ཅིག་ …", "གཞན་དག་ …" (another party's view)
                         "འོ་ན་ …" (the reply to an objection)
                         "དེ་སྐད་དུ་ …", "ཇི་སྐད་དུ་ …" (introducing a supporting quotation)
                         "དེ་ནས་ …" when it opens the next step of a procedure
                         "དཔེ་ …" / "དཔེར་ན་ …" when an example section begins
KEEP WITH the block before (merge into it):
                         "ད་ནི་ …" — a transitional "now …" line is not a new unit
                         (no heading or verse between them)
                         "ལེའུ་ … པའོ། །" — a chapter-closing line stays with the
                         explanation it closes
                         "ཞེས་ / ཅེས་ …" — the quotative closing the words just before it

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

[Block 2 [HEADING]]
## ཀླད་ཀྱི་དོན།

[Block 3]
༄༅༅། །རྒྱ་གར་སྐད་དུ། ཤྲཱི་ཧེ་བཛྲ་ཏནྟྲ་མ་ཧཱ་རཱ་ཛ་སྱ་པཉྩི་ཀཱ་ནེ་ཏྲ་བི་བྷཾ་ག་ནཱ་མ། བོད་སྐད་དུ། རྒྱུད་ཀྱི་རྒྱལ་པོ་ཆེན་པོ་དཔལ་དགྱེས་པའི་རྡོ་རྗེའི་དཀའ་འགྲེལ་སྤྱན་འབྱེད་ཅེས་བྱ་བ།

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
ཨེ་ཝཾ་མ་ཡཱ་ཤྲུ་ཏ་ཨེ་ཀ་སྨིན་ས་མ་ཡེ་བྷ་ག་བཱན། སརྦ་ཏ་ཐཱ་ག་ཏ་ཀཱ་ཡ་བཱཀྩི་ཏྟ་ཧྲྀ་ད་ཡ་བཛྲ་ཡོ་ཥཱི་ཏ་བྷ་གེ་ཥུ་བི་ཛ་ཧཱ་ར། །གླེང་གཞིའི་ངག་དང་པོའོ། །འདི་ཡང་སྒྲའི་ཚུལ་དུ་བཤད་པ་དང་། དོན་གྱི་ཚུལ་དུ་བཤད་པའོ། །

[Block 10 [HEADING]]
##### སྒྲའི་ཚུལ་དུ་བཤད་པ། ^1-1-1-1-0

[Block 11]
སྒྲའི་ཚུལ་ལ་ཡང་གསུམ་སྟེ། སྒྲའི་བྱེད་པའི་གནས་དང་སྦྱར་བ་དང་། ནུས་པའི་རྩལ་དང་མིང་ཁྱད་པར་དུ་བཏགས་པའི་ཡོན་ཏན་ཏོ། །

[Block 12 [HEADING]]
###### སྒྲའི་བྱེད་པའི་གནས་དང་སྦྱར་བ། ^1-1-1-1-1-0

[Block 13]
བྱེད་པའི་དབང་དུ་བྱས་པ་ནི་སྒྲའི་གནས་དང་སྦྱར་ཏེ། དེ་ཡང་སྒྲ་པའི་ལུགས་ཀྱི་ཏི་ངན་ཏིའི་མཐའ་ཅན་དང་སུ་པནྟིའི་མཐའ་ཅན་ལས་འདིར་སུ་བནྟ་བྱཱ་ཀཱ་ར་ཎའི་གནས་བརྒྱད་དོ།[^2] །གང་ཞེས་བྱ་བ་ལ་སོགས་པ་ལས། །འདིར་གང་གིས་ཐོས་ན་བདག་གིས་ཐོས་ཞེས་གསུམ་པ་སྦྱར། གང་གི་ཚེ་སྟེ་དུས་ནི་དང་པོའམ་ཏི་ངན་ཏའི༌[^3]གནས་མི་སྦྱར། གང་ལས་ཐོས་ཞེས་པས་བཅོམ་ལྡན་འདས་ཞེས་ལྔ་པ་ལ་སྦྱར་བ་དང་། གང་དུ་ཞེ་ན། བྷ་ག་ལ་ཞེས་བདུན་པའམ་གཉིས་པ་སྦྱར་བ་དང་། བཞུགས་ཞེས་པར་འཁོར་བསྟན་པས་ཐོས་པ་དང་འབྲེལ་བས། འདི་རྣམས་ཀྱི་ཕྱིར་ཞེས་བྱ་སྟེ་བཞི་པའི་སྒྲ་སྦྱར་རོ། །

[Block 14 [HEADING]]
###### ནུས་པའི་རྩལ། ^1-1-1-1-2-0

[Block 15]
ནུས་པའི་རྩལ་ནི་འདི་སྐད་ཀྱིས་འདི་སྐད་ནས༌[^4]འབྲུ་ལ་ཨའི་རྣམ་པའོ་ཞེས་པ་རྒྱུད་མགོ་ཞབས་ཀྱི་དོན་འདྲེན་པ༌[^5]དང་། འདི་སྐད་ཀྱིས་ཡང་སྒྲོ་མ་བཏགས་པ་དང་། སྐུར་པ་མ་བཏབ་པར་བཅོམ་ལྡན་འདས་ལས་ཐོས་ཤིང་གཟུངས་ནས་བསྡུས་ཞེས་པ་དང་། ཉན་པ་རྣམས་གུས་པ་དང་བཅས་པའོ། །བདག་གིས་ཞེས་པ་ནི་བདག་གིས་མངོན༌[^6]སུམ་དུ་ཐོས་ཀྱི་རྒྱུད་ཀྱི་བརྒྱུད་པས༌[^7]མ་ཡིན་པར་སྟོན་པ་དང་། ཐོས་པ་ཞེས་པ་ནི་ཐོས་པ་རྐྱང་བ༌[^8]སྟེ། རྟོགས་པ་ནི་མ་ཡིན་པའོ། །ཐོས་པའི་གནས་སྐབས་ན་ཐོས་ཀྱིས་རྟོགས་པ་ནི་མ་ཡིན་ཏེ་རང་གི༌[^9]བྱས་པ་སྟོན་པ་ལ་ཁྱད་པར་མེད་པ་དང་། གཞན་མི་གུས་པས༌[^10]འགྱུར་བས༌[^11]སོ། །

[Block 16]
སྡུད་པ་པོའི་གནས་སྐབས་ནི་དོན་དང་ཚིག་དང་བཅས་པར་བསྡུས་པས་ཁྱད་པར་དུ་འགྱུར་རོ། །དུས་གཅིག་གིས་ནི་ཡོན་ཏན་གསུམ་འདྲེན་པར་བྱེད་དེ། དུས་གཅིག་ན་འདི་ཐོས་པ་གཞན་དག་ཀྱང་ཐོས་ཞེས་པས་མང་བར་སྟོན་པ་དང་། གཞན་དུ་མ་ཐོས་པ་དག་སྲིད་དོ་ཞེ་ན། བྱང་ཆུབ་སེམས་དཔའ་བརྩོན་འགྲུས་རྒྱུན་མི་འཆད་པ་དང་།ཤེས་བྱའི་སྒྲིབ་པ་སྤོང་བར་གཙོར་བྱེད་པས་སོ། །དེས་ནི་སྡུད་པ་པོ་ཆེ་བར་བསྟན་ཏོ། །

[Block 17]
ཡང་དུས་གཅིག་གིས་བསྟན་པ་དཀོན་པར་སྟོན་ཏོ།[^12] །དེའི་ཚེ་ཁོ་ན་གསུངས་ཀྱི་གཞན་གང་དུ་ཡང་མ་བསྟན་པས་ན་དཀོན་པའོ། །དུས་གཅིག་སྟོན་པ་ཆེ་བར་སྟོན་ཏེ།[^13] སྐད་གཅིག༌[^14]མ་ལ་ཐོས་པས་འཁོར་རྣམས་རྣམ་པར་ཐར་པའི་སྐྱེ་མཆེད་སྒྲུབ་ནུས་པའམ་བྱ་བ་རྫོགས་པའི་སྐད་ཅིག་གཅིག་ཅེས་བྱའོ། །བྷ་ག་ཝཱན་གྱིས་ནི་ཡོན་ཏན་གཉིས་འདྲེན་ཏེ། བྷ་ག་རྣམ་པ་དྲུག་ཏུ་བརྗོད། །ཅེས་བྱ་བ།

[Block 18 [VERSE]]
[^15] དཔལ་དང་གྲགས་དང་ཡེ་ཤེས་དང་། །
དབང་ཕྱུག་དང་ནི་གཟུགས་བཟང་དང་། །
བརྩོན་འགྲུས་ཕུན་སུམ་ཚོགས་ལྡན་དང་། །
དྲུག་པོ་དེ་ལ་ལྡན་ཞེས་བརྗོད། །

[Block 19]
ཅེས་པས་ཡེ་ཤེས་ཕུན་སུམ་ཚོགས་པར་བསྟན་ཏོ། །

[Block 20]
ཡང་ན་ཉོན་མོངས་ལ་སོགས་བདུན། །ཞེས་བྱ་སྟེ། བྷ་ག་ཝཱན་ནའི་སྒྲ་ལས་འཇོམས་པ་སྟེ། ཉོན་མོངས་པའི་བདུད་འདོད་ཆགས་ལ་སོགས་པ་དང་། ཕུང་པོའི་བདུད་དེ་རང་དབང་དུ་མ་ཐོབ་པ་དང་། འཆི་བདག་གི་བདུད་དེ་འཆི་བའི་དུས་ན་གཤིན་རྗེའི་ལག་ཏུ་འགྲོ་བ་དང་ལྷའི་བུའི་བདུད་ནི་དགའ་རབ་དབང་ཕྱུག་གིས་བར་ཆད་བྱེད་པ་སྟེ། དེ་རྣམས་བཅོམ་ལྡན་འདས༌[^16]བྷ་ག་ཝཱན་ནོ། །སརྦ་ཏ་ཐཱ་ག་ཏ་ནི་ཏ་ཐཱའི་སྒྲས་དེ་ཁོ་ན་ཉིད་དུ་གཤེགས་པའམ་སོན་ཞེས་བྱ་སྟེ་ཆོས་སྐུར་གནས་པའོ། །ག་ཏས་མི༌[^17]རྟོགས་པའམ་བྱོན་པ་སྟེ་སྐུ་གཉིས་སོ། །

[Block 21]
དེ་ཡང་།

[Block 22 [VERSE]]
[^18]དཔལ་ལྡན་དེ་བཞིན་ཉིད་གཤེགས་ཤིང་། །
དེ་བཞིན་སླར༌[^19]ཡང་གཤེགས་པ་ཉིད། །

[Block 23]
ཅེས་གསུངས་ཏེ། སརྦ་སྟེ་རྣམ་པར་སྣང་མཛད་ལ་སོགས་པ་དེ་རྣམས་ཀྱི་སྐུ་གསུང་ཐུགས་བསྡུས་པ་ནས་ཧྲྀ་ད་སྟེ་སྙིང་པོ་བསྡུས་པ་དེ་རྡོ་རྗེ་ལྟར་དབྱེར་མི་ཕྱེད་པས་རྡོ་རྗེའོ། །བཙུན་མོ་ལ་བཞུགས༌[^20]པ་སྟེ། སྤྱན་ལ་སོགས་པ་དེ་རྣམས་འདུས་པ་བྷ་ག་རྣམས༌[^21]ཁྲོ་བ་དང་ཆགས་པ་ཅན་འདུལ་བ་ལ་གནས་དེར་བཞུགས་པ་སྟེ། ཡེ་ཤེས་ཀྱི་སྣང་བ་ཉིད་གནས་སུ་སྣང་བ་དེ་ལ་རྡོ་རྗེ་འཆང་བཞུགས་པའོ། །བི་ཛ་ཧ་ར་སྟེ་གཞི༌[^22]མཐུན་པའི་འབྲུ་མང་པོ་པའོ། །ཧ་ར་ནི་འཕྲོག་པ་སྟེ་གཙོ་བོའི་ཡོན་ཏན༌[^23]གྱིས་འཁོར་གྱི་ཐེ་ཚོམ་སྟོན་པས་འཕྲོག་པའོ། །བཞུགས་ཞེས་པས་ཡང་རྒྱལ་པོ་ཕོ་བྲང་ན་བཞུགས་པས་འཁོར་འདྲེན་ཏེ། རྒྱལ་པོ་གཅིག་ཏུ་བཞུགས་པ་མ་ཡིན་པ་དང་། ཐོས་པའི་འབྲེལ་པས་འཁོར༌[^24]དང་བཅས་པ༌[^25]སྟོན་པས་འཁོར་བསྟན་པ་དང་གཞན་དག་ནི་སྤྱོད་ལམ་དང་ཆོས་འཆད་པ་དང་ཏིང་ངེ་འཛིན་དང་ནང་དུ་ཡང་དག་འཇོག་པས་བཞུགས་ཞེས་ཀྱང་འཆད་དོ། །

[Block 24 [HEADING]]
###### མིང་ཁྱད་པར་དུ་བཏགས་པའི་ཡོན་ཏན། ^1-1-1-1-3-0

[Block 25]
མིང་ཁྱད་པར་ཅན་དུ་བཏགས་པ་ནི་འདི་སྐད་ལ་ཨེ་སིན་ནམ་ཨི་དཾ་ཞེས་མི་ཟེར་བར་ཨེ་ཝཾ་ཞེས་བཏགས་པས་ལོག་རྟོག་སེལ་ཏེ་ཁ་ཅིག་ཕྱྭ་དང་མེས་པོ་དང་དབང་ཕྱུག་ལ་སོགས་པ་རྒྱུར་སྨྲ་སྟེ།

[Block 26]
བྱེ་བྲག་པའི་ལུང་ལས།

[Block 27 [VERSE]]
བ་ནི་བ་སྨྲ་བ༌[^26]རྣམས་ཀྱི་རྒྱུ། །
འགྲོ་བའི་རྒྱུ་ནི་དབང་ཕྱུག་སྟེ། །
དབང་ཕྱུག་གིས་ནི་མཐོ་རིས་སམ། །
ངན་འགྲོ་དག་ཏུའང་ལྟུང་བར་བྱེད། །

[Block 28]
ཅེས་ཟེར་བ་དེ་ལྟ་བུ་དགག་པའི་ཆེད་དུ་སྟེ། །ཨེ་ཝཾ་ནི་ཆོས་ཐམས་ཅད་ཀྱི་ཕ་དང་མ༌[^27]ལྟ་བུའི་འབྱུང་ཁུངས་སུ་ཤེས་པར་བྱེད་ལ། ཨེ་ཝཾ་སྟེ་བདེ་སྟོང་དབྱེར་མེད་ཐབས་ཤེས་རབ་དང་དབྱེར་མེད་དུ་སྟོན་པས་ན་དེ་སྤོང་ངོ་། །དེ་ཡང༌[^28]ཨེ་ནི་མར་འགྱུར་ལ།

[Block 29 [VERSE]]
བི་ན་ཕ་ཞེས་བྱ་བར་གྲགས། །
ཐིག་ལེ་དེ་ནི་སྦྱོར་བ་སྟེ། །
སྦྱོར་ཏེ་དེ་ནི་རྨད་བྱུང་བའོ། །

[Block 30]
ཞེས་པ་དང་།

[Block 31 [VERSE]]
ཨེ་ནི་ཤེས་རབ་ཉིད་འགྱུར་ལ། །
ཝཾ་ནི་རབ་དགའི་བདག་པོའོ། །
འགྲོ་བ་གང་ཞིག་ཡི་གེ་གཉིས། །
མི་ཤེས་རྟག་ཏུ་འདོན་པ་དང་། །

[Block 32 [VERSE]]
དེས་ན་སངས་རྒྱས་ཆོས་རྣམས་ལས། །
ཕྱི་རོལ་སྦྱོར་སྤངས་ཐུབ་པ་བཞིན། །
ཨེ་ཝཾ་ཡིག་གཉིས་སྒྱུ་མ་ལ། །
ཐམས་ཅད་མཁྱེན་པ་འདིར་བཞུགས་པས། །

[Block 33 [VERSE]]
དམ་ཆོས༌[^29]བསྟན་པའི་ཐོག་མར་ནི། །
ཨེ་ཝཾ་དེ་ཕྱིར་རབ་ཏུ་བཤད། །

[Block 34]
ཅེས་གསུངས་སོ། །

[Block 35]
བདག་གིས་ལ་ཨཱཏྨའི་ཟེར་བ་ནི་མུ་སྟེགས་བདག་ཏུ་འདོད་པ་ཡང་གང་ཟག་བདག་ཏུ་འདོད་པ་སྟེ། གྲངས་ཅན་དག་ནི་ཡོན་ཏན་གསུམ་ཆེ་མཉམ་པ་ལས་གཙོ་བོ་ལས་བདག་སྟེ། དེ་ལས་འགྱུར་བ། དེ་ལས་ཡོན་ཏན་དུ་མ་སྐྱེ་སྟེ།

[Block 36 [VERSE]]
འདི་ཙམ་ཉི་ཤུ་ལྔ་ཤེས་ན། །
རལ་པའམ་སྤྱི་བོ་གཙུག་ཕུད་ཀྱི། །
བསྟི་གནས་གང་དུ་འགྲོ་བ་དེར། །
གྲོལ་འགྱུར་འདི་ལ་ཐེ་ཚོམ་མེད། །

[Block 37]
ཅེས་ཟེར་བ་དེ་བཟློག་པའི་ཕྱིར། མ༌[^30]ཡཱ་ནི་སྒྱུ་མའི་བདག་ཉིད་དུ་ཤེས་པར་བྱ་སྟེ། བདག་ནི་རྟག་པ་དང་གཅིག་པུ་དང་རང་དབང་དུ་འདོད་ལ། སྒྱུ་མ་ནི་དེ་དང་མཚན་ཉིད་མི་མཐུན་པས་ནི་དེ༌[^31]སྤོང་ངོ་། །ཐོས་པ་ཤྲུ་བ་ལའམ་ཤྲུ་ཏ་ཟེར་བ་ནི་མུ་སྟེགས་ཀྱི་རིག་བྱེད་པ་སྒྲ་ཡོན་ཏན་དུ་འདོད་པ་སྒྲས་ཆོག་པར་འཛིན་ཏེ། །

[Block 38]
དེའི་ལུང་ལས།

[Block 39 [VERSE]]
ཉེས་པ་རྣམས་དང་འབྲེལ་བའི་ཕྱིར། །
སྐྱེས་བུ་མ་བྱས་བདེན་དོན་ཅན། །

[Block 40]
ཞེས་སྒྲ་རྟག་པར་འདོད་པ་དེ་སྤོང་སྟེ། ཤྲུ་ཏ་རྒྱུ་བས་མ་ཤྲུ་ཏ་རིག་པ་ཤེས་པས་སྒྲ་རྟག་པ་དེ་ཐོས་བྱ་དང་ཐོས་བྱེད་ཀྱི་འབྲེལ་པ་མི་འཐད་པས་ན་དེ་བཟློག་གོ། །དུས་གཅིག་ན་ཨེ་ཀ་ཀཱ་ལ་མི་ཟེར་པར༌[^32]ས་མ་ཡ་ཟེར་བ་ནི་དུས་ཡོན་ཏན་དུ་འདོད་པ་ཡོད་དེ།
--- END BLOCKS ---
