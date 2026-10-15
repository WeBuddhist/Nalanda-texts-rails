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
[Block 2836]
སེམས་ཇི་ལྟ་བུ་ཞེ་ན། དེའི་ཕྱིར་དེར་འདུན་པས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འབྱིན་པར་འདུན་པས་ཡིན་གྱི་རྒྱུག་པ་ལ་སོགས་པའི་སེམས་ནི་མ་ཡིན་ནོ། །སུ་ལས་ཕྱུང་བ་ཞེ་ན། དེའི་ཕྱིར་རང་གི་ཁུ་བའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རང་གི་ཁུ་བ་ཡིན་གྱི་གཞན་གྱི་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2837]
འདི་ལ་ཁུ་བ་ཕྱུང་བ་ནི་མང་དུ་ཡོད་དེ། གནས་ནས་དབྱུང་བ་དང་གཞན་ཡང་སྦུབས་སུ་འོང་བས་དབྱུང་བ་དང་། དབང་པོའི་མཐའ་ནས་དབྱུང་བ་ནི་གསུམ་པ་ཞེས་བྱའོ། །

[Block 2838]
འདི་རྣམས་འདི་ལ་སུ་ཞིག་ལས་ཕྱུང་བ་ཞེ་ན། དེའི་ཕྱིར་དང་པོ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རང་གི་ཁུ་བ་ཡིན་པ་ནི་དང་པོ་སྟེ་ཕྱུང་བ་དེ་ལའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2839]
ཁུ་བ་ལ་ནི་མ་ཡིན་ཏེ་འོན་ཀྱང་ལུས་འདི་ལ་ཁུ་བའི་གནས་སུ་གྱུར་པ་ལོགས་ཤིག་ན་འཁྲིས་པ་ལྟ་བུ་མེད་དེ། ཡན་ལག་རྣམས་ལས་འབྱུང་བ་སྟེ། དཔེར་ན་བུ་རམ་ཤིང་ལས་ཁུ་བ་དང་ཤ་ལས་ཚིལ་དང་། ཞོ་ལས་མར་རོ། །

[Block 2840]
དེ་བཞིན་དུ་འདིར་འཕོ་བ་རྟོགས་པར་བྱའོ། །

[Block 2841]
སླར་འདི་ནི་ཕྱུང་བ་དང་པོ་དགེ་འདུན་ལྷག་མ་ཅིའི་ཕྱིར་ཏེ། དབང་པོའི་མཐའ་མ་ལ་སོགས་པ་རྣམས་ཀྱིས་ནི་མ་ཡིན་ནོ། །

[Block 2842]
འགའ་ཞིག༌[^1942]ཏུ་ཉེ་བ་འཁོར་གྱིས་ཞུས་པའི་འདོན་པ་ལས་བཙུན་པ་ཇི་ཙམ་གྱིས་ན་ཁུ་བ་ཕྱུང་བར་བརྗོད་པར་བགྱི། གང་གི་ཕྱིར་རྩའི་སྦུབས་ལ་བརྟེན་པར༌[^1943]གྱུར་ནའོ་ཞེས་བྱ་བའི་ཚིག་དང་། རྣམ་པར་འབྱེད་པའི་ཚིག་ལས་ཀྱང་། ཕྱུང་བའི་ཚིག་འདི་ནི་དེ་མ་ཐག་ཏུ་ཕྱུང་བའོ་ཞེས་གསུངས་སོ། །

[Block 2843]
གང་གི་ཕྱིར་གནས་ལ་གནས་པ་ལས་དེ་མ་ཐག་པ་ཉིད་མངོན་པར་འདོད་པ་རྣམ་པར་གནས་པ་ཡིན་གྱི་དབང་པོའི་མཐའ་མ་ནས་མ་ཡིན་ཏེ་མེད་པའི་ཕྱིར་རོ། །

[Block 2844]
དེ་བས་ན་རྣམ་པར་ཕྱུང་བ་གཞན་རྣམས་ཀྱིས་དེ་མ་ཐག་ཏུ་ཞེས་བྱ་བ་ཁྱད་པར་དོན་མེད་པའི་ཕྱིར་རོ། །

[Block 2845]
གང་གི་ཕྱིར་རྣམ་པར་སྤྱད་པར་བྱ་བ་མེད་ན་ཁྱད་པར་རབ་ཏུ་སྦྱོར་བ་མ་ཡིན་ཏེ། དབང་པོའི་མཐའ་མ་ནས་འབྱུང་བ་ལ་འདོད་ཆགས་ཤིན་ཏུ་ཤས་ཆེར་གྱུར་པ་ཉིད་དང་བསྒྲུབ་པ་ནི་མ་རྫོགས་པའོ། །

