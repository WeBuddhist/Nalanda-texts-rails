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
[Block 2941]
ལེགས་འབྱུང་ཆུང་ཡང་ཞེས་བྱ་བ་ནི་ཡུན་རིང་དུ་འཚོ་བར༌[^1883]གྱུར་ཀྱང་མཐོང་བའི་ཆོས་ལ་བདེ་བ་ཤིན་ཏུ་ཆུང་བའི་ཕྱིར་རོ། །

[Block 2942]
དེ་ལྟར་དེ་ལ་རང་གི་ཆུང་མ་ཡོངས་སུ་གཏོང་བ་མི་རིགས་པར་བསྟན་ནས། དེ་ནི༌[^1884]བདག་ཉིད་ཀྱིས༌[^1885]བླང་བ་ཉིད་དུ་མི་རིགས་པར་བསྟན་པའི་ཕྱིར་སྨྲས་པ། དམ་པ་རྣམས་ནི་ཕ་རོལ་སྨད་ལ་སོགས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 2943]
སྨད་པ་ལ་སོགས་པའི་སྡུག་བསྔལ་གང་ཡིན་པ་དེ་ནི་སྨད་པ་ལ་སོགས་པའི་སྡུག་བསྔལ་བྱས་པ་སྟེ། གང་སྔར་བསྟན་པའི་ཆོས་དང་འགལ་བ་དང་། སྐྱེ་བོས་སྨད་པ་དང་། བདེ་བ་ཉམས་པའི་མཚན་ཉིད་ནི་སྨད་པ་ལ་སོགས་པའི་སྡུག་བསྔལ་སྨོས་པ་འདིས་གཟུང་ངོ་། །མི་གནོད་པར་ཞེས་བྱ་བ་ནི་སྨད་པ་ལ་སོགས་པའི་སྡུག་བསྔལ་བླངས་ནས་སོ། །

[Block 2944]
བདག་གི་དོན་སྒྲུབ་ཅེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའི་སྒྲུབ་པ་སྟེ། བདག་དང་གཞན་གྱི་ཆོས་སུ་བཤད་པའོ། །

[Block 2945]
གཉི་གའི་ཆོས་མ་ཡིན་པ་མེད་པར་བསྟན་པའི་ཕྱིར་རྗེའི་དོན་དུ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་འདི་ཡིན་ཏེ། དེའི་སླད་དུ་ལྗོངས་ཀྱི༌[^1886]མི་དང་བཅས་པས་ཞེས་བྱ་བ་འདིས་ནི་གཉི་ག་ལ་ཡང་ཆོས་མ་ཡིན་པ་དང་གྲགས་པ་མ་ཡིན་པ་མེད་པར་བསྟན་ཏོ། །

[Block 2946]
རྒན་པ་བསྙེན་བཀུར་བྱ་བ་བྱས་པ་དང་། ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིའི་བསྡུས་པའི་དོན་ནི་དགེ་བའི་བཤེས་གཉེན་བསྟན་པ༌[^1887]དང་། ཆོས་ཉན་པ་དང་ཚུལ་བཞིན་ཡིད་ལ་བྱེད་པ་བསྟན་ཏོ། །

[Block 2947]
ཡང་ན་བླ་མ་དང་དམ་པའི་ཚོགས་ལ༌[^1888]བསྙེན་བཀུར་བྱས་པ་དང་ཤེས་རབ་ཕུན་སུམ་ཚོགས་པར༌[^1889]བསྟན་ཏོ། །

[Block 2948]
འཁོར་གསུམ་གྱི་རིག་པ་ནི་འཁོར་གསུམ་རིག་པའོ། །

[Block 2949]
དོན་གྱི་དེ་ཁོ་ན་ཉིད་ནི་དོན་གྱི་དེ་ཉིད་དོ། །

[Block 2950]
ལྷག་པའི་དོན་གྱི་དེ་ཁོ་ན་ཉིད་ནི་ལྷག་པའི་དེ་ཁོ་ན་ཉིད་དེ། འཁོར་གསུམ་རིག་པའི་ལྷག་པའི་དོན་གྱི་དེ་ཁོ་ན་ཉིད་དོ། །

