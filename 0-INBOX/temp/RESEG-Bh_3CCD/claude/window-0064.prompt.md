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
[Block 2241]
བྱུང་ནས་དགོན་པ་དབེན་པ་ལ་དྲང་སྲོང་དམ་པ་ལས་ཆགས་བྲལ་གྱི་ལམ་བླངས་ཏེ། རལ་གྲིས་དབུ་སྐྲ་བྲེགས་ཏེ་ཆོས་གོས་འཛིན་པར་གྱུར་ཏོ་ཞེས་བཙུན་མོའི་འཁོར་གྱི་ནང་ནས་ནི་ངེས་པར་བྱུང་བ་ནི་གླེང་གཞི་ཡིན་ཏེ། འདོད་ཆགས་དང་བྲལ་བའི་སྔོན་བྱུང་བའི་བཅས་གཞིའོ། །

[Block 2242]
དགོན་པར་གནས་པས་ཀྱང་གལ་ཏེ་འདོད་ཆགས་ལ་སོགས་པ་སྐྱེ་བར་གྱུར་ན། དེའི་ཚེ་ཁྱིམ་ནས་འབྱུང་བ་དོན་མེད་པར་འགྱུར་བས་དེའི་ཕྱིར་གསུམ་པ་ཡིན་ཏེ། འདུལ༌[^1495]ལས་ཞེས་བྱ་བ་ལ་སོགས་པ་འདུལ་བ་ལས་བསྟན་པ་ནི་སོ་སོར་ཐར་པའི་སྡོམ་པ་ལ་སོགས་པ་ནས་གསུངས་པའི་བསླབ་པའི་ཚིག་གི་ཚོགས་གང་ཡིན་པ་དེ་བཅོམ་ལྡན་འདས་ཀྱིས་བླངས་སོ། །

[Block 2243]
དེས་ནི་དོན་མཐུན་པ་བསྡུ་བའི་དངོས་པོ་བསྟན་ཏོ། །

[Block 2244]
གཞན་དུ་ན་སྡོམ་པ་མ་བླངས་པས་ཕ་རོལ་པོ་རྣམས་ལ་དེ་བསྟན་པ་དོན་མེད་པར་འགྱུར་རོ། །

[Block 2245]
དེ་བས་ན་དེ་རིགས་པ་ཡིན་ཏེ། །སེམས་ཅན་གྱི༌[^1496]དོན་གྱི་ཡན་ལག་གཙོ་བོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2246]
དེ་ནི་ངེས་པའི་ཚིག་ཅེས་བྱ་བ་ལ༌[^1497]སོགས་པར་གསུངས་པའི་སྡོམ་པའི་ཚིག་ངེས་པར་བསྲུང་བའི་ཕྱིར་རོ། །

[Block 2247]
འབྲས་བུ་ནི་སངས་རྒྱས་ཉིད་དོ། །

[Block 2248]
དེ་འདོད་པས་ནི་དེ་ཐོབ་པར་བྱ་བའི་འདུན༌[^1498]པས་སོ། །

[Block 2249]
ཆོས་སྤྱོད་པ་ནི་དཀའ་ཐུབ་ཀྱི་སྤྱོད་པ་ལ་སོགས་པ་བཅོམ་ལྡན་འདས་ཀྱིས་གང་མཛད་པ་དེ་ནི་རྒྱུ་ཞེས་བརྗོད་བྱ་སྟེ། འབྲས་བུ་ཐོབ་པ་ལ་ཐབས་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2250]
དེ་ཉིད་ནི་རིགས་པ་ཡིན་ཏེ། གང་གི་ཕྱིར་ལུས་དང་ངག་དང་ཡིད་སྡོམ༌[^1499]པར་བྱེད་པ་བརྟུལ་ཞུགས་ཀྱི་ཁྱད་པར་འདི་བྱང་ཆུབ་འདོད་པར་བྱ་བ༌[^1500]ཡིན་ནོ། །

[Block 2251]
འདི་ནི་ཞེས་བྱ་བ་ལ་སོགས་པས་ཉེ་བར་སྡུད་པ༌[^1501]བསྟན་ཏོ། །

[Block 2252]
འདོད་ཆགས་ཆོས་ཀྱི་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། འདོད་ཆགས་རྣམ་པར་དག་པར་བྱེད་པའི་སྔགས་ཀྱི་བསྟན་པ་ལའོ། །

[Block 2253]
དོན་གསལ་རྟོགས་ཕྱིར་བཤད་པར་བྱ། །ཞེས་པ་ནི་མི་སླུ་བའི༌[^1502]དོན་ཡོངས་སུ་ཤེས་པའི་རྒྱུ་བཤད་པར་བྱའོ། །