[Block 2846]
དེ་བས་ན་འདིར་དངོས་གཞི་འདི་ལ་སྦྱོར་བ་ཞེས་བྱ་ཞེ་ན་དེ་ནི་མ་ཡིན་ཏེ། ཚངས་པར་སྤྱོད་པ་མ་ཡིན་པ་བཞིན་དུ་དང་པོ་ལ་སྦྱོར་བའི་ཕྱིར་རོ། །

[Block 2847]
དེ་ལས་གཞན་པའི་ཆ་འབྱུང་བ་ལ་ཡང་འདི་ལྟར་དངོས་གཞིར༌[^1944]ཐལ་བར་འགྱུར་བས་སོ། །

[Block 2848]
རྩ་ལ་བརྟེན་པ་ཕྱུང་བ་ལ་ཡང་དངོས་གཞིར་ཐལ་བའི་ཕྱིར་འདིར་སྦོམ་པོའི་ལྟུང་བར་འདོད་པ་ཡིན་ནོ། །

[Block 2849]
བདེ་བ་དོན་དུ་གཉེར་བར༌[^1945]ཕྱུང་བའི་བདེ་བ་སོ་སོར་ཉམས་སུ་མྱོང་བའི་བསམ་པ་ཅན་སུ་ཞིག་ལ་འབྱིན་པའི་འདུན་པ་སྐྱེ་བ་ཡིན་ཏེ། རིག་པ་དོན་དུ་གཉེར་བ་སུ་ཞིག་ལ་གསང་སྔགས་ཀྱིས༌[^1946]ཕྱུང་བ་བསྒྲུབ་པ་ལ་བཞད་གད་ཅན་གྱི་ཆ་བྱད་ཅན་རིག་པར་གྱུར་པའི་བསླབ་པ་ཡང་དག་པར་བསྒྲུབ་པ་མངོན་པར་འདོད་པ་མང་ངོ་། །རིག་པ་དོན་དུ་གཉེར་བ་སུ་ཞིག་ལ་ཕྱུང་ནས་བཞག་པས་སོ། །

[Block 2850]
རྨ་རྣམ་པར་སྦས་པ་ལས་ཕྱུང་བར༌[^1947]སྐྱེ་དགུ་བསྒྲུབ་པ་སོ་སོར་ཤེས་བཞིན་པ་ལའོ། །

[Block 2851]
སྨན་དོན་དུ་གཉེར་བ་སུ་ཞིག་ལ་ཁུ་བ་ཕྱུང་བས་ནད་ཉེ་བར་ཞི་བ་སྨན་གྱིས་སམ་རྫས་གཞན་དང་ལྡན་པ་ལའོ། །

[Block 2852]
འགའ༌[^1948]ཞིག་ལ་ཁུ་བ་རྣམ་པར་དོར་བ་ལ་མངོན་པར་བརྩོན་པ་ལའོ། །