[Block 2951]
འཇིག་རྟེན་པ་ལ་ཕན་དང་གནོད་པ་ནི། །ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་གཉིས་ནི་སྐྱེ་དགུ་རྣམས་ཆོས་དང་འགལ་བར་འགྱུར་བའི་དབང་དུ་བྱས་པའོ། །

[Block 2952]
གལ་ཏེ་རྒྱལ་པོ་རྣམས་ལེགས་པར་སྤྱོད་ན་ནི་འབངས་རྣམས་ལ་ཕན་པ་ཡིན་ལ། ཅི་སྟེ་ལེགས་པ་མ་ཡིན་པ་སྤྱོད་ན་ནི་གནོད་པ་ཡིན་ནོ། །

[Block 2953]
འབངས་རྣམས་སྙིང་ཉེ་བསམས་ནས་ནི། །ཞེས་བྱ་བ་ནི་གཞན་གྱི་སྐྱེ་བོ་བས་ལྷག་པར་བདག་ལ་སྙིང་ཉེ་བ་ཡིན་ཏེ། ཁྱད་པར་དེས་ན་བདག་གིས་ལེགས་པ་དང་ལེགས་པ་མ་ཡིན་པ་སྤྱད་པ་དེ་གཉིས་ཀྱིས་འཇིག་རྟེན་པའི་ཕན་པ་དང་། གནོད་པའི་རྒྱུར་གྱུར་པ་ཡིན་པར་བསྟན་ཏོ། །

[Block 2954]
གཏམ་སྙན་པ་ནི་གྲགས་པའོ། །

[Block 2955]
ལམ་གྱི་མཆོག་ཉིད་ནི་ཆོས་ཀྱི་ལམ་མོ། །

[Block 2956]
རྒྱལ་པོ་རྣམས་ཀྱི་སྤྱོད་པ་ལ་འབངས་རྣམས་རག་ལུས་པ་ཡིན་ཏེ། ཕན་པ་དང་གནོད་པར་འགྱུར་བ་དེ་ཉིད་བསྒྲུབ་པའི་ཕྱིར་དཔེས་བསྟན་པ་སྟེ། ཁྱུ་མཆོག་འགྲོ་བ་དྲང་ངམ་ཡོ་བ་བཞིན། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ནོ། །

[Block 2957]
རྒྱལ་པོའི་ལེགས་པ་དང་ལེགས་པ་མ་ཡིན་པའི་སྤྱོད་པ་ལ་སྐྱེ་དགུའི་ཕན་པ་དང་གནོད་པ་རག་ལུས་པ་བདག་ཉིད་ཀྱང་མི་རིགས་པ་ལས་ལྡོག་པར་མི་ནུས་ན་གཞན་དག་ཇི་ལྟར་བཟློག༌[^1890]པར་མི༌[^1891]ནུས་ཞེས་པ་སྟེ། ཇི་ལྟར་འཁྲུལ༌[^1892]པ་མེད་པར་རྗེས་སུ་འབྲང་བའི་སྐྱེ་དགུའོ། །

[Block 2958]
དེ་ལྟར་འབངས་ལ་ཕན་པའི་ཞེས་བྱ་བའི་ཚིགས་བཅད་ནི་འབངས་ལ་ཕན་པར་ལྟ་བའི་ཚིགས་བཅད་ཡིན་ཏེ། འབངས་ལ་ཕན་པ་འོག་ཏུ་བཤད་པ་ནི་མི་རིགས་ཏེ། སྔར་སྨོས་པ་ནི་སྐྱེ་དགུ་ལ་ཕན་པ་གཙོ་བོ་ཡིན་པའི་ཕྱིར་དེ་ལྟར་གོང་དུ་བསྟན་ཏོ། །

[Block 2959]
དེའི་འོག་ཏུ་སྨོས་པའི་ཆོས་དང་གྲགས་པ་ལས་ནི་འགལ་བར་གྱུར་ཀྱང་ཕན་པ་ལས་མི་འདའ་བར་བསྟན་པའི་ཕྱིར་གཙོ་བོ་ཡིན་ཏེ། འབངས་ལ་ཕན་པར་ལྟ་བ་ནི་གཅེས་པའི་ཕྱིར་རོ། །

[Block 2960]
དེ་ལྟར་ཕན་པ་དེ་ལ་ཞུགས་པ་དང་། དེའི་འོག་ཏུ་ཆོས་དང་། དེའི་འོག་ཏུ་གྲགས་པའོ། །

