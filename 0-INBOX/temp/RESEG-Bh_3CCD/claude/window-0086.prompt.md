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
[Block 3011]
ཅིའི་རྣམ་པར་དག་པར་བྱ་བའི་ཕྱིར་ཡེ་ཤེས་སྐྱེའོ། །

[Block 3012]
སྐྱེ་མཆེད་ཀྱི་བསྐྱེད་པ་བསྟན་པར་བྱ་བའི་ཕྱིར། མ། [^1956]ཡིད་ཀྱི་སྐྱེ་མཆེད་ཅེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། ཡིད་ལ་སོགས་པ་ནང་གི་སྐྱེ་མཆེད་དྲུག་སྟེ། གང་གིས༌[^1957]ལས་ཀྱི་ལུས་པོ་འདི་དང་ཡུལ་རྣམས་དང་ལེན་པར་བྱེད་དེ། འདིར་ནི་ཚིགས་སུ་བཅད་པ་གཅིག་འདོར༌[^1958]ཏེ་བཤད་པར་བྱ་བ་ཡིན་ནོ། །

[Block 3013]
ལུས་སྐྱེས་པས་ལས་ཀྱི་དབང་གིས་སྐྱེ་བ་ལེན་པ་བསྟན་པར་བྱ་བའི་ཕྱིར། བྷ། འབྱུང་བ་འདི༌[^1959]ལས་རང་བཞིན་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། འདོད་ཆགས་ལ་སོགས་པའི་རང་བཞིན་བརྒྱ་དྲུག་ཅུའི་དབང་གིས་དགེ་བ་དང་མི་དགེ་བའི་ལས་བྱས་ནས་དེ་ནས་ཤི་འཕོས་ཏེ་ངན་སོང་དང་བདེ་འགྲོ་ལ་སོགས་པའི་མཚན་ཉིད་ཅན་སྐྱེ་བ་ཐོབ་པ་གང་ཡིན་པ་དེའི་རྒྱུ་ནི་རྣམ་པར་ཤེས་པ་གསུམ་པོ་ཁོ་ན་ལས་གཞན་མ་ཡིན་ནོ། །

[Block 3014]
བསྐྱེད་པའི་རིམ་པ་ཕུང་པོ་རྣམ་པར་དག་པ་བསྟན་པར་བྱ་བའི་ཕྱིར། ག །འགྲོ་བར་བྱེད་ཅེས༌[^1960]བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། འགྲོ་བ་ནི་མི་ལ་སོགས་པའི་འགྲོ་བའོ། །

[Block 3015]
དེས་ན་བདེ་འགྲོ་དང་ངན་འགྲོ་དག་ཏུ་ཉེ་བར་ལེན་པའི་ཕུང་པོ་ལྔ་གཟུགས་ལ་སོགས་པ་གང་ཡིན་པ་དེ་དག་འབྱུང་བ༌[^1961]ནི་སྐྱེ་བར་འགྱུར་ཏེ་ཉོན་མོངས་པ་དང་ལས་དང་རྣམ་པར་སྨིན་པའི་ངོ་བོ་ཉིད་ཀྱི༌[^1962]རྟེན་ཅིང་འབྲེལ་པ་ཡན་ལག་བཅུ་གཉིས་ཀྱི་མཚན་ཉིད་ཅན་སྲིད་པའི་འཁོར་ལོས་ཡོངས་སུ་འཁོར་རོ། །

[Block 3016]
དེ་དག་དག་པར་བྱ་བའི་ཕྱིར་བསྐྱེད་པའི་རིམ་པ་མངོན་པར་བྱང་ཆུབ་པ་རྣམ་པ་ལྔའི་བསྒོམ་པས་སངས་རྒྱས་ལྔའི་ངོ་བོ་ཉིད་ཐོབ་པ་གང་ཡིན་པ་དེའི་ཡང་རྒྱུ་ནི་རྣམ་པར་ཤེས་པ་གསུམ་ཡིན་ནོ། །

