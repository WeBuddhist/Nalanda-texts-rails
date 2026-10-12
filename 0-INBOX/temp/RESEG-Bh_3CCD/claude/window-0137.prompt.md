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

[Block 4801]
ཇི་སྐད་དུ།

[Block 4802 [VERSE]]
ཐུང་དང་རིང་དང་འཕར་མ་དང་། །
དབྱངས་ནི་གསུམ་པོ་དང་སྦྱར་དང་། །
སྣ་རྗེས་འགྲོ་བའི་མེད་པ་ཡིས། །
[^2873]གྲངས་སུ་རྣམ་པ་བཅོ་བརྒྱད་ཡིན། །

[Block 4803]
ཞེས་འབྱུང་ངོ་། །དེ་ལྟར་གྱུར་པའི་ཡི་གེ་ཨའི་འབྲེལ་པ་དང་ལྡན་པའི་ཕྲེང་བ་ནི་ཨཱ་ལི་ཞེས་བྱའོ། །

[Block 4804]
དེ་བཞིན་དུ་ཀའི་འབྲེལ་པ་དང་ལྡན་པའི་ཕྲེང་བ་ནི་ཀཱ་ལི་ཞེས་བྱའོ། །

[Block 4805]
ཨཱ་ལི་དང་ཀཱ་ལི་དེ་དག་ཡི་གེ་བཞི་བཅུ་རྩ་དགུའི་ཡི་གེ་ནི་ཕྱི་མོའི་རང་བཞིན་ནོ། །

[Block 4806]
མ་ནིང་ལ་སོགས་པའི་གཟུགས་ཅན་རྣམས་ནི་ཞེས་པ་ནི་དེ་ལ་བུད་མེད་ཀྱི་རང་བཞིན་ནི་ཡི་གེ་ཨ་ལ་སོགས་པ་སྟེ། ཤེས་རབ་ཀྱི་ངོ་བོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4807]
ཕོ་རྟགས་ཀྱི་རང་བཞིན་ནི་ཀ་ལ་སོགས་པ་སྟེ། ཐབས་ཀྱི་ངོ་བོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4808]
གཉིས་ཀ་དང་སྙོམས་པར་ཞུགས་པའི་རང་བཞིན་ཡ་ལ་སོགས་པ་སྟེ་མ་ནིང་གི༌[^2874]རྟགས་ཀྱི་ངོ་བོར་ཤེས་པར་བྱའོ། །

[Block 4809]
ཡི་གེ་གསུམ་དུ་ཞུགས་པས་མོ་རྟགས་ལ་སོགས་པའི་རང་བཞིན་གྱི་ཨ་ལ་སོགས་པ་དེ་རྣམས་སྐུ་གསུང་ཐུགས་ཀྱི་བདག་ཉིད་ཀྱི་ཡི་གེ་གསུམ་ལ་བསྡུས་པའི་ཕྱིར་རོ། །

[Block 4810]
ད་ནི་འདི་ལྟར་དཔྱད་པར་བྱ་སྟེ། མོ་རྟགས་དང་ཕོ་རྟགས་དང་མ་ནིང་གི་རྟགས་ནི་ཇི་ལྟ་བུ་ཡིན་ཞེ་ན། དེ་ལ་ཁ་ཅིག་ན་རེ། ནུ་མ་སྐྲ་ཅན་བུད་མེད་ཡིན།

[Block 4811 [VERSE]]
ཁ་སྤུ་དང་ལྡན་སྐྱེས་པར་བཤད། །
གང་ཞིག་གཉིས་ཀ་ལས་འདས་པའི། །

[Block 4812]
དེ་ནི་མ་ནིང་བཤད་པ་ཡིན། ཞེས་ཟེར་རོ། །

[Block 4813]
དེ་ཡང་མི་རིགས་ཏེ། གལ་ཏེ་ནུ་མ་དང་སྐྲ་ཅན་མོ་རྟགས་ཡིན་ན། དེའི་ཚེ་ཕྲེང་བ་དང་ཉལ་ཁྲི་ལ་སོགས་པ་དག་མོ་རྟགས་སུ་མི་འགྱུར་ཏེ། དེ་རྣམས་ནུ་མ་དང་སྐྲར་མི་ལྡན་པའི་ཕྱིར་རོ། །

[Block 4814]
འབྲེག་པའི་སྐྲ་དང་ལྡན་པའི་ས་ཕྱོགས་དག་ཀྱང་མོ་རྟགས་སུ་འགྱུར་རོ། །

[Block 4815]
སྦྱར་བའི་ནུ་མ་དང་སྐྲའི་ཆ་ལུགས་འཛིན་པའི་གར་མཁན་སྐྱེས་པ་ཡང་མོ་རྟགས་ཉིད་དུ་ཐལ་བར་འགྱུར་རོ། །