[Block 2961]
དེ་བས་ན་རིམ་པ་འདི་ནི་བདག་གིས་དེ་ལྟར་བསྟན་ཏོ། །

[Block 2962]
ཨེ་མའོ་འབངས་རྣམས་སྐལ་བ་ཕུན་སུམ་ཚོགས། །ཞེས་བྱ་བ་ནི་ཅིའི་ཕྱིར་ཞེ་ན། དཔེ་མེད་པའི་ཆོས་ལ་རྗེས་སུ་དགའ་བ་དང་། བདེ་བ་ལ་མ་ཆགས་པ་དེ་ལྟ་བུས་བསྲུངས་པ་ཐོབ་པས་སོ། །

[Block 2963]
དཔེ་མེད་པ་ནི་དཀའ་ཐུབ་ཀྱི་ནགས་ན་གནས་པ་ལ་ཡང་ཆོས་ལ་དགའ་ཞིང་བདེ་བ་ལ་མ་ཆགས་པ་དེ་ལྟ་བུ་དཀོན་ཏེ། དཀའ་ཐུབ་ནགས་ན་གནས་པའི་ཡོན་ཏན་དག་ལས་ཤིན་ཏུ་ལྷག་པའི་ཕྱིར་རོ། །

[Block 2964]
རྒྱལ་པོ་ཆེན་པོ་ཞེས་བྱ་བ་ནི་ཐ་མལ་པ་མ་ཡིན་པ་སྟེ།[^1893] དོན་ཇི་ལྟ་བ་བཞིན་གྱི་མིང་བསྟན་པའོ། །

[Block 2965]
ཆེན་པོའི་སྒྲ་ནི་སྔར་སྨོས་པ་དེ་ཉིད་བསྒྲུབ་པའི་ཕྱིར་སྨོས་པ་ཡིན་ཏེ། གང་རྣམས་བསྲུང་བའི་རྒྱལ་པོ་ཁྱོད། །ཅེས་བྱ་བའི་ལས་ཀྱིས་སོ། །

[Block 2966]
དེ་ལ་ངོ་མཚར་ཆེ་བ་ཉིད་མེད་པར་བསྟན་པའི་ཕྱིར། རྒྱ་མཚོ་རིན་ཆེན་འབྱུང་གནས་བཞིན། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ཏེ། འདིས་ནི༌[^1894]གཞན་ལ་མེད་པའི་ཡོན་ཏན་སྟོན་ཏོ། །

[Block 2967]
[^1895]སློབ་དཔོན་དཔའ་བོས་མཛད་པའི་སྐྱེས་པའི་རབས་རྒྱ་ཆེར་བཤད་པ་ལས་མྱོས་བྱེད་མའི་སྐྱེས་པའི་རབས་སོ།། །།

[Block 2968 [HEADING]]
## ལེགས་པར་ཕ་རོལ་ཏུ་ཕྱིན་པའི་སྐྱེས་པའི་རབས། ^15-0

[Block 2969]
ཆོས་ལ་གནས་ན་ཞེས་བྱ་བ་ནི་བདེན་པའི་ཚིག་གང་གི་གནས་ཆོས་ཡིན་པ་དེ་ནི། བདེན་པའི་ཚིག༌[^1896]ཆོས་ལ་གནས་པའོ། །

[Block 2970]
འདིར་ཆོས་ཞེས་སྨོས་པས་ནི་སྲོག་གཅོད་པ་ལས་ལྡོག་པ་ཡིན་ཏེ། དེ་ལ་གནས་པའི་གང་བདེན་པའི་ཚིག་དེ་ནི་ཆོས་ལ་གནས་པའི་བདེན་པའི་ཚིག་ཡིན་ནོ། །

[Block 2971]
འབྲས་བུ་ནི་དེའི་འབྲས་བུ་ལྟ་སྨོས་ཀྱང་ཅི་དགོས་ཞེས་བྱ་བ་ཡིན་ཏེ། དེ་ཞེས་བྱ་བ་ནི་གང་བདེན་པའི་ཚིག་གི་གནས་སྲོག་ཆགས་ལ་ཕན་འདོགས་པར་འཇུག་པ་དང་། སྲོག་གཅོད་པ་ལས་ལྡོག་པའོ། །