[Block 2254]
རིགས་ལྔའི་སངས་རྒྱས་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། ཉོན་མོངས་པ་ལྔ་དང་ཁམས་དང་དབང་པོ་དང་ཡུལ་དང་རྣམ་པར་ཤེས་པ་དང་ཕུང་པོ་ལྔ་རྣམ་པར་དག་པའི་སླད་དུ་བཅོམ་ལྡན་འདས་རྡོ་རྗེ་འཆང་ཆེན་པོས་གཟུགས་གཅིག་པུ་ཡང་ཡེ་ཤེས་ལྔའི་ངོ་བོ་ཉིད་དེ་བཞིན་གཤེགས་པ་ལྔའི་རིགས་སུ་སྤྲུལ་པར་མཛད་དེ། དེ་ཉིད་ཀྱིས་སྔོན་དུ་བཤད་པའི་ཉོན་མོངས་པ་ལ་སོགས་པ་འགོག་པའི་ཕྱིར་རོ། །

[Block 2255]
དེ་ཉིད་རིགས་པ་ཡིན་ཏེ། གང་གི་ཕྱིར་ལྷའི་སྐུ་ནི་ཐ་མལ་པའི་ལུས་དང་འགལ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2256]
ཀུན་རྫོབ་ཀྱི་ཕྱོགས་འདི་ཡིན་གྱི་དོན་དམ་པ་མ་ཡིན་པར་བསྟན་པར་བྱ་བའི་ཕྱིར། རྒྱུད་ཅེས་བྱ་བ་ཡིན་པར་བརྗོད་ཅེས་སྨོས་སོ། །

[Block 2257]
སླར་ཡང་ཞེས་བྱ༌[^1503]ལ་སོགས་པ་ལ། རིགས་ལྔ་པོ་རྡོ་རྗེ་འཆང་ཆེན་པོའི་རིགས་སུ་གཅིག་ཏུ་གྱུར་ཏེ། དེ་ཡང་བསྐྱེད་པའི་རིམ་པ་ལས་ཀྱི་རྒྱལ་བ་མཆོག་གི་ཏིང་ངེ་འཛིན་གྱི་བར་དུ་ཕྱིའི་དཀྱིལ་འཁོར་ལུས་ཀྱི་དཀྱིལ་འཁོར་ལ་བསྡུས་ཏེ་བདེ་བ་ཆེན་པོའི་རང་བཞིན་དཔའ་བོ་གཅིག་པུ་གནས་པ་བཞིན་ནོ། །

[Block 2258]
རྫོགས་པའི་རིམ་པ་ལ་ཡང་གཉིས་པ་དང་། བཞི་པའི་རིམ་པ་ལས་གསུངས་པའི་འོད་གསལ་བ་ལ་འཇུག་པའམ། ཟུང་དུ་འཇུག་པའི་ཏིང་ངེ་འཛིན་ནི་རིགས་གཅིག་ཏུ་གྱུར་པའོ། །

[Block 2259]
དེ་ཉིད་གླེང་གཞི་ཡིན་པར་བསྟན་པ་ནི་རྡོ་རྗེ་འཆང་ཆེན་པོ་ཉིད་བསྐལ་པའི་བར་དུ་གནས་པ་དང་། རང་བཞིན་གྱིས་རྟག་པ༌[^1504]ཡིན་གྱི་གཞན་ནི་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2260]
རིགས་པ་འདི་ཡང་ཡིན་ཏེ། དབྱེ་བ་ཐམས་ཅད་སྟོང་པར་ནུབ་པའི་ཕྱིར་རོ། །

[Block 2261]
རྡོ་རྗེ་ལ་སོགས་པ་ཞེས་བྱ་བ་ལ། མོས་པ་སྣ་ཚོགས་པའི་སེམས་ཅན་གྱི་ཁམས་རྗེས་སུ་གཟུང་བའི་ཕྱིར། དེ་བཞིན་གཤེགས་པ་རིགས་ལྔ་པོ་རྡོ་རྗེ་ལ་སོགས་པའི་ཕྱག་མཚན་གཟུང་བར་བྱ་བར་གསུངས་སོ། །

[Block 2262]
དེ་རྣམས་ཀྱང་རྣམ་པར་དག་པ་དང་བཅས་པར་བསྟན་ཏེ།

[Block 2263 [VERSE]]
སྤོང་བ་ལྔ་དང་རིག་པ་ལྔ། །
རྡོ་རྗེ་ཞེས་ནི་མངོན་པར་བརྗོད། །
ཇི་ལྟར་པདྨ་དམར་པོ༌[^1505]འདི། །
གནས་ཀྱི་སྐྱོན་གྱིས་མ་གོས་པ། །

[Block 2264 [VERSE]]
དངོས་པོ་སྣ་ཚོགས་སྐྱོན་རྣམས་ཀྱིས། །
མ་གོས་དེ་ལྟར་ཁམས་གསུམ་ཡིན། །

