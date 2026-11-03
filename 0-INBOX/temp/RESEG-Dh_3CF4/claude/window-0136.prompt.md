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
[Block 4761]
དེའི་སྡུག་བསྔལ་ཐུན་མོང་ཉིད་དུ་གྱུར་པ་ནི། དེའི་སྡུག་བསྔལ་གྱི་རྒྱུས་ཐུན་མོང་དུ་གྱུར་པའོ། །

[Block 4762]
ཡ་རབས་ཀྱི་ཚུལ་བཞིན་དུ་སྐྱེ་བོ་དགེ་བའི་རང་བཞིན་སྟོན་པར་བྱེད་པའི་ཚིག་དེ་བསྒྲུབ་པའི༌[^3090]ཕྱིར། རྒྱལ་པོ་ཆེན་པོ་སྣད་པར་མ༌[^3091]གྱུར་ཏམ། །ཞེས་ཚིགས་བཅད་སྨོས་སོ། །

[Block 4763]
དེ་ལ་ཡ་རབས་ཚུལ་བཞིན་ཞེས་བྱ་བ་ཉིད་ནི་རྒྱལ་པོ་ཆེན་པོ་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 4764]
སྐྱེ་བོ་དགེ་བའི་རང་བཞིན་སྟོན་བྱེད་ཅིང་། །ཞེས་བྱ་བའི་ཚིག་གིས་ནི་སྣད་པར་མ་གྱུར་ཏམ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིག་གིས་སོ། །

[Block 4765]
འདི་ནི་སྐྱེ་བོ་དགེ་བའི་རང་བཞིན་ཏེ། གཞན་སྡུག་བསྔལ་བ་ལ་རང་བཞིན་གྱིས་བརྩེ་བ་ཡིན་ཏེ། སྣད་པར་མ་གྱུར་ཏམ་ཞེས་བྱ་བ་ནི། ལུས་སྣད་པར་མ་གྱུར་ཏམ་ཞེས་བྱ་བའི་དབང་དུ་བྱས་པའོ། །

[Block 4766]
ལུས་ལ་ཆག་གྲུགས༌[^3092]བྱུང་བར་མ་གྱུར་ཏམ། །ཞེས་བྱ་བ་ནི་ཡན་ལག་རྣམས་ཆག་པར་མ་གྱུར་ཏམ་ཞེས་བྱ་བའི་དབང་དུ་བྱས་པའོ། །

[Block 4767]
ཁྱོད་ཀྱི་ནད་རྣམས་རྒྱས་པར་མ་གྱུར་ཏམ། །ཞེས་བྱ་བ་ནི། དེ་གཉི་ག་ལ་གནོད་པར་མ་གྱུར་ཏམ་ཞེས་བྱ་བའི་དབང་དུ་བྱས་པའོ། །

[Block 4768]
དབུགས་འབྱིན་འགྱུར་བ་འཇམ་པ་ཞེས་བྱ་བའི་དབང་དུ་བྱས་ནས། ། མིའི་རྒྱལ་པོ་བདག་ནི་གཞན་མ་ལགས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 4769]
ཡིད་ཆེས་པར་མི་འགྱུར་བ་ནི་རྣམ་པ་གཉིས་ཏེ། རི་དགས་མིའི་ཚིག་ཏུ་སྨྲ་བ་ཐོས་ཤིང་མི་མ་ཡིན་པར་ཤེས་པ་དང་། བདག་ཉིད་ཀྱིས་གནོད་པ་བྱས་པས་སོ། །

[Block 4770]
དེས་ནི་ཡིད་མི་ཆེས་པར་འགྱུར་བའི་རྒྱུ་གཉིས་པ་དེ་མེད་པར་སྟོན་ཏོ། །

[Block 4771]
ཚིགས་བཅད་གཉིས་ཀྱི་ཕྱེད་ཕྱེད་ཀྱིས༌[^3093]གོ་རིམས་བཞིན་དུ་གཅིག་ལ་གཅིག་ཕན་པ༌[^3094]བྱེད་པར་སྟོན་པའི་མཚན་ཉིད་འཇམ་པ་ནི་གཉེན་དུ་འབྲེལ་པ་ལྟ་བུའི་ཚིག་གི་མཚན་ཉིད་ཡིན་པའོ། །