[Block 3017]
ས་ལ་སོགས་པ་རྣམ་པར་དག་པའི་རྒྱུ་བསྟན་པར་བྱ་བའི༌[^1963]ཕྱིར། ཝཱན། རླུང་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། ས་ལ་སོགས་པ་ཁམས་བཞི་པོ་རྣམ་པར་དག་པའི་ངོ་བོ་སྤྱན་མ་ལ་སོགས་ཀྱི་བཙུན་མོ༌[^1964]ཡང་རྣམ་པར་ཤེས་པ་གསུམ་པོ་ལས་འབྱུང་བ༌[^1965]སྟེ། དེ་ལ་དམིགས་པ་ལས་དེ་དག་རྣམ་པར་དག་པའི་ཕྱིར་རོ། །

[Block 3018]
དེ་བས་ན་སངས་རྒྱས་བྱང་ཆུབ་ནི་ཞེས་སྨོས་ཏེ་ས་བརྒྱད་པ་ལ་གནས་པའི་བྱང་ཆུབ་སེམས་དཔའ་ལས་སངས་རྒྱས་ཉིད་སྟེར་བར་བྱེད་པ་དེ་ཉིད་ཅེས་ཚིག་ལྷག་མའོ། །

[Block 3019]
མིག་ལ་སོགས་པ་རྣམ་པར་དག་པའི་རྒྱུ་ཉིད་བསྟན་པར་བྱ་བའི་ཕྱིར། ས། ཐམས་ཅད་ཅེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། བསྐྱེད་པའི་རིམ་པས་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱིས་གང་སླར༌[^1966]བཤད་པ་དེ་ཉིད་རྣམ་པར་ཤེས་པ་གསུམ་གྱི་རྒྱུན་ཅན་ཡིན་ནོ། །

[Block 3020]
ཕྱག་རྒྱ་བཞིས་ནི་རྒྱས་བཏབ་ཅིང་། །ཞེས་པ་ནི་དེ་ལས་དགུག་པ་དང་། གཞུག་པ་དང་། བཅིང་བ་དང་། དབང་དུ་བསྡུ་བའི་མཚན་ཉིད་ཅན་ཕྱག་རྒྱ་བཞི་པོའོ། །

[Block 3021]
གང་གིས་ཡེ་ཤེས་སེམས་དཔའ་དགུག་པ་ལ་སོགས་པ་བྱའོ།[^1967] །

[Block 3022]
ཡང་ན་སྤྱན་ལ་སོགས་པ་བཞི་པོ་ནི་ཕྱག་རྒྱ་བཞི་སྟེ། དེ་རྣམས་ཀྱིས་རྒྱས་བཏབ་པ་ནི་ཡོངས་སུ་བསྐོར་ཏེ་དེས་ནི་གསང་བ་ལྔའི་དཀྱིལ་འཁོར་ཆེན་པོ་བསྟན་ཏོ། །

[Block 3023]
ཡང་ན་ལས་དང་། ཆོས་དང་། དམ་ཚིག་དང་། ཕྱག་རྒྱ་ཆེན་པོའི་དམ་ཚིག་ཅན་བཞིའོ། །

[Block 3024]
ཕྱག་རྒྱ་ཆེན་པོའི་གཟུགས་དེ་དག་གིས་འགྲུབ་པར་བྱའོ།[^1968] །

[Block 3025]
ཇི་སྐད་དུ།

[Block 3026]
ཐམས་ཅད་མཁྱེན་པ་འཇིགས་བྱེད་ཅེས་བྱ་བ་རྣལ་འབྱོར་ཆེན་པོའི་རྒྱུད་ལས།

[Block 3027 [VERSE]]
དེ་ནས་དེ་དག་རྣམས་ཀྱིས་ནི། །
རྣལ་འབྱོར་གསང་བ་མཆོག་བཤད་བྱ། །
དང་པོ་ཡེ་ཤེས་སེམས་བསྒོམས་ནས། །
ཕྱག་རྒྱ་ཆེན་པོ་འཆང་བར་བྱ། །