[Block 2853]
ཤིན་ཏུ་སྦྱངས་པ་དོན་དུ་གཉེར་བ་སུ་ཞིག་ལ་ལམ་དག་པ་བསྒྲུབ་པའམ། ལམ་ལ་ཡིད་ཆེས་པར་འདོད་པ་ལ་བདག་གི་ཁུ་བ་ཕྱུང་ངམ་འོན་ཏེ་མ་ཡིན་ཞེས་བྱ་བ་ཡོད་པ་ཉིད་དམ། བདག་ལ་ཁུ་བ་ཡོད་དམ་འོན་ཏེ་མ་ཡིན་སྙམ་དུ་ཡང་དག་པར་སྐྱེས་པ་ཡང་ཤེས་པར་འདོད་པ་ལ་བདག་ལ་ཁུ་བ་ཡང་དག་པར་སྐྱེས་སམ། འོན་ཏེ་མ༌[^1949]ཡིན་ཞེས་བྱ་བ་ལོའི་གནས་སྐབས་སམ། བུད་མེད་ཀྱིས་དུབ་པ་ལ་སོགས་པའི་སོ་སོར་ལྟུང་བའི་གནས་སྐབས་ལ་བདག་གི་ཁུ་བ་ནི་ཇི་ལྟ་བུའི་གནས་སྐབས་སྙམ་དུ་སྐལ་བ་དང་ལྡན་པ་ཉིད་དམ། བདག་གི་ཁུ་བ་ཇི་ལྟ་བུ་ཞེས་བྱ་བ་བདེ་བའི་རྣམ་པའི་དོན་དུ་ཡང་དག་པར་སྤྱོད་པས་ཤེས་པར་འདོད་པ་ལ་བདག་གི་བདེ་བ་འདི་ལྟ་བུ་ཞེས་ཡོད་པའམ། འདིར་སེམས་ཅན་གྱི་རྒྱུ་ཇི་ལྟ་བུ་ཞེས་བྱ་བ་དང་རང་བཞིན་ཇི་ལྟ་བུ་ཞེས་བྱ་བའི་ནུས་པའམ་རྣམ་པ་འདིས་ཁུ་བ་ཕྱུང་བས་བདག་གིས༌[^1950]ནུས་སམ་འོན་ཏེ་མིན་ཞེས་བྱ་བའི་བསླབ་པ་བསྒྲུབ་པའམ། བདག་གིས་འདི་ཕྱུང་བའི་རྣམ་པ་བསླབས༌[^1951]སམ་འོན་ཏེ་མ་ཡིན། འདིར་ལ་ལ་ཞིག་ཁ་ན་མ་ཐོ་བ་དང་བཅས་པ་དང་། ཁ་ན་མ་ཐོ་བ་མེད་པ་དང་། རྫོགས་པ་དང་མ་རྫོགས་པ་དང་ཤིན་ཏུ་ཆུང་བ་ཉིད་དང་། ཁ་ན་མ་ཐོ་བ་མ་ཡིན་པ་དེ༌[^1952]ཉིད་ཀྱི་ཕྱིར་ཅི་ཁྱད་པར་ཡོད་དམ་ཞེ་ན། དེའི་ཕྱིར་བདེ་བ་དང་རིག་སྔགས་དང་ས་བོན་དང་སྨན་དང་བརྟག་པའི་ཕྱིར་བརྟག་པ་ལ་བྱེ་བྲག་མེད་དོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 2854]
རྣམ་པ་གང་གིས་འབྱིན་པ་ཞེ་ན། དེའི་ཕྱིར་རེག་པས་སོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 2855]
རེག་པ་ཇི་ལྟ་བུས༌[^1953]ཤེ་ན། དེའི་ཕྱིར་བརྩལ་བས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བྱ་བས་དྲུད་པ་ལ་སོགས་པ་ཡིན་གྱི༌[^1954]གནས་པ་ནི་མ་ཡིན་ནོ། །

[Block 2856]
འདིར་ཚིག་ནི་རྩོལ༌[^1955]ན་ཞེས་གསུངས་ལ། འདུལ་བྱེད་དག་ལས་དགེ་སློང་ཡན་ལག་གི་རྣམ་པས་བཟུང་བ་ལ་མི་གཙང་བ་བྱུང་བ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ཉེས་པ་སྡོམ་པོར༌[^1956]འགྱུར་ཞེས་གསུངས་སོ། །གང་ལ་རེག་པས་ཤེ་ན། དེའི་ཕྱིར་ཡན་ལག་གི་རྣམ་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཕྱོགས་གཞན་ལ་ནི་མ་ཡིན་ནོ། །གང་གིས༌[^1957]རེག་པ་ཞེ་ན། དེའི་ཕྱིར་ཕྱི་རོལ་གྱིས་ཀྱང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ནང་གི་བདག་ཉིད་འབའ་ཞིག་གིས་ནི་མ་ཡིན་ནོ། །

[Block 2857]
སེམས་ཅན་དུ་བགྲང་བས་སོ། །

[Block 2858]
དེ་ནི་རྣམ་པར་གནས་པས་སོ་ཞེས་བྱ་བ་ནི་མི་འཕོ་བ་སྟེ་ལུས་ཀྱི་རྣམ་པ་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2859]
གང་ཡང་རུང་བ་ཅིག་གི་ཆས་རེག་པས་བྱུང་བ་ལ་དགེ་འདུན་གྱི་ལྷག་མའོ། །