[Block 2265]
ཞེས་འབྱུང་བ་དང་། དེ་བཞིན་དུ་ཡང་རིག་པའི་དབང་བསྐུར་བའི་དུས་སུ་སློབ་མའི་ལག་པ་དག་ཏུ་རྡོ་རྗེ་དང་དྲིལ་བུ་བྱིན་ནས།

[Block 2266 [VERSE]]
བྱང་ཆུབ་སེམས་གང་དེ་རྡོ་རྗེ། །
ཤེས་རབ་དྲིལ་བུ་ཞེས་བརྗོད་དོ། །

[Block 2267]
ཞེས་འབྱུང་ངོ་། །འདིར་ཡང་རིགས་པ༌[^1506]སྟེ། དོན་དང་རྗེས་སུ་ལྡན་པའི༌[^1507]མིང་དང་ལྡན་པ་འཛིན་པའི་ཕྱིར་རོ། །

[Block 2268]
གཞན་དུ་ན་ལྕགས་ལ་སོགས་པས་འཛིན་པ་མེད་དོ། །

[Block 2269]
དེ་ཉིད་ཀྱི་ཕྱིར། ངེས་པའི་ཚིག་ནི་ཡིན་པར་བཤད། །ཅེས་སྨོས་ཏེ། སྒེག་པ་ལ་སོགས་པ༌[^1508]ཞེས་བྱ་བ་ལ་སོགས་པ་ནི། བདེ་བས་བྱང་ཆུབ་ཐོབ་པར་འགྱུར། །ཞེས་ཚིག་ལས་སྒེག་པ་ལ་སོགས་པའི་གར་གྱི་ཉམས་དགུ་དང་ལྡན་པའི་སྤྱོད་པས་རྡོ་རྗེ་འཆང་ཆེན་པོའི་གོ་འཕང་ཐོབ་པར་འགྱུར་ཞེས་འབྲས་བུ་ཐོབ་པའི་ཕྱིར་སྤྱོད་པ་ལྔ་ནི་སྔ་མ་བཞིན་ཁོ་ནའོ། །

[Block 2270]
དེ་ལ།

[Block 2271 [VERSE]]
སྒེག་པ་དཔའ་བ་འཇིགས་རུང་དང་། །
དགོད་དང་གཤེ་དང་འཇིགས་བྱེད་དང་། །
སྙིང་རྗེ་རྔམ་དང་ཞི་བ་ནི། །
གར་གྱི་ཉམས་ནི་དགུ་རུ་བཤད། །

[Block 2272]
དེ་ལ་སྒེག་པའི་སྤྱོད་པ་ནི། དམ་ཚིག་གི་ཕྱག་རྒྱ་ལ་སོགས་པ་བསྟེན་པའོ། །

[Block 2273]
དཔའ་བའི༌[^1509]སྤྱོད་པ་ནི་ཐམས་ཅད་དུ་མི་འཇིགས་པའོ། །

[Block 2274]
འཇིགས་སུ་རུང་བའི་སྤྱོད་པ་ནི་གོ་ཀུ་ད་ཧ་ན་བཟའ་བའི་མཚན་ཉིད་དོ། །

[Block 2275]
སྨད་པ་དང་འཇིགས་པར་བྱེད་པ་ནི་འཇིགས་སུ་རུང་བ་ཞེས་བཤད་དོ། །

[Block 2276]
དགོད་པའི་སྤྱོད་པ་ནི་རོ་ལངས་བསླང་བ་ལ་སོགས་པའི་མཚན་ཉིད་དམ་སྒེག་པའི་ཉམས་ཀྱི་བྱེ་བྲག་གོ། །

[Block 2277]
གཤེ་བའི་སྤྱོད་པ་ནི་མངོན་སྤྱོད་ལ་སོགས་པའི་ལས་དྲག་པོའི་རབ་འབྱམས་བྱེད་པའི་མཚན་ཉིད་དོ། །

[Block 2278]
འཇིགས་པར་བྱེད་པའི་སྤྱོད་པ་ནི་ཞེ་སྡང་རྡོ་རྗེའི་ཏིང་ངེ་འཛིན་གྱིས་ཁྲོ་བོའི་འཁོར་ལོ་སྤྲོས་ཏེ་བགེགས་རྣམ་པར་གནོན་པ་དང་ཕུར་བུས་གདབ་པ་དང་བརྡུང་བའི༌[^1510]མཚན་ཉིད་དོ། །

[Block 2279]
སྙིང་རྗེའི་སྤྱོད་པ་ནི་སེམས་ཅན་རྗེས་སུ་བཟུང་བའི༌[^1511]མཚན་ཉིད་དོ། །

[Block 2280]
རྔམ་པའི་སྤྱོད་པ་ནི་བསྟན་པ་ལ་སོགས་པའི་རྫུ་འཕྲུལ་ལམ། ཆོས་འདི་རུ་བསྟན་པའི་དུས་སུ་གཞན་དུ་ཡང་བསྟན་པ་ལྟར་སྣང་བའོ། །
--- END BLOCKS ---