[Block 3028 [VERSE]]
ཟླ་བའི་དཀྱིལ་འཁོར་དང་མཚུངས་པའི། །
སྙིང་གར་གནས་པའི་བྱང་ཆུབ་སེམས། །
ཕྱི་མོའི་ཡི་གེ་དང་མཚུངས་པ། །
ཅུང་ཟད་སྣང་བ་ཙམ་དུ་བསྒོམ། །

[Block 3029 [VERSE]]
རྣལ་འབྱོར་ཆེན་པོའི་མཐོང་བ་བཞིན། །
དམ་ཚིག་ཅེས་བྱ་བཅད་པར་བྱ། །
རྟག༌[^1969]ཏུ་ལས་ཀྱི་རྒྱ་བཅིངས་ཏེ། །
སྣ་ཚོགས་རྡོ་རྗེ་སྙིང་གར་གནས། །

[Block 3030 [VERSE]]
ངེས་པ་ཉིད་དུ་ཤེས་བྱས་ན། །
དེ་ཚེ་ཐེ་ཚོམ་མེད་པར་འགྲུབ། །
དང་པོ་རྡོ་རྗེ་ལྕེར་བསྒོམས་ཏེ། །
ཆོས་ཀྱི་ཕྱག་རྒྱ་ཡང་དག་འཆང་། །

[Block 3031 [VERSE]]
ཅི་འདོད་པ་ཡི་ལས་རྣམས་ནི། །
མྱུར་དུ་ཐེ་ཚོམ་མེད་པར་འགྲུབ། །
དེ་ལྟར་ཕྱག་རྒྱ་རྣམ་པ་བཞི། །
བློ་ལྡན་གང་གིས་མི་ཤེས་ན། །

[Block 3032 [VERSE]]
སྡོམ་པའི་རྣལ་འབྱོར་མཆོག་ཉིད་ནི། །
དེ་ཡིས་ངེས་པར་ཐོབ་མི་འགྱུར། །
དཀོན་ཞིང་བདེ་བའི་ཐབས་འདི་ནི།
སངས་རྒྱས་རོལ་སྟོན་གསང་བ་ཡིན། །

[Block 3033 [VERSE]]
དེ་ནི་བྱང་ཆུབ་སེམས་ཡིན་ཏེ། །
རྟག་ཏུ་ཤེས་རབ་རྒྱ་མཚོར་གནས། །

[Block 3034]
ཞེས་འབྱུང་ངོ་། །མིག་ལ་སོགས་པའི་བདག་ཉིད་དེར། །ཞེས་པ་ནི་ལུས་དེ་ཉིད་དུ་མིག་ལ་སོགས་པ་གང་ཡོད་པ་དེ་དག་ཏུ་ཤིན་ཏུ་རྣལ་འབྱོར་གྱི་རིམ་པས་སའི་སྙིང་པོ་ལ་སོགས་པ་བྱང་ཆུབ་སེམས་དཔའ་བརྒྱད་ཀྱི་ས་བོན་བཀོད་པས་རྣམ་པར་དག་པར་བྱེད་པ་གང་ཡིན་པ་དེ་ནི་ཤེས་པ་གསུམ་གྱི་རྒྱུ་ཅན་ཁོ་ནའོ། །