[Block 4772]
ཡང་ན།

[Block 4773 [VERSE]]
ཞེ༌[^3095]སར་བཅས་ཤིང་ཡིད་དུ་འོང་བ་ཡིས། །
[^3096]ཞེས་བྱ་བ་འཇམ་པའི་དབང་དུ་བྱས་པ་སྟེ།
གཡང་སར་ལྷུང་བས་མི་དགེས་མ་མཛད་ཅིག །

[Block 4774]
ཅེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་ཏེ། ཕན་པ་བྱེད་པའི་མཚན་ཉིད་ནི་འཇམ་པར་སྟོན་པ་ཡིན་ནོ། །

[Block 4775 [VERSE]]
བདག་ལ་ཐུགས་ཆེས་རུང་བར་དགོངས་ནས་ནི། །
ཞེས་བྱ་བ་ནི་ཞེ་སར་བཅས་པ་ཉིད་དོ། །
བདག་ནི་མཆི༌[^3097]ཡིས་མྱུར་དུ་བཀའ་སྩོལ་ཅིག །

[Block 4776]
ཅེས་བྱ་བ་ནི་ཡིད་དུ་འོང་བ་སྟེ་འཇམ་པའོ། །

[Block 4777]
ངོ་མཚར་ཆེ་བ་དེས་ཞེས་བྱ་བ་ནི། སྨྲས་པའི་མཚན་ཉིད་དག་གིས་སོ། །

[Block 4778]
ཡ་མཚན་དུ་གྱུར་ཅིང་སེམས་མགུ་ཞེས་བྱ་བ་ལ། དེའི་རྒྱུ་བསྟན་པའི་ཕྱིར། དགྲ་ལ་བརྒལ་བར་ནུས་བཞིན་དུ། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཀྱི་ཕྱེད་ཀྱིས་བསྟན་ཏོ། །

[Block 4779 [VERSE]]
བདག་ལ་ཇི་ལྟར་སྙིང་རྗེ་སྐྱེས། །
ཞེས་བྱ་བ་དེ་བསྒྲུབ་པའི་ཕྱིར།
བདག་གིས་གནོད་པ་བྱས་པའང་ཤེས། །

[Block 4780]
ཞེས་བྱ་བ་ཕྱེད་འོག་མ་ཡིན་ནོ། །

[Block 4781]
ཚིགས་བཅད་འདི་བསྒྲུབ་པའི་ཕྱིར། ཨེ་མའོ་འཇམ་ཞིང་རྣོ་བ༌[^3098]ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་སྨོས་ཏེ། སྔར་བཤད་པ་ནི་བསྒྲུབ་པར་བྱ་བ་ཡིན་ཏེ། སྔར་བཤད་པའི་ཚིགས་བཅད་ཀྱི་ཕྱེད་དང་པོ་ནི་འདིའི་དང་པོ་ཕྱེད་ཀྱིས༌[^3099]སྒྲུབ་པ་ཡིན་ནོ། །

[Block 4782]
དེའི་གཉིས་པ་ནི་གཉིས་པའི་འོ། །

[Block 4783]
འཇམ་ཞིང་རྣོ་བ་ཞེས་བྱ་བ་ནི་འཇམ་པའི་ལས་ནི་སྙིང་རྗེས་སྒྲུབ་པའོ། །

[Block 4784]
རྣོ་བའི་ལས་ནི། དགྲ་ལ་བརྒལ་བར་ནུས་བཞིན་དུ། །ཞེས་བྱ་བ་སྟེ། བདག་ལ་ཡང་དག་པར་ལྡན་པའི་ཕྱིར་རམ། བདག་གི་སྙིང་ལ་ཕྱི་ནས་འགྱོད་པའི་ཕྱིར་རོ། །

