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
[Block 4831]
དེ་ཡང་མི་འཐད་དེ། དེ་རྣམས་མོ་རྟགས་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4832]
སྐད་རགས་པ་དང་ལྡན་པའི་རྫ་རྔ་ལ་སོགས་པ་ཡང་ཕོ་རྟགས་སུ་ཐལ་བར་འགྱུར་རོ། །

[Block 4833]
དེ་ཡང་མི་འཐད་དེ། མ་ནིང་ཡིན་པས་སོ། །

[Block 4834]
དེ་བས་ན་མཚན་ཉིད་དེ་ཡང་མ་ངེས་པའོ། །

[Block 4835]
བུ་ཆུང་ཆགས་པ་ལ་སོགས་པ་ཡང་མོ་རྟགས་ཀྱི་མཚན་ཉིད་དུ་མི་རིགས་ཏེ། མོ་བཤམ་ལ་དེ་མེད་པས་སྐྱེས་པ༌[^2879]ཉིད་དུ་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །ཤེས་རབ་དང་ལྡན་པ་ཕོ་རྟགས་ཀྱི་མཚན་ཉིད་དུ་མི་རིགས་ཏེ། དེ་དང་ལྡན་པའི་མོ་རྣམས་ཀྱང་སྐྱེས་པ་ཉིད་དུ་ཐལ་བར་འགྱུར་རོ། །

[Block 4836]
ཆགས་པའི་ཆ་ཆེ་བ་དང་ཆུང་བས་མོ་རྟགས་དང་ཕོ་རྟགས་ཡིན་ན་དེའི༌[^2880]ཆགས་པ་ཆེ་བའི་སྐྱེས་པ་ཡང་མོ་རྟགས་ཉིད་དུ་ཐལ་བར་འགྱུར་བ་དང་། ཆགས་པ་ཆུང་བའི་བུད་མེད་ཀྱང་སྐྱེས་པ་ཉིད་དུ་ཐལ་བར་འགྱུར་རོ། །

[Block 4837]
དེ་བས་ན་མཚན་ཉིད་དེ་ཡང་མ་ངེས་པའོ། །

[Block 4838]
ཕོའི་དབང་པོ་དང་མོའི་དབང་པོ་དང་ལྡན་པ་ཡང་ཕོ་རྟགས་དང་མོ་རྟགས་ཀྱི་མཚན་ཉིད་དང་ལྡན་པ་མ༌[^2881]ཡིན་ཏེ། །ནང་དུ་ཆུད་པས་ཕོའི་དབང་པོ་མི་མངོན་པའི་སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་མོ་རྟགས་སུ་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 4839]
མོའི་དབང་པོ་དང་ལྡན་པ་ཡང་མོ་རྟགས་མ་ཡིན་ཏེ། མ་ནིང་ལ་དེ་ཡོད་པའི་ཕྱིར་རོ། །

[Block 4840]
དེ་བས་ན་མཚན་ཉིད་དེ་ཡང་མ་ངེས་སོ། །

[Block 4841]
རྟགས་ནི་ཁྱད་པར་མེད་པ་སྟེ། །འཇིག་རྟེན་ལ་བརྟེན་པའི་ཕྱིར་རོ་ཞེས་བྱ་བར་བརྡ་སྤྲོད་པ་རྣམས་ཀྱིས་སྨྲ་བ་དེ་ནི་མ་ཡིན་ཏེ། གལ་ཏེ་འཇིག་རྟེན་ལ་བརྟེན་པའི་རྟགས་ཡིན་ན། དེའི་ཚེ་དངོས་པོ་ཐམས་ཅད་ནི་རྟགས་ཐམས་ཅད་དང་ལྡན་པར་ཐལ་བར་འགྱུར་ཏེ། འགྲམ་དང་ཁང་པ་ལ་སོགས་པའི་སྒྲ་བཞིན་ནོ། །

[Block 4842]
དེ་བས་ན་ཕོ་རྟགས་ལ་སོགས་པའི་མཚན་ཉིད་ནི་རིགས་པས་གྲུབ་པ་མ༌[^2882]ཡིན་ནོ། །

[Block 4843]
འདིར་སྨྲས་པ་ཁྱབ་པར་བྱ་བ་དང་ཁྱབ་པར་བྱེད་པ་དང་གཉིས་ཀ་དང་བྲལ་བ་ནི་ཕོ་རྟགས་དང་མོ་རྟགས་དང་མ་ནིང་གི་རྟགས་ཡིན་ཏེ། གང་གི་ཕྱིར་སྙོམས་པར་ཞུགས་པའི་དུས་སུ་ལྷན་ཅིག་སྐྱེས་པའི་དགའ་བའི་བདེ་བ་ཆེན་པོས་གང་གིས་ཁྱབ་པར་བྱེད་པ་ནི་སེམས་ཀྱི་རྒྱུད་དེའི་རང་བཞིན་དུ་བྱེད་པ་ཁྱབ་པར་བྱེད་པ་དེ་ནི་མོ་རྟགས༌[^2883]ཡིན་ནོ། །