[Block 3035]
རྟོག་པའི་རྣལ་འབྱོར་པའི་ཡན་ལག་ལ་འགོད་པ༌[^1970]ནི་ཤེས་པ་གསུམ་གྱི་ཡང་རྒྱུ་ཅན་ཡིན་པར་བསྟན་པར་བྱ་བའི་ཕྱིར། རྦ། རོལ་པས་ཤེས་པ་ལ་སོགས་པ་སྨོས་ཏེ། ཕྱོགས་བཅུ་ན་གནས་པའི༌[^1971]ཁྲོ་བོའི་རྒྱལ་པོའི་ཕྱིའི་དཀྱིལ་འཁོར་དུ་བརྒྱ་བྱིན་ལ་སོགས་པ་ཕྱོགས་སྐྱོང་རྣམས་ཟིལ་གྱིས་མནན་ནས་བཞུགས་པ། སྟོབས་དང་མཐུ་ཆེ་བ་གང་ཡིན་པ་དེ་རྣམས་ཞལ་ལ་སོགས་པའི་ཡན་ལག་དང་ཉིང་ལག་རྣམས་སུ་རྣམ་པར་བཀོད་པ། སྐུའི་དཀྱིལ་འཁོར་གྱི་ཚུལ་དུ་བཞུགས་པ་གང་ཡིན་པ་དེ་ཡང་ཤེས་པ་གསུམ་གྱི་རྒྱུ་ཅན་ཡིན་ནོ། །

[Block 3036]
དེའི་རྗེས་སུ་དཀྱིལ་འཁོར་ཉེ་བར་སྡུད་པ་ལ་རང་བཞིན་མེད་པ༌[^1972]ཉིད་ཀྱི་སྒོམ་པའི་ཡང་རྒྱུ་ཤེས་པ་གསུམ་ཡིན་པ་ཞེས་བསྟན་པར་བྱ་བའི་ཕྱིར། ཏ། དེ་དང་དེ་ཡི་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། ཐུགས་ཀྱི་རྡོ་རྗེ་འཛིན་པ་ལ་སོགས་པའི་རིགས་ལས་འབྱུང་བ་སྟེ། དེ་བཞིན་གཤེགས་པ་དང་ལྷ་མོ་དང་བྱང་ཆུབ་སེམས་དཔའ་དང་ཁྲོ་བོ་རྣམས་སོ། །

[Block 3037]
དེ་དག་ཁོ་ན་ཡོད་མིན་ཞེས་པ་ནི་ལས་ཀྱི་རྒྱལ་བ་མཆོག་གི་ཏིང་ངེ་འཛིན་གྱི་མཐར་ཉེ་བར་བསྡུས་པས༌[^1973]དམིགས་པར་མི་འགྱུར་རོ། །

[Block 3038]
འོན་ཀྱང་འགྲོ་བའི་དོན་དུ་བསྟན་པ་ཡིན་ཞེས་པ་ནི་འདོད་ཆགས་ལ་སོགས་པའི་ཉོན་མོངས་པས་དཀྲུགས་པའི་སེམས་ཅན་གྱི་ཁམས་རྗེས་སུ་གཟུང་བར་བྱ་བའི་ཕྱིར། དེ་དང་དེའི་མོས་པས་དབྱེ་བས་བཅོམ་ལྡན་འདས་ཀྱི་སྤྲུལ་པ་ཡིན་གྱི། དོན་དམ་པར་དེ་དག་ཐམས་ཅད་འོད་གསལ་བ་ཉིད་དོ། །

[Block 3039]
རྫོགས་པའི་རིམ་པའི་རྣལ་འབྱོར་པས་སོ་སོར་སྡུད་པའི་ཡན་ལག་གིས་འཇུག་པ་ནི་ཤེས་པ་གསུམ་གྱི་རྒྱུ་ཅན་ཡིན་ནོ་ཞེས་བསྟན་པའི༌[^1974]ཕྱིར། ཐཱ། འདི་ལས་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། འདོད་པའི་ཡོན་ཏན་ལྔ་ཉེ་བར་སྤྱོད་པའི་དུས་སུ་དམན་པ་དང་བར་མ་དང་དམ་པའི་དབྱེ་བས་སོ་སོ་ཐ་དད་པའི་གཟུགས་ལ་སོགས་པ་ཡུལ་ལྔ་མཆོག་ཏུ་གྱུར་པར་རྣམ་པར་འཇོག་ཅིང་ཤེས་པ་གསུམ་གྱི་ངོ་བོ་ཉིད་ཡིན་ཞེས་རྣམ་པར་སྤྱོད་ཅིང་། ཡུལ་དང་དབང་པོ་བཅུ་པོ༌[^1975]གཉིས་སུ་མེད་པར་མཐོང་ནས། རྣམ་པར་སྣང་མཛད་ལ་སོགས་པ་དེ་བཞིན་གཤེགས་པའི་ངོ་བོར་ལྷག་པར་མོས་ཏེ། རྣལ་འབྱོར་པས་གནས་པར་བྱའོ། །

