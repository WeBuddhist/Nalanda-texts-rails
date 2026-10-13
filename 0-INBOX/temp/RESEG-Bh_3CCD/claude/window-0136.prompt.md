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
དེ་རྣམས་ཀྱང་ཨ་ལ་སོགས་པ་དང་པོའི་ཡི་གེ་རྣམས་ལ་བསྡུ་བར་འགྱུར་རོ། །

[Block 4762]
དེ་རྣམས་ཀྱང་ཨ་ཀ་ཡ་ཤའི་ཡི་གེ་བཞི་པོ་ལ་ཐིམ་པར་འགྱུར་ཏེ། ཁམས་བཞིའི་རང་བཞིན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4763]
ཡི་གེ་བཞི་པོ་ཡང་ཨ་ཀ་ཡ་ཡི་གེ་གསུམ་ལ་ཐིམ་པར་གྱུར་ཏོ། །

[Block 4764]
དེ་རྣམས་ལས་ཤེས་རབ་ཀྱི་རང་བཞིན་ཡི་གེ་ཨ་ཡོངས་སུ་གྱུར་པ་འོད་དཔག་ཏུ་མེད་པའི་རང་བཞིན་གྱི་ཡི་གེ་ཨ་འགྱུར་ཏེ། དབྱངས་ཀྱི་སྡེ་ཚན་ནི་མོ་རྟགས་ཡིན་པས་སོ། །

[Block 4765]
ཐབས་ཀྱི་རང་བཞིན་ཡི་གེ་ཀ་ཡོངས་སུ་གྱུར་པ་ལས་ཧཱུྃ་བྱུང་བར་གྱུར་ཏེ། དེ་ནི་ཕོ་རྟགས་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4766]
གཉིས་ཀའི་རང་བཞིན་གྱི་ཡི་གེ་ཡ་ཡོངས་སུ་གྱུར་པ་ལས་ཡི་གེ་ཨོཾ་བྱུང་བར་གྱུར་ཏེ། དེ་ནི་མ་ནིང་གི་རྟགས་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4767]
དེ་ལྟར་ཡི་གེ་ཨོཾ་ཨཱཿཧཱུྃ་ཡི་གེ་གསུམ་པོ་ནི་སྐུ་གསུང་ཐུགས་ལ་སོགས་པའི་རང་བཞིན་དུ་ཤེས་པར་བྱའོ། །

[Block 4768]
དགོངས་པ་ལུང་བསྟན་པའི་རྣལ་འབྱོར་ཆེན་པོའི་རྒྱུད་ལས་ཀྱང་། །

[Block 4769 [VERSE]]
དང་པོ་གཅིག་ནི་དགུ་དབུས་ན། །
གང་ཞིག་བཅུ་ཡིས་མ་བཅིངས་པ། །
དེ་ནི་བཅིངས་མེད་ཅེས་བྱ་སྟེ། །
དེ་ཡིས༌[^2858]མཆོག་གི༌[^2859]གནས་ཤེས་སོ། །

[Block 4770 [VERSE]]
དབྱངས་དང་གསལ་བྱེད་ཡི་གེ་སྟེ། །
གྲངས་དགུ་རུ་ནི་རྗེས་འཇུག་པ། །
ཨས་བཅིངས་ཕན་ཚུན་ཡང་དག་སྦྱོར། །
གང་གིས་ཤེས་ཏེ་འགྲོ་བའི་བླ། །

[Block 4771 [VERSE]]
འབྱུང་བའི་མཐའ་དང་ཡང་དག་ལྡན། །
ཚ༌[^2860]ལ་སོགས་པ་བཅུ་དྲུག་གནས། །
ལྔ་པ་ལྔ་དང་ཡང་དག་ལྡན། །
བཞི་ནི་གསུམ་དུ་ངེས་པར་སྦྱར། །

[Block 4772 [VERSE]]
ཡི་གེ་ཨོཾ་བཅས་རིང་པོར༌[^2861]བཅས། །
ཡོན་ཏན་སྦྱོར་སོགས་ཕྱིས་དང་མཚུངས། །
ཐུང་ངུ་མ་ལུས་དག་ཏུ་འགྱུར། །
གཅིག་མིན་དུ་མའང་མ་ཡིན་ནོ། །