[Block 4785]
བདག་ཉིད་ནི་ཕྱུགས་སམ་རི་དགས་ཡིན་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། སྐྱོན་མེད་པ་ལ་གནོད་པ་བྱས་པས་སོ། །

[Block 4786]
རི་དགས་གཟུགས་ཅན་འདི་ནི་གཞན། །ཞེས་བྱ་བ་ནི་དགྲ་ལ་བརྒལ་བར་ནུས་བཞིན་དུ་སྙིང་རྗེས་སྒྲུབ་པ་སྟེ། དེ་ནི་དགྲ་ལ་བརྒལ་བར་ནུས་བཞིན་དུ་བདག་ལ་སྙིང་རྗེ་སྒྲུབ་པས་སོ། །

[Block 4787]
འཐབ་བེར༌[^3100]སྟུག་པོ་དགོས་པས༌[^3101]ན། །ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་ནི་རྒྱལ་པོ་ཆེན་པོ༌[^3102]སྣད་པར་མ་གྱུར་ཏམ། །ཞེས་བྱ་བ་དེའི་ལན་ཡིན་ནོ། །

[Block 4788]
གཡང་ས་ནས་ནི༌[^3103]ལྷུང་བ་ཡིས། །ཞེས་བྱ་བ་ནི་འདི་ལྷག་པར་མི་ཆེའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4789]
སྡུག་བསྔལ་གཞན་དག་ནི་བཟོད་པ་ཉིད་དུ་བསྟན་པའི་ཕྱིར། གཡང་ས་ནས་ནི༌[^3104]ལྷུང་བ་ཡིས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 4790]
ཁྱོད་དེ་ལྟར་དགེ་བར་སེམས་པ་ཞེས་བྱ་བ་ནི་བརྒལ་བར་ནུས་ཀྱང་། སྙིང་རྗེ་དང་ལྡན་པའི་ཕྱིར་དགེ་བར་སེམས་པའོ། །

[Block 4791]
ཉེས་པའི་རྒྱུ་བསྟན་པའི་ཕྱིར། གཟུགས་ཀྱི་རྐྱེན་གྱིས་རི་དགས་ལྟར། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 4792]
གཟུགས་ཀྱི་རྐྱེན་གྱིས་ཞེས་བྱ་བ་ནི་གཟུགས་ཉིད་ཀྱི་རྐྱེན་ནོ། །

[Block 4793]
དེའི་དྲུང་དུ་འོངས་ཏེ་བྱ་བ་ནི་ཐད་དུ་ལྷགས་པའོ། །

[Block 4794]
དེ་བས་ན་རང་བཞིན་གྱིས་དེ་ལྟར་དགེ་བའི་བློ་དང་། བསམ་པ་ཁྱད་པར་ཅན་ཉིད་ཡིན་ནོ། །

[Block 4795]
དགྱེས་པ་ཞེས་བྱ་བ་ནི་མངོན་པར་འདོད་པའི་དོན་གྲུབ༌[^3105]པའོ། །

[Block 4796]
དང་བ་ནི་དེའི་ཚེ་བདག་གིས་ཕྱུང་བར་རོ། །

[Block 4797]
དགྱེས་པ༌[^3106]དང་། དང་བ་དག་ནི། དགྱེས་པ༌[^3107]དང་དང་བ་དག་གོ། །

[Block 4798]
དེ་གཉིས་ཀྱིས་ཞལ་མངོན་དུ་ཕྱོགས་པ་ནི། དགྱེས་བཞིན༌[^3108]དང་བའི་ཞལ་གྱིས་མངོན་དུ་ཕྱོགས་པའོ། །

[Block 4799]
ཡང་ན་དགྱེས་ཤིང་དགའ་བས་ཞལ་མངོན་དུ་ཕྱོགས་པ་ནི།

[Block 4800 [VERSE]]
དགྱེས་ཤིང་དགའ་བས་ཞལ་མངོན་དུ་ཕྱོགས་པའོ། །
བདག་གི་སྲོག་ཀྱང་རི་དགས་ཁྱོད་དབང་ན། །
--- END BLOCKS ---