[Block 4844]
བདེ་བ་ཆེན་པོས་ཁྱབ་པར་བྱ་བ་ནི་ཕོ་རྟགས་ཡིན་ནོ། །

[Block 4845]
བདེ་བ་ཆེན་པོས་ཁྱབ་པ༌[^2884]དང་ཁྱབ་པར་བྱེད་པ་མེད་པས་གཉིས་ཀ་དང་བྲལ་བ་ནི་མ་ནིང་གི་རྟགས་ཡིན་ཏེ། སྣོད་ཀྱི་འཇིག་རྟེན་ནོ། །

[Block 4846]
སྣོད་ཀྱི་འཇིག་རྟེན་གྱི་དངོས་པོ་རྣམས་ལ་མོ་རྟགས་ལ་སོགས་པ་གང་ཡོད་པ་དེ་ནི་བརྟགས་པ༌[^2885]བ་ཡིན་ཏེ། དོན་དམ་པར་དེ་མེད་པའི་ཕྱིར་རོ། །

[Block 4847]
དེ་བཞིན་དུ་དབྱངས་ཀྱི་སྡེ་ཚན་ཟླ་བའི་ཆ་བཅུ་དྲུག་གི་རང་བཞིན་གྱིས་གསལ་བྱའི་སྡེ་ཚན་ཁྱབ་པར་བྱེད་པས་ནི་ཚིམ༌[^2886]པར་བྱེད་པ་ཤེས་རབ་ཀྱི་རང་བཞིན་ནི་ཨཱ་ལི་སྟེ་མོ་རྟགས་སོ། །

[Block 4848]
ཁྱབ་པར་བྱ་བ་ནི་དེ་རྣམས་ཀྱིས༌[^2887]བརྗོད་པར་བྱ་བ་དེ་ནི་ཀཱ་ལི་སྟེ་ཐབས་ཀྱི་རང་བཞིན་གྱི༌[^2888]ཕོ་རྟགས་ཡིན་ནོ། །

[Block 4849]
ཁྱབ་པར་བྱ་བ་དང་ཁྱབ་པར་བྱེད་པ་གཉིས་ཀའི་རང་བཞིན་ནི་ཡ་ལ་སོགས་པའི་སྡེ་ཚན་ཏེ་མ་ནིང་གི་རྟགས་སོ། །

[Block 4850]
དེ་ཉིད་ཀྱི་ཕྱིར་མོ་རྟགས་ཀྱི་རང་བཞིན་དབྱངས་ཀྱི་སྡེ་ཚན་ཀྱི་ཐོག་མ་དང་ཐ་མའི་ཡི་གེ་གཉིས་ཡང་དག་པར་སྦྱར་ནས་ཤེས་རབ་ཀྱི་རང་བཞིན་གྱི་ཡི་གེ་ཨ་རུ་འགྱུར་རོ། །

[Block 4851]
ཡི་གེ་ཀ་ལ་སོགས་པ་ཡང་དག་པར་སྦྱོར་བས་ཐབས་ཀྱི་རང་བཞིན་ནི་ཡི་གེ་ཧཱུཾ་སྟེ་ཕོ་རྟགས་ཡིན་ནོ། །

[Block 4852]
ཡ་ལ་སོགས་པ་སྡེ་ཚན་ཡོངས་སུ་གྱུར་པ་ལས་ཡི་གེ་ཨོཾ་དུ་འགྱུར་རོ། །

[Block 4853]
དེ་ལ་ཨ་ཨུ་མ་ཞེས་ཡང་དག་པར་སྦྱོར་བས༌[^2889]ཨོཾ་དུ་འགྱུར་རོ། །

[Block 4854 [VERSE]]
ཡི་གེ་ཨ་ནི་ཤེས་རབ་ཀྱི་རང་བཞིན་ནོ། །
ཡི་གེ་མ་ནི་ཐབས་ཀྱི་རང་བཞིན་ཏེ། །

[Block 4855]
གསལ་བྱ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4856]
ཡི་གེ་ཨོཾ་ནི་དེ་དང་སྦྱོར་བའི་རང་བཞིན་ཏེ་མ་ནིང་ཞེས་བྱའོ། །