[Block 4773 [VERSE]]
དྲུག་བཤད་བཞི་དང་གསུམ་གཅིག་དང་། །
ངོ་བོ་ཉིད་མེད་རང་བཞིན་ཅན། །
དེ་དག་དང་པོའི་དོན་སྦྱར་ནས།[^2862] །
དུས་གསུམ་ཡེ་ཤེས་སྐྱེ་བར་འགྱུར། །

[Block 4774]
ཞེས་བྱ་བ་ལ་སོགས་པ་འབྱུང་ངོ་། །ཡི་གེ་གསུམ་པོ་དེ་དག་འཇུག་པ་ལ་སོགས་པའི་རིམ་གྱིས་ཉིན་མཚན་ཏུ་སྟོང་ཕྲག་ཉི་ཤུ་རྩ་གཅིག་དང་དྲུག་བརྒྱའི་རླུང་རྣམས་རྒྱུའོ། །

[Block 4775]
དེ་ཉིད་ཡན་ལག་མ་ཉམས་པའི་བཟླས་པས་ངག་རྣམ་པར་དག་པ་བྱེད་དེ། །དེ་ཉིད་ཆ་ཤས་སུ་ཐིམ་པས་མ་ནིང་གི་བཟླས་པའི་མཐར་འོད་གསལ་བ་ཉིད་ཐོབ་པར་བྱེད་དོ། །

[Block 4776]
དེ་ཉིད་ཁྲོ་བོའི་བཟླས་པའི་དུས་སུ་བཟླས་པར་གྱུར་པས་ཞི་བ་ལ་སོགས་པའི་ལས་བྱེད་པར་འགྱུར་རོ། །

[Block 4777]
དེ་ཉིད་ཀྱིས་ཀྱང་བསྐྱེད་པའི་རིམ་པའི་རྣལ་འབྱོར་པ་རྣམས་ལ་རྡོ་རྗེ་ལ་སོགས་པ་ཡོངས་སུ་གྱུར་པ་ལས་ལྷའི་སྐུ་ཡོངས་སུ་རྫོགས་པར་བྱེད་དོ། །

[Block 4778]
དེ་ཉིད་ཀྱིས་ཀྱང་དེ་བཞིན་གཤེགས་པའི་ཐུགས་བསྐུལ་བའི་སྒོ་ནས་དེ་རྣམས་ཀྱི་ནུས་པ་འགུགས་པར་བྱེད་དོ། །

[Block 4779]
དེ་ཉིད་གྱེན་དུ་རྒྱུ་བས་སྔགས་ཐམས་ཅད་ཀྱི་རྒྱུར་གྱུར་པའི་ཨཱ་ལི༌[^2863]དང་ཀཱ་ལིའི་ཚུལ་དུ་རྣམ་པར་འཇུག་གོ། །

[Block 4780]
དེ་ཉིད་ཐབས་དང་ཤེས་རབ་ཀྱི་སྙོམས་པར་ཞུགས་པས་ཐུར་དུ་རྒྱུ་བ་ཅན་ཁུ་བ་དང་ཁྲག་དང་ཆུའི་ངོ་བོ་ཉིད་རིན་ཆེན་འབྱུང་ལྡན་དང་སྣང་བ་མཐའ་ཡས་དང་མི་བསྐྱོད་པའི་གཟུགས་སུ་རྗེས་སུ་འཇུག་གོ། །

[Block 4781]
དེ་ཉིད་ཆོས་འབྱུང་བའི་ནང་དུ་སྤྲོས་པས་བུ་དང་ཚ་བོ་ལ་སོགས་པའི༌[^2864]ཚུལ་དུ་ཁམས་གསུམ་པ་དང་དེའི་རྣམ་པར་དག་པའི་ངོ་བོ་ཉིད་དཀྱིལ་འཁོར་གྱི་འཁོར་ལོ་ཡང་སྐྱེད་པར་བྱེད་དོ། །

[Block 4782]
མཐའ་མར་འོད་གསལ་བ་ལ་ཞུགས་ནས་རྡོ་རྗེ་འཆང་ཆེན་པོའི་གོ་འཕང་ཐོབ་པར་བྱེད་དོ། །