[Block 2972]
ཡང་ན་བདེན་པའི་ཚིག་དེའི་འབྲས་བུ་དེ་ནི་དེའི་འབྲས་བུ་སྟེ། སྲོག་ཆགས་ལ་ཕན་གདགས་པ་དང་། རྣམ་པར་འཚེ་བ་ལས་བཟློག་པའོ། །

[Block 2973]
ཆོས་ཀྱི་རྗེས་སུ་འཇུག་པ་ཞེས་བྱ་བ་ནི་བདེན་པའི་ཚིག་གི་འབྲས༌[^1897]བུར་གྱུར་པའི་ཆོས་ཀྱི་རྗེས་སུ་འཇུག་པའོ། །

[Block 2974]
ཡང་ན་ཆོས་ནི༌[^1898]སྲོག་གཅོད་པ་ལས་སླར་ལྡོག་པའོ། །

[Block 2975]
དེ་ལ་གནས་པའི་བདེན་པའི་ཚིག་གང་ཡིན་པ་དེ་ནི་ཆོས་ལ་གནས་པའི་བདེན་པའི་ཚིག་སྟེ། དེའི་འབྲས་བུ་གང་སྲོག་གཅོད་པ་ལས་ལྡོག་པ་ཉིད་དོ། །

[Block 2976]
དེ་བས་ན་ཆོས་ཀྱི་རྗེས་སུ་འཇུག་པར་བྱའོ་ཞེས་བྱ་བ་ཡིན་ཏེ། སྲོག་གཅོད་པ་ལས་ལྡོག་པའི་མཚན་ཉིད་ཀྱི་ཆོས་ཀྱི་རྗེས་སུ་འཇུག་པར་བྱའོ་ཞེས་པའོ། །

[Block 2977]
རང་བཞིན་གྱིས་ཤེས་རབ་རྣོ་བས་ཞེས་བྱ་བ་ནི་ཤེས་རབ་དང་སྙིང་རྗེ་རབ་ཏུ་བསྒོམས་པའི་ཕྱིར་བྱང་ཆུབ་སེམས་དཔའ་ནི་རིགས་ཀྱིས་ཤེས་རབ་ཤས་ཆེ་བ་ཡིན་པས་ཤེས་རབ་རྣོ་བ་ཞེས་སྨོས་སོ། །

[Block 2978]
རང་བཞིན་དང་རིགས་དང་། རྒྱུ་དང་ས་བོན་ཞེས་བྱ་བ་རྣམ་གྲངས་སོ། །

[Block 2979]
རང་བཞིན་གྱིས་ཤེས་རབ་རྣོ་བ་ནི་རིགས་ཀྱིས་གྲུབ་པའི་ཤེས་རབ་རྣོ་བའོ། །

[Block 2980]
གཙུག་ལག་ཁྱད་པར་ཅན་གང་དང་གང་། སྒྱུ་རྩལ་ཁྱད་པར་ཅན་གང་དང་གང་ཞེས་བྱ་བ་ལ། ཁྱད་པར་ཅན་སྨོས་པ་ནི་གཙུག་ལག་དང་སྒྱུ་རྩལ་གྱིས་སེམས་ཅན་རྗེས་སུ་བཟུང་བར༌[^1899]བྱེད་པ་ཡིན་ཏེ། སློབ་པར་འདོད་པ་དེ་ཡང་དག་པར་བསྟན་པའི་ཕྱིར་དེ་དང་དེ་དག་ལ་ཞེས་བྱ་བ་ཡིན་ཏེ། སྐྱེ་བོ་གཞན་པས་ལྷག་པར་འགྱུར། །ཞེས་བྱ་བ་ནི་སྐྱེ་བོ་དྲི་མའི༌[^1900]ཤེས་རབ་ལས་ཀྱང་ལྷག་པར་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏེ། ཤེས་རབ་རྣོ་ཞིང་སྐྱེ་བོ༌[^1901]གཞན་པས་ཞེས་བྱ་བས་ནི་ལྷན་ཅིག་སྐྱེས་པའི་ཤེས་རབ་ཀྱིས་ཀྱང་ལྷག་པར་འགྱུར་བ་ཡིན་ཏེ། གཞན་དག་གི་ཤེས་རབ་ནི་འབད་པ་ལས་བྱུང་བའི་ཞེས་བྱ་བའི་དོན་ཏོ། །
--- END BLOCKS ---