[Block 4857]
དེ་ཉིད་ཀྱི་ཕྱིར་ཤེས་རབ་དང་ཐབས་གཉིས་ཀ་ཡང་དག་པར་སྦྱོར་བའི་རང་བཞིན་གྱི་མ་ནིང་གི་རྟགས་སོ། །

[Block 4858]
དེ་ལྟར་ཕོ་རྟགས་དང་མོ་རྟགས་གཉིས་ཀའི་རང་བཞིན་ནི་ཨོཾ་ལ་སོགས་པའི་ཡི་གེ་གསུམ་ཡིན་ནོ། །

[Block 4859]
མཉམ་པར་གཞག༌[^2890]ཅིང་ཞེས་པ་ནི་སྐད་ཀྱི་བྱིངས༌[^2891]དོན་དུ་མ་ཡིན་པའི་ཕྱིར་མཉམ་པར་གཞག་པའི༌[^2892]སྒྲ་ནི་བཟླས་པའི་དོན་ལ་འཇུག་པའོ། །

[Block 4860]
དེ་ཉིན་དང་མཚན་དུ་ལྡང་བ་དང་འཇུག་པ་དང་། གནས་པ་དང་ཞེས་པ་ནི་སྲོག་གི་རླུང་ནང་དུ་ཞུགས་པ་ནི་འཇུག་པའོ། །

[Block 4861]
མེ་དང་མཉམ་པའི་རླུང་བར་དུ་གཞག་པ༌[^2893]ནི་གནས་པའོ། །

[Block 4862]
སྲོག་གི་རླུང་གྱེན་དུ་རྒྱུ་བ་ནི་ལྡང་བ་ཡིན་ནོ། །

[Block 4863]
དེ་བས་ན༌[^2894]རླུང་གི་བྱ་བ་དེ་དག་གསུམ་ནི་འགུགས་པ་དང་། བཞུགས་སུ་གསོལ་བ་དང་། གཤེགས་སུ་གསོལ་བའི་རང་བཞིན་དུ་ཤེས་པར་བྱའོ། །

[Block 4864]
གང་གི་ཕྱིར་ཡི་གེ་ཨོཾ་བརྗོད་པའི་དུས་སུ་ནང་གི་ཚུལ་དུ་རླུང་འཇུག་པར་འགྱུར་རོ། །

[Block 4865]
ཡི་གེ་ཧཱུྃ་བརྗོད་པའི་དུས་སུ་ཕྱིའི་ཚུལ་དུ་རླུང་འབྱུང་བར་མཚོན་པའོ། །

[Block 4866]
ཡི་གེ་ཨ་བརྗོད་པའི་དུས་སུ་རླུང་ནི་བར་ན་གནས་པ་མཚོན་པར་འགྱུར་ཏེ། རླུང་དང་ཡི་གེ་ཐ་མི་དད་པའི་ཕྱིར་རོ། །

[Block 4867]
དེ་ལ་རླུང་རྒྱུ་བས་ཡི་གེ་རྣམས་འབྱུང་བ་ཡིན་ཏེ། ཡི་གེ་བརྗོད་པའི་དུས་སུ་རླུང་ཉིད་ཀྱིས་རྩོལ་བར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 4868]
དེ་བས་ན་བྱ་བ་དང་བྱེད་པའི་འབྲེལ་པའམ་ཕན་གདགས་པར་བྱ་བ་དང་ཕན་འདོགས་པར་བྱེད་པའི་འབྲེལ་པས་རླུང་དང་ཡི་གེ་དབྱེར་མེད་པ་ཡིན་ནོ། །

[Block 4869]
རླུང་གི་ལས་ཀྱི་བདག་ཉིད་ཀྱི་འཇུག་པ་ལ་སོགས་པའི་བྱ་བ་ནི་རླུང་དང་དེའི་བདག་ཉིད་དུ་འཇུག་པས་རླུང་ལས་ཐ་དད་པ་མ་ཡིན་ཏེ། འགྲོ་བ་དང་བསྐུམ་པ་དང་བརྐྱང་བའི་མཚན་ཉིད་དེ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4870]
ཇི་སྐད་དུ། ཡི་གེ་ཨོཾ་གྱི་དབུགས་ནི་ནང་དུ་འཇུག་པ་དང་། ཡི་གེ་ཨའི་སྔགས་ནི་བར་དུ་གནས་པ་དང་། ཡི་གེ་ཧཱུྃ་གི་སྔགས་ནི་ལྡང་བར༌[^2895]གྱུར་པ་སྟེ། རྐན་དང་མཆུ་དག་འབྲེལ་མེད་གསང་སྔགས་བཟླ། །ཞེས་འབྱུང་ངོ་། །
--- END BLOCKS ---