[Block 4783]
དེའི་ཕྱིར༌[^2865]ཁམས་གསུམ་ཁྱབ་པར་བྱེད་པ་ལ༌[^2866]ལོངས་སྤྱོད་དང་གྲོལ་བའི་འབྲས་བུ་སྟེར་བ་རྣམ་པར་སྣང་མཛད་ལ་སོགས་པ་དེ་བཞིན་གཤེགས་པ་གསུམ་གྱི་བདག་ཉིད་ཡི་གེ་གསུམ་པོ་ཁོ་ན་སྔགས་ཐམས་ཅད་ཀྱི་ཚུལ་དུ་གྲགས་པས་ཚོགས་ཞེས་བཤད་དོ། །

[Block 4784]
དེ་བས་ན་སྔགས་བཏུ་བ་ལ་སོགས་པ་བཞི་པོ་གོང་དུ་བཤད་པ་གང་ཡིན་པ་དེ་དག་ཡི་གེ་གསུམ་པོ་ཁོ་ན་ལ་བརྟེན་ཏེ་བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་སོ། །

[Block 4785]
ཇི་སྐད་དུ།

[Block 4786 [VERSE]]
བརྗོད་དང་དམིགས་པར་གྲགས་པ་དང་། །
བརྡར་གྱུར་དང་ནི་དོན་དམ་མོ། །
ཚིག་གི་བརྗོད་པ་ཐུན་མོང་སྟེ། །
དམིགས་པར་བཅས་པ་སངས་རྒྱས་ཉིད། །

[Block 4787 [VERSE]]
སྔགས་ཀྱི་དེ་ཉིད་བརྡ་རུ་བཤད། །
དོན་དམ་དེ་བཞིན་ཉིད་ཡིན་ནོ། །

[Block 4788]
ཞེས་འབྱུང་ངོ་། །གཏན་ཚིགས་བཤད་པར་བྱ་བའི་ཕྱིར་ཨཱ་ལི༌[^2867]ཀཱ་ལི་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། ཨ་ལ་སོགས་པའི་ཕྲེང་བ་ནི་ཨཱ་ལིའོ། །

[Block 4789]
ཨ་ལ་སོགས་པ་དབྱངས་ཀྱི་ཡི་གེ་བཅུ་དྲུག་ཟླ་བའི་ཆའི་ངོ་བོ་ཉིད་གང་ཡིན་པ་དེ་རྣམས་ཀྱི་རྩ་བ་ནི་ཨ་ཉིད་དོ། །

[Block 4790]
ཇི་སྐད་དུ།

[Block 4791 [VERSE]]
སྙིང་གི་དཀྱིལ་ནི༌[^2868]མི་ཤིགས་པའི། །
འབར་བའི་མར་མེ་ལྟ་བུ་ནི། །
ཡི་གེ་དམ་པ་ཕྲ་བ་ནི། །
ཨ་ཡིག་གསལ་བའི་གཙོ་བོར་གནས། །

[Block 4792]
ཞེས་འབྱུང་ངོ་། །དབྱངས་ཡིག་གི་ཕྲེང་བ་དེ་ཉིད་ཐབས་དང་ཤེས་རབ་ཉིས་འགྱུར་དུ་བྱས་ཏེ་མཚན་བཟང་པོ་སུམ་ཅུ་རྩ་གཉིས་ཀྱི་ངོ་བོ་ཉིད་དུ་འགྱུར་རོ། །

[Block 4793]
དེ་ཉིད་ཚེག་དྲག་དང་རྗེས་སུ་འཇུག་པའི་དབྱངས་དང་ལྕེའི་རྩ་བའི་ཡི་གེ་དང་བུང་བའི་ཡི་གེ་དང་རྗེས་སུ༌[^2869]དབྱངས་དང་བཅས་པའི་མཐར་གནས་པའི་ཡི་གེ་གསུམ་དང་བཅས་པར་གསལ་བྱ་སུམ་ཅུ་རྩ་གསུམ་ཉིས་འགྱུར་གྱིས་དཔེ་བྱད་བརྒྱད་ཅུའི་རང་བཞིན་དུ་འགྱུར་རོ། །