[Block 4816]
དེ་བཞིན་དུ། ཁ་སྤུ་དང་ལྡན་པ་ཕོ་རྟགས་ཡིན་ན་སྒོག་པ་ལ་སོགས་པ་ཡང་དེ་ཉིད་དུ་ཐལ་བར་འགྱུར་ཏེ། དེ་རྣམས་ནི་སྒྲའི་གཟུགས་ལ་ལྟོས་པས་མ་ནིང་གི་རྟགས་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4817]
གནས་ལ་སོགས་པ་གནས་པའི་རྣལ་འབྱོར་མ་རྣམས་ཁ་སྤུ་དང་ལྡན་པས་ཕོ་རྟགས་སུ་འགྱུར་བ་དང་། སྐྱེས་པ་ཁ་ཅིག་ཁ་སྤུ༌[^2875]དང་མི་ལྡན་པས་མོ་རྟགས་སུ་ཐལ་བར་འགྱུར་རོ། །

[Block 4818]
དེ་ཡང་མི་འཐད་དེ། གཉིས་ཀའི་རང་བཞིན་གྱི་རྟགས་མ་ནིང་ཡིན་ན་ས་ལ་སོགས་པ་རྣམས་ཀྱང་མ་ནིང་ཉིད་དུ་ཐལ་བར་འགྱུར་རོ། །

[Block 4819]
དེ་ཡང་མི་འཐད་དེ། དེ་རྣམས་མོ་རྟགས་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4820]
གཞན་ན་རེ་འཕེལ་བ་དང་འགྲིབ་པ་དང་། བར་མ་ནི་ཕོ་རྟགས་ལ་སོགས་པའི་མཚན་ཉིད་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 4821]
དེ་ལ་འཕེལ་བ་ནི་ནུས་པ་དང་པོ་དང་ལྡན་པའོ། །

[Block 4822]
འགྲིབ་པ་ནི་ནུས་པ་ཆུང་བ་དང་ལྡན་པའོ། །

[Block 4823]
བར་མ་ནི་ནུས་པ་བར་མ་དང་ལྡན་པའོ་ཞེ༌[^2876]ན། དེ་ཡང་མ་ཡིན་ཏེ། གང་གི་ཕྱིར་གལ་ཏེ་འགྲིབ་པ་ནི་མོ་རྟགས་ཀྱི་མཚན་ཉིད་ཡིན་ན་དེའི་ཚེ་བུ་མོ་སྐྱེ་ན་དེའི་ཚེ་ནུས་པ་འཕེལ་བས་ཕོ་རྟགས་སུ་ཐལ་བར་འགྱུར་རོ། །

[Block 4824]
དེ་ཡང་མི་འཐད་དེ། དེ་བཞིན་དུ་འཕེལ་བ་ཞེས་བྱ་བ་ཕོ་རྟགས་ཀྱི་མཚན་ཉིད་ཡིན་ན་དེའི་ཚེ་སྐྱེས་བུ་རྒས་པས་དེའི་ནུས་པ་འགྲིབ་པར་འགྱུར་ན་མོ་རྟགས་སུ་ཐལ་བར་འགྱུར་རོ། །

[Block 4825]
དེ་ཡང་མི་འཐད་དེ། [^2877]སྐྱེས་པ་དང་མ་བྲལ་བའི་ཕྱིར་རོ། །

[Block 4826]
ནུས་པ་བར་མ་མ་ནིང་གི་རྟགས་ཀྱི་མཚན་ཉིད་ཡིན་ན་དེའི་ཚེ་སྐྱེས་པའམ་བུད་མེད་ནུས་པ་བར་མ་དང་ལྡན་པས་མ་ནིང་ཉིད་དུ་ཐལ་བར་འགྱུར་རོ། །

[Block 4827]
དེ་བས་ན་མཚན་ཉིད་དེ་དག་ནི་མ་ངེས་པ་ཡིན་ནོ། །

[Block 4828]
ཁ་ཅིག་ན་རེ་སྐད་རགས་པ་ལ་སོགས་པ་ཕོ་རྟགས་ཀྱི་མཚན་ཉིད་ཡིན་ལ། །སྐད་ཕྲ་བ་ལ་སོགས་པ༌[^2878]ནི་མོ་རྟགས་ཀྱི་མཚན་ཉིད་ཡིན་ནོ། །

[Block 4829]
དེ་དག་མེད་ན་ནི་མ་ནིང་གི་མཚན་ཉིད་ཡིན་ནོ་ཞེ་ན། དེ་ཡང་མ་ཡིན་ཏེ། གལ་ཏེ་སྐད་རགས་པ་ལ་སོགས་པ་ཕོ་རྟགས་ཀྱི་མཚན་ཉིད་ཡིན་ན། དེའི་ཚེ་མཛེས་ཟིན་པའི་སྐྱེས་པ་རྣམས་སྐད་ཕྲ་བ་ཡིན་པས་མོ་རྟགས་སུ་ཐལ་བར་འགྱུར་བ་དང་། དབྱངས་རགས་པའི་མོ་རྣམས་ཀྱང་ཕོ་རྟགས་སུ་ཐལ་བར་འགྱུར་རོ། །

[Block 4830]
གཉིས་ཀ་མེད་པ་མ་ནིང་ཡིན་ན་ཕྲེང་བ་དང་ཉལ་ཁྲི་ལ་སོགས་པ་མ་ནིང་དུ་ཐལ་བར་འགྱུར་རོ། །

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
--- END BLOCKS ---