[Block 3040]
སོ་སོར་སྡུད་པ་དག་པར་བྱ་བའི་ཕྱིར་བསམ་གཏན་གྱི་ཡན་ལག་གིས་འཇུག་པ་གང་ཡིན་པ་དེ་ནི་ཡེ་ཤེས་གསུམ་གྱི་རྒྱུ་ཅན་ནོ་ཞེས་བསྟན་པར་བྱ་བའི་ཕྱིར། ག །དབང་པོ་རང་ཉིད་ཅེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། དབང་པོ་ལྔ་པོ༌[^1976]ནི་རང་རང་གི་ཡུལ་འཛིན་པ་ལ་སྲེད་པ་ཅན་ཡིན་པས་གང་གི་ཚེ་དེ་རྣམས་གཟུང་བར་བྱེད་ན་དེའི་ཚེ་དེ་བཞིན་གཤེགས་པའི་ངོ་བོ་ཉིད་ཡེ་ཤེས་ལྔའི་རང་བཞིན་གྱིས་སྣང་བས་སྤྱོད་པར་བྱའོ། །

[Block 3041]
དོན་དེ་ཉིད་རྒྱས་པར་བསྟན་པར་བྱ་བའི་ཕྱིར། ཏ། དབང་པོ་དེ་དེའི་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། མིག་ལ་སོགས་པའི་དབང་པོའི་སྒོ་ནས་རང་རང་གི་ཡུལ་ཐོབ་ཅིང་། དེ་དང་དེ་ལས་འབྱུང་བའི་དགའ་བས་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཚིམ་པར་བགྱིད་དོ་ཞེས་ལྷག་པར་མོས་པས་ཤེས་པ་གསུམ༌[^1977]ཁོ་ནའི་རྣམ་འཕྲུལ་ཡིན་ཏེ། བདེ་བའི་རང་བཞིན་རྣམ་པར་ཤེས་པ་གསུམ་ལས་འབྱུང་བའི་ཕྱིར་རོ། །ཤེས་པ་གསུམ་བརྟག་པ་ཉེ་བར་སྡུད་པ༌[^1978]བསྟན་པར་བྱ་བའི་ཕྱིར། ཀཱ། སྐུ་གསུམ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། དང་པོའི་སྦྱོར་བ་ལ་སོགས་པའི་ཏིང་ངེ་འཛིན་གསུམ་གྱི་རིམ་པའམ་བདག་ལ་བྱིན་གྱིས་རློབ་པའི་རིམ་པས། ཆོས་དང་ལོངས་སྤྱོད་དང་སྤྲུལ་པའི་བདག་ཉིད་སྐུ་གསུམ་པོ༌[^1979]བཅོམ་ལྡན་འདས་ཀྱིས་གང་གསུངས་པ། ཐ་དད་པར་སྐྱོབ་པས་གསུངས་པ་ནི་སོ་སོར་ངེས་པ་ཅན་གྱིས་ངེས་པར༌[^1980]བསྟན་པ་གང་ཡིན་པ་དེ་ཡང་ཤེས་པ་གསུམ་གྱི་རྣམ་འཕྲུལ་ཡིན་ནོ། །