[Block 2860]
ལག་པ་ཁོ་ནས་རེག་པར༌[^1958]ཕྱུང་བར་མ་ཟད་དེ།[^1959] །ལུས་ཀྱི་རྣམ་པ་ལས་ཉམས་པར༌[^1960]འཕོ་བ་ལ་ནི་སྦོམ་པོ་སྟེ། ཤའི་དུམ་བུས་ནི་སྦོམ་པོ་ཞེས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 2861]
རྣམ་པ་གང་ཡང་རུང་བ་དང་། དེའི་རྣམ་པ་བརྩལ་བས་རེག་པས་སོ་ཞེས་བྱ་བར་ཤེས་པས་ཆང་བས་བཅང་བའི་བརྩལ་བའི་རང་བཞིན་འབའ་ཞིག་ཏུ་མ་ཟད་དེ། [^1961]དམ་དུ་བཅང་བ་དང་བཅས་པས་བྱེ་བྲག་ཡོངས་སུ་མ་བཟུང་བས་ཡང་དག་པར་བསྟན་པའི་དོན་དུ༌[^1962]རྣམ་པར་མཚོན་པར་བྱའོ། །

[Block 2862]
རིལ་གྱིས༌[^1963]བཅད་པ་དང་དམ་དུ་བཅང་བ་གཉིས་མེད་པར་ཡང་ངོ་ཞེས་བྱ་བ་ནི་དེ་གཉིས་མེད་པར་ཡང་དངོས་གཞིར་འགྱུར་བའོ། །

[Block 2863]
བྱེ་བྲག་ངེས་པར་མྱོང་བ་ལ་སོགས་པ་བདེ་བ་སོ་སོར་ཉམས་སུ་མྱོང་བ་ཡང་འདིར་རེས་འགའ་འབྱུང་སྟེ། དེ་རྣམས་ལ་འདིར་ཆ་ཤས་ཉིད་ཅི་ཞིག་ཡོད་དམ་མ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་བྱེ་བྲག་ངེས་པར་མྱོང་བ་དང་བྱུང་ལ་ཐུག་པ་དང་ངད་ལས་པའི་བདེ་བ་ཉམས་སུ་མྱོང་བ་དག་ཀྱང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཡང་གི་སྒྲས་ནི་ཆོ་ག་བསྡུ་བའི༌[^1964]དོན་དུའོ། །

[Block 2864]
བདེ་བ་སོ་སོར་ཉམས་སུ་མྱོང་བ་འདི་རྣམས་མེད་པར་ཡོད་ཅེས༌[^1965]བྱ་བ་ནི་འདིར་བྱེ་བྲག་ངེས་པར་མྱོང་བ་ལ་ཐ་དད་པར་བྱས་པ་བཞིན་དུ་ཁྱད་པར་དུ་མྱོང་བར་རོ། །

[Block 2865]
ལུས་དང་དབང་པོ་ཆགས་པ་ཉིད་ལ་ལུས་ཀྱི་རྣམ་པར་ཤེས་པའི་བྱེད་པ་པོས་ཉེད་པས༌[^1966]རེག་པ་འབྱུང་བ་སྟེ་དེ་ཉམས་སུ་མྱོང་ནའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2866]
བྱུང་ལ་ཐུག་པ་ནི་བརྩལ་བའི་ཁུ་བའི་ཁུ་བ་ལ་ལུས་དང་དབང་པོ་ལས་ཀྱང་ངོ་། །ངད་ལས་པའི་བདེ་བ་ཉམས་སུ་མྱོང་བ་དག་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་ལུས་དང་དབང་པོ་ལས་བྱུང་མ་ཐག་པ་རྣམ་པར་གྲོལ་བཞིན་པའི་བྱེད་པའི་འཚོ་བ་ལ་མྱུར་དུ་ཉེ་བར༌[^1967]འཚོ་བར་བྱེད་པའི་གང་ཡིན་པ་དེ་ནི་འདིར་བདེ་བ་སོ་སོར་ཉམས་སུ་མྱོང་བ་དག་ཀྱང་ངོ་། །གང་དུ་ཁུ་བ་འབྱིན་པ་ལ་རྩེ་གཅིག་པ་ཉིད་ཀྱིས་འདི་ལ་ཉེ་བར་འཚོ་བར་བྱེད་པ་དེ་ལ་བྱེ་བྲག་ངེས་པར་མྱོང་བར་བྱེད་པ་ལ་བདེ་བ་སོ་སོར་ཉམས་སུ་མྱོང་བ་ལ་རྩེ་གཅིག་པ་ཉིད་མེད་པར་ཡང་མངོན་པར་གྲོལ་བའི་ཕྱིར་རོ། །