[Block 4794]
དེ་ཉིད་ཐུང་ངུ་ལྔའི་བདག་ཉིད་ཀྱིས་ཕུང་པོ་ལྔའི་ངོ་བོ་ཉིད་ཡེ་ཤེས་ལྔའི་མཚན་ཉིད་ཅན་ཐབས་ཀྱི་རང་བཞིན་དེ་བཞིན་གཤེགས་པ་ལྔའི་བདག་ཉིད་དུ་འགྱུར་རོ། །

[Block 4795]
དེ་ཉིད་རིང་པོ་ལྔ་དང་འབྲེལ་པའི་ཡི་གེ་བཞིའི་ཚུལ་གྱིས་ཤེས་རབ་ཀྱི་རང་བཞིན་གྱི་སངས་རྒྱས་སྤྱན་མ་ལ་སོགས་པའི་ཡུམ་བཞི་དང་གཟུགས་རྡོ་རྗེ་མ་ལ་སོགས་པ་མཆོད་པའི་ལྷ་མོ་ལྔར་ཤེས་པར་བྱའོ། །

[Block 4796]
མ་ནིང་གི་ཡི་གེ་བཞི་ཡོངས་སུ་སྤངས་ནས་དབྱངས་བཅུ་གཉིས་ཀྱི་ཚུལ་དུ་ཕྱི་དང་ནང་གི་སྐྱེ་མཆེད་ཀྱི་རང་བཞིན་དུ་འགྱུར་རོ། །

[Block 4797]
ཐུང་བ་དང་རིང་བ་གཉིས༌[^2870]ཀྱི་ཚུལ་དུ་འབྲེལ་པའི་ཡི་གེ་བཞི་དང་ལྷན་ཅིག་སྤྱན་མ་ལ་སོགས་པས་འཁྱུད་པ་དེ་བཞིན་གཤེགས་པ་ལྔ་དང་གཤིན་རྗེ་མཐར་བྱེད་ལ་སོགས་པའི་ཁྲོ་བོ་བཞི་སྟེ་བཅུ་གསུམ་གྱི་བདག་ཉིད་ཅན་གྱི་དཀྱིལ་འཁོར་གྱི་འཁོར་ལོའི་རང་བཞིན་ཉིད་དུ་འགྱུར་རོ། །

[Block 4798]
དེ་ཉིད་ཀ་ལ་སོགས་པའི་ཡི་གེ་ལྔ་ལྔ་པའི་སྡེ་ཚན་ལྔའི་རང་བཞིན་གྱི་ལྷ་མོ་བཞིས་ཡོངས་སུ་བསྐོར་བའི་དེ་བཞིན་གཤེགས་པ་ལྔའི༌[^2871]དཀྱིལ་འཁོར་ལྔ་མཐར་གནས་པ་དང་དྲོད་ཀྱི་ཡི་གེ་དང་ཚེག༌[^2872]དྲག་དང་རྗེས་སུ་འཇུག་པའི་དབྱངས་དང་ལྷན་ཅིག་ཏུ་ཁྲོ་བོའི་རྒྱལ་པོ་བཅུས་བསྐོར་བའི་དཀྱིལ་འཁོར་གྱི་འཁོར་ལོ་ཉིད་དུ་འགྱུར་རོ། །

[Block 4799]
དེ་ནི་ཐུང་བ་དང་རིང་བ་དང་འཕར་བའི་དབྱེ་བས་རྣམ་པ་བཅོ་བརྒྱད་ཀྱི་ཚུལ་གྱིས་ཁམས་བཅོ་བརྒྱད་ཀྱི་ངོ་བོ་ཉིད་དུ་འགྱུར་རོ། །

[Block 4800]
དེ་ལ་ཐུང་བ་དང་རིང་བ་དང་འཕར་བ་སྟེ་རེ་རེ་ལ་རྗེས་སུ་འཇུག་པའི་དབྱངས་དང་བཅས་པ་དང་རྗེས་སུ་འཇུག་པའི་དབྱངས་མེད་པ་དང་མཐོ་བ་དང་དམའ་བ་དང་བར་མའོ། །
--- END BLOCKS ---