[Block 3042]
རྫོགས་པའི་རིམ་པའི་སྦྱོར་བ་ཡིས། །གཅིག་ཏུ་ཡང་ནི་འགྱུར་བ༌[^1981]ཡིན། ཞེས་པ་ལ། ཡེ་ཤེས་གསུམ་གྱི་རྣམ་པར་རྟོག་པ་སྤངས་པས། འོད་གསལ་བ་ཤར་བར་གྱུར་པས་རོ་གཅིག་ཏུ་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3043]
དེ་ཡན་ཆད་ཡེ་ཤེས་གསུམ་པོ་རྣམ་པར་དཔྱོད་པའི་མཚན་ཉིད་ཅན་སྦས་པའི་དོན་རྣམ་པ་གཅིག་ཏུ་བསྟན་ཏོ། །

[Block 3044 [HEADING]]
##### འདོད་ཆགས་ཀྱི་ཆོས་རབ་ཏུ་བསྟན་པས་སྦས་པའི་དོན་གཉིས་པ། ^1-8-1-2-0

[Block 3045]
ཡེ། གང་ཡང་ཁམས་གསུམ་སེམས་ཅན་རྣམས། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྔོན་དུ་བཤད་པའི་ཚིགས་སུ་བཅད་པ་བཤད་པར་བྱ་སྟེ། སྒོ་ང་ལས་སྐྱེས་པ་དང་མངལ་ནས་སྐྱེས་པ་དང་དྲོད་གཤེར་ལས་སྐྱེས་པ་དང་རྫུས་ཏེ་སྐྱེས་པའི་དབྱེ་བས་ཁམས་གསུམ་གྱི་སེམས་ཅན་ཇི་སྲིད་ཡོད་པ་དེ་སྲིད་ཐམས་ཅད་བསམ་གཏན་དང་ཀློག་པའི་ཏིང་ངེ་འཛིན་དང་ཁ་ན་མ་ཐོ་བ༌[^1982]མེད་ཅིང་མི་ཤེས་པས་ཀྱང་རྡོ་རྗེའི་བཟླས་པས་གསང་སྔགས་ཀྱི་རྒྱལ་པོ་རང་བཞིན་གྱིས་བཟླས་པར་བྱེད་དེ། སྲོག་དང་རྩོལ་བ་དེའི་ངོ་བོར་ཟློས༌[^1983]པའི་ཕྱིར་རོ། །

[Block 3046]
གང་གི་ཕྱིར་ཕ་མ་མཉམ་པར་སྦྱོར་བའི་དུས་སུ་འཇུག་པས༌[^1984]སོགས་པའི་རླུང་གསུམ་གྱི་བདག་ཉིད་ཉེ་བར་སྡུད་པས་སེམས་ཅན་དེ་རྣམས་སྐྱེས་པའི་ཕྱིར་རོ། །

[Block 3047]
ཉིན་དང་མཚན་དུ་སྟོང་ཕྲག་ཉི་ཤུ་རྩ་གཅིག་དང་དྲུག་བརྒྱའི་རླུང་རྣམས་རྒྱུ་བ་སྟེ་ཟོ་ཆུན་བཞིན་ནོ། །

[Block 3048]
འདིས་ནི་འདོད་ཆགས་ཀྱི་ཆོས་རབ་ཏུ་བསྟན་པས་སྦས་པའི་དོན་གཉིས་པ༌[^1985]བཤད་དོ། །

[Block 3049]
ད་ནི་ཀུན་རྫོབ་ཀྱི་བདེན་པ་རྟགས་པར༌[^1986]བྱེད་པའི་མཚན་ཉིད་བདག་ལ་བྱིན་གྱིས་རློབ་པའི་རིམ་པ་བསྟན་པར་བྱ་བའི་ཕྱིར། ཡ། གང་ཞིག་ཅེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། སངས་རྒྱས་རྣམས་ཀྱིས༌[^1987]ནི་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་སྐུ་སྟེ་རྣམ་པའོ། །

[Block 3050]
དེ་འཇའ་ཚོན་བཞིན་དུ་གང་གིས་མཐོང་བ༌[^1988]དེ་མཚན་ཉིད་དོ། །
--- END BLOCKS ---