[Block 2867]
འདིར་གཞུང་ནི༌[^1968]དགེ་སློང་གིས༌[^1969]བྱེ་བྲག་ངེས་པར་མྱོང་བའི་བདེ་བ་སོ་སོར་ཉམས་སུ་མྱོང་བར་བྱེད་དེ། ཁུ་བ་འབྱིན་པར་བྱེད་ན་དགེ་འདུན་ལྷག་མའི་ལྟུང་བར་འགྱུར་རོ། །

[Block 2868]
དེ་བཞིན་དུ་བྱུང་ལ་ཐུག་པའི་བདེ་བ་དང་། ངད་ལས་པའི་བདེ་བ་སོ་སོར་ཉམས་སུ་མྱོང་བར་བྱེད་དེ། ཁུ་བ་འབྱིན་པ་ཡང་སྔ་མ་བཞིན་དུ་འབྱིན་པར་བྱེད་ན་ཞེས་བྱའོ། །

[Block 2869]
སྔ་མ་བཞིན་དུ་ཕྱུང་བ་ལ་དེའི་འདུན་པས་རང་གི་ཁུ་བ་དང་པོར་རེག་པས་ཆ་ཤས་ཀྱི་ཚོགས་ལ་བྱ་བ་བྱས་ནས་ཕྱི་རོལ་གྱི་སེམས་ཅན་དུ་བགྲང་བས་ཀྱང་དེའི་རྣམ་པར་གནས་པ་མ་ཡིན་ཞེས་བྱ་བ་ཆ་ཤས་འདི་རྣམས་ཀྱི་གང་ཡང་རུང་བ༌[^1970]ཅིག་མ་ཚང་བས༌[^1971]ལྷག་མ་མེད་པའོ། །

[Block 2870]
སྦུབས་སུ་མ་འོངས་པའོ་ཞེས་བྱ་བ་ནི་འདི་ལ་དང་པོའི་གནས་ལ་དོར་བར་འབྱུང་བར་འགྱུར་ཏེ། གང་དུ་འཕོ་བ་འདི་ལ་གནས་པར་འགྱུར་བ་དེ་ལས་འཕོ་བར་བྱེད་པས་ན་འདི་ནི་སྐུར་བ་བཏབ་པ་སྟེ་འདིར་སྦོམ་པོ་འཆད་པར་འགྱུར་རོ། །

[Block 2871]
ཤུགས་ཀྱི་གནས་སྐབས་སུ་བཏང་ན་རྫོགས་པར་མ་བྱས་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་དེ་མ་ཐག་པར་འཕོ་བཞིན་པ་ནི་འཕོ་བ་སྟེ་ལུས་ཀྱི་བྱ་བ་བཏང་བ་ནི་སྤོང་བའོ། །

[Block 2872]
ཤུགས་ཀྱི་གནས་སྐབས་སུ་སྤོང་བ་ཡོད་པར་འགྱུར་བ་ལ་སྦྱོར་བ་སྔ་མའི་དབང་གིས་རྫོགས་པ་གང་ཡིན་པ་ནི་ཁུ་བ་ཕྱུང་བ་སྟེ། དེ་ལ་མ་བྱས་པ་ཉིད་ནི་སྦོམ་པོའི་ལྟུང་བ་ཉིད་དོ། །

[Block 2873]
དེ་བཞིན་དུ་དེར་སྦྱར་བ༌[^1972]ཉིད་ཀྱི་ཕྱིར་དགེ་འདུན་ལྷག་མ་ནི༌[^1973]མ་ཡིན་ནོ། །

[Block 2874]
དངོས་གཞི་བསྐྱེད་པ་ཡང་འདི་ལྟར་མཐོང་སྟེ། དཔེར་ན་འདིར་སྲོག་གཅོད་པ་ལ་བརྟེན་པ་ནི་དེ་ལ་ནི་གྲོལ་བ་མ་ཡིན་ཏེ་སྲོག་གཅོད་པ་ལ༌[^1974]ནི་སྲོག་ཆགས་རྣམས་ལ་རྣམ་པར་ལྟུང་བ་ཡིན་ཏེ། དེ་བས་ན་དེ་བཞིན་དུ་འདིར་སྤོང་བ་རྫོགས་པ་ལ་བྱས་པ་ཉིད་ཅེས་བྱ་བ་དེའི་ཕྱིར་འདི་རྣམ་པར་ཤེས་པའོ། །

[Block 2875]
འདིར་གཞུང་ནི་ཤུགས་བཏང་སྟེ། ཁུ་བ་ཕྱུང་ན་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །
--- END BLOCKS ---
